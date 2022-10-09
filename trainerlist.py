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
    legendary=[Registeel,Regirock,Regice,Articuno,Zapdos,Moltres,Raikou,Entei,Suicune,Lugia,Hooh,Celebi,Deoxys,ADeoxys,SDeoxys,DDeoxys,Jirachi,Mew,Rayquaza,Latias,Latios,MLatias,MLatios]
    #FIGHTING SPECIALIST 
    if trclass in ["Dojo Master",",Blackbelt"]:
        namelist=["Taishi","Damme","Wesley","Joe","Dolph"]
        nn=random.choice(namelist)
        new_name=trclass+" "+nn
        mons=[MGallade,Gallade,Machamp,Poliwrath,Hitmonchan,Hitmonlee,Infernape,Blaziken,Breloom,Primeape,Heracross,MHeracross,Hariyama,MMedicham]
   #ELDER TRAINERS     
    if trclass =="Elder Trainer":
        namelist=["Jules","Shriner","Jason","Apollo","Damon","Castor","Marcus","Henry","Orion","Arthur","Julius","Zephyr","Helios","Liam","Odysseus","Albert","Helios"]
        nn=random.choice(namelist)
        new_name=trclass+" "+nn
        mons=[Groudon,Kyogre,Rayquaza,Mew,Regice,Regirock,Registeel,Aerodactyl,Kabutops,Omastar,Armaldo,Cradily,Rampardos,Bastiodon,Cloyster,Relicanth,Claydol,Arcanine,Mamoswine,Spiritomb,Lunatone,Solrock,Yanmega]
        mons+=random.choices([Rayquaza,Latias,Latios,Regice,Regirock,Registeel,Kyogre,Groudon,Entei,Suicune,Raikou],k=1)
    if trname is None and trclass not in ["Elder Trainer","Dojo Master",",Blackbelt"]:
        namelist=["Josh","Kyler","Jade","John","Joey","Jan","Gabriel","Jamie","Kylie","Andrea","Evy","Ebba","Titus","Emiliano","Emilia","Natalie","Justin","Anastasia","Frannie","Danielle","Daniel","Hugo","Robert","Carlos","Alex","Alexander","Alexandra","Arslan","Johan","Mike","Julian","Selena","Emmanuel","Kristin","Lawrence","Frank","Pamela","Nicole","Emma","Matthew"]
        nn=random.choice(namelist)
        new_name=trclass+" "+nn
     #WATER SPECIALISTS
    if trclass in ["Marine Biologist","Surfer","Scuba Diver","Swimmer","Sailor"]:
        mons=[EGastrodon,WGastrodon,Empoleon,Walrein,Huntail,Gorebyss,Relicanth,Milotic,Crawdaunt,Whiscash,Dewgong,Sharpedo,Pelipper,Kingdra,Politoed,Azumarill,Feraligatr,Lanturn,Lapras,Gyarados,Slowbro,Cloyster,Starmie, Blastoise,Poliwrath,Swampert,Ludicolo]+random.choices([Kyogre, Wailord],k=1)
        pass
#DRAGON SPECIALISTS
    if trclass in ["Dragon Tamer"]:
        mons=[Yanmega,Garchomp,MGarchomp,Gyarados,MGyarados,Dragonite,Kingdra,Charizard,Aerodactyl,Tyranitar, Salamence,MSalamence,MAerodactyl,MCharizardX,MTyranitar,Feraligatr]+random.choices([Latias,Latios,MLatias,MLatios],k=1)
        #POISON SPECIALISTS
    if trclass in ["Venom Expert"]:
        mons=[Toxicroak,Drapion,Roserade,Seviper,Arbok,Weezing,Crobat,MBeedrill,Venusaur,Nidoking,Nidoqueen,Victreebel,Tentacruel,Muk,Gengar,Overqwil]
        #FIRE SPECIALISTS
    if trclass in ["Kindler"]:
        mons=[Magmortar,Infernape,Arcanine,Rapidash,Houndoom,Flareon,Typhlosion,Blaziken,Camerupt,Charizard,MCharizardY]
        #DECENT TRAINERS
    if trclass in ["Expert","Veteran"]:
        mons=[Yanmega,Magnezone,Tangrowth,Hippowdon,Lucario,Mismagius,Luxray,Roserade,Torterra,Glalie,Absol,Banette,Milotic,Armaldo,Cradily,Aggron,Hariyama,Breloom,Gardevoir,Swellow,Ludicolo,Swampert,Houndoom,Heracross,Steelix,Espeon,Ampharos,Flareon,Jolteon,Vaporeon,Snorlax,Lapras,Gyarados,Tauros,Kangaskhan,Hitmonchan,Hitmonlee,Exeggutor,Gengar,Dodrio,Slowbro,Rapidash,AGolem,Victreebel,Machamp,Golduck,Alakazam,Pidgeot,Blastoise,Ninetales,Primeape,MBeedrill, Venusaur, Charizard,Cloyster,MBanette,MGlalie]
        ch=random.randint(1,15)
        if ch==7:
            mons+=random.choices(legendary,k=1)
        pass
#THUGS
    elif trclass in[ "Street Punk","Biker","Cueball"]:
        namelist=["Josh","Kyler","Jade","John","Jan","Gabriel","Jamie","Emiliano","Justin","Frannie","Danielle","Daniel","Hugo","Robert","Carlos","Alex","Alexander","Arslan","Johan","Mike","Julian","Emmanuel","Kristin","Murphy"]
        nn=random.choice(namelist)
        new_name=trclass+" "+nn
        mons=[PorygonZ,Magmortar,Magnezone,Electivire,Rhyperior,Drapion,Toxicroak,Mismagius,Luxray,Infernape,Absol,Farigarif,Crawdaunt,Seviper,Zangoose,Overqwil,Sharpedo,MManectric,MAggron,Hariyama,Breloom,Shiftry,Blaziken,MHoundoom,Skarmory,Scizor,Azumarill,Typhlosion,Gyarados,Pinsir,Weezing,Muk,Tentacruel,Primeape,Machamp,Golem,Cloyster,MSableye,MMawile,Crobat,Arbok]
        ch=random.randint(1,10)
        if ch==7:
            mons+=random.choices(legendary,k=1)
        pass 
        #FLYING SPECIALISTS
    elif trclass in ["Bird Keeper","Pilot","Sky Diver"]:
        mons=[Gliscor,Togekiss,Honchkrow,Staraptor,Empoleon,Flygon,Salamence,Pelipper,Swellow,MPidgeot,Charizard,Skarmory,Aerodactyl,Altaria,Crobat,Dodrio,Dragonite]
        mons+=random.choices([Articuno,Zapdos,Moltres,Latias,Latios,MLatias,MLatios],k=1)
        #ANIMAL LOVERS
    elif trclass == "Zoologist":
        mons=[Gliscor,Ambipom,Torterra,Farigarif,MAltaria,Sceptile,Houndoom,Tauros,Kangaskhan,Rapidash,Dodrio, Victreebel,Arcanine,Breloom]
        #ICE SPECIALISTS
    elif trclass == "Skier":
        mons=[Weavile,Abomasnow,Walrein,Lapras,Mamoswine,Glalie,MGlalie,Jynx,Cloyster,ANinetales,MAbomasnow]
        ch=random.randint(1,10)
        if ch==7:
            mons+=[Articuno]
     #BETTER TRAINERS
    elif trclass == "Ace Trainer":
        mons=[PorygonZ,Gliscor,Yanmega,Togekiss,Electivire,Rhyperior,Magnezone,Lucario,Drifblim,Roserade,Staraptor,Empoleon,Torterra,Infernape,Metagross,Salamence,Absol,Milotic,Altaria,Flygon,Wailord,MManectric,MGardevoir,Swellow,Ludicolo,Swampert,Blaziken,Kingdra,MHoundoom,Skarmory,Heracross,Scizor,MSteelix,Espeon,Umbreon,MAmpharos,Feraligatr,Typhlosion,Meganium,Dragonite,Snorlax,MGyarados,Tauros,MPinsir,Starmie,AMuk,AExeggutor,MGengar,Cloyster,MSlowbro,Golem,MAlakazam,MPidgeot,Poliwrath,Arcanine,ANinetales,Nidoking, Nidoqueen,MCharizardY,MVenusaur,MBlastoise,MSceptile,MCamerupt]
        ch=random.randint(1,5)
        if ch==3:
            mons+=random.choices(legendary,k=1)
            
        pass
#CHALLENGERS
    elif trclass == "Challenger":
        level=random.randint(70,74)
        mons=[Togekiss,Magnezone,Garchomp,Infernape,Latias,Latios,Metagross,Salamence,Slaking,Blissey,Kingdra,Skarmory,Umbreon,Crobat,Cloyster,Starmie,AExeggutor,Lapras,Typhlosion,Feraligatr,Meganium,Arcanine,Snorlax,Dragonite]+[MSharpedo,MScizor,MSteelix,MGyarados,MKangaskhan,MAlakazam,MPidgeot,MSlowbro,MAerodactyl,MBlastoise,MVenusaur,MCharizardX,MCharizardY,MHeracross,MHoundoom,MSceptile, MBlaziken,MSwampert,MGardevoir,MCamerupt,MAbsol,MSalamence,MMetagross,MLopunny,MLucario]
        ch=random.randint(1,3)
        if ch==2:
            mons+=random.choices(legendary,k=1)
        pass
#ROCK SPECIALISTS
    elif trclass in ["Ruin Explorer","Fossil Maniac","Paleontologist"]:
     mons=[Rhyperior,Bastiodon,Rampardos,Relicanth,Absol,Claydol,Armaldo,Cradily,Solrock,Lunatone,Mamoswine,Aggron,Steelix,Machamp,MAerodactyl,Golem,Omastar,Kabutops,Swampert,Tyranitar]
    
    
    if len(team)==0:
        while len(team)!=pknum:
            level=100#random.randint(96,100)
           
            party=random.choices(mons,k=1)[0]
            member=party(maxiv="Yes",level=level)
        
            if len(team)<(pknum-1) and "Mega " not in member.name and "Z-Crystal" not in member.name:
                team.append(member)
                clist.append(party)
            if len(team)==(1) and "Z-Crystal" in member.name and "Mega " not in member.name :
                if member not in team:
                    team.append(member)
            if len(team)==(pknum-1) and "Mega " in member.name and "Z-Crystal" not in member.name :
                if member not in team:
                    team.append(member)
            if len(team)==(pknum-1) and "Mega " not in member.name and "Z-Crystal" not in member.name:
                if member not in team:
                    team.append(member)
            if party in clist:
                mons.remove(party)
            else:
                #member=MBeedrill(level)
#                team.append(member)
                pass
            
    return new_name,team
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
red6=Espeon(maxiv="Yes",move=["Psychic","Dazzling Gleam","Recover","Shadow Ball"],nature="Modest")
red=Trainer("Pokémon Trainer Red",[red4,red5,red6,red2,red3,red1],"Kanto")
#E4 Agatha
agatha1=Crobat(maxiv="Yes",move=["Roost","Toxic","Brave Bird","U-Turn"],nature="Jolly")
agatha2=Gengar(maxiv="Yes",move=["Thunderbolt","Sludge Bomb","Shadow Ball","Nasty Plot"],nature="Timid")
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
wallace5=Swampert(maxiv="Yes",move=["Earthquake","Liquidation","Ice Punch","Hammer Arm"],nature="Adamant")
wallace6=Milotic(maxiv="Yes",move=["Scald","Toxic","Ice Beam","Recover"],nature="Modest")
wallace=Trainer("Hoenn Champion Wallace",[wallace1,wallace2,wallace3,wallace4,wallace5,wallace6],"Hoenn")




def genTrainer(name=None,num=6):
    trclasslist=["Blackbelt","Dojo Master","Dragon Tamer","Skier","Kindler","Sailor","Swimmer","Veteran","Elder Trainer","Challenger","Zoologist","Ruin Explorer","Ace Trainer","Expert","Street Punk","Scuba Diver","Fossil Maniac","Paleontologist","Surfer","Marine Biologist","Biker","Cueball","Bird Keeper","Pilot","Sky Diver","Venom Expert"]
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
#############
matchx=match()
p1=matchx[0]
p2=matchx[1]
#p1=random.choice([matchx[0],matchx[1]])
#p2=random.choice([red,lance,bruno,lorelei,agatha,steven,wallace])
showparty(p1)
print("")
showparty (p2)
mon1=p1.pokemons[random.randint(1,len(p1.pokemons))-1]
mon2=p2.pokemons[random.randint(1,len(p2.pokemons)-1)]
