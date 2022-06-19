import os
global nombreRep
Digitos=["0","1","2","3","4","5","6","7","8","9"]
Letras=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
Lerrores=[]
Ltokens=[]
Lestados=list()
def AFDINT(lexema):
    estado=0
    aceptacion = [1]
    
    for num in lexema:
        if estado==0:
            if num=="-" and num in Digitos or num in Digitos:
                estado=1
            else:
                estado=-1
        elif estado==1:
            if num in Digitos:
                estado=1
            else:
                estado=-1
        if estado==-1:
            return False
    return estado in aceptacion

def AFDINDENTIFICAOR(lexema):
    estado=0
    aceptacion = [1]

    for caracter in lexema:
        if estado==0:
            if caracter == "_" or caracter in Letras:
                estado=1
            else:
                estado=-1
        elif estado==1:
            if caracter == "_" or caracter in Letras or caracter in Digitos:
                estado=1
            else:
                estado=-1
        if estado==-1:
            return False

    return estado in aceptacion
def AFDCOMENTSIMPLE(lexema):
    estado=0
    aceptacion=[2]
    
    for coment in lexema:
        if estado==0:
            if coment =="/":
                estado=1
            else:
                estado=-1
        elif estado==1:
            if coment=="/":
                estado=2
            else: 
                estado=-1
        elif estado==2:
            if coment !='\n':
                estado=2
            else:
                estado=-1
        if estado==-1:
            return False
    return estado in aceptacion

def AFDCOMENTMULTI(lexema):
    estado=0
    aceptacion=[4]

    for multi in lexema:
        if estado == 0:
            if multi == "/":
                estado = 1
            else:
                estado = -1
        elif estado == 1:
            if multi == "*":
                estado = 2
            else:
                estado = -1
        elif estado == 2:
            if multi != '*':
                estado = 2
            elif multi == '*':
                estado = 3
            else:
                estado = -1
        elif estado == 3:
            if multi == "*":
                estado = 3
            elif multi != '*' and multi != '/':
                estado = 2
            elif multi == "/":
                estado = 4
            else:
                estado = -1

        elif estado == 4:
            estado = -1

        if estado == -1:
            return False

    return estado in aceptacion 

def AFDSTRING(lexema):
    estado=0
    aceptacion=[2]
    for stringg in lexema:
        if estado==0:
            if stringg=="\"":
                estado=1
            else:
                estado=-1
        elif estado==1:
            if stringg=="-" or stringg in Letras or stringg in Digitos:
                estado=2
            elif stringg =="\"":
                estado=2
            else:
                estado=-1
        elif estado==2:
            estado=-1
        if estado==-1:
            return False
    return estado in aceptacion

def AFDCHAR(lexema):
    estado=0
    aceptacion=[2]
    for char in lexema:
        if estado==0:
            if char=="\'":
                estado=1
            else:
                estado=-1
        elif estado==1:
            if char=="-" or char in Letras or char in Digitos:
                estado=2
            else:
                estado=-1
        elif estado==2:
            if char=="\'":
                estado=2
        if estado==-1:
            return False
    return estado in aceptacion

def AFDDOUBLE(lexema):
    estado=0
    aceptacion=[3]
    for double in lexema:
        if estado==0:
            if double in Digitos:
                estado=1
            elif double==".":
                estado=2
            else:
                estado=-1
        elif estado==1:
            if double in Digitos :
                estado=1
            elif double==".":
                estado=2
            else:
                estado=-1
        elif estado==2:
            if double in Digitos:
                estado=3
            else:
                estado=-1
        if estado==-1:
            return False
    return estado in aceptacion

tokens = {
"RESERVADA_INICIO": "INICIO",
"RESERVADA_FIN": "FIN",
"RESERVADA_IF": "if",
"RESERVADA_WHILE": "while",
"RESERVADA_VOID": "void",
"RESERVADA_DO": "do",
"RESERVADA_ELSE":"else",
"DOUBLE": AFDDOUBLE,
"INT": AFDINT,
"COMENT_SIMPLE": AFDCOMENTSIMPLE,
"COMENTARIO MULTILINEA": AFDCOMENTMULTI,
"STRING": AFDSTRING,
"CHAR": AFDCHAR,
"IDENTIFICADOR": AFDINDENTIFICAOR,
"SUMA": "+",
"RESTA": "-",
"MULTIPLICACION": "*",
"DIVISION": "/",
"RESTO": "%",
"IGUALACION": "==",
"DIFERENCIACION":"!=",
"MENOR_IGUAL":"<=",
"MAYOR_IGUAL": ">=",
"MAYOR":">",
"MENOR":"<",
"AND": "&&",
"OR": "||",
"NOT":"!",
"CORA":"[",
"CORB":"]",
"PARA":"(",
"PARB":")",
"LLAVEA":"{",
"LLAVEB":"}",
"PUNTO_COMA":";",
"ASIGNACION":"=",
"BOOLEAN":"True",
"BOOLEAN":"False",

}
def unionpatron(token, patron):
    descripcion={
    "INICIO":"Palbra reservada Inicio",
    "FIN":"Palbra reservada Fin",
    "if":"Palbra reservada if",
    "while":"Palbra reservada while",
    "void":"Palbra reservada void",
    "do":"Palbra reservada do",
    "else":"Palbra reservada else",
    "INT":"AFD de los numeros enteros",
    "DOUBLE": "AFD de los numeros double",
    "COMENT_SIMPLE": "AFD de los comentarios simples",
    "COMENTARIO MULTILINEA": "AFD de los comentarios multilinea",
    "+":"operador de suma",
    "-":"operador de resta",
    "*":"operador de multiplicacion",
    "/":"operador de division",
    "%":"operador de resto",
    "==":"operador de igualacion",
    "!=":"operador de diferenciacion",
    "<=":"operador de menor o igual",
    ">=":"operador de mayor o igual",
    ">":"operador de mayor",
    "<":"operador de menor",
    "&&":"operador AND",
    "||":"operador OR",
    "!":"operador NOT",
    "[":"Corchete que habre",
    "]":"Corchete que cierra",
    "(":"parentesis que habre",
    ")":"parentesis que cierra",
    "{":"llave que habre",
    "}":"llave que cierra",
    ";":"punto y coma",
    "=":"operador de asignacion",
    "True":"dato de tipo boolean",
    "False":"dato de tipo boolean",
    "CHAR":"AFD de los valores tipo char",
    "STRING": "AFD de los valores tipo string",
    "IDENTIFICADOR": "AFD de los identificadores"
    }

    patrones={
    "INICIO":"INICIO",
    "FIN":"Fin",
    "if":"if",
    "while":"while",
    "void":"void",
    "do":"do",
    "else":"else",
    "INT":"([0-9]+)",
    "DOUBLE": "([0-9]*[.])?[0-9]+",
    "COMENT_SIMPLE": "//.\*",
    "COMENTARIO MULTILINEA": "\/*([.\*]|\n)\*\*\/",
    "+":"+",
    "-":"-",
    "*":"*",
    "/":"/",
    "%":"%",
    "==":"==",
    "!=":"!=",
    "<=":"<=",
    ">=":">=",
    ">":">",
    "<":"<",
    "&&":"&&",
    "||":"||",
    "!":"!",
    "[":"[",
    "]":"]",
    "(":"(",
    ")":")",
    "{":"{",
    "}":"}",
    ";":";",
    "=":"=",
    "True":"True",
    "False":"False",
    "CHAR":"'[^']|(')'",
    "STRING":  "([^\"]|(\"))*",
    "IDENTIFICADOR": "(|[a-zA-Z])(|[a-zA-Z0-9])"
    }

    contenido= dict()
    for token, descripcion in descripcion.items():
        if patron==token:
            contenido['Descripcion']=descripcion
        elif tokens==token:
            contenido['Descripcion']=descripcion
    for token, patrones in patrones.items():
        if patron==token:
            contenido['Patron']=patrones
        elif tokens==token:
            contenido['Patron']=patrones
    return contenido

IGNORAR = " \n\t"

def analizar(archivo):
        filas=1 
        columna = 1
        indice = 0

        while indice < len(archivo):
            caracter = archivo[indice]
            reconocido = False

            if caracter=="\n":
                filas+=1
                columna=0
            columna+=1

            caracter_impresion = caracter
            if caracter_impresion == '\n': caracter_impresion = '\\n'

            print(f"[FILA: {filas}, COLUMNA: {columna}] CARACTER: '{caracter_impresion}'")

            if caracter in IGNORAR:
                print("IGNORANDO")
                indice += 1
                continue

            for token, patron in tokens.items():
                if isinstance(patron, str):
                    if indice + len(patron) > len(archivo): continue

                    lexema = archivo[indice : indice + len(patron)]

                    if lexema == patron:
                        reconocido = True
                        indice += len(patron)
                        columna += len(patron)
                        #descripcion=unionpatron(token, patron)
                        #Plexema=lexema(lexema,descripcion['Descripcion'], filas,columna,descripcion['patron'])
                        #Ptoken=token(token,Plexema)
                        print(f"RECONOCIDO: '{lexema}' | {token} - {patron}")

                else: 
                    indice_adelante = indice + 1
                    anterior_reconocido = False

                    while indice_adelante <= len(archivo) and archivo[indice_adelante - 1] != '\n':
                        lexema = archivo[indice : indice_adelante]
                        reconocido = patron(lexema)

                        if not reconocido and anterior_reconocido:
                            lexema = archivo[indice : indice_adelante - 1]
                            reconocido = True
                            indice = indice_adelante - 1
                            break

                        anterior_reconocido = reconocido
                        indice_adelante += 1

                    if reconocido:
                        #descripcion=unionpatron(token, patron)
                        #Plexema=lexema(lexema,descripcion['Descripcion'], filas,columna,descripcion['patron'])
                        #Ptoken=token(token,Plexema)
                        dtokens=Reptoken(filas,columna,lexema,token,patron)
                        Ltokens.append(dtokens)
                        print(f"RECONOCIDO: '{lexema}' | {token} - AFD")
                        columna += indice_adelante - indice + 1
                        indice = indice_adelante - 1

                if reconocido: break

            if not reconocido:
                indice += 1
                Derror=Reperrores(filas,columna,lexema)
                Lerrores.append(Derror)
                #dt={'tokens':Ltokens, "Errores":Lerrores}
                #return dt
                print("ERROR LEXICO")
        
class Reptoken:
    def __init__(self,filas,columna,lexema,token,patron):
        self.filas=filas
        self.columna=columna
        self.lexema=lexema
        self.token=token
        self.patron=patron

    def getfilas(self):
        return self.filas
    def getcolumna(self):
        return self.columna
    def getlexema(self):
        return self.lexema
    def gettoken(self):
        return self.token
    def getpatron(self):
        return self.patron

class Reperrores:
    def __init__(self,filas, columna,lexema):
        self.filas=filas
        self.columna=columna
        self.lexema=lexema
    
    def getfilas(self):
        return self.filas
    def getcolumna(self):
        return self.columna
    def getlexema(self):
        return self.lexema

def app():
    salir=False
    while not salir:
        res = input('''
1. Cargar archivo de codigo
2. Ingresar nombre de reporte
3. Salir
Selecciona una opcion: ''')
        #switch
        if res == '1':
            Nomarchivo=input("Ingrese el nombre del archivo (" + os.getcwd() + ")\n")
            #try:
            archivo=open(Nomarchivo, encoding="utf8").read()
            analizar(archivo)
                #print(str(archivo))    
            #except:
                #print('Error, archivo inexistente')
               # return
        elif res == '2':
            nombreRep= input("Ingrese el nombre que desea asignar: ")
            print("Su reporte ha sido creado con exito")
            with open(nombreRep, 'w') as f:
                f.write("<!DOCTYPE html>\n"
                "<html>\n"
                "<head>\n"
                "<title>Reporte de Errores</title>\n"
                "<style>"
                    "body { background-color: #C5FF33; }"
                "</style>"
                "</head>\n"
                "<body>\n"
                '<div id="main-container">\n'
                "<h2>Reporte de tokens lexico Francisco Cetino 202006716</h2>\n"
                "<table>\n"
                "<thead>\n"
                "<tr>\n"
                "<th>FILA</th><th>COLUMNA</th><th>LEXEMA</th><th>TOKEN</th>\n"
                "</tr>\n"
                "</thead>\n")

                for x in Ltokens:
                    f.write("<tr><td>" + str(x.getfilas()) + "</td><td>" + str(x.getcolumna()) + "</td><td>" + str(x.getlexema()) + "</td><td>" + str(x.gettoken()) + "</td><td>" + str(x.getpatron()) + "</td>\n</tr> ")

                f.write("</table>\n"
                    "<h2>Reporte de errores</h2>\n"
                    "<table>\n"
                    "<thead>\n"
                    "<tr>\n"
                    "<th>FILA</th><th>COLUMNA</th><th>LEXEMA</th>\n"
                    "</tr>\n"
                    "</thead>\n")
                for x in Lerrores:
                    f.write("<tr><td>" + str(x.getfilas()) + "</td><td>" + str(x.getcolumna()) + "</td><td>" + str(x.getlexema()) + "</td>\n</tr> ")


                f.write("</table>\n"
                    "</div>\n"
                    "</body>\n"
                    "</html>")

        elif res == '3':
            print("Adios")
            salir=True
            break
        else:
            print("Por favor seleccione un opcion valida")
app()