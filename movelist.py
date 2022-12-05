#pylint:disable=C0304
#pylint:disable=C0303
#pylint:disable=C0301

class Moves:
    def __init__(self):
        self.zmoves=["Breakneck Blitz","Inferno Overdrive","Gigavolt Havoc","Bloom Doom","Hydro Vortex","Shattered Psyche","Never-ending Nightmare","Tectonic Rage","Continental Crush","Twinkle Tackle","Acid Downpour","Black Hole Eclipse","Supersonic Skystrike","Savage Spin-Out","Corkscrew Crash","All-Out Pummeling","Subzero Slammer","Devastating Drake","10,000,000 Volt Thunderbolt","Catastropika","Pulverizing Pancake","Genesis Supernova"]
        self.contactmoves=["Fire Punch","Ice Punch","Thunder Punch","Horn Drill","Body Slam","Double-Edge","Drill Peck","Submission","Seismic Toss","Strength","Petal Dance","Waterfall","Skull Bash","High Jump Kick","Dizzy Punch","Leech Life","Crabhammer","Slash","Triple Kick","Mach Punch","Outrage","Steel Wing","Return","Dynamic Punch","Megahorn","Rapid Spin","Iron Tail","Cross Chop","Crunch","Extreme Speed","Fake Out","Facade","Superpower","Brick Break","Knock Off","Arm Thrust","Blaze Kick","Needle Arm","Poison Fang","Crush Claw","Meteor Mash","Shadow Punch","Sky Uppercut","Dragon Claw","Poison Tail","Volt Tackle","Leaf Blade","Hammer Arm","Gyro Ball","U-Turn","Close Combat","Assurance","Last Resort","Sucker Punch","Flare Blitz","Force Palm","Poison Jab","Night Slash","Aqua Tail","X-Scissor","Dragon Rush","Drain Punch","Brave Bird","Giga Impact","Bullet Punch","Avalanche","Shadow Claw","Thunder Fang","Ice Fang","Fire Fang","Psychic Fangs","Shadow Sneak","Zen Headbutt","Power Whip","Cross Poison","Iron Head","Grass Knot","Wood Hammer","Aqua Jet","Head Smash","Crash Grip","Shadow Force","Heavy Slam","Foul Play","Acrobatics","Dragon Tail","Wild Charge","Drill Run","Dual Chop","Horn Leech","Sacred Sword","Razor Shell","Heat Crash","Head Charge","Gear Grind","Bolt Strike","V-create","Flying Press","Fell Stinger","Phantom Force","Draining Kiss","Play Rough","Nuzzle","Power-Up Punch","Dragon Ascent","First Impression","Darkest Lariat","Ice Hammer","High Horsepower","Solar Blade","Throat Chop","Anchor Shot","Lunge","Fire Lash","Smart Strike","Trop Kick","Dragon Hanmer","Stomping Tantrum","Accelerock","Liquidation","Spectral Thief","Sunsteel Strike","Zing Zap","Multi-Attack","Plasma Fists","Jaw Lock","Bolt Beak","Double Iron Bash","Fishious Rend","Body Press","Behemoth Blade","Behemoth Bash","Breaking Swipe","Spirit Break","False Surrender","Grassy Glide","Skitter Smack","Flip Turn","Triple Axel","Dual Wingbeat","Wicked Blow","Surging Strikes","Thunderous Kick"]
        self.nondmgmove=["Stealth Rock","Toxic","Toxic Spikes","Sticky Web"]
        self.buffmove=["Iron Defense","Calm Mind","Swords Dance","Shell Smash","Bulk Up","Recover","Roost","Moonlight","Morning Sun","Synthesis","Hail","Rain Dance","Sunny Day","Sandstorm","Trickroom","Dragon Dance","Belly Drum","Nasty Plot","Rest","Coil","Curse","Explosion","Heal Order","Defend Order", "Protect","Spiky Shield","King's Shield"]
        self.normalmoves=["Double Edge","Return","Body Slam","Boomburst","Crush Claw","Crush Grip","Dizzy Punch","Egg Bomb","Explosion","Extreme Speed","Hyper Voice","Facade","Multi-Attack","Strength","Hyper Beam","Giga Impact","Relic Song","Techno Blast","Weather Ball","Breakneck Blitz","Skull Bash","Metronome","Head Charge","Max Strike","Rapid Spin","Pulverizing Pancake","Extreme Evoboost","Hyper Drill","G-Max Replenish","Population Bomb","Slash","Endeavor","Pain Split","Whirlwind","Roar"]
        self.firemoves=["Fire Blast","Flare Blitz","Flamethrower","Magma Storm","Eruption","Lava Plume","Fire Punch","Blaze Kick","Fire Fang","Fire Lash","Heat Crash","Pyro Ball","Raging Fury","Sacred Fire","V-create","Blast Burn","Blue Flare","Fiery Dance","Fusion Flare","Heat Wave","Inferno","Mystical Fire","Searing Shot","Inferno Overdrive","Armor Cannon","Bitter Blade","Max Flare","G-Max Wildfire","G-Max Centiferno","Shell Trap","Torch Song"]
        self.watermoves=["Hydro Pump","Surf","Liquidation","Flip Turn","Hydro Cannon","Muddy Water","Origin Pulse","Scald","Snipe Shot","Sparkling Aria","Steam Eruption","Waterfall","Water Spout","Aqua Jet","Crabhammer","Fishious Rend","Razor Shell","Surging Strikes","Water Shuriken","Wave Crash","Hydro Vortex","Aqua Tail","Max Geyser","G-Max Cannonade","G-Max Hydrosnipe","G-Max Foam Burst","G-Max Stonesurge","G-Max Rapid Flow","Aqua Step","Muddy Water","Oceanic Operetta","Aqua Cutter","Chilling Water","Jet Punch"]
        self.electricmoves=["Thunderbolt","Thunder","Volt Switch","Aura Wheel","Bolt Beak","Bolt Strike","Fusion Bolt","Plasma Fists","Thunder Fang","Thunder Punch","Volt Tackle","Electro Ball","Electroweb","Zap Cannon","Gigavolt Havoc","Wild Charge","Overdrive","Max Lightning","G-Max Volt Crash","G-Max Stun Shock","Discharge","Wildbolt Storm","10,000,000 Volt Thunderbolt","Catastropika","Stoked Sparksurfer","Electro Drift","Parabolic Charge","Double Shock"]
        self.groundmoves=["Earthquake","Earth Power","Scorching Sands","Sandsear Storm","Bone Rush","Drill Run","Headlong Rush","High Horsepower","Land's Wrath","Precipice Baldes","Stomping Tantrum","Thousand Arrows","Thousand Waves","Tectonic Rage","Magnitude","Bulldoze","Max Quake","Sandsear Storm"]
        self.icemoves=["Ice Beam","Blizzard","Icicle Crash","Freeze Shock","Ice Fang","Ice Punch","Ice Shard","Icicle Spear","Mountain Gale","Freeze Dry","Frost Breath","Ice Burn","Subzero Slammer","Glacial Lance","Max Hailstorm","G-Max Resonance","Ice Spinner"]
        self.fightingmoves=["Superpower","Close Combat","High Jump Kick","Aura Sphere","Final Gambit","Focus Blast","Secret Sword","Arm Thrust","Body Press","Brick Break","Drain Punch","Mach Punch","Dynamic Punch","Flying Press","Force Palm","Hammer Arm","Power-up Punch","Sacred Sword","Seismic Toss","Sky Uppercutt","Triple Arrows","All-Out Pummeling","Meteor Assault","Submission","Max Knuckle","G-Max Chi Strike","Thunderous Kick","Collision Course","Counter"]
        self.psychicmoves=["Psychic","Extrasensory","Psychic Fangs","Psycho Cut","Psyshield Bash","Zen Headbutt","Esper Wing","Luster Purge","Mist Ball","Psycho Boost","Psystrike","Stored Power","Shattered Psyche","Prismatic Laser","Expanding Force","Max Mindstorm","Freezing Glare","Genesis Supernova","Light That Burns The Sky","Lumina Crash","Mirror Coat","Twin Beam"]
        self.ghostmoves=["Shadow Ball","Shadow Sneak","Shadow Claw","Spirit Shackle","Bitter Malice","Hex","Infernal Parade","Phantom Force","Shadow Force","Never-ending Nightmare","Moongeist Beam","Astral Barrage","Max Phantasm","Shadow Punch","Destiny Bond","G-Max Terror","Menacing Moonraze Maelstrom","Soul-Stealing 7-Star Strike","Sinister Arrow Raid","Last Respects","Rage Fist"]
        self.fairymoves=["Moonblast","Dazzling Gleam","Play Rough","Spirit Break","Light of Ruin","Twinkle Tackle","Spirit Break","Max Starfall","G-Max Finale","Draining Kiss","Springtide Storm","Let's Snuggle Forever","Guardian of Alola","G-Max Smite","Strange Steam"]
        self.grassmoves=["Giga Drain","Leaf Blade","Chloroblast","Frenzy Plant","Energy Ball","Grass Knot","Leaf Storm","Leaf Tornado","Seed Flare","Solar Beam","Bullet Seed","Drum Beating","Grassy Glide","Horn Leech","Razor Leaf","Seed Bomb","Wood Hammer","Power Whip","Bloom Doom","Petal Dance","Apple Acid","Grav Apple","Max Overgrowth","G-Max Drum Solo","Flower Trick","G-Max Vine Lash"]
        self.rockmoves=["Stone Edge","Accelerock","Diamond Storm","Head Smash","Rock Blast","Rock Slide","Ancient Power","Power Gem","Splintered Stromshards","Continental Crush","Stone Axe","Meteor Beam","Rock Wrecker","Max Rockfall","G-Max Volcalith","Stone Axe"]
        self.darkmoves=["Dark Pulse","Night Slash","Crunch","Night Daze","Snarl","Assurance","Ceaseless Edge","Darkest Lariat","Throat Chop","Foul Play","Knock Off","Hyperspace Fury","Sucker Punch","Wicked Blow","Black Hole Eclipse","False Surrender","Max Darkness","Jaw Lock","G-Max One Blow","Fiery Wrath","Malicious Moonsault","Kowtow Cleave","Ruination","G-Max Snooze"]
        self.dragonmoves=["Draco Meteor","Dragon Pulse","Dragon Claw","Outrage","Core Enforcer","Roar of Time","Special Rend","Devastating Drake","Dragon Energy","Breaking Swipe","Dual Chop","Dragon Darts","Max Wyrmwind","G-Max Depletion","Dynamax Cannon","Eternabeam","Clangorous Soulblaze","Glaive Rush","Clangorous Scales","Order Up","Scale Shot"]
        self.bugmoves=["Megahorn","Pin Missile","Bug Buzz","U-Turn","X-Scissor","Leech Life","Savage Spin-Out","Max Flutterby","G-Max Befuddle","Pounce"]
        self.poisonmoves=["Poison Jab","Sludge Bomb","Cross Poison","Sludge Wave","Dire Claw","Gunk Shot","Belch","Poison Fang","Poison Tail","Venoshock","Acid Downpour","Max Ooze","G-Max Malodor"]
        self.steelmoves=["Flash Cannon","Meteor Mash","Bullet Punch","Steel Beam","Doom Desire","Gyro Ball","Heavy Slam","Iron Head","Iron Tail","Steel Wing","Corkscrew Crash","Sunsteel Strike","Max Steelspike","Behemoth Bash","Behemoth Blade","Searing Sunraze Smash","G-Max Steelsurge","Make It Rain","Double Iron Bash","Gigaton Hammer","Spin Out","G-Max Meltdown","Gear Grind","Anchor Shot"]
        self.flyingmoves=["Brave Bird","Sky Attack","Acrobatics","Beak Blast","Dragon Ascent","Drill Peck","Dual Wingbeat","Supersonic Skystrike","Aeroblast","Hurricane","Oblivion Wing","Air Slash","Max Airstream","Bleakwind Storm","G-Max Wind Rage"]
        self.statusmove=["Sleep Powder","Iron Defense","Calm Mind","Swords Dance","Bulk Up","Recover","Roost","Thunder Wave","Lunar Blessing","Take Heart","Heart Swap","Will-O-Wisp","Moonlight","Synthesis","Morning Sun","Rain Dance","Sunny Day","Hail","Sandstorm","Dark Void","Trick Room","Nasty Plot","Shell Smash","Dragon Dance","Belly Drum","Spore","Hypnosis","Rest","Coil","Curse","Strength Sap","Leech Seed","Protect","Spiky Shield","King's Shield","Heal Order","Defend Order","Grassy Terrain","Electric Terrain","Misty Terrain","Psychic Terrain","Yawn"]   
        self.healingmoves=["Recover","Roost","Synthesis","Morning Sun","Moonlight","Slack Off","Soft-Boiled","Milk Drink","Rest","Lunar Blessing"]
        self.priorityatkmoves=["Aqua Jet","Bullet Punch","Extreme Speed","Sucker Punch","Fake Out","Jet Punch"]
        self.atkboost=["Swords Dance","Bulk Up"]
        self.spatkboost=["Calm Mind","Nasty Plot","Geomancy"]
        self.protectmoves=["Protect","King's Shield","Spiky Shield","Baneful Bunker","Silk Trap"]
        self.terrainmove=["Grassy Terrain","Misty Terrain","Electric Terrain","Psychic Terrain"]
        self.statuschangemoves=["Will-O-Wisp","Toxic","Thunder Wave","Sleep Powder"]
        self.weathermoves=["Rain Dance","Sunny Day","Snowscape","Sandstorm"]
        self.pp5=["Aeroblast","Ancient Power","Armor Cannon","Astral Barrage","Behemoth Bash","Behemoth Blade","Blast Burn","Bleakwind Storm","Blizzard","Blue Flare","Bolt Strike","Burn Up","Burning Jealousy","Chloroblast","Clanging Scales","Clangorous Soul","Close Combat","Collision Course","Cross Chop","Crush Grip","Destiny Bond","Diamond Storm","Doom Desire","Double Iron Bash","Double Shock","Draco Meteor","Dragpn Ascent","Dragon Energy","Dynamax Cannon","Dynamic Punch","Electro Drift","Encore","Endeavor","Eruption","Eternabeam","Explosion","Extreme Speed","Final Gambit","Fire Blast","Fissure","Fleur Cannon","Focus Blast","Freeze Shock","Frenzy Plant","Fusion Bolt","Fusion Flare","Giga Impact","Gigaton Hammer","Glacial Lance","Glaive Rush","Guillotine","Gunk Shot","Gyro Ball","Head Smash","Headlong Rush","Heal Bell","Horn Drill","Hydro Pump","Hydro Cannon","Hyper Beam","Hyper Drill","Hyperspace Fury","Hyperspace Hole","Ice Burn","Inferno","Lash Out","Last Resort","Leaf Storm","Light of Ruin","Luster Purge","Magma Storm","Make It Rain","Meteor Assault","Mind Blown","Mist Ball","Misty Explosion","Moongeist Beam","Moonlight","Morning Sun","Mountain Gale","Overheat","Perish Song","Photon Geyser","Psycho Boost","Pyro Ball","Rain Dance","Roar of Time","Rock Wrecker","Sacred Fire","Sandsear Storm","Searing Shot","Seed Flare","Shadow Force","Sheer Cold","Shell Trap","Sky Attack","Spacial Rend","Spin Out","Springtide Storm","Steam Eruption","Steel Beam","Steel Roller","Stone Edge","Sucker Punch","Sunny Day","Sunsteel Strike","Superpower","Surging Strikes","Synthesis","Technoblast","Trick Room","V-create","Water Spout","Wicked Blow","Wildbolt Storm","Zap Cannon"]
        self.statusmove+=self.nondmgmove+self.buffmove+self.healingmoves
        self.allmove=self.firemoves+self.watermoves+self.electricmoves+self.grassmoves+self.normalmoves+self.darkmoves+self.ghostmoves+self.psychicmoves+self.poisonmoves+self.steelmoves+self.fairymoves+self.bugmoves+self.fightingmoves+self.flyingmoves+self.icemoves+self.rockmoves+self.groundmoves+self.dragonmoves+self.statusmove
typemoves=Moves()