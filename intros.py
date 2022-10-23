#pylint:disable=C0103
#pylint:disable=C0301
#import sys
#import time
#def print(something):
#    for character in something:
#        sys.stdout.write(character)
#        sys.stdout.flush()
#        time.sleep(0.01)
def intro (tr,sr):
    srname=sr.name.split(" ")[-1]
    if "Malva" in tr.name:
        print(f"{tr.name}: You're the illustrious {srname}, are you? Welcome at last to the Pokémon League. I am one of the Elite Four. People know me as the Fire-type-Pokémon user, Malva. Here in the Pokémon League, you'll encounter the four of us--the Elite Four--and our Champion. If you hope to meet the Champion and challenge her here, you must first defeat the four of us. Do your best, because if you can't impress us with your real strength, you'll never get to battle her. But it should be a walk in the park for you, right? The hero/heroin who destroyed big, bad Team Flare.")
    if "Drasna" in tr.name:
        print(f"{tr.name}: Oh goodness, hello to you! Welcome, welcome, come in. You must be a strong Trainer. Yes, quite strong indeed... That's just wonderful news! Facing opponents like you and your team will make my Pokémon grow like weeds!")
    if "Wikstrom" in tr.name:
        print(f"{tr.name}: Well met, young challenger! Verily am I the Elite Four's famed blade of hardened Steel, Wikstrom! With my magnificent Pokémon at my side, I will reveal the scope of Trainer achievement! Let us both give our word that our contest shall be fair and honorable. Ready? En garde!")
    if "Lucian" in tr.name:
        print(f"{tr.name}: Ah, you timed your arrival well. I've just finished reading a book, you see. Allow me to introduce myself. I am Lucian. I am a user of the Psychic type. I must say, you've already proven yourself to be outstanding by coming this far. They say I am the toughest of the Elite Four. I'm afraid I will have to go all out against you to live up to that reputation.")
    if "Bertha" in tr.name:
        print(f"{tr.name}: Well, well. You're quite the adorable Trainer, but you've also got a spine. Ahaha! I'm Bertha. I have a preference for Ground-type Pokémon. Well, would you show this old lady how much you've learned?")
    if "Aaron" in tr.name:
        print(f"{tr.name}: Hello! Welcome to the Pokémon League! I'm Aaron of the Elite Four. It's good to meet you. Oh, I should explain, I'm a huge fan of bug Pokémon. Bug Pokémon are nasty-mean, and yet they're beautiful, too... Would you like to know why I take on challengers here, in this room? It's because I want to become perfect, just like my bug Pokémon! Ok! Let me take you on!")
    if "Flint" in tr.name:
        print(f"{tr.name}: This situation just cooks! The drama and tension sizzles! Flint, the fiery master of fire Pokémon, is going to put you to the test! Let Flint see how hot your spirit burns!")
    if "Siebold" in tr.name:
        print(f"{tr.name}: ... ... ... Yes, I see it now. This is a path with no end. To seek to be the absolute best is an absurd goal. Yet, as long as I am alive, I shall strive onward to seek the ultimate cuisine... and the strongest opponents in battle!")
    if "Red" in tr.name:
        print(f"{tr.name}: ........")
    if "Cynthia" in tr.name:
        print(f"{tr.name}: One look at you tells me many things about you. Together, you and your Pokémon overcame all the challenges you faced, however difficult. It means that you've triumphed over any personal weaknesses, too. The power you learned... I can feel it emanating from you. That's enough talking. Let's get on with why you're here. I, Cynthia, accept your challenge as the Pokémon League Champion! There won't be any letup from me!")
    if "Tobias" in tr.name:
        print(f"{tr.name}: I'm the Lily of the Valley Conference Champion. You probably heard of my Famous Darkrai and Latios. {srname}! But now I will show you my true strength. The strength of Legendary Pokémons.")
    if "Wallace" in tr.name:
        print(f"{tr.name}: You have overcome challenges and made it this far because you worked as one with your Pokémon. Show me that strength here and now!")
    if "Steven" in tr.name:
        print(f"{tr.name}: Welcome, {srname}. I was looking forward to seeing you here one day. You… What did you see on your journey with Pokémon? What did you feel, meeting so many other Trainers like you? What has awoken in you? I want you to hit me with it all! Now, bring it!")
    if "Agatha" in tr.name:
        print(f"{tr.name}: I am Agatha of the Elite Four.My poison type Pokémon traumatizes him as well.{srname}! I'll show you how a real Trainer battles!")
    if "Lorelei" in tr.name:
        print(f"{tr.name}: Well then, allow me to reintroduce myself. I am Lorelei of the Elite Four. No one can best me when it comes to icy Pokémon. Freezing moves are powerful. Your Pokémon will be at my mercy when they are frozen solid. That's because frozen Pokémon can't do a thing in battle! Hahaha! Are you ready?")
        
    if "Bruno" in tr.name:
        print(f"{tr.name}: I am Bruno of the Elite Four! Through rigorous training, people and Pokémon can become stronger without limit. I've lived and trained with my fighting Pokémon! And that will never change! {srname}! We will grind you down with our superior power! Hoo hah!")
    if "Lance" in tr.name:
        print(f"{tr.name}: I've been waiting for you. {srname}! I knew that you, with your skills, would eventually reach me here. There's no need for words now. We will battle to determine who is the stronger of the two of us. As the most powerful trainer and as the Pokémon League Champion… I, Lance the dragon master, accept your challenge!")        
    print("")        