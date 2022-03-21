# if __name__=="__main__":
#     n = int(input())
#     integer_list = map(int, input().split()) #Split retorna una lista donde cada elemento está separado por un espacio

#     t = tuple(integer_list)

#     print(hash(t))
 #----------------------------------------
# import hashlib
# from hashlib import md5

# mensaje = input("Introduzca el mensaje: \n ")
# print(md5(mensaje.encode("utf-8")).hexdigest()) #Sirve para encriptar un mensaje
#----------------------------------------
# def convCad(cad):
#     salida =""

#     for l in cad:
#         salida += str(ord(l)) #ord me da el valor ascii
#     return int (salida)


# def hashM(cad, m):
#     i = convCad(cad)

#     return int(m*(i * 0.0000000000000000211 % 1))

# def agregar(cad, ht, m):
#     res = hashM(cad, m)
#     ht[res].append(cad)

# def buscar(cad, ht, m):
#     h = hashM(cad, m)

#     for i in ht[h]:
#         if i == cad:
#             return True
    
#     return False

# m = 19
# ht = [[] for i in range(m)]
# agregar("cama", ht, m)
# agregar("carro", ht, m)
# agregar("casa", ht, m)
# agregar("cuaderno", ht, m)

# print(ht)

# print(buscar("casa", ht, m))
# print(buscar("libro", ht, m))
#----------------------------------------

class MyHashSet:

    def __init__(self):
        

    def add(self, key: int):
        
        

    def remove(self, key: int):
        

    def contains(self, key: int):