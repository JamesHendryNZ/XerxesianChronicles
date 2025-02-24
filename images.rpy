
#copy this template for layered images

#layeredimage nameHere:
#    group poses:
#
#    group eyes:
#
#    group mouths:



#Index
#copy from here and use find fuction for quick speed

#image transfroms

#locations
    #Ectabana Backgrounds
    #Zwoti/Serinium
    #Zwoti Shrine
    #Kwortix Mine
    #Kwortix City

    #Takuria
    #Takurium

    #Gilgamorium

    #Ahrite Zones
    #Bardaiya Shahneh
    #Bala-Axerium
    #Aratashium
    #Kiridium

    #Temple of Ahura-Mazda
#Background Asserories

#projectiles and items

#characters
    #goons
        #"Astarts" (Kazwiians , Sarratans , Hammites , Ximdians , Kirinians, Kwimians , Ssyayans, Pellosians, Centralians) 
        #Jaka
        #Faronians
        #Balatians
        #Suzumites
        #Ordoians
        #Thians
        #humanoid Monsters
        #animal Monsters
        #Bardaiya's eleite guard

    #Furries
        #Shata
        #Ssatu
        #Tastsetu
        #Shatseta
        #Tastsetrotu
        
    #Zardonians
        #Korkins
        #Junatu
        #Half-Junatu

    #Makkabians

    #ahrites

#humanoid Monsters
    #antagonists
        #bardaiya
        #lakatinu
            #Shata key lady / Muwa
        #krokkosnek
            #Krokkosnek's GirlFriends
        #Balatius
        #Minona
        #Astart Officers
        #Ahrimaniom
        #Cult of Ahriman
        #Zardossatu
        #Versaniz
        #Zagzhino
        #Siayusi
        #Muiba
        
#boss
    #Saprotius
    #Modonon
    #Sakuna
    #Haidrasyon

    #protagonists
        #Xerxes
            #Keiozia
            #Adgilia
            #Xerxes' Parents
            
        #Tesipiz
            #Ato'ssa
            #Darius
            #Shahhriit
            #Takura

        #Volkara

        #Megabazus

        #Regius
            #fatima
            #kabiwa
            
#NPCs
    #Jameisa
        #Ectabana
            #EctabanaShopLady
        #Zwotilya/Serinians
            #ShopDudeOfZwotilya
            #Nyazhmyui
        #Kworix Mine
            #Cooking Lady
        #Kworix City
    #Jamesian Troopers

    #Zarat
        #Gilgamorium
        #Yimians
        #tastsetu
    #Takuria
        #Hwassak
        #Yiwatsyoh
        #Keimdak
#Astarts
    #Bardaiya's Realm
    #Imperial Core
    #Ssyayans

#other faction characters
    #Tarminians
#image transfroms are defined here

transform fullFit:
    fit "cover"

transform hiddenLegs:
        ypos 0
        xpos 0.3

transform noLegs:
    ypos 0.3

transform flipped:
    xzoom -1.0

transform upsideDown:
    yzoom -1.0

transform middleStand:
    yalign 0.5
    xalign 0.5
    ypos 0.7

transform size08:
    zoom 0.8

transform size3quat:
    zoom 0.75

transform size2Thrid:
    zoom 0.67

transform halfSize:
    zoom 0.5

transform thridSize:
    zoom 0.33

transform quatSize:
    zoom 0.25

transform fithSize:
    zoom 0.2

transform behindTable:
    zoom 0.7
    ypos 1000

transform regularSize:
    zoom 0.8
    ypos 1100

transform bigroom:
    xpos -0.2
    ypos -0.3

transform on33Horse:
    zoom 0.5
    ypos 0.0

transform xerxLeft:
    zoom 0.8
    yalign 0.2 
    xzoom -1.0

transform xerxLeftLeft:
    zoom 0.8
    yalign 0.2 

transform volkLeft:
    zoom 0.8
    yalign 0.0

transform xerxLeftHorse:
    zoom 0.5
    ypos 0.7
    xpos 0.2     

transform tesiRight:
    zoom 0.8
    yalign 0.2
    xalign 0.9

transform atoRight:
    zoom 0.8
    xzoom -1.0
    yalign 0.1
    xalign 1.0 

transform tesiRightHorse:
    zoom 0.5
    ypos 0.7
    xpos 0.7  

transform centerAlignment:
    yalign 0.5
    xalign 0.5

transform centerAnchor:
    yanchor 0.5
    xanchor 0.5

transform longImageBottom:
    ypos 0.8

transform longImageTop:
    ypos 1.0

transform backgroundSetPlace:
    yalign 0.5
    xalign 0.5
    zoom 0.7
    yzoom 0.7
    ypos 0.3      

transform lakeBeachBackground:
    yzoom 0.5
    yanchor 1.0
    ypos 1.0

transform lakatinuRight:
    xalign 0.5
    yalign 0.5
    xpos 0.9
    ypos 0.65

transform bardaiyaLeft:
    xalign 0.5
    yalign 0.5
    xpos 0.2
    ypos 0.7

transform mwejyaRight:
    xalign 1.25 
    yalign 0.4

transform defaultTint:
    matrixcolor TintMatrix("#fff")

transform farHazeDay:
    matrixcolor TintMatrix("#a3e9fc")


transform nightLights:
    matrixcolor TintMatrix("#84c2d3")

transform darkNight:
    matrixcolor TintMatrix("#0600bc")* BrightnessMatrix( -0.3 )

transform underWaterTint:
    matrixcolor TintMatrix("#55c2ff")

transform duskLights:
    matrixcolor TintMatrix("#ffd2a1")

transform dimLights:
    matrixcolor TintMatrix("#aaa")

transform doorLights:
    matrixcolor TintMatrix("#ffa2a2")

transform arenaLights:
    matrixcolor TintMatrix("#c4ffea")

transform summonnerLights:
    matrixcolor TintMatrix("#ffff00")

transform angryColored:
    matrixcolor TintMatrix("#d30000")

transform redLightDistrict:
    matrixcolor TintMatrix("#ffc0c0")

transform lightCrystalLights:
    matrixcolor TintMatrix("#ffffd0")

transform hornyAura:
    matrixcolor TintMatrix("#ff94b4")

transform flameLight:
    matrixcolor TintMatrix("#d4a650")

transform ahriteBright:
    matrixcolor TintMatrix("#ffccff")

transform poopShade:
    matrixcolor TintMatrix("#793a00")

transform peeShade:
    matrixcolor TintMatrix("#fb0")

transform grassTint:
    matrixcolor TintMatrix("#C9FE89")
transform darkGrassTint:
    matrixcolor TintMatrix("#64B601")

transform ahriteLight:
    matrixcolor TintMatrix("#7500ce")
transform ahriteDarkness:
    matrixcolor TintMatrix("#9000ff") * BrightnessMatrix( -0.4 )

transform spins:
    linear 0.5 xzoom -1.0
    linear 0.5 xzoom 1.0
    repeat

transform flicker:
    linear 0.1 xzoom 0.1
    linear 0.1 xzoom 1.0
    repeat

transform heavyBreathing:
    zoom 0.67
    linear 1.0 zoom 0.6
    linear 1.0 zoom 0.67
    repeat

transform movingSky:
    xpan 0 ypan 0
    linear 60 xpan 360 ypan 360
    repeat  

# images are defined here
#Scences
image greenPast = "images/Jamesos Realm Green.webp" 
image ectabanaHaboob = "images/Ectabana Haboob.webp"
#image oldmap = "images/Jamesos Realm Map.webp"
image map2 = "images/game world v2.webp"
image map212Axeria = "images/212 Axeria.webp"
#image map1Small = "images/Jamesos Realm Map small.webp"
image zwotiMotelRoomXerxesYawn = "images/Zwoti Motel Room Xerxes Yawn.webp"
image kwortixXerxyTesiYawn = "images/Kwortix Xerxes and tesipiz yawn.webp"
image yiwabisSleeping = "images/yiwatsyoh xerxTesi Sneaky Sleep.webp"
image templeSleeping = "images/Xerxes Sleeping in Temple Dorm Room.webp"

image shataSleepOver1 = "images/Shata Sleepover1.webp"
image shataSleepOver2 = "images/Shata Sleepover2.webp"

image takuraSleepOver1 = "images/Takura and Tesipiz Sleeping1.webp"
image takuraSleepOver2 = "images/Takura and Tesipiz Sleeping2.webp"
image tesipizInTakura = "images/Takura and Tesipiz Together.webp"
image takuriumAssult1 = "images/Takurium City Old Attacked.webp"
image astartVTarminians1 = "images/Astarts vs Tarminians1.webp"
image astartVTarminians2 = "images/Astarts vs Tarminians2.webp"

image gilgamoriumSleeps = "images/Gilgamorium Xerxes Bed Sleeping.webp"

image atossaBedXerxOnFloor = "images/Atossas Bedroom Xerxes and Atossa Sleeping.webp"
image atossaBedXerxWithAtossa = "images/Atossas Bedroom Xerxes and Atossa Same bed.webp"
image atossaBedXerxInAtossa = "images/Atossas Bedroom Xerxes Sleeping with Atossa.webp"
image atossaBedXerxInAtossa2 = "images/Atossas Bedroom Xerxes Sleeping with Atossa2.webp"
image atossaBedXerxReallyInAtossa = "images/Atossas Bedroom Xerxes Sleeping with Atossa3.webp"

image xerxBedXerx = "images/xerxes sleeping in his bed.webp"
image xerxBedWithAtossa = "images/xerxes sleeping in his bed and atossa.webp"
image xerxBedWithAtossa2 = "images/atossa covered sleeping on Xerxes in his bed.webp"
image xerxBedInAtossa = "images/atossa sleeping on Xerxes in his bed.webp"

image xerxSleepsNiitwanwa = "images/Niitwanwa Sleeps.webp"

image bardaiyaBedWithLakatinu = "images/Bardaiya and Lakatinu Cuddling.webp"

image bardaiyaVZyarya = "images/Bardaiya v Zyarya.webp"

image xerxVsAhriteZramaT2 = "images/Xerx vs T2 Ahrite Zrama Great Axe.webp"

image zaratVsZardonia = "images/Zardonians vs Zaratians.webp"
image tastsetuVsZardonians = "images/Zardonians vs ZaraTastsetu.webp"
image underwaterBattle1 = "images/Underwater battle.webp"
image gilgamoriumParty = "images/Gilgamorium Party.webp"
#skyboxes

image clearDayTime = "images/Location Accessories/Day Sky Plain.webp"
image starNightTime = "images/Location Accessories/Night Sky.webp"

image cloudyDayTime = "images/Location Accessories/Day sky clouds.webp"
image cloudyNightTime = "images/Location Accessories/Night Sky Cloudy.webp"
image rainySky = "images/Location Accessories/Cloud Skys.webp"

image blackBackground = "gui/game icons/blank.webp"
image ahriteSky = "images/Location Accessories/Ahrite Courrupted Sky.webp"

#textures 

image dustCloud = "images/dustcloud Textue.webp"
image sandTexture = Tile("images/Location Accessories/sand texture.webp")

#farground

image flatWater1 = "images/Location Accessories/Flat Water.webp"

#effects

image animeAngryRed = "images/angry cross red.webp"
image animeAngryOrange = "images/angry cross orange.webp"
image explosion = "images/Explosion.webp"
image smokes = "images/Smoke circle.webp"


#image ectabana0Compressy = "images/Battle of Ectabana0Compressy.webp"

#map icons

#special
image xMarxDaSpot = "images/Map X.webp"

#jamesiaIcons
image ectabanaIcon = "images/map icons/Ectabana Icon.webp"
image hikariCity = "images/map icons/Hikari.webp"
image seriniumIcon = "images/map icons/Serinium Zwotilya Icon.webp"
image kwotixMine = "images/map icons/Kworitx Mine Icon.webp"
image KwortixCity = "images/map icons/Kwortix Icon.webp"
image takuriumRuins = "images/map icons/Takurium Ruins Icon.webp"
image oldTakuriumCity1 = "images/map icons/Takurium Old Occupied Icon.webp"
image jamesianFortress = "images/map icons/jamesian fortress.webp"
image pashiCity = "images/map icons/Pashi.webp"
image kiridiumCity = "images/map icons/kiridium.webp"
image LandzeRuins = "images/map icons/Landze Ruins.webp"
image achemyeniznehTown = "images/map icons/Achemyenizneh.webp"
image oldTakuraTemple = "images/map icons/Old Takurium Temple.webp"
image nuidaCity = "images/map icons/Nuida.webp"
image templeOfAhuraMazdaIcon = "images/map icons/Temple of Ahura Mazda.webp"

#image jamesianTownClayWall
#image meinyashCity
#

#ZaratIcons
image zaratCamp = "images/map icons/Zaratian Camp.webp"
image zaratCampWalled = "images/map icons/Zaratian Camp Fortified.webp"
image mizheiumCity = "images/map icons/Mizheium.webp"
image zaradlyamCity = "images/map icons/Zaradlyam.webp"
image kyatrwaCity = "images/map icons/Kyatrwa.webp"
image chyarwaCity = "images/map icons/Chyarwa.webp"
image gilgamoriumCity1 = "images/map icons/Gilgamorium 1.webp"

#OxaIcons
image chiazhuCity = "images/map icons/Chiazhu.webp"
image meazhuCity = "images/map icons/Meazhu.webp"
image oxaFortress = "images/map icons/Oxa Fortress.webp"
image wizhuCity = "images/map icons/Wizhu Oxa City.webp"

#SsatuIcons
image yusidziuCity = "images/map icons/Yusidziu.webp"
image ssatuFortress = "images/map icons/ssatu fortress.webp"

#ZardoniaIcons
image miidosCity = "images/map icons/Miidos.webp"
image serdisCity = "images/map icons/Serdis.webp"
image artazaxaCity = "images/map icons/Artazaxa.webp"
image zwigaralya = "images/map icons/Zwigara.webp"
image zyoiumCity = "images/map icons/Zyoium.webp"
image nizaCity = "images/map icons/Niza.webp"
image azagaraCity = "images/map icons/Azagara.webp"
image kyuusholyaCity = "images/map icons/Kyuupsholya.webp"
image assiriaCity = "images/map icons/Assiria.webp"
image korkinFortress = "images/map icons/Korkin Fortress.webp"

#image junatuColony
#image spoodaweebs

#AstartIcons
    #Bardaiya's Realm
image balaAxeriumCity = "images/map icons/Bala-Axerium.webp"
#image balaAxeriumRuins
image hekuiumCity = "images/map icons/Hekuium.webp"
image kinosRuins = "images/map icons/kinos ruins.webp"
image makkabiumRuins1 = "images/map icons/Makkabium Ruins1.webp"
#image bardaiyaShahneh
#image bardaiyaShahnehFlooded 
    #Imperial Core
image sarrataCity = "images/map icons/Sarrata.webp"
image kiriniumCity = "images/map icons/Kirinium Ximdium.webp"
image nozzoriumCity = "images/map icons/Nozzorium and Nippo Regius.webp"
image kappaiumCity = "images/map icons/kappaium.webp"
image horoiumCity = "images/map icons/Horoium and Kaeshtartium.webp"
image astartesPalaceIcon = "images/map icons/Astartes Palace.webp"
image yusikta = "images/map icons/Yusikta Wodzyam.webp"
    #Ssayan
image woriumCity = "images/map icons/Worium.webp"
image lukitaCity = "images/map icons/Lukita.webp"
image rohmuCity = "images/map icons/Rohmu.webp"
image ordonianCity = "images/map icons/Ordonian Walled City.webp"
image koyuiumCity = "images/map icons/Koyuium.webp"
image toriiumCity = "images/map icons/toriium.webp"
    #Shared
image astartFortress = "images/map icons/astart Fortress.webp"
#AxeriaIcons
image xartabanaCity = "images/map icons/Xartabana.webp"
image axerianFort = "images/map icons/Axerian Fortress.webp"
#Ahrite Icons
#image ahrimanlyaRuins
#image mountAhrimanComplex
#image ahriteDesertHidout
image ahriteFotress = "images/map icons/Cultist Fortress.webp"
#image ahriman Shahneh
#image ahritePools
#image ahriteFactory



#locations

image achem = "images/Locations/Achemyenizneh Map.webp"
image astaport = "images/Locations/Astart Port - Sarrata.webp"
image astaJamesianBoarder = "images/Locations/Astarto-Jamesian Boarder.webp"
image astaJamesianBoarderModular = "images/Locations/Astarto-Jamesian Boarder No Sky.webp"
image astaJamesianBoarderNight = "images/Locations/Astarto-Jamesian Boarder Night.webp"
image jamesaAstartBoarder = "images/Locations/Astarto-Jamesian Boarder Facing Jamesia.webp"
image jamesaAstartBoarderNight = "images/Locations/Astarto-Jamesian Boarder Facing Jamesia Night.webp"
image desertRoad1 = "images/Locations/Desert Road 1.webp"
image desertRoad1Night = "images/Locations/Desert Road 1 Night.webp"
image desertRoad1Dusk = "images/Locations/Desert Road 1 Dusk.webp"
image forest1 = "images/Locations/Inside Forest1.webp"
image forestRepeatable = "images/Locations/Forest Repeatable.webp"
image forestOpening = "images/Locations/Into the Woods from grass.webp"
image forestSwamp = "images/Locations/Forest SWAMP.webp"
image forestTop = "images/Locations/Forest From Above Scolling Texture.webp"
image sandHoles = "images/Locations/Sandy Hole.webp"

image lakeBeach = "images/Locations/Lake Shoreline.webp"

#Ectabana Backgrounds

image lakeview = "images/Locations/Ectabana/Ectabana From Xerxes House.webp"
image lakeviewNight = "images/Locations/Ectabana/Ectabana From Xerxes House Night.webp"
image bigstump = "images/Locations/Ectabana/Xerxes House Outside Facing Towards.webp"
image bigstumpNight = "images/Locations/Ectabana/Xerxes House Outside Facing Towards Night.webp"

image bathhouseOut = "images/Locations/Ectabana/Ectabana Bathouse Outside.webp"
image missraOut = "images/Locations/Ectabana/Ectabana Missra Complex Outside.webp"
image missraOutNight = "images/Locations/Ectabana/Ectabana Missra Complex Outside Night.webp"

image ectabanaNorthEast1 = "images/Locations/Ectabana/Ectabana North East1.webp"
image ectabanaNorthEast1Night = "images/Locations/Ectabana/Ectabana North East1 Night.webp"
image ectabanaNorthEast2 = "images/Locations/Ectabana/Ectabana North East2.webp"
image ectabanaNorthEast2Night = "images/Locations/Ectabana/Ectabana North East2 Nights.webp"

image dariusDinner = "images/Locations/Ectabana/Ectabana Palace Dining Wall.webp"
image dariusDinnerDoor = "images/Locations/Ectabana/Ectabana Palace Dining Door.webp"
image dariusDinnerDoorMOAR = "images/Locations/Ectabana/Ectabana Palace Dining Door MOAR.webp"
image ectabanaPalaceOutNorth = "images/Locations/Ectabana/Ectabana Palace Outside North.webp"
image ectabanaPalaceOutNorthNight = "images/Locations/Ectabana/Ectabana Palace Outside North Night.webp"
image ectabanaPalaceGuarden = "images/Locations/Ectabana/Ectabana Palace Guarden.webp"
image ectabanaPalaceGuardenNight = "images/Locations/Ectabana/Ectabana Palace Guarden Night.webp"

image atossaBath = "images/Locations/Ectabana/Ectabana Palace Roof Pool.webp"
image atossaBed = "images/Locations/Ectabana/Atossas Bedroom Back.webp"
image atossaBedroom = "images/Locations/Ectabana/Atossas Bedroom.webp"
image atossaBedroomNight = "images/Locations/Ectabana/Atossas Bedroom Night.webp"

image rodentsAllywayEntrance = "images/Locations/Ectabana/Ectabana Rodents Allyway Outside.webp"
image rodentsAllywayEntranceNight = "images/Locations/Ectabana/Ectabana Rodents Allyway Outside Night.webp"
image rodentsAllywayIniside = "images/Locations/Ectabana/Rodents Alleyway Inside.webp"
image rodentsAllywayOutside = "images/Locations/Ectabana/Rodents Alleyway Inside Facing Outside.webp"
image rodentsAllyWayOutsideNight = "images/Locations/Ectabana/Rodents Alleyway Inside Facing Outside Night.webp"

image rodentsAllywayShopBackGround = "images/Locations/Ectabana/Ectabana Shop Cell.webp"
image rodentsAllywayShopForGround = "images/Locations/Ectabana/Ectabana Shop Cell Front.webp"
image rodentsAllywayCourtyardTile = Tile("images/Locations/Ectabana/Rodents Alleyway Courtyard.webp") 

image etcabanaStoneBench = "images/Locations/Ectabana/Ectabana Stone Bench.webp"
image etcabanaPalaceEntrance = "images/Locations/Ectabana/Outside Ectabana Palace Gate.webp"
image etcabanaPalaceEntranceNight = "images/Locations/Ectabana/Outside Ectabana Palace Gate Night.webp"

image etabanaWallsFromWall = "images/Locations/Ectabana/Ectabana Walls.webp"
image etabanaWallsTall = "images/Locations/Ectabana/Ectabana Walls elongated.webp"
image etabanaDesert = "images/Locations/Ectabana/Ectabana Outside Desert.webp"
image ectabanaDesertNoSky = "images/Locations/Ectabana/Ectabana Outside Desert No Sky.webp"
image ectabanaOutsideDesertFacingEctabana = "images/Locations/Ectabana/Ectabana Outside Desert Facing Ectabana.webp"
image ectabanaOutsideDesertFacingEctabanaNight = "images/Locations/Ectabana/Ectabana Outside Desert Facing Ectabana Night.webp"
image ectabanaGateClosed = "images/Locations/Ectabana/Ectabana Gate Closed.webp"
image ectabanaGateOpen = "images/Locations/Ectabana/Ectabana Gate Open.webp"
image ectabanaGateOpenNight = "images/Locations/Ectabana/Ectabana Gate Open Night.webp"
image ectabanaWallsOutside = "images/Locations/Ectabana/Ectabana Walls oustide facing inwards.webp"
image ectabanaEstablishingMorning = "images/Locations/Ectabana/Ectabana Establishing Morning.webp"
image ectabanaEstablishing = "images/Locations/Ectabana/Ectabana Establishing.webp"
image ectabanaEstablishingNight = "images/Locations/Ectabana/Ectabana Establishing Night.webp"


#xerxes' House
image xerxesHouseInisde = "images/Locations/Ectabana/Xerxes House Inside Face Inside.webp"
image xerxesHouseInisdeNight = "images/Locations/Ectabana/Xerxes House Inside Face Inside Night.webp"
image xerxesHouseInsideFacingOut = "images/Locations/Ectabana/Xerxes House Inside Face outside.webp"
image xerxesHouseInsideFacingOutNight = "images/Locations/Ectabana/Xerxes House Inside Face outside night.webp"
image xerxesBedWall = "images/Locations/Ectabana/xerxes bed Wall.webp"
image xerxesBed = "images/Locations/Ectabana/xerxes bed away.webp"





#Zwoti/Serinium
image zwotiKeyArenaBoss = "images/Locations/Serinium Zwotilya/Key arena.webp"

image zwotiKeyArenaBridge1 = "images/Locations/Serinium Zwotilya/Key arena bridge 1.webp"
image zwotiKeyArenaBridge2 = "images/Locations/Serinium Zwotilya/Key arena bridge 2.webp"
image zwotiKeyArenaBridge = "images/Locations/Serinium Zwotilya/Key arena bridge.webp"

image zwotiKeyArenaDoor = "images/Locations/Serinium Zwotilya/Key Arena facing door.webp"

image rockySnow = "images/Locations/Serinium Zwotilya/Rocky Snow.webp"
image rockySnowNighttime = "images/Locations/Serinium Zwotilya/Rocky Snow nightime.webp"
image seriniumMainStreet = "images/Locations/Serinium Zwotilya/Serinium Main Street.webp"
image seriniumMainStreetNight = "images/Locations/Serinium Zwotilya/Serinium Main Street Night time.webp"
image seriniumMarket = "images/Locations/Serinium Zwotilya/Serinium Market Zone.webp"
image seriniumMarketNight = "images/Locations/Serinium Zwotilya/Serinium Market Zone Night Time.webp"
image seriniumMountains = "images/Locations/Serinium Zwotilya/Serinium Mountains.webp"
image seriniumMountainsNightime = "images/Locations/Serinium Zwotilya/Serinium Mountains nighttime.webp"
image seriniumOutside = "images/Locations/Serinium Zwotilya/Serinium Ouside.webp"
image seriniumOutsideNightime = "images/Locations/Serinium Zwotilya/Serinium Ouside Night Time.webp"
image zwotiShop = "images/Locations/Serinium Zwotilya/Zwoti Shop.webp"

#Zwoti Shrine
image seriniumZwotiCaveStars = "images/Locations/Serinium Zwotilya/Zwoti Cave stars.webp"
image seriniumZwotiCaveStarsNighttime = "images/Locations/Serinium Zwotilya/Zwoti Cave stars nighttime.webp"

image zwotiArenaDoor = "images/Locations/Serinium Zwotilya/Zwoti Shrine Arena looking at door.webp"
image zwotiArenaDoorSpikesUp = "images/Locations/Serinium Zwotilya/Zwoti Shrine Arena looking at door spikes up.webp"
image zwotiArenaOut = "images/Locations/Serinium Zwotilya/Zwoti Shrine Arena looking at outside.webp"
image zwotiArenaOutSpike = "images/Locations/Serinium Zwotilya/Zwoti Shrine Arena looking at outside spikesz.webp"
image zwotiArenaOutNight = "images/Locations/Serinium Zwotilya/Zwoti Shrine Arena looking at outside nighttime.webp"
image zwotiArenaOutSpikeNight = "images/Locations/Serinium Zwotilya/Zwoti Shrine Arena looking at outside nighttime spikesz.webp"
image zwotiArenaBattleDoor = "images/Locations/Serinium Zwotilya/Zwoti Shrine Arena looking at door spikes up battle.webp"
image zwotiArenaBattleOut = "images/Locations/Serinium Zwotilya/Zwoti Shrine Arena looking at outside Battle.webp"
image zwotiArenaBattleOutNight = "images/Locations/Serinium Zwotilya/Zwoti Shrine Arena looking at outside Battle NightTime.webp"

image zwotiArenaFromDoor = "images/Locations/Serinium Zwotilya/Zwoti Shrine Door looking away from door.webp"
image zwotiArenaFromDoorNight = "images/Locations/Serinium Zwotilya/Zwoti Shrine Door looking away from door nighttime.webp"
image zwotiEntranceInside = "images/Locations/Serinium Zwotilya/Zwoti Shrine Enterance inside.webp"
image zwotiEntranceInsideNight = "images/Locations/Serinium Zwotilya/Zwoti Shrine Enterance inside nighttime.webp"
image zwotiEntrance = "images/Locations/Serinium Zwotilya/Zwoti Shrine Enterance outside.webp"
image zwotiEntranceNight = "images/Locations/Serinium Zwotilya/Zwoti Shrine Enterance outside nightime.webp"

image seriniumExpanedEntrance = "images/Locations/Serinium Zwotilya/Zwoti Shrine Enterance outside Expanded.webp"
image seriniumExpanedEntranceNight = "images/Locations/Serinium Zwotilya/Zwoti Shrine Enterance outside Expanded Night.webp"
image seriniumMountainsExpanded = "images/Locations/Serinium Zwotilya/Serinium Mountains Expanded.webp"
image seriniumMountainsExpandedNight = "images/Locations/Serinium Zwotilya/Serinium Mountains Expanded Night.webp"

image zwotiKeyArena = "images/Locations/Serinium Zwotilya/Zwoti Key approch.webp"
image zwotiKeyArenaBloody = "images/Locations/Serinium Zwotilya/Zwoti Key approch bloody.webp"
image zwotiLobbyStair = "images/Locations/Serinium Zwotilya/Zwoti motel lobby outside.webp"
image zwotiLobby = "images/Locations/Serinium Zwotilya/Zwoti Motel Lobby.webp"
image zwotiMotelOutside = "images/Locations/Serinium Zwotilya/Zwoti Motel Outside.webp"
image zwotiMotelOutsideNight = "images/Locations/Serinium Zwotilya/Zwoti Motel Outside nighttime.webp"
image zwotiMotelRoom = "images/Locations/Serinium Zwotilya/Zwoti Motel Room.webp"

#Kwortix Mine
    #outside
image kwortixMineFront = "images/Locations/Kwortix/Kwortix Mine Establishing.webp"
image kwortixMineFrontNight = "images/Locations/Kwortix/Kwortix Mine Establishing Night.webp"
image kwortixMineFrontDusk = "images/Locations/Kwortix/Kwortix Mine Establishing Dusk.webp"
image kwortixMineFrontMorning = "images/Locations/Kwortix/Kwortix Mine Establishing Morning.webp"
image kwortixMineFrontExplodingRocks = "images/Locations/Kwortix/Kwortix Mine Exploding Rocks.webp"
image kwortixMineFrontExplodingRocksNight = "images/Locations/Kwortix/Kwortix Mine Exploding Rocks Night.webp"
image kwortixMineFrontExplodingRocksDusk = "images/Locations/Kwortix/Kwortix Mine Exploding Rocks Dusk.webp"
image kwortixMineFrontExplodedRocks = "images/Locations/Kwortix/Kwortix Mine Exploded Rocks.webp"
image kwortixMineFrontExplodedRocksNight = "images/Locations/Kwortix/Kwortix Mine Exploded Rocks Night.webp"
image kwortixMineFrontExplodedRocksDusk = "images/Locations/Kwortix/Kwortix Mine Exploded Rocks Dusk.webp"
image kwortixMineFrontExplodedRocksMorning = "images/Locations/Kwortix/Kwortix Mine Exploded Rocks Morning.webp"
image KwortixMineFromFront = "images/Locations/Kwortix/Kwotix Mine From Front Door.webp"
image kwortixMineFromFrontNight = "images/Locations/Kwortix/Kwotix Mine From Front Door Nights.webp"
image kwortixMineFromFrontDusk = "images/Locations/Kwortix/Kwotix Mine From Front Door dusk.webp"
image kwortixBackdoor = "images/Locations/Kwortix/Kworitx Back Door.webp"
image kwortixMineFromBackDoor = "images/Locations/Kwortix/Kworitx Mine Outside From Backdoor.webp"
image kwortixMineFromBackDoorNight = "images/Locations/Kwortix/Kworitx Mine Outside From Backdoor Night.webp"
image kwortixMineFromBackDoorDusk = "images/Locations/Kwortix/Kworitx Mine Outside From Backdoor Dusk.webp"
image kwortixMineDesertTent = "images/Locations/Kwortix/Lakatinu Desert Tent.webp"

    #inside
        #Shata living quarters
image kwortixKitchen = "images/Locations/Kwortix/Kwortix mine kitchen.webp"
image kwortixKitchenDusk = "images/Locations/Kwortix/Kwortix mine kitchen dusk.webp"
image kwortixKitchenNight = "images/Locations/Kwortix/Kwortix mine kitchen night.webp"
image kwortixKitchenLight = "images/Locations/Kwortix/Kwortix mine kitchen used.webp"
image kwortixKitchenOutside = "images/Locations/Kwortix/Kwortix mine kitchen Door.webp"
image kwortixKitchenOutisdeNight = "images/Locations/Kwortix/Kwortix mine kitchen Door night.webp"
image kwortixKitchenOutsideDusk = "images/Locations/Kwortix/Kwortix mine kitchen Door dusk.webp"
image kwortixKitchenOutsideUsed = "images/Locations/Kwortix/Kwortix mine kitchen Door used.webp"
image kwortixKitchenOutsideUsedNight = "images/Locations/Kwortix/Kwortix mine kitchen Door used night.webp"
image kwortixKitchenOutsideUsedDusk = "images/Locations/Kwortix/Kwortix mine kitchen Door used dusk.webp"
image kwortixKicthenFight = "images/Locations/Kwortix/Kwortix mine kitchen used combat.webp"

image kwortixKaffateria = "images/Locations/Kwortix/Kwotix Mine Kaffateria.webp"
image kwortixKaffateriaOpen = "images/Locations/Kwortix/Kwotix Mine Kaffateria open door.webp"
image kwortixKaffateriaDark = "images/Locations/Kwortix/Kwotix Mine Kaffateria open door dusk.webp"
image kwortixKaffateriaNight = "images/Locations/Kwortix/Kwotix Mine Kaffateria open door night.webp"
image kwortixKaffateriaUsed = "images/Locations/Kwortix/Kwotix Mine Kaffateria used door closed.webp"
image kwortixKaffateriaUsedNight = "images/Locations/Kwortix/Kwotix Mine Kaffateria used night.webp"
image kwortixKaffateriaUsedDusk = "images/Locations/Kwortix/Kwotix Mine Kaffateria used.webp"
image kwortixKaffateriaUsedInside = "images/Locations/Kwortix/Kwortix kafateria Facing Living Quarters Used.webp"

image kwortixShataStreet = "images/Locations/Kwortix/Kwotix Shata Street.webp"
image kwortixShataStreetDed = "images/Locations/Kwortix/Kwortix Shata Street From Doggo Room Occupied Ded.webp"
image kwortixShataStreetStabby = "images/Locations/Kwortix/Kwortix Shata Street From Doggo Room Occupied Stabby.webp"
image kwortixShataStreetKey = "images/Locations/Kwortix/Kwortix Shata Street From Doggo Room Shata Leader.webp"
image kwortixShataStreetLeader = "images/Locations/Kwortix/Kwortix Shata Street From Doggo Room Shata Leader2.webp"
image kwortixShataStreetNight = "images/Locations/Kwortix/Kwotix Shata Street night.webp"
image kwortixShataStreetDusk = "images/Locations/Kwortix/Kwotix Shata Street dusk.webp"
image kwortixShataStreetUsed = "images/Locations/Kwortix/Kwotix Shata Street occupied.webp"
image kwortixShataStreetDoggo = "images/Locations/Kwortix/Kwortix Shata Street From Doggo Room.webp"
image kwortixShataStreetDoggoDusk = "images/Locations/Kwortix/Kwortix Shata Street From Doggo Room Dusk.webp"
image kwortixShataStreetDoggoNight = "images/Locations/Kwortix/Kwortix Shata Street From Doggo Room Night.webp"
image kwortixShataStreetDoggoUsed = "images/Locations/Kwortix/Kwortix Shata Street From Doggo Room Occupied.webp"

image kwortixDoggoRoom = "images/Locations/Kwortix/Kworitx Mine Doggo Room Light.webp"
image kwortixDoggoRoomDark = "images/Locations/Kwortix/Kworitx Mine Doggo Room.webp"
image kwortixDoggoPool = "images/Locations/Kwortix/Kworitx Mine Doggo Pool Light.webp"
image kwortixDoggoPoolDark = "images/Locations/Kwortix/Kworitx Mine Doggo Pool.webp"
image kwortixDoggoDoor = "images/Locations/Kwortix/Kwortix Mine Doggo Door Lights.webp"
    #shading means only need light and dark.
image kwortixDoggoDoorDark = "images/Locations/Kwortix/Kwortix Mine Doggo Door.webp"

image kwortixLivingHallSouth = "images/Locations/Kwortix/Kwortix Mine Living Hall South.webp"
image kwortixLivingHallSouthDusk = "images/Locations/Kwortix/Kwortix Mine Living Hall South dusk.webp"
image kwortixLivingHallSouthNight = "images/Locations/Kwortix/Kwortix Mine Living Hall South night.webp"
image kwortixLivingHallSouthUsed = "images/Locations/Kwortix/Kwortix Mine Living Hall South occupied.webp"
image kwortixLivingBench = "images/Locations/Kwortix/Kwotix Mine main bench.webp"
image kwortixLivingBenchDusk = "images/Locations/Kwortix/Kwotix Mine main bench dusk.webp"
image kwortixLivingBenchNight = "images/Locations/Kwortix/Kwotix Mine main bench night.webp"
image kwortixLivingBenchUsed = "images/Locations/Kwortix/Kwotix Mine main bench occupied.webp"
image kwortixLivingFighting = "images/Locations/Kwortix/Kwoti Mine Living Hall FIghting South.webp"
image kwortixLivingFightingDusk = "images/Locations/Kwortix/Kwoti Mine Living Hall FIghting South dusk.webp"
image kwortixLivingFightingNight = "images/Locations/Kwortix/Kwoti Mine Living Hall FIghting South Night.webp"
image kwortixLivingFightingUsed = "images/Locations/Kwortix/Kwoti Mine Living Hall FIghting South Occupied.webp"
image kwortixLivingFightingChwitaza = "images/Locations/Kwortix/Kwoti Mine Living Hall FIghting South Occupied Chwitaza.webp"
image kwortixLivingFightingDark = "images/Locations/Kwortix/Kwoti Mine Living Hall FIghting South Dark.webp"
image kwortixLivingNorth = "images/Locations/Kwortix/Kwortix Living Hall Center Facing Kafateria.webp"
image kwortixLivingNorthDusk = "images/Locations/Kwortix/Kwortix Living Hall Center Facing Kafateria dusk.webp"
image kwortixLivingNorthNight = "images/Locations/Kwortix/Kwortix Living Hall Center Facing Kafateria night.webp"
image kwortixLivingNorthUsed = "images/Locations/Kwortix/Kwortix Living Hall Center Facing Kafateria occupied.webp"
        #Mining Zone
image kwortixFlameRoom = "images/Locations/Kwortix/Kwotix Mine Flame Room.webp"
image kwortixFlameAway = "images/Locations/Kwortix/Kwotix Flame Room Away from flame.webp"
image kwortixMainPool = "images/Locations/Kwortix/Kwortix Mine Main Pool From Modonon Room.webp"
image kwortixMainPoolLight = "images/Locations/Kwortix/Kwortix Mine Main Pool From fire room.webp"
image kwortixMainPoolDark = "images/Locations/Kwortix/Kwortix Mine Main Pool From fire room early.webp"
image kwortixMainPoolFromModonon = "images/Locations/Kwortix/Kwortix Mine Main Pool From Modonon Room.webp"
image kwortixMainPoolFromDoggo = "images/Locations/Kwortix/Kwortix Mine Main Pool From Doggo room.webp"
image waterCollectionZone = "images/Locations/Kwortix/Kworitx Mine main room Water.webp"

image modononDoorImg = "images/Locations/Kwortix/Kworitx Mine main room Modonon Door.webp"
image modononFromDoor = "images/Locations/Kwortix/Kwortix Modonon From Door.webp"
image modononFromDoorDusk = "images/Locations/Kwortix/Kwortix Modonon From Door dusk.webp"
image modononFromDoorNight = "images/Locations/Kwortix/Kwortix Modonon From Door night.webp"
image kwortixModononIntro = "images/Locations/Kwortix/Kwortix Modonon Establishing.webp"
image kwortixModononIntroDusk = "images/Locations/Kwortix/Kwortix Modonon Establishing dusk.webp"
image kwortixModononIntroNight = "images/Locations/Kwortix/Kwortix Modonon Establishing night.webp"
image kwortixModononNorth = "images/Locations/Kwortix/Kwortix Modonon Facing North.webp"
image kwortixModononNorthDusk = "images/Locations/Kwortix/Kwortix Modonon Facing North Dusk.webp"
image kwortixModononNorthNight = "images/Locations/Kwortix/Kwortix Modonon Facing North Night.webp"
image kwortixModononNorthDuskBloody = "images/Locations/Kwortix/Kwortix Modonon Facing North Meaty Dusk.webp"
image kwortixModononNorthNightBloody = "images/Locations/Kwortix/Kwortix Modonon Facing North Meaty Night.webp"
image kwortixModononNorthBloody = "images/Locations/Kwortix/Kwortix Modonon Facing North Meaty.webp"
image kwortixModononSouth = "images/Locations/Kwortix/Kwortix Modonon Facing South.webp"
image kwortixModononSouthBloody = "images/Locations/Kwortix/Kwortix Modonon Facing South Bloody.webp"
image kwortixModononSouthDusk = "images/Locations/Kwortix/Kwortix Modonon Facing South dusk.webp"
image kwortixModononSouthDuskBloody = "images/Locations/Kwortix/Kwortix Modonon Facing South Bloody Dusk.webp"
image kwortixModononSouthNight = "images/Locations/Kwortix/Kwortix Modonon Facing South Night.webp"
image kwortixModononSouthNightBloody = "images/Locations/Kwortix/Kwortix Modonon Facing South Bloody Nights.webp"
image kwortixModononSide = "images/Locations/Kwortix/Kwortix Modonon Side.webp"
image kwortixModononSideBloody = "images/Locations/Kwortix/Kwortix Modonon Side Meaty.webp"
image kwortixModononSideDusk = "images/Locations/Kwortix/Kwortix Modonon Side Dusk.webp"
image kwortixModononSideDuskBloody = "images/Locations/Kwortix/Kwortix Modonon Side Meaty dusk.webp"
image kwortixModononSideNight = "images/Locations/Kwortix/Kwortix Modonon Side Night.webp"
image kwortixModononSideNightBloody = "images/Locations/Kwortix/Kwortix Modonon Side Meaty Night.webp"

#Kworix City
image kwortixCity = "images/Locations/Kwortix/Kworitx City Establishing.webp"
image kwortixCityNight = "images/Locations/Kwortix/Kworitx City Establishing Night.webp"
image kwortixCityDusk = "images/Locations/Kwortix/Kworitx City Establishing dusk.webp"
image kwortixSquare = "images/Locations/Kwortix/Kworitx City Square.webp"
image kwortixSquareNight = "images/Locations/Kwortix/Kworitx City Square night.webp"
image kwortixSquareDusk = "images/Locations/Kwortix/Kworitx City Square dusk.webp"
image kwortixTreeStreet = "images/Locations/Kwortix/Kworitx City Tree Street South.webp"
image kwortixTreeStreetNight = "images/Locations/Kwortix/Kworitx City Tree Street South Night.webp"
image kwortixTreeStreetDusk = "images/Locations/Kwortix/Kworitx City Tree Street South Dusk.webp"
image kwortixMotel = "images/Locations/Kwortix/Kwortix Motel Lobby.webp"
image kwortixMotelNight = "images/Locations/Kwortix/Kwortix Motel Lobby night.webp"
image kwortixMotelDusk = "images/Locations/Kwortix/Kwortix Motel Lobby dusk.webp"
image kwortixMotelDoor = "images/Locations/Kwortix/Kwortix Lobby Facing Door.webp"
image kwortixShop = "images/Locations/Kwortix/Kworitx Shop.webp"

#Takuria Area

image forestVillageFront = "images/Locations/Takurium/Forest Village1.webp"
image forestVillageFrontNight = "images/Locations/Takurium/Forest Village1 Night.webp"
image forestVillageBack = "images/Locations/Takurium/Forest Village2.webp"
image forestVillageBackNight = "images/Locations/Takurium/Forest Village2 Night.webp"
image foresVillageHouse = "images/Locations/Takurium/Forest Village House.webp"
image foresVillageHouseNight = "images/Locations/Takurium/Forest Village House Night.webp"
image forestVillageStables = "images/Locations/Takurium/Forest Stable.webp"

image forestShop = "images/Locations/Takurium/Forest Shop.webp"

image forestLobby = "images/Locations/Takurium/Forest Village Mess Hall Hotel.webp"
image forestLobbyDoor = "images/Locations/Takurium/Forest Village Mess Hall Lobby.webp"

image niitwanwaEstablishing = "images/Locations/Niitwanwa/Niitwanwa Establishing foz.webp"
image niitwanwaEstablishingNight = "images/Locations/Niitwanwa/Niitwanwa Establishing foz Night.webp"
image niitwanwaOutsideGate = "images/Locations/Niitwanwa/Niitwanwa Outside Gate.webp"
image niitwanwaOutside = "images/Locations/Niitwanwa/Niitwanwa Outside Gate Facing Out.webp"
image niitwanwaOutsideNight = "images/Locations/Niitwanwa/Niitwanwa Outside Gate Facing Out Night.webp"
image niitwanwaOutsideDock = "images/Locations/Niitwanwa/Niitwanwa court and docks.webp"
image niitwanwaInside = "images/Locations/Niitwanwa/Niitwanwa inside.webp"
image niitwanwaCortDock = "images/Locations/Niitwanwa/Niitwanwa court and docks.webp"
image niitwanwaPlatform = "images/Locations/Niitwanwa/Niitwanwa Platform.webp"

image lakeTakuraShore = "images/Locations/Takurium/Take Takura Shoreline.webp"
image oldWallFacingWall = "images/Locations/Takurium/Old Wall South.webp"
image oldWallAwayFromWall = "images/Locations/Takurium/Old Wall south from wall.webp"
image takuraRoadBend = "images/Locations/Takurium/Takurium road Bend.webp"

image yemehEstablishing = "images/Locations/Yemeh/Yemeh Establishing.webp"

#Takurium
image takuriumEstablishing = "images/Locations/Takurium/Takurium City Establshing 1.webp"
image takuriumEstablishingSutsshak = "images/Locations/Takurium/Takurium City Establshing 1 Sutsshak night.webp"
image takuriumEstablishingGame = "images/Locations/Takurium/Takurium City Establshing 1 Game Night.webp"

image takruriumSouthGate = "images/Locations/Takurium/Takurium South Wall Facing In.webp"
image takuriumEntrance1 = "images/Locations/Takurium/Takurium South Entrace Facing In.webp"
image takuriumEntranceGameNight = "images/Locations/Takurium/Takurium South Entrace Facing In Game night.webp"
image takuriumEntraceSutsshakNight = "images/Locations/Takurium/Takurium South Entrace Facing In Sutsshak Night.webp"
image takuriumEntraceAhrites = "images/Locations/Takurium/Takurium South Entrace Facing In Ahrite Uprising.webp"
image takuriumEntranceSouth = "images/Locations/Takurium/Takurium South Entrance.webp"
image takurium2TheSouth = "images/Locations/Takurium/Takurium to South.webp"
image takuriumHyengshinStreet = "images/Locations/Takurium/Hyengshin Street East.webp"
image takuriumHyengshinStreetLights = "images/Locations/Takurium/Hyengshin Street East Sutsshak Night.webp"
image takuriumSutsshakNorth = "images/Locations/Takurium/Sutsshak Road East.webp"
image takuriumSutsshakNorthLights = "images/Locations/Takurium/Sutsshak Road East Sutsshak night.webp"
image takuriumSutsshakSouth = "images/Locations/Takurium/Hyengshin Street West.webp"
image takuriumSutsshakSouthLights = "images/Locations/Takurium/Hyengshin Street West Sutsshak Night.webp"
image takuriumSutsshakSouthGameLights = "images/Locations/Takurium/Hyengshin Street West Game Night.webp"
image takuriumInsideSutsshakEast = "images/Locations/Takurium/Inside Sutsshak Temple Face East.webp"
image takuriumInsideSutsshakEastLights = "images/Locations/Takurium/Inside Sutsshak Temple Face East Lights.webp"
image takuriumInisdeSutsshakWest = "images/Locations/Takurium/Inside Sutsshak Temple Face West.webp"
image takuriumInsideSutsshakWestLights = "images/Locations/Takurium/Inside Sutsshak Temple Face West Light.webp"
image takuriumDaHill = "images/Locations/Takurium/Sutsshak Road West.webp"
image takuriumDaHillLights = "images/Locations/Takurium/Sutsshak Road West Sutsshak Night.webp"
image takuriumDaHillGame = "images/Locations/Takurium/Sutsshak Road West Game Night.webp"
image takuriumDaHillOld = "images/Locations/Takurium/Sutsshak Road West Takura Temple.webp"
image takuriumDaHillAstarte = "images/Locations/Takurium/Sutsshak Road West Astarte Temple.webp"
image takuriumDocks = "images/Locations/Takurium/Takurium Docks.webp"
image takuriumDocksLights = "images/Locations/Takurium/Takurium Docks Sutsshak Night.webp"
image takuriumGround0 = "images/Locations/Takurium/Ground Zero.webp"
image takuriumGround0Night = "images/Locations/Takurium/Ground Zero Night.webp"
image takuriumGround0Light = "images/Locations/Takurium/Ground Zero Sutsshak Night.webp"
image takuriumMainStreet = "images/Locations/Takurium/Takurium Main Road from Docks.webp"
image takuriumMainStreetSutsshak = "images/Locations/Takurium/Takurium Main Road from Docks Sutsshak Night.webp"
image takuriumMainStreetGame = "images/Locations/Takurium/Takurium Main Road from Docks Game night.webp"

    #Old Temple Hill
image takuriumOldTempleSouth = "images/Locations/Takurium/Takurium Old Temple Hill South.webp"
image takuriumOldTempleWest = "images/Locations/Takurium/Takurium Old Temple Hill West.webp"
image takuriumOldTempleNorth = "images/Locations/Takurium/Takurium Old Temple Hill North.webp"
image takuriumOldTempleNorthGame = "images/Locations/Takurium/Takurium Old Temple Hill North Game Night.webp"
image takuriumOldTempleEast = "images/Locations/Takurium/Takurium Old Temple Hill East.webp"
image takuriumOldTempleEastLights = "images/Locations/Takurium/Takurium Old Temple Hill East Sutsshak Night.webp"
image takuriumOutOfArena = "images/Locations/Takurium/Takura Arena Out Door Looking Away.webp"
    #Takura's Palace
image takurasRoom = "images/Locations/Takurium/Takura s Room Facing Benches.webp"
image takurasRoomBLocked = "images/Locations/Takurium/Takura s Room Facing Door Blocked Off.webp"
image takurasSpooderHallway = "images/Locations/Takurium/Takurium Spooder Hallway.webp"
image takurasPalaceCenter = "images/Locations/Takurium/Takurium Palace Center Room.webp"
image takurasPalaceCenterAway = "images/Locations/Takurium/Takurium Palace Center Room From North.webp"
    #Battle Arena
image takuriumArenaEstablishingSouth = "images/Locations/Takurium/Takurium Arena South Establishing.webp"
image takuriumArenaEstablishingSouthLights = "images/Locations/Takurium/Takurium Arena South Establishing Game Night.webp"
image takuriumArenaEstablishingEast = "images/Locations/Takurium/Takurium Arena East Establishing.webp"
image takuriumArenaEstablishingEastLights = "images/Locations/Takurium/Takurium Arena East Establishing Game Night.webp"
image takuriumArenaEstablishingNorth = "images/Locations/Takurium/Takurium Arena North Establishing.webp"
image takuriumArenaEstablishingNorthLights = "images/Locations/Takurium/Takurium Arena North Establishing Game Night.webp"
image takuriumOutDoor = "images/Locations/Takurium/Takurium Arena North Establishing Game Night.webp"
image takuriumNorthDoor = "images/Locations/Takurium/Takurium Arena North Door.webp"
image takuriumNorthDoorLights = "images/Locations/Takurium/Takurium Arena North Door Game Night.webp"
image takuriumSouthDoor = "images/Locations/Takurium/Takurium Arena South Door.webp"
image takuriumSouthDoorLights = "images/Locations/Takurium/Takurium Arena South Door Game Night.webp"
image takuriumArenaSandNorth = "images/Locations/Takurium/In Takurium Arena North.webp"
image takuriumArenaSandNorthLights = "images/Locations/Takurium/In Takurium Arena North Game Night.webp"
image takuriumArenaSandSouth = "images/Locations/Takurium/In Takurium Arena South.webp"
image takuriumArenaSandSouthLights = "images/Locations/Takurium/In Takurium Arena South Game Night.webp"
image takuriumArenaStairs2 = "images/Locations/Takurium/Stairway to GAME NIGHT.webp"
image takuriumArenaStairsAway = "images/Locations/Takurium/Stairway 2 HELL.webp"
image takuriumArenaBox = "images/Locations/Takurium/Krokkosnek Obsevation Box.webp"
image takuriumArenaBoxLights = "images/Locations/Takurium/Krokkosnek Obsevation Box Game Night.webp"
image takuriumArenaBoxDoor = "images/Locations/Takurium/Krokkosnek Obsevation Box Door.webp"

image takuriumEastDoor = "images/Locations/Takurium/Takurium Arena East Door.webp"
image takuriumEastDoorLights = "images/Locations/Takurium/Takurium Arena East Door Game Night.webp"

image whiteWallBrownWoodenDoor = "images/Locations/Takurium/Takurium Arena Out Door.webp"
image whiteWallBrownWoodenDoorOpen = "images/Locations/Takurium/Takurium Arena Out Door Open.webp"

#Zarat
    #Yimia
image yimiaGrassy = "images/Locations/Zarato-Jameisan Boarder Facing Zarat.webp"
image yimiaDeserty = "images/Locations/Zarato-Jameisan Boarder Facing Jamesia.webp"
image yimiaRoadCampEast = "images/Locations/Gilgamorium/yimi ri-in camp.webp"
image yimiaRoadCampNorth = "images/Locations/Gilgamorium/Fwimgyoka road rural.webp"
image chuwosWagonInside = "images/Locations/Chuwos Wagon Inside.webp"

    #Gilgamorium
image eastGate = "images/Locations/Gilgamorium/East Gate outside.webp"
image eastGateInside = "images/Locations/Gilgamorium/East Gate Inisde.webp"
image eastGateStreet = "images/Locations/Gilgamorium/East Gate Street.webp"
image fountainStreet = "images/Locations/Gilgamorium/Fountain Street.webp"
image fwimgyokaRoadWest = "images/Locations/Gilgamorium/Fwimgyoka road facing West.webp"
image fwimgyokaRoadWeatZaratNight = "images/Locations/Gilgamorium/Fwimgyoka road facing West Zaratians Nights.webp"
image fwimgyokaRaoadWestZarat = Composite( ( 7200 , 1620 ),(0,0),"images/Locations/Gilgamorium/Fwimgyoka road facing West.webp",(0,0),"images/Locations/Gilgamorium/Fwimgyoka road facing West Zaratians.webp")
image gilgamoriumFromLake = "images/Locations/Gilgamorium/Gilgamorium from Lake.webp"
image gilgamoriumPalaceDockNorth = "images/Locations/Gilgamorium/Gilgamorium Palace Docks North Face.webp"
image gilgamoriumPalaceDockSouth = "images/Locations/Gilgamorium/Gilgamorium Palace Docks South Face.webp"
image gilgamoriumPartyRoom = "images/Locations/Gilgamorium/Gilgamorium Rebel Establishing Night.webp"
image gilgamoriumRebelDay = "images/Locations/Gilgamorium/Gilgamorium Rebel Establishing.webp"
image gilgamoriumRebelNight = "images/Locations/Gilgamorium/Gilgamorium Rebel Establishing Night.webp"
image gilgamoriumZaratDay = "images/Locations/Gilgamorium/Gilgamorium Zarat Establishing.webp"
image gilgamoriumZaratNight = "images/Locations/Gilgamorium/Gilgamorium Zarat Establishing Night.webp"
image gilgamoriumShop = "images/Locations/Gilgamorium/Gilgamorium Shop.webp"
image gilgamoriumShore = "images/Locations/Gilgamorium/Gilgamorium Shoreline.webp"
image gilgamoriumBed = "images/Locations/Gilgamorium/Gilgamorium Xerxes Bed.webp"
image gilgamoriumBedAway = "images/Locations/Gilgamorium/Gilgamorium Xerxes Bedroom.webp"
image gilgamoriumPartyRoom = "images/Locations/Gilgamorium/Gilgamorium party room.webp"
image northGateIn = "images/Locations/Gilgamorium/North Gate Inisde.webp"
image northGateOut = "images/Locations/Gilgamorium/North Gate OUTsde.webp"
image northGateStreet = "images/Locations/Gilgamorium/North Gate Street.webp"
image yimiataStreet = "images/Locations/Gilgamorium/Yimiata Street.webp"
image fwimgyokaRoadFromNortGate = "images/Locations/Gilgamorium/Fwimgyoka road From Gate Outside.webp"
image missraiumRoadFromEastGate =  "images/Locations/Gilgamorium/Road2Missraium.webp"

#Ahrite Zones
image ahriteCave = "images/Locations/Ahrite Bases/ahrite cave.webp"
image ahriteBaseCenter = "images/Locations/Ahrite Bases/Ahrite Base Hub.webp"
image ahriteLair4 = "images/Locations/Ahrite Bases/Ahrimaniom mk4 Lair Entrance.webp"
image ahriteLair4Now = "images/Locations/Ahrite bases/Ahrimaniom mk4 Lair Flooded Ruin.webp"
image ahriteRoom = "images/Locations/Ahrite Bases/Ahrite Base Room.webp"
image ahriteWastland = "images/Locations/Ahrite Bases/Ahrite Wasterland FlahsBack.webp"

#Astart Zone

#Bardaiya Shahneh
image bardaiyaBedRoom = "images/Locations/Bardaiya Shahneh/Bardaiya's Room.webp"
image bardaiyaBed = "images/Locations/Bardaiya Shahneh/Bardaiya's Room Away.webp"
image bardaiyaBedNoLight = "images/Locations/Bardaiya Shahneh/Bardaiya's Room Away Neutral Lights.webp"
image bardaiyaLivingSeats = "images/Locations/Bardaiya Shahneh/Bardaiya Living Room Sitting.webp"
image bardaiyaProjectionScreen = "images/Locations/Bardaiya Shahneh/Bardaiya Living Room Projection Screen.webp"

#Bala-Axerium
image balatiusThroneRoom = "images/Locations/Bala-Axerium/Balatius Palace Throne Arena.webp"

#Aratashium
image aratashiumFrontEntrance = "images/Locations/Aratashium/Aratashium Front.webp"
image aratashiumPool = "images/Locations/Aratashium/Aratashium Pool.webp"
image aratashiumBeds = "images/Locations/Aratashium/Adgilias Room.webp"


#Kiridium
image keioziaHouse = "images/Locations/Kiridium/Kiridium Villa.webp"
image keioziaRoom = "images/Locations/Kiridium/Keiozias Room.webp"


#Temple of Ahura-Mazda
image templeOfAhuraMazdaEstb = "images/Locations/Temple of Ahura-Mazda/Temple of Ahura-Mazda Establishing Day.webp"
image templeOfAhuraMazdaEstbNight = "images/Locations/Temple of Ahura-Mazda/Temple of Ahura-Mazda Establishing.webp"
image templeOfAhuraMazdaNoDudes = "images/Locations/Temple of Ahura-Mazda/Temple of Ahura-Mazda Establishing No Dudes.webp"
image templeOfAhuraMazdaOutside = "images/Locations/Temple of Ahura-Mazda/Temple of Ahura-Mazda Entrance Out.webp"
image templeOfAhuraMazdaOutsideNight = "images/Locations/Temple of Ahura-Mazda/Temple of Ahura-Mazda Entrance Out Night.webp"
image templeOfAhuraMazdaFoodRoom = Tile("images/Locations/Temple of Ahura-Mazda/Temple of Ahura-Mazda Caffatria Wall.webp")
image templeOfAhuraMazdaHallWay = "images/Locations/Temple of Ahura-Mazda/Temple of Ahura-Mazda Upper Hallway.webp"
image templeOfAhuraMazdaChamberHall = "images/Locations/Temple of Ahura-Mazda/Temple of Ahura-Mazda Lower Hallway.webp"
image templeOfAhuraMazdaChamberDoor = "images/Locations/Temple of Ahura-Mazda/Temple of Ahura-Mazda Chamber Door.webp"
image templeOfAhuraMazdaGate = "images/Locations/Temple of Ahura-Mazda/Temple of Ahura-Mazda Entrance Inside Gate.webp"
image swordChamberLedge = "images/Locations/Temple of Ahura-Mazda/Chamber Interior From Wall.webp"
image swordChamberRoom = "images/Locations/Temple of Ahura-Mazda/Chamber Interior.webp"
image templeDormRoom = "images/Locations/Temple of Ahura-Mazda/Temple Dorm Room.webp"

#azagara
image azagaraWilds = "images/Locations/Azagara Wilds.webp"

#pegBoardGame
image boardGame = "images/Location Accessories/Game Board Empty.webp"
image stick1aBlue = "images/Location Accessories/game stick in 1a.webp"
image stick2bBlue = "images/Location Accessories/game stick in 2b.webp"

#Background Asserories
image tubeTentacles = Tile("images/Location Accessories/tubes.webp")
image transformationTube = "images/Location Accessories/transformation tube.webp"
image transformationTubeGlass = "images/Location Accessories/transformation tube glass.webp"
image transformationTubeGiant = "images/Location Accessories/transformation ahrite giant.webp"
image transformationTubeNiom = "images/Location Accessories/transformation tube niom.webp"
image transformationTubeMerDeamon = "images/Location Accessories/mer-deamon midTransform.webp"

image bushRound = "images/Location Accessories/Bush Round.webp"
image bushBushy = "images/Location Accessories/Bush Bushy.webp"

image swordDoorBottomOut =  "images/Location Accessories/SoAM Door Out Bottom.webp"
image swordDoorLeftOut = "images/Location Accessories/SoAM Door Out Top Left.webp"
image swordDoorRightOut = "images/Location Accessories/SoAM Door Out Top Right.webp"

image swordDoorTopIn = "images/Location Accessories/SoAM Door In Top.webp"
image swordDoorTopBottom ="images/Location Accessories/SoAM Door In Bottom.webp"
image swordDoorHub = "images/Location Accessories/SoAM Door In Hub.webp"
image swordDoorinWhole = "images/Location Accessories/SoAM Door In.webp"


image blueColumnRedBase = "images/Location Accessories/Collumn.webp"
image longRoyalTable = "images/Location Accessories/Royal Table from Table.webp"
image shortRoyalTable = "images/Location Accessories/Royal Litte-End Table from Table.webp"
image bronzeTable = "images/Location Accessories/Table Bronze.webp"
image bronzeFigureTable = "images/Location Accessories/Table Bronze With Copper Figurines.webp"
image wallBarrier = "images/Location Accessories/Wall Fence Section Ectabana.webp"
image zwotiDoorFrame = "images/Location Accessories/Zwoti Door Frame.webp"
image zwotiMotelCounter = "images/Location Accessories/Zwoti Motel Counter.webp"
image zwotiRock = "images/Location Accessories/Zwoti Rock.webp"
image zwotiRockNighttime = "images/Location Accessories/Zwoti Rock nighttime.webp"
image zwotiDoor = "images/Location Accessories/Zwoti side up door.webp"
image bloodyPlatform = "images/Location Accessories/platform bloody.webp"
image platform = "images/Location Accessories/platform.webp"
image platformWithDoor = "images/Location Accessories/platform2.webp"
image platformWithBend = "images/Location Accessories/platfrom 3.webp"
image roomButton = "images/Location Accessories/room button red.webp"
image shopCounter = "images/Location Accessories/Shop Counter.webp"
image shopCounter2 = "images/Location Accessories/Shop Counter 2.webp"
image kwortixBackdoorIcon = "images/Location Accessories/Kwortix Mine Backgroor.webp"
image kwortixBackdoorIconDusk = "images/Location Accessories/Kwortix Mine Backgroor Dusk.webp"
image kwortixRocks = "images/Location Accessories/Kwortix Mine Entrance Rocks.webp"
image kwortixRocksDisk = "images/Location Accessories/Kwortix Mine Entrance Rocks dusk.webp"
image kwortixMotelBench = "images/Location Accessories/Kwortix Motel Lobby Bench.webp"
image kwortixShataStreetDoor = "images/Location Accessories/Kwotix Shata Street door.webp"
image kwortixShataStreetDoorLights = "images/Location Accessories/Kwotix Shata Street door lights.webp"
image kwortixShataStreetDoggoDoor = "images/Location Accessories/Shata Street Door Doggo Room.webp"
image kwortixShataStreetDoggoDoorDark = "images/Location Accessories/Shata Street Door Doggo Room lights.webp"

image communicationBallTower = "images/Location Accessories/Comunications Crystal 1.webp"
image communicationBallTowerActive = "images/Location Accessories/Comunications Crystal 1 Activated.webp"
image communicationsBall = "images/items/Comunication Crystal2.webp"
image communicationsBallActive = "images/items/Comunication Crystal2 Active.webp"

image forestMessHallCounter = "images/Location Accessories/Forest Mess Hall Counter.webp" 

image sutsshakIdol = "images/Location Accessories/Sutsshak Front.webp"
image sutsshakIdolButt = "images/Location Accessories/Sutsshak Back.webp"
image astarteStatueIcon = "images/Location Accessories/Takurium City Establshing 1 Astarte's Statue.webp"
image wholeAssTable = "images/Location Accessories/Whole Table.webp"
image oldTempleHillFront = "images/Location Accessories/Sutsshak Road West MidGround.webp"
image oldRedCeelingVent = "images/Location Accessories/Red Vent Ceeling.webp"
image sandStatueBase = "images/Location Accessories/Sand Statute Base.webp"
image woodenBoard = "images/Location Accessories/Board No Nails.webp"
image blackNailHead = "images/Location Accessories/Black Nail.webp"
image insenseBurnerBox = "images/Location Accessories/Insense Burn Box.webp"
image centerBalcony = "images/Location Accessories/Takurium Palace Balcany From South.webp"
image foreGroundBalcony = "images/Location Accessories/Takurium Palace Center Room From North Balcony.webp"

image astarteStatue = "images/antagonists/Astarte/Astarte Statute.webp"

image purpleBrick = "images/Location Accessories/Purple Brick.webp"
image foodCart = "images/Location Accessories/Food Serving Cart Royal.webp"

image fryingPan = "images/Location Accessories/frying pan.webp"
image flamingHolesXerxFromFront = "images/Location Accessories/flaming holes.webp"

image gateDoorClosed = "images/Location Accessories/gate door.webp"
image gateDoorOpenIn = "images/Location Accessories/gate door Open2.webp"
image gateDoorOpenOut = "images/Location Accessories/gate door Open.webp"
image meatlBar = "images/Location Accessories/Metal Holding Bar.webp"

image flameCutHorizontal = "images/Location Accessories/SoAM Horizontal Cut.webp"
image flameCutVertical = "images/Location Accessories/SoAM Vertical cut.webp"
image woodCutout = "images/Location Accessories/Wood Cutout.webp"
image flame = "images/flame.webp"

image barrel = "images/Location Accessories/Barrel.webp"
image ironSpikes = "images/Location Accessories/Iron spikes.webp"

image ssatuBoxSmall = "images/Location Accessories/Little Ssatu Box.webp"

image gilgaBlanketOverlay = "images/Location Accessories/GilgaBedBlanket Overlay.webp"

#I'm on a boat
image zardonianBoatDeck = "images/Locations/Zardonian Boat Deck.webp"
image zardonianBoatCabin = "images/Locations/Zardonian Boat Captains Box.webp"
#image astartBoatDeck
#image astartBoatCabin

#dinner time
image cupTesi = "images/Location Accessories/cup Tesipiz.webp"
image cupVolk = "images/Location Accessories/cup Volkara.webp"
image cupAto = "images/Location Accessories/cup Atossa.webp"
image cupXerx = "images/Location Accessories/cup Xerxes.webp"
image cupGold = "images/Location Accessories/Goblet.webp"
image teaPot = "images/Location Accessories/hot fuild pot.webp"
image longJar = "images/Location Accessories/long jar.webp"

#plates
image plateGoldT = "images/Location Accessories/plate circle Tesipiz.webp"
image plateGoldX = "images/Location Accessories/plate circle Xerxes.webp"
image plateGoldV = "images/Location Accessories/plate circle Volkara.webp"
image plateGOldA = "images/Location Accessories/plate circle Atossa.webp"
image plateGoldD = "images/Location Accessories/plate circle Darius.webp"

image plateT = "images/Location Accessories/plate circle Tesipiz Clay.webp"
image plateD = "images/Location Accessories/plate circle Darius Clay.webp"
image plateX = "images/Location Accessories/plate circle Xerxes Clay.webp"
image plateV = "images/Location Accessories/plate circle Volkara clay.webp"
image plateA = "images/Location Accessories/plate circle Atossa Clay.webp"

image plateTanT = "images/Location Accessories/plate circle Tesipiz tan Clay.webp"
image plateTanA = "images/Location Accessories/plate circle Atossa Tan Clay.webp"
image plateTanD = "images/Location Accessories/plate circle Darius Tan Clay.webp"
image plateTanV = "images/Location Accessories/plate circle Volkara Tan clay.webp"
image plateTanX = "images/Location Accessories/plate circle Xerxes Tan Clay.webp"

image plateSquareB = "images/Location Accessories/plate square Bardaiya.webp"
image plateSquareL = "images/Location Accessories/plate square Lakatinu.webp"

#figurines and dolls
image dariusFigue = "images/Location Accessories/Darius Figurerine.webp"
image tazarannoFigue = "images/Location Accessories/Tazaranno Figurine.webp"
image jyennaFigue = "images/Location Accessories/Jyenna Figurine.webp"
image imyokyasFigue = "images/Location Accessories/Imyokimyas Figurine.webp"
image oldXerxFigue = "images/Location Accessories/Xerxes The Elder Figurine.webp"
image tastsurraFigue = "images/Location Accessories/Tastsurra Figurine.webp"
image astarteFigure = "images/Location Accessories/Astarte Figurine.webp"
image chariotFigue = "images/Location Accessories/Chariot Figurine.webp"


#projectiles and items
image roundRock = "images/items/ballStone.webp"
image arrows = "images/items/arrow.webp"
image metalArrows = "images/items/arrowBoltShort.webp"
image javelins = "images/items/javelinBasic.webp"
image ironJavelins = "images/items/javelinIron.webp"
image daricCoin = "images/items/daric.webp"
image potionzRed = "images/items/bottlePotionRed.webp"
image potionzBlue = "images/items/bottlePotionBlue.webp"
image reviva = "images/items/reviver fang.webp"
image purpleRock = "images/items/purple rock.webp"

image magicShot = "images/magic shot.webp"
image magicStart = "images/magic shot Point.webp"

image foodKnife = "images/items/knife iron.webp"
image theSoAM = "images/weapons armor and shields/Sword of Ahura-Mazda.webp"


image greenKey = "images/items/keysZwotiSoAM.webp"
image yellowKey = "images/items/keyKworitxSoAM.webp"
image redKey = "images/items/keyTakuriumSoAM.webp"
image kwortixGenericKeyz = "images/items/keysKwortixGeneric.webp"
image bombChemicals = "images/items/bombKitYellow.webp"

image goldRimShield = "images/weapons armor and shields/jamesian Shield Xerxes2.webp"

image grapplePointEnd = "images/Grapple Point.webp"
image grapplePointChain = "images/Chain.webp"
image chains = Tile("images/Chain.webp")

image doll1 = "images/items/Doll Partly Restored.webp"
image doll1MissingEye = "images/items/Doll Old.webp"
image dollEyeBall = "images/items/Glass Eye Red.webp"
image doll2 = "images/items/Doll 2.webp"
image doll2Hang = "images/items/Doll 2 hang.webp"

image aNet = "images/items/net.webp"

image antiStealthScroll = "images/items/tabletDocument.webp"

image jamesossianSword = "images/weapons armor and shields/jamesian Sword.webp"

image tastsetuShield1 = "images/weapons armor and shields/Zara-Tastsetu Shield with Javelins.webp"
image tastsetuShield2 = "images/weapons armor and shields/Zara-Tastsetu Shield with Darts.webp"
image zaratShield = "images/weapons armor and shields/zaratian shield rightHand.webp"

image shataShieldLow = "images/weapons armor and shields/Shata Shield lowLevel.webp"
image shataShieldHigh = "images/weapons armor and shields/shata shield highLevel.webp"
image ssatuShield = "images/weapons armor and shields/ssatu shield.webp"

image shataMace = "images/weapons armor and shields/Shata Mace.webp"
image ssatuLongbowWep = "images/weapons armor and shields/ssatu longbow.webp"

#food golrious food
image Meat = "images/items/meat.webp"
image spicedUpMeat = "images/items/Cooked Meat Spicy.webp"
image spicedUpCrayfish = "images/items/cave crayfish cooked spicy.webp" 
image crayfished = "images/items/cave crayfish.webp"

image saltyMeatyMeat = "images/items/salty meat.webp"
image baitFish = "images/items/bait fish.webp"
image floodFish = "images/items/jamesosian flood fish.webp"
image spicedUpFish = "images/items/bait fish.webp"

image cookedRat = "images/items/cooked Rat.webp"
image cookedMeat = "images/items/Cooked Meat.webp"
image redChesse = "images/items/cheese.webp"
image stinkyCheese = "images/items/smeally cheese.webp"
image cookedMussel = "images/items/cooked mussel.webp"
image meatRibs = "images/items/Meat Ribs.webp"

image bread = "images/items/Bread.webp"
image harraFruit = "images/items/Harra Fruit.webp"
image fruits = "images/items/fruits.webp"
image foodLeaves = "images/items/food Leaves.webp"
image foodSeedyLeaves = "images/items/food Seedy Leaves.webp"

image foodWorms = "images/items/Food Worms.webp"
image foodBeetles = "images/items/domestic food beetle.webp"

image fishCake = "images/items/fish cake gilgamorian.webp"
image meatyFishCake = "images/items/eggMeat Cake.webp"

image redSpicy = "images/items/red spice.webp"
image salty =  "images/items/Salt.webp"

image feathersFalcobite = "images/items/feathers falcobite.webp"

image grapplePointer1 = "images/items/Grapple Point Shooter.webp"
image harpoonLauncherImg = "images/items/Harpoon Launcher.webp"

image deadVelosoFe = "images/items/Dead VelosoraptorF.webp"
image deadVelosoMa = "images/items/Dead VelosoraptorM.webp"
image feathersVelosoM = "images/items/feathers VelosoM.webp"
image feathersVelosoF = "images/items/feathers VelosoF.webp"
image acidRock = "images/items/iron 2 sulfate.webp"
image acidPot = "images/items/Acid Pot.webp"
image astartinToken = "images/items/Astartin.webp"

image deadAssFalcobite = "images/items/Dead Falcobite.webp"
image deadAssJakalbite = "images/items/Dead Jakalbite Bomb.webp"
image deadVelsosDude = "images/items/Dead VelosoraptorM.webp"
image deadVelsosLady = "images/items/Dead VelosoraptorF.webp"




#The tablet

image stoneTablet = "images/Stone Tablet Whole.webp"
image stoneTabletGil = "images/items/Stone Tablet Zarat.webp"
image stoneTabletZard = "images/items/Stone Tablet Zardon.webp"
image stoneTabletBala = "images/items/Stone Tablet Bala.webp"
image stoneTabletMakka = "images/items/Stone Tablet Makka.webp"

#characters

#animals

image xerxesHorseArmored = "images/animals/Full Armored Horse Front2.webp"
image tesipizHorseArmored = "images/animals/Full Armored Horse Front1.webp"

#other Faction Troopers
#Axerians
image axerianInfAttackSpear = "images/Enemies/astartes goons/Astarto-Axerian Spear Attack.webp"
image axerianInfSuprizedSpear = "images/Enemies/astartes goons/Astarto-Axerian Spear Suprizeds.webp"
image axerianInfJavelins = "images/Enemies/astartes goons/Astarto-Axerian Javelin Attack.webp"
image axerianInfantry = "images/Enemies/astartes goons/Astarto-Axerian Spear.webp"

image zwotiInfantryDude = "images/NPCs/Takuria/Zwoti Infantry Male.webp"
image zwotiInfantryLady = "images/NPCs/Takuria/Zwoti Black Armor Infantry Female.webp"

image takuraSnakeArcher = "images/NPCs/Takuria/Takurian Snake Archer.webp"
image takuraKardakes = "images/NPCs/Takuria/Light Kardakes.webp"
image takuraLightCavarly = "images/NPCs/Takuria/Light Cavarly.webp"
image zwotiCavarly = "images/NPCs/Takuria/Zwoti Cavarly Male.webp"

#Neutral villagers
image astartLady1 = "images/NPCs/Astart Cilivians/astart lady1.webp"
image astartDude1 = "images/NPCs/Astart Cilivians/astart dude1.webp"
image astartDude1Side = "images/NPCs/Astart Cilivians/astart dude1 Side.webp"


#goons - place only if they appear in game
    #"images/Enemies/astartes goons"

#"Astarts" (Kazwiians , Sarratans , Hammites , Ximdians , Kirinians, Kwimians , Ssyayans, Pellosians, Centralians) 
image kazwiianSpear = "images/Enemies/astartes goons/Heavy Spear inf Kazwiian Female.webp"

image astartCommonInfantryMale = "images/Enemies/astartes goons/Astart Common Infantry Male1 v1.webp"
image astartCommonInfantryFemale = "images/Enemies/astartes goons/Astart Common Infantry Female1 v1.webp"
image astartCommonCavarlyMale = "images/Enemies/astartes goons/Astart Common Cavarly.webp"
image astartCommonCavarlyFemale = "images/Enemies/astartes goons/Astart Common Cavarly Female.webp"

image astartHopliteFemale = "images/Enemies/astartes goons/Astart Hoplite Female 1 v1.webp"
image astartHopliteMale = "images/Enemies/astartes goons/Astart Hoplite Male1 v1.webp"
image astartHopliteMale2 = "images/Enemies/astartes goons/Astart Hoplite Male2.webp"
image astartHopliteMale2Back = "images/Enemies/astartes goons/Astart Hoplite Male2 Back.webp"
image astartSlinger = "images/Enemies/astartes goons/Astart Slinger Low Level v1.webp"

image ostrichRider1NeutralHappy = "images/Enemies/astartes goons/Ostrich Raider 1 Neutral Happy.webp"
image ostrichRider1Suprized = "images/Enemies/astartes goons/Ostrich Raider 1 Suprized.webp"
image ostrichRider1 = "images/Enemies/astartes goons/Ostrich Raider 1.webp"
image ostrichRider1Fleeing = "images/Enemies/astartes goons/Ostrich Raider 1 fleeing.webp"
image ostrichRider2NeutralHappy = "images/Enemies/astartes goons/Ostrich Raider 2 Neutral Happy.webp"
image ostrichRider2Mad = "images/Enemies/astartes goons/Ostrich Raider 2 mad.webp"
image ostrichRider2Suprized = "images/Enemies/astartes goons/Ostrich Raider 2 Suprized.webp"
image ostrichRider2Fleeing = "images/Enemies/astartes goons/Ostrich Raider 2 fleeing.webp"

image astartMediumCvarly = "images/Enemies/astartes goons/Astart Medium Cavarly.webp"
image astartMediumCvarlyFlee = "images/Enemies/astartes goons/Astart Medium Cavarly Fleeing.webp"
#Jaka
image jakaKhopesh = "images/Enemies/astartes goons/Jaka Khopesh low-level v1.webp"
image jakaArcher = "images/Enemies/astartes goons/Jaka Archer Low Level.webp"
image jakaCamelLancer = "images/Enemies/astartes goons/Jaka Camel Lancer.webp"
image jakaCamelLancerFlee = "images/Enemies/astartes goons/Jaka Camel Lancer Fleeing.webp"
image jakaCamelArcher = "images/Enemies/astartes goons/Jaka Camel Archer.webp"

#Faronians
image faronianAxNakedFemale = "images/Enemies/astartes goons/Faronian Axe Naked Female v1 sfw.webp"

#Balatians
image balatianNekkedAxeWoman = "images/Enemies/astartes goons/Balatian Axe Naked Female v1.webp"
#image balatianAmoredAx = "images/Enemies/astartes goons/Balatian Axe Armored Female v1.webp"
image balaAstartWhippa = "images/Enemies/astartes goons/Balato-Astart Slaver.webp"
image balaAstartWhippaWhipping: 
    "images/Enemies/astartes goons/Balato-Astart Slaver Whip up.webp"
    pause 0.25
    "images/Enemies/astartes goons/Balato-Astart Slaver Whip down.webp"
    pause 0.125
    "images/Enemies/astartes goons/Balato-Astart Slaver Whip down2.webp"
    pause 0.125
    repeat
image astartBalatianLancerCharge = "images/Enemies/astartes goons/balatian light lancer charge.webp"

#Suzumites
image heavySuzumiteFemaleSpear = "images/Enemies/astartes goons/Heavy Spear inf Suzumite Female Shield.webp"

#Ordoians
image ordonianKaetratiiMaleNeko = "images/Enemies/astartes goons/Ordonian Kaetratii Male nekomini v1.webp"
image ordonianScutarii = "images/Enemies/astartes goons/Ordonian Scutarii low Level.webp"
image ordonianJavilenLight = "images/Enemies/astartes goons/Ordonian Kaetratii Javelin Low Level v1.webp"
image ordonianCavarly = "images/Enemies/astartes goons/Ordonian Falkata Cavarly.webp"

#Orodians
image orodianCavarly = "images/Enemies/astartes goons/Orodian Light Cavarly.webp"

#Thians
image thiaMaceMale = "images/Enemies/astartes goons/Thia mace male v1.webp"
image thiaSpear = "images/Enemies/astartes goons/Thia Spear Infantry Female low level v1.webp"
image astartoThiaKhopeshFemale = "images/Enemies/astartes goons/Astarto-Thia Khopesh Female v1.webp"

#Shata
image shataSpear = "images/Enemies/Shata and Ssatu/Shata Speardude Yeah.webp"
image shataSpearCharge = "images/Enemies/Shata and Ssatu/Shata Speardude Attack.webp"
image shataSpearFemale = "images/Enemies/Shata and Ssatu/Shata Speargirl Yeah.webp"
image shataSpearFemaleCharge = "images/Enemies/Shata and Ssatu/Shata Speargirl Attack.webp"
image shataDoggoDude = "images/Enemies/Shata and Ssatu/Shata Summoner Simple.webp"
image shataDoggoDudeFlees = "images/Enemies/Shata and Ssatu/Shata Summoner Simple Fleing.webp" 
image shataSkrimisher = "images/Enemies/Shata and Ssatu/Shata Speardude2 Yeah.webp"

image shataMaceLady = "images/Enemies/Shata and Ssatu/Shata Macelady.webp"
image shataMaceLadySwim = "images/Enemies/Shata and Ssatu/Shata Macelady Swimming Scared.webp"
image shataMaceLadyFlee = "images/Enemies/Shata and Ssatu/Shata Macelady flee backwards.webp"
image shataMaceLadyHandsUp = "images/Enemies/Shata and Ssatu/Shata Macelady Hands up.webp"
image shataMaceLdayNoMace = "images/Enemies/Shata and Ssatu/Shata Macelady unarmed.webp"

image shataBowDude = "images/Enemies/Shata and Ssatu/Shata archer.webp"

image shataArmoredMaceDude = "images/Enemies/Shata and Ssatu/Shata MaceMan.webp"
image shataArmoredMaceDudeFlee = "images/Enemies/Shata and Ssatu/Shata MaceMan flee back.webp"
image shataArmoredMaceDudeHandsUp = "images/Enemies/Shata and Ssatu/Shata MaceMan Hands Up.webp"

image shataArmoredMaceGirl = "images/Enemies/Shata and Ssatu/Shata Mauler.webp"

#shatseta
layeredimage shatsetaArmoredSpearM:
    group poses:
        attribute guarding default:
            "images/Enemies/Shata and Ssatu/Shtseta Armored Speardude Guarding.webp"
        attribute landAttack:
            "images/Enemies/Shata and Ssatu/Shtseta Armored Speardude.webp"
        attribute swimAttack:
            "images/Enemies/Shata and Ssatu/Shtseta Armored Speardude Swiimin.webp"

    group eyes:
        attribute neutralEyes default if_any["guarding","landAttack"]:
            "images/Enemies/Shata and Ssatu/Shtseta Armored Speardude Neutral Eyes.webp"
        attribute neutralEyes default if_any["swimAttack"]:
            "images/Enemies/Shata and Ssatu/Shtseta Armored Speardude Neutral Eyes.webp"
            ypos -232 xpos 15

        attribute meanEyes if_any["guarding","landAttack"]:
            "images/Enemies/Shata and Ssatu/Shtseta Armored Speardude Mean eyes.webp"
        attribute meanEyes if_any["swimAttack"]:
            "images/Enemies/Shata and Ssatu/Shtseta Armored Speardude Mean eyes.webp"
            ypos -232 xpos 15
        
        attribute sadEyes if_any["guarding","landAttack"]:
            "images/Enemies/Shata and Ssatu/Shtseta Armored Speardude Sad Eyes.webp"
        attribute sadEyes if_any["swimAttack"]:
            "images/Enemies/Shata and Ssatu/Shtseta Armored Speardude Sad Eyes.webp"
            ypos -232 xpos 15

    group mouths:
        attribute neutralHappyMouth default if_any["guarding","landAttack"]:
            "images/Enemies/Shata and Ssatu/Shtseta Armored Speardude Neutral Happy Mouth.webp"
        attribute neutralHappyMouth default if_any["swimAttack"]:
            "images/Enemies/Shata and Ssatu/Shtseta Armored Speardude Neutral Happy Mouth.webp"
            ypos -232 xpos 17

        attribute happyMouth if_any["guarding","landAttack"]:
            "images/Enemies/Shata and Ssatu/Shtseta Armored Speardude Happy Mouth.webp"
        attribute happyMouth if_any["swimAttack"]:
            "images/Enemies/Shata and Ssatu/Shtseta Armored Speardude Happy Mouth.webp"
            ypos -232 xpos 17

        attribute oMouth if_any["guarding","landAttack"]:
            "images/Enemies/Shata and Ssatu/Shtseta Armored Speardude O Mouth.webp"
        attribute oMouth if_any["swimAttack"]:
            "images/Enemies/Shata and Ssatu/Shtseta Armored Speardude O Mouth.webp"
            ypos -232 xpos 17

        attribute deltaMouth if_any["guarding","landAttack"]:
            "images/Enemies/Shata and Ssatu/Shtseta Armored Speardude Delta Mouth.webp"
        attribute deltaMouth if_any["swimAttack"]:
            "images/Enemies/Shata and Ssatu/Shtseta Armored Speardude Delta Mouth.webp"
            ypos -232 xpos 17

image shatsetaWarriorGirl = "images/Enemies/Shata and Ssatu/Shatseta Warrior Girl.webp"
image shatsetaWarriorGirlSwimming = "images/Enemies/Shata and Ssatu/Shatseta Warrior Swimming.webp"
image shatsetaArcherDude = "images/Enemies/Shata and Ssatu/Shatseta archer.webp"
image shatsetaArcherDudeSwimming = "images/Enemies/Shata and Ssatu/Shatseta archer swimming.webp"

#Ssatu

#Ssatu Bandits
image ssatuBanditSpear = "images/Enemies/Shata and Ssatu/ssatu bandit spear.webp"
image ssatuBanditSpearAttack = "images/Enemies/Shata and Ssatu/ssatu bandit spear attack.webp"
image ssatuBanditSpeargirl = "images/Enemies/Shata and Ssatu/Ssatu bandit spearlady.webp"
image ssatuBanditSpeargirlAttack = "images/Enemies/Shata and Ssatu/Ssatu levy spearlady attack.webp"
image ssatuBanditJavelins = "images/Enemies/Shata and Ssatu/Ssatu Bandit Javelins.webp"
image ssatuBanditGlaves = "images/Enemies/Shata and Ssatu/Ssatu Bandit Glaves.webp"

image ssatuSlaver = "images/Enemies/Shata and Ssatu/ssatu slaver.webp"
image ssatuSlaverOi = "images/Enemies/Shata and Ssatu/ssatu slaver oi.webp"
image ssatuSlaverCommanding = "images/Enemies/Shata and Ssatu/ssatu slaver commanding.webp"
image ssatuSlaverBallNChain = "images/Enemies/Shata and Ssatu/ssatu slaver summoning.webp"
image ssatuSlaverWhipping = "images/Enemies/Shata and Ssatu/ssatu slaver whipping.webp"

#Ssatu Bandits Enslaved
image ssatuSlaverEnslaved = "images/NPCs/Jamesia/Kwortix/Kwortix Mine/ssatu slaver enslaved lol.webp"
image ssatuDoggoEnSlaved = "images/NPCs/Jamesia/Kwortix/Kwortix Mine/Ssatu Summoner Slave.webp"
image ssatuLongbowEnslaved = "images/NPCs/Jamesia/Kwortix/Kwortix Mine/ssatu longbow slave.webp"


#regular ssatu
image ssatuDoggoDude = "images/Enemies/Shata and Ssatu/Ssatu Summoner Simple.webp"
image ssatuDoggoDudeFlees = "images/Enemies/Shata and Ssatu/Ssatu Summoner Simple Fleing.webp"
image ssatuLongbowImg = "images/Enemies/Shata and Ssatu/ssatu longbow dude.webp"

image ssatuLongbowGirlImg = "images/Enemies/Shata and Ssatu/Ssatu longbow lady.webp"
image ssatuLongbowGirlSwim = "images/Enemies/Shata and Ssatu/Ssatu longbow lady swim.webp"
image ssatuLongbowGirlFlee = "images/Enemies/Shata and Ssatu/Ssatu longbow lady flee back.webp"
image ssatuLonhbowGirlHandsUp = "images/Enemies/Shata and Ssatu/Ssatu longbow lady hands up.webp"

image ssatuArmoredJavelinMelee = "images/Enemies/Shata and Ssatu/ssatu armored Swords.webp"
image ssatuArmoredJavelinRanged = "images/Enemies/Shata and Ssatu/ssatu armored Javelins.webp"
image ssatuArmoredJavelinHold = "images/Enemies/Shata and Ssatu/ssatu armored Javelins arm up.webp"
image ssatuArmoredJavelinPush = "images/Enemies/Shata and Ssatu/ssatu armored Javelins push.webp"
image ssatuArmoredJavelinFlee = "images/Enemies/Shata and Ssatu/ssatu armored Javelins back flee.webp"
image ssatuArmoredJavelinSad = "images/Enemies/Shata and Ssatu/ssatu armored Javelins arm down sad.webp"
image ssatuArmoredJavelinSwim = "images/Enemies/Shata and Ssatu/ssatu armored Javelins swim.webp"
image ssatuArmoredJavelinArmsUp = "images/Enemies/Shata and Ssatu/ssatu armored Javelins arms up.webp"

image ssatuGlaiveGirlAttack = "images/Enemies/Shata and Ssatu/ssatu glave female attack.webp"
image ssatuGlaiveGirlSuprized = "images/Enemies/Shata and Ssatu/ssatu glave female suprized.webp"
image ssatuGlaiveGirlOuched = Composite( (1000,1800) , (0,0) , "images/Enemies/Shata and Ssatu/ssatu glave female suprized.webp" , (0,0) , "images/Enemies/Shata and Ssatu/ssatu glave female ouch face.webp")

image ssatuGlaiveBoyAttack = "images/Enemies/Shata and Ssatu/ssatu glave male attack.webp"
image ssatuGlaiveBoySuprized = "images/Enemies/Shata and Ssatu/ssatu glave male suprized.webp"

#Zardonians
image zardonianAxeDude = "images/Enemies/Zardonians/Zardonian AxeMAN.webp"

image zardonianAxeGirl = "images/Enemies/Zardonians/Zardonian Axe WoahMAN.webp"
image zardonianAxeGirlFlee = "images/Enemies/Zardonians/Zardonian Axe WoahMAN back fleeing.webp"

image zardonianSwordsMan = "images/Enemies/Zardonians/zardonian legionier mail.webp"
image zardonianSwordsManFlee = "images/Enemies/Zardonians/zardonian legionier mail back flee.webp"

image zardonianSwordsWoahMan = "images/Enemies/Zardonians/zardonian legionier pheemail.webp"

image zardonianDartBoy = "images/Enemies/Zardonians/Plumbata Peltast Duude.webp"

image zardonianDartGirl = "images/Enemies/Zardonians/Plumbata Peltast lady.webp"
image zardonianDartGirlLeave = "images/Enemies/Zardonians/Plumbata Peltast lady back fleeing.webp"

image zardonianHarpoonDude = "images/Enemies/Zardonians/Tastsetrotu Harpooneer.webp"
    #Korkins
    #Junatu
    #Half-Junatu

#boats
image zardonianBoatFrontUp = "images/antagonists/Mini-Bosses/Zardonian WarShip Ramside Up.webp"
image zardonianBoatFrontDown = "images/antagonists/Mini-Bosses/Zardonian WarShip Ramside Down.webp"
image zardonianBoatFrontNoRamp = "images/antagonists/Mini-Bosses/Zardonian WarShip Ramside.webp"
image zardonianBoatSide = "images/antagonists/Mini-Bosses/Zardonian WarShip Broadside.webp"

image astartTriremeFront = "images/antagonists/Mini-Bosses/Astart Trireme Ramside.webp"
image astartTriremeSide = "images/antagonists/Mini-Bosses/Astart Trireme Broadside.webp"

image astartLandingBoatFront = "images/antagonists/Mini-Bosses/Astart Landing Craft Front.webp"
image astartLandingBoatSide = "images/antagonists/Mini-Bosses/Astart Landing Craft Side.webp"
image astartLandingBoatMast = "images/antagonists/Mini-Bosses/Astart Sail.webp"
image astartLandingBoatRampUp = "images/antagonists/Mini-Bosses/Astart Landing Craft Ramp up.webp"
image astartLandingBoatRampDown = "images/antagonists/Mini-Bosses/Astart Landing Craft ramp down.webp"

#Makkabians
image makkabianArmoredLongbowFemale = "images/Enemies/Makkabians/Makkabian Longbow Female.webp"

#ahrites

image ahriteGiantMale = "images/Enemies/Ahrites/Ahrite Giant Male.webp"
image ahriteGiantFemale = "images/Enemies/Ahrites/Ahrite Giant Female.webp"
image ahriteNiomMale = "images/Enemies/Ahrites/ahrite Niom.webp"
image ahriteNiomFemale = "images/Enemies/Ahrites/ahrite Niom Female.webp"
image ahriteSpearMale = "images/Enemies/Ahrites/ahrite spear t1 Male.webp"
image ahriteSpearFemale = "images/Enemies/Ahrites/ahrite spear t1 Female.webp"
image merDemonMaleLand = "images/Enemies/Ahrites/Mer-Daemon t1 Male.webp"
image merDemonMaleSwim = "images/Enemies/Ahrites/Mer-Daemon t1 Male Swimming.webp"
image merDemonFemaleLand = "images/Enemies/Ahrites/Mer-Daemon t1 Female.webp"
image merDemonFemaleSwim = "images/Enemies/Ahrites/Mer-Daemon t1 Female Swimming.webp"

image miniAhrimaniomLosing = "images/Enemies/Ahrites/Mini Ahrimaniom Side Attacked.webp"

#humanoid Monsters
image jakalbiteKhopeshLight = "images/Enemies/astartes goons/Jakalbite Khopesh low-level v1.webp"
image lizardbiteEspionAx = "images/Enemies/astartes goons/Lizardbite Espion Axman v1.webp"
image jakalbiteSpear = "images/Enemies/astartes goons/Jakalbite Spear v1.webp"
image falcobiteArcher = "images/Enemies/astartes goons/falcobite archer.webp"
image lizardbiteArcher = "images/Enemies/astartes goons/Lizardbite archer.webp"
image jakalbiteKhopeshMedium = "images/Enemies/astartes goons/Jakalbite Khopesh medium-level v1.webp"
image minobiteSpear = "images/Enemies/astartes goons/Minobite Low level v1.webp"
image minobiteAxe = "images/Enemies/eliete goons/Minobite Great Axe.webp"

image minobiteFallingSide = "images/Enemies/astartes goons/Minobite Archer Falling.webp" 

image snakeMan = "images/Enemies/astartes goons/Snakebite.webp"
image snakeManInWater = "images/Enemies/astartes goons/Snakebite Swimming.webp"


#animal Monsters
image nitroacidicCobra = "images/Enemies/astartes goons/Nitroacidic Cobra.webp"
image pythonSnake = "images/Enemies/astartes goons/Python.webp"
image ratasUnmounted = "images/Enemies/astartes goons/ratas unmounted.webp"
image ssyayanBiterBat = "images/Enemies/astartes goons/Ssyayan Biter Bat.webp"
image jamesianWolf = "images/Enemies/Shata and Ssatu/Jamesian Wolf Unmounted.webp"

#tsetulings
image tsetulingGuardF = "images/Enemies/astartes goons/Tsetuling Fighter Guard.webp"
image tsetulingGuardM = "images/Enemies/astartes goons/Tsetuling Fighter Male Guarding.webp"
image tsetulingGuardM2 = "images/Enemies/astartes goons/Tsetuling Fighter Male Guarding Qhekka.webp"

# Bardaiya's eleite guard
image bardaiyaPioneerFemale = "images/Enemies/eliete goons/Bardaiya Pioneer Female.webp"
image bardaiyaPioneerMaleNeko = "images/Enemies/eliete goons/Bardaiya Pioneer Male Nekomimi.webp"

    # This shows a character sprite. A placeholder is used, but you can

#antagonists

#bardaiya
image bardproud = "images/antagonists/Bardaiya/Bardaiya Armored Proud Standing.webp"

image bardaiyaSad = "images/antagonists/Bardaiya/Bardaiya Sad.webp"
image bardaiyaAngry = "images/antagonists/Bardaiya/Bardaiya Angry.webp"
image bardaiya34Angry = "images/antagonists/Bardaiya/Bardaiya 34 Angry.webp"
image bardaiyaCommandingHappy = "images/antagonists/Bardaiya/Bardaiya Commaning Happy.webp"
image bardaiyaCommanding = "images/antagonists/Bardaiya/Bardaiya Commaning.webp"
image bardaiyaConsured = "images/antagonists/Bardaiya/Bardaiya Consurend.webp"
image bardaiyaHappy = "images/antagonists/Bardaiya/Bardaiya Happy.webp"
image bardaiyaHappyGun = "images/antagonists/Bardaiya/Bardaiya Happy with gun.webp"
image bardaiyaNeutralHappy = "images/antagonists/Bardaiya/Bardaiya Neutral Happy.webp"



#Lakatinu
image lakatinu34LookingDownHeheh = "images/antagonists/Lakatinu/Lakatinu 3-4 looking down heheh.webp"
image lakatinu34LookingDownMad = "images/antagonists/Lakatinu/Lakatinu 3-4 looking down slightly mad.webp"
image lakatinuKwortixMad = "images/antagonists/Lakatinu/Lakatinu Kwotix Mad.webp"
image lakatinuKwortixHehe = "images/antagonists/Lakatinu/Lakatinu Kwotix Hehe.webp"

image lakatinu34BackAnnoyed = "images/antagonists/Lakatinu/Lakatinu 34 Ass Annoyed.webp"
image lakatinu34BackHappy = "images/antagonists/Lakatinu/Lakatinu 34 Ass Happy.webp"

image lakatinuBack = "images/antagonists/Lakatinu/Lakatinu Ass Away Down.webp"
image lakatinuBackBlood = "images/antagonists/Lakatinu/Lakatinu Ass Away Down Bloodied.webp"
image lakatinuSlashDive = "images/antagonists/Lakatinu/Lakatinu Dive Attack Sword.webp"

image lakatinuShieldBash = "images/antagonists/Lakatinu/Lakatinu Shield Bash.webp"
image lakatinuJumpShield = "images/antagonists/Lakatinu/Lakatinu Hands Out FLying.webp"

image lakatinuNeutralHappy = "images/antagonists/Lakatinu/Lakatinu Neutral Happy.webp"
image lakatinuNeutralHappy2 = "images/antagonists/Lakatinu/Lakatinu Neutral Happy2.webp"
image lakatinuNeutralHappyArmored = "images/antagonists/Lakatinu/Lakatinu Neutral Happy Armored.webp"

image lakatinuHappy = "images/antagonists/Lakatinu/Lakatinu Happy.webp"
image lakatinuHappyWithGun = "images/antagonists/Lakatinu/Lakatinu Happy with gun.webp"

image lakatinuGunArmored = "images/antagonists/Lakatinu/Lakatinu Gun Armored.webp"

image lakatinuArmoredGround = "images/antagonists/Lakatinu/Lakatinu Sword Grounded.webp"

image lakatinuMad  = "images/antagonists/Lakatinu/Lakatinu Angry.webp"
image lakatinuMad2 = "images/antagonists/Lakatinu/Lakatinu Angry2.webp"
image lakatinuMadWithGun = "images/antagonists/Lakatinu/Lakatinu Angry with gun.webp"

image lakatinuSad = "images/antagonists/Lakatinu/Lakatinu Sad.webp"
image lakatinuSad2 = "images/antagonists/Lakatinu/Lakatinu Sad2.webp"
image lakatinuSadArmored = "images/antagonists/Lakatinu/Lakatinu Sad Armored.webp"

image lakatinuSexyNekked = "images/antagonists/Lakatinu/Lakatinu Nekked Seductive.webp"
image lakatinuSexyNekkedClosedMouth = "images/antagonists/Lakatinu/Lakatinu Nekked Seductive Closed Mouth.webp"
image lakatinuSexyNekkedSad = "images/antagonists/Lakatinu/Lakatinu Nekked Sad.webp"
image lakatinuSexyOnAll6s = "images/antagonists/Lakatinu/lakatinu seductive on all 4s.webp"
image lakatinuBoikingBardaiya = "images/antagonists/Lakatinu/lakatinu seductive on Nekked Bardaiya POV.webp"

image lakatinuWithBardaiyaHappy = "images/antagonists/Lakatinu/Lakatinu and Bardayia Together Happy.webp"
image lakatinuWithBardaiyaComforting = "images/antagonists/Lakatinu/Lakatinu and Bardayia Together Conforting.webp"

layeredimage lakatinuFront:
    group outfitPose:
        attribute basic default:
            "images/antagonists/Lakatinu/Lakatinu Neutral Happy.webp"
        attribute basicGun:
            "images/antagonists/Lakatinu/Lakatinu Angry with gun.webp"
        attribute light:
            "images/antagonists/Lakatinu/Lakatinu Neutral Happy2.webp"
        attribute armored:
            "images/antagonists/Lakatinu/Lakatinu Neutral Happy Armored.webp"
        attribute armoredGun:
            "images/antagonists/Lakatinu/Lakatinu With Gun Armored.webp"

    group eyes:
        attribute neutralEyes default:
            "images/antagonists/Lakatinu/Lakatinu Neutral Eyes.webp"
        attribute angryEyes:
            "images/antagonists/Lakatinu/Lakatinu Angry Eyes.webp"
        attribute sadEyes:
            "images/antagonists/Lakatinu/Lakatinu Sad Eyes.webp"
        attribute meanEyes:
            "images/antagonists/Lakatinu/Lakatinu Mean Eyes.webp"

    group mouth:
        attribute neutralHappyMouth default:
            "images/antagonists/Lakatinu/Lakatinu Neutral Happy Mouth.webp"
        attribute OMouth:
            "images/antagonists/Lakatinu/Lakatinu OMouth.webp"
        attribute happyMouth:
            "images/antagonists/Lakatinu/Lakatinu Happy Mouth.webp"
        attribute angryMouth:
            "images/antagonists/Lakatinu/Lakatinu Angry Mouth.webp"

image lakatinusButtWingsUp = "images/antagonists/Lakatinu/Lakatinu Ass Away Up.webp"

image lakatinuFlyAway:
    "images/antagonists/Lakatinu/Lakatinu Ass Away Down.webp"
    pause 1.0
    "images/antagonists/Lakatinu/Lakatinu Ass Away Up.webp"
    pause 1.0
    repeat
image lakatinuFlyAwayBloodied:
    "images/antagonists/Lakatinu/Lakatinu Ass Away Down Bloodied.webp"
    pause 1.0
    "images/antagonists/Lakatinu/Lakatinu Ass Away Up Bloodied.webp"
    pause 1.0
    repeat   
image lakatinuSideFlap:
    "images/antagonists/Lakatinu/Lakatinu Side Flying Wing Up.webp"
    pause 1.0
    "images/antagonists/Lakatinu/Lakatinu Side Flying Wing Down.webp"
    pause 1.0
    repeat    

image lakatinuSideWingUp = "images/antagonists/Lakatinu/Lakatinu Side Flying Wing Up.webp"

image lakatinuFrontFly:
    "images/antagonists/Lakatinu/Lakatinu Fly Foward Up.webp"
    pause 1.0
    "images/antagonists/Lakatinu/Lakatinu Fly Foward.webp"
    pause 1.0
    repeat 

image lakatinuFrontFlyMad:
    Composite ((3600,2200),(0,0),"images/antagonists/Lakatinu/Lakatinu Fly Foward Up.webp",(0,0),"images/antagonists/Lakatinu/Lakatinu Fly Angry Face.webp")
    pause 1.0
    Composite ((3600,2200),(0,0),"images/antagonists/Lakatinu/Lakatinu Fly Foward.webp",(0,0),"images/antagonists/Lakatinu/Lakatinu Fly Angry Face.webp")
    pause 1.0
    repeat 

image lakatinuFrontFlyYeah:
    Composite ((3600,2200),(0,0),"images/antagonists/Lakatinu/Lakatinu Fly Foward Up.webp",(0,0),"images/antagonists/Lakatinu/Lakatinu Fly Yeah Face.webp")
    pause 1.0
    Composite ((3600,2200),(0,0),"images/antagonists/Lakatinu/Lakatinu Fly Foward.webp",(0,0),"images/antagonists/Lakatinu/Lakatinu Fly Yeah Face.webp")
    pause 1.0
    repeat    

#krokkosnek
image krokkosnekAngryAround = "images/antagonists/Krokkosnek/Krokkosnek Angry around.webp"
image krokkosnekAngryWater = "images/antagonists/Krokkosnek/Krokkosnek Angry Swimming.webp"
image krokkosnekAngry = "images/antagonists/Krokkosnek/Krokkosnek Angry.webp"
image krokkosnekSad = Composite( (1300, 1500) , (0,0) , "images/antagonists/Krokkosnek/Krokkosnek Angry.webp" , (0,0) , "images/antagonists/Krokkosnek/Krokkosnek Sad Eyes.webp")
image krokkosnekAnnoyed = "images/antagonists/Krokkosnek/Krokkosnek Annoyed.webp"
image krokkosnekZappingU = "images/antagonists/Krokkosnek/Krokkosnek Battle Land Ranged.webp"
image krokkosnekZappingUNWater = "images/antagonists/Krokkosnek/Krokkosnek Battle Water Ranged.webp"
image krokkosnekSummon = "images/antagonists/Krokkosnek/Krokkosnek Battle Land.webp"
image krokkosnekSummonShield = "images/antagonists/Krokkosnek/Krokkosnek Battle Land Shield.webp"
image krokkosnekSummonNWater = "images/antagonists/Krokkosnek/Krokkosnek Grand Water Summoning.webp"
image krokkosnekSummonShieldNWater = "images/antagonists/Krokkosnek/Krokkosnek Battle Water.webp"
image krokkosnekCommanding = "images/antagonists/Krokkosnek/Krokkosnek Commanding.webp"
image krokkosnekCommandingSummoning = "images/antagonists/Krokkosnek/Krokkosnek Commanding Summoning.webp"
image krokkosnekGrand  = "images/antagonists/Krokkosnek/Krokkosnek Grand.webp"
image krokkosnekGrandWater = "images/antagonists/Krokkosnek/Krokkosnek Grand Water.webp"
image krokkosnekHappy = "images/antagonists/Krokkosnek/Krokkosnek Happy.webp"
image krokkosnekNeutralHappy = "images/antagonists/Krokkosnek/Krokkosnek Neutral Happy.webp"
image krokkosnekNeutralHappyPoint = "images/antagonists/Krokkosnek/Krokkosnek Neutral Happy around.webp"
image krokkosnekNeutralHappyWater = "images/antagonists/Krokkosnek/Krokkosnek Neutral Happy swimming.webp"
image krokkosnekScared = "images/antagonists/Krokkosnek/Krokkosnek Scared.webp"
image krokkosnekSuprized = Composite( (1300, 1500) , (0,0) , "images/antagonists/Krokkosnek/Krokkosnek Neutral Happy.webp" , (0,0) , "images/antagonists/Krokkosnek/Krokkosnek OMouth.webp" )
image krokkosnekSlitheringAway = "images/antagonists/Krokkosnek/Krokkosnek Slivering Away.webp"
image krokkosnekSwimmingAway = "images/antagonists/Krokkosnek/Krokkosnek Swimming Away.webp"

image krokkosnekGenderBentBoink = "images/antagonists/Krokkosnek/Genderbent Krokkosnek and Bardaiya.webp"

    #Krokkosnek's GirlFriends
image tipua34Happy = "images/antagonists/Krokkosnek/Krokkosneks Girlfriends/Tipua 34 lying happy.webp"
image tipuaAngry = "images/antagonists/Krokkosnek/Krokkosneks Girlfriends/Tipua Angry.webp"
image tipuaHappyCoiled = "images/antagonists/Krokkosnek/Krokkosneks Girlfriends/Tipua Coiled Happy.webp"
image tipuaShocked = "images/antagonists/Krokkosnek/Krokkosneks Girlfriends/Tipua Scared.webp"
image tipuaSliveringAway = "images/antagonists/Krokkosnek/Krokkosneks Girlfriends/Tipua Slivering Away.webp"
image tipuaHappyCoiled = "images/antagonists/Krokkosnek/Krokkosneks Girlfriends/Tipua Slivering Away.webp"#astart
image tipuaStandingHappy = "images/antagonists/Krokkosnek/Krokkosneks Girlfriends/Tipua standing Happy.webp" 
image tipuaExtraHappy = "images/antagonists/Krokkosnek/Krokkosneks Girlfriends/Tipua Extra Happy.webp"

image yeni34Happy = "images/antagonists/Krokkosnek/Krokkosneks Girlfriends/Yeni 34 lying happy.webp"
image yeniAngry = "images/antagonists/Krokkosnek/Krokkosneks Girlfriends/Yeni Angry.webp"
image yeniCoiledHappy = "images/antagonists/Krokkosnek/Krokkosneks Girlfriends/Yeni Coiled Happy.webp"
image yeniScared = "images/antagonists/Krokkosnek/Krokkosneks Girlfriends/Yeni Scared.webp"
image yeniShocked = "images/antagonists/Krokkosnek/Krokkosneks Girlfriends/Yeni Shocked.webp"
image yeniSliveringAway = "images/antagonists/Krokkosnek/Krokkosneks Girlfriends/Yeni Slivering Away.webp"
image yeniStandingHappy = "images/antagonists/Krokkosnek/Krokkosneks Girlfriends/Yeni Standing Happy.webp"
image yeniExtraHappy = "images/antagonists/Krokkosnek/Krokkosneks Girlfriends/Yeni Extra Happy.webp"


#Balatius
image balatiusHappy = "images/antagonists/King Balatius/Balatius Happy.webp"
image balatiusNeutralHappy = "images/antagonists/King Balatius/Balatius Neutral Happy.webp"
image balatiusAndGfs = "images/antagonists/King Balatius/Balatius with gfs Happy.webp"

    #Balatius' Girlfriends
image janaHappy = "images/antagonists/King Balatius/Balatius' Girlfriends/Jana Happy.webp"
image janaNeutralHappy = "images/antagonists/King Balatius/Balatius' Girlfriends/Jana Neutral Happy.webp"
image tsanihoniHappy = "images/antagonists/King Balatius/Balatius' Girlfriends/Tsanihoni Happy.webp"
image tsanihoniNeutralHappy = "images/antagonists/King Balatius/Balatius' Girlfriends/Tsanihoni Neutral Happy.webp"

#Minona
image astartChariot = "images/animals/Astart chariot.webp"
layeredimage minona:
    group poses:
        attribute sleepGear:
            "images/antagonists/Minona/Minona Standing Base.webp"
        attribute baseAndSpear default:
            "images/antagonists/Minona/Minona Armored Base.webp"
        attribute pointAndSpear:
            "images/antagonists/Minona/Minona Armored Pointing.webp"
    
    group mouths:
        attribute annoyedMouth if_not["pointAndSpear"]:
            "images/antagonists/Minona/Minona Annoyed Mouth.webp"
        attribute annoyedMouth if_any["pointAndSpear"]:
            "images/antagonists/Minona/Minona Annoyed Mouth.webp"
            xpos 300             

        attribute deltaMouth if_not["pointAndSpear"]:
            "images/antagonists/Minona/Minona Delta Mouth.webp"
        attribute deltaMouth if_any["pointAndSpear"]:
            "images/antagonists/Minona/Minona Delta Mouth.webp"
            xpos 300  

        attribute happyMouth if_not["pointAndSpear"]:
            "images/antagonists/Minona/Minona Happy Mouth.webp"
        attribute happyMouth if_any["pointAndSpear"]:
            "images/antagonists/Minona/Minona Happy Mouth.webp"
            xpos 300  

        attribute OMouth if_not["pointAndSpear"]:
            "images/antagonists/Minona/Minona O Mouth.webp"
        attribute OMouth if_any["pointAndSpear"]:
            "images/antagonists/Minona/Minona O Mouth.webp"
            xpos 300  

    group eyeBrows:
        attribute meanEyebrows if_not["pointAndSpear"]:
            "images/antagonists/Minona/Minona Mean Eyes.webp"
        attribute meanEyebrows if_any["pointAndSpear"]:
            "images/antagonists/Minona/Minona Mean Eyes.webp"
            xpos 300  

        attribute sadEyebrows  if_not["pointAndSpear"]:
            "images/antagonists/Minona/Minona Sad Eyebrows.webp"
        attribute sadEyebrows  if_any["pointAndSpear"]:
            "images/antagonists/Minona/Minona Sad Eyebrows.webp"
            xpos 300
    #veihcles are aways last
    group chariot:
        attribute inChariot:
            "images/animals/Astart chariot.webp"
            xpos -500  
            ypos 800
            zoom 0.9


#Astart Officers
#Astarto-Faronian
image astartoFaronianOfficerFight = "images/antagonists/Astart Officers/Astarto-Faronian Officer Fighting v1.webp"
image astartoFaronianOfficerCharge = "images/antagonists/Astart Officers/Astarto-Faronian Officer v1.webp"
image astartoFaronianOfficerPoint = "images/antagonists/Astart Officers/Astarto-Faronian Officer Pointing.webp"
image astartoFaronianOfficerTurn = "images/antagonists/Astart Officers/Astarto-Faronian Officer Turning v1.webp"
image astartoFaronianOfficerscared = "images/antagonists/Astart Officers/Astarto-Faronian Officer Turning v2 scared.webp"
image astartoFaronianOfficer = "images/antagonists/Astart Officers/Astarto-Faronian Officer.webp"
image astartoFaronianOfficerSlashed = "images/antagonists/Astart Officers/Astarto-Faronian Officer Attacked.webp"
#Astarto-Ordonian
image astartoOrdonianOffice = "images/antagonists/Astart Officers/Astarto-Ordonian Officer Fighting v1.webp"
image astartoOrdonianScared = "images/antagonists/Astart Officers/Astarto-Ordonian Officer Turning v1 scared.webp"

#ostrich captain
image captainHuksosNeutralHappy = "images/antagonists/Astart Officers/Huksos Neutral Happy.webp"
image captainHuksosSuprized = "images/antagonists/Astart Officers/Huksos Neutral Suprized.webp"
image captainHuksosAngry = "images/antagonists/Astart Officers/Huksos Neutral Angry.webp"
image captainHuksosAngryCommanding = "images/antagonists/Astart Officers/Huksos Angry Commanding.webp"
image captainHuksosFleeing = "images/antagonists/Astart Officers/Huksos Fleeing.webp"

#BalatianCavarly
image belgiusCharge = "images/antagonists/Astart Officers/Balatian Heavy Sword Cavarly Attack.webp"
layeredimage belgius:
    always:
        "images/antagonists/Astart Officers/Balatian Heavy Sword Cavarly.webp"
    group mouths:
        attribute happyMouth: 
            "images/antagonists/Astart Officers/Balatian Heavy Sword Cavarly Happy Mouth.webp"
        attribute neutralHappyMouth: 
            "images/antagonists/Astart Officers/Balatian Heavy Sword Cavarly Mini Happy Mouth.webp"
        attribute annoyedMouth: 
            "images/antagonists/Astart Officers/Balatian Heavy Sword Cavarly Annoyed Mouth.webp"
    group eyebrows:
        attribute meanEyebrows: 
            "images/antagonists/Astart Officers/Balatian Heavy Sword Cavarly Mean Eyes.webp"

image begliusGroundAttack = "images/antagonists/Astart Officers/Balatian Heavy Sword Attack.webp"
layeredimage belgius34Ground:
    always:
        "images/antagonists/Astart Officers/Balatian Heavy Sword Foot.webp"
    group eyes:
        attribute neutralEyes default:
            "images/antagonists/Astart Officers/Balatian Heavy Sword Neutral Eyes.webp"
        attribute meanEyes:
            "images/antagonists/Astart Officers/Balatian Heavy Sword Mean Eyes.webp"
    group mouths:
        attribute neutralHappyMouth default:
            "images/antagonists/Astart Officers/Balatian Heavy Sword Neutral Happy.webp"
        attribute happyMouth:
            "images/antagonists/Astart Officers/Balatian Heavy Sword Happy Mouth.webp"
        attribute annoyedMouth:
            "images/antagonists/Astart Officers/Balatian Heavy Sword Frown.webp"
        attribute angryMouth:
            "images/antagonists/Astart Officers/Balatian Heavy Sword Foot.webp"

#Commander Mwejya/ Flame Hypaspist
layeredimage mwejya:
    group poses:
        attribute basic default:
            "images/antagonists/Astart Officers/Astarto-Suzumite Hyspaspist.webp"
        attribute suprizedPose:
            "images/antagonists/Astart Officers/Astarto-Suzumite Hyspaspist Suprized.webp"
        attribute crossarms:
            "images/antagonists/Astart Officers/Astarto-Suzumite Hyspaspist Annoyed.webp"
        attribute chuckingPose:
            "images/antagonists/Astart Officers/Astarto-Suzumite Hyspaspist Throwing.webp"
        attribute commanding:
            "images/antagonists/Astart Officers/Astarto-Suzumite Hyspaspist Commanding.webp"
        attribute commnadingShield:
            "images/antagonists/Astart Officers/Astarto-Suzumite Hyspaspist Fighting.webp"

    group mouths:
        attribute neutralHappyMouth default if_any["basic"]:
            "images/antagonists/Astart Officers/Astarto-Suzumite Hyspaspist Neutral Happy Mouth.webp"
        attribute neutralHappy default if_any["suprizedPose", "crossarms"]:
            "images/antagonists/Astart Officers/Astarto-Suzumite Hyspaspist Neutral Happy Mouth.webp"
            xpos 165
        attribute neutralHappy default if_any["commanding","commnadingShield","chuckingPose"]:
            "images/antagonists/Astart Officers/Astarto-Suzumite Hyspaspist Neutral Happy Mouth.webp"
            xpos 365

        attribute happyMouth if_any["basic"]:
            "images/antagonists/Astart Officers/Astarto-Suzumite Hyspaspist Happy Mouth.webp"
        attribute happyMouth if_any["suprizedPose", "crossarms"]:
            "images/antagonists/Astart Officers/Astarto-Suzumite Hyspaspist Happy Mouth.webp"
            xpos 165
        attribute happyMouth if_any["commanding","commnadingShield","chuckingPose"]:
            "images/antagonists/Astart Officers/Astarto-Suzumite Hyspaspist Happy Mouth.webp"   
            xpos 365 
        
        attribute annoyedMouth if_any["basic"]:
            "images/antagonists/Astart Officers/Astarto-Suzumite Hyspaspist Frown.webp"
            xpos -165
        attribute annoyedMouth if_any["suprizedPose", "crossarms"]:
            "images/antagonists/Astart Officers/Astarto-Suzumite Hyspaspist Frown.webp"
        attribute annoyedMouth if_any["commanding","commnadingShield","chuckingPose"]:
            "images/antagonists/Astart Officers/Astarto-Suzumite Hyspaspist Frown.webp"  
            xpos 200  
        
        attribute oMouth if_any["basic"]:
            "images/antagonists/Astart Officers/Astarto-Suzumite Hyspaspist OMouth.webp"
            xpos -165
        attribute oMouth if_any["suprizedPose", "crossarms"]:
            "images/antagonists/Astart Officers/Astarto-Suzumite Hyspaspist OMouth.webp"
        attribute oMouth if_any["commanding","commnadingShield","chuckingPose"]:
            "images/antagonists/Astart Officers/Astarto-Suzumite Hyspaspist OMouth.webp"
            xpos 200
        
        attribute angryMouth if_any["basic"]:
            "images/antagonists/Astart Officers/Astarto-Suzumite Hyspaspist Angry Mouth.webp"
            xpos -370
        attribute angryMouth if_any["suprizedPose", "crossarms"]:
            "images/antagonists/Astart Officers/Astarto-Suzumite Hyspaspist Angry Mouth.webp"
            xpos -200
        attribute angryMouth if_any["commanding","commnadingShield","chuckingPose"]:
            "images/antagonists/Astart Officers/Astarto-Suzumite Hyspaspist Angry Mouth.webp"

    group eyes:
        attribute neutralEyes default if_any["basic"]: #430 left 2 nose
            "images/antagonists/Astart Officers/Astarto-Suzumite Hyspaspist Neutral Eyes.webp"
        attribute neutralEyes default if_any["suprizedPose", "crossarms"]: #600 left edge 2 nose
            "images/antagonists/Astart Officers/Astarto-Suzumite Hyspaspist Neutral Eyes.webp"
            xpos 165
        attribute neutralEyes default if_any["commanding","commnadingShield","chuckingPose"]: #800 left 2 nose
            "images/antagonists/Astart Officers/Astarto-Suzumite Hyspaspist Neutral Eyes.webp"
            xpos 365
        
        attribute meanEyes if_any["basic"]:
            "images/antagonists/Astart Officers/Astarto-Suzumite Hyspaspist Angry Eyes.webp"
            xpos -365
        attribute meanEyes if_any["suprizedPose", "crossarms"]:
            "images/antagonists/Astart Officers/Astarto-Suzumite Hyspaspist Angry Eyes.webp"
            xpos -200
        attribute meanEyes if_any["commanding","commnadingShield","chuckingPose"]:
            "images/antagonists/Astart Officers/Astarto-Suzumite Hyspaspist Angry Eyes.webp"

        
        attribute sadEyes if_any["basic"]:
            "images/antagonists/Astart Officers/Astarto-Suzumite Hyspaspist.webp"
        attribute sadEyes if_any["suprizedPose", "crossarms"]:
            "images/antagonists/Astart Officers/Astarto-Suzumite Hyspaspist.webp"
            xpos 165
        attribute sadEyes if_any["commanding","commnadingShield","chuckingPose"]:
            "images/antagonists/Astart Officers/Astarto-Suzumite Hyspaspist.webp"
            xpos 365
        
        attribute closedEyes if_any["basic"]: #same as neutral eyes
            "images/antagonists/Astart Officers/Astarto-Suzumite Hyspaspist Closed Eyes.webp"
        attribute closedEyes if_any["suprizedPose", "crossarms"]:
            "images/antagonists/Astart Officers/Astarto-Suzumite Hyspaspist Closed Eyes.webp"
            xpos 165
        attribute closedEyes if_any["commanding","commnadingShield","chuckingPose"]:
            "images/antagonists/Astart Officers/Astarto-Suzumite Hyspaspist Closed Eyes.webp"
            xpos 365
    

    

#MiniBosses
    #Seige Ladder Astart
image siegeLadderAstart = "images/antagonists/Mini-Bosses/Astart Siege Wheel Ladder.webp"
image siegeLadderAstartFlames = "images/antagonists/Mini-Bosses/Astart Siege Wheel Ladder Destroyed.webp"

    #gilgamata
image gilgamataDuckBite = "images/antagonists/Mini-Bosses/Gilgamata Duckbite.webp"
image gilgamataDuckBiteJump = "images/antagonists/Mini-Bosses/Gilgamata Duckbite Jumping.webp"
image gilgamataDuckBiteDead = "images/antagonists/Mini-Bosses/Gilgamata Duckbite dead.webp"

    #Female Astart Summoner
image astartSummerFemale = "images/antagonists/Mini-Bosses/Astart Summoner Female1.webp"
image astartSummerFemaleSummoning = "images/antagonists/Mini-Bosses/Astart Summoner Female1 summoning.webp"
image astartSummerFemaleGetU = "images/antagonists/Mini-Bosses/Astart Summoner Female1 gonna get u.webp"
image astartSummerFemaleCumHere = "images/antagonists/Mini-Bosses/Astart Summoner Female1 come here.webp"
image astartSummerFemaleDead = "images/antagonists/Mini-Bosses/Astart Summoner Female1 dead.webp"
image astartSummerFemaleAraAra = "images/antagonists/Mini-Bosses/Astart Summoner Female1 ara ara.webp"

    #Shata key lady / Muwa
        #Antagonistic
image muwaHehe = "images/Enemies/Shata and Ssatu/Shata key lady Hehe.webp"
image muwaYummy = "images/Enemies/Shata and Ssatu/Shata key lady yummy.webp"
image muwaGetEm = "images/Enemies/Shata and Ssatu/Shata key lady get em boys.webp"
image muwaScared = "images/Enemies/Shata and Ssatu/Shata key lady scared.webp"
image muwaKnifeyGot2Her = "images/Enemies/Shata and Ssatu/Shata key lady lying on bench Stabbed.webp"
image muwaRanThrough = "images/Enemies/Shata and Ssatu/Shata key lady lying on bench Sword.webp"
image muwaKnockedOut = "images/Enemies/Shata and Ssatu/Shata key lady lying on bench.webp"
        #freindly
image muwaNeutralHappy = "images/NPCs/Jamesia/Kwortix/Kwortix Mine/Shata leader Neutral Happy.webp"
image muwaHappy = "images/NPCs/Jamesia/Kwortix/Kwortix Mine/Shata leader Happy.webp"
image muwaUpMiniHappy = "images/NPCs/Jamesia/Kwortix/Kwortix Mine/Shata leady up slightly happy.webp"
image muwaUpNeutralHappy = "images/NPCs/Jamesia/Kwortix/Kwortix Mine/Shata leady up neutral happy.webp" 
image muwaGiving = "images/NPCs/Jamesia/Kwortix/Kwortix Mine/Shata lady giving item.webp"
image muwaByeBye = "images/NPCs/Jamesia/Kwortix/Kwortix Mine/Shata lady byebye.webp"
image muwaInviting = "images/NPCs/Jamesia/Kwortix/Kwortix Mine/Shata leady inviting.webp"
image muwaInsisting = "images/NPCs/Jamesia/Kwortix/Kwortix Mine/Shata leady isisting.webp"

image muwaStandingHappy = "images/NPCs/Jamesia/Kwortix/Kwortix Mine/Shata leader standing happy.webp"
image muwaStandingByeBye = "images/NPCs/Jamesia/Kwortix/Kwortix Mine/Shata leader standing bye.webp"
image muwaStandingInviting = "images/NPCs/Jamesia/Kwortix/Kwortix Mine/Shata leader standing inviting.webp"
image muwaStandingNeutralHappy = "images/NPCs/Jamesia/Kwortix/Kwortix Mine/Shata leader standing neutral happy.webp"
image muwaStandingSad = "images/NPCs/Jamesia/Kwortix/Kwortix Mine/Shata leader standing sad.webp"

image muwaSlaveHappy = "images/NPCs/Jamesia/Kwortix/Kwortix Mine/Shata slave leader happy.webp"
image muwaSlaveNeutralHappy = "images/NPCs/Jamesia/Kwortix/Kwortix Mine/Shata slave leader neutral happy.webp"
image muwaSlaveSad = "images/NPCs/Jamesia/Kwortix/Kwortix Mine/Shata slave leader Sad.webp"

image muwaChoke = "images/Xerxes and Shata Lady Choking.webp"
image muwaStab1 = "images/Xerxes and Shata Lady Stabby1.webp"
image muwaStab2 = "images/Xerxes and Shata Lady StabbyIn.webp"
image muwaStab3 = "images/Xerxes and Shata Lady StabbyOut.webp"
image muwaStabSword = "images/Xerxes and Shata Lady Sword Stab.webp"
image muwaChuck = "images/Xerxes and Shata Lady Chucking.webp"

#Chwitaza
image chwitazaA = "images/antagonists/Mini-Bosses/Chwitaza.webp"
image chwitazaB = "images/antagonists/Mini-Bosses/Chwitaza b.webp"
image chwitazaBackground = "images/antagonists/Mini-Bosses/Chwitaza Background.webp"
image chwitazaGetEm = "images/antagonists/Mini-Bosses/Chwitaza Get Em.webp"
image chwitazaHehe = "images/antagonists/Mini-Bosses/Chwitaza Heheh.webp"
image chwitazaMad = "images/antagonists/Mini-Bosses/Chwitaza Mad.webp"
image chwitazaSlave = "images/antagonists/Mini-Bosses/Chwitaza Slave.webp"
image chwitazaDead = "images/antagonists/Mini-Bosses/Chwitaza Dead.webp"

#Ahrimaniom
image ahrimaniomMK5UnderConstruction1 = "images/antagonists/Ahrimaniom/Ahrimaniom under construction.webp"
image ahrimaniomMK5UnderConstruction2 = "images/antagonists/Ahrimaniom/Ahrimaniom under construction 2.webp"

image ahrimaniomMK4 = "images/antagonists/Ahrimaniom/Ahrimaniom MK4.webp"
image ahrimaniomMK4Shrouded = "images/antagonists/Ahrimaniom/Ahrimaniom MK4 Shrouded.webp"



#Cult of Ahriman
image hizwenaT1 = "images/antagonists/Cult of Ahriman/Hizwena Teir 1.webp"
image hizwenaT1Yeah = "images/antagonists/Cult of Ahriman/Hizwena Teir 1 Yeah.webp"
image hizwenaT1Praising = "images/antagonists/Cult of Ahriman/Hizwena Teir 1 Praising.webp"
image hizwenaT2Commanding34 = "images/antagonists/Cult of Ahriman/Hizwena Teir 1 3-4 Commanding.webp"

image ahriteT1CultistMale = "images/antagonists/Cult of Ahriman/ahrite culist teir 1 Foward.webp"
image ahriteT1CultistMale34 = "images/antagonists/Cult of Ahriman/ahrite culist teir 1.webp"
image ahriteT1CultistMalePraising = "images/antagonists/Cult of Ahriman/ahrite culist teir 1 Praising.webp"


#Zardossatu
    #Versaniz
layeredimage versaniz:
    group poese:
        attribute armored default: #900 1600
            "images/antagonists/Versaniz III/Versaniz Armored.webp"
        attribute armoredPointy: # ditto
            "images/antagonists/Versaniz III/Versaniz Armored Pointy.webp"
        attribute armoredThink:
            "images/antagonists/Versaniz III/Versaniz Armored Thinking.webp"
        attribute angryPose:
            "images/antagonists/Versaniz III/Versaniz Armored Angry Pose.webp"
        attribute nekked: # 700 1400
            "images/antagonists/Versaniz III/Versaniz Nekked.webp"
    
    group eyes:
        attribute meanEyes if_not["nekked"]:
            "images/antagonists/Versaniz III/Versaniz Armored Mean Eyes.webp"
        attribute meanEyes if_any["nekked"]:
            "images/antagonists/Versaniz III/Versaniz Mean Eyes.webp"
        attribute hornyEyes if_not["nekked"]:
            "images/antagonists/Versaniz III/Versaniz Armored Horny Eyes.webp"
        attribute hornyEyes if_any["nekked"]:
            "images/antagonists/Versaniz III/Versaniz Horny eyes.webp"
        attribute sadEyes if_not["nekked"]:
            "images/antagonists/Versaniz III/Versaniz Armored Sad Eyes.webp"
        attribute sadEyes if_any["nekked"]:
            "images/antagonists/Versaniz III/Versaniz Sad Eyes.webp"

    group mouths:

        attribute angryMouth if_not["nekked"]:
            "images/antagonists/Versaniz III/Versaniz Arngry Mouth.webp"
        attribute angryMouth if_any["nekked"]:
            "images/antagonists/Versaniz III/Versaniz Arngry Mouth.webp"
            xpos -200 ypos -200

        attribute frowning if_not["nekked"]:
            "images/antagonists/Versaniz III/Versaniz Frown Mouth.webp"
        attribute frowning if_any["nekked"]:
            "images/antagonists/Versaniz III/Versaniz Frown Mouth.webp"
            xpos -200 ypos -200

        attribute happyMouth if_not["nekked"]:
            "images/antagonists/Versaniz III/Versaniz Happy mouth.webp"
        attribute happyMouth if_any["nekked"]:
            "images/antagonists/Versaniz III/Versaniz Happy mouth.webp"
            xpos -200 ypos -200

        attribute meanHappyMouth if_not["nekked"]:
            "images/antagonists/Versaniz III/Versaniz Mean Happy Mouth.webp"
        attribute meanHappyMouth if_any["nekked"]:
            "images/antagonists/Versaniz III/Versaniz Mean Happy Mouth.webp"
            xpos -200 ypos -200

        attribute OMouth if_not["nekked"]:
            "images/antagonists/Versaniz III/Versaniz O Mouth.webp"
        attribute OMouth if_any["nekked"]:
            "images/antagonists/Versaniz III/Versaniz O Mouth.webp"
            xpos -200 ypos -200

    group cheeks:
        attribute blush if_not["nekked"]:
            "images/antagonists/Versaniz III/Versaniz Blush.webp"
        attribute blush if_any["nekked"]:
            "images/antagonists/Versaniz III/Versaniz Blush.webp"
            xpos -200 ypos -200

image versanizBoinkingSiayusi = "images/antagonists/Versaniz III/Versaniz boinking Siayusi.webp"
    #Versaniz's GirlFriends
layeredimage siayusi:
    group poses:
        attribute front default:
            "images/antagonists/Versaniz III/Vasanizs gfs/Siayusi.webp"
        attribute back:
            "images/antagonists/Versaniz III/Vasanizs gfs/Siayusi 34 back.webp"
    
    group eyes:
        attribute hornyEyes if_any["back"]:
            "images/antagonists/Versaniz III/Vasanizs gfs/Siayusi 34 back horny eyes.webp"

        attribute meanEyes if_any["front"]:
            "images/antagonists/Versaniz III/Vasanizs gfs/Siayusi Mean eyes.webp"
        
        attribute sadEyes if_any["back"]:
            "images/antagonists/Versaniz III/Vasanizs gfs/Siayusi 34 back sad eyes.webp"

    group mouths:
        attribute happyMouth if_any["front"]:
            "images/antagonists/Versaniz III/Vasanizs gfs/Siayusi Happy Mouth.webp"
        attribute happyMouth if_any["back"]:
            "images/antagonists/Versaniz III/Vasanizs gfs/Siayusi 34 Happy Mouth.webp"
        attribute OMouth if_any["back"]:
            "images/antagonists/Versaniz III/Vasanizs gfs/Siayusi 34 back O Mouth.webp"


    group cheeks:
        attribute blush if_any["front"]:
            "images/antagonists/Versaniz III/Vasanizs gfs/Siayusi blush.webp"
        attribute blush if_any["back"]:
            "images/antagonists/Versaniz III/Vasanizs gfs/Siayusi 34 back blush.webp"

    group pupils:
        attribute bigPupils if_any["front"]:
            "images/antagonists/Versaniz III/Vasanizs gfs/Siayusi Big Pupils.webp"

layeredimage muiba:
    group poses:
        attribute basic default:
            "images/antagonists/Versaniz III/Vasanizs gfs/Muiba.webp"
    
    group mouths:
        attribute neutralHappy default:
            "images/antagonists/Versaniz III/Vasanizs gfs/Muiba neutral Happy Mouth.webp"
        attribute happy:
            "images/antagonists/Versaniz III/Vasanizs gfs/Muiba Happy Mouth.webp"
        attribute OMouth:
            "images/antagonists/Versaniz III/Vasanizs gfs/Muiba OMouth.webp"

    group eyes:
        attribute neutralEyes default:
            "images/antagonists/Versaniz III/Vasanizs gfs/Muiba Neutral Eyes.webp"
        attribute meanEyes:
            "images/antagonists/Versaniz III/Vasanizs gfs/Muiba Mean Eyes.webp"
        attribute sadEyes:
            "images/antagonists/Versaniz III/Vasanizs gfs/Muiba Sad Eyes.webp"

    group blush:
        attribute blush:
            "images/antagonists/Versaniz III/Vasanizs gfs/Muiba Blush.webp"

    group pupils:
        attribute normalPupils default:
            "images/antagonists/Versaniz III/Vasanizs gfs/Muiba Normal Pupils.webp"
        attribute thinPupils:
            "images/antagonists/Versaniz III/Vasanizs gfs/Muiba Shock Pupils.webp"
        attribute widePupils:
            "images/antagonists/Versaniz III/Vasanizs gfs/Muiba Cute Pupils.webp"

    group ears:
        attribute neutralEars default:
            "images/antagonists/Versaniz III/Vasanizs gfs/Muiba neutral Happy Mouth.webp"
        attribute smadEars:
            "images/antagonists/Versaniz III/Vasanizs gfs/Muiba Smad Ears.webp"


#junatu gf
    #Zagzhino
layeredimage zagzhino:

    group poses:
        attribute front default:
            "images/antagonists/Zagzhino/Zagzhino.webp"
        attribute twoFists:
            "images/antagonists/Zagzhino/Zagzhino 2 Fist.webp"
        attribute captured:
            "images/antagonists/Zagzhino/Zagzhino Captured.webp"

    group eyes:
        attribute neutralEyes default:
            "images/antagonists/Zagzhino/Zagzhino Neutral Eyes.webp"

        attribute meanEyes:
            "images/antagonists/Zagzhino/Zagzhino Angry Eyes.webp"

        attribute sadEyes:
            "images/antagonists/Zagzhino/Zagzhino Sad Eyes.webp"
        
        attribute closedEyes:
            "images/antagonists/Zagzhino/Zagzhino Eyes Closed.webp"

    group mouths:  
        attribute neutralHappy default:
            "images/antagonists/Zagzhino/Zagzhino Nutral Happy Mouth.webp"

        attribute angryMouth:
            "images/antagonists/Zagzhino/Zagzhino Angry mouth.webp"

        attribute frown:
            "images/antagonists/Zagzhino/Zagzhino Frown.webp"

        attribute sadMouth:
            "images/antagonists/Zagzhino/Zagzhino Sad Mouth.webp"

        attribute miniHappyMouth:
            "images/antagonists/Zagzhino/Zagzhino Mini Happy Mouth.webp"

        attribute happyMouth:   
            "images/antagonists/Zagzhino/Zagzhino Happy Mouth.webp"
    
    #tuksoi
layeredimage tuksoi:
    group poses:
        attribute basic default:
            "images/antagonists/Zagzhino/Zagzhino's Goons/Tuksoi.webp"
        attribute box:
            "images/antagonists/Zagzhino/Zagzhino's Goons/Tuksoi With Box.webp"
        attribute shocked:
            "images/antagonists/Zagzhino/Zagzhino's Goons/Tuksoi Shocked.webp"

    group mouths:
        attribute neutralHappyMouth default:
            "images/antagonists/Zagzhino/Zagzhino's Goons/Tuksoi Neutral Happy Mouth.webp"
        attribute OMouth:
            "images/antagonists/Zagzhino/Zagzhino's Goons/Tuksoi OMouth.webp"
        attribute deltaMouth:
            "images/antagonists/Zagzhino/Zagzhino's Goons/Tuksoi Delta Mouth.webp"

    group eyes:
        attribute neutralEyes default:
            "images/antagonists/Zagzhino/Zagzhino's Goons/Tuksoi Neutral Eyes.webp"
        attribute sadEyes:
            "images/antagonists/Zagzhino/Zagzhino's Goons/Tuksoi Sad Eyes.webp"

layeredimage ssatuCarrier:
    group poses:
        attribute carrying default:
            "images/NPCs/Ssatu and Shata Cilivians/ssatu carrier.webp"
    group eyes:
        attribute neutralEyes default:
            "images/NPCs/Ssatu and Shata Cilivians/ssatu carrier.webp"
        attribute meanEyes:
            "images/NPCs/Ssatu and Shata Cilivians/ssatu carrier.webp"
    group mouths:
        attribute annoyedMouth default:
            "images/NPCs/Ssatu and Shata Cilivians/ssatu carrier.webp"
        attribute OMouth:
            "images/NPCs/Ssatu and Shata Cilivians/ssatu carrier.webp"

layeredimage shataCarrier:
    group poses:
        attribute carrying default:
            "images/NPCs/Ssatu and Shata Cilivians/shata carrier.webp"
    group eyes:
        attribute neutralEyes default:
            "images/NPCs/Ssatu and Shata Cilivians/shata carrier Neutral Eyes.webp"
        attribute meanEyes:
            "images/NPCs/Ssatu and Shata Cilivians/shata carrier Mean Eyes.webp"
    group mouths:
        attribute deltaMouth default:
            "images/NPCs/Ssatu and Shata Cilivians/shata carrier Delta Mouth.webp"
        attribute happyMouth:
            "images/NPCs/Ssatu and Shata Cilivians/shata carrier happy mouth.webp"
        attribute OMouth:
            "images/NPCs/Ssatu and Shata Cilivians/shata carrier OMouth.webp"
#Bosses

#Saporius
image saporiusRising = "images/antagonists/Key Guardians/Saporius/Saporius Rising.webp"
image saporiusGroundedLazer = "images/antagonists/Key Guardians/Saporius/Saporius Grounded Lazer.webp"
image saporiusMeleeFlying = "images/antagonists/Key Guardians/Saporius/Saporius Melee Flying.webp"
image saporiusAHHHH = "images/antagonists/Key Guardians/Saporius/Saporius ahh fall.webp"
image saporiusROAR = "images/antagonists/Key Guardians/Saporius/Saporius Intro Roar!!.webp"

#Modonon
image modononSleeping = "images/antagonists/Key Guardians/Modonon/Modonon Sleeping Front.webp"
image modononSleepingSide = "images/antagonists/Key Guardians/Modonon/Modonon Sleeping Side.webp"
image modononSleepingBack = "images/antagonists/Key Guardians/Modonon/Modonon Sleeping Back.webp"
image modononAwake = "images/antagonists/Key Guardians/Modonon/Modonon Waking Up.webp"
image modononDefeated = "images/antagonists/Key Guardians/Modonon/Modonon Defeated Front Mouth closed.webp"
image modononDefeatedOpened = "images/antagonists/Key Guardians/Modonon/Modonon Defeated Front.webp"
image modononSideAngry = "images/antagonists/Key Guardians/Modonon/Modonon Side Angry.webp"
image modononSideAngryUp = "images/antagonists/Key Guardians/Modonon/Modonon Side Angry up.webp"
image modononSideExploded = "images/antagonists/Key Guardians/Modonon/Modonon Side Exploded.webp"
image modononSideXerxSmash = "images/antagonists/Key Guardians/Modonon/Modonon Side Exploded Crystal Xerxes.webp"
image modononSideTesiSmash = "images/antagonists/Key Guardians/Modonon/Modonon Side Exploded Crystal Tesipiz.webp"
image modononBackExplode = "images/antagonists/Key Guardians/Modonon/Modonon Back Crystal Exploded.webp"
image modononBack = "images/antagonists/Key Guardians/Modonon/Modonon Back.webp"
image modononSideTail1 = "images/antagonists/Key Guardians/Modonon/Modonon Side Shakey.webp"
image modononSideTail2 = "images/antagonists/Key Guardians/Modonon/Modonon Side Shakey 2.webp"
image modononSideTail3 = "images/antagonists/Key Guardians/Modonon/Modonon Side Shakey 3.webp"
image modononAngry = "images/antagonists/Key Guardians/Modonon/Modonon Angry.webp"
image modononAngryAttack = "images/antagonists/Key Guardians/Modonon/Modonon Angry Attack.webp"
image modononMonstergirl = "images/antagonists/Key Guardians/Modonon/Modonon monstergirl sfw.webp"
image modononTailAttack = "images/antagonists/Key Guardians/Modonon/Modonon Tail Attack.webp"
image modononKnockedOutBack = "images/antagonists/Key Guardians/Modonon/Modonon Unconshince Back.webp"
image modononExplodedFront = "images/antagonists/Key Guardians/Modonon/Modonon Exploded Front.webp"
image modononExplodedSide = "images/antagonists/Key Guardians/Modonon/Modonon Unconshince Side Side.webp"
image modononGutted = "images/antagonists/Key Guardians/Modonon/Modonon Unconshince Side gutted.webp"

#sakuna
image sakunaSand = "images/antagonists/Key Guardians/Sakuna/Sakuna Side In Sand.webp"
image sakunaSandOpen = "images/antagonists/Key Guardians/Sakuna/Sakuna Side In Sand OPen Mouth.webp"
image sakunaSandVore = "images/antagonists/Key Guardians/Sakuna/Sakuna Side In Sand Eating Minobite.webp"

image sakunaSide = "images/antagonists/Key Guardians/Sakuna/Sakuna Side.webp"

image sakunaAss = "images/antagonists/Key Guardians/Sakuna/Sakuna Assss.webp"
image sakunaSpin = "images/antagonists/Key Guardians/Sakuna/Sakuna Spin.webp"
image sakunaExploded = "images/antagonists/Key Guardians/Sakuna/Sakuna Da Fish exploded.webp"
image sakunaExpliding = "images/antagonists/Key Guardians/Sakuna/Sakuna Da Fish exploding.webp"

image sakunaKnockedOut = "images/antagonists/Key Guardians/Sakuna/Sakuna Da Fish Unoncenice.webp"
image sakunaFat = "images/antagonists/Key Guardians/Sakuna/Sakuna Da Fish Wide.webp"
image sakunaBalooned = "images/antagonists/Key Guardians/Sakuna/Sakuna Da Fish Inflated.webp"
image sakunaFish = "images/antagonists/Key Guardians/Sakuna/Sakuna Da Fish Mouth CLosed.webp"

image sakunaFromAbove = "images/antagonists/Key Guardians/Sakuna/Sakuna From Above.webp"
image sakunaFlopDown = "images/antagonists/Key Guardians/Sakuna/Sakuna Flop Down.webp"

image vomitss = Tile("images/antagonists/Key Guardians/Sakuna/Sakuna Vomit Texture.webp")

image sakunaEatFalcobite = "images/antagonists/Key Guardians/Sakuna/Sakuna Da Fish Head Eating Falcobitez.webp"
image sakunaEatJakalbite = "images/antagonists/Key Guardians/Sakuna/Sakuna Da Fish Head Eating Jakalbite.webp"
image sakunaEatLizardBite = "images/antagonists/Key Guardians/Sakuna/Sakuna Da Fish Head Eating Lizardbite.webp"
image sakunaEatMinobite = "images/antagonists/Key Guardians/Sakuna/Sakuna Da Fish Head Eating Minobite.webp"
image sakunaOpenMouth = "images/antagonists/Key Guardians/Sakuna/Sakuna Da Fish Head.webp"

#Monsters Sakuna Ate
image deadEatenFalcobite = "images/Enemies/astartes goons/Dead Eaten Falcobite.webp"
image deadEatenJakalbite = "images/Enemies/astartes goons/Dead Eaten Jakalbite.webp"
image deadEatenLizardbite = "images/Enemies/astartes goons/Dead Eaten Lizardbite.webp"
image deadEatenMinobite = "images/Enemies/astartes goons/Dead Eaten Minobite.webp"


#Haidrasyon

image hydrasyonInactive = "images/antagonists/Sword Guardian/Hydrasyon Inactive.webp"
image hydrasyonInactiveSnakes = "images/antagonists/Sword Guardian/Hydrasyon SnakeS Inactive.webp"

image hydrasyonActive = "images/antagonists/Sword Guardian/Hydrasyon Active Attack.webp"
image hydrasyonActiveNoSword = "images/antagonists/Sword Guardian/Hydrasyon Body No Sowrd.webp"
image hydrasyonMissleLaunch = "images/antagonists/Sword Guardian/Hydrasyon Active Missle Lunch1.webp"
image hydrasyonActiveSide = "images/antagonists/Sword Guardian/Hydrasyon Side.webp"
image hydrasyonActiveBack = "images/antagonists/Sword Guardian/Hydrasyon Back.webp"
image hydrasyonActiveSnakes = "images/antagonists/Sword Guardian/Hydrasyon SnakeS.webp"

image xerxesFacehuggingSnakes = "images/antagonists/Sword Guardian/xerxes facehugging Hydrasyon.webp"
image xerxesRidingSnakes = "images/antagonists/Sword Guardian/xerxes hugging Hydrasyon Snake.webp"
image xerxesHitBySnakeBlast = "images/antagonists/Sword Guardian/xerxes hugging Hydrasyon Snake Hit.webp"

image isofishFront = "images/antagonists/Sword Guardian/isofish front.webp"
image isofish34 = "images/antagonists/Sword Guardian/isofish 34.webp"
image isofishSide = "images/antagonists/Sword Guardian/isofish side.webp"
image isofishBack = "images/antagonists/Sword Guardian/isofish back.webp"




#protagonists
#Xerxes

image neutralHappyXerxes = "images/Protagonists/Xerxes/Neutral Happy Xerxes.webp"
image happyXerx = "images/Protagonists/Xerxes/Happy Xerxes.webp"
image happyXerxArmored = "images/Protagonists/Xerxes/Happy Xerxes Armored.webp"
image xerxArmsOutHappyArmored = "images/Protagonists/Xerxes/Happy Xerxes armored Arms out.webp"
image xerx1ArmOutHappyArmored = "images/Protagonists/Xerxes/Happy Xerxes armored one hand out.webp"
image slightlyHappyXerxes = "images/Protagonists/Xerxes/Slightly Happy Xerxes.webp"
image xerxNoWeGoodArmored = "images/Protagonists/Xerxes/No we good Happy Xerxes Armored.webp"

image miniSadXerxes = "images/Protagonists/Xerxes/Neutral Sad Xerxes.webp"
image sadXerxesNoHat = "images/Protagonists/Xerxes/Sad Xerxes No Hat.webp"
image scaredXerxesNoHat = "images/Protagonists/Xerxes/Scared Xerxes No Hat.webp"

image madsitterXerx = "images/Protagonists/Xerxes/Angry Sitting Xerxes2.webp"
image madNoHatXerx = "images/Protagonists/Xerxes/Mad Xerxes No Hat.webp"
image angrysitXerx = "images/Protagonists/Xerxes/Angry Sitting Xerxes.webp"
image annoyedsitXerx = "images/Protagonists/Xerxes/Annoyed Sitting Xerxes.webp"
image annoyedXerx = "images/Protagonists/Xerxes/Annoyed Xerxes.webp"
image slightlyAnnoyedXerx = "images/Protagonists/Xerxes/Slightly Annoyed Xerxes.webp"
image happysitXerx = "images/Protagonists/Xerxes/Happy Sitting Xerxes.webp"
image thinksitXerx = "images/Protagonists/Xerxes/Thinking Sitting Xerxes.webp"
image thinkXerx = "images/Protagonists/Xerxes/Thinking Xerxes.webp"
image xerxHappyGreet = "images/Protagonists/Xerxes/Happy Xerxes Greeting.webp"
image xerxHappyGreetArmored = "images/Protagonists/Xerxes/Xerxes 3-4 Armored Happy Greet.webp"
image xerxSuprized = "images/Protagonists/Xerxes/Xerxes Suprized.webp"
image xerxSuprizedArmored = "images/Protagonists/Xerxes/Xerxes Suprized Armored.webp"

image xerxYeah = "images/Protagonists/Xerxes/Xerxes Yeah.webp"
image xerxYeahArmored = "images/Protagonists/Xerxes/Xerxes Yeah Armored.webp"
image xerxYeahWithSoAM = "images/Protagonists/Xerxes/Xerxes Yeah with SoAM.webp"
image xerxYeahArmoredWithSoAM = "images/Protagonists/Xerxes/Xerxes Yeah Armored SoAM.webp"

image xerxWithChargedSoAM = "images/Protagonists/Xerxes/Xerxes Neutral Happy Soam.webp"

image xerxNeutralSuprizedUnarmored = "images/Protagonists/Xerxes/Neutral suprized Xerxes.webp"
image xerxNeutralSuprized = "images/Protagonists/Xerxes/Neutral suprized Xerxes Armored.webp"

image xerxMarchFowardArmed = "images/Protagonists/Xerxes/Xerxes walking determined armored.webp"
image xerxMarchFowardSoAM = "images/Protagonists/Xerxes/Xerxes walking determined armored SoAM.webp"
image xerxMarchFowardSoAMYeah = Composite( (1400 , 1400 ) , (0,0) , "images/Protagonists/Xerxes/Xerxes walking determined armored SoAM.webp" , (0,0) , "images/Protagonists/Xerxes/Xerxes walking determined armored SoAM Yeah Face.webp")

image xerxHehehArmoredArmed1 = "images/Protagonists/Xerxes/Xerxes Heheh Armored Armed v1.webp"
image xerxHehehArmoredArmed2 = "images/Protagonists/Xerxes/Xerxes Heheh Armored Armed v2.webp"
image xerxSwordPointArmored = "images/Protagonists/Xerxes/Xerxes Heheh Armored Armed Stabbing Foward.webp"
image xerxSoAMPointArmored = "images/Protagonists/Xerxes/Xerxes Heheh Armored Armed Stabbing Foward SoAM.webp"
image xerxSoAMPointArmoredAngry = Composite( (1200 , 1500 ) , (0,0) , "images/Protagonists/Xerxes/Xerxes Heheh Armored Armed Stabbing Foward SoAM.webp" , (0,0) , "images/Protagonists/Xerxes/Xerxes Armored Armed Stabbing Foward Angry Face.webp")
image xerxOoahArmored = "images/Protagonists/Xerxes/Xerxes ooah Armored.webp"


image neutralHappyXerxPointing = "images/Protagonists/Xerxes/Neutral Happy Xerxes Pointing.webp"

image trueNeutralXerxesArmored = "images/Protagonists/Xerxes/True Neutral Xerxes Armored.webp"
image neutralXerxes = "images/Protagonists/Xerxes/Neutral Xerxes.webp"
image neutralXerxesArmored = "images/Protagonists/Xerxes/Neutral Xerxes Armored.webp"
image neutralHappyXerxesArmored = "images/Protagonists/Xerxes/Neutral Happy Xerxes Armored.webp"
image xerxArmoredHappyGreet = "images/Protagonists/Xerxes/Happy Xerxes Greeting armored.webp"

image xerxPointBackArmored = "images/Protagonists/Xerxes/Neutral Happy Xerxes Pointing Back armored.webp"
image xerxPointArmored = "images/Protagonists/Xerxes/Commanding Xerxes Pointing armored.webp"
image xerxPointArmoredArmed = "images/Protagonists/Xerxes/Commanding Angry Xerxes Pointing armored armed.webp"

image xerxArmorShocked = "images/Protagonists/Xerxes/slightly shocked Xerxes Pointing Back armored.webp"
image xerxArmoredPoint = "images/Protagonists/Xerxes/Commanding Xerxes Pointing armored.webp"
image xerxArmoedCharge = "images/Protagonists/Xerxes/Xerxes Atackking armored v1.webp"
image xerxJumpUp = "images/Protagonists/Xerxes/Xerxes jump1.webp"
image xerArmoedJumpUp = "images/Protagonists/Xerxes/Xerxes jump1 armored v1.webp"
image xerxArmoredJumpUpSoam = "images/Protagonists/Xerxes/Xerxes jump1 armored Soam.webp"
image xerxArmoedJumpDown = "images/Protagonists/Xerxes/Xerxes jump2 armored.webp"
image xerxLandingSword = "images/Protagonists/Xerxes/Armored landing Xerxes v1.webp"
image xerxLandingBow = "images/Protagonists/Xerxes/Armored landing Xerxes v1 2.webp"

image xerxAnnoyedAmored = "images/Protagonists/Xerxes/Annoyed Xerxes Armored.webp"
image xerxMadArmed = "images/Protagonists/Xerxes/Xerxes Angry Armed v1.webp"
image xerxMadArmedArmored = "images/Protagonists/Xerxes/Xerxes Angry Armored Armed v1.webp"
image xerxMadArmed2 = "images/Protagonists/Xerxes/Xerxes Angry Armed v2.webp"
image xerxMadArmed2Armored = Composite( (800,1400),(0,0), "images/Protagonists/Xerxes/Xerxes Suprized Armored Armed v2.webp" , (0,0) ,"images/Protagonists/Xerxes/Xerxes Angry Armored Armed v2.webp" )
image xerxLitteMadArmed = "images/Protagonists/Xerxes/Xerxes slingly Angry Armed v1.webp"
image xerxLitteMadArmed2 = "images/Protagonists/Xerxes/Xerxes slingly Angry Armed v2.webp"

image xerxAngry = "images/Protagonists/Xerxes/Angry Xerxes Armored.webp"
image xerxAngrier = "images/Protagonists/Xerxes/Angrier Xerxes Armored.webp"
image xerxAngryMouthOpen = "images/Protagonists/Xerxes/Angry Xerxes Armored2.webp"

image xerxRunningConsuredArmored = "images/Protagonists/Xerxes/Xerxes running consured armored.webp"
image xerxRunningScaredArmored = "images/Protagonists/Xerxes/Xerxes running scared armored.webp"

image xerxGettingSucked:
    "images/Protagonists/Xerxes/Xerxes 3-4 Eaten By Sand.webp" with Dissolve(0.1)
    pause 0.2
    "images/Protagonists/Xerxes/Behind Xerxes Armored in Sand.webp" with Dissolve(0.1)
    pause 0.2
    repeat

image xerxHoldingBombAndDeadMonster = "images/Protagonists/Xerxes/Xerxes holding Bomb and Dead Jakalbite Armored.webp"
image xerxMakingMonsterBomb:
    "images/Protagonists/Xerxes/Xerxes holding Bomb and Dead Jakalbite Armored.webp"
    pause 0.3
    "images/Protagonists/Xerxes/Xerxes holding Bomb in Dead Jakalbite Armored.webp"
    pause 0.5
    "images/Protagonists/Xerxes/Xerxes holding Monster Bomb Armored.webp"
    xzoom -1.0

image xerxesHoldingMonsterBomb = "images/Protagonists/Xerxes/Xerxes holding Monster Bomb Armored.webp"

image xerxGrappleUpArmored = "images/Protagonists/Xerxes/Neutral Happy Xerxes Grapple Point Up.webp"
image xerxGrappleUpFlyBackArmored = "images/Protagonists/Xerxes/Behind Xerxes Grapple up Armored.webp"

image xerxSuprizedArmed = "images/Protagonists/Xerxes/Xerxes Suprized Armed v1.webp"
image xerxSuprizedArmed2 = "images/Protagonists/Xerxes/Xerxes Suprized Armed v2.webp"
image xerxSuprizedArmedArmored = "images/Protagonists/Xerxes/Xerxes Suprized Armored Armed v1.webp"
image xerxSuprizedArmedArmored2 = "images/Protagonists/Xerxes/Xerxes Suprized Armored Armed v2.webp"

image xerxHoldingKey = "images/Protagonists/Xerxes/Xerxes Holding key.webp"
image xerxHoldingRedKey = "images/Protagonists/Xerxes/Xerxes holding red key armored.webp"
image xerxZwotiKeyArmored = "images/Protagonists/Xerxes/Xerxes holding key armored.webp"
image xerxDaggerArmored = "images/Protagonists/Xerxes/Xerxes holding dagger armored.webp"
image xerxKwortixKeyBloody = "images/Protagonists/Xerxes/Xerxes holding key armored bloody.webp"

image xerxFistUp = "images/Protagonists/Xerxes/Xerxes Holding fist.webp"
image xerxFistUpArmored = "images/Protagonists/Xerxes/Xerxes holding fist armored.webp"
image xerxFistForward = "images/Protagonists/Xerxes/Xerxes Holding fist Foward.webp"
image xerxFistForwardArmored = "images/Protagonists/Xerxes/Xerxes holding fist foward armored.webp"

image xerx3410070Power = "images/Protagonists/Xerxes/Xerxes 3-4 unarmored 100-70.webp"

image xerx34BowStart = "images/Protagonists/Xerxes/Xerxes 3-4 with bow.webp"
image xerx34BowStartArmored = "images/Protagonists/Xerxes/Xerxes 3-4 Armored with bow.webp"
image xerx34BowDrawn = "images/Protagonists/Xerxes/Xerxes 3-4 with bow drawn.webp"
image xerx34BowDrawnArmored = "images/Protagonists/Xerxes/Xerxes 3-4 Armored with bow drawn.webp"
image xerx34JavelinArmored = "images/Protagonists/Xerxes/Xerxes Atackking with javelin armored.webp"
image xerx34Javelin = "images/Protagonists/Xerxes/Xerxes Atackking with Javelin.webp"

image xerxThrowinfArmored = "images/Protagonists/Xerxes/Xerxes throwing Armored.webp"
image xerx34RockThrowArmored = "images/Protagonists/Xerxes/Xerxes Atackking with rock armored.webp"
image xerx34RockThrow = "images/Protagonists/Xerxes/Xerxes Atackking with Rock.webp"

image xerx34RockArmored = "images/Protagonists/Xerxes/Xerxes holding rock Armored.webp"
image xerx34Rock = "images/Protagonists/Xerxes/Xerxes Holding rock.webp"

image xerx34LookDownArmored = "images/Protagonists/Xerxes/Xerxes 3-4 Armored looking down.webp"
image xerx34LookDown = "images/Protagonists/Xerxes/Xerxes 3-4 looking down.webp"
image xerx34LookDownSad = "images/Protagonists/Xerxes/Xerxes 3-4 looking down sad.webp"
image xerx34LookDownSadNoHat = "images/Protagonists/Xerxes/Xerxes 3-4 looking down sad No hat.webp"
image xerx34LookDownArmoredAnnoyed = "images/Protagonists/Xerxes/Xerxes 3-4 Armored looking down annoyed.webp"
image xerx34LookDownAnnoyed = "images/Protagonists/Xerxes/Xerxes 3-4 looking down annoyed.webp"

image xerxAttacked = "images/Protagonists/Xerxes/Xerxes Attacked.webp"
image xerxAttackedArmored = "images/Protagonists/Xerxes/Xerxes Attacked Armored.webp"
image xerxAttackedArmoredSoam = "images/Protagonists/Xerxes/Xerxes Attacked Armored SoAM.webp"
image xerxShotgunned = "images/Protagonists/Xerxes/Xerxes Shotguned Armored SoAM.webp"

image xerxAttackingSoamChargedArmored = "images/Protagonists/Xerxes/Xerxes Attacking Armored Soam.webp"

image xerxBehind = "images/Protagonists/Xerxes/Behind Xerxes Armored.webp"
image xerxBehindJumpUp = "images/Protagonists/Xerxes/Behind Xerxes jump up Armored.webp"
image xerxBehindJumpDown = "images/Protagonists/Xerxes/Behind Xerxes jump down Armored.webp"

image xerx3quatHappy = "images/Protagonists/Xerxes/Xerxes 3-4 Neutral Happy.webp"
image xerx3quatHappyArmored = "images/Protagonists/Xerxes/Xerxes 3-4 Neutral Happy Armored.webp"
image xerx3quatHappyer = "images/Protagonists/Xerxes/Xerxes 3-4 Happy.webp"
image xerxequatHappyerPoitingFoward = "images/Protagonists/Xerxes/Xerxes 3-4 Happy Pointing.webp"
image xerx3quatHappyerArmored = "images/Protagonists/Xerxes/Xerxes 3-4 Armored Happy.webp"

image xerx3quatConsurndArmored = "images/Protagonists/Xerxes/Xerxes 3-4 Armored Consurnd.webp"
image xerx3quatConsurnd = "images/Protagonists/Xerxes/Xerxes 3-4 Consurnd.webp"
image xerx3quatAnnoyed = "images/Protagonists/Xerxes/Xerxes 3-4 annoyed.webp"
image xerx3quatAnnoyedArmored = "images/Protagonists/Xerxes/Xerxes 3-4 annoyed Armored.webp"
image xerx3quatCommandingCrossarmsArmored = Composite(( 600, 1400 ) , (0,0) , "images/Protagonists/Xerxes/Xerxes 3-4 annoyed Armored.webp" , (0,0) , "Xerxes 3-4 pointing Commanding Armored")
image xerx3quatFistPushArmored = "images/Protagonists/Xerxes/Xerxes 3-4 Armored Commanding Fist Push.webp"
image xerx3quatPointCommandingArmored = Composite ( (600,1400) ,  (0,0) , "images/Protagonists/Xerxes/Xerxes 3-4 pointing Happy Armored.webp" , (0,0) , "images/Protagonists/Xerxes/Xerxes 3-4 pointing Commanding Armored.webp" )
image xerx3quatWash = "images/Protagonists/Xerxes/Xerxes 3-4 washing.webp"
image xerx3quatHappyCrossArms = "images/Protagonists/Xerxes/Xerxes 3-4 happy crossarms.webp"
image xerx3quatHappyCrossArmsArmored = "images/Protagonists/Xerxes/Xerxes 3-4 Neutral Happy Crossarms Armored.webp"
image xerx3quatHappyerCrossArmsArmored = Composite( ( 600 , 1400 ), (0,0) , "images/Protagonists/Xerxes/Xerxes 3-4 Neutral Happy Crossarms Armored.webp" , (0,0), "images/Protagonists/Xerxes/Xerxes 3-4 Happy Face.webp" )
image xerx3quatPoint = "images/Protagonists/Xerxes/Xerxes 3-4 pointing.webp"
image xerx3quatPointArmored = Composite( (600, 1400) , (0,0) , "images/Protagonists/Xerxes/Xerxes 3-4 pointing Happy Armored.webp" , (0,0) , "images/Protagonists/Xerxes/Xerxes 3-4 annoyed face.webp")
image xerx3quatPointHappyArmored = "images/Protagonists/Xerxes/Xerxes 3-4 pointing Happy Armored.webp"
image xerx3quatPointHappy = "images/Protagonists/Xerxes/Xerxes 3-4 pointing happy.webp"
image xerx3quatPointHappyLookForward = "images/Protagonists/Xerxes/Xerxes 3-4 pointing happy while looking foward.webp"
image xerx3quatThink = "images/Protagonists/Xerxes/Xerxes 3-4 thinking.webp"
image xerx3quatThinkArmored = "images/Protagonists/Xerxes/Xerxes 3-4 thinking Armored.webp"
image xerx3quatWorry = "images/Protagonists/Xerxes/Xerxes 3-4 worried.webp"
image xerx3quatWorryArmored = Composite( (600,1400) , (0,0) , "images/Protagonists/Xerxes/Xerxes 3-4 Neutral Happy Armored.webp" , ( 0,0 ) , "images/Protagonists/Xerxes/Xerxes 3-4 Worried Armored.webp" )

image xerx3quatYeah = "images/Protagonists/Xerxes/Xerxes 3-4 Yeah Pose.webp"
image xerx3quatYeahAngry = Composite( (600,1400) , (0,0) , "images/Protagonists/Xerxes/Xerxes 3-4 Yeah Pose.webp" , (-50,0) , "images/Protagonists/Xerxes/Xerxes 3-4 Yeah Pose Armored Angry.webp" )
image xerx3quatDetermined = Composite( (600,1400) , (0,0) , "images/Protagonists/Xerxes/Xerxes 3-4 Yeah Pose.webp" , (0,0) , "images/Protagonists/Xerxes/Xerxes 3-4 pointing Commanding Armored.webp" )
image xerx3quatYeahArmored = "images/Protagonists/Xerxes/Xerxes 3-4 Yeah Pose Armored.webp"
image xerx3quatYeahArmoredAngry = Composite( (700,1400),( 0,0 ), "images/Protagonists/Xerxes/Xerxes 3-4 Yeah Pose Armored.webp" , ( 0,0 ), "images/Protagonists/Xerxes/Xerxes 3-4 Yeah Pose Armored Angry.webp" )

image xerx3quatHehehArmored = "images/Protagonists/Xerxes/Xerxes 3-4 Neutral Happy Armored.webp"
image xerx3quatNO = "images/Protagonists/Xerxes/Xerxes 3-4 Defencive.webp"
image xerx3quatGreet = "images/Protagonists/Xerxes/Xerxes 3-4 Greeting.webp"
image xerx3quatSneaky = "images/Protagonists/Xerxes/Xerxes 3-4 Sneaky Look Armored.webp"
image xerx3quatSquatKey = "images/Protagonists/Xerxes/xerxes 3-4 Squatting with Key Armored.webp"
image xerx3quatMiniSuprized = "images/Protagonists/Xerxes/Xerxes 3-4 Neutral Suprized.webp"
image xerx3quatMiniSuprizedArmored = "images/Protagonists/Xerxes/Xerxes 3-4 Neutral Suprized Armored.webp"

image xerx3quatFalling = "images/Protagonists/Xerxes/Xerxes 3-4 falling down.webp"

image xerxSpartaKickArmored = "images/Protagonists/Xerxes/Xerxes Armored Sparta Kicking.webp"
image xerxSideOnSmash = "images/Protagonists/Xerxes/Xerxes Side on something SMASH.webp"
image xerxSideOnSwordUp = "images/Protagonists/Xerxes/Xerxes Side on something Sword Up.webp"
image xerxOnSword = "images/Protagonists/Xerxes/Xerxes Side on something.webp"
image xerxFlung = "images/Protagonists/Xerxes/Xerxes Flung.webp"

image xerxHorseSuprise = "images/Protagonists/Xerxes/Xerxes Suprized Armored on Horse.webp"
image xerxHorseBow = "images/Protagonists/Xerxes/Xerxes Angry with Bow Armored on Horse.webp"
image xerxHorseAngry = "images/Protagonists/Xerxes/Xerxes Angry Armored on Horse.webp"
image xerxHorseMiniMad = Composite( ( 1200,2200 ) , ( 0,0 ), "images/Protagonists/Xerxes/Xerxes Neutral Happy Armored on Horse.webp" , (0,0) , "images/Protagonists/Xerxes/Xerxes Annoyed Face On Horse.webp" )

image xerxHorseYeah = "images/Protagonists/Xerxes/Xerxes Yeah Armored on Horse.webp"
image xerxHorseYeahSoAM = "images/Protagonists/Xerxes/Xerxes Yeah Armored on Horse with soam.webp"
image xerxHorseWithSoAM = Composite( (1200,2500) , (0,0) , "images/Protagonists/Xerxes/Xerxes Yeah Armored on Horse with soam.webp" , (0,0) , "images/Protagonists/Xerxes/Xerxes Neutral Happy Armored on Horse with soam.webp"  )
image xerxHorseSwordUp = "images/Protagonists/Xerxes/Xerxes 3-4 Horse Sword Up.webp"
image xerxHorseSwordDown = "images/Protagonists/Xerxes/Xerxes 3-4 Horse Sword Down.webp"
image xerxHorseSwordSteam = "images/Protagonists/Xerxes/Xerxes 3-4 Horse Sword Mini Sad Stream.webp"

image xerxHorseMiniSad = "images/Protagonists/Xerxes/Xerxes Mini Sad Armored on Horse.webp"


image xerxHorseGreeting = "images/Protagonists/Xerxes/Xerxes Greeting Armored on Horse.webp"

image xerxHorseHapper = "images/Protagonists/Xerxes/Xerxes Happy Armored on Horse.webp"
image xerx3HorseHappy = "images/Protagonists/Xerxes/Xerxes Neutral Happy Armored on Horse.webp"
image xerx3HorseNeutral =  Composite( ( 1200,2200 ) , ( 0,0 ), "images/Protagonists/Xerxes/Xerxes Neutral Happy Armored on Horse.webp" , (0,0) , "images/Protagonists/Xerxes/Xerxes 3-4 Neutral Armored on Horse.webp")
image xerx3Horse = "images/Protagonists/Xerxes/Xerxes 3-4 Neutral-Happy Armored on Horse.webp"
image xerx3HorseCurious = "images/Protagonists/Xerxes/Xerxes 3-4 Curious Armored on Horse.webp"
image xerxHorseBrush = "images/Protagonists/Xerxes/Xerxes 3-4 Neutral-Happy Armored on Horse Brushing Mane.webp"

image xerxWithAtossa = "images/Protagonists/Xerxes/Xerxes Hugging Atossa.webp"

image xerxCarryingAhriteAtossa = "images/Protagonists/Xerxes/Xerxes Carraying Courrupted Ato'ssa.webp"

image littleXerx = "images/Protagonists/Xerxes/Young Xerxes Little Happy.webp"

image xerxHandOpen = "images/Protagonists/Xerxes/Xerxes Hand Push.webp"
image xerxHandGrabby = "images/Protagonists/Xerxes/Xerxes Hand grab.webp"
image xerxHandSoam = "images/Protagonists/Xerxes/Xerxes Hand Push.webp"

image xerxSoAMPull1 = "images/Protagonists/Xerxes/Xerxes Pulling SoAM.webp"
image xerxSoAMPull2 = "images/Protagonists/Xerxes/Xerxes Pulling SoAM1.webp"
image xerxSoAMPullWin = "images/Protagonists/Xerxes/Xerxes Pulling SoAM2.webp"

image xerxWithSoAM = "images/Protagonists/Xerxes/Xerxes 3-4 unarmored With SoAM.webp"
image xerxWithSoAMHappy = "images/Protagonists/Xerxes/Xerxes 3-4 Neutral Happy unarmored With SoAM.webp"
image xerxWithSoAMEyesClosed = "images/Protagonists/Xerxes/Xerxes 3-4 eyes closed unarmored With SoAM.webp"
image xerxWithSoAMEyesClosedCharged1 = "images/Protagonists/Xerxes/Xerxes 3-4 eyes closed glowing1 unarmored With SoAM.webp"
image xerxWithSoAMEyesClosedCharged2 = "images/Protagonists/Xerxes/Xerxes 3-4 eyes closed glowing2 unarmored With SoAM.webp"
image xerxWithSoAMEyesClosedCharged3 = "images/Protagonists/Xerxes/Xerxes 3-4 eyes closed glowing3 unarmored With SoAM.webp"

image xerxBinded2SoAMYeah = "images/Protagonists/Xerxes/Xerxes 3-4 SoAM Binded.webp"
image xerxArmoredHurt = "images/Protagonists/Xerxes/Xerxes 3-4 Armored 029-01.webp"



#based on xerx 34 yeah
image xerx34OuchBurns = "images/Protagonists/Xerxes/Xerxes 3-4 Yeowch Pose.webp"
image xerx34Ouch = "images/Protagonists/Xerxes/Xerxes 3-4 Yeowcha Pose.webp"
#based on xerx yeah with SoAM
image xerxYeahOpenHand = "images/Protagonists/Xerxes/Xerxes Yeah Pose Open Hand.webp"
image xerxHappySoAM = "images/Protagonists/Xerxes/Xerxes Happy Soam.webp"

#Keiozia
image keiozia = "images/Protagonists/Xerxes/Xerxes' Old Girlfriends/Keiozia Neutral Happy Armored.webp"
image keioziaSeductiveStanding = "images/Protagonists/Xerxes/Xerxes' Old Girlfriends/Keiozia Seductive.webp"
image keioziaPossessed = "images/Protagonists/Xerxes/Xerxes' Old Girlfriends/Keiozia Possessed.webp"
image keioziaPossessedKilled = "images/Protagonists/Xerxes/Xerxes' Old Girlfriends/Keiozia Possessed Stabbed.webp"

#Adgilia
image adgilia = "images/Protagonists/Xerxes/Xerxes' Old Girlfriends/Adgilia Seductive.webp"
image adgiliaKneeCute = "images/Protagonists/Xerxes/Xerxes' Old Girlfriends/Adgilia 34 Knees Seductive.webp"
image adgiliaFlyFight = "images/Protagonists/Xerxes/Xerxes' Old Girlfriends/Adgilia Combat.webp"
image adgiliaFlyBlasted = "images/Protagonists/Xerxes/Xerxes' Old Girlfriends/Adgilia Amored Blasted.webp"

#Xerxes' Parents
image xerxesParents = "images/Protagonists/Xerxes/Xerxes Perents/Harpeijis and Tyettuta Together.webp"

#Tesipiz

image tesipizAnnoyed = "images/Protagonists/Tesipiz/Annoyed Tesipiz.webp"
image tesipizSlightlyAnnoyed = "images/Protagonists/Tesipiz/Slightly Annoyed Tesipiz.webp"



image tesipizHappy = "images/Protagonists/Tesipiz/Happy Tesipiz.webp"
image tesipizHappyArmored = "images/Protagonists/Tesipiz/Happy Tesipiz armored.webp"
image tesipizHappyRunArmored = "images/Protagonists/Tesipiz/Happy Tesipiz armored Running.webp"
image tesipizHappyArmsOut = "images/Protagonists/Tesipiz/Happy Tesipiz Arms out.webp"
image tesipizArmsOutHappyArmored = "images/Protagonists/Tesipiz/Happy Tesipiz armored Arms out.webp"
image tesipizNoWeGoodArmored = "images/Protagonists/Tesipiz/No we good Happy Tesipiz Armored.webp"
image tesipizNeutralHappy = "images/Protagonists/Tesipiz/Neutral Happy Tesipiz.webp" 
image tesipizNeutralHappyArmored = "images/Protagonists/Tesipiz/Neutral Happy Tesipiz armored.webp" 


image tesipizNeutral = "images/Protagonists/Tesipiz/Neutral Tesipiz.webp"
image tesipizNeutralArmored = "images/Protagonists/Tesipiz/Neutral Tesipiz armored.webp"
image tesipizPointingNeutralArmored = "images/Protagonists/Tesipiz/Tesipiz neutral pointing armored.webp"

image tesipizCommanding = "images/Protagonists/Tesipiz/Tesipiz commanding.webp"
image tesipizCommandingHappy = "images/Protagonists/Tesipiz/Tesipiz commanding Happy.webp"

image tesipizPointingHappy = "images/Protagonists/Tesipiz/Neutral Happy Tesipiz Pointing.webp"
image tesipizPointingHappyArmored = "images/Protagonists/Tesipiz/Tesipiz happy pointing.webp"
image tesipizGreeting = "images/Protagonists/Tesipiz/Tesipiz Greeting.webp"
image tesipizGreetingArmored = "images/Protagonists/Tesipiz/Tesipiz Greeting Armored.webp"

image tesipizSuprized = "images/Protagonists/Tesipiz/Tesipiz Suprized.webp"
image tesipizSuprizedArmored = "images/Protagonists/Tesipiz/Tesipiz Suprized Armored.webp"
image tesipizSuprizedArmed = "images/Protagonists/Tesipiz/Tesipiz Suprized Armed v1.webp"
image tesipizSuprizedArmedAmored = "images/Protagonists/Tesipiz/Tesipiz Suprized Armored Armed v1.webp"
image tesipiz34SupirzedArmored = "images/Protagonists/Tesipiz/Tesipiz 3-4 Suprized armored.webp"

image tesipizPointArmedArmored = "images/Protagonists/Tesipiz/Tesipiz Look point away Armored.webp"

image tesipizScaredRunning = "images/Protagonists/Tesipiz/Scared Tesipiz armored Running.webp"

image tesipizGettingSucked:
    "images/Protagonists/Tesipiz/Tesipiz 3-4 Eaten By Sand.webp" with Dissolve( 0.1 )
    pause 0.25
    "images/Protagonists/Tesipiz/Behind Tesipiz Armored in Sand.webp" with Dissolve( 0.1 )
    pause 0.25
    repeat

image tesipizMadArmed = "images/Protagonists/Tesipiz/Tesipiz angry Armed v1.webp"
image tesipizLittleMadArmed = "images/Protagonists/Tesipiz/Tesipiz slightly angry Armed v1.webp"
image tesipizClosedMadArmedArmored = "images/Protagonists/Tesipiz/Tesipiz Angry Closed Mouth Armored Armed v1.webp"
image tesipizMadArmoredArmed = "images/Protagonists/Tesipiz/Tesipiz Angry Armored Armed v1.webp"

image tesipizArmedArmored = "images/Protagonists/Tesipiz/Tesipiz Annoyed Armored Armed v1.webp"

image tesiHammerNChiselArmored = "images/Protagonists/Tesipiz/Tesipiz hammer and chisel Armored Armed.webp"

image tesipizSwing = "images/Protagonists/Tesipiz/Tesipiz Swinging.webp"
image tesipizSwing2 = "images/Protagonists/Tesipiz/Tesipiz Swinging 2.webp"
image tesipizArmoredSwing = "images/Protagonists/Tesipiz/Tesipiz Swinging Armored.webp"
image tesipizArmoredSwing2 = "images/Protagonists/Tesipiz/Tesipiz Swinging 2 Armored.webp"
image tesipizArmoredSwing2Angry = Composite ( ( 900 , 1500 ) , (0,0) , "images/Protagonists/Tesipiz/Tesipiz Swinging 2 Armored.webp" , (0,0) , "images/Protagonists/Tesipiz/Tesipiz Swinging 2 Armored Angry.webp" ) 

image tesipizSwinging:
    "images/Protagonists/Tesipiz/Tesipiz Swinging.webp" with Dissolve( 0.1 )
    pause 0.25
    "images/Protagonists/Tesipiz/Tesipiz Swinging 2.webp" with Dissolve( 0.1 )
    pause 0.25
    repeat
image tesipizSwingingArmored:
    "images/Protagonists/Tesipiz/Tesipiz Swinging Armored.webp" with Dissolve( 0.1 )
    pause 0.25
    "images/Protagonists/Tesipiz/Tesipiz Swinging 2 Armored.webp" with Dissolve( 0.1 )
    pause 0.25
    repeat

image tesipizArmoredSwingBack = "images/Protagonists/Tesipiz/Tesipiz Swinging Armored Back.webp"
image tesipizArmoredSwingBack2 = "images/Protagonists/Tesipiz/Tesipiz Swinging 2 Armored Back.webp"

image tesipizSwingingAss:
    "images/Protagonists/Tesipiz/Tesipiz Swinging Armored Back.webp" with Dissolve( 0.1 )
    pause 0.25
    "images/Protagonists/Tesipiz/Tesipiz Swinging 2 Armored Back.webp" with Dissolve( 0.1 )
    pause 0.25
    repeat    

image tesipizHuffingArmored = "images/Protagonists/Tesipiz/Tesipiz armored 3-4 Sniff Eyes Closed.webp"

image tesipizAttacked = "images/Protagonists/Tesipiz/Tesipiz Attacked.webp"
image tesipizAttackedArmored = "images/Protagonists/Tesipiz/Tesipiz Attacked Armored.webp"
image tesipizThonkt = "images/Protagonists/Tesipiz/Tesipiz 3-4 unarmored Looking Down Thonkt.webp"
image tesipizJump = "images/Protagonists/Tesipiz/Tesipiz jump1.webp"
image tesipizJumpArmored = "images/Protagonists/Tesipiz/Tesipiz jump1 armored v1.webp"

image tesipizPointingUp = "images/Protagonists/Tesipiz/Happy Tesipiz 1 finger.webp"
image tesipizPointingUpArmored = "images/Protagonists/Tesipiz/Happy Tesipiz 1 finger Armored.webp"
image tesipiz2Fingers = "images/Protagonists/Tesipiz/Happy Tesipiz 2 fingers.webp"
image tesipiz2FingersPointyAway = "images/Protagonists/Tesipiz/Happy Tesipiz 2 fingers pointing 2 next.webp"
image tesipiz2FingersArmored = "images/Protagonists/Tesipiz/Happy Tesipiz 2 fingers Armored.webp"
image tesipiz3Fingers = "images/Protagonists/Tesipiz/Happy Tesipiz 3 fingers.webp"
image tesipiz3FingersArmored = "images/Protagonists/Tesipiz/Happy Tesipiz 3 fingers Armored.webp"


image tesipizHoldingMap = "images/Protagonists/Tesipiz/Tesipiz looking at map.webp"
image tesipizHoldingKey = "images/Protagonists/Tesipiz/Tesipiz holding Key.webp"
image tesipizHoldindZwotiKey = "images/Protagonists/Tesipiz/Tesipiz Holding Key Armored.webp"
image tesipizThrowingArmored = "images/Protagonists/Tesipiz/Tesipiz Throwing Armored.webp"
image tesipizThrowing = "images/Protagonists/Tesipiz/Tesipiz Throwing.webp"
image tesipizOoahArmored = "images/Protagonists/Tesipiz/Tesipiz ooah armored.webp"
image tesipizWooArmored = "images/Protagonists/Tesipiz/Wooo Tesipiz armored.webp"
image tesipizAngryArmored = "images/Protagonists/Tesipiz/Tesipiz angry armored.webp"
image tesipizAngerierArmored = "images/Protagonists/Tesipiz/Tesipiz angrier armored.webp"
image tesipizBombing = "images/Protagonists/Tesipiz/Tesipiz Atackking with bomb.webp"
image tesipizBombingArmed = "images/Protagonists/Tesipiz/Tesipiz Atackking with bomb armored.webp"
image tesipizHehehArmoredArmed = "images/Protagonists/Tesipiz/Tesipiz Heheh Armored Armed.webp"
image tesipizFlameStickAndBomb = "images/Protagonists/Tesipiz/Tesipiz with bomb and flame stick armored.webp"
image tesipizBombAndFist = "images/Protagonists/Tesipiz/Tesipiz with bomb and fist armored.webp"
image tesipizYeah = "images/Protagonists/Tesipiz/Tesipiz yeah.webp"
image tesipizYeahArmored = "images/Protagonists/Tesipiz/Tesipiz yeah armored.webp"

image tesipiz34OahArmored = "images/Protagonists/Tesipiz/Tesipiz 3-4 ooah armored.webp"
image tesipiz34PointingForward = "images/Protagonists/Tesipiz/Tesipiz 3-4 pointing forwards.webp"
image tesipiz34MiniSmugArmored = "images/Protagonists/Tesipiz/Tesipiz armored.webp"
image tesipiz34MiniHappyArmored = "images/Protagonists/Tesipiz/Tesipiz 3-4 slightly happy armored.webp"
image tesipiz34HappyArmored = "images/Protagonists/Tesipiz/Tesipiz armored 3-4 Happy.webp"
image tesipiz34Commanding = "images/Protagonists/Tesipiz/Tesipiz 3-4 Commanding.webp"
image tesipiz34MiniCommanding = "images/Protagonists/Tesipiz/Tesipiz 3-4 Mini Commanding.webp"
image tesipiz34MiniCommandingArmored = "images/Protagonists/Tesipiz/Tesipiz armored 3-4 Mini Commanding.webp"

image tesipiz34CommandingPoting = "images/Protagonists/Tesipiz/Tesipiz 3-4 Commanding pointing.webp"
image tesipiz34CommandingPotingArmored = Composite( (700,1400) , (0,0) , "images/Protagonists/Tesipiz/Tesipiz 3-4 annoyed armored pointing.webp" , (100,0), "images/Protagonists/Tesipiz/Tesipiz 3-4 consurned armored face.webp")
image tesipiz34MiniCommandingPoting = "images/Protagonists/Tesipiz/Tesipiz 3-4 Mni Commanding pointing.webp"

image tesipiz34Curious = "images/Protagonists/Tesipiz/Tesipiz 3-4 curious.webp"
image tesipiz34CuriousPointing = "images/Protagonists/Tesipiz/Tesipiz 3-4 curious pointing.webp"
image tesipiz34AnnoyedPointingArmored = "images/Protagonists/Tesipiz/Tesipiz 3-4 annoyed armored pointing.webp"

image tesipiz34HappyCommandingPoting = "images/Protagonists/Tesipiz/Tesipiz 3-4 Commanding happy pointing.webp"
image tesipiz34NeutralHappyArmoredPointing = "images/Protagonists/Tesipiz/Tesipiz 3-4 slightly happy armored pointing.webp"
image tesipiz34HappyArmoredPointing = "images/Protagonists/Tesipiz/Tesipiz 3-4 happy armored pointing.webp"
image tesipiz34NeutralHappy = "images/Protagonists/Tesipiz/Tesipiz 3-4 Neutral Happy.webp"
image tesipiz34Happy = "images/Protagonists/Tesipiz/Tesipiz 3-4 Happy.webp"
image tesipiz34PotingWithAx = "images/Protagonists/Tesipiz/Tesipiz 3-4 poiting with pashidian axe.webp"

image tesipiz34GivingBomb = "images/Protagonists/Tesipiz/Tesipiz armored 3-4 Giving Bomb.webp"

image tesipiz34Consurned = "images/Protagonists/Tesipiz/Tesipiz 3-4 consurned armored.webp"

image tesipiz34PoitingForwardLookingToDaSide = "images/Protagonists/Tesipiz/Tesipiz 3-4 side face poiting 2 side.webp"

image tesipiz34snekayArmored = "images/Protagonists/Tesipiz/Tesipiz 3-4 slightly sneaky armored.webp"

image tesipizDoll1 = "images/Protagonists/Tesipiz/Tesipiz armored 3-4 with Doll Old.webp"
image tesipizDollEye = "images/Protagonists/Tesipiz/Tesipiz armored 3-4 with Doll Old and eyeball.webp"
image tesipizDoll2 = "images/Protagonists/Tesipiz/Tesipiz armored 3-4 with Doll Old 2 eyeballs.webp"
image tesipizEyeDollIn:
    "images/Protagonists/Tesipiz/Tesipiz armored 3-4 with Doll Old and eyeball.webp"
    pause 0.5
    "images/Protagonists/Tesipiz/Tesipiz armored 3-4 with Doll Old putting eyeball back in.webp"
    pause 0.5
    "images/Protagonists/Tesipiz/Tesipiz armored 3-4 with Doll Old 2 eyeballs.webp"

image tesipiz34LookingDown = "images/Protagonists/Tesipiz/Tesipiz 3-4 unarmored Looking Down.webp"
image tesipiz34LookingDownArmored = "images/Protagonists/Tesipiz/Tesipiz looking down armored.webp"
image tesipiz34LookingDownSad = "images/Protagonists/Tesipiz/Tesipiz 3-4 unarmored Looking Down Sad.webp"
image tesipiz34LookingDownAnnoyed = "images/Protagonists/Tesipiz/Tesipiz 3-4 unarmored Looking Down Annoyed.webp"
image tesipiz34LookingDownAnnoyedArmored = "images/Protagonists/Tesipiz/Tesipiz looking down armored annoyed.webp"

image tesipiz34SittingNeutralHappy = "images/Protagonists/Tesipiz/Tesipiz 3-4 Neutral Happy Sitting.webp"

image tesipizDefeated = "images/Protagonists/Tesipiz/Tesipiz armored 3-4 00.webp"

image tesipizFlung = "images/Protagonists/Tesipiz/Tesipiz Flung.webp"
image tesipizSideOnUp = "images/Protagonists/Tesipiz/Tesipiz Side on something Ax Up.webp"
image tesipizSideOnDown = "images/Protagonists/Tesipiz/Tesipiz Side on something SMASH.webp"
image tesipizSideOn = "images/Protagonists/Tesipiz/Tesipiz Side on something.webp"

image tesipizHorseAnnoyed = "images/Protagonists/Tesipiz/Tesipiz Annoyed Armored on Horse.webp"
image tesipizHorseAngry = "images/Protagonists/Tesipiz/Tesipiz angry Armored on Horse.webp"
image tesipizHorseAngryJavelin = "images/Protagonists/Tesipiz/Tesipiz Annoyed with javelin Armored on Horse.webp"
image tesipizHorseAngryMace = "images/Protagonists/Tesipiz/Tesipiz Angry with Mace Armored on Horse No Bomb.webp"
image tesipizHorseMace = Composite ( (1300,2200) , (0,0) , "images/Protagonists/Tesipiz/Tesipiz Angry with Mace Armored on Horse No Bomb.webp", (0,0) , "images/Protagonists/Tesipiz/Tesipiz with Mace Armored on Horse No Bomb.webp" )
image tesipizHorseAngryMaceBomb = "images/Protagonists/Tesipiz/Tesipiz Angry with Mace Armored on Horse.webp"
image tesipizHorseBombExictedTaunght = "images/Protagonists/Tesipiz/Tesipiz exicted taunting with bomb Armored on Horse.webp"
image tesipizHorseBombExicted = "images/Protagonists/Tesipiz/Tesipiz exicted with bomb Armored on Horse.webp"
image tesipizHorseHappy2Fingers = "images/Protagonists/Tesipiz/Tesipiz Happy 2 fingers on horse.webp"
image tesipizHorseHappyGreeting = "images/Protagonists/Tesipiz/Tesipiz happy Greeting Armored on Horse.webp"
image tesipizHorseHappy = "images/Protagonists/Tesipiz/Tesipiz Happy Armored on Horse Forward.webp"
image tesipizHorseSad = "images/Protagonists/Tesipiz/Tesipiz Sad Armored on Horse.webp"
image tesipizHorseUnImpressed = "images/Protagonists/Tesipiz/Tesipiz unImpressed Armored on Horse.webp"
image tesipizHorseYeah = "images/Protagonists/Tesipiz/Tesipiz Yeah on Horse.webp"
image tesipizHorseNeutralHappy = "images/Protagonists/Tesipiz/Tesipiz Neutral-Happy Armored on Horse.webp"
image tesipizHorsePoiting = "images/Protagonists/Tesipiz/Tesipiz Poiting Armored on Horse.webp"
image tesipizHorseReadingMap = "images/Protagonists/Tesipiz/Tesipiz Reading map Armored on Horse.webp"
image tesipizHorseSupized = "images/Protagonists/Tesipiz/Tesipiz Suprized Armored on Horse.webp"
image tesipizHorseBrush = "images/Protagonists/Tesipiz/Tesipiz 3-4 Neutral-Happy Armored on Horse Brushing Mane.webp"

image tesipiz3HorseNeutralHappy = "images/Protagonists/Tesipiz/Tesipiz  3-4 Neutral-Happy Armored on Horse.webp"

image tesipiz33HorseConcerned = "images/Protagonists/Tesipiz/Tesipiz armored concerned on Horse.webp"
image tesipiz33HorseExicted = "images/Protagonists/Tesipiz/Tesipiz armored exicted on Horse.webp"
image tesipiz33HorseExtraHappy = "images/Protagonists/Tesipiz/Tesipiz armored extra Happy on Horse.webp"
image tesipiz33HorseHappy = "images/Protagonists/Tesipiz/Tesipiz armored Happy on Horse.webp"

image tesipizBackArmored = "images/Protagonists/Tesipiz/Behind Tesipiz Armored.webp"
image tesipizBackArmoredArmsUp = "images/Protagonists/Tesipiz/Behind Tesipiz Armored Arms up.webp"
image tesipizBackArmoredSQUAT = "images/Protagonists/Tesipiz/Behind Tesipiz Armored SQUAT.webp"

image TesipizhuggingMuwa = "images/Tesipiz and Muwa.webp"
image tesipizWithKorkinGF = "images/Protagonists/Tesipiz/tesipiz with korkin gf.webp"



#Ato'ssa

image atoOnXerxes = "images/Protagonists/Atossa/Atossa on Xerxes.webp"
image atoOnXerxesNeutralHappy = "images/Protagonists/Atossa/Atossa on Xerxes Neutral Happy.webp"
image atoOnXerxesHairScuffle = "images/Protagonists/Atossa/Atossa on Xerxes Hair Hold.webp"
image atoOnXerxesSad = "images/Protagonists/Atossa/Atossa on Xerxes Sad.webp"
image atoOnXerxesMad = "images/Protagonists/Atossa/Atossa on Xerxes Mad.webp"
image atoOnXerxesBoobaGrab1 = "images/Protagonists/Atossa/Atossa on Xerxes Booba Touch.webp"
image atoOnXerxesBoobaGrab2 = "images/Protagonists/Atossa/Atossa on Xerxes Booba Touch2.webp"
image atoOnXerxesHorny1 = "images/Protagonists/Atossa/Atossa on Xerxes Horny1.webp"
image atoOnXerxesHorny2 = "images/Protagonists/Atossa/Atossa on Xerxes Horny2.webp"
image atoOnXerxesEyesClosed = "images/Protagonists/Atossa/Atossa on Xerxes Eyes Closed.webp"

image atoOnXerxesSleeping = "images/Protagonists/Atossa/Atossa on Xerxes Sleeping.webp"
image atoOnXerxesSleepingTouch = "images/Protagonists/Atossa/Atossa on Xerxes Sleeping Touch.webp"
image atoOnXerxesSleepingTouchAwake = "images/Protagonists/Atossa/Atossa on Xerxes Sleeping Touch 1eye.webp"
image atoOnXerxesSleepingAwake = "images/Protagonists/Atossa/Atossa on Xerxes Sleeping 2eyes.webp"
image atoOnXerxesSleepingHalfNekked = "images/Protagonists/Atossa/Atossa on Xerxes Sleeping Half Nekked.webp"
image atoOnXerxesSleepingHalfNekkedAwake = "images/Protagonists/Atossa/Atossa on Xerxes Sleeping Half Nekked 2 eyes.webp"

image atoHalfNekkedOnXerxes = "images/Protagonists/Atossa/Atossa Half Nekked on Xerxes.webp"
image atoHalfNekkedOnXerxesNeutralHappy = "images/Protagonists/Atossa/Atossa Half Nekked on Xerxes Neutral happy.webp"
image atoHalfNekkedOnXerxesHairScuffle = "images/Protagonists/Atossa/Atossa Half Nekked on Xerxes Hair Hold.webp"
image atoHalfNekkedOnXerxesBoobaGrab = "images/Protagonists/Atossa/Atossa Half Nekked on Xerxes Booba Touch.webp"
image atoHalfNekkedOnXerxesEyesClosed = "images/Protagonists/Atossa/Atossa Half Nekked on Xerxes Eyes Closed.webp"

image atoHalfNekkedOnXerxesSad = "images/Protagonists/Atossa/Atossa Half Nekked on Xerxes Sad.webp"

image atohappywave = "images/Protagonists/Atossa/Atossa Happy Standing Waving.webp"
image atohappy = "images/Protagonists/Atossa/Ato'ssa Happy Standing.webp"
image atoHorny = "images/Protagonists/Atossa/Ato'ssa Horny Standing.webp"
image atoHalfNekkedHorny = "images/Protagonists/Atossa/Atossa Half-Nekked Horny.webp"

image atohappyHalfNekked = "images/Protagonists/Atossa/Atossa Half-Nekked Mini-Happy.webp"
image atohappyHalfNekkedEyesClosed = "images/Protagonists/Atossa/Atossa Half-Nekked Sleeping.webp"
image atohappyHalfNekkedEyesHalf = "images/Protagonists/Atossa/Atossa Half-Nekked waking up.webp"
image atohappy2 = "images/Protagonists/Atossa/Ato'ssa Happy Standing2.webp"
image atohappy2HalfNekked = "images/Protagonists/Atossa/Atossa Half-Nekked Standing.webp"
image atohappyerHalfNekked = "images/Protagonists/Atossa/Atossa Half-Nekked Happy.webp"
image atoSadHalfNekked = "images/Protagonists/Atossa/Atossa Half-Nekked Sad.webp"
image atohappy2SemiAhrite = "images/Protagonists/Atossa/Ato'ssa Happy Standing2 Semi-Courrupted.webp"
image atohappySemiAhriteNekked = "images/Protagonists/Atossa/Atossa Nekked Semi-Courrupted Standing.webp"

image atoSeductive = "images/Protagonists/Atossa/Ato'ssa Seductive Exitied.webp"

image atoExcited = "images/Protagonists/Atossa/Atossa exited.webp" 
image atoExcitedArmsOut = "images/Protagonists/Atossa/Atossa exicted arms out.webp" 
image atoMiniExcited = "images/Protagonists/Atossa/Atossa mini exicted.webp" 
image atolaugh = "images/Protagonists/Atossa/Ato'ssa Happy Standing2 laughing.webp"

image atosit = "images/Protagonists/Atossa/Atossa Sitting Happy.webp"
image atositHalfNekked = "images/Protagonists/Atossa/atossa half-Nekked Kneeling.webp"

image atorolly1 = "images/Protagonists/Atossa/Atossa rolly1.webp"
image atorolly2 = "images/Protagonists/Atossa/Atossa rolly2.webp"
image atoHappyPoint = "images/Protagonists/Atossa/Ato'ssa Happy Pointing.webp"
image atoHeadpats1 = "images/Protagonists/Atossa/Atossa Headpats1.webp"
image atoHeadpats2 = "images/Protagonists/Atossa/Atossa Headpats2.webp"
image atoSuprized = "images/Protagonists/Atossa/Atossa suprized.webp"

image atoOFaceNoShadowsNoShoes = "images/Protagonists/Atossa/Atossa Sleep Clothed No Shoes O.webp"
image atoOFaceHalfNekkedNoShadows = "images/Protagonists/Atossa/Atossa Half-Nekked O No Shade.webp"

image atoAngry = "images/Protagonists/Atossa/Ato'ssa Angry.webp"
image ato3quatAngry = "images/Protagonists/Atossa/Atossa 3-4 Angry.webp"
image atoAngryPunch = "images/Protagonists/Atossa/Atossa 3-4 Angry Punch.webp"

image atoSadAngry = "images/Protagonists/Atossa/Ato'ssa Sad Angry.webp"

image atoHoldingRock = "images/Protagonists/Atossa/Atossa Holding rock Mini-Happy.webp"
image atoThrowing = "images/Protagonists/Atossa/Atossa Happy Throw.webp"

image atoArmoredHehe = "images/Protagonists/Atossa/Atossa hehe happy armored.webp"
image atoArmorGiggle = "images/Protagonists/Atossa/Atossa giggle happy armored.webp"
image atoArmorFighty = "images/Protagonists/Atossa/Atossa fighty armored.webp"
image atoArmorFightyBow = "images/Protagonists/Atossa/Atossa fighty with bow armored.webp"
image atoArmoredAngry = "images/Protagonists/Atossa/Atossa angry armored.webp"
image atoArmoredAngryBow = "images/Protagonists/Atossa/Atossa angry armored with bow.webp"
image ato34Armored = "images/Protagonists/Atossa/Atossa 3-4 looking forward armored.webp"
image atoArmoredHappyGreeting = "images/Protagonists/Atossa/Atossa happy greeting armored.webp"
image atoHappyGreeting = "images/Protagonists/Atossa/Ato'ssa Happy Greeting.webp"
image atoHappyPointBack = "images/Protagonists/Atossa/Atossa happy pointing back armored.webp"
image atoArmored = "images/Protagonists/Atossa/Atossa 3-4 armored.webp"
image atoWorriedArmored = "images/Protagonists/Atossa/Atossa worried armored.webp"

image atoSleeping = "images/Protagonists/Atossa/Atossa Sleep Clothed.webp"
image atoSleepNoShoess = "images/Protagonists/Atossa/Atossa Sleep Clothed No Shoes.webp"
image atoWakeUp = "images/Protagonists/Atossa/Atossa waking up.webp"

image ato3quatHeadPats1 = "images/Protagonists/Atossa/Atossa 3-4 Headpats1.webp"
image ato3quatHeadPats2 = "images/Protagonists/Atossa/Atossa 3-4 Headpats2.webp"
image ato3quatFaceStorke1 = "images/Protagonists/Atossa/Atossa 3-4 face side scruffle.webp"
image ato3quatFaceStorke2 = "images/Protagonists/Atossa/Atossa 3-4 face side scruffle2.webp"
image ato3quatExicted = "images/Protagonists/Atossa/Atossa 3-4 exicted.webp"
image ato3quatMiniExict = "images/Protagonists/Atossa/Atossa 3-4 mini exicted.webp"
image ato3quatHappy = "images/Protagonists/Atossa/Atossa 3-4 Neutral Happy.webp"
image ato3quatHappy2 = "images/Protagonists/Atossa/Atossa 3-4 Happy2.webp"
image ato3quatGreet = "images/Protagonists/Atossa/Atossa 3-4 Greeting.webp"
image ato3quatHappyLookingAtU = "images/Protagonists/Atossa/Atossa 3-4 Neutral Happy looking at you.webp"
image ato3quatHappyer = "images/Protagonists/Atossa/Atossa 3-4 Happy.webp"
image ato3quatHehe = "images/Protagonists/Atossa/Atossa 3-4 Hehe.webp"
image ato3quatGetYa = "images/Protagonists/Atossa/Atossa 3-4 unarmored 100-70.webp"
image ato3quatSeduction = "images/Protagonists/Atossa/Atossa 3-4 seductive.webp"
image ato3quatCurious = "images/Protagonists/Atossa/Atossa 3-4 Curious.webp"
image ato3quatMiniSad = "images/Protagonists/Atossa/Atossa 3-4 slightly sad.webp"
image ato3quatTouchy = "images/Protagonists/Atossa/Atossa 3-4 Touchy Time.webp"
image ato3quatWash = "images/Protagonists/Atossa/Atossa washing.webp"
image ato3quatCheeky = "images/Protagonists/Atossa/Atossa 3-4 cheeky.webp"
image ato3quatO = "images/Protagonists/Atossa/Atossa 3-4 O Face.webp"

image ato3quatHalfNekked = "images/Protagonists/Atossa/Atossa 3-4 Half-Nekked.webp"
image ato3quatHalfNekkedHappy = "images/Protagonists/Atossa/Atossa 3-4 Half-Nekked Happy.webp"
image ato3quatHalfNekkedMad = "images/Protagonists/Atossa/Atossa 3-4 Half-Nekked Angry.webp"
image ato3quatHalfNakkedO = "images/Protagonists/Atossa/Atossa 3-4 Half-Nekked O.webp"

image littleAtoShocked = "images/Protagonists/Atossa/Young Atossa Shocked Sad.webp"
image littleAtoSad = "images/Protagonists/Atossa/Young Atossa Sad.webp"
image zyaryaDed = "images/Protagonists/Atossa/Ato'ssa's Mother/zyarya Ded.webp"

image atossaSideScruffle:
    "images/Protagonists/Atossa/Atossa 3-4 face side scruffle.webp" with Dissolve( 0.15 )
    pause 0.33
    "images/Protagonists/Atossa/Atossa 3-4 face side scruffle2.webp" with Dissolve( 0.15 )
    pause 0.33
    repeat

image atossaHeadPats:
    "images/Protagonists/Atossa/Atossa 3-4 Headpats1.webp" with Dissolve( 0.15 )
    pause 0.33
    "images/Protagonists/Atossa/Atossa 3-4 Headpats2.webp" with Dissolve( 0.15 )
    pause 0.33
    repeat

image atossaHairStroke:
    "images/Protagonists/Atossa/Ato'ssa Gets Stroked 1.webp" with Dissolve(0.15)
    pause 0.33
    "images/Protagonists/Atossa/Ato'ssa Gets Stroked 2.webp" with Dissolve(0.15)
    pause 0.33
    "images/Protagonists/Atossa/Ato'ssa Gets Stroked 3.webp" with Dissolve(0.15)
    pause 0.33
    repeat

#Darius

image dariusAnnoyed = "images/Protagonists/Darius/Darius annoyed.webp"
image dariusMiniAnnoyed = "images/Protagonists/Darius/Darius slightly annoyed.webp"
image dariusPointCommand = "images/Protagonists/Darius/Darius command pointing.webp"
image dariusGreeting = "images/Protagonists/Darius/Darius Happy Greeting.webp"
image dariusGreetingHand = "images/Protagonists/Darius/Darius greeting.webp"
image dariusCurious = "images/Protagonists/Darius/Darius Curious.webp"
image dariusMiniHappy = "images/Protagonists/Darius/Darius slightly Happy Greeting.webp"
image dariusYEAH = "images/Protagonists/Darius/Darius yeah pose.webp"
image dariusPointBack = "images/Protagonists/Darius/Darius pointing back.webp"
image happyDarius = "images/Protagonists/Darius/Darius Happy.webp"
image dariusThinking = "images/Protagonists/Darius/Darius thinking poiting.webp"
image dariusWorried = "images/Protagonists/Darius/Darius worried.webp"
image dariusNeutral = "images/Protagonists/Darius/Darius neutral.webp"
image dariusItem = "images/Protagonists/Darius/Darius pointing item.webp"

#Shahhriit

image shahhriitStand = "images/NPCs/Jamesia/Ectabana/shahhriit standing.webp"
image shahhriitPointBack = "images/NPCs/Jamesia/Ectabana/shahhriit standing poiting back.webp"
image shahhriitPointFoward = "images/NPCs/Jamesia/Ectabana/shahhriit standing poiting.webp"

#Takura
image takuraFightScared = "images/Protagonists/Takura/Takura Fighting Scared.webp"
image takuraHappy = "images/Protagonists/Takura/Takura Happy Standing.webp"
image takuraNeutralHappy = "images/Protagonists/Takura/Takura Neutral Happy Standing.webp"
image takuraSeductive = "images/Protagonists/Takura/Takura Happy Seductive.webp"
image takuraSeductiveEyesClosed = "images/Protagonists/Takura/Takura Happy Seductive eyes closed.webp"
image takuraHappySit = "images/Protagonists/Takura/Takura Happy Sitting.webp"
image takuraHornySit = "images/Protagonists/Takura/Takura Hornyy Sitting.webp"
image takuraHappySit2 = "images/Protagonists/Takura/Takura Happy Sitting2.webp"
image takuraHappySideSit = "images/Protagonists/Takura/Takura Side Sitting.webp"
image takuraNeutralHappySit = "images/Protagonists/Takura/Takura Neutral Happy Sitting.webp"
image takuraNeutralHappySideSit = "images/Protagonists/Takura/Takura Side Sitting Neutral Happy.webp"
image takuraOoah = "images/Protagonists/Takura/Takura Ooah.webp"
image takuraSadSit = "images/Protagonists/Takura/Takura sad Sitting.webp"
image takuraSadSitSide = "images/Protagonists/Takura/Takura Side Sitting Sad.webp"
image takuraWhatSitSide = "images/Protagonists/Takura/Takura Side Sitting What.webp"
image takuraTesipizSnuggle1 = "images/Protagonists/Takura/Takura Tesipiz Snuggling.webp"
image takuraTesipizSnuggle2 = "images/Protagonists/Takura/Takura Tesipiz Snuggling 2.webp"

image takuraTesipizSnuggleStand:
    "images/Protagonists/Takura/Takura Tesipiz Snuggling.webp" with Dissolve( 0.1 )
    pause 0.25
    "images/Protagonists/Takura/Takura Tesipiz Snuggling 2.webp" with Dissolve( 0.1 )
    pause 0.25
    repeat

#Volkara
image volkaraNeutralHappy = "images/Protagonists/Volkara/Volkara Neutral Happy.webp"
image volkaraHappy = "images/Protagonists/Volkara/Volkara Happy.webp"
image volkaraHeheh = "images/Protagonists/Volkara/Volkara Heheh.webp"
image volkaraYeah = "images/Protagonists/Volkara/Volkara Yeah.webp"
image volkaraSuprized = "images/Protagonists/Volkara/Volkara Suprized.webp"
image volkaraHappyGreeting = "images/Protagonists/Volkara/Volkara Happy Greeting.webp"
image volkaraMiniMad = "images/Protagonists/Volkara/Volkara Mini Mad.webp"
image volkaraThink = "images/Protagonists/Volkara/Volkara Thinking.webp"

image volkaraNeutralHappyNight = "images/Protagonists/Volkara/Volkara Neutral Happy Nigthtime.webp"
image volkaraNeutralHappyNightPillow = "images/Protagonists/Volkara/Volkara Neutral Happy Nigthtime Pillow.webp"
image volkaraHappyNightPillow = "images/Protagonists/Volkara/Volkara Happy Nigthtime Pillow.webp"

image volkaraNeutralHappyArmored = "images/Protagonists/Volkara/Volkara Neutral Happy armored.webp"
image volkaraHappyGreetingArmored = "images/Protagonists/Volkara/Volkara Happy Greeting armored.webp"

image volkaraArmedNeutralHappy = "images/Protagonists/Volkara/Volkara armored armed.webp"


layeredimage volkaraArmored:
    group poses:
        attribute basic default:
            "images/Protagonists/Volkara/Volkara Neutral Happy armored.webp" # 800-1500
        attribute greeting:
            "images/Protagonists/Volkara/Volkara Happy Greeting armored.webp" # 900-1500
        attribute armred:
            "images/Protagonists/Volkara/Volkara armored armed.webp" # 1000-1500
        attribute yeah:
            "images/Protagonists/Volkara/Volkara Yeah armored.webp" # 900-1500
        attribute armoredClever:
            "images/Protagonists/Volkara/Volkara armored Dagger and Cleaver.webp" # 900-1500

    group mouths:
        attribute neutralHappyMouth default if_any ["basic"]: #800-1500
            "images/Protagonists/Volkara/Volkara Neutral Happy mouth.webp"
        attribute neutralHappyMouth default if_any ["greeting","yeah","armoredClever"]:
            "images/Protagonists/Volkara/Volkara Neutral Happy mouth.webp"
            xpos 50
        attribute neutralHappyMouth default if_any ["armred"]:
            "images/Protagonists/Volkara/Volkara Neutral Happy mouth.webp"
            xpos 100

        attribute happyMouth if_any ["basic"]: #800-1400
            "images/Protagonists/Volkara/Volkara Happy Mouth.webp"
            ypos 100
        attribute happyMouth if_any ["armred"]:
            "images/Protagonists/Volkara/Volkara Happy Mouth.webp"
            ypos 100 xpos 100
        
        attribute happyMouth if_any ["greeting","yeah","armoredClever"]:
            "images/Protagonists/Volkara/Volkara Happy Mouth.webp"
            ypos 100 xpos 50
        
        attribute deltaMouth if_any["basic"]:# 1000-1500
            "images/Protagonists/Volkara/Volkara Delta Mouth.webp"
            xpos 200 
        attribute deltaMouth if_any["greeting","yeah","armoredClever"]:
            "images/Protagonists/Volkara/Volkara Delta Mouth.webp"
            xpos 100
        attribute deltaMouth if_any["armred"]:
            "images/Protagonists/Volkara/Volkara Delta Mouth.webp"
            

    group eyes:
        attribute heheh if_any["basic"]: #800-1500
            "images/Protagonists/Volkara/Volkara armored Heheh Eyes.webp"
        attribute heheh if_any["greeting","armred","yeah","armoredClever"]:
            "images/Protagonists/Volkara/Volkara armored Heheh Eyes.webp"
            xpos 50
        attribute heheh if_any["armred"]:
            "images/Protagonists/Volkara/Volkara armored Heheh Eyes.webp"
            xpos 100

        attribute meanEyes if_any["basic"]: #800-1500
            "images/Protagonists/Volkara/Volkara armored Mean Eyes.webp"
        attribute meanEyes if_any["greeting","yeah","armoredClever"]:
            "images/Protagonists/Volkara/Volkara armored Mean Eyes.webp"
            xpos 50
        attribute meanEyes if_any["armred"]:
            "images/Protagonists/Volkara/Volkara armored Mean Eyes.webp"
            xpos 100

image volkaraOnHorse = "images/Protagonists/Volkara/Volkara Neutral Happy armored on horse.webp"
image volkaraOnHorseHappyGreeting = "images/Protagonists/Volkara/Volkara Neutral Happy armored on horse greeting.webp"

image volkara34NeutralHappy = "images/Protagonists/Volkara/Volkara Neutral Happy 3quat.webp"
image volkara34NeutralHappyPoint = "images/Protagonists/Volkara/Volkara Neutral Happy hand 3quat.webp"
image volkara34Happy = "images/Protagonists/Volkara/Volkara Happy 3quat.webp"
image volkara34HappyPoint = "images/Protagonists/Volkara/Volkara Happy hand 3quat.webp"
image volkara34Sad = "images/Protagonists/Volkara/Volkara Sad 3quat.webp"
image volkara34SadPoint = "images/Protagonists/Volkara/Volkara Sad hand 3quat.webp"
image volkara34Suprized = "images/Protagonists/Volkara/Volkara Suprised 3quat.webp"

image volkara34NeutralHappyArmored = "images/Protagonists/Volkara/Volkara Neutral Happy 3quat armored.webp"

layeredimage volkara3quatArmored:
    group poses:
        attribute basic default:
            "images/Protagonists/Volkara/Volkara Neutral Happy 3quat armored.webp"
        attribute bentStand:
            "images/Protagonists/Volkara/Volkara arms forward 3quat armored.webp"
    
    group eyes:
        attribute normalEyes default:
            "images/Protagonists/Volkara/Volkara Neutral Eyes 3quat armored.webp"
        attribute sadEyes:
            "images/Protagonists/Volkara/Volkara Sad Eyes 3quat armored.webp"
        attribute meanEyes:
            "images/Protagonists/Volkara/Volkara Mean Eyes 3quat armored.webp"

    group mouths:
        attribute neutralHappyMouth default:
            "images/Protagonists/Volkara/Volkara Neutral Happy 3quat Mouth.webp"
        attribute happyMouth:
            "images/Protagonists/Volkara/Volkara 3-4 Happy Mouth.webp"
            ypos 100
        attribute OMouth:
            "images/Protagonists/Volkara/Volkara 3quat Armored Omouth.webp"
        attribute OMegaMouth:
            "images/Protagonists/Volkara/Volkara 3-4 OmegaMouth.webp"
            ypos 100
        attribute deltaMouth:
            "images/Protagonists/Volkara/Volkara Delta mouth 3quat.webp"

#this will be implemented soon
layeredimage volkara3quat:
    group poses:
        attribute basic default:
            "images/Protagonists/Volkara/Volkara Neutral Happy 3quat.webp"
        attribute nightOutfit:    
            "images/Protagonists/Volkara/Volkara Neutral Happy 3quat Nighttiem.webp"
        attribute nightOutfitPointy:
            "images/Protagonists/Volkara/Volkara Neutral Happy 3quat Nighttiem pointy.webp"
        attribute pointy:#900-1400
            "images/Protagonists/Volkara/Volkara Neutral Happy hand 3quat.webp"
        #attribute bent:
    
    
    group eyes:
        attribute normalEyes default if_any["basic","pointy"]:
            "images/Protagonists/Volkara/Volkara 3quat neutral eyes.webp"
        attribute normalEyes default if_any["nightOutfit", "nightOutfitPointy"]:
            "images/Protagonists/Volkara/Volkara 3quat neutral eyes hood.webp"

        attribute sadEyes if_any["basic","pointy"]:
            "images/Protagonists/Volkara/Volkara 3quat sad eyes.webp"
        attribute sadEyes if_any["nightOutfit", "nightOutfitPointy"]:
            "images/Protagonists/Volkara/Volkara 3quat sad eyes hood.webp"

        attribute meanEyes if_any["basic","pointy"]:
            "images/Protagonists/Volkara/Volkara 3quat Mean Eyes.webp"
        attribute meanEyes if_any["nightOutfit", "nightOutfitPointy"]:
            "images/Protagonists/Volkara/Volkara 3quat mean eyes Hood.webp"

        attribute lineEyes if_any["basic","pointy"]:
            "images/Protagonists/Volkara/Volkara Neutral Happy 3quat Line Eyes.webp"
        attribute lineEyes if_any["nightOutfit", "nightOutfitPointy"]:
            "images/Protagonists/Volkara/Volkara Neutral Happy 3quat line eyes hood.webp"
        
        attribute closedEyes if_any["basic","pointy"]:
            "images/Protagonists/Volkara/Volkara 3quat eyes closed.webp"
        attribute closedEyes if_any["nightOutfit", "nightOutfitPointy"]:
            "images/Protagonists/Volkara/Volkara Neutral Happy 3quat Closed eyes hood.webp"

    group mouths:
        attribute neutralHappyMouth default:
            "images/Protagonists/Volkara/Volkara Neutral Happy 3quat Mouth.webp"
            ypos -100
        attribute happyMouth:
            "images/Protagonists/Volkara/Volkara 3-4 Happy Mouth.webp"
        attribute OMouth:
            "images/Protagonists/Volkara/Volkara 3quat Armored Omouth.webp"
            ypos -100
        attribute OMegaMouth:
            "images/Protagonists/Volkara/Volkara 3-4 OmegaMouth.webp"
        attribute deltaMouth:
            "images/Protagonists/Volkara/Volkara Delta mouth 3quat.webp"
            ypos -100
            

image volkara34SittingHappy = "images/Protagonists/Volkara/Volkara Sitting 3quat Neutral Happy.webp"
image volkara34SittingLookingAtYou = "images/Protagonists/Volkara/Volkara Sitting 3quat looking at you.webp"

image volkaraDefeated = "images/Protagonists/Volkara/Volkara Neutral Happy 3quat armored 00.webp"

layeredimage volkaraFeety:
    group poses:
        attribute basic default:
            "images/Protagonists/Volkara/Volkara Neutral Happy.webp"
        attribute greeting:
            "images/Protagonists/Volkara/Volkara Happy Greeting.webp"
        attribute yeah:
            "images/Protagonists/Volkara/Volkara Yeah.webp"
        attribute nighttime:
            "images/Protagonists/Volkara/Volkara Neutral Happy Nigthtime.webp"
        attribute nighttimePillow:
            "images/Protagonists/Volkara/Volkara Happy Nigthtime Pillow.webp"

    group eyes:
        attribute neutralEyes default if_any['basic','greeting','yeah']:
            "images/Protagonists/Volkara/Volkara Neutral eyes.webp"
        attribute neutralEyes default if_any['nighttime','nighttimePillow']:
            "images/Protagonists/Volkara/Volkara Neutral Eyes Hood.webp"

        attribute sadEyes if_any['basic','greeting','yeah']:
            "images/Protagonists/Volkara/Volkara Sad Eyes.webp"
        attribute sadEyes if_any['nighttime','nighttimePillow']:
            "images/Protagonists/Volkara/Volkara sad hood.webp"

        attribute meanEyes if_any['basic','greeting','yeah']:
            "images/Protagonists/Volkara/Volkara Closed eyes.webp"
        attribute meanEyes if_any['nighttime','nighttimePillow']:
            "images/Protagonists/Volkara/Volkara closed eyes hood.webp"

        attribute closedEyes if_any['basic','greeting','yeah']:
            "images/Protagonists/Volkara/Volkara Happy Nigthtime Pillow.webp"
        attribute closedEyes if_any['nighttime','nighttimePillow']:
            "images/Protagonists/Volkara/Volkara Happy Nigthtime Pillow.webp"

    group mouths:
        attribute neutralHappyMouth: #800-1500
            "images/Protagonists/Volkara/Volkara Neutral Happy mouth.webp"
        attribute happyMouth: #800-1400
            "images/Protagonists/Volkara/Volkara Happy Mouth.webp"
            xpos 1
        attribute deltaMouth:# 1000-1500
            "images/Protagonists/Volkara/Volkara Delta Mouth.webp"
            xpos -97 ypos -99





layeredimage volkaraHorsey: #1200-2500
    group poses:
        attribute based default: 
            "images/Protagonists/Volkara/Volkara Neutral Happy armored on horse.webp"
        attribute greeting: 
            "images/Protagonists/Volkara/Volkara Neutral Happy armored on horse greeting.webp"
        attribute armedSword:
            "images/Protagonists/Volkara/Volkara Armed armored on horse.webp"
    group eyes:
        attribute heheh: #800-1500
            "images/Protagonists/Volkara/Volkara armored Heheh Eyes.webp" 
            xpos 289 ypos -17
        attribute meanEyes:
            "images/Protagonists/Volkara/Volkara armored Mean Eyes.webp"
            xpos 289 ypos -17
    group mouths:
        attribute happyMouth: 
            "images/Protagonists/Volkara/Volkara Happy Mouth.webp" #800 #1400
            xpos 290 ypos 83

#Megabazus
layeredimage megabazus:
    group poses:
        attribute base default:
            "images/Protagonists/Megabazus/Megabazus Based.webp"
        attribute armored:
            "images/Protagonists/Megabazus/Megabazus Armored Based.webp"
        attribute armoredGreet:
            "images/Protagonists/Megabazus/Megabazus Armored Greeting.webp"
        attribute base34:
            "images/Protagonists/Megabazus/Megabazus 3-4.webp"
        attribute armored34:
            "images/Protagonists/Megabazus/Megabazus 3-4 Armored.webp"
        attribute item34Armored:
            "images/Protagonists/Megabazus/Megabazus 3-4 Armored Item.webp"
        attribute point34Armored:
            "images/Protagonists/Megabazus/Megabazus 3-4 Armored Point.webp"
        attribute horse:
            "images/Protagonists/Megabazus/Megabazus Armored Based Horse.webp"
        attribute horseCommand:
            "images/Protagonists/Megabazus/Megabazus Armored Commanding Horse.webp"

    group eyes:
        attribute neutralEyes default if_not["base34","armored34","horse","horseCommand","point34Armored","item34Armored" ]: #420 from top 390 from side
            "images/Protagonists/Megabazus/Megabazus Neutral Eyes.webp"
        attribute neutralEyes default if_any["base34","armored34","point34Armored","item34Armored" ]: #different image
            "images/Protagonists/Megabazus/Megabazus 3-4 Neutral Eyes.webp"
        attribute neutralEyes default if_any["horse","horseCommand"]:
            "images/Protagonists/Megabazus/Megabazus Neutral Eyes.webp" #340 from top 630 from side
            ypos -83 xpos 230
        
        attribute meanEyes if_not["base34","armored34","horse","horseCommand","point34Armored","item34Armored"  ]:
            "images/Protagonists/Megabazus/Megabazus Mean Eyes.webp"
        attribute meanEyes if_any["base34","armored34","point34Armored","item34Armored" ]:
            "images/Protagonists/Megabazus/Megabazus 3-4 Mean Eyes.webp"
        attribute meanEyes if_any["horse","horseCommand"]:
            "images/Protagonists/Megabazus/Megabazus Mean Eyes.webp"
            ypos -83 xpos 230
        
        attribute sadEyes if_not["base34","armored34","horse","horseCommand","point34Armored","item34Armored"  ]:
            "images/Protagonists/Megabazus/Megabazus Sad Face.webp"
        attribute sadEyes if_any["base34","armored34","point34Armored" ]:
            "images/Protagonists/Megabazus/Megabazus 3-4 Sad Eyes.webp"
        attribute sadEyes if_any["horse","horseCommand"]:
            "images/Protagonists/Megabazus/Megabazus Sad Face.webp"
            ypos -83 xpos 230
        
        
    group mouths:
        attribute neutralHappyMouth default if_not["base34","armored34","horse","horseCommand","point34Armored","item34Armored" ]:
            "images/Protagonists/Megabazus/Megabazus Neutral Happy Mouth.webp"
        attribute neutralHappyMouth default if_any["base34","armored34","point34Armored","item34Armored"]:
            "images/Protagonists/Megabazus/Megabazus 3-4 Neutral Happy Mouth.webp" 
        attribute neutralHappyMouth default if_any["horse","horseCommand"]:
            "images/Protagonists/Megabazus/Megabazus Neutral Happy Mouth.webp"
            ypos -84 xpos 230

        attribute happyMouth if_not["base34","armored34","horse","horseCommand","point34Armored","item34Armored" ]:
            "images/Protagonists/Megabazus/Megabazus Happy Mouth.webp"
        attribute happyMouth if_any["base34","armored34","point34Armored","item34Armored"]:
            "images/Protagonists/Megabazus/Megabazus 3-4 Happy Mouth.webp" 
        attribute happyMouth if_any["horse","horseCommand"]:
            "images/Protagonists/Megabazus/Megabazus Happy Mouth.webp"
            ypos -84 xpos 230

        attribute OMouth if_not["base34","armored34","horse","horseCommand","point34Armored","item34Armored" ]:
            "images/Protagonists/Megabazus/Megabazus OMouth.webp"
        attribute OMouth if_any["base34","armored34","point34Armored","item34Armored"]:
            "images/Protagonists/Megabazus/Megabazus 3-4 OMouth.webp" 
        attribute OMouth if_any["horse","horseCommand"]:
            "images/Protagonists/Megabazus/Megabazus OMouth.webp"
            ypos -84 xpos 230

        attribute angryMouth if_not["base34","armored34","horse","horseCommand","point34Armored","item34Armored" ]:
            "images/Protagonists/Megabazus/Megabazus Angry Mouth.webp"
        attribute angryMouth if_any["base34","armored34","point34Armored","item34Armored"]:
            "images/Protagonists/Megabazus/Megabazus 3-4 Angry Mouth.webp" 
        attribute angryMouth if_any["horse","horseCommand"]:
            "images/Protagonists/Megabazus/Megabazus Angry Mouth.webp"
            ypos -84 xpos 230
        
        attribute frown if_not["base34","armored34","horse","horseCommand","point34Armored","item34Armored" ]:
            "images/Protagonists/Megabazus/Megabazus Frown.webp"
        attribute frown if_any["base34","armored34","point34Armored","item34Armored"]:
            "images/Protagonists/Megabazus/Megabazus 3-4 Frown.webp" 
        attribute frown if_any["horse","horseCommand"]:
            "images/Protagonists/Megabazus/Megabazus Frown.webp"
            ypos -84 xpos 230

#Regius

layeredimage regius:
    group poses:
        attribute basic default:
            "images/Protagonists/Regius/Regius.webp" #660-1400
        attribute armored:
            "images/Protagonists/Regius/Regius Armored.webp" #660-1500
        attribute armoredGreet:
            "images/Protagonists/Regius/Regius Armored Greet.webp" #660-1500
        attribute camelArmor:
            "images/Protagonists/Regius/Regius Armored on Camel.webp" #1600-2800
        attribute camelGreet:
            "images/Protagonists/Regius/Regius Armored on Camel Greet.webp" #1600-2800
        attribute camelAttack:
            "images/Protagonists/Regius/Regius Armored on Camel Battle.webp" #1600-2800
    group eyes:
        attribute neutralEyes default if_any["basic"]:
            "images/Protagonists/Regius/Regius Neutral eyes.webp"
            ypos -100
        attribute neutralEyes default if_any["camelArmor","camelGreet","camelAttack"]:
            "images/Protagonists/Regius/Regius Neutral eyes.webp"
            xpos 389 ypos 55
        attribute neutralEyes default if_any["armored","armoredGreet"]:
            "images/Protagonists/Regius/Regius Neutral eyes.webp"
            #ypos 100
        
        attribute meanEyes if_any["basic"]:
            "images/Protagonists/Regius/Regius Mean Eyes.webp"
            ypos -100
        attribute meanEyes if_any["camelArmor","camelGreet","camelAttack"]:
            "images/Protagonists/Regius/Regius Mean Eyes.webp"
            xpos 389 ypos 56
        attribute meanEyes if_any["armored","armoredGreet"]:
            "images/Protagonists/Regius/Regius Mean Eyes.webp"
            ypos 100    
        
        attribute sadEyes if_any["basic"]:
            "images/Protagonists/Regius/Regius Sad Eyes.webp"
        attribute sadEyes if_any["camelArmor","camelGreet","camelAttack"]:
            "images/Protagonists/Regius/Regius Sad Eyes.webp"
            xpos 389 ypos 156
        attribute sadEyes if_any["armored","armoredGreet"]:
            "images/Protagonists/Regius/Regius Sad Eyes.webp"
            ypos 100 
        
        #atttibute sadEyes:
    group mouths:
        attribute neutralMouth default if_any["basic"]:
            "images/Protagonists/Regius/Regius Neutral Happy Mouth.webp"
            ypos -100
        attribute neutralMouth default if_any["camelArmor","camelGreet","camelAttack"]:
            "images/Protagonists/Regius/Regius Neutral Happy Mouth.webp"
            xpos 389 ypos 57
        attribute neutralMouth default if_any["armored","armoredGreet"]:
            "images/Protagonists/Regius/Regius Neutral Happy Mouth.webp"
            ypos 100

        attribute angryMouth if_any["basic"]:
            "images/Protagonists/Regius/Regius Angry mouth.webp"
            ypos -100
        attribute angryMouth if_any["camelArmor","camelGreet","camelAttack"]:
            "images/Protagonists/Regius/Regius Angry mouth.webp"
            xpos 389 ypos 56
        attribute angryMouth if_any["armored","armoredGreet"]:
            "images/Protagonists/Regius/Regius Angry mouth.webp"
            ypos 100

        attribute happyMouth if_any["basic"]:
            "images/Protagonists/Regius/Regius Happy Mouth.webp"
            ypos -100
        attribute happyMouth if_any["camelArmor","camelGreet","camelAttack"]:
            "images/Protagonists/Regius/Regius Happy Mouth.webp" 
            xpos 389 ypos 56
        attribute happyMouth if_any["armored","armoredGreet"]:
            "images/Protagonists/Regius/Regius Happy Mouth.webp" 
            ypos 100
        
        attribute OMouth if_any["basic"]:
            "images/Protagonists/Regius/Regius O Mouth.webp"
        attribute OMouth if_any["camelArmor","camelGreet","camelAttack"]:
            "images/Protagonists/Regius/Regius O Mouth.webp"
            xpos 389 ypos 156
        attribute OMouth if_any["armored","armoredGreet"]:
            "images/Protagonists/Regius/Regius O Mouth.webp"
            ypos 100
        
        attribute sadMouth if_any["basic"]:
            "images/Protagonists/Regius/Regius Sad Mouth.webp"
        attribute sadMouth if_any["camelArmor","camelGreet","camelAttack"]:
            "images/Protagonists/Regius/Regius Sad Mouth.webp"
            xpos 389 ypos 156
        attribute sadMouth if_any["armored","armoredGreet"]:
            "images/Protagonists/Regius/Regius Sad Mouth.webp"
            ypos 100

layeredimage regius34:
    group poses:
        attribute basic default:
            "images/Protagonists/Regius/Regius 3-4.webp"
        attribute pointing:
            "images/Protagonists/Regius/Regius 3-4 Pointy.webp"
        attribute greeting:
            "images/Protagonists/Regius/Regius 3-4 Greeting.webp"
        attribute armed:
            "images/Protagonists/Regius/Regius 3-4 Armored Armed Angry.webp"
        attribute armored:
            "images/Protagonists/Regius/Regius 3-4 Armored arms down.webp"
        attribute armoredPointing:
            "images/Protagonists/Regius/Regius 3-4 Armored.webp"

    group eyes:
        attribute neutralEyes default if_not["armed" , "armored" , "armoredPointing" ]:
            "images/Protagonists/Regius/Regius 3-4 Neutral Eyes.webp"
        attribute neutralEyes default if_any["armed" , "armored" , "armoredPointing" ]:
            "images/Protagonists/Regius/Regius 3-4 Neutral Eyes.webp"
            ypos 100
        attribute lineEyes if_not["armed" , "armored" , "armoredPointing" ]:
            "images/Protagonists/Regius/Regius 3-4 Line eyes.webp"
        attribute lineEyes if_any["armed" , "armored" , "armoredPointing" ]:
            "images/Protagonists/Regius/Regius 3-4 Line eyes.webp"
            ypos 100
        attribute meanEyes if_not["armed" , "armored" , "armoredPointing" ]:
            "images/Protagonists/Regius/Regius 3-4 Mean Eyes.webp"
            xpos -200 ypos -100 
        attribute meanEyes if_any["armed" , "armored" , "armoredPointing" ]:
            "images/Protagonists/Regius/Regius 3-4 Mean Eyes.webp"
            xpos -200 
        attribute annoyedEyes if_not["armed" , "armored" , "armoredPointing" ]:
            "images/Protagonists/Regius/Regius 3-4 Annoyed Eyes.webp"
            xpos -200 ypos -100
        attribute annoyedEyes if_any["armed" , "armored" , "armoredPointing" ]:
            "images/Protagonists/Regius/Regius 3-4 Annoyed Eyes.webp"
        attribute sadEyes if_not["armed" , "armored" , "armoredPointing" ]:
            "images/Protagonists/Regius/Regius 3-4 Sad Eyes.webp"
        attribute sadEyes if_any["armed" , "armored" , "armoredPointing" ]:
            "images/Protagonists/Regius/Regius 3-4 Sad Eyes.webp"
            ypos 100

    group mouths:
        attribute neutralHappyMouth default if_not["armed" , "armored" , "armoredPointing" ]:
            "images/Protagonists/Regius/Regius 3-4 Neutal Happy Mouth.webp"
        attribute neutralHappyMouth default if_any["armed" , "armored" , "armoredPointing" ]:
            "images/Protagonists/Regius/Regius 3-4 Neutal Happy Mouth.webp"
            ypos 100
        attribute annoyedMouth if_not["armed" , "armored" , "armoredPointing" ]:
            "images/Protagonists/Regius/Regius 3-4 Annoyed Mouth.webp"
            ypos -100
        
        attribute angryMouth if_not["armed" , "armored" , "armoredPointing" ]:
            "images/Protagonists/Regius/Regius 3-4 Angry Mouth.webp"
            xpos -400 ypos -100 
        attribute angryMouth if_any["armed" , "armored" , "armoredPointing" ]:
            "images/Protagonists/Regius/Regius 3-4 Angry Mouth.webp"
            xpos -200 
        attribute happyMouth if_not["armed" , "armored" , "armoredPointing" ]:
            "images/Protagonists/Regius/Regius 3-4 Happy Mouth.webp"
        attribute happyMouth if_any["armed" , "armored" , "armoredPointing" ]:
            "images/Protagonists/Regius/Regius 3-4 Happy Mouth.webp"
            ypos 100
        attribute OMouth if_not["armed" , "armored" , "armoredPointing" ]:
            "images/Protagonists/Regius/Regius 3-4 OMouth.webp"
        attribute OMouth if_any["armed" , "armored" , "armoredPointing" ]:
            "images/Protagonists/Regius/Regius 3-4 OMouth.webp"
            ypos 100

image regius34ShieldBash = "images/Protagonists/Regius/Regius 3-4 Armored Shield Bash.webp"

    #Fatima
layeredimage fatima:
    group poses:
        attribute onFoot default:
            "images/Protagonists/Regius/Regiuss gf/Fatima.webp" # 800 - 1400
        attribute onFootGreet:
            "images/Protagonists/Regius/Regiuss gf/Fatima Greeting.webp" # 900 - 1500
        attribute onFootArmored:
            "images/Protagonists/Regius/Regiuss gf/Fatima Armored.webp" # 900 - 1500
        attribute onCamel:
            "images/Protagonists/Regius/Regiuss gf/Fatima Camel.webp" # 1600 - 2800
        attribute onCamelGreet:
            "images/Protagonists/Regius/Regiuss gf/Fatima Camel Greeting.webp" # 1600 - 2800
        attribute onCamelAttack:
            "images/Protagonists/Regius/Regiuss gf/Fatima Camel Attack.webp" # 2800 - 2800

    group eyes:
        attribute neutralEyes if_any["onFoot"] default:  # 800 - 1400
            "images/Protagonists/Regius/Regiuss gf/Fatima Neutral Eyes.webp"
        attribute neutralEyes if_any["onFootArmored"] default:  # 800 - 1400
            "images/Protagonists/Regius/Regiuss gf/Fatima Neutral Eyes.webp"
            ypos 100    
        attribute neutralEyes if_any["onFootGreet"] default:  # 800 - 1400
            "images/Protagonists/Regius/Regiuss gf/Fatima Neutral Eyes.webp"
            ypos 100 xpos 100
        attribute neutralEyes if_any["onCamel","onCamelGreet" , "onCamelAttack" ] default:  # 800 - 1400
            "images/Protagonists/Regius/Regiuss gf/Fatima Neutral Eyes.webp"
            xpos 322 ypos 174

        attribute angryEyes if_any["onFoot"]:
            "images/Protagonists/Regius/Regiuss gf/Fatima angry eyes.webp" # 900 - 1500
            ypos -100 
        attribute angryEyes if_any["onFootArmored"]:
            "images/Protagonists/Regius/Regiuss gf/Fatima angry eyes.webp" # 900 - 1500
        attribute angryEyes if_any["onFootGreet"]:    
            "images/Protagonists/Regius/Regiuss gf/Fatima angry eyes.webp"
            xpos 100
        attribute angryEyes if_any["onCamel","onCamelGreet" , "onCamelAttack"]:
            "images/Protagonists/Regius/Regiuss gf/Fatima angry eyes.webp" # 900 - 1500
            xpos 322 ypos 74

    group mouths:
        attribute neutralHappyMouth if_any["onFoot"] default: # 800 - 1400
            "images/Protagonists/Regius/Regiuss gf/Fatima Neutral Happy Mouth.webp"
        attribute neutralHappyMouth if_any["onFootArmored"] default: # 800 - 1400
            "images/Protagonists/Regius/Regiuss gf/Fatima Neutral Happy Mouth.webp"
            ypos 100
        attribute neutralHappyMouth if_any["onFootGreet"] default: # 800 - 1400
            "images/Protagonists/Regius/Regiuss gf/Fatima Neutral Happy Mouth.webp"
            ypos 100 xpos 100
        attribute neutralHappyMouth if_any["onCamel","onCamelGreet", "onCamelAttack"] default: # 800 - 1400
            "images/Protagonists/Regius/Regiuss gf/Fatima Neutral Happy Mouth.webp"
            xpos 322 ypos 174

        attribute happyMouth if_any["onFoot"]:
            "images/Protagonists/Regius/Regiuss gf/Fatima Happy mouth.webp" # 800 - 1400
            
        attribute happyMouth if_any["onFootArmored"]:
            "images/Protagonists/Regius/Regiuss gf/Fatima Happy mouth.webp" # 800 - 1400
            ypos 100
        attribute happyMouth if_any["onFootGreet"]:
            "images/Protagonists/Regius/Regiuss gf/Fatima Happy mouth.webp" # 800 - 1400
            ypos 100 xpos 100
        attribute happyMouth if_any["onCamel","onCamelGreet", "onCamelAttack"]:
            "images/Protagonists/Regius/Regiuss gf/Fatima Happy mouth.webp" # 800 - 1400
            xpos 322 ypos 174


        attribute angryMouth if_any["onFoot"]:
            "images/Protagonists/Regius/Regiuss gf/Fatima supang mouth.webp" # 900 - 1500
            ypos -100
        attribute angryMouth if_any["onFootArmored"]:
            "images/Protagonists/Regius/Regiuss gf/Fatima supang mouth.webp" # 900 - 1500
        attribute angryMouth if_any["onFootGreet"]:
            "images/Protagonists/Regius/Regiuss gf/Fatima supang mouth.webp"
            xpos 100
        attribute angryMouth if_any["onCamel","onCamelGreet" , "onCamelAttack"]:
            "images/Protagonists/Regius/Regiuss gf/Fatima supang mouth.webp" # 900 - 1500
            xpos 322 ypos 174

#Kabiwa

layeredimage kabiwa:
    group poses:
        attribute based default:
            "images/Protagonists/Kabiwa/Kabiwa.webp"
        attribute armored:
            "images/Protagonists/Kabiwa/Kabiwa Armored.webp"
        attribute annoyedPose:
            "images/Protagonists/Kabiwa/Kabiwa Annoyed Pose.webp"
        attribute greetingPose:
            "images/Protagonists/Kabiwa/Kabiwa Greeting.webp"

    group mouths:
        attribute neutralHappyMouth default:
            "images/Protagonists/Kabiwa/Kabiwa Happy mouth.webp"
        attribute happyMouth:
            "images/Protagonists/Kabiwa/Kabiwa Happyer mouth.webp"
        attribute deltaMouth:
            "images/Protagonists/Kabiwa/Kabiwa Delta Mouth.webp"
        attribute OMouth:
            "images/Protagonists/Kabiwa/Kabiwa o mouth.webp"
        attribute annoyedMouth:
            "images/Protagonists/Kabiwa/Kabiwa Annoyed Face.webp"

    group eyes:
        attribute normalEyes default:
            "images/Protagonists/Kabiwa/Kabiwa Up Eyes.webp"
        attribute sadEyes:
            "images/Protagonists/Kabiwa/Kabiwa Sad Eyes.webp"
        attribute meanEyes:
            "images/Protagonists/Kabiwa/Kabiwa Mean Eyes.webp"

#NPCs

#Jameisa

#Ectabana

image eliteAtossaGuard1 = "images/NPCs/Jamesia/Ectabana/jamesian immortal jamesian female v1.webp"
image eliteAtossaGuard2 = "images/NPCs/Jamesia/Ectabana/jamesian immortal oxatrotu female v1.webp"
image eliteDariusGuard1 = "images/NPCs/Jamesia/Ectabana/jamesian immortal jamesian male v1.webp"
image eliteDariusGuard1Greeting = "images/NPCs/Jamesia/Ectabana/jamesian immortal jamesian male Greeting.webp"
image eliteDariusGuard1Happy = "images/NPCs/Jamesia/Ectabana/jamesian immortal jamesian male v1 happy.webp"
image eliteDariusGuard1Sad = "images/NPCs/Jamesia/Ectabana/jamesian immortal jamesian male v1 sad.webp"

image eliteDariusGuard2 = "images/NPCs/Jamesia/Ectabana/jamesian immortal jamesian male2 v1.webp"

#Palace Workers
image foodServer = "images/NPCs/Jamesia/Ectabana/Food Server Standing.webp"
image foodServerItem = "images/NPCs/Jamesia/Ectabana/Food Server Standing Hold Out.webp"
image foodServerHand = "images/NPCs/Jamesia/Ectabana/Food Server Hand Over.webp"
image foodServerCartSide = "images/NPCs/Jamesia/Ectabana/Food Server with cart.webp"

#EctabanaShopLady
image ectabanaShopLadyGreet = "images/NPCs/Jamesia/Ectabana/Ectabana Shop Lady.webp"
image ectabanaShopLady = "images/NPCs/Jamesia/Ectabana/Ectabana Shop Lady Neutral Happy.webp"
image ectabanaShopLadyHappy = "images/NPCs/Jamesia/Ectabana/Ectabana Shop Lady Happy.webp"
image ectabanaShopLadySad = "images/NPCs/Jamesia/Ectabana/Ectabana Shop Lady Sad.webp"
image ectabanaShopLadyMad = "images/NPCs/Jamesia/Ectabana/Ectabana Shop Lady Mad.webp"
image ectabanaShopLadyItem = "images/NPCs/Jamesia/Ectabana/Ectabana Shop Lady Item.webp"

#the 2 who beat ato'ssa
image zhemzhuGirl = "images/NPCs/Jamesia/Ectabana/zhemzu korkin lady.webp"
image tyattuDude = "images/NPCs/Jamesia/Ectabana/jamesian dude.webp"

#Zwotilya/Serinians

#ShopDudeOfZwotilya
image seriniumShopHello = "images/NPCs/Jamesia/Zwotilya/come agian Happy Serinium Shop Dude.webp"
image seriniumShopDude = "images/NPCs/Jamesia/Zwotilya/Neutral Happy Serinium Shop Dude.webp"
image seriniumShopDissapoint = "images/NPCs/Jamesia/Zwotilya/Serinium Shop Dude dissapointed.webp"
image seriniumShopGiveItems = "images/NPCs/Jamesia/Zwotilya/Serinium Shop Dude give items.webp"
image seriniumShopNoMoneys = "images/NPCs/Jamesia/Zwotilya/Serinium Shop Dude you have no moneyz.webp"
#Nyazhmyui
image nyazhmyuiByeByeKeys = "images/NPCs/Jamesia/Zwotilya/Nyazhmyui bye bye with keys.webp"
image nyazhmyuiHappyGreeting = "images/NPCs/Jamesia/Zwotilya/Nyazhmyui Happy Greeting.webp"
image nyazhmyuiHappyGreeting2 = "images/NPCs/Jamesia/Zwotilya/Nyazhmyui Happy Greeting 2.webp"
image nyazhmyuiHappyCheeseKeys = "images/NPCs/Jamesia/Zwotilya/Nyazhmyui Happy with keys and cheese.webp"
image nyazhmyuiHappy = "images/NPCs/Jamesia/Zwotilya/Nyazhmyui Happy.webp"
image nyazhmyuiNeutralHappy = "images/NPCs/Jamesia/Zwotilya/Nyazhmyui Netrual Happy.webp"
image nyazhmyuiGivingItem = "images/NPCs/Jamesia/Zwotilya/Nyazhmyui putting item on counter.webp"
image nyazhmyuiNoMoney = "images/NPCs/Jamesia/Zwotilya/Nyazhmyui sorry you don't have the money.webp"
image nyazhmyuiBack = "images/NPCs/Jamesia/Zwotilya/Nyazhmyui from behind.webp"

#Kworix Mine
    #Cooking Lady
image shataCookingLadyYay = "images/NPCs/Jamesia/Kwortix/Kwortix Mine/Shata Cooking lady yay.webp"
image shataCookingLadyFreed = "images/NPCs/Jamesia/Kwortix/Kwortix Mine/Shata Cooking lady freed.webp"
image shataCookingLadyHappy = "images/NPCs/Jamesia/Kwortix/Kwortix Mine/Shata Cooking lady yay unchained.webp"
image shataCookingLadyScared = "images/NPCs/Jamesia/Kwortix/Kwortix Mine/Shata Cooking lady Scared.webp"
image shataCookingLadyFleeFront = "images/NPCs/Jamesia/Kwortix/Kwortix Mine/Shata Cooking Lady flee front.webp"
image shataCookingLadyFleeBack = "images/NPCs/Jamesia/Kwortix/Kwortix Mine/Shata Cooking Lady flee behind.webp"
image shataCookingLadyShocked = "images/NPCs/Jamesia/Kwortix/Kwortix Mine/Shata Cooking lady Shocked.webp"
image shataCookingLadySlaveLittleHappy = "images/NPCs/Jamesia/Kwortix/Kwortix Mine/Shata Cooking lady mini yay.webp"
image shataCookingLadySlave = "images/NPCs/Jamesia/Kwortix/Kwortix Mine/Kwortix mine kitchen used Shata Slave.webp"
image shataCookingLadySlaveSad = Composite( ( 800,1400 ) , ( 0,0 ), "images/NPCs/Jamesia/Kwortix/Kwortix Mine/Shata Cooking lady mini yay.webp" ,
    (0,0) , "images/NPCs/Jamesia/Kwortix/Kwortix Mine/Shata Cooking lady Sad Enslaved.webp" )
image shataCookingLadyWorried = "images/NPCs/Jamesia/Kwortix/Kwortix Mine/Shata Cooking lady worried.webp"
image shataCookingLady34Worried = "images/NPCs/Jamesia/Kwortix/Kwortix Mine/Shata Cooking lady 34Scared.webp"
    #slaves
image shataSlave1 = "images/NPCs/Jamesia/Kwortix/Kwortix Mine/Shata slave 1 yeah.webp"
image shataSlave2 = "images/NPCs/Jamesia/Kwortix/Kwortix Mine/Shata slave 2 yeah.webp"
image shataSlave2Sad = "images/NPCs/Jamesia/Kwortix/Kwortix Mine/Shata slave 2 yeah nah.webp"
image shataSlave3 = "images/NPCs/Jamesia/Kwortix/Kwortix Mine/Shata slave 3 yeah.webp"
image shataSlave4 = "images/NPCs/Jamesia/Kwortix/Kwortix Mine/Shata slave 4 yeah.webp"
image shataDoggoSlave = "images/NPCs/Jamesia/Kwortix/Kwortix Mine/Shata Slave Summoner yeah.webp"
image shataDoggoSlaveSad = Composite(( 700 , 1200 ),( 0,0 ),"images/NPCs/Jamesia/Kwortix/Kwortix Mine/Shata Slave Summoner yeah.webp" ,
    ( 0,0 ),"images/NPCs/Jamesia/Kwortix/Kwortix Mine/Shata Slave Summoner yeah nah.webp" )

#Kwortix City
    #Tazatu
image tazatuHappy = "images/NPCs/Jamesia/Kwortix/Kwortix City/kwortix motel dude happy.webp"
image tazatuHappyGreeting = "images/NPCs/Jamesia/Kwortix/Kwortix City/kwortix motel dude happy greeting.webp"
image tazatuItem = "images/NPCs/Jamesia/Kwortix/Kwortix City/kwortix motel dude giving item.webp"
image tazatuHandsInFrontOf = "images/NPCs/Jamesia/Kwortix/Kwortix City/kwortix motel dude giving item hands.webp"
image tazatuBehind = "images/NPCs/Jamesia/Kwortix/Kwortix City/kwortix motel dude behind.webp"
image tazatuSad = "images/NPCs/Jamesia/Kwortix/Kwortix City/kwortix motel dude sad.webp"
image tazatuMad = "images/NPCs/Jamesia/Kwortix/Kwortix City/kwortix motel dude mad.webp"
image tazatuKeys = "images/NPCs/Jamesia/Kwortix/Kwortix City/kwortix motel dude keys.webp"
image tazatuQuestioning = "images/NPCs/Jamesia/Kwortix/Kwortix City/kwortix motel dude questioning.webp"
image tazatuOh = "images/NPCs/Jamesia/Kwortix/Kwortix City/kwortix motel dude Oh.webp"
image tazatuExtraHappy = "images/NPCs/Jamesia/Kwortix/Kwortix City/kwortix motel dude extra happy.webp"
image tazatuAnnoyed = "images/NPCs/Jamesia/Kwortix/Kwortix City/kwortix motel dude annoyed.webp"
    #Tyetkrei
image tyetkreiHappy = "images/NPCs/Jamesia/Kwortix/Kwortix City/kwortix shop lady Happy.webp"
image tyetkreiHappyGreeting = "images/NPCs/Jamesia/Kwortix/Kwortix City/kwortix shop lady Happy greeting.webp"
image tyetkreiItem = "images/NPCs/Jamesia/Kwortix/Kwortix City/kwortix shop lady item.webp"
image tyetkreiItemUppa = "images/NPCs/Jamesia/Kwortix/Kwortix City/kwortix shop lady item uppa.webp"
image tyetkreiMad = "images/NPCs/Jamesia/Kwortix/Kwortix City/kwortix shop lady Mad.webp"
image tyetkreiSad = "images/NPCs/Jamesia/Kwortix/Kwortix City/kwortix shop lady sad.webp"
image tyetkreiNope = "images/NPCs/Jamesia/Kwortix/Kwortix City/kwortix shop lady nope.webp"


#Takuria
    #Hwassak
image hwassakHappyGreeting = "images/NPCs/Takuria/Happy Greeting Hwassak.webp"
image hwassakHappy = "images/NPCs/Takuria/Happy Hwassak.webp"
image hwassakHappyWink = "images/NPCs/Takuria/Happy Hwassak Wink.webp"
image hwassakNeutralHappy = "images/NPCs/Takuria/Neutral Happy Hwassak.webp"
image hwassakSad = "images/NPCs/Takuria/Sad Hwassak.webp"
image hwassakItem = "images/NPCs/Takuria/Item Hwassak.webp"
    #Yiwatsyoh
image yiwatsyohBack = "images/NPCs/Takuria/Yiwatsyoh Back.webp"
image yiwatsyohHappyGreeting = "images/NPCs/Takuria/Yiwatsyoh Happy Greeting.webp"
image yiwatsyohHappy = "images/NPCs/Takuria/Yiwatsyoh Happy.webp"
image yiwatsyohHappyClosedEyes = "images/NPCs/Takuria/Yiwatsyoh Happy Closed Eyes.webp"
image yiwatsyohNeutralHappy = "images/NPCs/Takuria/Yiwatsyoh Netrual Happy.webp"
image yiwatsyohItem = "images/NPCs/Takuria/Yiwatsyoh item.webp"
image yiwatsyohMad = "images/NPCs/Takuria/Yiwatsyoh Mad.webp"
image yiwatsohNope = "images/NPCs/Takuria/Yiwatsyoh Nope.webp"
image yiwatsyohSad = "images/NPCs/Takuria/Yiwatsyoh Sad.webp"
image yiwatsyohWink = "images/NPCs/Takuria/Yiwatsyoh Happy WInk.webp"
image yiwatsyohSuprized = "images/NPCs/Takuria/Yiwatsyoh Suprized.webp"
    #Keimdak
image keimdakGreeting = "images/NPCs/Takuria/Keimdak Greeting.webp"
image keimdakHappy = "images/NPCs/Takuria/Keimdak Happy.webp"
image keimdakNeutralHappy = "images/NPCs/Takuria/Keimdak Netrual Happy.webp"
image keimdakItem = "images/NPCs/Takuria/Keimdak item.webp"
image keimdakNope = "images/NPCs/Takuria/Keimdak Nope.webp"
image keimdakSad = "images/NPCs/Takuria/Keimdak Sad.webp"
image keimdakGTFO = "images/NPCs/Takuria/Keimdak GTFO.webp"

    #mauhin
layeredimage mauhin:
    group poses:
        attribute basic default:
            "images/NPCs/Takuria/Mauhin.webp"
        attribute greeting:
            "images/NPCs/Takuria/Mauhin Greeting.webp"
        attribute arms2Side:
            "images/NPCs/Takuria/Mauhin Spreadstand.webp"
        attribute onOstrich:
            "images/NPCs/Takuria/Mauhin on Ostrich.webp"

    group eyes:
        attribute neutralEyes default if_not["onOstrich"]:
            "images/NPCs/Takuria/Mauhin Nuetral Eyes.webp"
        attribute neutralEyes default if_any["onOstrich"]:
            "images/NPCs/Takuria/Mauhin Nuetral Eyes.webp"
            xpos 207 ypos 70

        attribute meanEyes if_not["onOstrich"]:
            "images/NPCs/Takuria/Mauhin Mean Eyes.webp"
        attribute MeanEyes if_any["onOstrich"]:
            "images/NPCs/Takuria/Mauhin Mean Eyes.webp"
            xpos 207 ypos 70

        attribute sadEyes if_not["onOstrich"]:
            "images/NPCs/Takuria/Mauhin Sad Eyes.webp"
        attribute sadEyes if_any["onOstrich"]:
            "images/NPCs/Takuria/Mauhin Sad Eyes.webp"
            xpos 207 ypos 70

    group mouths:
        attribute neutralHappyMouth default if_not["onOstrich"]:
            "images/NPCs/Takuria/Mauhin Neutral happy Mouth.webp"
        attribute neutralHappyMouth default if_any["onOstrich"]:
            "images/NPCs/Takuria/Mauhin Neutral happy Mouth.webp"
            xpos 207 ypos 70

        attribute happyMouth if_not["onOstrich"]:
            "images/NPCs/Takuria/Mauhin Happy Mouth.webp"
        attribute happyMouth if_any["onOstrich"]:
            "images/NPCs/Takuria/Mauhin Happy Mouth.webp"
            xpos 207 ypos 70

        attribute oMouth if_not["onOstrich"]:
            "images/NPCs/Takuria/Mauhin Spreadstand OMouth.webp"
        attribute oMouth if_any["onOstrich"]:
            "images/NPCs/Takuria/Mauhin Spreadstand OMouth.webp"
            xpos 207 ypos 70

    #takurium shopkeep

    #zarato-takurian shopkeep

#Jamesian Troopers
image jamesianHeavySpearDude = "images/NPCs/Jamesia/Troopers/Jamesian Heavy Spear Boy.webp"
image jamesianHeavySpearGirl = "images/NPCs/Jamesia/Troopers/Jamesian Heavy Spear Girl.webp"
image jamesianHeavySpearGirlGreeting = "images/NPCs/Jamesia/Troopers/Jamesian Heavy Spear Girl greeting.webp"
image jamesianSparabaraDude = "images/NPCs/Jamesia/Troopers/Ssatrotu Sparabara Dude(Jamesian).webp"
image jamesianSparabaraGirl = "images/NPCs/Jamesia/Troopers/Ssatrotu Sparabara Lady(Jamesian).webp"
image jamesianHeavyArcher = "images/NPCs/Jamesia/Troopers/Jamesian Heavy Archer.webp"
image jamesianHeavyHorseArcher = "images/NPCs/Jamesia/Troopers/Jamesian Heavy Horse Archer.webp"
image jamesianLongsword = "images/NPCs/Jamesia/Troopers/Jamesian Longsword Trooper.webp"
image jamesianTakabara = "images/NPCs/Jamesia/Troopers/Takabara.webp"
image jamesianSlinger = "images/NPCs/Jamesia/Troopers/Jamesossian Slinger.webp"
image jamesianCataphract = "images/NPCs/Jamesia/Troopers/Jamesian Cataphract Dude.webp"
image zamburak = "images/NPCs/Jamesia/Troopers/Camel Zamburak.webp"
image zamburakDismounted = "images/NPCs/Jamesia/Troopers/Zamburak Lady Unmounted.webp"
image zamburakLady = "images/NPCs/Jamesia/Troopers/Zamburak Lady.webp"





############################################################################################################################################

#Astarts
    #Bardaiya's Realm
image astartDude1 = "images/NPCs/Astart Cilivians/astart dude1.webp"
image astartDude1Side = "images/NPCs/Astart Cilivians/astart dude1 Side.webp"
image astartLady1 = "images/NPCs/Astart Cilivians/astart lady1.webp"
        #koitha
image koithaChillaxing = "images/NPCs/Astart Cilivians/Koitha Chillaxing.webp"
layeredimage koitha:
    group poses:
        attribute base default:
            "images/NPCs/Astart Cilivians/Koitha.webp"
        attribute crossArms:
            "images/NPCs/Astart Cilivians/Koitha Crossarms.webp"
    group eyes:
        attribute neutralEyes default:
            "images/NPCs/Astart Cilivians/Koitha Neutral Eyes.webp"
        attribute meanEyes:
            "images/NPCs/Astart Cilivians/Koitha Mean Eyes.webp"
        attribute sadEyes:
            "images/NPCs/Astart Cilivians/Koitha Sad Eyes.webp"

    group mouths:
        attribute neutralHappyMouth default:
            "images/NPCs/Astart Cilivians/Koitha Neutral Happy Mouth.webp"
        attribute happyMouth:
            "images/NPCs/Astart Cilivians/Koitha happy mouth.webp"
        attribute annoyedMouth:
            "images/NPCs/Astart Cilivians/Koitha Annoyed Mouth.webp"
        attribute oMouth:
            "images/NPCs/Astart Cilivians/Koitha OMouth.webp"
        #vimekkus
layeredimage vimekkus:
    group poses:
        attribute base default:
            "images/NPCs/Astart Cilivians/Vimekkus.webp"
        attribute crossarms:
            "images/NPCs/Astart Cilivians/Vimekkus Crossarms.webp"
        attribute point:
            "images/NPCs/Astart Cilivians/Vimekkus Poiting.webp"
    
    group eyes:
        attribute neutralEyes default:
            "images/NPCs/Astart Cilivians/Vimekkus Neutral Eyes.webp"
        attribute meanEyes:
            "images/NPCs/Astart Cilivians/Vimekkus MeanEyes.webp"
        attribute sadEyes:
            "images/NPCs/Astart Cilivians/Vimekkus Sad Eyes.webp"

    group mouths:
        attribute neutralHappyMouth default:
            "images/NPCs/Astart Cilivians/Vimekkus Neutral Happy Mouth.webp"
        attribute happyMouth:
            "images/NPCs/Astart Cilivians/Vimekkus Happy Mouth.webp"
        attribute oMouth:
            "images/NPCs/Astart Cilivians/Vimekkus OMouth.webp"
        attribute angryMouth:
            "images/NPCs/Astart Cilivians/Vimekkus angry mouth.webp"
        attribute annoyedMouth:
            "images/NPCs/Astart Cilivians/Vimekkus Annoyed Mouth.webp"
    
    #Imperial Core
    #Ssyayans

#Zarat
    #camel lady
layeredimage camelLady:
    group poses:
        attribute onFoot default:
            "images/NPCs/Zarat/Troopers/Zaratian Heavy Javelin Girl.webp" # 1000 - 1700
        attribute onFootYeah:
            "images/NPCs/Zarat/Troopers/Zaratian Heavy Javelin Girl Year.webp" # 1200 - 2400
        attribute onCamel:
            "images/NPCs/Zarat/Troopers/Zarat Camel Warrior Girl.webp" # 1600 - 2900
        attribute onCamelGreet:
            "images/NPCs/Zarat/Troopers/Zarat Camel Warrior Girl Greeting.webp" # 1600 - 2900
        attribute onCamelAttack:
            "images/NPCs/Zarat/Troopers/Zarat Camel Warrior Girl Attack.webp" # 1600 - 2900
    group eyes: # 1000 - 1700
        attribute meanEyes if_any["onFoot"]:
            "images/NPCs/Zarat/Troopers/Zaratian Heavy Javelin Girl Mean Eyes.webp"
        attribute meanEyes if_any["onFootYeah"]:
            "images/NPCs/Zarat/Troopers/Zaratian Heavy Javelin Girl Mean Eyes.webp"
            xpos 200 ypos 500
        attribute meanEyes if_any["onCamel","onCamelGreet","onCamelAttack"]:
            "images/NPCs/Zarat/Troopers/Zaratian Heavy Javelin Girl Mean Eyes.webp"
            xpos 259 ypos 31

    group mouths: # 1000 - 1700
        attribute OMouth if_any["onFoot"]:
            "images/NPCs/Zarat/Troopers/Zaratian Heavy Javelin Girl o mouth.webp"
        attribute OMouth if_any["onFootYeah"]:
            "images/NPCs/Zarat/Troopers/Zaratian Heavy Javelin Girl o mouth.webp"
            xpos 200 ypos 500
        attribute OMouth if_any["onCamel","onCamelGreet","onCamelAttack"]:
            "images/NPCs/Zarat/Troopers/Zaratian Heavy Javelin Girl o mouth.webp"
            xpos 259 ypos 31

        attribute happyMouth if_any["onFoot"]:
            "images/NPCs/Zarat/Troopers/Zaratian Heavy Javelin Girl Happy Mouth.webp"
        attribute happyMouth if_any["onFootYeah"]:
            "images/NPCs/Zarat/Troopers/Zaratian Heavy Javelin Girl Happy Mouth.webp"
            xpos 200 ypos 500
        attribute happyMouth if_any["onCamel","onCamelGreet","onCamelAttack"]:
            "images/NPCs/Zarat/Troopers/Zaratian Heavy Javelin Girl Happy Mouth.webp"
            xpos 259 ypos 31
    
    #zara-ssatu camel dude
image zaraSsatuSpear = "images/NPCs/Zarat/Troopers/Zaratian Ssatu Male.webp"
image zaraSsatuSpearYeah = "images/NPCs/Zarat/Troopers/Zaratian Ssatu Male Yeah.webp"
image zaraSsatuCamel = "images/NPCs/Zarat/Troopers/Zaratian Ssatu Camel Lancer.webp"
image zaraSsatuCamelNeutral = Composite( ( 2000,3000 ) , ( 0,0 ), "images/NPCs/Zarat/Troopers/Zaratian Ssatu Camel Lancer.webp" ,
    (0,0) , "images/NPCs/Zarat/Troopers/Zaratian Ssatu Camel Lancer closed mouth.webp" )


    
    #The holey ssatrotu sparabara
layeredimage ssatrotuSparabaraLady:
    group poses:
        attribute armed default:
            "images/NPCs/Zarat/Troopers/Ssatrotu Sparabara Lady.webp"
        attribute yeah:
            "images/NPCs/Zarat/Troopers/Ssatrotu Sparabara Lady Yeah.webp"
    group eyes:
        attribute meanEyes if_not["yeah"]:
            "images/NPCs/Zarat/Troopers/Ssatrotu Sparabara Lady Mean eyes.webp"
    group mouths:
        attribute angryMouth if_not["yeah"]:
            "images/NPCs/Zarat/Troopers/Ssatrotu Sparabara Lady Angry Mouth.webp"
        attribute happyMouth if_not["yeah"]:
            "images/NPCs/Zarat/Troopers/Ssatrotu Sparabara Lady Happy Mouth.webp"
#the dude version
#might have a yeah and guading version
layeredimage ssatrotuSparabaraDude:
    group poses:
        attribute attack default:
            "images/NPCs/Zarat/Troopers/Ssatrotu Sparabara Dude.webp"

#will be riding an armored camel
layeredimage zaratianEliteSpear:
    group poses:
        attribute unmountedAttack default:
            "images/NPCs/Zarat/Troopers/Zaratian Elite Spear.webp"

#will be riding an unarmored horse
layeredimage zaratoJamesianAxeLady:
    group poses:
        attribute unmounted default:
            "images/NPCs/Zarat/Troopers/Zarato Jamesian Axe Girl.webp"


#shata mace lady
image shataMaceLadyZarat = "images/NPCs/Zarat/Troopers/Shata Macelady Zarat.webp" 

    #yimi-oxa archer
image yimiOxaArcher = "images/NPCs/Zarat/Troopers/Yimi-Oxa Archer.webp"
image yimiOxaArcherAttack = "images/NPCs/Zarat/Troopers/Yimi-Oxa Archer Attack.webp"
image yimiOxaYeah = "images/NPCs/Zarat/Troopers/Yimi-Oxa Yeah.webp"
    #slinger
image zaratSlinger = "images/NPCs/Zarat/Troopers/zaratian slinger.webp"
image zaratSlingYeah = "images/NPCs/Zarat/Troopers/zaratian slinger yeah.webp"
image zaratSlingerSlung = "images/NPCs/Zarat/Troopers/zaratian slinger Slinging 3.webp"
image zaratSlingerSlinging:
    "images/NPCs/Zarat/Troopers/zaratian slinger Slinging 1.webp"
    pause 0.25
    "images/NPCs/Zarat/Troopers/zaratian slinger Slinging 2.webp"
    pause 0.25
    repeat
    
    
    #Chuwos
layeredimage chuwos:
    group poses:
        attribute onCamel default: # 1600-2800
            "images/NPCs/Zarat/Troopers/Shatrotu Camel Magus.webp"
        attribute onCamelAttack:
            "images/NPCs/Zarat/Troopers/Shatrotu Camel Magus Cammanding.webp"
        attribute onFoot: # 1000 - 1800
            "images/NPCs/Zarat/Troopers/Shatrotu Magus.webp"
    group eyes:
        attribute neutralEyes if_not["onFoot"] default:
            "images/NPCs/Zarat/Troopers/Shatrotu Camel Magus Neutral Eyes.webp"
        attribute neutralEyes default:
            "images/NPCs/Zarat/Troopers/Shatrotu Camel Magus Neutral Eyes.webp"
            xpos -600 ypos -1000
        attribute angryEyes if_not["onFoot"]:
            "images/NPCs/Zarat/Troopers/Shatrotu Camel Magus Angry Eyes.webp"
        attribute angryEyes:
            "images/NPCs/Zarat/Troopers/Shatrotu Camel Magus Angry Eyes.webp"
            xpos -600 ypos -1000

    group mouths:#all 1600-2800
        attribute neutralHappyMouth if_not["onFoot"] default:
            "images/NPCs/Zarat/Troopers/Shatrotu Camel Magus Neutral Happy Mouth.webp"
        attribute neutralHappyMouth default:
            "images/NPCs/Zarat/Troopers/Shatrotu Camel Magus Neutral Happy Mouth.webp"
            xpos -600 ypos -1000

        attribute annoyedMouth if_not["onFoot"]: 
            "images/NPCs/Zarat/Troopers/Shatrotu Camel Magus annoyed mouth.webp"
        attribute annoyedMouth: 
            "images/NPCs/Zarat/Troopers/Shatrotu Camel Magus annoyed mouth.webp"
            xpos -600 ypos -1000

        attribute angryMouth if_not["onFoot"]:
            "images/NPCs/Zarat/Troopers/Shatrotu Camel Magus angry mouth.webp"
        attribute angryMouth:
            "images/NPCs/Zarat/Troopers/Shatrotu Camel Magus angry mouth.webp"
            xpos -600 ypos -1000

layeredimage chuwos34:
    group poses:
        attribute basic default:
            "images/NPCs/Zarat/Troopers/Shatrotu Magus 3 4.webp"
        attribute pointy:
            "images/NPCs/Zarat/Troopers/Shatrotu Magus 3 4 pointy.webp"
        attribute think:
            "images/NPCs/Zarat/Troopers/Shatrotu Magus 3 4 Thinking.webp"

    group eyes:
        attribute neutralEyes default:
            "images/NPCs/Zarat/Troopers/Shatrotu Magus 3 4 neutral eyes.webp"
        attribute sadEyes:
            "images/NPCs/Zarat/Troopers/Shatrotu Magus 3 4 sad eyes.webp"
        attribute meanEyes:
            "images/NPCs/Zarat/Troopers/Shatrotu Magus 3 4 Mean eyes.webp"

    group mouths:
        attribute neutralHappy default:
            "images/NPCs/Zarat/Troopers/Shatrotu Magus 3 4 neutral happy mouth.webp"
        attribute lineMouth:
            "images/NPCs/Zarat/Troopers/Shatrotu Magus 3 4 line mouth.webp"
        attribute OMouth:
            "images/NPCs/Zarat/Troopers/Shatrotu Magus 3 4 oMouth.webp"
        attribute angryMouth:
            "images/NPCs/Zarat/Troopers/Shatrotu Magus 3 4 angry mouth.webp"
        attribute annoyedMouth:
            "images/NPCs/Zarat/Troopers/Shatrotu Magus 3 4 annoyed mouth.webp"
        attribute happyMouth:
            "images/NPCs/Zarat/Troopers/Shatrotu Magus 3 4 Happy Mouth.webp"
#Zaratian citizens
    #North Zarat
        #The chuck treeple
image zaratianDudeChuck = "images/NPCs/Zarat/North/zaratian dude flung.webp"
image shataGirlChuck = "images/NPCs/Zarat/North/shata girl flung.webp"
image ssatuGirlChuck = "images/NPCs/Zarat/North/ssatu girl flung.webp"
image theChucksSad = "images/NPCs/Zarat/North/Zaratian Ssatu and Shata sad.webp"
image theChucksHappy = "images/NPCs/Zarat/North/Zaratian Ssatu and Shata Happy.webp"

#other gilgamorians
layeredimage gilgamoriumShopDude:
    group poses:
        attribute based default:
            "images/NPCs/Zarat/North/Zarato-Jamesian Dude.webp"
        attribute greet:
            "images/NPCs/Zarat/North/Zarato-Jamesian Dude Greet.webp"
        attribute item:
            "images/NPCs/Zarat/North/Zarato-Jamesian Dude Item.webp"
        attribute smad:
            "images/NPCs/Zarat/North/Zarato-Jamesian Dude smad.webp"
        attribute yeah:
            "images/NPCs/Zarat/North/Zarato-Jamesian Dude Yeah.webp"
    
    group mouths:   
        attribute happyMouth if_not['yeah']:
            "images/NPCs/Zarat/North/Zarato-Jamesian Dude Happy Mouth.webp"
        attribute happyMouth if_any['yeah']:
            "images/NPCs/Zarat/North/Zarato-Jamesian Dude Happy Mouth.webp"
            ypos 200

        attribute OMouth if_not['yeah']: 
            "images/NPCs/Zarat/North/Zarato-Jamesian Dude o Mouth.webp"
        attribute OMouth if_any['yeah']:
            "images/NPCs/Zarat/North/Zarato-Jamesian Dude o Mouth.webp"
            ypos 200

    group eyes:
        attribute sadEyes if_not['yeah']:
            "images/NPCs/Zarat/North/Zarato-Jamesian Dude Sad Eyes and Ears.webp"
        attribute sadEyes if_any['yeah']:
            "images/NPCs/Zarat/North/Zarato-Jamesian Dude Sad Eyes and Ears.webp"
            ypos 200

image gilgamoriumShopDudeArmOver = "images/NPCs/Zarat/North/Zarato-Jamesian Dude Item hand.webp"

image zaratoJamesianSad = "images/NPCs/Zarat/North/Zarato-Jamesian Lady Sad.webp"
image zaratoJamesianYeah = "images/NPCs/Zarat/North/Zarato-Jamesian Lady Yeah.webp"

#yimians
layeredimage yimianLady:
    group poses:
        attribute based default:
            "images/NPCs/Zarat/North/Zaratian Lady.webp"
        attribute running:
            "images/NPCs/Zarat/North/Zaratian Lady Running.webp"
    
    group mouths:
        attribute happyMouth if_any['based']:
            "images/NPCs/Zarat/North/Zaratian Lady Happy mouth.webp"
        attribute happyMouth if_any['running']:
            "images/NPCs/Zarat/North/Zaratian Lady Happy mouth.webp"
            xpos 150

        attribute OMouth if_any['based']:
            "images/NPCs/Zarat/North/Zaratian Lady o mouth.webp"
        attribute OMouth if_any['running']:
            "images/NPCs/Zarat/North/Zaratian Lady o mouth.webp"
            xpos 150

    group eyes:
        attribute meanEyes if_any['based']:
            "images/NPCs/Zarat/North/Zaratian Lady Mean Eyes.webp"
        attribute meanEyes if_any['running']:
            "images/NPCs/Zarat/North/Zaratian Lady Mean Eyes.webp"
            xpos 150

#Tastsetu (Gilgamorium Lake)
#Tastetu Warrior dude
layeredimage tastsetuWarriorDude:
    group poses:
        attribute land default:
            "images/NPCs/Zarat/Tastsetu/Tastsetu Warrior Land.webp"
        attribute water:
            "images/NPCs/Zarat/Tastsetu/Tastsetu Warrior.webp"
    group mouths:
        attribute frown:
            "images/NPCs/Zarat/Tastsetu/Tastsetu Warrior Frown.webp"
        attribute angryMouth:
            "images/NPCs/Zarat/Tastsetu/Tastsetu Warrior Angry Mouth.webp"
#tastsetu dart shoota lady
layeredimage tastsetuDartShootaLady:
    group poses:
        attribute armDown default:
            "images/NPCs/Zarat/Tastsetu/Tastsetu Dart Shooter Point Foward.webp"
        attribute armUp:
            "images/NPCs/Zarat/Tastsetu/Tastsetu Dart Shooter.webp"
#tastsetu dude
image tastsetuDudeBase = "images/NPCs/Zarat/Tastsetu/tastsetu boy worming.webp"
layeredimage tastsetuDudeFront:
    group poses:
        attribute basic default:
            "images/NPCs/Zarat/Tastsetu/tastsetu boy front.webp"
        attribute full:
            "images/NPCs/Zarat/Tastsetu/tastsetu boy worming.webp"
    group eyes:
        attribute meanEyes:
            "images/NPCs/Zarat/Tastsetu/tastsetu boy Mean Eyes.webp"
    group mouths:
        attribute deltaMouth:
            "images/NPCs/Zarat/Tastsetu/tastsetu boy Delta Mouth.webp"


#taststeu lady
image tastsetuladyBase = "images/NPCs/Zarat/Tastsetu/Tastsetu Girl Worming.webp"
layeredimage tastsetuladyFront:
    group poses:
        attribute basic default:
            "images/NPCs/Zarat/Tastsetu/Tastsetu Girl Front.webp"
        attribute full:
            "images/NPCs/Zarat/Tastsetu/Tastsetu Girl Worming.webp"
    group eyes:
        attribute meanEyes:
            "images/NPCs/Zarat/Tastsetu/Tastsetu Girl Mean Eyes.webp"
    group mouths:
        attribute deltaMouth:
            "images/NPCs/Zarat/Tastsetu/Tastsetu Girl Delta Mouth.webp"

#tastetu net girl
image tastsetuNetGirlBase = "images/NPCs/Zarat/Tastsetu/Tastsetu Netter Girl Wata.webp"
layeredimage tastsetuNetGirl:
    group poses:
        attribute basic default: #based on netter girl wata
            "images/NPCs/Zarat/Tastsetu/Tastsetu Netter Girl Front.webp"
        attribute fullWata:
            "images/NPCs/Zarat/Tastsetu/Tastsetu Netter Girl Wata.webp"
        attribute fullWorm:
            "images/NPCs/Zarat/Tastsetu/Tastsetu Netter Girl.webp"

    group eyes:
        attribute neutralEyes default:
            "images/NPCs/Zarat/Tastsetu/Tastsetu Netter Girl Neutral Eyes.webp"
        attribute meanEyes:
            "images/NPCs/Zarat/Tastsetu/Tastsetu Netter Girl Wata Mean Eyes.webp"

    group mouths:
        attribute neutralHappyMouth default:
            "images/NPCs/Zarat/Tastsetu/Tastsetu Netter Girl Neutral Happy Mouth.webp"

        attribute deltaMouth:
            "images/NPCs/Zarat/Tastsetu/Tastsetu Netter Girl Wata Delta Mouth.webp"


#tastsetu eleite trooper
layeredimage tastsetrotuSwordBoy:
    group poses:
        attribute walk default:
            "images/NPCs/Zarat/Tastsetu/Tastsetrotu Elite Trooper Land.webp"
        attribute swim:
            "images/NPCs/Zarat/Tastsetu/Tastsetrotu Elite Trooper Wata.webp"
    #robe ghosts
image robeGhostXerx = "images/Protagonists/Robe Ghosts/Robe Ghost Xerx.webp"
image robeGhostTesi = "images/Protagonists/Robe Ghosts/Robe Ghost Tesi.webp"
image robeGhostVolk = "images/Protagonists/Robe Ghosts/Robe Ghost Volka.webp"
#other faction characters
    #Tarminians
image tarminianHoplite = "images/Neutral Troopers/Tarminian Hoplite Male.webp"