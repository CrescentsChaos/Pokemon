#pylint:disable=C0303
#pylint:disable=R0912
#pylint:disable=C0116
#pylint:disable=C0103
#pylint:disable=C0103
#pylint:disable=W0401
#pylint:disable=C0304
from trainerlistx import *
print(f" 🌁 {field.location}")
p1="None"
p2="None"
#SKIP
def skip(x,y,tr1,tr2):
    skip=False
    while skip!=True:
        kk=input("\n Do you want to skip this turn? (Enter anything)\n >>> ")
        if kk=="reveal":
            if tr1.ai==True:
                print("")
                showteam(tr1)
            if tr2.ai==True:
                print("")
                showteam(tr2)
        if kk=="p2":
            skip=False
            if tr2.ai==False:
                tr2.ai=True
                print(f" ✅ {tr2.name} is being controlled by AI.")
            elif tr2.ai==True:
                tr2.ai=False
                print(f" ✅ You are controlling {tr2.name}.")  
        if kk=="p1":
            skip=False
            if tr1.ai==False:
                tr1.ai=True
                print(f" ✅ {tr1.name} is being controlled by AI.")
            elif tr1.ai==True:
                tr1.ai=False    
                print(f" ✅ You are controlling {tr1.name}.")        
        if kk=="info2":
            y.info()
            movelist(y)
            skip=False
        if kk=="info1":
            x.info()
            movelist(x)
            skip=False
        if kk=="":
            print(f" ✅ Turn skipped successfully!")
            skip=True
def characters(text,location,nm=2):
    team="None"
    num=0
    chosen="None"
    if text in ["comp"]:
        team=[genTrainer(trclass="Competitive Player")]
    if text in ["dv"]:
        team=[tonoy]
    elif text in ["e4","elite four"]:
        team=e4list
    elif text in ["hc"]:
        team=hardlist
    elif text in ["evil","villain","ev"]:
        team=evilist
    elif text in ["champ","champion","ch"]:
        team=champlist
    elif text in ["gm"]:
        team=gymlist
    elif text in ["fr"]:
        team=fronlist
    elif text in ["tl"]:
        team=talentlist
    elif text in ["ts"]:
        team=test
    elif text in ["","None","rn"]:
        team="None"
    if text!="" and team !="None":
        for i in team:
            num+=1
            print(" "+str(num)+".",i.name)
    if team =="None":
        if nm==1:
            if "Tournament" in location:
                chosen=genplayer2(field)
            else:
                chosen=random.choices([genplayer2(field),genTrainer(trclass="Pokémon Trainer")],weights=[1,15],k=1)[0]
        if nm==2:
            chosen=random.choices([genplayer2(field),genTrainer(trclass="Pokémon Trainer")],weights=[15,5],k=1)[0]
            #random.choice(gymlist), random.choice(e4list),random.choice(fronlist),random.choice(evilist),random.choice(talentlist)
    else:
        ch=input(" Enter who you wanna play with: ")
        if ch in ("rn",""):
            chosen=random.choice(team)
        else:
            ch=int(ch)
            chosen=team[ch-1]
    print(f" ✅ You have chosen {chosen.name}!\n")
    return chosen
aa=input(" Choose a catagory(e4,ev,ch,gm,fr,tl,hc): ")
p1=characters(aa,field.location,1)
bb=input(" Choose a catagory(e4,ev,ch,gm,fr,tl,hc): ")
p2=characters(bb,field.location,2)
sm1=showsmogon(p1)
sm2=showsmogon (p2)
mon1="None"
mon2="None"
play=input(f" ⚠️ Do you want to play as {p1.name} or Simulate? ('yes'/Press Enter)\n >>>").lower()
if play=="yes":
    play=False
else:
    play=True
play2=input(f" ⚠️ Do you want to play as {p2.name} or Simulate? ('yes'/Press Enter)\n >>>").lower()
print("")
if play2=="yes":
    play2=False
else:
    play2=True
p1.ai=play
p2.ai=play2
showparty(p1)
showparty (p2)
if p1.ai is False or (p1.ai,p2.ai)==(True,True):
    showteam(p1)
    print("\n")
if p2.ai is False or (p1.ai,p2.ai)==(True,True):    
    showteam(p2)
    print("\n")
if False in (p1.ai,p2.ai):
    skip("None","None",p1,p2)     
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
    if len(p1.pokemons)==1:
        mon1=p1.pokemons[0]
    else:
        mon1=p1.pokemons[random.randint(1,(len(p1.pokemons))-1)]
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