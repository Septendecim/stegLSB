from math import log10, sqrt
import numpy
import sewar

deep = 1
offset = 1078 #54

# IN:     img - bytearray (list of int256 in hexview)
# OUT:    answ - значение PSNR метрики
def psnr(img1, img2):
    
    if(img1 == img2): return 0        # если изображения одинаковы - возвращаем max оценку
    
    s = 0
    n = min(len(img1),len(img2))
    for i,j in zip(img1,img2): s += (i-j)**2
    mse = (1/n)*s
    PIXEL_MAX = 255.0
    answ = 20 * log10(PIXEL_MAX / sqrt(mse))
    return answ
    

# IN:     string of chars - "Lorem ipsum"
# OUT:    string of binary representation of chars - '010011000110111101110010...'
def txtToBitstr(str):
    bit_str = ''
    for i in str:
        bin_char = bin(ord(i))          # получаем ascii-код символа в виде 0b11010
        bin_char = bin_char[2:]         # отбрасываем 0b
        while(len(bin_char) < 8):       # добавляем до 8 символов
            bin_char = '0' + bin_char
        bit_str += bin_char
    return bit_str


# IN:     string of binary representation of chars - '010011000110111101110010...'
# OUT:    string of chars - "Lorem ipsum"
def bitstrToText(bit_str):
    str = ''
    byte_str = ''
    counter = 0
    for i in bit_str:
        byte_str += i
        counter += 1
        if(counter == 8):                   # отсчитываем 8 бит
            str += chr(int(byte_str, 2))    # форматируем их в число, число в символ
            byte_str = ''
            counter = 0
    return str


# IN:     bytearray (list of int256 in hexview)
# OUT:    string of binary representation of chars - '010011000110111101110010...'
def bytearrayToBitstr(bytes_arr):
    bit_str = ''
    for i in bytes_arr:
        i
    return bit_str


# IN:     string of binary representation of chars - '010011000110111101110010...'
# OUT:    bytearray (list of int256 in hexview)
def bitstrToBytearray(bit_str):
    return binlistToBytearray(bitstrToBinlist(bit_str))
    

# IN:     bytearray (list of int256 in hexview)
# OUT:    list of bytes in binary string view - ['01101010', '00110100', ...]
def bytearrayToBinlist(bytes_arr):
    bytes_list = []
    for i in bytes_arr:
        bin_i = bin(i)              # получаем число int в виде 0b11010
        bin_i = bin_i[2:]           # отбрасываем 0b
        while(len(bin_i) < 8):      # добавляем до 8 символов
            bin_i = '0' + bin_i
        bytes_list.append(bin_i)
    return bytes_list


# IN:     list of bytes in binary string view - ['01101010', '00110100', ...]
# OUT:    bytearray (list of int256 in hexview)
def binlistToBytearray(bytes_list):
    bytes_arr = bytearray()
    for i in bytes_list:
        bytes_arr.append(int(i, 2))     # форматируем 1101010 в число, добавляем в конец
    return bytes_arr



# IN:     string of binary representation of chars - '010011000110111101110010...'
# OUT:    list of bytes in binary string view - ['01101010', '00110100', ...]
def bitstrToBinlist(bit_str):
    bytes_list = []
    counter = 0
    byte = ''
    for i in bit_str:
        byte += i
        counter += 1
        if(counter == 8):
            bytes_list.append(byte)
            byte = ''
            counter = 0
    return bytes_list
    



# IN:     data_container - bytelist ['01101010', '00110100', ...]
#         data_embedding - bitstring '010011000110111101110010...'
# OUT:    data_container - modified
def lsb_enc( data_container, data_embedding, deep):
    counter = 0
    data_embedding += '1111111111111111'       # символ остановки чтения в конце - 0xFFFF
    format_embedding = []
    part = ''
    
    # разбить bitstring на части размером deep для встраивания
    for i in data_embedding:
        part += i
        if(len(part) == deep):
            format_embedding.append(part)
            part = ''
    
    # встраивание emb-блоков размера deep к cont-блокам размера 8-deep
    for cont, emb in zip(data_container, format_embedding):
        data = cont[:(8-deep)] + emb
        data_container[counter] = data
        counter += 1

    return data_container


# IN:     data_container - bytelist ['01101010', '00110100', ...]
# OUT:    message - bitstring '010011000110111101110010...'
def lsb_dec(data_container, deep):
    message = ''
    for i in data_container: message += i[8-deep:]      # вытягиваем последние deep бит из каждого байта
    
    index = 0
    counter_1 = 0
    while (counter_1 < 16):                             # ищем стоп-символ 0xFFFF
        if message[index] == '1': counter_1 += 1
        else: counter_1 = 0
        index += 1
        
    message = message[:index-16]                        # отбрасываем 0xFFFF и все что после

    return message



#--------------------------------------------------

if __name__ == "__main__":

    # 1 paragraph, 145 words, 1024 bytes of Lorem Ipsum
    msg = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent semper sagittis iaculis. Nulla facilisis ligula tortor, quis pulvinar mauris condimentum ac. Ut placerat, metus id eleifend varius, nisi sapien tempus sapien, eget elementum dolor magna nec enim. Mauris a ante vehicula, viverra neque ac, tempor nisi. Praesent porta nunc quis nisi pellentesque, sed malesuada justo scelerisque. Fusce fermentum sodales odio sit amet tristique. Praesent scelerisque ex et leo pharetra tempor. Quisque gravida ipsum eget mi convallis, vel interdum felis tempor. Sed imperdiet volutpat lorem. Maecenas aliquam molestie finibus. Pellentesque erat erat, sodales vel eleifend ut, varius ac urna. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. In rhoncus neque sed dignissim molestie. Donec ut eros commodo, tincidunt diam vel, placerat neque. Donec tincidunt egestas quam non bibendum. Ut rhoncus dictum fringilla. Aliquam erat volutpat. Suspendisse egestas tempus tellus egestas augue."
    bin_msg = txtToBitstr(msg)

    # Открыть файл картинки
    with open(r"C:\Users\Vlad\Documents\code Python\ITMO\images\original.bmp", 'rb') as f:
        data = bytearray(f.read())                  # получаем всю картинку
        container = data[offset:]                   # откидываем метаинформацию
        bin_cont = bytearrayToBinlist(container)    # конвертируем в двоичный формат ['01101010', '00110100', ...]

    # Вывод общей информации
        print("Длина сообщения (биты)\t\t",len(bin_msg))
        print("Глубина встраивания (биты)\t", deep)
        print("Для встраивания необходимо байт\t",len(bin_msg)/deep)
        print("Объем контейнера (байты)\t", len(bin_cont))

    # Проверка длины сообщения и объема контейнера.
        if(len(bin_msg)/deep > len(bin_cont)):
            print("Сообщение не помещается")
        else:
            print("Сообщение помещается")
            enc_container = lsb_enc(bin_cont, bin_msg, deep)
            enc_container = binlistToBytearray(enc_container)   # результат встраивания отформатировать в bytearray
            enc_data = data[:offset] + enc_container            # соединить контейнер с пропущенной метой
        
            with open(r"C:\Users\Vlad\Documents\code Python\ITMO\images\lsb.bmp", "wb") as f:
                f.write(enc_data)
        
        
        
    # Извлечение сообщения из контейнера
        with open(r"C:/Users/Vlad/Documents/code Python/ITMO/images/lsb.bmp", 'rb') as f:
            data2 = bytearray(f.read())                 # получаем всю картинку
            container = data2[offset:]                  # откидываем метаинформацию
            bin_cont = bytearrayToBinlist(container)    # конвертируем в двоичный формат ['01101010', '00110100', ...]
            
            dec_container = lsb_dec(bin_cont, deep)
            msg = bitstrToText(dec_container)
            print("secret message is:")
            print(msg)
            
            # выдача результата
            msg_path = "C:/Users/Vlad/Documents/code Python/ITMO/images/output.txt"
            ext_message = bitstrToBytearray(dec_container)
            with open(msg_path, "wb") as f:
                f.write(ext_message)
        