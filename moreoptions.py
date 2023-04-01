#pylint:disable=C0303
#pylint:disable=R0912
#pylint:disable=C0116
#pylint:disable=C0103
#pylint:disable=C0103
#pylint:disable=W0401
#pylint:disable=C0304
from fieldtrip import *
from database import *
#print(" 💥 Battle Formats:\n 1. Single Battle\n 2. Double Battle [Unavailable]")
battle="1"#input(" 🆚 Choose your battle format: ")
if battle not in ["1","2"]:
    battle="1"
p1="None"
p2="None"
#SKIP
def skip(x,y,tr1,tr2,field):
    skip=False
    while skip!=True:
        kk=input("\n Do you want to skip this turn? (Enter anything)\n >>> ")
        if kk=="ab2":
            skip=False
            abilitydesc(y.ability)
        if kk=="ab1":
            skip=False
            abilitydesc(x.ability)
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
            movelist(y,x,field)
            skip=False
        if kk=="info1":
            x.info()
            movelist(x,y,field)
            skip=False
        if kk=="":
            print(f" ✅ Turn skipped successfully!")
            skip=True
def characters(text,location,nm=2):
    team="None"
    num=0
    chosen="None"
    team_mapping = {
    "img" : [genTrainer(trclass="Chaos Trainer")],
    "comp": [genTrainer(trclass="Competitive Player")],
    "fs": [genTrainer(trclass="Fusion Trainer")],
    "dv": [tonoy],
    "e4": e4list,
    "elite four": e4list,
    "rd": [wild(random.choice(allmon))],
    "hc": hardlist,
    "evil": evilist,
    "villain": evilist,
    "ev": evilist,
    "champ": champlist,
    "champion": champlist,
    "ch": champlist,
    "gm": gymlist,
    "fr": fronlist,
    "tl": talentlist,
    "ts": test,
    "": "None",
    "None": "None",
    "rn": "None"
}
    team = team_mapping.get(text, "None")

    #if text in ["comp"]:
#        team=[genTrainer(trclass="Competitive Player")]
#    elif text in ["fs"]:
#        team=[genTrainer(trclass="Fusion Trainer")]
#    elif text in ["dv"]:
#        team=[tonoy]
#    elif text in ["e4","elite four"]:
#        team=e4list
#    elif text in ["rd"]:
#        team=raids
#    elif text in ["hc"]:
#        team=hardlist
#    elif text in ["evil","villain","ev"]:
#        team=evilist
#    elif text in ["champ","champion","ch"]:
#        team=champlist
#    elif text in ["gm"]:
#        team=gymlist
#    elif text in ["fr"]:
#        team=fronlist
#    elif text in ["tl"]:
#        team=talentlist
#    elif text in ["ts"]:
#        team=test
#    elif text in ["","None","rn"]:
#        team="None"
    if text!="" and team !="None":
        for i in team:
            num+=1
            print(" "+str(num)+".",i.name)
    if team =="None":
        if nm==1:
            if "Tournament" in location:
                chosen=genplayer2(field)
            else:
                chosen=random.choices([genplayer2(field),genTrainer(trclass="Pokémon Trainer")],weights=[1,10],k=1)[0]
        if nm==2:
            chosen=random.choices([genplayer2(field),genTrainer(trclass="Pokémon Trainer")],weights=[25,3],k=1)[0]
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
def players(n):
    x=input(" Choose a catagory(e4,ev,ch,gm,fr,tl,hc): ")
    tr=characters(x,field.location,n)
    return tr
#p1=players()
#p2=players()
#sm1=showsmogon(p1)
#sm2=showsmogon (p2)
def leadchoice(p2):            
    mon2="None"
    if p2.ai is False:
        showmon(p2)  
        if battle=="2":
            monx=input(" Choose your first mon: ")
            if monx not in ["1","2","3","4","5","6"]:
                monx=random.randint(1,6)
                mon3=p2.pokemons[monx-1]
            if monx in ["1","2","3","4","5","6"]:
                monx=int(monx)
                mon3=p2.pokemons[monx-1]   
            mony=input(" Choose your second mon: ")
            if mony not in ["1","2","3","4","5","6"]:
                while True:
                    mony=random.randint(1,6)
                    mon4=p2.pokemons[mony-1]
                    if monx!=mony:
                        break
            if mony in ["1","2","3","4","5","6"]:
                mony=int(mony)
                if p2.pokemons[mony-1]!=mon3:
                    mon4=p2.pokemons[mony-1]   
                if p2.pokemons[mony-1]==mon3:
                    while True:
                        mony=random.randint(1,6)
                        mon1=p2.pokemons[mony-1]
                        if monx!=mony:
                            break
        if battle=="1":
            mon=input(" Choose your leading mon: ")
            if mon not in ["1","2","3","4","5","6"]:
                mon=random.randint(1,6)
                mon2=p2.pokemons[mon-1]
            if mon in ["1","2","3","4","5","6"]:
                mon=int(mon)
                mon2=p2.pokemons[mon-1]   
    if p2.ai is True:
        if battle=="2":
            if len(p2.pokemons)==6:
              mon3=p2.pokemons[random.randint(1,len(p2.pokemons)-1)]
            while True:
                mon4=p2.pokemons[random.randint(1,len(p2.pokemons)-1)]
                if mon3!=mon4:
                    break 
        if battle=="1":
            if len(p2.pokemons)==6:
              mon2=p2.pokemons[random.randint(1,len(p2.pokemons)-1)]
            if len(p2.pokemons)<6:
                mon2=p2.pokemons[0]       
    if mon2=="None":
        mon2=p2.pokemons[0]        
    return mon2                    
#print(mon1,mon2)