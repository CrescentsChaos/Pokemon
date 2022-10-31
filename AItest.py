#pylint:disable=W0613
#pylint:disable=C0103
#pylint:disable=C0321
#pylint:disable=C0301
#pylint:disable=W0612
#pylint:disable=C0304
#pylint:disable=C0303
import random
def AI(self=None,other=None,tr1=None,tr2=None):
    eff=1
    eff2=1
    res=1
    res2=1
    imm=1
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
    if self.type1 in grasseff and (other.type1=="Grass" or other.type2=="Grass"):
        eff*=2
    if self.type2 in grasseff and (other.type1=="Grass" or other.type2=="Grass"):
        eff2*=2
    if self.type1 in grasswk and (other.type1=="Grass" or other.type2=="Grass"):
        res/=2
    if self.type2 in grasswk and (other.type1=="Grass" or other.type2=="Grass"):
        res2/=2
    if self.type1 in watereff and (other.type1=="Water" or other.type2=="Water"):
        eff*=2
    if self.type2 in watereff and (other.type1=="Water" or other.type2=="Water"):
        eff2*=2
    if self.type1 in waterwk and (other.type1=="Water" or other.type2=="Water"):
        res/=2
    if self.type2 in waterwk and (other.type1=="Water" or other.type2=="Water"):
        res2/=2
    if self.type1 in fireeff and (other.type1=="Fire" or other.type2=="Fire"):
        eff*=2
    if self.type2 in fireeff and (other.type1=="Fire" or other.type2=="Fire"):
        eff2*=2
    if self.type1 in firewk and (other.type1=="Fire" or other.type2=="Fire"):
        res/=2
    if self.type2 in firewk and (other.type1=="Fire" or other.type2=="Fire"):
        res2/=2
    if self.type1 in electriceff and (other.type1=="Electric" or other.type2=="Electric"):
        eff*=2
    if self.type2 in electriceff and (other.type1=="Electric" or other.type2=="Electric"):
        eff2*=2
    if self.type1 in electricwk and (other.type1=="Electric" or other.type2=="Electric"):
        res/=2
    if self.type2 in electricwk and (other.type1=="Electric" or other.type2=="Electric"):
        res2/=2
    if self.type1 in psychiceff and (other.type1=="Psychic" or other.type2=="Psychic"):
        eff*=2
    if self.type2 in psychiceff and (other.type1=="Psychic" or other.type2=="Psychic"):
        eff2*=2
    if self.type1 in psychicwk and (other.type1=="Psychic" or other.type2=="Psychic"):
        res/=2
    if self.type2 in psychicwk and (other.type1=="Psychic" or other.type2=="Psychic"):
        res2/=2
    if self.type1 in ghosteff and (other.type1=="Ghost" or other.type2=="Ghost"):
        eff*=2
    if self.type2 in ghosteff and (other.type1=="Ghost" or other.type2=="Ghost"):
        eff2*=2
    if self.type1 in ghostwk and (other.type1=="Ghost" or other.type2=="Ghost"):
        res/=2
    if self.type2 in ghostwk and (other.type1=="Ghost" or other.type2=="Ghost"):
        res2/=2
    if self.type1 in darkeff and (other.type1=="Dark" or other.type2=="Dark"):
        eff*=2
    if self.type2 in darkeff and (other.type1=="Dark" or other.type2=="Dark"):
        eff2*=2
    if self.type1 in darkwk and (other.type1=="Dark" or other.type2=="Dark"):
        res/=2
    if self.type2 in darkwk and (other.type1=="Dark" or other.type2=="Dark"):
        res2/=2
    if self.type1 in bugeff and (other.type1=="Bug" or other.type2=="Bug"):
        eff*=2
    if self.type2 in bugeff and (other.type1=="Bug" or other.type2=="Bug"):
        eff2*=2
    if self.type1 in bugwk and (other.type1=="Bug" or other.type2=="Bug"):
        res/=2
    if self.type2 in bugwk and (other.type1=="Bug" or other.type2=="Bug"):
        res2/=2
    if self.type1 in iceeff and (other.type1=="Ice" or other.type2=="Ice"):
        eff*=2
    if self.type2 in iceeff and (other.type1=="Ice" or other.type2=="Ice"):
        eff2*=2
    if self.type1 in icewk and (other.type1=="Ice" or other.type2=="Ice"):
        res/=2
    if self.type2 in icewk and (other.type1=="Ice" or other.type2=="Ice"):
        res2/=2
    if self.type1 in dragoneff and (other.type1=="Dragon" or other.type2=="Dragon"):
        eff*=2
    if self.type2 in dragoneff and (other.type1=="Dragon" or other.type2=="Dragon"):
        eff2*=2
    if self.type1 in dragonwk and (other.type1=="Dragon" or other.type2=="Dragon"):
        res/=2
    if self.type2 in dragonwk and (other.type1=="Dragon" or other.type2=="Dragon"):
        res2/=2
    if self.type1 in fairyeff and (other.type1=="Fairy" or other.type2=="Fairy"):
        eff*=2
    if self.type2 in fairyeff and (other.type1=="Fairy" or other.type2=="Fairy"):
        eff2*=2
    if self.type1 in fairywk and (other.type1=="Fairy" or other.type2=="Fairy"):
        res/=2
    if self.type2 in fairywk and (other.type1=="Fairy" or other.type2=="Fairy"):
        res2/=2
    if self.type1 in steeleff and (other.type1=="Steel" or other.type2=="Steel"):
        eff*=2
    if self.type2 in steeleff and (other.type1=="Steel" or other.type2=="Steel"):
        eff2*=2
    if self.type1 in steelwk and (other.type1=="Steel" or other.type2=="Steel"):
        res/=2
    if self.type2 in steelwk and (other.type1=="Steel" or other.type2=="Steel"):
        res2/=2
    if self.type1 in poisoneff and (other.type1=="Poison" or other.type2=="Poison"):
        eff*=2
    if self.type2 in poisoneff and (other.type1=="Poison" or other.type2=="Poison"):
        eff2*=2
    if self.type1 in poisonwk and (other.type1=="Poison" or other.type2=="Poison"):
        res/=2
    if self.type2 in poisonwk and (other.type1=="Poison" or other.type2=="Poison"):
        res2/=2
    if self.type1 in flyingeff and (other.type1=="Flying" or other.type2=="Flying"):
        eff*=2
    if self.type2 in flyingeff and (other.type1=="Flying" or other.type2=="Flying"):
        eff2*=2
    if self.type1 in flyingwk and (other.type1=="Flying" or other.type2=="Flying"):
        res/=2
    if self.type2 in flyingwk and (other.type1=="Flying" or other.type2=="Flying"):
        res2/=2
    if self.type1 in fightingeff and (other.type1=="Fighting" or other.type2=="Fighting"):
        eff*=2
    if self.type2 in fightingeff and (other.type1=="Fighting" or other.type2=="Fighting"):
        eff2*=2
    if self.type1 in fightingwk and (other.type1=="Fighting" or other.type2=="Fighting"):
        res/=2
    if self.type2 in fightingwk and (other.type1=="Fighting" or other.type2=="Fighting"):
        res2/=2
    if self.type1 in normaleff and (other.type1=="Normal" or other.type2=="Normal"):
        eff*=2
    if self.type2 in normaleff and (other.type1=="Normal" or other.type2=="Normal"):
        eff2*=2
    if self.type1 in normalwk and (other.type1=="Normal" or other.type2=="Normal"):
        res/=2
    if self.type2 in normalwk and (other.type1=="Normal" or other.type2=="Normal"):
        res2/=2
    if self.type1 in rockeff and (other.type1=="Rock" or other.type2=="Rock"):
        eff*=2
    if self.type2 in rockeff and (other.type1=="Rock" or other.type2=="Rock"):
        eff2*=2
    if self.type1 in rockwk and (other.type1=="Rock" or other.type2=="Rock"):
        res/=2
    if self.type2 in rockwk and (other.type1=="Rock" or other.type2=="Rock"):
        res2/=2
    if self.type1 in groundeff and (other.type1=="Ground" or other.type2=="Ground"):
        eff*=2
    if self.type2 in groundeff and (other.type1=="Ground" or other.type2=="Ground"):
        eff2*=2
    if self.type1 in groundwk and (other.type1=="Ground" or other.type2=="Ground"):
        res/=2
    if self.type2 in groundwk and (other.type1=="Ground" or other.type2=="Ground"):
        res2/=2
    if self.type1 in groundimmune and (other.type1=="Ground" or other.type2=="Ground"):
        imm*=2
    if self.type2 in groundimmune and (other.type1=="Ground" or other.type2=="Ground"):
        imm*=2
    if self.type1 in ghostimmune and (other.type1=="Ghost" or other.type2=="Ghost"):
        imm*=2
    if self.type2 in ghostimmune and (other.type1=="Ghost" or other.type2=="Ghost"):
        imm*=2
    if self.type1 in poisonimmune and (other.type1=="Poison" or other.type2=="Poison"):
        imm*=2
    if self.type2 in poisonimmune and (other.type1=="Poison" or other.type2=="Poison"):
        imm*=2
    if self.type1 in normalimmune and (other.type1=="Normal" or other.type2=="Normal"):
        imm*=2
    if self.type2 in normalimmune and (other.type1=="Normal" or other.type2=="Normal"):
        imm*=2
    if self.type1 in psychicimmune and (other.type1=="Psychic" or other.type2=="Psychic"):
        imm*=2
    if self.type2 in psychicimmune and (other.type1=="Psychic" or other.type2=="Psychic"):
        imm*=2
    if self.type1 in electricimmune and (other.type1=="Electric" or other.type2=="Electric"):
        imm*=2
    if self.type2 in electricimmune and (other.type1=="Electric" or other.type2=="Electric"):
        imm*=2
    if self.type1 in fightingimmune and (other.type1=="Fighting" or other.type2=="Fighting"):
        imm*=2
    if self.type2 in fightingimmune and (other.type1=="Fighting" or other.type2=="Fighting"):
        imm*=2        
    if self.type1 in dragonimmune and (other.type1=="Dragon" or other.type2=="Dragon"):
        imm*=2
    if self.type2 in dragonimmune and (other.type1=="Dragon" or other.type2=="Dragon"):
        imm*=2 
    print(f"\nAI FEEDBACK:{other.name}")     
    offense=(eff*res)+(eff*res2)
    offense2=(eff2*res2)+(eff2*res)
    print(offense,offense2,imm)  
    return eff     
    
    
    
def moveAI(self,other,mtr,otr,field):
    mymove=[]
    if self.dmax is True:
        mymove+=self.maxmove
    if self.dmax is False:
        mymove+=self.moves
    types=[]
    mytypes=[]
    
    normalmoves=["Double Edge","Return","Body Slam","Boomburst","Crush Claw","Crush Grip","Dizzy Punch","Egg Bomb","Explosion","Extreme Speed","Hyper Voice","Facade","Multi-Attack","Strength","Hyper Beam","Giga Impact","Relic Song","Techno Blast","Weather Ball","Breakneck Blitz","Skull Bash","Metronome","Head Charge","Max Strike"]
    firemoves=["Fire Blast","Flare Blitz","Flamethrower","Magma Storm","Eruption","Lava Plume","Fire Punch","Blaze Kick","Fire Fang","Fire Lash","Heat Crash","Pyro Ball","Raging Fury","Sacred Fire","V-create","Blast Burn","Blue Flare","Fiery Dance","Fusion Flare","Heat Wave","Inferno","Mystical Fire","Searing Shot","Inferno Overdrive","Armor Cannon","Bitter Blade","Max Flare","G-Max Wildfire"]
    watermoves=["Hydro Pump","Surf","Liquidation","Flip Turn","Hydro Cannon","Muddy Water","Origin Pulse","Scald","Snipe Shot","Sparkling Aria","Steam Eruption","Waterfall","Water Spout","Aqua Jet","Crabhammer","Fishious Rend","Razor Shell","Surging Strikes","Water Shuriken","Wave Crash","Hydro Vortex","Aqua Tail","Max Geyser"]
    electricmoves=["Thunderbolt","Thunder","Volt Switch","Aura Wheel","Bolt Beak","Bolt Strike","Fusion Bolt","Plasma Fists","Thunder Fang","Thunder Punch","Volt Tackle","Electro Ball","Electroweb","Zap Cannon","Gigavolt Havoc","Wild Charge","Overdrive","Max Lightning"]
    groundmoves=["Earthquake","Earth Power","Scorching Sands","Sandsear Storm","Bone Rush","Drill Run","Headlong Rush","High Horsepower","Land's Wrath","Precipice Baldes","Stomping Tantrum","Thousand Arrows","Thousand Waves","Tectonic Rage","Magnitude","Bulldoze","Max Quake"]
    icemoves=["Ice Beam","Blizzard","Icicle Crash","Freeze Shock","Ice Fang","Ice Punch","Ice Shard","Icicle Spear","Mountain Gale","Freeze Dry","Frost Breath","Ice Burn","Subzero Slammer","Glacial Lance","Max Hailstorm","G-Max Resonance"]
    fightingmoves=["Superpower","Close Combat","High Jump Kick","Aura Sphere","Final Gambit","Focus Blast","Secret Sword","Arm Thrust","Body Press","Brick Break","Drain Punch","Mach Punch","Dynamic Punch","Flying Press","Force Palm","Hammer Arm","Power-up Punch","Sacred Sword","Seismic Toss","Sky Uppercutt","Triple Arrows","All-Out Pummeling","Meteor Assault","Submission","Max Knuckle","G-Max Chi Strike"]
    psychicmoves=["Psychic","Extrasensory","Psychic Fangs","Psycho Cut","Psyshield Bash","Zen Headbutt","Esper Wing","Luster Purge","Mist Ball","Psycho Boost","Psystrike","Stored Power","Shattered Psyche","Prismatic Laser","Expanding Force","Max Mindstorm"]
    ghostmoves=["Shadow Ball","Shadow Sneak","Shadow Claw","Spirit Shackle","Bitter Malice","Hex","Infernal Parade","Phantom Force","Shadow Force","Never-ending Nightmare","Moongeist Beam","Astral Barrage","Max Phantasm"]
    fairymoves=["Moonblast","Dazzling Gleam","Play Rough","Spirit Break","Light of Ruin","Twinkle Tackle","Spirit Break","Max Starfall"]
    grassmoves=["Giga Drain","Leaf Blade","Chloroblast","Frenzy Plant","Energy Ball","Grass Knot","Leaf Storm","Leaf Tornado","Seed Flare","Solar Beam","Bullet Seed","Drum Beating","Grassy Glide","Horn Leech","Razor Leaf","Seed Bomb","Wood Hammer","Power Whip","Bloom Doom","Petal Dance","Apple Acid","Grav Apple","Max Overgrowth"]
    rockmoves=["Stone Edge","Accelerock","Diamond Storm","Head Smash","Rock Blast","Rock Slide","Ancient Power","Power Gem","Splintered Stromshards","Continental Crush","Stone Axe","Meteor Beam","Rock Wrecker","Max Rockfall"]
    darkmoves=["Dark Pulse","Night Slash","Crunch","Night Daze","Snarl","Assurance","Ceaseless Edge","Darkest Lariat","Throat Chop","Foul Play","Knock Off","Hyperspace Fury","Sucker Punch","Wicked Blow","Black Hole Eclipse","False Surrender","Max Darkness"]
    dragonmoves=["Draco Meteor","Dragon Pulse","Dragon Claw","Outrage","Core Enforcer","Roar of Time","Special Rend","Devastating Drake","Dragon Energy","Breaking Swipe","Dual Chop","Dragon Darts","Max Wyrmwind"]
    bugmoves=["Megahorn","Pin Missile","Bug Buzz","U-Turn","X-Scissor","Leech Life","Savage Spin-Out","Max Flutterby"]
    poisonmoves=["Poison Jab","Sludge Bomb","Cross Poison","Sludge Wave","Dire Claw","Gunk Shot","Belch","Poison Fang","Poison Tail","Venoshock","Acid Downpour","Max Ooze"]
    steelmoves=["Flash Cannon","Meteor Mash","Bullet Punch","Steel Beam","Doom Desire","Gyro Ball","Heavy Slam","Iron Head","Iron Tail","Steel Wing","Corkscrew Crash","Sunsteel Strike","Max Steelspike","Behemoth Bash","Behemoth Blade"]
    flyingmoves=["Brave Bird","Sky Attack","Acrobatics","Beak Blast","Dragon Ascent","Drill Peck","Dual Wingbeat","Supersonic Skystrike","Aeroblast","Hurricane","Oblivion Wing","Air Slash","Max Airstream"]
    healingmoves=["Recover","Roost","Synthesis","Morning Sun","Moonlight","Slack Off","Soft-Boiled","Milk Drink","Rest","Lunar Blessing"]
    priorityatkmoves=["Mach Punch","Bullet Punch","Sucker Punch","Fake Out","Extreme Speed","Aqua Jet","Shadow Sneak","Accelerock","Ice Shard","Water Shuriken"]
    statuschangemoves=["Will-O-Wisp","Thunder Wave","Toxic"]  
    statusmoves=["Sleep Powder","Iron Defense","Calm Mind","Swords Dance","Bulk Up","Recover","Roost","Thunder Wave","Lunar Blessing","Take Heart","Heart Swap","Will-O-Wisp","Moonlight","Synthesis","Morning Sun","Rain Dance","Sunny Day","Hail","Sandstorm","Dark Void","Trick Room","Nasty Plot","Shell Smash","Dragon Dance","Belly Drum","Spore","Hypnosis","Rest","Coil","Curse","Strength Sap","Leech Seed","Protect","Autotomize"]  
    protectmoves=["King's Shield","Protect","Spiky Shield"]
    prioritymoves=["Mach Punch","Bullet Punch","Sucker Punch","Fake Out","Extreme Speed","Protect","Aqua Jet","Shadow Sneak","Accelerock","Ice Shard","Water Shuriken","Spiky Shield","King's Shield"]
    atkboost=["Swords Dance","Dragon Dance","Bulk Up","Belly Drum","Shell Smash","Victory Dance"] 
    spatkboost=["Nasty Plot","Calm Mind","Quiver Dance","Shell Smash"]
    terrainmove=["Electric Terrain","Misty Terrain","Grassy Terrain","Psychic Terrain"]
    weathermoves=["Rain Dance","Hail","Sandstorm","Sunny Day"]    
    if self.ability=="Galvanize":
        electricmoves+=normalmoves
    if self.ability=="Aerilate":
        flyingmoves+=normalmoves
    if self.ability=="Pixilate":
        fairymoves+=normalmoves
    if self.ability=="Liquid Voice":
        watermoves+=normalmoves
    if self.ability=="Gale Wings" and self.hp==self.maxhp:
        priorityatkmoves+=flyingmoves
    if self.ability=="Pankster" and self.hp==self.maxhp:
        prioritymoves+=statusmoves
    if self.ability=="Blazing Souls" and self.hp==self.maxhp:
        prioritymoves+=firemoves
    if self.type2 is None:
        mytypes.append(self.type1)
    if self.type2 is not None:
        mytypes.append(self.type1)
        mytypes.append(self.type2)
    if other.type2 is None:
        types.append(other.type1)
    if other.type2 is not None:
        types.append(other.type1)
        types.append(other.type2)
    weaklist= []
    resistlist= []
    immunelist=[]
    myweaklist=[]
    myresistlist=[]
    myimmunelist=[]
    myimmunemove=[]
    stablist=[]
    mystablist=[]
    emove=[]      
    resmove=[]
    immunemove=[]
    use=None
    bugres=['Grass', 'Fighting', 'Ground']
    bugwk=['Rock', 'Flying', 'Fire']
    #water✓
    waterres=['Water', 'Ice', 'Fire',"Steel"]
    waterwk=['Grass', 'Electric']
    #Ghost✓
    ghostres=['Poison', 'Bug']
    ghostwk=["Dark","Ghost"]
    ghostimmune=["Normal"]
    #Electric✓
    electricres=['Flying', 'Electric',"Steel"]
    electricwk=['Ground']
    #Psychic✓
    psychicres=['Fighting', 'Psychic']
    psychicwk=['Bug', 'Ghost',"Dark"]
    #Ice✓
    iceres=['Ice']
    icewk=['Steel', 'Fire', 'Fighting',"Rock"]
    #Dragon✓
    dragonres=["Fire","Water","Grass","Electric"]
    dragonwk=["Ice","Dragon","Fairy"]
    #Fairy✓
    fairyres=['Fighting', 'Bug', 'Dark']
    fairywk=['Poison', 'Steel']
    fairyimmune=["Dragon"]
    #Dark✓
    darkres=['Ghost', 'Psychic']
    darkwk=['Fighting', 'Bug', 'Fairy']
    darkimmune=["Psychic"]
    #Steel✓
    steelres=['Rock', 'Ice', 'Fairy',"Normal","Flying","Grass","Psychic","Bug","Steel","Dragon"]
    steelwk=['Fire', 'Fighting', 'Ground']
    steelimmune=["Poison"]
    #GRASS✓
    grassres=["Ground", "Electric", "Grass","Water"]
    grasswk=["Flying", "Poison", "Bug", "Ice", "Fire"]
    #FIRE✓
    fireres=["Bug", "Steel", "Grass", "Ice","Fairy","Fire"]
    firewk=["Rock", "Ground", "Water"]
    #POISON✓
    poisonres=["Grass", "Fairy","Bug","Poison","Fighting"]
    poisonwk=["Psychic", "Ground"]
    #FLYING✓
    flyingres=["Fighting", "Bug", "Grass"]
    flyingwk=['Rock', 'Ice', 'Electric']    
    flyingimmune=["Ground"]
    #Rock✓
    rockres=["Flying", "Normal", "Fire", "Poison"]
    rockwk=['Fighting', 'Ground', 'Steel',"Grass","Water"]
    #Normal✓
    normalres=[]
    normalwk=['Fighting']
    normalimmune=['Ghost']
    #fighting✓
    fightingres=['Bug', 'Rock', "Dark"]
    fightingwk=["Flying", 'Psychic', 'Fairy']
    #ground
    groundres=['Poison', 'Rock']
    groundwk=['Water', 'Grass',"Ice"]
    groundimmune=["Electric"]        
    if "Water" in types:
        stablist+=watermoves
        weaklist=weaklist+waterwk
        resistlist=resistlist+waterres
    if "Fire" in types:
        stablist+=firemoves
        weaklist=weaklist+firewk
        resistlist=resistlist+fireres
    if "Grass" in types:
        stablist+=grassmoves
        weaklist=weaklist+grasswk
        resistlist=resistlist+grassres
    if "Electric" in types:
        stablist+=electricmoves
        weaklist=weaklist+electricwk
        resistlist=resistlist+electricres
    if "Rock" in types:
        stablist+=rockmoves
        weaklist=weaklist+rockwk
        resistlist=resistlist+rockres
    if "Ground" in types:
        stablist+=groundmoves
        weaklist=weaklist+groundwk
        resistlist=resistlist+groundres
        immunelist+=groundimmune
    if "Ghost" in types:
        stablist+=ghostmoves
        weaklist=weaklist+ghostwk
        resistlist=resistlist+ghostres
        immunelist+=ghostimmune
    if "Normal" in types:
        stablist+=normalmoves
        weaklist=weaklist+normalwk
        resistlist=resistlist+normalres
        immunelist+=normalimmune
    if "Dark" in types:
        stablist+=darkmoves
        weaklist=weaklist+darkwk
        resistlist=resistlist+darkres
        immunelist+=darkimmune
    if "Psychic" in types:
        stablist+=psychicmoves
        weaklist=weaklist+psychicwk
        resistlist=resistlist+psychicres
    if "Bug" in types:
        stablist+=bugmoves
        weaklist=weaklist+bugwk
        resistlist=resistlist+bugres
    if "Flying" in types:
        stablist+=flyingmoves
        weaklist=weaklist+flyingwk
        resistlist=resistlist+flyingres
        immunelist+=flyingimmune
    if "Fighting" in types:
        stablist+=fightingmoves
        weaklist=weaklist+fightingwk
        resistlist=resistlist+fightingres
    if "Fairy" in types:
        stablist+=fairymoves
        weaklist=weaklist+fairywk
        resistlist=resistlist+fairyres
        immunelist+=fairyimmune
    if "Steel" in types:
        stablist+=steelmoves
        weaklist=weaklist+steelwk
        resistlist=resistlist+steelres
        immunelist+=steelimmune
    if "Poison" in types:
        stablist+=poisonmoves
        weaklist=weaklist+poisonwk
        resistlist=resistlist+poisonres
    if "Ice" in types:
        stablist+=icemoves
        weaklist=weaklist+icewk
        resistlist=resistlist+iceres
    if "Dragon" in types:
        stablist+=dragonmoves
        weaklist=weaklist+dragonwk
        resistlist=resistlist+dragonres
    if "Water" in mytypes:
        mystablist+=watermoves
        myweaklist=myweaklist+waterwk
        myresistlist=myresistlist+waterres
    if "Fire" in mytypes:
        mystablist+=firemoves
        myweaklist=myweaklist+firewk
        myresistlist=myresistlist+fireres
    if "Grass" in mytypes:
        mystablist+=grassmoves
        myweaklist=myweaklist+grasswk
        myresistlist=myresistlist+grassres
    if "Electric" in mytypes:
        mystablist+=electricmoves
        myweaklist=myweaklist+electricwk
        myresistlist=myresistlist+electricres
    if "Rock" in mytypes:
        mystablist+=rockmoves
        myweaklist=myweaklist+rockwk
        myresistlist=myresistlist+rockres
    if "Ground" in mytypes:
        mystablist+=groundmoves
        myweaklist=myweaklist+groundwk
        myresistlist=myresistlist+groundres
        myimmunelist+=groundimmune
    if "Ghost" in mytypes:
        mystablist+=ghostmoves
        myweaklist=myweaklist+ghostwk
        myresistlist=myresistlist+ghostres
        myimmunelist+=ghostimmune
    if "Normal" in mytypes:
        mystablist+=normalmoves
        myweaklist=myweaklist+normalwk
        myresistlist=myresistlist+normalres
        myimmunelist+=normalimmune
    if "Dark" in mytypes:
        mystablist+=darkmoves
        myweaklist=myweaklist+darkwk
        myresistlist=myresistlist+darkres
        myimmunelist+=darkimmune
    if "Psychic" in mytypes:
        mystablist+=psychicmoves
        myweaklist=myweaklist+psychicwk
        myresistlist=myresistlist+psychicres
    if "Bug" in mytypes:
        mystablist+=bugmoves
        myweaklist=myweaklist+bugwk
        myresistlist=myresistlist+bugres
    if "Flying" in mytypes:
        mystablist+=flyingmoves
        myweaklist=myweaklist+flyingwk
        myresistlist=myresistlist+flyingres
        myimmunelist+=flyingimmune
    if "Fighting" in mytypes:
        mystablist+=fightingmoves
        myweaklist=myweaklist+fightingwk
        myresistlist=myresistlist+fightingres
    if "Fairy" in mytypes:
        mystablist+=fairymoves
        myweaklist=myweaklist+fairywk
        myresistlist=myresistlist+fairyres
        myimmunelist+=fairyimmune
    if "Steel" in mytypes:
        mystablist+=steelmoves
        myweaklist=myweaklist+steelwk
        myresistlist=myresistlist+steelres
        myimmunelist+=steelimmune
    if "Poison" in mytypes:
        mystablist+=poisonmoves
        myweaklist=myweaklist+poisonwk
        myresistlist=myresistlist+poisonres
    if "Ice" in mytypes:
        mystablist+=icemoves
        myweaklist=myweaklist+icewk
        myresistlist=myresistlist+iceres
    if "Dragon" in mytypes:
        mystablist+=dragonmoves
        myweaklist=myweaklist+dragonwk
        myresistlist=myresistlist+dragonres        
    mystablist+=("Tera Blast","Judgement")
    mystablist=list(set(mymove).intersection(mystablist))
    weaklist=list(set(weaklist)-set(resistlist)-set(immunelist))
    #IMMUNEMOVES AGAINST OPPONENT
    if "Steel" in immunelist:
        myimmunemove+=list(set(mymove).intersection (steelmoves))
    if "Dark" in immunelist:
        myimmunemove+=list(set(mymove).intersection (darkmoves))        
    if "Ghost" in immunelist:
        myimmunemove+=list(set(mymove).intersection (ghostmoves))        
    if "Fairy" in immunelist:
        myimmunemove+=list(set(mymove).intersection (fairymoves))       
    if "Normal" in immunelist:
        myimmunemove+=list(set(mymove).intersection(normalmoves))         
    if "Flying" in immunelist:
        myimmunemove+=list(set(mymove).intersection (flyingmoves))        
    if "Ground" in immunelist:
        myimmunemove+=list(set(mymove).intersection (groundmoves))   
    #if "Steel" in myimmunelist:
#        myimmunemove+=list(set(mymove).intersection (steelmoves))
#    if "Dark" in myimmunelist:
#        myimmunemove+=list(set(mymove).intersection (darkmoves))        
#    if "Ghost" in myimmunelist:
#        myimmunemove+=list(set(mymove).intersection (ghostmoves))        
#    if "Fairy" in myimmunelist:
#        myimmunemove+=list(set(mymove).intersection (fairymoves))       
#    if "Normal" in myimmunelist:
#        myimmunemove+=list(set(mymove).intersection(normalmoves))         
#    if "Flying" in myimmunelist:
#        myimmunemove+=list(set(mymove).intersection (flyingmoves))        
#    if "Ground" in myimmunelist:
#        myimmunemove+=list(set(mymove).intersection (groundmoves))             
    if "Water" in weaklist:
        emove+=list(set(mymove). intersection(watermoves))
    if "Fire" in weaklist:
        emove+=list(set(mymove). intersection(firemoves))
    if "Grass" in weaklist:
        emove+=list(set(mymove). intersection(grassmoves))          
    if "Rock" in weaklist:
        emove+=list(set(mymove). intersection(rockmoves))     
    if "Ground" in weaklist:
        emove+=list(set(mymove). intersection(groundmoves)) 
    if "Electric" in weaklist:
        emove+=list(set(mymove). intersection(electricmoves))              
    if "Ice" in weaklist:
        emove+=list(set(mymove). intersection(icemoves))
    if "Dragon" in weaklist:
        emove+=list(set(mymove). intersection(dragonmoves))     
    if "Normal" in weaklist:
        emove+=list(set(mymove). intersection(normalmoves))     
    if "Steel" in weaklist:
        emove+=list(set(mymove). intersection(steelmoves))          
    if "Fairy" in weaklist:
        emove+=list(set(mymove). intersection(fairymoves))            
    if "Poison" in weaklist:
        emove+=list(set(mymove). intersection(poisonmoves))        
    if "Fighting" in weaklist:
        emove+=list(set(mymove). intersection(fightingmoves))        
    if "Flying" in weaklist:
        emove+=list(set(mymove). intersection(flyingmoves))        
    if "Bug" in weaklist:
        emove+=list(set(mymove). intersection(bugmoves))        
    if "Psychic" in weaklist:
        emove+=list(set(mymove). intersection(psychicmoves))       
    if "Ghost" in weaklist:
        emove+=list(set(mymove). intersection(ghostmoves))        
    if "Dark" in weaklist:
        emove+=list(set(mymove). intersection(darkmoves))        
    if "Water" in resistlist:
        resmove+=list(set(mymove). intersection(watermoves))
    if "Fire" in resistlist:
        resmove+=list(set(mymove). intersection(firemoves))
    if "Grass" in resistlist:
        resmove+=list(set(mymove). intersection(grassmoves))          
    if "Rock" in resistlist:
        resmove+=list(set(mymove). intersection(rockmoves))     
    if "Ground" in resistlist:
        resmove+=list(set(mymove). intersection(groundmoves)) 
    if "Electric" in resistlist:
        resmove+=list(set(mymove). intersection(electricmoves))              
    if "Ice" in resistlist:
        resmove+=list(set(mymove). intersection(icemoves))
    if "Dragon" in resistlist:
        resmove+=list(set(mymove). intersection(dragonmoves))     
    if "Normal" in resistlist:
        resmove+=list(set(mymove). intersection(normalmoves))     
    if "Steel" in resistlist:
        resmove+=list(set(mymove). intersection(steelmoves))          
    if "Fairy" in resistlist:
        resmove+=list(set(mymove). intersection(fairymoves))            
    if "Poison" in resistlist:
        resmove+=list(set(mymove). intersection(poisonmoves))        
    if "Fighting" in resistlist:
        resmove+=list(set(mymove). intersection(fightingmoves))        
    if "Flying" in resistlist:
        resmove+=list(set(mymove). intersection(flyingmoves))        
    if "Bug" in resistlist:
        resmove+=list(set(mymove). intersection(bugmoves))        
    if "Psychic" in resistlist:
        resmove+=list(set(mymove). intersection(psychicmoves))       
    if "Ghost" in resistlist:
        resmove+=list(set(mymove). intersection(ghostmoves))        
    if "Dark" in resistlist:
        resmove+=list(set(mymove). intersection(darkmoves))                
    #use=None 
    resmove=list(set(resmove)-set(emove)-set(myimmunemove))
    mymove=list(set(mymove)-set(myimmunemove))
    emove=list(set(emove)-set(myimmunemove))
    mystablist=list(set(mystablist)-set(myimmunemove)-set(resmove))
    eheal=list(set(mymove).intersection(healingmoves))
    eprior=list(set(mymove).intersection(priorityatkmoves))
    superduper=list(set(emove).intersection(mystablist))
    if self.item is not None and "Choice" in self.item:
        mymove=list(set(mymove)-set(statusmoves))
        mymove=list(set(mymove)-set(terrainmove))
        mymove=list(set(mymove)-set(weathermoves))
    if self.hp==self.maxhp:
        mymove=list(set(mymove)-set(healingmoves))
    if self.canfakeout is False:
        mymove.remove("Fake Out")
    if len(mtr.hazard)==0:
        if "Defog" in mymove:
            mymove.remove("Defog")       
    if self.choiced is True:
        mymove=list(set(mymove)-set(mymove). intersection(statusmoves))             
    if "Stealth Rock" in otr.hazard:
        if "Stealth Rock" in mymove:
            mymove.remove("Stealth Rock")
    if "Toxic Spikes" in otr.hazard:
        if "Toxic Spikes" in mymove:
            mymove.remove("Toxic Spikes")
    if other.status=="Badly Poisoned" or (other.type1 in ["Steel","Poison"] or other.type2 in ["Steel","Poison"] and self.ability!="Corrosion"):
        if "Toxic" in mymove:
            mymove.remove("Toxic")
    if other.status=="Paralyzed":
        if "Thunder Wave" in mymove:
            mymove.remove("Thunder Wave")         
    if self.spatkb==4:
        if "Tail Glow" in mymove:
            mymove.remove("Tail Glow")             
    
    if other.seeded==True:
        if "Leech Seed" in mymove:
            mymove.remove("Leech Seed")      
    if field.weather=="Sandstorm":
        if "Sandstorm" in mymove:
            mymove.remove("Sandstorm")        
    if field.weather=="Hail":
        if "Hail" in mymove:
            mymove.remove("Hail")        
    if field.weather=="Sunny":
        if "Sunny Day" in mymove:
            mymove.remove("Sunny Day")        
    if field.weather=="Rainy":
        if "Rain Dance" in mymove:
            mymove.remove("Rain Dance")
    if other.atkb<1 and other.status=="Alive":    
        if "Will-O-Wisp" in mymove:    
            use="Will-O-Wisp"
    if self.speed<other.speed and other.status=="Alive":
        if "Thunder Wave" in mymove:
            use="Thunder Wave"
             
    if self.protect!=False:       
        mymove=list(set(mymove)-set(protectmoves))  
    if other.ability in ["Water Absorb","Storm Drain"]:
        mymove=list(set(mymove)-(set(mymove).intersection(watermoves)))
        emove=list(set(emove)-set(watermoves))  
        mystablist=list(set(mystablist)-set(watermoves))
    if other.ability in ["Volt Absorb","Lightning Rod"]:
        mymove=list(set(mymove)-(set(mymove).intersection(electricmoves)))
        emove=list(set(emove)-set(electricmoves))       
        mystablist=list(set(mystablist)-set(electricmoves)) 
    if other.ability=="Flash Fire":       
        mymove=list(set(mymove)-(set(mymove).intersection(firemoves)))
    if other.ability=="Levitate":
        mymove=list(set(mymove)-(set(mymove).intersection(groundmoves)))
        emove=list(set(emove)-set(groundmoves)) 
        mystablist=list(set(mystablist)-set(groundmoves)) 
    if other.status!="Alive":
        mymove=list(set(mymove)-set(statuschangemoves))
    if "Trick Room" in mymove and field.trickroom is False and self.speed<other.speed:
        use="Trick Room"                      
    if self.hp<(self.maxhp/2) and self.speed<other.speed and other.hp!=(other.maxhp*0.3):
        if len(eheal)!=0:
            use=eheal[0]   
    if self.hp<=(self.maxhp/3) and self.speed<=other.speed:         
        if len(eheal)!=0:
            use=eheal[0]
    if len(emove)>0 and len(superduper)==0:
        use=random.choice(emove)
    if len(superduper)>0:
        use= superduper[0]
    if len(mystablist)>0 and len(emove)==0:
        use=random.choice(mystablist)  
    if field.terrain=="Normal":
        tmove=list (set(mymove).intersection(terrainmove))
        if len(tmove)!=0:
            use=tmove[0]
    if self.choiced is False and self.atk>self.spatk and self.atkb<=1 and self.hp>(self.maxhp*0.5) and other.hp>(other.maxhp*0.2):
        boost=list (set(mymove).intersection(atkboost))
        if len(boost)!=0:
            use=boost[0]        
    if self.choiced is False and self.spatk>self.atk and self.spatkb<=1 and self.hp>(self.maxhp*0.5) and other.hp>(other.maxhp*0.2):
        boost=list (set(mymove).intersection(spatkboost))
        if len(boost)!=0:
            use=boost[0]   
    if self.choiced is False and other.atk>other.spatk and "Reflect" in mymove and mtr.reflect is not True:
        use="Reflect"              
    if self.choiced is False and other.spatk>other.atk and "Light Screen" in mymove and mtr.lightscreen is not True:
        use="Light Screen"        
    if self.protect is False and "King's Shield" in mymove and other.hp>=(other.maxhp*0.2):
        use="King's Shield"       
    if self.item is not None and "Sticky Web"  not in otr.hazard and "Choice" not in self.item and other.hp>=(other.maxhp*0.3):
        if "Sticky Web"  in mymove:
            use="Sticky Web"                    
    if self.item is not None and "Stealth Rock"  not in otr.hazard and "Choice" not in self.item and other.hp>=(other.maxhp*0.3):
        if "Stealth Rock"  in mymove:
            use="Stealth Rock"      
    if self.item is not None and "Toxic Spikes"  not in otr.hazard and "Choice" not in self.item and other.hp>=(other.maxhp*0.3):
        if "Toxic Spikes"  in mymove:
            use="Toxic Spikes"  
    if (other.hp<=(other.maxhp*0.20) or other.defb<0.5) and self.speed<other.speed and len(eprior)!=0:
        use=random.choice([eprior[0],emove])             
    if self.item is not None and "Choice" in self.item and self.choiced is False and use is not None and self.dmax is False:
        self.choiced=True
        self.choicedmove=use
    if self.choiced is True and self.dmax is False:
        use=self.choicedmove         
    if use is None or use==[]:
        if len(mymove)==0:
            use=random.choice(self.moves)
        else:
            use=random.choice(mymove)
#    print("=====================")     
#    print(f"{self.name}'s AI says against {other.name}:"    )
#    print("=====================")     
#    print("USABLE MOVES:",mymove)
#    print("EFFECTIVE MOVES:",emove)
#    print("IMMUNE MOVES: ",myimmunemove)
#    print("RESISTED MOVES: ",resmove)
#    print("NON RES STAB MOVES:",mystablist)
#    print("STAB AND EFFECTIVE:",superduper)
#    print("CHOICED MOVE:",self.choicedmove)
#    print("SELECTED MOVE:",use)   
#    print("=====================")             
    return use,emove,superduper       

 
  
def switchAI(self,other,tr,tr2, field):
    sw=[]
    sw+=tr.pokemons
    mo=[self]
    sw=list(set(sw)-set(mo))
    phymon=[]
    spemon=[]
    effmon=[]
    spdefmon=[]
    defmon=[]
    tank=[]
    best=[]
    bestank=[]
    bestoff=[]
    for i in tr.pokemons:
        x=moveAI(i,other,tr,tr2,field)
        y=moveAI(other,i,tr2,tr,field)
        #print(i,x[1],other.name)
        
        if i.defense>250 and i.spdef>250 and i!=self:
            tank.append(i)
        if i.defense>250 and i!=self:
            defmon.append(i)
        if i.spdef>250 and i!=self:
            spdefmon.append(i)
#offense
#200+ spdef          
        if 200<other.spdef:
#Has effective move and oppo doesn't and spatk 270+            
            if len(x[1])!=0 and i!=self and len(y[1])==0 and i.spatk>270:
                bestoff.append(i)
#Has effective move and oppo doesn't and atk 270+                 
        elif 200<other.defense:
            if len(x[1])!=0 and i!=self and len(y[1])==0 and i.atk>270:
                bestoff.append(i)
#Def under 200                
        if other.defense<200:
#Has effective move and oppo doesn't and atk 200+               
            if len(x[1])!=0 and i!=self and len(y[1])==0 and i.atk>200:
                bestoff.append(i)
#spdef under 200                
        elif other.spdef<200:
#Has effective move and oppo doesn't and spatk 270+               
            if len(x[1])!=0 and i!=self and len(y[1])==0 and i.spatk>200:
                bestoff.append(i)
        if len(x[1])!=0 and i!=self and len(y[1])==0 and (i.atk>200 or i.spatk>200):
            effmon.append(i)
        if other.spatk>250:
            if i.spdef>200 and i in effmon and i!=self:
                best.append(i)
        if other.atk>250:
            if i.defense>200 and i in effmon and i!=self:
                best.append(i)
        if other.spatk>other.atk and i in spdefmon and i!=self:
            bestank.append(i)
        if other.atk>other.spatk and i in defmon and i!=self:
            bestank.append(i)        
#    print("=====================")   
#    print(f"Against {other.name}: ")
#    print("=====================")   
#    print("Special Tank:",spdefmon)
#    print("Physical Tank:",defmon)
#    print("Pure Tank:",tank)
#    print("Good Offense Choice:",bestoff)
#    print("Best Tank:",bestank)
#    print("Best Choice:",best)
#    print("=====================")   
    possible=[best,bestank,bestoff,defmon,spdefmon,tank]
    choice=random.choice(tr.pokemons)
    if len(sw)!=0:
        choice=random.choice(sw)
    if len(tr.pokemons)==1:
        choice=(tr.pokemons[0])
    if len(best)==0 and other.hp>(other.maxhp*0.3) and len(bestank)!=0:
        choice=random.choice(bestank)
    if len(bestank)==0 and len(best)==0 and len(bestoff)!=0:
        choice=random.choice(bestoff)        
    if len(best)==1:
        choice=best[0]
    if len(best)>1:
        choice=random.choice(best)                
    return choice,possible  
    
def decision (self,other,tr1,tr2,field):
    action=1
#NATURAL CURE    
    if self.ability=="Natural Cure" and self.status!="Alive" and len(tr1.pokemons)>1:
       action=2
#REGENERATOR       
    if self.ability=="Regenerator" and self.hp<=(self.maxhp/2) and len(tr1.pokemons)>1:
        action=2      
    mons=switchAI(self,other,tr1,tr2,field)[1]
    best=mons[0]
    bestank=mons[1]
    bestoff=mons[2]
    phytank=mons[3]
    spetank=mons[4]
#SUFFECIENT AMOUNT OF MONS    
    if len(tr1.pokemons)>1:
#P1 SLOWER THAN P2        
        if self.speed<other.speed:
#BELOW 40% AND OPPO FAST PHYSICAL SWEEPER
            if self.hp<(self.maxhp*0.4) and other.atk>300 and len(phytank)!=0 and self.defense<250:
                action=2
#BELOW 40% AND OPPO FAST SPECIAL SWEEPER                
            if self.hp<(self.maxhp*0.4) and other.spatk>300 and len(spetank)!=0 and self.spdef<250:
                action=2        
    if other.ability=="Shadow Tag" and "Ghost" not in (self.type1,self.type2):
            action=1    
            
    return action              