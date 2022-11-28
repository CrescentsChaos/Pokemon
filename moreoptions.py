#pylint:disable=C0303
#pylint:disable=R0912
#pylint:disable=C0116
#pylint:disable=C0103
#pylint:disable=C0103
#pylint:disable=W0401
#pylint:disable=C0304
from trainerlist import *

def characters(text,nm=1):
    print(" Text inserted:",text)
    text=text.lower()
    team=None
    num=0
    if text in ["e4","elite four"]:
        team=e4list
    if text in ["evil","villain","ev"]:
        team=evilist
    if text in ["champ","champion","ch"]:
        team=champlist
    if text in ["gm"]:
        team=gymlist
    if text in ["fr"]:
        team=fronlist
    if text in ["tl"]:
        team=talentlist
    if text in ["",None,"rn"]:
        team=None
    if text!="" and team is not None:
        for i in team:
            num+=1
            print(" "+str(num)+".",i.name)
    if team is None:
        if nm==1:
            chosen=matchx[0]
        if nm==2:
            chosen=genplayer2(field)
    else:
        ch=int(input(" Enter what you wanna play with: "))
        chosen=team[ch-1]
    print(f" ✅ You have chosen {chosen.name}!\n")
    return chosen
aa=input(" Choose a catagory(e4,ev,ch,gm,fr,tl): ")
p1=characters(aa,1)
bb=input(" Choose a catagory(e4,ev,ch,gm,fr,tl): ")
p2=characters(bb,2)
showparty(p1)
print("\n")
showparty (p2)
sm1=showsmogon(p1)
sm2=showsmogon (p2)
mon1=None
mon2=None
p1.ai=True
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
    if len(p2.pokemons)==6:
        mon2=p2.pokemons[random.randint(1,len(p2.pokemons)-1)]
    if len(p2.pokemons)==1:
        mon2=p2.pokemons[0]
print()