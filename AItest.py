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
    if self.dmax is False and "Ditto" not in self.name:
        mymove+=self.moves
    types=[]
    mytypes=[]
    if self.ability=="Galvanize":
        typemoves.electricmoves+=typemoves.normalmoves
    if self.ability=="Aerilate":
        typemoves.flyingmoves+=typemoves.normalmoves
    if self.ability=="Pixilate":
        typemoves.fairymoves+=typemoves.normalmoves
    if self.ability=="Liquid Voice":
        typemoves.watermoves+=typemoves.normalmoves
    if self.type2 is None:
        mytypes.append(self.type1)
    if self.type2 is not None:
        mytypes.append(self.type1)
        mytypes.append(self.type2)
    if other.type2 is None:
        types.append(other.type1)
    if other.type2 is not None:
        types.append(other.type1)
        types.append(other.type2)
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
    use=None
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
    groundimmune=["Electric"] 
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
        immunelist+=groundimmune
    if "Ghost" in types:
        stablist+=typemoves.ghostmoves
        weaklist=weaklist+ghostwk
        resistlist=resistlist+ghostres
        immunelist+=ghostimmune
    if "Normal" in types:
        stablist+=typemoves.normalmoves
        weaklist=weaklist+normalwk
        resistlist=resistlist+normalres
        immunelist+=normalimmune
    if "Dark" in types:
        stablist+=typemoves.darkmoves
        weaklist=weaklist+darkwk
        resistlist=resistlist+darkres
        immunelist+=darkimmune
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
        immunelist+=flyingimmune
    if "Fighting" in types:
        stablist+=typemoves.fightingmoves
        weaklist=weaklist+fightingwk
        resistlist=resistlist+fightingres
    if "Fairy" in types:
        stablist+=typemoves.fairymoves
        weaklist=weaklist+fairywk
        resistlist=resistlist+fairyres
        immunelist+=fairyimmune
    if "Steel" in types:
        stablist+=typemoves.steelmoves
        weaklist=weaklist+steelwk
        resistlist=resistlist+steelres
        immunelist+=steelimmune
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
    if "Water" in mytypes:
        mystablist+=typemoves.watermoves
        myweaklist=myweaklist+waterwk
        myresistlist=myresistlist+waterres
    if "Fire" in mytypes:
        mystablist+=typemoves.firemoves
        myweaklist=myweaklist+firewk
        myresistlist=myresistlist+fireres
    if "Grass" in mytypes:
        mystablist+=typemoves.grassmoves
        myweaklist=myweaklist+grasswk
        myresistlist=myresistlist+grassres
    if "Electric" in mytypes:
        mystablist+=typemoves.electricmoves
        myweaklist=myweaklist+electricwk
        myresistlist=myresistlist+electricres
    if "Rock" in mytypes:
        mystablist+=typemoves.rockmoves
        myweaklist=myweaklist+rockwk
        myresistlist=myresistlist+rockres
    if "Ground" in mytypes:
        mystablist+=typemoves.groundmoves
        myweaklist=myweaklist+groundwk
        myresistlist=myresistlist+groundres
        myimmunelist+=groundimmune
    if "Ghost" in mytypes:
        mystablist+=typemoves.ghostmoves
        myweaklist=myweaklist+ghostwk
        myresistlist=myresistlist+ghostres
        myimmunelist+=ghostimmune
    if "Normal" in mytypes:
        mystablist+=typemoves.normalmoves
        myweaklist=myweaklist+normalwk
        myresistlist=myresistlist+normalres
        myimmunelist+=normalimmune
    if "Dark" in mytypes:
        mystablist+=typemoves.darkmoves
        myweaklist=myweaklist+darkwk
        myresistlist=myresistlist+darkres
        myimmunelist+=darkimmune
    if "Psychic" in mytypes:
        mystablist+=typemoves.psychicmoves
        myweaklist=myweaklist+psychicwk
        myresistlist=myresistlist+psychicres
    if "Bug" in mytypes:
        mystablist+=typemoves.bugmoves
        myweaklist=myweaklist+bugwk
        myresistlist=myresistlist+bugres
    if "Flying" in mytypes:
        mystablist+=typemoves.flyingmoves
        myweaklist=myweaklist+flyingwk
        myresistlist=myresistlist+flyingres
        myimmunelist+=flyingimmune
    if "Fighting" in mytypes:
        mystablist+=typemoves.fightingmoves
        myweaklist=myweaklist+fightingwk
        myresistlist=myresistlist+fightingres
    if "Fairy" in mytypes:
        mystablist+=typemoves.fairymoves
        myweaklist=myweaklist+fairywk
        myresistlist=myresistlist+fairyres
        myimmunelist+=fairyimmune
    if "Steel" in mytypes:
        mystablist+=typemoves.steelmoves
        myweaklist=myweaklist+steelwk
        myresistlist=myresistlist+steelres
        myimmunelist+=steelimmune
    if "Poison" in mytypes:
        mystablist+=typemoves.poisonmoves
        myweaklist=myweaklist+poisonwk
        myresistlist=myresistlist+poisonres
    if "Ice" in mytypes:
        mystablist+=typemoves.icemoves
        myweaklist=myweaklist+icewk
        myresistlist=myresistlist+iceres
    if "Dragon" in mytypes:
        mystablist+=typemoves.dragonmoves
        myweaklist=myweaklist+dragonwk
        myresistlist=myresistlist+dragonres        
    mystablist+=("Tera Blast","Judgement","Multi-Attack")
    weaklist=list(set(weaklist)-set(resistlist)-set(immunelist))
    #IMMUNEMOVES AGAINST OPPONENT
    if "Steel" in immunelist:
        myimmunemove+=list(set(mymove).intersection (typemoves.steelmoves))
    if "Dark" in immunelist:
        myimmunemove+=list(set(mymove).intersection (typemoves.darkmoves))        
    if "Ghost" in immunelist:
        myimmunemove+=list(set(mymove).intersection (typemoves.ghostmoves))        
    if "Fairy" in immunelist:
        myimmunemove+=list(set(mymove).intersection (typemoves.fairymoves))       
    if "Normal" in immunelist:
        myimmunemove+=list(set(mymove).intersection(typemoves.normalmoves))         
    if "Flying" in immunelist:
        myimmunemove+=list(set(mymove).intersection (typemoves.flyingmoves))        
    if "Ground" in immunelist:
        myimmunemove+=list(set(mymove).intersection (typemoves.groundmoves))   
    #if "Steel" in myimmunelist:
#        myimmunemove+=list(set(mymove).intersection (typemoves.steelmoves))
#    if "Dark" in myimmunelist:
#        myimmunemove+=list(set(mymove).intersection (typemoves.darkmoves))        
#    if "Ghost" in myimmunelist:
#        myimmunemove+=list(set(mymove).intersection (typemoves.ghostmoves))        
#    if "Fairy" in myimmunelist:
#        myimmunemove+=list(set(mymove).intersection (typemoves.fairymoves))       
#    if "Normal" in myimmunelist:
#        myimmunemove+=list(set(mymove).intersection(typemoves.normalmoves))         
#    if "Flying" in myimmunelist:
#        myimmunemove+=list(set(mymove).intersection (typemoves.flyingmoves))        
#    if "Ground" in myimmunelist:
#        myimmunemove+=list(set(mymove).intersection (typemoves.groundmoves))             
    if "Water" in weaklist:
        emove+=list(set(mymove). intersection(typemoves.watermoves))
    if "Fire" in weaklist:
        emove+=list(set(mymove). intersection(typemoves.firemoves))
    if "Grass" in weaklist:
        emove+=list(set(mymove). intersection(typemoves.grassmoves))          
    if "Rock" in weaklist:
        emove+=list(set(mymove). intersection(typemoves.rockmoves))     
    if "Ground" in weaklist:
        emove+=list(set(mymove). intersection(typemoves.groundmoves)) 
    if "Electric" in weaklist:
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
    if "Poison" in weaklist:
        emove+=list(set(mymove). intersection(typemoves.poisonmoves))        
    if "Fighting" in weaklist:
        emove+=list(set(mymove). intersection(typemoves.fightingmoves))        
    if "Flying" in weaklist:
        emove+=list(set(mymove). intersection(typemoves.flyingmoves))        
    if "Bug" in weaklist:
        emove+=list(set(mymove). intersection(typemoves.bugmoves))        
    if "Psychic" in weaklist:
        emove+=list(set(mymove). intersection(typemoves.psychicmoves))       
    if "Ghost" in weaklist:
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
    #use=None
    eheal=list(set(mymove).intersection(typemoves.healingmoves))
    eprior=list(set(mymove).intersection(typemoves.priorityatkmoves))
    superduper=list(set(emove).intersection(mystablist))
    if self.item is not None and "Choice" in self.item:
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
            mymove.remove("Defog")       
    if self.choiced is True:
        mymove=list(set(mymove)-set(mymove). intersection(typemoves.statusmove))             
    if "Stealth Rock" in otr.hazard:
        if "Stealth Rock" in mymove:
            mymove.remove("Stealth Rock")
    if "Toxic Spikes" in otr.hazard:
        if "Toxic Spikes" in mymove:
            mymove.remove("Toxic Spikes")
    if other.status=="Badly Poisoned" or (other.type1 in ["Steel","Poison"] or other.type2 in ["Steel","Poison"] and self.ability!="Corrosion"):
        if "Toxic" in mymove:
            mymove.remove("Toxic")
    if other.status=="Paralyzed":
        if "Thunder Wave" in mymove:
            mymove.remove("Thunder Wave")         
    if self.spatkb==4:
        if "Tail Glow" in mymove:
            mymove.remove("Tail Glow")      
    if other.atkcat=="Physical" and self.speed<other.speed and "Counter" in self.moves:
        use="Counter"                   
    if other.atkcat=="Special" and self.speed<other.speed and "Mirror Coat" in self.moves:
        use="Mirror Coat"
    if other.seeded is True:
        if "Leech Seed" in mymove:
            mymove.remove("Leech Seed")      
    if field.weather=="Sandstorm":
        if "Sandstorm" in mymove:
            mymove.remove("Sandstorm")        
    if field.weather=="Hail":
        if "Hail" in mymove:
            mymove.remove("Hail")        
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
             
    if self.protect!=False:       
        mymove=list(set(mymove)-set(typemoves.protectmoves))  
    if other.ability in ["Water Absorb","Storm Drain"]:
        mymove=list(set(mymove)-(set(mymove).intersection(typemoves.watermoves)))
        emove=list(set(emove)-set(typemoves.watermoves))  
        mystablist=list(set(mystablist)-set(typemoves.watermoves))
    if other.ability in ["Volt Absorb","Lightning Rod"]:
        mymove=list(set(mymove)-(set(mymove).intersection(typemoves.electricmoves)))
        emove=list(set(emove)-set(typemoves.electricmoves))       
        mystablist=list(set(mystablist)-set(typemoves.electricmoves)) 
    if other.ability=="Flash Fire":       
        mymove=list(set(mymove)-(set(mymove).intersection(typemoves.firemoves)))
    if other.ability=="Levitate":
        mymove=list(set(mymove)-(set(mymove).intersection(typemoves.groundmoves)))
        emove=list(set(emove)-set(typemoves.groundmoves)) 
        mystablist=list(set(mystablist)-set(typemoves.groundmoves)) 
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
    if self.choiced is False and self.atk>self.spatk and self.atkb<=1 and self.hp>(self.maxhp*0.5) and other.hp>(other.maxhp*0.2):
        boost=list (set(mymove).intersection(typemoves.atkboost))
        if len(boost)!=0:
            use=boost[0]        
    if self.choiced is False and self.spatk>self.atk and self.spatkb<=1 and self.hp>(self.maxhp*0.5) and other.hp>(other.maxhp*0.2):
        boost=list (set(mymove).intersection(typemoves.atkboost))
        if len(boost)!=0:
            use=boost[0]   
    if self.choiced is False and other.speed>other.speed and "Tailwind" in mymove and mtr.tailwind is not True:
        use="Tailwind"                
    if self.choiced is False and other.atk>other.spatk and "Reflect" in mymove and mtr.reflect is not True:
        use="Reflect"              
    if self.choiced is False and other.spatk>other.atk and "Light Screen" in mymove and mtr.lightscreen is not True:
        use="Light Screen"        
    if self.protect is False and "King's Shield" in mymove and other.hp>=(other.maxhp*0.2):
        use="King's Shield"       
    if self.item is not None and "Sticky Web"  not in otr.hazard and "Choice" not in self.item and other.hp>=(other.maxhp*0.3):
        if "Sticky Web"  in mymove:
            use="Sticky Web"                    
    if self.item is not None and "Stealth Rock"  not in otr.hazard and "Choice" not in self.item and other.hp>=(other.maxhp*0.3):
        if "Stealth Rock"  in mymove:
            use="Stealth Rock"      
    if self.item is not None and "Toxic Spikes"  not in otr.hazard and "Choice" not in self.item and other.hp>=(other.maxhp*0.3):
        if "Toxic Spikes"  in mymove:
            use="Toxic Spikes"  
    if (other.hp<=(other.maxhp*0.20) or other.defb<0.5) and self.speed<other.speed and len(eprior)!=0:
        use=random.choice([eprior[0],emove])             
    if self.item is not None and "Choice" in self.item and self.choiced is False and use is not None and self.dmax is False:
        self.choiced=True
        self.choicedmove=use
    if self.choiced is True and self.dmax is False:
        use=self.choicedmove      
    if self.hp<=(self.maxhp*0.25) and "Destiny Bond" in mymove and self.speed>other.speed:
        use="Destiny Bond"
    if self.hp<=(self.maxhp*0.25) and "Misty Explosion" in mymove:
        use="Misty Explosion"
    if self.hp<=(self.maxhp*0.25) and "Explosion" in mymove:
        use="Explosion"
    if len(self.moves)>4:
        use=self.moves[4]
    if use is None or use==[]:
        if len(mymove)==0:
            use=random.choice(self.moves)
        else:
            use=random.choice(mymove)
#    print("=====================")     
#    print(f"{self.name}'s AI says against {other.name}:"    )
#    print("=====================")     
#    print("USABLE MOVES:",mymove)
#    print("EFFECTIVE MOVES:",emove)
#    if myimmunemove!=[]:
#        print("IMMUNE MOVES: ",myimmunemove)
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
    for i in tr.pokemons:
        x=moveAI(i,other,tr,tr2,field)
        y=moveAI(other,i,tr2,tr,field)
        #print(i,x[1],other.name)
        
        if i.defense>250 and i.spdef>250 and i!=self:
            tank.append(i)
        if i.defense>250 and i!=self:
            defmon.append(i)
        if i.spdef>250 and i!=self:
            spdefmon.append(i)
#offense
#200+ spdef          
        if 200<other.spdef:
#Has effective move and oppo doesn't and spatk 270+            
            if len(x[1])!=0 and i!=self and len(y[1])==0 and i.spatk>270:
                bestoff.append(i)
#Has effective move and oppo doesn't and atk 270+                 
        elif 200<other.defense:
            if len(x[1])!=0 and i!=self and len(y[1])==0 and i.atk>270:
                bestoff.append(i)
#Def under 200                
        if other.defense<200:
#Has effective move and oppo doesn't and atk 200+               
            if len(x[1])!=0 and i!=self and len(y[1])==0 and i.atk>200:
                bestoff.append(i)
#spdef under 200                
        elif other.spdef<200:
#Has effective move and oppo doesn't and spatk 270+               
            if len(x[1])!=0 and i!=self and len(y[1])==0 and i.spatk>200:
                bestoff.append(i)
        if len(x[1])!=0 and i!=self and len(y[1])==0 and (i.atk>200 or i.spatk>200):
            effmon.append(i)
        if other.spatk>250:
            if i.spdef>200 and i in effmon and i!=self:
                best.append(i)
        if other.atk>250:
            if i.defense>200 and i in effmon and i!=self:
                best.append(i)
        if other.spatk>other.atk and i in spdefmon and i!=self:
            bestank.append(i)
        if other.atk>other.spatk and i in defmon and i!=self:
            bestank.append(i)        
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
#NATURAL CURE    
    if self.ability=="Natural Cure" and self.status!="Alive" and len(tr1.pokemons)>1:
       action=2
#REGENERATOR       
    if self.ability=="Regenerator" and self.hp<=(self.maxhp/2) and len(tr1.pokemons)>1:
        action=2      
    mons=switchAI(self,other,tr1,tr2,field)[1]
    movech=moveAI(self,other,tr1,tr2,field)
    movech2=moveAI(other,self,tr2,tr1,field)
    use=movech[0]
    immune=movech2[3]
    best=mons[0]
    bestank=mons[1]
    bestoff=mons[2]
    phytank=mons[3]
    spetank=mons[4]
    if use==immune and len(tr1.pokemons)>1:
        action=2
#SUFFECIENT AMOUNT OF MONS    
    if len(tr1.pokemons)>1:
#P1 SLOWER THAN P2        
        if self.speed<other.speed:
#BELOW 40% AND OPPO FAST PHYSICAL SWEEPER
            if self.hp<(self.maxhp*0.4) and other.atk>300 and len(phytank)!=0 and self.defense<250:
                action=2
#BELOW 40% AND OPPO FAST SPECIAL SWEEPER                
            if self.hp<(self.maxhp*0.4) and other.spatk>300 and len(spetank)!=0 and self.spdef<250:
                action=2  
        if self.ability=="Zero to Hero" and "Hero" not in self.name:
            action=2                
        if other.ability=="Magnet Pull" and "Steel" in (self.type1,self.type2):
            action=1                   
        if other.ability=="Shadow Tag" and "Ghost" not in (self.type1,self.type2):
            action=1    
        if self.olock is True:
            action=1
        if self.dmax is True:
            action=1            
    return action              