#pylint:disable=R0914
#pylint:disable=C0304
#pylint:disable=R0913
#pylint:disable=C0301
#pylint:disable=C0303
from pokemonbase import *
#from attack import zmove

import random
class Pokemon2:
    weather=None
    trickroom=False 
    "Pokemon2"
    def __init__(self,name="Unidentified",type1="Normal",type2=None,nature=None,level=100,happiness=0,hp=0,atk=0,defense=0,spatk=0,spdef=0,speed=0,hpiv=0,atkiv=0,defiv=0,spatkiv=0,spdefiv=0,speediv=0,maxiv="No",atktype="Normal",hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0,status="Alive",atkb=1,defb=1,spatkb=1,spdefb=1,speedb=1,ability=None,moves=None,movez=None,badpoison=1,flinched=False,recharge=False,seeded=False, intimidated=False,item=None,precharge=False, protect=False):
        #Name
        self.name=name
        if moves is None:
            self.moves=[]
        else:
            self.moves=moves
        self.shiny=random.randint(1,4096)
        if self.shiny==7:
            self.name=self.name+"⭐"
        #Type
        self.type1=type1
        self.type2=type2
        self.item=item
        self.badpoison=badpoison
        self.recharge=recharge
        self.seeded=seeded
        self.flinched=flinched
        self.precharge=precharge 
        self.protect=protect
        self.intimidated=intimidated
        #Nature
        self.nature=nature
        #Level
        self.level=level
        #Happiness
        self.happiness=happiness
        #Base Stats
        self.hp=hp
        self.atk=atk
        self.defense=defense
        self.spatk=spatk
        self.spdef=spdef
        self.speed=speed
        #IVs
        self.hpiv=hpiv
        self.atkiv=atkiv
        self.defiv=defiv
        self.spatkiv=spatkiv
        self.spdefiv=spdefiv
        self.speediv=speediv
        
        #IVs
        self.hpev=hpev
        self.atkev=atkev
        self.defev=defev
        self.spatkev=spatkev
        self.spdefev=spdefev
        self.speedev=speedev
        self.alpha=random.randint(1,20)
        if "Mega " not in self.name and self.alpha==7 and maxiv!="Yes":
            self.name="Alpha "+name
        self.totem=random.randint(1,100)
        if "Mega " not in self.name and "Alpha " not in name and self.totem == 7 and maxiv!="Yes":
            self.name="Totem "+name
        self.teratype=random.randint(1,50)
        if self.teratype==2 and "Mega" not in self.name and "Alpha " not in self.name:
           self.type=random.choice(["Rock","Fire","Water","Grass","Electric","Ground","Flying","Fighting","Fairy","Dragon","Steel","Poison","Dark","Ghost","Normal","Bug","Ice"])
           if self.type1==self.type or self.type2==self.type:
                self.atkb=1.5
                self.spatkb=1.5
           self.type1=self.type
           self.type2=None
           self.moves+=["Tera Blast"]
           self.name+=f"({self.type1})"
        self.movez=movez
        if maxiv!="Yes" or "Z-Crystal" in self.name:
            self.movez=random.randint(1,2)
            if "Z-Crystal" in self.name:
                self.movez=2
        if self.movez==2 and "Mega " not in self.name and "Alpha " not in self.name:
            self.moves+=zmove(self)
            if "(Z-Crystal)" not in self.name:
                self.name+="(Z-Crystal)"
        #Command
        self.maxiv=maxiv
        #Attack Manipulation
        self.atktype=atktype
        #Boost
        self.atkb=atkb
        self.defb=defb
        self.spatkb=spatkb
        self.spdefb=spdefb
        self.speedb=speedb
        
        #stats
        self.ability=ability
        self.status=status
        self.calcst()
    def genlowiv(self):
        "Sets to Max IV"
        self.hpiv=self.atkiv=self.defiv=self.spatkiv=self.spdefiv=self.speediv=0
    def genmaxiv(self):
        "Sets to Max IV"
        self.hpiv=self.atkiv=self.defiv=self.spatkiv=self.spdefiv=self.speediv=31
#GENERATES RANDOM IV
    def geniv(self):
        "Generates Random IV"
        self.hpiv=random.randint(0,31)
        self.atkiv=random.randint(0,31)
        self.defiv=random.randint(0,31)
        self.spatkiv=random.randint(0,31)
        self.spdefiv=random.randint(0,31)
        self.speediv=random.randint(0,31)
        if "Mega " not in self.name and self.alpha==7:
            self.hpiv=random.randint(15,31)
            self.atkiv=random.randint(15,31)
            self.defiv=random.randint(15,31)
            self.spatkiv=random.randint(15,31)
            self.spdefiv=random.randint(15,31)
            self.speediv=random.randint(15,31)
        if "Mega " not in self.name and self.totem==7:
            num=random.randint(1,50)
            if num==1:
                self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=(31,31,31,31,31,31)
            if 1>num<5:
                iv=[31,31,31,31,31,random.randint(15,31)]
                random.shuffle(iv)
                self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=tuple(iv)
            if 4<num<20:
                iv=[31,31,31,31,random.randint(15,31),random.randint(15,31)]
                random.shuffle(iv)
                self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=tuple(iv)
            else:
                iv=[31,31,31,random.randint(15,31),random.randint(15,31),random.randint(15,31)]
                random.shuffle(iv)
                self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=tuple(iv)
                
    def calcst(self):
        "Calculates Stats"
        #Generates Nature
        if self.nature is None:
            self.gennature()
        else:
            pass
        #Generates Random IV
        if self.maxiv=="No":
            self.geniv()
        elif self.maxiv=="Low":
            self.genlowiv()
        else:
            self.genmaxiv()
        self.hp = stat_clac(self.hp,self.hpiv,self.hpev,self.level,"HP")
        self.atk = stat_clac(self.atk,self.atkiv,self.atkev,self.level)
        self.defense=stat_clac(self.defense,self.defiv,self.defev,self.level)
        self.spatk = stat_clac(self.spatk,self.spatkiv,self.spatkev,self.level)
        self.spdef = stat_clac(self.spdef,self.spdefiv,self.spdefev,self.level)
        self.speed =stat_clac(self.speed,self.speediv,self.speedev,self.level)
        
        self.natureboost()
        self.maxhp=self.hp
        self.maxatk=self.atk
        self.maxspeed=self.speed
        self.maxspatk=self.spatk
        self.maxspdef=self.spdef
        self.maxdef=self.defense
        self.maxtotal=self.maxhp+self.maxatk+self.maxdef+self.maxspatk+self.maxspdef+self.maxspeed
        
#NATURE BOOST
    def natureboost(self):
        "Boosts stats according to nature"
        if self.nature in ["Bashful","Docile","Hardy","Quirky","Serious"]:
            pass
        if self.nature in ["Adamant","Brave","Lonely","Naughty"]:
            self.atk+=round(self.atk*0.1)
        if self.nature in ["Mild","Modest","Quite","Rash"]:
            self.spatk+=round(self.spatk*0.1)
        if self.nature in ["Adamant","Careful","Impish","Jolly"]:
            self.spatk-=round(self.spatk*0.1)
        if self.nature in ["Bold","Calm","Modest","Timid"]:
            self.atk-=round(self.atk*0.1)
        if self.nature in ["Bold","Relaxed","Lax","Impish"]:
            self.defense+=round(self.defense*0.1)
        if self.nature in ["Gentle","Hasty","Lonely","Mild"]:
            self.defense-=round(self.defense*0.1)
        if self.nature in ["Calm","Careful","Gentle","Sassy"]:
            self.spdef+=round(self.spdef*0.1)
        if self.nature in ["Lax","Naive","Naughty","Rash"]:
            self.spdef-=round(self.spdef*0.1)
        if self.nature in ["Jolly","Timid","Naive","Hasty"]:
            self.speed+=round(self.speed*0.1)
        if self.nature in ["Brave","Quite","Sassy","Relaxed"]:
            self.speed-=round(self.speed*0.1)
#GENERATES NATURE
    def gennature(self):
        "Generates Nature"
        naturelist=["Hardy","Lonely","Adamant","Naughty","Brave", "Bold",'Docile','Impish','Lax']+\
        ['Relaxed' ,'Modest','Mild','Bashful']+\
        ['Rash','Quiet' ,'Calm','Gentle','Careful','Quirky']+\
        ['Sassy', 'Timid','Hasty','Jolly','Naive','Serious']
        self.nature=random.choice(naturelist)
        
    def ivc(self):
        "Checks IV"
        print(f"HP IV: {self.hpiv}/31")
        print(f"Attack IV: {self.atkiv}/31")
        print(f"Defence IV: {self.defiv}/31")
        print(f"Special Attack IV: {self.spatkiv}/31")
        print(f"Special Defence IV: {self.spdefiv}/31")
        print(f"Speed IV: {self.speediv}/31")
        totaliv=self.hpiv+self.atkiv+self.defiv+self.spatkiv+self.spdefiv+self.speediv
        print("=============================================")
        percentage=(totaliv/186)*100
        print(f"Total IV: {totaliv}/186")
        print(f"IV: {round(percentage,2)}%")
    
        print("=============================================")
    def info(self):
        "Shows Stats"
        print("=============================================")
        print(f"Name: {self.name}")
        if self.type2 is None:
            print(f"Type: {self.type1}")
        else:
            print(f"Type: {self.type1} {self.type2}")
        print(f"Nature: {self.nature}")
        print(f"Ability: {self.ability}")
        print(f"Level: {self.level}")
        print("=============================================")
        print("Stats:")
        print("=============================================")
        print(f"HP: {self.hp}")
        print(f"Attack: {self.atk}")
        print(f"Defence: {self.defense}")
        print(f"Special Attack: {self.spatk}")
        print(f"Special Defence: {self.spdef}")
        print(f"Speed: {self.speed}")
        print("=============================================")
        self.ivc()
#Kabutops
class Kabutops(Pokemon2):
    "Kabutops"
    def __init__(self,name="Kabutops",type1="Rock",type2="Water",nature=None,level=100,happiness=255,hp=60,atk=115,defense=105,spatk=65,spdef=70,speed=80,hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Swift Swim",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Liquidation","Hydro Pump","Rock Slide","Stone Edge","Flip Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                  
#Aerodactyl
class Aerodactyl (Pokemon2):
    "Aerodactyl"
    def __init__(self,name="Aerodactyl",type1="Rock",type2="Flying",nature=None,level=100,happiness=255,hp=80,atk=105,defense=65,spatk=60,spdef=75,speed=130,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Rock Head",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Ancient Power","Stone Edge","Rock Slide","Brave Bird"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)              
#Mega  Aerodactyl
class MAerodactyl (Pokemon2):
    "Mega Aerodactyl"
    def __init__(self,name="Mega Aerodactyl",type1="Rock",type2="Flying",nature=None,level=100,happiness=255,hp=80,atk=135,defense=85,spatk=70,spdef=95,speed=150,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Tough Claws",item="Aerodactylite"):
        if move is None:
            avmoves=["Protect","Ancient Power","Stone Edge","Rock Slide","Brave Bird"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)    
#Snorlax
class Snorlax(Pokemon2):
    "Snorlax"
    def __init__(self,name="Snorlax",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=160,atk=110,defense=65,spatk=65,spdef=110,speed=30,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability="Thick Fat",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hidden Power","Ice Beam","Body Slam","Thunder Punch","Double Edge","Hyper Beam","Giga Impact","Rest"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Articuno
class Articuno    (Pokemon2):
    "Articuno"
    def __init__(self,name="Articuno",type1="Ice",type2="Flying",nature=None,level=100,happiness=255,hp=90,atk=85,defense=100,spatk=95,spdef=125,speed=85,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Snow Warning",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hidden Power","Ice Beam","Blizzard","Freeze Dry","Brave Bird","Sky Attack","Roost"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      
#Zapdos
class Zapdos(Pokemon2):
    "Zapdos"
    def __init__(self,name="Zapdos",type1="Electric",type2="Flying",nature=None,level=100,happiness=255,hp=90,atk=90,defense=85,spatk=125,spdef=90,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Drizzle",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hidden Power","Thunder","Brave Bird","Thunderbolt","Sky Attack","Roost","Thunder Wave"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)             
#Moltres
class Moltres(Pokemon2):
    "Moltres"
    def __init__(self,name="Moltres",type1="Fire",type2="Flying",nature=None,level=100,happiness=255,hp=90,atk=100,defense=90,spatk=125,spdef=85,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Drought",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hidden Power","Flamethrower","Hurricane","Heat Wave","Sky Attack","Brave Bird","Fire Blast","Roost","Solar Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Dragonite
class Dragonite(Pokemon2):
    "Dragonite"
    def __init__(self,name="Dragonite",type1="Dragon",type2="Flying",nature=None,level=100,happiness=255,hp=91,atk=134,defense=95,spatk=100,spdef=100,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Multiscale",item=random.choice(["Weakness Policy","Leftovers"])):
        if move is None:
            avmoves=["Protect","Hidden Power","Ice Beam","Hydro Pump","Thunderbolt","Surf","Dragon Claw","Double Edge","Thunder Wave"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Mewtwo
class Mewtwo(Pokemon2):
    "Mewtwo"
    def __init__(self,name="Mewtwo",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=106,atk=110,defense=90,spatk=154,spdef=90,speed=130,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Regenerator",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hidden Power","Psystrike","Shadow Ball","Dark Pulse","Ice Beam","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Mew
class Mew(Pokemon2):
    "Mew"
    def __init__(self,name="Mew",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=100,atk=100,defense=100,spatk=100,spdef=100,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Regenerator",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Shadow Ball","Hidden Power","Transform","Psychic","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Mega Venusaur 
class MVenusaur(Pokemon2):
    "Mega Venusaur"
    def __init__(self,name="Mega Venusaur",type1="Grass",type2="Poison",nature=None,level=100,happiness=255,hp=80,atk=100,defense=123,spatk=122,spdef=120,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Thick Fat",item="Venusaurite"):
        if move is None:
            avmoves=["Protect","Hidden Power","Giga Drain","Sludge Bomb","Earth Power","Sleep Powder"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Mega Blastoise
class MBlastoise(Pokemon2):
    "Mega Blastoise"
    def __init__(self,name="Mega Blastoise",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=79,atk=103,defense=120,spatk=135,spdef=115,speed=78,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Mega Launcher",item="Blastoisinite"):
        if move is None:
            avmoves=["Protect","Hidden Power","Ice Beam","Hydro Pump","Dark Pulse","Dragon Pulse","Aura Sphere","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Mega Charizard X
class MCharizardX(Pokemon2):
    "Mega Charizard X"
    def __init__(self,name="Mega Charizard X",type1="Fire",type2="Dragon",nature=None,level=100,happiness=255,hp=78,atk=130,defense=111,spatk=130,spdef=85,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Tough Claws",item="Charizardite X"):
        if move is None:
            avmoves=["Protect","Dragon Fance","Dragon Claw","Flare Blitz","Roost","Earthquake"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      
#Mega Charizard Y
class MCharizardY(Pokemon2):
    "Mega Charizard Y"
    def __init__(self,name="Mega Charizard Y",type1="Fire",type2="Flying",nature=None,level=100,happiness=255,hp=78,atk=104,defense=78,spatk=169,spdef=115,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Drought",item="Charizardite Y"):
        if move is None:
            avmoves=["Protect","Hidden Power","Fire Blast","Solar Beam","Flamethrower","Earth Power","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Meganium
class Meganium(Pokemon2):
    "Meganium"
    def __init__(self,name="Meganium",type1="Grass",type2="Fairy",nature=None,level=100,happiness=255,hp=80,atk=72,defense=100,spatk=93,spdef=100,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Thick Fat",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hidden Power","Leaf Storm","Moon Blast","Dazzling Gleam","Synthesis","Leech Seed","Solar Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Typhlosion
class Typhlosion(Pokemon2):
    "Typhlosion"
    def __init__(self,name="Typhlosion",type1="Fire",type2="Dark",nature=None,level=100,happiness=255,hp=78,atk=84,defense=78,spatk=109,spdef=85,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Flash Fire",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hidden Power","Earth Power","Fire Blast","Lava Plume","Eruption","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Feraligatr
class Feraligatr(Pokemon2):
    "Feraligatr"
    def __init__(self,name="Feraligatr",type1="Water",type2="Dragon",nature=None,level=100,happiness=255,hp=85,atk=105,defense=100,spatk=79,spdef=83,speed=78,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Sheer Force",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Ice Beam","Hydro Pump","Liquidation","Dragon Claw","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Vaporeon
class Vaporeon(Pokemon2):
    "Vaporeon"
    def __init__(self,name="Vaporeon",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=130,atk=65,defense=60,spatk=110,spdef=95,speed=65,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=252,speedev=0,maxiv="No",move=None, ability="Water Absorb",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hidden Power","Ice Beam","Hydro Pump","Acid Armor","Surf","Rain Dance","Flip Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                   
#Jolteon
class Jolteon(Pokemon2):
    "Jolteon"
    def __init__(self,name="Jolteon",type1="Electric",type2=None,nature=None,level=100,happiness=255,hp=65,atk=65,defense=60,spatk=110,spdef=95,speed=130,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Volt Absorb",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hidden Power","Volt Switch","Thunder","Thunderbolt","Shadow Ball","Thunder Wave"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
               
#Flareon
class Flareon(Pokemon2):
    "Flareon"
    def __init__(self,name="Flareon",type1="Fire",type2=None,nature=None,level=100,happiness=255,hp=65,atk=130,defense=60,spatk=95,spdef=110,speed=65,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Flash Fire",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Flare Blitz","Fire Blast","Flame Charge","Last Resort","Will-O-Wisp"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)  
#Crobat
class Crobat(Pokemon2):
    "Crobat"
    def __init__(self,name="Crobat",type1="Poison",type2="Flying",nature=None,level=100,happiness=255,hp=85,atk=90,defense=80,spatk=70,spdef=80,speed=130,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Infiltrator",item="Black Sludge"):
        if move is None:
            avmoves=["Protect","Poison Jab","Cross Poison","Dual Wingbeat","Brave Bird","U-Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)              
#Lanturn
class Lanturn(Pokemon2):
    "Lanturn"
    def __init__(self,name="Lanturn",type1="Water",type2="Electric",nature=None,level=100,happiness=255,hp=125,atk=58,defense=58,spatk=76,spdef=76,speed=67,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Volt Absorb",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hidden Power","Ice Beam","Hydro Pump","Thunderbolt","Surf","Rain Dance","Flip Turn","Volt Switch","Thunder Wave"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Ampharos
class Ampharos(Pokemon2):
    "Amoharos"
    def __init__(self,name="Ampharos",type1="Electric",type2=None,nature=None,level=100,happiness=255,hp=90,atk=75,defense=85,spatk=115,spdef=90,speed=55,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=252,speedev=0,maxiv="No",move=None, ability="Static",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hidden Power","Signal Beam","Power Gem","Thunderbolt","Discharge","Thunder Wave","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)               
#Mega Ampharos
class MAmpharos(Pokemon2):
    "Mega Amoharos"
    def __init__(self,name="Mega Ampharos",type1="Electric",type2="Dragon",nature=None,level=100,happiness=255,hp=90,atk=95,defense=105,spatk=165,spdef=110,speed=45,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=252,speedev=0,maxiv="No",move=None, ability="Mold Breaker",item="Ampharosite"):
        if move is None:
            avmoves=["Protect","Hidden Power","Signal Beam","Power Gem","Thunderbolt","Draco Meteor","Dragon Pulse","Thunder Wave","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Azumarill
class Azumarill(Pokemon2):
    "Azumarill"
    def __init__(self,name="Azumarill",type1="Water",type2="Fairy",nature=None,level=100,happiness=255,hp=100,atk=50,defense=80,spatk=60,spdef=80,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Huge Power",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hidden Power","Ice Beam","Aqua Jet","Play Rough","Liquidation","Belly Drum"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)       
#Politoed
class Politoed(Pokemon2):
    "Politoed"
    def __init__(self,name="Politoed",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=90,atk=75,defense=75,spatk=90,spdef=100,speed=70,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability=random.choice(["Drizzle","Damp"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hidden Power","Ice Beam","Hydro Pump","Thunderbolt","Surf","Flip Turn","Focus Blast","Belly Drum"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)     
#Espeon
class Espeon(Pokemon2):
    "Espeon"
    def __init__(self,name="Espeon",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=65,atk=65,defense=60,spatk=130,spdef=95,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Magic Bounce","Synchronize"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hidden Power","Psychic","Shadow Ball","Dazzling Gleam","Morning Sun"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Umbreon
class Umbreon(Pokemon2):
    "Umbreon"
    def __init__(self,name="Umbreon",type1="Dark",type2=None,nature=None,level=100,happiness=255,hp=95,atk=65,defense=110,spatk=60,spdef=130,speed=65,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability="Inner Focus",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hidden Power","Foul Play","Shadow Ball","Dark Pulse","Moonlight","Toxic"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Steelix
class Steelix(Pokemon2):
    "Steelix"
    def __init__(self,name="Steelix",type1="Steel",type2="Ground",nature=None,level=100,happiness=255,hp=75,atk=125,defense=230,spatk=55,spdef=95,speed=30,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Rock Head",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Iron Tail","Gyro Ball","Earthquake","Stone Edge","Rock Slide","Toxic","Body Press"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Mega Steelix
class MSteelix(Pokemon2):
    "Mega Steelix"
    def __init__(self,name="Mega Steelix",type1="Steel",type2="Ground",nature=None,level=100,happiness=255,hp=75,atk=85,defense=200,spatk=55,spdef=65,speed=30,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Inner Focus",item="Steelixite"):
        if move is None:
            avmoves=["Protect","Iron Tail","Gyro Ball","Earthquake","Stone Edge","Rock Slide","Toxic","Body Press"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)       
#Scizor
class Scizor(Pokemon2):
    "Scizor"
    def __init__(self,name="Scizor",type1="Bug",type2="Steel",nature=None,level=100,happiness=255,hp=70,atk=130,defense=100,spatk=55,spdef=80,speed=65,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Technician",item="Life Orb"):
        if move is None:
            avmoves=["Protect","Iron Head","Bullet Punch","X-Scissor","U-Turn","Roost","Superpower"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Mega Scizor
class MScizor(Pokemon2):
    "Mega Scizor"
    def __init__(self,name="Mega Scizor",type1="Bug",type2="Steel",nature=None,level=100,happiness=255,hp=70,atk=150,defense=140,spatk=65,spdef=100,speed=75,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Technician",item="Scizorite"):
        if move is None:
            avmoves=["Protect","Iron Head","Bullet Punch","X-Scissor","U-Turn","Roost","Superpower"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                   
#Heracross
class Heracross(Pokemon2):
    "Heracross"
    def __init__(self,name="Heracross",type1="Bug",type2="Fighting",nature=None,level=100,happiness=255,hp=80,atk=125,defense=75,spatk=40,spdef=95,speed=85,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Guts",item="Flame Orb"):
        if move is None:
            avmoves=["Protect","Megahorn","Brick Break","X-Scissor","U-Turn","Close Combat","Superpower"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Mega Heracross
class MHeracross(Pokemon2):
    "Mega Heracross"
    def __init__(self,name="Mega Heracross",type1="Bug",type2="Fighting",nature=None,level=100,happiness=255,hp=80,atk=185,defense=115,spatk=40,spdef=105,speed=75,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Skill Link",item="Heracronite"):
        if move is None:
            avmoves=["Protect","Megahorn","Brick Break","X-Scissor","U-Turn","Close Combat","Superpower","Pin Missile"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#Skarmory
class Skarmory(Pokemon2):
    "Skarmory"
    def __init__(self,name="Skarmory",type1="Steel",type2="Flying",nature=None,level=100,happiness=255,hp=65,atk=80,defense=140,spatk=40,spdef=70,speed=70,hpev=252,atkev=0,defev=252,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Sturdy",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Roost","Brave Bird","Stealth Rock","Whirlwind","Steel Wing","Body Press"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Houndoom
class Houndoom(Pokemon2):
    "Houndoom"
    def __init__(self,name="Houndoom",type1="Dark",type2="Fire",nature=None,level=100,happiness=255,hp=75,atk=90,defense=50,spatk=110,spdef=80,speed=95,hpev=0,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=252,maxiv="No",move=None, ability="Flash Fire",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Fire Blast","Dark Pulse","Flamethrower","Inferno","Crunch","Will-O-Wisp"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Mega Houndoom
class MHoundoom(Pokemon2):
    "Mega Houndoom"
    def __init__(self,name="Mega Houndoom",type1="Dark",type2="Fire",nature=None,level=100,happiness=255,hp=75,atk=90,defense=90,spatk=140,spdef=90,speed=115,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Solar Power",item="Houndoominite"):
        if move is None:
            avmoves=["Protect","Fire Blast","Dark Pulse","Flamethrower","Inferno","Crunch"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)             
#Kingdra
class Kingdra(Pokemon2):
    "Kingdra"
    def __init__(self,name="Kingdra",type1="Water",type2="Dragon",nature=None,level=100,happiness=255,hp=75,atk=95,defense=95,spatk=95,spdef=95,speed=85,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Swift Swim",item="Life Orb"):
        if move is None:
            avmoves=["Protect","Dragon Pulse","Ice Beam","Surf","Thunder","Hydro Pump","Dragon Dance","Rain Dance","Flip Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                     
#Tyranitar
class Tyranitar(Pokemon2):
    "Tyranitar"
    def __init__(self,name="Tyranitar",type1="Rock",type2="Dark",nature=None,level=100,happiness=255,hp=100,atk=134,defense=110,spatk=95,spdef=100,speed=61,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Sand Stream",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Crunch","Earthquake","Stone Edge","Rock Slide","Hyper Beam","Dragon Dance","Giga Impact"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item) 
#Mega Tyranitar
class MTyranitar(Pokemon2):
    "Mega Tyranitar"
    def __init__(self,name="Mega Tyranitar",type1="Rock",type2="Dark",nature=None,level=100,happiness=255,hp=100,atk=164,defense=150,spatk=95,spdef=120,speed=71,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Sand Stream",item="Tyranitarite"):
        if move is None:
            avmoves=["Protect","Crunch","Earthquake","Stone Edge","Rock Slide","Hyper Beam","Dragon Dance"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)             
#Raikou
class Raikou(Pokemon2):
    "Raikou"
    def __init__(self,name="Raikou",type1="Electric",type2=None,nature=None,level=100,happiness=255,hp=90,atk=85,defense=75,spatk=115,spdef=100,speed=115,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Inner Focus",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Crunch","Thunder","Thunderbolt","Wild Charge","Hyper Beam","Rain Dance","Thunder Wave"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Entei
class Entei(Pokemon2):
    "Entei"
    def __init__(self,name="Entei",type1="Fire",type2=None,nature=None,level=100,happiness=255,hp=115,atk=115,defense=85,spatk=90,spdef=75,speed=100,hpev=0,atkev=115,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Inner Focus",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Crunch","Fire Blast","Stone Edge","Flamethrower","Hyper Beam","Flare Blitz","Eruption"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Suicune
class Suicune(Pokemon2):
    "Suicune"
    def __init__(self,name="Suicune",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=100,atk=75,defense=115,spatk=90,spdef=115,speed=85,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Inner Focus",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Crunch","Surf","Hydro Pump","Recover","Hyper Beam","Rain Dance"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Lugia
class Lugia(Pokemon2):
    "Lugia"
    def __init__(self,name="Lugia",type1="Psychic",type2="Flying",nature=None,level=100,happiness=255,hp=106,atk=90,defense=130,spatk=90,spdef=154,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Multiscale",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Crunch","Surf","Hydro Pump","Recover","Hyper Beam","Rain Dance","Aeroblast","Psychic","Extrasensory"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Ho-Oh
class Hooh(Pokemon2):
    "Ho-Oh"
    def __init__(self,name="Ho-Oh",type1="Fire",type2="Flying",nature=None,level=100,happiness=255,hp=106,atk=130,defense=90,spatk=110,spdef=154,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Regenerator",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Recover","Hyper Beam","Sunny Day","Sacred Fire","Fire Blast","Flamethrower","Brave Bird","Heat Wave","Sky Attack"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                     
#Celebi
class Celebi(Pokemon2):
    "Celebi"
    def __init__(self,name="Celebi",type1="Grass",type2="Psychic",nature=None,level=100,happiness=255,hp=100,atk=100,defense=100,spatk=100,spdef=100,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Natural Cure",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Recover","Psychic","Leaf Storm","Future Sight","Perish Song","Shadow Ball"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#Blissey
class Blissey(Pokemon2):
    "Blissey"
    def __init__(self,name="Blissey",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=255,atk=10,defense=10,spatk=75,spdef=135,speed=55,hpev=252,atkev=0,defev=252,spatkev=0,spdefev=4,speedev=0,maxiv="No",move=None, ability="Natural Cure",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Soft Boiled","Toxic","Seismic Toss","Light Screen","Reflect"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)  
#Deoxys
class Deoxys(Pokemon2):
    "Deoxys"
    def __init__(self,name="Deoxys",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=50,atk=150,defense=50,spatk=150,spdef=50,speed=150,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Pressure",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Psycho Boost","Toxic","Psychic","Shadow Ball","Dark Pulse"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)    
#Attack Deoxys
class ADeoxys(Pokemon2):
    "Attack Deoxys"
    def __init__(self,name="Attack Deoxys",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=50,atk=180,defense=20,spatk=180,spdef=20,speed=150,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Pressure",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Psycho Boost","Psychic","Shadow Ball","Dark Pulse"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)    
#Speed Deoxys
class SDeoxys(Pokemon2):
    "Speed Deoxys"
    def __init__(self,name="Speed Deoxys",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=50,atk=95,defense=90,spatk=95,spdef=90,speed=180,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Pressure",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Psycho Boost","Toxic","Psychic","Shadow Ball","Dark Pulse","Recover","Thunder Wave"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)   
#Defense Deoxys
class DDeoxys(Pokemon2):
    "Defense Deoxys"
    def __init__(self,name="Defense Deoxys",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=50,atk=70,defense=160,spatk=70,spdef=160,speed=90,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=4,maxiv="No",move=None, ability="Pressure",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Psycho Boost","Toxic","Psychic","Shadow Ball","Dark Pulse","Recover","Thunder Wave"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Jirachi       
class Jirachi(Pokemon2):
    "Jirachi"
    def __init__(self,name="Jirachi",type1="Steel",type2="Psychic",nature=None,level=100,happiness=255,hp=100,atk=100,defense=100,spatk=100,spdef=100,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Serene Grace",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Recover","Psychic","Doom Desire","Future Sight","Flash Cannon","Shadow Ball","Rest"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item) 
#Rayquaza     
class Rayquaza(Pokemon2):
    "Rayquaza"
    def __init__(self,name="Rayquaza",type1="Dragon",type2="Flying",nature=None,level=100,happiness=255,hp=105,atk=150,defense=90,spatk=150,spdef=90,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Air Lock",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Crunch","Hyper Beam","Dragon Ascent","Dragon Dance","Extreme Speed","Draco Meteor"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)   
#Mega Rayquaza     
class MRayquaza(Pokemon2):
    "Mega Rayquaza"
    def __init__(self,name="Mega Rayquaza",type1="Dragon",type2="Flying",nature=None,level=100,happiness=255,hp=105,atk=180,defense=100,spatk=180,spdef=100,speed=115,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Delta Stream",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Crunch","Hyper Beam","Dragon Ascent","Dragon Dance","Extreme Speed","Draco Meteor"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#Sceptile
class Sceptile(Pokemon2):
    "Sceptile"
    def __init__(self,name="Sceptile",type1="Grass",type2=None,nature=None,level=100,happiness=255,hp=70,atk=85,defense=65,spatk=105,spdef=86,speed=120,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Overgrow",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Leaf Blade","Hyper Beam","Leaf Storm","Dragon Dance","Dragon Pulse","Draco Meteor","Focus Blast","Energy Ball"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)     
#Mega Sceptile
class MSceptile(Pokemon2):
    "Mega Sceptile"
    def __init__(self,name="Mega Sceptile",type1="Grass",type2="Dragon",nature=None,level=100,happiness=255,hp=70,atk=110,defense=75,spatk=155,spdef=85,speed=145,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Lightning Rod",item="Sceptilite"):
        if move is None:
            avmoves=["Protect","Hyper Beam","Leaf Storm","Dragon Dance","Dragon Pulse","Draco Meteor","Focus Blast","Energy Ball"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#Blaziken
class Blaziken(Pokemon2):
    "Blaziken"
    def __init__(self,name="Blaziken",type1="Fire",type2="Fighting",nature=None,level=100,happiness=255,hp=80,atk=120,defense=70,spatk=110,spdef=70,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Speed Boost",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Overheat","High Jump Kick","Sky Uppercut","Blaze Kick","Brave Bird","Flare Blitz","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Mega Blaziken
class MBlaziken(Pokemon2):
    "Mega Blaziken"
    def __init__(self,name="Mega Blaziken",type1="Fire",type2="Fighting",nature=None,level=100,happiness=255,hp=80,atk=160,defense=80,spatk=130,spdef=80,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Speed Boost",item="Blazikenite"):
        if move is None:
            avmoves=["Protect","Overheat","High Jump Kick","Sky Uppercut","Blaze Kick","Brave Bird","Flare Blitz","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                     
#Swampert
class Swampert(Pokemon2):
    "Swampert"
    def __init__(self,name="Swampert",type1="Water",type2="Ground",nature=None,level=100,happiness=255,hp=100,atk=110,defense=90,spatk=85,spdef=90,speed=60,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Torrent",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Liquidation","Earthquake","Stone Edge","Power-up Punch","Waterfall","Ice Punch","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Mega Swampert
class MSwampert(Pokemon2):
    "Mega Swampert"
    def __init__(self,name="Mega Swampert",type1="Water",type2="Ground",nature=None,level=100,happiness=255,hp=100,atk=150,defense=110,spatk=95,spdef=110,speed=70,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Swift Swim",item="Swampertite"):
        if move is None:
            avmoves=["Protect","Liquidation","Earthquake","Stone Edge","Power-up Punch","Waterfall","Ice Punch","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                               
#Ludicolo
class Ludicolo(Pokemon2):
    "Ludicolo"
    def __init__(self,name="Ludicolo",type1="Grass",type2="Water",nature=None,level=100,happiness=255,hp=80,atk=70,defense=70,spatk=90,spdef=100,speed=70,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Swift Swim",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Ice Beam","Giga Drain","Surf","Hydro Pump","Rain Dance","Focus Blast","Energy Ball"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Shiftry
class Shiftry(Pokemon2):
    "Shiftry"
    def __init__(self,name="Shiftry",type1="Grass",type2="Dark",nature=None,level=100,happiness=255,hp=90,atk=100,defense=60,spatk=90,spdef=60,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Chlorophyll",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Sunny Day","Giga Drain","Leaf Storm","Hurricane","Leaf Tornado","Leech Seed","Focus Blast","Explosion"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Swellow
class Swellow(Pokemon2):
    "Swellow"
    def __init__(self,name="Swellow",type1="Normal",type2="Flying",nature=None,level=100,happiness=255,hp=60,atk=85,defense=60,spatk=75,spdef=50,speed=125,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Guts",item="Flame Orb"):
        if move is None:
            avmoves=["Protect","Roost","Brave Bird","Facade","Hurricane","Boomburst"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)   
#Pelipper
class Pelipper(Pokemon2):
    "Pelipper"
    def __init__(self,name="Pelipper",type1="Water",type2="Flying",nature=None,level=100,happiness=255,hp=60,atk=50,defense=100,spatk=95,spdef=70,speed=65,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Drizzle",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Roost","Surf","Ice Beam","Hurricane","Hydro Pump"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#Gardevoir
class Gardevoir(Pokemon2):
    "Gardevoir"
    def __init__(self,name="Gardevoir",type1="Psychic",type2="Fairy",nature=None,level=100,happiness=255,hp=68,atk=65,defense=65,spatk=125,spdef=115,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Trace",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Recover","Dazzling Gleam","Moon Blast","Psychic","Shadow Ball","Focus Blast","Trick Room"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)     
#Mega Gardevoir
class MGardevoir(Pokemon2):
    "Mega Gardevoir"
    def __init__(self,name="Mega Gardevoir",type1="Psychic",type2="Fairy",nature=None,level=100,happiness=255,hp=68,atk=85,defense=65,spatk=165,spdef=135,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Pixilate",item="Gardevoirite"):
        if move is None:
            avmoves=["Protect","Recover","Dazzling Gleam","Moon Blast","Psychic","Shadow Ball","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)               
#Breloom
class Breloom(Pokemon2):
    "Breloom"
    def __init__(self,name="Breloom",type1="Grass",type2="Fighting",nature=None,level=100,happiness=255,hp=60,atk=130,defense=80,spatk=60,spdef=60,speed=70,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Poison Heal",item="Toxic Orb"):
        if move is None:
            avmoves=["Protect","Dynamic Punch","Mach Punch","Spore","Sky Uppercut","Bullet Seed","Seed Bomb","Leech Seed"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Slaking
class Slaking(Pokemon2):
    "Slaking"
    def __init__(self,name="Slaking",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=150,atk=160,defense=100,spatk=95,spdef=65,speed=10,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Lazy",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Dynamic Punch","Hyper Beam","Double Edge","Sky Uppercut","Return","Slack Off","Rest"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Hariyama
class Hariyama(Pokemon2):
    "Hariyama"
    def __init__(self,name="Hariyama",type1="Fighting",type2=None,nature=None,level=100,happiness=255,hp=144,atk=120,defense=60,spatk=40,spdef=60,speed=50,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Guts",item="Flame Orb"):
        if move is None:
            avmoves=["Protect","Dynamic Punch","Force Palm","Sky Uppercut","Arm Thrust","Belly Drum","Knock Off"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)   
#Mega Sableye
class MSableye(Pokemon2):
    "Mega Sableye"
    def __init__(self,name="Mega Sableye",type1="Dark",type2="Ghost",nature=None,level=100,happiness=255,hp=50,atk=85,defense=125,spatk=85,spdef=115,speed=20,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability="Magic Bounce",item="Sablenite"):
        if move is None:
            avmoves=["Protect","Night Shade","Shadow Sneak","Power Gem","Zen Headbutt","Knock Off","Foul Play","Moonlight"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Mega Mawile
class MMawile(Pokemon2):
    "Mega Mawile"
    def __init__(self,name="Mega Mawile",type1="Steel",type2="Fairy",nature=None,level=100,happiness=255,hp=50,atk=105,defense=125,spatk=55,spdef=95,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Huge Power",item="Mawilite"):
        if move is None:
            avmoves=["Protect","Iron Head","Play Rough","Crunch","Sucker Punch","Iron Defense"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Aggron
class Aggron(Pokemon2):
    "Aggron"
    def __init__(self,name="Aggron",type1="Steel",type2="Rock",nature=None,level=100,happiness=255,hp=70,atk=110,defense=180,spatk=60,spdef=60,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Rock Head",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Iron Head","Stone Edge","Crunch","Earthquake","Iron Defense","Hyper Beam","Flash Cannon","Body Press"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)    
#Mega Aggron
class MAggron(Pokemon2):
    "Mega Aggron"
    def __init__(self,name="Mega Aggron",type1="Steel",type2=None,nature=None,level=100,happiness=255,hp=70,atk=140,defense=230,spatk=60,spdef=80,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Filter",item="Aggronite"):
        if move is None:
            avmoves=["Protect","Iron Head","Stone Edge","Crunch","Earthquake","Iron Defense","Hyper Beam","Flash Cannon","Heavy Slam","Body Press"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Mega Medicham
class MMedicham (Pokemon2):
    "Mega Medicham"
    def __init__(self,name="Mega Medicham",type1="Fighting",type2="Psychic",nature=None,level=100,happiness=255,hp=60,atk=100,defense=85,spatk=80,spdef=85,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Pure Power",item="Medichamite"):
        if move is None:
            avmoves=["Protect","Dynamic Punch","Thunder Punch","Psycho Cut","Fire Punch","Zen Headbutt","Ice Punch"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item) 
#Medicham        
class Medicham (Pokemon2):
    "Medicham"
    def __init__(self,name="Medicham",type1="Fighting",type2="Psychic",nature=None,level=100,happiness=255,hp=60,atk=60,defense=75,spatk=60,spdef=75,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Pure Power",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Dynamic Punch","Thunder Punch","Psycho Cut","Fire Punch","Zen Headbutt","Ice Punch"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)       
#Torkoal       
class Torkoal (Pokemon2):
    "Torkoal"
    def __init__(self,name="Torkoal",type1="Fire",type2=None,nature=None,level=100,happiness=255,hp=70,atk=85,defense=140,spatk=85,spdef=70,speed=20,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Drought",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Lava Plume","Thunder Wave","Flamethrower","Toxic"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                       
#Mega Manectric
class MManectric(Pokemon2):
    "Mega Manectric"
    def __init__(self,name="Mega Manectric",type1="Electric",type2=None,nature=None,level=100,happiness=255,hp=70,atk=75,defense=80,spatk=135,spdef=80,speed=135,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Intimidate",item="Manectite"):
        if move is None:
            avmoves=["Protect","Volt Switch","Thunder","Crunch","Thunderbolt","Wild Charge","Hyper Beam","Thunder Wave"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Sharpedo
class Sharpedo(Pokemon2):
    "Sharpedo"
    def __init__(self,name="Sharpedo",type1="Water",type2="Dark",nature=None,level=100,happiness=255,hp=70,atk=120,defense=40,spatk=95,spdef=40,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Speed Boost",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Flip Turn","Hydro Pump","Crunch","Ice Beam","Surf","Dark Pulse"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)              
#Overqwil
class Overqwil(Pokemon2):
    "Overqwil"
    def __init__(self,name="Overqwil",type1="Dark",type2="Poison",nature=None,level=100,happiness=255,hp=85,atk=115,defense=95,spatk=65,spdef=65,speed=85,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Intimidate",item="Black Sludge"):
        if move is None:
            avmoves=["Protect","Flip Turn","Pin Missile","Crunch","Poison Jab","Barb Barrage","Dark Pulse","Double Edge"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Mega Sharpedo
class MSharpedo(Pokemon2):
    "Mega Sharpedo"
    def __init__(self,name="Mega Sharpedo",type1="Water",type2="Dark",nature=None,level=100,happiness=255,hp=70,atk=140,defense=70,spatk=110,spdef=65,speed=105,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Strong Jaw",item="Sharpedonite"):
        if move is None:
            avmoves=["Protect","Flip Turn","Thunder Fang","Crunch","Liquidation","Surf","Ice Fang","Poison Fang"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#Wailord
class Wailord(Pokemon2):
    "Wailord"
    def __init__(self,name="Wailord",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=170,atk=90,defense=80,spatk=105,spdef=80,speed=50,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Blubber Defense",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Water Spout","Hydro Pump","Blizzard","Ice Beam","Surf","Rain Dance","Heavy Slam","Rest"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                
#Mega Camerupt
class MCamerupt(Pokemon2):
    "Mega Camerupt"
    def __init__(self,name="Mega Camerupt",type1="Fire",type2="Ground",nature=None,level=100,happiness=255,hp=70,atk=120,defense=100,spatk=145,spdef=105,speed=20,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Sheer Force",item="Cameruptite"):
        if move is None:
            avmoves=["Protect","Eruption","Earth Power","Lava Plume","Earthquake","Stone Edge","Fire Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item) 
#Camerupt
class Camerupt(Pokemon2):
    "Camerupt"
    def __init__(self,name="Camerupt",type1="Fire",type2="Ground",nature=None,level=100,happiness=255,hp=70,atk=100,defense=70,spatk=105,spdef=75,speed=40,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Solid Rock",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Eruption","Earth Power","Lava Plume","Earthquake","Stone Edge","Fire Blast","Will-O-Wisp"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Arbok
class Arbok(Pokemon2):
    "Arbok"
    def __init__(self,name="Arbok",type1="Poison",type2="Dark",nature=None,level=100,happiness=255,hp=60,atk=85,defense=69,spatk=65,spdef=79,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Intimidate",item="Black Sludge"):
        if move is None:
            avmoves=["Protect","Venoshock","Earth Power","Poison Fang","Crunch","Gunk Shot","Blech"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Regirock
class Regirock(Pokemon2):
    "Regirock"
    def __init__(self,name="Regirock",type1="Rock",type2=None,nature=None,level=100,happiness=255,hp=80,atk=100,defense=200,spatk=50,spdef=100,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Clear Body",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Zap Cannon","Earth Power","Hyper Beam","Earthquake","Stone Edge","Rock Slide","Explosion"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      
#Regice
class Regice(Pokemon2):
    "Regice"
    def __init__(self,name="Regice",type1="Ice",type2=None,nature=None,level=100,happiness=255,hp=80,atk=50,defense=100,spatk=100,spdef=200,speed=50,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Clear Body",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Ice Beam","Blizzard","Freeze Dry","Hyper Beam","Zap Cannon","Hail","Explosion"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Registeel
class Registeel(Pokemon2):
    "Registeel"
    def __init__(self,name="Registeel",type1="Steel",type2=None,nature=None,level=100,happiness=255,hp=80,atk=75,defense=150,spatk=75,spdef=150,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Clear Body",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Iron Head","Flash Cannon","Zap Cannon","Earthquake","Hyper Beam","Curse","Explosion"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)   
#Dewgong
class Dewgong(Pokemon2):
    "Dewgong"
    def __init__(self,name="Dewgong",type1="Water",type2="Ice",nature=None,level=100,happiness=255,hp=90,atk=50,defense=80,spatk=90,spdef=95,speed=70,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Thick Fat",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hidden Power","Ice Beam","Hydro Pump","Thunderbolt","Surf","Hail","Rain Dance","Frost Breath"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)       
#Jynx
class Jynx(Pokemon2):
    "Jynx"
    def __init__(self,name="Jynx",type1="Ice",type2="Psychic",nature=None,level=100,happiness=255,hp=65,atk=50,defense=50,spatk=115,spdef=95,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Dry Skin",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hidden Power","Ice Beam","Psychic","Blizzard","Dark Pulse","Hail","Shadow Ball","Trick Room"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#Mamoswine
class Mamoswine(Pokemon2):
    "Mamoswine"
    def __init__(self,name="Mamoswine",type1="Ice",type2="Ground",nature=None,level=100,happiness=255,hp=110,atk=130,defense=80,spatk=70,spdef=60,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Thick Fat",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Ice Beam","Earthquake","Blizzard","Stone Edge","Hail","Icicle Crash"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)       
#Flygon
class Flygon(Pokemon2):
    "Flygon"
    def __init__(self,name="Flygon",type1="Ground",type2="Dragon",nature=None,level=100,happiness=255,hp=100,atk=100,defense=80,spatk=100,spdef=80,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Tinted Lens",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Dragon Claw","Earthquake","Crunch","Stone Edge","Superpower","Sandstorm"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)   
#Altaria
class Altaria(Pokemon2):
    "Altaria"
    def __init__(self,name="Altaria",type1="Dragon",type2="Flying",nature=None,level=100,happiness=255,hp=85,atk=70,defense=90,spatk=70,spdef=105,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Natural Cure",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Dragon Claw","Earthquake","Crunch","Brave Bird","Sky Attack","Moon Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#Mega Altaria
class MAltaria(Pokemon2):
    "Mega Altaria"
    def __init__(self,name="Mega Altaria",type1="Dragon",type2="Fairy",nature=None,level=100,happiness=255,hp=85,atk=110,defense=110,spatk=110,spdef=105,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Pixilate",item="Altarianite"):
        if move is None:
            avmoves=["Protect","Dragon Claw","Earthquake","Crunch","Brave Bird","Sky Attack","Moon Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
#Zangoose
class Zangoose(Pokemon2):
    "Zangoose"
    def __init__(self,name="Zangoose",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=73,atk=115,defense=70,spatk=60,spdef=70,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Toxic Boost",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Clush Claw","Slash","Crunch","X-Scissor","Facade","Close Combat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Seviper
class Seviper(Pokemon2):
    "Seviper"
    def __init__(self,name="Seviper",type1="Poison",type2=None,nature=None,level=100,happiness=255,hp=83,atk=100,defense=83,spatk=100,spdef=83,speed=85,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Shed Skin",item="Black Sludge"):
        if move is None:
            avmoves=["Protect","Poison Fang","Poison Tail","Crunch","Poison Jab","Toxic","Sludge Bomb"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      
#Exploud
class Exploud(Pokemon2):
    "Exploud"
    def __init__(self,name="Exploud",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=104,atk=81,defense=63,spatk=91,spdef=73,speed=73,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=252,speedev=0,maxiv="No",move=None, ability="Scrappy",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Boomburst","Hyper Beam","Crunch","Hyper Voice","Toxic","Double Edge","Rest"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Lunatone
class Lunatone(Pokemon2):
    "Lunatone"
    def __init__(self,name="Lunatone",type1="Rock",type2="Psychic",nature=None,level=100,happiness=255,hp=70,atk=55,defense=65,spatk=105,spdef=85,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Levitate",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Ancient Power","Hyper Beam","Psychic","Power Gem","Moon Blast","Stone Edge","Moonlight","Explosion","Trick Room"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Solrock
class Solrock(Pokemon2):
    "Solrock"
    def __init__(self,name="Solrock",type1="Rock",type2="Psychic",nature=None,level=100,happiness=255,hp=70,atk=105,defense=85,spatk=55,spdef=65,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Levitate",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Ancient Power","Hyper Beam","Psychic","Power Gem","Moon Blast","Stone Edge","Morning Sun","Explosion","Trick Room","Solar Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)              
#Whiscash
class Whiscash(Pokemon2):
    "Whiscash"
    def __init__(self,name="Whiscash",type1="Water",type2="Ground",nature=None,level=100,happiness=255,hp=110,atk=78,defense=73,spatk=76,spdef=71,speed=60,hpev=0,atkev=252,defev=252,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Oblivious",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Ancient Power","Ice Beam","Surf","Power Gem","Hydro Pump","Stone Edge","Earthquake","Rest"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item) 
#Crawdaunt
class Crawdaunt(Pokemon2):
    "Crawdaunt"
    def __init__(self,name="Crawdaunt",type1="Water",type2="Dark",nature=None,level=100,happiness=255,hp=63,atk=120,defense=85,spatk=90,spdef=55,speed=55,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Adaptability",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Ancient Power","Ice Beam","Surf","Power Gem","Hydro Pump","Crabhammer","Liquidation"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)               
#Claydol
class Claydol(Pokemon2):
    "Claydol"
    def __init__(self,name="Claydol",type1="Ground",type2="Psychic",nature=None,level=100,happiness=255,hp=60,atk=70,defense=105,spatk=80,spdef=120,speed=75,hpev=0,atkev=0,defev=252,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Levitate",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Ancient Power","Hyper Beam","Psychic","Power Gem","Earth Power","Stone Edge","Explosion","Trick Room"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)    
#Cradily
class Cradily(Pokemon2):
    "Cradily"
    def __init__(self,name="Cradily",type1="Rock",type2="Grass",nature=None,level=100,happiness=255,hp=86,atk=81,defense=97,spatk=81,spdef=107,speed=43,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Storm Drain",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Ancient Power","Hyper Beam","Giga Drain","Sludge Bomb","Earth Power","Leech Seed","Energy Ball"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Armaldo
class Armaldo(Pokemon2):
    "Armaldo"
    def __init__(self,name="Armaldo",type1="Rock",type2="Bug",nature=None,level=100,happiness=255,hp=75,atk=125,defense=100,spatk=70,spdef=80,speed=45,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Swift Swim",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Ancient Power","Hyper Beam","X-Scissor","Rock Blast","Earth Power","Crush Claw"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Milotic
class Milotic(Pokemon2):
    "Milotic"
    def __init__(self,name="Milotic",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=95,atk=60,defense=84,spatk=100,spdef=125,speed=86,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Competitive",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Recover","Ice Beam","Surf","Rain Dance","Hydro Pump","Coil","Thunderbolt"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Farigarif
class Farigarif(Pokemon2):
    "Farigarif"
    def __init__(self,name="Farigarif",type1="Normal",type2="Psychic",nature=None,level=100,happiness=255,hp=80,atk=90,defense=74,spatk=120,spdef=75,speed=85,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Armor Tail",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Recover","Psychic","Crunch","Zen Headbutt","Assurance","Hypnosis","Shadow Ball","Trick Room"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)    
#Banette
class Banette(Pokemon2):
    "Banette"
    def __init__(self,name="Banette",type1="Ghost",type2=None,nature=None,level=100,happiness=255,hp=64,atk=115,defense=65,spatk=73,spdef=63,speed=65,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Insomnia",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Recover","Knock Off","Crunch","Pantom Force","Assurance","Hypnosis","Shadow Ball","Will-O-Wisp"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Mega Banette
class MBanette(Pokemon2):
    "Mega Banette"
    def __init__(self,name="Mega Banette",type1="Ghost",type2=None,nature=None,level=100,happiness=255,hp=64,atk=165,defense=75,spatk=93,spdef=83,speed=75,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Prankster",item="Banettite"):
        if move is None:
            avmoves=["Protect","Recover","Knock Off","Crunch","Pantom Force","Assurance","Hypnosis","Shadow Ball","Toxic","Thunder Wave","Will-O-Wisp"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)     
#Absol
class Absol(Pokemon2):
    "Absol"
    def __init__(self,name="Absol",type1="Dark",type2=None,nature=None,level=100,happiness=255,hp=75,atk=130,defense=70,spatk=85,spdef=70,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Super Luck",item="Life Orb"):
        if move is None:
            avmoves=["Protect","Recover","Knock Off","Crunch","Psycho Cut","Assurance","Night Slash","Shadow Ball","Toxic","Sucker Punch","Close Combat","Swords Dance"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Mega Absol
class MAbsol(Pokemon2):
    "Mega Absol"
    def __init__(self,name="Mega Absol",type1="Dark",type2=None,nature=None,level=100,happiness=255,hp=75,atk=150,defense=70,spatk=115,spdef=70,speed=125,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Magic Bounce",item="Absolite"):
        if move is None:
            avmoves=["Protect","Recover","Knock Off","Crunch","Psycho Cut","Assurance","Night Slash","Shadow Ball","Toxic","Sucker Punch","Close Combat","Swords Dance"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)             
#Mega Glalie
class MGlalie(Pokemon2):
    "Mega Glalie"
    def __init__(self,name="Mega Glalie",type1="Ice",type2=None,nature=None,level=100,happiness=255,hp=80,atk=120,defense=80,spatk=120,spdef=80,speed=120,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Refrigerate",item="Glalite"):
        if move is None:
            avmoves=["Protect","Recover","Earthquake","Crunch","Ice Beam","Blizzard","Freeze Dry","Ice Fang","Toxic","Hail","Hyper Beam","Rain Dance","Shadow Ball"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
                                    
#Glalie
class Glalie(Pokemon2):
    "Glalie"
    def __init__(self,name="Glalie",type1="Ice",type2=None,nature=None,level=100,happiness=255,hp=80,atk=80,defense=80,spatk=100,spdef=80,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Refrigerate",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Recover","Earthquake","Crunch","Ice Beam","Blizzard","Freeze Dry","Ice Fang","Toxic","Hail","Hyper Beam","Rain Dance","Shadow Ball"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Walrein
class Walrein(Pokemon2):
    "Walrein"
    def __init__(self,name="Walrein",type1="Ice",type2="Water",nature=None,level=100,happiness=255,hp=110,atk=80,defense=90,spatk=95,spdef=90,speed=65,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Thick Fat",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Slack Off","Surf","Crunch","Ice Beam","Blizzard","Freeze Dry","Ice Fang","Rest","Hail","Hyper Beam","Rain Dance","Liquidation","Iron Head"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Huntail
class Huntail(Pokemon2):
    "Huntail"
    def __init__(self,name="Huntail",type1="Water",type2="Dark",nature=None,level=100,happiness=255,hp=55,atk=104,defense=105,spatk=94,spdef=75,speed=52,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Intimidate",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Crunch","Ice Beam","Blizzard","Liquidation","Ice Fang","Waterfall","Hydro Pump","Rain Dance","Shell Smash"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)       
#Gorebyss
class Gorebyss(Pokemon2):
    "Gorebyss"
    def __init__(self,name="Gorebyss",type1="Water",type2="Fairy",nature=None,level=100,happiness=255,hp=55,atk=84,defense=105,spatk=114,spdef=75,speed=52,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Regenerator",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Dazzling Gleam","Ice Beam","Blizzard","Moon Blast","Ice Fang","Waterfall","Hydro Pump","Rain Dance","Shell Smash"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Relicanth
class Relicanth(Pokemon2):
    "Relicanth"
    def __init__(self,name="Relicanth",type1="Water",type2="Rock",nature=None,level=100,happiness=255,hp=100,atk=105,defense=130,spatk=45,spdef=65,speed=55,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Rock Head",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Liquidation","Ice Beam","Stone Edge","Rock Slide","Ice Fang","Waterfall","Hydro Pump","Rain Dance","Head Smash"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Salamence
class Salamence(Pokemon2):
    "Salamence"
    def __init__(self,name="Salamence",type1="Dragon",type2="Flying",nature=None,level=100,happiness=255,hp=95,atk=135,defense=80,spatk=110,spdef=80,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Intimidate","Moxie"]),item="Life Orb"):
        if move is None:
            avmoves=["Protect","Stone Edge","Dragon Claw","Ice Beam","Flamethrower","Crunch","Zen Headbutt","Double Edge","Hydro Pump","Earthquake","Dragon Dance","Roost"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      
#Mega Salamence
class MSalamence(Pokemon2):
    "Mega Salamence"
    def __init__(self,name="Mega Salamence",type1="Dragon",type2="Flying",nature=None,level=100,happiness=255,hp=95,atk=145,defense=130,spatk=120,spdef=90,speed=120,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Aerilate",item="Salamencite"):
        if move is None:
            avmoves=["Protect","Stone Edge","Dragon Claw","Ice Beam","Flamethrower","Crunch","Zen Headbutt","Double Edge","Hydro Pump","Earthquake","Dragon Dance","Roost"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Metagross
class Metagross(Pokemon2):
    "Metagross"
    def __init__(self,name="Metagross",type1="Steel",type2="Psychic",nature=None,level=100,happiness=255,hp=80,atk=135,defense=130,spatk=95,spdef=90,speed=70,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Clear Body",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Stone Edge","Bullet Punch","Meteor Mash","Hyper Beam","Crunch","Zen Headbutt","Double Edge","Iron Defense","Earthquake","Hammer Arm","Flash Cannon"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                    
#MegaMetagross
class MMetagross(Pokemon2):
    "Mega Metagross"
    def __init__(self,name="Mega Metagross",type1="Steel",type2="Psychic",nature=None,level=100,happiness=255,hp=80,atk=145,defense=150,spatk=105,spdef=110,speed=110,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Tough Claws",item="Metagrossite"):
        if move is None:
            avmoves=["Protect","Stone Edge","Bullet Punch","Meteor Mash","Hyper Beam","Crunch","Zen Headbutt","Double Edge","Iron Defense","Earthquake","Hammer Arm","Flash Cannon","Fire Punch"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Latias
class Latias(Pokemon2):
    "Latias"
    def __init__(self,name="Latias",type1="Dragon",type2="Psychic",nature=None,level=100,happiness=255,hp=80,atk=80,defense=90,spatk=110,spdef=130,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Levitate",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hyper Beam","Mist Ball","Zen Headbutt","Dragon Pulse","Psychic","Calm Mind","Ice Beam","Thunderbolt","Shadow Ball"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#Latios
class Latios(Pokemon2):
    "Latios"
    def __init__(self,name="Latios",type1="Dragon",type2="Psychic",nature=None,level=100,happiness=255,hp=80,atk=90,defense=80,spatk=130,spdef=110,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Levitate",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hyper Beam","Luster Purge","Zen Headbutt","Dragon Pulse","Psychic","Calm Mind","Ice Beam","Thunderbolt","Shadow Ball"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Mega Latias
class MLatias(Pokemon2):
    "Mega Latias"
    def __init__(self,name="Mega Latias",type1="Dragon",type2="Psychic",nature=None,level=100,happiness=255,hp=80,atk=100,defense=120,spatk=140,spdef=150,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Levitate",item="Latiasite"):
        if move is None:
            avmoves=["Protect","Hyper Beam","Mist Ball","Zen Headbutt","Dragon Pulse","Psychic","Calm Mind","Ice Beam","Thunderbolt","Shadow Ball"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Mega Latios
class MLatios(Pokemon2):
    "Mega Latios"
    def __init__(self,name="Mega Latios",type1="Dragon",type2="Psychic",nature=None,level=100,happiness=255,hp=80,atk=130,defense=100,spatk=160,spdef=120,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Levitate",item="Latiosite"):
        if move is None:
            avmoves=["Protect","Hyper Beam","Luster Purge","Zen Headbutt","Dragon Pulse","Psychic","Calm Mind","Ice Beam","Thunderbolt","Shadow Ball"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                
#Kyogre
class Kyogre(Pokemon2):
    "Kyogre"
    def __init__(self,name="Kyogre",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=100,atk=100,defense=90,spatk=150,spdef=140,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Drizzle",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hyper Beam","Origin Pulse","Thunder","Water Spout","Ancient Power","Calm Mind","Ice Beam","Thunderbolt","Rest","Thunder Wave"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                   
#Primal Kyogre
class PKyogre(Pokemon2):
    "Primal Kyogre"
    def __init__(self,name="Primal Kyogre",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=100,atk=150,defense=90,spatk=180,spdef=160,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Primordial Sea",item="Blue Orb"):
        if move is None:
            avmoves=["Protect","Hyper Beam","Origin Pulse","Thunder","Water Spout","Ancient Power","Calm Mind","Ice Beam","Thunderbolt","Rest","Thunder Wave"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Groudon
class Groudon(Pokemon2):
    "Groudon"
    def __init__(self,name="Groudon",type1="Ground",type2=None,nature=None,level=100,happiness=255,hp=100,atk=150,defense=140,spatk=100,spdef=90,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Drought",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hyper Beam","Precipice Blades","Earthquake","Eruption","Ancient Power","Swords Dance","Fire Blast","Fire Punch","Rest","Thunder Wave","Solar Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item) 
#Primal Groudon
class PGroudon(Pokemon2):
    "Primal Groudon"
    def __init__(self,name="Primal Groudon",type1="Ground",type2="Fire",nature=None,level=100,happiness=255,hp=100,atk=180,defense=160,spatk=150,spdef=90,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Desolate Land",item="Red Orb"):
        if move is None:
            avmoves=["Protect","Hyper Beam","Precipice Blades","Earthquake","Eruption","Ancient Power","Swords Dance","Fire Blast","Fire Punch","Rest","Thunder Wave","Solar Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Torterra
class Torterra(Pokemon2):
    "Torterra"
    def __init__(self,name="Torterra",type1="Grass",type2="Ground",nature=None,level=100,happiness=255,hp=95,atk=109,defense=105,spatk=75,spdef=85,speed=56,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Overgrow",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hyper Beam","Wood Hammer","Earthquake","Leaf Storm","Ancient Power","Swords Dance","Curse","Synthesis","Crunch","Giga Drain","Headlong Rush"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)   
#Infernape
class Infernape(Pokemon2):
    "Infernape"
    def __init__(self,name="Infernape",type1="Fire",type2="Fighting",nature=None,level=100,happiness=255,hp=76,atk=104,defense=71,spatk=104,spdef=71,speed=108,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Blaze",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hyper Beam","Flare Blitz","Close Combat","Fire Blast","Mach Punch","Swords Dance","Power-up Punch","Overheat","Calm Mind","Flamethrower"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item) 
#Empoleon
class Empoleon(Pokemon2):
    "Empoleon"
    def __init__(self,name="Empoleon",type1="Water",type2="Steel",nature=None,level=100,happiness=255,hp=84,atk=86,defense=88,spatk=111,spdef=101,speed=60,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Torrent",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hyper Beam","Surf","Flash Cannon","Hydro Pump","Liquidation","Wave Crash","Ice Beam","Steel Beam","Rest","Scald"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Staraptor
class Staraptor(Pokemon2):
    "Staraptor"
    def __init__(self,name="Staraptor",type1="Normal",type2="Flying",nature=None,level=100,happiness=255,hp=85,atk=120,defense=70,spatk=50,spdef=60,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Intimidate","Reckless"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Final Gambit","Roost","Brave Bird","Close Combat","U-Turn","Giga Impact"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Luxray
class Luxray(Pokemon2):
    "Luxray"
    def __init__(self,name="Luxray",type1="Electric",type2="Dark",nature=None,level=100,happiness=255,hp=80,atk=120,defense=79,spatk=95,spdef=79,speed=70,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Intimidate","Guts"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Wild Charge","Crunch","Thunder Wave","Play Rough"]
            moves=moveset(avmoves)
        else:
            moves=move
        if ability=="Guts":
            item="Flame Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#Roserade
class Roserade(Pokemon2):
    "Roserade"
    def __init__(self,name="Roserade",type1="Grass",type2="Poison",nature=None,level=100,happiness=255,hp=60,atk=70,defense=65,spatk=125,spdef=105,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Technician",item="Black Sludge"):
        if move is None:
            avmoves=["Protect","Weather Ball","Toxic","Sunny Day","Giga Drain","Energy Ball"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Rampardos
class Rampardos(Pokemon2):
    "Rampardos"
    def __init__(self,name="Rampardos",type1="Rock",type2=None,nature=None,level=100,happiness=255,hp=97,atk=165,defense=60,spatk=65,spdef=50,speed=58,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Mold Breaker",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Head Smash","Iron Head","Crunch","Stone Edge"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                           
#Bastiodon
class Bastiodon(Pokemon2):
    "Bastiodon"
    def __init__(self,name="Bastiodon",type1="Rock",type2="Steel",nature=None,level=100,happiness=255,hp=60,atk=52,defense=168,spatk=47,spdef=138,speed=30,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Sturdy",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Iron Defense","Iron Head","Crunch","Stone Edge"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Vespiquen
class Vespiquen(Pokemon2):
    "Vespiquen"
    def __init__(self,name="Vespiquen",type1="Bug",type2="Flying",nature=None,level=100,happiness=255,hp=70,atk=80,defense=102,spatk=80,spdef=102,speed=40,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Pressure",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Defense Order","Attack Order","Heal Order","Toxic"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                             #Gastrodon
class WGastrodon(Pokemon2):
    "Gastrodon"
    def __init__(self,name="West Sea Gastrodon",type1="Water",type2="Ground",nature=None,level=100,happiness=255,hp=111,atk=83,defense=68,spatk=92,spdef=82,speed=39,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Storm Drain",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Earth Power","Recover","Hydro Pump","Ice Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)  
#Gastrodon
class EGastrodon(Pokemon2):
    "Gastrodon"
    def __init__(self,name="East Sea Gastrodon",type1="Water",type2="Ground",nature=None,level=100,happiness=255,hp=111,atk=83,defense=68,spatk=92,spdef=82,speed=39,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Storm Drain",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Earth Power","Recover","Hydro Pump","Ice Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Ambipom
class Ambipom(Pokemon2):
    "Ambipom"
    def __init__(self,name="Ambipom",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=75,atk=100,defense=66,spatk=60,spdef=66,speed=115,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Skill Link",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Toxic","Double Hit","U-Turn","Return"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Drifblim
class Drifblim(Pokemon2):
    "Drifblim"
    def __init__(self,name="Drifblim",type1="Ghost",type2="Flying",nature=None,level=100,happiness=255,hp=150,atk=80,defense=44,spatk=90,spdef=54,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Flare Boost",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Psychic","Shadow Ball","Calm Mind","Thunderbolt","Explosion"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Mega Lopunny
class MLopunny(Pokemon2):
    "Mega Lopunny"
    def __init__(self,name="Mega Lopunny",type1="Normal",type2="Fighting",nature=None,level=100,happiness=255,hp=65,atk=136,defense=94,spatk=54,spdef=96,speed=135,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Scrappy",item="Lopunnite"):
        if move is None:
            avmoves=["Protect","High Jump Kick","Return","Fakeout","Power-up Punch"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Mismagius
class Mismagius(Pokemon2):
    "Mismagius"
    def __init__(self,name="Mismagius",type1="Ghost",type2="Fairy",nature=None,level=100,happiness=255,hp=60,atk=60,defense=60,spatk=105,spdef=105,speed=105,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Levitate",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Psychic","Shadow Ball","Calm Mind","Thunderbolt","Dazzling Gleam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Honchkrow
class Honchkrow(Pokemon2):
    "Honchkrow"
    def __init__(self,name="Honchkrow",type1="Dark",type2="Flying",nature=None,level=100,happiness=255,hp=100,atk=125,defense=60,spatk=105,spdef=60,speed=71,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Super Luck",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Night Slash","Shadow Ball","Drill Peck","Roost","Dark Pulse"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Spiritomb
class Spiritomb(Pokemon2):
    "Spiritomb"
    def __init__(self,name="Spiritomb",type1="Ghost",type2="Dark",nature=None,level=100,happiness=255,hp=50,atk=92,defense=108,spatk=92,spdef=108,speed=35,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Pressure",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Night Slash","Shadow Ball","Hypnosis","Nasty Plot","Dark Pulse"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#Garchomp
class Garchomp(Pokemon2):
    "Garchomp"
    def __init__(self,name="Garchomp",type1="Dragon",type2="Ground",nature=None,level=100,happiness=255,hp=108,atk=130,defense=95,spatk=80,spdef=85,speed=102,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Rough Skin",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Swords Dance","Earthquake","Dragon Claw","Stone Edge","Draco Meteor","Flamethrower"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Mega Garchomp
class MGarchomp(Pokemon2):
    "Mega Garchomp"
    def __init__(self,name="Mega Garchomp",type1="Dragon",type2="Ground",nature=None,level=100,happiness=255,hp=108,atk=170,defense=115,spatk=120,spdef=95,speed=92,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Sand Force",item="Garchompite"):
        if move is None:
            avmoves=["Protect","Swords Dance","Earthquake","Dragon Claw","Stone Edge","Draco Meteor","Flamethrower"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Lucario
class Lucario(Pokemon2):
    "Lucario"
    def __init__(self,name="Lucario",type1="Fighting",type2="Steel",nature=None,level=100,happiness=255,hp=70,atk=110,defense=70,spatk=115,spdef=70,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Steadfest",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Meteor Mash","Aura Sphere","Dragon Pulse","Close Combat","Bullet Punch","Bone Rush"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Mega Lucario
class MLucario(Pokemon2):
    "Mega Lucario"
    def __init__(self,name="Mega Lucario",type1="Fighting",type2="Steel",nature=None,level=100,happiness=255,hp=70,atk=145,defense=88,spatk=140,spdef=70,speed=112,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Adaptability",item="Lucarionite"):
        if move is None:
            avmoves=["Protect","Meteor Mash","Aura Sphere","Dragon Pulse","Close Combat","Bullet Punch","Bone Rush"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Hippowdon
class Hippowdon(Pokemon2):
    "Hippowdon"
    def __init__(self,name="Hippowdon",type1="Ground",type2=None,nature=None,level=100,happiness=255,hp=108,atk=112,defense=118,spatk=68,spdef=72,speed=47,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Sand Stream",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Earthquake","Slack Off","Stone Edge","Knock Off"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Drapion
class Drapion(Pokemon2):
    "Drapion"
    def __init__(self,name="Drapion",type1="Poison",type2="Dark",nature=None,level=100,happiness=255,hp=70,atk=90,defense=110,spatk=60,spdef=75,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Sniper",item="Black Sludge"):
        if move is None:
            avmoves=["Protect","Wicked Blow","Cross Poison","Swords Dance","Knock Off","Crunch"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Toxicroak
class Toxicroak(Pokemon2):
    "Toxicroak"
    def __init__(self,name="Toxicroak",type1="Poison",type2="Fighting",nature=None,level=100,happiness=255,hp=83,atk=106,defense=65,spatk=86,spdef=65,speed=85,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Sniper",item="Black Sludge"):
        if move is None:
            avmoves=["Protect","Close Combat","Cross Poison","Swords Dance","Knock Off","Venoshock","Poison Jab"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                       
#Abomasnow
class Abomasnow(Pokemon2):
    "Abomasnow"
    def __init__(self,name="Abomasnow",type1="Grass",type2="Ice",nature=None,level=100,happiness=255,hp=90,atk=92,defense=75,spatk=92,spdef=85,speed=60,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Snow Warning",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Wood Hammer","Icicle Crash","Blizzard","Ice Shard","Energy Ball","Earth Power"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)       
#Mega Abomasnow
class MAbomasnow(Pokemon2):
    "Abomasnow"
    def __init__(self,name="Abomasnow",type1="Grass",type2="Ice",nature=None,level=100,happiness=255,hp=90,atk=132,defense=105,spatk=132,spdef=105,speed=30,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Snow Warning",item="Abomasite"):
        if move is None:
            avmoves=["Protect","Wood Hammer","Icicle Crash","Blizzard","Ice Shard","Energy Ball","Earth Power"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Weavile
class Weavile(Pokemon2):
    "Weavile"
    def __init__(self,name="Weavile",type1="Dark",type2="Ice",nature=None,level=100,happiness=255,hp=70,atk=120,defense=65,spatk=45,spdef=85,speed=125,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Pressure",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Night Slash","Icicle Crash","Blizzard","Ice Shard","Assurance","Poison Jab","Fakeout"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Magnezone
class Magnezone(Pokemon2):
    "Magnezone"
    def __init__(self,name="Magnezone",type1="Electric",type2="Steel",nature=None,level=100,happiness=255,hp=70,atk=70,defense=115,spatk=130,spdef=90,speed=60,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Levitate","Sturdy"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hidden Power","Flash Cannon","Thunderbolt","Iron Defense"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      
#Rhyperior
class Rhyperior(Pokemon2):
    "Rhyperior"
    def __init__(self,name="Rhyperior",type1="Ground",type2="Rock",nature=None,level=100,happiness=255,hp=115,atk=140,defense=130,spatk=55,spdef=55,speed=40,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=4,speedev=0,maxiv="No",move=None, ability="Solid Rock",item="Weakness Policy"):
        if move is None:
            avmoves=["Protect","Stone Edge","Hammer Arm","High Horsepower","Thunder Punch","Giga Impact"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#Tangrowth
class Tangrowth(Pokemon2):
    "Tangrowth"
    def __init__(self,name="Tangrowth",type1="Grass",type2=None,nature=None,level=100,happiness=255,hp=100,atk=100,defense=125,spatk=110,spdef=50,speed=50,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=4,speedev=0,maxiv="No",move=None, ability="Regenerator",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Giga Drain","Sleep Powder","Ancient Power","Poison Jab"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)   
#Electivire
class Electivire(Pokemon2):
    "Electivire"
    def __init__(self,name="Electivire",type1="Electric",type2=None,nature=None,level=100,happiness=255,hp=75,atk=123,defense=67,spatk=95,spdef=85,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=4,speedev=252,maxiv="No",move=None, ability="Motor Drive",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Plasma Fists","Close Combat","Wild Charge","Brick Break","Giga Impact"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Magmortar
class Magmortar(Pokemon2):
    "Magmortar"
    def __init__(self,name="Magmortar",type1="Fire",type2=None,nature=None,level=100,happiness=255,hp=75,atk=95,defense=67,spatk=125,spdef=95,speed=83,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=4,speedev=252,maxiv="No",move=None, ability="Flash Fire",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Fire Blast","Sunny Day","Flamethrower","Toxic"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                     
#Togekiss
class Togekiss(Pokemon2):
    "Togekiss"
    def __init__(self,name="Togekiss",type1="Fairy",type2="Flying",nature=None,level=100,happiness=255,hp=85,atk=50,defense=95,spatk=120,spdef=115,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=4,speedev=252,maxiv="No",move=None, ability="Serene Grace",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Roost","Nasty Plot","Air Slash","Moon Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                
#Yanmega
class Yanmega(Pokemon2):
    "Yanmega"
    def __init__(self,name="Yanmega",type1="Bug",type2="Flying",nature=None,level=100,happiness=255,hp=86,atk=76,defense=86,spatk=116,spdef=56,speed=95,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=4,speedev=252,maxiv="No",move=None, ability="Speed Boost",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Ancient Power","Bug Buzz","Air Slash","U-Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)              
#Gliscor
class Gliscor(Pokemon2):
    "Gliscor"
    def __init__(self,name="Gliscor",type1="Ground",type2="Flying",nature=None,level=100,happiness=255,hp=75,atk=95,defense=125,spatk=45,spdef=75,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=4,speedev=252,maxiv="No",move=None, ability="Poison Heal",item="Toxic Orb"):
        if move is None:
            avmoves=["Protect","Swords Dance","Earthquake","Rock Slide","U-Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                         
#Porygon-Z
class PorygonZ(Pokemon2):
    "Porygon-Z"
    def __init__(self,name="Porygon-Z",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=85,atk=80,defense=70,spatk=135,spdef=75,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=4,speedev=252,maxiv="No",move=None, ability="Adaptability",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Ice Beam","Calm Mind","Recover","Thunderbolt","Flamethrower","Signal Beam","Hidden Power","Psychic","Shadow Ball","Hyper Beam","Trick Room"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                          
#Gallade
class Gallade(Pokemon2):
    "Gallade"
    def __init__(self,name="Gallade",type1="Psychic",type2="Fighting",nature=None,level=100,happiness=255,hp=68,atk=125,defense=65,spatk=65,spdef=115,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=4,speedev=252,maxiv="No",move=None, ability="Steadfast",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Swords Dance","Psycho Cut","Night Slash","Close Combat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Mega Gallade
class MGallade(Pokemon2):
    "Mega Gallade"
    def __init__(self,name="Mega Gallade",type1="Psychic",type2="Flighting",nature=None,level=100,happiness=255,hp=68,atk=165,defense=95,spatk=65,spdef=115,speed=110,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=4,speedev=252,maxiv="No",move=None, ability="Inner Focus",item="Galladite"):
        if move is None:
            avmoves=["Protect","Swords Dance","Psycho Cut","Night Slash","Close Combat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                           
#Hisuian Arcanine
class HArcanine(Pokemon2):
    "Hisuian Arcanine"
    def __init__(self,name="Hisuian Arcanine",type1="Fire",type2="Rock",nature=None,level=100,happiness=255,hp=95,atk=125,defense=80,spatk=85,spdef=80,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Intimidate","Flash Fire","Rock Head"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Fire Fang","Flare Blitz","Wild Charge","Head Smash","Headlong Rush","Morning Sun","Raging Fury"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)     
#Ursaluna
class Ursaluna(Pokemon2):
    "Ursaluna"
    def __init__(self,name="Ursaluna",type1="Normal",type2="Ground",nature=None,level=100,happiness=255,hp=130,atk=140,defense=105,spatk=45,spdef=80,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Guts","Rock Head"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Bulk Up","Double Edge","High Horsepower","Head Smash","Headlong Rush","Moonlight"]
            moves=moveset(avmoves)
        else:
            moves=move
        if ability=="Guts":
            item="Flame Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Probopass
class Probopass(Pokemon2):
    "Probopass"
    def __init__(self,name="Probopass",type1="Rock",type2="Steel",nature=None,level=100,happiness=255,hp=60,atk=55,defense=145,spatk=75,spdef=150,speed=40,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability=random.choice(["Sturdy","Sand Force"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Iron Defense","Thunder Wave","Heavy Slam","Sandstorm","Zap Cannon","Power Gem","Rest"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                       
#Dusknoir
class Dusknoir(Pokemon2):
    "Dusknoir"
    def __init__(self,name="Dusknoir",type1="Rock",type2="Steel",nature=None,level=100,happiness=255,hp=45,atk=100,defense=135,spatk=65,spdef=135,speed=45,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability=random.choice(["Pressure","Levitate"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Will-O-Wisp","Thunder Wave","Shadow Punch","Hex","Calm Mind","Rest"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Froslass
class Froslass(Pokemon2):
    "Froslass"
    def __init__(self,name="Froslass",type1="Ice",type2="Ghost",nature=None,level=100,happiness=255,hp=70,atk=80,defense=70,spatk=80,spdef=70,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Snow Cloak","Levitate"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Will-O-Wisp","Blizzard","Shadow Punch","Hex","Calm Mind","Ice Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Wash Rotom
class WRotom(Pokemon2):
    "Wash Rotom"
    def __init__(self,name="Wash Rotom",type1="Electric",type2="Water",nature=None,level=100,happiness=255,hp=50,atk=65,defense=107,spatk=105,spdef=107,speed=86,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=4,maxiv="No",move=None, ability=random.choice(["Levitate"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Volt Switch","Thunder Wave","Hydro Pump","Hex","Ice Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
#Uxie
class Uxie(Pokemon2):
    "Uxie"
    def __init__(self,name="Uxie",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=75,atk=75,defense=130,spatk=75,spdef=130,speed=95,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Levitate"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Thunder Wave","Recover","Shadow Ball","Psychic","Calm Mind"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Mesprit
class Mesprit(Pokemon2):
    "Mesprit"
    def __init__(self,name="Mesprit",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=80,atk=105,defense=105,spatk=105,spdef=105,speed=80,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Levitate"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Thunder Wave","Recover","Shadow Ball","Psychic","Calm Mind"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Azelf
class Azelf(Pokemon2):
    "Azelf"
    def __init__(self,name="Azelf",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=75,atk=125,defense=70,spatk=125,spdef=70,speed=115,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Levitate"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Thunderbolt","Recover","Shadow Ball","Psychic","Calm Mind","Ice Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Dialga
class Dialga(Pokemon2):
    "Dialga"
    def __init__(self,name="Dialga",type1="Steel",type2="Dragon",nature=None,level=100,happiness=255,hp=100,atk=120,defense=120,spatk=150,spdef=100,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Levitate"]),item="Adamant Orb"):
        if move is None:
            avmoves=["Protect","Flash Cannon","Rest","Roar of Time","Aura Sphere","Earth Power"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Origin Dialga
class ODialga(Pokemon2):
    "Origin Dialga"
    def __init__(self,name="Origin Dialga",type1="Steel",type2="Dragon",nature=None,level=100,happiness=255,hp=100,atk=100,defense=120,spatk=150,spdef=120,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Levitate"]),item="Adamant Orb"):
        if move is None:
            avmoves=["Protect","Flash Cannon","Rest","Roar of Time","Aura Sphere","Earth Power"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Palkia
class Palkia(Pokemon2):
    "Palkia"
    def __init__(self,name="Palkia",type1="Water",type2="Dragon",nature=None,level=100,happiness=255,hp=90,atk=120,defense=100,spatk=150,spdef=120,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Levitate"]),item="Lustrous Orb"):
        if move is None:
            avmoves=["Protect","Hydro Pump","Rest","Spacial Rend","Aura Sphere","Earth Power"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Origin Palkia
class OPalkia(Pokemon2):
    "Origin Palkia"
    def __init__(self,name="Origin Palkia",type1="Water",type2="Dragon",nature=None,level=100,happiness=255,hp=90,atk=100,defense=100,spatk=150,spdef=120,speed=120,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Levitate"]),item="Lustrous Orb"):
        if move is None:
            avmoves=["Protect","Hydro Pump","Rest","Spacial Rend","Aura Sphere","Earth Power"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      
#Giratina
class Giratina(Pokemon2):
    "Giratina"
    def __init__(self,name="Giratina",type1="Ghost",type2="Dragon",nature=None,level=100,happiness=255,hp=150,atk=100,defense=120,spatk=100,spdef=120,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Levitate"]),item="Griseous Orb"):
        if move is None:
            avmoves=["Protect","Shadow Ball","Rest","Shadow Force","Aura Sphere","Earth Power"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Origin Giratina
class OGiratina(Pokemon2):
    "Origin Giratina"
    def __init__(self,name="Origin Giratina",type1="Ghost",type2="Dragon",nature=None,level=100,happiness=255,hp=150,atk=120,defense=120,spatk=100,spdef=100,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Levitate"]),item="Griseous Orb"):
        if move is None:
            avmoves=["Protect","Shadow Ball","Rest","Shadow Force","Aura Sphere","Earth Power"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      
#Heatran
class Heatran(Pokemon2):
    "Heatran"
    def __init__(self,name="Heatran",type1="Fire",type2="Steel",nature=None,level=100,happiness=255,hp=91,atk=90,defense=106,spatk=130,spdef=106,speed=77,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Flash Fire"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Magma Storm","Fire Blast","Flash Cannon","Ancient Power","Earth Power"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)  
#Regigigas
class Regigigas(Pokemon2):
    "Regigigas"
    def __init__(self,name="Regigias",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=110,atk=160,defense=110,spatk=80,spdef=110,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Titan's Rage"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Crush Grip","Giga Impact","Iron Head","Hyper Beam","Earthquake"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                      
#Cresselia
class Cresselia(Pokemon2):
    "Cresselia"
    def __init__(self,name="Cresselia",type1="Fairy",type2=None,nature=None,level=100,happiness=255,hp=120,atk=70,defense=120,spatk=75,spdef=130,speed=85,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Levitate"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Lunar Blessing","Moon Blast","Psychic","Calm Mind","Dazzling Gleam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
#Phione
class Phione(Pokemon2):
    "Phione"
    def __init__(self,name="Phione",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=80,atk=80,defense=80,spatk=80,spdef=80,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Hydration"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Take Heart","Hydro Pump","Moon Blast","Calm Mind","Acid Armor"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Manaphy
class Manaphy(Pokemon2):
    "Manaphy"
    def __init__(self,name="Manaphy",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=100,atk=100,defense=100,spatk=100,spdef=100,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Hydration"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Heart Swap","Hydro Pump","Tail Glow","Rain Dance","Acid Armor"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Darkrai
class Darkrai(Pokemon2):
    "Darkrai"
    def __init__(self,name="Darkrai",type1="Dark",type2=None,nature=None,level=100,happiness=255,hp=70,atk=90,defense=90,spatk=135,spdef=90,speed=125,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Bad Dreams"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Dark Void","Shadow Ball","Psychic","Nasty Plot","Dark Pulse"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Shaymin
class Shaymin(Pokemon2):
    "Shaymin"
    def __init__(self,name="Shaymin",type1="Grass",type2=None,nature=None,level=100,happiness=255,hp=100,atk=100,defense=100,spatk=100,spdef=100,speed=100,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Natural Cure"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Seed Flare","Energy Ball","Synthesis","Leech Seed","Hidden Power"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Sky Shaymin
class SShaymin(Pokemon2):
    "Sky Shaymin"
    def __init__(self,name="Sky Shaymin",type1="Grass",type2="Flying",nature=None,level=100,happiness=255,hp=100,atk=103,defense=75,spatk=120,spdef=75,speed=127,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Natural Cure"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Seed Flare","Energy Ball","Synthesis","Leech Seed","Hidden Power"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
#Arceus
class Arceus(Pokemon2):
    "Arceus"
    def __init__(self,name="Arceus",type1=random.choice(["Rock","Fire","Water","Grass","Electric","Ground","Flying","Fighting","Fairy","Dragon","Steel","Poison","Dark","Ghost","Normal","Bug","Ice"]),type2=None,nature=None,level=100,happiness=255,hp=120,atk=120,defense=120,spatk=120,spdef=120,speed=120,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Multitype"]),item="Elemental Plates"):
        if move is None:
            avmoves=["Protect","Judgement","Hyper Beam","Extreme Speed","Recover","Hidden Power"]
            moves=moveset(avmoves)
        else:
            moves=move
        name=name+f"({type1})"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Origin Arceus
class OArceus(Pokemon2):
    "Origin Arceus"
    def __init__(self,name="Origin Arceus",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=200,atk=200,defense=200,spatk=200,spdef=200,speed=200,hpev=252,atkev=252,defev=252,spatkev=252,spdefev=252,speedev=252,maxiv="Yes",move=None, ability=random.choice(["Typeless"]),item=None):
        if move is None:
            avmoves=["Protect","Judgement","Roar of Time","Spacial Rend","Origin Pulse","Precipice Blades","Dragon Ascent","Magma Storm","Dark Void","Lunar Blessing","Crush Grip","Shadow Force","Aeroblast","Sacred Fire","Take Heart","Heart Swap","Seed Flare","Bleakwind Storm","Wildbolt Storm","Sandsear Storm","Sacred Sword","Secret Sword"]
            moves=avmoves
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Mightyena
class Mightyena(Pokemon2):
    "Mightyena"
    def __init__(self,name="Mightyena",type1="Dark",type2=None,nature=None,level=100,happiness=255,hp=70,atk=90,defense=70,spatk=60,spdef=60,speed=70,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Strong Jaw"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Crunch","Fire Fang","Thunder Fang","Ice Fang","Poison Fang"]
            moves=moveset(avmoves)
        else:
            moves=move
        
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item) 
#Bronzong
class Bronzong(Pokemon2):
    "Bronzong"
    def __init__(self,name="Bronzong",type1="Steel",type2="Psychic",nature=None,level=100,happiness=255,hp=67,atk=89,defense=116,spatk=79,spdef=116,speed=33,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability=random.choice(["Levitate"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Trick Room","Extrasensory","Thunder Wave","Flash Cannon","Iron Defense"]
            moves=moveset(avmoves)
        else:
            moves=move
        
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
                                                                                                         #Victini
class Victini(Pokemon2):
    "Victini"
    def __init__(self,name="Victini",type1="Psychic",type2="Fire",nature=None,level=100,happiness=255,hp=100,atk=100,defense=100,spatk=100,spdef=100,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Victory Star",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Searing Shot","Hidden Power","V-create","Psychic","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)       
#Serperior
class Serperior(Pokemon2):
    "Serperior"
    def __init__(self,name="Serperior",type1="Grass",type2="Dragon",nature=None,level=100,happiness=255,hp=75,atk=75,defense=95,spatk=75,spdef=95,speed=113,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Contrary",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Leaf Storm","Hidden Power","Giga Drain","Coil","Focus Blast","Leech Seed"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)     
#Emboar
class Emboar(Pokemon2):
    "Emboar"
    def __init__(self,name="Emboar",type1="Fire",type2="Fighting",nature=None,level=100,happiness=255,hp=110,atk=123,defense=65,spatk=100,spdef=65,speed=65,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Reckless",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hammer Arm","Flare Blitz","Heat Crash","Head Smash","Close Combat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#Samurott
class Samurott(Pokemon2):
    "Samurott"
    def __init__(self,name="Samurott",type1="Water",type2="Steel",nature=None,level=100,happiness=255,hp=95,atk=100,defense=85,spatk=108,spdef=70,speed=70,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Shell Armor",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Swords Dance","Razor Shell","Aqua Jet","Megahorn","Hydro Pump"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Hisuian Samurott
class HSamurott(Pokemon2):
    "Hisuian Samurott"
    def __init__(self,name="Hisuian Samurott",type1="Water",type2="Dark",nature=None,level=100,happiness=255,hp=90,atk=108,defense=80,spatk=100,spdef=65,speed=85,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Shell Armor",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Swords Dance","Razor Shell","Aqua Jet","Megahorn","Hydro Pump","Night Slash","Ceaseless Edge"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Hisuian Typhlosion
class HTyphlosion(Pokemon2):
    "Hisuian Typhlosion"
    def __init__(self,name="Hisuian Typhlosion",type1="Fire",type2="Ghost",nature=None,level=100,happiness=255,hp=73,atk=84,defense=78,spatk=119,spdef=85,speed=95,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Flash Fire",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hidden Power","Earth Power","Fire Blast","Lava Plume","Eruption","Focus Blast","Shadow Ball","Infernal Parade","Hex"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Unfezant
class Unfezant(Pokemon2):
    "Unfezant"
    def __init__(self,name="Unfezant",type1="Normal",type2="Flying",nature=None,level=100,happiness=255,hp=80,atk=115,defense=80,spatk=65,spdef=55,speed=93,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Super Luck","Big Pecks"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Final Gambit","Roost","Brave Bird","Close Combat","U-Turn","Giga Impact","Sky Attack","Air Slash"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                                                                                                                 #Zebstrika
class Zebstrika(Pokemon2):
    "Zebstrika"
    def __init__(self,name="Zebstrika",type1="Electric",type2=None,nature=None,level=100,happiness=255,hp=75,atk=100,defense=63,spatk=80,spdef=63,speed=116,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Motor Drive",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Wild Charge","Discharge","Thunderbolt","Thunder Wave","Volt Switch"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                                                                                                                 #Stoutland
class Stoutland(Pokemon2):
    "Stoutland"
    def __init__(self,name="Stoutland",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=85,atk=110,defense=90,spatk=45,spdef=90,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Scrappy",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Giga Impact","Crunch","Play Rough","Thunder Fang","Stomping Tantrum"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                  
#Gigalith
class Gigalith(Pokemon2):
    "Gigalith"
    def __init__(self,name="Gigalith",type1="Rock",type2=None,nature=None,level=100,happiness=255,hp=85,atk=135,defense=130,spatk=60,spdef=80,speed=25,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability=random.choice(["Sturdy","Sand Force","Sand Stream"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Iron Defense","Stone Edge","Rock Blast","Earthquake","Explosion","Rock Slide","Rest"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Excadrill
class Excadrill(Pokemon2):
    "Excadrill"
    def __init__(self,name="Excadrill",type1="Ground",type2="Steel",nature=None,level=100,happiness=255,hp=110,atk=135,defense=60,spatk=50,spdef=65,speed=88,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Sand Rush","Sand Force"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Swords Dance","Earthquake","Drill Run","Iron Head","Rock Slide"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Conkeldurr
class Conkeldurr(Pokemon2):
    "Conkeldurr"
    def __init__(self,name="Conkeldurr",type1="Fighting",type2=None,nature=None,level=100,happiness=255,hp=105,atk=140,defense=95,spatk=55,spdef=65,speed=45,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Guts",item="Flame Orb"):
        if move is None:
            avmoves=["Protect","Mach Punch","Drain Punch","Bulk Up","Facade","Knock Off"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Seismitoad
class Seismitoad (Pokemon2):
    "Seismitoad"
    def __init__(self,name="Seismitoad",type1="Water",type2="Ground",nature=None,level=100,happiness=255,hp=105,atk=95,defense=75,spatk=85,spdef=75,speed=74,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Swift Swim",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Liquidation","Earthquake","Stone Edge","Drain Punch","Waterfall","Ice Punch"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Leavanny
class Leavanny(Pokemon2):
    "Leavanny"
    def __init__(self,name="Leavanny",type1="Bug",type2="Grass",nature=None,level=100,happiness=255,hp=75,atk=103,defense=80,spatk=70,spdef=80,speed=92,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=4,speedev=252,maxiv="No",move=None, ability="Chlorophyll",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Razor Leaf","Swords Dance","X-Scissor","U-Turn","Leaf Blade"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)       
#Scolipede
class Scolipede(Pokemon2):
    "Scolipede"
    def __init__(self,name="Scolipede",type1="Bug",type2="Poison",nature=None,level=100,happiness=255,hp=60,atk=100,defense=89,spatk=55,spdef=69,speed=112,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=4,speedev=252,maxiv="No",move=None, ability="Speed Boost",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Leech Life","Megahorn","Toxic","U-Turn","X-Scissor","Poison Jab"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Basculegion
class Basculegion (Pokemon2):
    "Basculegion"
    def __init__(self,name="Basculegion",type1="Water",type2="Ghost",nature=None,level=100,happiness=255,hp=120,atk=112,defense=65,spatk=80,spdef=75,speed=78,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Reckless",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Wave Crash","Crunch","Aqua Tail","Aqua Jet","Waterfall","Zen Headbutt"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Hisuian Lilligant
class HLilligant(Pokemon2):
    "Hisuian Lilligant"
    def __init__(self,name="Hisuian Lilligant",type1="Grass",type2="Fighting",nature=None,level=100,happiness=255,hp=70,atk=105,defense=75,spatk=50,spdef=75,speed=105,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=4,speedev=252,maxiv="No",move=None, ability="Chlorophyll",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Leaf Blade","Swords Dance","Victory Dance","Close Combat","Petal Dance","Recover","Drain Punch","Sleep Powder"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Krookodile
class Krookodile(Pokemon2):
    "Krookodile"
    def __init__(self,name="Krookodile",type1="Ground",type2="Dark",nature=None,level=100,happiness=255,hp=95,atk=117,defense=80,spatk=65,spdef=70,speed=92,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Intimidate","Moxie"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Wicked Blow","Earthquake","Stone Edge","Crunch","Foul Play","Outrage"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Darmanitan
class Darmanitan(Pokemon2):
    "Darmanitan"
    def __init__(self,name="Darmanitan",type1="Fire",type2=None,nature=None,level=100,happiness=255,hp=105,atk=140,defense=55,spatk=30,spdef=55,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Sheer Force","Zen Mode"]),item="Leftovers"):
        if move is None:
            avmoves=["Superpower","Earthquake","Stone Edge","Crunch","Flare Blitz","U-Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Galarian Darmanitan
class GDarmanitan(Pokemon2):
    "Galarian Darmanitan"
    def __init__(self,name="Galarian Darmanitan",type1="Ice",type2=None,nature=None,level=100,happiness=255,hp=105,atk=140,defense=55,spatk=30,spdef=55,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Gorilla Tactics","Zen Mode"]),item="Leftovers"):
        if move is None:
            avmoves=["Superpower","Earthquake","Stone Edge","Crunch","Icicle Crash","U-Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Scrafty
class Scrafty(Pokemon2):
    "Scrafty"
    def __init__(self,name="Scrafty",type1="Dark",type2="Fighting",nature=None,level=100,happiness=255,hp=65,atk=90,defense=115,spatk=45,spdef=115,speed=58,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Intimidate","Moxie"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Close Combat","Drain Punch","Fakeout","Crunch","Foul Play","Knock Off"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Cofagrigus
class Cofagrigus(Pokemon2):
    "Cofagrigus"
    def __init__(self,name="Cofagrigus",type1="Ghost",type2=None,nature=None,level=100,happiness=255,hp=58,atk=50,defense=145,spatk=95,spdef=105,speed=30,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Mummy"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Will-O-Wisp","Hex","Shadow Sneak","Dark Pulse","Body Press"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Runerigus
class Runerigus(Pokemon2):
    "Runerigus"
    def __init__(self,name="Runerigus",type1="Ground",type2="Ghost",nature=None,level=100,happiness=255,hp=58,atk=95,defense=145,spatk=50,spdef=105,speed=30,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Wandering Spirit"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Will-O-Wisp","Shadow Claw","Shadow Sneak","Earthquake","Body Press"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Carracosta
class Carracosta (Pokemon2):
    "Carracosta"
    def __init__(self,name="Carracosta",type1="Water",type2="Rock",nature=None,level=100,happiness=255,hp=74,atk=108,defense=133,spatk=83,spdef=65,speed=32,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Solid Rock",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Liquidation","Earthquake","Stone Edge","Ancient Power","Waterfall","Shell Smash"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)    
#Archeops
class Archeops(Pokemon2):
    "Archeops"
    def __init__(self,name="Archeops",type1="Rock",type2="Flying",nature=None,level=100,happiness=255,hp=75,atk=140,defense=65,spatk=80,spdef=65,speed=110,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Speed Boost",item=None):
        if move is None:
            avmoves=["Protect","Acrobatics","Earthquake","Stone Edge","Dragon Claw","Crunch","U-Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Zoroark
class Zoroark(Pokemon2):
    "Zoroark"
    def __init__(self,name="Zoroark",type1="Dark",type2=None,nature=None,level=100,happiness=255,hp=60,atk=105,defense=60,spatk=120,spdef=60,speed=105,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Illusion",item="Life Orb"):
        if move is None:
            avmoves=["Protect","Dark Pulse","Flamethrower","Nasty Plot","Night Daze","Knock Off","U-Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Hisuian Zoroark
class HZoroark(Pokemon2):
    "Hisuian Zoroark"
    def __init__(self,name="Hisuian Zoroark",type1="Normal",type2="Ghost",nature=None,level=100,happiness=255,hp=55,atk=100,defense=60,spatk=125,spdef=60,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Illusion",item=None):
        if move is None:
            avmoves=["Protect","Shadow Ball","Flamethrower","Nasty Plot","Bitter Malice","Knock Off","U-Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Gothitelle
class Gothitelle(Pokemon2):
    "Gothitelle"
    def __init__(self,name="Gothitelle",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=70,atk=55,defense=95,spatk=95,spdef=110,speed=65,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Competitive",item=None):
        if move is None:
            avmoves=["Protect","Shadow Ball","Psychic","Calm Mind","Hypnosis","Thunder Wave","Stored Power"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Reuniclus
class Reuniclus(Pokemon2):
    "Reuniclus"
    def __init__(self,name="Reuniclus",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=110,atk=65,defense=75,spatk=125,spdef=85,speed=30,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Magic Guard",item=None):
        if move is None:
            avmoves=["Protect","Shadow Ball","Psychic","Calm Mind","Acid Armor","Thunder Wave","Stored Power"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                                                                                                                 #Swanna
class Swanna(Pokemon2):
    "Swanna"
    def __init__(self,name="Swanna",type1="Water",type2="Flying",nature=None,level=100,happiness=255,hp=75,atk=87,defense=63,spatk=87,spdef=63,speed=98,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Hydration",item=None):
        if move is None:
            avmoves=["Protect","Brave Bird","Hurricane","Rain Dance","Roost","Air Slash","Surf"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Vanilluxe
class Vanilluxe(Pokemon2):
    "Vanilluxe"
    def __init__(self,name="Vanilluxe",type1="Ice",type2=None,nature=None,level=100,happiness=255,hp=71,atk=95,defense=85,spatk=110,spdef=95,speed=79,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Snow Warning",item=None):
        if move is None:
            avmoves=["Protect","Blizzard","Ice Beam","Acid Armor","Icicle Spear","Freeze Dry","Weather Ball"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Escavalier
class Escavalier(Pokemon2):
    "Escavalier"
    def __init__(self,name="Escavalier",type1="Bug",type2="Steel",nature=None,level=100,happiness=255,hp=70,atk=135,defense=105,spatk=60,spdef=105,speed=20,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Shell Armor",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Iron Head","Iron Defense","X-Scissor","U-Turn","Swords Dance"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Jellicent
class Jellicent(Pokemon2):
    "Jellicent"
    def __init__(self,name="Jellicent",type1="Water",type2="Ghost",nature=None,level=100,happiness=255,hp=100,atk=60,defense=70,spatk=85,spdef=105,speed=60,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Water Absorb",item=None):
        if move is None:
            avmoves=["Protect","Night Shade","Acid Armor","Rain Dance","Recover","Will-O-Wisp","Hex"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
#Galvantula
class Galvantula(Pokemon2):
    "Galvantula"
    def __init__(self,name="Galvantula",type1="Bug",type2="Electric",nature=None,level=100,happiness=255,hp=70,atk=77,defense=60,spatk=97,spdef=60,speed=108,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Shell Armor",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Electoweb","Thunder Wave","Electro Ball","Sucker Punch","Discharge","Bug Buzz","Giga Drain"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Ferrothorn
class Ferrothorn(Pokemon2):
    "Ferrothorn"
    def __init__(self,name="Ferrothorn",type1="Grass",type2="Steel",nature=None,level=100,happiness=255,hp=74,atk=94,defense=131,spatk=54,spdef=116,speed=20,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability="Iron Barbs",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Gyro Ball","Iron Defense","Power Whip","Leech Seed","Curse","Heavy Slam","Body Press"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Eelektross
class Eelektross(Pokemon2):
    "Eelektross"
    def __init__(self,name="Eelektross",type1="Electric",type2=None,nature=None,level=100,happiness=255,hp=85,atk=116,defense=80,spatk=105,spdef=80,speed=50,hpev=0,atkev=252,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Levitate",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Wild Charge","Thunder Wave","Coil","Sludge Bomb","Discharge","Crunch","Crush Claw","Dragon Claw","Toxic"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Chandelure
class Chandelure(Pokemon2):
    "Chandelure"
    def __init__(self,name="Chandelure",type1="Ghost",type2="Fire",nature=None,level=100,happiness=255,hp=60,atk=55,defense=90,spatk=145,spdef=90,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Flash Fire",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hidden Power","Fire Blast","Focus Blast","Shadow Ball","Infernal Parade","Hex","Will-O-Wisp","Overheat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Haxorus
class Haxorus(Pokemon2):
    "Haxorus"
    def __init__(self,name="Haxorus",type1="Dragon",type2=None,nature=None,level=100,happiness=255,hp=76,atk=147,defense=90,spatk=60,spdef=70,speed=97,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Mold Breaker",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Outrage","Swords Dance","Dual Chop","Dragon Dance","Dragon Claw","Crunch"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                                                                                                                                                      
                                                                                                                                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            