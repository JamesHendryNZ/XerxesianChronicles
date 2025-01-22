init python:

    #def sortBySpeed(e):
    #    fast = e.speed
    #    return fast

    #def trooperDamge( damage , trooper ):
    #    trooper.health -= damage
    def choosePlayer2Attack( currentParty ):
        counter = 0
        targetiblePlayers = []
        # set targets for the enemy troopers---------------------------------------
        while counter < len(currentParty):
            if currentParty[counter].health > 0:
                #$ turnOrder.append(currentParty[counter])
                targetiblePlayers.append(currentParty[counter])
            counter += 1
        return targetiblePlayers

    def checkForFoeTypeByName( enemyTroopers , nameOfFoe ):

        for foe in enemyTroopers:
            if foe.name == nameOfFoe:
                return True
        #---------------------------
        return False

    def fillEnemyPartyRandom( dudes , goonAddPool , enemyTroopers ):

        counter = 0

        while counter < dudes:

            randomPlace = random.randint( 0 , len( goonAddPool )-1 )
            enemyTroopers.append( copy.copy( goonAddPool[ randomPlace ] ) )
            counter += 1


    def checkIfPossible2Melee( troopers ):
        
        for trooper in troopers:
            if ( isinstance( trooper , FlyingFoe ) ) or isinstance( trooper , PatterenFoe ):
                if trooper.isFlying is False:
                    return True
            else:
                return True
                
        return False

    def checkIfPossible2Shoot( ):# will be implemented later. For underwater sections.
        #maybe if they are fighting underwater they can't shoot because arrows and sling rocks don't travel in water well
        return True

    def checkWeakness ( targetTrooper , weaponName = "" , weaponType = "" , itemType = "" , itemName = "" ):
        #check if weapon
            if weaponName != "":

                if targetTrooper.weaknessSpeficiallity:
                    if weaponName == targetTrooper.weakness:
                        return targetTrooper.weaknessFactor
                else:
                    if weaponType == targetTrooper.weakness:                        
                        return targetTrooper.weaknessFactor
            
            else:

                if targetTrooper.weaknessSpeficiallity:
                    if itemName == targetTrooper.weakness:
                        return targetTrooper.weaknessFactor
                else:
                    if itemType == targetTrooper.weakness:
                        return targetTrooper.weaknessFactor
            #if all else is false

            return 0.0

        


    def checkIfBelong( dude2Check , spcecialGroup , doesItMatter ):

        if doesItMatter:
            pointer = 0
            while pointer < len( spcecialGroup ):
                if dude2Check is spcecialGroup[ pointer ]:
                    spcecialGroup.pop( pointer )
                    return spcecialGroup
                pointer += 1
        
        return spcecialGroup
    

    def enemyPartyUpdate( foes ):
        for foe in foes:
            if ( isinstance( foe , FlyingFoe ) ) or isinstance( foe , PatterenFoe ):
                foe.updateGraphic()

#----------------------------------------------------------------------------------------------------------------------------------------



screen statusScreen:

    

    $ enemyPartyUpdate( enemyTroopers )# this is so that foes that have multiple images always use the right one and to prevent reverting back to the base foe image

    hbox:
        if renpy.mobile:
            xalign 0.50 yalign 0.92
        else:
            xalign 0.5 yalign 0.95
        for partyMember in currentParty:

            frame:
                
                xalign 0.50 yalign 1.0
                xminimum 180 xmaximum 212
                vbox:
                    $ percentHealth = round( (partyMember.health/1.0)/(partyMember.hitpoints/1.0) , 2)
                    hbox:
                        xalign 0.5
                        text partyMember.name size 20 xalign 0.5
                        if partyMember.mount.mountArmor is not "":
                            image Transform( "/gui/Mounted.png" , zoom = 0.33 )
                        if check4Effect( "Burning" , partyMember.effects ):
                            image Transform( "/gui/burningStatus.png" , zoom = 0.33 )
                        if check4Effect( "Heals" , partyMember.effects ):
                            image Transform( "/gui/healing.png" , zoom = 0.33 )
                        if check4Effect( "Entangled" , partyMember.effects ):
                            image Transform( "/gui/spider weeb.png" , zoom = 0.33)
                        if check4Effect( "BoostedAttack" , partyMember.effects ):
                            image Transform( "/gui/attackUp.png" , zoom = 0.33)
                        if check4Effect( "HardSkinned" , partyMember.effects ):
                            image Transform( "/gui/armorUp.png" , zoom = 0.33)

                    if percentHealth >= 0.7:
                        image Transform( partyMember.armors[partyMember.currentArmor].health100 , zoom = 0.8 , crop=(0 , 70 , 200 , 120 ) )
                    elif percentHealth >= 0.3 and percentHealth <= 0.69:
                        image Transform(partyMember.armors[partyMember.currentArmor].health70 , zoom = 0.8 , crop=(0 , 70 , 200 , 120 ) )
                    elif percentHealth > 0 and percentHealth <= 0.29:
                        image Transform(partyMember.armors[partyMember.currentArmor].health30 , zoom = 0.8 , crop=(0 , 70 , 200 , 120 ) )
                    else:
                        image Transform(partyMember.armors[partyMember.currentArmor].health0 , zoom = 0.8 , crop=(0 , 70 , 200 , 120 ) )
                    null height 5
                    hbox:
                        bar:
                            xmaximum 100
                            ymaximum 15 yminimum 1
                            value partyMember.health
                            range partyMember.hitpoints
                            left_gutter 0
                            right_gutter 0
                            thumb None
                            thumb_shadow None
                            left_bar Frame("gui/bar/leftBlue.png", 10, 0)

                        null width 5
                        text "[partyMember.health]/[partyMember.hitpoints]" size 15


    hbox:
        xalign 0.5 yalign 0.00
        xminimum 100 xmaximum 250
        order_reverse True

        for badTrooper in enemyTroopers:
            frame:
                xmaximum 250
                background None
                vbox:
                    xalign 0.5 yalign 0.0
                    xmaximum 250
                    frame:
                        xalign 0.5 yalign 0.0
                        xminimum 100 xmaximum 250
                        vbox:
                        
                            hbox:
                                xalign 0.5
                                text badTrooper.name size 15 xalign 0.5 layout "nobreak"
                                if check4Effect( "Burning" , badTrooper.effects ):
                                    image Transform( "/gui/burningStatus.png" , zoom = 0.33 )
                                if check4Effect( "Heals" , badTrooper.effects ):
                                    image Transform( "/gui/healing.png" , zoom = 0.33 )
                                if check4Effect( "Entangled" , badTrooper.effects ):
                                    image Transform( "/gui/spider weeb.png" , zoom = 0.33)
                        
                            hbox:
                                bar:
                                    xmaximum 100
                                    ymaximum 12 yminimum 1
                                    value badTrooper.health
                                    range badTrooper.hitpoints
                                    left_gutter 0
                                    right_gutter 0
                                    thumb None
                                    thumb_shadow None
                                    left_bar Frame("gui/bar/leftBlue.png", 10, 0)

                                null width 2

                                text "[badTrooper.health] / [badTrooper.hitpoints]" size 15 layout "nobreak"
                    image badTrooper.foeImage 
                    

#-------------------------------------------------------------------------------
screen choose2Attack( attackType ):

    $ trooperNumber = 0

    side "c t":
        xalign 0.5
        viewport id "AttackChoosevp":
            xfill False
            
            draggable True
            #mousewheel True
            #xmaximum 1280
            xalign 0.5 yalign 0.0 
            #scrollbars "horizontal"
            #scrollbar_
            


            hbox:
                xalign 0.5 #yalign 0.0 
                #xminimum 100 xmaximum 250
                #xmaximum 1280
                #order_reverse True

            #for implementation in version 0.2.1 - too close to release for version 0.2.0
            #maybe next week 30/12/24 because of rules about backups
            #vpgrid:
            #    rows 1
            #    spacing 1
            #    draggable True
            #    mousewheel True
            #    xmaximum 1280
                #xminimum 1280
            #    xalign 0.5 yalign 0.0 xpos 0.5
                #scrollbars "horizontal"

                for badTrooper in enemyTroopers:
                    frame:
                        #xmaximum 250
                        background None
                        vbox:
                            xalign 0.5 yalign 0.0
                            #xmaximum 250
                            frame:
                                xalign 0.5 yalign 0.0
                                
                                xminimum 100 xmaximum 250
                            
                                vbox:

                                    hbox:
                                        xalign 0.5
                                        text badTrooper.name size 15 xalign 0.5 layout "nobreak"
                                        if check4Effect( "Burning" , badTrooper.effects ):
                                            image Transform( "/gui/burningStatus.png" , zoom = 0.33 )
                                        if check4Effect( "Heals" , badTrooper.effects ):
                                            image Transform( "/gui/healing.png" , zoom = 0.33 )
                                        if check4Effect( "Entangled" , badTrooper.effects ):
                                            image Transform( "/gui/spider weeb.png" , zoom = 0.33)
                                        

                                    hbox:
                                        bar:
                                            xmaximum 100
                                            ymaximum 12 yminimum 1
                                            value badTrooper.health
                                            range badTrooper.hitpoints
                                            left_gutter 0
                                            right_gutter 0
                                            thumb None
                                            thumb_shadow None
                                            left_bar Frame("gui/bar/leftBlue.png", 10, 0)


                                        null width 2

                                        text "[badTrooper.health] / [badTrooper.hitpoints]" size 15 layout "nobreak"
                        
                        #check for attackings
                            if ( isinstance( badTrooper , FlyingFoe ) or isinstance( badTrooper , PatterenFoe ) ) and attackType == "melee":
                                if badTrooper.isFlying:
                                    imagebutton:
                                        idle Transform(child = badTrooper.foeImage , matrixcolor=TintMatrix('#ff6767') * BrightnessMatrix(-0.3))
                                        hover Transform(child = badTrooper.foeImage , matrixcolor=TintMatrix('#ff6767') * BrightnessMatrix(-0.3))
                                        #action badTrooper.trooperDamge( currentParty[i].attack )
                                        #action Null
                                        focus_mask True       
                                else:
                                    imagebutton:
                                        idle Transform(child = badTrooper.foeImage , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.0))
                                        hover Transform(child = badTrooper.foeImage , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.5))
                                        #action badTrooper.trooperDamge( currentParty[i].attack )
                                        focus_mask True  
                                        action [ Return(trooperNumber) ]            

                            else:
                                imagebutton:
                                    idle Transform(child = badTrooper.foeImage , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.0))
                                    hover Transform(child = badTrooper.foeImage , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.5))
                                    #action badTrooper.trooperDamge( currentParty[i].attack )
                                    focus_mask True  
                                    action [ Return(trooperNumber) ]
                    #----------------------------------------------------------
                    $ trooperNumber += 1
            #-----------------------------------------------------------------------
        bar value XScrollValue("AttackChoosevp"):
            unscrollable "hide"
            yminimum 12 ymaximum 12
            
    #----------------------------------------------------------------------------------------------
    hbox:
        if renpy.mobile:
            xalign 0.50 yalign 0.92
        else:
            xalign 0.5 yalign 0.95
        for partyMember in currentParty:
            frame:
                xalign 0.50 yalign 1.0
                xminimum 180 xmaximum 180
                vbox:
                    $ percentHealth = round( (partyMember.health/1.0)/(partyMember.hitpoints/1.0) , 2)
                    
                    hbox:
                        xalign 0.5
                        text partyMember.name size 20 xalign 0.5
                        if partyMember.mount.mountArmor is not "":
                            image Transform( "/gui/Mounted.png" , zoom = 0.33 )
                        if check4Effect( "Burning" , partyMember.effects ):
                            image Transform( "/gui/burningStatus.png" , zoom = 0.33 )
                        if check4Effect( "Heals" , partyMember.effects ):
                            image Transform( "/gui/healing.png" , zoom = 0.33 )
                        if check4Effect( "Entangled" , partyMember.effects ):
                            image Transform( "/gui/spider weeb.png" , zoom = 0.33)
                        if check4Effect( "BoostedAttack" , partyMember.effects ):
                            image Transform( "/gui/attackUp.png" , zoom = 0.33)
                        if check4Effect( "HardSkinned" , partyMember.effects ):
                            image Transform( "/gui/armorUp.png" , zoom = 0.33)
                    
                    if percentHealth >= 0.7:
                        image Transform( partyMember.armors[partyMember.currentArmor].health100 , zoom = 0.8 , crop=(0 , 70 , 200 , 120 ) )
                    elif percentHealth >= 0.3 and percentHealth <= 0.69:
                        image Transform(partyMember.armors[partyMember.currentArmor].health70 , zoom = 0.8 , crop=(0 , 70 , 200 , 120 ) )
                    elif percentHealth > 0 and percentHealth <= 0.29:
                        image Transform(partyMember.armors[partyMember.currentArmor].health30 , zoom = 0.8 , crop=(0 , 70 , 200 , 120 ) )
                    else:
                        image Transform(partyMember.armors[partyMember.currentArmor].health0 , zoom = 0.8 , crop=(0 , 70 , 200 , 120 ) )
                    null height 5
                    hbox:
                        bar:
                            xmaximum 100
                            ymaximum 15 yminimum 1
                            value partyMember.health
                            range partyMember.hitpoints
                            left_gutter 0
                            right_gutter 0
                            thumb None
                            thumb_shadow None
                            left_bar Frame("gui/bar/leftBlue.png", 10, 0)

                        null width 5
                        text "[partyMember.health]/[partyMember.hitpoints]" size 15
#----------------------------------------------------------------------


screen partySelect ( reviving ):

    $ selectedCharacterNumber = 0

    hbox:
        if renpy.mobile:
            xalign 0.50 yalign 0.92
        else:
            xalign 0.5 yalign 0.95
        for partyMember in currentParty:
            frame:
                xalign 0.50 yalign 1.0
                xminimum 180 xmaximum 212
                vbox:

                    $ percentHealth = round( (partyMember.health/1.0)/(partyMember.hitpoints/1.0) , 2)
                    hbox:
                        xalign 0.5
                        text partyMember.name size 20 xalign 0.5
                        if partyMember.mount.mountArmor is not "":
                            image Transform( "/gui/Mounted.png" , zoom = 0.33 )
                        if check4Effect( "Burning" , partyMember.effects ):
                            image Transform( "/gui/burningStatus.png" , zoom = 0.33 )
                        if check4Effect( "Heals" , partyMember.effects ):
                            image Transform( "/gui/healing.png" , zoom = 0.33 )
                        if check4Effect( "Entangled" , partyMember.effects ):
                            image Transform( "/gui/spider weeb.png" , zoom = 0.33)
                        if check4Effect( "BoostedAttack" , partyMember.effects ):
                            image Transform( "/gui/attackUp.png" , zoom = 0.33)
                        if check4Effect( "HardSkinned" , partyMember.effects ):
                            image Transform( "/gui/armorUp.png" , zoom = 0.33)
                    
                    if reviving:

                        if percentHealth >= 0.7:
                            image Transform( partyMember.armors[partyMember.currentArmor].health100 , zoom = 0.8 , crop=(0 , 70 , 200 , 120 ) , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(-0.5) )
                        elif percentHealth >= 0.3 and percentHealth <= 0.69:
                            image Transform( partyMember.armors[partyMember.currentArmor].health70 , zoom = 0.8 , crop=(0 , 70 , 200 , 120 ) , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(-0.5) )
                        elif percentHealth > 0 and percentHealth <= 0.29:
                            image Transform( partyMember.armors[partyMember.currentArmor].health30 , zoom = 0.8 , crop=(0 , 70 , 200 , 120 ) , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(-0.5) )
                        else:
                            imagebutton:
                                idle Transform(partyMember.armors[partyMember.currentArmor].health0 , zoom = 0.8 , crop=(0 , 70 , 200 , 120 ) , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.0) )
                                hover  Transform( partyMember.armors[partyMember.currentArmor].health0 , zoom = 0.8 , crop=(0 , 70 , 200 , 120 ) , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.5) )
                                action [ Return(selectedCharacterNumber) ]
                    
                    else:
                        if percentHealth > 0.0:
                            imagebutton:
                                if percentHealth >= 0.7:
                                    idle Transform(partyMember.armors[partyMember.currentArmor].health100 , zoom = 0.8 , crop=(0 , 70 , 200 , 120 ) , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.0) )
                                    hover Transform( partyMember.armors[partyMember.currentArmor].health100 , zoom = 0.8 , crop=(0 , 70 , 200 , 120 ) , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.5) )
                                elif percentHealth >= 0.3 and percentHealth <= 0.69:
                                    idle Transform(partyMember.armors[partyMember.currentArmor].health70 , zoom = 0.8 , crop=(0 , 70 , 200 , 120 ) , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.0) )
                                    hover Transform( partyMember.armors[partyMember.currentArmor].health70 , zoom = 0.8 , crop=(0 , 70 , 200 , 120 ) , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.5) )
                                elif percentHealth > 0 and percentHealth <= 0.29:
                                    idle Transform(partyMember.armors[partyMember.currentArmor].health30 , zoom = 0.8 , crop=(0 , 70 , 200 , 120 ) , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.0) )
                                    hover Transform( partyMember.armors[partyMember.currentArmor].health30 , zoom = 0.8 , crop=(0 , 70 , 200 , 120 ) , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.5) )
                                
                                action [ Return(selectedCharacterNumber) ]
                                
                        else:
                            image Transform( partyMember.armors[partyMember.currentArmor].health0 , zoom = 0.8 , crop=(0 , 70 , 200 , 120 ) , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(-0.5) )


                    null height 5
                    hbox:
                        bar:
                            xmaximum 100
                            ymaximum 15 yminimum 1
                            value partyMember.health
                            range partyMember.hitpoints
                            left_gutter 0
                            right_gutter 0
                            thumb None
                            thumb_shadow None
                            left_bar Frame("gui/bar/leftBlue.png", 10, 0)

                        null width 5
                        text "[partyMember.health]/[partyMember.hitpoints]" size 15
            $ selectedCharacterNumber += 1



#--------------------------------------------------------------------------------



#label battleAttackLoopBoss ( isTimed , winOnTimeOut , turns , ringLeaders , endOnRingLeadersGone , foesLeft , winWhenFoeAmountKilled ):

label battleAttackLoop ( isTimed , winOnTimeOut , turns , ringLeaders = [] , foesLeft = 0 , winWhenFoeAmountKilled = False , goonAddPool = [] , goonsAllowed = 5 , ringLeaders2Kill = -1 , alternativeTargets = [] , alternativeTargets2Kill = -1 , continueStoryOnDefeat = False , canRunAway = False ):

    $ canPussyOut = canRunAway
    $ canAccessInventroyMenu = False
    #update status at beginning
    $ i = 0
    while i < len(currentParty):
        $ currentPlayer = currentParty[i]
        $ currentPlayer.updateStats()        
        $ i += 1

    if ringLeaders2Kill == -1:
        $ ringLeaders2Kill = len ( ringLeaders )
    if alternativeTargets2Kill == -1:
        $ alternativeTargets2Kill = len ( alternativeTargets )

    $ winWhenAlternativeTargetsKilled = False
    if alternativeTargets2Kill > 0:
        $ winWhenAlternativeTargetsKilled = True
    
    $ endOnRingLeadersGone = False
    if ringLeaders2Kill > 0:
        $ endOnRingLeadersGone = True



    #$ turnOrder = []
    $ playerAlive = True
    $ badTroopersAlive = True
    $ counter = 0

    #sort for turn order

    #$ turnOrder.sort(key=sortBySpeed)

    show screen statusScreen


    while playerAlive and badTroopersAlive and turns >= 0 and len( enemyTroopers ) > 0 :

        $ targetiblePlayers = []

       
        $ counter = 0

        while counter < len(enemyTroopers):
            if enemyTroopers[counter].health > 0:
                $ badTroopersAlive = True
                #$ turnOrder.append(enemyTroopers[counter])
                
                if isinstance( enemyTroopers[counter] , PatterenFoe ):
                    $ enemyTroopers[counter].updateStats()
                    $ enemyTroopers[counter].check4Flying()
                
                if isinstance( enemyTroopers[counter] , FlyingFoe ):
                    $ enemyTroopers[counter].check4Flying()

            $ counter += 1

        $i = 0
        default currentName = "LoL!"
        default currentFoe = "Da Default Dancer"
        $ currentFoe = enemyTroopers[i].name


        $ downAmount = 1

        while i < len(currentParty):

            $ currentName = currentParty[i].name

            if len(enemyTroopers) > 0:

                #apply effects
                $ canPlayTurn = True
                if check4Effect( "Entangled" , currentParty[i].effects ):
                    $ canPlayTurn = False

                
                $ statusMessage = applyEffect( currentParty[ i ].effects , currentParty[ i ] )
                $ statusMessageCount = 0
                if statusMessage is not None:
                    while statusMessageCount < len(statusMessage):
                        $ currentStatusEffect = statusMessage[statusMessageCount]
                        "[currentStatusEffect]"
                        $ statusMessageCount += 1
                #label battleMenu:

                $ playerAlive = False

                if currentParty[i].health > 0 and canPlayTurn:
                    $ playerAlive = True
                    if downAmount > 0:
                        "[currentName]'s Turn"
                    #$ currentParty[i].updateStats()
                    $ currentPlayer = currentParty[i]

                    $ currentPlayer.isDefending = False
                    $ currentPlayer.updateStats()

                    $ downAmount = 1              

                    menu:
                        "Melee Attack" if checkIfPossible2Melee( enemyTroopers ):
                            "[currentPlayer.name] attacks"

                            hide screen statusScreen
                            call screen choose2Attack( "melee" )
                            show screen statusScreen

                            $ badNumber = _return
                            #damage calulations
                            $ armorReduction = enemyTroopers[badNumber].armor - currentPlayer.armorPen

                            if armorReduction < 0:
                                $ armorReduction = 0

                            $ damage = currentPlayer.attack - armorReduction

                            # put rythm minigame in here
                            # make rythms be genrated later.

                            hide screen statusScreen

                            $ rythmPattern = getMeleePatterns( enemyTroopers[badNumber].diffculty )
                            call rythmAttack (rythmPattern[renpy.random.randint(0, len(rythmPattern)-1)] , enemyTroopers[badNumber] , currentPlayer , 1.2) from _call_rythmAttack_1

                            show screen statusScreen
                            #$ enemyTroopers[_return].health -= damage
                            $ targetName = enemyTroopers[badNumber].name

                            if enemyTroopers[badNumber].health <= 0:
                                play sound drop2DaFloor
                                play extraSound punchy
                                "[targetName] is defeated!"

                                #if enemyTroopers[ badNumber ]. in ringLeaders:
                                #    ringLeaders

                                $ originalNumber = len( ringLeaders )        
                                $ ringLeaders = checkIfBelong( enemyTroopers[badNumber] , ringLeaders , endOnRingLeadersGone )
                                if len( ringLeaders ) < originalNumber:
                                    $ ringLeaders2Kill -= 1

                                $ originalNumber = len( alternativeTargets )
                                $ alternativeTargets = checkIfBelong( enemyTroopers[badNumber] , alternativeTargets , winWhenAlternativeTargetsKilled )
                                if len( alternativeTargets ) < originalNumber:
                                    $ alternativeTargets2Kill -= 1

                                if isinstance( enemyTroopers[badNumber] , ChariotFoe ):
                                    
                                    $ enemyTroopers[badNumber].spawnTransportTroopers( enemyTroopers[badNumber].transportFoes , enemyTroopers )
                                $ enemyTroopers.pop(badNumber)


                            if currentPlayer.health <= 0:
                                play sound drop2DaFloor
                                play extraSound bloodySlam
                                "OOF!!"
                                "[currentPlayer.name] got defeated by the [targetName] in a counter attack!!"

                        #------------------------------------------------------------------------
                        "Ranged Attack" if currentPlayer.rangedWeapon.type != "None" :
                                "[currentPlayer.name] started to shoot"
                                $ useableItems = []
                                call ammoSelection( currentPlayer.rangedWeapon ) from _call_ammoSelection
                                $ downAmount = _return
                        
                        #--------------------------------------------------------------------------
                        "Throw Attack":
                            "[currentPlayer.name] looked for something to throw."
                            $ useableItems = []
                            call throwableSelection( ) from _call_throwableSelection
                            $ downAmount = _return


                        #------------------------------------------------------------------------------
                        "Items":
                            "[currentPlayer.name] went into the bag of things"
                            $ useableItems = []
                            call useItemScreen from _call_useItemScreen
                            $ downAmount = _return
                            #call useItemScreen
                        #-------------------------------------------------------------------------------
                        "Defend":
                            "[currentPlayer.name] Holds steadfast against the enemy"
                            $ currentPlayer.isDefending = True
                        #-------------------------------------------------------------------------------
                        "Leave" if canPussyOut:
                            hide screen statusScreen
                            return("pussy")
                    
                    #label battleMenuEnd:
                    #---------------------------------------------------
                #-------------------------------------------------------
                elif currentParty[i].health > 0:
                    $ playerAlive = True
            #-------------------------------------------------------
            $ i += downAmount
        #----------------------------------------------------------

        $i = 0
        #-----------------------------------------------------------------------------
        
        $ targetiblePlayers = choosePlayer2Attack( currentParty )
        #$ counter = 0
        # set targets for the enemy troopers---------------------------------------
        #while counter < len(currentParty):
        #    if currentParty[counter].health > 0:
                #$ turnOrder.append(currentParty[counter])
        #        $ targetiblePlayers.append(currentParty[counter])
        #    $counter += 1
        #---------------------------------------------------------
        $ badTroopersAlive = False
        #bad troopers turn.
        while i < len(enemyTroopers):


            #apply effects to the foes
            #$ applyEffect( enemyTroopers[ i ].effects , enemyTroopers[ i ] )
            $ canTurn = True
            if check4Effect( "Entangled" , enemyTroopers[ i ].effects ):
                $ canTurn = False
            $ statusMessage = applyEffect( enemyTroopers[ i ].effects , enemyTroopers[ i ] )
            $ statusMessageCount = 0
            
            if statusMessage is not None:
                while statusMessageCount < len(statusMessage):
                    $ currentStatusEffect = statusMessage[statusMessageCount]
                    "[currentStatusEffect]"
                    $ statusMessageCount += 1


            if enemyTroopers[i].health > 0:
                $ badTroopersAlive = True
                $ currentFoe = enemyTroopers[i]
                if len(targetiblePlayers) > 0:

                    if canTurn is False:
                        "[currentFoe.name] is entangled and cannot move."


                    elif ( isinstance( enemyTroopers[ i ] , SummonerFoe ) or isinstance( enemyTroopers[ i ] , PatterenFoe ) ) and len(enemyTroopers) < goonsAllowed and enemyTroopers[ i ].canSummon:
                        $ enemyTroopers[ i ].summonTroopers( goonsAllowed , enemyTroopers )
                        play sound bigPizyu
                        "[currentFoe.name] Summons new troops."

                    else:
                        $ targetNumber = renpy.random.randint( 0 , len(targetiblePlayers)-1)
                        $ targetPlayer = targetiblePlayers[ targetNumber ]
                        
                        $ armorReduction = targetPlayer.armorPoints - currentFoe.armorPen

                        if armorReduction < 0:
                            $ armorReduction = 0

                        if targetPlayer.isDefending:
                            if check4Effect( "HardSkinned" , targetPlayer.effects  ):
                                $ damage = currentFoe.attack * 0.35 - armorReduction
                                
                            else:
                                $ damage = currentFoe.attack * 0.7 - armorReduction
                        else:
                            if check4Effect( "HardSkinned" , targetPlayer.effects  ):
                                $ damage = currentFoe.attack * 0.5 - armorReduction
                            else:
                                $ damage = currentFoe.attack - armorReduction

                        $ attacky = int( damage )

                        if attacky < 0:
                            $ attacky = 0
                    
                        "The [currentFoe.name] Attacks [targetPlayer.name] for [attacky] damage!"

                        #" [targetPlayer.name] is defending [targetPlayer.isDefending]."
                        hide screen statusScreen

                        #will call from a list from somewhere else
                        if currentFoe.rangedFoe:
                            $ defencePattern = getRangedPatterns( currentFoe.diffculty )
                            call defenceTime ( defencePattern[renpy.random.randint( 0 , len(defencePattern)-1 )] , False , currentFoe , targetPlayer , 0.3) from _call_defenceTime
                        else:
                            $ defencePattern = getMeleeDefencePatterns( currentFoe.diffculty )
                            call defenceTime ( defencePattern[renpy.random.randint( 0 , len(defencePattern)-1 )] , True , currentFoe , targetPlayer , 0.36) from _call_defenceTime_1

                        show screen statusScreen

                        #$ targetPlayer.health -= damage

                        if targetPlayer.health <= 0:
                            play sound drop2DaFloor
                            play extraSound bloodySlam
                            "[targetPlayer.name] is defeated!!"
                            $ targetiblePlayers.pop(targetNumber)
                    
                    if currentFoe.health <= 0:
                        play sound drop2DaFloor
                        play extraSound punchy
                        "[currentFoe.name] was defeated in a counterattack!!"

                        $ originalNumber = len( ringLeaders )        
                        $ ringLeaders = checkIfBelong( currentFoe , ringLeaders , endOnRingLeadersGone )
                        if len( ringLeaders ) < originalNumber:
                            $ ringLeaders2Kill -= 1

                        $ originalNumber = len( alternativeTargets )
                        $ alternativeTargets = checkIfBelong( currentFoe , alternativeTargets , winWhenAlternativeTargetsKilled )
                        if len( alternativeTargets ) < originalNumber:
                            $ alternativeTargets2Kill -= 1

                        if isinstance( currentFoe , ChariotFoe ):
                            $ currentFoe.spawnTransportTroopers( currentFoe.transportFoes , enemyTroopers )

                        $ enemyTroopers.pop(i)
                        $ i -= 1
                        if len(enemyTroopers) <= 0:
                            $ badTroopersAlive = False
            else:
                if isinstance( enemyTroopers[ i ] , ChariotFoe ):
                    $ enemyTroopers[ i ].spawnTransportTroopers( enemyTroopers[ i ].transportFoes , enemyTroopers )
                $ enemyTroopers.pop(i)
                $ i -= 1 
                if len(enemyTroopers) <= 0:
                    $ badTroopersAlive = False
            $ i +=1
        #check if party alive----------------------------------------------------------------------
        $ counter = 0
        $ playerAlive = False
        while counter < len(currentParty):
            if currentParty[counter].health > 0:
                $ playerAlive = True
            $ counter += 1
        # iterate down a turn if it is a time combat encounter
        if isTimed:
            $ turns -= 1


        #check for foe counter
        #if winWhenFoeAmountKilled: 

            #check for extra spaces and 
        $ extraSpaces = goonsAllowed - len(enemyTroopers)
        $ foesLeft -= extraSpaces
            #check for empty slots and replenish with new foes.
        if foesLeft > 0 and len(goonAddPool) > 0:
                  

            while extraSpaces > 0:
                    
                $ dude2Add = renpy.random.randint( 0 , foesLeft )
                $ cantDo = True
                $ filledIn = False
                $ rejectedDudes = []

                if endOnRingLeadersGone:
                    if dude2Add == foesLeft :
                        while cantDo and len( rejectedDudes ) < len( ringLeaders ):
                            $ trooper2Add = ringLeaders[ renpy.random.randint( 0 , len(ringLeaders) - 1)]
                            if trooper2Add in enemyTroopers:                                     
                                if trooper2Add not in rejectedDudes:
                                    $ rejectedDudes.append( trooper2Add )
                            else:
                                $ cantDo = False
                                $ filledIn = True
                                $ enemyTroopers.append( trooper2Add ) 
                    
                    $ cantDo = True
                    $ rejectedDudes = []

                if winWhenAlternativeTargetsKilled:
                    if dude2Add == foesLeft and filledIn == False:
                        while cantDo and len( rejectedDudes ) < len( ringLeaders ):
                            $ trooper2Add = alternativeTargets[ renpy.random.randint( 0 , len(alternativeTargets) - 1)]
                            if trooper2Add in enemyTroopers:
                                if trooper2Add not in rejectedDudes:
                                    $ rejectedDudes.append( trooper2Add ) 
                            else:
                                $ cantDo = False
                                $ filledIn = True
                                $ enemyTroopers.append( trooper2Add )
                    
                if filledIn == False:
                    $ enemyTroopers.append( copy.copy( goonAddPool[ renpy.random.randint( 0 , ( len(goonAddPool) - 1 ) ) ] ) )
                    
                $ extraSpaces -= 1

        elif foesLeft <= 0 and winWhenFoeAmountKilled:
            $ badTroopersAlive = False
        #check if ringLeaders are dead.
        if ( endOnRingLeadersGone and ringLeaders2Kill <= 0 ) or ( winWhenAlternativeTargetsKilled and alternativeTargets2Kill <= 0 ):
            $ badTroopersAlive = False

        #update the pattern for patteren foes
        if badTroopersAlive:
            $ counter = 0
            while counter < len( enemyTroopers ):
                if isinstance( enemyTroopers[ counter ] , PatterenFoe ):
                    $ enemyTroopers[ counter ].tickUpOrder()
                $ counter += 1
        # endOnRingLeadersGone = False , foesLeft = 0 , winWhenFoeAmountKilled = False , goonAddPool = []
    #when it's over ----------------------------------------------------------

    $ canAccessInventroyMenu = True

    hide screen statusScreen
    
    #$ i = len(currentParty)
    #Players win
    if playerAlive and badTroopersAlive is False or winOnTimeOut and playerAlive:
        #"You kicked their asses"
        
        
        return turns
    else:
    #Game Over Yeah
        #play defeated music once
        stop music fadeout 0.5
        play sound weGotOwned fadein 0.5
        "Game Over Yeeeeaaahhhh!"
        # jump GameOver whatever
        #show screen goon1Fight("images/Enemies/astartes goons/Thia mace male v1.png")
        $ MainMenu( confirm=False , save=False )()


#( isTimed , winOnTimeOut , turns 
#, ringLeaders = [] , foesLeft = 0 , winWhenFoeAmountKilled = False , goonAddPool = [], goonsAllowed = 5 
#, ringLeaders2Kill = len(ringLeaders) , alternativeTargets = [] , alternativeTargets2Kill = len(alternativeTargets) )

screen playerActions( daMessage , canPussyOut , isTimed , winOnTimeOut , turns , ringLeaders = [] , foesLeft = 0 , winWhenFoeAmountKilled = False , goonAddPool = [], alternativeTargets = [] , ringLeaders2Kill = -1 , alternativeTargets2Kill = -1 , goonsAllowed = 5):


    hbox:
        xalign 0.5 yalign 0.04
        xminimum 100 xmaximum 250
        order_reverse True
        
        for badTrooper in enemyTroopers:

            if isinstance( badTrooper , PatterenFoe ):
                $ badTrooper.updateStats()

            frame:
                xmaximum 250
                background None            
            
                $ enemyPartyUpdate( enemyTroopers )
                image badTrooper.foeImage


    frame:
        ypos 615
        xpos 640
        yanchor 0.5
        xanchor 0.5
        vbox:
            text daMessage:
                xalign 0.5
            hbox xalign 0.5 yalign 0.5:
                button:
                    textbutton "Fight." action Call( "battleAttackLoop" , isTimed , winOnTimeOut , turns , ringLeaders = ringLeaders , ringLeaders2Kill = ringLeaders2Kill , foesLeft = foesLeft , winWhenFoeAmountKilled = winWhenFoeAmountKilled , goonAddPool = goonAddPool , alternativeTargets = alternativeTargets , alternativeTargets2Kill = alternativeTargets2Kill , goonsAllowed = goonsAllowed , canRunAway = canPussyOut) 
                    
                if canPussyOut:
                    button:
                        textbutton "Run Away." action Return("pussy")


#----------------------------------------------------------------------------

screen bossTitleScreen( textColor , backgroundColor , bossTitleSize , bossTitle , bossName , bossNameSize , xLocation , yLocation ):

    frame:
        background Frame( Transform( child = "gui/frame.png" , matrixcolor=TintMatrix( backgroundColor ) ) , 2 , 2 )
        xalign xLocation
        yalign yLocation
        vbox:
            text "[bossTitle]":
                size bossTitleSize
                color textColor
                xalign 0.5
                xanchor 0.5
            text "[bossName]":
                size bossNameSize
                color textColor
                xalign 0.5
                xanchor 0.5


    