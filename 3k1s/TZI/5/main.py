from Crypto.Hash import SHA256
from Crypto.PublicKey import DSA
from Crypto.Signature import DSS

if __name__ == "__main__":
    print("1 - Згенерувати ключі")
    print("2 - Підписати повідомлення")
    print("3 - Перевірити підпис")

    k = int(input("Оберіть: "))

    #Випадок генеруввання ключів
    if k == 1:
        public = input("Як назвати файл публічного ключа? ")
        privat = input("Як назвати файл приватного ключа? ")
        key = DSA.generate(bits=1024)
        with open(privat, "wb") as input_file_pr:
            input_file_pr.write(key.exportKey())
        with open(public, "wb") as input_file_pb:
            input_file_pb.write(key.publickey().exportKey())

    #Випадок запису підпису
    elif k == 2:
        privateFile = input("Файл приватного ключа: ")
        with open(privateFile, "rb") as file:
            privateKey = DSA.import_key(file.read())
        print("Звідки тягнути повідомлення для шифрування?")
        print("1 - З файлу")
        print("2 - З консолі")
        m = int(input("Оберіть: "))
        message = ""
        if m == 1:
            filename = input("Ім'я файлу: ")
            with open(filename, "rb") as file:
                message = file.read()
        elif m == 2:
            message = bytes(input("Повідомлення: "), encoding="utf-8")
        mess_enc = SHA256.new(message)
        sign = DSS.new(privateKey, "fips-186-3")
        signature = sign.sign(mess_enc)
        print("Підписане повідомлення: " + signature.hex())
        write_to_file = input("Записати у файл? (y/n)")
        if write_to_file.lower() == "y" or write_to_file.lower() == "":
            filename = input("Ім'я файлу: ")
            with open(filename, "w") as output:
                output.write(signature.hex())

    #Випадок перевірки підпису
    elif k == 3:
        publicFile = input("Файл публічного ключа: ")
        with open(publicFile, "rb") as file:
            publicKey = DSA.import_key(file.read())
        message = str.encode(input("Підпис: "))
        print("Звідки тягнути зашифрований підпис?")
        print("1 - З файлу")
        print("2 - З консолі")
        m = int(input("Оберіть: "))
        signature = ""
        if m == 1:
            filename = input("Ім'я файлу: ")
            with open(filename, "r") as file:
                signature = file.read()
        elif m == 2:
            signature = input("Підпис: ")
        message = SHA256.new(message)
        signature = bytes.fromhex(signature)
        verifier = DSS.new(publicKey, "fips-186-3")
        try:
            verifier.verify(message, signature)
            print("Дійсний підпис")
        except ValueError:
            print("Недійсний підпис")
        pass