from colorama import init
from sty import fg, bg, ef, rs
from termcolor import colored
from pokemonbase import *
from pokemonintros import *
from status import *
import climage              
def lastresort(self,other):
    al=1
    r=randroll()
    print(f"  {fg(self.color)+self.name+fg.rs} used "+colored("Last Resort","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Normal"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    dmg=physical(self,self.level,self.atk,other.defense,140,a,b,c,r,al)   
    other.hp-=dmg     
def focuspunch(self,other):
    if self.item=="Power Herb" or self.focus==True:
        if self.item=="Power Herb":
            itemicon(self.item)
            self.item+="[Used]"
            print(f"  {fg(self.color)+self.name+fg.rs} became fully charged due to its Power Herb.")
        al=1
        r=randroll()
        print(f" 👊  {fg(self.color)+self.name+fg.rs} used "+colored("Focus Punch","red",attrs=["bold"])+"!")
        c=isCrit(self,other,2)
        self.atktype="Fighting"
        ab=weakness(self,other,field)
        a=ab[0]
        b=ab[1]   
        other.hp-=physical(self,self.level,self.atk,other.defense,150,a,b,c,r,al)    
        self.focus=False  
    elif self.focus==False:
        print(f" 🤨  {fg(self.color)+self.name+fg.rs} tightening its focus!")
        self.focus=True       
def present(self,other):
    al=1
    r=randroll()
    print(f" 🎁  {fg(self.color)+self.name+fg.rs} used "+colored("Present","white",attrs=["bold"])+"!")
    c=isCrit(self,other)
    self.atktype="Normal"
    ab=weakness(self,other,field)
    a=ab[0]
    b=ab[1]   
    base=0
    ch=random.choices([1,2,3,4], weights=[40,30,10,20],k=1)[0]
    if ch==1:
        if other.hp!=other.maxhp:
            print(f"  {fg(self.color)+self.name+fg.rs}'s present healed {other.name}!")
            other.hp+=(other.maxhp/4)
    if ch==3:
        print(f"  {fg(self.color)+self.name+fg.rs}'s present damaged {other.name}!")
        base=120
    if ch==2:
        print(f"  {fg(self.color)+self.name+fg.rs}'s present damaged {other.name}!")
        base=80
    if ch==1:
        print(f"  {fg(self.color)+self.name+fg.rs}'s present damaged {other.name}!")
        base=40
    other.hp-=physical(self,self.level,self.atk,other.defense,base,a,b,c,r,al)     
def octolock(self,other):
    print(f" 🐙  {fg(self.color)+self.name+fg.rs} used "+colored("Octolock","red",attrs=["bold"])+"!")  
    if other.olock is False:
        other.olock=True
def takeheart(self,other):
    print(f" 💝  {fg(self.color)+self.name+fg.rs} used Take Heart.")
    atkchange(self,other,0.5)
    defchange(self,other,0.5)
    spatkchange(self,other,0.5)
    spdefchange(self,other,0.5)
def heartswap(self,other):
    print(f" 💞  {fg(self.color)+self.name+fg.rs} used Heart Swap.")
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
    print(f"  {fg(self.color)+self.name+fg.rs} swapped it's stat changes with {other.name}.")
def transform(self,other):
    print(f' 👥  {fg(self.color)+self.name+fg.rs} used Transform!')
    if other.dmax is False and other.item not in megastones:
        print(f' 👥  {fg(self.color)+self.name+fg.rs} transformed into {other.name}')
        self.maxhp=other.maxhp
        self.sprite=other.sprite
        self.maxatk=other.maxatk
        self.maxdef=other.maxdef
        self.maxspatk=other.maxspatk
        self.maxspdef=other.maxspdef
        self.maxspeed=other.maxspeed    
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
        self.atk=self.maxatk*self.atkb
        self.defense=self.maxdef*self.defb
        self.spatk=self.maxspatk*self.spatkb
        self.spdef=self.maxspdef*self.spdefb
        self.speed=self.maxspeed*self.speedb