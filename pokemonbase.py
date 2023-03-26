from pokemonbase2 import *
#Bombeedel
class Bombeedel(Pokemon2):
    def __init__(self,name="Bombeedel",type1="Bug",type2="None",nature="None",level=100,happiness=255,hp=70,atk=70,defense=30,spatk=130,spdef=70,speed=105,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Aftermath",item="Leftovers"):
        if move =="None":
            avmoves=["Protect","Toxic","Fire Blast","Final Gambit","U-turn","Recover","Explosion","X-Scissor","Sludge Bomb"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Final Gambit" in moves:
            hpev=252
            atkev=0
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Oricorio
class Plumageist(Pokemon2):
    def __init__(self,name="Plumageist",type1="Ghost",type2="Flying",nature="None",level=100,happiness=255,hp=75,atk=70,defense=75,spatk=110,spdef=85,speed=120,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Dance of the Specter"]),item=random.choice(["Focus Sash"])):
        if move =="None":
            avmoves=["Hurricane","Air Slash","Roost","Acrobatics","Calm Mind","Tailwind","U-turn","Hidden Power"]
            moves=moveset(type1,type2,avmoves,3)+["Revelation Dance"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
        #Dugtrio
class Terraterra(Pokemon2):
    def __init__(self,name="Terraterra",type1="Ground",type2="Steel",nature="None",level=100,happiness=255,hp=65,atk=130,defense=90,spatk=50,spdef=70,speed=130,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Arena Trap"]),item="Leftovers"):
        if move =="None":
            avmoves=["Sucker Punch","Earthquake","Night Slash","Bulldoze","Iron Head","Steel Beam","Tri Attack","Flash Cannon"]
            moves=moveset(type1,type2,avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)             
#ARaticate
class Verminlord(Pokemon2):
    "Raticate"
    def __init__(self,name="Verminlord",type1="Normal",type2="Dark",nature="None",level=100,happiness=255,hp=85,atk=135,defense=75,spatk=55,spdef=80,speed=120,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Swarm of Vermin"]),item="Sitrus Berry"):
        if move =="None":
            avmoves=["Swords Dance","Knock Off","Crunch","Sucker Punch","Double-Edge","Super Fang"]
            moves=moveset(type1,type2,avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)    
#Fearow
class Skyshrike(Pokemon2):
    "Fearow"
    def __init__(self,name="Skyshrike",type1="Flying",type2="Dragon",nature="None",level=100,happiness=255,hp=75,atk=130,defense=80,spatk=65,spdef=80,speed=125,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Winged Fury"]),item="Sharp Beak"):
        if move =="None":
            avmoves=["U-turn","Drill Peck","Drill Run","Dual Wingbeat","Brave Bird","Roost","Steel Wing","Dragon Claw","Draco Meteor","Dragon Rush"]
            moves=moveset(type1,type2,avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Arbok
class Venomspire(Pokemon2):
    "Arbok"
    def __init__(self,name="Venomspire",type1="Poison",type2="Dark",nature="None",level=100,happiness=255,hp=100,atk=120,defense=110,spatk=75,spdef=100,speed=85,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Toxic Fangs"]),item="Black Sludge"):
        if move =="None":
            avmoves=["Protect","Venoshock","Earth Power","Poison Fang","Crunch","Gunk Shot","Belch","Jaw Lock","Glare"]
            moves=moveset(type1,type2,avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)   
#Sandslash
class Quillshard(Pokemon2):
    "Sandslash"
    def __init__(self,name="Quillshard",type1="Ground",type2="Steel",nature="None",level=100,happiness=255,hp=80,atk=135,defense=140,spatk=50,spdef=70,speed=105,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Iron Spikes"]),item="Leftovers"):
        if move =="None":
            avmoves=["Swords Dance","Crush Claw","Earthquake","Gyro Ball","Bulldoze","Rock Slide","Rapid Spin","Spiky Shield","Iron Head"]
            moves=moveset(type1,type2,avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)               
#Tentacruel
class Cephalomight(Pokemon2):
    "Tentacruel"
    def __init__(self,name="Cephalomight",type1="Water",type2="Poison",nature="None",level=100,happiness=255,hp=80,atk=110,defense=110,spatk=120,spdef=100,speed=80,hpev=0,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=252,maxiv="No",move="None", ability=random.choice(["Venomous Aura"]),item="Black Sludge",weight=121.25):
        if move =="None":
            avmoves=["Hidden Power","Ice Beam","Hydro Pump","Thunderbolt","Sludge Bomb","Poison Jab","Rain Dance","Toxic Spikes"]
            moves=moveset(type1,type2,avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)     
    #Rapidash
class Ignisunico(Pokemon2):
    "Rapidash"
    def __init__(self,name="Ignisunico",type1="Fire",type2="Fairy",nature="None",level=100,happiness=255,hp=80,atk=120,defense=80,spatk=130,spdef=80,speed=120,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Radiant Blaze"]),item=random.choice(["Choice Band","Heavy-Duty Boots"])):
        if move =="None":
            avmoves=["Fire Blast","Flamethrower","Flare Blitz","Inferno","Morning Sun","Sunny Day","High Horsepower","Bounce"]
            moves=moveset(type1,type2,avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)     
#Dodrio
class Trioclaw(Pokemon2):
    "Dodrio"
    def __init__(self,name="Trioclaw",type1="Normal",type2="Flying",nature="None",level=100,happiness=255,hp=70,atk=130,defense=90,spatk=60,spdef=80,speed=120,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Talon Sweep"]),item=random.choice(["Choice Scarf","Heavy-Duty Boots"])):
        if move =="None":
            avmoves=["Close Combat","Brave Bird","Roost","Sky Attack","High Jump Kick","U-turn","Double-Edge","Tri Attack"]
            moves=moveset(type1,type2,avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)  
#Dewgong
class Glaciapod(Pokemon2):
    "Dewgong"
    def __init__(self,name="Glaciapod",type1="Water",type2="Ice",nature="None",level=100,happiness=255,hp=90,atk=70,defense=100,spatk=120,spdef=120,speed=80,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Icy Aura"]),item="Leftovers"):
        if move =="None":
            avmoves=["Protect","Hidden Power","Ice Beam","Hydro Pump","Thunderbolt","Surf","Snowscape","Rain Dance","Frost Breath","Aurora Veil"]
            moves=moveset(type1,type2,avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)    
class Sludgeon(Pokemon2):
    "Alolan Muk"
    def __init__(self,name="Sludgeon",type1="Poison",type2="Dark",nature="None",level=100,happiness=255,hp=120,atk=130,defense=110,spatk=80,spdef=110,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Toxic Drain"]),item=random.choice(["Black Sludge","Assault Vest"])):
        if move =="None":
            avmoves=["Sludge Bomb","Toxic","Poison Jab","Venoshock","Toxic Spikes","Drain Punch","Fire Punch","Poison Fang","Knock Off","Ice Punch","Parting Shot","Sucker Punch"]
            moves=moveset(type1,type2,avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item) 
#Cloyster
class Gemshell(Pokemon2):
    "Cloyster"
    def __init__(self,name="Gemshell",type1="Water",type2="Rock",nature="None",level=100,happiness=255,hp=75,atk=110,defense=130,spatk=75,spdef=115,speed=70,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Gemstone"]),item=random.choice(["Focus Sash","King's Rock"])):
        if move =="None":
            avmoves=["Ice Beam","Rock Blast","Icicle Spear","Shell Smash","Hydro Pump","Pin Missile","Snowscape","Liquidation"]
            moves=moveset(type1,type2,avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                                