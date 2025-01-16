
init python:


    config.allow_underfull_grids = True

    def getSellableItems( inventory ):

        sellbleItems = []
        for potentialItem in inventory:
            if potentialItem.item.itemType != "quest" and potentialItem.item.itemType != "grapple":
                sellbleItems.append( potentialItem )
        
        
        return sellbleItems


    def sellItems( selectedItem , selectedAmount , daAmount ):
        
        global money
        #int( money )
        
        if daAmount >= selectedAmount:
            money += ( selectedItem.cost * selectedAmount ) / 2
            int ( money )
            #selectedItem.amountOf -= selectedAmount
            changeItemAmount( inventory , selectedItem , -selectedAmount )
            return 1
        else:
            return 2

    def buyItems( selectedItem , selectedAmount ):

        global money

        #if selectedItem not in inventory:
        #    inventory.append( selectedItem )    
        
        if ( selectedItem.cost * selectedAmount ) <= money:
            money -= selectedItem.cost * selectedAmount
            #selectedItem.amountOf += selectedAmount
            changeItemAmount( inventory , selectedItem , selectedAmount )
            return 1
        else:
            return 2
        
#return codes for shop.
#0 = unused shop - sad - then leave shop.
#1 = used shop - get item ask if they want to do anything else.
#2 = angry shopkeeper - angry because the player tried to fraud them - menu on if they want to try again.
#3 = used shop but got no item - leaves the shop after a see you later
#---------------------------------------------------



label shopBasic( items2Sell , ifUsedShop , isAngryShop ):



    while True:
        menu:
            "Buy":
                call screen selectItems2BuySell( True , items2Sell , getSellableItems( inventory ) )
                $ amount2BuySell = 1
                call screen SelectAmount( _return[ 0 ] , _return[ 1 ] , 0 )
                if _return != 0:
                    call screen Confirmation( _return[0] , _return[1] , _return[2] , _return[ 3 ] )
                    if _return !=0:
                        if buyItems( _return[ 0 ] , _return[ 1 ] ) == 1:
                            return( [ 0 , _return[ 0 ].image ] )
                        else:
                            return( 2 )
            "Sell":
                call screen selectItems2BuySell( False , [] , getSellableItems( inventory ) )
                $ amount2BuySell = 1
                call screen SelectAmount( _return[ 0 ] , _return[ 1 ] , _return[ 2 ] )
                if _return != 0:
                    call screen Confirmation( _return[ 0 ] , _return[ 1 ] , _return[ 2 ] , _return[ 3 ] )
                    if _return != 0:
                        if sellItems( _return[ 0 ] , _return[ 1 ] , _return[ 2 ]) == 1:
                            return( [ 1 , _return[ 0 ].image ] )
                        else:
                            return( 2 )
            "Leave":

                if ifUsedShop:
                    return( 3 )

                else:
                    return ( 0 )
                
                



screen selectItems2BuySell( isBuying , items2Sell , sellableItems ):


    hbox:
        xpos 0.5
        ypos 0.5
        xanchor 0.5
        yanchor 0.5
        frame:
            xalign 0.5
            yalign 0.5

            xmaximum 640

            background Frame( "/gui/frame_Xerx.png" )
            ypadding 10
            
            vbox:
                frame:
                    background Frame( "/gui/frame_Xerx.png" )
                    xalign 0.5
                    text "Current Inventory":
                        outlines [ (2 , "#fff" , 0 , 0 )]
                vpgrid:
                    rows 2
                    spacing 2
                    draggable True
                    mousewheel True
                    xminimum 500
                    xalign 0.5
                    scrollbars "horizontal"

                    for itemSlot in sellableItems:

                        frame:

                            background Frame( "/gui/frame_Xerx.png" )
                            yminimum 150
                            
                            vbox:
                                $ icon = Transform( child = itemSlot.item.image , zoom = 0.2 , matrixcolor=TintMatrix('#ffffff'))
                                $ lightIcon = Transform( icon , zoom = 1.0 , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.5))
                                $ darkIcon = Transform( icon , zoom = 1.0 , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(-0.5))
                                
                                
                                if isBuying:
                                    if itemSlot.amountOf:
                                        imagebutton:
                                            idle icon
                                            hover icon  
                                        #background item.image
                                            xminimum 200 xmaximum 300
                                            yminimum 100

                                        #action [ Hide("showItemOptions") , Return(item) ]

                                    text itemSlot.item.name:
                                        size 22
                                        outlines [ (2 , "#fff" , 0 , 0 )] 
                                        layout "nobreak"
                                    text str(itemSlot.amountOf):
                                        size 25
                                        outlines [ (2 , "#fff" , 0 , 0 )]                                    
                                else:

                                    if itemSlot.amountOf > 0:
                                            imagebutton: 
                                                idle icon
                                                hover lightIcon
                                                #background item.image
                                                xminimum 250 xmaximum 400
                                                yminimum 100
                                                action Return( [ isBuying , itemSlot.item , itemSlot.amountOf ] )
                                        #action [ Hide("showItemOptions") , Return(item) ]
                                    else:
                                        imagebutton: 
                                            idle darkIcon
                                            hover darkIcon
                                            #background item.image
                                            xminimum 200 xmaximum 300
                                            yminimum 100

                                    text itemSlot.item.name:
                                        size 25 
                                        outlines [ (2 , "#fff" , 0 , 0 )]
                                    text f" { str(itemSlot.amountOf) } - Sell Value : {itemSlot.item.cost/2:.0f}":
                                        size 20
                                        outlines [ (2 , "#fff" , 0 , 0 )]

            
                #xminimum 200 xmaximum 200

                hbox:
                    image "images/items/daric.webp":
                        zoom 0.2
                        xpos 0.1
                    text "[money] Darics":
                        size 25
                        xpos 0.15
                        yalign 0.5
                        outlines [ (2 , "#fff" , 0 , 0 )]

                

#-------------------------------------------------------------------
        if isBuying:
        
            frame:
                xalign 0.5
                yalign 0.5

                background Frame( "/gui/frame_Xerx.png" )
                ypadding 10
                xmaximum 640
                vbox:
                    frame:
                        background Frame( "/gui/frame_Xerx.png" )
                        xalign 0.5
                        text "Items for Purchase":
                            outlines [ (2 , "#fff" , 0 , 0 )]
                    
                    vpgrid:
                        rows 2
                        spacing 2
                        draggable True
                        mousewheel True
                        xmaximum 700
                        scrollbars "horizontal"

                        for buyItem in items2Sell:

                            frame:

                                background Frame( "/gui/frame_Xerx.png" )

                                vbox:
                                    $ icon = Transform( child = buyItem.image , zoom = 0.2 , matrixcolor=TintMatrix('#ffffff'))
                                    $ lightIcon = Transform( icon , zoom = 1.0 , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.5))
                                    $ darkIcon = Transform( icon , zoom = 1.0 , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(-0.5))

                            


                                    imagebutton: 
                                        idle icon
                                        hover lightIcon
                                        #background item.image
                                        xminimum 200 xmaximum 300
                                        yminimum 100
                                        ymaximum 100
                                        action Return( [ isBuying , buyItem ] )
                                        #action Null

                                    text buyItem.name:
                                        size 22
                                        outlines [ (2 , "#fff" , 0 , 0 )] 
                                        layout "nobreak"
                                    text f"{buyItem.cost} Darics":
                                        size 25
                                        outlines [ (2 , "#fff" , 0 , 0 )]
            
                #xminimum 200 xmaximum 200

#-------------------------------------------------------------------

screen SelectAmount( isBuying , selectedItem , daAmount ):
    
    if isBuying and selectedItem.cost > money:
        $ daRange = 10
    elif isBuying:
        $ daRange = int( money / selectedItem.cost )
    else:
        $ daRange = daAmount

    #modal True
    frame: 
        xalign 0.5
        yalign 0.5
        xmaximum 800
        vbox:
            text selectedItem.name:
                size 25
                outlines [ (2 , "#fff" , 0 , 0 )]

            hbox:
                image Transform( child = selectedItem.image , zoom = 0.5 , matrixcolor=TintMatrix('#ffffff'))
                if isBuying:
                    text f"Cost per item : {selectedItem.cost}"
                else:
                    text f"Money gained per item : {str( int( round( selectedItem.cost / 2 , 0 ) ) )}"    
                
            text selectedItem.description

            hbox:
                text f"Amount to {'Buy' if isBuying else 'Sell'}:  "
                
                bar:
                    xmaximum 500
                    ymaximum 25 yminimum 1
                    value VariableValue( "amount2BuySell" , daRange )
                    range daRange
                    left_gutter 0
                    right_gutter 0
                    thumb Frame ( Transform ( child = "gui/namebox_Xerx.png" , matrixcolor = TintMatrix("#fff") ) , 0 ,0 )
                    thumb_offset 2
                    thumb_shadow None
                null width 5
                text "[amount2BuySell]"
                #input default 1 allow "0123456789" length 3 value VariableInputValue("amount2BuySell")

            if isBuying:
                $ totalCost = selectedItem.cost * amount2BuySell
            else:
                $ totalCost = int( round( ( selectedItem.cost*amount2BuySell ) / 2 , 0 ) ) 

            if isBuying and totalCost > money:
                text "Total Cost {color=#ff0000}" +  str( totalCost ) + "{/color}"
            elif isBuying:
                text f"Total Cost: { str( totalCost ) }   Money Left : { str ( abs( money - totalCost ) )  } "
            elif daAmount - amount2BuySell < 0:
                text f"{selectedItem.name}s left after: " + "{color=#ff0000}" + str( daAmount - amount2BuySell ) + "{/color}"
            else:            
                text f"Money Gained: { str( totalCost ) }   Money After : { str ( abs( money + totalCost ) )  }  {selectedItem.name}s left after: { str( daAmount - amount2BuySell )}"

            
            hbox:
                xalign 0.5
                #spacing parent.width
                xfill True
                #xfit True 
                #xsize this
                
                frame:
                    xalign 0.0
                    textbutton "Cancel":
                        action Return( 0 )
                frame:
                    xalign 1.0
                    xanchor 1.0
                    if amount2BuySell <= 0:
                        textbutton f"{'Buy' if isBuying else 'Sell'}"
                    else:
                        textbutton f"{'Buy' if isBuying else 'Sell'}":
                            action Return( [ selectedItem , amount2BuySell , isBuying , daAmount ] )
                


#---------------------------------------------------------------------

screen Confirmation( selectedItem , selectedAmount , isBuying , daAmount ):
    

    
    frame: 
        xalign 0.5
        yalign 0.5
        
        xmaximum 800
        vbox:
            text selectedItem.name:
                size 25
                outlines [ (2 , "#fff" , 0 , 0 )]

            hbox:
                image Transform( child = selectedItem.image , zoom = 0.5 , matrixcolor=TintMatrix('#ffffff'))

            text selectedItem.description

            if isBuying:

                if selectedAmount*selectedItem.cost > money:
                    text "{color=#ff0000}You can't afford this.{/color}"

                text f"Buying { selectedAmount } { selectedItem.name }{'s' if selectedAmount > 1 else ''} for { selectedItem.cost*int(amount2BuySell) } darics."
                text f"Money after perchase { money - ( selectedAmount * selectedItem.cost )}"
            else:

                if selectedAmount > daAmount:
                    text f"You don't have enough { selectedItem.name }s":
                        color "#ff0000"

                text f"Selling { selectedAmount } { selectedItem.name }{'s' if selectedAmount > 1 else ''} { str( int( round( ( selectedItem.cost*int(amount2BuySell) ) / 2 , 0 ) ) ) } darics."

            hbox:
                xalign 0.5
                xfill True
                frame:
                    xalign 0.0
                    textbutton "Cancel":
                        action Return( 0 )
                
                frame:
                    xalign 1.0
                    xanchor 1.0
                    
                    if isBuying:    
                        textbutton "Buy":
                            action Return( [ selectedItem , selectedAmount , daAmount ] )
                    
                    else:
                        textbutton "Sell":
                            action Return( [ selectedItem , selectedAmount , daAmount ] ) 

screen showItemImage( image2Show , maxtrixLight = TintMatrix("#fff") , horizontalPos = 0.5 , verticlePos = 0.5 , zoomies = 0.7):
    image Transform( child=image2Show , zoom = zoomies , matrixcolor = maxtrixLight):
        xalign horizontalPos
        yalign verticlePos
