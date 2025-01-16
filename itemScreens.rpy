init python:

    def getBiggestItemAmount( ressipi , inventory ):
        
        maxNumber = 1
        
        neededItems = ressipi.startItems

        for resipiItem in neededItems:
            item2CheckAmount = itemCheck( inventory , resipiItem[0] )
            if item2CheckAmount is not False:
                if item2CheckAmount.amountOf > maxNumber:
                    maxNumber = item2CheckAmount.amountOf
        
        return maxNumber
    #------------------------------------------------------------

    def calulatateAmountNeeded( ressipi , inventory , resquestedAmount , isMaking=False ):
        neededItems = ressipi.startItems
        canMake = True
        endItems = ressipi.endItems
        neededAmount = [ ]



        for startItem in neededItems:
            #neededAmount.append( [ startItem[ 0 ] , startItem[ 1 ] * resquestedAmount ] )
            
            if checkIfHave( inventory , startItem[ 0 ] ):
                if itemCheck( inventory , startItem[ 0 ] ).amountOf < startItem[ 1 ] * resquestedAmount:
                    canMake = False
                #some items
                neededAmount.append( [ startItem[ 0 ] , startItem[ 1 ] * resquestedAmount , itemCheck( inventory , startItem[ 0 ] ).amountOf ] )
            else:
                #no items
                canMake = False
                neededAmount.append( [ startItem[ 0 ] , startItem[ 1 ] * resquestedAmount , 0 ] )

            #if startItem[ 0 ].amountOf < startItem[ 1 ] * resquestedAmount:
            #    canMake = False


        if isMaking and canMake:
            for endProduct in endItems:
                #endProduct[ 0 ].amountOf += endProduct[ 1 ] * resquestedAmount
                changeItemAmount( inventory , endProduct[ 0 ] , endProduct[ 1 ] * resquestedAmount )

            for need in neededItems:
                #need[ 0 ].amountOf -= need[ 1 ] * resquestedAmount
                changeItemAmount( inventory , need[ 0 ] , -need[ 1 ] * resquestedAmount )

        if isMaking is False:    
            return [ canMake , neededAmount ]

    def updateAmountRequested( amountRequest ):
        if amount2Make <= 0:
            return 0
        else:
            return amountRequest

#--------------------------------------------------------------------------

screen craftingTime ( item2Craft ):

    #modal True
    $ amountRequest = updateAmountRequested( amount2Make )
   
    $ canIMakeIt = calulatateAmountNeeded( item2Craft , inventory , amountRequest )
    
    

    frame:
        xminimum 700
        xmaximum 1280
        yminimum 480
        xalign 0.5
        yalign 0.5
        background Frame("gui/frame_Xerx.png")
        vbox:
            #xminimum 500
            #xalign 0.5
            yalign 0.5
            text item2Craft.resipiName:
                xalign 0.5
                xanchor 0.5
                size 25
                outlines [ (2 , "#fff" , 0 , 0 )]
        
            hbox:
                xalign 0.5
                yalign 0.0
                for i, startItem in enumerate( item2Craft.startItems ):
                    frame:
                        vbox:
                            
                            image Transform( child=startItem[ 0 ].image , zoom=0.5 )
                            text startItem[ 0 ].name:
                                size 25
                                outlines [ (2 , "#fff" , 0 , 0 )]                            
                            if canIMakeIt[ 0 ]:
                                text f"Uses: {str( canIMakeIt[ 1 ][ i ][ 1 ] )} ":
                                    size 25
                                    outlines [ (2 , "#fff" , 0 , 0 )]
                                    xalign 0.5
                                text f"Items after: { str( canIMakeIt[ 1 ][ i ][ 2 ] - canIMakeIt[ 1 ][ i ][ 1 ] )}":
                                    outlines [ (2 , "#fff" , 0 , 0 )] 
                            else:
                                text f"Uses: {str ( canIMakeIt[ 1 ][ i ][ 1 ] )} ":
                                    size 25
                                    color "#900"
                                    outlines [ (2 , "#fff" , 0 , 0 )]
                                    xalign 0.5
                                text "Uses more then you have.":
                                    color "#900"
                                    outlines [ (2 , "#fff" , 0 , 0 )]
                    #   place arrow grphic here.
                text "Makes":
                    size 30
                    yalign 0.5#placeholder until arrow graphic made.
            
                for i, endItem in enumerate( item2Craft.endItems ):
                    
                    $ endingAmount = itemCheck( inventory , endItem[ 0 ] )

                    frame:
                        vbox:
                            image Transform( child=endItem[ 0 ].image , zoom =0.5 )
                            text endItem[ 0 ].name:
                                size 25
                                outlines [ (2 , "#fff" , 0 , 0 )]
                                xalign 0.5
                            text f"Makes: { str( amountRequest * endItem[ 1 ] ) }":
                                size 25
                                outlines [ (2 , "#fff" , 0 , 0 )]
                                xalign 0.5
                            if endingAmount is False:
                                text f"Items after: { str( 0 + ( amountRequest * endItem[ 1 ] ) ) }":
                                    outlines [ (2 , "#fff" , 0 , 0 )]
                            else:
                                text f"Items after: { str( endingAmount.amountOf + ( amountRequest * endItem[ 1 ] ) ) }":
                                    outlines [ (2 , "#fff" , 0 , 0 )]
            #-------------------------
            hbox:
                xalign 0.5
                xanchor 0.5
                text "Amount to Make: "

                bar:
                    xmaximum 400
                    ymaximum 25 yminimum 1
                    value VariableValue( "amount2Make" , getBiggestItemAmount( item2Craft , inventory ) )
                    range 50
                    left_gutter 0
                    right_gutter 0
                    thumb Frame ( Transform ( child = "gui/namebox_Xerx.png"  ) , 0 ,0 )
                    thumb_offset 3
                    thumb_shadow None
                null width 5
                text " [amount2Make]"
                #input allow "0123456789" length 3 value VariableInputValue("amount2Make")

                #$ amountRequest = updateAmountRequested( amount2Make )
            

            hbox:
                xalign 0.5
                #spacing 100
                xfill True
                frame:
                    xalign 0.0
                    #xanchor 0.0
                    textbutton "Cancel":
                        text_size 22
                        action Return( [ False ] )

                if canIMakeIt[ 0 ] is False:
                
                    text "You don't have enough resources.":
                        color "#a00"
                        outlines [ (2 , "#fff" , 0 , 0 )] 
                        xalign 0.5

                frame:
                    xalign 1.0
                    xanchor 1.0
                    
                    if canIMakeIt[ 0 ] and amountRequest > 0:     
                        textbutton "Craft":
                            text_size 22
                            action [ Function( calulatateAmountNeeded , item2Craft , inventory , int( amountRequest ) , isMaking=True ) , Return( [ True , int( amountRequest ) ] ) ]
                
                    else:
                        textbutton "Craft":
                            text_size 22

label carftTime:

    $ timeSpent = 0
    $ itemIterator = 0
    $ isCraftin = True
    #while itemIterator < len( itemCraftResipies ):
    #    $ amount2Make = 1
    #    call screen craftingTime( itemCraftResipies[ itemIterator ] )
    #    $ itemIterator += 1
    #    if _return:
    #       $ timeSpent += 1
    while isCraftin and timeTime <= time2Night:
        call screen resipiList
        $ amount2Make = 1
        $ theResipi = _return
        if isinstance( theResipi , Resipie ):
            call screen craftingTime( theResipi )
            if len(_return) > 1:
                $ timeTime += theResipi.timeTaken * _return[ 1 ]
        else:
            return 0
          
    return 0                 
                    

#---------------------------------------------------

screen resipiList:

    
    frame:
        xminimum 800
        xmaximum 1280
        xalign 0.5
        yalign 0.5
        background Frame("gui/frame_Xerx.png")
        vbox:
            frame:
                background Frame( "/gui/frame_Xerx.png" )
                xalign 0.5
                text "Item Crafting Recipes":
                    outlines [ (2 , "#fff" , 0 , 0 )]
                    size 40
                    xalign 0.5
                    
                vpgrid:
                    cols 1
                    spacing 0
                    draggable True
                    mousewheel True
                    
                    xmaximum 1280
                    ymaximum 560
                    scrollbars "vertical"
                    xalign 0.5
                    yalign 0.5

                    for resipi in itemCraftResipies:
                        
                        
                        hbox:
                            xalign 0.5
                            yalign 0.5
                            #spacing 20
                            xminimum 1000
                            frame:
                                background Frame( "/gui/frame_Xerx.png" )
                                xalign 0.5
                                xmaximum 1200
                                #yminimum 300
                                ymaximum 200
                                vbox:
                                    #xalign 0.0 
                                    frame:
                                        xalign 0.0
                                        xanchor 0.0
                                        xpos 0.0
                                        xmaximum 300
                                        #yminimum 300
                                        yfill False
                                        ymaximum 200
                                        background Frame( "/gui/frame_Xerx.png" )
                                             
                                        text "Takes":
                                            outlines [ (2 , "#fff" , 0 , 0 )]
                                        
                                        vpgrid:
                                            cols 1
                                            spacing 0
                                            draggable False
                                            mousewheel False
                                            xmaximum 500
                                            #ymaximum 500
                                            #scrollbars "vertical"
                                            xalign 0.0
                                            yalign 0.5
                                            for inputty in resipi.startItems:
                                                hbox:
                                                    image inputty[ 0 ].image:
                                                        zoom 0.125
                                                    
                                                    text "%s" % inputty[ 1 ]:
                                                        outlines [ (2 , "#fff" , 0 , 0 )]
                                                        yalign 0.5
                                                        size 18
                                                    text "%s" % inputty[ 0 ].name:
                                                        outlines [ (2 , "#fff" , 0 , 0 )]
                                                        yalign 0.5
                                                        size 18
                                #-------------------------------------------------
                                vbox:
                                    xanchor 0.5
                                    xpos 0.46
                                    yalign 0.5
                                    yanchor 0.5
                                    text resipi.resipiName:
                                        outlines [ (2 , "#fff" , 0 , 0 )]
                                        size 30
                                        xalign 0.5
                                    text "Time to make: %s flametimes." % resipi.timeTaken:
                                        outlines [ (2 , "#fff" , 0 , 0 )]
                                        xalign 0.5
                                #--------------------------------------------------
                                vbox:
                                    frame:
                                        xalign 1.0
                                        xanchor 1.0
                                        xpos 3.75
                                        xmaximum 300
                                        yfill False
                                        #ymaximum 200
                                        background Frame( "/gui/frame_Xerx.png" )
                                         
                                        text "Makes":
                                            outlines [ (2 , "#fff" , 0 , 0 )]
                                        vpgrid:
                                            cols 1
                                            spacing 2
                                            draggable False
                                            mousewheel False
                                            xmaximum 500
                                            #ymaximum 500
                                            #scrollbars "vertical"
                                            xalign 0.0
                                            yalign 0.5
                                            for outputty in resipi.endItems:
                                                hbox:
                                                    
                                                    image outputty[ 0 ].image:
                                                        zoom 0.15 
                                                    
                                                    text "%s " % outputty[ 1 ]:
                                                        yalign 0.5
                                                        outlines [ (2 , "#fff" , 0 , 0 )]
                                                    text "%s" % outputty[ 0 ].name:
                                                        yalign 0.5
                                                        outlines [ (2 , "#fff" , 0 , 0 )]
                                #---------------------------------------------------
                                frame:
                                    background Frame( "/gui/frame_Xerx.png" )
                                    xalign 1.0
                                    xpos 1.0
                                    yalign 0.5
                                    textbutton "Craft":
                                        action Return( resipi )
                    #---------------------------------------------------------------
            #bar of time------------------------------------------------------------
        frame:
            xalign 0.5
            ypos 0.9
            background Frame( "/gui/quickButton.png" )
            hbox:
                
                image "/images/The Suns.webp":
                    zoom 0.1
                bar:
                    xalign 0.5
                    yalign 0.5
                    xmaximum 600
                    ymaximum 15 yminimum 1
                    value timeTime
                    range time2Night
                    left_gutter 0
                    right_gutter 0
                    left_bar Frame("gui/bar/leftBlue.png", 10, 0)
                    #thumb Frame ( Transform ( child = "gui/namebox_Xerx.png" , matrixcolor = TintMatrix("#fff") ) , 0 ,0 )
                    #thumb_offset 2
                    #thumb_shadow None
                image "/images/Cresent Phazaros.webp":
                    zoom 0.1
        #---------------------------------------------------------------------------
        frame:
            background Frame( "/gui/frame_Xerx.png" )
            #xalign 0.5
            textbutton "Back":
                xalign 0.5
                action Return( 0 )                                                        