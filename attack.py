from trainerlistx import *
from moves import *
from AItest import *
pkball=random.choice(["Poké Ball","Great Ball","Ultra Ball","Net Ball","Quick Ball","Master Ball","Beast Ball","Dive Ball","Nest Ball","Repeat Ball","Timer Ball","Cherish Ball","Dream Ball","Dusk Ball","Fast Ball","Heal Ball","Heavy Ball","Level Ball","Love Ball","Lure Ball","Luxury Ball","Moon Ball","Park Ball","Premier Ball","Safari Ball"])
healingmoves=["Recover","Roost","Synthesis","Morning Sun","Moonlight","Slack Off","Soft-Boiled","Milk Drink","Rest","Lunar Blessing"]
allmove=typemoves.firemoves+typemoves.watermoves+typemoves.electricmoves+typemoves.grassmoves+typemoves.normalmoves+typemoves.darkmoves+typemoves.ghostmoves+typemoves.psychicmoves+typemoves.poisonmoves+typemoves.steelmoves+typemoves.fairymoves+typemoves.bugmoves+typemoves.fightingmoves+typemoves.flyingmoves+typemoves.icemoves+typemoves.rockmoves+typemoves.groundmoves+typemoves.dragonmoves+typemoves.statusmove
priorityatkmoves=["Mach Punch","Bullet Punch","Sucker Punch","Fake Out","Extreme Speed","Aqua Jet","Shadow Sneak","Accelerock","Ice Shard","Water Shuriken"]
multimove=["Bullet Seed","Rock Blast","Pin Missile","Icicle Spear","Dual Chop","Dual Wingbeat","Arm Thrust","Water Shuriken"]
nondmgmove=typemoves.statusmove+typemoves.buffmove+["Stealth Rock","Toxic","Toxic Spikes","Sticky Web","Trick Room"]
premove=["Solar Beam","Meteor Beam","Skull Bash","Geomancy","Phantom Force","Shadow Force","Sky Attack","Ice Burn","Freeze Shock"]
maxmovelist=["Max Strike","Max Flare","G-Max Wildfire","G-Max Centiferno","Max Geyser","G-Max Cannonade","G-Max Hydrosnipe","G-Max Foam Burst","Max Lightning","G-Max Volt Crash","G-Max Stun Shock","Max Quake","Max Knuckle","G-Max Chi Strike","Max Mindstorm","Max Phantasm","G-Max Terror","Max Starfall","Max Overgrowth","G-Max Drum Solo","G-Max Sweetness","G-Max Tartness","Max Rockfall","Max Darkness","Max Wyrmwind","G-Max Depletion","Max Flutterby","G-Max Befuddle","Max Ooze","Max Steelspike","Max Airstream","G-Max Resonance","G-Max Hailstorm","G-Max Finale","G-Max Volcalith","G-Max Stonesurge","Max Hailstorm"]
def fchoice(pk,tr):
    if tr.ai is False:
        movelist(pk)
        choice=input(f" {tr.name}: Choose a move.\n >>")
        if choice in ["1","2","3","4","5","6"]:
            choice=int(choice)
        if pk.item is not None and  ("Choice" in pk.item or pk.ability in ["Gorilla Tactics","Sage Power"]) and pk.choiced==False and pk.dmax==False:
            if choice in ["1","2","3","4","5","6"]:
                pk.choicemove=pk.moves[choice-1]
            if choice =="":
                choice=random.randint(1,len(pk.moves))
            pk.choiced=True
            pk.choicedmove=int(choice)
        if len(pk.moves)==1:
            choice=1
        if choice not in [1,2,3,4,5,6]:
            if pk.dmax is False:
                choice=random.randint(1,len(pk.moves))
            if pk.dmax is True:
                choice=random.randint(1,len(pk.maxmove))
        #print("Chosen moves:",pk.moves[choice-1])
        if choice=="":
            choice(random.randint(1,len(pk.moves)))
        return choice
def switch(self,other,trainer,trainer2,field,turn):
    if trainer.ai is not True:
        showmon(trainer)
    if "Ditto" in self.name:
        self.ability="Imposter"
    self.atkb=self.defb=self.spatkb=self.spdefb=self.speedb=1
    self.yawn=False
    self.aring=False
    self.atk=self.maxatk
    self.speed=self.maxspeed
    self.spatk=self.maxspatk
    self.spdef=self.maxspdef
    self.defense=self.maxdef
    self.badpoison=1
    self.priority=self.recharge=self.seeded=self.flinched=self.protect=other.protect=self.shelltrap=self.choiced=False
    self.canfakeout=True 
    self.choicedmove=None
    
    if self.dmax is True:
        self.dmax=False
        self.name=self.name.split(" ")[-1]
        self.hp/=2
        self.maxhp/=2
        print(f" 🔻 {self.name} returned to it's normal state!")
    m=None
    switchable=[1,2,3,4,5,6]
    if self in trainer.pokemons:
        m=trainer.pokemons.index(self)
        swe=[0,1,2,3,4,5]
        swe.remove(m)
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
        phase2=random.choice(["It's our show time.","Show your strength.","Let's do it buddy.","I believe in you!","Let's finish this off.","Are you ready buddy?","Let's show them what you are capable of.","You know what to do."])
        print(f" Go {self.name}! "+phase2)
        entryeff(self,other,trainer,trainer2,field,turn)
        return self
    else:
        return self
#return text
def pkreturn(tr,mon):
    if "Red" in tr.name:
        print(f" {tr.name}: ........")
    if "Giovanni" in tr.name and mon.name=="Mewtwo":
        print(f" {tr.name}: WHAT! This cannot be!")
    else:
        phase1=random.choice([" return! You did well buddy."," return! You disappointed me."," return! Pathetic Pokémon."," return! Take rest my friend."," return! You were strong as always."," return! Maybe next time."])
        print(f"\n {tr.name}: "+mon.name+phase1)
#WITHDRAW EFFECTS
def withdaweff(self,trainer,other):
    if self.ability=="Zero to Hero" and "Hero" not in self.name and self.hp>0:
        print(f" {self.name} underwent a heroic transformation!")
        self.name="Hero Palafin"
        per=self.maxhp/self.hp
        self.hp=100
        self.atk=160
        self.defense=97
        self.spatk=106
        self.spdef=87
        self.speed=100
        self.calcst()
        self.hp*=per
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
#ENTRY EFFECTS            
def entryeff(self,other,trainer,trainer2,field,turn):
    if self.ability=="Pressure" and other.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"]:
        print(f"\n 🦕 {self.name}'s {self.ability}!")
        print(f" {self.name} is exerting its pressure!")
    if self.ability=="Bull Rush":
        self.bullrush=True
    if self.ability=="Supreme Overlord" and len(trainer.pokemons)!=6:
        print(f"\n 👺 {self.name} gained strength from the fallen!")
    if self.ability=="Frisk":
        print(f"\n 🔎 {self.name}'s {self.ability}!")
        print(f" ✅ {other.name} is holding {other.item}!")
    if self.ability=="Air Lock" and field.weather!="Clear":
        print(f"\n ☁️ {self.name}'s {self.ability}. The effects of the weather disappeared!")
        field.weather="Clear"
    if self.ability=="Delta Stream" and field.weather!="Strong Winds":
        print(f"\n 🍃 {self.name}'s {self.ability}. Mysterious strong winds are protecting Flying-type Pokémon!")
        field.weather="Strong Winds"
    prebuff(self,other,trainer,turn,field)
    if self.ability=="Stakeout":
        self.atk*=2
        self.spatk*=2
    self.maxendturn(turn)
    print("")
    abilitylist=[]
    for i in trainer.pokemons:
        abilitylist.append(i.ability)
    if self.ability=="Vessel of Ruin":
        print(f" ♉ {self.name}'s {self.ability} weakened the Sp.Atk of all surrounding Pokémon!")
    if self.ability=="Tablets of Ruin":
        print(f" ♈ {self.name}'s {self.ability} weakened the Atk of all surrounding Pokémon!")
    if self.ability=="Sword of Ruin":
        print(f" ♐ {self.name}'s {self.ability} weakened the Defense of all surrounding Pokémon!")
    if self.ability=="Beads of Ruin":
        print(f" ♋ {self.name}'s {self.ability} weakened the Sp.Def of all surrounding Pokémon!")
    if self.ability=="Download":
        print(f" {self.name}'s Download!")
        m=[a,b,c,d,e]=[other.atk,other.defense,other.spatk,other.spdef,other.speed]
        if trainer2.reflect==True:
            m=[other.atk,other.defense/2,other.spatk,other.spdef,other.speed]
        if trainer2.lightscreen==True:
            m=[other.atk,other.defense,other.spatk,other.spdef/2,other.speed]
        x=min(m)
        y=max(m)
        if y==a:
        	defchange(self,0.5)
        elif x==b:
        	atkchange(self,0.5)
        elif y==c:
        	spdefchange(self,0.5)
        elif x==d:
        	spatkchange(self,0.5)
    if "Commander" in abilitylist and "Dondozo" in self.name:
        print(f" 🪖 Tatsugiri's Commander!")
        print(f" {self.name}'s stats raised sharply!")
        atkchange(self,1)
        spatkchange(self,1)
        defchange(self,1)
        spdefchange(self,1)
        speedchange(self,1)
    if self.ability=="Trace" and other.ability not in ["As One","Battle Bond","Commander","Disguise","Forecast","Ice Face","Imposter","Illusion","Multitype","Power of Alchemy","Protosynthesis","Stance Change","Quark Drive","RKS System","Schooling","Trace","Zen Mode","Zero to Hero"] and other.item!="Ability Shield":
            print(f" {self.name}'s {self.ability}!")        
            self.ability=other.ability
    if self.ability=="Illusion":
        self.name=trainer.pokemons[len(trainer.pokemons)-1].name.split(" ")[-1]
    if "Legendary" in self.name and self.item in ["Silver Feather","Crimson Orb","Navy Orb","Jade Orb","Rainbow Feather","Team Rocket Armor"]:
        print(f" 🔱 {self.item} shrouded {self.name} with mystical energy!")
        self.hp*=6/len(trainer.pokemons)
        self.maxhp*=6/len(trainer.pokemons)
#        self.maxdef*=1.2
#        self.maxspdef*=1.2
#        self.maxatk*=1.2
#        self.maxspatk*=1.2
#        self.maxspeed*=1.2
    if "Quark Drive" in self.ability and (field.terrain=="Electric" or self.item=="Booster Energy"):
        print(f" ⚡ {self.name}'s {self.ability}!")
    if "Protosynthesis" in self.ability and (field.weather in ["Sunny","Desolate Land"] or self.item=="Booster Energy"):
        print(f" ☀️ {self.name}'s {self.ability}!")
    if self.megaintro is False and "Ultra " in self.name:
        prevname=self.name.split(" ")[-1]
    if self.megaintro is False and "Primal Kyogre" in self.name:
        prevname=self.name.split(" ")[-1]
        print(f" ⛎ {prevname}'s Primal Reversion! It reverted to its primal form!")
        self.primalintro=True
    if self.megaintro is False and "Primal Groudon" in self.name:
        prevname=self.name.split(" ")[-1]
        print(f" ♉ {prevname}'s Primal Reversion! It reverted to its primal form!")
        self.primalintro=True
    if self.megaintro is False and "Mega " in self.name and "Rayquaza" in self.name:
        prevname=self.name.split(" ")[-1]
        trname=trainer.name.split(" ")[-1]
        print(f" 🧬 {trname}'s fervent wish has reached {prevname}!\n {prevname} Mega evolved into {self.name}!\n")
    if self.megaintro is False and "💎" in self.name:
        typ=None
        if self.teratype is None:
            self.teratype=random.choice(["Rock","Fire","Water","Grass","Electric","Ground","Flying","Fighting","Fairy","Dragon","Steel","Poison","Dark","Ghost","Normal","Bug","Ice"])
        self.name=self.name.split("💎")[0]+"-"+self.teratype
        if self.teratype=="Dragon":
            typ="🐲"
        if self.teratype=="Psychic":
            typ="👁️"
        if self.teratype=="Ghost":
            typ="👻"
        if self.teratype=="Normal":
            typ="💎"
        if self.teratype=="Bug":
            typ="🪲"
        if self.teratype=="Steel":
            typ="🪓"
        if self.teratype=="Ice":
            typ="❄️"
        if self.teratype=="Fighting":
            typ="👊🏽"
        if self.teratype=="Dark":
            typ="😈"
        if self.teratype=="Fairy":
            typ="❤️"
        if self.teratype=="Flying":
            typ="🎈"
        if self.teratype=="Poison":
            typ="☠️"
        if self.teratype=="Ground":
            typ="🌍"
        if self.teratype=="Rock":
            typ="🪨"
        if self.teratype=="Grass":
            typ="🌻"
        if self.teratype=="Electric":
            typ="💡"
        if self.teratype=="Water":
            typ="⛲"
        if self.teratype=="Fire":
            typ="🕯️"
        name=self.name.split("💎")[0]
        n=name.split("-")[0]
        print(f" {typ}{n} terastallized into {self.teratype}-type!")
        self.megaintro=True
    if self.megaintro is False and "Ultra " in self.name:
        prevname=self.name.split(" ")[-1]
        print(f" ✴️{prevname} regained its true power through Ultra Burst")
        self.megaintro=True
    if self.megaintro is False and "Complete " in self.name:
        print(f" 🧬 You sense the presence of many!\nZygarde transformed into its Complete Forme!")
        self.megaintro=True

    if self.megaintro is False and "Mega " in self.name and "Rayquaza" not in self.name:
        trname=trainer.name.split(" ")[-1]
        prevname=self.name.split(" ")[-1]
        if "Mewtwo" in self.name:
            prevname="Mewtwo"
        if "Charizard" in self.name:
            prevname="Charizard"
        print(f" 🧬 {prevname}'s {self.item} is reacting to {trname}'s Keystone!\n {prevname} has Mega Evolved into {self.name}!\n")
        self.megaintro=True
    if self.dmax is True:
        prevname=self.name.split(" ")[-1]
        if "Dynamax" in self.name:
            print(f" 🔺{trainer.name} dynamaxed {prevname}!\n")
        if "Gigantamax" in self.name:
            print(f" 🔺{trainer.name} gigantamaxed {prevname}!\n")
    if self.ability=="Costar":     
        print(f" 🦩 {self.name}'s {self.ability}!")
        self.atkb=other.atkb
        self.defb=other.defb
        self.spatkb=other.spatkb
        self.spdefb=other.spdefb
        self.speedb=other.speedb   
    if self.ability=="Imposter" and other.dmax is False:
        print(f" 👾 {self.name}'s {self.ability}!")
        print(f' {self.name} transformed into {other.name}!')
        self.hp=round(other.maxhp*(self.hp/self.maxhp))
        self.maxhp=other.maxhp
        self.maxatk=other.maxatk
        self.maxdef=other.maxdef
        self.maxspatk=other.maxspatk
        self.maxspdef=other.maxspdef
        self.maxspeed=other.maxspeed    
        self.atk=other.atk
        self.defense=other.defense
        self.spatk=other.spatk
        self.spdef=other.spdef
        self.speed=other.speed    
        self.atkb=other.atkb
        self.defb=other.defb
        self.spatkb=other.spatkb
        self.spdefb=other.spdefb
        self.speedb=other.speedb
        self.moves=other.moves
        self.type1=other.type1
        self.type2=other.type2
        self.ability=other.ability
        self.pplist=[5,5,5,5]
        self.name=self.name+f"({other.name})"
    if self.ability == "Delta Stream" :
        field.weather=="Strong Wind"
    if (self.ability == "Sand Stream" or (self.ability=="Forecast" and self.item=="Smooth Rock")) and field.weather not in ["Sandstorm","Primordial Sea","Desolate Land"]:
        print(f" 🏜️{self.name}'s {self.ability} whipped up a sandstorm!")
        field.weather="Sandstorm" 
        field.sandturn=turn
        field.sandend(self,other)
    
    if self.ability=="Primordial Sea" and field.weather!="Primordial Sea":
        print(f" 🌊 {self.name}'s {self.ability}. A heavy rain began to fall!")
        field.weather="Primordial Sea"
    if self.ability=="Desolate Land" and field.weather!="Desolate Land":
        print(f" 🌋 {self.name}'s {self.ability}. The sunlight turned extremely harsh!")
        field.weather="Desolate Land"
    if (self.ability in  ["Drought","Orichalcum Pulse"] or (self.ability=="Forecast" and self.item=="Heat Rock")) and field.weather not in ["Sunny","Primordial Sea","Desolate Land"]:
        print(f" ☀️{self.name}'s {self.ability} intensified the sun's rays!")
        if self.ability=="Orichalcum Pulse":
            print(f" ♊ {self.name} turned the sunlight harsh, sending its ancient pulse into a frenzy!")
        field.weather="Sunny"
        field.sunturn=turn
        field.sunend(self,other)
    if (self.ability == "Drizzle" or (self.ability=="Forecast" and self.item=="Damp Rock")) and field.weather not in ["Rainy","Primordial Sea","Desolate Land"]:
        print(f" 🌧️{self.name}'s {self.ability} made it rain!")
        field.weather="Rainy"
        field.rainturn=turn
        field.rainend(self,other)
    if (self.ability == "Snow Warning" or (self.ability=="Forecast" and self.item=="Icy Rock")) and field.weather not in ["Primordial Sea","Desolate Land","Snowstorm"]:
        print(f" 🌨️{self.name}'s {self.ability} whipped up a snowstorm!")
        field.weather="Snowstorm"      
        field.snowstormturn=turn
        field.snowstormend(self,other)
    if self.ability=="Intrepid Sword":
        print(f" {self.name}'s {self.ability}")
        atkchange(self,0.5)
        print(f" Attack x{self.atkb}")
    if self.ability=="Dauntless Shield":
        print(f" {self.name}'s {self.ability}")
        defchange(self,0.5)
        print(f" Defense x{self.defb}")
    if self.ability in ["Electric Surge","Hadron Engine"]:
        print(f" {self.name}'s {self.ability}!")
        print(" ⚡ An electric self ran across the battlefield!")
        if self.ability=="Hadron Engine":
            print (f" ♐ {self.name} used the Electric Terrain to energize its futuristic engine!")
        field.terrain="Electric"
        field.eleturn=turn
        field.eleend(self,other)
    if self.ability=="Misty Surge":
        print(f" {self.name}'s {self.ability}!")
        print(" 🌸 Mist swirled around the battlefield!")
        field.terrain="Misty"
        field.misturn=turn
        field.misend(self,other)
    if self.ability=="Grassy Surge":
        print(f" {self.name}'s {self.ability}!")
        print(" 🌿 Grass grew to cover the battlefield!")
        field.terrain="Grassy"
        field.grassturn=turn
        field.grassend(self,other)
    if self.ability=="Psychic Surge":
        print(f" {self.name}'s {self.ability}!")
        print(" 👁️ The battlefield got weird!")
        field.terrain="Psychic"        
        field.psyturn=turn
        field.psyend(self,other)        
    if "Toxic Spikes" in trainer.hazard:
        if self.type1 in ["Poison"] or self.type2 in ["Poison"]:
            trainer.hazard.remove("Toxic Spikes")
            print(f" {self.name} absorbed the Toxic Spikes!")
        if self.type1 not in ["Poison","Steel"] and self.type2 not in ["Poison","Steel"] and self.ability not in ["Magic Guard","Levitate","Shield Dust"] and self.item!="Heavy-Duty Boots":
            self.status="Badly Poisoned"
            print(f" {self.name} was poisoned by Toxic Spikes.")
    if "Sticky Web" in trainer.hazard and self.ability not in ["Levitate","Shield Dust"] and self.item!="Heavy-Duty Boots":       
        speedchange(self,-0.5)
        print(f" {self.name}'s speed was lowered.")
    if "Stealth Rock" in trainer.hazard and self.ability not in ["Magic Guard","Levitate","Shield Dust","Mountaineer"] and self.item!="Heavy-Duty Boots":
        buff=2
        #print(self.type1,self.type2)
        if self.type1 in ["Flying", "Bug", "Fire", "Ice"] and self.teratype==None:
            buff*=2
        if self.type2 in ["Flying", "Bug", "Fire", "Ice"] and self.teratype==None:
            buff*=2
        if self.teratype in ["Flying", "Bug", "Fire", "Ice"]:
            buff*=2
        if self.type1 in ['Fighting', 'Ground', 'Steel'] and self.teratype==None:
            buff=1
        if self.type2 in ['Fighting', 'Ground', 'Steel'] and self.teratype==None:
            buff=1
        if self.teratype in ['Fighting', 'Ground', 'Steel']:
            buff=1
        #print(buff)
        self.hp-=(1+(self.maxhp*0.0625*buff))
        print(f" 🪨 Pointed stones dug into {self.name}!")
    if "Steel Spikes" in trainer.hazard and self.ability not in ["Magic Guard","Levitate","Shield Dust","Mountaineer"] and self.item!="Heavy-Duty Boots":
        buff=2
        #print(self.type1,self.type2)
        if self.type1 in ['Rock', 'Ice', 'Fairy'] and self.teratype==None:
            buff*=2
        if self.type2 in ['Rock', 'Ice', 'Fairy'] and self.teratype==None:
            buff*=2
        if self.teratype in ['Rock', 'Ice', 'Fairy']:
            buff*=2
        if self.type1 in ['Steel', 'Fire', 'Water', 'Electric'] and self.teratype==None:
            buff=1
        if self.type2 in ['Steel', 'Fire', 'Water', 'Electric'] and self.teratype==None:
            buff=1
        if self.teratype in ['Steel', 'Fire', 'Water', 'Electric']:
            buff=1
        #print(buff)
        self.hp-=(1+(self.maxhp*0.0625*buff))
        print(f" 📌 The sharp steel bit into {self.name}!")        
#INTIMIDATE        
    if self.ability=="Intimidate" and other.ability not in ["Inner Focus","Oblivious","Clear Body","Good as Gold"] and self.item not in ["Clear Amulet"]:
        if other.ability!="Guard Dog":
            atkchange(other,-0.5)
            print(f" {self.name}'s {self.ability}!")
            print(f" {other.name}'s attack was lowered.") 
        if other.ability=="Guard Dog":
            atkchange(other,0.5)
            print(f" {self.name}'s {self.ability}!")
            print(f" {other.name}'s {other.ability}!")
            print(f" {other.name}'s attack was raised.") 
        if other.item=="Adrenaline Orb":
            speedchange(other,0.5)
            print(f" {other.name}'s speed was raised by the Adrenaline Orb.") 
#Stance Change        
def stancechange(self,used):    
    if used not in typemoves.statusmove and self.ability=="Stance Change" and self.sword!=True:
        self.shield=False
        self.sword=True
        print(f" {self.name}'s {self.ability}!")
        print(" Aegislash changed to it's blade forme.")
        self.name="Aegislash(Blade)"        
        self.atk,self.spatk,self.defense,self.spdef=self.defense,self.spdef,self.atk,self.spatk
        self.maxatk,self.maxspatk,self.maxdef,self.maxspdef=self.maxdef,self.maxspdef,self.maxatk,self.maxspatk
    if used in typemoves.statusmove and self.ability=="Stance Change" and self.shield!=True:
        self.shield=True
        self.sword=False
        print(f" {self.name}'s {self.ability}!")
        print(" Aegislash changed to it's shield forme.")
        self.name="Aegislash(Shield)"        
        self.atk,self.spatk,self.defense,self.spdef=self.defense,self.spdef,self.atk,self.spatk
        self.maxatk,self.maxspatk,self.maxdef,self.maxspdef=self.maxdef,self.maxspdef,self.maxatk,self.maxspatk
 #PREATTACK       
def preattackcheck(self,other,tr,optr,use,opuse,field,turn):
    if self.yawn is not True and self.yawn=="Sleep" and self.status=="Alive" and field.terrain!="Electric":
        self.status="Sleep"
        print(f" {self.name} fell asleep!")
        print(f" 💤 {self.name} is fast asleep!")
        self.yawn=False
        use=None
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
    
    
            
    if self.ability=="Limber" and self.status=="Paralyzed":
        print(f" {self.ability} cured {self.name}'s paralysis!")
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
    
    pass
#ATTACK
def attack(self,other,tr,optr,use,opuse,field,turn):
    if self.ability!="Parental Bond[Used]":
        print(f"\n {tr.name}:")
    if self.choiced==True and self.choicedmove not in self.moves:
        use="Struggle"
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
    if self.status=="Sleep" and self.ability in ["Insomnia","Vital Spirit"]:
        self.status="Alive"
    if self.ability=="Prankster" and "Dark" in (other.type1,other.type2,other.teratype) and use in typemoves.statusmove:
        use = None
        print(f" {other.name} is immune to {self.name}'s Prankster!")
    
    if use in typemoves.prioritymove and other.ability in ["Armor Tail","Queenly Majesty","Dazzling"]:
        print(" {other.name}'s {other.ability}!")
        use=None
    if use in typemoves.bulletmove and other.ability=="Bulletproof":
        print(" {other.name}'s {other.ability}!")
        use=None
    if use in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads"]:
        if other.ability=="Fluffy":
            self.atk/=2
    if use not in typemoves.statusmove:
        other.atkby=self.name
        other.atktime+=1
    if other.ability=="Ice Face" and other.abilityused==False and use not in typemoves.statusmove+typemoves.buffmove:
        print(f" {other.name}'s {other.ability}!")
        other.abilityused=True
        other.maxdef=round(other.maxdef/1.57)
        other.maxspdef=round(other.maxspdef/1.8)
        other.maxspeed=round(other.maxspeed*2.6)
    if other.ability=="Disguise" and other.abilityused==False and use not in typemoves.statusmove+typemoves.buffmove:
        print(f" {self.name} used {use}!")
        print(f" {other.name}'s {other.ability}!")     
        other.hp-=round(other.maxhp*0.0625)
        other.abilityused=True
        use=None
    if use in healingmoves:
        self.healcount+=1
        if self.healcount==16 and use in healingmoves:
            self.moves.remove(use)
    if use!="Destiny Bond" and "Destiny Bond" in self.moves:
        other.dbond=False
    if opuse in typemoves.statusmove and use=="Protect":
        use=None
        print(" It failed!")
    if self.dmax is False:
        moves=self.moves
    if self.dmax is True:
        #print(self.maxmove)
        moves=self.maxmove
    used=""    
    if use!=None:
        used=use
#    print(used)
    hit=1
    me=self
    canatk=True
    if self.ability!="Oblivious":
        if self.confused is True:
            print(f" 😵‍💫 {self.name} is confused!")
            ch=random.randint(1,100)
            if ch<30:
                print(f" ‼️ {self.name} snapped out of confusion!")
                self.confused=False        
            if ch>70 and self.dmax==False:
                canatk=False
                used=None
                print(f" 😵  It hurt itself in confusion.")
                r=randroll()
                self.hp-=physical(self,self.level,self.atk,self.defense,base=40,a=1,r=r)
            else:
                canatk=True
    if self.status=="Paralyzed":
        ch=random.randint(1,100)
        if ch>75:
            canatk=False
            used=None
            self.precharge=False
            print(f" ⚡ {self.name} is paralyzed and unable to move.")
        else:
            print(f" ⚡ {self.name} is paralyzed.")
            canatk=True
    if self.status=="Sleep":
        ch=random.randint(1,4)
        if ch==3:
            print(f" ‼️ {self.name} woke up!")
            self.status="Alive"
        else:
            print(f" 💤 {self.name} is fast asleep!")
            used=None
    if self.status=="Frozen":
        ch=random.randint(1,5)
        if ch==3:
            print(f" ‼️ {self.name} thawed out.")
            self.status="Alive"
        else:
            print(f" 🧊 {self.name} is frozen solid.")
            used=None
    pp=1
    if other.ability=="Pressure":
        pp=2
    if self.dmax is False and canatk is True:
        if len(self.moves)==0 and self.status not in ("Sleep"):
            used="Struggle"
        
    preattackcheck(self,other,tr,optr,use,opuse,field,turn)
    #if self.choiced==True and self.choicedmove is not None and self.dmax is False:
#        used=self.choicedmove
    if used=="Metronome":
        print(f" {self.name} used Metronome!")
        used=random.choice(allmove)
        print(f" Metronome turned into {used}!")
    if self.precharge==True and len(self.moves)>0 and "Geomancy" not in self.moves:
        used=list(set(self.moves).intersection(premove))[0]
    if (field.terrain=="Psychic" or other.ability in ["Dazzling","Queenly Majesty","Armor Tail"]) and used in priorityatkmoves:
        if field.terrain!="Psychic":
            print(f" {other.name}'s {other.ability}.")
        used=None
        print("  🚳 Cannot use priority moves!")
    
    before=other.hp
    sbefore=self.hp
    if self.ability=="Truant" and used!="Slack Off":
        if self.truant==True:
            print(f" {self.name} is loafing around!")
            used=None
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
            used=None
    if opuse in ["Phantom Force","Shadow Force","Sky Attack"] and other.precharge==True and use not in premove and self.precharge==False and use not in ["Stealth Rock","Toxic Spikes"]+typemoves.buffmove:
        print(f" {self.name} used {used}!")
        print(f" {other.name} avoided the attack({used}).")
        used=None
    if other.item=="Bright Powder":
        ch=random.randint(1,10)
        if ch==1:
            print(f" {self.name} used {used}!")
            print(f" {other.name} avoided the attack({used}).")
            used=None
#SNOW CLOAK
    if other.ability=="Snow Cloak" and field.weather in ["Hail","Snowstorm"] and used not in typemoves.noaccuracy:
        ch=random.randint(1,self.accuracy)
        if ch<25:
            print(f" {other.name}'s {other.ability}.")
            print(f" {self.name} used {used}!")
            print(f" {other.name} avoided the attack({used}).")
            used=None
#SAND VEIL            
    if other.ability=="Sand Veil" and field.weather=="Sandstorm" and used not in typemoves.noaccuracy:
        ch=random.randint(1,self.accuracy)
        if ch<25:
            print(f" {other.name}'s {other.ability}.")
            print(f" {self.name} used {used}!")
            print(f" {other.name} avoided the attack({used}).")
            used=None
#######        
    if self.choicedmove=="st" and self.choiced==True:
        used="Struggle"
    if used in moves or used not in moves:
#        print(used)
        if self.taunted==True:
            if self.item=="Mental Herb":
                self.taunted=False
                self.item=None
            else:
                print(f" 🎭 Cannot use non-damaging moves while taunted.")
                used=None
        if self.item=="Assault Vest" and used in typemoves.statusmove:
            print(f" 🦺 Cannot use status moves while holding an Assault Vest.")
            used=None
        if used not in ["Protect","Spiky Shield","King's Shield","Baneful Bunker","Obstruct"]:
            self.protect=False
        if self.precharge==True and "Geomancy" in self.moves:
            print(f" 🌈 {self.name} used "+colored(" Geomancy","magenta")+"!")
            spatkchange(self,1)     
            spdefchange(self,1)   
            speedchange(self,1)
            print(f" {self.name} sharply raised its special attack, special defense and speed!")      
            self.precharge=False
            used=None
        if self.recharge==True:
            print(f" {self.name} is recharging.")
            self.recharge=False
            used=None
        if self.flinched==True and self.dmax is False:
            self.precharge=False
            print(f" 😧 {self.name} flinched and couldn't move.")
            self.flinched=False
            used=None
        elif self.protect=="Pending" and used in ["Protect","Spiky Shield","King's Shield","Baneful Bunker","Obstruct"]:
            print(f" 🛡️ {self.name} used {used}!")
            print("  It failed.")
            self.protect=False
            used=None
        elif other.protect==True and other.dmax is True and used not in typemoves.buffmove and used not in ["G-Max One Blow","G-Max Rapid Flow"]:
            print(f" 🛡️ {other.name} protected itself from {self.name}'s {used}.")
            other.protect="Pending"
            used=None
            if used in ["Protect","Spiky Shield","King's Shield","Baneful Bunker"]:
                print(f" 🛡️ {self.name} used {used}!")
#                print("  It failed!")
                used=None
        elif other.dmax is False and other.protect==True and used not in typemoves.buffmove and (self.ability not in ["Infiltrator","Unseen Fist"]  and used not in ["Shadow Force","Phantom Force","Hyperspace Fury","Hyper Drill"] and used not in maxmovelist and used not in typemoves.zmoves):
            print(f" 🛡️ {other.name} protected itself from {self.name}'s {used}.")
            other.protect="Pending"
            if used in ["Protect","Spiky Shield","King's Shield","Baneful Bunker","Max Guard"]:
                print(f" 🛡️ {self.name} used {used}!")
                print("  It failed!")
                used=None
                self.protect=False            
            if "Spiky Shield" in other.moves and used in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads"]:
                self.hp-=round(self.maxhp/8)
                print(f" {self.name} was hurt by Spiky Shield.") 
            if "Silk Trap" in other.moves and used in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads"]:
                speedchange(self,-0.5)
                print(f" {self.name}'s speed fell!")
            if "Obstruct" in other.moves and used in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads"]:
                spatkchange(self,-0.5)
                print(f" {self.name}'s special attack fell!")
            if "King's Shield" in other.moves and used in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads"]:
                atkchange(self,-0.5)
                print(f" {self.name}'s attack fell!")
            if "Baneful Bunker" in other.moves and used in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads"]:
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
            if opuse in nondmgmove or opuse is None:
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
            print(f" {self.name} used Taunt.")
            if other.taunted==True:
                print(" It failed.")
            if other.taunted==False:
                other.taunted=True
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
            filletaway(self)
        elif used=="Cosmic Power":
            cosmicpower (self)
        elif used=="Amnesia":
            amnesia(self)
        elif used=="No Retreat":
            noretreat(self)
        elif used=="Aqua Ring":
            aquaring(self)
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
            darkhole(self,other)
        elif used=="Raging Bull":
            ragingbull (self,other)
        elif used=="Encore":
            if other.item=="Mental Herb":
                print(f" {other.name}'s {other.item} protected it from Encore.")
                self.item=None
            else:
                encore(self,other,opuse)
        elif used=="Strange Steam":
            strangesteam(self,other)
        elif used=="Growth":
            growth(self)
        elif used=="G-Max Cuddle":
            gmaxcuddle(self,other)
        elif used=="G-Max Gold Rush":
            gmaxgoldrush(self,other)
        elif used=="G-Max Malodor":
            gmaxmalodor(self,other)
        elif used=="G-Max Meltdown":
            gmaxmeltdown(self,other)
        
        elif used=="Lunar Blessing":
            lunarblessing(self)
            if self.status!="Alive":
                self.status="Alive"
                print(f" {self.name}'s status was cured.")
        elif used=="Take Heart":
            takeheart(self)
            if self.status!="Alive":
                self.status="Alive"
                print(f" {self.name}''s status was cured.")
        elif used=="G-Max Snooze":
            gmaxsnooze(self,other)
        elif used=="G-Max Wind Rage":
            gmaxwindrage(self,other)
        elif used=="G-Max Vine Lash":
            gmaxvinelash(self,other,turn)
        elif used=="G-Max Smite":
            gmaxsmite(self,other)
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
            cottonguard(self)
        elif used=="Spicy Extract":
            spicyextract(self,other)
        elif used=="Spin Out":
            spinout(self,other)
        elif used=="Clanging Scales":
            clangscale(self,other)
        elif used=="Clangorous Soul":
            clangsoul(self)
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
            geomancy(self)
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
            shelter(self)
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
            shoreup(self)
        elif used=="Electric Terrain":
            electricterrain(self,other,field,turn)
        elif used=="Misty Terrain":
            mistyterrain(self,other,field,turn)
        elif used=="Grassy Terrain":
            grassyterrain(self,other,field,turn)
        elif used=="Psychic Terrain":
            psychicterrain(self,other,field,turn)
        elif used=="Synthesis":
            synthesis(self)
        elif used=="Snowscape":
            snowscape(self,other,field,turn)
        elif used=="Hail":
            hail(self,other,field,turn)
        elif used=="Quiver Dance":
            quiverdance(self)
            if other.ability=="Dancer":
                print(f" {other.name}'s {other.ability}!")
                quiverdance(other)
        elif used=="Defend Order":
            defendorder(self)
        elif used=="Swords Dance":
            swordsdance(self)
            if other.ability=="Dancer":
                print(f" {other.name}'s {other.ability}!")
                swordsdance(other)
        elif used=="Nasty Plot":
            nastyplot(self)
        elif used=="Shell Smash":
            shellsmash(self)
        elif used=="Autotomize":
            autotomize(self)
        elif used=="Tidy Up":
            tidyup(self,other,tr)
        elif used=="Rapid Spin":
            rapidspin(self,other,tr)
        elif used=="Dragon Dance":
            dragondance(self)
            if other.ability=="Dancer":
                print(f" {other.name}'s {other.ability}!")
                dragondance(other)
        elif used=="Iron Defense":
            irondefense(self)
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
            print(f" {self.name} used defog.")
            print("  All the hazards blew away!")
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
             ceaseless(self,other)
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
            milkdrink(self)
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
            if len(tr.pokemons)>1 and (other.hp!=before):
                print(f" {self.name} returned to it's {pkball}.")
                self=switch(self,other,tr,optr,field,turn)
        elif used=="Chilly Reception":
            chillyreception(self,other,field,turn)
            if len(tr.pokemons)>1:
                print(f" {self.name} returned to it's {pkball}.")
                self=switch(self,other,tr,optr,field,turn)                        
        elif used=="U-Turn":
            uturn(self,other)
            if len(tr.pokemons)>1:
                print(f" {self.name} returned to it's {pkball}.")
                self=switch(self,other,tr,optr,field,turn)
        elif used=="Parting Shot":
            partingshot(self,other)
            if len(tr.pokemons)>1:
                print(f" {self.name} returned to it's {pkball}.")
                self=switch(self,other,tr,optr,field,turn)                
        elif used=="Volt Switch":
            voltswitch(self,other)
            if len(tr.pokemons)>1 and (other.hp!=before):
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
            print(f" {self.name} used Roar.")
            other=random.choice(optr.pokemons)
            print(f" {other.name} was dragged out!")
        elif used=="Whirlwind":
            print(f" {self.name} usedd Whirlwind.")
            print(f" {other.name} blew away with the wind.")
            other=random.choice(optr.pokemons)
            print(f" {other.name} was dragged out!")
        elif used=="Return":
            retrn(self,other)
        elif used=="Sleep Powder":
            miss=random.randint(1,self.accuracy)
            if miss<25:
                print(f" {other.name} avoided the attack({used}).")
            else:
                sleeppowder(self,other)
        elif used=="Spore":
            spore(self,other)
        elif used=="Hypnosis":
            miss=random.randint(1,self.accuracy)
            if miss<40:
                print(f" {other.name} avoided the attack({used}).")
            else:
                hypnosis(self,other)
        elif used=="Dark Void":
            miss=random.randint(1,self.accuracy)
            if miss<20:
                print(f" {other.name} avoided the attack({used}).")
            else:
                darkvoid(self,other)
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
            coil(self)
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
            curse(self)
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
            hit=random.randint(1,10)
            if self.ability=="Skill Link":
                print(f" {self.name}'s {self.ability}.")
                hit=10
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
            speedchange(self,0.5)
            print(f" {self.name}'s speed rose and defense fell!")
            defchange(self,-0.5)
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
            signalbeam(self,other)
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
            axekick(self,other)
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
                hurricane(self,other)
            if field.weather =="Sunny" and field.weather == "Sunny":
                miss=random.randint(1,self.accuracy)
                if miss<50:
                    print(f" {other.name} avoided the attack({used}).")
                elif miss>=50 or "No Guard" in (self.ability,other.ability):
                    hurricane(self,other)
            elif field.weather != "Rainy" and field.weather !="Rainy":
                miss=random.randint(1,self.accuracy)
                if miss<30:
                    print(f" {other.name} avoided the attack({used}).")
                elif miss>=30 or "No Guard" in (self.ability,other.ability):
                    hurricane(self,other)
          
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
            if "Toxic Spikes" in optr.hazard:
                print(" Nothing happened!")
            if "Toxic Spikes" not in optr.hazard:
                print(f" {self.name} used "+colored("Toxic Spikes","magenta")+".")
                print(" ☠️ Poison spikes were scattered all around the opposing team!")
                optr.hazard.append("Toxic Spikes")
            else:
                print(" Nothing happened!")
        elif used=="Stealth Rock":
            if "Stealth Rock" in optr.hazard:
                print(" Nothing happened!")
            if "Stealth Rock" not in optr.hazard:
                print(f" {self.name} used "+colored(" Stealth Rock","yellow")+"!")
                print(" 🪨 Pointed stones float in the air around the opposing team!")
                optr.hazard.append("Stealth Rock")
        elif used=="Sticky Web":
            if "Sticky Web" in optr.hazard:
                print(" Nothing happened!")
            if "Sticky Web" not in optr.hazard:
                print(f" {self.name} used Sticky Web.")
                print(" 🕸️ A sticky web spreads out in the ground around the opposing team!")
                optr.hazard.append("Sticky Web")            
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
                softboiled(self)
        elif used=="Heal Order":
            if self.hp==self.maxhp:
                print("  It failed!")
            else:
                healorder(self)
        elif used=="Slack Off":
            if self.hp==self.maxhp:
                print("  It failed!")
            else:
                slackoff(self)
        elif used=="Roost":
            if self.hp==self.maxhp:
                print("  It failed!")
            else:
                roost(self)
        elif used=="Recover":
            if self.hp==self.maxhp:
                print("  It failed!")
            else:
                recover(self)
            
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
                morningsun(self)
        elif used=="Moonlight":
            if self.hp==self.maxhp:
                print("  It failed!")
            else:
                moonlight(self)
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
            victorydance(self)
            if other.ability=="Dancer":
                print(f" {other.name}'s {other.ability}!")
                victorydance(other)
        elif used=="Light Screen":
            if tr.lightscreen==True:
                print(" It Failed!")
            if tr.lightscreen==False:
                lightscreen(self,other,tr,turn)
        elif used=="Calm Mind":
            calmmind(self)
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
            acidarmor(self)
        elif used=="Aeroblast":
            miss=random.randint(1,self.accuracy)
            if miss<5:
                print(f" {other.name} avoided the attack({used}).")
            else:
                aeroblast(self,other)
        elif used=="Wicked Blow":
            wickedblow(self,other)
        elif used=="Tail Glow":
            tailglow(self)
        elif used=="Psychic Fangs":
            psychicfang(self,other)
        elif used=="Poison Fang":
            poisonfang(self,other)
        elif used=="Poison Tail":
            poisontail(self,other)
        elif used=="Force Palm":
            forcepalm(self,other)
        elif used=="Techno Blast":
            technoblast(self,other)
        elif used=="Relic Song":
            relicsong(self,other)
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
            if "Fairy" not in (other.type1,other.type2,other.teratype):
                other=random.choice(optr.pokemons)
                print(f" {other.name} was dragged out!")
        elif used=="Rock Tomb":
            rocktomb(self,other)     
        elif used=="Last Resort":
            lastresort (self,other)           
        elif used=="Dizzy Punch":
            dizzypunch (self,other)
        elif used=="G-Max Sandblast":
            gmaxsandblast(self,other,tr,turn)
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
            direclaw(self,other)
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
            bellydrum(self)
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
                rest(self)
        elif used=="Bulk Up":
            bulkup(self)
        elif used=="Stone Edge":
            miss=random.randint(1,100)
            if miss>90:
                print(f" {other.name} avoided the attack({used}).")
            else:
                stoneedge(self,other)
        elif used=="Steel Wing":
            steelwing(self,other)
        elif used=="Focus Blast":
            miss=random.randint(1,self.accuracy)
            if miss>70:
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
            miss=random.randint(1,100)
            if miss>90:
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
            miss=random.randint(1,100)
            if miss>50 and self.ability!="No Guard":
                print(f" {other.name} avoided the attack({used}).")
            if miss<=50 or "No Guard" in (self.ability,other.ability):
                dynapunch(self,other)
        elif used=="Liquidation":
            liquidation(self,other)
        elif used=="Tera Blast":
            terablast(self,other)
        elif used=="Earthquake":
            earthquake(self,other)
        elif used=="Belch":
            miss=random.randint(1,100)
            if miss>90:
                print(f" {other.name} avoided the attack({used}).")
            else:
                belch(self,other)
        elif used=="Gunk Shot":
            miss=random.randint(1,100)
            if miss>80:
                print(f" {other.name} avoided the attack({used}).")
            else:
                gunkshot(self,other)
        elif used=="Freeze Shock":
            miss=random.randint(1,100)
            if miss>90:
                print(f" {other.name} avoided the attack({used}).")
            else:
                freezeshock(self,other)                   
        elif used=="Ice Burn":
            miss=random.randint(1,100)
            if miss>90:
                print(f" {other.name} avoided the attack({used}).")
            else:
                iceburn(self,other)                      
        elif used=="Blue Flare":
            miss=random.randint(1,100)
            if miss>85:
                print(f" {other.name} avoided the attack({used}).")
            else:
                blueflare(self,other)     
        elif used=="Eternabeam":
            miss=random.randint(1,100)
            if miss>90:
                print(f" {other.name} avoided the attack({used}).")
            else:
                eternabeam (self,other)   
                self.recharge=True                
        elif used=="Bolt Strike":
            miss=random.randint(1,100)
            if miss>85:
                print(f" {other.name} avoided the attack({used}).")
            else:
                boltstrike(self,other)   
        elif used=="Thunder Cage":
            miss=random.randint(1,100)
            if miss>90:
                print(f" {other.name} avoided the attack({used}).")
            else:
                thundercage(self,other)     
        elif used=="Mountain Gale":
            miss=random.randint(1,100)
            if miss>85:
                print(f" {other.name} avoided the attack({used}).")
            else:
                mountaingale(self,other)       
        elif used=="Mystical Power":#isinstance(used,FireBlast)
            miss=random.randint(1,100)
            if miss>90:
                print(f" {other.name} avoided the attack({used}).")
            else:
                mysticalpower(self,other)                
                                                
        elif used=="Fire Blast":#isinstance(used,FireBlast)
            miss=random.randint(1,100)
            if miss>85:
                print(f" {other.name} avoided the attack({used}).")
            else:
                fireBlast(self,other)
            
                
        elif used=="Pyro Ball":
            miss=random.randint(1,100)
            if miss>90:
                print(f" {other.name} avoided the attack({used}).")
            else:
                pyroball(self,other)       
        elif used=="Meteor Beam":
            miss=random.randint(1,100)
            if miss>90:
                print(f" {other.name} avoided the attack({used}).")
            else:
                meteorbeam(self,other)                                
        elif used=="Psychic":
            psychic(self,other)
        elif used=="Seed Flare":
            miss=random.randint(1,100)
            if miss>85:
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
            miss=random.randint(1,100)
            if miss>80:
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
            print(f" {self.name} reacting to {tr.name}'s Waterium Z.")
            self.item=None
            hydrovortex(self,other)
            self.moves.remove(used)
        elif used =="Oceanic Operetta":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item=None
            operetta(self,other)
            self.moves.remove(used)
        elif used =="Malicious Moonsault":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item=None
            moonsault(self,other)
            self.moves.remove(used)
        elif used =="Light That Burns The Sky":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item=None
            skyburn(self,other)
            self.moves.remove(used)
        elif used =="Let's Snuggle Forever":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item=None
            snuggle(self,other)
            self.moves.remove(used)      
        elif used =="Extreme Evoboost":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item=None
            exevoboost(self)
            self.moves.remove(used)      
        elif used =="Guardian of Alola":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item=None
            goalola(self,other)
            self.moves.remove(used)
        elif used =="Stoked Sparksurfer":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item=None
            sparksurf(self,other)
            self.moves.remove(used)
        elif used =="Clangorous Soulblaze ":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item=None
            soulblaze(self,other)
            self.moves.remove(used)
        elif used =="Sinister Arrow Raid":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item=None
            arrowraid(self,other)
            self.moves.remove(used)
        elif used =="Soul-Stealing 7-Star Strike":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item=None
            soulstealing(self,other)
            self.moves.remove(used)
        elif used =="Menacing Moonraze Maelstrom":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item=None
            menacingmoonrazemaelstrom(self,other)
            self.moves.remove(used)
        elif used =="Searing Sunraze Smash":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item=None
            searingsunrazesmash(self,other)
            self.moves.remove(used)
        elif used =="Genesis Supernova":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item=None
            genesissupernova(self,other,field,turn)
            self.moves.remove(used)
        elif used =="Pulverizing Pancake":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Snorlium Z.")
            self.item=None
            pulverizingpancake(self,other)
            self.moves.remove(used)
        elif used =="Splintered Stromshards":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Lycanium Z.")
            self.item=None
            stormshards(self,other)
            self.moves.remove(used)                
        elif used =="Inferno Overdrive":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Firium Z.")
            self.item=None
            infernooverdrive(self,other)
            self.moves.remove(used)
        elif used =="Bloom Doom":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Grassium Z.")
            self.item=None
            bloomdoom(self,other)
            self.moves.remove(used)
        elif used =="Gigavolt Havoc":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Electrium Z.")
            self.item=None
            gigavolthavoc(self,other)
            self.moves.remove(used)
        elif used =="Catastropika":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item=None
            catastropika(self,other)
            self.moves.remove(used)
        elif used =="Pulverizing Pancake":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item=None
            pulverizingpancake(self,other)
            self.moves.remove(used)
        elif used =="10,000,000 Volt Thunderbolt":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item=None
            tenmvolttb(self,other)
            self.moves.remove(used)
        elif used =="Acid Downpour":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Poisonium Z.")
            aciddownpour(self,other)
            self.moves.remove(used)
        elif used =="Breakneck Blitz":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Normalium Z.")
            self.item=None
            breakneckblitz(self,other)
            self.moves.remove(used)
        elif used =="All-Out Pummeling":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Fightinium Z.")
            self.item=None
            alloutpummeling(self,other)
            self.moves.remove(used)
        elif used =="Black Hole Eclipse":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Darkinium Z.")
            self.item=None
            blackholeeclipse(self,other)
            self.moves.remove(used)
        elif used =="Continental Crush":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Rockium Z.")
            self.item=None
            continentalcrush(self,other)
            self.moves.remove(used)
        elif used =="Tectonic Rage":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Groundium Z.")
            self.item=None
            tectonicrage(self,other)
            self.moves.remove(used)
        elif used =="Corkscrew Crash":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Steelium Z.")
            self.item=None
            corkscrewcrash(self,other)
            self.moves.remove(used)
        elif used =="Devastating Drake":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Dragonium Z.")
            self.item=None
            devastatingdrake(self,other)
            self.moves.remove(used)
        elif used =="Shattered Psyche":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Psychium Z.")
            self.item=None
            shatteredpsyche(self,other)
            self.moves.remove(used)
        elif used =="Never-ending Nightmare":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Ghostium Z.")
            self.item=None
            neverendingnightmare(self,other)
            self.moves.remove(used)
        elif used =="Supersonic Skystrike":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Flyinium Z.")
            self.item=None
            supersonicskystrike(self,other)
            self.moves.remove(used)
        elif used =="Savage Spin-Out":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Buginium Z.")
            self.item=None
            savagespinout(self,other)
            self.moves.remove(used)
        elif used =="Subzero Slammer":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Icium Z.")
            self.item=None
            subzeroslammer (self,other)
            self.moves.remove(used)
        elif used =="Twinkle Tackle":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Fairium Z.")
            self.item=None
            twinkletackle(self,other)
            self.moves.remove(used)
        elif used=="Counter":
           print(f" {self.name} used "+colored(" Counter","red")+"!")
           if self.speed<other.speed and other.atkcat=="Physical" and "Ghost" not in (other.type1,other.type2,other.teratype):
               other.hp-=self.dmgtaken*2
           else:
               print(" It failed.")
        elif used=="Mirror Coat":
           print(f" {self.name} used "+colored(" Mirror Coat","magenta")+"!")
           if self.speed<other.speed and other.atkcat=="Special" and "Dark" not in (other.type1,other.type2,other.teratype):
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
        self,other=attack(self,other,tr,optr,use,opuse,field,turn)
    if "Destiny Bond" in self.moves and used!="Destiny Bond":
        other.dbond=False
    if other.hp<0:
        other.hp=0
    other.dmgtaken=before-other.hp
    if used not in typemoves.statusmove:
        if other.item=="Rowap Berry" and other.atkcat=="Special" and self.hp!=sbefore:
          print(f" {other.name}'s {other.item} damaged {self.name}!")
          self.hp-=(other.maxhp/8)
          if other.ability!="Harvest":
                other.item=None
        if other.item=="Kee Berry":
            print(f" {other.item} raised it's defense.")
            defchange(other,0.5)
            if other.ability!="Harvest":
                other.item=None
        if other.item=="Jacoba Berry" and other.atkcat=="Physical" and self.hp!=sbefore:
            print(f" {other.name}'s {other.item} damaged {self.name}!")
            self.hp-=round(self.maxhp/8)
            if other.ability!="Harvest":
                other.item=None
    if self.item=="Throat Spray" and used in typemoves.soundmoves:
        spatkchange(self,0.5)
        print(f" The Throat Spray raised {self.name}'s Special Attack!")
        self.item=None            
    if other.item=="Maranga Berry" and other.atkcat=="Special" and self.hp!=sbefore:
          print(f" {other.item} raised it's special defense.")
          spdefchange (other,0.5)
          if other.ability!="Harvest":
             other.item=None
    if other.hp>0:
          if other.hp<=(other.maxhp/4)  and before>(other.maxhp/4):
              if other.item=="Starf Berry":
                  ss=random.randint(1,5)
                  if ss==1:
                      print(f" {other.item} sharply raised it's attack.")
                      atkchange (other,1)
                  if ss==2:
                      print(f" {other.item} sharply raised it's special attack.")
                      spatkchange (other,1)
                  if ss==3:
                      print(f" {other.item} sharply raised it's defense.")
                      defchange (other,1)
                  if ss==4:
                      print(f" {other.item} sharply raised it's special defense.")
                      spdefchange (other,1)
                  if ss==5:
                      print(f" {other.item} sharply raised it's speed.")
                      speedchange (other,1)
                  if other.ability!="Harvest":
                      other.item=None
              if other.item=="Custap Berry" and other.speed<self.speed:
                  print(f" {other.item} will let {other.name} move first!")
                  other.priority=True
                  if other.ability!="Harvest":
                      other.item=None
              if other.item=="Salac Berry":
                  print(f" {other.item} raised it's speed.")
                  speedchange (other,0.5)
                  if other.ability!="Harvest":
                      other.item=None
              if other.item=="Petaya Berry":
                  print(f" {other.item} raised it's special attack.")
                  spatkchange (other,0.5)
                  if other.ability!="Harvest":
                      other.item=None
              if other.item=="Liechi Berry":
                  print(f" {other.item} raised it's attack.")
                  atkchange (other,0.5)
                  if other.ability!="Harvest":
                      other.item=None
              if other.item=="Lansat Berry":
                  print(f" {other.item} raised it's critical hit ratio.")
                  other.critrate*=4
                  if other.ability!="Harvest":
                      other.item=None
              if other.item=="Ganlon Berry":
                  print(f" {other.item} raised it's defense.")
                  defchange (other,0.5)
                  if other.ability!="Harvest":
                      other.item=None
              if other.item=="Apicot Berry":
                  print(f" {other.item} raised it's special defense.")
                  spdefchange (other,0.5)
                  if other.ability!="Harvest":
                      other.item=None
          if other.hp<=(other.maxhp/2)  and before>(other.maxhp/2):
              if other.ability=="Anger Shell":
                  print(f" 💢 {other.name}'s {other.ability}!")
                  defchange (other,-0.5)
                  spdefchange (other,-0.5)
                  atkchange(other,0.5)
                  spatkchange (other,0.5)
                  speedchange (other,0.5)
              if other.ability=="Berserk":
                  print(f" {other.name}'s {other.ability}!")
                  spatkchange (other,0.5)
              if other.item in ["Aguav Berry","Figy Berry","Ipapa Berry","Mago Berry","Wiki Berry"]:
                  other.hp+=round(other.maxhp/4)
                  print(f" {other.name} consumed it's {other.item} and restored some HP!")
                  if other.ability!="Harvest":
                      other.item=None
              if other.item=="Sitrus Berry":
                  other.hp+=round(other.maxhp/4)
                  print(f" {other.name} restored HP using its {other.item}!")
                  if other.ability!="Harvest":
                      other.item=None
    if self.hp<self.maxhp/2:
        if self.item=="Sitrus Berry":       
            self.hp+=round(self.maxhp/4)
            print(f" {self.name} restored HP using its {self.item}!")
            if other.ability!="Harvest":
                other.item=None
#STURDY        
    if used in typemoves.contactmoves and other.ability == "Sand Spit" and field.weather not in ["Sandstorm","Primordial Sea","Desolate Land"] and self.item not in ["Protective Pads","Punching Glove"]:
        print(f" 🏜️{other.name}'s {other.ability} whipped up a sandstorm!")
        field.weather="Sandstorm" 
        field.sandturn=turn
        field.sandend(self,other)
    if used in typemoves.contactmoves and other.abilityused=="Shell Trap" and self.item not in ["Protective Pads","Punching Glove"]:
        shelltrap(other,self)
        other.abilityused=False
    if other.item=="Focus Band" and used not in multimove:
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
        if other.ability=="Sturdy" and other.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and used not in multimove:
            print(f" {other.name}'s Sturdy!")
            print(f" {other.name} hung on using Sturdy.")
            other.hp=1
            
        if other.item=="Focus Sash" and used not in multimove:
            print(f" {other.name} hung on using Focus Sash.")
            other.hp=1
            other.item=None
    per=round(((before-other.hp)/other.maxhp)*100,2)
    sper=round(((sbefore-self.hp)/self.maxhp)*100,2)
    if other.hp<0:
        per=round((before/other.maxhp)*100,2)
    if self.hp<0:
        sper=round((sbefore/self.maxhp)*100,2)
    if other.hp!=before:
#STAMINA        
        if other.ability=="Stamina":
            print(f" {other.name}'s {other.ability}!")
            defchange(other,0.5)
            print(f" {other.name}: Defense x{other.defb}")
    if self.dbond is True and other.hp<=0:
        self.hp=0
        print(f" {other.name} took away {self.name} with it!")
#ILLUSION        
    if other.ability=="Illusion" and "Zoroark" not in other.name and other.hp!=before:
        if other.type1=="Dark":
            other.name="Zoroark"
            print(f" {other.name}'s Illusion wore off!")
        else:
            other.name="Hisuian Zoroark"
            print(f" {other.name}'s Illusion wore off!")
    if other.item=="Sticky Barb" and me.ability!="Long Reach" and used in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads"] and other.hp!=before:
        self.hp-=(self.maxhp/8)   
        other.hp-=(other.maxhp/8)
        if self.item==None:
            self.item="Sticky Barb"
            other.item=None
        print(f" 🐌 {other.name}'s {other.ability}!")     
        speedchange (self,-0.5)           
    if other.ability=="Gooey" and me.ability not in ["Clear Body","Good as Gold"] and me.ability!="Long Reach" and used in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads"] and other.hp!=before:   
        print(f" 🐌 {other.name}'s {other.ability}!")     
        speedchange (self,-0.5)
    if other.ability=="Flame Body" and me.status=="Alive" and me.ability!="Long Reach" and used in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads"] and other.hp!=before:
        ch=random.randint(1,100)  
        if ch>70:
            print(f" 🔥 {other.name}'s {other.ability}!")
            me.status="Burned"  
            print(f" 🔥 {me.name} was burned.") 
    if other.ability=="Seed Sower" and "Toxic Spikes" not in tr.hazard and me.ability!="Long Reach" and used in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads"] and field.terrain!="Grassy" and other.hp!=before:
        print(f" {self.name}'s {self.ability}!")
        print(" 🌿 Grass grew to cover the battlefield!")
        field.terrain="Grassy"
        field.grassturn=turn
        field.grassend(self,other)          
    if other.ability=="Toxic Debris" and "Toxic Spikes" not in tr.hazard and me.ability!="Long Reach" and used in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads"] and other.hp!=before:
        print(f" ☣️ {other.name}'s {other.ability}!")   
        print(" ☠️ Poison spikes were scattered all around the opposing team!")
        tr.hazard.append("Toxic Spikes")   
    if other.ability=="Static" and me.status=="Alive" and me.ability!="Long Reach" and used in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads"] and other.hp!=before:
        ch=random.randint(1,100)  
        if ch>70:
            print(f" ⚡ {other.name}'s {other.ability}!")
            me.status="Paralyzed"
            print(f" ⚡ {self.name} was paralyzed.")
    if other.ability=="Poison Point" and me.status=="Alive" and me.ability!="Long Reach" and used in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads"]:
        ch=random.randint(1,100)  
        if ch>70:
            print(f" ☠️ {other.name}'s {other.ability}!")
            self.status="Badly Poisoned"  
            print(f" ☠️ {me.name} was badly poisoned.")
    if self.ability=="Poison Touch" and other.status=="Alive" and other.ability!="Long Reach" and used in typemoves.contactmoves and self.item not in ["Punching Glove","Protective Pads"]:
        ch=random.randint(1,100)  
        if ch>70:
            print(f" {self.name}'s {self.ability}!")
            other.status="Badly Poisoned"        
    if used in typemoves.contactmoves and other.item=="Air Balloon" and self.item not in ["Punching Glove","Protective Pads"]:
        print(f" {other.name}'s Air Balloon popped off!")
        other.item=None                      
    if other.hp!=before and per>0:
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
            print(f" {other.name} returned to it's {pkball}.")
            other.item=None
            other=random.choice(optr.pokemons)             
        if len(tr.pokemons)>1 and other.item=="Red Card":
            other.item=None
            print(f" {self.name} returned to it's {pkball}.")
            self=switch(self,other,tr,optr,field,turn)
        if len(optr.pokemons)>1 and other.item=="Eject Button":
            print(f" {other.name} returned to it's {pkball}.")
            other.item=None
            other=random.choice(optr.pokemons)       
                
#LIFE ORB                    
        if self.item=="Life Orb" and self.ability!="Magic Guard":
            self.hp-=round(self.maxhp/16)
            print(f" 🟣 {self.name} lost some of its HP!")
            if self.hp<0:
                self.hp=0
    if other.hp==0:
#AFTERMATH        
        if other.ability=="Aftermath":
            print(f" 💭 {other.name}'s {other.ability}!")
            if self.hp<(self.maxhp/4):
                self.hp==0
            else:
                self.hp-=round(self.maxhp/4)
    if other.item=="Custap Berry" and other.speed<self.speed and self.hp<(self.maxhp/4):
        print(f" {other.item} will let {other.name} move first!")
        other.priority=True
        if other.ability!="Harvest":
            other.item=None     
    if self.item=="Cheri Berry" and self.status=="Paralyzed":
        print(f" {self.item} cured {self.name}'s paralysis!")
        self.status="Alive"
        if other.ability!="Harvest":
            self.item=None
    if self.item=="Rawst Berry" and self.status=="Burned":
        print(f" {self.item} cured {self.name} from burn!")
        self.status="Alive"
        if other.ability!="Harvest":
            self.item=None
    if self.item=="Chesto Berry" and self.status=="Sleep":
        print(f" {self.item} cured {self.name} from sleep state!")
        print(f" {self.name} woke up!")
        self.status="Alive"
        if self.ability!="Harvest":
            self.item=None
    if other.item=="Chesto Berry" and other.status=="Sleep":
        print(f" {other.item} cured {other.name} from sleep state!")
        print(f" {other.name} woke up!")
        other.status="Alive"
        if other.ability!="Harvest":
            other.item=None
    if self.item=="Aspear Berry" and self.status=="Frozen":
        print(f" {self.item} cured {self.name} from frozen state!")
        print(f" {self.item} thawed out!")
        self.status="Alive"
        if self.ability!="Harvest":
            self.item=None
    if other.item=="Aspear Berry" and other.status=="Frozen":
        print(f" {other.item} cured {other.name} from frozen state!")
        print(f" {other.item} thawed out!")
        other.status="Alive"
        if other.ability!="Harvest":
            other.item=None
    if self.item=="Pecha Berry" and self.status=="Badly Poisoned":
        print(f" {self.item} cured {self.name}'s poison!")
        self.status="Alive"
        if self.ability!="Harvest":
            self.item=None
    if other.item=="Pecha Berry" and other.status=="Badly Poisoned":
        print(f" {other.item} cured {other.name}'s poison!")
        other.status="Alive"
        if other.ability!="Harvest":
            other.item=None
    if self.item=="Lum Berry" and self.status!="Alive":
        print(f" {self.item} cured {self.name}'s status condition!")
        self.status="Alive"
        if self.ability!="Harvest":
            self.item=None        
    if other.item=="Lum Berry" and other.status!="Alive":
        print(f" {other.item} cured {other.name}'s status condition!")
        other.status="Alive"
        if other.ability!="Harvest":
            other.item=None                               
    self.dbond=False   
    if other.hp!=before and use!=None:
        self.miss=False
    if other.hp==before and use==None:
        self.miss=True
    if len(self.moves)>=1 and used==self.moves[0] and len(self.pplist)>=1:
        if self.pplist[0]==1:
            pp=1
        self.pplist[0]-=pp
    if len(self.moves)>=2 and used==self.moves[1] and len(self.pplist)>=2:
        if self.pplist[1]==1:
            pp=1
        self.pplist[1]-=pp
    if len(self.moves)>=3 and used==self.moves[2] and len(self.pplist)>=3:
        if self.pplist[2]==1:
            pp=1
        self.pplist[2]-=pp
    if len(self.moves)>=4 and used==self.moves[3] and len(self.pplist)>=4:
        if self.pplist[2]==1:
            pp=1
        self.pplist[3]-=pp
    if self.dmax is True and canatk is True:
        if used==self.maxmove[0]:
            self.pplist[0]-=pp
        if used==self.maxmove[1]:
            self.pplist[1]-=pp
        if used==self.maxmove[2]:
            self.pplist[2]-=pp
        if used==self.maxmove[3]:
            self.pplist[3]-=pp
    stancechange(self,used)
#PERCENTAGE       
    if before!=other.hp and before-other.hp>0 and self.ability!="Parental Bond":
        print(f" ({other.name} lost {per}% of its health!)")
    if self.hp!=sbefore and self==me and self.hp<sbefore and sper>0:
        print(f" Total damage received {sper}%")
    return self,other
#EFFECTS
def effects(self,other,tr,turn):
    print("  ")
    self.flinched=False
    if self.vlendturn==turn:
        self.vldmg=False
    if self.cnendturn==turn:
        self.cndmg=False
    if self.wfendturn==turn:
        self.wfdmg=False
    if self.magmaendturn==turn:
        self.magmadmg=False
    if tr.vcendturn==turn:
        tr.vcdmg=False
        print(" ⚠️ G-Max Volcalith ended on the opposing team!")
    if tr.vcdmg==True and self.hp>0:
        print(f" 🪨 {self.name} is hurt by the rocks thrown out by G-Max Volcalith!")
        if self.ability!="Magic Guard":
            self.hp-=(self.maxhp/6)         
    if self.vldmg==True and self.hp>0:
        print(f" 🌿 {self.name} is hurt by G-Max Vine Lash’s ferocious beating!")
        if self.ability!="Magic Guard":
            self.hp-=(self.maxhp/6)
    if self.cndmg==True and self.hp>0:
        print(f" 🌊 {self.name} is hurt by G-Max Cannonade’s vortex!")
        if self.ability!="Magic Guard":
            self.hp-=(self.maxhp/6)
    if self.wfdmg==True and self.hp>0:
        print(f" 🔥 {self.name} is hurt by G-Max Wildlife’s flames!")
        if self.ability!="Magic Guard":
            self.hp-=(self.maxhp/6)
    if self.magmadmg==True and self.hp>0 and "Magma Storm" in other.moves:
        print(f" 🌋 {self.name} was hurt by Magma Storm!")
        if other.item!="Binding Band" and self.ability!="Magic Guard":
            self.hp-=(self.maxhp/8)
        if other.item=="Binding Band" and self.ability!="Magic Guard":
            self.hp-=(self.maxhp/6)
    if self.bullrush==True:
        self.bullrush=False
    if self.name=="Mega Kangaskhan":
        self.ability="Parental Bond"
    if self.olock is True:
        defchange(self,-0.5)
        spdefchange (self,-0.5)
    if self.ability=="Speed Boost":
        print(f" {self.name}'s {self.ability}!")
        print(f" {self.name}'s speed rose.")
        speedchange(self,0.5)
    if 0 in self.pplist:
        if self.dmax is False:
            self.moves.remove(self.moves[self.pplist.index(0)])
        if self.dmax is True:
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
        self.name=self.name.split(" ")[-1]
        self.hp=round(self.hp/2)
        self.maxhp=round(self.maxhp/2)
        print(f" 🔻 {self.name} returned to it's normal state!")
    if self.item is None and other.item is not None and self.ability=="Pick Pocket":
        self.item=other.item
        other.item=None       
#FLINCH RESET    
    self.flinched=False
#GRASSY TERRAIN    
    if self.hp>0 and field.terrain =="Grassy" and self.hp<self.maxhp and self.ability not in ["Levitate"] and self.type1!="Flying" and self.type2!="Flying":
        print(f" 🌿 {self.name}'s HP was restored.")
        self.hp+=round(self.maxhp/16)
        if self.hp>self.maxhp:
            self.hp=self.maxhp 
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
        if self.ability=="Ice Body" and self.hp>0 and self.hp<self.maxhp:
            print(f" ❄️ {self.name}'s {self.ability}!")
            self.hp+=round(self.maxhp/8)        
        if self.hp>self.maxhp:
            self.hp=self.maxhp                          
    #BAD DREAMS
    if other.ability=="Bad Dreams" and self.status=="Sleep" and self.hp>0:
        self.hp-=round(self.maxhp/8)
        print(f" 💀 {self.name} is tormented.")
    #FROSTBITE
    if self.status=="Frostbite" and self.ability not in ["Magic Guard"] and self.hp>0:
        self.hp-=round(self.maxhp/16)
        print(f" 🥶 {self.name} was hurt by frostbite.")
    #LEECH SEED
    if self.seeded==True and self.hp>0:
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
        print(f" ☠️ {self.name} was hurt by poison.")        
    #BURN        
    if self.status=="Burned" and self.ability not in ["Magic Guard","Flare Boost"] and self.hp>0:
        self.hp-=(1+round(self.maxhp/16))
        print(f" 🔥 {self.name} was hurt by burn.")        
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
        
    #BLACK SLUDGE        
    if self.hp>0 and self.item=="Black Sludge" and self.hp<self.maxhp:
        if self.type1=="Poison" or self.type2=="Poison":
            print(f" ☠️ {self.name} restored a little HP using its Black Sludge.")
            self.hp+=(1+round(self.maxhp/16))
        elif self.type1!="Poison" and self.type2!="Poison":   
            print(f" ☠️ {self.name} lost a little HP using its Black Sludge.")
            self.hp-=(1+round(self.maxhp/8))
    #POISON HEAL        
    if self.hp>0 and self.ability=="Poison Heal" and self.hp!=self.maxhp and self.status=="Badly Poisoned":
        print(f" 🟣 {self.name} restored a little HP using its Poison Heal.")
        self.hp+=round(self.maxhp/8)                    

    if self.hp>self.maxhp:
        self.hp=self.maxhp
    if self.hp<0:
        self.hp=0