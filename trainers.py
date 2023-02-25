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
	def __init__(self,name="Billy",pokemons=[],region="Kanto",hazard=None,ai=True,lightscreen=False,reflect=False,auroraveil=False,faintedmon=[],tailwind=False,wishhp=False,vcdmg=False,vcturn=False,vcendturn=False,canmega=True,canmax=True):
		self.name=name
		self.ai=ai
		self.pokemons=pokemons
		self.canmax=canmax
		self.faintedmon=faintedmon
		self.lightscreen=lightscreen
		self.reflect=reflect		
		self.canmega=canmega
		self.tailwind=tailwind
		self.auroraveil=auroraveil
		self.region=region
		self.reflecturn=0
		self.wishhp=wishhp
		self.tailturn=0
		self.auroraturn=0
		self.lsturn=0
		self.vcdmg=vcdmg
		self.vcturn=vcturn
		self.vcendturn=vcendturn
		self.screenend=self.lsturn+5
		self.twendturn=self.tailturn+4
		self.rfendturn=self.reflecturn+5
		self.avendturn=self.auroraturn+5
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
	       
	def auroraend(self,mon,mon2):
	       if "Light Clay" not in (mon.item,mon2.item):
	           self.avendturn=self.auroraturn+5
	       if "Light Clay" in (mon.item,mon2.item):
	           self.avendturn=self.auroraturn+8
	       return self.avendturn
	def twend(self,mon,mon2):
	    self.twendturn=self.tailturn+4
	    return self.twendturn              
