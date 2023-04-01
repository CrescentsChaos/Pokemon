#pylint:disable=R0916
#pylint:disable=R0902
#pylint:disable=C0116
#pylint:disable=C0114
#pylint:disable=R0914
#pylint:disable=C0303
#pylint:disable=R0913
#pylint:disable=C0116
#pylint:disable=C0301
import random
kanto=["Pallet Town","Viridian City","Viridian Forest","Pewter City","Mt. Moon","Cerulean Cave","Cerulean City","Rock Tunnel","Lavender Town","Saffron City","Celadon City","Cycling Road","Fuchsia City","Seafoam Islands","Cinnabar Island","Indigo Plateau","Vermilion City","Mount Silver","Victory Road","Diglett's Cave","Pokémon Mansion","Pokémon Tower","Power Plant","Silph Co."]
johto=["New Bark Town","Goldenrod City","Violet City","Olivine City","Azalea City","Ecruteak City","Cianwood City","Mahogany Town","Blackthorn City","Whirl Islands","Navel Rock","Bell Tower"]
hoenn=["Littleroot Town","Petalburg City","Rustboro City","Dewford Town","Mauville City","Lavaridge Town","Fortree City","Mosdeep City","Sootopolis City","Evergrande City","Aqua Hideout","Magma Hideout","Terra Cave","Marine Cave","Mt. Pyre","Mt. Chimney","Faraway Island","Birth Island","Mirage Island","Southern Island","Crescent Isle","Cave of Origin","Fabled Cave","Gnarled Den","Granite Cave","Jagged Pass","Lilycove City","Meteor Falls","Nameless Cavern","New Mauvile","Pacifidlog Town","Pathless Plain","Scorched Slab","Sea Mauvile","Seafloor Cavern","Shoal Cave","Sky Pillar","Slateport City","Soaring in the Sky","Trackless Forest","Rock Peak Ruins","Iceberg Ruins","Iron Ruins",f"Route {random.randint(101,134)}"]
sinnoh=["Twinleaf Town","Oreburgh City","Eterna City","Hearthome City","Veilstone City","Pastoria City","Canalave City","Iron Island","Snowpoint City","Sunnyshore City","Mountain Stark","Spear Pillar","Mount Coronet","Aquity Lakefront","Celestic Town","Eterna Forest","Floaroma Town","Flower Paradise","Fuego Ironworks","Grand Underground","Great Marsh","Lake Acuity","Lake Valor","Lake Verity","Lost Tower","Maniac Tunnel","Newmoon Island","Old Chateau","Oreburgh Mine","Ramanas Park","Ravaged Path","Resort Area","Ruin Maniac Cave","Sendoff Spring","Snowpoint Temple","Solaceon Ruins","Stark Mountain","Trophy Garden","Turnback Cave","Valley Windworks","Valor Lakefront","Wayward Cave",f"Route {random.randint(201,230)}"]
unova=["Abundant Shrine","Castelia City","Celestial Tower","Challenger's Cave","Chargestone Cave","Cold Storage","Desert Resort","Dragonspiral Tower","Dreamyard","Driftveil City","Driftveil Drawbridge","Giant Chasm","Icirrus City","Lostlorn Forest","Marvelous Forest","Mistralon Cave","Moon of Icirrus","N's Castle","Nacrene City","P2 Laboratory","Pinwheel Forest","Relic Castle","Striaton City","Twist Mountain","Undella Bay","Undella Town","Village Bridge","Wellspring Cave","Black City","White Forest","Accumula Town","Aspertia City","Castelia Sewers","Clay Tunnel","Floccesy Ranch","Floccesy Town","Humilau City","Nature Santuary","Nimbasa City","Relic Passage","Reversal Mountain","Seaside Cave","Strange House","Underground Ruins","Virbank City","Virbank Complex","Trial Chamber","Marvelous Bridge"]
kalos=["Ambrette Town","Aquacorde Town","Azure Bay","Connecting Cave","Couriway Town","Cyllage City","Frost Cavern","Glittering Cave","Laverre City","Lost Hotel","Lumiose City","Parfum Palace","Pokémon Village","Reflection Cave","Santalune Forest","Sea Spirit's Den","Shalour City","Team Flare Secret HQ","Terminus Cave","Tower of Mastery","Coumarine City","Anistar City","Snowbelle City","Crown Tundra","Isle of Armor"]
alola=["Aether Paradise","Akala Outskirts","Altar of the Moone","Altar of the Sunne","Ancient Poni Path","Berry Fields","Blush Mountain","Brooklet Hill","Diglett's Tunnel","Exeggutor Island","Haina Desert","Hano Beach","Ha'oli Cemetery","Hau'oli City","Iki Town","Kala'e Bay","Konikoni City","Lake of the Moone","Lake of the Sunne","Lush Jungle","Malie City","Malie Garden","Melemele Meadow","Melemele Sea","Memorial Hill","Mount Hokulani","Paniola Ranch","Paniola Town","Poke' Pelago","Poni Breaker Coast","Poni Coast","Poni Gauntlet","Poni Grove","Poni Meadow","Poni Plains","Poni Wilds","Resolution Cave","Ruins of Abundance","Ruins of Conflict","Ruins of Hope","Ruins of Life","Seafolk Village","Seaward Cave","Secluded Shore","Tapu Village","Ten Carat Hill","Thrifty Megamart","Ula'ula Meadow","Vast Poni Canyon","Verdant Cavern","Wela Volcano Park","Ultra Space Cave","Ultra Space Cliff","Ultra Space Crag","Ultra Space Waterfall",f"Ultra {random.choice(['Crater','Deep Sea','Desert','Forest','Jungle','Megalopolis','Plant','Ruin'])}"]
galar=["Axew's Eye","Ballimere Lake","Ballonlea","Brawler's Cave","Bridge Field","Challenge Beach","Challenge Road","Circhester","City of Motostoke","Courageous Cavern","Crown Shrine","Dappled Grove","Dusty Bowl","East Lake Axewell","Energy Plant","Fields of Honor","Fields of Focus","Freezington","Frigid Sea","Frostpoint Field","Galar Mine","Giant's Bed","Giant's Cap","Giant's Foot","Giant's Mirror","Giant's Seat","Glimwood Tangle","Hammerlocke","Hammerlocke Hills","Honeycalm Sea","Hulbury","Iceberg Ruins","Insular Sea","Iron Ruins","Lake of Outrage","Lakeside Cave","Loop Lagoon","Master Dojo","Max Lair","Meetup Spot","Motostoke","Motostoke Outskirts","Motostoke Riverbank","North Lake Miloch","Old Cemetery","Path of the Peak","Postwick","Potbottom Desert","Rock Peak Ruins","Rolling Fields","Slippery Slope","Slumbering Weald","Snowslide Slope","Soothing Wetlands","South Lake Miloch","Spikemuth","Split-Decision Ruins","Stepping-Stone Sea","Stony Wilderness","Stow-on-Side","Three-Point-Pass","Training Lowlands","Tunnel to the top","Turffield","Warm-Up Tunnel","Watchtower Ruins","West Lake Axewell","Workout Sea","Wyndon","Shamouti Island"]
paldea=["Caseeroya Lake","Area Zero","Cabo Poco","Los Platos","Mesagoza","Cortondo","Artazon","Levincia","Alfornada","Cascarrafa","Porto Marinada","Medali","Montenevera","Poco Path","Inlet Grotto","South Paldean Sea","East Paldean Sea","West Paldean Sea","North Paldean Sea","Alfornada Cavern","Asado Desert","Dalizapa Passage","Glaseado Mountain","Socarrat Trail","Tagtree Thicket","Casseroya Falls","Colonnade Hollow","Fury Falls","Glaseado's Grasp","Gracia Stones","Grand Olive Orchard","Leaking Tower","Million Volt Skyline","Secluded Beach","The Great Crater","West Province","North Province"]
special=["Pokémon World Tournament,Unova","Battle Frontier, Hoenn","Battle Frontier, Sinnoh"]
place=kanto+johto+hoenn+unova+sinnoh+kalos+alola+galar+paldea
class Field:
    def __init__(self,name="Stadium",weather="None",trickroom=False, terrain="None", gravity=False,magicroom=False,mudsport=False,watersport=False,wonderroom=False,rainturn=0,rainendturn=200,sunturn=0,sunendturn=200,sandturn=0, sandendturn=200,hailturn=0,hailendturn=200,grassturn=0,grassendturn=200,eleturn=0,eleendturn=200,troomturn=0,troomendturn=200,psyturn=0,psyendturn=200,misturn=0,misendturn=200,location="None",snowstormturn=0,snowstormendturn=200):
        self.name=name
        self.weather=weather
        self.trickroom=trickroom
        self.terrain=terrain
        self.gravity=gravity
        self.magicroom=magicroom
        self.mudsport=mudsport
        self.watersport=watersport
        self.wonderroom=wonderroom
        self.rainturn=rainturn
        self.rainendturn=rainendturn
        self.sunturn=sunturn
        self.sunendturn=sunendturn
        self.sandturn=sandturn
        self.sandendturn=sandendturn
        self.hailturn=hailturn
        self.hailendturn=hailendturn
        self.grassturn=grassturn
        self.grassendturn=grassendturn
        self.eleturn=eleturn
        self.eleendturn=eleendturn
        self.psyturn=psyturn
        self.psyendturn=psyendturn
        self.troomturn=troomturn
        self.troomendturn=troomendturn
        self.misturn=misturn
        self.snowstormturn=snowstormturn
        self.snowstormendturn=snowstormendturn
        self.location=location
        if self.location =="None":
            self.location=random.choices([random.choice(place),random.choice(special)],weights=[10,1],k=1)[0]
            if self.location in paldea:
                self.location+=", Paldea"
            elif self.location in galar:
                self.location+=", Galar"
            elif self.location in alola:
                self.location+=", Alola"
            elif self.location in kalos:
                self.location+=", Kalos"
            elif self.location in unova:
                self.location+=", Unova"
            elif self.location in hoenn:
                self.location+=", Hoenn"
            elif self.location in johto:
                self.location+=", Johto"
            elif self.location in kanto:
                self.location+=", Kanto"
            elif self.location in sinnoh:
                self.location+=", Sinnoh"
        self.misendturn=misendturn
    def troomend(self,mon,mon2):
	       if mon.item!="None" and "Room Service" not in (mon.item,mon2.item):
	           self.troomendturn=self.troomturn+5
	       if mon.item!="None" and "Room Service" in (mon.item,mon2.item):
	           self.troomendturn=self.troomturn+8
	       return self.troomendturn
    def psyend(self,mon,mon2):
	       if mon.item!="None" and "Terrain Extender" not in (mon.item,mon2.item):
	           self.psyendturn=self.psyturn+5
	       if mon.item!="None" and "Terrain Extender" in (mon.item,mon2.item):
	           self.psyendturn=self.psyturn+8
	       return self.psyendturn	       
    def eleend(self,mon,mon2):
	       if mon.item!="None" and "Terrain Extender" not in (mon.item,mon2.item):
	           self.eleendturn=self.eleturn+5
	       if mon.item!="None" and "Terrain Extender" in (mon.item,mon2.item):
	           self.eleendturn=self.eleturn+8
	       return self.eleendturn
    def hailend(self,mon,mon2):
	       if mon.item!="None" and "Icy Rock" not in (mon.item,mon2.item):
	           self.hailendturn=self.hailturn+5
	       if mon.item!="None" and "Icy Rock" in (mon.item,mon2.item):
	           self.hailendturn=self.hailturn+8
	       return self.hailendturn
    def rainend(self,mon,mon2):
	       if mon.item!="None" and "Damp Rock" not in (mon.item,mon2.item):
	           self.rainendturn=self.rainturn+5
	       if mon.item!="None" and "Damp Rock" in (mon.item,mon2.item):
	           self.rainendturn=self.rainturn+8
	       return self.rainendturn
    def snowstormend(self,mon,mon2):
	       if mon.item!="None" and "Icy Rock" not in (mon.item,mon2.item):
	           self.snowstormendturn=self.snowstormturn+5
	       if mon.item!="None" and "Icy Rock" in (mon.item,mon2.item):
	           self.snowstormendturn=self.snowstormturn+8	       
	       return self.snowstormendturn
    def sunend(self,mon,mon2):
	       if mon.item!="None" and "Heat Rock" not in (mon.item,mon2.item):
	           self.sunendturn=self.sunturn+5
	       if mon.item!="None" and "Heat Rock" in (mon.item,mon2.item):
	           self.sunendturn=self.sunturn+8
	       return self.sunendturn	     
    def sandend(self,mon,mon2):
	       if mon.item!="None" and "Smooth Rock" not in (mon.item,mon2.item):
	           self.sandendturn=self.sandturn+5
	       if mon.item!="None" and "Smooth Rock" in (mon.item,mon2.item):
	           self.sandendturn=self.sandturn+8
	       return self.sandendturn	 
    def grassend(self,mon,mon2):
	       if mon.item!="None" and "Terrain Extender" not in (mon.item,mon2.item):
	           self.grassendturn=self.grassturn+5
	       if mon.item!="None" and "Terrain Extender" in (mon.item,mon2.item):
	           self.grassendturn=self.grassturn+8
	       return self.grassendturn	               
    def misend(self,mon,mon2):
	       if mon.item!="None" and "Terrain Extender" not in (mon.item,mon2.item):
	           self.misendturn=self.misturn+5
	       if mon.item!="None" and "Terrain Extender" in (mon.item,mon2.item):
	           self.misendturn=self.misturn+8
	       return self.misendturn