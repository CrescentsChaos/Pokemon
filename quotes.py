import random
#RETURN QUOTES
def pkreturn(tr,self):
    if "Red" in tr.name:
        print(f"\n 🔁 {tr.name}: ........")
    elif "Archie" in tr.name and "Primal Kyogre" in self.name and self.hp<=0:
        print(random.choice([f"\n 🔁 {tr.name}: What?! I didn't do anything. Why did the Blue Orb... Where did Kyogre go?"]))
    elif "Giovanni" in tr.name and "Mewtwo" in self.name and self.hp<=0:
        print(random.choice([f"\n 🔁 {tr.name}: WHAT! This cannot be!",f"\n 🔁 {tr.name}: Huh. Most people cower in fear when they come face-to-face with Mewtwo... Maybe I underestimated you.",f"\n 🔁 {tr.name}: It appears the amount of energy we drew out was too much to handle, even for a Pokémon as powerful as Mewtwo."]))
    else:
        phase1=random.choice([" return! You did well buddy."," return! You disappointed me."," return! Pathetic Pokémon."," return! Take rest my friend."," return! You were strong as always."," return! Maybe next time."])
        print(f"\n 🔁 {tr.name}: "+self.name+phase1)
#SPECIAL QUOTES
def spquote(tr,self):
    prevname=self.name
    phase2=random.choice(["It's our show time.","Show your strength.","Let's do it buddy.","I believe in you!","Let's finish this off.","Are you ready buddy?","Let's show them what you are capable of.","You know what to do."])
    if "Red" in tr.name:
        pass
    elif "Giovanni" in tr.name and "Mewtwo" in self.name:
        print(random.choice([" Now you'll see what Mewtwo is all about!"," Mewtwo... I'm going to need you to sow some chaos for me."," You were lured here... By me and Mewtwo."," You were lured here... By me and Mewtwo.",]))
    else:
        print(f" Go {prevname}! "+phase2)