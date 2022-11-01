from attack import *
from moves import *
from trainerlist import *
from intros import intro
#SCOREBOARD
def  score(x,y,p1,p2,turn):
    print("")
    if x==None:
        x=p1.pokemons[0]
    if y==None:
        y=p2.pokemons[0]
        pass
    print(f" {p1.name}:")
    if len(p1.hazard)==0:
        print(" Hazard:",None)
    if len(p1.hazard)!=0:
        print(" Hazard:",end=" ")
        for i in range(len(p1.hazard)):
            if len(p1.hazard)!=1:
                print(p1.hazard[i],end=",")
            else:
                print(p1.hazard[i])
    if p1.reflect==True:
        print(f" 🪞 Reflect({p1.rfendturn-turn+1} turns left)")   
    if p1.lightscreen==True:              
        print(f" 🔲 Light Screen({p1.screenend-turn+1} turns left)")        
    print(f" Lv.{x.level} {x.name}: {x.hp}/{x.maxhp}({round((x.hp/x.maxhp)*100,2)}%)[{x.status}]")
    if x.teratype is not None:
        print(f" Type:{x.teratype} Ability: {x.ability} Item: {x.item}")
    if x.teratype is None and x.type2 is None and (p1.ai is False or (True in (p1.ai,p2.ai))):
        print(f" Type:{x.type1} Ability: {x.ability} Item: {x.item}")
    if x.teratype is None and x.type2 is not None and (p1.ai is False or (True in (p1.ai,p2.ai))):
        print(f" Type:{x.type1}/{x.type2} Ability: {x.ability} Item: {x.item}")
    if p1.ai is False or (True in (p1.ai,p2.ai)):        
        print(f" Atk: {round(x.atk)}({round(x.atkb,2)}) Def: {round(x.defense)}({round(x.defb,2)}) SpA: {round(x.spatk)}({round(x.spatkb,2)}) SpD: {round(x.spdef)}({round(x.spdefb,2)}) Spe: {round(x.speed)}({round(x.speedb,2)})")
    print("")
    print(f" {p2.name}:")
    if len(p2.hazard)==0:
        print(" Hazard:",None)
    if len(p2.hazard)!=0:
        print(" Hazard:",end=" ")
        for i in range(len(p2.hazard)):
            if len(p2.hazard)!=1:
                print(p2.hazard[i],end=",")
            else:
                print(p2.hazard[i])
    if p2.reflect==True:
        print(f" 🪞 Reflect({p2.rfendturn-turn+1} turns left)")     
    if p2.lightscreen==True:        
        print(f" 🔲 Light Screen({p2.screenend-turn+1} turns left)")               
    print(f" Lv.{y.level} {y.name}: {y.hp}/{y.maxhp}({round((y.hp/y.maxhp)*100,2)}%)[{y.status}]")
    if y.teratype is not None:
        print(f" Type:{y.teratype} Ability: {y.ability} Item: {y.item}")
    if y.teratype is None and y.type2 is None and (p2.ai is False or (True in (p1.ai,p2.ai))):
        print(f" Type:{y.type1} Ability: {y.ability} Item: {y.item}")
    if y.teratype is None and y.type2 is not None and (p2.ai is False or (True in (p1.ai,p2.ai))):
        print(f" Type:{y.type1}/{y.type2} Ability: {y.ability} Item: {y.item}")
    if p2.ai is False or (True in (p1.ai,p2.ai)):
        print(f" Atk: {round(y.atk)}({round(y.atkb,2)}) Def: {round(y.defense)}({round(y.defb,2)}) SpA: {round(y.spatk)}({round(y.spatkb,2)}) SpD: {round(y.spdef)}({round(y.spdefb,2)}) Spe: {round(y.speed)}({round(y.speedb,2)})\n")
    if field.weather=="Primordial Sea" and (x.ability!="Primordial Sea" and y.ability!="Primordial Sea" ):
        field.weather=None
        print (" The heavy rainfall stopped./n")
    if field.weather=="Desolate Land" and (x.ability!="Desolate Land" and  y.ability!="Desolate Land" ):
        field.weather=None
        print (" The extreme sunlight fade away./n")     
#FAINTED        
def faint(mon,mon2,trainer,trainer2,field,turn):
    if mon.hp<=0:
        mon.hp=0
        mon.status="Fainted"
        if mon.dmax is True:
            mon.dmax=False
            name=mon.name.split(" ")[-1]
            print(f" 🔻 {name} returned to it's normal state!")
        if "Mega " in mon.name:
            name=mon.name.split(" ")[-1]
            if "Mewtwo" in mon.name:
                name="Mewtwo"
            if "Charizard" in mon.name:
                name="Charizard"
            print(f" 🧬 {mon.name} returned to it's normal state!")
            mon.name=name
        if mon.owner==trainer.name:
            trainer.faintedmon.append(mon)
        print(f" \n 🏁 Refree: {mon.name} is unable to battle!")
        print(f" \n 🪦 {trainer.name}'s {mon.name} fainted!\n")
        if mon2.ability=="Beast Boost":
            print(f" {mon2.name}'s {mon2.ability}.")
            if "Buzzwole" in mon2.name:
                atkchange(mon2,0.5)
            if "Kartana" in mon2.name:
                atkchange(mon2,0.5)
            if "Guzzlord" in mon2.name:
                atkchange(mon2,0.5)
            if "Pheromosa" in mon2.name:
                speedchange(mon2,0.5)
            if "Xurkitree" in mon2.name:
                spatkchange(mon2,0.5)
            if "Celesteela" in mon2.name:
                spdefchange(mon2,0.5)
            if "Naganadel" in mon2.name:
                spatkchange(mon2,0.5)
            if "Stakataka" in mon2.name:
                defchange(mon2,0.5)
            if "Blacephalon" in mon2.name:
                spatkchange(mon2,0.5)
            if "Nihilego" in mon2.name:
                spdefchange(mon2,0.5)
        if mon2.ability=="Moxie":
            print(f" {mon2.name}'s {mon2.ability}.")
            atkchange(mon2,0.5)
        if mon2.ability=="As One" and "Ice Rider" in mon2.name:
            print(f" {mon2.name}'s {mon2.ability}.")
            atkchange(mon2,0.5)       
        if mon2.ability=="As One" and "Shadow Rider" in mon2.name:
            print(f" {mon2.name}'s {mon2.ability}.")
            spatkchange(mon2,0.5)        
        if mon2.ability=="Chilling Neigh" :
            print(f" {mon2.name}'s {mon2.ability}.")
            atkchange(mon2,0.5)    
        if mon2.ability=="Grim Neigh" :
            print(f" {mon2.name}'s {mon2.ability}.")
            spatkchange(mon2,0.5)                
        if mon in trainer.pokemons:
            mon.status="Fainted"
            mon.hp=0
            trainer.pokemons.remove(mon)
        if len(trainer.pokemons)!=0:
            mon=switch(mon,mon2,trainer,trainer2,field,turn)
            if mon.hp<=0:
                faint(mon,mon2,trainer,trainer2,field,turn)
        return mon
    else:
        pass
      
#ACTION             
def action(tr):
    if tr.ai is False:
        while True:
            print("\n Actions:\n 1.Fight\n 2.Switch\n 3.Forfeit\n 4.Pokemons\n 5.Smogonify\n")
            actionx= input(f"{tr.name}: What you wanna do?\n>>")
            if actionx in ["1","2","3"]:
                actionx=int(actionx)
            if actionx=="5":
                print(showsmogon(tr))
                action(tr)
            if actionx=="4":
                showmon(tr)
                n=(input("Which pokemon you wanna see?\n>>"))
                if n in ["1","2","3","4","5","6"]:
                    n=int(n)
                    tr.pokemons[n-1].info()
                    movelist(tr.pokemons[n-1])
            if actionx in [1,2,3]:
                return actionx    
                break    
            if actionx=="":
                actionx=random.choices([1,2,3], weights=[99,5,0],k=1)[0]
                return actionx
                break
    if tr.ai is True:
            return 1        
def movecat(sss):
    if sss=="Flying":
        return ["Brave Bird","Sky Attack","Air Slash","Roost"] 
    if sss=="Status":
        return ["Sleep Powder","Iron Defense","Calm Mind","Swords Dance","Bulk Up","Recover","Roost","Thunder Wave","Lunar Blessing","Take Heart","Heart Swap","Will-O-Wisp","Moonlight","Synthesis","Morning Sun","Rain Dance","Sunny Day","Hail","Sandstorm","Dark Void","Trick Room","Nasty Plot","Shell Smash","Dragon Dance","Belly Drum","Spore","Hypnosis","Rest","Coil","Curse","Strength Sap","Leech Seed","Protect"]
    if sss=="Priority":
        return ["Mach Punch","Bullet Punch","Sucker Punch","Fake Out","Extreme Speed","Protect","Aqua Jet","Shadow Sneak","Accelerock","Ice Shard","Water Shuriken","Spiky Shield","King's Shield","Baneful Bunker","Max Guard"]
def randomweather(turn,x,y,field):
    trn="Normal"
    ch=random.choices(["Clear","Rainy","Cloudy","Sandstorm","Hail","Sunny","Thunderstorm"], weights=[90,1,10,1,1,1,1],k=1)[0]    
    if ch=="Clear":
        print("\n 🌥️The weather looks clear!\n")
    if ch=="Cloudy":
        print("\n ☁️The weather is very gloomy!\n")      
    if ch=="Sunny":
        print("\n ☀️The sunlight is harsh!\n")     
#        field.sunturn=turn
#        field.sunend(x,y)   
    if ch=="Hail":
        print("\n 🌨️It's hailing!\n")      
#        field.hailturn=turn
#        field.hailend(x,y)
    if ch=="Sandstorm":
        print("\n 🏜️The sandstorm is raging!\n")
#        field.sandturn=turn
#        field.sandend(x,y)
    if ch=="Rainy":
        print("\n 🌧️It's raining!\n")    
#        field.rainturn=turn
#        field.rainend(x,y)        
    if ch=="Thunderstorm":
        print("\n ⛈️The thunderstorm is getting furious!\n")
        ch="Rainy"
        trn="Electric"
    return ch,trn
#SKIP
def skip():
    skip=False
    while skip==False:
        kk=input("\n Do you want to skip this turn?\n >>> ")
        if kk!=None:
            skip=True
#BATTLE
def battle(x,y,tr1,tr2):
    turn=0
    print("===================================================================================")
    field.weather,field.terrain=randomweather(turn,x,y,field)
    intro(tr1,tr2)
    intro(tr2,tr1)
    if x.speed>=y.speed:
        entryeff(x,y,tr1,tr2,field,turn)
        entryeff(y,x,tr2,tr1,field,turn)
        
    if y.speed>x.speed:
        entryeff(y,x,tr2,tr1,field,turn)
        entryeff(x,y,tr1,tr2,field,turn)
    while True:
        flyingmove=movecat("Flying")
        statusmove=movecat("Status")
        turn+=1
        print("===================================================================")
        print(" TURN:",turn)
        print("===================================================================")
        if field.weather=="Desolate Land":
            print(f" Weather: 🌋 Extremely Harsh Sunlight")
        if field.weather=="Primordial Sea":
            print(f" Weather: 🌊 Heavy Rain")
        if field.weather=="Rainy" and field.terrain=="Grassy":
            print(f" Weather: 🐸 Swampy ({field.rainendturn-turn} turns left)")
        if field.weather=="Rainy" and field.terrain=="Electric":
            print(f" Weather: ⛈️ Thunderstorm ({field.rainendturn-turn} turns left)")
        if field.weather=="Strong Wind" and field.terrain=="Electric":
            print(f" Weather: 🌪️ Hurricane")
        if field.weather=="Hail":
            print(f" Weather: ❄️ {field.weather} ({field.hailendturn-turn} turns left)")
        if field.weather=="Clear":
            print(f" Weather: 🌥️ {field.weather}")
            ch=random.randint(1,100)
            if 95>=ch>90:
                print(" ☀️ The sun is so bright all of a sudden!")
                field.weather="Sunny"  
            if ch>95:
                print(" 🌥️ The weather got cloudy all of a sudden!")
                field.weather="Cloudy"
        if field.weather=="Cloudy":
            print(f" Weather: ☁️ {field.weather}")
            ch=random.randint(1,100)
            if 90>=ch>85:
                print(" 🌥️ The clouds subsided!")
                field.weather="Clear"     
            if 95>=ch>90:
                print(" 🌨️ It started to hail!")
                field.weather="Hail"        
            if ch>95:
                print(" 🌧️ It started to rain!")
                field.weather="Rainy"        
        if field.weather=="Rainy" and field.terrain not in ["Electric","Grassy"]:
            print(f" Weather: ☔ {field.weather} ({field.rainendturn-turn} turns left)")
            ch=random.randint(1,100)
            if ch>95:
                print(" ⛈️ A thunderstorm was created suddenly!")
                field.weather="Rainy"
                field.terrain="Electric"                        
        if field.weather=="Sunny":
            print(f" Weather: ☀️ {field.weather} ({field.sunendturn-turn} turns left)")
            ch=random.randint(1,100)
            if ch>95:
                print(" 🏜️ A sandstorm was created suddenly!")
                field.weather="Sandstorm"
        if field.weather=="Sandstorm":
            print(f" Weather: 🏜️ {field.weather} ({field.sandendturn-turn} turns left)")    
        if field.terrain=="Misty":      
            print(f" Terrain: 🌸 {field.terrain} ({field.misendturn-turn} turns left)")
        if field.terrain=="Psychic":      
            print(f" Terrain: 👁️ {field.terrain} ({field.psyendturn-turn} turns left)")
        if field.terrain=="Normal":      
            print(" Terrain: 🌐 "+field.terrain)
        if field.terrain=="Electric":      
            print(f" Terrain: ⚡ {field.terrain} ({field.eleendturn-turn} turns left)")
        if field.terrain=="Grassy":      
            print(f" Terrain: 🌿 {field.terrain} ({field.grassendturn-turn} turns left)")
        if field.trickroom is True:
            print(f" Dimension: 🌀 Trick Room ({field.troomendturn-turn} turns left)")           
        print(f" \n ⏩⏩ {tr1.name} 🆚 {tr2.name} ⏪⏪\n")
        print(f" \n ⏩⏩ Lv.{x.level} {x.name} 🆚 {y.name} Lv.{y.level} ⏪⏪\n")
        prebuff(x,tr1,turn,field)
        prebuff(y,tr2,turn,field)
        switchAI(x,y,tr1,tr2, field)
        switchAI(y,x,tr2,tr1,field)
        #score(x,y,p1,p2,turn)
        action1=action(tr1)
        action2=action(tr2)
        check=len(moveAI(y,x,tr2,tr1,field)[1])
        check2=len(moveAI(x,y,tr1,tr2,field)[1])
        if p1AI is True:
            action1=decision(x,y,tr1,tr2,field)
        if p2AI is True:
            action2=decision(y,x,tr2,tr1,field)
        #print(action1,action2)
        if  action1==3 and action2!=3:
            print(f" {tr1.name} forfeited.")
            break
        if  action2==3 and action1!=3:
            print(f" {tr2.name} forfeited.")
            break
        if action1==2 and len(tr1.pokemons)==1:
            action1=1
        if action2==2 and len(tr2.pokemons)==1:
            action2=1
#IF BOTH CHOOSES TO ATTACK
        if action1==1 and action2==1:
            score(x,y,p1,p2,turn)
            choice1=fchoice(x,tr1)
            choice2=fchoice(y,tr2)    
            prioritymove=movecat("Priority")
            if p1.ai==True:              
                choice1=moveAI(x,y,tr1,tr2,field)[0]
            if p1.ai==False:     
                if x.dmax is True:
                    choice1=x.maxmove[choice1-1]
                if x.dmax is False:
                    choice1=x.moves[choice1-1]
            if x.ability=="Prankster":
                prioritymove+=statusmove
            if x.ability=="Gale Wings":
                prioritymove+=flyingmove
            prioritymove=movecat("Priority")   
            if p2.ai==True:  
                choice2=moveAI(y,x,tr2,tr1,field)[0]     
            if p2.ai==False:   
                if y.dmax is False:
                    choice2=y.moves[choice2-1]     
                if y.dmax is True:
                    choice2=y.maxmove[choice2-1]
            if y.ability=="Prankster":
                prioritymove+=statusmove
            if y.ability=="Gale Wings":
                prioritymove+=flyingmove
            
#P1 PRIORITY            
            if choice1 in prioritymove and choice2 not in prioritymove:
                weather(x,y)
                x=attack(x,y,tr1,tr2,choice1,choice2,field,turn)
                statchange(x,tr1,turn)
                statchange(y,tr2,turn)
                if x.hp<=0:
                    x=faint(x,y,tr1,tr2,field,turn)
                    if len(tr1.pokemons)==0:
                        print(" "+tr2.name,"wins.")
                        break
                elif y.hp>0:
                     
                    y=attack(y,x,tr2,tr1,choice2, choice1,field,turn)
                    effects (x,y,turn)
                    effects(y,x,turn)
                    statchange(x,tr1,turn)
                    statchange(y,tr2,turn)
                    if x.hp<=0:
                        x=faint(x,y,tr1,tr2,field,turn)
                        if len(tr1.pokemons)==0:
                            print(" "+tr2.name,"wins.")
                            break
                    if y.hp<=0:
                        y=faint(y,x,tr2,tr1,field,turn)
                        if len(tr2.pokemons)==0:
                            print(" "+tr1.name,"wins.")
                            break
                if y.hp<=0:
                    y=faint(y,x,tr2,tr1,field,turn)
                    effects(x,y,turn)
                    if x.hp<=0:
                        x=faint(x,y,tr1,tr2,field,turn)
                        if len(tr1.pokemons)==0:
                            print(" "+tr2.name,"wins.")
                            break
                    if len(tr2.pokemons)==0:
                        print(" "+tr1.name,"wins.")
                        break
                skip()
#P2 PRIORITY 
            elif choice2 in prioritymove and choice1 not in prioritymove:
                weather(y,x)
                 
                y=attack(y,x,tr2,tr1,choice2, choice1,field,turn)
                statchange(x,tr1,turn)
                statchange(y,tr2,turn)
                if y.hp<=0:
                    y=faint(y,x,tr2,tr1,field,turn)
                    if len(tr2.pokemons)==0:
                        print(" "+tr1.name,"wins.")
                        break
                elif x.hp>0:
                     
                    x=attack(x,y,tr1,tr2,choice1,choice2,field,turn)
                    effects(y,x,turn)
                    effects (x,y,turn)
                    statchange(x,tr1,turn)
                    statchange(y,tr2,turn)
                    if y.hp<=0:
                        y=faint(y,x,tr2,tr1,field,turn)
                        if len(tr2.pokemons)==0:
                            print(" "+tr1.name,"wins.")
                            break
                    if x.hp<=0:
                        x=faint(x,y,tr1,tr2,field,turn)
                        if len(tr1.pokemons)==0:
                            print(" "+tr2.name,"wins.")
                            break
                if x.hp<=0:
                    x=faint(x,y,tr1,tr2,field,turn)
                    effects(y,x,turn)
                    if y.hp<=0:
                        y=faint(y,x,tr2,tr1,field,turn)
                        if len(tr2.pokemons)==0:
                            print(" "+tr1.name,"wins.")
                            break
                    if len(tr1.pokemons)==0:
                        print(" "+tr2.name,"wins.")
                        break
                skip()
#P1 FAST
            elif x.speed>=y.speed and field.trickroom==False:
                weather(x,y)
                 
                x=attack(x,y,tr1,tr2,choice1,choice2,field,turn)
                statchange(x,tr1,turn)
                statchange(y,tr2,turn)
                if x.hp<=0:
                    x=faint(x,y,tr1,tr2,field,turn)
                    if len(tr1.pokemons)==0:
                        print(" "+tr2.name,"wins.")
                        break
                elif y.hp>0:
                     
                    
                    y=attack(y,x,tr2,tr1,choice2, choice1,field,turn)
                    effects (x,y,turn)
                    effects(y,x,turn)
                    statchange(x,tr1,turn)
                    statchange(y,tr2,turn)
                    if x.hp<=0:
                        x=faint(x,y,tr1,tr2,field,turn)
                        if len(tr1.pokemons)==0:
                            print(" "+tr2.name,"wins.")
                            break
                    if y.hp<=0:
                        y=faint(y,x,tr2,tr1,field,turn)
                        if len(tr2.pokemons)==0:
                            print(" "+tr1.name,"wins.")
                            break
                if y.hp<=0:
                    y=faint(y,x,tr2,tr1,field,turn)
                    effects(x,y,turn)
                    if x.hp<=0:
                        x=faint(x,y,tr1,tr2,field,turn)
                        if len(tr1.pokemons)==0:
                            print(" "+tr2.name,"wins.")
                            break
                    if len(tr2.pokemons)==0:
                        print(" "+tr1.name,"wins.")
                        break
                skip()
#P2 FAST (TRICK ROOM)
            elif x.speed<y.speed and field.trickroom==True:
                weather(x,y)
                 
                x=attack(x,y,tr1,tr2,choice1,choice2,field,turn)
                statchange(x,tr1,turn)
                statchange(y,tr2,turn)
                if x.hp<=0:
                    x=faint(x,y,tr1,tr2,field,turn)
                    if len(tr1.pokemons)==0:
                        print(" "+tr2.name,"wins.")
                        break
                elif y.hp>0:
                     
                    y=attack(y,x,tr2,tr1,choice2, choice1,field,turn)
                    effects (x,y,turn)
                    effects(y,x,turn)
                    statchange(x,tr1,turn)
                    statchange(y,tr2,turn)
                    if x.hp<=0:
                        x=faint(x,y,tr1,tr2,field,turn)
                        if len(tr1.pokemons)==0:
                            print(" "+tr2.name,"wins.")
                            break
                    if y.hp<=0:
                        y=faint(y,x,tr2,tr1,field,turn)
                        if len(tr2.pokemons)==0:
                            print(" "+tr1.name,"wins.")
                            break
                if y.hp<=0:
                    y=faint(y,x,tr2,tr1,field,turn)
                    effects(x,y,turn)
                    if x.hp<=0:
                        x=faint(x,y,tr1,tr2,field,turn)
                        if len(tr1.pokemons)==0:
                            print(" "+tr2.name,"wins.")
                            break
                    if len(tr2.pokemons)==0:
                        print(" "+tr1.name,"wins.")
                        break
                skip()
#P2 FAST
            elif y.speed>x.speed and field.trickroom==False:
                weather(y,x)
                 
                y=attack(y,x,tr2,tr1,choice2, choice1,field,turn)
                statchange(x,tr1,turn)
                statchange(y,tr2,turn)
                if y.hp<=0:
                    y=faint(y,x,tr2,tr1,field,turn)
                    if len(tr2.pokemons)==0:
                        print(" "+tr1.name,"wins.")
                        break
                elif x.hp>0:
                     
                    x=attack(x,y,tr1,tr2,choice1,choice2,field,turn)
                    effects(y,x,turn)
                    effects (x,y,turn)
                    statchange(x,tr1,turn)
                    statchange(y,tr2,turn)
                    if y.hp<=0:
                        y=faint(y,x,tr2,tr1,field,turn)
                        if len(tr2.pokemons)==0:
                            print(" "+tr1.name,"wins.")
                            break
                    if x.hp<=0:
                        x=faint(x,y,tr1,tr2,field,turn)
                        if len(tr1.pokemons)==0:
                            print(" "+tr2.name,"wins.")
                            break
                if x.hp<=0:
                    x=faint(x,y,tr1,tr2,field,turn)
                    effects(y,x,turn)
                    if y.hp<=0:
                        y=faint(y,x,tr2,tr1,field,turn)
                        if len(tr2.pokemons)==0:
                            print(" "+tr1.name,"wins.")
                            break
                    if len(tr1.pokemons)==0:
                        print(" "+tr2.name,"wins.")
                        break
                skip()
#P2 FAST (TRICK ROOM)
            elif y.speed<=x.speed and field.trickroom==True:
                weather(y,x)
                 
                y=attack(y,x,tr2,tr1,choice2, choice1,field,turn)
                statchange(x,tr1,turn)
                statchange(y,tr2,turn)
                if y.hp<=0:
                    y=faint(y,x,tr2,tr1,field,turn)
                    if len(tr2.pokemons)==0:
                        print(" "+tr1.name,"wins.")
                        break
                elif x.hp>0:
                     
                    x=attack(x,y,tr1,tr2,choice1,choice2,field,turn)
                    effects(y,x,turn)
                    effects (x,y,turn)
                    statchange(x,tr1,turn)
                    statchange(y,tr2,turn)
                    if y.hp<=0:
                        y=faint(y,x,tr2,tr1,field,turn)
                        if len(tr2.pokemons)==0:
                            print(" "+tr1.name,"wins.")
                            break
                    if x.hp<=0:
                        x=faint(x,y,tr1,tr2,field,turn)
                        if len(tr1.pokemons)==0:
                            print(" "+tr2.name,"wins.")
                            break
                if x.hp<=0:
                    x=faint(x,y,tr1,tr2,field,turn)
                    effects(y,x,turn)
                    if y.hp<=0:
                        y=faint(y,x,tr2,tr1,field,turn)
                        if len(tr2.pokemons)==0:
                            print(" "+tr1.name,"wins.")
                            break
                    if len(tr1.pokemons)==0:
                        print(" "+tr2.name,"wins.")
                        break
                skip()
#P1 SWITCH AND P2 ATTACK                
        elif action1==2 and action2==1:
            choice1=None
            score(x,y,p1,p2,turn)
            choice2=fchoice(y,tr2)  
            if p2.ai==True:             
                choice2=moveAI(y,x,tr2,tr1,field)[0]    
            if p2.ai==False:
                if y.dmax is True:
                    choice2=y.maxmove[choice2-1]
                if y.dmax is False:
                    choice2=y.moves[choice2-1]
            weather(y,x)
            x=switch(x,y,tr1,tr2,field,turn)
            y=attack(y,x,tr2,tr1,choice2, choice1,field,turn)
            effects(x,y,turn)
            effects(y,x,turn)
            statchange(x,tr1,turn)
            statchange(y,tr2,turn)
            if y.hp<=0:
                y=faint(y,x,tr2,tr1,field,turn)
                if len(tr2.pokemons)==0:
                    print(" "+tr1.name,"wins.")
                    break
            if x.hp<=0:
                x=faint(x,y,tr1,tr2,field,turn)
                if len(tr1.pokemons)==0:
                    print(" "+tr2.name,"wins.")
                    break
            y.protect=False
            skip()
#P1 ATTACKS AND P2 SWITCHES                
        elif action1==1 and action2==2:
            choice2=None
            score(x,y,p1,p2,turn)
            choice1=fchoice(x,tr1)
            if p1.ai==True:
                choice1=moveAI(x,y,tr1,tr2,field)[0]  
            if p1.ai==False:
                if x.dmax is True:
                    choice1=x.moves[choice1-1]    
                if x.dmax is False:
                    choice1=x.moves[choice1-1]        
            weather(y,x)
            y=switch(y,x,tr2,tr1,field,turn)
            x=attack(x,y,tr1,tr2,choice1,choice2,field,turn)
            if x.hp<=0:
                x=faint(x,y,tr1,tr2,field,turn)
                if len(tr1.pokemons)==0:
                    print(" "+tr2.name,"wins.")
                    break
            effects(y,x,turn)
            effects(x,y,turn)
            statchange(x,tr1,turn)
            statchange(y,tr2,turn)
            if x.hp<=0:
                x=faint(x,y,tr1,tr2,field,turn)
                if len(tr1.pokemons)==0:
                    print(" "+tr2.name,"wins.")
                    break
            if y.hp<=0:
                y=faint(y,x,tr2,tr1,field,turn)
                if len(tr2.pokemons)==0:
                    print(" "+tr1.name,"wins.")
                    break
            x.protect=False
            skip()
#IF BOTH SWITCHES                
        elif action1==2 and action2==2:
            y=switch(y,x,tr2,tr1,field,turn)
            x=switch(x,y,tr1,tr2,field,turn)       
            effects(y,x,turn)
            if y.hp<=0:
                y=faint(y,x,tr2,tr1,field,turn)
                if len(tr2.pokemons)==0:
                    print(" "+tr1.name,"wins.")
                    break
            effects(x,y,turn)              
            if x.hp<=0:
                x=faint(x,y,tr1,tr2,field,turn)
                if len(tr1.pokemons)==0:
                    print(" "+tr2.name,"wins.")
                    break   
                skip()                    
