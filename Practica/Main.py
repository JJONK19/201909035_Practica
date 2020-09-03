import json
import re
import webbrowser
X = ""
data = []
cd = False  #Verifica si se cargaron los datos
while (X.lower() != "salida"):
    print("------------------------------------------------------------------------------------------------------------")
    print("SimpleQL - V.1.0.0")
    print("MENÚ PRINCIPAL")
    print("Listado de Funciones:")
    print("1. Cargar Archivos: Cargar DirArchivo1, DirArchivo2, DirArchivo3,...  DirArchivoN")
    print("2. Seleccionar Archivos: Seleccionar atributo1, atributo2 Donde atributo=Valor")
    print("3. Maximo: Maximo atributo1")
    print("4. Minimo: Minimo atributo1")
    print("5. Suma: Suma atributo1")
    print("6. Cuenta: Cuenta")
    print("7. Reportar: Reportar NoDatos")
    print("8. Salir/Finalizar: Salida")
    X = input("INGRESE UNA INSTRUCCIÓN: ")
    print("------------------------------------------------------------------------------------------------------------")

    sep = X.split()
    com = sep[0]

    if com.lower() == "cargar":
        data = []
        cd = False
        arc = X[7:len(X)]
        if arc == "":
            print("ERROR: SINTAXIS INVALIDA")
        else:
            #Separar archivos en un arreglo e ir cargandolos uno a uno
            arM = arc.replace(" ", "")
            arF = arM.split(",")
            try:
                for i in range(len(arF)):
                    with open(arF[i]) as f:
                        data = data + json.load(f)
                print("MENSAJE: CARGA EXITOSA")
                cd = True
            except:
                print("ERROR: ARCHIVO/S NO ENCONTRADOS. VUELVA A CARGAR SUS ARCHIVOS NUEVAMENTE.")
                data = []
                cd= False


    elif com.lower() == "seleccionar":
        if cd == False:
            print("Error: CARGUE PRIMERO LA INFORMACION ANTES DE CONTINUAR")
        else:
            dat = X[12:len(X)]
            if dat == "":
                print("ERROR: SINTAXIS INVALIDA")
            elif dat == "*":
                for i in range(len(data)):
                    print(data[i])
            else:
                pos = re.search("donde", dat, re.IGNORECASE)
                if pos == None:
                    print("ERROR: SINTAXIS INVALIDA")
                else:
                    posI = pos.start()

                    #Partir atributos y meterlo en un arreglo
                    atr = dat[0:posI]
                    atM = atr.replace(" ", "")
                    atF = atM.split(",")

                    #Separar condicion de busqueda en atributo y el valor a buscar
                    con = dat[(posI+5):len(dat)]
                    coM = con.replace(" ", "")
                    coF = coM.split("=")

                    if atF[0]=='' or coF[0]=='' or coF[1]=='':
                        print("ERROR: SINTAXIS INVALIDA")
                    else:
                        atB = coF[0]
                        val = coF[1]

                        if atB == "edad":
                            val = int(val)

                        if atB == "promedio":
                            val = float(val)

                        if atB == "activo":
                            if val == "true":
                                val = True
                            else:
                                val = False

                        cont = 0

                        if atB == 'nombre' or atB == 'edad' or atB == 'activo' or atB == 'promedio':
                            for i in range(len(data)):
                                j = data[i]
                                if j.get(atB) == val:
                                    for k in range(len(atF)):
                                        if atF[k] == "nombre" or atF[k] == "edad" or atF[k] == "activo" or atF[k] == "promedio":
                                            print(j.get(atF[k]))
                                            cont = cont + 1
                                    print("************************************************************************************************************")

                            if cont == 0:
                                print("Mensaje: No existen registros que cumplan con la condición.")
                        else:
                            print("Mensaje: El atributo que busca no se encuentra en los registros.")

    elif com.lower() == "maximo":
        mi = []
        if cd == False:
            print("Error: CARGUE PRIMERO LA INFORMACION ANTES DE CONTINUAR")
        else:
            dat = X[7:len(X)]
            if dat == "edad" or dat == "promedio":
                for i in range(len(data)):
                    mi.append(data[i].get(dat))
                print(max(mi))
            else:
                print("Mensaje: El atributo del cual desea obtener el valor maximo no posee datos numericos o no existe.")

    elif com.lower() == "minimo":
        mi = []
        if cd == False:
            print("Error: CARGUE PRIMERO LA INFORMACION ANTES DE CONTINUAR")
        else:
            dat = X[7:len(X)]
            if dat == "edad" or dat == "promedio":
                for i in range(len(data)):
                    mi.append(data[i].get(dat))
                print(min(mi))
            else:
                print(
                    "Mensaje: El atributo del cual desea obtener el valor maximo no posee datos numericos o no existe.")

    elif com.lower() == "suma":
        mi = 0
        if cd == False:
            print("Error: CARGUE PRIMERO LA INFORMACION ANTES DE CONTINUAR")
        else:
            dat = X[5:len(X)]
            if dat == "edad" or dat == "promedio":
                for i in range(len(data)):
                    mi = mi + data[i].get(dat)
                print(mi)
            else:
                print(
                    "Mensaje: El atributo del cual desea obtener el valor maximo no posee datos numericos o no existe.")

    elif com.lower() == "cuenta":
        print(len(data))

    elif com.lower() == "reportar":
        if cd == False:
            print("Error: CARGUE PRIMERO LA INFORMACION ANTES DE CONTINUAR")
        else:
            dat = X[9:len(X)]
            try:
                reg = int(dat)
            except:
                print("ERROR: DEBE INGRESAR EL NUMERO DE REGISTROS QUE DESEE REPORTAR.")
            if reg > len(data):
                reg = len(data)

            html = open('Reporte.html', 'w')
            html.write('<!DOCTYPE html>')
            html.write('<html>')
            html.write('    <head>')
            html.write('        <title>Reporte</title>')
            html.write('        <style>')
            html.write('            *{')
            html.write('                background-color: #663333;')
            html.write('                color: #FFFFFF;')
            html.write('                font-family: "Arial Narrow";')
            html.write('              }')
            html.write('            table{')
            html.write('                font-style: italic;')
            html.write('                border: 1 px #ddd;')
            html.write('                border-collapse: collapse;')
            html.write('                width: 75%;')
            html.write('              }')
            html.write('            th, td{')
            html.write('                padding: 15px;')
            html.write('                border-bottom: 1px solid #ddd;')
            html.write('                color: #FFFFFF;')
            html.write('              }')
            html.write('            tr:nth-child(even) {background-color: #6666CC;}')
            html.write('              th{')
            html.write('                background-color: #993333;')
            html.write('                color: #FFFFFF;')
            html.write('              }')
            html.write('        </style>')
            html.write('    </head>')
            html.write('    <body>')
            html.write('        <center>')
            html.write('            <h1><b><u>REPORTE</u></b></h1>')
            html.write('             <table>')
            html.write('                <tr>')
            html.write('                    <th><b><u>NOMBRE</u></b></th>')
            html.write('                    <th><b><u>EDAD</u></b></th>')
            html.write('                    <th><b><u>ACTIVO</u></b></th>')
            html.write('                    <th><b><u>PROMEDIO</u></b></th>')
            html.write('                </tr>')
            for i in range(len(data)):
                html.write('                <tr>')
                html.write('                    <th>'+data[i].get("nombre")+'</th>')
                html.write('                    <th>'+str(data[i].get("edad"))+'</th>')
                html.write('                    <th>'+str(data[i].get("activo"))+'</th>')
                html.write('                    <th>'+str(data[i].get("promedio"))+'</th>')
                html.write('                </tr>')
            html.write('             </table>')
            html.write('        </center>')
            html.write('    </body>')
            html.write('</html>')
            html.close()

            webbrowser.open_new_tab('Reporte.html')

    elif com.lower() == "salida":
        print("")
    else:
        print("ERROR: INGRESE UN COMANDO VÁLIDO")




