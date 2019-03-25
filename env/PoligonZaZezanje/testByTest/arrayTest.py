# prvo, napraviti nekoliko lista
# globalni zadatak je :  kako pokrenuti metod kad se desi pucanje i da nastavi gde je stao
# zadnji clan liste nad kojim je izvrsena metoda plus jedan daje index za sledeci ciklus
# jedna od metoda daje paramtre kao sto je stranica od koje treba poceti
# kada treba da predje na drugu stranicu
#
import math
array = range(0,500)

appendList = []

for a in array:
    appendList.append(a)

lengthAppendList = len(appendList)
print(appendList)

placeInList = 360

# for l in range(placeInList, lengthAppendList):
#     print('obradjuje se ' + str(l))

def pageToStart(i):
    startPage = math.floor(i/100)
    startListMember = i - (startPage*100)
    for l in range(placeInList, lengthAppendList):
        print('obradjuje se ' + str(l))
    print(startPage)
    print(startListMember)

# pageToStart(i=placeInList)

def recoverMethod(l):

    if l == placeInList:
        pageToStart(i=l+1)

# recoverMethod(l=placeInList)