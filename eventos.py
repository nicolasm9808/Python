def registrar_evento(datos):
    datos = dict(datos)
    evento={}
    evento["nombre"]=input("Ingrese el nombre del evento: ")
    evento["locacion"]=input("Ingrese la locación del evento: ")
    evento["realizado"]=False
    try:
        dia=int(input("Ingrese el día en que se realizará el evento: "))
    except Exception:
        dia = 1
    if dia > 0 and dia <= 31:
        evento["dia"] = dia
    else:
        print("Día invalido, se asignará el día 1")
        evento["dia"] = 1
        
    datos["eventos"].append(evento)
    print("Eventoregistrado con éxito!")
    return datos

def modificar_evento(datos):
    datos = dict(datos)
    evento = input("Ingrese el nombre del evento: ")
    for i in range(len(datos["eventos"])):
        if datos["eventos"][i]["nombre"] == evento:
            if datos["eventos"][i]["realizado"] == False:
                try:
                    opc = int(input("Ingrese 1 para MODIFICAR el evento, o 2 para ELIMIAR el evento: "))
                except Exception:
                    opc = 0
                if opc == 1:
                    datos["eventos"][i]["nombre"] = input("Ingrese el nombre del evento: ")
                    datos["eventos"][i]["locacion"] = input("Ingrese la locación del evento: ")
                    try:
                        dia=int(input("Ingrese el día en que se realizará el evento: "))
                    except Exception:
                        dia = 1
                    if dia > 0 and dia <= 31:
                        datos["eventos"][i]["dia"] = dia
                    else:
                        print("Día invalido, se asignará el día 1")
                        datos["eventos"][i]["dia"] = 1
                    return datos
                elif opc == 2:
                    datos["eventos"].pop(i)
                    print("Evento eliminado!")
                    return datos
                else:
                    print("Opción no válida")
            else:
                print("El evento ya se realizó, no se puede modificar ni eliminar!!")
                return datos
    print("No existe el evento")
    return datos