#pylint:disable=C0114
#pylint:disable=R0912
#pylint:disable=C0303
#pylint:disable=C0116
#pylint:disable=W0401
#pylint:disable=C0301
#pylint:disable=C0304
from pokemonbase import *
firemon=[Charizard,Arcanine, HArcanine, Rapidash,AMarowak,Flareon, Typhlosion,Moltres,HTyphlosion, Magcargo,Entei,Hooh,Blaziken,Camerupt, Infernape, Magmortar,Heatran,Emboar,Simisear, Darmanitan,Heatmor,Delphox,Talonflame,Pyroar,Volcanion, Incineroar, Turtonator, Cinderace, Blacephalon, Centiskorch, Skeledirge,Ironmoth, Armarouge, Ceruledge]
watermon=[Alomomola,Blastoise,Golduck, Poliwrath,Tentacruel,Slowbro,Dewgong, Cloyster,Kingler,Kingdra,Seaking,Starmie,Gyarados,Lapras, Vaporeon, Feraligatr, Lanturn, Azumarill,Politoed, Quagsire, Slowking,Corsola,Octillery, Mantine,Suicune, Swampert,Ludicolo,Pelipper,Sharpedo,Wailord,Whiscash, Crawdaunt, Milotic,Huntail,Gorebyss,Relicanth,Kyogre,Empoleon,Floatzel, Gastrodon,  Lumineon,Palkia,Phione, Samurott,HSamurott,Simipour, Seismitoad, Basculegion,Carracosta,Swanna, Jellicent,Keldeo, Greninja, Clawitzer,Primarina,SWishiwashi, Araquanid,Tapufini,Inteleon,Drednaw,Barraskewda,Dracovish, Quaquaval,Wugtrio, Dondozo,Veluza,Palafin, Walkingwake,Terapagos, Pyukumuku,Luvdisc,Bruxish]
fairymon=[Clefable,Granbull,Togekiss,Florges,EFloette,Slurpuff,Sylveon,Xerneas, Alcremie,Dachsbun, Enamorus, Zacian, Screamtail, Ironvaliant, Tinkaton,Comfey]
darkmon=[APersian,GMoltres,Umbreon, Weavile, Honchkrow, Houndoom,Mightyena, Obstagoon, Sableye, Absol,Darkrai,Liepard,Scrafty,Zoroark, Bisharp, Kingambit, Mandibuzz, Hydreigon,Malamar,Yveltal,Guzzlord, Grimmsnarl,Zarude, Overqwil, Mabosstiff, Ironjugulis,Tinglu, Chienpao,Wochien,Chiyu]
dragonmon=[Dragonite, Altaria, Salamence, Latios,Latias, Rayquaza, Garchomp, Haxorus, Druddigon,Reshiram,Zekrom,Kyurem,BKyurem,WKyurem,Goodra,HGoodra, CZygarde,Kommo,Dragapult,Regidrago, Baxcalibur, Tatsugiri,Cyclizar, Roaringmoon]
grassmon=[Venusaur,Vileplume,Victreebel,Exeggutor, AExeggutor, Meganium, Bellossom, Jumpluff,Sunflora,Sceptile, Shiftry, Breloom,Tropius,Torterra, Roserade,Cherrim, Abomasnow, Tangrowth, Leafeon,Shaymin,SShaymin, Serperior,Simisage, Whimsicott, Lilligant,HLilligant, Amoongus, Ferrothorn, Virizion, Chesnaught,Gogoat, Decidueye, HDecidueye,Lurantis,Shiinotic,Tsareena,Dhelmise,Tapubulu,Kartana,Rillaboom,Eldegoss,Appletun,Flapple, Meowscarada, Arboliva, Scovillain,Brambleghast, Brutebonnet,Carnivine,Maractus,Ironleaves,Ogerpon]
electricmon=[Pikachu,Raichu,ARaichu, Electrode, HElectrode, Jolteon,Zapdos, Ampharos, Raikou, Manectric,Plusle,Minun,Luxray, Pachirisu, Magnezone,HRotom,WRotom,FrRotom,FRotom,MRotom, Zebstrika,Emolga, Galvantula,Eelektross,Thundurus,TThundurus, Heliolisk,Tapukoko,Xurkitree,Zeraora, Boltund,Toxtricity, Pincurchin, Dracozolt,Arctozolt, Regieleki,Bellibolt,Pawmot, Kilowattrel, Sandyshocks, Miraidon,Dedenne, Togedemaru,Morpeko]
fightingmon=[Primeape, Poliwrath,Machamp,Hitmonlee, Hitmonchan,PTauros,GZapdos,Hitmontop,Hariyama,Medicham,Lucario, Conkeldurr,Throh,Sawk,Mienshao,Pangoro,Hawlucha,Crabominable,Passimian, Marshadow,Grapploct, Sirfetchd, Zamazenta, DUrshifu, WUrshifu, Ironhands, Annihilape,Koraidon]
flyingmon=[Oricorio,Tornadus,TTornadus,Noivern, Corviknight,Bombirdier,Flamigo,Cramorant]
poisonmon=[EEternatus,Arbok,Nidoking, Nidoqueen,GSlowbro,Muk,AMuk, Weezing, GWeezing,Crobat,GSlowking,Swalot,Seviper,Skuntank,Drapion,Toxicroak, Garbodor,Dragalge,Toxapex,Salazzle, Naganadel, Eternatus, Sneasler, Grafaiai,Clodsire]
groundmon=[Sandslash, Dugtrio, ADugtrio, Marowak, Rhydon,Donphan,Flygon,Claydol,Groudon,Hippowdon, Rhyperior, Gliscor, Excadrill, Krookodile,Golurk,Landorus,TLandorus, Mudsdale, Sandaconda,Runerigus,Greattusk,Irontreads, Toedscruel,Stunfisk, GStunfisk]
rockmon=[Golem,AGolem, Omastar, Kabutops, Aerodactyl, Sudowoodo, Tyranitar,Lunatone,Solrock,Cradily,Armaldo,Regirock, Rampardos, Bastiodon, Probopass,Archeops,Terrakion, Barbaracle, Tyrantrum,Aurorus,Diancie, DLycanroc, MDLycanroc, MNLycanroc,Nihilego, Stakataka,Coalossal,Stonjourner,Klawf, Garganacl, Glimmora,Ironthorns,Carbink,Minior]
bugmon=[Butterfree,Beedrill, Parasect, Venomoth, Scyther, Pinsir, Ledian,Ariados, Forretress, Scizor, Shuckle,Heracross,Beautifly,Dustox, Masquerain,Ninjask,Shedinja,Volbeat,Illumise, Kricketune,SWormadam, TWormadam,Wormadam,Mothim,Vespiquen,Yanmega, Leavanny, Scolipede,Crustle, Escavalier, Galvantula,Accelgor,Durant,Volcarona, Genesect, Vivillon, Vikavolt, Ribombee,Golisopod,Buzzwole,Pheromosa,Orbeetle,Kleavor,Spidops,Lokix,Rabsca, Slitherwing]
steelmon=[Steelix,Skarmory,Mawile,Aggron,Metagross,Registeel, Bronzong,Dialga, Klinklang,Cobalion, Aegislash,Klefki,Magearna,Melmetal, Perrserker, Copperajah, Duraludon, Revavroom,Orthworm, Gholdengo]
ghostmon=[Gengar,GCorsola, Banette, Dusclops, Drifblim, Mismagius, Spiritomb, Dusknoir,Giratina, Cofagrigus,Chandelure,Trevenant,Gourgeist,Palossand,Mimikyu,Dhelmise,Polteageist,Cursola,Spectrier, Houndstone,Brambleghast,Fluttermane]
psychicmon=[ARaichu, Alakazam, GRapidash,Hypno,MrMime, GArticuno, Mewtwo,Mew,Xatu,Espeon,Wobbuffet,Lugia,Celebi, Gardevoir, Grumpig,Chimecho,ADeoxys,DDeoxys,SDeoxys,Deoxys,Gallade,Uxie,Mesprit,Azelf,Cresselia,Victini,Musharna,Swoobat,Sigilyph, Gothitelle,Reuniclus,Beheeyem,HBraviary, Meowstic,UHoopa,Tapulele, Solgaleo,Lunala,Necrozma,DWNecrozma,DMNecrozma, Hatterene,Indeedee,ICalyrex,SCalyrex,Espathra]
icemon=[ASandslash, ANinetales,Jynx, Articuno, Delibird, Glalie,Walrein,Regice,Glaceon, Mamoswine,Froslass,GDarmanitan, Vanilluxe,Beartic,Avalugg,HAvalugg,MrRime, Frosmoth,Eiscue,Glastrier,Cetitan, Ironbundle]
normalmon=[Eevee,Komala,Vigoroth,Pidgeot, Raticate, ARaticate,Fearow, Wigglytuff, Persian,Dodrio,Chansey, Kangaskhan,Tauros,Ditto,Snorlax,Furret, Noctowl, Ursaring, Porygon2, Smeargle,Miltank,Blissey, Linoone, Swellow, Slaking,Exploud, Delcatty,Spinda, Zangoose,Kecleon,Staraptor,Bibarel, Lopunny, Purugly, Lickilicky, PorygonZ, Regigigas, Arceus,Watchog, Stoutland, Unfezant,Audino,HZoroark, Cinccino, Sawsbuck, Bouffalant, Braviary,Meloetta,Diggersby,Toucannon,Gumshoos,Bewear
,Oranguru, Silvally,Drampa,Greedent,Dubwool,Wyrdeer,Ursaluna,Oinkologne, Dudunsparce, Farigiraf, Maushold]
allmon=firemon+watermon+fairymon+darkmon+dragonmon+grassmon+electricmon+fightingmon+flyingmon+poisonmon+groundmon+rockmon+bugmon+steelmon+ghostmon+psychicmon+icemon+normalmon
def allmonname(allmon):
    namelist=[]
    for i in allmon:
        x=i()
        if "Alpha" in x.name or "Totem" in x.name:
            x.name=x.name[6:]
        if "Z-Crystal" in x.name:
            x.name=x.name.split("(")[0]
        namelist.append(x.name)
    n=0
    namelist.sort()
    for i in namelist:
        n+=1
        print(str(n)+"."+i)
#allmonname(allmon)        
#SMOGON IMPORT
def smogonimport(spawn):
    name=spawn.name
    if "-" in name and "Porygon" not in name:
        name=name.split("-")[0]
    if "Low Key " in name:
        name=name.split(" ")[-1]+"-Low-Key"
    if "Amped " in name:
        name=name.split(" ")[1]+"-Amped"
    if "Pirouette " in name:
        name=name.split(" ")[1]+"-Pirouette"
    if "Resolute " in name:
        name=name.split(" ")[1]+"-Resolute"
    if "Ultra " in name:
        name=name.split(" ")[1]+"-Ultra"
    if "Dusk Mane " in name:
        name=name.split(" ")[1]+"-Dusk-Mane"
    if "Dawn Wings " in name:
        name=name.split(" ")[1]+"-Dawn-Wings"
    if "White " in name:
        name=name.split(" ")[1]+"-White"
    if "Black " in name:
        name=name.split(" ")[1]+"-Black"
    if "Primal " in name:
        name=name.split(" ")[1]+"-Primal"
    if "Origin " in name:
        name=name.split(" ")[1]+"-Origin"
    if "Therian " in name:
        name=name.split(" ")[1]+"-Therian"
    if "Sky " in name:
        name=name.split(" ")[1]+"-Sky"
    if "West Sea " in name:
        name=name.split(" ")[-1]
    if "East Sea " in name:
        name=name.split(" ")[1]+"-East"
    if "Midnight " in name:
        name=name.split(" ")[1]+"-Midnight"
    if "Dusk " in name:
        name=name.split(" ")[1]+"-Dusk"
    if "Midday " in name:
        name=name.split(" ")[1]
    if "Paldean " in name:
        name=name.split(" ")[1]+"-Paldea"
    if "Galarian " in name:
        name=name.split(" ")[1]+"-Galar"
    if "Alolan " in name:
        name=name.split(" ")[1]+"-Alola"
    if "Hisuian " in name:
        name=name.split(" ")[1]+"-Hisui"
    if "Mega " in name:
        name=name.split(" ")[1]+"-Mega"
    if "Alpha " in name:
        name=name.split(" ")[1]
    if "Totem " in name:
        name=name.split(" ")[1]
    if "(" in name:
        name=name.split("(")[0]
    if name in ["Wash Rotom","Frost Rotom","Fan Rotom","Mow Rotom","Heat Rotom"]:
        name=name.split(" ")[-1]+name.split(" ")[0]
    if spawn.item is not None and "✨" not in name:
        return (f'''\n {name} @ {spawn.item}  
 Ability: {spawn.ability}  
 EVs: {spawn.hpev} HP / {spawn.atkev} Atk / {spawn.defev} Def / {spawn.spatkev} SpA / {spawn.spdefev} SpD / {spawn.speedev} Spe  
 {spawn.nature} Nature
 IVs: {spawn.hpiv} HP / {spawn.atkiv} Atk / {spawn.defiv} Def / {spawn.spatkiv} SpA / {spawn.spdefiv} SpD / {spawn.speediv} Spe    
 - {spawn.moves[0]}  
 - {spawn.moves[1]}  
 - {spawn.moves[2]}
 - {spawn.moves[3]}'''
)
    if spawn.item is not None and "✨" in name:
        return (f'''\n{name} @ {spawn.item}  
Ability: {spawn.ability}  
Shiny: Yes
EVs: {spawn.hpev} HP / {spawn.atkev} Atk / {spawn.defev} Def / {spawn.spatkev} SpA / {spawn.spdefev} SpD / {spawn.speedev} Spe  
{spawn.nature} Nature
IVs: {spawn.hpiv} HP / {spawn.atkiv} Atk / {spawn.defiv} Def / {spawn.spatkiv} SpA / {spawn.spdefiv} SpD / {spawn.speediv} Spe    
- {spawn.moves[0]}  
- {spawn.moves[1]}  
- {spawn.moves[2]}
- {spawn.moves[3]}'''
)
    if spawn.item is None:
        return (f'''\n{name}
Ability: {spawn.ability}  
EVs: {spawn.hpev} HP / {spawn.atkev} Atk / {spawn.defev} Def / {spawn.spatkev} SpA / {spawn.spdefev} SpD / {spawn.speedev} Spe  
{spawn.nature} Nature
IVs: {spawn.hpiv} HP / {spawn.atkiv} Atk / {spawn.defiv} Def / {spawn.spatkiv} SpA / {spawn.spdefiv} SpD / {spawn.speediv} Spe    
- {spawn.moves[0]}  
- {spawn.moves[1]}  
- {spawn.moves[2]}
- {spawn.moves[3]}'''
)

#smogonimport(spawn)
def smogonexport(line):
    name=line.split(" @")[0]
    item=line.split("\nAbility")[0].split("@ ")[1]
    ability=line.split("Ability: ")[1].split("\nEVs")[0]
    print(name)
    print(item)
    print(ability)
    

