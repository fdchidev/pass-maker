import string
import random
longitud = int(input('Longitud requerida para su contraseña: '))
caracteres = string.ascii_letters + string.digits + string.punctuation
contraseña = ''.join(random.choice(caracteres) for i in range(longitud) ) 

print('Contraseña Generada: ' + contraseña)
