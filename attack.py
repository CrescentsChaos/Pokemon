#pylint:disable=W0401
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
    current.flinch=False
    
    n=(input(f"{trainer.name} Choose a Pokemon: "))
    if n not in ["1","2","3","4","5","6"] and len(trainer.pokemons)>0:
        n=random.randint(1,len(trainer.pokemons))
    if n in ["1","2","3","4","5","6"]:
        n=int(n)
    if n not in [1,2,3,4,5,6] and len(trainer.pokemons)>0:
        n=random.randint(1,len(trainer.pokemons))
    
    new=trainer.pokemons[n-1]
    
    
    if new.status=="Fainted":
        print(f"{new.name} is unable to battle.")
        switch(current,trainer,other)		
    if new==current and current.status=="Fainted":
        print(f"\n{new.name} is unable to battle.")
        switch(current,trainer,other)
        current=new
        return current	
    if new==current and current.status!="Fainted":
   	    print(f"\n{current.name} is already in battle.")
   	    return switch(current,trainer,other)			
    if new!=current and new.status!="Fainted":
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
def attack(self,other,tr,optr):
    me=self
    movelist(self)
    canatk=True
    multiscale=False
    
    if self.ability=="Speed Boost":
        if self.speed<(self.maxspeed*4) and self.speedb<4:
            print(f"{self.name}'s speed rose.")
            self.speedb+=0.5
            self.speed+=(self.speed/2)
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
    use=(input(f"\n{tr.name} select a move: "))
    if use=="stats":
        self.info()
        other.info()
    print("")
    if use in ["1","2","3","4","5","6","7"]:
        use=int(use)
    elif use not in [1,2,3,4,5,6,7]:
        use=random.randint(1,len(self.moves))
    use=self.moves[use-1]
    if other.ability=="Multiscale" and other.hp==other.maxhp:
        print(f"{other.name}'s {other.ability}.")
        self.atk=self.maxatk/2
        self.spatk=self.maxspatk/2
        multiscale=True
    if use in self.moves:
        if self.status=="Sleep":
            print(f"{self.name} is sleeping.")
        elif self.recharge==True:
            print(f"{self.name} is recharging.")
            self.recharge=False
        elif self.flinch==True:
            print(f"{self.name} flinched.")
            self.flinch=False
        elif self.status=="Paralyzed" and canatk==False:
            print(f"{self.name} is paralyzed.")
        elif self.status=="Frozen":
            print(f"{self.name} is frozen solid.")
        elif use=="Will-O-Wisp":
            miss=random.randint(1,100)
            if miss>85:
                print(f"{other.name} avoided the attack.")
            else:
                willowisp(self,other)
        elif use=="Toxic":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack.")
            else:
                toxic(self,other)
        elif use=="Thunder Wave":
            thunderwave(self,other)
        elif use=="Psystrike":
            psystrike(self,other)
        elif use=="Doom Desire":
            doomdesire(self,other)
        elif use=="Heavy Slam":
            heavyslam(self,other)
        elif use=="Steel Beam":
            steelbeam(self,other)
        elif use=="Rain Dance":
            raindance(self)
        elif use=="Sunny Day":
            sunnyday(self)
        elif use=="Leech Seed":
            leechseed(self,other)
        elif use=="Sandstorm":
            sandstorm(self)
        elif use=="Synthesis":
            synthesis(self)
        elif use=="Hail":
            hail(self)
        elif use=="Swords Dance":
            swordsdance(self)
        elif use=="Nasty Plot":
            nastyplot(self)
        elif use=="Shell Smash":
            shellsmash(self)
        elif use=="Dragon Dance":
            dragondance(self)
        elif use=="Iron Defense":
            irondefense(self)
        elif use=="Bullet Punch":
            bulletpunch(self,other)
        elif use=="X-Scissor":
            xscissor(self,other)
        elif use=="Boomburst":
            boomburst(self,other)
        elif use=="Knock Off":
            knockoff(self,other)
        elif use=="Facade":
            facade(self,other)
        elif use=="Luster Purge":
            lusterpurge(self,other)
        elif use=="Hammer Arm":
            hammerarm(self,other)
        elif use=="Final Gambit":
            finalgambit(self,other)
        elif use=="Bolt Beak":
            boltbeak(self,other)
        elif use=="Meteor Mash":
           meteormash(self,other)
        elif use=="Venoshock":
             venoshock(self,other)
        elif use=="Mist Ball":
            mistball(self,other)
        elif use=="Seed Bomb":
            seedbomb(self,other)
        elif use=="Flip Turn":
            flipturn(self,other)
            if len(tr.pokemons)>1:
                print(f"{self.name} returned to it's pokéball.")
                self=switch(self,tr,other)
        elif use=="U-Turn":
            uturn(self,other)
            if len(tr.pokemons)>1:
                print(f"{self.name} returned to it's pokéball.")
                self=switch(self,tr,other)
        elif use=="Parting Shot":
            partingshot(self,other)
            if len(tr.pokemons)>1:
                print(f"{self.name} returned to it's pokéball.")
                self=switch(self,tr,other)                
        elif use=="Volt Switch":
            voltswitch(self,other)
            if len(tr.pokemons)>1:
                print(f"{self.name} returned to it's pokéball.")
                self=switch(self,tr,other)
        elif use=="Extreme Speed":
            extemespeed(self,other)
        elif use=="Inferno":
            miss=random.randint(1,100)
            if miss>50:
                print(f"{other.name} avoided the attack.")
            else:
                inferno(self,other)
        elif use=="Overheat":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack.")
            else:
                overheat(self,other)
        elif use=="Whirlwind":
            print(f"{self.name} used Whirlwind.")
            print(f"{other.name} blew away with the wind.")
        elif use=="Return":
            retrn(self,other)
        elif use=="Sleep Powder":
            miss=random.randint(1,100)
            if miss>75:
                print(f"{other.name} avoided the attack.")
            else:
                sleeppowder(self,other)
        elif use=="Spore":
            spore(self,other)
        elif use=="Hypnosis":
            miss=random.randint(1,100)
            if miss>60:
                print(f"{other.name} avoided the attack.")
            else:
                hypnosis(self,other)
        elif use=="Dark Void":
            miss=random.randint(1,100)
            if miss>80:
                print(f"{other.name} avoided the attack.")
            else:
                darkvoid(self,other)
        elif use=="Body Press":
            bodypress(self,other)
        elif use=="Blizzard":
            if Pokemon.weather == "Hail" and Pokemon2.weather =="Hail":
                blizzard(self,other)
            if Pokemon.weather != "Hail" and Pokemon2.weather !="Hail":
                miss=random.randint(1,100)
                if miss>70:
                    print(f"{other.name} avoided the attack.")
                elif miss<=70:
                    blizzard(self,other)
        elif use=="Air Slash":
            miss=random.randint(1,100)
            if miss>95:
                print(f"{other.name} avoided the attack.")
            else:
                airslash(self,other)
        elif use=="Bone Rush":
            bonerush(self,other)
        elif use=="Gyro Ball":
            gyroball(self,other)
        elif use=="Blast Burn":
            blastburn(self,other)
            self.recharge=True
        elif use=="Zap Cannon":
            miss=random.randint(1,100)
            if miss>50:
                print(f"{other.name} avoided the attack.")
            else:
                zapcannon(self,other)
        elif use=="Freeze Dry":
            freezedry(self,other)
        elif use=="Ice Fang":
            icefang(self,other)
        elif use=="Coil":
            coil(self)
        elif use=="Dual Wingbeat":
            dualwingbeat(self,other)
        elif use=="Curse":
            curse(self)
        elif use=="Dragon Ascent":
            dragonascent(self,other)
        elif use=="Foul Play":
            foulplay(self,other)
        elif use=="Signal Beam":
            signalbeam(self,other)
        elif use=="Wild Charge":
            wildcharge(self,other)
        elif use=="Power Gem":
            powergem(self,other)
        elif use=="High Jump Kick":
            hijumpkick(self,other)
        elif use=="Blaze Kick":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack.")
            else:
                blazekick(self,other)
        elif use=="Crush Claw":
            crushclaw(self,other)
        elif use=="Lava Plume":
            lavaplume(self,other)
        elif use=="Hurricane":
            if Pokemon.weather == "Rainy" and Pokemon2.weather =="Rainy":
                hurricane(self,other)
            if Pokemon2.weather =="Sunny" and Pokemon2.weather == "Sunny":
                miss=random.randint(1,100)
                if miss>50:
                    print(f"{other.name} avoided the attack.")
                elif miss>=50:
                    hurricane(self,other)
            elif Pokemon.weather != "Rainy" and Pokemon2.weather !="Rainy":
                miss=random.randint(1,100)
                if miss>70:
                    print(f"{other.name} avoided the attack.")
                elif miss>=30:
                    hurricane(self,other)
          
        elif use=="Sky Uppercut":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack.")
            else:
                skyuppercut(self,other)
        elif use=="Precipice Blades":
            miss=random.randint(1,100)
            if miss>85:
                print(f"{other.name} avoided the attack.")
            else:
                precipiceblades(self,other)
        elif use=="Origin Pulse":
            miss=random.randint(1,100)
            if miss>85:
                print(f"{other.name} avoided the attack.")
            else:
                originpulse(self,other)
        elif use=="Draco Meteor":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack.")
            else:
                dracometeor(self,other)
        elif use=="Psycho Boost":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack.")
            else:
                psychoboost(self,other)
        elif use=="Drill Run":
            miss=random.randint(1,100)
            if miss>95:
                print(f"{other.name} avoided the attack.")
            else:
                drillrun(self,other)
        elif use=="Head Smash":
            miss=random.randint(1,100)
            if miss>80:
                print(f"{other.name} avoided the attack.")
            else:
                headsmash(self,other)
        elif use=="Flash Cannon":
            flashcannon(self,other)
        elif use=="Stealth Rock":
            if "Stealth Rock" not in optr.hazard:
                print(f"{self.name} used Stealth Rock.")
                optr.hazard.append("Stealth Rock")
        elif use=="Transform":
            transform(self,other)
        elif use=="Seismic Toss":
            seismictoss(self,other)
        elif use=="Night Shade":
            nightshade(self,other)
        elif use=="Snarl":
            snarl(self,other)
        elif use=="Soft Boiled":
            softboiled(self)
        elif use=="Heal Order":
            healorder(self)
        elif use=="Slack Off":
            slackoff(self)
        elif use=="Roost":
            roost(self)
        elif use=="Recover":
            recover(self)
        elif use=="Megahorn":
            miss=random.randint(1,100)
            if miss>85:
                print(f"{other.name} avoided the attack.")
            else:
                megahorn(self,other)
        elif use=="Leaf Storm":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack.")
            else:
                leafstorm(self,other)
        elif use=="Leaf Tornado":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack.")
            else:
                leaftornado(self,other)
        elif use=="Leaf Blade":
            leafblade(self,other)
        elif use=="Light Screen":
            lightscreen(self,other)
        elif use=="Calm Mind":
            calmmind(self)
        elif use=="Reflect":
            reflect(self,other)
        elif use=="Acid Armor":
            acidarmor(self)
        elif use=="Aeroblast":
            miss=random.randint(1,100)
            if miss>95:
                print(f"{other.name} avoided the attack.")
            else:
                aeroblast(self,other)
        elif use=="Wicked Blow":
            wickedblow(self,other)
        elif use=="Force Palm":
            forcepalm(self,other)
        elif use=="Drain Punch":
            drainpunch(self,other)
        elif use=="Frost Breath":
            frostbreath(self,other)
        elif use=="Icicle Crash":
            iciclecrash(self,other)
        elif use=="Scorching Sands":
            scorchingsands(self,other)
        elif use=="Strength Sap":
            strengthsap(self,other)
        elif use=="Surging Strike":
            surgingstrikes(self,other)
        elif use=="Heat Wave":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack.")
            else:
                heatwave(self,other)
        elif use=="Slash":
            slash(self,other)
        elif use=="Night Slash":
            nightslash(self,other)
        elif use=="Psycho Cut":
            psychocut(self,other)
        elif use=="Sacred Fire":
            miss=random.randint(1,100)
            if miss>95:
                print(f"{other.name} avoided the attack.")
            else:
                sacredfire(self,other)
        elif use=="Brick Break":
            brickbreak(self,other)
        elif use=="Hyper Beam":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack.")
            else:
                hyperbeam(self,other)
                self.recharge=True
        elif use=="Iron Head":
            ironhead(self,other)
        elif use=="Iron Tail":
            miss=random.randint(1,100)
            if miss>75:
                print(f"{other.name} avoided the attack.")
            else:
                irontail (self,other)
        elif use=="Dazzling Gleam":
            dazzlinggleam (self,other)
        elif use=="Water Spout":
            waterspout(self,other)
        elif use=="Eruption":
            eruption (self,other)
        elif use=="Dragon Pulse":
            dragonpulse (self,other)
        elif use=="Play Rough":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack.")
            else:
                playrough (self,other)
        elif use=="Power Whip":
            powerwhip(self,other)
        elif use=="Ancient Power":
            apower(self,other)
        elif use=="Strength":
            strength(self,other)
        elif use=="Dizzy Punch":
            dizzypunch (self,other)
        elif use=="Mach Punch":
            machpunch(self,other)
        elif use=="Thunder":
            if Pokemon.weather == "Rainy" and Pokemon2.weather =="Rainy":
                thunder(self,other)
            else:
                miss=random.randint(1,100)
                if miss>70:
                    print(f"{other.name} avoided the attack.")
                elif miss<=70:
                    thunder(self,other)
        elif use=="Scald":
            scald(self,other)
        elif use=="Egg Bomb":
            eggbomb(self,other)
        elif use=="Fakeout":
            fakeout(self,other)
        elif use=="Power-up Punch":
            poweruppunch(self,other)
        elif use=="Double Edge":
            doubleedge(self,other)
        elif use=="Dragon Claw":
            dragonclaw(self,other)
        elif use=="Surf":
            surf(self,other)
        elif use=="Aqua Tail":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack.")
            else:
                aquatail(self,other)
        elif use=="Sky Attack":
            skyattack(self,other)
        elif use=="Crunch":
            crunch(self,other)
        elif use=="Flamethrower":
            flamethrower(self,other)
        elif use=="Flare Blitz":
            flareblitz(self,other)
        elif use=="Thunder Punch":
            tpunch(self,other)
        elif use=="Fire Punch":
            firepunch(self,other)
        elif use=="Ice Punch":
            icepunch(self,other)
        elif use=="Zen Headbutt":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack.")
            else:
                zenheadbutt(self,other)
        elif use=="Dragon Hammer":
            dragonhammer(self,other)
        elif use=="Pin Missile":
            pinmissile(self,other)
        elif use=="Icicle Spears":
            iciclespears(self,other)
        elif use=="Waterfall":
            waterfall(self,other)
        elif use=="Rest":
            rest(self)
        elif use=="Bulk Up":
            bulkup(self)
        elif use=="Stone Edge":
            miss=random.randint(1,100)
            if miss>80:
                print(f"{other.name} avoided the attack.")
            else:
                stoneedge(self,other)
        elif use=="Steel Wing":
            steelwing(self,other)
        elif use=="Focus Blast":
            miss=random.randint(1,100)
            if miss>70:
                print(f"{other.name} avoided the attack.")
            else:
                focusblast(self,other)
        elif use=="Rock Slide":
            rockslide(self,other)
        elif use=="Shadow Ball":
            shadowball(self,other)
        elif use=="Dark Pulse":
            darkpulse(self,other)
        elif use=="Superpower":
            superpower(self,other)
        elif use=="Assurance":
            assurance(self,other)
        elif use=="Rock Blast":
            miss=random.randint(1,100)
            if miss>90:
                print(f"{other.name} avoided the attack.")
            else:
                rockblast(self,other)
        elif use=="Cross Poison":
            crosspoison(self,other)
        elif use=="Solar Beam":
            solarbeam(self,other)
        elif use=="Sludge Bomb":
            sludgebomb(self,other)
        elif use=="Close Combat":
            closecombat(self,other)
        elif use=="Brave Bird":
            bravebird(self,other)
        elif use=="Body Slam":
            bodyslam(self,other)
        elif use=="Dynamic Punch":
            dynapunch(self,other)
        elif use=="Liquidation":
            liquidation(self,other)
        elif use=="Tera Blast":
            terablast(self,other)
        elif use=="Earthquake":
            earthquake(self,other)
        elif use=="Fire Blast":
            miss=random.randint(1,100)
            if miss>85:
                print(f"{other.name} avoided the attack.")
            else:
                fireBlast(self,other)
        elif use=="Psychic":
            psychic(self,other)
        elif use=="Thunderbolt":
            tbolt(self,other)
        elif use=="Poison Jab":
            poisonjab(self,other)
        elif use=="Ice Beam":
            icebeam(self,other)
        elif use=="Moon Blast":
            moonblast(self,other)
        elif use=="Hydro Pump":
            miss=random.randint(1,100)
            if miss>80:
                print(f"{other.name} avoided the attack.")
            else:
                hydropump(self,other)
        elif use=="Earth Power":
            earthpower(self,other)
        elif use=="Giga Drain":
            gigadrain(self,other)
        elif use=="Hidden Power":
            hiddenpower(self,other)
        elif use =="Hydro Vortex":
            self.name=self.name.split("(")[0]
            print(f"{self.name} reacting to {tr.name}'s Waterium Z.")
            hydrovortex(self,other)
            self.moves.remove(use)
        elif use =="Pulverizing Pancake":
            self.name=self.name.split("(")[0]
            print(f"{self.name} reacting to {tr.name}'s Snorlium Z.")
            pulverizingpancake(self,other)
            self.moves.remove(use)
        elif use =="Inferno Overdrive":
            self.name=self.name.split("(")[0]
            print(f"{self.name} reacting to {tr.name}'s Firium Z.")
            infernooverdrive(self,other)
            self.moves.remove(use)
        elif use =="Bloom Doom":
            self.name=self.name.split("(")[0]
            print(f"{self.name} reacting to {tr.name}'s Grassium Z.")
            bloomdoom(self,other)
            self.moves.remove(use)
        elif use =="Gigavolt Havoc":
            self.name=self.name.split("(")[0]
            print(f"{self.name} reacting to {tr.name}'s Electrium Z.")
            gigavolthavoc(self,other)
            self.moves.remove(use)
        elif use =="Acid Downpour":
            self.name=self.name.split("(")[0]
            print(f"{self.name} reacting to {tr.name}'s Poisonium Z.")
            aciddownpour(self,other)
            self.moves.remove(use)
        elif use =="Breakneck Blitz":
            self.name=self.name.split("(")[0]
            print(f"{self.name} reacting to {tr.name}'s Normalium Z.")
            breakneckblitz(self,other)
            self.moves.remove(use)
        elif use =="All-Out Pummeling":
            self.name=self.name.split("(")[0]
            print(f"{self.name} reacting to {tr.name}'s Fightinium Z.")
            alloutpummeling(self,other)
            self.moves.remove(use)
        elif use =="Black Hole Eclipse":
            self.name=self.name.split("(")[0]
            print(f"{self.name} reacting to {tr.name}'s Darkinium Z.")
            blackholeeclipse(self,other)
            self.moves.remove(use)
        elif use =="Continental Crush":
            self.name=self.name.split("(")[0]
            print(f"{self.name} reacting to {tr.name}'s Rockium Z.")
            continentalcrush(self,other)
            self.moves.remove(use)
        elif use =="Tectonic Rage":
            self.name=self.name.split("(")[0]
            print(f"{self.name} reacting to {tr.name}'s Groundium Z.")
            tectonicrage(self,other)
            self.moves.remove(use)
        elif use =="Corkscrew Crash":
            self.name=self.name.split("(")[0]
            print(f"{self.name} reacting to {tr.name}'s Steelium Z.")
            corkscrewcrash(self,other)
            self.moves.remove(use)
        elif use =="Devastating Drake":
            self.name=self.name.split("(")[0]
            print(f"{self.name} reacting to {tr.name}'s Dragonium Z.")
            devastatingdrake(self,other)
            self.moves.remove(use)
        elif use =="Shattered Psyche":
            self.name=self.name.split("(")[0]
            print(f"{self.name} reacting to {tr.name}'s Psychium Z.")
            shatteredpsyche(self,other)
            self.moves.remove(use)
        elif use =="Never-ending Nightmare":
            self.name=self.name.split("(")[0]
            print(f"{self.name} reacting to {tr.name}'s Ghostium Z.")
            neverendingnightmare(self,other)
            self.moves.remove(use)
        elif use =="Supersonic Skystrike":
            self.name=self.name.split("(")[0]
            print(f"{self.name} reacting to {tr.name}'s Flyinium Z.")
            supersonicskystrike(self,other)
            self.moves.remove(use)
        elif use =="Savage Spin-Out":
            self.name=self.name.split("(")[0]
            print(f"{self.name} reacting to {tr.name}'s Buginium Z.")
            savagespinout(self,other)
            self.moves.remove(use)
        elif use =="Subzero Slammer":
            self.name=self.name.split("(")[0]
            print(f"{self.name} reacting to {tr.name}'s Icium Z.")
            subzeroslammer (self,other)
            self.moves.remove(use)
        elif use =="Twinkle Tackle":
            self.name=self.name.split("(")[0]
            print(f"{self.name} reacting to {tr.name}'s Fairium Z.")
            twinkletackle(self,other)
            self.moves.remove(use)
        else:
            print(f"{use} isn't defined yet.")
    #if other.hp<0:
#        other.hp=0
    if multiscale==True and other.hp<other.maxhp:
        self.atk=self.maxatk
        self.spatk=self.maxspatk
        multiscale=False    
    if self.status=="Poisoned" and self.ability not in ["Magic Guard","Poison Heal"]:
        self.hp-=round(self.maxhp/16)
        print(f"{self.name} was hurt by poison.")
    if self.status=="Burned" and self.ability!="Magic Guard":
        self.hp-=round(self.maxhp/16)
        print(f"{self.name} was hurt by burn.")
    if self.status=="Badly Poisoned" and self.ability not in ["Magic Guard","Poison Heal"]:
        self.hp-=(self.maxhp*self.badpoison/16)
        self.badpoison+=1
        print(f"{self.name} was hurt by poison.")
    if (Pokemon.weather =="Sandstorm" or Pokemon2.weather=="Sandstorm"):
        if self.type1 not in ["Rock","Ground","Steel"] and self.type2 not in ["Rock","Ground","Steel"] and self.ability!="Magic Guard":
            self.hp-=round(self.maxhp/16)
            print(f"{self.name} got pelted by sandstorm.")
    if (Pokemon.weather =="Hail" or Pokemon2.weather=="Hail"):     
        if self.type1!="Ice" and self.type2!="Ice" and self.ability!="Magic Guard":
            self.hp-=round(self.maxhp/16)
            print(f"{self.name} got pelted by hail.")
    if self.seeded==True:
        self.hp-=round(self.maxhp/16)
        if other.hp<=(other.maxhp-other.maxhp/16):
            other.hp+=round(other.maxhp/16)
    per=round(((before-other.hp)/other.maxhp)*100,2)
    sper=round(((sbefore-self.hp)/self.maxhp)*100,2)
    if other.hp<0:
        per=round((before/other.maxhp)*100,2)
    if self.hp<0:
        sper=round((sbefore/self.maxhp)*100,2)
    if other.hp!=before and per>0:
        print(f"Total damage dealt {per}%")
    if other.hp!=before and per<0:
        print(f"{other.name}' health regained {-per}%")
    if self.hp!=sbefore and self==me and sper<0:
        print(f"Total health regained {-sper}%")
    if self.hp!=sbefore and self==me and sper>0:
        print(f"Total damage received {sper}%")
    return self

#attack(t1.pokemons[0],t2.pokemons[0]) 
