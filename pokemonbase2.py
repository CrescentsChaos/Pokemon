#pylint:disable=R0914
#pylint:disable=C0304
#pylint:disable=R0913
#pylint:disable=C0301
#pylint:disable=C0303
from pokemonbase import *
#from attack import zmove
class Pokemon2:
    weather=None
    "Pokemon2"
    def __init__(self,name="Unidentified",type1="Normal",type2=None,nature=None,level=100,happiness=0,hp=0,atk=0,defense=0,spatk=0,spdef=0,speed=0,hpiv=0,atkiv=0,defiv=0,spatkiv=0,spdefiv=0,speediv=0,maxiv="No",atktype="Normal",hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0,status="Alive",atkb=1,defb=1,spatkb=1,spdefb=1,speedb=1,ability=None,moves=None,movez=None,badpoison=1,flinch=False,recharge=False,seeded=False):
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
        self.badpoison=badpoison
        self.recharge=recharge
        self.seeded=seeded
        self.flinch=flinch
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
                self.name+=f"(Z-Crystal)"
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
        if self.ability=="Guts":
            #print(f"{self.name} was burned by flame orb.")
            self.status="Burned"
            self.atk*=1.5
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
    def __init__(self,name="Kabutops",type1="Rock",type2="Water",nature=None,level=100,happiness=255,hp=60,atk=115,defense=105,spatk=65,spdef=70,speed=80,hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Swift Swim"):
        if move is None:
            avmoves=["Liquidation","Hydro Pump","Rock Slide","Stone Edge","Flip Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                  
#Aerodactyl
class Aerodactyl (Pokemon2):
    "Aerodactyl"
    def __init__(self,name="Aerodactyl",type1="Rock",type2="Flying",nature=None,level=100,happiness=255,hp=80,atk=105,defense=65,spatk=60,spdef=75,speed=130,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Rock Head"):
        if move is None:
            avmoves=["Ancient Power","Stone Edge","Rock Slide","Brave Bird"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)              
#Mega  Aerodactyl
class MAerodactyl (Pokemon2):
    "Mega Aerodactyl"
    def __init__(self,name="Mega Aerodactyl",type1="Rock",type2="Flying",nature=None,level=100,happiness=255,hp=80,atk=135,defense=85,spatk=70,spdef=95,speed=150,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Tough Claws"):
        if move is None:
            avmoves=["Ancient Power","Stone Edge","Rock Slide","Brave Bird"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)    
#Snorlax
class Snorlax(Pokemon2):
    "Snorlax"
    def __init__(self,name="Snorlax",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=160,atk=110,defense=65,spatk=65,spdef=110,speed=30,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability="Thick Fat"):
        if move is None:
            avmoves=["Hidden Power","Ice Beam","Body Slam","Thunder Punch","Double Edge","Hyper Beam","Giga Impact","Rest"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)
#Articuno
class Articuno    (Pokemon2):
    "Articuno"
    def __init__(self,name="Articuno",type1="Ice",type2="Flying",nature=None,level=100,happiness=255,hp=90,atk=85,defense=100,spatk=95,spdef=125,speed=85,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Snow Warning"):
        if move is None:
            avmoves=["Hidden Power","Ice Beam","Blizzard","Freeze Dry","Brave Bird","Sky Attack","Roost"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)      
#Zapdos
class Zapdos(Pokemon2):
    "Zapdos"
    def __init__(self,name="Zapdos",type1="Electric",type2="Flying",nature=None,level=100,happiness=255,hp=90,atk=90,defense=85,spatk=125,spdef=90,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Drizzle"):
        if move is None:
            avmoves=["Hidden Power","Thunder","Brave Bird","Thunderbolt","Sky Attack","Roost",", Thunder Wave"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)             
#Moltres
class Moltres(Pokemon2):
    "Moltres"
    def __init__(self,name="Moltres",type1="Fire",type2="Flying",nature=None,level=100,happiness=255,hp=90,atk=100,defense=90,spatk=125,spdef=85,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Drought"):
        if move is None:
            avmoves=["Hidden Power","Flamethrower","Hurricane","Heat Wave","Sky Attack","Brave Bird","Fire Blast","Roost"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)
#Dragonite
class Dragonite(Pokemon2):
    "Dragonite"
    def __init__(self,name="Dragonite",type1="Dragon",type2="Flying",nature=None,level=100,happiness=255,hp=91,atk=134,defense=95,spatk=100,spdef=100,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Multiscale"):
        if move is None:
            avmoves=["Hidden Power","Ice Beam","Hydro Pump","Thunderbolt","Surf","Dragon Claw","Double Edge","Thunder Wave"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)
#Mewtwo
class Mewtwo(Pokemon2):
    "Mewtwo"
    def __init__(self,name="Mewtwo",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=106,atk=110,defense=90,spatk=154,spdef=90,speed=130,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Regenerator"):
        if move is None:
            avmoves=["Hidden Power","Psystrike","Shadow Ball","Dark Pulse","Ice Beam","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)
#Mew
class Mew(Pokemon2):
    "Mew"
    def __init__(self,name="Mew",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=100,atk=100,defense=100,spatk=100,spdef=100,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Regenerator"):
        if move is None:
            avmoves=["Shadow Ball","Hidden Power","Transform","Psychic","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)
#Mega Venusaur 
class MVenusaur(Pokemon2):
    "Mega Venusaur"
    def __init__(self,name="Mega Venusaur",type1="Grass",type2="Poison",nature=None,level=100,happiness=255,hp=80,atk=100,defense=123,spatk=122,spdef=120,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Thick Fat"):
        if move is None:
            avmoves=["Hidden Power","Giga Drain","Sludge Bomb","Earth Power","Sleep Powder"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)
#Mega Blastoise
class MBlastoise(Pokemon2):
    "Mega Blastoise"
    def __init__(self,name="Mega Blastoise",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=79,atk=103,defense=120,spatk=135,spdef=115,speed=78,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Mega Launcher"):
        if move is None:
            avmoves=["Hidden Power","Ice Beam","Hydro Pump","Dark Pulse","Dragon Pulse","Aura Sphere","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)        
#Mega Charizard X
class MCharizardX(Pokemon2):
    "Mega Charizard X"
    def __init__(self,name="Mega Charizard X",type1="Fire",type2="Dragon",nature=None,level=100,happiness=255,hp=78,atk=130,defense=111,spatk=130,spdef=85,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Tough Claws"):
        if move is None:
            avmoves=["Dragon Fance","Dragon Claw","Flare Blitz","Roost","Earthquake"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)      
#Mega Charizard Y
class MCharizardY(Pokemon2):
    "Mega Charizard Y"
    def __init__(self,name="Mega Charizard Y",type1="Fire",type2="Flying",nature=None,level=100,happiness=255,hp=78,atk=104,defense=78,spatk=169,spdef=115,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Drought"):
        if move is None:
            avmoves=["Hidden Power","Fire Blast","Solar Beam","Flamethrower","Earth Power","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)
#Meganium
class Meganium(Pokemon2):
    "Meganium"
    def __init__(self,name="Meganium",type1="Grass",type2="Fairy",nature=None,level=100,happiness=255,hp=80,atk=72,defense=100,spatk=93,spdef=100,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Thick Fat"):
        if move is None:
            avmoves=["Hidden Power","Leaf Storm","Moon Blast","Dazzling Gleam","Synthesis","Leech Seed"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)        
#Typhlosion
class Typhlosion(Pokemon2):
    "Typhlosion"
    def __init__(self,name="Typhlosion",type1="Fire",type2="Dark",nature=None,level=100,happiness=255,hp=78,atk=84,defense=78,spatk=109,spdef=85,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Flash Fire"):
        if move is None:
            avmoves=["Hidden Power","Earth Power","Fire Blast","Lava Plume","Eruption","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)        
#Feraligatr
class Feraligatr(Pokemon2):
    "Feraligatr"
    def __init__(self,name="Feraligatr",type1="Water",type2="Dragon",nature=None,level=100,happiness=255,hp=85,atk=105,defense=100,spatk=79,spdef=83,speed=78,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Sheer Force"):
        if move is None:
            avmoves=["Ice Beam","Hydro Pump","Liquidation","Dragon Claw","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)        
#Vaporeon
class Vaporeon(Pokemon2):
    "Vaporeon"
    def __init__(self,name="Vaporeon",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=130,atk=65,defense=60,spatk=110,spdef=95,speed=65,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=252,speedev=0,maxiv="No",move=None, ability="Water Absorb"):
        if move is None:
            avmoves=["Hidden Power","Ice Beam","Hydro Pump","Acid Armor","Surf","Rain Dance","Flip Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                   
#Jolteon
class Jolteon(Pokemon2):
    "Jolteon"
    def __init__(self,name="Jolteon",type1="Electric",type2=None,nature=None,level=100,happiness=255,hp=65,atk=65,defense=60,spatk=110,spdef=95,speed=130,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Volt Absorb"):
        if move is None:
            avmoves=["Hidden Power","Volt Switch","Thunder","Thunderbolt","Shadow Ball","Thunder Wave"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)         
               
#Flareon
class Flareon(Pokemon2):
    "Flareon"
    def __init__(self,name="Flareon",type1="Fire",type2=None,nature=None,level=100,happiness=255,hp=65,atk=130,defense=60,spatk=95,spdef=110,speed=65,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Flash Fire"):
        if move is None:
            avmoves=["Flare Blitz","Fire Blast","Flame Charge","Last Resort","Will-O-Wisp"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)  
#Crobat
class Crobat(Pokemon2):
    "Crobat"
    def __init__(self,name="Crobat",type1="Poison",type2="Flying",nature=None,level=100,happiness=255,hp=85,atk=90,defense=80,spatk=70,spdef=80,speed=130,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Infiltrator"):
        if move is None:
            avmoves=["Poison Jab","Cross Poison","Dual Wingbeat","Brave Bird","U-Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)              
#Lanturn
class Lanturn(Pokemon2):
    "Lanturn"
    def __init__(self,name="Lanturn",type1="Water",type2="Electric",nature=None,level=100,happiness=255,hp=125,atk=58,defense=58,spatk=76,spdef=76,speed=67,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Volt Absorb"):
        if move is None:
            avmoves=["Hidden Power","Ice Beam","Hydro Pump","Thunderbolt","Surf","Rain Dance","Flip Turn","Volt Switch","Thunder Wave"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)            
#Ampharos
class Ampharos(Pokemon2):
    "Amoharos"
    def __init__(self,name="Ampharos",type1="Electric",type2=None,nature=None,level=100,happiness=255,hp=90,atk=75,defense=85,spatk=115,spdef=90,speed=55,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=252,speedev=0,maxiv="No",move=None, ability="Static"):
        if move is None:
            avmoves=["Hidden Power","Signal Beam","Power Gem","Thunderbolt","Discharge","Thunder Wave","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)               
#Mega Ampharos
class MAmpharos(Pokemon2):
    "Mega Amoharos"
    def __init__(self,name="Mega Ampharos",type1="Electric",type2="Dragon",nature=None,level=100,happiness=255,hp=90,atk=95,defense=105,spatk=165,spdef=110,speed=45,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=252,speedev=0,maxiv="No",move=None, ability="Mold Breaker"):
        if move is None:
            avmoves=["Hidden Power","Signal Beam","Power Gem","Thunderbolt","Draco Meteor","Dragon Pulse","Thunder Wave","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)         
#Azumarill
class Azumarill(Pokemon2):
    "Azumarill"
    def __init__(self,name="Azumarill",type1="Water",type2="Fairy",nature=None,level=100,happiness=255,hp=100,atk=50,defense=80,spatk=60,spdef=80,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Huge Power"):
        if move is None:
            avmoves=["Hidden Power","Ice Beam","Aqua Jet","Play Rough","Liquidation"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)       
#Politoed
class Politoed(Pokemon2):
    "Politoed"
    def __init__(self,name="Politoed",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=90,atk=75,defense=75,spatk=90,spdef=100,speed=70,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability="Drizzle"):
        if move is None:
            avmoves=["Hidden Power","Ice Beam","Hydro Pump","Thunderbolt","Surf","Flip Turn","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)     
#Espeon
class Espeon(Pokemon2):
    "Espeon"
    def __init__(self,name="Espeon",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=65,atk=65,defense=60,spatk=130,spdef=95,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Magic Bounce"):
        if move is None:
            avmoves=["Hidden Power","Psychic","Shadow Ball","Dazzling Gleam","Recover"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)         
#Umbreon
class Umbreon(Pokemon2):
    "Umbreon"
    def __init__(self,name="Umbreon",type1="Dark",type2=None,nature=None,level=100,happiness=255,hp=95,atk=65,defense=110,spatk=60,spdef=130,speed=65,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability="Inner Focus"):
        if move is None:
            avmoves=["Hidden Power","Foul Play","Shadow Ball","Dark Pulse","Recover","Toxic"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)         
#Steelix
class Steelix(Pokemon2):
    "Steelix"
    def __init__(self,name="Steelix",type1="Steel",type2="Ground",nature=None,level=100,happiness=255,hp=75,atk=125,defense=230,spatk=55,spdef=95,speed=30,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Rock Head"):
        if move is None:
            avmoves=["Iron Tail","Gyro Ball","Earthquake","Stone Edge","Rock Slide","Toxic","Body Press"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)            
#Mega Steelix
class MSteelix(Pokemon2):
    "Mega Steelix"
    def __init__(self,name="Mega Steelix",type1="Steel",type2="Ground",nature=None,level=100,happiness=255,hp=75,atk=85,defense=200,spatk=55,spdef=65,speed=30,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Inner Focus"):
        if move is None:
            avmoves=["Iron Tail","Gyro Ball","Earthquake","Stone Edge","Rock Slide","Toxic","Body Press"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)       
#Scizor
class Scizor(Pokemon2):
    "Scizor"
    def __init__(self,name="Scizor",type1="Bug",type2="Steel",nature=None,level=100,happiness=255,hp=70,atk=130,defense=100,spatk=55,spdef=80,speed=65,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Technician"):
        if move is None:
            avmoves=["Iron Head","Bullet Punch","X-Scissor","U-Turn","Roost","Superpower"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)            
#Mega Scizor
class MScizor(Pokemon2):
    "Mega Scizor"
    def __init__(self,name="Mega Scizor",type1="Bug",type2="Steel",nature=None,level=100,happiness=255,hp=70,atk=150,defense=140,spatk=65,spdef=100,speed=75,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Technician"):
        if move is None:
            avmoves=["Iron Head","Bullet Punch","X-Scissor","U-Turn","Roost","Superpower"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                                   
#Heracross
class Heracross(Pokemon2):
    "Heracross"
    def __init__(self,name="Heracross",type1="Bug",type2="Fighting",nature=None,level=100,happiness=255,hp=80,atk=125,defense=75,spatk=40,spdef=95,speed=85,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Guts"):
        if move is None:
            avmoves=["Megahorn","Brick Break","X-Scissor","U-Turn","Close Combat","Superpower"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                                            #Mega Heracross
class MHeracross(Pokemon2):
    "Mega Heracross"
    def __init__(self,name="Mega Heracross",type1="Bug",type2="Fighting",nature=None,level=100,happiness=255,hp=80,atk=185,defense=115,spatk=40,spdef=105,speed=75,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Skill Link"):
        if move is None:
            avmoves=["Megahorn","Brick Break","X-Scissor","U-Turn","Close Combat","Superpower","Pin Missile"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)           
#Skarmory
class Skarmory(Pokemon2):
    "Skarmory"
    def __init__(self,name="Skarmory",type1="Steel",type2="Flying",nature=None,level=100,happiness=255,hp=65,atk=80,defense=140,spatk=40,spdef=70,speed=70,hpev=252,atkev=0,defev=252,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Sturdy"):
        if move is None:
            avmoves=["Roost","Brave Bird","Stealth Rock","Whirlwind","Steel Wing","Body Press"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                                            #Houndoom
class Houndoom(Pokemon2):
    "Houndoom"
    def __init__(self,name="Houndoom",type1="Dark",type2="Fire",nature=None,level=100,happiness=255,hp=75,atk=90,defense=50,spatk=110,spdef=80,speed=95,hpev=0,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=252,maxiv="No",move=None, ability="Flash Fire"):
        if move is None:
            avmoves=["Fire Blast","Dark Pulse","Flamethrower","Inferno","Crunch","Will-O-Wisp"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                                            #Mega Houndoom
class MHoundoom(Pokemon2):
    "Mega Houndoom"
    def __init__(self,name="Mega Houndoom",type1="Dark",type2="Fire",nature=None,level=100,happiness=255,hp=75,atk=90,defense=90,spatk=140,spdef=90,speed=115,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Solar Power"):
        if move is None:
            avmoves=["Fire Blast","Dark Pulse","Flamethrower","Inferno","Crunch"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)             
#Kingdra
class Kingdra(Pokemon2):
    "Kingdra"
    def __init__(self,name="Kingdra",type1="Water",type2="Dragon",nature=None,level=100,happiness=255,hp=75,atk=95,defense=95,spatk=95,spdef=95,speed=85,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Swift Swim"):
        if move is None:
            avmoves=["Dragon Pulse","Ice Beam","Surf","Thunder","Hydro Pump","Dragon Dance","Rain Dance","Flip Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                     
#Tyranitar
class Tyranitar(Pokemon2):
    "Tyranitar"
    def __init__(self,name="Tyranitar",type1="Rock",type2="Dark",nature=None,level=100,happiness=255,hp=100,atk=134,defense=110,spatk=95,spdef=100,speed=61,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Sand Stream"):
        if move is None:
            avmoves=["Crunch","Earthquake","Stone Edge","Rock Slide","Hyper Beam","Dragon Dance"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability) 
#Mega Tyranitar
class MTyranitar(Pokemon2):
    "Mega Tyranitar"
    def __init__(self,name="Mega Tyranitar",type1="Rock",type2="Dark",nature=None,level=100,happiness=255,hp=100,atk=164,defense=150,spatk=95,spdef=120,speed=71,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Sand Stream"):
        if move is None:
            avmoves=["Crunch","Earthquake","Stone Edge","Rock Slide","Hyper Beam","Dragon Dance"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)             
#Raikou
class Raikou(Pokemon2):
    "Raikou"
    def __init__(self,name="Raikou",type1="Electric",type2=None,nature=None,level=100,happiness=255,hp=90,atk=85,defense=75,spatk=115,spdef=100,speed=115,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Inner Focus"):
        if move is None:
            avmoves=["Crunch","Thunder","Thunderbolt","Wild Charge","Hyper Beam","Rain Dance","Thunder Wave"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)        
#Entei
class Entei(Pokemon2):
    "Entei"
    def __init__(self,name="Entei",type1="Fire",type2=None,nature=None,level=100,happiness=255,hp=115,atk=115,defense=85,spatk=90,spdef=75,speed=100,hpev=0,atkev=115,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Inner Focus"):
        if move is None:
            avmoves=["Crunch","Fire Blast","Stone Edge","Flamethrower","Hyper Beam","Flare Blitz","Eruption"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)          
#Suicune
class Suicune(Pokemon2):
    "Suicune"
    def __init__(self,name="Suicune",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=100,atk=75,defense=115,spatk=90,spdef=115,speed=85,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Inner Focus"):
        if move is None:
            avmoves=["Crunch","Surf","Hydro Pump","Recover","Hyper Beam","Rain Dance"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)         
#Lugia
class Lugia(Pokemon2):
    "Lugia"
    def __init__(self,name="Lugia",type1="Psychic",type2="Flying",nature=None,level=100,happiness=255,hp=106,atk=90,defense=130,spatk=90,spdef=154,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Multiscale"):
        if move is None:
            avmoves=["Crunch","Surf","Hydro Pump","Recover","Hyper Beam","Rain Dance","Aeroblast","Psychic","Extrasensory"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)            
#Ho-Oh
class Hooh(Pokemon2):
    "Ho-Oh"
    def __init__(self,name="Ho-Oh",type1="Fire",type2="Flying",nature=None,level=100,happiness=255,hp=106,atk=130,defense=90,spatk=110,spdef=154,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Regenerator"):
        if move is None:
            avmoves=["Recover","Hyper Beam","Sunny Day","Sacred Fire","Fire Blast","Flamethrower","Brave Bird","Heat Wave","Sky Attack"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                     
#Celebi
class Celebi(Pokemon2):
    "Celebi"
    def __init__(self,name="Celebi",type1="Grass",type2="Psychic",nature=None,level=100,happiness=255,hp=100,atk=100,defense=100,spatk=100,spdef=100,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Natural Cure"):
        if move is None:
            avmoves=["Recover","Psychic","Leaf Storm","Future Sight","Perish Song","Shadow Ball"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)           
#Blissey
class Blissey(Pokemon2):
    "Blissey"
    def __init__(self,name="Blissey",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=255,atk=10,defense=10,spatk=75,spdef=135,speed=55,hpev=252,atkev=0,defev=252,spatkev=0,spdefev=4,speedev=0,maxiv="No",move=None, ability="Natural Cure"):
        if move is None:
            avmoves=["Soft Boiled","Toxic","Seismic Toss","Light Screen","Reflect"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)  
#Deoxys
class Deoxys(Pokemon2):
    "Deoxys"
    def __init__(self,name="Deoxys",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=50,atk=150,defense=50,spatk=150,spdef=50,speed=150,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Pressure"):
        if move is None:
            avmoves=["Psycho Boost","Toxic","Psychic","Shadow Ball","Dark Pulse"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)    
#Attack Deoxys
class ADeoxys(Pokemon2):
    "Attack Deoxys"
    def __init__(self,name="Attack Deoxys",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=50,atk=180,defense=20,spatk=180,spdef=20,speed=150,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Pressure"):
        if move is None:
            avmoves=["Psycho Boost","Psychic","Shadow Ball","Dark Pulse"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)    
#Speed Deoxys
class SDeoxys(Pokemon2):
    "Speed Deoxys"
    def __init__(self,name="Speed Deoxys",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=50,atk=95,defense=90,spatk=95,spdef=90,speed=180,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Pressure"):
        if move is None:
            avmoves=["Psycho Boost","Toxic","Psychic","Shadow Ball","Dark Pulse","Recover","Thunder Wave"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)   
#Defense Deoxys
class DDeoxys(Pokemon2):
    "Defense Deoxys"
    def __init__(self,name="Defense Deoxys",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=50,atk=70,defense=160,spatk=70,spdef=160,speed=90,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=4,maxiv="No",move=None, ability="Pressure"):
        if move is None:
            avmoves=["Psycho Boost","Toxic","Psychic","Shadow Ball","Dark Pulse","Recover","Thunder Wave"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                                            #Jirachi       
class Jirachi(Pokemon2):
    "Jirachi"
    def __init__(self,name="Jirachi",type1="Steel",type2="Psychic",nature=None,level=100,happiness=255,hp=100,atk=100,defense=100,spatk=100,spdef=100,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Serene Grace"):
        if move is None:
            avmoves=["Recover","Psychic","Doom Desire","Future Sight","Flash Cannon","Shadow Ball","Rest"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability) 
#Rayquaza     
class Rayquaza(Pokemon2):
    "Rayquaza"
    def __init__(self,name="Rayquaza",type1="Dragon",type2="Flying",nature=None,level=100,happiness=255,hp=105,atk=150,defense=90,spatk=150,spdef=90,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Air Lock"):
        if move is None:
            avmoves=["Crunch","Hyper Beam","Dragon Ascent","Dragon Dance","Extreme Speed","Draco Meteor"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)   
#Mega Rayquaza     
class MRayquaza(Pokemon2):
    "Mega Rayquaza"
    def __init__(self,name="Mega Rayquaza",type1="Dragon",type2="Flying",nature=None,level=100,happiness=255,hp=105,atk=180,defense=100,spatk=180,spdef=100,speed=115,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Delta Stream"):
        if move is None:
            avmoves=["Crunch","Hyper Beam","Dragon Ascent","Dragon Dance","Extreme Speed","Draco Meteor"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)           
#Sceptile
class Sceptile(Pokemon2):
    "Sceptile"
    def __init__(self,name="Sceptile",type1="Grass",type2=None,nature=None,level=100,happiness=255,hp=70,atk=85,defense=65,spatk=105,spdef=86,speed=120,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Overgrow"):
        if move is None:
            avmoves=["Leaf Blade","Hyper Beam","Leaf Storm","Dragon Dance","Dragon Pulse","Draco Meteor","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)     
#Mega Sceptile
class MSceptile(Pokemon2):
    "Mega Sceptile"
    def __init__(self,name="Mega Sceptile",type1="Grass",type2="Dragon",nature=None,level=100,happiness=255,hp=70,atk=110,defense=75,spatk=155,spdef=85,speed=145,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Lightning Rod"):
        if move is None:
            avmoves=["Hyper Beam","Leaf Storm","Dragon Dance","Dragon Pulse","Draco Meteor","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)           
#Blaziken
class Blaziken(Pokemon2):
    "Blaziken"
    def __init__(self,name="Blaziken",type1="Fire",type2="Fighting",nature=None,level=100,happiness=255,hp=80,atk=120,defense=70,spatk=110,spdef=70,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Speed Boost"):
        if move is None:
            avmoves=["Overheat","High Jump Kick","Sky Uppercut","Blaze Kick","Brave Bird","Flare Blitz","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)            
#Mega Blaziken
class MBlaziken(Pokemon2):
    "Mega Blaziken"
    def __init__(self,name="Mega Blaziken",type1="Fire",type2="Fighting",nature=None,level=100,happiness=255,hp=80,atk=160,defense=80,spatk=130,spdef=80,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Speed Boost"):
        if move is None:
            avmoves=["Overheat","High Jump Kick","Sky Uppercut","Blaze Kick","Brave Bird","Flare Blitz","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                                     
#Swampert
class Swampert(Pokemon2):
    "Swampert"
    def __init__(self,name="Swampert",type1="Water",type2="Ground",nature=None,level=100,happiness=255,hp=100,atk=110,defense=90,spatk=85,spdef=90,speed=60,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Torrent"):
        if move is None:
            avmoves=["Liquidation","Earthquake","Stone Edge","Power-up Punch","Waterfall","Ice Punch","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                                            #Mega Swampert
class MSwampert(Pokemon2):
    "Mega Swampert"
    def __init__(self,name="Mega Swampert",type1="Water",type2="Ground",nature=None,level=100,happiness=255,hp=100,atk=150,defense=110,spatk=95,spdef=110,speed=70,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Swift Swim"):
        if move is None:
            avmoves=["Liquidation","Earthquake","Stone Edge","Power-up Punch","Waterfall","Ice Punch","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                               
#Ludicolo
class Ludicolo(Pokemon2):
    "Ludicolo"
    def __init__(self,name="Ludicolo",type1="Grass",type2="Water",nature=None,level=100,happiness=255,hp=80,atk=70,defense=70,spatk=90,spdef=100,speed=70,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Swift Swim"):
        if move is None:
            avmoves=["Ice Beam","Giga Drain","Surf","Hydro Pump","Rain Dance","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                                            #Shiftry
class Shiftry(Pokemon2):
    "Shiftry"
    def __init__(self,name="Shiftry",type1="Grass",type2="Dark",nature=None,level=100,happiness=255,hp=90,atk=100,defense=60,spatk=90,spdef=60,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Chlorophyll"):
        if move is None:
            avmoves=["Sunny Day","Giga Drain","Leaf Storm","Hurricane","Leaf Tornado","Leech Seed","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                                            #Swellow
class Swellow(Pokemon2):
    "Swellow"
    def __init__(self,name="Swellow",type1="Normal",type2="Flying",nature=None,level=100,happiness=255,hp=60,atk=85,defense=60,spatk=75,spdef=50,speed=125,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Guts"):
        if move is None:
            avmoves=["Roost","Brave Bird","Facade","Hurricane","Boomburst"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)   
#Pelipper
class Pelipper(Pokemon2):
    "Pelipper"
    def __init__(self,name="Pelipper",type1="Water",type2="Flying",nature=None,level=100,happiness=255,hp=60,atk=50,defense=100,spatk=95,spdef=70,speed=65,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Drizzle"):
        if move is None:
            avmoves=["Roost","Surf","Ice Beam","Hurricane","Hydro Pump"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)           
#Gardevoir
class Gardevoir(Pokemon2):
    "Gardevoir"
    def __init__(self,name="Gardevoir",type1="Psychic",type2="Fairy",nature=None,level=100,happiness=255,hp=68,atk=65,defense=65,spatk=125,spdef=115,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Trace"):
        if move is None:
            avmoves=["Recover","Dazzling Gleam","Moon Blast","Psychic","Shadow Ball","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)     
#Mega Gardevoir
class MGardevoir(Pokemon2):
    "Mega Gardevoir"
    def __init__(self,name="Mega Gardevoir",type1="Psychic",type2="Fairy",nature=None,level=100,happiness=255,hp=68,atk=85,defense=65,spatk=165,spdef=135,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Pixilate"):
        if move is None:
            avmoves=["Recover","Dazzling Gleam","Moon Blast","Psychic","Shadow Ball","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)               
#Breloom
class Breloom(Pokemon2):
    "Breloom"
    def __init__(self,name="Breloom",type1="Grass",type2="Fighting",nature=None,level=100,happiness=255,hp=60,atk=130,defense=80,spatk=60,spdef=60,speed=70,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Poison Heal"):
        if move is None:
            avmoves=["Dynamic Punch","Mach Punch","Spore","Sky Uppercut","Bullet Seed","Seed Bomb","Leech Seed"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)            
#Slaking
class Slaking(Pokemon2):
    "Slaking"
    def __init__(self,name="Slaking",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=150,atk=160,defense=100,spatk=95,spdef=65,speed=10,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Lazy"):
        if move is None:
            avmoves=["Dynamic Punch","Hyper Beam","Double Edge","Sky Uppercut","Return","Slack Off","Rest"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)         
#Hariyama
class Hariyama(Pokemon2):
    "Hariyama"
    def __init__(self,name="Hariyama",type1="Fighting",type2=None,nature=None,level=100,happiness=255,hp=144,atk=120,defense=60,spatk=40,spdef=60,speed=50,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Guts"):
        if move is None:
            avmoves=["Dynamic Punch","Force Palm","Sky Uppercut","Arm Thrust","Belly Drum","Knock Off"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)   
#Mega Sableye
class MSableye(Pokemon2):
    "Mega Sableye"
    def __init__(self,name="Mega Sableye",type1="Dark",type2="Ghost",nature=None,level=100,happiness=255,hp=50,atk=85,defense=125,spatk=85,spdef=115,speed=20,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability="Magic Bounce"):
        if move is None:
            avmoves=["Night Shade","Shadow Sneak","Power Gem","Zen Headbutt","Recover","Knock Off","Foul Play"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)            
#Mega Mawile
class MMawile(Pokemon2):
    "Mega Mawile"
    def __init__(self,name="Mega Mawile",type1="Steel",type2="Fairy",nature=None,level=100,happiness=255,hp=50,atk=105,defense=125,spatk=55,spdef=95,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Huge Power"):
        if move is None:
            avmoves=["Iron Head","Play Rough","Crunch","Sucker Punch","Iron Defense"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)        
#Aggron
class Aggron(Pokemon2):
    "Aggron"
    def __init__(self,name="Aggron",type1="Steel",type2="Rock",nature=None,level=100,happiness=255,hp=70,atk=110,defense=180,spatk=60,spdef=60,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Rock Head"):
        if move is None:
            avmoves=["Iron Head","Stone Edge","Crunch","Earthquake","Iron Defense","Hyper Beam","Flash Cannon","Body Press"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)    
#Mega Aggron
class MAggron(Pokemon2):
    "Mega Aggron"
    def __init__(self,name="Mega Aggron",type1="Steel",type2=None,nature=None,level=100,happiness=255,hp=70,atk=140,defense=230,spatk=60,spdef=80,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Filter"):
        if move is None:
            avmoves=["Iron Head","Stone Edge","Crunch","Earthquake","Iron Defense","Hyper Beam","Flash Cannon","Heavy Slam","Body Press"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                                            #Mega Medicham
class MMedicham (Pokemon2):
    "Mega Medicham"
    def __init__(self,name="Mega Medicham",type1="Fighting",type2="Psychic",nature=None,level=100,happiness=255,hp=60,atk=100,defense=85,spatk=80,spdef=85,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Pure Power"):
        if move is None:
            avmoves=["Dynamic Punch","Thunder Punch","Psycho Cut","Fire Punch","Zen Headbutt","Ice Punch"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)       
#Mega Manectric
class MManectric(Pokemon2):
    "Mega Manectric"
    def __init__(self,name="Mega Manectric",type1="Electric",type2=None,nature=None,level=100,happiness=255,hp=70,atk=75,defense=80,spatk=135,spdef=80,speed=135,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Intimidate"):
        if move is None:
            avmoves=["Volt Switch","Thunder","Crunch","Thunderbolt","Wild Charge","Hyper Beam","Thunder Wave"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)         
#Sharpedo
class Sharpedo(Pokemon2):
    "Sharpedo"
    def __init__(self,name="Sharpedo",type1="Water",type2="Dark",nature=None,level=100,happiness=255,hp=70,atk=120,defense=40,spatk=95,spdef=40,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Speed Boost"):
        if move is None:
            avmoves=["Flip Turn","Hydro Pump","Crunch","Ice Beam","Surf","Dark Pulse"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)              
#Overqwil
class Overqwil(Pokemon2):
    "Overqwil"
    def __init__(self,name="Overqwil",type1="Dark",type2="Poison",nature=None,level=100,happiness=255,hp=85,atk=115,defense=95,spatk=65,spdef=65,speed=85,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Intimidate"):
        if move is None:
            avmoves=["Flip Turn","Pin Missile","Crunch","Poison Jab","Barb Barrage","Dark Pulse","Double Edge"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)        
#Mega Sharpedo
class MSharpedo(Pokemon2):
    "Mega Sharpedo"
    def __init__(self,name="Mega Sharpedo",type1="Water",type2="Dark",nature=None,level=100,happiness=255,hp=70,atk=140,defense=70,spatk=110,spdef=65,speed=105,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Strong Jaw"):
        if move is None:
            avmoves=["Flip Turn","Thunder Fang","Crunch","Liquidation","Surf","Ice Fang","Poison Fang"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)           
#Wailord
class Wailord(Pokemon2):
    "Wailord"
    def __init__(self,name="Wailord",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=170,atk=90,defense=80,spatk=105,spdef=80,speed=50,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Blubber Defense"):
        if move is None:
            avmoves=["Water Spout","Hydro Pump","Blizzard","Ice Beam","Surf","Rain Dance","Heavy Slam","Rest"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                
#Mega Camerupt
class MCamerupt(Pokemon2):
    "Mega Camerupt"
    def __init__(self,name="Mega Camerupt",type1="Fire",type2="Ground",nature=None,level=100,happiness=255,hp=70,atk=120,defense=100,spatk=145,spdef=105,speed=20,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Sheer Force"):
        if move is None:
            avmoves=["Eruption","Earth Power","Lava Plume","Earthquake","Stone Edge","Fire Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability) 
#Camerupt
class Camerupt(Pokemon2):
    "Camerupt"
    def __init__(self,name="Camerupt",type1="Fire",type2="Ground",nature=None,level=100,happiness=255,hp=70,atk=100,defense=70,spatk=105,spdef=75,speed=40,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Solid Rock"):
        if move is None:
            avmoves=["Eruption","Earth Power","Lava Plume","Earthquake","Stone Edge","Fire Blast","Will-O-Wisp"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)
#Arbok
class Arbok(Pokemon2):
    "Arbok"
    def __init__(self,name="Arbok",type1="Poison",type2="Dark",nature=None,level=100,happiness=255,hp=60,atk=85,defense=69,spatk=65,spdef=79,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Intimidate"):
        if move is None:
            avmoves=["Venoshock","Earth Power","Poison Fang","Crunch","Gunk Shot","Blech"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                                            #Regirock
class Regirock(Pokemon2):
    "Regirock"
    def __init__(self,name="Regirock",type1="Rock",type2=None,nature=None,level=100,happiness=255,hp=80,atk=100,defense=200,spatk=50,spdef=100,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Clear Body"):
        if move is None:
            avmoves=["Zap Cannon","Earth Power","Hyper Beam","Earthquake","Stone Edge","Rock Slide"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)      
#Regice
class Regice(Pokemon2):
    "Regice"
    def __init__(self,name="Regice",type1="Ice",type2=None,nature=None,level=100,happiness=255,hp=80,atk=50,defense=100,spatk=100,spdef=200,speed=50,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Clear Body"):
        if move is None:
            avmoves=["Ice Beam","Blizzard","Freeze Dry","Hyper Beam","Zap Cannon","Hail"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)
#Registeel
class Registeel(Pokemon2):
    "Registeel"
    def __init__(self,name="Registeel",type1="Steel",type2=None,nature=None,level=100,happiness=255,hp=80,atk=75,defense=150,spatk=75,spdef=150,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Clear Body"):
        if move is None:
            avmoves=["Iron Head","Flash Cannon","Zap Cannon","Earthquake","Hyper Beam","Curse"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)   
#Dewgong
class Dewgong(Pokemon2):
    "Dewgong"
    def __init__(self,name="Dewgong",type1="Water",type2="Ice",nature=None,level=100,happiness=255,hp=90,atk=50,defense=80,spatk=90,spdef=95,speed=70,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Thick Fat"):
        if move is None:
            avmoves=["Hidden Power","Ice Beam","Hydro Pump","Thunderbolt","Surf","Hail","Rain Dance","Frost Breath"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)       
#Jynx
class Jynx(Pokemon2):
    "Jynx"
    def __init__(self,name="Jynx",type1="Ice",type2="Psychic",nature=None,level=100,happiness=255,hp=65,atk=50,defense=50,spatk=115,spdef=95,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Dry Skin"):
        if move is None:
            avmoves=["Hidden Power","Ice Beam","Psychic","Blizzard","Dark Pulse","Hail","Shadow Ball"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)           
#Mamoswine
class Mamoswine(Pokemon2):
    "Mamoswine"
    def __init__(self,name="Mamoswine",type1="Ice",type2="Ground",nature=None,level=100,happiness=255,hp=110,atk=130,defense=80,spatk=70,spdef=60,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Thick Fat"):
        if move is None:
            avmoves=["Ice Beam","Earthquake","Blizzard","Stone Edge","Hail","Icicle Crash"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)       
#Flygon
class Flygon(Pokemon2):
    "Flygon"
    def __init__(self,name="Flygon",type1="Ground",type2="Dragon",nature=None,level=100,happiness=255,hp=100,atk=100,defense=80,spatk=100,spdef=80,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Tinted Lens"):
        if move is None:
            avmoves=["Dragon Claw","Earthquake","Crunch","Stone Edge","Superpower","Sandstorm"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)   
#Altaria
class Altaria(Pokemon2):
    "Altaria"
    def __init__(self,name="Altaria",type1="Dragon",type2="Flying",nature=None,level=100,happiness=255,hp=85,atk=70,defense=90,spatk=70,spdef=105,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Natural Cure"):
        if move is None:
            avmoves=["Dragon Claw","Earthquake","Crunch","Brave Bird","Sky Attack","Moon Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)           
#Mega Altaria
class MAltaria(Pokemon2):
    "Mega Altaria"
    def __init__(self,name="Mega Altaria",type1="Dragon",type2="Fairy",nature=None,level=100,happiness=255,hp=85,atk=110,defense=110,spatk=110,spdef=105,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Pixilate"):
        if move is None:
            avmoves=["Dragon Claw","Earthquake","Crunch","Brave Bird","Sky Attack","Moon Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                        
#Zangoose
class Zangoose(Pokemon2):
    "Zangoose"
    def __init__(self,name="Zangoose",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=73,atk=115,defense=70,spatk=60,spdef=70,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Toxic Boost"):
        if move is None:
            avmoves=["Clush Claw","Slash","Crunch","X-Scissor","Facade","Close Combat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)          
#Seviper
class Seviper(Pokemon2):
    "Seviper"
    def __init__(self,name="Seviper",type1="Poison",type2=None,nature=None,level=100,happiness=255,hp=83,atk=100,defense=83,spatk=100,spdef=83,speed=85,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Shed Skin"):
        if move is None:
            avmoves=["Poison Fang","Poison Tail","Crunch","Poison Jab","Toxic","Sludge Bomb"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)      
#Exploud
class Exploud(Pokemon2):
    "Exploud"
    def __init__(self,name="Exploud",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=104,atk=81,defense=63,spatk=91,spdef=73,speed=73,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=252,speedev=0,maxiv="No",move=None, ability="Scrappy"):
        if move is None:
            avmoves=["Boomburst","Hyper Beam","Crunch","Hyper Voice","Toxic","Double Edge","Rest"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                                            #Lunatone
class Lunatone(Pokemon2):
    "Lunatone"
    def __init__(self,name="Lunatone",type1="Rock",type2="Psychic",nature=None,level=100,happiness=255,hp=70,atk=55,defense=65,spatk=105,spdef=85,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Levitate"):
        if move is None:
            avmoves=["Ancient Power","Hyper Beam","Psychic","Power Gem","Moon Blast","Stone Edge"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)            
#Solrock
class Solrock(Pokemon2):
    "Solrock"
    def __init__(self,name="Solrock",type1="Rock",type2="Psychic",nature=None,level=100,happiness=255,hp=70,atk=105,defense=85,spatk=55,spdef=65,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Levitate"):
        if move is None:
            avmoves=["Ancient Power","Hyper Beam","Psychic","Power Gem","Moon Blast","Stone Edge"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)              
#Whiscash
class Whiscash(Pokemon2):
    "Whiscash"
    def __init__(self,name="Whiscash",type1="Water",type2="Ground",nature=None,level=100,happiness=255,hp=110,atk=78,defense=73,spatk=76,spdef=71,speed=60,hpev=0,atkev=252,defev=252,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Oblivious"):
        if move is None:
            avmoves=["Ancient Power","Ice Beam","Surf","Power Gem","Hydro Pump","Stone Edge","Earthquake","Rest"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability) 
#Crawdaunt
class Crawdaunt(Pokemon2):
    "Crawdaunt"
    def __init__(self,name="Crawdaunt",type1="Water",type2="Dark",nature=None,level=100,happiness=255,hp=63,atk=120,defense=85,spatk=90,spdef=55,speed=55,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Adaptability"):
        if move is None:
            avmoves=["Ancient Power","Ice Beam","Surf","Power Gem","Hydro Pump","Crabhammer","Liquidation"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)               
#Claydol
class Claydol(Pokemon2):
    "Claydol"
    def __init__(self,name="Claydol",type1="Ground",type2="Psychic",nature=None,level=100,happiness=255,hp=60,atk=70,defense=105,spatk=80,spdef=120,speed=75,hpev=0,atkev=0,defev=252,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Levitate"):
        if move is None:
            avmoves=["Ancient Power","Hyper Beam","Psychic","Power Gem","Earth Power","Stone Edge"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)    
#Cradily
class Cradily(Pokemon2):
    "Cradily"
    def __init__(self,name="Cradily",type1="Rock",type2="Grass",nature=None,level=100,happiness=255,hp=86,atk=81,defense=97,spatk=81,spdef=107,speed=43,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Storm Drain"):
        if move is None:
            avmoves=["Ancient Power","Hyper Beam","Giga Drain","Sludge Bomb","Earth Power","Leech Seed"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)         
#Armaldo
class Armaldo(Pokemon2):
    "Armaldo"
    def __init__(self,name="Armaldo",type1="Rock",type2="Bug",nature=None,level=100,happiness=255,hp=75,atk=125,defense=100,spatk=70,spdef=80,speed=45,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Swift Swim"):
        if move is None:
            avmoves=["Ancient Power","Hyper Beam","X-Scissor","Rock Blast","Earth Power","Crush Claw"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)          
#Milotic
class Milotic(Pokemon2):
    "Milotic"
    def __init__(self,name="Milotic",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=95,atk=60,defense=84,spatk=100,spdef=125,speed=86,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Competitive"):
        if move is None:
            avmoves=["Recover","Ice Beam","Surf","Rain Dance","Hydro Pump","Coil","Thunderbolt"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)            
#Farigarif
class Farigarif(Pokemon2):
    "Farigarif"
    def __init__(self,name="Farigarif",type1="Normal",type2="Psychic",nature=None,level=100,happiness=255,hp=80,atk=90,defense=74,spatk=120,spdef=75,speed=85,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Armor Tail"):
        if move is None:
            avmoves=["Recover","Psychic","Crunch","Zen Headbutt","Assurance","Hypnosis","Shadow Ball"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)    
#Banette
class Banette(Pokemon2):
    "Banette"
    def __init__(self,name="Banette",type1="Ghost",type2=None,nature=None,level=100,happiness=255,hp=64,atk=115,defense=65,spatk=73,spdef=63,speed=65,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Insomnia"):
        if move is None:
            avmoves=["Recover","Knock Off","Crunch","Pantom Force","Assurance","Hypnosis","Shadow Ball","Will-O-Wisp"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)          
#Mega Banette
class MBanette(Pokemon2):
    "Mega Banette"
    def __init__(self,name="Mega Banette",type1="Ghost",type2=None,nature=None,level=100,happiness=255,hp=64,atk=165,defense=75,spatk=93,spdef=83,speed=75,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Prankster"):
        if move is None:
            avmoves=["Recover","Knock Off","Crunch","Pantom Force","Assurance","Hypnosis","Shadow Ball","Toxic","Thunder Wave","Will-O-Wisp"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)     
#Absol
class Absol(Pokemon2):
    "Absol"
    def __init__(self,name="Absol",type1="Dark",type2=None,nature=None,level=100,happiness=255,hp=75,atk=130,defense=70,spatk=85,spdef=70,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Super Luck"):
        if move is None:
            avmoves=["Recover","Knock Off","Crunch","Psycho Cut","Assurance","Night Slash","Shadow Ball","Toxic","Sucker Punch","Close Combat","Swords Dance"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)         
#Mega Absol
class MAbsol(Pokemon2):
    "Mega Absol"
    def __init__(self,name="Mega Absol",type1="Dark",type2=None,nature=None,level=100,happiness=255,hp=75,atk=150,defense=70,spatk=115,spdef=70,speed=125,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Magic Bounce"):
        if move is None:
            avmoves=["Recover","Knock Off","Crunch","Psycho Cut","Assurance","Night Slash","Shadow Ball","Toxic","Sucker Punch","Close Combat","Swords Dance"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)             
#Mega Glalie
class MGlalie(Pokemon2):
    "Mega Glalie"
    def __init__(self,name="Mega Glalie",type1="Ice",type2=None,nature=None,level=100,happiness=255,hp=80,atk=120,defense=80,spatk=120,spdef=80,speed=120,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Refrigerate"):
        if move is None:
            avmoves=["Recover","Earthquake","Crunch","Ice Beam","Blizzard","Freeze Dry","Ice Fang","Toxic","Hail","Hyper Beam","Rain Dance","Shadow Ball"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)        
                                    
#Glalie
class Glalie(Pokemon2):
    "Glalie"
    def __init__(self,name="Glalie",type1="Ice",type2=None,nature=None,level=100,happiness=255,hp=80,atk=80,defense=80,spatk=100,spdef=80,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Refrigerate"):
        if move is None:
            avmoves=["Recover","Earthquake","Crunch","Ice Beam","Blizzard","Freeze Dry","Ice Fang","Toxic","Hail","Hyper Beam","Rain Dance","Shadow Ball"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                                            #Walrein
class Walrein(Pokemon2):
    "Walrein"
    def __init__(self,name="Walrein",type1="Ice",type2="Water",nature=None,level=100,happiness=255,hp=110,atk=80,defense=90,spatk=95,spdef=90,speed=65,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Thick Fat"):
        if move is None:
            avmoves=["Slack Off","Surf","Crunch","Ice Beam","Blizzard","Freeze Dry","Ice Fang","Rest","Hail","Hyper Beam","Rain Dance","Liquidation","Iron Head"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)         
#Huntail
class Huntail(Pokemon2):
    "Huntail"
    def __init__(self,name="Huntail",type1="Water",type2="Dark",nature=None,level=100,happiness=255,hp=55,atk=104,defense=105,spatk=94,spdef=75,speed=52,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Intimidate"):
        if move is None:
            avmoves=["Crunch","Ice Beam","Blizzard","Liquidation","Ice Fang","Waterfall","Hydro Pump","Rain Dance","Shell Smash"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)       
#Gorebyss
class Gorebyss(Pokemon2):
    "Gorebyss"
    def __init__(self,name="Gorebyss",type1="Water",type2="Fairy",nature=None,level=100,happiness=255,hp=55,atk=84,defense=105,spatk=114,spdef=75,speed=52,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Regenerator"):
        if move is None:
            avmoves=["Dazzling Gleam","Ice Beam","Blizzard","Moon Blast","Ice Fang","Waterfall","Hydro Pump","Rain Dance","Shell Smash"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)            
#Relicanth
class Relicanth(Pokemon2):
    "Relicanth"
    def __init__(self,name="Relicanth",type1="Water",type2="Rock",nature=None,level=100,happiness=255,hp=100,atk=105,defense=130,spatk=45,spdef=65,speed=55,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Rock Head"):
        if move is None:
            avmoves=["Liquidation","Ice Beam","Stone Edge","Rock Slide","Ice Fang","Waterfall","Hydro Pump","Rain Dance","Head Smash"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                                            #Salamence
class Salamence(Pokemon2):
    "Salamence"
    def __init__(self,name="Salamence",type1="Dragon",type2="Flying",nature=None,level=100,happiness=255,hp=95,atk=135,defense=80,spatk=110,spdef=80,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Intimidate"):
        if move is None:
            avmoves=["Stone Edge","Dragon Claw","Ice Beam","Flamethrower","Crunch","Zen Headbutt","Double Edge","Hydro Pump","Earthquake","Dragon Dance","Roost"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)      
#Mega Salamence
class MSalamence(Pokemon2):
    "Mega Salamence"
    def __init__(self,name="Mega Salamence",type1="Dragon",type2="Flying",nature=None,level=100,happiness=255,hp=95,atk=145,defense=130,spatk=120,spdef=90,speed=120,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Aerilate"):
        if move is None:
            avmoves=["Stone Edge","Dragon Claw","Ice Beam","Flamethrower","Crunch","Zen Headbutt","Double Edge","Hydro Pump","Earthquake","Dragon Dance","Roost"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                                            #Metagross
class Metagross(Pokemon2):
    "Metagross"
    def __init__(self,name="Metagross",type1="Steel",type2="Psychic",nature=None,level=100,happiness=255,hp=80,atk=135,defense=130,spatk=95,spdef=90,speed=70,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Clear Body"):
        if move is None:
            avmoves=["Stone Edge","Bullet Punch","Meteor Mash","Hyper Beam","Crunch","Zen Headbutt","Double Edge","Iron Defense","Earthquake","Hammer Arm","Flash Cannon"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                    
#MegaMetagross
class MMetagross(Pokemon2):
    "Mega Metagross"
    def __init__(self,name="Mega Metagross",type1="Steel",type2="Psychic",nature=None,level=100,happiness=255,hp=80,atk=145,defense=150,spatk=105,spdef=110,speed=110,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Tough Claws"):
        if move is None:
            avmoves=["Stone Edge","Bullet Punch","Meteor Mash","Hyper Beam","Crunch","Zen Headbutt","Double Edge","Iron Defense","Earthquake","Hammer Arm","Flash Cannon","Fire Punch"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                                            #Latias
class Latias(Pokemon2):
    "Latias"
    def __init__(self,name="Latias",type1="Dragon",type2="Psychic",nature=None,level=100,happiness=255,hp=80,atk=80,defense=90,spatk=110,spdef=130,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Levitate"):
        if move is None:
            avmoves=["Hyper Beam","Mist Ball","Zen Headbutt","Dragon Pulse","Psychic","Calm Mind","Ice Beam","Thunderbolt","Shadow Ball"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)           
#Latios
class Latios(Pokemon2):
    "Latios"
    def __init__(self,name="Latios",type1="Dragon",type2="Psychic",nature=None,level=100,happiness=255,hp=80,atk=90,defense=80,spatk=130,spdef=110,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Levitate"):
        if move is None:
            avmoves=["Hyper Beam","Luster Purge","Zen Headbutt","Dragon Pulse","Psychic","Calm Mind","Ice Beam","Thunderbolt","Shadow Ball"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)        
#Mega Latias
class MLatias(Pokemon2):
    "Mega Latias"
    def __init__(self,name="Mega Latias",type1="Dragon",type2="Psychic",nature=None,level=100,happiness=255,hp=80,atk=100,defense=120,spatk=140,spdef=150,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Levitate"):
        if move is None:
            avmoves=["Hyper Beam","Mist Ball","Zen Headbutt","Dragon Pulse","Psychic","Calm Mind","Ice Beam","Thunderbolt","Shadow Ball"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)        
#Mega Latios
class MLatios(Pokemon2):
    "Mega Latios"
    def __init__(self,name="Mega Latios",type1="Dragon",type2="Psychic",nature=None,level=100,happiness=255,hp=80,atk=130,defense=100,spatk=160,spdef=120,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Levitate"):
        if move is None:
            avmoves=["Hyper Beam","Luster Purge","Zen Headbutt","Dragon Pulse","Psychic","Calm Mind","Ice Beam","Thunderbolt","Shadow Ball"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                
#Kyogre
class Kyogre(Pokemon2):
    "Kyogre"
    def __init__(self,name="Kyogre",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=100,atk=100,defense=90,spatk=150,spdef=140,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Drizzle"):
        if move is None:
            avmoves=["Hyper Beam","Origin Pulse","Thunder","Water Spout","Ancient Power","Calm Mind","Ice Beam","Thunderbolt","Rest","Thunder Wave"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                   
#Primal Kyogre
class PKyogre(Pokemon2):
    "Primal Kyogre"
    def __init__(self,name="Primal Kyogre",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=100,atk=150,defense=90,spatk=180,spdef=160,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Primordial Sea"):
        if move is None:
            avmoves=["Hyper Beam","Origin Pulse","Thunder","Water Spout","Ancient Power","Calm Mind","Ice Beam","Thunderbolt","Rest","Thunder Wave"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)          
#Groudon
class Groudon(Pokemon2):
    "Groudon"
    def __init__(self,name="Groudon",type1="Ground",type2=None,nature=None,level=100,happiness=255,hp=100,atk=150,defense=140,spatk=100,spdef=90,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Drought"):
        if move is None:
            avmoves=["Hyper Beam","Precipice Blades","Earthq","Eruption","Ancient Power","Swords Dance","Fire Blast","Fire Punch","Rest","Thunder Wave"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability) 
#Primal Groudon
class PGroudon(Pokemon2):
    "Primal Groudon"
    def __init__(self,name="Primal Groudon",type1="Ground",type2="Fire",nature=None,level=100,happiness=255,hp=100,atk=180,defense=160,spatk=150,spdef=90,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Desolate Land"):
        if move is None:
            avmoves=["Hyper Beam","Precipice Blades","Earthquake","Eruption","Ancient Power","Swords Dance","Fire Blast","Fire Punch","Rest","Thunder Wave"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                                            #Torterra
class Torterra(Pokemon2):
    "Torterra"
    def __init__(self,name="Torterra",type1="Grass",type2="Ground",nature=None,level=100,happiness=255,hp=95,atk=109,defense=105,spatk=75,spdef=85,speed=56,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Overgrow"):
        if move is None:
            avmoves=["Hyper Beam","Wood Hammer","Earthquake","Leaf Storm","Ancient Power","Swords Dance","Curse","Synthesis","Crunch","Giga Drain"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)   
#Infernape
class Infernape(Pokemon2):
    "Infernape"
    def __init__(self,name="Infernape",type1="Fire",type2="Fighting",nature=None,level=100,happiness=255,hp=76,atk=104,defense=71,spatk=104,spdef=71,speed=108,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Blaze"):
        if move is None:
            avmoves=["Hyper Beam","Flare Blitz","Close Combat","Fire Blast","Mach Punch","Swords Dance","Power-up Punch","Overheat","Calm Mind","Flamethrower"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability) 
#Empoleon
class Empoleon(Pokemon2):
    "Empoleon"
    def __init__(self,name="Empoleon",type1="Water",type2="Steel",nature=None,level=100,happiness=255,hp=84,atk=86,defense=88,spatk=111,spdef=101,speed=60,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Torrent"):
        if move is None:
            avmoves=["Hyper Beam","Surf","Flash Cannon","Hydro Pump","Liquidation","Wave Crash","Ice Beam","Steel Beam","Rest","Scald"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)          
#Staraptor
class Staraptor(Pokemon2):
    "Staraptor"
    def __init__(self,name="Staraptor",type1="Normal",type2="Flying",nature=None,level=100,happiness=255,hp=85,atk=120,defense=70,spatk=50,spdef=60,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Intimidate"):
        if move is None:
            avmoves=["Final Gambit","Roost","Brave Bird","Close Combat","U-Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)            
#Luxray
class Luxray(Pokemon2):
    "Luxray"
    def __init__(self,name="Luxray",type1="Electric",type2="Dark",nature=None,level=100,happiness=255,hp=80,atk=120,defense=79,spatk=95,spdef=79,speed=70,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Intimidate"):
        if move is None:
            avmoves=["Wild Charge","Crunch","Thunder Wave","Play Rough"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)           
#Roserade
class Roserade(Pokemon2):
    "Roserade"
    def __init__(self,name="Roserade",type1="Grass",type2="Poison",nature=None,level=100,happiness=255,hp=60,atk=70,defense=65,spatk=125,spdef=105,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Technician"):
        if move is None:
            avmoves=["Weather Ball","Toxic","Sunny Day","Giga Drain"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)         
#Rampardos
class Rampardos(Pokemon2):
    "Rampardos"
    def __init__(self,name="Rampardos",type1="Rock",type2=None,nature=None,level=100,happiness=255,hp=97,atk=165,defense=60,spatk=65,spdef=50,speed=58,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Mold Breaker"):
        if move is None:
            avmoves=["Head Smash","Iron Head","Crunch","Stone Edge"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                                           
#Bastiodon
class Bastiodon(Pokemon2):
    "Bastiodon"
    def __init__(self,name="Bastiodon",type1="Rock",type2="Steel",nature=None,level=100,happiness=255,hp=60,atk=52,defense=168,spatk=47,spdef=138,speed=30,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Sturdy"):
        if move is None:
            avmoves=["Iron Defense","Iron Head","Crunch","Stone Edge"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                                            #Vespiquen
class Vespiquen(Pokemon2):
    "Vespiquen"
    def __init__(self,name="Vespiquen",type1="Bug",type2="Flying",nature=None,level=100,happiness=255,hp=70,atk=80,defense=102,spatk=80,spdef=102,speed=40,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Pressure"):
        if move is None:
            avmoves=["Defense Order","Attack Order","Heal Order","Toxic"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                                             #Gastrodon
class WGastrodon(Pokemon2):
    "Gastrodon"
    def __init__(self,name="West Sea Gastrodon",type1="Water",type2="Ground",nature=None,level=100,happiness=255,hp=111,atk=83,defense=68,spatk=92,spdef=82,speed=39,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Storm Drain"):
        if move is None:
            avmoves=["Earth Power","Recover","Hydro Pump","Ice Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)  
#Gastrodon
class EGastrodon(Pokemon2):
    "Gastrodon"
    def __init__(self,name="East Sea Gastrodon",type1="Water",type2="Ground",nature=None,level=100,happiness=255,hp=111,atk=83,defense=68,spatk=92,spdef=82,speed=39,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Storm Drain"):
        if move is None:
            avmoves=["Earth Power","Recover","Hydro Pump","Ice Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)            
#Ambipom
class Ambipom(Pokemon2):
    "Ambipom"
    def __init__(self,name="Ambipom",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=75,atk=100,defense=66,spatk=60,spdef=66,speed=115,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Skill Link"):
        if move is None:
            avmoves=["Toxic","Double Hit","U-Turn","Return"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                                            #Drifblim
class Drifblim(Pokemon2):
    "Drifblim"
    def __init__(self,name="Drifblim",type1="Ghost",type2="Flying",nature=None,level=100,happiness=255,hp=150,atk=80,defense=44,spatk=90,spdef=54,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Flare Boost"):
        if move is None:
            avmoves=["Psychic","Shadow Ball","Calm Mind","Thunderbolt"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                                            #Mega Lopunny
class MLopunny(Pokemon2):
    "Mega Lopunny"
    def __init__(self,name="Mega Lopunny",type1="Normal",type2="Fighting",nature=None,level=100,happiness=255,hp=65,atk=136,defense=94,spatk=54,spdef=96,speed=135,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Scrappy"):
        if move is None:
            avmoves=["High Jump Kick","Return","Fakeout","Power-up Punch"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)            
#Mismagius
class Mismagius(Pokemon2):
    "Mismagius"
    def __init__(self,name="Mismagius",type1="Ghost",type2="Fairy",nature=None,level=100,happiness=255,hp=60,atk=60,defense=60,spatk=105,spdef=105,speed=105,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Levitate"):
        if move is None:
            avmoves=["Psychic","Shadow Ball","Calm Mind","Thunderbolt","Dazzling Gleam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                                            #Honchkrow
class Honchkrow(Pokemon2):
    "Honchkrow"
    def __init__(self,name="Honchkrow",type1="Dark",type2="Flying",nature=None,level=100,happiness=255,hp=100,atk=125,defense=60,spatk=105,spdef=60,speed=71,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Super Luck"):
        if move is None:
            avmoves=["Night Slash","Shadow Ball","Drill Peck","Roost","Dark Pulse"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)          
#Spiritomb
class Spiritomb(Pokemon2):
    "Spiritomb"
    def __init__(self,name="Spiritomb",type1="Ghost",type2="Dark",nature=None,level=100,happiness=255,hp=50,atk=92,defense=108,spatk=92,spdef=108,speed=35,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Pressure"):
        if move is None:
            avmoves=["Night Slash","Shadow Ball","Hypnosis","Nasty Plot","Dark Pulse"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)           
#Garchomp
class Garchomp(Pokemon2):
    "Garchomp"
    def __init__(self,name="Garchomp",type1="Dragon",type2="Ground",nature=None,level=100,happiness=255,hp=108,atk=130,defense=95,spatk=80,spdef=85,speed=102,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Rough Skin"):
        if move is None:
            avmoves=["Swords Dance","Earthquake","Dragon Claw","Stone Edge","Draco Meteor","Flamethrower"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                                            #Mega Garchomp
class MGarchomp(Pokemon2):
    "Mega Garchomp"
    def __init__(self,name="Mega Garchomp",type1="Dragon",type2="Ground",nature=None,level=100,happiness=255,hp=108,atk=170,defense=115,spatk=120,spdef=95,speed=92,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Sand Force"):
        if move is None:
            avmoves=["Swords Dance","Earthquake","Dragon Claw","Stone Edge","Draco Meteor","Flamethrower"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                                            #Lucario
class Lucario(Pokemon2):
    "Lucario"
    def __init__(self,name="Lucario",type1="Fighting",type2="Steel",nature=None,level=100,happiness=255,hp=70,atk=110,defense=70,spatk=115,spdef=70,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Steadfest"):
        if move is None:
            avmoves=["Meteor Mash","Aura Sphere","Dragon Pulse","Close Combat","Bullet Punch","Bone Rush"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                                            #Mega Lucario
class MLucario(Pokemon2):
    "Mega Lucario"
    def __init__(self,name="Mega Lucario",type1="Fighting",type2="Steel",nature=None,level=100,happiness=255,hp=70,atk=145,defense=88,spatk=140,spdef=70,speed=112,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Adaptability"):
        if move is None:
            avmoves=["Meteor Mash","Aura Sphere","Dragon Pulse","Close Combat","Bullet Punch","Bone Rush"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                                            #Hippowdon
class Hippowdon(Pokemon2):
    "Hippowdon"
    def __init__(self,name="Hippowdon",type1="Ground",type2=None,nature=None,level=100,happiness=255,hp=108,atk=112,defense=118,spatk=68,spdef=72,speed=47,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Sand Stream"):
        if move is None:
            avmoves=["Earthquake","Slack Off","Stone Edge","Knock Off"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)          
#Drapion
class Drapion(Pokemon2):
    "Drapion"
    def __init__(self,name="Drapion",type1="Poison",type2="Dark",nature=None,level=100,happiness=255,hp=70,atk=90,defense=110,spatk=60,spdef=75,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Sniper"):
        if move is None:
            avmoves=["Wicked Blow","Cross Poison","Swords Dance","Knock Off","Crunch"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)          
#Toxicroak
class Toxicroak(Pokemon2):
    "Toxicroak"
    def __init__(self,name="Toxicroak",type1="Poison",type2="Fighting",nature=None,level=100,happiness=255,hp=83,atk=106,defense=65,spatk=86,spdef=65,speed=85,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Sniper"):
        if move is None:
            avmoves=["Close Combat","Cross Poison","Swords Dance","Knock Off","Venoshock","Poison Jab"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                                       
#Abomasnow
class Abomasnow(Pokemon2):
    "Abomasnow"
    def __init__(self,name="Abomasnow",type1="Grass",type2="Ice",nature=None,level=100,happiness=255,hp=90,atk=92,defense=75,spatk=92,spdef=85,speed=60,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Snow Warning"):
        if move is None:
            avmoves=["Wood Hammer","Icicle Crash","Blizzard","Ice Shard","Energy Ball","Earth Power"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)       
#Mega Abomasnow
class MAbomasnow(Pokemon2):
    "Abomasnow"
    def __init__(self,name="Abomasnow",type1="Grass",type2="Ice",nature=None,level=100,happiness=255,hp=90,atk=132,defense=105,spatk=132,spdef=105,speed=30,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Snow Warning"):
        if move is None:
            avmoves=["Wood Hammer","Icicle Crash","Blizzard","Ice Shard","Energy Ball","Earth Power"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                                            #Weavile
class Weavile(Pokemon2):
    "Weavile"
    def __init__(self,name="Weavile",type1="Dark",type2="Ice",nature=None,level=100,happiness=255,hp=70,atk=120,defense=65,spatk=45,spdef=85,speed=125,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Pressure"):
        if move is None:
            avmoves=["Night Slash","Icicle Crash","Blizzard","Ice Shard","Assurance","Poison Jab","Fakeout"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                                            #Magnezone
class Magnezone(Pokemon2):
    "Magnezone"
    def __init__(self,name="Magnezone",type1="Electric",type2="Steel",nature=None,level=100,happiness=255,hp=70,atk=70,defense=115,spatk=130,spdef=90,speed=60,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Levitate"):
        if move is None:
            avmoves=["Hidden Power","Flash Cannon","Thunderbolt","Iron Defense"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)      
#Rhyperior
class Rhyperior(Pokemon2):
    "Rhyperior"
    def __init__(self,name="Rhyperior",type1="Ground",type2="Rock",nature=None,level=100,happiness=255,hp=115,atk=140,defense=130,spatk=55,spdef=55,speed=40,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=4,speedev=0,maxiv="No",move=None, ability="Solid Rock"):
        if move is None:
            avmoves=["Stone Rdge","Hammer Arm","High Horsepower","Thunder Punch"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)           
#Tangrowth
class Tangrowth(Pokemon2):
    "Tangrowth"
    def __init__(self,name="Tangrowth",type1="Grass",type2=None,nature=None,level=100,happiness=255,hp=100,atk=100,defense=125,spatk=110,spdef=50,speed=50,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=4,speedev=0,maxiv="No",move=None, ability="Regenerator"):
        if move is None:
            avmoves=["Giga Drain","Sleep Powder","Ancient Power","Poison Jab"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)   
#Electivire
class Electivire(Pokemon2):
    "Electivire"
    def __init__(self,name="Electivire",type1="Electric",type2=None,nature=None,level=100,happiness=255,hp=75,atk=123,defense=67,spatk=95,spdef=85,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=4,speedev=252,maxiv="No",move=None, ability="Motor Drive"):
        if move is None:
            avmoves=["Plasma Fists","Close Combat","Wild Charge","Brick Break"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                                            #Magmortar
class Magmortar(Pokemon2):
    "Magmortar"
    def __init__(self,name="Magmortar",type1="Fire",type2=None,nature=None,level=100,happiness=255,hp=75,atk=95,defense=67,spatk=125,spdef=95,speed=83,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=4,speedev=252,maxiv="No",move=None, ability="Flash Fire"):
        if move is None:
            avmoves=["Fire Blast","Sunny Day","Flamethrower","Toxic"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                     
#Togekiss
class Togekiss(Pokemon2):
    "Togekiss"
    def __init__(self,name="Togekiss",type1="Fairy",type2="Flying",nature=None,level=100,happiness=255,hp=85,atk=50,defense=95,spatk=120,spdef=115,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=4,speedev=252,maxiv="No",move=None, ability="Serene Grace"):
        if move is None:
            avmoves=["Roost","Nasty Plot","Air Slash","Moon Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                
#Yanmega
class Yanmega(Pokemon2):
    "Yanmega"
    def __init__(self,name="Yanmega",type1="Bug",type2="Flying",nature=None,level=100,happiness=255,hp=86,atk=76,defense=86,spatk=116,spdef=56,speed=95,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=4,speedev=252,maxiv="No",move=None, ability="Speed Boost"):
        if move is None:
            avmoves=["Ancient Power","Bug Buzz","Air Slash","U-Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)              
#Gliscor
class Gliscor(Pokemon2):
    "Gliscor"
    def __init__(self,name="Gliscor",type1="Ground",type2="Flying",nature=None,level=100,happiness=255,hp=75,atk=95,defense=125,spatk=45,spdef=75,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=4,speedev=252,maxiv="No",move=None, ability="Poison Heal"):
        if move is None:
            avmoves=["Swords Dance","Earthquake","Rock Slide","U-Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                         
#Porygon-Z
class PorygonZ(Pokemon2):
    "Porygon-Z"
    def __init__(self,name="Porygon-Z",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=85,atk=80,defense=70,spatk=135,spdef=75,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=4,speedev=252,maxiv="No",move=None, ability="Adaptability"):
        if move is None:
            avmoves=["Ice Beam","Calm Mind","Recover","Thunderbolt","Flamethrower","Signal Beam","Hidden Power","Psychic","Shadow Ball","Hyper Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                          
#Gallade
class Gallade(Pokemon2):
    "Gallade"
    def __init__(self,name="Gallade",type1="Psychic",type2="Flighting",nature=None,level=100,happiness=255,hp=68,atk=125,defense=65,spatk=65,spdef=115,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=4,speedev=252,maxiv="No",move=None, ability="Steadfast"):
        if move is None:
            avmoves=["Swords Dance","Psycho Cut","Night Slash","Close Combat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)        
#Mega Gallade
class MGallade(Pokemon2):
    "Mega Gallade"
    def __init__(self,name="Mega Gallade",type1="Psychic",type2="Flighting",nature=None,level=100,happiness=255,hp=68,atk=165,defense=95,spatk=65,spdef=115,speed=110,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=4,speedev=252,maxiv="No",move=None, ability="Inner Focus"):
        if move is None:
            avmoves=["Swords Dance","Psycho Cut","Night Slash","Close Combat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability)                           
                                    
                                                     
                                                                                       
                       
                             
#test=Moltres()
#test.info()                                                                                                        