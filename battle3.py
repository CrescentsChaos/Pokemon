from attack import *
from moves import *
from trainerlist import *

statusmove=["Sleep Powder","Iron Defense","Calm Mind","Swords Dance","Bulk Up","Recover","Roost","Thunder Wave","Lunar Blessing","Take Heart","Heart Swap","Will-O-Wisp","Moonlight","Synthesis","Morning Sun","Rain Dance","Sunny Day","Hail","Sandstorm","Dark Void","Trick Room","Nasty Plot","Shell Smash","Dragon Dance","Belly Drum","Spore","Hypnosis","Rest","Coil","Curse","Strength Sap","Leech Seed","Protect"]
prioritymove=["Mach Punch","Bullet Punch","Sucker Punch","Fakeout","Extreme Speed","Protect","Aqua Jet","Shadow Sneak"]
def  score(x,y,p1,p2):
    print("")
    if x==None:
        x=p1.pokemons[0]
    if y==None:
        y=p2.pokemons[0]
        pass
    print(f"{p1.name}:")
    print(f"Lv.{x.level} {x.name}: {x.hp}/{x.maxhp}({round((x.hp/x.maxhp)*100,2)}%)[{x.status}] [{x.item}]")
   
    print(f"ATK: {round(x.atkb,2)} DEF: {round(x.defb,2)} SPATK: {round(x.spatkb,2)} SPDEF: {round(x.spdefb,2)} SPD: {round(x.speedb,2)}")
    print("")
    print(f"{p2.name}:")
    print(f"Lv.{y.level} {y.name}: {y.hp}/{y.maxhp}({round((y.hp/y.maxhp)*100,2)}%)[{y.status}] [{y.item}]")
    print(f"ATK: {round(y.atkb,2)} DEF: {round(y.defb,2)} SPATK: {round(y.spatkb,2)} SPDEF: {round(y.spdefb,2)} SPD: {round(y.speedb,2)}\n")
    if field.weather=="Primordial Sea" and (x.ability!="Primordial Sea" and y.ability!="Primordial Sea" ):
        field.weather=None
        print ("The heavy rainfall stopped./n")
    if field.weather=="Desolate Land" and (x.ability!="Desolate Land" and  y.ability!="Desolate Land" ):
        field.weather=None
        print ("The extreme sunlight fade away./n")     
        
def faint(mon,tr,mon2):
    if mon.hp<=0:
        mon.hp=0
        mon.status="Fainted"
        print(f"\nRefree: {mon.name} is unable to battle!")
        print(f"\n{tr.name}'s {mon.name} fainted.\n")
        if mon2.ability=="Moxie":
            print(f"{mon2.name}'s {mon2.ability}.")
            atkchange(mon2,0.5)
        if mon in tr.pokemons:
            tr.pokemons.remove(mon)
        if len(tr.pokemons)!=0:
            mon=switch(mon,tr,mon2)
            hazardcheck(tr,mon)
        if mon is None:
            mon=switch(mon,tr,mon2)
            hazardcheck(tr,mon)
        return mon
    else:
        pass


def fchoice(pk,tr):
    #print(len(pk.moves))
    
    movelist(pk)
    choice=input(f"{tr.name}: Choose a move.\n>>")
    if choice in ["1","2","3","4","5","6"]:
        choice=int(choice)
    else:
        choice=random.randint(1,len(pk.moves))
    return choice
    
def intro (tr,sr):
    srname=sr.name.split(" ")[-1]
    if "Red" in tr.name:
        print(f"{tr.name}: ........")
    if "Cynthia" in tr.name:
        print(f"{tr.name}: One look at you tells me many things about you. Together, you and your Pokémon overcame all the challenges you faced, however difficult. It means that you've triumphed over any personal weaknesses, too. The power you learned... I can feel it emanating from you. That's enough talking. Let's get on with why you're here. I, Cynthia, accept your challenge as the Pokémon League Champion! There won't be any letup from me!")
    if "Tobias" in tr.name:
        print(f"{tr.name}: I'm the Lily of the Valley Conference Champion. You probably heard of my Famous Darkrai and Latios. {srname}! But now I will show you my true strength. The strength of Legendary Pokémons.")
    if "Wallace" in tr.name:
        print(f"{tr.name}: You have overcome challenges and made it this far because you worked as one with your Pokémon. Show me that strength here and now!")
    if "Steven" in tr.name:
        print(f"{tr.name}: Welcome, {srname}. I was looking forward to seeing you here one day. You… What did you see on your journey with Pokémon? What did you feel, meeting so many other Trainers like you? What has awoken in you? I want you to hit me with it all! Now, bring it!")
    if "Agatha" in tr.name:
        print(f"{tr.name}: I am Agatha of the Elite Four.My poison type Pokémon traumatizes him as well.{srname}! I'll show you how a real Trainer battles!")
    if "Lorelei" in tr.name:
        print(f"{tr.name}: Well then, allow me to reintroduce myself. I am Lorelei of the Elite Four. No one can best me when it comes to icy Pokémon. Freezing moves are powerful. Your Pokémon will be at my mercy when they are frozen solid. That's because frozen Pokémon can't do a thing in battle! Hahaha! Are you ready?")
        
    if "Bruno" in tr.name:
        print(f"{tr.name}: I am Bruno of the Elite Four! Through rigorous training, people and Pokémon can become stronger without limit. I've lived and trained with my fighting Pokémon! And that will never change! {srname}! We will grind you down with our superior power! Hoo hah!")
    if "Lance" in tr.name:
        print(f"{tr.name}: I've been waiting for you. {srname}! I knew that you, with your skills, would eventually reach me here. There's no need for words now. We will battle to determine who is the stronger of the two of us. As the most powerful trainer and as the Pokémon League Champion… I, Lance the dragon master, accept your challenge!")            
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
             
def action(tr):
    
    while True:
        print("\nActions:\n1.Fight\n2.Switch\n3.Forfeit\n4.Pokemons\n")
        actionx= input(f"{tr.name}: What you wanna do?\n>>")
        if actionx in ["1","2","3"]:
            actionx=int(actionx)
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
            actionx=random.choices([1,2,3], weights=[99,10,0],k=1)[0]
            return actionx
            break
            
        
    
def battle(x,y,tr1,tr2):
    turn=0
    
    while True:
        turn+=1
        print("===================================================================================")
        print("TURN:",turn)
        print("===================================================================================")
        print("Weather:",field.weather)
        print(f"\n>>> {tr1.name} vs {tr2.name} <<<\n")
        print(f"\n>>> Lv.{x.level} {x.name} vs {y.name} Lv.{y.level} <<<\n")
        score(x,y,p1,p2)
        action1=action(tr1)
        action2=action(tr2)
        #print(action1,action2)
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
            choice1=x.moves[choice1-1]     
            choice2=y.moves[choice2-1]
#P1 PRIORITY            
            if choice1 in prioritymove and choice2 not in prioritymove or (choice1 in statusmove and x.ability=="Prankster") :
                weather(x,y)
                 
                x=attack(x,y,tr1,tr2,choice1,choice2)
                statchange(x)
                statchange(y)
                if x.hp<=0:
                    x=faint(x,tr1,y)
                    if len(tr1.pokemons)==0:
                        print(tr2.name,"wins.")
                        break
                elif y.hp>0:
                     
                    y=attack(y,x,tr2,tr1,choice2, choice1)
                    effects (x,y)
                    effects(y,x)
                    statchange(x)
                    statchange(y)
                    if x.hp<=0:
                        x=faint(x,tr1,y)
                        if len(tr1.pokemons)==0:
                            print(tr2.name,"wins.")
                            break
                    if y.hp<=0:
                        y=faint(y,tr2,x)
                        if len(tr2.pokemons)==0:
                            print(tr1.name,"wins.")
                            break
                if y.hp<=0:
                    y=faint(y,tr2,x)
                    effects(x,y)
                    if x.hp<=0:
                        x=faint(x,tr1,y)
                        if len(tr1.pokemons)==0:
                            print(tr2.name,"wins.")
                            break
                    if len(tr2.pokemons)==0:
                        print(tr1.name,"wins.")
                        break
#P2 PRIORITY 
            elif choice2 in prioritymove and choice1 not in prioritymove  or (choice2 in statusmove and y.ability=="Prankster"):
                weather(y,x)
                 
                y=attack(y,x,tr2,tr1,choice2, choice1)
                statchange(x)
                statchange(y)
                if y.hp<=0:
                    y=faint(y,tr2,x)
                    if len(tr2.pokemons)==0:
                        print(tr1.name,"wins.")
                        break
                elif x.hp>0:
                     
                    x=attack(x,y,tr1,tr2,choice1,choice2)
                    effects(y,x)
                    effects (x,y)
                    statchange(x)
                    statchange(y)
                    if y.hp<=0:
                        y=faint(y,tr2,x)
                        if len(tr2.pokemons)==0:
                            print(tr1.name,"wins.")
                            break
                    if x.hp<=0:
                        x=faint(x,tr1,y)
                        if len(tr1.pokemons)==0:
                            print(tr2.name,"wins.")
                            break
                if x.hp<=0:
                    x=faint(x,tr1,y)
                    effects(y,x)
                    if y.hp<=0:
                        y=faint(y,tr2,x)
                        if len(tr2.pokemons)==0:
                            print(tr1.name,"wins.")
                            break
                    if len(tr1.pokemons)==0:
                        print(tr2.name,"wins.")
                        break
#P1 FAST
            elif x.speed>=y.speed and field.trickroom==False:
                weather(x,y)
                 
                x=attack(x,y,tr1,tr2,choice1,choice2)
                statchange(x)
                statchange(y)
                if x.hp<=0:
                    x=faint(x,tr1,y)
                    if len(tr1.pokemons)==0:
                        print(tr2.name,"wins.")
                        break
                elif y.hp>0:
                     
                    
                    y=attack(y,x,tr2,tr1,choice2, choice1)
                    effects (x,y)
                    effects(y,x)
                    statchange(x)
                    statchange(y)
                    if x.hp<=0:
                        x=faint(x,tr1,y)
                        if len(tr1.pokemons)==0:
                            print(tr2.name,"wins.")
                            break
                    if y.hp<=0:
                        y=faint(y,tr2,x)
                        if len(tr2.pokemons)==0:
                            print(tr1.name,"wins.")
                            break
                if y.hp<=0:
                    y=faint(y,tr2,x)
                    effects(x,y)
                    if x.hp<=0:
                        x=faint(x,tr1,y)
                        if len(tr1.pokemons)==0:
                            print(tr2.name,"wins.")
                            break
                    if len(tr2.pokemons)==0:
                        print(tr1.name,"wins.")
                        break
#P2 FAST (TRICK ROOM)
            elif x.speed<y.speed and field.trickroom==True:
                weather(x,y)
                 
                x=attack(x,y,tr1,tr2,choice1,choice2)
                statchange(x)
                statchange(y)
                if x.hp<=0:
                    x=faint(x,tr1,y)
                    if len(tr1.pokemons)==0:
                        print(tr2.name,"wins.")
                        break
                elif y.hp>0:
                     
                    y=attack(y,x,tr2,tr1,choice2, choice1)
                    effects (x,y)
                    effects(y,x)
                    statchange(x)
                    statchange(y)
                    if x.hp<=0:
                        x=faint(x,tr1,y)
                        if len(tr1.pokemons)==0:
                            print(tr2.name,"wins.")
                            break
                    if y.hp<=0:
                        y=faint(y,tr2,x)
                        if len(tr2.pokemons)==0:
                            print(tr1.name,"wins.")
                            break
                if y.hp<=0:
                    y=faint(y,tr2,x)
                    effects(x,y)
                    if x.hp<=0:
                        x=faint(x,tr1,y)
                        if len(tr1.pokemons)==0:
                            print(tr2.name,"wins.")
                            break
                    if len(tr2.pokemons)==0:
                        print(tr1.name,"wins.")
                        break
#P2 FAST
            elif y.speed>x.speed and field.trickroom==False:
                weather(y,x)
                 
                y=attack(y,x,tr2,tr1,choice2, choice1)
                statchange(x)
                statchange(y)
                if y.hp<=0:
                    y=faint(y,tr2,x)
                    if len(tr2.pokemons)==0:
                        print(tr1.name,"wins.")
                        break
                elif x.hp>0:
                     
                    x=attack(x,y,tr1,tr2,choice1,choice2)
                    effects(y,x)
                    effects (x,y)
                    statchange(x)
                    statchange(y)
                    if y.hp<=0:
                        y=faint(y,tr2,x)
                        if len(tr2.pokemons)==0:
                            print(tr1.name,"wins.")
                            break
                    if x.hp<=0:
                        x=faint(x,tr1,y)
                        if len(tr1.pokemons)==0:
                            print(tr2.name,"wins.")
                            break
                if x.hp<=0:
                    x=faint(x,tr1,y)
                    effects(y,x)
                    if y.hp<=0:
                        y=faint(y,tr2,x)
                        if len(tr2.pokemons)==0:
                            print(tr1.name,"wins.")
                            break
                    if len(tr1.pokemons)==0:
                        print(tr2.name,"wins.")
                        break
#P2 FAST (TRICK ROOM)
            elif y.speed<=x.speed and field.trickroom==True:
                weather(y,x)
                 
                y=attack(y,x,tr2,tr1,choice2, choice1)
                statchange(x)
                statchange(y)
                if y.hp<=0:
                    y=faint(y,tr2,x)
                    if len(tr2.pokemons)==0:
                        print(tr1.name,"wins.")
                        break
                elif x.hp>0:
                     
                    x=attack(x,y,tr1,tr2,choice1,choice2)
                    effects(y,x)
                    effects (x,y)
                    statchange(x)
                    statchange(y)
                    if y.hp<=0:
                        y=faint(y,tr2,x)
                        if len(tr2.pokemons)==0:
                            print(tr1.name,"wins.")
                            break
                    if x.hp<=0:
                        x=faint(x,tr1,y)
                        if len(tr1.pokemons)==0:
                            print(tr2.name,"wins.")
                            break
                if x.hp<=0:
                    x=faint(x,tr1,y)
                    effects(y,x)
                    if y.hp<=0:
                        y=faint(y,tr2,x)
                        if len(tr2.pokemons)==0:
                            print(tr1.name,"wins.")
                            break
                    if len(tr1.pokemons)==0:
                        print(tr2.name,"wins.")
                        break
        elif action1==2 and action2==1:
            choice1=None
            score(x,y,p1,p2)
            choice2=fchoice(y,tr2)               
            choice2=y.moves[choice2-1]
            weather(y,x)
            x=switch(x,tr1,y)
            y=attack(y,x,tr2,tr1,choice2, choice1)
            effects(x,y)
            effects(y,x)
            statchange(x)
            statchange(y)
            if y.hp<=0:
                y=faint(y,tr2,x)
                if len(tr2.pokemons)==0:
                    print(tr1.name,"wins.")
                    break
            if x.hp<=0:
                x=faint(x,tr1,y)
                if len(tr1.pokemons)==0:
                    print(tr2.name,"wins.")
                    break
        elif action1==1 and action2==2:
            choice2=None
            score(x,y,p1,p2)
            choice1=fchoice(x,tr1)
            choice1=x.moves[choice1-1]     
            weather(y,x)
            y=switch(y,tr2,x)
            x=attack(x,y,tr1,tr2,choice1,choice2)
            if x.hp<=0:
                x=faint(x,tr1,y)
                if len(tr1.pokemons)==0:
                    print(tr2.name,"wins.")
                    break
            effects(y,x)
            effects(x,y)
            statchange(x)
            statchange(y)
            if x.hp<=0:
                x=faint(x,tr1,y)
                if len(tr1.pokemons)==0:
                    print(tr2.name,"wins.")
                    break
            if y.hp<=0:
                y=faint(y,tr2,x)
                if len(tr2.pokemons)==0:
                    print(tr1.name,"wins.")
                    break
        elif action1==2 and action2==2:
            y=switch(y,tr2,x) 
            x=switch(x,tr1,y)       
            effects(y,x)
            if y.hp<=0:
                y=faint(y,tr2,x)
                if len(tr2.pokemons)==0:
                    print(tr1.name,"wins.")
                    break
            effects(x,y)              
            if x.hp<=0:
                x=faint(x,tr1,y)
                if len(tr1.pokemons)==0:
                    print(tr2.name,"wins.")
                    break   
