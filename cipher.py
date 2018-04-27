def mainMenu():
    choice =""
    while choice !="1" or choice != "2":
        print("Enter the number corresponding to your choice:")
        print("1. Encrypt a message")
        print("2. Decrypt a message\n")
        print("3. Quit")
        choice = input()
        try:
            choice = int(choice)
        except ValueError:
            print("Only enter 1, 2 or 3")
            continue

        if choice < 1 or choice > 3:
            print("Only enter 1, 2 or 3")
        if choice == 1:
            message = input("Enter the message you want encrypted\n")
            message = message.replace(" ", "")

            secretKey = input("Enter the key you wish to use to encrypt the message\n")
            secretKey = secretKey.replace(" ", "")

            cipherTxt = vigEncrypt(message, secretKey)
            print("Your encrypted message is: "+cipherTxt)
            return True
        if choice == 2:
            message = input("Enter the message you want decrypted\n")
            message = message.replace(" ", "")

            secretKey = input("Enter the key you wish to use to decrypt the message\n")
            secretKey = secretKey.replace(" ", "")

            plainTxt = vigDecrypt(message, secretKey)
            print("Your decrypted message is: " + plainTxt)
            return True
        if choice == 3:
            return False


def rotn(char, rot):
    char = chr((ord(char)+ord(rot) - 65))
    if ord(char) > ord('Z'):
        val = ord(char) - ord('Z')
        val = val + (ord('A') - 1)
        char = chr( val )

    return char

def rotBack(char, rot):
    char = chr((ord(char) - (ord(rot) - 65)))

    if ord(char) < ord('A'):
        val = ord(char) + ord('A')-1
        if val > 97:
            val = val - 38
        char = chr(val)
    return char

def vigEncrypt(plainText, key):
    plainText = plainText.upper()
    key = key.upper()
    keyAry = []
    cipherText = []
    msgLen = len(plainText)
    keyLen = len(key)

    for i in range(msgLen):
        keyAry.append(key[i%keyLen])

    for i in range(msgLen):
        cipherText.append(rotn(plainText[i], keyAry[i]))
    return "".join(cipherText)


def vigDecrypt(cipherText, key):
    key = key.upper()
    plainText = []
    keyAry = []
    msgLen = len(cipherText)
    keyLen = len(key)

    for i in range(msgLen):
        keyAry.append(key[i%keyLen])

    for i in range(msgLen):
        plainText.append(rotBack(cipherText[i], keyAry[i]))

    return "".join(plainText)


go = True

while(go):
    go = mainMenu()
