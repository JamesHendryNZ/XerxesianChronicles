init python:

    import random

    class Projectile:
        x = 0
        y = 0
        attack = 0
        armorPen = 0
        isFriendly = True
        speed = 1
        projectileImage = "gui/desaturated arrow.webp"



        def __init__( self , x , y , attack , armorPen , isFriendly , speed , projectileImage = "gui/desaturated arrow.webp" ):
            self.x = x
            self.y = y
            self.attack = attack
            self.armorPen = armorPen
            self.speed = speed
            self.projectileImage = projectileImage
            self.isFriendly = isFriendly

        def goUp (self , by = 1 ):
            self.y -= by
        
        def goDown( self , by = 1 ):
            self.y += by
        
        def goLeft( self , by = 1 ):
            self.x -= by

        def goRight( self , by = 1 ):
            self.x += by 

    #----------------------------------------------
    def checkFriendlyArrows( projectiles ):
        for projectile in projectiles:
            if projectile.isFriendly:
                return True
        return False
    
    def determineBehaviorType( foe ):
        #determined by foe.difficulty
        if foe.diffculty == "easy":
            return "middleStay"
        if foe.diffculty == "medium" or foe.diffculty == "3width2" :
            return "edge2Egde"
        if foe.diffculty == "hard" or foe.diffculty == "4width2" or foe.diffculty == "lakatinu1":
            return "zigZag"
        if foe.diffculty == "4width" or foe.diffculty == "5width" or foe.diffculty == "medium4":
            return "edge2Zag"
        return "edge2Edge"
    
    def determineDuration( width ):
        newDuration = random.randint( 0 , width - 1 )
        return newDuration

    def foeBehavior( behaviorType , enemyTopPosition , width , leftOrRight , duration , badTrooper , zig2Right ):

        if behaviorType == "middleStay":
            if enemyTopPosition < int(width/2)-1:
                enemyTopPosition += 1
            elif enemyTopPosition > int(width/2)-1:
                enemyTopPosition -= 1

        elif behaviorType == "edge2Egde":
            if leftOrRight:
                if enemyTopPosition >= width - 1:
                    leftOrRight = False
                    enemyTopPosition -= 1
                else:
                    enemyTopPosition += 1
            else:
                if enemyTopPosition <= 0:
                    leftOrRight = True
                    enemyTopPosition += 1
                else:
                    enemyTopPosition -= 1
        
        elif behaviorType == "zigZag":
            if leftOrRight:
                if enemyTopPosition >= width - 1:
                    leftOrRight = False
                    enemyTopPosition -= 1

                else:
                    enemyTopPosition += 1

                if duration < 1:
                    leftOrRight = False
                    duration = determineDuration( width )
                    enemyTopPosition -= 1
                    duration -= 1
                else:
                    duration -= 1
            else:
                if enemyTopPosition <= 0:
                    leftOrRight = True
                    enemyTopPosition += 1
                else:
                    enemyTopPosition -= 1
                if duration < 1:
                    leftOrRight = False
                    duration = determineDuration( width )
                    enemyTopPosition += 1
                    duration += 1
                else:
                    duration -= 1

        elif behaviorType == "edge2Zag":           
            if leftOrRight:
                if enemyTopPosition >= width - 1:
                    leftOrRight = False
                    zig2Right = False
                    enemyTopPosition -= 1

                else:
                    enemyTopPosition += 1
                #-----------------
                if duration < 1:
                    leftOrRight = False
                    if zig2Right:
                        duration = determineDuration( width )
                    else:
                        duration = determineDuration( int( width/2 ) )
                    enemyTopPosition -= 1
                    duration -= 1               
                else:
                    duration -= 1
            else:
                if enemyTopPosition <= 0:
                    leftOrRight = True
                    zig2Right = True
                    enemyTopPosition += 1
                else:
                    enemyTopPosition -= 1
                #-------------------------
                if duration < 1:
                    leftOrRight = False
                    if zig2Right:
                        duration = determineDuration( width )
                    else:
                        duration = determineDuration( int( width/2 ) )
                    enemyTopPosition += 1
                    duration += 1
                else:
                    duration -= 1

        return [ enemyTopPosition , leftOrRight , zig2Right , duration ]
    #----------------------------------------------

    def foeShootDaBullet( speed , diffculty ):
        

        #shootNow = False
        speed = speed*100
        d = 100 
            
        if diffculty == "medium": 
            d = 90
        elif diffculty == "medium4": 
            d = 80
        elif diffculty == "hard": 
            d = 60
        elif diffculty == "5width": 
            d = 70
        elif diffculty == "4width": 
            d = 75
        elif diffculty == "3width2": 
            d = 50
        elif diffculty == "4width2":
            d = 55

        if random.randint(0 , d) > speed:         
            return True       
        else:
            return False

    #----------------------------------------------
    def setUpMatrixBoard( width , height ):
        i = 0
        bufferString = ""
        pattern = []
        while i < width:
            bufferString = bufferString + "_"
            i += 1

        i = 0
        while i <= height:
            pattern.append(bufferString)
            #pattern.insert(0 , bufferString)
            i += 1

        return pattern
    #the matrix board [0][0] is the top left.
    #some targets can shoot back

    def projectileAttacking( targetTrooper , character , projectile , attackFactor ):

        armorReduction = 0

        if projectile.isFriendly:
            armorReduction = targetTrooper.armor - projectile.armorPen
        else:
            armorReduction = character.armorPoints - projectile.armorPen
        
        if armorReduction < 0:
            armorReduction = 0

        damage = projectile.attack * attackFactor - armorReduction
        if damage < 0:
            damage = 0    

        if damage > 0:    
            if projectile.isFriendly:
                targetTrooper.health -= int(damage)
            else:
                character.health -= int(damage)
    #check is the projectile is out of range
    #done to avoid out of index errorspro
    def checkEdgeCollision( projectiles , projectile , board ):
        if projectile.y > len( board ) - 1 or projectile.y < 0:
            projectiles.remove( projectile )
    
    def checkPlayerAndFoeCollsion( projectiles , projectile , board , targetTrooper , character ):
        if projectile.y == 0 and projectile.x == enemyTopPosition:
            projectileAttacking ( targetTrooper , character , projectile , 3 )
            projectiles.remove( projectile )

        elif projectile.y == len(board) - 1 and projectile.x == playerBottomPosition:
            projectileAttacking ( targetTrooper , character , projectile , 1 )
            projectiles.remove( projectile )
    
    def shootDaProjectile ( xStart , projectiles , yStart = 1 , foeTrooper = None , isFriendly = False , weapon = None , ammo = None ):
        

        #projectile2Create = Projectile( x , y , attack , armorPen , isFriendly , speed , projectileType , usingWeapon = False )
        
        
        if isFriendly:
            
            attack = ammo.item.effectPower
            armorPen = ammo.item.effectArmorPower
            if weapon is not None:
                attack += weapon.damage
                armorPen += weapon.armorPen
            projectile2Create = Projectile( xStart , yStart , attack , armorPen , True , 6 )
        else:
            projectile2Create = Projectile( xStart , yStart , foeTrooper.attack , foeTrooper.armorPen , False , foeTrooper.speed  )
    #x axis only because they can only move side 2 side

        projectiles.append( projectile2Create )

    def renderCheck( y , x , board , projectiles , targetTrooper , character ):
        
        returnImage = None
        upWay = False
        downWay = False

        if y == 0 and x == enemyTopPosition:
            returnImage = Transform( child = "gui/game icons/foeTarget.webp" , matrixcolor=TintMatrix('#ff6c6c')* BrightnessMatrix(0.3) , zoom = 1.25) 
        elif y == len(board) - 1 and x == playerBottomPosition:    
            returnImage = Transform( child = "gui/game icons/player.webp" , zoom = 1.0) 


        for projectile in projectiles:
            #check for collisions
            checkEdgeCollision( projectiles , projectile , board )
            checkPlayerAndFoeCollsion( projectiles , projectile , board , targetTrooper , character )
            
            #only render projectiles that exist after the collsion checks
            if projectile in projectiles:
                
                #returnImage = Composite( ( 40 , 40 ) )
                #set image based on direction
                if y == projectile.y and x == projectile.x:
                    if projectile.isFriendly:
                        returnImage = Transform ( child = "gui/game icons/desaturated arrow.webp" , matrixcolor=TintMatrix('#0073ff')* BrightnessMatrix(0.5) , yzoom = -1.0 , zoom = 1.0) 
                        upWay = True
                    else:
                        returnImage = Transform ( child = "gui/game icons/desaturated arrow.webp" , matrixcolor=TintMatrix('#af1d1d')* BrightnessMatrix(0.3) , zoom = 1.0 ) 
                        downWay = True
                    
                    if upWay and downWay:
                        returnImage = Transform ( child = "gui/game icons/2WayArrows.webp" , matrixcolor=TintMatrix('#6c00ba') , zoom = 1.0 ) 
                        #no need to continue the for loop as their only be 2 projectiles at on place.
                        return returnImage
                    #return "Placeholder"

        
        return returnImage

    def cleanArenaPosition( foeLand , characterLand , junk2Clear ):
        foeLand = 0
        characterLand = 0
        junk2Clear = []

default enemyTopPosition = 0
default playerBottomPosition = 0
default projectiles = []

screen shootaGame( projectileUsed , character , badTrooper , board , daProjectile , timeLeft):

           
    timer 0.05 repeat True action If(times > 0, true=SetVariable('times', times - 1 ), false=[ Return(False) , Hide('shootaGame')])

    $ playerOuch.checkHurtGraphics ( )
    $ foeOuch.checkHurtGraphics ( ) 

    $ positionalPlayerGraphic = "^"            
    $ positionalFoeGraphic = "v"
    $ percentHealth = round( (character.health/1.0)/(character.hitpoints/1.0) , 2)

    #graphics
    frame:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.5

        xmaximum 1200
        ymaximum 700
        vbox:
            hbox:
                xalign 0.5
                yalign 0.5
                image Transform( child=badTrooper.foeImage , zoom=0.4 , matrixcolor=foeOuch.hurtTint)
                text badTrooper.name
                bar:
                    xmaximum 200
                    ymaximum 15 yminimum 1
                    value badTrooper.health
                    range badTrooper.hitpoints
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None
                    left_bar Frame("gui/bar/leftBlue.png", 10, 0)
                
                text "[badTrooper.health] / [badTrooper.hitpoints]"
            text "Time Left [timeLeft]"

            frame:
                background Frame("gui/DodgeCombatFrame.webp")
                xanchor 0.5
                xpos 0.5
                vbox:
                    xalign 0.5
                    yalign 0.5

                    $ ypoint = 0    
                    for column in board:
                    
                        $ xpoint = 0
                        hbox:
                            xalign 0.5
                            for row in column:
                                $ pointImage = renderCheck( ypoint , xpoint , board , projectiles , badTrooper , character )
                            
                                if pointImage is not None:
                                    image pointImage
                                else:
                                    vbox:
                                        xminimum 32
                                        yminimum 32                                
                            
                                $ xpoint += 1
                        $ ypoint += 1

            hbox:
                xalign 0.5
                if percentHealth >= 0.7:
                    image Transform( character.armors[character.currentArmor].health100 , zoom = 0.8 , crop=(0 , 70 , 200 , 120 ) , matrixcolor=playerOuch.hurtTint )
                elif percentHealth >= 0.3 and percentHealth <= 0.69:
                    image Transform(character.armors[character.currentArmor].health70 , zoom = 0.8 , crop=(0 , 70 , 200 , 120 ) , matrixcolor=playerOuch.hurtTint )
                elif percentHealth > 0 and percentHealth <= 0.29:
                    image Transform(character.armors[character.currentArmor].health30 , zoom = 0.8 , crop=(0 , 70 , 200 , 120 ) , matrixcolor=playerOuch.hurtTint )
                else:
                    image Transform(character.armors[character.currentArmor].health0 , zoom = 0.8 , crop=(0 , 70 , 200 , 120 ) , matrixcolor=playerOuch.hurtTint )
                text character.name
                bar:
                    xmaximum 200
                    ymaximum 15 yminimum 1
                    value character.health
                    range character.hitpoints
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None
                    left_bar Frame("gui/bar/leftBlue.png", 10, 0)
                
                text "[character.health] / [character.hitpoints]"  

                image projectileUsed.item.image:
                    zoom 0.2
                text "[projectileUsed.amountOf]"      
        
            imagebutton:
                ypos 1.0
                yanchor 1.0
                xpos 0.5
                xanchor 0.5

                idle Transform( child = "/gui/game icons/Gui Buttons ShootIdle.webp" , zoom=0.66 )
                hover Transform( child = "/gui/game icons/Gui Buttons Shoot Hover.webp" , zoom=0.66 )
                selected Transform( child ="/gui/game icons/Gui Buttons ShootSelected.webp" , zoom=0.66 )

                if daProjectile.amountOf > 0:
                    action [ Function( shootDaProjectile , playerBottomPosition , projectiles , yStart = len(board)-2 , foeTrooper = None , isFriendly = True , weapon = character.rangedWeapon , ammo = daProjectile ),  Return(True)  ]                    
    #--------------------------------------------------
    #will be buttons on the android version
    #the playerIsDaSame Here
    imagebutton:
        
        ypos 1.0
        yanchor 1.0

        idle "gui/game icons/PressZLeftIdle.webp"
        hover "gui/game icons/PressZLeftHover.webp"
        #
        #
        action [SetVariable( "playerBottomPosition" , move2DaLeft ( playerBottomPosition ) ),  Return(True) ]
    


    imagebutton:

        ypos 1.0
        xpos 1.0
        xanchor 1.0
        yanchor 1.0

        idle "gui/game icons/PressCRightIdle.webp"
        hover "gui/game icons/PressCRightHover.webp"
                    #
                    #
        action [SetVariable( "playerBottomPosition" , move2DaRight ( playerBottomPosition , len(board[0]) - 1 ) ),  Return(True) ]
            #text " Z <- -> C ":
            #    size 12
            #    xalign 0.5
#-------------------------------------------------

    key "c" action [SetVariable( "playerBottomPosition" , move2DaRight ( playerBottomPosition , len(board[0]) - 1 ) ),  Return(True) ]
    if daProjectile.amountOf > 0:
        key "x" action [ Function( shootDaProjectile , playerBottomPosition , projectiles , yStart = len(board)-2 , foeTrooper = None , isFriendly = True , weapon = character.rangedWeapon , ammo = daProjectile ) , Function( changeItemAmount , inventory , daProjectile.item , -1 ),  Return(True)  ]
    key "z" action [SetVariable( "playerBottomPosition" , move2DaLeft ( playerBottomPosition ) ),  Return(True) ]    

label shootaSetUp( widthOfLand , hightOfLand , loopss , character , badTrooper , daProjectile , characterLocation = 0):

    $ enemyTopPosition = random.randint( 0, widthOfLand - 1)
    $ playerBottomPosition = characterLocation
    $ loopAmounts = loopss * widthOfLand
    $ daArena = setUpMatrixBoard( widthOfLand , hightOfLand )
    $ duration = 1
    $ friendlyTime = int( ( 1 / character.speed ) * 12 )/ 2
    $ foeTime = int( ( 1 / badTrooper.speed ) * 12 ) 
    $ ticker = 0
    $ leftOrRight = True
    $ zig2Right = True
    $ behavior = determineBehaviorType( badTrooper )
    $ leftMove = 0
    $ rightMove = 0
    $ moves = 0

    while moves < loopAmounts and badTrooper.health > 0:

        $ countinue = True

        call screen shootaGame( daProjectile , character , badTrooper , daArena , daProjectile , loopAmounts - moves )

        $ renpy.block_rollback() #stops the cheezing
        $ countinue = _return

        if countinue is False:
            
            $ ticker += 1
            #update positions
            if character.health < 1:
                hide screen shootaGame
                return [ 1 , playerBottomPosition ]
            if badTrooper.health < 1:
                hide screen shootaGame
                return [ 2 , playerBottomPosition ]
            if daProjectile.amountOf < 1 and not checkFriendlyArrows( projectiles ):
                hide screen shootaGame
                return [ 3 , playerBottomPosition ]            
            
            #-----------------------------------------
            if ticker % foeTime == 0:

                if badTrooper.rangedFoe:
                    if foeShootDaBullet( badTrooper.speed , badTrooper.diffculty ):
                        $ shootDaProjectile ( enemyTopPosition , enemyTopPosition , projectiles , foeTrooper = badTrooper )
                $ foeReturns = foeBehavior( behavior , enemyTopPosition , widthOfLand , leftOrRight , duration , badTrooper , zig2Right )
                # return [ enemyTopPosition , leftOrRight , zig2Right , duration ]
                $ enemyTopPosition = foeReturns[ 0 ]
                $ leftOrRight = foeReturns[ 1 ]
                $ zig2Right = foeReturns[ 2 ]
                $ duration = foeReturns[ 3 ]

            #update 
            $ projectileCounter = 0
            while projectileCounter < len(projectiles):
            
                
                if projectiles[projectileCounter].isFriendly and ticker % friendlyTime == 0:
                    $ projectiles[projectileCounter].goUp()
                elif not projectiles[projectileCounter].isFriendly and ticker % foeTime == 0:
                    $ projectiles[projectileCounter].goDown()

                $ projectileCounter += 1
            #--------------------------------------------------------------
            $ times = 1
            $ moves += 1

    $ foeOuch.resetTint()
    return [ 0 , playerBottomPosition ]

