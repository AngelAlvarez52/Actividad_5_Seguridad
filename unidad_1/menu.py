import os

while True:
    os.system('cls')
    print("Sistema para pruebas de seguridad informatico")
    print("Version 1.0 Desarrollado por Angel Daniel Alvarez Felix")
    print("1.- Busqueda de Subdominios")
    print("2.- Banner Grabbing")
    print("3.- Escaneo de puertos")
    print("4.- Get IP using nslookup")
    print("5.- Get IP using socket")
    print("6.- Salir")

    opcion = int(input("Selecciona una opcion: "))
    if opcion == 1:
        target = input("Ingresa el dominio de la victima: ")
        os.system(f'python subdominios.py -t {target}')
        input("Presiona enter para continuar")
    elif opcion == 2:
        target = input("Ingresa la direccion ip de la victima: ")
        os.system(f'python bannergrabing.py -t {target}')
        input("Presiona enter para continuar")
    elif opcion == 3:
        target = input("Ingresa el dominio de la victima: ")
        os.system(f'python port_scanner.py -t {target}')
        input("Presiona enter para continuar")
    elif opcion == 4:
        target = input("Ingresa el dominio de la victima: ")
        os.system(f'python get_ip_2.py -t {target}')
        input("Presiona enter para continuar")
    elif opcion == 5:
        target = input("Ingresa la direccion ip de la victima: ")
        os.system(f'python get_ip.py -t {target}')
        input("Presiona enter para continuar")
    elif opcion == 6:
        break
    else:
        print("Opcion no valida")
        continue