class Field:
    def __init__(self,name="Stadium",weather=None,trickroom=False, terrain=None, gravity=False,magicroom=False,mudsport=False,watersport=False,wonderroom=False,rainturn=0,rainendturn=5):
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
    def rain(self,mon,tr):
        if mon.item=="Damp Rock":
            self.rainendturn=self.rainturn+8
        else:
            self.rainendturn=self.rainturn+5
        
