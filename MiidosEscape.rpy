

label zardonianWoodsAmbush:
    #in the woods

    #show troopas

    #ambush time
    xerx "ZARDONIAN MINOBITES!?"
    xerx "AT least let us leave Zardonia first Taruhira!"

    zardjun "{b}YES!!"
    zardjun "Taruhira knows th truth assassins!!"
    #need code if they go down the wait option
    tesi "{b}ASTARTE WAS THE ASSASSIN!!"

    zardjun "Will that matter when you're dead."

    #battle happends

    
label escapeDaAttack:
    #Xerxes Tesipiz Volkara trimdius and the Assiria and what's left of the Azagara embassies and elites 
    #flee trhough the forest.

    #they get attacked by Jemesis' forces
    #unlike in the sneaky jemesis' goons are more straight foorward.

    zardjun "Stop trators and jamesians!"
    zardjun "You are to be put to death for killing Queen Taruhira."
    xerx "We did not kill Taruhira!"
    trim "Astarte most likely did."
    tesi "Astarte wants us to fight for her gain!"

    zardjun "No."
    zardjun "You jamesians are now irrelivant desert dwellers!"
    zardjun "Now you and your backward and your camel tribes and these rebellious hill savages will soon taste the glory of Zardonia and the Astart Empire!"

    #battle time


#it's a little maze that should end with a fight agaist the kizharyuutu form of the Astarte clone sent to end Xerxes and friends

label villageIntercept:
    "village time"
    zardCat "FOR KING JEMESIS!!"
    zardCat "FOR PRINCE VERSANIZ III!!"

    menu:
        "Quick go left!":
            jump spoodaRoad
        "Push though the Cataphracts!":
            jump alongDaWoods
        "Blast through the Barricade!":
            jump pushTroughDaVillage

label spoodaRoad:
    "Road of the spider"

    menu:
        "Fight the Junatu":
            "Fight da spooda"
            jump toDaMountains
        "Escpae into the field":
            jump goatFieldEscape

label toDaMountains:
    "Escape to the mountains"
    jump astarteBattleInField

label pushTroughDaVillage:
    "Pushing through the barracade"
    jump astarteBattleInField

label alongDaWoods:
    "Chasing along the woods"

label goatFieldEscape:
    "Goats"
    jump astarteBattleInField

label woodenEscape:
    "Esape through the woods."
    jump astarteBattleInField


label escapeWithAssiriaAndAzagara:
    #"They get harassed out the gates of Miidos"
    
    zardjun "Their is no escape for you traitorous scum!"
    zardCapt "Take them all out!"
    #"They get attacked in the woods"
    zardCat "Close in on them!!"
    zardjun "Kill as many we you can!!"
    #"They punch through the blockade in the village"
    trim "They knew we would try to escape."
    trim "The ambush and the barricades would take too long to set up it they were reacting."
    trim "This was planned."

    xerx "We should head to Zarat."
    trim "There is an unfortified bridge to the north-west of here."
    trim "Although we will be expected there."
    xerx "Well."
    xerx "The quicker we punch through."
    xerx "The less time they have to form a response."

    #"They make it to the village"
    jump astarteBridgeGuard

    
