import random
from movelist import *
async def moveAI(x,y,tr1,tr2,field):
    mymove=[]
    if x.ability=="Imposter" and y.dmax is False:
        mymove+=y.moves
    if x.dmax is True:
        mymove=x.maxmoves.copy()
    elif x.dmax is False:
        mymove=x.moves.copy()
    types=[y.primaryType,y.secondaryType,y.teraType]
    mytypes=[x.primaryType,x.secondaryType,x.teraType]
    weaklist= []
    resistlist= []
    immunelist=[]
    myweaklist=[]
    myresistlist=[]
    myimmunelist=[]
    myimmunemove=[]
    stablist=[]
    mystablist=[]
    emove=[]      
    resmove=[]
    immunemove=[]
    superduper=[]
    use="None"
    bugres=['Grass', 'Fighting', 'Ground']
    bugwk=['Rock', 'Flying', 'Fire']
    #water✓
    waterres=['Water', 'Ice', 'Fire',"Steel"]
    waterwk=['Grass', 'Electric']
    #Ghost✓
    ghostres=['Poison', 'Bug']
    ghostwk=["Dark","Ghost"]
    ghostimmune=["Normal"]
    #Electric✓
    electricres=['Flying', 'Electric',"Steel"]
    electricwk=['Ground']
    #Psychic✓
    psychicres=['Fighting', 'Psychic']
    psychicwk=['Bug', 'Ghost',"Dark"]
    #Ice✓
    iceres=['Ice']
    icewk=['Steel', 'Fire', 'Fighting',"Rock"]
    #Dragon✓
    dragonres=["Fire","Water","Grass","Electric"]
    dragonwk=["Ice","Dragon","Fairy"]
    #Fairy✓
    fairyres=['Fighting', 'Bug', 'Dark']
    fairywk=['Poison', 'Steel']
    fairyimmune=["Dragon"]
    #Dark✓
    darkres=['Ghost', 'Psychic']
    darkwk=['Fighting', 'Bug', 'Fairy']
    darkimmune=["Psychic"]
    #Steel✓
    steelres=['Rock', 'Ice', 'Fairy',"Normal","Flying","Grass","Psychic","Bug","Steel","Dragon"]
    steelwk=['Fire', 'Fighting', 'Ground']
    steelimmune=["Poison"]
    #GRASS✓
    grassres=["Ground", "Electric", "Grass","Water"]
    grasswk=["Flying", "Poison", "Bug", "Ice", "Fire"]
    #FIRE✓
    fireres=["Bug", "Steel", "Grass", "Ice","Fairy","Fire"]
    firewk=["Rock", "Ground", "Water"]
    #POISON✓
    poisonres=["Grass", "Fairy","Bug","Poison","Fighting"]
    poisonwk=["Psychic", "Ground"]
    #FLYING✓
    flyingres=["Fighting", "Bug", "Grass"]
    flyingwk=['Rock', 'Ice', 'Electric']
    flyingimmune=["Ground"]
    #Rock✓
    rockres=["Flying", "Normal", "Fire", "Poison"]
    rockwk=['Fighting', 'Ground', 'Steel',"Grass","Water"]
    #Normal✓
    normalres=[]
    normalwk=['Fighting']
    normalimmune=['Ghost']
    #fighting✓
    fightingres=['Bug', 'Rock', "Dark"]
    fightingwk=["Flying", 'Psychic', 'Fairy']
    #ground
    groundres=['Poison', 'Rock']
    groundwk=['Water', 'Grass',"Ice"]
    groundimmune=["Flying"]     
    if x.zuse==True and tr1.canz==True:
        x.zuse=False
        tr1.canz=False
        return x.zmove,emove,superduper,myimmunemove 
        x.zuse=False
        tr1.canz=False
    if len(mymove)==0 and len(x.moves)==0:  
        use="Struggle"         
    type_moves = {
    "Water": {
        "stab": typemoves.watermoves,
        "weakness": waterwk,
        "resistance": waterres
    },
    "Fire": {
        "stab": typemoves.firemoves,
        "weakness": firewk,
        "resistance": fireres
    },
    "Grass": {
        "stab": typemoves.grassmoves,
        "weakness": grasswk,
        "resistance": grassres
    },
    "Electric": {
        "stab": typemoves.electricmoves,
        "weakness": electricwk,
        "resistance": electricres
    },
    "Rock": {
        "stab": typemoves.rockmoves,
        "weakness": rockwk,
        "resistance": rockres
    },
    "Ground": {
        "stab": typemoves.groundmoves,
        "weakness": groundwk,
        "resistance": groundres,
        "immunity": list(set(mymove).intersection(typemoves.electricmoves))
    },
    "Ghost": {
        "stab": typemoves.ghostmoves,
        "weakness": ghostwk,
        "resistance": ghostres,
        "immunity": list(set(mymove).intersection(typemoves.fightingmoves + typemoves.normalmoves))
    },
    "Normal": {
        "stab": typemoves.normalmoves,
        "weakness": normalwk,
        "resistance": normalres,
        "immunity": list(set(mymove).intersection(typemoves.ghostmoves))
    },
    "Dark": {
        "stab": typemoves.darkmoves,
        "weakness": darkwk,
        "resistance": darkres,
        "immunity": list(set(mymove).intersection(typemoves.psychicmoves))
    },
    "Psychic": {
        "stab": typemoves.psychicmoves,
        "weakness": psychicwk,
        "resistance": psychicres
    },
    "Bug": {
        "stab": typemoves.bugmoves,
        "weakness": bugwk,
        "resistance": bugres
    },
    "Flying": {
        "stab": typemoves.flyingmoves,
        "weakness": flyingwk,
        "resistance": flyingres,
        "immunity": list(set(mymove).intersection(typemoves.groundmoves))
    },
    "Fighting": {
        "stab": typemoves.fightingmoves,
        "weakness": fightingwk,
        "resistance": fightingres
    },
    "Fairy": {
        "stab": typemoves.fairymoves,
        "weakness": fairywk,
        "resistance": fairyres,
        "immunity": list(set(mymove).intersection(typemoves.dragonmoves))
    },
    "Steel": {
        "stab": typemoves.steelmoves,
        "weakness": steelwk,
        "resistance": steelres,
        "immunity": list(set(mymove).intersection(typemoves.poisonmoves))
    },
    "Poison": {
        "stab": typemoves.poisonmoves,
        "weakness": poisonwk,
        "resistance": poisonres
    },
    "Ice": {
        "stab": typemoves.icemoves,
        "weakness": icewk,
        "resistance": iceres
    },
    "Dragon": {
        "stab": typemoves.dragonmoves,
        "weakness": dragonwk,
                "resistance": dragonres
    }
}
    for type in types:
        if y.teraType==types[-1] and (y.teraType not in ["???","Stellar"]) and (type not in ["???","Stellar"]):
            type_data = type_moves[type]
            weaklist += list(set(type_data["weakness"])-set(typemoves.statusmove))
            resistlist += type_data["resistance"]
            if "immunity" in type_data:
                myimmunemove += type_data["immunity"]    
        elif type not in ["???","Stellar"]:
            type_data = type_moves[type]
            stablist += type_data["stab"]
            weaklist += list(set(type_data["weakness"])-set(typemoves.statusmove))
            resistlist += type_data["resistance"]
            if "immunity" in type_data:
                myimmunemove += type_data["immunity"]  
    mystablist+=("Judgement","Multi-Attack")
    weaklist=list(set(weaklist)-set(resistlist)-set(immunelist))
    if x.taunted:
        myimmunemove+=list(set(mymove). intersection (typemoves.statusmove))
    if (field.terrain=="Psychic") or y.ability in ["Dazzling","Queenly Majesty","Armor Tail"]:
        myimmunemove+=list(set(mymove). intersection (typemoves.prioritymove))
    if y.ability in ["Water Absorb","Water Compaction","Storm Drain","Dry Skin"] or field.weather=="Desolate Land":
        myimmunemove+=list(set(mymove). intersection (typemoves.watermoves))
    elif y.ability in ["Volt Absorb","Motor Drive","Lightning Rod"]:
        myimmunemove+=list(set(mymove). intersection (typemoves.electricmoves))     
    elif y.ability in ["Flash Fire","Well-baked Body"] or field.weather=="Primordial Sea":
        myimmunemove+=list(set(mymove). intersection (typemoves.firemoves))    
    elif y.ability in ["Levitate","Earth Eater"] or y.item=="Air Balloon":
        myimmunemove+=list(set(mymove). intersection (typemoves.groundmoves))               
        
    elif "Water" in weaklist and y.ability not in ["Water Absorb","Water Compaction","Storm Drain","Dry Skin"]:
        emove+=list(set(mymove). intersection(typemoves.watermoves))
    elif "Fire" in weaklist and y.ability not in ["Well-baked Body","Flash Fire"]:
        emove+=list(set(mymove). intersection(typemoves.firemoves))
    elif "Grass" in weaklist and y.ability not in ["Sap Sipper"]:
        emove+=list(set(mymove). intersection(typemoves.grassmoves))          
    elif "Rock" in weaklist and y.ability not in ["Mountaineer"]:
        emove+=list(set(mymove). intersection(typemoves.rockmoves))     
    elif "Ground" in weaklist and y.ability not in ["Levitate","Earth Eater"] and y.item!="Air Balloon":
        emove+=list(set(mymove). intersection(typemoves.groundmoves)) 
    if "Ice" in weaklist:
        emove+=list(set(mymove). intersection(typemoves.icemoves))
    if "Dragon" in weaklist:
        emove+=list(set(mymove). intersection(typemoves.dragonmoves))     
    if "Normal" in weaklist:
        emove+=list(set(mymove). intersection(typemoves.normalmoves))     
    if "Steel" in weaklist:
        emove+=list(set(mymove). intersection(typemoves.steelmoves))          
    if "Fairy" in weaklist:
        emove+=list(set(mymove). intersection(typemoves.fairymoves))            
    if "Poison" in weaklist and y.ability not in ["Immunity"]:
        emove+=list(set(mymove). intersection(typemoves.poisonmoves))        
    if "Fighting" in weaklist:
        emove+=list(set(mymove). intersection(typemoves.fightingmoves))        
    if "Flying" in weaklist:
        emove+=list(set(mymove). intersection(typemoves.flyingmoves))        
    if "Bug" in weaklist:
        emove+=list(set(mymove). intersection(typemoves.bugmoves))        
    if "Psychic" in weaklist and y.ability not in ["Dark Mind"]:
        emove+=list(set(mymove). intersection(typemoves.psychicmoves))       
    if "Ghost" in weaklist and y.ability not in ["Purifying Salt"]:
        emove+=list(set(mymove). intersection(typemoves.ghostmoves))        
    if "Dark" in weaklist:
        emove+=list(set(mymove). intersection(typemoves.darkmoves))        
    if "Water" in resistlist:
        resmove+=list(set(mymove). intersection(typemoves.watermoves))
    if "Fire" in resistlist:
        resmove+=list(set(mymove). intersection(typemoves.firemoves))
    if "Grass" in resistlist:
        resmove+=list(set(mymove). intersection(typemoves.grassmoves))          
    if "Rock" in resistlist:
        resmove+=list(set(mymove). intersection(typemoves.rockmoves))     
    if "Ground" in resistlist:
        resmove+=list(set(mymove). intersection(typemoves.groundmoves)) 
    if "Electric" in resistlist:
        resmove+=list(set(mymove). intersection(typemoves.electricmoves))              
    if "Ice" in resistlist:
        resmove+=list(set(mymove). intersection(typemoves.icemoves))
    if "Dragon" in resistlist:
        resmove+=list(set(mymove). intersection(typemoves.dragonmoves))     
    if "Normal" in resistlist:
        resmove+=list(set(mymove). intersection(typemoves.normalmoves))     
    if "Steel" in resistlist:
        resmove+=list(set(mymove). intersection(typemoves.steelmoves))          
    if "Fairy" in resistlist:
        resmove+=list(set(mymove). intersection(typemoves.fairymoves))            
    if "Poison" in resistlist:
        resmove+=list(set(mymove). intersection(typemoves.poisonmoves))        
    if "Fighting" in resistlist:
        resmove+=list(set(mymove). intersection(typemoves.fightingmoves))        
    if "Flying" in resistlist:
        resmove+=list(set(mymove). intersection(typemoves.flyingmoves))        
    if "Bug" in resistlist:
        resmove+=list(set(mymove). intersection(typemoves.bugmoves))        
    if "Psychic" in resistlist:
        resmove+=list(set(mymove). intersection(typemoves.psychicmoves))       
    if "Ghost" in resistlist:
        resmove+=list(set(mymove). intersection(typemoves.ghostmoves))        
    if "Dark" in resistlist:
        resmove+=list(set(mymove). intersection(typemoves.darkmoves))                
    eheal=list(set(mymove).intersection(typemoves.healingmoves))
    eprior=list(set(mymove).intersection(typemoves.priorityatkmoves))
    superduper=list(set(emove).intersection(mystablist))
    mymove=list(set(mymove)-set(myimmunelist))
    if x.item !="None" and "Choice" in x.item:
        mymove=list(set(mymove)-set(typemoves.statusmove))
        mymove=list(set(mymove)-set(typemoves.terrainmove))
        mymove=list(set(mymove)-set(typemoves.weathermoves))
    if x.hp==x.maxhp:
        mymove=list(set(mymove)-set(typemoves.healingmoves))
    if x.canfakeout is False:
        if "First Impression" in mymove:
            mymove.remove("First Impression")
        if "Fake Out" in mymove:
            mymove.remove("Fake Out")
    if tr1.hazard!=[]:
        if "Defog" in mymove:
            use="Defog"  
    if x.choiced is True:
        mymove=list(set(mymove)-set(mymove). intersection(typemoves.statusmove))       
    if "Sleep Talk" in x.moves and x.status!="Sleep":
        mymove.remove("Sleep Talk")                     
    if "Stealth Rock" in tr2.hazard:
        if "Stealth Rock" in mymove:
            mymove.remove("Stealth Rock")
    if y.status=="Badly Poisoned" or (y.primaryType in ["Steel","Poison"] or y.secondaryType in ["Steel","Poison"] and x.ability!="Corrosion"):
        if "Toxic" in mymove:
            mymove.remove("Toxic")
    if y.status=="Paralyzed":
        if "Thunder Wave" in mymove:
            mymove.remove("Thunder Wave")         
    if x.spatkb==6:
        if "Tail Glow" in mymove:
            mymove.remove("Tail Glow")      
    if y.atkcat=="Physical" and "Counter" in x.moves and y.use in typemoves.physicalmoves:
        use="Counter"                   
    if y.atkcat=="Special" and "Mirror Coat" in x.moves and y.use not in typemoves.physicalmoves and y.use not in typemoves.statusmove:
        use="Mirror Coat"
    if x.use=="Gigaton Hammer" and "Gigaton Hammer" in x.moves:
        mymove.remove("Gigaton Hammer")  
    if y.seeded is True:
        if "Leech Seed" in mymove:
            mymove.remove("Leech Seed")      
    if field.weather=="Sandstorm":
        if "Sandstorm" in mymove:
            mymove.remove("Sandstorm")   
    if field.weather=="Snowstorm":
        if "Snowscape" in mymove:
            mymove.remove("Snowscape")
    if field.weather=="Hail":
        if "Hail" in mymove:
            mymove.remove("Hail")                    
    if field.weather=="Sunny":
        if "Sunny Day" in mymove:
            mymove.remove("Sunny Day")        
    if field.weather=="Rainy":
        if "Rain Dance" in mymove:
            mymove.remove("Rain Dance")
    if y.atkb<1 and y.status=="Alive":    
        if "Will-O-Wisp" in mymove:    
            use="Will-O-Wisp"
    if x.speed<y.speed and y.status=="Alive":
        if "Thunder Wave" in mymove:
            use="Thunder Wave"
    if x.spatkb==6:
        mymove=list(set(mymove)-set(mymove). intersection(typemoves.spatkboost))            
    if x.atkb==6:
        mymove=list(set(mymove)-set(mymove). intersection(typemoves.atkboost))            
    if x.protect!=False:       
        mymove=list(set(mymove)-set(typemoves.protectmoves))
    if y.status!="Alive":
        mymove=list(set(mymove)-set(typemoves.statuschangemoves))
    mystablist=list(set(mymove). intersection (mystablist))        
    if "Trick Room" in mymove and field.trickroom is False and x.speed<y.speed:
        use="Trick Room"                      
    if x.hp<(x.maxhp/2) and x.speed<y.speed and y.hp!=(y.maxhp*0.3):
        if len(eheal)!=0:
            use=eheal[0]   
    if x.hp<=(x.maxhp/3) and x.speed<=y.speed:         
        if len(eheal)!=0:
            use=eheal[0]
    if len(emove)>0 and len(superduper)==0:
        use=random.choice(emove)
    elif len(superduper)>0:
        use= superduper[0]
    elif len(mystablist)>0 and len(emove)==0:
        use=random.choice(mystablist)  
    if field.terrain=="Normal":
        tmove=list (set(mymove).intersection(typemoves.terrainmove))
        if len(tmove)!=0:
            use=tmove[0]
    if x.choiced is False and x.atk>x.spatk and x.atkb<=1 and x.hp>(x.maxhp*0.5) and y.hp>(y.maxhp*0.2) and x.item not in ["Assault Vest"] and x.dmax==False:
        boost=list (set(mymove).intersection(typemoves.atkboost))
        if len(boost)!=0:
            use=boost[0]        
    if x.choiced is False and x.spatk>x.atk and x.spatkb<=1 and x.hp>(x.maxhp*0.5) and y.hp>(y.maxhp*0.2) and x.item not in ["Assault Vest"] and x.dmax==False:
        boost=list (set(mymove).intersection(typemoves.spatkboost))
        if len(boost)!=0:
            use=boost[0]   
    if x.choiced is False and y.speed>y.speed and "Tailwind" in mymove and tr1.tailwind is not True and x.item not in ["Assault Vest"] and x.dmax==False:
        use="Tailwind"                
    if x.choiced is False and y.atk>y.spatk and "Reflect" in mymove and tr1.reflect is not True and x.item not in ["Assault Vest"] and x.dmax==False:
        use="Reflect"              
    if x.choiced is False and y.spatk>y.atk and "Light Screen" in mymove and tr1.lightscreen is not True and x.item not in ["Assault Vest"] and x.dmax==False:
        use="Light Screen"        
    if x.protect is False and "King's Shield" in mymove and y.hp>=(y.maxhp*0.2) and x.dmax==False:
        use="King's Shield"       
    if x.item !="None" and "Sticky Web"  not in tr2.hazard and "Choice" not in x.item and y.hp>=(y.maxhp*0.3) and x.item not in ["Assault Vest"] and x.dmax==False:
        if "Sticky Web"  in mymove:
            use="Sticky Web"                    
    if x.item !="None" and "Stealth Rock"  not in tr2.hazard and "Choice" not in x.item and y.hp>=(y.maxhp*0.3) and x.item not in ["Assault Vest"]:
        if "Stealth Rock"  in mymove:
            use="Stealth Rock"      
    if x.item !="None" and "Toxic Spikes"  not in tr2.hazard and "Choice" not in x.item and y.hp>=(y.maxhp*0.3) and x.item not in ["Assault Vest"] and x.dmax==False:
        if "Toxic Spikes"  in mymove:
            use="Toxic Spikes"  
    if (y.hp<=(y.maxhp*0.20) or y.defb<0.5) and x.speed<y.speed and len(eprior)!=0:
        use=random.choice(eprior+emove) 
    if x.hp<=(x.maxhp*0.25) and "Destiny Bond" in mymove and x.speed>y.speed and x.dmax==False:
        use="Destiny Bond"
    if x.hp<=(x.maxhp*0.25) and "Misty Explosion" in mymove and x.dmax==False:
        use="Misty Explosion"
    if x.hp<=(x.maxhp*0.25) and "Explosion" in mymove and x.dmax==False:
        use="Explosion"
    if "Hero" not in x.name and "Flip Turn" in x.moves and x.ability=="Zero to Hero":
        use="Flip Turn"
    if y.status in ["Poison","Badly Poisoned"] and len(list(set(x.moves). intersection(["Venoshock"])))>0 and "Steel" not in (y.primaryType,y.secondaryType,y.teraType) and "Poison" not in (y.primaryType,y.secondaryType,y.teraType):
        use=list(set(x.moves). intersection (["Venoshock"]))[0]
    if y.status!="Alive" and len(list(set(x.moves). intersection(["Hex","Infernal Parade","Bitter Malice","Barb Barrage"])))>0 and "Ghost" not in (y.primaryType,y.secondaryType,y.teraType):
        use=list(set(x.moves).intersection (["Hex","Infernal Parade","Bitter Malice","Barb Barrage"]))[0]
    if x.status=="Sleep" and "Sleep Talk" in x.moves and x.choiced==False:
        use="Sleep Talk"
    if len(x.moves)==5 and (y.maxdef<250 or y.maxspdef<250):
        use=x.moves[4]
    if x.fmove==True:
        use=list(set(x.moves).intersection(["Outrage","Thrash","Petal Dance","Raging Fury"]))[0]
    if x.speed>y.speed and ((y.hp<y.maxhp*0.35) or y.defense<200 or y.spdef<200):
        if len(emove)>0:
            use=random.choice(emove)
        elif len(emove)>0:
            use=random.choice(resmove)
        elif len(mymove)!=0:
            use=random.choice(mymove)        
    if "Choice" in x.item and x.choiced is False and x.dmax is False:
        x.choiced=True
        x.choicedmove=use            
    if x.choiced is True and x.dmax is False:
        if x.choicedmove in x.moves:
            use=x.choicedmove 
    elif use =="None" or use==[]:
        if len(mymove)==0:
            if len(resmove)==0:
                use=random.choice(mymove)
            else:
                use=random.choice(resmove)
        else:
            use=random.choice(mymove)
#    print("=====================")     
#        print(f"{x.name}'s AI says against {y.name}:"    )
#    print("=====================")     
#    print(f" {x.name}'s USABLE MOVES:",mymove)
#    print("EFFECTIVE MOVES:",emove)
#    if myimmunemove!=[]:
#        print(f" {x.name}'s IMMUNE MOVES on {y.name}: ",myimmunemove)
#    print("RESISTED MOVES: ",resmove)
#    print("NON RES STAB MOVES:",mystablist)
#    print("STAB AND EFFECTIVE:",superduper)
#    print("CHOICED MOVE:",x.choicedmove)
#    print("SELECTED MOVE:",use)   
#    print("=====================")       
    return use,emove,superduper,myimmunemove 