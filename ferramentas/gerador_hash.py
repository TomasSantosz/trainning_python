import hashlib 

string = input("Digite o texto para ser transformado em hash: ")


menu = int(input(''' ### MENU - ESCOLHA O TIPO DE HASH ###
    1) MDS
    2) SHA1
    3) SHA256
    4) SHA512
'''))

if menu == 1:
    result = hashlib.md5(string.encode('utf-8'))
    print("O hash da string é: ", result.hexdigest())
elif menu == 2:
    result = hashlib.sha1(string.encode('utf-8'))   
    print("O hash da string é: ", result.hexdigest()) 
elif menu == 3:
    result = hashlib.sha256(string.encode('utf-8'))  
    print("O hash da string é: ", result.hexdigest())  
elif menu == 4:
    result = hashlib.sha512(string.encode('utf-8'))  
    print("O hash da string é: ", result.hexdigest())
else:
    print('Deu merda menor! Tenta dnv esse trem.')  
    
