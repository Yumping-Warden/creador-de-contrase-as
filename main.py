import random
caracteres_posibles = ("+-_.,!#$%&/()=@qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM1234567890")
longitud_contrasena = int(input("¿Cuántos dígitos quieres que tenga tu contraseña?"))
contrasena = ""
for i in range(longitud_contrasena):
    contrasena += random.choice(caracteres_posibles)
print("Tu contraseña es: ", contrasena)                                
