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
    if "Wake" in sr.name:
        print(random.choice([f" {sr.name}: Hunwah! It's gone and ended! How will I say this... I want more! I wanted to battle a lot more!\n"]))
    if "Wake" in tr.name:
        print(random.choice([f" {tr.name}: I won, but I want more! I wanted to battle a lot more!\n"]))
    if "Bugsy" in tr.name:
        print(random.choice([f" {tr.name}: Thanks! Thanks to our battle, I was also able to make progress in my research!\n"]))
    if "Blaine" in tr.name:
        print(random.choice([f" {tr.name}: Whoa hey! I'll power up my Pokémon with the heat from this victorious battle!\n"]))
    if "Koga" in tr.name:
        print(random.choice([f" {tr.name}: You expect to battle the Elite Four with your current skills?\n",f" {sr.name}: Have you learned to fear the techniques of the ninja?\n"]))
    if "Sabrina" in sr.name:
        print(random.choice([f" {sr.name}: Your power... It far exceeds what I foresaw... Maybe it isn't possible to fully predict what the future holds...\n",f" {sr.name}: This loss shocks me!\n But a loss is a loss.\n"]))
    if "Sabrina" in tr.name:
        print(random.choice([f" {tr.name}: This victory... It's exactly as I foresaw three years ago!\n"]))
    if "Erika" in tr.name:
        print(random.choice([f" {tr.name}: I feel inspired by my win. Fighting alongside your beloved Pokémon and winning. This is the joy of being a Pokémon Trainer.\n"]))
    if "Surge" in sr.name:
        print(random.choice([f" {sr.name}: Even my electric tricks lost. You're excellent! Keep goin' like lightning!\n"]))
    if "Surge" in tr.name:
        print(random.choice([f" {tr.name}: Oh yeah! When it comes to Electric-type Pokémon, I'm number one in the world!\n"]))
    if "Misty" in sr.name:
        print(random.choice([f" {sr.name}: Know what? My dream was to go on a journey and battle powerful Trainers... I made my dream come true, and now... my next dream is to defeat you!\n"]))
    if "Misty" in tr.name:
        print(random.choice([f" {tr.name}: Know what? My dream was to go on a journey and battle powerful Trainers... Now, that dream has come true!\n"]))
    if "Brock" in tr.name:
        print(random.choice([f" {tr.name}: I really enjoyed the battle with you. I guess my rock-hard defense works in top-level competition as well!\n"]))
    elif "Brock" in sr.name:
        print(random.choice([f" {sr.name}: I really enjoyed the battle with you. Still, the world is huge! I can't believe you got past my rock-hard defense.\n",f" {sr.name}: I knew you were strong, but this...\n",f" {sr.name}: Awesome... That was a really great battle. I compliment you on your victory!\n"]))
    if "Lucy" in tr.name:
        print(random.choice([f" {tr.name}: Humph...\n"]))
    elif "Lucy" in sr.name:
        print(random.choice([f" {sr.name}: ... ... ... ... ... ... Show me your Frontier Pass...\n",f" {sr.name}: Urk...\n",f" {sr.name}: ...That's all there is... Disappear already...\n"]))
    if "Shauntal" in sr.name:
        print(random.choice([f" {sr.name}: Wow. I'm dumbstruck! I know a lot of words, but right now I can't figure out how to say this. Perhaps, if the feeling I'm having now is put into words, it will be trapped there. So let me say this... My feeling is you're a great Trainer!\n",f" {sr.name}: S-sorry! First, I must apologize to my Pokémon... I'm really sorry you had a bad experience because of me! Oh! It's not your fault! This is how battles always are. Even in light of that, I'm still one of the Elite Four!\n",f" {sr.name}: Challenger, if you defeat the entire Elite Four of the Pokémon League, you can go on to challenge the Champion. And you have earned that right. Return to the plaza in the center and check the statue.\n"]))
    if "Blaine" in sr.name:
        print(random.choice([f" {sr.name}: I have burned down to nothing!\n Not even ashes remain!\n",f" {sr.name}: Awesome. I have burned out... But the fire inside me is only going to get stronger! Let's battle again sometime!\n"]))
    if "ner May" in sr.name:
        print(random.choice([f" {sr.name}: Woah, that was great!\n You lived up to the hype!\n"]))
    if "Jasmine" in sr.name:
        print(random.choice([f" {sr.name}: Well done...\n"]))
    if "Misty" in sr.name:
        print(random.choice([f" {sr.name}: Wow!\n You are too much!\n",f" {sr.name}: Ayaya!"]))
    if "Tonoy" in tr.name:
        print(f" {tr.name}: Thanks for playing the game! 😶‍🌫️\n")
    if "Iris" in tr.name:
        print(random.choice([f" {tr.name}: Do you ever feel that way too, {srname}?\n",f" {tr.name}: {mon.name} is amazing , right? I've trained him well..\n"]))
    if "Brendan" in sr.name:
        print(random.choice([f" {sr.name}: Drat, wasted yet again...\n",f" {sr.name}: Oof, I'm missing something...\n",f" {sr.name}: Not sure what I was expecting...\n",f" {sr.name}: Heh... not bad...\n"]))
    if "Lorelei" in sr.name:
        print(random.choice([f" {sr.name}: ... Things shouldn't be this way!\n"]))
    if "Bruno" in sr.name:
        print(random.choice([f" {sr.name}: Why? How could I lose?\n"]))
    if "Agatha" in sr.name:
        print(random.choice([f" {sr.name}: Oh, my!\n You are something special, child!\n"]))
    if "Lance" in sr.name:
        print(random.choice([f" {sr.name}: That's it!\n"]))
    if "Erika" in sr.name:
        print(random.choice([f" {sr.name}: Oh! I concede defeat... You are remarkably strong.... That was a delightful match. I felt inspired.\n"]))
    if "Chuck" in sr.name:
        print(random.choice([f" {sr.name}: Wha! I lost?!\n Incredible!\n"]))
    if "Bugsy" in sr.name:
        print(random.choice([f" {sr.name}: Gah...Now I'm not just single, I'm a frickin loser too!\n",f" {sr.name}: Whoa, amazing! You're an expert on Pokémon! My research isn't complete yet.\n"]))
    if "Koga" in sr.name:
        print(random.choice([f" {sr.name}: Humph!\n You have proven your worth!",f" {sr.name}: I subjected you to everything I could muster. But my efforts failed. I must hone my skills. Go on to the next room, and put your abilities to the test!\n"]))
    if "Falkner" in sr.name:
        print(random.choice([f" {sr.name}: Mmm... I have much to learn even before attaining the Mega Stones...\n"]))
    if "Pryce" in sr.name:
        print(random.choice([f" {sr.name}: Impressive... It appears you've overcame many obstacles as well.\n"]))
    if "Clair" in sr.name:
        print(random.choice([f" {sr.name}: Oh, I see...\n Your skills are rather mysterious.\n"]))
    if "Archer" in sr.name:
        print(random.choice([f" {sr.name}: What a shameful blunder!\n",f" {sr.name}: Again?! This is infuriating!\n",f" {sr.name}: That's how it be...\n"]))
    if "Ariana" in sr.name:
        print(random.choice([f" {sr.name}: Heh... I'm actually impressed.\n"]))
    if "Giovanni" in tr.name:
        print(random.choice([f" {tr.name}: Ha! That was a truly intense fight!\n",f" {tr.name}: I hope we meet again...\n"]))
    if "Blue" in sr.name:
        print(random.choice([f" {sr.name}: Hey! Take it easy!\n",f" {sr.name}: Aww!\n You just lucked out!\n",f" {sr.name}: No! That can't be!\n",f" {sr.name}: What!?\n"]))
    if "Surge" in sr.name:
        print(random.choice([f" {sr.name}: Now that's a shocker!\n",f" {sr.name}: Truly shocking!\n"]))
    if "Morty" in sr.name:
        print(random.choice([f" {sr.name}: I'm still not good enough yet...\n"]))
    if "Grunt" in sr.name:
        print(random.choice([f" {sr.name}: Dang!\n",f" {sr.name}: Ayaya!\n",f" {sr.name}: Stop! I give up!\n I'll leave quietly!\n",f" {sr.name}: Arrgh!\n You are good!\n",f" {sr.name}: Crushed by a kid, as usual.\n",f" {sr.name}: Must be nice being strong.\n",f" {sr.name}: Please! No more!\n",f" {sr.name}: I give up!\n"]))
    if "Giovanni" in sr.name:
        print(random.choice([f" {sr.name}: What? Me, lose?!\n",f" {sr.name}: Haarg! I lose?! There is nothing I wish to say to you!\n",f" {sr.name}: How this is possible...? The past three years have been a waste...? How can a kid like you manage to destroy my dream once again? The precious dream of Team Rocket has become little more than an illusion...\n",f" {sr.name}: ...I see you have raised your Pokémon with utmost care. It would be foolish to fight such a kid with all my might. Ha, very well.\n",f" {sr.name}: What!\n This can't be!\n",f" {sr.name}: W-what?! Impossible...\n"]))
    if "Noland" in sr.name:
        print(f" {sr.name}: Heh... You're a pretty bright spark... Next time, I'll come after you hard. No holds barred, understand? You keep up your studies!\n")
    if "Noland" in tr.name:
        print(f" {tr.name}: Way to work! That was a good lesson, eh?\n")
    if "Red" in tr.name:
        print(f" {tr.name}: .........\n")
    if "Red" in sr.name:
        print(f" {sr.name}: .........\n")
    elif "Eternatus" in mon.name:
        print(f" {sr.name}: {mon.name}! *sigh* You had to use that thing fr?😢\n")
    if tr.ai==True and sr.ai==False:
        print(random.choice([f" {tr.name}:\n Imagine losing to an AI. Bruh...Wtf are you doing with your life?🤣\n",f" {tr.name}:\n Humans this humans that...You are more worthless than something that does not exist!😒\n"]))
    else:
        pass
        #if mon.use!=None:
#            print(f" {tr.name}:\n Did you feel my pain in that {mon.use} from {mon.name}!\n")
#        else:
#            print(random.choice([f" {tr.name}:\n Me and {mon.name} trained a lot! Thanks for that!\n",f" {tr.name}:\n You are a fool if you thought you could beat me and {mon.name}...fwhahahhahahaha!\n"]))
    print("===================================================================================")