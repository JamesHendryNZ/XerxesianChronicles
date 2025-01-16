# The script of the game goes in this file.

define config.default_music_volume = 0.7
define config.default_sfx_volume = 0.7
define config.default_voice_volume = 0.7
# Declare characters used by this game. The color argument colorizes the
# name of the character.

default canAccessInventroyMenu = True

default enemyTroopers = []
default currentParty = [ xerxesCharacter ]

default IsDaytime = True
default isDusk = False
#default isMorning = False
default keys = 0

default enteringFrom = "Your Mom"
default label2Jump = ""
default playerLevel = 0
default playerLocation = [0,0]
#default canMakeBombJavelins = False
default givingKey = False
default timerTime = 20
default rythmPoints = 0
default visitedEctabana = 0

default lakatinuAssSmacks = 0
default lakatinuTalks = 0

default headPatCounter = 0  #game will assume the more the player gives affection to ato'ssa the more they want to solve xerxes' personal curse
default ahrimaniomNightmare = 0 #will cause the ahrimaniom to ressurect when it reaches a certain value
default atoBoinks = 0
default takuraBoinks = 0

#for combat hit effects
define hitTint = TintMatrix("#c00")
define defendTint = TintMatrix("#9f5")

#to show pain
default playerOuch = Hurtsees( 0 , False , TintMatrix("#fff") , TintMatrix("#fff") )
default foeOuch = Hurtsees( 0 , False , TintMatrix("#fff") , TintMatrix("#fff"))

#determins which way the dudes to after getting the soam
default goingEast = False
#default canVisitEctabana = True
#default sleepOversWithAtossa = 0

default xerxCanOverCharge = False #This is for the SoAM

default projectile = None

default deafeatedKrokkosnek = False
default killedSakuna = False
default freedTakura = False

default zaratiansHelped = False
default versanizAlive = True
default jemesisAlive = True
default yusinziaLoyal = True

default takuriumOwner = "Krokkosnek"    #

default shataLeaderFate = "alive"   

default tesiWaifuWants = True   #will be false when tesipiz gets a gf
default tesiRivalsAto = False   #Ato'ssa and Tesipiz start a rivalry because Tesipiz called Ato'ssa "Persistantly Stupid"

default leavingTown = False #Should be set to False if you don't want to chaaracters to leave

default whats4Dinner = "ZeBugz"

#for craft limits
default timeTime = 0
default time2Night = 90
# The game starts here.

label start:


    jump chunk1Start

    #jump chunk2assultOnEctabana1

    return


