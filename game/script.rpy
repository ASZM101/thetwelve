define one = Character("Athena")
define two = Character("Artemis")
define three = Character("Parvati")
define four = Character("Guanyin")
define five = Character("Ma'at")
define six = Character("Danu")
define seven = Character("Saraswati")
define eight = Character("Kannon")
define nine = Character("Amaterasu")
define ten = Character("Seshat")
define eleven = Character("Minerva")
define twelve = Character("Bellona")

label start:
    scene bg greece0
    show athena welcome at truecenter
    one "Yo, you're dead."
    one "However, if you complete 12 labors from some goddesses, you can become a demi-god."
    one "You wanna be immortal? Now's your chance."
    menu:
        one "You wanna be immortal? Now's your chance."
        "Attempt the 12 labors":
            one "Good luck!"
            jump athena1
        "Not even gonna try":
            one "Well, I guess it's farewell forever."
            return

# 1. Athena (greek god of battle strategy): If you are military sergeant, and your country is bombed → Bomb them, plead for a peace treaty, ask for allies
label athena1:
    one "Before we get started, I'll introduce myself first. I'm Athena, the Greek goddesss of battle strategy."
    one "For your first labor, I'm gonna test your strategic thinking in battle."
    one "Imagine you're the commanding officer of a military troop. Your country was just bombed by an enemy nation. What are you gonna do??"
    menu:
        one "Imagine you're the commanding officer of a military troop. Your country was just bombed by an enemy nation. What are you gonna do??"
        "Bomb the enemy, obviously":
            one "Violent... I like it!"
        "Negotiate a peace treaty":
            one "Boring... but honorable"
        "Ask allies for advice":
            one "You can't even think for yourself? That doesn't sound much like a commanding officer."

# 2. Artemis (greek goddess of the wilderness): guess the animal based on only part of its body
label artemis2:
    hide athena
    show artemis welcome at truecenter
    two "Welcome to the second labor. I'm Artemis, the Greek goddess of the wilderness."
    two "For this labor, I will test your knowledge of wildlife."

# 3. Parvati (Hindu goddess of beauty): [optical illusions](https://www.illusionsindex.org/i/all-is-vanity)
label parvati3:
    hide artemis
    show parvati welcome at truecenter
    three "Welcome to the third labor. I'm Parvati, the Hind goddess of beauty."

# 4. Guanyin (chinese buddhist goddess of mercy): If you’re on a sinking ship, and there’s one life jacket → use it, throw it away, give it to a kid
label guanyin4:
    four "Welcome to the fourth labor. I'm Guanyin, Chinese Buddhist goddess of mercy."
    four "Based on your answer, we will see the true measures of your heart"
    four "Here is the situation: if you are on a sinking ship with only one life jacket,would you keep it for yourself or give it to the little boy?"
    menu:
        "Nahh, thats for my personal use ONLY. NO Touching!":
            four "Based on your decision, I cannot permit someone with a cruel heart to become one of us"
            return
        "Yes, I will help that little boy with a whole future ahead of him":
            four "You have shown dignity and carelessness in your choice. You may proceed forward"
            jump maat5

# 5. Ma'at (Egyptian goddess symbolizing justice): Mini game, you’re the judge of conflict arguments 
label maat5:
    five "Welcome to the fifth labor. I am Ma'at, the Egyptian goddess of truth, justice, and order."
    five "In order to succeed in life you need to settle disputes and maintain order."
    menu:
        five "Are you ready to be the seeker of justice?"
        "Yes":
            five "Excellent"
            jump maatJudge

        "I don't think so...":
            five "ok then parish"
            return

    label maatJudge:
        five "2 roommates are having a dispute."
        five "Roommate A feels like they are the only ones doing the dishes. Roommate B says that the dishes are not a big deal since they are busy with homework."
        menu:
            five "Who is in the right?"
            "Roommate A":
                five "Correct. Plus 10 aura points."
            "Roommate B":
                five "Incorrect. Person A is in the right."
                five "Negative 30000 aura points. You will now die."
                return
        
        five "Person A and Person B are walking on the street. Person B accidentally bumps Person A."
        five "Person A had a bad day. They just lost their job, their wife and their kids so they punch Person B for bumping into them."
        five "This leads to Person B tackling A to the ground because a stranger just punched them for assumingly no reason which leads to a big fight."
        five "Who is in the right?"
        menu:
            five "Who is in the right?"
            "Person A":
                five "Inccorect. Person B is in the right."
            "Person B":
                five "Correct"
        five 'There is rarely a clear right and wrong answer. Whether you are in the "right" or in the "wrong" is... subjective.'
        five "There are always 2 sides of the story."
        five "And it is your job to listen to both sides in order to get the full truth."
        five "You may now go to the next goddess on your journey."



# 6. Danu (irish goddess of nature): guess the plant
label danu6:
    six "Welcome to the sixth labor. I'm Danu, the irish goddess of nature."
    six "I love plants! Which one is your favorite?"
    menu:
        "Uh. Flowers?":
            six "Which kind?"
            menu:
                "um. the colorful kind?":
                    six "I don't like you *Smites you*"
                    return
                "Chrysanthemum!":
                    six "Nice! Me Too!"
                "Lavender!":
                    six "Cool!"
        "I Love Trees!":
            six "Which kind?"
            menu:
                "Oak":
                    six "NICE"
                "Willow":
                    six "Me Too!"
                "Coconut":
                    six "Interesting"
    six "Let's see if you're a true plant lover!"

    label guessPlant:
        #pictures and guess it 




# 7. Saraswati (Hindu goddess, embodying arts): name the painting
label saraswati7:
    seven "Welcome to the seventh labor. I am Saraswati."
    seven "I am the Hindu goddess of art and knowledge. To test both, you have to name the paintings."
    menu:
        "I'm ready!":
            jump guessPainting
        "I'm not ready!!!":
            seven "Ok then parish *Smites you* 67 67 67 "
            return

label guessPainting:
    seven 'Who made the painting called "Girl With A Pearl Earring"?'
    menu:
        seven 'Who made the painting called "Girl With A Pearl Earring"?'

        "Leonardo da Vinci":
            seven "Bruh, no"
        "Claude Monet of course!":
            seven "You were so confident yet you were so wrong."
        "Johannes Vermeer?":
            seven "Yes!"
    
    seven " Next question. Edward Hopper made what famous painting?"
    menu:
        seven " Next question. Edward Hopper made what famous painting?"

        "Nighthawks":
            seven "Correct!"
        "The Ninth Wave":
            seven "Ew no."
            seven "You gotta die now"
            return
        "The scream":
            seven "Nice try but no."
    
    seven "Last question..."
    seven "What is my favorite painting?"
    menu:
        seven "What is my favorite painting?"

        "IDK":
            seven "Well. The correct answer is all of them!"
        "Trick question. It's all of them":
            seven "Correct!"
        '“The Last Supper” by Francis Newton Souza':
            seven "That is a great painting but actually its all of them"

    seven "Beauty is everywhere in this world."
    seven "If you can realize that everyone and everything is capable of life and beauty, the world around you will be a brighter place."
    seven "Remember that as you go to your next quest."



# 8. Kannon (Japanese buddhist  goddess of  compassion): If you get a million dollars → keep it, burn it, give it to charity
label kannon8:
    eight "Welcome to the eighth labor. I am Kannon, the Japanese buddhist goddess of compassion and mercy."
    eight "Do you have compassion in your heart? Do you have love for others?"
    menu:
        "Yes":
            eight "We shall see."
        "Yes?":
            eight "You are  unsure of yourself. Nevertheless, we shall see."
        "No":
            eight "We shall see..."

    eight "you encounter a homeless person on the street. They look hungry and cold."
    eight "luckily, you have a million dollars. What will you do? Be honest."

    menu:
        eight "luckily, you have a million dollars. What will you do? Be honest."
        "Give them $20":
            eight "Interesting"
        "Give them $100":
            eight "Interesting"
        "Give them  $125,000 (1/8 of your money)":
            eight "Interesting"
        "Give them All of your money":
            eight "YOU LIE"
            eight "But I shall show you mercy."
    
    eight "Your best friend is moving into a new apartment. Do you help them move out of their old apartment?"
    menu:
        eight "Do you help them move out? And remember, be honest."
        "Of course, they are my friend. Even if I'm busy, I will always help them.":
            eight "Ok"
        "Sure, Im not doing anything right now.":
            eight "Ok"
        "No, sorry I'm really busy, and I have no time.":
            eight "Ok"
        "NO. I really don't want to.":
            eight "Ok"

    eight "Lasty, did you drink water today?"
    menu:
        eight "Lasty, did you drink water today?"
        "Yes":
            eight "Good"
        "No":
            jump kindness
        "What does this have to do with anything?":
            jump kindness

label kindness:
    eight "You should not only have compassion with others. You should have some for yourself as well."
    eight "Let this guide your decisons as you venture further."





# 9. Amaterasu (japanese Goddess of the Sun): Trivia about the Sun
label amaterasu9:       
    $ score = 0
    nine "lets see how much you know about the Sun. If you know enough, I might let you move on"
    nine "first question, how old is the Sun?"
    menu: 
        "6-7 billion years":
           "Incorrect. Lets try another" 
        "4.5 billion years":
            "CORRECT. Keep going!"
            $ score +=1
    nine "next question, how long does it take the sun to rotate on its axis?"
    menu:
        "27 days": 
            nine"Correct, one more!"
            $ score +=1
        "18 days":
            nine"Incorrect, Try one more time"
    nine "last question, do you love Mr.Sun?"
    menu:
        "Yes":
           nine"Thank you for not putting no. You don't know how many people put that answer"
           $ score +=1 
        "No":
           nine "You humans are ungrateful. Moving on . . ."
    if score>1:
        nine "congratulations! You are able to pass to the next level!"
    else:
        "You have failed the test and will suffer a horrible fate. Sorry"

# 10. Seshat (egyptian goddess of writing): Vocabulary (SAT level)
label seshat10:
    $ score=0
    ten "What someone knows affects their decisions. Prove your knowledge in this test and show your worth"
    ten "Your first question shall be . . . what is the definition of CAMADERIE?"
    menu:
        "social and friendly":
            ten "Correct!!!Keep going"
            $ score +=1
        "formal and neutral":
            ten "No, do better"
    ten "Next question! What does ACCOLADE mean?"
    menu:
        "Harsh and mean":
            ten"Incorrect; I am NOT accolade when I say that this is why your grades are so low"
        "Praise and attention":
            ten "Correct! Last one!"
            $ score +=1
    ten "The Big question . . . What does IDK mean?!"
    menu:
        "I Don't Know":
            ten "Actually, I Don't Kare! HA . . Just kidding, I'll give it to you"
            $ score +=1
        "I Don't Kare":
            ten "We need to talk about your spelling"
    if score>1:
        ten "Yes! You have made it passed my vocabulary quiz and may go forward on your journey"
    else:
        ten "Whomp Whomp. You're dead. Bye"

# 11. Minerva (roman goddess of strategy): Chess board, choose best move
label minerva11:
    eleven "Welcome to the eleventh labor. I'm Minerva, the Roman goddess of strategy."
    eleven "For this second-to-last labor, I will test strategic thinking."
    eleven "How should white escape the check?"
    menu:
        eleven "How should white escape the check?"
        "King to H1":
            eleven "Black wins a queen. Tough luck!"
        "Pawn to F4":
            eleven "White is still in check. Gotta escape first!"
        "Queen to G5":
            eleven "Excellent! White captures the checking piece and wins a queen!"
    eleven "What we do in life must be based on strategy."

# 12. Bellona (oman goddess of war): Fight a monster using choices (stab, upper cut, punch, headlock)
label bellona12:
    $ score= 500
    twelve "Nice work young soldier. You have passed on the tests. All but one"
    twelve "You will now face your last opponent. The mighty manticore!"
    twelve "Here, the amount of aura that you have gained shall help or hinder the Manticore's defeat"
    twelve "Good luck young soldier, and remember . . ."
    twelve "I will ALWAYS have more aura than you"
    menu:
        "stab":
            $ score -=40
        "headlock":
            $ score -=40
        "upper_cut":
            $ score -=20
        "punch":
            $ score -=15
    python:
        while score > 0:
            renpy.say(twelve, "Keep fighting")
        renpy.say(twelve, "The mighty Manticore has been defeated!")
        renpy.say(twelve, "You really are worthy of becoming a demigod")



    
    return