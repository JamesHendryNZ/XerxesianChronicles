init python:

    #This is where pateerns will be stored and gotten
    #if it gets to big mayabe do it from a JSON file but 
    #this will do for the time being.
    #it justs needs to not be stored in active memory until its use is needed.

    #The melee rythm patterns for when the characters are attacking the
    #enemy troopers
    #long patterns will be constructed by concatinating multiple small patterns
    #together.
    #difficulty can also be done by modifing speed.

    #later the the unicode text characters will be replaced by 32x32 image graphics
    def getMeleePatterns( diffculty ):

        if diffculty == "easy":
            return (["zzxc","cxxx","zxcc","xxcz","zxc$c","$c$czx","czzx","xxxx","zcxc","$zzxz","!z!x!c","!x!x","zx!z","ccc!c"])
        
        elif diffculty == "medium":
            return (["xczx!c","!z!c!x$x","z!xcz","!zzc!c","!z$xcz","zzx!x","!c!zxx","xc!cz","xxc!z","$z$x!cc","!xcxz","xxc!z","cx!z$c","xc!c$z"])

        elif diffculty == "medium4":
            return (["xxc!z!z","cx!zzx","!x!z!c$c","cxcxz!c","x!x!zzc","$z$x$c!z","cxxz!z!xc","zxcx!z!x","x!x!czc","xx!c!z$x","$x!x$x!x","cxzc!c!z","!x!czxz","!z$zcx!x!c","!z!x!z!c!c!z!x!z"])

        elif diffculty == "hard" or diffculty == "medium6":
            return (["zx!z!x","!z!x!c!z","!c!zxc","!x!z!c$cc","!xx!cc","z!zx!xc!c","xx!x!x$x","!c!cccc","!z!x!z!cc","zx!x!z!cc","!cc!c$xc!c","c$zz!zz!z","c!zx!cz$c","z!x!cz!xz"])
        
        #confiqure 0 and $0 before implementing patterens
        elif diffculty == "mixed3" or diffculty == "shotgun":
            return (["zx0$c","!z!xxz","0$z0x","00!x!x$z","zccx0!x!z$z","$x0xc0$c","czx0","0z0x0c","!c!xc!z0","z0!zcx","0!zx$c","$c$x!x0"])
        
        elif diffculty == "mixed4":
            return (["$c!c0c","$Zz!z0x","xc!z0","000zx!z","xxczx!z!x$xz0","0$z!zx!xc!c","zx!zx$x0","!z!x!c0!c$c","z0z0$z0","0zx0!c$c","z$x0!z!cc0x"])

        elif diffculty == "lakatinu1":
            return (["zx!z!x","!z!x!cz$z","!c!zxc","!x!z!c$cc","!xx!cc","z!zx!xc!c","xx!x!x$x","!c!cccc","!z!x!z!c$c","$zx!x!z!cc","!cc!c$xc!c","c$zz!zz!z","c!zx!cz$c","z!x!cz!xz"])
        else: # to be used in more larger randomized gerations.
            return (["zzz","xxx","ccc","!z!z!z","!x!x!x","!c!c!c","$z$z","$x$x","$c$c","z!z$z","x!x$x","c!c#c","zxc","cxz"])
    #---------------------------------------------------------------
    #patterns for melee foes
    def getMeleeDefencePatterns ( diffculty ):
        if diffculty == "easy":
            return ([["_#_","_##","__$","__#"] , ["#_$","__#","__#","__$","_##","_##"]
            ,["_#_","_#_","___","#__","_#_","_$_","__#",] , ["_#_","___","$__","##_","##_","_#_"]
            ,["_##","___","$__","##_","$__","#_#"] , ["__#","__$","_##","$__","##_","___","___","_##","___","#_#"]
            ,["_#_","$#_","##_","___","_#_","_#$","_##"] , ["_#_","_#_","_#_","_##","__$","_#$","_##"]
            ,["##_","##_","___","___","_##","_##","__$","__#"] , ["_##","_##","__#","$__","#__","##_","#__","#_#"]
            ,["_#_","#__","__#","___","_#_"] , ["_#_","##_","___","$#_","___","#__","##_","___","_##"]
            ,["$$$","_##","___","__#","_#_","___","##_","$$_","#__"]
            ,["_$_","_#_","_$_","_#_","_#_","#__","_#_"] , ["_$_","_#_","_#_","___","#_#","#_#","___","_#$"]
            ,["__$","_##","___","$__","##_","___","__$","_##"]
            ,["_#_","___","#__","_#_","___","__#","_#_"] , ["$#_","#__","_#_","___","__#","_#$","___","#_#"]
            ,["_#_","___","__#","_#_","___","#__","_#_"] , ["__$","_##","_#_","___","#__","_#_","___","#_#"]
            ,["#_#","$__","##_","___","#_#","$__","##_","___","#_#"] , ["$__","##_","___","#_#","__$","##_","_#_"]
            ,["_#_","$#_","#__","___","_#_","_#$","__#"] , [ "_$_","_#_","$#_","#__","___","_#_","_#_","_#$"]
            ,["_##","___","#_#","#__","___","_##","$#_"] , [ "##_","___","#_#","___","_#_","_$_","_#_"]])
        
        #easyMixed
        elif diffculty == "mixed3":
            return([["#_|","#|_","|_#","_#_","__|"]
            ,["|_#","_|#","#_|","|_#"]
            ,["_|_","_#_","|__","_#_","__|","_#_","|__"]
            ,["_|_","_#_","__|","_#_","|__","_#_","__|"]
            ,["|__","_#$","__|","$#_","|__"]
            ,["__|","$#_","|__","_#$","__|"]
            ,["$_|","#_#","|_$","#_#","_|_","_#_","$_|"]
            ,["_#_","|#_","_|_","_#$","_|_","##_","|__"]
            ,["_#_","_#|","_|_","$#_","_|_","_##","__|"]
            ,["_#_","_#|","_|_","$#_","_|_","_##","__|"]
            ,["_#_","_#_","_#_","##|"]
            ,["_#_","_#_","_#_","|##"]])

        elif diffculty == "medium": #medium 3 witdhs
            return ([["_#_","$#_","___","$#_","#__","__#"] , ["_#_","___","#_#","__$","_##","_#_","___","_#_"]
            ,["#_#","___","$#_","_#_","___","_#$"] , ["_#_","___","#_#","#_#","___","_#_","_#_","_#$"]
            ,["_##","___","##_","_#_","___","__#"] , ["_##","___","_#_","##_","_#_","___","_#$","_##"]
            ,["$__","#_#","___","__$","#_#","___","_##"] , ["_##","__#","___","#__","##_","$__","#_#"]
            ,["_##","___","#_$","__#","_##","___","#__","##_","##_","#__","__#","_##"]
            ,["##$","$#_","___","__#","_##","__#","#__"] , ["_#_","#__","__#","_##","__#","#__","##_"]
            ,["#$#","__#","_##","__#","#__","$_#","#__","##_"] , ["#__","__#","_##","___","$#_","##_"]
            ,["$#_","##_","___","_#$","_##","___","$#_","##_"] , ["_#_","_#$","_##","___","$#_","##_"]
            ,["##_","#__","___","$#_","___","#__","__#","_##","__$"] , [ "_##","__$", "#_#","___","_##","__$","#_#"]
            ,["_##","__#","_#$","___","_##","__#","___","$#_"] , [ "#_#","__$","_##","__#","#_$"]
            ,["__#","_$_","_#_","_##","__#","#__","##_"] , ["___","_#_","$#_","___","#_#","___","_#$"]
            ,["#_#","___","_#_","_#_","_#_","$#_","___","#_#" ] , [ "#_#","___","_##","_##","___","_#$"]
            ,["#_#","___","_#_","_#_","_#_","_#$","___","#_#" ] , [ "#_#","___","##_","##_","___","$#_"]
            ,["_#$","_##","___","$#_","##_","___","__#"] , [ "__$","_##","__#","#__","$#_","___","_#$","_$_"]])

        #mediumMixed
        elif diffculty == "mixed4": #like hydrasyon but trickier
            return([["|##_","____","_##|","____","|##_","____","$##|"]
            ,["_##|","____","|##_","____","_##|","____","|##$"]
            ,["###|","___|","#_##","_|__","___|","##_#","#__#","#_##","#_|#","#_##"]
            ,["|###","|___","##_#","__|_","|___","#_##","#__#","##_#","#|_#","##_#"]
            ,["#_#_","_|#$","_##$","|___","#__#","#_|#","#|_#","|___"]
            ,["_#_#","$#|_","$##_","___|","#__#","#|_#","#_|#","___|"]
            ,["#||#","___$","#||#","___$","#||#"]
            ,["#||#","$___","#||#","$___","#||#"]
            ,["###|","___|","__|_","_###","|__$","_|__","$___","###_"]
            ,["|###","|___","_|__","###_","$__|","__|_","___$","_###"]
            ,["_$|_","_#__","_|$_","__#_","_$|_","_##_"]
            ,["_|$_","__#_","_$|_","_#__","_|$_","_##_"]
            ,["$$$|","__#|","$$_|"]])

        elif diffculty == "medium4" or diffculty == "lakatinu1": # medium 4 widths for melee foes.
            return([["__##","_##$","_##$","____","#___","##__","###_","$$__","#$#_","__#_","_##_","_##_","_$#_"]
            ,["_#_#","_#_#","_#$#","____","#__#","$__$","#__#","____","_##_","__#_","#__#","##__","$___","#_##","#__#"]
            ,["###_","____","____","_###","____","____","###_","____","____","_###","____","____","###_","#$__","##__"]
            ,["__##","_##_","___$","__##","___$","_###","___$","_###","___$","_###","___$","_###","___$","_###"]
            ,["$$$$","_##_","____","_##_","_##_","____","#__#","____","_##_","_$$_","_##_","____","#__#","#__$","$__#"]
            ,["###_","____", "____","__##","_###","____","##__","###_","##__","#__#","__##","_###","___#","##_$","##_#","$__#"]
            ,["#_##","____","##_#","____","$_##","___$","$#_#","____","##__","____","$#_#","____","_##_","$##_",]
            ,["_##_","____","###_","____","$##_","____","____","_###","____","$##$","___$","_##$","____","____","###_","$___","##_#"]
            ,["__#_","_#__","____","#__#","__##","_#$$","____","$___","_##_","_##_","##__","___#","__##","____","##__","$$#_"]
            ,["##_#","___#","#_##","____","_##_","_##$","____","#___","##__","____","__##","_##$","____","_##$","_#$_"]
            ,["_#_#","____","#_#_","____","_#_#","____","#_#_","____","_#_#","____","#_#_","____","_#_#","$#_#"]
            ,["##_#","$___","#_#_","____","_##_","$##_","____","##__","###_","#___","__##","_###","___$","_##$","_##$"]
            ,["#__#","____","_##_","____","#__#","____","_##_","____","#__#","____","_##_","____","#__#","#_#$"]
            ,["_###","____","___$","_##_","____","___$","_###","____","#___","$#__","###_","$___","_##_","$___","###_","$___","#_#_"]
            ])

        elif diffculty == "medium6":
            return(["_####_","______","#____#","##__##","$____$","##__##","______","_####_","______","_#_#_#","__$$__","#_#_#_"]
            ,["_#_#_#","#__#_$","_#__#_","##__##","$____$","#_##_#","______","####__","#####_"]
            ,["#####_","______","______","_#####","______","______","#####_","______","____##","$$#_##","#_#__$"]
            ,["_#####","______","______","#####_","______","______","_#####","______","##____","#_##$$","$_#_#_"]
            ,["#_#_#_","#___##","__#__$","_#$##_","_##___","$___##","###___","___#_#","$_____","#__###"]
            ,["#____#","##__##","###_##","$$$_$$","###_##","_##_#$","______","__##_#","_###_#","#$$#_#","$_____"]
            ,["__##__","__$$__","__##__","__$$__","__##__","#____#","_#__#_","$____$","##__##","______","__##__"]
            ,["__####","#__###","##__##","###__#","####__","#####_","#####_","####__","###__#","##__##","#__###","__####"]
            ,["####__","###__#","##__##","#__###","__####","_#####","__####","#__###","##__##","###__#","###__#","####__"]
            ,["_####_","_#$$#_","_#$$#_","_#$$#_","_####_","$$$$$$","__##__"]
            ,["#_#_#_","__$$__","_#_#_#","______","_####_","______","##__##","$____$","##__##","$____$","#____#","______","_####_"]
            ,["###_##","______","#_####","______","###_##","______","##_##_","##_##$","______","#_####","#____#","__##__","_####$"]
            ,["#####_","______","______","_#####","______","______","#####_","______","______","_#####"]
            ,["_#####","______","______","#####_","______","______","_#####","______","______","#####_"]
            ,["#_##_#","______","_####$","__#___","#_#_##","__#___","_####$"]
            ,["#_##_#","______","$####_","___#__","#_##_#","___#__","$####_"])


        elif diffculty == "hard": # hard will be 5 wide and not 3
            return ([["_#_#_","_____","_###_","_____","#_#_#","__###","#__##","$$$$$","_#_#_","_____","#_#_#","_____","##___","###_$"]
            ,["##_##","#___#","__#__","_###_","_###$","__#$_","__#__","#___#","##_##","_____","$___$","#_#_#","__#__","$_#_$"]
            ,["$___$","#_#_#","__#__","#___#","#_$_#","__#__","_#_#_","_____","_____","_###_","$###_","_##__","__#__","#___#"]
            ,["_####","_____","_____","_____","####_","_____","_____","_____","_####","_____","_____","_####","_____","__#$$"]
            ,["###__","____#","__###","#____","###_$","____#","___##","__###","_####","__###","_____","__##$","____$","__#__"]
            ,["##_##","_____","#_###","_____","###_#","_____","###_#","_____","###_#","_____","#$_##","$$___","_###_","__#$_"]
            ,["_###_","____$","#___#","_#_#_","#___$","#___#","##___","###__","####_","_____","___##","__###","_####","_____", "##_$$"]
            ,["$#_#$","#___#","$_#_$","__#__","_#$#_","_#$#_","_#$#_","_#$#_","_###_","_____","##_##","#___#","__#__","#_$_#"]
            ,["#$_$#","##_##","_____","__$__","__#__","_###_","__#__","__$__","#___#","#_#_#","_____","__#__","_###_","_####"]
            ,["#___#","#_#_#","#_$_#","#_#_#","_____","__#__","_###_","__#__","#_$_#","#_#_#","__#__","_###_","####_","###$_"]
            ,["_###_","__#__","#___#","##_##","#_$_#","__#__","_###_","$###_","_###_","__#__","#___#","#_$_#","__#__","_###$"]
            ,["_#_#_","_#_#_","$#$#$","$#_#$","$#_#_","_____","_____","_#_#_","_#_#_","$#$#$","_#$#$","_#_#$","__#__","___#_","__#$#"]
            ,["#_#$#","#___#","##_#$","#__#_","__#__","_#__#","_$__#","_#___","__#_#","_____","_#$#_","_____","_###_","_____","$#_#_","___##"]
            ,["####_","_____","___##","_####","_____","##___","####_","_____","___##","_####","_____","___$#","_##$$","_###$"]])

        #hard3 - mixed 3 2
        #hard4 - mixed 4 2
        #hard6 - 6

        #hardMixed
        
        #monsta
        #monstaMixed
        #Monsta8

        #chaosEasy
        #chaosMed
        #chaosHard
        #ChaosMonsta
        
        #Hell


        # these build a pattern sections should be 3-6 lines long with a 
        elif diffculty == "5width": # for genrating random 5 witdhs
            return ([["____#","___##","__###","_####","__$$$"]
            ,["#_#_#","_____","_#_#_","_____","_#$#_","_____","_###_","__$__"]
            ,["#____","##___","###__","####_","_____","$$$__"]
            ,["_#_#_","_____","#_#_#","_____","_###_","_____","#___#"]
            ,["_#$#_","_____","_###_","_$##_","_###_"]
            ,["$##__","_____","###__","_____","$_###"]
            ,["__##$","_____","__###","_____","###_$"]
            ,["$#$#$","_#$#$","_#$#_","_____","_###_"]
            ,["__#__","_###_","__#__","#_$_#","__#__"]
            ,["#___#","##_##","#___#","$_#_$","#___#"]
            ,["_#_#_","_#_#_","_#_#_","_#$#_","_#_##"]
            ,["#_#_#","#_#_#","#$#_#","#_###"]
            ,["#_#_#","#_#_#","#_#$#","###_#"]
            ,["_###_","__#__","#___#","##_##","#___#","$_#__"]])
        elif diffculty == "4width": # for generating random 4 widths
            return([[ "___#" , "__##" , "_###", "__$$"]
            ,[ "#___" , "##__" , "###_" , "$$__" ]
            ,[ "_##_" , "_$$_" , "_##_" , "____" , "#__#", "____" ]
            ,[ "#__#" , "____" , "_##_" , "$##_" , "$##_" , "###_" , "$___"]
            ,[ "#__#" , "____" , "_##_" , "_##$" , "_##$" , "_###" , "___$"]
            ,[ "#__#" , "$___" , "##__" , "___$" , "__##" ]
            ,[ "#__#" , "___$" , "__##" , "$___" , "##__" ]
            ,[ "_#_#" , "____" , "#_#_" ]
            ,[ "#_#_" , "____" , "_#_#" ]
            ,[ "###_" , "$$__" , "$___" , "###_" ]
            ,[ "_###" , "__$$" , "___$" , "_###" ]
            ,[ "$__$" , "##_#" , "#__#" , "__##" , "___$"]
            ,[ "$__$" , "#_##" , "#__#" , "##__" , "$___"]
            ,[ "#_##" , "#__#" , "##_#" ]
            ,[ "##_#" , "#__#" , "#_##" ]
            ])

        elif diffculty == "hydrasyon": #first mixed patteren: - keep it easy
            return([["_##_","_##_","____","_|__"]
            ,["#___","##__","###_","###|"]
            ,["___#","__##","_###","|###"]
            ,["#__#","____","_##_","##__"]
            ,["#__#","____","_##_","|#__"]
            ,["_##_","_#__","_|__","#___"]
            ,["_##_","__##","___#","___|"]
            ,["_##_","##__","#___","|___"]
            ,["###_","____","__##","____","_##_"]
            ,["_###","____","##__","____","_###"]
            ,["_#|_","____","_|#_","____","_#|_"]
            ,["_|#_","____","_#|_","____","_|#_"]
            ,["_|_#","|__#","_|#_","__|#","___|"]])

        else: # for genrating long random 3 widths
            return ([["#_#","___","_#_"]
            ,["#__","##_"]
            ,["__#","_##"]
            ,["$#_","___","##_"]
            ,["_#$","___","_##"]
            ,["##_","___","$#_"]
            ,["_##","___","$#_"]
            ,["_#_","_#_","_$_","_#_"]
            ,["#_#","#_$","$_#"]
            ,["##_","___","$#_"]
            ,["_#_","$#_","##_"]
            ,["_#_","_#$","_##"]
            ,["#$#","___","_#_"]
            ,["_$_","_#_","_$_","_#_"]])
    #--------------------------------------------------------------------
    #patterns for ranged foes
    #this can only be accessed if the targetted player has a shield
    #Rember the player has to catch the arrows with their shield to avoid damage
    #it should be esier for the player becuase ranged attacks do more damage
    #and shields are big and easy to block projectiles with
    #Big shields might be implemented and can catch more projectiles if
    #I can find a way to balance them.
    #size 1 = -
    #size 2 = --
    #size 3 = ---
    def getRangedPatterns (diffculty):
        if diffculty == "easy": # 3 width
            return ([["_|_","|__","_|_","__|","_|_"]
            ,["|__","_|_","__|","_|_","|__"]
            ,["__|","_|_","|__","_|_","__|"]
            ,["_|_","__|","___","|__"]
            ,["|__","_|_","__|","___","|__"]
            ,["__|","_|_","|__","___","__|"]
            ,["|__","_|_","__|"]
            ,["__|","_|_","|__"]
            ,["__|","_|_","|__","_|_"]
            ,["|__","_|_","__|","___","|__"]
            ,["_|_","|__","___","__|"]
            ,["__|","___","|__","___","__|","___","|__"]
            ,["|__","___","__|","___","|__","_|_"]])
        
        elif diffculty == "medium": # 4 width 
            return ([["_|__","|___","____","__|_","___|","__|_"]
            ,["|___","_|__","|___","_|__","____","__|_","___|","____","_|__","|___"]
            ,["___|","__|_","___|","__|_","___|","____","|___","_|__","|___","____","___|"]
            ,["_|__","|___","_|__","__|_","___|","_|__"]
            ,["__|_","___|","__|_","__|_","___|","____","|___"]
            ,["|___","_|__","__|_","___|","__|_","_|__","__|_","___|","__|_","|___"]
            ,["_|__","__|_","____","|___","____","__|_","___|","____","_|__","____","___|","__|_"]
            ,["___|","____","|___","___|","____","|___","____","___|","____","|___","____","|___"]
            ,["|___","____","___|","____","|___","____","___|","____","|___","____","___|"]
            ,["_|__","__|_","___|","__|_","_|__","|___","____","__|_","___|","____","_|__","|___"]
            ,["__|_","___|","__|_","_|__","____","|___","_|__","___|"]
            ,["|___","____","__|_","___|","__|_"]
            ,["___|","__|_","____","_|__","____","___|"]
            ,["|___","_|__","__|_","___|","____","_|__","|___"]])

        elif diffculty == "hard": # 5 width 
            return ([["|____","_____","__|__","___|_","____|","_____","__|__","_|___","|____","_____","__|__","_____","____|","__|__","_____","|____","_|___","__|__"]
            ,["____|","___|_","__|__","_|___","|____","_|___","__|__","___|_","__|__","_|___"]
            ,["__|__","_|___","___|_","__|__","_____","|____","_|___","__|__","_____","____|","___|_","____|","___|_","__|__","_____","|____","_|___","__|__"]
            ,["_|___","_____","____|","_____","__|__","___|_","____|","___|_","__|__","_|___","__|__","___|_","____|","_____","__|__","_|___","__|__","___|_","____|"]
            ,["___|_","____|","___|_","__|__","_|___","__|__","___|_","____|","___|_","__|__","_|___","__|__","____|"]
            ,["|____","__|__","____|","__|__","|____","__|__","____|","__|__","____|","__|__","|____","__|__","____|","__|__","|____","__|__","____|","__|__","|____"]
            ,["____|","__|__","|____","__|__","____|","__|__","|____","__|__","____|","__|__","|____","__|__","____|","__|__","|____","__|__","____|","__|__","|____"]
            ,["__|__","|____","_____","____|","_____","__|__","|____","__|__","____|","_|___","__|__"]
            ,["___|_","_|___","___|_","_|___","___|_","_____","|____","__|__","___|_","_|___","__|__","|____","_|___","___|_","__|__","____|","___|_","_|___","___|_"]
            ,["_|___","|____","__|__","___|_","__|__","_|___","|____","__|__","___|_","__|__","|____","_|___","___|_","_|___","|____","__|__","__|__","_|___","|____"]
            ,["|____","_|___","___|_","____|","___|_","_|___","___|_","____|","__|__","_|___","___|_","__|__","|____","_|___","__|__","____|","___|_","__|__","_|___"]
            ,["____|","___|_","_|___","|____","__|__","___|_","_|___","|____","_|___","___|_","____|","___|_","___|_","__|__","|____","_|___","__|__","|____"]
            ,["__|__","_|___","___|_","_|___","___|_","__|__","_|___","___|_","____|","___|_","_|___","__|__","|____","_|___","___|_","___|_","____|","___|_","_|___"]
            ,["|____","_____","____|","___|_","|____","_____","___|_","____|","_____","|____","_|___","_____","____|","__|__","|____","_____","____|"]])

        elif diffculty == "4width":
            return ([["|___","_|__","__|_","___|"]
            ,["___|","__|_","_|__","|___"]
            ,["_|__","__|_","_|__","|___"]
            ,["__|_","_|__","__|_","___|"]
            ,["|___","____","__|_","_|__"]
            ,["___|","____","_|__","__|_"]
            ,["_|__","___|","__|_","|___"]
            ,["__|_","|___","_|__","___|"]
            ,["|___","|___","_|__","_|__"]
            ,["___|","___|","__|_","__|_"]
            ,["_|__","__|_","___|","_|__"]
            ,["__|_","_|__","_|__","__|_"]
            ,["_|__","|___","_|__","__|_"]
            ,["___|","___|","_|__","__|_"]])

        elif diffculty == "5width":
            return ([["|____","_|___","__|__","___|_","____|"]
            ,["____|","___|_","__|__","_|___","|____"]
            ,["__|__","_|___","|____","_|___","__|__","___|_"]
            ,["__|__","___|_","____|","___|_","__|__","_|___"]
            ,["|____","|____","|____","_|___","_|___","__|__"]
            ,["____|","____|","____|","___|_","___|_","__|__"]
            ,["_|___","___|_","_|___","___|_","__|__","__|__"]
            ,["|____","__|__","____|","__|__"]
            ,["____|","__|__","____|","__|__"]
            ,["__|__","_|___","___|_","_|___","|____","_|___"]
            ,["___|_","____|","__|__","___|_","__|__","___|_"]
            ,["____|","___|_","_|___","__|__","___|_","__|__"]
            ,["|____","_|___","___|_","__|__","_|___","__|__"]
            ,["_|___","|____","__|__","___|_","__|__","____|"]])


        #elif diffculty == "6width":
        
        #Multi Protectiles/Shotgunning might be for foes that appear later in the game.
        elif diffculty == "3width2":
            return([["||_","|__","_||","_|_","||_"]
            ,["||_","___","_||","___","||_"]
            ,["_||","___","||_","___","_||"]
            ,["_||","__|","||_","_|_","_||"]
            ,["|_|","___","|_|","___","|_|"]
            ,["||_","||_","_|_","_||","_||"]
            ,["_||","_||","_|_","||_","||_"]
            ,["_|_","|__","__|","_|_","|__","__|"]
            ,["_|_","__|","|__","_|_","__|","|__"]
            ,["_|_","|_|","_|_","|_|"]
            ,["|__","_||","___","|__","_||"]
            ,["||_","_|_","_||"]
            ,["|||"]
            ,["|__","_|_","|__","__|","|__"]
            ,["__|","_|_","__|","|__","__|"]
            ])
            #
        elif diffculty == "4width2":
            return([["|_|_","_|_|","__||","|___"]
            ,["|___","_||_","___|","_||_","|___"]
            ,["__||","_||_","||__","__|_"]
            ,["|___","_||_","||__","__||"]
            ,["|___","___|","|___","___|","____","__|_","|___","___|","___|"]
            ,["___|","|___","___|","|___","____","_|__","___|","|___","|___"]
            ,["_|_|","|_|_","||__","___|","|___"]
            ,["||__","____","__||","____","||__","____","__||"]
            ,["__||","____","||__","____","__||","____","||__"]
            ,["_|_|","____","||__","____","|_|_","____","__||"]
            ,["|_|_","__||","_|_|","____","||__"]
            ,["_||_","||__","____","__||","_|_|"]
            ,["_||_","__||","____","||__","|_|_"]
            ,["|___","|||_","___|","_||_"]
            ,["___|","_|||","|___","_||_"]
            ,["|||_","__||","____","_|||"]
            ])
        elif diffculty == "shotgun":
            return([["___|_","__|_|","_____","_||__","|____","_||__","__|||"]
        ,["_|_|_","|____","__|__","_||__","_____","__|||","___|_"]
        ,["__|__","_|||_","_____","|____","||___","|||__"]
        ,["_|_|_","__|__","_|_|_","_____","__|__","_||__","__|_|"]
        ,["_|___","|_|__","_____","__||_","____|","__||_","|||__"]
        ,["_|___","_____","____|","__|||","|||__"]
        ,["___|_","_____","|____","|||__","__|||"]
        ,["__|__","_|_|_","|_|__","_|___","|||__"]
        ,["__|__","_|_|_","__|_|","___|_","__|||"]
        ,["_|___","___|_","_|___","__|__","_|||_"]
        ,["___|_","_|___","___|_","__|__","_|||_"]
        ,["|||__","__|||"]
        ,["__|||","|||__"]]
        )
        #elif diffculty == "4width3":
            #return([[]
            #,[]
            #,[]
            #])
        #elif diffculty == "5width2":
            #return([[]
            #,[]
            #,[]
            #])
        #elif diffculty == "5width3":
            #return([[]
            #,[]
            #,[]
            #])        
        #elif diffculty == "5width4":
            #return([[]
            #,[]
            #,[]
            #])   
        elif diffculty == "hydrasyon": #first mixed patteren: - missles and lazors
            return([["|___","#|__","##__","##__","_#_|","___#","___#","___#"]
            ,["___|","_|#_","__##","__##","|_#_","#___","#___","#___"]
            ,["_|__","_#__","_#__","_#_|","___|","___#","|__#","#_|#","#_#_","#_#_","#___"]
            ,["___|","__|#","__##","__##","|_##","#_#_","#___","#__|","___#","___#","___#"]
            ,["__|_","_|#_","_##_","_##_","_#__","___|","___#","|__#","#__#","#___","#___"]
            ,["||__","##__","##__","##__","_|__","_#__","_#__","_#_|","___#","___#","___#"]
            ,["__||","_|##","_###","_###","_#__","____","___|","__|#","__##","__##","__#_"]
            ,["___|","_|_#","_#_#","_#_#","_#__","|___","#___","#__|","#__#","#|_#","_#_#","_#__","_#__"]
            ])     
        else: # default is always 3 width
            return ([["|__","___","_|_","___","|__"]
            ,["__|","___","_|_","___","||_"]
            ,["_|_","_|_","_|_","___","__||"]
            ,["|__","|__","|__","___","_|_"]
            ,["__|","__|","__|"]
            ,["|__","___","__|"]
            ,["__|","___","__|","___","||_"]
            ,["|__","___","__|","___","__|"]
            ,["__|","___","|__","___","_|_"]
            ,["_|_","___","___","__|"]
            ,["__|","___","___","_|_"]
            ,["|__","___","_||","|__"]
            ,["|__","___","|__","___","_|_"]
            ,["__|","___","__|","___","_||"]])
    #--------------------------------------------------------------

