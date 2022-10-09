from typematchup import *
class Trainer:
	def __init__(self,name="Billy",pokemons=[],region="Kanto",hazard=None):
		self.name=name
		self.pokemons=pokemons
		self.region=region
		if hazard is None:
		    self.hazard=[]
		else:
		    self.hazard=hazard

def hazardcheck(self,pk):
    dmg=1
    if "Stealth Rock" in self.hazard:
        if pk.type1 in ["Flying", "Bug", "Fire", "Ice"]:
            dmg*=2
        if pk.type2!=None and pk.type2 in ["Flying", "Bug", "Fire", "Ice"]:
            dmg*=2
        if pk.type1 in ['Fighting', 'Ground', 'Steel']:
            dmg/=2
        if pk.type2!=None and pk.type2 in ['Fighting', 'Ground', 'Steel']:
            dmg/=2
        if dmg==0.25:
            pk.hp-=round((6.25/pk.maxhp)*100)
        if dmg==0.5:
            pk.hp-=round((12.5/pk.maxhp)*100)
        if dmg==1:
            pk.hp-=round((12.5/pk.maxhp)*100)
        if dmg==2:
            pk.hp-=round((25/pk.maxhp)*100)
        if dmg==4:
            pk.hp-=round((50/pk.maxhp)*100)
