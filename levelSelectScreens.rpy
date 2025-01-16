
screen select3Zonez( zone1 , zone2 , zone3 , canGo2Ectabana = False ):


    if canGo2Ectabana:

        vbox:
            xpos 0.495
            ypos 0.543
            xanchor 0.5
            yanchor 0.5
            hbox:

                frame:
                    yalign 0.6
                    yanchor 0.5
                    background Frame( "gui/frame_Xerx.png" )
                    hbox:
                        text "Ectabana":
                            size 18
                            #action Return( 3 )


                imagebutton:
                    #xpos 0.2
                    idle Transform ( child = "images/map icons/Ectabana Select.webp" , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.1) , zoom = 1.0)
                    hover Transform ( child = "images/map icons/Ectabana Select.webp" , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.5) , zoom = 1.0)
                    focus_mask True
                    action Return( 4 )


    if zone1:
        
        vbox:
            
            xpos 0.54
            ypos 0.68
            xanchor 0.5
            yanchor 0.5
            vbox:
                
                imagebutton:
                    #xpos 0.3
                    idle Transform ( child="images/map icons/Serinium Zwotilya Select.webp" , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.0)  , zoom = 1.0)
                    hover Transform ( child = "images/map icons/Serinium Zwotilya Select.webp" , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.5) , zoom = 1.0)
                    focus_mask True
                    action Return( 1 ) 
                frame:
                    background Frame ( "gui/frame_Xerx.png" )
                    xpos 0.1
                    hbox:
                        
                        image Transform ( child = "images/items/keysZwotiSoAM.webp" , zoom = 0.05)
                        text "Mount Zwoti Shrine":
                            size 18
                        #action Return( 1 )
    else:
        vbox:
            
            xpos 0.54
            ypos 0.68
            xanchor 0.5
            yanchor 0.5
            vbox:
                
                imagebutton:
                    #xpos 0.3
                    idle Transform ( child="images/map icons/Serinium Zwotilya Select.webp" , matrixcolor=TintMatrix('#20972c') * BrightnessMatrix(-0.2)  , zoom = 1.00)
                    hover Transform ( child = "images/map icons/Serinium Zwotilya Select.webp" , matrixcolor=TintMatrix('#20972c') * BrightnessMatrix(-0.2) , zoom = 1.00)
                    focus_mask True
                    #action Return( 1 ) 
                frame:
                    background Frame ( "gui/frame_Xerx.png" )
                    xpos 0.1
                    hbox:
                        
                        #image Transform ( child = "images/items/keysZwotiSoAM.webp" , zoom = 0.05)
                        text "Mount Zwoti Shrine":
                            size 18
                        #action Return( 1 )        
    if zone2:

        vbox:
            
            xpos 0.556
            ypos 0.32
            xanchor 0.5
            yanchor 0.5
            vbox:
                
                imagebutton:
                    xpos 0.3
                    idle Transform ( child = "images/map icons/Kworitx Mine Select.webp" , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.1) , zoom = 1.00)
                    hover Transform ( child = "images/map icons/Kworitx Mine Select.webp" , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.5) , zoom = 1.0)
                    focus_mask True
                    action Return ( 2 )
                frame:
                    background Frame( "gui/frame_Xerx.png" )
                    hbox:
                        image Transform ( child = "images/items/keyKworitxSoAM.webp" , zoom = 0.05)
                        text "Abandoned Kwortix Mine":
                            size 18
                            #action Return( 2 )
    else:
        vbox:
            
            xpos 0.56
            ypos 0.3
            xanchor 0.5
            yanchor 0.5
            vbox:
                
                imagebutton:
                    xpos 0.3
                    idle Transform ( child = "images/map icons/Kworitx Mine Select.webp" , matrixcolor=TintMatrix('#20972c') * BrightnessMatrix(-0.2) , zoom = 1.00)
                    hover Transform ( child = "images/map icons/Kworitx Mine Select.webp" , matrixcolor=TintMatrix('#20972c') * BrightnessMatrix(-0.2) , zoom = 1.00)
                    focus_mask True
                    action Return ( 2 )
                frame:
                    background Frame( "gui/frame_Xerx.png" )
                    hbox:
                        text "Abandoned Kwortix Mine":
                            size 18
                            #action Return( 2 )

    if zone3:

        vbox:
            xpos 0.76
            ypos 0.582
            xanchor 0.5
            yanchor 0.5
            vbox:
                
                imagebutton:
                    xpos 0.2
                    idle Transform ( child = "images/map icons/Takurium Ruins Select.webp" , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.1) , zoom = 1.00)
                    hover Transform ( child = "images/map icons/Takurium Ruins Select.webp" , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.5) , zoom = 1.00)
                    focus_mask True
                    action Return( 3 )
                frame:
                    background Frame( "gui/frame_Xerx.png" )
                    hbox:
                        image Transform ( child = "images/items/keyTakuriumSoAM.webp" , zoom = 0.05)
                        text "Takurium Ruins":
                            size 18
                            #action Return( 3 )
    else:
        vbox:
            xpos 0.758
            ypos 0.582
            xanchor 0.5
            yanchor 0.5
            vbox:
                
                imagebutton:
                    xpos 0.2
                    idle Transform ( child = "images/map icons/Takurium Ruins Select.webp" , matrixcolor=TintMatrix('#20972c') * BrightnessMatrix(-0.2) * BrightnessMatrix(0.1) , zoom = 1.0)
                    hover Transform ( child = "images/map icons/Takurium Ruins Select.webp" , matrixcolor=TintMatrix('#20972c') * BrightnessMatrix(-0.2) * BrightnessMatrix(0.5) , zoom = 1.0)
                    focus_mask True
                    #action Return( 3 )
                frame:
                    background Frame( "gui/frame_Xerx.png" )
                    hbox:
                        text "Takurium Ruins":
                            size 18
                            #action Return( 3 )


