from random import randint
from time import sleep

def testcalcul():
    a=randint(2,10)
    b=randint(2,9)
    print("Calculez de tête",a,"x",b,)
    sleep(1)
    print("\n"*50)
    reponse=int(input("Résultat du calcul"))
    print(a*b == reponse)
