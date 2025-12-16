import random
import string

longitud = int(input("Longitud de la contraseña: "))

caracteres = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(caracteres) for _ in range(longitud))

print("Contraseña generada:", password)
