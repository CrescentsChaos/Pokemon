import random
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
    if (chance>=miss and ("Steel" not in (other.type2,other.type1,other.teratype) and "Poison"  not in (other.type2,other.type1,other.teratype) or self.ability=="Corrosion") and other.ability not in ["Immunity","Magic Bounce","Leaf Guard","Comatose"] and other.status=="Alive" and self.ability!="Sheer Force") and other.hp>0:
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
        print(f" ⚡ {self.name} was badly poisoned.")        
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
    if chance>=miss and "Fire" not in (other.type2,other.type1,other.teratype) and other.ability not in ["Flash Fire","Magic Bounce","Leaf Guard","Comatose"] and other.status=="Alive" and self.ability!="Sheer Force" and other.hp>0:
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
    if chance>=miss and "Grass" not in (other.type2,other.type1,other.teratype) and other.ability not in ["Safety Googles","Magic Bounce","Leaf Guard","Comatose","Vital Spirit","Insomnia"] and other.status=="Alive" and self.ability!="Sheer Force" and other.hp>0:
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