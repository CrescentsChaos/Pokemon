#pylint:disable=C0303
from attack import *
from moves import *
from trainerlist import *
def score(x,y,p1,p2):
    print("")
    if x==None:
        x=p1.pokemons[0]
    if y==None:
        y=p2.pokemons[0]
        pass
    print(f"{p1.name}:")
    print(f"Lv.{x.level} {x.name}: {x.hp}/{x.maxhp}({round((x.hp/x.maxhp)*100,2)}%)[{x.status}]")
    #print(f"ATK: {round(x.atk,2)} DEF: {round(x.defense,2)} SPATK: {round(x.spatk,2)} SPDEF: {round(x.spdef,2)} SPD: {round(x.speed,2)}")
    print(f"ATK: {round(x.atkb,2)} DEF: {round(x.defb,2)} SPATK: {round(x.spatkb,2)} SPDEF: {round(x.spdefb,2)} SPD: {round(x.speedb,2)}")
    print("")
    print(f"{p2.name}:")
    print(f"Lv.{y.level} {y.name}: {y.hp}/{y.maxhp}({round((y.hp/y.maxhp)*100,2)}%)[{y.status}]")
    print(f"ATK: {round(y.atkb,2)} DEF: {round(y.defb,2)} SPATK: {round(y.spatkb,2)} SPDEF: {round(y.spdefb,2)} SPD: {round(y.speedb,2)}\n")
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
def intro (tr,sr):
    srname=sr.name.split(" ")[-1]
    if "Red" in tr.name:
        print(f"{tr.name}: ........")
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
            
            
def battle(x,y,tr1,tr2):
    turn=0
    alpha1=0
    alpha2=0
    mega1=0
    mega2=0
    print(f"\n>>> {tr1.name} vs {tr2.name} <<<\n")
    intro (tr1,tr2)
    print("")
    intro (tr2,tr1)
    if x.speed>= y.speed:
        weatherset(x)
        weatherset(y)
    elif y.speed>x.speed:
        weatherset(y)
        weatherset(x)
    print("")
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
                print(f"{nm} reacted to {tr1.name}'s keystone and turned into {i.name}.\n")
            else:
                if "X" in i.name:
                    nm="Charizard"
                    print(f"{nm} reacted to {tr1.name}'s keystone  and turned into {i.name}.\n")
                else:
                    nm="Charizard"
                    print(f"{nm} reacted to {tr1.name}'s keystone  and turned into {i.name}.\n")
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
                print(f"{nm} reacted to {tr2.name}'s keystone  and turned into {i.name}.\n")
            else:
                if "X" in i.name:
                    nm="Charizard"
                    print(f"{nm} reacted to {tr2.name}'s keystone  and turned into {i.name}.\n")
                else:
                    nm="Charizard"
                    print(f"{nm} reacted to {tr2.name}'s keystone  and turned into {i.name}.\n")
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
    while len(p1.pokemons)!=0 or len(p2.pokemons)!=0:
        turn+=1
        
        if len(tr1.pokemons)-len(tr2.pokemons)>3 and len(tr1.pokemons)>len(tr2.pokemons) and "Red" not in tr2.name:
            print(f"{tr2.name}: I Underestimated you!")
        if len(tr2.pokemons)-len(tr1.pokemons)>3 and len(tr2.pokemons)>len(tr1.pokemons) and "Red" not in tr1.name:
            print(f"{tr1.name}: You are really strong!")
        if x is None:
            x=switch(x,tr1,y)
        if y is None:
            y=switch(y,tr2,x)
        print("\nTURN:",turn)
        print("Weather:",Pokemon.weather)
        print(f"\n>>> {tr1.name} vs {tr2.name} <<<\n")
        print(f"\n>>> Lv.{x.level} {x.name} vs {y.name} Lv.{y.level} <<<\n")
        decision1=random.choices(["Switch","Attack"], weights=[1,10],k=1)[0]
        decision2=random.choices(["Switch","Attack"], weights=[1,10],k=1)[0]
        if len(tr1.pokemons)==1:
            decision1="Attack"
        if len(tr2.pokemons)==1:
            decision2="Attack"
        if x.speed>=y.speed and decision1=="Attack" and decision2=="Attack":
            weather(x,y)
            score(x,y,p1,p2)
            x=attack(x,y,tr1,tr2)
            statchange(x)
            statchange(y)
            if y.hp>0:
                score(x,y,p1,p2)
                y=attack(y,x,tr2,tr1)
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
                if len(tr2.pokemons)==0:
                    print(tr1.name,"wins.")
                    break
            if x!=None and x.hp<=0:
                x=faint(x,tr1,y)
                if len(tr1.pokemons)==0:
                    print(tr2.name,"wins.")
                    break
        elif y.speed>x.speed and decision1=="Attack" and decision2=="Attack":
            weather(y,x)
            score(x,y,p1,p2)
            y=attack(y,x,tr2,tr1)
            statchange(x)
            statchange(y)
            if x.hp>0:
                score(x,y,p1,p2)
                x=attack(x,y,tr1,tr2)
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
            #print("Problem")
            if x!=None and x.hp<=0:
                x=faint(x,tr1,y)
                if len(tr1.pokemons)==0:
                    print(tr2.name,"wins.")
                    break
            #print("Problem")
            if y!=None and y.hp<=0:
                y=faint(y,tr2,x)
                if len(tr2.pokemons)==0:
                    print(tr1.name,"wins.")
                    break
        elif decision1=="Switch" and decision2=="Attack":
            weather(y,x)
            x=switch(x,tr1,y)
            score(x,y,p1,p2)
            y=attack(y,x,tr2,tr1)
            statchange(x)
            statchange(y)
            if x.hp<=0:
                x=faint(x,tr1,y)
                if len(tr1.pokemons)==0:
                    print(tr2.name,"wins.")
                    break
        elif decision1=="Attack" and decision2=="Switch":
            weather(y,x)
            y=switch(y,tr2,x)
            score(x,y,p1,p2)
            x=attack(x,y,tr1,tr2)
            statchange(x)
            statchange(y)
            if y.hp<=0:
                y=faint(y,tr2,x)
                if len(tr2.pokemons)==0:
                    print(tr1.name,"wins.")
                    break
        elif decision1=="Switch" and decision2=="Switch":
            weather(x,y)
            if x.speed>=y.speed:
                x=switch(x,tr1,y)
                y=switch(y,tr2,x)     
            if x.speed<y.speed:
                y=switch(y,tr2,x) 
                x=switch(x,tr1,y)                        
            
        elif len(tr1.pokemons)==0:
            print(tr2.name,"wins.")
            break
        elif len(tr2.pokemons)==0:
            print(tr1.name,"wins.")
            break
        else:
            break
