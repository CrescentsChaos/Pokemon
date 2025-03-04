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
    #Bug
    bugres=['Grass', 'Fighting', 'Ground']
    bugwk=['Rock', 'Flying', 'Fire']
    #water
    waterres=['Water', 'Ice', 'Fire',"Steel"]
    waterwk=['Grass', 'Electric']
    #Ghost
    ghostres=['Poison', 'Bug']
    ghostwk=["Dark","Ghost"]
    ghostimmune=["Normal"]
    #Electric
    electricres=['Flying', 'Electric',"Steel"]
    electricwk=['Ground']
    #Psychic
    psychicres=['Fighting', 'Psychic']
    psychicwk=['Bug', 'Ghost',"Dark"]
    #Ice
    iceres=['Ice']
    icewk=['Steel', 'Fire', 'Fighting',"Rock"]
    #Dragon
    dragonres=["Fire","Water","Grass","Electric"]
    dragonwk=["Ice","Dragon","Fairy"]
    #Fairy
    fairyres=['Fighting', 'Bug', 'Dark']
    fairywk=['Poison', 'Steel']
    fairyimmune=["Dragon"]
    #Dark
    darkres=['Ghost', 'Psychic']
    darkwk=['Fighting', 'Bug', 'Fairy']
    darkimmune=["Psychic"]
    #Steel
    steelres=['Rock', 'Ice', 'Fairy',"Normal","Flying","Grass","Psychic","Bug","Steel","Dragon"]
    steelwk=['Fire', 'Fighting', 'Ground']
    steelimmune=["Poison"]
    #GRASS
    grassres=["Ground", "Electric", "Grass","Water"]
    grasswk=["Flying", "Poison", "Bug", "Ice", "Fire"]
    #FIRE
    fireres=["Bug", "Steel", "Grass", "Ice","Fairy","Fire"]
    firewk=["Rock", "Ground", "Water"]
    #POISON
    poisonres=["Grass", "Fairy","Bug","Poison","Fighting"]
    poisonwk=["Psychic", "Ground"]
    #FLYING
    flyingres=["Fighting", "Bug", "Grass"]
    flyingwk=['Rock', 'Ice', 'Electric']
    flyingimmune=["Ground"]
    #Rock
    rockres=["Flying", "Normal", "Fire", "Poison"]
    rockwk=['Fighting', 'Ground', 'Steel',"Grass","Water"]
    #Normal
    normalres=[]
    normalwk=['Fighting']
    normalimmune=['Ghost']
    #fighting
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
        type_data = type_moves[type]
        stablist += type_data["stab"]
        if y.teraType==types[-1]:
            type_data = type_moves[type]
            weaklist += list(set(type_data["weakness"])-set(typemoves.statusmove))
            resistlist += type_data["resistance"]
            if "immunity" in type_data:
                myimmunemove += type_data["immunity"]    
        elif y.teraType=="???":
            type_data = type_moves[type]
            weaklist += list(set(type_data["weakness"])-set(typemoves.statusmove))
            resistlist += type_data["resistance"]
            if "immunity" in type_data:
                myimmunemove += type_data["immunity"]  
    weaklist=list(set(weaklist)-set(resistlist)-set(immunelist))                       