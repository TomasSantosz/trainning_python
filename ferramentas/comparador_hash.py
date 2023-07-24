import hashlib

arquivo_1 = 'a.txt'
arquivo_2 = 'b.txt'

hash1 = hashlib.new('ripemd160')
hash2 = hashlib.new('ripemd160')

hash1.update(open(arquivo_1, 'rb').read())
hash2.update(open(arquivo_2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'o arquivo: {arquivo_1} é diferente do arquivo: {arquivo_2}')
    print('O hash do arquvio a.txt é: ', hash1.hexdigest())
    print('O hash do arquvio b.txt é: ', hash2.hexdigest())
else:
    print(f'o arquivo: {arquivo_1} é igual ao arquivo: {arquivo_2}') 
    print('O hash do arquvio a.txt é: ', hash1.hexdigest())
    print('O hash do arquvio b.txt é: ', hash2.hexdigest())