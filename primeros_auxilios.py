
pasos_seguir = input("Responde a Estímulos? SI o NO :").lower()

# Le coloco el else con esa respuesta ya que si lo dejo solo if y else podria colocar cualquier letra y sigue como si la respuesta fuera no
if pasos_seguir == "si":
    print("Valorar la necesidad de llevarlo al hospital más cercano")     
elif pasos_seguir == "no":
    print("Abrir la vía Aérea")
else:
    print("Digita bien tu respuesta a: si o no")
respira = input("¿Respira?: ")
if respira =="si":
    print("Permite posición de suficiente ventilación")
else:
    print("Administrar 5 Ventilaciones y llamar a una Ambulancia") 
    ambulancia = "no"
    while ambulancia == "no":
        signos = input("¿Signos de Vida?: ")
        if signos == "si":
            print("Reevaluar a la espera de la Ambulancia")
        else:
            print("Administrat Compresiones Torácicas hasta que llegue la ambulancia")
        ambulancia = input("Llego la ambulancia?: ")
print("Programa terminado")

