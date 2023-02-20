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
def teammaker(trclass=None,trname=None,pknum=6,field=field):
    "Creates Team"
    mons=[]
    team=[]
    if trclass=="Pokémon Trainer":
        mons=allmon
    ultrabeasts=[MDiancie,Blacephalon,Stakataka,Naganadel,UNecrozma,Necrozma,DMNecrozma,DWNecrozma,FMLunala,RSSolgaleo,Lunala,Solgaleo,Guzzlord,Kartana,Celesteela,Xurkitree,Buzzwole,Nihilego,Pheromosa]
    legendary=[Chiyu,Tinglu,Chienpao,Wochien,MMewtwoX,MMewtwoY,Enamorus,TEnamorus,Koraidon,Miraidon,ICalyrex,SCalyrex,Regieleki,Regidrago,Glastrier,Spectrier,Zarude,DUrshifu,WUrshifu,Eternatus,Zamazenta,Zacian,GArticuno,GZapdos,GMoltres,Melmetal,Zeraora,Silvally,Marshadow,Magearna,Tapufini,Tapubulu,Tapulele,Tapukoko,Diancie,MDiancie,UHoopa,Volcanion,CZygarde,Xerneas,Yveltal,Genesect,Keldeo,Meloetta,PMeloetta,BKyurem,WKyurem,Zekrom,Reshiram,Kyurem,TLandorus,TThundurus,TTornadus,Thundurus,Tornadus,Landorus,Victini,Cobalion,Terrakion,Virizion,Arceus,Shaymin,SShaymin,Darkrai,Cresselia,Manaphy,Uxie,Azelf,Mesprit,Registeel,Regirock,Regice,Articuno,Zapdos,Moltres,Raikou,Entei,Suicune,Lugia,Hooh,Celebi,Deoxys,ADeoxys,SDeoxys,DDeoxys,Jirachi,Mew,Rayquaza,Latias,Latios,MLatias,MLatios,Groudon,Kyogre,PGroudon,PKyogre,MRayquaza,Mewtwo,Dialga,ODialga,Palkia,OPalkia,Giratina,OGiratina,Heatran,Regigigas]
    if trclass in ["UB Expert"]:
        mons=ultrabeasts
    if trclass in ["Paldea Trainer"]:
        mons=[Charizard,Pikachu,Raichu, Wigglytuff,Dugtrio, Venomoth, Meowth,Persian,Golduck,Primeape, Arcanine,Slowbro,Muk, Cloyster, Gengar,Hypno,Chansey, Scyther,Tauros,PTauros,Gyarados,Ditto, Jolteon, Vaporeon,Flareon,Articuno, Zapdos, Moltres, Dragonite, Typhlosion, Ampharos, Azumarill,Sudowoodo,Jumpluff,Sunflora,Quagsire,Espeon,Umbreon, Slowking,Forretress,Scizor, Heracross,Ursaring,Delibird,Houndoom,Donphan, Blissey, Tyranitar]
    if trclass in ["Galar Trainer"]:
        mons=[Venusaur, Charizard,Blastoise,Butterfree,Pikachu,Meowth,HArcanine, Machamp,HElectrode,GArticuno,GZapdos,GMoltres,GRapidash,GSlowbro,GSlowking,Sirfetchd,Gengar,Kingler,GWeezing,MrRime, Lapras,Snorlax,HTyphlosion,GCorsola,HSamurott,HLilligant,Obstagoon,GDarmanitan,HZoroark,HBraviary,HGoodra,HAvalugg,HDecidueye,Melmetal,Runerigus,Garbodor,Rillaboom,Cinderace,Inteleon,Corviknight,Greedent,Orbeetle,Thievul,Dubwool,Eldegoss,Drednaw,Coalossal,Flapple,Appletun,Boltund,Sandaconda,Barraskewda,Toxtricity,Grapplot,Centiskorch,Polteageist,Hatterene,Grimmsnarl,Perrserker,Alcremie,Frosmoth,Stonjourner,Cursola,MrRime,Falinks,Pincurchin,Eiscue,Indeedee,Copperajah,Dracovish,Dracozolt,Arctovish,Arctozolt,Duraludon,Dragapult,DUrshifu,WUrshifu,Sandslash, Nidoqueen,Nidoking,Clefable, Ninetales, Wigglytuff,Vileplume,Dugtrio,Golduck,Arcanine,Poliwrath, Alakazam,Tentacruel,Rapidash,Slowbro, Cloyster, Exeggutor,Marowak, Hitmonlee, Hitmonchan,Weezing,Rhydon,Chansey, Kangaskhan, Seaking,Starmie,MrMime,Jynx,Pinsir,Tauros, Gyarados,Ditto, Vaporeon, Jolteon,Flareon,Omastar, Kabutops, Aerodactyl, Articuno, Zapdos,Moltres, Dragonite,Noctowl,Lanturn,Xatu, Bellossom, Sudowoodo,Politoed, Quagsire, Espeon,Umbreon, Slowking,Wobbuffet, Steelix,Scizor,Shuckle,Heracross, Octillery,Delibird,Mantine,Skarmory,Kingdra, Porygon2,Hitmontop,Miltank, Blissey, Raikou,Suicune,Entei, Tyranitar,Celebi,Hooh,Lugia,Mew,Mewtwo,Sceptile,Blaziken,Swampert,Linoone,Ludicolo,Shiftry, Pelipper, Gardevoir,Ninjask,Shedinja,Exploud, Sableye,Mawile,Aggron,Manectric,Sharpedo,Wailord, Torkoal, Flygon,Altaria,Whiscash,Solrock,Lunatone,Crawdaunt,Claydol,Cradily,Armaldo,Milotic,Dusclops,Absol,Glalie,Walrein,Relicanth,Salamence, Metagross,Regirock,Regice,Registeel,Latias,Latios,Kyogre,Groudon, Rayquaza,Jirachi,Luxray,Roserade,Vespiquen,Cherrim, WGastrodon, EGastrodon,Drifblim, Lopunny,Skuntank,Bronzong,Spiritomb, Garchomp,Lucario, Hippowdon,Drapion,Toxicroak, Abomasnow,Weavile, Magnezone, Lickilicky,Rhyperior, Tangrowth,Electivire,Magmortar,Togekiss,Leafeon,Glaceon,Mamoswine, PorygonZ,Dusknoir,Gallade,Froslass,HRotom,FrRotom,FRotom,WRotom,MRotom,Uxie,Mesprit,Azelf,Dialga,Palkia,ODialga,OPalkia,Heatran,Regigigas,Giratina,OGiratina, Cresselia]
    if trclass in ["Alola Trainer"]:
        mons=[MVenusaur,MCharizardX,MCharizardY,MBlastoise,MBeedrill,MAlakazam,MGengar,MScizor, MSteelix,MHeracross,MAerodactyl,MHoundoom,MSceptile,MSwampert,MBlaziken,MKangaskhan,MPinsir, MGyarados,MAmpharos,MTyranitar,MGardevoir, MSableye,MMawile,MAggron, MMedicham,MManectric,MSharpedo,MCamerupt,MAltaria,MBanette,MAbsol,MGlalie,MSalamence,MMetagross, MLopunny,MGarchomp,MGallade,MLucario,MAbomasnow,MAudino,ARaticate,ARaichu,ASandslash,ANinetales,ADugtrio,APersian,AGolem,AMuk, AExeggutor,AMarowak,Decidueye,Incineroar,Primarina,Toucannon, Vikavolt,DLycanroc,MDLycanroc,MNLycanroc,SWishiwashi, Toxapex,Mudsdale,Araquanid,Salazzle,Bewear,Tsareena,Golisopod,Palossand, Silvally,Turtonator,Mimikyu,Drampa, Dhelmise,Kommo]
    if trclass in ["Kalos Trainer"]:
        mons=[Chesnaught, Delphox, Greninja, Talonflame, Vivillon,Pyroar,Florges,Gogoat,Pangoro,Meowstic, Aegislash,Malamar, Barbaracle,Dragalge, Clawitzer,Heliolisk,Tyrantrum,Aurorus, Sylveon,Hawlucha,Goodra,Klefki,Trevenant,Gourgeist,Avalugg,Noivern,MVenusaur,MCharizardX,MCharizardY,MBlastoise,MBeedrill,MAlakazam,MGengar,MScizor, MSteelix,MHeracross,MAerodactyl,MHoundoom,MSceptile,MSwampert,MBlaziken,MKangaskhan,MPinsir, MGyarados,MAmpharos,MTyranitar,MGardevoir, MSableye,MMawile,MAggron, MMedicham,MManectric,MSharpedo,MCamerupt,MAltaria,MBanette,MAbsol,MGlalie,MSalamence,MMetagross, MLopunny,MGarchomp,MGallade,MLucario,MAbomasnow,MAudino]
    if trclass in ["Johto Trainer"]:
        mons=[Donphan,Porygon2,Miltank,Magcargo,Corsola,Delibird,Mantine,Granbull,Shuckle,Ursaring,Slowking,Wobbuffet,Forretress,Quagsire,Sunflora,Jumpluff,Sudowoodo,Bellossom,Xatu,Hitmontop,Ariados,Noctowl,Ledian,Furret,Meganium,Typhlosion,Feraligatr, Crobat,Lanturn,Ampharos,MAmpharos,Azumarill,Politoed,Espeon,Umbreon,Steelix,MSteelix, Scizor,MScizor,Heracross,MHeracross,Skarmory,Houndoom,MHoundoom,Kingdra,Blissey,Tyranitar,MTyranitar]
    if trclass in ["Kanto Trainer"]:
        mons=[Ditto,Scyther,Seaking,Rhydon,Chansey,Marowak,Electrode,Hypno,Persian,Dugtrio,Kingler,Wigglytuff,Sandslash,Clefable,Butterfree,Beedrill,Fearow,Pikachu,Venusaur,MVenusaur,Charizard,MCharizardX,MCharizardY,Blastoise,MBlastoise,MBeedrill,Pidgeot,MPidgeot,Arbok, Nidoking,Nidoqueen,Ninetales,Golduck,Primeape,Arcanine,Poliwrath, Alakazam,MAlakazam,Machamp,Victreebel,Tentacruel,Golem,Rapidash,Slowbro,MSlowbro,Dodrio,Dewgong,Muk,Cloyster,Gengar,MGengar,Exeggutor,Hitmonchan,Hitmonlee,Weezing,Kangaskhan,MKangaskhan,Starmie,Tauros,Jynx,Pinsir,MPinsir,Gyarados,MGyarados,Lapras,Jolteon,Vaporeon,Flareon,Omastar,Kabutops,Aerodactyl,MAerodactyl,Snorlax,Dragonite]
    if trclass in ["Hoenn Trainer"]:
        mons=[ Sceptile,MSceptile,Blaziken,MBlaziken,Swampert,MSwampert,Mightyena,Ludicolo,Shiftry,Swellow,Pelipper,Gardevoir,MGardevoir,Breloom, Slaking,Exploud,Hariyama,MSableye,MMawile,Aggron,MAggron,Medicham,MMedicham,MManectric,Sharpedo,MSharpedo,Wailord,Camerupt,MCamerupt,Torkoal,Flygon,Altaria,MAltaria,Zangoose,Seviper,Solrock,Lunatone,Whiscash,Crawdaunt,Claydol,Cradily,Armaldo,Milotic,Banette,MBanette,Absol,MAbsol,Glalie,MGlalie,Walrein,Huntail,Gorebyss,Relicanth,Salamence,MSalamence,Metagross,MMetagross]
    if trclass in ["Sinnoh Trainer"]:
        mons=[Lickilicky,Torterra,Infernape,Empoleon,Staraptor,Luxray,Roserade,Rampardos,Bastiodon,Vespiquen,EGastrodon,WGastrodon,Ambipom,Drifblim,MLopunny,Mismagius,Honchkrow,Purugly,Skuntank,Bronzong,Spiritomb,Garchomp,Lucario,MLucario,Hippowdon,MGarchomp,Drapion,Toxicroak,Abomasnow,MAbomasnow,Weavile,Magnezone,Rhyperior,Tangrowth,Electivire,Magmortar,Togekiss,Yanmega,Gliscor,Gallade,MGallade,Probopass,Dusknoir,Froslass,WRotom]
    if trclass in ["Unova Trainer"]:
        mons=[Musharna,Sawk,Throh,Simipour,Simisage,Simisear,Garbodor,Serperior,Emboar,Samurott,Stoutland,Unfezant,Zebstrika,Gigalith,Excadrill,Conkeldurr,Seismitoad,Leavanny,Scolipede,Krookodile,Darmanitan,Scrafty,Cofagrigus,Carracosta,Archeops,Zoroark,Gothitelle, Reuniclus, Swanna,Vanilluxe,Escavalier,Jellicent,Galvantula,Ferrothorn,Eelektross,Chandelure,Haxorus,Beartic,Accelgor,Mienshao,Druddigon,Golurk,Bisharp,Bouffalant,Braviary,Mandibuzz,Heatmor,Durant,Hydreigon,Volcarona,MCharizardX, MCharizardY,MBlastoise, MVenusaur]
#FIGHTING SPECIALIST 
    if trclass in ["Dojo Master","Blackbelt"]:
        namelist=["Taishi","Damme","Wesley","Joe","Dolph","Kenji","Kiyo","Lao","Lung","Nob","Wai","Yoshi","Atsushi","Daisuke","Hideki","Hitoshi","Koichi","Koji","Yuji","Rhett","Takao","Theodore","Zander","Aaron","Hugh","Mike","Nicolas","Shea","Takashi","Adam","Carl","Colby","Darren","David","Derek","Gregory","Griffin","Jarrett","Kendal","Luke","Nathaniel","Philip","Rafael","Ray","Ricky","Sean","Willie","Davon","Ander","Kenji","Manford","Benjamin","Edward","Grant","Jay","Kendrew","Kentaro","Ryder","Teppei","Tyrone","Corey","Donny","Drago","Gordon","Grigor","Jeriel","Kenneth","Mathis","Martell","Rodrigo","Rich","Rocky","Wesley","Zachery","Alonzo","Gunnar","Killan","Markus","Yanis","Ricardo","Igor","Cadox","Banting","Clayton","Earl","Greg","Roy","Terry","Walter","Tracy","Alvaro","Curtis"]
        nn=random.choice(namelist)
        new_name=trclass+" "+nn
        mons=[Sawk,Throh,PTauros,Flamigo,Slitherwing,Anihilape,Quaquaval,Ironvaliant,Ironhands,Greattusk,Hitmontop,DUrshifu,WUrshifu,Sirfetchd,Grapplot,Sneasler,HDecidueye,Hawlucha,Pangoro,Chesnaught,Mienshao,Scrafty,HLilligant,Conkeldurr,Emboar,MBlaziken,MGallade,Gallade,Machamp,Poliwrath,Hitmonchan,Hitmonlee,Infernape,Blaziken,Breloom,Primeape,Heracross,MHeracross,Hariyama,MMedicham]
   #ELDER TRAINERS     
    if trclass =="Elder Trainer":
        namelist=["Jules","Shriner","Jason","Apollo","Damon","Castor","Marcus","Henry","Orion","Arthur","Julius","Zephyr","Helios","Liam","Odysseus","Albert","Helios"]
        nn=random.choice(namelist)
        new_name=trclass+" "+nn
        mons=[Tyrantrum,Aurorus,Carracosta,MAerodactyl,Aerodactyl,Kabutops,Omastar,Armaldo,Cradily,Rampardos,Bastiodon,Cloyster,Relicanth,Claydol,Arcanine,Mamoswine,Spiritomb,Lunatone,Solrock,Yanmega]+legendary
        mons+=random.choices([Rayquaza,Latias,Latios,Regice,Regirock,Registeel,Kyogre,Groudon,Entei,Suicune,Raikou],k=1)
    if trname is None and trclass not in ["Elder Trainer","Dojo Master",",Blackbelt", "Egyptian","Exorcist"]:
        namelist=["Josh","Kyler","Jade","John","Joey","Jan","Gabriel","Jamie","Kylie","Andrea","Evy","Ebba","Titus","Emiliano","Emilia","Natalie","Justin","Anastasia","Frannie","Danielle","Daniel","Hugo","Robert","Carlos","Alex","Alexander","Alexandra","Arslan","Johan","Mike","Julian","Selena","Emmanuel","Kristin","Lawrence","Frank","Pamela","Nicole","Emma","Matthew","Catherine","Jackson","Jenna","Sebastian","Sophia","Gav","Lorenzo","Merdith","Nora","Beth","Chelsea","Katelyn","Logan","Madelin","Nicolas","Trenton","Allison","Ashlee","Deshawn","Dwayne","Felicia","Jeffery","Krista","Taylor","Annie","Audra","Brenda","Claude","Chloris","Crofton","Eliza","Harry","Irene","Jaden","Keith","Lewis","Mary","Miguel","Mylene","Pedro","Ralph","Richard","Shanti","Thalia","Anja","Bret","Briana","Daryl","Dianna","Eddie","Elie","Elaine","Forrest","Heidl","Hillary","Johan","Leaf","Lena","Lois","Malory","Maxwell","Melita","Mikiko","Naoko","Parker","Rick","Serenity","Steve","Ambre","Bjorn","Brooke","Chaise","Lee","Dean","Clementine","Maurice","Melina","Nash","Petra","Reed","Ralf","Shinobu","Silas","Twiggy","Kira","Dirk","Bobby","Danny","Caleb","Dylan","Thomas","Daniel","Jeff","Braven","Dell","Neagle","Haruki","Mitchell","Sheriff","Raymond","Cole","Edgar","Evan","Jason","Phil","Vincent","Yoshinari"]
        nn=random.choice(namelist)
        new_name=trclass+" "+nn
        #STEEL
    if trclass in ["Factory Boss","Industry Worker"]:
        mons=[Revavroom,Gholdengo,Tinkaton,Orthworm,Kingambit,Irontreads,Mawile,ADugtrio,ASandslash,Duraludon,Copperajah,Perrserker,Corviknight,Dhelmise,HGoodra,Aegislash,Bisharp,Magnezone,Steelix,MSteelix,Scizor,MScizor,Skarmory,MMawile,Aggron,MAggron,Metagross,MMetagross,Empoleon,Bastiodon,Bronzong,Lucario,MLucario,Probopass,Heatran,Excadrill,Ferrothorn,Escavalier]
        #Ghost
    if trclass == "Exorcist":
        namelist=["Gabrielle","Candido","Bishop","William","Bowden","Joseph","Thomas","Fantino","Angelo"]
        nn=random.choice(namelist)
        new_name=trclass+" "+nn
        mons=[Ceruledge,Houndstone,Anihilape,Skeledirge,Fluttermane,GCorsola,AMarowak,Dragapult,Polteageist,Mimikyu,Decidueye,Gourgeist,Aegislash,Trevenant,Golurk,Gengar,MGengar,HTyphlosion,MSableye,Banette,MBanette,Dusknoir,Drifblim,Mismagius,Spiritomb,Froslass,Cofagrigus,Runerigus,HZoroark,Jellicent,Chandelure]
        #Psychic
    if trclass == "Psychic":
        mons=[Musharna,Armarouge,Espathra,Veluza,Screamtail,Grumpig,Wobbuffet,Slowking,Xatu,MrMime,Hypno,Indeedee,GSlowking,GSlowbro,GRapidash,Wyrdeer,Malamar,Delphox,HBraviary,Alakazam,MAlakazam,Slowbro,MSlowbro,Exeggutor,Starmie,Jynx,Espeon,Farigiraf,Gardevoir,MGardevoir,Medicham,MMedicham,Lunatone,Solrock,Claydol,Metagross,MMetagross, Bronzong,Gallade,MGallade,Gothitelle,Reuniclus]
        #Grass
    if trclass == "Gardener":
        mons=[Simisage,Scovillain,Brutebonnet,Arboliva,Whimsicott,Toedscruel,Meowscarada,Leafeon,Cherrim,Tropius,Cacturne,Sunflora,Jumpluff, Bellossom,Parasect,Vileplume,Flapple,Appletun,Rillaboom,Dhelmise,Tsareena,HElectrode,HDecidueye,Gourgeist,Decidueye,Trevenant,Gogoat,Florges,Venusaur,MVenusaur,Victreebel,Exeggutor,AExeggutor,Tangrowth,Meganium,Sceptile,MSceptile,Ludicolo,Shiftry,Breloom,Roserade,Cradily,Torterra,Abomasnow,MAbomasnow,Serperior,Leavanny,HLilligant,Ferrothorn]+random.choices([Shaymin,SShaymin],k=1)
    if trclass in ["Chef","MasterChef","Cook","Foodie"]:
        mons=[Dachsbun,Slurpuff, Vanilluxe,Tropius,Polteageist, Alcremie,Miltank,Shuckle,Coalossal,Tsareena,Appletun,MAbomasnow,MAudino,MBlaziken]
    if trclass in ["Pokémon Ranger","Camper"]:
        mons=[Shiftry,Ludicolo, Bellossom,Roserade,Breloom,Cacturne,Altaria,MAltaria,Dusclops, Mismagius,Gengar,MGengar,Sunflora, Tangrowth, Venusaur,MVenusaur,Forretress,Electrode, Exeggutor, Victreebel,Starmie,Ledian,Blissey, Vileplume, Arcanine,Gyarados,Ambipom, Azumarill,Linoone, Skarmory, Lickilicky,Donphan,Empoleon,Flygon,Ursaring,Luxray,Floatzel,Leafeon,Arbok, Butterfree, Granbull,Jumpluff, MLopunny ,Infernape,Aggron,Marowak, Zangoose, Poliwrath, Dewgong, Steelix,MSteelix,Simisage,Simisear,Simipour,Swoobat, Zebstrika, Pinsir,MPinsir,Emolga, Pelipper, Vanilluxe, Musharna,Stoutland,Haxorus, Drifblim,Umbreon,Beartic, Leavanny, Unfezant,Seismitoad, Swanna,Mantine,Rapidash, MAbomasnow,Abomasnow, Magmortar, Wigglytuff,Farigiraf,Excadrill,Jolteon,Probopass,Galvantula,Volcarona,Flareon, Electivire,Accelgor,Swalot, Camerupt,MCamerupt,Banette,MBanette,Golduck,Krookodile, Sudowoodo, Cradily, Scolipede, Lucario,MLucario, Watchog,Grumpig,Ampharos,MAmpharos, Kricketune,Snorlax, Armaldo, Gliscor, Skuntank,Escavalier,Slaking,Wyrdeer, Sirfetchd,Garbodor, Amoongus,Goodra,Kingdra,Crawdaunt,Sandslash,Garchomp,MGarchomp, Ferrothorn,Pyroar,Crobat,Slowbro,Exploud,Quagsire,Manectric, MManectric ,Pikachu,Raichu, Seviper]
        #BUG
    if trclass in ["Bug Catcher","Bug Researcher"]:
        if "Hoenn" in field.location:
            mons=[Ribombee,Shuckle,Forretress,Ariados,Ledian,Scyther,Venomoth,Parasect,Butterfree,Beedrill,Scizor,Heracross,Pinsir,Shedinja,Ninjask,Masquerain,Beautifly,Dustox,MScizor,MHeracross,MPinsir,MBeedrill]
        if "Johto" in field.location:
            mons=[Shuckle,Forretress,Ariados,Ledian,Scyther,Venomoth,Parasect,Butterfree,Beedrill,Scizor,Heracross,Pinsir,MScizor,MHeracross,MPinsir,MBeedrill]
        else:
            mons=[Rabsca,Ironmoth,Spidops,Lokix,Slitherwing,Wormadam,Mothim,TWormadam,SWormadam,Kricketune,Shuckle,Forretress,Ariados,Ledian,Scyther,Venomoth,Parasect,Butterfree,Beedrill,Frosmoth,Kleavor,Centiskorch,Orbeetle,Golisopod,Araquanid,Vikavolt,Volcarona,Durant,Accelgor,Galvantula,Escavalier,Scolipede,Leavanny,Scizor,Heracross,Pinsir,Drapion,Vespiquen,Yanmega,MScizor,MHeracross,MPinsir,MBeedrill]        
        #ICE SPECIALISTS
    if trclass in ["Skier","Boarder"]:
        mons=[FrRotom,Arctovish, Arctozolt,Ironbundle,Cryogonal,Baxcalibur,Ironbundle,Glaceon,Delibird,ASandslash,Cetitan,Frosmoth,MrRime,Avalugg,HAvalugg,Aurorus,Beartic,Vanilluxe,GDarmanitan,Weavile,Abomasnow,Walrein,Lapras,Mamoswine,Glalie,MGlalie,Jynx,Cloyster,ANinetales,MAbomasnow]
        ch=random.randint(1,10)
        if ch==7:
            mons+=[Articuno]
    if trclass in ["Breeder"]:
     mons=[Pikachu,Raichu, Wigglytuff, Clefable,Blissey,Sudowoodo,Electivire, Magmortar,Jynx, MCharizardY, MBlastoise, MVenusaur]
#ROCK SPECIALISTS
    if trclass in ["Ruin Explorer","Hiker","Backpacker"]:
     mons=[Glimmora,Garganacl,Ironthorns,Klawf,Sudowoodo,Rhydon,Coalossal,Gigalith,Lunatone,Solrock,Probopass,HArcanine,Runerigus,Cofagrigus,MTyranitar,MAggron,Rhyperior,Aggron,Steelix,Machamp,Tyranitar,Golem]
#fossil
    if trclass in ["Fossil Maniac","Paleontologist"]:
        mons=[Dracovish,Dracozolt,Tyrantrum,Aurorus,Archeops,Carracosta,Omastar,Kabutops,MAerodactyl,Armaldo,Cradily,Aerodactyl,Mamoswine,Bastiodon,Rampardos,Relicanth]
#Ground
    if trclass in ["Desert Explorer","Egyptian"]:
        if trclass=="Egyptian":
            namelist=["Wongani","Abdelhamid","Ali","Zafar","Saif","Hakeem","Ziyad","Hamed","Daud","Apis","Amon","Aton"]
            nn=random.choice(namelist)
            new_name=trclass+" "+nn
        mons=[Clodsire,Toedscruel,Sandyshocks,Greattusk,Cacturne,Donphan,Quagsire,Rhydon,Marowak,Dugtrio,ADugtrio,Sandslash,Sandaconda,Palossand,Mudsdale,Mandibuzz,Golurk,Drapion,Camerupt,MCamerupt,Hippowdon,Nidoking,Nidoqueen,Golem,Gliscor,Steelix,MSteelix,Rhyperior,Mamoswine,Swampert,MSwampert,Flygon,Whiscash,Claydol,Torkoal,Torterra,EGastrodon,WGastrodon,Garchomp,MGarchomp,Seismitoad,Krookodile,Excadrill,Arbok]
#WATER SPECIALISTS
    if trclass in ["Marine Biologist","Surfer","Scuba Diver","Swimmer","Sailor","Captain","Pirate","Fisherman"]:
        mons=[Tatsugiri,Simisage,Dondozo,Palafin,Wugtrio,Quaquaval,Ironbundle,Lumineon,Floatzel,Bibarel,Mantine,Corsola,Slowking,Quagsire,Seaking,Kingler,Dracovish,Barraskewda,Inteleon,Araquanid,Toxapex,SWishiwashi,Primarina,Clawitzer,Barbaracle,Greninja,Jellicent,Swanna,Carracosta,Basculegion,Seismitoad,HSamurott,Samurott,MSharpedo,MSwampert,MBlastoise,Phione,EGastrodon,WGastrodon,Empoleon,Walrein,Huntail,Gorebyss,Relicanth,Milotic,Crawdaunt,Whiscash,Dewgong,Sharpedo,Pelipper,Kingdra,Politoed,Azumarill,Feraligatr,Lanturn,Lapras,Gyarados,Slowbro,Cloyster,Starmie, Blastoise,Poliwrath,Swampert,Ludicolo]+random.choices([Manaphy, Wailord],k=1)
#GRUNTS
    if trclass in ["Flare Grunt"]:
        mons=[]
    if trclass in ["Shadow Triads"]:
        mons=[Absol, Kingambit, Bisharp,MBanette,Accelgor,HLilligant,Volcarona, Basculegion]
    if trclass in ["Plasma Grunt"]:
        mons=[Watchog,Liepard,Krookodile, Scrafty, Garbodor,Crobat,Seviper,Weezing,Raticate,Drapion, Kingambit, Hydreigon,Weavile,Bisharp, Scolipede, Amoongus,Magnezone,Muk,Zangoose, Genesect,Metagross, Gigalith,Mandibuzz,Seismitoad,MHoundoom,MMedicham,MHeracross,MGallade]
    if trclass in ["Aqua Grunt"]:
        mons=[Crawdaunt,Sharpedo,Crobat,Mightyena,Muk,Weezing,Tentacruel,Wailord,MSharpedo,Walrein,Dusclops, Ludicolo,Seviper]
    if trclass in ["Magma Grunt"]:
        mons=[Camerupt,Torkoal,Crobat,Mightyena,Muk,Weezing,Magmortar,MCamerupt,Claydol,Houndoom,Magcargo,Sandslash, Salamence,Banette,Aggron, Zangoose]
    if trclass in ["Rocket Grunt"]:
        mons=[Arbok,Weezing,Victreebel,Muk,Crobat,Seviper,Houndoom,Yanmega, Machamp,MHoundoom,Raticate,Sandslash,Persian,Hypno,Marowak, Vileplume,Electrode,Gengar,Magnezone, Rhyperior, Skarmory,Tauros,Golem,Rhydon,Dodrio,Purugly,Toxicroak,Skuntank]
    if trclass in ["Galactic Grunt"]:
        mons=[Purugly,Skuntank,Weavile,Bronzong,Crobat,Toxicroak,Muk,Weezing,Magnezone,Electivire,Magmortar,Rhyperior,Probopass,Gyarados,MSableye]
#DRAGON SPECIALISTS
    if trclass in ["Dragon Tamer"]:
        mons=[Cyclizar,Baxcalibur,Roaringmoon,Dragapult,Duraludon,Dracovish,Dracozolt,Flapple,Appletun,MSceptile,Kommo,Drampa,Turtonator,Noivern,HGoodra,Goodra,Hydreigon,Druddigon,Haxorus,Krookodile,Serperior,Yanmega,Garchomp,MGarchomp,Gyarados,MGyarados,Dragonite,Kingdra,Charizard,Aerodactyl,Tyranitar, Salamence,MSalamence,MAerodactyl,MCharizardX,MTyranitar,Feraligatr]+random.choices([Latias,Latios,MLatias,MLatios],k=1)
    if trclass in ["Police Officer","Investigator","Policeman"]:
        mons=[Noctowl,Machamp,Medicham, MMedicham, Arcanine, HArcanine, Stoutland, Mienshao, Lucario, MLucario, Boltund,Ariados, Bastiodon]
#POISON SPECIALISTS
    if trclass in ["Venom Expert"]:
        mons=[Revavroom,Clodsire,Ironmoth,Grafaiai,Garbodor,Dustox,Swalot,Venomoth,Vileplume,Toxtricity,GSlowking,GWeezing,GSlowbro,Salazzle,Sneasler,Dragalge,Toxicroak,Drapion,Roserade,Seviper,Arbok,Weezing,Crobat,MBeedrill,Venusaur,Nidoking,Nidoqueen,Victreebel,Tentacruel,Muk,Gengar,Overqwil,MVenusaur]
#ELECTRIC
    if trclass in ["Rocker","Guitarist","Electrician"]:
        mons=[Pincurchin,Boltund,Pawmot,Kilowattrel,Ironthorns,Ironhands,Sandyshocks,Bellibolt,Pachirisu,Manectric,Electrode,Raichu,ARaichu,Pikachu,Dracozolt,Toxtricity,Vikavolt,HElectrode,Eelektross,Galvantula,MManectric,AGolem,Magnezone,Jolteon,Electivire,Lanturn,Ampharos,MAmpharos,Luxray,WRotom,Zebstrika]        
#FIRE SPECIALISTS
    if trclass in ["Kindler","Fiery Breathe","Volcano Explorer"]:
        mons=[Simisear,Scovillain,Skeledirge,Ironmoth,Ceruledge,Armarouge,Magcargo,AMarowak,Centiskorch,Coalossal,Cinderace,Turtonator,Salazzle,Incineroar,Pyroar,Talonflame,Delphox,Volcarona,Heatmor,Chandelure,Darmanitan,HTyphlosion,Emboar,HArcanine,Magmortar,Infernape,Arcanine,Rapidash,Houndoom,Flareon,Typhlosion,Blaziken,Camerupt,Charizard,MCharizardY,MHoundoom,MCamerupt]
#FLYING SPECIALISTS
    if trclass in ["Bird Keeper","Pilot","Sky Diver"]:
        mons=[Flamigo,Kilowattrel,Bombirdier,Ironjugulis,Xatu,Noctowl,Corviknight,Toucannon,Hawlucha,Talonflame,Mandibuzz,HBraviary,Braviary,Swanna,Archeops,Unfezant,Gliscor,Togekiss,Honchkrow,Staraptor,Pelipper,Swellow,MPidgeot,Charizard,Skarmory,Altaria,Crobat,Dodrio,MSalamence]
        mons+=random.choices([Articuno,Zapdos,Moltres,Thundurus,Landorus,Tornadus,Enamorus],k=1)      
    if trclass in ["Scientist","Super Nerd"]:
        mons=[Electrode,Magnezone,Metagross,Klinklang, Alakazam,MAlakazam,MMetagross, Revavroom,Irontreads,Electivire,WRotom,Ironhands, Ironthorns,Ironvaliant,Ironbundle, Ironjugulis,Ironmoth,FRotom,HRotom,FrRotom,MRotom,PorygonZ,Porygon2]
        #DECENT TRAINERS
    if trclass in ["Expert","Veteran","Businessman","Gentleman"]:
        mons=[Audino,Dudunsparce,Noctowl,Furret,Ditto,Chansey,Persian,Vileplume,Wigglytuff,Clefable,Pikachu,Raticate,ARaticate,Butterfree,Beedrill,MDLycanroc,MNLycanroc,DLycanroc,Aegislash,Delphox,Greninja,Chesnaught,Basculegion,Stoutland,Probopass,Ursaluna,Yanmega,Magnezone,Tangrowth,Hippowdon,Lucario,Mismagius,Luxray,Roserade,Torterra,Glalie,Absol,Banette,Milotic,Armaldo,Cradily,Aggron,Hariyama,Breloom,Gardevoir,Swellow,Ludicolo,Swampert,Houndoom,Heracross,Steelix,Espeon,Ampharos,Flareon,Jolteon,Vaporeon,Snorlax,Lapras,Gyarados,Tauros,Kangaskhan,Hitmonchan,Hitmonlee,Exeggutor,Gengar,Dodrio,Slowbro,Rapidash,AGolem,Victreebel,Machamp,Golduck,Alakazam,Pidgeot,Blastoise,Ninetales,Primeape,MBeedrill, Venusaur, Charizard,Cloyster,MBanette,MGlalie]
        ch=random.randint(1,15)
        if ch==7:
            mons+=random.choices(legendary,k=1)
        pass
    if trclass in[ "Chaos Trainer"]:
        mons=[Gremlid,Deigon,MFlygon,Gorochu,Salobber,Terryena,Malevorus, TMalevorus, UTyranitar,Medicrow,Cochungus,Bustoliv,Bombeedel, Mollonce, Machug, Doncrete,Dangal, Ajjimajji, Spinestial]
        
    if trclass in[ "Beauty","Lass"]:
        namelist=["Alexa","Andrea","Georgia","Emma","Rose","Kimmy","Layla","Stephanie","Alexandra","Kylie"]
        mons=[Wigglytuff,Blissey,MAudino,Swanna,Sylveon,Whimsicott, Alcremie,Slurpuff,Tsareena,Azumarill,GRapidash, Vileplume,Vaporeon,Cloyster, Bellossom, Seaking,Starmie,Clefable,Togekiss, Gardevoir,MGardevoir,Mawile,MMawile,Altaria,MAltaria,Florges,Klefki,Primarina, Hatterene,Dachsbun,Screamtail,Fluttermane,Tinkaton]
#THUGS
    if trclass in[ "Street Punk","Biker","Cueball","Smuggler","Thief","Goon","Driver"]:
        namelist=["Charles","Dwayne","Glenn","Harris","Joel","Riley","Zeke","Alex","Billy","Ernest","Gerald","Hideo","Isaac","Jared","Jaren","Jaxon","Jordy","Lao","Lucas","Nikolas","Ricardo","Ruben","Virgil","William","Aiden","Charles","Dale","Dan","Markey","Reese","Teddy","Theron","Jeremy","Morgann","Philip","Stanley","Dillon"]
        nn=random.choice(namelist)
        new_name=trclass+" "+nn
        mons=[Weezing,Muk, Electrode,Charizard, Flareon, Magmortar,Togekiss, MCharizardY, Forretress, Hypno, Tentacruel,Swalot, Ursaring, Drapion,Arbok,Seviper, Toxicroak, Galvantula, Scrafty, Krookodile, Bouffalant, Bisharp, Kingambit, Crobat,Conkeldurr, Nidoking, Nidoqueen, Hitmonlee, Machamp, Primeape, Hitmonchan, Venomoth, Poliwrath, Anihilape, Beedrill,MBeedrill, Kingdra, Kangaskhan, MKangaskhan, Kabutops,Jynx,Ariados, Dudunsparce, Ampharos, Skarmory, Cloyster, Venusaur, Rhydon, Victreebel, Skarmory, Miltank, Vaporeon, Parasect,Steelix, MSteelix]
        ch=random.randint(1,10)
        if ch==7:
            mons+=random.choices(legendary,k=1)

    if trclass == "Air Force Officer":
        mons=[Skarmory,Corviknight,Magnezone,Latios,Latias,Pidgeot,Staraptor,Braviary,Altaria,MAltaria,Dragonite,Salamence,Metagross,MSalamence]
    if trclass == "Navy Officer":
        mons=[Gyarados,Blastoise,Swampert,Feraligatr,Inteleon,Wailord,Starmie,MBlastoise,MSwampert]
    if trclass == "Military Officer":
        mons=[Aggron,Salamence,Tyranitar,Steelix,Rhyperior,Magnezone,Metagross,Dragonite,Magmortar,Electivire,Charizard, Blastoise,MAggron,MCharizardY, MBlastoise,MMetagross]
    if trclass == "Tamer":
        mons=[Anihilape,Ursaring,Granbull,GRapidash,Bewear,MDLycanroc,MNLycanroc,DLycanroc,Wyrdeer,Pangoro,Braviary,Tauros,Arbok,Arcanine,HArcanine,Rapidash,Ambipom,Ursaluna,Mamoswine,Houndoom,MHoundoom,Mightyena,Slaking,MManectric,Sharpedo,MSharpedo,Wailord,Zangoose,Seviper,Milotic,Absol,MAbsol,Walrein,Empoleon,Infernape,Luxray]+random.choices([Raikou,Suicune,Entei,Cobalion,Virizion,Terrakion])
            
     #BETTER TRAINERS
    if trclass in ["Ace Trainer","Cool Trainer"]:
        mons=[Victreebel, Vileplume, Venusaur, MVenusaur, Nidoking, Nidoqueen,Sandslash,Dugtrio,Rhydon, Rhyperior, Persian, APersian, Ninetales,ANinetales, Blastoise, MBlastoise, Charizard, MCharizardY, MCharizardX, Exeggutor, Cloyster, Arcanine, HArcanine, Parasect, Dewgong, Blissey,Kingler,Tentacruel, Rapidash, GRapidash, Magnezone, Quagsire, Electrode, Starmie,Butterfree, Bellossom,Kingdra,Flareon, Vaporeon, Jolteon, Seaking,Golduck, Pikachu,Raichu, Azumarill, Jumpluff, Dragonite, Pidgeot,MPidgeot,Electivire, Tangrowth,Tauros,PTauros,Muk,AMuk,Manectric, MManectric, Zangoose, Pelipper, Camerupt, MCamerupt, Roserade,Mawile, MMawile,Sableye, MSableye,Swellow,Flygon,Wailord,Shiftry,Aggron,MAggron,Linoone, Milotic,Delcatty,Medicham, MMedicham, Ludicolo,Golem, Alakazam, MAlakazam,Claydol,Sharpedo, MSharpedo,Dodrio,Magcargo,Hariyama, Wigglytuff, Slaking, Banette,MBanette, Dusclops,Dusknoir,Skarmory, Exploud, Lanturn, Cacturne,Absol,MAbsol,Tropius, Gardevoir, MGardevoir, Solrock,Lunatone, Machamp, Ursaring, Probopass,Tyranitar,MTyranitar,Lapras,Slowbro,MSlowbro, Kangaskhan, MKangaskhan, Farigiraf,Marowak, Raticate, ARaticate, Aerodactyl, MAerodactyl,Weavile,Gengar,MGengar, Torterra, Abomasnow, MAbomasnow,Ambipom,WGastrodon, Pachirisu, Mismagius, Drapion,Steelix,MSteelix, Drifblim, MLopunny, Hippowdon,Gallade,MGallade, Mightyena, Ampharos, MAmpharos, Infernape,Luxray,Gyarados,MGyarados, Salamence, MSalamence,Honchkrow,Staraptor, Metagross, MMetagross,Floatzel, Anihilape, Primeape,Wyrdeer, Sneasler,Purugly,Yanmega, Bibarel, Beautifly,Hypno, Dudunsparce, Scizor,MScizor,Rampardos, Pinsir,MPinsir,Crobat,Glalie,MGlalie,Beedrill,MBeedrill,Typhlosion, Meganium, Feraligatr, Mamoswine, Darmanitan, Klinklang, Whimsicott, Scolipede, Stoutland,Haxorus, Druddigon,Hydreigon, Garchomp, MGarchomp, Zebstrika,Liepard, Beartic, Leavanny, Krookodile, Accelgor,Espeon,Gothitelle,Walrein,Mienshao, Gliscor,WRotom, Magmortar,Chandelure, Galvantula,Golurk,Archeops,Mantine,Umbreon, Excadrill,Swanna,Mandibuzz, Toxicroak, Seismitoad,Cofagrigus,Carracosta,Gorebyss,Huntail,Braviary]
        ch=random.randint(1,5)
        if ch==3:
            mons+=random.choices(legendary,k=1)
            
        
#CHALLENGERS
    if trclass == "Challenger":
        mons=[DUrshifu,WUrshifu,Hatterene,Grimmsnarl,Toxtricity,Appletun,Corviknight,Melmetal,Zeraora,Silvally,Incineroar,Aegislash,Greninja,Volcarona,Hydreigon,Mandibuzz,Bisharp,Mienshao,Ferrothorn,Reuniclus,HZoroark,Zoroark,Darmanitan,GDarmanitan,Krookodile,Conkeldurr,Excadrill,Heatran,Uxie,Mesprit,Azelf,WRotom,Togekiss,Magnezone,Garchomp,Infernape,Latias,Latios,Metagross,Salamence,Slaking,Blissey,Kingdra,Skarmory,Umbreon,Crobat,Cloyster,Starmie,AExeggutor,Typhlosion,Feraligatr,Meganium,Arcanine,Snorlax,Dragonite]+[MSharpedo,MScizor,MSteelix,MGyarados,MKangaskhan,MAlakazam,MPidgeot,MSlowbro,MAerodactyl,MBlastoise,MVenusaur,MCharizardX,MCharizardY,MHeracross,MHoundoom,MSceptile, MBlaziken,MSwampert,MGardevoir,MCamerupt,MAbsol,MSalamence,MMetagross,MLopunny,MLucario]+ultrabeasts
        ch=random.randint(1,3)
        if ch==2:
            mons+=random.choices(legendary,k=3)
        pass


    if len(team)==0 and trclass=="Challenger":
        while len(team)!=pknum:
            party=random.choices(mons)[0]
            member=party( )
            if ("💎" not in member.name and "Gigantamax" not in member.name and "Dynamax " not in member.name and "Mega " not in member.name and "(" not in member.name and "Totem " not in member.name) and len(team)<3:
                team.append(member)
                mons.remove(party)
            if ("Dynamax" in member.name or "Gigantamax" in member.name) and len(team)==3:
                team.append(member)
                mons.remove(party)
            if "Z-Crystal" in member.name and len(team)==4:
                team.append(member)
                mons.remove(party)
            if "Mega " in member.name and len(team)==5:
                team.append(member)
                mons.remove(party)
                
    if len(team)==0 and trclass in ["Expert","Veteran"]:
        while len(team)!=pknum:
            party=random.choices(mons)[0]
            member=party( )
            if ("Gigantamax" not in member.name and "Dynamax " not in member.name and "Mega " not in member.name and "(" not in member.name and "Totem " not in member.name) and len(team)<4:
                team.append(member)
                mons.remove(party)
            if ("Dynamax" in member.name or "Gigantamax" in member.name) and len(team)==4:
                team.append(member)
                mons.remove(party)
            if "Mega " in member.name and len(team)==5:
                team.append(member)
                mons.remove(party)    
            
                
    if len(team)==0 and trclass in ["Ace Trainer","Dragon Tamer"]:
        while len(team)!=pknum:
            party=random.choices(mons)[0]
            member=party( )
            if ("💎" not in member.name and "Gigantamax" not in member.name and "Dynamax " not in member.name and "Mega " not in member.name and "(" not in member.name and "Totem " not in member.name) and len(team)<2:
                team.append(member)
                mons.remove(party)
            if "💎" in member.name and len(team)==2:
                team.append(member)
                mons.remove(party)
            if ("Dynamax" in member.name or "Gigantamax" in member.name) and len(team)==3:
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
            member=party( )
            if ("💎" not in member.name and "Gigantamax" not in member.name and "Dynamax " not in member.name and "Mega " not in member.name and "Z-Crystal" not in member.name and "Totem " not in member.name) and len(team)<7:
                team.append(member)
                mons.remove(party)
            if megachance==2:
                if "Mega " in member.name and len(team)==5:
                    team.append(member)
                    mons.remove(party)
            if megachance==1:
                if "Z-Crystal" in member.name and len(team)==5:
                    team.append(member)
                    mons.remove(party)                                 
                        
    if len(team)==0 and trclass not in ["Challenger","Ace Trainer","Dragon Tamer","Elder Trainer","Veteran","Expert","Cool Trainer"]:
        megachance=0
        if "Paldea" in trclass or "Paldea" in field.location:
            megachance=3
        if "Alola" in trclass or "Alola" in field.location:
            megachance=1
        if "Galar" in trclass or "Galar" in field.location:
            megachance=4
        if "Kalos" in trclass or "Kalos" in  field.location:
            megachance=2
        if megachance==0:
            megachance=random.randint(1,4) 
        while len(team)!=pknum:
            party=random.choices(mons)[0]
            member=party( )
            if ("💎" not in member.name and "Gigantamax" not in member.name and "Dynamax " not in member.name and "Mega " not in member.name and "(" not in member.name and "Totem " not in member.name) and len(team)<5:
                team.append(member)
                mons.remove(party)
            if megachance==4:
                if ("Dynamax" in member.name or "Gigantamax" in member.name) and len(team)==5:
                    team.append(member)
                    mons.remove(party)
            if megachance==3:
                if "💎" in member.name and len(team)==5:
                    team.append(member)
                    mons.remove(party)
            if megachance==1:
                if "Z-Crystal" in member.name and len(team)==5:
                    team.append(member)
                    mons.remove(party)         
            if megachance==2:
                if "Mega " in member.name and len(team)==5:
                    team.append(member)
                    mons.remove(party)        

                                                                                
                     
    return new_name,team            

def genTrainer(trclass=None,name=None,num=6,ai=True):
    trclasslist=["Blackbelt","Dojo Master","Dragon Tamer","Skier","Kindler","Sailor","Swimmer","Veteran","Elder Trainer","Challenger","Ruin Explorer","Ace Trainer","Expert","Street Punk","Scuba Diver","Fossil Maniac","Paleontologist","Surfer","Marine Biologist","Biker","Cueball","Bird Keeper","Pilot","Sky Diver","Venom Expert","Fiery Breathe","Rocker","Guitarist","Bug Catcher","Psychic","Exorcist","Electrician","Smuggler","Thief","Goon","Boarder","Desert Explorer","Egyptian","Tamer","Captain","Pirate","Driver","Magma Grunt","Aqua Grunt","Rocket Grunt","Galactic Grunt","Gardener","Factory Boss","Industry Worker","Hiker","Kanto Trainer","Johto Trainer","Hoenn Trainer","Sinnoh Trainer","Unova Trainer","UB Expert","Businessman","Police Officer","Investigator","Military Officer","Navy Officer","Air Force Officer","Bug Researcher","Fisherman","Chaos Trainer","Plasma Grunt","Shadow Triads","Kalos Trainer","Alola Trainer","Galar Trainer","Chef","MasterChef","Cook","Foodie","Beauty","Gentleman","Camper","Lass","Scientist","Breeder","Pokémon Ranger","Backpacker","Policeman","Super Nerd","Cool Trainer","Pokémon Trainer","Paldea Trainer"]
    rg=random.choice(["Kanto","Hoenn","Johto","Sinnoh","Unova","Kalos","Alola","Galar","Paldea"])
    if trclass is None:
        rclass=random.choice(trclasslist)
    if trclass is not None:
        rclass=trclass
    trainer=teammaker(rclass,name,num)
    rname=trainer[0]
    rteam=trainer[1]
    rand=Trainer(rname,rteam,ai=ai,region=rg)
    return rand
def showparty(obj):
    num=0
    total=0
    btotal=0
    for i in obj.pokemons:
        total+=i.maxtotal
        btotal+=i.basestats
    print(f"  {obj.name}'s Team [Power:{total}({btotal})]")
    for i in obj.pokemons:
        i.owner=obj
def showmon(obj):
    for i in obj.pokemons:
        num+=1
        print("  "+str(num)+".",i.name+f"({i.basestats})")
def match():
    t1=genTrainer(ai=p1AI)
    t2=genTrainer(ai=p2AI)
    return t1,t2                        
#E4 Bruno
bruno1=MSteelix(maxiv="Yes",move=["Earthquake","Iron Head", "Curse","Gyro Ball"],nature="Brave",ability="Heatproof")
bruno2=Machamp(maxiv="gmax",move=["Knock Off","Close Combat","Stone Edge","Facade"],nature="Adamant", ability="Guts")
bruno3=Hitmonchan(maxiv="Yes",move=["Thunder Punch","Close Combat","Fire Punch","Ice Punch"],nature="Adamant")
bruno4=Hitmonlee(maxiv="Yes",move=["Hi Jump Kick","Knock Off","Close Combat","Stone Edge"],nature="Adamant")
bruno5=Steelix(maxiv="Yes",move=["Earthquake","Iron Head", "Curse","Gyro Ball"],nature="Brave",ability="Heatproof")
bruno6=Poliwrath(maxiv="Yes",move=["Close Combat","Liquidation","Recover","Rain Dance"],nature="Adamant")
bruno7=Hitmontop(maxiv="Yes")
bruno8=Hariyama(maxiv="Yes")
bruno9=Lucario(maxiv="Yes")
bruno10=AGolem(maxiv="Yes")
brunoteam=teamset([bruno6,bruno2,bruno3,bruno4,bruno5,bruno7,bruno8,bruno9,bruno10],5)+[bruno1]
bruno=Trainer("Elite Four Bruno",brunoteam,"Kanto")
#E4 Lance
lance1=Hydreigon(maxiv="Yes",move=["Dark Pulse","Flamethrower","Thunderbolt","Dragon Pulse"],nature="Modest")
lance2=Gyarados(name="Gyarados✨",maxiv="Yes",move=["Dragon Dance","Waterfall","Earthquake","Ice Fang"],nature="Adamant")
lance3=Aerodactyl(maxiv="Yes",move=["Stone Edge","Earthquake","Roost","Stealth Rock"],nature="Jolly")
lance4=Dragonite (maxiv="gmax",move=["Dragon Dance","Extreme Speed","Dragon Claw","Roost"],nature="Adamant")
lance5=Kingdra(maxiv="Yes",move=["Rain Dance","Draco Meteor","Surf","Ice Beam"],nature="Modest",ability="Swift Swim")
lance6=Charizard(name="Charizard💎",maxiv="Dragon",move=["Dragon Dance","Roost","Dragon Claw","Flare Blitz"],nature="Adamant")
lance=Trainer("Elite Four Lance",[lance1,lance2,lance3,lance6,lance5,lance4])
#E4 Lorelei 
lorelei1=Lapras(maxiv="gmax",move=["Ice Beam","Hydro Pump","Recover","Thunder"],nature="Modest",dmax=True)
lorelei2=MSlowbro(maxiv="Yes",move=["Slack Off","Flamethrower","Hydro Pump","Ice Beam"],nature="Modest")
lorelei3=Dewgong(maxiv="Yes",move=["Ice Beam","Hydro Pump","Recover","Blizzard"],nature="Modest")
lorelei4=Cloyster(maxiv="Yes",move=["Rock Blast","Pin Missile","Icicle Spear","Shell Smash"],nature="Adamant")
lorelei5=Jynx(maxiv="Yes",move=["Ice Beam","Psychic","Recover","Blizzard"],nature="Timid")
lorelei6=Mamoswine(name="Mamoswine(Z-Crystal)",maxiv="Yes",move=["Ice Beam","Earthquake","Stone Edge","Blizzard"],nature="Naughty")
lorelei7=ASandslash(maxiv="Yes")
lorelei=Trainer("Elite Four Lorelei",[lorelei6,lorelei2,lorelei3, lorelei4,lorelei5,lorelei1])
#Red
red7=Pikachu(maxiv="gmax",move=["Extreme Speed","Volt Tackle","Thunderbolt","Electroweb"],nature="Modest")
red1=MCharizardX(maxiv="Yes",move=["Dragon Dance","Dragon Claw","Flare Blitz","Roost"],nature="Jolly")
red2=Blastoise(maxiv="Yes",move=["Hydro Pump","Shell Smash","Water Spout","Ice Beam"],nature="Modest")
red3=Venusaur (maxiv="Yes",move=["Earth Power","Sleep Powder","Sludge Bomb","Giga Drain"],nature="Modest")
red4=Lapras(maxiv="Yes",move=["Hydro Pump","Ice Beam","Thunderbolt","Freeze-Dry"],nature="Modest")
red5=Snorlax(maxiv="Yes",move=["Hyper Beam","Body Slam","Return","Double-Edge"],nature="Relaxed")
red6=Espeon(maxiv="Yes",move=["Psychic","Dazzling Gleam","Morning Sun","Shadow Ball"],nature="Modest")
red8=Mewtwo(maxiv="Yes")
red9=Zapdos(maxiv="Yes")
red10=Moltres(maxiv="Yes")
red11=Articuno(maxiv="Yes")
redteam=teamset([red4,red5,red6,red2,red3,red8,red9,red10],4)+[red7,red1]
red=Trainer("Pokémon Trainer Red",redteam,"Kanto")
#E4 Agatha
agatha1=Crobat(maxiv="Yes",move=["Roost","Toxic","Brave Bird","U-Turn"],nature="Jolly")
agatha2=Mismagius(maxiv="Yes",move=["Thunderbolt","Dazzling Gleam","Shadow Ball","Nasty Plot"],nature="Timid")
agatha3=Arbok(maxiv="Yes",move=["Earthquake","Poison Jab","Crunch","Coil"], nature="Adamant")
agatha4=Weezing(maxiv="Yes",move=["Sludge Bomb","Will-O-Wisp","Flamethrower","Toxic"],nature="Bold")
agatha5=Gengar(maxiv="gmax",move=["Thunderbolt","Sludge Bomb","Shadow Ball","Nasty Plot"],nature="Timid")
agatha6=MGengar(maxiv="Yes",move=["Thunderbolt","Sludge Bomb","Shadow Ball","Nasty Plot"],nature="Timid")
agatha7=AMarowak(maxiv="Yes")
agatha=Trainer("Elite Four Agatha",[agatha1,agatha2,agatha3,agatha4,agatha5,agatha6],"Kanto")
#alsada
alsada1=Screamtail(maxiv="Yes")
alsada2=Slitherwing(maxiv="Yes")
alsada6=Roaringmoon(maxiv="Yes")
alsada4=Fluttermane(maxiv="Yes")
alsada5=Sandyshocks(maxiv="Yes")
alsada3=Greattusk(maxiv="Yes")
alsada9=Koraidon(name="Koraidon💎",maxiv=random.choice(["Fighting","Dragon"]))
alsadateam=teamset ([alsada1,alsada2,alsada3,alsada4],4)+teamset([alsada5,alsada6],1)+[alsada9]
alsada=Trainer("Professor Sada",alsadateam,"Paldea")
#alturo
alturo1=Ironhands(maxiv="Yes")
alturo2=Ironmoth(maxiv="Yes")
alturo6=Ironthorns(maxiv="Yes")
alturo4=Ironbundle(maxiv="Yes")
alturo5=Ironjugulis(maxiv="Yes")
alturo3=Irontreads(maxiv="Yes")
alturo9=Miraidon(name="Miraidon💎",maxiv=random.choice(["Electric","Dragon"]))
alturoteam=teamset ([alturo1,alturo2,alturo3,alturo4],4)+teamset([alturo5,alturo6],1)+[alturo9]
alturo=Trainer("Professor Turo",alturoteam,"Paldea")
#Oak
oak1=Tauros(maxiv="Yes")
oak2=Exeggutor(maxiv="Yes")
oak3=Arcanine(maxiv="Yes")
oak4=Gyarados(maxiv="Yes")
oak5=Venusaur(maxiv="Yes")
oak6=Charizard(maxiv="Yes")
oak7=Blastoise(maxiv="Yes")
oak8=Dragonite(maxiv="Yes")
oak9=Mew(name="Mew(Z-Crystal)",move=["Psychic","Transform","Shadow Ball","Aura Sphere"],maxiv="Yes")
oakteam=teamset ([oak1,oak2,oak3,oak4,oak8],4)+teamset([oak5,oak6,oak7],1)+[oak9]
oak=Trainer("Professor Oak",oakteam,"Kanto")
#janine
janine3=Tentacruel(maxiv="Yes")
janine4=Ariados(maxiv="Yes")
janine5=Toxicroak(maxiv="Yes")
janine6=Weezing(maxiv="Yes")
janine7=Venomoth(maxiv="Yes")
janine8=Drapion(maxiv="Yes")
janine9=Crobat(maxiv="Yes")
janineteam=teamset ([janine3,janine4,janine8,janine5,janine6,janine7],5)+[janine9]
janine=Trainer("Gym Leader Janine",janineteam,"Kanto")
#goh
goh1=Heracross(maxiv="Yes")
goh2=Scizor(maxiv="Yes")
goh10=Beedrill(maxiv="Yes")
goh3=Aerodactyl (maxiv="Yes")
goh4=Absol(maxiv="Yes")
goh5=Rillaboom(maxiv="Yes")
goh6=Darmanitan(maxiv="Yes")
goh7=Inteleon(maxiv="Yes")
goh8=Suicune(maxiv="Yes")
goh9=Cinderace(maxiv="gmax")
goh11=Flygon (maxiv="Yes")
goh12=Dewgong (maxiv="Yes")
goh13=Raichu(maxiv="Yes")
goh14=Swellow(maxiv="Yes")
goh15=Pinsir(maxiv="Yes")
goh16=Butterfree (maxiv="Yes")
goh17=Greninja (maxiv="Yes")
goh18=Golurk(maxiv="Yes")
goh19=Exeggutor (maxiv="Yes")
goh20=Hitmonchan(maxiv="Yes")
goh21=Electrode(name="Electrode✨",maxiv="Yes")
goh22=Cloyster (maxiv="Yes")
goh23=Kingdra(maxiv="Yes")
goh24=Altaria(maxiv="Yes")
goh25=Ferrothorn (maxiv="Yes")
goh26=AExeggutor (maxiv="Yes")
goh27=Shedinja (maxiv="Yes")
goh28=Regieleki(maxiv="Yes")
gohteam=teamset ([goh1, goh2,goh3,goh4,goh5,goh6,goh7,goh10,goh11,goh12,goh13,goh14,goh15,goh16,goh17,goh18,goh19,goh20,goh21,goh22,goh23,goh24,goh25,goh26,goh27],3)+[goh8,goh28,goh9]
goh=Trainer("Pokémon Trainer Goh",gohteam,"Kanto")
#Champion Steven
steven1=Claydol(maxiv="Yes",move=["Sandstorm","Ancient Power","Psychic","Calm Mind"],nature="Bold")
steven2=Armaldo(maxiv="Yes",move=["X-Scissor","Stone Edge","Earthquake","Ancient Power"],nature="Adamant")
steven3=Cradily (maxiv="Yes",move=["Giga Drain","Leech Seed","Strength Sap","Ancient Power"],nature="Modest")
steven4=Skarmory(maxiv="Yes",move=["Brave Bird","Roost","Body Press","Stealth Rock"],nature="Impish")
steven5=Aggron(maxiv="gmax",move=["Body Press","Iron Head","Iron Defense","Stone Edge"],nature="Impish")
steven6=MMetagross(name="Mega Metagross✨",maxiv="Yes", move=["Zen Headbutt","Earthquake","Meteor Mash","Fire Punch"],nature="Adamant")
steven7=Diancie(maxiv="Yes")
steven8=Excadrill(maxiv="Yes")
steven9=Aerodactyl(maxiv="Yes")
steven10=Archeops(maxiv="Yes")
steventeam=teamset([steven1,steven2,steven3,steven4,steven5,steven7,steven8,steven9,steven10],5)+[steven6]
steven=Trainer("Hoenn Champion Steven", steventeam,"Hoenn")
#Champion Wallace
wallace1=Ludicolo(maxiv="Yes",move=["Giga Drain","Rain Dance","Ice Beam","Leech Seed"])
wallace2=Starmie(maxiv="Yes",move=["Psychic","Recover","Surf","Thunderbolt"],nature="Timid")
wallace3=Wailord(maxiv="Yes",move=["Water Spout","Ice Beam","Hydro Pump","Thunder Wave"])
wallace4=Gyarados(maxiv="Yes",move=["Dragon Dance","Waterfall","Earthquake","Crunch"],nature="Adamant")
wallace5=MSwampert(maxiv="Yes",move=["Earthquake","Liquidation","Ice Punch","Hammer Arm"],nature="Adamant")
wallace6=Milotic(maxiv="gmax",move=["Scald","Toxic","Ice Beam","Recover"],nature="Modest")
wallace7=Walrein(maxiv="Yes")
wallace8=Seaking(maxiv="Yes")
wallace9=Sharpedo(maxiv="Yes")
wallaceteam=teamset([wallace1,wallace2,wallace3,wallace4,wallace5,wallace7,wallace8,wallace9],5)+[wallace6]
wallace=Trainer("Hoenn Champion Wallace",wallaceteam,"Hoenn")
#Tobias
tobias1=Darkrai(maxiv="gmax",move=["Dark Void","Shadow Ball","Dark Pulse","Psychic"],nature="Modest")
tobias2=MLatios(maxiv="Yes",move=["Luster Purge","Dragon Pulse","Calm Mind","Shadow Ball"],nature="Timid")
tobias3=Entei(maxiv="Yes",move=["Lava Plume","Stone Edge","Flare Blitz","Fire Blast"],nature="Hasty")
tobias4=Heatran(maxiv="Yes",move=["Magma Storm","Flash Cannon","Ancient Power","Earth Power"],nature="Calm")
tobias5=Latias(maxiv="Yes",move=["Mist Ball","Dragon Pulse","Calm Mind","Shadow Ball"],nature="Timid")
tobias6=Cresselia(maxiv="Yes",move=["Lunar Blessing","Moonblast","Psychic","Shadow Ball"],nature="Calm")
tobias=Trainer("Pokémon Trainer Tobias",[tobias3,tobias4,tobias5,tobias6,tobias1,tobias2],"Sinnoh")
#Champion Cynthia
cynthia1=WGastrodon(maxiv="Yes",move=["Earth Power","Ice Beam","Recover","Ancient Power"],nature="Calm")
cynthia2=Togekiss(maxiv="gmax",move=["Air Slash","Roost","Moonblast","Nasty Plot"],nature="Modest")
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
aaron6=Drapion(maxiv="gmax",move=["Wicked Blow","Toxic","Crunch","Cross Poison"],nature="Adamant")
aaron=Trainer("Elite Four Aaron",[aaron1,aaron2,aaron3,aaron4,aaron5,aaron6],"Sinnoh")
#Bertha
bertha1=Golem(maxiv="Yes")
bertha2=Hippowdon(maxiv="Yes")
bertha3=Gliscor(maxiv="Yes")
bertha4=Nidoking (maxiv="Yes")
bertha5=Mamoswine(maxiv="Yes")
bertha6=Rhyperior(maxiv="gmax")
bertha7=MSteelix(maxiv="Yes")
bertha=Trainer("Elite Four Bertha",[bertha1,bertha2,bertha3,bertha4,bertha7,bertha6],"Sinnoh")
#rika
rika1=Camerupt(maxiv="Yes")
rika2=Whiscash(maxiv="Yes")
rika3=Donphan(maxiv="Yes")
rika4=Dugtrio(maxiv="Yes")
rika5=Greattusk(maxiv="gmax")
rika6=Clodsire(name="Clodsire💎",maxiv="Ground")
rika7=Irontreads(maxiv="gmax")
rikateam=teamset([rika1,rika2,rika3,rika4,rika6],5)+teamset([rika5,rika7],1)
rika=Trainer("Elite Four Rika",rikateam,"Paldea")
#Flint
flint1=Rapidash(maxiv="Yes")
flint2=Entei(maxiv="Yes")
flint3=Magmortar(maxiv="Yes")
flint4=MHoundoom(maxiv="Yes")
flint5=Arcanine(maxiv="Yes")
flint6=Infernape(maxiv="gmax")
flint=Trainer("Elite Four Flint",[flint1,flint2,flint3,flint4,flint5,flint6],"Sinnoh")
#Lucian
lucian1=Farigiraf(maxiv="Yes")
lucian2=Espeon(maxiv="Yes")
lucian3=Bronzong(maxiv="Yes")
lucian4=Alakazam(maxiv="gmax")
lucian5=Slowbro(maxiv="Yes")
lucian6=MGallade(maxiv="Yes")
lucian=Trainer("Elite Four Lucian",[lucian1,lucian2,lucian3,lucian4,lucian5,lucian6],"Sinnoh")
#Buck
buck1=Regice(maxiv="Yes")
buck2=Regirock(maxiv="Yes")
buck3=Registeel(maxiv="Yes")
buck4=Cresselia(maxiv="gmax")
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
palmer6=Regigigas(maxiv="gmax")
palmer=Trainer("Tower Tycoon Palmer",[palmer1,palmer2,palmer3,palmer4,palmer5,palmer6],"Sinnoh")
#Thorton
Thorton1=Bronzong(maxiv="Yes")
Thorton2=Ursaluna(maxiv="Yes")
Thorton3=Ledian(maxiv="Yes")
Thorton4=Electivire(maxiv="Yes")
Thorton5=Skarmory(maxiv="Yes")
Thorton6=MTyranitar(maxiv="Yes")
Thorton=Trainer("Factory Head Thorton",[Thorton1,Thorton2,Thorton3,Thorton4,Thorton5,Thorton6],"Sinnoh")
#noland
noland1=Breloom(maxiv="Yes")
noland2=Rhyperior(maxiv="Yes")
noland3=Machamp(maxiv="Yes")
noland4=Venusaur(maxiv="Yes")
noland5=Articuno(maxiv="Yes")
noland6=MPinsir(maxiv="Yes")
noland7=Aggron(maxiv="Yes")
noland8=Camerupt(maxiv="Yes")
noland9=Sandslash(maxiv="Yes")
noland10=Golduck(maxiv="Yes")
noland11=Manectric(maxiv="Yes")
noland12=Flygon(maxiv="Yes")
nolandteam=teamset([noland1,noland2,noland3,noland4,noland5,noland7,noland10,noland11,noland12,noland8,noland9],5)+[noland6]
noland=Trainer("Factory Head Noland",nolandteam,"Hoenn")
#Darach
darach1=Staraptor(maxiv="Yes")
darach2=Empoleon(maxiv="Yes")
darach3=Houndoom(maxiv="Yes")
darach4=Entei(maxiv="gmax")
darach5=MGallade(maxiv="Yes")
darach6=Alakazam(maxiv="Yes")
darach7=Metagross(maxiv="Yes")
darachteam=teamset([darach1,darach2,darach3,darach6,darach7],4)+[darach4,darach5]
darach=Trainer("Castle Velvet Darach",darachteam,"Sinnoh")
#Dahlia
dahlia1=Dusknoir(maxiv="Yes")
dahlia2=Medicham(maxiv="Yes")
dahlia3=Ludicolo(maxiv="Yes")
dahlia4=MBlaziken(maxiv="Yes")
dahlia5=Togekiss(maxiv="Yes")
dahlia6=Zapdos(maxiv="gmax")
dahlia=Trainer("Arcade Star Dahlia",[dahlia1,dahlia2,dahlia3,dahlia5,dahlia4,dahlia6],"Sinnoh")
#Archie
archie7=Walrein(maxiv="Yes")
archie1=Mightyena(maxiv="Yes")
archie2=Muk(maxiv="Yes")
archie3=Crobat(maxiv="Yes")
archie4=Tentacruel(maxiv="Yes")
archie5=MSharpedo(maxiv="Yes")
archie6=PKyogre(maxiv="Yes")
archie7=Kyogre(maxiv="gmax")
archieteam=teamset([archie1,archie2,archie3,archie4,archie5],5)+teamset([archie6,archie7],1)
archie=Trainer("Aqua Leader Archie",archieteam,"Hoenn")
#Maxie
maxie7=Houndoom(maxiv="Yes")
maxie1=Mightyena(maxiv="Yes")
maxie2=Weezing(maxiv="Yes")
maxie3=Crobat(maxiv="Yes")
maxie4=Torkoal(maxiv="Yes")
maxie5=MCamerupt(maxiv="Yes")
maxie6=PGroudon(maxiv="Yes")
maxie7=Groudon(maxiv="gmax")
maxieteam=[maxie1,maxie2,maxie3,maxie4,maxie5]+teamset([maxie6,maxie7],1)
maxie=Trainer("Magma Leader Maxie",maxieteam,"Hoenn")
#Tabitha
tab1=Mightyena(maxiv="Yes")
tab2=Weezing(maxiv="Yes")
tab3=Crobat(maxiv="Yes")
tab4=Torkoal(maxiv="Yes")
tab5=Camerupt(maxiv="gmax")
tab6=Swellow(maxiv="Yes")
tabitha=Trainer("Magma Admin Tabitha",[tab1,tab2,tab3,tab4,tab5,tab6],"Hoenn")
#Brandon
brandon1=Regice(maxiv="Yes")
brandon2=Regirock(maxiv="Yes")
brandon3=Registeel(maxiv="gmax")
brandon4=Articuno(maxiv="Yes")
brandon5=Zapdos(maxiv="Yes")
brandon6=Moltres(maxiv="Yes")
brandon7=Ninjask(maxiv="Yes")
brandon8=Dusclops(maxiv="Yes")
brandon9=Solrock(maxiv="Yes")
brandonteam=teamset([brandon7,brandon8,brandon9,brandon4,brandon5,brandon6],3)+[brandon1,brandon2,brandon3]
brandon=Trainer ("Pyramid King Brandon",brandonteam,"Hoenn")
#Illegal
illegal1=OArceus(maxiv="gmax")
illegal2=Cloyster()
illegal=Trainer("Missing No.",[illegal1,illegal2],"???")
#cyrus
cyrus1=Weavile(maxiv="Yes")
cyrus2=Honchkrow(maxiv="Yes")
cyrus3=Crobat(maxiv="Yes")
cyrus5=Houndoom(maxiv="Yes")
cyrus4=Gyarados (maxiv="Yes")
cyrus8=Entei(maxiv="gmax")
cyrus6=Dialga(maxiv="Yes")
cyrus7=Palkia(maxiv="Yes")
cyrus=Trainer("Galactic Leader Cyrus",[cyrus1,cyrus2,cyrus8,cyrus4,cyrus6,cyrus7],"Sinnoh")
#Saturn
saturn1=Alakazam(maxiv="Yes")
saturn2=Bronzong(maxiv="Yes")
saturn3=Toxicroak(maxiv="Yes")
saturn4=Absol(maxiv="Yes")
saturn5=Crobat(maxiv="Yes")
saturn6=Heatran(maxiv="gmax")
saturn=Trainer("Galactic Commander Saturn",[saturn1,saturn2,saturn3,saturn4,saturn5,saturn6],"Sinnoh")
#E4 Siebold
siebold1=Clawitzer(maxiv="Yes")
siebold2=Gyarados(maxiv="Yes")
siebold3=Starmie(maxiv="Yes")
siebold4=Barbaracle(maxiv="Yes")
siebold5=Milotic(maxiv="gmax")
siebold6=MBlastoise(maxiv="Yes")
siebold=Trainer("Elite Four Siebold",[siebold1,siebold2,siebold3,siebold4,siebold5,siebold6],"Kalos")
#E4 Wikstrom
wikstrom1=Probopass(maxiv="Yes")
wikstrom2=Aegislash (maxiv="Yes")
wikstrom3=Escavalier(maxiv="gmax")
wikstrom4=HGoodra(maxiv="Yes")
wikstrom5=Klefki(maxiv="Yes")
wikstrom6=MScizor(maxiv="Yes")
wikstrom=Trainer("Elite Four Wikstrom",[wikstrom1,wikstrom2,wikstrom3,wikstrom4,wikstrom5,wikstrom6],"Kalos")
#E4 Drasna
drasna1=Druddigon(maxiv="Yes")
drasna2=Dragalge(maxiv="Yes")
drasna3=Noivern(maxiv="gmax")
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
malva7=Yveltal(maxiv="gmax")
malva=Trainer("Elite Four Malva",[malva1,malva2,malva4,malva5,malva6,malva7],"Kalos")
#n
n1=Carracosta(maxiv="Yes")
n2=Vanilluxe(maxiv="Yes")
n3=Archeops(maxiv="Yes")
n4=Zoroark(maxiv="gmax")
n5=Zekrom(maxiv="Yes")
n6=Reshiram(maxiv="Yes")
n=Trainer("Pokémon Trainer N",[n1,n2,n3,n4,n5,n6],"Unova")
#Ghetsis
ghet4=Hydreigon(maxiv="gmax")
ghet2=Kingambit (maxiv="Yes")
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
alain2=Kingambit (maxiv="Yes",move=["Thunder Wave","Focus Blast","Iron Head","Night Slash"],item="Life Orb")
alain3=Unfezant(maxiv="Yes",move=["Sky Attack","Steel Wing","Hurricane","Air Slash"])
alain4=Metagross(maxiv="Yes",move=["Meteor Mash","Psyshock","Rock Slide","Zen Headbutt"],nature="Naughty")
alain5=Weavile(maxiv="Yes",move=["Protect","Night Slash","Ice Beam","Ice Shard"],nature="Hasty")
alain6=MCharizardX(maxiv="Yes",move=["Flamethrower","Dragon Claw","Thunder Punch","Blast Burn"],nature="Hasty")
alain7=Malamar(maxiv="Yes")
alain8=Chesnaught(maxiv="gmax")
alainteam=teamset([alain1,alain2,alain3,alain4,alain5,alain7,alain8],5)+[alain6]
alain=Trainer("Pokémon Trainer Alain",alainteam,"Unova")
#Anabel
anabel1=Alakazam(maxiv="Yes")
anabel2=Latios(maxiv="Yes")
anabel3=Snorlax(maxiv="Yes")
anabel4=Entei(maxiv="Yes")
anabel5=Raikou(maxiv="gmax")
anabel6=MLucario(maxiv="Yes")
anabel=Trainer("Salon Maiden Anabel",[anabel1,anabel2,anabel3,anabel4,anabel5,anabel6],"Hoenn")
#greta
greta1=Heracross(maxiv="gmax")
greta2=Breloom(maxiv="Yes")
greta3=Umbreon(maxiv="Yes")
greta4=Gengar(maxiv="Yes")
greta5=Hariyama(maxiv="Yes")
greta6=MMedicham(maxiv="Yes")
greta=Trainer("Arena Tycoon Greta",[greta1,greta2,greta3,greta4,greta5,greta6],"Hoenn")
#Tucker
tucker1=Metagross(maxiv="Yes")
tucker2=Arcanine(maxiv="Yes")
tucker3=Charizard(maxiv="Yes")
tucker4=Salamence(maxiv="Yes")
tucker5=Latias(maxiv="gmax")
tucker6=MSwampert(maxiv="Yes")
tucker=Trainer ("Dome Ace Tucker",[tucker1,tucker2,tucker3,tucker4,tucker5,tucker6],"Hoenn")
#Lucy
lucy1=Arbok(maxiv="Yes")
lucy2=Snorlax(maxiv="Yes")
lucy3=Steelix(maxiv="Yes")
lucy4=Gyarados(maxiv="Yes")
lucy5=Milotic(maxiv="Yes")
lucy6=Seviper(maxiv="gmax")
lucy=Trainer ("Pike Queen Lucy",[lucy1,lucy2,lucy3,lucy4,lucy5,lucy6],"Hoenn")
#spenser
spenser1=Arcanine(maxiv="Yes")
spenser2=Lapras(maxiv="Yes")
spenser3=Slaking(maxiv="Yes")
spenser4=Crobat(maxiv="Yes")
spenser5=Suicune(maxiv="gmax")
spenser6=MVenusaur(maxiv="Yes")
spenser=Trainer("Palace Maven Spenser",[spenser1,spenser2,spenser3,spenser4,spenser5,spenser6],"Hoenn")
#Giovanni
gio1=Nidoqueen(maxiv="Yes")
gio2=Nidoking(maxiv="Yes")
gio3=Honchkrow(maxiv="Yes")
gio4=Rhyperior(maxiv="Yes")
gio5=MKangaskhan(maxiv="Yes")
gio6=Mewtwo(maxiv="gmax")
gio7=Garchomp(maxiv="Yes")
gio8=Dugtrio(maxiv="Yes")
gio9=Steelix(maxiv="Yes")
gio10=Persian(maxiv="Yes")
gio11=Marowak(maxiv="Yes")
gio12=Sandslash(maxiv="Yes")
gio13=Gliscor(maxiv="Yes")
gio14=Krookodile(maxiv="Yes")
gio15=Hippowdon(maxiv="Yes")
gio16=TLandorus(maxiv="Yes")
gio17=TThundurus(maxiv="Yes")
gio18=TTornadus(maxiv="Yes")
gio19=MMewtwoX(maxiv="Yes")
gio20=MMewtwoY(maxiv="Yes")
gio21=Kangaskhan(maxiv="gmax")
gioteam1=teamset([gio1,gio2,gio3,gio4,gio7,gio8,gio9,gio10,gio11,gio12,gio13,gio14,gio15,gio16,gio17,gio18],4)+[gio5,gio6]
gioteam2=teamset([gio1,gio2,gio3,gio4,gio7,gio8,gio9,gio10,gio11,gio12,gio13,gio14,gio15,gio16,gio17,gio18],4)+[gio21]+teamset([gio19,gio20],1)
gioteam=random.choice([gioteam1,gioteam2])
giovanni=Trainer("Rocket Boss Giovanni",gioteam,"Kanto")
#Archer
archer1=Electrode(maxiv="Yes")
archer2=Mightyena(maxiv="Yes")
archer3=Weezing(maxiv="Yes")
archer4=Crobat(maxiv="Yes")
archer5=Tyranitar(maxiv="gmax")
archer6=MHoundoom(maxiv="Yes")
archer=Trainer("Rocket Commander Archer",[archer1,archer2,archer3,archer4,archer5,archer6],"Kanto")
#Ariana
ariana1=Muk(maxiv="Yes")
ariana2=Honchkrow(maxiv="Yes")
ariana3=Weavile(maxiv="Yes")
ariana4=Crobat(maxiv="Yes")
ariana5=Arbok(maxiv="gmax")
ariana6=MMawile(maxiv="Yes")
ariana=Trainer("Rocket Commander Ariana",[ariana1,ariana2,ariana3,ariana4,ariana5,ariana6],"Kanto")
#Silver
silver1=Weavile (maxiv="Yes")
silver2=Honchkrow(maxiv="Yes")
silver3=Kingdra(maxiv="Yes")
silver4=Ursaluna(maxiv="Yes")
silver5=MGyarados(name="Mega Gyarados✨",maxiv="Yes")
silver6=Feraligatr(maxiv="gmax")
silver7=Gengar(maxiv="Yes")
silver8=Alakazam (maxiv="Yes")
silver9=Crobat(maxiv="Yes")
silver10=Magnezone(maxiv="Yes")
silverteam=teamset([silver1,silver2,silver3,silver4,silver7,silver8,silver9,silver10],4)+[silver6,silver5]
silver=Trainer("Pokémon Trainer Silver",silverteam,"Johto")
#Gary
gary1=Arcanine(maxiv="Yes")
gary2=Nidoking(maxiv="Yes")
gary3=Scizor(maxiv="Yes")
gary4=Umbreon(maxiv="Yes")
gary5=Electivire(maxiv="Yes")
gary6=Blastoise(maxiv="gmax")
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
blue3=Rhyperior(maxiv="gmax")
blue4=Gyarados(maxiv="Yes")
blue5=Arcanine(maxiv="Yes")
blue6=MPidgeot(maxiv="Yes")
blue7=Machamp(maxiv="Yes")
blue8=Tyranitar(maxiv="Yes")
blue9=Blastoise (maxiv="Yes")
blue10=Venusaur(maxiv="Yes")
blue11=Charizard(maxiv="Yes")
blue12=Ninetales(maxiv="Yes")
blue13=Cloyster(maxiv="Yes")
blue14=Jolteon(maxiv="Yes")
blue15=Vaporeon (maxiv="Yes")
blue16=Flareon(maxiv="Yes")
blue17=Heracross(maxiv="Yes")
blue18=Aerodactyl(maxiv="Yes")
blueteam=teamset([blue2,blue3,blue4,blue5,blue7,blue8],3)+teamset([blue14,blue15,blue16],1)+teamset([blue9,blue10,blue11],1)+[blue6]
blue=Trainer("Pokémon Trainer Blue",blueteam,"Kanto")
#falkner
falkner1=Pelipper(maxiv="Yes")
falkner2=Honchkrow(maxiv="Yes")
falkner3=Swellow(maxiv="Yes")
falkner4=Skarmory(maxiv="Yes")
falkner5=Noctowl(maxiv="Yes")
falkner6=MPidgeot(maxiv="Yes")
falkner7=Staraptor(maxiv="Yes")
falkner8=Fearow(maxiv="Yes")
falkner9=Xatu(maxiv="Yes")
falkner10=Dodrio(maxiv="Yes")
falkner11=Crobat(maxiv="gmax")
falkner12=Aerodactyl(maxiv="Yes")
falkner13=Lugia(maxiv="Yes")
falknerteam=teamset([falkner1,falkner2,falkner3,falkner4,falkner5,falkner7,falkner8,falkner9,falkner10,falkner11,falkner12,falkner13],5)+[falkner6]
falkner=Trainer ("Gym Leader Falkner",falknerteam,"Johto")
#Ethan
ethan1=Tauros(maxiv="Yes")
ethan2=Tangrowth(maxiv="Yes")
ethan3=PorygonZ(maxiv="Yes")
ethan4=Azumarill(maxiv="Yes")
ethan5=MVenusaur(maxiv="Yes")
ethan6=Typhlosion(maxiv="Grass",move=["Hidden Power","Eruption","Fire Blast","Focus Blast"])
ethan=Trainer ("Pokémon Trainer Ethan",[ethan1,ethan2,ethan3,ethan4,ethan5,ethan6],"Johto")
#Kukui
kukui1=Braviary(maxiv="Yes")
kukui2=Venusaur(maxiv="gmax")
kukui3=Empoleon(maxiv="Yes")
kukui4=Lucario(maxiv="Yes")
kukui5=MDLycanroc(maxiv="Yes")
kukui6=Incineroar(name="Incineroar(Z-Crystal)",maxiv="Yes")
kukui=Trainer("Professor Kukui",[kukui1,kukui2,kukui3,kukui4,kukui5,kukui6],"Alola")
#Mustard
mustard1=WUrshifu(maxiv="gmax")
mustard9=WUrshifu(maxiv="Yes")
mustard8=DUrshifu(maxiv="gmax")
mustard2=Mienshao(maxiv="Yes")
mustard3=Corviknight(maxiv="Yes")
mustard5=MDLycanroc(maxiv="Yes")
mustard4=Kommo(maxiv="Yes")
mustard7=Luxray(maxiv="Yes")
mustard6=DUrshifu(maxiv="Yes")
mustardteam1=teamset([mustard2,mustard3,mustard4,mustard5],4)+[mustard1,mustard6]
mustardteam2=teamset([mustard2,mustard3,mustard4,mustard5],4)+[mustard9,mustard8]
mustard=Trainer("Pokémon Trainer Mustard", random.choice([mustardteam1,mustardteam2]),"Galar")    
#Brendan
bren1=Gardevoir(maxiv="Yes")
bren9=Aggron(maxiv="Yes")
bren7=Shiftry(maxiv="Yes")
bren8=Swampert(maxiv="Yes")
bren5=Latios(maxiv="gmax")
bren6=MSceptile(maxiv="Yes")
bren11=Wailord(maxiv="Yes")
bren12=Breloom(maxiv="Yes")
bren13=Camerupt(maxiv="Yes")
bren14=Swellow(maxiv="Yes")
bren15=Pelipper(maxiv="Yes")
bren16=Ludicolo(maxiv="Yes")
bren17=Magcargo(maxiv="Yes")
bren18=Tropius(maxiv="Yes")
bren19=Raichu(maxiv="Yes")
bren20=Claydol(maxiv="Yes")
bren21=Exploud(maxiv="Yes")
bren10=PGroudon(maxiv="Yes")
bren22=PKyogre(maxiv="Yes")
bren23=Rayquaza(maxiv="Yes")
brenteam=teamset([bren1,bren5,bren7,bren8,bren9,bren11,bren12,bren13,bren14,bren15,bren16,bren17,bren18,bren19,bren20,bren21,bren10,bren22,bren23],5)+[bren6]
brendan=Trainer("Pokémon Trainer Brendan",brenteam,"Hoenn")
#may
may1=Gallade(maxiv="Yes")
may2=Blastoise(maxiv="Yes")
may3=Snorlax(maxiv="Yes")
may4=Beautifly(maxiv="Yes")
may9=Glaceon(maxiv="Yes")
may7=Venusaur(maxiv="Yes")
may8=Swampert(maxiv="Yes")
may5=Latias(maxiv="gmax")
may6=MBlaziken(maxiv="Yes")
may10=Delcatty(maxiv="Yes")
may11=Wailord(maxiv="Yes")
may12=Breloom(maxiv="Yes")
may13=Camerupt(maxiv="Yes")
may14=Swellow(maxiv="Yes")
may15=Pelipper(maxiv="Yes")
may16=Ludicolo(maxiv="Yes")
may17=Magcargo(maxiv="Yes")
may18=Tropius(maxiv="Yes")
may19=Raichu(maxiv="Yes")
may20=Claydol(maxiv="Yes")
may21=Exploud(maxiv="Yes")
may22=PKyogre(maxiv="Yes")
may23=PGroudon(maxiv="Yes")
may24=Rayquaza(maxiv="Yes")
mayteam=teamset([may1,may2,may3,may4,may5,may7,may8,may9,may10,may11,may12,may13,may14,may15,may16,may17,may18,may19,may20,may21,may22,may23,may24],5)+[may6]
may=Trainer("Pokémon Trainer May",mayteam,"Hoenn")
#Ingo
ingo1=Gliscor(maxiv="Yes")
ingo2=Alakazam(maxiv="Yes")
ingo3=Tangrowth(maxiv="Yes")
ingo4=Machamp(maxiv="gmax")
ingo5=Probopass(maxiv="Yes")
ingo6=Magnezone(maxiv="Yes")
ingo7=Haxorus(maxiv="Yes")
ingo=Trainer("Subway Boss Ingo",[ingo1,ingo2,ingo3,ingo4,ingo5,ingo6],"Unova")
#Phoebe
phoebe1=Banette(maxiv="Yes")
phoebe2=Mismagius(maxiv="Yes")
phoebe3=Drifblim(maxiv="Yes")
phoebe4=Chandelure(maxiv="Yes")
phoebe5=Dusknoir(maxiv="gmax")
phoebe6=MSableye(maxiv="Yes")
phoebe7=MBanette(maxiv="Yes")
phoebeteam=teamset([phoebe1,phoebe2,phoebe3,phoebe4,phoebe5],5)+teamset([phoebe6,phoebe7],1)
phoebe=Trainer ("Elite Four Phoebe",phoebeteam,"Hoenn")
#Sidney
sidney1=Shiftry(maxiv="Yes")
sidney2=Scrafty(maxiv="Yes")
sidney3=Zoroark(maxiv="Yes")
sidney4=Sharpedo(maxiv="Yes")
sidney5=Mandibuzz(maxiv="Yes")
sidney6=MAbsol(maxiv="Yes")
sidney7=Cacturne(maxiv="gmax")
sidney8=Crawdaunt(maxiv="Yes")
sidney9=Mightyena(maxiv="Yes")
sidneyteam=teamset([sidney1,sidney2,sidney3,sidney4,sidney5,sidney7,sidney8,sidney9],5)+[sidney6]
sidney=Trainer ("Elite Four Sidney",sidneyteam,"Hoenn")
#Glacia
glacia1=Abomasnow(maxiv="Yes")
glacia2=Beartic(maxiv="Yes")
glacia3=Froslass(maxiv="Yes")
glacia4=Vanilluxe(maxiv="Yes")
glacia5=Walrein(maxiv="gmax")
glacia6=MGlalie(maxiv="Yes")
glacia=Trainer ("Elite Four Glacia",[glacia1,glacia2,glacia3,glacia4,glacia5,glacia6],"Hoenn")
#Drake
drake1=Altaria(maxiv="Yes")
drake2=Dragalge(maxiv="Yes")
drake3=Kingdra(maxiv="Yes")
drake4=Flygon(maxiv="gmax")
drake5=Haxorus(maxiv="Yes")
drake6=MSalamence(maxiv="Yes")
drake=Trainer ("Elite Four Drake",[drake1,drake2,drake3,drake4,drake5,drake6],"Hoenn")
#Karen
karen1=Weavile(maxiv="Yes")
karen2=Absol(maxiv="Yes")
karen3=Spiritomb(maxiv="Yes")
karen4=Houndoom(maxiv="Yes")
karen5=Honchkrow(maxiv="Yes")
karen6=Umbreon(maxiv="gmax")
karen7=Vileplume(maxiv="Yes")
karen8=Gengar(maxiv="Yes")
karenteam=teamset([karen1,karen2,karen3,karen4,karen5,karen7,karen8],5)+[karen6]
karen=Trainer ("Elite Four Karen",karenteam,"Johto")
#brock
brock1=Omastar(maxiv="Yes")
brock2=Kabutops(maxiv="Yes")
brock3=Rhyperior (maxiv="gmax")
brock4=Golem(maxiv="Yes")
brock5=Tyranitar(maxiv="Yes")
brock6=MSteelix(maxiv="Yes")
brock7=Rampardos(maxiv="Yes")
brock8=Aerodactyl(maxiv="Yes")
brock9=Relicanth(maxiv="Yes")
brock10=Sudowoodo(maxiv="Yes")
brock11=Blissey(maxiv="Yes")
brockteam=teamset([brock1,brock2,brock3,brock4,brock5,brock7,brock8,brock9,brock10,brock11],5)+[brock6]
brock=Trainer ("Gym Leader Brock",brockteam,"Kanto")
#Marshal
marshal1=Breloom(maxiv="Yes")
marshal2=Mienshao(maxiv="Yes")
marshal3=Toxicroak(maxiv="Yes")
marshal4=Lucario(maxiv="Yes")
marshal5=Machamp(maxiv="Yes")
marshal6=Conkeldurr(maxiv="gmax")
marshal=Trainer ("Elite Four Marshal",[marshal1,marshal2,marshal3,marshal4,marshal5,marshal6],"Unova")
#shauntal
shauntal1=Cofagrigus(maxiv="Yes")
shauntal2=Jellicent(maxiv="Yes")
shauntal3=Drifblim(maxiv="Yes")
shauntal4=Golurk(maxiv="Yes")
shauntal5=Froslass(maxiv="Yes")
shauntal6=Chandelure(maxiv="gmax")
shauntal=Trainer ("Elite Four Shauntal",[shauntal1,shauntal2,shauntal3,shauntal4,shauntal5,shauntal6],"Unova")
#grimsley
grimsley1=Scrafty(maxiv="Yes")
grimsley2=Drapion(maxiv="Yes")
grimsley3=Krookodile (maxiv="Yes")
grimsley4=Houndoom(maxiv="Yes")
grimsley6=MTyranitar(maxiv="Yes")
grimsley5=Kingambit(maxiv="gmax")
grimsley=Trainer ("Elite Four Grimsley",[grimsley1,grimsley2,grimsley3,grimsley4,grimsley5,grimsley6],"Unova")
#caitlin
caitlin1=Alakazam(maxiv="Yes")
caitlin2=Gallade (maxiv="Yes")
caitlin3=Reuniclus (maxiv="Yes")
caitlin4=Metagross (maxiv="Yes")
caitlin5=Bronzong (maxiv="Yes")
caitlin6=Gothitelle (maxiv="gmax")
caitlin=Trainer ("Elite Four Caitlin",[caitlin1,caitlin2,caitlin3,caitlin4,caitlin5,caitlin6],"Unova")
#sawyer
sawyer1=Slurpuff(maxiv="Yes")
sawyer2=Clawitzer (maxiv="Yes")
sawyer3=Aegislash (maxiv="Yes")
sawyer4=Slaking(maxiv="Yes")
sawyer5=Salamence(maxiv="gmax")
sawyer6=MSceptile (maxiv="Yes")
sawyer=Trainer ("Pokémon Trainer Sawyer",[sawyer1,sawyer2,sawyer3,sawyer4,sawyer5,sawyer6],"Kalos")
#alder
alder1=Escavalier(maxiv="Yes")
alder2=Conkeldurr(maxiv="Yes")
alder3=Krookodile (maxiv="Yes")
alder4=Bouffalant (maxiv="Yes")
alder5=Braviary (maxiv="Yes")
alder6=Volcarona (maxiv="gmax")
alder=Trainer ("Unova Champion Alder",[alder1,alder2,alder3,alder4,alder5,alder6],"Unova")
#barry
barry1=Roserade(maxiv="Yes")
barry2=Staraptor(maxiv="Yes")
barry3=Hitmonlee(maxiv="Yes")
barry4=MHeracross(maxiv="Yes")
barry5=Skarmory(maxiv="Yes")
barry6=Empoleon(maxiv="gmax")
barry7=Snorlax(name="Snorlax(Z-Crystal)",move=["Giga Impact","Rest","Heavy Slam","Ice Punch"],maxiv="Yes")
barry8=Rapidash(maxiv="Yes")
barry9=Floatzel(maxiv="Yes")
barryteam=teamset([barry1,barry2,barry3,barry4,barry5,barry7,barry8,barry9],5)+[barry6]
barry=Trainer ("Pokémon Trainer Barry",barryteam,"Sinnoh")
#wally
wally1=Roserade(maxiv="Yes")
wally2=Azumarill (maxiv="Yes")
wally3=Garchomp(maxiv="Yes")
wally4=Magnezone(maxiv="Yes")
wally5=Altaria(maxiv="Yes")
wally6=MGallade(maxiv="Yes")
wally7=Talonflame (maxiv="Yes")
wally8=Gardevoir(maxiv="Yes")
wally9=Delcatty(maxiv="Yes")
wallyteam=teamset([wally1,wally2,wally3,wally4,wally5,wally7,wally8,wally9],5)+[wally6]
wally=Trainer ("Pokémon Trainer Wally",wallyteam,"Hoenn")
#paul
paul1=Honchkrow(maxiv="Yes")
paul2=Weavile(maxiv="Yes")
paul3=Gyarados (maxiv="Yes")
paul4=Garchomp (maxiv="Yes")
paul5=Metagross(maxiv="Yes")
paul6=Electivire(maxiv="gmax")
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
trevor1=Florges(maxiv="gmax")
trevor2=Aerodactyl(maxiv="Yes")
trevor3=Crawdaunt(maxiv="Yes")
trevor4=Aurorus(maxiv="Yes")
trevor5=Tyrantrum(maxiv="Yes")
trevor6=MCharizardY(maxiv="Yes")
trevor7=Raichu(maxiv="Yes")
trevor8=Aerodactyl (maxiv="Yes")
trevor9=Tyrantrum (maxiv="Yes")
trevorteam=teamset([trevor1,trevor2,trevor3,trevor4,trevor5,trevor7,trevor8,trevor9],5)+[trevor6]
trevor=Trainer ("Pokémon Trainer Trevor",trevorteam,"Kalos")
#shauna
shauna1=Delcatty (maxiv="Yes")
shauna2=Goodra(maxiv="Yes")
shauna3=Florges(maxiv="Yes")
shauna4=Slurpuff(maxiv="Yes")
shauna5=Gothitelle (maxiv="Yes")
shauna6=MVenusaur(maxiv="Yes")
shauna7=Sylveon(maxiv="Yes")
shauna8=Delphox(maxiv="Yes")
shauna9=Greninja(maxiv="Yes")
shauna10=Chesnaught (maxiv="Yes")
shaunateam=teamset([shauna1,shauna2,shauna3,shauna4,shauna5,shauna7],4)+teamset([shauna8,shauna9,shauna10],1)+[shauna6]
shauna=Trainer("Pokémon Trainer Shauna",shaunateam,"Kalos")
#hop
hopa="Yes"
hopb="Yes"
hopr=random.randint(1,2)
if hopr==1:
    hopa="gmax"
if hopr==2:
    hopb="gmax"
hop1=Trevenant(maxiv="Yes")
hop2=Boltund(maxiv="Yes")
hop3=Heatmor(maxiv="Yes")
hop4=Snorlax(maxiv="Yes")
hop5=Dubwool(maxiv="Yes")
hop6=Zacian(maxiv="Yes")
hop7=Zamazenta(maxiv="Yes")
hop8=Inteleon(maxiv=hopa)
hop9=Cinderace(maxiv=hopa)
hop10=Rillaboom(maxiv=hopa)
hop11=Corviknight(maxiv=hopb)
hop12=Toxtricity(maxiv="Yes")
hop13=Pincurchin (maxiv="Yes")
hopteam=teamset([hop1,hop2,hop3,hop4,hop5,hop11,hop12,hop13],4)+teamset([hop8,hop9,hop10],1)+teamset([hop6,hop7],1)
hop=Trainer("Pokémon Trainer Hop",hopteam,"Galar")
#tierno
tierno1=Crawdaunt (maxiv="Yes")
tierno2=Hitmontop(maxiv="Yes")
tierno3=Raichu(maxiv="Yes")
tierno4=Ludicolo(maxiv="Yes")
tierno5=Politoed (maxiv="Yes")
tierno6=MBlastoise(maxiv="Yes")
tierno7=Hawlucha(maxiv="Yes")
tierno8=Roserade(maxiv="Yes")
tierno9=Talonflame (maxiv="Yes")
tiernoteam=teamset([tierno1,tierno2,tierno3,tierno4,tierno5,tierno7,tierno8, tierno9],5)+[tierno6]
tierno=Trainer("Pokémon Trainer Tierno",tiernoteam,"Kalos")
#hau
hau1=Noivern (maxiv="Yes")
hau2=Crabominable (maxiv="Yes")
hau3=Tauros(maxiv="Yes")
#hau4=Komala(maxiv="Yes")
hau5=ARaichu(maxiv="Yes")
hau6=Decidueye(maxiv="Yes")
hau7=Vaporeon (maxiv="Yes")
hauteam=teamset([hau1,hau2,hau3,hau7],4)+[hau5,hau6]
hau=Trainer("Pokémon Trainer Hau",hauteam,"Alola")
#hala
hala1=Kommo(maxiv="Yes")
hala2=Bewear(maxiv="Yes")
hala3=Primeape(maxiv="Yes")
hala4=Poliwrath(maxiv="Yes")
hala5=Machamp(maxiv="gmax")
hala6=Hariyama(name="Hariyama(Z-Crystal)",maxiv="Yes")
hala=Trainer ("Elite Four Hala",[hala1,hala2,hala3,hala4,hala5,hala6],"Alola")
#molayne
molayne1=Skarmory(maxiv="Yes")
molayne2=Magnezone(maxiv="Yes")
molayne3=Metagross(maxiv="Yes")
molayne4=Klefki(maxiv="Yes")
molayne5=Kingambit(maxiv="gmax")
molayne6=Steelix(maxiv="Yes")
molayne7=Genesect(maxiv="Yes")
molayne8=ADugtrio(name="Alolan Dugtrio(Z-Crystal)",maxiv="Yes")
molayneteam=teamset([molayne1,molayne2,molayne3,molayne4,molayne5,molayne7,molayne6],5)+[molayne8]
molayne=Trainer ("Elite Four Molayne", molayneteam,"Alola")
#olivia
olivia1=Relicanth(maxiv="Yes")
olivia2=Gigalith(maxiv="gmax")
olivia3=AGolem(maxiv="Yes")
olivia4=Armaldo(maxiv="Yes")
olivia5=Cradily(maxiv="Yes")
olivia6=MNLycanroc(name="Midnight Lycanroc(Z-Crystal)",maxiv="Yes")
olivia=Trainer ("Elite Four Olivia",[olivia1,olivia2,olivia3,olivia4,olivia5,olivia6],"Alola")
#acerola
acerola1=Froslass(maxiv="Yes")
acerola2=Palossand(maxiv="gmax")
acerola3=Drifblim(maxiv="Yes")
acerola4=Dhelmise (maxiv="Yes")
acerola5=Banette (maxiv="Yes")
acerola6=Mimikyu(name="Mimikyu(Z-Crystal)",maxiv="Yes")
acerola=Trainer ("Elite Four Acerola",[acerola1,acerola2,acerola3,acerola4,acerola5,acerola6],"Alola")
#kahili
kahili1=Skarmory (maxiv="Yes")
kahili2=Crobat(maxiv="Yes")
kahili3=Mandibuzz(maxiv="Yes")
kahili4=Hawlucha (maxiv="Yes")
kahili5=Braviary (maxiv="gmax")
kahili6=Toucannon(name="Toucannon(Z-Crystal)",maxiv="Yes")
kahili=Trainer ("Elite Four Kahili",[kahili1,kahili2,kahili3,kahili4,kahili5,kahili6],"Alola")
#odrake
odrake1=Ditto(maxiv="Yes")
odrake2=Gengar(maxiv="gmax")
odrake3=MVenusaur(maxiv="Yes")
odrake4=Steelix(maxiv="Yes")
odrake5=Electivire(maxiv="Yes")
odrake6=Dragonite(maxiv="Yes")
odrake=Trainer ("Supreme Gym Leader Drake",[odrake1,odrake2,odrake3,odrake4,odrake5,odrake6],"Orange Islands")
#Leon
gmaxleon=random.randint(1,2)
chmax="Yes"
cimax="Yes"
if gmaxleon==1:
    chmax="gmax"
    cimax="Yes"
if gmaxleon==2:
    chmax="Yes"
    cimax="gmax"    
leon1=MrRime(maxiv="Yes")
leon2=Aegislash(maxiv="Yes")
leon3=Dragapult (maxiv="Yes")
leon4=Inteleon(maxiv="Yes")
leon5=Rillaboom(maxiv="Yes",move=["Drum Beating","Acrobatics","High Horsepower","Knock Off"])
leon6=Cinderace(maxiv=cimax,ability="Libero",move=["Scorching Sands","Pyro Ball","Sucker Punch","Grass Knot"])
leon7=Charizard (maxiv=chmax,move=["Flamethrower","Ancient Power","Air Slash","Dragon Pulse"],atkev=0,spatkev=252,dmax=True)
leon8=Seismitoad(maxiv="Yes")
leon9=Rhyperior(maxiv="Yes")
leon10=Eternatus (maxiv="Yes")
leonteam=teamset([leon1,leon2,leon3,leon4,leon5,leon6,leon8,leon9,leon10],5)+[leon7]
leon=Trainer("Galar Champion Leon", leonteam,"Galar")
#Benga
benga1=Emboar(maxiv="Yes")
benga2=Dragonite (maxiv="Yes")
benga3=Garchomp (maxiv="Yes")
benga4=Latias (maxiv="Yes")
benga5=Latios (maxiv="Yes")
benga6=Volcarona(maxiv="gmax")
benga=Trainer ("Pokémon Trainer Benga",[benga1,benga2,benga3,benga4,benga5,benga6],"Unova")
#misty
misty1=Seaking(maxiv="Yes",ability="Lightning Rod")
misty2=Starmie(maxiv="gmax")
misty3=Politoed(maxiv="Yes", ability="Drizzle")
misty4=Kingdra(maxiv="Yes")
misty5=Lapras(maxiv="Yes")
misty6=MGyarados(maxiv="Yes")
misty7=Quagsire(maxiv="Yes")
misty8=Lanturn(maxiv="Yes")
misty9=Milotic(maxiv="Yes")
misty10=Jellicent(maxiv="Yes")
misty11=Blastoise(maxiv="Yes")
misty12=Golduck(name="Golduck(Z-Crystal)",maxiv="Yes")
misty13=Swanna(maxiv="Yes")
misty14=Carracosta(maxiv="Yes")
misty15=Dewgong (maxiv="Yes")
misty16=Vaporeon (maxiv="Yes")
misty17=Slowbro(maxiv="Yes")
misty18=Manaphy (maxiv="Yes")
mistyteam=teamset([misty1,misty4,misty5,misty7,misty8,misty9,misty10,misty11,misty12,misty13,misty14,misty15,misty16,misty17,misty18],3)+[misty3,misty2,misty6]
misty=Trainer ("Gym Leader Misty",mistyteam,"Kanto")
#surge
surge1=Ampharos(maxiv="Yes")
surge2=Jolteon(maxiv="Yes")
surge3=Magnezone(maxiv="Yes")
surge4=Electivire(maxiv="Yes")
surge5=Electrode(maxiv="Yes")
surge6=Raichu(maxiv="gmax")
surge7=MManectric(maxiv="Yes")
surge8=Lanturn(maxiv="Yes")
surge9=Zapdos(name="Zapdos(Z-Crystal)",maxiv="Yes")
surgeteam=teamset([surge1,surge2,surge3,surge4,surge5,surge7,surge8,surge9],5)+[surge6]
surge=Trainer ("Gym Leader Lt.Surge",surgeteam,"Kanto")
#erika
erika1=Jumpluff(maxiv="Yes")
erika2=Bellossom(name="Bellossom(Z-Crystal)",maxiv="Yes")
erika3=Tangrowth(maxiv="Yes")
erika4=Victreebel(maxiv="Yes")
erika5=Vileplume(maxiv="gmax")
erika6=MVenusaur(maxiv="Yes")
erika7=Shiftry(maxiv="Yes")
erika8=Roserade(maxiv="Yes")
erika9=Exeggutor(maxiv="Yes")
erika10=Cradily(maxiv="Yes")
erika11=Abomasnow(maxiv="Yes")
erika12=Parasect(maxiv="Yes")
erika13=Leafeon(maxiv="Yes")
erika14=Shaymin(maxiv="Yes")
erikateam=teamset([erika1,erika2,erika3,erika4,erika7,erika8,erika9,erika10,erika11,erika12,erika13,erika14],4)+[erika5,erika6]
erika=Trainer ("Gym Leader Erika",erikateam,"Kanto")
#sabrina
sabrina1=Venomoth(maxiv="Yes")
sabrina2=MrMime(maxiv="Yes")
sabrina3=Espeon(maxiv="gmax")
sabrina4=Jynx(maxiv="Yes")
sabrina5=Wobbuffet(maxiv="Yes")
sabrina6=MAlakazam(maxiv="Yes")
sabrina7=Gallade(maxiv="Yes")
sabrina8=Lanturn(maxiv="Yes")
sabrina9=Slowking (maxiv="Yes")
sabrina10=Hypno(maxiv="Yes")
sabrina11=Metagross (maxiv="Yes")
sabrina12=Exeggutor(maxiv="Yes")
sabrina13=Mewtwo(maxiv="Yes")
sabrinateam=teamset([sabrina1,sabrina2,sabrina3,sabrina4,sabrina5,sabrina7,sabrina8,sabrina9,sabrina10,sabrina11,sabrina12,sabrina13],5)+[sabrina6]
sabrina=Trainer ("Gym Leader Sabrina",sabrinateam,"Kanto")
#koga
koga1=Ariados(maxiv="Yes")
koga2=Venomoth(maxiv="Yes")
koga3=Crobat(name="Crobat(Z-Crystal)",maxiv="Yes")
koga4=Weezing(maxiv="Yes")
koga5=Skuntank(maxiv="Yes")
koga6=Muk(maxiv="gmax")
koga7=Toxicroak(maxiv="Yes")
koga8=Forretress(maxiv="Yes")
koga9=Tentacruel (maxiv="Yes")
koga10=Naganadel(maxiv="Yes")
kogateam=teamset([koga1,koga2,koga3,koga4,koga5,koga7,koga8,koga9,koga10],5)+[koga6]
koga=Trainer ("Elite Four Koga",kogateam,"Kanto")
#blaine
blaine1=Arcanine(maxiv="gmax")
blaine2=Ninetales(maxiv="Yes")
blaine3=Rapidash(maxiv="Yes")
blaine4=Magcargo(maxiv="Yes")
blaine6=Magmortar(maxiv="Yes")
blaine7=Torkoal(maxiv="Yes")
blaine8=Camerupt(maxiv="Yes")
blaine9=Houndoom(maxiv="Yes")
blaine10=MCharizardY(maxiv="Yes")
blaine11=Flareon(maxiv="Yes")
blaine12=Moltres(name="Moltres(Z-Crystal)",maxiv="Yes")
blaineteam=teamset([blaine2,blaine3,blaine4,blaine7,blaine8,blaine9,blaine10,blaine11,blaine12],4)+[blaine6,blaine1]
blaine=Trainer ("Gym Leader Blaine",blaineteam,"Kanto")
#bugsy
bugsy1=Butterfree(maxiv="Yes")
bugsy2=Yanmega(maxiv="Yes")
bugsy3=Pinsir(maxiv="Yes")
bugsy4=Vespiquen(maxiv="Yes")
bugsy5=Heracross(name="Heracross(Z-Crystal)",maxiv="Yes")
bugsy6=MBeedrill(maxiv="Yes")
bugsy7=Scizor(maxiv="gmax")
bugsy8=Shuckle(maxiv="Yes")
bugsy9=Forretress(maxiv="Yes")
bugsy10=Armaldo(maxiv="Yes")
bugsyteam=teamset([bugsy1,bugsy2,bugsy3,bugsy4,bugsy5,bugsy9,bugsy8,bugsy10],4)+[bugsy7,bugsy6]
bugsy=Trainer ("Gym Leader Bugsy",bugsyteam,"Johto")
#whitney
whitney1=Ursaluna(maxiv="Yes")
whitney2=Tauros(maxiv="Yes")
whitney3=Ambipom(maxiv="Yes")
whitney4=Wigglytuff(maxiv="Yes")
whitney5=Farigiraf(maxiv="Yes")
whitney6=Miltank(maxiv="gmax")
whitney7=Clefable(name="Clefable(Z-Crystal)",maxiv="Yes")
whitney8=Blissey(maxiv="Yes")
whitney9=MLopunny(maxiv="Yes")
whitneyteam=teamset([whitney1,whitney2,whitney3,whitney4,whitney5,whitney8,whitney7],4)+[whitney6,whitney9]
whitney=Trainer ("Gym Leader Whitney",whitneyteam,"Johto")
#morty
morty1=Drifblim(maxiv="Yes")
morty2=Mismagius(name="Mismagius(Z-Crystal)",maxiv="gmax")
morty3=Dusknoir(maxiv="Yes")
morty4=Banette(maxiv="Yes")
morty5=Froslass(maxiv="Yes")
morty6=Cofagrigus(maxiv="Yes")
morty7=Clefable(maxiv="Yes")
morty8=Jellicent(maxiv="Yes")
morty9=MGengar(maxiv="Yes")
mortyteam=teamset([morty1,morty6,morty3,morty4,morty5,morty8,morty7],4)+[morty2,morty9]
morty=Trainer ("Gym Leader Morty",mortyteam,"Johto")
#will
will1=Exeggutor(maxiv="Yes")
will2=Jynx(maxiv="Yes")
will3=Bronzong(maxiv="Yes")
will4=Grumpig(maxiv="Yes")
will5=Xatu(maxiv="gmax")
will6=MSlowbro(maxiv="Yes")
will7=Gardevoir(maxiv="Yes")
will8=MGardevoir(maxiv="Yes")
willteam=teamset([will1,will2,will3,will4],4)+[will5]+teamset([will6,will8],1)
will=Trainer ("Elite Four Will",willteam,"Johto")
#chuck
chuck1=Primeape(maxiv="Yes")
chuck2=Poliwrath(maxiv="gmax")
chuck3=Medicham(maxiv="Yes")
chuck4=Breloom(maxiv="Yes")
chuck5=Hitmonchan(maxiv="Yes")
chuck6=Hitmonlee(maxiv="Yes")
chuck7=Machamp(maxiv="Yes")
chuck8=Hitmontop(maxiv="Yes")
chuck9=Conkeldurr(maxiv="Yes")
chuckteam=teamset([chuck1,chuck2,chuck3,chuck4,chuck5,chuck6,chuck7,chuck8,chuck9],6)
chuck=Trainer ("Gym Leader Chuck",chuckteam,"Johto")
#jasmine
jasmine1=Skarmory(maxiv="Yes")
jasmine2=Empoleon(maxiv="gmax")
jasmine3=Metagross(maxiv="Yes")
jasmine4=Bronzong(maxiv="Yes")
jasmine5=Magnezone(maxiv="Yes")
jasmine6=MSteelix(maxiv="Yes")
jasmine7=Mawile(maxiv="Yes")
jasmine8=Lucario(maxiv="Yes")
jasmine9=Ferrothorn(maxiv="Yes")
jasmine10=Excadrill(maxiv="Yes")
jasmine11=Forretress(maxiv="Yes")
jasmineteam=teamset([jasmine1,jasmine2,jasmine3,jasmine4,jasmine5,jasmine7,jasmine8,jasmine9,jasmine10,jasmine11],5)+[jasmine6]
jasmine=Trainer ("Gym Leader Jasmine",jasmineteam,"Johto")
#pryce
pryce1=Walrein(maxiv="Yes")
pryce2=Froslass(maxiv="Yes")
pryce3=Glalie(maxiv="Yes")
pryce4=MAbomasnow(maxiv="Yes")
pryce5=Dewgong(maxiv="Yes")
pryce6=Mamoswine(maxiv="gmax")
pryce7=Jynx(maxiv="Yes")
pryce8=Lapras(maxiv="Yes")
pryce9=Weavile(maxiv="Yes")
pryce10=Cloyster(maxiv="Yes")
pryceteam=teamset([pryce1,pryce2,pryce3,pryce4,pryce5,pryce6,pryce7,pryce8,pryce9,pryce10],6)
pryce=Trainer ("Gym Leader Pryce",pryceteam,"Johto")
#claire
claire2=Aerodactyl(maxiv="Yes")
claire3=Charizard(maxiv="Yes")
claire4=Gyarados(maxiv="Yes")
claire5=Dragonite(maxiv="Yes")
claire6=Kingdra(maxiv="gmax")
claire7=Altaria(maxiv="Yes")
claire8=Salamence(maxiv="Yes")
claire9=Druddigon(maxiv="Yes")
claire1=Garchomp(maxiv="Yes")
claireteam=teamset([claire1,claire2,claire3,claire4,claire5,claire6,claire7,claire8,claire9],6)
claire=Trainer ("Gym Leader Claire",claireteam,"Johto")
#roxanne
roxanne2=Aerodactyl(maxiv="Yes")
roxanne3=Kabutops(maxiv="Yes")
roxanne4=Omastar(maxiv="Yes")
roxanne5=Golem(maxiv="Yes")
roxanne6=Steelix(maxiv="Yes")
roxanne7=Probopass(maxiv="gmax")
roxanne8=Cradily(maxiv="Yes")
roxanne9=Armaldo(maxiv="Yes")
roxanne1=Aggron(maxiv="Yes")
roxanne10=Relicanth(maxiv="Yes")
roxanne11=Carracosta(maxiv="Yes")
roxanneteam=teamset([roxanne1,roxanne2,roxanne3,roxanne4,roxanne5,roxanne6,roxanne7,roxanne8,roxanne9,roxanne10,roxanne11],6)
roxanne=Trainer ("Gym Leader Roxanne",roxanneteam,"Hoenn")
#brawly
brawly2=Medicham(maxiv="Yes")
brawly3=Machamp(maxiv="Yes")
brawly4=Hitmonchan(maxiv="Yes")
brawly5=Hitmontop(maxiv="Yes")
brawly6=Hariyama(maxiv="gmax")
brawly7=Hitmonlee(maxiv="Yes")
brawly8=Breloom(maxiv="Yes")
brawly9=Heracross(maxiv="Yes")
brawly1=Scrafty(maxiv="Yes")
brawly10=Mienshao(maxiv="Yes")
brawlyteam=teamset([brawly1,brawly2,brawly3,brawly4,brawly5,brawly7,brawly8,brawly9,brawly10],5)+[brawly6]
brawly=Trainer ("Gym Leader Brawly",brawlyteam,"Hoenn")
#winona
winona2=Tropius(maxiv="Yes")
winona3=Skarmory(maxiv="Yes")
winona4=Pelipper(maxiv="Yes")
winona5=Swellow(maxiv="Yes")
winona6=MAltaria(maxiv="Yes")
winona7=Noctowl(maxiv="Yes")
winona1=Dragonite(maxiv="gmax")
winona8=Honchkrow(maxiv="Yes")
winona9=Gyarados(maxiv="Yes")
winona10=Rayquaza(maxiv="Yes")
winonateam=teamset([winona1,winona2,winona3,winona4,winona5,winona7,winona8,winona9,winona10],5)+[winona6]
winona=Trainer ("Gym Leader Winona",winonateam,"Hoenn")
#wattson
wattson2=Electivire(maxiv="Yes")
wattson3=Electrode(maxiv="Yes")
wattson4=Raichu(maxiv="Yes")
wattson5=Ampharos(maxiv="gmax")
wattson6=MManectric(maxiv="Yes")
wattson7=Magnezone(maxiv="Yes")
wattson1=WRotom(maxiv="Yes")
wattsonteam=teamset([wattson1,wattson2,wattson3,wattson4,wattson5,wattson7],5)+[wattson6]
wattson=Trainer ("Gym Leader Wattson",wattsonteam,"Hoenn")
#flannery
flannery2=Torkoal(maxiv="Yes")
flannery3=Houndoom(maxiv="Yes")
flannery4=Rapidash(maxiv="Yes")
flannery5=Magcargo(maxiv="Yes")
flannery6=MCamerupt(maxiv="Yes")
flannery7=Blaziken(maxiv="gmax")
flannery1=Magmortar(maxiv="Yes")
flannery8=Chandelure(maxiv="Yes")
flanneryteam=teamset([flannery1,flannery2,flannery3,flannery4,flannery5,flannery6,flannery7,flannery8],6)
flannery=Trainer ("Gym Leader Flannery",flanneryteam,"Hoenn")
#norman
norman2=Tauros(maxiv="Yes")
norman3=Kangaskhan(maxiv="Yes")
norman4=Linoone(maxiv="Yes")
norman5=Zangoose(maxiv="Yes")
norman6=Slaking(maxiv="gmax")
norman7=Exploud(maxiv="Yes")
norman1=Blissey(maxiv="Yes")
norman8=Staraptor(maxiv="Yes")
norman9=Ambipom(maxiv="Yes")
norman10=Bouffalant (maxiv="Yes")
norman11=Stoutland(maxiv="Yes")
normanteam=teamset([norman1,norman2,norman3,norman4,norman5,norman7,norman8,norman9,norman10,norman11],5)+[norman6]
norman=Trainer ("Gym Leader Norman",normanteam,"Hoenn")
#tate
tate2=Bronzong (maxiv="Yes")
tate3=Claydol(maxiv="Yes")
tate4=Grumpig(maxiv="Yes")
tate5=Xatu(maxiv="Yes")
tate6=Solrock(maxiv="gmax")
tate1=Reuniclus(maxiv="Yes")
tate7=MGallade(maxiv="Yes")
tateteam=teamset([tate1,tate2,tate3,tate4,tate5,tate7],5)+[tate6]
tate=Trainer ("Gym Leader Tate",tateteam,"Hoenn")
#liza
liza2=Bronzong(maxiv="Yes")
liza3=Claydol(maxiv="Yes")
liza4=Grumpig(maxiv="Yes")
liza5=Xatu(maxiv="Yes")
liza6=Lunatone(maxiv="gmax")
liza1=Gothitelle(maxiv="Yes")
liza7=MGardevoir(maxiv="Yes")
lizateam=teamset([liza1,liza2,liza3,liza4,liza5,liza7],5)+[liza6]
liza=Trainer ("Gym Leader Liza",lizateam,"Hoenn")
#juan
juan2=Whiscash(maxiv="Yes")
juan3=Crawdaunt(maxiv="Yes")
juan4=Walrein(maxiv="Yes")
juan5=Politoed(maxiv="Yes")
juan6=Kingdra(maxiv="gmax")
juan1=Lapras(maxiv="Yes")
juan7=Huntail(maxiv="Yes")
juan8=Gorebyss(maxiv="Yes")
juan9=Relicanth(maxiv="Yes")
juanteam=teamset([juan1,juan2,juan3,juan4,juan5,juan7,juan8,juan9],5)+[juan6]
juan=Trainer ("Gym Leader Juan",juanteam,"Hoenn")
#roark
roark1=Armaldo (maxiv="Yes")
roark2=Aerodactyl (maxiv="Yes")
roark3=Probopass(maxiv="Yes")
roark4=Relicanth (maxiv="Yes")
roark5=Rampardos(maxiv="gmax")
roark6=Tyranitar(maxiv="Yes")
roark7=Golem(maxiv="Yes")
roark8=Archeops(maxiv="Yes")
roark9=Sudowoodo(maxiv="Yes")
roark10=Salamence(maxiv="Yes")
roark11=Lunatone(maxiv="Yes")
roark12=Torkoal(maxiv="Yes")
roark13=Slowbro(maxiv="Yes")
roark14=Torkoal(maxiv="Yes")
roarkteam=teamset([roark1,roark2,roark3,roark4,roark7,roark8,roark9,roark10,roark11,roark12,roark13,roark14],4)+[roark6,roark5]
roark=Trainer("Gym Leader Roark",roarkteam,"Sinnoh")
#gardenia
gardenia1=Jumpluff(maxiv="Yes")
gardenia2=Roserade(maxiv="Yes")
gardenia3=Bellossom(maxiv="Yes")
gardenia4=Cherrim(maxiv="Yes")
gardenia5=Tangrowth(maxiv="Yes")
gardenia6=Torterra(maxiv="gmax")
gardenia7=Leafeon(maxiv="Yes")
gardenia8=Tropius(maxiv="Yes")
gardenia9=Breloom(maxiv="Yes")
gardenia10=Sunflora(maxiv="Yes")
gardenia11=Venusaur(maxiv="Yes",ability="Chlorophyll")
gardenia12=Cradily(maxiv="Yes")
gardenia13=Milotic(maxiv="Yes")
gardenia14=Ninetales(maxiv="Yes",ability="Drought",item="Heat Rock")
gardenia15=MRotom(maxiv="Yes")
gardeniateam=teamset([gardenia1,gardenia5,gardenia3,gardenia4,gardenia7,gardenia8,gardenia9,gardenia10,gardenia11,gardenia12,gardenia13,gardenia14, gardenia15],4)+[gardenia2,gardenia6]
gardenia=Trainer("Gym Leader Gardenia",gardeniateam,"Sinnoh")
#fantina
fantina1=Banette(maxiv="Yes")
fantina2=Drifblim(maxiv="Yes")
fantina3=Dusknoir(maxiv="Yes")
fantina4=MGengar(maxiv="Yes")
fantina5=Spiritomb(maxiv="Yes")
fantina6=Mismagius(maxiv="gmax")
fantina7=Jellicent(maxiv="Yes")
fantina8=OGiratina(maxiv="Yes")
fantina9=Froslass(maxiv="Yes")
fantina10=Shedinja(maxiv="Yes")
fantinateam=teamset([fantina1,fantina5,fantina3,fantina4,fantina7,fantina8,fantina9,fantina10],4)+[fantina2,fantina6]
fantina=Trainer("Gym Leader Fantina",fantinateam,"Sinnoh")
#byron
byron1=Aggron(maxiv="Yes")
byron2=Skarmory(maxiv="Yes")
byron3=Magnezone(maxiv="Yes")
byron4=Bronzong (maxiv="Yes")
byron5=MSteelix(maxiv="Yes")
byron6=Bastiodon(maxiv="gmax")
byron7=Excadrill(maxiv="Yes")
byron8=Empoleon (maxiv="Yes")
byron9=Metagross(maxiv="Yes")
byron10=Scizor(maxiv="Yes")
byron11=Kabutops(maxiv="Yes")
byron12=Cradily(maxiv="Yes")
byron13=Armaldo(maxiv="Yes")
byron14=Omastar(maxiv="Yes")
byron15=Heatran(maxiv="Yes")
byronteam=teamset([byron1,byron2,byron3,byron4,byron7,byron8,byron9,byron10,byron11,byron12,byron13,byron14,byron15],4)+[byron5,byron6]
byron=Trainer("Gym Leader Byron",byronteam,"Sinnoh")
#maylene
maylene1=Infernape(maxiv="gmax")
maylene2=Breloom(maxiv="Yes")
maylene3=Hitmontop(maxiv="Yes")
maylene4=Machamp(maxiv="Yes")
maylene5=Medicham(maxiv="Yes")
maylene6=MLucario(maxiv="Yes")
maylene7=Gallade(maxiv="Yes")
maylene8=Toxicroak(maxiv="Yes")
maylene9=Heracross(maxiv="Yes")
maylene10=Blaziken(maxiv="Yes")
maylene11=Empoleon(maxiv="Yes")
maylene12=Dragonite (maxiv="Yes")
mayleneteam=teamset([maylene5,maylene2,maylene3,maylene4,maylene7,maylene8,maylene9,maylene10, maylene11,maylene12],4)+[maylene1,maylene6]
maylene=Trainer("Gym Leader Maylene",mayleneteam,"Sinnoh")
#wake
wake1=Floatzel(maxiv="gmax")
wake2=Quagsire(maxiv="Yes")
wake3=Sharpedo(maxiv="Yes")
wake4=Ludicolo(maxiv="Yes")
wake5=Empoleon(maxiv="Yes")
wake6=MGyarados(maxiv="Yes")
wake7=Lumineon(maxiv="Yes")
wake8=WGastrodon(maxiv="Yes")
wake9=Poliwrath(maxiv="Yes")
wake10=Kingdra(maxiv="Yes")
wake11=Politoed(maxiv="Yes")
wake12=Huntail(maxiv="Yes")
wake13=Suicune(maxiv="Yes")
wake14=Swampert (maxiv="Yes")
wake15=Armaldo(maxiv="Yes")
wake16=Pelipper(maxiv="Yes", ability="Drizzle",item="Damp Rock")
wake17=Scizor (maxiv="Yes")
waketeam=teamset([wake5,wake2,wake3,wake4,wake7,wake8,wake9,wake10,wake11,wake12,wake13,wake14,wake15,wake16    ],4)+[wake1,wake6]
wake=Trainer("Gym Leader Crasher Wake",waketeam,"Sinnoh")
#candice
candice1=Froslass(maxiv="gmax")
candice2=Weavile(maxiv="Yes")
candice3=Mamoswine(maxiv="Yes")
candice4=Glaceon(maxiv="Yes")
candice5=Glalie(maxiv="Yes")
candice6=MAbomasnow(maxiv="Yes")
candice7=Medicham(maxiv="Yes")
candice8=Jynx(maxiv="Yes")
candice9=Regice(maxiv="Yes")
candice10=Lapras(maxiv="Yes")
candice11=Cloyster(maxiv="Yes")
candice12=Articuno(maxiv="Yes")
candiceteam=teamset([candice5,candice2,candice3,candice4,candice7,candice8,candice9,candice10,candice11,candice12],4)+[candice1,candice6]
candice=Trainer("Gym Leader Candice",candiceteam,"Sinnoh")
#volkner
volkner1=Luxray(maxiv="Yes")
volkner2=Raichu(maxiv="Yes")
volkner3=Ambipom(maxiv="Yes")
volkner4=Octillery(maxiv="Yes")
volkner5=Jolteon(maxiv="Yes")
volkner6=Electivire(maxiv="gmax")
volkner7=Lanturn(maxiv="Yes")
volkner8=Electrode(maxiv="Yes")
volkner9=Eelektross(maxiv="Yes")
volkner10=Galvantula(maxiv="Yes")
volkner11=Zebstrika(maxiv="Yes")
volkner12=Pelipper(maxiv="Yes")
volkner13=Magnezone(maxiv="Yes")
volkner14=Zapdos(maxiv="Yes")
volknerteam=teamset([volkner5,volkner2,volkner3,volkner4,volkner7,volkner8,volkner9,volkner10,volkner11,volkner12,volkner13,volkner14],4)+[volkner1,volkner6]
volkner=Trainer("Gym Leader Volkner",volknerteam,"Sinnoh")
#lenora
lenora1=Watchog(maxiv="gmax")
lenora2=Stoutland(maxiv="Yes")
lenora3=Kangaskhan(maxiv="Yes")
lenora4=Clefable(maxiv="Yes")
lenora5=Lickilicky(maxiv="Yes")
lenora6=Braviary(maxiv="Yes")
lenorateam=teamset([lenora5,lenora2,lenora3,lenora4],4)+[lenora6,lenora1]
lenora=Trainer("Gym Leader Lenora",lenorateam,"Unova")
#burgh
burgh1=Scolipede(maxiv="Yes")
burgh2=Vespiquen(maxiv="Yes")
burgh3=Escavalier(maxiv="Yes")
burgh4=Accelgor(maxiv="Yes")
burgh5=Durant(maxiv="Yes")
burgh6=Leavanny(maxiv="gmax")
burgh7=Heracross(maxiv="Yes")
burghteam=teamset([burgh5,burgh2,burgh3,burgh4,burgh7],4)+[burgh1,burgh6]
burgh=Trainer("Gym Leader Burgh",burghteam,"Unova")
#elesa
elesa1=MAmpharos(maxiv="Yes")
elesa2=Galvantula(maxiv="Yes")
elesa3=Eelektross(maxiv="Yes")
elesa4=Luxray(maxiv="Yes")
elesa5=Vikavolt(maxiv="Yes")
elesa6=Zebstrika(maxiv="gmax")
elesa7=Manectric(maxiv="Yes")
elesa8=Emolga(maxiv="Yes")
elesateam=teamset([elesa1,elesa5,elesa2,elesa3,elesa4,elesa7],4)+[elesa8,elesa6]
elesa=Trainer("Gym Leader Elesa",elesateam,"Unova")
#clemont
clemont1=Manectric(maxiv="Yes")
clemont2=Luxray(maxiv="Yes")
clemont3=Emolga(maxiv="Yes")
clemont4=Magnezone(maxiv="Yes")
clemont5=MAmpharos(maxiv="Yes")
clemont6=Heliolisk(maxiv="gmax")
clemontteam=teamset([clemont2,clemont3,clemont4,clemont5,clemont1],5)+[clemont6]
clemont=Trainer ("Gym Leader Clemont",clemontteam,"Kalos")
#clay
clay1=Excadrill(maxiv="gmax")
clay2=Seismitoad(maxiv="Yes")
clay3=Sandslash(maxiv="Yes")
clay4=Claydol(maxiv="Yes")
clay5=Golurk(maxiv="Yes")
clay6=Krookodile(maxiv="Yes")
clay7=Mamoswine(maxiv="Yes")
clay8=Flygon(maxiv="Yes")
clayteam=teamset([clay5,clay2,clay3,clay4,clay7,clay8],4)+[clay6,clay1]
clay=Trainer("Gym Leader Clay",clayteam,"Unova")
#skyla
skyla1=Unfezant(maxiv="Yes")
skyla2=Braviary(maxiv="Yes")
skyla3=Skarmory(maxiv="Yes")
skyla4=Archeops(maxiv="Yes")
skyla5=Mandibuzz (maxiv="Yes")
skyla6=Swanna(maxiv="gmax")
skyla7=Jumpluff(maxiv="Yes")
skyla8=Drifblim(maxiv="Yes")
skylateam=teamset([skyla5,skyla2,skyla3,skyla4,skyla7,skyla8],4)+[skyla1,skyla6]
skyla=Trainer("Gym Leader Skyla",skylateam,"Unova")
#brycen
brycen1=Vanilluxe(maxiv="Yes")
brycen2=Weavile(maxiv="Yes")
brycen3=Dewgong (maxiv="Yes")
brycen4=Walrein(maxiv="Yes")
brycen5=Mandibuzz (maxiv="Yes")
brycen6=Beartic(maxiv="gmax")
brycen7=Kingambit(maxiv="Yes")
brycen8=Honchkrow(maxiv="Yes")
brycen9=Zoroark(maxiv="Yes")
brycen10=Scrafty(maxiv="Yes")
brycen11=Houndoom(maxiv="Yes")
brycen12=Hydreigon (maxiv="Yes")
brycen13=Sharpedo(maxiv="Yes")
brycen14=Cryogonal(maxiv="Yes")
brycenteam=teamset([brycen5,brycen2,brycen3,brycen4,brycen7,brycen8,brycen9,brycen10,brycen11,brycen12,brycen13,brycen1],4)+[brycen14,brycen6]
brycen=Trainer("Gym Leader Brycen",brycenteam,"Unova")
#drayden
drayden1=Druddigon(maxiv="Yes")
drayden2=Flygon(maxiv="Yes")
drayden3=Altaria(maxiv="Yes")
drayden4=Hydreigon (maxiv="Yes")
drayden5=Salamence(maxiv="Yes")
drayden6=Haxorus(maxiv="gmax")
draydenteam=teamset([drayden5,drayden2,drayden3,drayden4],4)+[drayden1,drayden6]
drayden=Trainer("Gym Leader Drayden",draydenteam,"Unova")
#cheren
cheren1=Unfezant(maxiv="Yes")
cheren2=Liepard(maxiv="Yes")
cheren3=Emboar(maxiv="Yes")
cheren6=Haxorus(maxiv="Yes")
cheren7=Gigalith (maxiv="Yes")
cheren8=Stoutland(maxiv="Yes")
cheren9=Watchog(maxiv="Yes")
cheren10=Zangoose (maxiv="Yes")
cheren11=Bouffalant (maxiv="Yes")
cheren12=MLopunny (maxiv="Yes")
cheren13=PorygonZ(maxiv="Yes")
cheren14=Lickilicky(maxiv="Yes")
cheren15=Kingambit(maxiv="Yes")
cheren16=Basculegion (maxiv="Yes")
cheren17=Beartic(maxiv="Yes")
cherenteam=teamset([cheren2,cheren3,cheren7,cheren8,cheren9,cheren10,cheren11,cheren12,cheren13,cheren14],4)+[cheren1,cheren6]
cheren=Trainer("Gym Leader Cheren",cherenteam,"Unova")    
#roxie
roxie1=Weezing(maxiv="Yes")
roxie2=Muk(maxiv="Yes")
roxie3=Seviper(maxiv="Yes")
roxie6=Scolipede(maxiv="gmax")
roxie4=Crobat(maxiv="Yes")
roxie5=Drapion(maxiv="Yes")
roxie7=Toxicroak(maxiv="Yes")
roxieteam=teamset([roxie2,roxie3,roxie7,roxie4,roxie5],4)+[roxie1,roxie6]
roxie=Trainer("Gym Leader Roxie",roxieteam,"Unova")    
#quillon
quillon1=Weavile(maxiv="Yes")
quillon2=Regice(maxiv="Yes")
quillon3=Regirock(maxiv="Yes")
quillon5=Registeel(maxiv="Yes")
quillon4=Rillaboom(maxiv="Yes")
quillon6=DUrshifu(maxiv="gmax")
quillonteam=teamset([quillon2,quillon3,quillon4,quillon5],4)+[quillon1,quillon6]
quillon=Trainer("Pokémon Trainer Quillon",quillonteam,"Galar")      
#marlon
marlon1=Carracosta(maxiv="gmax")
marlon2=Wailord(maxiv="Yes")
marlon3=Mantine(maxiv="Yes")
marlon6=Starmie(maxiv="Yes")
marlon4=Quagsire(maxiv="Yes")
marlon5=Cloyster(maxiv="Yes")
marlonteam=teamset([marlon2,marlon3,marlon4,marlon5],4)+[marlon1,marlon6]
marlon=Trainer("Gym Leader Marlon",marlonteam,"Unova")    
#diantha
diantha1=Goodra(maxiv="gmax")
diantha2=Hawlucha(maxiv="Yes")
diantha3=Tyrantrum(maxiv="Yes")
diantha6=MGardevoir(maxiv="Yes")
diantha4=Aurorus(maxiv="Yes")
diantha5=Gourgeist(maxiv="Yes")
dianthateam=teamset([diantha2,diantha3,diantha4,diantha5],4)+[diantha1,diantha6]
diantha=Trainer("Kalos Champion Diantha",dianthateam,"Kalos")    
#grant
grant4=Golem(maxiv="Yes")
grant2=Steelix(maxiv="Yes")
grant3=Bastiodon(maxiv="Yes")
grant6=Tyrantrum(maxiv="gmax")
grant1=Aurorus(maxiv="Yes")
grant5=Rampardos(maxiv="Yes")
grantteam=teamset([grant2,grant3,grant4,grant5],4)+[grant1,grant6]
grant=Trainer("Gym Leader Grant",grantteam,"Kalos")    
#danika
danika1=Azumarill (maxiv="Yes")
danika2=Gorebyss(maxiv="Yes")
danika3=Politoed(maxiv="Yes")
danika5=Ludicolo(maxiv="Yes")
danika4=Inteleon(maxiv="Yes")
danika6=WUrshifu(maxiv="gmax")
danikateam=teamset([danika2,danika3,danika4,danika5],4)+[danika1,danika6]
danika=Trainer("Pokémon Trainer Danika",danikateam,"Galar")    
#viola
viola1=Dustox(maxiv="Yes")
viola2=Beautifly(maxiv="Yes")
viola3=Mothim(maxiv="Yes")
viola4=Butterfree(maxiv="gmax")
viola5=Masquerain(maxiv="Yes")
viola6=Vivillon(maxiv="Yes")
violateam=teamset([viola2,viola3,viola4,viola5,viola1],5)+[viola6]
viola=Trainer ("Gym Leader Viola",violateam,"Kalos")
#ash
ash1=Infernape(maxiv="Yes")
ash2=Dragonite(maxiv="Yes")
ash3=Charizard(maxiv="Yes")
ash4=MLucario(maxiv="Yes")
ash5=Gengar(maxiv="gmax")
ash6=Pikachu(name="Pikachu(Z-Crystal)",move=["Thunderbolt","Electroweb","Extreme Speed","Iron Tail"],maxiv="Yes")
ash7=Sceptile(maxiv="Yes")
ash8=Staraptor(maxiv="Yes")
ash9=Tauros(maxiv="Yes")
ash10=Snorlax (maxiv="Yes")
ash11=Noivern(maxiv="Yes")
ash12=Goodra(maxiv="Yes")
ash13=Greninja(maxiv="Yes", ability="Battle Bond")
ash14=Noctowl(name="Noctowl✨",maxiv="Yes")
ash15=Torkoal(maxiv="Yes")
ash16=Dracovish (maxiv="Yes")
ash17=Sirfetchd(maxiv="Yes")
ash18=Muk(maxiv="Yes")
ash19=Heracross(maxiv="Yes")
ash20=Donphan(maxiv="Yes")
ash21=Swellow(maxiv="Yes")
ash22=Glalie(maxiv="Yes")
ash23=Torterra(maxiv="Yes")
ash24=Gliscor(maxiv="Yes")
ash25=Unfezant(maxiv="Yes")
ash26=Leavanny(maxiv="Yes")
ash27=Krookodile(maxiv="Yes")
ash28=Talonflame(maxiv="Yes")
ash29=Hawlucha(maxiv="Yes")
ash30=Incineroar(maxiv="Yes")
ash31=DLycanroc(maxiv="Yes")
ash32=Melmetal(maxiv="Yes")
ash33=Naganadel(maxiv="Yes")
ashteam=teamset([ash1,ash5,ash2,ash3,ash4,ash7,ash8,ash9,ash10,ash11,ash12,ash13,ash14,ash15,ash16,ash17,ash18,ash19,ash20,ash21,ash22,ash23,ash24,ash25,ash26,ash27,ash28,ash29,ash30,ash31,ash32,ash33],5)+[ash6]
ash=Trainer("Pokémon Trainer Ash",ashteam,"Unova")
#cissy
cissy1=Seaking(maxiv="Yes")
cissy2=Starmie(maxiv="Yes")
cissy3=Azumarill(maxiv="Yes")
cissy4=Kingdra(maxiv="Yes")
cissy5=MBlastoise(maxiv="Yes")
cissy6=Kingler(maxiv="gmax")
cissy=Trainer ("Gym Leader Cissy",[cissy1,cissy2,cissy3,cissy4,cissy5,cissy6],"Orange Islands")
#horace
horace1=Meganium (maxiv="gmax")
horace2=Virizion(maxiv="Yes")
horace3=Heracross(maxiv="Yes")
horace5=Donphan(maxiv="Yes")
horace4=Indeedee(maxiv="Yes")
horace6=MGardevoir(maxiv="Yes")
horaceteam=teamset([horace2,horace3,horace4,horace5],4)+[horace1,horace6]
horace=Trainer("Pokémon Trainer Horace",horaceteam,"Johto")    
#danny
danny1=Pinsir(maxiv="Yes")
danny2=Electrode(maxiv="Yes")
danny3=Golem(maxiv="Yes")
danny4=Nidoqueen(maxiv="Yes")
danny5=MScizor(maxiv="Yes")
danny6=Machamp(maxiv="gmax")
danny=Trainer ("Gym Leader Danny",[danny1,danny2,danny3,danny4,danny5,danny6],"Orange Islands")
#rudy
rudy1=MPidgeot(maxiv="Yes")
rudy2=Electivire(maxiv="Yes")
rudy3=Golem(maxiv="Yes")
rudy4=Exeggutor(maxiv="Yes")
rudy5=MAlakazam(maxiv="Yes")
rudy6=Starmie(maxiv="gmax")
rudy7=Rhydon(maxiv="Yes")
rudy8=Venomoth(maxiv="Yes")
rudy9=Hitmonchan(maxiv="Yes")
rudy10=Ninetales(maxiv="Yes")
rudyteam=teamset([rudy2,rudy3,rudy4,rudy6,rudy7,rudy8,rudy9,rudy10],5)+teamset([rudy1,rudy5],1)
rudy=Trainer ("Gym Leader Rudy",rudyteam,"Orange Islands")
#luana
luana1=Kabutops(maxiv="Yes")
luana2=Lunatone(maxiv="Yes")
luana3=Rhyperior(maxiv="Yes")
luana4=Raichu(maxiv="Yes")
luana5=MAlakazam(maxiv="Yes")
luana6=Marowak(maxiv="gmax")
luanateam=teamset([luana2,luana3,luana4,luana5,luana1],5)+[luana6]
luana=Trainer ("Gym Leader Luana",luanateam,"Orange Islands")
#larry
larry1=Tropius(maxiv="Yes")
larry2=Staraptor(maxiv="Yes")
larry3=MAltaria(maxiv="Yes")
larry4=Kilowattrel(maxiv="Yes")
larry5=Bombirdier(maxiv="Yes")
larry6=Flamigo(name="Flamigo💎",maxiv="Flying")
larry7=Dudunsparce(maxiv="Yes")
larry8=Braviary(maxiv="Yes")
larryteam=teamset([larry2,larry3,larry4,larry5,larry1,larry7,larry8],5)+[larry6]
larry=Trainer ("Elite Four Larry",larryteam,"Paldea")
#hassel
hassel1=Noivern (maxiv="Yes")
hassel2=Dragalge(maxiv="Yes")
hassel3=Flapple(maxiv="Yes")
hassel4=Haxorus(maxiv="Yes")
hassel5=Dragonite(maxiv="Yes")
hassel6=Baxcalibur(name="Baxcalibur💎",maxiv="Dragon")
hasselteam=teamset([hassel2,hassel3,hassel4,hassel5,hassel1],5)+[hassel6]
hassel=Trainer ("Elite Four Hassel",hasselteam,"Paldea")
#poppy
poppy1=Bronzong(maxiv="Yes")
poppy2=Copperajah(maxiv="gmax")
poppy3=Magnezone(maxiv="Yes")
poppy4=Corviknight(maxiv="Yes")
poppy5=MMawile(maxiv="Yes")
poppy6=Tinkaton(name="Tinkaton💎",maxiv="Steel")
poppyteam=teamset([poppy2,poppy3,poppy4,poppy5,poppy1],5)+[poppy6]
poppy=Trainer ("Elite Four Poppy",poppyteam,"Paldea")
#geeta
geeta1=Gogoat(maxiv="Yes")
geeta2=Espathra(maxiv="Yes")
geeta3=Veluza(maxiv="Yes")
geeta4=Avalugg(maxiv="Yes")
geeta5=Kingambit(maxiv="Yes")
geeta6=Glimmora(name="Glimmora💎",maxiv="Poison")
geetateam=teamset([geeta2,geeta3,geeta4,geeta5,geeta1],5)+[geeta6]
geeta=Trainer ("Paldea Champion Geeta",geetateam,"Paldea")
#korrina
korrina1=Chesnaught(maxiv="Yes")
korrina2=Pangoro(maxiv="Yes")
korrina3=Hawlucha(maxiv="Yes")
korrina4=Mienshao(maxiv="Yes")
korrina5=Machamp(maxiv="gmax")
korrina6=MLucario(maxiv="Yes")
korrinateam=teamset([korrina2,korrina3,korrina4,korrina5,korrina1],5)+[korrina6]
korrina=Trainer ("Gym Leader Korrina",korrinateam,"Kalos")
#ramos
ramos1=Exeggutor(maxiv="Yes")
ramos2=Sunflora(maxiv="Yes")
ramos3=Victreebel(maxiv="Yes")
ramos4=Jumpluff(maxiv="Yes")
ramos5=MVenusaur(maxiv="Yes")
ramos6=Gogoat(maxiv="gmax")
ramos7=Vileplume(maxiv="Yes")
ramos8=Bellossom(maxiv="Yes")
ramosteam=teamset([ramos2,ramos3,ramos4,ramos5,ramos1,ramos7,ramos8],5)+[ramos6]
ramos=Trainer ("Gym Leader Ramos",ramosteam,"Kalos")
#valerie
valerie1=Togekiss(maxiv="Yes")
valerie2=Azumarill(maxiv="Yes")
valerie3=Florges(maxiv="Yes")
valerie4=MrMime(maxiv="Yes")
valerie5=MMawile(maxiv="Yes")
valerie6=Sylveon(maxiv="gmax")
valerieteam=teamset([valerie2,valerie3,valerie4,valerie5,valerie1],5)+[valerie6]
valerie=Trainer ("Gym Leader Valerie",valerieteam,"Kalos")
#olympia
olympia1=Reuniclus(maxiv="Yes")
olympia2=Malamar(maxiv="Yes")
olympia3=Meowstic(maxiv="Yes")
olympia4=Delphox(maxiv="Yes")
olympia5=Slowking(maxiv="Yes")
olympia6=Meowstic(maxiv="gmax")
olympiateam=teamset([olympia2,olympia3,olympia4,olympia5,olympia1],5)+[olympia6]
olympia=Trainer ("Gym Leader Olympia",olympiateam,"Kalos")
#wulfric
wulfric1=GDarmanitan(maxiv="Yes")
wulfric2=Beartic(maxiv="Yes")
wulfric3=Aurorus(maxiv="Yes")
wulfric4=Cryogonal(maxiv="Yes")
wulfric5=MAbomasnow(maxiv="Yes")
wulfric6=Avalugg(maxiv="gmax")
wulfricteam=teamset([wulfric2,wulfric3,wulfric4,wulfric5,wulfric1],5)+[wulfric6]
wulfric=Trainer ("Gym Leader Wulfric",wulfricteam,"Kalos")
#milo
milo1=Tsareena(maxiv="Yes")
milo2=Bellossom(maxiv="Yes")
milo3=Cherrim(maxiv="Yes")
milo4=Shiftry(maxiv="Yes")
milo5=Eldegoss(maxiv="Yes")
milo6=Flapple(maxiv="gmax")
milo7=Appletun(maxiv="gmax")
milo8=Ludicolo(maxiv="Yes")
miloteam=teamset([milo2,milo3,milo4,milo5,milo1,milo8],5)+teamset([milo6,milo7],1)
milo=Trainer ("Gym Leader Milo",miloteam,"Galar")
#nessa
nessa1=Pelipper(maxiv="Yes")
nessa2=Quagsire(maxiv="Yes")
nessa3=Golisopod(maxiv="Yes")
nessa4=Seaking(maxiv="Yes")
nessa5=Barraskewda(maxiv="Yes")
nessa6=Drednaw(maxiv="gmax")
nessa7=Toxapex(maxiv="Yes")
nessa8=Milotic(maxiv="Yes")
nessateam=teamset([nessa2,nessa3,nessa4,nessa5,nessa1,nessa8,nessa7],5)+[nessa6]
nessa=Trainer ("Gym Leader Nessa",nessateam,"Galar")
#kabu
kabu1=Typhlosion(maxiv="Yes")
kabu2=Torkoal(maxiv="Yes")
kabu3=Salazzle(maxiv="Yes")
kabu4=Ninetales(maxiv="Yes")
kabu5=Arcanine(maxiv="Yes")
kabu6=Centiskorch(maxiv="gmax")
kabuteam=teamset([kabu2,kabu3,kabu4,kabu5,kabu1],5)+[kabu6]
kabu=Trainer ("Gym Leader Kabu",kabuteam,"Galar")
#bea
bea1=Hawlucha(maxiv="Yes")
bea2=Grapplot(maxiv="Yes")
bea3=Hitmontop(maxiv="Yes")
bea4=Pangoro(maxiv="Yes")
bea5=Sirfetchd(maxiv="Yes")
bea6=Machamp(maxiv="gmax")
beateam=teamset([bea2,bea3,bea4,bea5,bea1],5)+[bea6]
bea=Trainer ("Gym Leader Bea",beateam,"Galar")
#allister
allister1=Chandelure(maxiv="Yes")
allister2=Dusknoir(maxiv="Yes")
allister3=Polteageist(maxiv="Yes")
allister4=Runerigus(maxiv="Yes")
allister5=Mimikyu(maxiv="Yes")
allister6=Gengar(maxiv="gmax")
allister7=Dragapult(maxiv="Yes")
allisterteam=teamset([allister2,allister3,allister4,allister5,allister1,allister7],5)+[allister6]
allister=Trainer ("Gym Leader Allister",allisterteam,"Galar")
#lysandre
lysandre1=Mienshao(maxiv="Yes")
lysandre2=Honchkrow(maxiv="Yes")
lysandre3=Pyroar(maxiv="Yes")
lysandre4=MGyarados(name="Mega Gyarados✨",maxiv="Yes")
lysandre5=CZygarde(maxiv="gmax")
lysandre6=Yveltal(maxiv="Yes")
lysandre7=Xerneas(maxiv="Yes")
lysandreteam=teamset([lysandre2,lysandre3,lysandre4,lysandre1,lysandre5],5)+teamset([lysandre6,lysandre7],1)
lysandre=Trainer ("Flare Boss Lysandre",lysandreteam,"Kalos")
#mable
mable1=Delphox(maxiv="Yes")
mable2=Talonflame(maxiv="Yes")
mable3=Malamar(maxiv="Yes")
mable4=Pangoro(maxiv="Yes")
mable5=Weavile(maxiv="gmax")
mable6=MHoundoom(maxiv="Yes")
mableteam=teamset([mable2,mable3,mable4,mable5,mable1],5)+[mable6]
mable=Trainer ("Team Flare Mable",mableteam,"Kalos")
#giallo
giallo1=Tornadus(maxiv="Yes")
giallo2=Thundurus(maxiv="Yes")
giallo3=Landorus(maxiv="Yes")
giallo4=Mandibuzz(maxiv="Yes")
giallo5=Hydreigon(maxiv="Yes")
giallo6=Krookodile(maxiv="gmax")
gialloteam=teamset([giallo2,giallo3,giallo4,giallo5,giallo1],5)+[giallo6]
giallo=Trainer ("Plasma Sage Giallo",gialloteam,"Unova")
#opal
opal1=GRapidash(maxiv="Yes")
opal2=Primarina(maxiv="Yes")
opal3=MMawile(maxiv="Yes")
opal4=GWeezing(maxiv="Yes")
opal5=Togekiss(maxiv="Yes")
opal6=Alcremie(maxiv="gmax")
opalteam=teamset([opal2,opal3,opal4,opal5,opal1],5)+[opal6]
opal=Trainer ("Gym Leader Opal",opalteam,"Galar")
#bede
bede1=GRapidash(maxiv="Yes")
bede2=Gardevoir(maxiv="Yes")
bede3=MMawile(maxiv="Yes")
bede4=Reuniclus(maxiv="Yes")
bede5=Gothitelle(maxiv="Yes")
bede6=Hatterene(maxiv="gmax")
bede7=Sylveon(maxiv="Yes")
bedeteam=teamset([bede2,bede3,bede4,bede5,bede1,bede7],5)+[bede6]
bede=Trainer ("Gym Leader Bede",bedeteam,"Galar")
#gordie
gordie1=Aggron(maxiv="Yes")
gordie2=Stonjourner(maxiv="Yes")
gordie3=MTyranitar(maxiv="Yes")
gordie4=Shuckle(maxiv="Yes")
gordie5=Barbaracle(maxiv="Yes")
gordie6=Coalossal(maxiv="gmax")
gordieteam=teamset([gordie2,gordie3,gordie4,gordie5,gordie1],5)+[gordie6]
gordie=Trainer ("Gym Leader Gordie",gordieteam,"Galar")
#melony
melony1=ANinetales(maxiv="Yes")
melony2=MrRime(maxiv="Yes")
melony3=Eiscue(maxiv="Yes")
melony4=Frosmoth(maxiv="Yes")
melony5=GDarmanitan(maxiv="Yes")
melony6=Lapras(maxiv="gmax")
melonyteam=teamset([melony2,melony3,melony4,melony5,melony1],5)+[melony6]
melony=Trainer ("Gym Leader Melony",melonyteam,"Galar")
#piers
piers1=Overqwil(maxiv="Yes")
piers2=Toxtricity(maxiv="Yes")
piers3=Scrafty(maxiv="Yes")
piers4=Malamar(maxiv="Yes")
piers5=Skuntank(maxiv="Yes")
piers6=Obstagoon(maxiv="Yes")
piersteam=teamset([piers2,piers3,piers4,piers5,piers1],5)+[piers6]
piers=Trainer ("Gym Leader Piers",piersteam,"Galar")
#marnie
marnie1=Crawdaunt(maxiv="Yes")
marnie2=APersian(maxiv="Yes")
marnie3=Scrafty(maxiv="Yes")
marnie4=Liepard(maxiv="Yes")
marnie5=Toxicroak(maxiv="Yes")
marnie6=Grimmsnarl(maxiv="gmax")
marnieteam=teamset([marnie2,marnie3,marnie4,marnie5,marnie1],5)+[marnie6]
marnie=Trainer ("Gym Leader Marnie",marnieteam,"Galar")
#raihan
raihan1=Turtonator(maxiv="Yes")
raihan2=Goodra(maxiv="Yes")
raihan3=Gigalith(maxiv="Yes")
raihan4=Sandaconda(maxiv="Yes")
raihan5=Flygon(maxiv="Yes")
raihan6=Duraludon(maxiv="gmax")
raihan7=Torkoal(maxiv="Yes")
raihanteam=teamset([raihan2,raihan3,raihan4,raihan5,raihan1,raihan7],5)+[raihan6]
raihan=Trainer ("Gym Leader Raihan",raihanteam,"Galar")
#nemona
nemona1=MDLycanroc(maxiv="Yes")
nemona2=Goodra(maxiv="Yes")
nemona3=Orthworm(name="Orthworm💎",maxiv="Steel")
nemona4=Dudunsparce(maxiv="Yes")
nemona5=Skeledirge(maxiv="Yes")
nemona6=Meowscarada(maxiv="Yes")
nemona7=Quaquaval(maxiv="Yes")
nemonateam=teamset([nemona2,nemona3,nemona4,nemona5,nemona1,nemona7],5)+[nemona3]
nemona=Trainer ("Pokémon Trainer Nemona",nemonateam,"Paldea")
#katy
katy1=Lokix(maxiv="Yes")
katy2=Forretress(maxiv="Yes")
katy3=Heracross(maxiv="Yes")
katy4=Spidops(maxiv="Yes")
katy5=Kleavor(maxiv="Yes")
katy6=Ursaring(name="Ursaring💎",maxiv="Bug")
katyteam=teamset([katy2,katy3,katy4,katy5,katy1],5)+[katy6]
katy=Trainer ("Gym Leader Katy",katyteam,"Paldea")
#brassius
brassius1=HLilligant(maxiv="Yes")
brassius2=Tsareena(maxiv="Yes")
brassius3=Breloom(maxiv="Yes")
brassius4=Arboliva(maxiv="Yes")
brassius5=Rillaboom(maxiv="gmax")
brassius6=Sudowoodo(name="Sudowoodo💎",maxiv="Grass")
brassiusteam=teamset([brassius2,brassius3,brassius4,brassius5,brassius1],5)+[brassius6]
brassius=Trainer ("Gym Leader Brassius",brassiusteam,"Paldea")
#Iono
Iono1=Kilowattrel(maxiv="Yes")
Iono2=Dracozolt(maxiv="Yes")
Iono3=Bellibolt(maxiv="Yes")
Iono4=Electrode(maxiv="Yes")
Iono5=Luxray(maxiv="Yes")
Iono6=Mismagius(name="Mismagius💎",maxiv="Electric")
Ionoteam=teamset([Iono2,Iono3,Iono4,Iono5,Iono1],5)+[Iono6]
Iono=Trainer ("Gym Leader Iono",Ionoteam,"Paldea")
#kofu
kofu1=Veluza(maxiv="Yes")
kofu2=Clawitzer(maxiv="Yes")
kofu3=Pelipper(maxiv="Yes")
kofu4=Wugtrio(maxiv="Yes")
kofu5=Basculegion(maxiv="Yes")
kofu6=Basculegion(maxiv="Yes")
kofuteam=teamset([kofu2,kofu3,kofu4,kofu5,kofu1,kofu6],6)
kofu=Trainer ("Gym Leader Kofu",kofuteam,"Paldea")
#ryme
ryme1=Mimikyu(maxiv="Yes")
ryme2=Banette(maxiv="Yes")
ryme3=Spiritomb(maxiv="Yes")
ryme4=Houndstone(maxiv="Yes")
ryme5=HTyphlosion(maxiv="Yes")
ryme6=Toxtricity(name="Toxtricity💎",maxiv="Ghost")
rymeteam=teamset([ryme2,ryme3,ryme4,ryme5,ryme1],5)+[ryme6]
ryme=Trainer ("Gym Leader Ryme",rymeteam,"Paldea")
#grusha
grusha1=Frosmoth(maxiv="Yes")
grusha2=Beartic(maxiv="Yes")
grusha3=Weavile(maxiv="Yes")
grusha4=Cetitan(maxiv="Yes")
grusha5=HAvalugg(maxiv="Yes")
grusha6=Altaria(name="Altaria💎",maxiv="Ice")
grushateam=teamset([grusha2,grusha3,grusha4,grusha5,grusha1],5)+[grusha6]
grusha=Trainer ("Gym Leader Grusha",grushateam,"Paldea")
#tulip
tulip1=Farigiraf(maxiv="Yes")
tulip2=Gallade(maxiv="Yes")
tulip3=Espathra(maxiv="Yes")
tulip4=Gardevoir(maxiv="Yes")
tulip5=Wyrdeer(maxiv="Yes")
tulip6=Florges(name="Florges💎",maxiv="Psychic")
tulipteam=teamset([tulip2,tulip3,tulip4,tulip5,tulip1],5)+[tulip6]
tulip=Trainer ("Gym Leader Tulip",tulipteam,"Paldea")
#gorm
gorm1=Sigilyph(maxiv="Yes")
gorm2=Mandibuzz(maxiv="Yes")
gorm3=Hydreigon(maxiv="Yes")
gorm4=Kingambit(maxiv="Yes")
gorm5=MBanette(maxiv="Yes")
gorm6=Cofagrigus(maxiv="gmax")
gormteam=teamset([gorm2,gorm3,gorm4,gorm5,gorm1],5)+[gorm6]
gorm=Trainer ("Plasma Sage Gorm",gormteam,"Unova")
#gladion
gladion1=Zoroark(maxiv="Yes")
gladion2=Crobat(maxiv="Yes")
gladion3=Weavile(maxiv="Yes")
gladion4=MNLycanroc(name="Midnight Lycanroc(Z-Crystal)",maxiv="Yes")
gladion5=MLucario(maxiv="Yes")
gladion6=Silvally(maxiv="Yes")
gladion7=Venusaur(maxiv="gmax")
gladion8=Charizard(maxiv="gmax")
gladion9=Blastoise(maxiv="gmax")
gladion10=Nihilego(name="Lille✨",maxiv="Yes")
gladionteam=teamset([gladion2,gladion3,gladion4,gladion5,gladion1,gladion10],4)+teamset([gladion7,gladion8,gladion9],1)+[gladion6]
gladion=Trainer ("Pokémon Trainer Gladion",gladionteam,"Alola")
#lusamine
lusamine1=Clefable(maxiv="Yes")
lusamine2=Lilligant(maxiv="Yes")
lusamine3=Milotic(maxiv="Yes")
lusamine4=Mismagius (maxiv="Yes")
lusamine5=Bewear(maxiv="Yes")
lusamine6=Nihilego(maxiv="Yes")
lusamine7=Lopunny(maxiv="Yes")
lusamine8=Salazzle (maxiv="Yes")
lusamine9=Absol(maxiv="Yes")
lusamineteam=teamset([lusamine2,lusamine3,lusamine4,lusamine5,lusamine1,lusamine7,lusamine8,lusamine9],5)+[lusamine6]
lusamine=Trainer ("Aether President Lusamine",lusamineteam,"Alola")
#bronius
bronius1=Liepard(maxiv="Yes")
bronius2=Mandibuzz(maxiv="Yes")
bronius3=Salamence(maxiv="Yes")
bronius4=Bisharp(maxiv="Yes")
bronius5=MSableye(maxiv="Yes")
bronius6=Amoongus(maxiv="gmax")
broniusteam=teamset([bronius2,bronius3,bronius4,bronius5,bronius1],5)+[bronius6]
bronius=Trainer ("Plasma Sage Bronius",broniusteam,"Unova")
#ryoku
ryoku1=Garbodor(maxiv="Yes")
ryoku2=Absol(maxiv="Yes")
ryoku3=Flygon(maxiv="Yes")
ryoku4=Bisharp(maxiv="Yes")
ryoku5=MPinsir(maxiv="Yes")
ryoku6=Scolipede(maxiv="gmax")
ryokuteam=teamset([ryoku2,ryoku3,ryoku4,ryoku5,ryoku1],5)+[ryoku6]
ryoku=Trainer ("Plasma Sage Ryoku",ryokuteam,"Unova")
#rood
rood1=Swoobat(maxiv="Yes")
rood2=Stoutland(maxiv="Yes")
rood3=Zoroark(maxiv="Yes")
rood4=Granbull(maxiv="Yes")
rood5=MHoundoom(maxiv="Yes")
rood6=Chandelure(maxiv="gmax")
roodteam=teamset([rood2,rood3,rood4,rood5,rood1],5)+[rood6]
rood=Trainer ("Plasma Sage Rood",roodteam,"Unova")
#zinzolin
zinzolin1=MAbomasnow(maxiv="Yes")
zinzolin2=Vanilluxe(maxiv="Yes")
zinzolin3=Beartic(maxiv="Yes")
zinzolin4=Weavile(maxiv="Yes")
zinzolin5=Kyurem(maxiv="Yes")
zinzolin6=Cryogonal(maxiv="gmax")
zinzolinteam=teamset([zinzolin2,zinzolin3,zinzolin4,zinzolin5,zinzolin1],5)+[zinzolin6]
zinzolin=Trainer ("Plasma Sage Zinzolin",zinzolinteam,"Unova")
#colress
colress1=Magnezone(maxiv="Yes")
colress2=Beheeyem(maxiv="Yes")
colress3=WRotom(maxiv="Yes")
colress4=PorygonZ(maxiv="Yes")
colress5=MMetagross(maxiv="Yes")
colress6=Klinklang(maxiv="gmax")
colress7=Muk(maxiv="Yes")
colress8=Electrode(maxiv="Yes")
colressteam=teamset([colress2,colress3,colress4,colress5,colress1,colress7,colress8],5)+[colress6]
colress=Trainer ("Team Plasma Colress",colressteam,"Unova")
#argenta
argenta1=Azelf(maxiv="Yes")
argenta2=Mesprit(maxiv="Yes")
argenta3=Uxie(maxiv="Yes")
argenta4=Regirock(maxiv="Yes")
argenta5=Regice(maxiv="Yes")
argenta6=Registeel(maxiv="Yes")
argenta7=Raikou(maxiv="Yes")
argenta8=Entei(maxiv="Yes")
argenta9=Suicune(maxiv="Yes")
argenta10=Latios(maxiv="Yes")
argenta11=Latias(maxiv="Yes")
argenta12=Articuno(maxiv="Yes")
argenta13=Zapdos(maxiv="Yes")
argenta14=Moltres(maxiv="Yes")
argenta15=Heatran(maxiv="Yes")
argenta16=Regigigas(maxiv="Yes")
argentateam=teamset([argenta2,argenta3,argenta4,argenta5,argenta1,argenta7,argenta8,argenta6,argenta9,argenta10,argenta11,argenta12,argenta13,argenta14,argenta15,argenta16],6)
argenta=Trainer ("Hall Matron Argenta",argentateam,"Sinnoh")
#matt
matt1=Mightyena(maxiv="Yes")
matt2=Weezing(maxiv="Yes")
matt3=Crobat(maxiv="Yes")
matt4=Crawdaunt(maxiv="Yes")
matt5=Sharpedo(maxiv="gmax")
matt6=Walrein(maxiv="Yes")
matt=Trainer("Aqua Admin Matt",[matt1,matt2,matt3,matt4,matt5,matt6],"Hoenn")
#shelly
shelly1=Mightyena(maxiv="Yes")
shelly2=Weezing(maxiv="Yes")
shelly3=Crobat(maxiv="Yes")
shelly4=Crawdaunt(maxiv="Yes")
shelly5=Sharpedo(maxiv="gmax")
shelly6=Walrein(maxiv="Yes")
shelly=Trainer("Aqua Admin Shelly",[shelly1,shelly2,shelly3,shelly4,shelly5,shelly6],"Hoenn")
#eusine
eusine1=Pikachu(maxiv="Yes")
eusine2=Jumpluff(maxiv="Yes")
eusine3=Hypno(maxiv="Yes")
eusine4=MAlakazam(maxiv="Yes")
eusine5=Gengar(maxiv="gmax")
eusine6=Electrode(maxiv="Yes")
eusine=Trainer("Pokémon Trainer Eusine",[eusine1,eusine2,eusine3,eusine4,eusine5,eusine6],"Johto")
#evelyn
evelyn1=Pachirisu(maxiv="Yes")
evelyn2=Primeape(maxiv="Yes")
evelyn3=Raikou(maxiv="Yes")
evelyn4=Suicune(maxiv="Yes")
evelyn5=Entei(maxiv="Yes")
evelyn6=MLatios(maxiv="Yes")
evelyn7=Persian(maxiv="Yes")
evelyn8=Lumineon(maxiv="Yes")
evelynteam=teamset([evelyn7,evelyn8,evelyn1,evelyn2,evelyn3,evelyn4,evelyn5,evelyn6],6)
evelyn=Trainer("Battle Chatelaine Evelyn",evelynteam,"Hoenn")
#courtney
courtney1=Mightyena(maxiv="Yes")
courtney2=Weezing(maxiv="Yes")
courtney3=Crobat(maxiv="Yes")
courtney4=Torkoal(maxiv="Yes")
courtney5=Camerupt(maxiv="gmax")
courtney6=Swellow(maxiv="Yes")
courtney=Trainer("Magma Admin Courtney",[courtney1,courtney2,courtney3,courtney4,courtney5,courtney6],"Hoenn")
#butler
butler1=Dusclops(maxiv="Yes")
butler2=Gardevoir(maxiv="Yes")
butler3=Mightyena(maxiv="Yes")
butler4=MSalamence(maxiv="Yes")
butler5=Jirachi(maxiv="gmax")
butler6=Groudon(name="Meta Groudon",maxiv="Yes")
butler=Trainer("Team Magma Butler",[butler1,butler2,butler3,butler4,butler5,butler6],"Hoenn")
#LEGENDARY TRIALS
#Articuno
bossarticuno=Articuno(name="Legendary Articuno",maxiv="Yes",hpev=252,atkev=252,defev=252,spatkev=252,speedev=252,item="Silver Feather",move=["Blizzard","Hurricane","Ice Beam","Extrasensory"])
carticuno=Trainer("Trial Legend Crescent",[bossarticuno])
#Zapdos
bosszapdos=Zapdos(name="Legendary Zapdos",maxiv="Yes",hpev=252,atkev=252,defev=252,spatkev=252,speedev=252,item="Silver Feather",move=["Thunder","Hurricane","Thunderbolt","Drill Peck"])
czapdos=Trainer("Trial Legend Crescent",[bosszapdos])
#Moltres
bossmoltres=Moltres(name="Legendary Moltres",maxiv="Yes",hpev=252,atkev=252,defev=252,spatkev=252,speedev=252,item="Silver Feather",move=["Fire Blast","Sky Attack","Flamethrower","Heat Wave"])
cmoltres=Trainer("Trial Legend Crescent",[bossmoltres])
#gmoltres
bossgmoltres=GMoltres(name="Legendary Galarian Moltres",maxiv="Yes",hpev=252,atkev=252,defev=252,spatkev=252,speedev=252,item="Silver Feather",move=["Dark Pulse","Sky Attack","Flamethrower","Fiery Wrath"])
cgmoltres=Trainer("Trial Legend Crescent",[bossgmoltres])
#GArticuno
bossgarticuno=GArticuno(name="Legendary Galarian Articuno",maxiv="Yes",hpev=252,atkev=252,defev=252,spatkev=252,speedev=252,item="Silver Feather",move=["Ice Beam","Hurricane","Freezing Glare","Extrasensory"])
cgarticuno=Trainer("Trial Legend Crescent",[bossgarticuno])
#Mewtwo
bossmewtwo=Mewtwo(name="Legendary Mewtwo",maxiv="Yes",hpev=252,atkev=252,defev=252,spatkev=252,speedev=252,item="Team Rocket Armor",move=["Psystrike","Shadow Ball","Aura Sphere","Psychic"])
cmewtwo=Trainer("Trial Legend Crescent",[bossmewtwo])
#adaman
adaman1=Flareon(maxiv="Yes")
adaman2=Jolteon(maxiv="Yes")
adaman3=Glaceon(maxiv="Yes")
adaman4=Vaporeon(maxiv="Yes")
adaman5=Leafeon(maxiv="Yes")
adaman6=Umbreon(maxiv="Yes")
adaman=Trainer("Clan Leader Adaman",[adaman1,adaman2,adaman3,adaman4,adaman5,adaman6],"Hisui")
#celosia
celosia1=Absol(maxiv="Yes")
celosia2=Zoroark(maxiv="Yes")
celosia3=Aegislash(maxiv="Yes")
celosia4=Liepard(maxiv="Yes")
celosia5=Drapion(maxiv="Yes")
celosia6=MManectric(maxiv="Yes")
celosiateam=teamset([celosia2,celosia3,celosia4,celosia5,celosia1],5)+[celosia6]
celosia=Trainer ("Team Flare Celosia",celosiateam,"Kalos")
#bryony
bryony1=Mandibuzz(maxiv="Yes")
bryony2=Krookodile(maxiv="Yes")
bryony3=Scrafty(maxiv="Yes")
bryony4=Liepard(maxiv="Yes")
bryony5=Malamar(maxiv="Yes")
bryony6=Kingambit(maxiv="Yes")
bryonyteam=teamset([bryony2,bryony3,bryony4,bryony5,bryony1],5)+[bryony6]
bryony=Trainer ("Team Flare Bryony",bryonyteam,"Kalos")
#aliana
aliana1=Diggersby(maxiv="Yes")
aliana2=Gourgeist(maxiv="Yes")
aliana3=Pyroar(maxiv="Yes")
aliana4=Liepard(maxiv="Yes")
aliana5=Mightyena(maxiv="Yes")
aliana6=Druddigon(maxiv="Yes")
alianateam=teamset([aliana2,aliana3,aliana4,aliana5,aliana1],5)+[aliana6]
aliana=Trainer ("Team Flare Aliana",alianateam,"Kalos")
#xerosic
xerosic1=MMawile(maxiv="Yes")
xerosic2=Whimsicott(maxiv="Yes")
xerosic3=Jellicent(maxiv="Yes")
xerosic4=Volcarona(maxiv="Yes")
xerosic5=Crobat(maxiv="Yes")
xerosic6=Malamar(maxiv="Yes")
xerosic7=Granbull(maxiv="Yes")
xerosic8=Persian(maxiv="Yes")
xerosicteam=teamset([xerosic2,xerosic3,xerosic4,xerosic5,xerosic1,xerosic7,xerosic8],5)+[xerosic6]
xerosic=Trainer ("Team Flare Xerosic",xerosicteam,"Kalos")
#heatran
bossheatran=Heatran(name="Legendary Heatran",maxiv="Yes",hpev=252,atkev=252,defev=252,spatkev=252,speedev=252,item="Magma Stone",move=["Magma Storm","Flash Cannon","Earth Power","Fire Blast"])
cheatran=Trainer("Trial Legend Crescent",[bossheatran])
#raikou
bossraikou=Raikou(name="Legendary Raikou",maxiv="Yes",hpev=252,atkev=252,defev=252,spatkev=252,speedev=252,item="Rainbow Feather",move=["Thunder Fang","Crunch","Extreme Speed","Wild Charge"])
bossentei=Entei(name="Legendary Entei",maxiv="Yes",hpev=252,atkev=252,defev=252,spatkev=252,speedev=252,item="Rainbow Feather",move=["Flare Blitz","Crunch","Extreme Speed","Sacred Fire"])
bosssuicune=Suicune(name="Legendary Suicune",maxiv="Yes",hpev=252,atkev=252,defev=252,spatkev=252,speedev=252,item="Rainbow Feather",move=["Hydro Pump","Scald","Extreme Speed","Ice Beam"])
cbeast=Trainer("Trial Legend Crescent",[bosssuicune,bossraikou,bossentei])
#giacomo
giacomo1=Cacturne(maxiv="Yes")
giacomo2=Honchkrow(maxiv="Yes")
giacomo3=Mabosstiff(maxiv="Yes")
giacomo4=Krookodile(maxiv="Yes")
giacomo5=Kingambit(maxiv="Yes")
giacomo6=Revavroom(name="Segin Starmobile",type1="Dark",type2=None,maxiv="Yes")
giacomo=Trainer("Team Star Giacomo",[giacomo1,giacomo2,giacomo3,giacomo4,giacomo5,giacomo6],"Paldea")
#mela
mela1=Torkoal(maxiv="Yes")
mela2=Coalossal(maxiv="Yes")
mela3=Arcanine(maxiv="Yes")
mela4=Armarouge(maxiv="Yes")
mela5=MHoundoom(maxiv="Yes")
mela6=Revavroom(name="Schedar Starmobile",type1="Fire",type2=None,maxiv="Yes")
mela=Trainer("Team Star Mela",[mela1,mela2,mela3,mela4,mela5,mela6],"Paldea")
#atticus
atticus1=Skuntank(maxiv="Yes")
atticus2=Muk(maxiv="Yes")
atticus3=Dragalge(maxiv="Yes")
atticus4=Toxapex(maxiv="Yes")
atticus5=Grafaiai(maxiv="Yes")
atticus6=Revavroom(name="Navi Starmobile",type1="Poison",type2=None,maxiv="Yes")
atticus=Trainer("Team Star Atticus",[atticus1,atticus2,atticus3,atticus4,atticus5,atticus6],"Hoenn")
#ortega
ortega1=Azumarill(maxiv="Yes")
ortega2=Wigglytuff(maxiv="Yes")
ortega3=Dachsbun(maxiv="Yes")
ortega4=Klefki(maxiv="Yes")
ortega5=Hatterene(maxiv="Yes")
ortega6=Revavroom(name="Ruchbah Starmobile",type1="Fairy",type2=None,maxiv="Yes")
ortega=Trainer("Team Star Ortega",[ortega1,ortega2,ortega3,ortega4,ortega5,ortega6],"Paldea")
#eri
eri1=Toxicroak(maxiv="Yes")
eri2=Passimian(maxiv="Yes")
eri3=Primeape(maxiv="Yes")
eri4=Anihilape(maxiv="Yes")
eri5=MLucario(maxiv="Yes")
eri6=Revavroom(name="Caph Starmobile",type1="Fighting",type2=None,maxiv="Yes")
eri=Trainer("Team Star Eri",[eri1,eri2,eri3,eri4,eri5,eri6],"Paldea")
#penny
penny1=Umbreon(maxiv="Yes")
penny2=Leafeon(maxiv="Yes")
penny3=Flareon(maxiv="Yes")
penny4=Jolteon(maxiv="Yes")
penny5=Vaporeon(maxiv="Yes")
penny6=Sylveon(name="Sylveon💎",maxiv="Fairy")
penny=Trainer("Star Leader Penny",[penny1,penny2,penny3,penny4,penny5,penny6],"Paldea")
#clavell
clavell1=Oranguru(maxiv="Yes")
clavell2=Abomasnow(maxiv="Yes")
clavell3=Polteageist(maxiv="Yes")
clavell4=Gyarados(maxiv="Yes")
clavell5=Houndoom(maxiv="Yes")
clavell6=Quaquaval(name="Quaquaval💎",maxiv=random.choice(["Water","Fighting"]))
clavell7=Amoongus(maxiv="Yes")
clavell8=Meowscarada(name="Meowscarada💎",maxiv=random.choice(["Grass","Dark"]))
clavell9=Skeledirge(name="Skeledirge💎",maxiv=random.choice(["Fire","Ghost"]))
clavellteam=teamset([clavell2,clavell3,clavell4,clavell5,clavell1,clavell7],5)+teamset([clavell6, clavell9, clavell8],1)
clavell=Trainer ("Director Clavell Mesagoza",clavellteam,"Paldea")
#TEST2
t3=Palafin(maxiv="Yes")
t4=Tinglu(maxiv="Yes")
t5=Chienpao(maxiv="Yes")
t6=Chiyu(maxiv="Yes")
t7=Wochien(maxiv="Yes")
t8=Gholdengo(name="Gholdengo💎",maxiv="Steel")
test2=Trainer("Test-02",[t3,t4,t5,t6,t7,t8])
#############
matchx=match()
e4list=[hassel,larry,poppy,rika,will,koga,kahili,acerola,olivia,molayne,hala,caitlin,grimsley,shauntal,marshal,karen,drake,glacia,sidney,phoebe,siebold,lorelei,agatha,bruno,lance,aaron,bertha,lucian,flint,wikstrom,drasna,malva]

champlist=[geeta,oak,odrake,may,leon,alder,brendan,kukui,blue,red,wallace,steven,cynthia,diantha,mustard]

fronlist=[noland,lucy,tucker,greta,anabel,palmer,darach,dahlia,brandon,spenser,argenta,Thorton]

gymlist=[tulip,grusha,ryme,kofu,Iono,brassius,katy,raihan,marnie,piers,melony,gordie,bede,opal,allister,bea,kabu,nessa,milo,wulfric,olympia,valerie,clemont,ramos,korrina,viola,luana,rudy,danny,cissy,jasmine,brock,misty,surge,erika,sabrina,blaine,falkner,bugsy,whitney,chuck,pryce,claire,roxanne,brawly,wattson,flannery,norman,winona,tate,liza,juan,roark,fantina,byron,maylene,wake,gardenia,candice,volkner,lenora,burgh,elesa,clay,skyla,brycen,drayden,cheren,roxie,marlon,grant,janine]

talentlist=[clavell,goh,gladion,eusine,benga,trevor,paul,sawyer,ingo,ethan,gary,silver,buck,n,alain,tobias,ash,quillon,danika,horace,barry,wally,nemona,evelyn,adaman]

evilist=[penny,eri,ortega,atticus,mela,giacomo,xerosic,aliana,celosia,bryony,mable,lysandre,courtney,shelly,matt,ghetsis,colress,giallo,zinzolin,rood,ryoku,bronius,gorm,alsada,alturo,tabitha,ariana,archer,cyrus,archie,maxie,saturn,giovanni,butler]

gym=random.choice(gymlist)
elite4=random.choice(e4list)
champ=random.choice(champlist)
frontier=random.choice(fronlist)
evil=random.choice(evilist)
talent=random.choice(talentlist)
def genplayer2(f):
    pl=None
    field.weather="Clear"
    field.terrain="Normal"
    if "Bridge" in f.location:
        f.location="🌉 "+f.location
    if "River" in f.location:
        f.location="🏞️ "+f.location
    if "Desert" in f.location:
        f.location="🏜️ "+f.location
    if ("Mount" or "Mt") in f.location:
        f.location="⛰️ "+f.location
    if "Forest" in f.location:
        f.location="🌳 "+f.location
    if "Town" in f.location:
        f.location="🏡 "+f.location
    if "City" in f.location:
        f.location="🏙️ "+f.location
    if "Team Flare" in f.location:
        pl=random.choice([malva,xerosic,aliana,celosia,bryony,mable,lysandre,genTrainer(trclass=random.choice(["Ruin Explorer","Hiker"]))])
        if "Malva" in pl.name:
            pl.name="Team Flare Malva"
    if "Trackless" in f.location:
        pl=random.choice([cbeast,genTrainer(trclass=random.choice(["Ruin Explorer","Hiker"]))])
    if "Scorched Slab" in f.location:
        pl=random.choice([cheatran,buck,genTrainer(trclass=random.choice(["Volcano Explorer","Hiker"]))])
    if "Kanto" in f.location:
        pl=random.choice([ash,gary,red,giovanni,genTrainer(trclass=random.choice(["Kanto Trainer"]))])
    if "Hoenn" in f.location:
        pl=random.choice([ethan,silver,genTrainer(trclass=random.choice(["Hoenn Trainer"]))])
    if "Paldea" in f.location:
        pl=random.choice([hassel,larry,poppy,rika,geeta,genTrainer(trclass=random.choice(["Johto Trainer"]))])
    if "Johto" in f.location:
        pl=random.choice([ethan,silver,genTrainer(trclass=random.choice(["Johto Trainer"]))])
    if "Sinnoh" in f.location:
        pl=random.choice([cynthia,genTrainer(trclass=random.choice(["Sinnoh Trainer"]))])
    if "Kalos" in f.location:
        pl=random.choice([diantha,genTrainer(trclass=random.choice(["Kalos Trainer"]))])
    if "Alola" in f.location:
        pl=random.choice([kahili,acerola,olivia,molayne,hala,kukui,genTrainer(trclass=random.choice(["Alola Trainer"]))])
    if " Galar" in f.location:
        pl=random.choice([raihan,marnie,piers,melony,gordie,bede,opal,allister,bea,kabu,nessa,milo,leon,genTrainer(trclass=random.choice(["Galar Trainer"]))])
    if "Power Plant" in f.location:
        field.weather="Electric Terrain"
        pl=random.choice([czapdos,genTrainer(trclass=random.choice(["Rocket Grunt","Electrician"]))])
    if "Mt. Ember" in f.location:
        field.weather="Sunny"
        pl=random.choice([cmoltres,genTrainer(trclass=random.choice(["Rocket Grunt","Kindler"]))])
    if "Mt. Chimney" in f.location:
        pl=random.choice([maxie,tabitha,brendan,archie,genTrainer(trclass=random.choice(["Magma Grunt","Aqua Grunt"]))])
    if "Mt. Pyre" in f.location:
        pl=random.choice([phoebe,genTrainer(trclass=random.choice(["Exorcist"]))])
    if "Marine Cave" in f.location:
        pl=random.choice([archie,brendan,may,genTrainer(trclass=random.choice(["Aqua Grunt"]))])
    if "Terra Cave" in f.location:
        pl=random.choice([maxie,tabitha,brendan,may,genTrainer(trclass=random.choice(["Magma Grunt"]))])
    if "Aqua Hideout" in f.location:
        pl=random.choice([archie,genTrainer(trclass=random.choice(["Aqua Grunt"]))])
    if "Magma Hideout" in f.location:
        pl=random.choice([maxie,tabitha,genTrainer(trclass=random.choice(["Magma Grunt"]))])
    if "Mountain Coronet" in f.location:
        pl=random.choice([cyrus,genTrainer(trclass=random.choice(["Sinnoh Trainer","Galactic Grunt"]))])
    if "Spear Pillar" in f.location:
        pl=random.choice([cyrus,cynthia,saturn,barry])
    if "Mountain Stark" in f.location:
        pl=random.choice([buck,saturn,genTrainer(trclass=random.choice(["Sinnoh Trainer","Ruin Explorer","Fiery Breathe","Kindler","Paleontologist"]))])
    if "League, Sinnoh" in f.location:
        pl=random.choice([aaron,bertha,flint,lucian,cynthia,tobias,barry])
        if "Tobias" in pl.name:
            pl.name="SCL Champion Tobias"
    if "Evergrande" in f.location:
        pl=random.choice([sidney,phoebe,glacia,drake,steven,wallace])
    if "Sootopolis City" in f.location:
        pl=random.choice([juan,wallace,genTrainer(trclass=random.choice(["Swimmer","Hoenn Trainer","Scuba Diver","Fisherman"]))])
    if "Mosdeep City" in f.location:
        pl=random.choice([tate,liza,steven,maxie,genTrainer(trclass=random.choice(["Hoenn Trainer","Psychic"]))])
    if "Fortree City" in f.location:
        pl=random.choice([winona,steven,may,genTrainer(trclass=random.choice(["Hoenn Trainer","Pilot","Air Force Officer"]))])
    if "Lavaridge Town" in f.location:
        pl=random.choice([flannery,genTrainer(trclass=random.choice(["Hoenn Trainer","Kindler","Fiery Breathe"]))])
    if "Mauville City" in f.location:
        pl=random.choice([wattson,wally,may,genTrainer(trclass=random.choice(["Hoenn Trainer","Rocker","Guitarist"]))])
    if "Dewford Town" in f.location:
        pl=random.choice([brawly,steven,genTrainer(trclass=random.choice(["Hoenn Trainer","Blackbelt","Dojo Master"]))])
    if "Sunnyshore City" in f.location:
        pl=random.choice([volkner,jasmine,flint,paul,genTrainer(trclass=random.choice(["Sinnoh Trainer","Electrician","Rocker","Guitarist"]))])
    if "Snowpoint City" in f.location:
        field.weather="Snowstorm"
        pl=random.choice([candice,brandon,tobias,paul,genTrainer(trclass=random.choice(["Sinnoh Trainer","Elder Trainer","Galactic Grunt","Skier","Boarder"]))])
    if "Canalave City" in f.location:
        pl=random.choice([byron,roark,paul,barry,genTrainer(trclass=random.choice(["Sinnoh Trainer","Industry Worker","Factory Boss","Electrician","Sailor"]))])
    if "Hearthome City" in f.location:
        pl=random.choice([fantina,paul,barry,genTrainer(trclass=random.choice(["Sinnoh Trainer","Exorcist"]))])
    if "Pastoria City" in f.location:
        pl=random.choice([wake,paul,genTrainer(trclass=random.choice(["Sinnoh Trainer","Blackbelt","Swimmer","Fisherman"]))])
    if "Veilstone City" in f.location:
        pl=random.choice([maylene,cyrus,saturn,paul,genTrainer(trclass=random.choice(["Sinnoh Trainer","Galactic Grunt","Blackbelt"]))])
    if "Eterna City" in f.location:
        pl=random.choice([gardenia,saturn,paul,genTrainer(trclass=random.choice(["Sinnoh Trainer","Gardener","Galactic Grunt"]))])
    if "Oreburgh City" in f.location:
        pl=random.choice([roark,paul,genTrainer(trclass=random.choice(["Sinnoh Trainer","Paleontologist","Ruin Explorer"]))])
    if "Rustboro City" in f.location:
        pl=random.choice([roxanne,genTrainer(trclass=random.choice(["Hoenn Trainer","Paleontologist","Aqua Grunt","Ruin Explorer"]))])
    if "Petalburg City" in f.location:
        pl=random.choice([norman,wally,genTrainer(trclass=random.choice(["Hoenn Trainer","Bug Catcher","Bug Researcher"]))])
    if "Twinleaf Town" in f.location:
        pl=random.choice([barry,genTrainer(trclass=random.choice(["Sinnoh Trainer"]))])
    if "Littleroot Town" in f.location:
        pl=random.choice([brendan,norman,may,genTrainer(trclass=random.choice(["Hoenn Trainer"]))])
    if "Cianwood City" in f.location:
        pl=random.choice([horace,chuck,genTrainer(trclass=random.choice(["Blackbelt","Dojo Master"]))])
    if "Azalea City" in f.location:
        pl=random.choice([bugsy,genTrainer(trclass="Bug Catcher")])
    if "Blackthorn City" in f.location:
        pl=random.choice([claire,genTrainer(trclass="Dragon Tamer")])
    if "Ecruteak City" in f.location:
        pl=random.choice([morty,genTrainer(trclass="Exorcist")])
    if "Mahogany Town" in f.location:
        pl=random.choice([pryce,genTrainer(trclass=random.choice(["Johto Trainer","Boarder","Skier"]))])
    if "Lavender Town" in f.location:
        pl=random.choice([morty,blue,genTrainer(trclass="Exorcist")])
    if "Safari Zone" in f.location:
        pl=genTrainer(trclass=random.choice(["Fisherman","Bug Researcher","Bug Catcher","Rocket Grunt"]))
    if "Cycling Road" in f.location:
        pl=genTrainer(trclass=random.choice(["Biker","Cueball","Thief","Smuggler","Goon","Driver","Street Punk"]))
    if "Seafoam Island" in f.location:
        field.weather="Snowstorm"
        pl=random.choice([carticuno,genTrainer(trclass=random.choice(["Skier","Boarder"]))])        
    if "Rock Tunnel" in f.location or "Mount Moon" in f.location:
        pl=genTrainer(trclass=random.choice(["Ruin Explorer","Hiker","Paleontologist"]))
    if f.location in ["Victory Road, Kanto","Victory Road, Hoenn"]:
        pl=genTrainer(trclass=random.choice(["Ace Trainer","Challenger","Dragon Tamer"]))
    if "Violet City" in f.location:
        pl=falkner
    if "Olivine City" in f.location:
        pl=jasmine
    if "Indigo Plateau" in f.location:
        pl=random.choice([lorelei,bruno,agatha,lance,will,karen,koga,blue])
        blue.name="Kanto Champion Blue"
        ch=random.randint(1,3)
        if ch==3:
            lance.name="Johto Champion Lance"
        if ch==2:
            lance.name="Kanto Champion Lance"
    if "Goldenrod City" in f.location:
        pl=random.choice([whitney,genTrainer(trclass=random.choice(["Rocket Grunt","Paleontologist"]))])
    if "New Bark Town" in f.location:
        pl=random.choice([ethan,silver])
    if "Mount Silver" in f.location:
        pl=red
    if "Cinnabar Island" in f.location:
        pl=blaine
    if "Fuchsia City" in f.location:    
        pl=koga 
        koga.name="Gym Leader Koga"
    if "Celadon City" in f.location:
        pl=random.choice([erika,genTrainer(trclass=random.choice(["Rocket Grunt","Businessman"]))])
    if "Vermilion City" in f.location:
        pl=random.choice([surge,genTrainer(trclass=random.choice(["Rocker","Businessman","Guitarist","Sailor","Electrician"]))])
    if "Saffron City" in f.location:
        pl=sabrina
    if "Pallet Town" in f.location:
        pl=random.choice([gary,ash])
    if "Viridian Forest" in f.location:
        pl=genTrainer(random.choice(["Bug Catcher","Bug Researcher"]))
    if "Viridian City" in f.location:
        pl=random.choice([giovanni,blue])
        blue.name="Gym Leader Blue"
        giovanni.name="Gym Leader Giovanni"
    if "Pewter City" in f.location:
        pl=brock
    if "Cerulean Cave" in f.location:
        pl=random.choice([giovanni,red,cmewtwo,genTrainer(trclass=random.choice(["Ace Trainer","Challenger"]))])
    if "Cerulean City" in f.location:
        pl=random.choice([misty,genTrainer(trclass=random.choice(["Swimmer","Marine Biologist"]))])
        field.weather="Cloudy"
    if pl is None:
        pl=random.choices([matchx[1],gym,elite4,champ,frontier,evil,talent],weights=[15,5,5,5,5,5,5],k=1)[0]
    return pl
#PLAYER 02
#PLAYER 01
#pylint:disable=C0116
#pylint:disable=W0311
#pylint:disable=R0916
#pylint:disable=C0304
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
def teammaker(trclass=None,trname=None,pknum=6,field=field):
    "Creates Team"
    mons=[]
    team=[]
    if trclass=="Pokémon Trainer":
        mons=allmon
    ultrabeasts=[MDiancie,Blacephalon,Stakataka,Naganadel,UNecrozma,Necrozma,DMNecrozma,DWNecrozma,FMLunala,RSSolgaleo,Lunala,Solgaleo,Guzzlord,Kartana,Celesteela,Xurkitree,Buzzwole,Nihilego,Pheromosa]
    legendary=[Chiyu,Tinglu,Chienpao,Wochien,MMewtwoX,MMewtwoY,Enamorus,TEnamorus,Koraidon,Miraidon,ICalyrex,SCalyrex,Regieleki,Regidrago,Glastrier,Spectrier,Zarude,DUrshifu,WUrshifu,Eternatus,Zamazenta,Zacian,GArticuno,GZapdos,GMoltres,Melmetal,Zeraora,Silvally,Marshadow,Magearna,Tapufini,Tapubulu,Tapulele,Tapukoko,Diancie,MDiancie,UHoopa,Volcanion,CZygarde,Xerneas,Yveltal,Genesect,Keldeo,Meloetta,PMeloetta,BKyurem,WKyurem,Zekrom,Reshiram,Kyurem,TLandorus,TThundurus,TTornadus,Thundurus,Tornadus,Landorus,Victini,Cobalion,Terrakion,Virizion,Arceus,Shaymin,SShaymin,Darkrai,Cresselia,Manaphy,Uxie,Azelf,Mesprit,Registeel,Regirock,Regice,Articuno,Zapdos,Moltres,Raikou,Entei,Suicune,Lugia,Hooh,Celebi,Deoxys,ADeoxys,SDeoxys,DDeoxys,Jirachi,Mew,Rayquaza,Latias,Latios,MLatias,MLatios,Groudon,Kyogre,PGroudon,PKyogre,MRayquaza,Mewtwo,Dialga,ODialga,Palkia,OPalkia,Giratina,OGiratina,Heatran,Regigigas]
    if trclass in ["UB Expert"]:
        mons=ultrabeasts
    if trclass in ["Galar Trainer"]:
        mons=[Venusaur, Charizard,Blastoise,Butterfree,Pikachu,GRapidash,GSlowbro,GSlowking,Sirfetchd,Gengar,Kingler,GWeezing,MrRime, Lapras,Snorlax,Obstagoon,GDarmanitan,Runerigus,Garbodor,Rillaboom,Cinderace,Inteleon,Corviknight,Orbeetle,Eldegoss,Drednaw,Coalossal,Flapple,Appletun,Sandaconda,Barraskewda,Toxtricity,Centiskorch,Polteageist,Hatterene,Grimmsnarl,Perrserker,Alcremie,Frosmoth,Stonjourner,Eiscue,Indeedee,Copperajah,Dracovish,Dracozolt,Duraludon,Dragapult]
    if trclass in ["Alola Trainer"]:
        mons=[MVenusaur,MCharizardX,MCharizardY,MBlastoise,MBeedrill,MAlakazam,MGengar,MScizor, MSteelix,MHeracross,MAerodactyl,MHoundoom,MSceptile,MSwampert,MBlaziken,MKangaskhan,MPinsir, MGyarados,MAmpharos,MTyranitar,MGardevoir, MSableye,MMawile,MAggron, MMedicham,MManectric,MSharpedo,MCamerupt,MAltaria,MBanette,MAbsol,MGlalie,MSalamence,MMetagross, MLopunny,MGarchomp,MGallade,MLucario,MAbomasnow,MAudino,ARaticate,ARaichu,ASandslash,ANinetales,ADugtrio,APersian,AGolem,AMuk, AExeggutor,AMarowak,Decidueye,Incineroar,Primarina,Toucannon, Vikavolt,DLycanroc,MDLycanroc,MNLycanroc,SWishiwashi, Toxapex,Mudsdale,Araquanid,Salazzle,Bewear,Tsareena,Golisopod,Palossand, Silvally,Turtonator,Mimikyu,Drampa, Dhelmise,Kommo]
    if trclass in ["Kalos Trainer"]:
        mons=[Chesnaught, Delphox, Greninja, Talonflame, Vivillon,Pyroar,Florges,Gogoat,Pangoro,Meowstic, Aegislash,Malamar, Barbaracle,Dragalge, Clawitzer,Heliolisk,Tyrantrum,Aurorus, Sylveon,Hawlucha,Goodra,Klefki,Trevenant,Gourgeist,Avalugg,Noivern,MVenusaur,MCharizardX,MCharizardY,MBlastoise,MBeedrill,MAlakazam,MGengar,MScizor, MSteelix,MHeracross,MAerodactyl,MHoundoom,MSceptile,MSwampert,MBlaziken,MKangaskhan,MPinsir, MGyarados,MAmpharos,MTyranitar,MGardevoir, MSableye,MMawile,MAggron, MMedicham,MManectric,MSharpedo,MCamerupt,MAltaria,MBanette,MAbsol,MGlalie,MSalamence,MMetagross, MLopunny,MGarchomp,MGallade,MLucario,MAbomasnow,MAudino]
    if trclass in ["Johto Trainer"]:
        mons=[Donphan,Porygon2,Miltank,Magcargo,Corsola,Delibird,Mantine,Granbull,Shuckle,Ursaring,Slowking,Wobbuffet,Forretress,Quagsire,Sunflora,Jumpluff,Sudowoodo,Bellossom,Xatu,Hitmontop,Ariados,Noctowl,Ledian,Furret,Meganium,Typhlosion,Feraligatr, Crobat,Lanturn,Ampharos,MAmpharos,Azumarill,Politoed,Espeon,Umbreon,Steelix,MSteelix, Scizor,MScizor,Heracross,MHeracross,Skarmory,Houndoom,MHoundoom,Kingdra,Blissey,Tyranitar,MTyranitar]
    if trclass in ["Kanto Trainer"]:
        mons=[Ditto,Scyther,Seaking,Rhydon,Chansey,Marowak,Electrode,Hypno,Persian,Dugtrio,Kingler,Wigglytuff,Sandslash,Clefable,Butterfree,Beedrill,Fearow,Pikachu,Venusaur,MVenusaur,Charizard,MCharizardX,MCharizardY,Blastoise,MBlastoise,MBeedrill,Pidgeot,MPidgeot,Arbok, Nidoking,Nidoqueen,Ninetales,Golduck,Primeape,Arcanine,Poliwrath, Alakazam,MAlakazam,Machamp,Victreebel,Tentacruel,Golem,Rapidash,Slowbro,MSlowbro,Dodrio,Dewgong,Muk,Cloyster,Gengar,MGengar,Exeggutor,Hitmonchan,Hitmonlee,Weezing,Kangaskhan,MKangaskhan,Starmie,Tauros,Jynx,Pinsir,MPinsir,Gyarados,MGyarados,Lapras,Jolteon,Vaporeon,Flareon,Omastar,Kabutops,Aerodactyl,MAerodactyl,Snorlax,Dragonite]
    if trclass in ["Hoenn Trainer"]:
        mons=[ Sceptile,MSceptile,Blaziken,MBlaziken,Swampert,MSwampert,Mightyena,Ludicolo,Shiftry,Swellow,Pelipper,Gardevoir,MGardevoir,Breloom, Slaking,Exploud,Hariyama,MSableye,MMawile,Aggron,MAggron,Medicham,MMedicham,MManectric,Sharpedo,MSharpedo,Wailord,Camerupt,MCamerupt,Torkoal,Flygon,Altaria,MAltaria,Zangoose,Seviper,Solrock,Lunatone,Whiscash,Crawdaunt,Claydol,Cradily,Armaldo,Milotic,Banette,MBanette,Absol,MAbsol,Glalie,MGlalie,Walrein,Huntail,Gorebyss,Relicanth,Salamence,MSalamence,Metagross,MMetagross]
    if trclass in ["Sinnoh Trainer"]:
        mons=[Lickilicky,Torterra,Infernape,Empoleon,Staraptor,Luxray,Roserade,Rampardos,Bastiodon,Vespiquen,EGastrodon,WGastrodon,Ambipom,Drifblim,MLopunny,Mismagius,Honchkrow,Purugly,Skuntank,Bronzong,Spiritomb,Garchomp,Lucario,MLucario,Hippowdon,MGarchomp,Drapion,Toxicroak,Abomasnow,MAbomasnow,Weavile,Magnezone,Rhyperior,Tangrowth,Electivire,Magmortar,Togekiss,Yanmega,Gliscor,Gallade,MGallade,Probopass,Dusknoir,Froslass,WRotom]
    if trclass in ["Unova Trainer"]:
        mons=[Musharna,Sawk,Throh,Simipour,Simisage,Simisear,Garbodor,Serperior,Emboar,Samurott,Stoutland,Unfezant,Zebstrika,Gigalith,Excadrill,Conkeldurr,Seismitoad,Leavanny,Scolipede,Krookodile,Darmanitan,Scrafty,Cofagrigus,Carracosta,Archeops,Zoroark,Gothitelle, Reuniclus, Swanna,Vanilluxe,Escavalier,Jellicent,Galvantula,Ferrothorn,Eelektross,Chandelure,Haxorus,Beartic,Accelgor,Mienshao,Druddigon,Golurk,Bisharp,Bouffalant,Braviary,Mandibuzz,Heatmor,Durant,Hydreigon,Volcarona,MCharizardX, MCharizardY,MBlastoise, MVenusaur]
#FIGHTING SPECIALIST 
    if trclass in ["Dojo Master","Blackbelt"]:
        namelist=["Taishi","Damme","Wesley","Joe","Dolph","Kenji","Kiyo","Lao","Lung","Nob","Wai","Yoshi","Atsushi","Daisuke","Hideki","Hitoshi","Koichi","Koji","Yuji","Rhett","Takao","Theodore","Zander","Aaron","Hugh","Mike","Nicolas","Shea","Takashi","Adam","Carl","Colby","Darren","David","Derek","Gregory","Griffin","Jarrett","Kendal","Luke","Nathaniel","Philip","Rafael","Ray","Ricky","Sean","Willie","Davon","Ander","Kenji","Manford","Benjamin","Edward","Grant","Jay","Kendrew","Kentaro","Ryder","Teppei","Tyrone","Corey","Donny","Drago","Gordon","Grigor","Jeriel","Kenneth","Mathis","Martell","Rodrigo","Rich","Rocky","Wesley","Zachery","Alonzo","Gunnar","Killan","Markus","Yanis","Ricardo","Igor","Cadox","Banting","Clayton","Earl","Greg","Roy","Terry","Walter","Tracy","Alvaro","Curtis"]
        nn=random.choice(namelist)
        new_name=trclass+" "+nn
        mons=[Sawk,Throh,PTauros,Flamigo,Slitherwing,Anihilape,Quaquaval,Ironvaliant,Ironhands,Greattusk,Hitmontop,DUrshifu,WUrshifu,Sirfetchd,Grapplot,Sneasler,HDecidueye,Hawlucha,Pangoro,Chesnaught,Mienshao,Scrafty,HLilligant,Conkeldurr,Emboar,MBlaziken,MGallade,Gallade,Machamp,Poliwrath,Hitmonchan,Hitmonlee,Infernape,Blaziken,Breloom,Primeape,Heracross,MHeracross,Hariyama,MMedicham]
   #ELDER TRAINERS     
    if trclass =="Elder Trainer":
        namelist=["Jules","Shriner","Jason","Apollo","Damon","Castor","Marcus","Henry","Orion","Arthur","Julius","Zephyr","Helios","Liam","Odysseus","Albert","Helios"]
        nn=random.choice(namelist)
        new_name=trclass+" "+nn
        mons=[Tyrantrum,Aurorus,Carracosta,MAerodactyl,Aerodactyl,Kabutops,Omastar,Armaldo,Cradily,Rampardos,Bastiodon,Cloyster,Relicanth,Claydol,Arcanine,Mamoswine,Spiritomb,Lunatone,Solrock,Yanmega]+legendary
        mons+=random.choices([Rayquaza,Latias,Latios,Regice,Regirock,Registeel,Kyogre,Groudon,Entei,Suicune,Raikou],k=1)
    if trname is None and trclass not in ["Elder Trainer","Dojo Master",",Blackbelt", "Egyptian","Exorcist"]:
        namelist=["Josh","Kyler","Jade","John","Joey","Jan","Gabriel","Jamie","Kylie","Andrea","Evy","Ebba","Titus","Emiliano","Emilia","Natalie","Justin","Anastasia","Frannie","Danielle","Daniel","Hugo","Robert","Carlos","Alex","Alexander","Alexandra","Arslan","Johan","Mike","Julian","Selena","Emmanuel","Kristin","Lawrence","Frank","Pamela","Nicole","Emma","Matthew","Catherine","Jackson","Jenna","Sebastian","Sophia","Gav","Lorenzo","Merdith","Nora","Beth","Chelsea","Katelyn","Logan","Madelin","Nicolas","Trenton","Allison","Ashlee","Deshawn","Dwayne","Felicia","Jeffery","Krista","Taylor","Annie","Audra","Brenda","Claude","Chloris","Crofton","Eliza","Harry","Irene","Jaden","Keith","Lewis","Mary","Miguel","Mylene","Pedro","Ralph","Richard","Shanti","Thalia","Anja","Bret","Briana","Daryl","Dianna","Eddie","Elie","Elaine","Forrest","Heidl","Hillary","Johan","Sophie","Lena","Lois","Malory","Maxwell","Melita","Mikiko","Naoko","Parker","Rick","Serenity","Steve","Ambre","Bjorn","Brooke","Chaise","Lee","Dean","Clementine","Maurice","Melina","Nash","Petra","Reed","Ralf","Shinobu","Silas","Twiggy","Kira","Dirk","Bobby","Danny","Caleb","Dylan","Thomas","Daniel","Jeff","Braven","Dell","Neagle","Haruki","Mitchell","Sheriff","Raymond","Cole","Edgar","Evan","Jason","Phil","Vincent","Yoshinari","Georges","Morris","Jacopo","Anette","Brianna","Cindy","Colleen","Daphne","Elizabeth","Naomi","Sarah","Charlotte","Gillian","Jacki","Selphy","Melissa","Celeste","Elizendra","Isabella","Magnolia","Lynette","Colette","Lina","Dulcie","Auro","Brin","Eloos","Caril","Kowly","Illa","Rima","Ristin","Vesey","Brenna","Deasy","Denslon","Kylet","Nemi","Rene","Sanol","Sturk","Talmen","Zolla"]
        nn=random.choice(namelist)
        new_name=trclass+" "+nn
        #STEEL
    if trclass in ["Factory Boss","Industry Worker"]:
        mons=[Revavroom,Gholdengo,Tinkaton,Orthworm,Kingambit,Irontreads,Mawile,ADugtrio,ASandslash,Duraludon,Copperajah,Perrserker,Corviknight,Dhelmise,HGoodra,Aegislash,Bisharp,Magnezone,Steelix,MSteelix,Scizor,MScizor,Skarmory,MMawile,Aggron,MAggron,Metagross,MMetagross,Empoleon,Bastiodon,Bronzong,Lucario,MLucario,Probopass,Heatran,Excadrill,Ferrothorn,Escavalier]
        #Ghost
    if trclass == "Exorcist":
        namelist=["Gabrielle","Candido","Bishop","William","Bowden","Joseph","Thomas","Fantino","Angelo"]
        nn=random.choice(namelist)
        new_name=trclass+" "+nn
        mons=[Ceruledge,Houndstone,Anihilape,Skeledirge,Fluttermane,GCorsola,AMarowak,Dragapult,Polteageist,Mimikyu,Decidueye,Gourgeist,Aegislash,Trevenant,Golurk,Gengar,MGengar,HTyphlosion,MSableye,Banette,MBanette,Dusknoir,Drifblim,Mismagius,Spiritomb,Froslass,Cofagrigus,Runerigus,HZoroark,Jellicent,Chandelure]
        #Psychic
    if trclass == "Psychic":
        mons=[Musharna,Armarouge,Espathra,Veluza,Screamtail,Grumpig,Wobbuffet,Slowking,Xatu,MrMime,Hypno,Indeedee,GSlowking,GSlowbro,GRapidash,Wyrdeer,Malamar,Delphox,HBraviary,Alakazam,MAlakazam,Slowbro,MSlowbro,Exeggutor,Starmie,Jynx,Espeon,Farigiraf,Gardevoir,MGardevoir,Medicham,MMedicham,Lunatone,Solrock,Claydol,Metagross,MMetagross, Bronzong,Gallade,MGallade,Gothitelle,Reuniclus]
        #Grass
    if trclass == "Gardener":
        mons=[Simisage,Scovillain,Brutebonnet,Arboliva,Whimsicott,Toedscruel,Meowscarada,Leafeon,Cherrim,Tropius,Cacturne,Sunflora,Jumpluff, Bellossom,Parasect,Vileplume,Flapple,Appletun,Rillaboom,Dhelmise,Tsareena,HElectrode,HDecidueye,Gourgeist,Decidueye,Trevenant,Gogoat,Florges,Venusaur,MVenusaur,Victreebel,Exeggutor,AExeggutor,Tangrowth,Meganium,Sceptile,MSceptile,Ludicolo,Shiftry,Breloom,Roserade,Cradily,Torterra,Abomasnow,MAbomasnow,Serperior,Leavanny,HLilligant,Ferrothorn]+random.choices([Shaymin,SShaymin],k=1)
    if trclass in ["Chef","MasterChef","Cook","Foodie"]:
        mons=[Dachsbun,Slurpuff, Vanilluxe,Tropius,Polteageist, Alcremie,Miltank,Shuckle,Coalossal,Tsareena,Appletun,MAbomasnow,MAudino,MBlaziken]
    if trclass in ["Pokémon Ranger","Camper"]:
        mons=[Shiftry,Ludicolo, Bellossom,Roserade,Breloom,Cacturne,Altaria,MAltaria,Dusclops, Mismagius,Gengar,MGengar,Sunflora, Tangrowth, Venusaur,MVenusaur,Forretress,Electrode, Exeggutor, Victreebel,Starmie,Ledian,Blissey, Vileplume, Arcanine,Gyarados,Ambipom, Azumarill,Linoone, Skarmory, Lickilicky,Donphan,Empoleon,Flygon,Ursaring,Luxray,Floatzel,Leafeon,Arbok, Butterfree, Granbull,Jumpluff, MLopunny ,Infernape,Aggron,Marowak, Zangoose, Poliwrath, Dewgong, Steelix,MSteelix,Simisage,Simisear,Simipour,Swoobat, Zebstrika, Pinsir,MPinsir,Emolga, Pelipper, Vanilluxe, Musharna,Stoutland,Haxorus, Drifblim,Umbreon,Beartic, Leavanny, Unfezant,Seismitoad, Swanna,Mantine,Rapidash, MAbomasnow,Abomasnow, Magmortar, Wigglytuff,Farigiraf,Excadrill,Jolteon,Probopass,Galvantula,Volcarona,Flareon, Electivire,Accelgor,Swalot, Camerupt,MCamerupt,Banette,MBanette,Golduck,Krookodile, Sudowoodo, Cradily, Scolipede, Lucario,MLucario, Watchog,Grumpig,Ampharos,MAmpharos, Kricketune,Snorlax, Armaldo, Gliscor, Skuntank,Escavalier,Slaking,Wyrdeer, Sirfetchd,Garbodor, Amoongus,Goodra,Kingdra,Crawdaunt,Sandslash,Garchomp,MGarchomp, Ferrothorn,Pyroar,Crobat,Slowbro,Exploud,Quagsire,Manectric, MManectric ,Pikachu,Raichu, Seviper]
        #BUG
    if trclass in ["Bug Catcher","Bug Researcher"]:
        if "Hoenn" in field.location:
            mons=[Shuckle,Forretress,Ariados,Ledian,Scyther,Venomoth,Parasect,Butterfree,Beedrill,Scizor,Heracross,Pinsir,Shedinja,Ninjask,Masquerain,Beautifly,Dustox,MScizor,MHeracross,MPinsir,MBeedrill]
        if "Johto" in field.location:
            mons=[Shuckle,Forretress,Ariados,Ledian,Scyther,Venomoth,Parasect,Butterfree,Beedrill,Scizor,Heracross,Pinsir,MScizor,MHeracross,MPinsir,MBeedrill]
        else:
            mons=[Rabsca,Ironmoth,Spidops,Lokix,Slitherwing,Wormadam,Mothim,TWormadam,SWormadam,Kricketune,Shuckle,Forretress,Ariados,Ledian,Scyther,Venomoth,Parasect,Butterfree,Beedrill,Frosmoth,Kleavor,Centiskorch,Orbeetle,Golisopod,Araquanid,Vikavolt,Volcarona,Durant,Accelgor,Galvantula,Escavalier,Scolipede,Leavanny,Scizor,Heracross,Pinsir,Drapion,Vespiquen,Yanmega,MScizor,MHeracross,MPinsir,MBeedrill]        
        #ICE SPECIALISTS
    if trclass in ["Skier","Boarder"]:
        mons=[Ironbundle,Cryogonal,Baxcalibur,Ironbundle,Glaceon,Delibird,ASandslash,Cetitan,Frosmoth,MrRime,Avalugg,HAvalugg,Aurorus,Beartic,Vanilluxe,GDarmanitan,Weavile,Abomasnow,Walrein,Lapras,Mamoswine,Glalie,MGlalie,Jynx,Cloyster,ANinetales,MAbomasnow]
        ch=random.randint(1,10)
        if ch==7:
            mons+=[Articuno]
    if trclass in ["Breeder"]:
     mons=[Pikachu,Raichu, Wigglytuff, Clefable,Blissey,Sudowoodo,Electivire, Magmortar,Jynx, MCharizardY, MBlastoise, MVenusaur]
#ROCK SPECIALISTS
    if trclass in ["Ruin Explorer","Hiker","Backpacker"]:
     mons=[Glimmora,Garganacl,Ironthorns,Klawf,Sudowoodo,Rhydon,Coalossal,Gigalith,Lunatone,Solrock,Probopass,HArcanine,Runerigus,Cofagrigus,MTyranitar,MAggron,Rhyperior,Aggron,Steelix,Machamp,Tyranitar,Golem]
#fossil
    if trclass in ["Fossil Maniac","Paleontologist"]:
        mons=[Dracovish,Dracozolt,Tyrantrum,Aurorus,Archeops,Carracosta,Omastar,Kabutops,MAerodactyl,Armaldo,Cradily,Aerodactyl,Mamoswine,Bastiodon,Rampardos,Relicanth]
#Ground
    if trclass in ["Desert Explorer","Egyptian"]:
        if trclass=="Egyptian":
            namelist=["Wongani","Abdelhamid","Ali","Zafar","Saif","Hakeem","Ziyad","Hamed","Daud","Apis","Amon","Aton"]
            nn=random.choice(namelist)
            new_name=trclass+" "+nn
        mons=[Clodsire,Toedscruel,Sandyshocks,Greattusk,Cacturne,Donphan,Quagsire,Rhydon,Marowak,Dugtrio,ADugtrio,Sandslash,Sandaconda,Palossand,Mudsdale,Mandibuzz,Golurk,Drapion,Camerupt,MCamerupt,Hippowdon,Nidoking,Nidoqueen,Golem,Gliscor,Steelix,MSteelix,Rhyperior,Mamoswine,Swampert,MSwampert,Flygon,Whiscash,Claydol,Torkoal,Torterra,EGastrodon,WGastrodon,Garchomp,MGarchomp,Seismitoad,Krookodile,Excadrill,Arbok]
#WATER SPECIALISTS
    if trclass in ["Marine Biologist","Surfer","Scuba Diver","Swimmer","Sailor","Captain","Pirate","Fisherman"]:
        mons=[Tatsugiri,Simisage,Dondozo,Palafin,Wugtrio,Quaquaval,Ironbundle,Lumineon,Floatzel,Bibarel,Mantine,Corsola,Slowking,Quagsire,Seaking,Kingler,Dracovish,Barraskewda,Inteleon,Araquanid,Toxapex,SWishiwashi,Primarina,Clawitzer,Barbaracle,Greninja,Jellicent,Swanna,Carracosta,Basculegion,Seismitoad,HSamurott,Samurott,MSharpedo,MSwampert,MBlastoise,Phione,EGastrodon,WGastrodon,Empoleon,Walrein,Huntail,Gorebyss,Relicanth,Milotic,Crawdaunt,Whiscash,Dewgong,Sharpedo,Pelipper,Kingdra,Politoed,Azumarill,Feraligatr,Lanturn,Lapras,Gyarados,Slowbro,Cloyster,Starmie, Blastoise,Poliwrath,Swampert,Ludicolo]+random.choices([Manaphy, Wailord],k=1)
#GRUNTS
    if trclass in ["Flare Grunt"]:
        mons=[]
    if trclass in ["Shadow Triads"]:
        mons=[Absol, Kingambit, Bisharp,MBanette,Accelgor,HLilligant,Volcarona, Basculegion]
    if trclass in ["Plasma Grunt"]:
        mons=[Watchog,Liepard,Krookodile, Scrafty, Garbodor,Crobat,Seviper,Weezing,Raticate,Drapion, Kingambit, Hydreigon,Weavile,Bisharp, Scolipede, Amoongus,Magnezone,Muk,Zangoose, Genesect,Metagross, Gigalith,Mandibuzz,Seismitoad,MHoundoom,MMedicham,MHeracross,MGallade]
    if trclass in ["Aqua Grunt"]:
        mons=[Crawdaunt,Sharpedo,Crobat,Mightyena,Muk,Weezing,Tentacruel,Wailord,MSharpedo,Walrein,Dusclops, Ludicolo,Seviper]
    if trclass in ["Magma Grunt"]:
        mons=[Camerupt,Torkoal,Crobat,Mightyena,Muk,Weezing,Magmortar,MCamerupt,Claydol,Houndoom,Magcargo,Sandslash, Salamence,Banette,Aggron, Zangoose]
    if trclass in ["Rocket Grunt"]:
        mons=[Arbok,Weezing,Victreebel,Muk,Crobat,Seviper,Houndoom,Yanmega, Machamp,MHoundoom,Raticate,Sandslash,Persian,Hypno,Marowak, Vileplume,Electrode,Gengar,Magnezone, Rhyperior, Skarmory,Tauros,Golem,Rhydon,Dodrio,Purugly,Toxicroak,Skuntank]
    if trclass in ["Galactic Grunt"]:
        mons=[Purugly,Skuntank,Weavile,Bronzong,Crobat,Toxicroak,Muk,Weezing,Magnezone,Electivire,Magmortar,Rhyperior,Probopass,Gyarados,MSableye]
#DRAGON SPECIALISTS
    if trclass in ["Dragon Tamer"]:
        mons=[Cyclizar,Baxcalibur,Roaringmoon,Dragapult,Duraludon,Dracovish,Dracozolt,Flapple,Appletun,MSceptile,Kommo,Drampa,Turtonator,Noivern,HGoodra,Goodra,Hydreigon,Druddigon,Haxorus,Krookodile,Serperior,Yanmega,Garchomp,MGarchomp,Gyarados,MGyarados,Dragonite,Kingdra,Charizard,Aerodactyl,Tyranitar, Salamence,MSalamence,MAerodactyl,MCharizardX,MTyranitar,Feraligatr]+random.choices([Latias,Latios,MLatias,MLatios],k=1)
    if trclass in ["Police Officer","Investigator","Policeman"]:
        mons=[Noctowl,Machamp,Medicham, MMedicham, Arcanine, HArcanine, Stoutland, Mienshao, Lucario, MLucario, Boltund,Ariados, Bastiodon]
#POISON SPECIALISTS
    if trclass in ["Venom Expert"]:
        mons=[Revavroom,Clodsire,Ironmoth,Grafaiai,Garbodor,Dustox,Swalot,Venomoth,Vileplume,Toxtricity,GSlowking,GWeezing,GSlowbro,Salazzle,Sneasler,Dragalge,Toxicroak,Drapion,Roserade,Seviper,Arbok,Weezing,Crobat,MBeedrill,Venusaur,Nidoking,Nidoqueen,Victreebel,Tentacruel,Muk,Gengar,Overqwil,MVenusaur]
#ELECTRIC
    if trclass in ["Rocker","Guitarist","Electrician"]:
        mons=[Pincurchin,Boltund,Pawmot,Kilowattrel,Ironthorns,Ironhands,Sandyshocks,Bellibolt,Pachirisu,Manectric,Electrode,Raichu,ARaichu,Pikachu,Dracozolt,Toxtricity,Vikavolt,HElectrode,Eelektross,Galvantula,MManectric,AGolem,Magnezone,Jolteon,Electivire,Lanturn,Ampharos,MAmpharos,Luxray,WRotom,Zebstrika]        
#FIRE SPECIALISTS
    if trclass in ["Kindler","Fiery Breathe","Volcano Explorer"]:
        mons=[Simisear,Scovillain,Skeledirge,Ironmoth,Ceruledge,Armarouge,Magcargo,AMarowak,Centiskorch,Coalossal,Cinderace,Turtonator,Salazzle,Incineroar,Pyroar,Talonflame,Delphox,Volcarona,Heatmor,Chandelure,Darmanitan,HTyphlosion,Emboar,HArcanine,Magmortar,Infernape,Arcanine,Rapidash,Houndoom,Flareon,Typhlosion,Blaziken,Camerupt,Charizard,MCharizardY,MHoundoom,MCamerupt]
#FLYING SPECIALISTS
    if trclass in ["Bird Keeper","Pilot","Sky Diver"]:
        mons=[Flamigo,Kilowattrel,Bombirdier,Ironjugulis,Xatu,Noctowl,Corviknight,Toucannon,Hawlucha,Talonflame,Mandibuzz,HBraviary,Braviary,Swanna,Archeops,Unfezant,Gliscor,Togekiss,Honchkrow,Staraptor,Pelipper,Swellow,MPidgeot,Charizard,Skarmory,Altaria,Crobat,Dodrio,MSalamence]
        mons+=random.choices([Articuno,Zapdos,Moltres,Thundurus,Landorus,Tornadus,Enamorus],k=1)      
    if trclass in ["Scientist","Super Nerd"]:
        mons=[Electrode,Magnezone,Metagross,Klinklang, Alakazam,MAlakazam,MMetagross, Revavroom,Irontreads,Electivire,WRotom,Ironhands, Ironthorns,Ironvaliant,Ironbundle, Ironjugulis,Ironmoth]
        #DECENT TRAINERS
    if trclass in ["Expert","Veteran","Businessman","Gentleman"]:
        mons=[Audino,Dudunsparce,Noctowl,Furret,Ditto,Chansey,Persian,Vileplume,Wigglytuff,Clefable,Pikachu,Raticate,ARaticate,Butterfree,Beedrill,MDLycanroc,MNLycanroc,DLycanroc,Aegislash,Delphox,Greninja,Chesnaught,Basculegion,Stoutland,Probopass,Ursaluna,Yanmega,Magnezone,Tangrowth,Hippowdon,Lucario,Mismagius,Luxray,Roserade,Torterra,Glalie,Absol,Banette,Milotic,Armaldo,Cradily,Aggron,Hariyama,Breloom,Gardevoir,Swellow,Ludicolo,Swampert,Houndoom,Heracross,Steelix,Espeon,Ampharos,Flareon,Jolteon,Vaporeon,Snorlax,Lapras,Gyarados,Tauros,Kangaskhan,Hitmonchan,Hitmonlee,Exeggutor,Gengar,Dodrio,Slowbro,Rapidash,AGolem,Victreebel,Machamp,Golduck,Alakazam,Pidgeot,Blastoise,Ninetales,Primeape,MBeedrill, Venusaur, Charizard,Cloyster,MBanette,MGlalie]
        ch=random.randint(1,15)
        if ch==7:
            mons+=random.choices(legendary,k=1)
        pass
    if trclass in[ "Chaos Trainer"]:
        mons=[Gremlid,Deigon,MFlygon,Gorochu,Salobber,Terryena,Malevorus, TMalevorus, UTyranitar,Medicrow,Cochungus,Bustoliv,Bombeedel, Mollonce, Machug, Doncrete,Dangal, Ajjimajji, Spinestial]
        
    if trclass in[ "Beauty","Lass"]:
        namelist=["Alexa","Andrea","Georgia","Emma","Rose","Kimmy","Layla","Stephanie","Alexandra","Kylie"]
        mons=[Wigglytuff,Blissey,MAudino,Swanna,Sylveon,Whimsicott, Alcremie,Slurpuff,Tsareena,Azumarill,GRapidash, Vileplume,Vaporeon,Cloyster, Bellossom, Seaking,Starmie,Clefable,Togekiss, Gardevoir,MGardevoir,Mawile,MMawile,Altaria,MAltaria,Florges,Klefki,Primarina, Hatterene,Dachsbun,Screamtail,Fluttermane,Tinkaton]
#THUGS
    if trclass in[ "Street Punk","Biker","Cueball","Smuggler","Thief","Goon","Driver"]:
        namelist=["Charles","Dwayne","Glenn","Harris","Joel","Riley","Zeke","Alex","Billy","Ernest","Gerald","Hideo","Isaac","Jared","Jaren","Jaxon","Jordy","Lao","Lucas","Nikolas","Ricardo","Ruben","Virgil","William","Aiden","Charles","Dale","Dan","Markey","Reese","Teddy","Theron","Jeremy","Morgann","Philip","Stanley","Dillon"]
        nn=random.choice(namelist)
        new_name=trclass+" "+nn
        mons=[Weezing,Muk, Electrode,Charizard, Flareon, Magmortar,Togekiss, MCharizardY, Forretress, Hypno, Tentacruel,Swalot, Ursaring, Drapion,Arbok,Seviper, Toxicroak, Galvantula, Scrafty, Krookodile, Bouffalant, Bisharp, Kingambit, Crobat,Conkeldurr, Nidoking, Nidoqueen, Hitmonlee, Machamp, Primeape, Hitmonchan, Venomoth, Poliwrath, Anihilape, Beedrill,MBeedrill, Kingdra, Kangaskhan, MKangaskhan, Kabutops,Jynx,Ariados, Dudunsparce, Ampharos, Skarmory, Cloyster, Venusaur, Rhydon, Victreebel, Skarmory, Miltank, Vaporeon, Parasect,Steelix, MSteelix]
        ch=random.randint(1,10)
        if ch==7:
            mons+=random.choices(legendary,k=1)

    if trclass == "Air Force Officer":
        mons=[Skarmory,Corviknight,Magnezone,Latios,Latias,Pidgeot,Staraptor,Braviary,Altaria,MAltaria,Dragonite,Salamence,Metagross,MSalamence]
    if trclass == "Navy Officer":
        mons=[Gyarados,Blastoise,Swampert,Feraligatr,Inteleon,Wailord,Starmie,MBlastoise,MSwampert]
    if trclass == "Military Officer":
        mons=[Aggron,Salamence,Tyranitar,Steelix,Rhyperior,Magnezone,Metagross,Dragonite,Magmortar,Electivire,Charizard, Blastoise,MAggron,MCharizardY, MBlastoise,MMetagross]
    if trclass == "Tamer":
        mons=[Anihilape,Ursaring,Granbull,GRapidash,Bewear,MDLycanroc,MNLycanroc,DLycanroc,Wyrdeer,Pangoro,Braviary,Tauros,Arbok,Arcanine,HArcanine,Rapidash,Ambipom,Ursaluna,Mamoswine,Houndoom,MHoundoom,Mightyena,Slaking,MManectric,Sharpedo,MSharpedo,Wailord,Zangoose,Seviper,Milotic,Absol,MAbsol,Walrein,Empoleon,Infernape,Luxray]+random.choices([Raikou,Suicune,Entei,Cobalion,Virizion,Terrakion])
            
     #BETTER TRAINERS
    if trclass in ["Ace Trainer","Cool Trainer"]:
        mons=[Victreebel, Vileplume, Venusaur, MVenusaur, Nidoking, Nidoqueen,Sandslash,Dugtrio,Rhydon, Rhyperior, Persian, APersian, Ninetales,ANinetales, Blastoise, MBlastoise, Charizard, MCharizardY, MCharizardX, Exeggutor, Cloyster, Arcanine, HArcanine, Parasect, Dewgong, Blissey,Kingler,Tentacruel, Rapidash, GRapidash, Magnezone, Quagsire, Electrode, Starmie,Butterfree, Bellossom,Kingdra,Flareon, Vaporeon, Jolteon, Seaking,Golduck, Pikachu,Raichu, Azumarill, Jumpluff, Dragonite, Pidgeot,MPidgeot,Electivire, Tangrowth,Tauros,PTauros,Muk,AMuk,Manectric, MManectric, Zangoose, Pelipper, Camerupt, MCamerupt, Roserade,Mawile, MMawile,Sableye, MSableye,Swellow,Flygon,Wailord,Shiftry,Aggron,MAggron,Linoone, Milotic,Delcatty,Medicham, MMedicham, Ludicolo,Golem, Alakazam, MAlakazam,Claydol,Sharpedo, MSharpedo,Dodrio,Magcargo,Hariyama, Wigglytuff, Slaking, Banette,MBanette, Dusclops,Dusknoir,Skarmory, Exploud, Lanturn, Cacturne,Absol,MAbsol,Tropius, Gardevoir, MGardevoir, Solrock,Lunatone, Machamp, Ursaring, Probopass,Tyranitar,MTyranitar,Lapras,Slowbro,MSlowbro, Kangaskhan, MKangaskhan, Farigiraf,Marowak, Raticate, ARaticate, Aerodactyl, MAerodactyl,Weavile,Gengar,MGengar, Torterra, Abomasnow, MAbomasnow,Ambipom,WGastrodon, Pachirisu, Mismagius, Drapion,Steelix,MSteelix, Drifblim, MLopunny, Hippowdon,Gallade,MGallade, Mightyena, Ampharos, MAmpharos, Infernape,Luxray,Gyarados,MGyarados, Salamence, MSalamence,Honchkrow,Staraptor, Metagross, MMetagross,Floatzel, Anihilape, Primeape,Wyrdeer, Sneasler,Purugly,Yanmega, Bibarel, Beautifly,Hypno, Dudunsparce, Scizor,MScizor,Rampardos, Pinsir,MPinsir,Crobat,Glalie,MGlalie,Beedrill,MBeedrill,Typhlosion, Meganium, Feraligatr, Mamoswine, Darmanitan, Klinklang, Whimsicott, Scolipede, Stoutland,Haxorus, Druddigon,Hydreigon, Garchomp, MGarchomp, Zebstrika,Liepard, Beartic, Leavanny, Krookodile, Accelgor,Espeon,Gothitelle,Walrein,Mienshao, Gliscor,WRotom, Magmortar,Chandelure, Galvantula,Golurk,Archeops,Mantine,Umbreon, Excadrill,Swanna,Mandibuzz, Toxicroak, Seismitoad,Cofagrigus,Carracosta,Gorebyss,Huntail,Braviary]
        ch=random.randint(1,5)
        if ch==3:
            mons+=random.choices(legendary,k=1)
            
        
#CHALLENGERS
    if trclass == "Challenger":
        mons=[DUrshifu,WUrshifu,Hatterene,Grimmsnarl,Toxtricity,Appletun,Corviknight,Melmetal,Zeraora,Silvally,Incineroar,Aegislash,Greninja,Volcarona,Hydreigon,Mandibuzz,Bisharp,Mienshao,Ferrothorn,Reuniclus,HZoroark,Zoroark,Darmanitan,GDarmanitan,Krookodile,Conkeldurr,Excadrill,Heatran,Uxie,Mesprit,Azelf,WRotom,Togekiss,Magnezone,Garchomp,Infernape,Latias,Latios,Metagross,Salamence,Slaking,Blissey,Kingdra,Skarmory,Umbreon,Crobat,Cloyster,Starmie,AExeggutor,Typhlosion,Feraligatr,Meganium,Arcanine,Snorlax,Dragonite]+[MSharpedo,MScizor,MSteelix,MGyarados,MKangaskhan,MAlakazam,MPidgeot,MSlowbro,MAerodactyl,MBlastoise,MVenusaur,MCharizardX,MCharizardY,MHeracross,MHoundoom,MSceptile, MBlaziken,MSwampert,MGardevoir,MCamerupt,MAbsol,MSalamence,MMetagross,MLopunny,MLucario]+ultrabeasts
        ch=random.randint(1,3)
        if ch==2:
            mons+=random.choices(legendary,k=3)
        pass


    if len(team)==0 and trclass=="Challenger":
        while len(team)!=pknum:
            party=random.choices(mons)[0]
            member=party( )
            if ("💎" not in member.name and "Gigantamax" not in member.name and "Dynamax " not in member.name and "Mega " not in member.name and "(" not in member.name and "Totem " not in member.name) and len(team)<3:
                team.append(member)
                mons.remove(party)
            if ("Dynamax" in member.name or "Gigantamax" in member.name) and len(team)==3:
                team.append(member)
                mons.remove(party)
            if "Z-Crystal" in member.name and len(team)==4:
                team.append(member)
                mons.remove(party)
            if "Mega " in member.name and len(team)==5:
                team.append(member)
                mons.remove(party)
                
    if len(team)==0 and trclass in ["Expert","Veteran"]:
        while len(team)!=pknum:
            party=random.choices(mons)[0]
            member=party( )
            if ("Gigantamax" not in member.name and "Dynamax " not in member.name and "Mega " not in member.name and "(" not in member.name and "Totem " not in member.name) and len(team)<4:
                team.append(member)
                mons.remove(party)
            if ("Dynamax" in member.name or "Gigantamax" in member.name) and len(team)==4:
                team.append(member)
                mons.remove(party)
            if "Mega " in member.name and len(team)==5:
                team.append(member)
                mons.remove(party)    
            
                
    if len(team)==0 and trclass in ["Ace Trainer","Dragon Tamer"]:
        while len(team)!=pknum:
            party=random.choices(mons)[0]
            member=party( )
            if ("💎" not in member.name and "Gigantamax" not in member.name and "Dynamax " not in member.name and "Mega " not in member.name and "(" not in member.name and "Totem " not in member.name) and len(team)<2:
                team.append(member)
                mons.remove(party)
            if "💎" in member.name and len(team)==2:
                team.append(member)
                mons.remove(party)
            if ("Dynamax" in member.name or "Gigantamax" in member.name) and len(team)==3:
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
            member=party( )
            if ("💎" not in member.name and "Gigantamax" not in member.name and "Dynamax " not in member.name and "Mega " not in member.name and "Z-Crystal" not in member.name and "Totem " not in member.name) and len(team)<7:
                team.append(member)
                mons.remove(party)
            if megachance==2:
                if "Mega " in member.name and len(team)==5:
                    team.append(member)
                    mons.remove(party)
            if megachance==1:
                if "Z-Crystal" in member.name and len(team)==5:
                    team.append(member)
                    mons.remove(party)                                 
                        
    if len(team)==0 and trclass not in ["Challenger","Ace Trainer","Dragon Tamer","Elder Trainer","Veteran","Expert","Cool Trainer"]:
        megachance=0
        if "Paldea" in trclass or "Paldea" in field.location:
            megachance=3
        if "Alola" in trclass or "Alola" in field.location:
            megachance=1
        if "Galar" in trclass or "Galar" in field.location:
            megachance=4
        if "Kalos" in trclass or "Kalos" in  field.location:
            megachance=2
        if megachance==0:
            megachance=random.randint(1,4) 
        while len(team)!=pknum:
            party=random.choices(mons)[0]
            member=party( )
            if ("💎" not in member.name and "Gigantamax" not in member.name and "Dynamax " not in member.name and "Mega " not in member.name and "(" not in member.name and "Totem " not in member.name) and len(team)<5:
                team.append(member)
                mons.remove(party)
            if megachance==4:
                if ("Dynamax" in member.name or "Gigantamax" in member.name) and len(team)==5:
                    team.append(member)
                    mons.remove(party)
            if megachance==3:
                if "💎" in member.name and len(team)==5:
                    team.append(member)
                    mons.remove(party)
            if megachance==1:
                if "Z-Crystal" in member.name and len(team)==5:
                    team.append(member)
                    mons.remove(party)         
            if megachance==2:
                if "Mega " in member.name and len(team)==5:
                    team.append(member)
                    mons.remove(party)        

                                                                                
                     
    return new_name,team            

def genTrainer(trclass=None,name=None,num=6,ai=True):
    trclasslist=["Blackbelt","Dojo Master","Dragon Tamer","Skier","Kindler","Sailor","Swimmer","Veteran","Elder Trainer","Challenger","Ruin Explorer","Ace Trainer","Expert","Street Punk","Scuba Diver","Fossil Maniac","Paleontologist","Surfer","Marine Biologist","Biker","Cueball","Bird Keeper","Pilot","Sky Diver","Venom Expert","Fiery Breathe","Rocker","Guitarist","Bug Catcher","Psychic","Exorcist","Electrician","Smuggler","Thief","Goon","Boarder","Desert Explorer","Egyptian","Tamer","Captain","Pirate","Driver","Magma Grunt","Aqua Grunt","Rocket Grunt","Galactic Grunt","Gardener","Factory Boss","Industry Worker","Hiker","Kanto Trainer","Johto Trainer","Hoenn Trainer","Sinnoh Trainer","Unova Trainer","UB Expert","Businessman","Police Officer","Investigator","Military Officer","Navy Officer","Air Force Officer","Bug Researcher","Fisherman","Chaos Trainer","Plasma Grunt","Shadow Triads","Kalos Trainer","Alola Trainer","Galar Trainer","Chef","MasterChef","Cook","Foodie","Beauty","Gentleman","Camper","Lass","Scientist","Breeder","Pokémon Ranger","Backpacker","Policeman","Super Nerd","Cool Trainer","Pokémon Trainer"]
    rg=random.choice(["Kanto","Hoenn","Johto","Sinnoh","Unova","Kalos","Alola","Galar","Paldea"])
    if trclass is None:
        rclass=random.choice(trclasslist)
    if trclass is not None:
        rclass=trclass
    trainer=teammaker(rclass,name,num)
    rname=trainer[0]
    rteam=trainer[1]
    rand=Trainer(rname,rteam,ai=ai,region=rg)
    return rand
def showparty(obj):
    for i in obj.pokemons:
        i.owner=obj
def showteam(obj):
    num=0
    total=0
    btotal=0
    for i in obj.pokemons:
        total+=i.maxtotal
        btotal+=i.basestats
    print(f"  {obj.name}'s Team [Power:{total}({btotal})]")
    for i in obj.pokemons:
        num+=1
        print("  "+str(num)+".",i.name+f"({i.basestats})")        
def match():
    t1=genTrainer(ai=p1AI)
    t2=genTrainer(ai=p2AI)
    return t1,t2                        
#E4 Bruno
bruno1=MSteelix(maxiv="Yes",move=["Earthquake","Iron Head", "Curse","Gyro Ball"],nature="Brave",ability="Heatproof")
bruno2=Machamp(maxiv="gmax",move=["Knock Off","Close Combat","Stone Edge","Facade"],nature="Adamant", ability="Guts")
bruno3=Hitmonchan(maxiv="Yes",move=["Thunder Punch","Close Combat","Fire Punch","Ice Punch"],nature="Adamant")
bruno4=Hitmonlee(maxiv="Yes",move=["Hi Jump Kick","Knock Off","Close Combat","Stone Edge"],nature="Adamant")
bruno5=Steelix(maxiv="Yes",move=["Earthquake","Iron Head", "Curse","Gyro Ball"],nature="Brave",ability="Heatproof")
bruno6=Poliwrath(name="Poliwrath💎",maxiv="Fighting",move=["Close Combat","Liquidation","Recover","Surging Strikes"],nature="Adamant")
bruno7=Hitmontop(maxiv="Yes")
bruno8=Hariyama(maxiv="Yes")
bruno9=Lucario(maxiv="Yes")
bruno10=AGolem(maxiv="Yes")
brunoteam=teamset([bruno6,bruno2,bruno3,bruno4,bruno5,bruno7,bruno8,bruno9,bruno10],5)+[bruno1]
bruno=Trainer("Elite Four Bruno",brunoteam,"Kanto")
#E4 Lance
lance1=Hydreigon(maxiv="Yes",move=["Dark Pulse","Flamethrower","Thunderbolt","Dragon Pulse"],nature="Modest")
lance2=MGyarados(name="Gyarados✨",maxiv="Yes",move=["Dragon Dance","Waterfall","Earthquake","Ice Fang"],nature="Adamant")
lance3=Aerodactyl(maxiv="Yes",move=["Stone Edge","Earthquake","Roost","Stealth Rock"],nature="Jolly")
lance4=Dragonite (maxiv="gmax",move=["Dragon Dance","Extreme Speed","Dragon Claw","Roost"],nature="Adamant")
lance5=Kingdra(maxiv="Yes",move=["Rain Dance","Draco Meteor","Surf","Ice Beam"],nature="Modest",ability="Swift Swim")
lance6=Charizard(name="Charizard💎",maxiv="Dragon",move=["Dragon Dance","Roost","Dragon Claw","Flare Blitz"],nature="Adamant")
lance=Trainer("Elite Four Lance",[lance1,lance2,lance3,lance6,lance5,lance4])
#E4 Lorelei 
lorelei1=Lapras(maxiv="gmax",move=["Ice Beam","Hydro Pump","Recover","Thunder"],nature="Modest",dmax=True)
lorelei2=MSlowbro(maxiv="Yes",move=["Slack Off","Flamethrower","Hydro Pump","Ice Beam"],nature="Modest")
lorelei3=Dewgong(maxiv="Yes",move=["Ice Beam","Hydro Pump","Recover","Blizzard"],nature="Modest")
lorelei4=Cloyster(maxiv="Yes",move=["Rock Blast","Pin Missile","Icicle Spear","Shell Smash"],nature="Adamant")
lorelei5=Jynx(maxiv="Yes",move=["Ice Beam","Psychic","Recover","Blizzard"],nature="Timid")
lorelei6=Mamoswine(name="Mamoswine(Z-Crystal)",maxiv="Yes",move=["Ice Beam","Earthquake","Stone Edge","Blizzard"],nature="Naughty")
lorelei7=ASandslash(maxiv="Yes")
lorelei=Trainer("Elite Four Lorelei",[lorelei6,lorelei2,lorelei3, lorelei4,lorelei5,lorelei1])
#Red
red7=Pikachu(maxiv="gmax",move=["Extreme Speed","Volt Tackle","Thunderbolt","Electroweb"],nature="Modest")
red1=MCharizardX(maxiv="Yes",move=["Dragon Dance","Dragon Claw","Flare Blitz","Roost"],nature="Jolly")
red2=Blastoise(maxiv="Yes",move=["Hydro Pump","Shell Smash","Water Spout","Ice Beam"],nature="Modest")
red3=Venusaur (maxiv="Yes",move=["Earth Power","Sleep Powder","Sludge Bomb","Giga Drain"],nature="Modest")
red4=Lapras(maxiv="Yes",move=["Hydro Pump","Ice Beam","Thunderbolt","Freeze-Dry"],nature="Modest")
red5=Snorlax(maxiv="Yes",move=["Hyper Beam","Body Slam","Return","Double-Edge"],nature="Relaxed")
red6=Espeon(maxiv="Yes",move=["Psychic","Dazzling Gleam","Morning Sun","Shadow Ball"],nature="Modest")
red8=Mewtwo(maxiv="Yes")
red9=Zapdos(maxiv="Yes")
red10=Moltres(maxiv="Yes")
red11=Articuno(maxiv="Yes")
redteam=teamset([red4,red5,red6,red2,red3,red8,red9,red10],4)+[red7,red1]
red=Trainer("Pokémon Trainer Red",redteam,"Kanto")
#E4 Agatha
agatha1=Crobat(maxiv="Yes",move=["Roost","Toxic","Brave Bird","U-Turn"],nature="Jolly")
agatha2=Mismagius(maxiv="Yes",move=["Thunderbolt","Dazzling Gleam","Shadow Ball","Nasty Plot"],nature="Timid")
agatha3=Arbok(maxiv="Yes",move=["Earthquake","Poison Jab","Crunch","Coil"], nature="Adamant")
agatha4=Weezing(maxiv="Yes",move=["Sludge Bomb","Will-O-Wisp","Flamethrower","Toxic"],nature="Bold")
agatha5=Gengar(maxiv="gmax",move=["Thunderbolt","Sludge Bomb","Shadow Ball","Nasty Plot"],nature="Timid")
agatha6=MGengar(maxiv="Yes",move=["Thunderbolt","Sludge Bomb","Shadow Ball","Nasty Plot"],nature="Timid")
agatha7=AMarowak(maxiv="Yes")
agatha=Trainer("Elite Four Agatha",[agatha1,agatha2,agatha3,agatha4,agatha5,agatha6],"Kanto")
#alsada
alsada1=Screamtail(maxiv="Yes")
alsada2=Slitherwing(maxiv="Yes")
alsada6=Roaringmoon(maxiv="Yes")
alsada4=Fluttermane(maxiv="Yes")
alsada5=Sandyshocks(maxiv="Yes")
alsada3=Greattusk(maxiv="Yes")
alsada7=Brutebonnet(maxiv="Yes")
alsada9=Koraidon(name="Koraidon💎",maxiv=random.choice(["Fighting","Dragon"]),item="Heat Rock",move=["Giga Impact","Bulk Up","Flare Blitz","Collision Course"])
alsadateam=teamset ([alsada1,alsada2,alsada3,alsada4,alsada5,alsada6,alsada7],5)+[alsada9]
alsada=Trainer("Professor Sada",alsadateam,"Paldea")
#alturo
alturo1=Ironhands(maxiv="Yes")
alturo2=Ironmoth(maxiv="Yes")
alturo6=Ironthorns(maxiv="Yes")
alturo4=Ironbundle(maxiv="Yes")
alturo5=Ironjugulis(maxiv="Yes")
alturo3=Irontreads(maxiv="Yes")
alturo9=Miraidon(name="Miraidon💎",maxiv=random.choice(["Electric","Dragon"]))
alturoteam=teamset ([alturo1,alturo2,alturo3,alturo4],4)+teamset([alturo5,alturo6],1)+[alturo9]
alturo=Trainer("Professor Turo",alturoteam,"Paldea")
#Oak
oak1=Tauros(maxiv="Yes")
oak2=Exeggutor(maxiv="Yes")
oak3=Arcanine(maxiv="Yes")
oak4=Gyarados(maxiv="Yes")
oak5=Venusaur(maxiv="Yes")
oak6=Charizard(maxiv="Yes")
oak7=Blastoise(maxiv="Yes")
oak8=Dragonite(maxiv="Yes")
oak9=Mew(name="Mew(Z-Crystal)",move=["Psychic","Transform","Shadow Ball","Aura Sphere"],maxiv="Yes")
oakteam=teamset ([oak1,oak2,oak3,oak4,oak8],4)+teamset([oak5,oak6,oak7],1)+[oak9]
oak=Trainer("Professor Oak",oakteam,"Kanto")
#janine
janine3=Tentacruel(maxiv="Yes")
janine4=Ariados(maxiv="Yes")
janine5=Toxicroak(maxiv="Yes")
janine6=Weezing(maxiv="Yes")
janine7=Venomoth(maxiv="Yes")
janine8=Drapion(maxiv="Yes")
janine9=Crobat(maxiv="Yes")
janineteam=teamset ([janine3,janine4,janine8,janine5,janine6,janine7],5)+[janine9]
janine=Trainer("Gym Leader Janine",janineteam,"Kanto")
#goh
goh1=Heracross(maxiv="Yes")
goh2=Scizor(maxiv="Yes")
goh10=Beedrill(maxiv="Yes")
goh3=Aerodactyl (maxiv="Yes")
goh4=Absol(maxiv="Yes")
goh5=Rillaboom(maxiv="Yes")
goh6=Darmanitan(maxiv="Yes")
goh7=Inteleon(maxiv="Yes")
goh8=Suicune(maxiv="Yes")
goh9=Cinderace(maxiv="gmax")
goh11=Flygon (maxiv="Yes")
goh12=Dewgong (maxiv="Yes")
goh13=Raichu(maxiv="Yes")
goh14=Swellow(maxiv="Yes")
goh15=Pinsir(maxiv="Yes")
goh16=Butterfree (maxiv="Yes")
goh17=Greninja (maxiv="Yes")
goh18=Golurk(maxiv="Yes")
goh19=Exeggutor (maxiv="Yes")
goh20=Hitmonchan(maxiv="Yes")
goh21=Electrode(name="Electrode✨",maxiv="Yes")
goh22=Cloyster (maxiv="Yes")
goh23=Kingdra(maxiv="Yes")
goh24=Altaria(maxiv="Yes")
goh25=Ferrothorn (maxiv="Yes")
goh26=AExeggutor (maxiv="Yes")
goh27=Shedinja (maxiv="Yes")
goh28=Regieleki(maxiv="Yes")
gohteam=teamset ([goh1, goh2,goh3,goh4,goh5,goh6,goh7,goh10,goh11,goh12,goh13,goh14,goh15,goh16,goh17,goh18,goh19,goh20,goh21,goh22,goh23,goh24,goh25,goh26,goh27],3)+[goh8,goh28,goh9]
goh=Trainer("Pokémon Trainer Goh",gohteam,"Kanto")
#Champion Steven
steven1=Claydol(maxiv="Yes",move=["Sandstorm","Ancient Power","Psychic","Calm Mind"],nature="Bold")
steven2=Armaldo(maxiv="Yes",move=["X-Scissor","Stone Edge","Earthquake","Ancient Power"],nature="Adamant")
steven3=Cradily (maxiv="Yes",move=["Giga Drain","Leech Seed","Strength Sap","Ancient Power"],nature="Modest")
steven4=Skarmory(maxiv="Yes",move=["Brave Bird","Roost","Body Press","Stealth Rock"],nature="Impish")
steven5=Aggron(maxiv="gmax",move=["Body Press","Iron Head","Iron Defense","Stone Edge"],nature="Impish")
steven6=MMetagross(name="Mega Metagross✨",maxiv="Yes", move=["Zen Headbutt","Earthquake","Meteor Mash","Fire Punch"],nature="Adamant")
steven7=Diancie(maxiv="Yes")
steven8=Excadrill(maxiv="Yes")
steven9=Aerodactyl(maxiv="Yes")
steven10=Archeops(maxiv="Yes")
steventeam=teamset([steven1,steven2,steven3,steven4,steven5,steven7,steven8,steven9,steven10],5)+[steven6]
steven=Trainer("Hoenn Champion Steven", steventeam,"Hoenn")
#Champion Wallace
wallace1=Ludicolo(maxiv="Yes",move=["Energy Ball","Scald","Ice Beam","Fake Out"], ability="Swift Swim",item="Life Orb")
wallace2=Starmie(maxiv="Yes",move=["Psychic","Recover","Surf","Thunderbolt"],nature="Timid",item="Expert Belt")
wallace3=Wailord(maxiv="Yes",move=["Water Spout","Blizzard","Earthquake","Heavy Slam"], ability="Blubber Defense")
wallace4=Gyarados(maxiv="Yes",move=["Ice Fang","Waterfall","Stone Edge","Crunch"],nature="Adamant", ability="Intimidate")
wallace5=MSwampert(maxiv="Yes",move=["Earthquake","Liquidation","Ice Punch","Hammer Arm"],nature="Adamant")
wallace6=Milotic(maxiv="gmax",move=["Hydro Pump","Recover","Dragon Pulse","Blizzard"],nature="Modest",ability="Marvel Scale",item="Rocky Helmet")
wallace7=Walrein(maxiv="Yes",item="Leftovers",move=["Surf","Yawn","Blizzard","Sheer Cold"])
wallace8=Seaking(maxiv="Yes")
wallace9=Sharpedo(maxiv="Yes",item="Focus Sash",move=["Hydro Pump","Crunch","Zen Headbutt","Aqua Jet"], ability="Rough Skin")
wallace10=Whiscash(maxiv="Yes", ability="Oblivious",move=["Earthquake","Muddy Water","Rock Tomb","Rain Dance"],item="Damp Rock")
wallace11=Tentacruel(maxiv="Yes", ability="Clear Body",move=["Sludge Wave","Rain Dance","Dazzling Gleam","Scald"])
wallaceteam=teamset([wallace1,wallace2,wallace3,wallace4,wallace5,wallace7,wallace8,wallace9,wallace10,wallace11],5)+[wallace6]
wallace=Trainer("Hoenn Champion Wallace",wallaceteam,"Hoenn")
#Tobias
tobias1=Darkrai(maxiv="gmax",move=["Dark Void","Shadow Ball","Dark Pulse","Psychic"],nature="Modest")
tobias2=MLatios(maxiv="Yes",move=["Luster Purge","Dragon Pulse","Calm Mind","Shadow Ball"],nature="Timid")
tobias3=Entei(maxiv="Yes",move=["Lava Plume","Stone Edge","Flare Blitz","Fire Blast"],nature="Hasty")
tobias4=Heatran(maxiv="Yes",move=["Magma Storm","Flash Cannon","Ancient Power","Earth Power"],nature="Calm")
tobias5=Latias(maxiv="Yes",move=["Mist Ball","Dragon Pulse","Calm Mind","Shadow Ball"],nature="Timid")
tobias6=Cresselia(maxiv="Yes",move=["Lunar Blessing","Moonblast","Psychic","Shadow Ball"],nature="Calm")
tobias=Trainer("Pokémon Trainer Tobias",[tobias3,tobias4,tobias5,tobias6,tobias1,tobias2],"Sinnoh")
#Champion Cynthia
cynthia1=WGastrodon(maxiv="Yes",move=["Earthquake","Scald","Sludge Bomb","Rock Tomb"],nature="Calm",item="Leftovers", ability="Storm Drain")
cynthia2=Togekiss(maxiv="gmax",move=["Air Slash","Thunder Wave","Moonblast","Aura Sphere"],nature="Modest", ability="Serene Grace",item="Leftovers")
cynthia3=Lucario(maxiv="Yes",move=["Close Combat","Meteor Mash","Earthquake","Extreme Speed"],nature="Adamant", ability="Inner Focus",item="Focus Sash")
cynthia4=Milotic(maxiv="Yes",move=["Ice Beam","Mirror Coat","Recover","Scald"],nature="Calm", ability="Marvel Scale",item="Flame Orb")
cynthia5=Roserade(maxiv="Yes",move=["Dazzling Gleam","Shadow Ball","Sludge Bomb","Energy Ball"], nature="Modest",item="Expert Belt")
cynthia6=MGarchomp(maxiv="Yes",move=["Dragon Claw","Swords Dance","Poison Jab","Earthquake"],nature="Jolly")
cynthia8=Glaceon(maxiv="Yes")
cynthia7=Rayquaza (maxiv="Yes")
cynthia9=Altaria (maxiv="Yes")
cynthia10=Lickilicky (maxiv="Yes")
cynthia11=Spiritomb(maxiv="Yes",move=["Shadow Ball","Sucker Punch","Will-O-Wisp","Dark Pulse"], nature="Modest",item="Sitrus Berry")
cynthia12=PorygonZ(maxiv="Yes",move=["Hyper Beam","Shadow Ball","Ice Beam","Thunderbolt"], nature="Modest",item="Expert Belt")
cynthiateam=teamset([cynthia1,cynthia2,cynthia3,cynthia4,cynthia5,cynthia11, cynthia12],5)+[cynthia6]
cynthia=Trainer("Sinnoh Champion Cynthia", cynthiateam,"Sinnoh")
#E4 Aaron
aaron1=Yanmega(maxiv="Yes",move=["Air Slash","Bug Buzz","Signal Beam","Ancient Power"],nature="Modest")
aaron2=Vespiquen(maxiv="Yes",move=["Attack Order","Heal Order","Defense Order","Bug Buzz"],nature="Modest")
aaron3=Scizor(maxiv="Yes",move=["U-Turn","Superpower","Bullet Punch","Roost"],nature="Adamant")
aaron4=MHeracross(maxiv="Yes",move=["U-Turn","Close Combat","Megahorn","Brick Break"],nature="Adamant")
aaron5=Flygon(name="Flygon💎",maxiv="Bug",move=["Earthquake","Dragon Claw","Dragon Dance","Tera Blast"], nature="Jolly")
aaron7=Armaldo(maxiv="Yes")
aaron6=Drapion(maxiv="gmax",move=["Wicked Blow","Toxic","Crunch","Cross Poison"],nature="Adamant")
aaron=Trainer("Elite Four Aaron",[aaron1,aaron2,aaron3,aaron4,aaron5,aaron6],"Sinnoh")
#Bertha
bertha1=Golem(maxiv="Yes")
bertha2=Hippowdon(maxiv="Yes")
bertha3=Gliscor(maxiv="Yes")
bertha4=Nidoking (maxiv="Yes")
bertha5=Mamoswine(maxiv="Yes")
bertha6=Rhyperior(maxiv="gmax")
bertha7=MSteelix(maxiv="Yes")
bertha=Trainer("Elite Four Bertha",[bertha1,bertha2,bertha3,bertha4,bertha7,bertha6],"Sinnoh")
#rika
rika1=Camerupt(maxiv="Yes")
rika2=Whiscash(maxiv="Yes")
rika3=Donphan(maxiv="Yes")
rika4=Dugtrio(maxiv="Yes")
rika5=Greattusk(maxiv="gmax")
rika6=Clodsire(name="Clodsire💎",maxiv="Ground")
rika7=Irontreads(maxiv="gmax")
rikateam=teamset([rika1,rika2,rika3,rika4,rika6],5)+teamset([rika5,rika7],1)
rika=Trainer("Elite Four Rika",rikateam,"Paldea")
#Flint
flint1=Rapidash(maxiv="Yes", ability="Flame Body")
flint2=Entei(maxiv="Yes", ability="Inner Focus")
flint3=Magmortar(maxiv="Yes",ability="Flame Body",item=random.choice(["Lum Berry","Sitrus Berry"]))
flint4=MHoundoom(maxiv="Yes")
flint5=Arcanine(maxiv="Yes",ability="Intimidate")
flint6=Infernape(maxiv="gmax", ability="Iron Fist",item="Focus Sash",move=["Thunder Punch","Fire Punch","Close Combat","Mach Punch"])
flint7=Lopunny(maxiv="Yes",item="Leftovers")
flint8=Drifblim(maxiv="Yes",ability="Unburden",item="Sitrus Berry")
flint9=Steelix(maxiv="Yes", ability="Sheer Force",item="Life Orb")
flint10=Flareon(maxiv="Yes", ability="Flash Fire")
flint11=Ninetales(maxiv="Grass", ability="Drought",item="Heat Rock")
flint12=HRotom(maxiv="Yes")
flint13=Blaziken(maxiv="Yes", ability="Speed Boost")
flintteam=teamset([flint1,flint2,flint3,flint4,flint5,flint7,flint8,flint9,flint10,flint11,flint12,flint13],5)+[flint6]
flint=Trainer("Elite Four Flint",flintteam,"Sinnoh")
#Lucian
lucian1=Farigiraf(maxiv="Yes")
lucian2=Espeon(maxiv="Yes")
lucian3=Bronzong(maxiv="Yes")
lucian4=Alakazam(maxiv="gmax")
lucian5=Slowbro(maxiv="Yes")
lucian6=MGallade(maxiv="Yes")
lucian=Trainer("Elite Four Lucian",[lucian1,lucian2,lucian3,lucian4,lucian5,lucian6],"Sinnoh")
#Buck
buck1=Regice(maxiv="Yes")
buck2=Regirock(maxiv="Yes")
buck3=Registeel(maxiv="Yes")
buck4=Cresselia(maxiv="gmax")
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
palmer6=Regigigas(maxiv="gmax")
palmer=Trainer("Tower Tycoon Palmer",[palmer1,palmer2,palmer3,palmer4,palmer5,palmer6],"Sinnoh")
#Thorton
Thorton1=Bronzong(maxiv="Yes")
Thorton2=Ursaluna(maxiv="Yes")
Thorton3=Ledian(maxiv="Yes")
Thorton4=Electivire(maxiv="Yes")
Thorton5=Skarmory(maxiv="Yes")
Thorton6=MTyranitar(maxiv="Yes")
Thorton=Trainer("Factory Head Thorton",[Thorton1,Thorton2,Thorton3,Thorton4,Thorton5,Thorton6],"Sinnoh")
#noland
noland1=Breloom(maxiv="Yes")
noland2=Rhyperior(maxiv="Yes")
noland3=Machamp(maxiv="Yes")
noland4=Venusaur(maxiv="Yes")
noland5=Articuno(maxiv="Yes")
noland6=MPinsir(maxiv="Yes")
noland7=Aggron(maxiv="Yes")
noland8=Camerupt(maxiv="Yes")
noland9=Sandslash(maxiv="Yes")
noland10=Golduck(maxiv="Yes")
noland11=Manectric(maxiv="Yes")
noland12=Flygon(maxiv="Yes")
nolandteam=teamset([noland1,noland2,noland3,noland4,noland5,noland7,noland10,noland11,noland12,noland8,noland9],5)+[noland6]
noland=Trainer("Factory Head Noland",nolandteam,"Hoenn")
#Darach
darach1=Staraptor(maxiv="Yes")
darach2=Empoleon(maxiv="Yes")
darach3=Houndoom(maxiv="Yes")
darach4=Entei(maxiv="gmax")
darach5=MGallade(maxiv="Yes")
darach6=Alakazam(maxiv="Yes")
darach7=Metagross(maxiv="Yes")
darachteam=teamset([darach1,darach2,darach3,darach6,darach7],4)+[darach4,darach5]
darach=Trainer("Castle Velvet Darach",darachteam,"Sinnoh")
#volo
volo1=Spiritomb(maxiv="Yes")
volo2=Togekiss(maxiv="Yes")
volo3=HArcanine(maxiv="Yes")
volo4=Lucario(maxiv="gmax")
volo5=Garchomp(maxiv="Yes")
volo6=OGiratina(maxiv="Yes")
volo7=Roserade(maxiv="Yes")
voloteam=teamset([volo1,volo2,volo3,volo4,volo7],4)+[volo5,volo6]
volo=Trainer("Pokémon Wielder Volo",voloteam,"Hisui")
#Dahlia
dahlia1=Dusknoir(maxiv="Yes")
dahlia2=Medicham(maxiv="Yes")
dahlia3=Ludicolo(maxiv="Yes")
dahlia4=MBlaziken(maxiv="Yes")
dahlia5=Togekiss(maxiv="Yes")
dahlia6=Zapdos(maxiv="gmax")
dahlia=Trainer("Arcade Star Dahlia",[dahlia1,dahlia2,dahlia3,dahlia5,dahlia4,dahlia6],"Sinnoh")
#Archie
archie7=Walrein(maxiv="Yes")
archie1=Mightyena(maxiv="Yes")
archie2=Muk(maxiv="Yes")
archie3=Crobat(maxiv="Yes")
archie4=Tentacruel(maxiv="Yes")
archie5=MSharpedo(maxiv="Yes")
archie6=PKyogre(maxiv="Yes")
archie7=Kyogre(maxiv="gmax")
archieteam=teamset([archie1,archie2,archie3,archie4,archie5],5)+teamset([archie6,archie7],1)
archie=Trainer("Aqua Leader Archie",archieteam,"Hoenn")
#Maxie
maxie7=Houndoom(maxiv="Yes")
maxie1=Mightyena(maxiv="Yes")
maxie2=Weezing(maxiv="Yes")
maxie3=Crobat(maxiv="Yes")
maxie4=Torkoal(maxiv="Yes", ability="Drought")
maxie5=MCamerupt(maxiv="Yes")
maxie6=PGroudon(maxiv="Yes")
maxie7=Groudon(maxiv="gmax")
maxieteam=[maxie1,maxie2,maxie3,maxie4,maxie5]+teamset([maxie6,maxie7],1)
maxie=Trainer("Magma Leader Maxie",maxieteam,"Hoenn")
#Tabitha
tab1=Mightyena(maxiv="Yes")
tab2=Weezing(maxiv="Yes")
tab3=Crobat(maxiv="Yes")
tab4=Torkoal(maxiv="Yes", ability="Drought")
tab5=Camerupt(maxiv="gmax")
tab6=Swellow(maxiv="Yes")
tabitha=Trainer("Magma Admin Tabitha",[tab1,tab2,tab3,tab4,tab5,tab6],"Hoenn")
#blaise
blaise1=Magcargo(maxiv="Yes")
blaise2=Swellow (maxiv="Yes")
blaise3=Armaldo(maxiv="Yes")
blaise4=Torkoal(maxiv="Yes", ability="Drought")
blaise6=MCamerupt(maxiv="Yes")
blaise5=Crobat(maxiv="Yes")
blaise=Trainer("Magma Admin Blaise",[blaise1,blaise2,blaise3,blaise4,blaise5,blaise6],"Hoenn")
#Brandon
brandon1=Regice(maxiv="Yes")
brandon2=Regirock(maxiv="Yes")
brandon3=Registeel(maxiv="gmax")
brandon4=Articuno(maxiv="Yes")
brandon5=Zapdos(maxiv="Yes")
brandon6=Moltres(maxiv="Yes")
brandon7=Ninjask(maxiv="Yes")
brandon8=Dusclops(maxiv="Yes")
brandon9=Solrock(maxiv="Yes")
brandonteam=teamset([brandon7,brandon8,brandon9,brandon4,brandon5,brandon6],3)+[brandon1,brandon2,brandon3]
brandon=Trainer ("Pyramid King Brandon",brandonteam,"Hoenn")
#Illegal
illegal1=OArceus(maxiv="gmax")
illegal2=Cloyster()
illegal=Trainer("Missing No.",[illegal1,illegal2],"???")
#cyrus
cyrus1=Weavile(maxiv="Yes")
cyrus2=Honchkrow(maxiv="Yes")
cyrus3=Crobat(maxiv="Yes")
cyrus5=Houndoom(maxiv="Yes")
cyrus4=Gyarados (maxiv="Yes")
cyrus8=Entei(maxiv="gmax")
cyrus6=random.choice([Dialga,ODialga])(maxiv="Yes")
cyrus7=random.choice([Palkia,OPalkia])(maxiv="Yes")
cyrus8=Absol(maxiv="Yes")
cyrus9=Arcanine(maxiv="Yes")
cyrus10=Camerupt(maxiv="Yes")
cyrus11=Charizard(maxiv="Yes")
cyrus12=Zapdos(maxiv="Yes")
cyrus13=Darkrai(maxiv="Yes")
cyrus14=Sableye (maxiv="Yes")
cyrus15=Raticate(maxiv="Yes")
cyrusteam=teamset([cyrus1,cyrus2,cyrus8,cyrus4,cyrus5,cyrus8,cyrus9,cyrus10,cyrus11,cyrus12,cyrus13,cyrus14,cyrus15],4)+[cyrus6,cyrus7]
cyrus=Trainer("Galactic Leader Cyrus",cyrusteam,"Sinnoh")
#saturn
saturn1=Alakazam(maxiv="Yes")
saturn2=Bronzong(maxiv="Yes")
saturn3=Toxicroak(maxiv="Yes")
saturn4=Sharpedo(maxiv="Yes")
saturn5=Crobat(maxiv="Yes")
saturn6=Heatran(maxiv="Yes")
saturn7=Sableye(maxiv="Yes")
saturn8=Skuntank(maxiv="Yes")
saturn9=Tyranitar(maxiv="Yes")
saturn10=MGallade(maxiv="Yes")
saturn11=Rhyperior(maxiv="Yes")
saturn12=Magmortar(maxiv="Yes")
saturn13=Ambipom(maxiv="Yes")
saturnteam=teamset([saturn1,saturn2,saturn7,saturn4,saturn5,saturn6,saturn8,saturn9,saturn10,saturn11,saturn12],5)+[saturn3]
saturn=Trainer("Galactic Commander Saturn",saturnteam,"Sinnoh")
#mars
mars1=Raichu(maxiv="Yes")
mars2=Bronzong(maxiv="Yes")
mars3=Purugly(maxiv="Yes")
mars4=Togekiss(maxiv="Yes")
mars5=Crobat(maxiv="Yes")
mars6=Espeon(maxiv="Yes")
mars7=Yanmega(maxiv="Yes")
mars8=Electivire(maxiv="Yes")
mars9=MKangaskhan(maxiv="Yes")
mars10=Magnezone (maxiv="Yes")
mars11=PorygonZ (maxiv="Yes")
marsteam=teamset([mars1,mars2,mars7,mars4,mars5,mars6,mars8,mars9,mars10],5)+[mars3]
mars=Trainer("Galactic Commander Mars",marsteam,"Sinnoh")
#jupiter
jupiter1=Nidoking(maxiv="Yes")
jupiter2=Bronzong(maxiv="Yes")
jupiter3=Skuntank(maxiv="Yes")
jupiter4=MGengar(maxiv="Yes")
jupiter5=Crobat(maxiv="Yes")
jupiter6=Toxicroak(maxiv="Yes")
jupiter7=Sableye(maxiv="Yes")
jupiter8=EGastrodon(maxiv="Yes")
jupiter9=Tangrowth(maxiv="Yes")
jupiter10=Probopass(maxiv="Yes")
jupiterteam=teamset([jupiter1,jupiter2,jupiter7,jupiter4,jupiter5,jupiter6,jupiter8,jupiter9],5)+[jupiter3]
jupiter=Trainer("Galactic Commander Jupiter",jupiterteam,"Sinnoh")
#E4 Siebold
siebold1=Clawitzer(maxiv="Yes")
siebold2=Gyarados(maxiv="Yes")
siebold3=Starmie(maxiv="Yes")
siebold4=Barbaracle(maxiv="Yes")
siebold5=Milotic(maxiv="gmax")
siebold6=MBlastoise(maxiv="Yes")
siebold=Trainer("Elite Four Siebold",[siebold1,siebold2,siebold3,siebold4,siebold5,siebold6],"Kalos")
#E4 Wikstrom
wikstrom1=Probopass(maxiv="Yes")
wikstrom2=Aegislash (maxiv="Yes")
wikstrom3=Escavalier(maxiv="gmax")
wikstrom4=HGoodra(maxiv="Yes")
wikstrom5=Klefki(maxiv="Yes")
wikstrom6=MScizor(maxiv="Yes")
wikstrom=Trainer("Elite Four Wikstrom",[wikstrom1,wikstrom2,wikstrom3,wikstrom4,wikstrom5,wikstrom6],"Kalos")
#E4 Drasna
drasna1=Druddigon(maxiv="Yes")
drasna2=Dragalge(maxiv="Yes")
drasna3=Noivern(maxiv="gmax")
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
malva7=Yveltal(maxiv="gmax")
malva=Trainer("Elite Four Malva",[malva1,malva2,malva4,malva5,malva6,malva7],"Kalos")
#n
n1=Carracosta(maxiv="Yes")
n2=Vanilluxe(maxiv="Yes")
n3=Archeops(maxiv="Yes")
n4=Zoroark(maxiv="gmax")
n5=Zekrom(maxiv="Yes")
n6=Reshiram(maxiv="Yes")
n=Trainer("Pokémon Trainer N",[n1,n2,n3,n4,n5,n6],"Unova")
#Ghetsis
ghet4=Hydreigon(maxiv="gmax")
ghet2=Kingambit (maxiv="Yes")
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
alain2=Kingambit (maxiv="Yes",move=["Thunder Wave","Focus Blast","Iron Head","Night Slash"],item="Life Orb")
alain3=Unfezant(maxiv="Yes",move=["Sky Attack","Steel Wing","Hurricane","Air Slash"])
alain4=Metagross(maxiv="Yes",move=["Meteor Mash","Psyshock","Rock Slide","Zen Headbutt"],nature="Naughty")
alain5=Weavile(maxiv="Yes",move=["Protect","Night Slash","Ice Beam","Ice Shard"],nature="Hasty")
alain6=MCharizardX(maxiv="Yes",move=["Flamethrower","Dragon Claw","Thunder Punch","Blast Burn"],nature="Hasty")
alain7=Malamar(maxiv="Yes")
alain8=Chesnaught(maxiv="gmax")
alainteam=teamset([alain1,alain2,alain3,alain4,alain5,alain7,alain8],5)+[alain6]
alain=Trainer("Pokémon Trainer Alain",alainteam,"Unova")
#Anabel
anabel1=Alakazam(maxiv="Yes")
anabel2=Latios(maxiv="Yes")
anabel3=Snorlax(maxiv="Yes")
anabel4=Entei(maxiv="Yes")
anabel5=Raikou(maxiv="gmax")
anabel6=MLucario(maxiv="Yes")
anabel=Trainer("Salon Maiden Anabel",[anabel1,anabel2,anabel3,anabel4,anabel5,anabel6],"Hoenn")
#greta
greta1=Heracross(maxiv="gmax")
greta2=Breloom(maxiv="Yes")
greta3=Umbreon(maxiv="Yes")
greta4=Gengar(maxiv="Yes")
greta5=Hariyama(maxiv="Yes")
greta6=MMedicham(maxiv="Yes")
greta=Trainer("Arena Tycoon Greta",[greta1,greta2,greta3,greta4,greta5,greta6],"Hoenn")
#Tucker
tucker1=Metagross(maxiv="Yes")
tucker2=Arcanine(maxiv="Yes")
tucker3=Charizard(maxiv="Yes")
tucker4=Salamence(maxiv="Yes",item="Lum Berry")
tucker5=Latias(maxiv="gmax")
tucker6=MSwampert(maxiv="Yes")
tucker=Trainer ("Dome Ace Tucker",[tucker1,tucker2,tucker3,tucker4,tucker5,tucker6],"Hoenn")
#Lucy
lucy1=Arbok(maxiv="Yes")
lucy2=Snorlax(maxiv="Yes")
lucy3=Steelix(maxiv="Yes")
lucy4=Gyarados(maxiv="Yes")
lucy5=Milotic(maxiv="Yes")
lucy6=Seviper(maxiv="gmax")
lucy7=Shuckle(maxiv="Yes")
lucyteam=teamset([lucy1,lucy2,lucy3,lucy4,lucy5,lucy7],5)+[lucy6]
lucy=Trainer ("Pike Queen Lucy",lucyteam,"Hoenn")
#spenser
spenser1=Arcanine(maxiv="Yes")
spenser2=Lapras(maxiv="Yes")
spenser3=Slaking(maxiv="Yes")
spenser4=Crobat(maxiv="Yes")
spenser5=Suicune(maxiv="Yes")
spenser6=MVenusaur(maxiv="Yes")
spenser7=Venusaur(maxiv="gmax")    
spenser8=Claydol(maxiv="Yes")
spenser9=Dusclops(maxiv="Yes")
spenser10=Chansey(maxiv="Yes")
spenser11=Shiftry(maxiv="Yes")
spenserteam=teamset([spenser1,spenser2,spenser3,spenser4,spenser5,spenser8,spenser9,spenser10,spenser11],5)+teamset ([spenser6,spenser7],1)
spenser=Trainer("Palace Maven Spenser",spenserteam,"Hoenn")
#Giovanni
gio1=Nidoqueen(maxiv="Yes")
gio2=Nidoking(maxiv="Yes")
gio3=Honchkrow(maxiv="Yes")
gio4=Rhyperior(maxiv="Yes")
gio5=MKangaskhan(maxiv="Yes")
gio6=Mewtwo(maxiv="gmax")
gio7=Garchomp(maxiv="Yes")
gio8=Dugtrio(maxiv="Yes")
gio9=Steelix(maxiv="Yes")
gio10=Persian(maxiv="Yes")
gio11=Marowak(maxiv="Yes")
gio12=Sandslash(maxiv="Yes")
gio13=Gliscor(maxiv="Yes")
gio14=Krookodile(maxiv="Yes")
gio15=Hippowdon(maxiv="Yes")
gio19=MMewtwoX(maxiv="Yes")
gio20=MMewtwoY(maxiv="Yes")
gio21=Kangaskhan(maxiv="gmax")
gio22=Gyarados(maxiv="Yes")
gioteam1=teamset([gio1,gio2,gio3,gio4,gio7,gio8,gio9,gio10,gio11,gio12,gio13,gio14,gio15,gio22],4)+[gio5,gio6]
gioteam2=teamset([gio1,gio2,gio3,gio4,gio7,gio8,gio9,gio10,gio11,gio12,gio13,gio14,gio15],4)+[gio21]+teamset([gio19,gio20],1)
gioteam=random.choice([gioteam1,gioteam2])
giovanni=Trainer("Rocket Boss Giovanni",gioteam,"Kanto")
#Archer
archer1=Electrode(maxiv="Yes")
archer2=Mightyena(maxiv="Yes")
archer3=Weezing(maxiv="Yes")
archer4=Crobat(maxiv="Yes")
archer5=Tyranitar(maxiv="gmax")
archer6=MHoundoom(maxiv="Yes")
archer=Trainer("Rocket Commander Archer",[archer1,archer2,archer3,archer4,archer5,archer6],"Kanto")
#Ariana
ariana1=Muk(maxiv="Yes")
ariana2=Honchkrow(maxiv="Yes")
ariana3=Weavile(maxiv="Yes")
ariana4=Crobat(maxiv="Yes")
ariana5=Arbok(maxiv="gmax")
ariana6=MMawile(maxiv="Yes")
ariana=Trainer("Rocket Commander Ariana",[ariana1,ariana2,ariana3,ariana4,ariana5,ariana6],"Kanto")
#Silver
silver1=Weavile (maxiv="Yes")
silver2=Honchkrow(maxiv="Yes")
silver3=Kingdra(maxiv="Yes")
silver4=Ursaluna(maxiv="Yes")
silver5=MGyarados(name="Mega Gyarados✨",maxiv="Yes")
silver6=Feraligatr(maxiv="gmax")
silver7=Gengar(maxiv="Yes")
silver8=Alakazam (maxiv="Yes")
silver9=Crobat(maxiv="Yes")
silver10=Magnezone(maxiv="Yes")
silverteam=teamset([silver1,silver2,silver3,silver4,silver7,silver8,silver9,silver10],4)+[silver6,silver5]
silver=Trainer("Pokémon Trainer Silver",silverteam,"Johto")
#Gary
gary1=Arcanine(maxiv="Yes")
gary2=Nidoking(maxiv="Yes")
gary3=Scizor(maxiv="Yes")
gary4=Umbreon(maxiv="Yes")
gary5=Electivire(maxiv="Yes")
gary6=Blastoise(maxiv="gmax")
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
blue3=Rhyperior(maxiv="gmax")
blue4=Gyarados(maxiv="Yes")
blue5=Arcanine(maxiv="Yes")
blue6=MPidgeot(maxiv="Yes")
blue7=Machamp(maxiv="Yes")
blue8=Tyranitar(maxiv="Yes")
blue9=Blastoise (maxiv="Yes")
blue10=Venusaur(maxiv="Yes")
blue11=Charizard(maxiv="Yes")
blue12=Ninetales(maxiv="Yes")
blue13=Cloyster(maxiv="Yes")
blue14=Jolteon(maxiv="Yes")
blue15=Vaporeon (maxiv="Yes")
blue16=Flareon(maxiv="Yes")
blue17=Heracross(maxiv="Yes")
blue18=Aerodactyl(maxiv="Yes")
blueteam=teamset([blue2,blue3,blue4,blue5,blue7,blue8],3)+teamset([blue14,blue15,blue16],1)+teamset([blue9,blue10,blue11],1)+[blue6]
blue=Trainer("Pokémon Trainer Blue",blueteam,"Kanto")
#falkner
falkner1=Pelipper(maxiv="Yes")
falkner2=Honchkrow(maxiv="Yes")
falkner3=Swellow(maxiv="Yes")
falkner4=Skarmory(maxiv="Yes")
falkner5=Noctowl(maxiv="Yes")
falkner6=MPidgeot(maxiv="Yes")
falkner7=Staraptor(maxiv="Yes")
falkner8=Fearow(maxiv="Yes")
falkner9=Xatu(maxiv="Yes")
falkner10=Dodrio(maxiv="Yes")
falkner11=Crobat(maxiv="gmax")
falkner12=Aerodactyl(maxiv="Yes")
falkner13=Lugia(maxiv="Yes")
falkner14=Togekiss(maxiv="Yes")
falknerteam=teamset([falkner1,falkner2,falkner3,falkner4,falkner5,falkner7,falkner8,falkner9,falkner10,falkner11,falkner12,falkner13,falkner14],5)+[falkner6]
falkner=Trainer ("Gym Leader Falkner",falknerteam,"Johto")
#Kukui
kukui1=Braviary(maxiv="Yes")
kukui2=Venusaur(maxiv="gmax")
kukui3=Empoleon(maxiv="Yes")
kukui4=Lucario(maxiv="Yes")
kukui5=MDLycanroc(maxiv="Yes")
kukui6=Incineroar(name="Incineroar(Z-Crystal)",maxiv="Yes")
kukui=Trainer("Professor Kukui",[kukui1,kukui2,kukui3,kukui4,kukui5,kukui6],"Alola")
#Ethan
ethan1=Tauros(maxiv="Yes")
ethan2=Tangrowth(maxiv="Yes")
ethan3=PorygonZ(maxiv="Yes")
ethan4=Azumarill(maxiv="Yes")
ethan5=MVenusaur(maxiv="Yes")
ethan6=Typhlosion(maxiv="Grass")
ethan=Trainer ("Pokémon Trainer Ethan",[ethan1,ethan2,ethan3,ethan4,ethan5,ethan6],"Johto")
#Mustard
mustard1=WUrshifu(maxiv="gmax")
mustard9=WUrshifu(maxiv="Yes")
mustard8=DUrshifu(maxiv="gmax")
mustard2=Mienshao(maxiv="Yes")
mustard3=Corviknight(maxiv="Yes")
mustard5=MDLycanroc(maxiv="Yes")
mustard4=Kommo(maxiv="Yes")
mustard7=Luxray(maxiv="Yes")
mustard6=DUrshifu(maxiv="Yes")
mustardteam1=teamset([mustard2,mustard3,mustard4,mustard5],4)+[mustard1,mustard6]
mustardteam2=teamset([mustard2,mustard3,mustard4,mustard5],4)+[mustard9,mustard8]
mustard=Trainer("Pokémon Trainer Mustard", random.choice([mustardteam1,mustardteam2]),"Galar")    
#Brendan
bren1=Gardevoir(maxiv="Yes")
bren9=Aggron(maxiv="Yes")
bren7=Shiftry(maxiv="Yes")
bren8=Swampert(maxiv="Yes")
bren5=Latios(maxiv="gmax")
bren6=MSceptile(maxiv="Yes")
bren11=Wailord(maxiv="Yes")
bren12=Breloom(maxiv="Yes")
bren13=Camerupt(maxiv="Yes")
bren14=Swellow(maxiv="Yes")
bren15=Pelipper(maxiv="Yes")
bren16=Ludicolo(maxiv="Yes")
bren17=Magcargo(maxiv="Yes")
bren18=Tropius(maxiv="Yes")
bren19=Raichu(maxiv="Yes")
bren20=Claydol(maxiv="Yes")
bren21=Exploud(maxiv="Yes")
bren10=PGroudon(maxiv="Yes")
bren22=PKyogre(maxiv="Yes")
bren23=Rayquaza(maxiv="Yes")
brenteam=teamset([bren1,bren5,bren7,bren8,bren9,bren11,bren12,bren13,bren14,bren15,bren16,bren17,bren18,bren19,bren20,bren21,bren10,bren22,bren23],5)+[bren6]
brendan=Trainer("Pokémon Trainer Brendan",brenteam,"Hoenn")
#may
may1=Gallade(maxiv="Yes")
may2=Blastoise(maxiv="Yes")
may3=Snorlax(maxiv="Yes")
may4=Beautifly(maxiv="Yes")
may9=Glaceon(maxiv="Yes")
may7=Venusaur(maxiv="Yes")
may8=Swampert(maxiv="Yes")
may5=Latias(maxiv="gmax")
may6=MBlaziken(maxiv="Yes")
may10=Delcatty(maxiv="Yes")
may11=Wailord(maxiv="Yes")
may12=Breloom(maxiv="Yes")
may13=Camerupt(maxiv="Yes")
may14=Swellow(maxiv="Yes")
may15=Pelipper(maxiv="Yes")
may16=Ludicolo(maxiv="Yes")
may17=Magcargo(maxiv="Yes")
may18=Tropius(maxiv="Yes")
may19=Raichu(maxiv="Yes")
may20=Claydol(maxiv="Yes")
may21=Exploud(maxiv="Yes")
may22=PKyogre(maxiv="Yes")
may23=PGroudon(maxiv="Yes")
may24=Rayquaza(maxiv="Yes")
mayteam=teamset([may1,may2,may3,may4,may5,may7,may8,may9,may10,may11,may12,may13,may14,may15,may16,may17,may18,may19,may20,may21,may22,may23,may24],5)+[may6]
may=Trainer("Pokémon Trainer May",mayteam,"Hoenn")
#Ingo
ingo1=Gliscor(maxiv="Yes")
ingo2=Alakazam(maxiv="Yes")
ingo3=Tangrowth(maxiv="Yes")
ingo4=Machamp(maxiv="Yes")
ingo5=Probopass(maxiv="Yes")
ingo6=Magnezone(maxiv="Yes")
ingo7=Haxorus(maxiv="Yes")
ingo8=Garbodor(maxiv="Yes")
ingo9=Crustle(maxiv="Yes")
ingo10=Klinklang(maxiv="Yes")
ingo11=Excadrill(maxiv="Yes")
ingo12=Chandelure(maxiv="gmax")
ingo13=Kleavor(maxiv="Yes")
ingo14=Wyrdeer(maxiv="Yes")
ingo15=Basculegion(maxiv="Yes")
ingo16=Conkeldurr(maxiv="Yes")
ingoteam=teamset([ingo1,ingo2,ingo3,ingo4,ingo5,ingo7,ingo6,ingo8,ingo9,ingo10,ingo11,ingo13,ingo14,ingo15,ingo16],5)+[ingo12]
ingo=Trainer("Subway Boss Ingo",ingoteam,"Unova")
#emmet
emmet1=Crustle(maxiv="Yes")
emmet2=Klinklang (maxiv="Yes")
emmet3=Garbodor(maxiv="Yes")
emmet4=Durant(maxiv="Yes")
emmet5=Excadrill(maxiv="Yes")
emmet6=Chandelure(maxiv="Yes")
emmet7=Haxorus(maxiv="Yes")
emmet8=Eelektross(maxiv="gmax")
emmet9=Galvantula (maxiv="Yes")
emmet10=Archeops(maxiv="Yes")
emmet11=Gigalith(maxiv="Yes")
emmetteam=teamset([emmet1,emmet2,emmet3,emmet4,emmet5,emmet7,emmet6,emmet9,emmet10,emmet11],5)+[emmet8]
emmet=Trainer ("Subway Boss Emmet",emmetteam,"Unova")
#Phoebe
phoebe1=Banette(maxiv="Yes")
phoebe2=Mismagius(maxiv="Yes")
phoebe3=Drifblim(maxiv="Yes")
phoebe4=Chandelure(maxiv="Yes")
phoebe5=Dusknoir(maxiv="gmax")
phoebe6=MSableye(maxiv="Yes")
phoebe7=MBanette(maxiv="Yes")
phoebeteam=teamset([phoebe1,phoebe2,phoebe3,phoebe4,phoebe5],5)+teamset([phoebe6,phoebe7],1)
phoebe=Trainer ("Elite Four Phoebe",phoebeteam,"Hoenn")
#Sidney
sidney1=Shiftry(maxiv="Yes")
sidney2=Scrafty(maxiv="Yes")
sidney3=Zoroark(maxiv="Yes")
sidney4=Sharpedo(maxiv="Yes")
sidney5=Mandibuzz(maxiv="Yes")
sidney6=MAbsol(maxiv="Yes")
sidney7=Cacturne(maxiv="gmax")
sidney8=Crawdaunt(maxiv="Yes")
sidney9=Mightyena(maxiv="Yes")
sidneyteam=teamset([sidney1,sidney2,sidney3,sidney4,sidney5,sidney7,sidney8,sidney9],5)+[sidney6]
sidney=Trainer ("Elite Four Sidney",sidneyteam,"Hoenn")
#Glacia
glacia1=Abomasnow(maxiv="Yes")
glacia2=Beartic(maxiv="Yes")
glacia3=Froslass(maxiv="Yes")
glacia4=Vanilluxe(maxiv="Yes")
glacia5=Walrein(maxiv="gmax")
glacia6=MGlalie(maxiv="Yes")
glacia=Trainer ("Elite Four Glacia",[glacia1,glacia2,glacia3,glacia4,glacia5,glacia6],"Hoenn")
#Drake
drake1=Altaria(maxiv="Yes")
drake2=Dragalge(maxiv="Yes")
drake3=Kingdra(maxiv="Yes")
drake4=Flygon(maxiv="gmax")
drake5=Haxorus(maxiv="Yes")
drake6=MSalamence(maxiv="Yes")
drake=Trainer ("Elite Four Drake",[drake1,drake2,drake3,drake4,drake5,drake6],"Hoenn")
#Karen
karen1=Weavile(maxiv="Yes")
karen2=Absol(maxiv="Yes")
karen3=Spiritomb(maxiv="Yes")
karen4=Houndoom(maxiv="Yes")
karen5=Honchkrow(maxiv="Yes")
karen6=Umbreon(maxiv="gmax")
karen7=Vileplume(maxiv="Yes")
karen8=Gengar(maxiv="Yes")
karenteam=teamset([karen1,karen2,karen3,karen4,karen5,karen7,karen8],5)+[karen6]
karen=Trainer ("Elite Four Karen",karenteam,"Johto")
#brock
brock1=Omastar(maxiv="Yes")
brock2=Kabutops(maxiv="Yes")
brock3=Rhyperior (maxiv="gmax")
brock4=Golem(maxiv="Yes")
brock5=Tyranitar(maxiv="Yes")
brock6=MSteelix(maxiv="Yes")
brock7=Rampardos(maxiv="Yes")
brock8=Aerodactyl(maxiv="Yes")
brock9=Relicanth(maxiv="Yes")
brock10=Sudowoodo(maxiv="Yes")
brock11=Blissey(maxiv="Yes")
brock12=Anihilape(maxiv="Yes")
brock13=Sandslash(maxiv="Yes")
brock14=Crobat(maxiv="Yes")
brock15=Ninetales(maxiv="Yes")
brock16=Swampert(maxiv="Yes")
brock17=Forretress(maxiv="Yes")
brockteam=teamset([brock1,brock2,brock3,brock4,brock5,brock7,brock8,brock9,brock10,brock11,brock12,brock13,brock14,brock15,brock16,brock17],5)+[brock6]
brock=Trainer ("Gym Leader Brock",brockteam,"Kanto")
#Marshal
marshal1=Breloom(maxiv="Yes")
marshal2=Mienshao(maxiv="Yes")
marshal3=Toxicroak(maxiv="Yes")
marshal4=Lucario(maxiv="Yes")
marshal5=Machamp(maxiv="Yes")
marshal6=Conkeldurr(maxiv="gmax")
marshal=Trainer ("Elite Four Marshal",[marshal1,marshal2,marshal3,marshal4,marshal5,marshal6],"Unova")
#shauntal
shauntal1=Cofagrigus(maxiv="Yes")
shauntal2=Jellicent(maxiv="Yes")
shauntal3=Drifblim(maxiv="Yes")
shauntal4=Golurk(maxiv="Yes")
shauntal5=Froslass(maxiv="Yes")
shauntal6=Chandelure(maxiv="gmax")
shauntal=Trainer ("Elite Four Shauntal",[shauntal1,shauntal2,shauntal3,shauntal4,shauntal5,shauntal6],"Unova")
#grimsley
grimsley1=Scrafty(maxiv="Yes")
grimsley2=Drapion(maxiv="Yes")
grimsley3=Krookodile (maxiv="Yes")
grimsley4=Houndoom(maxiv="Yes")
grimsley6=MTyranitar(maxiv="Yes")
grimsley5=Kingambit(maxiv="gmax")
grimsley=Trainer ("Elite Four Grimsley",[grimsley1,grimsley2,grimsley3,grimsley4,grimsley5,grimsley6],"Unova")
#caitlin
caitlin1=Alakazam(maxiv="Yes")
caitlin2=Gallade (maxiv="Yes")
caitlin3=Reuniclus (maxiv="Yes")
caitlin4=Metagross (maxiv="Yes")
caitlin5=Bronzong (maxiv="Yes")
caitlin6=Gothitelle (maxiv="gmax")
caitlin=Trainer ("Elite Four Caitlin",[caitlin1,caitlin2,caitlin3,caitlin4,caitlin5,caitlin6],"Unova")
#sawyer
sawyer1=Slurpuff(maxiv="Yes")
sawyer2=Clawitzer (maxiv="Yes")
sawyer3=Aegislash (maxiv="Yes")
sawyer4=Slaking(maxiv="Yes")
sawyer5=Salamence(maxiv="gmax")
sawyer6=MSceptile (maxiv="Yes")
sawyer=Trainer ("Pokémon Trainer Sawyer",[sawyer1,sawyer2,sawyer3,sawyer4,sawyer5,sawyer6],"Kalos")
#alder
alder1=Escavalier(maxiv="Yes", ability="Swarm",move=["X-Scissor","Giga Impact","Iron Head","Double Iron Bash"])
alder2=Conkeldurr(maxiv="Yes",item="Life Orb", ability="Sheer Force",move=["Hammer Arm","Madh Punch","Stone Edge","Bulk Up"])
alder3=Krookodile (maxiv="Yes",move=["Earthquake","Crunch","Stone Edge","Outrage"],item="Expert Belt")
alder4=Bouffalant (maxiv="Yes", ability="Sap Sipper",move=["Head Charge","Megahorn","Stone Edge","Earthquake"])
alder5=Braviary (maxiv="Yes", move=["Crush Claw","Rock Slide","Superpower","Brave Bird"],item="Choice Band")
alder6=Volcarona (maxiv="gmax",move=["Quiver Dance","Bug Buzz","Heat Wave","Psychic"], ability="Flame Body",item="Charti Berry")
alder7=Vanilluxe(maxiv="Yes", ability="Ice Body",move=["Blizzard","Acid Armor","Flash Cannon","Light Screen"])
alder8=Accelgor(maxiv="Yes", ability="Hydration",move=["Bug Buzz","Focus Blast","Energy Ball","Water Shuriken"])
alder9=Druddigon(maxiv="Yes", ability="Rough Skin", move=["Night Slash","Outrage","Superpower","Dragon Dance"])
alder10=Chandelure(maxiv="Yes",item="Choice Scarf",move=["Flamethrower","Shadow Ball","Psychic","Energy Ball"])
alder11=Reuniclus(maxiv="Yes",item="Leftovers",move=["Light Screen","Reflect","Toxic","Psychic"])
alderteam=teamset([alder1,alder2,alder3,alder4,alder5,alder7,alder8,alder9,alder10,alder11],5)+[alder6]
alder=Trainer ("Unova Champion Alder",alderteam,"Unova")
#barry
barry1=Roserade(maxiv="Yes")
barry2=Staraptor(maxiv="Yes")
barry3=Hitmonlee(maxiv="Yes")
barry4=MHeracross(maxiv="Yes")
barry5=Skarmory(maxiv="Yes")
barry6=Empoleon(maxiv="gmax")
barry7=Snorlax(name="Snorlax(Z-Crystal)",move=["Giga Impact","Rest","Heavy Slam","Ice Punch"],maxiv="Yes")
barry8=Rapidash(maxiv="Yes")
barry9=Floatzel(maxiv="Yes")
barryteam=teamset([barry1,barry2,barry3,barry4,barry5,barry7,barry8,barry9],5)+[barry6]
barry=Trainer ("Pokémon Trainer Barry",barryteam,"Sinnoh")
#wally
wally1=Roserade(maxiv="Yes")
wally2=Azumarill (maxiv="Yes")
wally3=Garchomp(maxiv="Yes")
wally4=Magnezone(maxiv="Yes")
wally5=Altaria(maxiv="Yes")
wally6=MGallade(maxiv="Yes")
wally7=Talonflame (maxiv="Yes")
wally8=Gardevoir(maxiv="Yes")
wally9=Delcatty(maxiv="Yes")
wallyteam=teamset([wally1,wally2,wally3,wally4,wally5,wally7,wally8,wally9],5)+[wally6]
wally=Trainer ("Pokémon Trainer Wally",wallyteam,"Hoenn")
#paul
paul1=Honchkrow(maxiv="Yes")
paul2=Weavile(maxiv="Yes")
paul3=Gyarados (maxiv="Yes")
paul4=Garchomp (maxiv="Yes")
paul5=Metagross(maxiv="Yes")
paul6=Electivire(maxiv="gmax")
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
trevor1=Florges(maxiv="gmax")
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
hala5=Machamp(maxiv="gmax")
hala6=Hariyama(name="Hariyama(Z-Crystal)",maxiv="Yes")
hala=Trainer ("Elite Four Hala",[hala1,hala2,hala3,hala4,hala5,hala6],"Alola")
#molayne
molayne1=Skarmory(maxiv="Yes")
molayne2=Magnezone(maxiv="Yes")
molayne3=Metagross(maxiv="Yes")
molayne4=Klefki(maxiv="Yes")
molayne5=Kingambit(maxiv="gmax")
molayne6=Steelix(maxiv="Yes")
molayne7=Genesect(maxiv="Yes")
molayne8=ADugtrio(name="Alolan Dugtrio(Z-Crystal)",maxiv="Yes")
molayneteam=teamset([molayne1,molayne2,molayne3,molayne4,molayne5,molayne7,molayne6],5)+[molayne8]
molayne=Trainer ("Elite Four Molayne", molayneteam,"Alola")
#olivia
olivia1=Relicanth(maxiv="Yes")
olivia2=Gigalith(maxiv="gmax")
olivia3=AGolem(maxiv="Yes")
olivia4=Armaldo(maxiv="Yes")
olivia5=Cradily(maxiv="Yes")
olivia6=MNLycanroc(name="Midnight Lycanroc(Z-Crystal)",maxiv="Yes")
olivia=Trainer ("Elite Four Olivia",[olivia1,olivia2,olivia3,olivia4,olivia5,olivia6],"Alola")
#acerola
acerola1=Froslass(maxiv="Yes")
acerola2=Palossand(maxiv="gmax")
acerola3=Drifblim(maxiv="Yes")
acerola4=Dhelmise (maxiv="Yes")
acerola5=Banette (maxiv="Yes")
acerola6=Mimikyu(name="Mimikyu(Z-Crystal)",maxiv="Yes")
acerola=Trainer ("Elite Four Acerola",[acerola1,acerola2,acerola3,acerola4,acerola5,acerola6],"Alola")
#kahili
kahili1=Skarmory (maxiv="Yes")
kahili2=Crobat(maxiv="Yes")
kahili3=Mandibuzz(maxiv="Yes")
kahili4=Hawlucha (maxiv="Yes")
kahili5=Braviary (maxiv="gmax")
kahili6=Toucannon(name="Toucannon(Z-Crystal)",maxiv="Yes")
kahili=Trainer ("Elite Four Kahili",[kahili1,kahili2,kahili3,kahili4,kahili5,kahili6],"Alola")
#odrake
odrake1=Ditto(maxiv="Yes")
odrake2=Gengar(maxiv="gmax")
odrake3=MVenusaur(maxiv="Yes")
odrake4=Steelix(maxiv="Yes")
odrake5=Electivire(maxiv="Yes")
odrake6=Dragonite(maxiv="Yes")
odrake=Trainer ("Supreme Gym Leader Drake",[odrake1,odrake2,odrake3,odrake4,odrake5,odrake6],"Orange Islands")
#Leon
leonmax=random.randint(1,4)
cimax="Yes"
chmax="Yes"
rimax="Yes"
inmax="Yes"
if leonmax==1:
    cimax="gmax"
if leonmax==2:
    chmax="gmax"
if leonmax==3:
    rimax="gmax"
if leonmax==4:
    inmax="gmax"            
leon1=MrRime(maxiv="Yes")
leon2=Aegislash(maxiv="Yes")
leon3=Dragapult (maxiv="Yes")
leon4=Inteleon(maxiv=inmax)
leon5=Rillaboom(maxiv=rimax,move=["Drum Beating","Acrobatics","High Horsepower","Knock Off"],item="Flying Gem")
leon6=Cinderace(maxiv=cimax,ability="Libero",move=["Scorching Sands","Pyro Ball","Sucker Punch","Grass Knot"])
leon7=Charizard (maxiv=chmax,move=["Flamethrower","Ancient Power","Air Slash","Dragon Pulse"],atkev=0,spatkev=252)
leon8=Seismitoad(maxiv="Yes")
leon9=Rhyperior(maxiv="Yes")
leon10=Eternatus (maxiv="Yes")
leonteam=teamset([leon1,leon2,leon3,leon4,leon5,leon6,leon8,leon9,leon10],5)+[leon7]
leon=Trainer("Galar Champion Leon", leonteam,"Galar")
#Benga
benga1=Emboar(maxiv="Yes")
benga2=Dragonite (maxiv="Yes")
benga3=Garchomp (maxiv="Yes")
benga4=Latias (maxiv="Yes")
benga5=Latios (maxiv="Yes")
benga6=Volcarona(maxiv="gmax")
benga=Trainer ("Pokémon Trainer Benga",[benga1,benga2,benga3,benga4,benga5,benga6],"Unova")
#misty
misty1=Seaking(maxiv="Yes",ability="Lightning Rod")
misty2=Starmie(maxiv="gmax")
misty3=Politoed(maxiv="Yes", ability="Drizzle")
misty4=Kingdra(maxiv="Yes")
misty5=Lapras(maxiv="Yes")
misty6=MGyarados(maxiv="Yes")
misty7=Quagsire(maxiv="Yes")
misty8=Lanturn(maxiv="Yes")
misty9=Milotic(maxiv="Yes")
misty10=Jellicent(maxiv="Yes")
misty11=Blastoise(maxiv="Yes")
misty12=Golduck(name="Golduck(Z-Crystal)",maxiv="Yes")
misty13=Swanna(maxiv="Yes")
misty14=Carracosta(maxiv="Yes")
misty15=Dewgong (maxiv="Yes")
misty16=Vaporeon (maxiv="Yes")
misty17=Slowbro(maxiv="Yes")
misty18=Manaphy (maxiv="Yes")
misty19=Clawitzer (maxiv="Yes")
misty20=Azumarill (maxiv="Yes")
misty21=Tentacruel (maxiv="Yes")
misty22=Poliwrath (maxiv="Yes")
misty23=Corsola (maxiv="Yes")
mistyteam=teamset([misty1,misty4,misty5,misty7,misty8,misty9,misty10,misty11,misty12,misty13,misty14,misty15,misty16,misty17,misty18,misty19,misty20],3)+[misty3,misty2,misty6]
misty=Trainer ("Gym Leader Misty",mistyteam,"Kanto")
#surge
surge1=Ampharos(maxiv="Yes")
surge2=Jolteon(maxiv="Yes")
surge3=Magnezone(maxiv="Yes")
surge4=Electivire(maxiv="Yes")
surge5=Electrode(maxiv="Yes")
surge6=Raichu(maxiv="gmax")
surge7=MManectric(maxiv="Yes")
surge8=Lanturn(maxiv="Yes")
surge9=Zapdos(name="Zapdos(Z-Crystal)",maxiv="Yes")
surgeteam=teamset([surge1,surge2,surge3,surge4,surge5,surge7,surge8,surge9],5)+[surge6]
surge=Trainer ("Gym Leader Lt.Surge",surgeteam,"Kanto")
#erika
erika1=Jumpluff(maxiv="Yes")
erika2=Bellossom(name="Bellossom(Z-Crystal)",maxiv="Yes")
erika3=Tangrowth(maxiv="Yes")
erika4=Victreebel(maxiv="Yes")
erika5=Vileplume(maxiv="gmax")
erika6=MVenusaur(maxiv="Yes")
erika7=Shiftry(maxiv="Yes")
erika8=Roserade(maxiv="Yes")
erika9=Exeggutor(maxiv="Yes")
erika10=Cradily(maxiv="Yes")
erika11=Abomasnow(maxiv="Yes")
erika12=Parasect(maxiv="Yes")
erika13=Leafeon(maxiv="Yes")
erika14=Shaymin(maxiv="Yes")
erikateam=teamset([erika1,erika2,erika3,erika4,erika7,erika8,erika9,erika10,erika11,erika12,erika13,erika14],4)+[erika5,erika6]
erika=Trainer ("Gym Leader Erika",erikateam,"Kanto")
erikah1=Tsareena (ability="Striker",maxiv="Yes",nature="Adamant",item="Focus Sash",move=["Triple Axel","Trop Kick","High Jump Kick","Rapid Spin"])
erikah2=Hawlucha (ability="Unburden",nature="Adamant",maxiv="Yes",item="Grassy Seed",move=["Swords Dance","Close Combat","Acrobatics","Roost"])
erikah3=Bellossom (ability="Chlorophyll",maxiv="Yes",item="Leftovers",nature="Timid",move=["Sleep Powder","Quiver Dance","Giga Drain","Fiery Dance"])
erikah4=Rillaboom(ability="Grassy Surge",maxiv="Yes",item="Grassy Seed",nature="Timid",move=["Grassy Glide","Swords Dance","Acrobatics","High Horsepower"])
erikah5=Serperior (ability="Contrary",maxiv="Yes",item="Focus Sash",nature="Timid",move=["Leaf Storm","Dragon Pulse","Giga Drain","Leech Life"])
erikah6=MVenusaur (ability="Thick Fat",maxiv="Yes",item="Venusaurite",nature="Modest",move=["Giga Drain","Synthesis","Sludge Bomb","Earth Power"])
erikah=Trainer("Erika(Hard Mode)",[erikah1,erikah2,erikah3,erikah4,erikah5,erikah6],"Kanto")
erikahc1=Cradily(ability="Storm Drain",maxiv="Yes",nature="Relaxed",item="Grassy Seed",move=["Stealth Rock","Toxic","Power Whip","Earth Power"])
erikahc2=Hawlucha (ability="Unburden",nature="Adamant",maxiv="Yes",item="Grassy Seed",move=["Swords Dance","Close Combat","Acrobatics","Stone Edge"])
erikahc3=GSlowbro(ability="Regenerator",maxiv="Yes",item="Black Sludge",nature="Bold",move=["Thunder Wave","Sludge Bomb","Flamethrower","Teleport"])
erikahc4=Kartana(ability="Beast Boost",item="Life Orb",maxiv="Yes",nature="Jolly",move=["Grassy Glide","Swords Dance","Smart Strike","Sacred Sword"])
erikahc5=Toxtricity(ability="Punk Rock",maxiv="Yes",item="Life Orb",nature="Timid",move=["Boomburst","Hidden Power","Volt Switch","Overdrive"])
erikahc6=MSceptile(ability="Technician",maxiv="Yes",item="Sceptilite",nature="Jolly",move=["Swords Dance","Bullet Seed","Draco Barrage","High Horsepower"])
erikahc=Trainer("Erika(Hardcore Mode)",[erikahc1,erikahc2,erikahc3,erikahc4,erikahc5,erikahc6],"Kanto")
#sabrina
sabrina1=Venomoth(maxiv="Yes")
sabrina2=MrMime(maxiv="Yes")
sabrina3=Espeon(maxiv="Yes")
sabrina4=Jynx(maxiv="Yes")
sabrina5=Wobbuffet(maxiv="Yes")
sabrina6=MAlakazam(maxiv="Yes")
sabrina7=Gallade(maxiv="Yes")
sabrina8=Lanturn(maxiv="Yes")
sabrina9=Slowking (maxiv="Yes")
sabrina10=Hypno(maxiv="Yes")
sabrina11=Metagross (maxiv="gmax")
sabrina12=Exeggutor(maxiv="Yes")
sabrina13=Mewtwo(maxiv="Yes")
sabrina14=Gengar(maxiv="Yes")
sabrina15=Xatu(maxiv="Yes")
sabrinateam=teamset([sabrina1,sabrina2,sabrina3,sabrina4,sabrina5,sabrina7,sabrina8,sabrina9,sabrina10,sabrina11,sabrina12,sabrina13,sabrina14,sabrina15],5)+[sabrina6]
sabrina=Trainer ("Gym Leader Sabrina",sabrinateam,"Kanto")
#koga
koga1=Ariados(maxiv="Yes")
koga2=Venomoth(maxiv="Yes")
koga3=Crobat(name="Crobat(Z-Crystal)",maxiv="Yes")
koga4=Weezing(maxiv="Yes")
koga5=Skuntank(maxiv="Yes")
koga6=Muk(maxiv="gmax")
koga7=Toxicroak(maxiv="Yes")
koga8=Forretress(maxiv="Yes")
koga9=Tentacruel (maxiv="Yes")
koga10=MBeedrill(maxiv="Yes")
koga11=Ditto(maxiv="Yes")
koga12=Pidgeot(maxiv="Yes")
koga13=Tangrowth (maxiv="Yes")
koga14=Forretress (maxiv="Yes")
kogateam=teamset([koga1,koga2,koga3,koga4,koga5,koga7,koga8,koga9,koga10,koga11,koga12,koga13,koga14],5)+[koga6]
koga=Trainer ("Elite Four Koga",kogateam,"Kanto")
#Guzma
Guzma1=Ariados(maxiv="Yes")
Guzma2=Masquerain (maxiv="Yes")
Guzma3=Pinsir(maxiv="Yes")
Guzma4=Scizor(maxiv="Yes")
Guzma5=Vikavolt(maxiv="Yes")
Guzma6=Golisopod(maxiv="gmax")
Guzma7=Toxapex(maxiv="Yes")
Guzma8=Kingambit(maxiv="Yes")
Guzma9=Honchkrow(name="Honchkrow (Z-Crystal)",maxiv="Yes")
Guzma10=Liepard(maxiv="Yes")
Guzmateam=teamset([Guzma1,Guzma2,Guzma3,Guzma4,Guzma5,Guzma7,Guzma8,Guzma9,Guzma10],5)+[Guzma6]
Guzma=Trainer ("Skull Leader Guzma",Guzmateam,"Alola")
#blaine
blaine1=Arcanine(maxiv="gmax")
blaine2=Ninetales(maxiv="Yes")
blaine3=Rapidash(maxiv="Yes")
blaine4=Magcargo(maxiv="Yes")
blaine6=Magmortar(maxiv="Yes")
blaine7=Torkoal(maxiv="Yes")
blaine8=Camerupt(maxiv="Yes")
blaine9=Houndoom(maxiv="Yes")
blaine10=MCharizardY(maxiv="Yes")
blaine11=Flareon(maxiv="Yes")
blaine13=Typhlosion (maxiv="Yes")
blaine12=Moltres(name="Moltres(Z-Crystal)",maxiv="Yes")
blaineteam=teamset([blaine2,blaine3,blaine4,blaine7,blaine8,blaine9,blaine10,blaine11,blaine12,blaine13],4)+[blaine6,blaine1]
blaine=Trainer ("Gym Leader Blaine",blaineteam,"Kanto")
#bugsy
bugsy1=Butterfree(maxiv="Yes")
bugsy2=Yanmega(maxiv="Yes")
bugsy3=Pinsir(maxiv="Yes")
bugsy4=Vespiquen(maxiv="Yes")
bugsy5=Heracross(name="Heracross(Z-Crystal)",maxiv="Yes")
bugsy6=MBeedrill(maxiv="Yes")
bugsy7=Scizor(maxiv="gmax")
bugsy8=Shuckle(maxiv="Yes")
bugsy9=Forretress(maxiv="Yes")
bugsy10=Armaldo(maxiv="Yes")
bugsyteam=teamset([bugsy1,bugsy2,bugsy3,bugsy4,bugsy5,bugsy9,bugsy8,bugsy10],4)+[bugsy7,bugsy6]
bugsy=Trainer ("Gym Leader Bugsy",bugsyteam,"Johto")
#whitney
whitney1=Ursaluna(maxiv="Yes")
whitney2=Tauros(maxiv="Yes")
whitney3=Ambipom(maxiv="Yes")
whitney4=Wigglytuff(maxiv="Yes")
whitney5=Farigiraf(maxiv="Yes")
whitney6=Miltank(maxiv="gmax")
whitney7=Clefable(name="Clefable(Z-Crystal)",maxiv="Yes")
whitney8=Blissey(maxiv="Yes")
whitney9=MLopunny(maxiv="Yes")
whitneyteam=teamset([whitney1,whitney2,whitney3,whitney4,whitney5,whitney8,whitney7],4)+[whitney6,whitney9]
whitney=Trainer ("Gym Leader Whitney",whitneyteam,"Johto")
#morty
morty1=Drifblim(maxiv="Yes")
morty2=Mismagius(name="Mismagius(Z-Crystal)",maxiv="gmax")
morty3=Dusknoir(maxiv="Yes")
morty4=Banette(maxiv="Yes")
morty5=Froslass(maxiv="Yes")
morty6=Cofagrigus(maxiv="Yes")
morty7=Clefable(maxiv="Yes")
morty8=Jellicent(maxiv="Yes")
morty9=MGengar(maxiv="Yes")
mortyteam=teamset([morty1,morty6,morty3,morty4,morty5,morty8,morty7],4)+[morty2,morty9]
morty=Trainer ("Gym Leader Morty",mortyteam,"Johto")
#will
will1=Exeggutor(maxiv="Yes")
will2=Jynx(maxiv="Yes")
will3=Bronzong(maxiv="Yes")
will4=Grumpig(maxiv="Yes")
will5=Xatu(maxiv="gmax")
will6=MSlowbro(maxiv="Yes")
will7=Gardevoir(maxiv="Yes")
will8=MGardevoir(maxiv="Yes")
will9=Farigiraf(maxiv="Yes")
willteam=teamset([will1,will2,will3,will4,will9],4)+[will5]+teamset([will6,will8],1)
will=Trainer ("Elite Four Will",willteam,"Johto")
#chuck
chuck1=Primeape(maxiv="Yes")
chuck2=Poliwrath(maxiv="gmax")
chuck3=Medicham(maxiv="Yes")
chuck4=Breloom(maxiv="Yes")
chuck5=Hitmonchan(maxiv="Yes")
chuck6=Hitmonlee(maxiv="Yes")
chuck7=Machamp(maxiv="Yes")
chuck8=Hitmontop(maxiv="Yes")
chuck9=Conkeldurr(maxiv="Yes")
chuckteam=teamset([chuck1,chuck2,chuck3,chuck4,chuck5,chuck6,chuck7,chuck8,chuck9],6)
chuck=Trainer ("Gym Leader Chuck",chuckteam,"Johto")
#jasmine
jasmine1=Skarmory(maxiv="Yes")
jasmine2=Empoleon(maxiv="gmax")
jasmine3=Metagross(maxiv="Yes")
jasmine4=Bronzong(maxiv="Yes")
jasmine5=Magnezone(maxiv="Yes")
jasmine6=MSteelix(maxiv="Yes")
jasmine7=Mawile(maxiv="Yes")
jasmine8=Lucario(maxiv="Yes")
jasmine9=Ferrothorn(maxiv="Yes")
jasmine10=Excadrill(maxiv="Yes")
jasmine11=Forretress(maxiv="Yes")
jasmineteam=teamset([jasmine1,jasmine2,jasmine3,jasmine4,jasmine5,jasmine7,jasmine8,jasmine9,jasmine10,jasmine11],5)+[jasmine6]
jasmine=Trainer ("Gym Leader Jasmine",jasmineteam,"Johto")
#pryce
pryce1=Walrein(maxiv="Yes")
pryce2=Froslass(maxiv="Yes")
pryce3=Glalie(maxiv="Yes")
pryce4=MAbomasnow(maxiv="Yes")
pryce5=Dewgong(maxiv="Yes")
pryce6=Mamoswine(maxiv="gmax")
pryce7=Jynx(maxiv="Yes")
pryce8=Lapras(maxiv="Yes")
pryce9=Weavile(maxiv="Yes")
pryce10=Cloyster(maxiv="Yes")
pryceteam=teamset([pryce1,pryce2,pryce3,pryce4,pryce5,pryce6,pryce7,pryce8,pryce9,pryce10],6)
pryce=Trainer ("Gym Leader Pryce",pryceteam,"Johto")
#claire
claire2=Aerodactyl(maxiv="Yes")
claire3=Charizard(maxiv="Yes")
claire4=Gyarados(maxiv="Yes")
claire5=Dragonite(maxiv="Yes")
claire6=Kingdra(maxiv="gmax")
claire7=Altaria(maxiv="Yes")
claire8=Salamence(maxiv="Yes")
claire9=Druddigon(maxiv="Yes")
claire1=Garchomp(maxiv="Yes")
claireteam=teamset([claire1,claire2,claire3,claire4,claire5,claire6,claire7,claire8,claire9],6)
claire=Trainer ("Gym Leader Claire",claireteam,"Johto")
#zinnia
zr=random.randint(1,2)
if zr==1:
    zr1,zr2=(Salamence, MRayquaza)
if zr==2:
    zr1,zr2=(MSalamence,Rayquaza)    
zinnia2=Goodra(maxiv="Yes")
zinnia3=Altaria(maxiv="Yes")
zinnia4=Tyrantrum (maxiv="Yes")
zinnia5=zr1(maxiv="Yes")
zinnia6=zr2(maxiv="Yes")
zinnia1=Noivern(maxiv="Yes")
zinniateam=teamset([zinnia1,zinnia2,zinnia3,zinnia4,zinnia5,zinnia6],6)
zinnia=Trainer ("Lorekeeper Zinnia",zinniateam,"Hoenn")
#roxanne
roxanne2=Aerodactyl(maxiv="Yes")
roxanne3=Kabutops(maxiv="Yes")
roxanne4=Omastar(maxiv="Yes")
roxanne5=Golem(maxiv="Yes")
roxanne6=Steelix(maxiv="Yes")
roxanne7=Probopass(maxiv="gmax")
roxanne8=Cradily(maxiv="Yes")
roxanne9=Armaldo(maxiv="Yes")
roxanne1=Aggron(maxiv="Yes")
roxanne10=Relicanth(maxiv="Yes")
roxanne11=Carracosta(maxiv="Yes")
roxanneteam=teamset([roxanne1,roxanne2,roxanne3,roxanne4,roxanne5,roxanne6,roxanne7,roxanne8,roxanne9,roxanne10,roxanne11],6)
roxanne=Trainer ("Gym Leader Roxanne",roxanneteam,"Hoenn")
#brawly
brawly2=Medicham(maxiv="Yes")
brawly3=Machamp(maxiv="Yes")
brawly4=Hitmonchan(maxiv="Yes")
brawly5=Hitmontop(maxiv="Yes")
brawly6=Hariyama(maxiv="gmax")
brawly7=Hitmonlee(maxiv="Yes")
brawly8=Breloom(maxiv="Yes")
brawly9=Heracross(maxiv="Yes")
brawly1=Scrafty(maxiv="Yes")
brawly10=Mienshao(maxiv="Yes")
brawlyteam=teamset([brawly1,brawly2,brawly3,brawly4,brawly5,brawly7,brawly8,brawly9,brawly10],5)+[brawly6]
brawly=Trainer ("Gym Leader Brawly",brawlyteam,"Hoenn")
#winona
winona2=Tropius(maxiv="Yes")
winona3=Skarmory(maxiv="Yes")
winona4=Pelipper(maxiv="Yes")
winona5=Swellow(maxiv="Yes")
winona6=MAltaria(maxiv="Yes")
winona7=Noctowl(maxiv="Yes")
winona1=Dragonite(maxiv="gmax")
winona8=Honchkrow(maxiv="Yes")
winona9=Gyarados(maxiv="Yes")
winona10=Rayquaza(maxiv="Yes")
winonateam=teamset([winona1,winona2,winona3,winona4,winona5,winona7,winona8,winona9,winona10],5)+[winona6]
winona=Trainer ("Gym Leader Winona",winonateam,"Hoenn")
#wattson
wattson2=Electivire(maxiv="Yes")
wattson3=Electrode(maxiv="Yes")
wattson4=Raichu(maxiv="Yes")
wattson5=Ampharos(maxiv="gmax")
wattson6=MManectric(maxiv="Yes")
wattson7=Magnezone(maxiv="Yes")
wattson1=WRotom(maxiv="Yes")
wattsonteam=teamset([wattson1,wattson2,wattson3,wattson4,wattson5,wattson7],5)+[wattson6]
wattson=Trainer ("Gym Leader Wattson",wattsonteam,"Hoenn")
#flannery
flannery2=Torkoal(maxiv="Yes")
flannery3=Houndoom(maxiv="Yes")
flannery4=Rapidash(maxiv="Yes")
flannery5=Magcargo(maxiv="Yes")
flannery6=MCamerupt(maxiv="Yes")
flannery7=Blaziken(maxiv="gmax")
flannery1=Magmortar(maxiv="Yes")
flannery8=Chandelure(maxiv="Yes")
flanneryteam=teamset([flannery1,flannery2,flannery3,flannery4,flannery5,flannery6,flannery7,flannery8],6)
flannery=Trainer ("Gym Leader Flannery",flanneryteam,"Hoenn")
#norman
norman2=Tauros(maxiv="Yes")
norman3=Kangaskhan(maxiv="Yes")
norman4=Linoone(maxiv="Yes")
norman5=Zangoose(maxiv="Yes")
norman6=Slaking(maxiv="gmax")
norman7=Exploud(maxiv="Yes")
norman1=Blissey(maxiv="Yes")
norman8=Staraptor(maxiv="Yes")
norman9=Ambipom(maxiv="Yes")
norman10=Bouffalant (maxiv="Yes")
norman11=Stoutland(maxiv="Yes")
normanteam=teamset([norman1,norman2,norman3,norman4,norman5,norman7,norman8,norman9,norman10,norman11],5)+[norman6]
norman=Trainer ("Gym Leader Norman",normanteam,"Hoenn")
#tate
tate2=Bronzong (maxiv="Yes")
tate3=Claydol(maxiv="Yes")
tate4=Grumpig(maxiv="Yes")
tate5=Xatu(maxiv="Yes")
tate6=Solrock(maxiv="gmax")
tate1=Reuniclus(maxiv="Yes")
tate7=MGallade(maxiv="Yes")
tateteam=teamset([tate1,tate2,tate3,tate4,tate5,tate7],5)+[tate6]
tate=Trainer ("Gym Leader Tate",tateteam,"Hoenn")
#liza
liza2=Bronzong(maxiv="Yes")
liza3=Claydol(maxiv="Yes")
liza4=Grumpig(maxiv="Yes")
liza5=Xatu(maxiv="Yes")
liza6=Lunatone(maxiv="gmax")
liza1=Gothitelle(maxiv="Yes")
liza7=MGardevoir(maxiv="Yes")
lizateam=teamset([liza1,liza2,liza3,liza4,liza5,liza7],5)+[liza6]
liza=Trainer ("Gym Leader Liza",lizateam,"Hoenn")
#juan
juan2=Whiscash(maxiv="Yes")
juan3=Crawdaunt(maxiv="Yes")
juan4=Walrein(maxiv="Yes")
juan5=Politoed(maxiv="Yes")
juan6=Kingdra(maxiv="gmax")
juan1=Lapras(maxiv="Yes")
juan7=Huntail(maxiv="Yes")
juan8=Gorebyss(maxiv="Yes")
juan9=Relicanth(maxiv="Yes")
juanteam=teamset([juan1,juan2,juan3,juan4,juan5,juan7,juan8,juan9],5)+[juan6]
juan=Trainer ("Gym Leader Juan",juanteam,"Hoenn")
#roark
roark1=Armaldo (maxiv="Yes")
roark2=Aerodactyl (maxiv="Yes")
roark3=Probopass(maxiv="Yes")
roark4=Relicanth (maxiv="Yes")
roark5=Rampardos(maxiv="gmax")
roark6=Tyranitar(maxiv="Yes")
roark7=Golem(maxiv="Yes")
roark8=Archeops(maxiv="Yes")
roark9=Sudowoodo(maxiv="Yes")
roark10=Salamence(maxiv="Yes")
roark11=Lunatone(maxiv="Yes")
roark13=Slowbro(maxiv="Yes")
roark14=Torkoal(maxiv="Yes")
roarkteam=teamset([roark1,roark2,roark3,roark4,roark7,roark8,roark9,roark10,roark11,roark12,roark13,roark14],4)+[roark6,roark5]
roark=Trainer("Gym Leader Roark",roarkteam,"Sinnoh")
#gardenia
gardenia1=Jumpluff(maxiv="Yes")
gardenia2=Roserade(maxiv="Yes",item="Focus Sash")
gardenia3=Bellossom(maxiv="Yes")
gardenia4=Cherrim(maxiv="Yes")
gardenia5=Tangrowth(maxiv="Yes")
gardenia6=Torterra(maxiv="gmax",item=random.choice(["Yache Berry","Life Orb"]))
gardenia7=Leafeon(maxiv="Yes",item="Yache Berry")
gardenia8=Tropius(maxiv="Yes")
gardenia9=Breloom(maxiv="Yes",item="Toxic Orb", ability="Poison Heal")
gardenia10=Sunflora(maxiv="Yes")
gardenia11=Venusaur(maxiv="Yes", ability="Chlorophyll",item="Black Sludge")
gardenia12=MRotom(maxiv="Yes",item="Choice Specs")
gardenia13=Cradily(maxiv="Yes", ability="Storm Drain",item="Leftovers")
gardenia14=Milotic (maxiv="Yes",item="Life Orb")
gardenia15=Ninetales(maxiv="Yes", ability="Drought",item="Heat Rock")
gardeniateam=teamset([gardenia1,gardenia5,gardenia3,gardenia4,gardenia7,gardenia8,gardenia9,gardenia10, gardenia11,gardenia12, gardenia13,gardenia14,gardenia15],4)+[gardenia2,gardenia6]
gardenia=Trainer("Gym Leader Gardenia",gardeniateam,"Sinnoh")
#fantina
fantina1=Banette(maxiv="Yes")
fantina2=Drifblim(maxiv="Yes")
fantina3=Dusknoir(maxiv="Yes")
fantina4=MGengar(maxiv="Yes")
fantina5=Spiritomb(maxiv="Yes")
fantina6=Mismagius(maxiv="gmax")
fantina7=Jellicent(maxiv="Yes")
fantina8=OGiratina(maxiv="Yes")
fantina9=Froslass(maxiv="Yes")
fantina10=Shedinja(maxiv="Yes")
fantinateam=teamset([fantina1,fantina5,fantina3,fantina4,fantina7,fantina8,fantina9,fantina10],4)+[fantina2,fantina6]
fantina=Trainer("Gym Leader Fantina",fantinateam,"Sinnoh")
#byron
byron1=Aggron(maxiv="Yes")
byron2=Skarmory(maxiv="Yes")
byron3=Magnezone(maxiv="Yes")
byron4=Bronzong (maxiv="Yes")
byron5=MSteelix(maxiv="Yes")
byron6=Bastiodon(maxiv="gmax")
byron7=Excadrill(maxiv="Yes")
byron8=Empoleon (maxiv="Yes")
byron9=Metagross(maxiv="Yes")
byron10=Scizor(maxiv="Yes")
byron11=Kabutops(maxiv="Yes")
byron12=Cradily(maxiv="Yes")
byron13=Armaldo(maxiv="Yes")
byron14=Omastar(maxiv="Yes")
byron15=Heatran(maxiv="Yes")
byronteam=teamset([byron1,byron2,byron3,byron4,byron7,byron8,byron9,byron10,byron11,byron12,byron13,byron14,byron15],4)+[byron5,byron6]
byron=Trainer("Gym Leader Byron",byronteam,"Sinnoh")
#maylene
maylene1=Infernape(maxiv="gmax")
maylene2=Breloom(maxiv="Yes")
maylene3=Hitmontop(maxiv="Yes")
maylene4=Machamp(maxiv="Yes")
maylene5=Medicham(maxiv="Yes")
maylene6=MLucario(maxiv="Yes")
maylene7=Gallade(maxiv="Yes")
maylene8=Toxicroak(maxiv="Yes")
maylene9=Heracross(maxiv="Yes")
maylene10=Blaziken(maxiv="Yes")
mayleneteam=teamset([maylene5,maylene2,maylene3,maylene4,maylene7,maylene8,maylene9,maylene10],4)+[maylene1,maylene6]
maylene=Trainer("Gym Leader Maylene",mayleneteam,"Sinnoh")
#wake
wake1=Floatzel(maxiv="gmax")
wake2=Quagsire(maxiv="Yes")
wake3=Sharpedo(maxiv="Yes")
wake4=Ludicolo(maxiv="Yes")
wake5=Empoleon(maxiv="Yes")
wake6=MGyarados(maxiv="Yes")
wake7=Lumineon(maxiv="Yes")
wake8=WGastrodon(maxiv="Yes")
wake9=Poliwrath(maxiv="Yes")
wake10=Kingdra(maxiv="Yes")
wake11=Politoed(maxiv="Yes")
wake12=Huntail(maxiv="Yes")
wake13=Suicune(maxiv="Yes")
wake14=Swampert (maxiv="Yes")
waketeam=teamset([wake5,wake2,wake3,wake4,wake7,wake8,wake9,wake10,wake11,wake12,wake13,wake14],4)+[wake1,wake6]
wake=Trainer("Gym Leader Crasher Wake",waketeam,"Sinnoh")
#candice
candice1=Froslass(maxiv="gmax")
candice2=Weavile(maxiv="Yes")
candice3=Mamoswine(maxiv="Yes")
candice4=Glaceon(maxiv="Yes")
candice5=Glalie(maxiv="Yes")
candice6=MAbomasnow(maxiv="Yes")
candice7=Medicham(maxiv="Yes")
candice8=Jynx(maxiv="Yes")
candice9=Regice(maxiv="Yes")
candice10=Lapras(maxiv="Yes")
candice11=Cloyster(maxiv="Yes")
candice12=Articuno(maxiv="Yes")
candiceteam=teamset([candice5,candice2,candice3,candice4,candice7,candice8,candice9,candice10,candice11,candice12],4)+[candice1,candice6]
candice=Trainer("Gym Leader Candice",candiceteam,"Sinnoh")
#volkner
volkner1=Luxray(maxiv="Yes",item="Sitrus Berry", ability="Intimidate")
volkner2=Raichu(maxiv="Yes",item=random.choice(["Shuca Berry","Choice Scarf"]))
volkner3=Ambipom(maxiv="Yes",item="Chople Berry", ability="Technician")
volkner4=Octillery(maxiv="Yes",item="Expert Belt")
volkner5=Jolteon(maxiv="Yes",item=random.choice(["Air Balloon","Life Orb"]))
volkner6=Electivire(maxiv="gmax",item=random.choice(["Shuca Berry","Life Orb"]))
volkner7=Lanturn(maxiv="Yes")
volkner8=Electrode(maxiv="Yes",item="Electric Gem")
volkner9=Eelektross(maxiv="Yes")
volkner10=Galvantula(maxiv="Yes",item="Occa Berry")
volkner11=Zebstrika(maxiv="Yes")
volkner12=Pelipper(maxiv="Yes", ability="Drizzle",item="Damp Rock")
volkner13=Magnezone(maxiv="Yes", ability="Sturdy",item="Custap Berry")
volkner14=Zapdos(maxiv="Yes",item=random.choice(["Sitrus Berry","Choice Scarf","Life Orb"]), ability="Static")
volkner15=FRotom(maxiv="Yes")
volkner16=WRotom(maxiv="Yes")
volkner17=Gyarados(maxiv="Yes",item="Lum Berry")
volkner18=Swampert(maxiv="Yes",item="Life Orb")
volkner19=HRotom(maxiv="Yes")
volknerteam=teamset([volkner5,volkner2,volkner3,volkner4,volkner7,volkner8,volkner9,volkner10,volkner11,volkner12,volkner13,volkner14, volkner15, volkner16, volkner17, volkner19, volkner18],4)+[volkner1,volkner6]
volkner=Trainer("Gym Leader Volkner",volknerteam,"Sinnoh")
#lenora
lenora1=Watchog(maxiv="gmax")
lenora2=Stoutland(maxiv="Yes")
lenora3=Kangaskhan(maxiv="Yes")
lenora4=Clefable(maxiv="Yes")
lenora5=Lickilicky(maxiv="Yes")
lenora6=Braviary(maxiv="Yes")
lenorateam=teamset([lenora5,lenora2,lenora3,lenora4],4)+[lenora6,lenora1]
lenora=Trainer("Gym Leader Lenora",lenorateam,"Unova")
#burgh
burgh1=Scolipede(maxiv="Yes")
burgh2=Vespiquen(maxiv="Yes")
burgh3=Escavalier(maxiv="Yes")
burgh4=Accelgor(maxiv="Yes")
burgh5=Durant(maxiv="Yes")
burgh6=Leavanny(maxiv="gmax")
burgh7=Heracross(maxiv="Yes")
burghteam=teamset([burgh5,burgh2,burgh3,burgh4,burgh7],4)+[burgh1,burgh6]
burgh=Trainer("Gym Leader Burgh",burghteam,"Unova")
#elesa
elesa1=MAmpharos(maxiv="Yes")
elesa2=Galvantula(maxiv="Yes")
elesa3=Eelektross(maxiv="Yes")
elesa4=Luxray(maxiv="Yes")
elesa5=Vikavolt(maxiv="Yes")
elesa6=Zebstrika(maxiv="gmax")
elesa7=Manectric(maxiv="Yes")
elesa8=Emolga(maxiv="Yes")
elesateam=teamset([elesa1,elesa5,elesa2,elesa3,elesa4,elesa7],4)+[elesa8,elesa6]
elesa=Trainer("Gym Leader Elesa",elesateam,"Unova")
#clemont
clemont1=Manectric(maxiv="Yes")
clemont2=Luxray(maxiv="Yes")
clemont3=Emolga(maxiv="Yes")
clemont4=Magnezone(maxiv="Yes")
clemont5=MAmpharos(maxiv="Yes")
clemont6=Heliolisk(maxiv="gmax")
clemontteam=teamset([clemont2,clemont3,clemont4,clemont5,clemont1],5)+[clemont6]
clemont=Trainer ("Gym Leader Clemont",clemontteam,"Kalos")
#clay
clay1=Excadrill(maxiv="gmax")
clay2=Seismitoad(maxiv="Yes")
clay3=Sandslash(maxiv="Yes")
clay4=Claydol(maxiv="Yes")
clay5=Golurk(maxiv="Yes")
clay6=Krookodile(maxiv="Yes")
clay7=Mamoswine(maxiv="Yes")
clay8=Flygon(maxiv="Yes")
clayteam=teamset([clay5,clay2,clay3,clay4,clay7,clay8],4)+[clay6,clay1]
clay=Trainer("Gym Leader Clay",clayteam,"Unova")
#skyla
skyla1=Unfezant(maxiv="Yes")
skyla2=Braviary(maxiv="Yes")
skyla3=Skarmory(maxiv="Yes")
skyla4=Archeops(maxiv="Yes")
skyla5=Mandibuzz (maxiv="Yes")
skyla6=Swanna(maxiv="gmax")
skyla7=Jumpluff(maxiv="Yes")
skyla8=Drifblim(maxiv="Yes")
skylateam=teamset([skyla5,skyla2,skyla3,skyla4,skyla7,skyla8],4)+[skyla1,skyla6]
skyla=Trainer("Gym Leader Skyla",skylateam,"Unova")
#brycen
brycen1=Vanilluxe(maxiv="Yes")
brycen2=Weavile(maxiv="Yes")
brycen3=Dewgong (maxiv="Yes")
brycen4=Walrein(maxiv="Yes")
brycen5=Mandibuzz (maxiv="Yes")
brycen6=Beartic(maxiv="gmax")
brycen7=Kingambit(maxiv="Yes")
brycen8=Honchkrow(maxiv="Yes")
brycen9=Zoroark(maxiv="Yes")
brycen10=Scrafty(maxiv="Yes")
brycen11=Houndoom(maxiv="Yes")
brycen12=Hydreigon (maxiv="Yes")
brycen13=Sharpedo(maxiv="Yes")
brycen14=Cryogonal(maxiv="Yes")
brycenteam=teamset([brycen5,brycen2,brycen3,brycen4,brycen7,brycen8,brycen9,brycen10,brycen11,brycen12,brycen13,brycen1],4)+[brycen14,brycen6]
brycen=Trainer("Gym Leader Brycen",brycenteam,"Unova")
#drayden
drayden1=Druddigon(maxiv="Yes")
drayden2=Flygon(maxiv="Yes")
drayden3=Altaria(maxiv="Yes")
drayden4=Hydreigon (maxiv="Yes")
drayden5=Salamence(maxiv="Yes")
drayden6=Haxorus(maxiv="gmax")
draydenteam=teamset([drayden5,drayden2,drayden3,drayden4],4)+[drayden1,drayden6]
drayden=Trainer("Gym Leader Drayden",draydenteam,"Unova")
#iris
iris1=Druddigon(maxiv="Yes")
iris2=Salamence(maxiv="Yes")
iris3=Archeops(maxiv="Yes")
iris4=Hydreigon (maxiv="Yes")
iris5=Excadrill(maxiv="Yes")
iris6=Haxorus(maxiv="gmax")
iris7=Emolga(maxiv="Yes")
iris8=Dragonite(maxiv="Yes")
iris9=Garchomp(maxiv="Yes")
iris10=Lapras(maxiv="Yes")
iris11=Aggron(maxiv="Yes")
iristeam=teamset([iris5,iris2,iris3,iris4,iris7,iris8,iris9,iris10,iris11],4)+[iris1,iris6]
iris=Trainer("Unova Champion Iris",iristeam,"Unova")
#cheren
cheren1=Unfezant(maxiv="Yes")
cheren2=Liepard(maxiv="Yes")
cheren3=Emboar(maxiv="Yes")
cheren6=Haxorus(maxiv="Yes")
cheren7=Gigalith (maxiv="Yes")
cheren8=Stoutland(maxiv="Yes")
cheren9=Watchog(maxiv="Yes")
cheren10=Zangoose (maxiv="Yes")
cheren11=Bouffalant (maxiv="Yes")
cheren12=MLopunny (maxiv="Yes")
cheren13=PorygonZ(maxiv="Yes")
cheren14=Lickilicky(maxiv="Yes")
cheren15=Kingambit(maxiv="Yes")
cheren16=Basculegion (maxiv="Yes")
cheren17=Beartic(maxiv="Yes")
cherenteam=teamset([cheren2,cheren3,cheren7,cheren8,cheren9,cheren10,cheren11,cheren12,cheren13,cheren14],4)+[cheren1,cheren6]
cheren=Trainer("Gym Leader Cheren",cherenteam,"Unova")    
#roxie
roxie1=Weezing(maxiv="Yes")
roxie2=Muk(maxiv="Yes")
roxie3=Seviper(maxiv="Yes")
roxie6=Scolipede(maxiv="gmax")
roxie4=Crobat(maxiv="Yes")
roxie5=Drapion(maxiv="Yes")
roxie7=Toxicroak(maxiv="Yes")
roxieteam=teamset([roxie2,roxie3,roxie7,roxie4,roxie5],4)+[roxie1,roxie6]
roxie=Trainer("Gym Leader Roxie",roxieteam,"Unova")    
#quillon
quillon1=Weavile(maxiv="Yes")
quillon2=Regice(maxiv="Yes")
quillon3=Regirock(maxiv="Yes")
quillon5=Registeel(maxiv="Yes")
quillon4=Rillaboom(maxiv="Yes")
quillon6=DUrshifu(maxiv="gmax")
quillonteam=teamset([quillon2,quillon3,quillon4,quillon5],4)+[quillon1,quillon6]
quillon=Trainer("Pokémon Trainer Quillon",quillonteam,"Galar")      
#marlon
marlon1=Carracosta(maxiv="gmax")
marlon2=Wailord(maxiv="Yes")
marlon3=Mantine(maxiv="Yes")
marlon6=Starmie(maxiv="Yes")
marlon4=Quagsire(maxiv="Yes")
marlon5=Cloyster(maxiv="Yes")
marlonteam=teamset([marlon2,marlon3,marlon4,marlon5],4)+[marlon1,marlon6]
marlon=Trainer("Gym Leader Marlon",marlonteam,"Unova")    
#diantha
diantha1=Goodra(maxiv="Yes", ability="Sap Sipper",move=["Dragon Pulse","Muddy Water","Fire Blast","Focus Blast"])
diantha2=Hawlucha(maxiv="Yes", ability="Limber",move=["Poison Jab","Swords Dance","X-Scissor","Flying Press"])
diantha3=Tyrantrum(maxiv="gmax", ability="Strong Jaw",move=["Head Smash","Earthquake","Dragon Claw","Crunch"])
diantha6=MGardevoir(maxiv="Yes",move=["Thunderbolt","Psychic","Moonblast","Shadow Ball"])
diantha4=Aurorus(maxiv="Yes", ability="Refrigerate",move=["Thunder","Blizzard","Light Screen","Reflect"])
diantha5=Gourgeist(maxiv="Yes",move=["Seed Bomb","Phantom Force","Shadow Sneak","Trick-or-Treat"])
dianthateam=teamset([diantha2,diantha3,diantha4,diantha5],4)+[diantha1,diantha6]
diantha=Trainer("Kalos Champion Diantha",dianthateam,"Kalos")    
#grant
grant4=Golem(maxiv="Yes")
grant2=Steelix(maxiv="Yes")
grant3=Bastiodon(maxiv="Yes")
grant6=Tyrantrum(maxiv="gmax")
grant1=Aurorus(maxiv="Yes")
grant5=Rampardos(maxiv="Yes")
grantteam=teamset([grant2,grant3,grant4,grant5],4)+[grant1,grant6]
grant=Trainer("Gym Leader Grant",grantteam,"Kalos")    
#danika
danika1=Azumarill (maxiv="Yes")
danika2=Gorebyss(maxiv="Yes")
danika3=Politoed(maxiv="Yes")
danika5=Ludicolo(maxiv="Yes")
danika4=Inteleon(maxiv="Yes")
danika6=WUrshifu(maxiv="gmax")
danikateam=teamset([danika2,danika3,danika4,danika5],4)+[danika1,danika6]
danika=Trainer("Pokémon Trainer Danika",danikateam,"Galar")    
#viola
viola1=Dustox(maxiv="Yes")
viola2=Beautifly(maxiv="Yes")
viola3=Mothim(maxiv="Yes")
viola4=Butterfree(maxiv="gmax")
viola5=Masquerain(maxiv="Yes")
viola6=Vivillon(maxiv="Yes")
violateam=teamset([viola2,viola3,viola4,viola5,viola1],5)+[viola6]
viola=Trainer ("Gym Leader Viola",violateam,"Kalos")
#ash
ash1=Infernape(maxiv="Yes", ability="Blaze")
ash2=Dragonite(maxiv="Yes")
ash3=Charizard(maxiv="Yes", ability="Blaze")
ash4=MLucario(maxiv="Yes")
ash5=Gengar(maxiv="gmax", ability="Cursed Body")
ash6=Pikachu(name="Pikachu(Z-Crystal)",move=["Thunderbolt","Electroweb","Extreme Speed","Iron Tail"],maxiv="Yes", ability="Static")
ash7=Sceptile(maxiv="Yes", ability="Overgrow")
ash8=Staraptor(maxiv="Yes")
ash9=Tauros(maxiv="Yes")
ash10=Snorlax (maxiv="Yes")
ash11=Noivern(maxiv="Yes")
ash12=Goodra(maxiv="Yes")
ash13=Greninja(maxiv="Yes", ability="Battle Bond")
ash14=Noctowl(name="Noctowl✨",maxiv="Yes")
ash15=Torkoal(maxiv="Yes")
ash16=Dracovish (maxiv="Yes", ability="Strong Jaw")
ash17=Sirfetchd(maxiv="Yes")
ash18=Muk(maxiv="Yes")
ash19=Heracross(maxiv="Yes")
ash20=Donphan(maxiv="Yes")
ash21=Swellow(maxiv="Yes")
ash22=Glalie(maxiv="Yes")
ash23=Torterra(maxiv="Yes")
ash24=Gliscor(maxiv="Yes")
ash25=Unfezant(maxiv="Yes")
ash26=Leavanny(maxiv="Yes")
ash27=Krookodile(maxiv="Yes")
ash28=Talonflame(maxiv="Yes")
ash29=Hawlucha(maxiv="Yes")
ash30=Incineroar(maxiv="Yes", ability="Blaze")
ash31=DLycanroc(maxiv="Yes")
ash32=Melmetal(maxiv="Yes")
ash33=Naganadel(maxiv="Yes")
ashteam=teamset([ash1,ash5,ash2,ash3,ash4,ash7,ash8,ash9,ash10,ash11,ash12,ash13,ash14,ash15,ash16,ash17,ash18,ash19,ash20,ash21,ash22,ash23,ash24,ash25,ash26,ash27,ash28,ash29,ash30,ash31,ash32,ash33],5)+[ash6]
ash=Trainer("World Champion Ash",ashteam,"Unova")
#cissy
cissy1=Seaking(maxiv="Yes")
cissy2=Starmie(maxiv="Yes")
cissy3=Azumarill(maxiv="Yes")
cissy4=Kingdra(maxiv="Yes")
cissy5=MBlastoise(maxiv="Yes")
cissy6=Kingler(maxiv="gmax")
cissy=Trainer ("Gym Leader Cissy",[cissy1,cissy2,cissy3,cissy4,cissy5,cissy6],"Orange Islands")
#horace
horace1=Meganium (maxiv="gmax")
horace2=Virizion(maxiv="Yes")
horace3=Heracross(maxiv="Yes")
horace5=Donphan(maxiv="Yes")
horace4=Indeedee(maxiv="Yes")
horace6=MGardevoir(maxiv="Yes")
horaceteam=teamset([horace2,horace3,horace4,horace5],4)+[horace1,horace6]
horace=Trainer("Pokémon Trainer Horace",horaceteam,"Johto")    
#danny
danny1=Pinsir(maxiv="Yes")
danny2=Electrode(maxiv="Yes")
danny3=Golem(maxiv="Yes")
danny4=Nidoqueen(maxiv="Yes")
danny5=MScizor(maxiv="Yes")
danny6=Machamp(maxiv="gmax")
danny=Trainer ("Gym Leader Danny",[danny1,danny2,danny3,danny4,danny5,danny6],"Orange Islands")
#rudy
rudy1=MPidgeot(maxiv="Yes")
rudy2=Electivire(maxiv="Yes")
rudy3=Golem(maxiv="Yes")
rudy4=Exeggutor(maxiv="Yes")
rudy5=MAlakazam(maxiv="Yes")
rudy6=Starmie(maxiv="gmax")
rudy7=Rhydon(maxiv="Yes")
rudy8=Venomoth(maxiv="Yes")
rudy9=Hitmonchan(maxiv="Yes")
rudy10=Ninetales(maxiv="Yes")
rudyteam=teamset([rudy2,rudy3,rudy4,rudy6,rudy7,rudy8,rudy9,rudy10],5)+teamset([rudy1,rudy5],1)
rudy=Trainer ("Gym Leader Rudy",rudyteam,"Orange Islands")
#luana
luana1=Kabutops(maxiv="Yes")
luana2=Lunatone(maxiv="Yes")
luana3=Rhyperior(maxiv="Yes")
luana4=Raichu(maxiv="Yes")
luana5=MAlakazam(maxiv="Yes")
luana6=Marowak(maxiv="gmax")
luanateam=teamset([luana2,luana3,luana4,luana5,luana1],5)+[luana6]
luana=Trainer ("Gym Leader Luana",luanateam,"Orange Islands")
#larry
larry1=Tropius(maxiv="Yes")
larry2=Staraptor(maxiv="Yes")
larry3=MAltaria(maxiv="Yes")
larry4=Kilowattrel(maxiv="Yes")
larry5=Bombirdier(maxiv="Yes")
larry6=Flamigo(name="Flamigo💎",maxiv="Flying")
larry7=Dudunsparce(maxiv="Yes")
larry8=Braviary(maxiv="Yes")
larryteam=teamset([larry2,larry3,larry4,larry5,larry1,larry7,larry8],5)+[larry6]
larry=Trainer ("Elite Four Larry",larryteam,"Paldea")
#hassel
hassel1=Noivern (maxiv="Yes")
hassel2=Dragalge(maxiv="Yes")
hassel3=Flapple(maxiv="Yes")
hassel4=Haxorus(maxiv="Yes")
hassel5=Dragonite(maxiv="Yes")
hassel6=Baxcalibur(name="Baxcalibur💎",maxiv="Dragon")
hasselteam=teamset([hassel2,hassel3,hassel4,hassel5,hassel1],5)+[hassel6]
hassel=Trainer ("Elite Four Hassel",hasselteam,"Paldea")
#poppy
poppy1=Bronzong(maxiv="Yes")
poppy2=Copperajah(maxiv="gmax")
poppy3=Magnezone(maxiv="Yes")
poppy4=Corviknight(maxiv="Yes")
poppy5=MMawile(maxiv="Yes")
poppy6=Tinkaton(name="Tinkaton💎",maxiv="Steel")
poppyteam=teamset([poppy2,poppy3,poppy4,poppy5,poppy1],5)+[poppy6]
poppy=Trainer ("Elite Four Poppy",poppyteam,"Paldea")
#geeta
geeta1=Gogoat(maxiv="Yes", ability="Sap Sipper",move=["Horn Leech","Zen Headbutt","Play Rough","Bulk Up"])
geeta2=Espathra(maxiv="Yes", ability="Opportunist",move=["Lumina Crash","Dazzling Gleam","Extreme Speed","Reflect"])
geeta3=Veluza(maxiv="Yes", ability="Mold Breaker",move=["Aqua Jet","Liquidation","Psycho Cut","Ice Fang"])
geeta4=Avalugg(maxiv="Yes", ability="Own Tempo", move=["Earthquake","Crunch","Body Press","Icicle Crash"])
geeta5=Kingambit(maxiv="Yes", ability="Supreme Overload",move=["Iron Head","Kowtow Cleave","Stone Edge","Zen Headbutt"])
geeta6=Glimmora(name="Glimmora💎",maxiv="Rock", ability="Toxic Debris",move=["Tera Blast","Sludge Wave","Earth Power","Dazzling Gleam"])
geetateam=teamset([geeta2,geeta3,geeta4,geeta5,geeta1],5)+[geeta6]
geeta=Trainer ("Paldea Champion Geeta",geetateam,"Paldea")
#korrina
korrina1=Chesnaught(maxiv="Yes")
korrina2=Pangoro(maxiv="Yes")
korrina3=Hawlucha(maxiv="Yes")
korrina4=Mienshao(maxiv="Yes")
korrina5=Machamp(maxiv="gmax")
korrina6=MLucario(maxiv="Yes")
korrinateam=teamset([korrina2,korrina3,korrina4,korrina5,korrina1],5)+[korrina6]
korrina=Trainer ("Gym Leader Korrina",korrinateam,"Kalos")
#ramos
ramos1=Exeggutor(maxiv="Yes")
ramos2=Sunflora(maxiv="Yes")
ramos3=Victreebel(maxiv="Yes")
ramos4=Jumpluff(maxiv="Yes")
ramos5=MVenusaur(maxiv="Yes")
ramos6=Gogoat(maxiv="gmax")
ramos7=Vileplume(maxiv="Yes")
ramos8=Bellossom(maxiv="Yes")
ramosteam=teamset([ramos2,ramos3,ramos4,ramos5,ramos1,ramos7,ramos8],5)+[ramos6]
ramos=Trainer ("Gym Leader Ramos",ramosteam,"Kalos")
#valerie
valerie1=Togekiss(maxiv="Yes")
valerie2=Azumarill(maxiv="Yes")
valerie3=Florges(maxiv="Yes")
valerie4=MrMime(maxiv="Yes")
valerie5=MMawile(maxiv="Yes")
valerie6=Sylveon(maxiv="gmax")
valerieteam=teamset([valerie2,valerie3,valerie4,valerie5,valerie1],5)+[valerie6]
valerie=Trainer ("Gym Leader Valerie",valerieteam,"Kalos")
#olympia
olympia1=Reuniclus(maxiv="Yes")
olympia2=Malamar(maxiv="Yes")
olympia3=Meowstic(maxiv="Yes")
olympia4=Delphox(maxiv="Yes")
olympia5=Slowking(maxiv="Yes")
olympia6=Meowstic(maxiv="gmax")
olympiateam=teamset([olympia2,olympia3,olympia4,olympia5,olympia1],5)+[olympia6]
olympia=Trainer ("Gym Leader Olympia",olympiateam,"Kalos")
#wulfric
wulfric1=GDarmanitan(maxiv="Yes")
wulfric2=Beartic(maxiv="Yes")
wulfric3=Aurorus(maxiv="Yes")
wulfric4=Cryogonal(maxiv="Yes")
wulfric5=MAbomasnow(maxiv="Yes")
wulfric6=Avalugg(maxiv="gmax")
wulfricteam=teamset([wulfric2,wulfric3,wulfric4,wulfric5,wulfric1],5)+[wulfric6]
wulfric=Trainer ("Gym Leader Wulfric",wulfricteam,"Kalos")
#milo
milo1=Tsareena(maxiv="Yes")
milo2=Bellossom(maxiv="Yes")
milo3=Cherrim(maxiv="Yes")
milo4=Shiftry(maxiv="Yes")
milo5=Eldegoss(maxiv="Yes")
milo6=Flapple(maxiv="gmax")
milo7=Appletun(maxiv="gmax")
milo8=Ludicolo(maxiv="Yes")
miloteam=teamset([milo2,milo3,milo4,milo5,milo1,milo8],5)+teamset([milo6,milo7],1)
milo=Trainer ("Gym Leader Milo",miloteam,"Galar")
#nessa
nessa1=Pelipper(maxiv="Yes")
nessa2=Quagsire(maxiv="Yes")
nessa3=Golisopod(maxiv="Yes")
nessa4=Seaking(maxiv="Yes")
nessa5=Barraskewda(maxiv="Yes")
nessa6=Drednaw(maxiv="gmax")
nessa7=Toxapex(maxiv="Yes")
nessa8=Milotic(maxiv="Yes")
nessateam=teamset([nessa2,nessa3,nessa4,nessa5,nessa1,nessa8,nessa7],5)+[nessa6]
nessa=Trainer ("Gym Leader Nessa",nessateam,"Galar")
#kabu
kabu1=Typhlosion(maxiv="Yes")
kabu2=Torkoal(maxiv="Yes")
kabu3=Salazzle(maxiv="Yes")
kabu4=Ninetales(maxiv="Yes")
kabu5=Arcanine(maxiv="Yes")
kabu6=Centiskorch(maxiv="gmax")
kabuteam=teamset([kabu2,kabu3,kabu4,kabu5,kabu1],5)+[kabu6]
kabu=Trainer ("Gym Leader Kabu",kabuteam,"Galar")
#bea
bea1=Hawlucha(maxiv="Yes")
bea2=Grapplot(maxiv="Yes")
bea3=Hitmontop(maxiv="Yes")
bea4=Pangoro(maxiv="Yes")
bea5=Sirfetchd(maxiv="Yes")
bea6=Machamp(maxiv="gmax")
beateam=teamset([bea2,bea3,bea4,bea5,bea1],5)+[bea6]
bea=Trainer ("Gym Leader Bea",beateam,"Galar")
#rose
rose1=Klinklang(maxiv="Yes")
rose2=Perrserker(maxiv="Yes")
rose3=Escavalier (maxiv="Yes")
rose4=Ferrothorn (maxiv="Yes")
rose5=Eternatus(maxiv="Yes")
rose6=Copperajah(maxiv="gmax")
roseteam=teamset([rose1,rose2,rose3,rose4,rose5],5)+[rose6]
rose=Trainer ("Chairman Rose",roseteam,"Galar")
#allister
allister1=Chandelure(maxiv="Yes")
allister2=Dusknoir(maxiv="Yes")
allister3=Polteageist(maxiv="Yes")
allister4=Runerigus(maxiv="Yes")
allister5=Mimikyu(maxiv="Yes")
allister6=Gengar(maxiv="gmax")
allister7=Dragapult(maxiv="Yes")
allisterteam=teamset([allister2,allister3,allister4,allister5,allister1,allister7],5)+[allister6]
allister=Trainer ("Gym Leader Allister",allisterteam,"Galar")
#lysandre
lysandre1=Mienshao(maxiv="Yes")
lysandre2=Honchkrow(maxiv="Yes")
lysandre3=Pyroar(maxiv="Yes")
lysandre4=MGyarados(name="Mega Gyarados✨",maxiv="Yes")
lysandre5=CZygarde(maxiv="gmax")
lysandre6=Yveltal(maxiv="Yes")
lysandre7=Xerneas(maxiv="Yes")
lysandreteam=teamset([lysandre2,lysandre3,lysandre4,lysandre1,lysandre5],5)+teamset([lysandre6,lysandre7],1)
lysandre=Trainer ("Flare Boss Lysandre",lysandreteam,"Kalos")
#mable
mable1=Delphox(maxiv="Yes")
mable2=Talonflame(maxiv="Yes")
mable3=Malamar(maxiv="Yes")
mable4=Pangoro(maxiv="Yes")
mable5=Weavile(maxiv="gmax")
mable6=MHoundoom(maxiv="Yes")
mableteam=teamset([mable2,mable3,mable4,mable5,mable1],5)+[mable6]
mable=Trainer ("Team Flare Mable",mableteam,"Kalos")
#giallo
giallo1=Tornadus(maxiv="Yes")
giallo2=Thundurus(maxiv="Yes")
giallo3=Landorus(maxiv="Yes")
giallo4=Mandibuzz(maxiv="Yes")
giallo5=Hydreigon(maxiv="Yes")
giallo6=Krookodile(maxiv="gmax")
gialloteam=teamset([giallo2,giallo3,giallo4,giallo5,giallo1],5)+[giallo6]
giallo=Trainer ("Plasma Sage Giallo",gialloteam,"Unova")
#opal
opal1=GRapidash(maxiv="Yes")
opal2=Primarina(maxiv="Yes")
opal3=MMawile(maxiv="Yes")
opal4=GWeezing(maxiv="Yes")
opal5=Togekiss(maxiv="Yes")
opal6=Alcremie(maxiv="gmax")
opalteam=teamset([opal2,opal3,opal4,opal5,opal1],5)+[opal6]
opal=Trainer ("Gym Leader Opal",opalteam,"Galar")
#bede
bede1=GRapidash(maxiv="Yes")
bede2=Gardevoir(maxiv="Yes")
bede3=MMawile(maxiv="Yes")
bede4=Reuniclus(maxiv="Yes")
bede5=Gothitelle(maxiv="Yes")
bede6=Hatterene(maxiv="gmax")
bede7=Sylveon(maxiv="Yes")
bedeteam=teamset([bede2,bede3,bede4,bede5,bede1,bede7],5)+[bede6]
bede=Trainer ("Gym Leader Bede",bedeteam,"Galar")
#gordie
gordie1=Aggron(maxiv="Yes")
gordie2=Stonjourner(maxiv="Yes")
gordie3=MTyranitar(maxiv="Yes")
gordie4=Shuckle(maxiv="Yes")
gordie5=Barbaracle(maxiv="Yes")
gordie6=Coalossal(maxiv="gmax")
gordieteam=teamset([gordie2,gordie3,gordie4,gordie5,gordie1],5)+[gordie6]
gordie=Trainer ("Gym Leader Gordie",gordieteam,"Galar")
#melony
melony1=ANinetales(maxiv="Yes")
melony2=MrRime(maxiv="Yes")
melony3=Eiscue(maxiv="Yes")
melony4=Frosmoth(maxiv="Yes")
melony5=GDarmanitan(maxiv="Yes")
melony6=Lapras(maxiv="gmax")
melonyteam=teamset([melony2,melony3,melony4,melony5,melony1],5)+[melony6]
melony=Trainer ("Gym Leader Melony",melonyteam,"Galar")
#piers
piers1=Overqwil(maxiv="Yes")
piers2=Toxtricity(maxiv="Yes")
piers3=Scrafty(maxiv="Yes")
piers4=Malamar(maxiv="Yes")
piers5=Skuntank(maxiv="Yes")
piers6=Obstagoon(maxiv="Yes")
piersteam=teamset([piers2,piers3,piers4,piers5,piers1],5)+[piers6]
piers=Trainer ("Gym Leader Piers",piersteam,"Galar")
#marnie
marnie1=Crawdaunt(maxiv="Yes")
marnie2=APersian(maxiv="Yes")
marnie3=Scrafty(maxiv="Yes")
marnie4=Liepard(maxiv="Yes")
marnie5=Toxicroak(maxiv="Yes")
marnie6=Grimmsnarl(maxiv="gmax")
marnieteam=teamset([marnie2,marnie3,marnie4,marnie5,marnie1],5)+[marnie6]
marnie=Trainer ("Gym Leader Marnie",marnieteam,"Galar")
#raihan
raihan1=Turtonator(maxiv="Yes")
raihan2=Goodra(maxiv="Yes")
raihan3=Gigalith(maxiv="Yes")
raihan4=Sandaconda(maxiv="Yes")
raihan5=Flygon(maxiv="Yes")
raihan6=Duraludon(maxiv="gmax")
raihan7=Torkoal(maxiv="Yes")
raihanteam=teamset([raihan2,raihan3,raihan4,raihan5,raihan1,raihan7],5)+[raihan6]
raihan=Trainer ("Gym Leader Raihan",raihanteam,"Galar")
#nemona
nemona1=MDLycanroc(maxiv="Yes")
nemona2=Goodra(maxiv="Yes")
nemona3=Orthworm(name="Orthworm💎",maxiv="Steel")
nemona4=Dudunsparce(maxiv="Yes")
nemona5=Skeledirge(maxiv="Yes")
nemona6=Meowscarada(maxiv="Yes")
nemona7=Quaquaval(maxiv="Yes")
nemonateam=teamset([nemona2,nemona6,nemona4,nemona5,nemona1,nemona7],5)+[nemona3]
nemona=Trainer ("Pokémon Trainer Nemona",nemonateam,"Paldea")
#katy
katy1=Lokix(maxiv="Yes")
katy2=Forretress(maxiv="Yes")
katy3=Heracross(maxiv="Yes")
katy4=Spidops(maxiv="Yes")
katy5=Kleavor(maxiv="Yes")
katy6=Ursaring(name="Ursaring💎",maxiv="Bug")
katyteam=teamset([katy2,katy3,katy4,katy5,katy1],5)+[katy6]
katy=Trainer ("Gym Leader Katy",katyteam,"Paldea")
#brassius
brassius1=HLilligant(maxiv="Yes")
brassius2=Tsareena(maxiv="Yes")
brassius3=Breloom(maxiv="Yes")
brassius4=Arboliva(maxiv="Yes")
brassius5=Rillaboom(maxiv="gmax")
brassius6=Sudowoodo(name="Sudowoodo💎",maxiv="Grass")
brassiusteam=teamset([brassius2,brassius3,brassius4,brassius5,brassius1],5)+[brassius6]
brassius=Trainer ("Gym Leader Brassius",brassiusteam,"Paldea")
#Iono
Iono1=Kilowattrel(maxiv="Yes")
Iono2=Dracozolt(maxiv="Yes")
Iono3=Bellibolt(maxiv="Yes")
Iono4=Electrode(maxiv="Yes")
Iono5=Luxray(maxiv="Yes")
Iono6=Mismagius(name="Mismagius💎",maxiv="Electric")
Ionoteam=teamset([Iono2,Iono3,Iono4,Iono5,Iono1],5)+[Iono6]
Iono=Trainer ("Gym Leader Iono",Ionoteam,"Paldea")
#kofu
kofu1=Veluza(maxiv="Yes")
kofu2=Clawitzer(maxiv="Yes")
kofu3=Pelipper(maxiv="Yes")
kofu4=Wugtrio(maxiv="Yes")
kofu5=Basculegion(maxiv="Yes")
kofu6=Crabominable(name="Crabominable💎",maxiv="Water",ability="Swift Swim")
kofuteam=teamset([kofu2,kofu3,kofu4,kofu5,kofu1],5)+[kofu6]
kofu=Trainer ("Gym Leader Kofu",kofuteam,"Paldea")
#ryme
ryme1=Mimikyu(maxiv="Yes")
ryme2=Banette(maxiv="Yes")
ryme3=Spiritomb(maxiv="Yes")
ryme4=Houndstone(maxiv="Yes")
ryme5=HTyphlosion(maxiv="Yes")
ryme6=Toxtricity(name="Toxtricity💎",maxiv="Ghost")
rymeteam=teamset([ryme2,ryme3,ryme4,ryme5,ryme1],5)+[ryme6]
ryme=Trainer ("Gym Leader Ryme",rymeteam,"Paldea")
#grusha
grusha1=Frosmoth(maxiv="Yes")
grusha2=Beartic(maxiv="Yes")
grusha3=Weavile(maxiv="Yes")
grusha4=Cetitan(maxiv="Yes")
grusha5=HAvalugg(maxiv="Yes")
grusha6=Altaria(name="Altaria💎",maxiv="Ice")
grushateam=teamset([grusha2,grusha3,grusha4,grusha5,grusha1],5)+[grusha6]
grusha=Trainer ("Gym Leader Grusha",grushateam,"Paldea")
#tulip
tulip1=Farigiraf(maxiv="Yes")
tulip2=Gallade(maxiv="Yes")
tulip3=Espathra(maxiv="Yes")
tulip4=Gardevoir(maxiv="Yes")
tulip5=Wyrdeer(maxiv="Yes")
tulip6=Florges(name="Florges💎",maxiv="Psychic")
tulipteam=teamset([tulip2,tulip3,tulip4,tulip5,tulip1],5)+[tulip6]
tulip=Trainer ("Gym Leader Tulip",tulipteam,"Paldea")
#gorm
gorm1=Sigilyph(maxiv="Yes")
gorm2=Mandibuzz(maxiv="Yes")
gorm3=Hydreigon(maxiv="Yes")
gorm4=Kingambit(maxiv="Yes")
gorm5=MBanette(maxiv="Yes")
gorm6=Cofagrigus(maxiv="gmax")
gormteam=teamset([gorm2,gorm3,gorm4,gorm5,gorm1],5)+[gorm6]
gorm=Trainer ("Plasma Sage Gorm",gormteam,"Unova")
#sordward
sordward1=Falinks(maxiv="Yes")
sordward2=Golisopod(maxiv="Yes")
sordward3=Sirfetchd (maxiv="Yes")
sordward4=Kingambit(maxiv="Yes")
sordward5=Aegislash(maxiv="Yes")
sordward6=Zacian(maxiv="Yes")
sordwardteam=teamset([sordward2,sordward3,sordward4,sordward5,sordward1],5)+[sordward6]
sordward=Trainer ("Pokémon Trainer Sordward",sordwardteam,"Galar")
#shielbert
shielbert1=Falinks(maxiv="Yes")
shielbert2=Bronzong(maxiv="Yes")
shielbert3=Sirfetchd (maxiv="Yes")
shielbert4=Klinklang(maxiv="Yes")
shielbert5=Aegislash(maxiv="Yes")
shielbert6=Zamazenta(maxiv="Yes")
shielbertteam=teamset([shielbert2,shielbert3,shielbert4,shielbert5,shielbert1],5)+[shielbert6]
shielbert=Trainer ("Pokémon Trainer Shielbert",shielbertteam,"Galar")
#gladion
gladion1=Zoroark(maxiv="Yes")
gladion2=Crobat(maxiv="Yes")
gladion3=Weavile(maxiv="Yes")
gladion4=MNLycanroc(name="Midnight Lycanroc(Z-Crystal)",maxiv="Yes",item=random.choice(["Lycanium Z","Rockium Z","Dragonium Z"]),move=["Stone Edge","Swords Dance","Outrage","Crunch"])
gladion5=MLucario(maxiv="Yes")
gladion6=Silvally(maxiv="Yes")
gladion7=Venusaur(maxiv="gmax")
gladion8=Charizard(maxiv="gmax")
gladion9=Blastoise(maxiv="gmax")
gladion10=Nihilego(name="Lille✨",maxiv="Yes")
gladionteam=teamset([gladion2,gladion3,gladion4,gladion5,gladion1,gladion10],4)+teamset([gladion7,gladion8,gladion9],1)+[gladion6]
gladion=Trainer ("Pokémon Trainer Gladion",gladionteam,"Alola")
#morimoto
morimoto1=Spiritomb(maxiv="Yes")
morimoto2=Ambipom(maxiv="Yes")
morimoto3=Hippowdon(maxiv="Yes")
morimoto4=Jolteon(maxiv="Yes")
morimoto5=Vaporeon(maxiv="Yes")
morimoto6=Flareon(maxiv="Yes")
morimoto7=Cursola(maxiv="Yes")
morimoto8=Grapplot(maxiv="Yes")
morimoto9=Dragapult(maxiv="Yes")
morimoto10=Coalossal(maxiv="Yes")
morimoto11=Snorlax(maxiv="Yes")
morimoto12=Stonjourner (maxiv="Yes")
morimoto13=Kangaskhan(maxiv="Yes")
morimoto14=Machamp(maxiv="Yes")
morimoto15=Dragonite (maxiv="Yes")
morimoto16=Kecleon(maxiv="Yes")
morimoto17=Gengar(maxiv="Yes")
morimoto18=Blissey (maxiv="Yes")
morimoto19=Zebstrika(maxiv="Yes")
morimoto20=Swoobat(maxiv="Yes")
morimoto21=Liepard(maxiv="Yes")
morimoto22=Simipour(maxiv="Yes")
morimoto23=Simisage(maxiv="Yes")
morimoto24=Simisear (maxiv="Yes")
morimototeam=teamset([morimoto2,morimoto3,morimoto4,morimoto5,morimoto1,morimoto10,morimoto7,morimoto8,morimoto9,morimoto6,morimoto11,morimoto12,morimoto13,morimoto14,morimoto15,morimoto16,morimoto17,morimoto18,morimoto19,morimoto20,morimoto21,morimoto22,morimoto23,morimoto24],6)
morimoto=Trainer ("GAME FREAK's Morimoto",morimototeam,"Alola")
#dawn
dawn1=Lopunny(maxiv="Yes")
dawn2=Typhlosion (maxiv="Yes",item="Choice Scarf")
dawn3=Pachirisu(maxiv="Yes")
dawn4=Mamoswine (maxiv="Yes",item="Life Orb")
dawn5=Togekiss(maxiv="Yes",item="Lum Berry", ability="Serene Grace")
dawn6=Ambipom(maxiv="Yes")
dawn7=Floatzel(maxiv="Yes")
dawn8=Clefable(maxiv="Yes")
dawn9=Empoleon(maxiv="Yes")
dawn10=Alakazam(maxiv="Yes")
dawn11=Wormadam(maxiv="Yes")
dawn12=Magmortar (maxiv="Yes")
dawn13=Milotic(maxiv="Yes")
dawn14=Froslass(maxiv="Yes")
dawn15=Tangrowth (maxiv="Yes")
dawn16=Bellossom (maxiv="Yes")
dawn17=Blastoise(maxiv="Yes")
dawn18=Sceptile(maxiv="Yes")
dawn19=Crobat(maxiv="Yes")
dawn20=Gorebyss(maxiv="Yes")
dawn21=Lickilicky(maxiv="Yes")
dawn22=MrMime(maxiv="Yes")
dawn23=Arcanine(maxiv="Yes")
dawn24=Honchkrow(maxiv="Yes")
dawnteam=teamset([dawn2,dawn3,dawn4,dawn5,dawn1,dawn6,dawn7,dawn8,dawn10,dawn11,dawn12,dawn13,dawn14,dawn15,dawn16,dawn17,dawn18,dawn19,dawn20,dawn21,dawn22,dawn23,dawn24],5)+[dawn9]
dawn=Trainer ("Coordinator Dawn",dawnteam,"Sinnoh")
#lucas
lucas1=Mothim(maxiv="Yes",item="Focus Sash")
lucas2=Magmortar(maxiv="Yes",item="Expert Belt")
lucas3=Gallade(maxiv="Yes",item="Life Orb")
lucas4=Torterra(maxiv="Yes",item="Life Orb")
lucas5=Infernape(maxiv="Yes")
lucas6=Gliscor(maxiv="Yes")
lucas7=Cradily(maxiv="Yes")
lucas8=Clefable(maxiv="Yes",item="Sitrus Berry")
lucas9=Empoleon(maxiv="Yes")
lucas10=Glaceon(maxiv="Yes")
lucas11=Tauros(maxiv="Yes")
lucas12=HRotom(maxiv="Yes")
lucas13=Milotic(maxiv="Yes",item="Flame Orb")
lucas14=Dusknoir(maxiv="Yes")
lucas15=Tangrowth (maxiv="Yes",item="Lum Berry")
lucas16=Flareon(maxiv="Yes")
lucas17=WRotom(maxiv="Yes")
lucas18=Dudunsparce(maxiv="Yes")
lucas19=Rampardos(maxiv="Yes")
lucas20=Absol(maxiv="Yes")
lucas21=Kabutops(maxiv="Yes")
lucas22=MRotom(maxiv="Yes")
lucas23=Espeon(maxiv="Yes")
lucas24=PorygonZ(maxiv="Yes")
lucas25=Rhyperior(maxiv="Yes")
lucasteam=teamset([lucas2,lucas3,lucas1,lucas6,lucas7,lucas8,lucas10,lucas11,lucas12,lucas13,lucas14,lucas15,lucas16,lucas17,lucas18,lucas19,lucas20,lucas21,lucas22,lucas23,lucas24,lucas25],5)+teamset([lucas9,lucas4,lucas5],1)
lucas=Trainer ("Pokémon Trainer Lucas",lucasteam,"Sinnoh")
#bronius
bronius1=Liepard(maxiv="Yes")
bronius2=Mandibuzz(maxiv="Yes")
bronius3=Salamence(maxiv="Yes")
bronius4=Bisharp(maxiv="Yes")
bronius5=MSableye(maxiv="Yes")
bronius6=Amoongus(maxiv="gmax")
broniusteam=teamset([bronius2,bronius3,bronius4,bronius5,bronius1],5)+[bronius6]
bronius=Trainer ("Plasma Sage Bronius",broniusteam,"Unova")
#ryoku
ryoku1=Garbodor(maxiv="Yes")
ryoku2=Absol(maxiv="Yes")
ryoku3=Flygon(maxiv="Yes")
ryoku4=Bisharp(maxiv="Yes")
ryoku5=MPinsir(maxiv="Yes")
ryoku6=Scolipede(maxiv="gmax")
ryokuteam=teamset([ryoku2,ryoku3,ryoku4,ryoku5,ryoku1],5)+[ryoku6]
ryoku=Trainer ("Plasma Sage Ryoku",ryokuteam,"Unova")
#rood
rood1=Swoobat(maxiv="Yes")
rood2=Stoutland(maxiv="Yes")
rood3=Zoroark(maxiv="Yes")
rood4=Granbull(maxiv="Yes")
rood5=MHoundoom(maxiv="Yes")
rood6=Chandelure(maxiv="gmax")
roodteam=teamset([rood2,rood3,rood4,rood5,rood1],5)+[rood6]
rood=Trainer ("Plasma Sage Rood",roodteam,"Unova")
#zinzolin
zinzolin1=MAbomasnow(maxiv="Yes")
zinzolin2=Vanilluxe(maxiv="Yes")
zinzolin3=Beartic(maxiv="Yes")
zinzolin4=Weavile(maxiv="Yes")
zinzolin5=Kyurem(maxiv="Yes")
zinzolin6=Cryogonal(maxiv="gmax")
zinzolinteam=teamset([zinzolin2,zinzolin3,zinzolin4,zinzolin5,zinzolin1],5)+[zinzolin6]
zinzolin=Trainer ("Plasma Sage Zinzolin",zinzolinteam,"Unova")
#colress
colress1=Magnezone(maxiv="Yes")
colress2=Beheeyem(maxiv="Yes")
colress3=WRotom(maxiv="Yes")
colress4=PorygonZ(maxiv="Yes")
colress5=MMetagross(maxiv="Yes")
colress6=Klinklang(maxiv="gmax")
colress7=Muk(maxiv="Yes")
colress8=Electrode(maxiv="Yes")
colressteam=teamset([colress2,colress3,colress4,colress5,colress1,colress7,colress8],5)+[colress6]
colress=Trainer ("Team Plasma Colress",colressteam,"Unova")
#argenta
argenta1=Azelf(maxiv="Yes")
argenta2=Mesprit(maxiv="Yes")
argenta3=Uxie(maxiv="Yes")
argenta4=Regirock(maxiv="Yes")
argenta5=Regice(maxiv="Yes")
argenta6=Registeel(maxiv="Yes")
argenta7=Raikou(maxiv="Yes")
argenta8=Entei(maxiv="Yes")
argenta9=Suicune(maxiv="Yes")
argenta10=Latios(maxiv="Yes")
argenta11=Latias(maxiv="Yes")
argenta12=Articuno(maxiv="Yes")
argenta13=Zapdos(maxiv="Yes")
argenta14=Moltres(maxiv="Yes")
argenta15=Heatran(maxiv="Yes")
argenta16=Regigigas(maxiv="Yes")
argenta17=Drifblim(maxiv="Yes")
argentateam=teamset([argenta2,argenta3,argenta4,argenta5,argenta1,argenta7,argenta8,argenta6,argenta9,argenta10,argenta11,argenta12,argenta13,argenta14,argenta15,argenta16],5)+[argenta17]
argenta=Trainer ("Hall Matron Argenta",argentateam,"Sinnoh")
#matt
matt1=Mightyena(maxiv="Yes")
matt2=Muk(maxiv="Yes")
matt3=Crobat(maxiv="Yes")
matt4=Azumarill (maxiv="Yes")
matt5=Flygon(maxiv="Yes")
matt6=MSharpedo (maxiv="Yes")
matt=Trainer("Aqua Admin Matt",[matt1,matt2,matt3,matt4,matt5,matt6],"Hoenn")
#shelly
shelly1=Mightyena(maxiv="Yes")
shelly2=Muk (maxiv="Yes")
shelly3=Crobat(maxiv="Yes")
shelly4=Crawdaunt(maxiv="Yes")
shelly5=Sharpedo(maxiv="gmax")
shelly6=Walrein(maxiv="Yes")
shelly=Trainer("Aqua Admin Shelly",[shelly1,shelly2,shelly3,shelly4,shelly5,shelly6],"Hoenn")
#eusine
eusine1=Pikachu(maxiv="Yes")
eusine2=Jumpluff(maxiv="Yes")
eusine3=Hypno(maxiv="Yes")
eusine4=MAlakazam(maxiv="Yes")
eusine5=Gengar(maxiv="gmax")
eusine6=Electrode(maxiv="Yes")
eusine=Trainer("Pokémon Trainer Eusine",[eusine1,eusine2,eusine3,eusine4,eusine5,eusine6],"Johto")
#evelyn
evelyn1=Pachirisu(maxiv="Yes")
evelyn2=Primeape(maxiv="Yes")
evelyn3=Raikou(maxiv="Yes")
evelyn4=Suicune(maxiv="Yes")
evelyn5=Entei(maxiv="Yes")
evelyn6=MLatios(maxiv="Yes")
evelyn7=Persian(maxiv="Yes")
evelyn8=Lumineon(maxiv="Yes")
evelynteam=teamset([evelyn7,evelyn8,evelyn1,evelyn2,evelyn3,evelyn4,evelyn5,evelyn6],6)
evelyn=Trainer("Battle Chatelaine Evelyn",evelynteam,"Hoenn")
#courtney
courtney1=Mightyena(maxiv="Yes")
courtney2=Weezing(maxiv="Yes")
courtney3=Crobat(maxiv="Yes")
courtney4=Torkoal(maxiv="Yes", ability="Drought")
courtney5=MCamerupt(maxiv="Yes")
courtney6=Swellow(maxiv="Yes")
courtney7=Ninetales (maxiv="Yes", ability="Drought")
courtneyteam=teamset([courtney1,courtney2,courtney3,courtney4,courtney6,courtney7],5)+[courtney5]
courtney=Trainer("Magma Admin Courtney", courtneyteam,"Hoenn")
#butler
butler1=Dusclops(maxiv="Yes")
butler2=Gardevoir(maxiv="Yes")
butler3=Mightyena(maxiv="Yes")
butler4=MSalamence(maxiv="Yes")
butler5=Jirachi(maxiv="gmax")
butler6=Groudon(name="Meta Groudon",maxiv="Yes")
butler=Trainer("Team Magma Butler",[butler1,butler2,butler3,butler4,butler5,butler6],"Hoenn")
#LEGENDARY TRIALS
#Articuno
bossarticuno=Articuno(name="Legendary Articuno",maxiv="Yes",hpev=252,atkev=252,defev=252,spatkev=252,speedev=252,item="Silver Feather",move=["Blizzard","Hurricane","Ice Beam","Extrasensory"])
carticuno=Trainer("Trial Legend Crescent",[bossarticuno])
#Zapdos
bosszapdos=Zapdos(name="Legendary Zapdos",maxiv="Yes",hpev=252,atkev=252,defev=252,spatkev=252,speedev=252,item="Silver Feather",move=["Thunder","Hurricane","Thunderbolt","Drill Peck"])
czapdos=Trainer("Trial Legend Crescent",[bosszapdos])
#Moltres
bossmoltres=Moltres(name="Legendary Moltres",maxiv="Yes",hpev=252,atkev=252,defev=252,spatkev=252,speedev=252,item="Silver Feather",move=["Fire Blast","Sky Attack","Flamethrower","Heat Wave"])
cmoltres=Trainer("Trial Legend Crescent",[bossmoltres])
#gmoltres
bossgmoltres=GMoltres(name="Legendary Galarian Moltres",maxiv="Yes",hpev=252,atkev=252,defev=252,spatkev=252,speedev=252,item="Silver Feather",move=["Dark Pulse","Sky Attack","Flamethrower","Fiery Wrath"])
cgmoltres=Trainer("Trial Legend Crescent",[bossgmoltres])
#GArticuno
bossgarticuno=GArticuno(name="Legendary Galarian Articuno",maxiv="Yes",hpev=252,atkev=252,defev=252,spatkev=252,speedev=252,item="Silver Feather",move=["Ice Beam","Hurricane","Freezing Glare","Extrasensory"])
cgarticuno=Trainer("Trial Legend Crescent",[bossgarticuno])
#Mewtwo
bossmewtwo=Mewtwo(name="Legendary Mewtwo",maxiv="Yes",hpev=252,atkev=252,defev=252,spatkev=252,speedev=252,item="Team Rocket Armor",move=["Psystrike","Shadow Ball","Aura Sphere","Psychic"])
cmewtwo=Trainer("Trial Legend Crescent",[bossmewtwo])
#adaman
adaman1=Flareon(maxiv="Yes")
adaman2=Jolteon(maxiv="Yes")
adaman3=Glaceon(maxiv="Yes")
adaman4=Vaporeon(maxiv="Yes")
adaman5=Leafeon(maxiv="Yes")
adaman6=Umbreon(maxiv="Yes")
adaman=Trainer("Clan Leader Adaman",[adaman1,adaman2,adaman3,adaman4,adaman5,adaman6],"Hisui")
#celosia
celosia1=Absol(maxiv="Yes")
celosia2=Zoroark(maxiv="Yes")
celosia3=Aegislash(maxiv="Yes")
celosia4=Liepard(maxiv="Yes")
celosia5=Drapion(maxiv="Yes")
celosia6=MManectric(maxiv="Yes")
celosiateam=teamset([celosia2,celosia3,celosia4,celosia5,celosia1],5)+[celosia6]
celosia=Trainer ("Team Flare Celosia",celosiateam,"Kalos")
#bryony
bryony1=Mandibuzz(maxiv="Yes")
bryony2=Krookodile(maxiv="Yes")
bryony3=Scrafty(maxiv="Yes")
bryony4=Liepard(maxiv="Yes")
bryony5=Malamar(maxiv="Yes")
bryony6=Kingambit(maxiv="Yes")
bryonyteam=teamset([bryony2,bryony3,bryony4,bryony5,bryony1],5)+[bryony6]
bryony=Trainer ("Team Flare Bryony",bryonyteam,"Kalos")
#aliana
aliana1=Diggersby(maxiv="Yes")
aliana2=Gourgeist(maxiv="Yes")
aliana3=Pyroar(maxiv="Yes")
aliana4=Liepard(maxiv="Yes")
aliana5=Mightyena(maxiv="Yes")
aliana6=Druddigon(maxiv="Yes")
alianateam=teamset([aliana2,aliana3,aliana4,aliana5,aliana1],5)+[aliana6]
aliana=Trainer ("Team Flare Aliana",alianateam,"Kalos")
#xerosic
xerosic1=MMawile(maxiv="Yes")
xerosic2=Whimsicott(maxiv="Yes")
xerosic3=Jellicent(maxiv="Yes")
xerosic4=Volcarona(maxiv="Yes")
xerosic5=Crobat(maxiv="Yes")
xerosic6=Malamar(maxiv="Yes")
xerosic7=Granbull(maxiv="Yes")
xerosic8=Persian(maxiv="Yes")
xerosicteam=teamset([xerosic2,xerosic3,xerosic4,xerosic5,xerosic1,xerosic7,xerosic8],5)+[xerosic6]
xerosic=Trainer ("Team Flare Xerosic",xerosicteam,"Kalos")
#heatran
bossheatran=Heatran(name="Legendary Heatran",maxiv="Yes",hpev=252,atkev=252,defev=252,spatkev=252,speedev=252,item="Magma Stone",move=["Magma Storm","Flash Cannon","Earth Power","Fire Blast"])
cheatran=Trainer("Trial Legend Crescent",[bossheatran])
#kyogre
bosskyogre=PKyogre(name="Legendary Kyogre",maxiv="Yes",hpev=252,atkev=252,defev=252,spatkev=252,speedev=252,item="Navy Orb",move=["Origin Pulse","Water Spout","Thunder","Ice Beam"])
ckyogre=Trainer("Trial Legend Crescent",[bosskyogre])
#groudon
bossgroudon=PGroudon(name="Legendary Groudon",maxiv="Yes",hpev=252,atkev=252,defev=252,spatkev=252,speedev=252,item="Crimson Orb",move=["Precipice Blades","Eruption","Earthquake","Solar Beam"])
cgroudon=Trainer("Trial Legend Crescent",[bossgroudon])
#raikou
bossraikou=Raikou(name="Legendary Raikou",maxiv="Yes",hpev=252,atkev=252,defev=252,spatkev=252,speedev=252,item="Rainbow Feather",move=["Thunder Fang","Crunch","Extreme Speed","Wild Charge"])
bossentei=Entei(name="Legendary Entei",maxiv="Yes",hpev=252,atkev=252,defev=252,spatkev=252,speedev=252,item="Rainbow Feather",move=["Flare Blitz","Crunch","Extreme Speed","Sacred Fire"])
bosssuicune=Suicune(name="Legendary Suicune",maxiv="Yes",hpev=252,atkev=252,defev=252,spatkev=252,speedev=252,item="Rainbow Feather",move=["Hydro Pump","Scald","Extreme Speed","Ice Beam"])
cbeast=Trainer("Trial Legend Crescent",[bosssuicune,bossraikou,bossentei])
#giacomo
giacomo1=Cacturne(maxiv="Yes")
giacomo2=Honchkrow(maxiv="Yes")
giacomo3=Mabosstiff(maxiv="Yes")
giacomo4=Krookodile(maxiv="Yes")
giacomo5=Kingambit(maxiv="Yes")
giacomo6=Revavroom(name="Segin Starmobile",type1="Dark",type2=None,maxiv="Yes",move=["Wicked Torque","Spin Out","Poison Jab","Gunk Shot"])
giacomo=Trainer("Team Star Giacomo",[giacomo1,giacomo2,giacomo3,giacomo4,giacomo5,giacomo6],"Paldea")
#mela
mela1=Torkoal(maxiv="Yes")
mela2=Coalossal(maxiv="Yes")
mela3=Arcanine(maxiv="Yes")
mela4=Armarouge(maxiv="Yes")
mela5=MHoundoom(maxiv="Yes")
mela6=Revavroom(name="Schedar Starmobile",type1="Fire",type2=None,maxiv="Yes",move=["Blazing Torque","Spin Out","Poison Jab","Gunk Shot"])
mela=Trainer("Team Star Mela",[mela1,mela2,mela3,mela4,mela5,mela6],"Paldea")
#atticus
atticus1=Skuntank(maxiv="Yes")
atticus2=Muk(maxiv="Yes")
atticus3=Dragalge(maxiv="Yes")
atticus4=Toxapex(maxiv="Yes")
atticus5=Grafaiai(maxiv="Yes")
atticus6=Revavroom(name="Navi Starmobile",type1="Poison",type2=None,maxiv="Yes",move=["Noxious Torque","Spin Out","Poison Jab","Gunk Shot"])
atticus=Trainer("Team Star Atticus",[atticus1,atticus2,atticus3,atticus4,atticus5,atticus6],"Hoenn")
#ortega
ortega1=Azumarill(maxiv="Yes")
ortega2=Wigglytuff(maxiv="Yes")
ortega3=Dachsbun(maxiv="Yes")
ortega4=Klefki(maxiv="Yes")
ortega5=Hatterene(maxiv="Yes")
ortega6=Revavroom(name="Ruchbah Starmobile",type1="Fairy",type2=None,maxiv="Yes",move=["Magical Torque","Spin Out","Poison Jab","Gunk Shot"])
ortega=Trainer("Team Star Ortega",[ortega1,ortega2,ortega3,ortega4,ortega5,ortega6],"Paldea")
#eri
eri1=Toxicroak(maxiv="Yes")
eri2=Passimian(maxiv="Yes")
eri3=Primeape(maxiv="Yes")
eri4=Anihilape(maxiv="Yes")
eri5=MLucario(maxiv="Yes")
eri6=Revavroom(name="Caph Starmobile",type1="Fighting",type2=None,maxiv="Yes",move=["Combat Torque","Spin Out","Poison Jab","Gunk Shot"])
eri=Trainer("Team Star Eri",[eri1,eri2,eri3,eri4,eri5,eri6],"Paldea")
#penny
penny1=Umbreon(maxiv="Yes")
penny2=Leafeon(maxiv="Yes")
penny3=Flareon(maxiv="Yes")
penny4=Jolteon(maxiv="Yes")
penny5=Vaporeon(maxiv="Yes")
penny6=Sylveon(name="Sylveon💎",maxiv="Fairy")
penny=Trainer("Star Leader Penny",[penny1,penny2,penny3,penny4,penny5,penny6],"Paldea")
#mai
mai1=Snorlax(maxiv="Yes")
mai2=Weavile(maxiv="Yes")
mai3=Crobat(maxiv="Yes")
mai4=Ambipom(maxiv="Yes")
mai5=Floatzel(maxiv="Yes")
mai6=Wyrdeer(maxiv="Yes")
maiteam=teamset([mai1,mai2,mai3,mai4,mai5],5)+[mai6]
mai=Trainer("Warden Mai",maiteam,"Hisui")
#lian
lian1=Mamoswine(maxiv="Yes")
lian2=HGoodra(maxiv="Yes")
lian3=Whiscash(maxiv="Yes")
lian4=Hippowdon(maxiv="Yes")
lian5=Rhyperior(maxiv="Yes")
lian6=Kleavor(maxiv="Yes")
lianteam=teamset([lian1,lian2,lian3,lian4,lian5],5)+[lian6]
lian=Trainer("Warden Lian",lianteam,"Hisui")
#calaba
calaba1=Bibarel(maxiv="Yes")
calaba2=Lickilicky(maxiv="Yes")
calaba3=Snorlax(maxiv="Yes")
calaba4=MLopunny(maxiv="Yes")
calaba5=Purugly(maxiv="Yes")
calaba6=Ursaluna(maxiv="Yes")
calabateam=teamset([calaba1,calaba2,calaba3,calaba4,calaba5],5)+[calaba6]
calaba=Trainer("Warden Calaba",calabateam,"Hisui")
#iscan
iscan1=EGastrodon(maxiv="Yes")
iscan2=Empoleon(maxiv="Yes")
iscan3=Lumineon(maxiv="Yes")
iscan4=Sharpedo(maxiv="Yes")
iscan5=Floatzel(maxiv="Yes")
iscan6=Basculegion(maxiv="Yes")
iscanteam=teamset([iscan1,iscan2,iscan3,iscan4,iscan5],5)+[iscan6]
iscan=Trainer("Warden Iscan",iscanteam,"Hisui")
#palina
palina1=Torkoal(maxiv="Yes")
palina2=Infernape(maxiv="Yes")
palina3=Magmortar(maxiv="Yes")
palina4=Rapidash(maxiv="Yes")
palina5=Camerupt(maxiv="Yes")
palina6=HArcanine(maxiv="Yes")
palinateam=teamset([palina1,palina2,palina3,palina4,palina5],5)+[palina6]
palina=Trainer("Warden Palina",palinateam,"Hisui")
#peony
peony1=Bronzong(maxiv="Yes")
peony2=Perrserker(maxiv="Yes")
peony3=Escavalier (maxiv="Yes")
peony4=Aggron(maxiv="Yes")
peony5=Scizor(maxiv="Yes")
peony6=Copperajah(maxiv="gmax")
peonyteam=teamset([peony1,peony2,peony3,peony4,peony5],5)+[peony6]
peony=Trainer ("Champion Peony",peonyteam,"Alola")
#klara
klara1=Amoongus(maxiv="Yes")
klara2=Drapion(maxiv="Yes")
klara3=Scolipede (maxiv="Yes")
klara4=GWeezing(maxiv="Yes")
klara5=GSlowking (maxiv="Yes")
klara6=GSlowbro(maxiv="Yes")
klarateam=teamset([klara2,klara3,klara4,klara5,klara1],5)+[klara6]
klara=Trainer ("Gym Leader Klara",klarateam,"Galar")
#avery
avery1=Indeedee(maxiv="Yes")
avery2=GSlowking(maxiv="Yes")
avery3=Swoobat(maxiv="Yes")
avery4=Alakazam(maxiv="Yes")
avery5=GRapidash(maxiv="Yes")
avery6=GSlowbro(maxiv="Yes")
averyteam=teamset([avery2,avery3,avery4,avery5,avery1],5)+[avery6]
avery=Trainer ("Gym Leader Avery",averyteam,"Galar")
#arven
arven1=Greedent(maxiv="Yes")
arven2=Cloyster(maxiv="Yes")
arven3=Scovillain(maxiv="Yes")
arven4=Toedscruel(maxiv="Yes")
arven5=Garganacl(maxiv="Yes")
arven6=Mabosstiff(name="Mabosstiff💎",maxiv="Dark")
arventeam=teamset([arven2,arven3,arven4,arven5,arven1],5)+[arven6]
arven=Trainer ("Pokémon Trainer Arven",arventeam,"Paldea")
#jessie
jessie1=Wobbuffet(maxiv="Yes")
jessie2=Seviper(maxiv="Yes")
jessie3=Yanmega(maxiv="Yes")
jessie4=Dustox(maxiv="Yes")
jessie5=Arbok(maxiv="Yes")
jessie6=Mimikyu(maxiv="Yes")
jessie7=Gourgeist(maxiv="Yes")
jessie8=Blissey(maxiv="Yes")
jessie9=Meowth(maxiv="gmax")
jessieteam=teamset([jessie2,jessie3,jessie4,jessie5,jessie1,jessie6,jessie7,jessie8],5)+[jessie9]
jessie=Trainer ("Team Rocket Jessie",jessieteam,"Kanto")
#clavell
clavell1=Oranguru(maxiv="Yes")
clavell2=Abomasnow(maxiv="Yes")
clavell3=Polteageist(maxiv="Yes")
clavell4=Gyarados(maxiv="Yes")
clavell5=Houndoom(maxiv="Yes")
clavell6=Quaquaval(name="Quaquaval💎",maxiv=random.choice(["Water","Fighting"]))
clavell7=Amoongus(maxiv="Yes")
clavell8=Meowscarada(name="Meowscarada💎",maxiv=random.choice(["Grass","Dark"]))
clavell9=Skeledirge(name="Skeledirge💎",maxiv=random.choice(["Fire","Ghost"]))
clavellteam=teamset([clavell2,clavell3,clavell4,clavell5,clavell1,clavell7],5)+teamset([clavell6, clavell9, clavell8],1)
clavell=Trainer ("Director Clavell Mesagoza",clavellteam,"Paldea")
#zoey
zoey1=Glameow(maxiv="gmax")
zoey2=Lumineon(maxiv="Yes")
zoey3=WGastrodon(maxiv="Yes")
zoey4=Leafeon(maxiv="Yes")
zoey5=Mismagius(name="Mismagius💎",maxiv="Fairy")
zoey6=MGallade(maxiv="Yes")
zoey=Trainer("Coordinator Zoey",[zoey1,zoey2,zoey3,zoey4,zoey5,zoey6],"Sinnoh")
#conway
conway1=Slowking(maxiv="Yes")
conway2=Heracross (maxiv="Yes")
conway3=MAggron(maxiv="Yes")
conway4=Shuckle(maxiv="Yes")
conway5=Lickilicky(maxiv="Yes")
conway6=Dusknoir(maxiv="gmax")
conway=Trainer("Pokémon Trainer Conway",[conway1,conway2,conway3,conway4,conway5,conway6],"Sinnoh")
#james
james1=Weezing(maxiv="Yes")
james2=Victreebel(maxiv="Yes")
james3=Chimecho(maxiv="Yes")
james4=Arcanine(maxiv="Yes")
james5=Toxapex(maxiv="Yes")
james6=Malamar(maxiv="Yes")
james7=Gyarados(maxiv="Yes")
james8=Amoongus(maxiv="Yes")
james9=Meowth(maxiv="gmax")
jamesteam=teamset([james2,james3,james4,james5,james1,james6,james7,james8],5)+[james9]
james=Trainer ("Team Rocket James",jamesteam,"Kanto")
jessiejamesteam=teamset([james2,james3,james4,james5,james1,james6,james7,james8,jessie2,jessie3,jessie4,jessie5,jessie1,jessie6,jessie7,jessie8],5)+[james9]
jessiejames=Trainer ("Team Rocket Jessie & James",jessiejamesteam,"Kanto")
#nando
nando1=Roserade(maxiv="Yes")
nando2=Sunflora(maxiv="Yes")
nando3=Altaria(maxiv="Yes")
nando4=MLopunny(maxiv="Yes")
nando5=Kricketune(name="Kricketune 💎",maxiv="Steel")
nando6=Armaldo(maxiv="gmax")
nando=Trainer("Pokémon Trainer Nando",[nando1,nando2,nando3,nando4,nando5,nando6],"Sinnoh")
#drew
drew1=Swampert(maxiv="Yes")
drew2=Butterfree(maxiv="gmax")
drew3=Roserade(maxiv="Yes")
drew4=Masquerain(maxiv="Yes")
drew5=MAbsol(maxiv="Yes")
drew6=Flygon(name="Flygon💎",maxiv="Bug")
drew=Trainer("Pokémon Trainer Drew",[drew1,drew2,drew3,drew4,drew5,drew6],"Hoenn")
#trip
trip1=Unfezant(maxiv="Yes")
trip2=Vanilluxe (maxiv="Yes")
trip3=Chandelure(maxiv="Yes")
trip4=Jellicent(maxiv="Yes")
trip5=Conkeldurr(maxiv="Yes")
trip6=Serperior(maxiv="gmax")
trip=Trainer("Pokémon Trainer Trip",[trip1,trip2,trip3,trip4,trip5,trip6],"Unova")
#ursula
ursula1=Wigglytuff(maxiv="Yes")
ursula2=Minun(maxiv="Yes")
ursula3=Plusle(maxiv="Yes")
ursula4=Vaporeon(maxiv="Yes")
ursula5=Flareon(maxiv="Yes")
ursula6=Garchomp (name="Garchomp",maxiv="Ground")
ursula=Trainer("Coordinator Ursula",[ursula1,ursula2,ursula3,ursula4,ursula5,ursula6],"Sinnoh")
#kenny
kenny1=Scizor(maxiv="Yes")
kenny2=Floatzel(name="Floatzel💎",maxiv="Ice")
kenny3=Machamp(maxiv="Yes")
kenny4=Breloom(maxiv="Yes")
kenny5=MAlakazam(maxiv="Yes")
kenny6=Empoleon(maxiv="gmax")
kenny=Trainer("Coordinator Kenny",[kenny1,kenny2,kenny3,kenny4,kenny5,kenny6],"Sinnoh")
#ritchie
ritchie1=Tentacruel(maxiv="Yes")
ritchie2=Swellow(name="Rose",maxiv="Yes")
ritchie3=Tyranitar(name="Cruise💎",maxiv="Rock")
ritchie4=Butterfree(name="Happy",maxiv="Yes")
ritchie5=MCharizardY(name="Zippo",maxiv="Yes")
ritchie6=Pikachu(name="Sparky",maxiv="Yes")
ritchie=Trainer("Pokémon Trainer Ritchie",[ritchie1,ritchie2,ritchie3,ritchie4,ritchie5,ritchie6],"Kanto")
#hugh
hugh3=Eelektross (maxiv="Yes")
hugh4=Flygon (maxiv="Yes")
hugh5=Bouffalant (maxiv="Yes")
hugh6=Liepard(maxiv="Yes")
hugh7=Unfezant(maxiv="Yes")
hugh8=Samurott (maxiv="Yes")
hugh9=Emboar(maxiv="Yes")
hugh10=Serperior(maxiv="Yes")
hugh11=Simisage(maxiv="Yes")
hugh12=Simipour(maxiv="Yes")
hugh13=Simisear(maxiv="Yes")
hughteam=teamset([hugh3,hugh4,hugh5,hugh7,hugh6],4)+teamset([hugh11,hugh12,hugh13],1)+teamset([hugh8,hugh9,hugh10],1)
hugh=Trainer("Pokémon Trainer Hugh",hughteam,"Unova")
#harrison
harrison1=Kecleon(maxiv="Yes")
harrison2=Hypno(maxiv="Yes")
harrison3=Miltank(maxiv="Yes")
harrison4=Steelix(maxiv="Yes")
harrison5=Houndoom(name="Houndoom💎",maxiv="Dark")
harrison6=MBlaziken(maxiv="Yes")
harrison=Trainer("Pokémon Trainer Harrison",[harrison1,harrison2,harrison3,harrison4,harrison5,harrison6],"Hoenn")
#harley
harley1=Sceptile(maxiv="Yes")
harley2=Ariados(maxiv="Yes")
harley3=Octillery(maxiv="Yes")
harley4=Wigglytuff (maxiv="Yes")
harley5=Banette(maxiv="Yes")
harley6=Cacturne(maxiv="gmax")
harley=Trainer("Coordinator Harley",[harley1,harley2,harley3,harley4,harley5,harley6],"Hoenn")
#tyson
tyson1=Shiftry (maxiv="Yes")
tyson2=Hariyama (maxiv="Yes")
tyson3=Donphan(maxiv="Yes")
tyson4=Sceptile (name="Sceptile💎",maxiv="Grass")
tyson5=Metagross (maxiv="Yes")
tyson6=Meowth (maxiv="gmax")
tyson=Trainer("Pokémon Trainer Tyson",[tyson1,tyson2,tyson3,tyson4,tyson5,tyson6],"Hoenn")
#solidad
solidad1=Blissey (maxiv="Yes")
solidad2=Snorlax(maxiv="Yes")
solidad3=Butterfree(maxiv="Yes")
solidad4=Pidgeot (name="Pidgeot💎",maxiv="Normal")
solidad5=Lapras (maxiv="gmax")
solidad6=MSlowbro (maxiv="Yes")
solidad=Trainer("Coordinator Solidad",[solidad1,solidad2,solidad3,solidad4,solidad5,solidad6],"Kanto")
#dino
dino1=Seismitoad(maxiv="Yes")
dino2=Leavanny (maxiv="Yes")
dino3=Chandelure(maxiv="Yes")
dino4=Gigalith(maxiv="gmax")
dino5=Darmanitan (maxiv="Yes")
dino6=Druddigon(name="Druddigon💎",maxiv="Dragon")
dino7=Heatmor(maxiv="Yes")
dino8=Mandibuzz(maxiv="Yes")
dino9=Cofagrigus(maxiv="Yes")
dino10=Galvantula (maxiv="Yes")
dino11=Sawsbuck (maxiv="Yes")
dino12=Unfezant (maxiv="Yes")
dinoteam=teamset([dino1,dino2,dino3,dino4,dino5,dino7,dino8,dino9,dino10,dino11,dino12],5)+[dino6]
dino=Trainer("Pokémon Trainer Dino",dinoteam,"Unova")
#burgundy
burgundy1=Reuniclus(maxiv="Yes")
burgundy2=Scolipede (maxiv="Yes")
burgundy3=Darmanitan(maxiv="Yes")
burgundy4=Stoutland (maxiv="Yes")
burgundy5=Sawsbuck(maxiv="Yes")
burgundy6=Samurott(name="Samurott💎",maxiv="Water")
burgundy=Trainer("Connoisseuse Burgundy",[burgundy1,burgundy2,burgundy3,burgundy4,burgundy5,burgundy6],"Unova")
#virgil
virgil1=Glaceon(maxiv="Yes")
virgil2=Jolteon(maxiv="Yes")
virgil3=Flareon(maxiv="Yes")
virgil4=Vaporeon(maxiv="Yes")
virgil5=Espeon(maxiv="Yes")
virgil6=Umbreon(maxiv="Yes")
virgil7=Leafeon(maxiv="Yes")
virgil8=Klinklang(maxiv="Yes")
virgil9=Bouffalant(maxiv="Yes")
virgil10=Ampharos (maxiv="Yes")
virgil11=Zebstrika (maxiv="Yes")
virgil12=Sylveon(maxiv="Yes")
virgilteam=teamset([virgil1,virgil2,virgil3,virgil4,virgil5,virgil7,virgil8,virgil9,virgil10,virgil11,virgil12],5)+[virgil6]
virgil=Trainer("Pokémon Trainer Virgil",virgilteam,"Unova")
#cameron
cameron1=Watchog(maxiv="Yes")
cameron2=Swanna(maxiv="Yes")
cameron3=Lucario(maxiv="Yes")
cameron4=Ferrothorn (maxiv="Yes")
cameron5=Hydreigon(name="Hydreigon💎",maxiv="Dark")
cameron6=Samurott (maxiv="gmax")
cameronteam=teamset([cameron1,cameron2,cameron3,cameron4,cameron5],5)+[cameron6]
cameron=Trainer("Pokémon Trainer Cameron",cameronteam,"Unova")
#Ilima
Ilima1=Eevee(name="Eevee(Z-Crystal)",maxiv="Yes")
Ilima2=ARaticate (maxiv="Yes")
Ilima3=Gumshoos(maxiv="Yes")
Ilima4=Komala(maxiv="Yes")
Ilima5=Smeargle(maxiv="Yes")
Ilima6=MKangaskhan (maxiv="Yes")
Ilimateam=teamset([Ilima1,Ilima2,Ilima3,Ilima4,Ilima5],5)+[Ilima6]
Ilima=Trainer("Trial Captain Ilima",Ilimateam,"Alola")
#kiawe
kw=random.randint(1,3)
kw1,kw2,kw3=None,None,None
if kw==1:
    kw1,kw2,kw3="(Z-Crystal)","",""
if kw==2:
    kw2,kw1,kw3="(Z-Crystal)","",""   
if kw==3:
    kw1,kw2,kw3="","","(Z-Crystal)"   
kiawe1=Salazzle(maxiv="Yes")
kiawe2=Arcanine (maxiv="Yes")
kiawe3=Talonflame (maxiv="Yes")
kiawe4=AMarowak(name="Alolan Marowak"+kw3,maxiv="Yes")
kiawe5=Turtonator(name="Turtonator"+kw1,maxiv="Yes")
kiawe6=Charizard(name="Charizard"+kw2,maxiv="Yes")
kiawe7=MKangaskhan(maxiv="Yes")
kiaweteam=teamset([kiawe1,kiawe2,kiawe3,kiawe4,kiawe6,kiawe7],5)+[kiawe5]
kiawe=Trainer("Trial Captain Kiawe",kiaweteam,"Alola")
#lana
lana1=Vaporeon (maxiv="Yes")
lana2=Primarina (name="Primarina(Z-Crystal)",maxiv="Yes")
lana3=Lanturn (maxiv="Yes")
lana4=Cloyster(maxiv="Yes")
lana5=Araquanid(maxiv="Yes")
lana6=SWishiwashi(maxiv="Yes")
lana7=Lapras(maxiv="Yes")
lanateam=teamset([lana1,lana2,lana3,lana4,lana5,lana7],5)+[lana6]
lana=Trainer("Trial Captain Lana",lanateam,"Alola")
#saguaro
saguaro1=Pachirisu(maxiv="Yes")
saguaro2=Froslass(maxiv="Yes")
saguaro3=Amomola(maxiv="Yes")
saguaro4=Vespiquen(maxiv="Yes")
saguaro5=Goodra(maxiv="Yes")
saguaro6=Hatterene(maxiv="Yes")
saguaroteam=teamset([saguaro1,saguaro2,saguaro3,saguaro5,saguaro4],5)+[saguaro6]
saguaro=Trainer("Instructor Saguaro",saguaroteam,"Paldea")
#jacq
jacq1=Arcanine(maxiv="Yes")
jacq2=Lurantis(maxiv="Yes")
jacq3=Swalot(maxiv="Yes")
jacq4=Mudsdale(maxiv="Yes")
jacq5=Slowbro(maxiv="Yes")
jacq6=Farigiraf(maxiv="Yes")
jacqteam=teamset([jacq1,jacq2,jacq3,jacq5,jacq4],5)+[jacq6]
jacq=Trainer("Instructor Jacq",jacqteam,"Paldea")
#mallow
mallow1=Comfey(maxiv="Yes")
mallow2=Tsareena(name="Tsareena(Z-Crystal)",maxiv="Yes")
mallow3=Shiinotic(maxiv="Yes")
mallow4=Trevenant(maxiv="Yes")
mallow5=Lurantis(maxiv="Yes")
mallow6=SShaymin(maxiv="Yes")
mallow7=MSceptile(maxiv="Yes")
mallowteam=teamset([mallow1,mallow2,mallow3,mallow4,mallow5,mallow7],5)+[mallow6]
mallow=Trainer("Trial Captain Mallow",mallowteam,"Alola")
#ramone
ramone1=Lilligant (maxiv="Yes")
ramone2=Seismitoad (maxiv="Yes")
ramone3=Beartic(maxiv="Yes")
ramone4=Durant (maxiv="Yes")
ramone5=Stoutland(maxiv="Yes")
ramone6=Chandelure (maxiv="Yes")
ramone7=Unfezant (maxiv="Yes")
ramoneteam=teamset([ramone1,ramone2,ramone3,ramone4,ramone5,ramone7],5)+[ramone6]
ramone=Trainer("Pokémon Trainer Ramone",ramoneteam,"Unova")
#forina
forina1=Shiftry (maxiv="Yes")
forina2=Breloom (maxiv="Yes")
forina3=Tropius(maxiv="Yes")
forina4=Altaria (maxiv="Yes")
forina5=Linoone(maxiv="Yes")
forina6=Jirachi(maxiv="Yes")
forina7=Flygon (maxiv="Yes")
forina8=Absol (maxiv="Yes")
forinateam=teamset([forina1,forina2,forina3,forina4,forina5,forina7,forina8],5)+[forina6]
forina=Trainer("Pokémon Trainer Forina",forinateam,"Hoenn")
#calem
calem1=Xerneas(maxiv="Yes")
calem3=Charizard(maxiv="Yes")
calem4=Clefable (maxiv="Yes")
calem5=Altaria(maxiv="Yes")
calem6=Meowstic(maxiv="Yes")
calem7=MAbsol(maxiv="Yes")
calem10=Chesnaught(maxiv="Yes")
calem11=Jolteon(maxiv="Yes")
calem12=Vaporeon (maxiv="Yes")
calem13=Flareon(maxiv="Yes")
calemteam=teamset([calem3,calem4,calem5,calem7,calem6],4)+[calem10,calem1]
calem=Trainer("Pokémon Trainer Calem",calemteam,"Kalos")
#Lillie
Lillie1=Comfey(maxiv="Yes")
Lillie2=ANinetales(maxiv="Yes")
Lillie3=Clefable(maxiv="Yes")
Lillie4=Solgaleo(name="Nebby(Z-Crystal)",maxiv="Yes")
Lillie5=Ribombee(maxiv="Yes")
Lillie6=Magearna(name="Magearna✨",maxiv="Yes")
Lillie7=Lunala(name="Nebby(Z-Crystal)",maxiv="Yes")
Lillieteam=teamset([Lillie1,Lillie2,Lillie3,Lillie5],4)+teamset([Lillie4,Lillie7],1)+[Lillie6]
Lillie=Trainer("Trial Captain Lillie",Lillieteam,"Alola")
#raifort
raifort1=Grumpig(maxiv="Yes")
raifort2=Seviper(maxiv="Yes")
raifort3=Zoroark(maxiv="Yes")
raifort4=Lumineon(maxiv="Yes")
raifort5=Scizor(maxiv="Yes")
raifort6=Gengar(maxiv="Yes")
raifortteam=teamset([raifort1,raifort2,raifort3,raifort5,raifort4],5)+[raifort6]
raifort=Trainer("Instructor Raifort",raifortteam,"Paldea")
#miriam
miriam1=Pincurchin(maxiv="Yes")
miriam2=Hypno (maxiv="Yes")
miriam3=Sawsbuck(maxiv="Yes")
miriam4=Glalie(maxiv="Yes")
miriam5=Eelektross(maxiv="Yes")
miriam6=Toxapex(maxiv="Yes")
miriamteam=teamset([miriam1,miriam2,miriam3,miriam5,miriam4],5)+[miriam6]
miriam=Trainer("Instructor Miriam",miriamteam,"Paldea")
#dendra
dendra1=PTauros(type2="Fire",maxiv="Yes")
dendra2=PTauros(type2="Water",maxiv="Yes")
dendra3=Falinks(maxiv="Yes")
dendra4=Medicham(maxiv="Yes")
dendra5=Hawlucha(maxiv="Yes")
dendra6=Hariyama(maxiv="Yes")
dendrateam=teamset([dendra1,dendra2,dendra3,dendra5,dendra4],5)+[dendra6]
dendra=Trainer("Instructor Dendra",dendrateam,"Paldea")
#tyme
tyme1=MNLycanroc(maxiv="Yes")
tyme2=Drednaw(maxiv="Yes")
tyme3=MDLycanroc(maxiv="Yes")
tyme4=Stonjourner(maxiv="Yes")
tyme5=Coalossal(maxiv="Yes")
tyme6=Garganacl(maxiv="Yes")
tymeteam=teamset([tyme1,tyme2,tyme3,tyme5,tyme4],5)+[tyme6]
tyme=Trainer("Instructor Tyme",tymeteam,"Paldea")
#salvatore
salvatore1=Honchkrow (maxiv="Yes")
salvatore2=Persian(maxiv="Yes")
salvatore3=Palossand(maxiv="Yes")
salvatore4=Glaceon(maxiv="Yes")
salvatore5=Gothitelle (maxiv="Yes")
salvatore6=Raichu(maxiv="Yes")
salvatoreteam=teamset([salvatore1,salvatore2,salvatore3,salvatore5,salvatore4],5)+[salvatore6]
salvatore=Trainer("Instructor Salvatore",salvatoreteam,"Paldea")
#amber
amber1=Pelipper(maxiv="Yes")
amber2=Ninjask(maxiv="Yes")
amber3=Shedinja(maxiv="Yes")
amber4=Volbeat(maxiv="Yes")
amber6=MSharpedo(maxiv="Yes")
amber5=Gorebyss(maxiv="Yes")
amber=Trainer("Aqua Admin Amber",[amber1,amber2,amber3,amber4,amber5,amber6],"Hoenn")   
#TEST2
t3=Palafin(maxiv="Yes")
t4=Tinglu(maxiv="Yes")
t5=Chienpao(maxiv="Yes")
t6=Chiyu(maxiv="Yes")
t7=Wochien(maxiv="Yes")
t8=Gholdengo(name="Gholdengo💎",maxiv="Steel")
test2=Trainer("Test-02",[t3,t4,t5,t6,t7,t8])
#############
matchx=match()
e4list=[hassel,larry,poppy,rika,will,koga,kahili,acerola,olivia,molayne,hala,caitlin,grimsley,shauntal,marshal,karen,drake,glacia,sidney,phoebe,siebold,lorelei,agatha,bruno,lance,aaron,bertha,lucian,flint,wikstrom,drasna,malva]

champlist=[ash,iris,peony,geeta,oak,odrake,may,leon,alder,brendan,kukui,blue,red,wallace,steven,cynthia,diantha,mustard]
fronlist=[noland,lucy,tucker,greta,anabel,brandon,spenser,palmer,darach,dahlia,argenta,Thorton]
gymlist=[brock,misty,surge,erika,erikah,erikahc,sabrina,janine,blaine,cissy,danny,rudy,luana,falkner,bugsy,whitney,chuck,pryce,jasmine,claire,roxanne,brawly,wattson,flannery,norman,winona,tate,liza,juan,roark,gardenia,fantina,byron,maylene,wake,candice,volkner,lenora,burgh,elesa,clay,skyla,brycen,drayden,cheren,roxie,marlon,viola,grant,korrina,ramos,clemont,valerie,olympia,wulfric,milo,nessa,kabu,bea,allister,opal,bede,gordie,melony,piers,marnie,raihan,klara,avery,katy,brassius,Iono,kofu,ryme,grusha,tulip]

talentlist=[tyme,salvatore,miriam,dendra,raifort,jacq,saguaro,Lillie,mallow,lana,kiawe,Ilima,forina,lucas,calem,hugh,hop,hau,shauna,tierno,ramone,cameron,virgil,dino,burgundy,solidad,tyson,harley,harrison,ritchie,dawn,kenny,ursula,trip,drew,nando,conway,zoey,zinnia,arven,clavell,sordward,shielbert,morimoto,ethan,palina,iscan,calaba,lian,mai,goh,gladion,eusine,benga,trevor,paul,sawyer,emmet,ingo,gary,silver,buck,n,alain,tobias,quillon,danika,horace,barry,wally,nemona,evelyn,adaman]

evilist=[amber,blaise,lusamine,jessiejames,jessie,james,rose,Guzma,volo,penny,eri,ortega,atticus,mela,giacomo,xerosic,aliana,celosia,bryony,mable,lysandre,courtney,shelly,matt,ghetsis,colress,giallo,zinzolin,rood,ryoku,bronius,gorm,alsada,alturo,tabitha,ariana,archer,cyrus,archie,maxie,saturn,mars,jupiter,giovanni,butler]

gym=random.choice(gymlist)
elite4=random.choice(e4list)
champ=random.choice(champlist)
frontier=random.choice(fronlist)
evil=random.choice(evilist)
talent=random.choice(talentlist)
alltr=random.choice([gym,elite4,champ, frontier,evil,talent])
def genplayer2(f):
    pl=None
    field.weather="Clear"
    field.terrain="Normal"
    if "Bridge" in f.location:
        f.location="🌉 "+f.location
    if "River" in f.location:
        f.location="🏞️ "+f.location
    if "Desert" in f.location:
        f.location="🏜️ "+f.location
    if ("Mount" or "Mt") in f.location:
        f.location="⛰️ "+f.location
    if "Forest" in f.location:
        f.location="🌳 "+f.location
    if "Town" in f.location:
        f.location="🏡 "+f.location
    if "City" in f.location:
        f.location="🏙️ "+f.location
    if "Unova" in f.location:
        pl=random.choice([alder,iris,ash,lenora,burgh,elesa,clay,skyla,brycen,drayden,cheren,roxie,marlon,genTrainer(trclass=random.choice(["Unova Trainer"]))])
    if "Tournament" in f.location:
        pl=random.choice(champlist)
    if "Team Flare" in f.location:
        pl=random.choice([malva,xerosic,aliana,celosia,bryony,mable,lysandre,genTrainer(trclass=random.choice(["Ruin Explorer","Hiker"]))])
        if "Malva" in pl.name:
            pl.name="Team Flare Malva"
    if "Trackless" in f.location:
        pl=random.choice([cbeast,genTrainer(trclass=random.choice(["Ruin Explorer","Hiker"]))])
    if "Scorched Slab" in f.location:
        pl=random.choice([cheatran,buck,genTrainer(trclass=random.choice(["Volcano Explorer","Hiker"]))])
    if "Kanto" in f.location:
        pl=random.choice([ash,gary,red,giovanni,jessiejames,genTrainer(trclass=random.choice(["Kanto Trainer"]))])
    if "Hoenn" in f.location:
        pl=random.choice([ethan,silver,genTrainer(trclass=random.choice(["Hoenn Trainer"]))])
    if "Paldea" in f.location:
        pl=random.choice([tyme,salvatore,miriam,dendra,raifort,jacq,saguaro,tulip,grusha,ryme,kofu,Iono,brassius,katy,penny,eri,ortega,atticus,mela,giacomo,hassel,larry,poppy,rika,geeta,genTrainer(trclass=random.choice(["Kanto Trainer"]))])
    if "Johto" in f.location:
        pl=random.choice([ethan,silver,genTrainer(trclass=random.choice(["Johto Trainer"]))])
    if "Sinnoh" in f.location:
        pl=random.choice([cynthia,genTrainer(trclass=random.choice(["Sinnoh Trainer"]))])
    if "Kalos" in f.location:
        pl=random.choice([wulfric,olympia,valerie,clemont,ramos,korrina,viola,grant,diantha,alain,sawyer,tierno,trevor,calem,genTrainer(trclass=random.choice(["Kalos Trainer"]))])
    if "Alola" in f.location:
        pl=random.choice([kahili,acerola,olivia,molayne,hala,kukui,gladion,hau,genTrainer(trclass=random.choice(["Alola Trainer"]))])
    if " Galar" in f.location:
        pl=random.choice([raihan,marnie,piers,melony,gordie,bede,opal,allister,bea,kabu,nessa,milo,leon,genTrainer(trclass=random.choice(["Galar Trainer"]))])
    if "Power Plant" in f.location:
        field.weather="Electric Terrain"
        pl=random.choice([czapdos,genTrainer(trclass=random.choice(["Rocket Grunt","Electrician"]))])
    if "Mt. Ember" in f.location:
        field.weather="Sunny"
        pl=random.choice([cmoltres,genTrainer(trclass=random.choice(["Rocket Grunt","Kindler"]))])
    if "Mt. Chimney" in f.location:
        pl=random.choice([maxie,tabitha,brendan,archie,genTrainer(trclass=random.choice(["Magma Grunt","Aqua Grunt"]))])
    if "Mt. Pyre" in f.location:
        pl=random.choice([phoebe,genTrainer(trclass=random.choice(["Exorcist"]))])
    if "Marine Cave" in f.location:
        f.weather="Primordial Sea"
        pl=random.choice([ckyogre,archie,brendan,may,genTrainer(trclass=random.choice(["Aqua Grunt"]))])
    if "Terra Cave" in f.location:
        f.weather="Desolate Land"
        pl=random.choice([cgroudon,maxie,tabitha,brendan,may,genTrainer(trclass=random.choice(["Magma Grunt"]))])
    if "Aqua Hideout" in f.location:
        pl=random.choice([archie,genTrainer(trclass=random.choice(["Aqua Grunt"]))])
    if "Magma Hideout" in f.location:
        pl=random.choice([maxie,tabitha,genTrainer(trclass=random.choice(["Magma Grunt"]))])
    if "Mountain Coronet" in f.location:
        pl=random.choice([cyrus,genTrainer(trclass=random.choice(["Sinnoh Trainer","Galactic Grunt"]))])
    if "Spear Pillar" in f.location:
        pl=random.choice([cyrus,cynthia,saturn,barry])
    if "Mountain Stark" in f.location:
        pl=random.choice([buck,saturn,genTrainer(trclass=random.choice(["Sinnoh Trainer","Ruin Explorer","Fiery Breathe","Kindler","Paleontologist"]))])
    if "League, Sinnoh" in f.location:
        pl=random.choice([aaron,bertha,flint,lucian,cynthia,tobias,barry])
        if "Tobias" in pl.name:
            pl.name="SCL Champion Tobias"
    if "Evergrande" in f.location:
        pl=random.choice([sidney,phoebe,glacia,drake,steven,wallace])
    if "Sootopolis City" in f.location:
        pl=random.choice([juan,wallace,genTrainer(trclass=random.choice(["Swimmer","Hoenn Trainer","Scuba Diver","Fisherman"]))])
    if "Mosdeep City" in f.location:
        pl=random.choice([tate,liza,steven,maxie,genTrainer(trclass=random.choice(["Hoenn Trainer","Psychic"]))])
    if "Fortree City" in f.location:
        pl=random.choice([winona,steven,may,genTrainer(trclass=random.choice(["Hoenn Trainer","Pilot","Air Force Officer"]))])
    if "Lavaridge Town" in f.location:
        pl=random.choice([flannery,genTrainer(trclass=random.choice(["Hoenn Trainer","Kindler","Fiery Breathe"]))])
    if "Mauville City" in f.location:
        pl=random.choice([wattson,wally,may,genTrainer(trclass=random.choice(["Hoenn Trainer","Rocker","Guitarist"]))])
    if "Dewford Town" in f.location:
        pl=random.choice([brawly,steven,genTrainer(trclass=random.choice(["Hoenn Trainer","Blackbelt","Dojo Master"]))])
    if "Sunnyshore City" in f.location:
        pl=random.choice([volkner,jasmine,flint,paul,genTrainer(trclass=random.choice(["Sinnoh Trainer","Electrician","Rocker","Guitarist"]))])
    if "Snowpoint City" in f.location:
        field.weather="Snowstorm"
        pl=random.choice([candice,brandon,tobias,paul,genTrainer(trclass=random.choice(["Sinnoh Trainer","Elder Trainer","Galactic Grunt","Skier","Boarder"]))])
    if "Canalave City" in f.location:
        pl=random.choice([byron,roark,paul,barry,genTrainer(trclass=random.choice(["Sinnoh Trainer","Industry Worker","Factory Boss","Electrician","Sailor"]))])
    if "Hearthome City" in f.location:
        pl=random.choice([fantina,paul,barry,genTrainer(trclass=random.choice(["Sinnoh Trainer","Exorcist"]))])
    if "Pastoria City" in f.location:
        pl=random.choice([wake,paul,genTrainer(trclass=random.choice(["Sinnoh Trainer","Blackbelt","Swimmer","Fisherman"]))])
    if "Veilstone City" in f.location:
        pl=random.choice([maylene,cyrus,saturn,paul,genTrainer(trclass=random.choice(["Sinnoh Trainer","Galactic Grunt","Blackbelt"]))])
    if "Eterna City" in f.location:
        pl=random.choice([gardenia,saturn,paul,genTrainer(trclass=random.choice(["Sinnoh Trainer","Gardener","Galactic Grunt"]))])
    if "Oreburgh City" in f.location:
        pl=random.choice([roark,paul,genTrainer(trclass=random.choice(["Sinnoh Trainer","Paleontologist","Ruin Explorer"]))])
    if "Rustboro City" in f.location:
        pl=random.choice([roxanne,genTrainer(trclass=random.choice(["Hoenn Trainer","Paleontologist","Aqua Grunt","Ruin Explorer"]))])
    if "Petalburg City" in f.location:
        pl=random.choice([norman,wally,genTrainer(trclass=random.choice(["Hoenn Trainer","Bug Catcher","Bug Researcher"]))])
    if "Twinleaf Town" in f.location:
        pl=random.choice([barry,genTrainer(trclass=random.choice(["Sinnoh Trainer"]))])
    if "Littleroot Town" in f.location:
        pl=random.choice([brendan,norman,may,genTrainer(trclass=random.choice(["Hoenn Trainer"]))])
    if "Cianwood City" in f.location:
        pl=random.choice([horace,chuck,genTrainer(trclass=random.choice(["Blackbelt","Dojo Master"]))])
    if "Azalea City" in f.location:
        pl=random.choice([bugsy,genTrainer(trclass="Bug Catcher")])
    if "Blackthorn City" in f.location:
        pl=random.choice([claire,genTrainer(trclass="Dragon Tamer")])
    if "Ecruteak City" in f.location:
        pl=random.choice([morty,genTrainer(trclass="Exorcist")])
    if "Mahogany Town" in f.location:
        pl=random.choice([pryce,genTrainer(trclass=random.choice(["Johto Trainer","Boarder","Skier"]))])
    if "Lavender Town" in f.location:
        pl=random.choice([morty,blue,genTrainer(trclass="Exorcist")])
    if "Safari Zone" in f.location:
        pl=genTrainer(trclass=random.choice(["Fisherman","Bug Researcher","Bug Catcher","Rocket Grunt"]))
    if "Cycling Road" in f.location:
        pl=genTrainer(trclass=random.choice(["Biker","Cueball","Thief","Smuggler","Goon","Driver","Street Punk"]))
    if "Seafoam Island" in f.location:
        field.weather="Snowstorm"
        pl=random.choice([carticuno,genTrainer(trclass=random.choice(["Skier","Boarder"]))])        
    if "Rock Tunnel" in f.location or "Mount Moon" in f.location:
        pl=genTrainer(trclass=random.choice(["Ruin Explorer","Hiker","Paleontologist"]))
    if f.location in ["Victory Road, Kanto","Victory Road, Hoenn"]:
        pl=genTrainer(trclass=random.choice(["Ace Trainer","Challenger","Dragon Tamer"]))
    if "Violet City" in f.location:
        pl=falkner
    if "Olivine City" in f.location:
        pl=jasmine
    if "Indigo Plateau" in f.location:
        pl=random.choice([lorelei,bruno,agatha,lance,will,karen,koga,blue])
        blue.name="Kanto Champion Blue"
        ch=random.randint(1,3)
        if ch==3:
            lance.name="Johto Champion Lance"
        if ch==2:
            lance.name="Kanto Champion Lance"
    if "Goldenrod City" in f.location:
        pl=random.choice([whitney,genTrainer(trclass=random.choice(["Rocket Grunt","Paleontologist"]))])
    if "New Bark Town" in f.location:
        pl=random.choice([ethan,silver])
    if "Mount Silver" in f.location:
        pl=red
    if "Cinnabar Island" in f.location:
        pl=blaine
    if "Battle Frontier, Hoenn" in f.location:    
        pl=random.choice(brandon,noland,lucy,greta,anabel,tucker,spenser)
    if "Fuchsia City" in f.location:    
        pl=koga 
        koga.name="Gym Leader Koga"
    if "Celadon City" in f.location:
        pl=random.choice([erika,genTrainer(trclass=random.choice(["Rocket Grunt","Businessman"]))])
    if "Vermilion City" in f.location:
        pl=random.choice([surge,genTrainer(trclass=random.choice(["Rocker","Businessman","Guitarist","Sailor","Electrician"]))])
    if "Saffron City" in f.location:
        pl=sabrina
    if "Pallet Town" in f.location:
        pl=random.choice([gary,ash])
    if "Viridian Forest" in f.location:
        pl=genTrainer(random.choice(["Bug Catcher","Bug Researcher"]))
    if "Viridian City" in f.location:
        pl=random.choice([giovanni,blue])
        blue.name="Gym Leader Blue"
        giovanni.name="Gym Leader Giovanni"
    if "Pewter City" in f.location:
        pl=brock
    if "Cerulean Cave" in f.location:
        pl=random.choice([giovanni,red,cmewtwo,genTrainer(trclass=random.choice(["Ace Trainer","Challenger"]))])
    if "Cerulean City" in f.location:
        pl=random.choice([misty,genTrainer(trclass=random.choice(["Swimmer","Marine Biologist"]))])
        field.weather="Cloudy"
    if pl is None:
        pl=random.choices([matchx[1],gym,elite4,champ,frontier,evil,talent],weights=[15,5,5,5,5,5,5],k=1)[0]
    return pl
#PLAYER 02
#PLAYER 01
