#pylint:disable=W0613
#pylint:disable=R0913
#pylint:disable=C0116
#pylint:disable=W0401
#pylint:disable=C0301
#pylint:disable=W0622
#pylint:disable=W0621
#pylint:disable=C0103
#pylint:disable=C0303
#from attack import *
#from battle import *
from pokemonbase2 import *
from typematchup import *
from hiddenpower import *
from colorama import init
from termcolor import colored
#from rich import print
def electricterrain(self):
    print(f"{self.name} used Electric Terrain!")
    field.terrain="Electric"
    print("An electric current ran across the battlefield!")
def mistyterrain(self):
    print(f"{self.name} used Misty Terrain!")
    field.terrain="Misty"
    print("Mist swirled around the battlefield!")
def grassyterrain(self):
    print(f"{self.name} used Grassy Terrain!")
    field.terrain="Grassy"
    print("Grass grew to cover the battlefield!")   
def psychicterrain(self):
    print(f"{self.name} used Psychic Terrain!")
    field.terrain="Psychic"
    print("The battlefield got weird!")        
def trickortreat(self,other):
    self.atktype="Ghost"
    print(f"{self.name} used Trick-or-Treat!")
    other.type2=None
    other.type1="Ghost"
    print(f"{other.name} turned into {other.type1} type!")
def soak(self,other):
    self.atktype="Water"
    print(f"{self.name} used Soak!")
    other.type2=None
    other.type1="Water"    
    print(f"{other.name} turned into {other.type1} type!")
def forestscurse(self,other):
    self.atktype="Grass"
    print(f"{self.name} used Forest's Curse!")
    other.type2=None
    other.type1="Grass"    
    print(f"{other.name} turned into {other.type1} type!")
def magmastorm(self,other):
    self.atktype="Fire"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f"{self.name} used "+colored("Magma Storm","red")+".")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=special(self.level,self.spatk,other.spdef,120,a,b,c,r,al,w)
    other.hp-=dmg
    if other.status not in ["Alive","Burned"] and other.ability!="Flash Fire" and other.type1!="Fire" and other.type2!="Fire":
        other.status="Burned"
        print(f"{other.name} was burned.")
def fusionflare(self,other):
    self.atktype="Fire"
    w=weathereff(self)
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used "+colored("Fusion Flare","red")+".")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,100,a,b,c,r,al,w)        
def blueflare(self,other):
    self.atktype="Fire"
    w=weathereff(self)
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used "+colored("Blue Flare","red")+".")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,130,a,b,c,r,al,w)
    ch=random.randint(1,100)
    if ch>80 and other.status is None and self.ability!="Sheer Force":
        other.status="Burned"
        print(f"{other.name} was burned.")
def iceburn(self,other):
    self.atktype="Ice"
    w=weathereff(self)
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used "+colored("Ice Burn","cyan")+".")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,140,a,b,c,r,al,w)
    ch=random.randint(1,100)
    if ch>70 and other.status is None and self.ability!="Sheer Force":
        other.status="Burned"
        print(f"{other.name} was burned.")    

def fireBlast(self,other):
    self.atktype="Fire"
    w=weathereff(self)
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used "+colored("Fire Blast","red")+".")
    
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,110,a,b,c,r,al,w)
    ch=random.randint(1,10)
    if ch==1 and other.status is None and self.ability!="Sheer Force":
        other.status="Burned"
        print(f"{other.name} was burned.")
        other.atk=other.atk/2
def steameruption(self,other):
    self.atktype="Water"
    w=weathereff(self)
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used Steam Eruption!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,110,a,b,c,r,al,w)
    ch=random.randint(1,100)
    if ch>70 and other.status is None and self.ability!="Sheer Force" and other.status=="Alive":
        other.status="Burned"
        print(f"{other.name} was burned.")  
def pyroball(self,other):
    self.atktype="Fire"
    w=weathereff(self)
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used "+colored("Pyro Ball","red")+".")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,110,a,b,c,r,al,w)
    ch=random.randint(1,10)
    if ch==1 and other.status is None and self.ability!="Sheer Force":
        other.status="Burned"
        print(f"{other.name} was burned.")
        
def fierydance(self,other):
    self.atktype="Fire"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f"{self.name} used "+colored("Fiery Dance","red")+".")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,80,a,b,c,r,al,w)        
    ch=random.randint(1,2)
    if ch==1:
        spatkchange(self,0.5)
        print(f"Special Attack x{self.spatkb}")
def rest(self):
    print(f"{self.name} used "+colored("Rest","magenta")+".")   
    if self.status!="Sleep" and self.hp!=self.maxhp:
        self.status="Sleep"
        print(f"{self.name} fell asleep.")
        self.hp=self.maxhp
def lusterpurge(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used "+colored("Luster Purge","magenta")+".")
    self.atktype="Psychic"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al)
    ch=random.randint(1,2)
    if ch==2 and self.ability=="Sheer Force" and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        spdefchange(other,-0.5)
        print(f"{other.name}: Special Defense x"+str(other.spdefb))
def mistball(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used "+colored("Mist Ball","magenta")+".")
    self.atktype="Psychic"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al)
    ch=random.randint(1,2)
    if ch==2 and self.ability=="Sheer Force" and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        spatkchange(other,-0.5)
        print(f"{other.name}: Special Attack x"+str(other.spatkb))
def psychic(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used "+colored("Psychic","magenta")+".")
    self.atktype="Psychic"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al)
    ch=random.randint(1,10)
    if ch==7 and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        spdefchange(other,-0.5)
        print(f"{other.name}: Special Defense x"+str(other.spdefb))
def bellydrum(self):
    print(f"{self.name} used Belly Drum.")
    if self.hp>(self.maxhp/2):
        atkchange(self,4)
        self.hp-=(self.maxhp/2)
        print(f"{self.name} cuts its own HP and maximized its Attack.")
        print(f"Attack x{self.atkb}")     
    else:
        print ("It failed")    
def swordsdance(self):
    print(f"{self.name} used Swords Dance.")
    atkchange(self,1)
    print(f"Attack x{self.atkb}")
def curse(self):
    print(f"{self.name} used Curse.")
    atkchange(self,0.5)
    defchange(self,0.5)
    speedchange(self,-0.5)
    print(f"Attack x{self.atkb}")    
    print(f"Defense x{self.defb}")
    print(f"Speed x{self.speedb}")
def tailglow(self):
    print(f"{self.name} used Tail Glow.")
    spatkchange(self,1.5)
    print(f"Special Attack x{self.spatkb}")        
def nastyplot(self):
    print(f"{self.name} used Nasty Plot.")
    spatkchange(self,1)
    print(f"Special Attack x{self.spatkb}")    
def calmmind(self):
    print(f"{self.name} used Calm Mind.")
    spatkchange(self,0.5)
    spdefchange(self,0.5)
    print(f"Special Attack x{self.spatkb}")      
    print(f"Special Defense x{self.spdefb}")    
def acidarmor(self):
    print(f"{self.name} used Acid Armor.")    
    defchange(self,1)
    print(f"Defense x{self.defb}")      
def shelter(self):
    print(f"{self.name} used Shelter.")    
    defchange(self,1)
    print(f"Defense x{self.defb}")      
def irondefense(self):
    print(f"{self.name} used Iron Defense.")    
    defchange(self,1)
    print(f"Defense x{self.defb}")  
def leechseed(self,other):
    print(f"{self.name} used Leech Seed.")    
    if other.type1!="Grass" and other.type2!="Grass" and other.ability!="Magic Bounce" and other.seeded==False:
        other.seeded=True
        print(f"{other.name} was seeded.")
    elif self.type1!="Grass" and self.type2!="Grass"  and other.ability=="Magic Bounce" and self.seeded==False:
        self.seeded=True
        print(f"{self.name} was seeded.")
    else:
        print("It failed")
def strengthsap(self,other):
    print(f"{self.name} used Strength Sap.")    
    if other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        prevatk=other.atk
        atkchange(other,-0.5)
        newatk=other.atk*other.atkb
        heal=prevatk
        print(f"{other.name}: Attack x{other.atkb}")  
        if heal<=(self.maxhp-heal):
            self.hp+=heal
        else:
            self.hp=self.maxhp
    else:
        print ("It Failed!")
def defendorder(self):
    print(f"{self.name} used Defend Order.")
    spdefchange(self,0.5)     
    defchange(self,0.5)   
    print(f"Defense x{self.defb}")    
    print(f"Special Defense x{self.spdefb}")          
def bulkup(self):
    print(f"{self.name} used Bulk Up.")
    atkchange(self,0.5)     
    defchange(self,0.5)   
    print(f"Attack x{self.atkb}")   
    print(f"Defense x{self.defb}")          
def geomancy(self):
    print(f"{self.name} used Geomancy.")
    if self.item=="Power Herb":
        print(f"{self.name} became fully charged due to its Power Herb.")
        spatkchange(self,1)     
        spdefchange(self,1)   
        speedchange(self,1)
        print(f"Special Attack x{self.spatkb}")   
        print(f"Special Defense x{self.spdefb}")   
        print(f"Speed x{self.speedb}")      
        self.precharge=False
        self.item=None
    else:
        print(f"{self.name} absorbing its power.")
        self.precharge=True
def coil(self):
    print(f"{self.name} used Coil.")
    atkchange(self,0.5)     
    defchange(self,0.5)   
    print(f"Attack x{self.atkb}")   
    print(f"Defense x{self.defb}")  
def dragondance(self):
    print(f"{self.name} used Dragon Dance.")
    atkchange(self,0.5)
    speedchange(self,0.5)
    print(f"Attack x{self.atkb}")   
    print(f"Speed x{self.speedb}")
def quiverdance(self):
    print(f"{self.name} used Quiver Dance.")
    spatkchange(self,0.5)
    speedchange(self,0.5)
    spdefchange(self,0.5)
    print(f"Special Attack x{self.spatkb}")   
    print(f"Special Defense x{self.spdefb}")  
    print(f"Speed x{self.speedb}") 
              
def shellsmash(self):
    print(f"{self.name} used Shell Smash.")
    atkchange(self,1)
    spatkchange(self,1)
    speedchange(self,1)
    defchange(self,-0.5)
    spdefchange(self,-0.5)
    print(f"Attack x{self.atkb}")   
    print(f"Special Attack x{self.spatkb}")   
    print(f"Speed x{self.speedb}")       
    print(f"Defense x{self.defb}")    
    print(f"Special Defense x{self.spdefb}")        
def infernooverdrive(self,other):
    self.atktype="Fire"
    al=1
    r=randroll()
    print(f"{self.name} used Inferno Overdrive.")
    
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)   
def hydrovortex(self,other):
    self.atktype="Water"
    al=1
    r=randroll()
    print(f"{self.name} used Hydro Vortex.")
    
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)           
def bloomdoom(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Bloom Doom.")
    self.atktype="Grass"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)           
def gigavolthavoc(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used "+colored("Gigavolt Havoc","yellow")+".")
    self.atktype="Electric"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)         
def stormshards(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Splintered Stromshards.")
    self.atktype="Rock"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    field.terrain="Normal"
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)                 
def continentalcrush(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Continental Crush.")
    self.atktype="Rock"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)          
def tectonicrage(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Tectonic Rage.")
    self.atktype="Ground"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)                      
def corkscrewcrash(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Corkscrew Crash.")
    self.atktype="Steel"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)                   
def breakneckblitz(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Breakneck Blitz.")
    self.atktype="Normal"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)     
def thunderwave(self,other):
    print(f"{self.name} used Thunder Wave.")
    if other.type1!="Ground" and other.type2!="Ground" and other.type1!="Electric" and other.type2!="Electric" and other.status=="Alive" and other.ability not in ["Volt Absorb","Lightning Rod"]:
        other.status="Paralyzed"
        print(f"{other.name} is paralyzed.")
        
def sleeppowder(self,other):
    print(f"{self.name} used Sleep Powder.")
    if other.status!="Sleep" and (other.type1!="Grass" and other.type2!="Grass"):
        print(f"{other.name} fell asleep.")
        other.status="Sleep"
    else:
        print("It failed.")
def spore(self,other):
    print(f"{self.name} used "+colored("Spore","green")+".")
    if other.status!="Sleep" and (other.type1!="Grass" and other.type2!="Grass"):
        print(f"{other.name} fell asleep.")
        other.status="Sleep"
    else:
        print("It failed.")        
def hypnosis(self,other):
    print(f"{self.name} used Hypnosis.")
    if other.status!="Sleep":
        print(f"{other.name} fell asleep.")
        other.status="Sleep"
    else:
        print("It failed.")        
def darkvoid(self,other):
    print(f"{self.name} used Dark Void.")
    if other.status!="Sleep":
        print(f"{other.name} fell asleep.")
        other.status="Sleep"
    else:
        print("It failed.")             
def shatteredpsyche(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Shattered Psyche.")
    self.atktype="Psychic"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)                 
def neverendingnightmare(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Never-ending Nightmare.")
    self.atktype="Ghost"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)                 
def blackholeeclipse(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Black Hole Eclipse.")
    self.atktype="Dark"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)                 
def devastatingdrake(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Devastating Drake.")
    self.atktype="Dragon"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)      
def savagespinout(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Savage Spin-Out.")
    self.atktype="Bug"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)                   
def subzeroslammer(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Subzero Slammer.")
    self.atktype="Ice"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)                    
def twinkletackle(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Twinkle Tackle.")
    self.atktype="Fairy"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)              
def alloutpummeling(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used All-Out Pummeling.")
    self.atktype="Fighting"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)      
def aciddownpour(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Acid Downpour.")
    self.atktype="Poison"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)            
def supersonicskystrike(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Supersonic Skystrike.")
    self.atktype="Flying"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)              
def pulverizingpancake(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Pulverizing Pancake.")
    self.atktype="Normal"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)              
def trickroomm(self):
    print(f"{self.name} used Trick Room.")         
    if field.trickroom==False:
        field.trickroom=True
        print(f"{self.name} twisted the dimensions.")
    elif field.trickroom==True:
        field.trickroom=False
        print(f"{self.name} twisted the dimensions.")         
def shadowball (self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used Shadow Ball.")
    self.atktype="Ghost"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,80,a,b,c,r,al)  
    ch=random.randint(1,10)
    if ch==7 and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        spdefchange(other,-0.5)
        print(f"{other.name}: Special Defense x"+str(other.spdefb))
def judgement(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Judgement.")
    self.atktype=self.type1
    w=weathereff(self)
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,100,a,b,c,r,al)          
def multiattack(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Multi-Attack!")
    self.atktype=self.type1
    w=weathereff(self)
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,90,a,b,c,r,al)              
def seedflare (self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Seed Flare.")
    self.atktype="Grass"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,120,a,b,c,r,al)  
    ch=random.randint(1,100)
    if ch>60 and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        spdefchange(other,-1)
        print(f"{other.name}: Special Defense x"+str(other.spdefb))        
def storedpower(self,other):   
    atkx=(self.atkb-1)*2
    spatkx=(self.spatkb-1)*2
    defx=(self.defb-1)*2
    spdefx=(self.spdefb-1)*2
    speedx=(self.speedb-1)*2
    al=1
    r=randroll()
    print(f"{self.name} used Stored Power.")
    self.atktype="Ghost"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=20*(1+atkx+defx+spatkx+spdefx+speedx)
    if base<0:
        base=20
    other.hp-=special(self.level,self.spatk,other.spdef,base,a,b,c,r,al)  
def hex(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Hex.")
    self.atktype="Ghost"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=65
    if other.status!="Alive":
        base*=2
    other.hp-=special(self.level,self.spatk,other.spdef,base,a,b,c,r,al)  
    
def infernalparade(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Infernal Parade.")
    self.atktype="Ghost"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=65
    if other.status!="Alive":
        base*=2
    other.hp-=special(self.level,self.spatk,other.spdef,base,a,b,c,r,al)      
    ch=random.randint(1,100)
    if ch>70 and other.status=="Alive":
        other.status="Burned"
        print(f"{other.name} was burned.")
        
     
def energyball (self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used Energy Ball.")
    self.atktype="Grass"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,80,a,b,c,r,al)  
    ch=random.randint(1,10)
    if ch==7 and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        spdefchange(other,-0.5)
        print(f"{other.name}: Special Defense x"+str(other.spdefb))        
def bugbuzz (self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used Bug Buzz.")
    self.atktype="Bug"
    c=critch(self,other)
    if self.ability=="Punk Rock":
        al*=1.3
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al)  
    ch=random.randint(1,10)
    if ch==7 and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        spdefchange(other,-0.5)
        print(f"{other.name}: Special Defense x"+str(other.spdefb))        
def snipeshot (self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Snipe Shot.")
    self.atktype="Water"
    c=critch(self,other,2)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,80,a,b,c,r,al)                   
def signalbeam (self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Signal Beam.")
    self.atktype="Bug"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,70,a,b,c,r,al)            
def aeroblast (self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Aeroblast.")
    self.atktype="Flying"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,100,a,b,c,r,al)        
def leafstorm(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Leaf Storm.")
    self.atktype="Grass"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,130,a,b,c,r,al)           
    spatkchange(self,-1)
    print(f"Special Attack x{self.spatkb}")   
def blizzard(self,other):
    self.atktype="Ice"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f"{self.name} used Blizzard.")
    
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,110,a,b,c,r,al,w)    
    ch=random.randint(1,10)
    if ch==1 and other.status is None and self.ability!="Sheer Force":
        other.status="Frozen"
        print(f"{other.name} was frozen.")
        
def boomburst(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Boomburst.")
    self.atktype="Normal"
    c=critch(self,other)
    if self.ability=="Punk Rock":
        al*=1.3
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,140,a,b,c,r,al)        
def airslash(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Air Slash.")
    self.atktype="Flying"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,75,a,b,c,r,al)     
    chance=30
    if self.ability=="Serene Grace":
        chance*=2
    if self.speed>other.speed:
        ch=random.randint(1,100)            
        if ch>(100-chance)  and other.ability not in ["Inner Focus"]:
            other.flinched=True
def leaftornado(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used "+colored("Leaf Tornado","green")+".")
    self.atktype="Grass"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,130,a,b,c,r,al)             
       
def psystrike(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Psystrike.")
    self.atktype="Psychic"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.defense,100,a,b,c,r,al)             
def sacredfire(self,other):
    self.atktype="Fire"
    al=1
    r=randroll()
    print(f"{self.name} used Sacred Fire.")
    
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,110,a,b,c,r,al)  
def aurasphere(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Aura Sphere.")
    self.atktype="Fighting"
    c=critch(self,other)
    if self.ability=="Mega Launcher":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,80,a,b,c,r,al)      
    
def heatwave(self,other):
    self.atktype="Fire"
    al=1
    w=weathereff(self)
    r=randroll()
    print(f"{self.name} used "+colored("Heat Wave","red")+".")
    
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,95,a,b,c,r,al,w)     
def bleakwindstorm(self,other):
    al=1
    w=weathereff(self)
    r=randroll()
    print(f"{self.name} used Bleakwind Storm.")
    self.atktype="Flying"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,95,a,b,c,r,al,w)   
def springtidestorm(self,other):
    al=1
    w=weathereff(self)
    r=randroll()
    print(f"{self.name} used Springtide Storm.")
    self.atktype="Fairy"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,95,a,b,c,r,al,w)               
def sandsearstorm(self,other):
    al=1
    w=weathereff(self)
    r=randroll()
    print(f"{self.name} used Sandsear Storm.")
    self.atktype="Ground"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,95,a,b,c,r,al,w)                          
def wildboltstorm(self,other):
    al=1
    w=weathereff(self)
    r=randroll()
    print(f"{self.name} used Wildbolt Storm.")
    self.atktype="Electric"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,95,a,b,c,r,al,w)         
def morningsun(self):
    print(f"{self.name} used Morning Sun.")   
    if self.hp>=(self.maxhp/2):
        self.hp=self.maxhp
    elif self.hp==self.maxhp:
        print("Already at full HP.")
    else:
        if field.weather=="Sunny" or field.weather=="Sunny":
            self.hp+=((self.maxhp*2)/3)    
            if self.hp>self.maxhp:
                self.hp=self.maxhp
        if field.weather in ["Rainy","Hail","Sandstorm"] or field.weather in ["Rainy","Hail","Sandstorm"]:
            self.hp+=(self.maxhp/4)    
            if self.hp>self.maxhp:
                self.hp=self.maxhp
        else:    
            self.hp+=(self.maxhp/2)
            if self.hp>self.maxhp:
                self.hp=self.maxhp
def shoreup(self):
    print(f"{self.name} used Shore Up.")   
    if self.hp>=(self.maxhp/2):
        self.hp=self.maxhp
    elif self.hp==self.maxhp:
        print("Already at full HP.")
    else:
        if field.weather=="Sandstorm":
            self.hp+=((self.maxhp*2)/3)    
            if self.hp>self.maxhp:
                self.hp=self.maxhp
        else:    
            self.hp+=(self.maxhp/2)           
            if self.hp>self.maxhp:
                self.hp=self.maxhp                 
def moonlight(self):
    print(f"{self.name} used Moonlight.")   
    if self.hp>=(self.maxhp/2):
        self.hp=self.maxhp
    elif self.hp==self.maxhp:
        print("Already at full HP.")
    else:
        if field.weather=="Sunny" or field.weather=="Sunny":
            self.hp+=((self.maxhp*2)/3)    
            if self.hp>self.maxhp:
                self.hp=self.maxhp
        if field.weather in ["Rainy","Hail","Sandstorm"] or field.weather in ["Rainy","Hail","Sandstorm"]:
            self.hp+=(self.maxhp/4)    
            if self.hp>self.maxhp:
                self.hp=self.maxhp
        else:    
            self.hp+=(self.maxhp/2)           
            if self.hp>self.maxhp:
                self.hp=self.maxhp 
def synthesis(self):
    print(f"{self.name} used Synthesis.")   
    if self.hp>=(self.maxhp/2):
        self.hp=self.maxhp
    elif self.hp==self.maxhp:
        print("Already at full HP.")
    else:
        if field.weather=="Sunny" or field.weather=="Sunny":
            self.hp+=((self.maxhp*2)/3)    
            if self.hp>self.maxhp:
                self.hp=self.maxhp
        if field.weather in ["Rainy","Hail","Sandstorm"] or field.weather in ["Rainy","Hail","Sandstorm"]:
            self.hp+=(self.maxhp/4)    
            if self.hp>self.maxhp:
                self.hp=self.maxhp
        else:
            self.hp+=(self.maxhp/2)
            if self.hp>self.maxhp:
                self.hp=self.maxhp
def lunarblessing(self):
    self.atktype="Psychic"
    print(f"{self.name} used Lunar Blessing.")   
    if self.hp>=(self.maxhp/2):
        self.hp=self.maxhp
        if self.hp>self.maxhp:
                self.hp=self.maxhp
    elif self.hp==self.maxhp:
        print("Already at full HP.")
    else:
        self.hp+=(self.maxhp/2)     
        if self.hp>self.maxhp:
            self.hp=self.maxhp       
def recover(self):
    self.atktype="Normal"
    print(f"{self.name} used Recover.")   
    if self.hp>=(self.maxhp/2):
        self.hp=self.maxhp
    elif self.hp==self.maxhp:
        print("Already at full HP.")
    else:
        self.hp+=(self.maxhp/2)
        if self.hp>self.maxhp:
            self.hp=self.maxhp
def milkdrink(self):
    self.atktype="Normal"
    print(f"{self.name} used Milk Drink.")   
    if self.hp>=(self.maxhp/2):
        self.hp=self.maxhp
    elif self.hp==self.maxhp:
        print("Already at full HP.")
    else:
        self.hp+=(self.maxhp/2)
        if self.hp>self.maxhp:
            self.hp=self.maxhp            
def roost(self):
    self.atktype="Flying"
    print(f"{self.name} used Roost.")   
    if self.hp>=(self.maxhp/2):
        self.hp=self.maxhp
    elif self.hp==self.maxhp:
        print("Already at full HP.")
    else:
        self.hp+=(self.maxhp/2)        
def slackoff(self):
    self.atktype="Normal"
    print(f"{self.name} used Slack Off.")   
    if self.hp>=(self.maxhp/2):
        self.hp=self.maxhp
    elif self.hp==self.maxhp:
        print("Already at full HP.")
    else:
        self.hp+=(self.maxhp/2)             
def softboiled(self):
    self.atktype="Normal"
    print(f"{self.name} used Soft Boiled.")   
    if self.hp>=(self.maxhp/2):
        self.hp=self.maxhp
    elif self.hp==self.maxhp:
        print("Already at full HP.")
    else:
        self.hp+=(self.maxhp/2)      
def toxic(self, other):
    self.atktype="Poison"
    print(f"{self.name} used Toxic.")             
    if other.status=="Alive" and other.type1 not in ["Steel","Poison"] and other.type2 not in ["Steel","Poison"] and other.ability not in ["Immunity","Magic Bounce"]:
        other.status="Badly Poisoned"
        print(f"{other.name} was badly poisoned.")
    if other.ability in ["Magic Bounce","Synchronize"] and self.status=="Alive":
        self.status="Badly Poisoned"
        print(f"{self.name} was badly poisoned.")
    elif other.type1 in ["Steel","Poison"] or other.type2 in ["Steel","Poison"] or other.ability in ["Immunity","Magic Bounce"]:
        print("It failed.")
def willowisp(self, other):
    self.atktype="Fire"
    print(f"{self.name} used Will-O-Wisp.")             
    if other.status=="Alive" and other.type1 not in ["Fire"] and other.type2 not in ["Fire"] and other.ability not in ["Flash Fire","Magic Bounce"]:
        other.status="Burned"
        print(f"{other.name} was burned.")
        
    if other.ability in ["Magic Bounce","Synchronize"] and self.status=="Alive":
        self.status="Burned"
        print(f"{self.name} was burned.")
        
    elif other.type1 in ["Fire"] or other.type2 in ["Fire"] or other.ability in ["Flash Fire","Magic Bounce"]:
        print("It failed.")    
def healorder(self):
    print(f"{self.name} used Heal Order.")   
    if self.hp>=(self.maxhp/2):
        self.hp=self.maxhp
    elif self.hp==self.maxhp:
        print("Already at full HP.")
    else:
        self.hp+=(self.maxhp/2)                       
def tbolt(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used Thunderbolt.")
    c=critch(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al)    
def technoblast(self,other):
    al=1
    r=randroll()
    
    self.atktype="Normal"
    if self.item=="Burn Drive":
        self.atktype="Fire"
        print(f"{self.name}'s {self.item} mad Techno Blast {self.atktype}!")
    if self.item=="Chill Drive":
        self.atktype="Ice"
        print(f"{self.name}'s {self.item} mad Techno Blast {self.atktype}!")
    if self.item=="Douse Drive":
        self.atktype="Water"
        print(f"{self.name}'s {self.item} mad Techno Blast {self.atktype}!")
    if self.item=="Shock Drive":
        self.atktype="Electric"
        print(f"{self.name}'s {self.item} mad Techno Blast {self.atktype}!")
    print(f"{self.name} used Techno Blast({self.atktype})!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,120,a,b,c,r,al)            
def focusblast(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used Focus Blast.")
    c=critch(self,other)
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,120,a,b,c,r,al)        
    ch=random.randint(1,10)
    if ch==7 and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        spdefchange(other,-0.5)
        print(f"{other.name}: Special Defense x"+str(other.spdefb))
def thunder(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used Thunder.")
    c=critch(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,110,a,b,c,r,al)   
def finalgambit(self,other):
    print(f"{self.name} used Final Gambit.")        
    other.hp-=self.hp
    self.hp-=self.hp
def venoshock(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Venoshock.")
    c=critch(self,other)
    self.atktype="Poison"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=65
    if other.status in ["Poisoned","Badly Poisoned"]:
        base*=2
    other.hp-=special(self.level,self.spatk,other.spdef,base,a,b,c,r,al)     
def fishiousrend(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used "+colored("Fishious Rend","blue")+".")
    c=critch(self,other)
    self.atktype="Water"
    w=weathereff(self)
    if self.ability=="Strong Jaw":
        print(f"{self.name}'s {self.ability}!")
        al=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=85
    if self.speed>other.speed:
        base*=2
    other.hp-=physical(self.level,self.atk,other.defense,base,a,b,c,r,al,w)          
def boltbeak(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used "+colored("Bolt Beak","yellow")+".")
    c=critch(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=85
    if self.speed>other.speed:
        base*=2
    other.hp-=physical(self.level,self.atk,other.defense,base,a,b,c,r,al)              
def electroball(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used "+colored("Ellectro Ball","yellow")+".")
    c=critch(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=30*(self.speed/other.speed)
    if base<30:
        base=30
    other.hp-=special(self.level,self.spatk,other.spdef,base,a,b,c,r,al)              
def electroweb(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used "+colored("Electroweb","yellow")+".")
    c=critch(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=65
    other.hp-=special(self.level,self.spatk,other.spdef,base,a,b,c,r,al)        
    if other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        speedchange(other,-0.5)
        print(f"{other.name}: Speed x{other.speedb}")
def powergem(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Power Gem.")
    c=critch(self,other)
    self.atktype="Rock"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,80,a,b,c,r,al)            
def zapcannon(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used "+colored("Zap Cannon","yellow")+".")
    c=critch(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al)            
    if other.status=="Alive" and self.ability!="Sheer Force":
        other.status="Paralyzed"
        print(f"{other.name} is paralyzed.")
def freezedry(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used Freeze-Dry.")
    c=critch(self,other)
    self.atktype="Ice"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if other.type1=="Water" or other.type2=="Water":
        if a==1:
            a*=2
            print("It's super effective!")
        if a!=1:
            a*=2
    other.hp-=special(self.level,self.spatk,other.spdef,70,a,b,c,r,al) 
def shellsidearm(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used Poison Jab.")
    c=critch(self,other)
    self.atktype="Poison"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if other.spdef>other.defense:
        other.hp-=physical(self.level,self.atk,other.defense,90,a,b,c,r,al)
    if other.defense>other.spdef: 
        other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al)
    ch=random.randint(1,100)
    if ch>80 and other.status=="Alive" and other.type1 not in ["Steel","Poison"] and other.type2 not in ["Steel","Poison"] and other.ability not in ["Immunity","Magic Bounce"]:
        other.status="Badly Poisoned"
        print(f"{other.name} was badly poisoned.")                   
def poisonjab(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used Poison Jab.")
    c=critch(self,other)
    self.atktype="Poison"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,90,a,b,c,r,al) 
    ch=random.randint(1,100)
    if ch>70 and other.status=="Alive" and other.type1 not in ["Steel","Poison"] and other.type2 not in ["Steel","Poison"] and other.ability not in ["Immunity","Magic Bounce"]:
        other.status="Badly Poisoned"
        print(f"{other.name} was badly poisoned.")
def drillpeck(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used "+colored("Drill Peck","white")+".")
    c=critch(self,other,2)
    self.atktype="Flying"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,80,a,b,c,r,al)        
def leafblade(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used "+colored("Leaf Blade","green")+".")
    c=critch(self,other,2)
    self.atktype="Grass"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,90,a,b,c,r,al)    
def triplearrows(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Triple Arrows!")
    c=critch(self,other,4)
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,40,a,b,c,r,al)        
def razorleaf(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used "+colored("Razor Leaf","green")+".")
    c=critch(self,other,2)
    self.atktype="Grass"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    other.hp-=physical(self.level,self.atk,other.defense,70,a,b,c,r,al)        
def gyroball(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Gyro Ball.")
    c=critch(self,other)
    self.atktype="Steel"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=round(1+25*(other.speed/self.speed))
    other.hp-=physical(self.level,self.atk,other.defense,base,a,b,c,r,al)   
def overdrive(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used "+colored("Overdrive","yellow")+".")
    c=critch(self,other)
    if self.ability=="Punk Rock":
        al*=1.3
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=special (self.level,self.spatk,other.spdef,80,a,b,c,r,al)         
def discharge(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used "+colored("Disharge","yellow")+".")
    c=critch(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=special (self.level,self.spatk,other.spdef,80,a,b,c,r,al) 
    other.hp-=dmg    
    ch=random.randint(1,100)
    if ch>70 and other.status=="Alive":
        other.status="Paralyzed"
        print(f"{other.name} is paralyzed.")
       
def wildcharge(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used "+colored("Wild Charge","yellow")+".")
    c=critch(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,90,a,b,c,r,al) 
    if dmg>other.hp:
        dmg=other.hp
        other.hp=0
    else:
        other.hp-=dmg
    if self.ability!="Rock Head":
        self.hp-=round(dmg/4)
        print(f"{self.name} was hurt by recoil.")         
def accelerock(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Accelerock.")
    c=critch(self,other)
    self.atktype="Rock"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,40,a,b,c,r,al)     
def sacredsword(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Sacred Sword.")
    c=critch(self,other)
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.maxdef,90,a,b,c,r,al)         
def throatchop(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Throat Chop.")
    c=critch(self,other)
    self.atktype="Dark"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,80,a,b,c,r,al)           
def darkestlariat(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Darkest Lariat.")
    c=critch(self,other)
    self.atktype="Dark"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.maxdef,85,a,b,c,r,al)       
def acrobatics(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Acrobatics.")
    c=critch(self,other)
    self.atktype="Flying"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=55
    if self.item==None:
        base*=2
    other.hp-=physical(self.level,self.atk,other.defense,base,a,b,c,r,al)     
def aurawheel(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Aura Wheel.")
    c=critch(self,other)
    self.atktype="Electricb"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,110,a,b,c,r,al)            
def barbbarrage(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Barb Barrage.")
    c=critch(self,other)
    self.atktype="Poison"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=60
    if other.status!="Alive":
        base=120
    other.hp-=physical(self.level,self.atk,other.defense,base,a,b,c,r,al)         
def beakblast(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Beak Blast.")
    c=critch(self,other)
    self.atktype="Flying"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,100,a,b,c,r,al)     
def partingshot(self,other):
    print(f"{self.name} used Parting Shot.")        
    if other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        atkchange(other,-0.5)
        spatkchange (other,-0.5)
        print(f"{other.name}: Attack x{other.atkb}")
        print(f"{other.name}: Special Attack x{other.spatkb}")
    else:
        print(f"Can't lower {other.name}'s stats!")
def bonerush(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Bone Rush.")
    c=critch(self,other)
    self.atktype="Ground"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,125,a,b,c,r,al)  
def explosion(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Explosion.")
    c=critch(self,other)
    self.atktype="Normal"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,250,a,b,c,r,al)         
    self.hp=0     
def snarl(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Snarl.")
    c=critch(self,other)
    self.atktype="Dark"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,55,a,b,c,r,al)           
    if other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        spatkchange (other,-0.5) 
        print(f"{other.name}: Special Attack x{other.spatkb}")
    else:
        print("Nothing happened!")
def steelbeam(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Steel Beam.")
    c=critch(self,other)
    self.atktype="Steel"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,140,a,b,c,r,al)               
def aquajet(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Aqua Jet.")
    c=critch(self,other)
    self.atktype="Water"
    w=weathereff(self)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,40,a,b,c,r,al,w)                  
def armthrust(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Arm Thrust.")
    c=critch(self,other)
    self.atktype="Fighting"
    base=15
    if self.ability=="Technician":
        print(f"{self.name}'s {self.ability}.")
        base*=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,base,a,b,c,r,al)    
def psyshield(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Psyshield Bash.")
    c=critch(self,other)
    self.atktype="Psychic"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,70,a,b,c,r,al)  
    ch=random.randint(1,100)
    if ch>90:
        defchange(self,0.5)
        print("Defense x"+str(self.defb))    
def steelwing(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Steel Wing.")
    c=critch(self,other)
    self.atktype="Steel"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,70,a,b,c,r,al)  
    ch=random.randint(1,10)
    if ch==7:
        defchange(self,0.5)
        print("Defense x"+str(self.defb))
def heatcrash(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used "+colored("Heat Crash","red")+".")
    c=critch(self,other)
    self.atktype="Fire"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=80
    if self.defense>self.spdef:
        base*=(self.defense/other.defense)
    if self.spdef>self.defense:
        base*=(self.spdef/other.spdef)
    other.hp-=physical(self.level,self.atk,other.defense,base,a,b,c,r,al)         
def grassknot(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Grass Knot.")
    c=critch(self,other)
    self.atktype="Grass"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=80
    if self.defense<self.spdef:
        base*=(other.defense/self.defense)
    if self.spdef<self.defense:
        base*=(other.spdef/self.spdef)
    other.hp-=physical(self.level,self.atk,other.defense,base,a,b,c,r,al)             
def heavyslam(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Heavy Slam.")
    c=critch(self,other)
    self.atktype="Steel"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=80
    if self.defense>self.spdef:
        base*=(self.defense/other.defense)
    if self.spdef>self.defense:
        base*=(self.spdef/other.spdef)
    other.hp-=physical(self.level,self.atk,other.defense,base,a,b,c,r,al)          
def assurance(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Assurance.")
    c=critch(self,other)
    self.atktype="Dark"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=60
    if self.speed<other.speed:
        base=120
    other.hp-=physical(self.level,self.atk,other.defense,base,a,b,c,r,al)                   
def attackorder(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Attack Order.")
    c=critch(self,other,2)
    self.atktype="Bug"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,90,a,b,c,r,al)             
def facade(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Facade.")
    c=critch(self,other)
    self.atktype="Normal"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=70
    if self.status!="Alive":
        base*=2
    other.hp-=physical(self.level,self.atk,other.defense,base,a,b,c,r,al)                 
def retrn(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Return!")
    c=critch(self,other)
    self.atktype="Normal"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=round(self.happiness*(2/5))
    other.hp-=physical(self.level,self.atk,other.defense,base,a,b,c,r,al)
def bodypress(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Body Press")
    c=critch(self,other)
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.defense,other.defense,80,a,b,c,r,al)    
    
def stoneedge(self,other):
    al=1
    r=randroll()
    
    print(f"{self.name} used Stone Edge.")
    c=critch(self,other,2)
    self.atktype="Rock"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,90,a,b,c,r,al)   
def petaldance(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used "+colored("Petal Dance","green")+".")
    c=critch(self,other,2)
    self.atktype="Grass"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,90,a,b,c,r,al)       
def ragingfury(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used "+colored("Raging Fury","red")+".")
    c=critch(self,other,2)
    self.atktype="Fire"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,90,a,b,c,r,al)   
def outrage(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Outrage.")
    c=critch(self,other,2)
    self.atktype="Dragon"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,90,a,b,c,r,al)          
def icefang(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used Ice Fang.")
    c=critch(self,other)
    self.atktype="Ice"
    if self.ability=="Strong Jaw":
        print(f"{self.name}'s {self.ability}!")
        al=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,90,a,b,c,r,al)       
    ch=random.randint(1,100)
    if ch>90 and self.ability!="Sheer Force":
       other.status="Frozen"
       print(f"{other.name} was frozen.")
def rockslide(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used Rock Slide.")
    c=critch(self,other)
    self.atktype="Rock"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,85,a,b,c,r,al)   
def waterfall(self,other):
    self.atktype="Water"
    al=1
    w=weathereff(self)
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used "+colored("Waterfall","blue")+".")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,85,a,b,c,r,al,w)       
    ch=random.randint(1,100)
    if ch>80  and other.ability not in ["Inner Focus"]:
        other.flinched=True        
def crosspoison(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used Cross Poison.")
    c=critch(self,other)
    self.atktype="Poison"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,90,a,b,c,r,al)           
    ch=random.randint(1,100)
    if ch>90 and other.status=="Alive" and other.type1 not in ["Steel","Poison"] and other.type2 not in ["Steel","Poison"] and other.ability not in ["Immunity","Magic Bounce"]:
        other.status="Badly Poisoned"
        print(f"{other.name} was badly poisoned.")
def rockblast(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Rock Blast.")
    c=critch(self,other)
    self.atktype="Rock"
    base=25
    if self.ability=="Technician":
        print(f"{self.name}'s {self.ability}.")
        base*=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,base,a,b,c,r,al)         
def skyuppercut(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Sky Uppercut.")
    c=critch(self,other)
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,70,a,b,c,r,al)         
def shadowforce(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Shadow Force.")
    c=critch(self,other)
    self.atktype="Ghost"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,120,a,b,c,r,al)              
    ch=random.randint(1,100)
    if ch>70 and self.ability!="Sheer Force" and other.ability not in ["Inner Focus"]:
        other.flinched=True  
def phantomforce(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Phantom Force.")
    c=critch(self,other)
    self.atktype="Ghost"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,90,a,b,c,r,al)                      
def blazekick(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Blaze Kick.")
    c=critch(self,other)
    self.atktype="Fire"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,85,a,b,c,r,al)             
def hijumpkick(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used High Jump Kick.")
    c=critch(self,other)
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    miss=random.randint(1,100)
    if miss>90:
        dmg=physical(self.level,self.atk,other.defense,130,a,b,c,r,al)
        sdmg=dmg/2
        if sdmg>(self.maxhp/2):
            sdmg=self.maxhp/2
        print(f"{other.name} avoided the attack.")
        self.hp-=sdmg
    elif miss<=90:
         dmg=physical(self.level,self.atk,other.defense,130,a,b,c,r,al)
         other.hp-=physical(self.level,self.atk,other.defense,130,a,b,c,r,al)             
def foulplay(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Foul Play.")
    c=critch(self,other)
    self.atktype="Dark"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,other.atk,other.defense,80,a,b,c,r,al)      
def iciclespears(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used "+colored("Icicle Spear","cyan")+".")
    c=critch(self,other)
    self.atktype="Ice"
    base=25
    if self.ability=="Technician":
        print(f"{self.name}'s {self.ability}.")
        base*=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,base,a,b,c,r,al)       
def pinmissile (self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Pin Missile.")
    c=critch(self,other)
    self.atktype="Bug"
    base=25
    if self.ability=="Technician":
        print(f"{self.name}'s {self.ability}.")
        base*=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,base,a,b,c,r,al)   
def bulletseed(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Bullet Seed.")
    c=critch(self,other)
    self.atktype="Grass"
    base=25
    if self.ability=="Technician":
        print(f"{self.name}'s {self.ability}.")
        base*=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,base,a,b,c,r,al)       
def watershuriken(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Water Shuriken.")
    c=critch(self,other)
    self.atktype="Water"
    base=15
    if self.ability=="Battle Bond":
        print(f"{self.name}'s {self.ability}.")
        base*=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,base,a,b,c,r,al)           
def brickbreak(self,other,optr):
    al=1
    r=randroll()
    print(f"{self.name} used Brick Break.")
    c=critch(self,other)
    self.atktype="Fighting"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,70,a,b,c,r,al)       
    self.atk=self.maxatk*self.atkb
    self.spatk=self.maxspatk*self.spatkb
    if optr.lightscreen==True:
        optr.lightscreen=False
        print(f"{self.name} broke the Light Screen.")
    if optr.reflect==True:
        optr.reflect=False
        print(f"{self.name} broke the Reflect.")
def megahorn(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Megahorn!")
    c=critch(self,other)
    self.atktype="Bug"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,120,a,b,c,r,al)           
def icebeam(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used  "+colored("Ice Beam","cyan")+".")
    c=critch(self,other)
    self.atktype="Ice"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al)
    ch=random.randint(1,10)
    if ch==7 and other.status=="Alive":
        other.status="Frozen"
        print(f"{other.name} was frozen.")
def frostbreath(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Frost Breath.")
    c=critch(self,other,16)
    self.atktype="Ice"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,65,a,b,c,r,al)    
def darkpulse(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used Dark Pulse.")
    c=critch(self,other)
    self.atktype="Dark"
    if self.ability=="Mega Launcher":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al)  
    ch=random.randint(1,100)
    if ch>80 and self.ability!="Sheer Force" and other.ability not in ["Inner Focus"]:
        other.flinched=True
def extrasensory (self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used Extrasensory.")
    c=critch(self,other)
    self.atktype="Psychic"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al)  
    ch=random.randint(1,100)
    if ch>90 and self.ability!="Sheer Force" and other.ability not in ["Inner Focus"]:
        other.flinched=True
def nightdaze(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used Night Daze.")
    c=critch(self,other)
    self.atktype="Dark"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,95,a,b,c,r,al)  
def bittermalice(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used Bitter Malice.")
    c=critch(self,other)
    self.atktype="Ghost"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=65
    if other.status!="Alive":
        base*=2
    other.hp-=special(self.level,self.spatk,other.spdef,base,a,b,c,r,al)  
    ch=random.randint(1,100)
    if ch>70 and other.status=="Alive":
        other.status="Frostbite"
        print(f"{other.name} got frostbite.")
      
def hyperbeam(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Hyper Beam.")
    c=critch(self,other)
    self.atktype="Normal"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al)
def hypervoice(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Hyper Voice!")
    c=critch(self,other)
    self.atktype="Normal"
    if self.ability=="Punk Rock":
        al*=1.3
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al)    
def roaroftime(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Roar of Time.")
    c=critch(self,other)
    self.atktype="Dragon"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
def gigaimpact(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Giga Impact.")
    c=critch(self,other)
    self.atktype="Normal"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,150,a,b,c,r,al)             
def dragonpulse(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Dragon Pulse.")
    c=critch(self,other)
    self.atktype="Dragon"
    if self.ability=="Mega Launcher":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al)   
def spacialrend(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Spacial Rend.")
    c=critch(self,other,2)
    self.atktype="Dragon"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,100,a,b,c,r,al)       
def dazzlinggleam(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Dazzling Gleam.")
    c=critch(self,other)
    self.atktype="Fairy"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al)  
def lavaplume(self,other):
    self.atktype="Fire"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f"{self.name} used Lava Plume.")
    c=critch(self,other)
    
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al,w)       
    ch=random.randint(1,100)
    if ch>70 and other.type1!="Fire" and other.type2!="Fire" and other.ability!="Flash Fire" and other.status=="Alive":
        print(f"{other.name} was burned.")
        other.status="Burned"
      
def hurricane (self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Hurricane.")
    c=critch(self,other)
    self.atktype="Flying"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,110,a,b,c,r,al)          
def inferno(self,other):
    self.atktype="Fire"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f"{self.name} used Inferno.")
    c=critch(self,other)
    
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al,w)
    if other.type1!="Fire" and other.type2!="Fire" and other.ability!="Flash Fire"     and other.status=="Alive"    :
        other.status="Burned"
        print(f"{other.name} was burned.")
        
def overheat(self,other):
    self.atktype="Fire"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f"{self.name} used Overheat.")
    c=critch(self,other)
    
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,130,a,b,c,r,al,w)                
    spatkchange (self,-1)
    print(f"Special Attack x{self.spatkb}")
def blastburn(self,other):
    self.atktype="Fire"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f"{self.name} used Blast Burn.")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al,w)  
def frenzyplant(self,other):
    self.atktype="Grass"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f"{self.name} used Frenzy Plant.")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al,w)         
def hydrocannon(self,other):
    self.atktype="Water"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f"{self.name} used Hydro Cannon.")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al,w)      
def sparklingaria(self,other):
    self.atktype="Water"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f"{self.name} used Sparkling Aria!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al,w)           
    if other.status=="Burned":
        other.status="Alive"
        
def eruption (self,other):
    self.atktype="Fire"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f"{self.name} used Eruption.")
    c=critch(self,other)
    
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=round(150*(self.hp/self.maxhp))
    other.hp-=special(self.level,self.spatk,other.spdef,base,a,b,c,r,al,w)
def dragonenergy (self,other):
    self.atktype="Dragon"
    al=1
    w=weathereff(self)
    r=randroll()
    print(f"{self.name} used Dragon Energy.")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=round(150*(self.hp/self.maxhp))
    other.hp-=special(self.level,self.spatk,other.spdef,base,a,b,c,r,al,w)        
def waterspout (self,other):
    self.atktype="Water"
    al=1
    w=weathereff(self)
    r=randroll()
    print(f"{self.name} used Water Spout.")
    c=critch(self,other)
    
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=round(150*(self.hp/self.maxhp))
    other.hp-=special(self.level,self.spatk,other.spdef,base,a,b,c,r,al,w)    
def crushgrip (self,other):
    self.atktype="Normal"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f"{self.name} used Crush Grip.")
    c=critch(self,other)
    
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=round(1+120*(self.hp/self.maxhp))
    other.hp-=physical(self.level,self.atk,other.defense,base,a,b,c,r,al)    
def moonblast(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used Moonblast.")
    c=critch(self,other)
    self.atktype="Fairy"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al)       
    ch=random.randint(1,100)
    if ch>70 and self.ability!="Sheer Force" and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        spatkchange (other,-0.5)
        print(f"{other.name}: Special Attack x{other.spatkb}")
def sludgebomb(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used Sludge Bomb.")
    c=critch(self,other)
    self.atktype="Poison"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al)                
    ch=random.randint(1,100)
    if ch>90 and other.status=="Alive" and other.type1!="Steel" and other.type2!="Steel" and other.type1!="Poison" and other.type2!="Poison" and other.ability!="Immunity":
        other.status="Badly Poisoned"
def sludgewave(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used Sludge Wave.")
    c=critch(self,other)
    self.atktype="Poison"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,95,a,b,c,r,al)                
    ch=random.randint(1,100)
    if ch>90 and other.status=="Alive" and other.type1!="Steel" and other.type2!="Steel" and other.type1!="Poison" and other.type2!="Poison" and other.ability!="Immunity":
        other.status="Badly Poisoned"        
def hydropump(self,other):
    w=weathereff(self)
    al=1
    r=randroll()
    print(f"{self.name} used Hydro Pump.")
    self.atktype="Water"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,110,a,b,c,r,al,w)  
def hydrocannon(self,other):
    self.atktype="Water"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f"{self.name} used Hydro Cannon.")
    
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al,w)      
def earthpower(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used Earth Power.")
    c=critch(self,other)
    self.atktype="Ground"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al)
    ch=random.randint(1,100)
    if ch>90 and self.ability!="Sheer Force" and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        spdefchange (other,-0.5)
        print(f"{other.name}: Special Defense x{other.spdefb}")
def stompingtantrum(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Stomping Tantrum.")
    c=critch(self,other)
    self.atktype="Ground"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=75
    if self.speed<other.speed:
        base*=1.5
    other.hp-=physical (self.level,self.atk,other.defense,base,a,b,c,r,al)        
#Bulldoze
def bulldoze (self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Bulldoze.")
    c=critch(self,other)
    self.atktype="Ground"
    if field.terrain=="Grassy":
        print("Bulldozes damage was reduced by Grassy Terrain!")
        al*=0.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,60,a,b,c,r,al)    
    speedchange(other,-0.5)
    print(f"{other.name}: Speed x{other.speedb}")
#Magnitude     
def magnitude(self,other):
    al=1
    r=randroll()
    mag=random.choices([4,5,6,7,8,9,10],weights=[5,10,20,30,20,10,5],k=1)[0]
    print(f"{self.name} used Magnitude {mag}.")
    c=critch(self,other)
    self.atktype="Ground"
    if field.terrain=="Grassy":
        print("Magnitudes damage was reduced by Grassy Terrain!")
        al*=0.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    if mag<10:
        base=10+(20*mag-4)   
    if mag==10:
        base=150
    other.hp-=physical (self.level,self.atk,other.defense,base,a,b,c,r,al)    
#EARTHQUAKE        
def earthquake (self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Earthquake.")
    c=critch(self,other)
    self.atktype="Ground"
    if field.terrain=="Grassy":
        print("Earthquakes damage was reduced by Grassy Terrain!")
        al*=0.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,100,a,b,c,r,al)
def landswrath(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Land's Wrath!")
    c=critch(self,other)
    self.atktype="Ground"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,90,a,b,c,r,al)    
def thousandwaves(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Thousand Waves!")
    c=critch(self,other)
    self.atktype="Ground"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,90,a,b,c,r,al)        
def thousandarrows(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Thousand Arrows!")
    c=critch(self,other)
    self.atktype="Ground"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,90,a,b,c,r,al)        
def coreenforcer(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Core Enforcer!")
    c=critch(self,other)
    self.atktype="Dragon"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,100,a,b,c,r,al)        
def highhorsepower(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used High Horsepower.")
    c=critch(self,other)
    self.atktype="Ground"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,95,a,b,c,r,al)
def headlongrush (self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Headlong Rush.")
    c=critch(self,other)
    self.atktype="Ground"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,100,a,b,c,r,al)    
    if self.ability!="Rock Head":
        defchange (self,-0.5)
        print(f"Defense x{self.defb}")
        spdefchange (self,-0.5)
        print(f"Special Defense x{self.spdefb}")
def firelash(self,other):
    self.atktype="Fire"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f"{self.name} used Fire Lash.")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al,w)    
    if other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        defchange (other,-0.5)
        print(f"{other.name}: Defense x{other.defb}")
def mysticalfire(self,other):
    self.atktype="Fire"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f"{self.name} used Mystical Fire!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,70,a,b,c,r,al,w)    
    if other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        spatkchange (other,-0.5)
        print(f"{other.name}: Special Attack x{other.spatkb}")    
def liquidation (self,other):
    self.atktype="Water"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f"{self.name} used Liquidation.")
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al,w)    
    ch=random.randint(1,100)
    if ch>80 and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        defchange (other,-0.5)
        print(f"{other.name}: Defense x{other.defb}")
def razorshell(self,other):
    self.atktype="Water"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f"{self.name} used Razor Shell.")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,75,a,b,c,r,al,w)    
    ch=random.randint(1,100)
    if ch>50 and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        defchange (other,-0.5)
        print(f"{other.name}: Defense x{other.defb}") 
def diamondstorm(self,other):
    self.atktype="Rock"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f"{self.name} used Diamond Storm!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,100,a,b,c,r,al,w)    
    ch=random.randint(1,100)
    if ch>50 and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        defchange (other,-0.5)
        print(f"{other.name}: Defense x{other.defb}")                
def wavecrash(self,other):
    self.atktype="Water"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f"{self.name} used Wave Crash.")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,80,a,b,c,r,al,w)    
    other.hp-=dmg
    self.hp-=dmg/4
    print(f"{self.name} was hurt by recoil.")
    speedchange (self,0.5)
    print(f"Speed x{self.speedb}")
    
def dynapunch(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Dynamic Punch.")
    c=critch(self,other)
    self.atktype="Fighting"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    if self.ability=="Iron Fist":
        print(f"{self.name}'s {self.ability}!")
        al=1.2
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,100,a,b,c,r,al)      
def armorcannon(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Armor Cannon.")
    c=critch(self,other)
    self.atktype="Fire"
    w=weathereff(self)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,120,a,b,c,r,al,w)       
    if a!=0:
        defchange(self,-0.5)
        spdefchange(self,-0.5)
        print(f"Defense x{self.defb}")
        print(f"Special Defense x{self.spdefb}")    
def closecombat(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Close Combat.")
    c=critch(self,other)
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,120,a,b,c,r,al)       
    if a!=0:
        defchange(self,-0.5)
        spdefchange(self,-0.5)
        print(f"Defense x{self.defb}")
        print(f"Special Defense x{self.spdefb}")
def bulletpunch(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Bullet Punch.")
    c=critch(self,other)
    self.atktype="Steel"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    if self.ability=="Iron Fist":
        print(f"{self.name}'s {self.ability}!")
        al=1.2
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    base=40
    if self.ability=="Technician":
        print(f"{self.name}'s {self.ability}.")
        base*=1.5
    other.hp-=physical (self.level,self.atk,other.defense,base,a,b,c,r,al)        
def shadowsneak(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Shadow Sneak.")
    c=critch(self,other)
    self.atktype="Ghost"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    base=40
    if self.ability=="Technician":
        print(f"{self.name}'s {self.ability}.")
        base*=1.5
    other.hp-=physical (self.level,self.atk,other.defense,base,a,b,c,r,al)            
def voltswitch(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Volt Switch.")
    c=critch(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,70,a,b,c,r,al)       
def flipturn(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Flip Turn.")
    c=critch(self,other)
    self.atktype="Water"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,70,a,b,c,r,al)         
def uturn(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used U-Turn.")
    c=critch(self,other)
    self.atktype="Bug"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,70,a,b,c,r,al)               
def xscissor (self,other):
    al=1
    r=randroll()
    print(f"{self.name} used X-Scissor.")
    c=critch(self,other)
    self.atktype="Bug"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,90,a,b,c,r,al)           
def superpower(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Superpower.")
    c=critch(self,other)
    self.atktype="Fighting"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,120,a,b,c,r,al)   
    if a!=0:
        defchange(self,-0.5)
        atkchange(self,-0.5)
        print(f"Attack x{self.atkb}")
        print(f"Defense x{self.defb}")
    
def dragonhammer(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Dragon Hammer.")
    c=critch(self,other)
    self.atktype="Dragon"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,120,a,b,c,r,al)        
def lightscreen(self,tr1,turn):    
    print(f"{self.name} used Light Screen.")
    if tr1.lightscreen is True:
        print("It failed!")
    if tr1.lightscreen is False:
        tr1.lightscreen=True
        print("Light Screen raised your team's Special Defense!")
        tr1.lsturn=turn
        tr1.lightscreenend(self)
def reflect(self,tr1,turn):    
    print(f"{self.name} used Reflect.")
    if tr1.reflect is True:
        print("It failed!")
    if tr1.reflect is False:
        tr1.reflecturn=turn
        tr1.reflectend(self)
        tr1.reflect=True  
        print("Reflect raised your team's Defense!")
def zenheadbutt(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Zen Headbutt.")
    c=critch(self,other)
    self.atktype="Psychic"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)  
    ch=random.randint(1,100)
    if ch>80 and other.ability not in ["Inner Focus"]:
        other.flinched=True
def iciclecrash(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Icicle Crash.")
    c=critch(self,other)
    self.atktype="Ice"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,85,a,b,c,r,al)  
    ch=random.randint(1,100)
    if ch>70 and other.ability not in ["Inner Focus"]:
        other.flinched=True
def firepunch(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Fire Punch.")
    c=critch(self,other)
    self.atktype="Fire"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    if self.ability=="Iron Fist":
        print(f"{self.name}'s {self.ability}!")
        al=1.2
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,75,a,b,c,r,al)      
    ch=random.randint(1,100)
    if ch>90 and other.status=="Alive":
        other.status="Burned"
       
def spiritshackle(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Spirit Shackle.")
    c=critch(self,other)
    self.atktype="Ghost"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)           
    ch=random.randint(1,100)
    if ch>80 and other.ability not in ["Inner Focus"]:
        other.flinched=True   
def firefang(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Fire Fang.")
    c=critch(self,other)
    self.atktype="Fire"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    if self.ability=="Strong Jaw":
        print(f"{self.name}'s {self.ability}!")
        al=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,70,a,b,c,r,al)      
    ch=random.randint(1,100)
    if ch>90 and other.status=="Alive":
        other.status="Burned"
      
    ch=random.randint(1,100)
    if ch>90 and other.ability not in ["Inner Focus"]:
        other.flinched=True
def volttackle(self,other):
    self.atktype="Electric"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    w=weathereff(self)
    al=1
    r=randroll()
    print(f"{self.name} used "+colored("Volt Tackle","red")+"!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical(self.level,self.atk,other.defense,120,a,b,c,r,al,w)
    if dmg>other.hp:
        dmg=other.hp
        other.hp=0
    else:
        other.hp-=dmg
    if self.ability!="Rock Head" and a!=0:
        self.hp-=round(dmg/3)
        print(f"{self.name} was hurt by recoil.")         
    ch=random.randint(1,100)
    if ch>90 and other.status=="Alive" and other.ability!="Volt Switch":
        other.status="Paralyzed"
        print(f"{other.name} was paralyzed.") 
def flareblitz(self,other):
    self.atktype="Fire"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    w=weathereff(self)
    al=1
    r=randroll()
    print(f"{self.name} used "+colored("Flare Blitz","red")+".")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical(self.level,self.atk,other.defense,120,a,b,c,r,al,w)
    if dmg>other.hp:
        dmg=other.hp
        other.hp=0
    else:
        other.hp-=dmg
    if self.ability!="Rock Head":
        self.hp-=round(dmg/3)
        print(f"{self.name} was hurt by recoil.")         
    ch=random.randint(1,100)
    if ch>90 and other.status=="Alive" and other.ability!="Flash Fire":
        other.status="Burned"
        print(f"{other.name} was burned.")
        other.atk*=0.5 
def boltstrike(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used "+colored("Bolt Strike","yellow")+".")
    c=critch(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,130,a,b,c,r,al)  
    ch=random.randint(1,100)
    if ch>80 and other.status=="Alive":
        other.status="Paralyzed"
        print(f"{other.name} is paralyzed.")
        
def freezeshock(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used "+colored("Freeze Shock","cyan")+".")
    c=critch(self,other)
    self.atktype="Ice"
    w=weathereff(self)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,140,a,b,c,r,al,w)  
    ch=random.randint(1,100)
    if ch>70 and other.status=="Alive":
        other.status="Paralyzed"
        print(f"{other.name} is paralyzed.")
      
def fusionbolt(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used "+colored("Fusion Bolt","yellow")+".")
    c=critch(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,100,a,b,c,r,al)  
       
def tpunch(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used "+colored("Thunder Punch","yellow")+".")
    c=critch(self,other)
    self.atktype="Electric"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    if self.ability=="Iron Fist":
        print(f"{self.name}'s {self.ability}!")
        al=1.2
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)  
    ch=random.randint(1,100)
    if ch>90 and other.status=="Alive":
        other.status="Paralyzed"
        print(f"{other.name} is paralyzed.")
      
def poisontail(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Poison Tail.")
    c=critch(self,other)
    self.atktype="Poison"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,90,a,b,c,r,al)          
    ch=random.randint(1,100)
    if ch>70 and other.status=="Alive" and other.type1 not in ["Steel","Poison"] and other.type2 not in ["Steel","Poison"] and other.ability not in ["Immunity","Magic Bounce"]:
        other.status="Badly Poisoned"
        print(f"{other.name} was badly poisoned.")            
def poisonfang(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Poison Fang.")
    c=critch(self,other)
    self.atktype="Poison"
    if self.ability=="Strong Jaw":
        print(f"{self.name}'s {self.ability}!")
        al=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,75,a,b,c,r,al)          
    ch=random.randint(1,100)
    if ch>70 and other.status=="Alive" and other.type1 not in ["Steel","Poison"] and other.type2 not in ["Steel","Poison"] and other.ability not in ["Immunity","Magic Bounce"]:
        other.status="Badly Poisoned"
        print(f"{other.name} was badly poisoned.")    
def psychicfang(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Psychic Fang.")
    c=critch(self,other)
    self.atktype="Psychic"
    if self.ability=="Strong Jaw":
        print(f"{self.name}'s {self.ability}!")
        al=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,75,a,b,c,r,al)          
def tfang(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Thunder Fang.")
    c=critch(self,other)
    self.atktype="Electric"
    if self.ability=="Strong Jaw":
        print(f"{self.name}'s {self.ability}!")
        al=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,75,a,b,c,r,al)  
    ch=random.randint(1,100)
    if ch>80 and other.status=="Alive":
        other.status="Paralyzed"
        print(f"{other.name} is paralyzed.")
      
def plasmafists(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Plasma Fists.")
    c=critch(self,other)
    self.atktype="Electric"
    if self.ability=="Iron Fist":
        print(f"{self.name}'s {self.ability}!")
        al=1.2
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,100,a,b,c,r,al)          
def suckerpunch(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Sucker Punch.")
    c=critch(self,other)
    self.atktype="Dark"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)         
def machpunch(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Mach Punch.")
    c=critch(self,other)
    self.atktype="Fighting"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    if self.ability=="Iron Fist":
        print(f"{self.name}'s {self.ability}!")
        al=1.2
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,40,a,b,c,r,al)              
def iceshard(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Ice Shard.")
    c=critch(self,other)
    self.atktype="Ice"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,40,a,b,c,r,al)          
def hornleech(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Horn Leech.")
    c=critch(self,other)
    self.atktype="Grass"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,75,a,b,c,r,al)      
    if a!=0:
        print(f"{other.name} had its energy drained!")
    if dmg>other.hp:
        dmg=other.hp
        other.hp-=dmg
    else:
        other.hp-=dmg
    heal=dmg/2
    if heal<=(self.maxhp-heal):
        self.hp+=heal
    else:
        self.hp=self.maxhp    
def bitterblade(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Bitter Blade.")
    c=critch(self,other)
    self.atktype="Fire"
    w=weathereff(self)
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,75,a,b,c,r,al,w)      
    if a!=0:
        print(f"{other.name} had its energy drained!")
    if dmg>other.hp:
        dmg=other.hp
        other.hp-=dmg
    else:
        other.hp-=dmg
    heal=dmg/2
    if heal<=(self.maxhp-heal):
        self.hp+=heal
    else:
        self.hp=self.maxhp        
def drainpunch(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Drain Punch.")
    c=critch(self,other)
    self.atktype="Fighting"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    if self.ability=="Iron Fist":
        print(f"{self.name}'s {self.ability}!")
        al=1.2
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,75,a,b,c,r,al)      
    if a!=0:
        print(f"{other.name} had its energy drained!")
    if dmg>other.hp:
        dmg=other.hp
        other.hp-=dmg
    else:
        other.hp-=dmg
    heal=dmg/2
    if heal<=(self.maxhp-heal):
        self.hp+=heal
    else:
        self.hp=self.maxhp
def dizzypunch(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Dizzy Punch.")
    c=critch(self,other)
    self.atktype="Normal"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    if self.ability=="Iron Fist":
        print(f"{self.name}'s {self.ability}!")
        al=1.2
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)
def strength (self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Strength.")
    c=critch(self,other)
    self.atktype="Normal"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)          
def icepunch(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Ice Punch.")
    c=critch(self,other)
    self.atktype="Ice"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    if self.ability=="Iron Fist":
        print(f"{self.name}'s {self.ability}!")
        al=1.2
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)                  
    ch=random.randint(1,100)
    if ch>90 and other.status=="Alive":
        other.status="Frozen"
        print(f"{other.name} was frozen.")
def bodyslam(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Body Slam.")
    c=critch(self,other)
    self.atktype="Normal"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)     
    ch=random.randint(1,100)
    if ch>70 and other.status=="Alive":
        other.status="Paralyzed"
        print(f"{other.name} is paralyzed.")
     
    if other.ability=="Parental Bond":
        print(f"{self.name}'s {self.ability}!")
        dmg=dmg/2
        other.hp-=dmg
        ch=random.randint(1,100)
        if ch>70 and other.status=="Alive":
            other.status="Paralyzed"
            print(f"{other.name} is paralyzed.")
         
def forcepalm(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Force Palm.")
    c=critch(self,other)
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,60,a,b,c,r,al)     
    ch=random.randint(1,100)
    if ch>70 and other.status=="Alive":
        other.status="Paralyzed"
        print(f"{other.name} is paralyzed.")
     
def drillrun(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Drill Run.")
    c=critch(self,other,2)
    self.atktype="Ground"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)     
def smartstrike(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Smart Strike.")
    c=critch(self,other,2)
    self.atktype="Steel"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,70,a,b,c,r,al)         
def lightofruin(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Light of Ruin.")
    c=critch(self,other)
    self.atktype="Fairy"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=special (self.level,self.spatk,other.spdef,140,a,b,c,r,al)       
    if other.hp<dmg:
        dmg=other.hp
        other.hp-=dmg
    else:
        other.hp-=dmg        
    if self.ability!="Rock Head":
        print(f"{self.name} was hurt by recoil.")
        self.hp-=dmg/2    
def mindblown(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Mind Blown.")
    c=critch(self,other)
    self.atktype="Fire"
    w=weathereff(self)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=special (self.level,self.spatk,other.spdef,150,a,b,c,r,al)       
    if other.hp<dmg:
        dmg=other.hp
        other.hp-=dmg
    else:
        other.hp-=dmg        
    if self.ability!="Magic Guard":
        print(f"{self.name} was hurt by recoil.")
        self.hp-=self.maxhp/2                    
def chloroblast(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Chloroblast.")
    c=critch(self,other)
    self.atktype="Grass"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=special (self.level,self.spatk,other.spdef,120,a,b,c,r,al)       
    if other.hp<dmg:
        dmg=other.hp
        other.hp-=dmg
    else:
        other.hp-=dmg        
    if self.ability!="Rock Head":
        print(f"{self.name} was hurt by recoil.")
        self.hp-=self.maxhp/2            
def headsmash(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Head Smash.")
    c=critch(self,other)
    self.atktype="Rock"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,150,a,b,c,r,al)       
    if other.hp<dmg:
        dmg=other.hp
        other.hp-=dmg
    else:
        other.hp-=dmg        
    if self.ability!="Rock Head":
        print(f"{self.name} was hurt by recoil.")
        self.hp-=dmg/2
def gunkshot(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Gunk Shot.")
    c=critch(self,other)
    self.atktype="Poison"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,120,a,b,c,r,al)    
    other.hp-=dmg    
    ch=random.randint(1,100)
    if ch>70 and other.status=="Alive" and other.type1 not in ["Steel","Poison"] and other.type2 not in ["Steel","Poison"] and other.ability not in ["Immunity","Magic Bounce"]:
        other.status="Badly Poisoned"
        print(f"{other.name} was badly poisoned.")    
def belch(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Belch.")
    c=critch(self,other)
    self.atktype="Poison"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=special(self.level,self.spatk,other.spdef,120,a,b,c,r,al)    
    other.hp-=dmg            
    self.hp-=(self.maxhp/3)
    print(f"{self.name} was hurt by extreme poison.")
def bravebird(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Brave Bird.")
    c=critch(self,other)
    self.atktype="Flying"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,120,a,b,c,r,al)    
    if dmg>other.hp:
        dmg=other.hp
        other.hp=0
    else:
        other.hp-=dmg
    if self.ability!="Rock Head":
        self.hp-=round(dmg/3)
        print(f"{self.name} was hurt by recoil.")
def woodhammer(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Wood Hammer.")
    c=critch(self,other)
    self.atktype="Grass"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,120,a,b,c,r,al)    
    if dmg>other.hp:
        dmg=other.hp
        other.hp=0
    else:
        other.hp-=dmg
    if self.ability!="Rock Head":
        self.hp-=round(dmg/3)
        print(f"{self.name} was hurt by recoil.")        
def skyattack(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Sky Attack.")
    c=critch(self,other,2)
    self.atktype="Flying"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,150,a,b,c,r,al)               
def crunch(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Crunch.")
    c=critch(self,other)
    self.atktype="Dark"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    if self.ability=="Strong Jaw":
        print(f"{self.name}'s {self.ability}!")
        al=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)
    other.hp-=dmg
    ch=random.randint(1,100)
    if ch>80 and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        defchange(other,-0.5)
        print (f"{other.name}: Defense x{other.defb}")
    if other.ability=="Parental Bond":
        print(f"{self.name}'s {self.ability}!")
        dmg=dmg/2
        other.hp-=dmg
        ch=random.randint(1,100)
        if ch>80 and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
            defchange(other,-0.5)
            print (f"{other.name}: Defense x{other.defb}")
def playrough(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Play Rough.")
    c=critch(self,other)
    self.atktype="Fairy"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)                      
    ch=random.randint(1,10)
    if ch==7 and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        atkchange(other,-0.5)
        print (f"{other.name}: Attack x{other.atkb}")
def powerwhip(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Power Whip.")
    c=critch(self,other)
    self.atktype="Grass"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)        
def aquatail(self,other):
    w=weathereff(self)
    al=1
    r=randroll()
    print(f"{self.name} used Aqua Tail.")
    c=critch(self,other)
    self.atktype="Water"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al,w)         
def dragonclaw(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Dragon Claw.")
    c=critch(self,other)
    self.atktype="Dragon"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)   
def mountaingale(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Mountain Gale.")
    c=critch(self,other)
    self.atktype="Ice"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,100,a,b,c,r,al)       
def fakeout(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Fake Out.")
    c=critch(self,other)
    self.atktype="Normal"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,40,a,b,c,r,al)         
    if other.ability not in ["Inner Focus"]:
        other.flinched=True 
def eggbomb(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Egg Bomb.")
    c=critch(self,other)
    self.atktype="Normal"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)  
def knockoff(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Knock Off.")
    c=critch(self,other)
    self.atktype="Dark"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=65
    if "Mega " not in other.name and "Z-Crystal" not in other.name:
        print(f"{self.name} knocked off {other.name}'s {other.item}!")
        other.item=None
    other.hp-=physical (self.level,self.atk,other.defense,base,a,b,c,r,al)      
def crushclaw(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Crush Claw.")
    c=critch(self,other)
    self.atktype="Normal"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)      
    ch=random.randint(1,2)
    if ch==2 and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        defchange(other,-0.5)
        print(f"{other.name} Defense x{other.defb}")
def seedbomb(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Seed Bomb.")
    c=critch(self,other)
    self.atktype="Grass"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)                  
def irontail(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Iron Tail.")
    c=critch(self,other)
    self.atktype="Steel"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,100,a,b,c,r,al)             
    ch=random.randint(1,100)
    if ch>70 and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        defchange(other,0.5)
        print(f"{other.name} Defense x{other.defb}")
def moongeistbeam(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Moongeist Beam!")
    c=critch(self,other)
    self.atktype="Ghost"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special (self.level,self.spatk,other.spdef,100,a,b,c,r,al)              
def sunsteelstrike(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Sunsteel Strike!")
    c=critch(self,other)
    self.atktype="Steel"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,100,a,b,c,r,al)              
def ironhead(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Iron Head.")
    c=critch(self,other)
    self.atktype="Steel"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)      
    chance=30
    if self.ability=="Serene Grace":
        chance*=2
    if self.speed>other.speed:
        ch=random.randint(1,100)            
        if ch>(100-chance) and other.ability not in ["Inner Focus"]:
            other.flinched=True
def meteormash(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Meteor Mash.")
    c=critch(self,other)
    self.atktype="Steel"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,90,a,b,c,r,al)    
    other.hp-=dmg  
    ch=random.randint(1,100)
    if ch<80:
        atkchange(self,0.5)
        print(f"Attack x{self.atkb}")     
def grassyglide(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Grassy Glide.")
    c=critch(self,other)
    self.atktype="Grass"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,70,a,b,c,r,al)     
    other.hp-=dmg            
def appleacid(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Apple Acid.")
    c=critch(self,other)
    self.atktype="Grass"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=special (self.level,self.spatk,other.spdef,80,a,b,c,r,al)     
    if other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        other.hp-=dmg  
        defchange(other,-0.5)
        print(f"{other.name}: Special Defense x{other.spdefdb}")       
def gravapple(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Grav Apple.")
    c=critch(self,other)
    self.atktype="Grass"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)     
    other.hp-=dmg  
    defchange(other,-0.5)
    print(f"{other.name}: Defense x{other.defdb}")           
def drumbeating(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Drum Beating.")
    c=critch(self,other)
    self.atktype="Grass"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)     
    if other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        other.hp-=dmg  
        speedchange(other,-0.5)
        print(f"{other.name}: Speed x{other.speedb}")             
def hammerarm(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Hammer Arm.")
    c=critch(self,other)
    self.atktype="Fighting"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,100,a,b,c,r,al)     
    other.hp-=dmg  
    speedchange(self,-0.5)
    print(f"Speed x{self.speedb}")        
def poweruppunch(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Power-up Punch.")
    c=critch(self,other)
    self.atktype="Fighting"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    if self.ability=="Iron Fist":
        print(f"{self.name}'s {self.ability}!")
        al=1.2
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,40,a,b,c,r,al)     
    other.hp-=dmg  
    atkchange(self,0.5)
    print(f"Attack x{self.atkb}")
    if other.ability=="Parental Bond":
        print(f"{self.name}'s {self.ability}!")
        dmg=dmg/2
        other.hp-=dmg
        atkchange(self,0.5)
        print(f"Attack x{self.atkb}")
def doubleedge(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Double-Edge.")
    c=critch(self,other)
    self.atktype="Normal"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,100,a,b,c,r,al) 
    if dmg>other.hp:
        dmg=other.hp
        other.hp=0
    else:
        other.hp-=dmg
    if other.ability=="Parental Bond":
        print(f"{self.name}'s {self.ability}!")
        dmg=dmg/2
        other.hp-=dmg
    if self.ability!="Rock Head":
        self.hp-=round(dmg/3)
        print(f"{self.name} was hurt by recoil.")
def extemespeed(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Extreme Speed.")
    c=critch(self,other)
    self.atktype="Normal"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)              
def crabhammer(self,other):
    self.atktype="Water"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f"{self.name} used Crabhammer.")
    c=critch(self,other,2)
    
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,100,a,b,c,r,al,w)  
def slash(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Slash.")
    c=critch(self,other,2)
    self.atktype="Normal"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,70,a,b,c,r,al) 
def direclaw(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Dire Claw!")
    c=critch(self,other,2)
    self.atktype="Poison"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,65,a,b,c,r,al)      
    ch=random.randint(1,100)
    if ch>90 and other.status=="Alive":
        other.status="Sleep"
    ch=random.randint(1,100)
    if ch>90 and other.status=="Alive":
        other.status="Badly Poisoned"
    ch=random.randint(1,100)
    if ch>90 and other.status=="Alive":
        other.status="Paralyzed"
def nightslash(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Night Slash.")
    c=critch(self,other,2)
    self.atktype="Dark"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,70,a,b,c,r,al)  
def shadowpunch(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Shadow Punch!")
    c=critch(self,other,2)
    self.atktype="Ghost"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,70,a,b,c,r,al)          
def shadowclaw(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Shadow Claw!")
    c=critch(self,other,2)
    self.atktype="Ghost"
    if self.ability=="Tough Claws":
        print(f"{self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,70,a,b,c,r,al)      
def hyperspacefury(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Hyperspace Fury!")
    c=critch(self,other)
    self.atktype="Dark"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,100,a,b,c,r,al)            
def psychocut(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Psycho Cut.")
    c=critch(self,other,2)
    self.atktype="Psychic"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,70,a,b,c,r,al)   
def esperwing(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Esper Wing!")
    c=critch(self,other,2)
    self.atktype="Psychic"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,75,a,b,c,r,al)       
def wickedblow(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Wicked Blow.")
    c=critch(self,other,16)
    self.atktype="Dark"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)   
def ceaseless(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Ceasless Edge.")
    c=critch(self,other,16)
    self.atktype="Dark"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,70,a,b,c,r,al)       
def surgingstrikes(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Surging Strikes.")
    c=critch(self,other,16)
    self.atktype="Water"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,25,a,b,c,r,al)                    
def dragonascent(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Dragon Ascent.")
    c=critch(self,other)
    self.atktype="Flying"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,120,a,b,c,r,al)     
    defchange(self,-0.5)
    spdefchange(self,-0.5)
    print(f"Defense x{self.defb}")
    print(f"Special Defense x{self.spdefb}")
def weatherball(self,other):
    self.atktype="Normal"
    base=50
    if field.weather in ["Primordial Sea","Rainy"]:
        self.atktype="Water"
        base=100
    if field.weather in ["Desolate Land","Sunny"]:
        self.atktype="Fire" 
        base=100      
    if field.weather in ["Hail"]:
        self.atktype="Ice"  
        base=100     
    if field.weather in ["Sandstorm"]:
        self.atktype="Rock"  
        base=100
    al=1
    w=weathereff(self)
    r=randroll()
    print(f"{self.name} used Weather Ball.")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,base,a,b,c,r,al,w)
       
def raindance(self,tr1,turn):
    print(f"{self.name} used Rain Dance.")
    if field.weather not in ["Desolate Land","Primordial Sea","Strong Wind","Rainy"]  and field.weather not in ["Desolate Land","Primordial Sea","Strong Wind","Rainy"]:
        print(f"{self.name} made it rain.")
        field.weather="Rainy"
        tr1.rainturn=turn
        tr1.rainend(self)
    else:
        print("It failed.")        
def sunnyday(self,tr1,turn):
    print(f"{self.name} used Sunny Day.")
    if field.weather not in ["Desolate Land","Primordial Sea","Strong Wind","Sunny"]  and field.weather not in ["Desolate Land","Primordial Sea","Strong Wind","Sunny"]:
        print(f"{self.name} made the sunlight harsh.")
        field.weather="Sunny"
        tr1.sunturn=turn
        tr1.sunend(self)
    else:
        print("It failed.")        
def sandstorm(self,tr1,turn):
    print(f"{self.name} used Sandstorm.")
    if field.weather not in ["Desolate Land","Primordial Sea","Strong Wind","Sandstorm"]  and field.weather not in ["Desolate Land","Primordial Sea","Strong Wind","Sandstorm"]:
        print(f"{self.name} started a sandstorm.")
        field.weather="Sandstorm" 
        tr1.sandturn=turn
        tr1.sandend(self)
    else:
        print("It failed.")
def hail(self,tr1,turn):
    print(f"{self.name} used Hail.")
    if field.weather not in ["Desolate Land","Primordial Sea","Strong Wind","Hail"]  and field.weather not in ["Desolate Land","Primordial Sea","Strong Wind","Hail"]:
        print(f"{self.name} started a hailstorm.")
        field.weather="Hail"     
        tr1.hailturn=turn
        tr1.hailend(self) 
    else:
        print("It failed.")           
def dualwingbeat(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Dual Wingbeat.")
    c=critch(self,other)
    self.atktype="Flying"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)         
def precipiceblades(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Precipice Blades.")
    c=critch(self,other)
    self.atktype="Ground"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,120,a,b,c,r,al)         
def oblivionwing(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Oblivion Wing.")
    c=critch(self,other)
    self.atktype="Flying"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=special(self.level,self.spatk,other.spdef,80,a,b,c,r,al)    
    if dmg>other.hp:
        dmg=other.hp
        other.hp-=dmg
    else:
        other.hp-=dmg
    heal=dmg*0.75
    if heal<=(self.maxhp-heal):
        self.hp+=heal
    else:
        self.hp=self.maxhp    
def gigadrain(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Giga Drain.")
    c=critch(self,other)
    self.atktype="Grass"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al)    
    if dmg>other.hp:
        dmg=other.hp
        other.hp-=dmg
    else:
        other.hp-=dmg
    heal=dmg/2
    if heal<=(self.maxhp-heal):
        self.hp+=heal
    else:
        self.hp=self.maxhp
def relicsong(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Relic Song.")
    c=critch(self,other)
    self.atktype="Normal"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=special(self.level,self.spatk,other.spdef,75,a,b,c,r,al)            
    other.hp-=dmg
    ch=random.randint(1,100)
    if ch>90:
        if other.status!="Sleep":
            print(f"{other.name} fell asleep.")
            other.status="Sleep"

def leechlife(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Leech Life.")
    c=critch(self,other)
    self.atktype="Bug"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=special(self.level,self.spatk,other.spdef,80,a,b,c,r,al)    
    if dmg>other.hp:
        dmg=other.hp
        other.hp-=dmg
    else:
        other.hp-=dmg
    heal=dmg/2
    if heal<=(self.maxhp-heal):
        self.hp+=heal
    else:
        self.hp=self.maxhp        
def surf(self,other):
    w=weathereff(self)
    al=1
    r=randroll()
    print(f"{self.name} used Surf.")
    c=critch(self,other)
    self.atktype="Water"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al,w)  
def dracometeor(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Draco Meteor.")
    c=critch(self,other)
    self.atktype="Dragon"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,130,a,b,c,r,al)  
    spatkchange(self,-1)
    print(f"Special Attack x{self.spatkb}")
def originpulse(self,other):
    al=1
    self.atktype="Water"
    w=weathereff(self)
    r=randroll()
    print(f"{self.name} used Origin Pulse.")
    c=critch(self,other)
    
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,120,a,b,c,r,al,w)          
def apower(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Ancient Power.")
    c=critch(self,other)
    self.atktype="Rock"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al)      
    ch=random.randint(1,10)
    if ch==7:
        atkchange(self,0.5)
        defchange(self,0.5)
        spatkchange(self,0.5)
        spdefchange(self,0.5)
        speedchange(self,0.5)
        print(f"Attack x{self.atkb}")
        print(f"Defense x{self.defb}")
        print(f"Special Attack x{self.spatkb}")
        print(f"Special Defense x{self.spdefb}")
        print(f"Speed x{self.speedb}")
def scald(self,other):
    self.atktype="Water"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f"{self.name} used Scald.")
    c=critch(self,other)
    
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,80,a,b,c,r,al,w)            
    ch=random.randint(1,100)
    if ch>70 and other.status=="Alive":
        other.status="Burned"
        print(f"{other.name} was burned.")
      
def scorchingsands(self,other):
    self.atktype="Ground"
    al=1
    r=randroll()
    print(f"{self.name} used Scorching Sands.")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al)            
    ch=random.randint(1,100)
    if ch>70 and other.status=="Alive":
        other.status="Burned"
        print(f"{other.name} was burned.")
      
def doomdesire(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Doom Desire.")
    c=critch(self,other)
    self.atktype="Steel"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,140,a,b,c,r,al)        
    
def flashcannon(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Flash Cannon.")
    c=critch(self,other)
    self.atktype="Steel"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al)        
    ch=random.randint(1,10)
    if ch==7:
        spdefchange(other,-0.5)
        print(f"{other.name}: Special Defense x{other.spdefb}")
def psychoboost(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Psycho Boost.")
    c=critch(self,other)
    self.atktype="Psychic"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,140,a,b,c,r,al)       
    spatkchange(self,-1)
    print(f"Special Attack x{self.spatkb}")
def victorydance(self):
    print(f"{self.name} used Victory Dance.")
    atkchange (self,0.5)
    defchange(self,0.5)
    spatkchange(self,0.5)
    spdefchange(self,0.5)
    print(f"Attack x{self.atkb}")
    print(f"Defense x{self.spdefb}")
    print(f"Special Attack x{self.spatkb}")
    print(f"Special Defense x{self.spdefb}")    
def takeheart(self):
    print(f"{self.name} used Take Heart.")
    atkchange (self,0.5)
    defchange(self,0.5)
    spatkchange(self,0.5)
    spdefchange(self,0.5)
    print(f"Attack x{self.atkb}")
    print(f"Defense x{self.spdefb}")
    print(f"Special Attack x{self.spatkb}")
    print(f"Special Defense x{self.spdefb}")
def heartswap(self,other):
    print(f"{self.name} used Heart Swap.")
    st1=self.atkb
    st2=self.defb
    st3=self.spatkb
    st4=self.spdefb
    st5=self.speedb
    self.atkb=other.atkb
    self.defb=other.defb
    self.spatkb=other.spatkb
    self.spdefb=other.spdefb
    self.speedb=other.speedb
    other.atkb=st1
    other.defb=st2
    other.spatkb=st3
    other.spdefb=st4
    other.speedb=st5
    print(f"{self.name} swapped it's stat changes with {other.name}.")
def transform(self,other):
    print(f'{self.name} transformed into {other.name}')
    self.maxhp=other.maxhp
    self.atk=other.atk
    self.defense=other.defense
    self.spatk=other.spatk
    self.spdef=other.spdef
    self.speed=other.speed    
    self.atkb=other.atkb
    self.defb=other.defb
    self.spatkb=other.spatkb
    self.spdefb=other.spdefb
    self.speedb=other.speedb    
    self.moves=other.moves
    self.type1=other.type1
    self.type2=other.type2
    self.ability=other.ability
    self.name=self.name+f"({other.name})"
def seismictoss(self,other):
    if other.type1!="Ghost" and other.type2!="Ghost":
        print(f"{self.name} used Seismic Toss.")
        other.hp-=self.level
    else:
        print(f"Doesn't effect on {other.name}")
def nightshade(self,other):
    if other.type1!="Normal" and other.type2!="Normal":
        print(f"{self.name} used Night Shade.")
        other.hp-=self.level
    else:
        print(f"Doesn't effect on {other.name}")        
def flamethrower (self,other):
    self.atktype="Fire"
    w=weathereff(self)
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used Flamethrower.")
    c=critch(self,other)
    
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al,w)        
    ch=random.randint(1,100)
    if ch>90 and other.status=="Alive":
        other.status="Burned"
        print(f"{other.name} was burned.")
      
def solarbeam(self,other):
    al=1
    r=randroll()
    if (field.weather in ["Sunny","Desolate Land"]) or self.precharge==True:
        print(f"{self.name} used Solar Beam.")
        c=critch(self,other)
        self.atktype="Grass"
        ab=weakness(self,other,field)
        a=ab[0]
        b=ab[1]   
        other.hp-=special(self.level,self.spatk,other.spdef,120,a,b,c,r,al)         
        self.precharge=False
    elif self.precharge==False:
        print(f"{self.name} is absorbing sunlight!")
        self.precharge=True
    
def terablast(self,other):
    if self.teratype!=None:
        self.type2=None
        self.type1=self.teratype
        print(f"{self.name} terastalized into {self.type1}-type!")
    self.atktype=self.type1
    w=weathereff(self)
    al=1
    r=randroll()
    print(f"{self.name} used Tera Blast.")
    c=critch(self,other)
    
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    if self.atk>self.spatk:
        other.hp-=physical(self.level,self.atk,other.defense,90,a,b,c,r,al,w)
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al,w)                 
def hiddenpower(self,other):
    al=1
    
    r=randroll()
    x=hidp(self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv)
    base=x[0]
    self.atktype=x[1]
    w=weathereff(self)
    print(f"{self.name} used Hidden Power({self.atktype}).")
    c=critch(self,other)
    
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,base,a,b,c,r,al,w)
    
    
def special(level,spatk,spdef,base,a,b,c,r,al,w=1):
    dmg=round((((2*level + 10)/250)*(spatk/spdef)*base+2)*a*b*c*r*al*w)
    return dmg
def physical(level,atk,defense,base,a,b,c,r,al,w=1):
    dmg=round((((2*level + 10)/250)*(atk/ defense)*base+2)*a*b*c*r*al*w)
    return dmg
def weather(mon,pk):
    if field.weather =="Rainy":
        print("Rain continues to fall.\n")
    if field.weather =="Sandtorm":
        print("The sandstorm is raging!\n")
    if field.weather=="Hail":
        print("Hail continues to fall.\n")   
    if field.weather=="Sunny":
        print("The sunlight is strong.\n")        

def weathereff(mon):
    if field.weather=="Desolate Land" and mon.atktype=="Water":
        print("The Water-type attack evaporated in the harsh sunlight!")
        return 0
    if field.weather=="Primordial Sea" and mon.atktype=="Fire":
        print("The Fire-type attack fizzled out in the heavy rain!")
        return 0                                 
    if field.weather in ["Rainy","Primordial Sea"] and mon.atktype=="Water":
        return 1.5
    if (field.weather=="Sunny") and mon.atktype=="Water":
        return 0.5    
    if (field.weather=="Rain") and mon.atktype=="Fire":
        return 0.5      
    if field.weather in ["Sunny" ,"Desolate Land"] and mon.atktype=="Fire":
        return 1.5          
    if field.weather=="Hail" and mon.atktype=="Ice":
        return 1.5          
    else:
        return 1 
        