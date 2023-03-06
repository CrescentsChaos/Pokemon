from attack import *
from moves import *
from intros import intro
from outros import outro
from moreoptions import *
from movelist import *

#SCOREBOARD
def  score(x,y,p1,p2,turn):
    print("")
    if x==None:
        x=p1.pokemons[0]
    if y==None:
        y=p2.pokemons[0]
        pass
    print(f" {p1.name}:")
    if len(p1.hazard)!=0:
        print(" Hazard:",p1.hazard)
    if p1.tailwind==True:
        print(f" 🍃 Tailwind({p1.twendturn-turn} turns left)")                   
    if p1.reflect==True:
        print(f" 🟦 Reflect({p1.rfendturn-turn} turns left)")   
    if p1.auroraveil==True:
        print(f" ⬜ Aurora Veil({p1.avendturn-turn} turns left)")
    if p1.lightscreen==True:              
        print(f" 🟪 Light Screen({p1.screenend-turn} turns left)")        
    print(f" Lv.{x.level} {x.name}: {round(x.hp)}/{x.maxhp}({round((x.hp/x.maxhp)*100,3)}%)[{x.status}]")
    if x.teratype is not None and x.type2 is None and p2.ai is True:
        print(f" Type:{x.teratype} Ability: {x.ability} Item: {x.item} Nature: {x.nature}")
    if x.teratype is not None and x.type2 is not None and p2.ai is True:
        print(f" Type:{x.teratype} Ability: {x.ability} Item: {x.item} Nature: {x.nature}")
    if x.teratype is None and x.type2 is None and p2.ai is True:
        print(f" Type:{x.type1} Ability: {x.ability} Item: {x.item} Nature: {x.nature}")
    if x.teratype is None and x.type2 is not None and p2.ai is True:
        print(f" Type:{x.type1}/{x.type2} Ability: {x.ability} Item: {x.item} Nature: {x.nature}" )
    if p2.ai is True:        
        print(f" Atk: {round(x.atk)}({round(x.atkb,3)}) Def: {round(x.defense)}({round(x.defb,3)}) SpA: {round(x.spatk)}({round(x.spatkb,3)}) SpD: {round(x.spdef)}({round(x.spdefb,3)}) Spe: {round(x.speed)}({round(x.speedb,3)})")
    print("")
    print(f" {p2.name}:")
    if len(p2.hazard)!=0:
        print(" Hazard:",p2.hazard)
    if p2.tailwind==True:
        print(f" 🍃 Tailwind({p2.twendturn-turn} turns left)")                
    if p2.reflect==True:
        print(f" 🟦 Reflect({p2.rfendturn-turn} turns left)")     
    if p2.auroraveil==True:
        print(f" ⬜ Aurora Veil({p2.avendturn-turn} turns left)")
    if p2.lightscreen==True:        
        print(f" 🟪 Light Screen({p2.screenend-turn} turns left)")               
    print(f" Lv.{y.level} {y.name}: {round(y.hp)}/{y.maxhp}({round((y.hp/y.maxhp)*100,3)}%)[{y.status}]")
    if y.teratype is not None and y.type2 is None and p1.ai is True:
        print(f" Type:{y.teratype} Ability: {y.ability} Item: {y.item} Nature: {y.nature}")
    if y.teratype is not None and y.type2 is not None and p1.ai is True:
        print(f" Type:{y.teratype} Ability: {y.ability} Item: {y.item} Nature: {y.nature}")
    if y.teratype is None and y.type2 is None and p1.ai is True:
        print(f" Type:{y.type1} Ability: {y.ability} Item: {y.item} Nature: {y.nature}")
    if y.teratype is None and y.type2 is not None and p1.ai is True:
        print(f" Type:{y.type1}/{y.type2} Ability: {y.ability} Item: {y.item} Nature: {y.nature}")
    if p1.ai is True:
        print(f" Atk: {round(y.atk)}({round(y.atkb,3)}) Def: {round(y.defense)}({round(y.defb,3)}) SpA: {round(y.spatk)}({round(y.spatkb,3)}) SpD: {round(y.spdef)}({round(y.spdefb,3)}) Spe: {round(y.speed)}({round(y.speedb,3)})\n")
    if field.weather=="Primordial Sea" and "Primordial Sea" not in (x.ability,y.ability) and "Marine" not in field.location:
        field.weather="Clear"
        print (" 🌤️ The heavy rainfall stopped.\n")
    if field.weather=="Desolate Land" and "Desolate Land" not in (x.ability,y.ability) and "Terra" not in field.location and "Blaine(Hardcore Mode)" not in (x.owner.name,y.owner.name):
        field.weather="Clear"
        print (" 🌤️ The extreme sunlight fade away.\n")     
#FAINTED        
def faint(mon,mon2,trainer,trainer2,field,turn):
    if mon.hp<=0:
        mon.hp=0
        mon.status="Fainted"
        name=mon.name
        if mon.dmax is True:
            mon.dmax=False
            nn=-1
            prdx=["Great Tusk","Sandy Shocks","Roaring Moon","Brute Bonnet","Slither Wing","Flutter Mane","Scream Tail","Iron"]
            for i in prdx:
                if i in mon.name:
                    nn=-2
            if nn==-1:
                name=mon.name.split(" ")[-1]
            if nn==-2:
                name=name[8:]
            print(f" 🔻 {name} returned to it's normal state!")
            mon.name=name
        if "Mega " in mon.name:
            name=mon.name.split(" ")[-1]
            if "Mewtwo" in mon.name:
                name="Mewtwo"
            if "Charizard" in mon.name:
                name="Charizard"
            print(f" 🧬 {name} returned to it's normal state!")
            mon.name=name
        if mon.owner==trainer.name:
            trainer.faintedmon.append(mon)
        print(f" \n 🏁 Refree: {mon.name} is unable to battle!")
        print(f"  😵😵‍💫 {trainer.name}'s {mon.name} fainted!\n")
        if mon2.ability=="Battle Bond" and "Ash" not in mon2.name and mon2.dmax==False:
            print(f" {mon2.name}'s {mon2.ability}.")
            if "Ash" not in mon2.name and "Greninja" in mon2.name:
                mon2.name="Ash Greninja"
                print(f" {mon2.name} synced with its trainer's bond and transformed!")
                per=mon2.hp/mon2.maxhp
                mon2.hp=72
                mon2.atk=145
                mon2.defense=67
                mon2.spatk=153
                mon2.spdef=71
                mon2.speed=132
                mon2.calcst()
                mon2.hp=mon2.maxhp*per
            if "Greninja" not in mon2.name:
                atkchange(mon2,mon,0.5)
                spatkchange(mon2,mon,0.5)
                speedchange(mon2,mon,0.5)
        if mon2.ability=="Beast Boost":
            print(f" 👾 {mon2.name}'s {mon2.ability}!")
            m=[a,b,c,d,e]=[mon2.atk,mon2.defense,mon2.spatk,mon2.spdef,mon2.speed]
            if trainer2.reflect==True:
                m=[mon2.atk,mon2.defense/2,mon2.spatk,mon2.spdef,mon2.speed]
            if trainer2.lightscreen==True:
                m=[mon2.atk,mon2.defense,mon2.spatk,mon2.spdef/2,mon2.speed]
            x=max(m)
            if x==a:
            	atkchange(mon2,mon,0.5)
            	print(f" {mon2.name}'s attack rose!")
            elif x==b:
            	defchange(mon2,mon,0.5)
            	print(f" {mon2.name}'s defense rose!")
            elif x==c:
        	    spatkchange(mon2,mon,0.5)
        	    print(f" {mon2.name}'s special attack rose!")
            elif x==d:
        	    spdefchange(mon2,mon,0.5)
        	    print(f" {mon2.name}'s special defense rose!")
            elif x==e:
            	speedchange(mon2,mon,0.5)
            	print(f" {mon2.name}'s speed rose!")
        if mon2.ability=="Soul-Heart":
            print(f" 💗 {mon2.name}'s {mon2.ability}!")
            spatkchange(mon2,mon,0.5)
            print(f" {mon2.name}'s special attack rose!")
        if mon.ability =="Aftermath":
            print(f" 🕜 {mon.name}'s {mon.ability}.")
            mon2.hp-=mon2.maxhp/4
        if mon2.ability=="Moxie":
            print(f" ⏫ {mon2.name}'s {mon2.ability}!")
            atkchange(mon2,mon,0.5)
            print(f" {mon2.name}'s attack rose!")
        if mon2.ability=="As One" and "Ice Rider" in mon2.name:
            print(f" 🏇 {mon2.name}'s {mon2.ability}.")
            print(f" {mon2.name}'s attack rose!")
            atkchange(mon2,mon,0.5)       
        if mon2.ability=="As One" and "Shadow Rider" in mon2.name:
            print(f" 🏇 {mon2.name}'s {mon2.ability}.")
            print(f" {mon2.name}'s special attack rose!")
            spatkchange(mon2,mon,0.5)        
        if mon2.ability=="Chilling Neigh" :
            print(f" 🥶 {mon2.name}'s {mon2.ability}.")
            print(f" {mon2.name}'s attack rose!")
            atkchange(mon2,mon,0.5)    
        if mon2.ability=="Grim Neigh" :
            print(f" 😱 {mon2.name}'s {mon2.ability}.")
            print(f" {mon2.name}'s special attack rose!")
            spatkchange(mon2,mon,0.5)                
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
def action(tr,self,other):
    if tr.ai is False:
        while True:
            if tr.canmax is True and (self.item!=None and self.item not in megastones) and "Z-Crystal" not in self.name and self.teratype==None and ("Zacian" not in self.name and "Zamazenta" not in self.name and "Eternatus" not in self.name and "Z-Crystal" not in self.name and "Rayquaza" not in self.name and "Primal" not in self.name and "Mega" not in self.name) and tr.cantera==False:
                print("\n Actions:\n 1. 💥 Fight\n 2. 🔁 Switch\n 3. ❌ Forfeit\n 4. ℹ️ Pokemons\n 5. 🌐 Smogonify\n 8. ⭕ Dynamax/Gigantamax\n")
            elif tr.cantera is True and ((self.item!=None and self.item not in megastones) and "Z-Crystal" not in self.name):
                if tr.canmax is True and (self.item!=None and self.item not in megastones) and "Z-Crystal" not in self.name and self.teratype==None and ("Zacian" not in self.name and "Zamazenta" not in self.name and "Eternatus" not in self.name and "Z-Crystal" not in self.name and "Rayquaza" not in self.name and "Primal" not in self.name and "Mega" not in self.name):
                    print(f"\n Actions:\n 1. 💥 Fight\n 2. 🔁 Switch\n 3. ❌ Forfeit\n 4. ℹ️ Pokemons\n 5. 🌐 Smogonify\n 7. 💎 Terastallize({self.tera})\n 8. ⭕ Dynamax/Gigantamax\n")
                else:
                    print(f"\n Actions:\n 1. 💥 Fight\n 2. 🔁 Switch\n 3. ❌ Forfeit\n 4. ℹ️ Pokemons\n 5. 🌐 Smogonify\n 7. 💎 Terastallize({self.tera})\n")
            elif tr.canmega is True and self.item!=None and (self.item in megastones or "Dragon Ascent" in self.moves):
                print("\n Actions:\n 1. 💥 Fight\n 2. 🔁 Switch\n 3. ❌ Forfeit\n 4. ℹ️ Pokemons\n 5. 🌐 Smogonify\n 9. 🧬 Mega Evolve\n")
            elif self.item!=None and "Ultranecrozium Z" in self.item and "Ultra" not in self.name:
                print("\n Actions:\n 1. 💥 Fight\n 2. 🔁 Switch\n 3. ❌ Forfeit\n 4. ℹ️ Pokemons\n 5. 🌐 Smogonify\n 10. ✴️ Ultra Burst\n")
            else:
                print("\n Actions:\n 1. 💥 Fight\n 2. 🔁 Switch\n 3. ❌ Forfeit\n 4. ℹ️ Pokemons\n 5. 🌐 Smogonify\n")
            actionx= input(f"{tr.name}: What you wanna do?\n>>")
            if actionx in ["1","2","3","10","9","8","7"]:
                actionx=int(actionx)
            if actionx=="5":
                print(showsmogon(tr))
                action(tr,self,other)
            if actionx=="4":
                showmon(tr)
                n=(input("Which pokemon you wanna see?\n>>"))
                if n in ["1","2","3","4","5","6","10","9","8","7"]:
                    n=int(n)
                    tr.pokemons[n-1].info()
                    movelist(tr.pokemons[n-1])
            if actionx in [1,2,3,9,10,8,7]:
                if actionx==2:
                    if other.ability=="Magnet Pull" and (self.ability!="Levitate" or "Steel" in (self.type1,self.type2,self.teratype)):
                        print(f" 🧲 {other.name}'s Magnet Pull!")
                        actionx=1
                    if other.ability=="Shadow Tag" and (self.ability!="Levitate" or "Ghost" not in (self.type1,self.type2,self.teratype)):
                        print(f" 🔖 {other.name}'s Shadow Tag!")
                        actionx=1
                    if other.ability=="Arena Trap" and (self.ability!="Levitate" or "Flying" not in (self.type1,self.type2,self.teratype)):
                        print(f" 🏜️ {other.name}'s Arena Trap!")
                        actionx=1
                return actionx    
                break    
            if actionx=="":
                if tr.ai is not None:
                    rn=[1,2,3]
                    actionx=1#
#                    if (self.item in megastones or "Dragon Ascent" in self.moves) and "Mega" not in self.name and tr.canmega==True:
#                        actionx=9
#                    if  self.item!=None and "Ultranecrozium Z" in self.item:
#                        actionx=10
#                    if  tr.canmax==True and self.item not in megastones and "Z-Crystal" not in self.name:
#                        actionx=8
#                    else:
#                        actionx=random.choices(rn, weights=[99,5,1],k=1)[0]
                return actionx
                break
    if tr.ai is True:
            return 1        

#SKIP
def skip(x,y,tr1,tr2):
    skip=False
    while skip!=True:
        kk=input("\n Do you want to skip this turn? (Enter anything)\n >>> ")
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
#BATTLE
def battle(x,y,tr1,tr2):
    turn=0
    print("===================================================================================")
    #field.weather,field.terrain=randomweather(turn,x,y,field)
    intro(tr1,tr2,field)
    intro(tr2,tr1,field)
    print(f" {p2.name} was challenged by {p1.name}!")
    print(f" Battle between {p1.name} and {p2.name} begun!")
    if x.speed>=y.speed:
        entryeff(x,y,tr1,tr2,field,turn)
        entryeff(y,x,tr2,tr1,field,turn)
        
    if y.speed>x.speed:
        entryeff(y,x,tr2,tr1,field,turn)
        entryeff(x,y,tr1,tr2,field,turn)
    while True:
        if tr1==tr2:
            print(" Game Over.")
            break
        turn+=1
        print("===================================================================================")
        print(" TURN:",turn)
        print("===================================================================================")
        print(f" Location: {field.location}")
        if field.weather=="Strong Winds":
            print(f" Weather: 🍃 Strong Winds") 
        if field.weather=="Desolate Land":
            print(f" Weather: 🌋 Extremely Harsh Sunlight")
        if field.weather=="Primordial Sea":
            print(f" Weather: 🌊 Heavy Rain")
        if field.weather=="Rainy" and field.terrain=="Grassy":
            print(f" Weather: 🐸 Swampy ({field.rainendturn-turn} turns left)")
        if field.weather=="Rainy" and field.terrain=="Electric":
            print(f" Weather: ⛈️ Thunderstorm ({field.rainendturn-turn} turns left)")
        if field.weather=="Strong Winds" and field.terrain=="Electric":
            print(f" Weather: 🌪️ Hurricane")
        if field.weather in ["Hail","Snowstorm"]:
            if field.weather=="Snowstorm":
                print(f" Weather: ❄️ {field.weather} ({field.snowstormendturn-turn} turns left)")
            if field.weather=="Hail":
                print(f" Weather: ❄️ {field.weather} ({field.hailendturn-turn} turns left)")
        if field.weather in ["Clear"]:
            print(f" Weather: 🌥️ {field.weather}")
        if field.weather=="Cloudy":
            print(f" Weather: ☁️ {field.weather}")       
        if field.weather=="Rainy" and field.terrain not in ["Electric","Grassy"]:
            print(f" Weather: ☔ {field.weather} ({field.rainendturn-turn} turns left)")
        if field.weather=="Sunny":
            print(f" Weather: ☀️ {field.weather} ({field.sunendturn-turn} turns left)")
        if field.weather=="Sandstorm":
            print(f" Weather: 🏜️ {field.weather} ({field.sandendturn-turn} turns left)")    
        if field.terrain=="Misty":      
            print(f" Terrain: 🌸 {field.terrain} ({field.misendturn-turn} turns left)")
        if field.terrain=="Psychic":      
            print(f" Terrain: 👁️ {field.terrain} ({field.psyendturn-turn} turns left)")
        if field.terrain in ["Normal"]:      
            print(" Terrain: 🌐 "+field.terrain)
        if field.terrain=="Electric":      
            print(f" Terrain: ⚡ {field.terrain} ({field.eleendturn-turn} turns left)")
        if field.terrain=="Grassy":      
            print(f" Terrain: 🌿 {field.terrain} ({field.grassendturn-turn} turns left)")
        if field.trickroom is True:
            print(f" Dimension: 🌀 Trick Room ({field.troomendturn-turn} turns left)")           
        print(f" \n ⏩⏩ {tr1.name} ({len(tr1.pokemons)}) 🆚 ({len(tr2.pokemons)}) {tr2.name} ⏪⏪\n")
        print(f" \n ⏩⏩ Lv.{x.level} {x.name} 🆚 {y.name} Lv.{y.level} ⏪⏪\n")
        prebuff(x,y,tr1,turn,field)
        prebuff(y,x,tr2,turn,field)
        switchAI(x,y,tr1,tr2, field)
        switchAI(y,x,tr2,tr1,field)
        #score(x,y,p1,p2,turn)
        action1=action(tr1,x,y)
        action2=action(tr2,y,x)
        check=len(moveAI(y,x,tr2,tr1,field)[1])
        check2=len(moveAI(x,y,tr1,tr2,field)[1])
        if p1.ai is True:
            action1=decision(x,y,tr1,tr2,field)
        if p2.ai is True:
            action2=decision(y,x,tr2,tr1,field)
        #print(action1,action2)
        if  action1==3 and action2!=3:
            print(f" {tr1.name} forfeited.")
            break
        if  action2==3 and action1!=3:
            print(f" {tr2.name} forfeited.")
            break
        if action1 in [8,9,10,7]:
            if action1==7 and x.dmax==False and (x.item==None or x.item not in megastones) and "Z-Crystal" not in x.name and tr1.cantera==True:
                x.name+="💎"
                transformation(x,y,turn)
            if action1==8 and x.item!=None  and x.teratype==None and tr1.canmax==True and ("Zacian" not in x.name and "Zamazenta" not in x.name and "Eternatus" not in x.name and "Z-Crystal" not in x.name and "Rayquaza" not in x.name and "Primal" not in x.name and "Mega" not in x.name) and x.teratype==None:
                x.dmax=True
                tr1.canmax=False
                transformation(x,y,turn)
            if action1==9 and tr1.canmega is True and (((x.item!=None and x.item in megastones) or ("Dragon Ascent" in x.moves)) and x.dmax==False):
                transformation(x,y,turn)
            if action1==10:
                transformation(x,y,turn)
            action1=1
        if action2 in [8,9,10,7]:
            if action2==7 and y.dmax==False and (y.item==None or y.item not in megastones) and "Z-Crystal" not in y.name and tr2.cantera==True:
                y.name+="💎"
                transformation(y,x,turn)
            if action2==8 and y.item!=None and y.teratype==None and tr2.canmax==True  and ("Zacian" not in y.name and "Zamazenta" not in y.name and "Eternatus" not in y.name and "Z-Crystal" not in y.name and "Rayquaza" not in y.name and "Primal" not in y.name and "Mega" not in y.name) and y.teratype==None:
                y.dmax=True
                tr2.canmax=False
                transformation(y,x,turn)
            if action2==9 and tr2.canmega is True and ((y.item!=None and y.item in megastones) or ("Dragon Ascent" in y.moves)):
                transformation(y,x,turn)
            if action2==10:
                transformation(y,x,turn)
            action2=1
        if action1==2 and len(tr1.pokemons)==1:
            action1=1
        if action2==2 and len(tr2.pokemons)==1:
            action2=1
#IF BOTH CHOOSES TO ATTACK
        if action1==1 and action2==1:
            score(x,y,p1,p2,turn)
            choice1=fchoice(x,tr1)
            choice2=fchoice(y,tr2)    
            if p1.ai==True or choice1=="":              
                choice1=moveAI(x,y,tr1,tr2,field)[0]
            if p1.ai==False:     
                if x.dmax is True:
                    choice1=x.maxmove[choice1-1]
                if x.dmax is False:
                    choice1=x.moves[choice1-1]
            if p2.ai==True or choice2=="":  
                choice2=moveAI(y,x,tr2,tr1,field)[0]     
            if p2.ai==False:   
                if y.dmax is False:
                    choice2=y.moves[choice2-1]     
                if y.dmax is True:
                    choice2=y.maxmove[choice2-1]
            xpr=0
            ypr=0
            if x.item=="Quick Claw":
                xpr=random.randint(1,100)
            if y.item=="Quick Claw":
                ypr=random.randint(1,100)
#P1 PRIORITY            
            if (choice1 in typemoves.prioritymove and choice2 not in typemoves.prioritymove) or x.priority is True or (x.ability=="Prankster" and choice1 in typemoves.statusmove and "Dark" not in (y.type1,y.type2)) or (choice1 in typemoves.firemoves and x.ability=="Blazing Soul" and x.hp==x.maxhp) or (choice1 in typemoves.flyingmoves and x.ability=="Gale Wings" and x.hp==x.maxhp) or (field.terrain=="Grassy" and choice1=="Grassy Glide") or (x.ability=="Triage" and choice1 in typemoves.healingmoves) or (choice2 in typemoves.negprioritymove) or (xpr>72) or (choice2 in typemoves.statusmove and y.ability=="Mycelium Might"):
                weather(x,y)
                x,y=attack(x,y,tr1,tr2,choice1,choice2,field,turn)
                prebuff(x,y,tr1,turn,field)
                prebuff(y,x,tr2,turn,field)
                if x.hp<=0:
                    x=faint(x,y,tr1,tr2,field,turn)
                    if len(tr1.pokemons)==0:
                        print(" 🏆 "+tr2.name,"wins.")
                        outro(tr2,tr1,y,field)
                        break
                elif y.hp>0:
                     
                    y,x=attack(y,x,tr2,tr1,choice2, choice1,field,turn)
                    effects (x,y,tr1,turn)
                    effects(y,x,tr2,turn)
                    prebuff(x,y,tr1,turn,field)
                    prebuff(y,x,tr2,turn,field)
                    if x.hp<=0:
                        x=faint(x,y,tr1,tr2,field,turn)
                        if len(tr1.pokemons)==0:
                            print(" 🏆 "+tr2.name,"wins.")
                            outro(tr2,tr1,y,field)
                            break
                    if y.hp<=0:
                        y=faint(y,x,tr2,tr1,field,turn)
                        if len(tr2.pokemons)==0:
                            print(" 🏆 "+tr1.name,"wins.")
                            outro(tr1,tr2,x,field)
                            break
                if y.hp<=0:
                    y=faint(y,x,tr2,tr1,field,turn)
                    effects(x,y,tr1,turn)
                    if x.hp<=0:
                        x=faint(x,y,tr1,tr2,field,turn)
                        if len(tr1.pokemons)==0:
                            print(" 🏆 "+tr2.name,"wins.")
                            outro(tr2,tr1,y,field)
                            break
                    if len(tr2.pokemons)==0:
                        print(" 🏆 "+tr1.name,"wins.")
                        outro(tr1,tr2,x,field)
                        break
                x.priority=False
                skip(x,y,tr1,tr2)
#P2 PRIORITY 
            elif (choice2 in typemoves.prioritymove and choice1 not in typemoves.prioritymove) or y.priority is True or (y.ability=="Prankster" and choice2 in typemoves.statusmove and "Dark" not in (x.type1,x.type2)) or (choice2 in typemoves.firemoves and y.ability=="Blazing Soul" and y.hp==y.maxhp) or (choice2 in typemoves.flyingmoves and y.ability=="Gale Wings" and y.hp==y.maxhp) or (field.terrain=="Grassy" and choice2=="Grassy Glide") or (y.ability=="Triage" and choice2 in typemoves.healingmoves) or (choice1 in typemoves.negprioritymove) or (xpr>72) or (choice1 in typemoves.statusmove and x.ability=="Mycelium Might"):
                weather(y,x)
                 
                y,x=attack(y,x,tr2,tr1,choice2, choice1,field,turn)
                prebuff(x,y,tr1,turn,field)
                prebuff(y,x,tr2,turn,field)
                if y.hp<=0:
                    y=faint(y,x,tr2,tr1,field,turn)
                    if len(tr2.pokemons)==0:
                        print(" 🏆 "+tr1.name,"wins.")
                        outro(tr1,tr2,x,field)
                        break
                elif x.hp>0:
                     
                    x,y=attack(x,y,tr1,tr2,choice1,choice2,field,turn)
                    effects(y,x,tr2,turn)
                    effects (x,y,tr1,turn)
                    prebuff(x,y,tr1,turn,field)
                    prebuff(y,x,tr2,turn,field)
                    if y.hp<=0:
                        y=faint(y,x,tr2,tr1,field,turn)
                        if len(tr2.pokemons)==0:
                            print(" 🏆 "+tr1.name,"wins.")
                            outro(tr1,tr2,x,field)
                            break
                    if x.hp<=0:
                        x=faint(x,y,tr1,tr2,field,turn)
                        if len(tr1.pokemons)==0:
                            print(" 🏆 "+tr2.name,"wins.")
                            outro(tr2,tr1,y,field)
                            break
                if x.hp<=0:
                    x=faint(x,y,tr1,tr2,field,turn)
                    effects(y,x,tr2,turn)
                    if y.hp<=0:
                        y=faint(y,x,tr2,tr1,field,turn)
                        if len(tr2.pokemons)==0:
                            print(" 🏆 "+tr1.name,"wins.")
                            outro(tr1,tr2,x,field)
                            break
                    if len(tr1.pokemons)==0:
                        print(" 🏆 "+tr2.name,"wins.")
                        outro(tr2,tr1,y,field)
                        break
                y.priority=False
                skip(x,y,tr1,tr2)
#P1 FAST
            elif x.speed>=y.speed and field.trickroom==False:
                weather(x,y)
                 
                x,y=attack(x,y,tr1,tr2,choice1,choice2,field,turn)
                prebuff(x,y,tr1,turn,field)
                prebuff(y,x,tr2,turn,field)
                if x.hp<=0:
                    x=faint(x,y,tr1,tr2,field,turn)
                    if len(tr1.pokemons)==0:
                        print(" 🏆 "+tr2.name,"wins.")
                        outro(tr2,tr1,y,field)
                        break
                elif y.hp>0:
                     
                    
                    y,x=attack(y,x,tr2,tr1,choice2, choice1,field,turn)
                    effects (x,y,tr1,turn)
                    effects(y,x,tr2,turn)
                    prebuff(x,y,tr1,turn,field)
                    prebuff(y,x,tr2,turn,field)
                    if x.hp<=0:
                        x=faint(x,y,tr1,tr2,field,turn)
                        if len(tr1.pokemons)==0:
                            print(" 🏆 "+tr2.name,"wins.")
                            outro(tr2,tr1,y,field)
                            break
                    if y.hp<=0:
                        y=faint(y,x,tr2,tr1,field,turn)
                        if len(tr2.pokemons)==0:
                            print(" 🏆 "+tr1.name,"wins.")
                            outro(tr1,tr2,x,field)
                            break
                if y.hp<=0:
                    y=faint(y,x,tr2,tr1,field,turn)
                    effects(x,y,tr1,turn)
                    if x.hp<=0:
                        x=faint(x,y,tr1,tr2,field,turn)
                        if len(tr1.pokemons)==0:
                            print(" 🏆 "+tr2.name,"wins.")
                            outro(tr2,tr1,y,field)
                            break
                    if len(tr2.pokemons)==0:
                        print(" 🏆 "+tr1.name,"wins.")
                        outro(tr1,tr2,x,field)
                        break
                skip(x,y,tr1,tr2)
#P2 FAST (TRICK ROOM)
            elif x.speed<y.speed and field.trickroom==True:
                weather(x,y)
                 
                x,y=attack(x,y,tr1,tr2,choice1,choice2,field,turn)
                prebuff(x,y,tr1,turn,field)
                prebuff(y,x,tr2,turn,field)
                if x.hp<=0:
                    x=faint(x,y,tr1,tr2,field,turn)
                    if len(tr1.pokemons)==0:
                        print(" 🏆 "+tr2.name,"wins.")
                        outro(tr2,tr1,y,field)
                        break
                elif y.hp>0:
                     
                    y,x=attack(y,x,tr2,tr1,choice2, choice1,field,turn)
                    effects (x,y,tr1,turn)
                    effects(y,x,tr2,turn)
                    prebuff(x,y,tr1,turn,field)
                    prebuff(y,x,tr2,turn,field)
                    if x.hp<=0:
                        x=faint(x,y,tr1,tr2,field,turn)
                        if len(tr1.pokemons)==0:
                            print(" 🏆 "+tr2.name,"wins.")
                            outro(tr2,tr1,y,field)
                            break
                    if y.hp<=0:
                        y=faint(y,x,tr2,tr1,field,turn)
                        if len(tr2.pokemons)==0:
                            print(" 🏆 "+tr1.name,"wins.")
                            outro(tr1,tr2,x,field)
                            break
                if y.hp<=0:
                    y=faint(y,x,tr2,tr1,field,turn)
                    effects(x,y,tr1,turn)
                    if x.hp<=0:
                        x=faint(x,y,tr1,tr2,field,turn)
                        if len(tr1.pokemons)==0:
                            print(" 🏆 "+tr2.name,"wins.")
                            outro(tr2,tr1,y,field)
                            break
                    if len(tr2.pokemons)==0:
                        print(" 🏆 "+tr1.name,"wins.")
                        outro(tr1,tr2,x,field)
                        break
                skip(x,y,tr1,tr2)
#P2 FAST
            elif y.speed>x.speed and field.trickroom==False:
                weather(y,x)
                 
                y,x=attack(y,x,tr2,tr1,choice2, choice1,field,turn)
                prebuff(x,y,tr1,turn,field)
                prebuff(y,x,tr2,turn,field)
                if y.hp<=0:
                    y=faint(y,x,tr2,tr1,field,turn)
                    if len(tr2.pokemons)==0:
                        print(" 🏆 "+tr1.name,"wins.")
                        outro(tr1,tr2,x,field)
                        break
                elif x.hp>0:
                     
                    x,y=attack(x,y,tr1,tr2,choice1,choice2,field,turn)
                    effects(y,x,tr2,turn)
                    effects (x,y,tr1,turn)
                    prebuff(x,y,tr1,turn,field)
                    prebuff(y,x,tr2,turn,field)
                    if y.hp<=0:
                        y=faint(y,x,tr2,tr1,field,turn)
                        if len(tr2.pokemons)==0:
                            print(" 🏆 "+tr1.name,"wins.")
                            outro(tr1,tr2,x,field)
                            break
                    if x.hp<=0:
                        x=faint(x,y,tr1,tr2,field,turn)
                        if len(tr1.pokemons)==0:
                            print(" 🏆 "+tr2.name,"wins.")
                            outro(tr2,tr1,y,field)
                            break
                if x.hp<=0:
                    x=faint(x,y,tr1,tr2,field,turn)
                    effects(y,x,tr2,turn)
                    if y.hp<=0:
                        y=faint(y,x,tr2,tr1,field,turn)
                        if len(tr2.pokemons)==0:
                            print(" 🏆 "+tr1.name,"wins.")
                            outro(tr1,tr2,x,field)
                            break
                    if len(tr1.pokemons)==0:
                        print(" 🏆 "+tr2.name,"wins.")
                        outro(tr2,tr1,y,field)
                        break
                skip(x,y,tr1,tr2)
#P2 FAST (TRICK ROOM)
            elif y.speed<=x.speed and field.trickroom==True:
                weather(y,x)
                 
                y,x=attack(y,x,tr2,tr1,choice2, choice1,field,turn)
                prebuff(x,y,tr1,turn,field)
                prebuff(y,x,tr2,turn,field)
                if y.hp<=0:
                    y=faint(y,x,tr2,tr1,field,turn)
                    if len(tr2.pokemons)==0:
                        print(" 🏆 "+tr1.name,"wins.")
                        outro(tr1,tr2,x,field)
                        break
                elif x.hp>0:
                     
                    x,y=attack(x,y,tr1,tr2,choice1,choice2,field,turn)
                    effects(y,x,tr2,turn)
                    effects (x,y,tr1,turn)
                    prebuff(x,y,tr1,turn,field)
                    prebuff(y,x,tr2,turn,field)
                    if y.hp<=0:
                        y=faint(y,x,tr2,tr1,field,turn)
                        if len(tr2.pokemons)==0:
                            print(" 🏆 "+tr1.name,"wins.")
                            outro(tr1,tr2,x,field)
                            break
                    if x.hp<=0:
                        x=faint(x,y,tr1,tr2,field,turn)
                        if len(tr1.pokemons)==0:
                            print(" 🏆 "+tr2.name,"wins.")
                            outro(tr2,tr1,y,field)
                            break
                if x.hp<=0:
                    x=faint(x,y,tr1,tr2,field,turn)
                    effects(y,x,tr2,turn)
                    if y.hp<=0:
                        y=faint(y,x,tr2,tr1,field,turn)
                        if len(tr2.pokemons)==0:
                            print(" 🏆 "+tr1.name,"wins.")
                            outro(tr1,tr2,x,field)
                            break
                    if len(tr1.pokemons)==0:
                        print(" 🏆 "+tr2.name,"wins.")
                        outro(tr2,tr1,y,field)
                        break
                skip(x,y,tr1,tr2)
#P1 SWITCH AND P2 ATTACK                
        elif action1==2 and action2==1:
            choice1=None
            score(x,y,p1,p2,turn)
            choice2=fchoice(y,tr2)  
            if p2.ai==True or choice2=="":             
                choice2=moveAI(y,x,tr2,tr1,field)[0]    
            if p2.ai==False:
                if y.dmax is True:
                    choice2=y.maxmove[choice2-1]
                if y.dmax is False:
                    choice2=y.moves[choice2-1]
            weather(y,x)
            x=switch(x,y,tr1,tr2,field,turn)
            y,x=attack(y,x,tr2,tr1,choice2, choice1,field,turn)
            effects(x,y,tr1,turn)
            effects(y,x,tr2,turn)
            prebuff(x,y,tr1,turn,field)
            prebuff(y,x,tr2,turn,field)
            if y.hp<=0:
                y=faint(y,x,tr2,tr1,field,turn)
                if len(tr2.pokemons)==0:
                    print(" 🏆 "+tr1.name,"wins.")
                    outro(tr1,tr2,x,field)
                    break
            if x.hp<=0:
                x=faint(x,y,tr1,tr2,field,turn)
                if len(tr1.pokemons)==0:
                    print(" 🏆 "+tr2.name,"wins.")
                    outro(tr2,tr1,y,field)
                    break
            y.protect=False
            skip(x,y,tr1,tr2)
#P1 ATTACKS AND P2 SWITCHES                
        elif action1==1 and action2==2:
            choice2=None
            score(x,y,p1,p2,turn)
            choice1=fchoice(x,tr1)
            if p1.ai==True or choice1=="":
                choice1=moveAI(x,y,tr1,tr2,field)[0]  
            if p1.ai==False:
                if x.dmax is True:
                    choice1=x.moves[choice1-1]    
                if x.dmax is False:
                    choice1=x.moves[choice1-1]        
            weather(y,x)
            y=switch(y,x,tr2,tr1,field,turn)
            x,y=attack(x,y,tr1,tr2,choice1,choice2,field,turn)
            if x.hp<=0:
                x=faint(x,y,tr1,tr2,field,turn)
                if len(tr1.pokemons)==0:
                    print(" 🏆 "+tr2.name,"wins.")
                    outro(tr2,tr1,y,field)
                    break
            effects(y,x,tr2,turn)
            effects(x,y,tr1,turn)
            prebuff(x,y,tr1,turn,field)
            prebuff(y,x,tr2,turn,field)
            if x.hp<=0:
                x=faint(x,y,tr1,tr2,field,turn)
                if len(tr1.pokemons)==0:
                    print(" 🏆 "+tr2.name,"wins.")
                    outro(tr2,tr1,y,field)
                    break
            if y.hp<=0:
                y=faint(y,x,tr2,tr1,field,turn)
                if len(tr2.pokemons)==0:
                    print(" 🏆 "+tr1.name,"wins.")
                    outro(tr1,tr2,x,field)
                    break
            x.protect=False
            skip(x,y,tr1,tr2)
#IF BOTH SWITCHES                
        elif action1==2 and action2==2:
            y=switch(y,x,tr2,tr1,field,turn)
            x=switch(x,y,tr1,tr2,field,turn)       
            effects(y,x,tr2,turn)
            if y.hp<=0:
                y=faint(y,x,tr2,tr1,field,turn)
                if len(tr2.pokemons)==0:
                    print(" 🏆 "+tr1.name,"wins.")
                    outro(tr1,tr2,x,field)
                    break
            effects(x,y,tr1,turn)              
            if x.hp<=0:
                x=faint(x,y,tr1,tr2,field,turn)
                if len(tr1.pokemons)==0:
                    print(" 🏆 "+tr2.name,"wins.")
                    outro(tr2,tr1,y,field)
                    break   
                skip(x,y,tr1,tr2)                              
