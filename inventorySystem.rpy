#-------------------------------------------------
init python:


    def itemCheck( inventory , item , check4Index = False ):#checks amount and index of items in inventory
        
        for index , itemSlotty in enumerate(inventory):
            if itemSlotty.item.name == item.name:
                if check4Index:
                    return [ itemSlotty , index ]
                else:
                    return itemSlotty
                #return True
            
        return False
            
    
    def changeItemAmount( inventory , item , changeByAmount ):#should always be used for chaninging item amounts
        
        item2Change = itemCheck( inventory , item )
        
        if item2Change is False:
            newItemSlot = ItemSlot( item , changeByAmount )
            item2Change = newItemSlot
            inventory.append( newItemSlot )
        else:
            item2Change.amountOf += changeByAmount
        
        
        if item2Change.amountOf < 0:
            item2Change.amountOf = 0

        inventory = [ *set(inventory) ]
        cleanInventory( inventory )

    def checkIfHave( inventory , item2Check ):#default check if items are in the inventroy

        for itemSlot in inventory:
            if itemSlot.item.name == item2Check.name and itemSlot.amountOf > 0:
                return True
        return False

    def checkIfHaveType( inventory , itemType2Check ):
        for itemSlot in inventory:
            if itemSlot.item.itemType == itemType2Check and itemSlot.amountOf > 0:
                return True
        return False

    def cleanInventory( inventroy ):
        for itemSlot in inventory:
            if itemSlot.amountOf < 1:
                inventory.remove(itemSlot)
#--------------------------------------------------
default inventory = []
default money = 0

#--------------------------------------------------

   


label inventorySystemAllItems( ):

    $ inventory = [ *set(inventory) ]
    $ useableItems = []
    $ j = 0

    while j < len(inventory):
        $ useableItems.append(inventory[j])
        $ j += 1

    $ inItemScreen = True

    while inItemScreen:
        call screen showItemOptions( useableItems , True , hasBackButton = True )

        $ item2LookAt = _return

        if item2LookAt == False:
            $ inItemScreen = False
        else:
            call screen showItemDetail( item2LookAt.item )
    
    return
    #jump townTimeMenu

label inventorySystemSpecificTypeOfItem( typeOfItem ):

    $ useableItems = []
    $ j = 0

    while j < len(inventory):
        if inventory[j].item.itemType == typeOfItem:
            $ useableItems.append(inventory[j])
        $ j += 1
        
    if len(useableItems) > 0:
        call screen showItemOptions( useableItems , False )
        $ usedItem = _return 
        return usedItem

    return 0

label useItemScreen( ):

 
    $ j = 0
    $ itemContinue = True

    while j < len(inventory):
        if inventory[j].item.itemType == "grapple" or inventory[j].item.itemType == "reviver" or inventory[j].item.itemType == "potion" or inventory[j].item.itemType == "grappleNet":
            $ useableItems.append(inventory[j]) 
        
        $ j += 1
    
    #"size of useable items [itemAmountICanUse]"
    if len(useableItems) > 0:
        call screen showItemOptions( useableItems , False )
        $ usedItem = _return

        if type(usedItem) is not bool:
            "[currentPlayer.name] uses [usedItem.item.name]"
        else:
            return
        
        # makes flying/swimming troopers grounded 
        if usedItem.item.itemType == "grapple" or usedItem.item.itemType == "grappleNet":
            
            hide screen statusScreen
            call screen choose2Attack( "grappling ranged" )
            $ dude2AttackNumber = _return
            $ dudeThatGotGrappled = enemyTroopers[ dude2AttackNumber ]
            show screen statusScreen

            $ preDonk = dudeThatGotGrappled.health

            if isinstance( dudeThatGotGrappled , FlyingFoe ) or isinstance( dudeThatGotGrappled , PatterenFoe ):
                if dudeThatGotGrappled.isFlying:
                    $ itemAttacking ( dudeThatGotGrappled , currentPlayer , 1.5 , usedItem.item.effectPower , usedItem.item.effectArmorPower , False , usedItem.item )
                    #play slamming sound
                    play sound bloodySlam
                    with vpunch
                    with hpunch
                    with vpunch
                    "{size=30}{b}SLAM!!{/b}{/size}"
                    $ dudeThatGotGrappled.ground()
                    "[dudeThatGotGrappled.name] got grappled to the ground!!"
                
                else:
                    $ itemAttacking ( dudeThatGotGrappled , currentPlayer , 0.8 , usedItem.item.effectPower , usedItem.item.effectArmorPower , False , usedItem.item )
            else: 
                # this is so that the player isn't fully punished for using a grappler non-flying foe
                # also some grappler items may also have effects to give
                
                $ itemAttacking ( dudeThatGotGrappled , currentPlayer , 0.8 , usedItem.item.effectPower , usedItem.item.effectArmorPower , False , usedItem.item )
            
            $ postDonk = preDonk - dudeThatGotGrappled.health
            if postDonk > 0:
                play sound foeHit
            else:
                play sound armorProtected
            "[dudeThatGotGrappled.name] got donked by the grappler for [postDonk] damage!!"

            if dudeThatGotGrappled.health <= 0:
                play sound bloodySlam
                play extraSound drop2DaFloor
                "[dudeThatGotGrappled.name] got donked out!"
                $ enemyTroopers.pop( dude2AttackNumber )

            #throwable grapplers like nets are consumables
            if usedItem.item.itemType == "grappleNet":
                $ changeItemAmount( inventory , usedItem.item , -1 )
            return 1
        
        elif usedItem.item.itemType == "reviver":
            #"Get a people select screen"
            call screen partySelect( True )
            $ dude2Revive = currentParty[_return]
            $ dude2Revive.resurrect()
            
            play extraSound ressurection
            "[dude2Revive.name] got revived."

            $ changeItemAmount( inventory , usedItem.item , -1 )
            #$ usedItem.amountOf -= 1
            return 1

        elif usedItem.item.itemType == "potion":
            #"Get a people select screen"
            call screen partySelect ( False )
            $ dude2Heal = currentParty[_return]
            #"[_return]"
            $ dude2Heal.health += usedItem.item.effectPower
            if dude2Heal.health > dude2Heal.hitpoints:
                $ dude2Heal.health = dude2Heal.hitpoints

            if usedItem.item.effectDuration > 0:
                
                $ addEffects( usedItem.item.effectType , dude2Heal , usedItem.item.effectDuration , usedItem.item.effectPower , usedItem.item.name )
                #check for other effects
                if usedItem.item.effectType == "HardSkinned":
                    "[dude2Heal.name] will be tougher for [usedItem.item.effectDuration] turns."
                if usedItem.item.effectType == "BoostedAttack":
                    "[dude2Heal.name] will be hitting harder for [usedItem.item.effectDuration] turns."
            
            if dude2Heal.health > dude2Heal.hitpoints:
                $ dude2Heal.health = dude2Heal.hitpoints
            
            play sound PowerUp
            "[dude2Heal.name] was healed [usedItem.item.effectPower] health"

            $ changeItemAmount( inventory , usedItem.item , -1 )
            #$ usedItem.amountOf -= 1
            return 1

        return 1
   
   
    else:
        "Nothing in here is useful."
        return 0

label ammoSelection( rangedWeapon , inBattle = True ):

    $ useableItems = []
    $ j = 0
    
    while j < len(inventory):

        $ currentItem = inventory[j]

        if inventory[j].item.itemType == "ammo":
            if rangedWeapon.type == "Bow" and inventory[j].item.effectType == "Shoot":
                $ useableItems.append(inventory[j])
            
            if rangedWeapon.type == "Sling" and inventory[j].item.effectType == "Sling":
                $ useableItems.append(inventory[j])
        
        $ j += 1
    
    
    if len(useableItems) > 0 and inBattle:

        call screen showItemOptions( useableItems , False )
        $ selectedAmmo = _return

        if type(selectedAmmo) is not bool:
            "[currentPlayer.name] uses [selectedAmmo.item.name] as ammo"
        else:
            return 0

        hide screen statusScreen
        call screen choose2Attack( "ranged ")
        
        $ dude2AttackNumber = _return


        call shootingTime( selectedAmmo.item.effectPower , selectedAmmo.item.effectArmorPower , enemyTroopers[dude2AttackNumber] , currentPlayer , True , selectedAmmo ) from _call_shootingTime
        

        show screen statusScreen

        if enemyTroopers[dude2AttackNumber].health <= 0:
            $ deadDude = enemyTroopers[dude2AttackNumber]
            play sound drop2DaFloor
            play extraSound punchy

            if isinstance( deadDude , ChariotFoe ):                    
                $ deadDude.spawnTransportTroopers( deadDude.transportFoes , enemyTroopers )
            
            "[deadDude.name] is defeated!"

            $ originalNumber = len( ringLeaders )        
            $ ringLeaders = checkIfBelong( enemyTroopers[dude2AttackNumber] , ringLeaders , endOnRingLeadersGone )
            if len( ringLeaders ) < originalNumber:
                $ ringLeaders2Kill -= 1

            $ originalNumber = len( alternativeTargets )
            $ alternativeTargets = checkIfBelong( enemyTroopers[dude2AttackNumber] , alternativeTargets , winWhenAlternativeTargetsKilled )
            if len( alternativeTargets ) < originalNumber:
                $ alternativeTargets2Kill -= 1

            $ enemyTroopers.pop(dude2AttackNumber)

        return 1
        #jump battleMenuEnd

    elif len(useableItems) > 0 and not inBattle:
        call screen showItemOptions( useableItems , False )
        $ selectedAmmo = _return

        if type(selectedAmmo) is not bool:
            "[currentPlayer.name] uses [selectedAmmo.item.name] as ammo"
            return selectedAmmo
        else:
            return 0        

    else:
        "The [rangedWeapon.weaponName] is out of ammo."
        return 0
        #jump battleMenu
    



label throwableSelection( inBattle = True ):

    $ useableItems = []
    $ j = 0
    $ splash = 0

    while j < len(inventory):
        if inventory[j].item.itemType == "javelin":
            $ useableItems.append(inventory[j])
        $ j += 1
    
    $j = 0
    
    while j < len(inventory):
        if inventory[j].item.itemType == "bomb":
            $ useableItems.append(inventory[j])
        
        $ j += 1
    
    if len(useableItems) > 0 and inBattle:
        call screen showItemOptions( useableItems , False )
        $ throableItem = _return

        hide screen statusScreen

        if type(throableItem) is bool:
            jump battleMenu
        elif type(throableItem) is ItemSlot:


            if throableItem.item.itemType == "bomb":
                
                call screen choose2Attack( "explosion" )

                
                #$ dude2Attack = enemyTroopers[_return]
                
                show screen statusScreen
                play extraSound daBOOM

                $ splashCenter = _return
            
                while splash < len(enemyTroopers):
                
                    $ splashDistance = abs( splashCenter - splash )
                    $ splashFactor = 1.0 - (0.3 * splashDistance )

                    # 1.0 - 0.7 - 0.4 - 0.1 - -0.2=0.0

                    #"[splashFactor] and [splashDistance]"
                    $ originalHealth = enemyTroopers[splash].health

                    if splashFactor < 0:
                        $ splashFactor = 0
                
                    if splashFactor > 0:
                        


                        $ itemAttacking( enemyTroopers[splash] , currentPlayer , splashFactor , throableItem.item.effectPower , throableItem.item.effectArmorPower , False , throableItem.item )
                        
                        #Bombs have different effects when it comes to applying effects
                        #if splashFactor > 0.5 and throableItem.effectDuration > 0:
                            #$ addEffects( throableItem.effectType , enemyTroopers[splash] , throableItem.effectDuration , throableItem.effectPower , throableItem.name )
                    

                    $ currentDude = enemyTroopers[splash]
                    if originalHealth > currentDude.health:
                        if currentDude.health > 0:
                            $ blasted4 = originalHealth - currentDude.health
                            play sound foeHit
                            "[currentDude.name] got caught in the blast for [blasted4] damage"
                        
                        elif currentDude.health <= 0:
                            play sound meatEplosion
                            
                            if isinstance( currentDude , ChariotFoe ):                    
                                $ currentDude.spawnTransportTroopers( currentDude.transportFoes , enemyTroopers )

                            "[currentDude.name] GOT BLASTED TO BITS!!"

                            $ originalNumber = len( ringLeaders )        
                            $ ringLeaders = checkIfBelong( enemyTroopers[ splash ] , ringLeaders , endOnRingLeadersGone )
                            if len( ringLeaders ) < originalNumber:
                                $ ringLeaders2Kill -= 1

                            $ originalNumber = len( alternativeTargets )
                            $ alternativeTargets = checkIfBelong( enemyTroopers[ splash ] , alternativeTargets , winWhenAlternativeTargetsKilled )
                            if len( alternativeTargets ) < originalNumber:
                                $ alternativeTargets2Kill -= 1

                            $ enemyTroopers.pop(splash)
                            $ splash -= 1
                            $ splashCenter -= 1
                    $ splash += 1

                $ changeItemAmount( inventory , throableItem.item , -1 )
                #$ throableItem.amountOf -= 1
                return 1
            #--------------------------------------------
                


            elif throableItem.item.itemType == "javelin":

                call screen choose2Attack("ranged")
                #$ dude2Attack = enemyTroopers[_return]
                $ splashCenter = _return

                call shootingTime( throableItem.item.effectPower , throableItem.item.effectArmorPower , enemyTroopers[splashCenter] , currentPlayer , False , throableItem ) from _call_shootingTime_1

                show screen statusScreen
                
                if enemyTroopers[splashCenter].health <= 0:
                    $ deadDude = enemyTroopers[splashCenter]
                    play sound drop2DaFloor
                    play extraSound punchy

                    if isinstance( deadDude , ChariotFoe ):                    
                        $ deadDude.spawnTransportTroopers( deadDude.transportFoes , enemyTroopers )

                    "[deadDude.name] is defeated!"

                    $ originalNumber = len( ringLeaders )        
                    $ ringLeaders = checkIfBelong( enemyTroopers[splashCenter] , ringLeaders , endOnRingLeadersGone )
                    if len( ringLeaders ) < originalNumber:
                        $ ringLeaders2Kill -= 1

                    $ originalNumber = len( alternativeTargets )
                    $ alternativeTargets = checkIfBelong( enemyTroopers[splashCenter] , alternativeTargets , winWhenAlternativeTargetsKilled )
                    if len( alternativeTargets ) < originalNumber:
                        $ alternativeTargets2Kill -= 1

                    $ enemyTroopers.pop(splashCenter)
                
                return 1
    elif len(useableItems) > 0 and not inBattle:
        call screen showItemOptions( useableItems , False )
        $ throableItem = _return

        hide screen statusScreen

        return throableItem

    else:
        "There is nothing that can be thrown at the enemy"
        return 0



#----------------------------------------------------------------------------------

screen showItemOptions( useableItems , showMoney , hasBackButton = False ):

    frame:
        xalign 0.5
        yalign 0.5

        background Frame( "/gui/frame_Xerx.png" )
        ypadding 10
        vbox:
            vpgrid :
                if renpy.mobile:
                    rows 2
                else:
                    rows 3
                spacing 2
                draggable True
                mousewheel True
                xminimum 200
                xmaximum 1000
                
                scrollbars "horizontal"

                for itemSlotty in useableItems:

                    frame:
                        
                        if renpy.mobile:
                            xminimum 300
                            yminimum 300
                        else:
                            xminimum 200
                            yminimum 180
                        
                        background Frame( "/gui/frame_Xerx.png" )

                        vbox:
                            if renpy.mobile:
                                $ icon = Transform( child = itemSlotty.item.image , zoom = 0.3 , matrixcolor=TintMatrix('#ffffff'))
                            else:
                                $ icon = Transform( child = itemSlotty.item.image , zoom = 0.15 , matrixcolor=TintMatrix('#ffffff'))
                            $ lightIcon = Transform( icon , zoom = 1.0 , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.5))
                            $ darkIcon = Transform( icon , zoom = 1.0 , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(-0.5))

                            

                            if itemSlotty.amountOf > 0:
                                imagebutton: 
                                    idle icon
                                    hover lightIcon
                                    #background item.image
                                    if renpy.mobile:
                                        xminimum 300 xmaximum 500
                                    else:
                                        xminimum 200 xmaximum 400

                                    action [ Hide("showItemOptions") , Return(itemSlotty) ]
                            else:
                                imagebutton: 
                                    idle darkIcon
                                    hover darkIcon
                                    #background item.image
                                    xminimum 100 xmaximum 300

                            text itemSlotty.item.name:
                                if renpy.mobile:
                                    size 25
                                    outlines [ (3 , "#fff" , 0 , 0 )] 
                                else:
                                    size 20
                                    outlines [ (2 , "#fff" , 0 , 0 )] 
                            text str(itemSlotty.amountOf):
                                if renpy.mobile:
                                    size 25
                                    outlines [ (3 , "#fff" , 0 , 0 )] 
                                else:
                                    size 20
                                    outlines [ (2 , "#fff" , 0 , 0 )] 
            
                #xminimum 200 xmaximum 200
            hbox:
                yanchor 1.0
                ypos 1.0
                image "images/items/daric.webp":
                    zoom 0.2
                    #xpos 0.1
                text "[money] Dariks":
                    if renpy.mobile:
                        size 25
                        outlines [ (3 , "#fff" , 0 , 0 )] 
                    else:
                        size 20
                        outlines [ (2 , "#fff" , 0 , 0 )] 

            if hasBackButton:
                frame:
                    style "namebox"
                    yanchor 1.0
                    ypos 1.0
                    xanchor 1.0
                    xpos 1.0
                    
                    textbutton "Back": 
                        action [ Hide("showItemOptions") , Return(False)]

#------------------------------------------------------------------------------------------------        

screen showItemDetail( selectedItem ):
    


    #modal True
    frame: 
        xalign 0.5
        yalign 0.5
        xmaximum 900
        padding ( 20 , 20 )
        vbox:
            text selectedItem.name:
                size 25
                outlines [ (2 , "#fff" , 0 , 0 )]

            hbox:
                image Transform( child = selectedItem.image , zoom = 0.5 , matrixcolor=TintMatrix('#ffffff')) 
                
            text selectedItem.description

           
            
                
            frame:
                style "namebox"
                yanchor 1.0
                ypos 1.0
                xanchor 1.0
                xpos 1.0
                textbutton "Back":
                    action Return( 0 )

