#pylint:disable=C0116
import random
#from pokemons import Pokemon
def weakness(self,other):
    eff=1
    stab=1     
    #BUG
    bugeff=['Grass', 'Psychic', 'Dark']
    bugwk=['Fighting', 'Flying', 'Poison', 'Ghost', 'Steel', 'Fire', 'Fairy']
    #water
    watereff=['Ground', 'Rock', 'Fire']
    waterwk=['Water', 'Grass', 'Dragon']
    #Ghost
    ghosteff=['Ghost', 'Psychic']
    ghostwk=["Dark"]
    ghostimmune=["Normal"]
    #Electric
    electriceff=['Flying', 'Water']
    electricimmune=["Ground"]
    electricwk=['Grass', 'Electric', 'Dragon']
    #Psychic
    psychiceff=['Fighting', 'Poison']
    psychicimmune=["Dark"]
    psychicwk=['Steel', 'Psychic']
    #Ice
    iceeff=['Flying', 'Ground', 'Grass', 'Dragon']
    icewk=['Steel', 'Fire', 'Water', 'Ice']
    #Dragon
    dragonimmune=["Fairy"]
    dragoneff=["Dragon"]
    dragonwk=["Steel"]
    #Fairy
    fairyeff=['Fighting', 'Dragon', 'Dark']
    fairywk=['Poison', 'Steel', 'Fire']
    #Dark
    darkeff=['Ghost', 'Psychic']
    darkwk=['Fighting', 'Dark', 'Fairy']
    #Steel
    steeleff=['Rock', 'Ice', 'Fairy']
    steelwk=['Steel', 'Fire', 'Water', 'Electric']
    #GRASS      
    grasseff=["Ground", "Rock", "Water"]
    grasswk=["Flying", "Poison", "Bug", "Steel", "Fire", "Grass", "Dragon"]
    #FIRE
    fireeff=["Bug", "Steel", "Grass", "Ice"]
    firewk=["Rock", "Fire", "Water", "Dragon"]
    #POISON
    poisoneff=["Grass", "Fairy"]
    poisonwk=["Poison", "Ground", "Rock", "Ghost"]
    poisonimmune=["Steel"]
    #FLYING
    flyingeff=["Fighting", "Bug", "Grass"]
    flyingwk=['Rock', 'Steel', 'Electric']    
    #Rock
    rockeff=["Flying", "Bug", "Fire", "Ice"]
    rockwk=['Fighting', 'Ground', 'Steel']
    #Normal
    normaleff=[]
    normalwk=['Rock', 'Steel']
    normalimmune=['Ghost']
    #fighting
    fightingeff=['Normal', 'Rock', 'Steel', 'Ice', "Dark"]
    fightingwk=["Flying", 'Poison', 'Psychic', 'Bug','Fairy']
    fightingimmune=["Ghost"]
    #ground
    groundeff=['Poison', 'Rock', 'Steel', 'Fire', 'Electric']
    groundwk=['Bug', 'Grass']
    groundimmune=["Flying"]
    #MATCHUP)
    #ghost
    if self.atktype=="Ghost":
        if other.type1 in ghosteff:
            eff*=2
        if other.type2 in ghosteff:
            eff*=2
        if other.type1 in ghostwk:
            eff/=2
        if other.type2 in ghostwk:
            eff/=2
        if other.type1 in ghostimmune or other.type2 in ghostimmune:
            eff*=0
            
        else:
            eff*=1 
    #electric
    if self.atktype=="Electric":
        if other.ability=="Lightning Rod":
            print(f"{other.name}'s {other.ability}.")
            eff*=0
        if other.ability=="Volt Absorb":
            print(f"{other.name}'s {other.ability}.")
            other.hp+=(other.maxhp/4)
            eff*=0
        if other.type1 in electriceff:
            eff*=2
        if other.type2 in electriceff:
            eff*=2
        if other.type1 in electricwk:
            eff/=2
        if other.type2 in electricwk:
            eff/=2
        if other.type1 in electricimmune or other.type2 in electricimmune:
            eff*=0
        else:
            eff*=1 
    
    #psychic
    if self.atktype=="Psychic":
        if other.type1 in psychiceff:
            eff*=2
        if other.type2 in psychiceff:
            eff*=2
        if other.type1 in psychicwk:
            eff/=2
        if other.type2 in psychicwk:
            eff/=2
        if other.type1 in psychicimmune or other.type2 in psychicimmune:
            eff*=0
        else:
            eff*=1 
    #ice
    if self.atktype=="Ice":
        if other.type1 in iceeff:
            if other.ability=="Thick Fat":
                print(f"{other.name}'s {other.ability}.")
                eff*=1
            else:
                eff*=2
        if other.type2 in iceeff:
            eff*=2
        if other.type1 in icewk:
            eff/=2
        if other.type2 in icewk:
            eff/=2
       # if other.type1 in iceimmune or other.type2 in iceimmune:
           # eff*=0
        
        else:
            eff*=1 
    #fairy
    if self.atktype=="Fairy":
        if other.type1 in fairyeff:
            eff*=2
        if other.type2 in fairyeff:
            eff*=2
        if other.type1 in fairywk:
            eff/=2
        if other.type2 in fairywk:
            eff/=2
       # if other.type1 in fairyimmune or other.type2 in fairyimmune:
           # eff*=0
        else:
            eff*=1 
    #dark
    if self.atktype=="Dark":
        if other.type1 in darkeff:
            eff*=2
        if other.type2 in darkeff:
            eff*=2
        if other.type1 in darkwk:
            eff/=2
        if other.type2 in darkwk:
            eff/=2
       # if other.type1 in darkimmune or other.type2 in darkimmune:
           # eff*=0
        else:
            eff*=1 
    #steel
    if self.atktype=="Steel":
        if other.type1 in steeleff:
            eff*=2
        if other.type2 in steeleff:
            eff*=2
        if other.type1 in steelwk:
            eff/=2
        if other.type2 in steelwk:
            eff/=2
       # if other.type1 in steelimmune or other.type2 in steelimmune:
           # eff*=0
   
        else:
            eff*=1 
    #dragon
    if self.atktype=="Dragon":
        if other.type1 in dragoneff:
            eff*=2
        if other.type2 in dragoneff:
            eff*=2
        if other.type1 in dragonwk:
            eff/=2
        if other.type2 in dragonwk:
            eff/=2
        if other.type1 in dragonimmune or other.type2 in dragonimmune:
            eff*=0
        else:
            eff*=1 
    #bug
    if self.atktype=="Bug":
        if self.ability=="Swarm":
            if self.hp<=(self.maxhp/3):
                print(f"{self.name}'s {self.ability}.")
                eff*=2.25
        if other.type1 in bugeff:
            eff*=2
        if other.type2 in bugeff:
            eff*=2
        if other.type1 in bugwk:
            eff/=2
        if other.type2 in bugwk:
            eff/=2
       # if other.type1 in bugimmune or other.type2 in bugimmune:
           # eff*=0
        else:
            eff*=1 
    #Water
    if self.atktype=="Water":
        if other.ability in ["Storm Drain","Water Absorb"]:
            if other.ability=="Storm Drain":
                print(f"{other.name}'s {other.ability}.")
                spatkchange (other,0.5)
            eff*=0
            
        if self.ability=="Torrent":
            if self.hp<=(self.maxhp/3):
                print(f"{self.name}'s {self.ability}.")
                eff*=2.25
        if other.type1 in watereff:
            eff*=2
        if other.type2 in watereff:
            eff*=2
        if other.type1 in waterwk:
            eff/=2
        if other.type2 in waterwk:
            eff/=2
        if other.ability=="Solid Rock":
            print(f"{other.name}'s {other.ability}.")
            eff*=0.75
       # if other.type1 in waterimmune or other.type2 in waterimmune:
           # eff*=0
        else:
            eff*=1 
    #Ground
    if self.atktype=="Ground":
        if other.ability=="Levitate":
            print(f"{other.name}'s {other.ability}.")
            eff*=0
        if other.type1 in groundeff:
            eff*=2
        if other.type2 in groundeff:
            eff*=2
        if other.type1 in groundwk:
            eff/=2
        if other.type2 in groundwk:
            eff/=2
        if other.type1 in groundimmune or other.type2 in groundimmune:
            eff*=0
        else:
            eff*=1 
    #GRASS
    if self.atktype=="Grass":
        if self.ability=="Overgrow":
            if self.hp<=(self.maxhp/3):
                print(f"{self.name}'s {self.ability}.")
                eff*=2.25
        if other.type1 in grasseff:
            eff*=2
        if other.type2 in grasseff:
            eff*=2
        if other.type1 in grasswk:
            eff/=2
        if other.type2 in grasswk:
            eff/=2
    
        else:
            eff*=1
    #FLYING            
    if self.atktype=="Flying":
        if other.type1 in flyingeff:
            eff*=2
        if other.type2 in flyingeff:
            eff*=2
        if other.type1 in flyingwk:
            eff/=2
        if other.type2 in flyingwk:
            eff/=2
        else:
            eff*=1            
    #FIRE            
    if self.atktype=="Fire":
        if self.ability=="Blaze":
            if self.hp<=(self.maxhp/3):
                print(f"{self.name}'s {self.ability}.")
                eff*=2.25
        if other.ability=="Flash Fire":
            print(f"{other.name}'s {other.ability}.")
            other.atk=other.maxatk*1.5*other.atkb
            other.spatk=other.maxspatk*1.5*other.spatkb
            eff*=0
        if other.type1 in fireeff:
            if other.ability=="Thick Fat":
                print(f"{other.name}'s {other.ability}.")
                eff*=1
            else:
                eff*=2
        if other.type2 in fireeff:
            eff*=2
        if other.type1 in firewk:
            eff/=2
        if other.type2 in firewk:
            eff/=2
        else:
            eff*=1        
    #Poison            
    if self.atktype=="Poison":
        if other.type1 in poisoneff:
            eff*=2
        if other.type2 in poisoneff:
            eff*=2
        if other.type1 in poisonwk:
            eff/=2
        if other.type2 in poisonwk:
            eff/=2
        if other.type1 in poisonimmune or other.type2 in poisonimmune:
            eff*=0
        else:
            eff*=1   
    #Rock
    if self.atktype=="Rock":
        if other.type1 in rockeff:
            eff*=2
        if other.type2 in rockeff:
            eff*=2
        if other.type1 in rockwk:
            eff/=2
        if other.type2 in rockwk:
            eff/=2
        #if other.type1 in rockimmune or other.type2 in rockimmune:
            #eff*=0
        else:
            eff*=1                          
    #Normal
    if self.atktype=="Normal":
        if other.type1 in normaleff:
            eff*=2
        if other.type2 in normaleff:
            eff*=2
        if other.type1 in normalwk:
            eff/=2
        if other.type2 in normalwk:
            eff/=2
        if other.type1 in normalimmune or other.type2 in normalimmune:
            eff*=0
            if self.ability=="Scrappy":
                print(f"{self.name}'s {self.ability}.")
                eff=1
        else:
            eff*=1       
    #Fighting
    if self.atktype=="Fighting":
        if other.type1 in fightingeff:
            eff*=2
        if other.type2 in fightingeff:
            eff*=2
        if other.type1 in fightingwk:
            eff/=2
        if other.type2 in fightingwk:
            eff/=2
        if other.type1 in fightingimmune or other.type2 in fightingimmune:
            eff*=0
     
        else:
            eff*=1 
    if eff==2 or eff==4:
        if other.ability=="Solid Rock":
            print(f"{other.name}'s {other.ability}.")
            eff*=0.75
        else:
            print("Super Effective.")     
    elif eff==1:
        
        pass
    elif eff<1 and eff!=0:
        print("Not very effective.")
        if self.ability=="Tinted Lens":
            print(f"{self.name}'s {self.ability}.")
            print("Tinted Lens strengthen the power of not very effective move.")
            eff==2
    elif eff==0:
        print(f"Doesn't effect on {other.name}.")
     
                               
    #STAB              
    if self.atktype == self.type1 or self.atktype==self.type2:
        if self.ability=="Adaptability":
            print(f"{self.name}'s {self.ability}.")
            stab=2
        else:
            stab=1.5         
    return [eff,stab]
def critch(self,num=1):
    crit=16/num
    if self.ability=="Super Luck":
        crit=crit/2
    crit=random.randint(1,crit)
    if crit==1:
        if self.ability=="Sniper":
            print("It's a critical hit.")
            return 2.25
        else:
            print("It's a critical hit.")
            return 1.5
        
        
            
        
    else:
        return 1
def showmon(trainer):
	a=0
	print("==============================")
	for i in trainer.pokemons:
	    a+=1
	    print(str(a)+"."+i.name+f" ({i.hp}/{i.maxhp}) "+f"[{i.status}]")      
	 
	print("==============================")
#RANDOM DAMAGE ROLL
def randroll():
    rr=random.randint(85,100)       
    return (rr/100)    
def statchange(self):
    self.atk=self.maxatk*self.atkb
    self.defense=self.maxdef*self.defb
    self.spatk=self.maxspatk*self.spatkb
    self.spdef=self.maxspdef*self.spdefb
    self.speed=self.maxspeed*self.speedb    
def atkchange(self,amount):
    if amount==0.5:
        if 1<=self.atkb<4:
            self.atkb+=amount
        if 0.25<=self.atkb<1:
            self.atkb=2/(1/self.atkb-(amount*2))
        
    elif amount==1:
        if 1<=self.atkb<=3:
            self.atkb+=amount
        if 0.25<=self.atkb<1:
            self.atkb=2/(1/self.atkb-(amount*2))
        
    elif amount==1.5:
        if 1<=self.atkb<3:
            self.atkb+=amount
        if 0.25<=self.atkb<1:
            self.atkb=2/(1/self.atkb-(amount*2))
        
    elif amount==4:
        if 1<=self.atkb:
            self.atkb+=amount
        if 0.25<=self.atkb<1:
            self.atkb=2/(1/self.atkb-(amount*2))
       
    if amount==-0.5:
        if 0.25<self.atkb<=1   :
            self.atkb=2/(((1/self.atkb)*2)-2*amount)
        if 1<self.atkb<=4:
            self.atkb=self.atk-amount
      
    if amount==-1:
        if (2/7)<self.atkb<=1   :
            self.atkb=2/(((1/self.atkb)*2)-2*amount)
        if 1<self.atkb<=4:
            self.atkb=self.atk-amount
        
    if amount==-1.5:
        if (2/6)<self.atkb<=1   :
            self.atkb=2/(((1/self.atkb)*2)-2*amount)
        if 1<self.atkb<=4:
            self.atkb=self.atk-amount
   
    else:
        pass
def defchange(self,amount):
    if amount==0.5:
        if 1<=self.defb<4:
            self.defb+=amount
        if 0.25<=self.defb<1:
            self.defb=2/(1/self.defb-(amount*2))
        
    if amount==1:
        if 1<=self.defb<=3:
            self.defb+=amount
        if 0.25<=self.defb<1:
            self.defb=2/(1/self.defb-(amount*2))
       
    if amount==1.5:
        if 1<=self.defb<3:
            self.defb+=amount
        if 0.25<=self.defb<1:
            self.defb=2/(1/self.defb-(amount*2))
        
    if amount==4:
        if 1<=self.defb<=1    :
            self.defb+=amount
        if 0.25<=self.defb<1:
            self.defb=2/(1/self.defb-(amount*2))
      
    if amount==-0.5:
        if 0.25<self.defb<=1   :
            self.defb=2/(((1/self.defb)*2)-2*amount)
        if 1<self.defb<=4:
            self.defb=self.atk-amount
      
    if amount==-1:
        if (2/7)<self.defb<=1   :
            self.defb=2/(((1/self.defb)*2)-2*amount)
        if 1<self.defb<=4:
            self.defb=self.atk-amount
       
    if amount==-1.5:
        if (2/6)<self.defb<=1   :
            self.defb=2/(((1/self.defb)*2)-2*amount)
        if 1<self.defb<=4:
            self.defb=self.atk-amount
       
    else:
        pass
def spatkchange(self,amount):
    if amount==0.5:
        if 1<=self.spatkb<4:
            self.spatkb+=amount
        if 0.25<=self.spatkb<1:
            self.spatkb=2/(1/self.spatkb-(amount*2))
        
    if amount==1:
        if 1<=self.spatkb<=3:
            self.spatkb+=amount
        if 0.25<=self.spatkb<1:
            self.spatkb=2/(1/self.spatkb-(amount*2))
       
    if amount==1.5:
        if 1<=self.spatkb<3:
            self.spatkb+=amount
        if 0.25<=self.spatkb<1:
            self.spatkb=2/(1/self.spatkb-(amount*2))
       
    if amount==4:
        if 1<=self.spatkb<=1    :
            self.spatkb+=amount
        if 0.25<=self.spatkb<1:
            self.spatkb=2/(1/self.spatkb-(amount*2))
       
    if amount==-0.5:
        if 0.25<self.spatkb<=1   :
            self.spatkb=2/(((1/self.spatkb)*2)-2*amount)
        if 1<self.spatkb<=4:
            self.spatkb=self.atk-amount
        
    if amount==-1:
        if (2/7)<self.spatkb<=1   :
            self.spatkb=2/(((1/self.spatkb)*2)-2*amount)
        if 1<self.spatkb<=4:
            self.spatkb=self.atk-amount
        
    if amount==-1.5:
        if (2/6)<self.spatkb<=1   :
            self.spatkb=2/(((1/self.spatkb)*2)-2*amount)
        if 1<self.spatkb<=4:
            self.spatkb=self.atk-amount
        
    else:
        pass
def spdefchange(self,amount):
    if amount==0.5:
        if 1<=self.spdefb<4:
            self.spdefb+=amount
        if 0.25<=self.spdefb<1:
            self.spdefb=2/(1/self.spdefb-(amount*2))
     
    if amount==1:
        if 1<=self.spdefb<=3:
            self.spdefb+=amount
        if 0.25<=self.spdefb<1:
            self.spdefb=2/(1/self.spdefb-(amount*2))
     
    if amount==1.5:
        if 1<=self.spdefb<3:
            self.spdefb+=amount
        if 0.25<=self.spdefb<1:
            self.spdefb=2/(1/self.spdefb-(amount*2))
     
    if amount==4:
        if 1<=self.spdefb<=1    :
            self.spdefb+=amount
        if 0.25<=self.spdefb<1:
            self.spdefb=2/(1/self.spdefb-(amount*2))
       
    if amount==-0.5:
        if 0.25<self.spdefb<=1   :
            self.spdefb=2/(((1/self.spdefb)*2)-2*amount)
        if 1<self.spdefb<=4:
            self.spdefb=self.atk-amount
    
    if amount==-1:
        if (2/7)<self.spdefb<=1   :
            self.spdefb=2/(((1/self.spdefb)*2)-2*amount)
        if 1<self.spdefb<=4:
            self.spdefb=self.atk-amount
        
    if amount==-1.5:
        if (2/6)<self.spdefb<=1   :
            self.spdefb=2/(((1/self.spdefb)*2)-2*amount)
        if 1<self.spdefb<=4:
            self.spdefb=self.atk-amount
      
    else:
        pass
def speedchange(self,amount):
    if amount==0.5:
        if 1<=self.speedb<4:
            self.speedb+=amount
        if 0.25<=self.speedb<1:
            self.speedb=2/(1/self.speedb-(amount*2))
      
    if amount==1:
        if 1<=self.speedb<=3:
            self.speedb+=amount
        if 0.25<=self.speedb<1:
            self.speedb=2/(1/self.speedb-(amount*2))
  
    if amount==1.5:
        if 1<=self.speedb<3:
            self.speedb+=amount
        if 0.25<=self.speedb<1:
            self.speedb=2/(1/self.speedb-(amount*2))
      
    if amount==4:
        if 1<=self.speedb<=1    :
            self.speedb+=amount
        if 0.25<=self.speedb<1:
            self.speedb=2/(1/self.speedb-(amount*2))
       
    if amount==-0.5:
        if 0.25<self.speedb<=1   :
            self.speedb=2/(((1/self.speedb)*2)-2*amount)
        if 1<self.speedb<=4:
            self.speedb=self.atk-amount
      
    if amount==-1:
        if (2/7)<self.speedb<=1   :
            self.speedb=2/(((1/self.speedb)*2)-2*amount)
        if 1<self.speedb<=4:
            self.speedb=self.atk-amount
      
    if amount==-1.5:
        if (2/6)<self.speedb<=1   :
            self.speedb=2/(((1/self.speedb)*2)-2*amount)
        if 1<self.speedb<=4:
            self.speedb=self.atk-amount
     
    else:
        pass
