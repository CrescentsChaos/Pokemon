from trainerlistx import *
from moves import *
from quotes import *
pkball=random.choice(["Poké Ball","Great Ball","Ultra Ball","Net Ball","Quick Ball","Master Ball","Beast Ball","Dive Ball","Nest Ball","Repeat Ball","Timer Ball","Cherish Ball","Dream Ball","Dusk Ball","Fast Ball","Heal Ball","Heavy Ball","Level Ball","Love Ball","Lure Ball","Luxury Ball","Moon Ball","Park Ball","Premier Ball","Safari Ball"])
allmove=list(set(typemoves.firemoves+typemoves.watermoves+typemoves.electricmoves+typemoves.grassmoves+typemoves.normalmoves+typemoves.darkmoves+typemoves.ghostmoves+typemoves.psychicmoves+typemoves.poisonmoves+typemoves.steelmoves+typemoves.fairymoves+typemoves.bugmoves+typemoves.fightingmoves+typemoves.flyingmoves+typemoves.icemoves+typemoves.rockmoves+typemoves.groundmoves+typemoves.dragonmoves+typemoves.statusmove)-set(typemoves.zmoves+typemoves.maxmovelist))
#n=0
#for i in allmove:
#    n+=1
#    print(str(n)+"."+i)
nondmgmove=typemoves.statusmove+typemoves.buffmove+["Stealth Rock","Toxic","Toxic Spikes","Sticky Web","Trick Room"]
premove=["Solar Beam","Meteor Beam","Skull Bash","Geomancy","Phantom Force","Shadow Force","Sky Attack","Ice Burn","Freeze Shock","Solar Blade","Bounce"]
def faint(self,other,tr,optr,field,turn):
    if self.hp<=0:
        self.hp=0
        self.status="Fainted"
        name=self.name
        if self.dmax is True:
            self.dmax=False
            nn=-1
            prdx=["Great Tusk","Sandy Shocks","Roaring Moon","Brute Bonnet","Slither Wing","Flutter Mane","Scream Tail","Iron"]
            for i in prdx:
                if i in self.name:
                    nn=-2
            if nn==-1:
                name=self.name.split(" ")[-1]
            if nn==-2:
                name=name[8:]
            print(f" 🔻 {name} returned to it's normal state!")
            self.name=name
        if "Mega " in self.name:
            name=self.name.split(" ")[-1]
            if "Mewtwo" in self.name:
                name="Mewtwo"
            if "Charizard" in self.name:
                name="Charizard"
            print(f" 🧬 {name} returned to it's normal state!")
            self.name=name
        print(f" \n 🏁 Refree: {self.name} is unable to battle!")
        print(f"  😵😵‍💫 {tr.name}'s {self.name} fainted!\n")
        if other.ability=="Battle Bond" and "Ash" not in other.name and other.dmax==False:
            print(f" {other.name}'s {other.ability}.")
            if "Ash" not in other.name and "Greninja" in other.name:
                other.name="Ash Greninja"
                print(f" {other.name} synced with its tr's bond and transformed!")
                per=other.hp/other.maxhp
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
            print(f" 💗 {other.name}'s {other.ability}!")
            spatkchange(other,self,0.5)
        
        if self.ability =="Aftermath":
            print(f" 🕜 {self.name}'s {self.ability}.")
            other.hp-=other.maxhp/4
        if other.ability=="Moxie":
            print(f" ⏫ {other.name}'s {other.ability}!")
            atkchange(other,self,0.5)
            
        if other.ability=="As One" and "Ice Rider" in other.name:
            print(f" 🏇 {other.name}'s {other.ability}.")
          
            atkchange(other,self,0.5)       
        if other.ability=="As One" and "Shadow Rider" in other.name:
            print(f" 🏇 {other.name}'s {other.ability}.")
            
            spatkchange(other,self,0.5)        
        if other.ability=="Chilling Neigh" :
            print(f" 🥶 {other.name}'s {other.ability}.")
            
            atkchange(other,self,0.5)    
        if other.ability=="Grim Neigh" :
            print(f" 😱 {other.name}'s {other.ability}.")
            
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
        return self
def fchoice(pk,tr):
    if tr.ai is False:
        movelist(pk)
        choice=input(f" {tr.name}: Choose a move.\n >>")
        if choice in ["1","2","3","4","5","6"]:
            choice=int(choice)
            if (pk.item!="None" and ("Choice" in pk.item or pk.ability=="Gorilla Tactics")) and pk.choiced==False and pk.choicedmove=="None":
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
    resetboost(self,other)
    self.yawn=False
    self.aring=False
    self.atk=self.maxatk
    self.speed=self.maxspeed
    self.spatk=self.maxspatk
    self.spdef=self.maxspdef
    self.defense=self.maxdef
    self.badpoison=1
    self.perishturn=0
    self.priority=self.recharge=self.seeded=self.flinched=self.protect=other.protect=self.shelltrap=self.choiced=self.dbond=self.salty=False
    self.canfakeout=True 
    self.choicedmove="None"    
    if self.dmax is True:
        self.dmax=False
        nn=-1
        prdx=["Great Tusk","Sandy Shocks","Roaring Moon","Brute Bonnet","Slither Wing","Flutter Mane","Scream Tail","Iron","Unbound","Tapu","Black","White","Attack","Defense","Speed","Hero","Alolan","Hisuian","Galarian","Dusk Mane","Dawn Wing","Black","White"]
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
                movelist(trainer.pokemons[n-1])
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
   	    print(f" \n{self.name} is already in battle.")
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
        
#INTIMIDATE        
     
#Stance Change        
def stancechange(self,other,turn,field,used):    
    if used not in typemoves.statusmove and self.ability=="Stance Change" and self.sword!=True:
        self.shield=False
        self.sword=True
        print(f" {self.name}'s {self.ability}!")
        print(" 🗡️ Aegislash changed to it's blade forme.")
        self.name="Blade Aegislash"
        per=self.hp/self.maxhp
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
    if self.ability in ["Teravolt","Turboblaze","Propeller Tail"]:
        print(f" {self.name}'s {self.ability}!")
    if self.ability=="Mold Breaker":
        print(f" {self.name} breaks the mold!")
    if field.terrain=="Electric":
        if self.ability not in ["Levitate"] and self.type1!="Flying" and self.type2!="Flying" and self.status=="Sleep":
            self.status="Alive"
    if field.terrain=="Misty":
        if self.ability not in ["Levitate"] and self.type1!="Flying" and self.type2!="Flying":
            self.status="Alive"
    if other.ability=="Stench" and self.ability!="Long Reach":
        ch=random.randint(1,100)  
        if ch>90:
            print(f" 🤢 {other.name}'s {other.ability}!")
            self.flinched=True   
    if self.item=="King's Rock":
        ch=random.randint(1,100)
        if ch>90 and other.ability not in ["Inner Focus"]:
            other.flinched=True
    
    
#########ATTACK
def attack(self,other,tr,optr,used,opuse,field,turn):
    me=self
    they=other
    if self.roost!=False:
        if self.roost=="T1":
            self.type1="Flying"
        if self.roost=="T2":
            self.type2="Flying"
        if self.roost=="TR":
            self.teratype="Flying"
        self.roost=False
    
    if self.ability!="Parental Bond[Used]":
        print(f"\n {tr.name}:")
    preattackcheck(self,other,tr,optr,used,opuse,field,turn)
    hit=1
    canatk=True
    if self.choicedmove=="Struggle":
        used="Struggle"
    if self.confused is True:
        print(f" 😵‍💫 {self.name} is confused!")
        if turn>=self.confuseendturn or other.ability=="Oblivious":
            print(f" ‼️ {self.name} snapped out of confusion!")
            self.confused=False      
        ch=random.randint(1,100)  
        if ch>67 and self.dmax==False:
            canatk=False
            used="None"
            print(f" 😵  It hurt itself in confusion.")
            r=randroll()
            self.hp-=physical(self,self.level,self.atk,self.defense,base=40,a=1,r=r)
        else:
            canatk=True
    if self.status=="Paralyzed":
        ch=random.randint(1,100)
        if ch>75:
            canatk=False
            used="None"
            self.precharge=False
            print(f" ⚡ {self.name} is paralyzed and unable to move.")
        else:
            print(f" ⚡ {self.name} is paralyzed.")
            canatk=True
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
    if self.status=="Frozen":
        ch=random.randint(1,5)
        if ch==3:
            print(f" ‼️ {self.name} thawed out.")
            self.status="Alive"
        else:
            print(f" 🧊 {self.name} is frozen solid.")
            used="None"    
    
    if self.flinched==True and self.dmax is False:
            self.precharge=False
            print(f" 😧 {self.name} flinched and couldn't move.")
            self.flinched=False
            used="None"
    if self.use!="None" and used=="Gigaton Hammer" and self.use=="Gigaton Hammer":
        used="None"
        print(" ❌ Cannot use Gigaton Hammer consecutively!")      
    if self.fmove==True and self.status!="Sleep" and canatk==True:
        used=list(set(self.moves).intersection(["Outrage","Thrash","Petal Dance","Raging Fury"]))[0]
########
    self.use=used 
    if used in typemoves.statusmove:
        self.atkcat="Status"
    if used!="None":
        stancechange(self,other,turn,field,used)
    if other.ability=="Good as Gold" and used in typemoves.statusmove and used not in ["Stealth Rock","Haze","Toxic Spikes","Protect","Spiky Shield","Baneful Bunker","King's Shield","Silk Trap"]+typemoves.healingmoves+typemoves.buffmove:
        print(f" {self.name}'s used {used}.")
        print(f" 🪙 {other.name}'s {other.ability}!")
        used="None"    
    if used=="Me First":
        print(f" 🙏 {self.name} used Me First!")
        if opuse!="None":
            if self.speed>other.speed:
                self.atk*=1.5
                self.spatk*=1.5
                used=opuse
            else:
                print(f" It failed!")
    if used=="Assist":
        print(f" 🤝 {self.name} used Assist!")
        pmoves=[]
        for i in tr.pokemons:
            if i!=self:
                pmoves+=i.moves
                used=random.choice(pmoves)            
    if optr.wishhp is not False and other.speed<self.speed:
        print(f" 🌠 {other.name}'s wish came true!")
        other.hp+=optr.wishhp
        optr.wishhp=False
    if tr.wishhp is not False:
        print(f" 🌠 {self.name}'s wish came true!")
        self.hp+=tr.wishhp
        tr.wishhp=False
    if self.status=="Comatose":
        self.status="Drowsy"
    if self.ability=="Prankster" and "Dark" in (other.type1,other.type2,other.teratype) and used in typemoves.statusmove:
        used="None"
        print(f" {other.name} is immune to {self.name}'s Prankster!")
    if self.choiced is True and self.dmax is False:
        if (self.choicedmove in self.moves and self.dmax is False) and self.status!="Sleep" and self.flinched==False and canatk is True:
            used=self.choicedmove
            self.use=used
        else:
            self.choicedmove="Struggle"
            used="Struggle"
    if self.encore is not False and self.dmax is False:
        if turn==self.enendturn:    
            self.encore=False
        elif self.encore in self.moves:
            used=self.encore
        else:
            used="Struggle"
    
    if used in typemoves.bulletmove and other.ability=="Bulletproof":
        print(" {other.name}'s {other.ability}!")
        used="None"
    if used in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads"]:
        if other.ability=="Fluffy":
            self.atk/=2
    if used not in typemoves.statusmove:
        other.atkby=self.name
        other.atktime+=1
    if other.ability=="Disguise" and other.abilityused==False and used not in typemoves.statusmove+typemoves.buffmove+typemoves.zmoves+typemoves.multimove+typemoves.abilityigmoves and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"]:
        print(f" {self.name} used {used}!")
        print(f" 🥸 {other.name}'s {other.ability}!")     
        print(f" {other.name}'s disguise was busted!")
        other.hp-=round(other.maxhp/8)
        used="None"
        other.ability="Disguise[Used]"
    if used!="Destiny Bond" and "Destiny Bond" in self.moves:
        other.dbond=False
    if opuse in typemoves.buffmove and used in typemoves.protectmoves:
        print(f" {self.name} used {used}!")
        used="None"
        print(" It failed!")
    if self.dmax is False:
        moves=self.moves
    if self.dmax is True:
        #print(self.maxmove)
        moves=self.maxmove
#    print(used)
    pp=1
    if other.ability=="Pressure":
        pp=2
    if self.dmax is False and canatk is True:
        if len(self.moves)==0 and self.status not in ("Sleep"):
            used="Struggle"
    if used=="Metronome":
        print(f" 🎲 {self.name} used Metronome!")
        x=set(allmove)-set(typemoves.zmoves)-set(typemoves.maxmovelist)
        x=list(x)
        used=random.choice(x)
        print(f" Metronome turned into {used}!")
    if self.precharge==True and len(self.moves)>0 and "Geomancy" not in self.moves and self.status!="Sleep" and canatk==True:
        l=list(set(self.moves).intersection(premove))
        if len(l)!=0:
            used=l[0]
    if (field.terrain=="Psychic" or other.ability in ["Dazzling","Queenly Majesty","Armor Tail"]) and used in typemoves.prioritymove:
        if field.terrain!="Psychic":
            print(f" {other.name}'s {other.ability}.")
        used="None"
        print("  🚳 Cannot use priority moves!")
    
    before=other.hp
    sbefore=self.hp
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
    if self.ability=="Hustle" and self.dmax is False and used not in typemoves.noaccuracy:
        ch=random.randint(1,self.accuracy)
        if ch<20:
            print(f" {self.name}'s {self.ability}.")
            print(f" {self.name} used {used}!")
            print(f" {other.name} avoided the attack({used}).")
            used="None"
    if opuse in ["Phantom Force","Shadow Force","Sky Attack","Bounce"] and other.precharge==True and used not in premove and self.precharge==False and used not in typemoves.buffmove:
        print(f" {self.name} used {used}!")
        print(f" {other.name} avoided the attack({used}).")
        used="None"
    if other.item=="Bright Powder":
        ch=random.randint(1,self.accuracy)
        if ch<10:
            print(f" {self.name} used {used}!")
            print(f" {other.name} avoided the attack({used}).")
            used="None"
#SNOW CLOAK
    if other.ability=="Snow Cloak" and field.weather in ["Hail","Snowstorm"] and used not in typemoves.noaccuracy:
        ch=random.randint(1,self.accuracy)
        if ch<25:
            print(f" {other.name}'s {other.ability}.")
            print(f" {self.name} used {used}!")
            print(f" {other.name} avoided the attack({used}).")
            used="None"
#SAND VEIL            
    if other.ability=="Sand Veil" and field.weather=="Sandstorm" and used not in typemoves.noaccuracy:
        ch=random.randint(1,self.accuracy)
        if ch<25:
            print(f" {other.name}'s {other.ability}.")
            print(f" {self.name} used {used}!")
            print(f" {other.name} avoided the attack({used}).")
            used="None"
#######
    if turn==other.taunturn:
        print(f" {other.name}'s taunt ended!")
    if turn==other.encturn:
        print(f" {other.name}'s encore ended!")
    if used in moves or used not in moves:
#        print(used)
        if self.taunted==True and used in typemoves.statusmove:
            if self.item=="Mental Herb":
                self.taunted=False
                self.item+="[Used]"
            else:
                print(f" 🎭 Cannot use non-damaging moves while taunted.")
                used="None"
        if self.item=="Assault Vest" and used in typemoves.statusmove:
            print(f" 🦺 Cannot use status moves while holding an Assault Vest.")
            used="None"
        if used not in ["Protect","Spiky Shield","King's Shield","Baneful Bunker","Obstruct"]:
            self.protect=False
        if self.precharge==True and "Geomancy" in self.moves:
            print(f" 🌈 {self.name} used "+colored(" Geomancy","magenta")+"!")
            spatkchange(self,other,1)     
            spdefchange(self,other,1)   
            speedchange(self,other,1)
        
            self.precharge=False
            used="None"
        if self.recharge==True:
            print(f" {self.name} is recharging.")
            self.recharge=False
            used="None"
        elif self.protect=="Pending" and used in ["Protect","Spiky Shield","King's Shield","Baneful Bunker","Obstruct"]:
            print(f" 🛡️ {self.name} used {used}!")
            print("  It failed.")
            self.protect=False
            used="None"
        if other.protect==True and other.dmax is True and used not in typemoves.buffmove and used not in ["G-Max One Blow","G-Max Rapid Flow"]:
            print(f" 🛡️ {other.name} protected itself from {self.name}'s {used}.")
            other.protect="Pending"
            used="None"
            if used in ["Protect","Spiky Shield","King's Shield","Baneful Bunker"]:
                print(f" 🛡️ {self.name} used {used}!")
                used="None"
        if other.dmax is False and other.protect==True and used not in typemoves.buffmove and (self.ability not in ["Infiltrator","Unseen Fist"]  and used not in ["Shadow Force","Phantom Force","Hyperspace Fury","Hyper Drill","Hyperspace Hole"] and used not in typemoves.maxmovelist and used not in typemoves.zmoves):
            print(f" 🛡️ {other.name} protected itself from {self.name}'s {used}.")
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
                    self.status=["Badly Poisoned"]   
                    print(f" ☠️ {self.name} was badly poisoned.")  
        elif used=="Toxic":
            miss=random.randint(1,self.accuracy)
            if miss<10:
                print(f" {other.name} avoided the attack({used}).")
            else:
                toxic(self,other)
        elif used=="Thunder Wave":
            miss=random.randint(1,self.accuracy)
            if miss<15 and (self.type1!="Electric" and self.type2!="Electric"):
                print(f" {other.name} avoided the attack({used}).")
            else:
                thunderwave(self,other)
        elif used=="Sucker Punch":
            if opuse in nondmgmove or opuse =="None":
                print("  It failed.")
            else:
                suckerpunch(self,other)
        elif used=="Will-O-Wisp":
            miss=random.randint(1,self.accuracy)
            if miss<15 and (self.type1!="Fire" and self.type2!="Fire"):
                print(f" {other.name} avoided the attack({used}).")
            else:
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
            print(f" 🤌 {self.name} used "+ colored(" Taunt","white")+"!")
            if other.taunted==True:
                print(" It failed.")
            if other.taunted==False:
                other.taunted=True
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
            print(f" 🌙 {self.name} used "+colored(" Lunar Dance","magenta")+"!")
            self=faint(self,other,tr,optr,field,turn)
            if self.hp<self.maxhp:
                print(f" {self.name}'s HP was restored and status was cured!")
            self.hp=self.maxhp
            self.status="Alive"
        elif used=="Healing Wish":
            self.hp=0
            print(f" {self.name} used "+colored(" Healing Wish","magenta")+"!")
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
            swagger(self,other)
        elif used=="Feather Dance":
            featherdance(self,other)
        elif used=="Fake Tears":
            faketears(self,other)
        elif used=="Tri Attack":
            triattack(self,other)
        elif used=="Growth":
            growth(self,other)
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
                swordsdance(other)
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
            for i in range(3):
                triplearrows(self,other)
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
            print(f" 🔄 {self.name} used "+colored(" Teleport","magenta")+"!")
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
            miss=random.randint(1,self.accuracy)
            if miss<50:
                print(f" {other.name} avoided the attack({used}).")
            else:
                inferno(self,other)
        elif used=="Fleur Cannon":
            miss=random.randint(1,self.accuracy)
            if miss<10:
                print(f" {other.name} avoided the attack({used}).")
            else:
                fleurcannon(self,other)                
        elif used=="Overheat":
            miss=random.randint(1,self.accuracy)
            if miss<10:
                print(f" {other.name} avoided the attack({used}).")
            else:
                overheat(self,other)
        elif used=="Roar":
            print(f" 🐯 {self.name} used "+colored(" Roar","white")+"!")
            if len(optr.pokemons)>1 and other.ability!="Suction Cups":
                resetboost(other,self)
                l=other
                while True:
                    other=random.choice(optr.pokemons)
                    if other!=l:
                        break
                print(f" {other.name} was dragged out!")
                entryeff(other,self,optr,tr,field,turn)
        elif used=="Whirlwind":
            print(f" 🌪️ {self.name} used "+colored(" Whirlwind","white")+"!")
            print(f" {other.name} blew away with the wind.")
            if len(optr.pokemons)>1 and other.ability!="Suction Cups":
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
            miss=random.randint(1,self.accuracy)
            if miss<25:
                print(f" {other.name} avoided the attack({used}).")
            else:
                lovelykiss(self,other,turn)
        elif used=="Sleep Powder":
            miss=random.randint(1,self.accuracy)
            if miss<25:
                print(f" {other.name} avoided the attack({used}).")
            else:
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
            if field.weather in ["Hail","Snowstorm"]:
                blizzard(self,other)
            if field.weather not in ["Hail","Snowstorm"]:
                miss=random.randint(1,self.accuracy)
                if miss<30:
                    print(f" {other.name} avoided the attack({used}).")
                elif miss>=30:
                    blizzard(self,other)
        elif used=="Air Slash":
            miss=random.randint(1,self.accuracy)
            if miss<5:
                print(f" {other.name} avoided the attack({used}).")
            else:
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
            miss=random.randint(1,self.accuracy)
            if miss<50:
                print(f" {other.name} avoided the attack({used}).")
            else:
                zapcannon(self,other)
        elif used=="Freeze-Dry":
            freezedry(self,other)
        elif used=="Ice Fang":
            icefang(self,other)
        elif used=="Coil":
            coil(self,other)
        elif used=="Dual Chop":
            for i in range(2):
                dualchop(self,other)
        elif used=="Dragon Darts":
            for i in range(2):
                dragondarts(self,other)
        elif used=="Dual Wingbeat":
            for i in range(2):
                dualwingbeat(self,other)
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
            for i in range(2):
                ironbash(self,other)
            print(f" It hit 2 time(s).")         
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
            for i in range(hit):
                populationbomb(self,other)
            print(f" It hit {hit} time(s).")    
        elif used=="Twin Beam":
            for i in range(2):
                twinbeam(self,other)
            print(f" It hit 2 time(s).")      
        elif used=="Gear Grind":
            for i in range(2):
                geargrind(self,other)    
            print(f" It hit 2 time(s).")    
        elif used=="Scale Shot":
            hit=random.randint(2,5)
            if self.item=="Loaded Dice":
                hit=random.randint(4,5)
            if self.ability=="Skill Link":
                print(f" {self.name}'s {self.ability}.")
                hit=5
            for i in range(hit):
                scaleshot(self,other)
            speedchange(self,self,0.5)       
            defchange(self,self,-0.5)
            print(f" It hit {hit} time(s).") 
        elif used=="Triple Dive":
            hit=3
            for i in range(hit):
                tripledive(self,other)
            print(f" It hit {hit} time(s).")
        elif used=="Bone Rush":
            hit=random.randint(3,5)
            if self.ability=="Skill Link":
                print(f" {self.name}'s {self.ability}.")
                hit=5
            if self.item=="Loaded Dice":
                hit=random.randint(4,5)
            for i in range(hit):
                bonerush(self,other)
            print(f" It hit {hit} time(s).")
        elif used=="Bullet Seed":
            hit=random.randint(3,5)
            if self.ability=="Skill Link":
                print(f" {self.name}'s {self.ability}.")
                hit=5
            if self.item=="Loaded Dice":
                hit=random.randint(4,5)
            for i in range(hit):
                bulletseed(self,other)
            print(f" It hit {hit} time(s).")
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
            miss=random.randint(1,self.accuracy)
            if miss<10:
                print(f" {other.name} avoided the attack({used}).")
            else:
                blazekick(self,other)
        elif used=="Crush Claw":
            crushclaw(self,other)
        elif used=="Lava Plume":
            lavaplume(self,other)
        elif used=="Hurricane":
            if field.weather == "Rainy" and field.weather =="Rainy":
                hurricane(self,other,turn)
            if field.weather =="Sunny" and field.weather == "Sunny":
                miss=random.randint(1,self.accuracy)
                if miss<50 and "No Guard" not in (self.ability,other.ability):
                    print(f" {other.name} avoided the attack({used}).")
                elif miss>=50 or "No Guard" in (self.ability,other.ability):
                    hurricane(self,other,turn)
            elif field.weather != "Rainy" and field.weather !="Rainy":
                miss=random.randint(1,self.accuracy)
                if miss<30 and "No Guard" not in (self.ability,other.ability):
                    print(f" {other.name} avoided the attack({used}).")
                elif miss>=30 or "No Guard" in (self.ability,other.ability):
                    hurricane(self,other,turn)
          
        elif used=="Sky Uppercut":
            miss=random.randint(1,self.accuracy)
            if miss<10:
                print(f" {other.name} avoided the attack({used}).")
            else:
                skyuppercut(self,other)
        elif used=="Precipice Blades":
            miss=random.randint(1,self.accuracy)
            if miss<15:
                print(f" {other.name} avoided the attack({used}).")
            else:
                precipiceblades(self,other)
        elif used=="Origin Pulse":
            miss=random.randint(1,self.accuracy)
            if miss<15:
                print(f" {other.name} avoided the attack({used}).")
            else:
                originpulse(self,other)
        elif used=="Sheer Cold":
            miss=random.randint(1,self.accuracy)
            if miss<70:
                print(f" {other.name} avoided the attack({used}).")
            else:
                sheercold(self,other)
        elif used=="Fissure":
            miss=random.randint(1,self.accuracy)
            if miss<70:
                print(f" {other.name} avoided the attack({used}).")
            else:
                fissure(self,other)
        elif used=="Guillotine":
            miss=random.randint(1,self.accuracy)
            if miss<70:
                print(f" {other.name} avoided the attack({used}).")
            else:
                guillotine(self,other)
        elif used=="Horn Drill":
            miss=random.randint(1,self.accuracy)
            if miss<70:
                print(f" {other.name} avoided the attack({used}).")
            else:
                horndrill(self,other)      
        elif used=="Dragon Rush":
            miss=random.randint(1,self.accuracy)
            if miss<25:
                print(f" {other.name} avoided the attack({used}).")
            else:
                dragonrush(self,other)          
        elif used=="Draco Meteor":
            miss=random.randint(1,self.accuracy)
            if miss<10:
                print(f" {other.name} avoided the attack({used}).")
            else:
                dracometeor(self,other)
        elif used=="Psycho Boost":
            miss=random.randint(1,self.accuracy)
            if miss<10:
                print(f" {other.name} avoided the attack({used}).")
            else:
                psychoboost(self,other)
        elif used=="Drill Run":
            miss=random.randint(1,self.accuracy)
            if miss<5:
                print(f" {other.name} avoided the attack({used}).")
            else:
                drillrun(self,other)
        elif used=="Head Smash":
            miss=random.randint(1,self.accuracy)
            if miss<15:
                print(f" {other.name} avoided the attack({used}).")
            else:
                headsmash(self,other)
        elif used=="Flash Cannon":
            flashcannon(self,other)
        elif used=="Toxic Spikes":
            print(f" ☠️ {self.name} used "+colored("Toxic Spikes","magenta")+".")
            if optr.hazard.count(" Toxic Spikes")<3 and other.ability!="Magic Bounce":
                print(" ☠️ Poison spikes were scattered all around the opposing team!")
                optr.hazard.append("Toxic Spikes")
            if tr.hazard.count("Toxic Spikes")<3 and other.ability=="Magic Bounce":
                print(f" {other.name} bounced back the Toxic Spikes!")
                print(" ☠️ Poison spikes were scattered all around your team!")
                tr.hazard.append("Toxic Spikes")
            if tr.hazard.count("Toxic Spikes")==3:
                print(" Nothing happened!")
        elif used=="Spikes":
            print(f" ✴️ {self.name} used "+colored(" Spikes","yellow")+"!")
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
            print(f" 🪨 {self.name} used "+colored(" Stealth Rock","yellow")+"!")
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
            print(f" {self.name} used "+colored(" Sticky Web","green")+"!")
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
                print("  It failed!")
            else:
                softboiled(self,other)
        elif used=="Heal Order":
            if self.hp==self.maxhp:
                print("  It failed!")
            else:
                healorder(self,other)
        elif used=="Slack Off":
            if self.hp==self.maxhp:
                print("  It failed!")
            else:
                slackoff(self,other)
        elif used=="Roost":
            if self.hp==self.maxhp:
                print("  It failed!")
            else:
                roost(self,other)
        elif used=="Recover":
            if self.hp==self.maxhp:
                print("  It failed!")
            else:
                recover(self,other)
            
        elif used=="Spiky Shield":
            self.protect=True
            print(f" 🔰 {self.name} used "+colored(" Spiky Shield","green")+"!")
        elif used=="Baneful Bunker":
            self.protect=True
            print(f" ⛺ {self.name} used "+colored(" Baneful Bunker","magenta")+"!")
        elif used=="Silk Trap":
            self.protect=True
            print(f" 🕸️ {self.name} used "+colored(" Silk Trap","magenta")+"!")
        elif used=="Protect":
            self.protect=True
            print(f" 🛡️ {self.name} used "+colored(" Protect","white")+"!")
        elif used=="Max Guard":
            self.protect=True
            print(f" 🔺🛡️ {self.name} used "+colored(" Max Guard","white")+"!")
        elif used=="King's Shield":
            self.protect=True
            print(f" 👑🛡️ {self.name} used "+colored(" King's Shield","white")+"!")
        elif used=="Morning Sun":
            if self.hp==self.maxhp:
                print("  It failed!")
            else:
                morningsun(self,other)
        elif used=="Moonlight":
            if self.hp==self.maxhp:
                print("  It failed!")
            else:
                moonlight(self,other)
        elif used=="Megahorn":
            miss=random.randint(1,self.accuracy)
            if miss<15:
                print(f" {other.name} avoided the attack({used}).")
            else:
                megahorn(self,other)
        elif used=="Leaf Storm":
            miss=random.randint(1,self.accuracy)
            if miss<10:
                print(f" {other.name} avoided the attack({used}).")
            else:
                leafstorm(self,other)
        elif used=="Leaf Tornado":
            miss=random.randint(1,self.accuracy)
            if miss<10:
                print(f" {other.name} avoided the attack({used}).")
            else:
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
                print(" It Failed!")
            if tr.lightscreen==False:
                lightscreen(self,other,tr,turn)
        elif used=="Calm Mind":
            calmmind(self,other)
        elif used=="Aurora Veil":
            if tr.auroraveil==True:
                print(" It failed!")
            if tr.auroraveil==False:
                auroraveil(self,other,tr,turn)
        elif used=="Tailwind":
            if tr.tailwind==True:
                print(" It failed!")
            if tr.tailwind==False:
                tailwind(self,other,tr,turn)
        elif used=="Reflect":
            if tr.reflect==True:
                print(" It failed!")
            if tr.reflect==False:
                reflect(self,other,tr,turn)
        elif used=="Acid Armor":
            acidarmor(self,other)
        elif used=="Aeroblast":
            miss=random.randint(1,self.accuracy)
            if miss<5:
                print(f" {other.name} avoided the attack({used}).")
            else:
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
            miss=random.randint(1,self.accuracy)
            if miss<10:
                print(f" {other.name} avoided the attack({used}).")
            else:
                heatwave(self,other)
        elif used=="Slash":
            slash(self,other)
        elif used=="Night Slash":
            nightslash(self,other)
        elif used=="Psycho Cut":
            psychocut(self,other)
        elif used=="Sacred Fire":
            miss=random.randint(1,self.accuracy)
            if miss<5:
                print(f" {other.name} avoided the attack({used}).")
            else:
                sacredfire(self,other)
        elif used=="Brick Break":
            brickbreak(self,other,optr)
        elif used=="Rock Wrecker":
            miss=random.randint(1,self.accuracy)
            if miss<10:
                print(f" {other.name} avoided the attack({used}).")
            else:
                rockwrecker(self,other)
                if other.hp>0:
                    self.recharge=True            
        elif used=="Giga Impact":
            miss=random.randint(1,self.accuracy)
            if miss<10:
                print(f" {other.name} avoided the attack({used}).")
            else:
                gigaimpact(self,other)
                self.recharge=True
        elif used=="Meteor Assault":
            meteorassault (self,other)
            self.recharge=True
        elif used=="Cross Chop":
            miss=random.randint(1,self.accuracy)
            if miss<20 and "No Guard" not in (self.ability,other.ability):
                print(f" {other.name} avoided the attack({used}).")
            else:
                crosschop(self,other)
        elif used=="Hyper Beam":
            miss=random.randint(1,self.accuracy)
            if miss<10:
                print(f" {other.name} avoided the attack({used}).")
            else:
                hyperbeam(self,other)
                self.recharge=True
        elif used=="Roar of Time":
            miss=random.randint(1,self.accuracy)
            if miss<10:
                print(f" {other.name} avoided the attack({used}).")
            else:
                roaroftime(self,other)
                self.recharge=True
        elif used=="Spacial Rend":
            miss=random.randint(1,self.accuracy)
            if miss<5:
                print(f" {other.name} avoided the attack({used}).")
            else:
                spacialrend(self,other)
        elif used=="Phantom Force":
            miss=random.randint(1,self.accuracy)
            if miss>95:
                print(f" {other.name} avoided the attack({used}).")
            else:
                phantomforce(self,other)      
                   
        elif used=="Shadow Force":
            miss=random.randint(1,self.accuracy)
            if miss>95:
                print(f" {other.name} avoided the attack({used}).")
            else:
                shadowforce(self,other)   
                      
        elif used=="Iron Head":
            ironhead(self,other)
        elif used=="Iron Tail":
            miss=random.randint(1,self.accuracy)
            if miss>75:
                print(f" {other.name} avoided the attack({used}).")
            else:
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
            miss=random.randint(1,self.accuracy)
            if miss>90:
                print(f" {other.name} avoided the attack({used}).")
            else:
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
                if len(optr.pokemons)>1 and other.ability!="Suction Cups":
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
        elif used=="Mach Punch":
            machpunch(self,other)
        elif used=="Thunder":
            if field.weather in ["Rainy","Primordial Sea"] and field.weather in ["Rainy","Primordial Sea"]:
                thunder(self,other)
            else:
                miss=random.randint(1,self.accuracy)
                if miss>70:
                    print(f" {other.name} avoided the attack({used}).")
                elif miss<=70 or "No Guard" in (self.ability,other.ability):
                    thunder(self,other)
        elif used=="Scald":
            scald(self,other)
        elif used=="Egg Bomb":
            eggbomb(self,other)
        elif used=="Hex":
            hex (self,other)
        elif used=="First Impression":
            if self.canfakeout==False:
                print("  It failed!")
            if self.canfakeout==True:
                firstimpression(self,other)
                self.canfakeout=False
        elif used=="Fake Out":
            if self.canfakeout==False and self.ability!="Parental Bond[Used]":
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
            miss=random.randint(1,self.accuracy)
            if miss>90:
                print(f" {other.name} avoided the attack({used}).")
            else:
                aquatail(self,other)
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
            miss=random.randint(1,self.accuracy)
            if miss>90:
                print(f" {other.name} avoided the attack({used}).")
            else:
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
            for i in range(hit):
                armthrust(self,other)
        elif used=="Pin Missile":
            hit=random.randint(3,5)
            if self.ability=="Skill Link":
                print(f" {self.name}'s {self.ability}.")
                hit=5
            if self.item=="Loaded Dice":
                hit=random.randint(4,5)
            for i in range(hit):
                pinmissile(self,other)
            print(f" It hit {hit} time(s).")
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
            for i in range(hit):
                iciclespears(self,other)
            print(f" It hit {hit} time(s).")
        elif used=="Waterfall":
            waterfall(self,other)
        elif used=="Wood Hammer":
            woodhammer(self,other)
        elif used=="Energy Ball":
            energyball(self,other)
        elif used=="Rest":
            if self.hp==self.maxhp:
                print("  It failed!")
            else:
                rest(self,other,turn)
        elif used=="Bulk Up":
            bulkup(self,other)
        elif used=="Stone Edge":
            miss=random.randint(1,self.accuracy)
            if miss<10:
                print(f" {other.name} avoided the attack({used}).")
            else:
                stoneedge(self,other)
        elif used=="Steel Wing":
            steelwing(self,other)
        elif used=="Focus Blast":
            miss=random.randint(1,self.accuracy)
            if miss<30:
                print(f" {other.name} avoided the attack({used}).")
            else:
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
            miss=random.randint(1,self.accuracy)
            if miss<10:
                print(f" {other.name} avoided the attack({used}).")
            else:
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
            miss=random.randint(1,self.accuracy)
            if miss<50 and self.ability!="No Guard":
                print(f" {other.name} avoided the attack({used}).")
            if miss>=50 or "No Guard" in (self.ability,other.ability):
                dynapunch(self,other,turn)
        elif used=="Liquidation":
            liquidation(self,other)
        elif used=="Tera Blast":
            terablast(self,other)
        elif used=="Earthquake":
            earthquake(self,other)
        elif used=="Belch":
            miss=random.randint(1,self.accuracy)
            if miss<10:
                print(f" {other.name} avoided the attack({used}).")
            else:
                belch(self,other)
        elif used=="Gunk Shot":
            miss=random.randint(1,self.accuracy)
            if miss<20:
                print(f" {other.name} avoided the attack({used}).")
            else:
                gunkshot(self,other)
        elif used=="Freeze Shock":
            miss=random.randint(1,self.accuracy)
            if miss<10:
                print(f" {other.name} avoided the attack({used}).")
            else:
                freezeshock(self,other)                   
        elif used=="Ice Burn":
            miss=random.randint(1,self.accuracy)
            if miss<10:
                print(f" {other.name} avoided the attack({used}).")
            else:
                iceburn(self,other)                      
        elif used=="Blue Flare":
            miss=random.randint(1,self.accuracy)
            if miss<15:
                print(f" {other.name} avoided the attack({used}).")
            else:
                blueflare(self,other)     
        elif used=="Eternabeam":
            miss=random.randint(1,self.accuracy)
            if miss<10:
                print(f" {other.name} avoided the attack({used}).")
            else:
                eternabeam (self,other)   
                self.recharge=True                
        elif used=="Bolt Strike":
            miss=random.randint(1,self.accuracy)
            if miss<15:
                print(f" {other.name} avoided the attack({used}).")
            else:
                boltstrike(self,other)   
        elif used=="Thunder Cage":
            miss=random.randint(1,self.accuracy)
            if miss<10:
                print(f" {other.name} avoided the attack({used}).")
            else:
                thundercage(self,other)     
        elif used=="Mountain Gale":
            miss=random.randint(1,self.accuracy)
            if miss<15:
                print(f" {other.name} avoided the attack({used}).")
            else:
                mountaingale(self,other)       
        elif used=="Mystical Power":#isinstance(used,FireBlast)
            miss=random.randint(1,self.accuracy)
            if miss<10:
                print(f" {other.name} avoided the attack({used}).")
            else:
                mysticalpower(self,other)                
                                                
        elif used=="Fire Blast":#isinstance(used,FireBlast)
            miss=random.randint(1,self.accuracy)
            if miss<15:
                print(f" {other.name} avoided the attack({used}).")
            else:
                fireBlast(self,other)
            
        elif used=="Bounce":
            miss=random.randint(1,self.accuracy)
            if miss<15:
                print(f" {other.name} avoided the attack({used}).")
                self.precharge=False
            else:
                bounce(self,other)                 
        elif used=="Pyro Ball":
            miss=random.randint(1,self.accuracy)
            if miss<10:
                print(f" {other.name} avoided the attack({used}).")
            else:
                pyroball(self,other)     
                      
        elif used=="Meteor Beam":
            miss=random.randint(1,self.accuracy)
            if miss<10:
                print(f" {other.name} avoided the attack({used}).")
                self.precharge=False
            else:
                meteorbeam(self,other)                                
        elif used=="Psychic":
            psychic(self,other)
        elif used=="Seed Flare":
            miss=random.randint(1,self.accuracy)
            if miss<15:
                print(f" {other.name} avoided the attack({used}).")
            else:
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
            miss=random.randint(1,self.accuracy)
            if miss<20:
                print(f" {other.name} avoided the attack({used}).")
            else:
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
            hydrovortex(self,other)
            self.moves.remove(used)
        elif used =="Oceanic Operetta":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item+="[Used]"
            operetta(self,other)
            self.moves.remove(used)
        elif used =="Malicious Moonsault":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            moonsault(self,other)
            self.moves.remove(used)
        elif used =="Light That Burns The Sky":
            self.name=self.name.split("(")[0]
            if "Ultra" not in self.name:
                transformation(self,other,turn)
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            skyburn(self,other)
            self.item+="[Used]"
            self.moves.remove(used)
        elif used =="Let's Snuggle Forever":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item+="[Used]"
            snuggle(self,other)
            self.moves.remove(used)      
        elif used =="Extreme Evoboost":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item+="[Used]"
            exevoboost(self,other)
            self.moves.remove(used)      
        elif used =="Guardian of Alola":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item+="[Used]"
            goalola(self,other)
            self.moves.remove(used)
        elif used =="Stoked Sparksurfer":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item+="[Used]"
            sparksurf(self,other)
            self.moves.remove(used)
        elif used =="Clangorous Soulblaze ":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item+="[Used]"
            soulblaze(self,other)
            self.moves.remove(used)
        elif used =="Sinister Arrow Raid":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item+="[Used]"
            arrowraid(self,other)
            self.moves.remove(used)
        elif used =="Soul-Stealing 7-Star Strike":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item+="[Used]"
            soulstealing(self,other)
            self.moves.remove(used)
        elif used =="Menacing Moonraze Maelstrom":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item+="[Used]"
            menacingmoonrazemaelstrom(self,other)
            self.moves.remove(used)
        elif used =="Searing Sunraze Smash":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item+="[Used]"
            searingsunrazesmash(self,other)
            self.moves.remove(used)
        elif used =="Genesis Supernova":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item+="[Used]"
            genesissupernova(self,other,field,turn)
            self.moves.remove(used)
        elif used =="Pulverizing Pancake":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Snorlium-Z.")
            self.item+="[Used]"
            pulverizingpancake(self,other)
            self.moves.remove(used)
        elif used =="Splintered Stormshards":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Lycanium-Z.")
            self.item+="[Used]"
            stormshards(self,other)
            self.moves.remove(used)                
        elif used =="Inferno Overdrive":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Firium-Z.")
            self.item+="[Used]"
            infernooverdrive(self,other)
            self.moves.remove(used)
        elif used =="Bloom Doom":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Grassium-Z.")
            self.item+="[Used]"
            bloomdoom(self,other)
            self.moves.remove(used)
        elif used =="Gigavolt Havoc":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Electrium-Z.")
            self.item+="[Used]"
            gigavolthavoc(self,other)
            self.moves.remove(used)
        elif used =="Catastropika":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item+="[Used]"
            catastropika(self,other)
            self.moves.remove(used)
        elif used =="Pulverizing Pancake":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item+="[Used]"
            pulverizingpancake(self,other)
            self.moves.remove(used)
        elif used =="10,000,000 Volt Thunderbolt":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item+="[Used]"
            tenmvolttb(self,other)
            self.moves.remove(used)
        elif used =="Acid Downpour":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Poisonium-Z.")
            aciddownpour(self,other)
            self.moves.remove(used)
            self.item+="[Used]"
        elif used =="Breakneck Blitz":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Normalium-Z.")
            self.item+="[Used]"
            breakneckblitz(self,other)
            self.moves.remove(used)
        elif used =="All-Out Pummeling":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Fightinium-Z.")
            self.item+="[Used]"
            alloutpummeling(self,other)
            self.moves.remove(used)
        elif used =="Black Hole Eclipse":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Darkinium-Z.")
            self.item+="[Used]"
            blackholeeclipse(self,other)
            self.moves.remove(used)
        elif used =="Continental Crush":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Rockium-Z.")
            self.item+="[Used]"
            continentalcrush(self,other)
            self.moves.remove(used)
        elif used =="Tectonic Rage":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Groundium-Z.")
            self.item+="[Used]"
            tectonicrage(self,other)
            self.moves.remove(used)
        elif used =="Corkscrew Crash":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Steelium-Z.")
            self.item+="[Used]"
            corkscrewcrash(self,other)
            self.moves.remove(used)
        elif used =="Devastating Drake":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Dragonium-Z.")
            self.item+="[Used]"
            devastatingdrake(self,other)
            self.moves.remove(used)
        elif used =="Shattered Psyche":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Psychium-Z.")
            self.item+="[Used]"
            shatteredpsyche(self,other)
            self.moves.remove(used)
        elif used =="Never-ending Nightmare":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Ghostium-Z.")
            self.item+="[Used]"
            neverendingnightmare(self,other)
            self.moves.remove(used)
        elif used =="Supersonic Skystrike":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Flyinium-Z.")
            self.item+="[Used]"
            supersonicskystrike(self,other)
            self.moves.remove(used)
        elif used =="Savage Spin-Out":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Buginium-Z.")
            self.item+="[Used]"
            savagespinout(self,other)
            self.moves.remove(used)
        elif used =="Subzero Slammer":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Icium-Z.")
            self.item+="[Used]"
            subzeroslammer (self,other)
            self.moves.remove(used)
        elif used =="Twinkle Tackle":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Fairium-Z.")
            self.item+="[Used]"
            twinkletackle(self,other)
            self.moves.remove(used)
        elif used=="Counter":
           print(f" {self.name} used "+colored(" Counter","red")+"!")
           if other.atkcat=="Physical" and "Ghost" not in (other.type1,other.type2,other.teratype):
               other.hp-=self.dmgtaken*2
           else:
               print(" It failed.")
        elif used=="Mirror Coat":
           print(f" {self.name} used "+colored(" Mirror Coat","magenta")+"!")
           if other.atkcat=="Special" and "Dark" not in (other.type1,other.type2,other.teratype):
               other.hp-=self.dmgtaken*2
           else:
               print(" It failed.")
        else:
            pass
    if self.item=="Shell Bell" and other.dmgtaken>0:
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
    if other.item=="Focus Band" and used not in typemoves.multimove:
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
        if other.ability=="Phoenix Down" and other.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and used not in typemoves.abilityigmoves:
            print(f" 🌈 {other.name}'s Phoenix Down!")
            print(f" {other.name} revived itself to half of its HP.")
            other.hp=(other.maxhp/2)      
            other.ability="Phoenix Down[Used]"  
        if other.ability=="Sturdy" and other.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and used not in typemoves.abilityigmoves and used not in typemoves.multimove:
            print(f" {other.name}'s Sturdy!")
            print(f" {other.name} hung on using Sturdy.")
            other.hp=1
            
        if other.item=="Focus Sash" and used not in typemoves.multimove:
            print(f" {other.name} hung on using Focus Sash.")
            other.hp=1
            other.item+="[Used]"
    
    if other.hp!=before and used!="None":
        self.miss=False
    if other.hp==before and used=="None":
        self.miss=True
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
    if other.hp>0:
        if other.ability=="Weak Armor" and self.atkcat=="Physical":
            print(f" 🥜 {other.name}'s {other.ability}!")
            defchange (other,other,-0.5)
            speedchange (other,other,0.5)
        if other.hp<=(other.maxhp/2)  and before>(other.maxhp/2):
            if other.ability=="Anger Shell":
                print(f" 💢 {other.name}'s {other.ability}!")
                defchange(other,self,-0.5)
                spdefchange(other,self,-0.5)
                atkchange(other,self,0.5)
                spatkchange(other,self,0.5)
                speedchange(other,self,0.5)
            if other.ability=="Berserk":
                print(f" {other.name}'s {other.ability}!")
                spatkchange(other,self,0.5)
        if other.hp<=(other.maxhp/4)  and before>(other.maxhp/4):                
            if other.item in ["Aguav Berry","Figy Berry","Ipapa Berry","Mago Berry","Wiki Berry"]:
                other.hp+=round(other.maxhp/3)
                print(f" {other.name} consumed it's {other.item} and restored some HP!")
                if other.item=="Wiki Berry":
                    if other.nature in ["Adamant","Jolly","Careful","Impish"]:
                        confuse(other,other,turn,100)
                if other.item=="Ipapa Berry":
                    if other.nature in ["Lonely","Mild","Gentle","Hasty"]:
                        confuse(other,other,turn,100)
                if other.item=="Aguav Berry":
                    if other.nature in ["Naughty","Naive","Rash","Lax"]:
                        confuse(other,other,turn,100)
                if other.item=="Mago Berry":
                    if other.nature in ["Brave","Quiet","Sassy","Relaxed"]:
                        confuse(other,other,turn,100)
                if other.item=="Figy Berry":
                    if other.nature in ["Modest","Timid","Calm","Bold"]:
                        confuse(other,other,turn,100)
                other.item+="[Used]"
            if other.item=="Sitrus Berry":
                other.hp+=round(other.maxhp/4)
                print(f" {other.name} restored HP using its {other.item}!")
                other.item+="[Used]"        
    if self.hp!=sbefore and self==me and self.hp<sbefore and sper>0:
        print(f" Total damage received {sper}%")
    if used not in typemoves.statusmove:
        if other.item=="Rowap Berry" and other.atkcat=="Special" and self.hp!=sbefore:
          print(f" {other.name}'s {other.item} damaged {self.name}!")
          self.hp-=(other.maxhp/8)
          other.item+="[Used]"
        if other.item=="Kee Berry":
            print(f" {other.item} raised it's defense.")
            defchange(other,self,0.5)
            other.item+="[Used]"
        if other.ability=="Innards Out" and other==they and other.hp<=0:
            print(f" {other.name}'s Innards Out!")
            self.hp-=before
        if other.item=="Jacoba Berry" and other.atkcat=="Physical" and self.hp!=sbefore:
            print(f" {other.name}'s {other.item} damaged {self.name}!")
            self.hp-=round(self.maxhp/8)
            other.item+="[Used]"
    if self.item=="Throat Spray" and used in typemoves.soundmoves:
        spatkchange(self,other,0.5)
        print(f" The Throat Spray raised {self.name}'s Special Attack!")
        self.item+="[Used]"            
    if other.item=="Maranga Berry" and other.atkcat=="Special" and self.hp!=sbefore:
          print(f" {other.item} raised it's special defense.")
          spdefchange(other,self,0.5)
          other.item+="[Used]"
    if other.hp>0:
          if other.hp<=(other.maxhp/4)  and before>(other.maxhp/4):
              if other.item=="Starf Berry":
                  ss=random.randint(1,5)
                  if ss==1:
                      print(f" {other.item} sharply raised it's attack.")
                      atkchange(other,self,1)
                  if ss==2:
                      print(f" {other.item} sharply raised it's special attack.")
                      spatkchange(other,self,1)
                  if ss==3:
                      print(f" {other.item} sharply raised it's defense.")
                      defchange(other,self,1)
                  if ss==4:
                      print(f" {other.item} sharply raised it's special defense.")
                      spdefchange(other,self,1)
                  if ss==5:
                      print(f" {other.item} sharply raised it's speed.")
                      speedchange(other,self,1)
                      other.item+="[Used]"
              if other.item=="Custap Berry" and other.speed<self.speed:
                  print(f" {other.item} will let {other.name} move first!")
                  other.priority=True
                  other.item+="[Used]"
              if other.item=="Salac Berry":
                  print(f" {other.item} raised it's speed.")
                  speedchange(other,self,0.5)
                  other.item+="[Used]"
              if other.item=="Petaya Berry":
                  print(f" {other.item} raised it's special attack.")
                  spatkchange(other,self,0.5)
                  other.item+="[Used]"
              if other.item=="Liechi Berry":
                  print(f" {other.item} raised it's attack.")
                  atkchange(other,self,0.5)
                  other.item+="[Used]"
              if other.item=="Lansat Berry":
                  print(f" {other.item} raised it's critical hit ratio.")
                  other.critrate*=4
                  other.item+="[Used]"
              if other.item=="Ganlon Berry":
                  print(f" {other.item} raised it's defense.")
                  defchange(other,self,0.5)
                  other.item+="[Used]"
              if other.item=="Apicot Berry":
                  print(f" {other.item} raised it's special defense.")
                  spdefchange(other,self,0.5)
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
    if other.ability=="Gooey" and me.ability not in ["Clear Body","Good as Gold"] and me.ability!="Long Reach" and used in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads"] and other.hp!=before:
        print(f" 🐌 {other.name}'s {other.ability}!")     
        speedchange(self,other,-0.5)
    if other.ability=="Flame Body" and me.status=="Alive" and me.ability!="Long Reach" and used in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads"] and other.hp!=before:
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
    if other.ability in ["Mummy","Lingering Aroma","Wandering Spirit"] and me.ability!="Long Reach" and used in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads","Ability Shield"] and other.hp!=before:     
        print(f" {other.name}'s {other.ability}!")
        self.ability=other.ability   
    if other.ability=="Static" and me.status=="Alive" and me.ability!="Long Reach" and used in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads"] and other.hp!=before:
        paralyzed(other,self,30)
    if other.ability=="Poison Point" and me.status=="Alive" and me.ability!="Long Reach" and used in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads"]:
        poison(other,self,30)
    if self.ability=="Poison Touch" and other.status=="Alive" and other.ability!="Long Reach" and used in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads"]:
        poison(self,other,30)  
    if used in typemoves.contactmoves and other.item=="Air Balloon" and self.item not in ["Punching Glove","Protective Pads"] and used not in typemoves.groundmoves and other.hp!=before:
        print(f" 🎈 {other.name}'s Air Balloon popped off!")
        other.item+="[Used]"                      
    if other.hp!=before:
        if used not in typemoves.statusmove:
#ROUGH SKIN/IRON BARBS            
            if other.ability in ["Rough Skin","Iron Barbs"] and used in typemoves.contactmoves and self.ability!="Long Reach" and self.item not in ["Punching Glove","Protective Pads"]:
                print(f" ✴️ {me.name} was hurt by {other.name}'s {other.ability}!")
                me.hp-=round((me.maxhp/16),2)
                if me.hp<0:
                    me.hp=0
        if other.item=="Rocky Helmet" and self.ability!="Magic Guard" and used in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads"]:
            me.hp-=round(me.maxhp/6)
            print(f" 🪖 {me.name} was hurt by {other.name}'s Rocky Helmet!")
            if me.hp<0:
                me.hp=0      
        if len(optr.pokemons)>1 and other.item=="Eject Pack" and used in typemoves.statusmove:
            print(f" 🪂 {other.name} returned to it's {pkball}.")
            other.item+="[Used]"
            other=random.choice(optr.pokemons)
            entryeff(other,self,optr,tr,field,turn)  
        if len(tr.pokemons)>1 and other.item=="Red Card":
            other.item+="[Used]"
            print(f" 🟥 {self.name} returned to it's {pkball}.")
            self=switch(self,other,tr,optr,field,turn)
        if len(optr.pokemons)>1 and other.item=="Eject Button":
            print(f" 🔘 {other.name} returned to it's {pkball}.")
            other.item+="[Used]"
            other=random.choice(optr.pokemons)
            entryeff(other,self,optr,tr,field,turn)
#LIFE ORB                    
        if me.item=="Life Orb" and me.ability!="Magic Guard":
            me.hp-=round(me.maxhp/16)
            print(f" 🟣 {me.name} lost some of its HP!")
            if self.hp<0:
                self.hp=0
    if other.item=="Custap Berry" and other.speed<self.speed and self.hp<(self.maxhp/4) and self.hp>0:
        print(f" {other.item} will let {other.name} move first!")
        other.priority=True
        other.item+="[Used]"     
    if self.item=="Cheri Berry" and self.status=="Paralyzed" and self.hp>0:
        print(f" {self.item} cured {self.name}'s paralysis!")
        self.status="Alive"
        self.item+="[Used]"
    if self.item=="Rawst Berry" and self.status=="Burned" and self.hp>0:
        print(f" {self.item} cured {self.name} from burn!")
        self.status="Alive"
        self.item+="[Used]"
    if self.item=="Chesto Berry" and self.status=="Sleep" and self.hp>0:
        print(f" {self.item} cured {self.name} from sleep state!")
        print(f" {self.name} woke up!")
        self.status="Alive"
        self.item+="[Used]"
    if other.item=="Chesto Berry" and other.status=="Sleep" and other.hp>0:
        print(f" {other.item} cured {other.name} from sleep state!")
        print(f" {other.name} woke up!")
        other.status="Alive"
        other.item+="[Used]"
    if self.item=="Aspear Berry" and self.status=="Frozen" and self.hp>0:
        print(f" {self.item} cured {self.name} from frozen state!")
        print(f" {self.item} thawed out!")
        self.status="Alive"
        self.item+="[Used]"
    if other.item=="Aspear Berry" and other.status=="Frozen" and other.hp>0:
        print(f" {other.item} cured {other.name} from frozen state!")
        print(f" {other.item} thawed out!")
        other.status="Alive"
        other.item+="[Used]"
    if self.item=="Pecha Berry" and self.status=="Badly Poisoned" and self.hp>0:
        print(f" {self.item} cured {self.name}'s poison!")
        self.status="Alive"
        self.item+="[Used]"
    if other.item=="Pecha Berry" and other.status=="Badly Poisoned" and other.hp>0:
        print(f" {other.item} cured {other.name}'s poison!")
        other.status="Alive"
        other.item+="[Used]"
    if self.item=="Lum Berry" and self.status!="Alive"and self.hp>0:
        print(f" {self.item} cured {self.name}'s status condition!")
        self.status="Alive"
        self.item+="[Used]"        
    if other.item=="Lum Berry" and other.status!="Alive" and other.hp>0:
        print(f" {other.item} cured {other.name}'s status condition!")
        other.status="Alive"
        other.item+="[Used]"         
    if other.ability=="Stamina" and other.hp!=before and self.hp>0:
        print(f" {other.name}'s {other.ability}!")
        defchange(other,self,0.5)       
    if self.hp<self.maxhp/2 and self.hp>0:
        if self.item=="Sitrus Berry":       
            self.hp+=round(self.maxhp/4)
            print(f" {self.name} restored HP using its {self.item}!")
            self.item+="[Used]"    
    if other.ability=="Schooling" and "School" in other.name and other.hp<=(other.maxhp*0.25):
        print(f" 🐟 {other.name}'s {other.ability}!")
        other.name="Wishiwashi"
        per=other.hp/other.maxhp
        other.hp=55
        other.atk=20
        other.defense=20
        other.spatk=25
        other.spdef=25
        other.speed=40
        other.calcst()
        other.hp=other.maxhp*per
    return self,other
    
    
#EFFECTS
def effects(self,other,tr,turn):
    print("  ")
    self.flinched=False
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
    if self.fmove==True:
        self.fmoveturn-=1
        if self.fmoveturn==0:
            self.fmove=False
            confuse(self,self,turn,100)
    if self.perishturn!=0:
        self.perishturn-=1
        print(f" {self.name}'s perish count fell to {self.perishturn}!")
        if self.perishturn==0:
            self.hp=0
    if self.ability=="Power Construct" and "Complete" not in self.name and self.hp<=(self.maxhp/2) and self.hp>0:
        print(f" ⚕️ {self.name}'s Power Construct!")
        self.name="Complete Zygarde"
        print(f" 🧬 You sense the presence of many!\n Zygarde transformed into its Complete Forme!")
        per=self.hp/self.maxhp
        self.hp=216
        self.atk=100
        self.defense=91
        self.spatk=95
        self.spdef=85
        self.speed=85
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
    if field.weather =="Hail" and self.ability!="Snow Cloak" and self.item!="Safety Googles" and self.hp>0:     
        if self.type1!="Ice" and self.type2!="Ice" and self.ability!="Magic Guard":
            self.hp-=round(self.maxhp/16)
            print(f" ❄️ {self.name} is pelted by the hail!")
    #SAND DAMAGE
    if field.weather =="Sandstorm" and self.ability!="Sand Veil" and self.item!="Safety Googles" and self.hp>0:
        if self.type1 not in ["Rock","Ground","Steel"] and self.type2 not in ["Rock","Ground","Steel"] and self.ability!="Magic Guard":
            self.hp-=(1+round(self.maxhp/16))
            print(f" 🏜️ {self.name} is buffeted by the sandstorm!")
    #POISON
    if self.status=="Poisoned" and self.ability not in ["Magic Guard","Poison Heal","Immunity"] and self.hp>0:
        self.hp-=(1+round(self.maxhp/16))
        print(f" ☠️ {self.name} was hurt by poison.")
    #BADLY POISONED
    if self.status=="Badly Poisoned" and self.ability not in ["Magic Guard","Poison Heal","Toxic Boost","Immunity"] and self.hp>0:
        self.hp-=(1+(self.maxhp*self.badpoison/16))
        self.badpoison+=1
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
        spdefchange(self,-0.5)
    if self.ability=="Speed Boost":
        print(f" {self.name}'s {self.ability}!")
        speedchange(self,other,0.5)
    if 0 in self.pplist:
        if self.dmax is False and self.use in self.moves:
            self.moves.remove(self.moves[self.pplist.index(0)])
        if self.dmax is True and self.use in self.maxmove:
            self.moves.remove(self.moves[self.pplist.index(0)])
            self.maxmove.remove(self.maxmove[self.pplist.index(0)])
        self.pplist.remove(0)     
    if self.status!="Alive" and self.ability in ["Purifying Salt","Good as Gold"]:
        print(f" {self.name}'s {self.ability}!")
        self.status="Alive"
    if field.trickroom==True:
        if turn==field.troomendturn:
            field.trickroom=False
            print (" 🌐 The dimensions turned back to normal!")
    if self.dmax is True and turn==self.maxend:
        self.dmax=False
        prdx=["Great Tusk","Sandy Shocks","Roaring Moon","Brute Bonnet","Slither Wing","Flutter Mane","Scream Tail","Iron","Unbound","Tapu","Black","White","Attack","Defense","Speed","Hero","Alolan","Hisuian","Galarian","Dusk Mane","Dawn Wing","Black","White"]
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