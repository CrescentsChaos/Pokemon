#pylint:disable=C0114
#pylint:disable=R0912
#pylint:disable=C0303
#pylint:disable=C0116
#pylint:disable=W0401
#pylint:disable=C0301
#pylint:disable=C0304
from pokemonbase2 import *
firemon=[Charizard, MCharizardY, MCharizardX, Arcanine, HArcanine, Rapidash,AMarowak,Flareon, Typhlosion,Moltres,HTyphlosion, Magcargo,Entei,Hooh,Blaziken,MBlaziken, Camerupt,MCamerupt, Infernape, Magmortar,Heatran,Emboar,Simisear, Darmanitan,Heatmor,Delphox,Talonflame,Pyroar,Volcanion, Incineroar, Turtonator, Cinderace, Blacephalon, Centiskorch, Skeledirge,Ironmoth, Armarouge, Ceruledge]
watermon=[Blastoise, MBlastoise,Golduck, Poliwrath,Tentacruel,Slowbro, MSlowbro,Dewgong, Cloyster,Kingler,Kingdra,Seaking,Starmie,Gyarados,MGyarados,Lapras, Vaporeon, Feraligatr, Lanturn, Azumarill,Politoed, Quagsire, Slowking,Corsola,Octillery, Mantine,Suicune, Swampert,MSwampert, Ludicolo,Pelipper,Sharpedo, MSharpedo,Wailord,Whiscash, Crawdaunt, Milotic,Huntail,Gorebyss,Relicanth,Kyogre, PKyogre,Empoleon,Floatzel, EGastrodon, WGastrodon, Lumineon,Palkia,OPalkia,Phione, Samurott,HSamurott,Simipour, Seismitoad, Basculegion,Carracosta,Swanna, Jellicent,Keldeo, Greninja, Clawitzer,Primarina,SWishiwashi, Araquanid,Tapufini,Inteleon,Drednaw,Barraskewda,Dracovish, Quaquaval,Wugtrio, Dondozo,Veluza,Palafin]
fairymon=[Clefable,Granbull,Togekiss,Florges,EFloette,Slurpuff,Sylveon,Xerneas, Alcremie,Dachsbun, Enamorus, Zacian, Screamtail, Ironvaliant, Tinkaton]
darkmon=[APersian,GMoltres,Umbreon, Weavile, Honchkrow, Houndoom, MHoundoom,Mightyena, Obstagoon, Sableye, MSableye,Absol, MAbsol,Darkrai,Liepard,Scrafty,Zoroark, Bisharp, Kingambit, Mandibuzz, Hydreigon,Malamar,Yveltal,Guzzlord, Grimmsnarl,Zarude, Overqwil, Mabosstiff, Ironjugulis,Tinglu, Chienpao,Wochien,Chiyu]
dragonmon=[Dragonite, Altaria, MAltaria, Salamence, MSalamence,Latios,MLatios,Latias,MLatias, Rayquaza,MRayquaza, Garchomp, MGarchomp, Haxorus, Druddigon,Reshiram,Zekrom,Kyurem,BKyurem,WKyurem,Goodra,HGoodra, CZygarde,Kommo,Dragapult,Regidrago, Baxcalibur, Tatsugiri,Cyclizar, Roaringmoon]
allmon=firemon+watermon+fairymon+darkmon+dragonmon
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
