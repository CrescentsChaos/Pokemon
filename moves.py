from colorama import init
from termcolor import colored    
from pokemonbase2 import *
from typematchup import *
from hiddenpower import *
from movelist import *
def haze(self,tr):
    print(f" 🌫️ {self.name} used "+colored(" Haze","white")+"!")
    self.atkb=1
    self.defb=1
    self.spatkb=1
    self.spdefb=1
    self.speedb=1
    other.atkb=1
    other.defb=1
    other.spatkb=1
    other.spdefb=1
    other.speedb=1
    print(" Stat boosts neutralized!")
def healbell(self,tr):
    print(f" 🔔 {self.name} used "+colored(" Heal Bell","yellow")+"!")
    for i in tr.pokemons:
        if i.ability!="Soundproof":
            i.status="Alive"    
def aromatherapy(self,tr):
    print(f" 🏵️ {self.name} used "+colored(" Aromatherapy","green")+"!")
    for i in tr.pokemons:
        if i.ability=="Sap Sipper":
            print(f" {i.name}'s {i.ability}.")
            atkchange(i,0.5)
        if i.ability!="Sap Sipper":
            i.status="Alive"
def wish(self,tr):
    print(f" 🌠 {self.name} used "+colored(" Wish","yellow")+"!")
    if tr.wishhp is False:
        tr.wishhp=self.maxhp/2
def aquaring(self):
    print(f" 💦 {self.name} used "+colored(" Aqua Ring","blue")+"!")
    self.aring=True
def doodle(self,other):
    print(f" 🎨 {self.name} used "+colored(" Doodle","white")+"!")
    self.atktype="Normal"
    self.ability=other.ability
    print (f" {self.name} gained {other.ability}.")
def painsplit(self,other):
    print(f" {self.name} used "+colored(" Pain Split","white")+"!")
    self.atktype="Normal"
    print(" The battlers shared their pain.")
    ab=weakness(self,other,field)
    a=ab[0]
    if a>0:
        self.hp=other.hp=(other.hp+self.hp)/2
def endeavor (self,other):
    print(f" {self.name} used "+colored(" Endeavor","white")+"!")
    self.atktype="Normal"
    ab=weakness(self,other,field)
    a=ab[0]
    if self.hp<other.hp and a>0:
        other.hp=self.hp
def yawn(self,other):
    print(f" 🥱 {self.name} used "+colored(" Yawn","white")+"!")
    if other.yawn is False:
        other.yawn=True
        print(f" {other.name} became drowsy!")
def spicyextract(self,other):
    print(f" 🌶️🫑 {self.name} used "+colored(" Spicy Extract","green")+"!")
    atkchange (other,1)
    print(f" {other.name}'s attack rose sharply!")
    defchange(other,-1)
    print(f" {other.name}'s defense fell harshly!")
def electricterrain(self,other, field,turn):
    self.atktype="Electric"
    print(f" {self.name} used "+colored(" Electric Terrain","yellow")+"!")
    field.terrain="Electric"
    field.eleturn=turn
    field.eleend(self,other)
    print(" ⚡ An electric current ran across the battlefield!")
    
def mistyterrain(self,other, field,turn):
    self.atktype="Fairy"
    print(f" {self.name} used "+colored(" Misty Terrain","magenta")+"!")
    field.terrain="Misty"
    field.misturn=turn
    field.misend(self,other)
    print(" 🌸 Mist swirled around the battlefield!")
    
def grassyterrain(self,other,field,turn):
    self.atktype="Grass"
    print(f" {self.name} used "+colored(" Grassy Terrain","green")+"!")
    field.terrain="Grassy"
    field.grassturn=turn
    field.grassend(self,other)
    print(" 🌿 Grass grew to cover the battlefield!")   
    
def psychicterrain(self,other, field,turn):
    self.atktype="Psychic"
    print(f" {self.name} used "+colored(" Psychic Terrain","magenta")+"!")
    field.terrain="Psychic"
    field.psyturn=turn
    field.psyend(self,other)
    print(" 👁️ The battlefield got weird!")        
def trick(self,other):
    print(f" ♻️ {self.name} used "+colored(" Trick","white")+"!")
    if other.ability!="Sticky Hold" and "m Z" not in other.item and "ite" not in other.item:
        print(f" {self.name} swapped its {self.item} with {other.name}'s {other.item}!")
        self.item,other.item=other.item,self.item
def trickortreat(self,other):
    self.atktype="Ghost"
    print(f" 🎃 {self.name} used "+colored(" Trick-or-Treat","magenta")+"!")
    other.type2=None
    other.type1="Ghost"
    print(f" {other.name} turned into {other.type1} type!")
def magicpowder(self,other):
    self.atktype="Water"
    print(f" 🔮 {self.name} used "+colored(" Magic Powder","magenta")+"!")
    other.type2=None
    other.type1="Psychic"    
    print(f" {other.name} turned into {other.type1} type!")
def tarshot(self,other):
    self.atktype="Fire"
    print(f" 🔥 {self.name} used "+colored(" Tar Shot","red")+"!")   
    speedchange (other,-0.5)
    if other.tarshot is False:
        other.tarshot=True     
def soak(self,other):
    self.atktype="Water"
    print(f" 💦 {self.name} used "+colored(" Soak","blue")+"!")
    other.type2=None
    other.type1="Water"    
    print(f" {other.name} turned into {other.type1} type!")
    
def forestscurse(self,other):
    self.atktype="Grass"
    print(f" 🌲 {self.name} used "+colored(" Forest's Curse","green")+"!")
    other.type2=None
    other.type1="Grass"    
    print(f" {other.name} turned into {other.type1} type!")
    
def magmastorm(self,other):
    self.atktype="Fire"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f" 🌋 {self.name} used "+colored(" Magma Storm","red")+"!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=special(self.level,self.spatk,other.spdef,120,a,b,c,r,al,w)
    other.hp-=dmg
    if other.status not in ["Alive","Burned"] and other.ability!="Flash Fire" and other.type1!="Fire" and other.type2!="Fire":
        other.status="Burned"
        print(f" 🔥 {other.name} was burned.")
        
def fusionflare(self,other):
    self.atktype="Fire"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Fusion Flare","red")+"!")
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
        print(f" {self.name}'s {self.ability}.")
    print(f" 🔥 {self.name} used "+colored(" Blue Flare","cyan")+"!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,130,a,b,c,r,al,w)
    ch=random.randint(1,100)
    if ch>80 and other.status is None and self.ability!="Sheer Force" and other.ability not in ["Shield Dust"]:
        other.status="Burned"
        print(f" 🔥 {other.name} was burned.")
        
def iceburn(self,other):
    self.atktype="Ice"
    w=weathereff(self)
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    print(f" ❄️🔥 {self.name} used "+colored(" Ice Burn","cyan")+"!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,140,a,b,c,r,al,w)
    ch=random.randint(1,100)
    if ch>70 and other.status is None and self.ability!="Sheer Force" and other.ability not in ["Shield Dust"]: 
        other.status="Burned"
        print(f" 🔥 {other.name} was burned.")    

def fireBlast(self,other):
    self.atktype="Fire"
    w=weathereff(self)
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    print(f" 🔥 {self.name} used "+colored(" Fire Blast","red")+"!")
    print("""      🔥                
      🔥
 🔥🔥🔥🔥🔥🔥
     🔥🔥
    🔥  🔥
   🔥    🔥"""  )
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,110,a,b,c,r,al,w)
    chance=10
    if self.ability=="Serene Grace":
        chance*=2
    if self.speed>other.speed:
        ch=random.randint(1,100)            
        if ch>(100-chance)  and other.status is None and self.ability!="Sheer Force" and other.ability not in ["Shield Dust"]:
            other.status="Burned"
            print(f" 🔥 {other.name} was burned.")
def searingshot(self,other):
    self.atktype="Fire"
    w=weathereff(self)
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    print(f" 🔥 {self.name} used "+colored(" Searing Shot","red")+"!")
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,100,a,b,c,r,al,w)
    ch=random.randint(1,10)
    if ch>7 and other.status is None and self.ability!="Sheer Force" and other.ability not in ["Shield Dust"]:
        other.status="Burned"
        print(f" 🔥 {other.name} was burned.")        
def fierywrath(self,other):
    self.atktype="Dark"
    w=weathereff(self)
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    print(f" 🌑🔥 {self.name} used "+colored(" Fiery Wrath","red")+"!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al,w)
    ch=random.randint(1,100)
    if ch>80 and self.ability!="Sheer Force" and other.ability not in ["Inner Focus","Shield Dust"]:
        other.flinched=True        
def vcreate(self,other):
    self.atktype="Fire"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f" 🔥 {self.name} used "+colored(" V-Create","red")+"!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,180,a,b,c,r,al,w)    
    defchange(self,-0.5)
    spdefchange (self,-0.5)
    speedchange (self,-0.5)
    print(f" {self.name}'s Defense, Special Defense and Speed fell!"    )
def steameruption(self,other):
    self.atktype="Water"
    w=weathereff(self)
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    print(f" 🌋🌊 {self.name} used Steam Eruption!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,110,a,b,c,r,al,w)
    ch=random.randint(1,100)
    if ch>70 and other.status is None and self.ability!="Sheer Force" and other.status=="Alive" and other.ability not in ["Shield Dust"]:
        other.status="Burned"
        print(f" 🔥 {other.name} was burned.")
          
def pyroball(self,other):
    self.atktype="Fire"
    w=weathereff(self)
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    print(f" 🔥⚽  {self.name} used "+colored(" Pyro Ball","red")+"!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,120,a,b,c,r,al,w)
    ch=random.randint(1,10)
    if ch==1 and other.status is None and self.ability!="Sheer Force" and other.ability not in ["Shield Dust"]:
        other.status="Burned"
        print(f" 🔥 {other.name} was burned.")
def struggle(self,other):
    self.atktype="None"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f" 😣 {self.name} used "+colored(" Struggle","white")+"!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,50,a,b,c,r,al,w)     
    self.hp-=(self.maxhp/8)    
def fierydance(self,other):
    self.atktype="Fire"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f" 🔥🪰 {self.name} used "+colored(" Fiery Dance","red")+"!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,80,a,b,c,r,al,w)        
    ch=random.randint(1,2)
    if ch==1:
        spatkchange(self,0.5)
        print(f" Special Attack x{self.spatkb}")
        
def rest(self):
    print(f" 😪 {self.name} used "+colored(" Rest","magenta")+"!")
    if self.status!="Sleep" and self.hp!=self.maxhp:
        self.status="Sleep"
        print(f" {self.name} fell asleep.")
        self.hp=self.maxhp
        
def lusterpurge(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    print(f" ✈️ {self.name} used "+colored(" Luster Purge","magenta")+"!")
    self.atktype="Psychic"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al)
    ch=random.randint(1,2)
    if ch==2 and self.ability=="Sheer Force" and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil","Shield Dust"]:
        spdefchange(other,-0.5)
        print(f" {other.name}: Special Defense x"+str(other.spdefb))
        
def mistball(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    print(f" 🔮 {self.name} used "+colored(" Mist Ball","magenta")+"!")
    self.atktype="Psychic"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al)
    ch=random.randint(1,2)
    if ch==2 and self.ability=="Sheer Force" and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil","Shield Dust"]:
        spatkchange(other,-0.5)
        print(f" {other.name}: Special Attack x"+str(other.spatkb))
def luminacrash(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    print(f" 👁️ {self.name} used "+colored(" Lumina Crash","magenta")+"!")
    self.atktype="Psychic"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,80,a,b,c,r,al)
    if other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        spdefchange(other,-1)
        print(f" {other.name}: Special Defense x"+str(other.spdefb))        
def psychic(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    print(f" 👁️ {self.name} used "+colored(" Psychic","magenta")+"!")
    self.atktype="Psychic"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al)
    chance=10
    if self.ability=="Serene Grace":
        chance*=2
    if self.speed>other.speed:
        ch=random.randint(1,100)            
        if ch>(100-chance) and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil","Shield Dust"]:
            spdefchange(other,-0.5)
            print(f" {other.name}: Special Defense x"+str(other.spdefb))
        
def bellydrum(self):
    print(f" 🩸🪘 {self.name} used "+colored(" Belly Drum","red")+"!")
    if self.hp>(self.maxhp/2):
        atkchange(self,4)
        self.hp-=(self.maxhp/2)
        print(f" {self.name} cuts its own HP and maximized its Attack.")
        print(f" Attack x{self.atkb}")     
    else:
        print ( "It failed.")    
        
def superfang(self,other):        
    print(f" 🦷 {self.name} used "+colored(" Super Fang","white")+"!")
    ab=weakness(self,other,field)
    a=ab[0]
    other.hp-=a*(round(other.hp/2))
def charm(self,other):
    print(f" 🥰 {self.name} used "+colored(" Charm","magenta")+"!")
    atkchange(self,-1)
    print(f" {other.name}: Attack x{other.atkb}")    
def swordsdance(self):
    print(f" ⚔️ {self.name} used Swords Dance.")
    atkchange(self,1)
    print(f" Attack x{self.atkb}")
def filletaway(self):
    print(f" 🐟 {self.name} used "+colored(" Fillet Away","blue")+"!")
    atkchange(self,1)
    spatkchange(self,1)
    speedchange(self,1)
    self.hp-=self.maxhp/2
    print(f" Attack x{self.atkb}")    
    print(f" Special Attack x{self.spatkb}")
    print(f" Speed x{self.speedb}")    
def curse(self):
    print(f" {self.name} used "+colored(" Curse","red")+"!")
    atkchange(self,0.5)
    defchange(self,0.5)
    speedchange(self,-0.5)
    print(f" Attack x{self.atkb}")    
    print(f" Defense x{self.defb}")
    print(f" Speed x{self.speedb}")
    
def tailglow(self):
    print(f" {self.name} used Tail Glow.")
    spatkchange(self,1.5)
    print(f" Special Attack x{self.spatkb}")     
       
def nastyplot(self):
    print(f" ❔ {self.name} used "+colored(" Nasty Plot","red")+"!")
    print(""" ❔❔❔❔❔""")
    spatkchange(self,1)
    print(f" Special Attack x{self.spatkb}")    
    
def calmmind(self):
    print(f" 👁️ {self.name} used "+colored(" Calm Mind","magenta")+"!")
    spatkchange(self,0.5)
    spdefchange(self,0.5)
    print(f" Special Attack x{self.spatkb}")      
    print(f" Special Defense x{self.spdefb}")    
def corrosivegas(self):
    print(f" 🥽 {self.name} used "+colored(" Corrosive Gas","magenta")+"!")
    if other.item!=None:
        print (f" {self.name}'s corrosive gas melted {other.name}'s {other.item}!")
        other.item=None        
def acidarmor(self):
    print(f" 💦 {self.name} used "+colored(" Acid Armor","blue")+"!")
    defchange(self,1)
    print(f" Defense x{self.defb}")    
      
def shelter(self):
    print(f" 🐚 {self.name} used "+colored(" Shelter","white")+"!")   
    defchange(self,1)
    print(f" Defense x{self.defb}")   
def cosmicpower(self):
    print(f" 🌌 {self.name} used "+colored(" Cosmic Power","yellow")+"!")
    defchange(self,0.5)
    print(f" Defense x{self.defb}")      
    spdefchange(self,0.5)
    print(f" Special Defense x{self.spdefb}")  
def amnesia(self):
    print(f" ❓ {self.name} used "+colored(" Amnesia","magenta")+"!")  
    spdefchange(self,1)
    print(f" Special Defense x{self.spdefb}")     
def acidspray(self):
    al=1
    r=randroll()
    print(f" 🧯 {self.name} used "+colored(" Acid Spray","magenta")+"!")
    self.atktype="Poison"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,40,a,b,c,r,al)   
    spdefchange(self,-1)
    print(f" {other.name} Special Defense x{self.spdefb}")      
def agility(self):
    print(f" ⚡ {self.name} used "+colored(" Agility","magenta")+"!")
    speedchange(self,1)
    print(f" Speed x{self.speedb}")    
def rockpolish(self):
    print(f" 🪨🌟 {self.name} used "+colored(" Rock Polish","yellow")+"!")
    speedchange(self,1)
    print(f" Speed x{self.speedb}")    
def irondefense(self):
    print(f" ⛑️ {self.name} used "+colored(" Iron Defense","white")+"!")
    defchange(self,1)
    print(f" Defense x{self.defb}") 
     
def cottonguard(self):
    print(f" 🧶 {self.name} used "+colored(" Cotton Guard","green")+"!")
    defchange(self,1.5)
    print(f" Defense x{self.defb}")     
def leechseed(self,other):
    print(f" 🌱 {self.name} used "+colored(" Leech Seed","green")+"!")
    if "Grass" not in (other.type1,other.type2,other.teratype) and other.ability!="Magic Bounce" and other.seeded is False:
        other.seeded=True
        print(f" 🌱{other.name} was seeded.")
    elif "Grass" not in (self.type1,self.type2)and other.ability=="Magic Bounce" and self.seeded is False:
        self.seeded=True
        print(f" {self.name} was seeded.")
    
def strengthsap(self,other):
    print(f" 🌱 {self.name} used "+colored(" Strength Sap","green")+"!")
    if other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        prevatk=other.atk
        atkchange(other,-0.5)
        heal=prevatk
        print(f" {other.name}: Attack x{other.atkb}")  
        if heal<=(self.maxhp-heal):
            self.hp+=heal
        else:
            self.hp=self.maxhp
    else:
        print (" It Failed!")
        
def defendorder(self):
    print(f" 🐝🛡️ {self.name} used "+colored(" Defend Order","green")+"!")
    spdefchange(self,0.5)     
    defchange(self,0.5)   
    print(f" Defense x{self.defb}")    
    print(f" Special Defense x{self.spdefb}")
    
def toxicthread(self,other):
    print(f" 🕷️🕸️ {self.name} used "+colored(" Toxic Thread","magenta")+"!")
    if other.status=="Alive" and other.type1 not in ["Steel","Poison"] and other.type2 not in ["Steel","Poison"] and other.ability not in ["Immunity","Magic Bounce"]:
        other.status="Badly Poisoned"
        print(f" ☠️ {other.name} was badly poisoned.")
    speedchange(other,-0.5)     
    print(f" {other.name}: Speed x{self.speedb}")
    
def bulkup(self):
    print(f" 💪🏻 {self.name} used "+colored(" Bulk Up","red")+"!")
    atkchange(self,0.5)     
    defchange(self,0.5)   
    print(f" Attack x{self.atkb}")   
    print(f" Defense x{self.defb}")       
    
def skullbash(self,other):       
    print(f" ⛑️ {self.name} used "+colored(" Skull Bash","white")+"!")
    if self.item=="Power Herb" or self.precharge is True:
        if self.item=="Power Herb":
            self.item=None  
            atkchange(self,0.5)
            defchange(self,0.5)
            print(f" {self.name} became fully charged due to its Power Herb.")
            print(f" Attack x{self.atkb}")
            print(f" Defense x{self.defb}")
        al=1
        r=randroll()
        self.atktype="Normal"
        c=critch(self,other)
        ab=weakness(self,other,field)
        a=ab[0]
        b=ab[1]   
        other.hp-=special(self.level,self.spatk,other.spdef,130,a,b,c,r,al)    
        self.precharge=False
    else:
        print(f" {self.name} lowered it's head.")
        atkchange(self,0.5)
        defchange(self,0.5)
        print(f" Attack x{self.atkb}")
        print(f" Defense x{self.defb}")
        self.precharge=True    
        
def meteorbeam(self,other):       
    print(f" ☄️ {self.name} used "+colored(" Meteor Beam","yellow")+"!")
    if self.item=="Power Herb" or self.precharge is True:
        if self.item=="Power Herb":
            self.item=None  
            spatkchange(self,0.5)
            print(f" {self.name} became fully charged due to its Power Herb.")
            print(f" Special Attack x{self.spatkb}")
        al=1
        r=randroll()
        self.atktype="Rock"
        c=critch(self,other)
        ab=weakness(self,other,field)
        a=ab[0]
        b=ab[1]   
        other.hp-=special(self.level,self.spatk,other.spdef,120,a,b,c,r,al)    
        self.precharge=False
    else:
        print(f" {self.name} absorbing its power.")
        spatkchange(self,0.5)
        print(f" Special Attack x{self.spatkb}")
        self.precharge=True
        
def geomancy(self):
    print(f" 🌈 {self.name} used "+colored(" Geomancy","magenta")+"!")
    if self.item=="Power Herb":
        print(f" {self.name} became fully charged due to its Power Herb.")
        spatkchange(self,1)     
        spdefchange(self,1)   
        speedchange(self,1)
        print(f" Special Attack x{self.spatkb}")   
        print(f" Special Defense x{self.spdefb}")   
        print(f" Speed x{self.speedb}")      
        self.precharge=False
        self.item=None
    else:
        print(f" {self.name} absorbing its power.")
        self.precharge=True
def coil(self):
    print(f" 🐍 {self.name} used "+colored(" Coil","green")+"!")
    atkchange(self,0.5)     
    defchange(self,0.5)   
    print(f" Attack x{self.atkb}")   
    print(f" Defense x{self.defb}")  
    
def autotomize(self):
    print(f" 🔩 {self.name} used "+colored(" Autotomize","white")+"!")
    speedchange(self,1)
    print(f" Speed x{self.speedb}")
def mortalspin(self,other,tr1):
    print(f" 🥏 {self.name} used "+colored(" Mortal Spin","magenta")+"!")
    self.atktype="Poison"
    if other.status=="Alive":
        print(f" ☠️ {other.name} was badly poisoned.")
        other.status=random.choice(["Badly Poisoned"])  
    if self.seeded is True:
        self.seeded=False
    if len(tr1.hazard)>0:
        tr1.hazard=None
        print(f" {self.name} removed hazards from its side!")   
def tidyup(self,other,tr1):
    print(f" 🧹 {self.name} used "+colored(" Tidu Up","white")+"!")
    tr1.hazard=[]       
    atkchange(self,0.5)
    speedchange(self,0.5)
def rapidspin(self,other,tr1):
    print(f" 🥏 {self.name} used "+colored(" Rapid Spin","white")+"!")
    self.atktype="Normal"
    al=1
    r=randroll()
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    base=20
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    other.hp-=physical(self.level,self.atk,other.defense,base,a,b,c,r,al)      
    speedchange(self,0.5)
    print(f" Speed x{self.speedb}")    
    if len(tr1.hazard)>0:
        tr1.hazard=[]
        print(f" {self.name} removed hazards from its side!")
        
def dragondance(self):
    print(f" 🐉 {self.name} used "+colored(" Dragon Dance","red")+"!")   
    atkchange(self,0.5)
    speedchange(self,0.5)
    print(f" Attack x{self.atkb}")   
    print(f" Speed x{self.speedb}")
    
def quiverdance(self):
    print(f" 🦋 {self.name} used "+colored(" Quiver Dance","green")+"!")
    spatkchange(self,0.5)
    speedchange(self,0.5)
    spdefchange(self,0.5)
    print(f" Special Attack x{self.spatkb}")   
    print(f" Special Defense x{self.spdefb}")  
    print(f" Speed x{self.speedb}") 
              
def shellsmash(self):
    print(f" 🐚 {self.name} used "+colored(" Shell Smash","blue")+"!")
    atkchange(self,1)
    spatkchange(self,1)
    speedchange(self,1)
    defchange(self,-0.5)
    spdefchange(self,-0.5)
    print(f" Attack x{self.atkb}")   
    print(f" Special Attack x{self.spatkb}")   
    print(f" Speed x{self.speedb}")       
    print(f" Defense x{self.defb}")    
    print(f" Special Defense x{self.spdefb}")     
       
def infernooverdrive(self,other):
    self.atktype="Fire"
    al=1
    r=randroll()
    print(f" 🔥💥 {self.name} used "+colored(" Inferno Overdrive","red")+"!")
    w=weathereff(self)
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al,w)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al,w)   
        
def gmaxcentiferno(self,other):
    self.atktype="Fire"
    al=1
    w=weathereff(self)
    r=randroll()
    print(f" 🔺㊗️ {self.name} used "+colored(" G-Max Centiferno","red")+"!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al,w)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al,w)    
    if other.status=="Alive":
        other.status="Burned"        
        print(f" 🔥 {other.name} was burned.")
        
def gmaxwildfire(self,other):
    self.atktype="Fire"
    al=1
    w=weathereff(self)
    r=randroll()
    print(f" 🔺🔥 {self.name} used "+colored(" G-Max Wildfire","red")+"!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al,w)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al,w)    
    if other.status=="Alive":
        other.status="Burned"
        print(f" 🔥 {other.name} was burned.")
        
def naturesmadness(self,other):
    print(f" 🏝️ {self.name} used used "+colored(" Nature's Madness","magenta")+"!")
    self.atktype="Fairy"
    other.hp-=round(other.hp/2)
    
def gmaxbefuddle(self,other):
    self.atktype="Bug"
    al=1
    r=randroll()
    print(f" 🔺🦋 {self.name} used "+colored(" G-Max Befuddle","green")+"!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al)    
    if other.status=="Alive":
        other.status=random.choice(["Paralyzed","Badly Poisoned","Sleep"])
        
def gmaxdrumsolo(self,other):
    self.atktype="Grass"
    al=1
    r=randroll()
    w=weathereff(self)
    print(f" 🔺🥁 {self.name} used "+colored(" G-Max Drum Solo","green")+"!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if a==0:
        print(f" G-Max Drum Solo negates {other.name}'s ability!")
        a=1
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al,w)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al,w)           
        
def gmaxstonesurge(self,other,tr):
    self.atktype="Water"
    al=1
    r=randroll()
    w=weathereff(self)
    print(f" 🔺🪨🌊 {self.name} used "+colored(" G-Max Stonesurge","blue")+"!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al,w)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al,w)            
    if "Stealth Rock" not in tr.hazard:
        tr.hazard.append("Stealth Rock")
        print(" Pointed stones float in the air around the opposing team!")
        
def gmaxhydrosnipe(self,other):
    self.atktype="Water"
    al=1
    r=randroll()
    w=weathereff(self)
    print(f" 🔺🎯☄️ {self.name} used "+colored(" G-Max Hydrosnipe","blue")+"!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if a==0:
        print(f" G-Max Hydrosnipe negates {other.name}'s ability!")
        a=1
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al,w)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al,w)  
        
def gmaxfoamburst(self,other):
    self.atktype="Water"
    al=1
    r=randroll()
    w=weathereff(self)
    print(f" 🔺🧼 {self.name} used "+colored(" G-Max Foam Burst","blue")+"!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al,w)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al,w)     
    speedchange(other,-1)         
           
def gmaxcannonade(self,other):
    self.atktype="Water"
    al=1
    r=randroll()
    w=weathereff(self)
    print(f" 🔺💣🌊 {self.name} used "+colored(" G-Max Cannonade","blue")+"!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al,w)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al,w)     
    if other.status=="Alive":
        other.status="Frostbite"      
        
def hydrovortex(self,other):
    self.atktype="Water"
    al=1
    r=randroll()
    print(f" 🌊🌪️ {self.name} used "+colored(" Hydro Vortex","blue")+"!")
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
    print(f" 🌳💥 {self.name} used "+colored(" Bloom Doom","green")+"!")
    self.atktype="Grass"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)        
def gmaxvinelash(self,other):
    al=1
    r=randroll()
    print(f" 🔺🌿 {self.name} used "+colored(" G-Max Vine Lash","green")+"!")
    self.atktype="Grass"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al)        
    other.seeded=True 
def maxovergrowth(self,other,turn):
    al=1
    r=randroll()
    print(f" 🔺🌳 {self.name} used "+colored(" Max Overgrowth","green")+"!")
    self.atktype="Grass"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al)         
    if field.terrain!="Grassy":
        field.terrain="Grassy"   
        field.grassturn=turn
        field.grassend(self,other)
        print(" 🌿 Grass grew to cover the battlefield!")    
        
def maxlightning (self,other,turn):
    al=1
    r=randroll()
    print(f" 🔺⚡  {self.name} used"+colored(" Max Lightning","yellow")+"!")
    self.atktype="Electric"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al)      
    if field.terrain!="Electric":
        field.terrain="Electric"  
        field.eleturn=turn
        field.eleend(self,other)
        print(" ⚡ An electric current ran across the battlefield!")
        
def gmaxstunshock(self,other):
    al=1
    r=randroll()
    print(f" 🔺☣️⚡ {self.name} used "+colored(" G-Max Stun Shock","yellow")+"!")
    self.atktype="Electric"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al)                
    if other.status=="Alive" and a!=0:
        other.status=random.choice(["Paralyzed","Badly Poisoned"])       
        
def gmaxvoltcrash(self,other):
    al=1
    r=randroll()
    print(f" 🔺⚡ {self.name} used "+colored(" G-Max Volt Crash","yellow")+"!")
    self.atktype="Electric"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al)                
    if other.status=="Alive" and a!=0:
        other.status="Paralyzed"
        
def gigavolthavoc(self,other):
    al=1
    r=randroll()
    print(f" ⚡💥 {self.name} used "+colored(" Gigavolt Havoc","yellow")+"!")
    self.atktype="Electric"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)  
def exevoboost(self):
    print(f" 🌈 {self.name} used "+colored(" Extreme Evoboost","white")+"!")
    atkchange(self,1)
    defchange(self,1)
    spatkchange (self,1)
    spdefchange (self,1)
    speedchange (self,1)
    print(f" {self.name} sharply boosted all of its stats!")
        
def sparksurf(self,other):
    al=1
    r=randroll()
    print(f" ⚡🏄 {self.name} used "+colored(" Stoked Sparksurfer","yellow")+"!")
    self.atktype="Electric"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,175,a,b,c,r,al)            
def tenmvolttb(self,other):
    al=1
    r=randroll()
    print(f" ⚡💥 {self.name} used "+colored(" 10,000,000 Volt Thunderbolt","yellow")+"!")
    self.atktype="Electric"
    c=critch(self,other,2)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)
def catastropika(self,other):
    al=1
    r=randroll()
    print(f" ⚡💥 {self.name} used "+colored(" Catastropika","yellow")+"!")
    self.atktype="Electric"
    c=critch(self,other,2)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,210,a,b,c,r,al)              
       
def stormshards(self,other):
    al=1
    r=randroll()
    print(f" 🪨☄️ {self.name} used "+colored(" Splintered Stormshards","yellow")+"!")   
    self.atktype="Rock"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    field.terrain="Normal"
    other.hp-=physical(self.level,self.atk,other.defense,190,a,b,c,r,al)           
        
def gmaxvolcalith(self,other):
    al=1
    r=randroll()
    print(f" 🔺🪨🔥 {self.name} used "+colored(" G-Max Volcalith","red")+"!")   
    self.atktype="Rock"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al)          
    if other.status=="Alive":
        other.status="Burned"       
        print(f" 🔥 {other.name} was burned.") 
         
def continentalcrush(self,other):
    al=1
    r=randroll()
    print(f" 🌏🪨 {self.name} used "+colored(" Continental Crush","yellow")+"!")   
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
    print(f" ⛰️ {self.name} used "+colored(" Tectonic Rage","yellow")+"!")
    self.atktype="Ground"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)   
        
def maxquake(self,other):
    al=1
    r=randroll()
    print(f" 🔺⛰️ {self.name} used "+colored(" Max Quake","yellow")+"!")
    self.atktype="Ground"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al)            
    spdefchange(self,0.5)       
    print(f" {self.name}'s special defense rose!")          
def corkscrewcrash(self,other):
    al=1
    r=randroll()
    print(f" 🔩💥 {self.name} used "+colored(" Corkscrew Crash","white")+"!")
    self.atktype="Steel"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)          
def searingsunrazesmash(self,other):
    al=1
    r=randroll()
    print(f" ☀️💥 {self.name} used "+colored(" Searing Sunraze Smash","white")+"!")
    self.atktype="Steel"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if a==0:
        print(f" Searing Sunraze Smash negates {other.name}'s ability!")
        a=1
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)      
def menacingmoonrazemaelstrom(self,other):
    al=1
    r=randroll()
    print(f" 🌘💥 {self.name} used "+colored(" Menacing Moonraze Maelstrom","magenta")+"!")
    self.atktype="Ghost"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if a==0:
        print(f" Menacing Moonraze Maelstrom  negates {other.name}'s ability!")
        a=1
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)    
def soulstealing(self,other):
    al=1
    r=randroll()
    print(f" 👤💥 {self.name} used "+colored(" Soul-Stealing 7-Star Strike","magenta")+"!")
    self.atktype="Ghost"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)      
def moonsault(self,other):
    al=1
    r=randroll()
    print(f" 🤼‍♂️💥 {self.name} used "+colored(" Malicious Moonsault","red")+"!")
    self.atktype="Dark"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)           
def operetta(self,other):
    al=1
    r=randroll()
    print(f" 🎶💥 {self.name} used "+colored(" Oceanic Operetta","blue")+"!")
    self.atktype="Water"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)                    
def arrowraid(self,other):
    al=1
    r=randroll()
    print(f" 🎯💥 {self.name} used "+colored(" Sinister Arrow Raid","magenta")+"!")
    self.atktype="Ghost"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)      
def gmaxsteelsurge(self,other):
    al=1
    r=randroll()
    print(f" 🔺🔩 {self.name} used "+colored(" G-Max Steelsurge","white")+"!")
    self.atktype="Steel"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al)                                           
def maxsteelspike(self,other):
    al=1
    r=randroll()
    print(f" 🔺🔩 {self.name} used "+colored(" Max Steelspike","white")+"!")
    self.atktype="Steel"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al)                  
    defchange(self,0.5)
    print(f" {self.name}'s defense rose!")
def gmaxmeltdown(self,other):
    al=1
    r=randroll()
    print(f" 🔺🔩 {self.name} used "+colored(" G-Max Meltdown","white")+"!")
    self.atktype="Steel"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al)     
def breakneckblitz(self,other):
    al=1
    r=randroll()
    print(f" ⚡ {self.name} "+colored(" Breakneck Blitz","white")+"!")
    self.atktype="Normal"
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
    print(f" 🥞 {self.name} used "+colored(" Pulverizing Pancake","white")+"!")
    self.atktype="Normal"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spdef>self.defense:
        other.hp-=special(self.level,self.spdef,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.defense,other.defense,200,a,b,c,r,al)            
def gmaxreplenish(self,other):
    al=1
    r=randroll()
    print(f" 🔺🍐 {self.name} used "+colored(" G-Max Replenish","white")+"!")
    self.atktype="Normal"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al)         
    if self.item is None and self.hp<=self.maxhp-(self.maxhp/4):
        self.hp+=round(self.maxhp/4)
        print(f" {self.name} replenished it's Sitrus Berry and restored some HP!")  
def maxstrike(self,other):
    al=1
    r=randroll()
    print(f" 🔺✴️ {self.name} used "+colored(" Max Strike","white")+"!")
    self.atktype="Normal"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al)         
    speedchange (other,-0.5)    
    print(f" {other.name}'s speed fell!")
def gmaxgoldrush(self,other):
    al=1
    r=randroll()
    print(f" 🔺🪙 {self.name} used "+colored(" G-Max Gold Rush","yellow")+"!")
    self.atktype="Normal"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al)    
    if other.confused is False:
        other.confused=True
def glare(self,other):
    print(f" 👁️ {self.name} used "+colored(" Glare","yellow")+"!")
    if other.status=="Alive":
        other.status="Paralyzed"
        print(f" ⚡ {other.name} is paralyzed.")
def thunderwave(self,other):
    print(f" ⚡ {self.name} used "+colored(" Thunder Wave","yellow")+"!")
    if other.type1!="Ground" and other.type2!="Ground" and other.type1!="Electric" and other.type2!="Electric" and other.status=="Alive" and other.ability not in ["Volt Absorb","Lightning Rod"] and a!=0:
        other.status="Paralyzed"
        print(f" ⚡ {other.name} is paralyzed.")
        
def sleeppowder(self,other):
    print(f" 🍄 {self.name} used "+colored(" Sleep Powder","green")+"!")
    if other.status!="Sleep" and (other.type1!="Grass" and other.type2!="Grass") and other.item!="Safety Googles":
        print(f" {other.name} fell asleep.")
        other.status="Sleep"
    else:
        print(" It failed.")
        
def spore(self,other):
    print(f" 🍄 {self.name} used "+colored(" Spore","green")+"!")
    if other.status!="Sleep" and (other.type1!="Grass" and other.type2!="Grass") and self.item!="Safety Googles":
        print(f" {other.name} fell asleep.")
        other.status="Sleep"
    else:
        print(" It failed.")        
        
def hypnosis(self,other):
    print(f" 😵‍💫 {self.name} used "+colored(" Hypnosis","magenta")+"!")
    if other.status!="Sleep":
        print(f" {other.name} fell asleep.")
        other.status="Sleep"
    else:
        print(" It failed.")        
        
def darkvoid(self,other):
    print(f" 🌑 {self.name} used "+colored(" Dark Void","red")+"!")
    if other.status!="Sleep":
        print(f" {other.name} fell asleep.")
        other.status="Sleep"
    else:
        print(" It failed.")             
        
def shatteredpsyche(self,other):
    al=1
    r=randroll()
    print(f" 👁️💥 {self.name} used "+colored(" Shattered Psyche","magenta")+"!")
    self.atktype="Psychic"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)    
def skyburn(self,other):
    al=1
    r=randroll()
    print(f" 🌌🔥 {self.name} used "+colored(" Light That Burns The Sky","yellow")+"!")
    self.atktype="Psychic"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)          
def genesissupernova(self,other,field,turn):
    al=1
    r=randroll()
    print(f" 🧬💥 {self.name} used "+colored(" Genesis Supernova","magenta")+"!")
    self.atktype="Psychic"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)      
    if field.terrain!="Psychic":
        field.terrain="Psychic"       
        field.psyturn=turn
        field.psyend(self,other)
        print(" 👁️ The battlefield got weird!")      
def maxmindstorm(self,other,field,turn):
    al=1
    r=randroll()
    print(f" 🔺👁️ {self.name} used "+colored(" Max Mindstorm","magenta")+"!")
    self.atktype="Psychic"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al)      
    if field.terrain!="Psychic":
        field.terrain="Psychic"       
        field.psyturn=turn
        field.psyend(self,other)
        print(" 👁️ The battlefield got weird!")  
        
def gmaxterror(self,other):
    al=1
    r=randroll()
    print(f" 🔺🪑 {self.name} used "+colored(" G-Max Terror","magenta")+"!")
    self.atktype="Ghost"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al)            
        
def maxphantasm(self,other):
    al=1
    r=randroll()
    print(f" 🔺👻 {self.name} used "+colored(" Max Phantasm","magenta")+"!")
    self.atktype="Ghost"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al)    
    defchange(other,-0.5)              
    print(f" {other.name}'s defense fell!")  
    
def neverendingnightmare(self,other):
    al=1
    r=randroll()
    print(f" 👻 {self.name} used "+colored(" Never-ending Nightmare","magenta")+"!")
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
    print(f" 🕳️ {self.name} used "+colored(" Black Hole Eclipse","red")+"!")
    self.atktype="Dark"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)     
        
def gmaxrapidflow(self,other):
    al=1
    r=randroll()
    print(f" 🔺🌊 {self.name} used "+colored(" G-Max Rapid Flow","blue")+"!")
    self.atktype="Water"
    w=weathereff(self)
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al,w)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al,w)          
                
def gmaxoneblow(self,other):
    al=1
    r=randroll()
    print(f" 🔺🌑 {self.name} used "+colored(" G-Max One Blow","red")+"!")
    self.atktype="Dark"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al)                   
def gmaxsnooze(self,other):
    al=1
    r=randroll()
    print(f" 🔺👹 {self.name} used "+colored(" G-Max Snooze","red")+"!")
    self.atktype="Dark"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al)     
    if other.yawn is False and other.status=="Alive":
        other.yawn=True
        print(f" {other.name} became drowsy!")
def maxdarkness(self,other):
    al=1
    r=randroll()
    print(f" 🔺🌑 {self.name} used "+colored(" Max Darkness","magenta")+"!")
    self.atktype="Dark"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al)           
    spdefchange (other,-0.5)              
    print(f" {other.name}'s special defense fell!")                      
def devastatingdrake(self,other):
    al=1
    r=randroll()
    print(f" 🐲💥{self.name} used "+colored(" Devastating Drake","red")+"!")
    self.atktype="Dragon"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)  
def horndrill(self,other):
    self.atktype="Normal"     
    print(f" 😈 {self.name} used "+colored(" Horn Drill","white")+"!")   
    other.hp-=other.hp        
def guillotine(self,other):
    self.atktype="Normal"     
    print(f" ✂️ {self.name} used "+colored(" Guillotine","white")+"!")   
    other.hp-=other.hp        
def fissure(self,other):
    self.atktype="Ground"     
    print(f" 🌍 {self.name} used "+colored(" Fissure","yellow")+"!")   
    other.hp-=other.hp            
def sheercold(self,other):
    self.atktype="Ice"     
    print(f" ❄️ {self.name} used "+colored(" Sheer Cold","cyan")+"!")   
    other.hp-=other.hp
def maxwyrmwind(self,other):
    al=1
    r=randroll()
    print(f" 🔺🐲 {self.name} used "+colored(" Max Wyrmwind","red")+"!")
    self.atktype="Dragon"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al)             
    atkchange (other,-0.5)
    print(f" {other.name}'s attack fell!")
def gmaxdepletion(self,other):
    al=1
    r=randroll()
    print(f" 🔺🐲 {self.name} used G-Max Depletion!")
    self.atktype="Dragon"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al)             
    atkchange (other,-0.5)    
def maxflutterby(self,other):
    al=1
    r=randroll()
    print(f" 🔺🦋 {self.name} used "+colored(" Max Flutterby","green")+"!")
    self.atktype="Bug"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al)        
    spatkchange(other,-0.5)     
    print(f" {other.name}'s special attack fell!")       
def savagespinout(self,other):
    al=1
    r=randroll()
    print(f" 🇿🦋 {self.name} used "+colored(" Savage Spin-Out","green")+"!")
    self.atktype="Bug"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)        
def gmaxresonance(self,other,tr1,turn):
    al=1
    r=randroll()
    print(f" 🔺🎶 {self.name} used "+colored(" G-Max Resonance","cyan")+"!")
    self.atktype="Ice"
    w=weathereff(self)
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al,w)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al,w)   
    if tr1.auroraveil is False:
        tr1.auroraturn=turn
        tr1.auroraend(self,other)
        tr1.auroraveil=True  
        print(" G-Max Resonance set up Aurora Veil!")            
def subzeroslammer(self,other):
    al=1
    r=randroll()
    print(f" 🇿❄️ {self.name} used "+colored(" Subzero Slammer","cyan")+"!")
    self.atktype="Ice"
    w=weathereff(self)
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al,w)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al,w)    
def gmaxsmite(self,other):
    al=1
    r=randroll()
    print(f" 🔺🧚 {self.name} used "+colored(" G-Max Smite","magenta")+"!")
    self.atktype="Fairy"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al)
    if other.confused is False:
        other.confused=True
def maxstarfall(self,other,field,turn):
    al=1
    r=randroll()
    print(f" 🔺⭐ {self.name} used "+colored(" Max Starfall","magenta")+"!")
    self.atktype="Fairy"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al)   
    if field.terrain!="Misty":
        field.terrain="Misty" 
        field.misturn=turn
        field.misend(self,other)
        print(" 🌸 Mist swirled around the battlefield!")         
def gmaxfinale(self,other):
    al=1
    r=randroll()
    print(f" 🔺🎂 {self.name} used "+colored(" G-Max Finale","magenta")+"!")
    self.atktype="Fairy"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al)      
    if self.hp<=(self.hp-(self.maxhp/6)):
        self.hp+=round(self.maxhp/6)
def twinkletackle(self,other):
    al=1
    r=randroll()
    print(f" 🇿🎠 {self.name} used "+colored(" Twinkle Tackle","magenta")+"!")
    self.atktype="Fairy"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al) 
def goalola(self,other):
    print(f" 🇿💂 {self.name} used "+colored(" Guardian of Alola","magenta")+"!")
    self.atktype="Fairy"
    other.hp-=round(other.maxhp*0.75)    
def clangsoul(self):    
    print(f" {self.name} used "+colored(" Clangorous Soul","red")+"!")
    print(f" {self.name} got an omniboost!")
    atkchange(self,0.5)
    defchange(self,0.5)
    spatkchange(self,0.5)
    spdefchange (self,0.5)
    speedchange(self,0.5)
    self.hp-=self.maxhp/4
def clangscale(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Clangorous Scales","red")+"!")
    self.atktype="Dragon"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,110,a,b,c,r,al)       
def soulblaze(self,other):
    al=1
    r=randroll()
    print(f" 🇿🦘 {self.name} used "+colored(" Clangorous Soulblaze","red")+"!")
    self.atktype="Dragon"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,185,a,b,c,r,al)       
    if a!=0:
        print(f" {self.name} got an omniboost!")
        atkchange(self,0.5)
        defchange(self,0.5)
        spatkchange(self,0.5)
        spdefchange (self,0.5)
        speedchange(self,0.5)
def snuggle(self,other):
    al=1
    r=randroll()
    print(f" 🇿🤗 {self.name} used "+colored(" Let's Snuggle Forever","magenta")+"!")
    self.atktype="Fairy"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,190,a,b,c,r,al)         
def maxknuckle(self,other):
    al=1
    r=randroll()
    print(f" 🔺👊🏿 {self.name} used "+colored(" Max Knuckle","red")+"!")
    self.atktype="Fighting"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al)         
    atkchange(self,0.5)        
    print(f" {self.name}'s attack rose!")
def gmaxchistrike(self,other):
    al=1
    r=randroll()
    print(f" 🔺👊🏾 {self.name} used "+colored(" G-Max Chi Strike","red")+"!")
    self.atktype="Fighting"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al)          
    self.critrate+=1    
def alloutpummeling(self,other):
    al=1
    r=randroll()
    print(f" 🇿👊🏽 {self.name} used "+colored(" All-Out Pummeling","red")+"!")
    self.atktype="Fighting"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)
def maxooze(self,other):
    al=1
    r=randroll()
    print(f" 🔺☠️ {self.name} used "+colored(" Max Ooze","magenta")+"!")
    self.atktype="Poison"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al)         
    spatkchange(self,0.5)      
    print(f" {self.name}'s special attack rose!")        
def aciddownpour(self,other):
    al=1
    r=randroll()
    print(f" 🇿☣️ {self.name} used "+colored(" Acid Downpour","magenta")+"!")
    self.atktype="Poison"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)         
def gmaxmalodor(self,other):
    al=1
    r=randroll()
    print(f" 🛳️☣️ {self.name} used "+colored(" G-Max Malodor","magenta")+"!")
    self.atktype="Poison"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al)        
    if other.status=="Alive":
           other.status="Badly Poisoned"
           
                 
def supersonicskystrike(self,other):
    al=1
    r=randroll()
    print(f" 🇿✈️ {self.name} used "+colored(" Supersonic Skystrike","cyan")+"!")
    self.atktype="Flying"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,200,a,b,c,r,al)
def maxairstream(self,other):
    al=1
    r=randroll()
    print(f" 🔺🌪️ {self.name} used "+colored(" Max Airstream","cyan")+"!")
    self.atktype="Flying"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al)    
    speedchange(self,0.5)             
    print(f" {self.name}'s speed rose!")                   
def gmaxwindrage(self,other):
    al=1
    r=randroll()
    print(f" 🔺🌪️ {self.name} used "+colored(" G-Max Wind Rage","cyan")+"!")
    self.atktype="Flying"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al)      
             
def trickroomm(self,other,turn):
    print(f" 🔳 {self.name} used "+colored(" Trick Room","magenta")+"!")       
    if field.trickroom is False:
        field.trickroom=True
        field.troomturn=turn
        field.troomend(self,other)
        print(f" {self.name} twisted the dimensions.")
    elif field.trickroom is True:
        field.trickroom=False
        print(f" {self.name} twisted the dimensions.")         
def shadowball (self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" 🎱 {self.name}'s {self.ability}.")
    print(f" {self.name} used "+colored(" Shadow Ball","magenta")+"!")
    self.atktype="Ghost"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,80,a,b,c,r,al)  
    chance=20
    if self.ability=="Serene Grace":
        chance*=2
    if self.speed>other.speed:
        ch=random.randint(1,100)            
        if ch>(100-chance) and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
            spdefchange(other,-0.5)
            print(f" {other.name}: Special Defense x"+str(other.spdefb))
def judgement(self,other):
    al=1
    r=randroll()
    self.atktype=self.type1
    if True:
        typ=None
        color="white"
        if self.atktype=="Dragon":
            typ="🐲"
            color="red"
        if self.atktype=="Psychic":
            typ="👁️"
            color="magenta"
        if self.atktype=="Ghost":
            typ="👻"
            color="magenta"
        if self.atktype=="Normal":
            typ="🏳️"
            color="white"
        if self.atktype=="Bug":
            typ="🪲"
            color="green"
        if self.atktype=="Steel":
            typ="⚙️"
            color="white"
        if self.atktype=="Ice":
            typ="❄️"
            color="cyan"
        if self.atktype=="Fighting":
            typ="👊🏽"
            color="red"
        if self.atktype=="Dark":
            typ="🌑"
            color="red"
        if self.atktype=="Fairy":
            typ="🧚🏻‍♂️"
            color="magenta"
        if self.atktype=="Flying":
            typ="🕊️"
            color="cyan"
        if self.atktype=="Poison":
            typ="☣️"
            color="magenta"
        if self.atktype=="Ground":
            typ="🌍"
            color="yellow"
        if self.atktype=="Rock":
            typ="🪨"
            color="yellow"
        if self.atktype=="Grass":
            typ="🌿"
            color="green"
        if self.atktype=="Electric":
            typ="⚡"
            color="yellow"
        if self.atktype=="Water":
            typ="🌊"
            color="blue"
        if self.atktype=="Fire":
            typ="🔥"
            color="red"
    print(f" 🌌{typ} {self.name} used "+colored(" Judgement",f"{color}")+"!")
    w=weathereff(self)
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,100,a,b,c,r,al,w)          
def multiattack(self,other):
    al=1
    r=randroll()
    self.atktype=self.type1
    if True:
        typ=None
        color="white"
        if self.atktype=="Dragon":
            typ="🐲"
            color="red"
        if self.atktype=="Psychic":
            typ="👁️"
            color="magenta"
        if self.atktype=="Ghost":
            typ="👻"
            color="magenta"
        if self.atktype=="Normal":
            typ="🏳️"
            color="white"
        if self.atktype=="Bug":
            typ="🪲"
            color="green"
        if self.atktype=="Steel":
            typ="⚙️"
            color="white"
        if self.atktype=="Ice":
            typ="❄️"
            color="cyan"
        if self.atktype=="Fighting":
            typ="👊🏽"
            color="red"
        if self.atktype=="Dark":
            typ="🌑"
            color="red"
        if self.atktype=="Fairy":
            typ="🧚🏻‍♂️"
            color="magenta"
        if self.atktype=="Flying":
            typ="🕊️"
            color="cyan"
        if self.atktype=="Poison":
            typ="☣️"
            color="magenta"
        if self.atktype=="Ground":
            typ="🌍"
            color="yellow"
        if self.atktype=="Rock":
            typ="🪨"
            color="yellow"
        if self.atktype=="Grass":
            typ="🌿"
            color="green"
        if self.atktype=="Electric":
            typ="⚡"
            color="yellow"
        if self.atktype=="Water":
            typ="🌊"
            color="blue"
        if self.atktype=="Fire":
            typ="🔥"
            color="red"
    print(f" 💽{typ} {self.name} used "+colored(" Multi-Attack",f"{color}")+"!")
    w=weathereff(self)
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,90,a,b,c,r,al,w)              
def seedflare (self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Seed Flare","green")+"!")
    self.atktype="Grass"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,120,a,b,c,r,al)  
    ch=random.randint(1,100)
    if ch>60 and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        spdefchange(other,-1)
        print(f" {other.name}: Special Defense x"+str(other.spdefb))        
def storedpower(self,other):   
    atkx=(self.atkb-1)*2
    spatkx=(self.spatkb-1)*2
    defx=(self.defb-1)*2
    spdefx=(self.spdefb-1)*2
    speedx=(self.speedb-1)*2
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Stored Power","magenta")+"!")
    self.atktype="Psychic"
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
    print(f" {self.name} used "+colored(" Hex","magenta")+"!")
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
    print(f" {self.name} used "+colored(" Infernal Parade","magenta")+"!")
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
        print(f" 🔥 {other.name} was burned.")
        
     
def energyball (self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    print(f" {self.name} used "+colored(" Energy Ball","green")+"!")
    self.atktype="Grass"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,80,a,b,c,r,al)  
    ch=random.randint(1,10)
    if ch==7 and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil","Shield Dust"]:
        spdefchange(other,-0.5)
        print(f" {other.name}: Special Defense x"+str(other.spdefb))        
def bugbuzz (self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    print(f" 🪰 {self.name} used "+colored(" Bug Buzz","green")+"!")
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
        print(f" {other.name}: Special Defense x"+str(other.spdefb))        
def snipeshot (self,other):
    al=1
    r=randroll()
    w=weathereff(self)
    print(f" {self.name} used "+colored(" Snipe Shot","blue")+"!")
    self.atktype="Water"
    c=critch(self,other,4)
    if self.ability=="Mega Launcher":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,70,a,b,c,r,al,w)                   
def signalbeam (self,other):
    al=1
    r=randroll()
    print(f" 🚦 {self.name} used "+colored(" Signal Beam","magenta")+"!")
    self.atktype="Bug"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,75,a,b,c,r,al)  
    chance=10
    if self.ability=="Serene Grace":
        chance*=2
    ch=random.randint(1,100)            
    if ch>(100-chance)  and other.confused is False:
        other.confused=True       
def aeroblast (self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Aeroblast","cyan")+"!")
    self.atktype="Flying"
    c=critch(self,other,2)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,100,a,b,c,r,al)        
def makeitrain(self,other):
    al=1
    r=randroll()
    print(f" 🪙 {self.name} used "+colored(" Make It Rain","yellow")+"!")
    self.atktype="Steel"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,120,a,b,c,r,al)           
    spatkchange(self,-0.5)
    print(f" Special Attack x{self.spatkb}")     
def leafstorm(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Leaf Storm","green")+"!")
    self.atktype="Grass"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,130,a,b,c,r,al)           
    spatkchange(self,-1)
    print(f" Special Attack x{self.spatkb}")   
def blizzard(self,other):
    self.atktype="Ice"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f" ❄️ {self.name} used "+colored(" Blizzard","cyan")+"!")
    
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,110,a,b,c,r,al,w)    
    ch=random.randint(1,10)
    if ch==1 and other.status is None and self.ability!="Sheer Force" and other.ability not in ["Shield Dust"]:
        other.status=random.choice(["Frozen","Frostbite"])
        print(f" ❄️ {other.name} was frozen.")
        
def boomburst(self,other):
    al=1
    r=randroll()
    print(f" 🔊 {self.name} used "+colored(" Boomburst","white")+"!")
    self.atktype="Normal"
    c=critch(self,other)
    if self.ability=="Punk Rock":
        al*=1.3
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,140,a,b,c,r,al)        
def sonicslash(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Sonic Slash","cyan")+"!")
    self.atktype="Flying"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=80
    if self.speedb<2:
        base=80
    if 3>self.speedb>=2:
        base=120
    if self.speedb>3:
        base=140
    other.hp-=special(self.level,self.spatk,other.spdef,base,a,b,c,r,al)    
def airslash(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Air Slash","cyan")+"!")
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
    print(f" {self.name} used "+colored(" Leaf Tornado","green")+"!")
    self.atktype="Grass"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,130,a,b,c,r,al)             
       
def psystrike(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Psystrike","magenta")+"!")
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
    print(f" 🔥 {self.name} used "+colored(" Sacred Fire","red")+"!")
    w=weathereff(self)
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,110,a,b,c,r,al,w)  
def aurasphere(self,other):
    al=1
    r=randroll()
    print(f" 🌀 {self.name} used "+colored(" Aura Sphere","blue")+"!")
    self.atktype="Fighting"
    c=critch(self,other)
    if self.ability=="Mega Launcher":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,80,a,b,c,r,al)      
    
def heatwave(self,other):
    self.atktype="Fire"
    al=1
    w=weathereff(self)
    r=randroll()
    print(f" 🔥 {self.name} used "+colored(" Heat Wave","red")+"!")
    
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,95,a,b,c,r,al,w)     
def bleakwindstorm(self,other):
    al=1
    w=weathereff(self)
    r=randroll()
    print(f" 🌪️❄️ {self.name} used "+colored(" Bleakwind Storm","cyan")+"!")
    self.atktype="Flying"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,95,a,b,c,r,al,w)   
    ch=random.randint(1,100)
    if ch>90 and other.status=="Alive":
        other.status=random.choice(["Frozen","Frostbite"])
        print(f" ❄️ {other.name} was frozen.")
def springtidestorm(self,other):
    al=1
    w=weathereff(self)
    r=randroll()
    print(f" 🌸 {self.name} used "+colored(" Springtide Storm","magenta")+"!")
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
    print(f" {self.name} used "+colored(" Sandsear Storm","yellow")+"!")
    self.atktype="Ground"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,95,a,b,c,r,al,w)       
    ch=random.randint(1,100)
    if ch>90 and other.status=="Alive":
        other.status="Burned"
        print(f" 🔥 {other.name} was burned.")                   
def wildboltstorm(self,other):
    al=1
    w=weathereff(self)
    r=randroll()
    print(f" 🌩️ {self.name} used "+colored(" Wildbolt Storm","yellow")+"!")
    self.atktype="Electric"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,95,a,b,c,r,al,w)        
    ch=random.randint(1,100) 
    if ch>90 and other.status=="Alive" and a!=0:
        other.status="Paralyzed"
        print(f" ⚡ {other.name} was paralyzed.")
def morningsun(self):
    print(f" ☀️ {self.name} used Morning Sun.")   
    if self.hp>=(self.maxhp/2):
        self.hp=self.maxhp
    elif self.hp==self.maxhp:
        print(" Already at full HP.")
    else:
        if field.weather=="Sunny" or field.weather=="Desolate Land":
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
    print(f" 🏖️ {self.name} used Shore Up.")   
    if self.hp>=(self.maxhp/2):
        self.hp=self.maxhp
    elif self.hp==self.maxhp:
        print(" Already at full HP.")
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
    print(f" 🌕 {self.name} used Moonlight.")   
    if self.hp>=(self.maxhp/2):
        self.hp=self.maxhp
    elif self.hp==self.maxhp:
        print(" Already at full HP.")
    else:
        if field.weather=="Sunny" or field.weather=="Desolate Land":
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
    print(f" 🌻 {self.name} used "+colored(" Synthesis","green")+"!")
    if self.hp>=(self.maxhp/2):
        self.hp=self.maxhp
    elif self.hp==self.maxhp:
        print(" Already at full HP.")
    else:
        if field.weather=="Sunny" or field.weather=="Desolate Land":
            self.hp+=((self.maxhp*2)/3)    
            if self.hp>self.maxhp:
                self.hp=self.maxhp
        if field.weather in ["Rainy","Hail","Sandstorm"]:
            self.hp+=(self.maxhp/4)    
            if self.hp>self.maxhp:
                self.hp=self.maxhp
        else:
            self.hp+=(self.maxhp/2)
            if self.hp>self.maxhp:
                self.hp=self.maxhp
def lunarblessing(self):
    self.atktype="Psychic"
    print(f" 🌙 {self.name} used "+colored(" Lunar Blessing","magenta")+"!")   
    if self.hp>=(self.maxhp-self.maxhp/4):
        self.hp=self.maxhp
        if self.hp>self.maxhp:
            self.hp=self.maxhp
    elif self.hp==self.maxhp:
        print(" Already at full HP.")
    else:
        self.hp+=(self.maxhp/4)     
        if self.hp>self.maxhp:
            self.hp=self.maxhp       
def recover(self):
    self.atktype="Normal"
    print(f" ❤️‍🩹 {self.name} used Recover.")   
    if self.hp>=(self.maxhp/2):
        self.hp=self.maxhp
    elif self.hp==self.maxhp:
        print(" Already at full HP.")
    else:
        self.hp+=(self.maxhp/2)
        if self.hp>self.maxhp:
            self.hp=self.maxhp
def milkdrink(self):
    self.atktype="Normal"
    print(f" 🥛 {self.name} used Milk Drink.")   
    if self.hp>=(self.maxhp/2):
        self.hp=self.maxhp
    elif self.hp==self.maxhp:
        print(" Already at full HP.")
    else:
        self.hp+=(self.maxhp/2)
        if self.hp>self.maxhp:
            self.hp=self.maxhp            
def roost(self):
    self.atktype="Flying"
    print(f" 🦉 {self.name} used Roost.")   
    if self.hp>=(self.maxhp/2):
        self.hp=self.maxhp
    elif self.hp==self.maxhp:
        print(" Already at full HP.")
    else:
        self.hp+=(self.maxhp/2)        
def slackoff(self):
    self.atktype="Normal"
    print(f" 🦥 {self.name} used Slack Off.")   
    if self.hp>=(self.maxhp/2):
        self.hp=self.maxhp
    elif self.hp==self.maxhp:
        print(" Already at full HP.")
    else:
        self.hp+=(self.maxhp/2)             
def softboiled(self):
    self.atktype="Normal"
    print(f" 🥚 {self.name} used Softboiled.")   
    if self.hp>=(self.maxhp/2):
        self.hp=self.maxhp
    elif self.hp==self.maxhp:
        print(" Already at full HP.")
    else:
        self.hp+=(self.maxhp/2)      
def toxic(self, other):
    self.atktype="Poison"
    print(f" {self.name} used "+colored(" Toxic","magenta")+"!")       
    if other.status=="Alive" and other.type1 not in ["Steel","Poison"] and other.type2 not in ["Steel","Poison"] and other.ability not in ["Immunity","Magic Bounce"]:
        other.status="Badly Poisoned"
        print(f" ☠️ {other.name} was badly poisoned.")
    if other.ability in ["Magic Bounce","Synchronize"] and self.status=="Alive":
        self.status="Badly Poisoned"
        print(f" {self.name} was badly poisoned.")
    elif other.type1 in ["Steel","Poison"] or other.type2 in ["Steel","Poison"] or other.ability in ["Immunity","Magic Bounce"]:
        print(" It failed.")
def willowisp(self, other):
    self.atktype="Fire"
    print(f" {self.name} used "+colored(" Will-O-Wisp","red")+"!")          
    if other.status=="Alive" and other.type1 not in ["Fire"] and other.type2 not in ["Fire"] and other.ability not in ["Flash Fire","Magic Bounce"]:
        other.status="Burned"
        other.atk*=0.5
        print(f" 🔥 {other.name} was burned.")
        
    if other.ability in ["Magic Bounce","Synchronize"] and self.status=="Alive":
        self.status="Burned"
        print(f" 🔥 {self.name} was burned.")
        
    elif other.type1 in ["Fire"] or other.type2 in ["Fire"] or other.ability in ["Flash Fire","Magic Bounce"]:
        print(" It failed.")    
def healorder(self):
    print(f" {self.name} used "+colored(" Heal Order","green")+"!")   
    if self.hp>=(self.maxhp/2):
        self.hp=self.maxhp
    elif self.hp==self.maxhp:
        print(" Already at full HP.")
    else:
        self.hp+=(self.maxhp/2)                       
def tbolt(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    print(f" {self.name} used "+colored(" Thunderbolt","yellow")+"!")
    c=critch(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al) 
    ch=random.randint(1,10)
    if ch==10 and other.status=="Alive" and other.ability not in ["Shield Dust"] and a!=0:
        other.status="Paralyzed"
        print(f" ⚡ {other.name} was paralyzed.")
def thundercage(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Thunder Cage","yellow")+"!")
    c=critch(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,80,a,b,c,r,al)        
    if other.olock is False:
        other.olock=True 
def nuzzle(self,other):
    al=1
    r=randroll()
    print(f" ⚡ {self.name} used "+colored(" Nuzzle","yellow")+"!")
    c=critch(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,20,a,b,c,r,al)        
    if other.status=="Alive" and a!=0:
        other.status="Paralyzed"
        print(f" ⚡ {other.name} was paralyzed.")
def technoblast(self,other):
    al=1
    r=randroll()
    self.atktype="Normal"
    color="white"
    if self.item=="Burn Drive":
        self.atktype="Fire"
        color="red"
        print(f" 🔥 {self.name}'s {self.item} made Techno Blast {self.atktype}-type!")
    if self.item=="Chill Drive":
        self.atktype="Ice"
        color="cyan"
        print(f" ❄️ {self.name}'s {self.item} made Techno Blast {self.atktype}-type!")
    if self.item=="Douse Drive":
        self.atktype="Water"
        color="blue"
        print(f" 💧 {self.name}'s {self.item} made Techno Blast {self.atktype}-type!")
    if self.item=="Shock Drive":
        self.atktype="Electric"
        color="yellow"
        print(f" ⚡ {self.name}'s {self.item} made Techno Blast {self.atktype}-type!")
    print(f" {self.name} used "+colored(" Techno Blast",f"{color}")+"!")
    w=weathereff(self)
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,120,a,b,c,r,al,w)            
def focusblast(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    print(f" 🔴 {self.name} used "+colored(" Focus Blast","red")+"!")
    c=critch(self,other)
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,120,a,b,c,r,al)        
    ch=random.randint(1,10)
    if ch==7 and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil","Shield Dust"]:
        spdefchange(other,-0.5)
        print(f" {other.name}: Special Defense x"+str(other.spdefb))
def thunder(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    print(f" 🌩️ {self.name} used "+colored(" Thunder","yellow")+"!")
    c=critch(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,110,a,b,c,r,al)   
    ch=random.randint(1,100)
    if ch>70 and other.status=="Alive" and other.ability not in ["Shield Dust"] and a!=0:
        other.status="Paralyzed"
        print(f" {other.name} is paralyzed.")
def finalgambit(self,other):
    print(f" {self.name} used "+colored(" Final Gambit","red")+"!")       
    other.hp-=self.hp
    self.hp-=self.hp
def venoshock(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Venoshock","magenta")+"!")
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
    print(f" {self.name} used "+colored(" Fishious Rend","blue")+"!")
    c=critch(self,other)
    self.atktype="Water"
    w=weathereff(self)
    if self.ability=="Strong Jaw":
        print(f" {self.name}'s {self.ability}!")
        al=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=85
    if self.speed>other.speed:
        base*=2
    other.hp-=physical(self.level,self.atk,other.defense,base,a,b,c,r,al,w)      
def blazingtorque(self,other):
    al=1
    r=randroll()
    w=weathereff(self)
    print(f" {self.name} used "+colored(" Blazing Torque","red")+"!")
    c=critch(self,other)
    self.atktype="Fire"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    other.hp-=physical(self.level,self.atk,other.defense,100,a,b,c,r,al,w) 
def combattorque(self,other):
    al=1
    r=randroll()
    w=weathereff(self)
    print(f" {self.name} used "+colored(" Combat Torque","red")+"!")
    c=critch(self,other)
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    other.hp-=physical(self.level,self.atk,other.defense,100,a,b,c,r,al,w)       
def magicaltorque(self,other):
    al=1
    r=randroll()
    w=weathereff(self)
    print(f" {self.name} used "+colored(" Magical Torque","magenta")+"!")
    c=critch(self,other)
    self.atktype="Fairy"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    other.hp-=physical(self.level,self.atk,other.defense,100,a,b,c,r,al,w)      
def noxioustorque(self,other):
    al=1
    r=randroll()
    w=weathereff(self)
    print(f" {self.name} used "+colored(" Noxious Torque","magenta")+"!")
    c=critch(self,other)
    self.atktype="Poison"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    other.hp-=physical(self.level,self.atk,other.defense,100,a,b,c,r,al,w)     
def wickedtorque(self,other):
    al=1
    r=randroll()
    w=weathereff(self)
    print(f" {self.name} used "+colored(" Wicked Torque","red")+"!")
    c=critch(self,other)
    self.atktype="Dark"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    other.hp-=physical(self.level,self.atk,other.defense,100,a,b,c,r,al,w)             
def boltbeak(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Bolt Beak","yellow")+"!")
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
    print(f" {self.name} used "+colored(" Electro Ball","yellow")+"!")
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
    print(f" {self.name} used "+colored(" Electroweb","yellow")+"!")
    c=critch(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=65
    other.hp-=special(self.level,self.spatk,other.spdef,base,a,b,c,r,al)        
    if other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil","Shield Dust"]:
        speedchange(other,-0.5)
        print(f" {other.name}: Speed x{other.speedb}")
def powergem(self,other):
    al=1
    r=randroll()
    print(f" 🪨 {self.name} used "+colored(" Power Gem","yellow")+"!")   
    c=critch(self,other)
    self.atktype="Rock"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,80,a,b,c,r,al)            
def zapcannon(self,other):
    al=1
    r=randroll()
    if self.ability=="Mega Launcher":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    if self.ability=="Sheer Force":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    print(f" {self.name} used "+colored(" Zap Cannon","yellow")+"!")
    c=critch(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al)            
    if other.status=="Alive" and self.ability!="Sheer Force" and other.ability not in ["Shield Dust"] and a!=0:
        other.status="Paralyzed"
        print(f" {other.name} is paralyzed.")
def freezedry(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Freeze-Dry","cyan")+"!")
    c=critch(self,other)
    self.atktype="Ice"
    w=weathereff(self)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if "Water" in (other.type1,other.type2,other.teratype):
        if a==1:
            a*=2
            print(" It's super effective!")
        if a<1:
            a*=2
    other.hp-=special(self.level,self.spatk,other.spdef,70,a,b,c,r,al,w) 
def saltcure(self,other):
    al=1
    r=randroll()
    print(f" 🧂 {self.name} used "+colored(" Salt Cure","white")+"!")
    c=critch(self,other)
    self.atktype="Rock"
    w=weathereff(self)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if "Steel" in (other.type1,other.type2,other.teratype):
        if a==1:
            a*=2
        if a!=1:
            a*=2
    if "Water" in (other.type1,other.type2,other.teratype):
        if a==1:
            a*=1.5
        if a!=1:
            a*=1.5
    other.hp-=special(self.level,self.spatk,other.spdef,65,a,b,c,r,al,w)     
def shellsidearm(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" 🐚 {self.name}'s {self.ability}.")
    print(f" {self.name} used "+colored(" Shell Side Arm","magenta")+"!")
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
    if ch>80 and other.status=="Alive" and other.type1 not in ["Steel","Poison"] and other.type2 not in ["Steel","Poison"] and other.ability not in ["Immunity","Magic Bounce","Shield Dust"]:
        other.status="Badly Poisoned"
        print(f" ☠️ {other.name} was badly poisoned.")                   
def poisonjab(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    print(f" {self.name} used "+colored(" Poison Jab","magenta")+"!")
    c=critch(self,other)
    self.atktype="Poison"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,90,a,b,c,r,al) 
    ch=random.randint(1,100)
    if ch>70 and other.status=="Alive" and other.type1 not in ["Steel","Poison"] and other.type2 not in ["Steel","Poison"] and other.ability not in ["Immunity","Magic Bounce","Shield Dust"]:
        other.status="Badly Poisoned"
        print(f" ☠️ {other.name} was badly poisoned.")
def drillpeck(self,other):
    al=1
    r=randroll()
    print(f" 🐔 {self.name} used "+colored(" Drill Peck","cyan")+"!")
    c=critch(self,other,2)
    self.atktype="Flying"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,80,a,b,c,r,al)        
def leafblade(self,other):
    al=1
    r=randroll()
    print(f" 🌿 {self.name} used "+colored(" Leaf Blade","green")+"!")
    if self.ability=="Sharpness":
        al*=1.5
    c=critch(self,other,2)
    self.atktype="Grass"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,90,a,b,c,r,al)    
def triplearrows(self,other):
    al=1
    r=randroll()
    print(f" 🏹 {self.name} used "+colored(" Triple Arrows","red")+"!")
    c=critch(self,other,2)
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,90,a,b,c,r,al)
    ch=random.randint(1,100)
    if 95>ch>90 and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        defchange(other,-0.5)
        print(f" {other.name}: Defense x{other.defb}")
    if ch>95  and other.ability not in ["Inner Focus"]:
        other.flinched=True   
def razorleaf(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Razor Leaf","green")+"!")
    c=critch(self,other,2)
    self.atktype="Grass"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    other.hp-=physical(self.level,self.atk,other.defense,70,a,b,c,r,al)        
def gyroball(self,other):
    al=1
    r=randroll()
    print(f" 🏐 {self.name} used "+colored(" Gyro Ball","white")+"!")
    c=critch(self,other)
    self.atktype="Steel"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=round(1+25*(other.speed/self.speed))
    other.hp-=physical(self.level,self.atk,other.defense,base,a,b,c,r,al)   
def overdrive(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Overdrive","yellow")+"!")
    c=critch(self,other)
    if self.ability=="Punk Rock":
        al*=1.3
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=special (self.level,self.spatk,other.spdef,80,a,b,c,r,al)         
    other.hp-=dmg
def discharge(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Disharge","yellow")+"!")
    c=critch(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=special (self.level,self.spatk,other.spdef,80,a,b,c,r,al) 
    other.hp-=dmg    
    ch=random.randint(1,100)
    if ch>70 and other.status=="Alive" and a!=0:
        other.status="Paralyzed"
        print(f" {other.name} is paralyzed.")
def doubleshock(self,other):
    al=1
    r=randroll()
    print(f" ⚡ {self.name} used "+colored(" Double Shock","yellow")+"!")
    c=critch(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,120,a,b,c,r,al)        
    other.hp-=dmg
    if self.type2==None and self.type1=="Electric":
        self.type1=None
    if self.type2!=None and self.type1=="Electric":
        self.type1=self.type2
        self.type2=None
def wildcharge(self,other):
    al=1
    r=randroll()
    print(f" ⚡ {self.name} used "+colored(" Wild Charge","yellow")+"!")
    c=critch(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,90,a,b,c,r,al) 
    if self.ability=="Reckless":
        dmg*=1.2
    if dmg>other.hp:
        dmg=other.hp
        other.hp=0
    else:
        other.hp-=dmg
    if self.ability!="Rock Head":
        self.hp-=round(dmg/4)
        print(f" {self.name} was hurt by recoil.")         
def accelerock(self,other):
    al=1
    r=randroll()
    print(f" 🪨 {self.name} used "+colored(" Accelerock","yellow")+"!")
    c=critch(self,other)
    self.atktype="Rock"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,40,a,b,c,r,al)     
def secretsword(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Secret Sword","red")+"!")
    c=critch(self,other)
    self.atktype="Fighting"
    if self.ability=="Sharpness":
        al*=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.defense,85,a,b,c,r,al)          
def sacredsword(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Sacred Sword","red")+"!")
    c=critch(self,other)
    self.atktype="Fighting"
    if self.ability=="Sharpness":
        al*=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.maxdef,90,a,b,c,r,al)         
def throatchop(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Throat Chop","red")+"!")
    c=critch(self,other)
    self.atktype="Dark"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,80,a,b,c,r,al)           
def darkestlariat(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Darkest Lariat","red")+"!")
    c=critch(self,other)
    self.atktype="Dark"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.maxdef,85,a,b,c,r,al)       
def acrobatics(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Acrobatics","cyan")+"!")
    c=critch(self,other)
    self.atktype="Flying"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
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
    print(f" {self.name} used "+colored(" Aura Wheel","yellow")+"!")
    c=critch(self,other)
    self.atktype="Electricb"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,110,a,b,c,r,al)            
def barbbarrage(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Barb Barrage","magenta")+"!")
    c=critch(self,other)
    self.atktype="Poison"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=60
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    if other.status!="Alive":
        base=120
    other.hp-=physical(self.level,self.atk,other.defense,base,a,b,c,r,al)         
def beakblast(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Beak Blast","cyan")+"!")
    c=critch(self,other)
    self.atktype="Flying"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,100,a,b,c,r,al)     
def partingshot(self,other):
    print(f" {self.name} used Parting Shot.")        
    if other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        atkchange(other,-0.5)
        spatkchange (other,-0.5)
        print(f" {other.name}: Attack x{other.atkb}")
        print(f" {other.name}: Special Attack x{other.spatkb}")
    else:
        print(f" Can't lower {other.name}'s stats!")
def shadowbone(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Shadow Bone","yellow")+"!")
    c=critch(self,other)
    self.atktype="Ghost"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.ability=="Bone Zone":
        if a==0:
            a=1
        if 0<a<1:
            a=2
    other.hp-=physical(self.level,self.atk,other.defense,85,a,b,c,r,al)       
    ch=random.randint(1,100)
    if ch>80 and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        defchange (other,-0.5)
        print(f" {other.name}: Defense x{other.defb}") 
def bonerush(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Bone Rush","yellow")+"!")
    c=critch(self,other)
    self.atktype="Ground"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.ability=="Bone Zone":
        if a==0:
            a=1
        if 0<a<1:
            a=2
    other.hp-=physical(self.level,self.atk,other.defense,25,a,b,c,r,al)  
def mistyexplosion(self,other):
    al=1
    r=randroll()
    print(f" 🌸💥 {self.name} used "+colored(" Misty Explosion","magenta")+"!")
    c=critch(self,other)
    if self.ability=="Reckless":
        al*=1.2  
    self.atktype="Fairy"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=100
    if field.terrain=="Misty":
        base*=1.5
    other.hp-=special(self.level,self.spatk,other.spdef,base,a,b,c,r,al)         
    self.hp=0     
def explosion(self,other):
    al=1
    r=randroll()
    print(f" 💥 {self.name} used "+colored(" Explosion","white")+"!")
    c=critch(self,other)
    if self.ability=="Reckless":
        al*=1.2  
    self.atktype="Normal"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,(other.defense/2),150,a,b,c,r,al)         
    self.hp=0     
def snarl(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Snarl","magenta")+"!")
    c=critch(self,other)
    self.atktype="Dark"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,55,a,b,c,r,al)           
    if other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        spatkchange (other,-0.5) 
        print(f" {other.name}: Special Attack x{other.spatkb}")
    else:
        print(" Nothing happened!")
def steelbeam(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Steel Beam","white")+"!")
    c=critch(self,other)
    self.atktype="Steel"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=special(self.level,self.spatk,other.spdef,140,a,b,c,r,al)       
    if self.ability=="Reckless":
        dmg*=1.2 
    if other.hp<dmg:
        dmg=other.hp
        other.hp-=dmg
    else:
        other.hp-=dmg        
    if self.ability!="Magic Guard":
        print(f" {self.name} was hurt by recoil.")
        self.hp-=self.maxhp/2         
def aquajet(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Aqua Jet","blue")+"!")
    c=critch(self,other)
    self.atktype="Water"
    w=weathereff(self)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=40
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    other.hp-=physical (self.level,self.atk,other.defense,base,a,b,c,r,al,w)   
def jetpunch(self,other):
    al=1
    r=randroll()
    print(f" 🐬 {self.name} used "+colored(" Jet Punch","blue")+"!")
    c=critch(self,other)
    self.atktype="Water"
    w=weathereff(self)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=60
    if self.item=="Punching Glove":
        al=1.5
    if self.ability=="Iron Fist":
        print(f" {self.name}'s {self.ability}!")
        al=1.3
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    other.hp-=physical (self.level,self.atk,other.defense,base,a,b,c,r,al,w)                      
def armthrust(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Arm Thrust","red")+"!")
    c=critch(self,other)
    self.atktype="Fighting"
    base=25
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,base,a,b,c,r,al)    
def psyshield(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Psyshield Bash","magenta")+"!")
    c=critch(self,other)
    self.atktype="Psychic"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,70,a,b,c,r,al)  
    ch=random.randint(1,100)
    if ch>50:
        defchange(self,0.5)
        print(" Defense x"+str(self.defb))    
def steelwing(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Steel Wing","white")+"!")
    c=critch(self,other)
    self.atktype="Steel"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,70,a,b,c,r,al)  
    ch=random.randint(1,10)
    if ch==7:
        defchange(self,0.5)
        print(" Defense x"+str(self.defb))
def heatcrash(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Heat Crash","red")+"!")
    c=critch(self,other)
    self.atktype="Fire"
    w=weathereff(self)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=80
    if self.defense>self.spdef:
        base*=(self.defense/other.defense)
    if self.spdef>self.defense:
        base*=(self.spdef/other.spdef)
    other.hp-=physical(self.level,self.atk,other.defense,base,a,b,c,r,al,w)         
def grassknot(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Grass Knot","green")+"!")
    c=critch(self,other)
    self.atktype="Grass"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
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
    print(f" {self.name} used "+colored(" Heavy Slam","white")+"!")
    c=critch(self,other)
    self.atktype="Steel"
    if self.ability=="Heavy Metal":
        print(f" {self.name}'s {self.ability}!")
        al*=2
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
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
    print(f" {self.name} used "+colored(" Assurance","red")+"!")
    c=critch(self,other)
    self.atktype="Dark"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=60
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    if self.speed<other.speed:
        base*=2
    other.hp-=physical(self.level,self.atk,other.defense,base,a,b,c,r,al)                   
def attackorder(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Attack Order","green")+"!")
    c=critch(self,other,2)
    self.atktype="Bug"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,120,a,b,c,r,al)             
def facade(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Facade","white")+"!")
    c=critch(self,other)
    self.atktype="Normal"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
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
    print(f" {self.name} used "+colored(" Return","white")+"!")
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
    print(f" {self.name} used "+colored(" Body Press","red")+"!")
    c=critch(self,other)
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.defense,other.defense,80,a,b,c,r,al)    
    
def stoneedge(self,other):
    al=1
    r=randroll()
    
    print(f" {self.name} used "+colored(" Stone Edge","yellow")+"!")
    c=critch(self,other,2)
    self.atktype="Rock"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,90,a,b,c,r,al)   
def stoneaxe(self,other,optr):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Stone Axe","yellow")+"!")
    c=critch(self,other,2)
    self.atktype="Rock"
    if self.ability=="Sharpness":
        al*=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,65,a,b,c,r,al)       
    if "Stealth Rock" not in optr.hazard:
        print(" 🪨 Pointed stones float in the air around the opposing team!")
        optr.hazard.append("Stealth Rock")
def petaldance(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Petal Dance","green")+"!")
    c=critch(self,other,2)
    self.atktype="Grass"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,120,a,b,c,r,al) 
def petalblizzard(self,other):
    al=1
    r=randroll()
    print(f" 🌸 {self.name} used "+colored(" Petal Blizzard","green")+"!")
    c=critch(self,other,2)
    self.atktype="Grass"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,90,a,b,c,r,al)                 
def ragingfury(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Raging Fury","red")+"!")
    c=critch(self,other,2)
    self.atktype="Fire"
    w=weathereff(self)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,90,a,b,c,r,al,w)   
def outrage(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Outrage","red")+"!")
    c=critch(self,other,2)
    self.atktype="Dragon"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
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
        print(f" {self.name}'s {self.ability}.")
    print(f" ❄️ {self.name} used "+colored(" Ice Fang","cyan")+"!")
    c=critch(self,other)
    self.atktype="Ice"
    w=weathereff(self)
    if self.ability=="Strong Jaw":
        print(f" {self.name}'s {self.ability}!")
        al=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,90,a,b,c,r,al,w)       
    ch=random.randint(1,100)
    if ch>90 and self.ability!="Sheer Force" and other.ability not in ["Shield Dust"]:
       other.status=random.choice(["Frozen","Frostbite"])
       print(f" ❄️ {other.name} was frozen.")
def rockslide(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    print(f" {self.name} used "+colored(" Rock Slide","yellow")+"!")
    c=critch(self,other)
    self.atktype="Rock"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,85,a,b,c,r,al)   
    ch=random.randint(1,100)
    if ch>80  and other.ability not in ["Inner Focus","Shield Dust"]:
        other.flinched=True       
def waterfall(self,other):
    self.atktype="Water"
    al=1
    w=weathereff(self)
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    print(f" {self.name} used "+colored(" Waterfall","blue")+"!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,85,a,b,c,r,al,w)       
    ch=random.randint(1,100)
    if ch>80  and other.ability not in ["Inner Focus","Shield Dust"]:
        other.flinched=True        
def crosspoison(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    print(f" {self.name} used "+colored(" Cross Poison","magenta")+"!")
    c=critch(self,other)
    self.atktype="Poison"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,90,a,b,c,r,al)           
    ch=random.randint(1,100)
    if ch>90 and other.status=="Alive" and other.type1 not in ["Steel","Poison"] and other.type2 not in ["Steel","Poison"] and other.ability not in ["Immunity","Magic Bounce"]:
        other.status="Badly Poisoned"
        print(f" ☠️ {other.name} was badly poisoned.")
def rockblast(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Rock Blast","yellow")+"!")
    c=critch(self,other)
    self.atktype="Rock"
    base=25
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,base,a,b,c,r,al)         
def skyuppercut(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Sky Uppercut","red")+"!")
    c=critch(self,other)
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,70,a,b,c,r,al)         
def shadowforce(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Shadow Force","magenta")+"!")
    c=critch(self,other)
    self.atktype="Ghost"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,120,a,b,c,r,al)              
    ch=random.randint(1,100)
    if ch>70 and self.ability!="Sheer Force" and other.ability not in ["Inner Focus","Shield Dust"]:
        other.flinched=True  
def phantomforce(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Phantom Force","magenta")+"!")
    c=critch(self,other)
    self.atktype="Ghost"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,90,a,b,c,r,al)                      
def blazekick(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Blaze Kick","red")+"!")
    if self.ability=="Striker":
        print(f" {self.name}'s {self.ability}!")
        al=1.3
    c=critch(self,other)
    self.atktype="Fire"
    w=weathereff(self)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,85,a,b,c,r,al,w)       
def axekick(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Axe Kick","red")+"!")
    c=critch(self,other)
    if self.ability=="Striker":
        print(f" {self.name}'s {self.ability}!")
        al=1.3
    if self.ability=="Reckless":
        al*=1.2
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical(self.level,self.atk,other.defense,120,a,1,b,c,r,al)
    miss=random.randint(1,100)
    ch=random.randint(1,100)
    if ch>90:
        other.confused=True
    if miss>90:
        print(f" {other.name} avoided the attack.")
        print(f" {self.name} was hurt by recoil.")
        sdmg=dmg/2
        if sdmg>(self.maxhp/2):
            sdmg=self.maxhp/2        
        self.hp-=sdmg
    elif miss<=90:
        other.hp-=dmg
def hijumpkick(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" High Jump Kick","red")+"!")
    if self.ability=="Striker":
        print(f" {self.name}'s {self.ability}!")
        al=1.3
    c=critch(self,other)
    if self.ability=="Reckless":
        al*=1.2
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical(self.level,self.atk,other.defense,130,a,b,c,r,al)
    miss=random.randint(1,100)
    if miss>90:
        print(f" {other.name} avoided the attack.")
        print(f" {self.name} was hurt by recoil.")
        sdmg=dmg/2
        if sdmg>(self.maxhp/2):
            sdmg=self.maxhp/2        
        self.hp-=sdmg
    elif miss<=90:
         other.hp-=dmg
def foulplay(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Foul Play","red")+"!")
    c=critch(self,other)
    self.atktype="Dark"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,other.atk,other.defense,80,a,b,c,r,al)      
def bulletseed(self,other):
    al=1
    r=randroll()
    print(f" 🟢 {self.name} used "+colored(" Bullet Seed","green")+"!")
    c=critch(self,other)
    self.atktype="Grass"
    w=weathereff(self)
    base=25
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,base,a,b,c,r,al,w)      
def iciclespears(self,other):
    al=1
    r=randroll()
    print(f" ❄️ {self.name} used "+colored(" Icicle Spear","cyan")+"!")
    c=critch(self,other)
    self.atktype="Ice"
    w=weathereff(self)
    base=25
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,base,a,b,c,r,al,w)       
def pinmissile (self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Pin Missile","green")+"!")
    c=critch(self,other)
    self.atktype="Bug"
    base=25
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,base,a,b,c,r,al)   
def populationbomb(self,other):
    al=1
    r=randroll()
    print(f" 💣 {self.name} used "+colored(" Population Bomb","white")+"!")
    c=critch(self,other)
    self.atktype="Normal"
    base=20
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,base,a,b,c,r,al)      
def twinbeam(self,other):
    al=1
    r=randroll()
    print(f" 🦒 {self.name} used "+colored(" Twin Beam","magenta")+"!")
    c=critch(self,other)
    self.atktype="Psychic"
    base=40
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,base,a,b,c,r,al)    
def geargrind(self,other):
    al=1
    r=randroll()
    print(f" ⚙️ {self.name} used "+colored(" Gear Grind","white")+"!")
    c=critch(self,other)
    self.atktype="Steel"
    base=50
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,base,a,b,c,r,al)    
def tripledive(self,other):
    al=1
    r=randroll()
    w=weathereff(self)
    print(f" {self.name} used "+colored(" Triple Dive","blue")+"!")
    c=critch(self,other)
    self.atktype="Water"
    base=30
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,base,a,b,c,r,al,w)  
          
def ironbash(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Double Iron Bash","white")+"!")
    c=critch(self,other)
    self.atktype="Steel"
    base=60
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,base,a,b,c,r,al)     
    ch=random.randint(1,100)
    if ch>70 and self.ability!="Sheer Force" and other.ability not in ["Inner Focus","Shield Dust"]:
        other.flinched=True      
def watershuriken(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Water Shuriken","blue")+"!")
    c=critch(self,other)
    self.atktype="Water"
    base=15
    if self.ability=="Battle Bond":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,base,a,b,c,r,al)           
def brickbreak(self,other,optr):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Brick Break","red")+"!")
    c=critch(self,other)
    self.atktype="Fighting"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self.level,self.atk,other.defense,70,a,b,c,r,al)       
    self.atk=self.maxatk*self.atkb
    self.spatk=self.maxspatk*self.spatkb
    if optr.lightscreen is True:
        optr.lightscreen=False
        print(f" {self.name} broke the Light Screen.")
    if optr.reflect is True:
        optr.reflect=False
        print(f" {self.name} broke the Reflect.")
def megahorn(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Megahorn","green")+"!")
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
        print(f" {self.name}'s {self.ability}.")
    print(f" ❄️ {self.name} used "+colored(" Ice Beam","cyan")+"!")
    c=critch(self,other)
    self.atktype="Ice"
    w=weathereff(self)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al,w)
    ch=random.randint(1,10)
    if ch==7 and other.status=="Alive" and other.ability not in ["Shield Dust"]:
        other.status=random.choice(["Frozen","Frostbite"])
        print(f" ❄️ {other.name} was frozen.")
def glaciate(self,other):
    al=1
    r=randroll()
    print(f" ❄️ {self.name} used "+colored(" Glaciate","cyan")+"!")
    c=critch(self,other)
    self.atktype="Ice"
    w=weathereff(self)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,65,a,b,c,r,al,w)
    speedchange(other,-0.5)
    print(f" {other.name}: Speed x{other.speedb}")
def flowertrick(self,other):
    al=1
    r=randroll()
    print(f" 💐 {self.name} used "+colored(" Flower Trick","green")+"!")
    c=critch(self,other,16)
    self.atktype="Grass"
    w=weathereff(self)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=65
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    other.hp-=physical(self.level,self.atk,other.defense,base,a,b,c,r,al,w)            
def frostbreath(self,other):
    al=1
    r=randroll()
    print(f" ❄️ {self.name} used "+colored(" Frost Breath","cyan")+"!")
    c=critch(self,other,16)
    self.atktype="Ice"
    w=weathereff(self)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=65
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    other.hp-=special(self.level,self.spatk,other.spdef,base,a,b,c,r,al,w)    
def psyshock(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Psyshock","magenta")+"!")
    c=critch(self,other)
    self.atktype="Psychic"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.defense,80,a,b,c,r,al)      
def darkhole(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    print(f" {self.name} used "+colored(" Dark Hole","red")+"!")
    c=critch(self,other)
    self.atktype="Dark"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,100,a,b,c,r,al)  
    ch=random.randint(1,100)    
    if ch>60 and other.ability not in ["Insomnia"] and other.status=="Alive":
        other.status="Sleep"
        
def darkpulse(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    print(f" {self.name} used "+colored(" Dark Pulse","red")+"!")
    c=critch(self,other)
    self.atktype="Dark"
    if self.ability=="Mega Launcher":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,80,a,b,c,r,al)  
    ch=random.randint(1,100)
    if ch>80 and self.ability!="Sheer Force" and other.ability not in ["Inner Focus","Shield Dust"]:
        other.flinched=True    
def strangesteam(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    print(f" {self.name} used "+colored(" Strange Steam","magenta")+"!")
    c=critch(self,other)
    self.atktype="Fairy"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al)  
    ch=random.randint(1,100)
    if ch>80 and self.ability!="Sheer Force" and other.ability not in ["Inner Focus","Shield Dust"]:
        other.confused=True
def freezingglare(self,other):
    al=1
    w=1
    r=randroll()
    print(f" {self.name} used "+colored(" Freezing Glare","magenta")+"!")
    c=critch(self,other)
    self.atktype="Psychic"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al,w)  
    ch=random.randint(1,100)
    if ch>90 and other.status=="Alive":
        other.status=random.choice(["Frozen","Frostbite"])
        print(f" ❄️ {other.name} was frozen.")
def expandingforce(self,other):
    al=1
    w=1
    r=randroll()
    if field.terrain=="Psychic":
        w*=1.5
    print(f" {self.name} used "+colored(" Expanding Force","magenta")+"!")
    c=critch(self,other)
    self.atktype="Psychic"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,80,a,b,c,r,al,w)  
def risingvoltage(self,other):
    al=1
    w=1
    r=randroll()
    if field.terrain=="Electric":
        w*=1.5
    print(f" ⚡ {self.name} used "+colored(" Rising Voltage","yellow")+"!")
    c=critch(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,70,a,b,c,r,al,w)      
def extrasensory (self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    print(f" {self.name} used "+colored(" Extrasensory","magenta")+"!")
    c=critch(self,other)
    self.atktype="Psychic"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al)  
    ch=random.randint(1,100)
    if ch>90 and self.ability!="Sheer Force" and other.ability not in ["Inner Focus","Shield Dust"]:
        other.flinched=True
def nightdaze(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    print(f" {self.name} used "+colored(" Night Daze","red")+"!")
    c=critch(self,other)
    self.atktype="Dark"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,95,a,b,c,r,al)  
    other.accuracy-=10
def bittermalice(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    print(f" {self.name} used "+colored(" Bitter Malice","magenta")+"!")
    c=critch(self,other)
    self.atktype="Ghost"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=75
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    if other.status!="Alive":
        base*=2
    other.hp-=special(self.level,self.spatk,other.spdef,base,a,b,c,r,al) 
    atkchange(other,-0.5)
    print(f" {other.name}: Attack x{other.atkb}")
    ch=random.randint(1,100)
    if ch>70 and other.status=="Alive":
        other.status="Frostbite"
        print(f" {other.name} got frostbite.")
def dracobarrage(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Draco Barrage","red")+"!")
    c=critch(self,other)
    self.atktype="Dragon"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=0
    if a==0:
        a=1
    if self.spatk>self.atk:
        dmg=special(self.level,self.spatk,other.spdef,100,a,b,c,r,al)  
    if self.atk>self.spatk:
        dmg=physical(self.level,self.atk,other.defense,100,a,b,c,r,al)    
    other.hp-=dmg
    if other.hp<0:
        other.hp=0
    self.hp-=(other.maxhp-other.hp)*0.33
        
def photongeyser(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Photon Geyser","magenta")+"!")
    c=critch(self,other)
    self.atktype="Psychic"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,100,a,b,c,r,al)  
    if self.atk>self.spatk:
        other.hp-=physical(self.level,self.atk,other.defense,100,a,b,c,r,al)             
def prismaticlaser(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Prismatic Laser","magenta")+"!")
    c=critch(self,other)
    self.atktype="Psychic"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,160,a,b,c,r,al)      
def hyperbeam(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Hyper Beam","white")+"!")
    c=critch(self,other)
    self.atktype="Normal"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al)
def hypervoice(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Hyper Voice","white")+"!")
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
    print(f" {self.name} used "+colored(" Roar of Time","blue")+"!")
    c=critch(self,other)
    self.atktype="Dragon"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
def rockwrecker(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Rock Wrecker","red")+"!")
    c=critch(self,other)
    self.atktype="Rock"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,150,a,b,c,r,al)     
def meteorassault(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Meteor Assault","red")+"!")
    c=critch(self,other)
    self.atktype="Fighting"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,150,a,b,c,r,al)                 
def gigaimpact(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Giga Impact","white")+"!")
    c=critch(self,other)
    self.atktype="Normal"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,150,a,b,c,r,al)             
def dragonpulse(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Dragon Pulse","red")+"!")
    c=critch(self,other)
    self.atktype="Dragon"
    if self.ability=="Mega Launcher":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al)   
def eternabeam(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Eternabeam","blue")+"!")
    c=critch(self,other)
    self.atktype="Dragon"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,160,a,b,c,r,al)       
def dynamaxcannon(self,other):
    al=1
    r=randroll()
    print(f" 🔺 {self.name} used "+colored(" Dynamax Cannon","red")+"!")
    c=critch(self,other)
    self.atktype="Dragon"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=100
    if other.dmax==True:
        base*=2
    other.hp-=special(self.level,self.spatk,other.spdef,base,a,b,c,r,al)       
def spacialrend(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Spacial Rend","magenta")+"!")
    c=critch(self,other,2)
    self.atktype="Dragon"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,100,a,b,c,r,al)       
def dazzlinggleam(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Dazzling Gleam","magenta")+"!")
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
    print(f" {self.name} used "+colored(" Lava Plume","red")+"!")
    c=critch(self,other)
    
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al,w)       
    ch=random.randint(1,100)
    if ch>70 and other.type1!="Fire" and other.type2!="Fire" and other.ability!="Flash Fire" and other.status=="Alive":
        other.status="Burned"
        print(f" 🔥 {other.name} was burned.")
def hurricane (self,other):
    al=1
    r=randroll()
    print(f" 🌪️ {self.name} used "+colored(" Hurricane","cyan")+"!")
    c=critch(self,other)
    self.atktype="Flying"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,110,a,b,c,r,al)          
    ch=random.randint(1,100)
    if ch>70 and other.confused is False:
        other.confused=True
def inferno(self,other):
    self.atktype="Fire"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Inferno","red")+"!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,120,a,b,c,r,al,w)
    if other.type1!="Fire" and other.type2!="Fire" and other.ability!="Flash Fire"     and other.status=="Alive"    :
        other.status="Burned"
        print(f" 🔥 {other.name} was burned.")
        
def overheat(self,other):
    self.atktype="Fire"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Overheat","red")+"!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,130,a,b,c,r,al,w)                
    spatkchange (self,-1)
    print(f" Special Attack x{self.spatkb}")
def blastburn(self,other):
    self.atktype="Fire"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Blast Burn","red")+"!")
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
    print(f" {self.name} used "+colored(" Frenzy Plant","green")+"!")
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
    print(f" {self.name} used "+colored(" Hydro Cannon","blue")+"!")
    if self.ability=="Mega Launcher":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
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
    print(f" {self.name} used "+colored(" Sparkling Aria","blue")+"!")
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
    print(f" 🌋 {self.name} used "+colored(" Eruption","red")+"!")
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
    print(f" 🐉 {self.name} used "+colored(" Dragon Energy","red")+"!")
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
    print(f" ⛲ {self.name} used "+colored(" Water Spout","blue")+"!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=round(150*(self.hp/self.maxhp))
    other.hp-=special(self.level,self.spatk,other.spdef,base,a,b,c,r,al,w)    
def crushgrip (self,other):
    self.atktype="Normal"
    al=1
    r=randroll()
    print(f" ✊🏻 {self.name} used "+colored(" Crush Grip","white")+"!")
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
        print(f" {self.name}'s {self.ability}.")
    print(f" 🌕 {self.name} used "+colored(" Moonblast","magenta")+"!")
    c=critch(self,other)
    self.atktype="Fairy"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al)      
    chance=30
    if self.ability=="Serene Grace":
        chance*=2
    if self.speed>other.speed:
        ch=random.randint(1,100)            
        if ch>(100-chance) and self.ability!="Sheer Force" and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil","Shield Dust"]:
            spatkchange (other,-0.5)
            print(f" {other.name}: Special Attack x{other.spatkb}")
def sludgebomb(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    print(f" 💣 {self.name} used "+colored(" Sludge Bomb","magenta")+"!")
    c=critch(self,other)
    self.atktype="Poison"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al)                
    ch=random.randint(1,100)
    if ch>90 and other.status=="Alive" and other.type1!="Steel" and other.type2!="Steel" and other.type1!="Poison" and other.type2!="Poison" and other.ability!="Immunity" and other.ability not in ["Shield Dust"]:
        other.status="Badly Poisoned"
def sludgewave(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    print(f" 〰️ {self.name} used "+colored(" Sludge Wave","magenta")+"!")
    c=critch(self,other)
    self.atktype="Poison"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,95,a,b,c,r,al)                
    ch=random.randint(1,100)
    if ch>90 and other.status=="Alive" and other.type1!="Steel" and other.type2!="Steel" and other.type1!="Poison" and other.type2!="Poison" and other.ability!="Immunity" and other.ability not in ["Shield Dust"]:
        other.status="Badly Poisoned"        
def hydropump(self,other):
    self.atktype="Water"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f" 🌊 {self.name} used "+colored(" Hydro Pump","blue")+"!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,110,a,b,c,r,al,w)  
def earthpower(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" ⛰️ {self.name}'s {self.ability}.")
    print(f" {self.name} used "+colored(" Earth Power","yellow")+"!")
    c=critch(self,other)
    self.atktype="Ground"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al)
    ch=random.randint(1,100)
    if ch>90 and self.ability!="Sheer Force" and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil","Shield Dust"]:
        spdefchange (other,-0.5)
        print(f" {other.name}: Special Defense x{other.spdefb}")
def stompingtantrum(self,other):
    al=1
    r=randroll()
    print(f" 👣 {self.name} used "+colored(" Stomping Tantrum","yellow")+"!")
    c=critch(self,other)
    self.atktype="Ground"
    if self.ability=="Striker":
        print(f" {self.name}'s {self.ability}!")
        al=1.3
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
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
    print(f" 🚜 {self.name} used "+colored(" Bulldoze","yellow")+"!")
    c=critch(self,other)
    self.atktype="Ground"
    if field.terrain=="Grassy":
        print(" Bulldozes damage was reduced by Grassy Terrain!")
        al*=0.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=60
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    other.hp-=physical (self.level,self.atk,other.defense,base,a,b,c,r,al)    
    speedchange(other,-0.5)
    print(f" {other.name}: Speed x{other.speedb}")
def rocktomb(self,other):
    al=1
    r=randroll()
    print(f" 🪨❌ {self.name} used "+colored(" Rock Tomb","yellow")+"!")
    c=critch(self,other)
    self.atktype="Rock"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=60
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    other.hp-=physical (self.level,self.atk,other.defense,base,a,b,c,r,al)    
    speedchange(other,-0.5)
    print(f" {other.name}: Speed x{other.speedb}")    
#Magnitude     
def magnitude(self,other):
    al=1
    r=randroll()
    mag=random.choices([4,5,6,7,8,9,10],weights=[5,10,20,30,20,10,5],k=1)[0]
    print(f" ⛰️ {self.name} used Magnitude {mag}.")
    c=critch(self,other)
    self.atktype="Ground"
    if field.terrain=="Grassy":
        print(" Magnitudes damage was reduced by Grassy Terrain!")
        al*=0.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    if mag<10:
        base=10+(20*mag-4)   
    if mag==10:
        base=150
    other.hp-=physical (self.level,self.atk,other.defense,base,a,b,c,r,al)         
def hyperdrill(self,other):
    al=1
    r=randroll()
    print(f" 🪛  {self.name} used "+colored(" Hyper Drill","white")+"!")
    c=critch(self,other)
    self.atktype="Normal"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,100,a,b,c,r,al)    
#EARTHQUAKE        
def earthquake (self,other):
    al=1
    r=randroll()
    print(f" ⛰️ {self.name} used "+colored(" Earthquake","yellow")+"!")
    c=critch(self,other)
    self.atktype="Ground"
    if field.terrain=="Grassy":
        print(" Earthquakes damage was reduced by Grassy Terrain!")
        al*=0.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,100,a,b,c,r,al)
def landswrath(self,other):
    al=1
    r=randroll()
    print(f" ⛰️ {self.name} used "+colored(" Land's Wrath","green")+"!")
    c=critch(self,other)
    self.atktype="Ground"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,90,a,b,c,r,al)    
def thousandwaves(self,other):
    al=1
    r=randroll()
    print(f" 〰️ {self.name} used "+colored(" Thousand Waves","green")+"!")
    c=critch(self,other)
    self.atktype="Ground"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,90,a,b,c,r,al)        
def thousandarrows(self,other):
    al=1
    r=randroll()
    print(f" 🏹 {self.name} used "+colored(" Thousand Arrows","green")+"!")
    c=critch(self,other)
    self.atktype="Ground"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if a==0:
        a=1
    other.hp-=physical (self.level,self.atk,other.defense,90,a,b,c,r,al)        
def coreenforcer(self,other):
    al=1
    r=randroll()
    print(f" ⚕️ {self.name} used "+colored(" Core Enforcer","green")+"!")
    c=critch(self,other)
    self.atktype="Dragon"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,100,a,b,c,r,al)        
def highhorsepower(self,other):
    al=1
    r=randroll()
    print(f" 🐎 {self.name} used "+colored(" High Horsepower","yellow")+"!")
    c=critch(self,other)
    self.atktype="Ground"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,95,a,b,c,r,al)
def headlongrush (self,other):
    al=1
    r=randroll()
    print(f" 🐻 {self.name} used "+colored(" Headlong Rush","yellow")+"!")
    c=critch(self,other)
    self.atktype="Ground"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,120,a,b,c,r,al)
    if a!=0:
        defchange (self,-0.5)
        print(f" Defense x{self.defb}")
        spdefchange (self,-0.5)
        print(f" Special Defense x{self.spdefb}")
def firelash(self,other):
    self.atktype="Fire"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f" ⛓️ {self.name} used "+colored(" Fire Lash","red")+"!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al,w)    
    if other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        defchange (other,-0.5)
        print(f" {other.name}: Defense x{other.defb}")
def mysticalfire(self,other):
    self.atktype="Fire"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f" 🔥 {self.name} used "+colored(" Mystical Fire","red")+"!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,75,a,b,c,r,al,w)    
    if other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        spatkchange (other,-0.5)
        print(f" {other.name}: Special Attack x{other.spatkb}")    
def lunge(self,other):
    self.atktype="Bug"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f" 🪲 {self.name} used "+colored(" Lunge","green")+"!")
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al,w)         
    atkchange (other,-0.5)   
    print(f" {other.name}: Attack x{other.atkb}")
def shelltrap(self,other):
    self.atktype="Fire"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f" 🐢 {other.name} got blown up by  "+colored(" Shell Trap","red")+"!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,150,a,b,c,r,al,w)         
        
def thunderouskick(self,other):
    self.atktype="Fighting"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Thunderous Kick","red")+"!")
    if self.ability=="Striker":
        print(f" {self.name}'s {self.ability}!")
        al=1.3
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,90,a,b,c,r,al,w)    
    ch=random.randint(1,100)
    if ch>80 and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        defchange (other,-0.5)
        print(f" {other.name}: Defense x{other.defb}")    
def chillingwater(self,other):
    self.atktype="Water"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f" 💦 {self.name} used "+colored(" Chilling Water","blue")+"!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,50,a,b,c,r,al,w)
    if other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        atkchange (other,-0.5)
        print(f" {other.name}: Attack x{other.atkb}")        
def pounce(self,other):
    self.atktype="Bug"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f" 🪲 {self.name} used "+colored(" Pounce","green")+"!")
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,50,a,b,c,r,al,w)
    if other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        speedchange (other,-0.5)
        print(f" {other.name}: Speed x{other.speedb}")        
def skittersmack(self,other):
    self.atktype="Bug"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f" 🪲 {self.name} used "+colored(" Pounce","green")+"!")
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,70,a,b,c,r,al,w)
    if other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        spatkchange (other,-0.5)
        print(f" {other.name}: Special Attack x{other.spatknb}")                
def liquidation (self,other):
    self.atktype="Water"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f" 🗡️ {self.name} used "+colored(" Liquidation","blue")+"!")
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al,w)    
    ch=random.randint(1,100)
    if ch>80 and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        defchange (other,-0.5)
        print(f" {other.name}: Defense x{other.defb}")
def mysticalpower(self,other):
    self.atktype="Psychic"
    al=1
    r=randroll()
    print(f" 👁️‍🗨️ {self.name} used "+colored(" Mystical Power","magenta")+"!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,70,a,b,c,r,al)
    spatkchange(self,0.5)
    print(f" Special Attack x{self.spatkb}")        
def torchsong(self,other):
    self.atktype="Fire"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f" 🕯️ {self.name} used "+colored(" Torch Song","red")+"!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,80,a,b,c,r,al,w)
    spatkchange(self,0.5)
    print(f" Special Attack x{self.spatkb}")         
def aquastep(self,other):
    self.atktype="Water"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f" 💦 {self.name} used "+colored(" Aqua Step","blue")+"!")
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al,w)
    speedchange(self,0.5)
    print(f" Speed x{self.speedb}") 
def tropkick(self,other):
    self.atktype="Grass"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f" 🌳 {self.name} used "+colored(" Trop Kick","green")+"!")
    if self.ability=="Striker":
        al*=1.3
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,70,a,b,c,r,al,w)
    atkchange(other,-0.5)
    print(f" {other.name}'s attack fell!")     
def razorshell(self,other):
    self.atktype="Water"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f" 🐚 {self.name} used "+colored(" Razor Shell","blue")+"!")
    if self.ability=="Sharpness":
        al*=1.5
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,75,a,b,c,r,al,w)    
    ch=random.randint(1,100)
    if ch>50 and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        defchange (other,-0.5)
        print(f" {other.name}: Defense x{other.defb}") 
def diamondstorm(self,other):
    self.atktype="Rock"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f" 💎 {self.name} used "+colored(" Diamond Storm","magenta")+"!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special (self.level,self.spatk,other.spdef,100,a,b,c,r,al,w)    
    ch=random.randint(1,100)
    if ch>50 and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        defchange (other,-0.5)
        print(f" {other.name}: Defense x{other.defb}")                
def wavecrash(self,other):
    self.atktype="Water"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f" 🌊 {self.name} used "+colored(" Wave Crash","blue")+"!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,120,a,b,c,r,al,w)    
    if self.ability=="Reckless":
        dmg*=1.2
    if dmg>other.hp:
        dmg=other.hp
        other.hp=0
    else:
        other.hp-=dmg
    if self.ability!="Rock Head":
        self.hp-=round(dmg/3)
        print(f" {self.name} was hurt by recoil.")
    
def dynapunch(self,other):
    al=1
    r=randroll()
    print(f" 👊🏽 {self.name} used "+colored(" Dynamic Punch","red")+"!")   
    c=critch(self,other)
    self.atktype="Fighting"
    if self.item=="Punching Glove":
        al=1.5
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    if self.ability=="Iron Fist":
        print(f" {self.name}'s {self.ability}!")
        al=1.3
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,100,a,b,c,r,al)      
    if other.confused is False:
        other.confused=True
def armorcannon(self,other):
    al=1
    r=randroll()
    print(f" 🪖 {self.name} used "+colored(" Armor Cannon","red")+"!")
    if self.ability=="Mega Launcher":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
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
        print(f" Defense x{self.defb}")
        print(f" Special Defense x{self.spdefb}") 
def electrodrift(self,other):
    al=1
    r=randroll()
    print(f" 🧞 {self.name} used "+colored(" Electro Drift","yellow")+"!")
    c=critch(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if a>2:
        a*=1.5
    other.hp-=special(self.level,self.spatk,other.spdef,100,a,b,c,r,al)                
def collisioncourse(self,other):
    al=1
    r=randroll()
    print(f" 🏍️ {self.name} used "+colored(" Collision Course","red")+"!")
    c=critch(self,other)
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if a>2:
        a*=1.5
    other.hp-=physical (self.level,self.atk,other.defense,100,a,b,c,r,al)       
def smellingsalts(self,other):
    al=1
    r=randroll()
    print(f" 💥 {self.name} used "+colored(" Smelling Salts","red")+"!")
    c=critch(self,other)
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=70
    if other.status=="Paralyzed":
        base*=2
    other.hp-=physical (self.level,self.atk,other.defense,base,a,b,c,r,al)            
    if a!=0 and other.status=="Paralyzed":
        other.status="Alive"
                 
def closecombat(self,other):
    al=1
    r=randroll()
    print(f" 💥 {self.name} used "+colored(" Close Combat","red")+"!")
    c=critch(self,other)
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,120,a,b,c,r,al)       
    if a!=0:
        defchange(self,-0.5)
        spdefchange(self,-0.5)
        print(f" Defense x{self.defb}")
        print(f" Special Defense x{self.spdefb}")
def bulletpunch(self,other):
    al=1
    r=randroll()
    print(f" 👊🏻 {self.name} used "+colored(" Bullet Punch","white")+"!")
    c=critch(self,other)
    self.atktype="Steel"
    if self.item=="Punching Glove":
        al=1.5
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    if self.ability=="Iron Fist":
        print(f" {self.name}'s {self.ability}!")
        al=1.3
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    base=40
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    other.hp-=physical (self.level,self.atk,other.defense,base,a,b,c,r,al)        
def shadowsneak(self,other):
    al=1
    r=randroll()
    print(f" 👻 {self.name} used "+colored(" Shadow Sneak","magenta")+"!")
    c=critch(self,other)
    self.atktype="Ghost"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    base=40
    other.hp-=physical (self.level,self.atk,other.defense,base,a,b,c,r,al)            
def voltswitch(self,other):
    al=1
    r=randroll()
    print(f" ⚡↪️ {self.name} used "+colored(" Volt Switch","yellow")+"!")
    c=critch(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,70,a,b,c,r,al)       
def flipturn(self,other):
    al=1
    r=randroll()
    print(f" 💦↪️ {self.name} used "+colored(" Flip Turn","blue")+"!")
    c=critch(self,other)
    self.atktype="Water"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,70,a,b,c,r,al)         
def uturn(self,other):
    al=1
    r=randroll()
    print(f" 🪲↪️ {self.name} used "+colored(" U-Turn","green")+"!")
    c=critch(self,other)
    self.atktype="Bug"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,70,a,b,c,r,al)               
def xscissor (self,other):
    al=1
    r=randroll()
    print(f" ⚔️ {self.name} used "+colored(" X-Scissor","green")+"!")
    c=critch(self,other)
    self.atktype="Bug"
    if self.ability=="Sharpness":
        al*=1.5
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,90,a,b,c,r,al)           
def superpower(self,other):
    al=1
    r=randroll()
    print(f" 🦸 {self.name} used "+colored(" Superpower","red")+"!")
    c=critch(self,other)
    self.atktype="Fighting"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,120,a,b,c,r,al)   
    if a!=0:
        defchange(self,-0.5)
        atkchange(self,-0.5)
        print(f" Attack x{self.atkb}")
        print(f" Defense x{self.defb}")
    
def dragonhammer(self,other):
    al=1
    r=randroll()
    print(f" 🔨 {self.name} used "+colored(" Dragon Hammer","red")+"!")
    c=critch(self,other)
    self.atktype="Dragon"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,100,a,b,c,r,al)        
def lightscreen(self,other,tr1,turn):    
    print(f" 🟨 {self.name} used "+colored(" Light Screen","yellow")+"!")
    if tr1.lightscreen is True:
        print(" It failed!")
    if tr1.lightscreen is False:
        tr1.lightscreen=True
        print(" Light Screen raised your team's Special Defense!")
        tr1.lsturn=turn
        tr1.lightscreenend(self,other)
def tailwind(self,other,tr1,turn):    
    print(f" 🍃 {self.name} used "+colored(" Tailwind","cyan")+"!")
    if tr1.tailwind is True:
        print(" It failed!")
    if tr1.tailwind is False:
        tr1.tailturn=turn
        tr1.twend(self,other)
        tr1.tailwind=True  
        print(" The Tailwind blew from behind your team.")        
def reflect(self,other,tr1,turn):    
    print(f" 🟪 {self.name} used "+colored(" Reflect","magenta")+"!")
    if tr1.reflect is True:
        print(" It failed!")
    if tr1.reflect is False:
        tr1.reflecturn=turn
        tr1.reflectend(self,other)
        tr1.reflect=True  
        print(" Reflect raised your team's Defense!")
        
def auroraveil(self,other,tr1,turn):    
    print(f" ⬜ {self.name} used "+colored(" Aurora Veil","cyan")+"!")
    if tr1.auroraveil is True and ("Gigantamax Lapras" not in self.name or field.weather not in ["Hail","Snowstorm"]):
        print(" It failed!")
    if tr1.auroraveil is False and ("Gigantamax Lapras" in self.name or field.weather in ["Hail","Snowstorm"]):
        tr1.auroraurn=turn
        tr1.auroraend(self,other)
        tr1.auroraveil=True  
        print(" Aurora Veil will reduced your team's damage taken!")        
def zenheadbutt(self,other):
    al=1
    r=randroll()
    print(f" 🧘🏻 {self.name} used "+colored(" Zen Headbutt","magenta")+"!")
    c=critch(self,other)
    self.atktype="Psychic"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)  
    ch=random.randint(1,100)
    if ch>80 and other.ability not in ["Inner Focus"]:
        other.flinched=True
def icespinner(self,other):
    al=1
    r=randroll()
    print(f" 🌪️❄️ {self.name} used "+colored(" Ice Spinner","cyan")+"!")
    c=critch(self,other)
    self.atktype="Ice"
    w=weathereff(self)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al,w)  
    if field.terrain!="Normal":
        field.terrain="Normal"
        print(" 🌐 The battlefield turned normal.")
def tripleaxel(self,other):
    al=1
    r=randroll()
    print(f" 🏔️ {self.name} used "+colored(" Triple Axel","cyan")+"!")
    self.atktype="Ice"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.ability=="Striker":
        al*=1.3
    w=weathereff(self)
    ch=random.randint(1,100)
    if ch<90:
        c=critch(self,other)
        other.hp-=physical (self.level,self.atk,other.defense,20,a,b,c,r,al,w)    
        ch=random.randint(1,100)
        if ch<90:
            c=critch(self,other)
            ab=weakness(self,other,field)
            a=ab[0]
            b=ab[1]   
            other.hp-=physical (self.level,self.atk,other.defense,40,a,b,c,r,al,w)  
            ch=random.randint(1,100)    
            if ch<90:
                c=critch(self,other)
                other.hp-=physical (self.level,self.atk,other.defense,60,a,b,c,r,al,w)
        else:
            print(" It missed.")              
def iciclecrash(self,other):
    al=1
    r=randroll()
    print(f" 🏔️ {self.name} used "+colored(" Icicle Crash","cyan")+"!")
    c=critch(self,other)
    self.atktype="Ice"
    w=weathereff(self)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,85,a,b,c,r,al,w)  
    ch=random.randint(1,100)
    if ch>70 and other.ability not in ["Inner Focus"]:
        other.flinched=True
def zingzap(self,other):
    al=1
    r=randroll()
    print(f" ⚡ {self.name} used "+colored(" Zing Zap","yellow")+"!")
    c=critch(self,other)
    self.atktype="Electric"
    w=weathereff(self)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al,w)  
    ch=random.randint(1,100)
    if ch>70 and other.ability not in ["Inner Focus"]:
        other.flinched=True
def needlearm(self,other):
    al=1
    r=randroll()
    print(f" 🌵 {self.name} used "+colored(" Needle Arm","green")+"!")
    c=critch(self,other)
    self.atktype="Grass"
    w=weathereff(self)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,95,a,b,c,r,al,w)  
    ch=random.randint(1,100)
    if ch>70 and other.ability not in ["Inner Focus"]:
        other.flinched=True
def firepunch(self,other):
    al=1
    r=randroll()
    w=weathereff(self)
    print(f" 🔥 {self.name} used "+colored(" Fire Punch","red")+"!")
    c=critch(self,other)
    self.atktype="Fire"
    if self.item=="Punching Glove":
        al=1.5
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    if self.ability=="Iron Fist":
        print(f" {self.name}'s {self.ability}!")
        al=1.3
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,75,a,b,c,r,al,w)      
    ch=random.randint(1,100)
    if ch>90 and other.status=="Alive":
        other.status="Burned"
        print(f" 🔥 {other.name} was burned.")
def spiritshackle(self,other):
    al=1
    r=randroll()
    print(f" 🏹 {self.name} used "+colored(" Spirit Shackle","magenta")+"!")
    c=critch(self,other)
    self.atktype="Ghost"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)           
    ch=random.randint(1,100)
    if ch>80 and other.ability not in ["Inner Focus","Shield Dust"]:
        other.flinched=True   
def firefang(self,other):
    al=1
    r=randroll()
    print(f" 🔥 {self.name} used "+colored(" Fire Fang","red")+"!")
    c=critch(self,other)
    self.atktype="Fire"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    if self.ability=="Strong Jaw":
        print(f" {self.name}'s {self.ability}!")
        al=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,70,a,b,c,r,al)      
    ch=random.randint(1,100)
    if ch>90 and other.status=="Alive" and other.ability not in ["Shield Dust"]:
        other.status="Burned"
        print(f" 🔥 {other.name} was burned.")
    ch=random.randint(1,100)
    if ch>90 and other.ability not in ["Inner Focus"]:
        other.flinched=True

def volttackle(self,other):
    self.atktype="Electric"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    w=weathereff(self)
    al=1
    r=randroll()
    print(f" ⚡ {self.name} used "+colored(" Volt Tackle","yellow")+"!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical(self.level,self.atk,other.defense,120,a,b,c,r,al,w)
    if self.ability=="Reckless":
        dmg*=1.2
    if dmg>other.hp:
        dmg=other.hp
        other.hp=0
    else:
        other.hp-=dmg
    if self.ability!="Rock Head" and a!=0:
        self.hp-=round(dmg/3)
        print(f" {self.name} was hurt by recoil.")         
    ch=random.randint(1,100)
    if ch>90 and other.status=="Alive" and other.ability!="Volt Absorb" and a!=0:
        other.status="Paralyzed"
        print(f" {other.name} was paralyzed.") 
def flareblitz(self,other):
    self.atktype="Fire"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    w=weathereff(self)
    al=1
    r=randroll()
    print(f" 🔥 {self.name} used "+colored(" Flare Blitz","red")+"!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical(self.level,self.atk,other.defense,120,a,b,c,r,al,w)
    if self.ability=="Reckless":
        dmg*=1.2
    if dmg>other.hp:
        dmg=other.hp
        other.hp=0
    else:
        other.hp-=dmg
    if self.ability!="Rock Head":
        self.hp-=round(dmg/3)
        print(f" {self.name} was hurt by recoil.")         
    ch=random.randint(1,100)
    if ch>90 and other.status=="Alive" and other.ability!="Flash Fire" and other.ability not in ["Shield Dust"]:
        other.status="Burned"
        print(f" 🔥 {other.name} was burned.")
        other.atk*=0.5 
def boltstrike(self,other):
    al=1
    r=randroll()
    print(f" ⚡ {self.name} used "+colored(" Bolt Strike","yellow")+"!")
    c=critch(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,130,a,b,c,r,al)  
    ch=random.randint(1,100)
    if ch>80 and other.status=="Alive" and a!=0:
        other.status="Paralyzed"
        print(f" {other.name} is paralyzed.")
        
def freezeshock(self,other):
    al=1
    r=randroll()
    print(f" ❄️⚡ {self.name} used "+colored(" Freeze Shock","cyan")+"!")
    c=critch(self,other)
    self.atktype="Ice"
    w=weathereff(self)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,140,a,b,c,r,al,w)  
    ch=random.randint(1,100)
    if ch>70 and other.status=="Alive" and other.ability not in ["Shield Dust"] and a!=0:
        other.status="Paralyzed"
        print(f" {other.name} is paralyzed.")
      
def fusionbolt(self,other):
    al=1
    r=randroll()
    print(f" ⚡ {self.name} used "+colored(" Fusion Bolt","yellow")+"!")
    c=critch(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,100,a,b,c,r,al)  
       
def tpunch(self,other):
    al=1
    r=randroll()
    print(f" ⚡ {self.name} used "+colored(" Thunder Punch","yellow")+"!")
    c=critch(self,other)
    self.atktype="Electric"
    if self.item=="Punching Glove":
        al=1.5
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    if self.ability=="Iron Fist":
        print(f" {self.name}'s {self.ability}!")
        al=1.3
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)  
    ch=random.randint(1,100)
    if ch>90 and other.status=="Alive" and a!=0:
        other.status="'Paralyzed"
        print(f" {other.name} is paralyzed.")
      
def poisontail(self,other):
    al=1
    r=randroll()
    print(f" 🐍 {self.name} used "+colored(" Poison Tail","magenta")+"!")
    c=critch(self,other,2)
    self.atktype="Poison"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,90,a,b,c,r,al)          
    ch=random.randint(1,100)
    if ch>70 and other.status=="Alive" and other.type1 not in ["Steel","Poison"] and other.type2 not in ["Steel","Poison"] and other.ability not in ["Immunity","Magic Bounce"]:
        other.status="Badly Poisoned"
        print(f" ☠️ {other.name} was badly poisoned.")            
def poisonfang(self,other):
    al=1
    r=randroll()
    print(f" 🐍 {self.name} used "+colored(" Poison Fang","magenta")+"!")
    c=critch(self,other)
    self.atktype="Poison"
    if self.ability=="Strong Jaw":
        print(f" {self.name}'s {self.ability}!")
        al=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,75,a,b,c,r,al)          
    ch=random.randint(1,100)
    if ch>70 and other.status=="Alive" and other.type1 not in ["Steel","Poison"] and other.type2 not in ["Steel","Poison"] and other.ability not in ["Immunity","Magic Bounce"]:
        other.status="Badly Poisoned"
        print(f" ☠️ {other.name} was badly poisoned.")    
def psychicfang(self,other):
    al=1
    r=randroll()
    print(f" 👁️ {self.name} used "+colored(" Psychic Fangs","magenta")+"!")
    c=critch(self,other)
    self.atktype="Psychic"
    if self.ability=="Strong Jaw":
        print(f" {self.name}'s {self.ability}!")
        al=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,75,a,b,c,r,al)          
def tfang(self,other):
    al=1
    r=randroll()
    print(f" ⚡ {self.name} used "+colored(" Thunder Fang","yellow")+"!")
    c=critch(self,other)
    self.atktype="Electric"
    if self.ability=="Strong Jaw":
        print(f" {self.name}'s {self.ability}!")
        al=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,75,a,b,c,r,al)  
    ch=random.randint(1,100)
    if ch>80 and other.status=="Alive" and a!=0:
        other.status="Paralyzed"
        print(f" {other.name} is paralyzed.")
      
def plasmafists(self,other):
    al=1
    r=randroll()
    print(f" ⚡ {self.name} used "+colored(" Plasma Fists","yellow")+"!")
    c=critch(self,other)
    self.atktype="Electric"
    if self.item=="Punching Glove":
        al=1.5
    if self.ability=="Iron Fist":
        print(f" {self.name}'s {self.ability}!")
        al=1.3
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,100,a,b,c,r,al)          
def suckerpunch(self,other):
    al=1
    r=randroll()
    print(f" 👿 {self.name} used "+colored(" Sucker Punch","white")+"!")
    c=critch(self,other)
    if self.item=="Punching Glove":
        al=1.5
    if self.ability=="Iron Fist":
        print(f" {self.name}'s {self.ability}!")
        al=1.3
    self.atktype="Dark"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)         
def machpunch(self,other):
    al=1
    r=randroll()
    print(f" 👊🏼 {self.name} used "+colored(" Mach Punch","red")+"!")
    c=critch(self,other)
    self.atktype="Fighting"
    if self.item=="Punching Glove":
        al=1.5
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    if self.ability=="Iron Fist":
        print(f" {self.name}'s {self.ability}!")
        al=1.3
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,40,a,b,c,r,al)              
def iceshard(self,other):
    al=1
    r=randroll()
    print(f" ❄️ {self.name} used "+colored(" Ice Shard","cyan")+"!")
    w=weathereff(self)
    c=critch(self,other)
    self.atktype="Ice"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,40,a,b,c,r,al,w)          
def hornleech(self,other):
    al=1
    r=randroll()
    print(f" 🐮 {self.name} used "+colored(" Horn Leech","green")+"!")
    c=critch(self,other)
    self.atktype="Grass"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,75,a,b,c,r,al)      
    if a!=0:
        print(f" {other.name} had its energy drained!")
    if dmg>other.hp:
        dmg=other.hp
        other.hp-=dmg
    else:
        other.hp-=dmg
    heal=dmg/2
    if self.hp<=(self.maxhp-heal):
        self.hp+=heal
    else:
        self.hp=self.maxhp    
def bitterblade(self,other):
    al=1
    r=randroll()
    print(f" 🗡️ {self.name} used "+colored(" Bitter Blade","red")+"!")
    c=critch(self,other)
    self.atktype="Fire"
    w=weathereff(self)
    if self.ability=="Sharpness":
        al*=1.5
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,75,a,b,c,r,al,w)      
    if a!=0:
        print(f" {other.name} had its energy drained!")
    if dmg>other.hp:
        dmg=other.hp
        other.hp-=dmg
    else:
        other.hp-=dmg
    heal=dmg/2
    if self.hp<=(self.maxhp-heal):
        self.hp+=heal
    else:
        self.hp=self.maxhp 
def drainingkiss(self,other):
    al=1
    r=randroll()
    print(f" 💋 {self.name} used "+colored(" Draining Kiss","magenta")+"!")
    c=critch(self,other)
    self.atktype="Fairy"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,50,a,b,c,r,al)      
    if a!=0:
        print(f" {other.name} had its energy drained!")
    if dmg>other.hp:
        dmg=other.hp
        other.hp-=dmg
    else:
        other.hp-=dmg
    heal=dmg*0.75
    if self.hp<=(self.maxhp-heal):
        self.hp+=heal
    else:
        self.hp=self.maxhp               
def drainpunch(self,other):
    al=1
    r=randroll()
    print(f" 👊🏼 {self.name} used "+colored(" Drain Punch","red")+"!")
    c=critch(self,other)
    self.atktype="Fighting"
    if self.item=="Punching Glove":
        al=1.5
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    if self.ability=="Iron Fist":
        print(f" {self.name}'s {self.ability}!")
        al=1.3
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,75,a,b,c,r,al)      
    if a!=0:
        print(f" {other.name} had its energy drained!")
    if dmg>other.hp:
        dmg=other.hp
        other.hp-=dmg
    else:
        other.hp-=dmg
    heal=dmg/2
    if self.hp<=(self.maxhp-heal):
        self.hp+=heal
    else:
        self.hp=self.maxhp
def parabolic(self,other):
    al=1
    r=randroll()
    print(f" ⚡ {self.name} used "+colored(" Parabolic Charge","yellow")+"!")
    c=critch(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=special(self.level,self.spatk,other.spdef,75,a,b,c,r,al)
    if a!=0:
        print(f" {other.name} had its energy drained!")
    if dmg>other.hp:
        dmg=other.hp
        other.hp-=dmg
    else:
        other.hp-=dmg
    heal=dmg/2
    if self.hp<=(self.maxhp-heal):
        self.hp+=heal
    else:
        self.hp=self.maxhp        
        
def dizzypunch(self,other):
    al=1
    r=randroll()
    print(f" 😵 {self.name} used Dizzy Punch.")
    c=critch(self,other)
    self.atktype="Normal"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    if self.ability=="Iron Fist":
        print(f" {self.name}'s {self.ability}!")
        al=1.3
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,70,a,b,c,r,al)
    ch=random.randint(1,100)
    if ch>80 and other.confused is False:
        other.confused=True
def strength (self,other):
    al=1
    r=randroll()
    print(f" {self.name} used Strength.")
    c=critch(self,other)
    self.atktype="Normal"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)          
def icepunch(self,other):
    al=1
    r=randroll()
    print(f" ❄️ {self.name} used "+colored(" Ice Punch","cyan")+"!")
    w=weathereff(self)
    c=critch(self,other)
    self.atktype="Ice"
    if self.item=="Punching Glove":
        al=1.5
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    if self.ability=="Iron Fist":
        print(f" {self.name}'s {self.ability}!")
        al=1.3
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al,w)                  
    ch=random.randint(1,100)
    if ch>90 and other.status=="Alive":
        other.status=random.choice(["Frozen","Frostbite"])
        print(f" ❄️ {other.name} was frozen.")
def bodyslam(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Body Slam","white")+"!")
    c=critch(self,other)
    self.atktype="Normal"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)     
    other.hp-=dmg
    chance=30
    if self.ability=="Serene Grace":
        chance*=2
    if self.speed>other.speed:
        ch=random.randint(1,100)            
        if ch>(100-chance) and other.status=="Alive" and a!=0:
            other.status="Paralyzed"
            print(f" ⚡ {other.name} is paralyzed.")
         
def forcepalm(self,other):
    al=1
    r=randroll()
    print(f" ✋🏾 {self.name} used "+colored(" Force Palm","red")+"!")
    c=critch(self,other)
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=60
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    other.hp-=physical (self.level,self.atk,other.defense,base,a,b,c,r,al)     
    ch=random.randint(1,100)
    if ch>70 and other.status=="Alive" and a!=0:
        other.status="Paralyzed"
        print(f" {other.name} is paralyzed.")
     
def drillrun(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Drill Run","yellow")+"!")
    c=critch(self,other,2)
    self.atktype="Ground"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)     
def smartstrike(self,other):
    al=1
    r=randroll()
    print(f" 🗡️ {self.name} used "+colored(" Smart Strike","white")+"!")
    c=critch(self,other,2)
    self.atktype="Steel"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,70,a,b,c,r,al)   
def anchorshot(self,other):
    al=1
    r=randroll()
    print(f" ⚓ {self.name} used "+colored(" Anchor Shot","white")+"!")
    c=critch(self,other,2)
    self.atktype="Steel"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)             
def lightofruin(self,other):
    al=1
    r=randroll()
    print(f" 🌸 {self.name} used "+colored(" Light of Ruin","magenta")+"!")
    c=critch(self,other)
    self.atktype="Fairy"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=special (self.level,self.spatk,other.spdef,140,a,b,c,r,al)   
    if self.ability=="Reckless":
        dmg*=1.2    
    if other.hp<dmg:
        dmg=other.hp
        other.hp-=dmg
    else:
        other.hp-=dmg        
    if self.ability!="Rock Head":
        print(f" {self.name} was hurt by recoil.")
        self.hp-=dmg/2    
def mindblown(self,other):
    al=1
    r=randroll()
    print(f" 🎆 {self.name} used "+colored(" Mind Blown","red")+"!")
    c=critch(self,other)
    self.atktype="Fire"
    w=weathereff(self)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=special (self.level,self.spatk,other.spdef,150,a,b,c,r,al,w)   
    if self.ability=="Reckless":
        dmg*=1.2    
    if other.hp<dmg:
        dmg=other.hp
        other.hp-=dmg
    else:
        other.hp-=dmg        
    if self.ability!="Magic Guard":
        print(f" {self.name} was hurt by recoil.")
        self.hp-=self.maxhp/2                    
def chloroblast(self,other):
    al=1
    r=randroll()
    print(f" 🟢 {self.name} used "+colored(" Chloroblast","green")+"!")
    c=critch(self,other)
    self.atktype="Grass"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=special (self.level,self.spatk,other.spdef,120,a,b,c,r,al)       
    if self.ability=="Reckless":
        dmg*=1.2
    if other.hp<dmg:
        dmg=other.hp
        other.hp-=dmg
    else:
        other.hp-=dmg        
    if self.ability!="Rock Head":
        print(f" {self.name} was hurt by recoil.")
        self.hp-=self.maxhp/3        
def headsmash(self,other):
    al=1
    r=randroll()
    print(f" 🤕 {self.name} used "+colored(" Head Smash","yellow")+"!")
    c=critch(self,other)
    self.atktype="Rock"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,150,a,b,c,r,al)    
    if self.ability=="Reckless":
        dmg*=1.2   
    if other.hp<dmg:
        dmg=other.hp
        other.hp-=dmg
    else:
        other.hp-=dmg        
    if self.ability!="Rock Head":
        print(f" {self.name} was hurt by recoil.")
        self.hp-=dmg/2
def gunkshot(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Gunk Shot","magenta")+"!")
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
        print(f" ☠️ {other.name} was badly poisoned.")    
def belch(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Belch","magenta")+"!")
    c=critch(self,other)
    self.atktype="Poison"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=special(self.level,self.spatk,other.spdef,120,a,b,c,r,al)    
    other.hp-=dmg            
    self.hp-=(self.maxhp/3)
    print(f" {self.name} was hurt by extreme poison.")
def submission(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Submission","red")+"!")
    c=critch(self,other)
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)    
    if self.ability=="Reckless":
        dmg*=1.2
    if dmg>other.hp:
        dmg=other.hp
        other.hp=0
    else:
        other.hp-=dmg
    if self.ability!="Rock Head" and a!=0:
        self.hp-=round(dmg/4)
        print(f" {self.name} was hurt by recoil.")    
def headcharge(self,other):
    al=1
    r=randroll()
    print(f" 🐂 {self.name} used "+colored(" Head Charge","white")+"!")
    c=critch(self,other)
    self.atktype="Normal"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,120,a,b,c,r,al)    
    if self.ability=="Reckless":
        dmg*=1.2
    if dmg>other.hp:
        dmg=other.hp
        other.hp=0
    else:
        other.hp-=dmg
    if self.ability!="Rock Head" and a!=0:
        self.hp-=round(dmg/4)
        print(f" {self.name} was hurt by recoil.")        
def bravebird(self,other):
    al=1
    r=randroll()
    print(f" 🐦 {self.name} used "+colored(" Brave Bird","cyan")+"!")
    c=critch(self,other)
    self.atktype="Flying"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,120,a,b,c,r,al)    
    if self.ability=="Reckless":
        dmg*=1.2
    if dmg>other.hp:
        dmg=other.hp
        other.hp=0
    else:
        other.hp-=dmg
    if self.ability!="Rock Head" and a!=0:
        self.hp-=round(dmg/3)
        print(f" {self.name} was hurt by recoil.")
def spectralthief(self,other,tr):
    al=1
    r=randroll()
    print(f" 🫡 {self.name} used "+colored(" Spectral Thief","magenta")+"!")
    c=critch(self,other)
    self.atktype="Ghost"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=90
    dmg=physical(self.level,self.atk,other.defense,base,a,b,c,r,al)   
    other.hp-=dmg         
    self.atkb,self.defb,self.spatkb,self.spdefb,self.speedb=other.atkb,other.defb,other.spatkb,other.spdefb,other.speedb
    other.atkb,other.defb,other.spatkb,other.spdefb,other.speedb=1,1,1,1,1
def soulrobbery(self,other,tr):
    al=1
    r=randroll()
    print(f" 🫡 {self.name} used "+colored(" Soul Robbery","magenta")+"!")
    c=critch(self,other)
    self.atktype="Psychic"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=100
    dmg=special(self.level,self.spatk,other.spdef,base,a,b,c,r,al)   
    other.hp-=dmg         
    self.atkb,self.defb,self.spatkb,self.spdefb,self.speedb=other.atkb,other.defb,other.spatkb,other.spdefb,other.speedb
    other.atkb,other.defb,other.spatkb,other.spdefb,other.speedb=1,1,1,1,1    
    
def lastrespects(self,other,tr):
    al=1
    r=randroll()
    print(f" 🫡 {self.name} used "+colored(" Last Respects","magenta")+"!")
    c=critch(self,other)
    self.atktype="Ghost"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=50+(50*(6-len(tr.pokemons))) 
    dmg=physical(self.level,self.atk,other.defense,base,a,b,c,r,al)   
    other.hp-=dmg 
def woodhammer(self,other):
    al=1
    r=randroll()
    print(f" 🪵 {self.name} used "+colored(" Wood Hammer","green")+"!")
    c=critch(self,other)
    self.atktype="Grass"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,120,a,b,c,r,al)    
    if self.ability=="Reckless":
        dmg*=1.2
    if dmg>other.hp:
        dmg=other.hp
        other.hp=0
    else:
        other.hp-=dmg
    if self.ability!="Rock Head":
        self.hp-=round(dmg/3)
        print(f" {self.name} was hurt by recoil.")        
def skyattack(self,other):
    al=1
    r=randroll()
    print(f" 🕊️ {self.name} used "+colored(" Sky Attack","cyan")+"!")
    c=critch(self,other,2)
    self.atktype="Flying"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,150,a,b,c,r,al)     
    ch=random.randint(1,100)
    if ch>70 and other.ability not in ["Inner Focus"]:
        other.flinched=True             
def crunch(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Crunch","white")+"!")
    c=critch(self,other)
    self.atktype="Dark"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    if self.ability=="Strong Jaw":
        print(f" {self.name}'s {self.ability}!")
        al=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)
    other.hp-=dmg
    ch=random.randint(1,100)
    if ch>80 and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        defchange(other,-0.5)
        print (f" {other.name}: Defense x{other.defb}")
def jawlock(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Jaw Lock","red")+"!")
    c=critch(self,other)
    self.atktype="Dark"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    if self.ability=="Strong Jaw":
        print(f" {self.name}'s {self.ability}!")
        al=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)
    other.hp-=dmg
def playrough(self,other):
    al=1
    r=randroll()
    print(f" 💓 {self.name} used "+colored(" Play Rough","magenta")+"!")
    c=critch(self,other)
    self.atktype="Fairy"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)                      
    ch=random.randint(1,10)
    if ch==7 and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        atkchange(other,-0.5)
        print(f" {other.name}: Attack x{other.atkb}")
def powerwhip(self,other):
    al=1
    r=randroll()
    print(f" 🌿 {self.name} used "+colored(" Power Whip","green")+"!")
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
    print(f" {self.name} used "+colored(" Aqua Tail","blue")+"!")
    c=critch(self,other)
    self.atktype="Water"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al,w)        
def astralbarrage(self,other):
    al=1
    r=randroll()
    print(f" 👻 {self.name} used "+colored(" Astral Barrage","magenta")+"!")
    c=critch(self,other)
    self.atktype="Ghost"
    w=weathereff(self)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,130,a,b,c,r,al,w)        
def glaciallance(self,other):
    al=1
    r=randroll()
    print(f" 🏔️ {self.name} used "+colored(" Glacial Lance","cyan")+"!")
    c=critch(self,other)
    self.atktype="Ice"
    w=weathereff(self)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,130,a,b,c,r,al,w)       
    
def breakingswipe(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Breaking Swipe","red")+"!")
    c=critch(self,other)
    self.atktype="Dragon"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=60
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    other.hp-=physical (self.level,self.atk,other.defense,base,a,b,c,r,al)            
    atkchange(other,-0.5)
    print(f" {other.name} Attack x{other.atkb}")  
def falsesurrender(self,other):
    al=1
    r=randroll()
    print(f" 👹 {self.name} "+colored(" False Surrender","white")+"!")
    c=critch(self,other)
    self.atktype="Dark"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)            
def spiritbreak(self,other):
    al=1
    r=randroll()
    print(f" {self.name} "+colored(" Spirit Break","magenta")+"!")
    c=critch(self,other)
    self.atktype="Fairy"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,75,a,b,c,r,al)            
    spatkchange(other,-0.5)
    print(f" {other.name} Special Attack x{other.spatkb}")       
def orderup(self,other):
    al=1
    r=randroll()
    print(f" 🍥 {self.name} used "+colored(" Order Up","red")+"!")
    c=critch(self,other)
    self.atktype="Dragon"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)     
def dragonclaw(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Dragon Claw","red")+"!")
    c=critch(self,other)
    self.atktype="Dragon"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al) 
def dragontail(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Dragon Tail","red")+"!")
    c=critch(self,other)
    self.atktype="Dragon"
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}!")
        al=1.5
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,60,a,b,c,r,al)     
def gigatonhammer(self,other):
    al=1
    r=randroll()
    print(f" 🔨 {self.name} used "+colored(" Gigaton Hammer","white")+"!")
    c=critch(self,other)
    self.atktype="Steel"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,160,a,b,c,r,al)       
def flyingpress(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Flying Press","red")+"!")
    c=critch(self,other)
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    self.atktype="Flying"
    bc=weakness(self,other,field)
    a=ab[0]*bc[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)       
def mountaingale(self,other):
    al=1
    r=randroll()
    print(f" 🏔️ {self.name} used "+colored(" Mountain Gale","cyan")+"!")
    c=critch(self,other)
    self.atktype="Ice"
    w=weathereff(self)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,120,a,b,c,r,al,w)       
    ch=random.randint(1,100)
    if ch>70 and other.ability not in ["Inner Focus"]:
        other.flinched=True   
def firstimpression(self,other):
    al=1
    r=randroll()
    print(f" 🦗 {self.name} used "+colored(" First Impression","green")+"!")
    c=critch(self,other)
    self.atktype="Normal"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=90
    other.hp-=physical (self.level,self.atk,other.defense,base,a,b,c,r,al)               
def fakeout(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Fake Out","white")+"!")
    c=critch(self,other)
    self.atktype="Normal"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=40
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    other.hp-=physical (self.level,self.atk,other.defense,base,a,b,c,r,al)         
    if other.ability not in ["Inner Focus"]:
        other.flinched=True 
def eggbomb(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Egg Bomb","white")+"!")
    c=critch(self,other)
    self.atktype="Normal"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)  
def knockoff(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Knock Off","white")+"!")
    c=critch(self,other)
    self.atktype="Dark"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=65
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    if "Mega " not in other.name and "Z-Crystal" not in other.name and other.item is not None:
        print(f" {self.name} knocked off {other.name}'s {other.item}!")
        base*=2
        other.item=None
    other.hp-=physical (self.level,self.atk,other.defense,base,a,b,c,r,al)      
def crushclaw(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Crush Claw","red")+"!")
    c=critch(self,other)
    self.atktype="Normal"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)      
    ch=random.randint(1,2)
    if ch==2 and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        defchange(other,-0.5)
        print(f" {other.name} Defense x{other.defb}")
def seedbomb(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Seed Bomb","green")+"!")
    c=critch(self,other)
    self.atktype="Grass"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)  
def spinout(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Spin Out","white")+"!")
    c=critch(self,other)
    self.atktype="Steel"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,100,a,b,c,r,al)         
    speedchange(self,-1)
    print(" Its speed fell harshly!") 
def irontail(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Iron Tail","white")+"!")
    c=critch(self,other)
    self.atktype="Steel"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,100,a,b,c,r,al)             
    ch=random.randint(1,100)
    if ch>70 and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        defchange(other,-0.5)
        print(f" {other.name} Defense x{other.defb}")
def moongeistbeam(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Moongeist Beam","magenta")+"!")
    c=critch(self,other)
    self.atktype="Ghost"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special (self.level,self.spatk,other.spdef,100,a,b,c,r,al)              
def sunsteelstrike(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Sunsteel Strike","white")+"!")
    c=critch(self,other)
    self.atktype="Steel"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,100,a,b,c,r,al)     
def behemothbash(self,other):
    al=1
    r=randroll()
    print(f" 🛡️💥 {self.name} used "+colored(" Behemoth Bash","white")+"!")
    c=critch(self,other)
    self.atktype="Steel"
    if other.dmax is True:
        al*=2
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.defense,other.defense,100,a,b,c,r,al)          
def behemothblade(self,other):
    al=1
    r=randroll()
    print(f" 🗡️💥 {self.name} used "+colored(" Behemoth Blade","white")+"!")
    c=critch(self,other)
    self.atktype="Steel"
    if other.dmax is True:
        al*=2
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,100,a,b,c,r,al)                   
def ironhead(self,other):
    al=1
    r=randroll()
    print(f" 🤖 {self.name} used "+colored(" Iron Head","white")+"!")
    c=critch(self,other)
    self.atktype="Steel"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
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
    print(f" 🌌 {self.name} used "+colored(" Meteor Mash","white")+"!")
    c=critch(self,other)
    self.atktype="Steel"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,90,a,b,c,r,al)    
    other.hp-=dmg  
    ch=random.randint(1,100)
    if ch<80:
        atkchange(self,0.5)
        print(f" Attack x{self.atkb}")     
def grassyglide(self,other):
    al=1
    r=randroll()
    print(f" ☘️ {self.name} used "+colored(" Grassy Glide","green")+"!")
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
    print(f" 🍏 {self.name} used "+colored(" Apple Acid","green")+"!")
    c=critch(self,other)
    self.atktype="Grass"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=special (self.level,self.spatk,other.spdef,80,a,b,c,r,al)     
    if other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        other.hp-=dmg  
        spdefchange(other,-0.5)
        print(f" {other.name}: Special Defense x{other.spdefb}")       
def destinybond(self,other):
    print(f" 🪦 {self.name} used "+colored(" Destiny Bond","magenta")+"!")    
    other.dbond=True        
def gravapple(self,other):
    al=1
    r=randroll()
    print(f" 🍎 {self.name} used "+colored(" Grav Apple","green")+"!")
    c=critch(self,other)
    self.atktype="Grass"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)     
    other.hp-=dmg  
    defchange(other,-0.5)
    print(f" {other.name}: Defense x{other.defb}")           
def drumbeating(self,other):
    al=1
    r=randroll()
    print(f" 🥁 {self.name} used "+colored(" Drum Beating","green")+"!")
    c=critch(self,other)
    self.atktype="Grass"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)     
    if other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        other.hp-=dmg  
        speedchange(other,-0.5)
        print(f" {other.name}: Speed x{other.speedb}")             
def icehammer(self,other):
    al=1
    r=randroll()
    print(f" 🧊🔨 {self.name} used "+colored(" Ice Hammer","cyan")+"!")
    c=critch(self,other)
    self.atktype="Ice"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,100,a,b,c,r,al)     
    other.hp-=dmg  
    speedchange(self,-0.5)
    print(f" Speed x{self.speedb}")          
def hammerarm(self,other):
    al=1
    r=randroll()
    print(f" 🔨 {self.name} used "+colored(" Hammer Arm","red")+"!")
    c=critch(self,other)
    self.atktype="Fighting"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,100,a,b,c,r,al)     
    other.hp-=dmg  
    speedchange(self,-0.5)
    print(f" Speed x{self.speedb}")        
def poweruppunch(self,other):
    al=1
    r=randroll()
    print(f" 👊🏽 {self.name} used "+colored(" Power-Up Punch","red")+"!")
    c=critch(self,other)
    self.atktype="Fighting"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    if self.ability=="Iron Fist":
        print(f" {self.name}'s {self.ability}!")
        al=1.3
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=40
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    dmg=physical (self.level,self.atk,other.defense,base,a,b,c,r,al)     
    other.hp-=dmg  
    if a>0:
        atkchange(self,0.5)
        print(f" Attack x{self.atkb}")
def doubleedge(self,other):
    al=1
    r=randroll()
    print(f" 💥 {self.name} used "+colored(" Double-Edge","white")+"!")
    c=critch(self,other)
    self.atktype="Normal"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical (self.level,self.atk,other.defense,100,a,b,c,r,al) 
    if self.ability=="Reckless":
        dmg*=1.2
    if dmg>other.hp:
        dmg=other.hp
        other.hp=0
    else:
        other.hp-=dmg
    if self.ability!="Rock Head":
        self.hp-=round(dmg/3)
        print(f" {self.name} was hurt by recoil.")
def quickattack(self,other):
    al=1
    r=randroll()
    print(f" ⏪ {self.name} used "+colored(" Quick Attack","white")+"!")
    c=critch(self,other)
    self.atktype="Normal"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,40,a,b,c,r,al)          
def extemespeed(self,other):
    al=1
    r=randroll()
    print(f" ⏪ {self.name} used "+colored(" Extreme Speed","white")+"!")
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
    print(f" 🦀 {self.name} used "+colored(" Crabhammer","blue")+"!")
    c=critch(self,other,2)
    
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,100,a,b,c,r,al,w)  
def glaiverush(self,other):
    al=1
    r=randroll()
    print(f" 🔪 {self.name} used "+colored(" Glaive Rush","red")+"!")
    c=critch(self,other,2)
    self.atktype="Dragon"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,120,a,b,c,r,al)    
def slash(self,other):
    al=1
    r=randroll()
    print(f" 🗡️ {self.name} used "+colored(" Slash","white")+"!")
    if self.ability=="Sharpness":
        al*=1.5
    c=critch(self,other,2)
    self.atktype="Normal"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,70,a,b,c,r,al)
def aquacutter(self,other):
    al=1
    r=randroll()
    print(f" 💧🔪 {self.name} used "+colored(" Aqua Cutter","blue")+"!")
    if self.ability=="Sharpness":
        al*=1.5
    c=critch(self,other,2)
    self.atktype="Water"
    w=weathereff(self)
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,70,a,b,c,r,al,w) 
def direclaw(self,other):
    al=1
    r=randroll()
    print(f" 🐾 {self.name} used "+colored(" Dire Claw","magenta")+"!")
    c=critch(self,other,2)
    self.atktype="Poison"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=80
    other.hp-=physical (self.level,self.atk,other.defense,base,a,b,c,r,al)      
    ch=random.randint(1,100)
    if ch>90 and other.status=="Alive":
        other.status="Sleep"
    ch=random.randint(1,100)
    if ch>90 and other.status=="Alive":
        other.status="Badly Poisoned"
        print(f" ☠️ {other.name} was badly poisoned.") 
    ch=random.randint(1,100)
    if ch>90 and other.status=="Alive":
        other.status="Paralyzed"
def crosschop(self,other):
    al=1
    r=randroll()
    print(f" 🥋 {self.name} used "+colored(" Cross Chop","red")+"!")
    c=critch(self,other,2)
    self.atktype="Fighting"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,100,a,b,c,r,al)          
def nightslash(self,other):
    al=1
    r=randroll()
    print(f" 🔪 {self.name} used "+colored(" Night Slash","red")+"!")
    c=critch(self,other,2)
    self.atktype="Dark"
    if self.ability=="Sharpness":
        al*=1.5
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,70,a,b,c,r,al)  
def ruination(self,other):
    al=1
    r=randroll()
    print(f" 🌆 {self.name} used "+colored(" Ruination","red")+"!")
    c=critch(self,other,2)
    self.atktype="Dark"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=(other.hp/2)
def kowtowcleave(self,other):
    al=1
    r=randroll()
    print(f" ⚔️ {self.name} used "+colored(" Kowtow Cleave","red")+"!")
    c=critch(self,other,2)
    self.atktype="Dark"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,85,a,b,c,r,al)      
def shadowpunch(self,other):
    al=1
    r=randroll()
    print(f" 👊🏽 {self.name} used "+colored(" Shadow Punch","magenta")+"!")
    c=critch(self,other,2)
    self.atktype="Ghost"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)          
def shadowclaw(self,other):
    al=1
    r=randroll()
    print(f" 🐾 {self.name} used "+colored(" Shadow Claw","magenta")+"!")
    c=critch(self,other,2)
    self.atktype="Ghost"
    if self.ability=="Tough Claws":
        print(f" {self.name}'s {self.ability}!")
        al=1.33
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)      
def ragefist(self,other):
    al=1
    r=randroll()
    print(f" 💢 {self.name} used "+colored(" Rage Fist","magenta")+"!")
    c=critch(self,other)
    self.atktype="Ghost"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=50+(50*self.atktime)
    other.hp-=physical (self.level,self.atk,other.defense,base,a,b,c,r,al)       
def hyperspacefury(self,other):
    al=1
    r=randroll()
    print(f" 🌌 {self.name} used "+colored(" Hyperspace Fury","magenta")+"!")
    c=critch(self,other)
    self.atktype="Dark"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,100,a,b,c,r,al)            
def psychocut(self,other):
    al=1
    r=randroll()
    print(f" 🌀🗡️ {self.name} used "+colored(" Psycho Cut","magenta")+"!")
    if self.ability=="Sharpness":
        al*=1.5
    c=critch(self,other,2)
    self.atktype="Psychic"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,70,a,b,c,r,al)   
def esperwing(self,other):
    al=1
    r=randroll()
    print(f" 🦅 {self.name} used "+colored(" Esper Wing","magenta")+"!")
    c=critch(self,other,2)
    self.atktype="Psychic"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,80,a,b,c,r,al)       
    speedchange (self,0.5)
    print(f" Speed x{self.speedb}")
def wickedblow(self,other):
    al=1
    r=randroll()
    print(f" 😈 {self.name} used "+colored(" Wicked Blow","red")+"!")
    c=critch(self,other,16)
    self.atktype="Dark"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,80,a,b,c,r,al)   
def ceaseless(self,other):
    al=1
    r=randroll()
    print(f" 🗡️ {self.name} used "+colored(" Ceaseless Edge","red")+"!")
    c=critch(self,other,16)
    self.atktype="Dark"
    if self.ability=="Sharpness":
        al*=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,70,a,b,c,r,al)       
def surgingstrikes(self,other):
    al=1
    r=randroll()
    print(f" 🌊 {self.name} used "+colored(" Surging Strikes","blue")+"!")
    c=critch(self,other,16)
    self.atktype="Water"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,25,a,b,c,r,al)                    
def dragonascent(self,other):
    al=1
    r=randroll()
    print(f" 🐉 {self.name} used "+colored(" Dragon Ascent","green")+"!")
    c=critch(self,other)
    self.atktype="Flying"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,120,a,b,c,r,al)     
    defchange(self,-0.5)
    spdefchange(self,-0.5)
    print(f" Defense x{self.defb}")
    print(f" Special Defense x{self.spdefb}")
def weatherball(self,other):
    self.atktype="Normal"
    base=50
    typ=None
    color="white"
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    if field.weather in ["Primordial Sea","Rainy"]:
        self.atktype="Water"
        typ="💧"
        color="blue"
        base*=2
    if field.weather in ["Desolate Land","Sunny"]:
        self.atktype="Fire" 
        typ="🔥"
        color="red"
        base*=2     
    if field.weather in ["Hail"]:
        self.atktype="Ice"  
        typ="❄️"
        color="cyan"
        base*=2    
    if field.weather in ["Sandstorm"]:
        self.atktype="Rock"  
        typ="🪨"
        color="yellow"
        base*=2
    al=1
    w=weathereff(self)
    r=randroll()
    print(f" {typ} {self.name} used "+colored(" Weather Ball",f"{color}")+"!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,base,a,b,c,r,al,w)
def maxgeyser(self,other,tr1,turn):
    w=weathereff(self)
    print(f" 🔺🌊 {self.name} used "+colored(" Max Geyser","blue")+"!")
    self.atktype="Water"
    al=1
    r=randroll()
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al,w)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al,w)      
    if field.weather not in ["Desolate Land","Primordial Sea","Strong Wind","Rainy"]:
        print(f" 🌧️ {self.name} made it rain.")
        field.weather="Rainy"
        tr1.rainturn=turn
        tr1.rainend(self,other)       
def raindance(self,other,tr1,turn):
    print(f" ☔ {self.name} used "+colored(" Rain Dance","blue")+"!")
    if field.weather not in ["Desolate Land","Primordial Sea","Strong Wind","Rainy"]:
        print(f" 🌧️ {self.name} made it rain.")
        field.weather="Rainy"
        tr1.rainturn=turn
        tr1.rainend(self,other)
    else:
        print(" It failed.")   
def maxflare(self,other,tr1,turn):
    self.atktype="Fire"
    al=1
    r=randroll()
    w=weathereff(self)
    print(f" 🔺🔥 {self.name} used "+colored(" Max Flare","red")+"!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al,w)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al,w)
    if field.weather not in ["Desolate Land","Primordial Sea","Strong Wind","Sunny"]:
        print(f" ☀️ {self.name} made the sunlight harsh.")
        field.weather="Sunny"
        tr1.sunturn=turn
        tr1.sunend(self,other)     
                
def sunnyday(self,other,tr1,turn):
    print(f" ☀️ {self.name} used "+colored(" Sunny Day","yellow")+"!")
    if field.weather not in ["Desolate Land","Primordial Sea","Strong Wind","Sunny"]:
        print(f" ☀️ {self.name} made the sunlight harsh.")
        field.weather="Sunny"
        tr1.sunturn=turn
        tr1.sunend(self,other)
    else:
        print(" It failed.")        
def maxrockfall(self,other,tr1,turn):
    print(f" 🔺 {self.name} used "+colored(" Max Rockfall","yellow")+"!")
    al=1
    r=randroll()
    self.atktype="Rock"
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al)          
    if field.weather not in ["Desolate Land","Primordial Sea","Strong Wind","Sandstorm"]:
        print(f" 🏜️ {self.name} started a sandstorm.")
        field.weather="Sandstorm" 
        tr1.sandturn=turn
        tr1.sandend(self,other)     
def chillyreception (self,other,tr1,turn):
    print(f" ❄️ {self.name} used "+colored(" Chilly Reception","cyan")+"!")
    if field.weather not in ["Desolate Land","Primordial Sea","Strong Wind","Snowstorm"]:
        print(f" {self.name} started a snowstorm.")
        field.weather="Snowstorm" 
        tr1.snowstormturn=turn
        tr1.snowstormend(self,other)
    else:
        print(" It failed.")        
              
def snowscape(self,other,tr1,turn):
    print(f" ❄️ {self.name} used "+colored(" Snowscape","cyan")+"!")
    if field.weather not in ["Desolate Land","Primordial Sea","Strong Wind","Snowstorm"]:
        print(f" {self.name} started a snowstorm.")
        field.weather="Snowstorm" 
        tr1.snowstormturn=turn
        tr1.snowstormend(self,other)
    else:
        print(" It failed.")        
def sandstorm(self,other,tr1,turn):
    print(f" 🏜️ {self.name} used "+colored(" Sandstorm","yellow")+"!")
    if field.weather not in ["Desolate Land","Primordial Sea","Strong Wind","Sandstorm"]:
        print(f" {self.name} started a sandstorm.")
        field.weather="Sandstorm" 
        tr1.sandturn=turn
        tr1.sandend(self,other)
    else:
        print(" It failed.")
def hail(self,other,tr1,turn):
    print(f" 🧊 {self.name} used "+colored(" Hail","cyan")+"!")
    if field.weather not in ["Desolate Land","Primordial Sea","Strong Wind","Hail"]:
        print(f" 🌨️ {self.name} started a hailstorm.")
        field.weather="Hail"     
        tr1.hailturn=turn
        tr1.hailend(self,other) 
    else:
        print(" It failed.")      
def maxhailstorm(self,other,tr1,turn):
    print(f" 🔺🧊 {self.name} used "+colored(" Max Hailstorm","cyan")+"!")
    al=1
    r=randroll()
    self.atktype="Ice"
    w=weathereff(self)
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,150,a,b,c,r,al,w)    
    else:
        other.hp-=physical(self.level,self.atk,other.defense,150,a,b,c,r,al)   
    if field.weather not in ["Desolate Land","Primordial Sea","Strong Wind","Hail"]:
        print(f" 🌨️ {self.name} started a hailstorm.")
        field.weather="Hail"     
        tr1.hailturn=turn
        tr1.hailend(self,other)         
def dualchop(self,other):
    al=1
    r=randroll()
    print(f" 🦎 {self.name} used "+colored(" Dual Chop","red")+"!")
    c=critch(self,other)
    self.atktype="Dragon"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=40
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    other.hp-=physical (self.level,self.atk,other.defense,base,a,b,c,r,al)       
def scaleshot(self,other):
    al=1
    r=randroll()
    print(f" 🦎 {self.name} used "+colored(" Scale Shot","red")+"!")
    c=critch(self,other)
    self.atktype="Dragon"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=25
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    other.hp-=physical (self.level,self.atk,other.defense,base,a,b,c,r,al)                   
def dragondarts(self,other):
    al=1
    r=randroll()
    print(f" 🦎 {self.name} used "+colored(" Dragon Darts","red")+"!")
    c=critch(self,other)
    self.atktype="Dragon"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=50
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    other.hp-=physical (self.level,self.atk,other.defense,base,a,b,c,r,al)          
def dualwingbeat(self,other):
    al=1
    r=randroll()
    print(f" 🕊️ {self.name} used "+colored(" Dual Wingbeat","cyan")+"!")
    c=critch(self,other)
    self.atktype="Flying"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=40
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    other.hp-=physical (self.level,self.atk,other.defense,base,a,b,c,r,al)         
def precipiceblades(self,other):
    al=1
    r=randroll()
    print(f" 🦖🌋 {self.name} used "+colored(" Precipice Blades","red")+"!")
    c=critch(self,other)
    self.atktype="Ground"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical (self.level,self.atk,other.defense,120,a,b,c,r,al)         
def oblivionwing(self,other):
    al=1
    r=randroll()
    print(f" 🦅 {self.name} used "+colored(" Oblivion Wing","red")+"!")
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
    if self.hp<=(self.maxhp-heal):
        self.hp+=heal
    else:
        self.hp=self.maxhp 
def gigadrain(self,other):
    al=1
    r=randroll()
    print(f" 🌱 {self.name} used "+colored(" Giga Drain","green")+"!")
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
    if self.hp<=(self.maxhp-heal):
        self.hp+=heal
    else:
        self.hp=self.maxhp           
def dreameater(self,other):
    al=1
    r=randroll()
    print(f" 💭 {self.name} used "+colored(" Dream Eater","magenta")+"!")
    c=critch(self,other)
    self.atktype="Psychic"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if other.status=="Sleep":
        dmg=special(self.level,self.spatk,other.spdef,100,a,b,c,r,al)    
        if dmg>other.hp:
            dmg=other.hp
            other.hp-=dmg
        else:
            other.hp-=dmg
        heal=dmg/2
        if self.hp<=(self.maxhp-heal):
            self.hp+=heal
        else:
            self.hp=self.maxhp
def relicsong(self,other):
    al=1
    r=randroll()
    print(f" 🎶 {self.name} used "+colored(" Relic Song","green")+"!")
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
            print(f" {other.name} fell asleep.")
            other.status="Sleep"

def leechlife(self,other):
    al=1
    r=randroll()
    print(f" 🦟 {self.name} used "+colored(" Leech Life","green")+"!")
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
def revelationdance(self,other):
    w=weathereff(self)
    al=1
    r=randroll()
    print(f" 🐦 {self.name} used "+colored(" Revelation Dance","white")+"!")
    c=critch(self,other)
    self.atktype=self.type1
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,100,a,b,c,r,al,w)          
def surf(self,other):
    w=weathereff(self)
    al=1
    r=randroll()
    print(f" 🌊 {self.name} used "+colored(" Surf","blue")+"!")
    c=critch(self,other)
    self.atktype="Water"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al,w)  
def muddywater(self,other):
    w=weathereff(self)
    al=1
    r=randroll()
    print(f" 🌊 {self.name} used "+colored(" Muddy Water","blue")+"!")
    c=critch(self,other)
    self.atktype="Water"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,80,a,b,c,r,al,w)      
def dracometeor(self,other):
    al=1
    r=randroll()
    print(f" 🐉☄️ {self.name} used "+colored(" Draco Meteor","red")+"!")
    c=critch(self,other)
    self.atktype="Dragon"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,130,a,b,c,r,al)  
    spatkchange(self,-1)
    print(f" Special Attack x{self.spatkb}")
def originpulse(self,other):
    al=1
    self.atktype="Water"
    w=weathereff(self)
    r=randroll()
    print(f" 🐋🌊 {self.name} used "+colored(" Origin Pulse","blue")+"!")
    if self.ability=="Mega Launcher":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,120,a,b,c,r,al,w)          
def apower(self,other):
    al=1
    r=randroll()
    print(f" 🪨 {self.name} used "+colored(" Ancient Power","yellow")+"!")
    c=critch(self,other)
    self.atktype="Rock"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al) 
    chance=10
    if self.ability=="Serene Grace":
        chance*=2
    if self.speed>other.speed:
        ch=random.randint(1,100)            
        if ch>(100-chance):
            atkchange(self,0.5)
            defchange(self,0.5)
            spatkchange(self,0.5)
            spdefchange(self,0.5)
            speedchange(self,0.5)
            print(f" Attack x{self.atkb}")
            print(f" Defense x{self.defb}")
            print(f" Special Attack x{self.spatkb}")
            print(f" Special Defense x{self.spdefb}")
            print(f" Speed x{self.speedb}")
def noretreat(self):
    print(f" ⚔️ {self.name} used "+colored(" No Retreat","red")+"!")
    atkchange(self,0.5)
    defchange(self,0.5)
    spatkchange(self,0.5)
    spdefchange(self,0.5)
    speedchange(self,0.5)
    print(f" Attack x{self.atkb}")
    print(f" Defense x{self.defb}")
    print(f" Special Attack x{self.spatkb}")
    print(f" Special Defense x{self.spdefb}")
    print(f" Speed x{self.speedb}")     
def octolock(self,other):
    print(f" 🐙 {self.name} used "+colored(" Octolock","red")+"!")     
    if other.olock is False:
        other.olock=True
def octazooka(self,other):
    self.atktype="Water"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f" 🐙 {self.name} used "+colored(" Octazooka","blue")+"!")
    if self.ability=="Mega Launcher":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,65,a,b,c,r,al,w)       
    ch=random.randint(1,100)
    if ch>50:
        other.accuracy-=10
def scald(self,other):
    self.atktype="Water"
    w=weathereff(self)
    al=1
    r=randroll()
    print(f" 💦🔥 {self.name} used "+colored(" Scald","blue")+"!")
    c=critch(self,other)
    
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,80,a,b,c,r,al,w)            
    ch=random.randint(1,100)
    if ch>70 and other.status=="Alive":
        other.status="Burned"
        print(f" 🔥 {other.name} was burned.")
      
def scorchingsands(self,other):
    self.atktype="Ground"
    al=1
    r=randroll()
    print(f" 🏜️ {self.name} used "+colored(" Scorching Sands","yellow")+"!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al)            
    ch=random.randint(1,100)
    if ch>70 and other.status=="Alive":
        other.status="Burned"
        print(f" 🔥 {other.name} was burned.")
      
def doomdesire(self,other):
    al=1
    r=randroll()
    print(f" 🌟 {self.name} used "+colored(" Doom Desire","yellow")+"!")
    c=critch(self,other)
    self.atktype="Steel"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,140,a,b,c,r,al)        
def fleurcannon(self,other):
    al=1
    r=randroll()
    print(f" 🤖 {self.name} used "+colored(" Fleur Cannon","magenta")+"!")
    c=critch(self,other)
    self.atktype="Fairy"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,130,a,b,c,r,al)        
    spdefchange(self,-1)
    print(f" Special Defense x{self.spdefb}")    
def flashcannon(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Flash Cannon","white")+"!")
    c=critch(self,other)
    if self.ability=="Mega Launcher":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    self.atktype="Steel"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al) 
    chance=30
    if self.ability=="Serene Grace":
        chance*=2
    if self.speed>other.speed:
        ch=random.randint(1,100)            
        if ch>(100-chance):
            spdefchange(other,-0.5)
            print(f" {other.name}: Special Defense x{other.spdefb}")
def psychoboost(self,other):
    al=1
    r=randroll()
    print(f" 🔮 {self.name} used "+colored(" Psycho Boost","magenta")+"!")
    c=critch(self,other)
    self.atktype="Psychic"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,140,a,b,c,r,al)       
    spatkchange(self,-1)
    print(f" Special Attack x{self.spatkb}")
def victorydance(self):
    print(f" ✌🏻 {self.name} used Victory Dance.")
    atkchange (self,0.5)
    defchange(self,0.5)
    speedchange(self,0.5)
    print(f" Attack x{self.atkb}")
    print(f" Defense x{self.defb}")
    print(f" Speed x{self.speedb}")    
def takeheart(self):
    print(f" 💝 {self.name} used Take Heart.")
    atkchange (self,0.5)
    defchange(self,0.5)
    spatkchange(self,0.5)
    spdefchange(self,0.5)
    print(f" Attack x{self.atkb}")
    print(f" Defense x{self.spdefb}")
    print(f" Special Attack x{self.spatkb}")
    print(f" Special Defense x{self.spdefb}")
def heartswap(self,other):
    print(f" 💞 {self.name} used Heart Swap.")
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
    print(f" {self.name} swapped it's stat changes with {other.name}.")
def transform(self,other):
    print(f' 👥 {self.name} transformed into {other.name}')
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
        print(f" {self.name} used "+colored(" Seismic Toss","red")+"!")
        other.hp-=self.level
    else:
        print(f" Doesn't effect on {other.name}")
def nightshade(self,other):
    if other.type1!="Normal" and other.type2!="Normal":
        print(f" 👤 {self.name} used "+colored(" Night Shade","magenta")+"!")
        other.hp-=self.level
    else:
        print(f" Doesn't effect on {other.name}")        
def flamethrower (self,other):
    self.atktype="Fire"
    w=weathereff(self)
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    print(f" 🔥 {self.name} used "+colored(" Flamethrower","red")+"!")
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,90,a,b,c,r,al,w)        
    ch=random.randint(1,100)
    if ch>90 and other.status=="Alive" and other.ability not in ["Shield Dust"]:
        other.status="Burned"
        print(f" 🔥 {other.name} was burned.")
      
def solarbeam(self,other):
    al=1
    w=1
    r=randroll()
    if field.weather=="Sandstorm":
        w*=0.5
    if (field.weather in ["Sunny","Desolate Land"]) or self.precharge is True:
        print(f" ☀️ {self.name} used "+colored(" Solar Beam","green")+"!")
        c=critch(self,other)
        self.atktype="Grass"
        ab=weakness(self,other,field)
        a=ab[0]
        b=ab[1]   
        other.hp-=special(self.level,self.spatk,other.spdef,120,a,b,c,r,al,w)         
        self.precharge=False
    elif self.precharge is False:
        print(f" 🌤️ {self.name} is absorbing sunlight!")
        self.precharge=True
    
def terablast(self,other):
    if True:
        typ=None
        color="white"
        if self.teratype=="Dragon":
            typ="🐲"
            color="red"
        if self.teratype=="Psychic":
            typ="👁️"
            color="magenta"
        if self.teratype=="Ghost":
            typ="👻"
            color="magenta"
        if self.teratype=="Normal":
            typ="💎"
            color="white"
        if self.teratype=="Bug":
            typ="🪲"
            color="green"
        if self.teratype=="Steel":
            typ="🪓"
            color="white"
        if self.teratype=="Ice":
            typ="❄️"
            color="cyan"
        if self.teratype=="Fighting":
            typ="👊🏽"
            color="red"
        if self.teratype=="Dark":
            typ="🌑"
            color="red"
        if self.teratype=="Fairy":
            typ="🧚🏻‍♂️"
            color="magenta"
        if self.teratype=="Flying":
            typ="🎈"
            color="cyan"
        if self.teratype=="Poison":
            typ="☠️"
            color="magenta"
        if self.teratype=="Ground":
            typ="🌍"
            color="yellow"
        if self.teratype=="Rock":
            typ="🪨"
            color="yellow"
        if self.teratype=="Grass":
            typ="🌻"
            color="green"
        if self.teratype=="Electric":
            typ="💡"
            color="yellow"
        if self.teratype=="Water":
            typ="⛲"
            color="blue"
        if self.teratype=="Fire":
            typ="🕯️"
            color="red"
        print(f" {typ} {self.name} used "+colored(" Tera Blast",f"{color}")+"!")
    self.atktype=self.teratype
    w=weathereff(self)
    al=1
    r=randroll()
    c=critch(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    if self.atk>self.spatk:
        other.hp-=physical(self.level,self.atk,other.defense,80,a,b,c,r,al,w)
    if self.spatk>self.atk:
        other.hp-=special(self.level,self.spatk,other.spdef,80,a,b,c,r,al,w)                 
def hiddenpower(self,other):
    al=1
    r=randroll()
    x=hidp(self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv)
    base=x[0]
    if self.maxiv!="Yes":
        self.atktype=x[1]
    if self.maxiv in ["Rock","Fire","Water","Grass","Electric","Ground","Flying","Fighting","Fairy","Dragon","Steel","Poison","Dark","Ghost","Normal","Bug","Ice"]:
        self.atktype=self.maxiv
    w=weathereff(self)
    typ=None
    color="white"
    if self.atktype=="Dragon":
        typ="🐲"
        color="red"
    if self.atktype=="Psychic":
        typ="👁️"
        color="magenta"
    if self.atktype=="Ghost":
        typ="👻"
        color="magenta"
    if self.atktype=="Normal":
        typ="💎"
        color="white"
    if self.atktype=="Bug":
        typ="🪲"
        color="green"
    if self.atktype=="Steel":
        typ="⚙️"
        color="white"
    if self.atktype=="Ice":
        typ="❄️"
        color="cyan"
    if self.atktype=="Fighting":
        typ="👊🏽"
        color="red"
    if self.atktype=="Dark":
        typ="🌑"
        color="red"
    if self.atktype=="Fairy":
        typ="❤️"
        color="magenta"
    if self.atktype=="Flying":
        typ="🐦"
        color="cyan"
    if self.atktype=="Poison":
        typ="☠️"
        color="magenta"
    if self.atktype=="Ground":
        typ="🌍"
        color="yellow"
    if self.atktype=="Rock":
        typ="🪨"
        color="yellow"
    if self.atktype=="Grass":
        typ="🌿"
        color="green"
    if self.atktype=="Electric":
        typ="⚡"
        color="yellow"
    if self.atktype=="Water":
        typ="💧"
        color="blue"
    if self.atktype=="Fire":
        typ="🔥"
        color="red"
    print(f" {typ} {self.name} used "+colored(f" Hidden Power({self.atktype})",f"{color}")+"!")
    c=critch(self,other)
    
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self.level,self.spatk,other.spdef,base,a,b,c,r,al,w)
    
    
def special(level,spatk,spdef,base,a=1,b=1,c=1,r=1,al=1,w=1):
    dmg=round((((2*level + 10)/250)*(spatk/spdef)*base+2)*a*b*c*r*al*w)
    return dmg
def physical(level,atk,defense,base,a=1,b=1,c=1,r=1,al=1,w=1):
    dmg=round((((2*level + 10)/250)*(atk/ defense)*base+2)*a*b*c*r*al*w)
    return dmg
def weather(mon,pk):
    if field.weather =="Desolate Land":
        print("\n 🌋 The sunlight is extremely harsh.\n")
    if field.weather =="Primordial Sea":
        print("\n 🌊 Heavy rain continues to fall.\n")
    if field.weather =="Snowstorm":
        print("\n 🌨️ Snow continues to fall.\n")
    if field.weather =="Rainy":
        print("\n 🌧️ Rain continues to fall.\n")
    if field.weather =="Sandstorm":
        print("\n 🏜️ The sandstorm is raging!\n")
    if field.weather=="Hail":
        print("\n 🌨️ Hail continues to fall.\n")   
    if field.weather=="Sunny":
        print("\n ☀️ The sunlight is strong.\n")        

def weathereff(mon):
    if field.weather=="Desolate Land" and mon.atktype=="Water":
        print(" 🌋 The Water-type attack evaporated in the harsh sunlight!")
        return 0
    if field.weather=="Primordial Sea" and mon.atktype=="Fire":
        print(" 🌊 The Fire-type attack fizzled out in the heavy rain!")
        return 0                                 
    if field.weather in ["Rainy","Primordial Sea"] and mon.atktype=="Water":
        print(" 🌧️ Rain boosted!")
        return 1.5
    if (field.weather=="Sunny") and mon.atktype=="Water":
        print(" ☀️ Sun weakened!")
        return 0.5    
    if (field.weather=="Rainy") and mon.atktype=="Fire":
        print(" 🌧️ Rain weakened!")
        return 0.5      
    if field.weather in ["Sunny" ,"Desolate Land"] and mon.atktype=="Fire":
        print(" ☀️ Sun boosted!")
        if "Koraidon" in mon.name:
            return 2
        else:
            return 1.5        
#    if field.weather in ["Hail","Snowstorm"] and mon.atktype=="Ice":
#        print(f" ❄️ {field.weather} boosted!")
#        return 1.5          
    else:
        return 1 
        