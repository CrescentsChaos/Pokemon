#pylint:disable=C0304
#pylint:disable=R0915
#pylint:disable=R0912
#pylint:disable=C0116
#pylint:disable=C0103
#pylint:disable=C0301
#import sys
#import time
#def print(something):
#    for character in something:
#        sys.stdout.write(character)
#        sys.stdout.flush()
#        time.sleep(0.01)
import random
def intro (tr,sr,field):
    mons=[]
    mmons=[]
    for k in sr.pokemons:
        mmons.append(k.name)
    for i in tr.pokemons:
        mons.append(i.name)
    srname=sr.name.split(" ")[-1]
    if "Roark" in tr.name:
        if "Canalave City" in field.location:
            print(f" {tr.name}: You came to challenge dad? But guess what! you gotta challenge me first!")
    if "Buck" in tr.name:
        if "Heatran" in mmons:
            print(f" {tr.name}: Ohhhh! Is that a Heatran? So you did catch Heatran! That's cool! But You aren't even close to my collection!\n")
        else:
            print(f" {tr.name}: One, there are no shortcuts in the way of Pokémon! Two... Nevermind that, let's do this!\n")
    if "Falkner" in tr.name:
        if "Lugia" in mons:
            print(f" {tr.name}: Oh! Lugia? Haha... Don't worry he's just a friend of mine..\n")
        else:
            print(f" {tr.name}: I'm Falkner, the Violet Pokémon Gym leader! People say you can clip flying-type Pokémon's wings with a jolt of electricity... I won't allow such insults to bird Pokémon! I'll show you the real power of the magnificent bird Pokémon!\n")
    if "Trevor" in tr.name:
        print(f" {tr.name}: I think I will follow the crowd and be your opponent as well. But this time it won't be about the Pokédex. It will be a Pokémon battle!\n")
    if "Ingo" in tr.name:
        print(f" {tr.name}: What a selfish outlook.These frenzies cause the Pokémon themselves such suffering! But what is it you want to do, {srname}? ")
    if "Anabel" in tr.name:
        print(f" {tr.name}: Greetings... My name is Anabel. I am the Salon Maiden, and I am in charge of running the Battle Tower... I have heard several rumors about you... In all honesty, what I have heard does not seem attractive in any way... The reason I've come to see you... Well, there is but one reason... Let me see your talent in its entirety...\n")
    if "Ghetsis" in tr.name:
        print(f" {tr.name}: My name is Ghetsis. I am representing Team Plasma. I, too, was summoned from another world, much like the other leaders you've defeated!\n")
    if "Dahlia" in tr.name:
        print(f" {tr.name}: Whenever I battle someone tough, I smile. I cannot help it! How about you? What do you do? Do you laugh? Cry? Get angry?\n")
    if "Ethan" in tr.name:
        print(f" {tr.name}: I knew it was you, {srname}! How did you get past me? Here is your punishment for surprising me, {srname}!")
    if "Blue" in tr.name:
        if field.location=="Indigo Plateau":
            print(f" {tr.name}: Hey, {srname}! I was looking forward to seeing you, {srname}! Hahah, that is so great! My rival should be strong to keep me sharp. While working on my Pokédex, I looked all over for Pokémon. Not only that, I assembled teams that would beat any Pokémon type. And now… I am the Pokémon League Champion! {srname}! Do you know what that means? I'll tell you. I am the most powerful Trainer in the world!\n")
    if "Surge" in tr.name:
        print(f" {tr.name}: The name's Lt. Surge! When it comes to Electric-type Pokémon, I'm number one! You've got guts to challenge me! I'm gonna zap you!\n")
    if "Misty" in tr.name:
        print(f" {tr.name}: I'm Misty! I'm a user of Water-type Pokémon, and my Water-type Pokémon are tough!\n")
    if "Silver" in tr.name:
        print(f" {tr.name}: Hold it. You're going to take the Pokémon League challenge now? That's not going to happen. My super-well trained Pokémon are going to pound you. {srname}! I challenge you!\n")
    if "Leon" in tr.name:
        print(f" {tr.name}: A real hero, who battled alongside the Legendary Pokémon, Zacian and Zamazenta... I couldn't have dreamed of a better challenger to help increase my winning streak!\n")
    if "Trainer N" in tr.name:
        print(f" {tr.name}: Well, {srname}, is it? Let me hear your Pokémon's voice again!\n")
    if "Tabitha" in tr.name:
        print(f" {tr.name}: Hehehe... Got here already, did you? We underestimated you! But this is it! I'm a cut above the Grunts you've seen so far. I'm not stalling for time. I'm going to pulverize you!\n")
    if "Brendan" in tr.name:
        print(f" {tr.name}: Hey, {srname}. So this is where you were. How's it going? Have you been raising your Pokémon? I'll check for you.Oh! By checking I meant battling you get it?\n")
    if "Ariana" in tr.name:
        print(f" {tr.name}: I don't know or care if what I'm doing is right or wrong... I just put my faith in Giovanni and do as I am told.\n")
    if "Archer" in tr.name:
        print(f" {tr.name}: That's quite enough of you playing the hero, kid. Spreading lies about how Team Rocket has disbanded… It's such an obvious attempt to cause confusion in our ranks. Fortunately, we're not so ignorant to fall for the lies of a child! And now, I'll show you how scary an angry adult can be!\n")
    if "Cyrus" in tr.name:
        x=random.choice([(f" {tr.name}: ...The shadowy Pokémon isn't here. It abandoned me here, then disappeared somewhere farther down... Was it content to merely interfere with my plan...? Incidentally, do you understand the concept of genes?\n"),(f" {tr.name}: ...My name is Cyrus. I would like to ask you one question. Is this world the new world?\n"),(f" {tr.name}: I can sense in you the strong desire to protect... something. You have a powerful spirit. ...That must mean this isn't the world I desired. I used the power of the Pokémon that control time and space to create a perfect world, where the human spirit does not exist. That was when a great shadow appeared and engulfed me... And brought me to this world.\n"),(f" {tr.name}: So we meet again, {srname}. It seems our fates have become intertwined. But here and now, I will finally break that bond!")])
        print(x)
    if "Archie" in tr.name:
        x=random.choice([(f" {tr.name}: I find myself thinkin'… maybe I should make this world more like my ideal while I'm here anyway! I've got the Sea Basin Pokémon, Kyogre… With its power to control the rains, I'll call down a great deluge to wash away this world's land! All life is born from the sea! If we help the ocean to expand, we're creating the cradle for future life to grow and thrive!\n"),(f" {tr.name}: The ancient power of Primal Kyogre!\n"),(f" {tr.name}: The super-ancient Pokémon…KYOGRE!!!\n")])
        print(x)
    if "Maxie" in tr.name:
        x=random.choice([(f" {tr.name}: Groudon... Nothing could awaken you from your sleep bathed in magma... This Red Orb is what you sought. Wasn't it? I have brought you the Red Orb. Let its shine awaken you! And show me... Show me the full extent of your power!\n"),(f" {tr.name}: So the super-ancient Pokémon weren't only Groudon and Kyogre... After all our frantic scheming and fruitless efforts, that one Pokémon's simple action puts everything right again as if nothing had happened... Fu... Fuhahaha.../n")])
        print(x)
    if "Giovanni" in tr.name:
        x=random.choice([(f" {tr.name}: ... I don't know why you have come here. Anyway, I have to warn you that this is not a place for kids like you.\n"),(f" {tr.name}: You have a certain look... It reminds me of the kid who stood in front of me three years ago... You have the same eyes... I'm on my way to Goldenrod City to answer the call and join my team. Are you going to get in my way?\n"),(f" {tr.name}: For your insolence, you will feel a world of pain!\n")])
        if "Viridian City" in field.location:
            print(f" {tr.name}: Fwahahaha! This is my hideout! I planned to resurrect Team Rocket here! But, you have caught me again! So be it! This time, I'm not holding back! Once more, you shall face Giovanni, the greatest trainer!\n")
        else:
            print(x)
    if "Kahili" in tr.name:
        print(f" {tr.name}: Alola! And alola once again! My name is Kahili. A few years ago, I was a champion of the island challenge, too. Just like you. I've been traveling the world to improve my skill as both a Trainer and as a golfer. When I heard that they'd made a Pokémon League in my own home region, I came flying back to serve Alola. Have a look at my fantastic Flying-type team!\n")
    if "Acerola" in tr.name:
        print(f" {tr.name}: Nanu said maybe he can't refuse a tapu choosing him to serve as kahuna... But he'd be darned if he had to serve as one of the Elite Four just because some guy asked him! So I guess I'll just have to battle hard enough to make up for his not being here!\n")
    if "Olivia" in tr.name:
        print(f" {tr.name}: I won't be holding back! My Rock-type Pokémon will grind you to dust! Your puny little Pokémon are going to go down in one hit! Hah!\n")
    if "Molayne" in tr.name:
        print(f" {tr.name}: Kukui asked me to, so I decided to be in the Elite Four. I'm looking forward to battling against you and Sophocles in the Pokémon League.\n")
    if "Hala" in tr.name:
        print(f" {tr.name}: Your old kahuna is now also a member of the Elite Four. Well, this time I'm holding nothing back! Time for you to see what I can really do!\n")
    if "Caitlin" in tr.name:
        print(f" {tr.name}: Who are you? How impudent you are to disturb my sleep. Hmf... You appear to possess a combination of strength and kindness. Very well. Make your best effort not to bore me with a yawn-inducing battle. Clear?\n")
    if "Marshal" in tr.name:
        print(f" {tr.name}: Greetings, challenger. My name is Marshal. In order to master the art of fighting, I'm training under my mentor, Alder. My mentor sees your potential as a Trainer and is taking an interest in you. It is my intention to test you--to take you to the limits of your strength. Kiai!\n")
    if "Grimsley" in tr.name:
        print(f" {tr.name}: Man oh man... What is going on today? Challengers coming one right after another. Well, no matter. I am Grimsley of the Elite Four, and I will fulfill my duty to be your opponent.\n")
    if "Shauntal" in tr.name:
        x=random.choice([(f" {tr.name}: Eyes brimming with dark flame, this man rejected everything other than himself in order to bring about one singular justice...' That's part of a novel I'm writing. I was inspired by the challenger who was just here, and somehow I got a little sad... Excuse me. You're a challenger, right? I'm the Elite Four's Ghost-type Pokémon user, Shauntal, and I shall be your opponent.\n"),(f"'{tr.name}: Do you know Thunderbolt?' was his first greeting to me. It wasn't until after we battled that I learned his name was Volkner.' That's part of a novel I wrote. I absolutely love writing about the close bonds between the Trainers who come here and the Pokémon they train. Could I use you and your Pokémon as a subject?\n")])
        print(x)
    if "Karen" in tr.name:
        print(f" {tr.name}: I am Karen of the Elite Four. You're {srname}? How amusing. I love dark-type Pokémon. I find their wild, tough image to be so appealing. And they're so strong. Think you can take them? Just try to entertain me. Let's go.\n")
    if "Drake" in tr.name:
        print(f" {tr.name}: I am the last of the Pokémon League Elite Four, Drake the Dragon master! In their natural state, Pokémon are wild living things. They are free. At times, they hinder us. At times, they help us. For us to battle with Pokémon as partners, do you know what it takes? Do you know what is needed? If you don't, then you will never prevail over me!\n")
    if "Glacia" in tr.name:
        print(f" {tr.name}: Welcome, my name is Glacia of the Elite Four. I've traveled from afar to Hoenn so that I may hone my icy skills. But all I have seen are challenges by weak Trainers and their Pokémon. What about you? It would please me to no end if I could go all out against you!\n")
    if "Sidney" in tr.name:
        print(f" {tr.name}: Welcome, challenger! I'm Sidney of the Elite Four. I like that look you're giving me. I guess you'll give me a good match. That's good! Looking real good! All right! You and me, let's enjoy a battle that can only be staged here in the Pokémon League!\n")
    if "Phoebe" in tr.name:
        print(f" {tr.name}: Ahahaha! I'm Phoebe of the Elite Four. I did my training on Mt. Pyre. While I trained, I gained the ability to commune with Ghost-type Pokémon. Yes, the bond I developed with Pokémon is extremely tight. So, come on, just try and see if you can even inflict damage on my Pokémon!\n")
    if "Malva" in tr.name:
        print(f" {tr.name}: You're the illustrious {srname}, are you? Welcome at last to the Pokémon League. I am one of the Elite Four. People know me as the Fire-type-Pokémon user, Malva. Here in the Pokémon League, you'll encounter the four of us--the Elite Four--and our Champion. If you hope to meet the Champion and challenge her here, you must first defeat the four of us. Do your best, because if you can't impress us with your real strength, you'll never get to battle her. But it should be a walk in the park for you, right? The hero/heroin who destroyed big, bad Team Flare.\n")
    if "Drasna" in tr.name:
        print(f" {tr.name}: Oh goodness, hello to you! Welcome, welcome, come in. You must be a strong Trainer. Yes, quite strong indeed... That's just wonderful news! Facing opponents like you and your team will make my Pokémon grow like weeds!\n")
    if "Wikstrom" in tr.name:
        print(f" {tr.name}: Well met, young challenger! Verily am I the Elite Four's famed blade of hardened Steel, Wikstrom! With my magnificent Pokémon at my side, I will reveal the scope of Trainer achievement! Let us both give our word that our contest shall be fair and honorable. Ready? En garde!\n")
    if "Lucian" in tr.name:
        print(f" {tr.name}: Ah, you timed your arrival well. I've just finished reading a book, you see. Allow me to introduce myself. I am Lucian. I am a user of the Psychic type. I must say, you've already proven yourself to be outstanding by coming this far. They say I am the toughest of the Elite Four. I'm afraid I will have to go all out against you to live up to that reputation.\n")
    if "Bertha" in tr.name:
        print(f" {tr.name}: Well, well. You're quite the adorable Trainer, but you've also got a spine. Ahaha! I'm Bertha. I have a preference for Ground-type Pokémon. Well, would you show this old lady how much you've learned?\n")
    if "Aaron" in tr.name:
        print(f" {tr.name}: Hello! Welcome to the Pokémon League! I'm Aaron of the Elite Four. It's good to meet you. Oh, I should explain, I'm a huge fan of bug Pokémon. Bug Pokémon are nasty-mean, and yet they're beautiful, too... Would you like to know why I take on challengers here, in this room? It's because I want to become perfect, just like my bug Pokémon! Ok! Let me take you on!\n")
    if "Flint" in tr.name:
        print(f" {tr.name}: This situation just cooks! The drama and tension sizzles! Flint, the fiery master of fire Pokémon, is going to put you to the test! Let Flint see how hot your spirit burns!\n")
    if "Siebold" in tr.name:
        print(f" {tr.name}: ... ... ... Yes, I see it now. This is a path with no end. To seek to be the absolute best is an absurd goal. Yet, as long as I am alive, I shall strive onward to seek the ultimate cuisine... and the strongest opponents in battle!\n")
    if "Red" in tr.name:
        print(f" {tr.name}: ........\n")
    if "Cynthia" in tr.name:
        print(f" {tr.name}: One look at you tells me many things about you. Together, you and your Pokémon overcame all the challenges you faced, however difficult. It means that you've triumphed over any personal weaknesses, too. The power you learned... I can feel it emanating from you. That's enough talking. Let's get on with why you're here. I, Cynthia, accept your challenge as the Pokémon League Champion! There won't be any letup from me!\n")
    if "Tobias" in tr.name:
        print(f" {tr.name}: I'm the Lily of the Valley Conference Champion. You probably heard of my Famous Darkrai and Latios. {srname}! But now I will show you my true strength. The strength of Legendary Pokémons.\n")
    if "Wallace" in tr.name:
        print(f" {tr.name}: You have overcome challenges and made it this far because you worked as one with your Pokémon. Show me that strength here and now!\n")
    if "Steven" in tr.name:
        print(f" {tr.name}: Welcome, {srname}. I was looking forward to seeing you here one day. You… What did you see on your journey with Pokémon? What did you feel, meeting so many other Trainers like you? What has awoken in you? I want you to hit me with it all! Now, bring it!\n")
    if "Agatha" in tr.name:
        print(f" {tr.name}: I am Agatha of the Elite Four! Oak's taken a lot of interest in you, child! That old duff was once tough and handsome! That was decades ago! Now he just wants to fiddle with his Pokédex! He's wrong! Pokémon are for fighting! {srname}! I'll show you how a real trainer fights!\n")
    if "Lorelei" in tr.name:
        print(f" {tr.name}: Well then, allow me to reintroduce myself. I am Lorelei of the Elite Four. No one can best me when it comes to icy Pokémon. Freezing moves are powerful. Your Pokémon will be at my mercy when they are frozen solid. That's because frozen Pokémon can't do a thing in battle! Hahaha! Are you ready?\n")
        
    if "Bruno" in tr.name:
        print(f" {tr.name}: I am Bruno of the Elite Four! Through rigorous training, people and Pokémon can become stronger without limit. I've lived and trained with my fighting Pokémon! And that will never change! {srname}! We will grind you down with our superior power! Hoo hah!\n")
    if "Lance" in tr.name:
        print(f" {tr.name}: I've been waiting for you. {srname}! I knew that you, with your skills, would eventually reach me here. There's no need for words now. We will battle to determine who is the stronger of the two of us. As the most powerful trainer and as the Pokémon League Champion… I, Lance the dragon master, accept your challenge!\n")                