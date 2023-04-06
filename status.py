import random
from movelist import *
from typematchup import *
#CONFUSE
def confuse(self,other,turn,ch=100):
    miss=100-ch
    if self.ability=="Serene Grace":
        miss/=2
    chance=random.randint(1,100)
    if chance>=miss and other.confused is False and self.ability!="Sheer Force" and other.ability not in ["Own Tempo"] and other.status!="Sleep":
        print(f" 😕 {other.name} became confused!")
        other.confused=True
        other.confuseendturn=turn+random.randint(2,5)
#FLINCH        
def flinch(self,other,ch=100):
    miss=100-ch
    if self.ability=="Serene Grace":
        miss/=2
    chance=random.randint(1,100)
    if (chance>=miss and other.ability not in ["Inner Focus"] and self.ability!="Sheer Force") and other.hp>0:
        if miss==0  and (other.item!="Covert Cloak" or other.ability not in ["Shield Dust"]):
            other.flinched=True  
#POISON
def poison(self,other,ch=100):
    miss=100-ch
    if self.ability=="Serene Grace":
        miss/=2
    chance=random.randint(1,100)
    if (chance>=miss and ("Steel" not in (other.type2,other.type1,other.teratype) and "Poison"  not in (other.type2,other.type1,other.teratype) or self.ability=="Corrosion") and other.ability not in ["Immunity","Magic Bounce","Leaf Guard","Comatose","Pastel Veil"] and other.status=="Alive" and self.ability!="Sheer Force") and other.hp>0:
        if other.item!="Covert Cloak" or other.ability not in ["Shield Dust"]:
            other.status="Badly Poisoned"
            print(f" ☠️ {other.name} was badly poisoned.")
    if chance>=miss and other.status=="Badly Poisoned" and other.ability in ["Synchronize"] and self.status=="Alive":
        self.status="Badly Poisoned"
        print(f" {other.name}'s {other.ability}!")
        print(f" ☠️ {self.name} was badly poisoned!")
    if chance>=miss and other.ability in ["Magic Bounce"] and self.status=="Alive" and other.status!="Badly Poisoned":
        self.status="Badly Poisoned"
        print(f" {other.name}'s {other.ability}!")
        print(f" ☠️ {self.name} was badly poisoned!")        
#PARALYZED        
def paralyzed(self,other,ch=100):
    miss=100-ch
    if self.ability=="Serene Grace":
        miss/=2
    chance=random.randint(1,100)
    if chance>=miss and (((("Electric" not in (other.type2,other.type1,other.teratype) and "Ground" not in (other.type2,other.type1,other.teratype) or other.use in ["Body Slam","Force Plam","Glare","Lightning Rod","Volt Absorb"] and other.ability not in ["Limber","Leaf Guard","Comatose","Magic Bounce"])) and other.status=="Alive" and self.ability!="Sheer Force") and other.hp>0):
        if other.item!="Covert Cloak" or other.ability not in ["Shield Dust"]:
            other.status="Paralyzed"
            print(f" ⚡ {other.name} was paralyzed!")
    if chance>=miss and other.status=="Paralyzed" and other.ability in ["Synchronize"] and self.status=="Alive":
        self.status="Paralyzed"
        print(f" {other.name}'s {other.ability}!")
        print(f" ⚡ {self.name} was paralayzed.")        
    if chance>=miss and other.ability in ["Magic Bounce"] and self.status=="Alive" and other.status!="Paralyzed":
        self.status="Paralyzed"
        print(f" {other.name}'s {other.ability}!")
        print(f" ⚡ {self.name} was badly poisoned.")        
#Burned
def burn(self,other,ch=100):
    miss=100-ch
    if self.ability=="Serene Grace":
        miss/=2
    chance=random.randint(1,100)
    if chance>=miss and "Fire" not in (other.type2,other.type1,other.teratype) and other.ability not in ["Flash Fire","Magic Bounce","Leaf Guard","Comatose","Thermal Exchange","Magma Armor","Water Veil"] and other.status=="Alive" and self.ability!="Sheer Force" and other.hp>0:
        if other.item!="Covert Cloak" or other.ability not in ["Shield Dust"]:
            other.status="Burned"
            print(f" 🔥 {other.name} was burned.")
    if chance>=miss and other.status=="Burned" and other.ability in ["Synchronize"] and self.status=="Alive":
        self.status="Burned"
        print(f" {other.name}'s {other.ability}!")
        print(f" 🔥 {self.name} was burned!")  
    if chance>=miss and other.ability in ["Magic Bounce"] and self.status=="Alive" and other.status!="Burned":
        self.status="Burned"
        print(f" {other.name}'s {other.ability}!")
        print(f" 🔥 {self.name} was burned!")        
#sleep
def sleep(self,other,ch,turn):
    miss=100-ch
    if self.ability=="Serene Grace":
        miss/=2
    chance=random.randint(1,100)
    if chance>=miss and "Grass" not in (other.type2,other.type1,other.teratype) and other.ability not in ["Magic Bounce","Leaf Guard","Comatose","Vital Spirit","Insomnia"] and other.status=="Alive" and self.ability!="Sheer Force" and other.hp>0:
        if other.item!="Covert Cloak" or other.ability not in ["Shield Dust"]:
            other.status="Sleep"
            print(f" 💤 {other.name} fell asleep!")
            if other.ability=="Early Bird":
                other.sleependturn=turn+random.randint(2,3)
            if other.ability!="Early Bird":
                other.sleependturn=turn+random.randint(2,5)
    if chance>=miss and other.status=="Sleep" and other.ability in ["Synchronize"] and self.status=="Alive":
        self.status="Sleep"
        print(f" {other.name}'s {other.ability}!")
        print(f" 💤 {self.name} fell asleep!")
        if self.ability=="Early Bird":
            self.sleependturn=turn+random.randint(2,3)
        if self.ability!="Early Bird":
            self.sleependturn=turn+random.randint(2,5)   
    if chance>=miss and other.ability in ["Magic Bounce"] and self.status=="Alive" and other.status!="Sleep":
        self.status="Sleep"
        print(f" {other.name}'s {other.ability}!")
        print(f" 💤 {self.name} fell asleep!")
        if self.ability=="Early Bird":
            self.sleependturn=turn+random.randint(2,3)
        if self.ability!="Early Bird":
            self.sleependturn=turn+random.randint(2,5)
            
def berry(other,self,item,before,turn):
    if other.item=="Maranga Berry" and other.atkcat=="Special" and self.hp!=sbefore:
          if other.ability=="Cheek Pouch" and other.hp<other.maxhp:
                print(f" {other.name}'s Cheek Pouch!")
                other.hp+=(other.maxhp/3)
          print(colored(f" 🍍 {other.item} raised {other.name}'s special defense!!","yellow"))
          n=0.5
          if other.ability=="Ripen":
              n=1
          spdefchange(other,self,n)
          other.item+="[Used]"
    if self.use not in typemoves.statusmove:
        if other.item=="Jaboca Berry" and other.atkcat=="Physical" and self.hp!=sbefore:
            if other.ability=="Cheek Pouch" and other.hp<other.maxhp:
                print(f" {other.name}'s Cheek Pouch!")
                other.hp+=(other.maxhp/3)
            print(colored(f" 🍇 {other.name}'s {other.item} damaged {self.name}!!","yellow"))
            self.hp-=round(self.maxhp/8)
            other.item+="[Used]"
        if other.item=="Rowap Berry" and other.atkcat=="Special" and self.hp!=sbefore:
            if other.ability=="Cheek Pouch" and other.hp<other.maxhp:
                print(f" {other.name}'s Cheek Pouch!")
                other.hp+=(other.maxhp/3)
            print(colored(f" 🫐 {other.name}'s {other.item} damaged {self.name}!!","cyan"))
            self.hp-=(other.maxhp/8)
            other.item+="[Used]"
        if other.item=="Kee Berry" and self.ability not in ["Unnerve","As One"]:
            if other.ability=="Cheek Pouch" and other.hp<other.maxhp:
                print(f" {other.name}'s Cheek Pouch!")
                other.hp+=(other.maxhp/3)
            print(colored(f" 🍑 {other.item} raised {other.name}'s defense!!","red"))
            n=0.5
            if other.ability=="Ripen":
                n=1
            defchange(other,self,n)
            other.item+="[Used]"
    if (other.hp<=(other.maxhp/4)  and before>(other.maxhp/4)) or (other.ability=="Gluttony" and other.hp<=(other.maxhp/2) and before>(other.maxhp/2)):
        if other.item=="Liechi Berry" and self.ability not in ["Unnerve","As One"]:
              if other.ability=="Cheek Pouch" and other.hp<other.maxhp:
                  print(f" {other.name}'s Cheek Pouch!")
                  other.hp+=(other.maxhp/3)
              print(colored(f" 🍓 {other.item} raised {other.name}'s attack!!","yellow"))
              n=0.5
              if other.ability=="Ripen":
                  n=1
              atkchange(other,self,n)
              other.item+="[Used]"
        if other.item=="Petaya Berry" and self.ability not in ["Unnerve","As One"]:
              if other.ability=="Cheek Pouch" and other.hp<other.maxhp:
                  print(f" {other.name}'s Cheek Pouch!")
                  other.hp+=(other.maxhp/3)
              print(colored(f" 🌰 {other.item} raised {other.name}'s special attack!!","red"))
              n=0.5
              if other.ability=="Ripen":
                  n=1
              spatkchange(other,self,n)
              other.item+="[Used]"
        if other.item=="Salac Berry" and self.ability not in ["Unnerve","As One"]:
              if other.ability=="Cheek Pouch" and other.hp<other.maxhp:
                  print(f" {other.name}'s Cheek Pouch!")
                  other.hp+=(other.maxhp/3)
              print(colored(f" 🥬 {other.item} raised {other.name}'s speed!!","green"))
              n=0.5
              if other.ability=="Ripen":
                  n=1
              speedchange(other,self,n)
              other.item+="[Used]"
        if other.item=="Custap Berry" and other.speed<self.speed:
              if other.ability=="Cheek Pouch" and other.hp<other.maxhp:
                  print(f" {other.name}'s Cheek Pouch!")
                  other.hp+=(other.maxhp/3)
              print(colored(f" 🥝 {other.item} will let {other.name} move first!!","red"))
              other.priority=True
              other.item+="[Used]"
        if other.item=="Starf Berry" and self.ability not in ["Unnerve","As One"]:
              if other.ability=="Cheek Pouch" and other.hp<other.maxhp:
                  print(f" {other.name}'s Cheek Pouch!")
                  other.hp+=(other.maxhp/3)
              ss=random.randint(1,5)
              n=1
              if other.ability=="Ripen":
                  n=2
              if ss==1:
                  print(colored(f" 🌟 {other.item} sharply raised {other.name}'s attack!!","green"))
                  atkchange(other,self,n)
              if ss==2:
                  print(colored(f" 🌟 {other.item} sharply raised {other.name}'s special attack!!","green"))
                  spatkchange(other,self,n)
              if ss==3:
                  print(colored(f" 🌟 {other.item} sharply raised {other.name}'s defense!!","green"))
                  defchange(other,self,n)
              if ss==4:
                  print(colored(f" 🌟 {other.item} sharply raised {other.name}'s special defense!!","green"))
                  spdefchange(other,self,n)
              if ss==5:
                  print(colored(f" 🌟 {other.item} sharply raised {other.name}'s speed!!","green"))
                  speedchange(other,self,n)
              other.item+="[Used]"
        if other.item in ["Aguav Berry","Figy Berry","Ipapa Berry","Mago Berry","Wiki Berry"]:
                other.hp+=round(other.maxhp/3)
                print(colored(f" {other.name} consumed it's {other.item} and restored some HP!","green"))
                if other.item=="Wiki Berry" and self.ability not in ["Unnerve","As One"]:
                    if other.nature in ["Adamant","Jolly","Careful","Impish"]:
                        confuse(other,other,turn,100)
                if other.item=="Ipapa Berry" and self.ability not in ["Unnerve","As One"]:
                    if other.nature in ["Lonely","Mild","Gentle","Hasty"]:
                        confuse(other,other,turn,100)
                if other.item=="Aguav Berry" and self.ability not in ["Unnerve","As One"]:
                    if other.nature in ["Naughty","Naive","Rash","Lax"]:
                        confuse(other,other,turn,100)
                if other.item=="Mago Berry" and self.ability not in ["Unnerve","As One"]:
                    if other.nature in ["Brave","Quiet","Sassy","Relaxed"]:
                        confuse(other,other,turn,100)
                if other.item=="Figy Berry" and self.ability not in ["Unnerve","As One"]:
                    if other.nature in ["Modest","Timid","Calm","Bold"]:
                        confuse(other,other,turn,100)
                other.item+="[Used]"                                                     