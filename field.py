#pylint:disable=C0303
#pylint:disable=R0913
#pylint:disable=C0116
#pylint:disable=C0301
class Field:
    def __init__(self,name="Stadium",weather=None,trickroom=False, terrain=None, gravity=False,magicroom=False,mudsport=False,watersport=False,wonderroom=False,rainturn=0,rainendturn=5,sunturn=0,sunendturn=5,sandturn=0, sandendturn=5,hailturn=0,hailendturn=5):
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
    def hailend(self,mon):
	       if mon.item!="Icy Rock":
	           self.hailendturn=self.hailturn+5
	       if mon.item=="Icy Rock":
	           self.hailendturn=self.hailturn+8
	       return self.hailendturn
    def rainend(self,mon):
	       if mon.item!="Damp Rock":
	           self.rainendturn=self.rainturn+5
	       if mon.item=="Damp Rock":
	           self.rainendturn=self.rainturn+8
	       return self.rainendturn
    def sunend(self,mon):
	       if mon.item!="Heat Rock":
	           self.sunendturn=self.sunturn+5
	       if mon.item=="Heat Rock":
	           self.sunendturn=self.sunturn+8
	       return self.sunendturn	     
    def sandend(self,mon):
	       if mon.item!="Smooth Rock":
	           self.sandendturn=self.sandturn+5
	       if mon.item=="Smooth Rock":
	           self.sandendturn=self.sandturn+8
	       return self.sandendturn	 
	               
