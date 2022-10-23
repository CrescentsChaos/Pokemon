#pylint:disable=W0621
#pylint:disable=C0301
#pylint:disable=R0915
#pylint:disable=W0611
#pylint:disable=R0912
#pylint:disable=R1705
#pylint:disable=R0914
#pylint:disable=C0303
#pylint:disable=C0116
import random
from colorama import init
from termcolor import colored
from field import Field
field=Field()
#from pokemons import Pokemon
def weakness(self,other,field):
    eff=1
    stab=1     
    if self.ability=="Analytic":
        if self.speed>other.speed:
            print(f"{self.name}'s {self.ability}.")
            eff*=1.3
    if self.ability=="Normalize":
        self.atktype="Normal"
    if self.atktype=="Normal":
        if self.ability=="Pixilate":
            self.atktype="Fairy"
            eff*=1.33
        if self.ability=="Aerilate":
            self.atktype="Flying"
            eff*=1.33
        if self.ability=="Galvanize":
            self.atktype="Electric"
            eff*=1.33
        if self.ability=="Refrigerate":
            self.atktype="Ice"
            eff*=1.33    
        if self.ability=="Liquid Voice":
            self.atktype="Water"
            eff*=1.33            
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
    icewk=['Steel', 'Fire', 'Ice',"Water"]
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
        if self.item == "Spell Tag":
            eff*=1.2
        if other.item=="Kasib Berry":
            print(f"{other.name}'s {other.item} reduced the damage of {self.atktype}-type move!")
            other.item=None
        if self.item == "Ghost Gem":
            eff*=1.5
            print(f"{self.item} boosted {self.name}'s damage!")
            self.item=None
        if self.item in ["Griseous Orb"]:
            eff+=(eff*0.2)
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
        if self.item == "Magnet":
            eff*=1.2
        if other.item=="Wacan Berry":
            eff*=0.5
            print(f"{other.name}'s {other.item} reduced the damage of {self.atktype}-type move!")
            other.item=None
        if field.terrain=="Electric" and (self.ability not in ["Levitate"] and self.ability!="Mold Breaker") and self.type1!="Flying" and self.type2!="Flying":
            eff*=1.3
        if other.ability=="Delta Stream":
            eff*=0.5
        if self.item == "Electric Gem":
            eff*=1.5
            print(f"{self.item} boosted {self.name}'s damage!")
            self.item=None
        if other.ability=="Lightning Rod":
            print(f"{other.name}'s {other.ability}.")
            spatkchange(other,0.5)
            print(f"{other.name}: Attack x{other.atkb}")
            eff*=0
        if other.ability=="Volt Absorb":
            print(f"{other.name}'s {other.ability}.")
            if other.hp<=other.maxhp-(other.maxhp/4):
                other.hp+=other.maxhp/4
                print(f"{other.name} gained some health.")
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
        if self.item == "Twisted Spoon":
            eff*=1.2
        if other.item=="Payapa Berry":
            eff*=0.5
            print(f"{other.name}'s {other.item} reduced the damage of {self.atktype}-type move!")
            other.item=None
        if field.terrain=="Psychic" and self.ability not in ["Levitate"] and self.type1!="Flying" and self.type2!="Flying":
            eff*=1.3
        if self.item == "Psychic Gem":
            eff*=1.5
            print(f"{self.item} boosted {self.name}'s damage!")
            self.item=None
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
        if self.item == "Never Melt Ice":
            eff*=1.2
        if other.item=="Yache Berry":
            eff*=0.5
            print(f"{other.name}'s {other.item} reduced the damage of {self.atktype}-type move!")
            other.item=None
        if other.ability=="Thick Fat":
            print(f"{other.name}'s {other.ability}!")
            eff*=0.5
        if other.ability=="Delta Stream":
            eff*=0.5
        if self.item == "Ice Gem":
            eff*=1.5
            print(f"{self.item} boosted {self.name}'s damage!")
            self.item=None
        if other.type1 in iceeff:
            eff*=2
        if other.type2 in iceeff:
            eff*=2
        if other.type1 in icewk:
            eff/=2
        if other.type2 in icewk:
            eff/=2
        else:
            eff*=1 
    #fairy
    if self.atktype=="Fairy":
        if self.item == "Pixie Plate":
            eff*=1.2
        if other.item=="Roseli Berry":
            eff*=0.5
            print(f"{other.name}'s {other.item} reduced the damage of {self.atktype}-type move!")
            other.item=None
        if self.ability=="Fairy Aura":
            if other.ability!="Aura Break":
                print(f"{self.name}'s {self.ability}.")
                eff*=1.33
            else:
                print(f"{other.name}'s {other.ability}.")
                eff*=0.67
        if self.item == "Fairy Gem":
            eff*=1.5
            print(f"{self.item} boosted {self.name}'s damage!")
            self.item=None
        if other.type1 in fairyeff:
            eff*=2
        if other.type2 in fairyeff:
            eff*=2
        if other.type1 in fairywk:
            eff/=2
        if other.type2 in fairywk:
            eff/=2
        else:
            eff*=1 
    #dark
    if self.atktype=="Dark":
        if self.item == "Black Glasses":
            eff*=1.2
        if other.item=="Colbur Berry":
            eff*=0.5
            print(f"{other.name}'s {other.item} reduced the damage of {self.atktype}-type move!")
            other.item=None
        if self.ability=="Dark Aura":
            if other.ability!="Aura Break":
                print(f"{self.name}'s {self.ability}.")
                eff*=1.33
            else:
                print(f"{other.name}'s {other.ability}.")
                eff*=0.67
        if self.item == "Dark Gem":
            eff*=1.5
            print(f"{self.item} boosted {self.name}'s damage!")
            self.item=None
        if other.ability=="Justified":
            atkchange(other,0.5)
            print(f"{other.name}: Attack x{other.atkb}")
        if other.type1 in darkeff:
            eff*=2
        if other.type2 in darkeff:
            eff*=2
        if other.type1 in darkwk:
            eff/=2
        if other.type2 in darkwk:
            eff/=2
        else:
            eff*=1 
    #steel
    if self.atktype=="Steel":
        if self.ability=="Sand Force" and field.weather=="Sandstorm":
            eff*=1.3
        if self.item == "Metal Coat":
            eff*=1.2
        if other.item=="Babiri Berry":
            eff*=0.5
            print(f"{other.name}'s {other.item} reduced the damage of {self.atktype}-type move!")
            other.item=None
        if self.ability=="Steelworker":
            print(f"{self.name}'s {self.ability}.")
            eff*=1.5
        if self.item == "Steel Gem":
            eff*=1.5
            print(f"{self.item} boosted {self.name}'s damage!")
            self.item=None
        if self.item in ["Adamant Orb"]:
            eff+=(eff*0.2)
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
        if self.item == "Dragon Fang":
            eff*=1.2
        if other.item=="Haban Berry":
            eff*=0.5
            print(f"{other.name}'s {other.item} reduced the damage of {self.atktype}-type move!")
            other.item=None
        if field.terrain=="Misty" and self.ability not in ["Levitate"] and self.type1!="Flying" and self.type2!="Flying":
            eff*=0.5
        if self.item == "Dragon Gem":
            eff*=1.5
            print(f"{self.item} boosted {self.name}'s damage!")
            self.item=None
        if self.item in ["Adamant Orb","Lustrous Orb","Griseous Orb"]:
            eff+=(eff*0.2)
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
        if self.item == "Silver Powder":
            eff*=1.2
        if other.item=="Tanga Berry":
            eff*=0.5
            print(f"{other.name}'s {other.item} reduced the damage of {self.atktype}-type move!")
            other.item=None
        if self.item == "Bug Gem":
            eff*=1.5
            print(f"{self.item} boosted {self.name}'s damage!")
            self.item=None
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
        if other.ability=="Steam Engine":
            print(f"{other.name}'s {other.ability}!")
            speedchange (other,0.5)
            print(f"{other.name} Speed x{other.speedb}")
        if self.item == "Mystic Water":
            eff*=1.2
        if other.item=="Passho Berry":
            eff*=0.5
            print(f"{other.name}'s {other.item} reduced the damage of {self.atktype}-type move!")
            other.item=None
        if field.weather=="Desolate Land":
            eff*=0
        if self.item == "Water Gem":
            eff*=1.5
            print(f"{self.item} boosted {self.name}'s damage!")
            self.item=None
        if self.item in ["Lustrous Orb"]:
            eff+=(eff*0.2)
        if other.ability in ["Storm Drain","Water Absorb","Dry Skin"]:
            if other.ability=="Dry Skin":
                print(f"{other.name}'s {other.ability}.")
                if other.hp<=other.maxhp-(other.maxhp/4):
                    other.hp+=other.maxhp/4
                    print(f"{other.name} gained some health.")
            if other.ability=="Storm Drain":
                print(f"{other.name}'s {other.ability}.")
                spatkchange (other,0.5)
                print(f"{other.name}: Special Attack x{other.spatkb}")
            if other.ability=="Water Absorb":
                print(f"{other.name}'s {other.ability}.")
                if other.hp<=other.maxhp-(other.maxhp/4):
                    other.hp+=other.maxhp/4
                    print(f"{other.name} gained some health.")
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
       # if other.type1 in waterimmune or other.type2 in waterimmune:
           # eff*=0
        else:
            eff*=1 
    #Ground
    if self.atktype=="Ground":
        if other.item=="Air Balloon":
            eff*=0
        if self.ability=="Sand Force" and field.weather=="Sandstorm":
            eff*=1.3
        if self.item == "Soft Sand":
            eff*=1.2
        if other.item=="Shuca Berry":
            eff*=0.5
            print(f"{other.name}'s {other.item} reduced the damage of {self.atktype}-type move!")
            other.item=None
        if self.item == "Ground Gem":
            eff*=1.5
            print(f"{self.item} boosted {self.name}'s damage!")
            self.item=None
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
        if self.item == "Miracle Seed":
            eff*=1.2
        if other.item=="Rindo Berry":
            eff*=0.5
            print(f"{other.name}'s {other.item} reduced the damage of {self.atktype}-type move!")
            other.item=None
        if field.terrain=="Grassy" and self.ability not in ["Levitate"] and self.type1!="Flying" and self.type2!="Flying":
            eff*=1.3
        if self.item == "Grass Gem":
            eff*=1.5
            print(f"{self.item} boosted {self.name}'s damage!")
            self.item=None
        if other.ability=="Sap Sipper":
            print(f"{other.name}'s {other.ability}.")
            eff*=0
            atkchange (other,0.5)
            print(f"{other.name}: Attack x{other.atkb}")
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
        if self.item == "Sharp Beak":
            eff*=1.2
        if other.item=="Koba Berry":
            eff*=0.5
            print(f"{other.name}'s {other.item} reduced the damage of {self.atktype}-type move!")
            other.item=None
        if self.item == "Flying Gem":
            eff*=1.5
            print(f"{self.item} boosted {self.name}'s damage!")
            self.item=None
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
        if other.ability=="Steam Engine":
            print(f"{other.name}'s {other.ability}!")
            speedchange (other,0.5)
            print(f"{other.name} Speed x{other.speedb}")
        if self.item == "Charcoal":
            eff*=1.2
        if other.item=="Occa Berry":
            eff*=0.5
            print(f"{other.name}'s {other.item} reduced the damage of {self.atktype}-type move!")
            other.item=None
        if other.ability=="Dry Skin":
            print(f"{other.name}'s {other.ability}!")
            eff*=1.25
        if other.ability=="Thick Fat":
            print(f"{other.name}'s {other.ability}!")
            eff*=0.5
        if field.weather=="Primordial Sea":
            eff*=0
        if self.item == "Fire Gem":
            eff*=1.5
            print(f"{self.item} boosted {self.name}'s damage!")
            self.item=None
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
        if self.item == "Poison Barb":
            eff*=1.2
        if other.item=="Kebia Berry":
            eff*=0.5
            print(f"{other.name}'s {other.item} reduced the damage of {self.atktype}-type move!")
            other.item=None
        if self.item == "Poison Gem":
            eff*=1.5
            print(f"{self.item} boosted {self.name}'s damage!")
            self.item=None
        if other.type1 in poisoneff:
            eff*=2
        if other.type2 in poisoneff:
            eff*=2
        if other.type1 in poisonwk:
            eff/=2
        if other.type2 in poisonwk:
            eff/=2
        if other.type1 in poisonimmune or other.type2 in poisonimmune:
            if self.ability!="Corrosion":
                eff*=0
            else:
                print(f"{self.name}'s {self.ability}.")
                eff*=1
        else:
            eff*=1   
    #Rock
    if self.atktype=="Rock":
        if self.ability=="Sand Force" and field.weather=="Sandstorm":
            eff*=1.3
        if self.item == "Hard Stone":
            eff*=1.2
        if other.item=="Charti Berry":
            eff*=0.5
            print(f"{other.name}'s {other.item} reduced the damage of {self.atktype}-type move!")
            other.item=None
        if other.ability=="Delta Stream":
            eff*=0.5
        if self.item == "Rock Gem":
            eff*=1.5
            print(f"{self.item} boosted {self.name}'s damage!")
            self.item=None
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
        if self.item == "Silk Scarf":
            eff*=1.2
        if other.item=="Chilan Berry":
            eff*=0.5
            print(f"{other.name}'s {other.item} reduced the damage of {self.atktype}-type move!")
            other.item=None
        if self.item == "Normal Gem":
            eff*=1.5
            print(f"{self.item} boosted {self.name}'s damage!")
            self.item=None
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
        if self.item == "Black Belt":
            eff*=1.2
        if other.item=="Chople Berry":
            eff*=0.5
            print(f"{other.name}'s {other.item} reduced the damage of {self.atktype}-type move!")
            other.item=None
        if self.item == "Fighting Gem":
            eff*=1.5
            print(f"{self.item} boosted {self.name}'s damage!")
            self.item=None
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
        print("It's super effective!") 
        if other.item=="Weakness Policy":
            print(f"{other.name}'s {other.item}.")
            other.item=None
            atkchange (other,1)
            spatkchange (other,1)
            print(f"{other.name}: Attack x{other.atkb}")
            print(f"{other.name}: Special Attack x{other.spatkb}")
        if self.item=="Expert Belt":
            eff*=1.2
        if other.ability=="Solid Rock":
            print(f"{other.name}'s {other.ability}.")
            eff*=0.75
                
    elif eff==1:
        
        pass
    elif eff<1 and eff!=0:
        print("It's not very effective...")
        if self.ability=="Tinted Lens":
            print(f"{self.name}'s {self.ability}.")
            print("Tinted Lens strengthen the power of not very effective move.")
            eff=2
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
    
#CRITICAL    
def critch(self,other,num=1):
    crit=16/num
    if self.item=="Scope Lens" and crit!=1:
        crit=crit/2
    if self.ability=="Super Luck" and crit!=1:
        crit=crit/2
    crit=random.randint(1,crit)
    if crit==1 and other.ability not in ["Shell Armor","Battle Armor"]:
        if other.ability=="Anger Point":
            print(f"{other.name}'s {other.ability}.")
            atkchange(other,4)
        if self.ability=="Sniper":
            print(colored("It's a critical hit.","red"))
            return 3
        else:
            print(colored("It's a critical hit.","red"))
            return 2
    if other.ability in ["Shell Armor","Battle Armor"] and crit==1:
        return 1
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
def prebuff(self):    
    atkbuff=1
    defbuff=1
    spatkbuff=1
    spdefbuff=1
    speedbuff=1
    if self.ability in ["Huge Power","Pure Power","Guts","Multitype"]:
        if self.ability in ["Huge Power","Pure Power"]:
            atkbuff*=2
    if field.weather in ["Rainy","Primordial Sea"] and self.ability=="Swift Swim":
        print(f"{self.name}'s {self.ability}!")
        speedbuff*=2
    if field.weather in ["Sunny","Desolate Land"] and self.ability=="Chlorophyll":
        print(f"{self.name}'s {self.ability}!")
        speedbuff*=2
    if field.weather in ["Sandstorm"] and self.ability=="Sand Rush":
        print(f"{self.name}'s {self.ability}!")
        speedbuff*=2
    if field.weather in ["Hail"] and self.ability=="Slush Rush":
        print(f"{self.name}'s {self.ability}!")
        speedbuff*=2
    if field.weather in ["Sandstorm"] and (self.type1=="Rock" or self.type2=="Rock"):
        spdefbuff*=2
    if self.item=="Life Orb":
        atkbuff*=1.5
    if self.item=="Eviolite":
        defbuff*=1.5
        spdefbuff*=1.5
    if self.item=="Assault Vest":
        spdefbuff*=1.5
    self.atk=self.maxatk*self.atkb*atkbuff
    self.defense=self.maxdef*self.defb*defbuff
    self.spatk=self.maxspatk*self.spatkb
    self.spdef=self.maxspdef*self.spdefb*spdefbuff
    self.speed=self.maxspeed*self.speedb*speedbuff
def statchange(self):
    atkbuff=1
    defbuff=1
    spatkbuff=1
    spdefbuff=1
    speedbuff=1
    if self.ability=="Marvel Scale" and self.status!="Alive":
        defbuff*=1.5
    if self.ability=="Flare Boost" and self.status=="Burned":
        spatkbuff*=1.5
    if field.weather in ["Rainy","Primordial Sea"] and self.ability=="Swift Swim":
        print(f"{self.name}'s {self.ability}!")
        speedbuff*=2
    if field.weather in ["Sunny","Desolate Land"] and self.ability=="Chlorophyll":
        print(f"{self.name}'s {self.ability}!")
        speedbuff*=2
    if field.weather in ["Sandstorm"] and self.ability=="Sand Rush":
        print(f"{self.name}'s {self.ability}!")
        speedbuff*=2
    if field.weather in ["Hail"] and self.ability=="Slush Rush":
        print(f"{self.name}'s {self.ability}!")
        speedbuff*=2
    if field.weather in ["Sandstorm"] and (self.type1=="Rock" or self.type2=="Rock"):
        spdefbuff*=2
    if self.item=="Choice Band":
        atkbuff*=1.5
    if self.item=="Choice Specs":
        spatkbuff*=1.5
    if self.item=="Choice Scarf":
        speedbuff*=1.5
    if self.item=="Assault Vest":
        spdefbuff*=1.5
    if self.ability=="Typeless":
        self.type1=self.atktype
    if self.item=="Flame Orb" and self.status=="Alive":
        self.status="Burned"
        print(f"{self.name} was burned by its Flame Orb.")
    if self.item=="Toxic Orb" and self.status=="Alive":
        self.status="Badly Poisoned"
        print(f"{self.name} was badly poisoned by its Toxic Orb.")
    self.atk=self.maxatk*self.atkb
    if self.ability in ["Huge Power","Pure Power","Guts","Multitype"]:
        if self.ability in ["Huge Power","Pure Power"]:
            atkbuff*=2
        if self.ability=="Guts" and self.status!="Alive":
            atkbuff*=1.5
        if self.item=="Elemental Plates":
            atkbuff=1.5
    if self.item=="Life Orb":
        atkbuff=1.5
    if self.item=="Eviolite":
        defbuff=1.5
        spdefbuff=1.5
    if self.ability!="Stance Change":
        self.atk=self.maxatk*self.atkb*atkbuff
        self.defense=self.maxdef*self.defb*defbuff
        self.spatk=self.maxspatk*self.spatkb
        self.spdef=self.maxspdef*self.spdefb*spdefbuff
        self.speed=self.maxspeed*self.speedb*speedbuff
    #if self.ability=="Stance Change" and self.sword==True:
#        self.atk=self.maxatk*self.atkb*atkbuff
#        self.defense=self.maxdef*self.defb*defbuff
#        self.spatk=self.maxspatk*self.spatkb
#        self.spdef=self.maxspdef*self.spdefb*spdefbuff
#        self.speed=self.maxspeed*self.speedb
def atkchange(self,amount):
    if self.ability=="Defiant":
        if amount<0:
            print(f"{self.name}'s {self.ability}!")
            atkchange(self,1)
    if self.ability=="Competitive":
        if amount<0:
            print(f"{self.name}'s {self.ability}!")
            spatkchange(self,1)
    if self.ability=="Contrary":
        amount=-amount
    if amount==0.5:
        if 1<=self.atkb<4:
            self.atkb+=amount
        if 0.25<=self.atkb<1:
            self.atkb=round(1/((1/self.atkb)-amount),2)
        
    elif amount==1:
        if 1<=self.atkb<=3:
            self.atkb+=amount
        if 0.25<=self.atkb<1:
            self.atkb=round(1/((1/self.atkb)-amount),2)
        
    elif amount==1.5:
        if 1<=self.atkb<3:
            self.atkb+=amount
        if 0.25<=self.atkb<1:
            self.atkb=round(1/((1/self.atkb)-amount),2)
        
    elif amount==4:
        if 1<=self.atkb:
            self.atkb=amount
        if 0.25<=self.atkb<1:
            self.atkb=round(1/((1/self.atkb)-amount),2)
       
    if amount==-0.5:
        if 0.25<self.atkb<=1   :
            self.atkb=round(1/((1/self.atkb)-amount),2)
        if 1<self.atkb<=4:
            self.atkb=self.atkb+amount
      
    if amount==-1:
        if (2/7)<self.atkb<=1   :
            self.atkb=round(1/((1/self.atkb)-amount),2)
        if 1<self.atkb<=4:
            self.atkb=self.atkb+amount
        
    if amount==-1.5:
        if (2/6)<self.atkb<=1   :
            self.atkb=round(1/((1/self.atkb)-amount),2)
        if 1<self.atkb<=4:
            self.atkb=self.atkb+amount
   
    else:
        pass



def defchange(self,amount):
    if self.ability=="Defiant":
        if amount<0:
            print(f"{self.name}'s {self.ability}!")
            atkchange(self,1)
    if self.ability=="Competitive":
        if amount<0:
            print(f"{self.name}'s {self.ability}!")
            spatkchange(self,1)
    if self.ability=="Contrary":
        amount=-amount
    if amount==0.5:
        if 1<=self.defb<4:
            self.defb+=amount
        if 0.25<=self.defb<1:
            self.defb=round(1/((1/self.defb)-amount),2)
        
    elif amount==1:
        if 1<=self.defb<=3:
            self.defb+=amount
        if 0.25<=self.defb<1:
            self.defb=round(1/((1/self.defb)-amount),2)
        
    elif amount==1.5:
        if 1<=self.defb<3:
            self.defb+=amount
        if 0.25<=self.defb<1:
            self.defb=round(1/((1/self.defb)-amount),2)
        
    elif amount==4:
        if 1<=self.defb:
            self.defb=amount
        if 0.25<=self.defb<1:
            self.defb=round(1/((1/self.defb)-amount),2)
       
    if amount==-0.5:
        if 0.25<self.defb<=1   :
            self.defb=round(1/((1/self.defb)-amount),2)
        if 1<self.defb<=4:
            self.defb=self.defb+amount
      
    if amount==-1:
        if (2/7)<self.defb<=1   :
            self.defb=round(1/((1/self.defb)-amount),2)
        if 1<self.defb<=4:
            self.defb=self.defb+amount
        
    if amount==-1.5:
        if (2/6)<self.defb<=1   :
            self.defb=round(1/((1/self.defb)-amount),2)
        if 1<self.defb<=4:
            self.defb=self.defb+amount
   
    else:
        pass

def spatkchange(self,amount):
    if self.ability=="Defiant":
        if amount<0:
            print(f"{self.name}'s {self.ability}!")
            atkchange(self,1)
    if self.ability=="Competitive":
        if amount<0:
            print(f"{self.name}'s {self.ability}!")
            spatkchange(self,1)
    if self.ability=="Contrary":
        amount=-amount
    if amount==0.5:
        if 1<=self.spatkb<4:
            self.spatkb+=amount
        if 0.25<=self.spatkb<1:
            self.spatkb=round(1/((1/self.spatkb)-amount),2)
        
    elif amount==1:
        if 1<=self.spatkb<=3:
            self.spatkb+=amount
        if 0.25<=self.spatkb<1:
            self.spatkb=round(1/((1/self.spatkb)-amount),2)
        
    elif amount==1.5:
        if 1<=self.spatkb<3:
            self.spatkb+=amount
        if 0.25<=self.spatkb<1:
            self.spatkb=round(1/((1/self.spatkb)-amount),2)
        
    elif amount==4:
        if 1<=self.spatkb:
            self.spatkb=amount
        if 0.25<=self.spatkb<1:
            self.spatkb=round(1/((1/self.spatkb)-amount),2)
       
    if amount==-0.5:
        if 0.25<self.spatkb<=1   :
            self.spatkb=round(1/((1/self.spatkb)-amount),2)
        if 1<self.spatkb<=4:
            self.spatkb=self.spatkb+amount
      
    if amount==-1:
        if (2/7)<self.spatkb<=1   :
            self.spatkb=round(1/((1/self.spatkb)-amount),2)
        if 1<self.spatkb<=4:
            self.spatkb=self.spatkb+amount
        
    if amount==-1.5:
        if (2/6)<self.spatkb<=1   :
            self.spatkb=round(1/((1/self.spatkb)-amount),2)
        if 1<self.spatkb<=4:
            self.spatkb=self.spatkb+amount
   
    else:
        pass

def spdefchange(self,amount):
    if self.ability=="Defiant":
        if amount<0:
            print(f"{self.name}'s {self.ability}!")
            atkchange(self,1)
    if self.ability=="Competitive":
        if amount<0:
            print(f"{self.name}'s {self.ability}!")
            spatkchange(self,1)
    if self.ability=="Contrary":
        amount=-amount
    if amount==0.5:
        if 1<=self.spdefb<4:
            self.spdefb+=amount
        if 0.25<=self.spdefb<1:
            self.spdefb=round(1/((1/self.spdefb)-amount),2)
        
    elif amount==1:
        if 1<=self.spdefb<=3:
            self.spdefb+=amount
        if 0.25<=self.spdefb<1:
            self.spdefb=round(1/((1/self.spdefb)-amount),2)
        
    elif amount==1.5:
        if 1<=self.spdefb<3:
            self.spdefb+=amount
        if 0.25<=self.spdefb<1:
            self.spdefb=round(1/((1/self.spdefb)-amount),2)
        
    elif amount==4:
        if 1<=self.spdefb:
            self.spdefb=amount
        if 0.25<=self.spdefb<1:
            self.spdefb=round(1/((1/self.spdefb)-amount),2)
       
    if amount==-0.5:
        if 0.25<self.spdefb<=1   :
            self.spdefb=round(1/((1/self.spdefb)-amount),2)
        if 1<self.spdefb<=4:
            self.spdefb=self.spdefb+amount
      
    if amount==-1:
        if (2/7)<self.spdefb<=1   :
            self.spdefb=round(1/((1/self.spdefb)-amount),2)
        if 1<self.spdefb<=4:
            self.spdefb=self.spdefb+amount
        
    if amount==-1.5:
        if (2/6)<self.spdefb<=1   :
            self.spdefb=round(1/((1/self.spdefb)-amount),2)
        if 1<self.spdefb<=4:
            self.spdefb=self.spdefb+amount
   
    else:
        pass

def speedchange(self,amount):
    if self.ability=="Defiant":
        if amount<0:
            print(f"{self.name}'s {self.ability}!")
            atkchange(self,1)
    if self.ability=="Competitive":
        if amount<0:
            print(f"{self.name}'s {self.ability}!")
            spatkchange(self,1)
    if self.ability=="Contrary":
        amount=-amount
    if amount==0.5:
        if 1<=self.speedb<4:
            self.speedb+=amount
        if 0.25<=self.speedb<1:
            self.speedb=round(1/((1/self.speedb)-amount),2)
        
    elif amount==1:
        if 1<=self.speedb<=3:
            self.speedb+=amount
        if 0.25<=self.speedb<1:
            self.speedb=round(1/((1/self.speedb)-amount),2)
        
    elif amount==1.5:
        if 1<=self.speedb<3:
            self.speedb+=amount
        if 0.25<=self.speedb<1:
            self.speedb=round(1/((1/self.speedb)-amount),2)
        
    elif amount==4:
        if 1<=self.speedb:
            self.speedb=amount
        if 0.25<=self.speedb<1:
            self.speedb=round(1/((1/self.speedb)-amount),2)
       
    if amount==-0.5:
        if 0.25<self.speedb<=1   :
            self.speedb=round(1/((1/self.speedb)-amount),2)
        if 1<self.speedb<=4:
            self.speedb=self.speedb+amount
      
    if amount==-1:
        if (2/7)<self.speedb<=1   :
            self.speedb=round(1/((1/self.speedb)-amount),2)
        if 1<self.speedb<=4:
            self.speedb=self.speedb+amount
        
    if amount==-1.5:
        if (2/6)<self.speedb<=1   :
            self.speedb=round(1/((1/self.speedb)-amount),2)
        if 1<self.speedb<=4:
            self.speedb=self.speedb+amount
   
    else:
        pass

