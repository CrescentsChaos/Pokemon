import random
from AItest import *
from typematchup import *
from hiddenpower import *
megastones=["Gyaradosite","Venusaurite","Charizardite X","Charizardite Y","Abomasite","Absolite","Aerodactylite","Aggronite","Alakazite","Altarianite","Amoharosite","Audinite","Banettite","Beedrillite","Blastoisinite","Blazikenite","Camerupite","Diancite","Galladite","Garchompite","Gardevoirite","Gengarite","Glalitite","Heracronite","Houndoominite","Kangaskhanite","Latiasite","Latiosite","Lopunnite","Lucarionite","Manectite","Mawilite","Medichamite","Metagrossite","Mewtwonite X","Mewtwonite Y","Pidgeotite","Pinsirite","Sablenite","Salamencite","Sceptilite","Scizorite","Sharpedonite","Slowbronite","Steelixite","Seampertite","Tyranitarite"]
#ENTRY EFFECTS            
def entryeff(self,other,trainer,trainer2,field,turn):
    pokeintro(self,other,trainer,trainer2,field,turn)
    #Berserk Gene
    if self.item=="Berserk Gene":
        print("===================================================================================")
        print(f" 💢 {self.name} is going berserk!")
        atkchange(self,self,0.5)
        spatkchange(self,self,0.5)
        self.confused==True
        print("===================================================================================")
    #Comatose
    if self.ability=="Comatose":
        print("===================================================================================")
        print(f" 🐨 {self.name}'s {self.ability}!")
        self.status="Drowsy"
        print("===================================================================================")
    #Flower Gift
    if self.ability=="Flower Gift" and field.weather in ["Sunny","Desolate Land"] and "Blossom" not in self.name:
        print("===================================================================================")
        print(f" 🌸 {self.name}'s {self.ability}!")
        self.name+="-Blossom"
        print("===================================================================================")
    #Anticipation
    if self.ability=="Anticipation":
        l=moveAI(other,self,trainer2,trainer,field)[1]
        dangermoves=["Explosion","Fissure","Sheer Cold","Horn Drill"]+l
        x=list(set(other.moves). intersection(dangermoves)) 
        if len(x)>0:
            x=str(x)[1:-1:]
            print("===================================================================================")
            print(f" 🕵️ {self.name}'s {self.ability}.")
            print(f" ⚠️ {other.name} has some risky moves like {x}!")
            print("===================================================================================")
    #Illusion
    if self.ability=="Illusion":
        self.name=trainer.pokemons[len(trainer.pokemons)-1].name.split(" ")[-1]
    #Pressure
    if self.ability=="Pressure" and other.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves:
        print("===================================================================================")
        print(f" 🦕 {self.name}'s {self.ability}!")
        print(f" {self.name} is exerting its pressure!")
        print("===================================================================================")
    #Bull Rush
    if self.ability=="Bull Rush":
        self.bullrush=True
    #Supreme Overlord
    if self.ability=="Supreme Overlord" and len(trainer.pokemons)!=6:
        print("===================================================================================")
        print(f" 👺 {self.name} gained strength from the fallen!")
        print("===================================================================================")
    #Frisk
    if self.ability=="Frisk":
        print("===================================================================================")
        print(f" 🔎 {self.name}'s {self.ability}!")
        print(f" ✅ {other.name} is holding {other.item}!")
        print("===================================================================================")
    #Air Lock/Cloud Nine
    if self.ability in ["Air Lock","Cloud Nine"] and field.weather!="Clear":
        print("===================================================================================")
        print(f" ☁️ {self.name}'s {self.ability}.\n The effects of the weather disappeared!")
        print("===================================================================================")
    #Delta Stream        
    if self.ability=="Delta Stream" and field.weather!="Strong Winds":
        print("===================================================================================")
        print(f" 🍃 {self.name}'s {self.ability}. Mysterious strong winds are protecting Flying-type Pokémon!")
        print("===================================================================================")
        field.weather="Strong Winds"
    #Stakeout        
    if self.ability=="Stakeout":
        self.atk*=2
        self.spatk*=2
    #All ability in party        
    abilitylist=[]
    for i in trainer.pokemons:
        abilitylist.append(i.ability)
    #Download        
    if self.ability=="Download":
        print("===================================================================================")
        print(f" 📩 {self.name}'s Download!")
        m=[a,b,c,d,e]=[other.atk,other.defense,other.spatk,other.spdef,other.speed]
        if trainer2.reflect==True:
            m=[other.atk,other.defense/2,other.spatk,other.spdef,other.speed]
        if trainer2.lightscreen==True:
            m=[other.atk,other.defense,other.spatk,other.spdef/2,other.speed]
        x=min(m)
        y=max(m)
        if y==a:
        	defchange(self,other,0.5)
        elif x==b:
        	atkchange(self,other,0.5)
        elif y==c:
        	spdefchange(self,other,0.5)
        elif x==d:
        	spatkchange(self,other,0.5)
        print("===================================================================================")
    #Commander        	
    if "Commander" in abilitylist and "Dondozo" in self.name:
        print("===================================================================================")
        print(f" 🪖 Tatsugiri's Commander!")
        atkchange(self,other,1)
        spatkchange(self,other,1)
        defchange(self,other,1)
        spdefchange(self,other,1)
        speedchange(self,other,1)
        print("===================================================================================")
    #Trace        
    if self.ability=="Trace" and other.ability not in ["As One","Battle Bond","Commander","Disguise","Forecast","Ice Face","Imposter","Illusion","Multitype","Power of Alchemy","Protosynthesis","Stance Change","Quark Drive","RKS System","Schooling","Trace","Zen Mode","Zero to Hero"] and other.item!="Ability Shield":
            print("===================================================================================")
            print(f" {self.name}'s {self.ability}!")        
            self.ability=other.ability
            print("===================================================================================")
    #Legendary Aura    
    if "Legendary" in self.name and self.item in ["Silver Feather","Crimson Orb","Navy Orb","Jade Orb","Rainbow Feather","Team Rocket Armor"]:
        print("===================================================================================")
        print(f" 🔱 {self.item} shrouded {self.name} with mystical energy!")
        self.hp*=6/len(trainer.pokemons)
        self.maxhp*=6/len(trainer.pokemons)
        print("===================================================================================")
    #Quark Drive
    if "Quark Drive" in self.ability and (field.terrain=="Electric" or self.item=="Booster Energy"):
        print("===================================================================================")
        print(f" ⚡ {self.name}'s {self.ability}!")
        print("===================================================================================")
    #Protosynthesis
    if "Protosynthesis" in self.ability and (field.weather in ["Sunny","Desolate Land"] or self.item=="Booster Energy"):
        print("===================================================================================")
        print(f" ☀️ {self.name}'s {self.ability}!")
        print("===================================================================================")
    #Costar
    if self.ability=="Costar":     
        print("===================================================================================")
        print(f" 🦩 {self.name}'s {self.ability}!")
        self.atkb=other.atkb
        self.defb=other.defb
        self.spatkb=other.spatkb
        self.spdefb=other.spdefb
        self.speedb=other.speedb   
        print("===================================================================================")
    #Imposter        
    if self.ability=="Imposter" and other.dmax is False:
        print("===================================================================================")
        print(f" 👾 {self.name}'s {self.ability}!")
        print(f' {self.name} transformed into {other.name}!')
        print("===================================================================================")
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
    #Sand Stream
    if (self.ability == "Sand Stream" or (self.ability=="Forecast" and self.item=="Smooth Rock")) and field.weather not in ["Sandstorm","Primordial Sea","Desolate Land"]:
        print("===================================================================================")
        print(f" 🏜️{self.name}'s {self.ability} whipped up a sandstorm!")
        field.weather="Sandstorm" 
        field.sandturn=turn
        field.sandend(self,other)
        print("===================================================================================")
    #Primordial Sea
    if self.ability=="Primordial Sea" and field.weather!="Primordial Sea":
        print("===================================================================================")
        print(f" 🌊 {self.name}'s {self.ability}. A heavy rain began to fall!")
        print("===================================================================================")
        field.weather="Primordial Sea"
    #Desolate Land
    if self.ability=="Desolate Land" and field.weather!="Desolate Land":
        print("===================================================================================")
        print(f" 🌋 {self.name}'s {self.ability}. The sunlight turned extremely harsh!")
        print("===================================================================================")
        field.weather="Desolate Land"
    #Drought/ Orichalcum Pulse
    if (self.ability in  ["Drought","Orichalcum Pulse"] or (self.ability=="Forecast" and self.item=="Heat Rock")) and field.weather not in ["Sunny","Primordial Sea","Desolate Land"]:
        print("===================================================================================")
        print(f" ☀️{self.name}'s {self.ability} intensified the sun's rays!")
        if self.ability=="Orichalcum Pulse":
            print(f" ♊ {self.name} turned the sunlight harsh, sending its ancient pulse into a frenzy!")
        field.weather="Sunny"
        field.sunturn=turn
        field.sunend(self,other)
        print("===================================================================================")
    #Drizzle
    if (self.ability == "Drizzle" or (self.ability=="Forecast" and self.item=="Damp Rock")) and field.weather not in ["Rainy","Primordial Sea","Desolate Land"]:
        print("===================================================================================")
        print(f" 🌧️{self.name}'s {self.ability} made it rain!")
        field.weather="Rainy"
        field.rainturn=turn
        field.rainend(self,other)
        print("===================================================================================")
    #Snow Warning
    if (self.ability == "Snow Warning" or (self.ability=="Forecast" and self.item=="Icy Rock")) and field.weather not in ["Primordial Sea","Desolate Land","Snowstorm"]:
        print("===================================================================================")
        print(f" 🌨️{self.name}'s {self.ability} whipped up a snowstorm!")
        field.weather="Snowstorm"      
        field.snowstormturn=turn
        field.snowstormend(self,other)     
        print("===================================================================================")   
    #Electric Surge/Hadron Engine
    if self.ability in ["Electric Surge","Hadron Engine"]:
        print("===================================================================================")
        print(f" {self.name}'s {self.ability}!")
        print(" ⚡ An electric self ran across the battlefield!")
        if self.ability=="Hadron Engine":
            print (f" ♐ {self.name} used the Electric Terrain to energize its futuristic engine!")
        field.terrain="Electric"
        field.eleturn=turn
        field.eleend(self,other)
        print("===================================================================================")
   #Misty Surge
    if self.ability=="Misty Surge":
        print("===================================================================================")
        print(f" {self.name}'s {self.ability}!")
        print(" 🌸 Mist swirled around the battlefield!")
        field.terrain="Misty"
        field.misturn=turn
        field.misend(self,other)
        print("===================================================================================")
    #Grassy Surge
    if self.ability in ["Grassy Surge","Dance of the Specter"]:
        print("===================================================================================")
        print(f" {self.name}'s {self.ability}!")
        print(" 🌿 Grass grew to cover the battlefield!")
        field.terrain="Grassy"
        field.grassturn=turn
        field.grassend(self,other)
        print("===================================================================================")
    #Psychic Surge
    if self.ability=="Psychic Surge":
        print("===================================================================================")
        print(f" {self.name}'s {self.ability}!")
        print(" 👁️ The battlefield got weird!")
        field.terrain="Psychic"        
        field.psyturn=turn
        field.psyend(self,other)      
        print("===================================================================================")
    #Spikes
    if "Spikes" in trainer.hazard and self.ability not in ["Magic Guard","Levitate","Shield Dust"] and self.item!="Heavy-Duty Boots":
        print("===================================================================================")
        print(f" ✴️ {self.name} was hurt by the Spikes!")
        print("===================================================================================")
        if trainer.hazard.count("Spikes")==3:
            self.hp-=(self.maxhp/4)
        if trainer.hazard.count("Spikes")==2:
            self.hp-=(self.maxhp/6)
        if trainer.hazard.count("Spikes")==1:
            self.hp-=(self.maxhp/8)
   #Toxic Spikes
    if "Toxic Spikes" in trainer.hazard and self.ability not in ["Magic Guard","Levitate","Shield Dust"] and self.item!="Heavy-Duty Boots" and "Steel" not in (self.type1,self.type2,self.teratype) and self.status=="Alive":
        if "Poison" in (self.type1,self.type2,self.teratype):
            trainer.hazard.remove("Toxic Spikes")
            print("===================================================================================")
            print(f" 💜 {self.name} absorbed the Toxic Spikes!")
            print("===================================================================================")
        else:
            if trainer.hazard.count("Toxic Spikes")==1:
                print("===================================================================================")
                print(f" ☣️ {self.name} was poisoned by toxic spikes!")
                print("===================================================================================")
                self.status="Poisoned"
            if trainer.hazard.count("Toxic Spikes")>=2:
                print("===================================================================================")
                print(f" ☣️ {self.name} was badly poisoned by toxic spikes!")
                print("===================================================================================")
                self.status="Badly Poisoned"
    #Sticky Web
    if "Sticky Web" in trainer.hazard and self.ability not in ["Magic Guard","Levitate","Shield Dust"] and self.item!="Heavy-Duty Boots":    
        print("===================================================================================")
        print(f" 🕸️ {self.name} fell into the sticky web!")   
        speedchange(self,other,-0.5)
        print("===================================================================================")
   #Stealth Rock
    if "Stealth Rock" in trainer.hazard and self.ability not in ["Magic Guard","Levitate","Shield Dust","Mountaineer"] and self.item!="Heavy-Duty Boots":
        buff=2
        #print(self.type1,self.type2)
        if self.type1 in ["Flying", "Bug", "Fire", "Ice"] and self.teratype=="None":
            buff*=2
        if self.type2 in ["Flying", "Bug", "Fire", "Ice"] and self.teratype=="None":
            buff*=2
        if self.teratype in ["Flying", "Bug", "Fire", "Ice"]:
            buff*=2
        if self.type1 in ['Fighting', 'Ground', 'Steel'] and self.teratype=="None":
            buff=1
        if self.type2 in ['Fighting', 'Ground', 'Steel'] and self.teratype=="None":
            buff=1
        if self.teratype in ['Fighting', 'Ground', 'Steel']:
            buff=1
        #print(buff)
        self.hp-=(1+(self.maxhp*0.0625*buff))
        print("===================================================================================")
        print(f" 🪨 Pointed stones dug into {self.name}!")
        print("===================================================================================")
    #Steel Spikes
    if "Steel Spikes" in trainer.hazard and self.ability not in ["Magic Guard","Levitate","Shield Dust"] and self.item!="Heavy-Duty Boots":
        buff=2
        #print(self.type1,self.type2)
        if self.type1 in ['Rock', 'Ice', 'Fairy'] and self.teratype=="None":
            buff*=2
        if self.type2 in ['Rock', 'Ice', 'Fairy'] and self.teratype=="None":
            buff*=2
        if self.teratype in ['Rock', 'Ice', 'Fairy']:
            buff*=2
        if self.type1 in ['Steel', 'Fire', 'Water', 'Electric'] and self.teratype=="None":
            buff=1
        if self.type2 in ['Steel', 'Fire', 'Water', 'Electric'] and self.teratype=="None":
            buff=1
        if self.teratype in ['Steel', 'Fire', 'Water', 'Electric']:
            buff=1
        #print(buff)
        self.hp-=(1+(self.maxhp*0.0625*buff))
        print("===================================================================================")
        print(f" 📌 The sharp steel bit into {self.name}!")
        print("===================================================================================")
    self.maxendturn(turn)
    prebuff(self,other,trainer,turn,field)
def mxmove(self,typem=typemoves):
    maxmove=[]
    gm="None"
    for i in self.moves:
        if i in typem.dragonmoves:
            gm="Max Wyrmwind"
            if "Duraludon" in self.name:
                gm="G-Max Depletion"
        if i in typem.normalmoves:
            gm="Max Strike"
            if "Snorlax" in self.name:
                gm="G-Max Replenish"
            if "Meowth" in self.name:
                gm="G-Max Gold Rush"
            if "Eevee" in self.name:
                gm="G-Max Cuddle"
        if i in typem.steelmoves:
            gm="Max Steelspike"
            if "Copperajah" in self.name:
                gm="G-Max Steelsurge"
            if "Melmetal" in self.name:
                gm="G-Max Meltdown"
        if i in typem.fairymoves:
            gm="Max Starfall"
            if "Hatterene" in self.name:
                gm="G-Max Smite"
            if "Alcremie" in self.name:
                gm="G-Max Finale"
        if i in typem.rockmoves:
            gm="Max Rockfall"
            if "Coalossal" in self.name:
                gm="G-Max Volcalith"
        if i in typem.groundmoves:
            gm="Max Quake"
            if "Sandaconda" in self.name:
                gm="G-Max Sandblast"
        if i in typem.ghostmoves:
            gm="Max Phantasm"
            if "Gengar" in self.name:
                gm="G-Max Terror"
        if i in typem.grassmoves:
            gm="Max Overgrowth"
            if "Venusaur" in self.name:
                gm="G-Max Vine Lash"
            if "Flapple" in self.name:
                gm="G-Max Tartness"
            if "Appletun" in self.name:
                gm="G-Max Sweetness"
            if "Rillaboom" in self.name:
                gm="G-Max Drum Solo"
        if i in typem.poisonmoves:
            gm="Max Ooze"
            if "Garbodor" in self.name:
                gm="G-Max Malodor"
        if i in typem.psychicmoves:
            gm="Max Mindstorm"
            if "Orbeetle" in self.name:
                gm="G-Max Gravitas"
        if i in typem.electricmoves:
            gm="Max Lightning"
            if "Pikachu" in self.name:
                gm="G-Max Volt Crash"
            if "Toxtricity" in self.name:
                gm="G-Max Stun Shock"
        if i in typem.fightingmoves:
            gm="Max Knuckle"
            if "Machamp" in self.name:
                gm="G-Max Chi Strike"
        if i in typem.icemoves:
            gm="Max Hailstorm"
            if "Lapras" in self.name:
                gm="G-Max Resonance"
        if i in typem.statusmove:
            gm="Max Guard"
        if i in typem.watermoves:
            gm="Max Geyser"
            if "Drednaw" in self.name:
                gm="G-Max Stonesurge"
            if "Rapid" in self.name:
                gm="G-Max Rapid Flow"
            if "Inteleon" in self.name:
                gm="G-Max Hydrosnipe"
            if "Kingler" in self.name:
                gm="G-Max Foam Burst"
            if "Blastoise" in self.name:
                gm="G-Max Cannonade"
        if i in typem.bugmoves:
            gm="Max Flutterby"
            if "Butterfree" in self.name:
                gm="G-Max Befuddle"
        if i in typem.darkmoves:
            gm="Max Darkness"
            if "Grimmsnarl" in self.name:
                gm="G-Max Snooze"
            if "Single" in self.name:
                gm="G-Max One Blow"
        if i in typem.flyingmoves:
            gm="Max Airstream"
            if "Corviknight" in self.name:
                gm="G-Max Wind Rage"
        if i in typem.firemoves:
            gm="Max Flare"
            if "Charizard" in self.name:
                gm="G-Max Wildfire"
            if "Cinderace" in self.name:
                gm="G-Max Fireball"
            if "Centiskorch" in self.name:
                gm="G-Max Centiferno"
        maxmove.append(gm)
    return maxmove
def rename(self):
    if self.dmax is True and ("Mega " not in self.name or "Z-Crystal" not in self.name):
        if self.name in ["Charizard","Blastoise","Venusaur","Pikachu","Butterfree","Snorlax","Machamp","Gengar","Kingler","Lapras","Garbodor","Melmetal","Rillaboom","Cinderace","Inteleon","Corviknight","Orbeetle","Drednaw","Coalossal","Copperajah","Flapple","Appletun","Sandaconda","Grimmsnarl","Hatterene","Toxtricity","Centiskorch","Alcremie","Duraludon","Single Strike Urshifu","Rapid Strike Urshifu","Centiskorch","Meowth"]:
            self.name="Gigantamax "+self.name
        if "Toxtricity" in self.name:
            self.name="Gigantamax Toxtricity"
        if "Gigantamax " not in self.name:
            self.name="Dynamax "+self.name
def pokeintro(self,other,trainer,trainer2,field,turn):
    trname=trainer.name.split(" ")[-1]
    if self.ability=="Intimidate" and other.ability not in ["Inner Focus","Oblivious","Clear Body","Good as Gold"] and self.item not in ["Clear Amulet"] and self.abilityused==False:
        self.abilityused=True
        if other.ability!="Guard Dog":         
            print(f" 👹 {self.name}'s {self.ability}!")
            atkchange(other,self,-0.5)
        if other.ability=="Guard Dog":           
            print(f" 👹 {self.name}'s {self.ability}!")
            print(f" 🐕‍🦺 {other.name}'s {other.ability}!")
            atkchange(other,self,0.5)            
        if other.item=="Adrenaline Orb":            
            print(f" {other.name}'s speed was raised by the Adrenaline Orb.")
            speedchange(other,self,0.5)
    if self.ability=="Vessel of Ruin":
        print(f" ♉ {self.name}'s {self.ability} weakened the Sp.Atk of all surrounding Pokémon!")
    if self.ability=="Tablets of Ruin":
        print(f" ♈ {self.name}'s {self.ability} weakened the Atk of all surrounding Pokémon!")
    if self.ability=="Sword of Ruin":
        print(f" ♐ {self.name}'s {self.ability} weakened the Defense of all surrounding Pokémon!")
    if self.ability=="Beads of Ruin":
        print(f" ♋ {self.name}'s {self.ability} weakened the Sp.Def of all surrounding Pokémon!")
    if self.item!="None" and "Quick Claw" in self.item:
        print(f" ✴️ {self.name} flashed its Quick Claw!")
    if self.item!="None" and "Air Balloon" in self.item:
        print(f" 🎈 {self.name} floats in the air with its Air Balloon!")
    if self.ability=="Turboblaze":
        print(f" 🔥 {self.name} is radiating a blazing aura!")  
    if self.ability=="Teravolt":
        print(f" ⚡ {self.name} is radiating a bursting aura!")  
    if self.ability=="Fairy Aura":
        print(f" 🧚‍♀️ {self.name} is radiating a fairy aura!")  
    if self.ability=="Dark Aura":
        print(f" 🌑 {self.name} is radiating a dark aura!")  
    if self.ability=="Aura Break":
        print(f" 🧬 {self.name} reversed all the other pokemons aura!")  
    if self.ability=="Mold Breaker":
        print(f" {self.name} breaks the mold!")        
    if "Alpha " in self.name:
        prevname=self.name.split("Alpha ")[-1]
        print(f" 👹 {prevname}'s alpha aura spreading in the air!")
    if self.item=="Griseous Core" and "Origin" not in self.name:
        print(f" ♑ {self.name}'s Origin Reversion! It reverted to its origin form!")
        self.name="Origin Giratina"
        per=self.hp/self.maxhp
        self.ability="Levitate"
        self.hp=150
        self.atk=120
        self.defense=100
        self.spatk=120
        self.spdef=100
        self.speed=90
        self.calcst()
        self.hp=self.maxhp*per
    if self.item=="Adamant Crystal" and "Origin" not in self.name:
        print(f" ♐ {self.name}'s Origin Reversion! It reverted to its origin form!")
        self.name="Origin Dialga"
        per=self.hp/self.maxhp
        self.hp=100
        self.atk=100
        self.defense=120
        self.spatk=150
        self.spdef=120
        self.speed=90
        self.calcst()
        self.hp=self.maxhp*per
    if self.item=="Lustrous Globe" and "Origin" not in self.name:
        print(f" ♓ {self.name}'s Origin Reversion! It reverted to its origin form!")
        self.name="Origin Palkia"
        per=self.hp/self.maxhp
        self.hp=90
        self.atk=100
        self.defense=100
        self.spatk=150
        self.spdef=120
        self.speed=120
        self.calcst()
        self.hp=self.maxhp*per
    if self.megaintro is False and self.item=="Blue Orb":
        prevname=self.name.split(" ")[-1]
        print(f" ⛎ {prevname}'s Primal Reversion! It reverted to its primal form!")
        self.name="Primal Kyogre"
        per=self.hp/self.maxhp
        self.ability="Primordial Sea"
        self.hp=100
        self.atk=150
        self.defense=90
        self.spatk=180
        self.spdef=160
        self.speed=90
        self.calcst()
        self.hp=self.maxhp*per
        self.megaintro=True
    if self.ability=="Intrepid Sword":
        print(f" 🗡️ {self.name}'s {self.ability}!")
        atkchange(self,other,0.5)      
    if self.ability=="Dauntless Shield":
        print(f" 🛡️ {self.name}'s {self.ability}!")
        defchange(self,other,0.5)
    if self.megaintro is False and self.item=="Red Orb":
        prevname=self.name.split(" ")[-1]
        print(f" ♉ {prevname}'s Primal Reversion! It reverted to its primal form!")
        self.name="Primal Groudon"
        per=self.hp/self.maxhp
        self.ability="Desolate Land"
        self.type2="Fire"
        self.hp=100
        self.atk=180
        self.defense=160
        self.spatk=150
        self.spdef=90
        self.speed=90
        self.calcst()
        self.hp=self.maxhp*per
        self.megaintro=True
def statchange(self,other,tr1,turn):
    hpbuff=1
    atkbuff=1
    defbuff=1
    spatkbuff=1
    spdefbuff=1
    speedbuff=1
    
def transformation(self,other,turn):
    print("===================================================================================")
    self.abilityused=False
    trname=self.owner.name.split(" ")[-1]
    if "💎" in self.name:
        if self.maxiv in ["Rock","Fire","Water","Grass","Electric","Ground","Flying","Fighting","Fairy","Dragon","Steel","Poison","Dark","Ghost","Normal","Bug","Ice"]:
            self.teratype=self.tera
        typ="None"
        if self.teratype =="None" and self.maxiv not in ["Rock","Fire","Water","Grass","Electric","Ground","Flying","Fighting","Fairy","Dragon","Steel","Poison","Dark","Ghost","Normal","Bug","Ice"]:
            self.teratype=self.tera
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
            typ="🥊"
        if self.teratype=="Dark":
            typ="👿"
        if self.teratype=="Fairy":
            typ="❤️"
        if self.teratype=="Flying":
            typ="🎈"
        if self.teratype=="Poison":
            typ="☠️"
        if self.teratype=="Ground":
            typ="🌍"
        if self.teratype=="Rock":
            typ="🏛️"
        if self.teratype=="Grass":
            typ="🌻"
        if self.teratype=="Electric":
            typ="💡"
        if self.teratype=="Water":
            typ="⛲"
        if self.teratype=="Fire":
            typ="🕯️"
        name=self.name.split("💎")[0]
        self.name=self.name[:-1]+"-"+self.teratype
        print(f" {typ} {name} has Terastallized into the {self.teratype}-type❗")
        self.owner.cantera=False
    if self.dmax==True:
        self.maxend=turn+2
        self.maxhp*=2
        self.hp*=2
        rename(self)
        self.maxmove=mxmove(self,typemoves)
        prevname=self.name.split(" ")[-1]
        nn=False
        prdx=["Great Tusk","Sandy Shocks","Roaring Moon","Brute Bonnet","Slither Wing","Flutter Mane","Scream Tail","Iron","Unbound","Tapu"]
        for i in prdx:
            if i in self.name:
                nn=True
        if nn==False:
            prevname=self.name.split(" ")[-1]
        if nn==True:
            prevname=self.name[8:]
        if "Dynamax" in self.name:
            print(f" ⭕ {prevname} returned and synced with {trname}'s Dynamax Band!")
            print(f" 🔺{self.owner.name} dynamaxed {prevname}!")
            self.megaintro=True
        if "Gigantamax" in self.name:
            print(f" ⭕ {prevname} returned and synced with {trname}'s Dynamax Band!")
            print(f" 🔺{self.owner.name} gigantamaxed {prevname}!")
    if self.item!="None" and "Ultra" not in self.name and "Ultranecrozium Z" in self.item:
        prevname=self.name.split("(")[0]
        self.name="Ultra Necrozma"
        print(f" ✴️{prevname} regained its true power through Ultra Burst!")
        per=self.hp/self.maxhp
        self.ability="Neuroforce"
        self.type2="Dragon"
        self.hp=97
        self.atk=167
        self.defense=97
        self.spatk=167
        self.spdef=97
        self.speed=129
        self.calcst()
        self.hp=self.maxhp*per
    if (("Mega" not in self.name) and (self.item in megastones or "Dragon Ascent" in self.moves) and self.owner.canmega==True) and self.dmax==False:
        prevname=self.name.split(" ")[-1]
        trname=self.owner.name.split(" ")[-1]
        self.name="Mega "+self.name
        if "Rayquaza" not in self.name:
            if self.item=="Charizardite X":
                self.name="Mega Charizard X"
            if self.item=="Charizardite Y":
                self.name="Mega Charizard Y"
            if self.item=="Mewtwonite X":
                self.name="Mega Mewtwo X"
            if self.item=="Mewtwonite Y":
                self.name="Mega Mewtwo Y"
            print(f" 🧬 {prevname}'s {self.item} is reacting to {trname}'s Keystone!\n {prevname} has Mega Evolved into {self.name}!")
        if "Rayquaza" in self.name:
            print(f" 🧬 {trname}'s fervent wish has reached {prevname}!\n {prevname} Mega evolved into {self.name}!")
        if self.item=="Gyaradosite":
            self.type2="Dark"
            self.ability="Mold Breaker"
            per=self.hp/self.maxhp
            self.hp=95
            self.atk=155
            self.defense=109
            self.spatk=70
            self.spdef=130
            self.speed=81
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False
        if self.item=="Venusaurite":
            self.ability="Thick Fat"
            per=self.hp/self.maxhp
            self.hp=80
            self.atk=100
            self.defense=123
            self.spatk=122
            self.spdef=120
            self.speed=80
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False
        if self.item=="Charizardite X":
            self.ability="Tough Claws"
            self.type2="Dragon"
            per=self.hp/self.maxhp
            self.hp=78
            self.atk=130
            self.defense=111
            self.spatk=130
            self.spdef=130
            self.speed=100
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False
        if self.item=="Charizardite Y":
            self.ability="Drought"
            per=self.hp/self.maxhp
            self.hp=78
            self.atk=104
            self.defense=78
            self.spatk=159
            self.spdef=115
            self.speed=100
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False
        if self.item=="Blastoisinite":
            self.ability="Mega Launcher"
            per=self.hp/self.maxhp
            self.hp=79
            self.atk=103
            self.defense=120
            self.spatk=135
            self.spdef=115
            self.speed=78
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False    
        if self.item=="Beedrillite":
            self.ability="Adaptability"
            per=self.hp/self.maxhp
            self.hp=65
            self.atk=150
            self.defense=40
            self.spatk=15
            self.spdef=80
            self.speed=145
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False      
        if self.item=="Pidgeotite":
            self.ability="No Guard"
            per=self.hp/self.maxhp
            self.hp=83
            self.atk=80
            self.defense=80
            self.spatk=135
            self.spdef=80
            self.speed=121
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False     
        if self.item=="Alakazite":
            self.ability="Trace"
            per=self.hp/self.maxhp
            self.hp=55
            self.atk=50
            self.defense=65
            self.spatk=175
            self.spdef=105
            self.speed=150
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False  
        if self.item=="Slowbronite":
            self.ability="Regenerator"
            per=self.hp/self.maxhp
            self.hp=95
            self.atk=75
            self.defense=180
            self.spatk=130
            self.spdef=80
            self.speed=30
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False 
        if self.item=="Gengarite":
            self.ability="Shadow Tag"
            per=self.hp/self.maxhp
            self.hp=60
            self.atk=65
            self.defense=80
            self.spatk=170
            self.spdef=95
            self.speed=130
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False       
        if self.item=="Kangaskhanite":
            self.ability="Parental Bond"
            per=self.hp/self.maxhp
            self.hp=105
            self.atk=125
            self.defense=100
            self.spatk=60
            self.spdef=100
            self.speed=100
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False       
        if self.item=="Pinsirite":
            self.ability="Aerilate"
            self.type2="Flying"
            per=self.hp/self.maxhp
            self.hp=65
            self.atk=155
            self.defense=130
            self.spatk=65
            self.spdef=90
            self.speed=105
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False         
        if self.item=="Aerodactylite":
            self.ability="Tough Claws"
            per=self.hp/self.maxhp
            self.hp=80
            self.atk=135
            self.defense=85
            self.spatk=70
            self.spdef=95
            self.speed=150
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False
        if self.item=="Mewtwonite X":
            self.ability="Steadfast"
            self.type2="Fighting"
            per=self.hp/self.maxhp
            self.hp=106
            self.atk=190
            self.defense=100
            self.spatk=154
            self.spdef=100
            self.speed=130
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False    
        if self.item=="Mewtwonite Y":
            self.ability="Insomnia"
            per=self.hp/self.maxhp
            self.hp=106
            self.atk=150
            self.defense=70
            self.spatk=194
            self.spdef=120
            self.speed=140
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False     
        if self.item=="Ampharosite":
            self.ability=random.choice(["Thick Fat","Mold Breaker"])
            self.type2="Dragon"
            per=self.hp/self.maxhp
            self.hp=90
            self.atk=95
            self.defense=105
            self.spatk=165
            self.spdef=110
            self.speed=45
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False
        if self.item=="Steelixite":
            self.ability="Heatproof"
            per=self.hp/self.maxhp
            self.hp=75
            self.atk=125
            self.defense=230
            self.spatk=55
            self.spdef=95
            self.speed=30
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False   
        if self.item=="Scizorite":
            self.ability="Technician"
            per=self.hp/self.maxhp
            self.hp=70
            self.atk=150
            self.defense=140
            self.spatk=65
            self.spdef=100
            self.speed=75
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False  
        if self.item=="Heracronite":
            self.ability="Skill Link"
            per=self.hp/self.maxhp
            self.hp=80
            self.atk=185
            self.defense=115
            self.spatk=40
            self.spdef=105
            self.speed=75
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False
        if self.item=="Houndoominite":
            self.ability=random.choice(["Solar Power","Dark Aura"])
            per=self.hp/self.maxhp
            self.hp=75
            self.atk=110
            self.defense=90
            self.spatk=140
            self.spdef=90
            self.speed=115
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False
        if self.item=="Tyranitarite":
            self.ability="Sand Stream"
            per=self.hp/self.maxhp
            self.hp=100
            self.atk=164
            self.defense=150
            self.spatk=95
            self.spdef=120
            self.speed=71
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False    
        if self.item=="Sceptilite":
            self.ability="Technician"
            self.type2="Dragon"
            per=self.hp/self.maxhp
            self.hp=70
            self.atk=135
            self.defense=75
            self.spatk=110
            self.spdef=85
            self.speed=145
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False
        if self.item=="Blazikenite":
            self.ability="Speed Boost"
            per=self.hp/self.maxhp
            self.hp=80
            self.atk=160
            self.defense=80
            self.spatk=130
            self.spdef=80
            self.speed=100
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False
        if self.item=="Swampertite":
            self.ability="Swift Swim"
            per=self.hp/self.maxhp
            self.hp=100
            self.atk=150
            self.defense=110
            self.spatk=95
            self.spdef=110
            self.speed=70
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False
        if self.item=="Gardevoirite":
            self.ability="Pixilate"
            per=self.hp/self.maxhp
            self.hp=68
            self.atk=85
            self.defense=65
            self.spatk=165
            self.spdef=135
            self.speed=100
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False
        if self.item=="Sablenite":
            self.ability="Magic Bounce"
            per=self.hp/self.maxhp
            self.hp=50
            self.atk=85
            self.defense=125
            self.spatk=85
            self.spdef=115
            self.speed=20
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False
        if self.item=="Mawilite":
            self.ability="Huge Power"
            per=self.hp/self.maxhp
            self.hp=50
            self.atk=105
            self.defense=125
            self.spatk=55
            self.spdef=95
            self.speed=50
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False
        if self.item=="Aggronite":
            self.ability="Filter"
            self.type2="None"
            per=self.hp/self.maxhp
            self.hp=70
            self.atk=140
            self.defense=230
            self.spatk=60
            self.spdef=80
            self.speed=50
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False    
        if self.item=="Medichamite":
            self.ability="Pure Power"
            per=self.hp/self.maxhp
            self.hp=60
            self.atk=100
            self.defense=85
            self.spatk=80
            self.spdef=85
            self.speed=100
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False
        if self.item=="Manectite":
            self.ability="Intimidate"
            per=self.hp/self.maxhp
            self.hp=70
            self.atk=75
            self.defense=80
            self.spatk=135
            self.spdef=80
            self.speed=135
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False
        if self.item=="Sharpedonite":
            self.ability="Strong Jaw"
            per=self.hp/self.maxhp
            self.hp=70
            self.atk=140
            self.defense=70
            self.spatk=110
            self.spdef=65
            self.speed=105
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False
        if self.item=="Camerupite":
            self.ability="Sheer Force"
            per=self.hp/self.maxhp
            self.hp=90
            self.atk=100
            self.defense=110
            self.spatk=145
            self.spdef=115
            self.speed=20
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False
        if self.item=="Altarianite":
            self.ability="Pixilate"
            self.type2="Fairy"
            per=self.hp/self.maxhp
            self.hp=85
            self.atk=110
            self.defense=110
            self.spatk=110
            self.spdef=105
            self.speed=80
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False
        if self.item=="Banettite":
            self.ability="Prankster"
            self.type2="Normal"
            per=self.hp/self.maxhp
            self.hp=64
            self.atk=165
            self.defense=75
            self.spatk=93
            self.spdef=83
            self.speed=75
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False
        if self.item=="Absolite":
            self.ability=random.choice(["Magic Bounce","Sharpness"])
            self.type2="Fairy"
            per=self.hp/self.maxhp
            self.hp=65
            self.atk=150
            self.defense=60
            self.spatk=115
            self.spdef=60
            self.speed=115
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False
        if self.item=="Glalitite":
            self.ability="Refrigerate"
            per=self.hp/self.maxhp
            self.hp=80
            self.atk=135
            self.defense=80
            self.spatk=105
            self.spdef=80
            self.speed=100
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False
        if self.item=="Salamencite":
            self.ability="Aerilate"
            per=self.hp/self.maxhp
            self.hp=95
            self.atk=145
            self.defense=130
            self.spatk=120
            self.spdef=90
            self.speed=120
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False
        if self.item=="Metagrossite":
            self.ability="Tough Claws"
            per=self.hp/self.maxhp
            self.hp=80
            self.atk=145
            self.defense=150
            self.spatk=105
            self.spdef=110
            self.speed=110
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False
        if self.item=="Latiasite":
            per=self.hp/self.maxhp
            self.hp=80
            self.atk=100
            self.defense=120
            self.spatk=140
            self.spdef=150
            self.speed=110
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False
        if self.item=="Latiosite":
            per=self.hp/self.maxhp
            self.hp=80
            self.atk=139
            self.defense=100
            self.spatk=160
            self.spdef=120
            self.speed=110
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False
        if "Dragon Ascent" in self.moves:
            self.ability="Delta Stream"
            per=self.hp/self.maxhp
            self.hp=105
            self.atk=180
            self.defense=100
            self.spatk=180
            self.spdef=100
            self.speed=115
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False
        if self.item=="Lopunnite":
            self.ability="Scrappy"
            per=self.hp/self.maxhp
            self.hp=65
            self.atk=136
            self.defense=94
            self.spatk=54
            self.spdef=96
            self.speed=135
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False
        if self.item=="Garchompite":
            self.ability="Sand Force"
            per=self.hp/self.maxhp
            self.hp=108
            self.atk=170
            self.defense=105
            self.spatk=120
            self.spdef=95
            self.speed=102
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False
        if self.item=="Lucarionite":
            self.ability="Adaptability"
            per=self.hp/self.maxhp
            self.hp=70
            self.atk=145
            self.defense=88
            self.spatk=140
            self.spdef=70
            self.speed=112
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False
        if self.item=="Abomasite":
            self.ability="Slush Rush"
            per=self.hp/self.maxhp
            self.hp=90
            self.atk=132
            self.defense=105
            self.spatk=132
            self.spdef=105
            self.speed=60
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False
        if self.item=="Lopunnite":
            self.ability="Scrappy"
            per=self.hp/self.maxhp
            self.hp=80
            self.atk=139
            self.defense=100
            self.spatk=160
            self.spdef=120
            self.speed=110
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False
        if self.item=="Galladite":
            self.ability="Sharpness"
            per=self.hp/self.maxhp
            self.hp=68
            self.atk=165
            self.defense=95
            self.spatk=65
            self.spdef=115
            self.speed=110
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False
        if self.item=="Audinite":
            self.ability="Regenerator"
            self.type2="Fairy"
            per=self.hp/self.maxhp
            self.hp=103
            self.atk=60
            self.defense=126
            self.spatk=80
            self.spdef=126
            self.speed=50
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False
        if self.item=="Diancite":
            self.ability="Magic Bounce"
            per=self.hp/self.maxhp
            self.hp=50
            self.atk=160
            self.defense=110
            self.spatk=160
            self.spdef=110
            self.speed=110
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False
        entryeff(self,other,self.owner,other.owner,field,turn)
    print("===================================================================================")        
    #prebuff(self,other,self.owner,turn,field)