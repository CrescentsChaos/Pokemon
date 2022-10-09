#pylint:disable=C0301
#pylint:disable=W0622
#pylint:disable=W0621
#pylint:disable=C0103
#pylint:disable=C0303
#from attack import *
#from battle import *
from pokemonbase import Pokemon
from pokemonbase2 import Pokemon2
from typematchup import *
from hiddenpower import *
def fireBlast(self,other):
    self.atktype="Fire"
    w=weathereff(self)
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used Fire Blast.")
    
    c=critch(self)
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,110,a,b,c,r,al,w)
    ch=random.randint(1,10)
    if ch==1 and other.status is None and self.ability!="Sheer Force":
        other.status="Burned"
        print(f"{other.name} was burned.")
        other.atk=other.atk/2
def rest(self):
    print(f"{self.name} used Rest.")           
    if self.status!="Sleep":
        self.status="Sleep"
        print(f"{self.name} fell asleep.")
        self.hp=self.maxhp
def lusterpurge(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used Luster Purge.")
    self.atktype="Psychic"
    c=critch(self)
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al)
    ch=random.randint(1,2)
    if ch==2 and self.ability=="Sheer Force":
        spdefchange(other,-0.5)
        print(f"{other.name}: Special Defense x"+str(self.spdefb))
def mistball(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used Mist Ball.")
    self.atktype="Psychic"
    c=critch(self)
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al)
    ch=random.randint(1,2)
    if ch==2 and self.ability=="Sheer Force":
        spatkchange(other,-0.5)
        print(f"{other.name}: Special Attack x"+str(self.spatkb))
def psychic(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used Psychic.")
    self.atktype="Psychic"
    c=critch(self)
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al)
    ch=random.randint(1,10)
    if ch==7:
        spdefchange(other,-0.5)
        print(f"{other.name}: Special Defense x"+str(self.spdefb))
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
def irondefense(self):
    print(f"{self.name} used Iron Defense.")    
    defchange(self,1)
    print(f"Defense x{self.defb}")  
def leechseed(self,other):
    print(f"{self.name} used Leech Seed.")    
    if other.type1!="Grass" and other.type2!="Grass" and other.ability!="Magic Bounce":
        other.seeded=True
    elif other.ability=="Magic Bounce":
        self.seeded=True
def strengthsap(self,other):
    print(f"{self.name} used Strength Sap.")    
    prevatk=other.atk
    atkchange(other,-0.5)
    newatk=other.atk*other.atkb
    heal=prevatk-newatk
    print(f"{other.name}: Attack x{self.atkb}")  
    if heal<=(self.maxhp-heal):
        self.hp+=heal
    else:
        self.hp=self.maxhp
def bulkup(self):
    print(f"{self.name} used Bulk Up.")
    atkchange(self,0.5)     
    defchange(self,0.5)   
    print(f"Attack x{self.atkb}")   
    print(f"Defense x{self.defb}")          
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
    
    c=critch(self)
    ab=weakness(self,other)
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
    
    c=critch(self)
    ab=weakness(self,other)
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
    c=critch(self)
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)           
def gigavolthavoc(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Gigavolt Havoc.")
    self.atktype="Electric"
    c=critch(self)
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)           
def continentalcrush(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Continental Crush.")
    self.atktype="Rock"
    c=critch(self)
    ab=weakness(self,other)
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
    c=critch(self)
    ab=weakness(self,other)
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
    c=critch(self)
    ab=weakness(self,other)
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
    c=critch(self)
    ab=weakness(self,other)
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
        other.speed=other.speed/2
def sleeppowder(self,other):
    print(f"{self.name} used Sleep Powder.")
    if other.status!="Sleep" and (other.type1!="Grass" and other.type2!="Grass"):
        print(f"{other.name} fell asleep.")
        other.status="Sleep"
    else:
        print("It failed.")
def spore(self,other):
    print(f"{self.name} used Spore.")
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
    c=critch(self)
    ab=weakness(self,other)
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
    c=critch(self)
    ab=weakness(self,other)
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
    c=critch(self)
    ab=weakness(self,other)
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
    c=critch(self)
    ab=weakness(self,other)
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
    c=critch(self)
    ab=weakness(self,other)
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
    c=critch(self)
    ab=weakness(self,other)
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
    c=critch(self)
    ab=weakness(self,other)
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
    c=critch(self)
    ab=weakness(self,other)
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
    c=critch(self)
    ab=weakness(self,other)
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
    c=critch(self)
    ab=weakness(self,other)
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
    c=critch(self)
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)                                
def shadowball (self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used Shadow Ball.")
    self.atktype="Ghost"
    c=critch(self)
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,80,a,b,c,r,al)  
    ch=random.randint(1,10)
    if ch==7:
        spdefchange(other,-0.5)
        print(f"{other.name}: Special Defense x"+str(self.spdefb))
def signalbeam (self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Signal Beam.")
    self.atktype="Bug"
    c=critch(self)
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,70,a,b,c,r,al)            
def aeroblast (self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Aeroblast.")
    self.atktype="Flying"
    c=critch(self)
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,100,a,b,c,r,al)        
def leafstorm(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Leaf Storm.")
    self.atktype="Grass"
    c=critch(self)
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,130,a,b,c,r,al)           
def blizzard(self,other):
    self.atktype="Ice"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f"{self.name} used Blizzard.")
    
    c=critch(self)
    ab=weakness(self,other)
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
    c=critch(self)
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,140,a,b,c,r,al)        
def airslash(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Air Slash).")
    self.atktype="Flying"
    c=critch(self)
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,75,a,b,c,r,al)     
    if self.speed>other.speed:
        ch=random.randint(1,3)            
        if ch==1:
            other.flinch=True
def leaftornado(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Leaf Tornado.")
    self.atktype="Grass"
    c=critch(self)
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,130,a,b,c,r,al)             
       
def psystrike(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Psystrike.")
    self.atktype="Psychic"
    c=critch(self)
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.defense,100,a,b,c,r,al)             
def sacredfire(self,other):
    self.atktype="Fire"
    al=1
    r=randroll()
    print(f"{self.name} used Sacred Fire.")
    
    c=critch(self)
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,110,a,b,c,r,al)  
def aurasphere(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Aura Sphere.")
    self.atktype="Fighting"
    c=critch(self)
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,80,a,b,c,r,al)      
    
def heatwave(self,other):
    self.atktype="Fire"
    al=1
    w=weathereff(self)
    r=randroll()
    print(f"{self.name} used Heat Wave.")
    
    c=critch(self)
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,95,a,b,c,r,al,w)     
def bleakwindstorm(self,other):
    al=1
    w=weathereff(self)
    r=randroll()
    print(f"{self.name} used Bleakwind Storm.")
    self.atktype="Flying"
    c=critch(self)
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,95,a,b,c,r,al,w)   
def sandsearstorm(self,other):
    al=1
    w=weathereff(self)
    r=randroll()
    print(f"{self.name} used Sandsear Storm.")
    self.atktype="Ground"
    c=critch(self)
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,95,a,b,c,r,al,w)                          
def wildboltstorm(self,other):
    al=1
    w=weathereff(self)
    r=randroll()
    print(f"{self.name} used Wildbolt Storm.")
    self.atktype="Electric"
    c=critch(self)
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,95,a,b,c,r,al,w)         
def synthesis(self):
    print(f"{self.name} used Synthesis.")   
    if self.hp>=(self.maxhp/2):
        self.hp=self.maxhp
    elif self.hp==self.maxhp:
        print("Already at full HP.")
    else:
        if Pokemon.weather=="Sunny" or Pokemon2.weather=="Sunny":
            self.hp+=((self.maxhp*2)/3)    
        if Pokemon.weather in ["Sunny","Rainy","Hail"] or Pokemon2.weather in ["Sunny","Rainy","Hail"]:
            self.hp+=(self.maxhp/4)    
        else:
            self.hp+=(self.maxhp/2)
def recover(self):
    print(f"{self.name} used Recover.")   
    if self.hp>=(self.maxhp/2):
        self.hp=self.maxhp
    elif self.hp==self.maxhp:
        print("Already at full HP.")
    else:
        self.hp+=(self.maxhp/2)
def roost(self):
    print(f"{self.name} used Roost.")   
    if self.hp>=(self.maxhp/2):
        self.hp=self.maxhp
    elif self.hp==self.maxhp:
        print("Already at full HP.")
    else:
        self.hp+=(self.maxhp/2)        
def slackoff(self):
    print(f"{self.name} used Slack Off.")   
    if self.hp>=(self.maxhp/2):
        self.hp=self.maxhp
    elif self.hp==self.maxhp:
        print("Already at full HP.")
    else:
        self.hp+=(self.maxhp/2)             
def softboiled(self):
    print(f"{self.name} used Soft Boiled.")   
    if self.hp>=(self.maxhp/2):
        self.hp=self.maxhp
    elif self.hp==self.maxhp:
        print("Already at full HP.")
    else:
        self.hp+=(self.maxhp/2)      
def toxic(self, other):
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
    print(f"{self.name} used Will-O-Wisp.")             
    if other.status=="Alive" and other.type1 not in ["Fire"] and other.type2 not in ["Fire"] and other.ability not in ["Flash Fire","Magic Bounce"]:
        other.status="Burned"
        print(f"{other.name} was burned.")
        other.atk=other.atk/2
    if other.ability in ["Magic Bounce","Synchronize"] and self.status=="Alive":
        self.status="Burned"
        print(f"{self.name} was burned.")
        other.atk=other.atk/2
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
    c=critch(self)
    self.atktype="Electric"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al)    
def focusblast(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used Focus Blast.")
    c=critch(self)
    self.atktype="Fighting"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,120,a,b,c,r,al)        
    ch=random.randint(1,10)
    if ch==7:
        spdefchange(other,-0.5)
        print(f"{other.name}: Special Defense x"+str(other.spdefb))
def thunder(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used Thunder.")
    c=critch(self)
    self.atktype="Electric"
    ab=weakness(self,other)
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
    c=critch(self)
    self.atktype="Poison"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,80,a,b,c,r,al)     
def boltbeak(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Bolt Beak.")
    c=critch(self)
    self.atktype="Electric"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    base=85
    if self.speed>other.speed:
        base*=2
    other.hp-=special(self.level,self.spatk,other.spdef,base,a,b,c,r,al)                   
def powergem(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Power Gem.")
    c=critch(self)
    self.atktype="Rock"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,80,a,b,c,r,al)            
def zapcannon(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used Zap Cannon.")
    c=critch(self)
    self.atktype="Electric"
    ab=weakness(self,other)
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
    print(f"{self.name} used Freeze Dry.")
    c=critch(self)
    self.atktype="Electric"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    if other.type1=="Water" or other.type2=="Water":
        a*=2
    other.hp-=special(self.level,self.spatk,other.spdef,70,a,b,c,r,al)                
def poisonjab(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used Poison Jab.")
    c=critch(self)
    self.atktype="Poison"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,90,a,b,c,r,al) 
def leafblade(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Leaf Blade.")
    c=critch(self,2)
    self.atktype="Grass"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,80,a,b,c,r,al)    
def gyroball(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Gyro Ball.")
    c=critch(self)
    self.atktype="Steel"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,80,a,b,c,r,al)   
    
def wildcharge(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Wild Charge.")
    c=critch(self)
    self.atktype="Electric"
    ab=weakness(self,other)
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
    c=critch(self)
    self.atktype="Rock"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,80,a,b,c,r,al)     
def acrobatics(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Acrobatics.")
    c=critch(self)
    self.atktype="Flying"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,110,a,b,c,r,al)     
def aurawheel(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Aura Wheel.")
    c=critch(self)
    self.atktype="Electricb"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,110,a,b,c,r,al)            
def barbbarrage(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Barb Barrage.")
    c=critch(self)
    self.atktype="Poison"
    ab=weakness(self,other)
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
    c=critch(self)
    self.atktype="Flying"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,100,a,b,c,r,al)     
def partingshot(self,other):
    print(f"{self.name} used Parting Shot.")        
    atkchange(other,-0.5)
    spatkchange (other,-0.5)
    print(f"{other.name}: Attack x{other.atkb}")
    print(f"{other.name}: Special Attack x{other.spatkb}")
def bonerush(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Bone Rush.")
    c=critch(self)
    self.atktype="Ground"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,125,a,b,c,r,al)          
def snarl(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Snarl.")
    c=critch(self)
    self.atktype="Dark"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,55,a,b,c,r,al)           
    spatkchange (other,-0.5) 
    print(f"{other.name}: Special Attack x{other.spatkb}")
def steelbeam(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Steel Beam.")
    c=critch(self)
    self.atktype="Steel"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,140,a,b,c,r,al)               
def aquajet(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Aqua Jet.")
    c=critch(self)
    self.atktype="Water"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,60,a,b,c,r,al)                              
def armthrust(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Arm Thrust.")
    c=critch(self)
    self.atktype="Fighting"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,75,a,b,c,r,al)    
def steelwing(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Steel Wing.")
    c=critch(self)
    self.atktype="Steel"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,70,a,b,c,r,al)  
    ch=random.randint(1,10)
    if ch==7:
        defchange(self,0.5)
        print("Defense x"+str(self.defb))
def heavyslam(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Heavy Slam.")
    c=critch(self)
    self.atktype="Steel"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    base=80*(self.spdef/other.spdef)
    other.hp-=physical(self.level,self.atk,other.defense,base,a,b,c,r,al)          
def assurance(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Assurance.")
    c=critch(self)
    self.atktype="Dark"
    ab=weakness(self,other)
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
    c=critch(self,2)
    self.atktype="Bug"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,90,a,b,c,r,al)             
def facade(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Facade.")
    c=critch(self)
    self.atktype="Bug"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    base=70
    if self.status!="Alive":
        base=140
    other.hp-=physical(self.level,self.atk,other.defense,base,a,b,c,r,al)                 
def retrn(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Return")
    c=critch(self)
    self.atktype="Normal"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    base=round(self.happiness*(2/5))
    other.hp-=physical(self.level,self.atk,other.defense,base,a,b,c,r,al)
def bodypress(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Body Press")
    c=critch(self)
    self.atktype="Fighting"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.defense,other.defense,80,a,b,c,r,al)    
    
def stoneedge(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used Stone Edge.")
    c=critch(self,2)
    self.atktype="Rock"
    ab=weakness(self,other)
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
    c=critch(self)
    self.atktype="Ice"
    ab=weakness(self,other)
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
    c=critch(self)
    self.atktype="Rock"
    ab=weakness(self,other)
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
    print(f"{self.name} used Waterfall.")
    c=critch(self)
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,85,a,b,c,r,al,w)       
    ch=random.randint(1,100)
    if ch>80:
        other.flinch=True        
def crosspoison(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used Cross Poison.")
    c=critch(self)
    self.atktype="Poison"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,90,a,b,c,r,al)           
def rockblast(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Rock Blast.")
    c=critch(self)
    self.atktype="Rock"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,125,a,b,c,r,al)         
def skyuppercut(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Sky Uppercut.")
    c=critch(self)
    self.atktype="Fighting"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,70,a,b,c,r,al)             
def blazekick(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Blaze Kick.")
    c=critch(self)
    self.atktype="Fire"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,85,a,b,c,r,al)             
def hijumpkick(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used High Jump Kick.")
    c=critch(self)
    self.atktype="Fighting"
    ab=weakness(self,other)
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
    c=critch(self)
    self.atktype="Dark"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,other.atk,other.defense,80,a,b,c,r,al)      
def iciclespears(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Icicle Spear.")
    c=critch(self)
    self.atktype="Ice"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,125,a,b,c,r,al)       
def pinmissile (self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Pin Missile.")
    c=critch(self)
    self.atktype="Bug"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,125,a,b,c,r,al)   
def brickbreak(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Brick Break.")
    c=critch(self)
    self.atktype="Fighting"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,70,a,b,c,r,al)       
    self.atk=self.maxatk*self.atkb
    self.spatk=self.maxspatk*self.spatkb
def megahorn(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Megahorn")
    c=critch(self)
    self.atktype="Bug"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,120,a,b,c,r,al)           
def icebeam(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used Ice Beam.")
    c=critch(self)
    self.atktype="Ice"
    ab=weakness(self,other)
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
    c=critch(self,16)
    self.atktype="Ice"
    ab=weakness(self,other)
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
    c=critch(self)
    self.atktype="Dark"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al)  
    ch=random.randint(1,100)
    if ch>80 and self.ability!="Sheer Force":
        other.flinch=True
def hyperbeam(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Hyper Beam.")
    c=critch(self)
    self.atktype="Normal"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al)         
def dragonpulse(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Dragon Pulse.")
    c=critch(self)
    self.atktype="Dragon"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al)   
def dazzlinggleam(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Dazzling Gleam.")
    c=critch(self)
    self.atktype="Fairy"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al)  
def lavaplume(self,other):
    self.atktype="Fire"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f"{self.name} used Lava Plume.")
    c=critch(self)
    
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al,w)       
    ch=random.randint(1,100)
    if ch>70 and other.type1!="Fire" and other.type2!="Fire" and other.ability!="Flash Fire" and other.status=="Alive":
        print(f"{other.name} was burned.")
        other.status="Burned"
        other.atk*=0.5
def hurricane (self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Hurricane.")
    c=critch(self)
    self.atktype="Flying"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,110,a,b,c,r,al)          
def inferno(self,other):
    self.atktype="Fire"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f"{self.name} used Inferno.")
    c=critch(self)
    
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al,w)
    if other.type1!="Fire" and other.type2!="Fire" and other.ability!="Flash Fire"     and other.status=="Alive"    :
        other.status="Burned"
        print(f"{other.name} was burned.")
        other.atk*=0.5
def overheat(self,other):
    self.atktype="Fire"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f"{self.name} used Overheat.")
    c=critch(self)
    
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,130,a,b,c,r,al)                
    spatkchange (self,-1)
    print(f"Special Attack x{self.spatkb}")
def blastburn(self,other):
    self.atktype="Fire"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f"{self.name} used Blast Burn.")
    c=critch(self)
    
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al,w)    
def eruption (self,other):
    self.atktype="Fire"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f"{self.name} used Eruption.")
    c=critch(self)
    
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    base=round(150*(self.hp/self.maxhp))
    other.hp-=special(self.level,self.spatk,other.spdef,base,a,b,c,r,al)
def waterspout (self,other):
    self.atktype="Water"
    al=1
    w=weathereff(self)
    r=randroll()
    print(f"{self.name} used Water Spout.")
    c=critch(self)
    
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    base=round(150*(self.hp/self.maxhp))
    other.hp-=special(self.level,self.spatk,other.spdef,base,a,b,c,r,al,w)    
def moonblast(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used Moon Blast.")
    c=critch(self)
    self.atktype="Fairy"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al)       
    ch=random.randint(1,100)
    if ch>70 and self.ability!="Sheer Force":
        spatkchange (other,-0.5)
        print(f"{other.name}: Special Attack x{other.spatkb}")
def sludgebomb(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used Sludge Bomb.")
    c=critch(self)
    self.atktype="Poison"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al)                
    ch=random.randint(1,100)
    if ch>90 and other.status=="Alive" and other.type1!="Steel" and other.type2!="Steel" and other.type1!="Poison" and other.type2!="Poison" and other.ability!="Immunity":
        other.status="Badly Poisoned"
def hydropump(self,other):
    w=weathereff(self)
    al=1
    r=randroll()
    print(f"{self.name} used Hydro Pump.")
    self.atktype="Water"
    c=critch(self)
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,110,a,b,c,r,al,w)  
def hydrocannon(self,other):
    self.atktype="Water"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f"{self.name} used Hydro Cannon.")
    
    c=critch(self)
    ab=weakness(self,other)
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
    c=critch(self)
    self.atktype="Ground"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al)
    ch=random.randint(1,100)
    if ch>90 and self.ability!="Sheer Force":
        spdefchange (other,-0.5)
        print(f"{other.name}: Special Defense x{other.spdefb}")
#EARTHQUAKE        
def earthquake (self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Earthquake.")
    c=critch(self)
    self.atktype="Ground"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,100,a,b,c,r,al)
def liquidation (self,other):
    self.atktype="Water"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f"{self.name} used Liquidation.")
    c=critch(self)
    
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al,w)    
    ch=random.randint(1,100)
    if ch>80:
        defchange (other,-0.5)
        print(f"{other.name}: Defense x{other.defb}")
def dynapunch(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Dynamic Punch.")
    c=critch(self)
    self.atktype="Fighting"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,100,a,b,c,r,al)      
def closecombat(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Close Combat.")
    c=critch(self)
    self.atktype="Fighting"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,120,a,b,c,r,al)       
    defchange(self,-0.5)
    spdefchange(self,-0.5)
    print(f"Defense x{self.defb}")
    print(f"Special Defense x{self.spdefb}")
def bulletpunch(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Bullet Punch.")
    c=critch(self)
    self.atktype="Steel"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]
    base=40
    if self.ability=="Technician":
        print(f"{self.name}'s {self.ability}.")
        base*=1.5
    other.hp-=physical (self.level,self.atk,other.defense,base,a,b,c,r,al)        
    speedchange(self,0.5)
    print(f"Speed x{self.speedb}")
def voltswitch(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Volt Switch.")
    c=critch(self)
    self.atktype="Electric"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,70,a,b,c,r,al)       
def flipturn(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Flip Turn.")
    c=critch(self)
    self.atktype="Water"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,70,a,b,c,r,al)         
def uturn(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used U-Turn.")
    c=critch(self)
    self.atktype="Bug"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,70,a,b,c,r,al)               
def xscissor (self,other):
    al=1
    r=randroll()
    print(f"{self.name} used X-Scissor.")
    c=critch(self)
    self.atktype="Bug"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,90,a,b,c,r,al)           
def superpower(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Superpower.")
    c=critch(self)
    self.atktype="Fighting"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,120,a,b,c,r,al)   
    defchange(self,-0.5)
    atkchange(self,-0.5)
    print(f"Attack x{self.atkb}")
    print(f"Defense x{self.defb}")
    
def dragonhammer(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Dragon Hammer.")
    c=critch(self)
    self.atktype="Dragon"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,120,a,b,c,r,al)        
def lightscreen(self,other):    
    print(f"{self.name} used Light Screen.")
    spatkchange(other,-1)
def reflect(self,other):    
    print(f"{self.name} used Reflect.")
    atkchange(other,-1)   
def zenheadbutt(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Zen Headbutt.")
    c=critch(self)
    self.atktype="Psychic"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)  
    ch=random.randint(1,100)
    if ch>80:
        other.flinch=True
def iciclecrash(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Icicle Crash.")
    c=critch(self)
    self.atktype="Ice"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,85,a,b,c,r,al)  
    ch=random.randint(1,100)
    if ch>70:
        other.flinch=True
def firepunch(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Fire Punch.")
    c=critch(self)
    self.atktype="Fire"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)      
    ch=random.randint(1,100)
    if ch>90 and other.status=="Alive":
        other.status="Burned"
        other.atk*=0.5
def flareblitz(self,other):
    self.atktype="Fire"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f"{self.name} used Flare Blitz")
    c=critch(self)
    
    ab=weakness(self,other)
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
    if ch>90 and other.status=="Alive":
        other.status="Burned"
        print(f"{other.name} was burned.")
        other.atk*=0.5 
def tpunch(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Thunder Punch.")
    c=critch(self)
    self.atktype="Electric"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)  
    ch=random.randint(1,100)
    if ch>90 and other.status=="Alive":
        other.status="Paralyzed"
        print(f"{other.name} is paralyzed.")
        other.speed*=0.5
def machpunch(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Mach Punch.")
    c=critch(self)
    self.atktype="Fighting"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,40,a,b,c,r,al)          
    speedchange(self,0.5)
    print(f"Speed x{self.speedb}")
def drainpunch(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Drain Punch.")
    c=critch(self)
    self.atktype="Fighting"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,75,a,b,c,r,al)      
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
    c=critch(self)
    self.atktype="Normal"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)
def strength (self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Strength.")
    c=critch(self)
    self.atktype="Normal"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)          
def icepunch(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Ice Punch.")
    c=critch(self)
    self.atktype="Ice"
    ab=weakness(self,other)
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
    c=critch(self)
    self.atktype="Normal"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)     
    ch=random.randint(1,100)
    if ch>70 and other.status=="Alive":
        other.status="Paralyzed"
        print(f"{other.name} is paralyzed.")
        other.speed*=0.5
def forcepalm(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Force Palm.")
    c=critch(self)
    self.atktype="Fighting"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,60,a,b,c,r,al)     
    ch=random.randint(1,100)
    if ch>70 and other.status=="Alive":
        other.status="Paralyzed"
        print(f"{other.name} is paralyzed.")
        other.speed*=0.5        
def drillrun(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Drill Run.")
    c=critch(self,2)
    self.atktype="Ground"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)     
def headsmash(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Head Smash.")
    c=critch(self)
    self.atktype="Rock"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,150,a,b,c,r,al)       
    if other.hp<dmg:
        dmg=other.hp
    else:
        other.hp-=dmg        
    if self.ability!="Rock Head":
        self.hp-=dmg/2
def bravebird(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Brave Bird.")
    c=critch(self)
    self.atktype="Flying"
    ab=weakness(self,other)
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
    c=critch(self,2)
    self.atktype="Flying"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,150,a,b,c,r,al)               
def crunch(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Crunch.")
    c=critch(self)
    self.atktype="Dark"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)
    ch=random.randint(1,100)
    if ch>80:
        defchange(other,-0.5)
        print (f"{other.name}: Defense x{other.defb}")
def playrough(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Play Rough.")
    c=critch(self)
    self.atktype="Fairy"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)                      
    ch=random.randint(1,10)
    if ch==7:
        atkchange(other,-0.5)
        print (f"{other.name}: Attack x{other.atkb}")
def powerwhip(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Power Whip.")
    c=critch(self)
    self.atktype="Grass"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)        
def aquatail(self,other):
    w=weathereff(self)
    al=1
    r=randroll()
    print(f"{self.name} used Aqua Tail.")
    c=critch(self)
    self.atktype="Water"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al,w)         
def dragonclaw(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Dragon Claw.")
    c=critch(self)
    self.atktype="Dragon"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)   
def fakeout(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Fake Out.")
    c=critch(self)
    self.atktype="Normal"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,40,a,b,c,r,al)         
    if self.speed>other.speed:
        ch=random.randint(1,2)            
        if ch==1:
            other.flinch=True 
def eggbomb(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Egg Bomb.")
    c=critch(self)
    self.atktype="Normal"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)  
def knockoff(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Knock Off.")
    c=critch(self)
    self.atktype="Dark"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    base=65
    if "Mega " in other.name or "Z-Crystal" in other.name:
        base=130
    other.hp-=physical (self.level,self.atk,other.defense,base,a,b,c,r,al)      
def crushclaw(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Crush Claw.")
    c=critch(self)
    self.atktype="Normal"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)      
    ch=random.randint(1,2)
    if ch==2:
        defchange(other,-0.5)
        print(f"{other.name} xDefense{other.defb}")
def seedbomb(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Seed Bomb.")
    c=critch(self)
    self.atktype="Grass"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)                  
def irontail(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Iron Tail.")
    c=critch(self)
    self.atktype="Steel"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,100,a,b,c,r,al)                 
    ch=random.randint(1,100)
    if ch>70:
        other.flinch=True
def ironhead    (self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Iron Head.")
    c=critch(self)
    self.atktype="Steel"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)              
def meteormash(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Meteor Mash.")
    c=critch(self)
    self.atktype="Steel"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,90,a,b,c,r,al)    
    other.hp-=dmg  
    ch=random.randint(1,100)
    if ch<80:
        atkchange(self,0.5)
        print(f"Attack x{self.atkb}")           
def hammerarm(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Hammer Arm.")
    c=critch(self)
    self.atktype="Fighting"
    ab=weakness(self,other)
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
    c=critch(self)
    self.atktype="Fighting"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,40,a,b,c,r,al)     
    other.hp-=dmg  
    atkchange(self,0.5)
    print(f"Attack x{self.atkb}")
    if other.ability=="Parental Bond":
        dmg=dmg/2
        other.hp-=dmg
        atkchange(self,0.5)
        print(f"Attack x{self.atkb}")
def doubleedge(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Double Edge.")
    c=critch(self)
    self.atktype="Normal"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,100,a,b,c,r,al) 
    if dmg>other.hp:
        dmg=other.hp
        other.hp=0
    else:
        other.hp-=dmg
    if self.ability!="Rock Head":
        self.hp-=round(dmg/3)
        print(f"{self.name} was hurt by recoil.")
def extemespeed(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Extreme Speed.")
    c=critch(self)
    self.atktype="Normal"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)              
def crabhammer(self,other):
    self.atktype="Water"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f"{self.name} used Crabhammer.")
    c=critch(self,2)
    
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,100,a,b,c,r,al,w)  
def slash(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Slash.")
    c=critch(self,2)
    self.atktype="Normal"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,70,a,b,c,r,al) 
def nightslash(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Night Slash.")
    c=critch(self,2)
    self.atktype="Dark"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,70,a,b,c,r,al)        
def psychocut(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Psycho Cut.")
    c=critch(self,2)
    self.atktype="Psychic"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,70,a,b,c,r,al)   
def wickedblow(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Wicked Blow.")
    c=critch(self,16)
    self.atktype="Dark"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)   
def surgingstrikes(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Surging Strikes.")
    c=critch(self,16)
    self.atktype="Water"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,75,a,b,c,r,al)                    
def dragonascent(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Dragon Ascent.")
    c=critch(self)
    self.atktype="Flying"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,120,a,b,c,r,al)     
    defchange(self,-0.5)
    spdefchange(self,-0.5)
    print(f"Defense x{self.defb}")
    print(f"Special Defense x{self.spdefb}")
def raindance(self):
    print(f"{self.name} used Rain Dance.")
    if Pokemon2.weather not in ["Desolate Land","Primordial Sea","Strong Wind","Rainy"]  and Pokemon2.weather not in ["Desolate Land","Primordial Sea","Strong Wind","Rainy"]:
        print(f"{self.name} made it rain.")
        Pokemon2.weather=Pokemon.weather="Rainy"
    else:
        print("It failed.")        
def sunnyday(self):
    print(f"{self.name} used Sunny Day.")
    if Pokemon2.weather not in ["Desolate Land","Primordial Sea","Strong Wind","Sunny"]  and Pokemon2.weather not in ["Desolate Land","Primordial Sea","Strong Wind","Sunny"]:
        print(f"{self.name} made the sunlight harsh.")
        Pokemon2.weather=Pokemon.weather="Sunny"
    else:
        print("It failed.")        
def sandstorm(self):
    print(f"{self.name} used Sandstorm.")
    if Pokemon2.weather not in ["Desolate Land","Primordial Sea","Strong Wind","Sandstorm"]  and Pokemon2.weather not in ["Desolate Land","Primordial Sea","Strong Wind","Sandstorm"]:
        print(f"{self.name} started a sandstorm.")
        Pokemon2.weather=Pokemon.weather="Sandstorm" 
    else:
        print("It failed.")
def hail(self):
    print(f"{self.name} used Hail.")
    if Pokemon2.weather not in ["Desolate Land","Primordial Sea","Strong Wind","Hail"]  and Pokemon2.weather not in ["Desolate Land","Primordial Sea","Strong Wind","Hail"]:
        print(f"{self.name} started a hailstorm.")
        Pokemon2.weather=Pokemon.weather="Hail"      
    else:
        print("It failed.")           
def dualwingbeat(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Dual Wingbeat.")
    c=critch(self)
    self.atktype="Flying"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)         
def precipiceblades(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Precipice Blades.")
    c=critch(self)
    self.atktype="Ground"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,120,a,b,c,r,al)         
def gigadrain(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Giga Drain.")
    c=critch(self)
    self.atktype="Grass"
    ab=weakness(self,other)
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
def surf(self,other):
    w=weathereff(self)
    al=1
    r=randroll()
    print(f"{self.name} used Surf.")
    c=critch(self)
    self.atktype="Water"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al,w)  
def dracometeor(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Draco Meteor.")
    c=critch(self)
    self.atktype="Dragon"
    ab=weakness(self,other)
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
    c=critch(self)
    
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,120,a,b,c,r,al,w)          
def apower(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Ancient Power.")
    c=critch(self)
    self.atktype="Rock"
    ab=weakness(self,other)
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
    c=critch(self)
    
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,80,a,b,c,r,al,w)            
    ch=random.randint(1,100)
    if ch>70 and other.status=="Alive":
        other.status="Burned"
        print(f"{other.name} was burned.")
        other.atk*=0.5
def scorchingsands(self,other):
    self.atktype="Ground"
    al=1
    r=randroll()
    print(f"{self.name} used Scorching Sands.")
    c=critch(self)
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al)            
    ch=random.randint(1,100)
    if ch>70 and other.status=="Alive":
        other.status="Burned"
        print(f"{other.name} was burned.")
        other.atk*=0.5        
def doomdesire(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Doom Desire.")
    c=critch(self)
    self.atktype="Steel"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,140,a,b,c,r,al)        
    
def flashcannon(self,other):
    al=1
    r=randroll()
    print(f"{self.name} used Flash Cannon.")
    c=critch(self)
    self.atktype="Steel"
    ab=weakness(self,other)
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
    c=critch(self)
    self.atktype="Psychic"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,140,a,b,c,r,al)       
    spatkchange(self,-1)
    print(f"Special Attack x{self.spatkb}")
def transform(self,other):
    print(f'{self.name} transformed into {other.name}')
    self.maxhp=other.maxhp
    self.atk=other.atk
    self.defense=other.defense
    self.spatk=other.spatk
    self.spdef=other.spdef
    self.speed=other.speed    
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
    c=critch(self)
    
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al,w)        
    ch=random.randint(1,100)
    if ch>90 and other.status=="Alive":
        other.status="Burned"
        print(f"{other.name} was burned.")
        other.atk*=0.5
def solarbeam(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f"{self.name}'s {self.ability}.")
    print(f"{self.name} used Solar Beam.")
    c=critch(self)
    self.atktype="Grass"
    ab=weakness(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,120,a,b,c,r,al)         
def terablast(self,other):
    self.atktype=self.type1
    w=weathereff(self)
    al=1
    r=randroll()
    print(f"{self.name} used Tera Blast.")
    c=critch(self)
    
    ab=weakness(self,other)
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
    c=critch(self)
    
    ab=weakness(self,other)
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
    if (Pokemon.weather =="Rainy" or Pokemon2.weather=="Rainy"):
        print("Rain continues to fall.\n")
        if mon.ability=="Swift Swim":
            print(f"{mon.name}'s {mon.ability}.")
            mon.speed=mon.maxspeed*2*mon.speedb
        if pk.ability=="Swift Swim":
            print(f"{pk.name}'s {pk.ability}.")
            pk.speed=pk.maxspeed*2*pk.speedb
    if (Pokemon.weather =="Sandstorm" or Pokemon2.weather=="Sandstorm"):
        print("The sandstorm is raging!\n")
        if mon.type1=="Rock" or mon.type2=="Rock":
            mon.spdef=mon.maxspdef*2*mon.spdefb
        if pk.type1=="Rock" or pk.type2=="Rock":
            pk.spdef=pk.maxspdef*2*pk.spdefb
    if (Pokemon.weather =="Hail" or Pokemon2.weather=="Hail"):
        print("It's hailing.\n")   
        if mon.type1=="Ice" or mon.type2=="Ice":
            mon.spdef=mon.maxspdef*2*mon.spdefb
        if pk.type1=="Ice" or pk.type2=="Ice":
            pk.spdef=pk.maxspdef*2*pk.spdefb
    if (Pokemon.weather =="Sunny" or Pokemon2.weather=="Sunny"):
        print("The sunlight is harsh.\n")        
        if mon.ability=="Chlorophyll":
            print(f"{mon.name}'s {mon.ability}.")
            mon.speed=mon.maxspeed*2*mon.speedb
        if pk.ability=="Chlorophyll":
            print(f"{pk.name}'s {pk.ability}.")
            pk.speed=pk.maxspeed*2*pk.speedb
def weatherset(mon):
    print("\n")
    if mon.ability == "Sand Stream" and Pokemon.weather not in ["Sandstorm","Primordial Sea","Desolate Land"]:
        print(f"{mon.name}'s {mon.ability} brewed a sandstorm!")
        Pokemon.weather=Pokemon2.weather="Sandstorm" 
    if mon.ability=="Primordial Sea" and Pokemon.weather!="Primordial Sea" and Pokemon2.weather!="Primordial Sea":
        print(f"{mon.name}'s {mon.ability}. A heavy rain began to fall!")
        Pokemon.weather=Pokemon2.weather="Primordial Sea"
    if mon.ability=="Desolate Land" and Pokemon.weather!="Desolate Land":
        print(f"{mon.name}'s {mon.ability}. The sunlight turned extremely harsh!")
        Pokemon.weather=Pokemon2.weather="Desolate Land"
    if mon.ability == "Drought" and Pokemon.weather not in ["Sunny","Primordial Sea","Desolate Land"]:
        print(f"{mon.name}'s {mon.ability} intensified the sun's rays!")
        Pokemon.weather=Pokemon2.weather="Sunny"
    if mon.ability == "Drizzle" and Pokemon.weather not in ["Rainy","Primordial Sea","Desolate Land"]:
        print(f"{mon.name}'s {mon.ability} made it rain!")
        Pokemon.weather=Pokemon2.weather="Rainy"
    if mon.ability == "Snow Warning" and Pokemon.weather not in ["Hail","Primordial Sea","Desolate Land"]:
        print(f"{mon.name}'s {mon.ability} whipped up a hailstorm!")
        Pokemon.weather=Pokemon2.weather="Hail"      
    
def weathereff(mon):
    if Pokemon.weather=="Desolate Land" and mon.atktype=="Water":
        print("The Water-type attack evaporated in the harsh sunlight!")
        return 0
    if Pokemon.weather=="Primordial Sea" and mon.atktype=="Fire":
        print("The Fire-type attack fizzled out in the heavy rain!")
        return 0                                 
    if (Pokemon2.weather=="Rainy" or Pokemon.weather=="Primordial Sea") and mon.atktype=="Water":
        return 1.5
    if (Pokemon2.weather=="Sunmy" or Pokemon.weather=="Sunny") and mon.atktype=="Water":
        return 0.5    
    if (Pokemon2.weather=="Rainy" or Pokemon.weather=="Rainy") and mon.atktype=="Fire":
        return 0.5      
    if (Pokemon.weather=="Sunny" or Pokemon.weather=="Desolate Land") and mon.atktype=="Fire":
        return 1.5          
    if Pokemon.weather=="Hail" and mon.atktype=="Ice":
        return 1.5          
    else:
        return 1 
        