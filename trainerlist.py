#pylint:disable=C0103
#pylint:disable=C0103
#pylint:disable=R0915
#pylint:disable=R0912
#pylint:disable=C0303
#pylint:disable=C0114
#pylint:disable=W0401
#pylint:disable=C0301
from pokemonlist import *
from trainers import *
p1AI=True
p2AI=True
#from typematchup import *
def teamset(mons,num=6):
    new=[]
    while len(new)!=num:
        x=random.choice(mons)
        if x not in new:
            new.append(x)
    return new        
def showsmogon(obj):
    text=""
    for i in obj.pokemons:
        x=smogonimport(i)
        if x is not None:
            text+=x+"\n"
        
    return text
def teammaker(trclass=None,trname=None,pknum=6):
    "Creates Team"
    mons=[]
    team=[]
    ultrabeasts=[Blacephalon,Stakataka,Naganadel,UNecrozma,Necrozma,DMNecrozma,DWNecrozma,FMLunala,RSSolgaleo,Lunala,Solgaleo,Guzzlord,Kartana,Celesteela,Xurkitree,Buzzwole,Nihilego,Pheromosa]
    legendary=[Enamorus,TEnamorus,Koraidon,Miraidon,ICalyrex,SCalyrex,Regieleki,Regidrago,Glastrier,Spectrier,Zarude,DUrshifu,WUrshifu,Eternatus,Zamazenta,Zacian,GArticuno,GZapdos,GMoltres,Melmetal,Zeraora,Silvally,Marshadow,Magearna,Tapufini,Tapubulu,Tapulele,Tapukoko,Diancie,MDiancie,UHoopa,Volcanion,CZygarde,Xerneas,Yveltal,Genesect,Keldeo,Meloetta,PMeloetta,BKyurem,WKyurem,Zekrom,Reshiram,Kyurem,TLandous,TThundurus,TTornadus,Thundurus,Tornadus,Landous,Victini,Cobalion,Terrakion,Virizion,Arceus,Shaymin,SShaymin,Darkrai,Cresselia,Manaphy,Uxie,Azelf,Mesprit,Registeel,Regirock,Regice,Articuno,Zapdos,Moltres,Raikou,Entei,Suicune,Lugia,Hooh,Celebi,Deoxys,ADeoxys,SDeoxys,DDeoxys,Jirachi,Mew,Rayquaza,Latias,Latios,MLatias,MLatios,Groudon,Kyogre,PGroudon,PKyogre,MRayquaza,Mewtwo,Dialga,ODialga,Palkia,OPalkia,Giratina,OGiratina,Heatran,Regigigas]
    if trclass in ["UB Expert"]:
        mons=ultrabeasts
    if trclass in ["Johto Trainer"]:
        mons=[Meganium,Typhlosion,Feraligatr, Crobat,Lanturn,Ampharos,MAmpharos,Azumarill,Politoed,Espeon,Umbreon,Steelix,MSteelix, Scizor,MScizor,Heracross,MHeracross,Skarmory,Houndoom,MHoundoom,Kingdra,Blissey,Tyranitar,MTyranitar]
    if trclass in ["Kanto Trainer"]:
        mons=[Ditto,Scyther,Seaking,Rhydon,Chansey,Marowak,Electrode,Hypno,Persian,Dugtrio,Kingler,Wigglytuff,Sandslash,Clefable,Butterfree,Beedrill,Fearow,Pikachu,Venusaur,MVenusaur,Charizard,MCharizardX,MCharizardY,Blastoise,MBlastoise,MBeedrill,Pidgeot,MPidgeot,Arbok, Nidoking,Nidoqueen,Ninetales,Golduck,Primeape,Arcanine,Poliwrath, Alakazam,MAlakazam,Machamp,Victreebel,Tentacruel,Golem,Rapidash,Slowbro,MSlowbro,Dodrio,Dewgong,Muk,Cloyster,Gengar,MGengar,Exeggutor,Hitmonchan,Hitmonlee,Weezing,Kangaskhan,MKangaskhan,Starmie,Tauros,Jynx,Pinsir,MPinsir,Gyarados,MGyarados,Lapras,Jolteon,Vaporeon,Flareon,Omastar,Kabutops,Aerodactyl,MAerodactyl,Snorlax,Dragonite]
    if trclass in ["Hoenn Trainer"]:
        mons=[ Sceptile,MSceptile,Blaziken,MBlaziken,Swampert,MSwampert,Mightyena,Ludicolo,Shiftry,Swellow,Pelipper,Gardevoir,MGardevoir,Breloom, Slaking,Exploud,Hariyama,MSableye,MMawile,Aggron,MAggron,Medicham,MMedicham,MManectric,Sharpedo,MSharpedo,Wailord,Camerupt,MCamerupt,Torkoal,Flygon,Altaria,MAltaria,Zangoose,Seviper,Solrock,Lunatone,Whiscash,Crawdaunt,Claydol,Cradily,Armaldo,Milotic,Banette,MBanette,Absol,MAbsol,Glalie,MGlalie,Walrein,Huntail,Gorebyss,Relicanth,Salamence,MSalamence,Metagross,MMetagross]
    if trclass in ["Sinnoh Trainer"]:
        mons=[Torterra,Infernape,Empoleon,Staraptor,Luxray,Roserade,Rampardos,Bastiodon,Vespiquen,EGastrodon,WGastrodon,Ambipom,Drifblim,MLopunny,Mismagius,Honchkrow,Purugly,Skuntank,Bronzong,Spiritomb,Garchomp,Lucario,MLucario,Hippowdon,MGarchomp,Drapion,Toxicroak,Abomasnow,MAbomasnow,Weavile,Magnezone,Rhyperior,Tangrowth,Electivire,Magmortar,Togekiss,Yanmega,Gliscor,Gallade,MGallade,Probopass,Dusknoir,Froslass,WRotom]
    if trclass in ["Unova Trainer"]:
        mons=[Serperior,Emboar,Samurott,Stoutland,Unfezant,Zebstrika,Gigalith,Excadrill,Conkeldurr,Seismitoad,Leavanny,Scolipede,Krookodile,Darmanitan,Scrafty,Cofagrigus,Carracosta,Archeops,Zoroark,Gothitelle, Reuniclus, Swanna,Vanilluxe,Escavalier,Jellicent,Galvantula,Ferrothorn,Eelektross,Chandelure,Haxorus,Beartic,Accelgor,Mienshao,Druddigon,Golurk,Bisharp,Bouffalant,Braviary,Mandibuzz,Heatmor,Durant,Hydreigon,Volcarona]
#FIGHTING SPECIALIST 
    if trclass in ["Dojo Master","Blackbelt"]:
        namelist=["Taishi","Damme","Wesley","Joe","Dolph"]
        nn=random.choice(namelist)
        new_name=trclass+" "+nn
        mons=[DUrshifu,WUrshifu,Sirfetchd,Grapplot,Sneasler,HDecidueye,Hawlucha,Pangoro,Chesnaught,Mienshao,Scrafty,HLilligant,Conkeldurr,Emboar,MBlaziken,MGallade,Gallade,Machamp,Poliwrath,Hitmonchan,Hitmonlee,Infernape,Blaziken,Breloom,Primeape,Heracross,MHeracross,Hariyama,MMedicham]
   #ELDER TRAINERS     
    if trclass =="Elder Trainer":
        namelist=["Jules","Shriner","Jason","Apollo","Damon","Castor","Marcus","Henry","Orion","Arthur","Julius","Zephyr","Helios","Liam","Odysseus","Albert","Helios"]
        nn=random.choice(namelist)
        new_name=trclass+" "+nn
        mons=[Tyrantrum,Aurorus,Carracosta,MAerodactyl,Aerodactyl,Kabutops,Omastar,Armaldo,Cradily,Rampardos,Bastiodon,Cloyster,Relicanth,Claydol,Arcanine,Mamoswine,Spiritomb,Lunatone,Solrock,Yanmega]+legendary
        mons+=random.choices([Rayquaza,Latias,Latios,Regice,Regirock,Registeel,Kyogre,Groudon,Entei,Suicune,Raikou],k=1)
    if trname is None and trclass not in ["Elder Trainer","Dojo Master",",Blackbelt", "Egyptian","Exorcist"]:
        namelist=["Josh","Kyler","Jade","John","Joey","Jan","Gabriel","Jamie","Kylie","Andrea","Evy","Ebba","Titus","Emiliano","Emilia","Natalie","Justin","Anastasia","Frannie","Danielle","Daniel","Hugo","Robert","Carlos","Alex","Alexander","Alexandra","Arslan","Johan","Mike","Julian","Selena","Emmanuel","Kristin","Lawrence","Frank","Pamela","Nicole","Emma","Matthew"]
        nn=random.choice(namelist)
        new_name=trclass+" "+nn
        #STEEL
    if trclass in ["Factory Boss","Industry Worker"]:
        mons=[ADugtrio,ASandslash,Duraludon,Copperajah,Perrserker,Corviknight,Dhelmise,HGoodra,Aegislash,Bisharp,Magnezone,Steelix,MSteelix,Scizor,MScizor,Skarmory,MMawile,Aggron,MAggron,Metagross,MMetagross,Empoleon,Bastiodon,Bronzong,Lucario,MLucario,Probopass,Heatran,Excadrill,Ferrothorn,Escavalier]
        #Ghost
    if trclass == "Exorcist":
        namelist=["Gabrielle","Candido","Bishop","William","Bowden","Joseph","Thomas","Fantino","Angelo"]
        nn=random.choice(namelist)
        new_name=trclass+" "+nn
        mons=[AMarowak,Dragapult,Polteageist,Mimikyu,Decidueye,Gourgeist,Aegislash,Trevenant,Golurk,Gengar,MGengar,HTyphlosion,MSableye,Banette,MBanette,Dusknoir,Drifblim,Mismagius,Spiritomb,Froslass,Cofagrigus,Runerigus,HZoroark,Jellicent,Chandelure]
        #Psychic
    if trclass == "Psychic":
        mons=[MrMime,Hypno,Indeedee,GSlowking,GSlowbro,GRapidash,Wyrdeer,Malamar,Delphox,HBraviary,Alakazam,MAlakazam,Slowbro,MSlowbro,Exeggutor,Starmie,Jynx,Espeon,Farigarif,Gardevoir,MGardevoir,Medicham,MMedicham,Lunatone,Solrock,Claydol,Metagross,MMetagross, Bronzong,Gallade,MGallade,Gothitelle,Reuniclus]
        #Grass
    if trclass == "Gardener":
        mons=[Parasect,Vileplume,Flapple,Appletun,Rillaboom,Dhelmise,Tsareena,HElectrode,HDecidueye,Gourgeist,Decidueye,Trevenant,Gogoat,Florges,Venusaur,MVenusaur,Victreebel,Exeggutor,AExeggutor,Tangrowth,Meganium,Sceptile,MSceptile,Ludicolo,Shiftry,Breloom,Roserade,Cradily,Torterra,Abomasnow,MAbomasnow,Serperior,Leavanny,HLilligant,Ferrothorn]+random.choices([Shaymin,SShaymin],k=1)
        #ANIMAL LOVERS
    if trclass == "Zoologist":
        mons=[Persian,APersian,Bewear,MDLycanroc,DLycanroc,Gogoat,Pangoro,Pyroar,Bouffalant,Krookodile,Feraligatr,Stoutland,Zebstrika,Ursaluna,Gliscor,Ambipom,Torterra,Farigarif,Sceptile,Houndoom,Tauros,Kangaskhan,Rapidash,Dodrio, Victreebel,Arcanine,Breloom]
        #BUG
    if trclass == "Bug Catcher":
        mons=[Scyther,Venomoth,Parasect,Butterfree,Beedrill,Frosmoth,Kleavor,Centiskorch,Orbeetle,Golisopod,Araquanid,Vikavolt,Volcarona,Durant,Accelgor,Galvantula,Escavalier,Scolipede,Leavanny,Scizor,Heracross,Pinsir,Drapion,Vespiquen,Yanmega,MScizor,MHeracross,MPinsir]        
        #ICE SPECIALISTS
    if trclass in ["Skier","Boarder"]:
        mons=[ASandslash,Cetitan,Frosmoth,MrRime,Avalugg,HAvalugg,Aurorus,Beartic,Vanilluxe,GDarmanitan,Weavile,Abomasnow,Walrein,Lapras,Mamoswine,Glalie,MGlalie,Jynx,Cloyster,ANinetales,MAbomasnow]
        ch=random.randint(1,10)
        if ch==7:
            mons+=[Articuno]
#ROCK SPECIALISTS
    if trclass in ["Ruin Explorer","Hiker"]:
     mons=[Rhydon,Coalossal,Gigalith,Lunatone,Solrock,Probopass,HArcanine,Runerigus,Cofagrigus,Gigalith,MTyranitar,MAggron,Rhyperior,Aggron,Steelix,Machamp,Tyranitar,Golem]
#fossil
    if trclass in ["Fossil Maniac","Paleontologist"]:
        mons=[Dracovish,Dracozolt,Tyrantrum,Aurorus,Archeops,Carracosta,Omastar,Kabutops,MAerodactyl,Armaldo,Cradily,Aerodactyl,Mamoswine,Bastiodon,Rampardos,Relicanth]
#Ground
    if trclass in ["Desert Explorer","Egyptian"]:
        if trclass=="Egyptian":
            namelist=["Wongani","Abdelhamid","Ali","Zafar","Saif","Hakeem","Ziyad","Hamed","Daud","Apis","Amon","Aton"]
            nn=random.choice(namelist)
            new_name=trclass+" "+nn
        mons=[Rhydon,Marowak,Dugtrio,ADugtrio,Sandslash,Sandaconda,Palossand,Mudsdale,Mandibuzz,Golurk,Drapion,Camerupt,MCamerupt,Hippowdon,Nidoking,Nidoqueen,Golem,Gliscor,Steelix,MSteelix,Rhyperior,Mamoswine,Swampert,MSwampert,Flygon,Whiscash,Claydol,Torkoal,Torterra,EGastrodon,WGastrodon,Garchomp,MGarchomp,Seismitoad,Krookodile,Excadrill,Arbok]
#WATER SPECIALISTS
    if trclass in ["Marine Biologist","Surfer","Scuba Diver","Swimmer","Sailor","Captain","Pirate"]:
        mons=[Seaking,Kingler,Dracovish,Barraskewda,Inteleon,Araquanid,Toxapex,SWishiwashi,Primarina,Clawitzer,Barbaracle,Greninja,Jellicent,Swanna,Carracosta,Basculegion,Seismitoad,HSamurott,Samurott,MSharpedo,MSwampert,MBlastoise,Phione,EGastrodon,WGastrodon,Empoleon,Walrein,Huntail,Gorebyss,Relicanth,Milotic,Crawdaunt,Whiscash,Dewgong,Sharpedo,Pelipper,Kingdra,Politoed,Azumarill,Feraligatr,Lanturn,Lapras,Gyarados,Slowbro,Cloyster,Starmie, Blastoise,Poliwrath,Swampert,Ludicolo]+random.choices([Manaphy, Wailord],k=1)
#GRUNTS
    if trclass in ["Aqua Grunt"]:
        mons=[Crawdaunt,Sharpedo,Crobat,Mightyena,Muk,Weezing,Tentacruel,Wailord,MSharpedo]       
    if trclass in ["Magma Grunt"]:
        mons=[Camerupt,Torkoal,Crobat,Mightyena,Muk,Weezing,Magmortar,MCamerupt]           
    if trclass in ["Rocket Grunt"]:
        mons=[Arbok,Weezing,Victreebel,Muk,Crobat,Seviper,Houndoom,Yanmega, Machamp]
    if trclass in ["Galactic Grunt"]:
        mons=[Purugly,Skuntank,Weavile,Bronzong,Crobat,Toxicroak,Muk,Weezing,Magnezone,Electivire,Magmortar,Rhyperior,Probopass,Gyarados]
#DRAGON SPECIALISTS
    if trclass in ["Dragon Tamer"]:
        mons=[Dragapult,Duraludon,Dracovish,Dracozolt,Flapple,Appletun,MSceptile,Kommo,Drampa,Turtonator,Noivern,HGoodra,Goodra,Hydreigon,Druddigon,Haxorus,Krookodile,Serperior,Yanmega,Garchomp,MGarchomp,Gyarados,MGyarados,Dragonite,Kingdra,Charizard,Aerodactyl,Tyranitar, Salamence,MSalamence,MAerodactyl,MCharizardX,MTyranitar,Feraligatr]+random.choices([Latias,Latios,MLatias,MLatios],k=1)
    if trclass in ["Police Officer","Investigator"]:
        mons=[Arcanine,HArcanine,Machamp, Stoutland,MManectric,Lapras,Swanna,Mightyena]
#POISON SPECIALISTS
    if trclass in ["Venom Expert"]:
        mons=[Venomoth,Vileplume,Toxtricity,GSlowking,GWeezing,GSlowbro,Salazzle,Sneasler,Dragalge,Toxicroak,Drapion,Roserade,Seviper,Arbok,Weezing,Crobat,MBeedrill,Venusaur,Nidoking,Nidoqueen,Victreebel,Tentacruel,Muk,Gengar,Overqwil]
#ELECTRIC
    if trclass in ["Rocker","Guitarist","Electrician"]:
        mons=[Electrode,Raichu,ARaichu,Pikachu,Dracozolt,Toxtricity,Vikavolt,HElectrode,Eelektross,Galvantula,MManectric,AGolem,Magnezone,Jolteon,Electivire,Lanturn,Ampharos,MAmpharos,Luxray,WRotom,Zebstrika]        
#FIRE SPECIALISTS
    if trclass in ["Kindler","Fiery Breathe"]:
        mons=[AMarowak,Centiskorch,Coalossal,Cinderace,Turtonator,Salazzle,Incineroar,Pyroar,Talonflame,Delphox,Volcarona,Heatmor,Chandelure,Darmanitan,HTyphlosion,Emboar,HArcanine,Magmortar,Infernape,Arcanine,Rapidash,Houndoom,Flareon,Typhlosion,Blaziken,Camerupt,Charizard,MCharizardY]
#FLYING SPECIALISTS
    if trclass in ["Bird Keeper","Pilot","Sky Diver"]:
        mons=[Corviknight,Toucannon,Noivern,Hawlucha,Talonflame,Mandibuzz,HBraviary,Braviary,Swanna,Archeops,Unfezant,Gliscor,Togekiss,Honchkrow,Staraptor,Empoleon,Flygon,Salamence,Pelipper,Swellow,MPidgeot,Charizard,Skarmory,Aerodactyl,Altaria,Crobat,Dodrio,Dragonite]
        mons+=random.choices([Articuno,Zapdos,Moltres,Latias,Latios,MLatias,MLatios,Thundurus,Landous,Tornadus,Enamorus],k=1)        
        #DECENT TRAINERS
    if trclass in ["Expert","Veteran","Businessman"]:
        mons=[Ditto,Chansey,Persian,Vileplume,Wigglytuff,Clefable,Pikachu,Raticate,ARaticate,Butterfree,Beedrill,MDLycanroc,MNLycanroc,DLycanroc,Aegislash,Delphox,Greninja,Chesnaught,Basculegion,Stoutland,Probopass,Ursaluna,Yanmega,Magnezone,Tangrowth,Hippowdon,Lucario,Mismagius,Luxray,Roserade,Torterra,Glalie,Absol,Banette,Milotic,Armaldo,Cradily,Aggron,Hariyama,Breloom,Gardevoir,Swellow,Ludicolo,Swampert,Houndoom,Heracross,Steelix,Espeon,Ampharos,Flareon,Jolteon,Vaporeon,Snorlax,Lapras,Gyarados,Tauros,Kangaskhan,Hitmonchan,Hitmonlee,Exeggutor,Gengar,Dodrio,Slowbro,Rapidash,AGolem,Victreebel,Machamp,Golduck,Alakazam,Pidgeot,Blastoise,Ninetales,Primeape,MBeedrill, Venusaur, Charizard,Cloyster,MBanette,MGlalie]
        ch=random.randint(1,15)
        if ch==7:
            mons+=random.choices(legendary,k=1)
        pass
#THUGS
    if trclass in[ "Street Punk","Biker","Cueball","Smuggler","Thief","Goon","Driver"]:
        namelist=["Josh","Kyler","Jade","John","Jan","Gabriel","Jamie","Emiliano","Justin","Frannie","Danielle","Daniel","Hugo","Robert","Carlos","Alex","Alexander","Arslan","Johan","Mike","Julian","Emmanuel","Kristin","Murphy"]
        nn=random.choice(namelist)
        new_name=trclass+" "+nn
        mons=[Ditto,APersian,ARaticate,Obstagoon,Grimmsnarl,MNLycanroc,Incineroar,Sneasler,Skuntank,Dragalge,Malamar,Pangoro,Greninja,Chesnaught,Hydreigon,Eelektross,HZoroark,Zoroark,Scrafty,Krookodile,HLilligant,HSamurott,Drapion,Toxicroak,Absol,Crawdaunt,Seviper,Zangoose,Overqwil,Sharpedo,MManectric,MAggron,Hariyama,Breloom,Shiftry,Blaziken,MHoundoom,Gyarados,Pinsir,Weezing,Muk,Tentacruel,Primeape,Machamp,Golem,Cloyster,MSableye,Crobat,Arbok]
        ch=random.randint(1,10)
        if ch==7:
            mons+=random.choices(legendary,k=1)
        pass 

    if trclass == "Air Force Officer":
        mons=[Skarmory,Corviknight,Magnezone,Latios,Latias,Pidgeot,Staraptor,Braviary,Altaria,MAltaria,Dragonite,Salamence,Metagross]
    if trclass == "Navy Officer":
        mons=[Gyarados,Blastoise,Swampert,Feraligatr,Inteleon,Wailord,Starmie]
    if trclass == "Military Officer":
        mons=[Aggron,Salamence,Tyranitar,Steelix,Rhyperior,Magnezone,Metagross,Dragonite,Magmortar,Electivire,Charizard, Blastoise]
    if trclass == "Tamer":
        mons=[GRapidash,Bewear,MDLycanroc,MNLycanroc,DLycanroc,Wyrdeer,Pangoro,Braviary,Tauros,Arbok,Arcanine,HArcanine,Rapidash,Ambipom,Ursaluna,Mamoswine,Houndoom,MHoundoom,Mightyena,Slaking,MManectric,Sharpedo,MSharpedo,Wailord,Zangoose,Seviper,Milotic,Absol,MAbsol,Walrein,Empoleon,Infernape,Luxray]+random.choices([Raikou,Suicune,Entei,Cobalion,Virizion,Terrakion])
            
     #BETTER TRAINERS
    if trclass == "Ace Trainer":
        mons=[Clefable,Kleavor,Obstagoon,Grimmsnarl,Polteageist,Toxtricity,Silvally,MDLycanroc,MNLycanroc,DLycanroc,Primarina,Incineroar,Aegislash,Florges,AGreninja,Volcarona,Hydreigon,Mandibuzz,Braviary,Bouffalant,Bisharp,Mienshao,Haxorus,Eelektross,Ferrothorn,Gothitelle,Reuniclus,HZoroark,Zoroark,Archeops,Cofagrigus,Scrafty,Darmanitan,Krookodile,Basculegion,Conkeldurr,Excadrill,Gigalith,Heatran,Dusknoir,Ursaluna,HArcanine,PorygonZ,Gliscor,Yanmega,Togekiss,Electivire,Rhyperior,Magnezone,Lucario,Drifblim,Roserade,Staraptor,Empoleon,Torterra,Infernape,Metagross,Salamence,Absol,Milotic,Altaria,Flygon,Wailord,MManectric,MGardevoir,Swellow,Ludicolo,Swampert,Blaziken,Kingdra,MHoundoom,Skarmory,Heracross,Scizor,MSteelix,Espeon,Umbreon,MAmpharos,Feraligatr,Typhlosion,Meganium,Dragonite,Snorlax,MGyarados,Tauros,MPinsir,Starmie,AMuk,AExeggutor,MGengar,Cloyster,MSlowbro,Golem,MAlakazam,MPidgeot,Poliwrath,Arcanine,ANinetales,Nidoking, Nidoqueen,MCharizardY,MVenusaur,MBlastoise,MSceptile,MCamerupt]
        ch=random.randint(1,5)
        if ch==3:
            mons+=random.choices(legendary,k=1)
            
        
#CHALLENGERS
    if trclass == "Challenger":
        mons=[DUrshifu,WUrshifu,Hatterene,Grimmsnarl,Toxtricity,Appletun,Corviknight,Melmetal,Zeraora,Silvally,Incineroar,Aegislash,AGreninja,Volcarona,Hydreigon,Mandibuzz,Bisharp,Mienshao,Ferrothorn,Reuniclus,HZoroark,Zoroark,Darmanitan,GDarmanitan,Krookodile,Conkeldurr,Excadrill,Heatran,Uxie,Mesprit,Azelf,WRotom,Togekiss,Magnezone,Garchomp,Infernape,Latias,Latios,Metagross,Salamence,Slaking,Blissey,Kingdra,Skarmory,Umbreon,Crobat,Cloyster,Starmie,AExeggutor,Typhlosion,Feraligatr,Meganium,Arcanine,Snorlax,Dragonite]+[MSharpedo,MScizor,MSteelix,MGyarados,MKangaskhan,MAlakazam,MPidgeot,MSlowbro,MAerodactyl,MBlastoise,MVenusaur,MCharizardX,MCharizardY,MHeracross,MHoundoom,MSceptile, MBlaziken,MSwampert,MGardevoir,MCamerupt,MAbsol,MSalamence,MMetagross,MLopunny,MLucario]+ultrabeasts
        ch=random.randint(1,3)
        if ch==2:
            mons+=random.choices(legendary,k=3)
        pass


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

                                                                                
                     
    return new_name,team            

def genTrainer(name=None,num=6,ai=True):
    trclasslist=["Blackbelt","Dojo Master","Dragon Tamer","Skier","Kindler","Sailor","Swimmer","Veteran","Elder Trainer","Challenger","Zoologist","Ruin Explorer","Ace Trainer","Expert","Street Punk","Scuba Diver","Fossil Maniac","Paleontologist","Surfer","Marine Biologist","Biker","Cueball","Bird Keeper","Pilot","Sky Diver","Venom Expert","Fiery Breathe","Rocker","Guitarist","Bug Catcher","Psychic","Exorcist","Electrician","Smuggler","Thief","Goon","Boarder","Desert Explorer","Egyptian","Tamer","Captain","Pirate","Driver","Magma Grunt","Aqua Grunt","Rocket Grunt","Galactic Grunt","Gardener","Factory Boss","Industry Worker","Hiker","Kanto Trainer","Johto Trainer","Hoenn Trainer","Sinnoh Trainer","Unova Trainer","UB Expert","Businessman","Police Officer","Investigator","Military Officer","Navy Officer","Air Force Officer"]
    rclass=random.choice(trclasslist)
    trainer=teammaker(rclass,name,num)
    rname=trainer[0]
    rteam=trainer[1]
    rand=Trainer(rname,rteam,ai=ai)
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
    t1=genTrainer(ai=p1AI)
    t2=genTrainer(ai=p2AI)
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
lance1=Hydreigon(maxiv="Yes",move=["Dark Pulse","Flamethrower","Thunderbolt","Dragon Pulse"],nature="Modest")
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
lorelei4=Cloyster(maxiv="Yes",move=["Rock Blast","Pin Missile","Icicle Spear","Shell Smash"],nature="Adamant")
lorelei5=Jynx(maxiv="Yes",move=["Ice Beam","Psychic","Recover","Blizzard"],nature="Timid")
lorelei6=Mamoswine(maxiv="Yes",move=["Ice Beam","Earthquake","Stone Edge","Blizzard"],nature="Naughty")
lorelei=Trainer("Elite Four Lorelei",[lorelei6,lorelei2,lorelei3, lorelei4,lorelei5,lorelei1])
#Red
red1=MCharizardX(maxiv="Yes",move=["Dragon Dance","Dragon Claw","Flare Blitz","Roost"],nature="Jolly")
red2=Blastoise(maxiv="Yes",move=["Hydro Pump","Shell Smash","Water Spout","Ice Beam"],nature="Modest")
red3=Venusaur (maxiv="Yes",move=["Earth Power","Sleep Powder","Sludge Bomb","Giga Drain"],nature="Modest")
red4=Lapras(maxiv="Yes",move=["Hydro Pump","Ice Beam","Thunderbolt","Freeze-Dry"],nature="Modest")
red5=Snorlax(maxiv="Yes",move=["Hyper Beam","Body Slam","Return","Double-Edge"],nature="Relaxed")
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
steven4=Skarmory(maxiv="Yes",move=["Brave Bird","Roost","Body Press","Stealth Rock"],nature="Impish")
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
tobias6=Cresselia(maxiv="Yes",move=["Lunar Blessing","Moonblast","Psychic","Shadow Ball"],nature="Calm")
tobias=Trainer("Pokémon Trainer Tobias",[tobias3,tobias4,tobias5,tobias6,tobias1,tobias2],"Sinnoh")
#Champion Cynthia
cynthia1=WGastrodon(maxiv="Yes",move=["Earth Power","Ice Beam","Recover","Ancient Power"],nature="Calm")
cynthia2=Togekiss(maxiv="Yes",move=["Air Slash","Roost","Moonblast","Nasty Plot"],nature="Modest")
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
aaron7=Armaldo(maxiv="Yes")
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
buckteam=teamset([buck1,buck2,buck3,buck4,buck5,buck6,buck7,buck8,buck9,buck10,buck11,buck12,buck13,buck14,buck15])
buck=Trainer("Pokémon Trainer Buck",buckteam,"Sinnoh")
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
darach6=Alakazam(maxiv="Yes")
darach7=Metagross(maxiv="Yes")
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
archie7=Walrein(maxiv="Yes")
archie1=Mightyena(maxiv="Yes")
archie2=Muk(maxiv="Yes")
archie3=Crobat(maxiv="Yes")
archie4=Tentacruel(maxiv="Yes")
archie5=MSharpedo(maxiv="Yes")
archie6=PKyogre(maxiv="Yes")
archieteam=teamset([archie1,archie2,archie3,archie4,archie5],5)+[archie6]
archie=Trainer("Aqua Leader Archie",archieteam,"Hoenn")
#Maxie
maxie7=Houndoom(maxiv="Yes")
maxie1=Mightyena(maxiv="Yes")
maxie2=Weezing(maxiv="Yes")
maxie3=Crobat(maxiv="Yes")
maxie4=Torkoal(maxiv="Yes")
maxie5=MCamerupt(maxiv="Yes")
maxie6=PGroudon(maxiv="Yes")
maxie=Trainer("Magma Leader Maxie",[maxie1,maxie2,maxie3,maxie4,maxie5,maxie6],"Hoenn")
#Tabitha
tab1=Mightyena(maxiv="Yes")
tab2=Weezing(maxiv="Yes")
tab3=Crobat(maxiv="Yes")
tab4=Torkoal(maxiv="Yes")
tab5=Camerupt(maxiv="Yes")
tab6=Swellow(maxiv="Yes")
tabitha=Trainer("Magma Admin Tabitha",[tab1,tab2,tab3,tab4,tab5,tab6],"Hoenn")
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
saturn=Trainer("Galactic Commander Saturn",[saturn1,saturn2,saturn3,saturn4,saturn5,saturn6],"Sinnoh")
#E4 Siebold
siebold1=Clawitzer(maxiv="Yes")
siebold2=Gyarados(maxiv="Yes")
siebold3=Starmie(maxiv="Yes")
siebold4=Barbaracle(maxiv="Yes")
siebold5=Milotic(maxiv="Yes")
siebold6=MBlastoise(maxiv="Yes")
siebold=Trainer("Elite Four Siebold",[siebold1,siebold2,siebold3,siebold4,siebold5,siebold6],"Kalos")
#E4 Wikstrom
wikstrom1=Probopass(maxiv="Yes")
wikstrom2=Aegislash (maxiv="Yes")
wikstrom3=Escavalier(maxiv="Yes")
wikstrom4=HGoodra(maxiv="Yes")
wikstrom5=Klefki(maxiv="Yes")
wikstrom6=MScizor(maxiv="Yes")
wikstrom=Trainer("Elite Four Wikstrom",[wikstrom1,wikstrom2,wikstrom3,wikstrom4,wikstrom5,wikstrom6],"Kalos")
#E4 Drasna
drasna1=Druddigon(maxiv="Yes")
drasna2=Dragalge(maxiv="Yes")
drasna3=Noivern(maxiv="Yes")
drasna4=Goodra(maxiv="Yes")
drasna5=Tyrantrum(maxiv="Yes")
drasna6=MAltaria(maxiv="Yes")
drasna=Trainer("Elite Four Drasna",[drasna1,drasna2,drasna3,drasna4,drasna5,drasna6],"Kalos")
#E4 Malva
malva1=Talonflame(maxiv="Yes")
malva2=Pyroar(maxiv="Yes")
malva3=Torkoal(maxiv="Yes")
malva4=Chandelure(maxiv="Yes")
malva5=Delphox(maxiv="Yes")
malva6=MHoundoom(maxiv="Yes")
malva7=Yveltal(maxiv="Yes")
malva=Trainer("Elite Four Malva",[malva1,malva2,malva4,malva5,malva6,malva7],"Kalos")
#n
n1=Carracosta(maxiv="Yes")
n2=Vanilluxe(maxiv="Yes")
n3=Archeops(maxiv="Yes")
n4=Zoroark(maxiv="Yes")
n5=Zekrom(maxiv="Yes")
n6=Reshiram(maxiv="Yes")
n=Trainer("Pokémon Trainer N",[n1,n2,n3,n4,n5,n6],"Unova")
#Ghetsis
ghet4=Hydreigon(maxiv="Yes")
ghet2=Bisharp(maxiv="Yes")
ghet3=Drapion(maxiv="Yes")
ghet1=Seismitoad(maxiv="Yes")
ghet5=WKyurem(maxiv="Yes")
ghet6=BKyurem(maxiv="Yes")
ghet7=Cofagrigus(maxiv="Yes")
ghet8=Bouffalant(maxiv="Yes")
ghet9=Eelektross(maxiv="Yes")
ghet10=Toxicroak(maxiv="Yes")
ghetsis=Trainer("Plasma Leader Ghetsis",[ghet9,ghet3,ghet2,ghet4,ghet5,ghet6],"Unova")
#Alain
alain1=Tyranitar(maxiv="Yes",move=["Dark Pulse","Stone Edge","Crunch","Stealth Rock"],nature="Brave")
alain2=Bisharp(maxiv="Yes",move=["Thunder Wave","Focus Blast","Iron Head","Night Slash"],item="Life Orb")
alain3=Unfezant(maxiv="Yes",move=["Sky Attack","Steel Wing","Hurricane","Air Slash"])
alain4=Metagross(maxiv="Yes",move=["Meteor Mash","Psyshock","Rock Slide","Zen Headbutt"],nature="Naughty")
alain5=Weavile(maxiv="Yes",move=["Protect","Night Slash","Ice Beam","Ice Shard"],nature="Hasty")
alain6=MCharizardX(maxiv="Yes",move=["Flamethrower","Dragon Claw","Thunder Punch","Blast Burn"],nature="Hasty")
alain7=Malamar(maxiv="Yes")
alain8=Chesnaught(maxiv="Yes")
alainteam=teamset([alain1,alain2,alain3,alain4,alain5,alain7,alain8],5)+[alain6]
alain=Trainer("Pokémon Trainer Alain",alainteam,"Unova")
#Anabel
anabel1=Alakazam(maxiv="Yes")
anabel2=Latios(maxiv="Yes")
anabel3=Snorlax(maxiv="Yes")
anabel4=Entei(maxiv="Yes")
anabel5=Raikou(maxiv="Yes")
anabel6=MLucario(maxiv="Yes")
anabel=Trainer("Frontier Brain Anabel",[anabel1,anabel2,anabel3,anabel4,anabel5,anabel6],"Hoenn")
#greta
greta1=Heracross(maxiv="Yes")
greta2=Breloom(maxiv="Yes")
greta3=Umbreon(maxiv="Yes")
greta4=Gengar(maxiv="Yes")
greta5=Hariyama(maxiv="Yes")
greta6=MMedicham(maxiv="Yes")
greta=Trainer("Frontier Brain Greta",[greta1,greta2,greta3,greta4,greta5,greta6],"Hoenn")
#Tucker
tucker1=Metagross(maxiv="Yes")
tucker2=Arcanine(maxiv="Yes")
tucker3=Charizard(maxiv="Yes")
tucker4=Salamence(maxiv="Yes")
tucker5=Latias(maxiv="Yes")
tucker6=MSwampert(maxiv="Yes")
tucker=Trainer ("Dome Ace Tucker",[tucker1,tucker2,tucker3,tucker4,tucker5,tucker6],"Hoenn")
#Lucy
lucy1=Arbok(maxiv="Yes")
lucy2=Snorlax(maxiv="Yes")
lucy3=Steelix(maxiv="Yes")
lucy4=Gyarados(maxiv="Yes")
lucy5=Milotic(maxiv="Yes")
lucy6=Seviper(maxiv="Yes")
lucy=Trainer ("Pike Queen Lucy",[lucy1,lucy2,lucy3,lucy4,lucy5,lucy6],"Hoenn")
#spenser
spenser1=Arcanine(maxiv="Yes")
spenser2=Lapras(maxiv="Yes")
spenser3=Slaking(maxiv="Yes")
spenser4=Crobat(maxiv="Yes")
spenser5=Suicune(maxiv="Yes")
spenser6=MVenusaur(maxiv="Yes")
spenser=Trainer("Battle Frontier Spenser",[spenser1,spenser2,spenser3,spenser4,spenser5,spenser6],"Hoenn")
#Giovanni
gio1=Nidoqueen(maxiv="Yes")
gio2=Nidoking(maxiv="Yes")
gio3=Honchkrow(maxiv="Yes")
gio4=Rhyperior(maxiv="Yes")
gio5=MKangaskhan(maxiv="Yes")
gio6=Mewtwo(maxiv="Yes")
giovanni=Trainer("Rocket Boss Giovanni",[gio1,gio2,gio3,gio4,gio5,gio6],"Kanto")
#Archie
archer1=HElectrode(maxiv="Yes")
archer2=Mightyena(maxiv="Yes")
archer3=Weezing(maxiv="Yes")
archer4=Crobat(maxiv="Yes")
archer5=Tyranitar(maxiv="Yes")
archer6=MHoundoom(maxiv="Yes")
archer=Trainer("Rocket Commander Archer",[archer1,archer2,archer3,archer4,archer5,archer6],"Kanto")
#Ariana
ariana1=Muk(maxiv="Yes")
ariana2=Honchkrow(maxiv="Yes")
ariana3=Weavile(maxiv="Yes")
ariana4=Crobat(maxiv="Yes")
ariana5=Arbok(maxiv="Yes")
ariana6=MMawile(maxiv="Yes")
ariana=Trainer("Rocket Commander Ariana",[ariana1,ariana2,ariana3,ariana4,ariana5,ariana6],"Kanto")
#Silver
silver1=Weavile (maxiv="Yes")
silver2=Honchkrow(maxiv="Yes")
silver3=Kingdra(maxiv="Yes")
silver4=Ursaluna(maxiv="Yes")
silver5=MGyarados(name="Mega Gyarados⭐",maxiv="Yes")
silver6=Feraligatr(maxiv="Yes")
silver=Trainer("Pokémon Trainer Silver",[silver1,silver2,silver3,silver4,silver5,silver6],"Johto")
#Gary
gary1=Arcanine(maxiv="Yes")
gary2=Nidoking(maxiv="Yes")
gary3=Scizor(maxiv="Yes")
gary4=Umbreon(maxiv="Yes")
gary5=Electivire(maxiv="Yes")
gary6=MBlastoise(maxiv="Yes")
gary7=Nidoqueen(maxiv="Yes")
gary8=Dodrio(maxiv="Yes")
gary9=Tyranitar(maxiv="Yes")
gary10=Hatterene(maxiv="Yes")
gary11=Regidrago(maxiv="Yes")
gary12=Golem(maxiv="Yes")
gary13=Skarmory (maxiv="Yes")
gary14=Houndoom(maxiv="Yes")
gary15=Alakazam(maxiv="Yes")
gary16=Kingdra(maxiv="Yes")
garyteam=teamset([gary1,gary2,gary3,gary7,gary8,gary9,gary10,gary11,gary12,gary13,gary14,gary15,gary16],3)+[gary4,gary5,gary6]
gary=Trainer("Researcher Gary Oak",garyteam,"Kanto")
#Blue
blue1=Exeggutor(maxiv="Yes")
blue2=Alakazam(maxiv="Yes")
blue3=Rhyperior(maxiv="Yes")
blue4=Gyarados(maxiv="Yes")
blue5=Arcanine(maxiv="Yes")
blue6=MPidgeot(maxiv="Yes")
blue=Trainer("Pokémon Trainer Blue",[blue1,blue2,blue3,blue4,blue5,blue6],"Kanto")
#Ethan
ethan1=Tauros(maxiv="Yes")
ethan2=Tangrowth(maxiv="Yes")
ethan3=PorygonZ(maxiv="Yes")
ethan4=Azumarill(maxiv="Yes")
ethan5=Venusaur(maxiv="Yes")
ethan6=Typhlosion(maxiv="Yes")
ethan=Trainer ("Pokémon Trainer Ethan",[ethan1,ethan2,ethan3,ethan4,ethan5,ethan6],"Johto")
#Kukui
kukui1=Braviary(maxiv="Yes")
kukui2=Venusaur(maxiv="Yes")
kukui3=Empoleon(maxiv="Yes")
kukui4=Lucario(maxiv="Yes")
kukui5=MDLycanroc(maxiv="Yes")
kukui6=Incineroar(name="Incineroar (Z-Crystal)",maxiv="Yes")
kukui=Trainer("Professor Kukui",[kukui1,kukui2,kukui3,kukui4,kukui5,kukui6],"Alola")
#Brendan
bren1=Gardevoir(maxiv="Yes")
bren2=Ludicolo(maxiv="Yes")
bren3=Swellow(maxiv="Yes")
bren4=Breloom(maxiv="Yes")
bren5=Latios(maxiv="Yes")
bren6=MSceptile(maxiv="Yes")
brendan=Trainer("Pokémon Trainer Brendan",[bren1,bren2,bren3,bren4,bren5,bren6],"Hoenn")
#Ingo
ingo1=Gliscor(maxiv="Yes")
ingo2=Alakazam(maxiv="Yes")
ingo3=Tangrowth(maxiv="Yes")
ingo4=Machamp(maxiv="Yes")
ingo5=Probopass(maxiv="Yes")
ingo6=Magnezone(maxiv="Yes")
ingo7=Haxorus(maxiv="Yes")
ingo=Trainer("Subway Boss Ingo",[ingo1,ingo2,ingo3,ingo4,ingo5,ingo6],"Unova")
#Phoebe
phoebe1=Banette(maxiv="Yes")
phoebe2=Mismagius(maxiv="Yes")
phoebe3=Drifblim(maxiv="Yes")
phoebe4=Chandelure(maxiv="Yes")
phoebe5=Dusknoir(maxiv="Yes")
phoebe6=MSableye(maxiv="Yes")
phoebe=Trainer ("Elite Four Phoebe",[phoebe1,phoebe2,phoebe3,phoebe4,phoebe5,phoebe6],"Hoenn")
#Sidney
sidney1=Shiftry(maxiv="Yes")
sidney2=Scrafty(maxiv="Yes")
sidney3=Zoroark(maxiv="Yes")
sidney4=Sharpedo(maxiv="Yes")
sidney5=Mandibuzz(maxiv="Yes")
sidney6=MAbsol(maxiv="Yes")
sidney=Trainer ("Elite Four Sidney",[sidney1,sidney2,sidney3,sidney4,sidney5,sidney6],"Hoenn")
#Glacia
glacia1=Abomasnow(maxiv="Yes")
glacia2=Beartic(maxiv="Yes")
glacia3=Froslass(maxiv="Yes")
glacia4=Vanilluxe(maxiv="Yes")
glacia5=Walrein(maxiv="Yes")
glacia6=MGlalie(maxiv="Yes")
glacia=Trainer ("Elite Four Glacia",[glacia1,glacia2,glacia3,glacia4,glacia5,glacia6],"Hoenn")
#Drake
drake1=Altaria(maxiv="Yes")
drake2=Dragalge(maxiv="Yes")
drake3=Kingdra(maxiv="Yes")
drake4=Flygon(maxiv="Yes")
drake5=Haxorus(maxiv="Yes")
drake6=MSalamence(maxiv="Yes")
drake=Trainer ("Elite Four Drake",[drake1,drake2,drake3,drake4,drake5,drake6],"Hoenn")
#Karen
karen1=Weavile(maxiv="Yes")
karen2=Absol(maxiv="Yes")
karen3=Spiritomb(maxiv="Yes")
karen4=Houndoom(maxiv="Yes")
karen5=Honchkrow(maxiv="Yes")
karen6=Umbreon(maxiv="Yes")
karen=Trainer ("Elite Four Karen",[karen1,karen2,karen3,karen4,karen5,karen6],"Johto")
#Marshal
marshal1=Breloom(maxiv="Yes")
marshal2=Mienshao(maxiv="Yes")
marshal3=Toxicroak(maxiv="Yes")
marshal4=Lucario(maxiv="Yes")
marshal5=Machamp(maxiv="Yes")
marshal6=Conkeldurr(maxiv="Yes")
marshal=Trainer ("Elite Four Marshal",[marshal1,marshal2,marshal3,marshal4,marshal5,marshal6],"Unova")
#shauntal
shauntal1=Cofagrigus(maxiv="Yes")
shauntal2=Jellicent(maxiv="Yes")
shauntal3=Drifblim(maxiv="Yes")
shauntal4=Golurk(maxiv="Yes")
shauntal5=Froslass(maxiv="Yes")
shauntal6=Chandelure(maxiv="Yes")
shauntal=Trainer ("Elite Four Shauntal",[shauntal1,shauntal2,shauntal3,shauntal4,shauntal5,shauntal6],"Unova")
#grimsley
grimsley1=Scrafty(maxiv="Yes")
grimsley2=Drapion(maxiv="Yes")
grimsley3=Krookodile (maxiv="Yes")
grimsley4=Houndoom(maxiv="Yes")
grimsley6=MTyranitar(maxiv="Yes")
grimsley5=Bisharp(maxiv="Yes")
grimsley=Trainer ("Elite Four Grimsley",[grimsley1,grimsley2,grimsley3,grimsley4,grimsley5,grimsley6],"Unova")
#caitlin
caitlin1=Alakazam(maxiv="Yes")
caitlin2=Gallade (maxiv="Yes")
caitlin3=Reuniclus (maxiv="Yes")
caitlin4=Metagross (maxiv="Yes")
caitlin5=Bronzong (maxiv="Yes")
caitlin6=Gothitelle (maxiv="Yes")
caitlin=Trainer ("Elite Four Caitlin",[caitlin1,caitlin2,caitlin3,caitlin4,caitlin5,caitlin6],"Unova")
#sawyer
sawyer1=Pangoro(maxiv="Yes")
sawyer2=Clawitzer (maxiv="Yes")
sawyer3=Aegislash (maxiv="Yes")
sawyer4=Slaking(maxiv="Yes")
sawyer5=Salamence(maxiv="Yes")
sawyer6=MSceptile (maxiv="Yes")
sawyer=Trainer ("Pokémon Trainer Sawyer",[sawyer1,sawyer2,sawyer3,sawyer4,sawyer5,sawyer6],"Kalos")
#alder
alder1=Escavalier(maxiv="Yes")
alder2=Conkeldurr(maxiv="Yes")
alder3=Krookodile (maxiv="Yes")
alder4=Bouffalant (maxiv="Yes")
alder5=Braviary (maxiv="Yes")
alder6=Volcarona (maxiv="Yes")
alder=Trainer ("Unova Champion Alder",[alder1,alder2,alder3,alder4,alder5,alder6],"Unova")
#paul
paul1=Honchkrow(maxiv="Yes")
paul2=Weavile(maxiv="Yes")
paul3=Gyarados (maxiv="Yes")
paul4=Garchomp (maxiv="Yes")
paul5=Metagross(maxiv="Yes")
paul6=Electivire(maxiv="Yes")
paul7=Torterra(maxiv="Yes")
paul8=Drapion(maxiv="Yes")
paul9=Aggron(maxiv="Yes")
paul10=Magmortar (maxiv="Yes")
paul11=Froslass(maxiv="Yes")
paul12=Gliscor(maxiv="Yes")
paul13=Hariyama(maxiv="Yes")
paul14=Nidoking(maxiv="Yes")
paul15=EGastrodon(maxiv="Yes")
paulteam=teamset([paul7,paul2,paul3,paul4,paul5,paul1,paul8,paul9,paul10,paul11,paul12,paul13,paul14,paul15],5)+[paul6]
paul=Trainer ("Pokémon Trainer Paul",paulteam,"Sinnoh")
#Trevor
trevor1=Florges(maxiv="Yes")
trevor2=Aerodactyl(maxiv="Yes")
trevor3=Crawdaunt(maxiv="Yes")
trevor4=Aurorus(maxiv="Yes")
trevor5=Tyrantrum(maxiv="Yes")
trevor6=MCharizardY(maxiv="Yes")
trevor=Trainer ("Pokémon Trainer Trevor",[trevor1,trevor2,trevor3,trevor4,trevor5,trevor6],"Kalos")
#hala
hala1=Kommo(maxiv="Yes")
hala2=Bewear(maxiv="Yes")
hala3=Primeape(maxiv="Yes")
hala4=Poliwrath(maxiv="Yes")
hala5=Machamp(maxiv="Yes")
hala6=Hariyama(maxiv="Yes")
hala=Trainer ("Elite Four Hala",[hala1,hala2,hala3,hala4,hala5,hala6],"Alola")
#molayne
molayne1=Skarmory(maxiv="Yes")
molayne2=Magnezone(maxiv="Yes")
molayne3=Metagross(maxiv="Yes")
molayne4=Klefki(maxiv="Yes")
molayne5=Bisharp(maxiv="Yes")
molayne6=Steelix(maxiv="Yes")
molayne=Trainer ("Elite Four Molayne",[molayne1,molayne2,molayne3,molayne4,molayne5,molayne6],"Alola")
#olivia
olivia1=Relicanth(maxiv="Yes")
olivia2=Gigalith(maxiv="Yes")
olivia3=AGolem(maxiv="Yes")
olivia4=Armaldo(maxiv="Yes")
olivia5=Cradily(maxiv="Yes")
olivia6=MNLycanroc(maxiv="Yes")
olivia=Trainer ("Elite Four Olivia",[olivia1,olivia2,olivia3,olivia4,olivia5,olivia6],"Alola")
#acerola
acerola1=Froslass(maxiv="Yes")
acerola2=Palossand(maxiv="Yes")
acerola3=Drifblim(maxiv="Yes")
acerola4=Dhelmise (maxiv="Yes")
acerola5=Banette (maxiv="Yes")
acerola6=Mimikyu(maxiv="Yes")
acerola=Trainer ("Elite Four Acerola",[acerola1,acerola2,acerola3,acerola4,acerola5,acerola6],"Alola")
#kahili
kahili1=Skarmory (maxiv="Yes")
kahili2=Crobat(maxiv="Yes")
kahili3=Mandibuzz(maxiv="Yes")
kahili4=Hawlucha (maxiv="Yes")
kahili5=Braviary (maxiv="Yes")
kahili6=Toucannon(maxiv="Yes")
kahili=Trainer ("Elite Four Kahili",[kahili1,kahili2,kahili3,kahili4,kahili5,kahili6],"Alola")
#Leon
leon1=MrRime(maxiv="Yes")
leon2=Aegislash(maxiv="Yes")
leon3=Dragapult (maxiv="Yes")
leon4=Inteleon(maxiv="Yes")
leon5=Rillaboom(maxiv="Yes",move=["Drum Beating","Acrobatics","High Horsepower","Knock Off"])
leon6=Cinderace(maxiv="Yes",ability="Libero",move=["Scorching Sands","Pyro Ball","Sucker Punch","Grass Knot"])
leon7=Charizard (maxiv="Yes")
leonteam=teamset([leon1,leon2,leon3,leon4,leon5,leon6],5)+[leon7]
leon=Trainer("Galar Champion Leon", leonteam,"Galar")
#TEST1
t1=Skarmory(maxiv="Yes",move=["Light Screen","Reflect","Soft-Boiled","Toxic"])
t2=Skarmory(maxiv="Yes",move=["Light Screen","Reflect","Soft-Boiled","Toxic"])
test1=Trainer("Test-01",[t1,t2])
#TEST2
t3=Alakazam()
t4=Charizard()
test2=Trainer("Test-02",[t3,t4])
#############
matchx=match()
elite4=random.choice([kahili,acerola,olivia,molayne,hala,caitlin,grimsley,shauntal,marshal,karen,drake,glacia,sidney,phoebe,siebold,lorelei,agatha,bruno,lance,aaron,bertha,lucian,flint,wikstrom,drasna,malva])
champ=random.choice([leon,alder,brendan,kukui,blue,red,wallace,steven,cynthia])
frontier=random.choice([lucy,tucker,greta,anabel,palmer,darach,dahlia,brandon,spenser])
evil=random.choice([tabitha,ariana,archer,ghetsis,cyrus,archie,maxie,saturn,giovanni])
talent=random.choice([trevor,paul,sawyer,ingo,ethan,gary,silver,buck,n,alain,tobias])
#PLAYER 01
p1=random.choices([matchx[0],elite4,champ,frontier,evil,talent],weights=[100,5,5,5,10,15],k=1)[0]

elite4=random.choice([kahili,acerola,olivia,molayne,hala,caitlin,grimsley,shauntal,marshal,karen,drake,glacia,sidney,phoebe,siebold,lorelei,agatha,bruno,lance,aaron,bertha,lucian,flint,wikstrom,drasna,malva])
champ=random.choice([alder,brendan,kukui,blue,red,wallace,steven,cynthia])
frontier=random.choice([lucy,tucker,greta,anabel,palmer,darach,dahlia,brandon,spenser])
evil=random.choice([tabitha,ariana,archer,ghetsis,cyrus,archie,maxie,saturn,giovanni])
talent=random.choice([trevor,paul,sawyer,ingo,ethan,gary,silver,buck,n,alain,tobias])
#PLAYER 02
p2=random.choices([matchx[1],elite4,champ,frontier,evil,talent],weights=[50,10,5,5,5,15],k=1)[0]

showparty(p1)
sm1=showsmogon(p1)
print("\n")
showparty (p2)
sm2=showsmogon (p2)
mon1=p1.pokemons[random.randint(1,len(p1.pokemons))-1]
mon2=p2.pokemons[random.randint(1,len(p2.pokemons)-1)]
