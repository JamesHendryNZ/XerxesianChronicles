
label talkAboutGirlsInDaDesert:
    if visitedEctabana > 0 and tesiWaifuWants:
        
        
        if IsDaytime:
            scene desertRoad1:
                fit "cover"

            show xerx3HorseCurious at centerAlignment, xerxLeftHorse
            show tesipizHorseBrush at centerAlignment, tesiRightHorse:
                xzoom -1.0 
        else:
            scene desertRoad1Night:
                fit "cover"

            show xerx3HorseCurious at centerAlignment, xerxLeftHorse , nightLights
            show tesipizHorseBrush at centerAlignment, tesiRightHorse , nightLights:
                xzoom -1.0 
        with fade
        xerx "Tesipiz."
        xerx "Do you have any girls that annoy you where you live?"


        hide xerx3HorseCurious
        hide tesipizHorseBrush
        if IsDaytime:
            show xerxHorseBrush at centerAlignment, xerxLeftHorse
            show tesipiz3HorseNeutralHappy at centerAlignment, tesiRightHorse:
                xzoom -1.0 
        else:
            show xerxHorseBrush at centerAlignment, xerxLeftHorse , nightLights
            show tesipiz3HorseNeutralHappy at centerAlignment, tesiRightHorse , nightLights:
                xzoom -1.0 
        with dissolve

        tesi "No. I don't."
        
        scene clearDayTime
        show takuriumArenaBox
        show tesipizWithKorkinGF at centerAlignment:
            zoom 0.8
        with dissolve    
        tesi "I sort of want one though."

        $ tesiWaifuWants = False
    return