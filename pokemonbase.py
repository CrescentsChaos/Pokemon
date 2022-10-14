#pylint:disable=C0303
#pylint:disable=R0902
#pylint:disable=R0914
#pylint:disable=C0114
#pylint:disable=R0913
#pylint:disable=C0301
import random
import time
from field import Field
field=Field()
class Pokemon:
    weather=None
    "Pokemon"
    def __init__(self,name="Unidentified",type1="Normal",type2=None,nature=None,level=100,happiness=0,hp=0,atk=0,defense=0,spatk=0,spdef=0,speed=0,hpiv=0,atkiv=0,defiv=0,spatkiv=0,spdefiv=0,speediv=0,maxiv="No",atktype="Normal",hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0,status="Alive",atkb=1,defb=1,spatkb=1,spdefb=1,speedb=1,ability=None,moves=None,movez=None,badpoison=1,flinched=False,recharge=False,seeded=False,intimidated=False,item=None, precharge=False,protect=False):
        #Name
        self.name=name
        if moves is None:
            self.moves=[]
        else:
            self.moves=moves
        self.shiny=random.randint(1,4096)
        if self.shiny==2:
            self.name=self.name+"⭐"
        #Type
        self.type1=type1
        self.type2=type2
        self.item=item
        self.badpoison=badpoison
        self.flinched=flinched
        self.recharge=recharge
        self.seeded=seeded
        self.intimidated=intimidated
        self.precharge=precharge
        self.protect=protect
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
#Extra
    def attack(self,other):
        pass
    def stts(self):
        pass
#Calculates Stats
def stat_clac(stat,individual_value,effort_value,level,spst=None):
	"Generates enhanced stats"
	if spst == "HP":
	    new_stat=round((((2*stat+individual_value+(effort_value*0.25))*level)/100)+level+10)
	else:
	    new_stat=round((((2*stat+individual_value+(effort_value*0.25))*level)/100)+5)
	
	return new_stat
        
#Movelist
def movelist(self):
    "Shows Moves"
    num=0
    print("=============================================")
    print(f"{self.name}'s available moves.")
    print("=============================================")
    if self.moves == []:
        print("No Moves")
    else:
        for i in self.moves:
            num+=1
            print(str(num)+".",i)
    print("=============================================")
def moveset(moves):
    new=[]
    while len(new)!=4:
        x=random.choice(moves)
        if x not in new:
            new.append(x)
    return new
#POKEMONS
#Venusaur
class Venusaur(Pokemon):
    "Venusaur"
    def __init__(self,name="Venusaur",type1="Grass",type2="Poison",nature=None,level=100,happiness=255,hp=80,atk=82,defense=83,spatk=100,spdef=100,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Overgrow","Chlorophyll"]),item="Black Sludge"):
        if move is None:
            moves=["Giga Drain","Earth Power","Sludge Bomb","Solar Beam","Sleep Powder","Leech Seed"]
            moves=moveset(moves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
class Charizard(Pokemon):
    "Charizard"
    def __init__(self,name="Charizard",type1="Fire",type2="Flying",nature=None,level=100,happiness=255,hp=78,atk=84,defense=78,spatk=109,spdef=85,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Blaze","Solar Power"]),item="Leftovers"):
        if move is None:
            avmoves=["Flare Blitz","Dragon Dance","Dragon Claw","Roost"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
class Blastoise(Pokemon):
    "Blastoise"
    def __init__(self,name="Blastoise",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=79,atk=83,defense=100,spatk=85,spdef=105,speed=78,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Torrent","Rain Dish"]),item="Leftovers"):
        if move is None:
            avmoves=["Hydro Pump","Shell Smash","Dragon Pulse","Dark Pulse","Flip Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#mBeedrill
class MBeedrill(Pokemon):
    "Mega Beedrill"
    def __init__(self,name="Mega Beedrill",type1="Bug",type2="Poison",nature=None,level=100,happiness=255,hp=65,atk=90,defense=40,spatk=45,spdef=80,speed=75,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Adaptability",item="Beedrillite"):
        if move is None:
            avmoves=["Poison Jab","Knock Off","Sludge Bomb","Drill Run"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Nidoqueen
class Nidoqueen(Pokemon):
    "Nidoqueen"
    def __init__(self,name="Nidoqueen",type1="Poison",type2="Ground",nature=None,level=100,happiness=255,hp=90,atk=92,defense=87,spatk=75,spdef=85,speed=76,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Sheer Force",item="Life Orb"):
        if move is None:
            avmoves=["Ice Beam","Earth Power","Sludge Bomb","Strength","Poison Jab"]
            moves=moveset(avmoves)
            
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
        
        
#Nidoking
class Nidoking(Pokemon):
    "Nidoking"
    def __init__(self,name="Nidoking",type1="Poison",type2="Ground",nature=None,level=100,happiness=255,hp=81,atk=102,defense=77,spatk=85,spdef=75,speed=85,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Sheer Force",item="Life Orb"):
        if move is None:
            avmoves=["Ice Beam","Earth Power","Sludge Bomb","Strength","Poison Jab","Thunderbolt"]
            moves=moveset(avmoves)
            
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Ninetales
class Ninetales(Pokemon):
    "Ninetales"
    def __init__(self,name="Ninetales",type1="Fire",type2=None,    nature=None,level=100,happiness=255,hp=73,atk=76,defense=75,spatk=81,spdef=100,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Flash Fire","Drought"]),item="Leftovers"):
        if move is None:
            avmoves=["Fire Blast","Flamethrower","Solar Beam","Hidden Power"]
            moves=moveset(avmoves)
            
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Alolan Ninetales
class ANinetales(Pokemon):
    "Alolan Ninetales"
    def __init__(self,name="Alolan Ninetales",type1="Ice",type2="Fairy",    nature=None,level=100,happiness=255,hp=73,atk=67,defense=75,spatk=81,spdef=100,speed=109,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Snow Warning",item="Leftovers"):
        if move is None:
            avmoves=["Ice Beam","Moon Blast","Hidden Power","Dazzling Gleam"]
            moves=moveset(avmoves)
            
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Golduck
class Golduck(Pokemon):
    "Golduck"
    def __init__(self,name="Golduck",type1="Water",type2="Psychic",    nature=None,level=100,happiness=255,hp=80,atk=82,defense=78,spatk=95,spdef=80,speed=85,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Cloud Nine",item="Leftovers"):
        if move is None:
            avmoves=["Ice Beam","Psychic","Hydro Pump","Hidden Power","Rain Dance"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Primeape
class Primeape(Pokemon):
    "Primeape"
    def __init__(self,name="Primeape",type1="Fighting",type2=None,nature=None,level=100,happiness=255,hp=65,atk=105,defense=60,spatk=60,spdef=70,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Anger Point",item="Leftovers"):
        if move is None:
            avmoves=["Hidden Power","Dynamic Punch","Close Combat","Superpower","Fire Punch","U-Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Arcanine
class Arcanine(Pokemon):
    "Arcanine"
    def __init__(self,name="Arcanine",type1="Fire",type2=None,nature=None,level=100,happiness=255,hp=90,atk=110,defense=80,spatk=100,spdef=80,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Intimidate","Flash Fire"]),item="Leftovers"):
        if move is None:
            avmoves=["Hidden Power","Fire Blast","Flamethrower","Sunny Day","Solar Beam","Flare Blitz","Wild Charge","Morning Sun"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
        
#Poliwrath
class Poliwrath(Pokemon):
    "Poliwrath"
    def __init__(self,name="Poliwrath",type1="Water",type2="Fighting",nature=None,level=100,happiness=255,hp=90,atk=95,defense=95,spatk=70,spdef=90,speed=70,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Water Absorb",item="Leftovers"):
        if move is None:
            avmoves=["Hidden Power","Ice Beam","Hydro Pump","Dynamic Punch","Thunder Punch","Rain Dance"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Mega Pidgeot 
class MPidgeot(Pokemon):
    "Mega Pidgeot"
    def __init__(self,name="Mega Pidgeot",type1="Normal",type2="Flying",nature=None,level=100,happiness=255,hp=83,atk=80,defense=80,spatk=135,spdef=80,speed=121,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="No Guard",item="Pidgeotite"):
        if move is None:
            avmoves=["Hidden Power","Hurricane","Dual Wingbeat","Brave Bird","U-Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)   
#Pidgeot        
class Pidgeot(Pokemon):
    "Pidgeot"
    def __init__(self,name="Pidgeot",type1="Normal",type2="Flying",nature=None,level=100,happiness=255,hp=83,atk=80,defense=75,spatk=70,spdef=70,speed=101,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="No Guard",item="Leftovers"):
        if move is None:
            avmoves=["Hidden Power","Hurricane","Dual Wingbeat","Brave Bird","U-Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)       
#Alakazam
class Alakazam(Pokemon):
    "Alakazam"
    def __init__(self,name="Alakazam",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=55,atk=50,defense=45,spatk=135,spdef=95,speed=120,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Magic Guard",item="Focus Sash"):
        if move is None:
            avmoves=["Hidden Power","Recover","Moon Blast","Shadow Ball","Nasty Plot","Dark Pulse"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)              
#Mega  Alakazam
class MAlakazam(Pokemon):
    "Mega Alakazam"
    def __init__(self,name="Mega Alakazam",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=55,atk=50,defense=65,spatk=175,spdef=105,speed=150,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Trace",item="Alakazite"):
        if move is None:
            avmoves=["Hidden Power","Recover","Moon Blast","Shadow Ball","Nasty Plot","Dark Pulse"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Machamp
class Machamp(Pokemon):
    "Machamp"
    def __init__(self,name="Machamp",type1="Fighting",type2=None,nature=None,level=100,happiness=255,hp=90,atk=130,defense=80,spatk=65,spdef=85,speed=55,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="No Guard",item="Leftovers"):
        if move is None:
            avmoves=["Dynamic Punch","Close Combat","Superpower","Fire Punch"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                     
#Victreebel
class Victreebel(Pokemon):
    "Victreebel"
    def __init__(self,name="Victreebel",type1="Grass",type2="Poison",nature=None,level=100,happiness=255,hp=80,atk=105,defense=65,spatk=100,spdef=70,speed=70,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Chlorophyll",item="Leftovers"):
        if move is None:
            avmoves=["Power Whip","Sludge Bomb","Sleep Powder","Solar Beam","Toxic"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Tentacruel
class Tentacruel(Pokemon):
    "Tentacruel"
    def __init__(self,name="Tentacruel",type1="Water",type2="Poison",nature=None,level=100,happiness=255,hp=80,atk=70,defense=65,spatk=80,spdef=120,speed=100,hpev=0,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=252,maxiv="No",move=None, ability="Clear Body",item="Leftovers"):
        if move is None:
            avmoves=["Hidden Power","Ice Beam","Hydro Pump","Thunderbolt","Sludge Bomb","Poison Jab","Rain Dance"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Golem
class Golem(Pokemon):
    "Golem"
    def __init__(self,name="Golem",type1="Rock",type2="Ground",nature=None,level=100,happiness=255,hp=80,atk=120,defense=130,spatk=55,spdef=65,speed=45,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Rock Head","Sturdy"]),item="Leftovers"):
        if move is None:
            avmoves=["Stone Edge","Earthquake","Stealth Rock","Rock Blast","Explosion"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Golem
class AGolem(Pokemon):
    "Alolan Golem"
    def __init__(self,name="Alolan Golem",type1="Rock",type2="Electric",nature=None,level=100,happiness=255,hp=80,atk=120,defense=130,spatk=55,spdef=65,speed=45,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Galvanize",item="Leftovers"):
        if move is None:
            avmoves=["Stone Edge","Earthquake","Stealth Rock","Rock Blast","Thunderbolt","Explosion"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Rapidash
class Rapidash(Pokemon):
    "Rapidash"
    def __init__(self,name="Rapidash",type1="Fire",type2=None,nature=None,level=100,happiness=255,hp=65,atk=100,defense=70,spatk=80,spdef=80,speed=125,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Flash Fire","Reckless"]),item="Leftovers"):
        if move is None:
            avmoves=["Fire Blast","Flamethrower","Flare Blitz","Inferno","Morning Sun","Sunny Day","High Horsepower"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                
#Slowbro
class Slowbro(Pokemon):
    "Slowbro"
    def __init__(self,name="Slowbro",type1="Water",type2="Psychic",nature=None,level=100,happiness=255,hp=95,atk=75,defense=110,spatk=100,spdef=80,speed=30,hpev=0,atkev=0,defev=252,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Regenerator",item="Leftovers"):
        if move is None:
            avmoves=["Hidden Power","Ice Beam","Slack Off","Psychic","Flamethrower","Hydro Pump","Thunderbolt","Iron Defense","Rain Dance","Rest"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Mega Slowbro
class MSlowbro(Pokemon):
    "Mega Slowbro"
    def __init__(self,name="Mega Slowbro",type1="Water",type2="Psychic",nature=None,level=100,happiness=255,hp=95,atk=75,defense=180,spatk=130,spdef=80,speed=30,hpev=0,atkev=0,defev=252,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Shell Armor",item="Slowbronite"):
        if move is None:
            avmoves=["Hidden Power","Ice Beam","Slack Off","Psychic","Flamethrower","Hydro Pump","Thunderbolt","Iron Defense","Body Press","Rest"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                   
#Dodrio
class Dodrio(Pokemon):
    "Dodrio"
    def __init__(self,name="Dodrio",type1="Flying",type2="Fighting",nature=None,level=100,happiness=255,hp=60,atk=110,defense=70,spatk=60,spdef=60,speed=110,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Rock Head",item="Leftovers"):
        if move is None:
            avmoves=["Close Combat","Brave Bird","Roost","Sky Attack","High Jump Kick"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Muk
class Muk(Pokemon):
    "Muk"
    def __init__(self,name="Muk",type1="Poison",type2=None,nature=None,level=100,happiness=255,hp=105,atk=105,defense=75,spatk=65,spdef=100,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Regenerator",item="Black Sludge"):
        if move is None:
            avmoves=["Poison Jab","Acid Armor","Psychic","Toxic","Sludge Bomb","Venoshock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                       
#Cloyster
class Cloyster(Pokemon):
    "Cloyster"
    def __init__(self,name="Cloyster",type1="Water",type2="Ice",nature=None,level=100,happiness=255,hp=50,atk=95,defense=180,spatk=85,spdef=45,speed=70,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Skill Link",item="Focus Sash"):
        if move is None:
            avmoves=["Ice Beam","Rock Blast","Icicle Spear","Shell Smash","Hydro Pump","Pin Missile","Hail"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                               
#Gengar
class Gengar(Pokemon):
    "Gengar"
    def __init__(self,name="Gengar",type1="Ghost",type2="Poison",nature=None,level=100,happiness=255,hp=60,atk=65,defense=60,spatk=130,spdef=75,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Levitate",item="Black Sludge"):
        if move is None:
            avmoves=["Hidden Power","Ice Beam","Dazzling Gleam","Psychic","Shadow Ball","Dark Pulse","Thunderbolt","Nasty Plot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Mega Gengar
class MGengar(Pokemon):
    "Mega Gengar"
    def __init__(self,name="Mega Gengar",type1="Ghost",type2="Poison",nature=None,level=100,happiness=255,hp=60,atk=65,defense=80,spatk=170,spdef=95,speed=130,hpev=0,atkev=0,defev=0,spatkev=253,spdefev=0,speedev=252,maxiv="No",move=None, ability="Shadow Tag",item="Gengarite"):
        if move is None:
            avmoves=["Hidden Power","Ice Beam","Dazzling Gleam","Psychic","Shadow Ball","Dark Pulse","Thunderbolt","Nasty Plot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Exeggutor
class Exeggutor(Pokemon):
    "Exeggutor"
    def __init__(self,name="Exeggutor",type1="Grass",type2="Psychic",nature=None,level=100,happiness=255,hp=95,atk=95,defense=85,spatk=125,spdef=75,speed=55,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Chlorophyll",item="Leftovers"):
        if move is None:
            avmoves=["Hidden Power","Giga Drain","Sunny Day","Psychic","Solar Beam","Egg Bomb","Leech Seed","Morning Sun"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)             
#Alolan Exeggutor
class AExeggutor(Pokemon):
    "Alolan Exeggutor"
    def __init__(self,name="Alolan Exeggutor",type1="Grass",type2="Dragon",nature=None,level=100,happiness=255,hp=95,atk=105,defense=85,spatk=125,spdef=75,speed=45,hpev=0,atkev=252,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Chlorophyll",item="Leftovers"):
        if move is None:
            avmoves=["Sunny Day","Egg Bomb","Psychic","Solar Beam","Dragon Hammer","Zen Headbutt"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Alolan Muk
class AMuk(Pokemon):
    "Alolan Muk"
    def __init__(self,name="Alolan Muk",type1="Poison",type2="Dark",nature=None,level=100,happiness=255,hp=105,atk=105,defense=75,spatk=65,spdef=100,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Regenerator",item="Black Sludge"):
        if move is None:
            avmoves=["Sludge Bomb","Toxic","Poison Jab","Venoshock","Smocksceen"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Hitmonlee
class Hitmonlee(Pokemon):
    "Hitmonlee"
    def __init__(self,name="Hitmonlee",type1="Fighting",type2=None,nature=None,level=100,happiness=255,hp=50,atk=120,defense=53,spatk=35,spdef=110,speed=87,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Reckless",item="Leftovers"):
        if move is None:
            avmoves=["Blaze Kick","High Jump Kick","Superpower","Pyro Ball","Low Kick","Close Combat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Hitmonchan
class Hitmonchan(Pokemon):
    "Hitmonchan"
    def __init__(self,name="Hitmonchan",type1="Fighting",type2=None,nature=None,level=100,happiness=255,hp=50,atk=115,defense=79,spatk=35,spdef=110,speed=76,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Iron Fist",item="Leftovers"):
        if move is None:
            avmoves=["Ice Punch","Thunder Punch","Mach Punch","Fire Punch","Dizzy Punch","Dynamic Punch"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Weezing
class Weezing(Pokemon):
    "Weezing"
    def __init__(self,name="Weezing",type1="Poison",type2=None,nature=None,level=100,happiness=255,hp=65,atk=90,defense=120,spatk=85,spdef=70,speed=60,hpev=0,atkev=0,defev=252,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Levitate",item="Black Sludge"):
        if move is None:
            avmoves=["Sludge Bomb","Toxic","Poison Jab","Venoshock","Explosion"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)              
#Kangaskhan
class Kangaskhan(Pokemon):
    "Kangaskhan"
    def __init__(self,name="Kangaskhan",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=105,atk=95,defense=80,spatk=40,spdef=80,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Scrappy",item="Leftovers"):
        if move is None:
            avmoves=["Crunch","Body Slam","Fakeout","Power-up Punch","Earthquake"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Mega Kangaskhan
class MKangaskhan(Pokemon):
    "Mega Kangaskhan"
    def __init__(self,name="Mega Kangaskhan",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=105,atk=125,defense=100,spatk=60,spdef=100,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Parental Bond",item="Kangaskhanite"):
        if move is None:
            avmoves=["Crunch","Body Slam","Fakeout","Power-up Punch","Earthquake"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)     
#Starmie
class Starmie(Pokemon):
    "Starmie"
    def __init__(self,name="Starmie",type1="Water",type2="Psychic",nature=None,level=100,happiness=255,hp=60,atk=75,defense=85,spatk=100,spdef=85,speed=115,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Natural Cure",item="Leftovers"):
        if move is None:
            avmoves=["Hidden Power","Ice Beam","Scald","Psychic","Surf","Hydro Pump","Thunderbolt","Flip Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Pinsir
class Pinsir(Pokemon):
    "Pinsir"
    def __init__(self,name="Pinsir",type1="Bug",type2=None,nature=None,level=100,happiness=255,hp=65,atk=125,defense=100,spatk=55,spdef=70,speed=85,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Moxie",item="Leftovers"):
        if move is None:
            avmoves=["Megahorn","Return","Brick Break","Close Combat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Mega Pinsir
class MPinsir(Pokemon):
    "Mega Pinsir"
    def __init__(self,name="Mega Pinsir",type1="Bug",type2="Flying",nature=None,level=100,happiness=255,hp=65,atk=155,defense=120,spatk=65,spdef=90,speed=105,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Aerilate",item="Pinsirite"):
        if move is None:
            avmoves=["Double Edge","Megahorn","Return","Brick Break","Close Combat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Tauros
class Tauros(Pokemon):
    "Tauros"
    def __init__(self,name="Tauros",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=75,atk=100,defense=95,spatk=40,spdef=70,speed=110,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Intimidate","Sheer Force"]),item="Leftovers"):
        if move is None:
            avmoves=["Double Edge","Strength","Earthquake","Drill Run","Head Smash","Megahorn","Rest"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Gyarados
class Gyarados(Pokemon):
    "Gyarados"
    def __init__(self,name="Gyarados",type1="Water",type2="Flying",nature=None,level=100,happiness=255,hp=95,atk=125,defense=79,spatk=60,spdef=100,speed=81,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Intimidate","Moxie"]),item="Leftovers"):
        if move is None:
            avmoves=["Crunch","Waterfall","Dragon Dance","Earthquake","Aqua Tail"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Mega Gyarados
class MGyarados(Pokemon):
    "Mega Gyarados"
    def __init__(self,name="Mega Gyarados",type1="Water",type2="Dark",nature=None,level=100,happiness=255,hp=95,atk=155,defense=109,spatk=70,spdef=130,speed=81,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Mold Breaker",item="Gyaradosite"):
        if move is None:
            avmoves=["Crunch","Waterfall","Dragon Dance","Earthquake","Aqua Tail"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Lapras
class Lapras(Pokemon):
    "Lapras"
    def __init__(self,name="Lapras",type1="Water",type2="Ice",nature=None,level=100,happiness=255,hp=130,atk=85,defense=80,spatk=85,spdef=95,speed=60,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Water Absorb",item="Leftovers"):
        if move is None:
            avmoves=["Hidden Power","Ice Beam","Hydro Pump","Thunderbolt","Surf","Hail","Rain Dance"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)

#Omastar
class Omastar(Pokemon):
    "Omastar"
    def __init__(self,name="Omastar",type1="Rock",type2="Water",nature=None,level=100,happiness=255,hp=70,atk=60,defense=125,spatk=115,spdef=70,speed=55,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Shell Armor",item="Leftovers"):
        if move is None:
            avmoves=["Hidden Power","Ice Beam","Hydro Pump","Ancient Power","Rock Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        

        
#DRIVER CODE
#start=time.time()
#end=time.time()
#print(help(Venusaur))
#a=Nidoqueen()
#a.info()
#movelist(a)
def zmove(mon):
    tp=""
    ch=random.randint(1,2)
    if mon is None:
        return ["Breakneck Blitz "]
    if ch==1:
        tp=mon.type1
    if ch==2 :
        if mon.type2 is None:
            tp=mon.type1
        else:
            tp=mon.type2
       
    if "eon" in mon.name and "Last Resort" in mon.moves:
        mon.item="Eevium Z"
        return ["Extreme Evoboost"]
    elif "Snorlax" in mon.name and "Giga Impact" in mon.moves:
        mon.item="Snorlium Z"
        return ["Pulverizing Pancake"]
    elif tp=="Fire":
        mon.item="Firium Z"
        return ["Inferno Overdrive"]
    elif tp=="Water":
        mon.item="Waterium Z"
        return ["Hydro Vortex"]
    elif tp=="Poison":
        mon.item="Poisonium Z"
        return ["Acid Downpour"]
    elif tp=="Fighting":
        mon.item="Fightinium Z"
        return ["All-Out Pummeling"]
    elif tp=="Dark":
        mon.item="Darkium Z"
        return ["Black Hole Eclipse"]
    elif tp=="Grass":
        mon.item="Grassium Z"
        return ["Bloom Doom"]
    elif tp=="Normal":
        mon.item="Normalium Z"
        return ["Breakneck Blitz"]
    elif tp=="Rock":
        mon.item="Rockium Z"
        return ["Continental Crush"]
    elif tp=="Steel":
        mon.item="Steelium Z"
        return ["Corkscrew Crash"]
    elif tp=="Dragon":
        mon.item="Dragonium Z"
        return ["Devastating Drake"]
    elif tp=="Psychic":
        mon.item="Pychium Z"
        return ["Shattered Psyche"]
    elif tp=="Electric":
        mon.item="Electrium Z"
        return ["Gigavolt Havoc"]
    elif tp=="Ghost":
        mon.item="Ghostium Z"
        return ["Never-ending Nightmare"]
    elif tp=="Bug":
        mon.item="Buginium Z"
        return ["Savage Spin-Out"]
    elif tp=="Ice":
        mon.item="Icium Z"
        return ["Subzero Slammer"]
    elif tp=="Ground":
        mon.item="Groundium Z"
        return ["Tectonic Rage"]
    elif tp=="Fairy":
        mon.item="Fairium Z"
        return ["Twinkle Tackle"]
    elif tp=="Flying":
        mon.item="Flyinium Z"   
        return ["Supersonic Skystrike"]