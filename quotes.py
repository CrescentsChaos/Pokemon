import random
from colorama import init
from termcolor import colored    
import climage
def attackquote(self,tr,used):
    if "Blue" in tr.name and "Blastoise" in self.name and used=="Hydro Pump":
        print(random.choice([f" {tr.name}: Blastoise, now use Hydro Pump!"]))
    if "Lance" in tr.name and "Dragonite" in self.name:
        print(random.choice([f" {tr.name}: Dragonite, do your worst!",f" {tr.name}: Dragonite, attack!"]))
    if "Geeta" in tr.name and used=="Tera Blast":
        print(random.choice([f" {tr.name}: Being strong is a given for a Champion. You must also learn to give the audience a show!",f" {tr.name}: This is how you're supposed to unleash a move. This is what it takes to be at the top."]))
    if "Ryme" in tr.name and used=="Hex":
        print(random.choice([f" {tr.name}: Put your SOUL into it, Toxtricity! Let's bring the power!",f" {tr.name}: You think I'm down and out? I'm about to turn your world upside-down!"]))
    if "Ash" in tr.name and used=="10,000,000 Volt Thunderbolt":
        print(random.choice([f" {tr.name}: Pikachu! Are you ready,buddy!!"]))
        print(colored(" Pikachu","yellow")+" : Pikaa Pika!")
    if "Katy" in tr.name and used=="Lunge":
        print(random.choice([f" {tr.name}: I'll smash you like a cake with this decorative move! What do you think of this dessert?!",f" {tr.name}: Feast your eyes on my shining bug decoration! Though this one is not so sweet!"]))
    if "Iono" in tr.name and used=="Thunderbolt":
        print(random.choice([f" {tr.name}: Zap! Rock, paper, pew pew pew! Come on out if yer weak to Electric stuff!",f" {tr.name}: Danger—high voltage! Sorry if it’s TOO shocking, ’eyyy!"]))
    if "Brassius" in tr.name and used=="Trailblaze":
        print(random.choice([f" {tr.name}: At times, art becomes a race against the clock! Let us increase the pace!",f" {tr.name}: My dear grass… grow, I say! Heed my wishes and grow!"]))
    if "Kofu" in tr.name and used=="Crabhammer":
        print(random.choice([f" {tr.name}: Better get a big breath o' air, 'cause yer about to get hit by a surgin' wave!",f" {tr.name}: One ol’ man Kofu special, comin’ right up! Hang on tight or get swept away by the Surging Chef!"]))
    else:
        print(f" 👤 {tr.name}: ")
def teratalk(tr,self):
    if "Geeta" in tr.name and "Glimmora" in self.name:
        print(random.choice([f" {tr.name}: Be the light that guides all Trainers, Glimmora.",f" {tr.name}: May you shine as brightly as the future of Paldea, Glimmora!"]))
    if "Ryme" in tr.name and "Toxtricity" in self.name:
        print(random.choice([f" {tr.name}: This ghostly change'll turn your highs to lows! The brightest lights cast the darkest shadows!",f" {tr.name}: Kick back, relax, and enjoy this last track. Turn it up for a grave-rattlin' good time!\n When I'm on the mic, even the dead rise up! DJ G-Rave over there's sure feelin' it!"]))
    if "Katy" in tr.name and "Ursaring" in self.name:
        print(random.choice([f" {tr.name}: Now, my Pokémon! Time to break free from your cocoon and come into your own!",f" {tr.name}: My sweet little bear! Show me your new form as if you were a bug emerging from its cocoon!"]))
    if "Iono" in tr.name and "Mismagius" in self.name:
        print(random.choice([f" {tr.name}: Come fooorth, shiny li’l lightbulb! I’m not done yet! Iono power, goooooo!",f" {tr.name}: Come fooorth, shiny li'l lightbulb! Be the invention that leads me to victory! Bzzzzzzt!"]))
    if "Kofu" in tr.name and "Crabominable" in self.name:
        print(random.choice([f" {tr.name}: Prepare the rigging for a big transformation!\n My Pokémon’s gon’ rock the boat!",f" {tr.name}: A Crabominable Terastallizing!\n Think outside the crab trap, I say!"]))
    if "Brassius" in tr.name and "Sudowoodo" in self.name:
        print(f" {tr.name}: Allow me to touch this work up slightly!\n I will call it... “Truleewoodo”!")
#RETURN QUOTES
def pkreturn(tr,self):
#    print("===================================================================================")
    print("⬅️"*40)
    if "Red" in tr.name:
        print(f" 🔁 {tr.name}: ........")
    elif "Wild" in tr.name:
        print(f" ‼️ {self.name} disappeared!")
    elif "Paul" in tr.name:
        print(f" 🔁 {tr.name}: {self.name} not too shabby!")
    elif "Ash" in tr.name:
        print(f" 🔁 {tr.name}: {self.name}, You were amazing!")
    elif "Archie" in tr.name and "Primal Kyogre" in self.name and self.hp<=0:
        print(random.choice([f" 🔁 {tr.name}: What?! I didn't do anything. Why did the Blue Orb... Where did Kyogre go?"]))
    elif "Giovanni" in tr.name and "Mewtwo" in self.name and self.hp<=0:
        print(random.choice([f" 🔁 {tr.name}: WHAT! This cannot be!",f" 🔁 {tr.name}: Huh. Most people cower in fear when they come face-to-face with Mewtwo... Maybe I underestimated you.",f" 🔁 {tr.name}: It appears the amount of energy we drew out was too much to handle, even for a Pokémon as powerful as Mewtwo."]))
    else:
        phase1=random.choice([" return! You did well buddy."," return! You disappointed me."," return! Pathetic Pokémon."," return! Take rest my friend."," return! You were strong as always."," return! Maybe next time."])
        print(f" 🔁 {tr.name}: "+self.name+phase1)
#SPECIAL QUOTES
def spquote(tr,self):
    prevname=self.name
    phase2=random.choice(["It's our show time.","Show your strength.","Let's do it buddy.","I believe in you!","Let's finish this off.","Are you ready buddy?","Let's show them what you are capable of.","You know what to do."])
    if "Red" in tr.name:
        pass
    elif "Aaron" in tr.name and len(tr.pokemons)==1:
        print(f" {prevname} , not yet! We'll keep struggling till the very end!")
    elif "Cynthia" in tr.name and len(tr.pokemons)==1:
        print(f" {prevname} , we won't let this end yet! I can't remember the last time I was put in a corner like this!")
    elif "Geeta" in tr.name and len(tr.pokemons)==1:
        print(f" {prevname} goo, Heh! Hahahahahaha!\n Don't think you've won just yet!")
    elif "Blue" in tr.name and ("Blastoise" in self.name or "Venusaur" in self.name or "Charizard" in self.name):
        print(f" {prevname}, Go! This one is really strong. Don't get scared.")        
    elif "Ash" in tr.name:
        print(f" {prevname}, I choose you!")
    elif "Paul" in tr.name:
        print(f" {prevname} standby for battle!")
    elif "Giovanni" in tr.name and "Mewtwo" in self.name:
        print(random.choice([" Now you'll see what Mewtwo is all about!"," Mewtwo... I'm going to need you to sow some chaos for me."," You were lured here... By me and Mewtwo."," You were lured here... By me and Mewtwo.",]))
    elif "Wild" in tr.name:
        print(f" ‼️ wild {self.name} appeared!")
    else:
        print(f" Go {prevname}! "+phase2)
    if "unknown" not in self.sprite:    
        print(climage.convert(self.sprite,width=50,is_unicode=True))        
    print("➡️"*40)        