#pylint:disable=W0613
#pylint:disable=C0103
#pylint:disable=C0321
#pylint:disable=C0301
#pylint:disable=W0612
#pylint:disable=C0304
#pylint:disable=C0303
import random
from movelist import *
def moveAI(self,other,mtr,otr,field):
    mymove=[]
    if self.ability=="Imposter" and other.dmax is False:
        mymove+=other.moves
    if self.dmax is True:
        mymove+=self.maxmove
    if self.dmax is False:
        mymove+=self.moves
    types=[other.type1,other.type2,other.teratype]
    mytypes=[self.type1,self.type2,self.teratype]
    if self.ability=="Galvanize":
        typemoves.electricmoves+=typemoves.normalmoves
    if self.ability=="Aerilate":
        typemoves.flyingmoves+=typemoves.normalmoves
    if self.ability=="Pixilate":
        typemoves.fairymoves+=typemoves.normalmoves
    if self.ability=="Liquid Voice":
        typemoves.watermoves+=typemoves.normalmoves
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
    if len(mymove)==0 and len(self.moves)==0:  
        use="Struggle"     
    
    if "Water" in types:
        stablist+=typemoves.watermoves
        weaklist=weaklist+waterwk
        resistlist=resistlist+waterres
    if "Fire" in types:
        stablist+=typemoves.firemoves
        weaklist=weaklist+firewk
        resistlist=resistlist+fireres
    if "Grass" in types:
        stablist+=typemoves.grassmoves
        weaklist=weaklist+grasswk
        resistlist=resistlist+grassres
    if "Electric" in types:
        stablist+=typemoves.electricmoves
        weaklist=weaklist+electricwk
        resistlist=resistlist+electricres
    if "Rock" in types:
        stablist+=typemoves.rockmoves
        weaklist=weaklist+rockwk
        resistlist=resistlist+rockres
    if "Ground" in types:
        stablist+=typemoves.groundmoves
        weaklist=weaklist+groundwk
        resistlist=resistlist+groundres
        #myimmunemove+=set(mymove).intersection(typemoves.groundmoves)
        myimmunemove+=list(set(mymove). intersection (typemoves.electricmoves))
    if "Ghost" in types:
        stablist+=typemoves.ghostmoves
        weaklist=weaklist+ghostwk
        resistlist=resistlist+ghostres
        myimmunemove+=list(set(mymove). intersection (typemoves.fightingmoves))
        myimmunemove+=list(set(mymove). intersection (typemoves.normalmoves))
    if "Normal" in types:
        stablist+=typemoves.normalmoves
        weaklist=weaklist+normalwk
        resistlist=resistlist+normalres
        myimmunemove+=list(set(mymove). intersection (typemoves.ghostmoves))
    if "Dark" in types:
        stablist+=typemoves.darkmoves
        weaklist=weaklist+darkwk
        resistlist=resistlist+darkres
        myimmunemove+=list(set(mymove). intersection (typemoves.psychicmoves))
    if "Psychic" in types:
        stablist+=typemoves.psychicmoves
        weaklist=weaklist+psychicwk
        resistlist=resistlist+psychicres
    if "Bug" in types:
        stablist+=typemoves.bugmoves
        weaklist=weaklist+bugwk
        resistlist=resistlist+bugres
    if "Flying" in types:
        stablist+=typemoves.flyingmoves
        weaklist=weaklist+flyingwk
        resistlist=resistlist+flyingres
        myimmunemove+=list(set(mymove). intersection (typemoves.groundmoves))
    if "Fighting" in types:
        stablist+=typemoves.fightingmoves
        weaklist=weaklist+fightingwk
        resistlist=resistlist+fightingres
    if "Fairy" in types:
        stablist+=typemoves.fairymoves
        weaklist=weaklist+fairywk
        resistlist=resistlist+fairyres
        myimmunemove+=list(set(mymove). intersection (typemoves.dragonmoves))
    if "Steel" in types:
        stablist+=typemoves.steelmoves
        weaklist=weaklist+steelwk
        resistlist=resistlist+steelres
        myimmunemove+=list(set(mymove). intersection (typemoves.poisonmoves))
    if "Poison" in types:
        stablist+=typemoves.poisonmoves
        weaklist=weaklist+poisonwk
        resistlist=resistlist+poisonres
    if "Ice" in types:
        stablist+=typemoves.icemoves
        weaklist=weaklist+icewk
        resistlist=resistlist+iceres
    if "Dragon" in types:
        stablist+=typemoves.dragonmoves
        weaklist=weaklist+dragonwk
        resistlist=resistlist+dragonres
    mystablist+=("Judgement","Multi-Attack")
    weaklist=list(set(weaklist)-set(resistlist)-set(immunelist))
    if self.taunted:
        myimmunemove+=list(set(mymove). intersection (typemoves.statusmove))
    if (field.terrain=="Psychic") or other.ability in ["Dazzling","Queenly Majesty","Armor Tail"]:
        myimmunemove+=list(set(mymove). intersection (typemoves.prioritymove))
    if other.ability in ["Water Absorb","Water Compaction","Storm Drain","Dry Skin"] or field.weather=="Desolate Land":
        myimmunemove+=list(set(mymove). intersection (typemoves.watermoves))
    if other.ability in ["Volt Absorb","Motor Drive","Lightning Rod"]:
        myimmunemove+=list(set(mymove). intersection (typemoves.electricmoves))     
    if other.ability in ["Flash Fire","Well-baked Body"] or field.weather=="Primordial Sea":
        myimmunemove+=list(set(mymove). intersection (typemoves.firemoves))    
    if other.ability in ["Levitate","Earth Eater"] or other.item=="Air Balloon":
        myimmunemove+=list(set(mymove). intersection (typemoves.groundmoves))               
        
    if "Water" in weaklist and other.ability not in ["Water Absorb","Water Compaction","Storm Drain","Dry Skin"]:
        emove+=list(set(mymove). intersection(typemoves.watermoves))
    if "Fire" in weaklist and other.ability not in ["Well-baked Body","Flash Fire"]:
        emove+=list(set(mymove). intersection(typemoves.firemoves))
    if "Grass" in weaklist and other.ability not in ["Sap Sipper"]:
        emove+=list(set(mymove). intersection(typemoves.grassmoves))          
    if "Rock" in weaklist and other.ability not in ["Mountaineer"]:
        emove+=list(set(mymove). intersection(typemoves.rockmoves))     
    if "Ground" in weaklist and other.ability not in ["Levitate","Earth Eater"] and other.item!="Air Balloon":
        emove+=list(set(mymove). intersection(typemoves.groundmoves)) 
    if "Electric" in weaklist and other.ability not in ["Volt Absorb","Lightning Rod","Motor Drive"]:
        emove+=list(set(mymove). intersection(typemoves.electricmoves))
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
    if "Poison" in weaklist and other.ability not in ["Immunity"]:
        emove+=list(set(mymove). intersection(typemoves.poisonmoves))        
    if "Fighting" in weaklist:
        emove+=list(set(mymove). intersection(typemoves.fightingmoves))        
    if "Flying" in weaklist:
        emove+=list(set(mymove). intersection(typemoves.flyingmoves))        
    if "Bug" in weaklist:
        emove+=list(set(mymove). intersection(typemoves.bugmoves))        
    if "Psychic" in weaklist and other.ability not in ["Dark Mind"]:
        emove+=list(set(mymove). intersection(typemoves.psychicmoves))       
    if "Ghost" in weaklist and other.ability not in ["Purifying Salt"]:
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
    #use="None"
    eheal=list(set(mymove).intersection(typemoves.healingmoves))
    eprior=list(set(mymove).intersection(typemoves.priorityatkmoves))
    superduper=list(set(emove).intersection(mystablist))
    mymove=list(set(mymove)-set(myimmunelist))
    if self.item !="None" and "Choice" in self.item:
        mymove=list(set(mymove)-set(typemoves.statusmove))
        mymove=list(set(mymove)-set(typemoves.terrainmove))
        mymove=list(set(mymove)-set(typemoves.weathermoves))
    if self.hp==self.maxhp:
        mymove=list(set(mymove)-set(typemoves.healingmoves))
    if self.canfakeout is False:
        if "First Impression" in mymove:
            mymove.remove("First Impression")
        if "Fake Out" in mymove:
            mymove.remove("Fake Out")
    if mtr.hazard!=[]:
        if "Defog" in mymove:
            use="Defog"  
    if self.choiced is True:
        mymove=list(set(mymove)-set(mymove). intersection(typemoves.statusmove))             
    if "Stealth Rock" in otr.hazard:
        if "Stealth Rock" in mymove:
            mymove.remove("Stealth Rock")
    if other.status=="Badly Poisoned" or (other.type1 in ["Steel","Poison"] or other.type2 in ["Steel","Poison"] and self.ability!="Corrosion"):
        if "Toxic" in mymove:
            mymove.remove("Toxic")
    if other.status=="Paralyzed":
        if "Thunder Wave" in mymove:
            mymove.remove("Thunder Wave")         
    if self.spatkb==4:
        if "Tail Glow" in mymove:
            mymove.remove("Tail Glow")      
    if other.atkcat=="Physical" and "Counter" in self.moves:
        use="Counter"                   
    if other.atkcat=="Special" and "Mirror Coat" in self.moves:
        use="Mirror Coat"
    if self.use=="Gigaton Hammer" and "Gigaton Hammer" in self.moves:
        mymove.remove("Gigaton Hammer")  
    if other.seeded is True:
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
    if other.owner.future!=0:
        if "Future Sight" in mymove:
            mymove.remove("Future Sight")               
    if field.weather=="Sunny":
        if "Sunny Day" in mymove:
            mymove.remove("Sunny Day")        
    if field.weather=="Rainy":
        if "Rain Dance" in mymove:
            mymove.remove("Rain Dance")
    if other.atkb<1 and other.status=="Alive":    
        if "Will-O-Wisp" in mymove:    
            use="Will-O-Wisp"
    if self.speed<other.speed and other.status=="Alive":
        if "Thunder Wave" in mymove:
            use="Thunder Wave"
    if self.spatkb==4:
        mymove=list(set(mymove)-set(mymove). intersection(typemoves.spatkboost))            
    if self.atkb==4:
        mymove=list(set(mymove)-set(mymove). intersection(typemoves.atkboost))            
    if self.protect!=False:       
        mymove=list(set(mymove)-set(typemoves.protectmoves))
    if other.status!="Alive":
        mymove=list(set(mymove)-set(typemoves.statuschangemoves))
    mystablist=list(set(mymove). intersection (mystablist))        
    if "Trick Room" in mymove and field.trickroom is False and self.speed<other.speed:
        use="Trick Room"                      
    if self.hp<(self.maxhp/2) and self.speed<other.speed and other.hp!=(other.maxhp*0.3):
        if len(eheal)!=0:
            use=eheal[0]   
    if self.hp<=(self.maxhp/3) and self.speed<=other.speed:         
        if len(eheal)!=0:
            use=eheal[0]
    if len(emove)>0 and len(superduper)==0:
        use=random.choice(emove)
    if len(superduper)>0:
        use= superduper[0]
    if len(mystablist)>0 and len(emove)==0:
        use=random.choice(mystablist)  
    if field.terrain=="Normal":
        tmove=list (set(mymove).intersection(typemoves.terrainmove))
        if len(tmove)!=0:
            use=tmove[0]
    if self.choiced is False and self.atk>self.spatk and self.atkb<=1 and self.hp>(self.maxhp*0.5) and other.hp>(other.maxhp*0.2) and self.item not in ["Assault Vest"] and self.dmax==False:
        boost=list (set(mymove).intersection(typemoves.atkboost))
        if len(boost)!=0:
            use=boost[0]        
    if self.choiced is False and self.spatk>self.atk and self.spatkb<=1 and self.hp>(self.maxhp*0.5) and other.hp>(other.maxhp*0.2) and self.item not in ["Assault Vest"] and self.dmax==False:
        boost=list (set(mymove).intersection(typemoves.spatkboost))
        if len(boost)!=0:
            use=boost[0]   
    if self.choiced is False and other.speed>other.speed and "Tailwind" in mymove and mtr.tailwind is not True and self.item not in ["Assault Vest"] and self.dmax==False:
        use="Tailwind"                
    if self.choiced is False and other.atk>other.spatk and "Reflect" in mymove and mtr.reflect is not True and self.item not in ["Assault Vest"] and self.dmax==False:
        use="Reflect"              
    if self.choiced is False and other.spatk>other.atk and "Light Screen" in mymove and mtr.lightscreen is not True and self.item not in ["Assault Vest"] and self.dmax==False:
        use="Light Screen"        
    if self.protect is False and "King's Shield" in mymove and other.hp>=(other.maxhp*0.2) and self.dmax==False:
        use="King's Shield"       
    if self.item !="None" and "Sticky Web"  not in otr.hazard and "Choice" not in self.item and other.hp>=(other.maxhp*0.3) and self.item not in ["Assault Vest"] and self.dmax==False:
        if "Sticky Web"  in mymove:
            use="Sticky Web"                    
    if self.item !="None" and "Stealth Rock"  not in otr.hazard and "Choice" not in self.item and other.hp>=(other.maxhp*0.3) and self.item not in ["Assault Vest"]:
        if "Stealth Rock"  in mymove:
            use="Stealth Rock"      
    if self.item !="None" and "Toxic Spikes"  not in otr.hazard and "Choice" not in self.item and other.hp>=(other.maxhp*0.3) and self.item not in ["Assault Vest"] and self.dmax==False:
        if "Toxic Spikes"  in mymove:
            use="Toxic Spikes"  
    if (other.hp<=(other.maxhp*0.20) or other.defb<0.5) and self.speed<other.speed and len(eprior)!=0:
        use=random.choice(eprior+emove)  
    if self.item !="None" and "Choice" in self.item and self.choiced is False and use !="None" and self.dmax is False and self.owner.ai==True and self.owner.ai==True:
        self.choiced=True
        self.choicedmove=use
    if self.hp<=(self.maxhp*0.25) and "Destiny Bond" in mymove and self.speed>other.speed and self.dmax==False:
        use="Destiny Bond"
    if self.hp<=(self.maxhp*0.25) and "Misty Explosion" in mymove and self.dmax==False:
        use="Misty Explosion"
    if self.hp<=(self.maxhp*0.25) and "Explosion" in mymove and self.dmax==False:
        use="Explosion"
    if "Hero" not in self.name and "Flip Turn" in self.moves and self.ability=="Zero to Hero":
        use="Flip Turn"
    if other.status in ["Poison","Badly Poisoned"] and len(list(set(self.moves). intersection(["Venoshock"])))>0 and "Steel" not in (other.type1,other.type2,other.teratype) and "Poison" not in (other.type1,other.type2,other.teratype):
        use=list(set(self.moves). intersection (["Venoshock"]))[0]
    if other.status!="Alive" and len(list(set(self.moves). intersection(["Hex","Infernal Parade","Bitter Malice","Barb Barrage"])))>0 and "Ghost" not in (other.type1,other.type2,other.teratype):
        use=list(set(self.moves). intersection (["Hex","Infernal Parade","Bitter Malice","Barb Barrage"]))[0]
    if self.status=="Sleep" and "Sleep Talk" in self.moves and self.choiced==False:
        use="Sleep Talk"
    if len(self.moves)==5 and (other.maxdef<250 or other.maxspdef<250):
        use=self.moves[4]
    if self.fmove==True:
        use=list(set(self.moves).intersection(["Outrage","Thrash","Petal Dance","Raging Fury"]))[0]
    if self.speed>other.speed and ((other.hp<other.maxhp*0.35) or other.defense<200 or other.spdef<200):
        if len(emove)>0:
            use=random.choice(emove)
        elif len(emove)>0:
            use=random.choice(resmove)
        elif len(mymove)!=0:
            use=random.choice(mymove)        
    if self.choiced is True and self.dmax is False:
        if self.choicedmove in self.moves:
            use=self.choicedmove 
#        else:
#            use="Struggle"         
    
    elif use =="None" or use==[]:
        if len(mymove)==0:
            if len(resmove)==0:
                use=random.choice(self.moves)
            else:
                use=random.choice(resmove)
        else:
            use=random.choice(mymove)
#    print("=====================")     
#        print(f"{self.name}'s AI says against {other.name}:"    )
#    print("=====================")     
#    print(f" {self.name}'s USABLE MOVES:",mymove)
#    print("EFFECTIVE MOVES:",emove)
#    if myimmunemove!=[]:
#        print(f" {self.name}'s IMMUNE MOVES on {other.name}: ",myimmunemove)
#    print("RESISTED MOVES: ",resmove)
#    print("NON RES STAB MOVES:",mystablist)
#    print("STAB AND EFFECTIVE:",superduper)
#    print("CHOICED MOVE:",self.choicedmove)
#    print("SELECTED MOVE:",use)   
#    print("=====================")             
    return use,emove,superduper,myimmunemove 

 
  
def switchAI(self,other,tr,tr2, field):
    sw=[]
    sw+=tr.pokemons
    mo=[self]
    sw=list(set(sw)-set(mo))
    phymon=[]
    spemon=[]
    effmon=[]
    spdefmon=[]
    defmon=[]
    tank=[]
    best=[]
    bestank=[]
    bestoff=[]
    killmon=[]
    for i in sw:
#    bestdeflist=["Steelix","Aggron","Tyranitar","Amoongus","Rillaboom","Blastoise","Metagross","Groudon","Eternatus","Shuckle","Stakataka","Regirock","Avalugg","Cloyster","Slowbro","Bastiodon","Defense","Toxapex","Ice Rider","Diancie","Shield","Registeel","Orthworm","Zamazenta","rigus","Probopass","Melmetal","Golisopod","Torkoal","Skarmory","Forretress","Buzzwole","Stonjourner","Turtonator","Dusknoir","Dusclops","Carracosta","Tusk","Kartana","Ferrothorn","Garganacl","Glastr","Wishiwashi","Gigalith","Uxie","Leafeon","Rhyperior","Relicanth","Lugia","Golem","Cobalion","Audino","Ting-Lu","Sandaconda","Kommo","Crustle","Gliscor","Tangrowth","Sableye","Chesnaught","Hippowdon"]
#    bestspdeflist=["Eternatus","Shuckle","Regice","Kyogre","Defense","Florges","Ho-Oh","Lugia","Goodra","Latias","Probopass","Registeel","Shield","Diancie","Zamazenta","Toxapex","Mantine","Bastiodon","Blissey","Cryogonal","Gardevoir","Wo-Chien","Wishiwashi","Dusknoir","Araquanid","Nihilego","Cursola","Hoopa","Sylveon","Umbreon","Fini","Uxie","Dusclops","Cresselia","Celesteela"]
        if i !="None":
            if other.perishturn>0:
                if i.ability in ["Arena Trap","Shadow Tag"]:
                    best.append(i)
            x=moveAI(i,other,tr,tr2,field)
            y=moveAI(other,i,tr2,tr,field)
            if len(y[0])!=0 and len(x[0])>0 and (other.maxspdef*other.spdefb)<200 and i.maxspatk>250 and i not in bestoff:
                bestoff.append(i)
            if len(y[0])!=0 and len(x[0])>0 and (other.maxdef*other.defb)<200 and i.maxatk>250 and i not in bestoff:
                bestoff.append(i)
            if len(y[0])!=0 and (other.maxatk*other.atkb)>(other.maxspatk*other.spatkb) and i.maxdef>350 and i not in defmon:
                defmon.append(i)
            if len(y[0])!=0 and (other.maxspatk*other.spatkb)>(other.maxatk*other.atkb) and i.maxspdef>350 and i not in spdefmon:
                spdefmon.append(i)
            if len(y[0])==0 and (other.maxspatk*other.spatkb)>(other.maxatk*other.atkb) and i.maxspdef>(other.maxspatk*other.spatkb) and i not in spdefmon:
                spdefmon.append(i)
            if len(y[0])==0 and (other.maxatk*other.atkb)>(other.maxspatk*other.spatkb) and i.maxdef>(other.maxatk*other.atkb) and i not in defmon:
                defmon.append(i)
            if i in bestoff and len(x[3])==0 and i.maxspeed>(other.maxspeed*other.speedb):
                best.append(i)
            if "Poison" in (i.type1,i.type2,i.teratype) and "Toxic Spikes" in i.owner.hazard:
                best.append(i)
#    print("=====================")   
#    print(f"Against {other.name}: ")
#    print("=====================")   
#    print("Special Tank:",spdefmon)
#    print("Physical Tank:",defmon)
#    print("Pure Tank:",tank)
#    print("Good Offense Choice:",bestoff)
#    print("Best Tank:",bestank)
#    print("Best Choice:",best)
#    print("=====================")   
    possible=[best,bestank,bestoff,defmon,spdefmon,tank]
    choice=random.choice(tr.pokemons)
    if len(sw)!=0:
        choice=random.choice(sw)
    if len(tr.pokemons)==1:
        choice=(tr.pokemons[0])
    if len(best)==0 and other.hp>(other.maxhp*0.3) and len(bestank)!=0:
        choice=random.choice(bestank)
    if len(bestank)==0 and len(best)==0 and len(bestoff)!=0:
        choice=random.choice(bestoff)        
    if len(best)==1:
        choice=best[0]
    if len(best)>1:
        choice=random.choice(best)                
    return choice,possible  
    
def decision (self,other,tr1,tr2,field):
    action=1      
    megastones=["Gyaradosite","Venusaurite","Charizardite X","Charizardite Y","Abomasite","Absolite","Aerodactylite","Aggronite","Alakazite","Altarianite","Amoharosite","Audinite","Banettite","Beedrillite","Blasnoisinite","Blazikenite","Camerupite","Diancite","Galladite","Garchompite","Gardevoirite","Gengarite","Glalitite","Heracronite","Houndoominite","Kangaskhanite","Latiasite","Latiosite","Lopunnite","Lucarionite","Manectite","Mawilite","Medichamite","Metagrossite","Mewtwonite X","Mewtwonite Y","Pidgeotite","Pinsirite","Sablenite","Salamencite","Sceptilite","Scizorite","Sharpedonite","Slowbronite","Steelixite","Seampertite","Tyranitarite"]
    mons=switchAI(self,other,tr1,tr2,field)[1]
    movech=moveAI(self,other,tr1,tr2,field)
    #movech2=moveAI(other,self,tr2,tr1,field)
    use=movech[0]
    immune=movech[3]
    #print(immune)
    best=mons[0]
    bestank=mons[1]
    bestoff=mons[2]
    phytank=mons[3]
    spetank=mons[4]
    
#SUFFECIENT AMOUNT OF MONS    
    if len(tr1.pokemons)>1:
#NATURAL CURE            
        if self.ability=="Natural Cure" and self.status!="Alive":
           action=2
#REGENERATOR       
        if self.ability=="Regenerator" and self.hp<=(self.maxhp/2):
            action=2    
#P1 SLOWER THAN P2        
        if self.speed<other.speed:
#BELOW 40% AND OPPO FAST PHYSICAL SWEEPER
            if self.hp<(self.maxhp*0.4) and other.maxatk>300 and len(phytank)!=0:
                action=2
#BELOW 40% AND OPPO FAST SPECIAL SWEEPER                
            if self.hp<(self.maxhp*0.4) and other.maxspatk>300 and len(spetank)!=0:
                action=2  
            if self.defb<0.667 or self.spdefb<0.667:
                action=2
        if self.speed>other.speed and self.spatkb<0.667 or  self.atkb<0.667:
            action=2      
        if self.item!="None" and "Choice" in self.item and self.choicedmove!="None" and self.choicedmove!=self.moves:
            action=2    
        if use in immune:
            action=2
        if (self.maxatk*self.atkb)>300 and (other.maxdef*other.defb)<200 and (self.maxspeed*self.speedb)>(other.maxspeed*other.speedb):
            action=1
        if (self.maxspatk*self.spatkb)>300 and (other.maxspdef*other.spdefb)<200 and (self.maxspeed*self.speedb)>(other.maxspeed*other.speedb):
            action=1
        if self.item!="None" and use in typemoves.statusmove and self.item=="Assault Vest":
            action=2
        if "Koraidon" in self.name and "Ghost" in (other.type1,other.type2,other.teratype):
            action=2
        if "Miraidon" in self.name and "Ground" in (other.type1,other.type2,other.teratype):
            action=2
        if self.ability=="Zero to Hero" and "Hero" not in self.name and ("Flip Turn" not in self.moves or other.ability in ["Water Absorb","Storm Drain","Water Compaction","Desolate Land","Dry Skin"]):
            action=2      
        if self.owner.cantera is True and (self==self.owner.pokemons[-1] or self.atk>350 or self.spatk>350 or "Tera Blast" in self.moves or self.maxiv in ["Rock","Fire","Water","Grass","Electric","Ground","Flying","Fighting","Fairy","Dragon","Steel","Poison","Dark","Ghost","Normal","Bug","Ice"]):
            action=random.choices([1,7], weights=[2,5],k=1)[0]
        if self.owner.canmax is True and ((self.item!="None" and self.item not in megastones and (self.spatk>350 or self.atk>350)) or self.maxiv=="max"):
            action=8
        if self.item in megastones and "Mega" not in self.name and tr1.canmega==True:
            action=random.choices([1,9], weights=[2,8],k=1)[0]
        if self.yawn is True and self.status=="Alive":
            action=2
        if self.perishturn==1:
            action=2
        if self.fmoveturn!=0:
            action=1
        if self.precharge==True:
            action=1
        if self.firespin!=0 or self.whirlpool!=0 or self.infestation!=0:
            action=1      
        if other.ability=="Arena Trap" and "Flying" in (self.type1,self.type2,self.teratype):
            action=1        
        if other.ability=="Magnet Pull" and "Steel" in (self.type1,self.type2,self.teratype):
            action=1                   
        if (other.ability=="Shadow Tag" or self.trap==other or self.trap==True) and "Ghost" not in (self.type1,self.type2,self.teratype):
            action=1    
        if self.precharge is True:
            action=1
        if self.olock is True:
            action=1
        if self.dmax is True:
            action=1    
        if len(self.owner.item)!=0:
            if self.hp<=self.maxhp*.2 and "Full Restore" in self.owner.item:
                action=6
    return action              