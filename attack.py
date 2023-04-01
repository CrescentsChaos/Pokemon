from fieldtrip import *
from moves import *
pkball=random.choice(["Poké Ball","Great Ball","Ultra Ball","Net Ball","Quick Ball","Master Ball","Beast Ball","Dive Ball","Nest Ball","Repeat Ball","Timer Ball","Cherish Ball","Dream Ball","Dusk Ball","Fast Ball","Heal Ball","Heavy Ball","Level Ball","Love Ball","Lure Ball","Luxury Ball","Moon Ball","Park Ball","Premier Ball","Safari Ball"])
allmove=list(set(typemoves.firemoves+typemoves.watermoves+typemoves.electricmoves+typemoves.grassmoves+typemoves.normalmoves+typemoves.darkmoves+typemoves.ghostmoves+typemoves.psychicmoves+typemoves.poisonmoves+typemoves.steelmoves+typemoves.fairymoves+typemoves.bugmoves+typemoves.fightingmoves+typemoves.flyingmoves+typemoves.icemoves+typemoves.rockmoves+typemoves.groundmoves+typemoves.dragonmoves+typemoves.statusmove)-set(typemoves.zmoves+typemoves.maxmovelist))
#n=0
#for i in allmove:
#    n+=1
#    print(str(n)+"."+i)
nondmgmove=typemoves.statusmove+typemoves.buffmove+["Stealth Rock","Toxic","Toxic Spikes","Sticky Web","Trick Room"]

def faint(self,other,tr,optr,field,turn):
    if self.hp<=0:
        print("===================================================================================")
        prdx=[]
        di=[]
        nn=0
        self.hp=0
        self.status="Fainted"
        name=self.name
        if self.dmax is True:
            self.dmax=False
            nn=-1
            prdx=["Great Tusk","Sandy Shocks","Roaring Moon","Brute Bonnet","Slither Wing","Flutter Mane","Scream Tail","Iron","Unbound","Tapu","Black","White","Attack","Defense","Speed","Hero","Alolan","Hisuian","Galarian","Dusk Mane","Dawn Wing","Black","White","Ice Rider","Shadow Rider","Tapu","Wake"]
        di=["Single","Rapid"]
        for i in di:
            if i in self.name:
                nn=3
        for i in prdx:
            if i in self.name:
                nn=-2
        if nn==3:
            self.name=self.name.split("Gigantamax ")[-1]
        if nn==-1:
            self.name=self.name.split("Dynamax ")[-1]
        if nn==-2:
            self.name=name[8:]
            print(f" 🔻 {name} returned to it's normal state!")
            self.name=name
        if "Mega " in self.name:
            name=self.name.split(" ")[-1]
            if "Mewtwo" in self.name:
                name="Mewtwo"
            if "Charizard" in self.name:
                name="Charizard"
            print(f" 🧬 {name} returned to it's normal state!")
        print(f" 🏁 Refree: {self.name} is unable to battle!")
        print(f" 😵😵‍💫 {tr.name}'s {self.name} fainted!")
        print( " ❌❌❌❌❌ "+colored ("KO: ","white")+colored(self.name.upper(),self.color,attrs=["bold"])+" ❌❌❌❌❌")
        if other.ability=="Battle Bond" and "Ash" not in other.name and other.dmax==False:
            print(f" {other.name}'s {other.ability}.")
            if "Ash" not in other.name and "Greninja" in other.name:
                other.name="Ash Greninja"
                print(f" {other.name} synced with its tr's bond and transformed!")
                per=other.hp/other.maxhp
                self.weight=88.18
                self.color="blue"
                other.hp=72
                other.atk=145
                other.defense=67
                other.spatk=153
                other.spdef=71
                other.speed=132
                other.calcst()
                other.hp=other.maxhp*per
            if "Greninja" not in other.name:
                atkchange(other,self,0.5)
                spatkchange(other,self,0.5)
                speedchange(other,self,0.5)
        if other.ability=="Beast Boost":
            print(f" 👾 {other.name}'s {other.ability}!")
            m=[a,b,c,d,e]=[other.atk,other.defense,other.spatk,other.spdef,other.speed]
            if optr.reflect==True:
                m=[other.atk,other.defense/2,other.spatk,other.spdef,other.speed]
            if optr.lightscreen==True:
                m=[other.atk,other.defense,other.spatk,other.spdef/2,other.speed]
            x=max(m)
            if x==a:
            	atkchange(other,self,0.5)
           
            elif x==b:
            	defchange(other,self,0.5)
            	
            elif x==c:
        	    spatkchange(other,self,0.5)
        	    
            elif x==d:
        	    spdefchange(other,self,0.5)
        	  
            elif x==e:
            	speedchange(other,self,0.5)
       
        if other.ability=="Soul-Heart":
            print(colored(f" 💗 {other.name}'s {other.ability}!!","magenta"))
            spatkchange(other,self,0.5)
        
        if self.ability =="Aftermath":
            print(colored(f" 🕜 {self.name}'s {self.ability}!!","magenta"))
            other.hp-=other.maxhp/4
        if other.ability=="Moxie":
            print(colored(f" ⏫ {other.name}'s {other.ability}!!","red"))
            atkchange(other,self,0.5)
            
        if other.ability=="As One" and "Ice Rider" in other.name:
            print(colored(f" 🏇 {other.name}'s {other.ability}!!","cyan"))
          
            atkchange(other,self,0.5)       
        if other.ability=="As One" and "Shadow Rider" in other.name:
            print(colored(f" 🏇 {other.name}'s {other.ability}!!","magenta"))
            
            spatkchange(other,self,0.5)        
        if other.ability=="Chilling Neigh" :
            print(colored(f" 🥶 {other.name}'s {other.ability}!!","cyan"))
            
            atkchange(other,self,0.5)    
        if other.ability=="Grim Neigh" :
            print(colored(f" 😱 {other.name}'s {other.ability}!!","magenta"))
            
            spatkchange(other,self,0.5)                
        if self in tr.pokemons:
            self.status="Fainted"
            self.hp=0
            tr.faintedmon.append(self)
            tr.pokemons.remove(self)
        if len(tr.pokemons)!=0:
            self=switch(self,other,tr,optr,field,turn)
            if self.hp<=0:
                faint(self,other,tr,optr,field,turn)
        print("===================================================================================")                
        return self
def fchoice(pk,ck,tr,field):
    if tr.ai is False:
        movelist(pk,ck,field)
        choice=input(f" {tr.name}: Choose a move.\n >>")
        if choice in ["1","2","3","4","5","6"]:
            choice=int(choice)
            if ("Choice" in pk.item or pk.ability in ["Gorilla Tactics","Sage Power"]) and pk.choiced==False and pk.choicedmove=="None":
                pk.choiced=True
                pk.choicedmove=pk.moves[choice-1]
                return choice
        elif len(pk.moves)==1:
            choice=1
        elif choice not in [1,2,3,4,5,6]:
            if pk.dmax is False:
                #print(" ⚠️Move is being randomized")
                choice=random.randint(1,len(pk.moves))
            elif pk.dmax is True:
                choice=random.randint(1,len(pk.maxmove))
        if choice=="":
            choice=random.randint(1,len(pk.moves))
        return choice
def switch(self,other,trainer,trainer2,field,turn):
    if self.ability in ["Protean","Libero"]:
        if "Kecleon" in self.name:
            self.type1,self.type2="Normal","Ghost"
        if "Meowscarada" in self.name:
            self.type1,self.type2="Grass","Dark"
        if "Greninja" in self.name:
            self.type1,self.type2="Water","Dark"
    if "Disguise" in self.ability:
        self.ability="Disguise"
    if "Quark Drive" in self.ability:
        self.ability="Quark Drive"
    if "Protosynthesis" in self.ability:
        self.ability="Protosynthesis"
    if trainer.ai is not True:
        showmon(trainer)
    if "Ditto" in self.name:
        self.ability="Imposter"
        self.name="Ditto"
    resetboost(self,other)
    self.yawn=False
    self.aring=False
    if trainer.sub!="None" and "Shed Tail" not in self.moves:
        trainer.sub="None"
    self.accuracy=100
    self.evasion=100
    self.atk=self.maxatk
    self.speed=self.maxspeed
    self.spatk=self.maxspatk
    self.spdef=self.maxspdef
    self.defense=self.maxdef
    self.toxicCounter=1
    self.perishturn=0
    self.priority=self.recharge=self.seeded=self.flinched=self.protect=other.protect=self.shelltrap=self.choiced=self.dbond=self.salty=self.flashfire=self.taunted=self.confused=self.encore=self.cursed=False
    self.canfakeout=True 
    self.choicedmove="None"    
    if self.dmax is True:
        self.dmax=False
        nn=-1
        prdx=["Great Tusk","Sandy Shocks","Roaring Moon","Brute Bonnet","Slither Wing","Flutter Mane","Scream Tail","Iron","Unbound","Tapu","Black","White","Attack","Defense","Speed","Hero","Alolan","Hisuian","Galarian","Dusk Mane","Dawn Wing","Black","White","Ice Rider","Shadow Rider","Tapu","Wake"]
        di=["Single","Rapid"]
        for i in di:
            if i in self.name:
                nn=3
        for i in prdx:
            if i in self.name:
                nn=-2
        if nn==3:
            self.name=self.name[11:]    
        if nn==-1:
            self.name=self.name.split(" ")[-1]
        if nn==-2:
            self.name=name[8:]
        self.hp/=2
        self.maxhp/=2
        print(f" 🔻 {self.name} returned to it's normal state!")
    m="None"
    switchable=[1,2,3,4,5,6]
#    if self in trainer.pokemons:
#        m=trainer.pokemons.index(self,other)
#        swe=[0,1,2,3,4,5]
#        swe.remove(m)
    if trainer.ai is not True:        
        n=(input(f" {trainer.name} Choose a Pokemon: "))
        if n=="info":
            n=(input(" Which pokemon you wanna see?"))
            if n in ["1","2","3","4","5","6"]:
                n=int(n)
                trainer.pokemons[n-1].info()
                movelist(trainer.pokemons[n-1],other,field)
                return switch(self,other,trainer,trainer2,field)
            else:
                return switch(self,other,trainer,trainer2,field)
        if n not in ["1","2","3","4","5","6"] and len(trainer.pokemons)>0:
            n=random.randint(1,len(trainer.pokemons))
        if n not in switchable and len(trainer.pokemons)>0 and trainer.ai==True:
            while n!=m:
                n=random.randint(1,len(trainer.pokemons))
        if n in ["1","2","3","4","5","6"]:
            n=int(n)
    
    if trainer.ai is True:
        #print("  Not Working")
        new=switchAI(self,other,trainer,trainer2,field)[0]
    if trainer.ai is False:  
        #print("  Working")
        new=trainer.pokemons[n-1]   
    if new==self:
   	    print(f" {self.name} is already in battle.")
   	    return switch(self,other,trainer,trainer2,field,turn)		
    if new!=self:
        withdaweff(self,trainer,other)
        pkreturn(trainer,self)
        self=new
        if self.ability=="Illusion":
            self.name=trainer.pokemons[len(trainer.pokemons)-1].name.split(" ")[-1]
        spquote(trainer,self)
        entryeff(self,other,trainer,trainer2,field,turn)
        return self
    else:
        return self

#WITHDRAW EFFECTS
def withdaweff(self,trainer,other):
    if self.ability=="Zero to Hero" and "Hero" not in self.name and self.hp>0 and self.dmax==False:
        print(f" 🐬 {self.name} underwent a heroic transformation!")
        self.name="Hero Palafin"
        per=self.hp/self.maxhp
        self.color="blue"
        self.weight=214.73
        self.hp=100
        self.atk=160
        self.defense=97
        self.spatk=106
        self.spdef=87
        self.speed=100
        self.calcst()
        self.hp=self.maxhp*per
    if self.ability=="Illusion":
        self.name=trainer.pokemons[len(trainer.pokemons)-1].name.split(" ")[-1]        
    if self.ability=="Natural Cure" and (self.status!="Alive" and self.status!="Fainted"):
        print(f" {self.name}'s {self.ability}.")
        self.status="Alive"
    if self.ability=="Regenerator" and 0<self.hp<self.maxhp and self.status!="Fainted":
        print(f" {self.name}'s {self.ability}.")
        if self.hp<=(self.maxhp/3):
            self.hp+=round(self.maxhp/3)
        elif self.hp>(self.maxhp/3):
            self.hp=self.maxhp
#Stance Change        
def stancechange(self,other,turn,field,used):    
    if used not in typemoves.statusmove and self.ability=="Stance Change" and self.sword!=True:
        self.shield=False
        self.sword=True
        print(f" {self.name}'s {self.ability}!")
        print(" 🗡️ Aegislash changed to it's blade forme.")
        self.name="Blade Aegislash"
        per=self.hp/self.maxhp
        self.weight=116.84
        self.hp=60
        self.atk=140
        self.defense=50
        self.spatk=140
        self.spdef=50
        self.speed=60
        self.calcst()
        self.hp=self.maxhp*per
    if used in typemoves.statusmove and self.ability=="Stance Change" and self.shield!=True:
        self.shield=True
        self.sword=False
        print(f" {self.name}'s {self.ability}!")
        print(" 🛡️ Aegislash changed to it's shield forme.")
        self.name="Shield Aegislash"
        per=self.hp/self.maxhp
        self.hp=60
        self.atk=50
        self.defense=140
        self.spatk=50
        self.spdef=140
        self.speed=60
        self.calcst()
        self.hp=self.maxhp*per
    #prebuff(self,other,self.owner,turn,field)
 #PREATTACK       
def preattackcheck(self,other,tr,optr,use,opuse,field,turn):
    if self.yawn is not True and self.yawn=="Sleep" and self.status=="Alive" and field.terrain!="Electric":
        self.status="Sleep"
        print(f" {self.name} fell asleep!")
        self.sleependturn=turn+random.randint(2,5)
        self.yawn=False
    if self.yawn is True:
        self.yawn="Sleep"
    if self.status!="Alive" and self.ability in ["Purifying Salt","Good as Gold"]:
        print(f" {self.name}'s {self.ability}!")
        self.status="Alive"    
    if field.terrain=="Electric":
        if self.ability not in ["Levitate"] and self.type1!="Flying" and self.type2!="Flying" and self.status=="Sleep":
            print(" Electric Terrain cured its sleep!")
            self.status="Alive"
    if field.terrain=="Misty":
        if self.ability not in ["Levitate"] and self.type1!="Flying" and self.type2!="Flying":
            if self.status!="Alive":
                print(f" Misty Terrain cured its status condition!")
                self.status="Alive"
    if other.ability=="Stench" and self.ability!="Long Reach":
        ch=random.randint(1,100)  
        if ch>90:
            print(f" 🤢 {other.name}'s {other.ability}!")
            self.flinched=True   
    if self.item in ["King's Rock","Razor Fang"]:
        ch=random.randint(1,100)
        if ch>90 and other.ability not in ["Inner Focus"]:
            if use in typemoves.premove and self.precharge==False:
                pass
            if use in typemoves.premove and self.precharge==True:
                other.flinched=True
            else:
                other.flinched=True

    
def accheck(self,other,field):
    used=self.use
    accuracy=100
    eff=1
    if other.evasion<40:
        other.evasion=40
    if other.evasion>160:
        other.evasion=160
    if self.accuracy<40:
        self.accuracy=40
    if self.accuracy>160:
        self.accuracy=160
    if self.use in typemoves.acc30:
        accuracy=30
    if self.use in typemoves.acc95:
        accuracy=95
    if self.use in typemoves.acc80:
        accuracy=80
    if self.use in typemoves.acc50:
        accuracy=50
    if self.use in typemoves.acc70:
        accuracy=70
    if other.ability=="Wonder Skin" and self.use in typemoves.statusmove and self.use not in typemoves.buffmove:
        eff*=0.5  
    if field.weather in ["Sunny","Sandstorm","Desolate Land"] and self.use in ["Blizzard","Thunder","Hurricane"]:
        accuracy=50
    if field.weather in ["Rainy","Primordial Sea"] and self.use in ["Thunder","Hurricane"]:
        accuracy=100
    if field.weather in ["Hail","Snowstorm"] and self.use=="Blizzard":
        accuracy=100
    if self.use in typemoves.acc90:
        accuracy=90
    if self.item=="Zoom Lens" and self.speed<other.speed:
        eff*=1.2
    if self.item=="Wide Lens":
        eff*=1.1
    if other.item in ["Bright Powder","Lax Incense"]:
        eff*=0.9
    if other.ability=="Tangled Feet" and other.confused==True and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart"] and self.use not in typemoves.abilityigmoves:
        eff*=0.5
    if self.ability=="Hustle":
        eff*=0.8
    if other.ability not in ["Air Lock","Cloud Nine"] and self.ability not in ["Air Lock","Cloud Nine"] and field.weather=="Fog":
        eff*=0.6
    if other.ability=="Snow Cloak" and self.ability not in ["Air Lock","Cloud Nine"] and field.weather in ["Snowstorm","Hail"] and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart"] and self.use not in typemoves.abilityigmoves:
        eff*=0.75
    if other.ability=="Sand Veil" and self.ability not in ["Air Lock","Cloud Nine"] and field.weather=="Sandstorm"and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart"] and self.use not in typemoves.abilityigmoves:
        eff*=0.75
    if self.ability in ["Compound Eyes","Illuminate"]:
        eff*=1.3
    eff*=(other.evasion/100)
    eff*=(self.accuracy/100)
    accuracy=accuracy*eff
    if other.lockon==True:
        accuracy=100    
    if self.use in typemoves.noaccuracy:
        accuracy=100
    if other.use in ["Phantom Force","Shadow Force","Sky Attack","Bounce","Dig","Fly","Dive"] and other.precharge==True and used not in typemoves.buffmove and used!="None":
        accuracy=0
        if other.use in ["Bounce","Fly","Sky Attack"] and self.use=="Thunder":
            accuracy=1
            self.spatk*=2
        if "Dig" in other.use and self.use in ["Earthquake","Magnitude"]:
            accuracy=1
            self.atk*=2
    if self.ability=="No Guard" or other.ability=="No Guard":
        accuracy=100            
#    print(f" Accuracy: {int(accuracy)}")
    ch=random.randint(1, 100)
    if accuracy<100 and ch>accuracy and self.recharge==False:
        self.precharge=False
        print(f" {self.name} used {self.use}!")
        print(f" {other.name} avoided the attack!")
        used="None"
        if self.use in ["High Jump Kick","Axe Kick"]:
            a=b=c=r=al=1
            dmg=physical(self,self.level,self.atk,other.defense,130,a,b,c,r,al)
            self.hp-=dmg/2
            print(f" {self.name} was hurt by recoil!")
    return used


#########ATTACK########
def attack(self,other,tr,optr,used,opuse,field,turn):
    before=other.hp
    sbefore=self.hp
    #Substitute bypass check        
    if optr.sub!="None" and used not in typemoves.bypass:
        before=optr.sub.hp    
    #Status Catagory
    if used in typemoves.statusmove:
        self.atkcat="Status"
    hit=1
    canatk=True
    #Behind Substitute 
    subr=other
    #Checks Uncategorized Moves
    if used not in typemoves.allmove:
        print(f" ⚠️⚠️⚠️⚠️ Selected Move: {used}⚠️⚠️⚠️⚠️")
    me=self
    they=other
    #Roost typing 
    if self.roost!=False:
        if self.roost=="T1":
            self.type1="Flying"
        if self.roost=="T2":
            self.type2="Flying"
        if self.roost=="TR":
            self.teratype="Flying"
        self.roost=False
    #Parental Bond
    if self.ability!="Parental Bond[Used]":
        cl="green"
        if tr.ai==True:
            cl="red"
        print(colored("===================================================================================",cl))
        attackquote(self,tr,used)
        print(colored("===================================================================================",cl))
    #Pre-attack stuff        
    preattackcheck(self,other,tr,optr,used,opuse,field,turn)
    #Accuracy Check
    self.use=used
    used=accheck(self,other,field)
    #Checks Confusion 
    if self.confused is True:
        print(f" 😵‍💫 {self.name} is confused!")
        if turn>=self.confuseendturn or other.ability=="Oblivious":
            print(f" ‼️ {self.name} snapped out of confusion!")
            self.confused=False      
        ch=random.randint(1,100)  
        if ch>67 and self.dmax==False and self.confused==True:
            canatk=False
            used="None"
            print(f" 😵  It hurt itself in confusion.")
            r=randroll()
            self.hp-=physical(self,self.level,self.atk,self.defense,base=40,a=1,r=r)
        else:
            canatk=True
    #Checks Infatuation 
    if self.infatuated==True:
        if self.item=="Destiny Knot" and other.infatuated==False:
            other.infatuated=True
            print(f" 🥰 {other.name} is infatuated.")
        ch=random.randint(1,100)
        if ch<=25:
            canatk=False
            used="None"
            self.precharge=False
            print(f" 🥰 {self.name} is infatuated.")
            print(f" 💕 {self.name} is immobilized by love!")
        else:
            print(f" 🥰 {self.name} is infatuated.")
            canatk=True

    #Checks Paralysis
    if self.status=="Paralyzed":
        ch=random.randint(1,100)
        if ch<=25:
            canatk=False
            used="None"
            self.precharge=False
            print(f" ⚡ {self.name} is paralyzed.")
            print(colored(f" ⚡ {self.name} couldn't move because it's paralyzed!!","yellow",attrs=["bold"]))
        else:
            print(f" ⚡ {self.name} is paralyzed.")
            canatk=True

    #Checks Sleep
    if self.status=="Sleep":
        if turn>=self.sleependturn or self.ability in ["Insomnia","Vital Spirit"]:
            print(f" ‼️ {self.name} woke up!")
            self.status="Alive"
            self.yawn=False
        else:
            print(f" 💤 {self.name} is fast asleep!")
            if used=="Sleep Talk":
                print(f" {self.name} used Sleep Talk!")
                used=random.choice(self.moves)
            else:
                used="None"
                    
    #Checks Freeze                
    if other.status=="Frozen":
        if used in ["Beak Blast","Blaze Kick","Blue Flare","Burning Jealousy","Fire Blast","Fire Fang","Fire Punch","Flamethrower","Heat Wave","Ice Burn","Infernal Parade","Inferno","Lava Plume","Pyro Ball","Sacred Fire","Scorching Sands","Searing Shot","Steam Eruption","Shadow Fire","Tri Attack","Will-O-Wisp","Scald"]:       
            print(f" ‼️ {other.name} thawed out.")
            other.status="Alive"       
    if self.status=="Frozen":
        ch=random.randint(1,10)
        if ch<=2 or used in ["Beak Blast","Blaze Kick","Blue Flare","Burning Jealousy","Fire Blast","Fire Fang","Fire Punch","Flamethrower","Heat Wave","Ice Burn","Infernal Parade","Inferno","Lava Plume","Pyro Ball","Sacred Fire","Scorching Sands","Searing Shot","Steam Eruption","Shadow Fire","Tri Attack","Will-O-Wisp","Scald"]:
            print(f" ‼️ {self.name} thawed out.")
            self.status="Alive"
        else:
            print(colored(f" 🧊 {self.name} is frozen solid!","cyan",attrs=["bold"]))
            used="None"    
                
    #Checks Flinch    
    if self.flinched==True and self.dmax is False:
            self.precharge=False
            print(colored (f" 😧 {self.name} flinched and couldn't move.","white",attrs=["bold"]))
            self.flinched=False
            used="None"
    #Gigaton Hammer consecutively            
    if self.use!="None" and used=="Gigaton Hammer" and self.use=="Gigaton Hammer":
        used="None"
        print(" ❌ Cannot use Gigaton Hammer consecutively!")      
    #Multi-turned force moves        
    if self.fmove==True and self.status!="Sleep" and canatk==True:
        used=list(set(self.moves).intersection(["Outrage","Thrash","Petal Dance","Raging Fury"]))[0]
    #Recharging    
    if self.recharge==True:
        print(f" 🔋 {self.name} is recharging.")
        self.recharge=False
        used="None"      
    #Consecutive Protect        
    if self.protect=="Pending" and used in ["Protect","Spiky Shield","King's Shield","Baneful Bunker","Obstruct"]:
        print(f" 🛡️ {self.name} used {used}!")
        print("  It failed.")
        self.protect=False
        used="None"      
    #Choice Item        
    if self.choiced is True and self.dmax is False:
        if "Used" not in self.item and (self.choicedmove in self.moves and self.dmax is False) and self.status!="Sleep" and self.flinched==False and canatk is True:
            used=self.choicedmove
            self.use=used
        else:
            self.choicedmove="Struggle"
            used="Struggle"         
    #Stance Change        
    if used!="None":
        stancechange(self,other,turn,field,used)                             
########
    #Assigning the move globally
    self.use=used 
    #Substitue Bypass
    if optr.sub!="None":
        if optr.sub.hp>0:
            other=optr.sub
            if used in typemoves.bypass or self.ability=="Infiltrator":
                other=subr
            if used not in typemoves.soundmoves and used in typemoves.statusmove:   
                print(f" {self.name} used {used}!")
                print(" It failed!")
                used="None"     
    if optr.sub!="None" and (used in typemoves.statusmove and used not in typemoves.buffmove) and used not in typemoves.bypass:
        print(f" {self.name} used {used}!")
        print(" It failed!")
        used="None"
    #Me First        
    if used=="Me First" and canatk==True:
        print(f" 🙏 {self.name} used Me First!")
        if opuse!="None":
            if self.speed>other.speed:
                self.atk*=1.5
                self.spatk*=1.5
                used=opuse
            else:
                print(f" It failed!")
    #Assist                
    if used=="Assist" and canatk==True:
        print(f" 🤝 {self.name} used Assist!")
        pmoves=[]
        for i in tr.pokemons:
            if i!=self:
                pmoves+=i.moves
                used=random.choice(pmoves)        
    #Good as Gold        
    if other.ability=="Good as Gold" and used in typemoves.statusmove and used not in ["Stealth Rock","Haze","Toxic Spikes","Protect","Spiky Shield","Baneful Bunker","King's Shield","Silk Trap"]+typemoves.healingmoves+typemoves.buffmove:
        print(f" {self.name}'s used {used}.")
        print(f" 🪙 {other.name}'s {other.ability}!")
        used="None"    
    #Wish Heal              
    if optr.wishhp is not False and other.speed<self.speed:
        print(f" 🌠 {other.name}'s wish came true!")
        other.hp+=optr.wishhp
        if other.hp>other.maxhp:
            other.hp=other.maxhp
        optr.wishhp=False
    if tr.wishhp is not False:
        print(f" 🌠 {self.name}'s wish came true!")
        self.hp+=tr.wishhp
        if self.hp>self.maxhp:
            self.hp=self.maxhp
        tr.wishhp=False
    #Comatose
    if self.status=="Comatose":
        self.status="Drowsy"
    #Prankster immune        
    if self.ability=="Prankster" and "Dark" in (other.type1,other.type2,other.teratype) and used in typemoves.statusmove:
        used="None"
        print(f" {other.name} is immune to {self.name}'s Prankster!")
    #Encore   
    if self.encore is not False and self.dmax is False:
        if turn==self.enendturn:    
            self.encore=False
        elif self.encore in self.moves:
            used=self.encore
        else:
            used="Struggle"
    #Safety Googles            
    if used in typemoves.powdermoves and other.item=="Safety Googles":
        print(f" 👓 {other.name}'s Safety Googles protected it from {self.name}'s {used}!")
        used="None"            
    #Soundproof            
    if used in typemoves.soundmoves and other.ability=="Soundproof":
        print(f" 🔇 {other.name}'s {other.ability}!")
        used="None"
    #Bulletproof        
    if used in typemoves.bulletmove and other.ability=="Bulletproof":
        print(f" 🪖 {other.name}'s {other.ability}!")
        used="None"
    #Fluffy        
    if used in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads"]:
        if other.ability=="Fluffy":
            self.atk/=2
    #Hit count            
    if used not in typemoves.statusmove:
        other.atkby=self.name
        other.atktime+=1
    #Diguise        
    if other.ability=="Disguise" and other.abilityused==False and used not in typemoves.statusmove+typemoves.buffmove+typemoves.zmoves+typemoves.multimove+typemoves.abilityigmoves and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart"]:
        print(f" {self.name} used {used}!")
        print(f" 🥸 {other.name}'s {other.ability}!")     
        print(f" {other.name}'s disguise was busted!")
        other.hp-=round(other.maxhp/8)
        used="None"
        other.ability="Disguise[Used]"
    #Destiny Bond Reset        
    if used!="Destiny Bond" and "Destiny Bond" in self.moves:
        other.dbond=False
    #Protect while buffmoves/misses
    if (opuse in typemoves.buffmove or opuse=="None") and used in typemoves.protectmoves:
        print(f" {self.name} used {used}!")
        used="None"
        print(" It failed!")
    #Move assigning (not sure)        
    if self.dmax is False:
        moves=self.moves
    if self.dmax is True:
        moves=self.maxmove
    #PP defining        
    pp=1
    if other.ability=="Pressure":
        pp=2
    #Struggle        
    if self.dmax is False and canatk is True:
        if len(self.moves)==0 and self.status not in ("Sleep"):
            used="Struggle"
    #Metronome            
    if used=="Metronome":
        print(f" 🎲 {self.name} used Metronome!")
        x=set(allmove)-set(typemoves.zmoves)-set(typemoves.maxmovelist)
        x=list(x)
        used=random.choice(x)
        print(f" Metronome turned into {used}!")
    #Precharge move Selection        
    if self.precharge==True and len(self.moves)>0 and "Geomancy" not in self.moves and self.status not in ["Sleep","Frozen"] and canatk==True:
        l=list(set(self.moves).intersection(typemoves.premove))
        if len(l)!=0:
            used=l[0]
    #Priority blocker            
    if (field.terrain=="Psychic" or other.ability in ["Dazzling","Queenly Majesty","Armor Tail"]) and used in typemoves.prioritymove and self.dmax is False:
        if field.terrain!="Psychic":
            print(f" {other.name}'s {other.ability}.")
        used="None"
        print("  🚳 Cannot use priority moves!")
    #Truant
    if self.ability=="Truant" and used!="Slack Off":
        if self.truant==True:
            print(f" {self.name}'s Truant!")
            print(f" {self.name} is loafing around!")
            used="None"
            self.truant=False
        else:
            self.truant=True
    if self.ability=="Truant" and used=="Slack Off":
        self.truant=False

    if used in moves or used not in moves:
        #TAUNTED
        if self.taunted==True and used in typemoves.statusmove:
            if self.item=="Mental Herb":
                self.taunted=False
                self.item+="[Used]"
            else:
                print(colored(f" 🎭 {self.name} can't use {used} after the taunt.","white",attrs=["bold"]))
                used="None"
        #Assault Vest                
        if self.item=="Assault Vest" and used in typemoves.statusmove:
            print(f" 🦺 Cannot use status moves while holding an Assault Vest.")
            used="None"
       #Protect Reset     
        if used not in ["Protect","Spiky Shield","King's Shield","Baneful Bunker","Obstruct","Silk Trap","Mad Guard"]:
            self.protect=False
        #Geomancy
        if self.precharge==True and "Geomancy" in self.moves:
            print(f" 🌈 {self.name} used "+colored(" Geomancy","magenta")+"!")
            spatkchange(self,other,1)     
            spdefchange(self,other,1)   
            speedchange(self,other,1)        
            self.precharge=False
            used="None"
        #Max Guard
        if other.protect==True and (other.dmax is True and used not in typemoves.buffmove and used not in ["G-Max One Blow","G-Max Rapid Flow"] and used!="None"):
            print(f" 🛡️ {other.name} protected itself from {self.name}'s {used}.")
            self.fmoveturn=0
            other.protect="Pending"
            if used in typemoves.zmoves:
                self.name=self.name.split("(")[0]
                self.item+="[Used]"
                self.moves.remove(used)
            used="None"
            if used in ["Protect","Spiky Shield","King's Shield","Baneful Bunker"]:
                print(f" 🛡️ {self.name} used {used}!")
                used="None"
        #Protection Moves                
        if other.dmax is False and other.protect==True and used not in typemoves.buffmove and (self.ability not in ["Infiltrator","Unseen Fist"]  and used not in ["Shadow Force","Phantom Force","Hyperspace Fury","Hyper Drill","Hyperspace Hole"] and used not in typemoves.maxmovelist and used not in typemoves.zmoves) and used!="None" :
            print(f" 🛡️ {other.name} protected itself from {self.name}'s {used}.")
            self.fmoveturn=0
            other.protect="Pending"
            if used in ["Protect","Spiky Shield","King's Shield","Baneful Bunker","Max Guard"]:
                print(f" 🛡️ {self.name} used {used}!")
                print("  It failed!")
                used="None"
                self.protect=False            
            if "Spiky Shield" in other.use and used in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads"]:
                self.hp-=round(self.maxhp/8)
                print(f" {self.name} was hurt by Spiky Shield.") 
            if "Silk Trap" in other.use and used in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads"]:
                speedchange(self,other,-0.5)
             
            if "Obstruct" in other.use and used in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads"]:
                spatkchange(self,other,-0.5)
            
            if "King's Shield" in other.use and used in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads"]:
                atkchange(self,other,-0.5)
           
            if "Baneful Bunker" in other.use and used in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads"]:
                if self.status=="Alive":
                    self.status="Badly Poisoned"
                    print(f" ☠️ {self.name} was badly poisoned.")  
        #Start of actual moves                    
        elif used=="Toxic":
            toxic(self,other)
        elif used=="Thunder Wave":
            thunderwave(self,other)
        elif used=="Sucker Punch":
            if opuse in nondmgmove or opuse =="None":
                print(f" 👿 {self.name} used "+colored(" Sucker Punch","white",attrs=["bold"])+"!")
                print("  It failed.")
            else:
                suckerpunch(self,other)
        elif used=="Will-O-Wisp":
            willowisp(self,other)        
        elif used=="Overdrive":
            overdrive(self,other) 
        elif used=="Kowtow Cleave":
            kowtowcleave(self,other) 
        elif used=="Ice Spinner":
            icespinner(self,other) 
        elif used=="Jaw Lock":
            jawlock(self,other)  
        elif used=="Torch Song":
            torchsong(self,other)      
        elif used=="Psystrike":
            psystrike(self,other)
        elif used=="Shadow Punch":
            shadowpunch (self,other)
        elif used=="Smart Strike":
            smartstrike(self,other)
        elif used=="Magnitude":
            magnitude(self,other)
        elif used=="Attack Order":
            attackorder(self,other)
        elif used=="Acupressure":
            acupressure(self,other)
        elif used=="Bulldoze":
            bulldoze(self,other)
        elif used=="Fishious Rend":
            fishiousrend(self,other)
        elif used=="Grav Apple":
            gravapple(self,other)
        elif used=="Mind Blown":
            mindblown(self,other)
        elif used=="Shell Side Arm":
            shellsidearm(self,other)
        elif used=="Apple Acid":
            appleacid(self,other)
        elif used=="Taunt":
            print(f" 🤌 {self.name} used "+ colored(" Taunt","white",attrs=["bold"])+"!")
            if other.taunted==True:
                print(" It failed.")
            if other.taunted==False:
                other.taunted=True
                print(f" {other.name} fell for the taunt!")
                other.taunturn=turn+random.randint(3,5)
        elif used=="Grassy Glide":
            grassyglide(self,other)
        elif used=="Snipe Shot":
            snipeshot(self,other)
        elif used=="Drum Beating":
            drumbeating(self,other)
        elif used=="Doom Desire":
            doomdesire(self,other)
        elif used=="Shadow Sneak":
            shadowsneak(self,other)
        elif used=="Max Lightning":
            maxlightning(self,other,turn)
        elif used=="Max Overgrowth":
            maxovergrowth(self,other,turn)
        elif used=="Max Mindstorm":
            maxmindstorm(self,other,field,turn)
        elif used=="Gigaton Hammer":
            gigatonhammer(self,other)
        elif used=="Max Starfall":
            maxstarfall(self,other,field, turn)
        elif used=="Max Flare":
            maxflare(self,other,field,turn)
        elif used=="Max Hailstorm":
            maxhailstorm(self,other,field,turn)
        elif used=="Max Geyser":
            maxgeyser(self,other,field,turn)
        elif used=="Max Rockfall":
            maxrockfall(self,other,field,turn)
        elif used=="Pain Split":
            painsplit(self,other)
        elif used=="Endeavor":
            endeavor(self,other)
        elif used=="Yawn":
            yawn(self,other)
        elif used=="Doodle":
            doodle(self,other)
        elif used=="Glaciate":
            glaciate(self,other)
        elif used=="Salt Cure":
            saltcure(self,other)
        elif used=="Nuzzle":
            nuzzle(self,other)
        elif used=="Searing Shot":
            searingshot (self,other)
        elif used=="V-create":
            vcreate(self,other)
        elif used=="Octolock":
            octolock(self,other)
        elif used=="Octazooka":
            octazooka(self,other)
        elif used=="Dynamax Cannon":
            dynamaxcannon(self,other)
        elif used=="Fillet Away":
            filletaway(self,other)
        elif used=="Cosmic Power":
            cosmicpower (self,other)
        elif used=="Amnesia":
            amnesia(self,other)
        elif used=="No Retreat":
            noretreat(self,other)
        elif used=="Aqua Ring":
            aquaring(self,other)
        elif used=="Charm":
            charm(self,other)
        elif used=="Triple Axel":
            tripleaxel(self,other)
        elif used=="Quick Attack":
            quickattack(self,other)
        elif used=="Blazing Torque":
            blazingtorque(self,other)
        elif used=="Combat Torque":
            combattorque(self,other)
        elif used=="Magical Torque":
            magicaltorque(self,other)
        elif used=="Noxious Torque":
            noxioustorque(self,other)
        elif used=="Wicked Torque":
            wickedtorque(self,other)
        elif used=="Ice Hammer":
            icehammer(self,other)
        elif used=="Needle Arm":
            needlearm(self,other)
        elif used=="Rising Voltage":
            risingvoltage(self,other)
        elif used=="Smelling Salts":
            smellingsalts(self,other)
        elif used=="Sonic Slash":
            sonicslash(self,other)
        elif used=="Skitter Smack":
            skittersmack(self,other)
        elif used=="Zing Zap":
            zingzap(self,other)
        elif used=="Photon Geyser":
            photongeyser(self,other)
        elif used=="Tar Shot":
            tarshot(self,other)
        elif used=="Revelation Dance":
            revelationdance(self,other)
        elif used=="Trick":
            trick(self,other)
        elif used=="Trop Kick":
            tropkick(self,other)
        elif used=="Heal Bell":
            healbell(self,tr)
        elif used=="Aromatherapy":
            aromatherapy(self,tr)
        elif used=="Wish":
            wish(self,tr)
        elif used=="Spectral Thief":
            spectralthief(self,other)
        elif used=="Soul Robbery":
            soulrobbery(self,other)
        elif used=="Dream Eater":
            dreameater(self,other)
        elif used=="Glare":
            glare(self,other)
        elif used=="Draco Barrage":
            dracobarrage (self,other)
        elif used=="Acid Spray":
            acidspray(self,other)
        elif used=="Corrosive Gas":
            corrosivegas(self,other)
        elif used=="Haze":
            haze(self,other)
        elif used=="Dark Hole":
            darkhole(self,other,turn)
        elif used=="Raging Bull":
            ragingbull (self,other)
        elif used=="Encore":
            if other.item=="Mental Herb":
                print(f" {other.name}'s {other.item} protected it from Encore.")
                self.item+="[Used]"
            else:
                encore(self,other,opuse,turn)
        elif used=="Strange Steam":
            strangesteam(self,other,turn)
        elif used=="Eerie Spell":
            print(f" {self.name} used Eerie Spell!")
            if opuse!="None":
                print(f" {other.name}'s {opuse}'s PP was deducted!")
                if self.dmax is True:
                    if other.pplist[other.maxmove.index(opuse)]<=3:
                        other.pplist[other.maxmove.index(opuse)]=0
                    else:
                        other.pplist[other.maxmove.index(opuse)]-=3
                if self.dmax is False:
                    if other.pplist[other.moves.index(opuse)]<=3:
                        other.pplist[other.moves.index(opuse)]=0
                    else:
                        other.pplist[other.moves.index(opuse)]-=3
            if opuse=="None":
                print(" It failed!")        
                
        elif used=="Eerie Impulse":
            eerieimpulse(self,other)
        elif used=="Flail":
            flail(self,other)
        elif used=="Psyblade":
            psyblade(self,other)
        elif used=="Hydro Steam":
            hydrosteam(self,other)
        elif used=="Lunar Dance":
            self.hp=0
            print(f" 🌙 {self.name} used "+colored(" Lunar Dance","magenta",attrs=["bold"])+"!")
            self=faint(self,other,tr,optr,field,turn)
            if self.hp<self.maxhp:
                print(f" {self.name}'s HP was restored and status was cured!")
            self.hp=self.maxhp
            self.status="Alive"
        elif used=="Healing Wish":
            self.hp=0
            print(f" {self.name} used "+colored(" Healing Wish","magenta",attrs=["bold"])+"!")
            self=faint(self,other,tr,optr,field,turn)
            if self.hp<self.maxhp:
                print(f" {self.name}'s HP was restored and status was cured!")
            self.hp=self.maxhp
            self.status="Alive"
        elif used=="Triple Kick":
            triplekick(self,other)
        elif used=="Icy Wind":
            icywind(self,other)
        elif used=="Present":
            present(self,other)
        elif used=="Barrier":
            barrier(self,other)
        elif used=="Avalanche":
            avalanche(self,other)
        elif used=="Psycho Shift":
            psychoshift(self,other)
        elif used=="Perish Song":
            perishsong(self,other)
        elif used=="Aerial Ace":
            aerialace(self,other)
        elif used=="Swagger":
            swagger(self,other,turn)
        elif used=="Feather Dance":
            featherdance(self,other)
        elif used=="Fake Tears":
            faketears(self,other)
        elif used=="Tri Attack":
            triattack(self,other)
        elif used=="Doom Desire":
            print(f" 💫 {self.name} used "+colored(" Doom Desire","white",attrs=["bold"])+"!")
            if optr.doom!=0:
                print(" It failed!")
            if optr.doom==0:
                optr.doom=turn+3
                print(f" 🌟 {self.name} chose Doom Desire as it's Destiny!")
                al=1
                r=randroll()
                c=1
                a=1
                b=1
                optr.ftmul=special(self,other.level,self.spatk,other.spdef,140,a,b,c,r,al)
        elif used=="Future Sight":
            print(f" {self.name} used "+colored(" Future Sight","magenta",attrs=["bold"])+"!")
            if optr.future!=0:
                print(" It failed!")
            if optr.future==0:
                optr.future=turn+3
                print(f" 🔮 {self.name} foresaw the future!")
                al=1
                r=randroll()
                c=1
                a=1
                b=1
                optr.ftmul=special(self,other.level,self.spatk,other.spdef,120,a,b,c,r,al)
        elif used=="Shed Tail":
            print(f" 🦎 {self.name} used Shed Tail!")
            if self.hp<(self.maxhp/2) or tr.sub!="None":
                print(f" It failed!")
            if self.hp>(self.maxhp/2) and tr.sub=="None": 
                print(f" {self.name} created a substitute!")
                self.hp-=self.maxhp/2
                tr.sub=Pokemon2(name="Substitute",moves=["null","null","null","null"])
                tr.sub.hp=self.maxhp/2
                tr.sub.atk=self.atk
                tr.sub.defense=self.defense
                tr.sub.spdef=self.spdef
                tr.sub.spatk=self.spatk
                tr.sub.speed=self.speed   
                if len(tr.pokemons) >1:
                    print(f" {self.name} returned to it's {pkball}.")
                    self=switch(self,other,tr,optr,field,turn)
                          
        elif used=="Substitute":
            print(f" 🎎 {self.name} used "+colored(" Substitute","green")+"!")
            if self.hp<(self.maxhp/4) or tr.sub!="None":
                print(f" It failed!")
            if self.hp>(self.maxhp/4) and tr.sub=="None": 
                print(f" {self.name} created a substitute!")
                self.hp-=self.maxhp/4
                tr.sub=Pokemon2(name="Substitute",moves=["null","null","null","null"])
                tr.sub.hp=self.maxhp/4
                tr.sub.atk=self.atk
                tr.sub.defense=self.defense
                tr.sub.spdef=self.spdef
                tr.sub.spatk=self.spatk
                tr.sub.speed=self.speed
        elif used=="Lock-On":
            if other.lockon==True:
                print(f" It failed!")
            if other.lockon!=True:
                print(f" {self.name} used Lock-On!")
                print(f" 🎯 {self.name} locked its aim on {other.name}!")
                other.lockon=True
        elif used=="Recycle":
            recycle(self,other)   
        elif used=="Sweet Kiss":
            sweetkiss(self,other,turn)   
        elif used=="Flame Charge":
            flamecharge(self,other)
        elif used=="Trailblaze":
            trailblaze(self,other) 
        elif used=="Minimize":
            print(f" ◽▫️{self.name} used "+colored(" Minimize","white",attrs=["bold"])+"!")
            if self.evasion>40:
                print(f" 🔼 {self.name}'s evasion sharply rose!")
                self.evasion-=20
        elif used=="Sand-Attack":
            print(f" 😖 {self.name} used "+colored(" Sand-Attack","yellow",attrs=["bold"])+"!")
            if other.accuracy>40:
                print(f" 🔽 {other.name}'s accuracy fell!")
                other.accuracy-=10
        elif used=="Smokescreen":
            print(f" 💣 {self.name} used "+colored(" Smokescreen","white",attrs=["bold"])+"!")
            if other.accuracy>40:
                print(f" 🔽 {other.name}'s accuracy fell!")
                other.accuracy-=10
        elif used=="Double Team":
            print(f" 🥷 {self.name} used "+colored(" Double Team","white",attrs=["bold"])+"!")
            if self.evasion>40:
                print(f" 🔼 {self.name}'s evasion rose!")
                self.evasion-=10            
        elif used=="Focus Punch":
            focuspunch(self,other)
        elif used=="Pollen Puff":
            pollenpuff(self,other)
        elif used=="Dive":
            dive(self,other)
        elif used=="Fly":
            fly(self,other)
        elif used=="Dig":
            dig(self,other)
        elif used=="Growth":
            growth(self,other)
        elif used=="Power Trip":
            powertrip(self,other)
        elif used=="Skill Swap":
            skillswap(self,other)
        elif used=="Feint":
            feint(self,other)
        elif used=="Aurora Beam":
            aurorabeam(self,other)
        elif used=="Aqua Fang":
            aquafang(self,other)
        elif used=="Poltergeist":
            poltergeist(self,other)
        elif used=="Scary Face":
            scaryface(self,other)
        elif used=="Metal Sound":
            metalsound(self,other)
        elif used=="Tickle":
            tickle(self,other)
        elif used=="Confuse Ray":
            confuseray(self,other,turn)
        elif used=="Payback":
            payback(self,other)
        elif used=="Reversal":
            reversal(self,other)
        elif used=="Stun Spore":
            stunspore(self,other)
        elif used=="G-Max Tartness":
            gmaxtartness(self,other)
        elif used=="G-Max Sweetness":
            gmaxsweetness(self,other)
        elif used=="G-Max Cuddle":
            gmaxcuddle(self,other)
        elif used=="G-Max Gold Rush":
            gmaxgoldrush(self,other,turn)
        elif used=="G-Max Malodor":
            gmaxmalodor(self,other)
        elif used=="G-Max Meltdown":
            gmaxmeltdown(self,other)        
        elif used=="Lunar Blessing":
            lunarblessing(self,other)
            if self.status!="Alive":
                self.status="Alive"
                print(f" {self.name}'s status was cured.")
        elif used=="Take Heart":
            takeheart(self,other)
            if self.status!="Alive":
                self.status="Alive"
                print(f" {self.name}''s status was cured.")
        elif used=="G-Max Snooze":
            gmaxsnooze(self,other)
        elif used=="G-Max Wind Rage":
            gmaxwindrage(self,other,optr)
        elif used=="G-Max Vine Lash":
            gmaxvinelash(self,other,turn)
        elif used=="G-Max Smite":
            gmaxsmite(self,other,turn)
        elif used=="Rage Fist":
            ragefist(self,other)
        elif used=="Petal Blizzard":
            petalblizzard(self,other)
        elif used=="Double Shock":
            doubleshock(self,other)
        elif used=="G-Max Steelsurge":
            gmaxsteelsurge(self,other,optr)
        elif used=="Max Wyrmwind":
            maxwyrmwind(self,other)
        elif used=="G-Max Fireball":
            gmaxfireball(self,other)
        elif used=="G-Max Hydrosnipe":
            gmaxhydrosnipe(self,other)
        elif used=="G-Max One Blow":
            gmaxoneblow(self,other)
        elif used=="G-Max Rapid Flow":
            gmaxrapidflow(self,other)
        elif used=="Collision Course":
            collisioncourse(self,other)
        elif used=="Flower Trick":
            flowertrick(self,other)
        elif used=="Aqua Step":
            aquastep(self,other)
        elif used=="Struggle":
            struggle(self,other)
        elif used=="Last Respects":
            lastrespects(self,other,tr)
        elif used=="Chilling Water":
            chillingwater(self,other)
        elif used=="G-Max Terror":
            gmaxterror(self,other)
        elif used=="G-Max Volcalith":
            gmaxvolcalith(self,other,turn,optr)
        elif used=="G-Max Volt Crash":
            gmaxvoltcrash(self,other)
        elif used=="G-Max Stun Shock":
            gmaxstunshock(self,other)
        elif used=="G-Max Finale":
            gmaxfinale(self,other)
        elif used=="Max Flutterby":
            maxflutterby(self,other)
        elif used=="G-Max Befuddle":
            gmaxbefuddle(self,other)
        elif used=="Draining Kiss":
            drainingkiss(self,other)
        elif used=="Max Phantasm":
            maxphantasm(self,other)
        elif used=="G-Max Cannonade":
            gmaxcannonade(self,other,turn)
        elif used=="G-Max Chi Strike":
            gmaxchistrike(self,other)
        elif used=="Cotton Guard":
            cottonguard(self,other)
        elif used=="Spicy Extract":
            spicyextract(self,other)
        elif used=="Spin Out":
            spinout(self,other)
        elif used=="Clanging Scales":
            clangscale(self,other)
        elif used=="Clangorous Soul":
            clangsoul(self,other)
        elif used=="G-Max Foam Burst":
            gmaxfoamburst(self,other)
        elif used=="G-Max Centiferno":
            gmaxcentiferno(self,other)
        elif used=="G-Max Depletion":
            gmaxdepletion(self,other)
        elif used=="G-Max Drum Solo":
            gmaxdrumsolo(self,other)
        elif used=="G-Max Replenish":
            gmaxreplenish(self,other)
        elif used=="G-Max Wildfire":
            gmaxwildfire(self,other,turn)
        elif used=="Behemoth Bash":
            behemothbash(self,other)
        elif used=="Clangorous Scales":
            clangscale(self,other)
        elif used=="Parabolic Charge":
            parabolic(self,other)
        elif used=="Behemoth Blade":
            behemothblade(self,other)
        elif used=="Max Knuckle":
            maxknuckle(self,other)
        elif used=="Max Quake":
            maxquake(self,other)
        elif used=="Max Steelspike":
            maxsteelspike (self,other)
        elif used=="Max Darkness":
            maxdarkness(self,other)
        elif used=="Hyper Drill":
            hyperdrill(self,other)
        elif used=="Max Ooze":
            maxooze(self,other)
        elif used=="Max Strike":
            maxstrike(self,other)
        elif used=="Max Airstream":
            maxairstream(self,other)
        elif used=="Psyshock":
            psyshock(self,other)
        elif used=="Lumina Crash":
            luminacrash(self,other)
        elif used=="Mortal Spin":
            mortalspin(self,other,tr)
        elif used=="Accelerock":
            accelerock(self,other)
        elif used=="Geomancy":
            geomancy(self,other)
        elif used=="Heavy Slam":
            heavyslam(self,other)
        elif used=="Heart Swap":
            heartswap(self,other)
        elif used=="Dragon Energy":
            dragonenergy(self,other)
        elif used=="Court Change":
            print(f" {self.name} used Court Change!")
            tr.hazard,optr.hazard=optr.hazard,tr.hazard
        elif used=="Land's Wrath":
            landswrath(self,other)
        elif used=="Thousand Arrows":
            thousandarrows(self,other)
        elif used=="Thousand Waves":
            thousandwaves(self,other)
        elif used=="Steel Beam":
            steelbeam(self,other)
        elif used=="Shadow Claw":
            shadowclaw(self,other)
        elif used=="Shelter":
            shelter(self,other)
        elif used=="Crush Grip":
            crushgrip(self,other)
        elif used=="Night Daze":
            nightdaze(self,other)
        elif used=="Crabhammer":
            crabhammer(self,other)
        elif used=="Mystical Fire":
            mysticalfire(self,other)
        elif used=="Bitter Malice":
            bittermalice(self,other)
        elif used=="Rain Dance":
            raindance(self,other,field,turn)
            if other.ability=="Dancer":
                print(f" {other.name}'s {other.ability}!")
                raindance(other,self,field,turn)
        elif used=="Sunny Day":
            sunnyday(self,other,field,turn)
        elif used=="Leech Seed":
            leechseed(self,other)
        elif used=="Trick Room":
            trickroomm(self, other,turn)
        elif used=="Sandstorm":
            sandstorm(self,other,field,turn)
        elif used=="Shore Up":
            shoreup(self,other)
        elif used=="Electric Terrain":
            electricterrain(self,other,field,turn)
        elif used=="Misty Terrain":
            mistyterrain(self,other,field,turn)
        elif used=="Grassy Terrain":
            grassyterrain(self,other,field,turn)
        elif used=="Psychic Terrain":
            psychicterrain(self,other,field,turn)
        elif used=="Synthesis":
            synthesis(self,other)
        elif used=="Snowscape":
            snowscape(self,other,field,turn)
        elif used=="Hail":
            hail(self,other,field,turn)
        elif used=="Quiver Dance":
            quiverdance(self,other)
            if other.ability=="Dancer":
                print(f" {other.name}'s {other.ability}!")
                quiverdance(other)
        elif used=="Defend Order":
            defendorder(self,other)
        elif used=="Swords Dance":
            swordsdance(self,other)
            if other.ability=="Dancer":
                print(f" {other.name}'s {other.ability}!")
                swordsdance(other,self)
        elif used=="Nasty Plot":
            nastyplot(self,other)
        elif used=="Shell Smash":
            shellsmash(self,other)
        elif used=="Autotomize":
            autotomize(self,other)
        elif used=="Tidy Up":
            tidyup(self,other,tr)
        elif used=="Rapid Spin":
            rapidspin(self,other,tr)
        elif used=="Dragon Dance":
            dragondance(self,other)
            if other.ability=="Dancer":
                print(f" {other.name}'s {other.ability}!")
                dragondance(other)
        elif used=="Iron Defense":
            irondefense(self,other)
        elif used=="Bullet Punch":
            bulletpunch(self,other)
        elif used=="Flying Press":
            flyingpress(self,other)
        elif used=="X-Scissor":
            xscissor(self,other)
        elif used=="Drill Peck":
            drillpeck(self,other)
        elif used=="Triple Arrows":
            hitx=0
            while True:
                hitx+=1
                triplearrows(self,other)
                if hitx==3 or other.hp<=0:
                    break
            print(f" It hit {hitx} time(s).")     
        elif used=="Boomburst":
            boomburst(self,other)
        elif used=="Muddy Water":
            muddywater(self,other)
        elif used=="Hyperspace Fury":
            hyperspacefury(self,other)
        elif used=="Knock Off":
            knockoff(self,other)
        elif used=="Volt Tackle":
            volttackle(self,other)
        elif used=="Chloroblast":
            chloroblast(self,other)
        elif used=="Beak Blast":
            beakblast(self,other)
        elif used=="Facade":
            facade(self,other)
        elif used=="Soak":
            soak(self,other)
        elif used=="Defog":
            print(f" {self.name} used Defog.")
            print(" All the hazards blew away!")
            other.evasion=100
            tr.hazard=[]
            optr.hazard=[]
            field.terrain="Normal"
            optr.lightscreen=False
            optr.reflect=False
            if field.terrain!="Normal":
                field.terrain="Normal"
        elif used=="Trick-or-Treat":
            trickortreat(self,other)
        elif used=="Forest's Curse":
            forestscurse(self,other)
        elif used=="Moongeist Beam":
            moongeistbeam(self,other)
        elif used=="Sunsteel Strike":
            sunsteelstrike(self,other)
        elif used=="Stored Power":
            storedpower(self,other)
        elif used=="Luster Purge":
            lusterpurge(self,other)
        elif used=="Hammer Arm":
            hammerarm(self,other)
        elif used=="Final Gambit":
            finalgambit(self,other)
        elif used=="Bolt Beak":
            boltbeak(self,other)
        elif used=="Expanding Force":
            expandingforce(self,other)
        elif used=="Oblivion Wing":
            oblivionwing(self,other)
        elif used=="Aura Sphere":
           aurasphere(self,other)
        elif used=="Aura Wheel":
           aurawheel(self,other)
        elif used=="Meteor Mash":
           meteormash(self,other)
        elif used=="Venoshock":
             venoshock(self,other)
        elif used=="Infernal Parade":
             infernalparade(self,other)
        elif used=="Raging Fury":
             ragingfury(self,other)
        elif used=="Heat Crash":
             heatcrash(self,other)
        elif used=="Spirit Shackle":
             spiritshackle(self,other)
        elif used=="Throat Chop":
             throatchop(self,other)
        elif used=="Steam Eruption":
            steameruption(self,other)
        elif used=="Diamond Storm":
            diamondstorm(self,other)
        elif used=="Light of Ruin":
            lightofruin(self,other)
        elif used=="Hyper Voice":
             hypervoice(self,other)
        elif used=="Prismatic Laser":
             prismaticlaser(self,other)
             self.recharge=True
        elif used=="Sparkling Aria":
             sparklingaria(self,other)
        elif used=="Glaive Rush":
             glaiverush(self,other)
        elif used=="Glacial Lance":
             glaciallance(self,other)
        elif used=="Astral Barrage":
             astralbarrage(self,other)
        elif used=="Darkest Lariat":
             darkestlariat(self,other)
        elif used=="Ceaseless Edge":
             ceaseless(self,other,optr)
        elif used=="Mist Ball":
            mistball(self,other)
        elif used=="Aqua Cutter":
            aquacutter(self,other)
        elif used=="False Surrender":
            falsesurrender(self,other)
        elif used=="Ruination":
            ruination(self,other)
        elif used=="Electro Drift":
            electrodrift(self,other)
        elif used=="Spirit Break":
            spiritbreak(self,other)
        elif used=="Breaking Swipe":
            breakingswipe(self,other)
        elif used=="Thunder Fang":
            tfang(self,other)
        elif used=="Stomping Tantrum":
            stompingtantrum(self,other)
        elif used=="Razor Shell":
            razorshell(self,other)
        elif used=="Headlong Rush":
            headlongrush(self,other)
        elif used=="Seed Bomb":
            seedbomb(self,other)
        elif used=="Fire Fang":
            firefang(self,other)
        elif used=="Fire Lash":
            firelash(self,other)
        elif used=="Armor Cannon":
            armorcannon(self,other)
        elif used=="Bitter Blade":
            bitterblade(self,other)
        elif used=="Milk Drink":
            milkdrink(self,other)
        elif used=="Fiery Dance":
            fierydance(self,other)
            if other.ability=="Dancer":
                print(f" {other.name}'s {other.ability}!")
                fierydance(other)
        elif used=="Leech Life":
            leechlife(self,other)
        elif used=="Freezing Glare":
            freezingglare(self,other)
        elif used=="Skull Bash":
            skullbash(self,other)
        elif used=="Horn Leech":
            hornleech(self,other)
        elif used=="Flip Turn":
            flipturn(self,other)
            if len(tr.pokemons)>1 and (other.hp!=before) and other.ability not in ["Water Absorb","Storm Drain","Water Compaction","Desolate Land","Dry Skin"]:
                print(f" {self.name} returned to it's {pkball}.")
                self=switch(self,other,tr,optr,field,turn)
        elif used=="Chilly Reception":
            chillyreception(self,other,field,turn)
            if len(tr.pokemons)>1:
                print(f" {self.name} returned to it's {pkball}.")
                self=switch(self,other,tr,optr,field,turn)                        
        elif used=="U-turn":
            uturn(self,other)
            if len(tr.pokemons)>1:
                print(f" {self.name} returned to it's {pkball}.")
                self=switch(self,other,tr,optr,field,turn)
        elif used=="Parting Shot":
            partingshot(self,other)
            if len(tr.pokemons)>1:
                print(f" {self.name} returned to it's {pkball}.")
                self=switch(self,other,tr,optr,field,turn)                
        elif used=="Teleport":
            print(f" 🔄 {self.name} used "+colored(" Teleport","magenta",attrs=["bold"])+"!")
            if len(tr.pokemons)==1:
                print(" It failed!")
            if len(tr.pokemons)>1:
                print(f" {self.name} returned to it's {pkball}.")
                self=switch(self,other,tr,optr,field,turn)                
        elif used=="Volt Switch":
            voltswitch(self,other)
            if len(tr.pokemons)>1 and (other.hp!=before) and other.ability not in ["Volt Absorb","Lightning Rod","Motor Drive"] and "Ground" not in (other.type1,other.type2,other.teratype):
                print(f" {self.name} returned to it's {pkball}.")
                self=switch(self,other,tr,optr,field,turn)
        elif used=="Extreme Speed":
            extemespeed(self,other)
        elif used=="Inferno":
            inferno(self,other)
        elif used=="Fleur Cannon":
            fleurcannon(self,other)                
        elif used=="Overheat":
            overheat(self,other)
        elif used=="Roar":
            print(f" 🐯 {self.name} used "+colored(" Roar","white",attrs=["bold"])+"!")
            if len(optr.pokemons)>1 and other.ability!="Suction Cups" and other.dmax is False:
                resetboost(other,self)
                l=other
                while True:
                    other=random.choice(optr.pokemons)
                    if other!=l:
                        break
                print(f" {other.name} was dragged out!")
                entryeff(other,self,optr,tr,field,turn)
        elif used=="Whirlwind":
            print(f" 🌪️ {self.name} used "+colored(" Whirlwind","white",attrs=["bold"])+"!")
            print(f" {other.name} blew away with the wind.")
            if len(optr.pokemons)>1 and other.ability!="Suction Cups" and other.dmax is False:
                resetboost(other,self)
                l=other
                while True:
                    other=random.choice(optr.pokemons)
                    if other!=l:
                        break
                print(f" {other.name} was dragged out!")
                entryeff(other,self,optr,tr,field,turn) 
        elif used=="Return":
            retrn(self,other)
        elif used=="Lovely Kiss":
            lovelykiss(self,other,turn)
        elif used=="Sleep Powder":
            sleeppowder(self,other,turn)
        elif used=="Spore":
            spore(self,other,turn)
        elif used=="Hypnosis":
            hypnosis(self,other,turn)
        elif used=="Dark Void":
            darkvoid(self,other,turn)
        elif used=="Body Press":
            bodypress(self,other)
        elif used=="Blizzard":
            blizzard(self,other)
        elif used=="Air Slash":
            airslash(self,other)
        elif used=="Shadow Bone":
            shadowbone(self,other)
        elif used=="Gyro Ball":
            gyroball(self,other)
        elif used=="Electro Ball":
            electroball(self,other)
        elif used=="Electroweb":
            electroweb(self,other)
        elif used=="Blast Burn":
            blastburn(self,other)
            if other.hp>0:
                self.recharge=True
        elif used=="Frenzy Plant":
            frenzyplant(self,other)
            if other.hp>0:
                self.recharge=True
        elif used=="Hydro Cannon":
            hydrocannon(self,other)
            if other.hp>0:
                self.recharge=True
        elif used=="Zap Cannon":
            zapcannon(self,other)
        elif used=="Freeze-Dry":
            freezedry(self,other)
        elif used=="Ice Fang":
            icefang(self,other)
        elif used=="Coil":
            coil(self,other)
        elif used=="Dual Chop":
            hitx=0
            while True:
                hitx+=1
                dualchop(self,other)
                if hitx==2 or other.hp<=0:
                    break
            print(f" It hit {hitx} time(s).")      
        elif used=="Dragon Darts":
            hitx=0
            while True:
                hitx+=1
                dragondarts(self,other)
                if hitx==2 or other.hp<=0:
                    break
            print(f" It hit {hitx} time(s).")      
        elif used=="Dual Wingbeat":
            hitx=0
            while True:
                hitx+=1
                dualwingbeat(self,other)
                if hitx==2 or other.hp<=0:
                    break
            print(f" It hit {hitx} time(s).")      
        elif used=="Order Up":
            orderup(self,other)                
        elif used=="Acrobatics":
            acrobatics(self,other)
        elif used=="Curse":
            curse(self,other)
        elif used=="Dragon Ascent":
            dragonascent(self,other)
        elif used=="Foul Play":
            foulplay(self,other)
        elif used=="High Horsepower":
            highhorsepower(self,other)
        elif used=="Water Shuriken":
            hit=random.randint(2,5)
            if self.item=="Loaded Dice":
                hit=random.randint(4,5)
            if self.ability=="Skill Link":
                print(f" {self.name}'s {self.ability}.")
                hit=5
            for i in range(hit):
                watershuriken(self,other)
            print(f" It hit {hit} time(s).")           
        elif used=="Double Iron Bash":
            hitx=0
            while True:
                hitx+=1
                ironbash(self,other)
                if hitx==2 or other.hp<=0:
                    break
            print(f" It hit {hitx} time(s).")           
        elif used=="Population Bomb":
            hit=0
            choice=0
            while hit!=10 and choice<90:
                if (self.item=="None" or self.item!="Wide Lens") and self.ability!="Skill Link":
                    choice=random.randint(1,100)
                    hit+=1
                if self.item=="Wide Lens":
                    hit = random.choice([9,10])
                    break
                if self.ability=="Skill Link":
                    print(f" {self.name}'s {self.ability}.")
                    hit=10
                    break
            hitx=0
            while True:
                hitx+=1
                populationbomb(self,other)
                if hitx==hit or other.hp<=0:
                    break
            print(f" It hit {hitx} time(s).")    
        elif used=="Twin Beam":
            hitx=0
            while True:
                hitx+=1
                twinbeam(self,other)
                if hitx==2 or other.hp<=0:
                    break
            print(f" It hit {hitx} time(s).")      
        elif used=="Gear Grind":
            hitx=0
            while True:
                hitx+=1
                geargrind(self,other)
                if hitx==2 or other.hp<=0:
                    break
            print(f" It hit {hitx} time(s).")        
        elif used=="Scale Shot":
            hit=random.randint(3,5)
            if self.ability=="Skill Link":
                print(f" {self.name}'s {self.ability}.")
                hit=5
            if self.item=="Loaded Dice":
                hit=random.randint(4,5)
            hitx=0
            while True:
                hitx+=1
                scaleshot(self,other)
                if hitx==hit or other.hp<=0:
                    break 
            speedchange(self,self,0.5)       
            defchange(self,self,-0.5)
            print(f" It hit {hitx} time(s).")
        elif used=="Triple Dive":
            hitx=0
            while True:
                hitx+=1
                tripledive(self,other)
                if hitx==3 or other.hp<=0:
                    break
            print(f" It hit {hitx} time(s).")      
        elif used=="Bone Rush":
            hit=random.randint(3,5)
            if self.ability=="Skill Link":
                print(f" {self.name}'s {self.ability}.")
                hit=5
            if self.item=="Loaded Dice":
                hit=random.randint(4,5)
            hitx=0
            while True:
                hitx+=1
                bonerush(self,other)
                if hitx==hit or other.hp<=0:
                    break 
            print(f" It hit {hitx} time(s).")
        elif used=="Bullet Seed":
            hit=random.randint(3,5)
            if self.ability=="Skill Link":
                print(f" {self.name}'s {self.ability}.")
                hit=5
            if self.item=="Loaded Dice":
                hit=random.randint(4,5)
            hitx=0
            while True:
                hitx+=1
                bulletseed(self,other)
                if hitx==hit or other.hp<=0:
                    break 
            print(f" It hit {hitx} time(s).")
        elif used=="Jet Punch":
            jetpunch(self,other)
        elif used=="Signal Beam":
            signalbeam(self,other,turn)
        elif used=="Anchor Shot":
            anchorshot(self,other)
        elif used=="Grass Knot":
            grassknot(self,other)
        elif used=="Extrasensory":
            extrasensory(self,other)
        elif used=="Wild Charge":
            wildcharge(self,other)
        elif used=="Multi-Attack":
            multiattack(self,other)
        elif used=="Wave Crash":
            wavecrash(self,other)
        elif used=="Power Gem":
            powergem(self,other)
        elif used=="Axe Kick":
            axekick(self,other,turn)
        elif used=="High Jump Kick":
            hijumpkick(self,other)
        elif used=="Plasma Fists":
            plasmafists(self,other)
        elif used=="Blaze Kick":
            blazekick(self,other)
        elif used=="Crush Claw":
            crushclaw(self,other)
        elif used=="Lava Plume":
            lavaplume(self,other)
        elif used=="Hurricane":
            hurricane(self,other,turn)        
        elif used=="Sky Uppercut":
            skyuppercut(self,other)
        elif used=="Precipice Blades":
            precipiceblades(self,other)
        elif used=="Origin Pulse":
            originpulse(self,other)
        elif used=="Sheer Cold":
            sheercold(self,other)
        elif used=="Fissure":
            fissure(self,other)
        elif used=="Guillotine":
            guillotine(self,other)
        elif used=="Horn Drill":
            horndrill(self,other)      
        elif used=="Dragon Rush":
            dragonrush(self,other)          
        elif used=="Draco Meteor":
            dracometeor(self,other)
        elif used=="Psycho Boost":
            psychoboost(self,other)
        elif used=="Drill Run":
            drillrun(self,other)
        elif used=="Head Smash":
            headsmash(self,other)
        elif used=="Flash Cannon":
            flashcannon(self,other)
        elif used=="Toxic Spikes":
            print(f" ☠️ {self.name} used "+colored("Toxic Spikes","magenta",attrs=["bold"])+".")
            if tr.hazard.count("Toxic Spikes")==3:
                print(" Nothing happened!")
            elif optr.hazard.count(" Toxic Spikes")<3 and other.ability!="Magic Bounce":
                print(" ☠️ Poison spikes were scattered all around the opposing team!")
                optr.hazard.append("Toxic Spikes")
            elif tr.hazard.count("Toxic Spikes")<3 and other.ability=="Magic Bounce":
                print(f" {other.name} bounced back the Toxic Spikes!")
                print(" ☠️ Poison spikes were scattered all around your team!")
                tr.hazard.append("Toxic Spikes")
            
        elif used=="Spikes":
            print(f" ✴️ {self.name} used "+colored(" Spikes","yellow",attrs=["bold"])+"!")
            if optr.hazard.count("Spikes")<3 and other.ability!="Magic Bounce":
                print(" ✴️ Spikes were scattered all around the opposing team!")
                optr.hazard.append("Spikes")
            if tr.hazard.count("Spikes")<3 and other.ability=="Magic Bounce":
                print(f" {other.name} bounced back the Spikes!")
                print(" ✴️ Spikes were scattered all around your team!")     
                tr.hazard.append("Spikes")
            else:
                print(" Nothing happened!")
              
        elif used=="Stealth Rock":
            print(f" 🪨 {self.name} used "+colored(" Stealth Rock","yellow",attrs=["bold"])+"!")
            if "Stealth Rock" in optr.hazard:
                print(" Nothing happened!")
            if "Stealth Rock" not in optr.hazard and other.ability!="Magic Bounce":
                print(" 🪨 Pointed stones float in the air around the opposing team!")
                optr.hazard.append("Stealth Rock")
            if "Stealth Rock" not in tr.hazard and other.ability=="Magic Bounce":
                print(f" {other.name} bounced back the Stealth Rock!")
                print(" 🪨 Pointed stones float in the air around your team!")
                tr.hazard.append("Stealth Rock")  
        elif used=="Sticky Web":
            print(f" {self.name} used "+colored(" Sticky Web","green",attrs=["bold"])+"!")
            if "Sticky Web" in optr.hazard:
                print(" Nothing happened!")
            if "Sticky Web" not in optr.hazard and other.ability!="Magic Bounce":
                print(" 🕸️ A sticky web spreads out in the ground around the opposing team!")
                optr.hazard.append("Sticky Web")
            if "Sticky Web" not in tr.hazard and other.ability=="Magic Bounce":
                print(" 🕸️ A sticky web spreads out in the ground around your team!")
                tr.hazard.append("Sticky Web") 
        elif used=="Transform":
            transform(self,other)
        elif used=="Seismic Toss":
            seismictoss(self,other)
        elif used=="Night Shade":
            nightshade(self,other)
        elif used=="Snarl":
            snarl(self,other)
        elif used=="Soft-Boiled":
            if self.hp==self.maxhp:
                print(f" {self.name} used {used}!")
                print("  It failed!")
            else:
                softboiled(self,other)
        elif used=="Heal Order":
            if self.hp==self.maxhp:
                print(f" {self.name} used {used}!")
                print("  It failed!")
            else:
                healorder(self,other)
        elif used=="Slack Off":
            if self.hp==self.maxhp:
                print(f" {self.name} used {used}!")
                print("  It failed!")
            else:
                slackoff(self,other)
        elif used=="Roost":
            if self.hp==self.maxhp:
                print(f" {self.name} used {used}!")
                print("  It failed!")
            else:
                roost(self,other)
        elif used=="Recover":
            if self.hp==self.maxhp:
                print(f" {self.name} used {used}!")
                print("  It failed!")
            else:
                recover(self,other)
        elif used=="Jungle Healing":
            if self.hp==self.maxhp:
                print(f" {self.name} used {used}!")
                print("  It failed!")
            else:
                junglehealing (self,other)            
        elif used=="Spiky Shield":
            self.protect=True
            print(f" 🔰 {self.name} used "+colored(" Spiky Shield","green",attrs=["bold"])+"!")
        elif used=="Baneful Bunker":
            self.protect=True
            print(f" ⛺ {self.name} used "+colored(" Baneful Bunker","magenta",attrs=["bold"])+"!")
        elif used=="Silk Trap":
            self.protect=True
            print(f" 🕸️ {self.name} used "+colored(" Silk Trap","green",attrs=["bold"])+"!")
        elif used=="Protect":
            self.protect=True
            print(f" 🛡️ {self.name} used "+colored(" Protect","white",attrs=["bold"])+"!")
        elif used=="Max Guard":
            self.protect=True
            print(f" 🔺🛡️ {self.name} used "+colored(" Max Guard","white",attrs=["bold"])+"!")
        elif used=="King's Shield":
            self.protect=True
            print(f" 👑🛡️ {self.name} used "+colored(" King's Shield","white",attrs=["bold"])+"!")
        elif used=="Morning Sun":
            if self.hp==self.maxhp:
                print(f" {self.name} used {used}!")
                print("  It failed!")
            else:
                morningsun(self,other)
        elif used=="Moonlight":
            print(f" {self.name} used {used}!")
            if self.hp==self.maxhp:
                print("  It failed!")
            else:
                moonlight(self,other)
        elif used=="Megahorn":
            megahorn(self,other)
        elif used=="Leaf Storm":
            leafstorm(self,other)
        elif used=="Leaf Tornado":
            leaftornado(self,other)
        elif used=="Leaf Blade":
            leafblade(self,other)
        elif used=="Razor Leaf":
            razorleaf(self,other)
        elif used=="Victory Dance":
            victorydance(self,other)
            if other.ability=="Dancer":
                print(f" {other.name}'s {other.ability}!")
                victorydance(other)
        elif used=="Light Screen":
            if tr.lightscreen==True:
                print(f" {self.name} used {used}!")
                print(" It Failed!")
            if tr.lightscreen==False:
                lightscreen(self,other,tr,turn)
        elif used=="Calm Mind":
            calmmind(self,other)
        elif used=="Aurora Veil":
            if tr.auroraveil==True:
                print(f" {self.name} used {used}!")
                print(" It failed!")
            if tr.auroraveil==False:
                auroraveil(self,other,tr,turn)
        elif used=="Tailwind":
            if tr.tailwind==True:
                print(f" {self.name} used {used}!")
                print(" It failed!")
            if tr.tailwind==False:
                tailwind(self,other,tr,turn)
        elif used=="Reflect":
            if tr.reflect==True:
                print(f" {self.name} used {used}!")
                print(" It failed!")
            if tr.reflect==False:
                reflect(self,other,tr,turn)
        elif used=="Acid Armor":
            acidarmor(self,other)
        elif used=="Aeroblast":
            aeroblast(self,other)
        elif used=="Wicked Blow":
            wickedblow(self,other)
        elif used=="Tail Glow":
            tailglow(self,other)
        elif used=="Psychic Fangs":
            psychicfang(self,other)
        elif used=="Poison Fang":
            poisonfang(self,other)
        elif used=="Poison Tail":
            poisontail(self,other)
        elif used=="Low Kick":
            lowkick(self,other)
        elif used=="Force Palm":
            forcepalm(self,other)
        elif used=="Techno Blast":
            technoblast(self,other)
        elif used=="Relic Song":
            relicsong(self,other,turn)
        elif used=="Drain Punch":
            drainpunch(self,other)
        elif used=="Frost Breath":
            frostbreath(self,other)
        elif used=="Head Charge":
            headcharge(self,other)
        elif used=="Icicle Crash":
            iciclecrash(self,other)
        elif used=="Toxic Thread":
            toxicthread(self,other)
        elif used=="Nature's Madness":
            naturesmadness(self,other)
        elif used=="Scorching Sands":
            scorchingsands(self,other)
        elif used=="Thrash":
            thrash(self,other)
        elif used=="Outrage":
            outrage(self,other)
        elif used=="Pounce":
            pounce(self,other)
        elif used=="Lunge":
            lunge(self,other)
        elif used=="Strength Sap":
            strengthsap(self,other)
        elif used=="Surging Strikes":
            for i in range(3):
                surgingstrikes(self,other)
        elif used=="Heat Wave":
            heatwave(self,other)
        elif used=="Slash":
            slash(self,other)
        elif used=="Night Slash":
            nightslash(self,other)
        elif used=="Psycho Cut":
            psychocut(self,other)
        elif used=="Sacred Fire":
            sacredfire(self,other)
        elif used=="Brick Break":
            brickbreak(self,other,optr)
        elif used=="Rock Wrecker":
            rockwrecker(self,other)
            if other.hp>0:
                self.recharge=True            
        elif used=="Giga Impact":
            gigaimpact(self,other)
            self.recharge=True
        elif used=="Meteor Assault":
            meteorassault (self,other)
            self.recharge=True
        elif used=="Cross Chop":
            crosschop(self,other)
        elif used=="Hyper Beam":
            hyperbeam(self,other)
            self.recharge=True
        elif used=="Roar of Time":
            roaroftime(self,other)
            self.recharge=True
        elif used=="Spacial Rend":
            spacialrend(self,other)
        elif used=="Phantom Force":
            phantomforce(self,other)      
                   
        elif used=="Shadow Force":
            shadowforce(self,other)   
                      
        elif used=="Iron Head":
            ironhead(self,other)
        elif used=="Iron Tail":
           irontail (self,other)
        elif used=="Dazzling Gleam":
            dazzlinggleam (self,other)
        elif used=="Magma Storm":
            magmastorm(self,other,turn)
        elif used=="Water Spout":
            waterspout(self,other)
        elif used=="Eruption":
            eruption (self,other)
        elif used=="Dragon Pulse":
            dragonpulse (self,other)
        elif used=="Play Rough":
            playrough (self,other)
        elif used=="Rock Polish":
            rockpolish (self,other)
        elif used=="Agility":
            agility(self,other)
        elif used=="Power Whip":
            powerwhip(self,other)
        elif used=="Ancient Power":
            apower(self,other)
        elif used=="Stone Axe":
            stoneaxe(self,other,optr)
        elif used=="Strength":
            strength(self,other)
        elif used=="Petal Dance":
            petaldance(self,other)
            if other.ability=="Dancer":
                print(f" {other.name}'s {other.ability}!")
                petaldance(other)
        elif used=="Dragon Tail":
            dragontail(self,other) 
            if "Fairy" not in (other.type1,other.type2,other.teratype) and other.hp>0:
                if len(optr.pokemons)>1 and other.ability!="Suction Cups" and other.dmax is False:
                    resetboost(other,self)
                    l=other
                    while True:
                        other=random.choice(optr.pokemons)
                        if other!=l:
                            break
                    print(f" {other.name} was dragged out!")
                    entryeff(other,self,optr,tr,field,turn)
        elif used=="Rock Tomb":
            rocktomb(self,other)     
        elif used=="Infestation":
            infestation(self,other,turn)
        elif used=="Fire Spin":
            firespin(self,other,turn)
        elif used=="Whirlpool":
            whirlpool(self,other,turn)
        elif used=="Last Resort":
            lastresort (self,other)           
        elif used=="G-Max Gravitas":
            gmaxgravitas(self,other)
        elif used=="Dizzy Punch":
            dizzypunch (self,other,turn)
        elif used=="G-Max Sandblast":
            gmaxsandblast(self,other,field,turn)
        elif used=="G-Max Resonance":
            gmaxresonance(self,other,tr,turn)
        elif used=="G-Max Stonesurge":
            gmaxstonesurge(self,other,optr)
        elif used=="Barb Barrage":
            barbbarrage (self,other)
        elif used=="Storm Throw":
            stormthrow(self,other)
        elif used=="Venom Drench":
            venomdrench(self,other)
        elif used=="Vaccum Wave":
            vaccumwave(self,other)
        elif used=="Mach Punch":
            machpunch(self,other)
        elif used=="Thunder":
            thunder(self,other)
        elif used=="Scald":
            scald(self,other)
        elif used=="Egg Bomb":
            eggbomb(self,other)
        elif used=="Hex":
            hex (self,other)
        elif used=="First Impression":
            if self.canfakeout==False:
                print(f" {self.name} used {used}!")
                print("  It failed!")
            if self.canfakeout==True:
                firstimpression(self,other)
                self.canfakeout=False
        elif used=="Fake Out":
            if self.canfakeout==False and self.ability!="Parental Bond[Used]":
                print(f" {self.name} used {used}!")
                print("  It failed!")
            if self.canfakeout==False and self.ability=="Parental Bond[Used]":
                fakeout(self,other)
                self.canfakeout=False
            if self.canfakeout==True:
                fakeout(self,other)
                self.canfakeout=False
        elif used=="Power-up Punch":
            poweruppunch(self,other)
        elif used=="Double-Edge":
            doubleedge(self,other)
        elif used=="Esper Wing":
            esperwing(self,other)
        elif used=="Dire Claw":
            direclaw(self,other,turn)
        elif used=="Dragon Claw":
            dragonclaw(self,other)
        elif used=="Psyshield Bash":
            psyshield(self,other)
        elif used=="Surf":
            surf(self,other)
        elif used=="Aqua Tail":
            aquatail(self,other)
        elif used=="Razor Wind":
            razorwind(self,other)
        elif used=="Sky Attack":
            skyattack(self,other)
        elif used=="Belly Drum":
            bellydrum(self,other)
        elif used=="Weather Ball":
            weatherball(self,other)
        elif used=="Crunch":
            crunch(self,other)
        elif used=="Aqua Jet":
            aquajet(self,other)
        elif used=="Ice Shard":
            iceshard(self,other)
        elif used=="Bug Buzz":
            bugbuzz(self,other)
        elif used=="Flamethrower":
            flamethrower(self,other)
        elif used=="Flare Blitz":
            flareblitz(self,other)
        elif used=="Thunder Punch":
            tpunch(self,other)
        elif used=="Fire Punch":
            firepunch(self,other)
        elif used=="Ice Punch":
            icepunch(self,other)
        elif used=="Zen Headbutt":
            zenheadbutt(self,other)
        elif used=="Dragon Hammer":
            dragonhammer(self,other)
        elif used=="Arm Thrust":
            hit=random.randint(3,5)
            if self.ability=="Skill Link":
                print(f" {self.name}'s {self.ability}.")
                hit=5
            if self.item=="Loaded Dice":
                hit=random.randint(4,5)
            hitx=0
            while True:
                hitx+=1
                armthrust(self,other)
                if hitx==hit or other.hp<=0:
                    break 
            print(f" It hit {hitx} time(s).")
        elif used=="Pin Missile":
            hit=random.randint(3,5)
            if self.ability=="Skill Link":
                print(f" {self.name}'s {self.ability}.")
                hit=5
            if self.item=="Loaded Dice":
                hit=random.randint(4,5)
            hitx=0
            while True:
                hitx+=1
                pinmissile(self,other)
                if hitx==hit or other.hp<=0:
                    break 
            print(f" It hit {hitx} time(s).")
        elif used=="Misty Explosion":
            if other.ability=="Damp":
                print("  Can't explode on Damp Pokémons.")
            if other.ability!="Damp":
                mistyexplosion(self,other)
        elif used=="Explosion":
            if other.ability=="Damp":
                print("  Can't explode on Damp Pokémons.")
            if other.ability!="Damp":
                explosion(self,other)
        elif used=="Icicle Spear":
            hit=random.randint(3,5)
            if self.ability=="Skill Link":
                print(f" {self.name}'s {self.ability}.")
                hit=5
            if self.item=="Loaded Dice":
                hit=random.randint(4,5)
            hitx=0
            while True:
                hitx+=1
                iciclespears(self,other)
                if hitx==hit or other.hp<=0:
                    break 
            print(f" It hit {hitx} time(s).")
        elif used=="Waterfall":
            waterfall(self,other)
        elif used=="Wood Hammer":
            woodhammer(self,other)
        elif used=="Energy Ball":
            energyball(self,other)
        elif used=="Rest":
            if self.hp==self.maxhp:
                print(f" {self.name} used {used}!")
                print("  It failed!")
            else:
                rest(self,other,turn)
        elif used=="Bulk Up":
            bulkup(self,other)
        elif used=="Stone Edge":
            stoneedge(self,other)
        elif used=="Steel Wing":
            steelwing(self,other)
        elif used=="Focus Blast":
            focusblast(self,other)
        elif used=="Rock Slide":
            rockslide(self,other)
        elif used=="Shadow Ball":
            shadowball(self,other)
        elif used=="Wildbolt Storm":
            wildboltstorm(self,other)
        elif used=="Springtide Storm":
            springtidestorm(self,other)
        elif used=="Sandsear Storm":
            sandsearstorm(self,other)
        elif used=="Bleakwind Storm":
            bleakwindstorm(self,other)
        elif used=="Make It Rain":
            makeitrain(self,other)
        elif used=="Dark Pulse":
            darkpulse(self,other)
        elif used=="Sacred Sword":
            sacredsword(self,other)
        elif used=="Secret Sword":
            secretsword(self,other)
        elif used=="Super Fang":
            superfang(self,other)
        elif used=="Core Enforcer":
            coreenforcer(self,other)
        elif used=="Superpower":
            superpower(self,other)
        elif used=="Assurance":
            assurance(self,other)
        elif used=="Rock Blast":
            hit=random.randint(3,5)
            if self.ability=="Skill Link":
                print(f" {self.name}'s {self.ability}.")
                hit=5
            if self.item=="Loaded Dice":
                hit=random.randint(4,5)
            for i in range(hit):
                rockblast(self,other)
            print(f" It hit {hit} time(s).")
        elif used=="Cross Poison":
            crosspoison(self,other)
        elif used=="Solar Beam":
            solarbeam(self,other)
        elif used=="Solar Blade":
            solarblade(self,other)
        elif used=="Sludge Bomb":
            sludgebomb(self,other)
        elif used=="Sludge Wave":
            sludgewave(self,other)
        elif used=="Close Combat":
            closecombat(self,other)
        elif used=="Submission":
            submission(self,other)
        elif used=="Brave Bird":
            bravebird(self,other)
        elif used=="Body Slam":
            bodyslam(self,other)
        elif used=="Dynamic Punch":
            dynapunch(self,other,turn)
        elif used=="Liquidation":
            liquidation(self,other)
        elif used=="Tera Blast":
            terablast(self,other)
        elif used=="Earthquake":
            earthquake(self,other)
        elif used=="Belch":
            belch(self,other)
        elif used=="Gunk Shot":
            gunkshot(self,other)
        elif used=="Freeze Shock":
            freezeshock(self,other)                   
        elif used=="Ice Burn":
            iceburn(self,other)                      
        elif used=="Blue Flare":
            blueflare(self,other)     
        elif used=="Eternabeam":
            eternabeam (self,other)   
            self.recharge=True                
        elif used=="Bolt Strike":
            boltstrike(self,other)   
        elif used=="Thunder Cage":
            thundercage(self,other)     
        elif used=="Mountain Gale":
            mountaingale(self,other)       
        elif used=="Mystical Power":#isinstance(used,FireBlast)
            mysticalpower(self,other)                
                                                
        elif used=="Fire Blast":#isinstance(used,FireBlast)
            fireBlast(self,other)
            
        elif used=="Bounce":
            bounce(self,other)                 
        elif used=="Pyro Ball":
            pyroball(self,other)     
                      
        elif used=="Meteor Beam":
            meteorbeam(self,other)                                
        elif used=="Psychic":
            psychic(self,other)
        elif used=="Seed Flare":
            seedflare(self,other)
        elif used=="Thunderbolt":
            tbolt(self,other)
        elif used=="Shell Trap":
            print(f" {self.name} used Shell Trap!")
            self.abilityused="Shell Trap"
        elif used=="Poison Jab":
            poisonjab(self,other)
        elif used=="Judgement":
            judgement(self,other)
        elif used=="Discharge":
            discharge(self,other)
        elif used=="Ice Beam":
            icebeam(self,other)
        elif used=="Fusion Bolt":
            fusionbolt(self,other)
        elif used=="Fiery Wrath":
            fierywrath(self,other)
        elif used=="Thunderous Kick":
            thunderouskick(self,other)
        elif used=="Fusion Flare":
            fusionflare(self,other)
        elif used=="Moonblast":
            moonblast(self,other)
        elif used=="Hydro Pump":
            hydropump(self,other)
        elif used=="Earth Power":
            earthpower(self,other)
        elif used=="Destiny Bond":
            destinybond(self,other)
        elif used=="Giga Drain":
            gigadrain(self,other)
        elif used=="Hidden Power":
            hiddenpower(self,other)
        elif used =="Hydro Vortex":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Waterium-Z.")
            self.item+="[Used]"             
            print(f" {self.name} surrounded itself with its Z-Power!")
            print(f" {self.name} unleashes its full-force Z-Move!")
            hydrovortex(self,other)
            self.moves.remove(used)
        elif used =="Oceanic Operetta":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item+="[Used]"             
            print(f" {self.name} surrounded itself with its Z-Power!")
            print(f" {self.name} unleashes its full-force Z-Move!")
            operetta(self,other)
            self.moves.remove(used)
        elif used =="Malicious Moonsault":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item+="[Used]"             
            print(f" {self.name} surrounded itself with its Z-Power!")
            print(f" {self.name} unleashes its full-force Z-Move!")
            moonsault(self,other)
            self.moves.remove(used)
        elif used =="Light That Burns The Sky":
            self.name=self.name.split("(")[0]
            if "Ultra" not in self.name:
                transformation(self,other,turn)
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item+="[Used]"             
            print(f" {self.name} surrounded itself with its Z-Power!")
            print(f" {self.name} unleashes its full-force Z-Move!")
            skyburn(self,other)
            self.moves.remove(used)
        elif used =="Let's Snuggle Forever":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item+="[Used]"             
            print(f" {self.name} surrounded itself with its Z-Power!")
            print(f" {self.name} unleashes its full-force Z-Move!")
            snuggle(self,other)
            self.moves.remove(used)      
        elif used =="Extreme Evoboost":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item+="[Used]"             
            print(f" {self.name} surrounded itself with its Z-Power!")
            print(f" {self.name} unleashes its full-force Z-Move!")
            exevoboost(self,other)
            self.moves.remove(used)      
        elif used =="Guardian of Alola":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item+="[Used]"             
            print(f" {self.name} surrounded itself with its Z-Power!")
            print(f" {self.name} unleashes its full-force Z-Move!")
            goalola(self,other)
            self.moves.remove(used)
        elif used =="Stoked Sparksurfer":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item+="[Used]"             
            print(f" {self.name} surrounded itself with its Z-Power!")
            print(f" {self.name} unleashes its full-force Z-Move!")
            sparksurf(self,other)
            self.moves.remove(used)
        elif used =="Clangorous Soulblaze":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item+="[Used]"             
            print(f" {self.name} surrounded itself with its Z-Power!")
            print(f" {self.name} unleashes its full-force Z-Move!")
            soulblaze(self,other)
            self.moves.remove(used)
        elif used =="Sinister Arrow Raid":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item+="[Used]"             
            print(f" {self.name} surrounded itself with its Z-Power!")
            print(f" {self.name} unleashes its full-force Z-Move!")
            arrowraid(self,other)
            self.moves.remove(used)
        elif used =="Soul-Stealing 7-Star Strike":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item+="[Used]"             
            print(f" {self.name} surrounded itself with its Z-Power!")
            print(f" {self.name} unleashes its full-force Z-Move!")
            soulstealing(self,other)
            self.moves.remove(used)
        elif used =="Menacing Moonraze Maelstrom":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item+="[Used]"             
            print(f" {self.name} surrounded itself with its Z-Power!")
            print(f" {self.name} unleashes its full-force Z-Move!")
            menacingmoonrazemaelstrom(self,other)
            self.moves.remove(used)
        elif used =="Searing Sunraze Smash":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item+="[Used]"             
            print(f" {self.name} surrounded itself with its Z-Power!")
            print(f" {self.name} unleashes its full-force Z-Move!")
            searingsunrazesmash(self,other)
            self.moves.remove(used)
        elif used =="Genesis Supernova":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item+="[Used]"             
            print(f" {self.name} surrounded itself with its Z-Power!")
            print(f" {self.name} unleashes its full-force Z-Move!")
            genesissupernova(self,other,field,turn)
            self.moves.remove(used)
        elif used =="Pulverizing Pancake":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Snorlium-Z.")
            self.item+="[Used]"             
            print(f" {self.name} surrounded itself with its Z-Power!")
            print(f" {self.name} unleashes its full-force Z-Move!")
            pulverizingpancake(self,other)
            self.moves.remove(used)
        elif used =="Splintered Stormshards":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Lycanium-Z.")
            self.item+="[Used]"             
            print(f" {self.name} surrounded itself with its Z-Power!")
            print(f" {self.name} unleashes its full-force Z-Move!")
            stormshards(self,other)
            self.moves.remove(used)                
        elif used =="Inferno Overdrive":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Firium-Z.")
            self.item+="[Used]"             
            print(f" {self.name} surrounded itself with its Z-Power!")
            print(f" {self.name} unleashes its full-force Z-Move!")
            infernooverdrive(self,other)
            self.moves.remove(used)
        elif used =="Bloom Doom":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Grassium-Z.")
            self.item+="[Used]"             
            print(f" {self.name} surrounded itself with its Z-Power!")
            print(f" {self.name} unleashes its full-force Z-Move!")
            bloomdoom(self,other)
            self.moves.remove(used)
        elif used =="Gigavolt Havoc":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Electrium-Z.")
            self.item+="[Used]"             
            print(f" {self.name} surrounded itself with its Z-Power!")
            print(f" {self.name} unleashes its full-force Z-Move!")
            gigavolthavoc(self,other)
            self.moves.remove(used)
        elif used =="Catastropika":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item+="[Used]"             
            print(f" {self.name} surrounded itself with its Z-Power!")
            print(f" {self.name} unleashes its full-force Z-Move!")
            catastropika(self,other)
            self.moves.remove(used)
        elif used =="Pulverizing Pancake":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item+="[Used]"             
            print(f" {self.name} surrounded itself with its Z-Power!")
            print(f" {self.name} unleashes its full-force Z-Move!")
            pulverizingpancake(self,other)
            self.moves.remove(used)
        elif used =="10,000,000 Volt Thunderbolt":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item+="[Used]"             
            print(f" {self.name} surrounded itself with its Z-Power!")
            print(f" {self.name} unleashes its full-force Z-Move!")
            tenmvolttb(self,other)
            self.moves.remove(used)
        elif used =="Acid Downpour":
            self.name=self.name.split("(")[0]
            print(f" {self.name} surrounded itself with its Z-Power!")
            print(f" {self.name} unleashes its full-force Z-Move!")
            print(f" {self.name} reacting to {tr.name}'s Poisonium-Z.")
            self.item+="[Used]"   
            aciddownpour(self,other)
            self.moves.remove(used)                                  
        elif used =="Breakneck Blitz":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Normalium-Z.")
            self.item+="[Used]"             
            print(f" {self.name} surrounded itself with its Z-Power!")
            print(f" {self.name} unleashes its full-force Z-Move!")
            breakneckblitz(self,other)
            self.moves.remove(used)
        elif used =="All-Out Pummeling":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Fightinium-Z.")
            self.item+="[Used]"             
            print(f" {self.name} surrounded itself with its Z-Power!")
            print(f" {self.name} unleashes its full-force Z-Move!")
            alloutpummeling(self,other)
            self.moves.remove(used)
        elif used =="Black Hole Eclipse":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Darkinium-Z.")
            self.item+="[Used]"             
            print(f" {self.name} surrounded itself with its Z-Power!")
            print(f" {self.name} unleashes its full-force Z-Move!")
            blackholeeclipse(self,other)
            self.moves.remove(used)
        elif used =="Continental Crush":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Rockium-Z.")
            self.item+="[Used]"             
            print(f" {self.name} surrounded itself with its Z-Power!")
            print(f" {self.name} unleashes its full-force Z-Move!")
            continentalcrush(self,other)
            self.moves.remove(used)
        elif used =="Tectonic Rage":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Groundium-Z.")
            self.item+="[Used]"             
            print(f" {self.name} surrounded itself with its Z-Power!")
            print(f" {self.name} unleashes its full-force Z-Move!")
            tectonicrage(self,other)
            self.moves.remove(used)
        elif used =="Corkscrew Crash":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Steelium-Z.")
            self.item+="[Used]"             
            print(f" {self.name} surrounded itself with its Z-Power!")
            print(f" {self.name} unleashes its full-force Z-Move!")
            corkscrewcrash(self,other)
            self.moves.remove(used)
        elif used =="Devastating Drake":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Dragonium-Z.")
            self.item+="[Used]"             
            print(f" {self.name} surrounded itself with its Z-Power!")
            print(f" {self.name} unleashes its full-force Z-Move!")
            devastatingdrake(self,other)
            self.moves.remove(used)
        elif used =="Shattered Psyche":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Psychium-Z.")
            self.item+="[Used]"             
            print(f" {self.name} surrounded itself with its Z-Power!")
            print(f" {self.name} unleashes its full-force Z-Move!")
            shatteredpsyche(self,other)
            self.moves.remove(used)
        elif used =="Never-ending Nightmare":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Ghostium-Z.")
            self.item+="[Used]"             
            print(f" {self.name} surrounded itself with its Z-Power!")
            print(f" {self.name} unleashes its full-force Z-Move!")
            neverendingnightmare(self,other)
            self.moves.remove(used)
        elif used =="Supersonic Skystrike":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Flyinium-Z.")
            self.item+="[Used]"             
            print(f" {self.name} surrounded itself with its Z-Power!")
            print(f" {self.name} unleashes its full-force Z-Move!")
            supersonicskystrike(self,other)
            self.moves.remove(used)
        elif used =="Savage Spin-Out":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Buginium-Z.")
            self.item+="[Used]"             
            print(f" {self.name} surrounded itself with its Z-Power!")
            print(f" {self.name} unleashes its full-force Z-Move!")
            savagespinout(self,other)
            self.moves.remove(used)
        elif used =="Subzero Slammer":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Icium-Z.")
            self.item+="[Used]"             
            print(f" {self.name} surrounded itself with its Z-Power!")
            print(f" {self.name} unleashes its full-force Z-Move!")
            subzeroslammer (self,other)
            self.moves.remove(used)
        elif used =="Twinkle Tackle":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Fairium-Z.")
            self.item+="[Used]"             
            print(f" {self.name} surrounded itself with its Z-Power!")
            print(f" {self.name} unleashes its full-force Z-Move!")
            twinkletackle(self,other)
            self.moves.remove(used)
        elif used=="Counter":
           print(f" 👊 {self.name} used "+colored(" Counter","red",attrs=["bold"])+"!")
           if other.atkcat=="Physical" and "Ghost" not in (other.type1,other.type2,other.teratype):
               other.hp-=self.dmgtaken*2
           if other.atkcat=="Special":
               print(" It failed.")
        elif used=="Mirror Coat":
           print(f" 🪞 {self.name} used "+colored(" Mirror Coat","magenta",attrs=["bold"])+"!")
           if other.atkcat=="Special" and "Dark" not in (other.type1,other.type2,other.teratype):
               other.hp-=self.dmgtaken*2
           if other.atkcat=="Physical":
               print(" It failed.")
        else:
            pass
    if self.item=="Shell Bell" and other.dmgtaken>0 and other.protect==False and self.recharge==False:
        self.hp+=(other.dmgtaken/8)
        print(f" 🐚 {self.name} restored a little HP using its Shell Bell.")
    if self.ability=="Parental Bond":
        self.atk/=2
        self.ability="Parental Bond[Used]"
        self,other=attack(self,other,tr,optr,used,opuse,field,turn)
    if "Destiny Bond" in self.moves and used!="Destiny Bond":
        other.dbond=False
    if other.hp<0:
        other.hp=0
    other.dmgtaken=before-other.hp
    if other.ability=="Ice Face" and other.hp!=before and other.hp>0 and "Noice" not in other.name:
        print(f" 🐧 {other.name}'s {other.ability}!")
        other.name="Noice Face Eiscue"
        per=other.hp/other.maxhp
        self.weight=196.2
        other.hp=75
        other.atk=100
        other.defense=70
        other.spatk=45
        other.spdef=50
        other.speed=130
        other.calcst()
        other.hp=other.maxhp*per
    if used in typemoves.contactmoves and other.ability == "Sand Spit" and field.weather not in ["Sandstorm","Primordial Sea","Desolate Land"] and self.item not in ["Protective Pads","Punching Glove"]:
        print(f" 🏜️{other.name}'s {other.ability} whipped up a sandstorm!")
        field.weather="Sandstorm" 
        field.sandturn=turn
        field.sandend(self,other)
    if used in typemoves.contactmoves and other.abilityused=="Shell Trap" and self.item not in ["Protective Pads","Punching Glove"] and other.hp!=before:
        shelltrap(other,self)
        other.abilityused=False
    if other.item=="Focus Band" and used not in typemoves.multimove and other.hp<=0:
        ch=random.randint(1,10)
        if ch==1:
            print(f" {other.name} hung on using Focus Band.")
            other.hp=1
    if before==other.maxhp and other.hp<=0 and hit==1:        
        if "Ash" in other.owner.name:
            ch=random.randint(1,100)
            if ch<40:
                print(f" 💝 {other.name} got up remembering {other.owner.name}'s friendship!")
                other.hp=1
        if other.ability=="Phoenix Down" and other.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart"] and used not in typemoves.abilityigmoves:
            print(f" 🌈 {other.name}'s Phoenix Down!")
            print(f" {other.name} revived itself to half of its HP.")
            other.hp=(other.maxhp/2)      
            other.ability="Phoenix Down[Used]"  
        if other.ability in ["Sturdy","Nine Lives"] and other.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart"] and used not in typemoves.abilityigmoves and used not in typemoves.multimove:
            print(f" {other.name}'s {other.ability}!")
            print(f" {other.name} hung on using {other.ability}.")
            other.hp=1
            
        if other.item=="Focus Sash" and used not in typemoves.multimove:
            print(f" {other.name} hung on using Focus Sash.")
            other.hp=1
            other.item+="[Used]"
    
    if other.hp!=before and used!="None":
        self.miss=False
    if other.hp==before and used=="None":
        self.miss=True
        if self.item=="Blunder Policy":
            print(f" 📄 Blunder Policy was used upon miss!")
            item+="[Used]"
            speedchange(self,self,1)
    if len(self.moves)>=1 and self.use==self.moves[0] and len(self.pplist)>=1:
        if self.pplist[0]==1:
            pp=1
        self.pplist[0]-=pp
    elif len(self.moves)>=2 and self.use==self.moves[1] and len(self.pplist)>=2:
        if self.pplist[1]==1:
            pp=1
        self.pplist[1]-=pp
    elif len(self.moves)>=3 and self.use==self.moves[2] and len(self.pplist)>=3:
        if self.pplist[2]==1:
            pp=1
        self.pplist[2]-=pp
    elif len(self.moves)>=4 and self.use==self.moves[3] and len(self.pplist)>=4:
        if self.pplist[2]==1:
            pp=1
        self.pplist[3]-=pp
    if self.dmax is True and canatk is True:
        if len(self.maxmove)>=1 and used==self.maxmove[0]:
            self.pplist[0]-=pp
        if len(self.maxmove)>=2 and used==self.maxmove[1]:
            self.pplist[1]-=pp
        if len(self.maxmove)>=3 and used==self.maxmove[2]:
            self.pplist[2]-=pp
        if len(self.maxmove)>=4 and used==self.maxmove[3]:
            self.pplist[3]-=pp
    
    per=round(((before-other.hp)/other.maxhp)*100,2)
    sper=round(((sbefore-self.hp)/self.maxhp)*100,2)
    if other.focus==True and other.hp<before:
        print(f" {other.name} lost its focus!")
        other.focus=False
    if optr.sub!="None" and used not in typemoves.soundmoves:
        other=subr
        if optr.sub.hp>=0 and used not in typemoves.statusmove and optr.sub.hp!=before:
            print(f" The substitute took the damage for {subr.name}!")
        if optr.sub.hp<=0:
            optr.sub="None"
            print(f" The substitute faded away!")
    if self.hp>self.maxhp:
        self.hp=self.maxhp            
    if other.hp<0:
        per=round((before/other.maxhp)*100,2)
    if self.hp<0:
        sper=round((sbefore/self.maxhp)*100,2)
#PERCENTAGE       
    if before>they.hp and they==other:
        me.dmgdealt+=before-other.hp
        other.dmgrec+=before-other.hp
    if before>they.hp and they!=other:
        me.dmgdealt+=before-they.hp
        they.dmgrec+=before-they.hp            

    if sbefore!=self.hp and sbefore-self.hp<0 and self.ability!="Parental Bond" and self==me:
        print(f" ({self.name} regained {-sper}% of its health!)")
    if before!=other.hp and before-other.hp>0 and self.ability!="Parental Bond" and other==they:
        print(f" ({other.name} lost {per}% of its health!)")
    if self.hp!=sbefore and self==me and self.hp<sbefore and sper>0:
        print(f" Total damage received {sper}%")
    cl="green"
    if tr.ai==True:
        cl="red"
    print(colored("===================================================================================",cl))       
    if me.dmgdealt>0:
        if me.ability=="Toxic Drain":
            print(f" {me.name} regained some HP using its Toxic Drain!")
            me.hp+=(me.dmgdealt/2)
    if "Gulp Missile" in other.ability and other.hp!=before:
        if "-" in other.ability:
            print("===================================================================================")
            print(f" {other.name}'s Gulp Missile!")
            if self.ability!="Magic Guard":
                self.hp-=(self.maxhp/4)
            if "Pikachu" in other.ability:
                paralyzed(other,self,100)
                other.ability="Gulp Missile"
            if "Arrocuda" in other.ability:
                defchange(self,other,-0.5)
                other.ability="Gulp Missile"  
            print("===================================================================================")
    if other.hp>0:
        if other.ability=="Weak Armor" and self.atkcat=="Physical" and other.hp<before:
            print("===================================================================================")
            print(f" 🥜 {other.name}'s {other.ability}!")
            defchange (other,other,-0.5)
            speedchange (other,other,0.5)
            print("===================================================================================")
        if other.hp<=(other.maxhp/2)  and before>(other.maxhp/2):
            if other.ability=="Anger Shell":
                print("===================================================================================")
                print(f" 💢 {other.name}'s {other.ability}!")
                defchange(other,self,-0.5)
                spdefchange(other,self,-0.5)
                atkchange(other,self,0.5)
                spatkchange(other,self,0.5)
                speedchange(other,self,0.5)
                print("===================================================================================")
            if other.ability=="Swarm of Vermin":
                print(f" 🐀 {other.name}'s {other.ability}!")
                atkchange(other,self,0.5)
            if other.ability=="Berserk":
                print("===================================================================================")
                print(f" {other.name}'s {other.ability}!")
                spatkchange(other,self,0.5)
                print("===================================================================================")
        berry(other,self,other.item,before,turn)
    bg="white"              
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
    
    if other.ability=="Innards Out" and other==they and other.hp<=0:
        print(f" {other.name}'s Innards Out!")
        self.hp-=before
        
    if self.item=="Throat Spray" and used in typemoves.soundmoves:
        spatkchange(self,other,0.5)
        print(f" The Throat Spray raised {self.name}'s Special Attack!")
        self.item+="[Used]"            
    
    if other.hp>0:
          if other.hp<=(other.maxhp/4)  and before>(other.maxhp/4):
              
              
              if other.item=="Lansat Berry" and self.ability not in ["Unnerve","As One"]:
                  if other.ability=="Cheek Pouch" and other.hp<other.maxhp:
                      print(f" {other.name}'s Cheek Pouch!")
                      other.hp+=(other.maxhp/3)
                  print(colored(f" 🍅 {other.item} raised {other.name}'s critical hit ratio!!","red"))
                  n=4
                  if other.ability=="Ripen":
                      n=8
                  other.critrate*=n
                  other.item+="[Used]"
              if other.item=="Ganlon Berry" and self.ability not in ["Unnerve","As One"]:
                  if other.ability=="Cheek Pouch" and other.hp<other.maxhp:
                      print(f" {other.name}'s Cheek Pouch!")
                      other.hp+=(other.maxhp/3)
                  print(colored(f" 🍆 {other.item} raised {other.name}'s defense!!","blue"))
                  n=0.5
                  if other.ability=="Ripen":
                      n=1
                  defchange(other,self,n)
                  other.item+="[Used]"
              if other.item=="Apicot Berry" and self.ability not in ["Unnerve","As One"]:
                  if other.ability=="Cheek Pouch" and other.hp<other.maxhp:
                      print(f" {other.name}'s Cheek Pouch!")
                      other.hp+=(other.maxhp/3)
                  print(colored(f" 🍈 {other.item} raised {other.name}'s special defense!!","green"))
                  n=0.5
                  if other.ability=="Ripen":
                      n=1
                  spdefchange(other,self,n)
                  other.item+="[Used]"
    if self.dbond is True and other.hp<=0:
        self.hp=0
        print(f" 🥀 {other.name} took away {self.name} with it!")
#ILLUSION        
    if other.ability=="Illusion" and "Zoroark" not in other.name and other.hp!=before:
        if other.type1=="Dark":
            other.name="Zoroark"
            print(f" 🌀 {other.name}'s Illusion wore off!")
        else:
            other.name="Hisuian Zoroark"
            print(f" 🌀 {other.name}'s Illusion wore off!")
    if other.item=="Sticky Barb" and me.ability!="Long Reach" and used in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads"] and other.hp!=before:
        self.hp-=(self.maxhp/8)   
        other.hp-=(other.maxhp/8)
        if self.item=="None":
            self.item="Sticky Barb"
            other.item+="[Used]"
    if other.ability in ["Gooey","Tangling Hair"] and me.ability not in ["Clear Body","Good as Gold"] and me.ability!="Long Reach" and used in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads"] and other.hp!=before:
        print(f" {other.name}'s {other.ability}!")     
        speedchange(self,other,-0.5)
    if other.ability=="Radiant Blaze" and me.status=="Alive" and me.ability!="Long Reach" and used in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads"] and other.hp!=before:
        confuse(self,other,turn,100)        
    if other.ability=="Flame Body" and me.status=="Alive" and me.ability!="Long Reach" and used in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads"] and other.hp!=before:
        print(f" 🔥 {other.name}'s {other.ability}!")
        burn(self,other,30)
    if other.ability=="Seed Sower" and "Toxic Spikes" not in tr.hazard and me.ability!="Long Reach" and used in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads"] and field.terrain!="Grassy" and other.hp!=before:
        print(f" 🚜 {other.name}'s {other.ability}!")
        print(" 🌿 Grass grew to cover the battlefield!")
        field.terrain="Grassy"
        field.grassturn=turn
        field.grassend(self,other)          
    if other.ability=="Toxic Debris" and "Toxic Spikes" not in tr.hazard and me.ability!="Long Reach" and used in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads"] and other.hp!=before:
        print(f" ☣️ {other.name}'s {other.ability}!")   
        print(" ☠️ Poison spikes were scattered all around the opposing team!")
        tr.hazard.append("Toxic Spikes")   
    if other.ability in ["Mummy","Lingering Aroma","Wandering Spirit"] and me.ability!="Long Reach" and used in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads","Ability Shield"] and other.hp!=before and self.ability not in ["Mummy","Lingering Aroma","Wandering Spirit"]:     
        print(f" {other.name}'s {other.ability}!")
        self.ability=other.ability   
    if other.ability=="Cute Charm" and me.ability!="Long Reach" and used in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads"] and other.hp!=before:  
        self.infatuated=True
        print(f" 🥰 {other.name}'s {other.ability}!")
        print(f" 🥰 {self.name} is infatuated!")
    if other.ability=="Perish Body" and me.ability!="Long Reach" and used in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads"] and other.hp!=before and 0 in (self.perishturn,other.perishturn):   
        print(f" 💀 {other.name}'s {other.ability}!")  
        if self.perishturn==0:
            self.perishturn=4
        if other.perishturn==0:
            other.perishturn=4  
    if other.ability=="Static" and me.status=="Alive" and me.ability!="Long Reach" and used in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads"] and other.hp!=before:
        print(f" ⚡ {other.name}'s {other.ability}!")
        paralyzed(other,self,30)
    if other.ability=="Venomous Aura" and me.status=="Alive" and me.ability!="Long Reach" and used in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads"]:
        print(f" {other.name}'s {other.ability}!")
        poison(other,self,100)        
    if other.ability=="Poison Point" and me.status=="Alive" and me.ability!="Long Reach" and used in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads"]:
        print(f" ☣️ {other.name}'s {other.ability}!")
        poison(other,self,30)
    if self.ability in ["Poison Touch","Toxic Fangs","Toxic Drain"] and other.status=="Alive" and other.ability!="Long Reach" and used in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads"] and me==self:
        print(f" ☣️ {self.name}'s {self.ability}!")
        poison(self,other,30)  
    if used in typemoves.contactmoves and other.item=="Air Balloon" and self.item not in ["Punching Glove","Protective Pads"] and used not in typemoves.groundmoves and other.hp!=before:
        print(f" 🎈 {other.name}'s Air Balloon popped off!")
        other.item+="[Used]"                      
    if other.hp!=before:
        if used not in typemoves.statusmove:
#ROUGH SKIN/IRON BARBS            
            if other.ability in ["Rough Skin","Iron Barbs","Iron Spikes"] and used in typemoves.contactmoves and self.ability!="Long Reach" and self.item not in ["Punching Glove","Protective Pads"]:
                print(f" ✴️ {me.name} was hurt by {other.name}'s {other.ability}!")
                me.hp-=round((me.maxhp/16),2)
                if me.hp<0:
                    me.hp=0
        if other.item=="Rocky Helmet" and self.ability!="Magic Guard" and used in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads"]:
            me.hp-=round(me.maxhp/6)
            print(f" 🪖 {me.name} was hurt by {other.name}'s Rocky Helmet!")
            if me.hp<0:
                me.hp=0      
        if len(optr.pokemons)>1 and other.item=="Eject Pack" and used in typemoves.statusmove and self.speed>other.speed:
            print(f" 🪂 {other.name} returned to it's {pkball}.")
            other.item+="[Used]"
            other=random.choice(optr.pokemons)
            entryeff(other,self,optr,tr,field,turn)  
        if len(tr.pokemons)>1 and other.item=="Red Card":
            other.item+="[Used]"
            print(f" 🟥 {self.name} returned to it's {pkball}.")
            self=switch(self,other,tr,optr,field,turn)
        if len(optr.pokemons)>1 and other.item=="Eject Button" and self.speed>other.speed:
            print(f" 🔘 {other.name} was ejected and returned to it's {pkball}.")
            other.item+="[Used]"
            other=random.choice(optr.pokemons)
            entryeff(other,self,optr,tr,field,turn)
#LIFE ORB                    
        if me.item=="Life Orb" and me.ability!="Magic Guard":
            me.hp-=round(me.maxhp/16)
            print(f" 🟣 {me.name} lost some of its HP!")
            if self.hp<0:
                self.hp=0
    if other.item=="Custap Berry" and other.speed<self.speed and self.hp<(self.maxhp/4) and self.hp>0 and self.ability not in ["Unnerve","As One"]:
        if other.ability=="Cheek Pouch" and other.hp<other.maxhp:
            print(f" {other.name}'s Cheek Pouch!")
            other.hp+=(other.maxhp/3)
        print(colored(f" 🥝 {other.item} will let {other.name} move first!!","red"))
        other.priority=True
        other.item+="[Used]"     
    if other.item=="Persim Berry" and other.confused==True and other.hp>0 and self.ability not in ["Unnerve","As One"]:
        if other.ability=="Cheek Pouch" and other.hp<other.maxhp:
            print(f" {other.name}'s Cheek Pouch!")
            other.hp+=(other.maxhp/3)
        print(colored(f" 🍑 {other.item} cured {other.name}'s confusion!!","red"))
        other.confused=False
        other.item+="[Used]"        
    if self.item=="Persim Berry" and self.confused==True and self.hp>0 and other.ability not in ["Unnerve","As One"]:
        if self.ability=="Cheek Pouch" and self.hp<self.maxhp:
            print(f" {self.name}'s Cheek Pouch!")
            self.hp+=(self.maxhp*0.33)
        print(colored(f" 🍑 {self.item} cured {self.name}'s confusion!!","red"))
        self.confused=False
        self.item+="[Used]"        
    if self.item=="Cheri Berry" and self.status=="Paralyzed" and self.hp>0 and other.ability not in ["Unnerve","As One"]:
        if self.ability=="Cheek Pouch" and self.hp<self.maxhp:
            print(f" {self.name}'s Cheek Pouch!")
            self.hp+=(self.maxhp*0.33)
        print(colored(f" 🍒 {self.item} cured {self.name}'s paralysis!!","red"))
        self.status="Alive"
        self.item+="[Used]"
    if self.item=="Rawst Berry" and self.status=="Burned" and self.hp>0 and self.ability not in ["Unnerve","As One"]:
        if self.ability=="Cheek Pouch" and self.hp<self.maxhp:
            print(f" {self.name}'s Cheek Pouch!")
            self.hp+=(self.maxhp*0.33)
        print(colored(f" 🍓 {self.item} cured {self.name} from burn!!","cyan"))
        self.status="Alive"
        self.item+="[Used]"
    if self.item=="Chesto Berry" and self.status=="Sleep" and self.hp>0 and other.ability not in ["Unnerve","As One"]:
        if self.ability=="Cheek Pouch" and self.hp<self.maxhp:
            print(f" {self.name}'s Cheek Pouch!")
            self.hp+=(self.maxhp*0.33)
        print(colored(f" 🌰 {self.item} cured {self.name} from sleep state!!","blue"))
        print(f" ‼️ {self.name} woke up!")
        self.status="Alive"
        self.item+="[Used]"
    if other.item=="Chesto Berry" and other.status=="Sleep" and other.hp>0 and self.ability not in ["Unnerve","As One"]:
        if other.ability=="Cheek Pouch" and other.hp<other.maxhp:
            print(f" {other.name}'s Cheek Pouch!")
            other.hp+=(other.maxhp/3)
        print(colored(f" 🌰 {other.item} cured {other.name} from sleep state!!","blue"))
        print(f" ‼️ {other.name} woke up!")
        other.status="Alive"
        other.item+="[Used]"
    if self.item=="Aspear Berry" and self.status=="Frozen" and self.hp>0 and other.ability not in ["Unnerve","As One"]:
        if self.ability=="Cheek Pouch" and self.hp<self.maxhp:
            print(f" {self.name}'s Cheek Pouch!")
            self.hp+=(self.maxhp*0.33)
        print(colored(f" 🍐 {self.item} cured {self.name} from frozen state!!","yellow"))
        print(f" ‼️ {self.item} thawed out!")
        self.status="Alive"
        self.item+="[Used]"
    if other.item=="Aspear Berry" and other.status=="Frozen" and other.hp>0 and self.ability not in ["Unnerve","As One"]:
        if other.ability=="Cheek Pouch" and other.hp<other.maxhp:
            print(f" {other.name}'s Cheek Pouch!")
            other.hp+=(other.maxhp/3)
        print(colored(f" 🍐 {other.item} cured {other.name} from frozen state!!","yellow"))
        print(f" ‼️ {other.item} thawed out!")
        other.status="Alive"
        other.item+="[Used]"
    if self.item=="Pecha Berry" and self.status=="Badly Poisoned" and self.hp>0 and other.ability not in ["Unnerve","As One"]:
        if self.ability=="Cheek Pouch" and self.hp<self.maxhp:
            print(f" {self.name}'s Cheek Pouch!")
            self.hp+=(self.maxhp*0.33)
        print(colored(f" 🍑 {self.item} cured {self.name}'s poison!!","red"))
        self.status="Alive"
        self.item+="[Used]"
    if other.item=="Pecha Berry" and other.status=="Badly Poisoned" and other.hp>0 and self.ability not in ["Unnerve","As One"]:
        if other.ability=="Cheek Pouch" and other.hp<other.maxhp:
            print(f" {other.name}'s Cheek Pouch!")
            other.hp+=(other.maxhp/3)
        print(colored(f" 🍑 {other.item} cured {other.name}'s poison!!","red"))
        other.status="Alive"
        other.item+="[Used]"
    if self.item=="Lum Berry" and self.status!="Alive"and self.hp>0 and other.ability not in ["Unnerve","As One"]:
        if self.ability=="Cheek Pouch" and self.hp<self.maxhp:
            print(f" {self.name}'s Cheek Pouch!")
            self.hp+=(self.maxhp*0.33)
        print(colored(f" 🫒 {self.item} cured {self.name}'s status condition!!","green"))
        self.status="Alive"
        self.item+="[Used]"        
    if other.item=="Lum Berry" and other.status!="Alive" and other.hp>0 and self.ability not in ["Unnerve","As One"]:
        if other.ability=="Cheek Pouch" and other.hp<other.maxhp:
            print(f" {other.name}'s Cheek Pouch!")
            other.hp+=(other.maxhp/3)
        print(colored(f" 🫒 {other.item} cured {other.name}'s status condition!!","green"))
        other.status="Alive"
        other.item+="[Used]"         
    if other.ability=="Stamina" and other.hp!=before and self.hp>0:
        print(f" {other.name}'s {other.ability}!")
        defchange(other,self,0.5)       
    if other.hp<=other.maxhp/2 and other.hp>0:
        if other.item=="Sitrus Berry" and self.ability not in ["Unnerve","As One"]:
            if other.ability!="Ripen":
                other.hp+=round(other.maxhp/2)     
            if other.ability=="Ripen":
                other.hp+=round(other.maxhp/4)
            print(colored(f" 🍋 {other.name} restored HP using its {other.item}!!","yellow"))
            other.item+="[Used]"        
    if self.hp<=self.maxhp/2 and self.hp>0:
        if self.item=="Sitrus Berry" and other.ability not in ["Unnerve","As One"]:    
            if self.ability=="Ripen":   
                self.hp+=round(self.maxhp/2)
            if self.ability!="Ripen":   
                self.hp+=round(self.maxhp/4)
            print(colored(f" 🍋 {self.name} restored HP using its {self.item}!!","yellow"))
            self.item+="[Used]"    
    if other.ability=="Schooling" and "School" in other.name and other.hp<=(other.maxhp*0.25):
        print(f" 🐟 {other.name}'s {other.ability}!")
        other.name="Wishiwashi"
        per=other.hp/other.maxhp
        self.weight=0.66
        self.color="blue"
        other.hp=55
        other.atk=20
        other.defense=20
        other.spatk=25
        other.spdef=25
        other.speed=40
        other.calcst()
        other.hp=other.maxhp*per
    if self.item=="White Herb":
        if self.atkb<1 or self.defb<1 or self.spatkb<1 or self.spdefb<1 or self.speedb<1:
            print(f" White Herb cured {self.name}'s negative stats!")
            self.item+="[Used]"
            if self.atkb<1:
                self.atkb=1
            if self.defb<1:
                self.defb=1
            if self.spatkb<1:
                self.spatkb=1
            if self.spdefb<1:
                self.spdefb=1
            if self.speedb<1:
                self.speedb=1
    if other.item=="White Herb":
        if other.atkb<1 or other.defb<1 or other.spatkb<1 or other.spdefb<1 or other.speedb<1:
            print(f" White Herb cured {other.name}'s negative stats!")
            other.item+="[Used]"
            if other.atkb<1:
                other.atkb=1
            if other.defb<1:
                other.defb=1
            if other.spatkb<1:
                other.spatkb=1
            if other.spdefb<1:
                other.spdefb=1
            if other.speedb<1:
                other.speedb=1           
    if other.lockon==True:
        other.lockon=False                     
    return self,other
    
    
#EFFECTS
def effects(self,other,tr,turn):
    if self.hp>self.maxhp:
        self.hp=self.maxhp
    if other.hp>other.maxhp:
        other.hp=other.maxhp
    self.flinched=False
    self.canfakeout=False
    if turn==self.taunturn:
        print(f" {self.name}'s taunt ended!")
        self.taunted=False
    if turn==self.encturn:
        print(f" {self.name}'s encore ended!")
        self.encore=False
    if self.trap!=other:
        self.trap=False
    if self.ability=="Hunger Switch" and self.dmax==False and self.hp>0:
        print(f" {self.name}'s Hunger Switch!")
        if "Full Belly" in self.name:
            self.name="Hungry Mode Morpeko"
            self.atktype="Dark"
        elif "Hungry Mode" in self.name:
            self.name="Full Belly Morpeko"
            self.atktype="Electric"
    if self.cursed==True:
        print(f" {self.name} is afflicted by the curse!")
        if self.dmax==True:
            self.hp-=self.maxhp/6
        if self.dmax==False:
            self.hp-=self.maxhp/4            
    if self.ability=="Swarm":
        if self.hp<=(self.maxhp*0.3):
            print(f" 🪲 {self.name} is swarming around {other.name}!")
    if self.ability=="Overgrow":
        if self.hp<=(self.maxhp*0.3):
            print(f" 🌿 {self.name} is growing large vines and creating a jungle around it!")
    if self.ability=="Torrent":
        if self.hp<=(self.maxhp*0.3):
            print(f" 🌊 {self.name} is creating an oceanic aura!")
    if self.ability=="Blaze":
        if self.hp<=(self.maxhp*0.3):
            print(f" 🔥 {self.name} is unleashing huge amount of flame energy!")
    if tr.doom!=0 and tr.doom==turn:
        print(f" 💫 {self.name} took the Doom Desire attack!")
        self.hp-=tr.ftmul
        tr.doom=0
        tr.ftmul=0
    if tr.future!=0 and tr.future==turn:
        print(f" 🔮 {self.name} took the Future Sight attack!")
        self.hp-=tr.ftmul
        tr.future=0
        tr.ftmul=0
    if self.status!="Alive" and self.ability=="Shed Skin":
        x=random.randint(1,100)
        if x>67:
            print(f" 🦪 {self.name}'s Shed Skin!")
            self.status="Alive"
    if "Berry" in self.item and self.ability=="Harvest":
        if field.weather in ["Sunny","Desolate Land"]:
            if "Berry[Used]" in self.item:
                print(f" 🌽 {self.name}'s Harvest!")
                self.item=self.item.split("[")[0]
        else:
            ch=random.randint(1,2)
            if ch==1:
                if "Berry[Used]" in self.item:
                    print(f" 🌽 {self.name}'s Harvest!")
                    self.item=self.item.split("[")[0]
    if field.weather in ["Rainy","Primordial Sea"] and self.ability=="Hydration" and self.status!="Alive":
        self.status="Alive"           
        print(f" 💉 {self.name}'s status was cured by Hydration.")            
    if field.weather=="Primordial Sea" and "Primordial Sea" not in (self.ability,other.ability) and "Marine" not in field.location:
        field.weather="Clear"
        print (" 🌤️ The heavy rainfall stopped.")
    if field.weather=="Desolate Land" and "Desolate Land" not in (self.ability,other.ability) and "Terra" not in field.location and "Blaine(Hardcore Mode)" not in (self.owner.name,other.owner.name):
        field.weather="Clear"
        print (" 🌤️ The extreme sunlight fade away.")                     
    if field.trickroom==True:
        if turn==field.troomendturn:
            field.trickroom=False
            print (" 🌐 The dimensions turned back to normal!")                    
    if field.terrain=="Misty":
        if turn>=field.misendturn:
            print(" 🌐 The battlefield turned normal.")
            field.terrain="Normal"
    if field.terrain=="Psychic":
        if turn>=field.psyendturn:
            print(" 🌐 The battlefield turned normal.")
            field.terrain="Normal"
    if field.terrain=="Electric":
        if turn>=field.eleendturn:
            print(" 🌐 The electricity disappeared from the battlefield.")
            field.terrain="Normal"
            if "Quark Drive" in self.ability and self.item!="Booster Energy":
                print(" 🌐 The effects of {self.name}'s Quark Drive wore off.")
                self.ability="Quark Drive"
    if field.terrain=="Grassy":
        if turn>=field.grassendturn:
            print(" 🌐 The battlefield turned normal.")
            field.terrain="Normal"
    if field.weather=="Snowstorm":
        if turn>=field.snowstormendturn:
            print(" 🌥️The snowstorm stopped.")
            field.weather="Cloudy"            
    if field.weather=="Hail":
        if turn>=field.hailendturn:
            print(" 🌥️The hail stopped.")
            field.weather="Cloudy"
    if field.weather=="Sandstorm":
        if turn>=field.sandendturn:
            print(" 🌥️The sandstorm subsided.")
            field.weather="Clear"
    if field.weather=="Sunny":
        if turn>=field.sunendturn:
            print(" 🌤️The harsh sunlight faded.")
            field.weather="Clear"
            if "Protosynthesis" in self.ability:
                print(" 🌥️ The effects of {self.name}'s Protosynthesis wore off.")
                self.ability="Protosynthesis"
    if field.weather=="Rainy":
        if turn>=field.rainendturn:
            print(" 🌦️The rain stopped.")
            field.weather="Cloudy"                    
    if self.fmove==True:
        self.fmoveturn-=1
        if self.fmoveturn==0:
            self.fmove=False
            confuse(self,self,turn,100)
    if self.perishturn!=0:
        self.perishturn-=1
        print(f" 💔 {self.name}'s perish count fell to {self.perishturn}!")
        if self.perishturn==0:
            self.hp=0
            print(f" 💀 {self.name} perished away!")
    if self.ability=="Power Construct" and "Complete" not in self.name and self.hp<=(self.maxhp/2) and self.hp>0:
        print(f" ⚕️ {self.name}'s Power Construct!")
        self.name="Complete Zygarde"
        print(f" 🧬 You sense the presence of many!\n Zygarde transformed into its Complete Forme!")
        per=self.hp/self.maxhp
        self.weight=1344.82
        self.hp=216
        self.atk=100
        self.defense=91
        self.spatk=95
        self.spdef=85
        self.speed=85
        self.calcst()
        self.hp=self.maxhp*per            
    if self.ability=="Shield Down" and "Core" not in self.name and self.hp<=(self.maxhp/2) and self.hp>0:
        print(f" ☄️{self.name}'s Shield Down!")
        self.name="Core Minior"
        self.color=random.choice(["cyan","blue","red","yellow","green","magenta"])
        self.weight=88.18
        per=self.hp/self.maxhp
        self.hp=60
        self.atk=100
        self.defense=60
        self.spatk=100
        self.spdef=60
        self.speed=120
        self.calcst()
        self.hp=self.maxhp*per
    if self.item=="Flame Orb" and self.status=="Alive" and self.hp>0:
        self.status="Burned"
        print(f" ❤️‍🔥 {self.name} was burned by its Flame Orb.")
    if self.item=="Toxic Orb" and self.status=="Alive" and self.hp>0:
        self.status="Badly Poisoned"
        print(f" 🟣 {self.name} was badly poisoned by its Toxic Orb.")
    if self.ability=="Anticipation" and self.hp>0 and other.hp>0:
        l=moveAI(other,self,other.owner,tr,field)[1]
        dangermoves=["Explosion","Fissure","Sheer Cold","Horn Drill"]+l
        x=list(set(other.moves). intersection(dangermoves)) 
        if len(x)>0:
            x=str(x)[1:-1:]
            print(f" 🕵️ {self.name}'s {self.ability}.")
            print(f" ⚠️ {other.name} has some risky moves like {x}!")
    #BAD DREAMS
    if other.ability=="Bad Dreams" and self.status=="Sleep" and self.hp>0:
        self.hp-=round(self.maxhp/8)
        print(f" 💀 {self.name} is tormented.")
    #FROSTBITE
    if self.status=="Frostbite" and self.ability not in ["Magic Guard"] and self.hp>0:
        self.hp-=round(self.maxhp/16)
        print(f" 🥶 {self.name} was hurt by frostbite.")
    #LEECH SEED
    if self.seeded==True and self.hp>0 and other.hp>0:
        print(f" 🌱 The opposing {self.name}'s health is sapped by leech seed!")
        self.hp-=round(self.maxhp/16)
        if other.hp<=(other.maxhp-other.maxhp/16):
            other.hp+=round(other.maxhp/16)   
    #HAIL DAMAGE
    if field.weather =="Hail" and self.ability not in ["Snow Cloak","Ice Body","Overcoat","Slush Rush"] and self.item!="Safety Googles" and self.hp>0:     
        if self.type1!="Ice" and self.type2!="Ice" and self.ability!="Magic Guard":
            self.hp-=round(self.maxhp/16)
            print(f" ❄️ {self.name} is pelted by the hail!")
    #SAND DAMAGE
    if field.weather =="Sandstorm" and self.ability not in ["Sand Veil","Sand Force","Overcoat","Sand Rush"] and self.item!="Safety Googles" and self.hp>0:
        if self.type1 not in ["Rock","Ground","Steel"] and self.type2 not in ["Rock","Ground","Steel"] and self.ability!="Magic Guard":
            self.hp-=(1+round(self.maxhp/16))
            print(f" 🏜️ {self.name} is buffeted by the sandstorm!")
    #POISON
    if self.status=="Poisoned" and self.ability not in ["Magic Guard","Poison Heal","Immunity"] and self.hp>0:
        self.hp-=(1+round(self.maxhp/16))
        print(f" ☠️ {self.name} was hurt by poison.")
    #BADLY POISONED
    if self.status=="Badly Poisoned" and self.ability not in ["Magic Guard","Poison Heal","Toxic Boost","Immunity"] and self.hp>0:
        self.hp-=(1+(self.maxhp*self.toxicCounter/16))
        self.toxicCounter+=1
        print(f" ☠️ {self.name} was hurt by fatal poison.")        
    #BURN        
    if self.status=="Burned" and self.ability not in ["Magic Guard","Flare Boost"] and self.hp>0:
        self.hp-=(1+round(self.maxhp/16))
        print(f" 🔥 {self.name} was hurt by burn.")                
    if self.ability=="Pastel Veil" and self.status in ["Badly Poisoned","Poisoned"]:
        print(f" 🦄 {self.name}'s {self.ability}!")
        self.status="Alive"
    if self.gravendturn==turn:
        self.grav=False
    if self.vlendturn==turn:
        self.vldmg=False
    if self.cntendturn==turn:
        self.cntdmg=False
    if self.cnendturn==turn:
        self.cndmg=False
    if self.wfendturn==turn:
        self.wfdmg=False
    if self.magmaendturn==turn:
        self.magmadmg=False
    if self.infestation==turn or (self.infestation!=False and "Infestation" not in other.moves):
        self.infestation=False
        print(f" {self.name} is freed from the infestation.")
    if self.whirlpool==turn or (self.whirlpool!=False and "Whirlpool" not in other.moves):
        self.whirlpool=False
        print(f" {self.name} is freed from the whirlpool.")
    if self.firespin==turn or (self.firespin!=False and "Fire Spin" not in other.moves):
        self.firespin=False
        print(f" {self.name} is freed from the vortex of fire.")
    if tr.vcendturn==turn:
        tr.vcdmg=False
        print(" ⚠️ G-Max Volcalith ended on the opposing team!")
    if self.salty==True and other.ability!="Magic Guard":
        print(f" 🧂 {self.name} was hurt by salt cure!")
        if "Steel" in (self.type1,self.type2,self.teratype) or "Water" in (self.type1,self.type2,self.teratype):
            self.hp-=(self.maxhp/4)
        else:
            self.hp-=(self.maxhp/8)
    if tr.vcdmg==True and self.hp>0 and self.ability!="Magic Guard":
        print(f" 🪨 {self.name} is hurt by the rocks thrown out by G-Max Volcalith!")
        self.hp-=(self.maxhp/6)         
    if self.vldmg==True and self.hp>0 and self.ability!="Magic Guard":
        print(f" 🌿 {self.name} is hurt by G-Max Vine Lash’s ferocious beating!")
        self.hp-=(self.maxhp/6)
    if self.cntdmg==True and self.hp>0 and self.ability!="Magic Guard":
        print(f" ㊗️ {self.name} is hurt by G-Max Centiferno’s vortex!")       
        self.hp-=(self.maxhp/6) 
    if self.cndmg==True and self.hp>0 and self.ability!="Magic Guard":
        print(f" 🌊 {self.name} is hurt by G-Max Cannonade’s vortex!")
        self.hp-=(self.maxhp/6)
    if self.wfdmg==True and self.hp>0 and self.ability!="Magic Guard":
        print(f" 🔥 {self.name} is hurt by G-Max Wildlife’s flames!")
        self.hp-=(self.maxhp/6)
    if self.magmadmg==True and self.hp>0 and "Magma Storm" in other.moves and self.ability!="Magic Guard":
        print(f" 🌋 {self.name} was hurt by Magma Storm!")
        if other.item!="Binding Band":
            self.hp-=(self.maxhp/8)
        if other.item=="Binding Band":
            self.hp-=(self.maxhp/6)
    if self.bullrush==True:
        self.bullrush=False
    if self.name=="Mega Kangaskhan":
        self.ability="Parental Bond"
    if self.olock is True:
        defchange(self,other,-0.5)
        spdefchange(self,other,-0.5)
    if self.ability=="Speed Boost" and self.hp>0:
        print(f" {self.name}'s {self.ability}!")
        speedchange(self,other,0.5)
    if self.infestation!=0 and self.hp>0 and self.ability!="Magic Guard":
        print(f" 🦗 {self.name} is hurt by the infestation!")        
        self.hp-=(self.maxhp/16)   
    if self.whirlpool!=0 and self.hp>0 and self.ability!="Magic Guard":
        print(f" 🌪️ {self.name} is hurt by the whirlpool!")        
        self.hp-=(self.maxhp/16)   
    if self.firespin!=0 and self.hp>0 and self.ability!="Magic Guard":
        print(f" 🔥 {self.name} is hurt by the vortex of fire!")
        self.hp-=(self.maxhp/16)        
    if 0 in self.pplist:
        if self.dmax is False and self.use in self.moves:
            self.lostmoves.append(self.moves[self.pplist.index(0)])
            self.moves.remove(self.moves[self.pplist.index(0)])
        if self.dmax is True and self.use in self.maxmove:
            self.moves.remove(self.moves[self.pplist.index(0)])
            self.maxmove.remove(self.maxmove[self.pplist.index(0)])
        self.pplist.remove(0)     
    if self.status!="Alive" and self.ability in ["Purifying Salt","Good as Gold"]:
        print(f" {self.name}'s {self.ability}!")
        self.status="Alive"
    if self.dmax is True and turn==self.maxend:
        self.dmax=False
        prdx=["Great Tusk","Sandy Shocks","Roaring Moon","Brute Bonnet","Slither Wing","Flutter Mane","Scream Tail","Iron","Unbound","Tapu","Black","White","Attack","Defense","Speed","Hero","Alolan","Hisuian","Galarian","Dusk Mane","Dawn Wing","Black","White","Ice Rider","Shadow Rider"]
        di=["Single","Rapid"]
        x=1
        for i in di:
            if i in self.name:
                x=3
        for i in prdx:
            if i in self.name:
                x=2
        if x==3:
            self.name=self.name[11:]
        if x==2:
            self.name=self.name[8:]
        else:
            self.name=self.name.split(" ")[-1]
        self.hp=round(self.hp/2)
        self.maxhp=round(self.maxhp/2)
        print(f" 🔻 {self.name} returned to it's normal state!")
    if self.item =="None" and other.item !="None" and self.ability=="Pick Pocket":
        self.item=other.item
        other.item+="None"       
#FLINCH RESET    
    self.flinched=False
#DRY SKIN            
    if field.weather in ["Sunny","Desolate Land"]:
        if self.ability=="Dry Skin" and self.hp>0:
            print(f" {self.name}'s {self.ability}!")
            self.hp-=round(self.maxhp/8)
    if field.weather in ["Rainy","Primordial Sea"]:
        if self.ability in ["Dry Skin","Rain Dish"]:
            print(f" {self.name}'s {self.ability}!")
            self.hp+=round(self.maxhp/8)  
        if self.hp>self.maxhp:
            self.hp=self.maxhp       
#ICE BODY            
    if field.weather in ["Hail","Snowstorm"]:
        if self.ability=="Ice Face" and "Noice" in self.name:
            print(f" 🐧 {self.name}'s {self.ability}!")
            self.name="Eiscue"
            per=self.hp/self.maxhp
            self.weight=196.2
            self.hp=75
            self.atk=100
            self.defense=110
            self.spatk=45
            self.spdef=90
            self.speed=50
            self.calcst()
            self.hp=self.maxhp*per
        if self.ability=="Ice Body" and self.hp>0 and self.hp<self.maxhp:
            print(f" ❄️ {self.name}'s {self.ability}!")
            self.hp+=round(self.maxhp/8)        
        if self.hp>self.maxhp:
            self.hp=self.maxhp           
    #LEFTOVERS        
    if self.hp>0 and self.item=="Leftovers" and self.hp<self.maxhp:
        print(f" 🍎 {self.name} restored a little HP using its Leftovers.")
        self.hp+=round(self.maxhp/16)
    if self.hp>0 and self.aring==True and self.hp<self.maxhp:
        print(f" 💦 {self.name} restored a little HP using its Aqua Ring.")
        if self.item=="Big Root":
            self.hp+=(round(self.maxhp/16)*1.3)
        else:
            self.hp+=round(self.maxhp/16)
#GRASSY TERRAIN    
    if self.hp>0 and field.terrain =="Grassy" and self.hp<self.maxhp and (self.ability not in ["Levitate"] and "Flying" not in (self.type1,self.type2,self.teratype) or self.grav is True):
        print(f" 🌿 {self.name}'s HP was restored.")
        self.hp+=round(self.maxhp/16)
        if self.hp>self.maxhp:
            self.hp=self.maxhp         
    #BLACK SLUDGE        
    if self.hp>0 and self.item=="Black Sludge" and self.hp<self.maxhp:
        if self.type1=="Poison" or self.type2=="Poison":
            print(f" ☠️ {self.name} restored a little HP using its Black Sludge.")
            self.hp+=(1+round(self.maxhp/16))
        elif self.type1!="Poison" and self.type2!="Poison":   
            print(f" ☠️ {self.name} lost a little HP using its Black Sludge.")
            self.hp-=(1+round(self.maxhp/8))
    #POISON HEAL        
    if self.hp>0 and self.ability=="Poison Heal" and self.hp!=self.maxhp and self.status in ["Badly Poisoned","Poisoned"]:
        print(f" 🟣 {self.name} restored a little HP using its Poison Heal.")
        self.hp+=round(self.maxhp/8)
    if self.hp>self.maxhp:
        self.hp=self.maxhp
    if self.hp<0:
        self.hp=0