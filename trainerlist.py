#pylint:disable=C0103
#pylint:disable=C0103
#pylint:disable=R0915
#pylint:disable=R0912
#pylint:disable=C0303
#pylint:disable=C0114
#pylint:disable=W0401
#pylint:disable=C0301
from pokemonbase2 import *
from trainers import *
from typematchup import *
def teammaker(trclass=None,trname=None,pknum=6):
    "Creates Team"
    mons=[]
    team=[]
    clist=[]
    level=0
    legendary=[Shaymin,SShaymin,Darkrai,Cresselia,Manaphy,Uxie,Azelf,Mesprit,Registeel,Regirock,Regice,Articuno,Zapdos,Moltres,Raikou,Entei,Suicune,Lugia,Hooh,Celebi,Deoxys,ADeoxys,SDeoxys,DDeoxys,Jirachi,Mew,Rayquaza,Latias,Latios,MLatias,MLatios,Groudon,Kyogre,PGroudon,PKyogre,MRayquaza,Mewtwo,Dialga,ODialga,Palkia,OPalkia,Giratina,OGiratina,Heatran,Regigigas]
    #FIGHTING SPECIALIST 
    if trclass in ["Dojo Master","Blackbelt"]:
        namelist=["Taishi","Damme","Wesley","Joe","Dolph"]
        nn=random.choice(namelist)
        new_name=trclass+" "+nn
        mons=[Scrafty,HLilligant,Conkeldurr,Emboar,MBlaziken,MGallade,Gallade,Machamp,Poliwrath,Hitmonchan,Hitmonlee,Infernape,Blaziken,Breloom,Primeape,Heracross,MHeracross,Hariyama,MMedicham]
   #ELDER TRAINERS     
    if trclass =="Elder Trainer":
        namelist=["Jules","Shriner","Jason","Apollo","Damon","Castor","Marcus","Henry","Orion","Arthur","Julius","Zephyr","Helios","Liam","Odysseus","Albert","Helios"]
        nn=random.choice(namelist)
        new_name=trclass+" "+nn
        mons=[Carracosta,MAerodactyl,Arceus,Regigigas,Heatran,Groudon,Kyogre,Rayquaza,Mew,Regice,Regirock,Registeel,Aerodactyl,Kabutops,Omastar,Armaldo,Cradily,Rampardos,Bastiodon,Cloyster,Relicanth,Claydol,Arcanine,Mamoswine,Spiritomb,Lunatone,Solrock,Yanmega]
        mons+=random.choices([Rayquaza,Latias,Latios,Regice,Regirock,Registeel,Kyogre,Groudon,Entei,Suicune,Raikou],k=1)
    if trname is None and trclass not in ["Elder Trainer","Dojo Master",",Blackbelt", "Egyptian","Exorcist"]:
        namelist=["Josh","Kyler","Jade","John","Joey","Jan","Gabriel","Jamie","Kylie","Andrea","Evy","Ebba","Titus","Emiliano","Emilia","Natalie","Justin","Anastasia","Frannie","Danielle","Daniel","Hugo","Robert","Carlos","Alex","Alexander","Alexandra","Arslan","Johan","Mike","Julian","Selena","Emmanuel","Kristin","Lawrence","Frank","Pamela","Nicole","Emma","Matthew"]
        nn=random.choice(namelist)
        new_name=trclass+" "+nn
     #WATER SPECIALISTS
    if trclass in ["Marine Biologist","Surfer","Scuba Diver","Swimmer","Sailor","Captain","Pirate"]:
        mons=[Jellicent,Swanna,Carracosta,Basculegion,Seismitoad,HSamurott,Samurott,MSharpedo,MSwampert,MBlastoise,Phione,EGastrodon,WGastrodon,Empoleon,Walrein,Huntail,Gorebyss,Relicanth,Milotic,Crawdaunt,Whiscash,Dewgong,Sharpedo,Pelipper,Kingdra,Politoed,Azumarill,Feraligatr,Lanturn,Lapras,Gyarados,Slowbro,Cloyster,Starmie, Blastoise,Poliwrath,Swampert,Ludicolo]+random.choices([Manaphy, Wailord],k=1)
        #GRUNTS
    if trclass in ["Aqua Grunt"]:
        mons=[Crawdaunt,Sharpedo,Crobat,Mightyena,Muk,Weezing,Tentacruel,Wailord,MSharpedo]       
    if trclass in ["Magma Grunt"]:
        mons=[Camerupt,Torkoal,Crobat,Mightyena,Muk,Weezing,Magmortar,MCamerupt]           
    if trclass in ["Rocket Grunt"]:
        mons=[Arbok,Weezing,Victreebel,Muk,Crobat,Seviper,Houndoom,Yanmega, Machamp]
    if trclass in ["Galactic Grunt"]:
        mons=[Weavile,Bronzong,Crobat,Toxicroak,Muk,Weezing,Magnezone,Electivire,Magmortar,Rhyperior,Probopass,Gyarados]
#DRAGON SPECIALISTS
    if trclass in ["Dragon Tamer"]:
        mons=[Haxorus,Krookodile,Serperior,Yanmega,Garchomp,MGarchomp,Gyarados,MGyarados,Dragonite,Kingdra,Charizard,Aerodactyl,Tyranitar, Salamence,MSalamence,MAerodactyl,MCharizardX,MTyranitar,Feraligatr]+random.choices([Latias,Latios,MLatias,MLatios],k=1)
        #POISON SPECIALISTS
    if trclass in ["Venom Expert"]:
        mons=[Toxicroak,Drapion,Roserade,Seviper,Arbok,Weezing,Crobat,MBeedrill,Venusaur,Nidoking,Nidoqueen,Victreebel,Tentacruel,Muk,Gengar,Overqwil]
        #ELECTRIC
    if trclass in ["Rocker","Guitarist","Electrician"]:
        mons=[Eelektross,Galvantula,MManectric,AGolem,Magnezone,Jolteon,Electivire,Lanturn,Ampharos,MAmpharos,Luxray,WRotom,Zebstrika]        
        #FIRE SPECIALISTS
    if trclass in ["Kindler","Fiery Breathe"]:
        mons=[Chandelure,Darmanitan,HTyphlosion,Emboar,HArcanine,Magmortar,Infernape,Arcanine,Rapidash,Houndoom,Flareon,Typhlosion,Blaziken,Camerupt,Charizard,MCharizardY]
        #DECENT TRAINERS
    if trclass in ["Expert","Veteran"]:
        mons=[Basculegion,Stoutland,Probopass,Ursaluna,Yanmega,Magnezone,Tangrowth,Hippowdon,Lucario,Mismagius,Luxray,Roserade,Torterra,Glalie,Absol,Banette,Milotic,Armaldo,Cradily,Aggron,Hariyama,Breloom,Gardevoir,Swellow,Ludicolo,Swampert,Houndoom,Heracross,Steelix,Espeon,Ampharos,Flareon,Jolteon,Vaporeon,Snorlax,Lapras,Gyarados,Tauros,Kangaskhan,Hitmonchan,Hitmonlee,Exeggutor,Gengar,Dodrio,Slowbro,Rapidash,AGolem,Victreebel,Machamp,Golduck,Alakazam,Pidgeot,Blastoise,Ninetales,Primeape,MBeedrill, Venusaur, Charizard,Cloyster,MBanette,MGlalie]
        ch=random.randint(1,15)
        if ch==7:
            mons+=random.choices(legendary,k=1)
        pass
#THUGS
    elif trclass in[ "Street Punk","Biker","Cueball","Smuggler","Thief","Goon","Driver"]:
        namelist=["Josh","Kyler","Jade","John","Jan","Gabriel","Jamie","Emiliano","Justin","Frannie","Danielle","Daniel","Hugo","Robert","Carlos","Alex","Alexander","Arslan","Johan","Mike","Julian","Emmanuel","Kristin","Murphy"]
        nn=random.choice(namelist)
        new_name=trclass+" "+nn
        mons=[Eelektross,HZoroark,Zoroark,Scrafty,Krookodile,HLilligant,Seismitoad,Excadrill,Gigalith,HSamurott,PorygonZ,Magmortar,Magnezone,Electivire,Rhyperior,Drapion,Toxicroak,Mismagius,Luxray,Infernape,Absol,Farigarif,Crawdaunt,Seviper,Zangoose,Overqwil,Sharpedo,MManectric,MAggron,Hariyama,Breloom,Shiftry,Blaziken,MHoundoom,Skarmory,Scizor,Azumarill,Typhlosion,Gyarados,Pinsir,Weezing,Muk,Tentacruel,Primeape,Machamp,Golem,Cloyster,MSableye,MMawile,Crobat,Arbok]
        ch=random.randint(1,10)
        if ch==7:
            mons+=random.choices(legendary,k=1)
        pass 
        #FLYING SPECIALISTS
    elif trclass in ["Bird Keeper","Pilot","Sky Diver"]:
        mons=[Swanna,Archeops,Unfezant,Gliscor,Togekiss,Honchkrow,Staraptor,Empoleon,Flygon,Salamence,Pelipper,Swellow,MPidgeot,Charizard,Skarmory,Aerodactyl,Altaria,Crobat,Dodrio,Dragonite]
        mons+=random.choices([Articuno,Zapdos,Moltres,Latias,Latios,MLatias,MLatios],k=1)
    elif trclass == "Tamer":
        mons=[Tauros,Arbok,Arcanine,HArcanine,Rapidash,Ambipom,Ursaluna,Mamoswine,Houndoom,MHoundoom,Mightyena,Slaking,MManectric,Sharpedo,MSharpedo,Wailord,Zangoose,Seviper,Milotic,Absol,MAbsol,Walrein,Empoleon,Infernape,Luxray]+random.choices([Raikou,Suicune,Entei])
        #Ghost
    elif trclass == "Exorcist":
        namelist=["Gabrielle","Candido","Bishop","William","Bowden","Joseph","Thomas","Fantino","Angelo"]
        nn=random.choice(namelist)
        new_name=trclass+" "+nn
        mons=[Gengar,MGengar,HTyphlosion,MSableye,Banette,MBanette,Dusknoir,Drifblim,Mismagius,Spiritomb,Froslass,Cofagrigus,Runerigus,HZoroark,Jellicent,Chandelure]
        #Psychic
    elif trclass == "Psychic":
        mons=[Alakazam,MAlakazam,Slowbro,MSlowbro,Exeggutor,Starmie,Jynx,Espeon,Farigarif,Gardevoir,MGardevoir,Medicham,MMedicham,Lunatone,Solrock,Claydol,Metagross,MMetagross, Bronzong,Gallade,MGallade,Gothitelle,Reuniclus]
        #ANIMAL LOVERS
    elif trclass == "Zoologist":
        mons=[Krookodile,Feraligatr,Stoutland,Zebstrika,Ursaluna,Gliscor,Ambipom,Torterra,Farigarif,Sceptile,Houndoom,Tauros,Kangaskhan,Rapidash,Dodrio, Victreebel,Arcanine,Breloom]
        #BUG
    elif trclass == "Bug Catcher":
        mons=[Galvantula,Escavalier,Scolipede,Leavanny,Scizor,Heracross,Pinsir,Drapion,Vespiquen,Yanmega,MScizor,MHeracross,MPinsir]        
        #ICE SPECIALISTS
    elif trclass in ["Skier","Boarder"]:
    
        mons=[Vanilluxe,GDarmanitan,Weavile,Abomasnow,Walrein,Lapras,Mamoswine,Glalie,MGlalie,Jynx,Cloyster,ANinetales,MAbomasnow]
        ch=random.randint(1,10)
        if ch==7:
            mons+=[Articuno]
     #BETTER TRAINERS
    elif trclass == "Ace Trainer":
        mons=[Haxorus,Eelektross,Ferrothorn,Gothitelle,Reuniclus,HZoroark,Zoroark,Archeops,Cofagrigus,Scrafty,Darmanitan,Krookodile,Basculegion,Conkeldurr,Excadrill,Gigalith,Heatran,Dusknoir,Ursaluna,HArcanine,PorygonZ,Gliscor,Yanmega,Togekiss,Electivire,Rhyperior,Magnezone,Lucario,Drifblim,Roserade,Staraptor,Empoleon,Torterra,Infernape,Metagross,Salamence,Absol,Milotic,Altaria,Flygon,Wailord,MManectric,MGardevoir,Swellow,Ludicolo,Swampert,Blaziken,Kingdra,MHoundoom,Skarmory,Heracross,Scizor,MSteelix,Espeon,Umbreon,MAmpharos,Feraligatr,Typhlosion,Meganium,Dragonite,Snorlax,MGyarados,Tauros,MPinsir,Starmie,AMuk,AExeggutor,MGengar,Cloyster,MSlowbro,Golem,MAlakazam,MPidgeot,Poliwrath,Arcanine,ANinetales,Nidoking, Nidoqueen,MCharizardY,MVenusaur,MBlastoise,MSceptile,MCamerupt]
        ch=random.randint(1,5)
        if ch==3:
            mons+=random.choices(legendary,k=1)
            
        
#CHALLENGERS
    elif trclass == "Challenger":
        level=random.randint(70,74)
        mons=[Ferrothorn,Reuniclus,HZoroark,Zoroark,Darmanitan,GDarmanitan,Krookodile,Conkeldurr,Excadrill,Heatran,Uxie,Mesprit,Azelf,WRotom,Togekiss,Magnezone,Garchomp,Infernape,Latias,Latios,Metagross,Salamence,Slaking,Blissey,Kingdra,Skarmory,Umbreon,Crobat,Cloyster,Starmie,AExeggutor,Typhlosion,Feraligatr,Meganium,Arcanine,Snorlax,Dragonite]+[MSharpedo,MScizor,MSteelix,MGyarados,MKangaskhan,MAlakazam,MPidgeot,MSlowbro,MAerodactyl,MBlastoise,MVenusaur,MCharizardX,MCharizardY,MHeracross,MHoundoom,MSceptile, MBlaziken,MSwampert,MGardevoir,MCamerupt,MAbsol,MSalamence,MMetagross,MLopunny,MLucario]
        ch=random.randint(1,3)
        if ch==2:
            mons+=random.choices(legendary,k=1)
        pass
#fossil
    elif trclass in ["Fossil Maniac","Paleontologist"]:
        mons=[Archeops,Carracosta,Omastar,Kabutops,MAerodactyl,Armaldo,Cradily,Aerodactyl,Mamoswine,Bastiodon,Rampardos,Relicanth]
        #Ground
    elif trclass in ["Desert Explorer","Egyptian"]:
        if trclass=="Egyptian":
            namelist=["Wongani","Abdelhamid","Ali","Zafar","Saif","Hakeem","Ziyad","Hamed","Daud","Apis","Amon","Aton"]
            nn=random.choice(namelist)
            new_name=trclass+" "+nn
        mons=[Drapion,Camerupt,MCamerupt,Hippowdon,Nidoking,Nidoqueen,Golem,Gliscor,Steelix,MSteelix,Rhyperior,Mamoswine,Swampert,MSwampert,Flygon,Whiscash,Claydol,Torkoal,Torterra,EGastrodon,WGastrodon,Garchomp,MGarchomp,Seismitoad,Krookodile,Excadrill,Arbok]
#ROCK SPECIALISTS
    elif trclass in ["Ruin Explorer","Hiker"]:
     mons=[Gigalith,Lunatone,Solrock,Probopass,HArcanine,Runerigus,Cofagrigus,Gigalith,MTyranitar,MAggron,Rhyperior,Aggron,Steelix,Machamp,Tyranitar,Golem]
    if len(team)==0 and trclass=="Challenger":
        megachance=random.randint(1,2)
        while len(team)!=pknum:
            party=random.choices(mons)[0]
            member=party()
            if ("Mega " not in member.name and "(" not in member.name and "Totem " not in member.name) and len(team)<3:
                team.append(member)
                mons.remove(party)
            if ("(" in member.name and "Z-Crystal" not in member.name) and len(team)==3:
                team.append(member)
                mons.remove(party)
            if "Z-Crystal" in member.name and len(team)==4:
                team.append(member)
                mons.remove(party)
            if "Mega " in member.name and len(team)==5:
                team.append(member)
                mons.remove(party)
                
    if len(team)==0 and trclass in ["Expert","Veteran"]:
        megachance=random.randint(1,2)
        while len(team)!=pknum:
            party=random.choices(mons)[0]
            member=party()
            if ("Mega " not in member.name and "(" not in member.name and "Totem " not in member.name) and len(team)<5:
                team.append(member)
                mons.remove(party)
            if "Totem " in member.name and "Z-Crystal" in member.name and len(team)==5:
                team.append(member)
                mons.remove(party)
            if "Mega " in member.name and len(team)==5:
                team.append(member)
                mons.remove(party)    
            
                
    if len(team)==0 and trclass in ["Ace Trainer","Dragon Tamer"]:
        megachance=random.randint(1,2)
        while len(team)!=pknum:
            party=random.choices(mons)[0]
            member=party()
            if ("Mega " not in member.name and "(" not in member.name and "Totem " not in member.name) and len(team)<4:
                team.append(member)
                mons.remove(party)
            if "Z-Crystal" in member.name and len(team)==4:
                team.append(member)
                mons.remove(party)
            if "Mega " in member.name and len(team)==5:
                team.append(member)
                mons.remove(party)                       
                        
    if len(team)==0 and trclass not in ["Challenger","Ace Trainer","Dragon Tamer","Elder Trainer","Veteran","Expert"]:
        megachance=random.randint(1,2)
        while len(team)!=pknum:
            party=random.choices(mons)[0]
            member=party()
            if ("Mega " not in member.name and "Z-Crystal" not in member.name and "Totem " not in member.name) and len(team)<7:
                team.append(member)
                mons.remove(party)
            if megachance==2:
                if "Mega " in member.name and len(team)==5:
                    team.append(member)
                    mons.remove(party)
            if megachance==1:
                if "Totem " in member.name and "Z-Crystal" in member.name and len(team)==5:
                    team.append(member)
                    mons.remove(party)      

    if len(team)==0 and trclass=="Elder Trainer":
        megachance=random.randint(1,2)
        while len(team)!=pknum:
            party=random.choices(mons)[0]
            member=party()
            if ("Mega " not in member.name and "Z-Crystal" not in member.name and "Totem " not in member.name) and len(team)<7:
                team.append(member)
                mons.remove(party)
            if megachance==2:
                if "Mega " in member.name and len(team)==5:
                    team.append(member)
                    mons.remove(party)
            if megachance==1:
                if "Totem " in member.name and "Z-Crystal" in member.name and len(team)==5:
                    team.append(member)
                    mons.remove(party)                                                                                        
                     
    return new_name,team            

def genTrainer(name=None,num=6):
    trclasslist=["Blackbelt","Dojo Master","Dragon Tamer","Skier","Kindler","Sailor","Swimmer","Veteran","Elder Trainer","Challenger","Zoologist","Ruin Explorer","Ace Trainer","Expert","Street Punk","Scuba Diver","Fossil Maniac","Paleontologist","Surfer","Marine Biologist","Biker","Cueball","Bird Keeper","Pilot","Sky Diver","Venom Expert","Fiery Breathe","Rocker","Guitarist","Bug Catcher","Psychic","Exorcist","Electrician","Smuggler","Thief","Goon","Boarder","Desert Explorer","Egyptian","Tamer","Captain","Pirate","Driver","Magma Grunt","Aqua Grunt","Rocket Grunt","Galactic Grunt"]
    rclass=random.choice(trclasslist)
    trainer=teammaker(rclass,name,num)
    rname=trainer[0]
    rteam=trainer[1]
    rand=Trainer(rname,rteam)
    return rand
def showparty(obj):
    num=0
    total=0
    for i in obj.pokemons:
        total+=i.maxtotal
    print(f"{obj.name}'s Team [Power:{total}]")
    for i in obj.pokemons:
        num+=1
        print(str(num)+".",i.name)
def match():
    t1=genTrainer()
    t2=genTrainer()
    return t1,t2                        
#E4 Bruno
bruno1=MSteelix(maxiv="Yes",move=["Earthquake","Iron Head", "Curse","Gyro Ball"],nature="Brave",ability="Heatproof")
bruno2=Machamp(name="Machamp(Z-Crystal)",maxiv="Yes",move=["Knock Off","Close Combat","Stone Edge","Facade"],nature="Adamant", ability="Guts")
bruno3=Hitmonchan(maxiv="Yes",move=["Thunder Punch","Close Combat","Fire Punch","Ice Punch"],nature="Adamant")
bruno4=Hitmonlee(maxiv="Yes",move=["Hi Jump Kick","Knock Off","Close Combat","Stone Edge"],nature="Adamant")
bruno5=Steelix(maxiv="Yes",move=["Earthquake","Iron Head", "Curse","Gyro Ball"],nature="Brave",ability="Heatproof")
bruno6=Poliwrath(maxiv="Yes",move=["Close Combat","Liquidation","Recover","Rain Dance"],nature="Adamant")
bruno=Trainer("Elite Four Bruno",[bruno6,bruno2,bruno3,bruno4,bruno5,bruno1])
#E4 Lance
lance1=Dragonite (maxiv="Yes",move=["Dragon Dance","Extreme Speed","Dragon Claw","Roost"],nature="Adamant")
lance2=Gyarados(name="Gyarados⭐",maxiv="Yes",move=["Dragon Dance","Waterfall","Earthquake","Ice Fang"],nature="Adamant")
lance3=Aerodactyl(maxiv="Yes",move=["Stone Edge","Earthquake","Roost","Stealth Rock"],nature="Jolly")
lance4=Dragonite (name="Dragonite(Z-Crystal)",maxiv="Yes",move=["Dragon Dance","Extreme Speed","Dragon Claw","Roost"],nature="Adamant")
lance5=Kingdra(maxiv="Yes",move=["Rain Dance","Draco Meteor","Surf","Ice Beam"],nature="Modest",ability="Swift Swim")
lance6=MCharizardX(maxiv="Yes",move=["Blast Burn","Roost","Dragon Claw","Flare Blitz"],nature="Adamant")
lance=Trainer("Elite Four Lance",[lance1,lance2,lance3,lance6,lance5,lance4])
#E4 Lorelei 
lorelei1=Lapras(name="Lapras(Z-Crystal)",maxiv="Yes",move=["Ice Beam","Hydro Pump","Recover","Thunder"],nature="Modest")
lorelei2=MSlowbro(maxiv="Yes",move=["Slack Off","Flamethrower","Hydro Pump","Ice Beam"],nature="Modest")
lorelei3=Dewgong(maxiv="Yes",move=["Ice Beam","Hydro Pump","Recover","Blizzard"],nature="Modest")
lorelei4=Cloyster(maxiv="Yes",move=["Rock Blast","Pin Missile","Icicle Spears","Shell Smash"],nature="Adamant")
lorelei5=Jynx(maxiv="Yes",move=["Ice Beam","Psychic","Recover","Blizzard"],nature="Timid")
lorelei6=Mamoswine(maxiv="Yes",move=["Ice Beam","Earthquake","Stone Edge","Blizzard"],nature="Naughty")
lorelei=Trainer("Elite Four Lorelei",[lorelei6,lorelei2,lorelei3, lorelei4,lorelei5,lorelei1])
#Red
red1=MCharizardX(maxiv="Yes",move=["Dragon Dance","Dragon Claw","Flare Blitz","Roost"],nature="Jolly")
red2=Blastoise(maxiv="Yes",move=["Hydro Pump","Shell Smash","Water Spout","Ice Beam"],nature="Modest")
red3=Venusaur (maxiv="Yes",move=["Earth Power","Sleep Powder","Sludge Bomb","Giga Drain"],nature="Modest")
red4=Lapras(maxiv="Yes",move=["Hydro Pump","Ice Beam","Thunderbolt","Freeze Dry"],nature="Modest")
red5=Snorlax(maxiv="Yes",move=["Hyper Beam","Body Slam","Return","Double Edge"],nature="Relaxed")
red6=Espeon(maxiv="Yes",move=["Psychic","Dazzling Gleam","Morning Sun","Shadow Ball"],nature="Modest")
red=Trainer("Pokémon Trainer Red",[red4,red5,red6,red2,red3,red1],"Kanto")
#E4 Agatha
agatha1=Crobat(maxiv="Yes",move=["Roost","Toxic","Brave Bird","U-Turn"],nature="Jolly")
agatha2=Mismagius(maxiv="Yes",move=["Thunderbolt","Dazzling Gleam","Shadow Ball","Nasty Plot"],nature="Timid")
agatha3=Arbok(maxiv="Yes",move=["Earthquake","Poison Jab","Crunch","Coil"], nature="Adamant")
agatha4=Weezing(maxiv="Yes",move=["Sludge Bomb","Will-O-Wisp","Flamethrower","Toxic"],nature="Bold")
agatha5=Gengar(name="Gengar(Z-Crystal)",maxiv="Yes",move=["Thunderbolt","Sludge Bomb","Shadow Ball","Nasty Plot"],nature="Timid")
agatha6=MGengar(maxiv="Yes",move=["Thunderbolt","Sludge Bomb","Shadow Ball","Nasty Plot"],nature="Timid")
agatha=Trainer("Elite Four Agatha",[agatha1,agatha2,agatha3,agatha4,agatha5,agatha6],"Kanto")
#Champion Steven
steven1=Claydol(maxiv="Yes",move=["Sandstorm","Ancient Power","Psychic","Calm Mind"],nature="Bold")
steven2=Armaldo(maxiv="Yes",move=["X-Scissor","Stone Edge","Earthquake","Ancient Power"],nature="Adamant")
steven3=Cradily (maxiv="Yes",move=["Giga Drain","Leech Seed","Strength Sap","Ancient Power"],nature="Modest")
steven4=Skarmory(maxiv="Yes",move=["Brave Bird","Roost","Body Press","Toxic"],nature="Impish")
steven5=Aggron(maxiv="Yes",move=["Body Press","Iron Head","Iron Defense","Stone Edge"],nature="Impish")
steven6=MMetagross(name="Mega Metagross⭐",maxiv="Yes", move=["Zen Headbutt","Earthquake","Meteor Mash","Fire Punch"],nature="Adamant")
steven=Trainer("Hoenn Champion Steven",[steven1,steven2,steven3,steven4,steven5,steven6],"Hoenn")
#Champion Wallace
wallace1=Ludicolo(maxiv="Yes",move=["Giga Drain","Rain Dance","Ice Beam","Leech Seed"])
wallace2=Starmie(maxiv="Yes",move=["Psychic","Recover","Surf","Thunderbolt"],nature="Timid")
wallace3=Wailord(maxiv="Yes",move=["Water Spout","Ice Beam","Hydro Pump","Thunder Wave"])
wallace4=Gyarados(maxiv="Yes",move=["Dragon Dance","Waterfall","Earthquake","Crunch"],nature="Adamant")
wallace5=MSwampert(maxiv="Yes",move=["Earthquake","Liquidation","Ice Punch","Hammer Arm"],nature="Adamant")
wallace6=Milotic(maxiv="Yes",move=["Scald","Toxic","Ice Beam","Recover"],nature="Modest")
wallace=Trainer("Hoenn Champion Wallace",[wallace1,wallace2,wallace3,wallace4,wallace5,wallace6],"Hoenn")
#Tobias
tobias1=Darkrai(maxiv="Yes",move=["Dark Void","Shadow Ball","Dark Pulse","Psychic"],nature="Modest")
tobias2=MLatios(maxiv="Yes",move=["Luster Purge","Dragon Pulse","Calm Mind","Shadow Ball"],nature="Timid")
tobias3=Entei(maxiv="Yes",move=["Lava Plume","Stone Edge","Flare Blitz","Fire Blast"],nature="Hasty")
tobias4=Heatran(maxiv="Yes",move=["Magma Storm","Flash Cannon","Ancient Power","Earth Power"],nature="Calm")
tobias5=Latias(maxiv="Yes",move=["Mist Ball","Dragon Pulse","Calm Mind","Shadow Ball"],nature="Timid")
tobias6=Cresselia(maxiv="Yes",move=["Lunar Blessing","Moon Blast","Psychic","Shadow Ball"],nature="Calm")
tobias=Trainer("Pokémon Trainer Tobias",[tobias3,tobias4,tobias5,tobias6,tobias1,tobias2],"Sinnoh")
#Champion Cynthia
cynthia1=WGastrodon(maxiv="Yes",move=["Earth Power","Ice Beam","Recover","Ancient Power"],nature="Calm")
cynthia2=Togekiss(maxiv="Yes",move=["Air Slash","Roost","Moon Blast","Nasty Plot"],nature="Modest")
cynthia3=Lucario(maxiv="Yes",move=["Close Combat","Bullet Punch","Aura Sphere","Bone Rush"],nature="Mild")
cynthia4=Milotic(maxiv="Yes",move=["Ice Beam","Coil","Recover","Scald"],nature="Calm")
cynthia5=Roserade(maxiv="Yes",move=["Sunny Day","Weather Ball","Sludge Bomb","Giga Drain"], nature="Modest")
cynthia6=MGarchomp(maxiv="Yes",move=["Dragon Claw","Dragon Dance","Draco Meteor","Earthquake"],nature="Jolly")
cynthia=Trainer("Sinnoh Champion Cynthia",[cynthia1,cynthia2,cynthia3,cynthia4,cynthia5,cynthia6],"Sinnoh")
#E4 Aaron
aaron1=Yanmega(maxiv="Yes",move=["Air Slash","Bug Buzz","Signal Beam","Ancient Power"],nature="Modest")
aaron2=Vespiquen(maxiv="Yes",move=["Attack Order","Heal Order","Defense Order","Bug Buzz"],nature="Modest")
aaron3=Scizor(maxiv="Yes",move=["U-Turn","Superpower","Bullet Punch","Roost"],nature="Adamant")
aaron4=MHeracross(maxiv="Yes",move=["U-Turn","Close Combat","Megahorn","Brick Break"],nature="Adamant")
aaron5=Flygon(maxiv="Yes",move=["Earthquake","Dragon Claw","Dragon Dance","Sandstorm"], nature="Jolly")
aaron6=Drapion(maxiv="Yes",move=["Wicked Blow","Toxic","Crunch","Cross Poison"],nature="Adamant")
aaron=Trainer("Elite Four Aaron",[aaron1,aaron2,aaron3,aaron4,aaron5,aaron6],"Sinnoh")
#Bertha
bertha1=Golem(maxiv="Yes")
bertha2=Hippowdon(maxiv="Yes")
bertha3=Gliscor(maxiv="Yes")
bertha4=Nidoking (maxiv="Yes")
bertha5=Mamoswine(maxiv="Yes")
bertha6=Rhyperior(maxiv="Yes")
bertha7=MSteelix(maxiv="Yes")
bertha=Trainer("Elite Four Bertha",[bertha1,bertha2,bertha3,bertha4,bertha7,bertha6],"Sinnoh")
#Flint
flint1=Rapidash(maxiv="Yes")
flint2=Entei(maxiv="Yes")
flint3=Magmortar(maxiv="Yes")
flint4=MHoundoom(maxiv="Yes")
flint5=Arcanine(maxiv="Yes")
flint6=Infernape(maxiv="Yes")
flint=Trainer("Elite Four Flint",[flint1,flint2,flint3,flint4,flint5,flint6],"Sinnoh")
#Lucian
lucian1=Farigarif(maxiv="Yes")
lucian2=Espeon(maxiv="Yes")
lucian3=Bronzong(maxiv="Yes")
lucian4=Alakazam(maxiv="Yes")
lucian5=Slowbro(maxiv="Yes")
lucian6=MGallade(maxiv="Yes")
lucian=Trainer("Elite Four Lucian",[lucian1,lucian2,lucian3,lucian4,lucian5,lucian6],"Sinnoh")
#Buck
buck1=Regice(maxiv="Yes")
buck2=Regirock(maxiv="Yes")
buck3=Registeel(maxiv="Yes")
buck4=Cresselia(maxiv="Yes")
buck5=Articuno(maxiv="Yes")
buck6=Suicune(maxiv="Yes")
buck7=Umbreon(maxiv="Yes")
buck8=Dusknoir(maxiv="Yes")
buck9=Claydol(maxiv="Yes")
buck10=Cloyster(maxiv="Yes")
buck11=Steelix(maxiv="Yes")
buck12=Skarmory(maxiv="Yes")
buck13=Bastiodon(maxiv="Yes")
buck14=Probopass(maxiv="Yes")
buck15=Metagross(maxiv="Yes")
buck=Trainer("Pokémon Trainer Buck",[buck1,buck2,buck3,buck4,buck5,buck6],"Sinnoh")
#Palmer
palmer1=Milotic(maxiv="Yes")
palmer2=Rhyperior(maxiv="Yes")
palmer3=Dragonite(maxiv="Yes")
palmer4=Cresselia(maxiv="Yes")
palmer5=Heatran(maxiv="Yes")
palmer6=Regigigas(maxiv="Yes")
palmer=Trainer("Tower Tycoon Palmer",[palmer1,palmer2,palmer3,palmer4,palmer5,palmer6],"Sinnoh")
#Darach
darach1=Staraptor(maxiv="Yes")
darach2=Empoleon(maxiv="Yes")
darach3=Houndoom(maxiv="Yes")
darach4=Entei(maxiv="Yes")
darach5=MGallade(maxiv="Yes")
darach6=Luxray(maxiv="Yes")
darach=Trainer("Castle Velvet Darach",[darach1,darach2,darach3,darach4,darach5,darach6],"Sinnoh")
#Dahlia
dahlia1=Dusknoir(maxiv="Yes")
dahlia2=Medicham(maxiv="Yes")
dahlia3=Ludicolo(maxiv="Yes")
dahlia4=MBlaziken(maxiv="Yes")
dahlia5=Togekiss(maxiv="Yes")
dahlia6=Zapdos(maxiv="Yes")
dahlia=Trainer("Battle Arcade Dahlia",[dahlia1,dahlia2,dahlia3,dahlia5,dahlia4,dahlia6],"Sinnoh")
#Archie
archie1=Mightyena(maxiv="Yes")
archie2=Muk(maxiv="Yes")
archie3=Crobat(maxiv="Yes")
archie4=Tentacruel(maxiv="Yes")
archie5=MSharpedo(maxiv="Yes")
archie6=PKyogre(maxiv="Yes")
archie=Trainer("Aqua Leader Archie",[archie1,archie2,archie3,archie4,archie5,archie6],"Hoenn")
#Maxie
maxie1=Mightyena(maxiv="Yes")
maxie2=Weezing(maxiv="Yes")
maxie3=Crobat(maxiv="Yes")
maxie4=Torkoal(maxiv="Yes")
maxie5=MCamerupt(maxiv="Yes")
maxie6=PGroudon(maxiv="Yes")
maxie=Trainer("Magma Leader Maxie",[maxie1,maxie2,maxie3,maxie4,maxie5,maxie6],"Hoenn")
#Brandon
brandon1=Regice(maxiv="Yes")
brandon2=Regirock(maxiv="Yes")
brandon3=Registeel(maxiv="Yes")
brandon4=Articuno(maxiv="Yes")
brandon5=Zapdos(maxiv="Yes")
brandon6=Moltres(maxiv="Yes")
brandon=Trainer ("Pyramid King Brandon",[brandon1,brandon2,brandon3,brandon4,brandon5,brandon6],"Hoenn")
#Illegal
illegal1=OArceus()
illegal2=Cloyster()
illegal=Trainer("Missing No.",[illegal1,illegal2],"???")
#cyrus
cyrus1=Weavile(maxiv="Yes")
cyrus2=Honchkrow(maxiv="Yes")
cyrus3=Crobat(maxiv="Yes")
cyrus5=Houndoom(maxiv="Yes")
cyrus4=Gyarados (maxiv="Yes")
cyrus8=Entei(maxiv="Yes")
cyrus6=Dialga(maxiv="Yes")
cyrus7=Palkia(maxiv="Yes")
cyrus=Trainer("Galactic Leader Cyrus",[cyrus1,cyrus2,cyrus8,cyrus4,cyrus6,cyrus7],"Sinnoh")
#Saturn
saturn1=Alakazam(maxiv="Yes")
saturn2=Bronzong(maxiv="Yes")
saturn3=Toxicroak(maxiv="Yes")
saturn4=Absol(maxiv="Yes")
saturn5=Crobat(maxiv="Yes")
saturn6=Heatran(maxiv="Yes")
#############
matchx=match()
p1=matchx[0]
p2=matchx[1]
#p1=random.choice([matchx[0],matchx[1]])
#p1=random.choice([red,lance,bruno,lorelei,agatha,steven,wallace,tobias,cynthia,bertha,aaron,lucian,flint,lucian,palmer,buck,darach,dahlia,archie,maxie,brandon])
#p2=random.choice([red,lance,bruno,lorelei,agatha,steven,wallace,cynthia,bertha,aaron,flint,lucian,palmer,buck,darach,dahlia,archie,maxie, brandon])
showparty(p1)
print("")
showparty (p2)
mon1=p1.pokemons[random.randint(1,len(p1.pokemons))-1]
mon2=p2.pokemons[random.randint(1,len(p2.pokemons)-1)]
