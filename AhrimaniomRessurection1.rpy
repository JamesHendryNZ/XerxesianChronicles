



label ahrimaniomResurrectionPart1:

    play music ahriteCavess fadein 1.0 fadeout 1.0
    scene ahriteBaseCenter at size08:
        xpos -0.8
        ypos 0.0
        linear 5 ypos -1.5
    show ahrimaniomMK5UnderConstruction2 at truecenter , size2Thrid:
        ypos 2.0
        linear 5 ypos 0.5
    with Fade(2,0,1)
    pause 4

    show hizwenaT1Yeah at middleStand , size2Thrid with dissolve
    hiz "{i}Soon the Ahrimaniom will have a new body!"
    hiz "{i}All we need now is to install 3 energy crystals , attatch the tail,"
    hiz "{i}And a soul of a sapient being."

    hide hizwenaT1Yeah
    show hizwenaT2Commanding34 at middleStand , size2Thrid:
        xpos 0.6
        linear 1 xpos 0.7
    show ahriteT1CultistMale34 at size2Thrid:
        xpos -0.3
        linear 1 xpos 0.0
    with dissolve
    hiz "How is the Ahrite growth?"
    hiz "Do we have enough to fill the body now?"

    cultist "We just have enough ahrite."

    scene ahriteRoom at fullFit
    show tubeTentacles at quatSize , ahriteBright:
        xpos 0.5
        xanchor 0.5
        xsize 0.5
        zoom 0.5
    show transformationTube at quatSize , truecenter , ahriteBright
    show transformationTubeGiant at  quatSize , truecenter
    show transformationTubeGlass at ahriteLight , quatSize , truecenter:
        matrixcolor  BrightnessMatrix(0.8)

    show tubeTentacles as merTenta at quatSize , ahriteBright:
        xpos 0.2
        xanchor 0.5
        xsize 0.5
        zoom 0.5
    show transformationTube as merDemonTube at quatSize , left , ahriteBright
    show transformationTubeMerDeamon at quatSize , left
    show transformationTubeGlass as merDemonGlass at ahriteLight , quatSize , left:
        matrixcolor  BrightnessMatrix(0.8)

    show tubeTentacles as niomTenta at quatSize , ahriteBright:
        xpos 0.8
        xanchor 0.5
        xsize 0.5
        zoom 0.5
    show transformationTube as niomTube at quatSize , right , ahriteBright
    show transformationTubeNiom at  quatSize , right
    show transformationTubeGlass as niomGlass at ahriteLight , quatSize , right:
        matrixcolor  BrightnessMatrix(0.8)
    with fade

    cultist "We can reperpose the energy crystals from our transformation tubes once they're done."

    scene ahriteBaseCenter at size08:
        xpos -0.8
        ypos -1.5
    show ahrimaniomMK5UnderConstruction2 at truecenter , size2Thrid:
        ypos 0.5

    show hizwenaT2Commanding34 at tesiRight ,  size08 , noLegs
    show ahriteT1CultistMale34 at xerxLeftLeft , size08 , noLegs
    with dissolve
    hiz "How long will that be?"
    cultist "A week at most."

    hide hizwenaT2Commanding34
    show hizwenaT1Yeah at tesiRight , noLegs
    with dissolve
    hiz "Good."
    hiz "We'll kidnap the sacrificial victim when he's ready."

    hide hizwenaT1Yeah 
    hide ahriteT1CultistMale34
    show hizwenaT1Praising at tesiRight , noLegs
    show ahriteT1CultistMalePraising at xerxLeftLeft , noLegs
    with dissolve
    hiz "{b}PRAISE BE TO THE AHRIMANIOM!!"
    hiz "{b}PRAISE TO THE AHRITE PARADISE!!"
    return
