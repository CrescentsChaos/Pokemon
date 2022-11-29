class Move:
    "Move Source"
    def __init__(self,name,base,movetype,cat,pp):
        self.name=name
        self.base=base
        self.movetype=movetype
        self.cat=cat
        self.pp=pp
class FireBlast(Move):
    def __init__(self,name="Fire Blast",base=110, movetype="Fire",cat="Special",pp=5):
        super().__init__(name,base,movetype,cat,pp)
        
