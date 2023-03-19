#pylint:disable=C0304
#pylint:disable=C0303
#pylint:disable=C0301
from hiddenpower import *
class Moves:
    def __init__(self):
        self.premove=["Solar Beam","Meteor Beam","Skull Bash","Geomancy","Phantom Force","Shadow Force","Sky Attack","Ice Burn","Freeze Shock","Solar Blade","Bounce","Focus Punch","Dig","Fly"]
        self.abilityigmoves=["G-Max Fireball","G-Max Hydrosnipe","G-Max Drum Solo","Light That Burns The Sky","Photon Geyser","Moongeist Beam","Sunsteel Strike","Menacing Moonraze Maelstrom","Searing Sunraze Smash"]
        self.windmoves=["Bleakwind Storm","Whirlwind","Blizzard","Heat Wave","Hurricane","Petal Blizzard","Sandsear Storm","Sandstorm","Springtide Storm","Wildbolt Storm","Tailwind","Icy Wind"]
        self.multimove=["Bullet Seed","Rock Blast","Pin Missile","Icicle Spear","Dual Chop","Dual Wingbeat","Arm Thrust","Water Shuriken","Double Iron Bash","Spike Cannon","Triple Axel","Triple Arrows","Triple Kick","Population Bomb","Scale Shot"]
        self.acc95=["Aeroblast","Air Slash","Crush Claw","Diamond Storm","Drill Run","Electroweb","Fire Fang","Fly","Flying Press","Glaciate","High Horsepower","Ice Fang","Icy Wind","Night Daze","Pin Missile","Razor Leaf","Razor Shell","Rock Tomb","Sacred Fire","Snarl","Spacial Rend","Steam Eruption","Thunder Fang","V-create","Triple Dive"]
        self.acc30=["Fissure","Horn Drill","Guillotine","Sheer Cold"]
        self.acc80=["Dragon Rush","Egg Bomb","Iron Tail","Lovely Kiss","Sleep Powder","Cross Chop","Stone Edge","Head Smash","Submission","Magma Storm","Hydro Pump"]
        self.acc50=["Inferno","Zap Cannon","Dynamic Punch"]
        self.acc70=["Blizzard","Focus Blast","Hurricane","Thunder"]
        self.acc90=["Scale Shot","Skitter Smack","Dual Wingbeat","Meteor Beam","Thunder Cage","Aqua Tail","Axe Kick","Belch","Blast Burn","Blaze Kick","Blue Flare","Bolt Strike","Bone Rush","Bounce","Ceaseless Edge","Crabhammer","Draco Meteor","Dragon Tail","Dual Chop","Esper Wing","Eternabeam","Fire Blast","Fleur Cannon","Freeze Shock","Frenzy Plant","Frost Breath","Gear Grind","Giga Impact","Gunk Shot","Hammer Arm","Heat Wave","High Jump Kick","Hydro Cannon","Hyper Beam","Ice Burn","Ice Hammer","Icicle Crash","Leaf Storm","Leaf Tornado","Leech Seed","Light of Ruin","Megahorn","Meteor Mash","Mountain Gale","Muddy Water","Mystical Power","Nature's Madness","Octazooka","Origin Pulse","Precipice Blades","Overheat","Play Rough","Power Whip","Present","Psyshield Bash","Pyro Ball","Raging Fury","Roar of Time","Rock Blast","Rock Slide","Rock Wrecker","Seed Flare","Sky Attack","Sky Upperrcut","Steel Wing","Stone Axe","Super Fang","Swagger","Toxic","Will-O-Wisp","Zen Headbutt","Ruination"]
        self.zmoves=["Breakneck Blitz","Inferno Overdrive","Gigavolt Havoc","Bloom Doom","Hydro Vortex","Shattered Psyche","Never-ending Nightmare","Tectonic Rage","Continental Crush","Twinkle Tackle","Acid Downpour","Black Hole Eclipse","Supersonic Skystrike","Savage Spin-Out","Corkscrew Crash","All-Out Pummeling","Subzero Slammer","Devastating Drake","10,000,000 Volt Thunderbolt","Catastropika","Pulverizing Pancake","Genesis Supernova","Soul-Stealing 7-Star Strike","Clangorous Soulblaze","Splintered Stormshards","Sinister Arrow Raid","Let's Snuggle Forever","Oceanic Operetta","Malicious Moonsault","Searing Sunraze Smash","Menacing Moonraze Maelstrom","Stoked Sparksurfer","Light That Burns The Sky","Extreme Evoboost","Guardian of Alola"]
        self.maxmovelist=["Max Strike","Max Flare","G-Max Wildfire","G-Max Centiferno","Max Geyser","G-Max Cannonade","G-Max Hydrosnipe","G-Max Foam Burst","Max Lightning","G-Max Volt Crash","G-Max Stun Shock","Max Quake","Max Knuckle","G-Max Chi Strike","Max Mindstorm","Max Phantasm","G-Max Terror","Max Starfall","Max Overgrowth","G-Max Drum Solo","G-Max Sweetness","G-Max Tartness","Max Rockfall","Max Darkness","Max Wyrmwind","G-Max Depletion","Max Flutterby","G-Max Befuddle","Max Ooze","Max Steelspike","Max Airstream","G-Max Resonance","G-Max Hailstorm","G-Max Finale","G-Max Volcalith","G-Max Stonesurge","Max Hailstorm","G-Max Cuddle","G-Max Sandblast","G-Max Fireball","G-Max Steelsurge","G-Max Snooze","G-Max Malodor","G-Max Vine Lash","G-Max One Blow","G-Max Rapid Flow","G-Max Wind Rage","G-Max Gold Rush","G-Max Replenish","G-Max Meltdown","G-Max Smite"]
        self.buffmove=["Iron Defense","Calm Mind","Swords Dance","Shell Smash","Bulk Up","Recover","Roost","Moonlight","Morning Sun","Synthesis","Hail","Rain Dance","Sunny Day","Sandstorm","Trickroom","Dragon Dance","Belly Drum","Nasty Plot","Rest","Coil","Curse","Heal Order","Defend Order", "Protect","Spiky Shield","King's Shield","Acid Armor","Amnesia","Aqua Ring","Silk Trap","Heal Bell","Aromatherapy","Cosmic Power","Quiver Dance","Cotton Guard","Electric Terrain","Grassy Terrain","Misty Terrain","Psychic Terrain","Snowscape","Geomancy","Iron Defense","Light Screen","Reflect","Slack Off","Soft-Boiled","Tail Glow","Jungle Healing","Obstract","Growth","Trick Room","Tailwind","Shell Trap","Flail","Substitute","Shed Tail","Explosion","Misty Explosion","Teleport","No Retreat"]
        self.noaccuracy=self.zmoves+["Aerial Ace","Aura Sphere","Defog","False Surrender","Disarming Voice","Flower Trick","Flying Press","Heart Swap","Hyperspace Hole","Hyperspace Fury","Kowtow Cleave","Phantom Force","Roar","Reflect","Light Screen","Aurora Veil","Shadow Punch","Shadow Force","Smart Strike","Spider Web","Struggle", "Vital Throw","Yawn","Whirlwind"]+self.maxmovelist+self.buffmove
        self.soundmoves=["Boomburst","Bug Buzz","Clanging Scales","Clangorous Soul","Clangorous Soulblaze","Disarming Voice","Grass Whistle","Heal Bell","Howl","Hyper Voice","Metal Sound","Noble Roar","Overdrive","Parting Shot","Perish Song","Relic Song","Torch Song","Roar","Shadow Panic","Snarl","Snore","Sparkling Aria"]
        self.prioritymove=["Mach Punch","Bullet Punch","Sucker Punch","Fake Out","Extreme Speed","Protect","Aqua Jet","Shadow Sneak","Accelerock","Ice Shard","Water Shuriken","Spiky Shield","King's Shield","Baneful Bunker","Max Guard","Silk Trap","Jet Punch","Quick Attack","First Impression","Water Shuriken","Vaccum Wave"]
        self.negprioritymove=["Whirlwind","Shell Trap","Counter","Mirror Coat","Roar","Dragon Tail","Teleport","Avalanche"]
        self.bulletmove=["Bullet Seed","Snipe Shot","Armor Cannon","Aura Sphere","Flash Cannon","Spike Cannon","Fleur Cannon","Zap Cannon","Dynamax Cannon","Scale Shot","Ice Shard","Searing Shot","Rock Blast","Pin Missile","Icicle Spear","Pyro Ball","Focus Blast","Mist Ball","Beak Blast","Rock Wrecker","Octazooka","Sludge Bomb","Pollen Puff","Seed Bomb","Weather Ball","Shadow Ball"]
        self.contactmoves=["Fire Punch","Ice Punch","Thunder Punch","Horn Drill","Body Slam","Double-Edge","Drill Peck","Submission","Seismic Toss","Strength","Petal Dance","Waterfall","Skull Bash","High Jump Kick","Dizzy Punch","Leech Life","Crabhammer","Slash","Triple Kick","Mach Punch","Outrage","Steel Wing","Return","Dynamic Punch","Megahorn","Rapid Spin","Iron Tail","Cross Chop","Crunch","Extreme Speed","Fake Out","Facade","Superpower","Brick Break","Knock Off","Arm Thrust","Blaze Kick","Needle Arm","Poison Fang","Crush Claw","Meteor Mash","Shadow Punch","Sky Uppercut","Dragon Claw","Poison Tail","Volt Tackle","Leaf Blade","Hammer Arm","Gyro Ball","U-turn","Close Combat","Assurance","Last Resort","Sucker Punch","Flare Blitz","Force Palm","Poison Jab","Night Slash","Aqua Tail","X-Scissor","Dragon Rush","Drain Punch","Brave Bird","Giga Impact","Bullet Punch","Avalanche","Shadow Claw","Thunder Fang","Ice Fang","Fire Fang","Psychic Fangs","Shadow Sneak","Zen Headbutt","Power Whip","Cross Poison","Iron Head","Grass Knot","Wood Hammer","Aqua Jet","Head Smash","Crash Grip","Shadow Force","Heavy Slam","Foul Play","Acrobatics","Dragon Tail","Wild Charge","Drill Run","Dual Chop","Horn Leech","Sacred Sword","Razor Shell","Heat Crash","Head Charge","Gear Grind","Bolt Strike","V-create","Flying Press","Fell Stinger","Phantom Force","Draining Kiss","Play Rough","Nuzzle","Power-up Punch","Dragon Ascent","First Impression","Darkest Lariat","Ice Hammer","High Horsepower","Solar Blade","Throat Chop","Anchor Shot","Lunge","Fire Lash","Smart Strike","Trop Kick","Dragon Hanmer","Stomping Tantrum","Accelerock","Liquidation","Spectral Thief","Sunsteel Strike","Zing Zap","Multi-Attack","Plasma Fists","Jaw Lock","Bolt Beak","Double Iron Bash","Fishious Rend","Body Press","Behemoth Blade","Behemoth Bash","Breaking Swipe","Spirit Break","False Surrender","Grassy Glide","Skitter Smack","Flip Turn","Triple Axel","Dual Wingbeat","Wicked Blow","Surging Strikes","Thunderous Kick","Quick Attack","Aqua Step","Aqua Cutter","Axe Kick","Bitter Blade","Blazing Torque","Collision Course","Combat Torque","Double Shock","Electro Drift","Gigaton Hammer","Glaive Rush","Hyper Drill","Jet Punch","Ice Spinner","Kowtow Cleave","Last Respects","Lumina Crash","Magical Torque","Mortal Spin","Noxious Torque","Order Up","Pounce","Rage Fist","Raging Bull","Ruination","Spin Out","Trailblaze","Triple Dive","Wicked Torque","Soul Robbery","Dragon Tail"]
        self.nondmgmove=["Stealth Rock","Toxic","Toxic Spikes","Sticky Web"]
        self.normalmoves=["Double-Edge","Return","Body Slam","Boomburst","Crush Claw","Crush Grip","Dizzy Punch","Egg Bomb","Explosion","Extreme Speed","Hyper Voice","Facade","Multi-Attack","Strength","Hyper Beam","Giga Impact","Relic Song","Techno Blast","Weather Ball","Breakneck Blitz","Skull Bash","Metronome","Head Charge","Max Strike","Rapid Spin","Pulverizing Pancake","Extreme Evoboost","Hyper Drill","G-Max Replenish","Population Bomb","Slash","Endeavor","Pain Split","Quick Attack","G-Max Gold Rush","G-Max Cuddle","Last Resort","Hidden Power","Present","Assist","Tri Attack","Fake Out","Horn Drill","Guillotine","Raging Bull","Tail Slap","Tera Blast","Revelation Dance","Super Fang"]
        self.firemoves=["Fire Blast","Flare Blitz","Flamethrower","Magma Storm","Eruption","Lava Plume","Fire Punch","Blaze Kick","Fire Fang","Fire Lash","Heat Crash","Pyro Ball","Raging Fury","Sacred Fire","V-create","Blast Burn","Blue Flare","Fiery Dance","Fusion Flare","Heat Wave","Inferno","Mystical Fire","Searing Shot","Inferno Overdrive","Armor Cannon","Bitter Blade","Max Flare","G-Max Wildfire","G-Max Centiferno","Shell Trap","Torch Song","Blazing Torque","G-Max Fireball","Overheat","Mind Blown","Flame Charge"]
        self.watermoves=["Hydro Pump","Surf","Liquidation","Flip Turn","Hydro Cannon","Muddy Water","Origin Pulse","Scald","Snipe Shot","Sparkling Aria","Steam Eruption","Waterfall","Water Spout","Aqua Jet","Crabhammer","Fishious Rend","Razor Shell","Surging Strikes","Water Shuriken","Wave Crash","Hydro Vortex","Aqua Tail","Max Geyser","G-Max Cannonade","G-Max Hydrosnipe","G-Max Foam Burst","G-Max Stonesurge","G-Max Rapid Flow","Aqua Step","Muddy Water","Oceanic Operetta","Aqua Cutter","Chilling Water","Jet Punch","Octazooka","Triple Dive","Hydro Steam"]
        self.electricmoves=["Thunderbolt","Thunder","Volt Switch","Aura Wheel","Bolt Beak","Bolt Strike","Fusion Bolt","Plasma Fists","Thunder Fang","Thunder Punch","Volt Tackle","Electro Ball","Electroweb","Zap Cannon","Gigavolt Havoc","Wild Charge","Overdrive","Max Lightning","G-Max Volt Crash","G-Max Stun Shock","Discharge","Wildbolt Storm","10,000,000 Volt Thunderbolt","Catastropika","Stoked Sparksurfer","Electro Drift","Parabolic Charge","Double Shock","Nuzzle","Thunder Cage","Rising Voltage","Zing Zap"]
        self.groundmoves=["Earthquake","Earth Power","Scorching Sands","Sandsear Storm","Bone Rush","Drill Run","Headlong Rush","High Horsepower","Land's Wrath","Precipice Blades","Stomping Tantrum","Thousand Arrows","Thousand Waves","Tectonic Rage","Magnitude","Bulldoze","Max Quake","Sandsear Storm","G-Max Sandblast","Fissure","Dig"]
        self.icemoves=["Ice Beam","Blizzard","Icicle Crash","Freeze Shock","Ice Fang","Ice Punch","Ice Shard","Icicle Spear","Mountain Gale","Freeze-Dry","Frost Breath","Ice Burn","Subzero Slammer","Glacial Lance","Max Hailstorm","G-Max Resonance","Ice Spinner","Ice Hammer","Glaciate","Triple Axel","Icy Wind","Avalanche","Sheer Cold"]
        self.fightingmoves=["Superpower","Close Combat","High Jump Kick","Aura Sphere","Final Gambit","Focus Blast","Secret Sword","Arm Thrust","Body Press","Brick Break","Drain Punch","Mach Punch","Dynamic Punch","Flying Press","Force Palm","Hammer Arm","Power-up Punch","Sacred Sword","Seismic Toss","Sky Uppercutt","Triple Arrows","All-Out Pummeling","Meteor Assault","Submission","Max Knuckle","G-Max Chi Strike","Thunderous Kick","Collision Course","Counter","Combat Torque","Smelling Salts","Low Kick","Triple Kick","Cross Chop","Sky Uppercut","Focus Punch","Axe Kick","Reversal"]
        self.psychicmoves=["Psychic","Extrasensory","Psychic Fangs","Psycho Cut","Psyshield Bash","Zen Headbutt","Esper Wing","Luster Purge","Mist Ball","Psycho Boost","Psystrike","Stored Power","Shattered Psyche","Prismatic Laser","Expanding Force","Max Mindstorm","Freezing Glare","Genesis Supernova","Light That Burns The Sky","Lumina Crash","Mirror Coat","Twin Beam","Dream Eater","Soul Robbery","G-Max Gravitas","Psyshock","Psyblade","Future Sight","Mystical Power","Photon Geyser"]
        self.ghostmoves=["Shadow Ball","Shadow Sneak","Shadow Claw","Spirit Shackle","Bitter Malice","Hex","Infernal Parade","Phantom Force","Shadow Force","Never-ending Nightmare","Moongeist Beam","Astral Barrage","Max Phantasm","Shadow Punch","G-Max Terror","Menacing Moonraze Maelstrom","Soul-Stealing 7-Star Strike","Sinister Arrow Raid","Last Respects","Rage Fist","Shadow Bone","Night Shade","Spectral Thief"]
        self.fairymoves=["Moonblast","Dazzling Gleam","Play Rough","Spirit Break","Light of Ruin","Twinkle Tackle","Spirit Break","Max Starfall","G-Max Finale","Draining Kiss","Springtide Storm","Let's Snuggle Forever","Guardian of Alola","G-Max Smite","Strange Steam","Fleur Cannon","Misty Explosion","Magical Torque"]
        self.grassmoves=["Giga Drain","Leaf Blade","Chloroblast","Frenzy Plant","Energy Ball","Grass Knot","Leaf Storm","Leaf Tornado","Seed Flare","Solar Beam","Bullet Seed","Drum Beating","Grassy Glide","Horn Leech","Razor Leaf","Seed Bomb","Wood Hammer","Power Whip","Bloom Doom","Petal Dance","Apple Acid","Grav Apple","Max Overgrowth","G-Max Drum Solo","Flower Trick","G-Max Vine Lash","Petal Blizzard","Needle Arm","Solar Blade","Trailblaze"]
        self.rockmoves=["Stone Edge","Accelerock","Diamond Storm","Head Smash","Rock Blast","Rock Slide","Ancient Power","Power Gem","Splintered Stormshards","Continental Crush","Stone Axe","Meteor Beam","Rock Wrecker","Max Rockfall","G-Max Volcalith","Stone Axe","Salt Cure","Rock Tomb"]
        self.darkmoves=["Dark Pulse","Night Slash","Crunch","Night Daze","Snarl","Assurance","Ceaseless Edge","Darkest Lariat","Throat Chop","Foul Play","Knock Off","Hyperspace Fury","Sucker Punch","Wicked Blow","Black Hole Eclipse","False Surrender","Max Darkness","Jaw Lock","G-Max One Blow","Fiery Wrath","Malicious Moonsault","Kowtow Cleave","Ruination","G-Max Snooze","Wicked Torque","Dark Hole"]
        self.dragonmoves=["Draco Meteor","Dragon Pulse","Dragon Claw","Outrage","Core Enforcer","Roar of Time","Special Rend","Devastating Drake","Dragon Energy","Breaking Swipe","Dual Chop","Dragon Darts","Max Wyrmwind","G-Max Depletion","Dynamax Cannon","Eternabeam","Clangorous Soulblaze","Glaive Rush","Clangorous Scales","Order Up","Scale Shot","Draco Barrage","Dragon Tail","Dragon Rush","Dragon Hammer"]
        self.bugmoves=["Megahorn","Pin Missile","Bug Buzz","U-turn","X-Scissor","Leech Life","Savage Spin-Out","Max Flutterby","G-Max Befuddle","Pounce","Lunge","First Impression","Skitter Smack","Signal Beam","Attack Order","Pollen Puff"]
        self.poisonmoves=["Poison Jab","Sludge Bomb","Cross Poison","Sludge Wave","Dire Claw","Gunk Shot","Belch","Poison Fang","Poison Tail","Venoshock","Acid Downpour","Max Ooze","G-Max Malodor","Noxious Torque","Acid Spray","Barb Barrage","Mortal Spin","Shell Side Arm"]
        self.steelmoves=["Flash Cannon","Meteor Mash","Bullet Punch","Steel Beam","Doom Desire","Gyro Ball","Heavy Slam","Iron Head","Iron Tail","Steel Wing","Corkscrew Crash","Sunsteel Strike","Max Steelspike","Behemoth Bash","Behemoth Blade","Searing Sunraze Smash","G-Max Steelsurge","Make It Rain","Double Iron Bash","Gigaton Hammer","Spin Out","G-Max Meltdown","Gear Grind","Anchor Shot","Smart Strike"]
        self.flyingmoves=["Brave Bird","Sky Attack","Acrobatics","Beak Blast","Dragon Ascent","Drill Peck","Dual Wingbeat","Supersonic Skystrike","Aeroblast","Hurricane","Oblivion Wing","Air Slash","Max Airstream","Bleakwind Storm","G-Max Wind Rage","Sonic Slash","Aerial Ace","Bounce","Fly"]
        self.statusmove=["Sleep Powder","Iron Defense","Calm Mind","Swords Dance","Bulk Up","Recover","Roost","Thunder Wave","Lunar Blessing","Take Heart","Heart Swap","Will-O-Wisp","Moonlight","Synthesis","Morning Sun","Rain Dance","Sunny Day","Hail","Sandstorm","Dark Void","Trick Room","Nasty Plot","Shell Smash","Dragon Dance","Belly Drum","Spore","Hypnosis","Rest","Coil","Curse","Strength Sap","Leech Seed","Protect","Spiky Shield","King's Shield","Heal Order","Defend Order","Grassy Terrain","Electric Terrain","Misty Terrain","Psychic Terrain","Yawn","Doodle","Cosmic Power","Charm","Chilly Reception","Amnesia","Aromatherapy","Wish","Quiver Dance","Glare","Haze","Healing Bell","Light Screen","Reflect","Acid Armor","Agility","Aqua Ring","Autotomize","Cotton Guard","Corrosive Gas","Encore","Forest's Curse","Soak","Magic Powder","Trick-or-Treat","Iron Defense","Metronome","Pain Split","Growth","Destiny Bond","Shore Up","Aurora Veil","Max Guard","Shell Trap","Taunt","Encore","Toxic","Spikes","Psycho Shift","Barrier","Healing Wish","Lunar Dance","Acupressure","Me First","Lovely Kiss","Perish Song","Feather Dance","Fake Tears","Swagger","Trick","Fillet Away","Parting Shot","Shelter","Toxic Threads","Victory Dance","Spicy Extract","Eerie Spell","Substitute","Shed Tail","Recycle","Defog","Double Team","Minimize","Lock-On","Roar","Whirlwind","Transform","Court Change","Teleport","No Retreat","Smokescreen","Sand Attack","Clangorous Soul","Eerie Impulse"]
        self.healingmoves=["Recover","Roost","Synthesis","Morning Sun","Moonlight","Slack Off","Soft-Boiled","Milk Drink","Rest","Lunar Blessing","Giga Drain","Drain Punch","Jungle Healing","Pain Split","Wish","Bitter Blade","Draining Kiss","Horn Leech","Leech Life","Parabolic Charge","Oblivion Wing","Shore Up"]
        self.priorityatkmoves=["Aqua Jet","Bullet Punch","Extreme Speed","Sucker Punch","Fake Out","Jet Punch","Quick Attack","First Impression","Fake Out"]
        self.atkboost=["Swords Dance","Bulk Up","Fillet Away","Dragon Dance","Belly Drum","Clangorous Soul","Coil","Curse","Growth","Hone Claws","Howl","No Retreat","Meditate","Power-up Punch","Shell Smash","Victory Dance","Shift Gear","Tidy Up"]
        self.spatkboost=["Calm Mind","Nasty Plot","Geomancy","Torch Song","Shell Smash","Quiver Dance","Growth","Meteor Beam","Mystical Power","No Retreat","Tail Glow","Take Heart"]
        self.protectmoves=["Protect","King's Shield","Spiky Shield","Baneful Bunker","Silk Trap","Obstruct"]
        self.terrainmove=["Grassy Terrain","Misty Terrain","Electric Terrain","Psychic Terrain"]
        self.statuschangemoves=["Will-O-Wisp","Toxic","Thunder Wave","Sleep Powder"]
        self.weathermoves=["Rain Dance","Sunny Day","Snowscape","Sandstorm"]
        self.pp15=["Acrobatics","Attack Order","Body Slam","Brave Bird","Brick Break","Crunch","Double-Edge","Dragon Claw","Dual Chop","Fire Fang","Fire Punch","Flail","Flare Blitz","Foul Play","Gear Grind","Head Charge","Ice Fang","Hyper Fang","Ice Punch","Iron Head","Iron Tail","Leaf Blade","Needle Arm","Night Slash","Petal Blizzard","Poison Fang","Present","Rock Tomb","Seed Bomb","Shadow Claw","Sky Uppercut","Spike Cannon","Strength","Thunder Fang","Thunder Punch","Volt Tackle","Waterfall","Wild Charge","Wood Hammer","X-Scissor","Zen Headbutt","Beak Blast","Dragon Hammer","Fire Lash","Lunge","Throat Chop","Trop Kick","Plasma Fists","Snap Trap","Breaking Swipe","Spirit Break","Shadow Ball","Barb Barrage","Bitter Malice","Dire Claw","Infernal Parade","Stone Axe","Triple Arrows","Sacred Sword","Hidden Power","Signal Beam","Dark Pulse","Flamethrower","Spore","Sleep Powder","Snipe Shot","Icy Wind"]
        self.pp10=["Aqua Tail","Assurance","Avalanche","Blaze Kick","Bone Rush","Bonemerang","Circle Throw","Crabhammer","Crush Claw","Dizzy Punch","Double Hit","Dragon Rush","Dragon Tail","Drain Punch","Earthquake","Egg Bomb","Fake Out","Flying Press","Force Palm","Hammer Arm","Heat Crash","High Jump Kick","Land's Wrath","Leech Life","Megahorn","Metal Burst","Meteor Mash","Play Rough","Power Whip","Power-up Punch","Razor Shell","Rock Blast","Rock Slide","Smelling Salts","Storm Throw","Super Fang","Triple Kick","Vital Throw","Precipice Blades","Darkest Lariat","First Impression","High Horsepower","Ice Hammer","Liquidation","Multi-Attack","Psychic Fangs","Shadow Bone","Smart Strike","Spectral Thief","Spirit Shackle","Stomping Tantrum","Zing Zap","Jaw Lock","Dragon Darts","Bolt Beak","Fishious Rend","Body Press","Drum Beating","Aura Wheel","Grav Apple","False Surrender","Skitter Smack","Triple Axel","Dual Wingbeat","Thunderous Kick","Aqua Step","Axe Kick","Bitter Blade","Blazing Torque","Chilly Reception","Combat Torque","Doodle","Fillet Away","Flower Trick","Kowtow Cleave","Last Respects","Lumina Crash","Magical Torque","Noxious Torque","Order Up","Population Bomb","Rage Fist","Raging Bull","Ruination","Shed Tail","Silk Trap","Snowscape","Tidy Up","Torch Song","Triple Dive","Twin Beam","Wicked Torque","Psychic","Protect","Toxic","Dark Void","Stored Power","Weather Ball","Baneful Bunker","Esper Wing","Freezing Glare","Jungle Healing","Lunar Blessing","Obstruct","Mystical Power","Psyshield Bash","Shelter","Take Heart","Thunder Cage","Victory Dance","Wave Crash","Giga Drain","Ice Beam","Earth Power","Belch","Thunder","Roost","Slack Off","Recover","Icicle Crash","Sludge Bomb","Shell Side Arm","Mystical Fire","Judgement","Multi-Attack"]
        self.pp5=["Aeroblast","Ancient Power","Armor Cannon","Astral Barrage","Behemoth Bash","Behemoth Blade","Blast Burn","Bleakwind Storm","Blizzard","Blue Flare","Bolt Strike","Burn Up","Burning Jealousy","Chloroblast","Clanging Scales","Clangorous Soul","Close Combat","Collision Course","Cross Chop","Crush Grip","Destiny Bond","Diamond Storm","Doom Desire","Double Iron Bash","Double Shock","Draco Meteor","Dragpn Ascent","Dragon Energy","Dynamax Cannon","Dynamic Punch","Electro Drift","Encore","Endeavor","Eruption","Eternabeam","Explosion","Extreme Speed","Final Gambit","Fire Blast","Fissure","Fleur Cannon","Focus Blast","Frenzy Plant","Fusion Bolt","Fusion Flare","Giga Impact","Gigaton Hammer","Glacial Lance","Glaive Rush","Guillotine","Gunk Shot","Gyro Ball","Head Smash","Headlong Rush","Heal Bell","Horn Drill","Hydro Pump","Hydro Cannon","Hyper Beam","Hyper Drill","Hyperspace Fury","Hyperspace Hole","Inferno","Lash Out","Last Resort","Leaf Storm","Light of Ruin","Luster Purge","Magma Storm","Make It Rain","Meteor Assault","Mind Blown","Mist Ball","Misty Explosion","Moongeist Beam","Moonlight","Morning Sun","Mountain Gale","Overheat","Perish Song","Photon Geyser","Psycho Boost","Pyro Ball","Rain Dance","Roar of Time","Rock Wrecker","Sacred Fire","Sandsear Storm","Searing Shot","Seed Flare","Sheer Cold","Spacial Rend","Spin Out","Springtide Storm","Steam Eruption","Steel Beam","Steel Roller","Stone Edge","Sucker Punch","Sunny Day","Sunsteel Strike","Superpower","Surging Strikes","Synthesis","Technoblast","Trick Room","V-create","Water Spout","Wicked Blow","Wildbolt Storm","Zap Cannon","Dark Hole","Armor Cannon","Collision Course","Double Shock","Electro Drift","Gigaton Hammer","Glaive Rush","Hyper Drill","Make It Rain","Spin Out","Strength Sap","Sucker Punch","Techno Blast"]
        self.statusmove+=self.nondmgmove+self.buffmove+self.healingmoves
        self.allmove=self.firemoves+self.watermoves+self.electricmoves+self.grassmoves+self.normalmoves+self.darkmoves+self.ghostmoves+self.psychicmoves+self.poisonmoves+self.steelmoves+self.fairymoves+self.bugmoves+self.fightingmoves+self.flyingmoves+self.icemoves+self.rockmoves+self.groundmoves+self.dragonmoves+self.statusmove+["Struggle"]
    def hpselect(self,mon):
            x=hidp(mon.hpiv,mon.atkiv,mon.defiv,mon.spatkiv,mon.spdefiv,mon.speediv)
            type=x[0]
            if "Dragon" in (mon.maxiv,type):
                self.dragonmoves+=["Hidden Power"]
            if "Psychic" in (mon.maxiv,type):
                self.psychicmoves+=["Hidden Power"]
            if "Ghost" in (mon.maxiv,type):
                self.ghostmoves+=["Hidden Power"]
            if "Normal" in (mon.maxiv,type):
                self.normalmoves+=["Hidden Power"]
            if "Bug" in (mon.maxiv,type):
                self.bugmoves+=["Hidden Power"]
            if "Steel" in (mon.maxiv,type):
                self.steelmoves+=["Hidden Power"]
            if "Ice" in (mon.maxiv,type):
                self.icemoves+=["Hidden Power"]
            if "Fighting" in (mon.maxiv,type):
                self.fightingmoves+=["Hidden Power"]
            if "Dark" in (mon.maxiv,type):
                self.darkmoves+=["Hidden Power"]
            if "Fairy" in (mon.maxiv,type):
                self.fairymoves+=["Hidden Power"]
            if "Flying" in (mon.maxiv,type):
                self.flyingmoves+=["Hidden Power"]
            if "Poison" in (mon.maxiv,type):
                self.poisonmoves+=["Hidden Power"]
            if "Ground" in (mon.maxiv,type):
                self.groundmoves+=["Hidden Power"]
            if "Rock" in (mon.maxiv,type):
                self.rockmoves+=["Hidden Power"]
            if "Grass" in (mon.maxiv,type):    
                self.grassmoves+=["Hidden Power"]
            if "Electric" in (mon.maxiv,type):
                self.electricmoves+=["Hidden Power"]
            if "Water" in (mon.maxiv,type):
                self.watermoves+=["Hidden Power"]
            if "Fire" in (mon.maxiv,type):
                self.firemoves+=["Hidden Power"]
    def weatherselect(self,mon,field):    
        if field.weather in ["Sandstorm"]:
            self.rockmoves+=["Weather Ball"] 
        if field.weather in ["Hail","Snowstorm"]:
            self.icemoves+=["Weather Ball"]  
        if field.weather in ["Rainy","Primordial Sea"]:
            self.watermoves+=["Weather Ball"] 
        if field.weather in ["Sunny","Desolate Land"]:
            self.firemoves+=["Weather Ball"]
        else:
            self.normalmoves+=["Weather Ball"]
    def teraselect(self,mon):
            if mon.tera=="Dragon":
                self.dragonmoves+=["Tera Blast"]
            if mon.tera=="Psychic":
                self.psychicmoves+=["Tera Blast"]
            if mon.tera=="Ghost":
                self.ghostmoves+=["Tera Blast"]
            if mon.tera=="Normal":
                self.normalmoves+=["Tera Blast"]
            if mon.tera=="Bug":
                self.bugmoves+=["Tera Blast"]
            if mon.tera=="Steel":
                self.steelmoves+=["Tera Blast"]
            if mon.tera=="Ice":
                self.icemoves+=["Tera Blast"]
            if mon.tera=="Fighting":
                self.fightingmoves+=["Tera Blast"]
            if mon.tera=="Dark":
                self.darkmoves+=["Tera Blast"]
            if mon.tera=="Fairy":
                self.fairymoves+=["Tera Blast"]
            if mon.tera=="Flying":
                self.flyingmoves+=["Tera Blast"]
            if mon.tera=="Poison":
                self.poisonmoves+=["Tera Blast"]
            if mon.tera=="Ground":
                self.groundmoves+=["Tera Blast"]
            if mon.tera=="Rock":
                self.rockmoves+=["Tera Blast"]
            if mon.tera=="Grass":
                self.grassmoves+=["Tera Blast"]
            if mon.tera=="Electric":
                self.electricmoves+=["Tera Blast"]
            if mon.tera=="Water":
                self.watermoves+=["Tera Blast"]
            if mon.tera=="Fire":
                self.firemoves+=["Tera Blast"]
            else:
                self.normalmoves+=["Tera Blast"]
    def teraselect(self,mon):
            if mon.type1=="Dragon":
                self.dragonmoves+=["Judgement","Multi-Attack"]
            if mon.type1=="Psychic":
                self.psychicmoves+=["Judgement","Multi-Attack"]
            if mon.type1=="Ghost":
                self.ghostmoves+=["Judgement","Multi-Attack"]
            if mon.type1=="Normal":
                self.normalmoves+=["Judgement","Multi-Attack"]
            if mon.type1=="Bug":
                self.bugmoves+=["Judgement","Multi-Attack"]
            if mon.type1=="Steel":
                self.steelmoves+=["Judgement","Multi-Attack"]
            if mon.type1=="Ice":
                self.icemoves+=["Judgement","Multi-Attack"]
            if mon.type1=="Fighting":
                self.fightingmoves+=["Judgement","Multi-Attack"]
            if mon.type1=="Dark":
                self.darkmoves+=["Judgement","Multi-Attack"]
            if mon.type1=="Fairy":
                self.fairymoves+=["Judgement","Multi-Attack"]
            if mon.type1=="Flying":
                self.flyingmoves+=["Judgement","Multi-Attack"]
            if mon.type1=="Poison":
                self.poisonmoves+=["Judgement","Multi-Attack"]
            if mon.type1=="Ground":
                self.groundmoves+=["Judgement","Multi-Attack"]
            if mon.type1=="Rock":
                self.rockmoves+=["Judgement","Multi-Attack"]
            if mon.type1=="Grass":
                self.grassmoves+=["Judgement","Multi-Attack"]
            if mon.type1=="Electric":
                self.electricmoves+=["Judgement","Multi-Attack"]
            if mon.type1=="Water":
                self.watermoves+=["Judgement","Multi-Attack"]
            if mon.type1=="Fire":
                self.firemoves+=["Judgement","Multi-Attack"]
            else:
                self.normalmoves+=["Judgement","Multi-Attack"]                
typemoves=Moves()
