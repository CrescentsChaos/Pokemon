from trainerlist import *
from moves import *
from AItest import *

statusmove=["Sleep Powder","Iron Defense","Calm Mind","Swords Dance","Bulk Up","Recover","Roost","Thunder Wave","Lunar Blessing","Take Heart","Heart Swap","Will-O-Wisp","Moonlight","Synthesis","Morning Sun","Rain Dance","Sunny Day","Hail","Sandstorm","Dark Void","Trick Room","Nasty Plot","Shell Smash","Dragon Dance","Belly Drum","Spore","Hypnosis","Rest","Coil","Curse","Strength Sap","Leech Seed","Protect","Spiky Shield","King's Shield","Heal Order","Defend Order"]
buffmove=["Iron Defense","Calm Mind","Swords Dance","Shell Smash","Bulk Up","Recover","Roost","Moonlight","Morning Sun","Synthesis","Hail","Rain Dance","Sunny Day","Sandstorm","Trickroom","Dragon Dance","Belly Drum","Nasty Plot","Rest","Coil","Curse","Explosion","Heal Order","Defend Order", "Protect","Spiky Shield","King's Shield"]
contactmoves=["Fire Punch","Ice Punch","Thunder Punch","Horn Drill","Body Slam","Double-Edge","Drill Peck","Submission","Seismic Toss","Strength","Petal Dance","Waterfall","Skull Bash","High Jump Kick","Dizzy Punch","Leech Life","Crabhammer","Slash","Triple Kick","Mach Punch","Outrage","Steel Wing","Return","Dynamic Punch","Megahorn","Rapid Spin","Iron Tail","Cross Chop","Crunch","Extreme Speed","Fake Out","Facade","Superpower","Brick Break","Knock Off","Arm Thrust","Blaze Kick","Needle Arm","Poison Fang","Crush Claw","Meteor Mash","Shadow Punch","Sky Uppercut","Dragon Claw","Poison Tail","Volt Tackle","Leaf Blade","Hammer Arm","Gyro Ball","U-Turn","Close Combat","Assurance","Last Resort","Sucker Punch","Flare Blitz","Force Palm","Poison Jab","Night Slash","Aqua Tail","X-Scissor","Dragon Rush","Drain Punch","Brave Bird","Giga Impact","Bullet Punch","Avalanche","Shadow Claw","Thunder Fang","Ice Fang","Fire Fang","Psychic Fangs","Shadow Sneak","Zen Headbutt","Power Whip","Cross Poison","Iron Head","Grass Knot","Wood Hammer","Aqua Jet","Head Smash","Crash Grip","Shadow Force","Heavy Slam","Foul Play","Acrobatics","Dragon Tail","Wild Charge","Drill Run","Dual Chop","Horn Leech","Sacred Sword","Razor Shell","Heat Crash","Head Charge","Gear Grind","Bolt Strike","V-create","Flying Press","Fell Stinger","Phantom Force","Draining Kiss","Play Rough","Nuzzle","Power-Up Punch","Dragon Ascent","First Impression","Darkest Lariat","Ice Hammer","High Horsepower","Solar Blade","Throat Chop","Anchor Shot","Lunge","Fire Lash","Smart Strike","Trop Kick","Dragon Hanmer","Stomping Tantrum","Accelerock","Liquidation","Spectral Thief","Sunsteel Strike","Zing Zap","Multi-Attack","Plasma Fists","Jaw Lock","Bolt Beak","Double Iron Bash","Fishious Rend","Body Press","Behemoth Blade","Behemoth Bash","Breaking Swipe","Spirit Break","False Surrender","Grassy Glide","Skitter Smack","Flip Turn","Triple Axel","Dual Wingbeat","Wicked Blow","Surging Strikes","Thunderous Kick"]
priorityatkmoves=["Mach Punch","Bullet Punch","Sucker Punch","Fake Out","Extreme Speed","Aqua Jet","Shadow Sneak","Accelerock","Ice Shard","Water Shuriken"]
def fchoice(pk,tr):
    movelist(pk)
    choice=input(f"{tr.name}: Choose a move.\n>>")
    if choice in ["1","2","3","4","5","6"]:
        choice=int(choice)
    if pk.item is not None and  "Choice" in pk.item and pk.choiced==False:
        pk.choiced=True
        pk.choicemove=int(choice)
    if pk.choiced==True:
        choice=pk.choicedmove
    if len(pk.moves)==1:
        choice=1
    else:
        choice=random.randint(1,len(pk.moves))
    return choice

def switch(current,other,trainer,trainer2,field):
    showmon(trainer)
    current.atkb=1
    current.defb=1
    current.spatkb=1
    current.spdefb=1
    current.speedb=1
    current.atk=current.maxatk
    current.speed=current.maxspeed
    current.spatk=current.maxspatk
    current.spdef=current.maxspdef
    current.defense=current.maxdef
    current.badpoison=1
    current.recharge=False
    current.seeded=False
    current.flinched=False
    current.protect=False
    other.protect=False
    current.shelltrap=False
    current.canfakeout=True
    current.choiced=False
    current.choicedmove=None
    m=None
    switchable=[1,2,3,4,5,6]
    if current in trainer.pokemons:
        m=trainer.pokemons.index(current)
        swe=[0,1,2,3,4,5]
        swe.remove(m)
    n=(input(f"{trainer.name} Choose a Pokemon: "))
    if n=="info":
        n=(input("Which pokemon you wanna see?"))
        if n in ["1","2","3","4","5","6"]:
            n=int(n)
            trainer.pokemons[n-1].info()
            movelist(trainer.pokemons[n-1])
            return switch(current,other,trainer,trainer2,field)
        else:
            return switch(current,other,trainer,trainer2,field)
    if n not in ["1","2","3","4","5","6"] and len(trainer.pokemons)>0:
        n=random.randint(1,len(trainer.pokemons))
    if n not in switchable and len(trainer.pokemons)>0 and trainer.ai==True:
        while n!=m:
            n=random.randint(1,len(trainer.pokemons))
    if n in ["1","2","3","4","5","6"]:
        n=int(n)
    
    if trainer.ai==True:
        #print("Not Working")
        new=switchAI(current,other,trainer,trainer2,field) 
    if trainer.ai==False:  
        #print("Working")
        new=trainer.pokemons[n-1]   
    if new==current:
   	    print(f"\n{current.name} is already in battle.")
   	    return switch(current,other,trainer,trainer2,field)		
    if new!=current:
        withdaweff(current,trainer,other)
        if "Red" in trainer.name:
            print(f"{trainer.name}: ........")
            current=new
            entryeff(current,other,trainer,trainer2,field)
            return current
        else:
            phase1=random.choice([" return! You did well buddy."," return! You disappointed me."," return! Pathetic Pokémon."," return! Take rest my friend."," return! You were strong as always."])
            print(f"\n{trainer.name}: "+current.name+phase1)
            current=new
            phase2=random.choice(["It's our show time.","Show your strength.","Let's do it buddy.","I believe in you!","Let's finish this off.","Are you ready buddy?","Let's show them what you are capable of."])
            print(f"Go {current.name}! "+phase2)
          
            entryeff(current,other,trainer,trainer2,field)
            return current
    else:
        return current

#WITHDRAW EFFECTS
def withdaweff(current,trainer,other):
    if current.ability=="Natural Cure" and current.status!="Alive":
        print(f"{current.name}'s {current.ability}.")
        current.status="Alive"
    if current.ability=="Illusion":
        current.name=random.choice(["Raikou","Entei","Suicune","Primape","Machamp","Nihilego","Gengar","Toxicroak"])
    if current.ability=="Regenerator" and 0<current.hp<current.maxhp:
        print(f"{current.name}'s {current.ability}.")
        if current.hp<=(current.maxhp/3):
            current.hp+=round(current.maxhp/3)
        elif current.hp>(current.maxhp/3):
            current.hp=current.maxhp
#ENTRY EFFECTS            
def entryeff(current,other,trainer,trainer2,field):
    if current.ability == "Sand Stream" and field.weather not in ["Sandstorm","Primordial Sea","Desolate Land"]:
        print(f"{current.name}'s {current.ability} whipped up a sandstorm!")
        field.weather="Sandstorm" 
    if current.ability=="Primordial Sea" and field.weather!="Primordial Sea" and field.weather!="Primordial Sea":
        print(f"{current.name}'s {current.ability}. A heavy rain began to fall!")
        field.weather="Primordial Sea"
    if current.ability=="Desolate Land" and field.weather!="Desolate Land":
        print(f"{current.name}'s {current.ability}. The sunlight turned extremely harsh!")
        field.weather="Desolate Land"
    if current.ability == "Drought" and field.weather not in ["Sunny","Primordial Sea","Desolate Land"]:
        print(f"{current.name}'s {current.ability} intensified the sun's rays!")
        field.weather="Sunny"
    if current.ability == "Drizzle" and field.weather not in ["Rainy","Primordial Sea","Desolate Land"]:
        print(f"{current.name}'s {current.ability} made it rain!")
        field.weather="Rainy"
    if current.ability == "Snow Warning" and field.weather not in ["Hail","Primordial Sea","Desolate Land"]:
        print(f"{current.name}'s {current.ability} whipped up a hailstorm!")
        field.weather="Hail"      
    if current.ability=="Download":
        print(f"{current.name}'s {current.ability}.")
        if other.spdef<other.defense:
            spatkchange(current,0.5)
        if other.defense<=other.spdef:
            atkchange(current,0.5)
    if current.ability=="Intrepid Sword":
        print(f"{current.name}'s {current.ability}")
        atkchange(current,0.5)
        print(f"Attack x{current.atkb}")
    if current.ability=="Dauntless Shield":
        print(f"{current.name}'s {current.ability}")
        defchange(current,0.5)
        print(f"Defense x{current.defb}")
    if current.ability=="Electric Surge":
        print("An electric current ran across the battlefield!")
        field.terrain="Electric"
    if current.ability=="Misty Surge":
        print("Mist swirled around the battlefield!")
        field.terrain="Misty"
    if current.ability=="Grassy Surge":
        print("Grass grew to cover the battlefield!")
        field.terrain="Grassy"
    if current.ability=="Psychic Surge":
        print("The battlefield got weird!")
        field.terrain="Psychic"                
    if "Toxic Spikes" in trainer.hazard:
        if current.type1 in ["Poison"] or current.type2 in ["Poison"]:
            trainer.hazard.remove("Toxic Spikes")
            print(f"{current.name} absorbed the Toxic Spikes!")
        if current.type1 not in ["Poison","Steel"] and current.type2 not in ["Poison","Steel"] and current.ability not in ["Magic Guard","Levitate"] and current.item!="Heavy-Duty Boots":
            current.status="Badly Poisoned"
            print(f"{current.name} was poisoned by Toxic Spikes.")
    if "Stealth Rock" in trainer.hazard and current.ability not in ["Magic Guard","Levitate"] and current.item!="Heavy-Duty Boots":
        buff=2
        #print(current.type1,current.type2)
        if current.type1 in ["Flying", "Bug", "Fire", "Ice"]:
            buff*=2
        if current.type2 in ["Flying", "Bug", "Fire", "Ice"]:
            buff*=2
        if current.type1 in ['Fighting', 'Ground', 'Steel']:
            buff=1
        if current.type2 in ['Fighting', 'Ground', 'Steel']:
            buff=1
        #print(buff)
        current.hp-=(current.hp*0.0625*buff)
        print(f"Pointed stones dug into {current.name}!")
#INTIMIDATE        
    if current.ability=="Intimidate" and other.ability not in ["Inner Focus","Oblivious","Clear Body"]:
        atkchange(other,-0.5)
        print(f"{current.name}'s {current.ability}!")
        print(f"{other.name}'s attack was lowered.") 
#Stance Change        
def stancechange(self,used):    
    if used not in statusmove and self.ability=="Stance Change" and self.sword!=True:
        self.shield=False
        self.sword=True
        print(f"{self.name}'s {self.ability}!")
        print("Aegislash changed its stance.")
        self.name="Sword Aegislash"        
        self.atk,self.spatk,self.defense,self.spdef=self.defense,self.spdef,self.atk,self.spatk
        self.maxatk,self.maxspatk,self.maxdef,self.maxspdef=self.maxdef,self.maxspdef,self.maxatk,self.maxspatk
    if used in statusmove and self.ability=="Stance Change" and self.shield!=True:
        self.shield=True
        self.sword=False
        print(f"{self.name}'s {self.ability}!")
        print("Aegislash changed its stance.")
        self.name="Shield Aegislash"        
        self.atk,self.spatk,self.defense,self.spdef=self.defense,self.spdef,self.atk,self.spatk
        self.maxatk,self.maxspatk,self.maxdef,self.maxspdef=self.maxdef,self.maxspdef,self.maxatk,self.maxspatk
#ATTACK
def attack(self,other,tr,optr,use,opuse,field,turn):
    print(f"\n{tr.name}:")
    used=use
    hit=1
    me=self
    canatk=True
    multiscale=False
    stancechange(self,used)
    if field.terrain=="Psychic":
        if used in priorityatkmoves:
            used=None
            print("Cannot use priority moves in psychic terrain!")
    if self.ability=="Limber" and self.status=="Paralyzed":
        print(f"{self.ability} cured {self.name}'s paralysis!")
        self.status="Alive"
    if other.ability=="Stench" and self.ability!="Long Reach":
        ch=random.randint(1,100)  
        if ch>90:
            print(f"{other.name}'s {other.ability}!")
            self.flinched=True   
    if self.item=="King's Rock":
        ch=random.randint(1,100)
        if ch>90 and other.ability not in ["Inner Focus"]:
            other.flinched=True
    if self.item=="Lum Berry" and self.status!="Alive":
        print(f"{self.item} cured {self.name}'s status condition!")
        self.item=None
    
    if field.terrain=="Electric":
        if self.ability not in ["Levitate"] and self.type1!="Flying" and self.type2!="Flying" and self.status=="Sleep":
            self.status="Alive"
    if field.terrain=="Misty":
        if self.ability not in ["Levitate"] and self.type1!="Flying" and self.type2!="Flying":
            self.status="Alive"
    if self.ability=="Trace":
            print(f"{self.name}'s {self.ability}!")        
            self.ability=other.ability
            entryeff(self,other,tr,optr,field)
    if self.ability=="Speed Boost":
            print(f"{self.name}'s {self.ability}!")
            print(f"{self.name}'s speed rose.")
            speedchange(self,0.5)
    if self.status=="Paralyzed":
        ch=random.randint(1,3)
        if ch==3:
            canatk=False
            used=None
            print(f"{self.name} is paralyzed and unable to move.")
        else:
            canatk=True
    if self.status=="Sleep":
        ch=random.randint(1,3)
        if ch==3:
            print(f"{self.name} woke up!")
            self.status="Alive"
        else:
            print(f"{self.name} is fast asleep!")
            used=None
    if self.status=="Frozen":
        ch=random.randint(1,5)
        if ch==3:
            print(f"{self.name} thawed out.")
            self.status="Alive"
        else:
            print(f"{self.name} is frozen solid.")
            used=None
    before=other.hp
    sbefore=self.hp
    if self.ability=="Truant":
        if self.truant==True:
            print(f"{self.name} is loafing around!")
            used=None
            self.truant=False
        else:
            self.truant=True
    if other.ability=="Multiscale" and other.hp==other.maxhp:
        print(f"{other.name}'s {other.ability}.")
        self.atk=self.maxatk/2
        self.spatk=self.maxspatk/2
        multiscale=True
    if used in self.moves:
        if self.item=="Assault Vest" and used in statusmove:
            while True:
                print(f"Cannot used status moves while holding an Assault Vest.")
                new=fchoice(self,tr)
                used=self.moves[new-1]
                if used not in statusmove:
                    break
        if used not in ["Protect","Spiky Shield","King's Shield","Baneful Bunker"]:
            self.protect=False
        elif used=="Lunar Blessing":
            lunarblessing(self)
            if self.status!="Alive":
                self.status="Alive"
                print(f"{self.name}'s status was cured.")
        elif used=="Take Heart":
            takeheart(self)
            if self.status!="Alive":
                self.status="Alive"
                print(f"{self.name}''s status was cured.")
        if self.precharge==True and "Geomancy" in self.moves:
            print(f"{self.name} used Geomancy!")
            spatkchange(self,1)     
            spdefchange(self,1)   
            speedchange(self,1)
            print(f"Special Attack x{self.spatkb}")   
            print(f"Special Defense x{self.spdefb}")   
            print(f"Speed x{self.speedb}")      
            self.precharge=False
        if self.recharge==True:
            print(f"{self.name} is recharging.")
            self.recharge=False
            used=None
        if self.flinched==True:
            print(f"{self.name} flinched.")
            self.flinched=False
            used=None
        elif self.protect=="Pending" and used in ["Protect","Spiky Shield","King's Shield","Baneful Bunker"]:
            print(f"{self.name} used {used}!")
            print("It failed.")
            self.protect=False
            used=None
        elif other.protect==True and used not in buffmove and self.ability not in ["Infiltrator","Unseen Fist"] and used not in ["Shadow Force","Phantom Force","Hyperspace Fury"]:
            print(f"{other.name} protected itself from {self.name}'s {used}.")
            other.protect="Pending"
            if used in ["Protect","Spiky Shield","King's Shield","Baneful Bunker"]:
                print(f"{self.name} used {used}!")
                print("It failed!")
                used=None
            
            if "Spiky Shield" in other.moves and used in contactmoves:
                self.hp-=round(self.maxhp/8)
            if "King's Shield" in other.moves and used in contactmoves:
                atkchange(self,-0.5)
                print(f"Attack x{self.atkb}")
            if "Baneful Bunker" in other.moves and used in contactmoves:
                if self.status=="Alive":
                    self.status=["Badly Poisoned"]    
        elif used=="Toxic":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack({used}).")
            else:
                toxic(self,other)
        elif used=="Thunder Wave":
            thunderwave(self,other)
        elif used=="Sucker Punch":
            if opuse in statusmove or opuse is None:
                print("It failed.")
            else:
                suckerpunch(self,other)
        elif used=="Will-O-Wisp":
            miss=random.randint(1,100)
            if miss>85:
                print(f"{other.name} avoided the attack({used}).")
            else:
                willowisp(self,other)        
        elif used=="Overdrive":
            overdrive(self,other)        
        elif used=="Psystrike":
            psystrike(self,other)
        elif used=="Shadow Punch":
            shadowpunch (self,other)
        elif used=="Smart Strike":
            smartstrike(self,other)
        elif used=="Magnitude":
            magnitude(self,other)
        elif used=="Attack Order":
            attackorder(self,other)
        elif used=="Bulldoze":
            bulldoze(self,other)
        elif used=="Fishious Rend":
            fishiousrend(self,other)
        elif used=="Grav Apple":
            gravapple(self,other)
        elif used=="Mind Blown":
            mindblown(self,other)
        elif used=="Shell Side Arm":
            shellsidearm(self,other)
        elif used=="Apple Acid":
            appleacid(self,other)
        elif used=="Grassy Glide":
            grassyglide(self,other)
        elif used=="Snipe Shot":
            snipeshot(self,other)
        elif used=="Drum Beating":
            drumbeating(self,other)
        elif used=="Doom Desire":
            doomdesire(self,other)
        elif used=="Shadow Sneak":
            shadowsneak(self,other)
        elif used=="Geomancy":
            geomancy(self,other)
        elif used=="Heavy Slam":
            heavyslam(self,other)
        elif used=="Heart Swap":
            heartswap(self,other)
        elif used=="Dragon Energy":
            dragonenergy(self,other)
        elif used=="Court Change":
            print(f"{self.name} used Court Change!")
            tr.hazard,optr.hazard=optrhazard,trhazard
        elif used=="Land's Wrath":
            landswrath(self,other)
        elif used=="Thousand Arrows":
            thousandarrows(self,other)
        elif used=="Thousand Waves":
            thousandwaves(self,other)
        elif used=="Steel Beam":
            steelbeam(self,other)
        elif used=="Shadow Claw":
            shadowclaw(self,other)
        elif used=="Shelter":
            shelter(self)
        elif used=="Crush Grip":
            crushgrip(self,other)
        elif used=="Night Daze":
            nightdaze(self,other)
        elif used=="Crabhammer":
            crabhammer(self,other)
        elif used=="Mystical Fire":
            mysticalfire(self,other)
        elif used=="Bitter Malice":
            bittermalice(self,other)
        elif used=="Rain Dance":
            raindance(self,field,turn)
            if other.ability=="Dancer":
                print(f"{other.name}'s {other.ability}!")
                raindance(other,field,turn)
        elif used=="Sunny Day":
            sunnyday(self,field,turn)
        elif used=="Leech Seed":
            leechseed(self,other)
        elif used=="Trick Room":
            trickroomm(self)
        elif used=="Sandstorm":
            sandstorm(self,field,turn)
        elif used=="Shore Up":
            shoreup(self)
        elif used=="Electric Terrain":
            electricterrain(self)
        elif used=="Misty Terrain":
            mistyterrain(self)
        elif used=="Grassy Terrain":
            grassyterrain(self)
        elif used=="Psychic Terrain":
            psychicterrain(self)
        elif used=="Synthesis":
            synthesis(self)
        elif used=="Hail":
            hail(self,field,turn)
        elif used=="Quiver Dance":
            quiverdance(self)
            if other.ability=="Dancer":
                print(f"{other.name}'s {other.ability}!")
                quiverdance(other)
        elif used=="Defend Order":
            defendorder(self)
        elif used=="Swords Dance":
            swordsdance(self)
            if other.ability=="Dancer":
                print(f"{other.name}'s {other.ability}!")
                swordsdance(other)
        elif used=="Nasty Plot":
            nastyplot(self)
        elif used=="Shell Smash":
            shellsmash(self)
        elif used=="Dragon Dance":
            dragondance(self)
            if other.ability=="Dancer":
                print(f"{other.name}'s {other.ability}!")
                dragondance(other)
        elif used=="Iron Defense":
            irondefense(self)
        elif used=="Bullet Punch":
            bulletpunch(self,other)
        elif used=="X-Scissor":
            xscissor(self,other)
        elif used=="Drill Peck":
            drillpeck(self,other)
        elif used=="Triple Arrows)":
            for i in range(3):
                triplearrows(self,other)
        elif used=="Boomburst":
            boomburst(self,other)
        elif used=="Hyperspace Fury":
            hyperspacefury(self,other)
        elif used=="Knock Off":
            knockoff(self,other)
        elif used=="Volt Tackle":
            volttackle(self,other)
        elif used=="Chloroblast":
            chloroblast(self,other)
        elif used=="Beak Blast":
            beakblast(self,other)
        elif used=="Facade":
            facade(self,other)
        elif used=="Soak":
            soak(self,other)
        elif used=="Defog":
            print(f"{self.name} used defog.")
            print("All the hazards blew away!")
            tr.hazard=[]
            optr.hazard=[]
        elif used=="Trick-or-Treat":
            trickortreat(self,other)
        elif used=="Forest's Curse":
            forestscurse(self,other)
        elif used=="Moongeist Beam":
            moongeistbeam(self,other)
        elif used=="Sunsteel Strike":
            sunsteelstrike(self,other)
        elif used=="Stored Power":
            storedpower(self,other)
        elif used=="Luster Purge":
            lusterpurge(self,other)
        elif used=="Hammer Arm":
            hammerarm(self,other)
        elif used=="Final Gambit":
            finalgambit(self,other)
        elif used=="Bolt Beak":
            boltbeak(self,other)
        elif used=="Oblivion Wing":
            oblivionwing(self,other)
        elif used=="Aura Sphere":
           aurasphere(self,other)
        elif used=="Aura Wheel":
           aurawheel(self,other)
        elif used=="Meteor Mash":
           meteormash(self,other)
        elif used=="Venoshock":
             venoshock(self,other)
        elif used=="Infernal Parade":
             infernalparade(self,other)
        elif used=="Raging Fury":
             ragingfury(self,other)
        elif used=="Heat Crash":
             heatcrash(self,other)
        elif used=="Spirit Shackle":
             spiritshackle(self,other)
        elif used=="Throat Chop":
             throatchop(self,other)
        elif used=="Steam Eruption":
            steameruption(self,other)
        elif used=="Diamond Storm":
            diamondstorm(self,other)
        elif used=="Light of Ruin":
            lightofruin(self,other)
        elif used=="Hyper Voice":
             hypervoice(self,other)
        elif used=="Sparkling Aria":
             sparklingaria(self,other)
        elif used=="Darkest Lariat":
             darkestlariat(self,other)
        elif used=="Ceaseless Edge":
             ceaseless(self,other)
        elif used=="Mist Ball":
            mistball(self,other)
        elif used=="Thunder Fang":
            tfang(self,other)
        elif used=="Stomping Tantrum":
            stompingtantrum(self,other)
        elif used=="Razor Shell":
            razorshell(self,other)
        elif used=="Headlong Rush":
            headlongrush(self,other)
        elif used=="Seed Bomb":
            seedbomb(self,other)
        elif used=="Fire Fang":
            firefang(self,other)
        elif used=="Fire Lash":
            firelash(self,other)
        elif used=="Armor Cannon":
            armorcannon(self,other)
        elif used=="Bitter Blade":
            bitterblade(self,other)
        elif used=="Milk Drink":
            milkdrink(self)
        elif used=="Fiery Dance":
            fierydance(self,other)
            if other.ability=="Dancer":
                print(f"{other.name}'s {other.ability}!")
                fierydance(other)
        elif used=="Leech Life":
            leechlife(self,other)
        elif used=="Horn Leech":
            hornleech(self,other)
        elif used=="Flip Turn":
            flipturn(self,other)
            if len(tr.pokemons)>1 and (other.hp!=before):
                print(f"{self.name} returned to it's pokéball.")
                self=switch(self,other,tr,optr,field)
        elif used=="U-Turn":
            uturn(self,other)
            if len(tr.pokemons)>1:
                print(f"{self.name} returned to it's pokéball.")
                self=switch(self,other,tr,optr,field)
        elif used=="Parting Shot":
            partingshot(self,other)
            if len(tr.pokemons)>1:
                print(f"{self.name} returned to it's pokéball.")
                self=switch(self,other,tr,optr,field)                
        elif used=="Volt Switch":
            voltswitch(self,other)
            if len(tr.pokemons)>1 and (other.hp!=before):
                print(f"{self.name} returned to it's pokéball.")
                self=switch(self,other,tr,optr,field)
        elif used=="Extreme Speed":
            extemespeed(self,other)
        elif used=="Inferno":
            miss=random.randint(1,100)
            if miss>50:
                print(f"{other.name} avoided the attack({used}).")
            else:
                inferno(self,other)
        elif used=="Overheat":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack({used}).")
            else:
                overheat(self,other)
        elif used=="Whirlwind":
            print(f"{self.name} usedd Whirlwind.")
            print(f"{other.name} blew away with the wind.")
            speedchange(other,-0.5)
            print(f"{other.name}: Speed x"+str(other.speedb))   
        elif used=="Return":
            retrn(self,other)
        elif used=="Sleep Powder":
            miss=random.randint(1,100)
            if miss>75:
                print(f"{other.name} avoided the attack({used}).")
            else:
                sleeppowder(self,other)
        elif used=="Spore":
            spore(self,other)
        elif used=="Hypnosis":
            miss=random.randint(1,100)
            if miss>60:
                print(f"{other.name} avoided the attack({used}).")
            else:
                hypnosis(self,other)
        elif used=="Dark Void":
            miss=random.randint(1,100)
            if miss>80:
                print(f"{other.name} avoided the attack({used}).")
            else:
                darkvoid(self,other)
        elif used=="Body Press":
            bodypress(self,other)
        elif used=="Blizzard":
            if field.weather == "Hail" and field.weather =="Hail":
                blizzard(self,other)
            if field.weather != "Hail" and field.weather !="Hail":
                miss=random.randint(1,100)
                if miss>70:
                    print(f"{other.name} avoided the attack({used}).")
                elif miss<=70:
                    blizzard(self,other)
        elif used=="Air Slash":
            miss=random.randint(1,100)
            if miss>95:
                print(f"{other.name} avoided the attack({used}).")
            else:
                airslash(self,other)
        elif used=="Bone Rush":
            bonerush(self,other)
        elif used=="Gyro Ball":
            gyroball(self,other)
        elif used=="Electro Ball":
            electroball(self,other)
        elif used=="Electroweb":
            electroweb(self,other)
        elif used=="Blast Burn":
            blastburn(self,other)
            self.recharge=True
        elif used=="Frenzy Plant":
            frenzyplant(self,other)
            self.recharge=True
        elif used=="Hydro Cannon":
            hydrocannon(self,other)
            self.recharge=True
        elif used=="Zap Cannon":
            miss=random.randint(1,100)
            if miss>50:
                print(f"{other.name} avoided the attack({used}).")
            else:
                zapcannon(self,other)
        elif used=="Freeze-Dry":
            freezedry(self,other)
        elif used=="Ice Fang":
            icefang(self,other)
        elif used=="Coil":
            coil(self)
        elif used=="Dual Wingbeat":
            dualwingbeat(self,other)
        elif used=="Acrobatics":
            acrobatics(self,other)
        elif used=="Curse":
            curse(self)
        elif used=="Dragon Ascent":
            dragonascent(self,other)
        elif used=="Foul Play":
            foulplay(self,other)
        elif used=="High Horsepower":
            highhorsepower(self,other)
        elif used=="Water Shuriken":
            hit=random.randint(2,5)
            if self.ability=="Skill Link":
                print(f"{self.name}'s {self.ability}.")
                hit=5
            for i in range(hit):
                watershuriken(self,other)
            print(f"It hit {hit} time(s).")            
        elif used=="Bullet Seed":
            hit=random.randint(3,5)
            if self.ability=="Skill Link":
                print(f"{self.name}'s {self.ability}.")
                hit=5
            for i in range(hit):
                bulletseed(self,other)
            print(f"It hit {hit} time(s).")
        elif used=="Signal Beam":
            signalbeam(self,other)
        elif used=="Grass Knot":
            grassknot(self,other)
        elif used=="Extrasensory":
            extrasensory(self,other)
        elif used=="Wild Charge":
            wildcharge(self,other)
        elif used=="Multi-Attack":
            multiattack(self,other)
        elif used=="Wave Crash":
            wavecrash(self,other)
        elif used=="Power Gem":
            powergem(self,other)
        elif used=="High Jump Kick":
            hijumpkick(self,other)
        elif used=="Plasma Fists":
            plasmafists(self,other)
        elif used=="Blaze Kick":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack({used}).")
            else:
                blazekick(self,other)
        elif used=="Crush Claw":
            crushclaw(self,other)
        elif used=="Lava Plume":
            lavaplume(self,other)
        elif used=="Hurricane":
            if field.weather == "Rainy" and field.weather =="Rainy":
                hurricane(self,other)
            if field.weather =="Sunny" and field.weather == "Sunny":
                miss=random.randint(1,100)
                if miss>50:
                    print(f"{other.name} avoided the attack({used}).")
                elif miss>=50:
                    hurricane(self,other)
            elif field.weather != "Rainy" and field.weather !="Rainy":
                miss=random.randint(1,100)
                if miss>70:
                    print(f"{other.name} avoided the attack({used}).")
                elif miss>=30:
                    hurricane(self,other)
          
        elif used=="Sky Uppercut":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack({used}).")
            else:
                skyuppercut(self,other)
        elif used=="Precipice Blades":
            miss=random.randint(1,100)
            if miss>85:
                print(f"{other.name} avoided the attack({used}).")
            else:
                precipiceblades(self,other)
        elif used=="Origin Pulse":
            miss=random.randint(1,100)
            if miss>85:
                print(f"{other.name} avoided the attack({used}).")
            else:
                originpulse(self,other)
        elif used=="Draco Meteor":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack({used}).")
            else:
                dracometeor(self,other)
        elif used=="Psycho Boost":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack({used}).")
            else:
                psychoboost(self,other)
        elif used=="Drill Run":
            miss=random.randint(1,100)
            if miss>95:
                print(f"{other.name} avoided the attack({used}).")
            else:
                drillrun(self,other)
        elif used=="Head Smash":
            miss=random.randint(1,100)
            if miss>80:
                print(f"{other.name} avoided the attack({used}).")
            else:
                headsmash(self,other)
        elif used=="Flash Cannon":
            flashcannon(self,other)
        elif used=="Toxic Spikes":
            if "Toxic Spikes" in optr.hazard:
                print("Nothing happened!")
            if "Toxic Spikes" not in optr.hazard:
                print(f"{self.name} used Toxic Spikes.")
                print ("Poison spikes were scattered all around the opposing team!")
                optr.hazard.append("Toxic Spikes")
            else:
                print("Nothing happened!")
        elif used=="Stealth Rock":
            if "Stealth Rock" in optr.hazard:
                print("Nothing happened!")
            if "Stealth Rock" not in optr.hazard:
                print(f"{self.name} used Stealth Rock.")
                print ("Pointed stones float in the air around the opposing team!")
                optr.hazard.append("Stealth Rock")
            
        elif used=="Transform":
            transform(self,other)
        elif used=="Seismic Toss":
            seismictoss(self,other)
        elif used=="Night Shade":
            nightshade(self,other)
        elif used=="Snarl":
            snarl(self,other)
        elif used=="Soft Boiled":
            if self.hp==self.maxhp:
                print("It failed!")
            else:
                softboiled(self)
        elif used=="Heal Order":
            if self.hp==self.maxhp:
                print("It failed!")
            else:
                healorder(self)
        elif used=="Slack Off":
            if self.hp==self.maxhp:
                print("It failed!")
            else:
                slackoff(self)
        elif used=="Roost":
            if self.hp==self.maxhp:
                print("It failed!")
            else:
                roost(self)
        elif used=="Recover":
            if self.hp==self.maxhp:
                print("It failed!")
            else:
                recover(self)
            
        elif used=="Spiky Shield":
            self.protect=True
            print(f"{self.name} used Spiky Shield!")
        elif used=="Protect":
            self.protect=True
            print(f"{self.name} used Protect.")
            
        elif used=="King's Shield":
            self.protect=True
            print(f"{self.name} used King's Shield.")
        elif used=="Morning Sun":
            if self.hp==self.maxhp:
                print("It failed!")
            else:
                morningsun(self)
        elif used=="Moonlight":
            if self.hp==self.maxhp:
                print("It failed!")
            else:
                moonlight(self)
        elif used=="Megahorn":
            miss=random.randint(1,100)
            if miss>85:
                print(f"{other.name} avoided the attack({used}).")
            else:
                megahorn(self,other)
        elif used=="Leaf Storm":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack({used}).")
            else:
                leafstorm(self,other)
        elif used=="Leaf Tornado":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack({used}).")
            else:
                leaftornado(self,other)
        elif used=="Leaf Blade":
            leafblade(self,other)
        elif used=="Razor Leaf":
            razorleaf(self,other)
        elif used=="Victory Dance":
            victorydance(self)
            if other.ability=="Dancer":
                print(f"{other.name}'s {other.ability}!")
                victorydance(other)
        elif used=="Light Screen":
            lightscreen(self,field,turn)
        elif used=="Calm Mind":
            calmmind(self)
        elif used=="Reflect":
            reflect(self,field,turn)
        elif used=="Acid Armor":
            acidarmor(self)
        elif used=="Aeroblast":
            miss=random.randint(1,100)
            if miss>95:
                print(f"{other.name} avoided the attack({used}).")
            else:
                aeroblast(self,other)
        elif used=="Wicked Blow":
            wickedblow(self,other)
        elif used=="Tail Glow":
            tailglow(self)
        elif used=="Psychic Fang":
            psychicfang(self,other)
        elif used=="Poison Fang":
            poisonfang(self,other)
        elif used=="Poison Tail":
            poisontail(self,other)
        elif used=="Force Palm":
            forcepalm(self,other)
        elif used=="Techno Blast":
            technoblast(self,other)
        elif used=="Relic Song":
            relicsong(self,other)
        elif used=="Drain Punch":
            drainpunch(self,other)
        elif used=="Frost Breath":
            frostbreath(self,other)
        elif used=="Icicle Crash":
            iciclecrash(self,other)
        elif used=="Scorching Sands":
            scorchingsands(self,other)
        elif used=="Outrage":
            outrage(self,other)
        elif used=="Strength Sap":
            strengthsap(self,other)
        elif used=="Surging Strikes":
            for i in range(3):
                surgingstrikes(self,other)
        elif used=="Heat Wave":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack({used}).")
            else:
                heatwave(self,other)
        elif used=="Slash":
            slash(self,other)
        elif used=="Night Slash":
            nightslash(self,other)
        elif used=="Psycho Cut":
            psychocut(self,other)
        elif used=="Sacred Fire":
            miss=random.randint(1,100)
            if miss>95:
                print(f"{other.name} avoided the attack({used}).")
            else:
                sacredfire(self,other)
        elif used=="Brick Break":
            brickbreak(self,other,optr)
        elif used=="Giga Impact":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack({used}).")
            else:
                gigaimpact(self,other)
                self.recharge=True
        elif used=="Hyper Beam":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack({used}).")
            else:
                hyperbeam(self,other)
                self.recharge=True
        elif used=="Roar of Time":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack({used}).")
            else:
                roaroftime(self,other)
                self.recharge=True
        elif used=="Spacial Rend":
            miss=random.randint(1,100)
            if miss>95:
                print(f"{other.name} avoided the attack({used}).")
            else:
                spacialrend(self,other)
        elif used=="Phantom Force":
            miss=random.randint(1,100)
            if miss>95:
                print(f"{other.name} avoided the attack({used}).")
            else:
                phantomforce(self,other)                  
        elif used=="Shadow Force":
            miss=random.randint(1,100)
            if miss>95:
                print(f"{other.name} avoided the attack({used}).")
            else:
                shadowforce(self,other)                
        elif used=="Iron Head":
            ironhead(self,other)
        elif used=="Iron Tail":
            miss=random.randint(1,100)
            if miss>75:
                print(f"{other.name} avoided the attack({used}).")
            else:
                irontail (self,other)
        elif used=="Dazzling Gleam":
            dazzlinggleam (self,other)
        elif used=="Magma Storm":
            magmastorm(self,other)
        elif used=="Water Spout":
            waterspout(self,other)
        elif used=="Eruption":
            eruption (self,other)
        elif used=="Dragon Pulse":
            dragonpulse (self,other)
        elif used=="Play Rough":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack({used}).")
            else:
                playrough (self,other)
        elif used=="Power Whip":
            powerwhip(self,other)
        elif used=="Ancient Power":
            apower(self,other)
        elif used=="Strength":
            strength(self,other)
        elif used=="Petal Dance":
            petaldance(self,other)
            if other.ability=="Dancer":
                print(f"{other.name}'s {other.ability}!")
                petaldance(other)
        elif used=="Dizzy Punch":
            dizzypunch (self,other)
        elif used=="Barb Barrage":
            barbbarrage (self,other)
        elif used=="Mach Punch":
            machpunch(self,other)
        elif used=="Thunder":
            if field.weather in ["Rainy","Primordial Sea"] and field.weather in ["Rainy","Primordial Sea"]:
                thunder(self,other)
            else:
                miss=random.randint(1,100)
                if miss>70:
                    print(f"{other.name} avoided the attack({used}).")
                elif miss<=70:
                    thunder(self,other)
        elif used=="Scald":
            scald(self,other)
        elif used=="Egg Bomb":
            eggbomb(self,other)
        elif used=="Hex":
            hex (self,other)
        elif used=="Fake Out":
            if self.canfakeout==False:
                print("It failed!")
            if self.canfakeout==True:
                fakeout(self,other)
                self.canfakeout=False
        elif used=="Power-up Punch":
            poweruppunch(self,other)
        elif used=="Double-Edge":
            doubleedge(self,other)
        elif used=="Esper Wing":
            esperwing(self,other)
        elif used=="Dire Claw":
            direclaw(self,other)
        elif used=="Dragon Claw":
            dragonclaw(self,other)
        elif used=="Psyshield Bash":
            psyshield(self,other)
        elif used=="Surf":
            surf(self,other)
        elif used=="Aqua Tail":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack({used}).")
            else:
                aquatail(self,other)
        elif used=="Sky Attack":
            skyattack(self,other)
            self.recharge=True
        elif used=="Belly Drum":
            bellydrum(self)
        elif used=="Weather Ball":
            weatherball(self,other)
        elif used=="Crunch":
            crunch(self,other)
        elif used=="Aqua Jet":
            aquajet(self,other)
        elif used=="Ice Shard":
            iceshard(self,other)
        elif used=="Bug Buzz":
            bugbuzz(self,other)
        elif used=="Flamethrower":
            flamethrower(self,other)
        elif used=="Flare Blitz":
            flareblitz(self,other)
        elif used=="Thunder Punch":
            tpunch(self,other)
        elif used=="Fire Punch":
            firepunch(self,other)
        elif used=="Ice Punch":
            icepunch(self,other)
        elif used=="Zen Headbutt":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack({used}).")
            else:
                zenheadbutt(self,other)
        elif used=="Dragon Hammer":
            dragonhammer(self,other)
        elif used=="Arm Thrust":
            hit=random.randint(3,5)
            if self.ability=="Skill Link":
                print(f"{self.name}'s {self.ability}.")
                hit=5
            for i in range(hit):
                armthrust(self,other)
        elif used=="Pin Missile":
            hit=random.randint(3,5)
            if self.ability=="Skill Link":
                print(f"{self.name}'s {self.ability}.")
                hit=5
            for i in range(hit):
                pinmissile(self,other)
            print(f"It hit {hit} time(s).")
        elif used=="Explosion":
            if other.ability=="Damp":
                print("Can't explode on Damp Pokémons.")
            if other.ability!="Damp":
                explosion(self,other)
        elif used=="Icicle Spear":
            hit=random.randint(3,5)
            if self.ability=="Skill Link":
                print(f"{self.name}'s {self.ability}.")
                hit=5
            for i in range(hit):
                iciclespears(self,other)
            print(f"It hit {hit} time(s).")
        elif used=="Waterfall":
            waterfall(self,other)
        elif used=="Wood Hammer":
            woodhammer(self,other)
        elif used=="Energy Ball":
            energyball(self,other)
        elif used=="Rest":
            rest(self)
            if self.hp==self.maxhp:
                print("It failed!")
        elif used=="Bulk Up":
            bulkup(self)
        elif used=="Stone Edge":
            miss=random.randint(1,100)
            if miss>80:
                print(f"{other.name} avoided the attack({used}).")
            else:
                stoneedge(self,other)
        elif used=="Steel Wing":
            steelwing(self,other)
        elif used=="Focus Blast":
            miss=random.randint(1,100)
            if miss>70:
                print(f"{other.name} avoided the attack({used}).")
            else:
                focusblast(self,other)
        elif used=="Rock Slide":
            rockslide(self,other)
        elif used=="Shadow Ball":
            shadowball(self,other)
        elif used=="Wildbolt Storm":
            wildboltstorm(self,other)
        elif used=="Springtide Storm":
            springtidestorm(self,other)
        elif used=="Sandsear Storm":
            sandsearstorm(self,other)
        elif used=="Bleakwind Storm":
            bleakwindstorm(self,other)
        elif used=="Dark Pulse":
            darkpulse(self,other)
        elif used=="Sacred Sword":
            sacredsword(self,other)
        elif used=="Secret Sword":
            secretsword(self,other)
        elif used=="Core Enforcer":
            coreenforcer(self,other)
        elif used=="Superpower":
            superpower(self,other)
        elif used=="Assurance":
            assurance(self,other)
        elif used=="Rock Blast":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack({used}).")
            else:
                hit=random.randint(3,5)
                if self.ability=="Skill Link":
                    print(f"{self.name}'s {self.ability}.")
                    hit=5
                for i in range(hit):
                    rockblast(self,other)
                print(f"It hit {hit} time(s).")
        elif used=="Cross Poison":
            crosspoison(self,other)
        elif used=="Solar Beam":
            solarbeam(self,other)
        elif used=="Sludge Bomb":
            sludgebomb(self,other)
        elif used=="Sludge Wave":
            sludgewave(self,other)
        elif used=="Close Combat":
            closecombat(self,other)
        elif used=="Brave Bird":
            bravebird(self,other)
        elif used=="Body Slam":
            bodyslam(self,other)
        elif used=="Dynamic Punch":
            miss=random.randint(1,100)
            if miss>50 and self.ability!="No Guard":
                print(f"{other.name} avoided the attack({used}).")
            else:
                dynapunch(self,other)
        elif used=="Liquidation":
            liquidation(self,other)
        elif used=="Tera Blast":
            terablast(self,other)
        elif used=="Earthquake":
            earthquake(self,other)
        elif used=="Belch":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack({used}).")
            else:
                belch(self,other)
        elif used=="Gunk Shot":
            miss=random.randint(1,100)
            if miss>80:
                print(f"{other.name} avoided the attack({used}).")
            else:
                gunkshot(self,other)
        elif used=="Freeze Shock":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack({used}).")
            else:
                freezeshock(self,other)                   
        elif used=="Ice Burn":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack({used}).")
            else:
                iceburn(self,other)                      
        elif used=="Blue Flare":
            miss=random.randint(1,100)
            if miss>85:
                print(f"{other.name} avoided the attack({used}).")
            else:
                blueflare(self,other)                
        elif used=="Bolt Strike":
            miss=random.randint(1,100)
            if miss>85:
                print(f"{other.name} avoided the attack({used}).")
            else:
                boltstrike(self,other)       
        elif used=="Mountain Gale":
            miss=random.randint(1,100)
            if miss>85:
                print(f"{other.name} avoided the attack({used}).")
            else:
                mountaingale(self,other)       
                
                                                
        elif used=="Fire Blast":#isinstance(used,FireBlast)
            miss=random.randint(1,100)
            if miss>85:
                print(f"{other.name} avoided the attack({used}).")
            else:
                fireBlast(self,other)
            
                
        elif used=="Pyro Ball":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack({used}).")
            else:
                pyroball(self,other)                
        elif used=="Psychic":
            psychic(self,other)
        elif used=="Seed Flare":
            miss=random.randint(1,100)
            if miss>85:
                print(f"{other.name} avoided the attack({used}).")
            else:
                seedflare(self,other)
        elif used=="Thunderbolt":
            tbolt(self,other)
        elif used=="Poison Jab":
            poisonjab(self,other)
        elif used=="Judgement":
            judgement(self,other)
        elif used=="Ice Beam":
            icebeam(self,other)
        elif used=="Fusion Bolt":
            fusionbolt(self,other)
        elif used=="Fusion Flare":
            fusionflare(self,other)
        elif used=="Moonblast":
            moonblast(self,other)
        elif used=="Hydro Pump":
            miss=random.randint(1,100)
            if miss>80:
                print(f"{other.name} avoided the attack({used}).")
            else:
                hydropump(self,other)
        elif used=="Earth Power":
            earthpower(self,other)
        elif used=="Giga Drain":
            gigadrain(self,other)
        elif used=="Hidden Power":
            hiddenpower(self,other)
        elif used =="Hydro Vortex":
            self.name=self.name.split("(")[0]
            print(f"{self.name} reacting to {tr.name}'s Waterium Z.")
            self.item=None
            hydrovortex(self,other)
            self.moves.remove(used)
        elif used =="Pulverizing Pancake":
            self.name=self.name.split("(")[0]
            print(f"{self.name} reacting to {tr.name}'s Snorlium Z.")
            self.item=None
            pulverizingpancake(self,other)
            self.moves.remove(used)
        elif used =="Splintered Stromshards":
            self.name=self.name.split("(")[0]
            print(f"{self.name} reacting to {tr.name}'s Lycanium Z.")
            self.item=None
            stormshards(self,other)
            self.moves.remove(used)                
        elif used =="Inferno Overdrive":
            self.name=self.name.split("(")[0]
            print(f"{self.name} reacting to {tr.name}'s Firium Z.")
            self.item=None
            infernooverdrive(self,other)
            self.moves.remove(used)
        elif used =="Bloom Doom":
            self.name=self.name.split("(")[0]
            print(f"{self.name} reacting to {tr.name}'s Grassium Z.")
            self.item=None
            bloomdoom(self,other)
            self.moves.remove(used)
        elif used =="Gigavolt Havoc":
            self.name=self.name.split("(")[0]
            print(f"{self.name} reacting to {tr.name}'s Electrium Z.")
            self.item=None
            gigavolthavoc(self,other)
            self.moves.remove(used)
        elif used =="Acid Downpour":
            self.name=self.name.split("(")[0]
            print(f"{self.name} reacting to {tr.name}'s Poisonium Z.")
            aciddownpour(self,other)
            self.moves.remove(used)
        elif used =="Breakneck Blitz":
            self.name=self.name.split("(")[0]
            print(f"{self.name} reacting to {tr.name}'s Normalium Z.")
            self.item=None
            breakneckblitz(self,other)
            self.moves.remove(used)
        elif used =="All-Out Pummeling":
            self.name=self.name.split("(")[0]
            print(f"{self.name} reacting to {tr.name}'s Fightinium Z.")
            self.item=None
            alloutpummeling(self,other)
            self.moves.remove(used)
        elif used =="Black Hole Eclipse":
            self.name=self.name.split("(")[0]
            print(f"{self.name} reacting to {tr.name}'s Darkinium Z.")
            self.item=None
            blackholeeclipse(self,other)
            self.moves.remove(used)
        elif used =="Continental Crush":
            self.name=self.name.split("(")[0]
            print(f"{self.name} reacting to {tr.name}'s Rockium Z.")
            self.item=None
            continentalcrush(self,other)
            self.moves.remove(used)
        elif used =="Tectonic Rage":
            self.name=self.name.split("(")[0]
            print(f"{self.name} reacting to {tr.name}'s Groundium Z.")
            self.item=None
            tectonicrage(self,other)
            self.moves.remove(used)
        elif used =="Corkscrew Crash":
            self.name=self.name.split("(")[0]
            print(f"{self.name} reacting to {tr.name}'s Steelium Z.")
            self.item=None
            corkscrewcrash(self,other)
            self.moves.remove(used)
        elif used =="Devastating Drake":
            self.name=self.name.split("(")[0]
            print(f"{self.name} reacting to {tr.name}'s Dragonium Z.")
            self.item=None
            devastatingdrake(self,other)
            self.moves.remove(used)
        elif used =="Shattered Psyche":
            self.name=self.name.split("(")[0]
            print(f"{self.name} reacting to {tr.name}'s Psychium Z.")
            self.item=None
            shatteredpsyche(self,other)
            self.moves.remove(used)
        elif used =="Never-ending Nightmare":
            self.name=self.name.split("(")[0]
            print(f"{self.name} reacting to {tr.name}'s Ghostium Z.")
            self.item=None
            neverendingnightmare(self,other)
            self.moves.remove(used)
        elif used =="Supersonic Skystrike":
            self.name=self.name.split("(")[0]
            print(f"{self.name} reacting to {tr.name}'s Flyinium Z.")
            self.item=None
            supersonicskystrike(self,other)
            self.moves.remove(used)
        elif used =="Savage Spin-Out":
            self.name=self.name.split("(")[0]
            print(f"{self.name} reacting to {tr.name}'s Buginium Z.")
            self.item=None
            savagespinout(self,other)
            self.moves.remove(used)
        elif used =="Subzero Slammer":
            self.name=self.name.split("(")[0]
            print(f"{self.name} reacting to {tr.name}'s Icium Z.")
            self.item=None
            subzeroslammer (self,other)
            self.moves.remove(used)
        elif used =="Twinkle Tackle":
            self.name=self.name.split("(")[0]
            print(f"{self.name} reacting to {tr.name}'s Fairium Z.")
            self.item=None
            twinkletackle(self,other)
            self.moves.remove(used)
        else:
            pass
    #Type change
    if self.ability in ["Protean","Libero"]:
        self.type2=None
        self.type1=self.atktype
        print(f"{self.name} changed it's type to {self.type1} using {self.ability}!")
#MULTISCALE        
    if multiscale==True and other.hp<other.maxhp:
        self.atk=self.maxatk
        self.spatk=self.maxspatk
        multiscale=False    
    if other.hp>0 and other.hp<=(other.maxhp/2)  and before>(other.maxhp/2):
              if other.item=="Sitrus Berry":
                  other.hp+=round(other.maxhp/4)
                  print(f"{other.name} ate {other.item} and restored some HP!")
                  other.item=None
    if self.hp>0 and self.hp<=(self.maxhp/2)  and sbefore>(self.maxhp/2):
              if self.item=="Sitrus Berry":
                  self.hp+=round(self.maxhp/4)
                  print(f"{self.name} ate {self.item} and restored some HP!")
                  self.item=None
              
#STURDY        
    if before==other.maxhp and other.hp<=0 and hit==1:
        if other.ability=="Sturdy":
            print(f"{other.name}'s Sturdy!")
            other.hp=1
        if other.item=="Focus Sash":
            print(f"{other.name} hung on using Focus Sash.")
            other.hp=1
            other.item=None
    per=round(((before-other.hp)/other.maxhp)*100,2)
    sper=round(((sbefore-self.hp)/self.maxhp)*100,2)
    if other.hp<0:
        per=round((before/other.maxhp)*100,2)
    if self.hp<0:
        sper=round((sbefore/self.maxhp)*100,2)
    if other.hp!=before:
#ILLUSION        
        if other.ability=="Illusion" and "Zoroark" not in other.name:
            if other.type1=="Dark":
                other.name="Zoroark"
                print(f"{other.name}'s Illusion wore off!")
            else:
                other.name="Hisuian Zoroark"
                print(f"{other.name}'s Illusion wore off!")
    if self.hp!=sbefore and self==me:
        if self.ability=="Illusion" and "Zoroark" not in self.name:
            if self.type1=="Dark":
                self.name="Zoroark"
                print(f"{self.name}'s Illusion wore off!")
            else:
                self.name="Hisuian Zoroark"
                print(f"{self.name}'s Illusion wore off!")
    if other.ability=="Flame Body" and self.status=="Alive" and self.ability!="Long Reach":
        ch=random.randint(1,100)  
        if ch>70:
            print(f"{other.name}'s {other.ability}!")
            self.status="Burned"                
    if other.ability=="Static" and self.status=="Alive" and self.ability!="Long Reach":
        ch=random.randint(1,100)  
        if ch>70:
            print(f"{other.name}'s {other.ability}!")
            self.status="Paralyzed"
    if other.ability=="Poison Point" and self.status=="Alive" and self.ability!="Long Reach":
        ch=random.randint(1,100)  
        if ch>70:
            print (f"{other.name}'s {other.ability}!")
            self.status="Badly Poisoned"  
    if self.ability=="Poison Touch" and other.status=="Alive" and other.ability!="Long Reach":
        ch=random.randint(1,100)  
        if ch>70:
            print(f"{self.name}'s {self.ability}!")
            other.status="Badly Poisoned"        
    if used in contactmoves:
        if other.item=="Air Balloon":
            print(f"{other.name}'s Air Balloon popped off!")
            other.item=None                      
    if other.hp!=before and per>0:
        if used not in statusmove:
#ROUGH SKIN/IRON BARBS            
            if other.ability in ["Rough Skin","Iron Barbs"] and used in contactmoves and self.ability!="Long Reach":
                print(f"{me.name} was hurt by {other.name}'s {other.ability}!")
                me.hp-=round((me.maxhp/16),2)
                if me.hp<0:
                    me.hp=0
        if other.item=="Rocky Helmet" and self.ability!="Magic Guard" and used in contactmoves:
            me.hp-=round(me.maxhp/6)
            print(f"{me.name} was hurt by {other.name}'s Rocky Helmet!")
            if me.hp<0:
                me.hp=0                    
#LIFE ORB                    
        if self.item=="Life Orb" and self.ability!="Magic Guard":
            self.hp-=round(self.maxhp/16)
            print(f"{self.name} lost some of its HP!")
            if self.hp<0:
                self.hp=0
#PERCENTAGE                
        print(f"({other.name} lost {per}% of its health!)")
    if self.hp!=sbefore and self==me and sper<0:
        print(f"Total health regained {-sper}%")
    if self.hp!=sbefore and self==me and sper>0:
        print(f"Total damage received {sper}%")
    return self
#EFFECTS
def effects(self,other):
    print("")
#FLINCH RESET    
    self.flinched=False
    if ("Primal Kyogre" not in self.name and "Primal Kyogre" not in other.name) and field.weather=="Primordial Sea":
        field.weather="Clear"
        print("The heavy rain stopped!")
    if ("Primal Groudon" not in self.name and "Primal Groudon" not in other.name) and field.weather=="Desolate Land":
        field.weather="Clear"       
        print("The extremely harsh sunlight faded!")
#GRASSY TERRAIN    
    if field.terrain =="Grassy" and self.hp<self.maxhp and self.ability not in ["Levitate"] and self.type1!="Flying" and self.type2!="Flying":
        print(f"{self.name}'s HP was restored.")
        self.hp+=round(self.maxhp/16)
        if self.hp>self.maxhp:
            self.hp=self.maxhp 
#DRY SKIN            
    if field.weather in ["Sunny","Desolate Land"]:
        if self.ability=="Dry Skin":
            print(f"{self.name}'s {self.ability}!")
            self.hp-=round(self.maxhp/8)
    if field.weather in ["Rainy","Primordial Sea"]:
        if self.ability=="Dry Skin":
            print(f"{self.name}'s {self.ability}!")
            self.hp+=round(self.maxhp/8)  
        if self.hp>self.maxhp:
            self.hp=self.maxhp       
#ICE BODY            
    if field.weather in ["Hail"]:
        if self.ability=="Ice Body":
            print(f"{self.name}'s {self.ability}!")
            self.hp+=round(self.maxhp/8)        
        if self.hp>self.maxhp:
            self.hp=self.maxhp                          
    #BAD DREAMS
    if other.ability=="Bad Dreams" and self.status=="Sleep":
        self.hp-=round(self.maxhp/8)
        print(f"{self.name} was hurt by {other.name}'s {other.ability}.")
    #FROSTBITE
    if self.status=="Frostbite" and self.ability not in ["Magic Guard"]:
        self.hp-=round(self.maxhp/16)
        print(f"{self.name} was hurt by frostbite.")
    #LEECH SEED
    if self.seeded==True:
        print(f"The opposing {self.name}'s health is sapped by leech seed!")
        self.hp-=round(self.maxhp/16)
        if other.hp<=(other.maxhp-other.maxhp/16):
            other.hp+=round(other.maxhp/16)   
    #HAIL DAMAGE
    if (field.weather =="Hail" or field.weather=="Hail"):     
        if self.type1!="Ice" and self.type2!="Ice" and self.ability!="Magic Guard":
            self.hp-=round(self.maxhp/16)
            print(f"{self.name} is buffeted by the hail!")
    #SAND DAMAGE
    if (field.weather =="Sandstorm" or field.weather=="Sandstorm"):
        if self.type1 not in ["Rock","Ground","Steel"] and self.type2 not in ["Rock","Ground","Steel"] and self.ability!="Magic Guard":
            self.hp-=round(self.maxhp/16)
            print(f"{self.name} is buffeted by the sandstorm!")
    #POISON
    if self.status=="Poisoned" and self.ability not in ["Magic Guard","Poison Heal"]:
        self.hp-=round(self.maxhp/16)
        print(f"{self.name} was hurt by poison.")
    #BADLY POISONED
    if self.status=="Badly Poisoned" and self.ability not in ["Magic Guard","Poison Heal"]:
        self.hp-=(self.maxhp*self.badpoison/16)
        self.badpoison+=1
        print(f"{self.name} was hurt by poison.")        
    #BURN        
    if self.status=="Burned" and self.ability!="Magic Guard":
        self.hp-=round(self.maxhp/16)
        print(f"{self.name} was hurt by burn.")        
    #LEFTOVERS        
    if self.hp>0 and self.item=="Leftovers" and self.hp<self.maxhp:
        print(f"{self.name} restored a little HP using its Leftovers.")
        self.hp+=round(self.maxhp/16)
        
    #BLACK SLUDGE        
    if self.hp>0 and self.item=="Black Sludge" and self.hp<self.maxhp:
        if self.type1=="Poison" or self.type2=="Poison":
            print(f"{self.name} restored a little HP using its Black Sludge.")
            self.hp+=round(self.maxhp/16)    
        elif self.type1!="Poison" and self.type2!="Poison":   
            print(f"{self.name} lost a little HP using its Black Sludge.")
            self.hp-=round(self.maxhp/16)
    #POISON HEAL        
    if self.hp>0 and self.ability=="Poison Heal" and self.hp!=self.maxhp and self.status=="Badly Poisoned":
        print(f"{self.name} restored a little HP using its Poison Heal.")
        self.hp+=round(self.maxhp/8)                    

    if self.hp>self.maxhp:
        self.hp=self.maxhp
    if self.hp<0:
        self.hp=0