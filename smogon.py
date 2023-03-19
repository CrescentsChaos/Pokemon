import sys
from pokemonbase2 import *
z="""Glalie @ Lum Berry  
Ability: Intimidate  
Tera Type: Ice  
EVs: 4 Atk / 252 SpA / 252 Spe  
Hasty Nature  
- Weather Ball  
- Ice Beam  
- Spikes  
- Explosion  

Wailord @ Lum Berry  
Ability: Pressure  
Tera Type: Water  
EVs: 248 HP / 8 Atk / 252 SpA  
Lax Nature  
- Hyper Voice  
- Water Spout  
- Explosion  
- Amnesia  

Regice @ Lum Berry  
Ability: Clear Body  
Tera Type: Ice  
EVs: 248 HP / 8 Atk / 252 SpA  
Quiet Nature  
- Counter  
- Ice Beam  
- Thunder  
- Explosion  

Dewgong @ Lum Berry  
Ability: Swift Swim  
Tera Type: Water  
EVs: 4 Atk / 252 SpA / 252 Spe  
Mild Nature  
- Ice Beam  
- Drill Run  
- Hidden Power [Grass]  
- Surf  

Swampert @ Lum Berry  
Ability: Swift Swim  
Tera Type: Water  
EVs: 4 Atk / 252 SpA / 252 Spe  
Mild Nature  
- Earthquake  
- Yawn  
- Muddy Water  
- Ancient Power  

Lapras @ Lum Berry  
Ability: Shell Armor  
Tera Type: Water  
EVs: 248 HP / 8 Atk / 252 SpA  
Mild Nature  
- Ice Shard  
- Thunder  
- Ice Beam  
- Hydro Pump  

"""


#def str_to_class(classname):
#    return getattr(sys.modules[__name__], classname)
#def con_mon(name):
#    
#    mon=None
#    if name=="Walking Wake":
#        mon=Walkingwake
#    else:
#        mon=str_to_class(name)
#    return mon
def rename(n):
    if "Black" in n:
        n="B"+n.split("-")[0]
    if "White" in n:
        n="W"+n.split("-")[0]
    if n=="Eternamax":
        n="E"+n.split("-")[0]
    if "-Mega" in n:
        n=n.split("-")[0]
    if n=="Gastrodon":
        n="W"+n
    if "East" in n:
        n="E"+n.split("-")[0]
    if "Therian" in n:
        n="T"+n.split("-")[0]
    if "Sky" in n:
        n="S"+n.split("-")[0]
    if n=="Sandy Shocks":
        n="Sandyshocks"
    if "Hisui" in n:
        n="H"+n.split("-")[0]
    if "Alola" in n:
        n="A"+n.split("-")[0]
    if "Galar" in n:
        n="G"+n.split("-")[0]
    if "Paldea" in n:
        n="P"+n.split("-")[0]
    if n=="Midnight":
        n="MNLycanroc"
    if n=="Midday":
        n="MDLycanroc"
    if n=="c-Dusk":
        n="DLycanroc"
    if n=="Slither Wing":
        n="Slitherwing"
    if n=="Flutter Mane":
        n="Fluttermane"
    if n=="Scream Tail":
        n="Screamtail"
    if "Iron" in n:
        n=n.split(" ")[0]+(n.split(" ")[-1]).lower()
    if "Origin" in n:
        n="O"+n.split("-")[0]
    if n=="Chi-Yu":
        n="Chiyu"
    if n=="Ting-Lu":
        n="Tinglu"
    if n=="Wo-Chien":
        n="Wo-Chien"
    if n=="Chien-Pao":
        n="Chienpao"
    if n=="Roaring Moon":
        n="Roaringmoon"
    if "Dusk-Mane" in n:
        n="DMNecrozma"
    if "Dawn-Wing" in n:
        n="DWNecrozma"
    if "Toxtricity" in n:
        n="Toxtricity"
    if "Keldeo" in n:
        n="Keldeo"
    if n=="Rotom-Frost":
        n="FrRotom"
    if n=="Rotom-Fan":
        n="FRotom"
    if n=="Rotom-Heat":
        n="HRotom"
    if n=="Rotom-Mow":
        n="MRotom"
    if n=="Rotom-Wash":
        n="WRotom"
    if n=="Great Tusk":
        n="Greattusk"
    if n=="Walking Wake":
        n="Walkingwake"
    else:
        pass
    return n
def pastemon(x,n=1):
    hpev=0
    atkev=0
    defev=0
    spatkev=0
    spdefev=0
    speedev=0
    if "EVs" in x:
        ev=x.split("""  
""")[2]
        ev=ev[4:]
        ev=ev.split("/")
        for i in ev:
            if "SpA" in i:
                spatkev=int(i.strip().split(" ")[0])
            if "SpD" in i:
                spdefev=int(i.strip().split(" ")[0])
            if "Spe" in i:
                speedev=int(i.strip().split(" ")[0])
            if "Def" in i:
                defev=int(i.strip().split(" ")[0])
            if "HP" in i:
                hpev=int(i.strip().split(" ")[0])
    if "(" in x:
        name=x.split("(")[1].split(")")[0]
    if "(" not in x:
        name=x.split(" @")[0]
    #mon=con_mon(name)
    if """  
Ability""" in x:
        item=x.split(" @ ")[1].split("""  
Ability""")[0]
    if """  
Ability""" not in x:
        item=x.split(" @ ")[1].split("""
Ability""")[0]
    if "Tera Type" not in x:
        if """  
""" in x:
            ability=x.split("Ability: ")[1].split("""  
""")[0]
        if """  
""" not in x:
            ability=x.split("Ability: ")[1].split("""
""")[0]
        tera="Yes"
    if "Tera Type" in x:
        ability=x.split("Ability: ")[1].split("""  
Tera Type: """)[0]
        tera=x.split("Tera Type: ")[1].split("""  
""")[0]
    
    if """  
- """ in x:
        nature=x.split(" Nature")[0].split(" ")[-1][1:]
        l,mv1,mv2,mv3,mv4=tuple(x.split("""  
- """))
    if """  
- """ not in x:
        nature=x.split(" Nature")[0].split(" ")[-1].split("\n")[-1]
        l,mv1,mv2,mv3,mv4=tuple(x.split("""
- """))
    newname=name
    if "m-Z" in item:
        newname=name+"(Z-Crystal)"
    name=rename(name)
    print(f'edit{n}={name}(name="{newname}",item="{item}",ability="{ability}",maxiv="{tera}",nature="{nature}",move=["{mv1}","{mv2}","{mv3}","{mv4}"],hpev={hpev},atkev={atkev},defev={defev},spatkev={spatkev},spdefev={spdefev},speedev={speedev})')

def smogonteam(z):
    z=str(z.strip())
    z=z.split("""  

""")
    n=0
    for i in z:
        n+=1
        pastemon(i,n)
    print(f'edit=Trainer("x",[edit1, edit2, edit3, edit4, edit5, edit6], "x")')  
smogonteam(z)
#x="""x"""
#x=x.strip()


#pastemon(x)    