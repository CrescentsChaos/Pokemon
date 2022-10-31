#pylint:disable=R0902
#pylint:disable=C0303
#pylint:disable=C0116
#pylint:disable=W0201
#pylint:disable=W0613
#pylint:disable=C0103
#pylint:disable=C0115
#pylint:disable=C0301
#pylint:disable=R0913
#pylint:disable=W0401
#pylint:disable=W0102
from typematchup import *
class Trainer:
	def __init__(self,name="Billy",pokemons=[],region="Kanto",hazard=None,ai=True,lightscreen=False,reflect=False,faintedmon=[]):
		self.name=name
		self.ai=ai
		self.pokemons=pokemons
		self.faintedmon=faintedmon
		self.lightscreen=lightscreen
		self.reflect=reflect
		self.region=region
		self.reflecturn=0
		self.lsturn=0
		self.screenend=self.lsturn+5
		self.rfendturn=self.reflecturn+5
		if hazard is None:
		    self.hazard=[]
		else:
		    self.hazard=hazard
	def lightscreenend(self,mon,mon2):
	       if "Light Clay" not in (mon.item,mon2.item):
	           self.screenend=self.lsturn+5
	       if "Light Clay" in (mon.item,mon2.item):
	           self.screenend=self.lsturn+8
	       return self.screenend
	def reflectend(self,mon,mon2):
	       if "Light Clay" not in (mon.item,mon2.item):
	           self.rfendturn=self.reflecturn+5
	       if "Light Clay" in (mon.item,mon2.item):
	           self.rfendturn=self.reflecturn+8
	       return self.rfendturn        
