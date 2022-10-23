from attack import *
from moves import *
from trainerlist import *
from intros import intro
#SCOREBOARD
def  score(x,y,p1,p2):
    print("")
    if x==None:
        x=p1.pokemons[0]
    if y==None:
        y=p2.pokemons[0]
        pass
    print(f"{p1.name}:")
    print(f"Lv.{x.level} {x.name}: {x.hp}/{x.maxhp}({round((x.hp/x.maxhp)*100,2)}%)[{x.status}] [{x.item}]")
    if x.type2 is None:
        print(f"Type:{x.type1} Ability: {x.ability}")
    if x.type2 is not None:
        print(f"Type:{x.type1}/{x.type2} Ability: {x.ability}")
    print(f"ATK: {round(x.atkb,2)} DEF: {round(x.defb,2)} SPATK: {round(x.spatkb,2)} SPDEF: {round(x.spdefb,2)} SPD: {round(x.speedb,2)}")
    print("")
    print(f"{p2.name}:")
    print(f"Lv.{y.level} {y.name}: {y.hp}/{y.maxhp}({round((y.hp/y.maxhp)*100,2)}%)[{y.status}] [{y.item}]")
    if y.type2 is None:
        print(f"Type:{y.type1} Ability: {y.ability}")
    if y.type2 is not None:
        print(f"Type:{y.type1}/{y.type2} Ability: {y.ability}")
    print(f"ATK: {round(y.atkb,2)} DEF: {round(y.defb,2)} SPATK: {round(y.spatkb,2)} SPDEF: {round(y.spdefb,2)} SPD: {round(y.speedb,2)}\n")
    if field.weather=="Primordial Sea" and (x.ability!="Primordial Sea" and y.ability!="Primordial Sea" ):
        field.weather=None
        print ("The heavy rainfall stopped./n")
    if field.weather=="Desolate Land" and (x.ability!="Desolate Land" and  y.ability!="Desolate Land" ):
        field.weather=None
        print ("The extreme sunlight fade away./n")     
#FAINTED        
def faint(mon,mon2,tr1,tr2,field):
    if mon.hp<=0:
        mon.hp=0
        mon.status="Fainted"
        print(f"\nRefree: {mon.name} is unable to battle!")
        print(f"\n{tr1.name}'s {mon.name} fainted.\n")
        if mon2.ability=="Beast Boost":
            print(f"{mon2.name}'s {mon2.ability}.")
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
            print(f"{mon2.name}'s {mon2.ability}.")
            atkchange(mon2,0.5)
        if mon2.ability=="As One":
            print(f"{mon2.name}'s {mon2.ability}.")
            atkchange(mon2,0.5)        
        if mon in tr1.pokemons:
            tr1.pokemons.remove(mon)
        if len(tr1.pokemons)!=0:
            mon=switch(mon,mon2,tr1,tr2,field)
            if mon.hp<=0:
                faint(mon,mon2,tr1,tr2,field)
#        if mon is None:
#            mon=switch(mon,tr,mon2)
        return mon
    else:
        pass



    
#PreMatch 
def prematch(tr1,tr2):            
    alpha1=0
    alpha2=0
    mega1=0
    mega2=0           
    for i in (tr1.pokemons):
        if "Alpha " in i.name:
            alpha1+=1
        if "Primal " in i.name:
            nm=i.name.split(" ")[-1]
            print(f"{nm}'s Primal Reversion! It reverted to its primal form!\n")
        if "Mega " in i.name:
            mega1+=1
            if "Charizard" not in i.name:
                nm=i.name.split(" ")[-1]
                print(f"{nm}'s {i.item} reacted to {tr1.name}'s Keystone and turned into {i.name}.\n")
            else:
                if "X" in i.name:
                    nm="Charizard"
                    print(f"{nm}'s {i.item} reacted to {tr1.name}'s Keystone  and turned into {i.name}.\n")
                else:
                    nm="Charizard"
                    print(f"{nm}'s {i.item} reacted to {tr1.name}'s Keystone  and turned into {i.name}.\n")
    for i in tr2.pokemons:
        if "Alpha " in i.name:
            alpha2+=1
        if "Primal " in i.name:
            nm=i.name.split(" ")[-1]
            print(f"{nm}'s Primal Reversion! It reverted to its primal form!\n")
        if "Mega " in i.name:
            mega2+=1
            if "Charizard" not in i.name:
                nm=i.name.split(" ")[-1]
                print(f"{nm}'s {i.item} reacted to {tr2.name}'s Keystone  and turned into {i.name}.\n")
            else:
                if "X" in i.name:
                    nm="Charizard"
                    print(f"{nm}'s {i.item} reacted to {tr2.name}'s Keystone  and turned into {i.name}.\n")
                else:
                    nm="Charizard"
                    print(f"{nm}'s {i.item} reacted to {tr2.name}'s Keystone  and turned into {i.name}.\n")
    if mega1==1 and mega2==1:
        vc=random.choice([tr1,tr2])            
        print(f"{vc.name}: Guess it's gonna be battle of Mega Evolutions!")
    if mega1==1 and mega2==0:   
        print(f"{tr2.name}: Mega Evolution doesn't mean anything to me.")
    if mega1==0 and mega2==1:      
        print(f"{tr1.name}: Let's see if my buddies are ready for your Mega Evolution!")
    if alpha1>3:
        print(f"{tr2.name}: Those giants won't help you wjn against me.")      
    if alpha2>3:
         print(f"{tr1.name}: Are you a alpha hunter or something?")         
         
#ACTION             
def action(tr):
       
    while True:
        print("\nActions:\n1.Fight\n2.Switch\n3.Forfeit\n4.Pokemons\n5.Smogonify\n")
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
                action(tr)
            else:
                action(tr)
        
        if actionx in [1,2,3]:
            return actionx    
            break    
        else:
            actionx=random.choices([1,2,3], weights=[99,5,0],k=1)[0]
            return actionx
            break

def movecat(sss):
    if sss=="Flying":
        return ["Brave Bird","Sky Attack","Air Slash","Roost"] 
    if sss=="Status":
        return ["Sleep Powder","Iron Defense","Calm Mind","Swords Dance","Bulk Up","Recover","Roost","Thunder Wave","Lunar Blessing","Take Heart","Heart Swap","Will-O-Wisp","Moonlight","Synthesis","Morning Sun","Rain Dance","Sunny Day","Hail","Sandstorm","Dark Void","Trick Room","Nasty Plot","Shell Smash","Dragon Dance","Belly Drum","Spore","Hypnosis","Rest","Coil","Curse","Strength Sap","Leech Seed","Protect"]
    if sss=="Priority":
        return ["Mach Punch","Bullet Punch","Sucker Punch","Fake Out","Extreme Speed","Protect","Aqua Jet","Shadow Sneak","Accelerock","Ice Shard","Water Shuriken","Spiky Shield","King's Shield"]
def randomweather():
    ch=random.choices(["Clear","Rainy","Cloudy","Sandstorm","Hail","Sunny","Thunderstorm"], weights=[90,5,10,5,5,5,1],k=1)[0]    
    if ch=="Clear":
        print("\nThe weather looks clear!\n")
    if ch=="Cloudy":
        print("\nThe weather is very gloomy!\n")      
    if ch=="Sunny":
        print("\nThe sunlight is very bright!\n")          
    if ch=="Hail":
        print("\nSeems like the hailstorm won't stop any time soon!\n")        
    if ch=="Sandstorm":
        print("\nSeems like the sandstorm won't stop any time soon!\n")         
    if ch=="Rainy":
        print("\nIt's raining continuously!\n")          
    if ch=="Thunderstorm":
        print("\nThe thunderstorm is getting furious!\n")       
        ch="Rainy"
        field.terrain="Electric"
    return ch
#SKIP
def skip():
    skip=False
    while skip==False:
        kk=input("\nDo you want to skip this turn?\n>>> ")
        if kk!=None:
            skip=True
#BATTLE
def battle(x,y,tr1,tr2):
    turn=0
    
    print("===================================================================================")
    field.weather=randomweather()
    field.terrain="Normal"
    intro(tr1,tr2)
    intro(tr2,tr1)
    entryeff(x,y,tr1,tr2,field)
    entryeff(y,x,tr2,tr1,field)
    while True:
        flyingmove=movecat("Flying")
        statusmove=movecat("Status")
        turn+=1
        print("===================================================================================")
        print("TURN:",turn)
        print("===================================================================================")
        print("Weather:",field.weather)
        print("Terrain:",field.terrain)
        print(f"\n>>> {tr1.name} vs {tr2.name} <<<\n")
        print(f"\n>>> Lv.{x.level} {x.name} vs {y.name} Lv.{y.level} <<<\n")
        switchAI(x,y,tr1,tr2, field)
        switchAI(y,x,tr2,tr1,field)
        score(x,y,p1,p2)
        action1=action(tr1)
        action2=action(tr2)
        check=len(moveAI(y,x,tr2,tr1,field)[1])
        check2=len(moveAI(x,y,tr1,tr2,field)[1])
        if p1AI is True:
            oppo=moveAI(y,x,tr2,tr1,field)[2]
            my=moveAI(x,y,tr1,tr2,field)
            if x.ability=="Natural Cure" and x.status!="Alive" and len(tr1.pokemons)>1:
                action1=2
            if x.ability=="Regenerator" and x.hp<=(x.maxhp/2) and len(tr1.pokemons)>1:
                action1=2
        if p2AI is True:
            my=moveAI(y,x,tr2,tr1,field)
            oppo=moveAI(x,y,tr1,tr2,field)[1]  
            if y.ability=="Natural Cure" and y.status!="Alive" and len(tr2.pokemons)>1:
                action2=2
            if y.ability=="Regenerator" and y.hp<=(y.maxhp/2) and len(tr2.pokemons)>1:
                action2=2     
        print(action1,action2)#lol
        if  action1==3 and action2!=3:
            print(f"{tr1.name} forfeited.")
            break
        if  action2==3 and action1!=3:
            print(f"{tr2.name} forfeited.")
            break
        if action1==2 and len(tr1.pokemons)==1:
            action1=1
        if action2==2 and len(tr2.pokemons)==1:
            action2=1
#IF BOTH CHOOSES TO ATTACK
        if action1==1 and action2==1:
            score(x,y,p1,p2)
            choice1=fchoice(x,tr1)
            choice2=fchoice(y,tr2)    
            prioritymove=movecat("Priority")
            if p1AI==True:              
                choice1=moveAI(x,y,tr1,tr2,field)[0]         
            if p1AI==False:     
                choice1=x.moves[choice1-1]
            if x.ability=="Prankster":
                prioritymove+=statusmove
            if x.ability=="Gale Wings":
                prioritymove+=flyingmove
            prioritymove=movecat("Priority")   
            if p2AI==True:  
                choice2=moveAI(y,x,tr2,tr1,field)[0]     
            if p2AI==False:        
                choice2=y.moves[choice2-1]
            if y.ability=="Prankster":
                prioritymove+=statusmove
            if y.ability=="Gale Wings":
                prioritymove+=flyingmove
            
#P1 PRIORITY            
            if choice1 in prioritymove and choice2 not in prioritymove:
                weather(x,y)
                x=attack(x,y,tr1,tr2,choice1,choice2,field)
                statchange(x)
                statchange(y)
                if x.hp<=0:
                    x=faint(x,y,tr1,tr2,field)
                    if len(tr1.pokemons)==0:
                        print(tr2.name,"wins.")
                        break
                elif y.hp>0:
                     
                    y=attack(y,x,tr2,tr1,choice2, choice1,field)
                    effects (x,y)
                    effects(y,x)
                    statchange(x)
                    statchange(y)
                    if x.hp<=0:
                        x=faint(x,y,tr1,tr2,field)
                        if len(tr1.pokemons)==0:
                            print(tr2.name,"wins.")
                            break
                    if y.hp<=0:
                        y=faint(y,x,tr2,tr1,field)
                        if len(tr2.pokemons)==0:
                            print(tr1.name,"wins.")
                            break
                if y.hp<=0:
                    y=faint(y,x,tr2,tr1,field)
                    effects(x,y)
                    if x.hp<=0:
                        x=faint(x,y,tr1,tr2,field)
                        if len(tr1.pokemons)==0:
                            print(tr2.name,"wins.")
                            break
                    if len(tr2.pokemons)==0:
                        print(tr1.name,"wins.")
                        break
                skip()
#P2 PRIORITY 
            elif choice2 in prioritymove and choice1 not in prioritymove:
                weather(y,x)
                 
                y=attack(y,x,tr2,tr1,choice2, choice1,field)
                statchange(x)
                statchange(y)
                if y.hp<=0:
                    y=faint(y,x,tr2,tr1,field)
                    if len(tr2.pokemons)==0:
                        print(tr1.name,"wins.")
                        break
                elif x.hp>0:
                     
                    x=attack(x,y,tr1,tr2,choice1,choice2,field)
                    effects(y,x)
                    effects (x,y)
                    statchange(x)
                    statchange(y)
                    if y.hp<=0:
                        y=faint(y,x,tr2,tr1,field)
                        if len(tr2.pokemons)==0:
                            print(tr1.name,"wins.")
                            break
                    if x.hp<=0:
                        x=faint(x,y,tr1,tr2,field)
                        if len(tr1.pokemons)==0:
                            print(tr2.name,"wins.")
                            break
                if x.hp<=0:
                    x=faint(x,y,tr1,tr2,field)
                    effects(y,x)
                    if y.hp<=0:
                        y=faint(y,x,tr2,tr1,field)
                        if len(tr2.pokemons)==0:
                            print(tr1.name,"wins.")
                            break
                    if len(tr1.pokemons)==0:
                        print(tr2.name,"wins.")
                        break
                skip()
#P1 FAST
            elif x.speed>=y.speed and field.trickroom==False:
                weather(x,y)
                 
                x=attack(x,y,tr1,tr2,choice1,choice2,field)
                statchange(x)
                statchange(y)
                if x.hp<=0:
                    x=faint(x,y,tr1,tr2,field)
                    if len(tr1.pokemons)==0:
                        print(tr2.name,"wins.")
                        break
                elif y.hp>0:
                     
                    
                    y=attack(y,x,tr2,tr1,choice2, choice1,field)
                    effects (x,y)
                    effects(y,x)
                    statchange(x)
                    statchange(y)
                    if x.hp<=0:
                        x=faint(x,y,tr1,tr2,field)
                        if len(tr1.pokemons)==0:
                            print(tr2.name,"wins.")
                            break
                    if y.hp<=0:
                        y=faint(y,x,tr2,tr1,field)
                        if len(tr2.pokemons)==0:
                            print(tr1.name,"wins.")
                            break
                if y.hp<=0:
                    y=faint(y,x,tr2,tr1,field)
                    effects(x,y)
                    if x.hp<=0:
                        x=faint(x,y,tr1,tr2,field)
                        if len(tr1.pokemons)==0:
                            print(tr2.name,"wins.")
                            break
                    if len(tr2.pokemons)==0:
                        print(tr1.name,"wins.")
                        break
                skip()
#P2 FAST (TRICK ROOM)
            elif x.speed<y.speed and field.trickroom==True:
                weather(x,y)
                 
                x=attack(x,y,tr1,tr2,choice1,choice2,field)
                statchange(x)
                statchange(y)
                if x.hp<=0:
                    x=faint(x,y,tr1,tr2,field)
                    if len(tr1.pokemons)==0:
                        print(tr2.name,"wins.")
                        break
                elif y.hp>0:
                     
                    y=attack(y,x,tr2,tr1,choice2, choice1,field)
                    effects (x,y)
                    effects(y,x)
                    statchange(x)
                    statchange(y)
                    if x.hp<=0:
                        x=faint(x,y,tr1,tr2,field)
                        if len(tr1.pokemons)==0:
                            print(tr2.name,"wins.")
                            break
                    if y.hp<=0:
                        y=faint(y,x,tr2,tr1,field)
                        if len(tr2.pokemons)==0:
                            print(tr1.name,"wins.")
                            break
                if y.hp<=0:
                    y=faint(y,x,tr2,tr1,field)
                    effects(x,y)
                    if x.hp<=0:
                        x=faint(x,y,tr1,tr2,field)
                        if len(tr1.pokemons)==0:
                            print(tr2.name,"wins.")
                            break
                    if len(tr2.pokemons)==0:
                        print(tr1.name,"wins.")
                        break
                skip()
#P2 FAST
            elif y.speed>x.speed and field.trickroom==False:
                weather(y,x)
                 
                y=attack(y,x,tr2,tr1,choice2, choice1,field)
                statchange(x)
                statchange(y)
                if y.hp<=0:
                    y=faint(y,x,tr2,tr1,field)
                    if len(tr2.pokemons)==0:
                        print(tr1.name,"wins.")
                        break
                elif x.hp>0:
                     
                    x=attack(x,y,tr1,tr2,choice1,choice2,field)
                    effects(y,x)
                    effects (x,y)
                    statchange(x)
                    statchange(y)
                    if y.hp<=0:
                        y=faint(y,x,tr2,tr1,field)
                        if len(tr2.pokemons)==0:
                            print(tr1.name,"wins.")
                            break
                    if x.hp<=0:
                        x=faint(x,y,tr1,tr2,field)
                        if len(tr1.pokemons)==0:
                            print(tr2.name,"wins.")
                            break
                if x.hp<=0:
                    x=faint(x,y,tr1,tr2,field)
                    effects(y,x)
                    if y.hp<=0:
                        y=faint(y,x,tr2,tr1,field)
                        if len(tr2.pokemons)==0:
                            print(tr1.name,"wins.")
                            break
                    if len(tr1.pokemons)==0:
                        print(tr2.name,"wins.")
                        break
                skip()
#P2 FAST (TRICK ROOM)
            elif y.speed<=x.speed and field.trickroom==True:
                weather(y,x)
                 
                y=attack(y,x,tr2,tr1,choice2, choice1,field)
                statchange(x)
                statchange(y)
                if y.hp<=0:
                    y=faint(y,x,tr2,tr1,field)
                    if len(tr2.pokemons)==0:
                        print(tr1.name,"wins.")
                        break
                elif x.hp>0:
                     
                    x=attack(x,y,tr1,tr2,choice1,choice2,field)
                    effects(y,x)
                    effects (x,y)
                    statchange(x)
                    statchange(y)
                    if y.hp<=0:
                        y=faint(y,x,tr2,tr1,field)
                        if len(tr2.pokemons)==0:
                            print(tr1.name,"wins.")
                            break
                    if x.hp<=0:
                        x=faint(x,y,tr1,tr2,field)
                        if len(tr1.pokemons)==0:
                            print(tr2.name,"wins.")
                            break
                if x.hp<=0:
                    x=faint(x,y,tr1,tr2,field)
                    effects(y,x)
                    if y.hp<=0:
                        y=faint(y,x,tr2,tr1,field)
                        if len(tr2.pokemons)==0:
                            print(tr1.name,"wins.")
                            break
                    if len(tr1.pokemons)==0:
                        print(tr2.name,"wins.")
                        break
                skip()
#P1 SWITCH AND P2 ATTACK                
        elif action1==2 and action2==1:
            choice1=None
            score(x,y,p1,p2)
            choice2=fchoice(y,tr2)  
            if p2AI==True:             
                choice2=moveAI(y,x,tr2,tr1,field)[0]    
            if p2AI==False:
                choice2=y.moves[choice2-1]                  
            weather(y,x)
            x=switch(x,y,tr1,tr2,field)
            y=attack(y,x,tr2,tr1,choice2, choice1,field)
            effects(x,y)
            effects(y,x)
            statchange(x)
            statchange(y)
            if y.hp<=0:
                y=faint(y,x,tr2,tr1,field)
                if len(tr2.pokemons)==0:
                    print(tr1.name,"wins.")
                    break
            if x.hp<=0:
                x=faint(x,y,tr1,tr2,field)
                if len(tr1.pokemons)==0:
                    print(tr2.name,"wins.")
                    break
            y.protect=False
            skip()
#P1 ATTACKS AND P2 SWITCHES                
        elif action1==1 and action2==2:
            choice2=None
            score(x,y,p1,p2)
            choice1=fchoice(x,tr1)
            if p1AI==True:
                choice1=moveAI(x,y,tr1,tr2,field)[0]  
            if p1AI ==False:
                choice1=x.moves[choice1-1]           
            weather(y,x)
            y=switch(y,x,tr2,tr1,field)
            x=attack(x,y,tr1,tr2,choice1,choice2,field)
            if x.hp<=0:
                x=faint(x,y,tr1,tr2,field)
                if len(tr1.pokemons)==0:
                    print(tr2.name,"wins.")
                    break
            effects(y,x)
            effects(x,y)
            statchange(x)
            statchange(y)
            if x.hp<=0:
                x=faint(x,y,tr1,tr2,field)
                if len(tr1.pokemons)==0:
                    print(tr2.name,"wins.")
                    break
            if y.hp<=0:
                y=faint(y,x,tr2,tr1,field)
                if len(tr2.pokemons)==0:
                    print(tr1.name,"wins.")
                    break
            x.protect=False
            skip()
#IF BOTH SWITCHES                
        elif action1==2 and action2==2:
            y=switch(y,x,tr2,tr1,field)
            x=switch(x,y,tr1,tr2,field)       
            effects(y,x)
            if y.hp<=0:
                y=faint(y,x,tr2,tr1,field)
                if len(tr2.pokemons)==0:
                    print(tr1.name,"wins.")
                    break
            effects(x,y)              
            if x.hp<=0:
                x=faint(x,y,tr1,tr2,field)
                if len(tr1.pokemons)==0:
                    print(tr2.name,"wins.")
                    break   
                skip()                    
