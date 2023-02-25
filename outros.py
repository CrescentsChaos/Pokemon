import random
def outro(tr,sr,mon,field):
    mons=[]
    mmons=[]
    for k in sr.pokemons:
        mmons.append(k.name)
    for i in tr.pokemons:
        mons.append(i.name)
    srname=sr.name.split(" ")[-1]
    print("===================================================================================")
    if "Iris" in tr.name:
        print(random.choice([f" {tr.name}: Do you ever feel that way too, {srname}?\n",f" {tr.name}: {mon.name} is amazing , right? I've trained him well..\n"]))
    if "Giovanni" in tr.name:
        print(random.choice([f" {tr.name}: Ha! That was a truly intense fight!\n",f" {tr.name}: I hope we meet again...\n"]))
    if "Giovanni" in sr.name:
        print(random.choice([f" {sr.name}: What? Me, lose?!\n",f" {sr.name}: Haarg! I lose?! There is nothing I wish to say to you!\n",f" {sr.name}: How this is possible...? The past three years have been a waste...? How can a kid like you manage to destroy my dream once again? The precious dream of Team Rocket has become little more than an illusion...\n",f" {sr.name}: ...I see you have raised your Pokémon with utmost care. It would be foolish to fight such a kid with all my might. Ha, very well.\n"]))
    if "Noland" in sr.name:
        print(f" {sr.name}: Heh... You're a pretty bright spark... Next time, I'll come after you hard. No holds barred, understand? You keep up your studies!\n")
    if "Noland" in tr.name:
        print(f" {tr.name}: Way to work! That was a good lesson, eh?\n")
    if "Red" in tr.name:
        print(f" {tr.name}: .........\n")
    if "Red" in sr.name:
        print(f" {sr.name}: .........\n")
    print("===================================================================================")