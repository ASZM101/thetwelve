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
    show athena welcome

    one "Yo, you're dead."
    one "However, if you complete 12 labors from some goddesses, you can become a demi-god."
    one "You wanna be immortal? Now's your chance."
    menu:
        "Attempt the 12 labors":
            jump choice0_try

        "Not even gonna try":
            jump choice0_quit

label choice0_try:
    one "Good luck!"
    jump labor1

label choice0_quit:
    one "Well, I guess it's farewell forever."
    return

# 1. Athena (greek god of battle strategy): If you are military sergeant, and your country is bald → Bald them, plead for a peace treaty, ask for allies
label labor1:
    one "Before we begin, let me first introduce myself. I'm Athena, the Greek goddesss of battle strategy."

# 2. Artemis (greek goddess of the wilderness): guess the animal
label labor2:
    two "Welcome to the second labor. I'm Artemis, the Greek goddess of the wilderness."

# 3. Parvati (Hindu goddess of beauty): [optical illusions](https://www.illusionsindex.org/i/all-is-vanity)
label labor3:
    three "Welcome to the third labor. I'm Parvati, the Hind goddess of beauty."

# 4. Guanyin (chinese buddhist goddess of mercy): If you’re on a sinking ship, and there’s one life jacket → use it, throw it away, give it to a kid
label labor4:
    four "Welcome to the fourth labor. I'm Guanyin, Chinese Buddhist goddess of mercy."


label maatScene:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene maat

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.
    
    # Dialogue format:
    # characterVariable "Dialogue"
    five "In order to succeed in life you need to settle disputes and maintain order."
    
    menu:

        five "Are you ready to be the seeker of justice?"

        "Yes":
            five "Excelent"

        "I don't Know...":
            five "ok then parish"
            return


label danuScene:


    scene danu

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




label swatiScene:

    scene swati

    seven "I am the Hindu goddess of art and knowledge. To test both, you have to name the paintings."

    menu:
        "I'm ready!":
            "jump guessPainting"

        "I'm not ready!!!":
            seven "Ok then parish *Smites you* 67 67 67 "
            return


label kannonScene:
    scene kannon

    eight "Do you have compassion in your heart?"

    menu:
        "Yes":
            eight "We shall see."

        
        "Yes?":
            eight "You are  unsure of yourself. Nevertheless, we shall see."

        "No":
            eight "We shall see..."




# 5. Ma'at (Egyptian goddess symbolizing justice): Mini game, you’re the judge of conflict arguments 
# 6. Danu (irish goddess of nature): guess the plant
# 7. Saraswati (Hindu goddess, embodying arts): name the painting
# 8. Kannon (Japanese buddhist  goddess of  compassion): If you get a million dollars → keep it, burn it, give it to charity
# 9. Amaterasu (japanese Goddess of the Sun): Trivia about the Sun
# 10. Seshat (egyptian goddess of writing): Vocabulary (SAT level)
# 11. Minerva (roman goddess of strategy): Chess board, choose best move
# 12. Bellona (oman goddess of war): Fight a monster using choices (stab, upper cut, punch, headlock)
