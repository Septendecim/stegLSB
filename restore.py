# очистить контейнер lsb
def restoreImage():
    with open(r"C:\Users\Vlad\Documents\code Python\ITMO\images\original.bmp", 'rb') as f:
        data = bytearray(f.read())

    with open(r"C:\Users\Vlad\Documents\code Python\ITMO\images\lsb.bmp", "wb") as f:
        f.write(data)
        
        print("l33t")



if __name__ == '__main__':
    restoreImage()