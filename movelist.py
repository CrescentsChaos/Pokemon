#pylint:disable=C0304
#pylint:disable=C0303
#pylint:disable=C0301
import random
class Moves:
    def __init__(self):
        self.thawmove=["Flame Wheel","Sacred Fire","Flare Blitz","Fusion Flare","Scald","Steam Eruption","Burn Up","Pyro Ball","Scorching Sands"]
        self.physicalmoves=['Attack Order',"Mighty Cleave","Supercell Slam","Temper Flare","Hard Press","Beat Up","Vine Whip","Ivy Cudgel","Upper Hand","Freeze Shock","Double-Edge","Return","Body Slam","Crush Claw","Crush Grip","Dizzy Punch","Explosion","Extreme Speed","Facade","Multi-Attack","Strength","Giga Impact","Skull Bash","Head Charge","Max Strike","Rapid Spin","Hyper Drill","Population Bomb","Slash","Endeavor","Pain Split","Quick Attack","Last Resort","Present","Tri Attack","Fake Out","Horn Drill","Guillotine","Raging Bull","Tail Slap","Super Fang","Thrash","Flail","Feint","Judgement","Double Hit","Flare Blitz","Fire Punch","Blaze Kick","Fire Fang","Fire Lash","Heat Crash","Pyro Ball","Raging Fury","Bitter Blade","Flame Charge","Liquidation","Flip Turn","Waterfall","Crabhammer","Fishious Rend","Razor Shell","Surging Strikes","Water Shuriken","Wave Crash","Aqua Tail","Aqua Step","Aqua Cutter","Jet Punch","Octazooka","Triple Dive","Dive","Aqua Fang","Volt Switch","Aura Wheel","Bolt Beak","Bolt Strike","Fusion Bolt","Plasma Fists","Thunder Fang","Thunder Punch","Volt Tackle","Wild Charge","Overdrive","Electro Drift","Double Shock","Nuzzle","Zing Zap","Earthquake","Bone Rush","Drill Run","Headlong Rush","High Horsepower","Land's Wrath","Precipice Blades","Stomping Tantrum","Thousand Arrows","Thousand Waves","Magnitude","Bulldoze","Fissure","Dig","Bonemerang","Icicle Crash","Ice Fang","Ice Punch","Ice Shard","Icicle Spear","Mountain Gale","Glacial Lance","Ice Spinner","Ice Hammer","Triple Axel","Avalanche","Superpower","Close Combat","High Jump Kick","Final Gambit","Arm Thrust","Body Press","Brick Break","Drain Punch","Mach Punch","Dynamic Punch","Flying Press","Force Palm","Hammer Arm","Power-Up Punch","Sacred Sword","Seismic Toss","Sky Uppercutt","Triple Arrows","Meteor Assault","Submission","Thunderous Kick","Collision Course","Counter","Combat Torque","Smelling Salts","Low Kick","Triple Kick","Cross Chop","Sky Uppercut","Focus Punch","Axe Kick","Reversal","Storm Throw","Psychic Fangs","Psycho Cut","Psyshield Bash","Zen Headbutt","Psyblade","Shadow Sneak","Shadow Claw","Spirit Shackle","Bitter Malice","Phantom Force","Shadow Force","Shadow Punch","Last Respects","Rage Fist","Shadow Bone","Spectral Thief","Poltergeist","Play Rough","Spirit Break","Magical Torque","Leaf Blade","Bullet Seed","Drum Beating","Grassy Glide","Horn Leech","Razor Leaf","Seed Bomb","Wood Hammer","Power Whip","Grav Apple","Needle Arm","Solar Blade","Trailblaze","Trop Kick","Stone Edge","Accelerock","Head Smash","Rock Blast","Rock Slide","Stone Axe","Rock Wrecker","Rock Tomb","Night Slash","Crunch","Assurance","Ceaseless Edge","Darkest Lariat","Throat Chop","Foul Play","Knock Off","Hyperspace Fury","Sucker Punch","Wicked Blow","False Surrender","Kowtow Cleave","Wicked Torque","Power Trip","Payback","Dragon Claw","Outrage","Breaking Swipe","Dual Chop","Dragon Darts","Order Up","Scale Shot","Draco Barrage","Dragon Tail","Dragon Rush","Dragon Hammer","Megahorn","Pin Missile","U-turn","X-Scissor","Leech Life","Pounce","Lunge","First Impression","Skitter Smack","Fell Stinger","Poison Jab","Cross Poison","Dire Claw","Gunk Shot","Belch","Poison Fang","Poison Tail","Barb Barrage","Mortal Spin","Shell Side Arm","Meteor Mash","Bullet Punch","Doom Desire","Gyro Ball","Heavy Slam","Iron Head","Iron Tail","Steel Wing","Behemoth Bash","Behemoth Blade","Double Iron Bash","Gigaton Hammer","Spin Out","Gear Grind","Anchor Shot","Smart Strike","Brave Bird","Sky Attack","Acrobatics","Beak Blast","Dragon Ascent","Drill Peck","Dual Wingbeat","Sonic Slash","Aerial Ace","Bounce","Fly","Razor Wind","Deathroll"]
        self.powdermoves=["Cotton Spore","Magic Powder","Poison Powder","Powder","Rage Powder","Sleep Powder","Spore","Stun Spore"]
        self.premove=["Solar Beam","Meteor Beam","Skull Bash","Geomancy","Phantom Force","Shadow Force","Sky Attack","Ice Burn","Freeze Shock","Solar Blade","Bounce","Focus Punch","Dig","Fly","Dive","Razor Wind","Electro Shot"]
        self.abilityigmoves=["G-Max Fireball","G-Max Hydrosnipe","G-Max Drum Solo","Light That Burns The Sky","Photon Geyser","Moongeist Beam","Sunsteel Strike","Menacing Moonraze Maelstrom","Searing Sunraze Smash","Core Enforcer"]
        self.windmoves=["Bleakwind Storm","Whirlwind","Blizzard","Heat Wave","Hurricane","Petal Blizzard","Sandsear Storm","Sandstorm","Springtide Storm","Wildbolt Storm","Tailwind","Icy Wind"]
        self.multimove=["Bullet Seed","Rock Blast","Pin Missile","Icicle Spear","Dual Chop","Dual Wingbeat","Arm Thrust","Water Shuriken","Double Iron Bash","Spike Cannon","Triple Axel","Triple Arrows","Triple Kick","Population Bomb","Scale Shot","Double Hit","Bonemerang","Deathroll"]
        self.acc95=["Supercell Slam","Aeroblast","Air Slash","Crush Claw","Diamond Storm","Drill Run","Electroweb","Fire Fang","Fly","Flying Press","Glaciate","High Horsepower","Ice Fang","Icy Wind","Night Daze","Pin Missile","Razor Leaf","Razor Shell","Rock Tomb","Sacred Fire","Snarl","Spacial Rend","Steam Eruption","Thunder Fang","V-create","Triple Dive"]
        self.acc30=["Fissure","Horn Drill","Guillotine","Sheer Cold"]
        self.acc80=["Dragon Rush","Egg Bomb","Iron Tail","Lovely Kiss","Sleep Powder","Cross Chop","Stone Edge","Head Smash","Submission","Magma Storm","Hydro Pump"]
        self.acc50=["Inferno","Zap Cannon","Dynamic Punch"]
        self.acc70=["Blizzard","Focus Blast","Hurricane","Thunder"]
        self.acc90=["Poltergeist","Scale Shot","Skitter Smack","Dual Wingbeat","Meteor Beam","Thunder Cage","Aqua Tail","Axe Kick","Belch","Blast Burn","Blaze Kick","Blue Flare","Bolt Strike","Bone Rush","Bounce","Ceaseless Edge","Crabhammer","Draco Meteor","Dragon Tail","Dual Chop","Esper Wing","Eternabeam","Fire Blast","Fleur Cannon","Freeze Shock","Frenzy Plant","Frost Breath","Gear Grind","Giga Impact","Gunk Shot","Hammer Arm","Heat Wave","High Jump Kick","Hydro Cannon","Hyper Beam","Ice Burn","Ice Hammer","Icicle Crash","Leaf Storm","Leaf Tornado","Leech Seed","Light of Ruin","Megahorn","Meteor Mash","Mountain Gale","Muddy Water","Mystical Power","Nature's Madness","Octazooka","Origin Pulse","Precipice Blades","Overheat","Play Rough","Power Whip","Present","Psyshield Bash","Pyro Ball","Raging Fury","Roar of Time","Rock Blast","Rock Slide","Rock Wrecker","Seed Flare","Sky Attack","Sky Upperrcut","Steel Wing","Stone Axe","Super Fang","Swagger","Toxic","Will-O-Wisp","Zen Headbutt","Ruination"]
        self.zmoves=["Breakneck Blitz","Inferno Overdrive","Gigavolt Havoc","Bloom Doom","Hydro Vortex","Shattered Psyche","Never-ending Nightmare","Tectonic Rage","Continental Crush","Twinkle Tackle","Acid Downpour","Black Hole Eclipse","Supersonic Skystrike","Savage Spin-Out","Corkscrew Crash","All-Out Pummeling","Subzero Slammer","Devastating Drake","10,000,000 Volt Thunderbolt","Catastropika","Pulverizing Pancake","Genesis Supernova","Soul-Stealing 7-Star Strike","Clangorous Soulblaze","Splintered Stormshards","Sinister Arrow Raid","Let's Snuggle Forever","Oceanic Operetta","Malicious Moonsault","Searing Sunraze Smash","Menacing Moonraze Maelstrom","Stoked Sparksurfer","Light That Burns The Sky","Extreme Evoboost","Guardian of Alola"]
        self.maxmovelist=["Max Strike","Max Flare","G-Max Wildfire","G-Max Centiferno","Max Geyser","G-Max Cannonade","G-Max Hydrosnipe","G-Max Foam Burst","Max Lightning","G-Max Volt Crash","G-Max Stun Shock","Max Quake","Max Knuckle","G-Max Chi Strike","Max Mindstorm","Max Phantasm","G-Max Terror","Max Starfall","Max Overgrowth","G-Max Drum Solo","G-Max Sweetness","G-Max Tartness","Max Rockfall","Max Darkness","Max Wyrmwind","G-Max Depletion","Max Flutterby","G-Max Befuddle","Max Ooze","Max Steelspike","Max Airstream","G-Max Resonance","G-Max Hailstorm","G-Max Finale","G-Max Volcalith","G-Max Stonesurge","Max Hailstorm","G-Max Cuddle","G-Max Sandblast","G-Max Fireball","G-Max Steelsurge","G-Max Snooze","G-Max Malodor","G-Max Vine Lash","G-Max One Blow","G-Max Rapid Flow","G-Max Wind Rage","G-Max Gold Rush","G-Max Replenish","G-Max Meltdown","G-Max Smite","Max Guard"]
        self.atkboost=["Swords Dance","Bulk Up","Fillet Away","Dragon Dance","Belly Drum","Clangorous Soul","Coil","Curse","Growth","Hone Claws","Howl","No Retreat","Meditate","Shell Smash","Victory Dance","Shift Gear","Tidy Up","No Retreat","Shift Gear"]
        self.spatkboost=["Calm Mind","Nasty Plot","Geomancy","Shell Smash","Quiver Dance","Growth","Meteor Beam","No Retreat","Tail Glow","Take Heart"]
        self.defboost=["Iron Defense","Acid Armor","Defend Order","Cosmic Power","Cotton Guard","Growth","Curse","Barrier"]
        self.protectmoves=["Protect","King's Shield","Spiky Shield","Baneful Bunker","Silk Trap","Obstruct","Burning Bulwark"]
        self.spdefboost=["Calm Mind","Amnesia"]
        self.buffmove=["Recover","Roost","Moonlight","Morning Sun","Synthesis","Hail","Rain Dance","Sunny Day","Sandstorm","Rest","Heal Order","Aqua Ring","Heal Bell","Aromatherapy","Electric Terrain","Grassy Terrain","Misty Terrain","Psychic Terrain","Snowscape","Light Screen","Reflect","Slack Off","Soft-Boiled","Jungle Healing","Trick Room","Tailwind","Shell Trap","Substitute","Shed Tail","Explosion","Misty Explosion","Teleport","Rest","Rock Polish","Lunar Blessing","Charge","Psych Up"]+self.atkboost+self.spatkboost+self.defboost+self.spdefboost+self.protectmoves
        self.noaccuracy=self.zmoves+["Aerial Ace","Aura Sphere","Defog","False Surrender","Disarming Voice","Flower Trick","Flying Press","Heart Swap","Hyperspace Hole","Hyperspace Fury","Kowtow Cleave","Phantom Force","Roar","Reflect","Light Screen","Aurora Veil","Shadow Punch","Shadow Force","Smart Strike","Spider Web","Struggle", "Vital Throw","Yawn","Whirlwind","Tachyon Cutter"]+self.maxmovelist+self.buffmove
        self.soundmoves=["Boomburst","Bug Buzz","Clanging Scales","Clangorous Soul","Clangorous Soulblaze","Disarming Voice","Grass Whistle","Heal Bell","Howl","Hyper Voice","Metal Sound","Noble Roar","Overdrive","Parting Shot","Perish Song","Relic Song","Torch Song","Roar","Shadow Panic","Snarl","Snore","Sparkling Aria","Roar","Metal Sound"]
        self.bypass=self.soundmoves+["Whirlwind"]
        self.prioritymove=["Mach Punch","Bullet Punch","Sucker Punch","Fake Out","Extreme Speed","Protect","Aqua Jet","Shadow Sneak","Accelerock","Ice Shard","Water Shuriken","Spiky Shield","King's Shield","Baneful Bunker","Max Guard","Silk Trap","Jet Punch","Quick Attack","First Impression","Water Shuriken","Vaccum Wave","Feint","Vaccum Wave","Burning Bulwark"]
        self.negprioritymove=["Whirlwind","Shell Trap","Counter","Mirror Coat","Roar","Dragon Tail","Teleport","Avalanche","Metal Burst"]
        self.bulletmove=["Bullet Seed","Snipe Shot","Armor Cannon","Aura Sphere","Flash Cannon","Spike Cannon","Fleur Cannon","Zap Cannon","Dynamax Cannon","Scale Shot","Ice Shard","Searing Shot","Rock Blast","Pin Missile","Icicle Spear","Pyro Ball","Focus Blast","Mist Ball","Beak Blast","Rock Wrecker","Octazooka","Sludge Bomb","Pollen Puff","Seed Bomb","Weather Ball","Shadow Ball"]
        self.contactmoves=["Fire Punch","Ice Punch","Thunder Punch","Horn Drill","Body Slam","Double-Edge","Drill Peck","Submission","Seismic Toss","Strength","Petal Dance","Waterfall","Skull Bash","High Jump Kick","Dizzy Punch","Leech Life","Crabhammer","Slash","Triple Kick","Mach Punch","Outrage","Steel Wing","Return","Dynamic Punch","Megahorn","Rapid Spin","Iron Tail","Cross Chop","Crunch","Extreme Speed","Fake Out","Facade","Superpower","Brick Break","Knock Off","Arm Thrust","Blaze Kick","Needle Arm","Poison Fang","Crush Claw","Meteor Mash","Shadow Punch","Sky Uppercut","Dragon Claw","Poison Tail","Volt Tackle","Leaf Blade","Hammer Arm","Gyro Ball","U-turn","Close Combat","Assurance","Last Resort","Sucker Punch","Flare Blitz","Force Palm","Poison Jab","Night Slash","Aqua Tail","X-Scissor","Dragon Rush","Drain Punch","Brave Bird","Giga Impact","Bullet Punch","Avalanche","Shadow Claw","Thunder Fang","Ice Fang","Fire Fang","Psychic Fangs","Shadow Sneak","Zen Headbutt","Power Whip","Cross Poison","Iron Head","Grass Knot","Wood Hammer","Aqua Jet","Head Smash","Crash Grip","Shadow Force","Heavy Slam","Foul Play","Acrobatics","Dragon Tail","Wild Charge","Drill Run","Dual Chop","Horn Leech","Sacred Sword","Razor Shell","Heat Crash","Head Charge","Gear Grind","Bolt Strike","V-create","Flying Press","Fell Stinger","Phantom Force","Draining Kiss","Play Rough","Nuzzle","Power-Up Punch","Dragon Ascent","First Impression","Darkest Lariat","Ice Hammer","High Horsepower","Solar Blade","Throat Chop","Anchor Shot","Lunge","Fire Lash","Smart Strike","Trop Kick","Dragon Hanmer","Stomping Tantrum","Accelerock","Liquidation","Spectral Thief","Sunsteel Strike","Zing Zap","Multi-Attack","Plasma Fists","Jaw Lock","Bolt Beak","Double Iron Bash","Fishious Rend","Body Press","Behemoth Blade","Behemoth Bash","Breaking Swipe","Spirit Break","False Surrender","Grassy Glide","Skitter Smack","Flip Turn","Triple Axel","Dual Wingbeat","Wicked Blow","Surging Strikes","Thunderous Kick","Quick Attack","Aqua Step","Aqua Cutter","Axe Kick","Bitter Blade","Blazing Torque","Collision Course","Combat Torque","Double Shock","Electro Drift","Gigaton Hammer","Glaive Rush","Hyper Drill","Jet Punch","Ice Spinner","Kowtow Cleave","Last Respects","Lumina Crash","Magical Torque","Mortal Spin","Noxious Torque","Order Up","Pounce","Rage Fist","Raging Bull","Ruination","Spin Out","Trailblaze","Triple Dive","Wicked Torque","Soul Robbery","Dragon Tail","Aerial Ace","Aqua Fang"]
        self.nondmgmove=["Stealth Rock","Toxic","Toxic Spikes","Sticky Web","Spikes"]
        self.normalmoves=["Double-Edge","Return","Body Slam","Boomburst","Crush Claw","Crush Grip","Dizzy Punch","Explosion","Extreme Speed","Hyper Voice","Facade","Multi-Attack","Strength","Hyper Beam","Giga Impact","Relic Song","Techno Blast","Weather Ball","Breakneck Blitz","Skull Bash","Metronome","Head Charge","Max Strike","Rapid Spin","Pulverizing Pancake","Extreme Evoboost","Hyper Drill","G-Max Replenish","Population Bomb","Slash","Endeavor","Pain Split","Quick Attack","G-Max Gold Rush","G-Max Cuddle","Last Resort","Hidden Power","Present","Assist","Tri Attack","Fake Out","Horn Drill","Guillotine","Raging Bull","Tail Slap","Tera Blast","Revelation Dance","Super Fang","Hidden Power","Thrash","Flail","Feint","Judgement","Double Hit","Blood Moon","Recover","Slack Off","Milk Drink","Double Team"]
        self.firemoves=["Fire Blast","Flare Blitz","Flamethrower","Magma Storm","Eruption","Lava Plume","Fire Punch","Blaze Kick","Fire Fang","Fire Lash","Heat Crash","Pyro Ball","Raging Fury","Sacred Fire","V-create","Blast Burn","Blue Flare","Fiery Dance","Fusion Flare","Heat Wave","Inferno","Mystical Fire","Searing Shot","Inferno Overdrive","Armor Cannon","Bitter Blade","Max Flare","G-Max Wildfire","G-Max Centiferno","Shell Trap","Torch Song","Blazing Torque","G-Max Fireball","Overheat","Mind Blown","Flame Charge","Fire Spin","Burn Up","Burning Jealousy","Will-O-Wisp","Sunny Day","Burning Bulwark","Temper Flare"]
        self.watermoves=["Hydro Pump","Surf","Liquidation","Flip Turn","Hydro Cannon","Muddy Water","Origin Pulse","Scald","Snipe Shot","Sparkling Aria","Steam Eruption","Waterfall","Water Spout","Aqua Jet","Crabhammer","Fishious Rend","Razor Shell","Surging Strikes","Water Shuriken","Wave Crash","Hydro Vortex","Aqua Tail","Max Geyser","G-Max Cannonade","G-Max Hydrosnipe","G-Max Foam Burst","G-Max Stonesurge","G-Max Rapid Flow","Aqua Step","Oceanic Operetta","Aqua Cutter","Chilling Water","Jet Punch","Octazooka","Triple Dive","Hydro Steam","Dive","Aqua Fang","Whirlpool","Bubble Beam","Aqua Ring","Life Dew","Rain Dance","Soak","Water Sport","Withdraw","Deathroll"]
        self.electricmoves=["Supercell Slam","Thunderbolt","Thunder","Volt Switch","Aura Wheel","Bolt Beak","Bolt Strike","Fusion Bolt","Plasma Fists","Thunder Fang","Thunder Punch","Volt Tackle","Electro Ball","Electroweb","Zap Cannon","Gigavolt Havoc","Wild Charge","Overdrive","Max Lightning","G-Max Volt Crash","G-Max Stun Shock","Discharge","Wildbolt Storm","10,000,000 Volt Thunderbolt","Catastropika","Stoked Sparksurfer","Electro Drift","Parabolic Charge","Double Shock","Nuzzle","Thunder Cage","Rising Voltage","Zing Zap","Charge","Eerie Impulse","Electric Terrain","Electrify","Ion Deluge","Magnet Rise","Magnetic Flux","Thunder Wave","Electro Shot","Thunderclap"]
        self.groundmoves=["Earthquake","Earth Power","Scorching Sands","Sandsear Storm","Bone Rush","Drill Run","Headlong Rush","High Horsepower","Land's Wrath","Precipice Blades","Stomping Tantrum","Thousand Arrows","Thousand Waves","Tectonic Rage","Magnitude","Bulldoze","Max Quake","Sandsear Storm","G-Max Sandblast","Fissure","Dig","Bonemerang","Sand Tomb","Mud Sport","Rototiller","Sand Attack","Shore Up","Spikes"]
        self.icemoves=["Ice Beam","Blizzard","Icicle Crash","Freeze Shock","Ice Fang","Ice Punch","Ice Shard","Icicle Spear","Mountain Gale","Freeze-Dry","Frost Breath","Ice Burn","Subzero Slammer","Glacial Lance","Max Hailstorm","G-Max Resonance","Ice Spinner","Ice Hammer","Glaciate","Triple Axel","Icy Wind","Avalanche","Sheer Cold","Aurora Beam","Aurora Veil","Chilly Reception","Hail","Haze","Mist","Snowscape"]
        self.fightingmoves=["Superpower","Close Combat","High Jump Kick","Aura Sphere","Final Gambit","Focus Blast","Secret Sword","Arm Thrust","Body Press","Brick Break","Drain Punch","Mach Punch","Dynamic Punch","Flying Press","Force Palm","Hammer Arm","Power-Up Punch","Sacred Sword","Seismic Toss","Sky Uppercutt","Triple Arrows","All-Out Pummeling","Meteor Assault","Submission","Max Knuckle","G-Max Chi Strike","Thunderous Kick","Collision Course","Counter","Combat Torque","Smelling Salts","Low Kick","Triple Kick","Cross Chop","Sky Uppercut","Focus Punch","Axe Kick","Reversal","Vaccum Wave","Storm Throw","Bulk Up","Coaching","Detect","Mat Block","No Retreat","Octolock","Quick Guard","Victory Dance","Upper Hand"]
        self.psychicmoves=["Psychic","Extrasensory","Psychic Fangs","Psycho Cut","Psyshield Bash","Zen Headbutt","Esper Wing","Luster Purge","Mist Ball","Psycho Boost","Psystrike","Stored Power","Shattered Psyche","Prismatic Laser","Expanding Force","Max Mindstorm","Freezing Glare","Genesis Supernova","Light That Burns The Sky","Lumina Crash","Mirror Coat","Twin Beam","Dream Eater","Soul Robbery","G-Max Gravitas","Psyshock","Psyblade","Future Sight","Mystical Power","Photon Geyser","Hyperspace Hole","Agility","Ally Switch","Amnesia","Barrier","Calm Mind","Cosmic Power","Gravity","Guard Split","Guard Swap","Heal Block","Healing Pulse","Healing Wish","Heart Swap","Hypnosis","Imprison","Instruct","Kinesis","Light Screen","Lunar Blessing","Lunar Dance","Magic Coat","Magic Powder","Magic Room","Meditate","Miracle Eye","Power Split","Power Swap","Power Trick","Psychic Terrain","Psycho Shift","Reflect","Rest","Role Play","Skill Swap","Speed Swap","Take Heart","Telekinesis","Teleport","Trick","Trick Room","Wonder Room","Psychic Noise"]
        self.ghostmoves=["Shadow Ball","Shadow Sneak","Shadow Claw","Spirit Shackle","Bitter Malice","Hex","Infernal Parade","Phantom Force","Shadow Force","Never-ending Nightmare","Moongeist Beam","Astral Barrage","Max Phantasm","Shadow Punch","G-Max Terror","Menacing Moonraze Maelstrom","Soul-Stealing 7-Star Strike","Sinister Arrow Raid","Last Respects","Rage Fist","Shadow Bone","Night Shade","Spectral Thief","Poltergeist","Confuse Ray","Curse","Destiny Bond","Grudge","Nightmare","Spite","Trick-Or-Treat"]
        self.fairymoves=["Moonblast","Dazzling Gleam","Play Rough","Spirit Break","Light of Ruin","Twinkle Tackle","Spirit Break","Max Starfall","G-Max Finale","Draining Kiss","Springtide Storm","Let's Snuggle Forever","Guardian of Alola","G-Max Smite","Strange Steam","Fleur Cannon","Misty Explosion","Magical Torque","Nature's Madness","Aromatic Mist","Baby-Doll Eyes","Charm","Crafty Shield","Decorate","Fairy Lock","Floral Healing","Flower Shield","Geomancy","Misty Terrain","Moonlight","Sweet Kiss","Alluring Voice","Decorate"]
        self.grassmoves=["Giga Drain","Leaf Blade","Chloroblast","Frenzy Plant","Energy Ball","Grass Knot","Leaf Storm","Leaf Tornado","Seed Flare","Solar Beam","Bullet Seed","Drum Beating","Grassy Glide","Horn Leech","Razor Leaf","Seed Bomb","Wood Hammer","Power Whip","Bloom Doom","Petal Dance","Apple Acid","Grav Apple","Max Overgrowth","G-Max Drum Solo","Flower Trick","G-Max Vine Lash","Petal Blizzard","Needle Arm","Solar Blade","Trailblaze","Trop Kick","G-Max Tartness","G-Max Sweetness","Aromatherapy","Cotton Guard","Cotton Spore","Forests Curse","Grass Whistle","Grassy Terrain","Ingrain","Jungle Healing","Leech Seed","Sleep Powder","Spicy Extract","Spiky Shield","Spore","Strength Sap","Stun Spore","Synthesis","Worry Seed","Syrup Bomb","Matcha Gotcha","Syrup Bomb","Ivy Cudgel","Vine Whip","Egg Bomb"]
        self.rockmoves=["Mighty Cleave","Stone Edge","Accelerock","Diamond Storm","Head Smash","Rock Blast","Rock Slide","Ancient Power","Power Gem","Splintered Stormshards","Continental Crush","Stone Axe","Meteor Beam","Rock Wrecker","Max Rockfall","G-Max Volcalith","Stone Axe","Salt Cure","Rock Tomb","Rock Polish","Sandstorm","Stealth Rock","Tar Shot","Wide Guard"]
        self.darkmoves=["Dark Pulse","Night Slash","Crunch","Night Daze","Snarl","Assurance","Ceaseless Edge","Darkest Lariat","Throat Chop","Foul Play","Knock Off","Hyperspace Fury","Sucker Punch","Wicked Blow","Black Hole Eclipse","False Surrender","Max Darkness","Jaw Lock","G-Max One Blow","Fiery Wrath","Malicious Moonsault","Kowtow Cleave","Ruination","G-Max Snooze","Wicked Torque","Dark Hole","Power Trip","Payback","Catastrophic Strike","Dark Void","Embargo","Fake Tears","Flatter","Hone Claws","Memento","Nasty Plot","Obstruct","Parting Shot","Quash","Snatch","Switcheroo","Taunt","Topsy-Turvy","Torment","Lash Out","Beat Up"]
        self.dragonmoves=["Roar Of Time","Draco Meteor","Dragon Pulse","Dragon Claw","Outrage","Core Enforcer","Roar of Time","Spacial Rend","Devastating Drake","Dragon Energy","Breaking Swipe","Dual Chop","Dragon Darts","Max Wyrmwind","G-Max Depletion","Dynamax Cannon","Eternabeam","Clangorous Soulblaze","Glaive Rush","Clanging Scales","Order Up","Scale Shot","Draco Barrage","Dragon Tail","Dragon Rush","Dragon Hammer","Clangorous Soul","Dragon Dance","Dragon Cheer","Fickle Beam","Dragon Cheer"]
        self.bugmoves=['U-Turn',"Megahorn","Pin Missile","Bug Buzz","U-turn","X-Scissor","Leech Life","Savage Spin-Out","Max Flutterby","G-Max Befuddle","Pounce","Lunge","First Impression","Skitter Smack","Signal Beam","Attack Order","Pollen Puff","Infestation","Fell Stinger","Defend Order","Heal Order","Powder","Quiver Dance","Rage Powder","Silk Trap","Spider Web","Sticky Web","String Shot","Tail Glow"]
        self.poisonmoves=["Poison Jab","Sludge Bomb","Cross Poison","Sludge Wave","Dire Claw","Gunk Shot","Belch","Poison Fang","Poison Tail","Venoshock","Acid Downpour","Max Ooze","G-Max Malodor","Noxious Torque","Acid Spray","Barb Barrage","Mortal Spin","Shell Side Arm","Acid Armor","Baneful Bunker","Coil","Corrosive Gas","Gastro Acid","Poison Gas","Poison Powder","Purify","Toxic","Toxic Spikes","Toxic Thread","Venom Drench"]
        self.steelmoves=["Flash Cannon","Meteor Mash","Bullet Punch","Steel Beam","Doom Desire","Gyro Ball","Heavy Slam","Iron Head","Iron Tail","Steel Wing","Corkscrew Crash","Sunsteel Strike","Max Steelspike","Behemoth Bash","Behemoth Blade","Searing Sunraze Smash","G-Max Steelsurge","Make It Rain","Double Iron Bash","Gigaton Hammer","Spin Out","G-Max Meltdown","Gear Grind","Anchor Shot","Smart Strike","Metal Burst","Autotomize","Gear Up","Iron Defense","Kings Shield","Metal Sound","Shelter","Shift Gear","Tachyon Cutter","Hard Press"]
        self.flyingmoves=["Brave Bird","Sky Attack","Acrobatics","Beak Blast","Dragon Ascent","Drill Peck","Dual Wingbeat","Supersonic Skystrike","Aeroblast","Hurricane","Oblivion Wing","Air Slash","Max Airstream","Bleakwind Storm","G-Max Wind Rage","Sonic Slash","Aerial Ace","Bounce","Fly","Razor Wind","Defog","Feather Dance","Mirror Move","Roost","Tailwind","Air Cutter"]
        self.statusmove=["Geomancy","Recover","Roost","Synthesis","Morning Sun","Moonlight","Slack Off","Soft-Boiled","Milk Drink","Rest","Lunar Blessing","Shore Up","Wish","Sleep Powder","Iron Defense","Calm Mind","Swords Dance","Bulk Up","Recover","Roost","Thunder Wave","Lunar Blessing","Take Heart","Heart Swap","Will-O-Wisp","Moonlight","Synthesis","Morning Sun","Rain Dance","Sunny Day","Hail","Sandstorm","Dark Void","Trick Room","Nasty Plot","Shell Smash","Dragon Dance","Belly Drum","Spore","Hypnosis","Rest","Coil","Curse","Strength Sap","Leech Seed","Protect","Spiky Shield","King's Shield","Heal Order","Defend Order","Grassy Terrain","Electric Terrain","Misty Terrain","Psychic Terrain","Yawn","Doodle","Cosmic Power","Charm","Chilly Reception","Amnesia","Aromatherapy","Wish","Quiver Dance","Glare","Haze","Healing Bell","Light Screen","Reflect","Acid Armor","Agility","Aqua Ring","Autotomize","Cotton Guard","Corrosive Gas","Encore","Forest's Curse","Soak","Magic Powder","Trick-or-Treat","Iron Defense","Metronome","Pain Split","Growth","Destiny Bond","Shore Up","Aurora Veil","Shell Trap","Taunt","Encore","Toxic","Spikes","Psycho Shift","Barrier","Healing Wish","Lunar Dance","Acupressure","Me First","Lovely Kiss","Perish Song","Feather Dance","Fake Tears","Swagger","Trick","Fillet Away","Parting Shot","Shelter","Victory Dance","Spicy Extract","Eerie Spell","Substitute","Shed Tail","Recycle","Defog","Double Team","Minimize","Lock-On","Roar","Whirlwind","Transform","Court Change","Teleport","No Retreat","Smokescreen","Sand-Attack","Clangorous Soul","Eerie Impulse","Obstruct","Octolock","Sweet Kiss","Toxic Thread","Skill Swap","Rock Polish","Metal Sound","Confuse Ray","Tickle","Scary Face","Venom Drench","Stun Spore","Tar Shot","Psych Up","Charge","Mimic","Captivate","Stealth Rock","Sticky Web","Tailwind","Tail Glow","Toxic Spikes","Slack Off","Snowscape","Heal Bell","Shift Gear","Sleep Talk","Tidy Up","Burning Bulwark","Focus Energy","Dragon Cheer"]
        self.recoverymoves=["Recover","Roost","Synthesis","Morning Sun","Moonlight","Slack Off","Soft-Boiled","Milk Drink","Rest","Lunar Blessing","Shore Up","Wish"]
        self.healingmoves=["Recover","Roost","Synthesis","Morning Sun","Moonlight","Slack Off","Soft-Boiled","Milk Drink","Rest","Lunar Blessing","Giga Drain","Drain Punch","Jungle Healing","Pain Split","Wish","Bitter Blade","Draining Kiss","Horn Leech","Leech Life","Parabolic Charge","Oblivion Wing","Shore Up","Wish","Slack Off"]
        self.priorityatkmoves=["Aqua Jet","Bullet Punch","Extreme Speed","Sucker Punch","Fake Out","Jet Punch","Quick Attack","First Impression","Fake Out","Feint","Vaccum Wave"]
        self.terrainmove=["Grassy Terrain","Misty Terrain","Electric Terrain","Psychic Terrain"]
        self.statuschangemoves=["Will-O-Wisp","Toxic","Thunder Wave","Sleep Powder"]
        self.weathermoves=["Rain Dance","Sunny Day","Snowscape","Sandstorm"]
        self.pp15=["Supercell Slam","Acrobatics","Attack Order","Body Slam","Brave Bird","Brick Break","Crunch","Double-Edge","Dragon Claw","Dual Chop","Fire Fang","Fire Punch","Flail","Flare Blitz","Foul Play","Gear Grind","Head Charge","Ice Fang","Hyper Fang","Ice Punch","Iron Head","Iron Tail","Leaf Blade","Needle Arm","Night Slash","Petal Blizzard","Poison Fang","Present","Rock Tomb","Seed Bomb","Shadow Claw","Sky Uppercut","Spike Cannon","Strength","Thunder Fang","Thunder Punch","Volt Tackle","Waterfall","Wild Charge","Wood Hammer","X-Scissor","Zen Headbutt","Beak Blast","Dragon Hammer","Fire Lash","Lunge","Throat Chop","Trop Kick","Plasma Fists","Snap Trap","Breaking Swipe","Spirit Break","Shadow Ball","Barb Barrage","Bitter Malice","Dire Claw","Infernal Parade","Stone Axe","Triple Arrows","Sacred Sword","Hidden Power","Signal Beam","Dark Pulse","Flamethrower","Spore","Sleep Powder","Snipe Shot","Icy Wind","Aqua Fang"]
        self.pp10=["Aqua Tail","Assurance","Avalanche","Blaze Kick","Bone Rush","Bonemerang","Circle Throw","Crabhammer","Crush Claw","Dizzy Punch","Double Hit","Dragon Rush","Dragon Tail","Drain Punch","Earthquake","Egg Bomb","Fake Out","Flying Press","Force Palm","Hammer Arm","Heat Crash","High Jump Kick","Land's Wrath","Leech Life","Megahorn","Metal Burst","Meteor Mash","Play Rough","Power Whip","Power-Up Punch","Razor Shell","Rock Blast","Rock Slide","Smelling Salts","Storm Throw","Super Fang","Triple Kick","Vital Throw","Precipice Blades","Darkest Lariat","First Impression","High Horsepower","Ice Hammer","Liquidation","Multi-Attack","Psychic Fangs","Shadow Bone","Smart Strike","Spectral Thief","Spirit Shackle","Stomping Tantrum","Zing Zap","Jaw Lock","Dragon Darts","Bolt Beak","Fishious Rend","Body Press","Drum Beating","Aura Wheel","Grav Apple","False Surrender","Skitter Smack","Triple Axel","Dual Wingbeat","Thunderous Kick","Aqua Step","Axe Kick","Bitter Blade","Blazing Torque","Chilly Reception","Combat Torque","Doodle","Fillet Away","Flower Trick","Kowtow Cleave","Last Respects","Lumina Crash","Magical Torque","Noxious Torque","Order Up","Population Bomb","Rage Fist","Raging Bull","Ruination","Shed Tail","Silk Trap","Snowscape","Tidy Up","Torch Song","Triple Dive","Twin Beam","Wicked Torque","Psychic","Protect","Toxic","Dark Void","Stored Power","Weather Ball","Baneful Bunker","Esper Wing","Freezing Glare","Jungle Healing","Lunar Blessing","Obstruct","Mystical Power","Psyshield Bash","Shelter","Take Heart","Thunder Cage","Victory Dance","Wave Crash","Giga Drain","Ice Beam","Earth Power","Belch","Thunder","Roost","Slack Off","Recover","Icicle Crash","Sludge Bomb","Shell Side Arm","Mystical Fire","Judgement","Multi-Attack","Thunder Wave","Ivy Cudgel","Syrup Bomb","Deathroll","Burning Bulwark","Temper Flare","Alluring Voice"]
        self.hazards=["Stealth Rock","Sticky Web","Toxic Spikes","Spikes"]
        self.pp5=["Mighty Cleave","Aeroblast","Ancient Power","Armor Cannon","Astral Barrage","Behemoth Bash","Behemoth Blade","Blast Burn","Bleakwind Storm","Blizzard","Blue Flare","Bolt Strike","Burn Up","Burning Jealousy","Chloroblast","Clanging Scales","Clangorous Soul","Close Combat","Collision Course","Cross Chop","Crush Grip","Destiny Bond","Diamond Storm","Doom Desire","Double Iron Bash","Double Shock","Draco Meteor","Dragpn Ascent","Dragon Energy","Dynamax Cannon","Dynamic Punch","Electro Drift","Encore","Endeavor","Eruption","Eternabeam","Explosion","Extreme Speed","Final Gambit","Fire Blast","Fissure","Fleur Cannon","Focus Blast","Frenzy Plant","Fusion Bolt","Fusion Flare","Giga Impact","Gigaton Hammer","Glacial Lance","Glaive Rush","Guillotine","Gunk Shot","Gyro Ball","Head Smash","Headlong Rush","Heal Bell","Horn Drill","Hydro Pump","Hydro Cannon","Hyper Beam","Hyper Drill","Hyperspace Fury","Hyperspace Hole","Inferno","Lash Out","Last Resort","Leaf Storm","Light of Ruin","Luster Purge","Magma Storm","Make It Rain","Meteor Assault","Mind Blown","Mist Ball","Misty Explosion","Moongeist Beam","Moonlight","Morning Sun","Mountain Gale","Overheat","Perish Song","Photon Geyser","Psycho Boost","Pyro Ball","Rain Dance","Roar of Time","Rock Wrecker","Sacred Fire","Sandsear Storm","Searing Shot","Seed Flare","Sheer Cold","Spacial Rend","Spin Out","Springtide Storm","Steam Eruption","Steel Beam","Steel Roller","Stone Edge","Sucker Punch","Sunny Day","Sunsteel Strike","Superpower","Surging Strikes","Synthesis","Technoblast","Trick Room","V-create","Water Spout","Wicked Blow","Wildbolt Storm","Zap Cannon","Dark Hole","Armor Cannon","Collision Course","Double Shock","Electro Drift","Gigaton Hammer","Glaive Rush","Hyper Drill","Make It Rain","Spin Out","Strength Sap","Sucker Punch","Techno Blast","Burn Up","Burning Jealousy","Teleport","Blood Moon","Fickle Beam"]+self.recoverymoves
        self.pivotingmoves=self.defboost+self.spdefboost+["Chilly Reception"]
        self.everymove=self.firemoves+self.watermoves+self.electricmoves+self.grassmoves+self.normalmoves+self.darkmoves+self.ghostmoves+self.psychicmoves+self.poisonmoves+self.steelmoves+self.fairymoves+self.bugmoves+self.fightingmoves+self.flyingmoves+self.icemoves+self.rockmoves+self.groundmoves+self.dragonmoves+self.statusmove+["Struggle","None"]
        self.allmove=tuple(set(self.everymove)-set(self.maxmovelist+self.zmoves))

typemoves=Moves()
def remove_common(a, b):
    for i in a:
        if i in b:
            a.remove(i)
def common(a,b):
    new=False
    for i in a:
        if i in b:
            new=True
    return new
def moveset(type1,type2,moves,num=4,name="None"):
    new=[]
    forbidden=["Healing Wish","Switcheroo","Trick","Psyshock","Psychic","Wave Crash","Liquidation","Hydro Pump","Surf","Muddy Water","Hydro Cannon","Hurricane","Air Slash","Brave Bird","Knock Off","Foul Play","Flamethrower","Fiery Dance","Lava Plume","Magma Storm","Overheat","Heat Wave","Fire Blast","Fire Fang","Flame Charge","Inferno","Flare Blitz","Thunder Punch","Wild Charge","Dire Claw","Poison Jab","Gunk Shot","Aura Sphere","Focus Blast","Close Combat","Drain Punch","Superpower","Hammer Arm","Bitter Malice","Shadow Ball","Dragon Pulse","Draco Meteor","Spacial Rend","Taunt","Strength Sap","Encore","Will-O-Wisp","Thunder Wave","Toxic Spikes","Stone Edge","Rock Slide","Yawn","Substitute","Haze","Nuzzle","Defog","Toxic","Yawn","Water Spout","Bulldoze","Earthquake","Stomping Tantrum","Headlong Rush","Magnitude","Drill Run","Fissure","Rock Blast","Rock Tomb","Head Smash","Rock Wrecker","Meteor Beam","Ancient Power","Frenzy Plant","Giga Drain","Leaf Storm","Razor Leaf","Petal Dance","Petal Blizzard","Leaf Blade","Power Whip","Rest","Sleep Talk","Dragon Pulse"]+typemoves.atkboost+typemoves.spatkboost+typemoves.pivotingmoves+typemoves.hazards+typemoves.recoverymoves
    while len(new)!=num:
        x=random.choice(moves)
        if len(new)==0:
            new.append(x)
        elif x not in new and x in ["Rest","Sleep Talk"] and common(new,["Rest","Sleep Talk"]) is True:
            new.append(x)  
        elif x not in new and x in ["Frenzy Plant","Giga Drain","Leaf Storm","Razor Leaf","Petal Dance","Petal Blizzard","Leaf Blade","Power Whip"] and common(new,["Frenzy Plant","Giga Drain","Leaf Storm","Razor Leaf","Petal Dance","Petal Blizzard","Leaf Blade","Power Whip"]) is False:
            new.append(x)  
        elif x not in new and x in typemoves.buffmove and common(new,typemoves.hazards) is False:
            new.append(x)
        elif x not in new and x in typemoves.buffmove and common(new,["Haze","Nuzzle","Defog","Toxic","Yawn","Water Spout"]) is False:
            new.append(x)   
        elif x not in new and x in ["Stone Edge","Rock Slide","Rock Blast","Rock Tomb","Head Smash","Rock Wrecker","Meteor Beam","Ancient Power"] and common(new,["Stone Edge","Rock Slide","Rock Blast","Rock Tomb","Head Smash","Rock Wrecker","Meteor Beam","Ancient Power"]) is False:
            new.append(x)
        elif x not in new and x in typemoves.recoverymoves and common(new,typemoves.recoverymoves) is False:
            new.append(x)
        elif x not in new and x=="Thunder Wave" and common(new,typemoves.spatkboost) is False:
            new.append(x)  
        elif x not in new and x=="Substitute" and common(new,typemoves.pivotingmoves) is False:
            new.append(x)
        elif x not in new and x in typemoves.atkboost and common(new,typemoves.spatkboost) is False:
            new.append(x)
        elif x not in new and x in typemoves.spatkboost and common(new,typemoves.atkboost) is False:
            new.append(x)     
        elif x not in new and x in typemoves.spatkboost and common(new,typemoves.spatkboost) is False:
            new.append(x)
        elif x not in new and x in typemoves.atkboost and common(new,typemoves.atkboost) is False:
            new.append(x)
        elif x not in new and x in ["Bulldoze","Earthquake","Stomping Tantrum","Headlong Rush","Magnitude","Drill Run","Fissure"] and common(new,["Bulldoze","Earthquake","Stomping Tantrum","Headlong Rush","Magnitude","Drill Run","Fissure"]) is False:
            new.append(x)  
        elif x not in new and x in ["Toxic","Will-O-Wisp","Thunder Wave","Toxic Spikes","Yawn"] and common(new,["Toxic","Will-O-Wisp","Thunder Wave","Toxic Spikes","Yawn"]) is False:
            new.append(x)
        elif x not in new and x in ["Taunt","Strength Sap","Encore"] and common(new,["Taunt","Strength Sap","Encore"]) is False:
            new.append(x)
        elif x not in new and x in ["Dragon Pulse","Draco Meteor","Spacial Rend"] and common(new,["Dragon Pulse","Draco Meteor","Spacial Rend"]) is False:
            new.append(x)
        elif x not in new and x in ["Close Combat","Drain Punch","Superpower","Hammer Arm"] and common(new,["Close Combat","Drain Punch","Superpower","Hammer Arm"]) is False:
            new.append(x)  
        elif x not in new and x in ["Aura Sphere","Focus Blast"] and common(new,["Aura Sphere","Focus Blast"]) is False:
            new.append(x)  
        elif x not in new and x in ["Dire Claw","Poison Jab","Gunk Shot"] and common(new,["Dire Claw","Poison Jab","Gunk Shot"]) is False:
            new.append(x)  
        elif x not in new and x in ["Thunder Punch","Wild Charge"] and common(new,["Thunder Punch","Wild Charge"]) is False:
            new.append(x)  
        elif x not in new and x in ["Hurricane","Air Slash","Brave Bird"] and common(new,["Hurricane","Air Slash","Brave Bird"]) is False:
            new.append(x)  
        elif x not in new and x in ["Wave Crash","Liquidation","Hydro Pump","Surf","Muddy Water","Hydro Cannon"] and common(new,["Wave Crash","Liquidation","Hydro Pump","Surf","Muddy Water","Hydro Cannon"]) is False:
            new.append(x)    
        elif x not in new and x in ["Healing Wish","Switcheroo","Trick"] and common(new,["Healing Wish","Switcheroo","Trick"]) is False:
            new.append(x)
        elif x not in new and x in ["Knock Off","Foul Play"] and common(new,["Knock Off","Foul Play"]) is False:
            new.append(x)  
        elif x not in new and x in ["Bitter Malice","Shadow Ball"] and common(new,["Bitter Malice","Shadow Ball"]) is False:
            new.append(x)
        elif x not in new and x in ["Dragon Dance","Draco Meteor","Dragon Pulse"] and common(new,["Dragon Dance","Draco Meteor","Dragon Pulse"]) is False:
            new.append(x)   
        elif x not in new and x in ["Psyshock","Psychic"] and common(new,["Psyshock","Psychic"]) is False:
            new.append(x)       
        elif x not in new and x in ["Flamethrower","Fiery Dance","Lava Plume","Magma Storm","Overheat","Heat Wave","Fire Blast","Fire Fang","Flame Charge","Inferno","Flare Blitz"] and common(new,["Flamethrower","Fiery Dance","Lava Plume","Magma Storm","Overheat","Heat Wave","Fire Blast","Fire Fang","Flame Charge","Inferno","Flare Blitz"]) is False:
            new.append(x)
        elif x not in new and x not in forbidden:
            new.append(x)
        
    return new

async def abilitydesc(ability):
    abilitylist={
    "Blaze":"Powers up Fire-type move when HP is low.",
    "Torrent":"Powers up Water-type move when HP is low.",
    "Overgrow":"Powers up Grass-type move when HP is low.",
    "Swarm":"Powers up Bug-type move when HP is low.",
    "Adaptability":"Increases the same-type attack bonus from 1.5x to 2x.",
    "Aerilate":"Turns Normal-type moves Flying-type and boost their damage to 1.3x.",
    "Aftermath":"Damages the attacker for 1/4 its health when knocked out by a contact move.",
    "Air Lock":"Negates all weather effects but doesnt prevent weather itself.",
    "Analytic":"Boosts moves to 1.3x if user moves last",
    "Anger Point":"Maximizes attack when hit by a critical hit.",
    "Anger Shell":"Sharply raises Atk,SpAtk,Speed and drops Def and SpDef when HP drops below half.",
    "Anticipation":"Notifies if opponent has super effective moves or OHKO moves.",
    "Arena Trap":"Prevents grounded opponents from fleeing the battlefield.",
    "Armor Tail":"Prevent opponent from using priority moves.",
    "As One":"Boost Atk/SpAtk on KO and prevents opponent from consuming its held Berry.",
    "Aura Break":"Reverses the effects of fairy and dark aura.",
    "Bad Dreams":"Damages sleeping opportunity for 1/8 of their max HP each turn.",
    "Battle Armor":"Protects against critical hits.",
    "Battle Bond" : " Transforms Greninja into Ash Greninja on KO.",
    "Beads of Ruin":"Lowers th SpDef of other Pokémons except itself.",
    "Beast Boost":"Raises the best stats by one stage on KO.",
    "Berserk":"Raises SpAtk when HP drops below half.",
    "Big Pecks":"Protects against Defense drops.",
    "Blazing Soul":"Raises Fire-type moves priority by one stage.",
    "Bulletproof":"Protects gaints bullet,ball and bomb-based moves.",
    "Cheek Pouch":"Restores HP upon eating Berry, in addition to the Berrys effect.",
    "Chilling Neigh":"Raises Atk upon KO.",
    "Chlorophyll":"Doubles speed during strong sunlight.",
    "Clear Body":"Prevents stats from being lowered by other Pokémon.",
    "Cloud Nine":"Negates all weather effects but doesnt prevent weather itself.",
    "Color Change":"Changes type to match when hit by a damaging move.",
    "Comatose":"Keeps the Pokémon in a drowsy state. Cannot be statused.",
    "Commander":"Sharply boosts allied Dondozos stats.",
    "Competitive":"Raises SpAtk by 2 stages upon having any stat lowered.",
    "Compound Eyes":"Raises moves accuracy to 1.3x.",
    "Contrary":"Inverts stat changes.",
    "Corrosion":"Poison moves can hit and poison Steel and Poison-type Pokémons.",
    "Costar":"Copies the opponents stat changes upon entry.",
    "Cotton Down":"Lowers the speed of other Pokémons upon getting hit by any move.",
    "Cud Chew":"Can restore berry one time.",
    "Curious Medicine":"Resets stat changes of other Pokémon.",
    "Cursed Body":"30% chance of disabling any move used on contact.",
    "Cute Charm":"30% chance of infatuating the attacker on contact.",
    "Damp":"Prevents self destructing moves.",
    "Dancer":"Copies dancing move of other Pokémon.",
    "Dark Aura":"Boost Dark-type moves of every Pokémon by 1.33x.",
    "Dauntless Shield":"Boosts defense by one stage upon entering.",
    "Dazzling":"Prevents opponent from using priority moves.",
    "Defeatist":"Lowers Atk and SpAtk stats when HP drops to 1/3 of max HP.",
    "Delta Stream":"Removes the weather and eliminates the Flying-type weaknesses.",
    "Desolate Land":"Nullifies any Water-type attacks.",
    "Disguise":"Allows the Pokémon to escape damage for one time.",
    "Download":"Boosts certain stat according to opponent upon entering the field.",
    "Dragons Maw":"Increases Dragon-typr moves damage.",
    "Drizzle":"Summons rain on the battlefield upon entering.",
    "Drought":"Summons strong sunlight on the battlefield upon entering.",
    "Dry Skin":"Heals during rainfall and damages in strong sunlight.\nImmune to Water-type attacks.",
    "Early Bird":"Makes sleep pass twice as quickly.",
    "Earth Eater":"Heals instead of damaging when when hit by Ground-type attack.",
    "Effect Spore":"30% chance of inflicting paralysis,poison and sleep on contact.",
    "Electric Surge":"Summons Electric Terrain.",
    "Electromorphosis":"Powers up Electric-type moves when it takes damage.",
    "Emergency Exit":"Switches out when HP drops below half.",
    "Fairy Aura":"Boosts Fairy-type moves of all the pokémon by 1.33x.",
    "Filter":"Takes 0.75x damage from super effective moves.",
    "Flame Body":"30% chance of causing burn on contact.",
    "Flare Boost":"Immune to burn damage and boosts special attack by 1.5x when burned.",
    "Flash Fire":"Immune to Fire-type attack.\nBoosts Fire-type moves by 1.5x when hit by Fire-type moves.",
    "Flower Gift":"Transforms in sunlight and boosts its Def and SpDef.",
    "Flower Veil":"Protects from stats being lowered.",
    "Fluffy":"Takes half damage from moves that make contact and takes double damage from Fire-type moves.",
    "Forecast":"Changes form according to weather and summons weather by checking the rock its holding.",
    "Forewarn":"Warns about opponents strongest move.",
    "Frisk":"Reveals opponents item.",
    "Full Metal Body":"Prevents from stats being lowered.",
    "Fur Coat":"Halves damage taken from physical attacks.",
    "Gale Wings" : " Raises Flying-type moves priority by one stage.",
    "Galvanize":"Normal-type moves converts to Electric-type and boosts it by 33%.",
    "Gluttony":"Eats Berry when HP drops to half.",
    "Good as Gold":"Immune to other pokémons status move and stat lowering.",
    "Gooey":"Lowers speed by one stage of opponent when his by a contact move.",
    "Gorilla Tactics":"Boosts attack but only allows to use first selected move.",
    "Grass Pelt":"Boost Defense while Grassy Terrain is in effect.",
    "Grassy Surge":"Summons Grassy Terrain.",
    "Grim Neigh":"Boosts Special Attack on KO.",
    "Guard Dog":"Boost Attack when gets intimidated instead of lowering it.",
    "Gulp Missile":"Catches prey while surfing and diving.",
    "Guts":"Boosts Attack by 1.5x when struggling by any major status.",
    "Hadron Engine":"Summons Electric Terrain and boosts Special Attack.",
    "Harvest":"Restores Berry while Berry is consumed.",
    "Healer":"Cures ally pokémons status condition but has 30% chance of it.",
    "Heatproof":"Takes half damage from Fire-type moves.",
    "Heavy Metal":"Doubles the pokémons weight.",
    "Huge Power":"Doubles attack in battle.",
    "Hunger Switch":"Switches form each turn between Full Belly to Hungry Mode.",
    "Hustle":"Boosts physical moves by 1.5x and decrease accuracy to 0.8x.",
    "Hydration":"Cures status condition during rain.",
    "Hyper Cutter":"Prevents from stats being lowered.",
    "Ice Body":"Restores HP during Hail/Snowstorm by 1/16 of max HP.",
    "Ice Face":"Ice face acts as substitute and boosts stats when broken. Restores in Hail/Snowstorm.",
    "Ice Scales":"Halves damage from Special Attacks.",
    "Illuminate":"Boosts accuracy by 1.3x.",
    "Illusion":"Disguises as the last pokémon in party and deals extra damage while disguised.",
    "Immunity":"Immune to Poison damage.",
    "Imposter":"Transforms upon entering the battle.",
    "Infiltrator":"Bypasses screens, protects and substitute.",
    "Innards Out":"Deals damage equal to the amount of HP during getting KOd.",
    "Inner Focus":"Prevents flinching.",
    "Insomnia":"Prevents sleep.",
    "Intimidate":"Lowers opponents attack by one stage upon entering the battle.",
    "Intepid Sword":"Boosts attack by one stage upon entering the battle.",
    "Iron Barbs":"Deals damage equal to 1/8 of max HP when hit by a contact move.",
    "Iron Fist":"Boosts punching moves.",
    "Justified":"Raises attack when hit by a Dark-type attack.",
    "Keen Eye":"Prevents accuracy lowering.",
    "Leaf Guard":"Protects from status condition.",
    "Levitate":"Floats and immune to Ground-type moves.",
    "Libero":"Changes type to the type of the moves its about to use.",
    "Light Metal":"Halves pokémons weight.",
    "Lightning Rod":"Immune to Electric-type moves and boost Special attack when hit by one.",
    "Limber":"Prevents paralysis.",
    "Lingering Aroma":"Passes the ability on contact.",
    "Liquid Ooze":"Deals damage instead of healing.",
    "Long Reach":"Doesnt make any contact.",
    "Magic Bounce":"Reflects non damaging moves to the user.",
    "Magic Guard":"Protects from indirect damage.",
    "Magician":"Steals item when not holding any.",
    "Magma Armor":"Prevents freezing.",
    "Magnet Pull":"Traps Steel-type pokémon.",
    "Marvel Scale":"Increases defense by 1.5x when statused.",
    "Mega Launcher":"Boosts pulse and aura moves by 1.5x.",
    "Merciless":"Hits critical hits on poisoned opponents.",
    "Mirror Armor":"Bounces back stat-lowering effects.",
    "Misty Surge":"Summons Misty Terrain.",
    "Mold Breaker":"Bypasses targets ability.",
    "Moody":"Sharply raises random stat while lowering random stat.",
    "Motor Drive":"Immune to Electric-type moves and boosts speed when hit by one.",
    "Terrain Rush":"Immune to Ground-type moves and boosts speed when hit by one.",
    "Ignition":"Immune to Fire-type moves and boosts speed when hit by one.",
    "Magnetic Field":"Immune to Steel-type moves and boosts defense when hit by one.",
    "Moxie":"Raises attack on KO.",
    "Multiscale":"Takes half damage on full HP.",
    "Blubber Defense":"Takes half damage on full HP.",
    "Multitype":"Changes type according to the plate its holding.",
    "Mummy":"Passes the ability on contact.",
    "Mycelium Might":"Status moves have negative priority.",
    "Natural Cure":"Cures status condition on switch.",
    "Neuroforce":"Powers up super effective moves by 1.2x.",
    "Neutralizing Gas":"Neutralizes opponents ability.",
    "No Guard":"Ensures all the moves used by and against hit.",
    "Normalize":"Makes every move Normal-type.",
    "Oblivious":"Protects from infatuating.",
    "Opportunist":"Boosts stats when opponent boosts their stats.",
    "Orichalcum Pulse":"Summons harsh sunlight and boosts Attack stat.",
    "Overcoat":"Prevents against status and weather condition.",
    "Own Tempo":"Prevents confusion.",
    "Parental Bond":"Hits twice but 2nd hit deals 0.25x damage.",
    " Pastel Veil":"Protects from poison.",
    "Perish Body":"The attacker and the pokémon will faint if they dont switch out in three turns.",
    "Pickpocket":"Steals attackers held item on contact.",
    "Pixilate":"Turn Normal-type moves into Fairy-type and boosts them by 1.3x.",
    "Poison Heal":"Heals when poisoned instead of damaging.",
    "Poison Touch":"30% chance of poisoning opponent on making contact.",
    "Poison Point":"30% chance of poisoning when hit by contact move.",
    "Power Construct":"Transforms to its Complete form when HP drops below half.",
    "Power of Alchemy":"Passes ability when ally faints",
    "Power Spot":"Powers up moves.",
    "Prankster" : "Raises non-damaging moves priority by one but cant effect Dark-types.",
    "Pressure":"Increases PP usage.",
    "Primordial Sea":"Nullifying Fire-type moves and summons Heavy Rain.",
    "Prism Armor":"Takes 0.75x damage from super effective moves.",
    "Propeller Tail":"Ignores ability of other pokémons.",
    "Protean":"Changes type to match the type of its move.",
    "Protosynthesis":"Boosts proficient stat in harsh sunlight or in usage of Booster Energy.",
    "Psychic Surge":"Summons Psychic Terrain.",
    "Punk Rock":"Boosts sound-based moves and takes half damage from them.",
    "Pure Power":"Doubles attack in battle",
    "Purifying Salt":"Protects from status condition and takes half damage from Ghost-type moves.",
    "Quark Drive":"Boosts proficient stat in Electric Terrain or in usage of Booster Energy.",
    "Queenly Majesty":"Protects from priority moves.",
    "Quick Draw":"20% chance of moving first.",
    "Quick Feet":"Boosts speed when statused.",
    "Rain Dish":"Restores HP by 1/16 of max HP during Rain.",
    "Rattled":"Raises speed when hit by Dark,Ghost or Bug-type moves.",
    "Receiver":"Can recieve ability from fainted ally.",
    "Reckless":"Boosts recoil moves by 1.2x.",
    "Refrigerate":"Turn Normal-type moves into Ice-type and boosts them by 1.3x.",
    "Regenerator":"Heals 1/3 of max HP upon switching out.",
    "Ripen":"Doubles the Berries effect.",
    "RKS System":"Changes type to the memory its holding.",
    "Rock Head":"Prevents from recoil damage.",
    "Rocky Payload":"Powers up Rock-type moves.",
    "Rough Skin":"Deals damage equal to 1/8 of max HP on contact.",
    "Sand Force":"Boosts Steel,Rock and Ground-type moves by 1.3x.",
    "Sand Rush":"Doubles speed in sandstorm.",
    "Sand Spit":"Summons sandstorm on contact.",
    "Sand Stream":"Summons sandstorm upon entering the battle.",
    "Sand Veil":"Increases evasion during sandstorm.",
    "Sap Sipper":"Immune to Grass-type moves and boosts attack when hit by one.",
    "Schooling":"Creates a giant whale like creature by schooling in certain condition.",
    "Scrappy":"Normal and Fighting-type moves can heat Ghost-type pokémon.",
    "Screen Cleaner":"Clears the screens on the opponent side.",
    "Seed Sower":"Summons Grassy Terrain on contact.",
    "Serene Grace":"Doubles the chance of moves extra effects occuring.",
    "Shadow Shield":"Halves damages on full HP.",
    "Shadow Tag":"Prevents opponent from fleeing.",
    "Sharpness":"Boosts slicing moves.",
    "Shed Skin":"33% chance of curing status condition.",
    "Sheer Force":"Boosts damage but prevents moves additional effects.",
    "Shell Armor":"Prevents critical hits.",
    "Shield Dust":"Protects from status condition.",
    "Shield Down":"Changes form when HP drops below half.",
    "Simple":"Doubles the stat modifiers.",
    "Skill Link":"Multi-moves hit every time.",
    "Slow Start":"Halves attack and speed for sometimes.",
    "Slush Rush":"Doubles speed during snowstorm/hail.",
    "Sniper":"Boosts critical hit damage.",
    "Snow Cloak":"Boosts evasion on snowstorm/hail.",
    "Snow Warning":"Summons snowstorm upon entering the battle.",
    "Solar Power":"Boosts special attack on harsh sunlight.",
    "Solid Rock":"Takes 0.75x damage from super effective attack.",
    "Soul-Heart":"Boosts special attack on KO.",
    "Soundproof":"Protects from sound-based moves.",
    "Speed Boost":"Raises speed every turn.",
    "Defiant":"Raise attack by two stages when a stat is lowered.",
    "Stakeout":"Deals double damage upon entering the battle.",
    "Stall":"Gives every moves negative priority.",
    "Stalwart":"Ignores ability of other pokémon.",
    "Stamina":"Raises defense when hit by a attack.",
    "Stance Change":"Changes stance according to the move.",
    "Static":"30% chance of causing paralysis on contact.",
    "Steadfast":"Raises speed upon flinching.",
    "Striker":"Boosts kicking moves.",
    "Steam Engine":"Boosts speed when hit by Fire or Water-type move.",
    "Steelworker":"Powers up Steel-type moves.",
    "Steely Spirit":"Powers up Steel-type moves.",
    "Stench":"10% chance of making flinch on contact.",
    "Sticky Hold":"Protects held item from being removed.",
    "Storm Drain":"Absorbs Water-type moves and raises special attack.",
    "Strong Jaw":"Boosts biting moves by 1.5x.",
    "Sturdy":"Prevent being KOd when at full HP.",
    "Suction Cups":"Prevents forced switchouts.",
    "Super Luck":"Raises critical hit rates by one stage.",
    "Supreme Overlord":"Gains strength from the fallen allies.",
    "Surge Surfer":"Doubles speed on Electric Terrain.",
    "Sweet Veil":"Prevents sleep.",
    "Swift Swim":"Doubles speed during rain.",
    "Sword of Ruin":"Lowers defense stat of all the pokémons except itself.",
    "Symbiosis":"Passes held item to ally upon use.",
    "Synchronize":"Inflicts status when its gets statuses.",
    "Tablets of Ruin":"Lowers attack stat of all pokémon except itself.",
    "Tangled Feet":"Doubles evasion when confused.",
    "Tangling Hair":"Lowers speed on contact.",
    "Technician":"Boosts weaker moves.",
    "Teravolt":"Bypasses ability of opponent.",
    "Thermal Exchange":"Boosts attack when hit by Fire-type move.\nCannot be burned as well.",
    "Thick Fat":"Takes half damage from Fire and Ice-type moves.",
    "Tinted Lens":"Doubles damage of not very-effective moves.",
    "Tough Claws":"Boosts contact moves.",
    "Toxic Boost":"Immunity to poison damage and boosts attack by 1.5x.",
    "Toxic Debris":"Scatters toxic spikes on contact.",
    "Trace":"Copies ability upon entering the battle.",
    "Transistor":"Boosts damage of Electric-type moves.",
    "Triage":"Raise priority of healing moves.",
    "Truant":"Skips every second turn.",
    "Turboblaze":"Bypasses ability of other Pokémons.",
    "Unaware":"Ignores stat change of other pokémons.",
    "Unburden":"Doubles speed when not holding a item.",
    "Unnerve":"Prevents opponent from eating its Berry.",
    "Unseen Fist":"Bypasses protection of other Pokémon.",
    "Vessel of Ruin":"Lowers special attack of all the pokémon except itself.",
    "Victory Star":"Increases move accuracy by 1.1x.",
    "Vital Spirit":"Prevents sleep.",
    "Volt Absorb":"Absorbs Electric-type moves and heals for 1/4 of max HP.",
    "Wandering Spirit":"Passes ability on contact.",
    "Water Absorb":"Absorbs Water-type moves and heals for 1/4 of max HP.",
    "Water Bubble":"Boosts Water-type moves and halves Fire-type moves damage taken.",
    "Water Compaction":"Raises defense when hit by Water-type moves.",
    "Water Veil":"Prevents burns.",
    "Weak Armor":"Drops defense stats and boosts speed when hit by a physical moves.",
    "Well-Baked Body":"Immune to Fire-type moves and sharply increases defense when hit by one.",
    "White Smoke":"Prevents stat from lowering.",
    "Wind Power":"Boosts Electric-type moves when hit by wind moves.",
    "Wind Rider":"Boosts attack when hit by wind move. Also immune to them.",
    "Wonder Guard":"Only takes damage from super effective moves.",
    "Wonder Skin":"Lowers accuracy of status moves from opponent by 0.5x.",
    "Zen Mode":"Transforms to zen form upon entering the battle.",
    "Zero to Hero":"Transforms into Hero form upon switching out.",
    "Winged":"Immune to Ground-moves and boosts Flying-moves by 1.5x.",
    "Volcaano Rage":"Uses Eruption after you use a move.",
    "Buginize":"Normal moves become Bug and get a 30% boost.",
    "Sun Worship":"Ups highest stat by +1 on entry when sunny.",
    "Ice Dew":"Ice ups Atk or SpAtk by +1.",
    "Amplifier":"Ups sound moves by 20%..",
    "Deadeye":"Never misses.",
    "Big Leaves":"Chloroplast/phyll, Harvest, Leaf Guard and Solar Power.",
    "Power Core":"The Pokémon uses +25% of its Defense or SpDef during moves.",
    "Looter":"Heals 1/4 HP when defeating an enemy.",
    "Predator":"Heals 1/4 HP when defeating an enemy.",
    "Flock":"Ups Flying moves by 20%, 50% when at 1/3 HP.",
    "North Wind":"Aurora Veil on entry. Immune to Hail damage.",
    "Scavenger":"Heals 1/4 HP when defeating an enemy.",
    "Soul Eater":"Heals 1/4 HP when defeating an enemy.",
    "Scare":"Lowers the foe's Special Attack.",
    "Majestic Bird":"Boosts Special Attack by 50%.",
    "Poisonate":"Normal moves become Poison and get a 20% boost.",
    "Short Circuit":"Ups Electric moves by 20%, 50% when at 1/3 HP.",
    "Juggernaut":"Contact moves use + 20% of its Defense stat. Can't get paralyzed.",
    "Primal Armor":"Weakens “supereffective” by 50%.",
    "Mountaineer":"Immune to Rock-type and Stealth Rock damage.",
    "Groundsate":"Normal moves become Ground and get a 20% boost",
    "Fossilized":"Halves incoming Rock-type damage.",
    "Feline Prowess":"Doubles Special Attack.",
    "Amphibious":"Water moves gain STAB (+ 50% power).",
    "Dragon's Maw":"Ups Dragon-type moves by 30%.",
    "Tera Shift":"When the Pokémon enters a battle, it absorbs the energy around itself and transforms into its Terastal Form.",
    "Tera Shell":" The Pokémon's shell contains the powers of each type. All damage-dealing moves that hit the Pokémon when its HP is full will not be very effective.",
    "Teraform Zero":"When Terapagos changes into its Stellar Form, it uses its hidden powers to eliminate all effects of weather and terrain, reducing them to zero."
    }
    if ability in abilitylist:
        return abilitylist[ability]
    else:
        return "Info missing!"
def tips():
    tipslist=(" Tips: You can type info1 on skip input to see player1s Pokémon."," Tips: You can type info2 on skip input to see player2s Pokémon."," Tips: You can type p2 on skip input to control or simulate player2."," Tips: You can type p1 on skip input to control or simulate player1."," Tips: You can type info on switch menu to see Pokémon from your party."," Tips: You can type reveal on skip input to reveal opponents party."," Tips: You can type ab2 on skip input to see pokémon2s ability."," Tips: You can type ab1 on skip input to see pokémon1s ability."," Tips: AI can use items from bag when not in Competitive mode."," Tips: You can type fs on trainer catagory option to get secret Fusion Trainer."," Tips: ev=Evil,e4=Elite Four,fr=Frontier Brain,ch=Champion,\n tl=Talented Trainer,gm=Gym Leader,hc=Hardcore"," Tips: Entering nothing will randomly input for you."," Tips: Rayquaza can Mega Evolve if it has Dragon Ascent in its moves.")        
