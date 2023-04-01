from colorama import init
from termcolor import colored    
from pokemonbase import *
from pokemonintros import *
from status import *
foe=""
#if tr.ai == True and optr.ai==True:
#    foe=""
def perishsong(self,other):
    print(f" 🎼 {self.name} used "+colored(" Perish Song","white",attrs=["bold"])+"!")
    if 0 in (self.perishturn,other.perishturn):
        print(" All Pokémon that heard the song will faint in three turns!")
    if self.perishturn==0 and self.ability!="Soundproof":
        self.perishturn=4
    if other.perishturn==0 and other.ability!="Soundproof":
        other.perishturn=4
def acupressure(self,other):
    print(f" ⚜️ {self.name} used "+colored(" Acupressure","white",attrs=["bold"])+"!")
    if x==1:
        atkchange(self,self,1)
    if x==2:
        defchange(self,self,1)
    if x==3:
        spatkchange(self,self,1)
    if x==4:
        spdefchange(self,self,1)
    if x==5:
        speedchange(self,self,1)
    x=random.randint(1,5)
def psychoshift(self,other):
    print(f" 🔂 {self.name} used "+colored(" Psycho Shift","magenta",attrs=["bold"])+"!")
    if other.status=="Alive" and self.status!="Alive":
        self.status,other,status=other.status,self.status
        print(f" {self.name} shifted it's status condition to {other.name}!")
def flail(self,other):
    print(f" 💢 {self.name} used "+colored(" Flail","white",attrs=["bold"])+"!")
    mark=(64*self.hp)/self.maxhp
    dmg=0
    if 0<=mark<=1:
        dmg=200
    if 2<=mark<=5:
        dmg=150
    if 6<=mark<=12:
        dmg=100
    if 13<=mark<=21:
        dmg=80
    if 22<=mark<=42:
        dmg=40
    if 43<=mark<=64:
        dmg=20
    self.atktype="Normal"
    al=1
    r=randroll()
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    w=weathereff(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.atk,other.defense,dmg,a,b,c,r,al,w)
def reversal(self,other):
    print(f" 💢 {self.name} used "+colored(" Reversal","red",attrs=["bold"])+"!")
    mark=(64*self.hp)/self.maxhp
    dmg=0
    if 0<=mark<=1:
        dmg=200
    if 2<=mark<=5:
        dmg=150
    if 6<=mark<=12:
        dmg=100
    if 13<=mark<=21:
        dmg=80
    if 22<=mark<=42:
        dmg=40
    if 43<=mark<=64:
        dmg=20
    self.atktype="Fighting"
    al=1
    r=randroll()
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    w=weathereff(self,other)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.atk,other.defense,dmg,a,b,c,r,al,w)    
#ENCORE
def encore(self,other,opuse,turn):
    print(f" 👏 {self.name} used "+colored(" Encore","white",attrs=["bold"])+"!")
    if other.use!=None and other.encore==False and other.dmax is False:
        print(f" 🎉👏 {other.name} fell for the encore!")
        other.encore=opuse
        other.encturn=random.randint(3,5)
    else:
        print(f" It failed!")
#HAZE
def haze(self,other):
    print(f" 🌫️ {self.name} used "+colored(" Haze","white",attrs=["bold"])+"!")
    other.evasion=100
    self.evasion=100
    other.accuracy=100
    self.accuracy=100
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
    
#HEAL BELL    
def healbell(self,tr):
    print(f" 🔔 {self.name} used "+colored(" Heal Bell","yellow",attrs=["bold"])+"!")
    print(" A bell chimed!")
    for i in tr.pokemons:
        if i.ability!="Soundproof":
            if i.status=="Burned":
                print(" 💉 {i.name} was cured of burn!")
                i.status="Alive"  
            if i.status=="Frostbite":
                print(" 💉 {i.name} was cured of frostbite!")
                i.status="Alive"  
            if i.status=="Frozen":
                print(" 💉 {i.name} was cured of freeze!")
                i.status="Alive"  
            if i.status=="Badly Poisoned":
                print(" 💉 {i.name} was cured of poison!")
                i.status="Alive"  
            if i.status=="Sleep":
                print(" 💉 {i.name} was cured of sleep!")
                i.status="Alive"  
            if i.status=="Paralyzed":
                print(" 💉 {i.name} was cured of paralysis!")
                i.status="Alive"    
#AROMATHERAPY            
def aromatherapy(self,tr):
    print(f" 🏵️ {self.name} used "+colored(" Aromatherapy","green",attrs=["bold"])+"!")
    for i in tr.pokemons:
        if i.ability=="Sap Sipper":
            print(f" {i.name}'s {i.ability}.")
            atkchange(i,self,0.5)
        if i.ability!="Sap Sipper":
            if i.status=="Burned":
                print(" 💉 {i.name} was cured of burn!")
                i.status="Alive"  
            if i.status=="Frostbite":
                print(" 💉 {i.name} was cured of frostbite!")
                i.status="Alive"  
            if i.status=="Frozen":
                print(" 💉 {i.name} was cured of freeze!")
                i.status="Alive"  
            if i.status=="Badly Poisoned":
                print(" 💉 {i.name} was cured of poison!")
                i.status="Alive"  
            if i.status=="Sleep":
                print(" 💉 {i.name} was cured of sleep!")
                i.status="Alive"  
            if i.status=="Paralyzed":
                print(" 💉 {i.name} was cured of paralysis!")
                i.status="Alive" 
#WISH            
def wish(self,tr):
    print(f" 🌠 {self.name} used "+colored(" Wish","yellow",attrs=["bold"])+"!")
    if tr.wishhp is not False:
        print(" It failed!")
    if tr.wishhp is False:
        tr.wishhp=(self.maxhp/2)
#AQUA RING        
def aquaring(self,other):
    print(f" 💦 {self.name} used "+colored(" Aqua Ring","blue",attrs=["bold"])+"!")
    self.aring=True
#DOODLE
def doodle(self,other):
    print(f" 🎨 {self.name} used "+colored(" Doodle","white",attrs=["bold"])+"!")
    self.atktype="Normal"
    self.ability=other.ability
    print (f" {self.name} gained {other.ability}.")
#PAIN SPLIT    
def painsplit(self,other):
    print(f" 😖 {self.name} used "+colored(" Pain Split","white",attrs=["bold"])+"!")
    self.atktype="Normal"
    print(" The battlers shared their pain.")
    ab=weakness(self,other,field)
    a=ab[0]
    if a>0:
        self.hp=other.hp=(other.hp+self.hp)/2
#ENDEAVOR        
def endeavor (self,other):
    print(f" 🤒 {self.name} used "+colored(" Endeavor","white",attrs=["bold"])+"!")
    self.atktype="Normal"
    ab=weakness(self,other,field)
    a=ab[0]
    if self.hp<other.hp and a>0:
        other.hp=self.hp
#YAWN        
def yawn(self,other):
    print(f" 🥱 {self.name} used "+colored(" Yawn","white",attrs=["bold"])+"!")
    if other.yawn is False and other.status=="Alive":
        other.yawn=True
        print(f" {other.name} became drowsy!")
    else:
        print(" It failed!")
#SPICY EXTRACT        
def spicyextract(self,other):
    print(f" 🌶️🫑 {self.name} used "+colored(" Spicy Extract","green",attrs=["bold"])+"!")
    atkchange(other,self,1)
    defchange(other,self,-1)
#ELECTRIC TERRAIN    
def electricterrain(self,other, field,turn):
    self.atktype="Electric"
    print(f" {self.name} used "+colored(" Electric Terrain","yellow",attrs=["bold"])+"!")
    if field.terrain!="Electric":
        field.terrain="Electric"
        field.eleturn=turn
        field.eleend(self,other)
        print(" ⚡ An electric current ran across the battlefield!")
#MISTY TERRAIN    
def mistyterrain(self,other, field,turn):
    self.atktype="Fairy"
    print(f" {self.name} used "+colored(" Misty Terrain","magenta",attrs=["bold"])+"!")
    if field.terrain!="Misty":
        field.terrain="Misty"
        field.misturn=turn
        field.misend(self,other)
        print(" 🌸 Mist swirled around the battlefield!")
#GRASSY TERRAIN    
def grassyterrain(self,other,field,turn):
    self.atktype="Grass"
    print(f" {self.name} used "+colored(" Grassy Terrain","green",attrs=["bold"])+"!")
    if field.terrain!="Grassy":
        field.terrain="Grassy"
        field.grassturn=turn
        field.grassend(self,other)
        print(" 🌿 Grass grew to cover the battlefield!")   
#PSYCHIC TERRAIN    
def psychicterrain(self,other, field,turn):
    self.atktype="Psychic"
    print(f" {self.name} used "+colored(" Psychic Terrain","magenta",attrs=["bold"])+"!")
    if field.terrain!="Psychic":
        field.terrain="Psychic"
        field.psyturn=turn
        field.psyend(self,other)
        print(" 👁️ The battlefield got weird!")
def recycle(self,other):
    print(f" ♻️ {self.name} used "+colored(" Recycle","white",attrs=["bold"])+"!")
    if "Used" not in self.item:
        print(" It failed!")
    if ( "Used" in self.item and "m-Z" not in self.item and self.item not in megastones):
        self.item=self.item.split("[")[0]
        print(f" {self.name} recycled its {self.item}!")
#Skill Swap          
def skillswap(self,other):
    print(f" ♻️ {self.name} used "+colored(" Skill Swap","magenta",attrs=["bold"])+"!")
    if other.item!="Ability Shield":  
        print(f" {self.name} swapped its {self.ability} with {other.name}'s {other.ability}!")
        self.ability,other.ability=other.ability,self.ability  
#TRICK            
def trick(self,other):
    print(f" ♻️ {self.name} used "+colored(" Trick","magenta",attrs=["bold"])+"!")
    if other.item=="None" or (other.ability!="Sticky Hold" and "m-Z" not in other.item and other.item not in megastones):  
        print(f" {self.name} swapped its {self.item} with {other.name}'s {other.item}!")
        self.item,other.item=other.item,self.item
#TRICK-OR-TREAT        
def trickortreat(self,other):
    self.atktype="Ghost"
    print(f" 🎃 {self.name} used "+colored(" Trick-or-Treat","magenta",attrs=["bold"])+"!")
    other.type2=None
    other.type1="Ghost"
    print(f" {other.name} turned into {other.type1} type!")
#MAGIC POWDER    
def magicpowder(self,other):
    self.atktype="Water"
    print(f" 🔮 {self.name} used "+colored(" Magic Powder","magenta",attrs=["bold"])+"!")
    other.type2=None
    other.type1="Psychic"    
    print(f" {other.name} turned into {other.type1} type!")
#TAR SHOT    
def tarshot(self,other):
    self.atktype="Fire"
    print(f" 🔥 {self.name} used "+colored(" Tar Shot","red",attrs=["bold"])+"!")   
    speedchange(other,self,-0.5)
    if other.tarshot is False:
        other.tarshot=True     
#SOAK        
def soak(self,other):
    self.atktype="Water"
    print(f" 💦 {self.name} used "+colored(" Soak","blue",attrs=["bold"])+"!")
    other.type2=None
    other.type1="Water"    
    print(f" {other.name} turned into {other.type1} type!")
#FOREST'S CURSE'    
def forestscurse(self,other):
    self.atktype="Grass"
    print(f" 🌲 {self.name} used "+colored(" Forest's Curse","green",attrs=["bold"])+"!")
    other.type2=None
    other.type1="Grass"    
    print(f" {other.name} turned into {other.type1} type!")
#MAGMA STORM    
def magmastorm(self,other,turn):
    self.atktype="Fire"
    w=weathereff(self,other)
    al=1
    r=randroll()
    print(f" 🌋 {self.name} used "+colored(" Magma Storm","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=special(self,self.level,self.spatk,other.spdef,120,a,b,c,r,al,w)
    other.hp-=dmg
    if other.magmadmg is False:
        other.magmadmg=True
        self.magmaendturn=magma(turn,self)
def magma(turn,self):
    x=random.randint(2,5)        
    if self.item=="Binding Band":
        x=5
    return turn+x
#FUSION FLARE
def fusionflare(self,other):
    self.atktype="Fire"
    w=weathereff(self,other)
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Fusion Flare","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,100,a,b,c,r,al,w)        
#BLUE FLARE    
def blueflare(self,other):
    self.atktype="Fire"
    w=weathereff(self,other)
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" ⚜️ {self.name}'s {self.ability}.")
    print(f" 🔥 {self.name} used "+colored(" Blue Flare","cyan",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,130,a,b,c,r,al,w)
    burn(self,other,20)
#ICE BURN        
def iceburn(self,other):
    if self.item=="Power Herb" or self.precharge==True:
        if self.item=="Power Herb":
            self.item+="[Used]"
            print(f" {self.name} became fully charged due to its Power Herb.")
        self.atktype="Ice"
        w=weathereff(self,other)
        al=1
        r=randroll()
        if self.ability=="Sheer Force":
            al=1.5
            print(f" {self.name}'s {self.ability}.")
        print(f" ❄️🔥 {self.name} used "+colored(" Ice Burn","cyan",attrs=["bold"])+"!")
        c=isCrit(self,other)
        ab=weakness(self,other,field)
        a=ab[0]
        b=ab[1]   
        other.hp-=special(self,self.level,self.spatk,other.spdef,140,a,b,c,r,al,w)
        burn(self,other,30) 
        self.precharge=False  
    elif self.precharge==False:
        print(f" ❄️ {self.name} became cloaked in a freezing air!")
        self.precharge=True
       
#FIRE BLAST
def fireBlast(self,other):
    self.atktype="Fire"
    w=weathereff(self,other)
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" ⚜️ {self.name}'s {self.ability}.")
    print(f" 🔥 {self.name} used "+colored(" Fire Blast","red",attrs=["bold"])+"!")
    print("""      🔥                
      🔥
 🔥🔥🔥🔥🔥🔥
     🔥🔥
    🔥  🔥
   🔥    🔥"""  )
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,110,a,b,c,r,al,w)
    burn(self,other,10)
#SEARING SHOT            
def searingshot(self,other):
    self.atktype="Fire"
    w=weathereff(self,other)
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" ⚜️ {self.name}'s {self.ability}.")
    print(f" 🔥 {self.name} used "+colored(" Searing Shot","red",attrs=["bold"])+"!")
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,100,a,b,c,r,al,w)
    burn(self,other,30)  
    #FIERY WRATH   
def fierywrath(self,other):
    self.atktype="Dark"
    w=weathereff(self,other)
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" ⚜️ {self.name}'s {self.ability}.")
    print(f" 🌑🔥 {self.name} used "+colored(" Fiery Wrath","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,90,a,b,c,r,al,w)
    flinch(self,other,20)
#V-CREATE        
def vcreate(self,other):
    self.atktype="Fire"
    w=weathereff(self,other)
    al=1
    r=randroll()
    print(f" 🔥 {self.name} used "+colored(" V-Create","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,180,a,b,c,r,al,w)    
    if a!=0:
        defchange(self,self,-0.5)
        spdefchange(self,self,-0.5)
        speedchange(self,self,-0.5)
     
#STEAM ERUPTION    
def steameruption(self,other):
    self.atktype="Water"
    w=weathereff(self,other)
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" ⚜️ {self.name}'s {self.ability}.")
    print(f" 🌋🌊 {self.name} used "+colored(" Steam Eruption","blue",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,110,a,b,c,r,al,w)
    burn(self,other,30)
#PYRO BALL          
def pyroball(self,other):
    self.atktype="Fire"
    w=weathereff(self,other)
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" ⚜️ {self.name}'s {self.ability}.")
    print(f" 🔥⚽  {self.name} used "+colored(" Pyro Ball","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,120,a,b,c,r,al,w)
    burn(self,other,10)
#STRUGGLE        
def struggle(self,other):
    self.atktype="None"
    w=weathereff(self,other)
    al=1
    r=randroll()
    print(f" 😣 {self.name} used "+colored(" Struggle","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,50,a,b,c,r,al,w)     
    self.hp-=(self.maxhp/8)    
#FIERY DANCE    
def fierydance(self,other):
    self.atktype="Fire"
    w=weathereff(self,other)
    al=1
    r=randroll()
    print(f" 🔥🪰 {self.name} used "+colored(" Fiery Dance","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,80,a,b,c,r,al,w)        
    ch=random.randint(1,2)
    if ch==1:
        spatkchange(self,self,0.5)
       
#REST        
def rest(self,other,turn):
    print(f" 😪 {self.name} used "+colored(" Rest","magenta",attrs=["bold"])+"!")
    if self.status!="Sleep" and self.hp!=self.maxhp:
        self.status="Sleep"
        print(f" {self.name} fell asleep.")
        self.sleependturn=turn+random.randint(2,5)
        self.hp=self.maxhp
#LUSTER PURGE        
def lusterpurge(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" ⚜️ {self.name}'s {self.ability}.")
    print(f" ✈️ {self.name} used "+colored(" Luster Purge","magenta",attrs=["bold"])+"!")
    self.atktype="Psychic"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,90,a,b,c,r,al)
    ch=random.randint(1,2)
    if ch==2 and self.ability=="Sheer Force" and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil","Shield Dust"] and a!=0:
        spdefchange(other,self,-0.5)
        
#MIST BALL        
def mistball(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" ⚜️ {self.name}'s {self.ability}.")
    print(f" 🔮 {self.name} used "+colored(" Mist Ball","magenta",attrs=["bold"])+"!")
    self.atktype="Psychic"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,90,a,b,c,r,al)
    ch=random.randint(1,2)
    if ch==2 and self.ability=="Sheer Force" and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil","Shield Dust"] and a!=0:
        spatkchange(other,self,-0.5)
        
#LUMINA CRASH        
def luminacrash(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" ⚜️ {self.name}'s {self.ability}.")
    print(f" 👁️ {self.name} used "+colored(" Lumina Crash","magenta",attrs=["bold"])+"!")
    self.atktype="Psychic"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,80,a,b,c,r,al)
    if other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"] and a!=0:
        spdefchange(other,self,-1)
      
#PSYCHIC        
def psychic(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" ⚜️ {self.name}'s {self.ability}.")
    print(f" 👁️ {self.name} used "+colored(" Psychic","magenta",attrs=["bold"])+"!")
    self.atktype="Psychic"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,90,a,b,c,r,al)
    chance=10
    if self.ability=="Serene Grace":
        chance*=2
    if self.speed>other.speed:
        ch=random.randint(1,100)            
        if ch>(100-chance) and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil","Shield Dust"] and a!=0:
            spdefchange(other,self,-0.5)
            
#BELLY DRUM        
def bellydrum(self,other):
    print(f" 🩸🪘 {self.name} used "+colored(" Belly Drum","red",attrs=["bold"])+"!")
    if self.hp>(self.maxhp/3):
        atkchange(self,self,4)
        self.hp-=(self.maxhp/2)
        print(f" {self.name} cuts its own HP and maximized its Attack.")
        
    else:
        print(" It failed.")    
#SUPER FANG        
def superfang(self,other):        
    print(f" 🦷 {self.name} used "+colored(" Super Fang","white",attrs=["bold"])+"!")
    ab=weakness(self,other,field)
    a=ab[0]
    other.hp-=a*(round(other.hp/2))
#EERIE IMPULSE    
def eerieimpulse(self,other):
    print(f" ⚡ {self.name} used "+colored(" Eerie Impulse","yellow",attrs=["bold"])+"!")
    spatkchange(other,self,-1)
   
#CHARM    
def charm(self,other):
    print(f" 🥰 {self.name} used "+colored(" Charm","magenta",attrs=["bold"])+"!")
    atkchange(other,self,-1)

def scaryface(self,other):
    print(f" 👿 {self.name} used "+colored(" Scary Face","white",attrs=["bold"])+"!")
    speedchange(other,self,-1)
    
def venomdrench(self,other):
    print(f" ☣️ {self.name} used "+colored(" Venom Drench","magenta",attrs=["bold"])+"!")
    if other.status not in ["Poisoned","Badly Poisoned"]:
        print(" It failed.")
    if other.status in ["Poisoned","Badly Poisoned"]:
        atkchange(other,self,-0.5)    
        spatkchange(other,self,-0.5)   
        speedchange(other,self,-0.5)   
def tickle(self,other):
    print(f" 😂 {self.name} used "+colored(" Tickle","white",attrs=["bold"])+"!")
    atkchange(other,self,-0.5)    
    defchange(other,self,-0.5)              
      
def metalsound(self,other):
    print(f" 🔊 {self.name} used "+colored(" Metal Sound","white",attrs=["bold"])+"!")
    spdefchange(other,self,-1)    
    
def swagger(self,other,turn):
    print(f" 😎 {self.name} used "+colored(" Swagger","white",attrs=["bold"])+"!")
    atkchange(other,self,1)
    confuse(self,other,turn,100)
        
def faketears(self,other):
    print(f" 😢 {self.name} used "+colored(" Fake Tears","red",attrs=["bold"])+"!")
    spdefchange(other,self,-1)

def featherdance(self,other):
    print(f" 🪶 {self.name} used "+colored(" Feather Dance","cyan",attrs=["bold"])+"!")
    atkchange(other,self,-1)    
            
    #SWORDS DANCE
def swordsdance(self,other):
    print(f" ⚔️ {self.name} used "+colored(" Swords Dance","white",attrs=["bold"])+"!")
    if self.atkb<4:
        atkchange(self,self,1)
#FILLET AWAY    
def filletaway(self,other):
    print(f" 🐟 {self.name} used "+colored(" Fillet Away","blue",attrs=["bold"])+"!")
    atkchange(self,self,1)
    spatkchange(self,self,1)
    speedchange(self,self,1)
    self.hp-=self.maxhp/3
#CURSE    
def curse(self,other):
    print(f" {self.name} used "+colored(" Curse","red",attrs=["bold"])+"!")
    if "Ghost" not in (self.type1,self.type2,self.tera):
        atkchange(self,self,0.5)
        defchange(self,self,0.5)
        speedchange(self,self,-0.5)
    else:
        if other.cursed!=True:
            self.hp-=(self.maxhp/2)  
            print(f" {self.name} cut its own HP and put a curse on {other.name}!")
            other.cursed=True      
    
#TAIL GLOW    
def tailglow(self,other):
    print(f" {self.name} used Tail Glow.")
    spatkchange(self,self,1.5)
    print(f" {self.name} drastically raised its attack!")   
#Growth
def growth(self,other):
    print(f" 🪴 {self.name} used "+colored(" Growth","white",attrs=["bold"])+"!")
    spatkchange(self,self,0.5)
    atkchange(self,self,0.5)
#NASTY PLOT       
def nastyplot(self,other):
    print(f" ❔ {self.name} used "+colored(" Nasty Plot","red",attrs=["bold"])+"!")
    if self.spatkb<4:
        spatkchange(self,self,1)
#CALM MIND    
def calmmind(self,other):
    print(f" 👁️ {self.name} used "+colored(" Calm Mind","magenta",attrs=["bold"])+"!")
    spatkchange(self,self,0.5)
    spdefchange(self,self,0.5)
    
#CORROSIVE GAS    
def corrosivegas(self,other):
    print(f" 🥽 {self.name} used "+colored(" Corrosive Gas","magenta",attrs=["bold"])+"!")
    if other.item!=None:
        print (f" {self.name}'s corrosive gas melted {other.name}'s {other.item}!")
        other.item+="[Used]"
#ACID ARMOR           
def acidarmor(self,other):
    print(f" 💦 {self.name} used "+colored(" Acid Armor","blue",attrs=["bold"])+"!")
    defchange(self,self,1)
    
#SHELTER      
def shelter(self,other):
    print(f" 🐚 {self.name} used "+colored(" Shelter","white",attrs=["bold"])+"!")   
    defchange(self,self,1)
#COSMIC POWER
def cosmicpower(self,other):
    print(f" 🌌 {self.name} used "+colored(" Cosmic Power","yellow",attrs=["bold"])+"!")
    defchange(self,self,0.5)  
    spdefchange(self,self,0.5)
#AMNESIA    
def amnesia(self,other):
    print(f" ❓ {self.name} used "+colored(" Amnesia","magenta",attrs=["bold"])+"!")  
    spdefchange(self,other,1)
#ACID SPRAY    
def acidspray(self,other):
    al=1
    r=randroll()
    print(f" 🧯 {self.name} used "+colored(" Acid Spray","magenta",attrs=["bold"])+"!")
    self.atktype="Poison"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,40,a,b,c,r,al)   
    spdefchange(self,self,-1)
    
#AGILITY    
def agility(self,other):
    print(f" ⚡ {self.name} used "+colored(" Agility","magenta",attrs=["bold"])+"!")
    speedchange(self,other,1)
#ROCK POLISH    
def rockpolish(self,other):
    print(f" 🪨🌟 {self.name} used "+colored(" Rock Polish","yellow",attrs=["bold"])+"!")
    speedchange(self,other,1)  
#IRON DEFENSE    
def barrier(self,other):
    print(f" 🟦 {self.name} used "+colored(" Barrier","magenta",attrs=["bold"])+"!")
    if self.defb<4:
        defchange(self,other,1)
def irondefense(self,other):
    print(f" ⛑️ {self.name} used "+colored(" Iron Defense","white",attrs=["bold"])+"!")
    if self.defb<4:
        defchange(self,other,1)
#COTTON GUARD     
def cottonguard(self,other):
    print(f" 🧶 {self.name} used "+colored(" Cotton Guard","green",attrs=["bold"])+"!")
    defchange(self,other,1.5)
#LEECH SEED    
def leechseed(self,other):
    print(f" 🌱 {self.name} used "+colored(" Leech Seed","green",attrs=["bold"])+"!")
    if "Grass" not in (other.type1,other.type2,other.teratype) and other.ability!="Magic Bounce" and other.seeded is False:
        other.seeded=True
        print(f" 🌱{other.name} was seeded.")
    elif "Grass" not in (self.type1,self.type2,self.teratype) and other.ability=="Magic Bounce" and self.seeded is False:
        self.seeded=True
        print(f" {other.name}'s Magic Bounce!")
        print(f" {self.name} was seeded.")
#STRENGTH SAP    
def strengthsap(self,other):
    print(f" 🌱 {self.name} used "+colored(" Strength Sap","green",attrs=["bold"])+"!")
    if other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        prevatk=other.atk
        atkchange(other,self,-0.5)
        heal=prevatk
             
        if heal<=(self.maxhp-heal):
            self.hp+=heal
        else:
            self.hp=self.maxhp
    else:
        print (" It Failed!")
#DEFEND ORDER        
def defendorder(self,other):
    print(f" 🐝🛡️ {self.name} used "+colored(" Defend Order","green",attrs=["bold"])+"!")
    spdefchange(self,other,0.5)     
    defchange(self,other,0.5)   
#TOXIC THREAD    
def toxicthread(self,other):
    print(f" 🕷️🕸️ {self.name} used "+colored(" Toxic Thread","magenta",attrs=["bold"])+"!")
    if other.status=="Alive":
        poison(self,other,100)
    speedchange(other,self,-0.5)     
        
#BULK UP    
def bulkup(self,other):
    print(f" 💪🏻 {self.name} used "+colored(" Bulk Up","red",attrs=["bold"])+"!")
    atkchange(self,other,0.5)     
    defchange(self,other,0.5)   
    
def skullbash(self,other):       
    print(f" ⛑️ {self.name} used "+colored(" Skull Bash","white",attrs=["bold"])+"!")
    if self.item=="Power Herb" or self.precharge is True:
        if self.item=="Power Herb":
            self.item+="[Used]"  
            atkchange(self,other,0.5)
            defchange(self,other,0.5)
            print(f" {self.name} became fully charged due to its Power Herb.")
            
        al=1
        r=randroll()
        self.atktype="Normal"
        c=isCrit(self,other)
        ab=weakness(self,other,field)
        a=ab[0]
        b=ab[1]   
        other.hp-=special(self,self.level,self.spatk,other.spdef,130,a,b,c,r,al)    
        self.precharge=False
    else:
        print(f" {self.name} lowered it's head.")
        atkchange(self,other,0.5)
        defchange(self,other,0.5)
        self.precharge=True    
        
def meteorbeam(self,other):       
    print(f" ☄️ {self.name} used "+colored(" Meteor Beam","yellow",attrs=["bold"])+"!")
    if self.item=="Power Herb" or self.precharge is True:
        if self.item=="Power Herb":
            self.item+="[Used]"  
            spatkchange(self,other,0.5)
            print(f" {self.name} became fully charged due to its Power Herb.")
        al=1
        r=randroll()
        self.atktype="Rock"
        c=isCrit(self,other)
        ab=weakness(self,other,field)
        a=ab[0]
        b=ab[1]   
        other.hp-=special(self,self.level,self.spatk,other.spdef,120,a,b,c,r,al)    
        self.precharge=False
    else:
        print(f" {self.name} is overflowing with space power!")
        spatkchange(self,other,0.5)
        self.precharge=True
        
def geomancy(self,other):
    print(f" 🌈 {self.name} used "+colored(" Geomancy","magenta",attrs=["bold"])+"!")
    if self.item=="Power Herb":
        print(f" {self.name} became fully charged due to its Power Herb.")
        spatkchange(self,other,1)     
        spdefchange(self,other,1)   
        speedchange(self,other,1)
        self.precharge=False
        self.item+="[Used]"
    else:
        print(f" {self.name} is absorbing power.")
        self.precharge=True
def coil(self,other):
    print(f" 🐍 {self.name} used "+colored(" Coil","green",attrs=["bold"])+"!")
    atkchange(self,other,0.5)     
    defchange(self,other,0.5)   
    self.accuracy+=10
    print(f" 🔼 {self.name}'s accuracy rose!")
    
def autotomize(self,other):
    print(f" 🔩 {self.name} used "+colored(" Autotomize","white",attrs=["bold"])+"!")
    speedchange(self,other,1)
def mortalspin(self,other,tr1):
    print(f" 🥏 {self.name} used "+colored(" Mortal Spin","magenta",attrs=["bold"])+"!")
    self.atktype="Poison"
    if other.status=="Alive":
        poison(self,other,100)
    if self.seeded is True:
        self.seeded=False
    if len(tr1.hazard)>0:
        tr1.hazard=[]
        print(f" {self.name} removed hazards from its side!")   
def tidyup(self,other,tr1):
    print(f" 🧹 {self.name} used "+colored(" Tidu Up","white",attrs=["bold"])+"!")
    tr1.hazard=[]       
    atkchange(self,other,0.5)
    speedchange(self,other,0.5)
def rapidspin(self,other,tr1):
    print(f" 🥏 {self.name} used "+colored(" Rapid Spin","white",attrs=["bold"])+"!")
    self.atktype="Normal"
    al=1
    r=randroll()
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    base=20
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)      
    speedchange(self,other,0.5)
    if self.firespin!=0 or self.infestation!=0 or self.whirlpool!=0:
        self.firespin=self.infestation=self.whirlpool=False
        print(f" {self.name} was freed.")
    if len(tr1.hazard)>0:
        tr1.hazard=[]
        print(f" {self.name} removed hazards from its side!")
        
def dragondance(self,other):
    print(f" 🐉 {self.name} used "+colored(" Dragon Dance","red",attrs=["bold"])+"!")   
    atkchange(self,other,0.5)
    speedchange(self,other,0.5)
    
def quiverdance(self,other):
    print(f" 🦋 {self.name} used "+colored(" Quiver Dance","green",attrs=["bold"])+"!")
    spatkchange(self,other,0.5)
    speedchange(self,other,0.5)
    spdefchange(self,other,0.5)
              
def shellsmash(self,other):
    print(f" 🐚 {self.name} used "+colored(" Shell Smash","blue",attrs=["bold"])+"!")
    atkchange(self,other,1)
    spatkchange(self,other,1)
    speedchange(self,other,1)
    defchange(self,self,-0.5)
    spdefchange(self,self,-0.5)
   
       
def infernooverdrive(self,other):
    self.atktype="Fire"
    al=1
    r=randroll()
    print(f" 🔥💥 {self.name} used "+colored(" Inferno Overdrive","red",attrs=["bold"])+"!")
    w=weathereff(self,other)
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,200,a,b,c,r,al,w)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,200,a,b,c,r,al,w)   
        
def gmaxcentiferno(self,other):
    self.atktype="Fire"
    al=1
    w=weathereff(self,other)
    r=randroll()
    print(f" 🔺㊗️ {self.name} used "+colored(" G-Max Centiferno","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al,w)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al,w)    
    if other.cntdmg is False and "Fire" not in (other.type1,other.type2,other.teratype) and other.hp>0:
        other.cntdmg=True
        print(f" ㊗️ {other.name} was trapped by vortex of fire!")
        self.cntendturn=turn+4
        
def gmaxwildfire(self,other,turn):
    self.atktype="Fire"
    al=1
    w=weathereff(self,other)
    r=randroll()
    print(f" 🔺🔥 {self.name} used "+colored(" G-Max Wildfire","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al,w)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al,w)    
    if other.wfdmg is False and "Fire" not in (other.type1,other.type2,other.teratype) and other.hp>0:
        other.wfdmg=True
        print(f" 🔥 {other.name} was surrounded by fire!")
        self.wfendturn=turn+4
        
def naturesmadness(self,other):
    print(f" 🏝️ {self.name} used used "+colored(" Nature's Madness","magenta",attrs=["bold"])+"!")
    self.atktype="Fairy"
    other.hp-=round(other.hp/2)
    
def gmaxbefuddle(self,other):
    self.atktype="Bug"
    al=1
    r=randroll()
    print(f" 🔺🦋 {self.name} used "+colored(" G-Max Befuddle","green",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)    
    if other.status=="Alive":
        other.status=random.choice(["Paralyzed","Badly Poisoned","Sleep"])
        
def gmaxdrumsolo(self,other):
    self.atktype="Grass"
    al=1
    r=randroll()
    w=weathereff(self,other)
    print(f" 🔺🥁 {self.name} used "+colored(" G-Max Drum Solo","green",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al,w)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al,w)           
        
def gmaxstonesurge(self,other,tr):
    self.atktype="Water"
    al=1
    r=randroll()
    w=weathereff(self,other)
    print(f" 🔺🪨🌊 {self.name} used "+colored(" G-Max Stonesurge","blue",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al,w)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al,w)            
    if "Stealth Rock" not in tr.hazard:
        tr.hazard.append("Stealth Rock")
        print(" Pointed stones float in the air around the opposing team!")
        
def gmaxhydrosnipe(self,other):
    self.atktype="Water"
    al=1
    r=randroll()
    w=weathereff(self,other)
    print(f" 🔺🎯☄️ {self.name} used "+colored(" G-Max Hydrosnipe","blue",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al,w)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al,w)  
def gmaxfireball(self,other):
    self.atktype="Fire"
    al=1
    r=randroll()
    w=weathereff(self,other)
    print(f" 🔺🔥⚽ {self.name} used "+colored(" G-Max Fireball","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al,w)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al,w)          
        
def gmaxfoamburst(self,other):
    self.atktype="Water"
    al=1
    r=randroll()
    w=weathereff(self,other)
    print(f" 🔺🦀 {self.name} used "+colored(" G-Max Foam Burst","blue",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al,w)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al,w)  
    if a!=0:   
        
        speedchange(other,self,-1)         
           
def gmaxcannonade(self,other,turn):
    self.atktype="Water"
    al=1
    r=randroll()
    w=weathereff(self,other)
    print(f" 🔺💣🌊 {self.name} used "+colored(" G-Max Cannonade","blue",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al,w)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al,w)     
    if other.cndmg is False and "Water" not in (other.type1,other.type2,other.teratype) and other.hp>0:
        other.cndmg=True
        print(f" 🌊 {other.name} got caught in the vortex of water!")
        self.cnendturn=turn+4   
        
def hydrovortex(self,other):
    self.atktype="Water"
    al=1
    r=randroll()
    print(f" 🌊🌪️ {self.name} used "+colored(" Hydro Vortex","blue",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,200,a,b,c,r,al)           
        
def bloomdoom(self,other):
    al=1
    r=randroll()
    print(f" 🌳💥 {self.name} used "+colored(" Bloom Doom","green",attrs=["bold"])+"!")
    self.atktype="Grass"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,200,a,b,c,r,al)
#GMAX VINE LASH                
def gmaxvinelash(self,other,turn):
    al=1
    r=randroll()
    print(f" 🔺🌿 {self.name} used "+colored(" G-Max Vine Lash","green",attrs=["bold"])+"!")
    self.atktype="Grass"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)        
    if other.vldmg is False and "Grass" not in (other.type1,other.type2,other.teratype) and other.hp>0:
        other.vldmg=True
        print(f" 🌿 {other.name} got trapped with vines!")
        self.vlendturn=turn+4  
def gmaxtartness(self,other):
    al=1
    r=randroll()
    print(f" 🔺🍏 {self.name} used "+colored(" G-Max Tartness","green",attrs=["bold"])+"!")
    self.atktype="Grass"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)             
    other.evasion+=10   
def gmaxsweetness(self,other):
    al=1
    r=randroll()
    print(f" 🔺🍎 {self.name} used "+colored(" G-Max Sweetness","green",attrs=["bold"])+"!")
    self.atktype="Grass"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)                 
    self.status="Alive"
def maxovergrowth(self,other,turn):
    al=1
    r=randroll()
    print(f" 🔺🌳 {self.name} used "+colored(" Max Overgrowth","green",attrs=["bold"])+"!")
    self.atktype="Grass"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)         
    if field.terrain!="Grassy" and a!=0:
        field.terrain="Grassy"   
        field.grassturn=turn
        field.grassend(self,other)
        print(" 🌿 Grass grew to cover the battlefield!")    
        
def maxlightning (self,other,turn):
    al=1
    r=randroll()
    print(f" 🔺⚡ {self.name} used"+colored(" Max Lightning","yellow",attrs=["bold"])+"!")
    self.atktype="Electric"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)      
    if field.terrain!="Electric" and a!=0:
        field.terrain="Electric"  
        field.eleturn=turn
        field.eleend(self,other)
        print(" ⚡ An electric current ran across the battlefield!")
        
def gmaxstunshock(self,other):
    al=1
    r=randroll()
    print(f" 🔺🎸 {self.name} used "+colored(" G-Max Stun Shock","yellow",attrs=["bold"])+"!")
    self.atktype="Electric"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)                
    if other.status=="Alive" and a!=0:
        other.status=random.choice(["Paralyzed","Badly Poisoned"])       
        
def gmaxvoltcrash(self,other):
    al=1
    r=randroll()
    print(f" 🔺⚡ {self.name} used "+colored(" G-Max Volt Crash","yellow",attrs=["bold"])+"!")
    self.atktype="Electric"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)                
    if other.status=="Alive" and a!=0:
        other.status="Paralyzed"
        
def gigavolthavoc(self,other):
    al=1
    r=randroll()
    print(f" ⚡💥 {self.name} used "+colored(" Gigavolt Havoc","yellow",attrs=["bold"])+"!")
    self.atktype="Electric"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,200,a,b,c,r,al)  
def exevoboost(self,other):
    print(f" 🌈 {self.name} used "+colored(" Extreme Evoboost","white",attrs=["bold"])+"!")
    atkchange(self,other,1)
    defchange(self,other,1)
    spatkchange(self,other,1)
    spdefchange(self,other,1)
    speedchange(self,other,1)
    print(f" {self.name} sharply boosted all of its stats!")
        
def sparksurf(self,other):
    al=1
    r=randroll()
    print(f" ⚡🏄 {self.name} used "+colored(" Stoked Sparksurfer","yellow",attrs=["bold"])+"!")
    self.atktype="Electric"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,175,a,b,c,r,al)    
    paralayzed(self,other,100)
    
def tenmvolttb(self,other):
    al=1
    r=randroll()
    print(f" ⚡💥 {self.name} used "+colored(" 10,000,000 Volt Thunderbolt","yellow",attrs=["bold"])+"!")
    self.atktype="Electric"
    c=isCrit(self,other,2)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    other.hp-=special(self,self.level,self.spatk,other.spdef,195,a,b,c,r,al)
    
def catastropika(self,other):
    al=1
    r=randroll()
    print(f" ⚡💥 {self.name} used "+colored(" Catastropika","yellow",attrs=["bold"])+"!")
    self.atktype="Electric"
    c=isCrit(self,other,2)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,210,a,b,c,r,al)              
       
def stormshards(self,other):
    al=1
    r=randroll()
    print(f" 🪨☄️ {self.name} used "+colored(" Splintered Stormshards","yellow",attrs=["bold"])+"!")   
    self.atktype="Rock"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,190,a,b,c,r,al)      
    if field.terrain!="Normal":
        field.terrain="Normal"
        print(" 🌐 The battlefield turned normal.")     
        
def gmaxvolcalith(self,other,turn,optr):
    al=1
    r=randroll()
    print(f" 🔺🪨🔥 {self.name} used "+colored(" G-Max Volcalith","red",attrs=["bold"])+"!")   
    self.atktype="Rock"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)        
    if optr.vcdmg is False and "Rock" not in (other.type1,other.type2,other.teratype) and other.hp>0:
        optr.vcdmg=True
        print(" 🪨 The opposing Pokémon became surrounded by rocks!")
        optr.vcendturn=turn+4 
         
def continentalcrush(self,other):
    al=1
    r=randroll()
    print(f" 🌏🪨 {self.name} used "+colored(" Continental Crush","yellow",attrs=["bold"])+"!")   
    self.atktype="Rock"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,200,a,b,c,r,al)          
        
def tectonicrage(self,other):
    al=1
    r=randroll()
    print(f" ⛰️ {self.name} used "+colored(" Tectonic Rage","yellow",attrs=["bold"])+"!")
    self.atktype="Ground"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,200,a,b,c,r,al)   
        
def maxquake(self,other):
    al=1
    r=randroll()
    print(f" 🔺⛰️ {self.name} used "+colored(" Max Quake","yellow",attrs=["bold"])+"!")
    self.atktype="Ground"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)          
    if a!=0:  
        spdefchange(self,other,0.5)       
        
def gmaxsandblast(self,other,tr1,turn):
    al=1
    r=randroll()
    print(f" 🔺🏜️ {self.name} used "+colored(" G-Max Sandblast","yellow",attrs=["bold"])+"!")
    self.atktype="Ground"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)            
    if field.weather not in ["Desolate Land","Primordial Sea","Strong Wind","Sandstorm"]:
        print(f" 🏜️ {self.name} started a sandstorm.")
        field.weather="Sandstorm" 
        tr1.sandturn=turn
        tr1.sandend(self,other)                
def corkscrewcrash(self,other):
    al=1
    r=randroll()
    print(f" 🔩💥 {self.name} used "+colored(" Corkscrew Crash","white",attrs=["bold"])+"!")
    self.atktype="Steel"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,200,a,b,c,r,al)          
def searingsunrazesmash(self,other):
    al=1
    r=randroll()
    print(f" ☀️🌌 {self.name} used "+colored(" Searing Sunraze Smash","yellow",attrs=["bold"])+"!")
    self.atktype="Steel"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1] 
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,200,a,b,c,r,al)      
def menacingmoonrazemaelstrom(self,other):
    al=1
    r=randroll()
    print(f" 🌘🌌 {self.name} used "+colored(" Menacing Moonraze Maelstrom","cyan",attrs=["bold"])+"!")
    self.atktype="Ghost"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,200,a,b,c,r,al)    
def soulstealing(self,other):
    al=1
    r=randroll()
    print(f" 👤💥 {self.name} used "+colored(" Soul-Stealing 7-Star Strike","magenta",attrs=["bold"])+"!")
    self.atktype="Ghost"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,200,a,b,c,r,al)      
def moonsault(self,other):
    al=1
    r=randroll()
    print(f" 🤼‍♂️💥 {self.name} used "+colored(" Malicious Moonsault","red",attrs=["bold"])+"!")
    self.atktype="Dark"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,180,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,180,a,b,c,r,al)           
def operetta(self,other):
    al=1
    r=randroll()
    print(f" 🦭🎶 {self.name} used "+colored(" Oceanic Operetta","blue",attrs=["bold"])+"!")
    self.atktype="Water"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,195,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,195,a,b,c,r,al)                    
def arrowraid(self,other):
    al=1
    r=randroll()
    print(f" 🎯💥 {self.name} used "+colored(" Sinister Arrow Raid","magenta",attrs=["bold"])+"!")
    self.atktype="Ghost"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,180,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,180,a,b,c,r,al)      
def gmaxsteelsurge(self,other,optr):
    al=1
    r=randroll()
    print(f" 🔺🐘 {self.name} used "+colored(" G-Max Steelsurge","white",attrs=["bold"])+"!")
    self.atktype="Steel"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)
    if "Steel Spikes" not in optr.hazard:
        print(" 📌 Sharp-pointed pieces of steel started floating around your ally Pokémon!")
        optr.hazard.append("Steel Spikes")                                               
def maxsteelspike(self,other):
    al=1
    r=randroll()
    print(f" 🔺🔩 {self.name} used "+colored(" Max Steelspike","white",attrs=["bold"])+"!")
    self.atktype="Steel"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)                  
    defchange(self,other,0.5)
    
def gmaxmeltdown(self,other):
    al=1
    r=randroll()
    print(f" 🔺🔩 {self.name} used "+colored(" G-Max Meltdown","white",attrs=["bold"])+"!")
    self.atktype="Steel"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)     
def breakneckblitz(self,other):
    al=1
    r=randroll()
    print(f" ⚡ {self.name} used"+colored(" Breakneck Blitz","white",attrs=["bold"])+"!")
    self.atktype="Normal"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,200,a,b,c,r,al)  
def pulverizingpancake(self,other):
    al=1
    r=randroll()
    print(f" 🥞 {self.name} used "+colored(" Pulverizing Pancake","white",attrs=["bold"])+"!")
    self.atktype="Normal"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spdef>self.defense:
        other.hp-=special(self,self.level,self.spdef,other.spdef,210,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.defense,other.defense,210,a,b,c,r,al)            
def gmaxreplenish(self,other):
    al=1
    r=randroll()
    print(f" 🔺🍐 {self.name} used "+colored(" G-Max Replenish","white",attrs=["bold"])+"!")
    self.atktype="Normal"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)         
    if self.item is None and self.hp<=self.maxhp-(self.maxhp/4):
        print(f" {self.name} obtained a Sitrus Berry")  
        self.item="Sitrus Berry"
def maxstrike(self,other):
    al=1
    r=randroll()
    print(f" 🔺✴️ {self.name} used "+colored(" Max Strike","white",attrs=["bold"])+"!")
    self.atktype="Normal"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)        
    if a!=0: 
        speedchange(other,self,-0.5)    
        
def gmaxcuddle(self,other):
    al=1
    r=randroll()
    print(f" 🔺🤗 {self.name} used "+colored(" G-Max Cuddle","white",attrs=["bold"])+"!")
    self.atktype="Normal"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)    
    other.infatuated=True
def gmaxgoldrush(self,other,turn):
    al=1
    r=randroll()
    print(f" 🔺🪙 {self.name} used "+colored(" G-Max Gold Rush","yellow",attrs=["bold"])+"!")
    self.atktype="Normal"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)    
    confuse(self,other,turn,100)
def glare(self,other):
    print(f" 👁️ {self.name} used "+colored(" Glare","yellow",attrs=["bold"])+"!")
    if other.status=="Alive":
         paralyzed(self,other,100)
def thunderwave(self,other):
    print(f" ⚡ {self.name} used "+colored(" Thunder Wave","yellow",attrs=["bold"])+"!")
    paralyzed(self,other,100)
def sweetkiss(self,other,turn):
    print(f" 💋 {self.name} used "+colored(" Sweet Kiss","white",attrs=["bold"])+"!")
    confuse(self,other,turn,100)        
def lovelykiss(self,other,turn):
    print(f" 💋 {self.name} used "+colored(" Lovely Kiss","white",attrs=["bold"])+"!")
    if other.status=="Alive":
        sleep(self,other,100,turn)
    else:
        print(" It failed.")        
def sleeppowder(self,other,turn):
    print(f" 🍄 {self.name} used "+colored(" Sleep Powder","green",attrs=["bold"])+"!")
    if other.status=="Alive" and "Safety Googles" not in other.item:
        sleep(self,other,100,turn)
    else:
        print(" It failed.")
def stunspore(self,other):
    print(f" 🍄 {self.name} used "+colored(" Stun Spore","green",attrs=["bold"])+"!")
    if other.status=="Alive" and "Safety Googles" not in other.item:
        paralyzed(self,other,100)
    else:
        print(" It failed.")              
        
def spore(self,other,turn):
    print(f" 🍄 {self.name} used "+colored(" Spore","green",attrs=["bold"])+"!")
    if other.ability!="Sap Sipper" and "Safety Googles" not in other.item:
        sleep(self,other,100,turn)    
    if "Sap Sipper" in other.ability:
        print(f" {other.name}'s Sap Sipper!")
        atkchange(other,self,0.5)        
def hypnosis(self,other,turn):
    print(f" 😵‍💫 {self.name} used "+colored(" Hypnosis","magenta",attrs=["bold"])+"!")
    sleep(self,other,60,turn)        
        
def darkvoid(self,other,turn):
    print(f" 🌑 {self.name} used "+colored(" Dark Void","red",attrs=["bold"])+"!")
    sleep(self,other,100,turn)         
        
def shatteredpsyche(self,other):
    al=1
    r=randroll()
    print(f" 👁️💥 {self.name} used "+colored(" Shattered Psyche","magenta",attrs=["bold"])+"!")
    self.atktype="Psychic"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,200,a,b,c,r,al)    
def skyburn(self,other):
    al=1
    r=randroll()
    print(f" 🌌🔥 {self.name} used "+colored(" Light That Burns The Sky","yellow",attrs=["bold"])+"!")
    self.atktype="Psychic"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=special(self,self.level,self.atk,other.spdef,200,a,b,c,r,al)          
def genesissupernova(self,other,field,turn):
    al=1
    r=randroll()
    print(f" 🧬💥 {self.name} used "+colored(" Genesis Supernova","magenta",attrs=["bold"])+"!")
    self.atktype="Psychic"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,185,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,185,a,b,c,r,al)      
    if field.terrain!="Psychic":
        field.terrain="Psychic"       
        field.psyturn=turn
        field.psyend(self,other)
def gmaxgravitas(self,other,field,turn):
    al=1
    r=randroll()
    print(f" 🔺🛸 {self.name} used "+colored(" G-Max Gravitas","magenta",attrs=["bold"])+"!")
    self.atktype="Psychic"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)         
    if other.grav is False and other.hp>0:
        other.grav=True
        print(f" 🛸 {other.name} got pulled down by intense gravity!")
        self.gravendturn=turn+5
            
def maxmindstorm(self,other,field,turn):
    al=1
    r=randroll()
    print(f" 🔺👁️ {self.name} used "+colored(" Max Mindstorm","magenta",attrs=["bold"])+"!")
    self.atktype="Psychic"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)      
    if field.terrain!="Psychic" and a!=0:
        field.terrain="Psychic"       
        field.psyturn=turn
        field.psyend(self,other)
        print(" 👁️ The battlefield got weird!")  
        
def gmaxterror(self,other):
    al=1
    r=randroll()
    print(f" 🔺🪑 {self.name} used "+colored(" G-Max Terror","magenta",attrs=["bold"])+"!")
    self.atktype="Ghost"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)            
    other.trap=self        
def maxphantasm(self,other):
    al=1
    r=randroll()
    print(f" 🔺👻 {self.name} used "+colored(" Max Phantasm","magenta",attrs=["bold"])+"!")
    self.atktype="Ghost"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)    
    if a!=0:
        defchange(other,self,-0.5)              
          
    
def neverendingnightmare(self,other):
    al=1
    r=randroll()
    print(f" 👻 {self.name} used "+colored(" Never-ending Nightmare","magenta",attrs=["bold"])+"!")
    self.atktype="Ghost"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,200,a,b,c,r,al)                 
        
def blackholeeclipse(self,other):
    al=1
    r=randroll()
    print(f" 🕳️ {self.name} used "+colored(" Black Hole Eclipse","red",attrs=["bold"])+"!")
    self.atktype="Dark"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,200,a,b,c,r,al)     
        
def gmaxrapidflow(self,other):
    al=1
    r=randroll()
    print(f" 🔺🌊 {self.name} used  "+colored("G-Max Rapid Flow","blue",attrs=["bold"])+"!")
    self.atktype="Water"
    w=weathereff(self,other)
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al,w)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al,w)          
                
def gmaxoneblow(self,other):
    al=1
    r=randroll()
    print(f" 🔺🌑 {self.name} used "+colored(" G-Max One Blow","red",attrs=["bold"])+"!")
    self.atktype="Dark"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)                   
def gmaxsnooze(self,other):
    al=1
    r=randroll()
    print(f" 🔺👹 {self.name} used "+colored(" G-Max Snooze","red",attrs=["bold"])+"!")
    self.atktype="Dark"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)     
    if other.yawn is False and other.status=="Alive":
        other.yawn=True
        print(f" {other.name} became drowsy!")
def maxdarkness(self,other):
    al=1
    r=randroll()
    print(f" 🔺🌑 {self.name} used "+colored(" Max Darkness","magenta",attrs=["bold"])+"!")
    self.atktype="Dark"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)           
    spdefchange(other,self,-0.5)              
                          
def devastatingdrake(self,other):
    al=1
    r=randroll()
    print(f" 🐲💥{self.name} used "+colored(" Devastating Drake","red",attrs=["bold"])+"!")
    self.atktype="Dragon"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,200,a,b,c,r,al)  
def horndrill(self,other):
    self.atktype="Normal"     
    print(f" 😈 {self.name} used "+colored(" Horn Drill","white",attrs=["bold"])+"!")   
    other.hp-=other.hp        
def guillotine(self,other):
    self.atktype="Normal"     
    print(f" ✂️ {self.name} used "+colored(" Guillotine","white",attrs=["bold"])+"!")   
    other.hp-=other.hp        
def fissure(self,other):
    self.atktype="Ground"     
    print(f" 🌍 {self.name} used "+colored(" Fissure","yellow",attrs=["bold"])+"!")   
    other.hp-=other.hp            
def sheercold(self,other):
    self.atktype="Ice"     
    print(f" ❄️ {self.name} used "+colored(" Sheer Cold","cyan",attrs=["bold"])+"!")   
    other.hp-=other.hp
def maxwyrmwind(self,other):
    al=1
    r=randroll()
    print(f" 🔺🐲 {self.name} used "+colored(" Max Wyrmwind","red",attrs=["bold"])+"!")
    self.atktype="Dragon"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)      
    if a!=0:       
        atkchange(other,self,-0.5)
        
def gmaxdepletion(self,other):
    al=1
    r=randroll()
    print(f" 🔺🐲 {self.name} used G-Max Depletion!")
    self.atktype="Dragon"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)             
    if a!=0:
        other.pplist[0]=other.pplist[0]-2
def maxflutterby(self,other):
    al=1
    r=randroll()
    print(f" 🔺🦋 {self.name} used "+colored(" Max Flutterby","green",attrs=["bold"])+"!")
    self.atktype="Bug"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)        
    spatkchange(other,self,-0.5)     
           
def savagespinout(self,other):
    al=1
    r=randroll()
    print(f" 🇿🦋 {self.name} used "+colored(" Savage Spin-Out","green",attrs=["bold"])+"!")
    self.atktype="Bug"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,200,a,b,c,r,al)        
def gmaxresonance(self,other,tr1,turn):
    al=1
    r=randroll()
    print(f" 🔺🎶 {self.name} used "+colored(" G-Max Resonance","cyan",attrs=["bold"])+"!")
    self.atktype="Ice"
    w=weathereff(self,other)
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al,w)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al,w)   
    if tr1.auroraveil is False:
        tr1.auroraturn=turn
        tr1.auroraend(self,other)
        tr1.auroraveil=True  
        print(" 🌈 Aurora Veil made its team stronger against physical and special moves!")            
def subzeroslammer(self,other):
    al=1
    r=randroll()
    print(f" 🇿❄️ {self.name} used "+colored(" Subzero Slammer","cyan",attrs=["bold"])+"!")
    self.atktype="Ice"
    w=weathereff(self,other)
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,200,a,b,c,r,al,w)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,200,a,b,c,r,al,w)    
def gmaxsmite(self,other, turn):
    al=1
    r=randroll()
    print(f" 🔺🧚 {self.name} used "+colored(" G-Max Smite","magenta",attrs=["bold"])+"!")
    self.atktype="Fairy"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)
    confuse(self,other,turn,100)
def maxstarfall(self,other,field,turn):
    al=1
    r=randroll()
    print(f" 🔺⭐ {self.name} used "+colored(" Max Starfall","magenta",attrs=["bold"])+"!")
    self.atktype="Fairy"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)   
    if field.terrain!="Misty":
        field.terrain="Misty" 
        field.misturn=turn
        field.misend(self,other)
        print(" 🌸 Mist swirled around the battlefield!")         
def gmaxfinale(self,other):
    al=1
    r=randroll()
    print(f" 🔺🎂 {self.name} used "+colored(" G-Max Finale","magenta",attrs=["bold"])+"!")
    self.atktype="Fairy"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)      
    if self.hp<self.maxhp:
        self.hp+=round(self.maxhp/6)
        print(f" 🎂 {self.name} had its HP restored!")
        if self.hp>self.maxhp:
            self.hp=self.maxhp
def twinkletackle(self,other):
    al=1
    r=randroll()
    print(f" 🇿🎠 {self.name} used "+colored(" Twinkle Tackle","magenta",attrs=["bold"])+"!")
    self.atktype="Fairy"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,195,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,195,a,b,c,r,al) 
def goalola(self,other):
    print(f" 🇿💂 {self.name} used "+colored(" Guardian of Alola","magenta",attrs=["bold"])+"!")
    self.atktype="Fairy"
    other.hp-=round(other.maxhp*0.75)    
def clangsoul(self,other):    
    print(f" {self.name} used "+colored(" Clangorous Soul","red",attrs=["bold"])+"!")
    print(f" {self.name} got an omniboost!")
    atkchange(self,other,0.5)
    defchange(self,other,0.5)
    spatkchange(self,other,0.5)
    spdefchange(self,other,0.5)
    speedchange(self,other,0.5)
    self.hp-=self.maxhp/4
def clangscale(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Clangorous Scales","red",attrs=["bold"])+"!")
    self.atktype="Dragon"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,110,a,b,c,r,al)       
def soulblaze(self,other):
    al=1
    r=randroll()
    print(f" 🇿🦘 {self.name} used "+colored(" Clangorous Soulblaze","red",attrs=["bold"])+"!")
    self.atktype="Dragon"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,185,a,b,c,r,al)       
    if a!=0:
        print(f" {self.name} got an omniboost!")
        atkchange(self,other,0.5)
        defchange(self,other,0.5)
        spatkchange(self,other,0.5)
        spdefchange(self,other,0.5)
        speedchange(self,other,0.5)
def snuggle(self,other):
    al=1
    r=randroll()
    print(f" 🇿🤗 {self.name} used "+colored(" Let's Snuggle Forever","magenta",attrs=["bold"])+"!")
    self.atktype="Fairy"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,190,a,b,c,r,al)         
def maxknuckle(self,other):
    al=1
    r=randroll()
    print(f" 🔺👊🏿 {self.name} used "+colored(" Max Knuckle","red",attrs=["bold"])+"!")
    self.atktype="Fighting"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)         
    if a!=0:
        atkchange(self,other,0.5)        
        
def gmaxchistrike(self,other):
    al=1
    r=randroll()
    print(f" 🔺👊🏾 {self.name} used "+colored(" G-Max Chi Strike","red",attrs=["bold"])+"!")
    self.atktype="Fighting"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)          
    self.critrate+=1    
def alloutpummeling(self,other):
    al=1
    r=randroll()
    print(f" 🇿👊🏽 {self.name} used "+colored(" All-Out Pummeling","red",attrs=["bold"])+"!")
    self.atktype="Fighting"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,200,a,b,c,r,al)
def maxooze(self,other):
    al=1
    r=randroll()
    print(f" 🔺☠️ {self.name} used "+colored(" Max Ooze","magenta",attrs=["bold"])+"!")
    self.atktype="Poison"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)       
    if a!=0  :
        spatkchange(self,other,0.5)      
        
def aciddownpour(self,other):
    al=1
    r=randroll()
    print(f" 🇿☣️ {self.name} used "+colored(" Acid Downpour","magenta",attrs=["bold"])+"!")
    self.atktype="Poison"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,200,a,b,c,r,al)         
def gmaxmalodor(self,other):
    al=1
    r=randroll()
    print(f" 🛳️☣️ {self.name} used "+colored(" G-Max Malodor","magenta",attrs=["bold"])+"!")
    self.atktype="Poison"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)        
    if other.status=="Alive":
        poison(self,other,100)
           
                 
def supersonicskystrike(self,other):
    al=1
    r=randroll()
    print(f" 🇿✈️ {self.name} used "+colored(" Supersonic Skystrike","cyan",attrs=["bold"])+"!")
    self.atktype="Flying"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,200,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,200,a,b,c,r,al)
def maxairstream(self,other):
    al=1
    r=randroll()
    print(f" 🔺🌪️ {self.name} used "+colored(" Max Airstream","cyan",attrs=["bold"])+"!")
    self.atktype="Flying"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)    
    speedchange(self,other,0.5)             
              
def gmaxwindrage(self,other,optr):
    al=1
    r=randroll()
    print(f" 🔺🌪️ {self.name} used "+colored(" G-Max Wind Rage","cyan",attrs=["bold"])+"!")
    self.atktype="Flying"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)      
    optr.lightscreen=False
    optr.reflect=False
             
def trickroomm(self,other,turn):
    print(f" 🔳 {self.name} used "+colored(" Trick Room","magenta",attrs=["bold"])+"!")       
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
        print(f" {self.name}'s {self.ability}.")
    print(f" 🎱 {self.name} used "+colored(" Shadow Ball","magenta",attrs=["bold"])+"!")
    self.atktype="Ghost"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,80,a,b,c,r,al)  
    chance=20
    if self.ability=="Serene Grace":
        chance*=2
    if self.speed>other.speed:
        ch=random.randint(1,100)            
        if ch>(100-chance) and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"] and a!=0:
            spdefchange(other,self,-0.5)
            
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
    print(f" 🎇{typ} {self.name} used "+colored(" Judgement",f"{color}",attrs=["bold"])+"!")
    w=weathereff(self,other)
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,100,a,b,c,r,al,w)          
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
    print(f" 💽{typ} {self.name} used "+colored(" Multi-Attack",f"{color}",attrs=["bold"])+"!")
    w=weathereff(self,other)
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,90,a,b,c,r,al,w)              
def seedflare (self,other):
    al=1
    r=randroll()
    print(f" 🌸 {self.name} used "+colored(" Seed Flare","green",attrs=["bold"])+"!")
    self.atktype="Grass"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,120,a,b,c,r,al)  
    ch=random.randint(1,100)
    if ch>60 and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        spdefchange(other,self,-1)
def powertrip(self,other):   
    atkx=(self.atkb-1)*2
    spatkx=(self.spatkb-1)*2
    defx=(self.defb-1)*2
    spdefx=(self.spdefb-1)*2
    speedx=(self.speedb-1)*2
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Power Trip","red",attrs=["bold"])+"!")
    self.atktype="Dark"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=20*(1+atkx+defx+spatkx+spdefx+speedx)
    if base<0:
        base=20
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)          
def storedpower(self,other):   
    atkx=(self.atkb-1)*2
    spatkx=(self.spatkb-1)*2
    defx=(self.defb-1)*2
    spdefx=(self.spdefb-1)*2
    speedx=(self.speedb-1)*2
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Stored Power","magenta",attrs=["bold"])+"!")
    self.atktype="Psychic"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=20*(1+atkx+defx+spatkx+spdefx+speedx)
    if base<0:
        base=20
    other.hp-=special(self,self.level,self.spatk,other.spdef,base,a,b,c,r,al)  
def hex(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Hex","magenta",attrs=["bold"])+"!")
    self.atktype="Ghost"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=65
    if other.status!="Alive":
        base*=2
    other.hp-=special(self,self.level,self.spatk,other.spdef,base,a,b,c,r,al)  
    
def infernalparade(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Infernal Parade","magenta",attrs=["bold"])+"!")
    self.atktype="Ghost"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=65
    if other.status!="Alive":
        base*=2
    other.hp-=special(self,self.level,self.spatk,other.spdef,base,a,b,c,r,al)      
    burn(self,other,30)
        
     
def energyball (self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" ⚜️ {self.name}'s {self.ability}.")
    print(f" {self.name} used "+colored(" Energy Ball","green",attrs=["bold"])+"!")
    self.atktype="Grass"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,80,a,b,c,r,al)  
    ch=random.randint(1,10)
    if ch==7 and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil","Shield Dust"]:
        spdefchange(other,self,-0.5)
def pollenpuff(self,other):
    al=1
    r=randroll()
    print(f" 🍯 {self.name} used "+colored(" Pollen Puff","green",attrs=["bold"])+"!")
    self.atktype="Bug"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=special(self,self.level,self.spatk,other.spdef,90,a,b,c,r,al)    
    self.hp+=dmg/3
    other.hp-=dmg
         
def bugbuzz (self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" ⚜️ {self.name}'s {self.ability}.")
    print(f" 🪰 {self.name} used "+colored(" Bug Buzz","green",attrs=["bold"])+"!")
    self.atktype="Bug"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,90,a,b,c,r,al)  
    ch=random.randint(1,10)
    if ch==7 and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        spdefchange(other,self,-0.5)
                
def snipeshot (self,other):
    al=1
    r=randroll()
    w=weathereff(self,other)
    print(f" {self.name} used "+colored(" Snipe Shot","blue",attrs=["bold"])+"!")
    self.atktype="Water"
    c=isCrit(self,other,4)
    if self.ability=="Mega Launcher":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,70,a,b,c,r,al,w)                   
def signalbeam (self,other,turn):
    al=1
    r=randroll()
    print(f" 🚦 {self.name} used "+colored(" Signal Beam","green",attrs=["bold"])+"!")
    self.atktype="Bug"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,75,a,b,c,r,al)  
    confuse(self,other,turn,10)
    
def aeroblast (self,other):
    al=1
    r=randroll()
    print(f" ☄️ {self.name} used "+colored(" Aeroblast","cyan",attrs=["bold"])+"!")
    self.atktype="Flying"
    c=isCrit(self,other,2)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,100,a,b,c,r,al)        
    
def makeitrain(self,other):
    al=1
    r=randroll()
    print(f" 🪙 {self.name} used "+colored(" Make It Rain","yellow",attrs=["bold"])+"!")
    self.atktype="Steel"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,120,a,b,c,r,al)           
    spatkchange(self,self,-0.5)
    
def leafstorm(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Leaf Storm","green",attrs=["bold"])+"!")
    self.atktype="Grass"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,130,a,b,c,r,al)           
    if a!=0:
        spatkchange(self,self,-1)
           
def blizzard(self,other):
    self.atktype="Ice"
    w=weathereff(self,other)
    al=1
    r=randroll()
    print(f" ❄️ {self.name} used "+colored(" Blizzard","cyan",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,110,a,b,c,r,al,w)    
    ch=random.randint(1,10)
    if ch==1 and other.status is None and self.ability!="Sheer Force" and other.ability not in ["Shield Dust"] and other.item!="Covert Cloak":
        other.status=random.choice(["Frozen","Frostbite"])
        print(f" ❄️ {other.name} was frozen.")
        
def boomburst(self,other):
    al=1
    r=randroll()
    print(f" 🔊 {self.name} used "+colored(" Boomburst","white",attrs=["bold"])+"!")
    self.atktype="Normal"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,140,a,b,c,r,al)        
def sonicslash(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Sonic Slash","cyan",attrs=["bold"])+"!")
    self.atktype="Flying"
    c=isCrit(self,other)
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
    other.hp-=special(self,self.level,self.spatk,other.spdef,base,a,b,c,r,al) 
       
def airslash(self,other):
    al=1
    r=randroll()
    print(f" 🌀 {self.name} used "+colored(" Air Slash","cyan",attrs=["bold"])+"!")
    self.atktype="Flying"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,75,a,b,c,r,al)     
    flinch(self,other,30)

def aircutter(self,other):
    al=1
    r=randroll()
    print(f" 🌀 {self.name} used "+colored(" Air Cutter","cyan",attrs=["bold"])+"!")
    self.atktype="Flying"
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}!")
        al*=1.5
    c=isCrit(self,other,2)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,60,a,b,c,r,al)

def aerialace(self,other):
    al=1
    r=randroll()
    print(f" 🪶 {self.name} used "+colored(" Aerial Ace","cyan",attrs=["bold"])+"!")
    self.atktype="Flying"
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}!")
        al*=1.5
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,60,a,b,c,r,al)        
    
def leaftornado(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Leaf Tornado","green",attrs=["bold"])+"!")
    self.atktype="Grass"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,130,a,b,c,r,al)             
       
def psystrike(self,other):
    al=1
    r=randroll()
    print(f" 👁️ {self.name} used "+colored(" Psystrike","magenta",attrs=["bold"])+"!")
    self.atktype="Psychic"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.defense,100,a,b,c,r,al)             
def sacredfire(self,other):
    self.atktype="Fire"
    al=1
    r=randroll()
    print(f" 🎇 {self.name} used "+colored(" Sacred Fire","red",attrs=["bold"])+"!")
    w=weathereff(self,other)
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,110,a,b,c,r,al,w)  
def aurasphere(self,other):
    al=1
    r=randroll()
    if "World Champion Ash" not in self.owner.name:
        print(f" 🌀 {self.name} used "+colored(" Aura Sphere","blue",attrs=["bold"])+"!")
    if "World Champion Ash" in self.owner.name:
        print(f" 🌀 {self.name} used "+colored(" Giant Aura Sphere","blue",attrs=["bold"])+"!")
        al*=1.3
    self.atktype="Fighting"
    c=isCrit(self,other)
    if self.ability=="Mega Launcher":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,80,a,b,c,r,al)      
    
def heatwave(self,other):
    self.atktype="Fire"
    al=1
    w=weathereff(self,other)
    r=randroll()
    print(f" 🔥 {self.name} used "+colored(" Heat Wave","red",attrs=["bold"])+"!")    
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,100,a,b,c,r,al,w)     
    burn(self,other,10)  
    
def bleakwindstorm(self,other):
    al=1
    w=weathereff(self,other)
    r=randroll()
    print(f" 🌪️❄️ {self.name} used "+colored(" Bleakwind Storm","cyan",attrs=["bold"])+"!")
    self.atktype="Flying"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,95,a,b,c,r,al,w)   
    ch=random.randint(1,100)
    if ch>90 and other.status=="Alive":
        other.status=random.choice(["Frozen","Frostbite"])
        print(f" ❄️ {other.name} was frozen.")
def springtidestorm(self,other):
    al=1
    w=weathereff(self,other)
    r=randroll()
    print(f" 🌸 {self.name} used "+colored(" Springtide Storm","magenta",attrs=["bold"])+"!")
    self.atktype="Fairy"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,95,a,b,c,r,al,w)               
def sandsearstorm(self,other):
    al=1
    w=weathereff(self,other)
    r=randroll()
    print(f" {self.name} used "+colored(" Sandsear Storm","yellow",attrs=["bold"])+"!")
    self.atktype="Ground"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,95,a,b,c,r,al,w)       
    burn(self,other,10)                  
def wildboltstorm(self,other):
    al=1
    w=weathereff(self,other)
    r=randroll()
    print(f" 🌩️ {self.name} used "+colored(" Wildbolt Storm","yellow",attrs=["bold"])+"!")
    self.atktype="Electric"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,95,a,b,c,r,al,w)        
    paralyzed(self,other,10)
def morningsun(self,other):
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
def shoreup(self,other):
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
def moonlight(self,other):
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
def synthesis(self,other):
    print(f" 🌻 {self.name} used "+colored(" Synthesis","green",attrs=["bold"])+"!")
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
def lunarblessing(self,other):
    self.atktype="Psychic"
    print(f" 🌙 {self.name} used "+colored(" Lunar Blessing","magenta",attrs=["bold"])+"!")   
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
def junglehealing(self,other):
    self.atktype="Normal"
    print(f" 🌿 {self.name} used "+colored(" Jungle Healing","green",attrs=["bold"])+"!")             
    self.status="Alive"
    if self.hp>=(self.maxhp/2):
        self.hp=self.maxhp
    elif self.hp==self.maxhp:
        print(" Already at full HP.")
    else:
        self.hp+=(self.maxhp/2)
        if self.hp>self.maxhp:
            self.hp=self.maxhp            
def recover(self,other):
    self.atktype="Normal"
    print(f" ❤️‍🩹 {self.name} used "+colored(" Recover","white",attrs=["bold"])+"!")             
    if self.hp>=(self.maxhp/2):
        self.hp=self.maxhp
    elif self.hp==self.maxhp:
        print(" Already at full HP.")
    else:
        self.hp+=(self.maxhp/2)
        if self.hp>self.maxhp:
            self.hp=self.maxhp
def milkdrink(self,other):
    self.atktype="Normal"
    print(f" 🥛 {self.name} used "+colored(" Milk Drink","white",attrs=["bold"])+"!")            
    if self.hp>=(self.maxhp/2):
        self.hp=self.maxhp
    elif self.hp==self.maxhp:
        print(" Already at full HP.")
    else:
        self.hp+=(self.maxhp/2)
        if self.hp>self.maxhp:
            self.hp=self.maxhp            
def roost(self,other):
    self.atktype="Flying"
    print(f" 🦉 {self.name} used "+colored(" Roost","cyan",attrs=["bold"])+"!")           
    if self.hp>=(self.maxhp/2):
        self.hp=self.maxhp
    elif self.hp==self.maxhp:
        print(" Already at full HP.")
    else:
        self.hp+=(self.maxhp/2)     
        if self.teratype=="Flying":
            self.roost="TR"
            self.teratype="None"
        if self.type2=="Flying":
            self.roost="T2"
            self.type2="None"
        if self.type1=="Flying":
            self.roost="T1"
            self.type1="None"
def slackoff(self,other):
    self.atktype="Normal"
    print(f" 🦥 {self.name} used "+colored(" Slack Off","white",attrs=["bold"])+"!")             
    if self.hp>=(self.maxhp/2):
        self.hp=self.maxhp
    elif self.hp==self.maxhp:
        print(" Already at full HP.")
    else:
        self.hp+=(self.maxhp/2)             
def softboiled(self,other):
    self.atktype="Normal"
    print(f" 🥚 {self.name} used "+colored(" Softboiled","white",attrs=["bold"])+"!")          
    if self.hp>=(self.maxhp/2):
        self.hp=self.maxhp
    elif self.hp==self.maxhp:
        print(" Already at full HP.")
    else:
        self.hp+=(self.maxhp/2)      
def toxic(self, other):
    self.atktype="Poison"
    print(f" {self.name} used "+colored(" Toxic","magenta",attrs=["bold"])+"!")       
    if other.status=="Alive":
        poison(self,other,100)
    else:
        print(" It failed.")
def willowisp(self, other):
    self.atktype="Fire"
    print(f" {self.name} used "+colored(" Will-O-Wisp","red",attrs=["bold"])+"!")         
    burn(self,other,100)
    if other.ability=="Flash Fire":
        print(f" 🔥 {other.name}'s {other.ability}.")
        other.flashfire=True
    
    
def healorder(self,other):
    print(f" {self.name} used "+colored(" Heal Order","green",attrs=["bold"])+"!")   
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
        print(f" ⚜️ {self.name}'s {self.ability}.")
    print(f" {self.name} used "+colored(" Thunderbolt","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,90,a,b,c,r,al) 
    paralyzed(self,other,10)
def thundercage(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Thunder Cage","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,80,a,b,c,r,al)        
    if other.olock is False:
        other.olock=True 
def nuzzle(self,other):
    al=1
    r=randroll()
    print(f" ⚡ {self.name} used "+colored(" Nuzzle","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,20,a,b,c,r,al)        
    if other.status=="Alive" and a!=0:
        paralyzed(self,other,100)
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
    print(f" {self.name} used "+colored(" Techno Blast",f"{color}",attrs=["bold"])+"!")
    w=weathereff(self,other)
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,120,a,b,c,r,al,w)            
def focusblast(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" ⚜️ {self.name}'s {self.ability}.")
    print(f" 🔴 {self.name} used "+colored("Focus Blast","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,120,a,b,c,r,al)        
    ch=random.randint(1,10)
    if ch==7 and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil","Shield Dust"] and a!=0 and self.ability!="Sheer Force":
        spdefchange(other,self,-0.5)
        
def thunder(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" ⚜️ {self.name}'s {self.ability}.")
    print(f" 🌩️ {self.name} used "+colored(" Thunder","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,110,a,b,c,r,al)   
    paralyzed(self,other,30)
def finalgambit(self,other):
    print(f" 💀 {self.name} used "+colored(" Final Gambit","red",attrs=["bold"])+"!")       
    if "Ghost" not in (other.type1, other.type2,other.teratype):
        other.hp-=self.hp
        self.hp-=self.hp
def venoshock(self,other):
    al=1
    r=randroll()
    print(f" ☣️ {self.name} used "+colored(" Venoshock","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Poison"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=65
    if other.status in ["Poisoned","Badly Poisoned"]:
        base*=2
    other.hp-=special(self,self.level,self.spatk,other.spdef,base,a,b,c,r,al)     
def fishiousrend(self,other):
    al=1
    r=randroll()
    print(f" 🦈 {self.name} used "+colored(" Fishious Rend","blue",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Water"
    w=weathereff(self,other)
    if self.ability=="Strong Jaw":
        print(f" 🦈 {self.name}'s {self.ability}!")
        al=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=85
    if self.speed>other.speed:
        base*=2
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al,w)      
def blazingtorque(self,other):
    al=1
    r=randroll()
    w=weathereff(self,other)
    print(f" 🏎️ {self.name} used "+colored(" Blazing Torque","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Fire"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    other.hp-=physical(self,self.level,self.atk,other.defense,100,a,b,c,r,al,w) 
def combattorque(self,other):
    al=1
    r=randroll()
    w=weathereff(self,other)
    print(f" 🏎️ {self.name} used "+colored(" Combat Torque","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    other.hp-=physical(self,self.level,self.atk,other.defense,100,a,b,c,r,al,w)       
def magicaltorque(self,other):
    al=1
    r=randroll()
    w=weathereff(self,other)
    print(f" 🏎️ {self.name} used "+colored(" Magical Torque","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Fairy"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    other.hp-=physical(self,self.level,self.atk,other.defense,100,a,b,c,r,al,w)      
def noxioustorque(self,other):
    al=1
    r=randroll()
    w=weathereff(self,other)
    print(f" 🏎️ {self.name} used "+colored(" Noxious Torque","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Poison"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    other.hp-=physical(self,self.level,self.atk,other.defense,100,a,b,c,r,al,w)     
def wickedtorque(self,other):
    al=1
    r=randroll()
    w=weathereff(self,other)
    print(f" 🏎️ {self.name} used "+colored(" Wicked Torque","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Dark"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    other.hp-=physical(self,self.level,self.atk,other.defense,100,a,b,c,r,al,w)             
def boltbeak(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Bolt Beak","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=85
    if self.speed>other.speed:
        base*=2
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)              
def electroball(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Electro Ball","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=30*(self.speed/other.speed)
    if base<30:
        base=30
    other.hp-=special(self,self.level,self.spatk,other.spdef,base,a,b,c,r,al)              
def electroweb(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Electroweb","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=65
    other.hp-=special(self,self.level,self.spatk,other.spdef,base,a,b,c,r,al)        
    if other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil","Shield Dust"] and a!=0:
        speedchange(other,self,-0.5)
        
def powergem(self,other):
    al=1
    r=randroll()
    print(f" 🪨 {self.name} used "+colored(" Power Gem","yellow",attrs=["bold"])+"!")   
    c=isCrit(self,other)
    self.atktype="Rock"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,80,a,b,c,r,al)            
def zapcannon(self,other):
    al=1
    r=randroll()
    if self.ability=="Mega Launcher":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    if self.ability=="Sheer Force":
        al=1.5
        print(f" ⚜️ {self.name}'s {self.ability}.")
    print(f" {self.name} used "+colored(" Zap Cannon","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al)            
    paralyzed(self,other,100)
def freezedry(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Freeze-Dry","cyan",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Ice"
    w=weathereff(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    other.hp-=special(self,self.level,self.spatk,other.spdef,70,a,b,c,r,al,w) 
def saltcure(self,other):
    al=1
    r=randroll()
    print(f" 🧂 {self.name} used "+colored(" Salt Cure","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Rock"
    w=weathereff(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    other.hp-=special(self,self.level,self.spatk,other.spdef,40,a,b,c,r,al,w)    
    if other.salty==False:
        print(f" {other.name} is being salt cured!")
        other.salty=True
def shellsidearm(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    print(f" 🐚 {self.name} used "+colored(" Shell Side Arm","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Poison"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if other.spdef>other.defense:
        other.hp-=physical(self,self.level,self.atk,other.defense,90,a,b,c,r,al)
    if other.defense>other.spdef: 
        other.hp-=special(self,self.level,self.spatk,other.spdef,90,a,b,c,r,al)
    poison(self,other,20)           
def poisonjab(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" ⚜️ {self.name}'s {self.ability}.")
    print(f" {self.name} used "+colored(" Poison Jab","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Poison"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,90,a,b,c,r,al) 
    poison(self,other,30)
def drillpeck(self,other):
    al=1
    r=randroll()
    print(f" 🐔 {self.name} used "+colored(" Drill Peck","cyan",attrs=["bold"])+"!")
    c=isCrit(self,other,2)
    self.atktype="Flying"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,80,a,b,c,r,al)        
def leafblade(self,other):
    al=1
    r=randroll()
    print(f" 🌿 {self.name} used "+colored(" Leaf Blade","green",attrs=["bold"])+"!")
    if self.ability=="Sharpness":
        al*=1.5
    c=isCrit(self,other,2)
    self.atktype="Grass"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,90,a,b,c,r,al)    
def triplearrows(self,other):
    al=1
    r=randroll()
    print(f" 🏹 {self.name} used "+colored(" Triple Arrows","red",attrs=["bold"])+"!")
    c=isCrit(self,other,2)
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,50,a,b,c,r,al)
    ch=random.randint(1,100)
    if 95>ch>90 and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        defchange(other,self,-0.5)
        
    flinch(self,other,5)  
def razorleaf(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Razor Leaf","green",attrs=["bold"])+"!")
    c=isCrit(self,other,2)
    self.atktype="Grass"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    other.hp-=physical(self,self.level,self.atk,other.defense,70,a,b,c,r,al)        
def gyroball(self,other):
    al=1
    r=randroll()
    print(f" 🏐 {self.name} used "+colored(" Gyro Ball","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Steel"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=round(1+25*(other.speed/self.speed))
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)   
def overdrive(self,other):
    al=1
    r=randroll()
    print(f" 🎸 {self.name} used "+colored(" Overdrive","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=special(self,self.level,self.spatk,other.spdef,80,a,b,c,r,al)         
    other.hp-=dmg
def discharge(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Disharge","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=special(self,self.level,self.spatk,other.spdef,80,a,b,c,r,al) 
    other.hp-=dmg    
    paralyzed(self,other,30)
def doubleshock(self,other):
    al=1
    r=randroll()
    print(f" ⚡ {self.name} used "+colored(" Double Shock","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical(self,self.level,self.atk,other.defense,120,a,b,c,r,al)        
    other.hp-=dmg
    if self.type2==None and self.type1=="Electric":
        self.type1=None
    if self.type2!=None and self.type1=="Electric":
        self.type1=self.type2
        self.type2=None
def wildcharge(self,other):
    al=1
    r=randroll()
    print(f" ⚡ {self.name} used "+colored(" Wild Charge","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical(self,self.level,self.atk,other.defense,90,a,b,c,r,al) 
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
    print(f" 🪨 {self.name} used "+colored(" Accelerock","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Rock"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,40,a,b,c,r,al)     
def secretsword(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Secret Sword","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Fighting"
    if self.ability=="Sharpness":
        al*=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.defense,85,a,b,c,r,al)          
def sacredsword(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Sacred Sword","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Fighting"
    if self.ability=="Sharpness":
        al*=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.maxdef,90,a,b,c,r,al)         
def throatchop(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Throat Chop","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Dark"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,80,a,b,c,r,al)           
def darkestlariat(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Darkest Lariat","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Dark"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.maxdef,85,a,b,c,r,al)       
def acrobatics(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Acrobatics","cyan",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Flying"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=55
    if self.item=="None" or "Used" in self.item:
        base*=2
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)     
def aurawheel(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Aura Wheel","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Electric"
    if "Hungry" in self.name:
        self.atktype="Dark"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,110,a,b,c,r,al)            
def barbbarrage(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Barb Barrage","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Poison"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=60
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    if other.status!="Alive":
        base*=2
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)      
    if a!=0:
        poison(self,other,30)   
def beakblast(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Beak Blast","cyan",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Flying"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,100,a,b,c,r,al)     
def partingshot(self,other):
    print(f" {self.name} used Parting Shot.")
    atkchange(other,self,-0.5)
    spatkchange(other,self,-0.5)
def shadowbone(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Shadow Bone","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Ghost"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.ability=="Bone Zone":
        if a==0:
            a=1
        if 0<a<1:
            a=2
    other.hp-=physical(self,self.level,self.atk,other.defense,85,a,b,c,r,al)       
    ch=random.randint(1,100)
    if ch>80 and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        defchange(other,self,-0.5)
         
def bonerush(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Bone Rush","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Ground"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.ability=="Bone Zone":
        if a==0:
            a=1
        if 0<a<1:
            a=2
    other.hp-=physical(self,self.level,self.atk,other.defense,25,a,b,c,r,al)  
def mistyexplosion(self,other):
    al=1
    r=randroll()
    print(f" 🌸💥 {self.name} used "+colored(" Misty Explosion","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    if self.ability=="Reckless":
        al*=1.2  
    self.atktype="Fairy"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=100
    if field.terrain=="Misty":
        base*=1.5
    if other.protect==False:
        other.hp-=special(self,self.level,self.spatk,other.spdef,base,a,b,c,r,al)         
    self.hp=0     
def explosion(self,other):
    al=1
    r=randroll()
    print(f" 💥 {self.name} used "+colored(" Explosion","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    if self.ability=="Reckless":
        al*=1.2  
    self.atktype="Normal"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if other.protect==False:
        other.hp-=physical(self,self.level,self.atk,(other.defense/2),150,a,b,c,r,al)         
    self.hp=0     
def snarl(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Snarl","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Dark"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,65,a,b,c,r,al)           
    if other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        spatkchange(other,self,-0.5) 
        
    else:
        print(" Nothing happened!")
def steelbeam(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Steel Beam","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Steel"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=special(self,self.level,self.spatk,other.spdef,140,a,b,c,r,al)       
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
    print(f" {self.name} used "+colored(" Aqua Jet","blue",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Water"
    w=weathereff(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=40
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al,w)   
def jetpunch(self,other):
    al=1
    r=randroll()
    print(f" 🐬 {self.name} used "+colored(" Jet Punch","blue",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Water"
    w=weathereff(self,other)
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
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al,w)                      
def armthrust(self,other):
    al=1
    r=randroll()
    print(f" ✋🏻 {self.name} used "+colored(" Arm Thrust","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Fighting"
    base=25
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)    
def psyshield(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Psyshield Bash","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Psychic"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,70,a,b,c,r,al)  
    ch=random.randint(1,100)
    if ch>50:
        defchange(self,other,0.5)
        
def steelwing(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Steel Wing","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Steel"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,70,a,b,c,r,al)  
    ch=random.randint(1,10)
    if ch==7:
        defchange(self,other,0.5)
        
def heatcrash(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Heat Crash","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Fire"
    w=weathereff(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=80
    if self.defense>self.spdef:
        base*=(self.defense/other.defense)
    if self.spdef>self.defense:
        base*=(self.spdef/other.spdef)
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al,w)         
def grassknot(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Grass Knot","green",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Grass"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=0
    x=other.weight
    if other.ability=="Light Metal":
        x*=0.5
    if other.ability=="Heavy Metal":
        x*=2
    if 0.1<=x<=21.8:
        base=20
    if 21.9<=x<=54.9:
        base=40
    if 55.1<=x<=110:
        base=60
    if 110.2<=x<=220.2:
        base=80
    if 220.4<=x<=440.7:
        base=100
    if x>=440.9:
        base=120
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)             
def heavyslam(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Heavy Slam","white",attrs=["bold"])+"!")
    if other.dmax==False:
        c=isCrit(self,other)
        self.atktype="Steel"
        y=1
        if self.ability=="Light Metal":
            print(f" {self.name}'s {self.ability}!")
            y*=0.5
        if self.ability=="Heavy Metal":
            print(f" {self.name}'s {self.ability}!")
            y*=2
        ab=weakness(self,other,field)
        a=ab[0]
        b=ab[1]   
        base=0
        x=(other.weight/(self.weight*y))*100
        if x>50:
            base=40
        if 50>=x>=33.35:
            base=60
        if 33.34>=x>=25.01:
            base=80
        if 25>x>=20.01:
            base=100
        if 20>x:
            base=120
        other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)  
    else:
        print(" It failed.")         
def payback(self,other):
    al=1
    r=randroll()
    print(f" 😤 {self.name} used "+colored(" Payback","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Dark"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=50
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    if self.speed<other.speed:
        base*=2
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)           
def assurance(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Assurance","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Dark"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=60
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    if self.speed<other.speed:
        base*=2
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)                   
def attackorder(self,other):
    al=1
    r=randroll()
    print(f" 🐝 {self.name} used "+colored(" Attack Order","green",attrs=["bold"])+"!")
    c=isCrit(self,other,2)
    self.atktype="Bug"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,120,a,b,c,r,al)             
def facade(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Facade","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Normal"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=70
    if self.status!="Alive":
        base*=2
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)                 
def retrn(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Return","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Normal"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=round(self.happiness*(2/5))
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)
def bodypress(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Body Press","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.defense,other.defense,80,a,b,c,r,al)    
    
def stoneedge(self,other):
    al=1
    r=randroll()
    
    print(f" {self.name} used "+colored(" Stone Edge","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other,2)
    self.atktype="Rock"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,90,a,b,c,r,al)   
def stoneaxe(self,other,optr):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Stone Axe","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other,2)
    self.atktype="Rock"
    if self.ability=="Sharpness":
        al*=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,65,a,b,c,r,al)     
    if "Stealth Rock" not in optr.hazard:
        print(" 🪨 Pointed stones float in the air around the opposing team!")
        optr.hazard.append("Stealth Rock")  
    
def petaldance(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Petal Dance","green",attrs=["bold"])+"!")
    c=isCrit(self,other,2)
    self.atktype="Grass"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,120,a,b,c,r,al) 
    if self.fmove==False:
        self.fmove=True
        self.fmoveturn+=3
       
def petalblizzard(self,other):
    al=1
    r=randroll()
    print(f" 🌸 {self.name} used "+colored(" Petal Blizzard","green",attrs=["bold"])+"!")
    c=isCrit(self,other,2)
    self.atktype="Grass"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,90,a,b,c,r,al)                 
def ragingfury(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Raging Fury","red",attrs=["bold"])+"!")
    c=isCrit(self,other,2)
    self.atktype="Fire"
    w=weathereff(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,90,a,b,c,r,al,w)   
    if self.fmove==False:
        self.fmove=True
        self.fmoveturn+=3
def thrash(self,other):
    al=1
    r=randroll()
    print(f" 💥 {self.name} used "+colored(" Thrash","white",attrs=["bold"])+"!")
    c=isCrit(self,other,2)
    self.atktype="Normal"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,120,a,b,c,r,al)       
    if self.fmove==False:
        self.fmove=True
        self.fmoveturn+=3        
def outrage(self,other):
    al=1
    r=randroll()
    print(f" 🔥 {self.name} used "+colored(" Outrage","red",attrs=["bold"])+"!")
    c=isCrit(self,other,2)
    self.atktype="Dragon"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,90,a,b,c,r,al)       
    if self.fmove==False:
        self.fmove=True
        self.fmoveturn+=3
def aquafang(self,other):
    al=1
    r=randroll()
    self.atktype="Water"
    w=weathereff(self,other)
    print(f" 💦 {self.name} used "+colored(" Aqua Fang","blue",attrs=["bold"])+"!")
    c=isCrit(self,other)
    if self.ability=="Strong Jaw":
        print(f" 🦈 {self.name}'s {self.ability}!")
        al=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,80,a,b,c,r,al,w)          
def icefang(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" ⚜️ {self.name}'s {self.ability}.")
    print(f" ❄️ {self.name} used "+colored(" Ice Fang","cyan",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Ice"
    w=weathereff(self,other)
    if self.ability=="Strong Jaw":
        print(f" 🦈 {self.name}'s {self.ability}!")
        al=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,75,a,b,c,r,al,w)       
    ch=random.randint(1,100)
    if ch>90 and self.ability!="Sheer Force" and other.ability not in ["Shield Dust"] and other.item!="Covert Cloak":
       other.status=random.choice(["Frozen","Frostbite"])
       print(f" ❄️ {other.name} was frozen.")
def rockslide(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" ⚜️ {self.name}'s {self.ability}.")
    print(f" 🪨 {self.name} used "+colored(" Rock Slide","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Rock"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,85,a,b,c,r,al)   
    flinch(self,other,20)  
def waterfall(self,other):
    self.atktype="Water"
    al=1
    w=weathereff(self,other)
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" ⚜️ {self.name}'s {self.ability}.")
    print(f" 🌊 {self.name} used "+colored(" Waterfall","blue",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,85,a,b,c,r,al,w)       
    flinch(self,other,20)    
def crosspoison(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" ⚜️ {self.name}'s {self.ability}.")
    print(f" ❌ {self.name} used "+colored(" Cross Poison","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Poison"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,90,a,b,c,r,al)           
    poison(self,other,10)
def rockblast(self,other):
    al=1
    r=randroll()
    print(f" 🪨 {self.name} used "+colored(" Rock Blast","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Rock"
    base=25
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)         
def skyuppercut(self,other):
    al=1
    r=randroll()
    print(f" 👊 {self.name} used "+colored(" Sky Uppercut","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,70,a,b,c,r,al)         
def shadowforce(self,other):
    if self.item=="Power Herb" or self.precharge==True:
        if self.item=="Power Herb":
            self.item+="[Used]"
            print(f" {self.name} became fully charged due to its Power Herb.")
        al=1
        r=randroll()
        print(f" 👥 {self.name} used "+colored(" Shadow Force","magenta",attrs=["bold"])+"!")
        c=isCrit(self,other)
        self.atktype="Ghost"
        ab=weakness(self,other,field)
        a=ab[0]
        b=ab[1]   
        other.hp-=physical(self,self.level,self.atk,other.defense,120,a,b,c,r,al)   
        self.precharge=False
        flinch(self,other,30)
    elif self.precharge==False:
        print(f" 😶‍🌫️  {self.name} vanished instantly!")
        self.precharge=True         
    
def phantomforce(self,other):
    if self.item=="Power Herb" or self.precharge==True:
        if self.item=="Power Herb":
            self.item+="[Used]"
            print(f" {self.name} became fully charged due to its Power Herb.")
        al=1
        r=randroll()
        print(f" 👤 {self.name} used "+colored(" Phantom Force","magenta",attrs=["bold"])+"!")
        c=isCrit(self,other)
        self.atktype="Ghost"
        ab=weakness(self,other,field)
        a=ab[0]
        b=ab[1]   
        other.hp-=physical(self,self.level,self.atk,other.defense,90,a,b,c,r,al)      
        self.precharge=False  
    elif self.precharge==False:
        print(f" 😶‍🌫️ {self.name} vanished instantly!")
        self.precharge=True
def blazekick(self,other):
    al=1
    r=randroll()
    print(f" 🔥 {self.name} used "+colored(" Blaze Kick","red",attrs=["bold"])+"!")
    if self.ability=="Striker":
        print(f" {self.name}'s {self.ability}!")
        al=1.3
    c=isCrit(self,other)
    self.atktype="Fire"
    w=weathereff(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,85,a,b,c,r,al,w)       
def axekick(self,other,turn):
    al=1
    r=randroll()
    print(f" 🪓 {self.name} used "+colored(" Axe Kick","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    if self.ability=="Striker":
        print(f" {self.name}'s {self.ability}!")
        al=1.3
    if self.ability=="Reckless":
        al*=1.2
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical(self,self.level,self.atk,other.defense,120,a,1,b,c,r,al)
    other.hp-=dmg
def lowkick(self,other):
    al=1
    r=randroll()
    print(f" 🦶 {self.name} used "+colored(" Low Kick","red",attrs=["bold"])+"!")
    if self.ability=="Striker":
        print(f" {self.name}'s {self.ability}!")
        al=1.3
    c=isCrit(self,other)
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=0
    x=other.weight
    if other.ability=="Light Metal":
        x*=0.5
    if other.ability=="Heavy Metal":
        x*=2
    if 0.1<=x<=21.8:
        base=20
    if 21.9<=x<=54.9:
        base=40
    if 55.1<=x<=110:
        base=60
    if 110.2<=x<=220.2:
        base=80
    if 220.4<=x<=440.7:
        base=100
    if x>=440.9:
        base=120
    dmg=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)
    other.hp-=dmg
def hijumpkick(self,other):
    al=1
    r=randroll()
    print(f" 🦶 {self.name} used "+colored(" High Jump Kick","red",attrs=["bold"])+"!")
    if self.ability=="Striker":
        print(f" {self.name}'s {self.ability}!")
        al=1.3
    c=isCrit(self,other)
    if self.ability=="Reckless":
        al*=1.2
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical(self,self.level,self.atk,other.defense,130,a,b,c,r,al)
    other.hp-=dmg
def foulplay(self,other):
    al=1
    r=randroll()
    print(f" 💥 {self.name} used "+colored(" Foul Play","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Dark"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,other.atk,other.defense,80,a,b,c,r,al)      
def bulletseed(self,other):
    al=1
    r=randroll()
    print(f" 🟢 {self.name} used "+colored(" Bullet Seed","green",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Grass"
    w=weathereff(self,other)
    base=25
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al,w)      
def iciclespears(self,other):
    al=1
    r=randroll()
    print(f" ❄️ {self.name} used "+colored(" Icicle Spear","cyan",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Ice"
    w=weathereff(self,other)
    base=25
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al,w)       
def pinmissile (self,other):
    al=1
    r=randroll()
    print(f" 🧨 {self.name} used "+colored(" Pin Missile","green",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Bug"
    base=25
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)   
def populationbomb(self,other):
    al=1
    r=randroll()
    print(f" 💣 {self.name} used "+colored(" Population Bomb","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Normal"
    base=20
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)      
def twinbeam(self,other):
    al=1
    r=randroll()
    print(f" 🦒 {self.name} used "+colored(" Twin Beam","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Psychic"
    base=40
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,base,a,b,c,r,al)    
def geargrind(self,other):
    al=1
    r=randroll()
    print(f" ⚙️ {self.name} used "+colored(" Gear Grind","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Steel"
    base=50
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)    
def tripledive(self,other):
    al=1
    r=randroll()
    w=weathereff(self,other)
    print(f" 🤿 {self.name} used "+colored(" Triple Dive","blue",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Water"
    base=30
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al,w)  
          
def ironbash(self,other):
    al=1
    r=randroll()
    print(f" 💥 {self.name} used "+colored(" Double Iron Bash","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Steel"
    base=60
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)     
    flinch(self,other,30) 
def watershuriken(self,other):
    al=1
    r=randroll()
    print(f" 🥷 {self.name} used "+colored(" Water Shuriken","blue",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Water"
    base=15
    if "Ash" in self.name:
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)           
def brickbreak(self,other,optr):
    al=1
    r=randroll()
    print(f" 🧱 {self.name} used "+colored(" Brick Break","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,80,a,b,c,r,al)       
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
    print(f" {self.name} used "+colored(" Megahorn","green",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Bug"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,120,a,b,c,r,al) 
def aurorabeam(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" ⚜️ {self.name}'s {self.ability}.")
    if self.ability=="Technician":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    print(f" 🌈 {self.name} used "+colored(" Aurora Beam","cyan",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Ice"
    w=weathereff(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,65,a,b,c,r,al,w)          
    ch=random.randint(1,100)   
    if ch<=30:
        atkchange(other,self,-0.5)
def icebeam(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" ⚜️ {self.name}'s {self.ability}.")
    print(f" ❄️ {self.name} used "+colored(" Ice Beam","cyan",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Ice"
    w=weathereff(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,90,a,b,c,r,al,w)
    ch=random.randint(1,10)
    if ch==7 and other.status=="Alive" and other.ability not in ["Shield Dust"] and other.item!="Covert Cloak":
        other.status=random.choice(["Frozen","Frostbite"])
        print(f" ❄️ {other.name} was frozen.")
def glaciate(self,other):
    al=1
    r=randroll()
    print(f" ❄️ {self.name} used "+colored(" Glaciate","cyan",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Ice"
    w=weathereff(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,65,a,b,c,r,al,w)
    speedchange(other,self,-0.5)
    
def flowertrick(self,other):
    al=1
    r=randroll()
    print(f" 💐 {self.name} used "+colored(" Flower Trick","green",attrs=["bold"])+"!")
    c=isCrit(self,other,16)
    self.atktype="Grass"
    w=weathereff(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=65
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al,w)            
def frostbreath(self,other):
    al=1
    r=randroll()
    print(f" ❄️ {self.name} used "+colored(" Frost Breath","cyan",attrs=["bold"])+"!")
    c=isCrit(self,other,16)
    self.atktype="Ice"
    w=weathereff(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=65
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    other.hp-=special(self,self.level,self.spatk,other.spdef,base,a,b,c,r,al,w)    
def psyshock(self,other):
    al=1
    r=randroll()
    print(f" 💥 {self.name} used "+colored(" Psyshock","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Psychic"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.defense,80,a,b,c,r,al)      
def darkhole(self,other,turn):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" ⚜️ {self.name}'s {self.ability}.")
    print(f" 🕳️ {self.name} used "+colored(" Dark Hole","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Dark"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,100,a,b,c,r,al)  
    sleep(self,other,40,turn)
        
def darkpulse(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" ⚜️ {self.name}'s {self.ability}.")
    print(f" ⭕ {self.name} used "+colored(" Dark Pulse","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Dark"
    if self.ability=="Mega Launcher":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,80,a,b,c,r,al)  
    flinch(self,other,20) 
def strangesteam(self,other,turn):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" ⚜️ {self.name}'s {self.ability}.")
    print(f" ☁️ {self.name} used "+colored(" Strange Steam","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Fairy"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,90,a,b,c,r,al)  
    confuse(self,other,turn,20)
def freezingglare(self,other):
    al=1
    w=1
    r=randroll()
    print(f" 👁️ {self.name} used "+colored(" Freezing Glare","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Psychic"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,90,a,b,c,r,al,w)  
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
    print(f" 👁️ {self.name} used "+colored(" Expanding Force","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Psychic"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,80,a,b,c,r,al,w)  
def risingvoltage(self,other):
    al=1
    w=1
    r=randroll()
    if field.terrain=="Electric":
        w*=1.5
    print(f" ⚡ {self.name} used "+colored(" Rising Voltage","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,70,a,b,c,r,al,w)      
def extrasensory (self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" ⚜️ {self.name}'s {self.ability}.")
    print(f" 👁️ {self.name} used "+colored(" Extrasensory","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Psychic"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,90,a,b,c,r,al)  
    flinch(self,other,10)
def nightdaze(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" ⚜️ {self.name}'s {self.ability}.")
    print(f" 🌃 {self.name} used "+colored(" Night Daze","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Dark"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=special(self,self.level,self.spatk,other.spdef,120,a,b,c,r,al)  
    self.hp-=dmg/4
    other.hp-=dmg
    print(f" {self.name} was hurt by recoil!")
    ch=random.randint(1,100)
    if ch<40 and self.ability!="Sheer Force":
        print(f" {other.name}'s accuracy fell!")
        other.accuracy-=10
def bittermalice(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" ⚜️ {self.name}'s {self.ability}.")
    print(f" 😖 {self.name} used "+colored(" Bitter Malice","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
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
    other.hp-=special(self,self.level,self.spatk,other.spdef,base,a,b,c,r,al) 
    if a!=0:
        atkchange(other,self,-0.5)
        
    ch=random.randint(1,100)
    if ch>70 and other.status=="Alive" and a!=0:
        other.status="Frostbite"
        print(f" {other.name} got frostbite.")
def dracobarrage(self,other):
    al=1
    r=randroll()
    print(f" 🐉 {self.name} used "+colored(" Draco Barrage","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Dragon"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=0
    if a==0:
        a=1
    if self.spatk>self.atk:
        dmg=special(self,self.level,self.spatk,other.spdef,100,a,b,c,r,al)  
    if self.atk>self.spatk:
        dmg=physical(self,self.level,self.atk,other.defense,100,a,b,c,r,al)    
    other.hp-=dmg
    if other.hp<0:
        other.hp=0
    self.hp-=(other.maxhp-other.hp)*0.33
        
def photongeyser(self,other):
    al=1
    r=randroll()
    print(f" ☄️ {self.name} used "+colored(" Photon Geyser","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Psychic"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,100,a,b,c,r,al)  
    if self.atk>self.spatk:
        other.hp-=physical(self,self.level,self.atk,other.defense,100,a,b,c,r,al)             
def prismaticlaser(self,other):
    al=1
    r=randroll()
    print(f" ☄️ {self.name} used "+colored(" Prismatic Laser","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Psychic"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,160,a,b,c,r,al)      
def hyperbeam(self,other):
    al=1
    r=randroll()
    print(f" ☄️ {self.name} used "+colored(" Hyper Beam","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Normal"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al)
def triattack(self,other):
    al=1
    r=randroll()
    print(f" 🔥❄️⚡ {self.name} used "+colored(" Tri Attack","white",attrs=["bold"])+"!")
    if self.ability=="Sheer Force":
        al=1.5
        print(f" ⚜️ {self.name}'s {self.ability}.")
    c=isCrit(self,other)
    self.atktype="Normal"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,90,a,b,c,r,al)    
    ch=random.randint(1,100)
    if ch<20 and other.status=="Alive" and self.ability!="Sheer Force":
        x=random.randint(1,3)
        print(f" {other.name} got a status!")
        if x==3:
            other.status=="Paralyzed"
        if x==2:
            other.status=="Frozen"
        if x==1:
            other.status=="Burned"
            
        
def hypervoice(self,other):
    al=1
    r=randroll()
    print(f" 🔉 {self.name} used "+colored(" Hyper Voice","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Normal"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,100,a,b,c,r,al)    
    ch=random.randint(1,100)
    if ch<10:
        spdefchange(other,self,-0.5)
def roaroftime(self,other):
    al=1
    r=randroll()
    print(f" ⏳ {self.name} used "+colored(" Roar of Time","blue",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Dragon"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
def rockwrecker(self,other):
    al=1
    r=randroll()
    print(f" 🪨 {self.name} used "+colored(" Rock Wrecker","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Rock"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)     
def meteorassault(self,other):
    al=1
    r=randroll()
    print(f" 💥 {self.name} used "+colored(" Meteor Assault","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,160,a,b,c,r,al)
    if a!=0:
        paralyzed(self,other,40)         
def gigaimpact(self,other):
    al=1
    r=randroll()
    print(f" 💥 {self.name} used "+colored(" Giga Impact","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Normal"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)             
def dragonpulse(self,other):
    al=1
    r=randroll()
    print(f" 🐉 {self.name} used "+colored(" Dragon Pulse","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Dragon"
    if self.ability=="Mega Launcher":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,90,a,b,c,r,al)   
def eternabeam(self,other):
    al=1
    r=randroll()
    print(f" 🌇 {self.name} used "+colored(" Eternabeam","blue",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Dragon"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,160,a,b,c,r,al)       
def dynamaxcannon(self,other):
    al=1
    r=randroll()
    print(f" 🔺 {self.name} used "+colored(" Dynamax Cannon","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Dragon"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=100
    if other.dmax==True:
        base*=2
    other.hp-=special(self,self.level,self.spatk,other.spdef,base,a,b,c,r,al)       
def spacialrend(self,other):
    al=1
    r=randroll()
    print(f" 🌌 {self.name} used "+colored(" Spacial Rend","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other,2)
    self.atktype="Dragon"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,100,a,b,c,r,al)       
def dazzlinggleam(self,other):
    al=1
    r=randroll()
    print(f" 🌟 {self.name} used "+colored(" Dazzling Gleam","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Fairy"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,90,a,b,c,r,al)  
def lavaplume(self,other):
    self.atktype="Fire"
    w=weathereff(self,other)
    al=1
    r=randroll()
    print(f" 🌋 {self.name} used "+colored(" Lava Plume","red",attrs=["bold"])+"!")
    c=isCrit(self,other)    
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,90,a,b,c,r,al,w)       
    burn(self,other,30)
def hurricane (self,other,turn):
    al=1
    r=randroll()
    print(f" 🌪️ {self.name} used "+colored(" Hurricane","cyan",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Flying"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,110,a,b,c,r,al)          
    confuse(self,other,turn,100)
def inferno(self,other):
    self.atktype="Fire"
    w=weathereff(self,other)
    al=1
    r=randroll()
    print(f" 🔥 {self.name} used "+colored(" Inferno","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,120,a,b,c,r,al,w)
    burn(self,other,100)
        
def overheat(self,other):
    self.atktype="Fire"
    w=weathereff(self,other)
    al=1
    r=randroll()
    print(f" 🔥 {self.name} used "+colored(" Overheat","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,130,a,b,c,r,al,w)                
    spatkchange(self,self,-1)
    
def blastburn(self,other):
    self.atktype="Fire"
    w=weathereff(self,other)
    al=1
    r=randroll()
    print(f" 🌋 {self.name} used "+colored(" Blast Burn","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,160,a,b,c,r,al,w)  
    burn(self,other,60)
def frenzyplant(self,other):
    self.atktype="Grass"
    w=weathereff(self,other)
    al=1
    r=randroll()
    print(f" 🌿 {self.name} used "+colored(" Frenzy Plant","green",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,160,a,b,c,r,al,w)        
    if a!=0:
        poison(self,other,80) 
def hydrocannon(self,other):
    self.atktype="Water"
    w=weathereff(self,other)
    al=1
    r=randroll()
    print(f" 🌊 {self.name} used "+colored(" Hydro Cannon","blue",attrs=["bold"])+"!")
    if self.ability=="Mega Launcher":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,160,a,b,c,r,al,w)      
    ch=random.randint(1,100)
    if ch>40 and a!=0:
        other.status="Frostbite"
        print (f" 🥶 {other.name} was frozen.")
def sparklingaria(self,other):
    self.atktype="Water"
    w=weathereff(self,other)
    al=1
    r=randroll()
    print(f" 🦭 {self.name} used "+colored(" Sparkling Aria","blue",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,90,a,b,c,r,al,w)           
    if other.status=="Burned":
        other.status="Alive"
def eruption (self,other):
    self.atktype="Fire"
    w=weathereff(self,other)
    al=1
    r=randroll()
    print(f" 🌋 {self.name} used "+colored(" Eruption","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=round(150*(self.hp/self.maxhp))
    other.hp-=special(self,self.level,self.spatk,other.spdef,base,a,b,c,r,al,w)
def dragonenergy (self,other):
    self.atktype="Dragon"
    al=1
    w=weathereff(self,other)
    r=randroll()
    print(f" 🐉 {self.name} used "+colored(" Dragon Energy","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=round(150*(self.hp/self.maxhp))
    other.hp-=special(self,self.level,self.spatk,other.spdef,base,a,b,c,r,al,w)        
def waterspout (self,other):
    self.atktype="Water"
    al=1
    w=weathereff(self,other)
    r=randroll()
    print(f" ⛲ {self.name} used "+colored(" Water Spout","blue",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=round(150*(self.hp/self.maxhp))
    other.hp-=special(self,self.level,self.spatk,other.spdef,base,a,b,c,r,al,w)    
def crushgrip (self,other):
    self.atktype="Normal"
    al=1
    r=randroll()
    print(f" ✊ {self.name} used "+colored(" Crush Grip","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=round(1+120*(self.hp/self.maxhp))
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)    
def moonblast(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" ⚜️ {self.name}'s {self.ability}.")
    print(f" 🌕 {self.name} used "+colored(" Moonblast","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Fairy"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,90,a,b,c,r,al)      
    chance=30
    if self.ability=="Serene Grace":
        chance*=2
    if self.speed>other.speed:
        ch=random.randint(1,100)            
        if ch>(100-chance) and self.ability!="Sheer Force" and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil","Shield Dust"]:
            spatkchange(other,self,-0.5)
            
def sludgebomb(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" ⚜️ {self.name}'s {self.ability}.")
    print(f" 💣 {self.name} used "+colored(" Sludge Bomb","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Poison"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,90,a,b,c,r,al)                
    poison(self,other,10)
def sludgewave(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        print(f" {self.name}'s {self.ability}.")
        al=1.5
    print(f" 〰️ {self.name} used "+colored(" Sludge Wave","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Poison"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,95,a,b,c,r,al)                
    poison(self,other,10)        
def hydropump(self,other):
    self.atktype="Water"
    w=weathereff(self,other)
    al=1
    r=randroll()
    print(f" 🌊 {self.name} used "+colored(" Hydro Pump","blue",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,110,a,b,c,r,al,w)  
def earthpower(self,other):
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    print(f" ⛰️ {self.name} used "+colored(" Earth Power","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Ground"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,90,a,b,c,r,al)
    ch=random.randint(1,100)
    if ch>90 and self.ability!="Sheer Force" and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil","Shield Dust"]:
        spdefchange(other,self,-0.5)
         
def stompingtantrum(self,other):
    al=1
    r=randroll()
    print(f" 👣 {self.name} used "+colored(" Stomping Tantrum","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Ground"
    base=75
    if self.miss==True:
        base*=2
    if self.ability=="Striker":
        print(f" {self.name}'s {self.ability}!")
        al=1.3
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)        
#Bulldoze
def bulldoze (self,other):
    al=1
    r=randroll()
    print(f" 🚜 {self.name} used "+colored(" Bulldoze","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other)
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
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)    
    if a!=0:
        speedchange(other,self,-0.5)
         
#Icy Wind
def icywind (self,other):
    al=1
    r=randroll()
    print(f" 💨 {self.name} used "+colored(" Icy Wind","cyan",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Ice"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=55
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    other.hp-=special(self,self.level,self.spatk,other.spdef,base,a,b,c,r,al)    
    if a!=0:
        speedchange(other,self,-0.5)
           
def rocktomb(self,other):
    al=1
    r=randroll()
    print(f" 🪨❌ {self.name} used "+colored(" Rock Tomb","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Rock"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=60
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)    
    speedchange(other,self,-0.5)
         
#Magnitude     
def magnitude(self,other):
    al=1
    r=randroll()
    mag=random.choices([4,5,6,7,8,9,10],weights=[5,10,20,30,20,10,5],k=1)[0]
    print(f" ⛰️ {self.name} used "+colored(f" Magnitude {mag}","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other)
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
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)         
def hyperdrill(self,other):
    al=1
    r=randroll()
    print(f" 🪛  {self.name} used "+colored(" Hyper Drill","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Normal"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,100,a,b,c,r,al)    
#EARTHQUAKE        
def earthquake (self,other):
    al=1
    r=randroll()
    print(f" ⛰️ {self.name} used "+colored(" Earthquake","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Ground"
    if field.terrain=="Grassy":
        print(" Earthquakes damage was reduced by Grassy Terrain!")
        al*=0.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,100,a,b,c,r,al)
def landswrath(self,other):
    al=1
    r=randroll()
    print(f" ⛰️ {self.name} used "+colored(" Land's Wrath","green",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Ground"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,90,a,b,c,r,al)    
def thousandwaves(self,other):
    al=1
    r=randroll()
    print(f" 〰️ {self.name} used "+colored(" Thousand Waves","green",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Ground"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,90,a,b,c,r,al)        
    other.trap=self
def thousandarrows(self,other):
    al=1
    r=randroll()
    print(f" 🏹 {self.name} used "+colored(" Thousand Arrows","green",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Ground"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if a==0:
        a=1
    other.hp-=physical(self,self.level,self.atk,other.defense,90,a,b,c,r,al)        
def coreenforcer(self,other):
    al=1
    r=randroll()
    print(f" ⚕️ {self.name} used "+colored(" Core Enforcer","green",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Dragon"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,100,a,b,c,r,al)        
def highhorsepower(self,other):
    al=1
    r=randroll()
    print(f" 🐎 {self.name} used "+colored(" High Horsepower","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Ground"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,95,a,b,c,r,al)
def headlongrush (self,other):
    al=1
    r=randroll()
    print(f" 🐻 {self.name} used "+colored(" Headlong Rush","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Ground"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,120,a,b,c,r,al)
    if a!=0:
        defchange(self,self,-0.5)
        spdefchange(self,self,-0.5)
       
def firelash(self,other):
    self.atktype="Fire"
    w=weathereff(self,other)
    al=1
    r=randroll()
    print(f" ⛓️ {self.name} used "+colored(" Fire Lash","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,80,a,b,c,r,al,w)    
    if other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        defchange(other,self,-0.5)
        
def mysticalfire(self,other):
    self.atktype="Fire"
    w=weathereff(self,other)
    al=1
    r=randroll()
    print(f" 🔥 {self.name} used "+colored(" Mystical Fire","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,75,a,b,c,r,al,w)    
    if a!=0:
        spatkchange(other,self,-0.5)
           
def lunge(self,other):
    self.atktype="Bug"
    w=weathereff(self,other)
    al=1
    r=randroll()
    print(f" 🪲 {self.name} used "+colored(" Lunge","green",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,80,a,b,c,r,al,w)         
    atkchange(other,self,-0.5)   
    
def shelltrap(self,other):
    self.atktype="Fire"
    w=weathereff(self,other)
    al=1
    r=randroll()
    print(f" 🐢 {other.name} got blown up by  "+colored(" Shell Trap","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al,w)         
        
def thunderouskick(self,other):
    self.atktype="Fighting"
    w=weathereff(self,other)
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Thunderous Kick","red",attrs=["bold"])+"!")
    if self.ability=="Striker":
        print(f" {self.name}'s {self.ability}!")
        al=1.3
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,90,a,b,c,r,al,w)    
    ch=random.randint(1,100)
    if ch>80 and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        defchange(other,self,-0.5)
            
def chillingwater(self,other):
    self.atktype="Water"
    w=weathereff(self,other)
    al=1
    r=randroll()
    print(f" 💦 {self.name} used "+colored(" Chilling Water","blue",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,50,a,b,c,r,al,w)
    if other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        atkchange(other,self,-0.5)
                
def pounce(self,other):
    self.atktype="Bug"
    w=weathereff(self,other)
    al=1
    r=randroll()
    print(f" 🪲 {self.name} used "+colored(" Pounce","green",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,50,a,b,c,r,al,w)
    if other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        speedchange(other,self,-0.5)
                
def skittersmack(self,other):
    self.atktype="Bug"
    w=weathereff(self,other)
    al=1
    r=randroll()
    print(f" 🪲 {self.name} used "+colored(" Pounce","green",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,70,a,b,c,r,al,w)
    spatkchange(other,self,-0.5)
                        
def liquidation (self,other):
    self.atktype="Water"
    w=weathereff(self,other)
    al=1
    r=randroll()
    print(f" 🗡️ {self.name} used "+colored(" Liquidation","blue",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,80,a,b,c,r,al,w)    
    ch=random.randint(1,100)
    if ch>80 and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        defchange(other,self,-0.5)
        
def mysticalpower(self,other):
    self.atktype="Psychic"
    al=1
    r=randroll()
    print(f" 👁️‍🗨️ {self.name} used "+colored(" Mystical Power","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,70,a,b,c,r,al)
    if a!=0:
        spatkchange(self,other,0.5)
        
def torchsong(self,other):
    self.atktype="Fire"
    w=weathereff(self,other)
    al=1
    r=randroll()
    print(f" 🕯️ {self.name} used "+colored(" Torch Song","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,80,a,b,c,r,al,w)
    if a!=0:
        spatkchange(self,other,0.5)
def flamecharge(self,other):
    self.atktype="Fire"
    w=weathereff(self,other)
    al=1
    r=randroll()
    print(f" 🔥 {self.name} used "+colored(" Flame Charge","red",attrs=["bold"])+"!")
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}!")
        al=1.5
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,50,a,b,c,r,al,w)
    if a!=0:
        speedchange(self,other,0.5)   
def trailblaze(self,other):
    self.atktype="Grass"
    w=weathereff(self,other)
    al=1
    r=randroll()
    print(f" 🍃 {self.name} used "+colored(" Trailblaze","green",attrs=["bold"])+"!")
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}!")
        al=1.5
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,50,a,b,c,r,al,w)
    if a!=0:
        speedchange(self,other,0.5)                
def aquastep(self,other):
    self.atktype="Water"
    w=weathereff(self,other)
    al=1
    r=randroll()
    print(f" 💦 {self.name} used "+colored(" Aqua Step","blue",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,80,a,b,c,r,al,w)
    if a!=0:
        speedchange(self,other,0.5)
        
def tropkick(self,other):
    self.atktype="Grass"
    w=weathereff(self,other)
    al=1
    r=randroll()
    print(f" 🌳 {self.name} used "+colored(" Trop Kick","green",attrs=["bold"])+"!")
    if self.ability=="Striker":
        al*=1.3
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,70,a,b,c,r,al,w)
    atkchange(other,self,-0.5)
         
def razorshell(self,other):
    self.atktype="Water"
    w=weathereff(self,other)
    al=1
    r=randroll()
    print(f" 🐚 {self.name} used "+colored(" Razor Shell","blue",attrs=["bold"])+"!")
    if self.ability=="Sharpness":
        al*=1.5
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,75,a,b,c,r,al,w)    
    ch=random.randint(1,100)
    if ch>50 and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        defchange(other,self,-0.5)
         
def diamondstorm(self,other):
    self.atktype="Rock"
    w=weathereff(self,other)
    al=1
    r=randroll()
    print(f" 💎 {self.name} used "+colored(" Diamond Storm","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,100,a,b,c,r,al,w)    
    ch=random.randint(1,100)
    if ch>50 and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        spdefchange(other,self,-0.5)
                        
def wavecrash(self,other):
    self.atktype="Water"
    w=weathereff(self,other)
    al=1
    r=randroll()
    print(f" 🌊 {self.name} used "+colored(" Wave Crash","blue",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical(self,self.level,self.atk,other.defense,120,a,b,c,r,al,w)    
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
def confuseray(self,other,turn):
    print(f" 😵 {self.name} used "+colored(" Confuse Ray","red",attrs=["bold"])+"!")  
    confuse(self,other,turn,100)    
def dynapunch(self,other,turn):
    al=1
    r=randroll()
    print(f" 👊🏽 {self.name} used "+colored(" Dynamic Punch","red",attrs=["bold"])+"!")   
    c=isCrit(self,other)
    self.atktype="Fighting"
    if self.item=="Punching Glove":
        al=1.5
    if self.ability=="Iron Fist":
        print(f" {self.name}'s {self.ability}!")
        al=1.3
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,100,a,b,c,r,al)      
    confuse(self,other,turn,100)
def armorcannon(self,other):
    al=1
    r=randroll()
    print(f" 💣 {self.name} used "+colored(" Armor Cannon","red",attrs=["bold"])+"!")
    if self.ability=="Mega Launcher":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    c=isCrit(self,other)
    self.atktype="Fire"
    w=weathereff(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,120,a,b,c,r,al,w)       
    if a!=0:
        defchange(self,self,-0.5)
        spdefchange(self,self,-0.5)
        
def electrodrift(self,other):
    al=1
    r=randroll()
    print(f" 🚙 {self.name} used "+colored(" Electro Drift","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if a>2:
        a*=1.5
    other.hp-=special(self,self.level,self.spatk,other.spdef,100,a,b,c,r,al)                
def collisioncourse(self,other):
    al=1
    r=randroll()
    print(f" 🏍️ {self.name} used "+colored(" Collision Course","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if a>2:
        a*=1.5
    other.hp-=physical(self,self.level,self.atk,other.defense,100,a,b,c,r,al)       
    
def smellingsalts(self,other):
    al=1
    r=randroll()
    print(f" 💥 {self.name} used "+colored(" Smelling Salts","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=70
    if other.status=="Paralyzed":
        base*=2
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)            
    if a!=0 and other.status=="Paralyzed":
        other.status="Alive"
                 
def closecombat(self,other):
    al=1
    r=randroll()
    print(f" 💥 {self.name} used "+colored(" Close Combat","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,120,a,b,c,r,al)       
    if a!=0:
        defchange(self,self,-0.5)
        spdefchange(self,self,-0.5)
        
def bulletpunch(self,other):
    al=1
    r=randroll()
    print(f" 👊🏻 {self.name} used "+colored(" Bullet Punch","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Steel"
    if self.item=="Punching Glove":
        al=1.5
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
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)        
    
def shadowsneak(self,other):
    al=1
    r=randroll()
    print(f" 👻 {self.name} used "+colored(" Shadow Sneak","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Ghost"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    base=40
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)         
       
def voltswitch(self,other):
    al=1
    r=randroll()
    print(f" ⚡↪️ {self.name} used "+colored(" Volt Switch","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,70,a,b,c,r,al)       
    
def flipturn(self,other):
    al=1
    r=randroll()
    print(f" 💦↪️ {self.name} used "+colored(" Flip Turn","blue",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Water"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,70,a,b,c,r,al)         
    
def uturn(self,other):
    al=1
    r=randroll()
    print(f" 🪲↪️ {self.name} used "+colored(" U-turn","green",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Bug"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,70,a,b,c,r,al)         
          
def xscissor (self,other):
    al=1
    r=randroll()
    print(f" ⚔️ {self.name} used "+colored(" X-Scissor","green",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Bug"
    if self.ability=="Sharpness":
        al*=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,90,a,b,c,r,al)        
       
def superpower(self,other):
    al=1
    r=randroll()
    print(f" 🦸 {self.name} used "+colored(" Superpower","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,120,a,b,c,r,al)   
    if a!=0:
        atkchange(self,self,-0.5)
        defchange(self,self,-0.5)
            
def dragonhammer(self,other):
    al=1
    r=randroll()
    print(f" 🔨 {self.name} used "+colored(" Dragon Hammer","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Dragon"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,100,a,b,c,r,al)        
    
def lightscreen(self,other,tr1,turn):    
    print(f" 🟪 {self.name} used "+colored(" Light Screen","yellow",attrs=["bold"])+"!")
    if tr1.lightscreen is True:
        print(" It failed!")
    if tr1.lightscreen is False:
        tr1.lightscreen=True
        print(" Light Screen raised your team's Special Defense!")
        tr1.lsturn=turn
        tr1.lightscreenend(self,other)
        
def tailwind(self,other,tr1,turn):    
    print(f" 🍃 {self.name} used "+colored(" Tailwind","cyan",attrs=["bold"])+"!")
    if tr1.tailwind is True:
        print(" It failed!")
    if tr1.tailwind is False:
        tr1.tailturn=turn
        tr1.twend(self,other)
        tr1.tailwind=True  
        print(" The Tailwind blew from behind your team.")        
        
def reflect(self,other,tr1,turn):    
    print(f" 🟦 {self.name} used "+colored(" Reflect","magenta",attrs=["bold"])+"!")
    if tr1.reflect is True:
        print(" It failed!")
    if tr1.reflect is False:
        tr1.reflecturn=turn
        tr1.reflectend(self,other)
        tr1.reflect=True  
        print(" Reflect raised your team's Defense!")
        
def auroraveil(self,other,tr1,turn):    
    print(f" ⬜ {self.name} used "+colored(" Aurora Veil","cyan",attrs=["bold"])+"!")
    if tr1.auroraveil is True and ("Gigantamax Lapras" not in self.name or field.weather not in ["Hail","Snowstorm"]):
        print(" It failed!")
    if tr1.auroraveil is False and ("Gigantamax Lapras" in self.name or field.weather in ["Hail","Snowstorm"]):
        tr1.auroraturn=turn
        tr1.auroraend(self,other)
        tr1.auroraveil=True  
        print(" 🌈 Aurora Veil will reduced your team's damage taken!")        
        
def zenheadbutt(self,other):
    al=1
    r=randroll()
    print(f" 🧘🏻 {self.name} used "+colored(" Zen Headbutt","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Psychic"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,80,a,b,c,r,al)  
    flinch(self,other,20)
def icespinner(self,other):
    al=1
    r=randroll()
    print(f" 🌪️❄️ {self.name} used "+colored(" Ice Spinner","cyan",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Ice"
    w=weathereff(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,80,a,b,c,r,al,w)  
    if field.terrain!="Normal":
        field.terrain="Normal"
        print(" 🌐 The battlefield turned normal.")
def tripleaxel(self,other):
    al=1
    r=randroll()
    print(f" 🏔️ {self.name} used "+colored(" Triple Axel","cyan",attrs=["bold"])+"!")
    self.atktype="Ice"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.ability=="Striker":
        al*=1.3
    w=weathereff(self,other)
    ch=random.randint(1,100)
    hit=0
    if ch<90:
        c=isCrit(self,other)
        other.hp-=physical(self,self.level,self.atk,other.defense,20,a,b,c,r,al,w)    
        hit+=1
        ch=random.randint(1,100)
        if ch<90:
            c=isCrit(self,other)
            other.hp-=physical(self,self.level,self.atk,other.defense,40,a,b,c,r,al,w)  
            hit+=1
            ch=random.randint(1,100)    
            if ch<90:
                c=isCrit(self,other)
                other.hp-=physical(self,self.level,self.atk,other.defense,60,a,b,c,r,al,w)
                hit+=1
        print(f" It hit {hit} times!")
    else:
        print(" It missed.")          
def triplekick(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Triple Kick","red",attrs=["bold"])+"!")
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.ability=="Striker":
        al*=1.3
    w=weathereff(self,other)
    ch=random.randint(1,100)
    hit=0
    if ch<90:
        c=isCrit(self,other)
        other.hp-=physical(self,self.level,self.atk,other.defense,20,a,b,c,r,al,w)    
        hit+=1
        ch=random.randint(1,100)
        if ch<90:
            c=isCrit(self,other)
            other.hp-=physical(self,self.level,self.atk,other.defense,40,a,b,c,r,al,w)  
            hit+=1
            ch=random.randint(1,100)    
            if ch<90:
                c=isCrit(self,other)
                other.hp-=physical(self,self.level,self.atk,other.defense,60,a,b,c,r,al,w)
                hit+=1
        print(f" It hit {hit} times!")
    else:
        print(" It missed.")        
def avalanche(self,other):
    al=1
    r=randroll()
    print(f" 🏔️ {self.name} used "+colored(" Avalanche","cyan",attrs=["bold"])+"!")
    if other.use!=None and other.use not in typemoves.statusmove:
        al*=2
    c=isCrit(self,other)
    self.atktype="Ice"
    w=weathereff(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,60,a,b,c,r,al,w)                   
def iciclecrash(self,other):
    al=1
    r=randroll()
    print(f" 🏔️ {self.name} used "+colored(" Icicle Crash","cyan",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Ice"
    w=weathereff(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,85,a,b,c,r,al,w)  
    flinch(self,other,30)
def zingzap(self,other):
    al=1
    r=randroll()
    print(f" ⚡ {self.name} used "+colored(" Zing Zap","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Electric"
    w=weathereff(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,80,a,b,c,r,al,w)  
    flinch(self,other,30)
def needlearm(self,other):
    al=1
    r=randroll()
    print(f" 🌵 {self.name} used "+colored(" Needle Arm","green",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Grass"
    w=weathereff(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,95,a,b,c,r,al,w)  
    flinch(self,other,30)
def firepunch(self,other):
    al=1
    r=randroll()
    w=weathereff(self,other)
    print(f" 🔥 {self.name} used "+colored(" Fire Punch","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Fire"
    if self.item=="Punching Glove":
        al=1.5
    if self.ability=="Iron Fist":
        print(f" {self.name}'s {self.ability}!")
        al=1.3
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,75,a,b,c,r,al,w)      
    burn(self,other,10)
def spiritshackle(self,other):
    al=1
    r=randroll()
    print(f" 🏹 {self.name} used "+colored(" Spirit Shackle","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Ghost"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,80,a,b,c,r,al)           
    flinch(self,other,20)
    other.trap=self
def firefang(self,other):    
    al=1
    r=randroll()
    self.atktype="Fire"
    weathereff(self,other)
    print(f" 🔥 {self.name} used "+colored(" Fire Fang","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    if self.ability=="Strong Jaw":
        print(f" 🦈 {self.name}'s {self.ability}!")
        al=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,75,a,b,c,r,al)      
    burn(self,other,10)

def volttackle(self,other):
    self.atktype="Electric"
    w=weathereff(self,other)
    al=1
    r=randroll()
    print(f" ⚡ {self.name} used "+colored(" Volt Tackle","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical(self,self.level,self.atk,other.defense,120,a,b,c,r,al,w)
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
    paralyzed(self,other,10) 
def flareblitz(self,other):
    self.atktype="Fire"
    w=weathereff(self,other)
    al=1
    r=randroll()
    print(f" 🔥 {self.name} used "+colored(" Flare Blitz","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical(self,self.level,self.atk,other.defense,120,a,b,c,r,al,w)
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
    burn(self,other,10)
def boltstrike(self,other):
    al=1
    r=randroll()
    print(f" ⚡ {self.name} used "+colored(" Bolt Strike","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,130,a,b,c,r,al)  
    paralyzed(self,other,20)
        
def freezeshock(self,other):
    if self.item=="Power Herb" or self.precharge==True:
        if self.item=="Power Herb":
            self.item+="[Used]"
            print(f" {self.name} became fully charged due to its Power Herb.")
        al=1
        r=randroll()
        print(f" ❄️⚡ {self.name} used "+colored(" Freeze Shock","cyan",attrs=["bold"])+"!")
        c=isCrit(self,other)
        self.atktype="Ice"
        w=weathereff(self,other)
        ab=weakness(self,other,field)
        a=ab[0]
        b=ab[1]   
        other.hp-=physical(self,self.level,self.atk,other.defense,140,a,b,c,r,al,w)  
        paralyzed(self,other,30)
        self.precharge=False  
    elif self.precharge==False:
        print(f" ❄️ {self.name} became cloaked in a freezing light!")
        self.precharge=True
    
      
def fusionbolt(self,other):
    al=1
    r=randroll()
    print(f" ⚡ {self.name} used "+colored(" Fusion Bolt","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,100,a,b,c,r,al)  
       
def tpunch(self,other):
    al=1
    r=randroll()
    print(f" ⚡ {self.name} used "+colored(" Thunder Punch","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Electric"
    if self.item=="Punching Glove":
        al=1.5
    if self.ability=="Iron Fist":
        print(f" {self.name}'s {self.ability}!")
        al=1.3
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,80,a,b,c,r,al)  
    paralyzed(self,other,10)
      
def poisontail(self,other):
    al=1
    r=randroll()
    print(f" 🐍 {self.name} used "+colored(" Poison Tail","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other,2)
    self.atktype="Poison"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,90,a,b,c,r,al)          
    poison(self,other,30)            
def poisonfang(self,other):
    al=1
    r=randroll()
    print(f" 🐍 {self.name} used "+colored(" Poison Fang","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Poison"
    if self.ability=="Strong Jaw":
        print(f" 🦈 {self.name}'s {self.ability}!")
        al=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,75,a,b,c,r,al)          
    poison(self,other,30)
def psychicfang(self,other):
    al=1
    r=randroll()
    print(f" 👁️ {self.name} used "+colored(" Psychic Fangs","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Psychic"
    if self.ability=="Strong Jaw":
        print(f" 🦈 {self.name}'s {self.ability}!")
        al=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,75,a,b,c,r,al)          
def tfang(self,other):
    al=1
    r=randroll()
    print(f" ⚡ {self.name} used "+colored(" Thunder Fang","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Electric"
    if self.ability=="Strong Jaw":
        print(f" 🦈 {self.name}'s {self.ability}!")
        al=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,75,a,b,c,r,al)  
    paralyzed(self,other,20)
      
def plasmafists(self,other):
    al=1
    r=randroll()
    print(f" ⚡ {self.name} used "+colored(" Plasma Fists","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Electric"
    if self.item=="Punching Glove":
        al=1.5
    if self.ability=="Iron Fist":
        print(f" {self.name}'s {self.ability}!")
        al=1.3
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,100,a,b,c,r,al)          
def suckerpunch(self,other):
    al=1
    r=randroll()
    print(f" 👿 {self.name} used "+colored(" Sucker Punch","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    if self.item=="Punching Glove":
        al=1.5
    if self.ability=="Iron Fist":
        print(f" {self.name}'s {self.ability}!")
        al=1.3
    self.atktype="Dark"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,80,a,b,c,r,al)         
def machpunch(self,other):
    al=1
    r=randroll()
    print(f" 👊🏼 {self.name} used "+colored(" Mach Punch","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Fighting"
    if self.item=="Punching Glove":
        al=1.5
    if self.ability=="Iron Fist":
        print(f" {self.name}'s {self.ability}!")
        al=1.3
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,40,a,b,c,r,al)   
def vaccumwave(self,other):
    al=1
    r=randroll()
    print(f" 🌀 {self.name} used "+colored(" Vaccum Wave","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,40,a,b,c,r,al)                  
def iceshard(self,other):
    al=1
    r=randroll()
    print(f" ❄️ {self.name} used "+colored(" Ice Shard","cyan",attrs=["bold"])+"!")
    w=weathereff(self,other)
    c=isCrit(self,other)
    self.atktype="Ice"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,40,a,b,c,r,al,w)          
def hornleech(self,other):
    al=1
    r=randroll()
    print(f" 🐮 {self.name} used "+colored(" Horn Leech","green",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Grass"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical(self,self.level,self.atk,other.defense,75,a,b,c,r,al)      
    if a!=0 and self.hp!=self.maxhp:
        print(f" {other.name} had its energy drained!")
    if dmg>other.hp:
        dmg=other.hp
        other.hp-=dmg
    else:
        other.hp-=dmg
    heal=dmg/2
    if other.ability=="Liquid Ooze" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"]:
        print(f" 🤢 {other.name}'s Liquid Ooze!")
        heal=-heal
    if self.hp<=(self.maxhp-heal):
        if self.item=="Big Root":
            self.hp+=heal*1.3
        else:
            self.hp+=heal
    else:
        self.hp=self.maxhp    
def bitterblade(self,other):
    al=1
    r=randroll()
    print(f" 🗡️ {self.name} used "+colored(" Bitter Blade","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Fire"
    w=weathereff(self,other)
    if self.ability=="Sharpness":
        al*=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical(self,self.level,self.atk,other.defense,75,a,b,c,r,al,w)      
    if a!=0 and self.hp!=self.maxhp:
        print(f" {other.name} had its energy drained!")
    if dmg>other.hp:
        dmg=other.hp
        other.hp-=dmg
    else:
        other.hp-=dmg
    heal=dmg/2
    if other.ability=="Liquid Ooze" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"]:
        print(f" 🤢 {other.name}'s Liquid Ooze!")
        heal=-heal
    if self.hp<=(self.maxhp-heal):
        if self.item=="Big Root":
            self.hp+=heal*1.3
        else:
            self.hp+=heal
    else:
        self.hp=self.maxhp 
def drainingkiss(self,other):
    al=1
    r=randroll()
    print(f" 💋 {self.name} used "+colored(" Draining Kiss","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Fairy"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical(self,self.level,self.atk,other.defense,50,a,b,c,r,al)      
    if a!=0 and self.hp!=self.maxhp:
        print(f" {other.name} had its energy drained!")
    if dmg>other.hp:
        dmg=other.hp
        other.hp-=dmg
    else:
        other.hp-=dmg
    heal=dmg*0.75
    if other.ability=="Liquid Ooze" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"]:
        print(f" 🤢 {other.name}'s Liquid Ooze!")
        heal=-heal
    if self.hp<=(self.maxhp-heal):
        if self.item=="Big Root":
            self.hp+=heal*1.3
        else:
            self.hp+=heal
    else:
        self.hp=self.maxhp               
def drainpunch(self,other):
    al=1
    r=randroll()
    print(f" 👊🏼 {self.name} used "+colored(" Drain Punch","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Fighting"
    if self.item=="Punching Glove":
        al=1.5
    if self.ability=="Iron Fist":
        print(f" {self.name}'s {self.ability}!")
        al=1.3
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical(self,self.level,self.atk,other.defense,75,a,b,c,r,al)      
    if a!=0 and self.hp!=self.maxhp:
        print(f" {other.name} had its energy drained!")
    if dmg>other.hp:
        dmg=other.hp
        other.hp-=dmg
    else:
        other.hp-=dmg
    heal=dmg/2
    if other.ability=="Liquid Ooze" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"]:
        print(f" 🤢 {other.name}'s Liquid Ooze!")
        heal=-heal
    if self.hp<=(self.maxhp-heal):
        if self.item=="Big Root":
            self.hp+=heal*1.3
        else:
            self.hp+=heal
    else:
        self.hp=self.maxhp
def parabolic(self,other):
    al=1
    r=randroll()
    print(f" ⚡ {self.name} used "+colored(" Parabolic Charge","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Electric"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=special(self,self.level,self.spatk,other.spdef,75,a,b,c,r,al)
    if a!=0 and self.hp!=self.maxhp:
        print(f" {other.name} had its energy drained!")
    if dmg>other.hp:
        dmg=other.hp
        other.hp-=dmg
    else:
        other.hp-=dmg
    heal=dmg/2
    if other.ability=="Liquid Ooze" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"]:
        print(f" 🤢 {other.name}'s Liquid Ooze!")
        heal=-heal
    if self.hp<=(self.maxhp-heal):
        if self.item=="Big Root":
            self.hp+=heal*1.3
        else:
            self.hp+=heal
    else:
        self.hp=self.maxhp        
        
def dizzypunch(self,other,turn):
    al=1
    r=randroll()
    print(f" 😵 {self.name} used Dizzy Punch.")
    c=isCrit(self,other)
    self.atktype="Normal"
    if self.ability=="Iron Fist":
        print(f" {self.name}'s {self.ability}!")
        al=1.3
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,70,a,b,c,r,al)
    confuse(self,other,turn,20)
def strength (self,other):
    al=1
    r=randroll()
    print(f" 💪 {self.name} used "+colored(" Strength","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Normal"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,80,a,b,c,r,al)          
def icepunch(self,other):
    al=1
    r=randroll()
    print(f" ❄️ {self.name} used "+colored(" Ice Punch","cyan",attrs=["bold"])+"!")
    w=weathereff(self,other)
    c=isCrit(self,other)
    self.atktype="Ice"
    if self.item=="Punching Glove":
        al=1.5
    if self.ability=="Iron Fist":
        print(f" {self.name}'s {self.ability}!")
        al=1.3
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,80,a,b,c,r,al,w)                  
    ch=random.randint(1,100)
    if ch>90 and other.status=="Alive":
        other.status=random.choice(["Frozen","Frostbite"])
        print(f" ❄️ {other.name} was frozen.")
def lastresort(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Last Resort","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Normal"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical(self,self.level,self.atk,other.defense,140,a,b,c,r,al)   
    other.hp-=dmg     
def bodyslam(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Body Slam","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Normal"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical(self,self.level,self.atk,other.defense,80,a,b,c,r,al)     
    other.hp-=dmg
    paralyzed(self,other,30)
         
def forcepalm(self,other):
    al=1
    r=randroll()
    print(f" ✋🏾 {self.name} used "+colored(" Force Palm","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=60
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)     
    paralyzed(self,other,30)
     
def drillrun(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Drill Run","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other,2)
    self.atktype="Ground"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,100,a,b,c,r,al)     
def smartstrike(self,other):
    al=1
    r=randroll()
    print(f" 🗡️ {self.name} used "+colored(" Smart Strike","white",attrs=["bold"])+"!")
    c=isCrit(self,other,2)
    self.atktype="Steel"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,70,a,b,c,r,al)   
def anchorshot(self,other):
    al=1
    r=randroll()
    print(f" ⚓ {self.name} used "+colored(" Anchor Shot","white",attrs=["bold"])+"!")
    c=isCrit(self,other,2)
    self.atktype="Steel"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,80,a,b,c,r,al)             
    other.trap=self
def lightofruin(self,other):
    al=1
    r=randroll()
    print(f" 🌸 {self.name} used "+colored(" Light of Ruin","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Fairy"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=special(self,self.level,self.spatk,other.spdef,140,a,b,c,r,al)   
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
    print(f" 🎆 {self.name} used "+colored(" Mind Blown","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Fire"
    w=weathereff(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al,w)   
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
    print(f" 🟢 {self.name} used "+colored(" Chloroblast","green",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Grass"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=special(self,self.level,self.spatk,other.spdef,120,a,b,c,r,al)       
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
    print(f" 🤕 {self.name} used "+colored(" Head Smash","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Rock"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)    
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
    print(f" {self.name} used "+colored(" Gunk Shot","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Poison"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical(self,self.level,self.atk,other.defense,120,a,b,c,r,al)    
    other.hp-=dmg    
    poison(self,other,30) 
def belch(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Belch","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Poison"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=special(self,self.level,self.spatk,other.spdef,120,a,b,c,r,al)    
    other.hp-=dmg            
    self.hp-=(self.maxhp/3)
    print(f" {self.name} was hurt by extreme poison.")
def submission(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Submission","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical(self,self.level,self.atk,other.defense,80,a,b,c,r,al)    
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
    print(f" 🐂 {self.name} used "+colored(" Head Charge","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Normal"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.ability=="Sheer Force":
        print(f" {self.name}'s {self.ability}!")
        al=1.5
    dmg=physical(self,self.level,self.atk,other.defense,120,a,b,c,r,al)
    ch=random.randint(1,10)    
    if ch>8 and self.ability!="Sheer Force" and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        defchange(other,self,-0.5)
       
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
    print(f" 🐦 {self.name} used "+colored(" Brave Bird","cyan",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Flying"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical(self,self.level,self.atk,other.defense,120,a,b,c,r,al)    
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
def spectralthief(self,other):
    al=1
    r=randroll()
    print(f" 🫡 {self.name} used "+colored(" Spectral Thief","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Ghost"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=90
    dmg=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)   
    other.hp-=dmg         
    self.atkb,self.defb,self.spatkb,self.spdefb,self.speedb=other.atkb,other.defb,other.spatkb,other.spdefb,other.speedb
    other.atkb,other.defb,other.spatkb,other.spdefb,other.speedb=1,1,1,1,1
def soulrobbery(self,other):
    al=1
    r=randroll()
    print(f" 🫡 {self.name} used "+colored(" Soul Robbery","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Psychic"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=100
    dmg=special(self,self.level,self.spatk,other.spdef,base,a,b,c,r,al)   
    other.hp-=dmg         
    self.atkb,self.defb,self.spatkb,self.spdefb,self.speedb=other.atkb,other.defb,other.spatkb,other.spdefb,other.speedb
    other.atkb,other.defb,other.spatkb,other.spdefb,other.speedb=1,1,1,1,1    
    
def lastrespects(self,other,tr):
    al=1
    r=randroll()
    print(f" 🫡 {self.name} used "+colored(" Last Respects","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Ghost"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=50+(50*(6-len(tr.pokemons))) 
    dmg=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)   
    other.hp-=dmg 
def woodhammer(self,other):
    al=1
    r=randroll()
    print(f" 🪵 {self.name} used "+colored(" Wood Hammer","green",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Grass"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical(self,self.level,self.atk,other.defense,120,a,b,c,r,al)    
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

def focuspunch(self,other):
    if self.item=="Power Herb" or self.focus==True:
        if self.item=="Power Herb":
            self.item+="[Used]"
            print(f" {self.name} became fully charged due to its Power Herb.")
        al=1
        r=randroll()
        print(f" 👊 {self.name} used "+colored(" Focus Punch","red",attrs=["bold"])+"!")
        c=isCrit(self,other,2)
        self.atktype="Fighting"
        ab=weakness(self,other,field)
        a=ab[0]
        b=ab[1]   
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)    
        self.focus=False  
    elif self.focus==False:
        print(f" 🤨 {self.name} tightening its focus!")
        self.precharge=True   
def skyattack(self,other):
    if self.item=="Power Herb" or self.precharge==True:
        if self.item=="Power Herb":
            self.item+="[Used]"
            print(f" {self.name} became fully charged due to its Power Herb.")
        al=1
        r=randroll()
        print(f" 🕊️ {self.name} used "+colored(" Sky Attack","cyan",attrs=["bold"])+"!")
        c=isCrit(self,other,2)
        self.atktype="Flying"
        ab=weakness(self,other,field)
        a=ab[0]
        b=ab[1]   
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)     
        flinch(self,other,30)  
        self.precharge=False  
    elif self.precharge==False:
        print(f" 🌌 {self.name} became cloaked in a harsh light!")
        self.precharge=True
def razorwind(self,other):
    if self.item=="Power Herb" or self.precharge==True:
        if self.item=="Power Herb":
            self.item+="[Used]"
            print(f" {self.name} became fully charged due to its Power Herb.")
        al=1
        r=randroll()
        print(f" 🌪️ {self.name} used "+colored(" Razor Wind","cyan",attrs=["bold"])+"!")
        c=isCrit(self,other,2)
        self.atktype="Flying"
        ab=weakness(self,other,field)
        a=ab[0]
        b=ab[1]   
        other.hp-=physical(self,self.level,self.atk,other.defense,160,a,b,c,r,al)
        self.precharge=False  
    elif self.precharge==False:
        print(f" 🌪️ {self.name} whipped up a whirlwind!")
        self.precharge=True
def dive(self,other):
    if self.item=="Power Herb" or self.precharge==True:
        w=weathereff(self,other)
        if self.item=="Power Herb":
            self.item+="[Used]"
            print(f" {self.name} became fully charged due to its Power Herb.")
        al=1
        r=randroll()
        print(f" 🤿 {self.name} used "+colored(" Dive","blue",attrs=["bold"])+"!")
        c=isCrit(self,other)
        self.atktype="Water"
        ab=weakness(self,other,field)
        a=ab[0]
        b=ab[1]   
        other.hp-=physical(self,self.level,self.atk,other.defense,90,a,b,c,r,al,w)     
        self.precharge=False  
    elif self.precharge==False:
        print(f" 💦 {self.name} hid underwater!")
        self.precharge=True
        if self.ability=="Gulp Missile":
            x=""
            if self.hp<=(self.maxhp/2):
                x="Pikachu"
            if self.hp>(self.maxhp/2):
                x="Arrocuda"
            self.ability+=f"-{x}"
            print(f" 🐦 {self.name} caught a {x}!")
def fly(self,other):
    if self.item=="Power Herb" or self.precharge==True:
        if self.item=="Power Herb":
            self.item+="[Used]"
            print(f" {self.name} became fully charged due to its Power Herb.")
        al=1
        r=randroll()
        print(f" 🕊️ {self.name} used "+colored(" Fly","cyan",attrs=["bold"])+"!")
        c=isCrit(self,other)
        self.atktype="Flying"
        ab=weakness(self,other,field)
        a=ab[0]
        b=ab[1]   
        other.hp-=physical(self,self.level,self.atk,other.defense,90,a,b,c,r,al)     
        self.precharge=False  
    elif self.precharge==False:
        print(f" 🌌 {self.name} flew up high!")
        self.precharge=True
def dig(self,other):
    if self.item=="Power Herb" or self.precharge==True:
        if self.item=="Power Herb":
            self.item+="[Used]"
            print(f" {self.name} became fully charged due to its Power Herb.")
        al=1
        r=randroll()
        print(f" ⛏️ {self.name} used "+colored(" Dig","yellow",attrs=["bold"])+"!")
        c=isCrit(self,other)
        self.atktype="Ground"
        ab=weakness(self,other,field)
        a=ab[0]
        b=ab[1]   
        other.hp-=physical(self,self.level,self.atk,other.defense,80,a,b,c,r,al)     
        self.precharge=False  
    elif self.precharge==False:
        print(f" 🕳️ {self.name} burrowed its way under the ground!")
        self.precharge=True
def bounce(self,other):
    if self.item=="Power Herb" or self.precharge==True:
        if self.item=="Power Herb":
            self.item+="[Used]"
            print(f" {self.name} became fully charged due to its Power Herb.")
        al=1
        r=randroll()
        print(f" 🦘 {self.name} used "+colored(" Bounce","cyan",attrs=["bold"])+"!")
        c=isCrit(self,other)
        self.atktype="Flying"
        ab=weakness(self,other,field)
        a=ab[0]
        b=ab[1]   
        other.hp-=physical(self,self.level,self.atk,other.defense,85,a,b,c,r,al)     
        paralyzed(self,other,30)  
        self.precharge=False  
    elif self.precharge==False:
        print(f" ⬆️ {self.name} sprang up!")
        self.precharge=True               
                                             
def crunch(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Crunch","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Dark"
    if self.ability=="Sheer Force":
        print(f" {self.name}'s {self.ability}!")
        al=1.5
    if self.ability=="Strong Jaw":
        print(f" 🦈 {self.name}'s {self.ability}!")
        al=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical(self,self.level,self.atk,other.defense,80,a,b,c,r,al)
    other.hp-=dmg
    ch=random.randint(1,100)
    if ch>80 and self.ability!="Sheer Force" and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        defchange(other,self,-0.5)
         
def jawlock(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Jaw Lock","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Dark"
    if self.ability=="Strong Jaw":
        print(f" 🦈 {self.name}'s {self.ability}!")
        al=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical(self,self.level,self.atk,other.defense,80,a,b,c,r,al)
    other.hp-=dmg
    other.trap=self
def playrough(self,other):
    al=1
    r=randroll()
    print(f" 💓 {self.name} used "+colored(" Play Rough","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Fairy"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,80,a,b,c,r,al)                      
    ch=random.randint(1,10)
    if ch==7 and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        atkchange(other,self,-0.5)
        
def powerwhip(self,other):
    al=1
    r=randroll()
    print(f" 🌿 {self.name} used "+colored(" Power Whip","green",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Grass"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,80,a,b,c,r,al)   
         
def aquatail(self,other):
    w=weathereff(self,other)
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Aqua Tail","blue",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Water"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,80,a,b,c,r,al,w)       
     
def astralbarrage(self,other):
    al=1
    r=randroll()
    print(f" 👻 {self.name} used "+colored(" Astral Barrage","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Ghost"
    w=weathereff(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,130,a,b,c,r,al,w)        
def glaciallance(self,other):
    al=1
    r=randroll()
    print(f" 🏔️ {self.name} used "+colored(" Glacial Lance","cyan",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Ice"
    w=weathereff(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,130,a,b,c,r,al,w)       
    
def breakingswipe(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Breaking Swipe","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Dragon"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=60
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)            
    if a!=0:
        atkchange(other,self,-0.5)
          
def falsesurrender(self,other):
    al=1
    r=randroll()
    print(f" 👹 {self.name} used"+colored(" False Surrender","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Dark"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,80,a,b,c,r,al)            
def spiritbreak(self,other):
    al=1
    r=randroll()
    print(f" {self.name} "+colored(" Spirit Break","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Fairy"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,75,a,b,c,r,al)            
    spatkchange(other,self,-0.5)
           
def orderup(self,other):
    al=1
    r=randroll()
    print(f" 🍥 {self.name} used "+colored(" Order Up","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Dragon"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,80,a,b,c,r,al)     
def dragonclaw(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Dragon Claw","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Dragon"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,80,a,b,c,r,al) 
def dragontail(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Dragon Tail","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Dragon"
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}!")
        al=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,60,a,b,c,r,al)     
def gigatonhammer(self,other):
    al=1
    r=randroll()
    print(f" 🔨 {self.name} used "+colored(" Gigaton Hammer","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Steel"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,160,a,b,c,r,al)       
def flyingpress(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Flying Press","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    self.atktype="Flying"
    bc=weakness(self,other,field)
    a=ab[0]*bc[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,80,a,b,c,r,al)       
def mountaingale(self,other):
    al=1
    r=randroll()
    print(f" 🏔️ {self.name} used "+colored(" Mountain Gale","cyan",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Ice"
    w=weathereff(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,120,a,b,c,r,al,w)       
    flinch(self,other,30)
def firstimpression(self,other):
    al=1
    r=randroll()
    print(f" 🦗 {self.name} used "+colored(" First Impression","green",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Bug"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=90
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)               
def fakeout(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Fake Out","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Normal"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=40
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)    
    if a!=0:     
        flinch(self,other,100)
def present(self,other):
    al=1
    r=randroll()
    print(f" 🎁 {self.name} used "+colored(" Present","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Normal"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=0
    ch=random.choices([1,2,3,4], weights=[40,30,10,20],k=1)[0]
    if ch==1:
        if other.hp!=other.maxhp:
            print(f" {self.name}'s present healed {other.name}!")
            other.hp+=(other.maxhp/4)
    if ch==3:
        print(f" {self.name}'s present damaged {other.name}!")
        base=120
    if ch==2:
        print(f" {self.name}'s present damaged {other.name}!")
        base=80
    if ch==1:
        print(f" {self.name}'s present damaged {other.name}!")
        base=40
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)     
def eggbomb(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Egg Bomb","green",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Grass"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,80,a,b,c,r,al)  
def knockoff(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Knock Off","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Dark"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=65
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    if "Used" not in other.item and other.item not in megastones and "m-Z" not in other.item:
        print(f" {self.name} knocked off {other.name}'s {other.item}!")
        base*=2
        other.item+="[Used]"
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)      
def crushclaw(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Crush Claw","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Normal"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,100,a,b,c,r,al)      
    ch=random.randint(1,2)
    if ch==2 and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        defchange(other,self,-0.5)
        
def seedbomb(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Seed Bomb","green",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Grass"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,80,a,b,c,r,al)  
def spinout(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Spin Out","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Steel"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,100,a,b,c,r,al)         
    speedchange(self,self,-1)
    
def irontail(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Iron Tail","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Steel"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,100,a,b,c,r,al)             
    ch=random.randint(1,100)
    if ch>70 and other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        defchange(other,self,-0.5)
      
def moongeistbeam(self,other):
    al=1
    r=randroll()
    print(f" 🦇 {self.name} used "+colored(" Moongeist Beam","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Ghost"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,100,a,b,c,r,al)              
def sunsteelstrike(self,other):
    al=1
    r=randroll()
    print(f" 🦁 {self.name} used "+colored(" Sunsteel Strike","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Steel"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,100,a,b,c,r,al)     
def behemothbash(self,other):
    al=1
    r=randroll()
    print(f" 🛡️💥 {self.name} used "+colored(" Behemoth Bash","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Steel"
    if other.dmax is True:
        al*=2
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.defense,other.defense,100,a,b,c,r,al)          
def behemothblade(self,other):
    al=1
    r=randroll()
    print(f" 🗡️💥 {self.name} used "+colored(" Behemoth Blade","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Steel"
    if other.dmax is True:
        al*=2
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,100,a,b,c,r,al)                   
def ironhead(self,other):
    al=1
    r=randroll()
    print(f" 🤖 {self.name} used "+colored(" Iron Head","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Steel"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,80,a,b,c,r,al)      
    flinch(self,other,30)
def meteormash(self,other):
    al=1
    r=randroll()
    print(f" 🌌 {self.name} used "+colored(" Meteor Mash","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Steel"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical(self,self.level,self.atk,other.defense,90,a,b,c,r,al)    
    other.hp-=dmg  
    ch=random.randint(1,100)
    if ch<80:
        atkchange(self,other,0.5)
       
def grassyglide(self,other):
    al=1
    r=randroll()
    print(f" ☘️ {self.name} used "+colored(" Grassy Glide","green",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Grass"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical(self,self.level,self.atk,other.defense,70,a,b,c,r,al)     
    other.hp-=dmg            
def appleacid(self,other):
    al=1
    r=randroll()
    print(f" 🍏 {self.name} used "+colored(" Apple Acid","green",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Grass"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=special(self,self.level,self.spatk,other.spdef,80,a,b,c,r,al)     
    if other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        other.hp-=dmg  
        spdefchange(other,self,-0.5)
        
def destinybond(self,other):
    print(f" 🪦 {self.name} used "+colored(" Destiny Bond","magenta",attrs=["bold"])+"!")    
    if other.dbond==True:
        print(" It failed")
    if other.dbond!=True:
        other.dbond=True       
        print(f" {self.name} is hoping to take its attacker down with it!")
def gravapple(self,other):
    al=1
    r=randroll()
    print(f" 🍎 {self.name} used "+colored(" Grav Apple","green",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Grass"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical(self,self.level,self.atk,other.defense,80,a,b,c,r,al)     
    other.hp-=dmg  
    defchange(other,self,-0.5)
  
def drumbeating(self,other):
    al=1
    r=randroll()
    print(f" 🥁 {self.name} used "+colored(" Drum Beating","green",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Grass"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical(self,self.level,self.atk,other.defense,80,a,b,c,r,al)     
    if other.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        other.hp-=dmg  
        speedchange(other,self,-0.5)
       
def icehammer(self,other):
    al=1
    r=randroll()
    print(f" 🧊🔨 {self.name} used "+colored(" Ice Hammer","cyan",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Ice"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical(self,self.level,self.atk,other.defense,100,a,b,c,r,al)     
    other.hp-=dmg  
    speedchange(self,self,-0.5)
   
def hammerarm(self,other):
    al=1
    r=randroll()
    print(f" 🔨 {self.name} used "+colored(" Hammer Arm","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical(self,self.level,self.atk,other.defense,100,a,b,c,r,al)     
    other.hp-=dmg  
    speedchange(self,self,-0.5)
   
def poweruppunch(self,other):
    al=1
    r=randroll()
    print(f" 👊🏽 {self.name} used "+colored(" Power-Up Punch","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Fighting"
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
    dmg=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)     
    other.hp-=dmg  
    if a>0:
        atkchange(self,other,0.5)
        
def doubleedge(self,other):
    al=1
    r=randroll()
    print(f" 💥 {self.name} used "+colored(" Double-Edge","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Normal"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical(self,self.level,self.atk,other.defense,100,a,b,c,r,al) 
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
    print(f" ⏪ {self.name} used "+colored(" Quick Attack","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Normal"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,40,a,b,c,r,al) 
def feint(self,other):
    al=1
    r=randroll()
    print(f" ⏪ {self.name} used "+colored(" Feint","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Normal"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,50,a,b,c,r,al)              
def extemespeed(self,other):
    al=1
    r=randroll()
    print(f" ⏪ {self.name} used "+colored(" Extreme Speed","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Normal"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,80,a,b,c,r,al)              
def crabhammer(self,other):
    self.atktype="Water"
    w=weathereff(self,other)
    al=1
    r=randroll()
    print(f" 🦀 {self.name} used "+colored(" Crabhammer","blue",attrs=["bold"])+"!")
    c=isCrit(self,other,2)   
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,100,a,b,c,r,al,w)  
def glaiverush(self,other):
    al=1
    r=randroll()
    print(f" 🔪 {self.name} used "+colored(" Glaive Rush","red",attrs=["bold"])+"!")
    c=isCrit(self,other,2)
    self.atktype="Dragon"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,120,a,b,c,r,al)    
def dragonrush(self,other):
    al=1
    r=randroll()
    print(f" 🐲 {self.name} used "+colored(" Dragon Rush","red",attrs=["bold"])+"!")
    c=isCrit(self,other,2)
    self.atktype="Dragon"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,100,a,b,c,r,al)    
    flinch(self,other,20)
def slash(self,other):
    al=1
    r=randroll()
    print(f" 🗡️ {self.name} used "+colored(" Slash","white",attrs=["bold"])+"!")
    if self.ability=="Sharpness":
        al*=1.5
    c=isCrit(self,other,2)
    self.atktype="Normal"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,70,a,b,c,r,al)
def aquacutter(self,other):
    al=1
    r=randroll()
    print(f" 💧🔪 {self.name} used "+colored(" Aqua Cutter","blue",attrs=["bold"])+"!")
    if self.ability=="Sharpness":
        al*=1.5
    c=isCrit(self,other,2)
    self.atktype="Water"
    w=weathereff(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,70,a,b,c,r,al,w) 
def direclaw(self,other,turn):
    al=1
    r=randroll()
    print(f" 🐾 {self.name} used "+colored(" Dire Claw","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other,2)
    self.atktype="Poison"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=80
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)
    if other.status=="Alive":
        sleep(self,other,10,turn)
    if other.status=="Alive":
        poison(self,other,10)
    if other.status=="Alive":
        paralyzed(self,other,10)
def crosschop(self,other):
    al=1
    r=randroll()
    print(f" 🥋 {self.name} used "+colored(" Cross Chop","red",attrs=["bold"])+"!")
    c=isCrit(self,other,2)
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,100,a,b,c,r,al)          
def nightslash(self,other):
    al=1
    r=randroll()
    print(f" 🔪 {self.name} used "+colored(" Night Slash","red",attrs=["bold"])+"!")
    c=isCrit(self,other,2)
    self.atktype="Dark"
    if self.ability=="Sharpness":
        al*=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,70,a,b,c,r,al)  
def ruination(self,other):
    print(f" 🌆 {self.name} used "+colored(" Ruination","red",attrs=["bold"])+"!")
    other.hp-=(other.hp/2)
def kowtowcleave(self,other):
    al=1
    r=randroll()
    print(f" ⚔️ {self.name} used "+colored(" Kowtow Cleave","red",attrs=["bold"])+"!")
    c=isCrit(self,other,2)
    self.atktype="Dark"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,85,a,b,c,r,al)      
def shadowpunch(self,other):
    al=1
    r=randroll()
    print(f" 👊🏽 {self.name} used "+colored(" Shadow Punch","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other,2)
    self.atktype="Ghost"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,80,a,b,c,r,al)        
def shadowclaw(self,other):
    al=1
    r=randroll()
    print(f" 🐾 {self.name} used "+colored(" Shadow Claw","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other,2)
    self.atktype="Ghost"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,80,a,b,c,r,al)       
def poltergeist(self,other):
    al=1
    r=randroll()
    print(f" ☕ {self.name} used "+colored(" Poltergeist","magenta",attrs=["bold"])+"!")
    if "Used" not in other.item:
        print(f" {other.name} is about to be attacked by its {other.item}.")
        c=isCrit(self,other,2)
        self.atktype="Ghost"
        ab=weakness(self,other,field)
        a=ab[0]
        b=ab[1]   
        other.hp-=physical(self,self.level,self.atk,other.defense,110,a,b,c,r,al) 
    if "Used" in other.item:
        print(f" It failed!") 
def ragefist(self,other):
    al=1
    r=randroll()
    print(f" 💢 {self.name} used "+colored(" Rage Fist","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Ghost"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=50+(50*self.atktime)
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)       
def hyperspacefury(self,other):
    al=1
    r=randroll()
    print(f" 🌌 {self.name} used "+colored(" Hyperspace Fury","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Dark"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,100,a,b,c,r,al)         
    defchange(self,self,-0.5)   
def psychocut(self,other):
    al=1
    r=randroll()
    print(f" 🌀🗡️ {self.name} used "+colored(" Psycho Cut","magenta",attrs=["bold"])+"!")
    if self.ability=="Sharpness":
        al*=1.5
    c=isCrit(self,other,2)
    self.atktype="Psychic"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,70,a,b,c,r,al) 
def psyblade(self,other):
    al=1
    r=randroll()
    print(f" 🌀🗡️ {self.name} used "+colored(" Psyblade","magenta",attrs=["bold"])+"!")
    if self.ability=="Sharpness":
        al*=1.5
    if field.terrain=="Electric":
        al*=1.5
    c=isCrit(self,other,2)
    self.atktype="Psychic"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,80,a,b,c,r,al)         
def esperwing(self,other):
    al=1
    r=randroll()
    print(f" 🦅 {self.name} used "+colored(" Esper Wing","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other,2)
    self.atktype="Psychic"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,80,a,b,c,r,al)       
    if a!=0:
        speedchange(self, other,0.5)
        
def wickedblow(self,other):
    al=1
    r=randroll()
    print(f" 😈 {self.name} used "+colored(" Wicked Blow","red",attrs=["bold"])+"!")
    c=isCrit(self,other,16)
    self.atktype="Dark"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,80,a,b,c,r,al) 
def stormthrow(self,other):
    al=1
    r=randroll()
    print(f" 🥏 {self.name} used "+colored(" Storm Throw","red",attrs=["bold"])+"!")
    c=isCrit(self,other,16)
    self.atktype="Fighting"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,60,a,b,c,r,al)       
def ceaseless(self,other,optr):
    al=1
    r=randroll()
    print(f" 🗡️ {self.name} used "+colored(" Ceaseless Edge","red",attrs=["bold"])+"!")
    c=isCrit(self,other,16)
    self.atktype="Dark"
    if self.ability=="Sharpness":
        al*=1.5
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,70,a,b,c,r,al)       
    if optr.hazard.count("Spikes")<3:
        print(" ✴️ Pointed spikes float in the air around the opposing team!")
        optr.hazard.append("Spikes")
def surgingstrikes(self,other):
    al=1
    r=randroll()
    print(f" 🌊 {self.name} used "+colored(" Surging Strikes","blue",attrs=["bold"])+"!")
    c=isCrit(self,other,16)
    self.atktype="Water"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,25,a,b,c,r,al)                    
def dragonascent(self,other):
    al=1
    r=randroll()
    print(f" 🐉 {self.name} used "+colored(" Dragon Ascent","green",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Flying"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,120,a,b,c,r,al)     
    defchange(self,self,-0.5)
    spdefchange(self,self,-0.5)
def weatherball(self,other):
    self.atktype="Normal"
    base=50
    typ="⚪"
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
    if field.weather in ["Hail","Snowstorm"]:
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
    w=weathereff(self,other)
    r=randroll()
    print(f" {typ} {self.name} used "+colored(" Weather Ball",f"{color}",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,base,a,b,c,r,al,w)
def maxgeyser(self,other,tr1,turn):
    self.atktype="Water"
    w=weathereff(self,other)
    print(f" 🔺🌊 {self.name} used "+colored(" Max Geyser","blue",attrs=["bold"])+"!")
    al=1
    r=randroll()
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al,w)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al,w)      
    if field.weather not in ["Desolate Land","Primordial Sea","Strong Wind","Rainy"]:
        print(f" 🌧️ {self.name} made it rain.")
        field.weather="Rainy"
        tr1.rainturn=turn
        tr1.rainend(self,other)       
def raindance(self,other,tr1,turn):
    print(f" ☔ {self.name} used "+colored(" Rain Dance","blue",attrs=["bold"])+"!")
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
    w=weathereff(self,other)
    print(f" 🔺🔥 {self.name} used "+colored(" Max Flare","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al,w)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al,w)
    if field.weather not in ["Desolate Land","Primordial Sea","Strong Wind","Sunny"]:
        print(f" ☀️ The sunlight turned harsh!")
        field.weather="Sunny"
        tr1.sunturn=turn
        tr1.sunend(self,other)     
                
def sunnyday(self,other,tr1,turn):
    print(f" ☀️ {self.name} used "+colored(" Sunny Day","yellow",attrs=["bold"])+"!")
    if field.weather not in ["Desolate Land","Primordial Sea","Strong Wind","Sunny"]:
        print(f" ☀️ {self.name} made the sunlight harsh.")
        field.weather="Sunny"
        tr1.sunturn=turn
        tr1.sunend(self,other)
    else:
        print(" It failed.")        
def maxrockfall(self,other,tr1,turn):
    print(f" 🔺 {self.name} used "+colored(" Max Rockfall","yellow",attrs=["bold"])+"!")
    al=1
    r=randroll()
    self.atktype="Rock"
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)          
    if field.weather not in ["Desolate Land","Primordial Sea","Strong Wind","Sandstorm"]:
        print(f" 🏜️ {self.name} started a sandstorm.")
        field.weather="Sandstorm" 
        tr1.sandturn=turn
        tr1.sandend(self,other)     
def chillyreception (self,other,tr1,turn):
    print(f" ❄️ {self.name} used "+colored(" Chilly Reception","cyan",attrs=["bold"])+"!")
    if field.weather not in ["Desolate Land","Primordial Sea","Strong Wind","Snowstorm"]:
        print(f" {self.name} started a snowstorm.")
        field.weather="Snowstorm" 
        tr1.snowstormturn=turn
        tr1.snowstormend(self,other)
    else:
        print(" It failed.")        
              
def snowscape(self,other,tr1,turn):
    print(f" ❄️ {self.name} used "+colored(" Snowscape","cyan",attrs=["bold"])+"!")
    if field.weather not in ["Desolate Land","Primordial Sea","Strong Wind","Snowstorm"]:
        print(f" {self.name} started a snowstorm.")
        field.weather="Snowstorm" 
        tr1.snowstormturn=turn
        tr1.snowstormend(self,other)
    else:
        print(" It failed.")        
def sandstorm(self,other,tr1,turn):
    print(f" 🏜️ {self.name} used "+colored(" Sandstorm","yellow",attrs=["bold"])+"!")
    if field.weather not in ["Desolate Land","Primordial Sea","Strong Wind","Sandstorm"]:
        print(f" {self.name} started a sandstorm.")
        field.weather="Sandstorm" 
        tr1.sandturn=turn
        tr1.sandend(self,other)
    else:
        print(" It failed.")
def hail(self,other,tr1,turn):
    print(f" 🧊 {self.name} used "+colored(" Hail","cyan",attrs=["bold"])+"!")
    if field.weather not in ["Desolate Land","Primordial Sea","Strong Wind","Hail"]:
        print(f" 🌨️ {self.name} started a hailstorm.")
        field.weather="Hail"     
        tr1.hailturn=turn
        tr1.hailend(self,other) 
    else:
        print(" It failed.")      
def maxhailstorm(self,other,tr1,turn):
    print(f" 🔺🧊 {self.name} used "+colored(" Max Hailstorm","cyan",attrs=["bold"])+"!")
    al=1
    r=randroll()
    self.atktype="Ice"
    w=weathereff(self,other)
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,150,a,b,c,r,al,w)    
    else:
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)   
    if field.weather not in ["Desolate Land","Primordial Sea","Strong Wind","Hail"]:
        print(f" 🌨️ {self.name} started a hailstorm.")
        field.weather="Hail"     
        tr1.hailturn=turn
        tr1.hailend(self,other)         
def dualchop(self,other):
    al=1
    r=randroll()
    print(f" 🦎 {self.name} used "+colored(" Dual Chop","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Dragon"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=40
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)       
def scaleshot(self,other):
    al=1
    r=randroll()
    print(f" 🦎 {self.name} used "+colored(" Scale Shot","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Dragon"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=25
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)                   
def dragondarts(self,other):
    al=1
    r=randroll()
    print(f" 🦎 {self.name} used "+colored(" Dragon Darts","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Dragon"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=50
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)          
def dualwingbeat(self,other):
    al=1
    r=randroll()
    print(f" 🕊️ {self.name} used "+colored(" Dual Wingbeat","cyan",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Flying"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=40
    if self.ability=="Technician":
        print(f" {self.name}'s {self.ability}.")
        base*=1.5
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)         
def precipiceblades(self,other):
    al=1
    r=randroll()
    print(f" 🦖🌋 {self.name} used "+colored(" Precipice Blades","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Ground"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,120,a,b,c,r,al)         
def oblivionwing(self,other):
    al=1
    r=randroll()
    print(f" 🦅 {self.name} used "+colored(" Oblivion Wing","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Flying"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=special(self,self.level,self.spatk,other.spdef,80,a,b,c,r,al)    
    if a!=0 and self.hp!=self.maxhp:
        print(f" {other.name} had its energy drained!")
    if dmg>other.hp:
        dmg=other.hp
        other.hp-=dmg
    else:
        other.hp-=dmg
    heal=dmg*0.75
    if other.ability=="Liquid Ooze" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"]:
        print(f" 🤢 {other.name}'s Liquid Ooze!")
        heal=-heal
    if self.hp<=(self.maxhp-heal):
        if self.item=="Big Root":
            self.hp+=heal*1.3
        else:
            self.hp+=heal
    else:
        self.hp=self.maxhp 
def gigadrain(self,other):
    al=1
    r=randroll()
    print(f" 🌱 {self.name} used "+colored(" Giga Drain","green",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Grass"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=special(self,self.level,self.spatk,other.spdef,90,a,b,c,r,al)    
    if a!=0 and self.hp!=self.maxhp:
        print(f" {other.name} had its energy drained!")
    if dmg>other.hp:
        dmg=other.hp
        other.hp-=dmg
    else:
        other.hp-=dmg
    heal=dmg/2
    if other.ability=="Liquid Ooze" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"]:
        print(f" 🤢 {other.name}'s Liquid Ooze!")
        heal=-heal
    if self.hp<=(self.maxhp-heal):
        if self.item=="Big Root":
            self.hp+=heal*1.3
        else:
            self.hp+=heal
    else:
        self.hp=self.maxhp           
def dreameater(self,other):
    al=1
    r=randroll()
    print(f" 💭 {self.name} used "+colored(" Dream Eater","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Psychic"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    if other.status=="Sleep":
        dmg=special(self,self.level,self.spatk,other.spdef,100,a,b,c,r,al)    
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
def relicsong(self,other,turn):
    al=1
    r=randroll()
    print(f" 🎶 {self.name} used "+colored(" Relic Song","green",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Normal"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=special(self,self.level,self.spatk,other.spdef,75,a,b,c,r,al)            
    other.hp-=dmg
    sleep(self,other,10,turn)

def leechlife(self,other):
    al=1
    r=randroll()
    print(f" 🦟 {self.name} used "+colored(" Leech Life","green",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Bug"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=special(self,self.level,self.spatk,other.spdef,80,a,b,c,r,al)    
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
def ragingbull(self,other):
    w=weathereff(self,other)
    al=1
    r=randroll()
    self.atktype=self.type2
    color="white"
    if self.atktype=="Water":
        color="blue"
    if self.atktype=="Fire":
        color="red"
    print(f" 🐂 {self.name} used "+colored(" Raging Bull",f"{color}",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=physical(self,self.level,self.atk,other.defense,90,a,b,c,r,al,w)         
def revelationdance(self,other):
    w=weathereff(self,other)
    al=1
    r=randroll()
    print(f" 🐦 {self.name} used "+colored(" Revelation Dance","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype=self.type1
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,100,a,b,c,r,al,w)     
def whirlpool(self,other,turn):
    al=1
    r=randroll()
    print(f" 🌪️ {self.name} used "+colored(" Whirlpool","blue",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Water"
    w=weathereff(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,35,a,b,c,r,al,w)    
    if other.whirlpool==False:
        other.whirlpool=turn+random.randint(2,5)
        print(f" {other.name} was trapped in a whirlpool.")
def firespin(self,other,turn):
    al=1
    r=randroll()
    print(f" 🔥 {self.name} used "+colored(" Fire Spin","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Fire"
    w=weathereff(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,35,a,b,c,r,al,w)    
    if other.firespin==False:
        other.firespin=turn+random.randint(2,5)
        print(f" {other.name} was trapped in a vortex of fire.")    
def infestation (self,other,turn):
    al=1
    r=randroll()
    print(f" 🦗 {self.name} used "+colored(" Infestation","blue",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Bug"
    w=weathereff(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,35,a,b,c,r,al,w)    
    if other.infestation==False:
        other.infestation=turn+random.randint(2,5)
        print(f" {other.name} is being infested.")            
def surf(self,other):
    al=1
    r=randroll()
    print(f" 🌊 {self.name} used "+colored(" Surf","blue",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Water"
    w=weathereff(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,90,a,b,c,r,al,w)  
    if self.ability=="Gulp Missile":
        x=""
        if self.hp<=(self.maxhp/2):
            x="Pikachu"
        if self.hp>(self.maxhp/2):
            x="Arrocuda"
        self.ability+=f"-{x}"
        print(f" 🐦 {self.name} caught a {x}!")
def muddywater(self,other):
    al=1
    r=randroll()
    print(f" 🌊 {self.name} used "+colored(" Muddy Water","blue",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Water"
    w=weathereff(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,80,a,b,c,r,al,w)      
def dracometeor(self,other):
    al=1
    r=randroll()
    print(f" 🐉☄️ {self.name} used "+colored(" Draco Meteor","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Dragon"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,130,a,b,c,r,al)  
    if a!=0:
        spatkchange(self,self,-1)
        
def originpulse(self,other):
    al=1
    self.atktype="Water"
    w=weathereff(self,other)
    r=randroll()
    print(f" 🐋🌊 {self.name} used "+colored(" Origin Pulse","blue",attrs=["bold"])+"!")
    if self.ability=="Mega Launcher":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,120,a,b,c,r,al,w)          
def apower(self,other):
    al=1
    r=randroll()
    print(f" 🪨 {self.name} used "+colored(" Ancient Power","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Rock"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,90,a,b,c,r,al) 
    chance=10
    if self.ability=="Serene Grace":
        chance*=2
    if self.speed>other.speed:
        ch=random.randint(1,100)            
        if ch>(100-chance):
            atkchange(self,other,0.5)
            defchange(self,other,0.5)
            spatkchange(self,other,0.5)
            spdefchange(self,other,0.5)
            speedchange(self,other,0.5)
            print(f" {self.name} got an omniboost!")
            
def noretreat(self,other):
    print(f" ⚔️ {self.name} used "+colored(" No Retreat","red",attrs=["bold"])+"!")
    atkchange(self,other,0.5)
    defchange(self,other,0.5)
    spatkchange(self,other,0.5)
    spdefchange(self,other,0.5)
    speedchange(self,other,0.5)
    print(f" {self.name}'s gained an omniboost but it cannot escape!")
    self.trap=True
def octolock(self,other):
    print(f" 🐙 {self.name} used "+colored(" Octolock","red",attrs=["bold"])+"!")  
    if other.olock is False:
        other.olock=True
def octazooka(self,other):
    self.atktype="Water"
    w=weathereff(self,other)
    al=1
    r=randroll()
    print(f" 🐙 {self.name} used "+colored(" Octazooka","blue",attrs=["bold"])+"!")
    if self.ability=="Mega Launcher":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    c=isCrit(self,other,2)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,80,a,b,c,r,al,w)       
    speedchange(other,self,-0.5)
        
def scald(self,other):
    self.atktype="Water"
    w=weathereff(self,other)
    al=1
    r=randroll()
    print(f" 💦🔥 {self.name} used "+colored(" Scald","blue",attrs=["bold"])+"!")
    c=isCrit(self,other)    
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,80,a,b,c,r,al,w)            
    burn(self,other,30)
def hydrosteam(self,other):
    self.atktype="Water"
    al=1
    r=randroll()
    print(f" 🌊 {self.name} used "+colored(" Hydro Steam","blue",attrs=["bold"])+"!")
    if field.weather in ["Rainy","Primordial Sea","Sunny"]:
        al*=1.5
    c=isCrit(self,other)    
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,80,a,b,c,r,al)        
def scorchingsands(self,other):
    self.atktype="Ground"
    al=1
    r=randroll()
    print(f" 🏜️ {self.name} used "+colored(" Scorching Sands","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,90,a,b,c,r,al)            
    burn(self,other,30)
      
def doomdesire(self,other):
    al=1
    r=randroll()
    print(f" 🌟 {self.name} used "+colored(" Doom Desire","yellow",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Steel"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,140,a,b,c,r,al)        
def fleurcannon(self,other):
    al=1
    r=randroll()
    print(f" 🤖 {self.name} used "+colored(" Fleur Cannon","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Fairy"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,130,a,b,c,r,al)        
    spdefchange(self,self,-1)
        
def flashcannon(self,other):
    al=1
    r=randroll()
    print(f" {self.name} used "+colored(" Flash Cannon","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    if self.ability=="Mega Launcher":
        al=1.5
        print(f" {self.name}'s {self.ability}.")
    self.atktype="Steel"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,90,a,b,c,r,al) 
    chance=30
    if self.ability=="Serene Grace":
        chance*=2
    if self.speed>other.speed:
        ch=random.randint(1,100)            
        if ch>(100-chance):
            spdefchange(other,self,-0.5)
            
def psychoboost(self,other):
    al=1
    r=randroll()
    print(f" 🔮 {self.name} used "+colored(" Psycho Boost","magenta",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Psychic"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,140,a,b,c,r,al)       
    if a!=0:
        spatkchange(self,self,-1)
        
def victorydance(self,other):
    print(f" ✌🏻 {self.name} used Victory Dance.")
    atkchange(self,other,0.5)
    defchange(self,other,0.5)
    speedchange(self,other,0.5)
def takeheart(self,other):
    print(f" 💝 {self.name} used Take Heart.")
    atkchange(self,other,0.5)
    defchange(self,other,0.5)
    spatkchange(self,other,0.5)
    spdefchange(self,other,0.5)
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
    self.pplist=[5,5,5,5]
    self.name=self.name+f"({other.name})"
def seismictoss(self,other):
    if other.type1!="Ghost" and other.type2!="Ghost":
        print(f" {self.name} used "+colored(" Seismic Toss","red",attrs=["bold"])+"!")
        other.hp-=self.level
    else:
        print(f" {self.name} used "+colored(" Seismic Toss","red",attrs=["bold"])+"!")
        print(f" 🔴 Doesn't effect on {other.name}!")
def nightshade(self,other):
    if other.type1!="Normal" and other.type2!="Normal":
        print(f" 👤 {self.name} used "+colored(" Night Shade","magenta",attrs=["bold"])+"!")
        other.hp-=self.level
    else:
        print(f" 🔴 Doesn't effect on {other.name}!")        
def flamethrower (self,other):
    self.atktype="Fire"
    w=weathereff(self,other)
    al=1
    r=randroll()
    if self.ability=="Sheer Force":
        al=1.5
        print(f" ⚜️ {self.name}'s {self.ability}.")
    print(f" 🔥 {self.name} used "+colored(" Flamethrower","red",attrs=["bold"])+"!")
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,90,a,b,c,r,al,w)        
    burn(self,other,10)
      
def solarbeam(self,other):
    al=1
    w=1
    r=randroll()
    if field.weather=="Sandstorm":
        w*=0.5
    if self.item=="Power Herb":
        self.item+="[Used]"
        print(f" {self.name} became fully charged due to its Power Herb.")
        self.precharge=True
    if (field.weather in ["Sunny","Desolate Land"]) or self.precharge is True:
        print(f" ☀️ {self.name} used "+colored(" Solar Beam","green",attrs=["bold"])+"!")
        c=isCrit(self,other)
        self.atktype="Grass"
        ab=weakness(self,other,field)
        a=ab[0]
        b=ab[1]   
        other.hp-=special(self,self.level,self.spatk,other.spdef,120,a,b,c,r,al,w)         
        self.precharge=False
    elif self.precharge is False:
        print(f" 🌤️ {self.name} is absorbing sunlight!")
        self.precharge=True
def solarblade(self,other):
    al=1
    w=1
    r=randroll()
    if self.item=="Power Herb":
        self.item+="[Used]"
        print(f" {self.name} became fully charged due to its Power Herb.")
        self.precharge=True
    if (field.weather in ["Sunny","Desolate Land"]) or self.precharge is True:
        print(f" ☀️🗡️ {self.name} used "+colored(" Solar Blade","green",attrs=["bold"])+"!")
        c=isCrit(self,other)
        self.atktype="Grass"
        ab=weakness(self,other,field)
        a=ab[0]
        b=ab[1]   
        other.hp-=physical(self,self.level,self.atk,other.defense,125,a,b,c,r,al,w)         
        self.precharge=False
    elif self.precharge is False:
        print(f" 🌤️ {self.name} is absorbing sunlight!")
        self.precharge=True    
def terablast(self,other):
    if True:
        typ="💎"
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
            typ="🥊"
            color="red"
        if self.teratype=="Dark":
            typ="👿"
            color="red"
        if self.teratype=="Fairy":
            typ="❤️"
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
            typ="🏛️"
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
        print(f" {typ} {self.name} used "+colored(" Tera Blast",f"{color}",attrs=["bold"])+"!")
    self.atktype=self.teratype
    if self.atktype==None:
        self.atktype="Normal"
    w=weathereff(self,other)
    al=1
    r=randroll()
    c=isCrit(self,other)
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]
    if self.atk>self.spatk:
        other.hp-=physical(self,self.level,self.atk,other.defense,80,a,b,c,r,al,w)
    if self.spatk>self.atk:
        other.hp-=special(self,self.level,self.spatk,other.spdef,80,a,b,c,r,al,w)                 
def hiddenpower(self,other):
    al=1
    r=randroll()
    x=hidp(self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv)
    base=x[0]
    if self.maxiv=="Yes":
        self.maxiv=random.choice(["Rock","Fire","Water","Grass","Electric","Ground","Flying","Fighting","Fairy","Dragon","Steel","Poison","Dark","Ghost","Normal","Bug","Ice"])
    if self.maxiv!="Yes":
        self.atktype=x[1]
    if self.maxiv in ["Rock","Fire","Water","Grass","Electric","Ground","Flying","Fighting","Fairy","Dragon","Steel","Poison","Dark","Ghost","Normal","Bug","Ice"]:
        self.atktype=self.maxiv
    w=weathereff(self,other)
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
    print(f" ❇️ {self.name} used "+colored(f" Hidden Power","white",attrs=["bold"])+"!")
    c=isCrit(self,other)    
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    other.hp-=special(self,self.level,self.spatk,other.spdef,base,a,b,c,r,al,w)
    
    
def special(self,level,spatk,spdef,base,a=1,b=1,c=1,r=1,al=1,w=1):
    self.atkcat="Special"
    dmg=round((((2*level + 10)/250)*(spatk/spdef)*base+2)*a*b*c*r*al*w)
    return dmg
def physical(self,level,atk,defense,base,a=1,b=1,c=1,r=1,al=1,w=1):
    self.atkcat="Physical"
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

def weathereff(mon,mon2):
    if field.weather=="Desolate Land" and mon.atktype=="Water" and "Cloud Nine" not in (mon.ability,mon2.ability):
        print(colored(" 🌋 The Water-type attack evaporated in the harsh sunlight!!","red",attrs=["bold"]))
        return 0
    if field.weather=="Primordial Sea" and mon.atktype=="Fire" and "Cloud Nine" not in (mon.ability,mon2.ability):
        print(colored(" 🌊 The Fire-type attack fizzled out in the heavy rain!!","blue",attrs=["bold"]))
        return 0                                 
    if field.weather in ["Rainy","Primordial Sea"] and mon.atktype=="Water" and "Cloud Nine" not in (mon.ability,mon2.ability):
        print(" 🌧️ Rain boosted!")
        return 1.5
    if (field.weather=="Sunny") and mon.atktype=="Water" and "Cloud Nine" not in (mon.ability,mon2.ability):
        print(" ☀️ Sun weakened!")
        return 0.5    
    if (field.weather=="Rainy") and mon.atktype=="Fire" and "Cloud Nine" not in (mon.ability,mon2.ability):
        print(" 🌧️ Rain weakened!")
        return 0.5      
    if field.weather in ["Sunny" ,"Desolate Land"] and mon.atktype=="Fire" and "Cloud Nine" not in (mon.ability,mon2.ability):
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
        