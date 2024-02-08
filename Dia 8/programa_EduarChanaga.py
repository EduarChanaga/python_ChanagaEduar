# ********************************************
# ********************************************
#** Desde mi ordenador no funciona con (  '  )***
# ********************************************
# ********************************************

import json

# Abrir el archivo JSON
with open('datos.json', 'r') as Lospedidos:
    # Cargar el contenido del archivo en un diccionario
    diccionario = json.load(Lospedidos)

# Acceder a la parte de "pedidos" dentro de "ventas"
pedidos = diccionario["ventas"]["pedidos"]
comerciales = diccionario["ventas"]["comerciales"]
clientes = diccionario["ventas"]["clientes"]

while True:
    print("Que desea realizar?")
    print("1. Ejecutar")
    print("2. Modificar")
    decision3=int(input("--> "))
    if decision3 == 1:
        print("Que desea ver?")
        print("1. Los pedidos en orden de fecha (comenzando desde el más reciente)")
        print("2. Los pedidos de mayor valor ")
        print("3. Los clientes que han realizado compras")
        print("4. Los pedidos realizados en 2017, cuya cantidad total es superior a 500€")
        print("5. Los comerciales con comisión entre 0.05 y 0.11")
        print("6. El valor de la comisión más alto en la tabla comercial")
        print("7. Clientes de Sevilla ordenados alfabéticamente por apellidos y nombre")
        print("8. Listado de nombres de clientes que empiezan por A y terminan por n, o empiezan por P")
        print("9. Listado de nombres de clientes que empiezan por A")
        print("10. Listado de nombres de comerciales con apellido 'Ruiz'")
        print("11. Ver clientes")
        print("12. Ver pedidos")
        print("13. Ver comerciales")
        decision=int(input("--> "))

        if decision == 1:##############################################################################################################################
            # Ordenar los pedidos por fecha en orden descendente
            pedidos_ordenados = sorted(pedidos, key=lambda x: x['fecha'], reverse=True)
            # Imprimir los pedidos en orden de fecha, comenzando desde el más reciente
            print("Los pedidos en orden de fecha (comenzando desde el más reciente) son:")
            for i in pedidos_ordenados:
                print(i)

        elif decision ==2:##############################################################################################################################
            pedidos_mayorvalor=sorted(pedidos, key=lambda x: x['total'], reverse=True)
            print("Los pedidos de mayor valor son:")
            for i in pedidos_mayorvalor[:2]:
                print(i)
            print("")

        elif decision==3:##############################################################################################################################
            lista_ids_clientes = []
            for pedido in pedidos:
                id_cliente = pedido["id_cliente"]
                if id_cliente not in lista_ids_clientes:
                    lista_ids_clientes.append(id_cliente)
            # Imprimimos la lista de IDs de los clientes
            print("Los clientes que han realizado compras son:")
            print(lista_ids_clientes)
        elif decision==4:##############################################################################################################################
            # Filtrar los pedidos que se realizaron en <link>2017</link> y cuya cantidad total sea superior a 500€
            pedidos_2017_mayor_500 = [i for i in pedidos if i["fecha"].startswith("2017") and i["total"] > 500]                 
            #El método ".startswith()" es una función integrada de Python que se utiliza para verificar si una cadena de texto comienza con ciertos caracteres específicos. Su sintaxis es la siguiente
            print("")  
            # Imprimir los pedidos que cumplen con los criterios
            print("Los pedidos realizados en 2017, cuya cantidad total es superior a 500€ son:")
            for i in pedidos_2017_mayor_500:
                print(i)
        elif decision==5:##############################################################################################################################
            # Imprimir los nombres y apellidos de los comerciales seleccionados
            print("")
            comerciales_seleccionados = [i for i in comerciales if 0.05 <= i["comision"] <= 0.11]
            print("Los comerciales con comisión entre 0.05 y 0.11 son:")
            for i in comerciales_seleccionados:
                nombre = i["nombre"]
                apellido1 = i["apellido1"]
                apellido2 = i.get("apellido2", "")  # Si no hay segundo apellido, se asigna una cadena vacía
                print(f"{nombre} {apellido1} {apellido2}")
        elif decision==6:##############################################################################################################################
            # Inicializar el valor máximo de la comisión
            max_comision = float('-inf')  # Inicializado con el valor negativo infinito
            # Iterar sobre la lista de comerciales y actualizar el valor máximo de la comisión
            for i in comerciales:
                comision = i.get("comision", 0)  # Si no hay comisión, se asigna un valor predeterminado de 0
                if comision > max_comision:
                    max_comision = comision

            # Imprimir el valor máximo de la comisión
            print("")
            print("El valor de la comisión más alto en la tabla comercial es:", max_comision)
            print("")
        elif decision==7:##############################################################################################################################
            # Filtrar los clientes cuya ciudad sea "Sevilla"
            clientes_sevilla = [i for i in clientes if i.get("ciudad", "") == "Sevilla"]

            # Ordenar los clientes alfabéticamente por apellidos y nombre
            clientes_sevilla_ordenados = sorted(clientes_sevilla, key=lambda x: (x["apellido1"], x["nombre"]))

            # Imprimir el identificador, nombre y primer apellido de los clientes de Sevilla ordenados
            print("Clientes de Sevilla ordenados alfabéticamente por apellidos y nombre:")
            for i in clientes_sevilla_ordenados:
                identificador = i["id"]
                nombre = i["nombre"]
                apellido1 = i["apellido1"]
                print(f"ID: {identificador}, Nombre: {nombre}, Apellido: {apellido1}")
        elif decision==8:##############################################################################################################################
            # Filtrar los nombres que empiezan por "A" y terminan por "n"
            nombres_A_n = [i["nombre"] for i in clientes if i["nombre"].startswith("A") and i["nombre"].endswith("n")]

            # Filtrar los nombres que empiezan por "P"
            nombres_P = [i["nombre"] for i in clientes if i["nombre"].startswith("P")]

            # Combinar y ordenar alfabéticamente los nombres de ambos grupos
            nombres_ordenados = sorted(nombres_A_n + nombres_P)
            print("")
            # Imprimir el listado de nombres ordenados alfabéticamente
            print("Listado de nombres de clientes que empiezan por A y terminan por n, o empiezan por P:")
            for i in nombres_ordenados:
                print(i)


            
        elif decision==9:##############################################################################################################################
            # Imprimir el listado de nombres ordenados alfabéticamente
            nombres_A_n = [cliente["nombre"] for cliente in clientes if cliente["nombre"].startswith("A")]
            print("")
            print("Listado de nombres de clientes que empiezan por A ")
            for nombre in nombres_A_n:
                print(nombre)


        

            # Imprimir el listado de nombres de los comerciales que tienen como apellido "Ruiz"
        elif decision==10:##############################################################################################################################
        # Filtrar los comerciales cuyo apellido sea "Ruiz" y obtener sus nombres
            nombres_ruiz = {comercial["nombre"] for comercial in comerciales if comercial.get("apellido1", "") == "Ruiz"}
            print("")
            print("Listado de nombres de comerciales con apellido 'Ruiz':")
            for nombre in nombres_ruiz:
                print(nombre)

        elif decision==11:
            for i in clientes:
                print(i)
        elif decision==12:
            for i in pedidos:
                print(i)
        elif decision==13:
            for i in comerciales:
                print(i)
        else:
            break
        print("")
        print("")
        ### Decision de modificar ###
        
    elif decision3==2:

######################### MODIFICAR DATOS #########################
        print("1. Modificar datos de cliente ( Nombre/Apellido/Apellido2/ciudad )")
        print("2. Modificar pedidos ( Total / fecha )")
        decision4=int(input("-->"))
        if decision4==1:
            id_cliente_mod=int(input("Id del usuario a modificar: "))
            nombre_cliente_mod=str(input("Nombre: "))
            apellido_cliente_mod=str(input("Apellido: "))
            apellido2_cliente_mod=str(input("Apellido 2: "))
            ciudad_cliente_mod=str(input("Ciudad: "))
    # Iterar sobre la lista de clientes y modificar los nombres
            for cliente in diccionario['ventas']['clientes']:
                if cliente['id'] == id_cliente_mod:  # Modificar el nombre del cliente con ID 4
                    cliente['nombre'] = nombre_cliente_mod
                    cliente['apellido1'] = apellido_cliente_mod
                    cliente['apellido2'] = apellido2_cliente_mod
                    cliente['ciudad'] = ciudad_cliente_mod
            # Guardar los cambios en el mismo JSON (sobreescribir)
            with open('datos.json', 'w') as file:
                json.dump(diccionario, file, indent=2)

        if decision4==2:
            id_cliente_mod=int(input("Id del pedido a modificar: "))
            print("fecha = año-mes-dia")
            total_pedido_mod=float(input("Total: "))
            año_pedido_mod=int(input("Año: "))
            mes_pedido_mod=int(input("Mes: "))
            Dia_pedido_mod=int(input("Dia: "))
            
    # Iterar sobre la lista de clientes y modificar los nombres
            for pedido in diccionario['ventas']['pedidos']:
                if pedido['id'] == id_cliente_mod:  # Modificar el nombre del cliente con ID 4
                    pedido['Total'] = total_pedido_mod
                    pedido["fecha"]=año_pedido_mod+"-"+mes_pedido_mod+"-"+Dia_pedido_mod
  
            # Guardar los cambios en el mismo JSON (sobreescribir)
            with open('datos.json', 'w') as file:
                json.dump(diccionario, file, indent=2)
## Desarrollado por Eduar Damian Chanaga Gonzalez - 1095581647