#pylint:disable=C0114
#pylint:disable=R0912
#pylint:disable=C0303
#pylint:disable=C0116
#pylint:disable=W0401
#pylint:disable=C0301
#pylint:disable=C0304
from pokemonbase2 import *
allmon=[Venusaur,MVenusaur,Charizard,MCharizardX,MCharizardY,Blastoise,MBlastoise,MBeedrill,Pidgeot,MPidgeot,Arbok, Nidoking,Nidoqueen,Ninetales,Golduck,Primeape,Arcanine,Poliwrath, Alakazam,MAlakazam,Machamp,Victreebel,Tentacruel,Golem,Rapidash,Slowbro,MSlowbro,Dodrio,Dewgong,Muk,Cloyster,Gengar,MGengar,Exeggutor,Hitmonchan,Hitmonlee,Weezing,Kangaskhan,MKangaskhan,Starmie,Tauros,Jynx,Pinsir,MPinsir,Gyarados,MGyarados,Lapras,Jolteon,Vaporeon,Flareon,Omastar,Kabutops,Aerodactyl,MAerodactyl,Snorlax,Dragonite, Sceptile,MSceptile,Blaziken,MBlaziken,Swampert,MSwampert,Mightyena,Ludicolo,Shiftry,Swellow,Pelipper,Gardevoir,MGardevoir,Breloom, Slaking,Exploud,Hariyama,MSableye,MMawile,Aggron,MAggron,Medicham,MMedicham,MManectric,Sharpedo,MSharpedo,Wailord,Camerupt,MCamerupt,Torkoal,Flygon,Altaria,MAltaria,Zangoose,Seviper,Solrock,Lunatone,Whiscash,Crawdaunt,Claydol,Cradily,Armaldo,Milotic,Banette,MBanette,Absol,MAbsol,Glalie,MGlalie,Walrein,Huntail,Gorebyss,Relicanth,Salamence,MSalamence,Metagross,MMetagross,Torterra,Infernape,Empoleon,Staraptor,Luxray,Roserade,Rampardos,Bastiodon,Vespiquen,EGastrodon,WGastrodon,Ambipom,Drifblim,MLopunny,Mismagius,Honchkrow,Purugly,Skuntank,Bronzong,Spiritomb,Garchomp,Lucario,MLucario,Hippowdon,MGarchomp,Drapion,Toxicroak,Abomasnow,MAbomasnow,Weavile,Magnezone,Rhyperior,Tangrowth,Electivire,Magmortar,Togekiss,Yanmega,Gliscor,Gallade,MGallade,Probopass,Dusknoir,Froslass,WRotom,Serperior,Emboar,Samurott,Stoutland,Unfezant,Zebstrika,Gigalith,Excadrill,Conkeldurr,Seismitoad,Leavanny,Scolipede,Krookodile,Darmanitan,Scrafty,Cofagrigus,Carracosta,Archeops,Zoroark,Gothitelle, Reuniclus, Swanna,Vanilluxe,Escavalier,Jellicent,Galvantula,Ferrothorn,Eelektross,Chandelure,Haxorus,Beartic,Accelgor,Mienshao,Druddigon,Golurk,Bisharp,Bouffalant,Braviary,Mandibuzz,Heatmor,Durant,Hydreigon,Volcarona,GArticuno,GZapdos,GMoltres,Melmetal,Zeraora,Silvally,Marshadow,Magearna,Tapufini,Tapubulu,Tapulele,Tapukoko,Diancie,MDiancie,UHoopa,Volcanion,CZygarde,Xerneas,Yveltal,Genesect,Keldeo,Meloetta,PMeloetta,BKyurem,WKyurem,Zekrom,Reshiram,Kyurem,TLandous,TThundurus,TTornadus,Thundurus,Tornadus,Landous,Victini,Cobalion,Terrakion,Virizion,Arceus,Shaymin,SShaymin,Darkrai,Cresselia,Manaphy,Uxie,Azelf,Mesprit,Registeel,Regirock,Regice,Articuno,Zapdos,Moltres,Raikou,Entei,Suicune,Lugia,Hooh,Celebi,Deoxys,ADeoxys,SDeoxys,DDeoxys,Jirachi,Mew,Rayquaza,Latias,Latios,MLatias,MLatios,Groudon,Kyogre,PGroudon,PKyogre,MRayquaza,Mewtwo,Dialga,ODialga,Palkia,OPalkia,Giratina,OGiratina,Heatran,Regigigas,Blacephalon,Stakataka,Naganadel,UNecrozma,Necrozma,DMNecrozma,DWNecrozma,FMLunala,RSSolgaleo,Lunala,Solgaleo,Guzzlord,Kartana,Celesteela,Xurkitree,Buzzwole,Nihilego,Pheromosa]
pokemon=random.choice(allmon)
#SMOGON IMPORT
def smogonimport(spawn):
    name=spawn.name
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
    if "Z-Crystal" in name:
        name=name.split("(")[0]
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
