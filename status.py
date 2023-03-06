import random
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
    if (chance>=miss and ("Steel" not in (other.type2,other.type1,other.teratype) and "Poison"  not in (other.type2,other.type1,other.teratype) or self.ability=="Corrosion") and other.ability not in ["Immunity","Magic Bounce","Leaf Guard","Comatose"] and other.status=="Alive" and self.ability!="Sheer Force") and other.hp>0:
        if miss==0  and (other.item!="Covert Cloak" or other.ability not in ["Shield Dust"]):
            other.status="Badly Poisoned"
            print(f" ☠️ {other.name} was badly poisoned.")
    if chance<=miss and other.status=="Badly Poisoned" and other.ability in ["Synchronize","Magic Bounce"] and self.status=="Alive":
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
        if miss==0  and (other.item!="Covert Cloak" or other.ability not in ["Shield Dust"]):
            other.status="Paralyzed"
            print(f" ⚡ {other.name} was paralyzed!")
    if chance<=miss and other.status=="Paralyzed" and other.ability in ["Synchronize","Magic Bounce"] and self.status=="Alive":
        self.status="Paralyzed"
        print(f" {other.name}'s {other.ability}!")
        print(f" ⚡ {self.name} was badly poisoned.")        