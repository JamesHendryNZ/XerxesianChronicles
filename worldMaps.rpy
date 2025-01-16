
#this is where all the world maps should be placed
#maps used more than once will be placed here
#all labels should be called to render map before
#showing screens and animations


label mapOfDaWorldoSouthJamesia:

    #should show all locations

    scene map2:
            xpos -0.8
            ypos -0.8

    with fade
    
    return

label lowerJamesosRealmMap:

    scene map2:
            xpos -2.5
            ypos -1.9

    return

label middleJamesosRealmMap:
    scene map2:
            zoom 0.6
            xpos -0.2
            ypos -0.4

    return

label jamesosRealmSmollAndWholl:

    #use variables for dynamic icons
    
    #za worldo
    scene map2:
            zoom 0.4
            xpos -0.05
            ypos -0.2

    #variants based on events
    #bardaiya shahneh reveal
    #ahrite courruption levels
    

    return