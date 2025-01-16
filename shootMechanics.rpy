init python:


    def caculateFactor( pointy ):
        center = timeRange / 2.00 
        distanceFromCenter = abs(center - pointy)
        #maybe have 3 be replaced by a weapon stat like crit or something later
        damageFactor = 3 - (3 * ( distanceFromCenter / center ) )
        return damageFactor


    def itemAttacking ( targetTrooper , character , attackFactor , damage , penetration , usingWeapon , ammo ):

        extraDamage = 0.0

        if usingWeapon:
            character.weaponUsed( True )
            
            if isinstance( targetTrooper , WeaknessFoe ):
                if checkWeakness ( targetTrooper , weaponName = character.weapon.weaponName , weaponType = character.weapon.type ) != 0:          
                    extraDamage = checkWeakness ( targetTrooper , weaponName = character.weapon.weaponName , weaponType = character.weapon.type )
                else:
                    extraDamage = checkWeakness ( targetTrooper , itemName = ammo.name , itemType = ammo.itemType ) 
            armorReduction = targetTrooper.armor - ( character.armorPen + penetration )       
        else:
            if isinstance( targetTrooper , WeaknessFoe ):
                extraDamage = checkWeakness ( targetTrooper , itemName = ammo.name , itemType = ammo.itemType )        
            armorReduction = targetTrooper.armor - penetration
            

        if armorReduction < 0:
            armorReduction = 0

        #check for character buffs , character.effect
        if check4Effect( "BoostedAttack" , character.effects  ):
            attackFactor += 1.0

        if usingWeapon:
            damage = ( (character.attack + damage ) * attackFactor - armorReduction ) + ( (character.attack + damage ) * extraDamage )
        else:
            damage = ( damage * attackFactor - armorReduction ) + ( damage * extraDamage )
        
        
        #check for weakness


        if damage < 0:
            damage = 0
        
        targetTrooper.health -= int(damage)

        # check for effect, add to target trooper
        if ammo.effectDuration > 0 and attackFactor > 0.5:
            addEffects( ammo.effectType , targetTrooper , ammo.effectDuration , ammo.effectPower , ammo.name )


#--------------------------------------------------------------------------------------

screen shootMechanics( timeRange , goingUp , damage , penetration , targetTrooper , character , usingWeapon , ammo , timeSpeed ):


    if goingUp:
        timer 0.03 repeat True action If(times < timeRange, true=SetVariable('times', times + timeSpeed ), false=[  Return(0) , Hide('shootMechanics')])    

    else:
        timer 0.03 repeat True action If(times > 0, true=SetVariable('times', times - timeSpeed ), false=[  Return(1) , Hide('shootMechanics')])


    #vbox:
    #    xalign 0.5
    #    yalign 0.0
    #    xanchor 0.5
    #    yanchor 0.0


    frame:
        xalign 0.5 yalign 0.1
        background Frame("gui/game icons/Nothingness.webp")
        vbox: 
            
            frame:
                #background Frame("gui/namebox_Xerx.png")
                
                xpadding 10
                ypadding 2
                xalign 0.5

                vbox:
                    text targetTrooper.name size 30 xalign 0.5 outlines [ (2 , "#fff" , 0 , 0 )]
                    hbox:
                        xalign 0.5        
                        bar:
                            xmaximum 200
                            ymaximum 15 yminimum 1
                            value targetTrooper.health
                            range targetTrooper.hitpoints
                            left_gutter 0
                            right_gutter 0
                            thumb None
                            thumb_shadow None
                            left_bar Frame("gui/bar/leftBlue.png", 10, 0)

                        null width 5
                        text "[targetTrooper.health]/[targetTrooper.hitpoints]" size 25  
            image Transform(targetTrooper.foeImage , zoom = 1.0 ):
                xalign 0.5 xanchor 0.5
            null height 5
                      

#make it so bigger enemies can be attacked and that the ui is placement is more consistant
    vbox:
        xalign 0.5
        yalign 0.9
        xanchor 0.5
        yanchor 0.9
        bar:
            xmaximum 600
            ymaximum 32 yminimum 32
            value times
            range timeRange
            base_bar Frame("/gui/game icons/targetBar.webp", 0 , 0 )
            left_gutter 0
            right_gutter 0
            thumb_offset 16
            thumb Frame("/gui/game icons/targetThumbs.webp" , 0 ,0 )
            thumb_shadow None
            xalign 0.5
            yalign 1.0
        
        frame: #for the moblie version
            xalign 0.5
            imagebutton :
                idle Transform( child = "/gui/game icons/Gui Buttons ShootIdle.webp" , zoom=1.25 )
                hover Transform( child = "/gui/game icons/Gui Buttons Shoot Hover.webp" , zoom=1.25 )
                selected Transform( child ="/gui/game icons/Gui Buttons ShootSelected.webp" , zoom=1.25 )
                action [ Function( itemAttacking ,  targetTrooper , character , caculateFactor( times )  , damage , penetration , usingWeapon , ammo )  , Hide("shootMechanics") , Return(2)]
        
    key "x" action [ Function( itemAttacking ,  targetTrooper , character , caculateFactor( times )  , damage , penetration , usingWeapon , ammo ) , Hide("shootMechanics")  , Return(2)]

#--------------------------------------------------------------------------------------------------------
label shootingTime( damage , penetration , targetTrooper , character , usingWeapon , ammo ):

    $ countinue = True
    $ times = 0.00
    $ timeRange = 1.00
    $ goingUp = True
    $ reapeats = 5 # will be set later but not now
    $ reapeatCounter = 0
    $ originalTargetTrooperHealth = targetTrooper.health
    $ timeSpeed = targetTrooper.speed * 0.02

    #check to see if foe has a weakness
    
    
    while reapeatCounter < 5:


        # minimizes time wasted by preventing overkilling or being overkilled.


        #$ intervalBetween = duration
        $ lateMercy = 0.05
        #$ times = 1.00
        #$ intervalToPress = 0.3
        $ countinue = 1


        call screen shootMechanics( timeRange , goingUp , damage , penetration , targetTrooper , character , usingWeapon , ammo.item , timeSpeed )
        #pause intervalBetween + lateMercy
        #hide screen rythmBar
        #"got to next"
        #"[rythmList]"
        $ renpy.block_rollback() #stops the cheezing
        $ countinue = _return

        if countinue == 0:
            $ goingUp = False
        elif countinue == 1:
            $ goingUp = True
            $ reapeatCounter += 1
        elif countinue == 2:
            $ ammo.amountOf -= 1
            $ reapeatCounter = 5
            
        


    #---------------------------------------------------------------

    $ totalDamage = originalTargetTrooperHealth - targetTrooper.health
    if totalDamage > 0:
        play sound arrowHit
    else:
        play sound arrowMiss
    "[targetTrooper.name] takes [totalDamage] damage."


    

    







