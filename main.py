from battle3 import *
#from moreoptions import *
mon1=None
mon2=None
p1.ai=False
p2.ai=True
if p1.ai is False:
    showmon(p1)
    mon=input(" Choose your leading mon: ")
    if mon not in ["1","2","3","4","5","6"]:
        mon=random.randint(1,6)
        mon1=p1.pokemons[mon-1]
    if mon in ["1","2","3","4","5","6"]:
        mon=int(mon)
        mon1=p1.pokemons[mon-1]
if p1.ai is True:
    mon1=p1.pokemons[random.randint(1,len(p1.pokemons))-1]
if p2.ai is False:
    showmon(p2)
    mon=input(" Choose your leading mon: ")
    if mon not in ["1","2","3","4","5","6"]:
        mon=random.randint(1,6)
        mon2=p2.pokemons[mon-1]
    if mon in ["1","2","3","4","5","6"]:
        mon=int(mon)
        mon2=p2.pokemons[mon-1]         
if p2.ai is True:
    mon2=p2.pokemons[random.randint(1,len(p2.pokemons)-1)]
print()
battle(mon1,mon2,p1,p2)