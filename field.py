#pylint:disable=C0115
#pylint:disable=C0114
#pylint:disable=R0914
#pylint:disable=C0303
#pylint:disable=R0913
#pylint:disable=C0116
#pylint:disable=C0301
import random
place=["Pallet Town","Viridian City","Viridian Forest","Pewter City","Mount Moon","Cerulean Cave","Cerulean City","Rock Tunnel","Lavender Town","Saffron City","Celadon City","Cycling Road","Fuchsia City","Safari Zone, Kanto","Seafoam Island","Cinnabar Island","Indigo Plateau","Vermilion City","Mount Silver","New Bark Town","Goldenrod City","Violet City","Olivine City","Victory Road","Azalea City","Ecruteak City","Cianwood City","Mahogany Town","Blackthorn City","Littleroot Town","Petalburg City","Rustboro City","Dewford Town","Mauville City","Lavaridge Town","Fortree City","Mosdeep City","Sootopolis City","Evergrande City","Victory Road, Hoenn","Pokémon League, Sinnoh","Twinleaf Town","Oreburgh City","Eterna City","Hearthome City","Veilstone City","Pastoria City","Canalave City","Iron Island","Snowpoint City","Sunnyshore City"]
kanto=["Pallet Town","Viridian City","Viridian Forest","Pewter City","Mount Moon","Cerulean Cave","Cerulean City","Rock Tunnel","Lavender Town","Saffron City","Celadon City","Cycling Road","Fuchsia City","Seafoam Island","Cinnabar Island","Indigo Plateau","Vermilion City","Mount Silver","Victory Road"]
johto=["New Bark Town","Goldenrod City","Violet City","Olivine City","Azalea City","Ecruteak City","Cianwood City","Mahogany Town","Blackthorn City"]
hoenn=["Littleroot Town","Petalburg City","Rustboro City","Dewford Town","Mauville City","Lavaridge Town","Fortree City","Mosdeep City","Sootopolis City","Evergrande City"]
sinnoh=["Twinleaf Town","Oreburgh City","Eterna City","Hearthome City","Veilstone City","Pastoria City","Canalave City","Iron Island","Snowpoint City","Sunnyshore City"]
class Field:
    def __init__(self,name="Stadium",weather=None,trickroom=False, terrain=None, gravity=False,magicroom=False,mudsport=False,watersport=False,wonderroom=False,rainturn=0,rainendturn=200,sunturn=0,sunendturn=200,sandturn=0, sandendturn=200,hailturn=0,hailendturn=200,grassturn=0,grassendturn=200,eleturn=0,eleendturn=200,troomturn=0,troomendturn=200,psyturn=0,psyendturn=200,misturn=0,misendturn=200,location=None,snowstormturn=0,snowstormendturn=200):
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
        if self.location is None:
            self.location=random.choice(place)
            if self.location in hoenn:
                self.location+=", Hoenn"
            if self.location in johto:
                self.location+=", Johto"
            if self.location in kanto:
                self.location+=", Kanto"
            if self.location in sinnoh:
                self.location+=", Sinnoh"
        self.misendturn=misendturn
    def troomend(self,mon,mon2):
	       if"Room Service" not in (mon.item,mon2.item):
	           self.troomendturn=self.troomturn+6
	       if"Room Service" in (mon.item,mon2.item):
	           self.troomendturn=self.troomturn+9
	       return self.troomendturn
    def psyend(self,mon,mon2):
	       if"Terrain Extender" not in (mon.item,mon2.item):
	           self.psyendturn=self.psyturn+6
	       if"Terrain Extender" in (mon.item,mon2.item):
	           self.psyendturn=self.psyturn+9
	       return self.psyendturn	       
    def eleend(self,mon,mon2):
	       if"Terrain Extender" not in (mon.item,mon2.item):
	           self.eleendturn=self.eleturn+6
	       if"Terrain Extender" in (mon.item,mon2.item):
	           self.eleendturn=self.eleturn+9
	       return self.eleendturn
    def hailend(self,mon,mon2):
	       if"Icy Rock" not in (mon.item,mon2.item):
	           self.hailendturn=self.hailturn+6
	       if"Icy Rock" in (mon.item,mon2.item):
	           self.hailendturn=self.hailturn+9
	       return self.hailendturn
    def rainend(self,mon,mon2):
	       if"Damp Rock" not in (mon.item,mon2.item):
	           self.rainendturn=self.rainturn+6
	       if"Damp Rock" in (mon.item,mon2.item):
	           self.rainendturn=self.rainturn+9
	       return self.rainendturn
    def snowstormend(self,mon,mon2):
	       if"Snowy Rock" not in (mon.item,mon2.item):
	           self.snowstormendturn=self.snowstormturn+6
	       if"Snowy Rock" in (mon.item,mon2.item):
	           self.snowstormendturn=self.snowstormturn+9	       
	       return self.snowstormendturn
    def sunend(self,mon,mon2):
	       if"Heat Rock" not in (mon.item,mon2.item):
	           self.sunendturn=self.sunturn+6
	       if"Heat Rock" in (mon.item,mon2.item):
	           self.sunendturn=self.sunturn+9
	       return self.sunendturn	     
    def sandend(self,mon,mon2):
	       if"Smooth Rock" not in (mon.item,mon2.item):
	           self.sandendturn=self.sandturn+6
	       if"Smooth Rock" in (mon.item,mon2.item):
	           self.sandendturn=self.sandturn+9
	       return self.sandendturn	 
    def grassend(self,mon,mon2):
	       if"Terrain Extender" not in (mon.item,mon2.item):
	           self.grassendturn=self.grassturn+6
	       if"Terrain Extender" in (mon.item,mon2.item):
	           self.grassendturn=self.grassturn+9
	       return self.grassendturn	               
    def misend(self,mon,mon2):
	       if"Terrain Extender" not in (mon.item,mon2.item):
	           self.misendturn=self.misturn+6
	       if"Terrain Extender" in (mon.item,mon2.item):
	           self.misendturn=self.misturn+9
	       return self.misendturn