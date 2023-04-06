import random
from quotes import *
from AItest import *
from typematchup import *
from hiddenpower import *
megastones=["Gyaradosite","Venusaurite","Charizardite X","Charizardite Y","Abomasite","Absolite","Aerodactylite","Aggronite","Alakazite","Altarianite","Ampharosite","Audinite","Banettite","Beedrillite","Blastoisinite","Blazikenite","Camerupite","Diancite","Galladite","Garchompite","Gardevoirite","Gengarite","Glalitite","Heracronite","Houndoominite","Kangaskhanite","Latiasite","Latiosite","Lopunnite","Lucarionite","Manectite","Mawilite","Medichamite","Metagrossite","Mewtwonite X","Mewtwonite Y","Pidgeotite","Pinsirite","Sablenite","Salamencite","Sceptilite","Scizorite","Sharpedonite","Slowbronite","Steelixite","Seampertite","Tyranitarite"]
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
    if other.ability=="Frisk":
        print("===================================================================================")
        print(f" 🔎 {other.name}'s {other.ability}!")
        print(f" ✅ {other.name} frisked and found {self.name}'s {self.item}!")
        print("===================================================================================")
    if self.ability=="Frisk":
        print("===================================================================================")
        print(f" 🔎 {self.name}'s {self.ability}!")
        print(f" ✅ {self.name} frisked and found {other.name}'s {other.item}!")
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
    if "Wild" in self.name:
        print("===================================================================================")
        print(f" ⚜️ {self.name} was shrouded with mystical energy!")
        self.hp*=6/len(trainer.pokemons)
        self.maxhp*=6/len(trainer.pokemons)
        print("===================================================================================")
    #Quark Drive
    if "Quark Drive" in self.ability and field.terrain=="Electric" and ("Booster" not in self.item or "Used" in self.item):
        print("===================================================================================")
        print(f" ⚡ Electric Terrain activated {self.name}'s {self.ability}!")
        print("===================================================================================")
    #Protosynthesis
    if "Protosynthesis" in self.ability and field.weather in ["Sunny","Desolate Land"] and ("Booster" not in self.item or "Used" in self.item):
        print("===================================================================================")
        print(f" ☀️ Harsh sunlight activated {self.name}'s {self.ability}!")
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
        print(colored("===================================================================================","yellow"))
        print(f" ☀️{self.name}'s {self.ability} intensified the sun's rays!")
        if self.ability=="Orichalcum Pulse":
            print(f" ♊ {self.name} turned the sunlight harsh, sending its ancient pulse into a frenzy!")
        field.weather="Sunny"
        field.sunturn=turn
        field.sunend(self,other)
        print(colored("===================================================================================","yellow"))
    #Drizzle
    if (self.ability == "Drizzle" or (self.ability=="Forecast" and self.item=="Damp Rock")) and field.weather not in ["Rainy","Primordial Sea","Desolate Land"]:
        print(colored("===================================================================================","blue"))
        print(f" 🌧️{self.name}'s {self.ability} made it rain!")
        field.weather="Rainy"
        field.rainturn=turn
        field.rainend(self,other)
        print(colored("===================================================================================","blue"))
    #Snow Warning
    if (self.ability == "Snow Warning" or (self.ability=="Forecast" and self.item=="Icy Rock")) and field.weather not in ["Primordial Sea","Desolate Land","Snowstorm"]:
        print(colored("===================================================================================","cyan"))
        print(f" 🌨️{self.name}'s {self.ability} whipped up a snowstorm!")
        field.weather="Snowstorm"      
        field.snowstormturn=turn
        field.snowstormend(self,other)     
        print(colored("===================================================================================","cyan"))
    #Electric Surge/Hadron Engine
    if self.ability in ["Electric Surge","Hadron Engine"]:
        print(colored("===================================================================================","yellow"))
        print(f" {self.name}'s {self.ability}!")
        print(" ⚡ An electric self ran across the battlefield!")
        if self.ability=="Hadron Engine":
            print (f" ♐ {self.name} used the Electric Terrain to energize its futuristic engine!")
        field.terrain="Electric"
        field.eleturn=turn
        field.eleend(self,other)
        print(colored("===================================================================================","yellow"))
   #Misty Surge
    if self.ability=="Misty Surge":
        print(colored("===================================================================================","magenta"))
        print(f" {self.name}'s {self.ability}!")
        print(" 🌸 Mist swirled around the battlefield!")
        field.terrain="Misty"
        field.misturn=turn
        field.misend(self,other)
        print(colored("===================================================================================","magenta"))
    #Grassy Surge
    if self.ability in ["Grassy Surge","Dance of the Specter"]:
        print(colored("===================================================================================","green"))
        print(f" {self.name}'s {self.ability}!")
        print(" 🌿 Grass grew to cover the battlefield!")
        field.terrain="Grassy"
        field.grassturn=turn
        field.grassend(self,other)
        print(colored("===================================================================================","green"))
    #Psychic Surge
    if self.ability=="Psychic Surge":
        print(colored("===================================================================================","magenta"))
        print(f" {self.name}'s {self.ability}!")
        print(" 👁️ The battlefield got weird!")
        field.terrain="Psychic"        
        field.psyturn=turn
        field.psyend(self,other)      
        print(colored("===================================================================================","magenta"))
    #Spikes
    if "Spikes" in trainer.hazard and self.ability not in ["Magic Guard","Levitate","Shield Dust"] and self.item not in ["Heavy-Duty Boots","Air Balloon"]:
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
    if "Toxic Spikes" in trainer.hazard and self.ability not in ["Magic Guard","Levitate","Shield Dust"] and self.item not in ["Heavy-Duty Boots","Air Balloon"] and "Steel" not in (self.type1,self.type2,self.teratype) and self.status=="Alive":
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
    if "Sticky Web" in trainer.hazard and self.ability not in ["Magic Guard","Levitate","Shield Dust"] and self.item not in ["Heavy-Duty Boots","Air Balloon"]:    
        print("===================================================================================")
        print(f" 🕸️ {self.name} fell into the sticky web!")   
        speedchange(self,other,-0.5)
        print("===================================================================================")
   #Stealth Rock
    if "Stealth Rock" in trainer.hazard and self.ability not in ["Magic Guard","Levitate","Shield Dust","Mountaineer"] and self.item not in ["Heavy-Duty Boots","Air Balloon"]:
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
    if "Steel Spikes" in trainer.hazard and self.ability not in ["Magic Guard","Levitate","Shield Dust"] and self.item not in ["Heavy-Duty Boots","Air Balloon"]:
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
            self.name=f"Gigantamax {self.name}"
        if "Toxtricity" in self.name:
            self.name="Gigantamax Toxtricity"
        if "Gigantamax " not in self.name:
            self.name=f"Dynamax {self.name}"
def pokeintro(self,other,trainer,trainer2,field,turn):
    trname=trainer.name.split(" ")[-1]
    if self.ability=="Intimidate" and other.ability not in ["Inner Focus","Oblivious","Clear Body","Good as Gold"] and self.item not in ["Clear Amulet"]:
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
        print(colored("===================================================================================","red"))
        print(f" ♉ {self.name}'s {self.ability} weakened the Sp.Atk of all surrounding Pokémon!")
        print(colored("===================================================================================","red"))
    if self.ability=="Tablets of Ruin":
        print(colored("===================================================================================","green"))
        print(f" ♈ {self.name}'s {self.ability} weakened the Atk of all surrounding Pokémon!")
        print(colored("===================================================================================","green"))
    if self.ability=="Sword of Ruin":
        print(colored("===================================================================================","cyan"))
        print(f" ♐ {self.name}'s {self.ability} weakened the Defense of all surrounding Pokémon!")
        print(colored("===================================================================================","cyan"))
    if self.ability=="Beads of Ruin":
        print(colored("===================================================================================","red"))
        print(f" ♋ {self.name}'s {self.ability} weakened the Sp.Def of all surrounding Pokémon!")
        print(colored("===================================================================================","red"))
    if self.item!="None" and "Quick Claw" in self.item:
        print(f" ✴️ {self.name} flashed its Quick Claw!")
    if self.item!="None" and "Air Balloon" in self.item:
        print(f" 🎈 {self.name} floats in the air with its Air Balloon!")
    if self.ability=="Turboblaze":
        print(colored("===================================================================================","red"))
        print(f" 🔥 {self.name} is radiating a blazing aura!")  
        print(colored("===================================================================================","red"))
    if self.ability=="Teravolt":
        print(colored("===================================================================================","yellow"))
        print(f" ⚡ {self.name} is radiating a bursting aura!")  
        print(colored("===================================================================================","yellow"))
    if self.ability=="Fairy Aura":
        print(colored("===================================================================================","magenta"))
        print(f" 🧚‍♀️ {self.name} is radiating a fairy aura!")  
        print(colored("===================================================================================","magenta"))
    if self.ability=="Dark Aura":
        print(colored("===================================================================================","red"))
        print(f" 🌑 {self.name} is radiating a dark aura!")  
        print(colored("===================================================================================","red"))
    if self.ability=="Aura Break":
        print(colored("===================================================================================","green"))
        print(f" 🧬 {self.name} reversed all the other pokemons aura!")  
        print(colored("===================================================================================","green"))
    if self.ability=="Mold Breaker":
        print(colored("===================================================================================","red"))
        print(f" {self.name} breaks the mold!")    
        print(colored("===================================================================================","red"))    
    if "Alpha " in self.name:
        prevname=self.name.split("Alpha ")[-1]
        print(colored("===================================================================================","red"))
        print(f" 👹 {prevname}'s alpha aura spreading in the air!")
        print(colored("===================================================================================","red"))
    if self.item=="Griseous Core" and "Origin" not in self.name:
        print(colored("===================================================================================","red"))
        print(f" ♑ {self.name}'s Origin Reversion! It reverted to its origin form!")
        print(colored("===================================================================================","red"))
        self.name="Origin Giratina"
        per=self.hp/self.maxhp
        self.ability="Levitate"
        self.weight=1433
        self.sprite="sprites/Origin Giratina.png"
        self.hp=150
        self.atk=120
        self.defense=100
        self.spatk=120
        self.spdef=100
        self.speed=90
        self.calcst()
        self.hp=self.maxhp*per
    if self.item=="Adamant Crystal" and "Origin" not in self.name:
        print(colored("===================================================================================","blue"))
        print(f" ♐ {self.name}'s Origin Reversion! It reverted to its origin form!")
        print(colored("===================================================================================","blue"))
        self.name="Origin Dialga"
        per=self.hp/self.maxhp
        self.sprite="sprites/Origin Dialga.png"
        self.weight=1873.9
        self.hp=100
        self.atk=100
        self.defense=120
        self.spatk=150
        self.spdef=120
        self.speed=90
        self.calcst()
        self.hp=self.maxhp*per
    if self.item=="Lustrous Globe" and "Origin" not in self.name:
        print(colored("===================================================================================","magenta"))
        print(f" ♓ {self.name}'s Origin Reversion! It reverted to its origin form!")
        print(colored("===================================================================================","magenta"))
        self.name="Origin Palkia"
        per=self.hp/self.maxhp
        self.weight=1455.1
        self.sprite="sprites/Origin Palkia.png"
        self.hp=90
        self.atk=100
        self.defense=100
        self.spatk=150
        self.spdef=120
        self.speed=120
        self.calcst()
        self.hp=self.maxhp*per
    if self.megaintro is False and self.item in ["Blue Orb","Navy Orb"]:
        prevname=self.name.split(" ")[-1]
        print(colored("===================================================================================","blue"))
        print(f" ⛎ {prevname}'s Primal Reversion! It reverted to its primal form!")
        self.sprite="sprites/Primal Kyogre.png"
        print(climage.convert("Misc/Blue Orb.png",is_unicode=True,width=30))
        print(climage.convert(self.sprite,is_unicode=True,width=50))
        print(colored("===================================================================================","blue"))
        self.name="Primal Kyogre"
        per=self.hp/self.maxhp
        self.ability="Primordial Sea"
        self.weight=947.99
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
        print(colored("===================================================================================","cyan"))
        print(f" 🗡️ {self.name}'s {self.ability}!")
        atkchange(self,other,0.5)      
        print(colored("===================================================================================","cyan"))
    if self.ability=="Dauntless Shield":
        print(colored("===================================================================================","magenta"))
        print(f" 🛡️ {self.name}'s {self.ability}!")
        defchange(self,other,0.5)
        print(colored("===================================================================================","magenta"))
    if self.megaintro is False and self.item in ["Red Orb","Crimson Orb"]:
        prevname=self.name.split(" ")[-1]
        print(colored("===================================================================================","red"))
        print(f" ♉ {prevname}'s Primal Reversion! It reverted to its primal form!")
        self.sprite="sprites/Primal Groudon.png"
        print(climage.convert("Misc/Red Orb.png",is_unicode=True,width=30))
        print(climage.convert(self.sprite,is_unicode=True,width=50))
        print(colored("===================================================================================","red"))
        self.name="Primal Groudon"
        per=self.hp/self.maxhp
        self.ability="Desolate Land"
        self.type2="Fire"
        self.weight=2203.96
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
    trname=self.owner.name.split(" ")[-1]
    if "💎" in self.name and self.owner.cantera is True:
        clr="white"
        if self.maxiv in ["Rock","Fire","Water","Grass","Electric","Ground","Flying","Fighting","Fairy","Dragon","Steel","Poison","Dark","Ghost","Normal","Bug","Ice"]:
            self.teratype=self.tera
        typ="None"
        if self.teratype =="None" and self.maxiv not in ["Rock","Fire","Water","Grass","Electric","Ground","Flying","Fighting","Fairy","Dragon","Steel","Poison","Dark","Ghost","Normal","Bug","Ice"]:
            self.teratype=self.tera
        if self.teratype=="Dragon":
            clr="red"
            typ="🐲"
        if self.teratype=="Psychic":
            clr="magenta"
            typ="👁️"
        if self.teratype=="Ghost":
            clr="magenta"
            typ="👻"
        if self.teratype=="Normal":
            typ="💎"
        if self.teratype=="Bug":
            clr="green"
            typ="🪲"
        if self.teratype=="Steel":
            typ="🪓"
        if self.teratype=="Ice":
            clr="cyan"
            typ="❄️"
        if self.teratype=="Fighting":
            clr="red"
            typ="🥊"
        if self.teratype=="Dark":
            clr="red"
            typ="👿"
        if self.teratype=="Fairy":
            clr="magenta"
            typ="❤️"
        if self.teratype=="Flying":
            clr="cyan"
            typ="🎈"
        if self.teratype=="Poison":
            clr="magenta"
            typ="☠️"
        if self.teratype=="Ground":
            clr="yellow"
            typ="🌍"
        if self.teratype=="Rock":
            clr="yellow"
            typ="🏛️"
        if self.teratype=="Grass":
            clr="green"
            typ="🌻"
        if self.teratype=="Electric":
            clr="yellow"
            typ="💡"
        if self.teratype=="Water":
            clr="blue"
            typ="⛲"
        if self.teratype=="Fire":
            clr="red"
            typ="🕯️"
        if "Terapagos" in self.name:
            print(f" 💎 {self.name} unleashed it's true power and transformed while Terastallizing!")
            self.name="Terapagos Unleashed"
            per=self.hp/self.maxhp
            self.weight=507.06
            self.hp=215
            self.atk=45
            self.defense=80
            self.spatk=160
            self.spdef=90
            self.speed=20
            self.calcst()
            self.hp=self.maxhp*per
            self.atk=self.maxatk*self.atkb 
            self.spatk=self.maxspatk*self.spatkb 
            self.defense=self.maxdef*self.defb 
            self.spdef=self.maxspdef*self.spdefb 
            self.speed=self.maxspeed*self.speedb 
        name=self.name.split("💎")[0]
        self.name=self.name[:-1]+"-"+self.teratype
        teratalk(self.owner,self)
        print(colored(f" {typ} {name} has Terastallized into the {self.teratype}-type!!",clr,attrs=["bold"]))
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
            print(colored(f" ⭕ {prevname} returned and synced with {trname}'s Dynamax Band!!","red",attrs=["bold"]))
            print(colored(f" 🔺{self.owner.name} dynamaxed {prevname}!!","red",attrs=["bold"]))
            print(climage.convert("Misc/Dynamax.png",width=50,is_unicode=True))
            if "unknown" not in self.sprite:    
                print(climage.convert(self.sprite,width=83,is_unicode=True)) 
            self.megaintro=True
        if "Gigantamax" in self.name:
            print(colored(f" ⭕ {prevname} returned and synced with {trname}'s Dynamax Band!!","red",attrs=["bold"]))
            print(colored(f" 🔺{self.owner.name} gigantamaxed {prevname}!!","red",attrs=["bold"]))
            print(climage.convert("Misc/Dynamax.png",width=50,is_unicode=True)) 
            if "unknown" not in self.gsprite:    
                print(climage.convert(self.gsprite,width=83,is_unicode=True)) 
    if "Ultra" not in self.name and "Ultranecrozium-Z" in self.item:
        prevname=self.name.split("(")[0]
        self.name="Ultra Necrozma"
        print(colored(f" ✴️ Light is bursting out of {prevname}!!","yellow",attrs=["bold"]))
        print(colored(f" 🔆 {prevname} regained its true power through Ultra Burst!!","yellow",attrs=["bold"]))
        per=self.hp/self.maxhp
        self.ability="Neuroforce"
        self.type2="Dragon"
        self.sprite="sprites/Ultra.png"
        self.weight=507.06
        self.hp=97
        self.atk=167
        self.defense=97
        self.spatk=167
        self.spdef=97
        self.speed=129
        self.calcst()
        self.hp=self.maxhp*per
        self.atk=self.maxatk*self.atkb 
        self.spatk=self.maxspatk*self.spatkb 
        self.defense=self.maxdef*self.defb 
        self.spdef=self.maxspdef*self.spdefb 
        self.speed=self.maxspeed*self.speedb   
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
            print(colored(f" 🧬 {prevname}'s {self.item} is reacting to {trname}'s Keystone!\n {prevname} has Mega Evolved into {self.name}!!","green",attrs=["bold"]))
        if "Rayquaza" in self.name:
            print(colored(f" 🧬 {trname}'s fervent wish has reached {prevname}!\n {prevname} Mega evolved into {self.name}!!","green",attrs=["bold"]))
        print(climage.convert("Misc/Mega.png",width=30,is_unicode=True)) 
        if self.item=="Gyaradosite":
            self.type2="Dark"
            self.abilityused=self.ability
            self.ability="Mold Breaker"
            self.color=17
            self.sprite="sprites/Mega Gyarados.png"
            if "✨" in self.name:
                self.sprite="sprites/SMega Gyarados.png"
            per=self.hp/self.maxhp
            self.weight=672.41
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
            self.abilityused=self.ability
            self.ability="Thick Fat"
            self.sprite="sprites/Mega Venusaur.png"
            self.weight=342.82
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
            self.abilityused=self.ability
            self.ability="Tough Claws"
            self.type2="Dragon"
            self.color=236
            self.sprite="sprites/Mega Charizard X.png"
            self.weight=243.61
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
            self.abilityused=self.ability
            self.ability="Drought"
            self.sprite="sprites/Mega Charizard Y.png"
            self.weight=221.56
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
            self.abilityused=self.ability
            self.ability="Mega Launcher"
            self.sprite="sprites/Mega Blastoise.png"
            self.weight=222.89
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
            self.abilityused=self.ability
            self.ability="Adaptability"
            self.sprite="sprites/Mega Beedrill.png"
            self.weight=89.29
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
            self.abilityused=self.ability
            self.ability="No Guard"
            self.sprite="sprites/Mega Pidgeot.png"
            self.weight=111.33
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
            self.abilityused=self.ability
            self.ability="Trace"
            self.sprite="sprites/Mega Alakazam.png"
            self.weight=105.82
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
            self.abilityused=self.ability
            self.ability="Regenerator"
            self.sprite="sprites/Mega Slowbro.png"
            self.weight=264.55
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
            self.abilityused=self.ability
            self.ability="Shadow Tag"
            self.weight=89.29
            self.sprite="sprites/Mega Gengar.png"
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
            self.abilityused=self.ability
            self.ability="Parental Bond"
            self.sprite="sprites/Mega Kangaskhan.png"
            self.weight=220.46
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
            self.abilityused=self.ability
            self.ability="Aerilate"
            self.type2="Flying"
            self.sprite="sprites/Mega Pinsir.png"
            self.weight=130.07
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
            self.abilityused=self.ability
            self.ability="Tough Claws"
            self.sprite="sprites/Mega Aerodactyl.png"
            self.weight=174.17
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
            self.abilityused=self.ability
            self.ability="Steadfast"
            self.type2="Fighting"
            self.sprite="sprites/Mega Mewtwo X.png"
            self.weight=279.99
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
            self.abilityused=self.ability
            self.ability="Insomnia"
            self.sprite="sprites/Mega Mewtwo Y.png"
            self.weight=72.75
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
            self.abilityused=self.ability
            self.ability=random.choice(["Thick Fat","Mold Breaker"])
            self.type2="Dragon"
            self.sprite="sprites/Mega Ampharos.png"
            self.weight=135.58
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
            self.abilityused=self.ability
            self.ability="Heatproof"
            self.weight=1631.42
            self.sprite="sprites/Mega Steelix.png"
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
            self.abilityused=self.ability
            self.ability="Technician"
            self.sprite="sprites/Mega Scizor.png"
            self.weight=275.58
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
            self.abilityused=self.ability
            self.ability="Skill Link"
            self.sprite="sprites/Mega Heracross.png"
            self.weight=137.79
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
            self.abilityused=self.ability
            self.ability=random.choice(["Solar Power","Dark Aura"])
            self.sprite="sprites/Mega Houndoom.png"
            self.weight=109.13
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
            self.abilityused=self.ability
            self.ability="Sand Stream"
            self.sprite="sprites/Mega Tyranitar.png"
            self.weight=562.18
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
            self.abilityused=self.ability
            self.ability="Technician"
            self.type2="Dragon"
            self.sprite="sprites/Mega Sceptile.png"
            self.weight=121.7
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
            self.abilityused=self.ability
            self.ability="Speed Boost"
            self.sprite="sprites/Mega Blaziken.png"
            self.weight=114.64
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
            self.abilityused=self.ability
            self.ability="Swift Swim"
            self.sprite="sprites/Mega Swampert.png"
            self.weight=224.87
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
            self.abilityused=self.ability
            self.ability="Pixilate"
            self.sprite="sprites/Mega Gardevoir.png"
            self.weight=106.7
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
            self.abilityused=self.ability
            self.ability="Magic Bounce"
            self.sprite="sprites/Mega Sableye.png"
            self.weight=354.94
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
            self.abilityused=self.ability
            self.ability="Huge Power"
            self.sprite="sprites/Mega Mawile.png"
            self.weight=51.81
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
            self.abilityused=self.ability
            self.ability="Filter"
            self.type2="None"
            self.sprite="sprites/Mega Aggron.png"
            self.weight=870.83
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
            self.abilityused=self.ability
            self.ability="Pure Power"
            self.sprite="sprites/Mega Medicham.png"
            self.weight=69.45
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
            self.abilityused=self.ability
            self.ability="Intimidate"
            self.sprite="sprites/Mega Manectric.png"
            self.weight=97
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
            self.abilityused=self.ability
            self.ability="Strong Jaw"
            self.sprite="sprites/Mega Sharpedo.png"
            self.weight=287.26
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
            self.abilityused=self.ability
            self.ability="Sheer Force"
            self.sprite="sprites/Mega Camerupt.png"
            self.weight=706.58
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
            self.abilityused=self.ability
            self.ability="Pixilate"
            self.type2="Fairy"
            self.sprite="sprites/Mega Altaria.png"
            self.weight=45.42
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
            self.abilityused=self.ability
            self.ability="Prankster"
            self.type2="Normal"
            self.color="magenta"
            self.sprite="sprites/Mega Banette.png"
            self.weight=28.66
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
            self.abilityused=self.ability
            self.ability=random.choice(["Magic Bounce","Sharpness"])
            self.type2="Fairy"
            self.sprite="sprites/Mega Absol.png"
            self.weight=108.03
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
            self.abilityused=self.ability
            self.ability="Refrigerate"
            self.sprite="sprites/Mega Glalie.png"
            self.weight=772.06
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
            self.abilityused=self.ability
            self.ability="Aerilate"
            self.color="red"
            self.sprite="sprites/Mega Salamence.png"
            self.weight=248.24
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
            self.abilityused=self.ability
            self.ability="Tough Claws"
            self.sprite="sprites/Mega Metagross.png"
            if "✨" in self.name:
                self.sprite="sprites/SMega Metagross.png"
            self.weight=2078.74
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
            self.abilityused=self.ability
            per=self.hp/self.maxhp
            self.weight=114.64
            self.color="blue"
            self.sprite="sprites/Mega Latias.png"
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
            self.abilityused=self.ability
            per=self.hp/self.maxhp
            self.weight=154.32
            self.color="blue"
            self.sprite="sprites/Mega Latios.png"
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
            self.abilityused=self.ability
            self.ability="Delta Stream"
            self.sprite="sprites/Mega Rayquaza.png"
            if "✨" in self.name:
                self.sprite="sprites/SMega Rayquaza.png"
            per=self.hp/self.maxhp
            self.weight=864.21
            self.hp=105
            self.atk=180
            self.defense=100
            self.spatk=180
            self.spdef=100
            self.speed=115
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False
        if self.item=="Garchompite":
            self.abilityused=self.ability
            self.ability="Sand Force"
            self.sprite="sprites/Mega Garchomp.png"
            self.weight=209.44
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
            self.abilityused=self.ability
            self.ability="Adaptability"
            self.sprite="sprites/Mega Lucario.png"
            self.weight=126.77
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
            self.abilityused=self.ability
            self.ability="Slush Rush"
            self.sprite="sprites/Mega Abomasnow.png"
            self.weight=407.86
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
            self.abilityused=self.ability
            self.ability="Scrappy"
            self.sprite="sprites/Mega Lopunny.png"
            per=self.hp/self.maxhp
            self.weight=62.9
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
            self.abilityused=self.ability
            self.ability="Sharpness"
            self.sprite="sprites/Mega Gallade.png"
            self.weight=124.34
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
            self.abilityused=self.ability
            self.ability="Regenerator"
            self.type2="Fairy"
            color="yellow"
            self.sprite="sprites/Mega Audino.png"
            self.weight=70.55
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
            self.abilityused=self.ability
            self.ability="Magic Bounce"
            self.sprite="sprites/Mega Diancie.png"
            self.weight=61.29
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
        if "unknown" not in self.sprite:    
            print(climage.convert(self.sprite,width=83,is_unicode=True))    
    elif "Mega" in self.name:
        self.name=self.name.split("Mega ")[-1]
        if "Mewtwo" in self.name:
            self.name="Mewtwo"
        if "Charizard" in self.name:
            self.name="Charizard"
        if self.item=="Gyaradosite":
            self.type2="Flying"
            self.ability=self.abilityused
            per=self.hp/self.maxhp
            self.hp=95
            self.atk=125
            self.defense=79
            self.spatk=60
            self.spdef=100
            self.speed=81
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        if self.item=="Venusaurite":
            self.ability=self.abilityused
            per=self.hp/self.maxhp
            self.hp=80
            self.atk=72
            self.defense=93
            self.spatk=110
            self.spdef=100
            self.speed=80
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        if self.item in ["Charizardite X","Charizardite Y"]:
            self.ability=self.abilityused
            self.type2="Flying"
            per=self.hp/self.maxhp
            self.hp=78
            self.atk=84
            self.defense=78
            self.spatk=110
            self.spdef=85
            self.speed=100
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        if self.item=="Blastoisinite":
            self.ability=self.abilityused
            per=self.hp/self.maxhp
            self.hp=84
            self.atk=73
            self.defense=100
            self.spatk=95
            self.spdef=105
            self.speed=78
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        if self.item=="Beedrillite":
            self.ability=self.abilityused
            per=self.hp/self.maxhp
            self.hp=65
            self.atk=115
            self.defense=40
            self.spatk=40
            self.spdef=80
            self.speed=115
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        if self.item=="Pidgeotite":
            self.ability=self.abilityused
            per=self.hp/self.maxhp
            self.hp=83
            self.atk=60
            self.defense=75
            self.spatk=115
            self.spdef=70
            self.speed=101
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        if self.item=="Alakazite":
            self.ability=self.abilityused
            per=self.hp/self.maxhp
            self.hp=55
            self.atk=50
            self.defense=45
            self.spatk=135
            self.spdef=95
            self.speed=120
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        if self.item=="Slowbronite":
            self.ability=self.abilityused
            per=self.hp/self.maxhp
            self.hp=95
            self.atk=75
            self.defense=110
            self.spatk=100
            self.spdef=80
            self.speed=30
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        if self.item=="Gengarite":
            self.ability=self.abilityused
            per=self.hp/self.maxhp
            self.hp=60
            self.atk=65
            self.defense=60
            self.spatk=130
            self.spdef=75
            self.speed=110
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        if self.item=="Kangaskhanite":
            self.ability=self.abilityused
            per=self.hp/self.maxhp
            self.hp=105
            self.atk=95
            self.defense=80
            self.spatk=40
            self.spdef=80
            self.speed=90
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        if self.item=="Pinsirite":
            self.ability=self.abilityused
            self.type2="None"
            per=self.hp/self.maxhp
            self.hp=65
            self.atk=125
            self.defense=100
            self.spatk=55
            self.spdef=70
            self.speed=85
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True    
        if self.item=="Aerodactylite":
            self.ability=self.abilityused
            per=self.hp/self.maxhp
            self.hp=80
            self.atk=105
            self.defense=65
            self.spatk=60
            self.spdef=75
            self.speed=130
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        if self.item in ["Mewtwonite X","Mewtwonite Y"]:
            self.ability=self.abilityused
            self.type2="None"
            per=self.hp/self.maxhp
            self.hp=106
            self.atk=110
            self.defense=90
            self.spatk=154
            self.spdef=90
            self.speed=130
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        if self.item=="Ampharosite":
            self.ability=self.abilityused
            self.type2="None"
            per=self.hp/self.maxhp
            self.hp=90
            self.atk=75
            self.defense=85
            self.spatk=115
            self.spdef=90
            self.speed=55
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        if self.item=="Steelixite":
            self.ability=self.abilityused
            per=self.hp/self.maxhp
            self.hp=75
            self.atk=85
            self.defense=200
            self.spatk=55
            self.spdef=65
            self.speed=30
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True   
        if self.item=="Scizorite":
            self.ability=self.abilityused
            per=self.hp/self.maxhp
            self.hp=70
            self.atk=130
            self.defense=100
            self.spatk=65
            self.spdef=80
            self.speed=65
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True 
        if self.item=="Heracronite":
            self.ability=self.abilityused
            per=self.hp/self.maxhp
            self.hp=80
            self.atk=125
            self.defense=75
            self.spatk=40
            self.spdef=95
            self.speed=85
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        if self.item=="Houndoominite":
            self.ability=self.abilityused
            per=self.hp/self.maxhp
            self.hp=75
            self.atk=110
            self.defense=90
            self.spatk=140
            self.spdef=90
            self.speed=115
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        if self.item=="Tyranitarite":
            self.ability=self.abilityused
            per=self.hp/self.maxhp
            self.sprite="sprites/Tyranitar.png"
            self.hp=100
            self.atk=164
            self.defense=150
            self.spatk=95
            self.spdef=120
            self.speed=71
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True  
        if self.item=="Sceptilite":
            self.ability=self.abilityused
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
            self.owner.canmega=True
        if self.item=="Blazikenite":
            self.ability=self.abilityused
            per=self.hp/self.maxhp
            self.hp=80
            self.atk=160
            self.defense=80
            self.spatk=130
            self.spdef=80
            self.speed=100
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        if self.item=="Swampertite":
            self.ability=self.abilityused
            per=self.hp/self.maxhp
            self.hp=100
            self.atk=150
            self.defense=110
            self.spatk=95
            self.spdef=110
            self.speed=70
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        if self.item=="Gardevoirite":
            self.ability=self.abilityused
            per=self.hp/self.maxhp
            self.hp=68
            self.atk=85
            self.defense=65
            self.spatk=165
            self.spdef=135
            self.speed=100
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        if self.item=="Sablenite":
            self.ability=self.abilityused
            per=self.hp/self.maxhp
            self.hp=50
            self.atk=85
            self.defense=125
            self.spatk=85
            self.spdef=115
            self.speed=20
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        if self.item=="Mawilite":
            self.ability=self.abilityused
            per=self.hp/self.maxhp
            self.hp=50
            self.atk=105
            self.defense=125
            self.spatk=55
            self.spdef=95
            self.speed=50
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        if self.item=="Aggronite":
            self.ability=self.abilityused
            self.type2="Rock"
            per=self.hp/self.maxhp
            self.hp=70
            self.atk=140
            self.defense=230
            self.spatk=60
            self.spdef=80
            self.speed=50
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        if self.item=="Medichamite":
            self.ability=self.abilityused
            per=self.hp/self.maxhp
            self.hp=60
            self.atk=100
            self.defense=85
            self.spatk=80
            self.spdef=85
            self.speed=100
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        if self.item=="Manectite":
            self.ability=self.abilityused
            per=self.hp/self.maxhp
            self.hp=70
            self.atk=75
            self.defense=80
            self.spatk=135
            self.spdef=80
            self.speed=135
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        if self.item=="Sharpedonite":
            self.ability=self.abilityused
            per=self.hp/self.maxhp
            self.hp=70
            self.atk=140
            self.defense=70
            self.spatk=110
            self.spdef=65
            self.speed=105
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        if self.item=="Camerupite":
            self.ability=self.abilityused
            per=self.hp/self.maxhp
            self.hp=90
            self.atk=100
            self.defense=110
            self.spatk=145
            self.spdef=115
            self.speed=20
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        if self.item=="Altarianite":
            self.ability=self.abilityused
            self.type2="Flying"
            per=self.hp/self.maxhp
            self.hp=85
            self.atk=110
            self.defense=110
            self.spatk=110
            self.spdef=105
            self.speed=80
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        if self.item=="Banettite":
            self.ability=self.abilityused
            self.type2="Dark"
            per=self.hp/self.maxhp
            self.hp=64
            self.atk=165
            self.defense=75
            self.spatk=93
            self.spdef=83
            self.speed=75
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        if self.item=="Absolite":
            self.ability=self.abilityused
            self.type2="None"
            per=self.hp/self.maxhp
            self.hp=65
            self.atk=150
            self.defense=60
            self.spatk=115
            self.spdef=60
            self.speed=115
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        if self.item=="Glalitite":
            self.ability=self.abilityused
            per=self.hp/self.maxhp
            self.hp=80
            self.atk=135
            self.defense=80
            self.spatk=105
            self.spdef=80
            self.speed=100
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        if self.item=="Salamencite":
            self.ability=self.abilityused
            per=self.hp/self.maxhp
            self.sprite="sprites/Salamence.png"
            self.hp=95
            self.atk=145
            self.defense=130
            self.spatk=120
            self.spdef=90
            self.speed=120
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        if self.item=="Metagrossite":
            self.ability=self.abilityused
            per=self.hp/self.maxhp
            self.hp=80
            self.atk=145
            self.defense=150
            self.spatk=105
            self.spdef=110
            self.speed=110
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        if self.item=="Latiasite":
            self.ability=self.abilityused
            per=self.hp/self.maxhp
            self.hp=80
            self.atk=100
            self.defense=120
            self.spatk=140
            self.spdef=150
            self.speed=110
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        if self.item=="Latiosite":
            self.ability=self.abilityused
            per=self.hp/self.maxhp
            self.hp=80
            self.atk=139
            self.defense=100
            self.spatk=160
            self.spdef=120
            self.speed=110
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        if "Dragon Ascent" in self.moves:
            self.ability=self.abilityused
            per=self.hp/self.maxhp
            self.hp=105
            self.atk=180
            self.defense=100
            self.spatk=180
            self.spdef=100
            self.speed=115
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        if self.item=="Lopunnite":
            self.ability=self.abilityused
            per=self.hp/self.maxhp
            self.hp=65
            self.atk=136
            self.defense=94
            self.spatk=54
            self.spdef=96
            self.speed=135
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        if self.item=="Garchompite":
            self.ability=self.abilityused
            per=self.hp/self.maxhp
            self.hp=108
            self.atk=170
            self.defense=105
            self.spatk=120
            self.spdef=95
            self.speed=102
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        if self.item=="Lucarionite":
            self.ability=self.abilityused
            per=self.hp/self.maxhp
            self.hp=70
            self.atk=145
            self.defense=88
            self.spatk=140
            self.spdef=70
            self.speed=112
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        if self.item=="Abomasite":
            self.ability=self.abilityused
            per=self.hp/self.maxhp
            self.hp=90
            self.atk=132
            self.defense=105
            self.spatk=132
            self.spdef=105
            self.speed=60
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        if self.item=="Lopunnite":
            self.ability=self.abilityused
            per=self.hp/self.maxhp
            self.hp=80
            self.atk=139
            self.defense=100
            self.spatk=160
            self.spdef=120
            self.speed=110
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        if self.item=="Galladite":
            self.ability=self.abilityused
            per=self.hp/self.maxhp
            self.hp=68
            self.atk=165
            self.defense=95
            self.spatk=65
            self.spdef=115
            self.speed=110
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        if self.item=="Audinite":
            self.ability=self.abilityused
            self.type2="None"
            per=self.hp/self.maxhp
            self.hp=103
            self.atk=60
            self.defense=126
            self.spatk=80
            self.spdef=126
            self.speed=50
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        if self.item=="Diancite":
            self.ability=self.abilityused
            per=self.hp/self.maxhp
            self.hp=50
            self.atk=160
            self.defense=110
            self.spatk=160
            self.spdef=110
            self.speed=110
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=True
        self.atk=self.maxatk*self.atkb 
        self.spatk=self.maxspatk*self.spatkb 
        self.defense=self.maxdef*self.defb 
        self.spdef=self.maxspdef*self.spdefb 
        self.speed=self.maxspeed*self.speedb    
    print("===================================================================================")        
    #prebuff(self,other,self.owner,turn,field)