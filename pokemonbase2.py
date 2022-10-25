#pylint:disable=R0902
#pylint:disable=C0116
#pylint:disable=C0115
#pylint:disable=C0115
#pylint:disable=R0915
##pylint:disable=R0914
#pylint:disable=C0304
#pylint:disable=R0913
#pylint:disable=C0301
#pylint:disable=C0303
import random
naturelist=["Hardy","Lonely","Adamant","Naughty","Brave", "Bold",'Docile','Impish','Lax','Relaxed' ,'Modest','Mild','Bashful','Rash','Quiet' ,'Calm','Gentle','Careful','Quirky','Sassy', 'Timid','Hasty','Jolly','Naive','Serious']
class Pokemon2:
    weather=None
    trickroom=False 
    "Pokemon2"
    def __init__(self,name="Unidentified",type1="Normal",type2=None,nature=None,level=100,happiness=0,hp=0,atk=0,defense=0,spatk=0,spdef=0,speed=0,hpiv=0,atkiv=0,defiv=0,spatkiv=0,spdefiv=0,speediv=0,maxiv="No",atktype="Normal",hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0,status="Alive",atkb=1,defb=1,spatkb=1,spdefb=1,speedb=1,ability=None,moves=None,movez=None,badpoison=1,flinched=False,recharge=False,seeded=False, canfakeout=True,item="Leftovers",precharge=False, protect=False,gmax=False,shelltrap=False,choiced=False,choicedmove=None):
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
        self.shelltrap=shelltrap
        self.canfakeout=canfakeout
        self.choiced=choiced
        self.choicedmove=choicedmove
        #Nature
        self.nature=nature
        if self.nature is None:
            self.gennature()
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
           self.teratype=random.choice(["Rock","Fire","Water","Grass","Electric","Ground","Flying","Fighting","Fairy","Dragon","Steel","Poison","Dark","Ghost","Normal","Bug","Ice"])
           if self.teratype in (self.type1,self.type2):
                self.atkb=1.5
                self.spatkb=1.5
           self.moves+=["Tera Blast"]
           self.name+="💎"
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
        self.gmax=gmax
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
            print(f"Type: {self.type1}/{self.type2}")
        print(f"Nature: {self.nature}")
        print(f"Ability: {self.ability}")
        print(f"Item: {self.item}")
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
    elif "Lycanroc" in mon.name and "Stone Edge" in mon.moves:
        mon.item="Lycanium Z"
        return ["Splintered Stromshards"]        
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

        
#Venusaur
class Venusaur(Pokemon2):
    "Venusaur"
    def __init__(self,name="Venusaur",type1="Grass",type2="Poison",nature=None,level=100,happiness=255,hp=80,atk=82,defense=83,spatk=100,spdef=100,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Overgrow","Chlorophyll"]),item=random.choice(["Black Sludge","Life Orb","Grass Gem","Poison Gem"])):
        if move is None:
            moves=["Giga Drain","Earth Power","Sludge Bomb","Solar Beam","Sleep Powder","Leech Seed","Frenzy Plant"]
            moves=moveset(moves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
class Charizard(Pokemon2):
    "Charizard"
    def __init__(self,name="Charizard",type1="Fire",type2="Flying",nature=None,level=100,happiness=255,hp=78,atk=84,defense=78,spatk=109,spdef=85,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Blaze","Solar Power"]),item=random.choice(["Heavy-Duty Boots","Life Orb","Fire Gem"])):
        if move is None:
            avmoves=["Flare Blitz","Dragon Dance","Dragon Claw","Roost","Flamethrower","Fire Blast","Blast Burn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
class Blastoise(Pokemon2):
    "Blastoise"
    def __init__(self,name="Blastoise",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=79,atk=83,defense=100,spatk=85,spdef=105,speed=78,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Torrent","Rain Dish"]),item=random.choice(["Sitrus Berry","Life Orb","Water Gem"])):
        if move is None:
            avmoves=["Hydro Pump","Shell Smash","Dragon Pulse","Dark Pulse","Flip Turn","Hydro Cannon"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#mBeedrill
class MBeedrill(Pokemon2):
    "Mega Beedrill"
    def __init__(self,name="Mega Beedrill",type1="Bug",type2="Poison",nature=None,level=100,happiness=255,hp=65,atk=150,defense=40,spatk=15,spdef=80,speed=145,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Adaptability",item="Beedrillite"):
        if move is None:
            avmoves=["Poison Jab","Knock Off","Sludge Bomb","Drill Run","Toxic Spikes"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Nidoqueen
class Nidoqueen(Pokemon2):
    "Nidoqueen"
    def __init__(self,name="Nidoqueen",type1="Poison",type2="Ground",nature=None,level=100,happiness=255,hp=90,atk=92,defense=87,spatk=75,spdef=85,speed=76,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Sheer Force","Poison Point"]),item=random.choice(["Black Sludge","Life Orb"])):
        if move is None:
            avmoves=["Ice Beam","Earth Power","Sludge Bomb","Strength","Poison Jab","Toxic Spikes"]
            moves=moveset(avmoves)
            
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
        
        
#Nidoking
class Nidoking(Pokemon2):
    "Nidoking"
    def __init__(self,name="Nidoking",type1="Poison",type2="Ground",nature=None,level=100,happiness=255,hp=81,atk=102,defense=77,spatk=85,spdef=75,speed=85,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Sheer Force","Poison Point"]),item=random.choice(["Black Sludge","Life Orb"])):
        if move is None:
            avmoves=["Ice Beam","Earth Power","Sludge Bomb","Strength","Poison Jab","Thunderbolt","Toxic Spikes"]
            moves=moveset(avmoves)
            
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Ninetales
class Ninetales(Pokemon2):
    "Ninetales"
    def __init__(self,name="Ninetales",type1="Fire",type2=None,    nature=None,level=100,happiness=255,hp=73,atk=76,defense=75,spatk=81,spdef=100,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Flash Fire","Drought"]),item=random.choice(["Heat Rock","Life Orb","Fire Gem"])):
        if move is None:
            avmoves=["Fire Blast","Flamethrower","Solar Beam","Hidden Power"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Alolan Ninetales
class ANinetales(Pokemon2):
    "Alolan Ninetales"
    def __init__(self,name="Alolan Ninetales",type1="Ice",type2="Fairy",    nature=None,level=100,happiness=255,hp=73,atk=67,defense=75,spatk=81,spdef=100,speed=109,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Snow Warning",item=random.choice(["Icy Rock","Light Clay","Ice Gem","Fairy Gem"])):
        if move is None:
            avmoves=["Ice Beam","Moonblast","Hidden Power","Dazzling Gleam"]
            moves=moveset(avmoves)
            
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Golduck
class Golduck(Pokemon2):
    "Golduck"
    def __init__(self,name="Golduck",type1="Water",type2="Psychic",    nature=None,level=100,happiness=255,hp=80,atk=82,defense=78,spatk=100,spdef=80,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Neuroforce",item=random.choice(["Leftovers","Life Orb"])):
        if move is None:
            avmoves=["Ice Beam","Psychic","Hydro Pump","Hidden Power","Rain Dance"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Primeape
class Primeape(Pokemon2):
    "Primeape"
    def __init__(self,name="Primeape",type1="Fighting",type2=None,nature=None,level=100,happiness=255,hp=65,atk=105,defense=60,spatk=60,spdef=70,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Gorilla Tactics",item=random.choice(["Choice Scarf","Life Orb"])):
        if move is None:
            avmoves=["Hidden Power","Dynamic Punch","Close Combat","Superpower","Fire Punch","U-Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Arcanine
class Arcanine(Pokemon2):
    "Arcanine"
    def __init__(self,name="Arcanine",type1="Fire",type2=None,nature=None,level=100,happiness=255,hp=90,atk=110,defense=80,spatk=100,spdef=80,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Intimidate","Flash Fire"]),item=random.choice(["Heavy-Duty Boots","Life Orb"])):
        if move is None:
            avmoves=["Hidden Power","Fire Blast","Flamethrower","Sunny Day","Solar Beam","Flare Blitz","Wild Charge","Morning Sun","Extreme Speed"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
        
#Poliwrath
class Poliwrath(Pokemon2):
    "Poliwrath"
    def __init__(self,name="Poliwrath",type1="Water",type2="Fighting",nature=None,level=100,happiness=255,hp=90,atk=95,defense=95,spatk=70,spdef=90,speed=70,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Water Absorb",item=random.choice(["Choice Band","Life Orb","Leftovers"])):
        if move is None:
            avmoves=["Hidden Power","Ice Beam","Hydro Pump","Dynamic Punch","Thunder Punch","Rain Dance"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Mega Pidgeot 
class MPidgeot(Pokemon2):
    "Mega Pidgeot"
    def __init__(self,name="Mega Pidgeot",type1="Normal",type2="Flying",nature=None,level=100,happiness=255,hp=83,atk=80,defense=80,spatk=135,spdef=80,speed=121,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="No Guard",item="Pidgeotite"):
        if move is None:
            avmoves=["Hidden Power","Hurricane","Dual Wingbeat","Brave Bird","U-Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)   
#Pidgeot        
class Pidgeot(Pokemon2):
    "Pidgeot"
    def __init__(self,name="Pidgeot",type1="Normal",type2="Flying",nature=None,level=100,happiness=255,hp=83,atk=80,defense=75,spatk=70,spdef=70,speed=101,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Big Pecks",item=random.choice(["Choice Band","Life Orb","Flying Gem"])):
        if move is None:
            avmoves=["Hidden Power","Hurricane","Dual Wingbeat","Brave Bird","U-Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)       
#Alakazam
class Alakazam(Pokemon2):
    "Alakazam"
    def __init__(self,name="Alakazam",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=55,atk=50,defense=45,spatk=135,spdef=95,speed=120,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Magic Guard","Inner Focus"]),item="Focus Sash"):
        if move is None:
            avmoves=["Hidden Power","Recover","Dazzling Gleam","Shadow Ball","Nasty Plot","Dark Pulse","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)              
#Mega  Alakazam
class MAlakazam(Pokemon2):
    "Mega Alakazam"
    def __init__(self,name="Mega Alakazam",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=55,atk=50,defense=65,spatk=175,spdef=105,speed=150,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Trace",item="Alakazite"):
        if move is None:
            avmoves=["Hidden Power","Recover","Dazzling Gleam","Shadow Ball","Nasty Plot","Dark Pulse","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Machamp
class Machamp(Pokemon2):
    "Machamp"
    def __init__(self,name="Machamp",type1="Fighting",type2=None,nature=None,level=100,happiness=255,hp=90,atk=130,defense=80,spatk=65,spdef=85,speed=55,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["No Guard","Guts"]),item=random.choice(["Choice Band","Black Belt"])):
        if move is None:
            avmoves=["Dynamic Punch","Close Combat","Superpower","Fire Punch"]
            moves=moveset(avmoves)
        else:
            moves=move
        if ability=="Guts":
            item="Flame Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                     
#Victreebel
class Victreebel(Pokemon2):
    "Victreebel"
    def __init__(self,name="Victreebel",type1="Grass",type2="Poison",nature=None,level=100,happiness=255,hp=80,atk=105,defense=70,spatk=100,spdef=75,speed=70,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Chlorophyll",item=random.choice(["Rocky Helmet","Black Sludge"])):
        if move is None:
            avmoves=["Power Whip","Sludge Bomb","Sleep Powder","Solar Beam","Toxic","Toxic Spikes"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Tentacruel
class Tentacruel(Pokemon2):
    "Tentacruel"
    def __init__(self,name="Tentacruel",type1="Water",type2="Poison",nature=None,level=100,happiness=255,hp=80,atk=60,defense=80,spatk=90,spdef=120,speed=100,hpev=0,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=252,maxiv="No",move=None, ability="Clear Body",item="Black Sludge"):
        if move is None:
            avmoves=["Hidden Power","Ice Beam","Hydro Pump","Thunderbolt","Sludge Bomb","Poison Jab","Rain Dance","Toxic Spikes"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Golem
class Golem(Pokemon2):
    "Golem"
    def __init__(self,name="Golem",type1="Rock",type2="Ground",nature=None,level=100,happiness=255,hp=80,atk=120,defense=130,spatk=55,spdef=65,speed=45,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Rock Head","Sturdy"]),item=random.choice(["Weakness Policy","Custap Berry"])):
        if move is None:
            avmoves=["Stone Edge","Earthquake","Stealth Rock","Rock Blast","Explosion","Magnitude","Bulldoze"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Golem
class AGolem(Pokemon2):
    "Alolan Golem"
    def __init__(self,name="Alolan Golem",type1="Rock",type2="Electric",nature=None,level=100,happiness=255,hp=80,atk=120,defense=130,spatk=55,spdef=65,speed=45,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Galvanize","Sturdy"]),item=random.choice(["Choice Scarf","Weakness Policy"])):
        if move is None:
            avmoves=["Stone Edge","Earthquake","Stealth Rock","Rock Blast","Thunderbolt","Explosion","Magnitude","Bulldoze"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Rapidash
class Rapidash(Pokemon2):
    "Rapidash"
    def __init__(self,name="Rapidash",type1="Fire",type2=None,nature=None,level=100,happiness=255,hp=65,atk=100,defense=70,spatk=80,spdef=80,speed=125,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Flash Fire","Reckless"]),item=random.choice(["Choice Band","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Fire Blast","Flamethrower","Flare Blitz","Inferno","Morning Sun","Sunny Day","High Horsepower"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                
#Slowbro
class Slowbro(Pokemon2):
    "Slowbro"
    def __init__(self,name="Slowbro",type1="Water",type2="Psychic",nature=None,level=100,happiness=255,hp=95,atk=75,defense=110,spatk=100,spdef=80,speed=30,hpev=0,atkev=0,defev=252,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Regenerator",item=random.choice(["Colbur Berry","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Hidden Power","Ice Beam","Slack Off","Psychic","Flamethrower","Hydro Pump","Thunderbolt","Iron Defense","Rain Dance","Rest"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Mega Slowbro
class MSlowbro(Pokemon2):
    "Mega Slowbro"
    def __init__(self,name="Mega Slowbro",type1="Water",type2="Psychic",nature=None,level=100,happiness=255,hp=95,atk=75,defense=180,spatk=130,spdef=80,speed=30,hpev=0,atkev=0,defev=252,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Regenerator",item="Slowbronite"):
        if move is None:
            avmoves=["Hidden Power","Ice Beam","Slack Off","Psychic","Flamethrower","Hydro Pump","Thunderbolt","Iron Defense","Body Press","Rest"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                   
#Dodrio
class Dodrio(Pokemon2):
    "Dodrio"
    def __init__(self,name="Dodrio",type1="Normal",type2="Flying",nature=None,level=100,happiness=255,hp=60,atk=110,defense=70,spatk=60,spdef=60,speed=110,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Rock Head",item=random.choice(["Choice Scarf","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Close Combat","Brave Bird","Roost","Sky Attack","High Jump Kick"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Muk
class Muk(Pokemon2):
    "Muk"
    def __init__(self,name="Muk",type1="Poison",type2=None,nature=None,level=100,happiness=255,hp=105,atk=105,defense=75,spatk=65,spdef=100,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Poison Touch","Regenerator"]),item=random.choice(["Black Sludge","Shuca Berry","Payapa Berry"])):
        if move is None:
            avmoves=["Poison Jab","Acid Armor","Psychic","Toxic","Sludge Bomb","Venoshock","Toxic Spikes"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                       
#Cloyster
class Cloyster(Pokemon2):
    "Cloyster"
    def __init__(self,name="Cloyster",type1="Water",type2="Ice",nature=None,level=100,happiness=255,hp=50,atk=95,defense=180,spatk=85,spdef=45,speed=70,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Skill Link",item=random.choice(["Focus Sash","King's Rock"])):
        if move is None:
            avmoves=["Ice Beam","Rock Blast","Icicle Spear","Shell Smash","Hydro Pump","Pin Missile","Hail"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                               
#Gengar
class Gengar(Pokemon2):
    "Gengar"
    def __init__(self,name="Gengar",type1="Ghost",type2="Poison",nature=None,level=100,happiness=255,hp=60,atk=65,defense=60,spatk=130,spdef=75,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Levitate",item="Black Sludge"):
        if move is None:
            avmoves=["Hidden Power","Ice Beam","Dazzling Gleam","Psychic","Shadow Ball","Dark Pulse","Thunderbolt","Nasty Plot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Mega Gengar
class MGengar(Pokemon2):
    "Mega Gengar"
    def __init__(self,name="Mega Gengar",type1="Ghost",type2="Poison",nature=None,level=100,happiness=255,hp=60,atk=65,defense=80,spatk=170,spdef=95,speed=130,hpev=0,atkev=0,defev=0,spatkev=253,spdefev=0,speedev=252,maxiv="No",move=None, ability="Shadow Tag",item="Gengarite"):
        if move is None:
            avmoves=["Hidden Power","Ice Beam","Dazzling Gleam","Psychic","Shadow Ball","Dark Pulse","Thunderbolt","Nasty Plot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Exeggutor
class Exeggutor(Pokemon2):
    "Exeggutor"
    def __init__(self,name="Exeggutor",type1="Grass",type2="Psychic",nature=None,level=100,happiness=255,hp=95,atk=95,defense=85,spatk=125,spdef=75,speed=55,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Chlorophyll",item=random.choice(["Lum Berry","Leftovers"])):
        if move is None:
            avmoves=["Hidden Power","Giga Drain","Sunny Day","Psychic","Solar Beam","Egg Bomb","Leech Seed","Morning Sun","Light Screen"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)             
#Alolan Exeggutor
class AExeggutor(Pokemon2):
    "Alolan Exeggutor"
    def __init__(self,name="Alolan Exeggutor",type1="Grass",type2="Dragon",nature=None,level=100,happiness=255,hp=95,atk=105,defense=85,spatk=125,spdef=75,speed=45,hpev=0,atkev=252,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Chlorophyll",item="Leftovers"):
        if move is None:
            avmoves=["Sunny Day","Egg Bomb","Psychic","Solar Beam","Dragon Hammer","Zen Headbutt"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Alolan Muk
class AMuk(Pokemon2):
    "Alolan Muk"
    def __init__(self,name="Alolan Muk",type1="Poison",type2="Dark",nature=None,level=100,happiness=255,hp=105,atk=105,defense=75,spatk=65,spdef=100,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Power of Alchemy","Poison Touch"]),item="Black Sludge"):
        if move is None:
            avmoves=["Sludge Bomb","Toxic","Poison Jab","Venoshock","Smocksceen","Toxic Spikes"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Hitmonlee
class Hitmonlee(Pokemon2):
    "Hitmonlee"
    def __init__(self,name="Hitmonlee",type1="Fighting",type2=None,nature=None,level=100,happiness=255,hp=50,atk=120,defense=53,spatk=35,spdef=110,speed=87,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Reckless","Limber"]),item=random.choice(["Choice Band","Assault Vest"])):
        if move is None:
            avmoves=["Blaze Kick","High Jump Kick","Superpower","Pyro Ball","Low Kick","Close Combat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Hitmonchan
class Hitmonchan(Pokemon2):
    "Hitmonchan"
    def __init__(self,name="Hitmonchan",type1="Fighting",type2=None,nature=None,level=100,happiness=255,hp=50,atk=115,defense=79,spatk=35,spdef=110,speed=76,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Iron Fist",item=random.choice(["Assault Vest","Choice Band"])):
        if move is None:
            avmoves=["Ice Punch","Thunder Punch","Mach Punch","Fire Punch","Dizzy Punch","Dynamic Punch"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Weezing
class Weezing(Pokemon2):
    "Weezing"
    def __init__(self,name="Weezing",type1="Poison",type2=None,nature=None,level=100,happiness=255,hp=65,atk=90,defense=120,spatk=85,spdef=70,speed=60,hpev=0,atkev=0,defev=252,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Levitate",item=random.choice(["Black Sludge","Rocky Helmet"])):
        if move is None:
            avmoves=["Sludge Bomb","Toxic","Poison Jab","Venoshock","Explosion","Toxic Spikes"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)              
#Kangaskhan
class Kangaskhan(Pokemon2):
    "Kangaskhan"
    def __init__(self,name="Kangaskhan",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=105,atk=95,defense=80,spatk=40,spdef=80,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Scrappy",item=random.choice(["Silk Scarf","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Crunch","Body Slam","Fake Out","Power-up Punch","Earthquake"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Mega Kangaskhan
class MKangaskhan(Pokemon2):
    "Mega Kangaskhan"
    def __init__(self,name="Mega Kangaskhan",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=105,atk=125,defense=100,spatk=60,spdef=100,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Parental Bond",item="Kangaskhanite"):
        if move is None:
            avmoves=["Crunch","Body Slam","Fake Out","Power-up Punch","Earthquake"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)     
#Starmie
class Starmie(Pokemon2):
    "Starmie"
    def __init__(self,name="Starmie",type1="Water",type2="Psychic",nature=None,level=100,happiness=255,hp=60,atk=75,defense=85,spatk=100,spdef=85,speed=115,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Natural Cure",item="Life Orb"):
        if move is None:
            avmoves=["Hidden Power","Ice Beam","Scald","Psychic","Surf","Hydro Pump","Thunderbolt","Flip Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Pinsir
class Pinsir(Pokemon2):
    "Pinsir"
    def __init__(self,name="Pinsir",type1="Bug",type2=None,nature=None,level=100,happiness=255,hp=65,atk=125,defense=100,spatk=55,spdef=70,speed=85,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Moxie",item="Life Orb"):
        if move is None:
            avmoves=["Megahorn","Return","Brick Break","Close Combat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Mega Pinsir
class MPinsir(Pokemon2):
    "Mega Pinsir"
    def __init__(self,name="Mega Pinsir",type1="Bug",type2="Flying",nature=None,level=100,happiness=255,hp=65,atk=155,defense=120,spatk=65,spdef=90,speed=105,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Aerilate",item="Pinsirite"):
        if move is None:
            avmoves=["Double-Edge","Megahorn","Return","Brick Break","Close Combat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Tauros
class Tauros(Pokemon2):
    "Tauros"
    def __init__(self,name="Tauros",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=75,atk=100,defense=95,spatk=70,spdef=70,speed=110,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Intimidate","Sheer Force"]),item="Life Orb"):
        if move is None:
            avmoves=["Double-Edge","Strength","Earthquake","Drill Run","Head Smash","Megahorn","Rest"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Gyarados
class Gyarados(Pokemon2):
    "Gyarados"
    def __init__(self,name="Gyarados",type1="Water",type2="Flying",nature=None,level=100,happiness=255,hp=95,atk=125,defense=79,spatk=60,spdef=100,speed=81,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Intimidate","Moxie"]),item=random.choice(["Mystic Water","Heavy-Duty Boots","Lum Berry"])):
        if move is None:
            avmoves=["Crunch","Waterfall","Dragon Dance","Earthquake","Aqua Tail","Ice Fang","Power Whip"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Mega Gyarados
class MGyarados(Pokemon2):
    "Mega Gyarados"
    def __init__(self,name="Mega Gyarados",type1="Water",type2="Dark",nature=None,level=100,happiness=255,hp=95,atk=155,defense=109,spatk=70,spdef=130,speed=81,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Mold Breaker",item="Gyaradosite"):
        if move is None:
            avmoves=["Crunch","Waterfall","Dragon Dance","Earthquake","Aqua Tail","Ice Fang"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Lapras
class Lapras(Pokemon2):
    "Lapras"
    def __init__(self,name="Lapras",type1="Water",type2="Ice",nature=None,level=100,happiness=255,hp=130,atk=85,defense=80,spatk=85,spdef=95,speed=60,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Water Absorb",item=random.choice(["Choice Specs","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Hidden Power","Ice Beam","Hydro Pump","Thunderbolt","Surf","Hail","Rain Dance"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)

#Omastar
class Omastar(Pokemon2):
    "Omastar"
    def __init__(self,name="Omastar",type1="Rock",type2="Water",nature=None,level=100,happiness=255,hp=70,atk=60,defense=125,spatk=115,spdef=70,speed=55,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Shell Armor",item=random.choice(["Power Herb","Mystic Water"])):
        if move is None:
            avmoves=["Hidden Power","Ice Beam","Hydro Pump","Ancient Power","Rock Blast","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)             
#Kabutops
class Kabutops(Pokemon2):
    "Kabutops"
    def __init__(self,name="Kabutops",type1="Rock",type2="Water",nature=None,level=100,happiness=255,hp=60,atk=115,defense=105,spatk=65,spdef=70,speed=80,hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Swift Swim",item=random.choice(["Choice Band","Life Orb"])):
        if move is None:
            avmoves=["Protect","Liquidation","Hydro Pump","Rock Slide","Stone Edge","Flip Turn","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                  
#Aerodactyl
class Aerodactyl (Pokemon2):
    "Aerodactyl"
    def __init__(self,name="Aerodactyl",type1="Rock",type2="Flying",nature=None,level=100,happiness=255,hp=80,atk=105,defense=65,spatk=60,spdef=75,speed=130,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Rock Head",item=random.choice(["Flying Gem","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Protect","Ancient Power","Stone Edge","Rock Slide","Brave Bird","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)              
#Mega  Aerodactyl
class MAerodactyl (Pokemon2):
    "Mega Aerodactyl"
    def __init__(self,name="Mega Aerodactyl",type1="Rock",type2="Flying",nature=None,level=100,happiness=255,hp=80,atk=135,defense=85,spatk=70,spdef=95,speed=150,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Tough Claws",item="Aerodactylite"):
        if move is None:
            avmoves=["Protect","Ancient Power","Stone Edge","Rock Slide","Brave Bird","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)    
#Snorlax
class Snorlax(Pokemon2):
    "Snorlax"
    def __init__(self,name="Snorlax",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=160,atk=110,defense=65,spatk=65,spdef=110,speed=30,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability="Thick Fat",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hidden Power","Ice Beam","Body Slam","Thunder Punch","Double-Edge","Hyper Beam","Giga Impact","Rest"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Articuno
class Articuno    (Pokemon2):
    "Articuno"
    def __init__(self,name="Articuno",type1="Ice",type2="Flying",nature=None,level=100,happiness=255,hp=90,atk=70,defense=100,spatk=95,spdef=125,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Snow Warning",item=random.choice(["Choice Specs","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Protect","Hidden Power","Ice Beam","Blizzard","Freeze-Dry","Brave Bird","Sky Attack","Roost"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      
#Zapdos
class Zapdos(Pokemon2):
    "Zapdos"
    def __init__(self,name="Zapdos",type1="Electric",type2="Flying",nature=None,level=100,happiness=255,hp=90,atk=90,defense=85,spatk=125,spdef=90,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Drizzle",item=random.choice(["Choice Specs","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Protect","Hidden Power","Thunder","Brave Bird","Thunderbolt","Sky Attack","Roost","Thunder Wave"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)             
#Moltres
class Moltres(Pokemon2):
    "Moltres"
    def __init__(self,name="Moltres",type1="Fire",type2="Flying",nature=None,level=100,happiness=255,hp=90,atk=100,defense=90,spatk=125,spdef=85,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Drought",item=random.choice(["Choice Specs","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Protect","Hidden Power","Flamethrower","Hurricane","Heat Wave","Sky Attack","Brave Bird","Fire Blast","Roost","Solar Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Dragonite
class Dragonite(Pokemon2):
    "Dragonite"
    def __init__(self,name="Dragonite",type1="Dragon",type2="Flying",nature=None,level=100,happiness=255,hp=91,atk=134,defense=95,spatk=100,spdef=100,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Multiscale",item=random.choice(["Weakness Policy","Leftovers","Choice Band","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Protect","Hidden Power","Ice Beam","Hydro Pump","Thunderbolt","Surf","Dragon Claw","Double-Edge","Thunder Wave"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Mewtwo
class Mewtwo(Pokemon2):
    "Mewtwo"
    def __init__(self,name="Mewtwo",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=106,atk=110,defense=90,spatk=154,spdef=90,speed=130,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Pressure",item=random.choice(["Expert Belt","Life Orb"])):
        if move is None:
            avmoves=["Protect","Hidden Power","Psystrike","Shadow Ball","Dark Pulse","Ice Beam","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Mew
class Mew(Pokemon2):
    "Mew"
    def __init__(self,name="Mew",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=100,atk=100,defense=100,spatk=100,spdef=100,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Synchronize",item="Leftovers"):
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
    def __init__(self,name="Meganium",type1="Grass",type2="Fairy",nature=None,level=100,happiness=255,hp=80,atk=72,defense=100,spatk=93,spdef=100,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Grassy Surge",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hidden Power","Leaf Storm","Moonblast","Dazzling Gleam","Synthesis","Leech Seed","Solar Beam","Frenzy Plant","Light Screen"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Typhlosion
class Typhlosion(Pokemon2):
    "Typhlosion"
    def __init__(self,name="Typhlosion",type1="Fire",type2=None,nature=None,level=100,happiness=255,hp=78,atk=84,defense=78,spatk=109,spdef=85,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Flash Fire",item="Choice Specs"):
        if move is None:
            avmoves=["Protect","Hidden Power","Earth Power","Fire Blast","Lava Plume","Eruption","Focus Blast","Blast Burn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Feraligatr
class Feraligatr(Pokemon2):
    "Feraligatr"
    def __init__(self,name="Feraligatr",type1="Water",type2="Dragon",nature=None,level=100,happiness=255,hp=85,atk=105,defense=100,spatk=79,spdef=83,speed=78,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Sheer Force",item=random.choice(["Choice Band","Life Orb"])):
        if move is None:
            avmoves=["Protect","Ice Beam","Hydro Pump","Liquidation","Dragon Claw","Focus Blast","Hydro Cannon"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Vaporeon
class Vaporeon(Pokemon2):
    "Vaporeon"
    def __init__(self,name="Vaporeon",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=130,atk=65,defense=60,spatk=110,spdef=95,speed=65,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=252,speedev=0,maxiv="No",move=None, ability="Water Absorb",item=random.choice(["Leftovers","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Protect","Hidden Power","Ice Beam","Hydro Pump","Acid Armor","Surf","Rain Dance","Flip Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                   
#Jolteon
class Jolteon(Pokemon2):
    "Jolteon"
    def __init__(self,name="Jolteon",type1="Electric",type2=None,nature=None,level=100,happiness=255,hp=65,atk=65,defense=60,spatk=110,spdef=95,speed=130,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Volt Absorb",item=random.choice(["Choice Specs","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Protect","Hidden Power","Volt Switch","Thunder","Thunderbolt","Shadow Ball","Thunder Wave"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
               
#Flareon
class Flareon(Pokemon2):
    "Flareon"
    def __init__(self,name="Flareon",type1="Fire",type2=None,nature=None,level=100,happiness=255,hp=65,atk=130,defense=60,spatk=95,spdef=110,speed=65,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Flash Fire","Guts"]),item=random.choice(["Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Protect","Flare Blitz","Fire Blast","Flame Charge","Last Resort","Will-O-Wisp"]
            moves=moveset(avmoves)
        else:
            moves=move
        if ability=="Guts":
            item="Toxic Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)  
#Crobat
class Crobat(Pokemon2):
    "Crobat"
    def __init__(self,name="Crobat",type1="Poison",type2="Flying",nature=None,level=100,happiness=255,hp=85,atk=90,defense=80,spatk=90,spdef=80,speed=130,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Infiltrator",item=random.choice(["Black Sludge","Heavy-Duty Boots"])):
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
    def __init__(self,name="Ampharos",type1="Electric",type2=None,nature=None,level=100,happiness=255,hp=90,atk=75,defense=85,spatk=115,spdef=90,speed=55,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=252,speedev=0,maxiv="No",move=None, ability="Static",item=random.choice(["Life Orb","Leftovers"])):
        if move is None:
            avmoves=["Protect","Hidden Power","Signal Beam","Power Gem","Thunderbolt","Discharge","Thunder Wave","Focus Blast","Light Screen","Reflect"]
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
    def __init__(self,name="Azumarill",type1="Water",type2="Fairy",nature=None,level=100,happiness=255,hp=100,atk=50,defense=80,spatk=60,spdef=80,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Huge Power",item=random.choice(["Choice Specs","Sitrus Berry"])):
        if move is None:
            avmoves=["Protect","Hidden Power","Ice Beam","Aqua Jet","Play Rough","Liquidation","Belly Drum"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)       
#Politoed
class Politoed(Pokemon2):
    "Politoed"
    def __init__(self,name="Politoed",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=90,atk=75,defense=75,spatk=90,spdef=100,speed=70,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability=random.choice(["Drizzle","Damp"]),item=random.choice(["Choice Specs","Damp Rock"])):
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
            avmoves=["Protect","Hidden Power","Psychic","Shadow Ball","Dazzling Gleam","Morning Sun","Light Screen"]
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
            avmoves=["Protect","Iron Tail","Gyro Ball","Earthquake","Stone Edge","Rock Slide","Toxic","Body Press","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Mega Steelix
class MSteelix(Pokemon2):
    "Mega Steelix"
    def __init__(self,name="Mega Steelix",type1="Steel",type2="Ground",nature=None,level=100,happiness=255,hp=75,atk=85,defense=200,spatk=55,spdef=65,speed=30,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Inner Focus",item="Steelixite"):
        if move is None:
            avmoves=["Protect","Iron Tail","Gyro Ball","Earthquake","Stone Edge","Rock Slide","Toxic","Body Press","Stealth Rock"]
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
    def __init__(self,name="Skarmory",type1="Steel",type2="Flying",nature=None,level=100,happiness=255,hp=65,atk=80,defense=140,spatk=40,spdef=70,speed=70,hpev=252,atkev=0,defev=252,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Sturdy",item=random.choice(["Leftovers","Rocky Helmet"])):
        if move is None:
            avmoves=["Protect","Roost","Brave Bird","Stealth Rock","Whirlwind","Steel Wing","Body Press"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Houndoom
class Houndoom(Pokemon2):
    "Houndoom"
    def __init__(self,name="Houndoom",type1="Dark",type2="Fire",nature=None,level=100,happiness=255,hp=75,atk=90,defense=50,spatk=110,spdef=80,speed=95,hpev=0,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=252,maxiv="No",move=None, ability="Flash Fire",item="Life Orb"):
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
    def __init__(self,name="Tyranitar",type1="Rock",type2="Dark",nature=None,level=100,happiness=255,hp=100,atk=134,defense=110,spatk=95,spdef=100,speed=61,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Sand Stream",item=random.choice(["Chople Berry","Weakness Policy"])):
        if move is None:
            avmoves=["Protect","Crunch","Earthquake","Stone Edge","Rock Slide","Hyper Beam","Dragon Dance","Giga Impact","Stealth Rock"]
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
    def __init__(self,name="Raikou",type1="Electric",type2=None,nature=None,level=100,happiness=255,hp=90,atk=85,defense=75,spatk=115,spdef=100,speed=115,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Inner Focus",item=random.choice(["Leftovers","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Protect","Crunch","Thunder","Thunderbolt","Wild Charge","Hyper Beam","Rain Dance","Thunder Wave","Extreme Speed","Reflect"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Entei
class Entei(Pokemon2):
    "Entei"
    def __init__(self,name="Entei",type1="Fire",type2=None,nature=None,level=100,happiness=255,hp=115,atk=115,defense=85,spatk=90,spdef=75,speed=100,hpev=0,atkev=115,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Inner Focus",item=random.choice(["Choice Band","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Protect","Crunch","Fire Blast","Sacred Fire","Flamethrower","Hyper Beam","Flare Blitz","Eruption","Extreme Speed"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Suicune
class Suicune(Pokemon2):
    "Suicune"
    def __init__(self,name="Suicune",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=100,atk=75,defense=115,spatk=90,spdef=115,speed=85,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Inner Focus",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Crunch","Surf","Hydro Pump","Recover","Hyper Beam","Rain Dance","Scald","Extreme Speed","Light Screen"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Lugia
class Lugia(Pokemon2):
    "Lugia"
    def __init__(self,name="Lugia",type1="Psychic",type2="Flying",nature=None,level=100,happiness=255,hp=106,atk=90,defense=130,spatk=90,spdef=154,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Multiscale",item=random.choice(["Choice Specs","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Protect","Crunch","Surf","Hydro Pump","Recover","Hyper Beam","Rain Dance","Aeroblast","Psychic","Extrasensory"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Ho-Oh
class Hooh(Pokemon2):
    "Ho-Oh"
    def __init__(self,name="Ho-Oh",type1="Fire",type2="Flying",nature=None,level=100,happiness=255,hp=106,atk=130,defense=90,spatk=110,spdef=154,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Regenerator",item=random.choice(["Choice Specs","Heavy-Duty Boots"])):
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
            avmoves=["Protect","Soft Boiled","Toxic","Seismic Toss","Light Screen","Reflect","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)  
#Deoxys
class Deoxys(Pokemon2):
    "Deoxys"
    def __init__(self,name="Deoxys",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=50,atk=150,defense=50,spatk=150,spdef=50,speed=150,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Pressure",item="Kasib Berry"):
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
            avmoves=["Protect","Psycho Boost","Toxic","Psychic","Shadow Ball","Dark Pulse","Recover","Thunder Wave","Toxic Spikes","Stealth Rock","Extreme Speed"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)   
#Defense Deoxys
class DDeoxys(Pokemon2):
    "Defense Deoxys"
    def __init__(self,name="Defense Deoxys",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=50,atk=70,defense=160,spatk=70,spdef=160,speed=90,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=4,maxiv="No",move=None, ability="Pressure",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Psycho Boost","Toxic","Psychic","Shadow Ball","Dark Pulse","Recover","Thunder Wave","Toxic Spikes","Stealth Rock"]
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
    def __init__(self,name="Rayquaza",type1="Dragon",type2="Flying",nature=None,level=100,happiness=255,hp=105,atk=150,defense=90,spatk=150,spdef=90,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Air Lock",item="Life Orb"):
        if move is None:
            avmoves=["Protect","Crunch","Hyper Beam","Dragon Ascent","Dragon Dance","Extreme Speed","Draco Meteor"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)   
#Mega Rayquaza     
class MRayquaza(Pokemon2):
    "Mega Rayquaza"
    def __init__(self,name="Mega Rayquaza",type1="Dragon",type2="Flying",nature=None,level=100,happiness=255,hp=105,atk=180,defense=100,spatk=180,spdef=100,speed=115,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Delta Stream",item="Life Orb"):
        if move is None:
            avmoves=["Protect","Crunch","Hyper Beam","Dragon Ascent","Dragon Dance","Extreme Speed","Draco Meteor"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#Sceptile
class Sceptile(Pokemon2):
    "Sceptile"
    def __init__(self,name="Sceptile",type1="Grass",type2="Dragon",nature=None,level=100,happiness=255,hp=70,atk=105,defense=65,spatk=85,spdef=86,speed=120,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Overgrow",item="Life Orb"):
        if move is None:
            avmoves=["Protect","Leaf Blade","Hyper Beam","Leaf Storm","Dragon Dance","Dragon Pulse","Draco Meteor","Focus Blast","Energy Ball","Frenzy Plant"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)     
#Mega Sceptile
class MSceptile(Pokemon2):
    "Mega Sceptile"
    def __init__(self,name="Mega Sceptile",type1="Grass",type2="Dragon",nature=None,level=100,happiness=255,hp=70,atk=135,defense=75,spatk=110,spdef=85,speed=145,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Lightning Rod",item="Sceptilite"):
        if move is None:
            avmoves=["Protect","Leaf Blade","Dragon Dance","Dragon Pulse","Draco Meteor","Focus Blast", "Energy Ball","X-Scissor"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#Blaziken
class Blaziken(Pokemon2):
    "Blaziken"
    def __init__(self,name="Blaziken",type1="Fire",type2="Fighting",nature=None,level=100,happiness=255,hp=80,atk=120,defense=70,spatk=110,spdef=70,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Speed Boost",item=random.choice(["Life Orb","Leftovers"])):
        if move is None:
            avmoves=["Protect","Overheat","High Jump Kick","Sky Uppercut","Blaze Kick","Brave Bird","Flare Blitz","Focus Blast","Blast Burn"]
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
            avmoves=["Protect","Liquidation","Earthquake","Stone Edge","Power-up Punch","Waterfall","Ice Punch","Hydro Cannon","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Mega Swampert
class MSwampert(Pokemon2):
    "Mega Swampert"
    def __init__(self,name="Mega Swampert",type1="Water",type2="Ground",nature=None,level=100,happiness=255,hp=100,atk=150,defense=110,spatk=95,spdef=110,speed=70,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Swift Swim",item="Swampertite"):
        if move is None:
            avmoves=["Protect","Liquidation","Earthquake","Stone Edge","Power-up Punch","Waterfall","Ice Punch","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                               
#Ludicolo
class Ludicolo(Pokemon2):
    "Ludicolo"
    def __init__(self,name="Ludicolo",type1="Grass",type2="Water",nature=None,level=100,happiness=255,hp=80,atk=70,defense=70,spatk=100,spdef=100,speed=70,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Swift Swim","Dancer"]),item="Life Orb"):
        if move is None:
            avmoves=["Protect","Ice Beam","Giga Drain","Surf","Hydro Pump","Rain Dance","Focus Blast","Energy Ball"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Shiftry
class Shiftry(Pokemon2):
    "Shiftry"
    def __init__(self,name="Shiftry",type1="Grass",type2="Dark",nature=None,level=100,happiness=255,hp=90,atk=120,defense=60,spatk=110,spdef=60,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Chlorophyll",item=random.choice(["Life Orb","Dark Gem"])):
        if move is None:
            avmoves=["Protect","Sunny Day","Giga Drain","Leaf Storm","Hurricane","Leaf Tornado","Leech Seed","Focus Blast","Explosion","Parting Shot","Sucker Punch"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Swellow
class Swellow(Pokemon2):
    "Swellow"
    def __init__(self,name="Swellow",type1="Normal",type2="Flying",nature=None,level=100,happiness=255,hp=60,atk=85,defense=60,spatk=75,spdef=50,speed=125,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Guts","Aerilate"]),item=random.choice(["Choice Specs","Heavy-Duty Boots","Flying Gem"])):
        if move is None:
            avmoves=["Protect","Roost","Brave Bird","Facade","Hurricane","Boomburst"]
            moves=moveset(avmoves)
        else:
            moves=move
        if ability=="Guts":
            item="Flame Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)   
#Pelipper
class Pelipper(Pokemon2):
    "Pelipper"
    def __init__(self,name="Pelipper",type1="Water",type2="Flying",nature=None,level=100,happiness=255,hp=60,atk=50,defense=100,spatk=95,spdef=70,speed=65,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Drizzle",item=random.choice(["Damp Rock","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Protect","Roost","Surf","Ice Beam","Hurricane","Hydro Pump"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#Gardevoir
class Gardevoir(Pokemon2):
    "Gardevoir"
    def __init__(self,name="Gardevoir",type1="Psychic",type2="Fairy",nature=None,level=100,happiness=255,hp=68,atk=65,defense=65,spatk=125,spdef=115,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Trace",item=random.choice(["Choice Specs","Life Orb","Leftovers"])):
        if move is None:
            avmoves=["Protect","Recover","Dazzling Gleam","Moonblast","Psychic","Shadow Ball","Focus Blast","Trick Room","Misty Terrain"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)     
#Mega Gardevoir
class MGardevoir(Pokemon2):
    "Mega Gardevoir"
    def __init__(self,name="Mega Gardevoir",type1="Psychic",type2="Fairy",nature=None,level=100,happiness=255,hp=68,atk=85,defense=65,spatk=165,spdef=135,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Pixilate",item="Gardevoirite"):
        if move is None:
            avmoves=["Protect","Recover","Dazzling Gleam","Moonblast","Psychic","Shadow Ball","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)               
#Breloom
class Breloom(Pokemon2):
    "Breloom"
    def __init__(self,name="Breloom",type1="Grass",type2="Fighting",nature=None,level=100,happiness=255,hp=60,atk=130,defense=80,spatk=60,spdef=60,speed=70,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Poison Heal",item="Toxic Orb"):
        if move is None:
            avmoves=["Protect","Dynamic Punch","Mach Punch","Spore","Sky Uppercut","Bullet Seed","Seed Bomb","Leech Seed","Misty Terrain"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Slaking
class Slaking(Pokemon2):
    "Slaking"
    def __init__(self,name="Slaking",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=150,atk=160,defense=100,spatk=95,spdef=65,speed=10,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Truant",item="Leftovers",truant=False):
        if move is None:
            avmoves=["Protect","Dynamic Punch","Hyper Beam","Double-Edge","Sky Uppercut","Return","Slack Off","Rest"]
            moves=moveset(avmoves)
        else:
            moves=move
        self.truant=truant
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Hariyama
class Hariyama(Pokemon2):
    "Hariyama"
    def __init__(self,name="Hariyama",type1="Fighting",type2=None,nature=None,level=100,happiness=255,hp=144,atk=120,defense=60,spatk=40,spdef=60,speed=50,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Guts",item="Flame Orb"):
        if move is None:
            avmoves=["Protect","Dynamic Punch","Force Palm","Sky Uppercut","Arm Thrust","Belly Drum","Knock Off","Facade"]
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
            avmoves=["Protect","Iron Head","Play Rough","Crunch","Sucker Punch","Iron Defense","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Aggron
class Aggron(Pokemon2):
    "Aggron"
    def __init__(self,name="Aggron",type1="Steel",type2="Rock",nature=None,level=100,happiness=255,hp=70,atk=110,defense=180,spatk=60,spdef=60,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Rock Head","Sturdy"]),item=random.choice(["Choice Band","Leftovers"])):
        if move is None:
            avmoves=["Protect","Iron Head","Stone Edge","Crunch","Earthquake","Iron Defense","Hyper Beam","Flash Cannon","Body Press","Stealth Rock"]
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
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Mega Medicham
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
    def __init__(self,name="Torkoal",type1="Fire",type2=None,nature=None,level=100,happiness=255,hp=70,atk=75,defense=140,spatk=95,spdef=70,speed=20,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Drought",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Lava Plume","Thunder Wave","Flamethrower","Toxic","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                       
#Mega Manectric
class MManectric(Pokemon2):
    "Mega Manectric"
    def __init__(self,name="Mega Manectric",type1="Electric",type2=None,nature=None,level=100,happiness=255,hp=70,atk=75,defense=80,spatk=135,spdef=80,speed=135,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Intimidate",item="Manectite"):
        if move is None:
            avmoves=["Protect","Volt Switch","Thunder","Crunch","Thunderbolt","Wild Charge","Hyper Beam","Thunder Wave","Flamethrower","Electric Terrain"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Sharpedo
class Sharpedo(Pokemon2):
    "Sharpedo"
    def __init__(self,name="Sharpedo",type1="Water",type2="Dark",nature=None,level=100,happiness=255,hp=70,atk=120,defense=40,spatk=95,spdef=40,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Speed Boost",item="Life Orb"):
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
            avmoves=["Protect","Flip Turn","Pin Missile","Crunch","Poison Jab","Barb Barrage","Dark Pulse","Double-Edge","Toxic Spikes","Stealth Rock"]
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
    def __init__(self,name="Mega Camerupt",type1="Fire",type2="Ground",nature=None,level=100,happiness=255,hp=90,atk=100,defense=110,spatk=145,spdef=115,speed=20,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Sheer Force",item="Cameruptite"):
        if move is None:
            avmoves=["Protect","Eruption","Earth Power","Lava Plume","Earthquake","Stone Edge","Fire Blast","Stealth Rock","Magnitude","Bulldoze"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item) 
#Camerupt
class Camerupt(Pokemon2):
    "Camerupt"
    def __init__(self,name="Camerupt",type1="Fire",type2="Ground",nature=None,level=100,happiness=255,hp=90,atk=100,defense=70,spatk=105,spdef=75,speed=40,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Solid Rock",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Eruption","Earth Power","Lava Plume","Earthquake","Stone Edge","Fire Blast","Will-O-Wisp","Stealth Rock","Magnitude","Bulldoze"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Arbok
class Arbok(Pokemon2):
    "Arbok"
    def __init__(self,name="Arbok",type1="Poison",type2="Dark",nature=None,level=100,happiness=255,hp=75,atk=85,defense=75,spatk=65,spdef=79,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Intimidate",item="Black Sludge"):
        if move is None:
            avmoves=["Protect","Venoshock","Earth Power","Poison Fang","Crunch","Gunk Shot","Belch"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Regirock
class Regirock(Pokemon2):
    "Regirock"
    def __init__(self,name="Regirock",type1="Rock",type2=None,nature=None,level=100,happiness=255,hp=80,atk=100,defense=200,spatk=50,spdef=100,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Clear Body","Solid Rock"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Zap Cannon","Earth Power","Hyper Beam","Earthquake","Stone Edge","Rock Slide","Explosion","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      
#Regice
class Regice(Pokemon2):
    "Regice"
    def __init__(self,name="Regice",type1="Ice",type2=None,nature=None,level=100,happiness=255,hp=80,atk=50,defense=100,spatk=100,spdef=200,speed=50,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Clear Body","Filter"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Ice Beam","Blizzard","Freeze-Dry","Hyper Beam","Zap Cannon","Hail","Explosion"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Registeel
class Registeel(Pokemon2):
    "Registeel"
    def __init__(self,name="Registeel",type1="Steel",type2=None,nature=None,level=100,happiness=255,hp=80,atk=75,defense=150,spatk=75,spdef=150,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Clear Body"]),item="Leftovers"):
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
            avmoves=["Protect","Hidden Power","Ice Beam","Psychic","Blizzard","Dark Pulse","Hail","Shadow Ball","Trick Room","Light Screen"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#Mamoswine
class Mamoswine(Pokemon2):
    "Mamoswine"
    def __init__(self,name="Mamoswine",type1="Ice",type2="Ground",nature=None,level=100,happiness=255,hp=110,atk=130,defense=80,spatk=70,spdef=60,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Thick Fat",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Ice Beam","Earthquake","Blizzard","Stone Edge","Hail","Icicle Crash","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)       
#Flygon
class Flygon(Pokemon2):
    "Flygon"
    def __init__(self,name="Flygon",type1="Ground",type2="Dragon",nature=None,level=100,happiness=255,hp=100,atk=100,defense=80,spatk=100,spdef=80,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Tinted Lens","Levitate"]),item="Leftovers"):
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
            avmoves=["Protect","Dragon Claw","Earthquake","Crunch","Brave Bird","Sky Attack","Moonblast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#Mega Altaria
class MAltaria(Pokemon2):
    "Mega Altaria"
    def __init__(self,name="Mega Altaria",type1="Dragon",type2="Fairy",nature=None,level=100,happiness=255,hp=85,atk=110,defense=110,spatk=110,spdef=105,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Pixilate",item="Altarianite"):
        if move is None:
            avmoves=["Protect","Dragon Claw","Earthquake","Crunch","Brave Bird","Sky Attack","Moonblast"]
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
            avmoves=["Protect","Boomburst","Hyper Beam","Crunch","Hyper Voice","Toxic","Double-Edge","Rest"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Lunatone
class Lunatone(Pokemon2):
    "Lunatone"
    def __init__(self,name="Lunatone",type1="Rock",type2="Psychic",nature=None,level=100,happiness=255,hp=70,atk=55,defense=65,spatk=105,spdef=85,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Levitate",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Ancient Power","Hyper Beam","Psychic","Power Gem","Moonblast","Stone Edge","Moonlight","Explosion","Trick Room","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Solrock
class Solrock(Pokemon2):
    "Solrock"
    def __init__(self,name="Solrock",type1="Rock",type2="Psychic",nature=None,level=100,happiness=255,hp=70,atk=105,defense=85,spatk=55,spdef=65,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Levitate",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Ancient Power","Hyper Beam","Psychic","Power Gem","Moonblast","Stone Edge","Morning Sun","Explosion","Trick Room","Solar Beam","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)              
#Whiscash
class Whiscash(Pokemon2):
    "Whiscash"
    def __init__(self,name="Whiscash",type1="Water",type2="Ground",nature=None,level=100,happiness=255,hp=110,atk=78,defense=73,spatk=76,spdef=71,speed=60,hpev=0,atkev=252,defev=252,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Oblivious",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Ancient Power","Ice Beam","Surf","Power Gem","Hydro Pump","Stone Edge","Earthquake","Rest","Magnitude"]
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
            avmoves=["Protect","Ancient Power","Hyper Beam","Psychic","Power Gem","Earth Power","Stone Edge","Explosion","Trick Room","Stealth Rock","Light Screen"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)    
#Cradily
class Cradily(Pokemon2):
    "Cradily"
    def __init__(self,name="Cradily",type1="Rock",type2="Grass",nature=None,level=100,happiness=255,hp=86,atk=81,defense=97,spatk=81,spdef=107,speed=43,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Storm Drain",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Ancient Power","Hyper Beam","Giga Drain","Sludge Bomb","Earth Power","Leech Seed","Energy Ball","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Armaldo
class Armaldo(Pokemon2):
    "Armaldo"
    def __init__(self,name="Armaldo",type1="Rock",type2="Bug",nature=None,level=100,happiness=255,hp=75,atk=125,defense=100,spatk=70,spdef=80,speed=45,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Swift Swim",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Ancient Power","Hyper Beam","X-Scissor","Rock Blast","Earth Power","Crush Claw","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Milotic
class Milotic(Pokemon2):
    "Milotic"
    def __init__(self,name="Milotic",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=95,atk=60,defense=84,spatk=100,spdef=125,speed=86,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Competitive","Marvel Scale"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Recover","Ice Beam","Surf","Rain Dance","Hydro Pump","Coil","Thunderbolt","Light Screen"]
            moves=moveset(avmoves)
        else:
            moves=move
        if ability=="Marvel Scale":
            item="Flame Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Farigarif
class Farigarif(Pokemon2):
    "Farigarif"
    def __init__(self,name="Farigarif",type1="Normal",type2="Psychic",nature=None,level=100,happiness=255,hp=80,atk=90,defense=74,spatk=120,spdef=75,speed=85,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Armor Tail",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Recover","Psychic","Crunch","Zen Headbutt","Assurance","Hypnosis","Shadow Ball","Trick Room","Light Screen","Reflect"]
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
    def __init__(self,name="Absol",type1="Dark",type2=None,nature=None,level=100,happiness=255,hp=75,atk=130,defense=70,spatk=85,spdef=70,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Super Luck","Justified"]),item=random.choice(["Life Orb","Choice Band","Black Glasses","Scope Lens"])):
        if move is None:
            avmoves=["Protect","Recover","Knock Off","Crunch","Psycho Cut","Assurance","Night Slash","Shadow Ball","Toxic","Sucker Punch","Close Combat","Swords Dance","Play Rough"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Mega Absol
class MAbsol(Pokemon2):
    "Mega Absol"
    def __init__(self,name="Mega Absol",type1="Dark",type2="Fairy",nature=None,level=100,happiness=255,hp=75,atk=150,defense=70,spatk=115,spdef=70,speed=125,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Magic Bounce",item="Absolite"):
        if move is None:
            avmoves=["Protect","Recover","Knock Off","Crunch","Psycho Cut","Assurance","Night Slash","Shadow Ball","Toxic","Sucker Punch","Close Combat","Swords Dance","Play Rough"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)             
#Mega Glalie
class MGlalie(Pokemon2):
    "Mega Glalie"
    def __init__(self,name="Mega Glalie",type1="Ice",type2=None,nature=None,level=100,happiness=255,hp=80,atk=135,defense=80,spatk=105,spdef=80,speed=120,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Refrigerate",item="Glalite"):
        if move is None:
            avmoves=["Protect","Recover","Earthquake","Crunch","Ice Beam","Blizzard","Freeze-Dry","Ice Fang","Toxic","Hail","Hyper Beam","Rain Dance","Icicle Crash"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
                                    
#Glalie
class Glalie(Pokemon2):
    "Glalie"
    def __init__(self,name="Glalie",type1="Ice",type2=None,nature=None,level=100,happiness=255,hp=80,atk=80,defense=80,spatk=100,spdef=80,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Inner Focus",item="Focus Sash"):
        if move is None:
            avmoves=["Protect","Recover","Earthquake","Crunch","Ice Beam","Blizzard","Freeze-Dry","Ice Fang","Toxic","Hail","Hyper Beam","Rain Dance","Shadow Ball"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Walrein
class Walrein(Pokemon2):
    "Walrein"
    def __init__(self,name="Walrein",type1="Ice",type2="Water",nature=None,level=100,happiness=255,hp=110,atk=80,defense=90,spatk=95,spdef=90,speed=65,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Thick Fat",item=random.choice(["Leftovers","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Protect","Slack Off","Surf","Crunch","Ice Beam","Blizzard","Freeze-Dry","Ice Fang","Rest","Hail","Hyper Beam","Earthquake","Icicle Spear","Iron Head","Swords Dance"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Huntail
class Huntail(Pokemon2):
    "Huntail"
    def __init__(self,name="Huntail",type1="Water",type2="Dark",nature=None,level=100,happiness=255,hp=55,atk=104,defense=105,spatk=94,spdef=75,speed=52,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Intimidate",item="White Herb"):
        if move is None:
            avmoves=["Protect","Crunch","Ice Beam","Blizzard","Liquidation","Ice Fang","Waterfall","Hydro Pump","Rain Dance","Shell Smash"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)       
#Gorebyss
class Gorebyss(Pokemon2):
    "Gorebyss"
    def __init__(self,name="Gorebyss",type1="Water",type2="Fairy",nature=None,level=100,happiness=255,hp=55,atk=84,defense=105,spatk=114,spdef=75,speed=52,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Regenerator",item="White Herb"):
        if move is None:
            avmoves=["Protect","Dazzling Gleam","Ice Beam","Blizzard","Moonblast","Ice Fang","Waterfall","Hydro Pump","Rain Dance","Shell Smash"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Relicanth
class Relicanth(Pokemon2):
    "Relicanth"
    def __init__(self,name="Relicanth",type1="Water",type2="Rock",nature=None,level=100,happiness=255,hp=100,atk=105,defense=130,spatk=45,spdef=65,speed=55,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Rock Head",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Liquidation","Ice Beam","Stone Edge","Rock Slide","Ice Fang","Waterfall","Hydro Pump","Rain Dance","Head Smash","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Salamence
class Salamence(Pokemon2):
    "Salamence"
    def __init__(self,name="Salamence",type1="Dragon",type2="Flying",nature=None,level=100,happiness=255,hp=95,atk=135,defense=80,spatk=110,spdef=80,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Intimidate","Moxie"]),item=random.choice(["Life Orb","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Protect","Stone Edge","Dragon Claw","Ice Beam","Flamethrower","Crunch","Zen Headbutt","Double-Edge","Hydro Pump","Earthquake","Dragon Dance","Roost"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      
#Mega Salamence
class MSalamence(Pokemon2):
    "Mega Salamence"
    def __init__(self,name="Mega Salamence",type1="Dragon",type2="Flying",nature=None,level=100,happiness=255,hp=95,atk=145,defense=130,spatk=120,spdef=90,speed=120,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Aerilate",item="Salamencite"):
        if move is None:
            avmoves=["Protect","Stone Edge","Dragon Claw","Ice Beam","Flamethrower","Crunch","Zen Headbutt","Double-Edge","Hydro Pump","Earthquake","Dragon Dance","Roost"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Metagross
class Metagross(Pokemon2):
    "Metagross"
    def __init__(self,name="Metagross",type1="Steel",type2="Psychic",nature=None,level=100,happiness=255,hp=80,atk=135,defense=130,spatk=95,spdef=90,speed=70,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Clear Body",item=random.choice(["Leftovers","Choice Band"])):
        if move is None:
            avmoves=["Protect","Stone Edge","Bullet Punch","Meteor Mash","Hyper Beam","Crunch","Zen Headbutt","Double-Edge","Iron Defense","Earthquake","Hammer Arm","Flash Cannon","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                    
#MegaMetagross
class MMetagross(Pokemon2):
    "Mega Metagross"
    def __init__(self,name="Mega Metagross",type1="Steel",type2="Psychic",nature=None,level=100,happiness=255,hp=80,atk=145,defense=150,spatk=105,spdef=110,speed=110,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Tough Claws",item="Metagrossite"):
        if move is None:
            avmoves=["Protect","Stone Edge","Bullet Punch","Meteor Mash","Hyper Beam","Crunch","Zen Headbutt","Double-Edge","Iron Defense","Earthquake","Hammer Arm","Flash Cannon","Fire Punch"]
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
    def __init__(self,name="Latios",type1="Dragon",type2="Psychic",nature=None,level=100,happiness=255,hp=80,atk=90,defense=80,spatk=130,spdef=110,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Levitate",item=random.choice(["Choice Scarf","Choice Specs"])):
        if move is None:
            avmoves=["Protect","Hyper Beam","Luster Purge","Zen Headbutt","Dragon Pulse","Psychic","Calm Mind","Ice Beam","Thunderbolt","Shadow Ball","Draco Meteor"]
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
    def __init__(self,name="Kyogre",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=100,atk=100,defense=90,spatk=150,spdef=140,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Drizzle",item=random.choice(["Choice Scarf","Choice Specs","Leftovers"])):
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
    def __init__(self,name="Groudon",type1="Ground",type2=None,nature=None,level=100,happiness=255,hp=100,atk=150,defense=140,spatk=100,spdef=90,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Drought",item=random.choice(["Choice Band","Leftovers","Lum Berry","Life Orb"])):
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
    def __init__(self,name="Torterra",type1="Grass",type2="Ground",nature=None,level=100,happiness=255,hp=95,atk=109,defense=105,spatk=75,spdef=85,speed=56,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Overgrow","Rock Head"]),item=random.choice(["Choice Band","Leftovers","Yache Berry"])):
        if move is None:
            avmoves=["Protect","Hyper Beam","Wood Hammer","Earthquake","Leaf Storm","Ancient Power","Swords Dance","Curse","Synthesis","Crunch","Giga Drain","Headlong Rush","Frenzy Plant","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)   
#Infernape
class Infernape(Pokemon2):
    "Infernape"
    def __init__(self,name="Infernape",type1="Fire",type2="Fighting",nature=None,level=100,happiness=255,hp=76,atk=110,defense=71,spatk=110,spdef=71,speed=113,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Blaze","Iron Fist"]),item=random.choice(["Choice Band","Focus Sash","Expert Belt","Life Orb"])):
        if move is None:
            avmoves=["Protect","Hyper Beam","Flare Blitz","Close Combat","Fire Blast","Mach Punch","Swords Dance","Power-up Punch","Overheat","Calm Mind","Flamethrower","Blast Burn","Stealth Rock","Raging Fury"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item) 
#Empoleon
class Empoleon(Pokemon2):
    "Empoleon"
    def __init__(self,name="Empoleon",type1="Water",type2="Steel",nature=None,level=100,happiness=255,hp=84,atk=86,defense=88,spatk=111,spdef=101,speed=60,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Torrent","Competitive"]),item=random.choice(["Leftovers","Shuca Berry","Chople Berry"])):
        if move is None:
            avmoves=["Protect","Hyper Beam","Surf","Flash Cannon","Hydro Pump","Liquidation","Wave Crash","Ice Beam","Steel Beam","Rest","Scald","Hydro Cannon","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Staraptor
class Staraptor(Pokemon2):
    "Staraptor"
    def __init__(self,name="Staraptor",type1="Normal",type2="Flying",nature=None,level=100,happiness=255,hp=85,atk=120,defense=70,spatk=50,spdef=60,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Intimidate","Reckless"]),item=random.choice(["Choice Scarf","Choice Band","Leftovers"])):
        if move is None:
            avmoves=["Protect","Final Gambit","Roost","Brave Bird","Close Combat","U-Turn","Giga Impact","Facade"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Luxray
class Luxray(Pokemon2):
    "Luxray"
    def __init__(self,name="Luxray",type1="Electric",type2="Dark",nature=None,level=100,happiness=255,hp=80,atk=120,defense=79,spatk=95,spdef=79,speed=70,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Intimidate","Guts"]),item="Life Orb"):
        if move is None:
            avmoves=["Protect","Wild Charge","Crunch","Thunder Wave","Play Rough","Electric Terrain"]
            moves=moveset(avmoves)
        else:
            moves=move
        if ability=="Guts":
            item="Flame Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#Roserade
class Roserade(Pokemon2):
    "Roserade"
    def __init__(self,name="Roserade",type1="Grass",type2="Poison",nature=None,level=100,happiness=255,hp=60,atk=70,defense=65,spatk=125,spdef=105,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Technician","Poison Point"]),item=random.choice(["Heavy-Duty Boots","Black Sludge","Rocky Helmet"])):
        if move is None:
            avmoves=["Protect","Weather Ball","Toxic","Sunny Day","Giga Drain","Energy Ball","Toxic Spikes","Grassy Terrain"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Rampardos
class Rampardos(Pokemon2):
    "Rampardos"
    def __init__(self,name="Rampardos",type1="Rock",type2=None,nature=None,level=100,happiness=255,hp=97,atk=165,defense=60,spatk=65,spdef=50,speed=58,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Sheer Force","Mold Breaker"]),item=random.choice(["Choice Scarf","Choice Band"])):
        if move is None:
            avmoves=["Protect","Head Smash","Iron Head","Crunch","Stone Edge"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                           
#Bastiodon
class Bastiodon(Pokemon2):
    "Bastiodon"
    def __init__(self,name="Bastiodon",type1="Rock",type2="Steel",nature=None,level=100,happiness=255,hp=60,atk=52,defense=168,spatk=47,spdef=138,speed=30,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Sturdy","Dauntless Shield"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Iron Defense","Iron Head","Crunch","Stone Edge"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Vespiquen
class Vespiquen(Pokemon2):
    "Vespiquen"
    def __init__(self,name="Vespiquen",type1="Bug",type2="Flying",nature=None,level=100,happiness=255,hp=85,atk=80,defense=102,spatk=80,spdef=102,speed=40,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Pressure",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Defense Order","Attack Order","Heal Order","Toxic"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                             #Gastrodon
class WGastrodon(Pokemon2):
    "Gastrodon"
    def __init__(self,name="West Sea Gastrodon",type1="Water",type2="Ground",nature=None,level=100,happiness=255,hp=111,atk=83,defense=68,spatk=92,spdef=82,speed=39,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Storm Drain",item=random.choice(["Leftovers","Rindo Berry","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Protect","Earth Power","Recover","Hydro Pump","Ice Beam","Stealth Rock","Light Screen","Reflect"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)  
#Gastrodon
class EGastrodon(Pokemon2):
    "Gastrodon"
    def __init__(self,name="East Sea Gastrodon",type1="Water",type2="Ground",nature=None,level=100,happiness=255,hp=111,atk=83,defense=68,spatk=92,spdef=82,speed=39,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Storm Drain",item=random.choice(["Leftovers","Rindo Berry","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Protect","Earth Power","Recover","Hydro Pump","Ice Beam","Stealth Rock","Light Screen","Reflect"]
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
    def __init__(self,name="Drifblim",type1="Ghost",type2="Flying",nature=None,level=100,happiness=255,hp=150,atk=80,defense=44,spatk=90,spdef=54,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Flare Boost",item="Flame Orb"):
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
            avmoves=["Protect","High Jump Kick","Return","Fake Out","Power-up Punch"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Mismagius
class Mismagius(Pokemon2):
    "Mismagius"
    def __init__(self,name="Mismagius",type1="Ghost",type2="Fairy",nature=None,level=100,happiness=255,hp=70,atk=60,defense=70,spatk=105,spdef=105,speed=105,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Levitate",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Psychic","Shadow Ball","Calm Mind","Thunderbolt","Dazzling Gleam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Purugly
class Purugly(Pokemon2):
    "Purugly"
    def __init__(self,name="Purugly",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=100,atk=82,defense=79,spatk=79,spdef=64,speed=112,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Thick Fat",item=random.choice(["Silk Scarf","Life Orb"])):
        if move is None:
            avmoves=["Protect","Sucker Punch","Play Rough","Body Slam","Double-Edge","Bulk Up"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)    
#Skuntank
class Skuntank(Pokemon2):
    "Skuntank"
    def __init__(self,name="Skuntank",type1="Poison",type2="Dark",nature=None,level=100,happiness=255,hp=103,atk=93,defense=67,spatk=91,spdef=61,speed=84,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Stench",item=random.choice(["Rocky Helmet","Black Sludge","Black Glasses","Choice Band","Choice Scarf"])):
        if move is None:
            avmoves=["Protect","Dark Pulse","Shadow Ball","Flamethrower","Belch","Sludge Wave","Sludge Bomb"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Honchkrow
class Honchkrow(Pokemon2):
    "Honchkrow"
    def __init__(self,name="Honchkrow",type1="Dark",type2="Flying",nature=None,level=100,happiness=255,hp=100,atk=125,defense=60,spatk=105,spdef=60,speed=71,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Super Luck",item=random.choice(["Scope Lens","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Protect","Night Slash","Shadow Ball","Drill Peck","Roost","Dark Pulse"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Spiritomb
class Spiritomb(Pokemon2):
    "Spiritomb"
    def __init__(self,name="Spiritomb",type1="Ghost",type2="Dark",nature=None,level=100,happiness=255,hp=50,atk=92,defense=108,spatk=92,spdef=108,speed=35,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Pressure",item=random.choice(["Choice Band","Leftovers"])):
        if move is None:
            avmoves=["Protect","Night Slash","Shadow Ball","Hypnosis","Nasty Plot","Dark Pulse"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#Garchomp
class Garchomp(Pokemon2):
    "Garchomp"
    def __init__(self,name="Garchomp",type1="Dragon",type2="Ground",nature=None,level=100,happiness=255,hp=108,atk=130,defense=95,spatk=80,spdef=85,speed=102,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Rough Skin",item=random.choice(["Life Orb","Yache Berry","Leftovers","Rocky Helmet"])):
        if move is None:
            avmoves=["Protect","Swords Dance","Earthquake","Dragon Claw","Stone Edge","Draco Meteor","Flamethrower","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Mega Garchomp
class MGarchomp(Pokemon2):
    "Mega Garchomp"
    def __init__(self,name="Mega Garchomp",type1="Dragon",type2="Ground",nature=None,level=100,happiness=255,hp=108,atk=170,defense=105,spatk=120,spdef=95,speed=102,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Sand Force",item="Garchompite"):
        if move is None:
            avmoves=["Protect","Swords Dance","Earthquake","Dragon Claw","Stone Edge","Draco Meteor","Flamethrower","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Lucario
class Lucario(Pokemon2):
    "Lucario"
    def __init__(self,name="Lucario",type1="Fighting",type2="Steel",nature=None,level=100,happiness=255,hp=70,atk=110,defense=70,spatk=115,spdef=70,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Inner Focus",item=random.choice(["Choice Band","Life Orb"])):
        if move is None:
            avmoves=["Protect","Meteor Mash","Aura Sphere","Dragon Pulse","Close Combat","Bullet Punch","Bone Rush","Extreme Speed"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Mega Lucario
class MLucario(Pokemon2):
    "Mega Lucario"
    def __init__(self,name="Mega Lucario",type1="Fighting",type2="Steel",nature=None,level=100,happiness=255,hp=70,atk=145,defense=88,spatk=140,spdef=70,speed=112,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Adaptability",item="Lucarionite"):
        if move is None:
            avmoves=["Protect","Meteor Mash","Aura Sphere","Dragon Pulse","Close Combat","Bullet Punch","Bone Rush","Extreme Speed"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Hippowdon
class Hippowdon(Pokemon2):
    "Hippowdon"
    def __init__(self,name="Hippowdon",type1="Ground",type2=None,nature=None,level=100,happiness=255,hp=108,atk=112,defense=118,spatk=68,spdef=72,speed=47,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Sand Stream",item=random.choice(["Leftovers","Rocky Helmet"])):
        if move is None:
            avmoves=["Protect","Earthquake","Slack Off","Stone Edge","Knock Off","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Drapion
class Drapion(Pokemon2):
    "Drapion"
    def __init__(self,name="Drapion",type1="Poison",type2="Dark",nature=None,level=100,happiness=255,hp=70,atk=90,defense=110,spatk=60,spdef=75,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Sniper",item=random.choice(["Shuca Berry","Choice Band","Black Sludge"])):
        if move is None:
            avmoves=["Protect","Wicked Blow","Cross Poison","Swords Dance","Knock Off","Crunch","Toxic Spikes"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Toxicroak
class Toxicroak(Pokemon2):
    "Toxicroak"
    def __init__(self,name="Toxicroak",type1="Poison",type2="Fighting",nature=None,level=100,happiness=255,hp=83,atk=106,defense=65,spatk=86,spdef=65,speed=85,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Sniper",item=random.choice(["Choice Band","Life Orb"])):
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
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Weavile
class Weavile(Pokemon2):
    "Weavile"
    def __init__(self,name="Weavile",type1="Dark",type2="Ice",nature=None,level=100,happiness=255,hp=70,atk=120,defense=65,spatk=45,spdef=85,speed=125,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Pressure",item=random.choice(["Heavy-Duty Boots","Choice Band"])):
        if move is None:
            avmoves=["Protect","Night Slash","Icicle Crash","Ice Shard","Poison Jab","Fake Out"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                       #Magnezone
class Magnezone(Pokemon2):
    "Magnezone"
    def __init__(self,name="Magnezone",type1="Electric",type2="Steel",nature=None,level=100,happiness=255,hp=70,atk=70,defense=115,spatk=130,spdef=90,speed=60,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Levitate","Sturdy"]),item=random.choice(["Leftovers","Choice Specs"])):
        if move is None:
            avmoves=["Protect","Hidden Power","Flash Cannon","Thunderbolt","Iron Defense","Electric Terrain"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      
#Rhyperior
class Rhyperior(Pokemon2):
    "Rhyperior"
    def __init__(self,name="Rhyperior",type1="Ground",type2="Rock",nature=None,level=100,happiness=255,hp=115,atk=140,defense=130,spatk=55,spdef=55,speed=40,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=4,speedev=0,maxiv="No",move=None, ability="Solid Rock",item=random.choice(["Leftovers","Weakness Policy"])):
        if move is None:
            avmoves=["Protect","Stone Edge","Hammer Arm","High Horsepower","Thunder Punch","Giga Impact","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#Tangrowth
class Tangrowth(Pokemon2):
    "Tangrowth"
    def __init__(self,name="Tangrowth",type1="Grass",type2=None,nature=None,level=100,happiness=255,hp=100,atk=100,defense=125,spatk=110,spdef=50,speed=50,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=4,speedev=0,maxiv="No",move=None, ability="Regenerator",item=random.choice(["Assault Vest","Rocky Helmet"])):
        if move is None:
            avmoves=["Protect","Giga Drain","Sleep Powder","Ancient Power","Poison Jab","Grassy Terrain","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)   
#Electivire
class Electivire(Pokemon2):
    "Electivire"
    def __init__(self,name="Electivire",type1="Electric",type2=None,nature=None,level=100,happiness=255,hp=75,atk=123,defense=67,spatk=95,spdef=85,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=4,speedev=252,maxiv="No",move=None, ability="Motor Drive",item="Life Orb"):
        if move is None:
            avmoves=["Protect","Plasma Fists","Close Combat","Wild Charge","Brick Break","Giga Impact","Electric Terrain"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Magmortar
class Magmortar(Pokemon2):
    "Magmortar"
    def __init__(self,name="Magmortar",type1="Fire",type2=None,nature=None,level=100,happiness=255,hp=75,atk=95,defense=67,spatk=125,spdef=95,speed=83,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=4,speedev=252,maxiv="No",move=None, ability="Flash Fire",item=random.choice(["Choice Specs","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Protect","Fire Blast","Sunny Day","Flamethrower","Toxic","Armor Cannon"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                     
#Togekiss
class Togekiss(Pokemon2):
    "Togekiss"
    def __init__(self,name="Togekiss",type1="Fairy",type2="Flying",nature=None,level=100,happiness=255,hp=85,atk=50,defense=95,spatk=120,spdef=115,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=4,speedev=252,maxiv="No",move=None, ability="Serene Grace",item="Heavy-Duty Boots"):
        if move is None:
            avmoves=["Protect","Roost","Nasty Plot","Air Slash","Moonblast","Extreme Speed"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                
#Yanmega
class Yanmega(Pokemon2):
    "Yanmega"
    def __init__(self,name="Yanmega",type1="Bug",type2="Flying",nature=None,level=100,happiness=255,hp=86,atk=76,defense=86,spatk=116,spdef=56,speed=95,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=4,speedev=252,maxiv="No",move=None, ability="Speed Boost",item=random.choice(["Choice Specs","Heavy-Duty Boots","Life Orb"])):
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
    def __init__(self,name="Porygon-Z",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=85,atk=80,defense=70,spatk=135,spdef=75,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=4,speedev=252,maxiv="No",move=None, ability="Adaptability",item="Choice Scarf"):
        if move is None:
            avmoves=["Protect","Ice Beam","Calm Mind","Recover","Thunderbolt","Flamethrower","Signal Beam","Hidden Power","Psychic","Shadow Ball","Hyper Beam","Trick Room"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                          
#Gallade
class Gallade(Pokemon2):
    "Gallade"
    def __init__(self,name="Gallade",type1="Psychic",type2="Fighting",nature=None,level=100,happiness=255,hp=68,atk=125,defense=65,spatk=65,spdef=115,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=4,speedev=252,maxiv="No",move=None, ability="Steadfast",item=random.choice(["Choice Band","Assault Vest","Life Orb"])):
        if move is None:
            avmoves=["Protect","Swords Dance","Psycho Cut","Night Slash","Close Combat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Mega Gallade
class MGallade(Pokemon2):
    "Mega Gallade"
    def __init__(self,name="Mega Gallade",type1="Psychic",type2="Fighting",nature=None,level=100,happiness=255,hp=68,atk=165,defense=95,spatk=65,spdef=115,speed=110,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=4,speedev=252,maxiv="No",move=None, ability="Inner Focus",item="Galladite"):
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
            avmoves=["Protect","Bulk Up","Double-Edge","High Horsepower","Head Smash","Headlong Rush","Moonlight"]
            moves=moveset(avmoves)
        else:
            moves=move
        if ability=="Guts":
            item="Flame Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Probopass
class Probopass(Pokemon2):
    "Probopass"
    def __init__(self,name="Probopass",type1="Rock",type2="Steel",nature=None,level=100,happiness=255,hp=60,atk=55,defense=145,spatk=75,spdef=150,speed=40,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability=random.choice(["Sturdy","Sand Force"]),item=random.choice(["Leftovers","Air Ballon"])):
        if move is None:
            avmoves=["Protect","Iron Defense","Thunder Wave","Heavy Slam","Sandstorm","Zap Cannon","Power Gem","Rest"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                       
#Dusknoir
class Dusknoir(Pokemon2):
    "Dusknoir"
    def __init__(self,name="Dusknoir",type1="Ghost",type2=None,nature=None,level=100,happiness=255,hp=45,atk=100,defense=135,spatk=65,spdef=135,speed=45,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability=random.choice(["Pressure","Levitate"]),item=random.choice(["Choice Band","Leftovers"])):
        if move is None:
            avmoves=["Protect","Will-O-Wisp","Thunder Wave","Shadow Punch","Hex","Calm Mind","Rest"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Froslass
class Froslass(Pokemon2):
    "Froslass"
    def __init__(self,name="Froslass",type1="Ice",type2="Ghost",nature=None,level=100,happiness=255,hp=70,atk=80,defense=70,spatk=80,spdef=70,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Snow Cloak","Levitate"]),item="Focus Sash"):
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
    def __init__(self,name="Cresselia",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=120,atk=70,defense=120,spatk=75,spdef=130,speed=85,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Levitate"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Lunar Blessing","Moonblast","Psychic","Calm Mind","Dazzling Gleam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
#Phione
class Phione(Pokemon2):
    "Phione"
    def __init__(self,name="Phione",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=80,atk=80,defense=80,spatk=80,spdef=80,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Hydration"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Take Heart","Hydro Pump","Moonblast","Calm Mind","Acid Armor"]
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
    def __init__(self,name="Origin Arceus",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=200,atk=200,defense=200,spatk=200,spdef=200,speed=200,hpev=252,atkev=252,defev=252,spatkev=252,spdefev=252,speedev=252,maxiv="Yes",move=None, ability=random.choice(["Typeless"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Judgement","Roar of Time","Spacial Rend","Origin Pulse","Precipice Blades","Dragon Ascent","Magma Storm","Dark Void","Lunar Blessing","Crush Grip","Shadow Force","Aeroblast","Sacred Fire","Take Heart","Heart Swap","Seed Flare","Bleakwind Storm","Wildbolt Storm","Sandsear Storm","Sacred Sword","Secret Sword","Relic Song","Techno Blast","Blue Flare","Bolt Strike","Fusion Flare","Fusion Bolt","Freeze Shock","Ice Burn"]
            moves=avmoves
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Mightyena
class Mightyena(Pokemon2):
    "Mightyena"
    def __init__(self,name="Mightyena",type1="Dark",type2=None,nature=None,level=100,happiness=255,hp=70,atk=95,defense=70,spatk=60,spdef=60,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Strong Jaw","Intimidate"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Crunch","Fire Fang","Thunder Fang","Ice Fang","Poison Fang"]
            moves=moveset(avmoves)
        else:
            moves=move
        
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item) 
#Bronzong
class Bronzong(Pokemon2):
    "Bronzong"
    def __init__(self,name="Bronzong",type1="Steel",type2="Psychic",nature=None,level=100,happiness=255,hp=67,atk=89,defense=116,spatk=79,spdef=116,speed=33,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability=random.choice(["Levitate","Heatproof"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Trick Room","Extrasensory","Thunder Wave","Flash Cannon","Iron Defense","Light Screen","Reflect"]
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
            avmoves=["Protect","Leaf Storm","Hidden Power","Giga Drain","Coil","Focus Blast","Leech Seed","Frenzy Plant"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)     
#Emboar
class Emboar(Pokemon2):
    "Emboar"
    def __init__(self,name="Emboar",type1="Fire",type2="Fighting",nature=None,level=100,happiness=255,hp=110,atk=123,defense=65,spatk=100,spdef=65,speed=65,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Reckless",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hammer Arm","Flare Blitz","Heat Crash","Head Smash","Close Combat","Blast Burn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#Samurott
class Samurott(Pokemon2):
    "Samurott"
    def __init__(self,name="Samurott",type1="Water",type2="Steel",nature=None,level=100,happiness=255,hp=95,atk=100,defense=85,spatk=108,spdef=70,speed=70,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Shell Armor",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Swords Dance","Razor Shell","Aqua Jet","Megahorn","Hydro Pump","Hydro Cannon"]
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
    def __init__(self,name="Stoutland",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=85,atk=110,defense=90,spatk=45,spdef=90,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Scrappy",item=random.choice(["Silk Scarf","Life Orb"])):
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
    def __init__(self,name="Seismitoad",type1="Water",type2="Ground",nature=None,level=100,happiness=255,hp=105,atk=95,defense=75,spatk=85,spdef=75,speed=74,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Poison Touch","Swift Swim"]),item="Leftovers"):
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
    def __init__(self,name="Scolipede",type1="Bug",type2="Poison",nature=None,level=100,happiness=255,hp=60,atk=100,defense=89,spatk=55,spdef=69,speed=112,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=4,speedev=252,maxiv="No",move=None, ability=random.choice(["Poison Point","Speed Boost"]),item="Leftovers"):
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
    def __init__(self,name="Darmanitan",type1="Fire",type2=None,nature=None,level=100,happiness=255,hp=105,atk=140,defense=55,spatk=30,spdef=55,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Sheer Force","Zen Mode"]),item="Choice Scarf"):
        if move is None:
            avmoves=["Superpower","Earthquake","Stone Edge","Crunch","Flare Blitz","U-Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Galarian Darmanitan
class GDarmanitan(Pokemon2):
    "Galarian Darmanitan"
    def __init__(self,name="Galarian Darmanitan",type1="Ice",type2=None,nature=None,level=100,happiness=255,hp=105,atk=140,defense=55,spatk=30,spdef=55,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Gorilla Tactics","Zen Mode"]),item="Choice Scarf"):
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
            avmoves=["Protect","Close Combat","Drain Punch","Fake Out","Crunch","Foul Play","Knock Off"]
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
    def __init__(self,name="Archeops",type1="Rock",type2="Flying",nature=None,level=100,happiness=255,hp=75,atk=140,defense=65,spatk=80,spdef=65,speed=110,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Speed Boost",item="Flying Gem"):
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
        name=random.choice(["Raikou","Entei","Suicune","Primape","Machamp","Nihilego","Gengar","Toxicroak"])
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Hisuian Zoroark
class HZoroark(Pokemon2):
    "Hisuian Zoroark"
    def __init__(self,name="Hisuian Zoroark",type1="Normal",type2="Ghost",nature=None,level=100,happiness=255,hp=55,atk=100,defense=60,spatk=125,spdef=60,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Illusion",item=random.choice(["Life Orb","Leftovers"])):
        if move is None:
            avmoves=["Protect","Shadow Ball","Flamethrower","Nasty Plot","Bitter Malice","Knock Off","U-Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        name=random.choice(["Raikou","Entei","Suicune","Snorlax","Machamp"])
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Gothitelle
class Gothitelle(Pokemon2):
    "Gothitelle"
    def __init__(self,name="Gothitelle",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=70,atk=55,defense=95,spatk=95,spdef=110,speed=65,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Competitive",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Shadow Ball","Psychic","Calm Mind","Hypnosis","Thunder Wave","Stored Power"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Reuniclus
class Reuniclus(Pokemon2):
    "Reuniclus"
    def __init__(self,name="Reuniclus",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=110,atk=65,defense=75,spatk=125,spdef=85,speed=30,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Magic Guard",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Shadow Ball","Psychic","Calm Mind","Acid Armor","Thunder Wave","Stored Power","Reflect"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                                                                                                                 #Swanna
class Swanna(Pokemon2):
    "Swanna"
    def __init__(self,name="Swanna",type1="Water",type2="Flying",nature=None,level=100,happiness=255,hp=75,atk=87,defense=63,spatk=87,spdef=63,speed=98,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Hydration",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Brave Bird","Hurricane","Rain Dance","Roost","Air Slash","Surf"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Vanilluxe
class Vanilluxe(Pokemon2):
    "Vanilluxe"
    def __init__(self,name="Vanilluxe",type1="Ice",type2=None,nature=None,level=100,happiness=255,hp=71,atk=95,defense=85,spatk=110,spdef=95,speed=79,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Snow Warning",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Blizzard","Ice Beam","Acid Armor","Icicle Spear","Freeze-Dry","Weather Ball"]
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
    def __init__(self,name="Jellicent",type1="Water",type2="Ghost",nature=None,level=100,happiness=255,hp=100,atk=60,defense=70,spatk=85,spdef=105,speed=60,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Water Absorb",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Night Shade","Acid Armor","Rain Dance","Recover","Will-O-Wisp","Hex"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
#Galvantula
class Galvantula(Pokemon2):
    "Galvantula"
    def __init__(self,name="Galvantula",type1="Bug",type2="Electric",nature=None,level=100,happiness=255,hp=70,atk=77,defense=60,spatk=97,spdef=60,speed=108,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Swarm",item=random.choice(["Life Orb","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Protect","Electoweb","Thunder Wave","Electro Ball","Sucker Punch","Discharge","Bug Buzz","Giga Drain"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Ferrothorn
class Ferrothorn(Pokemon2):
    "Ferrothorn"
    def __init__(self,name="Ferrothorn",type1="Grass",type2="Steel",nature=None,level=100,happiness=255,hp=74,atk=94,defense=131,spatk=54,spdef=116,speed=20,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability="Iron Barbs",item=random.choice(["Leftovers","Rocky Helmet"])):
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
    def __init__(self,name="Haxorus",type1="Dragon",type2=None,nature=None,level=100,happiness=255,hp=76,atk=147,defense=90,spatk=60,spdef=70,speed=97,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Mold Breaker",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Outrage","Swords Dance","Dual Chop","Dragon Dance","Dragon Claw","Crunch"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Beartic
class Beartic(Pokemon2):
    "Beartic"
    def __init__(self,name="Beartic",type1="Ice",type2=None,nature=None,level=100,happiness=255,hp=95,atk=110,defense=80,spatk=70,spdef=80,speed=50,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Slush Rush",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Outrage","Swords Dance","Icicle Crash","Ice Fang","Dragon Claw","Crunch","Hammer Arm","Superpower","Hail"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      
#Accelgor
class Accelgor(Pokemon2):
    "Accelgor"
    def __init__(self,name="Accelgor",type1="Bug",type2=None,nature=None,level=100,happiness=255,hp=80,atk=70,defense=40,spatk=100,spdef=60,speed=145,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Sticky Hold",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Toxic","Bug Buzz","Final Gambit","U-Turn","Recover","Giga Drain","Water Shuriken"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)    
#Mienshao
class Mienshao(Pokemon2):
    "Mienshao"
    def __init__(self,name="Mienshao",type1="Fighting",type2=None,nature=None,level=100,happiness=255,hp=65,atk=125,defense=60,spatk=95,spdef=60,speed=105,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Regenerator",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Drain Punch","High Jump Kick","Aura Sphere","U-Turn","Fake Out","Rock Slide"]
            moves=moveset(avmoves)
        else:
            moves=move    
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                
#Druddigon
class Druddigon(Pokemon2):
    "Druddigon"
    def __init__(self,name="Druddigon",type1="Dragon",type2=None,nature=None,level=100,happiness=255,hp=77,atk=120,defense=90,spatk=60,spdef=90,speed=48,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Sheer Force",item="Life Orb"):
        if move is None:
            avmoves=["Protect","Outrage","Swords Dance","Superpower","Dragon Dance","Dragon Claw","Crunch"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      

#Golurk
class Golurk(Pokemon2):
    "Golurk"
    def __init__(self,name="Golurk",type1="Ground",type2="Ghost",nature=None,level=100,happiness=255,hp=89,atk=124,defense=80,spatk=55,spdef=80,speed=55,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["No Guard"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Phantom Force","Hammer Arm","Shadow Sneak","Earthquake","Dynamic Punch","Stomping Tantrum","High Horsepower","Magnitude"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)       
#Bisharp
class Bisharp(Pokemon2):
    "Bisharp"
    def __init__(self,name="Bisharp",type1="Dark",type2="Steel",nature=None,level=100,happiness=255,hp=65,atk=125,defense=100,spatk=60,spdef=70,speed=70,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Defiant"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Night Slash","Swords Dance","Iron Head","Superpower"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)   
#Bouffalant
class Bouffalant(Pokemon2):
    "Bouffalant"
    def __init__(self,name="Bouffalant",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=95,atk=110,defense=95,spatk=40,spdef=95,speed=55,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Sap Sipper",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Megahorn","Swords Dance","Superpower","Head Charge","High Horsepower","Wild Charge","Stone Edge","Iron Head","Zen Headbutt","Close Combat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)  
#Braviary
class Braviary(Pokemon2):
    "Braviary"
    def __init__(self,name="Braviary",type1="Normal",type2="Flying",nature=None,level=100,happiness=255,hp=100,atk=123,defense=75,spatk=57,spdef=75,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Defiant","Sheer Force"]),item="Life Orb"):
        if move is None:
            avmoves=["Protect","Final Gambit","Roost","Brave Bird","Close Combat","U-Turn","Sky Attack","Rock Slide"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Hisuian Braviary
class HBraviary(Pokemon2):
    "Hisuian Braviary"
    def __init__(self,name="Hisuian Braviary",type1="Psychic",type2="Flying",nature=None,level=100,happiness=255,hp=110,atk=83,defense=70,spatk=112,spdef=70,speed=65,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Sheer Force"]),item="Life Orb"):
        if move is None:
            avmoves=["Protect","Final Gambit","Roost","Esper Wing","Air Slash","Dazzling Gleam","Mystical Fire","Psychic"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Mandibuzz
class Mandibuzz(Pokemon2):
    "Mandibuzz"
    def __init__(self,name="Mandibuzz",type1="Dark",type2="Flying",nature=None,level=100,happiness=255,hp=110,atk=65,defense=105,spatk=55,spdef=95,speed=80,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Overcoat"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Final Gambit","Roost","Brave Bird","Iron Defense","U-Turn","Knock Off","Bone Rush"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Heatmor
class Heatmor(Pokemon2):
    "Heatmor"
    def __init__(self,name="Heatmor",type1="Fire",type2=None,nature=None,level=100,happiness=255,hp=85,atk=97,defense=66,spatk=105,spdef=66,speed=65,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Flash Fire"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Fire Lash","Flare Blitz","Inferno","Giga Drain","U-Turn","Knock Off","Sunny Day"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Durant
class Durant(Pokemon2):
    "Durant"
    def __init__(self,name="Durant",type1="Bug",type2="Steel",nature=None,level=100,happiness=255,hp=58,atk=109,defense=112,spatk=48,spdef=48,speed=109,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Hustle"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Crunch","Iron Head","U-Turn","Knock Off","X-Scissor","Rock Slide","Stomping Tantrum"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Hydreigon
class Hydreigon(Pokemon2):
    "Hydreigon"
    def __init__(self,name="Hydreigon",type1="Dark",type2="Dragon",nature=None,level=100,happiness=255,hp=92,atk=105,defense=90,spatk=125,spdef=90,speed=98,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Levitate"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Dragon Pulse","Dark Pulse","Flamethrower","U-Turn","Thunderbolt","Shadow Ball","Thunder Wave","Nasty Plot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Volcarona
class Volcarona(Pokemon2):
    "Volcarona"
    def __init__(self,name="Volcarona",type1="Bug",type2="Fire",nature=None,level=100,happiness=255,hp=85,atk=60,defense=65,spatk=135,spdef=105,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Flame Body"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Quiver Dance","Fiery Dance","Bug Buzz","Giga Drain","Heat Wave"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      
#Cobalion
class Cobalion(Pokemon2):
    "Cobalion"
    def __init__(self,name="Cobalion",type1="Steel",type2="Fighting",nature=None,level=100,happiness=255,hp=91,atk=90,defense=129,spatk=90,spdef=72,speed=108,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Justified",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Swords Dance","Secred Sword","Superpower","Close Combat","Iron Head"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Terrakion
class Terrakion(Pokemon2):
    "Terrakion"
    def __init__(self,name="Terrakion",type1="Rock",type2="Fighting",nature=None,level=100,happiness=255,hp=91,atk=129,defense=90,spatk=72,spdef=90,speed=108,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Justified",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Swords Dance","Secred Sword","Earthquake","Close Combat","Stone Edge"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Virizion
class Virizion(Pokemon2):
    "Virizion"
    def __init__(self,name="Virizion",type1="Grass",type2="Fighting",nature=None,level=100,happiness=255,hp=91,atk=90,defense=72,spatk=90,spdef=129,speed=108,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Justified",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Swords Dance","Secred Sword","Giga Drain","Close Combat","Leaf Blade"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Tornadus
class Tornadus(Pokemon2):
    "Tornadus"
    def __init__(self,name="Tornadus",type1="Flying",type2=None,nature=None,level=100,happiness=255,hp=79,atk=115,defense=70,spatk=125,spdef=80,speed=111,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Prankster",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hurricane","Bleakwind Storm","Air Slash","Extrasensory"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Thundurus
class Thundurus(Pokemon2):
    "Thundurus"
    def __init__(self,name="Thundurus",type1="Electric",type2="Flying",nature=None,level=100,happiness=255,hp=79,atk=115,defense=70,spatk=125,spdef=80,speed=111,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Prankster",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Thunder","Wildbolt Storm","Nasty Plot","Extrasensory"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Landorus
class Landous(Pokemon2):
    "Landorus"
    def __init__(self,name="Landorus",type1="Ground",type2="Flying",nature=None,level=100,happiness=255,hp=89,atk=125,defense=90,spatk=115,spdef=80,speed=101,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Prankster",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Earth Power","Sandsear Storm","Air Slash","Extrasensory"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Therian Tornadus
class TTornadus(Pokemon2):
    "Therian Tornadus"
    def __init__(self,name="Therian Tornadus",type1="Flying",type2=None,nature=None,level=100,happiness=255,hp=79,atk=100,defense=80,spatk=110,spdef=90,speed=121,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Regenerator",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hurricane","Bleakwind Storm","Air Slash","Extrasensory"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                   
#Therian Thundurus
class TThundurus(Pokemon2):
    "Therian Thundurus"
    def __init__(self,name="Therian Thundurus",type1="Electric",type2="Flying",nature=None,level=100,happiness=255,hp=79,atk=105,defense=70,spatk=145,spdef=80,speed=101,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Volt Absorb",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Thunder","Wildbolt Storm","Nasty Plot","Extrasensory"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Therian Landorus
class TLandous(Pokemon2):
    "Therian Landorus"
    def __init__(self,name="Therian Landorus",type1="Ground",type2="Flying",nature=None,level=100,happiness=255,hp=89,atk=145,defense=90,spatk=105,spdef=80,speed=91,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Intimidate",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Earthquake","Sandsear Storm","U-Turn","Stone Edge","Swords Dance"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Reshiram
class Reshiram(Pokemon2):
    "Reshiram"
    def __init__(self,name="Reshiram",type1="Dragon",type2="Fire",nature=None,level=100,happiness=255,hp=100,atk=120,defense=100,spatk=150,spdef=120,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Turboblaze",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Blue Flare","Fusion Flare","Dragon Pulse"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Zekrom
class Zekrom(Pokemon2):
    "Zekrom"
    def __init__(self,name="Zekrom",type1="Dragon",type2="Electric",nature=None,level=100,happiness=255,hp=100,atk=150,defense=120,spatk=120,spdef=100,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Teravolt",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Bolt Strike","Fusion Bolt","Dragon Claw"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Kyurem
class Kyurem(Pokemon2):
    "Kyurem"
    def __init__(self,name="Kyurem",type1="Dragon",type2="Ice",nature=None,level=100,happiness=255,hp=125,atk=130,defense=90,spatk=130,spdef=90,speed=95,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Pressure",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Glaciate","Outrage","Sheer Cold"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #White Kyurem
class WKyurem(Pokemon2):
    "White Kyurem"
    def __init__(self,name="White Kyurem",type1="Dragon",type2="Ice",nature=None,level=100,happiness=255,hp=125,atk=120,defense=90,spatk=170,spdef=100,speed=95,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Turboblaze",item="Leftovers"):
        if move is None:
            avmoves=["Blue Flare","Fusion Flare","Dragon Pulse","Ice Burn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Black Kyurem 
class BKyurem(Pokemon2):
    "Black Kyurem"
    def __init__(self,name="Black Kyurem",type1="Dragon",type2="Ice",nature=None,level=100,happiness=255,hp=125,atk=170,defense=100,spatk=120,spdef=90,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Teravolt",item="Leftovers"):
        if move is None:
            avmoves=["Freeze Shock","Fusion Bolt","Dragon Claw","Bolt Strike"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Keldeo
class Keldeo(Pokemon2):
    "Keldeo"
    def __init__(self,name="Keldeo",type1="Water",type2="Fighting",nature=None,level=100,happiness=255,hp=91,atk=72,defense=90,spatk=129,spdef=90,speed=108,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Justified",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Sacred Sword","Secret Sword","Hydro Pump","Close Combat"]
            moves=moveset(avmoves)
        else:
            moves=move
        if "Secret Sword" in moves:
            name="Resolute "+name
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Meloetta
class Meloetta(Pokemon2):
    "Meloetta"
    def __init__(self,name="Meloetta",type1="Normal",type2="Psychic",nature=None,level=100,happiness=255,hp=100,atk=77,defense=77,spatk=128,spdef=128,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Serene Grace",item="Leftovers"):
        if move is None:
            avmoves=["Protect","U-Turn","Psychic","Relic Song","Close Combat"]
            moves=moveset(avmoves)
        else:
            moves=move
        
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Pirouette Meloetta
class PMeloetta(Pokemon2):
    "Meloetta"
    def __init__(self,name="Pirouette Meloetta",type1="Normal",type2="Fighting",nature=None,level=100,happiness=255,hp=100,atk=128,defense=90,spatk=77,spdef=77,speed=128,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Serene Grace",item="Leftovers"):
        if move is None:
            avmoves=["Protect","U-Turn","Psychic","Relic Song","Close Combat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Genesect
class Genesect(Pokemon2):
    "Genesect"
    def __init__(self,name="Genesect",type1="Bug",type2="Steel",nature=None,level=100,happiness=255,hp=71,atk=120,defense=95,spatk=120,spdef=95,speed=95,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Download",item=random.choice(["Burn Drive","Chill Drive","Douse Drive","Shock Drive"])):
        if move is None:
            avmoves=["Protect","Techno Blast","Bug Buzz","Iron Head","X-Scissor","Flash Cannon"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Delphox
class Delphox(Pokemon2):
    "Delphox"
    def __init__(self,name="Delphox",type1="Fire",type2="Psychic",nature=None,level=100,happiness=255,hp=75,atk=69,defense=72,spatk=114,spdef=100,speed=104,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Blaze","Magic Guard"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Fire Blast","Flamethrower","Psychic","Mystical Fire","Shadow Ball","Blast Burn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Chesnaught
class Chesnaught(Pokemon2):
    "Chesnaught"
    def __init__(self,name="Chesnaught",type1="Grass",type2="Fighting",nature=None,level=100,happiness=255,hp=88,atk=107,defense=122,spatk=74,spdef=75,speed=64,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Overgrow","Iron Barbs"]),item="Leftovers"):
        if move is None:
            avmoves=["Hammer Arm","Wood Hammer","Bulk Up","Seed Bomb","Close Combat","Frenzy Plant","Spiky Shield"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Greninja
class Greninja(Pokemon2):
    "Greninja"
    def __init__(self,name="Greninja",type1="Water",type2="Dark",nature=None,level=100,happiness=255,hp=72,atk=95,defense=67,spatk=103,spdef=71,speed=122,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Protean",item="Life Orb"):
        if move is None:
            avmoves=["Water Shuriken","Dark Pulse","Hydro Pump","Extrasensory","Grass Knot","Hydro Cannon","Poison Jab","Ice Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Ash Greninja
class AGreninja(Pokemon2):
    "Ash Greninja"
    def __init__(self,name="Ash Greninja",type1="Water",type2="Dark",nature=None,level=100,happiness=255,hp=72,atk=145,defense=67,spatk=153,spdef=71,speed=132,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Battle Bond",item="Life Orb"):
        if move is None:
            avmoves=["Water Shuriken","Dark Pulse","Hydro Pump","Extrasensory","Grass Knot","Hydro Cannon","Ice Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Talonflame
class Talonflame(Pokemon2):
    "Talonflame"
    def __init__(self,name="Talonflame",type1="Fire",type2="Flying",nature=None,level=100,happiness=255,hp=78,atk=81,defense=71,spatk=74,spdef=69,speed=126,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Gale Wings",item="Charti Berry"):
        if move is None:
            avmoves=["Protect","Heat Wave","Sky Attack","Brave Bird","Flare Blitz","Roost"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Pyroar
class Pyroar(Pokemon2):
    "Pyroar"
    def __init__(self,name="Pyroar",type1="Fire",type2="Normal",nature=None,level=100,happiness=255,hp=86,atk=68,defense=72,spatk=109,spdef=66,speed=106,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Moxie",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Heat Wave","Fire Blast","Flamethrower","Flare Blitz","Overheat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                                                                                           
#Florges
class Florges(Pokemon2):
    "Florges"
    def __init__(self,name="Florges",type1="Fairy",type2=None,nature=None,level=100,happiness=255,hp=78,atk=65,defense=68,spatk=112,spdef=154,speed=75,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Misty Terrain",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Moonblast","Petal Blizzard","Grass Knot","Dazzling Gleam","Synthesis","Grassy Terrain","Misty Terrain"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Eternal Floette
class EFloette(Pokemon2):
    "Floette"
    def __init__(self,name="Eternal Floette",type1="Fairy",type2=None,nature=None,level=100,happiness=255,hp=74,atk=65,defense=67,spatk=125,spdef=128,speed=92,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Misty Terrain",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Moonblast","Petal Blizzard","Grass Knot","Light of Ruin","Synthesis","Grassy Terrain","Misty Terrain"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                                                                                                                 #Gogoat
class Gogoat(Pokemon2):
    "Gogoat"
    def __init__(self,name="Gogoat",type1="Grass",type2=None,nature=None,level=100,happiness=255,hp=123,atk=100,defense=62,spatk=97,spdef=81,speed=68,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Sap Sipper",item="Leftovers"):
        if move is None:
            avmoves=["Leaf Blade","Wood Hammer","Bulk Up","Seed Bomb","Milk Drink","Horn Leech","Leech Seed"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Pangoro
class Pangoro(Pokemon2):
    "Pangoro"
    def __init__(self,name="Pangoro",type1="Fighting",type2="Dark",nature=None,level=100,happiness=255,hp=95,atk=124,defense=78,spatk=69,spdef=71,speed=58,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Scrappy",item="Leftovers"):
        if move is None:
            avmoves=["Hammer Arm","Parting Shot","Bulk Up","Crunch","Close Combat","Night Slash","Grass Knot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Aegislash
class Aegislash(Pokemon2):
    "Aegislash"
    def __init__(self,name="Aegislash",type1="Steel",type2="Ghost",nature=None,level=100,happiness=255,hp=60,atk=50,defense=140,spatk=50,spdef=140,speed=60,hpev=252,atkev=0,defev=252,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Stance Change",item="Leftovers", shield=True,sword=False):
        if move is None:
            avmoves=["King's Shield","Sacred Sword","Shadow Sneak","Iron Head"]
            moves=moveset(avmoves)
        else:
            moves=move
        self.shield=shield
        self.sword=sword
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                                                                                                                 #Malamar
class Malamar(Pokemon2):
    "Malamar"
    def __init__(self,name="Malamar",type1="Dark",type2="Psychic",nature=None,level=100,happiness=255,hp=86,atk=92,defense=88,spatk=68,spdef=75,speed=75,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Contrary",item="Leftovers", shield=True,sword=False):
        if move is None:
            avmoves=["Superpower","Psycho Cut","Shadow Sneak","Night Slash","Hypnosis"]
            moves=moveset(avmoves)
        else:
            moves=move
        self.shield=shield
        self.sword=sword
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Barbaracle
class Barbaracle(Pokemon2):
    "Barbaracle"
    def __init__(self,name="Barbaracle",type1="Rock",type2="Water",nature=None,level=100,happiness=255,hp=72,atk=105,defense=115,spatk=54,spdef=86,speed=68,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Tough Claws",item="Leftovers", shield=True,sword=False):
        if move is None:
            avmoves=["Superpower","Shell Smash","Razor Shell","Stone Edge","Cross Chop"]
            moves=moveset(avmoves)
        else:
            moves=move
        self.shield=shield
        self.sword=sword
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Dragalge
class Dragalge(Pokemon2):
    "Dragalge"
    def __init__(self,name="Dragalge",type1="Poison",type2="Dragon",nature=None,level=100,happiness=255,hp=65,atk=75,defense=90,spatk=97,spdef=123,speed=44,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Poison Point","Adaptability"]),item="Leftovers"):
        if move is None:
            avmoves=["Hydro Pump","Sludge Bomb","Outrage","Dragon Pulse","Sludge Wave"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Clawitzer
class Clawitzer(Pokemon2):
    "Clawitzer"
    def __init__(self,name="Clawitzer",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=71,atk=73,defense=88,spatk=120,spdef=89,speed=59,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Mega Launcher",item="Leftovers"):
        if move is None:
            avmoves=["Hydro Pump","Aura Sphere","Dark Pulse","Dragon Pulse","Sludge Wave"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Tyrantrum
class Tyrantrum(Pokemon2):
    "Tyrantrum"
    def __init__(self,name="Tyrantrum",type1="Rock",type2="Dragon",nature=None,level=100,happiness=255,hp=82,atk=121,defense=119,spatk=69,spdef=59,speed=71,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Rock Head","Strong Jaw"]),item="Leftovers", shield=True,sword=False):
        if move is None:
            avmoves=["Giga Impact","Head Smash","Earthquake","Stone Edge","Dragon Claw"]
            moves=moveset(avmoves)
        else:
            moves=move
        self.shield=shield
        self.sword=sword
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Aurorus
class Aurorus(Pokemon2):
    "Aurorus"
    def __init__(self,name="Aurorus",type1="Rock",type2="Ice",nature=None,level=100,happiness=255,hp=123,atk=77,defense=72,spatk=99,spdef=92,speed=58,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Refrigerate",item="Leftovers", shield=True,sword=False):
        if move is None:
            avmoves=["Giga Impact","Blizzard","Ice Beam","Stone Edge","Freeze-Dry","Light Screen"]
            moves=moveset(avmoves)
        else:
            moves=move
        self.shield=shield
        self.sword=sword
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Hawlucha
class Hawlucha(Pokemon2):
    "Hawlucha"
    def __init__(self,name="Hawlucha",type1="Fighting",type2="Flying",nature=None,level=100,happiness=255,hp=78,atk=92,defense=75,spatk=74,spdef=63,speed=118,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Limber"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Sky Attack","Roost","Brave Bird","Close Combat","U-Turn","High Jump Kick","Flying Press","Swords Dance"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Goodra
class Goodra(Pokemon2):
    "Goodra"
    def __init__(self,name="Goodra",type1="Dragon",type2=None,nature=None,level=100,happiness=255,hp=90,atk=100,defense=70,spatk=110,spdef=150,speed=80,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Sap Sipper",item="Assault Vest", shield=True,sword=False):
        if move is None:
            avmoves=["Power Whip","Body Slam","Hydro Pump","Rain Dance","Dragon Pulse","Protect"]
            moves=moveset(avmoves)
        else:
            moves=move
        self.shield=shield
        self.sword=sword
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Hisuian Goodra
class HGoodra(Pokemon2):
    "Hisuian Goodra"
    def __init__(self,name="Hisuian Goodra",type1="Dragon",type2="Steel",nature=None,level=100,happiness=255,hp=80,atk=100,defense=100,spatk=110,spdef=150,speed=60,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Sap Sipper",item="Assault Vest", shield=True,sword=False):
        if move is None:
            avmoves=["Power Whip","Body Slam","Hydro Pump","Shelter","Dragon Pulse","Protect"]
            moves=moveset(avmoves)
        else:
            moves=move
        self.shield=shield
        self.sword=sword
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Trevenant
class Trevenant(Pokemon2):
    "Trevenant"
    def __init__(self,name="Trevenant",type1="Ghost",type2="Grass",nature=None,level=100,happiness=255,hp=85,atk=110,defense=76,spatk=65,spdef=82,speed=56,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Natural Cure",item="Leftovers"):
        if move is None:
            avmoves=["Leech Seed","Wood Hammer","Shadow Claw","Will-O-Wisp","Horn Leech","Phantom Force","Forest's Curse"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                         #Gourgeist
class Gourgeist(Pokemon2):
    "Gourgeist"
    def __init__(self,name="Gourgeist",type1="Ghost",type2="Grass",nature=None,level=100,happiness=255,hp=85,atk=100,defense=122,spatk=58,spdef=75,speed=54,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Frisk",item="Leftovers"):
        if move is None:
            avmoves=["Leech Seed","Bullet Seed","Shadow Claw","Will-O-Wisp","Razor Leaf","Phantom Force","Trick-or-Treat"]
            moves=moveset(avmoves)
        else:
            moves=move
        name=random.choice(["Small","Large","Super"])+" "+name
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Hisuian Avalugg
class HAvalugg(Pokemon2):
    "Avalugg"
    def __init__(self,name="Hisuian Avalugg",type1="Ice",type2="Rock",nature=None,level=100,happiness=255,hp=95,atk=127,defense=184,spatk=34,spdef=36,speed=38,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Sturdy",item="Leftovers", shield=True,sword=False):
        if move is None:
            avmoves=["Mountain Gale","Ice Shard","Icicle Crash","Stone Edge","Earthquake","Iron Defense"]
            moves=moveset(avmoves)
        else:
            moves=move
        self.shield=shield
        self.sword=sword
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Avalugg
class Avalugg(Pokemon2):
    "Avalugg"
    def __init__(self,name="Avalugg",type1="Ice",type2=None,nature=None,level=100,happiness=255,hp=95,atk=117,defense=184,spatk=44,spdef=46,speed=28,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Refrigerate",item="Leftovers", shield=True,sword=False):
        if move is None:
            avmoves=["Mountain Gale","Ice Shard","Icicle Crash","Earthquake","Iron Defense","Recover"]
            moves=moveset(avmoves)
        else:
            moves=move
        self.shield=shield
        self.sword=sword
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Noivern
class Noivern(Pokemon2):
    "Noivern"
    def __init__(self,name="Noivern",type1="Flying",type2="Dragon",nature=None,level=100,happiness=255,hp=85,atk=70,defense=80,spatk=97,spdef=80,speed=123,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Infiltrator",item="Leftovers"):
        if move is None:
            avmoves=["Boomburst","Hurricane","Roost","Dragon Pulse","Air Slash"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                                             
#Xerneas
class Xerneas(Pokemon2):
    "Xerneas"
    def __init__(self,name="Xerneas",type1="Fairy",type2=None,nature=None,level=100,happiness=255,hp=126,atk=131,defense=95,spatk=131,spdef=98,speed=99,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Fairy Aura",item="Power Herb"):
        if move is None:
            avmoves=["Geomancy","Moonblast","Thunder","Flamethrower","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Yveltal
class Yveltal(Pokemon2):
    "Yveltal"
    def __init__(self,name="Yveltal",type1="Dark",type2=None,nature=None,level=100,happiness=255,hp=126,atk=131,defense=95,spatk=131,spdef=98,speed=99,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Dark Aura",item="Leftovers"):
        if move is None:
            avmoves=["Oblivion Wing","Dark Pulse","Thunder","Sucker Punch","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Complete Zygarde
class CZygarde(Pokemon2):
    "Zygarde"
    def __init__(self,name="Complete Zygarde",type1="Dragon",type2="Ground",nature=None,level=100,happiness=255,hp=216,atk=100,defense=121,spatk=91,spdef=95,speed=85,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Power Constrict",item="Leftovers"):
        if move is None:
            avmoves=["Land's Wrath","Thousand Arrows","Core Enforcer","Earthquake","Coil","Thousand Waves"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Klefki
class Klefki(Pokemon2):
    "Klefki"
    def __init__(self,name="Klefki",type1="Steel",type2="Fairy",nature=None,level=100,happiness=255,hp=57,atk=80,defense=91,spatk=80,spdef=87,speed=75,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Prankster",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Foul Play","Play Rough","Flash Cannon","Toxic"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)       
#Diancie
class Diancie(Pokemon2):
    "Diancie"
    def __init__(self,name="Diancie",type1="Rock",type2="Fairy",nature=None,level=100,happiness=255,hp=50,atk=100,defense=150,spatk=100,spdef=150,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Clear Body",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Diamond Storm","Play Rough","Moonblast","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)  

#Mega Diancie
class MDiancie(Pokemon2):
    "Mega Diancie"
    def __init__(self,name="Mega Diancie",type1="Rock",type2="Fairy",nature=None,level=100,happiness=255,hp=50,atk=160,defense=110,spatk=160,spdef=110,speed=110,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Clear Body",item="Diancite"):
        if move is None:
            avmoves=["Protect","Diamond Storm","Play Rough","Moonblast","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Hoopa Unbound 
class UHoopa(Pokemon2):
    "Hoopa Unbound"
    def __init__(self,name="Hoopa Unbound",type1="Psychic",type2="Dark",nature=None,level=100,happiness=255,hp=80,atk=160,defense=60,spatk=170,spdef=130,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Magician",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hyperspace Fury","Psychic","Dark Pulse","Shadow Ball"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Volcanion
class Volcanion(Pokemon2):
    "Volcanion"
    def __init__(self,name="Volcanion",type1="Fire",type2="Water",nature=None,level=100,happiness=255,hp=80,atk=110,defense=120,spatk=130,spdef=90,speed=70,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Water Absorb",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Steam Eruption","Flare Blitz","Overheat","Hydro Pump"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Decidueye
class Decidueye(Pokemon2):
    "Decidueye"
    def __init__(self,name="Decidueye",type1="Grass",type2="Ghost",nature=None,level=100,happiness=255,hp=78,atk=107,defense=75,spatk=100,spdef=100,speed=70,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Overgrow",item="Leftovers"):
        if move is None:
            avmoves=["Spirit Shackle","U-Turn","Shadow Claw","Brave Bird","Leaf Blade","Shadow Sneak","Sucker Punch"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Hisuian Decidueye
class HDecidueye(Pokemon2):
    "Hisuian Decidueye"
    def __init__(self,name="Hisuian Decidueye",type1="Grass",type2="Fighting",nature=None,level=100,happiness=255,hp=88,atk=112,defense=80,spatk=95,spdef=95,speed=60,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Overgrow",item="Leftovers"):
        if move is None:
            avmoves=["Triple Arrows","U-Turn","Aura Sphere","Brave Bird","Leaf Blade","Close Combat","Roost"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Incineroar
class Incineroar(Pokemon2):
    "Incineroar"
    def __init__(self,name="Incineroar",type1="Fire",type2="Dark",nature=None,level=100,happiness=255,hp=95,atk=115,defense=90,spatk=80,spdef=90,speed=60,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Intimidate",item="Leftovers"):
        if move is None:
            avmoves=["Darkest Lariat","Throat Chop","Flare Blitz","Parting Shot","Snarl"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Primarina
class Primarina(Pokemon2):
    "Primarina"
    def __init__(self,name="Primarina",type1="Water",type2="Fairy",nature=None,level=100,happiness=255,hp=80,atk=74,defense=74,spatk=126,spdef=116,speed=60,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Liquid Voice",item="Leftovers"):
        if move is None:
            avmoves=["Sparkling Aria","Moonblast","Hyper Voice","Hydro Pump","Misty Terrain","Ice Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Toucannon
class Toucannon(Pokemon2):
    "Toucannon"
    def __init__(self,name="Toucannon",type1="Normal",type2="Flying",nature=None,level=100,happiness=255,hp=80,atk=120,defense=75,spatk=75,spdef=75,speed=60,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Sheer Force","Skill Link"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Beak Blast","Roost","Brave Bird","Rock Blast","U-Turn","Bullet Seed","Drill Peck"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Hisuian Electrode
class HElectrode(Pokemon2):
    "Hisuian Electrode"
    def __init__(self,name="Hisuian Electrode",type1="Electric",type2="Grass",nature=None,level=100,happiness=255,hp=60,atk=50,defense=70,spatk=80,spdef=80,speed=150,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Overgrow",item="Leftovers"):
        if move is None:
            avmoves=["Chloroblast","Thunder","Thunderbolt","Thunder Wave","Energy Ball","Hyper Beam","Rest","Explosion"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Sneasler
class Sneasler(Pokemon2):
    "Sneasler"
    def __init__(self,name="Sneasler",type1="Poison",type2="Fighting",nature=None,level=100,happiness=255,hp=80,atk=130,defense=60,spatk=40,spdef=80,speed=120,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Poison Touch",item="Leftovers"):
        if move is None:
            avmoves=["Dire Claw","Poison Jab","Close Combat","Swords Dance","X-Scissor","Bulk Up","Rest","Shadow Claw"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Wyrdeer
class Wyrdeer(Pokemon2):
    "Wyrdeer"
    def __init__(self,name="Wyrdeer",type1="Normal",type2="Psychic",nature=None,level=100,happiness=255,hp=103,atk=105,defense=72,spatk=105,spdef=75,speed=65,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Intimidate",item="Leftovers"):
        if move is None:
            avmoves=["Psyshield Bash","Zen Headbutt","Double-Edge","Wild Charge","Megahorn","Rest","High Horsepower"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Vikavolt
class Vikavolt(Pokemon2):
    "Vikavolt"
    def __init__(self,name="Vikavolt",type1="Bug",type2="Electric",nature=None,level=100,happiness=255,hp=77,atk=70,defense=90,spatk=145,spdef=75,speed=43,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Levitate",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Thunderbolt","Thunder Wave","Zap Cannon","Energy Ball","Crunch","Bug Buzz","Thunder"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Midday Lycanroc
class MDLycanroc(Pokemon2):
    "Lycanroc"
    def __init__(self,name="Midday Lycanroc",type1="Rock",type2=None,nature=None,level=100,happiness=255,hp=75,atk=115,defense=65,spatk=55,spdef=65,speed=112,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Sand Rush",item="Leftovers"):
        if move is None:
            avmoves=["Accelerock","Stone Edge","Crunch","Sucker Punch","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Midnight Lycanroc
class MNLycanroc(Pokemon2):
    "Lycanroc"
    def __init__(self,name="Midnight Lycanroc",type1="Rock",type2=None,nature=None,level=100,happiness=255,hp=85,atk=115,defense=75,spatk=55,spdef=75,speed=82,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="No Guard",item="Leftovers"):
        if move is None:
            avmoves=["Accelerock","Stone Edge","Crunch","Close Combat","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)       
#Dusk Lycanroc
class DLycanroc(Pokemon2):
    "Lycanroc"
    def __init__(self,name="Dusk Lycanroc",type1="Rock",type2=None,nature=None,level=100,happiness=255,hp=75,atk=117,defense=75,spatk=55,spdef=65,speed=110,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Tough Claws",item="Leftovers"):
        if move is None:
            avmoves=["Accelerock","Stone Edge","Crunch","Sucker Punch","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #School Wishiwashi
class SWishiwashi(Pokemon2):
    "Wishiwashi"
    def __init__(self,name="School Wishiwashi",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=45,atk=140,defense=130,spatk=140,spdef=135,speed=30,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Schooling",item="Leftovers"):
        if move is None:
            avmoves=["Hydro Pump","Water Spout","Double-Edge","Soak","Rest","Rain Dance","Scald","Ice Beam","Earth Power"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Toxapex
class Toxapex(Pokemon2):
    "Toxapex"
    def __init__(self,name="Toxapex",type1="Poison",type2="Water",nature=None,level=100,happiness=255,hp=50,atk=63,defense=152,spatk=53,spdef=142,speed=35,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability="Regenerator",item="Black Sludge"):
        if move is None:
            avmoves=["Baneful Bunker","Toxic","Liquidation","Toxic Spikes","Scald","Ice Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Mudsdale
class Mudsdale(Pokemon2):
    "Mudsdale"
    def __init__(self,name="Mudsdale",type1="Ground",type2=None,nature=None,level=100,happiness=255,hp=100,atk=125,defense=100,spatk=55,spdef=85,speed=35,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Stamina",item="Leftovers"):
        if move is None:
            avmoves=["High Horsepower","Stone Edge","Earthquake","Heavy Slam","Iron Defense"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Araquanid
class Araquanid(Pokemon2):
    "Araquanid"
    def __init__(self,name="Araquanid",type1="Water",type2="Bug",nature=None,level=100,happiness=255,hp=68,atk=70,defense=92,spatk=50,spdef=132,speed=42,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability="Water Absorb",item="Leftovers"):
        if move is None:
            avmoves=["Leech Life","Lunge","Liquidation","Crunch","Scald","Ice Beam","X-Scissor"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Salazzle
class Salazzle(Pokemon2):
    "Salazzle"
    def __init__(self,name="Salazzle",type1="Poison",type2="Fire",nature=None,level=100,happiness=255,hp=68,atk=64,defense=60,spatk=111,spdef=60,speed=117,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Corrosion",item="Black Sludge"):
        if move is None:
            avmoves=["Fire Lash","Toxic","Flamethrower","Toxic Spikes","Dragon Pulse","Nasty Plot","Sludge Bomb"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
#Bewear
class Bewear(Pokemon2):
    "Bewear"
    def __init__(self,name="Bewear",type1="Normal",type2="Fighting",nature=None,level=100,happiness=255,hp=120,atk=125,defense=80,spatk=55,spdef=60,speed=60,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Unnerve",item="Leftovers"):
        if move is None:
            avmoves=["Superpower","Double-Edge","Hammer Arm","Strength","High Horsepower","Zen Headbutt"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Tsareena
class Tsareena(Pokemon2):
    "Tsareena"
    def __init__(self,name="Tsareena",type1="Grass",type2=None,nature=None,level=100,happiness=255,hp=72,atk=120,defense=98,spatk=50,spdef=98,speed=72,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Queenly Majesty",item="Leftovers"):
        if move is None:
            avmoves=["Trop Kick","High Jump Kick","Power Whip","Play Rough","Grass Knot","U-Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Golisopod
class Golisopod(Pokemon2):
    "Golisopod"
    def __init__(self,name="Golisopod",type1="Bug",type2="Water",nature=None,level=100,happiness=255,hp=75,atk=125,defense=140,spatk=60,spdef=90,speed=40,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability="Tough Claws",item="Leftovers"):
        if move is None:
            avmoves=["Leech Life","First Impression","Liquidation","Crunch","Swords Dance","Ice Beam","X-Scissor","Razor Shell","Sucker Punch"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                                                                                                                 #Palossand
class Palossand(Pokemon2):
    "Palossand"
    def __init__(self,name="Palossand",type1="Ghost",type2="Ground",nature=None,level=100,happiness=255,hp=85,atk=75,defense=110,spatk=100,spdef=75,speed=35,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability="Water Compaction",item="Leftovers"):
        if move is None:
            avmoves=["Shore Up","Earth Power","Shadow Ball","Giga Drain","Sandstorm","Sludge Bomb"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Silvally
class Silvally(Pokemon2):
    "Silvally"
    def __init__(self,name="Silvally",type1=random.choice(["Rock","Fire","Water","Grass","Electric","Ground","Flying","Fighting","Fairy","Dragon","Steel","Poison","Dark","Ghost","Normal","Bug","Ice"]),type2=None,nature=None,level=100,happiness=255,hp=95,atk=95,defense=95,spatk=95,spdef=95,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["RKS System"]),item="Elemental Disks"):
        if move is None:
            avmoves=["Protect","Multi-Attack","Hyper Beam","Double-Edge","Crush Claw"]
            moves=moveset(avmoves)
        else:
            moves=move
        name=name+f"({type1})"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Turtonator
class Turtonator(Pokemon2):
    "Turtonator"
    def __init__(self,name="Turtonator",type1="Fire",type2="Dragon",nature=None,level=100,happiness=255,hp=60,atk=78,defense=135,spatk=91,spdef=85,speed=36,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability="Dauntless Shield",item="Leftovers"):
        if move is None:
            avmoves=["Shell Trap","Shell Smash","Overheat","Flamethrower","Dragon Pulse","Iron Defense"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Mimikyu
class Mimikyu(Pokemon2):
    "Mimikyu"
    def __init__(self,name="Mimikyu",type1="Ghost",type2="Fairy",nature=None,level=100,happiness=255,hp=55,atk=90,defense=80,spatk=50,spdef=105,speed=96,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Disguise",item="Leftovers"):
        if move is None:
            avmoves=["Shadow Sneak","Play Rough","Shadow Claw","Wood Hammer","Swords Dance"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Drampa
class Drampa(Pokemon2):
    "Drampa"
    def __init__(self,name="Drampa",type1="Normal",type2="Dragon",nature=None,level=100,happiness=255,hp=78,atk=60,defense=85,spatk=135,spdef=91,speed=36,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Berserk","Sap Sipper"]),item="Leftovers"):
        if move is None:
            avmoves=["Hyper Voice","Dragon Pulse","Extrasensory","Hyper Beam","Hurricane","Ice Beam","Energy Ball","Focus Blast","Heat Wave","Light Screen"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Dhelmise
class Dhelmise(Pokemon2):
    "Delmise"
    def __init__(self,name="Dhelmise",type1="Ghost",type2="Grass",nature=None,level=100,happiness=255,hp=70,atk=131,defense=100,spatk=86,spdef=90,speed=40,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Steelworker",item="Leftovers"):
        if move is None:
            avmoves=["Power Whip","Phantom Force","Anchor Shot","Shadow Ball","Heavy Slam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Kommo-o
class Kommo(Pokemon2):
    "Kommo-o"
    def __init__(self,name="Kommo-o",type1="Dragon",type2="Fighting",nature=None,level=100,happiness=255,hp=75,atk=110,defense=125,spatk=100,spdef=105,speed=85,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Overcoat","Bulletproof"]),item="Leftovers"):
        if move is None:
            avmoves=["Hyper Voice","Dragon Pulse","Clangorous Soul","Focus Blast","Aura Sphere","Clanging Scales","Flash Cannon"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Tapu Koko
class Tapukoko(Pokemon2):
    "Tapu Koko"
    def __init__(self,name="Tapu Koko",type1="Electric",type2="Fairy",nature=None,level=100,happiness=255,hp=70,atk=115,defense=85,spatk=95,spdef=75,speed=130,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Electric Surge"]),item="Leftovers"):
        if move is None:
            avmoves=["Nature's Madness","Wild Charge","Play Rough","Brave Bird","Thunder"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Tapu Lele
class Tapulele(Pokemon2):
    "Tapu Lele"
    def __init__(self,name="Tapu Lele",type1="Psychic",type2="Fairy",nature=None,level=100,happiness=255,hp=70,atk=85,defense=75,spatk=130,spdef=115,speed=95,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Psychic Surge"]),item="Leftovers"):
        if move is None:
            avmoves=["Nature's Madness","Extrasensory","Moonblast","Psyshock","Psychic"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Tapu Bulu
class Tapubulu(Pokemon2):
    "Tapu Bulu"
    def __init__(self,name="Tapu Bulu",type1="Grass",type2="Fairy",nature=None,level=100,happiness=255,hp=70,atk=130,defense=115,spatk=85,spdef=95,speed=75,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Grassy Surge"]),item="Leftovers"):
        if move is None:
            avmoves=["Nature's Madness","Horn Leech","Play Rough","Wood Hammer","Zen Headbutt"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Tapu Fini
class Tapufini(Pokemon2):
    "Tapu Fini"
    def __init__(self,name="Tapu Fini",type1="Water",type2="Fairy",nature=None,level=100,happiness=255,hp=70,atk=75,defense=115,spatk=95,spdef=130,speed=85,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Misty Surge"]),item="Leftovers"):
        if move is None:
            avmoves=["Nature's Madness","Hydro Pump","Moonblast","Surf"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Solgaleo
class Solgaleo(Pokemon2):
    "Solgaleo"
    def __init__(self,name="Solgaleo",type1="Psychic",type2="Steel",nature=None,level=100,happiness=255,hp=137,atk=137,defense=107,spatk=113,spdef=89,speed=97,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Full Metal Body"]),item="Leftovers"):
        if move is None:
            avmoves=["Sunsteel Strike","Flare Blitz","Solar Beam","Wild Charge","Morning Sun","Zen Headbutt"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Radiant Sun Solgaleo
class RSSolgaleo(Pokemon2):
    "Solgaleo"
    def __init__(self,name="Radiant Sun Solgaleo",type1="Psychic",type2="Steel",nature=None,level=100,happiness=255,hp=137,atk=157,defense=107,spatk=113,spdef=89,speed=97,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Full Metal Body"]),item="Leftovers"):
        if move is None:
            avmoves=["Sunsteel Strike","Flare Blitz","Solar Beam","Wild Charge","Morning Sun","Zen Headbutt"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Lunala
class Lunala(Pokemon2):
    "Lunala"
    def __init__(self,name="Lunala",type1="Psychic",type2="Ghost",nature=None,level=100,happiness=255,hp=137,atk=113,defense=89,spatk=157,spdef=107,speed=97,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Shadow Shield"]),item="Leftovers"):
        if move is None:
            avmoves=["Moongeist Beam","Phamtom Force","Moonblast","Night Daze","Moonlight","Shadow Ball","Psychic"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Full Moon Lunala
class FMLunala(Pokemon2):
    "Lunala"
    def __init__(self,name="Full Moon Lunala",type1="Psychic",type2="Ghost",nature=None,level=100,happiness=255,hp=137,atk=113,defense=89,spatk=137,spdef=107,speed=97,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Shadow Shield"]),item="Leftovers"):
        if move is None:
            avmoves=["Moongeist Beam","Phamtom Force","Moonblast","Night Daze","Moonlight","Shadow Ball","Psychic"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Dusk Mane Necrozma
class DMNecrozma(Pokemon2):
    "Necrozma"
    def __init__(self,name="Dusk Mane Necrozma",type1="Psychic",type2="Steel",nature=None,level=100,happiness=255,hp=97,atk=157,defense=127,spatk=113,spdef=109,speed=77,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Prism Armor"]),item="Leftovers"):
        if move is None:
            avmoves=["Sunsteel Strike","Flare Blitz","Solar Beam","Photon Geyser","Prismatic Laser","Morning Sun","Zen Headbutt"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Dawn Wing Necrozma
class DWNecrozma(Pokemon2):
    "Necrozma"
    def __init__(self,name="Dawn Wing Necrozma",type1="Psychic",type2="Ghost",nature=None,level=100,happiness=255,hp=97,atk=113,defense=109,spatk=157,spdef=127,speed=77,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Prism Armor"]),item="Leftovers"):
        if move is None:
            avmoves=["Moongeist Beam","Shadow Ball","Moonblast","Photon Geyser","Prismatic Laser","Moonlight","Psychic"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Necrozma
class Necrozma(Pokemon2):
    "Necrozma"
    def __init__(self,name="Necrozma",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=97,atk=107,defense=101,spatk=127,spdef=89,speed=79,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Prism Armor"]),item="Leftovers"):
        if move is None:
            avmoves=["Moonlight","Iron Defense","Rock Blast","Photon Geyser","Prismatic Laser","Morning Sun"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Nihilego
class Nihilego(Pokemon2):
    "Nihilego"
    def __init__(self,name="Nihilego",type1="Rock",type2="Poison",nature=None,level=100,happiness=255,hp=109,atk=53,defense=47,spatk=127,spdef=131,speed=103,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Beast Boost"]),item="Leftovers"):
        if move is None:
            avmoves=["Venom Drench","Iron Defense","Toxic Spikes","Stealth Rock","Venoshock","Power Gem"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Buzzwole
class Buzzwole(Pokemon2):
    "Buzzwole"
    def __init__(self,name="Buzzwole",type1="Bug",type2="Fighting",nature=None,level=100,happiness=255,hp=107,atk=139,defense=139,spatk=53,spdef=53,speed=79,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Beast Boost"]),item="Leftovers"):
        if move is None:
            avmoves=["Lunge","Superpower","Bulk Up","Fell Stinger","Power-up Punch","Close Combat","Drain Punch"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Pheromosa
class Pheromosa(Pokemon2):
    "Pheromosa"
    def __init__(self,name="Pheromosa",type1="Rock",type2="Poison",nature=None,level=100,happiness=255,hp=71,atk=137,defense=37,spatk=137,spdef=37,speed=151,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Beast Boost"]),item="Leftovers"):
        if move is None:
            avmoves=["U-Turn","Triple Axel","High Jump Kick","Quiver Dance","Bug Buzz","Lunge"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                                                                                                                 #Xurkitree
class Xurkitree(Pokemon2):
    "Xurkitree"
    def __init__(self,name="Xurkitree",type1="Electric",type2=None,nature=None,level=100,happiness=255,hp=83,atk=89,defense=71,spatk=173,spdef=71,speed=83,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Beast Boost"]),item="Leftovers"):
        if move is None:
            avmoves=["Eerie Impulse","Thunderbolt","Electric Terrain","Power Whip","Discharge","Hypnosis"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Celesteela
class Celesteela(Pokemon2):
    "Celesteela"
    def __init__(self,name="Celesteela",type1="Steel",type2="Flying",nature=None,level=100,happiness=255,hp=97,atk=101,defense=103,spatk=107,spdef=101,speed=61,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability=random.choice(["Beast Boost"]),item="Leftovers"):
        if move is None:
            avmoves=["Heavy Slam","Iron Defense","Leech Seed","Flash Cannon","Giga Drain"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Kartana
class Kartana(Pokemon2):
    "Kartana"
    def __init__(self,name="Kartana",type1="Grass",type2="Steel",nature=None,level=100,happiness=255,hp=59,atk=181,defense=131,spatk=59,spdef=31,speed=109,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Beast Boost"]),item="Leftovers"):
        if move is None:
            avmoves=["Swords Dance","Sacred Sword","Leaf Blade","Night Slash","Smart Strike"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Guzzlord
class Guzzlord(Pokemon2):
    "Guzzlord"
    def __init__(self,name="Guzzlord",type1="Dark",type2="Dragon",nature=None,level=100,happiness=255,hp=223,atk=101,defense=53,spatk=97,spdef=53,speed=43,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Beast Boost"]),item="Leftovers"):
        if move is None:
            avmoves=["Heavy Slam","Belch","Hammer Arm","Stomping Tantrum","Knock Off","Dragon Rush"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Necrozma
class UNecrozma(Pokemon2):
    "Necrozma"
    def __init__(self,name="Ultra Necrozma",type1="Psychic",type2="Dragon",nature=None,level=100,happiness=255,hp=97,atk=167,defense=97,spatk=167,spdef=97,speed=129,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Neuroforce"]),item="Leftovers"):
        if move is None:
            avmoves=["Moonlight","Iron Defense","Rock Blast","Photon Geyser","Prismatic Laser","Morning Sun"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Magearna
class Magearna(Pokemon2):
    "Magearna"
    def __init__(self,name="Magearna",type1="Steel",type2="Fairy",nature=None,level=100,happiness=255,hp=80,atk=95,defense=115,spatk=130,spdef=115,speed=65,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Soul-Heart"]),item="Leftovers"):
        if move is None:
            avmoves=["Fleur Cannon","Zap Cannon","Flash Cannon","Aura Sphere"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                                                                                                                 #Marshadow
class Marshadow(Pokemon2):
    "Marshadow"
    def __init__(self,name="Marshadow",type1="Fighting",type2="Ghost",nature=None,level=100,happiness=255,hp=90,atk=125,defense=80,spatk=90,spdef=90,speed=125,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Technician"]),item="Leftovers"):
        if move is None:
            avmoves=["Spectral Thief","Superpower","Bulk Up","Drain Punch","Power-up Punch","Close Combat","Sucker Punch","Shadow Sneak"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Naganadel
class Naganadel (Pokemon2):
    "Naganadel"
    def __init__(self,name="Naganadel",type1="Poison",type2="Dragon",nature=None,level=100,happiness=255,hp=73,atk=73,defense=73,spatk=127,spdef=73,speed=121,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Beast Boost"]),item="Leftovers"):
        if move is None:
            avmoves=["Dragon Pulse","Sludge Wave","Nasty Plot","Dark Pulse"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                                                                                                                 #Stakataka
class Stakataka(Pokemon2):
    "Stakataka"
    def __init__(self,name="Stakataka",type1="Rock",type2="Steel",nature=None,level=100,happiness=255,hp=61,atk=131,defense=211,spatk=53,spdef=101,speed=13,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability=random.choice(["Beast Boost"]),item="Leftovers"):
        if move is None:
            avmoves=["Iron Head","Iron Defense","Double-Edge","Stealth Rock","Heavy Slam","Rock Slide"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Blacephalon
class Blacephalon(Pokemon2):
    "Blacephalon"
    def __init__(self,name="Blacephalon",type1="Fire",type2="Ghost",nature=None,level=100,happiness=255,hp=53,atk=127,defense=53,spatk=151,spdef=79,speed=107,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Beast Boost"]),item="Leftovers"):
        if move is None:
            avmoves=["Mind Blown","Fire Blast","Shadow Ball","Mystical Fire"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Zeraora
class Zeraora(Pokemon2):
    "Zeraora"
    def __init__(self,name="Zeraora",type1="Electric",type2=None,nature=None,level=100,happiness=255,hp=88,atk=112,defense=75,spatk=102,spdef=80,speed=143,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Volt Absorb"]),item="Leftovers"):
        if move is None:
            avmoves=["Plasma Fists","Close Combat","Wild Charge","Thunder Punch","Volt Switch","Power-up Punch"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Melmetal
class Melmetal(Pokemon2):
    "Melmetal"
    def __init__(self,name="Melmetal",type1="Steel",type2=None,nature=None,level=100,happiness=255,hp=135,atk=143,defense=143,spatk=80,spdef=65,speed=34,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Iron Fist"]),item="Leftovers"):
        if move is None:
            avmoves=["Double Iron Bash","Superpower","Thunder Punch","Ice Punch","Fire Punch","Iron Defense"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
                                                                                                         #Galarian Rapidash
class GRapidash(Pokemon2):
    "Rapidash"
    def __init__(self,name="Galarian Rapidash",type1="Psychic",type2="Fairy",nature=None,level=100,happiness=255,hp=65,atk=100,defense=70,spatk=80,spdef=80,speed=125,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Flash Fire","Reckless"]),item="Leftovers"):
        if move is None:
            avmoves=["Megahorn","Psycho Cut","Paly Rough","Drill Run","High Horsepower","Wild Charge","Flare Blitz"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Slowbro
class GSlowbro(Pokemon2):
    "Slowbro"
    def __init__(self,name="Galarian Slowbro",type1="Poison",type2="Psychic",nature=None,level=100,happiness=255,hp=95,atk=100,defense=95,spatk=100,spdef=70,speed=30,hpev=0,atkev=0,defev=252,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Regenerator",item="Leftovers"):
        if move is None:
            avmoves=["Hidden Power","Ice Beam","Slack Off","Psychic","Flamethrower","Sludge Bomb","Thunderbolt","Iron Defense","Rain Dance","Shell Side Arm"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Weezing
class GWeezing(Pokemon2):
    "Weezing"
    def __init__(self,name="Galarian Weezing",type1="Poison",type2="Fairy",nature=None,level=100,happiness=255,hp=65,atk=90,defense=120,spatk=85,spdef=70,speed=60,hpev=0,atkev=0,defev=252,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Levitate","Misty Surge"]),item="Black Sludge"):
        if move is None:
            avmoves=["Sludge Bomb","Toxic","Venoshock","Explosion","Toxic Spikes","Strange Stream"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Articuno
class GArticuno    (Pokemon2):
    "Articuno"
    def __init__(self,name="Galarian Articuno",type1="Psychic",type2="Flying",nature=None,level=100,happiness=255,hp=90,atk=85,defense=85,spatk=125,spdef=100,speed=95,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Competitive",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hidden Power","Psychic","Freezing Glare","Extrasensory","Brave Bird","Sky Attack","Roost"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      
#Zapdos
class GZapdos(Pokemon2):
    "Zapdos"
    def __init__(self,name="Galarian Zapdos",type1="Fighting",type2="Flying",nature=None,level=100,happiness=255,hp=90,atk=125,defense=90,spatk=85,spdef=90,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Defiant",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hidden Power","Thunderous Kick","Brave Bird","Close Combat","Sky Attack","Roost","Bulk Up"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)             
#Moltres
class GMoltres(Pokemon2):
    "Moltres"
    def __init__(self,name="Galarian Moltres",type1="Dark",type2="Flying",nature=None,level=100,happiness=255,hp=90,atk=85,defense=90,spatk=100,spdef=125,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Berserk",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hidden Power","Fiery Wrath","Hurricane","Nasty Plot","Sky Attack","Brave Bird","Sucker Punch","Roost"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Slowking
class GSlowking(Pokemon2):
    "Slowking"
    def __init__(self,name="Galarian Slowking",type1="Poison",type2="Psychic",nature=None,level=100,happiness=255,hp=95,atk=65,defense=80,spatk=110,spdef=110,speed=30,hpev=0,atkev=0,defev=252,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Curious Medicine",item="Leftovers"):
        if move is None:
            avmoves=["Hidden Power","Ice Beam","Slack Off","Psychic","Flamethrower","Sludge Bomb","Thunderbolt","Iron Defense","Rain Dance","Eerie Spell"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Rillaboom
class Rillaboom(Pokemon2):
    "Rillaboom"
    def __init__(self,name="Rillaboom",type1="Grass",type2=None,nature=None,level=100,happiness=255,hp=100,atk=125,defense=90,spatk=60,spdef=70,speed=85,hpev=0,atkev=252,defev=4,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Grassy Surge","Overgrow"]),item="Choice Band"):
        if move is None:
            avmoves=["Drum Beating","Wood Hammer","Grassy Glide","Swords Dance","Knock Off","Superpower"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Cinderace
class Cinderace(Pokemon2):
    "Cinderace"
    def __init__(self,name="Cinderace",type1="Fire",type2=None,nature=None,level=100,happiness=255,hp=80,atk=116,defense=75,spatk=65,spdef=75,speed=119,hpev=80,atkev=164,defev=0,spatkev=0,spdefev=48,speedev=216,maxiv="No",move=None, ability=random.choice(["Libero","Blaze"]),item="Heavy-Duty Boots"):
        if move is None:
            avmoves=["Pyro Ball","Court Change","U-Turn","Sucker Punch","Gunk Shot","Zen Headbutt"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Inteleon
class Inteleon(Pokemon2):
    "Inteleon"
    def __init__(self,name="Inteleon",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=70,atk=65,defense=65,spatk=125,spdef=65,speed=120,hpev=0,atkev=0,defev=4,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Sniper","Torrent"]),item=random.choice(["Expert Belt","Scope Lens"])):
        if move is None:
            avmoves=["Snipe Shot","Ice Beam","Shadow Ball","U-Turn","Knock Off","Hydro Pump"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Corviknight
class Corviknight(Pokemon2):
    "Corviknight"
    def __init__(self,name="Corviknight",type1="Flying",type2="Steel",nature=None,level=100,happiness=255,hp=98,atk=87,defense=105,spatk=53,spdef=85,speed=67,hpev=252,atkev=252,defev=4,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Pressure","Mirror Armor"]),item="Leftovers"):
        if move is None:
            avmoves=["Roost","Brave Bird","Defog","U-Turn","Body Press","Steel Wing"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Orbeetle
class Orbeetle(Pokemon2):
    "Orbeetle"
    def __init__(self,name="Orbeetle",type1="Bug",type2="Psychic",nature=None,level=100,happiness=255,hp=60,atk=45,defense=110,spatk=80,spdef=120,speed=90,hpev=0,atkev=0,defev=4,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Swarm","Frisk"]),item="Expert Belt"):
        if move is None:
            avmoves=["Reflect","Light Screen","Sticky Web","U-Turn","Body Press","Calm Mind"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Coalossal
class Coalossal(Pokemon2):
    "Coalossal"
    def __init__(self,name="Coalossal",type1="Rock",type2="Fire",nature=None,level=100,happiness=255,hp=110,atk=80,defense=120,spatk=80,spdef=90,speed=30,hpev=252,atkev=0,defev=4,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Steam Engine","Flash Fire"]),item="Heavy-Duty Boots"):
        if move is None:
            avmoves=["Stealth Rock","Rock Blast","Flamethrower","Rapid Spin","Earth Power","Body Press"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
#Flapple
class Flapple(Pokemon2):
    "Flapple"
    def __init__(self,name="Flapple",type1="Grass",type2="Dragon",nature=None,level=100,happiness=255,hp=75,atk=110,defense=80,spatk=95,spdef=60,speed=70,hpev=0,atkev=0,defev=4,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Ripen","Hustle"]),item="Life Orb"):
        if move is None:
            avmoves=["Grab Apple","Outrage","Sucker Punch","U-Turn","Grassy Glide","Dragon Pulse"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Appletun
class Appletun(Pokemon2):
    "Appletun"
    def __init__(self,name="Appletun",type1="Grass",type2="Dragon",nature=None,level=100,happiness=255,hp=110,atk=85,defense=80,spatk=100,spdef=80,speed=30,hpev=252,atkev=0,defev=4,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Ripen","Thick Fat"]),item="Leftovers"):
        if move is None:
            avmoves=["Draco Meteor","Outrage","Apple Acid","Recover","Giga Drain","Dragon Pulse","Leech Seed"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Sandaconda
class Sandaconda(Pokemon2):
    "Sandaconda"
    def __init__(self,name="Sandaconda",type1="Ground",type2=None,nature=None,level=100,happiness=255,hp=72,atk=107,defense=125,spatk=65,spdef=70,speed=71,hpev=252,atkev=252,defev=4,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Sand Spit","Sand Veil"]),item="Leftovers"):
        if move is None:
            avmoves=["Coil","Sandstorm","Glare","Recover","Earthquake","Drill Run","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                                                                                                                 #Centiskorch
class Centiskorch(Pokemon2):
    "Centiskorch"
    def __init__(self,name="Centiskorch",type1="Fire",type2="Bug",nature=None,level=100,happiness=255,hp=100,atk=115,defense=65,spatk=90,spdef=90,speed=65,hpev=252,atkev=252,defev=4,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Flash Fire","Flame Body"]),item="Leftovers"):
        if move is None:
            avmoves=["Lunge","Fire Lash","Coil","Crunch","Inferno","Power Whip","X-Scissor","Flare Blitz","Leech Life"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Toxtricity
class Toxtricity(Pokemon2):
    "Toxtricity"
    def __init__(self,name="Toxtricity",type1="Electric",type2="Poison",nature=random.choice(naturelist),level=100,happiness=255,hp=75,atk=98,defense=70,spatk=114,spdef=70,speed=75,hpev=0,atkev=0,defev=4,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Punk Rock","Technician"]),item="Leftovers"):
        if move is None:
            avmoves=["Boomburst","Overdrive","Sludge Wave","Hyper Voice","Volt Switch"]
            moves=moveset(avmoves)
        if nature in ['Hardy', 'Brave', 'Adamant', 'Naughty', 'Docile', 'Impish', 'Lax', 'Hasty', 'Jolly', 'Naive', 'Rash', 'Sassy','Quirky']:
            name="Amped "+name
        if nature not in ['Hardy', 'Brave', 'Adamant', 'Naughty', 'Docile', 'Impish', 'Lax', 'Hasty', 'Jolly', 'Naive', 'Rash', 'Sassy','Quirky']:
            name="Low Key "+name
        if move is not None:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Barraskewda
class Barraskewda(Pokemon2):
    "Barraskewda"
    def __init__(self,name="Barraskewda",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=61,atk=123,defense=60,spatk=60,spdef=50,speed=136,hpev=0,atkev=252,defev=4,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Propeller Tail","Swift Swim"]),item="Leftovers"):
        if move is None:
            avmoves=["Liquidation","Double-Edge","Aqua Jet","Crunch","Psychic Fangs","Close Combat","Poison Jab","Waterfall","Ice Fang"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Grapplot
class Grapplot(Pokemon2):
    "Grapplot"
    def __init__(self,name="Grapplot",type1="Fighting",type2=None,nature=None,level=100,happiness=255,hp=80,atk=118,defense=90,spatk=70,spdef=80,speed=42,hpev=252,atkev=252,defev=4,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Technician","Limber"]),item="Leftovers"):
        if move is None:
            avmoves=["Octolock","Superpower","Topsy-Turvy","Submission","Bulk Up","Close Combat","Focus Blast","Brick Break","Octazooka"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Polteageist
class Polteageist (Pokemon2):
    "Polteageist"
    def __init__(self,name="Polteageist",type1="Ghost",type2=None,nature=None,level=100,happiness=255,hp=60,atk=65,defense=65,spatk=134,spdef=114,speed=70,hpev=0,atkev=0,defev=4,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Weak Armor"]),item="Focus Sash"):
        if move is None:
            avmoves=["Shell Smash","Giga Drain","Shadow Ball","Stored Power"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Hatterene
class Hatterene(Pokemon2):
    "Hatterene"
    def __init__(self,name="Hatterene",type1="Psychic",type2="Fairy",nature=None,level=100,happiness=255,hp=57,atk=90,defense=95,spatk=136,spdef=103,speed=29,hpev=252,atkev=0,defev=4,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Magic Bounce"]),item="Leftovers"):
        if move is None:
            avmoves=["Calm Mind","Dazzling Gleam","Mystical Fire","Moonblast","Psychic"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Grimmsnarl
class Grimmsnarl(Pokemon2):
    "Grimmsnarl"
    def __init__(self,name="Grimmsnarl",type1="Dark",type2="Fairy",nature=None,level=100,happiness=255,hp=95,atk=120,defense=65,spatk=95,spdef=75,speed=60,hpev=252,atkev=252,defev=4,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Prankster"]),item="Leftovers"):
        if move is None:
            avmoves=["Light Screen","Reflect","Spirit Break","Play Rough","Dark Pulse","Sucker Punch","False Surrender"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Obstagoon
class Obstagoon(Pokemon2):
    "Obstagoon"
    def __init__(self,name="Obstagoon",type1="Dark",type2="Normal",nature=None,level=100,happiness=255,hp=93,atk=90,defense=101,spatk=60,spdef=81,speed=95,hpev=0,atkev=252,defev=4,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Guts","Defiant"]),item="Leftovers"):
        if move is None:
            avmoves=["Obstruct","Double-Edge","Close Combat","Snarl","Night Slash","Sucker Punch","Throat Chop"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Kleavor
class Kleavor(Pokemon2):
    "Kealvor"
    def __init__(self,name="Kleavor",type1="Bug",type2="Rock",nature=None,level=100,happiness=255,hp=70,atk=135,defense=95,spatk=45,spdef=70,speed=85,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Technician",item="Life Orb"):
        if move is None:
            avmoves=["Protect","Stone Axe","Stealth Rock","X-Scissor","U-Turn","Swords Dance","Close Combat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Perrserker
class Perrserker(Pokemon2):
    "Perrserker"
    def __init__(self,name="Perrserker",type1="Steel",type2=None,nature=None,level=100,happiness=255,hp=70,atk=110,defense=100,spatk=50,spdef=60,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Tough Claws",item="Life Orb"):
        if move is None:
            avmoves=["Protect","Iron Head","Slash","Iron Defense","Play Rough","Swords Dance","Close Combat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Sirfetchd
class Sirfetchd(Pokemon2):
    "Sirfetchd"
    def __init__(self,name="Sirfetch'd",type1="Fighting",type2=None,nature=None,level=100,happiness=255,hp=62,atk=135,defense=95,spatk=68,spdef=82,speed=65,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Scrappy"]),item="Leftovers"):
        if move is None:
            avmoves=["Swords Dance","Sacred Sword","Leaf Blade","Night Slash","Meteor Assault","Brave Bird"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #MrRime
class MrRime(Pokemon2):
    "MrRime"
    def __init__(self,name="Mr.Rime",type1="Ice",type2="Psychic",nature=None,level=100,happiness=255,hp=80,atk=85,defense=75,spatk=110,spdef=100,speed=70,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Ice Body",item="Leftovers"):
        if move is None:
            avmoves=["Psychic","Ice Shard","Freeze-Dry","Sucker Punch","Dazzling Gleam","Grass Knot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Alcremie
class Alcremie(Pokemon2):
    "Alcremie"
    def __init__(self,name="Alcremie",type1="Fairy",type2=None,nature=None,level=100,happiness=255,hp=65,atk=60,defense=75,spatk=110,spdef=121,speed=64,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Sweet Veil",item="Leftovers"):
        if move is None:
            avmoves=["Decorate","Misty Terrain","Freeze-Dry","Draining Kiss","Dazzling Gleam","Calm Mind"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Frosmoth
class Frosmoth(Pokemon2):
    "Frosmoth"
    def __init__(self,name="Frosmoth",type1="Ice",type2="Bug",nature=None,level=100,happiness=255,hp=70,atk=65,defense=60,spatk=125,spdef=90,speed=65,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Ice Scales",item="Leftovers"):
        if move is None:
            avmoves=["Defog","Ice Shard","Freeze-Dry","Bug Buzz","Tailwind","Quiver Dance"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Indeedee
class Indeedee(Pokemon2):
    "Indeedee"
    def __init__(self,name="Indeedee",type1="Psychic",type2="Normal",nature=None,level=100,happiness=255,hp=60,atk=65,defense=55,spatk=105,spdef=95,speed=95,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Psychic Surge",item="Leftovers"):
        if move is None:
            avmoves=["Psychic","Expanding Force","Calm Mind","Stored Power"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Copperajah
class Copperajah(Pokemon2):
    "Copperajah"
    def __init__(self,name="Copperajah",type1="Steel",type2=None,nature=None,level=100,happiness=255,hp=122,atk=130,defense=69,spatk=80,spdef=69,speed=30,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Sheer Force",item="Leftovers"):
        if move is None:
            avmoves=["Heavy Slam","High Horsepower","Iron Head","Play Rough","Bulldoze"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Dracozolt
class Dracozolt(Pokemon2):
    "Dracozolt"
    def __init__(self,name="Dracozolt",type1="Electric",type2="Dragon",nature=None,level=100,happiness=255,hp=90,atk=100,defense=90,spatk=80,spdef=70,speed=75,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Sand Rush",item="Leftovers"):
        if move is None:
            avmoves=["Bolt Beak","Dragon Rush","Dragon Tail","Wild Charge","Earthquake"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Dracovish
class Dracovish(Pokemon2):
    "Dracovish"
    def __init__(self,name="Dracovish",type1="Water",type2="Dragon",nature=None,level=100,happiness=255,hp=90,atk=90,defense=100,spatk=70,spdef=80,speed=75,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Strong Jaw",item="Choice Band"):
        if move is None:
            avmoves=["Fishious Rend","Dragon Rush","Ice Fang","Thunder Fang","Earthquake"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Duraludon
class Duraludon(Pokemon2):
    "Duraludon"
    def __init__(self,name="Duraludon",type1="Steel",type2="Dragon",nature=None,level=100,happiness=255,hp=70,atk=95,defense=115,spatk=120,spdef=50,speed=85,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Stalwart",item="Leftovers"):
        if move is None:
            avmoves=["Draco Meteor","Steel Beam","Flash Cannon","Dark Pulse","Iron Defense"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Dragapult
class Dragapult(Pokemon2):
    "Dragapult"
    def __init__(self,name="Dragapult",type1="Dragon",type2="Ghost",nature=None,level=100,happiness=255,hp=88,atk=120,defense=75,spatk=100,spdef=75,speed=142,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Infiltrator",item="Choice Band"):
        if move is None:
            avmoves=["Dragon Darts","Draco Meteor","Phantom Force","Flamethrower","Thunderbolt","U-Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Zacian
class Zacian(Pokemon2):
    "Zacian"
    def __init__(self,name="Crowned Sword Zacian",type1="Fairy",type2="Steel",nature=None,level=100,happiness=255,hp=92,atk=170,defense=115,spatk=80,spdef=115,speed=148,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Intrepid Sword",item="Rusted Sword"):
        if move is None:
            avmoves=["Behemoth Blade","Play Rough","Protect","Crunch","Swords Dance"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Zamazenta
class Zamazenta(Pokemon2):
    "Zamazenta"
    def __init__(self,name="Crowned Shield Zamazenta",type1="Fighting",type2="Steel",nature=None,level=100,happiness=255,hp=92,atk=130,defense=145,spatk=80,spdef=145,speed=128,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Dauntless Shield",item="Rusted Shield"):
        if move is None:
            avmoves=["Behemoth Bash","Close Combat","Protect","Crunch","Swords Dance"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                                                                                                                 #Eternatus
class Eternatus(Pokemon2):
    "Eternatus"
    def __init__(self,name="Eternatus",type1="Poison",type2="Dragon",nature=None,level=100,happiness=255,hp=140,atk=85,defense=95,spatk=145,spdef=95,speed=130,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Pressure",item="Black Sludge"):
        if move is None:
            avmoves=["Dynamax Cannon","Eternabeam","Flamethrower","Sludge Bomb"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Urshifu
class DUrshifu(Pokemon2):
    "Urshifu"
    def __init__(self,name="Single Strike Urshifu",type1="Fighting",type2="Dark",nature=None,level=100,happiness=255,hp=100,atk=130,defense=100,spatk=63,spdef=60,speed=97,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Unseen Fist",item="Choice Band"):
        if move is None:
            avmoves=["Wicked Blow","Close Combat","U-Turn","Sucker Punch"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Urshifu
class WUrshifu(Pokemon2):
    "Urshifu"
    def __init__(self,name="Rapid Strike Urshifu",type1="Fighting",type2="Water",nature=None,level=100,happiness=255,hp=100,atk=130,defense=100,spatk=63,spdef=60,speed=97,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Unseen Fist",item="Choice Band"):
        if move is None:
            avmoves=["Surging Strikes","Close Combat","U-Turn","Aqua Jet"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Zarude
class Zarude(Pokemon2):
    "Zarude"
    def __init__(self,name="Zarude",type1="Dark",type2="Grass",nature=None,level=100,happiness=255,hp=105,atk=120,defense=105,spatk=70,spdef=95,speed=105,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Leaf Guard",item="Leftovers"):
        if move is None:
            avmoves=["Jungle Healing","Power Whip","U-Turn","Darkest Lariat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Regieleki
class Regieleki(Pokemon2):
    "Regieleki"
    def __init__(self,name="Regieleki",type1="Electric",type2=None,nature=None,level=100,happiness=255,hp=80,atk=100,defense=50,spatk=100,spdef=50,speed=200,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Transistor",item="Life Orb"):
        if move is None:
            avmoves=["Thunder Cage","Explosion","Thunderbolt","Thunder"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Regidrago
class Regidrago(Pokemon2):
    "Regidrago"
    def __init__(self,name="Regidrago",type1="Dragon",type2=None,nature=None,level=100,happiness=255,hp=200,atk=100,defense=50,spatk=100,spdef=50,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Dragon's Maw",item="Leftovers"):
        if move is None:
            avmoves=["Dragon Energy","Explosion","Dragon Pulse","Hyper Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Glastrier
class Glastrier(Pokemon2):
    "Glastrier"
    def __init__(self,name="Glastrier",type1="Ice",type2=None,nature=None,level=100,happiness=255,hp=100,atk=145,defense=130,spatk=65,spdef=110,speed=30,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Chilling Neigh",item="Leftovers"):
        if move is None:
            avmoves=["Swords Dance","Icicle Crash","High Horsepower","Close Combat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Spectrier
class Spectrier(Pokemon2):
    "Spectrier"
    def __init__(self,name="Spectrier",type1="Ghost",type2=None,nature=None,level=100,happiness=255,hp=100,atk=65,defense=60,spatk=145,spdef=80,speed=130,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Grim Neigh",item="Leftovers"):
        if move is None:
            avmoves=["Nasty Plot","Shadow Ball","Dark Pulse","Hex"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Calyrex
class ICalyrex(Pokemon2):
    "Calyrex"
    def __init__(self,name="Ice Rider Calyrex",type1="Psychic",type2="Ice",nature=None,level=100,happiness=255,hp=100,atk=165,defense=150,spatk=85,spdef=130,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="As One",item="Leftovers"):
        if move is None:
            avmoves=["Swords Dance","Glacial Lance","High Horsepower","Close Combat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Calyrex
class SCalyrex(Pokemon2):
    "Calyrex"
    def __init__(self,name="Shadow Rider Calyrex",type1="Psychic",type2="Ghost",nature=None,level=100,happiness=255,hp=100,atk=85,defense=80,spatk=165,spdef=100,speed=150,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="As One",item="Leftovers"):
        if move is None:
            avmoves=["Nasty Plot","Astral Barrage","Dark Pulse","Hex"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Cetitan
class Cetitan(Pokemon2):
    "Cetitan"
    def __init__(self,name="Cetitan",type1="Ice",type2=None,nature=None,level=100,happiness=255,hp=100,atk=125,defense=90,spatk=55,spdef=100,speed=70,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Thick Fat","Slush Rush"]),item="Leftovers"):
        if move is None:
            avmoves=["Swords Dance","Icicle Crash","Protect","Stone Edge","Mountain Gale"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Koraidon
class Koraidon(Pokemon2):
    "Koraidon"
    def __init__(self,name="Koraidon",type1="Dragon",type2="Fighting",nature=None,level=100,happiness=255,hp=80,atk=150,defense=100,spatk=130,spdef=90,speed=130,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Mold Breaker","Scrappy"]),item="Leftovers"):
        if move is None:
            avmoves=["Extreme Speed","Dragon Pulse","Superpower","Focus Blast","Aura Sphere","Close Combat","Dragon Claw","Draco Meteor"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Miraidon
class Miraidon(Pokemon2):
    "Miraidon"
    def __init__(self,name="Miraidon",type1="Dragon",type2="Electric",nature=None,level=100,happiness=255,hp=80,atk=130,defense=90,spatk=150,spdef=100,speed=130,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Mold Breaker","Transistor"]),item="Leftovers"):
        if move is None:
            avmoves=["Extreme Speed","Dragon Pulse","Thunderbolt","Thunder","Volt Switch","Wild Charge","Dragon Claw","Draco Meteor"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Enamorus
class Enamorus(Pokemon2):
    "Enamorus"
    def __init__(self,name="Enamorus",type1="Fairy",type2="Flying",nature=None,level=100,happiness=255,hp=74,atk=115,defense=70,spatk=135,spdef=80,speed=106,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Trace","Fairy Aura"]),item="Leftovers"):
        if move is None:
            avmoves=["Springtide Storm","Moonblast","Extrasensory","Focus Blast","Draining Kiss","Hurricane"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Enamorus
class TEnamorus(Pokemon2):
    "Enamorus"
    def __init__(self,name="Therian Enamorus",type1="Fairy",type2="Flying",nature=None,level=100,happiness=255,hp=74,atk=115,defense=110,spatk=135,spdef=100,speed=46,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Trace","Fairy Aura"]),item="Leftovers"):
        if move is None:
            avmoves=["Springtide Storm","Moonblast","Extrasensory","Focus Blast","Draining Kiss","Hurricane"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Butterfree
class Butterfree(Pokemon2):
    "Butterfree"
    def __init__(self,name="Butterfree",type1="Bug",type2="Flying",nature=None,level=100,happiness=255,hp=60,atk=45,defense=60,spatk=100,spdef=90,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Tinted Lens","Compound Eyes"]),item="Leftovers"):
        if move is None:
            avmoves=["Quiver Dance","Air Slash","Bug Buzz","Tailwind","Psychic","Sleep Powder"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                                                                                                                 #Beedrill
class Beedrill(Pokemon2):
    "Beedrill"
    def __init__(self,name="Beedrill",type1="Bug",type2="Poison",nature=None,level=100,happiness=255,hp=65,atk=90,defense=40,spatk=45,spdef=80,speed=75,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Sniper",item="Black Sludge"):
        if move is None:
            avmoves=["Poison Jab","Knock Off","Sludge Bomb","Drill Run","Toxic Spikes"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Raticate
class Raticate(Pokemon2):
    "Raticate"
    def __init__(self,name="Raticate",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=65,atk=91,defense=60,spatk=45,spdef=70,speed=97,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Guts",item="Flame Orb"):
        if move is None:
            avmoves=["Swords Dance","Knock Off","Crunch","Sucker Punch","Double-Edge"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#ARaticate
class ARaticate(Pokemon2):
    "Raticate"
    def __init__(self,name="Alolan Raticate",type1="Normal",type2="Dark",nature=None,level=100,happiness=255,hp=75,atk=91,defense=70,spatk=40,spdef=80,speed=77,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Thick Fat",item="Sitrus Berry"):
        if move is None:
            avmoves=["Swords Dance","Knock Off","Crunch","Sucker Punch","Double-Edge"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Fearow
class Fearow(Pokemon2):
    "Fearow"
    def __init__(self,name="Fearow",type1="Normal",type2="Flying",nature=None,level=100,happiness=255,hp=65,atk=100,defense=65,spatk=61,spdef=61,speed=115,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Technician","Sniper"]),item="Sharp Beak"):
        if move is None:
            avmoves=["U-Turn","Drill Peck","Drill Run","Dual Wingbeat","Brave Bird","Roost","Steel Wing"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Pikachu
class Pikachu(Pokemon2):
    "Pikachu"
    def __init__(self,name="Pikachu",type1="Electric",type2=None,nature=None,level=100,happiness=255,hp=45,atk=80,defense=50,spatk=75,spdef=60,speed=120,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Static",item="Light Ball"):
        if move is None:
            avmoves=["Extreme Speed","Volt Tackle","Iron Tail","Thunderbolt","Electroweb","Electro Ball","Thunder"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Raichu
class Raichu(Pokemon2):
    "Raichu"
    def __init__(self,name="Raichu",type1="Electric",type2=None,nature=None,level=100,happiness=255,hp=70,atk=100,defense=55,spatk=100,spdef=80,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Static",item="Leftovers"):
        if move is None:
            avmoves=["Extreme Speed","Volt Tackle","Iron Tail","Thunderbolt","Electroweb","Electro Ball","Thunder","Fake Out","Nasty Plot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #ARaichu
class ARaichu(Pokemon2):
    "Raichu"
    def __init__(self,name="Alolan Raichu",type1="Electric",type2="Psychic",nature=None,level=100,happiness=255,hp=60,atk=85,defense=50,spatk=95,spdef=85,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Surge Surfer",item="Leftovers"):
        if move is None:
            avmoves=["Extreme Speed","Volt Tackle","Grass Knot","Thunderbolt","Psychic","Electro Ball","Thunder","Fake Out","Nasty Plot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Sandslash
class Sandslash(Pokemon2):
    "Sandslash"
    def __init__(self,name="Sandslash",type1="Ground",type2=None,nature=None,level=100,happiness=255,hp=75,atk=110,defense=120,spatk=25,spdef=65,speed=65,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Sand Rush",item="Leftovers"):
        if move is None:
            avmoves=["Swords Dance","Crush Claw","Earthquake","Gyro Ball","Bulldoze","Rock Slide"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Sandslash
class ASandslash(Pokemon2):
    "Sandslash"
    def __init__(self,name="Alolan Sandslash",type1="Ice",type2="Steel",nature=None,level=100,happiness=255,hp=75,atk=110,defense=120,spatk=25,spdef=65,speed=65,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Slush Rush",item="Leftovers"):
        if move is None:
            avmoves=["Swords Dance","Spiky Shield","Icicle Crash","Gyro Ball","Ice Shard","Icicle Spear"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Clefable
class Clefable(Pokemon2):
    "Clefable"
    def __init__(self,name="Clefable",type1="Fairy",type2=None,nature=None,level=100,happiness=255,hp=95,atk=76,defense=73,spatk=95,spdef=90,speed=60,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Magic Guard",item="Leftovers"):
        if move is None:
            avmoves=["Cosmic Power","Moonblast","Meteor Mash","Stored Power","Moonlight"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Wigglytuff
class Wigglytuff(Pokemon2):
    def __init__(self,name="Wigglytuff",type1="Normal",type2="Fairy",nature=None,level=100,happiness=255,hp=140,atk=70,defense=45,spatk=85,spdef=50,speed=45,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Competitive",item="Leftovers"):
        if move is None:
            avmoves=["Body Slam","Moonblast","Rest","Play Rough","Gyro Ball"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Vileplume
class Vileplume(Pokemon2):
    def __init__(self,name="Vileplume",type1="Grass",type2="Poison",nature=None,level=100,happiness=255,hp=85,atk=80,defense=85,spatk=110,spdef=90,speed=50,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Chlorophyll",item="Black Sludge"):
        if move is None:
            avmoves=["Grassy Terrain","Moonblast","Giga Drain","Sleep Powder","Moonlight","Sludge Bomb","Toxic"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Parasect
class Parasect(Pokemon2):
    def __init__(self,name="Parasect",type1="Bug",type2="Grass",nature=None,level=100,happiness=255,hp=80,atk=110,defense=100,spatk=60,spdef=80,speed=30,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Dry Skin",item="Leftovers"):
        if move is None:
            avmoves=["Spore","X-Scissor","Giga Drain","Cross Poison","Synthesis"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                                                                                                                 #Venomoth
class Venomoth(Pokemon2):
    def __init__(self,name="Venomoth",type1="Bug",type2="Poison",nature=None,level=100,happiness=255,hp=70,atk=65,defense=65,spatk=95,spdef=75,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Tinted Lens",item="Black Sludge"):
        if move is None:
            avmoves=["Quiver Dance","Bug Buzz","Giga Drain","Psychic","Sleep Powder"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Dugtrio
class Dugtrio(Pokemon2):
    def __init__(self,name="Dugtrio",type1="Ground",type2=None,nature=None,level=100,happiness=255,hp=45,atk=100,defense=60,spatk=50,spdef=70,speed=120,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Sand Force",item="Leftovers"):
        if move is None:
            avmoves=["Sucker Punch","Earthquake","Night Slash","Bulldoze","Rock Slide"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Dugtrio
class ADugtrio(Pokemon2):
    def __init__(self,name="Dugtrio",type1="Ground",type2="Steel",nature=None,level=100,happiness=255,hp=45,atk=100,defense=60,spatk=50,spdef=70,speed=120,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Tangling Hair",item="Leftovers"):
        if move is None:
            avmoves=["Sucker Punch","Earthquake","Night Slash","Bulldoze","Iron Head"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Persian
class Persian(Pokemon2):
    def __init__(self,name="Persian",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=65,atk=80,defense=60,spatk=60,spdef=65,speed=115,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Technician",item="Leftovers"):
        if move is None:
            avmoves=["Play Rough","Sucker Punch","Slash","Night Slash","Fake Out","U-Turn","Shadow Claw"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Persian
class APersian(Pokemon2):
    def __init__(self,name="Alolan Persian",type1="Dark",type2=None,nature=None,level=100,happiness=255,hp=65,atk=60,defense=60,spatk=55,spdef=65,speed=115,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Feline Prowess",item="Leftovers"):
        if move is None:
            avmoves=["Nasty Plot","Sucker Punch","Power Gem","Dark Pulse","Fake Out","U-Turn","Shadow Ball"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Kingler
class Kingler(Pokemon2):
    def __init__(self,name="Kingler",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=65,atk=130,defense=115,spatk=50,spdef=50,speed=75,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Sheer Force",item="Leftovers"):
        if move is None:
            avmoves=["Swords Dance","Crabhammer","Razor Shell","Hammer Arm","X-Scissor","Rock Slide","Waterfall","Liquidation"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Hypno
class Hypno(Pokemon2):
    def __init__(self,name="Hypno",type1="Psychic",type2="Dark",nature=None,level=100,happiness=255,hp=85,atk=73,defense=70,spatk=73,spdef=115,speed=67,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Psychic Surge",item="Leftovers"):
        if move is None:
            avmoves=["Nasty Plot","Psyshock","Psychic","Dark Pulse","Hypnosis","Thunder Wave","Shadow Ball"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Electrode
class Electrode(Pokemon2):
    "Electrode"
    def __init__(self,name="Electrode",type1="Electric",type2=None,nature=None,level=100,happiness=255,hp=60,atk=50,defense=70,spatk=80,spdef=80,speed=140,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Static",item="Leftovers"):
        if move is None:
            avmoves=["Thunder","Thunderbolt","Thunder Wave","Hyper Beam","Rest","Explosion","Reflect","Light Screen"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Marowak
class Marowak(Pokemon2):
    def __init__(self,name="Marowak",type1="Ground",type2=None,nature=None,level=100,happiness=255,hp=80,atk=80,defense=110,spatk=30,spdef=80,speed=45,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Rock Head",item="Leftovers"):
        if move is None:
            avmoves=["Bone Rush","Bonemerang","Earthquake","Stomping Tantrum","Bulldoze","Rock Slide","Swords Dance","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Marowak
class AMarowak(Pokemon2):
    def __init__(self,name="Alolan Marowak",type1="Fire",type2="Ghost",nature=None,level=100,happiness=255,hp=80,atk=80,defense=110,spatk=30,spdef=80,speed=45,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Rock Head",item="Leftovers"):
        if move is None:
            avmoves=["Bone Rush","Bonemerang","Earthquake","Will-O-Wisp","Bulldoze","Rock Slide","Swords Dance","Stealth Rock","Shadow Bone"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Rhydon
class Rhydon(Pokemon2):
    def __init__(self,name="Rhydon",type1="Ground",type2="Rock",nature=None,level=100,happiness=255,hp=105,atk=130,defense=120,spatk=45,spdef=45,speed=40,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=4,speedev=0,maxiv="No",move=None, ability="Rock Head",item=random.choice(["Eviolite"])):
        if move is None:
            avmoves=["Protect","Stone Edge","Hammer Arm","High Horsepower","Thunder Punch","Giga Impact","Stealth Rock","Horn Drill","Double-Edge"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Chansey
class Chansey(Pokemon2):
    def __init__(self,name="Chansey",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=250,atk=5,defense=5,spatk=35,spdef=105,speed=50,hpev=252,atkev=0,defev=252,spatkev=0,spdefev=4,speedev=0,maxiv="No",move=None, ability="Natural Cure",item="Eviolite"):
        if move is None:
            avmoves=["Protect","Soft Boiled","Toxic","Seismic Toss","Light Screen","Reflect","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Seaking
class Seaking(Pokemon2):
    def __init__(self,name="Seaking",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=80,atk=92,defense=65,spatk=65,spdef=80,speed=68,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Lightning Rod","Swift Swim"]),item="Leftovers"):
        if move is None:
            avmoves=["Fishious Rend","Megahorn","Horn Drill","Poison Jab","Swords Dance","Rain Dance","Waterfall","Liquidation"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Mr.Mime
class MrMime(Pokemon2):
    def __init__(self,name="Mr.Mime",type1="Psychic",type2="Fairy",nature=None,level=100,happiness=255,hp=50,atk=45,defense=65,spatk=100,spdef=120,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Sheer Force",item="Leftovers"):
        if move is None:
            avmoves=["Psychic","Dazzling Gleam","Sucker Punch","Encore","Light Screen","Reflect"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Scyther
class Scyther(Pokemon2):
    def __init__(self,name="Scyther",type1="Bug",type2="Flying",nature=None,level=100,happiness=255,hp=70,atk=110,defense=80,spatk=55,spdef=80,speed=105,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Technician",item="Eviolite"):
        if move is None:
            avmoves=["Swords Dance","Slash","X-Scissor","U-Turn","Roost","Dual Wingbeat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Ditto
class Ditto(Pokemon2):
    "Ditto"
    def __init__(self,name="Ditto",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=40,atk=40,defense=40,spatk=40,spdef=40,speed=40,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Imposter",item="Choice Scarf"):
        if move is None:
            moves=["Transform","Protect","Recover","Light Screen"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   