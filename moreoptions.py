#pylint:disable=C0304
#pylint:disable=C0304
from trainerlist import *
def characters(text,nm):
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
    if text=="":
        team=None
    if text!="":
        for i in team:
            num+=1
            print(" "+str(num)+".",i.name)
    if team is None:
        if nm==1:
            chosen=matchx[0]
        if nm==2:
            chosen=genplayer2(field)
    if team is not None:
        ch=int(input(" Enter what you wannna play with: "))
        chosen=team[ch-1]
    print(f" ✅ You have chosen {chosen.name}!\n")
    return chosen
    
p1=characters(input(" Choose a catagory(e4,ev,ch,gm,fr,tl): "),1)
p2=characters(input(" Choose a catagory(e4,ev,ch,gm,fr,tl): "),2)
showparty(p1)
print("\n")
showparty (p2)
sm1=showsmogon(p1)
sm2=showsmogon (p2)