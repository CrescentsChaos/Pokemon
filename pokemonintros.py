import random 
from movelist import *
megastones=["Gyaradosite","Venusaurite","Charizardite X","Charizardite Y","Abomasite","Absolite","Aerodactylite","Aggronite","Alakazite","Altarianite","Amoharosite","Audinite","Banettite","Beedrillite","Blastoisinite","Blazikenite","Camerupite","Diancite","Galladite","Garchompite","Gardevoirite","Gengarite","Glalitite","Heracronite","Houndoominite","Kangaskhanite","Latiasite","Latiosite","Lopunnite","Lucarionite","Manectite","Mawilite","Medichamite","Metagrossite","Mewtwonite X","Mewtwonite Y","Pidgeotite","Pinsirite","Sablenite","Salamencite","Sceptilite","Scizorite","Sharpedonite","Slowbronite","Steelixite","Seampertite","Tyranitarite"]
def mxmove(self,typem=typemoves):
    maxmove=[]
    gm=None
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
    if self.megaintro is False and "Primal Kyogre" in self.name:
        prevname=self.name.split(" ")[-1]
        print(f" ⛎ {prevname}'s Primal Reversion! It reverted to its primal form!")
        self.megaintro=True
    if self.megaintro is False and "Primal Groudon" in self.name:
        prevname=self.name.split(" ")[-1]
        print(f" ♉ {prevname}'s Primal Reversion! It reverted to its primal form!")
        self.megaintro=True
    if "💎" in self.name:
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
            typ="⚪"
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
def statchange(self,other,tr1,turn):
    hpbuff=1
    atkbuff=1
    defbuff=1
    spatkbuff=1
    spdefbuff=1
    speedbuff=1
    if tr1.auroraveil is True:
        if turn==tr1.avendturn:
            tr1.auroraveil=False
            print(" ⚠️The Aurora Veil wore off!")  
        else:
            defbuff*=2
            spdefbuff*=2
        
    if tr1.tailwind is True:
        
        if turn==tr1.twendturn:
            tr1.tailwind=False
            print(" ⚠️The Tailwind petered out!!") 
        else:
            speedbuff*=2     
    if tr1.reflect is True:
        if turn==tr1.rfendturn:
            tr1.reflect=False
            print(" ⚠️The Reflect wore off!")
        else:
            defbuff*=2
    if tr1.lightscreen is True:
        if turn==tr1.screenend:
            tr1.lightscreen=False
            print(" ⚠️The Light Screen wore off!") 
        else:
            spdefbuff*=2
        
    if self.ability=="Typeless":
        self.type1=self.atktype
    if self.status=="Frostbite":
        spatkbuff*=0.5
    if self.ability in ["Pure Power","Huge Power"]:
        atkbuff*=2
    if self.ability=="Feline Prowess":
        spatkbuff*=2
    if self.status=="Burned" and self.ability!="Guts":
        atkbuff*=0.5
    self.atk=self.maxatk*self.atkb*atkbuff
    self.defense=self.maxdef*self.defb*defbuff
    self.spatk=self.maxspatk*self.spatkb*spatkbuff
    self.spdef=self.maxspdef*self.spdefb*spdefbuff
    self.speed=self.maxspeed*self.speedb*speedbuff
    self.natureboost()
def transformation(self,other,turn):
    print(" ")
    trname=self.owner.name.split(" ")[-1]
    if self.dmax==True:
        self.maxend=turn+2
        self.maxhp=self.hp=self.hp*2
        rename(self)
        self.maxmove=mxmove(self,typemoves)
        prevname=self.name.split(" ")[-1]
        nn=-1
        prdx=["Great Tusk","Sandy Shocks","Roaring Moon","Brute Bonnet","Slither Wing","Flutter Mane","Scream Tail","Iron","Unbound"]
        for i in prdx:
            if i in self.name:
                nn=-2
        if nn==-1:
            prevname=self.name.split(" ")[-1]
        if nn==-2:
            prevname=self.name[8:]
        if "Dynamax" in self.name:
            print(f" ⭕ {prevname} returned and synced with {trname}'s Dynamax Band!")
            print(f" 🔺{self.owner.name} dynamaxed {prevname}!")
            self.megaintro=True
        if "Gigantamax" in self.name:
            print(f" ⭕ {prevname} returend and synced with {trname}'s Dynamax Band!")
            print(f" 🔺{self.owner.name} gigantamaxed {prevname}!")
    if self.item!=None and "Ultra" not in self.name and "Ultranecrozium Z" in self.item:
        prevname=self.name.split("(")[0]
        self.name="Ultra Necrozma"
        print(f" ✴️{prevname} regained its true power through Ultra Burst!")
        per=self.hp/self.maxhp
        self.hp=97
        self.atk=167
        self.defense=97
        self.spatk=167
        self.spdef=97
        self.speed=129
        self.calcst()
        self.hp=self.maxhp*per
    if ((("Mega" not in self.name and (self.item in megastones)) or "Dragon Ascent" in self.moves) and self.owner.canmega==True):
        prevname=self.name.split(" ")[-1]
        trname=self.owner.name.split(" ")[-1]
        self.name="Mega "+self.name
        if "Rayquaza" not in self.name:
            if self.item=="Charizardite X":
                self.name="Mega Charizard X"
            if self.item=="Charizardite Y":
                self.name="Mega Charizard Y"
            if self.item=="Mewtwonite X":
                self.name=" Mega Mewtwo X"
            if self.item=="Mewtwonite Y":
                self.name=" Mega Mewtwo Y"
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
            self.ability="Mold Breaker"
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
            self.ability="Solar Power"
            per=self.hp/self.maxhp
            self.hp=75
            self.atk=90
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
            self.atk=145
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
            self.type2=None
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
            self.hp=70
            self.atk=120
            self.defense=100
            self.spatk=145
            self.spdef=105
            self.speed=20
            self.calcst()
            self.hp=self.maxhp*per
            self.owner.canmega=False
        if self.item=="Altarianite":
            self.ability="Pixilate"
            self.type2="Fairy"
            per=self.hp/self.maxhp
            self.hp=75
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
            self.ability="Magic Bounce"
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
            self.atk=120
            self.defense=80
            self.spatk=120
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
        if self.item=="Grachompite":
            self.ability="Sand Force"
            per=self.hp/self.maxhp
            self.hp=108
            self.atk=170
            self.defense=115
            self.spatk=120
            self.spdef=95
            self.speed=92
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
            self.ability="Snow Warning"
            per=self.hp/self.maxhp
            self.hp=90
            self.atk=132
            self.defense=105
            self.spatk=132
            self.spdef=105
            self.speed=30
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
            self.ability="Inner Focus"
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
            self.ability="Healer"
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
    statchange(self,other,self.owner,turn)