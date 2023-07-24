import ctypes

atributs = 0x02

returned = ctypes.windll.kernel32.SetFileAttributesW('ocultar.txt', atributs)

if returned:
    print('arquivo ocultado')
else:
    print('Não ocultado')