#from attack import *
#from moves import *
#from intros import intro
#from outros import outro
#from moreoptions import *
#from movelist import *
from doublebattle import *
import os
def clear ():
    os.system("cls" if os.name== "nt" else "clear")
"None"
#SCOREBOARD
def winner(tr,optr):
    tr.winner=True
    optr.winner=False
    cl="green"
    if tr.ai==True:
        cl="red"
    print(colored("===================================================================================",cl))
    if "Wild" not in tr.name:
        print(f" 🏆 {tr.name} won the match.")
    if "Wild" in tr.name:
        print(colored(f" {tr.pokemons[0].name} returned to {field.location.split(',')[0]}.","red"))
    print(colored("===================================================================================",cl))
    
def  score(x,y,tr1,tr2,turn,bg):
    print("")
    xitem="None"
    yitem="None"
    if "Used" not in y.item:
        yitem=y.item
    if "Used" not in x.item:
        xitem=x.item
    xs=ys=colored("ALIVE","green")
    xsa=ysa="red"
    xsb=ysb="yellow"
    xsc=ysc="magenta"
    xsd=ysd="blue"
    xse=yse="cyan"
    xa=xb=xc=xd=xe=ya=yb=yc=yd=ye="white"
    if x.atk!=x.maxspeed:
        if x.speed>x.maxspeed:
            xe="green"
        if x.speed<x.maxspeed:
            xe="red"
    if x.spdef!=x.maxspdef:
        if x.spdef>x.maxspdef:
            xd="green"
        if x.spdef<x.maxspdef:
            xd="red"
    if x.defense!=x.maxdef:
        if x.defense>x.maxdef:
            xb="green"
        if x.defense<x.maxdef:
            xb="red"
    if x.spatk!=x.maxspatk:
        if x.spatk>x.maxspatk:
            xc="green"
        if x.spatk<x.maxspatk:
            xc="red"
    if x.atk!=x.maxatk:
        if x.atk>x.maxatk:
            xa="green"
        if x.atk<x.maxatk:
            xa="red"
    if y.atk!=y.maxspeed:
        if y.speed>y.maxspeed:
            ye="green"
        if y.speed<y.maxspeed:
            ye="red"
    if y.spdef!=y.maxspdef:
        if y.spdef>y.maxspdef:
            yd="green"
        if y.spdef<y.maxspdef:
            yd="red"
    if y.defense!=y.maxdef:
        if y.defense>y.maxdef:
            yb="green"
        if y.defense<y.maxdef:
            yb="red"
    if y.spatk!=y.maxspatk:
        if y.spatk>y.maxspatk:
            yc="green"
        if y.spatk<y.maxspatk:
            yc="red"
    if y.atk!=y.maxatk:
        if y.atk>y.maxatk:
            ya="green"
        if y.atk<y.maxatk:
            ya="red"      
    if x.status=="Drowsy":
        xs=colored("DROWSY","white")
    if y.status=="Drowsy":
        ys=colored("DROWSY","white")            
    if x.status=="Sleep":
        xs=colored("SLEEP","cyan")
    if y.status=="Sleep":
        ys=colored("SLEEP","cyan")
    if x.status=="Frostbite":
        xs=colored("FROSTBITE","cyan")
    if y.status=="Frostbite":
        ys=colored("FROSTBITE","cyan")
    if y.status=="Badly Poisoned":
        ys=colored("BADLY POISONED","magenta")
    if y.status=="Poisoned":
        ys=colored("POISONED","magenta")
    if y.status=="Paralyzed":
        ys=colored("PARALYZED","yellow")
    if y.status=="Burned":
        ys=colored("BURNED","red")
    if y.status=="Frozen":
        ys=colored("FROZEN","cyan")
    if x.status=="Badly Poisoned":
        xs=colored("BADLY POISONED","magenta")
    if x.status=="Poisoned":
        xs=colored("POISONED","magenta")
    if x.status=="Paralyzed":
        xs=colored("PARALYZED","yellow")
    if x.status=="Burned":
        xs=colored("BURNED","red")
    if x.status=="Frozen":
        xs=colored("FROZEN","cyan")
    if x=="None":
        x=tr1.pokemons[0]
    if y=="None":
        y=tr2.pokemons[0]
        pass
    print(colored("===================================================================================",bg,attrs=["bold"]))
    print(f" {tr1.name}:")
    if len(tr1.hazard)!=0:
        print(" Hazards: ",end="")
        if "Stealth Rock" in tr1.hazard:
            print("🪨 ",end="")
        if "Steel Spikes" in tr1.hazard:
            print("📌 ",end="")
        if "Sticky Web" in tr1.hazard:
            print("🕸️ ",end="")
        if "Spikes" in tr1.hazard:
            print("✴️ "*tr1.hazard.count("Toxic Spikes"),end="")
        if "Toxic Spikes" in tr1.hazard:
            print("☠️ "*tr1.hazard.count("Toxic Spikes"),end="")
        print("")
    if tr1.tailwind==True:
        print(f" 🍃 Tailwind({tr1.twendturn-turn} turns left)")                   
    if tr1.reflect==True:
        print(f" 🟦 Reflect({tr1.rfendturn-turn} turns left)")   
    if tr1.auroraveil==True:
        print(f" ⬜ Aurora Veil({tr1.avendturn-turn} turns left)")
    if tr1.lightscreen==True:              
        print(f" 🟪 Light Screen({tr1.screenend-turn} turns left)")        
    print(colored(f" {x.name}",x.color,attrs=["bold"])+colored(f" Lv.{x.level}","white"),f"[{xs}]")
    print(colored(f" HP: ","green")+colored(f"{round(x.hp)}/{x.maxhp}({round((x.hp/x.maxhp)*100,3)}%)","white"))
    if x.status in ["Sleep","Drowsy"]:
        print(" "+"⬜"*int((x.hp/x.maxhp)*25))
    if x.status in ["Poisoned","Badly Poisoned"]:
        print(" "+"🟪"*int((x.hp/x.maxhp)*25))
    if x.status in ["Frozen","Frostbite"]:
        print(" "+"🟦"*int((x.hp/x.maxhp)*25))
    if x.status=="Burned":
        print(" "+"🟧"*int((x.hp/x.maxhp)*25))
    if x.status=="Paralyzed":
        print(" "+"🟨"*int((x.hp/x.maxhp)*25))
    if x.status=="Alive":
        if x.dmax is True:
            print(" "+"🛑"*int((x.hp/x.maxhp)*25))
        if x.dmax is False:
            if 6<=int((x.hp/x.maxhp)*10)<=10:
                print(" "+"🟩"*int((x.hp/x.maxhp)*25))
            if 3<int((x.hp/x.maxhp)*10)<6:
                print(" "+"🟨"*int((x.hp/x.maxhp)*25))
            if int((x.hp/x.maxhp)*10)<=3:
                print(" "+"🟥"*int((x.hp/x.maxhp)*25))
    if tr1.sub!="None":
        print(colored(" || Substitute || ","green"),end="")                
    if x.perishturn!=0:
        print(colored(" || Perishes in {x.perishturn-turn} turns || ","white"),end="")
    if x.encore==True:
        print(colored(" || Encore || ","white"),end="")
    if x.confused==True:
        print(colored(" || Confused || ","white"),end="")
    if x.taunted==True:
        print(colored(" || Taunt || ","red"),end="") 
    if x.seeded==True:
        print(colored(" || Leech Seed || ","green"),end="")
    if x.salty==True:
        print(colored(" || Salt Cure || ","yellow"),end="")
    if x.flashfire==True:
        print(colored(" || Flash Fire || ","red"),end="")
    if x.grav==True:
        print(colored(" || Gravity || ","magenta"),end="")
    if x.aring==True:
        print(colored(" || Aqua Ring || ","blue"),end="")
    if x.infestation!=0:
        print(colored(" || Infestation || ","green"),end="")
    if x.whirlpool!=0:
        print(colored(" || Whirlpool || ","blue"),end="")
    if x.firespin!=0:
        print(colored(" || Fire Spin || ","red"),end="")
    if x.cursed!=0:
        print(colored(" || Curse || ","magenta"),end="")
    if x.ability=="Supreme Overlord":
        print(colored(f" || Fallen: {6-len(tr1.pokemons)} || ","red"),end="")
    print(end="\n")
    #print("")
    if x.teratype !="None" and x.type2 =="None" and tr2.ai is True:
        print(colored(f" Type:{x.teratype} Ability: {x.ability} Item: {xitem} Nature: {x.nature}","white"))
    if x.teratype !="None" and x.type2 !="None" and tr2.ai is True:
        print(colored(f" Type:{x.teratype} Ability: {x.ability} Item: {xitem} Nature: {x.nature}","white"))
    if x.teratype =="None" and x.type2 =="None" and tr2.ai is True:
        print(colored(f" Type:{x.type1} Ability: {x.ability} Item: {xitem} Nature: {x.nature}","white"))
    if x.teratype =="None" and x.type2 !="None" and tr2.ai is True:
        print(colored(f" Type:{x.type1}/{x.type2} Ability: {x.ability} Item: {xitem} Nature: {x.nature}","white"))
    if tr2.ai is True:        
        print(colored(f" Atk: ",xsa)+colored(f"{round(x.atk)}({round(x.atkb,3)})",xa)+colored(f" Def: ",xsb)+colored(f"{round(x.defense)}({round(x.defb,3)})",xb)+colored(f" SpA: ",xsc)+colored(f"{round(x.spatk)}({round(x.spatkb,3)})",xc)+colored(f" SpD: ",xsd)+colored(f"{round(x.spdef)}({round(x.spdefb,3)})",xd)+colored(f" Spe: ",xse)+colored(f"{round(x.speed)}({round(x.speedb,3)})",xe))
    print(colored("===================================================================================",bg,attrs=["bold"]))
    print(f" {tr2.name}:")
    if len(tr2.hazard)!=0:
        print(" Hazards: ",end="")
        if "Stealth Rock" in tr2.hazard:
            print("🪨 ",end="")
        if "Steel Spikes" in tr2.hazard:
            print("📌 ",end="")
        if "Sticky Web" in tr2.hazard:
            print("🕸️ ",end="")
        if "Spikes" in tr2.hazard:
            print("✴️ "*tr2.hazard.count("Toxic Spikes"),end="")
        if "Toxic Spikes" in tr2.hazard:
            print("☠️ "*tr2.hazard.count("Toxic Spikes"),end="")
        print("")
    if tr2.tailwind==True:
        print(f" 🍃 Tailwind({tr2.twendturn-turn} turns left)")                
    if tr2.reflect==True:
        print(f" 🟦 Reflect({tr2.rfendturn-turn} turns left)")     
    if tr2.auroraveil==True:
        print(f" ⬜ Aurora Veil({tr2.avendturn-turn} turns left)")
    if tr2.lightscreen==True:        
        print(f" 🟪 Light Screen({tr2.screenend-turn} turns left)")               
    print(colored(f" {y.name}",y.color,attrs=["bold"])+colored(f" Lv.{y.level}","white"),f"[{ys}]")
    print(colored(f" HP: ","green")+colored(f"{round(y.hp)}/{y.maxhp}({round((y.hp/y.maxhp)*100,3)}%)","white"))
    if y.status in ["Sleep","Drowsy"]:
        print(" "+"⬜"*int((y.hp/y.maxhp)*25))
    if y.status in ["Poisoned","Badly Poisoned"]:
        print(" "+"🟪"*int((y.hp/y.maxhp)*25))
    if y.status in ["Frozen","Frostbite"]:
        print(" "+"🟦"*int((y.hp/y.maxhp)*25))
    if y.status=="Burned":
        print(" "+"🟧"*int((y.hp/y.maxhp)*25))
    if y.status=="Paralyzed":
        print(" "+"🟨"*int((y.hp/y.maxhp)*25))
    if y.status=="Alive":
        if y.dmax is True:
            print(" "+"🛑"*int((y.hp/y.maxhp)*25))
        if y.dmax is False:
            if int((y.hp/y.maxhp)*10)>=6:
                print(" "+"🟩"*int((y.hp/y.maxhp)*25))
            if 3<int((y.hp/y.maxhp)*10)<6:
                print(" "+"🟨"*int((y.hp/y.maxhp)*25))
            if int((y.hp/y.maxhp)*10)<=3:
                print(" "+"🟥"*int((y.hp/y.maxhp)*25))
    if tr2.sub!="None":
        print(colored(" || Substitute || ","green"),end="")                   
    if y.encore==True:
        print(colored(" || Encore || ","white"),end="")
    if y.perishturn!=0:
        print(colored(" || Perishes in {y.perishturn-turn} turns || ","white"),end="")
    if y.confused==True:
        print(colored(" || Confused || ","white"),end="")
    if y.taunted==True:
        print(colored(" || Taunt || ","red"),end="") 
    if y.seeded==True:
        print(colored(" || Leech Seed || ","green"),end="")
    if y.salty==True:
        print(colored(" || Salt Cure || ","yellow"),end="")
    if y.grav==True:
        print(colored(" || Gravity || ","magenta"),end="")
    if y.flashfire==True:
        print(colored(" || Flash Fire || ","red"),end="")
    if y.aring==True:
        print(colored(" || Aqua Ring || ","blue"),end="")
    if y.infestation!=0:
        print(colored(" || Infestation || ","green"),end="")
    if y.whirlpool!=0:
        print(colored(" || Whirlpool || ","blue"),end="")
    if y.firespin!=0:
        print(colored(" || Fire Spin || ","red"),end="")
    if y.cursed!=0:
        print(colored(" || Curse || ","magenta"),end="")
    if y.ability=="Supreme Overlord":
        print(colored(f" || Fallen: {6-len(tr2.pokemons)} || ","red"),end="")
    print(end="\n")                
    if y.teratype !="None" and y.type2 =="None" and tr1.ai is True:
        print(colored(f" Type:{y.teratype} Ability: {y.ability} Item: {yitem} Nature: {y.nature}","white"))
    if y.teratype !="None" and y.type2 !="None" and tr1.ai is True:
        print(colored(f" Type:{y.teratype} Ability: {y.ability} Item: {yitem} Nature: {y.nature}","white"))
    if y.teratype =="None" and y.type2 =="None" and tr1.ai is True:
        print(colored(f" Type:{y.type1} Ability: {y.ability} Item: {yitem} Nature: {y.nature}","white"))
    if y.teratype =="None" and y.type2 !="None" and tr1.ai is True:
        print(colored(f" Type:{y.type1}/{y.type2} Ability: {y.ability} Item: {yitem} Nature: {y.nature}","white"))
    if tr1.ai is True:
        print(colored(f" Atk: ",ysa)+colored(f"{round(y.atk)}({round(y.atkb,3)})",ya)+colored(f" Def: ",ysb)+colored(f"{round(y.defense)}({round(y.defb,3)})",yb)+colored(f" SpA: ",ysc)+colored(f"{round(y.spatk)}({round(y.spatkb,3)})",yc)+colored(f" SpD: ",ysd)+colored(f"{round(y.spdef)}({round(y.spdefb,3)})",yd)+colored(f" Spe: ",yse)+colored(f"{round(y.speed)}({round(y.speedb,3)})",ye))
    if tr1.ai is False:
        print(colored(f" Atk: ",ysa)+colored(f"{round(y.atkb,3)}",ya)+colored(f" Def: ",ysb)+colored(f"{round(y.defb,3)}",yb)+colored(f" SpA: ",ysc)+colored(f"{round(y.spatkb,3)}",yc)+colored(f" SpD: ",ysd)+colored(f"{round(y.spdefb,3)}",yd)+colored(f" Spe: ",yse)+colored(f"{round(y.speedb,3)}",ye))        
    print(colored("===================================================================================",bg,attrs=["bold"]))
#        print(colored(f" Atk: {round(y.atk)}({round(y.atkb,3)})",ya)+colored(f" Def: {round(y.defense)}({round(y.defb,3)})",yb)+colored(f" SpA: {round(y.spatk)}({round(y.spatkb,3)})",yc)+colored(f" SpD: {round(y.spdef)}({round(y.spdefb,3)})",yd)+colored(f" Spe: {round(y.speed)}({round(y.speedb,3)})\n",ye))
        
#FAINTED        
def healmon(self,tr):
    print(colored("===================================================================================","green"))
    print(f" 👤 {tr.name}: ")
    print(colored("===================================================================================","green"))
    if len(tr.item)!=0:
        x="None"
        n=0
        if tr.ai is False:
            print(f" {tr.name}'s Bag:")
            for i in tr.item:
                n+=1
                print(f" {n}. {i}")
            x=input(" What do you wanna use?\n >>>")
            if x in ["1","2","3","4","5"]:
                x=int(x)
            else:
                x=random.randint(1,len(tr.item))
            while True:
                if tr.item[x-1]=="X-Attack":
                    print(f" ⏫ {tr.name} used X-Attack on {self.name}!")
                    atkchange(self,self,0.5)
                    tr.item.remove("X-Attack")
                    break
                if tr.item[x-1]=="X-Defend":
                    print(f" ⏫ {tr.name} used X-Defend on {self.name}!")
                    defchange(self,self,0.5)
                    tr.item.remove("X-Defend") 
                    break
                if tr.item[x-1]=="Full Restore":
                    print(colored(f" 💉 {tr.name} used Full Restore on {self.name}!!","green",attrs=["bold"]))
                    tr.item.remove("Full Restore")
                    self.hp=self.maxhp
                    self.status="Alive"
                    break
                else:
                    break
        if tr.ai is True:
            while True:
                if "Full Restore" in tr.item and self.hp<self.maxhp*0.2:
                    print(colored(f" 💉 {tr.name} used Full Restore on {self.name}!!","green",attrs=["bold"]))
                    tr.item.remove("Full Restore")
                    self.hp=self.maxhp
                    self.status="Alive"
                    break 
                if "X-Defend" in tr.item and self.defense>other.atk and self.hp>self.maxhp*.7:
                    print(colored(f" ⏫ {tr.name} used X-Defend on {self.name}!!","yellow",attrs=["bold"]))
                    defchange(self,self,0.5)
                    tr.item.remove("X-Defend") 
                    break 
                if self.status!="Alive" and "Full Heal" in tr.item and self.hp>self.maxhp*0.7:
                    print(colored(f" 💉 {tr.name} used Full Heal on {self.name}!!","green",attrs=["bold"]))
                    tr.item.remove("Full Heal")
                    break
                else:
                    print(f" {tr.name} wasted a turn!")
                    break
            
    print(colored("===================================================================================","green"))        
    return self            
#ACTION             
def action(tr,self,other):
    if tr.ai is False:
        while True:
            print(" 1. 💥 Action")
            print(" 2. 🔁 Switch")
            print(" 3. ❌ Forfeit")
            print(" 4. 🐜 Pokémons")
            print(" 5. 🌐 Smogonify")
            if len(tr.item)!=0:
                print(" 6. 🎒 Bag")
            if tr.cantera==True and self.dmax==False and self.item not in megastones:
                print(f" 7. 💎 Terastallize({self.tera})")
            if tr.canmax==True and self.dmax==False and self.item not in megastones and self.teratype=="None":
                print(" 8. ⭕ Dynamax/Gigantamax")
            if tr.canmega==True and (self.item in megastones or "Dragon Ascent" in self.moves):
                print(" 9. 🧬 Mega Evolve")
            if "Ultranecrozium-Z" in self.item and "Ultra" not in self.name:
                print(" 10. ✴️ Ultra Burst")
            
            actionx= input(f"{tr.name}: What you wanna do?\n>>")
            if actionx in ["1","2","3","10","9","8","7","6"]:
                actionx=int(actionx)
            if actionx=="5":
                print(showsmogon(tr))
                action(tr,self,other)
            if actionx=="4":
                showmon(tr)
                n=(input("Which pokemon you wanna see?\n>>"))
                if n in ["1","2","3","4","5","6","10","9","8","7","11"]:
                    n=int(n)
                    tr.pokemons[n-1].info()
                    movelist(tr.pokemons[n-1],other,field)
            if actionx in [1,2,3,9,10,8,7,6]:
                if actionx==2:
                    if len(self.owner.item)==0:
                        action=1
                    if self.fmoveturn!=0:
                        action=1
                    if self.firespin!=0 or self.infestation!=0 or self.whirlpool!=0:
                        action=1
                        print(f" {self.name} is trapped and cannot escape!")
                    if self.precharge==True:
                        action=1
                    if other.ability=="Magnet Pull" and (self.ability!="Levitate" or "Steel" in (self.type1,self.type2,self.teratype)):
                        print(f" 🧲 {other.name}'s Magnet Pull!")
                        actionx=1
                    if self.trap==other or self.trap==True:
                        print(f" ❌ {self.name} cannot escape from the battlefield!")
                    if other.ability=="Shadow Tag" and (self.ability!="Levitate" or "Ghost" not in (self.type1,self.type2,self.teratype)):
                        print(f" 🔖 {other.name}'s Shadow Tag!")
                        actionx=1
                    if other.ability=="Arena Trap" and (self.ability!="Levitate" or "Flying" not in (self.type1,self.type2,self.teratype)):
                        print(f" 🏜️ {other.name}'s Arena Trap!")
                        actionx=1
                return actionx    
                break    
            if actionx=="":
                rn=[1,2,3]
                actionx=1
                return actionx
                break
    if tr.ai is True:
            return 1        


#BATTLE
def singlebattle(btype):
    print(f" Please wait for a while...\n")
    print(colored(f" Location: {field.location}","white"))
    tr1=players(1)
    tr2=players(2)
    bg="white"
    if len(tr1.pokemons)==6:
        createtable(tr1)
    if len(tr2.pokemons)==6:
        createtable(tr2)
    play=play2="None"
    play=input(f" ⚠️ Do you want to play as {tr1.name} or Simulate? ('yes'/Press Enter)\n >>>").lower()
    if play=="yes":
        play=False
    else:
        play=True
    play2=input(f" ⚠️ Do you want to play as {tr2.name} or Simulate? ('yes'/Press Enter)\n >>>").lower()
    if play2=="yes":
        play2=False
    else:
        play2=True
    tr1.ai=play
    tr2.ai=play2
    showparty(tr1)
    showparty (tr2)
    x=leadchoice(tr1)
    y=leadchoice(tr2)  
    print("")
    if tr1.ai is False or (tr1.ai,tr2.ai)==(True,True):
        showteam(tr1)
        print("\n")
    if tr2.ai is False or (tr1.ai,tr2.ai)==(True,True):    
        showteam(tr2)
        print("\n")
    turn=0
    print("===================================================================================")
    #field.weather,field.terrain=randomweather(turn,x,y,field)
    intro(tr1,tr2,field)
    intro(tr2,tr1,field)
    if "Wild" not in (tr1.name,tr2.name):
        print(f" {tr2.name} was challenged by {tr1.name}!")
        print(f" Battle between {tr1.name} and {tr2.name} begun!")
    if "Wild" in tr1.name and "Wild" not in tr2.name :
        print(colored(f" {tr2.name} sensed some wild pokémon nearby!","white"))
        print(colored(f" {tr1.pokemons[0].name}: Grawwwrr...","white"))
        print(colored(f" A {tr1.pokemons[0].name} appeared!","white"))
    if "Wild" in tr2.name and "Wild" not in tr1.name :
        print(colored(f" {tr1.name} sensed some wild pokémon nearby!","white"))
        print(colored(f" {tr2.pokemons[0].name}: Grawwwrr...","white"))
        print(colored(f" A {tr2.pokemons[0].name} appeared!","white"))
    print("===================================================================================")
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
        if field.terrain in ["Normal"]:
            bg="white"
        if field.weather=="Strong Winds":
            bg="green"
        if field.weather=="Desolate Land":
            bg="red"
        if field.weather=="Primordial Sea":
            bg="blue"
        if field.weather in ["Hail","Snowstorm"]:
            if field.weather=="Snowstorm":
                bg="cyan"
            if field.weather=="Hail":
                bg="cyan"
        if field.weather in ["Clear","None"]:
            bg="white"
        if field.weather=="Cloudy": 
            bg="white"  
        if field.weather=="Rainy":
            bg="blue"
        if field.weather=="Sunny":
            bg="yellow"
        if field.weather=="Sandstorm":
            bg="yellow"
        if field.terrain=="Misty":
            bg="magenta"
        if field.terrain=="Psychic":
            bg="magenta"
        if field.terrain=="Electric":
            bg="yellow"
        if field.terrain=="Grassy":
            bg="green"
        
        print(colored("===================================================================================",bg,attrs=["bold"]))
        print(colored(f" TURN: {turn}","white"))
        if x.protect==True:
            x.protect=False
        if y.protect==True:
            y.protect=False
        print(colored("===================================================================================",bg,attrs=["bold"]))
        print(f" Location: {field.location}")
        print(f" Battle: {btype}")
        if field.weather=="Strong Winds":
            print(f" Weather: 🍃 Strong Winds")
        if field.weather=="Desolate Land":
            print(colored(f" Weather: 🌋 Extremely Harsh Sunlightt","red"))
        if field.weather=="Primordial Sea":
            print(colored(f" Weather: 🌊 Heavy Rainn","blue"))
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
        if field.weather in ["Clear","None"]:
            print(f" Weather: 🌥️ {field.weather}")
        if field.weather=="Cloudy":
            print(f" Weather: ☁️ {field.weather}")
        if field.weather=="Rainy" and field.terrain not in ["Electric","Grassy"]:
            print(f" Weather: ☔ {field.weather} ({field.rainendturn-turn+1} turns left)")
        if field.weather=="Sunny":
            print(f" Weather: ☀️ {field.weather} ({field.sunendturn-turn+1} turns left)")
        if field.weather=="Sandstorm":
            print(f" Weather: 🏜️ {field.weather} ({field.sandendturn-turn+1} turns left)")
        if field.terrain=="Misty":      
            print(colored(f" Terrain: 🌸 {field.terrain} ({field.misendturn-turn+1} turns left))","magenta"))
        if field.terrain=="Psychic":      
            print(colored(f" Terrain: 👁️ {field.terrain} ({field.psyendturn-turn+1} turns left))","magenta"))
        if field.terrain in ["Normal"]:      
            print(colored(f" Terrain: 🌐 Normall","white"))
        if field.terrain=="Electric":      
            print(colored(f" Terrain: ⚡ {field.terrain} ({field.eleendturn-turn+1} turns left))","yellow"))
        if field.terrain=="Grassy":      
            print(colored(f" Terrain: 🌿 {field.terrain} ({field.grassendturn-turn+1} turns left))","green"))
        if field.trickroom is True:
            print(f" Dimension: 🌀 Trick Room ({field.troomendturn-turn+1} turns left)")           
        print(f" \n ⏩⏩ {tr1.name} ({len(tr1.pokemons)}) 🆚 ({len(tr2.pokemons)}) {tr2.name} ⏪⏪\n")
        print(f" \n ⏩⏩ Lv.{x.level} {x.name} 🆚 {y.name} Lv.{y.level} ⏪⏪\n")
        prebuff(x,y,tr1,turn,field)
        prebuff(y,x,tr2,turn,field)
        switchAI(x,y,tr1,tr2, field)
        switchAI(y,x,tr2,tr1,field)
 
        #score(x,y,tr1,tr2,turn,bg)
        tr1.mon=x
        tr2.mon=y
        action1=action(tr1,x,y)
        action2=action(tr2,y,x)
        check=len(moveAI(y,x,tr2,tr1,field)[1])
        check2=len(moveAI(x,y,tr1,tr2,field)[1])
        if tr1.ai is True:
            action1=decision(x,y,tr1,tr2,field)
        if tr2.ai is True:
            action2=decision(y,x,tr2,tr1,field)
        #print(action1,action2)
        if action2==6 and (len(tr2.item)==0 or tr2.ai==False):
            print(f" 🎒 Your Bag is empty or it's locked!")
            action2=1
        if action1==6 and (len(tr1.item)==0 or tr1.ai==False):
            print(f" 🎒 Your Bag is empty or It's locked!")
            action1=1
        if  action1==3 and action2!=3:
            print(f" {tr1.name} forfeited.")
            tr2.winner=True
            tr1.winner=False
            break
        if  action2==3 and action1!=3:
            print(f" {tr2.name} forfeited.")
            tr1.winner=True
            tr2.winner=False
            break
        if action1 in [8,9,10,7]:
            if action1==7 and x.dmax==False and (x.item=="None" or x.item not in megastones) and "m-Z" not in x.item and tr1.cantera==True:
                x.name+="💎"
                transformation(x,y,turn)
            if action1==8 and "m-Z" not in x.item and x.teratype=="None" and tr1.canmax==True and ("Zacian" not in x.name and "Zamazenta" not in x.name and "Eternatus" not in x.name and "Rayquaza" not in x.name and "Primal" not in x.name and "Mega" not in x.name) and x.teratype=="None":
                x.dmax=True
                tr1.canmax=False
                transformation(x,y,turn)
            if action1==9 and tr1.canmega is True and (((x.item!="None" and x.item in megastones) or ("Dragon Ascent" in x.moves)) and x.dmax==False):
                transformation(x,y,turn)
            if action1==10:
                transformation(x,y,turn)
            action1=1
        if action2 in [8,9,10,7]:
            if action2==7 and y.dmax==False and (y.item=="None" or y.item not in megastones) and "m-Z" not in y.item and tr2.cantera==True:
                y.name+="💎"
                transformation(y,x,turn)
            if action2==8 and "m-Z" not in y.item and y.teratype=="None" and tr2.canmax==True  and ("Zacian" not in y.name and "Zamazenta" not in y.name and "Eternatus" not in y.name and "Rayquaza" not in y.name and "Primal" not in y.name and "Mega" not in y.name) and y.teratype=="None":
                y.dmax=True
                tr2.canmax=False
                transformation(y,x,turn)
            if action2==9 and tr2.canmega is True and ((y.item!="None" and y.item in megastones) or ("Dragon Ascent" in y.moves)):
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
            score(x,y,tr1,tr2,turn,bg)
            choice1=fchoice(x,y,tr1,field)
            choice2=fchoice(y,x,tr2,field)    
            if tr1.ai==True or choice1=="":              
                choice1=moveAI(x,y,tr1,tr2,field)[0]
            if tr1.ai==False:     
                if x.dmax is True:
                    choice1=x.maxmove[choice1-1]
                if x.dmax is False:
                    choice1=x.moves[choice1-1]
            if tr2.ai==True or choice2=="":  
                choice2=moveAI(y,x,tr2,tr1,field)[0]     
            if tr2.ai==False:   
                if y.dmax is False:
                    choice2=y.moves[choice2-1]     
                if y.dmax is True:
                    choice2=y.maxmove[choice2-1]
            xPriority=0
            yPriority=0
            if y.ability=="Quick Draw":
                yPriority=random.randint(1,100)     
                if yPriority>80:
                    yPriority=True
            if x.ability=="Quick Draw":
                xPriority=random.randint(1,100)
                if xPriority>20:
                    xPriority=True
            if x.item=="Quick Claw":
                xPriority=random.randint(1,100)
                if xPriority>82:
                    xPriority=True
            if y.item=="Quick Claw":
                yPriority=random.randint(1,100)
                if yPriority>82:
                    yPriority=True
            if y.item=="Quick Claw" and y.ability=="Quick Draw":
                yPriority=random.randint(1,100)
                if yPriority>64:
                    yPriority=True
            if x.item=="Quick Claw" and x.ability=="Quick Draw":
                xPriority=random.randint(1,100)
                if xPriority>64:
                    xPriority=True
#tr1 PRIORITY            
            if (choice1 in typemoves.prioritymove and choice2 not in typemoves.prioritymove) or x.priority is True or (x.ability=="Prankster" and choice1 in typemoves.statusmove and "Dark" not in (y.type1,y.type2)) or (choice1 in typemoves.firemoves and x.ability=="Blazing Soul") or (choice1 in typemoves.flyingmoves and x.ability=="Gale Wings") or (field.terrain=="Grassy" and choice1=="Grassy Glide") or (x.ability=="Triage" and choice1 in typemoves.healingmoves) or (choice2 in typemoves.negprioritymove) or (xPriority==True) or (choice2 in typemoves.statusmove and y.ability=="Mycelium Might") or y.item=="Lagging Tail":
                weather(x,y)
                x,y=attack(x,y,tr1,tr2,choice1,choice2,field,turn)
                prebuff(x,y,tr1,turn,field)
                prebuff(y,x,tr2,turn,field)
                if x.hp<=0:
                    x=faint(x,y,tr1,tr2,field,turn)
                    if len(tr1.pokemons)==0:
                        winner(tr2,tr1)
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
                            winner(tr2,tr1)
                            outro(tr2,tr1,y,field)
                            break
                    if y.hp<=0:
                        y=faint(y,x,tr2,tr1,field,turn)
                        if len(tr2.pokemons)==0:
                            winner(tr1,tr2)
                            outro(tr1,tr2,x,field)
                            break
                if y.hp<=0:
                    y=faint(y,x,tr2,tr1,field,turn)
                    effects(x,y,tr1,turn)
                    if x.hp<=0:
                        x=faint(x,y,tr1,tr2,field,turn)
                        if len(tr1.pokemons)==0:
                            winner(tr2,tr1)
                            outro(tr2,tr1,y,field)
                            break
                    if len(tr2.pokemons)==0:
                        winner(tr1,tr2)
                        outro(tr1,tr2,x,field)
                        break
                x.priority=False
                skip(x,y,tr1,tr2,field)
#tr2 PRIORITY 
            elif (choice2 in typemoves.prioritymove and choice1 not in typemoves.prioritymove) or y.priority is True or (y.ability=="Prankster" and choice2 in typemoves.statusmove and "Dark" not in (x.type1,x.type2)) or (choice2 in typemoves.firemoves and y.ability=="Blazing Soul") or (choice2 in typemoves.flyingmoves and y.ability=="Gale Wings") or (field.terrain=="Grassy" and choice2=="Grassy Glide") or (y.ability=="Triage" and choice2 in typemoves.healingmoves) or (choice1 in typemoves.negprioritymove) or (yPriority==True) or (choice1 in typemoves.statusmove and x.ability=="Mycelium Might") or x.item=="Lagging Tail":
                weather(y,x)
                y,x=attack(y,x,tr2,tr1,choice2, choice1,field,turn)
                prebuff(x,y,tr1,turn,field)
                prebuff(y,x,tr2,turn,field)
                if y.hp<=0:
                    y=faint(y,x,tr2,tr1,field,turn)
                    if len(tr2.pokemons)==0:
                        winner(tr1,tr2)
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
                            winner(tr1,tr2)
                            outro(tr1,tr2,x,field)
                            break
                    if x.hp<=0:
                        x=faint(x,y,tr1,tr2,field,turn)
                        if len(tr1.pokemons)==0:
                            winner(tr2,tr1)
                            outro(tr2,tr1,y,field)
                            break
                if x.hp<=0:
                    x=faint(x,y,tr1,tr2,field,turn)
                    effects(y,x,tr2,turn)
                    if y.hp<=0:
                        y=faint(y,x,tr2,tr1,field,turn)
                        if len(tr2.pokemons)==0:
                            winner(tr1,tr2)
                            outro(tr1,tr2,x,field)
                            break
                    if len(tr1.pokemons)==0:
                        winner(tr2,tr1)
                        outro(tr2,tr1,y,field)
                        break
                y.priority=False
                skip(x,y,tr1,tr2,field)
#tr1 FAST
            elif x.speed>=y.speed and field.trickroom==False:
                weather(x,y)        
                #X Attacks         
                x,y=attack(x,y,tr1,tr2,choice1,choice2,field,turn)
                #Stat Clac
                prebuff(x,y,tr1,turn,field)
                prebuff(y,x,tr2,turn,field)
                #Checks X's HP
                if x.hp<=0:
                    x=faint(x,y,tr1,tr2,field,turn)
                    if len(tr1.pokemons)==0:
                        winner(tr2,tr1)
                        outro(tr2,tr1,y,field)
                        break
                #elif y.hp>0: (edited here)
                elif y.hp>0:                    
                    y,x=attack(y,x,tr2,tr1,choice2, choice1,field,turn)
                    effects (x,y,tr1,turn)
                    effects(y,x,tr2,turn)
                    prebuff(x,y,tr1,turn,field)
                    prebuff(y,x,tr2,turn,field)
                    if x.hp<=0:
                        x=faint(x,y,tr1,tr2,field,turn)
                        if len(tr1.pokemons)==0:
                            winner(tr2,tr1)
                            outro(tr2,tr1,y,field)
                            break
                    if y.hp<=0:
                        y=faint(y,x,tr2,tr1,field,turn)
                        if len(tr2.pokemons)==0:
                            winner(tr1,tr2)
                            outro(tr1,tr2,x,field)
                            break
                if y.hp<=0:
                    y=faint(y,x,tr2,tr1,field,turn)
                    effects(x,y,tr1,turn)
                    if x.hp<=0:
                        x=faint(x,y,tr1,tr2,field,turn)
                        if len(tr1.pokemons)==0:
                            winner(tr2,tr1)
                            outro(tr2,tr1,y,field)
                            break
                    if len(tr2.pokemons)==0:
                        winner(tr1,tr2)
                        outro(tr1,tr2,x,field)
                        break
                skip(x,y,tr1,tr2,field)
#tr2 FAST (TRICK ROOM)
            elif x.speed<y.speed and field.trickroom==True:
                weather(x,y)
                 
                x,y=attack(x,y,tr1,tr2,choice1,choice2,field,turn)
                prebuff(x,y,tr1,turn,field)
                prebuff(y,x,tr2,turn,field)
                if x.hp<=0:
                    x=faint(x,y,tr1,tr2,field,turn)
                    if len(tr1.pokemons)==0:
                        winner(tr2,tr1)
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
                            winner(tr2,tr1)
                            outro(tr2,tr1,y,field)
                            break
                    if y.hp<=0:
                        y=faint(y,x,tr2,tr1,field,turn)
                        if len(tr2.pokemons)==0:
                            winner(tr1,tr2)
                            outro(tr1,tr2,x,field)
                            break
                if y.hp<=0:
                    y=faint(y,x,tr2,tr1,field,turn)
                    effects(x,y,tr1,turn)
                    if x.hp<=0:
                        x=faint(x,y,tr1,tr2,field,turn)
                        if len(tr1.pokemons)==0:
                            winner(tr2,tr1)
                            outro(tr2,tr1,y,field)
                            break
                    if len(tr2.pokemons)==0:
                        winner(tr1,tr2)
                        outro(tr1,tr2,x,field)
                        break
                skip(x,y,tr1,tr2,field)
#tr2 FAST
            elif y.speed>x.speed and field.trickroom==False:
                weather(y,x)
                 
                y,x=attack(y,x,tr2,tr1,choice2, choice1,field,turn)
                prebuff(x,y,tr1,turn,field)
                prebuff(y,x,tr2,turn,field)
                if y.hp<=0:
                    y=faint(y,x,tr2,tr1,field,turn)
                    if len(tr2.pokemons)==0:
                        winner(tr1,tr2)
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
                            winner(tr1,tr2)
                            outro(tr1,tr2,x,field)
                            break
                    if x.hp<=0:
                        x=faint(x,y,tr1,tr2,field,turn)
                        if len(tr1.pokemons)==0:
                            winner(tr2,tr1)
                            outro(tr2,tr1,y,field)
                            break
                if x.hp<=0:
                    x=faint(x,y,tr1,tr2,field,turn)
                    effects(y,x,tr2,turn)
                    if y.hp<=0:
                        y=faint(y,x,tr2,tr1,field,turn)
                        if len(tr2.pokemons)==0:
                            winner(tr1,tr2)
                            outro(tr1,tr2,x,field)
                            break
                    if len(tr1.pokemons)==0:
                        winner(tr2,tr1)
                        outro(tr2,tr1,y,field)
                        break
                skip(x,y,tr1,tr2,field)
#tr2 FAST (TRICK ROOM)
            elif y.speed<=x.speed and field.trickroom==True:
                weather(y,x)
                 
                y,x=attack(y,x,tr2,tr1,choice2, choice1,field,turn)
                prebuff(x,y,tr1,turn,field)
                prebuff(y,x,tr2,turn,field)
                if y.hp<=0:
                    y=faint(y,x,tr2,tr1,field,turn)
                    if len(tr2.pokemons)==0:
                        winner(tr1,tr2)
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
                            winner(tr1,tr2)
                            outro(tr1,tr2,x,field)
                            break
                    if x.hp<=0:
                        x=faint(x,y,tr1,tr2,field,turn)
                        if len(tr1.pokemons)==0:
                            winner(tr2,tr1)
                            outro(tr2,tr1,y,field)
                            break
                if x.hp<=0:
                    x=faint(x,y,tr1,tr2,field,turn)
                    effects(y,x,tr2,turn)
                    if y.hp<=0:
                        y=faint(y,x,tr2,tr1,field,turn)
                        if len(tr2.pokemons)==0:
                            winner(tr1,tr2)
                            outro(tr1,tr2,x,field)
                            break
                    if len(tr1.pokemons)==0:
                        winner(tr2,tr1)
                        outro(tr2,tr1,y,field)
                        break
                skip(x,y,tr1,tr2,field)
#tr1 SWITCH AND tr2 ATTACK                
        elif action1==2 and action2==1:
            choice1="None"
            score(x,y,tr1,tr2,turn,bg)
            choice2=fchoice(y,x,tr2,field)  
            if tr2.ai==True or choice2=="":             
                choice2=moveAI(y,x,tr2,tr1,field)[0]    
            if tr2.ai==False:
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
                    winner(tr1,tr2)
                    outro(tr1,tr2,x,field)
                    break
            if x.hp<=0:
                x=faint(x,y,tr1,tr2,field,turn)
                if len(tr1.pokemons)==0:
                    winner(tr2,tr1)
                    outro(tr2,tr1,y,field)
                    break
            y.protect=False
            skip(x,y,tr1,tr2,field)
#tr1 ATTACKS AND tr2 SWITCHES                
        elif action1==1 and action2==2:
            choice2="None"
            score(x,y,tr1,tr2,turn,bg)
            choice1=fchoice(x,y,tr1,field)
            if tr1.ai==True or choice1=="":
                choice1=moveAI(x,y,tr1,tr2,field)[0]  
            if tr1.ai==False:
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
                    winner(tr2,tr1)
                    outro(tr2,tr1,y,field)
                    break
            effects(y,x,tr2,turn)
            effects(x,y,tr1,turn)
            prebuff(x,y,tr1,turn,field)
            prebuff(y,x,tr2,turn,field)
            if x.hp<=0:
                x=faint(x,y,tr1,tr2,field,turn)
                if len(tr1.pokemons)==0:
                    winner(tr2,tr1)
                    outro(tr2,tr1,y,field)
                    break
            if y.hp<=0:
                y=faint(y,x,tr2,tr1,field,turn)
                if len(tr2.pokemons)==0:
                    winner(tr1,tr2)
                    outro(tr1,tr2,x,field)
                    break
            x.protect=False
            skip(x,y,tr1,tr2,field)
#IF BOTH SWITCHES                
        elif action1==2 and action2==2:
            score(x,y,tr1,tr2,turn,bg)
            y=switch(y,x,tr2,tr1,field,turn)
            x=switch(x,y,tr1,tr2,field,turn)       
            effects(y,x,tr2,turn)
            if y.hp<=0:
                y=faint(y,x,tr2,tr1,field,turn)
                if len(tr2.pokemons)==0:
                    winner(tr1,tr2)    
                    outro(tr1,tr2,x,field)
                    break
            effects(x,y,tr1,turn)              
            if x.hp<=0:
                x=faint(x,y,tr1,tr2,field,turn)
                if len(tr1.pokemons)==0:
                    winner(tr2,tr1)
                    outro(tr2,tr1,y,field)
                    break   
                skip(x,y,tr1,tr2,field)       
#tr1 heals AND tr2 ATTACK                
        elif action1==6 and action2==1:
            choice1="None"
            score(x,y,tr1,tr2,turn,bg)
            choice2=fchoice(y,x,tr2,field)  
            if tr2.ai==True or choice2=="":             
                choice2=moveAI(y,x,tr2,tr1,field)[0]    
            if tr2.ai==False:
                if y.dmax is True:
                    choice2=y.maxmove[choice2-1]
                if y.dmax is False:
                    choice2=y.moves[choice2-1]
            weather(y,x)
            x=healmon(x,tr1)
            y,x=attack(y,x,tr2,tr1,choice2, choice1,field,turn)
            effects(x,y,tr1,turn)
            effects(y,x,tr2,turn)
            prebuff(x,y,tr1,turn,field)
            prebuff(y,x,tr2,turn,field)
            if y.hp<=0:
                y=faint(y,x,tr2,tr1,field,turn)
                if len(tr2.pokemons)==0:
                    winner(tr1,tr2)
                    outro(tr1,tr2,x,field)
                    break
            if x.hp<=0:
                x=faint(x,y,tr1,tr2,field,turn)
                if len(tr1.pokemons)==0:
                    winner(tr2,tr1)
                    outro(tr2,tr1,y,field)
                    break
            y.protect=False
            skip(x,y,tr1,tr2,field) 
#tr1 heals AND tr2 switches             
        elif action1==6 and action2==2:
            choice1="None"
            score(x,y,tr1,tr2,turn,bg)
            weather(y,x)
            y=switch(y,x,tr2,tr1,field,turn)
            x=healmon(x,tr1)
            effects(x,y,tr1,turn)
            effects(y,x,tr2,turn)
            prebuff(x,y,tr1,turn,field)
            prebuff(y,x,tr2,turn,field)
            if y.hp<=0:
                y=faint(y,x,tr2,tr1,field,turn)
                if len(tr2.pokemons)==0:
                    winner(tr1,tr2)
                    outro(tr1,tr2,x,field)
                    break
            if x.hp<=0:
                x=faint(x,y,tr1,tr2,field,turn)
                if len(tr1.pokemons)==0:
                    winner(tr2,tr1)
                    outro(tr2,tr1,y,field)
                    break
            y.protect=False
            skip(x,y,tr1,tr2,field) 
#tr2 heals AND tr1 switches             
        elif action1==2 and action2==6:
            choice1="None"
            score(x,y,tr1,tr2,turn,bg)
            weather(y,x)
            x=switch(x,y,tr1,tr2,field,turn) 
            y=healmon(y,tr2)
            effects(x,y,tr1,turn)
            effects(y,x,tr2,turn)
            prebuff(x,y,tr1,turn,field)
            prebuff(y,x,tr2,turn,field)
            if y.hp<=0:
                y=faint(y,x,tr2,tr1,field,turn)
                if len(tr2.pokemons)==0:
                    winner(tr1,tr2)
                    outro(tr1,tr2,x,field)
                    break
            if x.hp<=0:
                x=faint(x,y,tr1,tr2,field,turn)
                if len(tr1.pokemons)==0:
                    winner(tr2,tr1)
                    outro(tr2,tr1,y,field)
                    break
            y.protect=False
            skip(x,y,tr1,tr2,field)                             
#tr1 ATTACKS AND tr2 heals               
        elif action1==1 and action2==6:
            choice2="None"
            score(x,y,tr1,tr2,turn,bg)
            choice1=fchoice(x,y,tr1,field)
            if tr1.ai==True or choice1=="":
                choice1=moveAI(x,y,tr1,tr2,field)[0]  
            if tr1.ai==False:
                if x.dmax is True:
                    choice1=x.moves[choice1-1]    
                if x.dmax is False:
                    choice1=x.moves[choice1-1]        
            weather(y,x)
            y=healmon(y,tr2)
            x,y=attack(x,y,tr1,tr2,choice1,choice2,field,turn)
            if x.hp<=0:
                x=faint(x,y,tr1,tr2,field,turn)
                if len(tr1.pokemons)==0:
                    winner(tr2,tr1)
                    outro(tr2,tr1,y,field)
                    break
            effects(y,x,tr2,turn)
            effects(x,y,tr1,turn)
            prebuff(x,y,tr1,turn,field)
            prebuff(y,x,tr2,turn,field)
            if x.hp<=0:
                x=faint(x,y,tr1,tr2,field,turn)
                if len(tr1.pokemons)==0:
                    winner(tr2,tr1)
                    outro(tr2,tr1,y,field)
                    break
            if y.hp<=0:
                y=faint(y,x,tr2,tr1,field,turn)
                if len(tr2.pokemons)==0:
                    winner(tr1,tr2)
                    outro(tr1,tr2,x,field)
                    break
            x.protect=False
            skip(x,y,tr1,tr2,field)     
#IF BOTH heals               
        elif action1==6 and action2==6:
            score(x,y,tr1,tr2,turn,bg)
            y=healmon(y,tr2)
            x=healmon(x,tr1) 
            effects(y,x,tr2,turn)
            if y.hp<=0:
                y=faint(y,x,tr2,tr1,field,turn)
                if len(tr2.pokemons)==0:
                    winner(tr1,tr2)    
                    outro(tr1,tr2,x,field)
                    break
            effects(x,y,tr1,turn)              
            if x.hp<=0:
                x=faint(x,y,tr1,tr2,field,turn)
                if len(tr1.pokemons)==0:
                    winner(tr2,tr1)
                    outro(tr2,tr1,y,field)
                    break   
                skip(x,y,tr1,tr2,field)
    