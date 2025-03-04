import random
import discord
import sqlite3
from movelist import *
from field import *
async def weathereff(field,x,y,em):
    if field.weather=="Extreme Sunlight" and x.atktype=="Water" and "Cloud Nine" not in (x.ability,y.ability):
        em.add_field(name="Extreme Sunlight:",value="The Water-type attack evaporated in the harsh sunlight!")
        return 0
    if field.weather=="Heavy Rain" and x.atktype=="Fire" and "Cloud Nine" not in (x.ability,y.ability):
        em.add_field(name="Heavy Rain:",value="The Fire-type attack fizzled out in the heavy rain!")
        return 0                                 
    if field.weather in ["Rainy","Heavy Rain"] and x.atktype=="Water" and "Cloud Nine" not in (x.ability,y.ability):
        return 1.5
    if (field.weather=="Sunny") and x.atktype=="Water" and "Cloud Nine" not in (x.ability,y.ability):
        return 0.5    
    if (field.weather=="Rainy") and x.atktype=="Fire" and "Cloud Nine" not in (x.ability,y.ability):
        return 0.5      
    if field.weather in ["Sunny" ,"Extreme Sunlight"] and x.atktype=="Fire" and "Cloud Nine" not in (x.ability,y.ability):
        if "Koraidon" in x.name:
            return 2
        else:
            return 1.5        
    else:
        return 1     
async def hailend(tr1,mon,mon2):
       if mon.item!="Icy Rock":
           tr1.hailendturn=tr1.hailturn+5
       elif mon.item=="Icy Rock":
	       tr1.hailendturn=tr1.hailturn+8  
async def snowend(tr1,mon,mon2):
       if mon.item!="Icy Rock":
           tr1.snowendturn=tr1.snowturn+5
       if mon.item=="Icy Rock":
	       tr1.snowendturn=tr1.snowturn+8 
async def sandend(tr1,mon,mon2):
       if mon.item!="Smooth Rock":
           tr1.sandendturn=tr1.sandturn+5
       elif mon.item=="Smooth Rock":
           tr1.sandendturn=tr1.sandturn+8  
async def rainend(tr1,mon,mon2):
       if mon.item!="Damp Rock":
           tr1.rainendturn=tr1.rainturn+5
       elif mon.item=="Damp Rock":
           tr1.rainendturn=tr1.rainturn+8 
async def sunend(tr1,mon,mon2):
       if mon.item!="Heat Rock":
           tr1.sunendturn=tr1.sunturn+5
       elif mon.item=="Heat Rock":
           tr1.sunendturn=tr1.sunturn+8  
async def itemicon(itm):
    if itm=="None":
        return "<:000:1127112083792728074>"
    elif "Used" in itm:
        return "<:000:1127112083792728074>"
    else:
        try:
            db=sqlite3.connect("pokemondata.db")
            c=db.cursor()
            c.execute(f"select * from itemshop where item=='{itm}'")
            l=c.fetchone()
            return l[4]
        except:
            return "<:000:1127112083792728074>"
async def physical(x,level,atk,defense,base,a=1,b=1,c=1,r=1,al=1,w=1):
    if x.ability=="Power Core":
        if x.defense>=x.spdef:
            atk+=(x.defense*0.25)
        elif x.defense<x.spdef:
            atk+=(x.spdef*0.25)
    elif x.ability=="Juggernaut" and x.use in typemoves.contactmoves:
        atk+=(x.defense*0.2)
    x.atkcat="Physical"
    dmg=round((((2*level + 10)/250)*(atk/ defense)*base+2)*a*b*c*r*al*w)
    return dmg
async def special(x,level,spatk,spdef,base,a=1,b=1,c=1,r=1,al=1,w=1):
    if x.ability=="Power Core":
        if x.defense>=x.spdef:
            spatk+=(x.defense*0.25)
        elif x.defense<x.spdef:
            spatk+=(x.spdef*0.25)
    x.atkcat="Special"
    dmg=round((((2*level + 10)/250)*(spatk/spdef)*base+2)*a*b*c*r*al*w)
    return dmg
async def weakness(ctx,x,y,field,em):
    eff=1
    ty=1
    stab=1
    if x.use in typemoves.contactmoves:
        if x.ability in ["Tough Claws","Big Pecks"] and "Neutralizing Gas" not in y.ability:
            eff*=1.33
        elif x.ability=="Speed Force" and "Neutralizing Gas" not in y.ability:
            if (x.speed/x.atk)>1.5:
                eff*=1.5
            else:
                eff*=(x.speed/x.atk) 
    if x.use in typemoves.soundmoves and x.ability=="Punk Rock" and "Neutralizing Gas" not in y.ability:
        eff*=1.3
    if x.use in typemoves.soundmoves and y.ability=="Punk Rock" and "Neutralizing Gas" not in x.ability:
        eff*=0.5
    if x.charged==True:
        if x.use in typemoves.electricmoves:
            eff*=2
        x.charged=False
    if y.use=="Glaive Rush":
        eff*=2
    if x.use in typemoves.windmoves and y.ability=="Wind Rider" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart","Neutralizing Gas"]:
        eff*=0
        y.showability=True
        em.add_field(name=f"{y.icon} {y.name}'s {y.ability}!",value="Wind move boosted its Attack!")
        await atkchange(em,y,x,1)
    if "Absolute Zero" in (x.ability,y.ability) and x.atktype=="Water" and "Neutralizing Gas" not in (y.ability,x.ability):
        if x.ability=="Absolute Zero":
            em.add_field(name=f"{x.icon} {x.name}'s {x.ability}!",value="Absolute Zero turned the Water-type move into Ice-type move!")
            x.showability=True
        if y.ability=="Absolute Zero":
            em.add_field(name=f"{y.icon} {y.name}'s {y.ability}!",value="Absolute Zero turned the Water-type move into Ice-type move!")
            y.showability=True
        x.atktype="Ice"
    #UNAWARE(y EFFECT)
    if x.ability=="Unaware" and "Neutralizing Gas" not in y.ability:
        muldict={1:1.5,2:2,3:2.5,4:3,5:3.5,6:4,0:1,-1:0.66,-2:0.5,-3:0.4,-4:0.33,-5:0.29,-6:0.25}
        y.defense=round(y.defense/muldict[y.defb])
        y.spdef=round(y.spdef/muldict[y.spdefb])
    #UNAWARE(x EFFECT)
    if y.ability=="Unaware" and "Neutralizing Gas" not in x.ability:
        muldict={1:1.5,2:2,3:2.5,4:3,5:3.5,6:4,0:1,-1:0.66,-2:0.5,-3:0.4,-4:0.33,-5:0.29,-6:0.25}
        x.atk=round(x.atk/muldict[x.atkb])
        x.spatk=round(x.spatk/muldict[x.spatkb])
    #PROTEAN/LIBERO
    if x.ability in ["Protean","Libero"] and x.primaryType!=x.atktype and "Neutralizing Gas" not in y.ability:
        x.secondaryType="???"
        x.primaryType=x.atktype
        em.add_field(name=f"{x.icon} {x.name}'s {x.ability}!",value=f"{x.name} changed it's type to {x.primaryType}!")
        y.showability=True
    #Color Change
    if y.ability in ["Color Change"] and y.primaryType!=x.atktype and "Neutralizing Gas" not in x.ability:
        y.secondaryType="???"
        y.primaryType=y.atktype
        em.add_field(name=f"{y.icon} {y.name}'s {y.ability}!",value=f"{y.name} changed it's type to {y.primaryType}!")
        y.showability=True
    elif y.ability=="Battle Armor":
        eff*=0.9
    #SHADOW SHIELD/MULTISCALE/BLUBBER DEFENSE       
    if (y.hp == y.maxhp and y.ability in ["Multiscale", "Blubber Defense", "Shadow Shield"] and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart","Neutralizing Gas"] and x.use not in typemoves.abilityigmoves):
        em.add_field(name=f"{y.icon} {y.name}'s {y.ability}!",value=f"Damage was reduced in full HP!")
        y.showability=True
        eff *= 0.5
    #SOLAR POWER
    elif x.ability in ["Solar Power","Big Leaves"] and field.weather in ["Sunny","Desolate Land"] and "Cloud Nine" not in (x.ability,y.ability) and "Neutralizing Gas" not in y.ability:
        eff*=1.5
    #ANALYTIC
    elif x.ability=="Analytic" and "Neutralizing Gas" not in y.ability:
        if x.speed<y.speed:
            eff*=1.3
    #NORMALIZE 
    elif x.ability=="Normalize" and "Neutralizing Gas" not in y.ability:
        x.atktype="Normal"
    #CHANGING NORMAL TYPE MOVES
    if x.atktype=="Normal":
        if x.ability in ["Pixilate","Aerilate","Galvanize","Refrigerate","Liquid Voice","Burnate","Poisonate","Buginize"] and "Neutralizing Gas" not in y.ability:
            ability_dict = {"Pixilate": "Fairy", "Aerilate": "Flying", "Galvanize": "Electric", "Refrigerate": "Ice", "Liquid Voice": "Water","Burnate":"Fire","Poisonate":"Poison","Buginize":"Bug"}
            x.atktype = ability_dict[x.ability]
            eff *= 1.2
    type_chart = {
    'Bug': {'effective': ['Grass', 'Psychic', 'Dark'], 'weak': ['Fighting', 'Flying', 'Poison', 'Ghost', 'Steel', 'Fire', 'Fairy']},
    'Water': {'effective': ['Ground', 'Rock', 'Fire'], 'weak': ['Water', 'Grass', 'Dragon']},
    'Ghost': {'effective': ['Ghost', 'Psychic'], 'weak': ['Dark'], 'immune': ['Normal']},
    'Electric': {'effective': ['Flying', 'Water'], 'immune': ['Ground'], 'weak': ['Grass', 'Electric', 'Dragon']},
    'Psychic': {'effective': ['Fighting', 'Poison'], 'immune': ['Dark'], 'weak': ['Steel', 'Psychic']},
    'Ice': {'effective': ['Flying', 'Ground', 'Grass', 'Dragon'], 'weak': ['Steel', 'Fire', 'Ice', 'Water']},
    'Dragon': {'immune': ['Fairy'], 'effective': ['Dragon'], 'weak': ['Steel']},
    'Fairy': {'effective': ['Fighting', 'Dragon', 'Dark'], 'weak': ['Poison', 'Steel', 'Fire']},
    'Dark': {'effective': ['Ghost', 'Psychic'], 'weak': ['Fighting', 'Dark', 'Fairy']},
    'Steel': {'effective': ['Rock', 'Ice', 'Fairy'], 'weak': ['Steel', 'Fire', 'Water', 'Electric']},
    'Grass': {'effective': ['Ground', 'Rock', 'Water'], 'weak': ['Flying', 'Poison', 'Bug', 'Steel', 'Fire', 'Grass', 'Dragon']},
    'Fire': {'effective': ['Bug', 'Steel', 'Grass', 'Ice'], 'weak': ['Rock', 'Fire', 'Water', 'Dragon']},
    'Poison': {'effective': ['Grass', 'Fairy'], 'weak': ['Poison', 'Ground', 'Rock', 'Ghost'], 'immune': ['Steel']},
    'Flying': {'effective': ['Fighting', 'Bug', 'Grass'], 'weak': ['Rock', 'Steel', 'Electric']},
    'Rock': {'effective': ['Flying', 'Bug', 'Fire', 'Ice'], 'weak': ['Fighting', 'Ground', 'Steel']},
    'Normal': {'weak': ['Rock', 'Steel'], 'immune': ['Ghost']},
    'Fighting': {'effective': ['Normal', 'Rock', 'Steel', 'Ice', 'Dark'], 'weak': ['Flying', 'Poison', 'Psychic', 'Bug', 'Fairy'], 'immune': ['Ghost']},
    'Ground': {'effective': ['Poison', 'Rock', 'Steel', 'Fire', 'Electric'], 'weak': ['Bug', 'Grass'], 'immune': ['Flying']}
}
    #BUG
    bugeff=type_chart["Bug"]["effective"]
    bugwk=type_chart["Bug"]["weak"]
    #water
    watereff=type_chart["Water"]["effective"]
    waterwk=type_chart["Water"]["weak"]
    #Ghost
    ghosteff=type_chart["Ghost"]["effective"]
    ghostwk=type_chart["Ghost"]["weak"]
    ghostimmune=type_chart["Ghost"]["immune"]
    #Electric
    electriceff=type_chart["Electric"]["effective"]
    electricimmune=type_chart["Electric"]["immune"]
    electricwk=type_chart["Electric"]["weak"]
    #Psychic
    psychiceff=type_chart["Psychic"]["effective"]
    psychicimmune=["Dark"]
    psychicwk=type_chart["Psychic"]["weak"]
    #Ice
    iceeff=type_chart["Ice"]["effective"]
    icewk=type_chart["Ice"]["weak"]
    #Dragon
    dragonimmune=["Fairy"]
    dragoneff=type_chart["Dragon"]["effective"]
    dragonwk=type_chart["Dragon"]["weak"]
    #Fairy
    fairyeff=type_chart["Fairy"]["effective"]
    fairywk=type_chart["Fairy"]["weak"]
    #Dark
    darkeff=type_chart["Dark"]["effective"]
    darkwk=type_chart["Dark"]["weak"]
    #Steel
    steeleff=type_chart["Steel"]["effective"]
    steelwk=type_chart["Steel"]["weak"]
    #GRASS      
    grasseff=type_chart["Grass"]["effective"]
    grasswk=type_chart["Grass"]["weak"]
    #FIRE
    fireeff=type_chart["Fire"]["effective"]
    firewk=type_chart["Fire"]["weak"]
    #POISON
    poisoneff=type_chart["Poison"]["effective"]
    poisonwk=type_chart["Poison"]["weak"]
    poisonimmune=["Steel"]
    #FLYING
    flyingeff=type_chart["Flying"]["effective"]
    flyingwk=type_chart["Flying"]["weak"] 
    #Rock
    rockeff=type_chart["Rock"]["effective"]
    rockwk=type_chart["Rock"]["weak"]
    #Normal
    normaleff=[]
    normalwk=type_chart["Normal"]["weak"]
    normalimmune=['Ghost']
    #fighting
    fightingeff=type_chart["Fighting"]["effective"]
    fightingwk=type_chart["Fighting"]["weak"]
    fightingimmune=["Ghost"]
    #ground
    groundeff=type_chart["Ground"]["effective"]
    groundwk=type_chart["Ground"]["weak"]
    groundimmune=["Flying"]       
    if x.atktype=="Ghost":
        if x.ability=="Dance of the Specter" and "Neutralizing Gas" not in y.ability:
            eff*=1.2
        elif y.ability=="Rattled" and "Neutralizing Gas" not in x.ability:
            em.add_field(name=f"{y.icon} {y.name}'s {y.ability}!",value="Ghost move boosted its Speed!")
            y.showability=True
            await speedchange(em,y,x,1)
        #PURIFYING SALT
        elif y.ability=="Purifying Salt" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart","Neutralizing Gas"] and x.use not in typemoves.abilityigmoves:
            eff*=0.5
        #Kasib Berry
        if y.item=="Kasib Berry" and x.ability not in ["Unnerve","As One"]:
            em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.name}'s {y.item} weakened the damage of {x.atktype}-type move!")
            y.item+="[Used]"
        #Ghost Gem
        if x.item == "Ghost Gem":
            eff*=1.5
            em.add_field(name=f"Item:",value=f"{x.item} strengthened the damage of {x.name}'s {x.atktype}-type moves!")
            x.item+="[Used]"
        if x.item in ["Griseous Orb","Spooky Plate","Spell Tag","Griseous Core"]:
            eff*=1.2
        if y.primaryType in ghosteff and y.teraType in ["???","Stellar"]:
            ty*=2
        if y.secondaryType in ghosteff and y.teraType in ["???","Stellar"]:
            ty*=2
        if y.teraType in ghosteff:
            ty*=2
        if y.primaryType in ghostwk and y.teraType in ["???","Stellar"]:
            ty/=2
        if y.secondaryType in ghostwk and y.teraType in ["???","Stellar"]:
            ty/=2
        if y.teraType in ghostwk:
            ty/=2
        if ((y.primaryType in ghostimmune or y.secondaryType in ghostimmune) and y.teraType in ["???","Stellar"]) or (y.teraType in ghostimmune and y.item!="Ring Target"):
            ty*=0         
            if x.use in ["High Jump Kick","Axe Kick","Supercell Slam"]:
                a=b=c=r=al=1
                dmg=await physical(x,x.level,x.atk,y.defense,130,a,b,c,r,al)
                x.hp-=dmg/2
                em.add_field(name=f"Recoil:",value=f"{x.name} was hurt by recoil!")
    if x.atktype=="Electric":
        #Electromorphosis
        if x.atktime>0 and x.ability=="Electromorphosis" and x.speed<y.speed and "Neutralizing Gas" not in y.ability:
            em.add_field(name=f"{x.icon} {x.name}'s {x.ability}!",value="Electric move was boosted!")
            x.showability=True
            eff*=1.34
        #Motor Drive
        if y.ability=="Motor Drive" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart","Neutralizing Gas"] and x.use not in typemoves.abilityigmoves:
            y.showability=True
            em.add_field(name=f"{y.icon} {y.name}'s {y.ability}!",value="Electric move boosted its speed!")
            await speedchange(em,y,x,1)
            eff*=0
        #Transistor
        if x.ability=="Transistor" and "Neutralizing Gas" not in y.ability:
            eff*=1.5
        if x.ability=="Short Circuit" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart","Neutralizing Gas"] and x.use not in typemoves.abilityigmoves:
            if x.hp<=(x.maxhp/3):
                eff*=1.5
            else:
                eff*=1.2            
        if x.item == "Magnet":
            eff*=1.2
        if y.item=="Wacan Berry" and x.ability not in ["Unnerve","As One"]:
            eff*=0.5
            em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.name}'s {y.item} weakened the damage of {x.atktype}-type move!")
            y.item+="[Used]"
        if field.terrain=="Electric" and ((x.ability not in ["Levitate"] and x.ability!="Mold Breaker") and "Flying" not in (x.primaryType,x.secondaryType,x.teraType) or x.grav is True):
            eff*=1.3
        if y.ability=="Delta Stream" and "Flying" in (y.primaryType,y.secondaryType,y.teraType) and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart","Neutralizing Gas"] and x.use not in typemoves.abilityigmoves:
            eff*=0.5
        if x.item in ["Zap Plate","Battery","Magnet"]:
            eff*=1.2
        if x.item == "Electric Gem":
            eff*=1.5
            em.add_field(name=f"{x.icon} {x.name}'s {await itemicon(x.item)} {x.item}!",value=f"{x.item} strengthened the damage of {x.icon} {x.name}'s {x.atktype}-type moves!")
            x.item+="[Used]"
        if y.ability=="Lightning Rod" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart","Neutralizing Gas"] and x.use not in typemoves.abilityigmoves:
            em.add_field(name=f"{y.icon} {y.name}'s {y.ability}!",value="Electric move boosted its special attack!")
            await spatkchange(em,y,x,1)
            eff*=0
        if y.ability=="Volt Absorb" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart","Neutralizing Gas"] and x.use not in typemoves.abilityigmoves:
            em.add_field(name=f"{y.icon} {y.name}'s {y.ability}!",value="Electric move was absorbed!")
            y.showability=True
            if y.hp<=y.maxhp-(y.maxhp/4):
                y.hp+=y.maxhp/4
            if y.hp>y.maxhp-(y.maxhp/4):
                y.hp=y.maxhp
            eff*=0
        if y.primaryType in electriceff and y.teraType in ["???","Stellar"]:
            ty*=2
        if y.teraType in electriceff:
            ty*=2
        if y.secondaryType in electriceff and y.teraType in ["???","Stellar"]:
            ty*=2
        if y.primaryType in electricwk and y.teraType in ["???","Stellar"]:
            ty/=2
        if y.secondaryType in electricwk and y.teraType in ["???","Stellar"]:
            ty/=2
        if y.teraType in electricwk:
            ty/=2
        if (y.primaryType in electricimmune or y.secondaryType in electricimmune and y.teraType in ["???","Stellar"]) or y.teraType in electricimmune and y.item!="Ring Target":
            ty*=0
    
    #psychic
    if x.atktype=="Psychic":
        if x.ability=="Psychic Mind":
            eff*=1.25
        if y.ability=="Dark Mind" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart","Neutralizing Gas"] and x.use not in typemoves.abilityigmoves:
            em.add_field(name=f"{y.icon} {y.name}'s {y.ability}!",value="Psychic move perished away!")
            y.showability=True
            eff*=0
        if y.item=="Payapa Berry" and x.ability not in ["Unnerve","As One"]:
            eff*=0.5
            em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.name}'s {y.item} weakened the damage of {x.atktype}-type move!")
            y.item+="[Used]"
        if field.terrain=="Psychic" and (x.ability not in ["Levitate"] and "Flying" not in (x.primaryType,x.secondaryType,x.teraType) or x.grav is True):
            eff*=1.3
        if x.item in ["Mind Plate","Twisted Spoon","Soul Dew","Odd Incense"]:
            eff*=1.2
        if x.item == "Psychic Gem":
            eff*=1.5
            em.add_field(name=f"{x.icon} {x.name}'s {await itemicon(x.item)} {x.item}!",value=f"{x.item} strengthened the damage of {x.icon} {x.name}'s {x.atktype}-type moves!")
            x.item+="[Used]"
        if y.primaryType in psychiceff and y.teraType in ["???","Stellar"]:
            ty*=2
        if y.secondaryType in psychiceff and y.teraType in ["???","Stellar"]:
            ty*=2
        if y.primaryType in psychicwk and y.teraType in ["???","Stellar"]:
            ty/=2
        if y.secondaryType in psychicwk and y.teraType in ["???","Stellar"]:
            ty/=2
        if y.teraType in psychiceff:
            ty*=2
        if y.teraType in psychicwk:
            ty/=2
        if (y.primaryType in psychicimmune or y.secondaryType in psychicimmune and y.teraType in ["???","Stellar"]) or y.teraType in psychicimmune and y.item!="Ring Target":
            ty*=0
    #ice
    if x.atktype=="Ice":
        if x.ability=="Icy Aura" and "Neutralizing Gas" not in y.ability:
            eff*=1.5
        if x.use=="Freeze-Dry" and "Water" in (y.primaryType,y.secondaryType,y.teraType):
            ty*=4
        if x.item in ["Never Melt Ice","Icicle Plate"]:
            eff*=1.2
        if y.item=="Yache Berry" and x.ability not in ["Unnerve","As One"]:
            eff*=0.5
            em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.name}'s {y.item} weakened the damage of {x.atktype}-type move!")
            y.item+="[Used]"
        if y.ability=="Thick Fat" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart","Neutralizing Gas"] and x.use not in typemoves.abilityigmoves:
            eff*=0.5
        if y.ability=="Delta Stream" and "Flying" in (y.primaryType,y.secondaryType) and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart","Neutralizing Gas"] and x.use not in typemoves.abilityigmoves:
            eff*=0.5
        if x.item == "Ice Gem":
            eff*=1.5
            em.add_field(name=f"{x.icon} {x.name}'s {await itemicon(x.item)} {x.item}!",value=f"{x.item} strengthened the damage of {x.icon} {x.name}'s {x.atktype}-type moves!")
            x.item+="[Used]"
        if y.primaryType in iceeff and y.teraType in ["???","Stellar"]:
            ty*=2
        if y.secondaryType in iceeff and y.teraType in ["???","Stellar"]:
            ty*=2
        if y.primaryType in icewk and y.teraType in ["???","Stellar"]:
            ty/=2
        if y.secondaryType in icewk and y.teraType in ["???","Stellar"]:
            ty/=2
        if y.teraType in iceeff:
            ty*=2
        if y.teraType in icewk:
            ty/=2
    #fairy
    if x.atktype=="Fairy":
        if x.item in ["Pixie Plate","Fairy Feather"]:
            eff*=1.2
        if y.item=="Roseli Berry" and x.ability not in ["Unnerve","As One"]:
            eff*=0.5
            em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.name}'s {y.item} weakened the damage of {x.atktype}-type move!")
            y.item+="[Used]"
        if "Fairy Aura" in (x.ability,y.ability):
            if y.ability!="Aura Break":
                eff*=1.33
            else:
                eff*=0.67
        if x.item == "Fairy Gem":
            eff*=1.5
            em.add_field(name=f"{x.icon} {x.name}'s {await itemicon(x.item)} {x.item}!",value=f"{x.item} strengthened the damage of {x.icon} {x.name}'s {x.atktype}-type moves!")
            x.item+="[Used]"
        if y.primaryType in fairyeff and y.teraType in ["???","Stellar"]:
            ty*=2
        if y.secondaryType in fairyeff and y.teraType in ["???","Stellar"]:
            ty*=2
        if y.primaryType in fairywk and y.teraType in ["???","Stellar"]:
            ty/=2
        if y.secondaryType in fairywk and y.teraType in ["???","Stellar"]:
            ty/=2
        if y.teraType in fairyeff:
            ty*=2
        if y.teraType in fairywk:
            ty/=2
    #dark
    if x.atktype=="Dark":
        if x.ability=="Toxic Drain":
            eff*=1.5
        if y.ability=="Rattled":
            em.add_field(name=f"{y.icon} {y.name}'s {y.ability}!",value="Dark move boosted its speed!")
            y.showability=True
            await speedchange(em,y,x,1)
        if x.item in ["Black Glasses","Dread Plate"]:
            eff*=1.2
        if y.item=="Colbur Berry" and x.ability not in ["Unnerve","As One"]:
            eff*=0.5
            em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.name}'s {y.item} weakened the damage of {x.atktype}-type move!")
            y.item+="[Used]"
        if "Dark Aura" in (x.ability,y.ability):
            if y.ability!="Aura Break":
                eff*=1.33
            else:
                eff*=0.67
        if x.item == "Dark Gem":
            eff*=1.5
            em.add_field(name=f"{x.icon} {x.name}'s {await itemicon(x.item)} {x.item}!",value=f"{x.item} strengthened the damage of {x.icon} {x.name}'s {x.atktype}-type moves!")
            x.item+="[Used]"
        if y.ability=="Justified" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart","Neutralizing Gas"] and x.use not in typemoves.abilityigmoves:
            y.showability=True
            em.add_field(name=f"{y.icon} {y.name}'s {y.ability}!",value="Dark move boosted its Attack!")
            await atkchange(em,y,x,1)            
        if y.primaryType in darkeff and y.teraType in ["???","Stellar"]:
            ty*=2
        if y.secondaryType in darkeff and y.teraType in ["???","Stellar"]:
            ty*=2
        if y.primaryType in darkwk and y.teraType in ["???","Stellar"]:
            ty/=2
        if y.secondaryType in darkwk and y.teraType in ["???","Stellar"]:
            ty/=2
        if y.teraType in darkeff:
            ty*=2
        if y.teraType in darkwk:
            ty/=2
    #steel
    if x.atktype=="Steel":
        if x.ability in ["Steely Spirit","Iron Spikes"]:
            eff*=1.5
        elif y.ability=="Magnetic Field" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart","Neutralizing Gas"] and x.use not in typemoves.abilityigmoves:
            y.showability=True
            em.add_field(name=f"{y.icon} {y.name}'s {y.ability}!",value="Steel move boosted its defense!")
            await defchange(em,y,x,1)
            eff*=0            
        if x.ability=="Sand Force" and field.weather=="Sandstorm":
            eff*=1.3
        if x.item in ["Metal Coat","Iron Plate"]:
            eff*=1.2
        if y.item=="Babiri Berry" and x.ability not in ["Unnerve","As One"]:
            eff*=0.5
            em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.name}'s {y.item} weakened the damage of {x.atktype}-type move!")
            y.item+="[Used]"
        if x.ability=="Steelworker":
            eff*=1.5
        if x.item == "Steel Gem":
            eff*=1.5
            em.add_field(name=f"{x.icon} {x.name}'s {await itemicon(x.item)} {x.item}!",value=f"{x.item} strengthened the damage of {x.icon} {x.name}'s {x.atktype}-type moves!")
            x.item+="[Used]"
        if x.item in ["Adamant Orb","Adamant Crystal"]:
            eff+=(eff*0.2)
        if y.primaryType in steeleff and y.teraType in ["???","Stellar"]:
            ty*=2
        if y.secondaryType in steeleff and y.teraType in ["???","Stellar"]:
            ty*=2
        if y.primaryType in steelwk and y.teraType in ["???","Stellar"]:
            ty/=2
        if y.secondaryType in steelwk and y.teraType in ["???","Stellar"]:
            ty/=2
        if y.teraType in steeleff:
            ty*=2
        if y.teraType in steelwk:
            ty/=2   
    #dragon
    if x.atktype=="Dragon":
        if x.ability=="Dragon's Maw":
            eff*=1.5
        if x.item in ["Dragon Fang","Draco Plate"]:
            eff*=1.2
        if y.item=="Haban Berry" and x.ability not in ["Unnerve","As One"]:
            eff*=0.5
            em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.name}'s {y.item} weakened the damage of {x.atktype}-type move!")
            y.item+="[Used]"
        if field.terrain=="Misty" and (x.ability not in ["Levitate"] and "Flying" not in (x.primaryType,x.secondaryType,x.teraType) or x.grav is True):
            eff*=0.5
        if x.item == "Dragon Gem":
            eff*=1.5
            em.add_field(name=f"{x.icon} {x.name}'s {await itemicon(x.item)} {x.item}!",value=f"{x.item} strengthened the damage of {x.icon} {x.name}'s {x.atktype}-type moves!")
            x.item+="[Used]"
        if x.item in ["Adamant Orb","Lustrous Orb","Griseous Orb","Soul Dew","Griseous Core","Adamant Crystal","Lustrous Globe"]:
            eff*=1.2
        if y.primaryType in dragoneff and y.teraType in ["???","Stellar"]:
            ty*=2
        if y.secondaryType in dragoneff and y.teraType in ["???","Stellar"]:
            ty*=2
        if y.primaryType in dragonwk and y.teraType in ["???","Stellar"]:
            ty/=2
        if y.secondaryType in dragonwk and y.teraType in ["???","Stellar"]:
            ty/=2
        if y.teraType in dragoneff:
            ty*=2
        if y.teraType in dragonwk:
            ty/=2
        if (y.primaryType in dragonimmune or y.secondaryType in dragonimmune and y.teraType in ["???","Stellar"]) or y.teraType in dragonimmune and y.item!="Ring Target":
            ty*=0
    #bug
    if x.atktype=="Bug":
        if y.ability=="Rattled":
            em.add_field(name=f"{y.icon} {y.name}'s {y.ability}!",value="Bug move boosted its Speed!")
            y.showability=True
            await speedchange(em,y,x,1)
        if x.item in ["Silver Powder","Insect Plate"]:
            eff*=1.2
        if y.item=="Tanga Berry" and x.ability not in ["Unnerve","As One"]:
            eff*=0.5
            em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.name}'s {y.item} weakened the damage of {x.atktype}-type move!")
            y.item+="[Used]"
        if x.item == "Bug Gem":
            eff*=1.5
            em.add_field(name=f"{x.icon} {x.name}'s {await itemicon(x.item)} {x.item}!",value=f"{x.item} strengthened the damage of {x.icon} {x.name}'s {x.atktype}-type moves!")
            x.item+="[Used]"
        if x.ability=="Swarm" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart","Neutralizing Gas"] and x.use not in typemoves.abilityigmoves:
            if x.hp<=(x.maxhp/3):
                eff*=1.5
            else:
                eff*=1.2
        if y.primaryType in bugeff and y.teraType in ["???","Stellar"]:
            ty*=2
        if y.secondaryType in bugeff and y.teraType in ["???","Stellar"]:
            ty*=2
        if y.primaryType in bugwk and y.teraType in ["???","Stellar"]:
            ty/=2
        if y.secondaryType in bugwk and y.teraType in ["???","Stellar"]:
            ty/=2
        if y.teraType in bugeff:
            ty*=2
        if y.teraType in bugwk:
            ty/=2
    #Water
    if x.atktype=="Water":
        if x.ability=="Water Bubble":
            eff*=2
        elif x.ability=="Amphibious":
            eff*=1.5
        if y.item=="Luminous Moss":
            em.add_field(name=f"{x.icon} {x.name}'s {await itemicon(x.item)} {x.item}!",value="Luminous Moss absorbed {x.name}'s Water-type moves energy and raised {y.name}'s Special Defense!")
            await spdefchange(em,y,x,1)
            y.item+="[Used]"
        if y.item=="Absorb Bulb":
            em.add_field(name=f"{x.icon} {x.name}'s {await itemicon(x.item)} {x.item}!",value="Absorb Bulb absorbed {x.name}'s Water-type moves energy and raised {y.name}'s Special Attack!")
            await spatkchange(em,y,x,1)
            y.item+="[Used]"
        if y.ability=="Steam Engine" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart","Neutralizing Gas"] and x.use not in typemoves.abilityigmoves:
            y.showability=True
            em.add_field(name=f"{y.icon} {y.name}'s {y.ability}!",value="Water move drastically boosted its speed!")
            await speedchange(em,y,x,3)
        if x.item in  ["Mystic Water","Splash Plate","Lustrous Orb","Wave Incense","Sea Incense","Lustrous Globe"]:
            eff*=1.2
        if y.item=="Passho Berry" and x.ability not in ["Unnerve","As One"]:
            eff*=0.5
            em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.name}'s {y.item} weakened the damage of {x.atktype}-type move!")
            y.item+="[Used]"
        if field.weather=="Desolate Land" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart","Neutralizing Gas"] and x.use not in typemoves.abilityigmoves  and "Cloud Nine" not in (x.ability,y.ability):
            eff*=0
        if x.item == "Water Gem":
            eff*=1.5
            em.add_field(name=f"{x.icon} {x.name}'s {await itemicon(x.item)} {x.item}!",value=f"{x.item} strengthened the damage of {x.icon} {x.name}'s {x.atktype}-type moves!")
            x.item+="[Used]"
        if y.ability in ["Storm Drain","Water Absorb","Dry Skin","Water Compaction","Evaporate"] and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart","Neutralizing Gas"] and x.use not in typemoves.abilityigmoves:
            if y.ability=="Water Compaction":
                em.add_field(name=f"{y.icon} {y.name}'s {y.ability}!",value="Water move sharply boosted it defense!")
                await defchange(em,y,x,2)
                eff*=0.5
            if y.ability=="Dry Skin" and "Cloud Nine" not in (x.ability,y.ability):
                eff*=0
                em.add_field(name=f"{y.icon} {y.name}'s {y.ability}!",value="Water move was absorbed!")
                y.showability=True
                if y.hp<=y.maxhp-(y.maxhp/4):
                    y.hp+=y.maxhp/4
            if y.ability in ["Storm Drain","Evaporate"]:
                em.add_field(name=f"{y.icon} {y.name}'s {y.ability}!",value="Water move was diminished!")
                y.showability=True
                eff*=0
                await spatkchange(em,y,x,1)
            if y.ability=="Water Absorb":
                y.showability=True
                eff*=0
                em.add_field(name=f"{y.icon} {y.name}'s {y.ability}!",value="Water move was absorbed!")
                if y.hp<=y.maxhp-(y.maxhp/4):
                    y.hp+=y.maxhp/4
                if y.hp>y.maxhp-(y.maxhp/4):
                    y.hp=y.maxhp            
        if x.ability=="Torrent" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart","Neutralizing Gas"] and x.use not in typemoves.abilityigmoves:
            if x.hp<=(x.maxhp/3):
                eff*=1.5
            else:
                eff*=1.2
        if y.primaryType in watereff and y.teraType in ["???","Stellar"]:
            ty*=2
        if y.secondaryType in watereff and y.teraType in ["???","Stellar"]:
            ty*=2
        if y.primaryType in waterwk and y.teraType in ["???","Stellar"]:
            ty/=2
        if y.secondaryType in waterwk and y.teraType in ["???","Stellar"]:
            ty/=2
        if y.teraType in watereff:
            ty*=2
        if y.teraType in waterwk:
            ty/=2
    #Ground
    if x.atktype=="Ground":
        if y.ability=="Earth Eater" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart","Neutralizing Gas"] and x.use not in typemoves.abilityigmoves:
            y.showability=True
            em.add_field(name=f"{y.icon} {y.name}'s {y.ability}!",value="Ground move was absorbed!")
            if y.hp<=y.maxhp-(y.maxhp/4):
                y.hp+=y.maxhp/4
            if y.hp>y.maxhp-(y.maxhp/4):
                y.hp=y.maxhp
            eff*=0
        if y.ability=="Terrain Rush" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart","Neutralizing Gas"] and x.use not in typemoves.abilityigmoves:
            em.add_field(name=f"{y.icon} {y.name}'s {y.ability}!",value="Ground move boosted its speed!")
            y.showability=True
            await speedchange(em,y,x,1)
            eff*=0            
        if y.item=="Air Balloon":
            eff*=0
        if x.ability=="Sand Force" and field.weather=="Sandstorm":
            eff*=1.3
        if x.item in ["Soft Sand","Earth Plate"]:
            eff*=1.2
        if y.item=="Shuca Berry" and x.ability not in ["Unnerve","As One"]:
            eff*=0.5
            em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.name}'s {y.item} weakened the damage of {x.atktype}-type move!")
            y.item+="[Used]"
        if x.item == "Ground Gem":
            eff*=1.5
            em.add_field(name=f"{x.icon} {x.name}'s {await itemicon(x.item)} {x.item}!",value=f"{x.item} strengthened the damage of {x.icon} {x.name}'s {x.atktype}-type moves!")
            x.item+="[Used]"
        if (y.ability in ["Levitate","Winged"] and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart","Neutralizing Gas"] and x.use not in typemoves.abilityigmoves and x.grav is not True):
            y.showability=True
            em.add_field(name=f"{y.icon} {y.name}'s {y.ability}!",value=f"{y.name} is levitating on the air and immune to Ground attacks!")
            eff*=0
        if y.primaryType in groundeff and y.teraType in ["???","Stellar"]:
            ty*=2
        if y.secondaryType in groundeff and y.teraType in ["???","Stellar"]:
            ty*=2
        if y.primaryType in groundwk and y.teraType in ["???","Stellar"]:
            ty/=2
        if y.secondaryType in groundwk and y.teraType in ["???","Stellar"]:
            ty/=2
        if y.teraType in groundeff:
            ty*=2
        if y.teraType in groundwk:
            ty/=2
        if (y.primaryType in groundimmune or y.secondaryType in groundimmune and y.teraType in ["???","Stellar"]) or y.teraType in groundimmune and y.item not in ["Ring Target","Iron Ball"] and x.grav==False and x.ability!="Ground Shock":
            ty*=0
    #GRASS
    if x.atktype=="Grass":
        if x.item in ["Miracle Seed","Meadow Plate","Rose Incense"]:
            eff*=1.2
        if y.item=="Rindo Berry" and x.ability not in ["Unnerve","As One"]:
            eff*=0.5
            em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.name}'s {y.item} weakened the damage of {x.atktype}-type move!")
            y.item+="[Used]"
        if field.terrain=="Grassy" and (x.ability not in ["Levitate"] and "Flying" not in (x.primaryType,x.secondaryType,x.teraType) or x.grav is True):
            eff*=1.3
        if x.item == "Grass Gem":
            eff*=1.5
            em.add_field(name=f"{x.icon} {x.name}'s {await itemicon(x.item)} {x.item}!",value=f"{x.item} strengthened the damage of {x.icon} {x.name}'s {x.atktype}-type moves!")
            x.item+="[Used]"
        if y.ability=="Sap Sipper":
            y.showability=True
            em.add_field(name=f"{y.icon} {y.name}'s {y.ability}!",value="Grass move was absorbed!")
            eff*=0
            await atkchange(em,y,x,1)            
        if x.ability=="Overgrow":
            if x.hp<=(x.maxhp/3):
                eff*=1.5
            else:
                eff*=1.2
        if y.primaryType in grasseff and y.teraType in ["???","Stellar"]:
            ty*=2
        if y.secondaryType in grasseff and y.teraType in ["???","Stellar"]:
            ty*=2
        if y.primaryType in grasswk and y.teraType in ["???","Stellar"]:
            ty/=2
        if y.secondaryType in grasswk and y.teraType in ["???","Stellar"]:
            ty/=2
        if y.teraType in grasseff:
            ty*=2
        if y.teraType in grasswk:
            ty/=2
    #FLYING            
    if x.atktype=="Flying" or x.use=="Flying Press":
        if x.ability=="Flock" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart","Neutralizing Gas"] and x.use not in typemoves.abilityigmoves:
            if x.hp<=(x.maxhp/3):
                eff*=1.5
            else:
                eff*=1.2
        elif x.ability=="Winged":
            eff*=1.5
        if x.item in ["Sharp Beak","Sky Plate"]:
            eff*=1.2
        if y.item=="Coba Berry" and x.ability not in ["Unnerve","As One"]:
            eff*=0.5
            em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.name}'s {y.item} weakened the damage of {x.atktype}-type move!")
            y.item+="[Used]"
        if x.item == "Flying Gem":
            eff*=1.5
            em.add_field(name=f"{x.icon} {x.name}'s {await itemicon(x.item)} {x.item}!",value=f"{x.item} strengthened the damage of {x.icon} {x.name}'s {x.atktype}-type moves!")
            x.item+="[Used]"
        if y.primaryType in flyingeff and y.teraType in ["???","Stellar"]:
            ty*=2
        if y.secondaryType in flyingeff and y.teraType in ["???","Stellar"]:
            ty*=2
        if y.primaryType in flyingwk and y.teraType in ["???","Stellar"]:
            ty/=2
        if y.secondaryType in flyingwk and y.teraType in ["???","Stellar"]:
            ty/=2
        if y.teraType in flyingeff:
            ty*=2
        if y.teraType in flyingwk:
            ty/=2
    #FIRE            
    if x.atktype=="Fire":
        if y.ability=="Well-Baked Body":
            em.add_field(name=f"{y.icon} {y.name}'s {y.ability}!",value="Fire move was absorbed!")
            y.showability=True
            await defchange(em,y,x,2)
            eff*=0
        if x.ability=="Radiant Blaze" or x.flashfire==True:
            eff*=1.5
        if y.ability=="Volcanic Body":
            em.add_field(name=f"{y.icon} {y.name}'s {y.ability}!",value="Fire move was absorbed!")
            y.showability=True
            if y.hp<=y.maxhp-(y.maxhp/4):
                y.hp+=y.maxhp/4
            if y.hp>y.maxhp-(y.maxhp/4):
                y.hp=y.maxhp            
            eff*=0
        if y.tarshot is True:
            eff*=2
        if y.ability=="Fluffy" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart","Neutralizing Gas"] and x.use not in typemoves.abilityigmoves:
            eff*=2
        if y.ability=="Steam Engine" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart","Neutralizing Gas"] and x.use not in typemoves.abilityigmoves:
            y.showability=True
            em.add_field(name=f"{y.icon} {y.name}'s {y.ability}!",value="Fire move drastically boosted its speed.")
            await speedchange(em,y,x,3)
        if x.item in ["Charcoal","Flame Plate"]:
            eff*=1.2
        if y.ability=="Water Bubble":
            eff*=0.5
        if y.item=="Occa Berry" and x.ability not in ["Unnerve","As One"]:
            eff*=0.5
            em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.name}'s {y.item} weakened the damage of {x.atktype}-type move!")
            y.item+="[Used]"
        if y.ability=="Dry Skin" and "Cloud Nine" not in (x.ability,y.ability):
            em.add_field(name=f"{y.icon} {y.name}'s {y.ability}!",value="Fire move was strengthened!")
            eff*=1.25
        elif y.ability=="Ignition" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart","Neutralizing Gas"] and x.use not in typemoves.abilityigmoves:
            y.showability=True
            em.add_field(name=f"{y.icon} {y.name}'s {y.ability}!",value="Fire move boosted its speed!")
            await speedchange(em,y,x,1)
            eff*=0            
        elif y.ability in ["Thick Fat","Heatproof"] and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart","Neutralizing Gas"] and x.use not in typemoves.abilityigmoves:
            eff*=0.5
        if field.weather=="Primordial Sea" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart","Neutralizing Gas"] and x.use not in typemoves.abilityigmoves and "Cloud Nine" not in (x.ability,y.ability):
            eff*=0
        if x.item == "Fire Gem":
            eff*=1.5
            em.add_field(name=f"{x.icon} {x.name}'s {await itemicon(x.item)} {x.item}!",value=f"{x.item} strengthened the damage of {x.icon} {x.name}'s {x.atktype}-type moves!")
            x.item+="[Used]"
        if x.ability=="Blaze" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart","Neutralizing Gas"] and x.use not in typemoves.abilityigmoves:
            if x.hp<=(x.maxhp/3):
                eff*=1.5
            else:
                eff*=1.2
        if y.ability=="Thermal Exchange" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart","Neutralizing Gas"] and x.use not in typemoves.abilityigmoves:
            em.add_field(name=f"{y.icon} {y.name}'s {y.ability}!",value="Fire move boosted its attack!")
            y.showability=True
            await atkchange(em,y,x,1)
        if y.ability=="Flash Fire" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart","Neutralizing Gas"] and x.use not in typemoves.abilityigmoves:
            y.showability=True
            em.add_field(name=f"{y.icon} {y.name}'s {y.ability}!",value="Fire move was absorbed!")
            y.flashfire=True
            eff*=0
        if y.primaryType in fireeff and y.teraType in ["???","Stellar"]:
            ty*=2
        if y.secondaryType in fireeff and y.teraType in ["???","Stellar"]:
            ty*=2
        if y.primaryType in firewk and y.teraType in ["???","Stellar"]:
            ty/=2
        if y.secondaryType in firewk and y.teraType in ["???","Stellar"]:
            ty/=2
        if y.teraType in fireeff:
            ty*=2
        if y.teraType in firewk:
            ty/=2
    #Poison            
    if x.atktype=="Poison":
        if x.ability in ["Venomous Aura"]:
            eff*=1.5
        if x.item in ["Poison Barb","Toxic Plate"]:
            eff*=1.2
        if y.item=="Kebia Berry" and x.ability not in ["Unnerve","As One"]:
            eff*=0.5
            em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.name}'s {y.item} weakened the damage of {x.atktype}-type move!")
            y.item+="[Used]"
        if x.item == "Poison Gem":
            eff*=1.5
            em.add_field(name=f"{x.icon} {x.name}'s {await itemicon(x.item)} {x.item}!",value=f"{x.item} strengthened the damage of {x.icon} {x.name}'s {x.atktype}-type moves!")
            x.item+="[Used]"
        if y.primaryType in poisoneff and y.teraType in ["???","Stellar"]:
            ty*=2
        if y.secondaryType in poisoneff and y.teraType in ["???","Stellar"]:
            ty*=2
        if y.primaryType in poisonwk and y.teraType in ["???","Stellar"]:
            ty/=2
        if y.secondaryType in poisonwk and y.teraType in ["???","Stellar"]:
            ty/=2
        if y.teraType in poisoneff:
            ty*=2
        if y.teraType in poisonwk:
            ty/=2
        if (y.primaryType in poisonimmune or y.secondaryType in poisonimmune and y.teraType in ["???","Stellar"]) or y.teraType in poisonimmune and y.item!="Ring Target":
            if x.ability!="Corrosion":
                ty*=0
            else:
                em.add_field(name=f"{x.icon} {x.name}'s {x.ability}!",value="Poison move defied its immunity!")
    #Rock
    if x.atktype=="Rock":
        if y.ability=="Lithogen" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart","Neutralizing Gas"] and x.use not in typemoves.abilityigmoves:
            y.showability=True
            em.add_field(name=f"{y.icon} {y.name}'s {y.ability}!",value="Rock move was absorbed!")
            if y.hp<=y.maxhp-(y.maxhp/4):
                y.hp+=y.maxhp/4
            if y.hp>y.maxhp-(y.maxhp/4):
                y.hp=y.maxhp
            eff*=0
        if y.ability=="Mountaineer" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart","Neutralizing Gas"] and x.use not in typemoves.abilityigmoves:
            y.showability=True
            em.add_field(name=f"{y.icon} {y.name}'s {y.ability}!",value="Rock move was absorbed!")
            eff*=0
        if x.ability=="Sand Force" and field.weather=="Sandstorm":
            eff*=1.3
        if x.item in ["Hard Stone","Stone Plate","Rock Incense"]:
            eff*=1.2
        if y.item=="Charti Berry" and x.ability not in ["Unnerve","As One"]:
            eff*=0.5
            em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.name}'s {y.item} weakened the damage of {x.atktype}-type move!")
            y.item+="[Used]"
        if y.ability=="Delta Stream" and "Flying" in (y.primaryType,y.secondaryType) and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart","Neutralizing Gas"] and x.use not in typemoves.abilityigmoves:
            eff*=0.5
        elif y.ability=="Fossilized" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart","Neutralizing Gas"] and x.use not in typemoves.abilityigmoves:
            eff*=0.5
        if x.item == "Rock Gem":
            eff*=1.5
            em.add_field(name=f"{x.icon} {x.name}'s {await itemicon(x.item)} {x.item}!",value=f"{x.item} strengthened the damage of {x.icon} {x.name}'s {x.atktype}-type moves!")
            x.item+="[Used]"
        if y.primaryType in rockeff and y.teraType in ["???","Stellar"]:
            ty*=2
        if y.secondaryType in rockeff and y.teraType in ["???","Stellar"]:
            ty*=2
        if y.primaryType in rockwk and y.teraType in ["???","Stellar"]:
            ty/=2
        if y.secondaryType in rockwk and y.teraType in ["???","Stellar"]:
            ty/=2
        if y.teraType in rockeff:
            ty*=2
        if y.teraType in rockwk:
            ty/=2
    #Normal
    if x.atktype=="Normal":
        if x.ability=="Talon Sweep":
            eff*=1.5
        if x.item in ["Silk Scarf","Blank Plate","Legend Plate","Pink Bow","Polkadot Bow"]:
            eff*=1.2
        if y.item=="Chilan Berry" and x.ability not in ["Unnerve","As One"]:
            eff*=0.5
            em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.name}'s {y.item} weakened the damage of {x.atktype}-type move!")
            y.item+="[Used]"
        if x.item == "Normal Gem":
            eff*=1.5
            em.add_field(name=f"{x.icon} {x.name}'s {await itemicon(x.item)} {x.item}!",value=f"{x.item} strengthened the damage of {x.icon} {x.name}'s {x.atktype}-type moves!")
            x.item+="[Used]"
        if y.primaryType in normaleff and y.teraType in ["???","Stellar"]:
            ty*=2
        if y.secondaryType in normaleff and y.teraType in ["???","Stellar"]:
            ty*=2
        if y.primaryType in normalwk and y.teraType in ["???","Stellar"]:
            ty/=2
        if y.secondaryType in normalwk and y.teraType in ["???","Stellar"]:
            ty/=2
        if y.teraType in normaleff:
            ty*=2
        if y.teraType in normalwk:
            ty/=2
        if ((y.primaryType in normalimmune or y.secondaryType in normalimmune) and y.teraType in ["???","Stellar"]) or (y.teraType in normalimmune and y.item!="Ring Target"):
            if x.ability not in ["Scrappy","Mind's Eye"]:
                ty*=0
            else:
                print(f" {x.name}'s {x.ability}.")
    #Fighting
    if x.atktype=="Fighting":
        
        if x.item in["Black Belt","Fist Plate"]:
            eff*=1.2
        if y.item=="Chople Berry" and x.ability not in ["Unnerve","As One"]:
            eff*=0.5
            em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.name}'s {y.item} weakened the damage of {x.atktype}-type move!")
            y.item+="[Used]"
        if x.item == "Fighting Gem":
            eff*=1.5
            em.add_field(name=f"{x.icon} {x.name}'s {await itemicon(x.item)} {x.item}!",value=f"{x.item} strengthened the damage of {x.icon} {x.name}'s {x.atktype}-type moves!")
            x.item+="[Used]"
        if y.primaryType in fightingeff and y.teraType in ["???","Stellar"]:
            ty*=2
        if y.secondaryType in fightingeff and y.teraType in ["???","Stellar"]:
            ty*=2
        if y.primaryType in fightingwk and y.teraType in ["???","Stellar"]:
            ty/=2
        if y.secondaryType in fightingwk and y.teraType in ["???","Stellar"]:
            ty/=2
        if y.teraType in fightingeff:
            ty*=2
        if y.teraType in fightingwk:
            ty/=2
        if (y.primaryType in fightingimmune or y.secondaryType in fightingimmune and y.teraType in ["???","Stellar"]) or y.teraType in fightingimmune and y.item!="Ring Target":
            ty*=0     
    if y.hp!=0:
        if y.ability=="Weak Armor" and x.atkcat=="Physical" and eff!=0:
            y.showability=True
            em.add_field(name=f"{y.icon} {y.name}'s {y.ability}!",value="Its armor cracked!")
            await defchange(em,y,y,-1)
            await speedchange(em,y,y,1)
    if x.teraType=="Stellar":
        eff*=1.3
        if x.atktype=="Stellar" and y.teraType!="???":
            ty=2
    if y.ability=="Tera Shell" and y.hp==y.maxhp:
        ty=0.5       
        em.add_field(name=f"{y.icon} {y.name}'s {y.ability}!",value="Terapagos made its shell gleam! It's distorting type matchups!")
    if ty>=2 and eff!=0:
        em.add_field(name="Effectiveness:",value=f"It's super effective!")
        if y.ability=="Primal Armor":
            y.showability=True
            em.add_field(name=f"{y.icon} {y.name}'s {y.ability}!",value="Super effective move neutralized!")
            eff*=0.5
        if x.ability=="Fatal Precision":
            eff*=1.2
        if y.item=="Enigma Berry" and x.ability not in ["Unnerve","As One"]:
            y.hp+=round(y.maxhp/4)
            y.item+="[Used]"
        if y.item=="Weakness Policy":
            em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.item} poosted attack and special attack!")
            y.item+="[Used]"
            await atkchange(em,y,x,1)
            await spatkchange(em,y,x,1)
        if x.item=="Expert Belt":
            eff*=1.2
        if y.ability in ["Solid Rock","Filter","Prism Armor","Permafrost"]:
            eff*=0.75
    elif 0<ty<1 and eff!=0:
        em.add_field(name="Effectiveness:",value=f"It's not very effective...")
        if y.ability=="Wonder Guard" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart","Neutralizing Gas"] and x.use not in typemoves.abilityigmoves:
            em.add_field(name=f"{y.icon} {y.name}'s {y.ability}!",value=f"{y.name} is immune to {x.atktype}-Type attack!")
            eff*=0
        if x.ability=="Tinted Lens":
            eff*=2
    elif ty==0 or eff==0:
        if "Legendary" in x.name:
            eff=0.5
        else:
            em.add_field(name="Effectiveness:",value=f"Doesn't effect on {y.name}.")
    else:
        if y.ability=="Wonder Guard" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart","Neutralizing Gas"] and x.use not in typemoves.abilityigmoves:
            em.add_field(name=f"{y.icon} {y.name}'s {y.ability}!",value=f"{y.name} is immune to {x.atktype}-Type attack!")
            eff*=0            
    #STAB              
    if x.atktype in (x.primaryType,x.secondaryType,x.teraType):
        if x.teraType in (x.primaryType,x.secondaryType):
            stab=2
        if x.ability=="Adaptability":
            stab=2
        if x.teraType=="???":
            stab=1.5
    eff*=ty 
    return [eff,stab]                    

async def isCrit(em,tr1,x,y,num="None"):
    if num =="None":
        num=1
    if x.fenergy==True:
        num*=2
    if x.dcheer==True:
        if ("Dragon" in (x.primaryType,x.secondaryType) and "Dragon" not in x.teraType) or "Dragon" in x.teraType:
            num*=4
        else:
            num*=2
    if "Sirfetch" in x.name and x.item=="Leek":
        num*=4
    if "Chansey" in x.name and x.item=="Lucky Punch":
        num*=4
    if x.item in ["Scope Lens","Razor Claw"]:
        num*=2
    if x.ability in ["Super Luck","Winged Fury","Hyper Cutter"]:
        num*=2
    crit=round(16/(x.critrate*num))
    if crit<1:
        crit=1
    if crit>1:
        crit=random.randint(1,crit)
    if x.ability=="Merciless" and (y.status in ["Badly Poisoned","Poisoned","Paralyzed"] or y.speed<y.maxspeed):
        crit=1
    if crit==1 and y.ability not in ["Shell Armor","Battle Armor"]:
        em.add_field(name="Critical Hit:",value="It's a critical hit.")
        muldict={1:1.5,2:2,3:2.5,4:3,5:3.5,6:4,0:1,-1:0.66,-2:0.5,-3:0.4,-4:0.33,-5:0.29,-6:0.25}
        if tr1.lightscreen is True:
            x.spdef/=2
        if tr1.reflect is True:
            x.defense/=2
        if tr1.reflect is True:
            x.defense/=2
        if x.atkb<1:
            x.atk/=muldict[x.atkb]
        if x.spatkb<1:
            x.spatk/=muldict[x.spatkb]
        if y.defb>1:
            y.defense/=muldict[y.defb]
        if y.spdefb>1:
            y.spdef/=muldict[y.spdefb]
        if y.ability=="Anger Point":
            await atkchange(em,y,x,6)
            y.showability=True
        elif y.ability=="Stamina":
            await defchange(em,y,x,6)
            y.showability=True
        if x.ability=="Sniper":
            return 2.25
        else:
            return 1.5
    elif y.ability in ["Shell Armor","Battle Armor"] and crit==1:
        return 1
    else:
        return 1                        

async def randroll():
    rr=random.randint(85,100)       
    return rr/100
                        
async def atkchange(em,x,y,amount):
    if x.ability=="Contrary":
        amount=-amount
    elif amount<0 and x!=y and x.ability=="Defiant":
        await atkchange(em,x,x,2)    
    elif amount<0 and x!=y and x.ability=="Competitive":
        await spatkchange(em,x,x,2)          
    if amount<0 and (x.ability in ["Clear Body","White Smoke","Full Metal Body","Flower Veil"] or x.item=="Clear Amulet") and x!=y:
        amount=0      
    x.atkb+=amount         
    if x.atkb<-6:
        em.add_field(name="<:low:1140755454071418910>Attack Drop:",value=f"{x.icon} {x.name}'s attack won't go any lower!")
        x.atkb=-6
    elif x.atkb>6:
        em.add_field(name="<:high:1140755420533772389>Attack Increase:",value=f"{x.icon} {x.name}'s attack won't go any higher!")
        x.atkb=6  
    elif x.atkb<=6 and x.name!="Substitute" and x.hp>0 and amount>0:
        if amount==1:
            em.add_field(name="<:high:1140755420533772389>Attack Increase:",value=f"{x.icon} {x.name}'s attack rose!")
        elif amount==2:
            em.add_field(name="<:high:1140755420533772389>Attack Increase:",value=f"{x.icon} {x.name}'s attack sharply rose!")
        elif amount>=3:
            em.add_field(name="<:high:1140755420533772389>Attack Increase:",value=f"{x.icon} {x.name}'s attack drastically rose!")
    elif x.atkb>=-6 and x.name!="Substitute" and x.hp>0:
        if amount==-1:
            em.add_field(name="<:low:1140755454071418910>Attack Drop:",value=f"{x.icon} {x.name}'s attack fell!")
        elif amount<=-2:
            em.add_field(name="<:low:1140755454071418910>Attack Drop:",value=f"{x.icon} {x.name}'s attack harshly fell!")               
    
#defense        
async def defchange(em,x,y,amount):
    if x.ability=="Contrary":
        amount=-amount
    elif amount<0 and x!=y and x.ability=="Defiant":
        await atkchange(em,x,x,2)       
    elif amount<0 and x!=y and x.ability=="Competitive":
        await spatkchange(em,x,x,2)            
    if amount<0 and (x.ability in ["Clear Body","White Smoke","Full Metal Body","Flower Veil"] or x.item=="Clear Amulet") and x!=y:
        amount=0
    x.defb+=amount
    if x.defb<-6:
        em.add_field(name="<:low:1140755454071418910>Defense Drop:",value=f"{x.icon} {x.name}'s defense won't go any lower!") 
        x.defb=-6
    if x.defb>6:
        em.add_field(name="<:high:1140755420533772389>Defense Increase:",value=f"{x.icon} {x.name}'s defense won't go any higher!")
        x.defb=6  
    elif x.defb<=6 and x.name!="Substitute" and x.hp>0 and amount>0:
        if amount==1:
            em.add_field(name="<:high:1140755420533772389>Defense Increase:",value=f"{x.icon} {x.name}'s defense rose!")
        elif amount==2:
            em.add_field(name="<:high:1140755420533772389>Defense Increase:",value=f"{x.icon} {x.name}'s defense sharply rose!")
        elif amount>=3:
            em.add_field(name="<:high:1140755420533772389>Defense Increase:",value=f"{x.icon} {x.name}'s defense drastically rose!")
    elif x.defb>=-6 and x.name!="Substitute" and x.hp>0:
        if amount==-1:
            em.add_field(name="<:low:1140755454071418910>Defense Drop:",value=f"{x.icon} {x.name}'s defense fell!")
        elif amount<=-2:
            em.add_field(name="<:low:1140755454071418910>Defense Drop:",value=f"{x.icon} {x.name}'s defense harshly fell!") 
    
#special attack       
async def spatkchange(em,x,y,amount):
    if x.ability=="Contrary":
        amount=-amount
    elif amount<0 and x!=y and x.ability=="Defiant":
        await atkchange(em,x,x,2)      
    elif amount<0 and x!=y and x.ability=="Competitive":
        await spatkchange(em,x,x,2)             
    if amount<0 and (x.ability in ["Clear Body","White Smoke","Full Metal Body","Flower Veil"] or x.item=="Clear Amulet") and x!=y:
        amount=0
    x.spatkb+=amount
    if x.spatkb<-6:
        em.add_field(name="<:low:1140755454071418910>Special Attack Drop:",value=f"{x.icon} {x.name}'s special attack won't go any lower!") 
        x.spatkb=-6
    elif x.spatkb>6:
        em.add_field(name="<:high:1140755420533772389>Special Attack Increase:",value=f"{x.icon} {x.name}'s special attack won't go any higher!")
        x.spatkb=6
    elif x.spatkb<=6 and x.name!="Substitute" and x.hp>0 and amount>0:
        if amount==1:
            em.add_field(name="<:high:1140755420533772389>Special Attack Increase:",value=f"{x.icon} {x.name}'s special attack rose!")
        elif amount==2:
            em.add_field(name="<:high:1140755420533772389>Special Attack Increase:",value=f"{x.icon} {x.name}'s special attack sharply rose!")
        elif amount>=3:
            em.add_field(name="<:high:1140755420533772389>Special Attack Increase:",value=f"{x.icon} {x.name}'s special attack drastically rose!")
    elif x.spatkb>=-6 and x.name!="Substitute" and x.hp>0:
        if amount==-1:
            em.add_field(name="<:low:1140755454071418910>Special Attack Drop:",value=f"{x.icon} {x.name}'s special attack fell!")
        elif amount<=-2:
            em.add_field(name="<:low:1140755454071418910>Special Attack Drop:",value=f"{x.icon} {x.name}'s special attack harshly fell!") 
      
#special defense       
async def spdefchange(em,x,y,amount):
    if x.ability=="Contrary":
        amount=-amount
    elif amount<0 and x!=y and x.ability=="Defiant":
        await atkchange(em,x,x,2)      
    elif amount<0 and x!=y and x.ability=="Competitive":
        await spatkchange(em,x,x,2)             
    if amount<0 and (x.ability in ["Clear Body","White Smoke","Full Metal Body","Flower Veil"] or x.item=="Clear Amulet") and x!=y:
        amount=0
    x.spdefb+=amount
    if x.spdefb<-6:
        em.add_field(name="<:low:1140755454071418910>Special Defense Drop:",value=f"{x.icon} {x.name}'s special defense won't go any lower!")
        x.spdefb=-6
    elif x.spdefb>6:
        em.add_field(name="<:high:1140755420533772389>Special Defense Increase:",value=f"{x.icon} {x.name}'s special defense won't go any higher!")
        x.spdefb=6 
    elif x.spdefb<=6 and x.name!="Substitute" and x.hp>0 and amount>0:
        if amount==1:
            em.add_field(name="<:high:1140755420533772389>Special Defense Increase:",value=f"{x.icon} {x.name}'s special defense rose!")
        elif amount==2:
            em.add_field(name="<:high:1140755420533772389>Special Defense Increase:",value=f"{x.icon} {x.name}'s special defense sharply rose!")
        elif amount>=3:
            em.add_field(name="<:high:1140755420533772389>Special Defense Increase:",value=f"{x.icon} {x.name}'s special defense drastically rose!")
    elif x.spdefb>=-6 and x.name!="Substitute" and x.hp>0:
        if amount==-1:
            em.add_field(name="<:low:1140755454071418910>Special Defense Drop:",value=f"{x.icon} {x.name}'s special defense fell!")
        elif amount<=-2:
            em.add_field(name="<:low:1140755454071418910>Special Defense Drop:",value=f"{x.icon} {x.name}'s special defense harshly fell!") 
     
#Speed        
async def speedchange(em,x,y,amount):
    if x.ability=="Contrary":
        amount=-amount
    elif amount<0 and x!=y and x.ability=="Defiant":
        await atkchange(em,x,x,2) 
    elif amount<0 and x!=y and x.ability=="Competitive":
        await spatkchange(em,x,x,2)                 
    if amount<0 and (x.ability in ["Clear Body","White Smoke","Full Metal Body","Flower Veil"] or x.item=="Clear Amulet") and x!=y:
        amount=0
    x.speedb+=amount
    if x.speedb<-6:
        em.add_field(name="<:low:1140755454071418910>Speed Drop:",value=f"{x.icon} {x.name}'s speed won't go any lower!")
        x.speedb=-6
    if x.speedb>6:
        em.add_field(name="<:high:1140755420533772389>Speed Increase:",value=f"{x.icon} {x.name}'s speed won't go any higher!")
        x.speedb=6    
    elif x.speedb<=6 and x.name!="Substitute" and x.hp>0 and amount>0:
        if amount==1:
            em.add_field(name="<:high:1140755420533772389>Speed Increase:",value=f"{x.icon} {x.name}'s speed rose!")
        elif amount==2:
            em.add_field(name="<:high:1140755420533772389>Speed Increase:",value=f"{x.icon} {x.name}'s speed sharply rose!")
        elif amount>=3:
            em.add_field(name="<:high:1140755420533772389>Speed Increase:",value=f"{x.icon} {x.name}'s speed drastically rose!")
    elif x.speedb>=-6 and x.name!="Substitute" and x.hp>0:
        if amount==-1:
            em.add_field(name="<:low:1140755454071418910>Speed Drop:",value=f"{x.icon} {x.name}'s speed fell!")
        elif amount<=-2:
            em.add_field(name="<:low:1140755454071418910>Speed Drop:",value=f"{x.icon} {x.name}'s speed harshly fell!") 