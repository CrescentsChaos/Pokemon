from pokemonbase2 import *
from pokemonlist import *
def showallmon():
    n=0
    for i in allmon:
        x=i()
        n+=1
        if "Alpha" in x.name or "Totem" in x.name:
            x.name=x.name[6:]
        if "Z-Crystal" in x.name:
            x.name=x.name.split("(")[0]
        print(str(n)+"."+x.name,end=" ")
showallmon()        