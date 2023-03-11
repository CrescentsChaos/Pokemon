#pylint:disable=W0401
#pylint:disable=C0103
#pylint:disable=W0621
#pylint:disable=C0301
#pylint:disable=R0915
#pylint:disable=W0611
#pylint:disable=R0912
#pylint:disable=R1705
#pylint:disable=R0914
#pylint:disable=C0303
#pylint:disable=C0116
from movelist import *
import random
from colorama import init
from termcolor import colored
from field import *
field=Field()
#from pokemons import Pokemon
def resetboost(mon,mon2):
    mon.atkb,mon.defb,mon.spatkb,mon.spdefb,mon.speedb=1,1,1,1,1
def weakness(self,other,field):
    eff=1
    stab=1     
    if other.use=="Glaive Rush":
        eff*=2
    if self.use in typemoves.windmoves and other.ability=="Wind Rider" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves:
        eff*=0
        atkchange(other,self,0.5)
        print(f" 🍃 {other.name}'s {other.ability}!")
  
    if "Absolute Zero" in (self.ability,other.ability) and self.atktype=="Water":
        print(" 🥶 Absolute Zero turned the Water-type move into Ice-type move!")
        self.atktype="Ice"
    #UNAWARE(OTHER EFFECT)
    if self.ability=="Unaware":
        other.defense=round(other.defense/other.defb)
        other.spdef=round(other.spdef/other.spdefb)
    #UNAWARE(SELF EFFECT)
    if other.ability=="Unaware":
        self.atk=round(self.atk/self.atkb)
        self.spatk=round(self.spatk/self.spatkb)
    #PROTEAN/LIBERO
    if self.ability in ["Protean","Libero"] and self.type1!=self.atktype:
        self.type2="None"
        self.type1=self.atktype
        print(f" {self.name} changed it's type to {self.type1} using {self.ability}!")
    if self.ability in ["Color Change"] and self.type1!=other.atktype:
        self.type2="None"
        self.type1=other.atktype
        print(f" {self.name} changed it's type to {self.type1} using {self.ability}!")
    #SHADOW SHIELD/MULTISCALE/BLUBBER DEFENSE        
    if other.hp==other.maxhp and other.ability in ["Multiscale","Blubber Defense","Shadow Shield"] and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves:
        print(f" 🔰 {other.name}'s {other.ability}.")
        eff*=0.5
    #SOLAR POWER
    if self.ability=="Solar Power" and field.weather in ["Sunny","Desolate Land"] and "Cloud Nine" not in (self.ability,other.ability):
        print(f" ☀️ {self.name}'s {self.ability}!")
        eff*=1.5
    #ILLUSION BOOST
    if "Zoroark" not in self.name and self.ability=="Illusion":
        eff*=1.3
    #ANALYTIC
    if self.ability=="Analytic":
        if self.speed<other.speed:
            print(f" {self.name}'s {self.ability}.")
            eff*=1.3
    #NORMALIZE 
    if self.ability=="Normalize":
        self.atktype="Normal"
    #CHANGING NORMAL TYPE MOVES
    if self.atktype=="Normal":
        if self.ability in ["Pixilate","Aerilate","Galvanize","Refrigerate","Liquid Voice"]:
            eff*=1.33
        if self.ability=="Pixilate":
            self.atktype="Fairy"
        if self.ability=="Aerilate":
            self.atktype="Flying"
        if self.ability=="Galvanize":
            self.atktype="Electric"
        if self.ability=="Refrigerate":
            self.atktype="Ice"
        if self.ability=="Liquid Voice":
            self.atktype="Water"   
            
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
        #RATTLED
        if other.ability=="Rattled":
            speedchange(other,self,0.5)
        #PURIFYING SALT
        if other.ability=="Purifying Salt" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves:
            eff*=0.5
        if other.item=="Kasib Berry":
            print(f" {other.name}'s {other.item} weakened the damage of {self.atktype}-type move!")
            self.item+="[Used]"
        if self.item == "Ghost Gem":
            eff*=1.5
            print(f" 💎 {self.item} boosted {self.name}'s damage!")
            self.item+="[Used]"
        if self.item in ["Griseous Orb","Spooky Plate","Spell Tag"]:
            eff*=1.2
        if other.type1 in ghosteff and other.teratype=="None":
            eff*=2
        if other.type2 in ghosteff and other.teratype=="None":
            eff*=2
        if other.teratype in ghosteff:
            eff*=2
        if other.type1 in ghostwk and other.teratype=="None":
            eff/=2
        if other.type2 in ghostwk and other.teratype=="None":
            eff/=2
        if other.teratype in ghostwk:
            eff/=2
        if (other.type1 in ghostimmune or other.type2 in ghostimmune and other.teratype=="None") or (other.teratype in ghostimmune and other.item!="Ring Target"):
            eff*=0            
#        else:
#            eff*=1 
    #electric
    if self.atktype=="Electric":
        if self.atktime>0 and self.ability=="Electromorphosis" and self.speed<other.speed:
            print(f" 🐸 {self.name}'s {self.ability}!")
            eff*=1.34
        if other.ability=="Motor Drive" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves:
            print(f" ⚙️ {other.name}'s {other.ability}!")
            speedchange(other,self,0.5)
       
            eff*=0
        if other.ability=="Wonder Guard" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves:
            print(f" 🛡️ {other.name}'s {other.ability}!")
            eff*=0
        if self.ability=="Transistor":
            print(f" 🔋 {self.name}'s {self.ability}.")
            eff*=1.5
        if self.item == "Magnet":
            eff*=1.2
        if other.item=="Wacan Berry":
            eff*=0.5
            print(f" {other.name}'s {other.item} weakened the damage of {self.atktype}-type move!")
            self.item+="[Used]"
        if field.terrain=="Electric" and ((self.ability not in ["Levitate"] and self.ability!="Mold Breaker") and "Flying" not in (self.type1,self.type2,self.teratype) or self.grav is True):
            eff*=1.3
        if other.ability=="Delta Stream" and "Flying" in (other.type1,other.type2,other.teratype) and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves:
            eff*=0.5
        if self.item in ["Zap Plate","Battery","Magnet"]:
            eff*=1.2
        if self.item == "Electric Gem":
            eff*=1.5
            print(f" 💎 {self.item} boosted {self.name}'s damage!")
            self.item+="[Used]"
        if other.ability=="Lightning Rod" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves:
            print(f" ⚡ {other.name}'s {other.ability}.")
            spatkchange(other,self,0.5)
 
            eff*=0
        if other.ability=="Volt Absorb" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves:
            print(f" ⚡ {other.name}'s {other.ability}.")
            if other.hp<other.maxhp:
                print(f" {other.name} gained some health.")
            if other.hp<=other.maxhp-(other.maxhp/4):
                other.hp+=other.maxhp/4
            if other.hp>other.maxhp-(other.maxhp/4):
                other.hp=other.maxhp
            eff*=0
        if other.type1 in electriceff and other.teratype=="None":
            eff*=2
        if other.teratype in electriceff:
            eff*=2
        if other.type2 in electriceff and other.teratype=="None":
            eff*=2
        if other.type1 in electricwk and other.teratype=="None":
            eff/=2
        if other.type2 in electricwk and other.teratype=="None":
            eff/=2
        if other.teratype in electricwk:
            eff/=2
        if (other.type1 in electricimmune or other.type2 in electricimmune and other.teratype=="None") or other.teratype in electricimmune and other.item!="Ring Target":
            eff*=0
#        else:
#            eff*=1 
    
    #psychic
    if self.atktype=="Psychic":
        if other.ability=="Dark Mind" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves:
            print(f" 😈 {other.name}'s {other.ability}!")
            eff*=0
        if other.ability=="Wonder Guard" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves:
            print(f" 🛡️ {other.name}'s {other.ability}!")
            eff*=0
        if other.item=="Payapa Berry":
            eff*=0.5
            print(f" {other.name}'s {other.item} weakened the damage of {self.atktype}-type move!")
            self.item+="[Used]"
        if field.terrain=="Psychic" and (self.ability not in ["Levitate"] and "Flying" not in (self.type1,self.type2,self.teratype) or self.grav is True):
            eff*=1.3
        if self.item in ["Mind Plate","Twisted Spoon","Soul Dew","Odd Incense"]:
            eff*=1.2
        if self.item == "Psychic Gem":
            eff*=1.5
            print(f" 💎 {self.item} boosted {self.name}'s damage!")
            self.item+="[Used]"
        if other.type1 in psychiceff and other.teratype=="None":
            eff*=2
        if other.type2 in psychiceff and other.teratype=="None":
            eff*=2
        if other.type1 in psychicwk and other.teratype=="None":
            eff/=2
        if other.type2 in psychicwk and other.teratype=="None":
            eff/=2
        if other.teratype in psychiceff:
            eff*=2
        if other.teratype in psychicwk:
            eff/=2
        if (other.type1 in psychicimmune or other.type2 in psychicimmune and other.teratype=="None") or other.teratype in psychicimmune and other.item!="Ring Target":
            eff*=0
#        else:
#            eff*=1 
    #ice
    if self.atktype=="Ice":
        if self.use=="Freeze-Dry" and "Water" in (other.type1,other.type2,other.teratype):
            eff*=4
        if other.ability=="Wonder Guard" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves:
            print(f" 🛡️ {other.name}'s {other.ability}!")
            eff*=0
        if self.item in ["Never Melt Ice","Icicle Plate"]:
            eff*=1.2
        if other.item=="Yache Berry":
            eff*=0.5
            print(f" {other.name}'s {other.item} weakened the damage of {self.atktype}-type move!")
            self.item+="[Used]"
        if other.ability=="Thick Fat" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves:
            print(f" 🌡️ {other.name}'s {other.ability}!")
            eff*=0.5
        if other.ability=="Delta Stream" and "Flying" in (other.type1,other.type2) and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves:
            eff*=0.5
        if self.item == "Ice Gem":
            eff*=1.5
            print(f" 💎 {self.item} boosted {self.name}'s damage!")
            self.item+="[Used]"
        if other.type1 in iceeff and other.teratype=="None":
            eff*=2
        if other.type2 in iceeff and other.teratype=="None":
            eff*=2
        if other.type1 in icewk and other.teratype=="None":
            eff/=2
        if other.type2 in icewk and other.teratype=="None":
            eff/=2
        if other.teratype in iceeff:
            eff*=2
        if other.teratype in icewk:
            eff/=2
#        else:
#            eff*=1 
    #fairy
    if self.atktype=="Fairy":
        if other.ability=="Wonder Guard" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves:
            print(f" 🛡️ {other.name}'s {other.ability}!")
            eff*=0
        if self.item == "Pixie Plate":
            eff*=1.2
        if other.item=="Roseli Berry":
            eff*=0.5
            print(f" {other.name}'s {other.item} weakened the damage of {self.atktype}-type move!")
            self.item+="[Used]"
        if self.ability=="Fairy Aura":
            if other.ability!="Aura Break":
                print(f" 🧚🏻‍♀️ {self.name}'s {self.ability}.")
                eff*=1.33
            else:
                print(f" {other.name}'s {other.ability}.")
                eff*=0.67
        if self.item == "Fairy Gem":
            eff*=1.5
            print(f" 💎 {self.item} boosted {self.name}'s damage!")
            self.item+="[Used]"
        if other.type1 in fairyeff and other.teratype=="None":
            eff*=2
        if other.type2 in fairyeff and other.teratype=="None":
            eff*=2
        if other.type1 in fairywk and other.teratype=="None":
            eff/=2
        if other.type2 in fairywk and other.teratype=="None":
            eff/=2
        if other.teratype in fairyeff:
            eff*=2
        if other.teratype in fairywk:
            eff/=2
#        else:
#            eff*=1 
    #dark
    if self.atktype=="Dark":
        if other.ability=="Rattled":
            speedchange(other,self,0.5)
        if self.item in ["Black Glasses","Dread Plate"]:
            eff*=1.2
        if other.item=="Colbur Berry":
            eff*=0.5
            print(f" {other.name}'s {other.item} weakened the damage of {self.atktype}-type move!")
            self.item+="[Used]"
        if self.ability=="Dark Aura":
            if other.ability!="Aura Break":
                print(f" 🌑 {self.name}'s {self.ability}.")
                eff*=1.33
            else:
                print(f" {other.name}'s {other.ability}.")
                eff*=0.67
        if self.item == "Dark Gem":
            eff*=1.5
            print(f" 💎 {self.item} boosted {self.name}'s damage!")
            self.item+="[Used]"
        if other.ability=="Justified" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves:
            atkchange(other,self,0.5)
            
        if other.type1 in darkeff and other.teratype=="None":
            eff*=2
        if other.type2 in darkeff and other.teratype=="None":
            eff*=2
        if other.type1 in darkwk and other.teratype=="None":
            eff/=2
        if other.type2 in darkwk and other.teratype=="None":
            eff/=2
        if other.teratype in darkeff:
            eff*=2
        if other.teratype in darkwk:
            eff/=2
#        else:
#            eff*=1 
    #steel
    if self.atktype=="Steel":
        if self.ability=="Steely Spirit":
            eff*=1.5
        if other.ability=="Wonder Guard" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves:
            print(f" 🛡️ {other.name}'s {other.ability}!")
            eff*=0
        if self.ability=="Sand Force" and field.weather=="Sandstorm":
            eff*=1.3
        if self.item in ["Metal Coat","Iron Plate"]:
            eff*=1.2
        if other.item=="Babiri Berry":
            eff*=0.5
            print(f" {other.name}'s {other.item} weakened the damage of {self.atktype}-type move!")
            self.item+="[Used]"
        if self.ability=="Steelworker":
            print(f" 🔩 {self.name}'s {self.ability}.")
            eff*=1.5
        if self.item == "Steel Gem":
            eff*=1.5
            print(f" 💎 {self.item} boosted {self.name}'s damage!")
            self.item+="[Used]"
        if self.item in ["Adamant Orb"]:
            eff+=(eff*0.2)
        if other.type1 in steeleff and other.teratype=="None":
            eff*=2
        if other.type2 in steeleff and other.teratype=="None":
            eff*=2
        if other.type1 in steelwk and other.teratype=="None":
            eff/=2
        if other.type2 in steelwk and other.teratype=="None":
            eff/=2
        if other.teratype in steeleff:
            eff*=2
        if other.teratype in steelwk:
            eff/=2   
#        else:
#            eff*=1 
    #dragon
    if self.atktype=="Dragon":
        if other.ability=="Wonder Guard" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves:
            print(f" 🛡️ {other.name}'s {other.ability}!")
            eff*=0
        if self.ability=="Dragon's Maw":
            print(f" 🐲 {self.name}'s {self.ability}.")
            eff*=1.5
        if self.item in ["Dragon Fang","Draco Plate"]:
            eff*=1.2
        if other.item=="Haban Berry":
            eff*=0.5
            print(f" {other.name}'s {other.item} weakened the damage of {self.atktype}-type move!")
            self.item+="[Used]"
        if field.terrain=="Misty" and (self.ability not in ["Levitate"] and "Flying" not in (self.type1,self.type2,self.teratype) or self.grav is True):
            eff*=0.5
        if self.item == "Dragon Gem":
            eff*=1.5
            print(f" 💎 {self.item} boosted {self.name}'s damage!")
            self.item+="[Used]"
        if self.item in ["Adamant Orb","Lustrous Orb","Griseous Orb","Soul Dew"]:
            eff*=1.2
        if other.type1 in dragoneff and other.teratype=="None":
            eff*=2
        if other.type2 in dragoneff and other.teratype=="None":
            eff*=2
        if other.type1 in dragonwk and other.teratype=="None":
            eff/=2
        if other.type2 in dragonwk and other.teratype=="None":
            eff/=2
        if other.teratype in dragoneff:
            eff*=2
        if other.teratype in dragonwk:
            eff/=2
        if (other.type1 in dragonimmune or other.type2 in dragonimmune and other.teratype=="None") or other.teratype in dragonimmune and other.item!="Ring Target":
            eff*=0
#        else:
#            eff*=1 
    #bug
    if self.atktype=="Bug":
        if other.ability=="Rattled":
            speedchange(other,self,0.5)
        if other.ability=="Wonder Guard" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves:
            print(f" 🛡️ {other.name}'s {other.ability}!")
            eff*=0
        if self.item in ["Silver Powder","Insect Plate"]:
            eff*=1.2
        if other.item=="Tanga Berry":
            eff*=0.5
            print(f" {other.name}'s {other.item} weakened the damage of {self.atktype}-type move!")
            self.item+="[Used]"
        if self.item == "Bug Gem":
            eff*=1.5
            print(f" 💎 {self.item} boosted {self.name}'s damage!")
            self.item+="[Used]"
        if self.ability=="Swarm" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves:
            if self.hp<=(self.maxhp/3):
                print(f" 🪲 {self.name}'s {self.ability}!")
                eff*=2.25
        if other.type1 in bugeff and other.teratype=="None":
            eff*=2
        if other.type2 in bugeff and other.teratype=="None":
            eff*=2
        if other.type1 in bugwk and other.teratype=="None":
            eff/=2
        if other.type2 in bugwk and other.teratype=="None":
            eff/=2
        if other.teratype in bugeff:
            eff*=2
        if other.teratype in bugwk:
            eff/=2
#        else:
#            eff*=1 
    #Water
    if self.atktype=="Water":
        if other.item=="Absorb Bulb":
            spatkchange(other,self,0.5)
            print(f" Absorb Bulb absorbed {self.name}'s Water-type moves energy and raised {other.name}'s Special Attack!")
            other.item+="[Used]"
        
        if other.ability=="Wonder Guard" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves:
            print(f" 🛡️ {other.name}'s {other.ability}!")
            eff*=0
        if other.ability=="Steam Engine" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves:
            print(f" 🚂 {other.name}'s {other.ability}!")
            speedchange(other,self,0.5)
            
        if self.item in  ["Mystic Water","Splash Plate","Lustrous Orb","Wave Incense","Sea Incense"]:
            eff*=1.2
        if other.item=="Passho Berry":
            eff*=0.5
            print(f" {other.name}'s {other.item} weakened the damage of {self.atktype}-type move!")
            self.item+="[Used]"
        if field.weather=="Desolate Land" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves  and "Cloud Nine" not in (self.ability,other.ability):
            eff*=0
        if self.item == "Water Gem":
            eff*=1.5
            print(f" 💎 {self.item} boosted {self.name}'s damage!")
            self.item+="[Used]"
        if other.ability in ["Storm Drain","Water Absorb","Dry Skin","Water Compaction"] and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves:
            if other.ability=="Water Compaction":
                print(f" 🚱 {other.name}'s {other.ability}.")
                defchange(other,self,1)
                
                eff*=0.5
            if other.ability=="Dry Skin" and "Cloud Nine" not in (self.ability,other.ability):
                eff*=0
                print(f" ♨️ {other.name}'s {other.ability}.")
                if other.hp<=other.maxhp-(other.maxhp/4):
                    other.hp+=other.maxhp/4
                    print(f" {other.name} gained some health.")
            if other.ability=="Storm Drain":
                eff*=0
                print(f" ⛈️ {other.name}'s {other.ability}.")
                spatkchange(other,self,0.5)
               
            if other.ability=="Water Absorb":
                eff*=0
                print(f" 💧 {other.name}'s {other.ability}.")
                if other.hp<other.maxhp:
                    print(f" {other.name} gained some health.")
                if other.hp<=other.maxhp-(other.maxhp/4):
                    other.hp+=other.maxhp/4
                if other.hp>other.maxhp-(other.maxhp/4):
                    other.hp=other.maxhp            
            
        if self.ability=="Torrent" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves:
            if self.hp<=(self.maxhp/3):
                print(f" 🌊 {self.name}'s {self.ability}!")
                eff*=2.25
        if other.type1 in watereff and other.teratype=="None":
            eff*=2
        if other.type2 in watereff and other.teratype=="None":
            eff*=2
        if other.type1 in waterwk and other.teratype=="None":
            eff/=2
        if other.type2 in waterwk and other.teratype=="None":
            eff/=2
        if other.teratype in watereff:
            eff*=2
        if other.teratype in waterwk:
            eff/=2
#        else:
#            eff*=1 
    #Ground
    if self.atktype=="Ground":
        if other.ability=="Earth Eater" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves:
            print(f" 🌍 {other.name}'s {other.ability}.")
            print(f" {other.name} gained some health.")
            if other.hp<=other.maxhp-(other.maxhp/4):
                other.hp+=other.maxhp/4
            if other.hp>other.maxhp-(other.maxhp/4):
                other.hp=other.maxhp
            
            eff*=0
        if other.ability=="Wonder Guard" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves:
            print(f" 🛡️ {other.name}'s {other.ability}!")
            eff*=0
        if other.item=="Air Balloon":
            eff*=0
        if self.ability=="Sand Force" and field.weather=="Sandstorm":
            eff*=1.3
        if self.item in ["Soft Sand","Earth Plate"]:
            eff*=1.2
        if other.item=="Shuca Berry":
            eff*=0.5
            print(f" {other.name}'s {other.item} weakened the damage of {self.atktype}-type move!")
            self.item+="[Used]"
        if self.item == "Ground Gem":
            eff*=1.5
            print(f" 💎 {self.item} boosted {self.name}'s damage!")
            self.item+="[Used]"
        if (other.ability=="Levitate" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves and self.grav is not True):
            print(f" 🛸 {other.name}'s {other.ability}.")
            eff*=0
        if other.type1 in groundeff and other.teratype=="None":
            eff*=2
        if other.type2 in groundeff and other.teratype=="None":
            eff*=2
        if other.type1 in groundwk and other.teratype=="None":
            eff/=2
        if other.type2 in groundwk and other.teratype=="None":
            eff/=2
        if other.teratype in groundeff:
            eff*=2
        if other.teratype in groundwk:
            eff/=2
        if (other.type1 in groundimmune or other.type2 in groundimmune and other.teratype=="None") or other.teratype in groundimmune and other.item!="Ring Target" and self.grav==False:
            if other.item!="Iron Ball":
                eff*=0
#        else:
#            eff*=1 
    #GRASS
    if self.atktype=="Grass":
        if other.ability=="Wonder Guard" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves:
            print(f" 🛡️ {other.name}'s {other.ability}!")
            eff*=0
        if self.item in ["Miracle Seed","Meadow Plate","Rose Incense"]:
            eff*=1.2
        if other.item=="Rindo Berry":
            eff*=0.5
            print(f" {other.name}'s {other.item} weakened the damage of {self.atktype}-type move!")
            self.item+="[Used]"
        if field.terrain=="Grassy" and (self.ability not in ["Levitate"] and "Flying" not in (self.type1,self.type2,self.teratype) or self.grav is True):
            eff*=1.3
        if self.item == "Grass Gem":
            eff*=1.5
            print(f" 💎 {self.item} boosted {self.name}'s damage!")
            self.item+="[Used]"
        if other.ability=="Sap Sipper":
            print(f" {other.name}'s {other.ability}.")
            eff*=0
            atkchange(other,self,0.5)
            
        if self.ability=="Overgrow":
            if self.hp<=(self.maxhp/3):
                print(f" 🌿 {self.name}'s {self.ability}.")
                eff*=2.25
        if other.type1 in grasseff and other.teratype=="None":
            eff*=2
        if other.type2 in grasseff and other.teratype=="None":
            eff*=2
        if other.type1 in grasswk and other.teratype=="None":
            eff/=2
        if other.type2 in grasswk and other.teratype=="None":
            eff/=2
        if other.teratype in grasseff:
            eff*=2
        if other.teratype in grasswk:
            eff/=2
#        else:
#            eff*=1
    #FLYING            
    if self.atktype=="Flying":
        if self.item in ["Sharp Beak","Sky Plate"]:
            eff*=1.2
        if other.item=="Koba Berry":
            eff*=0.5
            print(f" {other.name}'s {other.item} weakened the damage of {self.atktype}-type move!")
            self.item+="[Used]"
        if self.item == "Flying Gem":
            eff*=1.5
            print(f" 💎 {self.item} boosted {self.name}'s damage!")
            self.item+="[Used]"
        if other.type1 in flyingeff and other.teratype=="None":
            eff*=2
        if other.type2 in flyingeff and other.teratype=="None":
            eff*=2
        if other.type1 in flyingwk and other.teratype=="None":
            eff/=2
        if other.type2 in flyingwk and other.teratype=="None":
            eff/=2
        if other.teratype in flyingeff:
            eff*=2
        if other.teratype in flyingwk:
            eff/=2
#        else:
#            eff*=1            
    #FIRE            
    if self.atktype=="Fire":
        if other.ability=="Volcanic Body":
            print(f" 🌋 {other.name}'s {other.ability}.")
            print(f" {other.name} gained some health.")
            if other.hp<=other.maxhp-(other.maxhp/4):
                other.hp+=other.maxhp/4
            if other.hp>other.maxhp-(other.maxhp/4):
                other.hp=other.maxhp            
            eff*=0
        if other.tarshot is True:
            eff*=2
        if other.ability=="Fluffy" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves:
            eff*=2
        if other.ability=="Steam Engine" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves:
            print(f" 🚂 {other.name}'s {other.ability}!")
            speedchange(other,self,0.5)
         
        if self.item in ["Charcoal","Flame Plate"]:
            eff*=1.2
        if other.item=="Occa Berry":
            eff*=0.5
            print(f" {other.name}'s {other.item} weakened the damage of {self.atktype}-type move!")
            self.item+="[Used]"
        if other.ability=="Dry Skin" and "Cloud Nine" not in (self.ability,other.ability):
            print(f" {other.name}'s {other.ability}!")
            eff*=1.25
        if other.ability in ["Thick Fat","Heatproof"] and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves:
            print(f" 🌡️ {other.name}'s {other.ability}!")
            eff*=0.5
        if field.weather=="Primordial Sea" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves and "Cloud Nine" not in (self.ability,other.ability):
            eff*=0
        if self.item == "Fire Gem":
            eff*=1.5
            print(f" 💎 {self.item} boosted {self.name}'s damage!")
            self.item+="[Used]"
        if self.ability=="Blaze" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves:
            if self.hp<=(self.maxhp/3):
                print(f" 🔥 {self.name}'s {self.ability}!")
                eff*=2.25
        if other.ability=="Thermal Exchange" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves:
            print(f" 🌡️ {other.name}'s {other.ability}.")
            atkchange(other,self,0.5)
        if other.ability=="Flash Fire" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves:
            print(f" 🔥 {other.name}'s {other.ability}.")
            other.flashfire=True
            eff*=0
        if other.type1 in fireeff and other.teratype=="None":
            eff*=2
        if other.type2 in fireeff and other.teratype=="None":
            eff*=2
        if other.type1 in firewk and other.teratype=="None":
            eff/=2
        if other.type2 in firewk and other.teratype=="None":
            eff/=2
        if other.teratype in fireeff:
            eff*=2
        if other.teratype in firewk:
            eff/=2
#        else:
#            eff*=1        
    #Poison            
    if self.atktype=="Poison":
        if other.ability=="Wonder Guard" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves:
            print(f" 🛡️ {other.name}'s {other.ability}!")
            eff*=0
        if self.item in ["Poison Barb","Toxic Plate"]:
            eff*=1.2
        if other.item=="Kebia Berry":
            eff*=0.5
            print(f" {other.name}'s {other.item} weakened the damage of {self.atktype}-type move!")
            self.item+="[Used]"
        if self.item == "Poison Gem":
            eff*=1.5
            print(f" 💎 {self.item} boosted {self.name}'s damage!")
            self.item+="[Used]"
        if other.type1 in poisoneff and other.teratype=="None":
            eff*=2
        if other.type2 in poisoneff and other.teratype=="None":
            eff*=2
        if other.type1 in poisonwk and other.teratype=="None":
            eff/=2
        if other.type2 in poisonwk and other.teratype=="None":
            eff/=2
        if other.teratype in poisoneff:
            eff*=2
        if other.teratype in poisonwk:
            eff/=2
        if (other.type1 in poisonimmune or other.type2 in poisonimmune and other.teratype=="None") or other.teratype in poisonimmune and other.item!="Ring Target":
            if self.ability!="Corrosion":
                eff*=0
            else:
                print(f" ☠️ {self.name}'s {self.ability}.")
#        else:
#            eff*=1   
    #Rock
    if self.atktype=="Rock":
        if other.ability=="Lithogen" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves:
            print(f" 🪨 {other.name}'s {other.ability}.")
            print(f" {other.name} gained some health.")
            if other.hp<=other.maxhp-(other.maxhp/4):
                other.hp+=other.maxhp/4
            if other.hp>other.maxhp-(other.maxhp/4):
                other.hp=other.maxhp
            
            eff*=0
        if other.ability=="Mountaineer" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves:
            print(f" 🧗🏻‍♂️{other.name}'s {other.ability}!")
            eff*=0
        if self.ability=="Sand Force" and field.weather=="Sandstorm":
            eff*=1.3
        if self.item in ["Hard Stone","Stone Plate","Rock Incense"]:
            eff*=1.2
        if other.item=="Charti Berry":
            eff*=0.5
            print(f" {other.name}'s {other.item} weakened the damage of {self.atktype}-type move!")
            self.item+="[Used]"
        if other.ability=="Delta Stream" and "Flying" in (other.type1,other.type2) and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves:
            eff*=0.5
        if self.item == "Rock Gem":
            eff*=1.5
            print(f" 💎 {self.item} boosted {self.name}'s damage!")
            self.item+="[Used]"
        if other.type1 in rockeff and other.teratype=="None":
            eff*=2
        if other.type2 in rockeff and other.teratype=="None":
            eff*=2
        if other.type1 in rockwk and other.teratype=="None":
            eff/=2
        if other.type2 in rockwk and other.teratype=="None":
            eff/=2
        if other.teratype in rockeff:
            eff*=2
        if other.teratype in rockwk:
            eff/=2
#        else:
#            eff*=1                          
    #Normal
    if self.atktype=="Normal":
        if other.ability=="Wonder Guard" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves:
            print(f" 🛡️ {other.name}'s {other.ability}!")
            eff*=0
        if self.item in ["Silk Scarf","Blank Plate","Legend Plate"]:
            eff*=1.2
        if other.item=="Chilan Berry":
            eff*=0.5
            print(f" 🫐 {other.name}'s {other.item} weakened the damage of {self.atktype}-type move!")
            self.item+="[Used]"
        if self.item == "Normal Gem":
            eff*=1.5
            print(f" 💎 {self.item} boosted {self.name}'s damage!")
            self.item+="[Used]"
        if other.type1 in normaleff and other.teratype=="None":
            eff*=2
        if other.type2 in normaleff and other.teratype=="None":
            eff*=2
        if other.type1 in normalwk and other.teratype=="None":
            eff/=2
        if other.type2 in normalwk and other.teratype=="None":
            eff/=2
        if other.teratype in normaleff:
            eff*=2
        if other.teratype in normalwk:
            eff/=2
        if (other.type1 in normalimmune or other.type2 in normalimmune and other.teratype=="None") or (other.teratype in normalimmune and other.item!="Ring Target"):
            if self.ability!="Scrappy":
                eff*=0
            else:
                print(f" {self.name}'s {self.ability}.")
#        else:
#            eff*=1       
    #Fighting
    if self.atktype=="Fighting":
        if other.ability=="Wonder Guard" and self.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and other.use not in typemoves.abilityigmoves:
            print(f" 🛡️ {other.name}'s {other.ability}!")
            eff*=0
        if self.item in["Black Belt","Fist Plate"]:
            eff*=1.2
        if other.item=="Chople Berry":
            eff*=0.5
            print(f" {other.name}'s {other.item} weakened the damage of {self.atktype}-type move!")
            self.item+="[Used]"
        if self.item == "Fighting Gem":
            eff*=1.5
            print(f" 💎 {self.item} boosted {self.name}'s damage!")
            self.item+="[Used]"
        if other.type1 in fightingeff and other.teratype=="None":
            eff*=2
        if other.type2 in fightingeff and other.teratype=="None":
            eff*=2
        if other.type1 in fightingwk and other.teratype=="None":
            eff/=2
        if other.type2 in fightingwk and other.teratype=="None":
            eff/=2
        if other.teratype in fightingeff:
            eff*=2
        if other.teratype in fightingwk:
            eff/=2
        if (other.type1 in fightingimmune or other.type2 in fightingimmune and other.teratype=="None") or other.teratype in fightingimmune and other.item!="Ring Target":
            eff*=0     
#        else:
#            eff*=1 
    if eff>=2:
        print(" 🟢 It's super effective!") 
        if self.ability=="Primal Armor":
            eff*=0.5
        if self.ability=="Fatal Precision":
            eff*=1.2
        if other.item=="Enigma Berry":
            other.hp+=round(other.maxhp/4)
            "None"
        if other.item=="Weakness Policy":
            print(f" 📄 {other.name}'s {other.item}.")
            other.item+="[Used]"
            atkchange(other,self,1)
            spatkchange(other,self,1)
         
        if self.item=="Expert Belt":
            eff*=1.2
        if other.ability in ["Solid Rock","Filter","Prism Armor"]:
            print(f" {other.name}'s {other.ability}.")
            eff*=0.75
                
    elif eff==1:
        pass
    elif eff<1 and eff!=0:
        print(" 🟡 It's not very effective...")
        if self.ability=="Tinted Lens":
            print(f" {self.name}'s {self.ability}.")
            print(" Tinted Lens strengthen the power of not very effective move.")
            eff*=2
    elif eff==0:
        if "Legendary" in self.name:
            eff=0.5
        else:
            print(f" 🔴 Doesn't effect on {other.name}.")
     
                               
    #STAB              
    if self.atktype in (self.type1,self.type2,self.teratype):
        if self.teratype in (self.type1,self.type2):
            stab=2
        if self.ability=="Adaptability":
            print(f" {self.name}'s {self.ability}.")
            stab=2
        else:
            stab=1.5
    return [eff,stab]
    
#CRITICAL    
def critch(self,other,num="None"):
    if num =="None":
        num=1
    if "Sirfetch" in self.name and self.item=="Leek":
        num*=4
    if "Chansey" in self.name and self.item=="Lucky Punch":
        num*=4
    if self.item in ["Scope Lens","Razor Claw"]:
        num*=2
    if self.ability=="Super Luck":
        num*=2
    crit=round(16/(self.critrate*num))
    if crit<1:
        crit=1
    if crit>1:
        crit=random.randint(1,crit)
    if self.ability=="Merciless" and other.status=="Badly Poisoned":
        crit=1
    if crit==1 and other.ability not in ["Shell Armor","Battle Armor"]:
        if self.owner.lightscreen is True:
            self.spdef/=2
        if self.owner.reflect is True:
            self.defense/=2
        if self.owner.reflect is True:
            self.defense/=2
        if self.atkb<1:
            self.atk/=self.atkb
        if self.spatkb<1:
            self.spatk/=self.spatkb
        if other.defb>1:
            other.defense/=other.defb
        if other.spdefb>1:
            other.spdef/=other.spdefb
        if other.ability=="Anger Point":
            print(f" {other.name}'s {other.ability}.")
            atkchange(other,self,4)
        if self.ability=="Sniper":
            print(colored(" It's a critical hit.","red"))
            return 2.25
        else:
            print(colored(" It's a critical hit.","red"))
            return 1.5
    if other.ability in ["Shell Armor","Battle Armor"] and crit==1:
        return 1
    else:
        return 1
def showmon(trainer):
	a=0
	
	print("======================================")
	for i in trainer.pokemons:
	    a+=1
	    print("  "+str(a)+"."+i.name+f" ({i.hp}/{i.maxhp}) "+f"[{i.status}]")      
	 
	print("======================================")
#	for j in trainer.faintedmon:
#	    b+=1
#	    print("   "+str(b)+"."+j.name+f" ({j.hp}/{j.maxhp}) "+f"[{j.status}]")
#	if len(trainer.faintedmon)!=0:
#	    print(" ======================================")
#RANDOM DAMAGE ROLL
def randroll():
    
    rr=random.randint(85,100)       
    return rr/100
    
def prebuff(self,other,tr1,turn,field):
    atkbuff=1
    defbuff=1
    spatkbuff=1
    spdefbuff=1
    speedbuff=1   
    typemoves.hpselect(self)
    typemoves.teraselect(self)
    if self.maxiv!="No":
        self.geniv()
    if self.flashfire==True:
        atkbuff*=1.5
        spatkbuff*=1.5
    if self.ability=="Schooling" and "School" not in self.name and self.hp>(self.maxhp*0.25):
        print(f" 🐋 {self.name}'s {self.ability}!")
        print(" Wishiwashi formed a school!")
        self.name="School Wishiwashi"
        per=self.hp/self.maxhp
        self.hp=55
        self.atk=140
        self.defense=130
        self.spatk=140
        self.spdef=135
        self.speed=30
        self.calcst()
        self.hp=self.maxhp*per
    if self.ability=="RKS System" and (self.item=="None" or self.item not in ["Rock Memory","Fire Memory","Water Memory","Grass Memory","Electric Memory","Ground Memory","Flying Memory","Fighting Memory","Fairy Memory","Dragon Memory","Steel Memory","Poison Memory","Dark Memory","Ghost Memory","Normal Memory","Bug Memory","Ice Memory"]):
        self.name="Silvally"
    if self.ability=="Multitype" and (self.item=="None" or self.item not in ["Draco Plate","Dread Plate","Earth Plate","Fist Plate","Flame Plate","Icicle Plate","Insect Plate","Iron Plate","Meadow Plate","Mind Plate","Pixie Plate","Sky Plate","Splash Plate","Spooky Plate","Stone Plate","Toxic Plate","Zap Plate"]):
        self.name="Arceus"
    #if "Erika(Hard Mode)" in (self.owner.name,other.owner.name) or "Erika(Hardcore Mode)" in (self.owner.name,other.owner.name):
#        field.terrain="Grassy"
    if self.item!="None" and "Choice" not in self.item:
        self.choiced=False
        self.choicedmove="None"
    if tr1.auroraveil is True:
        if turn==tr1.avendturn:
            tr1.auroraveil=False
            print(" ⚠️The Aurora Veil wore off!")  
        else:
            defbuff*=2
            spdefbuff*=2        
    if tr1.tailwind is True:        
        if turn==tr1.twendturn:
            tr1.tailwind=False
            print(" ⚠️The Tailwind petered out!") 
        else:
            speedbuff*=2     
    if tr1.reflect is True:
        if turn==tr1.rfendturn:
            tr1.reflect=False
            print(" ⚠️The Reflect wore off!")
        else:
            defbuff*=2
    if tr1.lightscreen is True:
        if turn==tr1.screenend:
            tr1.lightscreen=False
            print(" ⚠️The Light Screen wore off!") 
        else:
            spdefbuff*=2                
    if self.item=="Float Stone":
        defbuff*=0.5
        spdefbuff*=0.5
    if self.item=="Iron Ball":
        speedbuff*=0.5
    if len(self.moves)==0:
        self.moves=["Struggle"]
        self.pplist=[100]
    if self.item=="Wise Glasses":
        spatkbuff*=1.1
    if self.item=="Muscle Band":
        atkbuff*=1.1
    if self.ability=="Zen Mode":
        if "Zen" not in self.name:
            print(f" 🎎 {self.name}'s {self.ability}!")
            self.name+="-Zen"
            if "Galarian" in self.name:
                self.type1,self.type2="Ice","Fire"
                per=self.hp/self.maxhp
                self.hp=105
                self.atk=160
                self.defense=55
                self.spatk=30
                self.spdef=55
                self.speed=135
                self.calcst()
                self.hp=self.maxhp*per
            if "Galarian" not in self.name:
                self.type1,self.type2="Fire","Psychic"
                per=self.hp/self.maxhp
                self.hp=105
                self.atk=30
                self.defense=105
                self.spatk=140
                self.spdef=105
                self.speed=55
                self.calcst()
                self.hp=self.maxhp*per
    if self.ability=="Flower Gift" and field.weather in ["Sunny","Desolate Land"]:
        speedbuff*=1.5
        atkbuff*=1.5
    if self.ability=="Illusion" and "Zoroark" not in self.name:
        atkbuff*=1.3
        spatkbuff*=1.3
        if self.ability=="Quick Feet" and self.status!="Alive":
            speedbuff*=2
        if self.ability in ["Bull Rush","Quill Rush"] and self.bullrush==True:
            speedbuff*=1.5
            atkbuff*=1.2
        if field.weather=="Strong Winds" and "Delta Stream" not in (self.ability,other.ability):
            print(" 🍃 The mysterious strong winds have dissipated!")
            field.weather="Clear"
    if "Air Lock" in self.ability:
        field.weather="Clear"
    if "Delta Stream" in self.ability:
        field.weather="Strong Winds"
    if other.ability=="Screen Cleaner":
        tr1.lightscreen=False
        tr1.reflect=False
        tr1.auroraveil=False
    if self.ability=="Unburden" and (self.item=="None" or "Used" in self.item):
        speedbuff*=2
    if self.ability=="Grass Pelt" and field.terrain=="Grassy":
        defbuff*=1.5
    if self.ability=="Forecast":
        if field.weather=="Clear":
            self.type1="Normal"
        if field.weather=="Sandstorm":
            self.type1="Rock"
        if field.weather=="Snowstrom":
            self.type1="Ice"
        if field.weather=="Rainy":
            self.type1="Water"
        if field.weather=="Sunny":
            self.type1="Fire"
    if self.ability=="Defeatist" and self.hp<=(self.maxhp/3):
        atkbuff*=0.5
        spatkbuff*=0.5
    if "Poison" in self.status and self.ability=="Toxic Boost":
        atkbuff*=1.5
    if self.ability=="Supreme Overlord":
        atkbuff*=1+0.1*(6-len(tr1.pokemons))
        spatkbuff*=1+0.1*(6-len(tr1.pokemons))
    if field.weather in ["Sunny","Desolate Land"] and self.ability=="Orichalcum Pulse":
        atkbuff*=1.34
    if field.terrain=="Electric" and self.ability=="Hadron Engine":
        spatkbuff*=1.34
    if ("Protosynthesis" in self.ability and (field.weather in ["Sunny","Desolate Land"] or self.item=="Booster Energy")) or self.ability in ["Protosynthesis [Attack]","Protosynthesis [Sp. Attack]","Protosynthesis [Defense]","Protosynthesis [Sp. Defense]","Protosynthesis [Speed]"]:
        if field.weather not in ["Sunny","Desolate Land"] and "[" not in self.ability:
            print(f" 💊 {self.name} used its Booster Energy to raise its best stat!")
            self.item+="[Used]"
        m=[a,b,c,d,e]=[self.atk,self.defense,self.spatk,self.spdef,self.speed]
        if tr1.reflect==True:
            m=[self.atk,self.defense/2,self.spatk,self.spdef,self.speed]
        if tr1.lightscreen==True:
            m=[self.atk,self.defense,self.spatk,self.spdef/2,self.speed]
        x=max(m)
        if x==a or "[Attack" in self.ability:
        	atkbuff*=1.3
        	self.ability="Protosynthesis [Attack]"
        elif x==b or "[Defense" in self.ability:
        	defbuff*=1.3
        	self.ability="Protosynthesis [Defense]"
        elif x==c or "[Sp. Attack" in self.ability:
        	spatkbuff*=1.3
        	self.ability="Protosynthesis [Sp. Attack]"
        elif x==d or "[Sp. Defense" in self.ability:
        	spdefbuff*=1.3
        	self.ability="Protosynthesis [Sp. Defense]"
        elif x==e or "Speed" in self.ability:
        	speedbuff*=1.5
        	self.ability="Protosynthesis [Speed]"
    if ("Quark Drive" in self.ability and (field.terrain=="Electric" or self.item=="Booster Energy")) or self.ability in ["Quark Drive [Attack]","Quark Drive [Sp. Attack]","Quark Drive [Defense]","Quark Drive [Sp. Defense]","Quark Drive [Speed]"]:
        if field.terrain not in ["Electric"] and "[" not in self.ability:
            print(f" 💊 {self.name} used its Booster Energy to raise its best stat!")
            self.item+="[Used]"
        m=[a,b,c,d,e]=[self.atk,self.defense,self.spatk,self.spdef,self.speed]
        if tr1.reflect==True:
            m=[self.atk,self.defense/2,self.spatk,self.spdef,self.speed]
        if tr1.lightscreen==True:
            m=[self.atk,self.defense,self.spatk,self.spdef/2,self.speed]
        x=max(m)
        if x==a or "[Attack" in self.ability:
        	atkbuff*=1.3
        	self.ability="Quark Drive [Attack]"
        elif x==b or "[Defense" in self.ability:
        	defbuff*=1.3
        	self.ability="Quark Drive [Defense]"
        elif x==c or "[Sp. Attack" in self.ability:
        	spatkbuff*=1.3
        	self.ability="Quark Drive [Sp. Attack]"
        elif x==d or "[Sp. Def" in self.ability:
        	spdefbuff*=1.3
        	self.ability="Quark Drive [Sp. Defense]"
        elif x==e or "Speed" in self.ability:
        	speedbuff*=1.5
        	self.ability="Quark Drive [Speed]"
    if field.trickroom==True and self.item=="Room Service":
        speedchange(self,other,-0.5)       	
    if field.terrain=="Misty":
        if self.item=="Misty Seed":
            print(f" 🍇 {self.name} consumed {self.item} and raised its Sp.Def!")
            spdefchange(self,other,0.5)
            self.item+="[Used]"
    if field.terrain=="Electric":
        if self.item=="Electric Seed":
            print(f" 🍇 {self.name} consumed {self.item} and raised its Sp.Def!")
            spdefchange(self,other,0.5)
            self.item+="[Used]"
    if field.terrain=="Psychic":
        if self.item=="Psychic Seed":
            print(f" 🍇 {self.name} consumed {self.item} and raised its Sp.Def!")
            spdefchange(self,other,0.5)
            self.item+="[Used]"
    if field.terrain=="Grassy":
        if self.item=="Grassy Seed":
            print(f" 🍇 {self.name} consumed {self.item} and raised its Sp.Def!")
            spdefchange(self,other,0.5)
            self.item+="[Used]"
    if other.ability=="Vessel of Ruin":
        spatkbuff*=0.75
    if other.ability=="Tablets of Ruin":
        atkbuff*=0.75
    if other.ability=="Sword of Ruin":
        defbuff*=0.75
    if other.ability=="Beads of Ruin":
        spdefbuff*=0.75
        self.protect=False    
    if field.terrain=="Misty":
        if turn>=field.misendturn:
            print(" 🌐 The battlefield turned normal.")
            field.terrain="Normal"
    if field.terrain=="Psychic":
        if turn>=field.psyendturn:
            print(" 🌐 The battlefield turned normal.")
            field.terrain="Normal"
    if field.terrain=="Electric":
        if turn>=field.eleendturn:
            print(" 🌐 The battlefield turned normal.")
            field.terrain="Normal"
    if field.terrain=="Grassy":
        if turn>=field.grassendturn:
            print(" 🌐 The battlefield turned normal.")
            field.terrain="Normal"
    if field.weather=="Snowstorm":
        if turn>=field.snowstormendturn:
            print(" 🌥️The snowstorm stopped.")
            field.weather="Cloudy"            
    if field.weather=="Hail":
        if turn>=field.hailendturn:
            print(" 🌥️The hail stopped.")
            field.weather="Cloudy"
    if field.weather=="Sandstorm":
        if turn>=field.sandendturn:
            print(" 🌥️The sandstorm subsided.")
            field.weather="Clear"
    if field.weather=="Sunny":
        if turn>=field.sunendturn:
            print(" 🌤️The harsh sunlight faded.")
            field.weather="Clear"
    if field.weather=="Rainy":
        if turn>=field.rainendturn:
            print(" 🌦️The rain stopped.")
            field.weather="Cloudy"
#    if tr1.auroraveil is True:
#        defbuff*=2
#        spdefbuff*=2
#    if tr1.tailwind is True:
#        speedbuff*=2
#    if tr1.reflect is True:
#        defbuff*=2
#    if tr1.lightscreen is True:
#        spdefbuff*=2
    if self.ability=="Guts" and self.status!="Alive":
        atkbuff*=1.5
    if self.ability=="Feline Prowess":
        spatkbuff*=2
    if field.terrain=="Electric" and self.ability=="Surge Surfer":
        speedbuff*=2
    if self.status=="Paralyzed" and self.ability!="Quick Feet":
        speedbuff*=0.5
    if self.status=="Frostbite":
        spatkbuff*=0.5
    if self.status=="Burned" and self.ability!="Guts":
        atkbuff*=0.5
    if ("Pikachu" or "Sparky") in self.name and (self.item=="Light Ball" or "Ash" in self.owner.name):
        atkbuff*=2
        spatkbuff*=2
    if self.ability=="Marvel Scale" and self.status!="Alive":
        defbuff*=1.5
    if self.ability=="Hustle":
        atkbuff*=1.5
    if self.ability=="Flare Boost" and self.status=="Burned":
        spatkbuff*=1.5
    if field.weather in ["Rainy","Primordial Sea"] and self.ability=="Swift Swim" and "Cloud Nine" not in (self.ability,other.ability):
        speedbuff*=2
    if field.weather in ["Sunny","Desolate Land"] and self.ability=="Chlorophyll" and "Cloud Nine" not in (self.ability,other.ability):
        speedbuff*=2
    if field.weather in ["Sandstorm"] and self.ability=="Sand Rush" and "Cloud Nine" not in (self.ability,other.ability):
        speedbuff*=2
    if field.weather in ["Hail","Snowstorm"] and self.ability=="Slush Rush" and "Cloud Nine" not in (self.ability,other.ability):
        speedbuff*=2
    if field.weather in ["Snowstorm"] and ("Ice" in (self.type1,self.type2,self.teratype)) and "Cloud Nine" not in (self.ability,other.ability):
        defbuff*=1.5
    if field.weather in ["Sandstorm"] and ("Rock" in (self.type1,self.type2,self.teratype)) and "Cloud Nine" not in (self.ability,other.ability):
        spdefbuff*=1.5
    if other.ability=="Fur Coat":
        atkbuff*=0.5
    if self.ability=="Ice Scales":
        spdefbuff*=2
    if self.ability=="Sage Power":
        spatkbuff*=1.5
    if self.ability=="Gorilla Tactics":
        atkbuff*=1.5
    if self.item=="Choice Band" and self.dmax is False:
        atkbuff*=1.5
    if self.item=="Choice Specs" and self.dmax is False:
        spatkbuff*=1.5
    if self.item=="Choice Scarf" and self.dmax is False:
        speedbuff*=1.5
    if self.item=="Assault Vest":
        spdefbuff*=1.5
    if self.ability=="Typeless":
        self.type1=self.atktype
    if self.ability in ["Huge Power","Pure Power"]:
        atkbuff*=2
    if self.item=="Life Orb":
        atkbuff*=1.3
        spatkbuff*=1.3
    if self.item=="Eviolite":
        defbuff*=1.5
        spdefbuff*=1.5
    self.atk=self.maxatk*self.atkb*atkbuff
    self.defense=self.maxdef*self.defb*defbuff
    self.spatk=self.maxspatk*self.spatkb*spatkbuff
    self.spdef=self.maxspdef*self.spdefb*spdefbuff
    self.speed=self.maxspeed*self.speedb*speedbuff
#    self.natureboost()
#


def atkchange(self,other,amount):
    if self.ability in ["Big Pecks","Clear Body","Flower Veil","Full Metal Body","White Smoke","Hyper Cutter","Keen Eye"] and amount<0 and other.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and self!=other:
        print(f" {self.name}'s {self.ability}!")
        amount=0
    if self.ability=="Simple":
        amount*=2
    if self.ability=="Defiant" and self!=other:
        if amount<0:
            print(f" {self.name}'s {self.ability}!")
            atkchange(self,other,1)
    if self.ability=="Competitive" and self!=other:
        if amount<0:
            print(f" {self.name}'s {self.ability}!")
            spatkchange(self,other,1)
    if self.ability=="Contrary":
        amount=-amount
    if amount<4:
        if amount>=1.5:
            print(f" ⏫ {self.name}'s attack drastically rose!")
        if amount==1:
            print(f" ⏫ {self.name}'s attack sharply rose!")
        if amount==0.5:
            print(f" 🔼 {self.name}'s attack rose!")
        if amount==-0.5:
            print(f" 🔽 {self.name}'s attack fell!")
        if amount<=-1:
            print(f" ⏬ {self.name}'s attack harshly fell!")
    if amount==0.5:#+1
        if self.atkb==0.249:
            self.atkb=0.285
        elif self.atkb==0.285:
            self.atkb==0.333
        elif self.atkb==0.333:
            self.atkb==0.4
        elif self.atkb==0.4:
            self.atkb==0.5
        elif self.atkb==0.5:
            self.atkb==0.667
        elif self.atkb==0.667:
            self.atkb=1
        elif self.atkb>=1:
            self.atkb+=amount
        elif self.atkb>4:
            self.atkb=4  
    if amount==1:#+2
        if self.atkb==0.249:
            self.atkb=0.333
        elif self.atkb==0.285:
            self.atkb=0.4
        elif self.atkb==0.336:
            self.atkb=0.5
        elif self.atkb==0.4:
            self.atkb=0.667
        elif self.atkb==0.5:
            self.atkb=1
        elif self.atkb==0.667:
            self.atkb=1.5
        elif self.atkb>=1:
            self.atkb+=(amount*1)     
        elif self.atkb>3:
            self.atkb=4        
    if amount==1.5:#+3
        if self.atkb==0.249:
            self.atkb=0.4
        elif self.atkb==0.285:
            self.atkb=0.5
        elif self.atkb==0.333:
            self.atkb=0.667
        elif self.atkb==0.4:
            self.atkb=1
        elif self.atkb==0.5:
            self.atkb=1.5
        elif self.atkb==0.667:
            self.atkb=2
        elif self.atkb==1:
            self.atkb=2.5
        elif self.atkb==1.5:
            self.atkb=3
        elif self.atkb==2:
            self.atkb=3.5
        elif self.atkb==2.5:
            self.atkb=4
        elif self.atkb>2.5:
            self.atkb=4
    if amount==2:#+4    
        if self.atkb==0.249:
            self.atkb=0.5   
        elif self.atkb==0.285:
            self.atkb=0.667
        elif self.atkb==0.333:
            self.atkb=1
        elif self.atkb==0.4:
            self.atkb=1.5
        elif self.atkb==0.5:
            self.atkb=2
        elif self.atkb==0.667:
            self.atkb=2.5
        elif self.atkb==1:
            self.atkb=3
        elif self.atkb==1.5:
            self.atkb=3.5
        elif self.atkb==2:
            self.atkb=4
    if amount==4:#+6
        if self.atkb==0.249:
            self.atkb=1  
        elif self.atkb==0.285:
            self.atkb=1.5
        elif self.atkb==0.333:
            self.atkb=2
        elif self.atkb==0.4:
            self.atkb=2.5
        elif self.atkb==0.5:
            self.atkb=3
        elif self.atkb==0.667:
            self.atkb=3.5
        elif self.atkb==1:
            self.atkb=4
        elif self.atkb>1:
            self.atkb=4
    if amount==-0.5:
        if 0.249<self.atkb<=1:
            self.atkb=round(1/((1/self.atkb)-amount),3)
        if 1<self.atkb<=4:
            self.atkb=self.atkb+amount
        
    if amount==-1:
        if self.atkb>1:
            self.atkb+=amount
        elif self.atkb==1:
            self.atkb=0.5
        elif self.atkb==0.667:
            self.atkb=0.4
        elif self.atkb==0.5:
            self.atkb=0.333
        elif self.atkb==0.4:
            self.atkb=0.285
        elif self.atkb==0.333:
            self.atkb=0.249
        elif self.atkb<=0.285:
            self.atkb=0.249
    if self.atkb>4:
        self.atkb=4


def defchange(self,other,amount):
    if self.ability in ["Big Pecks","Clear Body","Flower Veil","Full Metal Body","White Smoke","Hyper Cutter","Keen Eye"] and amount<0 and other.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and self!=other:
        print(f" {self.name}'s {self.ability}!")
        amount=0
    if self.ability=="Simple":
        amount*=2
    if self.ability=="Big Pecks" and amount<0:
        amount=0
    if self.ability=="Defiant" and self!=other:
        if amount<0:
            print(f" {self.name}'s {self.ability}!")
            atkchange(self,other,1)
    if self.ability=="Competitive" and self!=other:
        if amount<0:
            print(f" {self.name}'s {self.ability}!")
            spatkchange(self,other,1)
    if self.ability=="Contrary":
        amount=-amount
    if amount<4:
        if amount>=1.5:
            print(f" ⏫ {self.name}'s defense drastically rose!")
        if amount==1:
            print(f" ⏫ {self.name}'s defense sharply rose!")
        if amount==0.5:
            print(f" 🔼 {self.name}'s defense rose!")
        if amount==-0.5:
            print(f" 🔽 {self.name}'s defense fell!")
        if amount<=-1:
            print(f" ⏬ {self.name}'s defense harshly fell!")
    if amount==0.5:#+1
        if self.defb==0.249:
            self.defb=0.285
        elif self.defb==0.285:
            self.defb==0.333
        elif self.defb==0.333:
            self.defb==0.4
        elif self.defb==0.4:
            self.defb==0.5
        elif self.defb==0.5:
            self.defb==0.667
        elif self.defb==0.667:
            self.defb==1
        elif self.defb>=1:
            self.defb+=amount      
        elif self.defb>4:
            self.defb=4  
    elif amount==1:#+2
        if self.defb==0.249:
            self.defb=0.333
        elif self.defb==0.285:
            self.defb=0.4
        elif self.defb==0.336:
            self.defb=0.5
        elif self.defb==0.4:
            self.defb=0.667
        elif self.defb==0.5:
            self.defb=1
        elif self.defb==0.667:
            self.defb=1.5
        elif self.defb>=1:
            self.defb+=(amount*1)     
        elif self.defb>3:
            self.defb=4        
    elif amount==1.5:#+3
        if self.defb==0.249:
            self.defb=0.4
        elif self.defb==0.285:
            self.defb=0.5
        elif self.defb==0.333:
            self.defb=0.667
        elif self.defb==0.4:
            self.defb=1
        elif self.defb==0.5:
            self.defb=1.5
        elif self.defb==0.667:
            self.defb=2
        elif self.defb==1:
            self.defb=2.5
        elif self.defb==1.5:
            self.defb=3
        elif self.defb==2:
            self.defb=3.5
        elif self.defb==2.5:
            self.defb=4
        elif self.defb>2.5:
            self.defb=4
    elif amount==2:#+4    
        if self.defb==0.249:
            self.defb=0.5   
        elif self.defb==0.285:
            self.defb=0.667
        elif self.defb==0.333:
            self.defb=1
        elif self.defb==0.4:
            self.defb=1.5
        elif self.defb==0.5:
            self.defb=2
        elif self.defb==0.667:
            self.defb=2.5
        elif self.defb==1:
            self.defb=3
        elif self.defb==1.5:
            self.defb=3.5
        elif self.defb==2:
            self.defb=4
    elif amount==4:#+6
        if self.defb==0.249:
            self.defb=1  
        elif self.defb==0.285:
            self.defb=1.5
        elif self.defb==0.333:
            self.defb=2
        elif self.defb==0.4:
            self.defb=2.5
        elif self.defb==0.5:
            self.defb=3
        elif self.defb==0.667:
            self.defb=3.5
        elif self.defb==1:
            self.defb=4
        elif self.defb>1:
            self.defb=4
    elif amount==-0.5:
        if 0.249<self.defb<=1:
            self.defb=round(1/((1/self.defb)-amount),3)
        if 1<self.defb<=4:
            self.defb=self.defb+amount
        
    elif amount==-1:
        if self.defb>1:
            self.defb+=amount
        elif self.defb==1:
            self.defb=0.5
        elif self.defb==0.667:
            self.defb=0.4
        elif self.defb==0.5:
            self.defb=0.333
        elif self.defb==0.4:
            self.defb=0.285
        elif self.defb==0.333:
            self.defb=0.249
        elif self.defb<=0.285:
            self.defb=0.249
    if self.defb>4:
        self.defb=4
def spatkchange(self,other,amount):
    if self.ability in ["Big Pecks","Clear Body","Flower Veil","Full Metal Body","White Smoke","Hyper Cutter","Keen Eye"] and amount<0 and other.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and self!=other:
        print(f" {self.name}'s {self.ability}!")
        amount=0
    if self.ability=="Simple":
        amount*=2
    if self.ability=="Defiant" and self!=other:
        if amount<0:
            print(f" {self.name}'s {self.ability}!")
            atkchange(self,other,1)
    if self.ability=="Competitive" and self!=other:
        if amount<0:
            print(f" {self.name}'s {self.ability}!")
            spatkchange(self,other,1)
    if self.ability=="Contrary":
        amount=-amount
    if amount<4:
        if amount>=1.5:
            print(f" ⏫ {self.name}'s special attack drastically rose!")
        if amount==1:
            print(f" ⏫ {self.name}'s special attack sharply rose!")
        if amount==0.5:
            print(f" 🔼 {self.name}'s special attack rose!")
        if amount==-0.5:
            print(f" 🔽 {self.name}'s special attack fell!")
        if amount<=-1:
            print(f" ⏬ {self.name}'s special attack harshly fell!")
    if amount==0.5:#+1
        if self.spatkb==0.249:
            self.spatkb=0.285
        elif self.spatkb==0.285:
            self.spatkb==0.333
        elif self.spatkb==0.333:
            self.spatkb==0.4
        elif self.spatkb==0.4:
            self.spatkb==0.5
        elif self.spatkb==0.5:
            self.spatkb==0.667
        elif self.spatkb==0.667:
            self.spatkb==1
        elif self.spatkb>=1:
            self.spatkb+=amount      
        elif self.spatkb>4:
            self.spatkb=4  
    elif amount==1:#+2
        if self.spatkb==0.249:
            self.spatkb=0.333
        elif self.spatkb==0.285:
            self.spatkb=0.4
        elif self.spatkb==0.336:
            self.spatkb=0.5
        elif self.spatkb==0.4:
            self.spatkb=0.667
        elif self.spatkb==0.5:
            self.spatkb=1
        elif self.spatkb==0.667:
            self.spatkb=1.5
        elif self.spatkb>=1:
            self.spatkb+=(amount*1)     
        elif self.spatkb>3:
            self.spatkb=4        
    elif amount==1.5:#+3
        if self.spatkb==0.249:
            self.spatkb=0.4
        elif self.spatkb==0.285:
            self.spatkb=0.5
        elif self.spatkb==0.333:
            self.spatkb=0.667
        elif self.spatkb==0.4:
            self.spatkb=1
        elif self.spatkb==0.5:
            self.spatkb=1.5
        elif self.spatkb==0.667:
            self.spatkb=2
        elif self.spatkb==1:
            self.spatkb=2.5
        elif self.spatkb==1.5:
            self.spatkb=3
        elif self.spatkb==2:
            self.spatkb=3.5
        elif self.spatkb==2.5:
            self.spatkb=4
        elif self.spatkb>2.5:
            self.spatkb=4
    elif amount==2:#+4    
        if self.spatkb==0.249:
            self.spatkb=0.5   
        elif self.spatkb==0.285:
            self.spatkb=0.667
        elif self.spatkb==0.333:
            self.spatkb=1
        elif self.spatkb==0.4:
            self.spatkb=1.5
        elif self.spatkb==0.5:
            self.spatkb=2
        elif self.spatkb==0.667:
            self.spatkb=2.5
        elif self.spatkb==1:
            self.spatkb=3
        elif self.spatkb==1.5:
            self.spatkb=3.5
        elif self.spatkb==2:
            self.spatkb=4
    elif amount==4:#+6
        if self.spatkb==0.249:
            self.spatkb=1  
        elif self.spatkb==0.285:
            self.spatkb=1.5
        elif self.spatkb==0.333:
            self.spatkb=2
        elif self.spatkb==0.4:
            self.spatkb=2.5
        elif self.spatkb==0.5:
            self.spatkb=3
        elif self.spatkb==0.667:
            self.spatkb=3.5
        elif self.spatkb==1:
            self.spatkb=4
        elif self.spatkb>1:
            self.spatkb=4
    if amount==-0.5:
        if 0.249<self.spatkb<=1:
            self.spatkb=round(1/((1/self.spatkb)-amount),3)
        if 1<self.spatkb<=4:
            self.spatkb=self.spatkb+amount
        
    if amount==-1:
        if self.spatkb>1:
            self.spatkb+=amount
        elif self.spatkb==1:
            self.spatkb=0.5
        elif self.spatkb==0.667:
            self.spatkb=0.4
        elif self.spatkb==0.5:
            self.spatkb=0.333
        elif self.spatkb==0.4:
            self.spatkb=0.285
        elif self.spatkb==0.333:
            self.spatkb=0.249
        elif self.spatkb<=0.285:
            self.spatkb=0.249
    if self.spatkb>4:
        self.spatkb=4
def spdefchange(self,other,amount):
    if self.ability in ["Big Pecks","Clear Body","Flower Veil","Full Metal Body","White Smoke","Hyper Cutter","Keen Eye"] and amount<0 and other.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and self!=other:
        print(f" {self.name}'s {self.ability}!")
        amount=0
    if self.ability=="Simple":
        amount*=2
    if self.ability=="Defiant" and self!=other:
        if amount<0:
            print(f" {self.name}'s {self.ability}!")
            atkchange(self,other,1)
    if self.ability=="Competitive" and self!=other:
        if amount<0:
            print(f" {self.name}'s {self.ability}!")
            spatkchange(self,other,1)
    if self.ability=="Contrary":
        amount=-amount
    if amount<4:
        if amount>=1.5:
            print(f" ⏫ {self.name}'s special defense drastically rose!")
        if amount==1:
            print(f" ⏫ {self.name}'s special defense sharply rose!")
        if amount==0.5:
            print(f" 🔼 {self.name}'s special defense rose!")
        if amount==-0.5:
            print(f" 🔽 {self.name}'s special defense fell!")
        if amount<=-1:
            print(f" ⏬ {self.name}'s special defense harshly fell!")
    if amount==0.5:#+1
        if self.spdefb==0.249:
            self.spdefb=0.285
        elif self.spdefb==0.285:
            self.spdefb==0.333
        elif self.spdefb==0.333:
            self.spdefb==0.4
        elif self.spdefb==0.4:
            self.spdefb==0.5
        elif self.spdefb==0.5:
            self.spdefb==0.667
        elif self.spdefb==0.667:
            self.spdefb==1
        elif self.spdefb>=1:
            self.spdefb+=amount      
        elif self.spdefb>4:
            self.spdefb=4  
    elif amount==1:#+2
        if self.spdefb==0.249:
            self.spdefb=0.333
        elif self.spdefb==0.285:
            self.spdefb=0.4
        elif self.spdefb==0.336:
            self.spdefb=0.5
        elif self.spdefb==0.4:
            self.spdefb=0.667
        elif self.spdefb==0.5:
            self.spdefb=1
        elif self.spdefb==0.667:
            self.spdefb=1.5
        elif self.spdefb>=1:
            self.spdefb+=(amount*1)     
        elif self.spdefb>3:
            self.spdefb=4        
    elif amount==1.5:#+3
        if self.spdefb==0.249:
            self.spdefb=0.4
        elif self.spdefb==0.285:
            self.spdefb=0.5
        elif self.spdefb==0.333:
            self.spdefb=0.667
        elif self.spdefb==0.4:
            self.spdefb=1
        elif self.spdefb==0.5:
            self.spdefb=1.5
        elif self.spdefb==0.667:
            self.spdefb=2
        elif self.spdefb==1:
            self.spdefb=2.5
        elif self.spdefb==1.5:
            self.spdefb=3
        elif self.spdefb==2:
            self.spdefb=3.5
        elif self.spdefb==2.5:
            self.spdefb=4
        elif self.spdefb>2.5:
            self.spdefb=4
    elif amount==2:#+4    
        if self.spdefb==0.249:
            self.spdefb=0.5   
        elif self.spdefb==0.285:
            self.spdefb=0.667
        elif self.spdefb==0.333:
            self.spdefb=1
        elif self.spdefb==0.4:
            self.spdefb=1.5
        elif self.spdefb==0.5:
            self.spdefb=2
        elif self.spdefb==0.667:
            self.spdefb=2.5
        elif self.spdefb==1:
            self.spdefb=3
        elif self.spdefb==1.5:
            self.spdefb=3.5
        elif self.spdefb==2:
            self.spdefb=4
    elif amount==4:#+6
        if self.spdefb==0.249:
            self.spdefb=1  
        elif self.spdefb==0.285:
            self.spdefb=1.5
        elif self.spdefb==0.333:
            self.spdefb=2
        elif self.spdefb==0.4:
            self.spdefb=2.5
        elif self.spdefb==0.5:
            self.spdefb=3
        elif self.spdefb==0.667:
            self.spdefb=3.5
        elif self.spdefb==1:
            self.spdefb=4
        elif self.spdefb>1:
            self.spdefb=4
    if amount==-0.5:
        if 0.249<self.spdefb<=1:
            self.spdefb=round(1/((1/self.spdefb)-amount),3)
        if 1<self.spdefb<=4:
            self.spdefb=self.spdefb+amount
        
    if amount==-1:
        if self.spdefb>1:
            self.spdefb+=amount
        elif self.spdefb==1:
            self.spdefb=0.5
        elif self.spdefb==0.667:
            self.spdefb=0.4
        elif self.spdefb==0.5:
            self.spdefb=0.333
        elif self.spdefb==0.4:
            self.spdefb=0.285
        elif self.spdefb==0.333:
            self.spdefb=0.249
        elif self.spdefb<=0.285:
            self.spdefb=0.249
    if self.spdefb>4:
        self.spdefb=4
def speedchange(self,other,amount):
    if self.ability in ["Big Pecks","Clear Body","Flower Veil","Full Metal Body","White Smoke","Hyper Cutter","Keen Eye"] and amount<0 and other.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and self!=other:
        print(f" {self.name}'s {self.ability}!")
        amount=0
    if self.ability=="Simple":
        amount*=2
    if self.ability=="Defiant" and self!=other:
        if amount<0:
            print(f" {self.name}'s {self.ability}!")
            atkchange(self,other,1)
    if self.ability=="Competitive" and self!=other:
        if amount<0:
            print(f" {self.name}'s {self.ability}!")
            spatkchange(self,other,1)
    if self.ability=="Contrary":
        amount=-amount
    if amount<4:
        if amount>=1.5:
            print(f" ⏫ {self.name}'s speed drastically rose!")
        if amount==1:
            print(f" ⏫ {self.name}'s speed sharply rose!")
        if amount==0.5:
            print(f" 🔼 {self.name}'s speed rose!")
        if amount==-0.5:
            print(f" 🔽 {self.name}'s speed fell!")
        if amount<=-1:
            print(f" ⏬ {self.name}'s speed harshly fell!")
    if amount==0.5:#+1
        if self.speedb==0.249:
            self.speedb=0.285
        elif self.speedb==0.285:
            self.speedb==0.333
        elif self.speedb==0.333:
            self.speedb==0.4
        elif self.speedb==0.4:
            self.speedb==0.5
        elif self.speedb==0.5:
            self.speedb==0.667
        elif self.speedb==0.667:
            self.speedb==1
        elif self.speedb>=1:
            self.speedb+=amount      
        elif self.speedb>4:
            self.speedb=4  
    elif amount==1:#+2
        if self.speedb==0.249:
            self.speedb=0.333
        elif self.speedb==0.285:
            self.speedb=0.4
        elif self.speedb==0.336:
            self.speedb=0.5
        elif self.speedb==0.4:
            self.speedb=0.667
        elif self.speedb==0.5:
            self.speedb=1
        elif self.speedb==0.667:
            self.speedb=1.5
        elif self.speedb>=1:
            self.speedb+=(amount*1)     
        elif self.speedb>3:
            self.speedb=4        
    elif amount==1.5:#+3
        if self.speedb==0.249:
            self.speedb=0.4
        elif self.speedb==0.285:
            self.speedb=0.5
        elif self.speedb==0.333:
            self.speedb=0.667
        elif self.speedb==0.4:
            self.speedb=1
        elif self.speedb==0.5:
            self.speedb=1.5
        elif self.speedb==0.667:
            self.speedb=2
        elif self.speedb==1:
            self.speedb=2.5
        elif self.speedb==1.5:
            self.speedb=3
        elif self.speedb==2:
            self.speedb=3.5
        elif self.speedb==2.5:
            self.speedb=4
        elif self.speedb>2.5:
            self.speedb=4
    elif amount==2:#+4    
        if self.speedb==0.249:
            self.speedb=0.5   
        elif self.speedb==0.285:
            self.speedb=0.667
        elif self.speedb==0.333:
            self.speedb=1
        elif self.speedb==0.4:
            self.speedb=1.5
        elif self.speedb==0.5:
            self.speedb=2
        elif self.speedb==0.667:
            self.speedb=2.5
        elif self.speedb==1:
            self.speedb=3
        elif self.speedb==1.5:
            self.speedb=3.5
        elif self.speedb==2:
            self.speedb=4
    elif amount==4:#+6
        if self.speedb==0.249:
            self.speedb=1  
        elif self.speedb==0.285:
            self.speedb=1.5
        elif self.speedb==0.333:
            self.speedb=2
        elif self.speedb==0.4:
            self.speedb=2.5
        elif self.speedb==0.5:
            self.speedb=3
        elif self.speedb==0.667:
            self.speedb=3.5
        elif self.speedb==1:
            self.speedb=4
        elif self.speedb>1:
            self.speedb=4
    if amount==-0.5:
        if 0.249<self.speedb<=1:
            self.speedb=round(1/((1/self.speedb)-amount),3)
        if 1<self.speedb<=4:
            self.speedb=self.speedb+amount
        
    if amount==-1:
        if self.speedb>1:
            self.speedb+=amount
        elif self.speedb==1:
            self.speedb=0.5
        elif self.speedb==0.667:
            self.speedb=0.4
        elif self.speedb==0.5:
            self.speedb=0.333
        elif self.speedb==0.4:
            self.speedb=0.285
        elif self.speedb==0.333:
            self.speedb=0.249
        elif self.speedb<=0.285:
            self.speedb=0.249
    if self.speedb>4:
        self.speedb=4
