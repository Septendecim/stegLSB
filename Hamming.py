import LSB
import random

# длина блока кодирования
CHUNK_LENGTH = 8

# проверка длины блока
assert not CHUNK_LENGTH % 8, 'Длина блока должна быть кратна 8'

# вычисление контрольных бит
CHECK_BITS = [i for i in range(1, CHUNK_LENGTH + 1) if not i & (i - 1)]


def chars_to_bin(chars):
    """
    Преобразование символов в бинарный формат
    """
    assert not len(chars) * 8 % CHUNK_LENGTH, 'Длина кодируемых данных должна быть кратна длине блока кодирования'
    return ''.join([bin(ord(c))[2:].zfill(8) for c in chars])


def chunk_iterator(text_bin, chunk_size=CHUNK_LENGTH):
    """
    Поблочный вывод бинарных данных
    """
    for i in range(len(text_bin)):
        if not i % chunk_size:
            yield text_bin[i:i + chunk_size]


def get_check_bits_data(value_bin):
    """
    Получение информации о контрольных битах из бинарного блока данных
    """
    check_bits_count_map = {k: 0 for k in CHECK_BITS}
    for index, value in enumerate(value_bin, 1):
        if int(value):
            bin_char_list = list(bin(index)[2:].zfill(8))
            bin_char_list.reverse()
            for degree in [2 ** int(i) for i, value in enumerate(bin_char_list) if int(value)]:
                check_bits_count_map[degree] += 1
    check_bits_value_map = {}
    for check_bit, count in check_bits_count_map.items():
        check_bits_value_map[check_bit] = 0 if not count % 2 else 1
    return check_bits_value_map


def set_empty_check_bits(value_bin):
    """
    Добавить в бинарный блок "пустые" контрольные биты
    """
    for bit in CHECK_BITS:
        value_bin = value_bin[:bit - 1] + '0' + value_bin[bit - 1:]
    return value_bin


def set_check_bits(value_bin):
    """
    Установить значения контрольных бит
    """
    value_bin = set_empty_check_bits(value_bin)
    check_bits_data = get_check_bits_data(value_bin)
    for check_bit, bit_value in check_bits_data.items():
        value_bin = '{0}{1}{2}'.format(
            value_bin[:check_bit - 1], bit_value, value_bin[check_bit:])
    return value_bin


def get_check_bits(value_bin):
    """
    Получить информацию о контрольных битах из блока бинарных данных
    """
    check_bits = {}
    for index, value in enumerate(value_bin, 1):
        if index in CHECK_BITS:
            check_bits[index] = int(value)
    return check_bits


def exclude_check_bits(value_bin):
    """
    Исключить информацию о контрольных битах из блока бинарных данных
    """
    clean_value_bin = ''
    for index, char_bin in enumerate(list(value_bin), 1):
        if index not in CHECK_BITS:
            clean_value_bin += char_bin

    return clean_value_bin


def set_errors(encoded):
    """
    Допустить ошибку в блоках бинарных данных
    """
    result = ''
    for chunk in chunk_iterator(encoded, CHUNK_LENGTH + len(CHECK_BITS)):
        num_bit = random.randint(1, len(chunk))
        chunk = '{0}{1}{2}'.format(chunk[:num_bit - 1], int(chunk[num_bit - 1]) ^ 1, chunk[num_bit:])
        result += (chunk)
    return result


def check_and_fix_error(encoded_chunk):
    """
    Проверка и исправление ошибки в блоке бинарных данных
    """
    check_bits_encoded = get_check_bits(encoded_chunk)
    check_item = exclude_check_bits(encoded_chunk)
    check_item = set_check_bits(check_item)
    check_bits = get_check_bits(check_item)
    if check_bits_encoded != check_bits:
        invalid_bits = []
        for check_bit_encoded, value in check_bits_encoded.items():
            if check_bits[check_bit_encoded] != value:
                invalid_bits.append(check_bit_encoded)
        num_bit = sum(invalid_bits)
        encoded_chunk = '{0}{1}{2}'.format(
            encoded_chunk[:num_bit - 1],
            int(encoded_chunk[num_bit - 1]) ^ 1,
            encoded_chunk[num_bit:])
    return encoded_chunk


def get_diff_index_list(value_bin1, value_bin2):
    """
    Получить список индексов различающихся битов
    """
    diff_index_list = []
    for index, char_bin_items in enumerate(zip(list(value_bin1), list(value_bin2)), 1):
        if char_bin_items[0] != char_bin_items[1]:
            diff_index_list.append(index)
    return diff_index_list


def encode(source):
    """
    Кодирование данных
    """
    #text_bin = chars_to_bin(source)
    text_bin = source
    result = ''
    for chunk_bin in chunk_iterator(text_bin):
        chunk_bin = set_check_bits(chunk_bin)
        result += chunk_bin
    return result


def decode(encoded, fix_errors=True):
    """
    Декодирование данных
    """
    decoded_value = ''
    fixed_encoded_list = []
    for encoded_chunk in chunk_iterator(encoded, CHUNK_LENGTH + len(CHECK_BITS)):
        if fix_errors:
            encoded_chunk = check_and_fix_error(encoded_chunk)
        fixed_encoded_list.append(encoded_chunk)

    clean_chunk_list = []
    for encoded_chunk in fixed_encoded_list:
        encoded_chunk = exclude_check_bits(encoded_chunk)
        clean_chunk_list.append(encoded_chunk)

    for clean_chunk in clean_chunk_list:
        for clean_char in [clean_chunk[i:i + 8] for i in range(len(clean_chunk)) if not i % 8]:
            #decoded_value += chr(int(clean_char, 2))
            decoded_value += clean_char
    return decoded_value


if __name__ == '__main__':
    #source = input('Укажите текст для кодирования/декодирования:')
    print('Длина блока кодирования: {0}'.format(CHUNK_LENGTH))
    print('Контрольные биты: {0}'.format(CHECK_BITS))
    source = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent semper sagittis iaculis. Nulla facilisis ligula tortor, quis pulvinar mauris condimentum ac. Ut placerat, metus id eleifend varius, nisi sapien tempus sapien, eget elementum dolor magna nec enim. Mauris a ante vehicula, viverra neque ac, tempor nisi. Praesent porta nunc quis nisi pellentesque, sed malesuada justo scelerisque. Fusce fermentum sodales odio sit amet tristique. Praesent scelerisque ex et leo pharetra tempor. Quisque gravida ipsum eget mi convallis, vel interdum felis tempor. Sed imperdiet volutpat lorem. Maecenas aliquam molestie finibus. Pellentesque erat erat, sodales vel eleifend ut, varius ac urna. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. In rhoncus neque sed dignissim molestie. Donec ut eros commodo, tincidunt diam vel, placerat neque. Donec tincidunt egestas quam non bibendum. Ut rhoncus dictum fringilla. Aliquam erat volutpat. Suspendisse egestas tempus tellus egestas augue."
    source = LSB.txtToBitstr(source)
    encoded = encode(source)
    print('\nЗакодированные данные: {0}'.format(encoded))
    decoded = decode(encoded)
    print('\nРезультат декодирования: {0}'.format(LSB.bitstrToText(decoded)))
    encoded_with_error = set_errors(encoded)
    print('\nДопускаем ошибки в закодированных данных: {0}'.format(encoded_with_error))
    diff_index_list = get_diff_index_list(encoded, encoded_with_error)
    print('\nДопущены ошибки в битах: {0}'.format(diff_index_list))
    decoded = decode(encoded_with_error, fix_errors=False)
    print('\nРезультат декодирования ошибочных данных без исправления ошибок: {0}'.format(LSB.bitstrToText(decoded)))
    decoded = decode(encoded_with_error)
    print('\nРезультат декодирования ошибочных данных с исправлением ошибок: {0}'.format(LSB.bitstrToText(decoded)))