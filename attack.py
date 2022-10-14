from trainerlist import *
from moves import *
def switch(current,trainer,other):
    showmon(trainer)
    if  current==None:
        #current=switch (current,trainer,other)
        n=random.randint(1,len(trainer.pokemons)-1)
        new=trainer.pokemons[n]
        current=(trainer.pokemons[0])
        phase1=random.choice([" return! You did well buddy."," return! You disappointed me."," return! Pathetic Pokémon."," return! Take rest my friend."," return! You were strong as always."])
        print(f"\n{trainer.name}: "+current.name+phase1)
        current=new
        phase2=random.choice(["It's our show time.","Show your strength.","Let's do it buddy.","I believe in you!","Let's finish this off.","Are you ready buddy?","Let's show them what you are capable of."])
        print(f"Go {current.name}! "+phase2)
        weatherset(current)
        return current
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
    current.intimidated=False
    current.protect=False
    other.protect=False
    
    n=(input(f"{trainer.name} Choose a Pokemon: "))
    if n=="info":
        n=(input("Which pokemon you wanna see?"))
        if n in ["1","2","3","4","5","6"]:
            n=int(n)
            trainer.pokemons[n-1].info()
            movelist(trainer.pokemons[n-1])
            return switch(current,trainer,other)
        else:
            return switch(current,trainer,other)
    if n not in ["1","2","3","4","5","6"] and len(trainer.pokemons)>0:
        n=random.randint(1,len(trainer.pokemons))
    if n in ["1","2","3","4","5","6"]:
        n=int(n)
    if n not in [1,2,3,4,5,6] and len(trainer.pokemons)>0:
        n=random.randint(1,len(trainer.pokemons))
    
    new=trainer.pokemons[n-1]
    if new==current:
   	    print(f"\n{current.name} is already in battle.")
   	    return switch(current,trainer,other)			
    if new!=current:
        if current.ability=="Regenerator":
            print("{current.name}'s {current.ability}.")
            if current.hp<=(current.maxhp/3):
                current.hp+=current.maxhp/3
            elif current.hp>(current.maxhp/3):
                current.hp=current.maxhp
        if "Red" in trainer.name:
            print(f"{trainer.name}: ........")
            current=new
            weatherset(current)
            return current
        else:
            phase1=random.choice([" return! You did well buddy."," return! You disappointed me."," return! Pathetic Pokémon."," return! Take rest my friend."," return! You were strong as always."])
            print(f"\n{trainer.name}: "+current.name+phase1)
            current=new
            phase2=random.choice(["It's our show time.","Show your strength.","Let's do it buddy.","I believe in you!","Let's finish this off.","Are you ready buddy?","Let's show them what you are capable of."])
            print(f"Go {current.name}! "+phase2)
            weatherset(current)
            return current
    else:
        #switch(current,trainer,other)
        return current

#ATTACK
def attack(self,other,tr,optr,use,opuse):
    print(f"\n{tr.name}:")
    used=use
    hit=1
    buffmove=["Iron Defense","Calm Mind","Swords Dance","Shell Smash","Bulk Up","Recover","Roost","Moonlight","Morning Sun","Synthesis","Hail","Rain Dance","Sunny Day","Sandstorm","Trickroom","Dragon Dance","Belly Drum","Nasty Plot","Rest","Coil","Curse","Explosion"]
    statusmove=["Sleep Powder","Iron Defense","Calm Mind","Swords Dance","Bulk Up","Recover","Roost","Thunder Wave","Lunar Blessing","Take Heart","Heart Swap","Will-O-Wisp","Moonlight","Synthesis","Morning Sun","Rain Dance","Sunny Day","Hail","Sandstorm","Dark Void","Trick Room","Nasty Plot","Shell Smash","Dragon Dance","Belly Drum","Spore","Hypnosis","Rest","Coil","Curse","Strength Sap","Leech Seed","Protect"]
    me=self
    canatk=True
    multiscale=False
    if self.ability=="Intimidate" and other.intimidated==False:
        other.intimidated=True
        atkchange(other,-0.5)
        print(f"{self.name}'s {self.ability}")
        print(f"{other.name}'s attack was lowered.")    
    if self.ability=="Speed Boost":
        if self.speed<(self.maxspeed*4) and self.speedb<4:
            print(f"{self.name}'s speed rose.")
            speedchange(self,0.5)
        else:
            print(f"{self.name}'s speed won't go higher.")
    
    if self.status=="Paralyzed":
        ch=random.randint(1,3)
        if ch==3:
            canatk=False
        else:
            canatk=True
    if self.status=="Sleep":
        ch=random.randint(1,3)
        if ch==3:
            print(f"{self.name} woke up.")
            self.status="Alive"
        else:
            pass
    if self.status=="Frozen":
        ch=random.randint(1,5)
        if ch==3:
            print(f"{self.name} thawed out.")
            self.status="Alive"
        else:
            pass
    before=other.hp
    sbefore=self.hp
    print("")
    if other.ability=="Multiscale" and other.hp==other.maxhp:
        print(f"{other.name}'s {other.ability}.")
        self.atk=self.maxatk/2
        self.spatk=self.maxspatk/2
        multiscale=True
    if used in self.moves:
        if self.item=="Assault Vest" and used in statusmove:
            print(f"Cannot used status moves while holding an Assault Vest.")
            attack(self,other,tr,optr)
        if used!="Protect":
            self.protect=False
        elif used=="Lunar Blessing":
            lunarblessing(self)
            if self.status!="Alive":
                self.status="Alive"
                print(f"{self.name}'s status was cured.")
        elif used=="Take Heart":
            takeheart(self,other)
            if self.status!="Alive":
                self.status="Alive"
                print(f"{self.name}''s status was cured.")
        elif self.status=="Sleep":
            print(f"{self.name} is sleeping.")
            used=None
        if self.recharge==True:
            print(f"{self.name} is recharging.")
            self.recharge=False
            used=None
        if self.flinched==True:
            print(f"{self.name} flinched.")
            self.flinched=False
            used=None
        if self.status=="Paralyzed" and canatk==False:
            print(f"{self.name} is paralyzed and unable to move.")
        elif self.status=="Frozen":
            print(f"{self.name} is frozen solid.")
            used=None
        elif used=="Will-O-Wisp":
            miss=random.randint(1,100)
            if miss>85:
                print(f"{other.name} avoided the attack.")
            else:
                willowisp(self,other)
        elif self.protect=="Pending" and used=="Protect":
            print(f"{self.name} used {used}!")
            print("It failed.")
            self.protect=False
            used=None
        elif other.protect==True and used not in buffmove:
            print(f"{other.name} protected itself.")
            other.protect="Pending"
            
        elif used=="Toxic":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack.")
            else:
                toxic(self,other)
        elif used=="Thunder Wave":
            thunderwave(self,other)
        elif used=="Sucker Punch":
            if opuse in statusmove:
                print("It failed.")
            else:
                suckerpunch(self,other)
        elif used=="Psystrike":
            psystrike(self,other)
        elif used=="Doom Desire":
            doomdesire(self,other)
        elif used=="Shadow Sneak":
            shadowsneak(self,other)
        elif used=="Heavy Slam":
            heavyslam(self,other)
        elif used=="Heart Swap":
            heartswap(self,other)
        elif used=="Steel Beam":
            steelbeam(self,other)
        elif used=="Crush Grip":
            crushgrip(self,other)
        elif used=="Rain Dance":
            raindance(self)
        elif used=="Sunny Day":
            sunnyday(self)
        elif used=="Leech Seed":
            leechseed(self,other)
        elif used=="Trick Room":
            trickroomm(self)
        elif used=="Sandstorm":
            sandstorm(self)
        elif used=="Synthesis":
            synthesis(self)
        elif used=="Hail":
            hail(self)
        elif used=="Quiver Dance":
            quiverdance(self)
        elif used=="Defense Order":
            defenseorder(self)
        elif used=="Swords Dance":
            swordsdance(self)
        elif used=="Nasty Plot":
            nastyplot(self)
        elif used=="Shell Smash":
            shellsmash(self)
        elif used=="Dragon Dance":
            dragondance(self)
        elif used=="Iron Defense":
            irondefense(self)
        elif used=="Bullet Punch":
            bulletpunch(self,other)
        elif used=="X-Scissor":
            xscissor(self,other)
        elif used=="Boomburst":
            boomburst(self,other)
        elif used=="Knock Off":
            knockoff(self,other)
        elif used=="Facade":
            facade(self,other)
            
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
        elif used=="Flip Turn":
            flipturn(self,other)
            if len(tr.pokemons)>1 and (other.hp!=before):
                print(f"{self.name} returned to it's pokéball.")
                self=switch(self,tr,other)
        elif used=="U-Turn":
            uturn(self,other)
            if len(tr.pokemons)>1:
                print(f"{self.name} returned to it's pokéball.")
                self=switch(self,tr,other)
        elif used=="Parting Shot":
            partingshot(self,other)
            if len(tr.pokemons)>1:
                print(f"{self.name} returned to it's pokéball.")
                self=switch(self,tr,other)                
        elif used=="Volt Switch":
            voltswitch(self,other)
            if len(tr.pokemons)>1 and (other.hp!=before):
                print(f"{self.name} returned to it's pokéball.")
                self=switch(self,tr,other)
        elif used=="Extreme Speed":
            extemespeed(self,other)
        elif used=="Inferno":
            miss=random.randint(1,100)
            if miss>50:
                print(f"{other.name} avoided the attack.")
            else:
                inferno(self,other)
        elif used=="Overheat":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack.")
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
                print(f"{other.name} avoided the attack.")
            else:
                sleeppowder(self,other)
        elif used=="Spore":
            spore(self,other)
        elif used=="Hypnosis":
            miss=random.randint(1,100)
            if miss>60:
                print(f"{other.name} avoided the attack.")
            else:
                hypnosis(self,other)
        elif used=="Dark Void":
            miss=random.randint(1,100)
            if miss>80:
                print(f"{other.name} avoided the attack.")
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
                    print(f"{other.name} avoided the attack.")
                elif miss<=70:
                    blizzard(self,other)
        elif used=="Air Slash":
            miss=random.randint(1,100)
            if miss>95:
                print(f"{other.name} avoided the attack.")
            else:
                airslash(self,other)
        elif used=="Bone Rush":
            bonerush(self,other)
        elif used=="Gyro Ball":
            gyroball(self,other)
        elif used=="Blast Burn":
            blastburn(self,other)
            self.recharge=True
        elif used=="Zap Cannon":
            miss=random.randint(1,100)
            if miss>50:
                print(f"{other.name} avoided the attack.")
            else:
                zapcannon(self,other)
        elif used=="Freeze Dry":
            freezedry(self,other)
        elif used=="Ice Fang":
            icefang(self,other)
        elif used=="Coil":
            coil(self)
        elif used=="Dual Wingbeat":
            dualwingbeat(self,other)
        elif used=="Curse":
            curse(self)
        elif used=="Dragon Ascent":
            dragonascent(self,other)
        elif used=="Foul Play":
            foulplay(self,other)
        elif used=="High Horsepower":
            highhorsepower(self,other)
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
        elif used=="Wild Charge":
            wildcharge(self,other)
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
                print(f"{other.name} avoided the attack.")
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
                    print(f"{other.name} avoided the attack.")
                elif miss>=50:
                    hurricane(self,other)
            elif field.weather != "Rainy" and field.weather !="Rainy":
                miss=random.randint(1,100)
                if miss>70:
                    print(f"{other.name} avoided the attack.")
                elif miss>=30:
                    hurricane(self,other)
          
        elif used=="Sky Uppercut":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack.")
            else:
                skyuppercut(self,other)
        elif used=="Precipice Blades":
            miss=random.randint(1,100)
            if miss>85:
                print(f"{other.name} avoided the attack.")
            else:
                precipiceblades(self,other)
        elif used=="Origin Pulse":
            miss=random.randint(1,100)
            if miss>85:
                print(f"{other.name} avoided the attack.")
            else:
                originpulse(self,other)
        elif used=="Draco Meteor":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack.")
            else:
                dracometeor(self,other)
        elif used=="Psycho Boost":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack.")
            else:
                psychoboost(self,other)
        elif used=="Drill Run":
            miss=random.randint(1,100)
            if miss>95:
                print(f"{other.name} avoided the attack.")
            else:
                drillrun(self,other)
        elif used=="Head Smash":
            miss=random.randint(1,100)
            if miss>80:
                print(f"{other.name} avoided the attack.")
            else:
                headsmash(self,other)
        elif used=="Flash Cannon":
            flashcannon(self,other)
        elif used=="Stealth Rock":
            if "Stealth Rock" not in optr.hazard:
                print(f"{self.name} usedd Stealth Rock.")
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
            softboiled(self)
        elif used=="Heal Order":
            healorder(self)
        elif used=="Slack Off":
            slackoff(self)
        elif used=="Roost":
            roost(self)
        elif used=="Recover":
            recover(self)
        elif used=="Protect":
            self.protect=True
            print(f"{self.name} used Protect.")
        elif used=="Morning Sun":
            morningsun(self)
        elif used=="Moonlight":
            moonlight(self)
        elif used=="Megahorn":
            miss=random.randint(1,100)
            if miss>85:
                print(f"{other.name} avoided the attack.")
            else:
                megahorn(self,other)
        elif used=="Leaf Storm":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack.")
            else:
                leafstorm(self,other)
        elif used=="Leaf Tornado":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack.")
            else:
                leaftornado(self,other)
        elif used=="Leaf Blade":
            leafblade(self,other)
        elif used=="Razor Leaf":
            razorleaf(self,other)
        elif used=="Victory Dance":
            victorydance(self)
        elif used=="Light Screen":
            lightscreen(self,other)
        elif used=="Calm Mind":
            calmmind(self)
        elif used=="Reflect":
            reflect(self,other)
        elif used=="Acid Armor":
            acidarmor(self)
        elif used=="Aeroblast":
            miss=random.randint(1,100)
            if miss>95:
                print(f"{other.name} avoided the attack.")
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
        elif used=="Surging Strike":
            surgingstrikes(self,other)
        elif used=="Heat Wave":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack.")
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
                print(f"{other.name} avoided the attack.")
            else:
                sacredfire(self,other)
        elif used=="Brick Break":
            brickbreak(self,other)
        elif used=="Giga Impact":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack.")
            else:
                gigaimpact(self,other)
                self.recharge=True
        elif used=="Hyper Beam":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack.")
            else:
                hyperbeam(self,other)
                self.recharge=True
        elif used=="Roar of Time":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack.")
            else:
                roaroftime(self,other)
                self.recharge=True
        elif used=="Spacial Rend":
            miss=random.randint(1,100)
            if miss>95:
                print(f"{other.name} avoided the attack.")
            else:
                spacialrend(self,other)
        elif used=="Shadow Force":
            miss=random.randint(1,100)
            if miss>95:
                print(f"{other.name} avoided the attack.")
            else:
                shadowforce(self,other)                
        elif used=="Iron Head":
            ironhead(self,other)
        elif used=="Iron Tail":
            miss=random.randint(1,100)
            if miss>75:
                print(f"{other.name} avoided the attack.")
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
                print(f"{other.name} avoided the attack.")
            else:
                playrough (self,other)
        elif used=="Power Whip":
            powerwhip(self,other)
        elif used=="Ancient Power":
            apower(self,other)
        elif used=="Strength":
            strength(self,other)
        elif used=="Dizzy Punch":
            dizzypunch (self,other)
        elif used=="Mach Punch":
            machpunch(self,other)
        elif used=="Thunder":
            if field.weather in ["Rainy","Primordial Sea"] and field.weather in ["Rainy","Primordial Sea"]:
                thunder(self,other)
            else:
                miss=random.randint(1,100)
                if miss>70:
                    print(f"{other.name} avoided the attack.")
                elif miss<=70:
                    thunder(self,other)
        elif used=="Scald":
            scald(self,other)
        elif used=="Egg Bomb":
            eggbomb(self,other)
        elif used=="Hex":
            hex (self,other)
        elif used=="Fakeout":
            fakeout(self,other)
        elif used=="Power-up Punch":
            poweruppunch(self,other)
        elif used=="Double Edge":
            doubleedge(self,other)
        elif used=="Dragon Claw":
            dragonclaw(self,other)
        elif used=="Surf":
            surf(self,other)
        elif used=="Aqua Tail":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack.")
            else:
                aquatail(self,other)
        elif used=="Sky Attack":
            skyattack(self,other)
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
                print(f"{other.name} avoided the attack.")
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
        elif used=="Bulk Up":
            bulkup(self)
        elif used=="Stone Edge":
            miss=random.randint(1,100)
            if miss>80:
                print(f"{other.name} avoided the attack.")
            else:
                stoneedge(self,other)
        elif used=="Steel Wing":
            steelwing(self,other)
        elif used=="Focus Blast":
            miss=random.randint(1,100)
            if miss>70:
                print(f"{other.name} avoided the attack.")
            else:
                focusblast(self,other)
        elif used=="Rock Slide":
            rockslide(self,other)
        elif used=="Shadow Ball":
            shadowball(self,other)
        elif used=="Wildbolt Storm":
            wildboltstorm(self,other)
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
        elif used=="Superpower":
            superpower(self,other)
        elif used=="Assurance":
            assurance(self,other)
        elif used=="Rock Blast":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack.")
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
        elif used=="Close Combat":
            closecombat(self,other)
        elif used=="Brave Bird":
            bravebird(self,other)
        elif used=="Body Slam":
            bodyslam(self,other)
        elif used=="Dynamic Punch":
            miss=random.randint(1,100)
            if miss>50 and self.ability!="No Guard":
                print(f"{other.name} avoided the attack.")
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
                print(f"{other.name} avoided the attack.")
            else:
                belch(self,other)
        elif used=="Gunk Shot":
            miss=random.randint(1,100)
            if miss>80:
                print(f"{other.name} avoided the attack.")
            else:
                gunkshot(self,other)
        elif used=="Fire Blast":
            miss=random.randint(1,100)
            if miss>85:
                print(f"{other.name} avoided the attack.")
            else:
                fireBlast(self,other)
        elif used=="Psychic":
            psychic(self,other)
        elif used=="Seed Flare":
            miss=random.randint(1,100)
            if miss>85:
                print(f"{other.name} avoided the attack.")
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
        elif used=="Moon Blast":
            moonblast(self,other)
        elif used=="Hydro Pump":
            miss=random.randint(1,100)
            if miss>80:
                print(f"{other.name} avoided the attack.")
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
    if multiscale==True and other.hp<other.maxhp:
        self.atk=self.maxatk
        self.spatk=self.maxspatk
        multiscale=False    
    if before==other.maxhp and other.hp<=0 and hit==1:
        if other.ability=="Sturdy":
            print(f"{other.name}'s Sturdy")
            other.hp=1
        if other.item=="Focus Sash":
            print(f"{other.name} hung on using Focus Sash")
            other.hp=1
            other.item=None
    per=round(((before-other.hp)/other.maxhp)*100,2)
    sper=round(((sbefore-self.hp)/self.maxhp)*100,2)
    if other.hp<0:
        per=round((before/other.maxhp)*100,2)
    if self.hp<0:
        sper=round((sbefore/self.maxhp)*100,2)
    if other.hp!=before and per>0:
        if self.item=="Life Orb":
            self.hp-=round(self.maxhp/16)
            print(f"{self.name} lost some of its HP!")
            if self.hp<0:
                self.hp=0
        print(f"({other.name} lost {per}% of its health!)")
    if other.hp!=before and per<0:
        print(f"{other.name}' health regained {-per}%")
    if self.hp!=sbefore and self==me and sper<0:
        print(f"Total health regained {-sper}%")
    if self.hp!=sbefore and self==me and sper>0:
        print(f"Total damage received {sper}%")
    return self
def effects(self,other):
    print("")
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
            print(f"{self.name} got pelted by hail.")
    #SAND DAMAGE
    if (field.weather =="Sandstorm" or field.weather=="Sandstorm"):
        if self.type1 not in ["Rock","Ground","Steel"] and self.type2 not in ["Rock","Ground","Steel"] and self.ability!="Magic Guard":
            self.hp-=round(self.maxhp/16)
            print(f"{self.name} got pelted by sandstorm.")
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