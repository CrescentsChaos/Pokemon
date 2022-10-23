#pylint:disable=R0913
#pylint:disable=W0401
#pylint:disable=W0102
from typematchup import *
class Trainer:
	def __init__(self,name="Billy",pokemons=[],region="Kanto",hazard=None,ai=True):
		self.name=name
		self.ai=ai
		self.pokemons=pokemons
		self.region=region
		if hazard is None:
		    self.hazard=[]
		else:
		    self.hazard=hazard


