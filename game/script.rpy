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
    scene bg room
    show eileen happy

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
    return

# 5. Ma'at (Egyptian goddess symbolizing justice): Mini game, you’re the judge of conflict arguments 
# 6. Danu (irish goddess of nature): guess the plant
# 7. Saraswati (Hindu goddess, embodying arts): name the painting
# 8. Kannon (Japanese buddhist  goddess of  compassion): If you get a million dollars → keep it, burn it, give it to charity
# 9. Amaterasu (japanese Goddess of the Sun): Trivia about the Sun
# 10. Seshat (egyptian goddess of writing): Vocabulary (SAT level)
# 11. Minerva (roman goddess of strategy): Chess board, choose best move
# 12. Bellona (oman goddess of war): Fight a monster using choices (stab, upper cut, punch, headlock)