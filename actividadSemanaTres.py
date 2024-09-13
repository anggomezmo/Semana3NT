global biblioteca


def agregar_libro ():
    titulo = str(input("Ingrese el nombre del libro: "))
    autor = str(input("Ingrese el autor del libro: " ))
    ano = str(input("Ingrese el ano del libro: "))
    chiquiccionario={}
    chiquiccionario.setdefault("autor",autor)
    chiquiccionario.setdefault("año",ano)
    chiquiccionario.setdefault("disponible",True)
    biblioteca.setdefault(titulo,chiquiccionario)
    
def prestar_libro ():
    titulo = str(input("Ingrese el titulo del libro: "))
    if  biblioteca[titulo]["disponible"] == False:
        print(f"El libro {titulo} ya esta prestado")
        return
    biblioteca[titulo]["disponible"] = False
    print(f"El libro {titulo} es tuyo mi rey")
    

def devolver_libro():
    titulo = str(input("Ingrese el titulo del libro a devolver: "))
    
    if  biblioteca[titulo]["disponible"] == True:
        print(f"El libro {titulo} no esta prestado")
        return
    biblioteca[titulo]["disponible"] = True
    print(f"Gracias por devolver el libro {titulo}")
    

def mostrar_libros():
    
    contador = 0
    for titulo,libro in biblioteca.items():
        
        print(f"{contador+1}. Titulo del libro: {titulo}")
        print(f"- Autor: {libro['autor']}")
        print(f"- Año de publicación: {libro['año']}")
        if libro['disponible']:
            print(f"- Disponibilidad: Disponible ")
        else:
            print(f"- Disponibilidad: No disponible ")
        contador+=1
 
 

biblioteca = {
    "Cien años de soledad": {"autor": "Gabriel García Márquez", "año": 1967, "disponible": True},
    "1984": {"autor": "George Orwell", "año": 1949, "disponible": True},
    "El principito": {"autor": "Antoine de Saint-Exupéry", "año": 1943, "disponible": False}
}

while True:
    print("------------Bienvenido a la biblioteca------------",end="\n")
  
    print("1. Agregar un libro.")
    print("2. Prestar un libro.")
    print("3. Devolver un libro.")
    print("4. Ver libros.")

    print("6. Salir",end="\n")
    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        agregar_libro()
        continue
    if opcion == 2:
        prestar_libro()
        continue
    if opcion == 3:
        devolver_libro()
        continue
    if opcion == 4:
        mostrar_libros()
        continue
    if opcion == 6:
        print("Gracias por usar la biblioteca")
        break
    else:
        print("seleccione una opción valida")
    

