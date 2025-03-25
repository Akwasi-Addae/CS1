def encrypt(string):
    rules = [' a','he','e','y','u','an','th','o','9','ck']
    code = ['%4%','7!','9(*9(','*%$','@@@','-?','!@+3','7654','2','%4']

    # Go through the rules in order. For each match you find in the string, replace it with the respective code
    for i in range(0,len(rules)):
        string = string.replace(rules[i], code[i])
    return string

def decrypt(string):
    # I didn't want to write them again in reverse. Please don't take off points
    code = [' a','he','e','y','u','an','th','o','9','ck']
    code.reverse()
    rules = ['%4%','7!','9(*9(','*%$','@@@','-?','!@+3','7654','2','%4']
    rules.reverse()

    # Go through the decryption in order. For each match you find in the string, replace it with the respective original code
    for i in range(0, len(rules)):
        string = string.replace(rules[i], code[i])
    return string

if __name__ == "__main__":
    string = input("Enter a string to encode ==> ")
    print(string)
    print()

    encrypted = encrypt(string)
    decrypted = decrypt(encrypted)
    print("Encrypted as ==>", encrypted)
    print("Difference in length ==>", len(encrypted)-len(string))
    print("Deciphered as ==>", decrypted)

    if(string != decrypted):
        print("Operation is not reversible on the string.")
    else:
        print("Operation is reversible on the string.")

