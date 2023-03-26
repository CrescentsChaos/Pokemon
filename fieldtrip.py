from trainerlistx import *
def wild(self):
    mon=self(maxiv="Yes",hpev=252,atkev=252,defev=252,spatkev=252,speedev=252,item="Wild DNA")
    mon.name="Wild "+mon.name
    tr=Trainer("Wild",[mon])
    return tr
def pprestore(self):
    self.pplist=[20,20,20,20]
    if self.moves[0] in typemoves.pp15:
      self.m1pp=self.mx1pp=15
    if self.moves[0] in typemoves.pp10:
       self.m1pp=self.mx1pp=10
    if self.moves[0] in typemoves.pp5:
        self.m1pp=self.mx1pp=5
    if self.moves[1] in typemoves.pp15:
        self.m2pp=self.mx2pp=15
    if self.moves[1] in typemoves.pp10:
        self.m2pp=self.mx2pp=10
    if self.moves[1] in typemoves.pp5:
       self.m2pp=self.mx2pp=5
    if self.moves[2] in typemoves.pp15:
       self.m3pp=self.mx3pp=15
    if self.moves[2] in typemoves.pp10:
        self.m3pp=self.mx3pp=10
    if self.moves[2] in typemoves.pp5:
        self.m3pp=self.mx3pp=5
    if self.moves[3] in typemoves.pp15:
        self.m4pp=self.mx4pp=15
    if self.moves[3] in typemoves.pp10:
        self.m4pp=self.mx4pp=10
    if self.moves[3] in typemoves.pp5:
        self.m4pp=self.mx4pp=5
    self.pplist=[self.m1pp,self.m2pp,self.m3pp,self.m4pp]        
def heal (tr):
    print(colored(" Nurse Joy:","magenta")+f" {tr.name}, your pokemons were healed!\n")
    tr.hazard=[]
    tr.lightscreen=False
    tr.reflect=False
    tr.tailwind=False
    tr.auroraveil=False
    tr.wishhp=False
    tr.sub="None"
    tr.faintedmon=[]
    for i in tr.pokemons:
        transformation(i,Pikachu(),0)
        i.perishturn=0
        i.dbond=False
        i.atkb=i.defb=i.spatkb=i.spdefb=i.speedb=1
        if i.teratype!="None":
            i.name=i.name.split("-")[0]
            i.teratype="None"
        i.hp=i.maxhp
        if "Used" in i.item:
            i.item=i.item.split("[")[0]
        i.status="Alive"
        while len(i.moves)!=4:
            for x in i.lostmoves:
                i.moves.append(x)                        
        pprestore(i)     
    tr.cantera=True
    tr.canmax=True
    tr.canmega=True           
def genplayer2(f):
    pl=red
    field.weather="Clear"
    field.terrain="Normal"    
    #Regions
    if "Kanto" in f.location:
        pl=random.choices([random.choice([lorelei,bruno,agatha, lance,brock,misty,surge,erika,sabrina,janine,blaine,ash,gary,red,giovanni,jessiejames]),genTrainer(trclass=random.choice(["Kanto Trainer"])),genTrainer(trclass=random.choice(allclass))],weights=[1,7,4],k=1)[0]
        
    if "Hoenn" in f.location:
        pl=random.choices([random.choice([noland,lucy,tucker,greta,anabel,brandon,spenser,brendan,may,roxanne,brawly,wattson,flannery,norman,winona,tate,liza,juan,steven,wallace,sidney,phoebe,drake,glacia,zinnia,archie,maxie,tabitha,matt,shelly,courtney,jessie,james,jessiejames]),genTrainer(trclass=random.choice(allclass)),genTrainer(trclass="Hoenn Trainer")],weights=[1,7,4],k=1)[0]
        
    if "Paldea" in f.location:
        pl=random.choices([random.choice([tyme,salvatore,miriam,dendra,raifort,jacq,saguaro,tulip,grusha,ryme,kofu,Iono,brassius,katy,penny,eri,ortega,atticus,mela,giacomo,hassel,larry,poppy,rika,geeta,clavell,arven]),genTrainer(trclass=random.choice(allclass)),genTrainer(trclass="Paldea Trainer")],weights=[1,7,4],k=1)[0]
        
    if "Johto" in f.location:
        pl=random.choices([random.choice([ethan,silver,falkner,bugsy,whitney,chuck,pryce,jasmine,clair,will,bruno,karen,lance, koga]),genTrainer(trclass=random.choice(allclass)),genTrainer(trclass="Johto Trainer")],weights=[1,7,4],k=1)[0]
        
    if "Sinnoh" in f.location:
        pl=random.choices([random.choice([dawn,kenny,ursula,trip,drew,riley,cheryl,marley,mira,nando,conway,zoey,cynthia,aaron,lucian,bertha,flint,roark,gardenia,fantina,byron,maylene,wake,candice,volkner,cyrus,mars,jupiter,saturn,palmer,darach,dahlia,argenta,Thorton]),genTrainer(trclass=random.choice(allclass)),genTrainer(trclass="Sinnoh Trainer")],weights=[1,7,4],k=1)[0]
        
    if "Kalos" in f.location:
        pl=random.choices([random.choice([wulfric,olympia,valerie,clemont,ramos,korrina,viola,grant,diantha,alain,sawyer,tierno, shauna,trevor,calem]),genTrainer(trclass=random.choice(allclass)),genTrainer(trclass="Kalos Trainer")],weights=[1,7,4],k=1)[0]
        
    if "Alola" in f.location:
        pl=random.choice([Lillie,mallow,lana,kiawe,Ilima, lusamine,kahili,acerola,olivia,molayne,hala,kukui,gladion,hau,genTrainer(trclass=random.choice(allclass)),genTrainer(trclass="Alola Trainer")])
        
    if " Galar" in f.location:
        pl=random.choices([random.choice([raihan,marnie,piers,melony,gordie,bede,opal,allister,bea,kabu,nessa,milo,leon,hop,rose,mustard]),genTrainer(trclass=random.choice(allclass)),genTrainer(trclass="Galar Trainer")],weights=[1,7,4],k=1)[0]
        
    if "Unova" in f.location:
        pl=random.choices([random.choice([alder,iris,ash,lenora,burgh,elesa,clay,skyla,brycen,drayden,cheren,roxie,marlon]),genTrainer(trclass=random.choice(allclass)),genTrainer(trclass="Unova Trainer")],weights=[1,10,4],k=1)[0]
        
    if "Team Flare" in f.location:
        pl=random.choice([malva,xerosic,aliana,celosia,bryony,mable,lysandre])
        if "Malva" in pl.name:
            pl.name=colored("Team Flare Malva","red")
            
    if "Trackless" in f.location:
        pl=random.choice([wild(Raikou),wild(Entei),wild(Suicune),anabel,genTrainer(trclass=random.choice(["Hiker"]))])
        
    if "Twist Mountain" in f.location:
        pl=random.choice([cheren,genTrainer(trclass=random.choice(["Ace Trainer","Hiker","Battle Girl","Worker","Doctor","Black Belt","Veteran","Nurse"]))])
        
    if "Scorched Slab" in f.location:
        pl=random.choice([wild(Heatran),buck,genTrainer(trclass=random.choice(["Volcano Explorer","Hiker"]))])
    
    if "Power Plant" in f.location:
        field.weather="Electric Terrain"
        pl=random.choice([wild(Zapdos),surge,genTrainer(trclass=random.choice(["Rocket Grunt","Electrician","Scientist","Coach Trainer"]))])
        
    if "Mt. Ember" in f.location:
        field.weather="Sunny"
        pl=random.choice([wild(Moltres),blaine,genTrainer(trclass=random.choice(["Rocket Grunt","Kindler"]))])
        
    if "Mt. Chimney" in f.location:
        pl=random.choice([maxie,tabitha,brendan,archie,matt,genTrainer(trclass=random.choice(["Magma Grunt","Aqua Grunt"]))])
        
    if "Mt. Pyre" in f.location:
        pl=random.choice([phoebe,maxie,archie,genTrainer(trclass=random.choice(["Exorcist","Aqua Grunt","Magma Grunt","Channeler"]))])
        
    if "Marine Cave" in f.location:
        f.weather="Primordial Sea"
        pl=random.choice([wild(Kyogre),archie,brendan,may,genTrainer(trclass=random.choice(["Aqua Grunt"]))])
        
    if "Terra Cave" in f.location:
        f.weather="Desolate Land"
        pl=random.choice([wild(Groudon),maxie,tabitha,brendan,may,genTrainer(trclass=random.choice(["Magma Grunt"]))])
        
    if "Aqua Hideout" in f.location:
        pl=random.choice([archie,matt,shelly,genTrainer(trclass=random.choice(["Aqua Grunt"]))])
        
    if "Magma Hideout" in f.location:
        pl=random.choice([maxie,tabitha,courtney,genTrainer(trclass=random.choice(["Magma Grunt"]))])
        
    if "Mountain Coronet" in f.location:
        pl=random.choice([cyrus,cynthia,mars,jupiter,saturn,lucas,dawn,barry,genTrainer(trclass=random.choice(["Sinnoh Trainer","Galactic Grunt"]))])
        
    if "Spear Pillar" in f.location:
        pl=random.choice([wild(Dialga),wild(Palkia),wild(Giratina),cyrus,cynthia,mars,jupiter,saturn,lucas,dawn,barry])
        
    if "Mountain Stark" in f.location:
        pl=random.choice([wild(Heatran),buck,saturn,candice,byron,mira,palmer,tobias,genTrainer(trclass=random.choice(["Sinnoh Trainer","Fire Breather","Kindler","Paleontologist","Hiker"]))])
        
    if "League, Sinnoh" in f.location:
        pl=random.choice([aaron,bertha,flint,lucian,cynthia,tobias,barry])
        if "Tobias" in pl.name:
            pl.name=colored("SCL Champion Tobias","red")
            
    if "Evergrande" in f.location:
        pl=random.choice([sidney,phoebe,glacia,drake,steven,wallace])
        
    if "Sootopolis City" in f.location:
        pl=random.choice([juan,wallace,genTrainer(trclass=random.choice(["Swimmer","Hoenn Trainer","Scuba Diver","Fisherman"]))])
        
    if "Mosdeep City" in f.location:
        pl=random.choice([tate,liza,steven,maxie,genTrainer(trclass=random.choice(["Hoenn Trainer","Psychic"]))])
        
    if "Fortree City" in f.location:
        pl=random.choice([winona,steven,may,genTrainer(trclass=random.choice(["Hoenn Trainer","Pilot","Air Force Officer"]))])
        
    if "Lavaridge Town" in f.location:
        pl=random.choice([flannery,may,brendan,genTrainer(trclass=random.choice(["Hoenn Trainer","Kindler","Fire Breather"]))])
        
    if "Mauville City" in f.location:
        pl=random.choice([wattson,wally,may,genTrainer(trclass=random.choice(["Hoenn Trainer","Rocker","Guitarist"]))])
        
    if "Dewford Town" in f.location:
        pl=random.choice([brawly,steven,genTrainer(trclass=random.choice(["Hoenn Trainer","Black Belt","Dojo Master","Crush Girl"]))])
        
    if "Sunnyshore City" in f.location:
        pl=random.choice([volkner,jasmine,flint,paul,genTrainer(trclass=random.choice(["Sinnoh Trainer","Electrician","Rocker","Guitarist"]))])
        
    if "Snowpoint City" in f.location:
        field.weather="Snowstorm"
        pl=random.choice([candice,brandon,tobias,paul,genTrainer(trclass=random.choice(["Sinnoh Trainer","Galactic Grunt","Skier","Boarder"]))])
        
    if "Canalave City" in f.location:
        pl=random.choice([byron,roark,paul,barry,genTrainer(trclass=random.choice(["Sinnoh Trainer","Industry Worker","Factory Boss","Electrician","Sailor"]))])
        
    if "Hearthome City" in f.location:
        pl=random.choice([fantina,paul,barry,genTrainer(trclass=random.choice(["Sinnoh Trainer","Exorcist"]))])
        
    if "Pastoria City" in f.location:
        pl=random.choice([wake,paul,genTrainer(trclass=random.choice(["Sinnoh Trainer","Black Belt","Swimmer","Fisherman"]))])
        
    if "Veilstone City" in f.location:
        pl=random.choice([maylene,cyrus,saturn,paul,genTrainer(trclass=random.choice(["Sinnoh Trainer","Galactic Grunt","Black Belt"]))])
        
    if "Eterna City" in f.location:
        pl=random.choice([gardenia,saturn,paul,genTrainer(trclass=random.choice(["Sinnoh Trainer","Gardener","Galactic Grunt"]))])
        
    if "Oreburgh City" in f.location:
        pl=random.choice([roark,paul,genTrainer(trclass=random.choice(["Sinnoh Trainer","Paleontologist","Ruin Maniac"]))])
        
    if "Rustboro City" in f.location:
        pl=random.choice([roxanne,genTrainer(trclass=random.choice(["Hoenn Trainer","Paleontologist","Aqua Grunt","Ruin Maniac"]))])
        
    if "Petalburg City" in f.location:
        pl=random.choice([norman,wally,genTrainer(trclass=random.choice(["Hoenn Trainer","Bug Catcher","Bug Researcher"]))])
        
    if "Twinleaf Town" in f.location:
        pl=random.choice([barry,genTrainer(trclass=random.choice(["Sinnoh Trainer"]))])
        
    if "Littleroot Town" in f.location:
        pl=random.choice([brendan,norman,may,genTrainer(trclass=random.choice(["Hoenn Trainer"]))])
        
    if "Cianwood City" in f.location:
        pl=random.choice([horace,chuck,genTrainer(trclass=random.choice(["Black Belt","Dojo Master"]))])
        
    if "Azalea City" in f.location:
        pl=random.choice([bugsy,genTrainer(trclass="Bug Catcher")])
        
    if "Blackthorn City" in f.location:
        pl=random.choice([clair,genTrainer(trclass="Dragon Tamer")])
        
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
        pl=random.choice([wild(Articuno),blaine,genTrainer(trclass=random.choice(["Skier","Boarder","Coach Trainer","Beauty","Ace Trainer"]))])        
        
    if "Rock Tunnel" in f.location or "Mount Moon" in f.location:
        pl=random.choice([silver,genTrainer(trclass=random.choice(["Hiker","Paleontologist","Lass","Bug Catcher","Super Nerd","Rocket Grunt"]))])
        
    if f.location in ["Victory Road, Kanto","Victory Road, Hoenn"]:
        pl=genTrainer(trclass=random.choice(["Ace Trainer","Challenger","Dragon Tamer","Cool Trainer","Black Belt","Juggler","Tamer","Poké Maniac","Coach Trainer","Hiker","Scientist"]))
    if "Navel Rock" in f.location:        
        pl=random.choice([wild(Lugia),wild(Hooh)])
    if "Whirl Island" in f.location:        
        pl=random.choice([wild(Lugia)])
    if "Bell Tower" in f.location:        
        pl=random.choice([wild(Hooh),morty])
    if "Snowpoint Temple" in f.location:        
        pl=random.choice([brandon,palmer,wild(Registeel),wild(Regice),wild(Regirock),wild(Regigigas)])
    if "Iron Ruins" in f.location:        
        pl=random.choice([wild(Registeel)])
    if "Iceberg Ruins" in f.location:        
        pl=random.choice([wild(Regice)])
    if "Rock Peak Ruins" in f.location:        
        pl=random.choice([wild(Regirock)])
    if "Pokémon Mansion" in f.location:        
        pl=random.choice([wild(Mewtwo),blaine,giovanni])
    if "Faraway Island" in f.location:        
        pl=random.choice([wild(Mew),goh,oak])
    if "Shamouti Island" in f.location:        
        pl=random.choice([wild(GMoltres),wild(GArticuno),wild(GZapdos)])
    if "Sea Spirit's Den" in f.location:        
        pl=random.choice([wild(Zapdos),wild(Moltres),wild(Articuno)])
    if "Violet City" in f.location:
        pl=falkner
    if "Cave of Origin" in f.location:        
        pl=random.choice([wallace,steven,wild(Kyogre),wild(Groudon)])
    if "Underground Ruins" in f.location:        
        pl=random.choice([wild(Regigigas)])
    if "Olivine City" in f.location:
        pl=jasmine 
    if "Indigo Plateau" in f.location:
        pl=random.choice([lorelei,bruno,agatha,lance,will,karen,koga,blue])
        blue.name=colored("Kanto Champion Blue","blue")
        ch=random.randint(1,3)
        if ch==3:
            lance.name=colored("Johto Champion Lance","red")
        if ch==2:
            lance.name=colored ("Kanto Champion Lance","red")
            
    if "Goldenrod City" in f.location:
        pl=random.choice([whitney,genTrainer(trclass=random.choice(["Rocket Grunt","Paleontologist"]))])
        
    if "New Bark Town" in f.location:
        pl=random.choice([ethan,silver])
        
    if "Mount Silver" in f.location:
        pl=random.choice([ethan,red,wild(Moltres)])

    if "Cinnabar Island" in f.location:
        pl=random.choice([blaine,genTrainer(random.choice(["Kindler","Juggler","Lass","Fire Breather","Ace Trainer"]))])

    if "Sky Pillar" in f.location:
        pl=random.choice([wild(Rayquaza),zinnia,steven,wallace,brendan,may])
        
    if "Fuchsia City" in f.location:    
        pl=random.choice([koga,janine,genTrainer(random.choice(["Psychic","Juggler","Lass","Black Belt","Ace Trainer"]))])
        koga.name="Gym Leader Koga"
        
    if "Celadon City" in f.location:
        pl=random.choice([erika,genTrainer(trclass=random.choice(["Rocket Grunt","Businessman"]))])
        
    if "Vermilion City" in f.location:
        pl=random.choice([surge,genTrainer(trclass=random.choice(["Rocker","Businessman","Guitarist","Sailor","Electrician"]))])
        
    if "Saffron City" in f.location:
        pl=random.choice([sabrina,genTrainer(random.choice(["Psychic","Juggler"]))])
        
    if "Pallet Town" in f.location:
        pl=random.choice([gary,ash])
        
    if "Viridian Forest" in f.location:
        pl=genTrainer(random.choice(["Bug Catcher","Bug Researcher"]))
        
    if "Viridian City" in f.location:
        pl=random.choice([giovanni,blue,genTrainer(trclass=random.choice(["Psychic","Lass","Ace Trainer"]))])
        blue.name="Gym Leader Blue"
        giovanni.name="Gym Leader Giovanni"
        
    if "Pewter City" in f.location:
        pl=random.choice([brock,genTrainer(trclass=random.choice(["Bird Keeper","Lass","Hiker"]))])
        
    if "Cerulean Cave" in f.location:
        pl=random.choice([giovanni,red,wild(Mewtwo),genTrainer(trclass=random.choice(["Ace Trainer","Challenger"]))])
        
    if "Cerulean City" in f.location:
        pl=random.choice([misty,blue,genTrainer(trclass=random.choice(["Swimmer","Marine Biologist","Rocket Grunt","Bird Keeper","Lass","Black Belt","Ace Trainer","Psychic","Coach Trainer"]))])
        field.weather="Cloudy"
    if "Tournament" in f.location:
        pl=random.choice([random.choice(gymlist),random.choice(e4list),random.choice(champlist),random.choice(fronlist),random.choice(evilist),random.choice(talentlist),genTrainer(trclass="Competitive Player")])   
    if "Battle Frontier, Hoenn" in f.location:    
        pl=random.choices([random.choice([brandon,noland,lucy,greta,anabel,tucker,spenser]),genTrainer(trclass="Pokémon Trainer")],weights=[1,5],k=1)[0]
        
    if "Battle Frontier, Sinnoh" in f.location:    
        pl=random.choices([random.choice([palmer,Thorton,dahlia,argenta,darach]),genTrainer(trclass="Pokémon Trainer")],weights=[1,5],k=1)[0]
    if pl is None:
        pl=red
    return pl