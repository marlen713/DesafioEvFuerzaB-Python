
# Esta libreria se importa para que reconozca las letras en minusculas
from string import ascii_lowercase
import getpass

password = getpass.getpass("Ingrese la contraseña gato: ").lower()
intento = ''
intentos = 0

# Enumerate Retorna un objeto con un contador que sirve de clave para cada valor, lo que facilita el acceso a cada elemento del grupo de datos.
# el guion bajo (_) en Python es para omitir valores. siempre que no deseemos almacenar algún valor en una variable, y simplemente queramos pasar de él,
# haremos uso del guion bajo.
for i, _ in enumerate(password):
    for letra in ascii_lowercase:
        intentos += 1
        print(f"La contraseña fue forzada en {intentos} intentos: {intento + letra}")
        if letra == password[i]:
            intento += letra
            break

# NOTA: A modo explicativo se mostrará la contraseña a buscar pero la idea es que ésta se ingrese de manera oculta.
# Por ese motivo es que al momento de ingresar esta oculpa, pero en lo demás visible.