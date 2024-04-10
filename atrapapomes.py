from random import randint as rd

#VARIABLES GLOBALS
rows, cols = (5,5)
estaJugant = True
x = 2
y = 2
xObj = 2
yObj = 3
score = 0
Jugador = 'x'
Objectiu = 'o'
Caselles = '#'
arr = [[Caselles for i in range(cols)] for j in range(rows)]


#ALTRES FUNCIONS 
def nomCela():
    numero=rows  #es moura cap abaix
    for i in range(cols):
        lletra=65 #ascii 'A'
        for j in range(rows):
            arr[i][j] = chr(lletra)+str(numero)
            lletra+=1
        numero-=1
def dibuixaAmbNumeros():
    for i in range(cols):
        for j in range(rows):
            if i%2 == 0: #si i es parell
                if j%2 == 0: #si j es parell
                    arr[i][j]=1
            else: #si i es senar
                if j%2 != 0: #si j es senar
                    arr[i][j]=1

#FUNCIONS BASIQUES
def Dibuixa():
    for row in arr:
        print(row)

def Clear():
    for i in range(cols):
        for j in range(rows):
            arr[i][j]=Caselles

def PosicionamentJugador(x,y):
    arr[y][x] = Jugador

def PosicionamentObjectiu(xObj_,yObj_):
    #aqui definim unes coordenades per spawnejar a lobjectiu '.'
    arr[yObj_][xObj_] = Objectiu
    
def SpawnejaObjectiu():
    xObj = rd(0, cols-1)
    yObj = rd(0, rows-1)
    return(xObj,yObj)

def Contador(score_):
    score_+=1
    return(score_)

#SETUP
print("___Caçapomes___")
print("Sortir: 'x' | Amunt: 'w' | Abaix: 's' | Esquerra: 'a' | Dreta: 'd'")
coordsObj = SpawnejaObjectiu()
PosicionamentObjectiu(coordsObj[0],coordsObj[1])
PosicionamentJugador(x,y)
Dibuixa()


#LOOP
while estaJugant:

    inputJugador=input(f"Punts:{score} >>").lower()#[0]
    match inputJugador:
        case 'x':
            estaJugant = False

        case 'w':
            if y-1<0:
                pass
            else:
                y-=1

        case 'a':
            if x-1<0:
                pass
            else:
                x-=1

        case 's':
            if y+1==rows:
                pass
            else:
                y+=1

        case 'd':
            if x+1==cols:
                pass
            else:
                x+=1

    Clear()
    
    PosicionamentJugador(x,y)
    if x==coordsObj[0] and y == coordsObj[1]:
        coordsObj = SpawnejaObjectiu()
        score=Contador(score)
    PosicionamentObjectiu(coordsObj[0],coordsObj[1])
    Dibuixa()

    #WINCASE
    if score == 10:
        estaJugant = False
print(f"Puntuiació Total:{score}")

if score == 10: 
    print("Has guanyat!")





    