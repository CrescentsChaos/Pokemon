from trainerlist import *
from moves import *
from AItest import *
healingmoves=["Recover","Roost","Synthesis","Morning Sun","Moonlight","Slack Off","Soft-Boiled","Milk Drink","Rest","Lunar Blessing"]
allmove=["Double Edge","Return","Body Slam","Boomburst","Crush Claw","Crush Grip","Dizzy Punch","Egg Bomb","Explosion","Extreme Speed","Hyper Voice","Facade","Multi-Attack","Strength","Hyper Beam","Giga Impact","Relic Song","Techno Blast","Weather Ball","Breakneck Blitz","Skull Bash","Fire Blast","Flare Blitz","Flamethrower","Magma Storm","Eruption","Lava Plume","Fire Punch","Blaze Kick","Fire Fang","Fire Lash","Heat Crash","Pyro Ball","Raging Fury","Sacred Fire","V-create","Blast Burn","Blue Flare","Fiery Dance","Fusion Flare","Heat Wave","Inferno","Mystical Fire","Searing Shot","Inferno Overdrive","Armor Cannon","Bitter Blade","Hydro Pump","Surf","Liquidation","Flip Turn","Hydro Cannon","Muddy Water","Origin Pulse","Scald","Snipe Shot","Sparkling Aria","Steam Eruption","Waterfall","Water Spout","Aqua Jet","Crabhammer","Fishious Rend","Razor Shell","Surging Strikes","Water Shuriken","Wave Crash","Hydro Vortex","Aqua Tail","Thunderbolt","Thunder","Volt Switch","Aura Wheel","Bolt Beak","Bolt Strike","Fusion Bolt","Plasma Fists","Thunder Fang","Thunder Punch","Volt Tackle","Electro Ball","Electroweb","Zap Cannon","Gigavolt Havoc","Wild Charge","Overdrive","Earthquake","Earth Power","Scorching Sands","Sandsear Storm","Bone Rush","Drill Run","Headlong Rush","High Horsepower","Land's Wrath","Precipice Baldes","Stomping Tantrum","Thousand Arrows","Thousand Waves","Tectonic Rage","Magnitude","Bulldoze","Ice Beam","Blizzard","Icicle Crash","Freeze Shock","Ice Fang","Ice Punch","Ice Shard","Icicle Spear","Mountain Gale","Freeze Dry","Frost Breath","Ice Burn","Subzero Slammer","Glacial Lance","Superpower","Close Combat","High Jump Kick","Aura Sphere","Final Gambit","Focus Blast","Secret Sword","Arm Thrust","Body Press","Brick Break","Drain Punch","Mach Punch","Dynamic Punch","Flying Press","Force Palm","Hammer Arm","Power-up Punch","Sacred Sword","Seismic Toss","Sky Uppercutt","Triple Arrows","All-Out Pummeling","Meteor Assault","Submission","Psychic","Extrasensory","Psychic Fangs","Psycho Cut","Psyshield Bash","Zen Headbutt","Esper Wing","Luster Purge","Mist Ball","Psycho Boost","Psystrike","Stored Power","Shattered Psyche","Prismatic Laser","Expanding Force","Shadow Ball","Shadow Sneak","Shadow Claw","Spirit Shackle","Bitter Malice","Hex","Infernal Parade","Phantom Force","Shadow Force","Never-ending Nightmare","Moongeist Beam","Astral Barrage","Moonblast","Dazzling Gleam","Play Rough","Spirit Break","Light of Ruin","Twinkle Tackle","Spirit Break","Giga Drain","Leaf Blade","Chloroblast","Frenzy Plant","Energy Ball","Grass Knot","Leaf Storm","Leaf Tornado","Seed Flare","Solar Beam","Bullet Seed","Drum Beating","Grassy Glide","Horn Leech","Razor Leaf","Seed Bomb","Wood Hammer","Power Whip","Bloom Doom","Petal Dance","Apple Acid","Grav Apple","Stone Edge","Accelerock","Diamond Storm","Head Smash","Rock Blast","Rock Slide","Ancient Power","Power Gem","Splintered Stromshards","Continental Crush","Stone Axe","Meteor Beam","Rock Wrecker","Dark Pulse","Night Slash","Crunch","Night Daze","Snarl","Assurance","Ceaseless Edge","Darkest Lariat","Throat Chop","Foul Play","Knock Off","Hyperspace Fury","Sucker Punch","Wicked Blow","Black Hole Eclipse","False Surrender","Draco Meteor","Dragon Pulse","Dragon Claw","Outrage","Core Enforcer","Roar of Time","Special Rend","Devastating Drake","Dragon Energy","Breaking Swipe","Dual Chop","Dragon Darts","Megahorn","Pin Missile","Bug Buzz","U-Turn","X-Scissor","Leech Life","Savage Spin-Out","Poison Jab","Sludge Bomb","Cross Poison","Sludge Wave","Dire Claw","Gunk Shot","Belch","Poison Fang","Poison Tail","Venoshock","Acid Downpour","Flash Cannon","Meteor Mash","Bullet Punch","Steel Beam","Doom Desire","Gyro Ball","Heavy Slam","Iron Head","Iron Tail","Steel Wing","Corkscrew Crash","Sunsteel Strike","Brave Bird","Sky Attack","Acrobatics","Beak Blast","Dragon Ascent","Drill Peck","Dual Wingbeat","Supersonic Skystrike","Aeroblast","Hurricane","Oblivion Wing","Air Slash","Recover","Roost","Synthesis","Morning Sun","Moonlight","Slack Off","Soft-Boiled","Milk Drink","Rest","Lunar Blessing","Sleep Powder","Iron Defense","Calm Mind","Swords Dance","Bulk Up","Recover","Roost","Thunder Wave","Lunar Blessing","Take Heart","Heart Swap","Will-O-Wisp","Moonlight","Synthesis","Morning Sun","Rain Dance","Sunny Day","Hail","Sandstorm","Dark Void","Trick Room","Nasty Plot","Shell Smash","Dragon Dance","Belly Drum","Spore","Hypnosis","Rest","Coil","Curse","Strength Sap","Leech Seed","Protect","Autotomize","King's Shield","Protect","Spiky Shield"]
zmoves=["Breakneck Blitz","Inferno Overdrive","Gigavolt Havoc","Bloom Doom","Hydro Vortex","Shattered Psyche","Never-ending Nightmare","Tectonic Rage","Continental Crush","Twinkle Tackle","Acid Downpour","Black Hole Eclipse","Supersonic Skystrike","Savage Spin-Out","Corkscrew Crash","All-Out Pummeling","Subzero Slammer","Devastating Drake","10,000,000 Volt Thunderbolt","Catastropika","Pulverizing Pancake","Genesis Supernova"]
statusmove=["Sleep Powder","Iron Defense","Calm Mind","Swords Dance","Bulk Up","Recover","Roost","Thunder Wave","Lunar Blessing","Take Heart","Heart Swap","Will-O-Wisp","Moonlight","Synthesis","Morning Sun","Rain Dance","Sunny Day","Hail","Sandstorm","Dark Void","Trick Room","Nasty Plot","Shell Smash","Dragon Dance","Belly Drum","Spore","Hypnosis","Rest","Coil","Curse","Strength Sap","Leech Seed","Protect","Spiky Shield","King's Shield","Heal Order","Defend Order","Light Screen","Reflect","Defog","Tailwind","Aurora Veil","Tailwind"]
buffmove=["Iron Defense","Calm Mind","Swords Dance","Shell Smash","Bulk Up","Recover","Roost","Moonlight","Morning Sun","Synthesis","Hail","Rain Dance","Sunny Day","Sandstorm","Trickroom","Dragon Dance","Belly Drum","Nasty Plot","Rest","Coil","Curse","Explosion","Heal Order","Defend Order", "Protect","Spiky Shield","Quiver Dance","Cosmic Power","Light Screen","Reflect","Tailwind"]
contactmoves=["Fire Punch","Ice Punch","Thunder Punch","Horn Drill","Body Slam","Double-Edge","Drill Peck","Submission","Seismic Toss","Strength","Petal Dance","Waterfall","Skull Bash","High Jump Kick","Dizzy Punch","Leech Life","Crabhammer","Slash","Triple Kick","Mach Punch","Outrage","Steel Wing","Return","Dynamic Punch","Megahorn","Rapid Spin","Iron Tail","Cross Chop","Crunch","Extreme Speed","Fake Out","Facade","Superpower","Brick Break","Knock Off","Arm Thrust","Blaze Kick","Needle Arm","Poison Fang","Crush Claw","Meteor Mash","Shadow Punch","Sky Uppercut","Dragon Claw","Poison Tail","Volt Tackle","Leaf Blade","Hammer Arm","Gyro Ball","U-Turn","Close Combat","Assurance","Last Resort","Sucker Punch","Flare Blitz","Force Palm","Poison Jab","Night Slash","Aqua Tail","X-Scissor","Dragon Rush","Drain Punch","Brave Bird","Giga Impact","Bullet Punch","Avalanche","Shadow Claw","Thunder Fang","Ice Fang","Fire Fang","Psychic Fangs","Shadow Sneak","Zen Headbutt","Power Whip","Cross Poison","Iron Head","Grass Knot","Wood Hammer","Aqua Jet","Head Smash","Crash Grip","Shadow Force","Heavy Slam","Foul Play","Acrobatics","Dragon Tail","Wild Charge","Drill Run","Dual Chop","Horn Leech","Sacred Sword","Razor Shell","Heat Crash","Head Charge","Gear Grind","Bolt Strike","V-create","Flying Press","Fell Stinger","Phantom Force","Draining Kiss","Play Rough","Nuzzle","Power-Up Punch","Dragon Ascent","First Impression","Darkest Lariat","Ice Hammer","High Horsepower","Solar Blade","Throat Chop","Anchor Shot","Lunge","Fire Lash","Smart Strike","Trop Kick","Dragon Hanmer","Stomping Tantrum","Accelerock","Liquidation","Spectral Thief","Sunsteel Strike","Zing Zap","Multi-Attack","Plasma Fists","Jaw Lock","Bolt Beak","Double Iron Bash","Fishious Rend","Body Press","Behemoth Blade","Behemoth Bash","Breaking Swipe","Spirit Break","False Surrender","Grassy Glide","Skitter Smack","Flip Turn","Triple Axel","Dual Wingbeat","Wicked Blow","Surging Strikes","Thunderous Kick"]
priorityatkmoves=["Mach Punch","Bullet Punch","Sucker Punch","Fake Out","Extreme Speed","Aqua Jet","Shadow Sneak","Accelerock","Ice Shard","Water Shuriken"]
multimove=["Bullet Seed","Rock Blast","Pin Missile","Icicle Spear","Dual Chop","Dual Wingbeat","Arm Thrust","Water Shuriken"]
nondmgmove=statusmove+buffmove+["Stealth Rock","Toxic","Toxic Spikes","Sticky Web","Trick Room"]
premove=["Solar Beam","Meteor Beam","Skull Bash"]
maxmovelist=["Max Strike","Max Flare","G-Max Wildfire","G-Max Centiferno","Max Geyser","G-Max Cannonade","G-Max Hydrosnipe","G-Max Foam Burst","Max Lightning","G-Max Volt Crash","G-Max Stun Shock","Max Quake","Max Knuckle","G-Max Chi Strike","Max Mindstorm","Max Phantasm","G-Max Terror","Max Starfall","Max Overgrowth","G-Max Drum Solo","G-Max Sweetness","G-Max Tartness","Max Rockfall","Max Darkness","Max Wyrmwind","G-Max Depletion","Max Flutterby","G-Max Befuddle","Max Ooze","Max Steelspike","Max Airstream","G-Max Resonance","G-Max Hailstorm","G-Max Finale","G-Max Volcalith","G-Max Stonesurge","Max Hailstorm"]
def fchoice(pk,tr):
    if tr.ai is False:
        movelist(pk)
        choice=input(f" {tr.name}: Choose a move.\n >>")
        if choice in ["1","2","3","4","5","6"]:
            choice=int(choice)
        if pk.item is not None and  ("Choice" in pk.item or pk.ability=="Gorilla Tactics") and pk.choiced==False and pk.dmax==False:
            pk.choiced=True
            pk.choicedmove=int(choice)
        if len(pk.moves)==1:
            choice=1
        if choice not in [1,2,3,4,5,6]:
            if pk.dmax is False:
                choice=random.randint(1,len(pk.moves))
            if pk.dmax is True:
                choice=random.randint(1,len(pk.maxmove))
        #print("Chosen moves:",pk.moves[choice-1])
        if choice=="":
            choice(random.randint(1,len(pk.moves)))
        return choice
def switch(current,other,trainer,trainer2,field,turn):
    if trainer.ai is not True:
        showmon(trainer)
    if "Ditto" in current.name:
        current.ability="Imposter"
    current.atkb=1
    current.defb=1
    current.spatkb=1
    current.spdefb=1
    current.speedb=1
    current.yawn=False
    current.atk=current.maxatk
    current.speed=current.maxspeed
    current.spatk=current.maxspatk
    current.spdef=current.maxspdef
    current.defense=current.maxdef
    current.badpoison=1
    current.priority=False
    current.recharge=False
    current.seeded=False
    current.flinched=False
    current.protect=False
    other.protect=False
    current.shelltrap=False
    current.canfakeout=True
    current.choiced=False
    current.choicedmove=None
    if current.dmax is True:
        current.dmax=False
        current.name=current.name.split(" ")[-1]
        current.hp/=2
        current.maxhp/=2
        print(f" 🔻 {current.name} returned to it's normal state!")
    m=None
    switchable=[1,2,3,4,5,6]
    if current in trainer.pokemons:
        m=trainer.pokemons.index(current)
        swe=[0,1,2,3,4,5]
        swe.remove(m)
    if trainer.ai is not True:        
        n=(input(f" {trainer.name} Choose a Pokemon: "))
        if n=="info":
            n=(input(" Which pokemon you wanna see?"))
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
    
    if trainer.ai is True:
        #print("  Not Working")
        new=switchAI(current,other,trainer,trainer2,field)[0]
    if trainer.ai is False:  
        #print("  Working")
        new=trainer.pokemons[n-1]   
    if new==current:
   	    print(f" \n{current.name} is already in battle.")
   	    return switch(current,other,trainer,trainer2,field,turn)		
    if new!=current:
        withdaweff(current,trainer,other)
        pkreturn(trainer,current)
        current=new
        phase2=random.choice(["It's our show time.","Show your strength.","Let's do it buddy.","I believe in you!","Let's finish this off.","Are you ready buddy?","Let's show them what you are capable of.","You know what to do."])
        print(f" Go {current.name}! "+phase2)
        entryeff(current,other,trainer,trainer2,field,turn)
        return current
    else:
        return current
#return text
def pkreturn(tr,mon):
    if "Red" in tr.name:
        print(f" {tr.name}: ........")
    if "Giovanni" in tr.name and mon.name=="Mewtwo":
        print(f" {tr.name}: WHAT! This cannot be!")
    else:
        phase1=random.choice([" return! You did well buddy."," return! You disappointed me."," return! Pathetic Pokémon."," return! Take rest my friend."," return! You were strong as always."," return! Maybe next time."])
        print(f"\n {tr.name}: "+mon.name+phase1)
#WITHDRAW EFFECTS
def withdaweff(current,trainer,other):
    if current.ability=="Zero to Hero" and "Hero" not in current.name:
        print(f" {current.name}'s {current.ability}!")
        current.name="Hero Palafin"
        current.hp=100
        current.atk=160
        current.defense=97
        current.spatk=106
        current.spdef=87
        current.speed=100
        current.calcst()
    if current.ability=="Natural Cure" and (current.status!="Alive" and current.status!="Fainted"):
        print(f" {current.name}'s {current.ability}.")
        current.status="Alive"
    if current.ability=="Illusion":
        current.name=random.choice(["Raikou","Entei","Suicune","Primape","Machamp","Nihilego","Gengar","Toxicroak"])
    if current.ability=="Regenerator" and 0<current.hp<current.maxhp and current.status!="Fainted":
        print(f" {current.name}'s {current.ability}.")
        if current.hp<=(current.maxhp/3):
            current.hp+=round(current.maxhp/3)
        elif current.hp>(current.maxhp/3):
            current.hp=current.maxhp
#ENTRY EFFECTS            
def entryeff(current,other,trainer,trainer2,field,turn):
    prebuff(current,other,trainer,turn,field)
    current.maxendturn(turn)
    print("")
    if "Legendary" in current.name and current.item in ["Silver Feather","Red Orb","Blue Orb","Jade Orb","Rainbow Feather"]:
        print(f" 🔱 {current.item} shrouded {current.name} with mystical energy!")
        current.hp*=6
        current.maxhp*=6
#        current.maxdef*=1.2
#        current.maxspdef*=1.2
#        current.maxatk*=1.2
#        current.maxspatk*=1.2
#        current.maxspeed*=1.2
    if current.ability=="Quark Drive" and (field.terrain=="Electric" or current.item=="Booster Energy"):
        print(f" ⚡ {current.name}'s {current.ability}!")
        if current.spatk>current.atk and current.spatkb==1:
            spatkchange (current,0.5)
        if current.atk>current.spatk and current.atkb==1:
            atkchange (current,0.5)        
    if current.ability=="Protosynthesis" and (field.weather in ["Sunny","Desolate Land"] or current.item=="Booster Energy"):
        print(f" ☀️ {current.name}'s {current.ability}!")
        if current.spatk>current.atk and current.spatkb==1:
            spatkchange (current,0.5)
        if current.atk>current.spatk and current.atkb==1:
            atkchange (current,0.5)
    if current.ability=="Supreme Overlord" and len(trainer.pokemons)<6:
        print(f" 👾{current.name}'s {current.ability}!")
        atkchange(current,0.5*(6-len(trainer.pokemons)))
        print(f" Attack x{current.atkb}")
        spatkchange(current,0.5*(6-len(trainer.pokemons)))
        print(f" Special Attack x{current.spatkb}")
    if current.megaintro is False and "Ultra " in current.name:
        prevname=current.name.split(" ")[-1]
    if current.megaintro is False and "Primal Kyogre" in current.name:
        prevname=current.name.split(" ")[-1]
        print(f" ⛎ {prevname}'s Primal Reversion! It reverted to its primal form!\n")
        current.primalintro=True
    if current.megaintro is False and "Primal Groudon" in current.name:
        prevname=current.name.split(" ")[-1]
        print(f" ♉ {prevname}'s Primal Reversion! It reverted to its primal form!\n")
        current.primalintro=True
    if current.megaintro is False and "Mega " in current.name and "Rayquaza" in current.name:
        prevname=current.name.split(" ")[-1]
        trname=trainer.name.split(" ")[-1]
        print(f" 🧬 {trname}'s fervent wish has reached {prevname}!\n {prevname} Mega evolved into {current.name}!\n")
    if current.megaintro is False and "💎" in current.name:
        typ=None
        if current.teratype=="Dragon":
            typ="🐲"
        if current.teratype=="Psychic":
            typ="👁️"
        if current.teratype=="Ghost":
            typ="👻"
        if current.teratype=="Normal":
            typ="🏳️"
        if current.teratype=="Bug":
            typ="🪲"
        if current.teratype=="Steel":
            typ="🔩"
        if current.teratype=="Ice":
            typ="🧊"
        if current.teratype=="Fighting":
            typ="👊🏽"
        if current.teratype=="Dark":
            typ="🌑"
        if current.teratype=="Fairy":
            typ="🧚🏻‍♂️"
        if current.teratype=="Flying":
            typ="🕊️"
        if current.teratype=="Poison":
            typ="☣️"
        if current.teratype=="Ground":
            typ="🌍"
        if current.teratype=="Rock":
            typ="🪨"
        if current.teratype=="Grass":
            typ="🌿"
        if current.teratype=="Electric":
            typ="⚡"
        if current.teratype=="Water":
            typ="💧"
        if current.teratype=="Fire":
            typ="🔥"
        name=current.name.split("💎")[0]
        print(f" {typ}{name} terastalized into {current.teratype}-type!")
        current.megaintro=True
    if current.megaintro is False and "Mega " in current.name and "Rayquaza" not in current.name:
        trname=trainer.name.split(" ")[-1]
        prevname=current.name.split(" ")[-1]
        if "Mewtwo" in current.name:
            prevname="Mewtwo"
        if "Charizard" in current.name:
            prevname="Charizard"
        print(f" 🧬 {prevname}'s {current.item} reacted to {trname}'s Keystone!\n {prevname} Mega evolved into {current.name}!\n")
        current.megaintro=True
    if current.dmax is True:
        prevname=current.name.split(" ")[-1]
        if "Dynamax" in current.name:
            print(f" 🔺{trainer.name} dynamaxed {prevname}!\n")
        if "Gigantamax" in current.name:
            print(f" 🔺{trainer.name} gigantamaxed {prevname}!\n")
    if current.ability=="Imposter" and other.dmax is False:
        print(f" 👾{current.name}'s {current.ability}!")
        print(f' {current.name} transformed into {other.name}!')
        current.hp=round(other.maxhp*(current.hp/current.maxhp))
        current.maxhp=other.maxhp
        current.maxatk=other.maxatk
        current.maxdef=other.maxdef
        current.maxspatk=other.maxspatk
        current.maxspdef=other.maxspdef
        current.maxspeed=other.maxspeed    
        current.atk=other.atk
        current.defense=other.defense
        current.spatk=other.spatk
        current.spdef=other.spdef
        current.speed=other.speed    
        current.atkb=other.atkb
        current.defb=other.defb
        current.spatkb=other.spatkb
        current.spdefb=other.spdefb
        current.speedb=other.speedb
        current.moves=other.moves
        current.type1=other.type1
        current.type2=other.type2
        current.ability=other.ability
        current.name=current.name+f"({other.name})"
    if current.ability == "Delta Stream" :
        field.weather=="Strong Wind"
    if current.ability == "Sand Stream" and field.weather not in ["Sandstorm","Primordial Sea","Desolate Land"]:
        print(f" 🏜️{current.name}'s {current.ability} whipped up a sandstorm!")
        field.weather="Sandstorm" 
        field.sandturn=turn
        field.sandend(current,other)
    if current.ability=="Primordial Sea" and field.weather!="Primordial Sea" and field.weather!="Primordial Sea":
        print(f" 🌊{current.name}'s {current.ability}. A heavy rain began to fall!")
        field.weather="Primordial Sea"
    if current.ability=="Desolate Land" and field.weather!="Desolate Land":
        print(f" 🌋{current.name}'s {current.ability}. The sunlight turned extremely harsh!")
        field.weather="Desolate Land"
    if current.ability in  ["Drought","Orichalcum Pulse"] and field.weather not in ["Sunny","Primordial Sea","Desolate Land"]:
        print(f" ☀️{current.name}'s {current.ability} intensified the sun's rays!")
        field.weather="Sunny"
        field.sunturn=turn
        field.sunend(current,other)
    if current.ability == "Drizzle" and field.weather not in ["Rainy","Primordial Sea","Desolate Land"]:
        print(f" 🌧️{current.name}'s {current.ability} made it rain!")
        field.weather="Rainy"
        field.rainturn=turn
        field.rainend(current,other)
    if current.ability == "Snow Warning" and field.weather not in ["Hail","Primordial Sea","Desolate Land"]:
        print(f" 🌨️{current.name}'s {current.ability} whipped up a snowstorm!")
        field.weather="Snowstorm"      
        field.snowstormturn=turn
        field.snowstormend(current,other) 
    if current.ability=="Download":
        print(f" {current.name}'s {current.ability}.")
        if other.spdef<other.defense:
            spatkchange(current,0.5)
        if other.defense<=other.spdef:
            atkchange(current,0.5)
    if current.ability=="Intrepid Sword":
        print(f" {current.name}'s {current.ability}")
        atkchange(current,0.5)
        print(f" Attack x{current.atkb}")
    if current.ability=="Dauntless Shield":
        print(f" {current.name}'s {current.ability}")
        defchange(current,0.5)
        print(f" Defense x{current.defb}")
    if current.ability in ["Electric Surge","Hadron Engine"]:
        print(f" {current.name}'s {current.ability}!")
        print(" ⚡ An electric current ran across the battlefield!")
        field.terrain="Electric"
        field.eleturn=turn
        field.eleend(current,other)
    if current.ability=="Misty Surge":
        print(f" {current.name}'s {current.ability}!")
        print(" 🌸 Mist swirled around the battlefield!")
        field.terrain="Misty"
        field.misturn=turn
        field.misend(current,other)
    if current.ability=="Grassy Surge":
        print(f" {current.name}'s {current.ability}!")
        print(" 🌿 Grass grew to cover the battlefield!")
        field.terrain="Grassy"
        field.grassturn=turn
        field.grassend(current,other)
    if current.ability=="Psychic Surge":
        print(f" {current.name}'s {current.ability}!")
        print(" 👁️ The battlefield got weird!")
        field.terrain="Psychic"        
        field.psyturn=turn
        field.psyend(current,other)        
    if "Toxic Spikes" in trainer.hazard:
        if current.type1 in ["Poison"] or current.type2 in ["Poison"]:
            trainer.hazard.remove("Toxic Spikes")
            print(f" {current.name} absorbed the Toxic Spikes!")
        if current.type1 not in ["Poison","Steel"] and current.type2 not in ["Poison","Steel"] and current.ability not in ["Magic Guard","Levitate","Shield Dust"] and current.item!="Heavy-Duty Boots":
            current.status="Badly Poisoned"
            print(f" {current.name} was poisoned by Toxic Spikes.")
    if "Sticky Web" in trainer.hazard and current.ability not in ["Levitate","Shield Dust"] and current.item!="Heavy-Duty Boots":       
        speedchange(current,-0.5)
        print(f" {current.name}'s speed was lowered.")
    if "Stealth Rock" in trainer.hazard and current.ability not in ["Magic Guard","Levitate","Shield Dust","Mountaineer"] and current.item!="Heavy-Duty Boots":
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
        current.hp-=(1+(current.maxhp*0.0625*buff))
        print(f" 🪨 Pointed stones dug into {current.name}!")
#INTIMIDATE        
    if current.ability=="Intimidate" and other.ability not in ["Inner Focus","Oblivious","Clear Body"]:
        if other.ability!="Guard Dog":
            atkchange(other,-0.5)
            print(f" {current.name}'s {current.ability}!")
            print(f" {other.name}'s attack was lowered.") 
        if other.ability=="Guard Dog":
            atkchange(other,0.5)
            print(f" {current.name}'s {current.ability}!")
            print(f" {other.name}'s {other.ability}!")
            print(f" {other.name}'s attack was raised.") 
        if other.item=="Adrenaline Orb":
            speedchange(other,0.5)
            print(f" {other.name}'s speed was raised by the Adrenaline Orb.") 
#Stance Change        
def stancechange(self,used):    
    if used not in statusmove and self.ability=="Stance Change" and self.sword!=True:
        self.shield=False
        self.sword=True
        print(f" {self.name}'s {self.ability}!")
        print(" Aegislash changed to it's blade forme.")
        self.name="Aegislash(Blade)"        
        self.atk,self.spatk,self.defense,self.spdef=self.defense,self.spdef,self.atk,self.spatk
        self.maxatk,self.maxspatk,self.maxdef,self.maxspdef=self.maxdef,self.maxspdef,self.maxatk,self.maxspatk
    if used in statusmove and self.ability=="Stance Change" and self.shield!=True:
        self.shield=True
        self.sword=False
        print(f" {self.name}'s {self.ability}!")
        print(" Aegislash changed to it's shield forme.")
        self.name="Aegislash(Shield)"        
        self.atk,self.spatk,self.defense,self.spdef=self.defense,self.spdef,self.atk,self.spatk
        self.maxatk,self.maxspatk,self.maxdef,self.maxspdef=self.maxdef,self.maxspdef,self.maxatk,self.maxspatk
 #PREATTACK       
def preattackcheck(self,other,tr,optr,use,opuse,field,turn):
    if self.status=="Sleep":
        self.yawn=False
    if self.yawn is not True and self.yawn=="Sleep":
        self.status="Sleep"
        print(f" {self.name} fell asleep!")
    if self.yawn is True:
        self.yawn="Sleep"
    if self.status!="Alive" and self.ability in ["Purifying Salt","Good as Gold"]:
        print(f" {self.name}'s {self.ability}!")
        self.status="Alive"    
    if self.item=="Throat Spray" and use in ["Hyper Voice","Boomburst","Overdrive","Clanging Scales"]:
        spatkchange(self,0.5)
        print(f" {self.name}'s Special Attack rose!")
    if self.ability=="Mold Breaker":
        print(f" {self.name} breaks the mold!")
    if field.terrain=="Electric":
        if self.ability not in ["Levitate"] and self.type1!="Flying" and self.type2!="Flying" and self.status=="Sleep":
            self.status="Alive"
    if field.terrain=="Misty":
        if self.ability not in ["Levitate"] and self.type1!="Flying" and self.type2!="Flying":
            self.status="Alive"
    if self.ability=="Trace":
            print(f" {self.name}'s {self.ability}!")        
            self.ability=other.ability
            entryeff(self,other,tr,optr,field,turn)
    if self.ability=="Speed Boost":
            print(f" {self.name}'s {self.ability}!")
            print(f" {self.name}'s speed rose.")
            speedchange(self,0.5)
            
    if self.ability=="Limber" and self.status=="Paralyzed":
        print(f" {self.ability} cured {self.name}'s paralysis!")
        self.status="Alive"
    if other.ability=="Stench" and self.ability!="Long Reach":
        ch=random.randint(1,100)  
        if ch>90:
            print(f" {other.name}'s {other.ability}!")
            self.flinched=True   
    if self.item=="King's Rock":
        ch=random.randint(1,100)
        if ch>90 and other.ability not in ["Inner Focus"]:
            other.flinched=True
    
    pass
#ATTACK
def attack(self,other,tr,optr,use,opuse,field,turn):
    print(f"\n {tr.name}:")
    if other.ability=="Ice Face" and other.abilityused==False and use not in statusmove+buffmove:
        print(f" {other.name}'s {other.ability}!")
        other.abilityused=True
        other.maxdef=round(other.maxdef/1.57)
        other.maxspdef=round(other.maxspdef/1.8)
        other.maxspeed=round(other.maxspeed*2.6)
    if other.ability=="Disguise" and other.abilityused==False and use not in statusmove+buffmove:
        print(f" {self.name} used {use}!")
        print(f" {other.name}'s {other.ability}!")     
        other.hp-=round(other.maxhp*0.0625)
        other.abilityused=True
        use=None
    if use in healingmoves:
        self.healcount+=1
        if self.healcount==16 and use in healingmoves:
            self.moves.remove(use)
    if use!="Destiny Bond" and "Destiny Bond" in self.moves:
        other.dbond=False
    if opuse in statusmove and use=="Protect":
        use=None
        print("It failed!")
    moves=["Struggle"]
    if self.dmax is False:
        moves=self.moves
    if self.dmax is True:
        #print(self.maxmove)
        moves=self.maxmove
    used=use
#    print(used)
    hit=1
    me=self
    canatk=True
    stancechange(self,used)
    preattackcheck(self,other,tr,optr,use,opuse,field,turn)
    #if self.choiced==True and self.choicedmove is not None and self.dmax is False:
#        used=self.choicedmove
    if used=="Metronome":
        print(f" {self.name} used Metronome!")
        used=random.choice(allmove)
        print(f" Metronome turned into {used}!")
    if self.precharge==True:
        used=list(set(self.moves).intersection(premove))[0]
    if field.terrain=="Psychic":
        if used in priorityatkmoves:
            used=None
            print("  🚳 Cannot use priority moves in psychic terrain!")
    if self.ability!="Oblivious":
        if self.confused is True:
            print(f" 😵‍💫 {self.name} is confused!")
            ch=random.randint(1,100)
            if ch<40:
                print(f" ‼️ {self.name} snapped out of confusion!")
                self.confused=False        
            if ch>67:
                canatk=False
                used=None
                print(f" 😵  It hurt itself in confusion.")
                r=randroll()
                self.hp-=physical(self.level,self.atk,other.defense,40,a=1,r=r)
            else:
                canatk=True
    if self.status=="Paralyzed":
        ch=random.randint(1,100)
        if ch>75:
            canatk=False
            used=None
            print(f" ⚡ {self.name} is paralyzed and unable to move.")
        else:
            canatk=True
    if self.status=="Sleep":
        ch=random.randint(1,3)
        if ch==3:
            print(f" ‼️ {self.name} woke up!")
            self.status="Alive"
        else:
            print(f" 💤 {self.name} is fast asleep!")
            used=None
    if self.status=="Frozen":
        ch=random.randint(1,5)
        if ch==3:
            print(f" ‼️ {self.name} thawed out.")
            self.status="Alive"
        else:
            print(f" 🧊 {self.name} is frozen solid.")
            used=None
    before=other.hp
    sbefore=self.hp
    if self.ability=="Truant":
        if self.truant==True and "Slack Off" in self.moves:
            used="Slack Off"
            self.truant=False
        if self.truant==True and "Slack Off" not in self.moves:
            print(f" {self.name} is loafing around!")
            used=None
            self.truant=False
        else:
            self.truant=True
    if self.ability=="Hustle":
        ch=random.randint(1,self.accuracy)
        if ch<20:
            print(f" {self.name}'s {self.ability}.")
            print(f" {self.name} used {used}!")
            print(f" {other.name} avoided the attack({used}).")
            used=None
#SNOW CLOAK
    if other.ability=="Snow Cloak" and field.weather in ["Hail","Snow Cloak"]:
        ch=random.randint(1,self.accuracy)
        if ch<25:
            print(f" {other.name}'s {other.ability}.")
            print(f" {self.name} used {used}!")
            print(f" {other.name} avoided the attack({used}).")
            used=None
#SAND VEIL            
    if other.ability=="Sand Veil" and field.weather=="Sandstorm":
        ch=random.randint(1,self.accuracy)
        if ch<25:
            print(f" {other.name}'s {other.ability}.")
            print(f" {self.name} used {used}!")
            print(f" {other.name} avoided the attack({used}).")
            used=None
#######            
    if used in moves or used not in moves:
#        print(used)
        if self.taunted==True:
            while True:
                print(f" Cannot use non-damaging moves while taunted.")
                new=fchoice(self,tr)
                if new is None:
                    used="Struggle"
                used=self.moves[new-1]
                if used not in statusmove:
                    break
        if self.item=="Assault Vest" and used in statusmove:
            while True:
                print(f" Cannot use status moves while holding an Assault Vest.")
                new=fchoice(self,tr)
                if self.dmax is False:
                    used=moveAI(self,other,tr,optr,field)
                if self.dmax is True:
                    used=moveAI(self,other,tr,optr,field)
                if used not in statusmove:
                    break
        if used not in ["Protect","Spiky Shield","King's Shield","Baneful Bunker"]:
            self.protect=False
        elif used=="Lunar Blessing":
            lunarblessing(self)
            if self.status!="Alive":
                self.status="Alive"
                print(f" {self.name}'s status was cured.")
        elif used=="Take Heart":
            takeheart(self)
            if self.status!="Alive":
                self.status="Alive"
                print(f" {self.name}''s status was cured.")
        if self.precharge==True and "Geomancy" in self.moves:
            print(f" {self.name} used Geomancy!")
            spatkchange(self,1)     
            spdefchange(self,1)   
            speedchange(self,1)
            print(f" Special Attack x{self.spatkb}")   
            print(f" Special Defense x{self.spdefb}")   
            print(f" Speed x{self.speedb}")      
            self.precharge=False
        if self.recharge==True:
            print(f" {self.name} is recharging.")
            self.recharge=False
            used=None
        if self.flinched==True and self.dmax is False:
            print(f" {self.name} flinched.")
            self.flinched=False
            used=None
        elif self.protect=="Pending" and used in ["Protect","Spiky Shield","King's Shield","Baneful Bunker"]:
            print(f" 🛡️ {self.name} used {used}!")
            print("  It failed.")
            self.protect=False
            used=None
        elif other.protect==True and other.dmax is True and used not in buffmove and used not in ["G-Max One Blow","G-Max Rapid Flow"]:
            print(f" 🛡️ {other.name} protected itself from {self.name}'s {used}.")
            other.protect="Pending"
            used=None
            if used in ["Protect","Spiky Shield","King's Shield","Baneful Bunker"]:
                print(f" 🛡️ {self.name} used {used}!")
                print("  It failed!")
                used=None
        elif other.dmax is False and other.protect==True and used not in buffmove and (self.ability not in ["Infiltrator","Unseen Fist"]  and used not in ["Shadow Force","Phantom Force","Hyperspace Fury","Hyper Drill"] and used not in maxmovelist and used not in zmoves):
            print(f" 🛡️ {other.name} protected itself from {self.name}'s {used}.")
            other.protect="Pending"
            if used in ["Protect","Spiky Shield","King's Shield","Baneful Bunker","Max Guard"]:
                print(f" 🛡️ {self.name} used {used}!")
                print("  It failed!")
                used=None
                self.protect=False
            
            if "Spiky Shield" in other.moves and used in contactmoves:
                self.hp-=round(self.maxhp/8)
                print(f" {self.name} was hurt by Spiky Shield.") 
            if "Silk Trap" in other.moves and used in contactmoves:
                speedchange(self,-0.5)
                print(f" Speed x{self.atkb}")
            if "King's Shield" in other.moves and used in contactmoves:
                atkchange(self,-0.5)
                print(f" Attack x{self.atkb}")
            if "Baneful Bunker" in other.moves and used in contactmoves:
                if self.status=="Alive":
                    self.status=["Badly Poisoned"]   
                    print(f" ☠️ {self.name} was badly poisoned.")  
        elif used=="Toxic":
            miss=random.randint(1,self.accuracy)
            if miss<10:
                print(f" {other.name} avoided the attack({used}).")
            else:
                toxic(self,other)
        elif used=="Thunder Wave":
            miss=random.randint(1,self.accuracy)
            if miss<15 and (self.type1!="Electric" and self.type2!="Electric"):
                print(f" {other.name} avoided the attack({used}).")
            else:
                thunderwave(self,other)
        elif used=="Sucker Punch":
            if opuse in nondmgmove or opuse is None:
                print("  It failed.")
            else:
                suckerpunch(self,other)
        elif used=="Will-O-Wisp":
            miss=random.randint(1,self.accuracy)
            if miss<15 and (self.type1!="Fire" and self.type2!="Fire"):
                print(f" {other.name} avoided the attack({used}).")
            else:
                willowisp(self,other)        
        elif used=="Overdrive":
            overdrive(self,other) 
        elif used=="Kowtow Cleave":
            kowtowcleave(self,other) 
        elif used=="Ice Spinner":
            icespinner(self,other) 
        elif used=="Jaw Lock":
            jawlock(self,other)  
        elif used=="Torch Song":
            torchsong(self,other)      
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
        elif used=="Taunt":
            print(f"{self.name} used Taunt.")
            if other.taunted==True:
                print("It failed.")
            if other.taunted==False:
                other.taunted=True
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
        elif used=="Max Lightning":
            maxlightning(self,other,turn)
        elif used=="Max Overgrowth":
            maxovergrowth(self,other,turn)
        elif used=="Max Mindstorm":
            maxmindstorm(self,other,field,turn)
        elif used=="Gigaton Hammer":
            gigatonhammer(self,other)
        elif used=="Max Starfall":
            maxstarfall(self,other,field, turn)
        elif used=="Max Flare":
            maxflare(self,other,field,turn)
        elif used=="Max Hailstorm":
            maxhailstorm(self,other,field,turn)
        elif used=="Max Geyser":
            maxgeyser(self,other,field,turn)
        elif used=="Max Rockfall":
            maxrockfall(self,other,field,turn)
        elif used=="G-Max Snooze":
            gmaxsnooze(self,other)
        elif used=="G-Max Wind Rage":
            gmaxwindrage(self,other)
        elif used=="G-Max Vine Lash":
            gmaxvinelash(self,other)
        elif used=="G-Max Smite":
            gmaxsmite(self,other)
        elif used=="G-Max Steelsurge":
            gmaxsteelsurge(self,other)
        elif used=="Max Wyrmwind":
            maxwyrmwind(self,other)
        elif used=="G-Max Hydrosnipe":
            gmaxhydrosnipe(self,other)
        elif used=="G-Max One Blow":
            gmaxoneblow(self,other)
        elif used=="G-Max Rapid Flow":
            gmaxrapidflow(self,other)
        elif used=="Collision Course":
            collisioncourse(self,other)
        elif used=="Flower Trick":
            flowertrick(self,other)
        elif used=="Aqua Step":
            aquastep(self,other)
        elif used=="Last Respects":
            lastrespects(self,other,tr)
        elif used=="Chilling Water":
            chillingwater(self,other)
        elif used=="G-Max Terror":
            gmaxterror(self,other)
        elif used=="G-Max Volcalith":
            gmaxvolcalith(self,other)
        elif used=="G-Max Volt Crash":
            gmaxvoltcrash(self,other)
        elif used=="G-Max Stun Shock":
            gmaxstunshock(self,other)
        elif used=="G-Max Finale":
            gmaxfinale(self,other)
        elif used=="Max Flutterby":
            maxflutterby(self,other)
        elif used=="G-Max Befuddle":
            gmaxbefuddle(self,other)
        elif used=="Draining Kiss":
            drainingkiss(self,other)
        elif used=="Max Phantasm":
            maxphantasm(self,other)
        elif used=="G-Max Cannonade":
            gmaxcannonade(self,other)
        elif used=="G-Max Chi Strike":
            gmaxchistrike(self,other)
        elif used=="Cotton Guard":
            cottonguard(self)
        elif used=="Clangorous Soul":
            clangsoul(self)
        elif used=="G-Max Foam Burst":
            gmaxfoamburst(self,other)
        elif used=="G-Max Centiferno":
            gmaxcentiferno(self,other)
        elif used=="G-Max Depletion":
            gmaxdepletion(self,other)
        elif used=="G-Max Drum Solo":
            gmaxdrumsolo(self,other)
        elif used=="G-Max Replenish":
            gmaxreplenish(self,other)
        elif used=="G-Max Wildfire":
            gmaxwildfire(self,other)
        elif used=="Behemoth Bash":
            behemothbash(self,other)
        elif used=="Clangorous Scales":
            clangscale(self,other)
        elif used=="Parabolic Charge":
            parabolic(self,other)
        elif used=="Behemoth Blade":
            behemothblade(self,other)
        elif used=="Max Knuckle":
            maxknuckle(self,other)
        elif used=="Max Quake":
            maxquake(self,other)
        elif used=="Max Steelspike":
            maxsteelspike (self,other)
        elif used=="Max Darkness":
            maxdarkness(self,other)
        elif used=="Hyper Drill":
            hyperdrill(self,other)
        elif used=="Max Ooze":
            maxooze(self,other)
        elif used=="Max Strike":
            maxstrike(self,other)
        elif used=="Max Airstream":
            maxairstream(self,other)
        elif used=="Psyshock":
            psyshock(self,other)
        elif used=="Lumina Crash":
            luminacrash(self,other)
        elif used=="Mortal Spin":
            mortalspin(self,other)
        elif used=="Accelerock":
            accelerock(self,other)
        elif used=="Geomancy":
            geomancy(self,other)
        elif used=="Heavy Slam":
            heavyslam(self,other)
        elif used=="Heart Swap":
            heartswap(self,other)
        elif used=="Dragon Energy":
            dragonenergy(self,other)
        elif used=="Court Change":
            print(f" {self.name} used Court Change!")
            tr.hazard,optr.hazard=optr.hazard,tr.hazard
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
            raindance(self,other,field,turn)
            if other.ability=="Dancer":
                print(f" {other.name}'s {other.ability}!")
                raindance(other,self,field,turn)
        elif used=="Sunny Day":
            sunnyday(self,other,field,turn)
        elif used=="Leech Seed":
            leechseed(self,other)
        elif used=="Trick Room":
            trickroomm(self, other,turn)
        elif used=="Sandstorm":
            sandstorm(self,other,field,turn)
        elif used=="Shore Up":
            shoreup(self)
        elif used=="Electric Terrain":
            electricterrain(self,other,field,turn)
        elif used=="Misty Terrain":
            mistyterrain(self,other,field,turn)
        elif used=="Grassy Terrain":
            grassyterrain(self,other,field,turn)
        elif used=="Psychic Terrain":
            psychicterrain(self,other,field,turn)
        elif used=="Synthesis":
            synthesis(self)
        elif used=="Snowscape":
            snowscape(self,other,field,turn)
        elif used=="Hail":
            hail(self,other,field,turn)
        elif used=="Quiver Dance":
            quiverdance(self)
            if other.ability=="Dancer":
                print(f" {other.name}'s {other.ability}!")
                quiverdance(other)
        elif used=="Defend Order":
            defendorder(self)
        elif used=="Swords Dance":
            swordsdance(self)
            if other.ability=="Dancer":
                print(f" {other.name}'s {other.ability}!")
                swordsdance(other)
        elif used=="Nasty Plot":
            nastyplot(self)
        elif used=="Shell Smash":
            shellsmash(self)
        elif used=="Autotomize":
            autotomize(self)
        elif used=="Rapid Spin":
            rapidspin(self,other,tr)
        elif used=="Dragon Dance":
            dragondance(self)
            if other.ability=="Dancer":
                print(f" {other.name}'s {other.ability}!")
                dragondance(other)
        elif used=="Iron Defense":
            irondefense(self)
        elif used=="Bullet Punch":
            bulletpunch(self,other)
        elif used=="Flying Press":
            flyingpress(self,other)
        elif used=="X-Scissor":
            xscissor(self,other)
        elif used=="Drill Peck":
            drillpeck(self,other)
        elif used=="Triple Arrows)":
            for i in range(3):
                triplearrows(self,other)
        elif used=="Boomburst":
            boomburst(self,other)
        elif used=="Muddy Water":
            muddywater(self,other)
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
            print(f" {self.name} used defog.")
            print("  All the hazards blew away!")
            tr.hazard=[]
            optr.hazard=[]
            field.terrain="Normal"
            optr.lightscreen=False
            optr.reflect=False
            if field.terrain!="Normal":
                field.terrain="Normal"
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
        elif used=="Expanding Force":
            expandingforce(self,other)
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
        elif used=="Prismatic Laser":
             prismaticlaser(self,other)
             self.recharge=True
        elif used=="Sparkling Aria":
             sparklingaria(self,other)
        elif used=="Glaive Rush":
             glaiverush(self,other)
        elif used=="Glacial Lance":
             sparklingaria(self,other)
        elif used=="Astral Barrage":
             astralbarrage(self,other)
        elif used=="Darkest Lariat":
             darkestlariat(self,other)
        elif used=="Ceaseless Edge":
             ceaseless(self,other)
        elif used=="Mist Ball":
            mistball(self,other)
        elif used=="Aqua Cutter":
            aquacutter(self,other)
        elif used=="False Surrender":
            falsesurrender(self,other)
        elif used=="Ruination":
            ruination(self,other)
        elif used=="Electro Drift":
            electrodrift(self,other)
        elif used=="Spirit Break":
            spiritbreak(self,other)
        elif used=="Breaking Swipe":
            breakingswipe(self,other)
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
                print(f" {other.name}'s {other.ability}!")
                fierydance(other)
        elif used=="Leech Life":
            leechlife(self,other)
        elif used=="Freezing Glare)":
            freezingglare(self,other)
        elif used=="Skull Bash":
            skullbash(self,other)
        elif used=="Horn Leech":
            hornleech(self,other)
        elif used=="Flip Turn":
            flipturn(self,other)
            if len(tr.pokemons)>1 and (other.hp!=before):
                print(f" {self.name} returned to it's pokéball.")
                self=switch(self,other,tr,optr,field,turn)
        elif used=="Chilly Reception":
            chillyreception(self,other,field,turn)
            if len(tr.pokemons)>1:
                print(f" {self.name} returned to it's pokéball.")
                self=switch(self,other,tr,optr,field,turn)                        
        elif used=="U-Turn":
            uturn(self,other)
            if len(tr.pokemons)>1:
                print(f" {self.name} returned to it's pokéball.")
                self=switch(self,other,tr,optr,field,turn)
        elif used=="Parting Shot":
            partingshot(self,other)
            if len(tr.pokemons)>1:
                print(f" {self.name} returned to it's pokéball.")
                self=switch(self,other,tr,optr,field,turn)                
        elif used=="Volt Switch":
            voltswitch(self,other)
            if len(tr.pokemons)>1 and (other.hp!=before):
                print(f" {self.name} returned to it's pokéball.")
                self=switch(self,other,tr,optr,field,turn)
        elif used=="Extreme Speed":
            extemespeed(self,other)
        elif used=="Inferno":
            miss=random.randint(1,self.accuracy)
            if miss<50:
                print(f" {other.name} avoided the attack({used}).")
            else:
                inferno(self,other)
        elif used=="Overheat":
            miss=random.randint(1,self.accuracy)
            if miss<10:
                print(f" {other.name} avoided the attack({used}).")
            else:
                overheat(self,other)
        elif used=="Whirlwind":
            print(f" {self.name} usedd Whirlwind.")
            print(f" {other.name} blew away with the wind.")
            speedchange(other,-0.5)
            print(f" {other.name}: Speed x"+str(other.speedb))   
        elif used=="Return":
            retrn(self,other)
        elif used=="Sleep Powder":
            miss=random.randint(1,self.accuracy)
            if miss<25:
                print(f" {other.name} avoided the attack({used}).")
            else:
                sleeppowder(self,other)
        elif used=="Spore":
            spore(self,other)
        elif used=="Hypnosis":
            miss=random.randint(1,self.accuracy)
            if miss<40:
                print(f" {other.name} avoided the attack({used}).")
            else:
                hypnosis(self,other)
        elif used=="Dark Void":
            miss=random.randint(1,self.accuracy)
            if miss<20:
                print(f" {other.name} avoided the attack({used}).")
            else:
                darkvoid(self,other)
        elif used=="Body Press":
            bodypress(self,other)
        elif used=="Blizzard":
            if field.weather in ["Hail","Snowstorm"]:
                blizzard(self,other)
            if field.weather not in ["Hail","Snowstorm"]:
                miss=random.randint(1,self.accuracy)
                if miss<30:
                    print(f" {other.name} avoided the attack({used}).")
                elif miss>=30:
                    blizzard(self,other)
        elif used=="Air Slash":
            miss=random.randint(1,self.accuracy)
            if miss<5:
                print(f" {other.name} avoided the attack({used}).")
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
            if other.hp>0:
                self.recharge=True
        elif used=="Frenzy Plant":
            frenzyplant(self,other)
            if other.hp>0:
                self.recharge=True
        elif used=="Hydro Cannon":
            hydrocannon(self,other)
            if other.hp>0:
                self.recharge=True
        elif used=="Zap Cannon":
            miss=random.randint(1,self.accuracy)
            if miss<50:
                print(f" {other.name} avoided the attack({used}).")
            else:
                zapcannon(self,other)
        elif used=="Freeze-Dry":
            freezedry(self,other)
        elif used=="Ice Fang":
            icefang(self,other)
        elif used=="Coil":
            coil(self)
        elif used=="Dual Chop":
            for i in range(2):
                dualchop(self,other)
        elif used=="Dragon Darts":
            for i in range(2):
                dragondarts(self,other)
        elif used=="Dual Wingbeat":
            for i in range(2):
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
                print(f" {self.name}'s {self.ability}.")
                hit=5
            for i in range(hit):
                watershuriken(self,other)
            print(f" It hit {hit} time(s).")           
        elif used=="Double Iron Bash":
            for i in range(2):
                ironbash(self,other)
            print(f" It hit 2 time(s).")             
        elif used=="Bullet Seed":
            hit=random.randint(3,5)
            if self.ability=="Skill Link":
                print(f" {self.name}'s {self.ability}.")
                hit=5
            for i in range(hit):
                bulletseed(self,other)
            print(f" It hit {hit} time(s).")
        elif used=="Jet Punch":
            jetpunch(self,other)
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
        elif used=="Axe Kick":
            axekick(self,other)
        elif used=="High Jump Kick":
            hijumpkick(self,other)
        elif used=="Plasma Fists":
            plasmafists(self,other)
        elif used=="Blaze Kick":
            miss=random.randint(1,self.accuracy)
            if miss<10:
                print(f" {other.name} avoided the attack({used}).")
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
                miss=random.randint(1,self.accuracy)
                if miss<50:
                    print(f" {other.name} avoided the attack({used}).")
                elif miss>=50 or "No Guard" in (self.ability,other.ability):
                    hurricane(self,other)
            elif field.weather != "Rainy" and field.weather !="Rainy":
                miss=random.randint(1,self.accuracy)
                if miss<30:
                    print(f" {other.name} avoided the attack({used}).")
                elif miss>=30 or "No Guard" in (self.ability,other.ability):
                    hurricane(self,other)
          
        elif used=="Sky Uppercut":
            miss=random.randint(1,self.accuracy)
            if miss<10:
                print(f" {other.name} avoided the attack({used}).")
            else:
                skyuppercut(self,other)
        elif used=="Precipice Blades":
            miss=random.randint(1,self.accuracy)
            if miss<15:
                print(f" {other.name} avoided the attack({used}).")
            else:
                precipiceblades(self,other)
        elif used=="Origin Pulse":
            miss=random.randint(1,self.accuracy)
            if miss<15:
                print(f" {other.name} avoided the attack({used}).")
            else:
                originpulse(self,other)
        elif used=="Draco Meteor":
            miss=random.randint(1,self.accuracy)
            if miss<10:
                print(f" {other.name} avoided the attack({used}).")
            else:
                dracometeor(self,other)
        elif used=="Psycho Boost":
            miss=random.randint(1,self.accuracy)
            if miss<10:
                print(f" {other.name} avoided the attack({used}).")
            else:
                psychoboost(self,other)
        elif used=="Drill Run":
            miss=random.randint(1,self.accuracy)
            if miss<5:
                print(f" {other.name} avoided the attack({used}).")
            else:
                drillrun(self,other)
        elif used=="Head Smash":
            miss=random.randint(1,self.accuracy)
            if miss<15:
                print(f" {other.name} avoided the attack({used}).")
            else:
                headsmash(self,other)
        elif used=="Flash Cannon":
            flashcannon(self,other)
        elif used=="Toxic Spikes":
            if "Toxic Spikes" in optr.hazard:
                print(" Nothing happened!")
            if "Toxic Spikes" not in optr.hazard:
                print(f" {self.name} used "+colored("Toxic Spikes","magenta")+".")
                print(" ☠️ Poison spikes were scattered all around the opposing team!")
                optr.hazard.append("Toxic Spikes")
            else:
                print(" Nothing happened!")
        elif used=="Stealth Rock":
            if "Stealth Rock" in optr.hazard:
                print(" Nothing happened!")
            if "Stealth Rock" not in optr.hazard:
                print(f" {self.name} used Stealth Rock.")
                print(" 🪨 Pointed stones float in the air around the opposing team!")
                optr.hazard.append("Stealth Rock")
        elif used=="Sticky Web":
            if "Sticky Web" in optr.hazard:
                print(" Nothing happened!")
            if "Sticky Web" not in optr.hazard:
                print(f" {self.name} used Sticky Web.")
                print(" 🕸️ A sticky web spreads out in the ground around the opposing team!")
                optr.hazard.append("Sticky Web")            
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
                print("  It failed!")
            else:
                softboiled(self)
        elif used=="Heal Order":
            if self.hp==self.maxhp:
                print("  It failed!")
            else:
                healorder(self)
        elif used=="Slack Off":
            if self.hp==self.maxhp:
                print("  It failed!")
            else:
                slackoff(self)
        elif used=="Roost":
            if self.hp==self.maxhp:
                print("  It failed!")
            else:
                roost(self)
        elif used=="Recover":
            if self.hp==self.maxhp:
                print("  It failed!")
            else:
                recover(self)
            
        elif used=="Spiky Shield":
            self.protect=True
            print(f" {self.name} used Spiky Shield!")
        elif used=="Baneful Bunker":
            self.protect=True
            print(f" {self.name} used Baneful Bunker.")
        elif used=="Silk Trap":
            self.protect=True
            print(f" {self.name} used Silk Trap.")
        elif used=="Protect":
            self.protect=True
            print(f" {self.name} used Protect.")
        elif used=="Max Guard":
            self.protect=True
            print(f" 🔺 {self.name} used Max Guard.")            
        elif used=="King's Shield":
            self.protect=True
            print(f" {self.name} used King's Shield.")
        elif used=="Morning Sun":
            if self.hp==self.maxhp:
                print("  It failed!")
            else:
                morningsun(self)
        elif used=="Moonlight":
            if self.hp==self.maxhp:
                print("  It failed!")
            else:
                moonlight(self)
        elif used=="Megahorn":
            miss=random.randint(1,self.accuracy)
            if miss<15:
                print(f" {other.name} avoided the attack({used}).")
            else:
                megahorn(self,other)
        elif used=="Leaf Storm":
            miss=random.randint(1,self.accuracy)
            if miss<10:
                print(f" {other.name} avoided the attack({used}).")
            else:
                leafstorm(self,other)
        elif used=="Leaf Tornado":
            miss=random.randint(1,self.accuracy)
            if miss<10:
                print(f" {other.name} avoided the attack({used}).")
            else:
                leaftornado(self,other)
        elif used=="Leaf Blade":
            leafblade(self,other)
        elif used=="Razor Leaf":
            razorleaf(self,other)
        elif used=="Victory Dance":
            victorydance(self)
            if other.ability=="Dancer":
                print(f" {other.name}'s {other.ability}!")
                victorydance(other)
        elif used=="Light Screen":
            if tr.lightscreen==True:
                print(" It Failed!")
            if tr.lightscreen==False:
                lightscreen(self,other,tr,turn)
        elif used=="Calm Mind":
            calmmind(self)
        elif used=="Aurora Veil":
            if tr.auroraveil==True:
                print(" It failed!")
            if tr.auroraveil==False:
                auroraveil(self,other,tr,turn)
        elif used=="Tailwind":
            if tr.tailwind==True:
                print(" It failed!")
            if tr.tailwind==False:
                tailwind(self,other,tr,turn)
        elif used=="Reflect":
            if tr.reflect==True:
                print(" It failed!")
            if tr.reflect==False:
                reflect(self,other,tr,turn)
        elif used=="Acid Armor":
            acidarmor(self)
        elif used=="Aeroblast":
            miss=random.randint(1,self.accuracy)
            if miss<5:
                print(f" {other.name} avoided the attack({used}).")
            else:
                aeroblast(self,other)
        elif used=="Wicked Blow":
            wickedblow(self,other)
        elif used=="Tail Glow":
            tailglow(self)
        elif used=="Psychic Fangs":
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
        elif used=="Head Charge":
            headcharge(self,other)
        elif used=="Icicle Crash":
            iciclecrash(self,other)
        elif used=="Toxic Thread":
            toxicthread(self,other)
        elif used=="Nature's Madness":
            naturesmadness(self,other)
        elif used=="Scorching Sands":
            scorchingsands(self,other)
        elif used=="Outrage":
            outrage(self,other)
        elif used=="Lunge":
            lunge(self,other)
        elif used=="Strength Sap":
            strengthsap(self,other)
        elif used=="Surging Strikes":
            for i in range(3):
                surgingstrikes(self,other)
        elif used=="Heat Wave":
            miss=random.randint(1,self.accuracy)
            if miss<10:
                print(f" {other.name} avoided the attack({used}).")
            else:
                heatwave(self,other)
        elif used=="Slash":
            slash(self,other)
        elif used=="Night Slash":
            nightslash(self,other)
        elif used=="Psycho Cut":
            psychocut(self,other)
        elif used=="Sacred Fire":
            miss=random.randint(1,self.accuracy)
            if miss<5:
                print(f" {other.name} avoided the attack({used}).")
            else:
                sacredfire(self,other)
        elif used=="Brick Break":
            brickbreak(self,other,optr)
        elif used=="Rock Wrecker":
            miss=random.randint(1,self.accuracy)
            if miss<10:
                print(f" {other.name} avoided the attack({used}).")
            else:
                rockwrecker(self,other)
                if other.hp>0:
                    self.recharge=True            
        elif used=="Giga Impact":
            miss=random.randint(1,self.accuracy)
            if miss<10:
                print(f" {other.name} avoided the attack({used}).")
            else:
                gigaimpact(self,other)
                self.recharge=True
        elif used=="Meteor Assault":
            meteorassault (self,other)
            if other.hp>0:
                self.recharge=True
        elif used=="Cross Chop":
            miss=random.randint(1,self.accuracy)
            if miss<20 and "No Guard" not in (self.ability,other.ability):
                print(f" {other.name} avoided the attack({used}).")
            else:
                crosschop(self,other)
        elif used=="Hyper Beam":
            miss=random.randint(1,self.accuracy)
            if miss<10:
                print(f" {other.name} avoided the attack({used}).")
            else:
                hyperbeam(self,other)
                self.recharge=True
        elif used=="Roar of Time":
            miss=random.randint(1,self.accuracy)
            if miss<10:
                print(f" {other.name} avoided the attack({used}).")
            else:
                roaroftime(self,other)
                self.recharge=True
        elif used=="Spacial Rend":
            miss=random.randint(1,self.accuracy)
            if miss<5:
                print(f" {other.name} avoided the attack({used}).")
            else:
                spacialrend(self,other)
        elif used=="Phantom Force":
            miss=random.randint(1,self.accuracy)
            if miss>95:
                print(f" {other.name} avoided the attack({used}).")
            else:
                phantomforce(self,other)                  
        elif used=="Shadow Force":
            miss=random.randint(1,self.accuracy)
            if miss>95:
                print(f" {other.name} avoided the attack({used}).")
            else:
                shadowforce(self,other)                
        elif used=="Iron Head":
            ironhead(self,other)
        elif used=="Iron Tail":
            miss=random.randint(1,self.accuracy)
            if miss>75:
                print(f" {other.name} avoided the attack({used}).")
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
            miss=random.randint(1,self.accuracy)
            if miss>90:
                print(f" {other.name} avoided the attack({used}).")
            else:
                playrough (self,other)
        elif used=="Power Whip":
            powerwhip(self,other)
        elif used=="Ancient Power":
            apower(self,other)
        elif used=="Stone Axe":
            stoneaxe(self,other,optr)
        elif used=="Strength":
            strength(self,other)
        elif used=="Petal Dance":
            petaldance(self,other)
            if other.ability=="Dancer":
                print(f" {other.name}'s {other.ability}!")
                petaldance(other)
        elif used=="Dizzy Punch":
            dizzypunch (self,other)
        elif used=="G-Max Resonance":
            gmaxresonance(self,other,tr,turn)
        elif used=="G-Max Stonesurge":
            gmaxstonesurge(self,other,optr)
        elif used=="Barb Barrage":
            barbbarrage (self,other)
        elif used=="Mach Punch":
            machpunch(self,other)
        elif used=="Thunder":
            if field.weather in ["Rainy","Primordial Sea"] and field.weather in ["Rainy","Primordial Sea"]:
                thunder(self,other)
            else:
                miss=random.randint(1,self.accuracy)
                if miss>70:
                    print(f" {other.name} avoided the attack({used}).")
                elif miss<=70 or "No Guard" in (self.ability,other.ability):
                    thunder(self,other)
        elif used=="Scald":
            scald(self,other)
        elif used=="Egg Bomb":
            eggbomb(self,other)
        elif used=="Hex":
            hex (self,other)
        elif used=="Fake Out":
            if self.canfakeout==False:
                print("  It failed!")
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
            miss=random.randint(1,self.accuracy)
            if miss>90:
                print(f" {other.name} avoided the attack({used}).")
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
            miss=random.randint(1,self.accuracy)
            if miss>90:
                print(f" {other.name} avoided the attack({used}).")
            else:
                zenheadbutt(self,other)
        elif used=="Dragon Hammer":
            dragonhammer(self,other)
        elif used=="Arm Thrust":
            hit=random.randint(3,5)
            if self.ability=="Skill Link":
                print(f" {self.name}'s {self.ability}.")
                hit=5
            for i in range(hit):
                armthrust(self,other)
        elif used=="Pin Missile":
            hit=random.randint(3,5)
            if self.ability=="Skill Link":
                print(f" {self.name}'s {self.ability}.")
                hit=5
            for i in range(hit):
                pinmissile(self,other)
            print(f" It hit {hit} time(s).")
        elif used=="Explosion":
            if other.ability=="Damp":
                print("  Can't explode on Damp Pokémons.")
            if other.ability!="Damp":
                explosion(self,other)
        elif used=="Icicle Spear":
            hit=random.randint(3,5)
            if self.ability=="Skill Link":
                print(f" {self.name}'s {self.ability}.")
                hit=5
            for i in range(hit):
                iciclespears(self,other)
            print(f" It hit {hit} time(s).")
        elif used=="Waterfall":
            waterfall(self,other)
        elif used=="Wood Hammer":
            woodhammer(self,other)
        elif used=="Energy Ball":
            energyball(self,other)
        elif used=="Rest":
            if self.hp==self.maxhp:
                print("  It failed!")
            else:
                rest(self)
        elif used=="Bulk Up":
            bulkup(self)
        elif used=="Stone Edge":
            miss=random.randint(1,100)
            if miss>90:
                print(f" {other.name} avoided the attack({used}).")
            else:
                stoneedge(self,other)
        elif used=="Steel Wing":
            steelwing(self,other)
        elif used=="Focus Blast":
            miss=random.randint(1,self.accuracy)
            if miss>70:
                print(f" {other.name} avoided the attack({used}).")
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
        elif used=="Make It Rain":
            makeitrain(self,other)
        elif used=="Dark Pulse":
            darkpulse(self,other)
        elif used=="Sacred Sword":
            sacredsword(self,other)
        elif used=="Secret Sword":
            secretsword(self,other)
        elif used=="Super Fang":
            superfang(self,other)
        elif used=="Core Enforcer":
            coreenforcer(self,other)
        elif used=="Superpower":
            superpower(self,other)
        elif used=="Assurance":
            assurance(self,other)
        elif used=="Rock Blast":
            miss=random.randint(1,100)
            if miss>90:
                print(f" {other.name} avoided the attack({used}).")
            else:
                hit=random.randint(3,5)
                if self.ability=="Skill Link":
                    print(f" {self.name}'s {self.ability}.")
                    hit=5
                for i in range(hit):
                    rockblast(self,other)
                print(f" It hit {hit} time(s).")
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
        elif used=="Submission":
            submission(self,other)
        elif used=="Brave Bird":
            bravebird(self,other)
        elif used=="Body Slam":
            bodyslam(self,other)
        elif used=="Dynamic Punch":
            miss=random.randint(1,100)
            if miss>50 and self.ability!="No Guard":
                print(f" {other.name} avoided the attack({used}).")
            if miss<=50 or "No Guard" in (self.ability,other.ability):
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
                print(f" {other.name} avoided the attack({used}).")
            else:
                belch(self,other)
        elif used=="Gunk Shot":
            miss=random.randint(1,100)
            if miss>80:
                print(f" {other.name} avoided the attack({used}).")
            else:
                gunkshot(self,other)
        elif used=="Freeze Shock":
            miss=random.randint(1,100)
            if miss>90:
                print(f" {other.name} avoided the attack({used}).")
            else:
                freezeshock(self,other)                   
        elif used=="Ice Burn":
            miss=random.randint(1,100)
            if miss>90:
                print(f" {other.name} avoided the attack({used}).")
            else:
                iceburn(self,other)                      
        elif used=="Blue Flare":
            miss=random.randint(1,100)
            if miss>85:
                print(f" {other.name} avoided the attack({used}).")
            else:
                blueflare(self,other)                
        elif used=="Bolt Strike":
            miss=random.randint(1,100)
            if miss>85:
                print(f" {other.name} avoided the attack({used}).")
            else:
                boltstrike(self,other)       
        elif used=="Mountain Gale":
            miss=random.randint(1,100)
            if miss>85:
                print(f" {other.name} avoided the attack({used}).")
            else:
                mountaingale(self,other)       
        elif used=="Mystical Power":#isinstance(used,FireBlast)
            miss=random.randint(1,100)
            if miss>90:
                print(f" {other.name} avoided the attack({used}).")
            else:
                mysticalpower(self,other)                
                                                
        elif used=="Fire Blast":#isinstance(used,FireBlast)
            miss=random.randint(1,100)
            if miss>85:
                print(f" {other.name} avoided the attack({used}).")
            else:
                fireBlast(self,other)
            
                
        elif used=="Pyro Ball":
            miss=random.randint(1,100)
            if miss>90:
                print(f" {other.name} avoided the attack({used}).")
            else:
                pyroball(self,other)       
        elif used=="Meteor Beam":
            miss=random.randint(1,100)
            if miss>90:
                print(f" {other.name} avoided the attack({used}).")
            else:
                meteorbeam(self,other)                                
        elif used=="Psychic":
            psychic(self,other)
        elif used=="Seed Flare":
            miss=random.randint(1,100)
            if miss>85:
                print(f" {other.name} avoided the attack({used}).")
            else:
                seedflare(self,other)
        elif used=="Thunderbolt":
            tbolt(self,other)
        elif used=="Shell Trap":
            print(f" {self.name} used Shell Trap!")
            self.abilityused="Shell Trap"
        elif used=="Poison Jab":
            poisonjab(self,other)
        elif used=="Judgement":
            judgement(self,other)
        elif used=="Discharge":
            discharge(self,other)
        elif used=="Ice Beam":
            icebeam(self,other)
        elif used=="Fusion Bolt":
            fusionbolt(self,other)
        elif used=="Fiery Wrath":
            fierywrath(self,other)
        elif used=="Thunderous Kick":
            thunderouskick(self,other)
        elif used=="Fusion Flare":
            fusionflare(self,other)
        elif used=="Moonblast":
            moonblast(self,other)
        elif used=="Hydro Pump":
            miss=random.randint(1,100)
            if miss>80:
                print(f" {other.name} avoided the attack({used}).")
            else:
                hydropump(self,other)
        elif used=="Earth Power":
            earthpower(self,other)
        elif used=="Destiny Bond":
            destinybond(self,other)
        elif used=="Giga Drain":
            gigadrain(self,other)
        elif used=="Hidden Power":
            hiddenpower(self,other)
        elif used =="Hydro Vortex":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Waterium Z.")
            self.item=None
            hydrovortex(self,other)
            self.moves.remove(used)
        elif used =="Oceanic Operetta":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item=None
            operetta(self,other,field,turn)
            self.moves.remove(used)
        elif used =="Malicious Moonsault":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item=None
            moonsault(self,other)
            self.moves.remove(used)
        elif used =="Light That Burns The Sky":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item=None
            skyburn(self,other)
            self.moves.remove(used)
        elif used =="Let's Snuggle Forever":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item=None
            snuggle(self,other)
            self.moves.remove(used)      
        elif used =="Extreme Evoboost":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item=None
            exevoboost(self)
            self.moves.remove(used)      
        elif used =="Guardian of Alola":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item=None
            goalola(self,other)
            self.moves.remove(used)
        elif used =="Stoked Sparksurfer":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item=None
            sparksurf(self,other)
            self.moves.remove(used)
        elif used =="Clangorous Soulblaze ":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item=None
            soulblaze(self,other)
            self.moves.remove(used)
        elif used =="Sinister Arrow Raid":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item=None
            arrowraid(self,other)
            self.moves.remove(used)
        elif used =="Soul-Stealing 7-Star Strike":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item=None
            soulstealing(self,other)
            self.moves.remove(used)
        elif used =="Menacing Moonraze Maelstrom":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item=None
            menacingmoonrazemaelstrom(self,other)
            self.moves.remove(used)
        elif used =="Searing Sunraze Smash":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item=None
            searingsunrazesmash(self,other,field,turn)
            self.moves.remove(used)
        elif used =="Genesis Supernova":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item=None
            genesissupernova(self,other,field,turn)
            self.moves.remove(used)
        elif used =="Pulverizing Pancake":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Snorlium Z.")
            self.item=None
            pulverizingpancake(self,other)
            self.moves.remove(used)
        elif used =="Splintered Stromshards":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Lycanium Z.")
            self.item=None
            stormshards(self,other)
            self.moves.remove(used)                
        elif used =="Inferno Overdrive":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Firium Z.")
            self.item=None
            infernooverdrive(self,other)
            self.moves.remove(used)
        elif used =="Bloom Doom":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Grassium Z.")
            self.item=None
            bloomdoom(self,other)
            self.moves.remove(used)
        elif used =="Gigavolt Havoc":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Electrium Z.")
            self.item=None
            gigavolthavoc(self,other)
            self.moves.remove(used)
        elif used =="Catastropika":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item=None
            catastropika(self,other)
            self.moves.remove(used)
        elif used =="Pulverizing Pancake":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item=None
            pulverizingpancake(self,other)
            self.moves.remove(used)
        elif used =="10,000,000 Volt Thunderbolt":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s {self.item}.")
            self.item=None
            tenmvolttb(self,other)
            self.moves.remove(used)
        elif used =="Acid Downpour":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Poisonium Z.")
            aciddownpour(self,other)
            self.moves.remove(used)
        elif used =="Breakneck Blitz":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Normalium Z.")
            self.item=None
            breakneckblitz(self,other)
            self.moves.remove(used)
        elif used =="All-Out Pummeling":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Fightinium Z.")
            self.item=None
            alloutpummeling(self,other)
            self.moves.remove(used)
        elif used =="Black Hole Eclipse":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Darkinium Z.")
            self.item=None
            blackholeeclipse(self,other)
            self.moves.remove(used)
        elif used =="Continental Crush":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Rockium Z.")
            self.item=None
            continentalcrush(self,other)
            self.moves.remove(used)
        elif used =="Tectonic Rage":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Groundium Z.")
            self.item=None
            tectonicrage(self,other)
            self.moves.remove(used)
        elif used =="Corkscrew Crash":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Steelium Z.")
            self.item=None
            corkscrewcrash(self,other)
            self.moves.remove(used)
        elif used =="Devastating Drake":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Dragonium Z.")
            self.item=None
            devastatingdrake(self,other)
            self.moves.remove(used)
        elif used =="Shattered Psyche":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Psychium Z.")
            self.item=None
            shatteredpsyche(self,other)
            self.moves.remove(used)
        elif used =="Never-ending Nightmare":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Ghostium Z.")
            self.item=None
            neverendingnightmare(self,other)
            self.moves.remove(used)
        elif used =="Supersonic Skystrike":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Flyinium Z.")
            self.item=None
            supersonicskystrike(self,other)
            self.moves.remove(used)
        elif used =="Savage Spin-Out":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Buginium Z.")
            self.item=None
            savagespinout(self,other)
            self.moves.remove(used)
        elif used =="Subzero Slammer":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Icium Z.")
            self.item=None
            subzeroslammer (self,other)
            self.moves.remove(used)
        elif used =="Twinkle Tackle":
            self.name=self.name.split("(")[0]
            print(f" {self.name} reacting to {tr.name}'s Fairium Z.")
            self.item=None
            twinkletackle(self,other)
            self.moves.remove(used)
        elif used=="Counter":
           print(f" {self.name} used Counter!")
           if self.speed<other.speed and opuse in contactmoves:
               other.hp-=self.dmgtaken*2
           else:
               print(" It failed.")
        elif used=="Mirror Coat":
           print(f" {self.name} used Mirror Coat!")
           if self.speed<other.speed and opuse not in contactmoves:
               other.hp-=self.dmgtaken*2
           else:
               print(" It failed.")
        else:
            pass
    if "Destiny Bond" in self.moves and used!="Destiny Bond":
        other.dbond=False
    if other.hp<0:
        other.hp=0
    other.dmgtaken=before-other.hp
    if used not in statusmove:
        if other.item=="Maranga Berry":
            print(f" {other.item} raised it's special defense.")
            spdefchange(other,0.5)
            other.item=None
        if other.item=="Kee Berry":
            print(f" {other.item} raised it's defense.")
            defchange(other,0.5)
            other.item=None
        if other.item=="Jacoba Berry":
            print(f" {other.name}'s {other.item} damaged {self.name}!")
            self.hp-=round(self.maxhp/8)
            other.item=None
            
    
    if other.hp>0:
          if other.hp<=(other.maxhp/4)  and before>(other.maxhp/4):
              if other.item=="Custap Berry" and other.speed<self.speed:
                  print(f" {other.item} will let {other.name} move first!")
                  other.priority=True
                  other.item=None
              if other.item=="Liechi Berry":
                  print(f" {other.item} raised it's attack.")
                  atkchange (other,0.5)
                  other.item=None
              if other.item=="Lansat Berry":
                  print(f" {other.item} raised it's critical hit ratio.")
                  other.critrate*=4
              if other.item=="Ganlon Berry":
                  print(f" {other.item} raised it's defense.")
                  defchange (other,0.5)
                  other.item=None
              if other.item=="Apicot Berry":
                  print(f" {other.item} raised it's special defense.")
                  spdefchange (other,0.5)
                  other.item=None
          if other.hp<=(other.maxhp/2)  and before>(other.maxhp/2):
              if other.ability=="Anger Shell":
                  print(f" 💢 {other.name}'s {other.ability}!")
                  defchange (other,-0.5)
                  spdefchange (other,-0.5)
                  atkchange(other,0.5)
                  spatkchange (other,0.5)
                  speedchange (other,0.5)
              if other.ability=="Berserk":
                  print(f" {other.name}'s {other.ability}!")
                  spatkchange (other,0.5)
              if other.item in ["Aguav Berry","Figy Berry","Ipapa Berry","Mago Berry"]:
                  other.hp+=round(other.maxhp/4)
                  print(f" {other.name} consumed it's {other.item} and restored some HP!")
              if other.item=="Sitrus Berry":
                  other.hp+=round(other.maxhp/4)
                  print(f" {other.name} restored HP using its {other.item}!")
                  other.item=None
    if self.hp>0 and self.hp<=(self.maxhp/2)  and sbefore>(self.maxhp/2):
              if self.item=="Sitrus Berry":
                  self.hp+=round(self.maxhp/4)
                  print(f" {self.name} ate {self.item} and restored some HP!")
                  self.item=None
              
#STURDY        
    if used in contactmoves and other.abilityused=="Shell Trap":
        shelltrap(other,self)
        other.abilityused=False
    if before==other.maxhp and other.hp<=0 and hit==1:        
        if "Ash" in other.owner.name:
            ch=random.randint(1,100)
            if ch<40:
                print(f" 💝 {other.name} got up remembering {other.owner.name}'s friendship!")
                other.hp=1
        if other.ability=="Sturdy" and other.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and used not in multimove:
            print(f" {other.name}'s Sturdy!")
            other.hp=1
            if other.item=="Custap Berry" and other.speed<self.speed:
              print(f" {other.item} will let {other.name} move first!")
              other.priority=True
              other.item=None
        if other.item=="Focus Sash" and used not in multimove:
            print(f" {other.name} hung on using Focus Sash.")
            other.hp=1
            other.item=None
    per=round(((before-other.hp)/other.maxhp)*100,2)
    sper=round(((sbefore-self.hp)/self.maxhp)*100,2)
    if other.hp<0:
        per=round((before/other.maxhp)*100,2)
    if self.hp<0:
        sper=round((sbefore/self.maxhp)*100,2)
    if other.hp!=before:
#STAMINA        
        if other.ability=="Stamina":
            print(f" {other.name}'s {other.ability}!")
            defchange(other,0.5)
            print(f" {other.name}: Defense x{other.defb}")
    if self.dbond is True and other.hp<=0:
        self.hp=0
        print(f" {other.name} took away {self.name} with it!")
#ILLUSION        
        if other.ability=="Illusion" and "Zoroark" not in other.name:
            if other.type1=="Dark":
                other.name="Zoroark"
                print(f" {other.name}'s Illusion wore off!")
            else:
                other.name="Hisuian Zoroark"
                print(f" {other.name}'s Illusion wore off!")
    if self.hp!=sbefore and self==me:
        if self.ability=="Illusion" and "Zoroark" not in self.name:
            if self.type1=="Dark":
                self.name="Zoroark"
                print(f" {self.name}'s Illusion wore off!")
            else:
                self.name="Hisuian Zoroark"
                print(f" {self.name}'s Illusion wore off!")
    if other.ability=="Flame Body" and me.status=="Alive" and me.ability!="Long Reach" and used in contactmoves:
        ch=random.randint(1,100)  
        if ch>70:
            print(f" 🔥 {other.name}'s {other.ability}!")
            me.status="Burned"  
            print(f" 🔥 {me.name} was burned.") 
    if other.ability=="Toxic Debris" and "Toxic Spikes" not in tr.hazard and me.ability!="Long Reach" and used in contactmoves:
        print(f" ☣️ {other.name}'s {other.ability}!")   
        print(" ☠️ Poison spikes were scattered all around the opposing team!")
        tr.hazard.append("Toxic Spikes")   
    if other.ability=="Static" and me.status=="Alive" and me.ability!="Long Reach" and used in contactmoves:
        ch=random.randint(1,100)  
        if ch>70:
            print(f" ⚡ {other.name}'s {other.ability}!")
            me.status="Paralyzed"
            print(f" ⚡ {self.name} was paralyzed.")
    if other.ability=="Poison Point" and me.status=="Alive" and me.ability!="Long Reach" and used in contactmoves:
        ch=random.randint(1,100)  
        if ch>70:
            print(f" ☠️ {other.name}'s {other.ability}!")
            self.status="Badly Poisoned"  
            print(f" ☠️ {me.name} was badly poisoned.")
    if self.ability=="Poison Touch" and other.status=="Alive" and other.ability!="Long Reach" and used in contactmoves:
        ch=random.randint(1,100)  
        if ch>70:
            print(f" {self.name}'s {self.ability}!")
            other.status="Badly Poisoned"        
    if used in contactmoves and other.item=="Air Balloon":
        print(f" {other.name}'s Air Balloon popped off!")
        other.item=None                      
    if other.hp!=before and per>0:
        if used not in statusmove:
#ROUGH SKIN/IRON BARBS            
            if other.ability in ["Rough Skin","Iron Barbs"] and used in contactmoves and self.ability!="Long Reach":
                print(f" {me.name} was hurt by {other.name}'s {other.ability}!")
                me.hp-=round((me.maxhp/16),2)
                if me.hp<0:
                    me.hp=0
        if other.item=="Rocky Helmet" and self.ability!="Magic Guard" and used in contactmoves:
            me.hp-=round(me.maxhp/6)
            print(f" {me.name} was hurt by {other.name}'s Rocky Helmet!")
            if me.hp<0:
                me.hp=0                    
#LIFE ORB                    
        if self.item=="Life Orb" and self.ability!="Magic Guard":
            self.hp-=round(self.maxhp/16)
            print(f" {self.name} lost some of its HP!")
            if self.hp<0:
                self.hp=0
    if other.hp==0:
#AFTERMATH        
        if other.ability=="Aftermath":
            print(f" {other.name}'s {other.ability}!")
            if self.hp<(self.maxhp/4):
                self.hp==0
            else:
                self.hp-=round(self.maxhp/4)
    self.dbond=False            
#PERCENTAGE                
    if before!=other.hp:
        print(f" ({other.name} lost {per}% of its health!)")
    if self.hp!=sbefore and self==me and sper<0:
        print(f" Total health regained {-sper}%")
    if self.hp!=sbefore and self==me and sper>0:
        print(f" Total damage received {sper}%")
    return self
#EFFECTS
def effects(self,other,turn):
    print("  ")
    self.flinched=False
    if self.status!="Alive" and self.ability in ["Purifying Salt","Good as Gold"]:
        print(f" {self.name}'s {self.ability}!")
        self.status="Alive"
    if field.trickroom==True:
        if turn==field.troomendturn:
            field.trickroom=False
            print (" 🌐 The dimensions turned back to normal!")
    if self.dmax is True and turn==self.maxend:
        self.dmax=False
        self.name=self.name.split(" ")[-1]
        self.hp=round(self.hp/2)
        self.maxhp=round(self.maxhp/2)
        print(f" 🔻 {self.name} returned to it's normal state!")
    if self.item is None and other.item is not None and self.ability=="Pick Pocket":
        self.item=other.item
        other.item=None       
#FLINCH RESET    
    self.flinched=False
    if ("Primal Kyogre" not in self.name and "Primal Kyogre" not in other.name) and field.weather=="Primordial Sea":
        field.weather="Clear"
        print("  🌦️ The heavy rain stopped!")
    if ("Primal Groudon" not in self.name and "Primal Groudon" not in other.name) and field.weather=="Desolate Land":
        field.weather="Clear"       
        print("  🌥️ The extremely harsh sunlight faded!")
#GRASSY TERRAIN    
    if self.hp>0 and field.terrain =="Grassy" and self.hp<self.maxhp and self.ability not in ["Levitate"] and self.type1!="Flying" and self.type2!="Flying":
        print(f" 🌿 {self.name}'s HP was restored.")
        self.hp+=round(self.maxhp/16)
        if self.hp>self.maxhp:
            self.hp=self.maxhp 
#DRY SKIN            
    if field.weather in ["Sunny","Desolate Land"]:
        if self.ability=="Dry Skin":
            print(f" {self.name}'s {self.ability}!")
            self.hp-=round(self.maxhp/8)
    if field.weather in ["Rainy","Primordial Sea"]:
        if self.ability in ["Dry Skin","Rain Dish"]:
            print(f" {self.name}'s {self.ability}!")
            self.hp+=round(self.maxhp/8)  
        if self.hp>self.maxhp:
            self.hp=self.maxhp       
#ICE BODY            
    if field.weather in ["Hail"]:
        if self.ability=="Ice Body":
            print(f" ❄️ {self.name}'s {self.ability}!")
            self.hp+=round(self.maxhp/8)        
        if self.hp>self.maxhp:
            self.hp=self.maxhp                          
    #BAD DREAMS
    if other.ability=="Bad Dreams" and self.status=="Sleep":
        self.hp-=round(self.maxhp/8)
        print(f" 💀 {self.name} was hurt by {other.name}'s {other.ability}.")
    #FROSTBITE
    if self.status=="Frostbite" and self.ability not in ["Magic Guard"]:
        self.hp-=round(self.maxhp/16)
        print(f" 🥶 {self.name} was hurt by frostbite.")
    #LEECH SEED
    if self.seeded==True:
        print(f" 🌱 The opposing {self.name}'s health is sapped by leech seed!")
        self.hp-=round(self.maxhp/16)
        if other.hp<=(other.maxhp-other.maxhp/16):
            other.hp+=round(other.maxhp/16)   
    #HAIL DAMAGE
    if field.weather =="Hail" and self.ability!="Snow Cloak":     
        if self.type1!="Ice" and self.type2!="Ice" and self.ability!="Magic Guard":
            self.hp-=round(self.maxhp/16)
            print(f" ❄️ {self.name} is pelted by the hail!")
    #SAND DAMAGE
    if field.weather =="Sandstorm" and self.ability!="Sand Veil":
        if self.type1 not in ["Rock","Ground","Steel"] and self.type2 not in ["Rock","Ground","Steel"] and self.ability!="Magic Guard":
            self.hp-=(1+round(self.maxhp/16))
            print(f" 🏜️ {self.name} is buffeted by the sandstorm!")
    #POISON
    if self.status=="Poisoned" and self.ability not in ["Magic Guard","Poison Heal","Immunity"]:
        self.hp-=(1+round(self.maxhp/16))
        print(f" ☠️ {self.name} was hurt by poison.")
    #BADLY POISONED
    if self.status=="Badly Poisoned" and self.ability not in ["Magic Guard","Poison Heal","Toxic Boost"]:
        self.hp-=(1+(self.maxhp*self.badpoison/16))
        self.badpoison+=1
        print(f" ☠️ {self.name} was hurt by poison.")        
    #BURN        
    if self.status=="Burned" and self.ability not in ["Magic Guard","Flare Boost"]:
        self.hp-=(1+round(self.maxhp/16))
        print(f" 🔥 {self.name} was hurt by burn.")        
    #LEFTOVERS        
    if self.hp>0 and self.item=="Leftovers" and self.hp<self.maxhp:
        print(f" 🍎 {self.name} restored a little HP using its Leftovers.")
        self.hp+=round(self.maxhp/16)
        
    #BLACK SLUDGE        
    if self.hp>0 and self.item=="Black Sludge" and self.hp<self.maxhp:
        if self.type1=="Poison" or self.type2=="Poison":
            print(f" ☠️ {self.name} restored a little HP using its Black Sludge.")
            self.hp+=(1+round(self.maxhp/16))
        elif self.type1!="Poison" and self.type2!="Poison":   
            print(f" ☠️ {self.name} lost a little HP using its Black Sludge.")
            self.hp-=(1+round(self.maxhp/16))
    #POISON HEAL        
    if self.hp>0 and self.ability=="Poison Heal" and self.hp!=self.maxhp and self.status=="Badly Poisoned":
        print(f" ☠️ {self.name} restored a little HP using its Poison Heal.")
        self.hp+=round(self.maxhp/8)                    

    if self.hp>self.maxhp:
        self.hp=self.maxhp
    if self.hp<0:
        self.hp=0