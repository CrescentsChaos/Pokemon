from pokemonlist import *
from trainers import *
p1AI=True
p2AI=True

def fuse(c1,c2):
    x=c1(maxiv="Yes")
    y=c2(maxiv="Yes")
    z=Pokemon2(maxiv="Yes")
    prdx=["Great Tusk","Sandy Shocks","Roaring Moon","Brute Bonnet","Slither Wing","Flutter Mane","Scream Tail","Iron","Unbound","Tapu","Black","White","Attack","Defense","Speed","Hero","Alolan","Hisuian","Galarian","Dusk Mane","Dawn Wing","Black","White","Ice Rider","Shadow Rider","Single","Rapid","Sky","Alpha","Totem","Pom Pom","Sensu","West Sea","East Sea","Rotom","Resolute","Crowned","Lycanroc","Gastrodon","Gourgeist"]
    for i in prdx:
        if i in y.name:
            y.name=y.name.split(" ")[-1]
        if i in x.name:
            x.name=x.name.split(" ")[-1]
    if "Unrivaled" in y.name:
        y.name=y.name.split(" ")[0]            
    if "Z-Crystal" in y.name:
        y.name=y.name.split("(")[0]
    if "Z-Crystal" in x.name:
        x.name=x.name.split("(")[0]
    z.name=x.name[:len(x.name)//2]+y.name[len(y.name)//2:]#+f"({x.name}+{y.name})"
    z.type1,z.type2=x.type1,y.type2
    if x.type1==y.type2:
        z.type2="None"
    if x.type1!=y.type1 and y.type2=="None":
        z.type2=y.type1
    z.hpiv,z.atkiv,z.defiv,z.spatkiv,z.spdefiv,z.speediv=x.hpiv,z.atkiv,z.defiv,z.spatkiv,z.spdefiv,z.speediv    
    x.calcst()
    y.calcst()
    z.ability=y.ability
    z.item=x.item
    z.hp=x.hp/2.5
    z.atk=x.atk
    z.defense=x.defense
    z.spatk=y.spatk
    z.spdef=y.spdef
    z.speed=y.speed
    z.nature=y.nature
    z.speedev=252
    z.tera=x.tera
    if z.atk<z.spatk:
        z.spatkev=252
    if z.atk>z.spatk:
        z.atkev=252
    z.calcst()
    z.hp=z.maxhp
    #print(z.maxspatk)
    #z.info()
    z.moves=[x.moves[3],x.moves[2],y.moves[3],y.moves[2]]
    z.pplist=[x.pplist[3],x.pplist[2],y.pplist[3],y.pplist[2]]
    #movelist(z,x,field)
    return z
z=fuse(Gallade, Charizard)    
megastones=["Gyaradosite","Venusaurite","Charizardite X","Charizardite Y","Abomasite","Absolite","Aerodactylite","Aggronite","Alakazite","Altarianite","Amoharosite","Audinite","Banettite","Beedrillite","Blastoisinite","Blazikenite","Camerupite","Diancite","Galladite","Garchompite","Gardevoirite","Gengarite","Glalitite","Heracronite","Houndoominite","Kangaskhanite","Latiasite","Latiosite","Lopunnite","Lucarionite","Manectite","Mawilite","Medichamite","Metagrossite","Mewtwonite X","Mewtwonite Y","Pidgeotite","Pinsirite","Sablenite","Salamencite","Sceptilite","Scizorite","Sharpedonite","Slowbronite","Steelixite","Seampertite","Tyranitarite"]
allclass=["Black Belt","Dojo Master","Dragon Tamer","Skier","Kindler","Sailor","Swimmer","Veteran","Challenger","Ace Trainer","Expert","Street Punk","Scuba Diver","Ruin Maniac","Paleontologist","Surfer","Marine Biologist","Biker","Cueball","Bird Keeper","Pilot","Sky Diver","Venom Expert","Fire Breather","Rocker","Guitarist","Bug Catcher","Psychic","Exorcist","Electrician","Smuggler","Thief","Goon","Boarder","Desert Explorer","Egyptian","Tamer","Captain","Pirate","Driver","Magma Grunt","Aqua Grunt","Rocket Grunt","Galactic Grunt","Gardener","Factory Boss","Industry Worker","Hiker","Kanto Trainer","Johto Trainer","Hoenn Trainer","Sinnoh Trainer","Unova Trainer","UB Expert","Businessman","Police Officer","Investigator","Military Officer","Navy Officer","Air Force Officer","Bug Researcher","Fisherman","Chaos Trainer","Plasma Grunt","Shadow Triads","Kalos Trainer","Alola Trainer","Galar Trainer","Chef","MasterChef","Cook","Foodie","Beauty","Gentleman","Camper","Lass","Scientist","Breeder","Pokémon Ranger","Backpacker","Policeman","Super Nerd","Cool Trainer","Pokémon Trainer","Paldea Trainer","Battle Girl","Worker","Doctor","Nurse","Coach Trainer","Poké Maniac","Juggler","Crush Girl","Channeler","Waiter","Musician","Aroma Lady","Butler","Count","Countess","Duke","Earl","Pro Wrestler","Burglar","Gambler","Teacher","Parasol Lady","Tuber","Rancher","Smasher","Triathlete","Competitive Player","Fusion Trainer"]
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
#    print(" ⚠️TET: "+trclass)
    "Creates Team"
    mons=[]
    team=[]
    new_name=None
    if trclass in ["Triathlete"]:
        mons=[Magnezone, Pelipper,Starmie,Dodrio,Electrode,Flareon,Pinsir,Houndoom,Wyrdeer,Mantine, Klinklang,Wailord,Kingdra, Azumarill,Minun,Plusle,Arcanine, Floatzel, Tentacruel,Golduck,Walrein, Sableye,Slaking, Poliwrath, Politoed]
    if trclass in ["Pokémon Trainer","Pokémon Ranger","Competitive Player","Fusion Trainer"]:
        mons=allmon
    ultrabeasts=[Blacephalon,Stakataka,Naganadel,Necrozma,DMNecrozma,DWNecrozma,FMLunala,RSSolgaleo,Lunala,Solgaleo,Guzzlord,Kartana,Celesteela,Xurkitree,Buzzwole,Nihilego,Pheromosa]
    legendary=[Chiyu,Tinglu,Chienpao,Wochien,Enamorus,TEnamorus,Koraidon,Miraidon,ICalyrex,SCalyrex,Regieleki,Regidrago,Glastrier,Spectrier,Zarude,DUrshifu,WUrshifu,Eternatus,Zamazenta,Zacian,GArticuno,GZapdos,GMoltres,Melmetal,Zeraora,Silvally,Marshadow,Magearna,Tapufini,Tapubulu,Tapulele,Tapukoko,Diancie,UHoopa,Volcanion,CZygarde,Xerneas,Yveltal,Genesect,Keldeo,Meloetta,PMeloetta,BKyurem,WKyurem,Zekrom,Reshiram,Kyurem,TLandorus,TThundurus,TTornadus,Thundurus,Tornadus,Landorus,Victini,Cobalion,Terrakion,Virizion,Arceus,Shaymin,SShaymin,Darkrai,Cresselia,Manaphy,Uxie,Azelf,Mesprit,Registeel,Regirock,Regice,Articuno,Zapdos,Moltres,Raikou,Entei,Suicune,Lugia,Hooh,Celebi,Deoxys,ADeoxys,SDeoxys,DDeoxys,Jirachi,Mew,Rayquaza,Latias,Latios,Groudon,Kyogre,Mewtwo,Dialga,Palkia,Giratina,Heatran,Regigigas]
    if trclass in ["UB Expert"]:
        mons=ultrabeasts
    if trclass in ["Paldea Trainer"]:
        palmon=[Meowscarada,Skeledirge, Quaquaval, Oinkologne,Spidops,Lokix,Pawmot, Clodsire,Maushold,Dachsbun, Arboliva, Garganacl, Annihilape,Armarouge, Ceruledge,Bellibolt, Kilowattrel, Dudunsparce, Farigiraf,Mabosstiff,Grafaiai,Brambleghast, Toedscruel,Klawf, Scovillain,Rabsca,Espathra,Tinkaton,Wugtrio, Bombirdier,Palafin,Revavroom,Cyclizar, Orthworm, Glimmora,Houndstone, Flamigo,Cetitan, Kingambit,Veluza,Dondozo,Tatsugiri, Greattusk, Screamtail, Brutebonnet, Fluttermane, Slitherwing, Sandyshocks, Irontreads,Ironbundle,Ironhands, Ironjugulis,Ironmoth,Ironthorns, Baxcalibur, Gholdengo,Wochien,Chienpao,Tinglu,Chiyu, Roaringmoon, Ironvaliant,Koraidon,Miraidon, Ironleaves, Walkingwake]
        natmon=[Charizard,Pikachu,Primeape,Chansey,Golduck, Wigglytuff,Hypno,Gengar,Raichu, Gyarados,Persian,Dugtrio,Eevee,Primeape,Jolteon, Vaporeon,Flareon,Muk,Electrode,Ditto,Arcanine, Tauros,PTauros, Venomoth,Scyther, Slowbro, Cloyster, Dragonite,Articuno,Zapdos,Moltres,Mewtwo,Mew, Typhlosion,Jumpluff, Houndoom,Sunflora,Blissey, Azumarill, Sudowoodo, Ampharos,Quagsire,Donphan,Espeon,Umbreon, Ursaring, Forretress, Scizor, Heracross, Tyranitar, Slowking,Delibird, Masquerain, Gardevoir, Slaking, Breloom,Grumpig, Hariyama, Pelipper,Swalot,Torkoal,Camerupt, Medicham,Whiscash,Zangoose,Seviper,Altaria,Tropius,Cacturne,Salamence,Sableye,Glalie, Kricketune, Vespiquen, Floatzel,Gallade,Luxray, Staraptor, Mismagius, Garchomp, Drifblim, Bronzong, Lucario, Toxicroak, Leafeon,Glaceon, Pachirisu,Skuntank, Magnezone, Weavile, Honchkrow, Hippowdon,Spiritomb,WRotom,HRotom,MRotom,FRotom,FrRotom, EGastrodon, WGastrodon,Lumineon, Abomasnow,Froslass, Lilligant,Haxorus, Sawsbuck, Amoongus, Zoroark, Gothitelle, Krookodile,Volcarona, Alomomola, Eelektross, Beartic, Cryogonal, Braviary, Bisharp, Hydreigon, Talonflame, Vivillon,Florges,Goodra, Sylveon,Dedenne,Gogoat,Pyroar,Hawlucha,Noivern, Dragalge, Clawitzer, Avalugg, Gumshoos,Tsareena, MDLycanroc, MNLycanroc, DLycanroc, Oricorio, Crabominable, Salazzle, Mimikyu,Lurantis,Mudsdale,Oranguru,Passimian,Komala,Palossand,Toxapex,Greedent, Corviknight, Drednaw, Coalossal,Appletun,Flapple,Copperajah, Barraskewda, Toxtricity, Polteageist, Indeedee, Sandaconda, Hatterene, Grimmsnarl, Dragapult, Stonjourner, Eiscue, Pincurchin, Frosmoth]
        mixmon=natmon+palmon
        mons=random.choice([mixmon,palmon])
    if trclass in ["Galar Trainer"]:
        galmon=[HElectrode,GArticuno,GZapdos,GMoltres,GRapidash,GSlowbro,GSlowking,Sirfetchd,GWeezing,MrRime,HArcanine,HTyphlosion,GCorsola,HSamurott,HLilligant,Obstagoon,GDarmanitan,HZoroark,HBraviary,HGoodra,HAvalugg,HDecidueye,Melmetal,Runerigus,Garbodor,Rillaboom,Cinderace,Inteleon,Corviknight,Greedent,Orbeetle,Thievul,Dubwool,Eldegoss,Drednaw,Coalossal,Flapple,Appletun,Boltund,Sandaconda,Barraskewda,Toxtricity,Grapploct,Centiskorch,Polteageist,Hatterene,Grimmsnarl,Perrserker,Alcremie,Frosmoth,Stonjourner,Cursola,MrRime,Falinks,Pincurchin,Eiscue,Indeedee,Copperajah,Dracovish,Dracozolt,Arctovish,Arctozolt,Duraludon,Dragapult,DUrshifu,WUrshifu, Pyukumuku]
        natmon=[Venusaur, Charizard,Blastoise,Butterfree,Pikachu,Meowth, Machamp,Gengar,Kingler,Lapras,Snorlax,Sandslash, Nidoqueen,Nidoking,Clefable, Ninetales, Wigglytuff,Vileplume,Dugtrio,Golduck,Arcanine,Poliwrath, Alakazam,Tentacruel,Rapidash,Slowbro, Cloyster, Exeggutor,Marowak, Hitmonlee, Hitmonchan,Weezing,Rhydon,Chansey, Kangaskhan, Seaking,Starmie,MrMime,Jynx,Pinsir,Tauros, Gyarados,Ditto, Vaporeon, Jolteon,Flareon,Omastar, Kabutops, Aerodactyl, Articuno, Zapdos,Moltres, Dragonite,Noctowl,Lanturn,Xatu, Bellossom, Sudowoodo,Politoed, Quagsire, Espeon,Umbreon, Slowking,Wobbuffet, Steelix,Scizor,Shuckle,Heracross, Octillery,Delibird,Mantine,Skarmory,Kingdra, Porygon2,Hitmontop,Miltank, Blissey, Raikou,Suicune,Entei, Tyranitar,Celebi,Hooh,Lugia,Mew,Mewtwo,Sceptile,Blaziken,Swampert,Linoone,Ludicolo,Shiftry, Pelipper, Gardevoir,Ninjask,Shedinja,Exploud, Sableye,Mawile,Aggron,Manectric,Sharpedo,Wailord, Torkoal, Flygon,Altaria,Whiscash,Solrock,Lunatone,Crawdaunt,Claydol,Cradily,Armaldo,Milotic,Dusclops,Absol,Glalie,Walrein,Relicanth,Salamence, Metagross,Regirock,Regice,Registeel,Latias,Latios,Kyogre,Groudon, Rayquaza,Jirachi,Luxray,Roserade,Vespiquen,Cherrim, WGastrodon, EGastrodon,Drifblim, Lopunny,Skuntank,Bronzong,Spiritomb, Garchomp,Lucario, Hippowdon,Drapion,Toxicroak, Abomasnow,Weavile, Magnezone, Lickilicky,Rhyperior, Tangrowth,Electivire,Magmortar,Togekiss,Leafeon,Glaceon,Mamoswine, PorygonZ,Dusknoir,Gallade,Froslass,HRotom,FrRotom,FRotom,WRotom,MRotom,Uxie,Mesprit,Azelf,Dialga,Palkia,Heatran,Regigigas,Giratina,Giratina, Cresselia,Victini, Stoutland, Liepard,Musharna, Unfezant, Gigalith,Swoobat, Excadrill,Audino, Conkeldurr, Seismitoad,Sawk,Throh, Scolipede, Whimsicott, Lilligant, Krookodile, Darmanitan, Maractus,Crustle,Scrafty, Sigilyph, Cofagrigus, Carracosta,Archeops, Garbodor,Zoroark,Cinccino, Gothitelle, Reuniclus, Vanilluxe,Emolga,Escavalier, Amoongus, Jellicent, Galvantula, Ferrothorn, Klinklang, Beheeyem, Chandelure, Haxorus,Beartic, Cryogonal,Accelgor,Stunfisk,GStunfisk,Mienshao, Druddigon,Golurk, Bisharp, Bouffalant, Braviary,Mandibuzz,Heatmor,Durant, Hydreigon, Volcarona,Cobalion, Terrakion, Virizion, Tornadus, TTornadus, Thundurus, TThundurus,Reshiram,Zekrom, Landorus, TLandorus,Kyurem,WKyurem,BKyurem,Keldeo,Genesect]
        mixmon=natmon+galmon
        mons=random.choice([mixmon,galmon])
    if trclass in ["Alola Trainer"]:
        mons=[ARaticate,ARaichu,ASandslash,ANinetales,ADugtrio,APersian,AGolem,AMuk, AExeggutor,AMarowak,Decidueye,Incineroar,Primarina,Toucannon, Vikavolt,DLycanroc,MDLycanroc,MNLycanroc,SWishiwashi, Toxapex,Mudsdale,Araquanid,Salazzle,Bewear,Tsareena,Golisopod,Palossand, Silvally,Turtonator,Mimikyu,Drampa, Dhelmise,Kommo,Gumshoos, Lilligant,Lurantis,Oranguru,Passimian, Ribombee, Crabominable, Oricorio, Shiinotic,Comfey,Komala,Togedemaru,Tapukoko,Tapulele,Tapubulu,Tapufini,Solgaleo,Lunala, Nihilego,Buzzwole,Pheromosa,Xurkitree,Celesteela,Kartana,Guzzlord, Necrozma,DMNecrozma,DWNecrozma,Magearna,Marshadow, Naganadel,Stakataka,Blacephalon,Zeraora,Melmetal]
    if trclass in ["Kalos Trainer"]:
        mons=[Chesnaught, Delphox, Greninja, Talonflame, Vivillon,Pyroar,Florges,Gogoat,Pangoro,Meowstic, Aegislash,Malamar, Barbaracle,Dragalge, Clawitzer,Heliolisk,Tyrantrum,Aurorus, Sylveon,Hawlucha,Goodra,Klefki,Trevenant,Gourgeist,Avalugg,Noivern,Blastoise,Venusaur,Charizard,Alakazam, Gyarados,Gengar,Beedrill]
    if trclass in ["Johto Trainer"]:
        mons=[Donphan,Porygon2,Miltank,Magcargo,Corsola,Delibird,Mantine,Granbull,Shuckle,Ursaring,Slowking,Wobbuffet,Forretress,Quagsire,Sunflora,Jumpluff,Sudowoodo,Bellossom,Xatu,Hitmontop,Ariados,Noctowl,Ledian,Furret,Meganium,Typhlosion,Feraligatr, Crobat,Lanturn,Ampharos,Azumarill,Politoed,Espeon,Umbreon,Steelix,Scizor,Heracross,Skarmory,Houndoom,Kingdra,Blissey,Tyranitar]
    if trclass in ["Kanto Trainer"]:
        mons=[Ditto,Scyther,Seaking,Rhydon,Chansey,Marowak,Electrode,Hypno,Persian,Dugtrio,Kingler,Wigglytuff,Sandslash,Clefable,Butterfree,Beedrill,Fearow,Pikachu,Venusaur,Charizard,Blastoise,Pidgeot,Arbok, Nidoking,Nidoqueen,Ninetales,Golduck,Primeape,Arcanine,Poliwrath, Alakazam,Machamp,Victreebel,Tentacruel,Golem,Rapidash,Slowbro,Dodrio,Dewgong,Muk,Cloyster,Gengar,Exeggutor,Hitmonchan,Hitmonlee,Weezing,Kangaskhan,Starmie,Tauros,Jynx,Pinsir,Gyarados,Lapras,Jolteon,Vaporeon,Flareon,Omastar,Kabutops,Aerodactyl,Snorlax,Dragonite]
    if trclass in ["Hoenn Trainer"]:
        mons=[ Sceptile,Blaziken,Swampert,Mightyena,Ludicolo,Shiftry,Swellow,Pelipper,Gardevoir,Breloom, Slaking,Exploud,Hariyama,Aggron,Medicham,Sharpedo,Wailord,Camerupt,Torkoal,Flygon,Altaria,Zangoose,Seviper,Solrock,Lunatone,Whiscash,Crawdaunt,Claydol,Cradily,Armaldo,Milotic,Banette,Absol,Glalie,Walrein,Huntail,Gorebyss,Relicanth,Salamence,Metagross]
    if trclass in ["Sinnoh Trainer"]:
        mons=[Lickilicky,Torterra,Infernape,Empoleon,Staraptor,Luxray,Roserade,Rampardos,Bastiodon,Vespiquen,EGastrodon,WGastrodon,Ambipom,Drifblim,Mismagius,Honchkrow,Purugly,Skuntank,Bronzong,Spiritomb,Garchomp,Lucario,Hippowdon,Drapion,Toxicroak,Abomasnow,Weavile,Magnezone,Rhyperior,Tangrowth,Electivire,Magmortar,Togekiss,Yanmega,Gliscor,Gallade,Probopass,Dusknoir,Froslass,WRotom]
    if trclass in ["Unova Trainer"]:
        mons=[Musharna,Sawk,Throh,Simipour,Simisage,Simisear,Garbodor,Serperior,Emboar,Samurott,Stoutland,Unfezant,Zebstrika,Gigalith,Excadrill,Conkeldurr,Seismitoad,Leavanny,Scolipede,Krookodile,Darmanitan,Scrafty,Cofagrigus,Carracosta,Archeops,Zoroark,Gothitelle, Reuniclus, Swanna,Vanilluxe,Escavalier,Jellicent,Galvantula,Ferrothorn,Eelektross,Chandelure,Haxorus,Beartic,Accelgor,Mienshao,Druddigon,Golurk,Bisharp,Bouffalant,Braviary,Mandibuzz,Heatmor,Durant,Hydreigon,Volcarona, Venusaur, Charizard, Blastoise,Sceptile,Swampert,Blaziken]
#FIGHTING SPECIALIST 
    if trclass in ["Dojo Master","Black Belt","Pro Wrestler","Smasher"]:
        namelist=["Taishi","Damme","Wesley","Joe","Dolph","Kenji","Kiyo","Lao","Lung","Nob","Wai","Yoshi","Atsushi","Daisuke","Hideki","Hitoshi","Koichi","Koji","Yuji","Rhett","Takao","Theodore","Zander","Aaron","Hugh","Mike","Nicolas","Shea","Takashi","Adam","Carl","Colby","Darren","David","Derek","Gregory","Griffin","Jarrett","Kendal","Luke","Nathaniel","Philip","Rafael","Ray","Ricky","Sean","Willie","Davon","Ander","Kenji","Manford","Benjamin","Edward","Grant","Jay","Kendrew","Kentaro","Ryder","Teppei","Tyrone","Corey","Donny","Drago","Gordon","Grigor","Jeriel","Kenneth","Mathis","Martell","Rodrigo","Rich","Rocky","Wesley","Zachery","Alonzo","Gunnar","Killan","Markus","Yanis","Ricardo","Igor","Cadox","Banting","Clayton","Earl","Greg","Roy","Terry","Walter","Tracy","Alvaro","Curtis"]
        nn=random.choice(namelist)
        new_name=trclass+" "+nn
        mons=[Sawk,Throh,PTauros,Flamigo,Slitherwing,Annihilape,Quaquaval,Ironvaliant,Ironhands,Greattusk,Hitmontop,DUrshifu,WUrshifu,Sirfetchd,Grapploct,Sneasler,HDecidueye,Hawlucha,Pangoro,Chesnaught,Mienshao,Scrafty,HLilligant,Conkeldurr,Emboar,Gallade,Machamp,Poliwrath,Hitmonchan,Hitmonlee,Infernape,Blaziken,Breloom,Primeape,Heracross,Hariyama]
    
        #STEEL
    if trclass in ["Factory Boss","Industry Worker"]:
        mons=[Revavroom,Gholdengo,Tinkaton,Orthworm,Kingambit,Irontreads,Mawile,ADugtrio,ASandslash,Duraludon,Copperajah,Perrserker,Corviknight,Dhelmise,HGoodra,Aegislash,Bisharp,Magnezone,Steelix,Scizor,Skarmory,Aggron,Metagross,Empoleon,Bastiodon,Bronzong,Lucario,Probopass,Heatran,Excadrill,Ferrothorn,Escavalier]
        #Ghost
    if trclass in ["Exorcist","Channeler"]:
        namelist=["Gabrielle","Candido","Bishop","William","Bowden","Joseph","Thomas","Fantino","Angelo"]
        nn=random.choice(namelist)
        new_name=trclass+" "+nn
        mons=[Ceruledge,Houndstone,Annihilape,Skeledirge,Fluttermane,GCorsola,AMarowak,Dragapult,Polteageist,Mimikyu,Decidueye,Gourgeist,Aegislash,Trevenant,Golurk,Gengar,HTyphlosion,Banette,Dusknoir,Drifblim,Mismagius,Spiritomb,Froslass,Cofagrigus,Runerigus,HZoroark,Jellicent,Chandelure, Sableye]
        
        #Psychic
    if trclass in ["Psychic","Juggler"]:
        mons=[Musharna,Armarouge,Espathra,Veluza,Screamtail,Grumpig,Wobbuffet,Slowking,Xatu,MrMime,Hypno,Indeedee,GSlowking,GSlowbro,GRapidash,Wyrdeer,Malamar,Delphox,HBraviary,Alakazam,Slowbro,Exeggutor,Starmie,Jynx,Espeon,Farigiraf,Gardevoir,Medicham,Lunatone,Solrock,Claydol,Metagross, Bronzong,Gallade,Gothitelle,Reuniclus, Gengar,Chimecho, Drifblim,Dusknoir,Banette,Dusclops,Absol,Swoobat, Mismagius,Musharna, Sigilyph,Beheeyem]
        
        #Grass
    if trclass == "Gardener":
        mons=[Simisage,Scovillain,Brutebonnet,Arboliva,Whimsicott,Toedscruel,Meowscarada,Leafeon,Cherrim,Tropius,Cacturne,Sunflora,Jumpluff, Bellossom,Parasect,Vileplume,Flapple,Appletun,Rillaboom,Dhelmise,Tsareena,HElectrode,HDecidueye,Gourgeist,Decidueye,Trevenant,Gogoat,Florges,Venusaur,Victreebel,Exeggutor,AExeggutor,Tangrowth,Meganium,Sceptile,Ludicolo,Shiftry,Breloom,Roserade,Cradily,Torterra,Abomasnow,Serperior,Leavanny,HLilligant,Ferrothorn,Crawdaunt,MRotom]+random.choices([Shaymin,SShaymin],k=1)
    if trclass in ["Chef","MasterChef","Cook","Foodie","Waiter"]:
        mons=[Dachsbun,Slurpuff, Vanilluxe,Tropius,Polteageist, Alcremie,Miltank,Shuckle,Coalossal,Tsareena,Appletun,Blaziken,Audino, Abomasnow,Blaziken,Audino,Golduck,Parasect,Ribombee, Gyarados, Exeggutor,Shiinotic, Vespiquen,Arboliva,Breloom, Amoongus,Toedscruel]
        
    if trclass in ["Camper","Rancher"]:
        if trclass=="Rancher":
            mons=[Rapidash,Miltank,Tauros,Ambipom,Golduck, Farigiraf,PTauros, Bouffalant]
        else:
            mons=[Dugtrio,Sandslash, Annihilape,Primeape,Raticate,Arbok, Blastoise,Fearow, Arcanine, Charizard, Nidoking, Victreebel,Golduck, Azumarill,Crobat,Tauros,Golem, Magcargo,Claydol, Swellow,Linoone,Kecleon,Shiftry,Xatu, Cacturne, Whiscash,Pinsir, Heracross, Luxray,Dustox, Beautifly,Gengar,Skuntank,Floatzel, Infernape, Staraptor,Bibarel, Jumpluff,Rhydon, Poliwrath,Politoed, Sudowoodo,Lanturn, Slaking,Swalot,Plusle,Minun,Volbeat,Illumise,Dodrio,Pelipper,Camerupt,Flareon,Eevee,Kingler]
        
        #BUG
    if trclass in ["Bug Catcher","Bug Researcher"]:
        if "Hoenn" in field.location:
            mons=[Ribombee,Shuckle,Forretress,Ariados,Ledian,Scyther,Venomoth,Parasect,Butterfree,Beedrill,Scizor,Heracross,Pinsir,Shedinja,Ninjask,Masquerain,Beautifly,Dustox,Illumise,Volbeat,Armaldo]
        if "Johto" in field.location:
            mons=[Shuckle,Forretress,Ariados,Ledian,Scyther,Venomoth,Parasect,Butterfree,Beedrill,Scizor,Heracross,Pinsir]
        if "Sinnoh" in field.location:
            mons=[Ribombee,Shuckle,Forretress,Ariados,Ledian,Scyther,Venomoth,Parasect,Butterfree,Beedrill,Scizor,Heracross,Pinsir,Shedinja,Ninjask,Masquerain,Beautifly,Dustox,Illumise,Volbeat,Armaldo, Kricketune, Wormadam, SWormadam,TWormadam,Mothim, Vespiquen,Drapion,Yanmega]
        if "Unova" in field.location:
            mons=[Ribombee,Shuckle,Forretress,Ariados,Ledian,Scyther,Venomoth,Parasect,Butterfree,Beedrill,Scizor,Heracross,Pinsir,Shedinja,Ninjask,Masquerain,Beautifly,Dustox,Illumise,Volbeat,Armaldo, Kricketune, Wormadam, SWormadam,TWormadam,Mothim, Vespiquen,Drapion,Yanmega, Leavanny, Scolipede,Crustle, Escavalier,Accelgor, Galvantula,Durant,Volcarona,Genesect]
        else:
            mons=[Rabsca,Ironmoth,Spidops,Lokix,Slitherwing,Wormadam,Mothim,TWormadam,SWormadam,Kricketune,Shuckle,Forretress,Ariados,Ledian,Scyther,Venomoth,Parasect,Butterfree,Beedrill,Frosmoth,Kleavor,Centiskorch,Orbeetle,Golisopod,Araquanid,Vikavolt,Volcarona,Durant,Accelgor,Galvantula,Escavalier,Scolipede,Leavanny,Scizor,Heracross,Pinsir,Drapion,Vespiquen,Yanmega,Genesect]        
        #ICE SPECIALISTS
    if trclass in ["Skier","Boarder"]:
        mons=[FrRotom,Arctovish, Arctozolt,Ironbundle,Cryogonal,Baxcalibur,Ironbundle,Glaceon,Delibird,ASandslash,Cetitan,Frosmoth,MrRime,Avalugg,HAvalugg,Aurorus,Beartic,Vanilluxe,GDarmanitan,Weavile,Abomasnow,Walrein,Lapras,Mamoswine,Glalie,Jynx,Cloyster,ANinetales]
        ch=random.randint(1,10)
        if ch==7:
            mons+=[Articuno]
            
    if trclass in ["Breeder"]:
     mons=[Pikachu,Raichu, Wigglytuff, Clefable,Blissey,Sudowoodo,Electivire, Magmortar,Jynx, Charizard, Blastoise,Venusaur]
     
#ROCK SPECIALISTS
    if trclass in ["Hiker","Backpacker"]:
     mons=[Golem,Steelix,Machamp,Dugtrio,Sandslash, Mamoswine, Probopass, Camerupt, Claydol, Sudowoodo, Charizard,Crobat,Bibarel, Bronzong,Rhydon, Rhyperior, Donphan,Clefable, Dudunsparce, Magnezone, Gigalith, Conkeldurr, Excadrill, Aggron,Swoobat, Hippowdon,Crustle, Tyranitar,Lucario,Golurk,Mawile,Torkoal, Relicanth, Krookodile, Diggersby,Stunfisk,Flygon, Magmortar, MDLycanroc, Mudsdale,AGolem, ADugtrio,Archeops,Rampardos,Hariyama, Aerodactyl, Kabutops, Tyrantrum,Omastar]
     #mons=[Glimmora,Garganacl,Ironthorns,Klawf,Sudowoodo,Rhydon,Coalossal,Gigalith,Lunatone,Solrock,Probopass,HArcanine,Runerigus,Cofagrigus,Rhyperior,Aggron,Steelix,Machamp,Tyranitar,Golem, Aerodactyl]
     
#fossil
    if trclass in ["Ruin Maniac","Paleontologist"]:
        mons=[Dracovish,Dracozolt,Tyrantrum,Aurorus,Archeops,Carracosta,Omastar,Kabutops,Armaldo,Cradily,Aerodactyl,Mamoswine,Bastiodon,Rampardos,Relicanth, Sandslash,Probopass,Claydol, Golem,Steelix,Machamp,Marowak, Bronzong, Relicanth]
        
#Ground
    if trclass in ["Desert Explorer","Egyptian"]:
        if trclass=="Egyptian":
            namelist=["Wongani","Abdelhamid","Ali","Zafar","Saif","Hakeem","Ziyad","Hamed","Daud","Apis","Amon","Aton"]
            nn=random.choice(namelist)
            new_name=trclass+" "+nn
        mons=[Clodsire,Toedscruel,Sandyshocks,Greattusk,Cacturne,Donphan,Quagsire,Rhydon,Marowak,Dugtrio,ADugtrio,Sandslash,Sandaconda,Palossand,Mudsdale,Mandibuzz,Golurk,Drapion,Camerupt,Hippowdon,Nidoking,Nidoqueen,Golem,Gliscor,Steelix,Rhyperior,Mamoswine,Swampert,Flygon,Whiscash,Claydol,Torkoal,Torterra,EGastrodon,WGastrodon,Garchomp,Seismitoad,Krookodile,Excadrill,Arbok]
        
        #WATER SPECIALISTS
    if trclass in ["Marine Biologist","Surfer","Scuba Diver","Swimmer","Sailor","Captain","Pirate","Fisherman","Tuber"]:
        mons=[Tatsugiri,Simisage,Dondozo,Palafin,Wugtrio,Quaquaval,Ironbundle,Lumineon,Floatzel,Bibarel,Mantine,Corsola,Slowking,Quagsire,Seaking,Kingler,Dracovish,Barraskewda,Inteleon,Araquanid,Toxapex,SWishiwashi,Primarina,Clawitzer,Barbaracle,Greninja,Jellicent,Swanna,Carracosta,Basculegion,Seismitoad,HSamurott,Samurott,Phione,EGastrodon,WGastrodon,Empoleon,Walrein,Huntail,Gorebyss,Relicanth,Milotic,Crawdaunt,Whiscash,Dewgong,Sharpedo,Pelipper,Kingdra,Politoed,Azumarill,Feraligatr,Lanturn,Lapras,Gyarados,Slowbro,Cloyster,Starmie, Blastoise,Poliwrath,Swampert,Ludicolo]+random.choices([Manaphy, Wailord],k=1)
        
#GRUNTS
    if trclass in ["Flare Grunt"]:
        mons=[]
        
    if trclass in ["Shadow Triads"]:
        mons=[Absol, Kingambit, Bisharp,Banette,Accelgor,HLilligant,Volcarona, Basculegion]
        
    if trclass in ["Plasma Grunt"]:
        mons=[Watchog,Liepard,Krookodile, Scrafty, Garbodor,Crobat,Seviper,Weezing,Raticate,Drapion, Kingambit, Hydreigon,Weavile,Bisharp, Scolipede, Amoongus,Magnezone,Muk,Zangoose, Genesect,Metagross, Gigalith,Mandibuzz,Seismitoad]
        
    if trclass in ["Aqua Grunt"]:
        mons=[Crawdaunt,Sharpedo,Crobat,Mightyena,Muk,Weezing,Tentacruel,Wailord,Walrein,Dusclops, Ludicolo,Seviper]
        
    if trclass in ["Magma Grunt"]:
        mons=[Camerupt,Torkoal,Crobat,Mightyena,Muk,Weezing,Magmortar,Claydol,Houndoom,Magcargo,Sandslash, Salamence,Banette,Aggron, Zangoose]
        
    if trclass in ["Rocket Grunt"]:
        mons=[Arbok,Weezing,Victreebel,Muk,Crobat,Seviper,Houndoom,Yanmega, Machamp,Raticate,Sandslash,Persian,Hypno,Marowak, Vileplume,Electrode,Gengar,Magnezone, Rhyperior, Skarmory,Tauros,Golem,Rhydon,Dodrio,Purugly,Toxicroak,Skuntank,Mawile,Charizard,Blastoise, Venusaur]
        
    if trclass in ["Galactic Grunt"]:
        mons=[Purugly,Skuntank,Weavile,Bronzong,Crobat,Toxicroak,Muk,Weezing,Magnezone,Electivire,Magmortar,Rhyperior,Probopass,Gyarados,Sableye]
        
#DRAGON SPECIALISTS
    if trclass in ["Dragon Tamer"]:
        mons=[Cyclizar,Baxcalibur,Roaringmoon,Dragapult,Duraludon,Dracovish,Dracozolt,Flapple,Appletun,Kommo,Drampa,Turtonator,Noivern,HGoodra,Goodra,Hydreigon,Druddigon,Haxorus,Krookodile,Serperior,Yanmega,Garchomp,Gyarados,Dragonite,Kingdra,Charizard,Aerodactyl,Tyranitar, Salamence,Feraligatr]+random.choices([Latias,Latios],k=1)
        
    if trclass in ["Police Officer","Investigator","Policeman"]:
        mons=[Noctowl,Machamp,Medicham, Arcanine, HArcanine, Stoutland, Mienshao, Lucario,Boltund,Ariados, Bastiodon, Blastoise]
        
#POISON SPECIALISTS
    if trclass in ["Venom Expert"]:
        mons=[Revavroom,Clodsire,Ironmoth,Grafaiai,Garbodor,Dustox,Swalot,Venomoth,Vileplume,Toxtricity,GSlowking,GWeezing,GSlowbro,Salazzle,Sneasler,Dragalge,Toxicroak,Drapion,Roserade,Seviper,Arbok,Weezing,Crobat,Venusaur,Nidoking,Nidoqueen,Victreebel,Tentacruel,Muk,Gengar,Overqwil]
        
#ELECTRIC
    if trclass in ["Rocker","Guitarist","Electrician","Musician"]:
        mons=[Pincurchin,Boltund,Pawmot,Kilowattrel,Ironthorns,Ironhands,Sandyshocks,Bellibolt,Pachirisu,Manectric,Electrode,Raichu,ARaichu,Pikachu,Dracozolt,Toxtricity,Vikavolt,HElectrode,Eelektross,Galvantula,AGolem,Magnezone,Jolteon,Electivire,Lanturn,Ampharos,Luxray,WRotom,Zebstrika]    
            
#FIRE SPECIALISTS
    if trclass in ["Kindler","Fire Breather","Volcano Explorer"]:
        mons=[Simisear,Scovillain,Skeledirge,Ironmoth,Ceruledge,Armarouge,Magcargo,AMarowak,Centiskorch,Coalossal,Cinderace,Turtonator,Salazzle,Incineroar,Pyroar,Talonflame,Delphox,Volcarona,Heatmor,Chandelure,Darmanitan,HTyphlosion,Emboar,HArcanine,Magmortar,Infernape,Arcanine,Rapidash,Houndoom,Flareon,Typhlosion,Blaziken,Camerupt,Charizard]
        
#FLYING SPECIALISTS
    if trclass in ["Bird Keeper","Pilot","Sky Diver"]:
        mons=[Flamigo,Kilowattrel,Bombirdier,Ironjugulis,Xatu,Noctowl,Corviknight,Toucannon,Hawlucha,Talonflame,Mandibuzz,HBraviary,Braviary,Swanna,Archeops,Unfezant,Gliscor,Togekiss,Honchkrow,Staraptor,Pelipper,Swellow,Charizard,Skarmory,Altaria,Crobat,Dodrio, Salamence,Flygon]
        mons+=random.choices([Articuno,Zapdos,Moltres,Thundurus,Landorus,Tornadus,Enamorus],k=1)      
        
    if trclass in ["Scientist","Super Nerd","Doctor","Poké Maniac"]:
        mons=[Electrode,Magnezone,Metagross,Klinklang, Alakazam, Revavroom,Irontreads,Electivire,WRotom,Ironhands, Ironthorns,Ironvaliant,Ironbundle, Ironjugulis,Ironmoth,FRotom,HRotom,FrRotom,MRotom,PorygonZ,Porygon2,Muk, Weezing, Ninetales,Rapidash,Arcanine,Kingdra,Jolteon,Torkoal,Slowbro, Magcargo, Camerupt, Magmortar]
    if trclass=="Worker":
        mons=[Golem, Steelix, Rapidash,Machamp, Magmortar, Magnezone,Swoobat,Swanna, Excadrill, Unfezant, Krookodile, Conkeldurr,Simisage, Seismitoad, Simipour,Simisear, Gigalith, Walrein,Glalie, Vanilluxe,Mawile, Sigilyph, Dugtrio, Weezing, Watchog,Electivire, Sableye,Stoutland,Claydol,Lucario, Abomasnow, Nidoking,Rhydon,Jynx,Beartic, Octillery, Probopass, ADugtrio, Mudsdale, Bastiodon,Relicanth,Archeops, Coalossal, Maushold,Luxray,Hypno, Stonjourner, Eelektross,Raichu,Electrode, Magnezone, Revavroom,WRotom, HRotom, MRotom, FRotom, FrRotom,]
        #DECENT TRAINERS
    if trclass in ["Expert","Veteran","Businessman","Gentleman","Veteran","Count","Duke","Earl","Teacher","Butler"]:
        mons=[Audino,Dudunsparce,Noctowl,Furret,Ditto,Chansey,Persian,Vileplume,Wigglytuff,Clefable,Pikachu,Raticate,ARaticate,Butterfree,Beedrill,MDLycanroc,MNLycanroc,DLycanroc,Aegislash,Delphox,Greninja,Chesnaught,Basculegion,Stoutland,Probopass,Ursaluna,Yanmega,Magnezone,Tangrowth,Hippowdon,Lucario,Mismagius,Luxray,Roserade,Torterra,Glalie,Absol,Banette,Milotic,Armaldo,Cradily,Aggron,Hariyama,Breloom,Gardevoir,Swellow,Ludicolo,Swampert,Houndoom,Heracross,Steelix,Espeon,Ampharos,Flareon,Jolteon,Vaporeon,Snorlax,Lapras,Gyarados,Tauros,Kangaskhan,Hitmonchan,Hitmonlee,Exeggutor,Gengar,Dodrio,Slowbro,Rapidash,AGolem,Victreebel,Machamp,Golduck,Alakazam,Pidgeot,Blastoise,Ninetales,Primeape,Venusaur,Charizard,Cloyster]
        ch=random.randint(1,15)
        if ch==7:
            mons+=random.choices(legendary,k=1)
        pass
    if trclass in[ "Chaos Trainer"]:
        mons=[Gremlid,Gorochu,Salobber,Terryena,Malevorus, TMalevorus,Medicrow,Cochungus,Bustoliv,Bombeedel, Mollonce, Machug, Doncrete,Dangal, Ajjimajji, Spinestial, Plumageist, Verminlord,Terraterra, Skyshrike, Venomspire, Cephalomight, Ignisunico,Trioclaw, Glaciapod, Sludgeon,Gemshell]
        
    if trclass in[ "Beauty","Lass","Battle Girl","Nurse","Crush Girl","Aroma Lady","Countess","Parasol Lady"]:
        namelist=["Alexa","Andrea","Georgia","Emma","Rose","Kimmy","Layla","Stephanie","Alexandra","Kylie","Anette","Brianna","Cindy","Colleen","Daphne","Elizabeth","Naomi","Sarah","Charlotte","Gillian","Jacki","Selphy","Melissa","Celeste","Elizendra","Isabella","Magnolia","Lynette","Colette","Lina","Dulcie","Auro","Brin","Eloos","Caril","Kowly","Illa","Rima","Ristin","Vesey","Brenna","Deasy","Denslon","Kylet","Nemi","Rene","Sanol"]
        new_name=trclass+" "+random.choice(namelist)
        if trclass in [ "Beauty","Lass","Aroma Lady","Countess","Parasol Lady"]:
            mons=[Wigglytuff,Blissey,Swanna,Sylveon,Whimsicott, Alcremie,Slurpuff,Tsareena,Azumarill,GRapidash, Vileplume,Vaporeon,Cloyster, Bellossom, Seaking,Starmie,Clefable,Togekiss, Gardevoir,Mawile,Altaria,Florges,Klefki,Primarina, Hatterene,Dachsbun,Screamtail,Fluttermane,Tinkaton]
        if trclass in ["Battle Girl","Crush Girl"]:
            mons=[Sawk,Throh,PTauros,Flamigo,Slitherwing,Annihilape,Quaquaval,Ironvaliant,Ironhands,Greattusk,Hitmontop,DUrshifu,WUrshifu,Sirfetchd,Grapploct,Sneasler,HDecidueye,Hawlucha,Pangoro,Chesnaught,Mienshao,Scrafty,HLilligant,Conkeldurr,Emboar,Gallade,Machamp,Poliwrath,Hitmonchan,Hitmonlee,Infernape,Blaziken,Breloom,Primeape,Heracross,Hariyama]
        if trclass in ["Nurse"]:
            mons=[Audino,Chansey,Blissey,Alomomola, Gothitelle,Musharna, Leavanny,Clefable, Wigglytuff,Hatterene,Aromatisse]
            
#THUGS
    if trclass in[ "Street Punk","Biker","Cueball","Smuggler","Thief","Goon","Driver","Burglar","Gambler"]:
        namelist=["Charles","Dwayne","Glenn","Harris","Joel","Riley","Zeke","Alex","Billy","Ernest","Gerald","Hideo","Isaac","Jared","Jaren","Jaxon","Jordy","Lao","Lucas","Nikolas","Ricardo","Ruben","Virgil","William","Aiden","Charles","Dale","Dan","Markey","Reese","Teddy","Theron","Jeremy","Morgann","Philip","Stanley","Dillon"]
        
        if trclass =="Street Punk":
            namelist=["Faust","Jacques","Sid","Slater","Adam","Alex","Earnest","Felix","Gerald","Harvey","Hideo","Jared","Lao","Malik"]
            mons=[Gengar,Skuntank, Crawdaunt, Scrafty,Sharpedo,Bisharp, Dudunsparce,Kingambit,Bisharp,Pangoro,Arbok,Primeape, Annihilape,Muk, Weezing, Magmortar, Raticate,Fearow,Steelix,Rhydon, Rhyperior,Liepard,Seviper, Krookodile,APersian, Honchkrow,Ariados]
        if trclass=="Biker":
            mons=[Weezing,Muk,Electrode, Charizard, Magmortar,Flareon,Hypno, Tentacruel,Swalot, Azumarill, Ursaring, Ursaluna,Drapion,Toxicroak, Galvantula, Scrafty, Krookodile, Bouffalant, Bisharp, Kingambit, Conkeldurr]
        else:
            mons=[Weezing,Muk, Electrode,Charizard, Flareon, Magmortar,Togekiss, Forretress, Hypno, Tentacruel,Swalot, Ursaring, Drapion,Arbok,Seviper, Toxicroak, Galvantula, Scrafty, Krookodile, Bouffalant, Bisharp, Kingambit, Crobat,Conkeldurr, Nidoking, Nidoqueen, Hitmonlee, Machamp, Primeape, Hitmonchan, Venomoth, Poliwrath, Annihilape, Beedrill,Kingdra, Kangaskhan, Kabutops,Jynx,Ariados, Dudunsparce, Ampharos, Skarmory, Cloyster, Venusaur, Rhydon, Victreebel, Skarmory, Miltank, Vaporeon, Parasect,Steelix]
        nn=random.choice(namelist)
        new_name=trclass+" "+nn
    

    if trclass == "Air Force Officer":
        mons=[Skarmory,Corviknight,Magnezone,Latios,Latias,Pidgeot,Staraptor,Braviary,Altaria,Dragonite,Salamence,Metagross]
        
    if trclass == "Navy Officer":
        mons=[Gyarados,Blastoise,Swampert,Feraligatr,Inteleon,Wailord,Starmie]
        
    if trclass == "Military Officer":
        mons=[Aggron,Salamence,Tyranitar,Steelix,Rhyperior,Magnezone,Metagross,Dragonite,Magmortar,Electivire,Charizard, Blastoise]
        
    if trclass == "Tamer":
        mons=[Annihilape,Ursaring,Granbull,GRapidash,Bewear,MDLycanroc,MNLycanroc,DLycanroc,Wyrdeer,Pangoro,Braviary,Tauros,Arbok,Arcanine,HArcanine,Rapidash,Ambipom,Ursaluna,Mamoswine,Houndoom,Mightyena,Slaking,Sharpedo,Wailord,Zangoose,Seviper,Milotic,Absol,Walrein,Empoleon,Infernape,Luxray]+random.choices([Raikou,Suicune,Entei,Cobalion,Virizion,Terrakion])

                        
     #BETTER TRAINERS
    if trclass in ["Ace Trainer","Cool Trainer","Coach Trainer"]:
        mons=[Victreebel,Vileplume, Venusaur, Nidoking,Sandslash,Dugtrio,Rhydon,Rhyperior, Persian, Ninetales, Blastoise, Charizard, Exeggutor, Cloyster,Parasect,Dewgong,Chansey,Kingler,Tentacruel,Rapidash,Magnezone, Quagsire,Electrode,Starmie, Kingdra,Butterfree, Bellossom, Poliwrath,Politoed,Flareon, Vaporeon,Jolteon,Seaking,Golduck,Pikachu, Azumarill, Jumpluff, Dragonite, Nidoqueen, Pidgeot,Electivire, Tangrowth,Tauros,PTauros,ADugtrio,Manectric, Muk, Zangoose, Pelipper, Camerupt,Roserade,Mawile,Sableye,Swellow,Flygon,Wailord,Shiftry,Cacturne,Aggron,Linoone, Milotic, Delcatty,Probopass,Medicham,Ludicolo,Kecleon,Golem,AGolem,Exploud, Alakazam,Dodrio,Claydol,Sharpedo,Magcargo,Hariyama, Wigglytuff, Miltank,Snorlax, Ursaring,Ursaluna, Dusclops, Dusknoir, Banette,Vigoroth,Slaking,Skarmory,Spinda,Lanturn,Absol,Tropius, Gardevoir,Solrock,Lunatone,Machamp, Tyranitar,Lapras,Arcanine,Slowbro,HArcanine, Kangaskhan, Farigiraf,Steelix,Marowak,AMarowak, Raticate, ARaticate , Aerodactyl,Weavile,Gengar,Torterra, Abomasnow,Ambipom,Raichu, EGastrodon, WGastrodon, Pachirisu, Sudowoodo, Drifblim, Lopunny, Drapion, Hippowdon,Mightyena, Ampharos,Infernape, Gyarados,Luxray,Mothim, Salamence, MrMime,MrRime,Honchkrow, Staraptor, Metagross, Metagross,Floatzel,Primeape,Annihilape,Torkoal,Purugly,Glameow,Bibarel,Beautifly,Yanmega, Meowth,Hypno,Dudunsparce, Scyther, Scizor,Carnivine, Rampardos,Pinsir, Lickilicky,Granbull,Crobat,Glalie,Porygon2, PorygonZ, Beedrill,Magmortar,Gliscor, Hitmonchan, Mamoswine, Slowking,GSlowking, GSlowbro,Excadrill, Zebstrika,Swoobat,Stoutland,Furret,Garchomp,Grumpig, Vanilluxe, Gothitelle, Reuniclus, Galvantula, Simisear, Simisage, Simipour, Sawsbuck, Jellicent, Haxorus, Whimsicott,Carracosta, Hydreigon, Druddigon, Scolipede,Mienshao, Beheeyem, Bisharp,Kingambit,Liepard,Watchog, Alomomola, Klinklang, Darmanitan, GDarmanitan, Beartic, Leavanny,Archeops,Accelgor, Eelektross, Krookodile,Seismitoad,Walrein,Gallade,Ironvaliant,Jynx,HRotom,WRotom,MRotom,FRotom,FrRotom,Lilligant,Swanna,Chandelure,Unfezant,Sigilyph,Golurk,Heatmor,Umbreon,Mantine, Basculegion,Emolga, Cofagrigus, Vaporeon,Espeon, Durant, Ferrothorn, Lucario, Weezing , Bronzong, Aegislash,Crustle, Delibird,Seviper, Fearow,ANinetales,Toxapex,Garbodor,MDLycanroc, MNLycanroc,DLycanroc,Kommo,Sylveon,Gorebyss,Lurantis,AMuk, Dragalge, Talonflame, HLilligant, Braviary,Huntail, Noivern,Shiinotic, ASandslash]
            
        
#CHALLENGERS
    if trclass == "Challenger":
        mons=[Amoongus, Azumarill, Breloom,Ceruledge,Cinderace,Clodsire, Corviknight,Dondozo, Dragapult, Dragonite, Garchomp, Garganacl, Gholdengo,Glimmora,Greattusk, Greninja,Grimmsnarl, Hatterene,Ironmoth,Irontreads,Ironvaliant, Kingambit, Meowscarada,Orthworm,Pelipper,Quaquaval,Roaringmoon,WRotom,Scizor,Skeledirge,Tinglu,Toxapex, Volcarona, Alomomola, Arcanine, Avalugg, Barraskewda,Baxcalibur,Blissey, Brutebonnet,Cetitan,Chansey, Charizard, Cloyster,Ditto, Floatzel,Gallade,Gengar, Gyarados, Hawlucha,Haxorus,Hippowdon, Hydreigon,Indeedee,Ironhands,Ironjugulis,Ironthorns,Kilowattrel,Klefki,Lokix, Magnezone, Masquerain,Maushold,Mimikyu,Pawmot,Pincurchin, Polteageist,Rabsca,HRotom, Salamence,Sandyshocks, Scovillain,Screamtail,Slitherwing,Slowbro, Slowking, Sylveon, Talonflame,PTauros, Torkoal, Tyranitar, Umbreon]
        
        
    if trname is None and new_name==None:
        namelist=["Josh","Kyler","Jade","John","Joey","Jan","Gabriel","Jamie","Kylie","Andrea","Evy","Ebba","Titus","Emiliano","Emilia","Natalie","Justin","Anastasia","Frannie","Danielle","Daniel","Hugo","Robert","Carlos","Alex","Alexander","Alexandra","Arslan","Johan","Mike","Julian","Selena","Emmanuel","Kristin","Lawrence","Frank","Pamela","Nicole","Emma","Matthew","Catherine","Jackson","Jenna","Sebastian","Sophia","Gav","Lorenzo","Merdith","Nora","Beth","Chelsea","Katelyn","Logan","Madelin","Nicolas","Trenton","Allison","Ashlee","Deshawn","Dwayne","Felicia","Jeffery","Krista","Taylor","Annie","Audra","Brenda","Claude","Chloris","Crofton","Eliza","Harry","Irene","Jaden","Keith","Lewis","Mary","Miguel","Mylene","Pedro","Ralph","Richard","Shanti","Thalia","Anja","Bret","Briana","Daryl","Dianna","Eddie","Elie","Elaine","Forrest","Heidl","Hillary","Johan","Sophie","Lena","Lois","Malory","Maxwell","Melita","Mikiko","Naoko","Parker","Rick","Serenity","Steve","Ambre","Bjorn","Brooke","Chaise","Lee","Dean","Clementine","Maurice","Melina","Nash","Petra","Reed","Ralf","Shinobu","Silas","Twiggy","Kira","Dirk","Bobby","Danny","Caleb","Dylan","Thomas","Daniel","Jeff","Braven","Dell","Neagle","Haruki","Mitchell","Sheriff","Raymond","Cole","Edgar","Evan","Jason","Phil","Vincent","Yoshinari","Georges","Morris","Jacopo","Anette","Brianna","Cindy","Colleen","Daphne","Elizabeth","Naomi","Sarah","Charlotte","Gillian","Jacki","Selphy","Melissa","Celeste","Elizendra","Isabella","Magnolia","Lynette","Colette","Lina","Dulcie","Auro","Brin","Eloos","Caril","Kowly","Illa","Rima","Ristin","Vesey","Brenna","Deasy","Denslon","Kylet","Nemi","Rene","Sanol","Sturk","Talmen","Zolla","Caroline","Allyson","Albert","Alexa","Kathleen","Leroy","Rolando","Warren","Yuji","Alicia","Alyssa","Anton","Blake","Brandi","Breanna","Cesar","Deanna","Dana","Dennis","Destiny","Felix","Garrett","Graham","Isaiah","Jake","Jamie","Jasmin","Jonah","Jose","Keenan","Mariah","Maya","Micah","Monique","Natasha","Meagan","Quinn","Rodolfo","Ruben","Sandra","Savannah","Sergio","Shannon","Skylar","Stefan","Zachery","Sydney","Allen","Alton","Arabella","Bonita","Brian","Cal","Carol","Cody","Cybil","Fran","French","Gaven","Joyce","Kelly","Kobe","Lola","Megan","Paulo","Piper","Reena","Shaye","Salma","Austin","Becklett","Brevely","Corky","David","Glinda","Henry","Webstar"]    
        nn=random.choice(namelist)
        new_name=trclass+" "+nn        
        
        
        
    if len(team)==0 and trclass=="Challenger":
        while len(team)!=pknum:
#            print(f"⚠️{trclass} cdi")
            party=random.choices(mons)[0]
            member=party( )
            if (member.item not in megastones and "(" not in member.name and "Totem " not in member.name) and len(team)<4:
                team.append(member)
                mons.remove(party)
            if "Z-Crystal" in member.name and len(team)==4:
                team.append(member)
                mons.remove(party)
            if member.item in megastones and len(team)==5:
                team.append(member)
                mons.remove(party)
                
    if len(team)==0 and trclass in ["Pokémon Trainer"]:
        megachance=0
        if "Alola" in trclass or "Alola" in field.location:
            megachance=1
        if "Kalos" in trclass or "Kalos" in  field.location:
            megachance=2
        if megachance==0:
            megachance=random.randint(1,2) 
        while len(team)!=pknum:
#            print(f"⚠️{trclass} SEXxxx")
            party=random.choices(mons)[0]
            member=party( )
            if (member.item not in megastones and "(" not in member.name) and len(team)<5:
                team.append(member)
                mons.remove(party)
            if megachance==1:
                if "Z-Crystal" in member.name and len(team)==5:
                    team.append(member)
                    mons.remove(party)         
            if megachance==2:
                if member.item in megastones and len(team)==5:
                    team.append(member)
                    mons.remove(party)        
        
            
                
    if len(team)==0 and trclass in ["Ace Trainer","Dragon Tamer"]:
        while len(team)!=pknum:
#            print(f"⚠️{trclass} nigga")
            party=random.choices(mons)[0]
            member=party( )
            if (member.item not in megastones and "(" not in member.name and "Totem " not in member.name) and len(team)<4:
                team.append(member)
                mons.remove(party)
            if "Z-Crystal" in member.name and len(team)==4:
                team.append(member)
                mons.remove(party)
            if member.item in megastones and len(team)==5:
                team.append(member)
                mons.remove(party)                  
    if len(team)==0 and trclass in ["Competitive Player"]:    
        while len(team)!=pknum:
            party=random.choices(mons)[0]
            c="OU-"+random.choice(["Rock","Fire","Water","Grass","Electric","Ground","Flying","Fighting","Fairy","Dragon","Steel","Poison","Dark","Ghost","Normal","Bug","Ice"])
            member=party(maxiv=c)
            if member.item not in megastones and "(" not in member.name and len(team)<6:
                team.append(member)
                mons.remove(party)
    if len(team)==0 and trclass in ["Fusion Trainer"]:             
        while len(team)!=pknum:
#            print(f"⚠️{trclass} ERROR!!!!")
            p1=random.choices(mons)[0]
            p2=random.choices(mons)[0]
            member=fuse(p1,p2)
            if member.item not in megastones and "m-Z" not in member.item and len(team)<6:
                team.append(member)
               
    else:
        while len(team)!=pknum:
#            print(f"⚠️{trclass} ERROR!!!!")
            party=random.choices(mons)[0]
            member=party( )
            if member.item not in megastones and "(" not in member.name and len(team)<5:
                team.append(member)
                mons.remove(party)
            if "Z-Crystal" in member.name and len(team)==5:
                    team.append(member)
                    mons.remove(party) 
            if member.item in megastones and len(team)==5:
                    team.append(member)
                    mons.remove(party)  

                                                                                
                     
    return new_name,team            

def genTrainer(trclass=None,name=None,num=6,ai=True):
    trclasslist=allclass
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
bruno1=Steelix(maxiv="Yes",move=["Earthquake","Iron Head", "Curse","Gyro Ball"],nature="Brave",item="Steelixite")
bruno2=Machamp(maxiv="Yes",move=["Bullet Punch","Dynamic Punch","Stone Edge","Earthquake"],nature="Adamant", ability="No Guard")
bruno3=Hitmonchan(maxiv="Yes",move=["Thunder Punch","Close Combat","Fire Punch","Ice Punch"],nature="Adamant", ability="Iron Fist")
bruno4=Hitmonlee(maxiv="Yes",move=["High Jump Kick","Knock Off","Poison Jab","Stone Edge"],nature="Adamant", ability="Reckless")
bruno6=Poliwrath(name="Poliwrath",maxiv="Fighting",move=["Close Combat","Liquidation","Body Slam","Surging Strikes"],nature="Adamant")
bruno7=Hitmontop(maxiv="Yes",move=["Earthquake","Close Combat","Counter","Quick Attack"])
bruno8=Hariyama(maxiv="Yes",item="Sitrus Berry",move=["Bulk Up","Low Kick","Bullet Punch","Knock Off"])
bruno9=Lucario(maxiv="Yes", ability="Inner Focus",move=["Close Combat","Counter","Extreme Speed","Iron Tail"])
bruno10=AGolem(maxiv="Yes",move=["Thunder Punch","Rock Slide","Superpower","Earthquake"])
brunoteam=teamset([bruno6,bruno1,bruno3,bruno4,bruno7,bruno8,bruno9,bruno10],5)+[bruno2]
bruno=Trainer("Elite Four Bruno",brunoteam,"Kanto")
#E4 Lance
lance1=Hydreigon(maxiv="Yes",move=["Dark Pulse","Fire Blast","Earth Power","Draco Meteor"],nature="Modest",item="White Herb")
lance2=Gyarados(name="Gyarados✨",maxiv="max",move=["Dragon Dance","Waterfall","Earthquake","Ice Fang"],nature="Adamant")
lance3=Aerodactyl(maxiv="Yes",move=["Stone Edge","Earthquake","Roost","Stealth Rock"],nature="Jolly")
lance4=Dragonite (maxiv="max",move=["Dragon Dance","Extreme Speed","Dragon Claw","Roost"],nature="Adamant",item="Focus Sash")
lance5=Kingdra(maxiv="Yes",move=["Flash Cannon","Dragon Pulse","Surf","Ice Beam"],nature="Modest",item="Scope Lens")
lance6=Charizard(maxiv="Yes",move=["Dragon Dance","Thunder Punch","Dragon Claw","Flare Blitz"],nature="Adamant",item="Charizardite X",atkev=252,spatkev=0)
lance7=Haxorus(maxiv="Yes",item="Choice Scarf",move=["Outrage","Superpower","Earthquake","Rock Slide"], ability="Mold Breaker")
lance8=AExeggutor(maxiv="Yes",move=["Giga Drain","Psychic","Dragon Pulse","Hyper Voice"],atkev=0,spatkev=252)
lance9=Salamence (maxiv="Yes",item="Expert Belt",move=["Dragon Claw","Crunch","Earthquake","Stone Edge"], ability="Intimidate")
lance10=Flygon (maxiv="Yes",item="Power Herb",move=["Solar Beam","Draco Meteor","Earth Power","U-turn"],spatkev=252,atkev=0, ability="Levitate")
lance11=Lapras(maxiv="Yes")
lance12=Altaria(maxiv="Yes", ability="Natural Cure",move=["Double Team","Perish Song","Hyper Beam","Dragon Pulse"])
lance13=Garchomp(maxiv="Yes", ability="Sand Veil",move=["Outrage","Swords Dance","Roar","Earthquake"])
lance14=Tyranitar(maxiv="Yes",move=["Crunch","Rock Slide","Earthquake","Hyper Beam"],item="Quick Claw")
lanceteam=teamset([lance1,lance2,lance3,lance6,lance5,lance7,lance8,lance9,lance10,lance11,lance12,lance13,lance14],5)+[lance4]
lance=Trainer("Elite Four Lance",lanceteam,"Johto")
#E4 Lorelei 
lorelei1=Lapras(maxiv="Yes",move=["Blizzard","Hydro Pump","Dragon Pulse","Thunder"],nature="Modest")
lorelei2=Slowbro(maxiv="Yes",move=["Yawn","Flamethrower","Surf","Psychic"],nature="Modest",item="Slowbronite")
lorelei3=Dewgong(maxiv="Yes",move=["Aqua Jet","Waterfall","Ice Shard","Iron Tail"],nature="Adamant",spatkev=0,atkev=252)
lorelei4=Cloyster(maxiv="Yes",move=["Rock Blast","Pin Missile","Icicle Spear","Shell Smash"],nature="Adamant",item="Focus Sash", ability="Skill Link")
lorelei5=Jynx(maxiv="Yes",move=["Ice Beam","Psychic","Recover","Blizzard"],nature="Timid")
lorelei6=Mamoswine(name="Mamoswine(Z-Crystal)",maxiv="Yes",move=["Ice Beam","Earthquake","Stone Edge","Blizzard"],nature="Naughty")
lorelei7=ASandslash(maxiv="Yes",move=["Ice Punch","Earthquake","Iron Tail","Ice Shard"])
loreleiteam=teamset([lorelei6,lorelei2,lorelei3, lorelei4,lorelei5,lorelei7],5)+[lorelei1]
lorelei=Trainer("Elite Four Lorelei",loreleiteam,"Kanto")
#Red
red7=Pikachu(name=random.choice(["Pikachu(Z-Crystal)","Pikachu"]),maxiv="Yes",move=["Extreme Speed","Iron Tail",random.choice(["Thunderbolt","Volt Tackle"]),"Electroweb"],nature="Modest")
red1=Charizard(maxiv="Yes",move=["Dragon Dance","Dragon Claw","Flare Blitz","Roost"],nature="Jolly",item="Charizardite X",atkev=252,spatkev=0)
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
red=Trainer(random.choice(["Pokémon Trainer","Battle Legend","Kanto Champion"])+" Red",redteam,"Kanto")
#E4 Agatha
agatha1=Crobat(maxiv="Yes",move=["Roost","Toxic","Brave Bird","U-turn"],nature="Jolly")
agatha2=Mismagius(maxiv="Yes",move=["Thunderbolt","Dazzling Gleam","Shadow Ball","Nasty Plot"],nature="Timid")
agatha3=Arbok(maxiv="Yes",move=["Earthquake","Poison Jab","Crunch","Coil"], nature="Adamant")
agatha4=Weezing(maxiv="Yes",move=["Sludge Bomb","Will-O-Wisp","Flamethrower","Toxic"],nature="Bold")
agatha5=Gengar(maxiv="Yes",move=["Thunderbolt","Sludge Bomb","Shadow Ball","Nasty Plot"],nature="Timid")
agatha6=Gengar(maxiv="Yes",move=["Thunderbolt","Sludge Bomb","Shadow Ball","Nasty Plot"],nature="Timid",item="Gengarite")
agatha7=AMarowak(maxiv="Yes")
agathateam=teamset([agatha1,agatha2,agatha3,agatha4,agatha5,agatha7],5)+[agatha6]
agatha=Trainer("Elite Four Agatha", agathateam,"Kanto")
#alsada
alsada1=Screamtail(maxiv="Yes")
alsada2=Slitherwing(maxiv="Yes")
alsada6=Roaringmoon(maxiv="Yes")
alsada4=Fluttermane(maxiv="Yes")
alsada5=Sandyshocks(maxiv="Yes")
alsada3=Greattusk(maxiv="Yes")
alsada7=Brutebonnet(maxiv="Yes")
alsada9=Koraidon(name="Koraidon",maxiv=random.choice(["Fighting","Dragon"]),item="Heat Rock",move=["Giga Impact","Bulk Up","Flare Blitz","Collision Course"])
alsadateam=teamset ([alsada1,alsada2,alsada3,alsada4,alsada5,alsada6,alsada7],5)+[alsada9]
alsada=Trainer("Professor Sada",alsadateam,"Paldea")
#alturo
alturo1=Ironhands(maxiv="Yes")
alturo2=Ironmoth(maxiv="Yes")
alturo6=Ironthorns(maxiv="Yes")
alturo4=Ironbundle(maxiv="Yes")
alturo5=Ironjugulis(maxiv="Yes")
alturo3=Irontreads(maxiv="Yes")
alturo9=Miraidon(name="Miraidon",maxiv=random.choice(["Electric","Dragon"]))
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
#tonoy
tonoy1=Umbreon(maxiv="Yes",item="Leftovers", ability="Inner Focus",move=["Wish","Protect","Foul Play","Toxic"],nature="Careful")
tonoy2=Conkeldurr(maxiv="Yes",item="Flame Orb",nature="Adamant", ability="Guts",move=["Mach Punch","Bulk Up","Stone Edge","Drain Punch"])
tonoy3=Venusaur(maxiv="Yes",item="Venusaurite",nature="Modest", ability="Chlorophyll",move=["Earth Power","Sludge Bomb","Sleep Powder","Giga Drain"])
tonoy4=Skarmory (maxiv="Yes",item="Rocky Helmet", ability="Sturdy", nature="Impish", move=["Whirlwind","Roost","Stealth Rock","Brave Bird"])
tonoy5=Scizor(maxiv="Yes",item="Life Orb", ability="Technician", nature="Adamant",move=["Bullet Punch","U-turn","Superpower","Roost"])
tonoy6=Cloyster(maxiv="Yes",item="Focus Sash", ability="Skill Link",nature="Adamant",move=["Ice Shard","Icicle Spear","Rock Blast","Shell Smash"])
tonoyteam=teamset ([tonoy1,tonoy2,tonoy3,tonoy4,tonoy5,tonoy6])
tonoy=Trainer("Developer Crescent",tonoyteam,"Hoenn")
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
goh9=Cinderace(maxiv="Yes")
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
steven1=Claydol(maxiv="Yes",move=["Reflect","Earth Power","Extrasensory","Light Screen"],nature="Bold")
steven2=Armaldo(maxiv="Yes",move=["X-Scissor","Rock Blast","Earthquake","Crush Claw"],nature="Adamant", ability="Battle Armor")
steven3=Cradily (maxiv="Yes",move=["Giga Drain","Sludge Bomb","Strength Sap","Ancient Power"],nature="Modest",item="Expert Belt")
steven4=Skarmory(maxiv="Yes",move=["Brave Bird","Whirlwind","Roost","Stealth Rock"],nature="Impish", item="Rocky Helmet")
steven5=Aggron(maxiv="Yes",move=["Dragon Claw","Iron Tail","Earthquake","Head Smash"],ability="Rock Head",item="Air Balloon",nature="Adamant")
steven6=Metagross(name="Metagross✨",maxiv="Yes", move=["Zen Headbutt","Bullet Punch","Meteor Mash","Hammer Arm"],nature="Adamant",item="Metagrossite")
steven7=Deoxys(maxiv="Yes")
steven8=Excadrill(maxiv="Yes",item="Focus Sash",move=["Earthquake","Rock Slide","X-Scissor","Sandstorm"])
steven9=Aerodactyl(maxiv="Yes", ability="Pressure",move=["Fire Fang","Thunder Fang","Ice Fang","Rock Slide"],item="Focus Sash")
steven10=Archeops(maxiv="Yes",item="Sitrus Berry",move=["Head Smash","Acrobatics","Earthquake","Extreme Speed"])
steven11=Rayquaza(name="Rayquaza✨",maxiv="Yes")
steventeam=teamset([steven1,steven2,steven3,steven4,steven5,steven7,steven8,steven9,steven10,steven11],5)+[steven6]
steven=Trainer("Hoenn Champion Steven", steventeam,"Hoenn")
#Champion Wallace
wallace1=Ludicolo(maxiv="Yes",move=["Energy Ball","Scald","Ice Beam","Fake Out"], ability="Swift Swim",item="Life Orb")
wallace2=Starmie(maxiv="Yes",move=["Psychic","Recover","Surf","Thunderbolt"],nature="Timid",item="Expert Belt")
wallace3=Wailord(maxiv="Yes",move=["Water Spout","Blizzard","Earthquake","Heavy Slam"], ability="Blubber Defense")
wallace4=Gyarados(maxiv="Yes",move=["Ice Fang","Waterfall","Stone Edge","Crunch"],nature="Adamant", ability="Intimidate")
wallace5=Swampert(maxiv="Yes",move=["Earthquake","Liquidation","Ice Punch","Hammer Arm"],nature="Adamant",item="Swampertite")
wallace6=Milotic(maxiv="Yes",move=["Hydro Pump","Recover","Dragon Pulse","Blizzard"],nature="Modest",ability="Marvel Scale",item="Rocky Helmet")
wallace7=Walrein(maxiv="Yes",item="Leftovers",move=["Surf","Yawn","Blizzard","Sheer Cold"])
wallace8=Seaking(maxiv="Yes")
wallace9=Sharpedo(maxiv="Yes",item="Focus Sash",move=["Liquidation","Zen Headbutt","Aqua Jet","Crunch"], ability="Rough Skin")
wallace10=Whiscash(maxiv="Yes", ability="Oblivious",move=["Earthquake","Muddy Water","Rock Tomb","Rain Dance"],item="Damp Rock")
wallace11=Tentacruel(maxiv="Yes", ability="Clear Body",move=["Sludge Wave","Rain Dance","Dazzling Gleam","Scald"])
wallaceteam=teamset([wallace1,wallace2,wallace3,wallace4,wallace5,wallace7,wallace8,wallace9,wallace10,wallace11],5)+[wallace6]
wallace=Trainer("Hoenn Champion Wallace",wallaceteam,"Hoenn")
#Tobias
tobias1=Darkrai(maxiv="Yes",move=["Dark Void","Shadow Ball","Dark Pulse","Psychic"],nature="Modest")
tobias2=Latios(maxiv="Yes",move=["Luster Purge","Dragon Pulse","Calm Mind","Shadow Ball"],nature="Timid")
tobias3=Entei(maxiv="Yes",move=["Lava Plume","Stone Edge","Flare Blitz","Fire Blast"],nature="Hasty")
tobias4=Heatran(maxiv="Yes",move=["Magma Storm","Flash Cannon","Ancient Power","Earth Power"],nature="Calm")
tobias5=Latias(maxiv="Yes",move=["Mist Ball","Dragon Pulse","Calm Mind","Shadow Ball"],nature="Timid")
tobias6=Cresselia(maxiv="Yes",move=["Lunar Blessing","Moonblast","Psychic","Shadow Ball"],nature="Calm")
tobias=Trainer("Pokémon Trainer Tobias",[tobias3,tobias4,tobias5,tobias6,tobias1,tobias2],"Sinnoh")
#Champion Cynthia
cynthia1=WGastrodon(maxiv="Yes",move=["Earthquake","Scald","Sludge Bomb","Rock Tomb"],nature="Calm",item="Leftovers", ability="Storm Drain")
cynthia2=Togekiss(maxiv="max",move=["Air Slash","Thunder Wave","Moonblast","Aura Sphere"],nature="Modest", ability="Serene Grace",item="Leftovers")
cynthia3=Lucario(maxiv="Yes",move=["Close Combat","Meteor Mash","Earthquake","Extreme Speed"],nature="Adamant", ability="Inner Focus")
cynthia4=Milotic(maxiv="Yes",move=["Ice Beam","Mirror Coat","Recover","Scald"],nature="Calm", ability="Marvel Scale",item="Flame Orb")
cynthia5=Roserade(maxiv="Yes",move=["Dazzling Gleam","Shadow Ball","Sludge Bomb","Energy Ball"], nature="Modest",item="Expert Belt")
cynthia6=Garchomp(maxiv="Yes",move=["Dragon Claw","Swords Dance","Poison Jab","Earthquake"],nature="Jolly", item=random.choice(["Yache Berry","Garchompite"]))
cynthia8=Glaceon(maxiv="Yes")
cynthia7=Rayquaza (maxiv="Yes")
cynthia9=Altaria (maxiv="Yes")
cynthia10=Lickilicky (maxiv="Yes")
cynthia14=Kommo(maxiv="Yes")
cynthia13=Giratina (maxiv="Yes")
cynthia11=Spiritomb(maxiv="Yes",move=["Shadow Ball","Sucker Punch","Will-O-Wisp","Dark Pulse"], nature="Modest",item="Sitrus Berry")
cynthia12=PorygonZ(maxiv="Yes",move=["Hyper Beam","Shadow Ball","Ice Beam","Thunderbolt"], nature="Modest",item="Expert Belt")
cynthiateam=teamset([cynthia1,cynthia2,cynthia3,cynthia4,cynthia5,cynthia11, cynthia12,cynthia7, cynthia8,cynthia9,cynthia10,cynthia13,cynthia14],5)+[cynthia6]
cynthia=Trainer("Sinnoh Champion Cynthia", cynthiateam,"Sinnoh")
#E4 Aaron
aaron1=Yanmega(maxiv="Yes",move=["Air Slash","Bug Buzz","Signal Beam","Ancient Power"],nature="Modest",item="Wise Glasses", ability="Speed Boost")
aaron2=Vespiquen(maxiv="Yes",move=["Attack Order","Power Gem","Defend Order","Air Slash"],nature="Modest",item="Sitrus Berry")
aaron3=Scizor(maxiv="Yes",move=["Swords Dance","X-Scissor","Bullet Punch","Night Slash"],nature="Adamant", ability="Technician")
aaron4=Heracross(maxiv="Yes",move=["Earthquake","Close Combat","Rock Slide","Pin Missile"],nature="Adamant",item="Heracronite")
aaron5=Flygon(name="Flygon",maxiv="Bug",move=["Earth Power","Dragon Pulse","Boomburst","Bug Buzz"], nature="Jolly",item="Wise Glasses",atkev=0,spatkev=252)
aaron6=Drapion(maxiv="Yes",move=["Night Slash","Earthquake","X-Scissor","Cross Poison"],nature="Adamant", ability="Sniper",item="Scope Lens")
aaron8=Dustox(maxiv="Yes",item="Black Sludge",move=["Toxic","Bug Buzz","Moonlight","Light Screen"])
aaron9=Beautifly(maxiv="Yes",item="Wise Glasses",move=["Bug Buzz","Shadow Ball","Psychic","Quiver Dance"])
aaronteam=teamset([aaron1,aaron2,aaron3,aaron4,aaron5,aaron8,aaron9],5)+[aaron6]
aaron=Trainer("Elite Four Aaron",aaronteam,"Sinnoh")
#Bertha
bertha1=Golem(maxiv="Yes",item="Soft Sand", move=["Rock Polish","Heavy Slam","Earthquake","Stone Edge"], ability="Sturdy")
bertha2=Hippowdon(maxiv="Yes", ability="Sand Stream",move=["Ice Fang","Earthquake","Body Press","Slack Off"],item="Iapapa Berry")
bertha3=Gliscor(maxiv="Yes", ability="Poison Heal",item="Toxic Orb",move=["Earthquake","Thunder Fang","Guillotine","X-Scissor"])
bertha4=Nidoking (maxiv="Yes",item="Life Orb", ability="Sheer Force",move=["Sludge Bomb","Earth Power","Thunderbolt","Ice Beam"],nature="Modest")
bertha5=Mamoswine(maxiv="Yes",item="Never-Melt Ice",move=["Earthquake","Icicle Spear","Ice Shard","Double-Edge"])
bertha6=Rhyperior(maxiv="Yes",item="Muscle Band", ability="Solid Rock",move=["Rock Slide","Earthquake","Ice Punch","Thunder Punch"])
bertha7=Steelix(maxiv="Yes",item="Steelixite",move=["Gyro Ball","Earthquake","Rock Slide","Thunder Fang"], ability="Sturdy")
bertha8=Quagsire (maxiv="Yes",move=["Recover","Toxic","Earthquake","Surf"], ability="Water Absorb")
bertha9=Whiscash(maxiv="Yes",item="Rindo Berry",move=["Scald","Earthquake","Zen Headbutt","Ice Beam"])
bertha10=Donphan(maxiv="Yes", ability="Sturdy",move=["Earthquake","Ice Shard","Play Rough","Rock Slide"],item="Expert Belt")
bertha11=Sudowoodo (maxiv="Yes",item="Sitrus Berry", ability="Rock Head",move=["Double-Edge","Head Smash","Sucker Punch","Low Kick"])
berthateam= teamset([bertha1,bertha5,bertha3,bertha4,bertha7,bertha6,bertha8,bertha9,bertha10],5)+[bertha2]
bertha=Trainer("Elite Four Bertha",berthateam,"Sinnoh")
#rika
rika1=Camerupt(maxiv="Yes")
rika2=Whiscash(maxiv="Yes")
rika3=Donphan(maxiv="Yes")
rika4=Dugtrio(maxiv="Yes")
rika5=Greattusk(maxiv="Yes")
rika6=Clodsire(name="Clodsire",maxiv="Ground")
rika7=Irontreads(maxiv="Yes")
rikateam=teamset([rika1,rika2,rika3,rika4,rika6],5)+teamset([rika5,rika7],1)
rika=Trainer("Elite Four Rika",rikateam,"Paldea")
#dexio
dexio1=Turtonator (maxiv="Yes")
dexio2=Slowbro (maxiv="Yes")
dexio3=Passimian (maxiv="Yes")
dexio4=Whimsicott (maxiv="Yes")
dexio5=Ninetales (maxiv="Yes")
dexio6=Braviary (maxiv="Yes")
dexio7=Espeon(maxiv="Yes")
dexioteam=teamset([dexio1,dexio2,dexio3,dexio4,dexio6,dexio5,dexio7])
dexio=Trainer("Pokémon Trainer Dexio",dexioteam,"Alola")
#Flint
flint1=Rapidash(maxiv="Yes", ability="Flame Body",move=["Flare Blitz","Hypnosis","Iron Tail","Poison Jab"])
flint2=Entei(maxiv="Yes", ability="Inner Focus",item="Muscle Band",move=["Sacred Fire","Extreme Speed","Bulldoze","Iron Head"])
flint3=Magmortar(maxiv="Yes",ability="Flame Body",item=random.choice(["Lum Berry","Sitrus Berry"]),move=["Fire Blast","Thunderbolt","Focus Blast","Psychic"])
flint4=Houndoom(maxiv="Yes",move=["Flamethrower","Dark Pulse","Nasty Plot","Destiny Bond"])
flint5=Arcanine(maxiv="Yes",ability="Intimidate",item="Shuca Berry",move=["Flare Blitz","Play Rough","Close Combat","Extreme Speed"])
flint6=Infernape(maxiv="Yes", ability="Iron Fist",item="Focus Sash",move=["Thunder Punch","Fire Punch","Close Combat","Mach Punch"])
flint7=Lopunny(maxiv="Yes",item="Leftovers",move=["Mirror Coat","High Jump Kick","Fire Punch","Quick Attack"])
flint8=Drifblim(maxiv="Yes",ability="Unburden",item="Sitrus Berry",move=["Strength Sap","Will-O-Wisp","Shadow Ball","Destiny Bond"])
flint9=Steelix(maxiv="Yes", ability="Sheer Force",item="Life Orb",move=["Thunder Fang","Fire Fang","Iron Tail","Crunch"])
flint10=Flareon(maxiv="Yes", ability="Flash Fire",item="Sitrus Berry",move=["Flare Blitz","Flail","Will-O-Wisp","Quick Attack"])
flint11=Ninetales(maxiv="Grass", ability="Drought",item="Heat Rock",move=["Flamethrower","Solar Beam","Hypnosis","Nasty Plot"])
flint12=HRotom(maxiv="Yes",item="Choice Scarf",move=["Overheat","Discharge","Volt Switch","Shadow Ball"])
flint13=Blaziken(maxiv="Yes", ability="Speed Boost",move=["Protect","Close Combat","Rock Slide","Flare Blitz"])
flintteam=teamset([flint1,flint2,flint3,flint4,flint5,flint7,flint8,flint9,flint10,flint11,flint12,flint13],5)+[flint6]
flint=Trainer("Elite Four Flint",flintteam,"Sinnoh")
#Lucian
lucian1=Farigiraf(maxiv="Yes", ability="Armor Tail",move=["Twin Beam","Recover","Body Slam","Hypnosis"])
lucian2=Espeon(maxiv="Yes",move=["Psychic","Dazzling Gleam","Shadow Ball","Light Screen"], ability="Magic Bounce")
lucian3=Bronzong(maxiv="Yes", ability="Levitate",move=["Gyro Ball","Earthquake","Rock Slide","Extrasensory"],item="Muscle Band")
lucian4=Alakazam(maxiv="Yes",move=["Nasty Plot","Psychic","Dazzling Gleam","Thunderbolt"])
lucian5=Slowbro(maxiv="Yes", ability="Regenerator",move=["Scald","Psychic","Flamethrower","Psychic"],item="Leftovers")
lucian6=Gallade(maxiv="Yes",item="Galladite",move=["Close Combat","Psycho Cut","Poison Jab","Shadow Sneak"], ability="Justified")
lucian7=MrMime(maxiv="Yes",item="Light Clay",move=["Light Screen","Reflect","Psychic","Dazzling Gleam"], ability="Filter")
lucian8=Medicham(maxiv="Yes")
lucianteam=teamset([lucian1,lucian2,lucian7,lucian4,lucian5,lucian8],4)+[lucian6,lucian3]
lucian=Trainer("Elite Four Lucian",lucianteam,"Sinnoh")
#Buck
buck1=Shuckle(maxiv="Yes")
buck2=Umbreon(maxiv="Yes")
buck3=Torkoal(maxiv="Yes")
buck4=Dusknoir(maxiv="Yes")
buck5=Cloyster(maxiv="Yes")
buck6=Forretress(maxiv="Yes")
buck7=Steelix(maxiv="Yes")
buck8=Skarmory(maxiv="Yes")
buck9=Claydol(maxiv="Yes")
buck10=Regirock(maxiv="Yes")
buck11=Regice(maxiv="Yes")
buck12=Registeel(maxiv="Yes")
buck13=Bastiodon(maxiv="Yes")
buck14=Probopass(maxiv="Yes")
buck15=Metagross(maxiv="Yes")
buck16=Cresselia(maxiv="Yes")
buck17=Articuno(maxiv="Yes")
buck18=Suicune(maxiv="Yes")
buck19=Bronzong(maxiv="Yes")
buck20=Hippowdon(maxiv="Yes")
buck21=Tangrowth (maxiv="Yes")
buck22=Leafeon(maxiv="Yes")
buckteam=teamset([buck1,buck2,buck3,buck4,buck5,buck6,buck7,buck8,buck10,buck11,buck12,buck13,buck14,buck15,buck16,buck17,buck18,buck19,buck20,buck21,buck22],5)+[buck9]
buck=Trainer("Pokémon Trainer Buck",buckteam,"Sinnoh")
#Palmer
palmer1=Milotic(maxiv="Yes",ability="Competitive",move=["Muddy Water","Ice Beam","Hydro Pump","Protect"])
palmer2=Rhyperior(maxiv="Yes",item="Expert Belt",move=["Earthquake","Rock Blast","Ice Punch","Thunder Punch"])
palmer3=Dragonite(maxiv="Yes",item="Choice Band",move=["Fire Punch","Outrage","Earthquake","Thunder Punch"], ability="Multiscale")
palmer4=Cresselia(maxiv="Yes",item="Sitrus Berry",move=["Moonblast","Thunder Wave","Moonlight","Ice Beam"])
palmer5=Heatran(maxiv="Yes",item="Focus Sash",move=["Heat Wave","Flash Cannon","Dragon Pulse","Earth Power"])
palmer6=Regigigas(maxiv="Yes",move=["Crush Grip","Earthquake","Knock Off","Protect"],item="Life Orb")
palmer=Trainer("Tower Tycoon Palmer",[palmer1,palmer2,palmer3,palmer4,palmer5,palmer6],"Sinnoh")
#Thorton
Thorton1=Bronzong(maxiv="Yes")
Thorton2=Ursaluna(maxiv="Yes")
Thorton3=Ledian(maxiv="Yes")
Thorton4=Electivire(maxiv="Yes")
Thorton5=Skarmory(maxiv="Yes")
Thorton6=Tyranitar(maxiv="Yes",item="Tyranitarite")
Thorton=Trainer("Factory Head Thorton",[Thorton5,Thorton2,Thorton3,Thorton4,Thorton6,Thorton1],"Sinnoh")
#noland
noland1=Breloom(maxiv="Yes")
noland2=Rhyperior(maxiv="Yes")
noland3=Machamp(maxiv="Yes")
noland4=Venusaur(maxiv="Yes")
noland5=Articuno(maxiv="Yes")
noland6=Pinsir(maxiv="Yes",item="Pinsirite")
noland7=Aggron(maxiv="Yes")
noland8=Camerupt(maxiv="Yes")
noland9=Sandslash(maxiv="Yes")
noland10=Golduck(maxiv="Yes")
noland11=Manectric(maxiv="Yes")
noland12=Flygon(maxiv="Yes")
nolandteam=teamset([noland1,noland2,noland3,noland4,noland5,noland7,noland10,noland11,noland12,noland8,noland9],5)+[noland6]
noland=Trainer("Factory Head Noland",nolandteam,"Hoenn")
#Darach
darach1=Staraptor(maxiv="Yes",item="King's Rock",nature="Jolly",move=["Return","Brave Bird","Roost","Close Combat"], ability="Intimidate")
darach2=Empoleon(maxiv="Yes",item="Razor Claw",move=["Waterfall","Drill Peck","Brick Break","Knock Off"],nature="Adamant",atkev=252)
darach3=Houndoom(maxiv="Yes",item="Focus Sash",nature="Jolly",move=["Fire Fang","Crunch","Thunder Fang","Roar"])
darach4=Entei(maxiv="Yes",item="Shuca Berry",nature="Modest",move=["Fire Blast","Extrasensory","Shadow Ball","Calm Mind"])
darach5=Gallade(maxiv="Yes",nature="Adamant",move=["Psycho Cut","Close Combat","Night Slash","X-Scissor"],item="Galladite")
darach6=Alakazam(maxiv="Yes",item="Focus Sash",nature="Modest",move=["Nasty Plot","Psychic","Focus Blast","Shadow Ball"])
darach7=Metagross(maxiv="Yes",item="Air Balloon",move=["Fire Punch","Zen Headbutt","Meteor Mash","Bullet Punch"])
darachteam=teamset([darach1,darach2,darach3,darach6,darach7],4)+[darach4,darach5]
darach=Trainer("Castle Velvet Darach",darachteam,"Sinnoh")
#volo
volo1=Spiritomb(maxiv="Yes")
volo2=Togekiss(maxiv="Yes")
volo3=HArcanine(maxiv="Yes")
volo4=Lucario(maxiv="Yes")
volo5=Garchomp(maxiv="Yes")
volo6=Giratina(maxiv="Yes")
volo7=Roserade(maxiv="Yes")
voloteam=teamset([volo1,volo2,volo3,volo4,volo7],4)+[volo5,volo6]
volo=Trainer("Pokémon Wielder Volo",voloteam,"Hisui")
#Dahlia
dahlia1=Dusknoir(maxiv="Yes",move=["Will-O-Wisp","Trick Room","Shadow Punch","Trick"],nature="Brave",item="Iron Ball")
dahlia2=Medicham(maxiv="Yes",nature="Jolly",item="Salac Berry",move=["Zen Headbutt","Fake Out","Bulk Up","Drain Punch"])
dahlia3=Ludicolo(maxiv="Yes",item="Muscle Band",nature="Adamant",atkev=252,move=["Waterfall","Razor Leaf","Drain Punch","Swords Dance"])
dahlia4=Blaziken(maxiv="Yes",nature="Adamant",move=["Flare Blitz","High Jump Kick","Thunder Punch","Night Slash"],item="Blazikenite")
dahlia5=Togekiss(maxiv="Yes",nature="Modest",move=["Air Slash","Aura Sphere","Psychic","Moonblast"],item="Expert Belt")
dahlia6=Zapdos(maxiv="Yes",nature="Modest",item="Bright Powder",move=["Thunderbolt","Heat Wave","Hurricane","Roost"])
dahlia=Trainer("Arcade Star Dahlia",[dahlia1,dahlia2,dahlia3,dahlia5,dahlia4,dahlia6],"Sinnoh")
#Archie
archie7=Walrein(maxiv="Yes")
archie1=Mightyena(maxiv="Yes")
archie2=Muk(maxiv="Yes")
archie3=Crobat(maxiv="Yes")
archie4=Tentacruel(maxiv="Yes")
archie5=Sharpedo(maxiv="Yes",nature=random.choice(["Adamant","Jolly"]),move=["Crunch","Ice Fang","Protect",random.choice(["Earthquake","Psychic Fangs"])],item="Sharpedonite")
archie6=Kyogre(maxiv=random.choice(["Grass","Ground"]),nature=random.choice(["Modest","Timid"]),move=["Origin Pulse","Ice Beam",random.choice(["Tera Blast","Calm Mind"]),random.choice(["Water Spout","Thunder"])],item="Blue Orb")
archieteam=teamset([archie1,archie2,archie3,archie4,archie5],5)+[archie6]
archie=Trainer("Aqua Leader Archie",archieteam,"Hoenn")
#Maxie
maxie7=Houndoom(maxiv="Yes")
maxie1=Mightyena(maxiv="Yes")
maxie2=Weezing(maxiv="Yes")
maxie3=Crobat(maxiv="Yes")
maxie4=Torkoal(maxiv="Yes", ability="Drought",item="Heat Rock")
maxie5=Camerupt(maxiv="Yes",nature="Calm",move=["Fire Blast","Earth Power","Rest","Ancient Power"],item="Camerupite")
maxie6=Groudon(maxiv="Rock",nature="Adamant",move=["Stealth Rock","Swords Dance","Precipice Blades",random.choice(["Rock Tomb","Stone Edge"])],item="Red Orb")
maxieteam=teamset([maxie1,maxie2,maxie3,maxie4,maxie5],5)+[maxie6]
maxie=Trainer("Magma Leader Maxie",maxieteam,"Hoenn")
#Tabitha
tab1=Mightyena(maxiv="Yes")
tab2=Weezing(maxiv="Yes")
tab3=Crobat(maxiv="Yes")
tab4=Torkoal(maxiv="Yes", ability="Drought")
tab5=Camerupt(maxiv="Yes")
tab6=Swellow(maxiv="Yes")
tabitha=Trainer("Magma Admin Tabitha",[tab1,tab2,tab3,tab4,tab5,tab6],"Hoenn")
#blaise
blaise1=Magcargo(maxiv="Yes")
blaise2=Swellow (maxiv="Yes")
blaise3=Armaldo(maxiv="Yes")
blaise4=Torkoal(maxiv="Yes", ability="Drought")
blaise6=Camerupt(maxiv="Yes",item="Camerupite")
blaise5=Crobat(maxiv="Yes")
blaise=Trainer("Magma Admin Blaise",[blaise1,blaise2,blaise3,blaise4,blaise5,blaise6],"Hoenn")
#Brandon
brandon1=Regice(maxiv="Yes",nature="Modest",item="Chesto Berry",move=["Ice Beam","Rest","Amnesia","Thunder"], ability="'Clear Body")
brandon2=Regirock(maxiv="Yes", nature="Adamant",item="Quick Claw", ability="Clear Body",move=["Explosion","Superpower","Earthquake","Ancient Power"])
brandon3=Registeel(maxiv="Yes",nature="Adamant",ability="Clear Body",item="Leftovers",move=["Earthquake","Iron Head","Toxic","Iron Defense"])
brandon4=Articuno(maxiv="Yes",nature="Mild",item="Scope Lens",move=["Blizzard","Reflect","Hurricane","Hydro Pump"])
brandon5=Zapdos(maxiv="Yes",nature="Mild",item="Lum Berry",move=["Thunder","Drill Peck","Light Screen","Protect"])
brandon6=Moltres(maxiv="Yes",nature="Mild",item="Bright Powder",move=["Fire Blast","Hyper Beam","Hurricane","Roost"])
brandon7=Ninjask(maxiv="Yes")
brandon8=Dusclops(maxiv="Yes")
brandon9=Solrock(maxiv="Yes")
brandonteam=teamset([brandon7,brandon8,brandon9,brandon4,brandon5,brandon6],3)+[brandon1,brandon2,brandon3]
brandon=Trainer ("Pyramid King Brandon",brandonteam,"Hoenn")
#Illegal
illegal1=OArceus(maxiv="Yes")
illegal2=Cloyster()
illegal=Trainer("Missing No.",[illegal1,illegal2],"???")
#cyrus
cyrus1=Weavile(maxiv="Yes",item="Focus Sash",move=["Fake Out","Ice Punch","Ice Shard","Night Slash"])
cyrus2=Honchkrow(maxiv="Yes", ability="Super Luck",item="Scope Lens",move=["Night Slash","Drill Peck","Defog","Steel Wing"])
cyrus3=Crobat(maxiv="Yes",item="Quick Claw",move=["Tailwind","Cross Poison","U-turn","Dual Wingbeat"], ability="Infiltrator")
cyrus5=Houndoom(maxiv="Yes", move=["Fire Blast","Dark Pulse","Sludge Bomb","Shadow Ball"])
cyrus4=Gyarados (maxiv="Yes",item="Sitrus Berry", move=["Dragon Dance","Ice Fang","Power Whip","Waterfall"], ability="Intimidate")
cyrus8=Entei(maxiv="Yes",item="Muscle Band",move=["Sacred Fire","Bulldoze","Extreme Speed","Iron Head"], ability="Inner Focus")
cyrus6=Dialga(maxiv="Yes",move=["Roar of Time","Flash Cannon","Earth Power","Thunderbolt"])
cyrus7=Palkia(maxiv="Yes",move=["Spacial Rend","Surf","Earth Power","Thunderbolt"])
cyrus8=Absol(maxiv="Yes", ability="Super Luck",item="Scope Lens",move=["Night Slash","Psycho Cut","Sucker Punch","Close Combat"])
cyrus9=Arcanine(maxiv="Yes")
cyrus10=Camerupt(maxiv="Yes")
cyrus11=Charizard(maxiv="Yes")
cyrus12=Zapdos(maxiv="Yes",move=["Thunderbolt","Heat Wave","Hurricane","Roost"],item="Heavy-Duty Boots")
cyrus13=Darkrai(maxiv="Yes",move=["Dark Void","Dark Hole","Nasty Plot","Focus Blast"])
cyrus14=Sableye (maxiv="Yes")
cyrus15=Raticate(maxiv="Yes",move=["Endeavor","Quick Attack","Super Fang","Crunch"],item="Focus Sash",nature="Adamant")
cyrus16=HRotom(maxiv="Yes",item="Choice Scarf",move=["Overheat","Discharge","Volt Switch","Shadow Ball"])
cyrus17=Salamence(maxiv="Yes",item="White Herb",move=["Heat Wave","Draco Meteor","Hurricane","Protect"], ability="Intimidate", atkev=0,spatkev=252)
cyrusteam=teamset([cyrus1,cyrus2,cyrus8,cyrus4,cyrus5,cyrus8,cyrus9,cyrus10,cyrus11,cyrus12,cyrus13,cyrus14,cyrus15,cyrus16,cyrus17],4)+[cyrus6,cyrus7]
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
saturn10=Gallade(maxiv="Yes",item="Galladite")
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
mars9=Kangaskhan(maxiv="Yes",item="Kangaskhanite")
mars10=Magnezone (maxiv="Yes")
mars11=PorygonZ (maxiv="Yes")
marsteam=teamset([mars1,mars2,mars7,mars4,mars5,mars6,mars8,mars9,mars10],5)+[mars3]
mars=Trainer("Galactic Commander Mars",marsteam,"Sinnoh")
#jupiter
jupiter1=Nidoking(maxiv="Yes")
jupiter2=Bronzong(maxiv="Yes")
jupiter3=Skuntank(maxiv="Yes")
jupiter4=Gengar(maxiv="Yes",item="Gengarite")
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
siebold2=Gyarados(maxiv="Yes", move=["Dragon Dance","Ice Fang","Crunch","Waterfall"],nature="Adamant")
siebold3=Starmie(maxiv="Yes", ability="Natural Cure",move=["Psychic","Surf","Thunderbolt","Ice Beam"],item="Life Orb")
siebold4=Barbaracle(maxiv="Yes")
siebold5=Milotic(maxiv="Yes")
siebold7=Octillery(maxiv="Yes")
siebold6=Blastoise(maxiv="Yes",item="Blastoisinite",move=["Dragon Pulse","Dark Pulse","Hydro Pump","Shell Smash"])
sieboldteam=teamset([siebold1,siebold2,siebold3,siebold4,siebold5,siebold7],5)+[siebold6]
siebold=Trainer("Elite Four Siebold", sieboldteam,"Kalos")
#E4 Wikstrom
wikstrom1=Probopass(maxiv="Yes",move=["Power Gem","Earth Power","Discharge","Flash Cannon"], ability="Sturdy",spatkev=252)
wikstrom2=Aegislash (maxiv="Yes",move=["Sacred Sword","Iron Head","Shadow Claw","King's Shield"],nature="Adamant")
wikstrom3=Escavalier(maxiv="Yes",move=["Double Iron Bash","X-Scissor","U-turn","Swords Dance"],atkev=252)
wikstrom4=Kingambit (maxiv="Yes")
wikstrom5=Klefki(maxiv="Yes",move=["Flash Cannon","Spikes","Dazzling Gleam","Taunt"], ability="Prankster")
wikstrom6=Scizor(maxiv="Yes",item="Scizorite",move=["X-Scissor","Night Slash","Iron Head","Bullet Punch"],nature="Adamant")
wikstrom=Trainer("Elite Four Wikstrom",[wikstrom1,wikstrom2,wikstrom3,wikstrom4,wikstrom5,wikstrom6],"Kalos")
#E4 Drasna
drasna1=Druddigon(maxiv="Yes")
drasna2=Dragalge(maxiv="Yes")
drasna3=Noivern(maxiv="Yes")
drasna4=Goodra(maxiv="Yes")
drasna5=Tyrantrum(maxiv="Yes")
drasna6=Altaria(maxiv="Yes",item="Altarianite")
drasna=Trainer("Elite Four Drasna",[drasna1,drasna2,drasna3,drasna4,drasna5,drasna6],"Kalos")
#E4 Malva
malva1=Talonflame(maxiv="Yes",spatkev=0,atkev=252,move=["Brave Bird","Swords Dance","Roost","Flare Blitz"], ability="Gale Wings",nature="Adamant",item="Leftovers")
malva2=Pyroar(maxiv="Yes",item=random.choice(["Life Orb","Choice Specs"]),move=["Fire Blast","Hyper Voice","Hidden Power",random.choice(["Will-O-Wisp","Taunt","Flamethrower"])],nature="Timid")
malva3=Torkoal(maxiv="Yes", ability="Drought",item="Heat Rock",move=["Stealth Rock","Yawn","Lava Plume","Rapid Spin"],nature="Bold")
malva4=Chandelure(maxiv="Yes", ability="Flash Fire",move=["Fire Blast","Shadow Ball","Energy Ball","Trick"],item="Choice Scarf",nature="Timid")
malva5=Delphox(maxiv="Yes",item=random.choice(["Life Orb","Salac Berry"]), ability="Blaze", nature="Timid",move=["Fire Blast","Psychic","Calm Mind","Grass Knot"])
malva6=Houndoom(maxiv="Yes",item="Houndoominite", ability="Flash Fire", nature="Timid",move=["Nasty Plot","Fire Blast","Dark Pulse",random.choice(["Taunt","Will-O-Wisp"])])
malva7=Yveltal(maxiv="Yes",item=random.choice(["Life Orb","Black Glasses"]), nature="Rash",move=["Dark Pulse","Oblivion Wing","Sucker Punch",random.choice(["Heat Wave","Focus Blast"])])
malva=Trainer("Elite Four Malva",[malva1,malva2,malva4,malva5,malva6,malva7],"Kalos")
#n
n1=Carracosta(maxiv="Yes")
n2=Vanilluxe(maxiv="Yes")
n3=Archeops(maxiv="Yes")
n4=Zoroark(maxiv="Yes",item="Life Orb",nature="Timid",move=["Nasty Plot","Dark Pulse",random.choice(["Focus Blast","Flamethrower"]),"Sludge Bomb"])
n5=Zekrom(maxiv="Yes")
n6=Reshiram(maxiv="Yes")
n7=BKyurem(maxiv="Yes")
n8=Sigilyph (maxiv="Yes")
nteam=teamset([n1,n2,n3,n4,n8],4)+teamset([n5,n6,n7],2)
n=Trainer("Pokémon Trainer N",nteam,"Unova")
#Ghetsis
ghet4=Hydreigon(maxiv="Yes")
ghet2=Kingambit (maxiv="Yes")
ghet3=Drapion(maxiv="Yes")
ghet1=Seismitoad(maxiv="Yes")
ghet5=WKyurem(maxiv="Yes")
ghet6=BKyurem(maxiv="Yes")
ghet7=Cofagrigus(maxiv="Yes")
ghet8=Bouffalant(maxiv="Yes")
ghet9=Eelektross(maxiv="Yes")
ghet10=Toxicroak(maxiv="Yes")
ghet11=Kyurem(maxiv="Yes")
ghetsisteam=teamset([ghet9,ghet3,ghet2,ghet4,ghet7,ghet8,ghet9,ghet10,ghet11],5)+teamset([ghet5,ghet6],1)
ghetsis=Trainer("Plasma Leader Ghetsis", ghetsisteam,"Unova")
#Alain
alain1=Tyranitar(maxiv="Yes",move=["Dark Pulse","Stone Edge","Crunch","Stealth Rock"],nature="Brave")
alain2=Kingambit (maxiv="Yes",move=["Thunder Wave","Focus Blast","Iron Head","Kowtow Cleave"],item="Life Orb")
alain3=Unfezant(maxiv="Yes",move=["Sky Attack","Steel Wing","Heat Wave","Air Slash"])
alain4=Metagross(maxiv="Yes",move=["Meteor Mash","Psyshock","Rock Slide","Agility"],nature="Naughty")
alain5=Weavile(maxiv="Yes",move=["Protect","Night Slash","Ice Beam","Double Team"],nature="Hasty")
alain6=Charizard(maxiv="Yes",move=["Flamethrower","Dragon Claw","Thunder Punch","Blast Burn"],nature="Hasty",item="Charizardite X",atkev=252,spatkev=0)
alain7=Malamar(maxiv="Yes",move=["Psycho Cut","Throat Chop","Superpower","Night Slash"])
alain8=Chesnaught(maxiv="Yes",move=["Hammer Arm","Spiky Shield","Gyro Ball","Pin Missile"])
alainteam=teamset([alain1,alain2,alain3,alain4,alain5,alain7,alain8],5)+[alain6]
alain=Trainer("Pokémon Trainer Alain",alainteam,"Kalos")
#Anabel
anabel1=Alakazam(maxiv="Yes")
anabel2=Latios(maxiv="Yes")
anabel3=Snorlax(maxiv="Yes")
anabel4=Entei(maxiv="Yes")
anabel5=Raikou(maxiv="Electric")
anabel6=Lucario(maxiv="Yes")
anabel7=Weavile(maxiv="Yes")
anabel8=Mismagius(maxiv="Yes")
anabel9=Salamence(maxiv="Yes")
anabelteam=teamset([anabel1,anabel2,anabel7,anabel4,anabel5,anabel6,anabel8,anabel9],5)+[anabel3]
anabel=Trainer("Salon Maiden Anabel",anabelteam,"Hoenn")
#greta
greta1=Heracross(maxiv="Yes",nature="Jolly")
greta2=Breloom(maxiv="Yes",nature="Jolly")
greta3=Umbreon(maxiv="Yes",nature="Calm")
greta4=Gengar(maxiv="Yes",nature="Modest")
greta5=Hariyama(maxiv="Yes")
greta6=Medicham(maxiv="Yes",item="Medichamite")
greta7=Shedinja(maxiv="Yes",nature="Adamant")
gretateam=teamset([greta1,greta2,greta3,greta4,greta5,greta7],5)+[greta6]
greta=Trainer("Arena Tycoon Greta",gretateam,"Hoenn")
#Tucker
tucker1=Metagross(maxiv="Yes",nature="Brave")
tucker2=Arcanine(maxiv="Yes")
tucker3=Charizard(maxiv="Yes")
tucker4=Salamence(maxiv="Yes",nature="Adamant", ability="Intimidate")
tucker5=Latias(maxiv="Yes",nature="Modest")
tucker6=Swampert(maxiv="Yes",nature="Brave")
tucker=Trainer ("Dome Ace Tucker",[tucker1,tucker2,tucker3,tucker4,tucker5,tucker6],"Hoenn")
#Lucy
lucy1=Arbok(maxiv="Yes")
lucy2=Snorlax(maxiv="Yes")
lucy3=Steelix(maxiv="Yes")
lucy4=Gyarados(maxiv="Yes")
lucy5=Milotic(maxiv="Yes",move=["Ice Beam","Mirror Coat","Surf","Recover"],nature="Modest",item="Leftovers")
lucy6=Seviper(maxiv="Yes")
lucy7=Shuckle(maxiv="Yes",move=["Sandstorm","Toxic","Cosmic Power","Stealth Rock"],item="Leftovers",nature="Bold", ability="Sturdy")
lucyteam=teamset([lucy1,lucy2,lucy3,lucy4,lucy5,lucy7],5)+[lucy6]
lucy=Trainer ("Pike Queen Lucy",lucyteam,"Hoenn")
#spenser
spenser1=Arcanine(maxiv="Yes",nature="Hasty",item="White Herb",move=["Overheat","Roar","Protect","Extreme Speed"],defev=252,speedev=0,hpev=4)
spenser2=Lapras(maxiv="Yes",item="Quick Claw")
spenser3=Slaking(maxiv="Yes",move=["Shadow Ball","Earthquake","Swagger","Brick Break"],item="Scope Lens",hpev=152,atkev=152,spatkev=100,speedev=106)
spenser4=Crobat(maxiv="Yes",nature="Adamant",item="Bright Powder")
spenser5=Suicune(maxiv="Yes",nature="Hasty",item="King's Rock", move=["Blizzard","Surf","Crunch","Calm Mind"],hpev=252,defev=252,spatkev=0,speedev=6)
spenser6=Venusaur(maxiv="Yes",ability="Chlorophyll",nature="Modest",move=["Earth Power","Giga Drain","Sludge Bomb","Sleep Powder"])
spenser8=Claydol(maxiv="Yes")
spenser9=Dusclops(maxiv="Yes")
spenser10=Chansey(maxiv="Yes")
spenser11=Shiftry(maxiv="Yes")
spenserteam=teamset([spenser1,spenser2,spenser3,spenser4,spenser5,spenser8,spenser9,spenser10,spenser11],5)+[spenser6]
spenser=Trainer("Palace Maven Spenser",spenserteam,"Hoenn")
#Giovanni
gio1=Nidoqueen(maxiv="Yes")
gio2=Nidoking(maxiv="Yes")
gio3=Honchkrow(maxiv="Yes")
gio4=Rhyperior(maxiv="Yes")
gio5=Kangaskhan(maxiv="Yes",nature="Jolly",move=["Fake Out","Seismic Toss",random.choice(["Shadow Claw","Crunch"]),random.choice(["Body Slam","Rock Tomb"])],item="Kangaskhanite")
gio6=Mewtwo(maxiv="Yes")
gio7=Garchomp(maxiv="Yes")
gio8=Dugtrio(maxiv="Yes")
gio9=Steelix(maxiv="Yes")
gio10=Persian(maxiv="Yes")
gio11=Marowak(maxiv="Yes")
gio12=Sandslash(maxiv="Yes")
gio13=Gliscor(maxiv="Yes")
gio14=Krookodile(maxiv="Yes")
gio15=Hippowdon(maxiv="Yes", ability="Sand Stream",move=["Roar","Stealth Rock","Stone Edge","Earthquake"],nature="Careful",item="Rocky Helmet")
gio22=Gyarados(maxiv="Yes")
gioteam=teamset([gio1,gio2,gio3,gio4,gio7,gio8,gio9,gio10,gio11,gio12,gio13,gio14,gio15,gio22],4)+[gio5,gio6]
giovanni=Trainer("Rocket Boss Giovanni",gioteam,"Kanto")
#Archer
archer1=Electrode(maxiv="Yes")
archer2=Mightyena(maxiv="Yes")
archer3=Weezing(maxiv="Yes")
archer4=Crobat(maxiv="Yes")
archer5=Tyranitar(maxiv="Yes")
archer6=Houndoom(maxiv="Yes",item="Houndoominite")
archer7=Persian(maxiv="Yes")
archer8=Mismagius(maxiv="Yes")
archer9=Victreebel(maxiv="Yes")
archer10=Wobbuffet(maxiv="Yes")
archer11=Octillery (maxiv="Yes")
archer12=Hypno(maxiv="Yes")
archer13=Parasect(maxiv="Yes")
archerteam=teamset([archer1,archer2,archer3,archer4,archer5,archer7,archer8,archer9,archer10,archer11,archer12],5)+[archer6]
archer=Trainer("Rocket Executive Archer",archerteam,"Kanto")
#sird
sird1=Crobat(maxiv="Yes")
sird2=Weezing (maxiv="Yes")
sird3=Starmie(maxiv="Yes")
sird4=Persian(maxiv="Yes")
sird5=Banette(maxiv="Yes",item="Banettite")
sird6=Darkrai(maxiv="Yes")
sird=Trainer("Rocket Admin Sird",[sird1,sird2,sird3,sird4,sird5,sird6],"Kanto")
#petrel
petrel1=Crobat(maxiv="Yes")
petrel2=Weezing (maxiv="Yes")
petrel3=Weezing(maxiv="Yes")
petrel4=GWeezing(maxiv="Yes")
petrel5=GWeezing(maxiv="Yes")
petrel6=Raticate(maxiv="Yes")
petrel=Trainer("Rocket Executive Petrel",[petrel1,petrel2,petrel3,petrel4,petrel5,petrel6],"Kanto")
#proton
proton1=Crobat(maxiv="Yes")
proton2=Weezing (maxiv="Yes")
proton3=Crobat(maxiv="Yes")
proton4=Weezing(maxiv="Yes")
proton5=Weezing(maxiv="Yes")
proton6=Crobat(maxiv="Yes")
proton=Trainer("Rocket Executive Proton",[proton1,proton2,proton3,proton4,proton5,proton6],"Kanto")
#Ariana
ariana1=Muk(maxiv="Yes")
ariana2=Honchkrow(maxiv="Yes")
ariana3=Weavile(maxiv="Yes")
ariana4=Crobat(maxiv="Yes")
ariana5=Arbok(maxiv="Yes")
ariana6=Mawile(maxiv="Yes",item="Mawilite")
ariana7=Vileplume(maxiv="Yes")
ariana8=Weavile(maxiv="Yes")
ariana9=Lickilicky (maxiv="Yes")
ariana10=Raticate (maxiv="Yes")
ariana11=Magcargo(maxiv="Yes")
ariana12=Kabutops (maxiv="Yes")
ariana13=Victreebel(maxiv="Yes")
arianateam=teamset([ariana1,ariana2,ariana3,ariana4,ariana5,ariana7,ariana8,ariana9,ariana10,ariana11,ariana12,ariana13],5)+[ariana6]
ariana=Trainer("Rocket Executive Ariana",arianateam,"Kanto")
#Silver
silver1=Weavile (maxiv="Yes")
silver2=Honchkrow(maxiv="Yes")
silver3=Kingdra(maxiv="Yes")
silver4=Ursaluna(maxiv="Yes")
silver5=Gyarados(name="Gyarados✨",maxiv="Yes")
silver6=Feraligatr(maxiv="Yes")
silver11=Meganium(maxiv="Yes")
silver12=Typhlosion(maxiv="Yes")
silver7=Gengar(maxiv="Yes")
silver8=Alakazam (maxiv="Yes",item="Alakazite")
silver9=Crobat(maxiv="Yes")
silver10=Magnezone(maxiv="Yes")
silver13=Hooh(maxiv="Yes")
silver14=Lugia(maxiv="Yes")
silver15=Mewtwo(maxiv="Yes")
silver16=Nidoking(maxiv="Yes")
silverteam=teamset([random.choice([silver13,silver14,silver15]),silver1,silver2,silver3,silver4,silver7,silver8,silver9,silver10,silver5,silver16],5)+teamset([silver6,silver11,silver12],1)
silver=Trainer("Rival Silver",silverteam,"Johto")
#Gary
gary1=Arcanine(maxiv="Yes")
gary2=Nidoking(maxiv="Yes")
gary3=Scizor(maxiv="Yes")
gary4=Umbreon(maxiv="Yes")
gary5=Electivire(maxiv="Yes")
gary6=Blastoise(maxiv="Yes")
gary7=Nidoqueen(maxiv="Yes")
gary8=Dodrio(maxiv="Yes")
gary9=Tyranitar(maxiv="Yes",item="Tyranitarite")
gary10=Hatterene(maxiv="Yes")
gary11=Regidrago(maxiv="Yes")
gary12=Golem(maxiv="Yes")
gary13=Skarmory (maxiv="Yes")
gary14=Houndoom(maxiv="Yes")
gary15=Alakazam(maxiv="Yes")
gary16=Kingdra(maxiv="Yes")
garyteam=teamset([gary1,gary2,gary3,gary7,gary8,gary9,gary10,gary11,gary12,gary13,gary14,gary15,gary16],3)+[gary4,gary5,gary6]
gary=Trainer("Rival Gary Oak",garyteam,"Kanto")
#Blue
blue1=Exeggutor(maxiv="Yes",move=["Power Whip","Light Screen","Psychic","Body Slam"])
blue2=Alakazam(maxiv="Yes",move=["Dazzling Gleam","Psychic","Reflect","Foul Play"])
blue3=Rhyperior(maxiv="Yes")
blue4=Gyarados(maxiv="Yes",move=["Waterfall","Crunch","Earthquake","Outrage"])
blue5=Arcanine(maxiv="Yes")
blue6=Pidgeot(maxiv="Yes",nature="Timid", move=["Hurricane","Heat Wave","Roost","U-turn"],item="Pidgeotite")
blue7=Machamp(maxiv="Yes")
blue8=Tyranitar(maxiv="Yes")
blue9=Blastoise (maxiv="Yes")
blue10=Venusaur(maxiv="Yes")
blue11=Charizard(maxiv="Yes",item="Charizardite Y",move=["Fire Blast","Dragon Pulse","Hyper Beam","Air Slash"])
blue12=Ninetales(maxiv="Yes")
blue13=Cloyster(maxiv="Yes")
blue14=Jolteon(maxiv="Yes")
blue15=Vaporeon (maxiv="Yes")
blue16=Flareon(maxiv="Yes")
blue17=Heracross(maxiv="Yes")
blue18=Aerodactyl(maxiv="Yes",move=["Rock Slide","Iron Tail","Earthquake","Crunch"])
blue19=Tauros(maxiv="Yes",move=["Double-Edge","Rock Slide","Earthquake","Iron Tail"])
blueteam=teamset([blue2,blue3,blue4,blue5,blue7,blue8,blue19],3)+teamset([blue14,blue15,blue16],1)+teamset([blue9,blue10,blue11],1)+[blue6]
blue=Trainer(random.choice(["Pokémon Trainer","Battle Legend","Kanto Champion","Rival","Gym Leader"])+" Blue",blueteam,"Kanto")
#falkner
falkner1=Pelipper(maxiv="Yes")
falkner2=Honchkrow(maxiv="Yes")
falkner3=Swellow(maxiv="Yes")
falkner4=Skarmory(maxiv="Yes")
falkner5=Noctowl(maxiv="Yes")
falkner6=Pidgeot(maxiv="Yes",nature="Timid", move=["Hurricane","Heat Wave","Roost","U-turn"],item="Pidgeotite")
falkner7=Staraptor(maxiv="Yes")
falkner8=Fearow(maxiv="Yes")
falkner9=Xatu(maxiv="Yes")
falkner10=Dodrio(maxiv="Yes")
falkner11=Crobat(maxiv="Yes")
falkner12=Aerodactyl(maxiv="Yes")
falkner13=Lugia(maxiv="Yes")
falkner14=Togekiss(maxiv="Yes")
falknerteam=teamset([falkner1,falkner2,falkner3,falkner4,falkner5,falkner7,falkner8,falkner9,falkner10,falkner11,falkner12,falkner13,falkner14],5)+[falkner6]
falkner=Trainer ("Gym Leader Falkner",falknerteam,"Johto")
#Kukui
kukui1=Braviary(maxiv="Yes",item="Life Orb", move=["Crush Claw","Brave Bird","Tailwind","Whirlwind"],nature="Adamant")
kukui2=Venusaur(maxiv="Yes",nature="Modest",move=["Earth Power","Sludge Bomb","Weather Ball","Giga Drain"])
kukui3=Empoleon(maxiv="Yes",nature="Modest", ability="Competitive",move=["Ice Beam","Surf","Flash Cannon","Drill Peck"])
kukui4=Lucario(maxiv="Yes",nature="Adamant",move=["Bullet Punch","Meteor Mash","Close Combat","Bone Rush"])
kukui5=MDLycanroc(maxiv="Yes", item="Life Orb",nature="Adamant",move=["Stone Edge","Accelerock","Snarl","Protect"])
kukui6=Incineroar(name="Incineroar(Z-Crystal)",maxiv="Yes",nature="Adamant",move=["Flare Blitz","Darkest Lariat","Outrage","Cross Chop"])
kukui7=ANinetales(maxiv="Yes",item="Passho Berry",nature="Timid",move=["Freeze-Dry","Dazzling Gleam","Extrasensory","Ice Shard"])
kukui8=Magnezone(maxiv="Yes",item="Assault Vest",nature="Modest",move=["Thunderbolt","Flash Cannon","Volt Switch","Thunder"])
kukui9=Snorlax(maxiv="Yes",item="Assault Vest", nature="Careful",move=["Body Slam","Fissure","Earthquake","Crunch"])
kukui10=Crabominable(maxiv="Yes",item="Quick Claw",move=["Ice Hammer","Close Combat","Assurance","Protect"],nature="Brave")
kukuiteam=teamset([kukui1,kukui2,kukui3,kukui4,kukui5,kukui7,kukui8,kukui9,kukui10],5)+[kukui6]
kukui=Trainer("Professor Kukui",kukuiteam,"Alola")
#Ethan
ethan1=Tauros(maxiv="Yes")
ethan2=Tangrowth(maxiv="Yes")
ethan3=PorygonZ(maxiv="Yes")
ethan4=Azumarill(maxiv="Yes")
ethan5=Venusaur(maxiv="Yes", item="Venusaurite")
ethan6=Typhlosion(maxiv="Grass",move=["Focus Blast","Hidden Power","Eruption","Flamethrower"], nature="Modest")
ethan7=Lugia(maxiv="Yes")
ethanteam=teamset([ethan1,ethan2,ethan3,ethan4,ethan5,ethan7],5)+[ethan6]
ethan=Trainer("Pokémon Trainer Ethan", ethanteam,"Johto")
#Mustard
mustard1=WUrshifu(maxiv="Yes")
mustard9=WUrshifu(maxiv="Yes")
mustard8=DUrshifu(maxiv="Yes")
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
bren5=Latios(maxiv="Yes")
bren6=Sceptile(maxiv="Yes",item="Sceptilite")
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
bren10=Groudon(maxiv="Yes")
bren22=Kyogre(maxiv="Yes")
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
may5=Latias(maxiv="Yes")
may6=Blaziken(maxiv="Yes",item="Blazikenite")
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
may22=Kyogre(maxiv="Yes")
may23=Groudon(maxiv="Yes")
may24=Rayquaza(maxiv="Yes")
may25=Lopunny(maxiv="Yes")
may26=Latios(maxiv="Yes")
may27=Aggron(maxiv="Yes")
may28=Altaria(maxiv="Yes")
mayteam=teamset([may1,may2,may3,may4,may5,may7,may8,may9,may10,may11,may12,may13,may14,may15,may16,may17,may18,may19,may20,may21,may22,may23,may24,may25,may26,may27,may28],5)+[may6]
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
ingo12=Chandelure(maxiv="Yes")
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
emmet8=Eelektross(maxiv="Yes")
emmet9=Galvantula (maxiv="Yes")
emmet10=Archeops(maxiv="Yes")
emmet11=Gigalith(maxiv="Yes")
emmet12=Escavalier (maxiv="Yes")
emmet13=Accelgor(maxiv="Yes")
emmetteam=teamset([emmet1,emmet2,emmet3,emmet4,emmet5,emmet7,emmet6,emmet9,emmet10,emmet11,emmet12,emmet13],5)+[emmet8]
emmet=Trainer ("Subway Boss Emmet",emmetteam,"Unova")
#Phoebe
phoebe1=Banette(maxiv="Yes")
phoebe2=Mismagius(maxiv="Yes")
phoebe3=Drifblim(maxiv="Yes")
phoebe4=Chandelure(maxiv="Yes")
phoebe5=Dusknoir(maxiv="Yes")
phoebe6=Sableye(maxiv="Yes",item="Sablenite")
phoebeteam=teamset([phoebe1,phoebe2,phoebe3,phoebe4,phoebe5],5)+[phoebe6]
phoebe=Trainer ("Elite Four Phoebe",phoebeteam,"Hoenn")
#Sidney
sidney1=Shiftry(maxiv="Yes", ability="Chlorophyll",move=["Fake Out","Extrasensory","Leaf Blade","Hurricane"],item="King's Rock")
sidney2=Scrafty(maxiv="Yes", ability="Intimidate",move=["Crunch","Brick Break","Poison Jab","Dragon Claw"])
sidney3=Zoroark(maxiv="Yes",move=["Dark Pulse","Nasty Plot","Flamethrower","Sludge Bomb"],nature="Timid")
sidney4=Sharpedo(maxiv="Yes",move=["Crunch","Aqua Jet","Liquidation","Poison Fang"])
sidney5=Mandibuzz(maxiv="Yes",move=["Tailwind","Bone Rush","Brave Bird","Roost"],item="Rocky Helmet")
sidney6=Absol(maxiv="Yes",item="Absolite", ability="Super Luck",move=["Night Slash","Psycho Cut","Play Rough","Sucker Punch"], nature="Adamant")
sidney7=Cacturne(maxiv="Yes",move=["Needle Arm","Spiky Shield","Leech Shield","Knock Off"])
sidney8=Crawdaunt(maxiv="Yes",move=["Swords Dance","Crabhammer","Knock Off","Guillotine"])
sidney9=Mightyena(maxiv="Yes",move=["Crunch","Sucker Punch","Poison Fang","Psychic Fangs"], ability="Intimidate")
sidneyteam=teamset([sidney1,sidney2,sidney3,sidney4,sidney5,sidney7,sidney8,sidney9],5)+[sidney6]
sidney=Trainer ("Elite Four Sidney",sidneyteam,"Hoenn")
#Glacia
glacia1=Abomasnow(maxiv="Yes", ability="Snow Warning",move=["Blizzard","Wood Hammer","Ice Shard","Earthquake"],item="Icy Rock")
glacia2=Beartic(maxiv="Yes",move=["Icicle Crash","Shadow Claw","Brick Break","Slash"], ability="Snow Cloak")
glacia3=Froslass(maxiv="Yes",move=["Draining Kiss","Blizzard","Shadow Ball","Snowscape"], ability="Snow Cloak")
glacia4=Vanilluxe(maxiv="Yes",move=["Ice Beam","Freeze-Dry","Mirror Coat","Signal Beam"], ability="Ice Body")
glacia5=Walrein(maxiv="Yes",move=["Surf","Blizzard","Blizzard","Sheer Cold"], ability="Thick Fat")
glacia6=Glalie(maxiv="Yes", item="Glalitite",move=["Protect","Snowscape","Freeze-Dry","Ice Shard"], ability="Inner Focus")
glacia=Trainer ("Elite Four Glacia",[glacia1,glacia2,glacia3,glacia4,glacia5,glacia6],"Hoenn")
#Drake
drake1=Altaria(maxiv="Yes")
drake2=Dragalge(maxiv="Yes")
drake3=Kingdra(maxiv="Yes")
drake4=Flygon(maxiv="Yes")
drake5=Haxorus(maxiv="Yes")
drake6=Salamence(maxiv="Yes",item="Salamencite")
drake=Trainer ("Elite Four Drake",[drake1,drake2,drake3,drake4,drake5,drake6],"Hoenn")
#Karen
karen1=Weavile(maxiv="Yes",move=["Ice Shard","Ice Punch","Low Kick","Night Slash"])
karen2=Absol(maxiv="Yes",item="Absolite", ability="Super Luck",move=["Psycho Cut","Night Slash","Protect","Play Rough"])
karen3=Spiritomb(maxiv="Yes",move=["Curse","Sucker Punch","Pain Split","Shadow Sneak"])
karen4=Houndoom(maxiv="Yes",move=["Nasty Plot","Sludge Bomb","Dark Pulse","Flamethrower"], ability="Flash Fire")
karen5=Honchkrow(maxiv="Yes",move=["Drill Peck","Thunder Wave","Whirlwind","Sucker Punch"], ability="Super Luck",item="Scope Lens")
karen6=Umbreon(maxiv="Yes",nature="Careful",move=["Toxic","Wish","Protect","Foul Play"],item="Leftovers", ability="Synchronize")
karen7=Vileplume(maxiv="Yes",move=["Sleep Powder","Petal Dance","Sludge Bomb","Moonlight"])
karen8=Gengar(maxiv="Yes",move=["Focus Blast","Destiny Bond","Shadow Ball","Sludge move"], ability="Levitate")
karenteam=teamset([karen1,karen2,karen3,karen4,karen5,karen7,karen8],5)+[karen6]
karen=Trainer ("Elite Four Karen",karenteam,"Johto")
#brock
brock1=Omastar(maxiv="Yes",item="Rindo Berry",move=["Hydro Pump","Ancient Power","Ice Beam","Earth Power"])
brock2=Kabutops(maxiv="Yes",item="Focus Sash",move=["Waterfall","Rock Slide","X-Scissor","Swords Dance"])
brock3=Rhyperior (maxiv="Yes",move=["Earthquake","Stone Edge","Megahorn","Icicle Crash"],item="Expert Belt")
brock4=Golem(maxiv="Yes",item="Lum Berry",move=["Stone Edge","Earthquake","Rock Polish","Sucker Punch"])
brock5=Tyranitar(maxiv="Yes",move=["Stone Edge","Thunder Punch","Ice Punch","Crunch"],item="Chople Berry")
brock6=Steelix(maxiv="Yes",item="Steelixite")
brock7=Rampardos(maxiv="Yes",move=["Earthquake","Stone Edge","Rock Polish","Icicle Crash"])
brock8=Aerodactyl(maxiv="Yes",item="Choice Scarf",move=["Rock Slide","Earthquake","Fire Fang","Ice Fang"])
brock9=Relicanth(maxiv="Yes",item="Rock Gem",move=["Rock Slide","Waterfall","Rock Polish","Yawn"])
brock10=Sudowoodo(maxiv="Yes")
brock11=Blissey(maxiv="Yes")
brock13=Sandslash(maxiv="Yes")
brock14=Crobat(maxiv="Yes")
brock15=Ninetales(maxiv="Yes")
brock16=Swampert(maxiv="Yes")
brock17=Forretress(maxiv="Yes")
brockteam=teamset([brock1,brock2,brock3,brock4,brock5,brock7,brock8,brock9,brock10,brock11,brock13,brock14,brock15,brock16,brock17],5)+[brock6]
brock=Trainer ("Gym Leader Brock",brockteam,"Kanto")
#Marshal
marshal1=Breloom(maxiv="Yes")
marshal2=Mienshao(maxiv="Yes")
marshal3=Toxicroak(maxiv="Yes")
marshal4=Lucario(maxiv="Yes",item="Lucarionite",move=["Close Combat","Ice Punch","Bullet Punch","Rock Slide"], ability="Justified", nature="Hasty")
marshal5=Machamp(maxiv="Yes")
marshal6=Conkeldurr(maxiv="Yes")
marshal7=Sawk(maxiv="Yes")
marshal8=Throh(maxiv="Yes")
marshal9=Medicham(maxiv="Yes")
marshalteam=teamset([marshal1,marshal2,marshal3,marshal4,marshal5,marshal7,marshal8,marshal9],5)+[marshal6]
marshal=Trainer ("Elite Four Marshal",marshalteam,"Unova")
#shauntal
shauntal1=Cofagrigus(maxiv="Yes")
shauntal2=Jellicent(maxiv="Yes",item="Leftovers",move=["Scald","Icy Wind","Shadow Ball","Recover"], ability="Water Absorb", nature="Bold")
shauntal3=Drifblim(maxiv="Yes")
shauntal4=Golurk(maxiv="Yes",item="Rindo Berry",move=["Shadow Punch","Shadow Sneak","High Horsepower","Ice Punch"], ability="Ice Punch",nature="Calm")
shauntal5=Froslass(maxiv="Yes")
shauntal6=Chandelure(maxiv="Yes",item="Air Balloon",move=["Heat Wave","Shadow Ball","Energy Ball","Will-O-Wisp"],nature="Bashful", ability="Shadow Tag")
shauntal7=Gengar(maxiv="Yes",item="Life Orb",move=["Shadow Ball","Sludge Bomb","Aura Sphere","Energy Ball"], ability="Levitate", nature="Jolly")
shauntal8=Mismagius(maxiv="Yes",item="Focus Sash",move=["Mystical Fire","Shadow Ball","Dazzling Gleam","Nasty Plot"], nature="Relaxed", ability="Levitate")
shauntal9=Banette(maxiv="Yes")
shauntalteam=teamset([shauntal1,shauntal2,shauntal3,shauntal4,shauntal5,shauntal7,shauntal8,shauntal9],5)+[shauntal6]
shauntal=Trainer ("Elite Four Shauntal",shauntalteam,"Unova")
#grimsley
grimsley1=Scrafty(maxiv="Yes")
grimsley2=Drapion(maxiv="Yes")
grimsley3=Krookodile (maxiv="Yes",item="Leftovers", ability="Intimidate",move=["Earthquake","Knock Off","Stealth Rock","Toxic"])
grimsley4=Houndoom(maxiv="Yes")
grimsley6=Tyranitar(maxiv="Yes",move=["Dragon Dance","Crunch","Stone Edge","Ice Beam"],nature="Gentle")
grimsley5=Kingambit(maxiv="Yes")
grimsley7=Liepard(maxiv="Yes")
grimsley8=Honchkrow (maxiv="Yes",ability="Moxie",move=["Night Slash","Brave Bird","Superpower","Heat Wave"])
grimsley9=Absol(maxiv="Yes",ability="Super Luck",move=["Night Slash","Psycho Cut","Close Combat","Sucker Punch"],nature="Adamant")
grimsley10=Sharpedo(maxiv="Yes")
grimsleyteam=teamset([grimsley1,grimsley2,grimsley3,grimsley4,grimsley5,grimsley7, grimsley8, grimsley9,grimsley10],5)+[grimsley6]
grimsley=Trainer ("Elite Four Grimsley", grimsleyteam,"Unova")
#caitlin
caitlin1=Alakazam(maxiv="Yes")
caitlin2=Gallade (maxiv="Yes",item="Life Orb",move=["Psycho Cut","Close Combat","Triple Axel","Swords Dance"],nature="Adamant", ability="Justified")
caitlin3=Reuniclus (maxiv="Yes")
caitlin4=Metagross (maxiv="Yes",item="Air Balloon",move=["Meteor Mash","Rock Slide","Trick Room","Bullet Punch"],nature="Naive")
caitlin5=Bronzong (maxiv="Yes")
caitlin6=Gothitelle (maxiv="Yes")
caitlin7=Sigilyph(maxiv="Yes")
caitlin8=Musharna(maxiv="Yes",item="Leftovers",move=["Trick Room","Psyshock","Dazzling Gleam","Shadow Ball"])
caitlinteam=teamset([caitlin1,caitlin2,caitlin3,caitlin4,caitlin5,caitlin7,caitlin8],5)+[caitlin6]
caitlin=Trainer ("Elite Four Caitlin",caitlinteam,"Unova")
#sawyer
sawyer1=Slurpuff(maxiv="Yes")
sawyer2=Clawitzer (maxiv="Yes")
sawyer3=Aegislash (maxiv="Yes")
sawyer4=Slaking(maxiv="Yes")
sawyer5=Salamence(maxiv="Yes")
sawyer6=Sceptile (maxiv="Yes",item="Sceptilite")
sawyer=Trainer ("Pokémon Trainer Sawyer",[sawyer1,sawyer2,sawyer3,sawyer4,sawyer5,sawyer6],"Kalos")
#alder
alder1=Escavalier(maxiv="Yes", ability="Swarm",move=["X-Scissor","Giga Impact","Iron Head","Double Iron Bash"])
alder2=Conkeldurr(maxiv="Yes",item="Life Orb", ability="Sheer Force",move=["Hammer Arm","Madh Punch","Stone Edge","Bulk Up"])
alder3=Krookodile (maxiv="Yes",move=["Earthquake","Crunch","Stone Edge","Outrage"],item="Expert Belt")
alder4=Bouffalant (maxiv="Yes", ability="Sap Sipper",move=["Head Charge","Megahorn","Stone Edge","Earthquake"])
alder5=Braviary (maxiv="Yes", move=["Crush Claw","Rock Slide","Superpower","Brave Bird"],item="Choice Band")
alder6=Volcarona (maxiv="Yes",move=["Quiver Dance","Bug Buzz","Heat Wave","Psychic"], ability="Flame Body",item="Charti Berry")
alder7=Vanilluxe(maxiv="Yes", ability="Ice Body",move=["Blizzard","Acid Armor","Flash Cannon","Light Screen"])
alder8=Accelgor(maxiv="Yes", ability="Hydration",move=["Bug Buzz","Focus Blast","Energy Ball","Water Shuriken"])
alder9=Druddigon(maxiv="Yes", ability="Rough Skin", move=["Night Slash","Outrage","Superpower","Dragon Dance"])
alder10=Chandelure(maxiv="Yes",item="Choice Scarf",move=["Flamethrower","Shadow Ball","Psychic","Energy Ball"])
alder11=Reuniclus(maxiv="Yes",item="Leftovers",move=["Light Screen","Reflect","Toxic","Psychic"])
alderteam=teamset([alder1,alder2,alder3,alder4,alder5,alder7,alder8,alder9,alder10,alder11],5)+[alder6]
alder=Trainer ("Unova Champion Alder",alderteam,"Unova")
#barry
barry1=Roserade(maxiv="Yes", ability="Natural Cure",move=["Sludge Bomb","Giga Drain","Shadow Ball","Sleep Powder"],item="Black Sludge")
barry2=Staraptor(maxiv="Yes", ability="Reckless",move=["Close Combat","Brave Bird","U-turn","Double-Edge"], nature="Jolly",item="Choice Scarf")
barry3=Hitmonlee(maxiv="Yes")
barry4=Heracross(maxiv="Yes",item="Heracronite", ability="Moxie",move=["Close Combat","Rock Slide","Earthquake","Bullet Seed"])
barry5=Skarmory(maxiv="Yes")
barry6=Empoleon(maxiv="Yes",item="Shuca Berry",move=["Waterfall","Drill Peck","Aqua Jet","Protect"], ability="Defiant",atkev=252,spatkev=0)
barry7=Snorlax(move=["Crunch","Curse","Body Slam","Fire Punch"],maxiv="Yes")
barry8=Rapidash(maxiv="Yes",item="Expert Belt",move=["Smart Strike","Megahorn","Poison Jab","Flare Blitz"])
barry9=Floatzel(maxiv="Yes",move=["Ice Fang","Crunch","Waterfall","Aqua Jet"],item="Quick Claw")
barryteam=teamset([barry1,barry2,barry3,barry4,barry5,barry7,barry8,barry9],5)+[barry6]
barry=Trainer ("Rival Barry",barryteam,"Sinnoh")
#wally
wally1=Roserade(maxiv="Yes")
wally2=Azumarill (maxiv="Yes")
wally3=Garchomp(maxiv="Yes")
wally4=Magnezone(maxiv="Yes")
wally5=Altaria(maxiv="Yes")
wally6=Gallade(maxiv="Yes",item="Galladite")
wally7=Talonflame (maxiv="Yes")
wally8=Gardevoir(maxiv="Yes")
wally9=Delcatty(maxiv="Yes")
wallyteam=teamset([wally1,wally2,wally3,wally4,wally5,wally7,wally8,wally9],5)+[wally6]
wally=Trainer ("Rival Wally",wallyteam,"Hoenn")
#sina
sina1=Drampa(maxiv="Yes")
sina2=Lilligant (maxiv="Yes")
sina3=Abomasnow (maxiv="Yes")
sina4=Oranguru(maxiv="Yes")
sina5=Mandibuzz (maxiv="Yes")
sina6=Glaceon(maxiv="Yes")
sina7=Sandslash(maxiv="Yes")
sinateam=teamset([sina1,sina2,sina3,sina4,sina6,sina5,sina7])
sina=Trainer("Pokémon Trainer Sina",sinateam,"Alola")
#reggie
reggie1=Roserade(maxiv="Yes")
reggie2=Kangaskhan (maxiv="Yes")
reggie3=Swalot(maxiv="Yes")
reggie4=Bibarel(maxiv="Yes")
reggie5=Staraptor (maxiv="Yes")
reggie6=Drapion(maxiv="Yes")
reggie7=Kricketune(maxiv="Yes")
reggie8=Luxray(maxiv="Yes")
reggie9=Skuntank(maxiv="Yes")
reggie10=Cherrim(maxiv="Yes")
reggieteam=teamset([reggie1,reggie2,reggie3,reggie4,reggie5,reggie7,reggie8,reggie9,reggie10],5)+[reggie6]
reggie=Trainer ("Pokémon Trainer Reggie",reggieteam,"Sinnoh")
#paul
paul1=Honchkrow(maxiv="Yes")
paul2=Weavile(maxiv="Yes")
paul3=Gyarados (maxiv="Yes",move=["Hyper Beam","Ice Fang","Waterfall","Crunch"])
paul4=Garchomp (maxiv="Yes", move=["Dragon Claw","Stone Edge","Draco Meteor","Earthquake"])
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
paul16=Ursaluna (maxiv="Yes")
paul17=Ninjask(maxiv="Yes")
paulteam=teamset([paul7,paul2,paul3,paul4,paul5,paul1,paul8,paul9,paul10,paul11,paul12,paul13,paul14,paul15],5)+[paul6]
paul=Trainer ("Rival Paul",paulteam,"Sinnoh")
#Trevor
trevor1=Florges(maxiv="Yes")
trevor2=Aerodactyl(maxiv="Yes")
trevor3=Crawdaunt(maxiv="Yes")
trevor4=Aurorus(maxiv="Yes")
trevor5=Tyrantrum(maxiv="Yes")
trevor6=Charizard(maxiv="Yes",item="Charizardite Y",atkev=0,spatkev=252)
trevor=Trainer ("Rival Trevor",[trevor1,trevor2,trevor3,trevor4,trevor5,trevor6],"Kalos")
#hala
hala1=Kommo(maxiv="Yes")
hala2=Bewear(maxiv="Yes")
hala3=Annihilape(maxiv="Yes")
hala4=Poliwrath(maxiv="Yes")
hala5=Machamp(maxiv="Yes")
hala6=Hariyama(name="Hariyama(Z-Crystal)",maxiv="Yes")
hala7=Crabominable(maxiv="Yes")
halateam=teamset([hala1,hala2,hala3,hala4,hala5,hala6],5)+[hala7]
hala=Trainer ("Elite Four Hala",halateam,"Alola")
#molayne
molayne1=Skarmory(maxiv="Yes")
molayne2=Magnezone(maxiv="Yes")
molayne3=Metagross(maxiv="Yes",item="Metagrossite")
molayne4=Klefki(maxiv="Yes")
molayne5=Kingambit(maxiv="Yes")
molayne6=Steelix(maxiv="Yes")
molayne7=Genesect(maxiv="Yes")
molayne8=ADugtrio(name="Alolan Dugtrio(Z-Crystal)",maxiv="Yes")
molayne9=Ampharos(maxiv="Yes")
molayneteam=teamset([molayne1,molayne2,molayne3,molayne4,molayne5,molayne7,molayne6, molayne9],5)+[molayne8]
molayne=Trainer ("Elite Four Molayne", molayneteam,"Alola")
#olivia
olivia1=Relicanth(maxiv="Yes")
olivia2=Gigalith(maxiv="Yes")
olivia3=AGolem(maxiv="Yes")
olivia4=Armaldo(maxiv="Yes")
olivia5=Cradily(maxiv="Yes")
olivia6=MNLycanroc(name="Midnight Lycanroc(Z-Crystal)",maxiv="Yes")
olivia7=Probopass(maxiv="Yes")
oliviateam=teamset([olivia1,olivia2,olivia3,olivia4,olivia5,olivia7],5)+[olivia6]
olivia=Trainer ("Elite Four Olivia",oliviateam,"Alola")
#acerola
acerola1=Froslass(maxiv="Yes")
acerola2=Palossand(maxiv="Yes")
acerola3=Drifblim(maxiv="Yes")
acerola4=Dhelmise (maxiv="Yes")
acerola5=Banette (maxiv="Yes")
acerola6=Mimikyu(name="Mimikyu(Z-Crystal)",maxiv="Yes")
acerola7=Sableye(maxiv="Yes")
acerolateam=teamset([acerola1,acerola2,acerola3,acerola4,acerola5,acerola7],5)+[acerola6]
acerola=Trainer ("Elite Four Acerola",acerolateam,"Alola")
#kahili
kahili1=Skarmory (maxiv="Yes")
kahili2=Crobat(maxiv="Yes")
kahili3=Mandibuzz(maxiv="Yes")
kahili4=Hawlucha (maxiv="Yes")
kahili5=Braviary (maxiv="Yes")
kahili6=Toucannon(name="Toucannon(Z-Crystal)",maxiv="Yes")
kahili7=Oricorio(maxiv="Yes")
kahiliteam=teamset([kahili1,kahili2,kahili3,kahili4,kahili5,kahili7],5)+[kahili6]
kahili=Trainer ("Elite Four Kahili",kahiliteam,"Alola")
#odrake
odrake1=Ditto(maxiv="Yes")
odrake2=Gengar(maxiv="Yes")
odrake3=Venusaur(maxiv="Yes",item="Venusaurite")
odrake4=Steelix(maxiv="Yes")
odrake5=Electivire(maxiv="Yes")
odrake6=Dragonite(maxiv="Yes")
odrake=Trainer ("Supreme Gym Leader Drake",[odrake1,odrake2,odrake3,odrake4,odrake5,odrake6],"Orange Islands")
#Leon
leonmax=random.randint(1,4)
leon1=MrRime(maxiv="Yes")
leon2=Aegislash(maxiv="Yes",nature="Adamant",atkev=252)
leon3=Dragapult (maxiv="Yes")
leon4=Inteleon(maxiv="maz",move=[random.choice(["Hydro Pump","Snipe Shot"]),"Dark Pulse","Ice Beam","U-turn"],nature="Timid")
leon5=Rillaboom(maxiv="max",move=["Drum Beating","Acrobatics","High Horsepower","Knock Off"],item="Flying Gem")
leon6=Cinderace(maxiv="max",ability="Libero",move=["Scorching Sands","Pyro Ball","Sucker Punch","Grass Knot"])
leon7=Charizard (maxiv="max",move=["Flamethrower","Ancient Power","Air Slash","Dragon Pulse"],atkev=0,spatkev=252)
leon8=Seismitoad(maxiv="Yes")
leon9=Rhyperior(maxiv="Yes")
leonteam=teamset([leon1,leon2,leon3,leon4,leon5,leon6,leon8,leon9],5)+[leon7]
leon=Trainer("Galar Champion Leon",leonteam,"Galar")
#Benga
benga1=Emboar(maxiv="Yes")
benga2=Dragonite (maxiv="Yes")
benga3=Garchomp (maxiv="Yes")
benga4=Latias (maxiv="Yes")
benga5=Latios (maxiv="Yes")
benga6=Volcarona(maxiv="Yes")
benga=Trainer ("Boss Trainer Benga",[benga1,benga2,benga3,benga4,benga5,benga6],"Unova")
#misty
misty1=Seaking(maxiv="Yes",ability="Lightning Rod")
misty2=Starmie(maxiv="Yes")
misty3=Politoed(maxiv="Yes", ability="Drizzle")
misty4=Kingdra(maxiv="Yes")
misty5=Lapras(maxiv="Yes")
misty6=Gyarados(maxiv="Yes",item="Gyaradosite")
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
mistyteam=teamset([misty1,misty4,misty5,misty7,misty8,misty9,misty10,misty11,misty12,misty13,misty14,misty15,misty16,misty17,misty18,misty19,misty20,misty21,misty22,misty23],3)+[misty3,misty2,misty6]
misty=Trainer ("Gym Leader Misty",mistyteam,"Kanto")
#cheryl
cheryl1=Snorlax(maxiv="Yes")
cheryl2=Drifblim (maxiv="Yes")
cheryl3=Hariyama(maxiv="Yes")
cheryl4=Wobbuffet(maxiv="Yes")
cheryl5=Wailord(maxiv="Yes")
cheryl6=Blissey(maxiv="Yes")
cheryl7=Espeon(maxiv="Yes")
cheryl8=Umbreon(maxiv="Yes")
cheryl9=PorygonZ(maxiv="Yes")
cheryl10=Armaldo(maxiv="Yes")
cheryl11=Milotic(maxiv="Yes")
cheryl12=Latias(maxiv="Yes")
cheryl13=Latios(maxiv="Yes")
cheryl14=WGastrodon(maxiv="Yes")
cheryl15=Cresselia(maxiv="Yes")
cheryl16=Venusaur(maxiv="Yes")
cheryl17=Alakazam(maxiv="Yes")
cheryl18=Victreebel(maxiv="Yes")
cheryl19=Exeggutor(maxiv="Yes")
cheryl20=Starmie(maxiv="Yes")
cheryl21=Meganium (maxiv="Yes")
cheryl22=Miltank(maxiv="Yes")
cheryl23=Sceptile(maxiv="Yes")
cheryl24=Ludicolo(maxiv="Yes")
cheryl25=Shiftry(maxiv="Yes")
cheryl26=Medicham (maxiv="Yes")
cheryl27=Cradily(maxiv="Yes")
cheryl28=Walrein(maxiv="Yes")
cheryl29=Regirock(maxiv="Yes")
cheryl30=Regice(maxiv="Yes")
cheryl31=Torterra(maxiv="Yes")
cheryl32=Roserade(maxiv="Yes")
cheryl33=Vespiquen (maxiv="Yes")
cheryl34=Hippowdon(maxiv="Yes")
cheryl35=Abomasnow (maxiv="Yes")
cheryl36=Tangrowth(maxiv="Yes")
cheryl37=Dusknoir(maxiv="Yes")
cherylteam=teamset([cheryl1,cheryl2,cheryl3,cheryl4,cheryl5,cheryl7,cheryl8,cheryl9,cheryl10,cheryl11,cheryl12,cheryl13,cheryl14,cheryl15,cheryl16,cheryl17,cheryl18,cheryl19,cheryl20,cheryl21,cheryl22,cheryl23,cheryl24,cheryl25,cheryl26,cheryl27,cheryl28,cheryl29,cheryl30,cheryl31,cheryl32,cheryl33,cheryl34,cheryl35,cheryl36,cheryl37],5)+[cheryl6]
cheryl=Trainer("Pokémon Trainer Cheryl",cherylteam,"Sinnoh")
#blanche
blanche1=Mamoswine(maxiv="Yes")
blanche2=Empoleon (maxiv="Yes")
blanche3=Glaceon(maxiv="Yes")
blanche4=Suicune(maxiv="Yes")
blanche5=Metagross (maxiv="Yes")
blanche6=Articuno(maxiv="Yes")
blanche7=Walrein(maxiv="Yes")
blanche8=Castform(maxiv="Yes",item="Icy Rock")
blanche9=Weavile (maxiv="Yes")
blanche10=Gliscor(maxiv="Yes")
blanche11=Lapras(maxiv="Yes")
blanche12=ANinetales(maxiv="Yes")
blanche13=Glalie(maxiv="Yes")
blanche14=Blastoise (maxiv="Yes")
blanche15=Gyarados (maxiv="Yes")
blanche16=Milotic(maxiv="Yes")
blanche17=Slowking (maxiv="Yes")
blancheteam=teamset([blanche1,blanche2,blanche3,blanche4,blanche5,blanche7, blanche8,blanche9,blanche10,blanche11,blanche12,blanche13,blanche14,blanche15,blanche16,blanche17],5)+[blanche6]
blanche=Trainer("Mystic Leader Blanche", blancheteam,"Unknown")
#nate
nate1=Beartic(maxiv="Yes")
nate2=Archeops(maxiv="Yes")
nate3=Sawk(maxiv="Yes")
nate4=Escavalier(maxiv="Yes")
nate5=Accelgor(maxiv="Yes")
nate6=Excadrill (maxiv="Yes")
nate7=Braviary (maxiv="Yes")
nate8=Mienshao(maxiv="Yes")
nate9=Vanilluxe (maxiv="Yes")
nate10=Haxorus(maxiv="Yes")
nate11=Darmanitan(maxiv="Yes")
nate12=Golurk(maxiv="Yes")
nate13=Cryogonal (maxiv="Yes")
nate14=Reuniclus (maxiv="Yes")
nate15=Bisharp(maxiv="Yes")
nate16=Conkeldurr (maxiv="Yes")
nate17=Krookodile (maxiv="Yes")
nate18=Chandelure (maxiv="Yes")
nate19=Bouffalant (maxiv="Yes")
nate20=Eelektross (maxiv="Yes")
nate21=Druddigon (maxiv="Yes")
nate22=Audino(maxiv="Yes")
nate23=Amoongus(maxiv="Yes")
nate24=Alomomola(maxiv="Yes")
nate25=Jellicent (maxiv="Yes")
nate26=Throh (maxiv="Yes")
nate27=Cofagrigus(maxiv="Yes")
nate28=Ferrothorn (maxiv="Yes")
nate29=Mandibuzz (maxiv="Yes")
nate30=Klinklang(maxiv="Yes")
nate31=Lilligant (maxiv="Yes")
nate32=Durant(maxiv="Yes")
nate33=Gigalith (maxiv="Yes")
nate34=Gothitelle (maxiv="Yes")
nate35=Musharna(maxiv="Yes")
nate36=Scrafty(maxiv="Yes")
nate37=Arcanine(maxiv="Yes")
nate38=SShaymin(maxiv="Yes")
hilbert1=Samurott(maxiv="Yes")
hilbert2=Genesect(maxiv="Yes")
hilbert3=Mightyena(maxiv="Yes")
hilbert4=Zekrom(maxiv="Yes")
hilda1=Emboar(maxiv="Yes")
hilda2=Victini(maxiv="Yes")
hilda3=Diancie(maxiv="Yes")
hilda4=Grapploct(name="Grapploct✨",maxiv="Yes")
nateteam=teamset([nate1,nate2,nate3,nate4,nate5,nate7,nate8,nate9,nate10,nate11,nate12,nate13,nate14,nate15,nate16,nate17,nate18,nate19,nate20,nate21,nate22,nate23,nate24,nate25,nate26,nate27,nate28,nate29,nate30,nate31,nate32,nate33,nate34,nate35,nate36,nate6,nate38],5)+[nate37]
rosa=Trainer("Pokémon Trainer Rosa",nateteam,"Unova")
nate=Trainer("Pokémon Trainer Nate",nateteam,"Unova")
hildateam=teamset(nateteam+[hilda3,hilda4],4)+[hilda1,hilda2]
hilbertteam=teamset(nateteam+[hilbert3,hilbert4],4)+[hilbert1,hilbert2]
hilbert=Trainer("Pokémon Trainer Hilbert",hilbertteam,"Unova")
hilda=Trainer("Pokémon Trainer Hilda",hildateam,"Unova")
#mira
mira1=PorygonZ(maxiv="Yes")
mira2=Gengar(maxiv="Yes")
mira3=Magnezone(maxiv="Yes")
mira4=Togekiss(maxiv="Yes")
mira5=Exeggutor(maxiv="Yes")
mira6=Alakazam(maxiv="Yes")
mira7=Zapdos(maxiv="Yes")
mira8=Gardevoir(maxiv="Yes")
mira9=Magmortar(maxiv="Yes")
mira10=Armaldo(maxiv="Yes")
mira11=Glaceon(maxiv="Yes")
mira12=Latias(maxiv="Yes")
mira13=Latios(maxiv="Yes")
mira14=Moltres(maxiv="Yes")
mira15=Espeon(maxiv="Yes")
mira16=Empoleon(maxiv="Yes")
mira17=Yanmega(maxiv="Yes")
mira18=Heatran(maxiv="Yes")
mirateam=teamset([mira1,mira2,mira3,mira4,mira5,mira7,mira8,mira9,mira10,mira11,mira12,mira13,mira14,mira15,mira16,mira17,mira18],5)+[mira6]
mira=Trainer("Pokémon Trainer Mira",mirateam,"Sinnoh")
#riley
riley1=Absol(maxiv="Yes")
riley2=Ursaring(maxiv="Yes")
riley3=Metagross(maxiv="Yes")
riley4=Salamence(maxiv="Yes")
riley5=Poliwrath(maxiv="Yes")
riley6=Lucario(maxiv="Yes")
riley7=Machamp(maxiv="Yes")
riley8=Rhyperior(maxiv="Yes")
riley9=Gyarados(maxiv="Yes")
riley10=Dragonite(maxiv="Yes")
riley11=Heracross(maxiv="Yes")
riley12=Tyranitar(maxiv="Yes")
riley13=Blaziken(maxiv="Yes")
riley14=Breloom(maxiv="Yes")
riley15=Slaking(maxiv="Yes")
riley16=Hariyama(maxiv="Yes")
riley17=Medicham(maxiv="Yes")
riley18=Infernape(maxiv="Yes")
riley19=Rampardos(maxiv="Yes")
riley20=Garchomp(maxiv="Yes")
riley21=Toxicroak(maxiv="Yes")
riley22=Mamoswine(maxiv="Yes")
riley23=Gallade(maxiv="Yes")
riley24=Regigigas(maxiv="Yes")
riley25=Pinsir(maxiv="Yes")
riley26=Entei(maxiv="Yes")
rileyteam=teamset([riley1,riley2,riley3,riley4,riley5,riley7,riley8,riley9,riley10,riley11,riley12,riley13,riley14,riley15,riley16,riley17,riley18,riley19,riley20,riley21,riley22,riley23,riley24,riley25,riley26],5)+[riley6]
riley=Trainer("Pokémon Trainer Riley",rileyteam,"Sinnoh")
#surge
surge1=Ampharos(maxiv="Yes")
surge2=Jolteon(maxiv="Yes")
surge3=Magnezone(maxiv="Yes")
surge4=Electivire(maxiv="Yes")
surge5=Electrode(maxiv="Yes")
surge6=Raichu(maxiv="Yes")
surge7=Manectric(maxiv=random.choice(["Ice","Grass"]),item="Manectite",move=["Volt Switch","Flamethrower","Thunderbolt","Hidden Power"],nature="Timid")
surge8=Lanturn(maxiv="Yes")
surge9=Zapdos(maxiv="Ice",move=["Discharge","Heat Wave","Hidden Power","Roost"],item=random.choice(["Leftovers","Rocky Helmet"]),nature="Bold")
surgeteam=teamset([surge1,surge2,surge3,surge4,surge5,surge7,surge8,surge9],5)+[surge6]
surge=Trainer ("Gym Leader Lt.Surge",surgeteam,"Kanto")
#blainehc
blainehc1=Heliolisk(maxiv="Yes", ability="Solar Power",item="Focus Sash",nature="Timid",move=["Boomburst","Weather Ball","Thunderbolt","Solar Beam"])
blainehc2=Groudon(name="Primal Groudon✨",maxiv="Yes", nature="Naive",move=["Precipice Blades","Fire Blast","Stone Edge","Solar Beam"],item="Red Orb")
blainehc3=GDarmanitan(maxiv="Yes", ability="Zen Mode",nature="Jolly",move=["Mountain Gale","Flare Blitz","U-turn","Rock Slide"],item="Ice Gem")
blainehc4=Venusaur (maxiv="Yes", ability="Chlorophyll", nature="Modest",item="Focus Sash",move=["Growth","Solar Beam","Sludge Bomb","Weather Ball"])
blainehc5=Hooh(maxiv="Yes",name="Ho-Oh(Z-Crystal)",nature="Jolly",move=["Sacred Fire","Brave Bird","Earthquake","Solar Beam"])
blainehc6=Charizard(maxiv="Yes",nature="Jolly",move=["Dragon Dance","Flare Blitz","Dragon Claw","Earthquake"],item="Charizardite X",atkev=252,spatkev=0)
blainehcteam=teamset([blainehc1,blainehc2,blainehc3,blainehc4,blainehc5],5)+[blainehc6]
blainehc=Trainer ("Blaine(Hardcore Mode)",blainehcteam,"Kanto")
#erika
erika1=Jumpluff(maxiv="Yes", ability="Chlorophyll",move=["U-turn","Sleep Powder","Giga Drain","Air Slash"])
erika2=Bellossom(name="Bellossom(Z-Crystal)",maxiv="Yes", ability="Chlorophyll",move=["Sunny Day","Solar Beam","Giga Drain","Weather Ball"])
erika3=Tangrowth(maxiv="Ice", ability="Regenerator", item="Assault Vest",move=[random.choice(["Hidden Power","Sludge Bomb"]),"Giga Drain","Earthquake","Knock Off"])
erika4=Victreebel(maxiv="Yes", ability="Chlorophyll",move=["Swords Dance","Sucker Punch","Leaf Blade","Reflect"],item="Salac Berry")
erika5=Vileplume(maxiv="Yes", ability="Chlorophyll",move=["Petal Dance","Sleep Powder","Sunny Day","Moonlight"],item="Grass Gem")
erika6=Venusaur(maxiv="Yes",item="Venusaurite",move=["Weather Ball","Giga Drain","Earth Power","Sludge Bomb"], ability="Chlorophyll")
erika7=Shiftry(maxiv="Yes", ability="Chlorophyll",move=["Leaf Storm","Sucker Punch","Sunny Day","Explosion"])
erika8=Roserade(maxiv="Yes", ability="Natural Cure",move=["Weather Ball","Energy Ball","Sludge Bomb","Sunny Day"])
erika9=Exeggutor(maxiv="Yes",item="Tanga Berry",move=["Psyshock","Solar Beam","Hypnosis","Sunny Day"], ability="Chlorophyll")
erika10=Cradily(maxiv="Yes", ability="Suction Cups",item="Leftovers",move=["Curse","Recover","Seed Bomb","Stone Edge"])
erika11=Abomasnow(maxiv="Yes", ability="Snow Warning",move=["Leech Seed","Protect","Blizzard","Sheer Cold"],item="Focus Sash")
erika12=Parasect(maxiv="Yes")
erika13=Leafeon(maxiv="Yes")
erika14=Lilligant(maxiv="Yes")
erika15=Whimsicott(maxiv="Yes",item="Mental Herb", ability="Prankster",move=["Tailwind","Taunt","Giga Drain","Leech Seed"])
erikateam=teamset([erika1,erika2,erika3,erika4,erika7,erika8,erika9,erika10,erika11,erika12,erika13,erika14,erika15],4)+[erika5,erika6]
erika=Trainer ("Gym Leader Erika",erikateam,"Kanto")
erikah1=Tsareena (ability="Striker",maxiv="Yes",nature="Adamant",item="Focus Sash",move=["Triple Axel","Trop Kick","High Jump Kick","Rapid Spin"])
erikah2=Hawlucha (ability="Unburden",nature="Adamant",maxiv="Yes",item="Grassy Seed",move=["Swords Dance","Close Combat","Acrobatics","Roost"])
erikah3=Bellossom (ability="Chlorophyll",maxiv="Yes",item="Leftovers",nature="Timid",move=["Sleep Powder","Quiver Dance","Giga Drain","Fiery Dance"])
erikah4=Rillaboom(ability="Grassy Surge",maxiv="Yes",item="Grassy Seed",nature="Timid",move=["Grassy Glide","Swords Dance","Acrobatics","High Horsepower"])
erikah5=Serperior (ability="Contrary",maxiv="Yes",item="Focus Sash",nature="Timid",move=["Leaf Storm","Dragon Pulse","Giga Drain","Leech Life"])
erikah6=Venusaur (ability="Thick Fat",maxiv="Yes",item="Venusaurite",nature="Modest",move=["Giga Drain","Synthesis","Sludge Bomb","Earth Power"])
erikah=Trainer("Erika(Hard Mode)",[erikah1,erikah2,erikah3,erikah4,erikah5,erikah6],"Kanto")
erikahc1=Cradily(ability="Storm Drain",maxiv="Yes",nature="Relaxed",item="Grassy Seed",move=["Stealth Rock","Toxic","Power Whip","Earth Power"])
erikahc2=Hawlucha (ability="Unburden",nature="Adamant",maxiv="Yes",item="Grassy Seed",move=["Swords Dance","Close Combat","Acrobatics","Stone Edge"])
erikahc3=GSlowbro(ability="Regenerator",maxiv="Yes",item="Black Sludge",nature="Bold",move=["Thunder Wave","Sludge Bomb","Flamethrower","Teleport"])
erikahc4=Kartana(ability="Beast Boost",item="Life Orb",maxiv="Yes",nature="Jolly",move=["Grassy Glide","Swords Dance","Smart Strike","Sacred Sword"])
erikahc5=Toxtricity(ability="Punk Rock",maxiv="Yes",item="Life Orb",nature="Timid",move=["Boomburst","Hidden Power","Volt Switch","Overdrive"])
erikahc6=Sceptile(ability="Technician",maxiv="Yes",item="Sceptilite",nature="Jolly",move=["Swords Dance","Bullet Seed","Draco Barrage","High Horsepower"])
erikahc=Trainer("Erika(Hardcore Mode)",[erikahc1,erikahc2,erikahc3,erikahc4,erikahc5,erikahc6],"Kanto")
#sabrina
sabrina1=Venomoth(maxiv="Yes")
sabrina2=MrMime(maxiv="Yes", item="Kasib Berry")
sabrina3=Espeon(maxiv="Yes", move=["Psyshock","Psychic","Signal Beam","Calm Mind"], item="Leftovers")
sabrina4=Jynx(maxiv="Yes",item="Salac Berry")
sabrina5=Wobbuffet(maxiv="Yes")
sabrina6=Alakazam(maxiv="Yes",item="Alakazite",move=["Focus Blast","Psychic","Shadow Ball","Nasty Plot"], ability="Inner Focus")
sabrina7=Gallade(maxiv="Yes")
sabrina8=Lanturn(maxiv="Yes")
sabrina9=Slowking (maxiv="Yes",move=["Psychic","Shadow Ball","Focus Blast","Scald"],item="Choice Specs", ability="Oblivious")
sabrina10=Hypno(maxiv="Yes",item="Sitrus Berry",move=["Hypnosis","Dream Eater","Shadow Ball","Calm Mind"])
sabrina11=Metagross (maxiv="Yes",item="Expert Belt")
sabrina12=Exeggutor(maxiv="Yes",item="Tanga Berry")
sabrina13=Mewtwo(maxiv="Yes")
sabrina14=Gengar(maxiv="Yes")
sabrina15=Xatu(maxiv="Yes")
sabrina16=Sigilyph (maxiv="Yes",item="Life Orb",move=["Psychic","Air Slash","Ice Beam","Light Screen"])
sabrina17=Swoobat(maxiv="Yes")
sabrinateam=teamset([sabrina1,sabrina2,sabrina3,sabrina4,sabrina5,sabrina7,sabrina8,sabrina9,sabrina10,sabrina11,sabrina12,sabrina13,sabrina14,sabrina15, sabrina16, sabrina17],5)+[sabrina6]
sabrina=Trainer ("Gym Leader Sabrina",sabrinateam,"Kanto")
#koga
koga1=Ariados(maxiv="Yes",move=["Sticky Web","Megahorn","Poison Jab","Night Shade"], ability="Insomnia")
koga2=Venomoth(maxiv="Yes",move=["Sludge Bomb","Giga Drain","Psychic","Bug Buzz"])
koga3=Crobat(name="Crobat(Z-Crystal)",maxiv="Yes",move=["Sky Attack","Cross Poison","Toxic","Poison Jab"], ability="Inner Focus")
koga4=Weezing(maxiv="Yes",move=["Fire Blast","Thunder","Toxic","Sludge Bomb"])
koga5=Skuntank(maxiv="Yes",move=["Sucker Punch","Flamethrower","Explosion","Sludge Bomb"], ability="Aftermath")
koga6=Muk(maxiv="Yes",move=["Dark Pulse","Moonblast","Giga Drain","Sludge Bomb"])
koga7=Toxicroak(maxiv="Yes", ability="Dry Skin",move=["X-Scissor","Cross Chop","Gunk Shot","Drain Punch"])
koga8=Forretress(maxiv="Yes",move=["Explosion","Protect","Toxic Spikes","Spikes"], ability="Sturdy")
koga9=Tentacruel (maxiv="Yes",move=["Sludge Bomb","Giga Drain","Toxic","Hydro Pump"])
koga14=Swalot (maxiv="Yes",move=["Amnesia","Sludge Bomb","Pain Split","Yawn"], ability="Sticky Hold",item="Leftovers")
kogateam=teamset([koga1,koga2,koga3,koga4,koga5,koga7,koga8,koga9,koga14],5)+[koga6]
koga=Trainer ("Elite Four Koga",kogateam,"Kanto")
#Guzma
Guzma1=Ariados(maxiv="Yes")
Guzma2=Masquerain (maxiv="Yes")
Guzma3=Pinsir(maxiv="Yes")
Guzma4=Scizor(maxiv="Yes")
Guzma5=Vikavolt(maxiv="Yes")
Guzma6=Golisopod(maxiv="Yes")
Guzma7=Toxapex(maxiv="Yes")
Guzma8=Kingambit(maxiv="Yes")
Guzma9=Honchkrow(name="Honchkrow (Z-Crystal)",maxiv="Yes")
Guzma10=Liepard(maxiv="Yes")
Guzma11=Buzzwole(maxiv="Yes")
Guzmateam=teamset([Guzma1,Guzma2,Guzma3,Guzma4,Guzma5,Guzma7,Guzma8,Guzma9,Guzma10,Guzma11],5)+[Guzma6]
Guzma=Trainer ("Skull Leader Guzma",Guzmateam,"Alola")
#blaine
blaine1=Arcanine(maxiv="Yes",item="Focus Sash",move=["Flare Blitz","Extreme Speed","Close Combat","Wild Charge"],nature="Adamant", ability="Intimidate")
blaine2=Ninetales(maxiv="Yes", ability="Drought",item="Heat Rock",move=["Fire Blast","Solar Beam","Psyshock","Will-O-Wisp"],nature="Modest")
blaine3=Rapidash(maxiv="Yes",item="Shuca Berry",move=["Flare Blitz","Wild Charge","Megahorn","Hypnosis"], ability="Flash Fire")
blaine4=Magcargo(maxiv="Yes", ability="Flame Body",move=["Curse","Gyro Ball","Overheat","Stone Edge"])
blaine6=Magmortar(maxiv="Yes",item="Choice Scarf",move=["Fire Blast","Psychic","Thunderbolt","Focus Blast"])
blaine7=Torkoal(maxiv="Yes", ability="Drought",item="Heat Rock",move=["Explosion","Yawn","Lava Plume","Stealth Rock"])
blaine8=Camerupt(maxiv="Yes",move=["Eruption","Earthquake","Solar Beam","Rock Slide"])
blaine9=Houndoom(maxiv="Yes",move=["Dark Pulse","Flamethrower","Shadow Ball","Sucker Punch"], ability="Flash Fire")
blaine10=Charizard(maxiv="Grass",move=["Air Slash","Flamethrower","Focus Blast","Hidden Power"],nature="Modest",item="Charizardite Y",atkev=0,spatkev=252)
blaine11=Flareon(maxiv="Yes",item="Passho Berry",move=["Overheat","Superpower","Toxic","Quick Attack"])
blaine13=Typhlosion (maxiv="Grass", ability="Blazing Soul",item="Choice Specs",move=["Eruption","Flamethrower","Hidden Power","Focus Blast"],nature="Modest")
blaine12=Moltres(name="Moltres(Z-Crystal)",maxiv="Yes",nature="Mild",item="Bright Powder",move=["Fire Blast","Hyper Beam","Hurricane","Roost"])
blaine14=HRotom(maxiv="Yes",item="Flame Orb",move=["Trick","Thunderbolt","Overheat","Pain Split"])
blaine15=Rhydon(maxiv="Yes")
blaine16=Kangaskhan(maxiv="Yes")
blaine17=Entei(maxiv="Yes")
blaine18=Mewtwo(maxiv="Yes",item=random.choice(["Mewtwonite X","Mewtwonite Y"]))
blaineteam=teamset([blaine2,blaine3,blaine4,blaine7,blaine8,blaine9,blaine1,blaine11,blaine12,blaine13,blaine14,blaine15,blaine16,blaine10,blaine17,blaine18],4)+[blaine6]
blaine=Trainer ("Gym Leader Blaine",blaineteam,"Kanto")
#bugsy
bugsy1=Butterfree(maxiv="Yes")
bugsy2=Yanmega(maxiv="Yes")
bugsy3=Pinsir(maxiv="Yes")
bugsy4=Vespiquen(maxiv="Yes")
bugsy5=Heracross(name="Heracross(Z-Crystal)",maxiv="Yes")
bugsy6=Beedrill(maxiv="Yes",item="Beedrillite")
bugsy7=Scizor(maxiv="Yes")
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
whitney6=Miltank(maxiv="Yes")
whitney7=Clefable(name="Clefable(Z-Crystal)",maxiv="Yes")
whitney8=Blissey(maxiv="Yes")
whitney9=Lopunny(maxiv="Yes",item="Lopunnite")
whitney10=Cinccino(maxiv="Yes")
whitney11=Watchog (maxiv="Yes")
whitneyteam=teamset([whitney1,whitney2,whitney3,whitney4,whitney5,whitney8,whitney7,whitney10,whitney11],4)+[whitney6,whitney9]
whitney=Trainer ("Gym Leader Whitney",whitneyteam,"Johto")
#morty
morty1=Drifblim(maxiv="Yes")
morty2=Mismagius(name="Mismagius(Z-Crystal)",maxiv="Yes")
morty3=Dusknoir(maxiv="Yes")
morty4=Banette(maxiv="Yes")
morty5=Froslass(maxiv="Yes")
morty6=Cofagrigus(maxiv="Yes")
morty7=Clefable(maxiv="Yes")
morty8=Jellicent(maxiv="Yes")
morty10=Hooh(maxiv="Yes")
morty9=Gengar(maxiv="Yes",item="Gengarite")
mortyteam=teamset([morty1,morty6,morty3,morty4,morty5,morty8,morty7,morty10],4)+[morty2,morty9]
morty=Trainer ("Gym Leader Morty",mortyteam,"Johto")
#will
will1=Exeggutor(maxiv="Fire",move=["Solar Beam","Psychic","Ancient Power","Hidden Power"], ability="Chlorophyll",item="Lum Berry",nature="Hardy")
will2=Jynx(maxiv="Fire",move=["Hidden Power","Ice Beam","Psychic","Hypnosis"],item="Lum Berry",ability="Oblivious")
will3=Bronzong(maxiv="Yes", ability="Levitate",item="Leftovers",nature=random.choice(["Careful","Sassy"]),move=["Stealth Rock","Earthquake","Toxic",random.choice(["Heavy Slam","Gyro Ball"])])
will4=Grumpig(maxiv="Yes", ability="Thick Fat",nature="Impish",item="Leftovers",move=["Toxic","Protect","Psychic","Fire Punch"])
will5=Xatu(maxiv="Yes", ability="Early Bird",item="Lum Berry",nature="Adamant",atkev=252, move=["Calm Mind","Giga Drain","Psychic","Drill Peck"])
will6=Slowbro(maxiv="Yes",item="Slowbronite",move=["Slack Off","Surf","Calm Mind","Thunder Wave"],nature="Mild", ability="Shell Armor")
will8=Gardevoir(maxiv="Yes",item="Gardevoirite",move=["Psychic","Thunderbolt","Moonblast","Focus Blast"], ability="Modest")
will9=Farigiraf(maxiv="Yes", ability="Armor Tail",nature="Naive",item="Lum Berry",move=["Earthquake","Twin Beam","Body Slam","Signal Beam"])
willteam=teamset([will1,will2,will3,will4,will9,will6,will8],5)+[will5]
will=Trainer ("Elite Four Will",willteam,"Johto")
#cilan
cilan1=Whimsicott(maxiv="Yes")
cilan2=Jumpluff(maxiv="Yes")
cilan3=Maractus(maxiv="Yes")
cilan4=Ferrothorn (maxiv="Yes")
cilan5=Simisage(maxiv="Yes")
cilan6=Lilligant(maxiv="Yes")
cilan7=Serperior(maxiv="Yes")
cilanteam=teamset([cilan1,cilan2,cilan3,cilan4,cilan7,cilan6],5)+[cilan5]
cilan=Trainer ("Gym Leader Cilan",cilanteam,"Unova")
#chili
chili1=Camerupt(maxiv="Yes")
chili2=Arcanine (maxiv="Yes")
chili3=Heatmor(maxiv="Yes")
chili4=Darmanitan(maxiv="Yes")
chili5=Simisear(maxiv="Yes")
chili6=Magmortar(maxiv="Yes")
chili7=Emboar(maxiv="Yes")
chiliteam=teamset([chili1,chili2,chili3,chili4,chili7,chili6],5)+[chili5]
chili=Trainer ("Gym Leader Chili",chiliteam,"Unova")
#cress
cress1=Slowking (maxiv="Yes")
cress2=Azumarill (maxiv="Yes")
cress3=Floatzel (maxiv="Yes")
cress4=Golduck (maxiv="Yes")
cress5=Simipour(maxiv="Yes")
cress6=Basculegion (maxiv="Yes")
cress7=Samurott (maxiv="Yes")
cressteam=teamset([cress1,cress2,cress3,cress4,cress7,cress6],5)+[cress5]
cress=Trainer ("Gym Leader Cress",cressteam,"Unova")
#chuck
chuck1=Primeape(maxiv="Yes")
chuck2=Poliwrath(maxiv="Yes")
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
jasmine2=Empoleon(maxiv="Yes")
jasmine3=Metagross(maxiv="Yes")
jasmine4=Bronzong(maxiv="Yes")
jasmine5=Magnezone(maxiv="Yes")
jasmine6=Steelix(maxiv="Yes",item="Steelixite")
jasmine7=Mawile(maxiv="Yes")
jasmine8=Lucario(maxiv="Yes")
jasmine9=Ferrothorn(maxiv="Yes")
jasmine10=Excadrill(maxiv="Yes")
jasmine11=Forretress(maxiv="Yes")
jasmine12=Ampharos (maxiv="Yes")
jasmine13=Celesteela(maxiv="Yes")
jasmineteam=teamset([jasmine1,jasmine2,jasmine3,jasmine4,jasmine5,jasmine7,jasmine8,jasmine9,jasmine10,jasmine11, jasmine13,jasmine12],5)+[jasmine6]
jasmine=Trainer ("Gym Leader Jasmine",jasmineteam,"Johto")
#pryce
pryce1=Walrein(maxiv="Yes")
pryce2=Froslass(maxiv="Yes")
pryce3=Glalie(maxiv="Yes")
pryce4=Abomasnow(maxiv="Yes",item="Abomasite")
pryce5=Dewgong(maxiv="Yes")
pryce6=Mamoswine(maxiv="Yes")
pryce7=Jynx(maxiv="Yes")
pryce8=Lapras(maxiv="Yes")
pryce9=Weavile(maxiv="Yes")
pryce10=Cloyster(maxiv="Yes")
pryceteam=teamset([pryce1,pryce2,pryce3,pryce4,pryce5,pryce6,pryce7,pryce8,pryce9,pryce10],6)
pryce=Trainer ("Gym Leader Pryce",pryceteam,"Johto")
#clair
clair2=Aerodactyl(maxiv="Yes")
clair3=Charizard(maxiv="Yes")
clair4=Gyarados(maxiv="Yes")
clair5=Dragonite(maxiv="Yes")
clair6=Kingdra(maxiv="Yes")
clair7=Altaria(maxiv="Yes")
clair8=Salamence(maxiv="Yes")
clair9=Druddigon(maxiv="Yes")
clair1=Garchomp(maxiv="Yes")
clairteam=teamset([clair1,clair2,clair3,clair4,clair5,clair6,clair7,clair8,clair9],6)
clair=Trainer ("Gym Leader Clair",clairteam,"Johto")
#zinnia
zinnia2=Goodra(maxiv="Yes")
zinnia3=Altaria(maxiv="Yes")
zinnia4=Tyrantrum (maxiv="Yes")
zinnia5=Salamence (maxiv="Yes",item="Salamencite")
zinnia6=Rayquaza (maxiv="Yes")
zinnia1=Noivern(maxiv="Yes")
zinniateam=teamset([zinnia1,zinnia2,zinnia3,zinnia4],4)+[zinnia5,zinnia6]
zinnia=Trainer ("Lorekeeper Zinnia",zinniateam,"Hoenn")
#roxanne
roxanne2=Aerodactyl(maxiv="Yes")
roxanne3=Kabutops(maxiv="Yes")
roxanne4=Omastar(maxiv="Yes")
roxanne5=Golem(maxiv="Yes")
roxanne6=Steelix(maxiv="Yes")
roxanne7=Probopass(maxiv="Yes")
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
brawly6=Hariyama(maxiv="Yes")
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
winona6=Altaria(maxiv="Yes",item="Altarianite")
winona7=Noctowl(maxiv="Yes")
winona1=Dragonite(maxiv="Yes")
winona8=Honchkrow(maxiv="Yes")
winona9=Gyarados(maxiv="Yes")
winona10=Rayquaza(maxiv="Yes")
winonateam=teamset([winona1,winona2,winona3,winona4,winona5,winona7,winona8,winona9,winona10],5)+[winona6]
winona=Trainer ("Gym Leader Winona",winonateam,"Hoenn")
#wattson
wattson2=Electivire(maxiv="Yes")
wattson3=Electrode(maxiv="Yes")
wattson4=Raichu(maxiv="Yes")
wattson5=Ampharos(maxiv="Yes")
wattson6=Manectric(maxiv=random.choice(["Ice","Grass"]),item="Manectite",move=["Volt Switch","Flamethrower","Thunderbolt","Hidden Power"], ability="Intimidate",nature="Timid")
wattson7=Magnezone(maxiv="Fire",item="Air Balloon", ability="Magnet Pull",move=["Hidden Power","Flash Cannon","Thunderbolt","Iron Defense"])
wattson1=WRotom(maxiv="Yes",item="Choice Scarf",move=["Volt Switch","Trick","Hydro Pump","Thunder Wave"],nature="Bold")
wattsonteam=teamset([wattson1,wattson2,wattson3,wattson4,wattson5,wattson7],5)+[wattson6]
wattson=Trainer ("Gym Leader Wattson",wattsonteam,"Hoenn")
#flannery
flannery2=Torkoal(maxiv="Yes", ability="Drought",item="Heat Rock",move=["Eruption","Explosion","Stone Edge","Earthquake"])
flannery3=Houndoom(maxiv="Yes",item="Life Orb",move=["Will-O-Wisp","Sucker Punch","Overheat","Fire Blast"])
flannery4=Rapidash(maxiv="Yes", ability="Flash Fire",move=["Flamethrower","Solar Beam","Fire Blast","Scorching Sands"])
flannery5=Magcargo(maxiv="Yes",item="Shuca Berry",move=["Earth Power","Ancient Power","Lava Plume","Shell Smash"])
flannery6=Camerupt(maxiv="Yes",move=["Yawn","Fire Blast","Earth Power","Rock Slide"],item="Camerupite")
flannery7=Blaziken(maxiv="Yes", ability="Blaze",move=["High Jump Kick","Flare Blitz","Brave Bird","Bulk Up"],item="Salac Berry")
flannery1=Magmortar(maxiv="Yes", ability="Flame Body",item="Shuca Berry",move=["Psychic","Armor Cannon","Thunderbolt","Fire Blast"])
flannery8=Chandelure(maxiv="Yes",item="Focus Sash",move=["Shadow Ball","Calm Mind","Flamethrower","Will-O-Wisp"])
flanneryteam=[flannery2]+teamset([flannery1,flannery3,flannery4,flannery5,flannery6,flannery7,flannery8],5)
flannery=Trainer ("Gym Leader Flannery",flanneryteam,"Hoenn")
#norman
norman2=Tauros(maxiv="Yes")
norman3=Kangaskhan(maxiv="Yes")
norman4=Linoone(maxiv="Yes")
norman5=Zangoose(maxiv="Yes")
norman6=Slaking(maxiv="Yes",item="Chople Berry")
norman7=Exploud(maxiv="Yes")
norman1=Blissey(maxiv="Yes")
norman8=Staraptor(maxiv="Yes")
norman9=Ambipom(maxiv="Yes")
norman10=Bouffalant (maxiv="Yes",item="Lum Berry")
norman11=Stoutland(maxiv="Yes",item="Sitrus Berry")
norman12=Sawsbuck(maxiv="Yes",item="Occa Berry")
norman13=Spinda(maxiv="Yes")
normanteam=teamset([norman1,norman2,norman3,norman4,norman5,norman7,norman8,norman9,norman10,norman11,norman12,norman13],5)+[norman6]
norman=Trainer ("Gym Leader Norman",normanteam,"Hoenn")
#tate
tate2=Bronzong (maxiv="Yes")
tate3=Claydol(maxiv="Yes")
tate4=Grumpig(maxiv="Yes")
tate5=Xatu(maxiv="Yes")
tate6=Solrock(maxiv="Yes")
tate1=Reuniclus(maxiv="Yes")
tate7=Gallade(maxiv="Yes",item="Galladite")
tateteam=teamset([tate1,tate2,tate3,tate4,tate5,tate7],5)+[tate6]
tate=Trainer ("Gym Leader Tate",tateteam,"Hoenn")
#liza
liza2=Bronzong(maxiv="Yes")
liza3=Claydol(maxiv="Yes")
liza4=Grumpig(maxiv="Yes")
liza5=Xatu(maxiv="Yes")
liza6=Lunatone(maxiv="Yes")
liza1=Gothitelle(maxiv="Yes")
liza7=Gardevoir(maxiv="Yes",item="Gardevoirite")
lizateam=teamset([liza1,liza2,liza3,liza4,liza5,liza7],5)+[liza6]
liza=Trainer ("Gym Leader Liza",lizateam,"Hoenn")
#juan
juan2=Whiscash(maxiv="Yes")
juan3=Crawdaunt(maxiv="Yes")
juan4=Walrein(maxiv="Yes")
juan5=Politoed(maxiv="Yes")
juan6=Kingdra(maxiv="Yes")
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
roark5=Rampardos(maxiv="Yes")
roark6=Tyranitar(maxiv="Yes")
roark7=Golem(maxiv="Yes")
roark8=Archeops(maxiv="Yes")
roark9=Sudowoodo(maxiv="Yes")
roark10=Salamence(maxiv="Yes")
roark11=Lunatone(maxiv="Yes")
roark12=Torkoal(maxiv="Yes")
roark13=Slowbro(maxiv="Yes")
roarkteam=teamset([roark1,roark2,roark3,roark4,roark7,roark8,roark9,roark10,roark11,roark12,roark13],4)+[roark6,roark5]
roark=Trainer("Gym Leader Roark",roarkteam,"Sinnoh")
#hop
hop1=Trevenant(maxiv="Yes")
hop2=Boltund(maxiv="Yes")
hop3=Heatmor(maxiv="Yes")
hop4=Snorlax(maxiv="Yes")
hop5=Dubwool(maxiv="Yes")
hop6=Zacian(maxiv="Yes")
hop7=Zamazenta(maxiv="Yes")
hop8=Inteleon(maxiv="Yes")
hop9=Cinderace(maxiv="Yes")
hop10=Rillaboom(maxiv="Yes")
hop11=Corviknight(maxiv="Yes")
hop12=Toxtricity(maxiv="Yes")
hop13=Pincurchin (maxiv="Yes")
hop14=GZapdos(maxiv="Yes")
hop15=Cramorant (maxiv="Yes")
hopteam=teamset([hop1,hop2,hop3,hop4,hop5,hop11,hop12,hop13,hop14,hop15],4)+teamset([hop8,hop9,hop10],1)+teamset([hop6,hop7],1)
hop=Trainer("Pokémon Trainer Hop",hopteam,"Galar")
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
#shauna
shauna1=Delcatty (maxiv="Yes")
shauna2=Goodra(maxiv="Yes")
shauna3=Florges(maxiv="Yes")
shauna4=Slurpuff(maxiv="Yes")
shauna5=Gothitelle (maxiv="Yes")
shauna6=Venusaur(maxiv="Yes",item="Venusaurite")
shauna7=Sylveon(maxiv="Yes")
shauna8=Delphox(maxiv="Yes")
shauna9=Greninja(maxiv="Yes")
shauna10=Chesnaught (maxiv="Yes")
shaunateam=teamset([shauna1,shauna2,shauna3,shauna4,shauna5,shauna7],4)+teamset([shauna8,shauna9,shauna10],1)+[shauna6]
shauna=Trainer("Pokémon Trainer Shauna",shaunateam,"Kalos")
#tierno
tierno1=Crawdaunt (maxiv="Yes")
tierno2=Hitmontop(maxiv="Yes")
tierno3=Raichu(maxiv="Yes")
tierno4=Ludicolo(maxiv="Yes")
tierno5=Politoed (maxiv="Yes")
tierno6=Blastoise(maxiv="Yes",item="Blastoisinite")
tierno7=Hawlucha(maxiv="Yes")
tierno8=Roserade(maxiv="Yes")
tierno9=Talonflame (maxiv="Yes")
tiernoteam=teamset([tierno1,tierno2,tierno3,tierno4,tierno5,tierno7,tierno8, tierno9],5)+[tierno6]
tierno=Trainer("Pokémon Trainer Tierno",tiernoteam,"Kalos")
#faba
faba1=Ledian(maxiv="Yes")
faba2=Bruxish (maxiv="Yes")
faba3=Slowbro (maxiv="Yes")
faba4=Hypno (maxiv="Yes")
faba5=ARaichu(maxiv="Yes")
faba6=Alakazam (maxiv="Yes")
faba7=Claydol(maxiv="Yes")
fabateam=teamset([faba2,faba3,faba4,faba5,faba1,faba7],5)+[faba6]
faba=Trainer ("Aether Foundation Faba",fabateam,"Alola")
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
lusamine10=DMNecrozma(name="Dusk Mane Necrozma(Z-Crystal)",maxiv="Yes")
lusamine11=Pheromosa(maxiv="Yes")
lusamineteam=teamset([lusamine2,lusamine3,lusamine4,lusamine5,lusamine1,lusamine7,lusamine8,lusamine9, lusamine11, lusamine10],5)+[lusamine6]
lusamine=Trainer ("Aether President Lusamine",lusamineteam,"Alola")
#gardenia
gardenia1=Jumpluff(maxiv="Yes")
gardenia2=Roserade(maxiv="Yes",item="Focus Sash")
gardenia3=Bellossom(maxiv="Yes")
gardenia4=Cherrim(maxiv="Yes")
gardenia5=Tangrowth(maxiv="Yes")
gardenia6=Torterra(maxiv="Yes",item=random.choice(["Yache Berry","Life Orb"]))
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
fantina4=Gengar(maxiv="Yes",item="Gengarite")
fantina5=Spiritomb(maxiv="Yes")
fantina6=Mismagius(maxiv="Yes")
fantina7=Jellicent(maxiv="Yes")
fantina8=Giratina(maxiv="Yes",item="Griseous Core")
fantina9=Froslass(maxiv="Yes")
fantina10=Shedinja(maxiv="Yes")
fantina11=Dragonite (maxiv="Yes")
fantina12=Crawdaunt(maxiv="Yes")
fantina13=Sableye(maxiv="Yes")
fantinateam=teamset([fantina1,fantina5,fantina3,fantina4,fantina7,fantina8,fantina9,fantina10,fantina11,fantina12,fantina13],4)+[fantina2,fantina6]
fantina=Trainer("Gym Leader Fantina",fantinateam,"Sinnoh")
#byron
byron1=Aggron(maxiv="Yes")
byron2=Skarmory(maxiv="Yes")
byron3=Magnezone(maxiv="Yes")
byron4=Bronzong (maxiv="Yes")
byron5=Steelix(maxiv="Yes",item="Steelixite")
byron6=Bastiodon(maxiv="Yes")
byron7=Excadrill(maxiv="Yes")
byron8=Empoleon (maxiv="Yes")
byron9=Metagross(maxiv="Yes")
byron10=Scizor(maxiv="Yes")
byron11=Kabutops(maxiv="Yes")
byron12=Cradily(maxiv="Yes")
byron13=Armaldo(maxiv="Yes")
byron14=Omastar(maxiv="Yes")
byron15=Heatran(maxiv="Yes")
byron16=Moltres(maxiv="Yes")
byron17=Pelipper(maxiv="Yes", ability="Drizzle")
byronteam=teamset([byron1,byron2,byron3,byron4,byron7,byron8,byron9,byron10,byron11,byron12,byron13,byron14,byron15],4)+[byron5,byron6]
byron=Trainer("Gym Leader Byron",byronteam,"Sinnoh")    
#maylene
maylene1=Infernape(maxiv="Yes")
maylene2=Breloom(maxiv="Yes")
maylene3=Hitmontop(maxiv="Yes")
maylene4=Machamp(maxiv="Yes")
maylene5=Medicham(maxiv="Yes")
maylene6=Lucario(maxiv="Yes", item="Lucarionite")
maylene7=Gallade(maxiv="Yes")
maylene8=Toxicroak(maxiv="Yes")
maylene9=Heracross(maxiv="Yes")
maylene10=Blaziken(maxiv="Yes")
maylene11=Empoleon (maxiv="Yes")
maylene12=Dragonite (maxiv="Yes")
mayleneteam=teamset([maylene5,maylene2,maylene3,maylene4,maylene7,maylene8,maylene9,maylene10,maylene11,maylene12],4)+[maylene1,maylene6]
maylene=Trainer("Gym Leader Maylene",mayleneteam,"Sinnoh")
#wake
wake1=Floatzel(maxiv="Yes")
wake2=Quagsire(maxiv="Yes")
wake3=Sharpedo(maxiv="Yes")
wake4=Ludicolo(maxiv="Yes")
wake5=Empoleon(maxiv="Yes")
wake6=Gyarados(maxiv="Yes",item="Gyaradosite")
wake7=Lumineon(maxiv="Yes")
wake8=WGastrodon(maxiv="Yes")
wake9=Poliwrath(maxiv="Yes")
wake10=Kingdra(maxiv="Yes")
wake11=Politoed(maxiv="Yes", ability="Drizzle")
wake12=Huntail(maxiv="Yes")
wake13=Suicune(maxiv="Yes")
wake14=Swampert (maxiv="Yes")
wake15=Armaldo(maxiv="Yes")
wake16=Scizor(maxiv="Yes")
wake17=Pelipper(maxiv="Yes", ability="Drizzle")
waketeam=teamset([wake5,wake2,wake3,wake4,wake7,wake8,wake9,wake10,wake11,wake12,wake13,wake14,wake15,wake16,wake17],4)+[wake1,wake6]
wake=Trainer("Gym Leader Crasher Wake",waketeam,"Sinnoh")
#candice
candice1=Froslass(maxiv="Yes")
candice2=Weavile(maxiv="Yes")
candice3=Mamoswine(maxiv="Yes")
candice4=Glaceon(maxiv="Yes")
candice5=Glalie(maxiv="Yes")
candice6=Abomasnow(maxiv="Yes",item="Abomasite")
candice7=Medicham(maxiv="Yes")
candice8=Jynx(maxiv="Yes")
candice9=Regice(maxiv="Yes")
candice10=Lapras(maxiv="Yes")
candice11=Cloyster(maxiv="Yes")
candice12=Articuno(maxiv="Yes")
candice13=Heatran(maxiv="Yes")
candice14=Venusaur(maxiv="Yes")
candiceteam=teamset([candice5,candice2,candice3,candice4,candice7,candice8,candice9,candice10,candice11,candice12],4)+[candice1,candice6]
candice=Trainer("Gym Leader Candice",candiceteam,"Sinnoh")
#volkner
volkner1=Luxray(maxiv="Yes",item="Sitrus Berry", ability="Intimidate")
volkner2=Raichu(maxiv="Yes",item=random.choice(["Shuca Berry","Choice Scarf"]))
volkner3=Ambipom(maxiv="Yes",item="Chople Berry", ability="Technician")
volkner4=Octillery(maxiv="Yes",item="Expert Belt")
volkner5=Jolteon(maxiv="Yes",item=random.choice(["Air Balloon","Life Orb"]))
volkner6=Electivire(maxiv="Yes",item=random.choice(["Shuca Berry","Life Orb"]))
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
lenora1=Watchog(maxiv="Yes")
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
burgh6=Leavanny(maxiv="Yes")
burgh7=Heracross(maxiv="Yes")
burghteam=teamset([burgh5,burgh2,burgh3,burgh4,burgh7],4)+[burgh1,burgh6]
burgh=Trainer("Gym Leader Burgh",burghteam,"Unova")
#elesa
elesa1=Ampharos(maxiv="Yes",item="Amoharosite")
elesa2=Galvantula(maxiv="Yes")
elesa3=Eelektross(maxiv="Yes")
elesa4=Luxray(maxiv="Yes")
elesa5=Vikavolt(maxiv="Yes")
elesa6=Zebstrika(maxiv="Yes")
elesa7=Manectric(maxiv="Yes")
elesa8=Emolga(maxiv="Yes")
elesateam=teamset([elesa1,elesa5,elesa2,elesa3,elesa4,elesa7],4)+[elesa8,elesa6]
elesa=Trainer("Gym Leader Elesa",elesateam,"Unova")
#clemont
clemont1=Manectric(maxiv="Yes")
clemont2=Luxray(maxiv="Yes")
clemont3=Emolga(maxiv="Yes")
clemont4=Magnezone(maxiv="Yes")
clemont5=Ampharos(maxiv="Yes",item="Amoharosite")
clemont6=Heliolisk(maxiv="Yes")
clemontteam=teamset([clemont2,clemont3,clemont4,clemont5,clemont1],5)+[clemont6]
clemont=Trainer ("Gym Leader Clemont",clemontteam,"Kalos")
#clay
clay1=Excadrill(maxiv="Yes")
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
skyla6=Swanna(maxiv="Yes")
skyla7=Jumpluff(maxiv="Yes")
skyla8=Drifblim(maxiv="Yes")
skyla9=TTornadus(maxiv="Yes")
skyla10=Togekiss(maxiv="Yes")
skylateam=teamset([skyla5,skyla2,skyla3,skyla4,skyla7,skyla8,skyla9,skyla10],4)+[skyla1,skyla6]
skyla=Trainer("Gym Leader Skyla",skylateam,"Unova")
#brycen
brycen1=Vanilluxe(maxiv="Yes")
brycen2=Weavile(maxiv="Yes")
brycen3=Dewgong (maxiv="Yes")
brycen4=Walrein(maxiv="Yes")
brycen5=Mandibuzz (maxiv="Yes")
brycen6=Beartic(maxiv="Yes")
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
drayden6=Haxorus(maxiv="Yes")
draydenteam=teamset([drayden5,drayden2,drayden3,drayden4],4)+[drayden1,drayden6]
drayden=Trainer("Gym Leader Drayden",draydenteam,"Unova")
#iris
iris1=Druddigon(maxiv="Yes")
iris2=Salamence(maxiv="Yes")
iris3=Archeops(maxiv="Yes")
iris4=Hydreigon (maxiv="Yes")
iris5=Excadrill(maxiv="Yes")
iris6=Haxorus(maxiv="Yes")
iris7=Emolga(maxiv="Yes")
iris8=Dragonite(maxiv="Yes")
iris9=Garchomp(maxiv="Yes")
iris10=Lapras(maxiv="Yes")
iris11=Aggron(maxiv="Yes")
iris12=Naganadel(maxiv="Yes")
iristeam=teamset([iris5,iris2,iris3,iris4,iris7,iris8,iris9,iris10,iris11,iris12],4)+[iris1,iris6]
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
cheren12=Lopunny (maxiv="Yes",item="Lopunnite")
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
roxie6=Scolipede(maxiv="Yes")
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
quillon4=Honchkrow(maxiv="Yes")
quillon6=DUrshifu(maxiv="Yes")
quillonteam=teamset([quillon2,quillon3,quillon4,quillon5],4)+[quillon1,quillon6]
quillon=Trainer("Project Mew: Quillon",quillonteam,"Galar")      
#marlon
marlon1=Carracosta(maxiv="Yes")
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
diantha3=Tyrantrum(maxiv="Yes", ability="Strong Jaw",move=["Head Smash","Earthquake","Dragon Claw","Crunch"])
diantha6=Gardevoir(maxiv="Yes",move=["Thunderbolt","Psychic","Moonblast","Shadow Ball"],item="Gardevoirite")
diantha4=Aurorus(maxiv="Yes", ability="Refrigerate",move=["Thunder","Blizzard","Light Screen","Reflect"])
diantha5=Gourgeist(maxiv="Yes",move=["Seed Bomb","Phantom Force","Shadow Sneak","Trick-or-Treat"])
diantha7=Diancie(maxiv="Yes")
diantha8=Keldeo(maxiv="Yes")
dianthateam=teamset([diantha2,diantha3,diantha4,diantha5,diantha7,diantha8],4)+[diantha1,diantha6]
diantha=Trainer("Kalos Champion Diantha",dianthateam,"Kalos")    
#grant
grant4=Golem(maxiv="Yes")
grant2=Steelix(maxiv="Yes")
grant3=Bastiodon(maxiv="Yes")
grant6=Tyrantrum(maxiv="Yes")
grant1=Aurorus(maxiv="Yes")
grant5=Rampardos(maxiv="Yes")
grantteam=teamset([grant2,grant3,grant4,grant5],4)+[grant1,grant6]
grant=Trainer("Gym Leader Grant",grantteam,"Kalos")    
#danika
danika1=Azumarill (maxiv="Yes")
danika2=Barraskewda(maxiv="Yes")
danika3=Jellicent(maxiv="Yes")
danika5=Drednaw(maxiv="Yes")
danika4=Inteleon(maxiv="Yes")
danika6=WUrshifu(maxiv="Yes")
danikateam=teamset([danika2,danika3,danika4,danika5],4)+[danika1,danika6]
danika=Trainer("Project Mew: Danika",danikateam,"Galar")    
#viola
viola1=Dustox(maxiv="Yes")
viola2=Beautifly(maxiv="Yes")
viola3=Mothim(maxiv="Yes")
viola4=Butterfree(maxiv="Yes")
viola5=Masquerain(maxiv="Yes")
viola6=Vivillon(maxiv="Yes")
violateam=teamset([viola2,viola3,viola4,viola5,viola1],5)+[viola6]
viola=Trainer ("Gym Leader Viola",violateam,"Kalos")
#ash
ash1=Infernape(maxiv="Yes", ability="Blaze")
ash2=Dragonite(maxiv="Yes")
ash3=Charizard(maxiv="Yes", ability="Blaze",nature="Adamant", move=["Flamethrower","Dual Wingbeat","Slash","Dragon Tail"])
ash4=Lucario(maxiv="Yes",item="Lucarionite", ability="Inner Focus",move=["Double Team","Aura Sphere","Bullet Punch","Reversal"])
ash5=Gengar(maxiv="Yes", ability="Cursed Body")
ash6=Pikachu(name="Pikachu(Z-Crystal)",move=["Thunderbolt","Electroweb","Quick Attack","Iron Tail"],maxiv="Yes", ability="Static")
ash7=Sceptile(maxiv="Yes", ability="Overgrow")
ash8=Staraptor(maxiv="Yes")
ash9=Tauros(maxiv="Yes")
ash10=Snorlax (maxiv="Yes",move=["Rest","Ice Punch","Hyper Beam","Body Slam"])
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
cissy5=Blastoise(maxiv="Yes",item="Blastoisinite")
cissy6=Kingler(maxiv="Yes")
cissy=Trainer ("Gym Leader Cissy",[cissy1,cissy2,cissy3,cissy4,cissy5,cissy6],"Orange Islands")
#horace
horace1=Meganium (maxiv="Yes")
horace2=Virizion(maxiv="Yes")
horace3=Heracross(maxiv="Yes")
horace5=Donphan(maxiv="Yes")
horace4=Indeedee(maxiv="Yes")
horace6=Gardevoir(maxiv="Yes",item="Gardevoirite")
horaceteam=teamset([horace2,horace3,horace4,horace5],4)+[horace1,horace6]
horace=Trainer("Project Mew: Horace",horaceteam,"Johto")    
#danny
danny1=Pinsir(maxiv="Yes")
danny2=Electrode(maxiv="Yes")
danny3=Golem(maxiv="Yes")
danny4=Nidoqueen(maxiv="Yes")
danny5=Scizor(maxiv="Yes",item="Scizorite")
danny6=Machamp(maxiv="Yes")
danny=Trainer ("Gym Leader Danny",[danny1,danny2,danny3,danny4,danny5,danny6],"Orange Islands")
#rudy
rudy1=Pidgeot(maxiv="Yes",item="Pidgeotite")
rudy2=Electivire(maxiv="Yes")
rudy3=Golem(maxiv="Yes")
rudy4=Exeggutor(maxiv="Yes")
rudy5=Alakazam(maxiv="Yes",item="Alakazite")
rudy6=Starmie(maxiv="Yes")
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
luana5=Alakazam(maxiv="Yes",item="Alakazite")
luana6=Marowak(maxiv="Yes")
luanateam=teamset([luana2,luana3,luana4,luana5,luana1],5)+[luana6]
luana=Trainer ("Gym Leader Luana",luanateam,"Orange Islands")
#larry
larry1=Tropius(maxiv="Yes")
larry2=Staraptor(maxiv="Yes")
larry3=Altaria(maxiv="Yes",item="Altarianite")
larry4=Kilowattrel(maxiv="Yes")
larry5=Bombirdier(maxiv="Yes")
larry6=Flamigo(name="Flamigo",maxiv="Flying")
larry7=Dudunsparce(maxiv="Yes")
larry8=Braviary(maxiv="Yes")
larry9=Oricorio(maxiv="Yes",type1="Electric(")
larry10=Komala(maxiv="Yes")
larry11=Oinkologne (maxiv="Yes")
larryteam=teamset([larry2,larry3,larry4,larry5,larry1,larry7,larry8,larry9,larry10,larry11],5)+[larry6]
larry=Trainer ("Elite Four Larry",larryteam,"Paldea")
#hassel
hassel1=Noivern (maxiv="Yes", ability="Infiltrator",move=["Air Slash","Dragon Pulse","Super Fang","Boomburst"])
hassel2=Dragalge(maxiv="Yes",move=["Sludge Bomb","Dragon Pulse","Hydro Pump","Thunderbolt"])
hassel3=Flapple(maxiv="Yes",ability="Ripen", move=["Dragon Rush","Seed Bomb","Leech Seed","Acrobatics"])
hassel4=Haxorus(maxiv="Yes", ability="Mold Breaker",move=["Dragon Claw","Crunch","Iron Head","Rock Tomb"])
hassel5=Dragonite(maxiv="Yes", ability="Inner Focus",move=["Extreme Speed","Dragon Rush","Fire Punch","Stone Edge"])
hassel6=Baxcalibur(name="Baxcalibur",maxiv="Dragon", ability="Thermal Exchange",move=["Icicle Crash","Brick Break","Glaive Rush","Ice Shard"])
hasselteam=teamset([hassel2,hassel3,hassel4,hassel5,hassel1],5)+[hassel6]
hassel=Trainer ("Elite Four Hassel",hasselteam,"Paldea")
#poppy
poppy1=Bronzong(maxiv="Yes",move=["Iron Defense","Zen Headbutt","Rock Blast","Earthquake"], ability="Levitate")
poppy2=Copperajah(maxiv="Yes",move=["High Horsepower","Heavy Slam","Stealth Rock","Play Rough"], ability="Sheer Force")
poppy3=Magnezone(maxiv="Fire",move=["Discharge","Flash Cannon","Light Screen","Hidden Power"], ability="Sturdy")
poppy4=Corviknight(maxiv="Yes", ability="Pressure",move=["Brave Bird","Iron Head","Iron Defense","Body Press"])
poppy5=Gholdengo(maxiv="Yes")
poppy6=Tinkaton(maxiv="Steel",move=["Play Rough","Gigaton Hammer","Brick Break","Stone Edge"])
poppyteam=teamset([poppy2,poppy3,poppy4,poppy5,poppy1],5)+[poppy6]
poppy=Trainer ("Elite Four Poppy",poppyteam,"Paldea")
#geeta
geeta1=Gogoat(maxiv="Yes", ability="Sap Sipper",move=["Horn Leech","Zen Headbutt","Play Rough","Bulk Up"])
geeta2=Espathra(maxiv="Yes", ability="Opportunist",move=["Lumina Crash","Dazzling Gleam","Extreme Speed","Reflect"])
geeta3=Veluza(maxiv="Yes", ability="Mold Breaker",move=["Aqua Jet","Liquidation","Psycho Cut","Ice Fang"])
geeta4=Avalugg(maxiv="Yes", ability="Own Tempo", move=["Earthquake","Crunch","Body Press","Icicle Crash"])
geeta5=Kingambit(maxiv="Yes", ability="Supreme Overload",move=["Iron Head","Kowtow Cleave","Stone Edge","Zen Headbutt"])
geeta6=Glimmora(name="Glimmora",maxiv="Rock", ability="Toxic Debris",move=["Tera Blast","Sludge Wave","Earth Power","Dazzling Gleam"])
geetateam=teamset([geeta2,geeta3,geeta4,geeta5,geeta1],5)+[geeta6]
geeta=Trainer ("Paldea Champion Geeta",geetateam,"Paldea")
#korrina
korrina1=Chesnaught(maxiv="Yes")
korrina2=Pangoro(maxiv="Yes")
korrina3=Hawlucha(maxiv="Yes")
korrina4=Mienshao(maxiv="Yes")
korrina5=Machamp(maxiv="Yes")
korrina6=Lucario(maxiv="Yes",item="Lucarionite")
korrina7=Marshadow(maxiv="Yes")
korrinateam=teamset([korrina2,korrina3,korrina4,korrina5,korrina1,korrina7],5)+[korrina6]
korrina=Trainer ("Gym Leader Korrina",korrinateam,"Kalos")
#ramos
ramos1=Exeggutor(maxiv="Yes")
ramos2=Sunflora(maxiv="Yes")
ramos3=Victreebel(maxiv="Yes")
ramos4=Jumpluff(maxiv="Yes")
ramos5=Venusaur(maxiv="Yes",item="Venusaurite")
ramos6=Gogoat(maxiv="Yes")
ramos7=Vileplume(maxiv="Yes")
ramos8=Bellossom(maxiv="Yes")
ramosteam=teamset([ramos2,ramos3,ramos4,ramos5,ramos1,ramos7,ramos8],5)+[ramos6]
ramos=Trainer ("Gym Leader Ramos",ramosteam,"Kalos")
#valerie
valerie1=Togekiss(maxiv="Yes")
valerie2=Azumarill(maxiv="Yes")
valerie3=Florges(maxiv="Yes")
valerie4=MrMime(maxiv="Yes")
valerie5=Mawile(maxiv="Yes", item="Mawilite")
valerie6=Sylveon(maxiv="Yes")
valerieteam=teamset([valerie2,valerie3,valerie4,valerie5,valerie1],5)+[valerie6]
valerie=Trainer ("Gym Leader Valerie",valerieteam,"Kalos")
#kogah
kogah1=Swellow(maxiv="Yes",item="Choice Specs", ability="Aerilate",nature="Timid",move=["Boomburst","U-turn","U-turn","Boomburst"])
kogah2=Accelgor(maxiv="Yes",item="Life Orb", ability="Sheer Force",nature="Timid",move=["Bug Buzz","U-turn","Focus Blast","Sludge Bomb"])
kogah3=Drapion(maxiv="Yes",item="Choice Scarf", ability="Sniper",nature="Jolly",move=["Wicked Blow","Cross Poison","Wicked Blow","Cross Poison"])
kogah4=Greninja(maxiv="Yes",item="Life Orb", ability="Battle Bond",nature="Timid",move=["Surf","Water Shuriken","Dark Pulse","Ice Beam"])
kogah5=Dragapult(maxiv="Yes", item="Life Orb", ability="Infiltrator",nature="Timid",move=["Shadow Ball","Flamethrower","Dragon Pulse","U-turn"],spatkev=252,atkev=0)
kogah6=Toxtricity(maxiv="Yes",item="Throat Spray", ability="Punk Rock",nature="Timid",move=["Volt Switch","Boomburst","Sludge Bomb","Overdrive"])
kogahteam=teamset([kogah2,kogah3,kogah4,kogah5,kogah1],5)+[kogah6]
kogah=Trainer ("Koga(Hard Mode)",kogahteam,"Kanto")
#olympia
olympia1=Reuniclus(maxiv="Yes", ability="Magic Guard")
olympia2=Malamar(maxiv="Yes", ability="Contrary")
olympia3=Meowstic(maxiv="Yes")
olympia4=Delphox(maxiv="Yes", ability="Magic Guard")
olympia5=Slowking(maxiv="Yes")
olympia6=Meowstic(maxiv="Yes")
olympiateam=teamset([olympia2,olympia3,olympia4,olympia5,olympia1],5)+[olympia6]
olympia=Trainer ("Gym Leader Olympia",olympiateam,"Kalos")
#wulfric
wulfric1=GDarmanitan(maxiv="Yes")
wulfric2=Beartic(maxiv="Yes")
wulfric3=Aurorus(maxiv="Yes")
wulfric4=Cryogonal(maxiv="Yes")
wulfric5=Abomasnow(maxiv="Yes",item="Abomasite")
wulfric6=Avalugg(maxiv="Yes")
wulfricteam=teamset([wulfric2,wulfric3,wulfric4,wulfric6,wulfric1],5)+[wulfric5]
wulfric=Trainer ("Gym Leader Wulfric",wulfricteam,"Kalos")
#milo
milo1=Tsareena(maxiv="Yes")
milo2=Bellossom(maxiv="Yes")
milo3=Cherrim(maxiv="Yes")
milo4=Shiftry(maxiv="Yes")
milo5=Eldegoss(maxiv="Yes")
milo6=Flapple(maxiv="Yes")
milo7=Appletun(maxiv="Yes")
milo8=Ludicolo(maxiv="Yes")
miloteam=teamset([milo2,milo3,milo4,milo5,milo1,milo8],5)+teamset([milo6,milo7],1)
milo=Trainer ("Gym Leader Milo",miloteam,"Galar")
#nessa
nessa1=Pelipper(maxiv="Yes", ability="Drizzle",item="Damp Rock")
nessa2=Quagsire(maxiv="Yes")
nessa3=Golisopod(maxiv="Yes")
nessa4=Seaking(maxiv="Yes")
nessa5=Barraskewda(maxiv="Yes")
nessa6=Drednaw(maxiv="Yes")
nessa7=Toxapex(maxiv="Yes")
nessa8=Milotic(maxiv="Yes")
nessateam=teamset([nessa2,nessa3,nessa4,nessa5,nessa1,nessa8,nessa7],5)+[nessa6]
nessa=Trainer ("Gym Leader Nessa",nessateam,"Galar")
#kabu
kabu1=Typhlosion(maxiv="Yes",nature=random.choice(["Modest","Timid"]), ability="Blazing Soul")
kabu2=Torkoal(maxiv="Yes", ability="Drought",item="Heat Rock")
kabu3=Salazzle(maxiv="Yes")
kabu4=Ninetales(maxiv="Yes", ability="Drought",item="Heat Rock",nature=random.choice(["Modest","Timid"]))
kabu5=Arcanine(maxiv="Yes")
kabu6=Centiskorch(maxiv="Yes")
kabuteam=teamset([kabu2,kabu3,kabu4,kabu5,kabu1],5)+[kabu6]
kabu=Trainer ("Gym Leader Kabu",kabuteam,"Galar")
#bea
bea1=Hawlucha(maxiv="Yes")
bea2=Grapploct(maxiv="Yes")
bea3=Hitmontop(maxiv="Yes")
bea4=Pangoro(maxiv="Yes")
bea5=Sirfetchd(maxiv="Yes")
bea6=Machamp(maxiv="Yes")
beateam=teamset([bea2,bea3,bea4,bea5,bea1],5)+[bea6]
bea=Trainer ("Gym Leader Bea",beateam,"Galar")
#rose
rose1=Klinklang(maxiv="Yes")
rose2=Perrserker(maxiv="Yes")
rose3=Escavalier (maxiv="Yes")
rose4=Ferrothorn (maxiv="Yes")
rose5=Eternatus(maxiv="Yes")
rose6=Copperajah(maxiv="Yes")
roseteam=teamset([rose1,rose2,rose3,rose4,rose5],5)+[rose6]
rose=Trainer ("Chairman Rose",roseteam,"Galar")
#allister
allister1=Chandelure(maxiv="Yes")
allister2=Dusknoir(maxiv="Yes")
allister3=Polteageist(maxiv="Yes")
allister4=Runerigus(maxiv="Yes")
allister5=Mimikyu(maxiv="Yes")
allister6=Gengar(maxiv="Yes")
allister7=Dragapult(maxiv="Yes")
allisterteam=teamset([allister2,allister3,allister4,allister5,allister1,allister7],5)+[allister6]
allister=Trainer ("Gym Leader Allister",allisterteam,"Galar")
#lysandre
lysandre1=Mienshao(maxiv="Yes")
lysandre2=Honchkrow(maxiv="Yes")
lysandre3=Pyroar(maxiv="Yes")
lysandre4=Gyarados(name="Gyarados✨",maxiv="Yes",item="Gyaradosite")
lysandre5=CZygarde(maxiv="Yes")
lysandre6=Yveltal(maxiv="Yes")
lysandre7=Xerneas(maxiv="Yes")
lysandre8=Volcanion(maxiv="Yes")
lysandreteam=teamset([lysandre2,lysandre3,lysandre4,lysandre1,lysandre5,lysandre8],5)+teamset([lysandre6,lysandre7],1)
lysandre=Trainer ("Flare Boss Lysandre",lysandreteam,"Kalos")
#mable
mable1=Delphox(maxiv="Yes")
mable2=Talonflame(maxiv="Yes")
mable3=Malamar(maxiv="Yes")
mable4=Pangoro(maxiv="Yes")
mable5=Weavile(maxiv="Yes")
mable6=Houndoom(maxiv="Yes",item="Houndoominite")
mableteam=teamset([mable2,mable3,mable4,mable5,mable1],5)+[mable6]
mable=Trainer ("Team Flare Mable", mableteam,"Kalos")
#giallo
giallo1=Tornadus(maxiv="Yes")
giallo2=Thundurus(maxiv="Yes")
giallo3=Landorus(maxiv="Yes")
giallo4=Mandibuzz(maxiv="Yes")
giallo5=Hydreigon(maxiv="Yes")
giallo6=Krookodile(maxiv="Yes")
gialloteam=teamset([giallo2,giallo3,giallo4,giallo5,giallo1],5)+[giallo6]
giallo=Trainer ("Plasma Sage Giallo",gialloteam,"Unova")
#opal
opal1=GRapidash(maxiv="Yes")
opal2=Primarina(maxiv="Yes")
opal3=Mawile(maxiv="Yes",item="Mawilite")
opal4=GWeezing(maxiv="Yes")
opal5=Togekiss(maxiv="Yes")
opal6=Alcremie(maxiv="Yes")
opalteam=teamset([opal2,opal3,opal4,opal5,opal1],5)+[opal6]
opal=Trainer ("Gym Leader Opal",opalteam,"Galar")
#xadv
xadv1=Kangaskhan(maxiv="Yes")
xadv2=Chesnaught (maxiv="Yes")
xadv3=Charizard(maxiv="Yes")
xadv4=Manectric(maxiv="Yes")
xadv5=Gengar(maxiv="Yes")
xadv6=Pinsir(maxiv="Yes")
xadvteam=teamset([xadv2,xadv6,xadv4,xadv5,xadv1],5)+[xadv3]
xadv=Trainer ("Pokémon Trainer X",xadvteam,"Kalos")
#bede
bede1=GRapidash(maxiv="Yes")
bede2=Gardevoir(maxiv="Yes")
bede3=Mawile(maxiv="Yes",item="Mawilite")
bede4=Reuniclus(maxiv="Yes")
bede5=Gothitelle(maxiv="Yes")
bede6=Hatterene(maxiv="gmax")
bede7=Sylveon(maxiv="Yes")
bede8=GArticuno(maxiv="Yes")
bedeteam=teamset([bede2,bede3,bede4,bede5,bede1,bede7,bede8],5)+[bede6]
bede=Trainer ("Gym Leader Bede",bedeteam,"Galar")
#gordie
gordie1=Aggron(maxiv="Yes")
gordie2=Stonjourner(maxiv="Yes")
gordie3=Tyranitar(maxiv="Yes",item="Tyranitarite")
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
marnie7=GMoltres(maxiv="Yes")
marnie8=Mawile(maxiv="Yes")
marnieteam=teamset([marnie2,marnie3,marnie4,marnie5,marnie1,marnie7,marnie8],5)+[marnie6]
marnie=Trainer ("Gym Leader Marnie",marnieteam,"Galar")
#raihan
raihan1=Turtonator(maxiv="Yes")
raihan2=Goodra(maxiv="Yes")
raihan3=Gigalith(maxiv="Yes")
raihan4=Sandaconda(maxiv="gmax")
raihan5=Flygon(maxiv="Yes")
raihan6=Duraludon(maxiv="gmax")
raihan7=Torkoal(maxiv="Yes")
raihanteam=teamset([raihan2,raihan3,raihan4,raihan5,raihan1,raihan7],5)+[raihan6]
raihan=Trainer ("Gym Leader Raihan",raihanteam,"Galar")
#nemona
nemona1=MDLycanroc(maxiv="Yes")
nemona2=Goodra(maxiv="Yes")
nemona3=Orthworm(maxiv="Steel")
nemona4=Dudunsparce(maxiv="Yes")
nemona5=Skeledirge(maxiv="Yes")
nemona6=Meowscarada(maxiv="Yes")
nemona7=Quaquaval(maxiv="Yes")
nemonateam=teamset([nemona2,nemona6,nemona4,nemona5,nemona1,nemona7],5)+[nemona3]
nemona=Trainer ("Pokémon Trainer Nemona",nemonateam,"Paldea")
#katy
katy1=Lokix(maxiv="Yes",move=["Axe Kick","Sucker Punch","Lunge","Bounce"], ability="Swarm")
katy2=Forretress(maxiv="Yes",move=["Gyro Ball","Curse","Stone Edge","Lunge"])
katy3=Heracross(maxiv="Yes",move=["Megahorn","Close Combat","Stone Edge","Night Slash"])
katy4=Spidops(maxiv="Yes",move=["Skitter Smack","Throat Chop","Brick Break","Silk Trap"])
katy5=Kleavor(maxiv="Yes")
katy6=Ursaring(name="Ursaring",maxiv="Bug",move=["Play Rough","Lunge","High Horsepower","Crunch"])
katyteam=teamset([katy2,katy3,katy4,katy5,katy1],5)+[katy6]
katy=Trainer ("Gym Leader Katy",katyteam,"Paldea")
#brassius
brassius1=Lilligant(maxiv="Yes",move=["Quiver Dance","Light Screen","Hyper Beam","Petal Blizzard"])
brassius2=Tsareena(maxiv="Yes",move=["Trop Kick","High Jump Kick","Play Rough","Zen Headbutt"])
brassius3=Breloom(maxiv="Yes",move=["Mach Punch","Seed Bomb","Spore","Thunder Punch"])
brassius4=Arboliva(maxiv="Yes",move=["Energy Ball","Leech Seed","Grassy Terrain","Tera Blast"], ability="Seed Sower")
brassius5=Rillaboom(maxiv="Yes")
brassius6=Sudowoodo(name="Sudowoodo",maxiv="Grass",move=["Trailblaze","Stone Edge","Ice Punch","Fire Punch"], ability="Sturdy")
brassiusteam=teamset([brassius2,brassius3,brassius4,brassius5,brassius1],5)+[brassius6]
brassius=Trainer ("Gym Leader Brassius",brassiusteam,"Paldea")
#Iono
Iono1=Kilowattrel(maxiv="Yes",move=["Hurricane","Quick Attack","Discharge","Tailwind"], ability="Wind Power")
Iono2=Dracozolt(maxiv="Yes")
Iono3=Bellibolt(maxiv="Yes",move=["Thunder","Reflect","Sucker Punch","Hydro Pump"])
Iono4=Electrode(maxiv="Yes",move=["Foul Play","Electric Terrain","Discharge","Sucker Punch"], ability="Static")
Iono5=Luxray(maxiv="Yes", ability="Intimidate",move=["Crunch","Wild Charge","Psychic Fangs","Ice Fang"])
Iono6=Mismagius(name="Mismagius",maxiv="Electric",move=["Shadow Ball","Mystical Fire","Dazzling Gleam","Thunderbolt"])
Ionoteam=teamset([Iono2,Iono3,Iono4,Iono5,Iono1],5)+[Iono6]
Iono=Trainer ("Gym Leader Iono",Ionoteam,"Paldea")
#kofu
kofu1=Veluza(maxiv="Yes",move=["Aqua Jet","Aqua Cutter","Night Slash","Psycho Cut"], ability="Mold Breaker")
kofu2=Clawitzer(maxiv="Yes", ability="Mega Launcher",move=["Dark Pulse","Dragon Pulse","Hydro Pump","Aura Sphere"])
kofu3=Pelipper(maxiv="Yes", ability="Drizzle",move=["Hurricane","Blizzard","Surf","Quick Attack"])
kofu4=Wugtrio(maxiv="Yes", ability="Gooey",move=["Triple Dive","Throat Chop","Sucker Punch","Stomping Tantrum"])
kofu5=Basculegion(maxiv="Yes")
kofu6=Crabominable(name="Crabominable",maxiv="Water",ability="Iron Fist",move=["Crabhammer","Ice Hammer","Close Combat","Zen Headbutt"])
kofuteam=teamset([kofu2,kofu3,kofu4,kofu5,kofu1],5)+[kofu6]
kofu=Trainer ("Gym Leader Kofu",kofuteam,"Paldea")
#ryme
ryme1=Mimikyu(maxiv="Yes",move=["Light Screen","Shadow Sneak","Slash","Play Rough"])
ryme2=Banette(maxiv="Yes",move=["Icy Wind","Sucker Punch","Shadow Sneak","Phantom Force"])
ryme3=Spiritomb(maxiv="Yes",move=["Protect","Sucker Punch","Curse","Will-O-Wisp"])
ryme4=Houndstone(maxiv="Yes",move=["Play Rough","Crunch","Ice Fang","Phantom Force"])
ryme5=HTyphlosion(maxiv="Yes")
ryme6=Toxtricity(name="Toxtricity",maxiv="Ghost",move=["Overdrive","Hex","Boomburst","Sludge Bomb"])
rymeteam=teamset([ryme2,ryme3,ryme4,ryme5,ryme1],5)+[ryme6]
ryme=Trainer ("Gym Leader Ryme",rymeteam,"Paldea")
#grusha
grusha1=Frosmoth(maxiv="Yes")
grusha2=Beartic(maxiv="Yes")
grusha3=Weavile(maxiv="Yes")
grusha4=Cetitan(maxiv="Yes")
grusha5=HAvalugg(maxiv="Yes")
grusha6=Altaria(name="Altaria",maxiv="Ice")
grushateam=teamset([grusha2,grusha3,grusha4,grusha5,grusha1],5)+[grusha6]
grusha=Trainer ("Gym Leader Grusha",grushateam,"Paldea")
#tulip
tulip1=Farigiraf(maxiv="Yes")
tulip2=Gallade(maxiv="Yes")
tulip3=Espathra(maxiv="Yes")
tulip4=Gardevoir(maxiv="Yes")
tulip5=Wyrdeer(maxiv="Yes")
tulip6=Florges(name="Florges",maxiv="Psychic")
tulipteam=teamset([tulip2,tulip3,tulip4,tulip5,tulip1],5)+[tulip6]
tulip=Trainer ("Gym Leader Tulip",tulipteam,"Paldea")
#gorm
gorm1=Sigilyph(maxiv="Yes")
gorm2=Mandibuzz(maxiv="Yes")
gorm3=Hydreigon(maxiv="Yes")
gorm4=Kingambit(maxiv="Yes")
gorm5=Banette(maxiv="Yes",item="Banettite")
gorm6=Cofagrigus(maxiv="Yes")
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
gladion1=Zoroark(maxiv="Yes",move=["Night Daze","Hyper Voice","Grass Knot","Foul Play"])
gladion2=Crobat(maxiv="Yes", ability="Inner Focus",move=["Acrobatics","X-Scissor","Steel Wing","Cross Poison"])
gladion3=Weavile(maxiv="Yes",move=["Ice Shard","Night Slash","Brick Break","Shadow Claw"])
gladion4=MNLycanroc(name="Midnight Lycanroc(Z-Crystal)",maxiv=random.choice(["Yes","Rock","Dragon"]),move=["Stone Edge","Swords Dance","Outrage","Crunch"])
gladion5=Lucario(maxiv="Yes",item="Lucarionite",move=["Aura Sphere","Flash Cannon","Psychic","Extreme Speed"],spatkev=252, ability="Inner Focus")
gladion6=Silvally(maxiv="Yes",move=["Crunch","Multi-Attack","Crush Claw","X-Scissor"])
gladion7=Venusaur(maxiv="Yes",move=["Petal Blizzard","Sludge Bomb","Earthquake","Outrage"],atkev=252)
gladion8=Charizard(maxiv="Yes",move=["Air Slash","Flamethrower","Outrage","Earthquake"], atkev=252)
gladion9=Blastoise(maxiv="Yes",move=["Surf","Ice Beam","Earthquake","Outrage"],atkev=252)
gladion10=Nihilego(name="Lille✨",maxiv="Yes")
gladion11=PorygonZ(maxiv="Yes",move=["Dark Pulse","Ice Beam","Thunderbolt","Hyper Beam"])
gladionteam=teamset([gladion2,gladion3,gladion4,gladion5,gladion1,gladion10,gladion11],4)+teamset([gladion7,gladion8,gladion9],1)+[gladion6]
gladion=Trainer ("Pokémon Trainer Gladion",gladionteam,"Alola")
#morimoto
morimoto1=Spiritomb(maxiv="Yes")
morimoto2=Ambipom(maxiv="Yes")
morimoto3=Hippowdon(maxiv="Yes")
morimoto4=Jolteon(maxiv="Yes")
morimoto5=Vaporeon(maxiv="Yes")
morimoto6=Flareon(maxiv="Yes")
morimoto7=Cursola(maxiv="Yes")
morimoto8=Grapploct(maxiv="Yes")
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
dawn25=Cresselia (maxiv="Yes")
dawnteam=teamset([dawn2,dawn3,dawn4,dawn5,dawn1,dawn6,dawn7,dawn8,dawn10,dawn11,dawn12,dawn13,dawn14,dawn15,dawn16,dawn17,dawn18,dawn19,dawn20,dawn21,dawn22,dawn23,dawn24,dawn25],5)+[dawn9]
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
bronius5=Sableye(maxiv="Yes",item="Sablenite")
bronius6=Amoongus(maxiv="Yes")
broniusteam=teamset([bronius2,bronius3,bronius4,bronius5,bronius1],5)+[bronius6]
bronius=Trainer ("Plasma Sage Bronius",broniusteam,"Unova")
#ryoku
ryoku1=Garbodor(maxiv="Yes")
ryoku2=Absol(maxiv="Yes")
ryoku3=Flygon(maxiv="Yes")
ryoku4=Bisharp(maxiv="Yes")
ryoku5=Pinsir(maxiv="Yes",item="Pinsirite")
ryoku6=Scolipede(maxiv="Yes")
ryokuteam=teamset([ryoku2,ryoku3,ryoku4,ryoku5,ryoku1],5)+[ryoku6]
ryoku=Trainer ("Plasma Sage Ryoku",ryokuteam,"Unova")
#rood
rood1=Swoobat(maxiv="Yes")
rood2=Stoutland(maxiv="Yes")
rood3=Zoroark(maxiv="Yes")
rood4=Granbull(maxiv="Yes")
rood5=Houndoom(maxiv="Yes",item="Houndoominite")
rood6=Chandelure(maxiv="Yes")
roodteam=teamset([rood2,rood3,rood4,rood5,rood1],5)+[rood6]
rood=Trainer ("Plasma Sage Rood",roodteam,"Unova")
#zinzolin
zinzolin1=Abomasnow(maxiv="Yes",item="Abomasite")
zinzolin2=Vanilluxe(maxiv="Yes")
zinzolin3=Beartic(maxiv="Yes")
zinzolin4=Weavile(maxiv="Yes")
zinzolin5=Kyurem(maxiv="Yes")
zinzolin6=Cryogonal(name="Cryogonal",maxiv="Steel")
zinzolinteam=teamset([zinzolin2,zinzolin3,zinzolin4,zinzolin5,zinzolin1],5)+[zinzolin6]
zinzolin=Trainer ("Plasma Sage Zinzolin",zinzolinteam,"Unova")
#colress
colress1=Magnezone(maxiv="Yes")
colress2=Beheeyem(maxiv="Yes")
colress3=WRotom(maxiv="Yes")
colress4=PorygonZ(maxiv="Yes")
colress5=Metagross(maxiv="Yes",item="Metagrossite")
colress6=Klinklang(maxiv="Yes")
colress7=Muk(maxiv="Yes")
colress8=Electrode(maxiv="Yes")
colressteam=teamset([colress2,colress3,colress4,colress5,colress1,colress7,colress8],5)+[colress6]
colress=Trainer ("Plasma Admin Colress",colressteam,"Unova")
#argenta
argenta1=random.choice(allmon)(maxiv="Yes")
argenta2=random.choice(allmon)(maxiv="Yes")
argenta3=random.choice(allmon)(maxiv="Yes")
argenta4=random.choice(allmon)(maxiv="Yes")
argenta5=random.choice(allmon)(maxiv="Yes")
argenta6=Drifblim(maxiv="Yes")
argentateam=teamset([argenta1,argenta2,argenta3,argenta4,argenta5],5)+[argenta6]
argenta=Trainer ("Hall Matron Argenta",argentateam,"Sinnoh")
#matt
matt1=Mightyena(maxiv="Yes")
matt2=Muk(maxiv="Yes")
matt3=Crobat(maxiv="Yes")
matt4=Azumarill (maxiv="Yes")
matt5=Flygon(maxiv="Yes")
matt6=Sharpedo (maxiv="Yes",item="Sharpedonite")
matt=Trainer("Aqua Admin Matt",[matt1,matt2,matt3,matt4,matt5,matt6],"Hoenn")
#shelly
shelly1=Mightyena(maxiv="Yes")
shelly2=Muk (maxiv="Yes")
shelly3=Crobat(maxiv="Yes")
shelly4=Crawdaunt(maxiv="Yes")
shelly5=Sharpedo(maxiv="Yes")
shelly6=Walrein(maxiv="Yes")
shelly=Trainer("Aqua Admin Shelly",[shelly1,shelly2,shelly3,shelly4,shelly5,shelly6],"Hoenn")
#eusine
eusine1=Pikachu(maxiv="Yes")
eusine2=Jumpluff(maxiv="Yes")
eusine3=Hypno(maxiv="Yes")
eusine4=Alakazam(maxiv="Yes",item="Alakazite")
eusine5=Gengar(maxiv="Yes")
eusine6=Electrode(maxiv="Yes")
eusine=Trainer("Pokémon Trainer Eusine",[eusine1,eusine2,eusine3,eusine4,eusine5,eusine6],"Johto")
#evelyn
evelyn1=Pachirisu(maxiv="Yes",item="Sitrus Berry")
evelyn2=Primeape(maxiv="Yes",item="Scope Lens")
evelyn3=Raikou(maxiv="Yes",item="Air Balloon")
evelyn4=Suicune(maxiv="Yes",item="Lum Berry")
evelyn5=Entei(maxiv="Yes",item="Life Orb")
evelyn6=Latios(maxiv="Yes",item="Latiosite")
evelyn7=Persian(maxiv="Yes",item="Life Orb")
evelyn8=Lumineon(maxiv="Yes",item="Expert Belt")
evelynteam=teamset([evelyn7,evelyn8,evelyn1,evelyn2,evelyn3,evelyn4,evelyn6],5)+[evelyn5]
evelyn=Trainer("Battle Chatelaine Evelyn",evelynteam,"Hoenn")
#morgan
morgan1=Mantine(maxiv="Yes",item="Wacan Berry")
morgan2=Sawsbuck (maxiv="Yes",item="Leftovers")
morgan3=Swalot(maxiv="Yes",item="Black Sludge")
morgan4=Klefki(maxiv="Yes",item="Apicot Berry")
morgan5=Cobalion(maxiv="Yes",item="Maranga Berry")
morgan6=Virizion(maxiv="Yes",item="Coba Berry")
morgan7=Terrakion(maxiv="Yes",item="Sitrus Berry")
morgan8=Latias(maxiv="Yes",item="Latiasite")
morganteam=teamset([morgan7,morgan8,morgan1,morgan2,morgan3,morgan4,morgan6],5)+[morgan5]
morgan=Trainer("Battle Chatelaine Morgan",morganteam,"Hoenn")
#nita
nita1=Purugly(maxiv="Yes",item="Life Orb")
nita2=Wigglytuff (maxiv="Yes",item="Leftovers")
nita3=Grumpig(maxiv="Yes",item="Wise Glasses")
nita4=Tornadus(maxiv="Yes",item="Yache Berry")
nita5=Thundurus(maxiv="Yes",item="Sitrus Berry")
nita6=Landorus(maxiv="Yes",item="Choice Scarf")
nitateam=teamset([nita1,nita2,nita3,nita4,nita5],5)+[nita6]
nita=Trainer("Battle Chatelaine Nita",nitateam,"Hoenn")
#dana
dana1=Mamoswine (maxiv="Yes",item="Persim Berry")
dana2=Dragalge (maxiv="Yes",item="Bright Powder")
dana3=Whimsicott(maxiv="Yes",item="Sitrus Berry")
dana4=Magnezone(maxiv="Yes",item="Shuca Berry")
dana5=Farigiraf (maxiv="Yes",item="Colbur Berry")
dana6=Magcargo(maxiv="Yes")
dana7=Articuno(maxiv="Yes",item="Charti Berry")
dana8=Zapdos (maxiv="Yes",item="Petaya Berry")
dana9=Moltres(maxiv="Yes")
dana10=Regirock (maxiv="Yes",item="Luminous Moss")
dana11=Regice (maxiv="Yes")
dana12=Registeel(maxiv="Yes",item="King's Rock")
danateam=teamset([dana1,dana2,dana3,dana4,dana5,dana6,dana7,dana8,dana9,dana10,dana11],5)+[dana12]
dana=Trainer("Battle Chatelaine Dana",danateam,"Hoenn")
#courtney
courtney1=Mightyena(maxiv="Yes")
courtney2=Weezing(maxiv="Yes")
courtney3=Crobat(maxiv="Yes")
courtney4=Torkoal(maxiv="Yes", ability="Drought")
courtney5=Camerupt(maxiv="Yes",item="Camerupite")
courtney6=Swellow(maxiv="Yes")
courtney7=Ninetales (maxiv="Yes", ability="Drought")
courtneyteam=teamset([courtney1,courtney2,courtney3,courtney4,courtney6,courtney7],5)+[courtney5]
courtney=Trainer("Magma Admin Courtney", courtneyteam,"Hoenn")
#butler
butler1=Dusclops(maxiv="Yes")
butler2=Gardevoir(maxiv="Yes")
butler3=Mightyena(maxiv="Yes")
butler4=Salamence(maxiv="Yes",item="Salamencite")
butler5=Jirachi(maxiv="Yes")
butler6=Groudon(name="Meta Groudon",maxiv="Yes")
butler=Trainer("Team Magma Butler",[butler1,butler2,butler3,butler4,butler5,butler6],"Hoenn")
#TRIALS

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
celosia6=Manectric(maxiv="Yes",item="Manectite")
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
xerosic1=Mawile(maxiv="Yes",item="Mawilite")
xerosic2=Whimsicott(maxiv="Yes")
xerosic3=Jellicent(maxiv="Yes")
xerosic4=Volcarona(maxiv="Yes")
xerosic5=Crobat(maxiv="Yes")
xerosic6=Malamar(maxiv="Yes")
xerosic7=Granbull(maxiv="Yes")
xerosic8=Persian(maxiv="Yes")
xerosicteam=teamset([xerosic2,xerosic3,xerosic4,xerosic5,xerosic1,xerosic7,xerosic8],5)+[xerosic6]
xerosic=Trainer ("Team Flare Xerosic",xerosicteam,"Kalos")

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
mela5=Houndoom(maxiv="Yes",item="Houndoominite")
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
eri4=Annihilape(maxiv="Yes")
eri5=Lucario(maxiv="Yes",item="Lucarionite")
eri6=Revavroom(name="Caph Starmobile",type1="Fighting",type2=None,maxiv="Yes",move=["Combat Torque","Spin Out","Poison Jab","Gunk Shot"])
eri=Trainer("Team Star Eri",[eri1,eri2,eri3,eri4,eri5,eri6],"Paldea")
#penny
penny1=Umbreon(maxiv="Yes")
penny2=Leafeon(maxiv="Yes")
penny3=Flareon(maxiv="Yes")
penny4=Jolteon(maxiv="Yes")
penny5=Vaporeon(maxiv="Yes")
penny6=Sylveon(name="Sylveon",maxiv="Fairy")
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
calaba4=Lopunny(maxiv="Yes",item="Lopunnite")
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
peony6=Copperajah(maxiv="Yes")
peonyteam=teamset([peony1,peony2,peony3,peony4,peony5],5)+[peony6]
peony=Trainer ("Champion Peony",peonyteam,"Alola")
#klara
klara1=Amoongus(maxiv="Yes")
klara2=Drapion(maxiv="Yes",move=["X-Scissor","Poison Fang","Ice Fang","Crunch"], ability="Battle Armor")
klara3=Scolipede (maxiv="Yes",move=["Smart Strike","Poison Jab","Megahorn","Protect"])
klara4=GWeezing(maxiv="Yes",move=["Toxic","Heat Wave","Strange Steam","Protect"])
klara5=GSlowking (maxiv="Yes",move=["Scald","Blizzard","Power Gem","Eerie Spell"])
klara6=GSlowbro(maxiv="max",move=["Shell Side Arm","Scald","Focus Blast","Psychic"])
klarateam=teamset([klara2,klara3,klara4,klara5,klara1],5)+[klara6]
klara=Trainer ("Gym Leader Klara",klarateam,"Galar")
#avery
avery1=Indeedee(maxiv="Yes")
avery2=GSlowking(maxiv="max",move=["Scald","Blizzard","Power Gem","Eerie Spell"])
avery3=Swoobat(maxiv="Yes",move=["Psychic","Air Slash","Energy Ball","Future Sight"])
avery4=Alakazam(maxiv="Yes",move=["Psychic","Shadow Ball","Tri Attack","Reflect"])
avery5=GRapidash(maxiv="Yes",move=["Psychic","Mystical Fire","Extreme Speed","Dazzling Gleam"])
avery6=GSlowbro(maxiv="Yes",move=["Shell Side Arm","Scald","Focus Blast","Psychic"])
averyteam=teamset([avery6,avery3,avery4,avery5,avery1],5)+[avery2]
avery=Trainer ("Gym Leader Avery",averyteam,"Galar")
#arven
arven1=Greedent(maxiv="Yes")
arven2=Cloyster(maxiv="Yes")
arven3=Scovillain(maxiv="Yes")
arven4=Toedscruel(maxiv="Yes")
arven5=Garganacl(maxiv="Yes")
arven6=Mabosstiff(name="Mabosstiff",maxiv="Dark")
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
jessie9=Meowth(maxiv="Yes")
jessieteam=teamset([jessie2,jessie3,jessie4,jessie5,jessie1,jessie6,jessie7,jessie8],5)+[jessie9]
jessie=Trainer ("Team Rocket Jessie",jessieteam,"Kanto")
#clavell
clavell1=Oranguru(maxiv="Yes")
clavell2=Abomasnow(maxiv="Yes")
clavell3=Polteageist(maxiv="Yes")
clavell4=Gyarados(maxiv="Yes")
clavell5=Houndoom(maxiv="Yes")
clavell6=Quaquaval(name="Quaquaval",maxiv=random.choice(["Water","Fighting"]))
clavell7=Amoongus(maxiv="Yes")
clavell8=Meowscarada(name="Meowscarada",maxiv=random.choice(["Grass","Dark"]))
clavell9=Skeledirge(name="Skeledirge",maxiv=random.choice(["Fire","Ghost"]))
clavellteam=teamset([clavell2,clavell3,clavell4,clavell5,clavell1,clavell7],5)+teamset([clavell6, clavell9, clavell8],1)
clavell=Trainer ("Director Clavell Mesagoza",clavellteam,"Paldea")
#zoey
zoey1=Glameow(maxiv="Yes")
zoey2=Lumineon(maxiv="Yes")
zoey3=WGastrodon(maxiv="Yes")
zoey4=Leafeon(maxiv="Yes")
zoey5=Mismagius(name="Mismagius",maxiv="Fairy")
zoey6=Gallade(maxiv="Yes",item="Galladite")
zoey=Trainer("Coordinator Zoey",[zoey1,zoey2,zoey3,zoey4,zoey5,zoey6],"Sinnoh")
#conway
conway1=Slowking(maxiv="Yes")
conway2=Heracross (maxiv="Yes")
conway3=Aggron(maxiv="Yes",item="Aggronite")
conway4=Shuckle(maxiv="Yes")
conway5=Lickilicky(maxiv="Yes")
conway6=Dusknoir(maxiv="Yes")
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
james9=Meowth(maxiv="Yes")
jamesteam=teamset([james2,james3,james4,james5,james1,james6,james7,james8],5)+[james9]
james=Trainer ("Team Rocket James",jamesteam,"Kanto")
jessiejamesteam=teamset([james2,james3,james4,james5,james1,james6,james7,james8,jessie2,jessie3,jessie4,jessie5,jessie1,jessie6,jessie7,jessie8],5)+[james9]
jessiejames=Trainer ("Team Rocket Jessie & James",jessiejamesteam,"Kanto")
#nando
nando1=Roserade(maxiv="Yes")
nando2=Sunflora(maxiv="Yes")
nando3=Altaria(maxiv="Yes")
nando4=Lopunny(maxiv="Yes",item="Lopunnite")
nando5=Kricketune(name="Kricketune ",maxiv="Steel")
nando6=Armaldo(maxiv="Yes")
nando=Trainer("Pokémon Trainer Nando",[nando1,nando2,nando3,nando4,nando5,nando6],"Sinnoh")
#drew
drew1=Swampert(maxiv="Yes")
drew2=Butterfree(maxiv="Yes")
drew3=Roserade(maxiv="Yes")
drew4=Masquerain(maxiv="Yes")
drew5=Absol(maxiv="Yes",item="Absolite")
drew6=Flygon(name="Flygon",maxiv="Bug")
drew=Trainer("Pokémon Trainer Drew",[drew1,drew2,drew3,drew4,drew5,drew6],"Hoenn")
#trip
trip1=Unfezant(maxiv="Yes")
trip2=Vanilluxe (maxiv="Yes")
trip3=Chandelure(maxiv="Yes")
trip4=Jellicent(maxiv="Yes")
trip5=Conkeldurr(maxiv="Yes")
trip6=Serperior(maxiv="Yes")
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
kenny2=Floatzel(name="Floatzel",maxiv="Ice")
kenny3=Machamp(maxiv="Yes")
kenny4=Breloom(maxiv="Yes")
kenny5=Alakazam(maxiv="Yes",item="Alakazite")
kenny6=Empoleon(maxiv="Yes")
kenny=Trainer("Coordinator Kenny",[kenny1,kenny2,kenny3,kenny4,kenny5,kenny6],"Sinnoh")
#ritchie
ritchie1=Tentacruel(maxiv="Yes")
ritchie2=Swellow(name="Rose",maxiv="Yes")
ritchie3=Tyranitar(name="Cruise",maxiv="Rock")
ritchie4=Butterfree(name="Happy",maxiv="Yes")
ritchie5=Charizard(name="Zippo",maxiv="Yes",item="Charizardite Y",atkev=0,spatkev=252)
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
hugh=Trainer("Rival Hugh",hughteam,"Unova")
#harrison
harrison1=Kecleon(maxiv="Yes")
harrison2=Hypno(maxiv="Yes")
harrison3=Miltank(maxiv="Yes")
harrison4=Steelix(maxiv="Yes")
harrison5=Houndoom(name="Houndoom",maxiv="Dark")
harrison6=Blaziken(maxiv="Yes",item="Blazikenite")
harrison=Trainer("Pokémon Trainer Harrison",[harrison1,harrison2,harrison3,harrison4,harrison5,harrison6],"Hoenn")
#harley
harley1=Sceptile(maxiv="Yes")
harley2=Ariados(maxiv="Yes")
harley3=Octillery(maxiv="Yes")
harley4=Wigglytuff (maxiv="Yes")
harley5=Banette(maxiv="Yes")
harley6=Cacturne(maxiv="Yes")
harley=Trainer("Coordinator Harley",[harley1,harley2,harley3,harley4,harley5,harley6],"Hoenn")
#tyson
tyson1=Shiftry (maxiv="Yes")
tyson2=Hariyama (maxiv="Yes")
tyson3=Donphan(maxiv="Yes")
tyson4=Sceptile (name="Sceptile",maxiv="Grass")
tyson5=Metagross (maxiv="Yes")
tyson6=Meowth (maxiv="Yes")
tyson=Trainer("Pokémon Trainer Tyson",[tyson1,tyson2,tyson3,tyson4,tyson5,tyson6],"Hoenn")
#solidad
solidad1=Blissey (maxiv="Yes")
solidad2=Snorlax(maxiv="Yes")
solidad3=Butterfree(maxiv="Yes")
solidad4=Pidgeot (name="Pidgeot",maxiv="Normal")
solidad5=Lapras (maxiv="Yes")
solidad6=Slowbro (maxiv="Yes",item="Slowbronite")
solidad=Trainer("Coordinator Solidad",[solidad1,solidad2,solidad3,solidad4,solidad5,solidad6],"Kanto")
#dino
dino1=Seismitoad(maxiv="Yes")
dino2=Leavanny (maxiv="Yes")
dino3=Chandelure(maxiv="Yes")
dino4=Gigalith(maxiv="Yes")
dino5=Darmanitan (maxiv="Yes")
dino6=Druddigon(name="Druddigon",maxiv="Dragon")
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
burgundy6=Samurott(name="Samurott",maxiv="Water")
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
cameron5=Hydreigon(name="Hydreigon",maxiv="Dark")
cameron6=Samurott (maxiv="Yes")
cameronteam=teamset([cameron1,cameron2,cameron3,cameron4,cameron5],5)+[cameron6]
cameron=Trainer("Pokémon Trainer Cameron",cameronteam,"Unova")
#Ilima
Ilima1=Eevee(name="Eevee(Z-Crystal)",maxiv="Yes")
Ilima2=ARaticate (maxiv="Yes")
Ilima3=Gumshoos(maxiv="Yes")
Ilima4=Komala(maxiv="Yes")
Ilima5=Smeargle(maxiv="Yes")
Ilima6=Kangaskhan (maxiv="Yes",item="Kangaskhanite")
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
kiawe7=Kangaskhan(maxiv="Yes",item="Kangaskhanite")
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
saguaro3=Alomomola(maxiv="Yes")
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
mallow7=Sceptile(maxiv="Yes",item="Sceptilite")
mallow8=Appletun(maxiv="Yes")
mallow9=Talonflame(maxiv="Yes")
mallow10=Toucannon (maxiv="Yes")
mallowteam=teamset([mallow1,mallow2,mallow3,mallow4,mallow5,mallow7,mallow8,mallow9,mallow10],5)+[mallow6]
mallow=Trainer("Trial Captain Mallow",mallowteam,"Alola")
#plumeria
plumeria1=Toxapex(maxiv="Yes")
plumeria2=Lurantis (maxiv="Yes")
plumeria3=Gumshoos (maxiv="Yes")
plumeria4=Gengar(maxiv="Yes")
plumeria5=Crobat(maxiv="Yes")
plumeria6=Salazzle(maxiv="Yes")
plumeriateam=teamset([plumeria1,plumeria2,plumeria3,plumeria4,plumeria6,plumeria5])
plumeria=Trainer("Team Skull Plumeria",plumeriateam,"Alola")
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
calem7=Absol(maxiv="Yes",item="Absolite")
calem10=Chesnaught(maxiv="Yes")
calem11=Jolteon(maxiv="Yes")
calem12=Vaporeon (maxiv="Yes")
calem13=Flareon(maxiv="Yes")
calem14=Greninja(name="Greninja ✨",maxiv="Yes")
calemteam=teamset([calem3,calem4,calem5,calem7,calem6,calem14],4)+[calem10,calem1]
calem=Trainer("Rival Calem",calemteam,"Kalos")
#sun
sun1=APersian(name="Cent",maxiv="Yes")
sun2=Stakataka (name="Drachma",maxiv="Yes")
sun3=Crabominable (name="Loot",maxiv="Yes")
sun4=Mimikyu(name="Penny",maxiv="Yes")
sun5=SWishiwashi (name="Quarter",maxiv="Yes")
sun6=Incineroar(name="Dollar",maxiv="Yes")
sunteam=teamset([sun2,sun3,sun4,sun5,sun1],5)+[sun6]
sun=Trainer ("Rival Sun",sunteam,"Alola")
#Lillie
Lillie1=Comfey(maxiv="Yes")
Lillie2=ANinetales(maxiv="Yes")
Lillie3=Clefable(maxiv="Yes")
Lillie4=Solgaleo(name="Nebby(Z-Crystal)",maxiv="Yes")
Lillie5=Ribombee(maxiv="Yes")
Lillie6=Magearna(name="Magearna✨",maxiv="Yes")
Lillie7=Lunala(name="Nebby(Z-Crystal)",maxiv="Yes")
Lillie8=Polteageist(maxiv="Yes")
Lillieteam=teamset([Lillie1,Lillie2,Lillie3,Lillie5,Lillie8],4)+teamset([Lillie4,Lillie7],1)+[Lillie6]
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
amber6=Sharpedo(maxiv="Yes",item="Sharpedonite")
amber5=Gorebyss(maxiv="Yes")
amber=Trainer("Aqua Admin Amber",[amber1,amber2,amber3,amber4,amber5,amber6],"Hoenn")   
#brunoh
brunoh1=Infernape(maxiv="Yes",item="Focus Sash",move=["Taunt","Pyro Ball","Close Combat","Stealth Rock"], ability="Blaze",nature="Jolly")
brunoh2=DUrshifu(maxiv="Yes",item="Choice Scarf",move=["Wicked Blow","Close Combat","U-turn","Poison Jab"],nature="Jolly")
brunoh3=Zacian(maxiv="Yes",move=["Behemoth Blade","Close Combat","Swords Dance","Crunch"],nature="Jolly")
brunoh4=Kommo(maxiv="Yes",item="Throat Spray",move=["Aura Sphere","Flash Cannon","Clanging Scales","Clangorous Soul"],nature="Timid")
brunoh6=Lucario(maxiv="Yes",item="Lucarionite",move=["Swords Dance","Bullet Punch","Close Combat","Meteor Mash"],nature="Jolly")
brunoh5=Conkeldurr(maxiv="Yes", ability="Iron Fist",item="Assault Vest",move=["Knock Off","Ice Punch","Mach Punch","Drain Punch"],nature="Adamant")
brunoh=Trainer("E4 Bruno(Hard Mode)",[brunoh1,brunoh2,brunoh3,brunoh4,brunoh5,brunoh6],"Kanto") 
#edit
brockh1=Terrakion(item="Lum Berry",ability="Justified",maxiv="Yes",nature="Jolly",move=["Close Combat","X-Scissor","Stone Edge","Stealth Rock"])
brockh2=Landorus(item="Life Orb",ability="Sand Force",maxiv="Yes",nature="Naive",move=["Earthquake","Grass Knot","Stone Edge","U-turn"])
brockh3=CZygarde(item="Leftovers",ability="Power Construct",maxiv="Yes",nature="Careful",move=["Coil","Thousand Arrows","Rest","Sleep Talk"])
brockh4=Sandslash(name="Sandslash(Z-Crystal)",item="Groundium-Z",ability="Sand Rush",maxiv="Ground",nature="Jolly",move=["Swords Dance","Earthquake","Stone Edge","Knock Off"])
brockh5=Empoleon(item="Leftovers",ability="Competitive",maxiv="Yes",nature="Bold",move=["Scald","Ice Beam","Toxic","Roost"])
brockh6=Aerodactyl(item="Aerodactylite",ability="Pressure",maxiv="Yes",nature="Jolly",move=["Stone Edge","Dual Wingbeat","Earthquake","Dragon Dance"])
brockh=Trainer("Brock(Hard Mode)",[brockh1,brockh2,brockh3,brockh4,brockh5,brockh6],"Kanto")
#edit
mistyh1=Kingdra(item="Life Orb",ability="Swift Swim",maxiv="Yes",nature="Modest",move=["Hydro Pump","Draco Barrage","Hurricane","Flip Turn"])
mistyh2=Seismitoad(item="Life Orb",ability="Swift Swim",maxiv="Yes",nature="Modest",move=["Earth Power","Weather Ball","Power Whip","Focus Blast"])
mistyh3=Jirachi(item="Leftovers",ability="Serene Grace",maxiv="Yes",nature="Timid",move=["Psyshock","Thunder","Water Pulse","Calm Mind"])
mistyh4=TThundurus(name="Therian Thundurus(Z-Crystal)",item="Fightinium-Z",ability="Volt Absorb",maxiv="Fighting",nature="Timid",move=["Thunder","Weather Ball","Focus Blast","Nasty Plot"])
mistyh5=Gyarados(item="Gyaradosite",ability="Intimidate",maxiv="Yes",nature="Jolly",move=["Waterfall","Crunch","Earthquake","Dragon Dance"])
mistyh6=Greninja(item="Focus Sash",ability="Protean",maxiv="Yes",nature="Naive",move=["Ice Beam","Surf","Dark Pulse","U-turn"])
mistyh=Trainer("Misty(Hard Mode)",[mistyh1,mistyh2,mistyh3,mistyh4,mistyh5,mistyh6],"Kanto")
#maskedman
maskedman1=Lugia(maxiv="Yes")
maskedman2=Hooh(maxiv="Yes")
maskedman3=Ariados(maxiv="Yes")
maskedman4=Gengar(maxiv="Yes")
maskedman5=Houndoom(maxiv="Yes")
maskedman6=Delibird(maxiv="Yes", ability="Snow Warning",spatkev=252,speedev=252,defev=252,spdefev=252,hpev=252)
maskedman7=Celebi(maxiv="Yes")
mmteam=teamset([maskedman3,maskedman4,maskedman5,maskedman7],3)+[maskedman1,maskedman2,maskedman6]
maskedman=Trainer("Rocket Boss Masked Man",mmteam,"Johto")
#marley
marley1=Ninjask(maxiv="Yes")
marley2=Electrode(maxiv="Yes")
marley3=Crobat(maxiv="Yes")
marley4=Weavile(maxiv="Yes")
marley5=Dugtrio(maxiv="Yes")
marley6=Arcanine(maxiv="Yes")
marley7=Starmie(maxiv="Yes")
marley8=Aerodactyl(maxiv="Yes")
marley9=Sceptile(maxiv="Yes")
marley10=Swellow(maxiv="Yes")
marley11=Alakazam(maxiv="Yes")
marley12=Pinsir(maxiv="Yes")
marley13=Jolteon(maxiv="Yes")
marley14=Raikou(maxiv="Yes")
marley15=Floatzel(maxiv="Yes")
marley16=Ambipom(maxiv="Yes")
marleyteam=teamset([marley1,marley2,marley3,marley4,marley5,marley7,marley8,marley9,marley10,marley11,marley12,marley13,marley14,marley15,marley16],5)+[marley6]
marley=Trainer("Pokémon Trainer Marley",marleyteam,"Sinnoh")
hof1=Toxapex(name="Toxapex",item="Black Sludge",ability="Regenerator",maxiv="Yes",nature="Impish",move=["Knock Off","Scald","Baneful Bunker","Toxic Spikes"],hpev=252,atkev=0,defev=252,spatkev=0,spdefev=0,speedev=0)
hof2=Ferrothorn(name="Ferrothorn",item="Rocky Helmet",ability="Iron Barbs",maxiv="Yes",nature="Brave",move=["Gyro Ball","Shadow Claw","Grass Knot","Stealth Rock"],hpev=248,atkev=0,defev=0,spatkev=8,spdefev=0,speedev=0)
hof3=Corviknight(name="Corviknight",item="Leftovers",ability="Pressure",maxiv="Yes",nature="Impish",move=["Roost","Brave Bird","Reflect","Light Screen"],hpev=248,atkev=0,defev=252,spatkev=0,spdefev=0,speedev=0)
hof4=Dracozolt(name="Dracozolt",item="Choice Scarf",ability="Sand Rush",maxiv="Yes",nature="Rash",move=["Bolt Beak","Flamethrower","Earth Power","Draco Meteor"],hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252)
hof5=Polteageist(name="Polteageist",item="Focus Sash",ability="Weak Armor",maxiv="Yes",nature="Modest",move=["Giga Drain","Stored Power","Shell Smash","Shadow Ball"],hpev=0,atkev=0,defev=0,spatkev=252,spdefev=4,speedev=252)
hof6=Silvally(name="Silvally",item="Fairy Memory",ability="RKS System",maxiv="Yes",nature="Jolly",move=["Iron Head","Multi-Attack","Swords Dance","Protect"],hpev=0,atkev=0,defev=0,spatkev=0,spdefev=4,speedev=252)
hof=Trainer("Hall of Fame Silver",[hof1, hof2, hof3, hof4, hof5, hof6], "Unknown")
garyhc1=Kyogre(name="Kyogre",item="Blue Orb",ability="Primordial Sea",maxiv="Yes",nature="Timid",move=["Origin Pulse","Thunder","Ice Punch","Liquidation"],hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0)
garyhc2=Arceus(name="Arceus(Z-Crystal)",item="Normalium-Z",ability="Multitype",maxiv="Yes",nature="Jolly",move=["Extremespeed","Shadow Claw","Recover","Swords Dance"],hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0)
garyhc3=DWNecrozma(name="Necrozma(Z-Crystal)",item="Ultranecrozmium-Z",ability="Neuroforce",maxiv="Yes",nature="Jolly",move=["Photon Geyser","Earthquake","Stone Edge","Dragon Dance"],hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0)
garyhc4=Metagross(name="Metagross",item="Metagrossite",ability="Tough Claws",maxiv="Yes",nature="Jolly",move=["Meteor Mash","Ice Punch","Thunder Punch","Bullet Punch"],hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0)
garyhc5=EEternatus(name="Eternatus-Eternamax",item="Eternamax Orb",ability="Levitate",maxiv="Yes",nature="Timid",move=["Draco Barrage","Sludge Wave","Thunder","Recover"],hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0)
garyhc6=Swampert(name="Swampert",item="Swampertite",ability="Swift Swim",maxiv="Yes",nature="Adamant",move=["Earthquake","Waterfall","Ice Punch","Stone Edge"],hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0)
garyhc=Trainer("Gary(Hard Mode)",[garyhc1, garyhc2, garyhc3, garyhc4, garyhc5, garyhc6], "Unknown")
wulfrich1=Froslass(name="Froslass",item="Bright Powder",ability="Snow Cloak",maxiv="Ice",nature="Timid",move=["Blizzard","Thunderbolt","Shadow Ball","Psychic"],hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0)
wulfrich2=Jynx(name="Jynx",item="Life Orb",ability="Dry Skin",maxiv="Ice",nature="Timid",move=["Lovely Kiss","Psychic","Blizzard","Energy Ball"],hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0)
wulfrich3=Aurorus(name="Aurorus",item="Icy Rock",ability="Snow Warning",maxiv="Rock",nature="Modest",move=["Blizzard","Earth Power","Power Gem","Protect"],hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0)
wulfrich4=WKyurem(name="White Kyurem",item="Life Orb",ability="Turboblaze",maxiv="Dragon",nature="Hasty",move=["Fusion Flare","bizzard","Earth Power","Dragon Pulse"],hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0)
wulfrich5=Lapras(name="Lapras",item="Icicle Plate",ability="Water Absorb",maxiv="Water",nature="Quiet",move=["Blizzard","Giga Drain","Focus Blast","Ice Shard"],hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0)
wulfrich6=Abomasnow(name="Abomasnow-Mega",item="Abomasite",ability="Snow Warning",maxiv="Grass",nature="Quiet",move=["Blizzard","Giga Drain","Focus Blast","Ice Shard"],hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0)
wulfrich=Trainer("Wulfric(Hard Mode)",[wulfrich1, wulfrich2, wulfrich3, wulfrich4, wulfrich5, wulfrich6], "Kalos")
olympiah1=Claydol(name="Claydol",item="Leftovers",ability="Levitate",maxiv="Ground",nature="Modest",move=["Earth Power","Psyshock","Calm Mind","Ice Beam"],hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0)
olympiah2=Sigilyph(name="Sigilyph",item="Flame Orb",ability="Magic Guard",maxiv="Psychic",nature="Calm",move=["Stored Power","Cosmic Power","Psycho Shift","Roost"],hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0)
olympiah3=ADeoxys(name="Deoxys-Attack",item="Focus Sash",ability="Pressure",maxiv="Psychic",nature="Hasty",move=["Psycho Boost","Superpower","Fire Punch","Knock Off"],hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0)
olympiah4=Latias(name="Latias",item="Soul Dew",ability="Levitate",maxiv="Dragon",nature="Bold",move=["Psyshock","Dragon Pulse","Calm Mind","Recover"],hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0)
olympiah5=Metagross(name="Metagross",item="Air Balloon",ability="Tough Claws",maxiv="Steel",nature="Adamant",move=["Meteor Mash","Earthquake","Ice Punch","Rock Polish"],hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0)
olympiah6=Medicham(name="Medicham-Mega",item="Medichamite",ability="Pure Power",maxiv="Fighting",nature="Jolly",move=["Drain Punch","Zen Headbutt","Ice Punch","Poison Jab"],hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0)
olympiah=Trainer("Olympia(Hard Mode)",[olympiah1, olympiah2, olympiah3, olympiah4, olympiah5, olympiah6], "Kalos")
sidneyk1=Sableye(name="Sableye",item="Lum Berry",ability="Pressure",maxiv="Rock",nature="Brave",move=["Shadow Sneak","Shadow Ball","Brick Break","Hidden Power"],hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0)
sidneyk2=Machamp(name="Machamp",item="Chesto Berry",ability="Guts",maxiv="Ghost",nature="Brave",move=["Superpower","Hidden Power","Earthquake","Rock Slide"],hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0)
sidneyk3=Jolteon(name="Jolteon",item="Lum Berry",ability="Static",maxiv="Grass",nature="Hasty",move=["Thunderbolt","Hidden Power","Crunch","Signal Beam"],hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0)
sidneyk4=Alakazam(name="Alakazam",item="Lum Berry",ability="Synchronize",maxiv="Water",nature="Hasty",move=["Psychic","Hidden Power","Fire Punch","Thunder Punch"],hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0)
sidneyk5=Tauros(name="Tauros",item="Lum Berry",ability="Intimidate",maxiv="Ghost",nature="Hasty",move=["Double-Edge","Hidden Power","Earthquake","Extreme Speed"],hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0)
sidneyk6=Houndoom(name="Houndoom",item="Lum Berry",ability="Intimidate",maxiv="Grass",nature="Mild",move=["Heat Wave","Crunch","Hidden Power","Dark Pulse"],hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0)
sidneyk=Trainer("Sidney(Kaizo)",[sidneyk1, sidneyk2, sidneyk3, sidneyk4, sidneyk5, sidneyk6], "Hoenn")
phoebek1=Gengar(name="Gengar",item="Lum Berry",ability="Levitate",maxiv="Yes",nature="Hasty",move=["Hypnosis","Destiny Bond","Thunderbolt","Ice Punch"],hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0)
phoebek2=Ludicolo(name="Ludicolo",item="Lum Berry",ability="Swift Swim",maxiv="Yes",nature="Modest",move=["Spore","Giga Drain","Ice Beam","Surf"],hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0)
phoebek3=Crobat(name="Crobat",item="Leftovers",ability="Inner Focus",maxiv="Ground",nature="Timid",move=["Hypnosis","Air Slash","Heat Wave","Hidden Power"],hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0)
phoebek4=Gardevoir(name="Gardevoir",item="Lum Berry",ability="Synchronize",maxiv="Yes",nature="Hasty",move=["Thunder Wave","Psychic","Thunderbolt","Fire Punch"],hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0)
phoebek5=Sableye(name="Sableye",item="Lum Berry",ability="Pressure",maxiv="Yes",nature="Relaxed",move=["Shadow Sneak","Recover","Shadow Ball","Brick Break"],hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0)
phoebek6=Dusclops(name="Dusclops",item="Eviolite",ability="Pressure",maxiv="Yes",nature="Brave",move=["Shadow Sneak","Brick Break","Rest","Shadow Ball"],hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0)
phoebek=Trainer("Phoebe(Kaizo)",[phoebek1, phoebek2, phoebek3, phoebek4, phoebek5, phoebek6], "Hoenn")
glaciak1=Glalie(name="Glalie",item="Lum Berry",ability="Intimidate",maxiv="Yes",nature="Hasty",move=["Weather Ball","Ice Beam","Spikes","Explosion"],hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252)
glaciak2=Wailord(name="Wailord",item="Lum Berry",ability="Pressure",maxiv="Yes",nature="Lax",move=["Hyper Voice","Water Spout","Explosion","Amnesia"],hpev=248,atkev=8,defev=0,spatkev=252,spdefev=0,speedev=0)
glaciak3=Regice(name="Regice",item="Lum Berry",ability="Clear Body",maxiv="Yes",nature="Quiet",move=["Counter","Ice Beam","Thunder","Explosion"],hpev=248,atkev=8,defev=0,spatkev=252,spdefev=0,speedev=0)
glaciak4=Dewgong(name="Dewgong",item="Lum Berry",ability="Swift Swim",maxiv="Grass",nature="Mild",move=["Ice Beam","Drill Run","Hidden Power","Surf"],hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0)
glaciak5=Swampert(name="Swampert",item="Lum Berry",ability="Swift Swim",maxiv="Yes",nature="Mild",move=["Earthquake","Yawn","Muddy Water","Ancient Power"],hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252)
glaciak6=Lapras(name="Lapras",item="Lum Berry",ability="Shell Armor",maxiv="Yes",nature="Mild",move=["Ice Shard","Thunder","Ice Beam","Hydro Pump"],hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252)
glaciak=Trainer("Glacia(Kaizo)",[glaciak1, glaciak2, glaciak3, glaciak4, glaciak5, glaciak6], "Hoenn")
drakek1=Latias(name="Latias",item="Soul Dew",ability="Levitate",maxiv="Fire",nature="Calm",move=["Calm Mind","Dragon Claw","Hidden Power","Recover"],hpev=252,atkev=0,defev=252,spatkev=0,spdefev=0,speedev=0)
drakek2=Tyranitar(name="Tyranitar",item="Lum Berry",ability="Intimidate",maxiv="Rock",nature="Mild",move=["Dragon Dance","Ancient Power","Earthquake","Ancient Power"],hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0)
drakek3=Salamence(name="Salamence",item="Lum Berry",ability="Intimidate",maxiv="Yes",nature="Hasty",move=["Draco Meteor","Air Slash","Earthquake","Flamethrower"],hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252)
drakek4=Kingdra(name="Kingdra",item="Lum Berry",ability="Swift Swim",maxiv="Fighting",nature="Sassy",move=["Hidden Power","Octazooka","Draco Meteor","Ice Beam"],hpev=0,atkev=0,defev=0,spatkev=252,spdefev=4,speedev=252)
drakek5=Dragonite(name="Dragonite",item="Lum Berry",ability="Thick Fat",maxiv="Yes",nature="Jolly",move=["Dragon Dance","Earthquake","Extreme Speed","Rock Slide"],hpev=0,atkev=0,defev=0,spatkev=0,spdefev=4,speedev=252)
drakek6=Latios(name="Latios",item="Soul Dew",ability="Levitate",maxiv="Fire",nature="Brave",move=["Draco Meteor","Luster Purge","Hidden Power","Recover"],hpev=252,atkev=0,defev=0,spatkev=252,spdefev=4,speedev=0)
drakek=Trainer("Drake(Kaizo)",[drakek1, drakek2, drakek3, drakek4, drakek5, drakek6], "Hoenn")
#astrid
astrid1=Mamoswine(maxiv="Yes")
astrid2=Arcanine(maxiv="Yes")
astrid3=Mismagius (maxiv="Yes")
astrid4=Meowstic(maxiv="Yes")
astrid5=Pyroar(maxiv="Yes")
astrid6=Absol(maxiv="Yes",item="Absolite")
astridteam=teamset([astrid2,astrid3,astrid4,astrid5,astrid1],5)+[astrid6]
astrid=Trainer ("Pokémon Trainer Astrid",astridteam,"Kalos")
#TEST2
t3=z
t4=Charizard(maxiv="OU-Grass")
t5=Morpeko(maxiv="Yes")
t6=Skarmory(maxiv="Yes",item="Rocky Helmet",move=["Substitute","Healing Wish","Roost","Outrage"])
t7=Silvally(maxiv="Yes")
t8=HRotom(maxiv="Yes",move=["Will-O-Wisp","Hex","Overheat","Shed Tail"])
test2=Trainer("Test-02",[t3,t4,t5,t6,t7,t8])
#############
#matchx=match
e4list=[lorelei,bruno,agatha, lance,will,koga,karen,sidney,phoebe,glacia,drake,aaron,bertha,flint,lucian,shauntal,marshal,grimsley,caitlin,siebold,wikstrom,drasna,malva,kahili,acerola,olivia,molayne,hala,rika,larry,poppy,hassel]

champlist=[oak,blue,red,odrake,ethan,steven,wallace,brendan,may,cynthia,alder,iris,diantha,alain,kukui,ash,mustard,peony,leon,geeta]

fronlist=[noland,lucy,tucker,greta,anabel,brandon,spenser,palmer,darach,dahlia,argenta,Thorton]

gymlist=[brock,misty,surge,erika,sabrina,janine,blaine,cissy,danny,rudy,luana,falkner,bugsy,whitney,chuck,morty,pryce,jasmine,clair,roxanne,brawly,wattson,flannery,norman,winona,tate,liza,juan,roark,gardenia,fantina,byron,maylene,wake,candice,volkner,cilan,chili,cress,lenora,burgh,elesa,clay,skyla,brycen,drayden,cheren,roxie,marlon,viola,grant,korrina,ramos,clemont,valerie,olympia,wulfric,milo,nessa,kabu,bea,allister,opal,bede,gordie,melony,piers,marnie,raihan,klara,avery,katy,brassius,Iono,kofu,ryme,grusha,tulip]

test=[test2,hof]

hardlist=[erikah,erikahc,blainehc,brunoh,kogah,brockh,mistyh,garyhc,wulfrich,olympiah,sidneyk,phoebek,glaciak,drakek]

talentlist=[gary,barry,paul,reggie,sun,calem,lucas,nate,rosa,hilbert,hilda,xadv,tyme,salvatore,miriam,dendra,raifort,jacq,saguaro,Lillie,mallow,lana,kiawe,Ilima,forina,hugh,hop,hau,shauna,tierno,astrid,ramone,cameron,virgil,dino,burgundy,solidad,tyson,harley,harrison,ritchie,dawn,kenny,ursula,trip,drew,riley,cheryl,marley,mira,nando,conway,zoey,zinnia,arven,clavell,sordward,shielbert,morimoto,palina,iscan,calaba,lian,mai,dexio,sina,goh,gladion,eusine,benga,trevor,sawyer,emmet,ingo,silver,buck,n,tobias,quillon,danika,horace,wally,nemona,evelyn,nita,dana,morgan,adaman]

evilist=[sird,jessiejames,jessie,james,petrel,proton,ariana,archer,maskedman,giovanni,shelly,matt,archie,amber,courtney,blaise,tabitha,maxie,saturn,mars,jupiter,cyrus,faba,lusamine,rose,plumeria,Guzma,volo,penny,eri,ortega,atticus,mela,giacomo,xerosic,aliana,celosia,bryony,mable,lysandre,ghetsis,colress,giallo,zinzolin,rood,ryoku,bronius,gorm,alsada,alturo,butler,blanche]

gym=random.choice(gymlist)
elite4=random.choice(e4list)
champ=random.choice(champlist)
frontier=random.choice(fronlist)
evil=random.choice(evilist)
talent=random.choice(talentlist)
alltr=random.choice([gym,elite4,champ, frontier,evil,talent])
