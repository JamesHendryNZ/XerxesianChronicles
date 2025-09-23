init python:

    #do AFTER the 0.1.14 stroy bits are done and tested so that debugging is easier. 
    #implement in all instances it's placed 
    #inventroySystem
    #ShopSystem
    #BattleSystem
    #EctabanaAssult1
    class ItemSlot:

        item = None
        amountOf = 0 #Will replace amountOf in Items after successful intergration.

        def __init__( self , item , amountOf ):
            self.item = item
            self.amountOf = amountOf

    class Item:

        name = "jar of dirt"
        image = "images/items/bottleJarODirt.webp"
        itemType = "quest"
        effectPower = 0 # this is both for healing and damaging # also for differnt ammo types.
        effectArmorPower = 0 # this is for throwable weapons and ammo.
        # amountOf  0  This is how multiple ofs will be handled / Will be moved to ItemSlot at the end of 0.1.14
        effectDuration = 0
        effectType = "none"

        description = "I've got a jar of Dirt! I've got a jar of Dirt! And guess what's inside it."
        cost = 9001

        def __init__( self , name , image , itemType , effectPower , effectDuration , effectType , effectArmorPower , description , cost ):
            self.name = name
            self.image = image
            self.itemType = itemType
            self.effectPower = effectPower
            self.effectDuration = effectDuration
            self.effectType = effectType
            self.effectArmorPower = effectArmorPower
            self.description = description
            self.cost = cost
        
        #----------------------------------------------------------------------------------------------------

        def __copy__( original ):
            return Item( original.name , original.image , original.itemType , original.effectPower , original.effectDuration , original.effectType , original.effectArmorPower , original.description , original.cost )


        



#----------------------------------------------
#items-----------------------------------------------------
define arrow = Item( "Arrow" , "images/items/arrow.webp" , "ammo" , 4 , 0 , "Shoot" , 0 , "Simple yet dependible ammo for the common bow." , 4 ) #common arrow for common foes
define metalArrow = Item( "Metal Arrow" , "images/items/arrowBoltShort.webp" , "ammo" , 8 , 0 , "Shoot" , 20 , "A heavy metal arrow for punching through armor." , 12 ) #for armored foes mid game
define powerArrow = Item( "Power Arrow" , "images/items/arrowPower.webp" , "ammo" , 24 , 0 , "Shoot" , 28 , "An enchanted arrow that is a powerful as a bomb." , 36 )  #for elites late game and super elite end game
define jarOfDirt = Item( "Jar of Dirt" , "images/items/bottleJarODirt.webp" , "quest" , 0 , 0 , "TextPromt" , 0 , "I've got a jar of Dirt! I've got a jar of Dirt! And guess what's inside it." , 9001 )
define yellowBomb = Item( "Bomb" , "images/items/bombYellow.webp" , "bomb" , 50 , 0 , "Explosion" , 0 , "The most common type of bomb used by the Grenadiers of Ahura-Mazda." , 40 )
define tanBomb = Item( "Strong Bomb" , "images/items/bombTan.webp" , "bomb" , 100 , 0 , "Explosion" , 0 , "The stronger bomb that higher ranking memebers the Grenadiers of Ahura-Mazda use." , 80 )
define javelinBasic = Item( "Javelin" , "images/items/javelinBasic.webp" , "javelin" , 12 , 0 , "Yeet" , 4 , "A stick with a metal spike. Easily used by anyone with a good throwing arm." , 4 )
define plumbataDart= Item( "Plumbata" , "images/items/plumbata.webp" , "javelin" , 15 , 0 , "Yeet" , 7 , "A heavy lead-weighted war dart used by the Zardonians. Suprizingly punchy" , 15 )
define javelinBronze = Item( "Bronze Spear" , "images/items/javelinBronze.webp" , "javelin" , 21 , 0 , "Yeet" , 12 , "A soild bronze spear off an old battle statue. Packs quite a punch when thrown" , 20 )
define javelinIron = Item( "Iron Spike" , "images/items/javelinIron.webp" , "javelin" , 18 , 0 , "Yeet" , 6 , "A short iron spike used in spring cannons. Can be used as a javelin as well." , 12 )
define redPotion = Item("Healing Potion (Red)" , "images/items/bottlePotionRed.webp" , "potion" , 60 , 0 , "Heals" , 0 , "Magic potion that replenisihes some lifeforce to keep auto-heal going." , 25)
define bluePotion = Item("Healing Potion (Blue)" , "images/items/bottlePotionBlue.webp" , "potion" , 80 , 4 , "Heals" , 0 , "Magic potion that replenisihes a lot of lifeforce to keep auto-heal going. Heals 80 for 4 turns" , 35)
define yellowBombMakitKit = Item( "Yellow Bomb Kit" , "images/items/bombKitYellow.webp" , "preKit" , 0 , 0 , "preBomb" , 0 , "Random Chemicals needed to make yellow bombs. Needs Tesipiz and time to convert it to bombs." , 25 )
define tanBombMakitKit = Item( "Strong Bomb Kit" , "images/items/bombKitTan.webp" , "preKit" , 0 , 0 , "preBomb" , 0 , "Random Chemicals needed to make the strong tan bombs. Needs Tesipiz and time to convert it to bombs." , 50 )
define zwotiKey = Item( "Zwoti Sword Key" , "images/items/keysZwotiSoAM.webp" , "quest" , 6 , 0 , "questKey" , 3 , "A key needed to access the Sword of Ahura-Mazda. Found in the Zwoti Shrine." , 4 )
define kwortixKey = Item( "Kworitx Sword Key" , "images/items/keyKworitxSoAM.webp" , "quest" , 6 , 0 , "questKey" , 3 , "A key needed to access the Sword of Ahura-Mazda. Found in the Abandoned Mines." , 4 )
define kwortixGenericKey = Item("Kwortix Access Key" , "images/items/keysKwortixGeneric.webp" , "quest" , 6 , 0 , "OpenDoorKwortix" , 3 , "A key used to open doors in the Kwortix Mine." , 4) 
define TakuriumKey = Item( "Takurium Sword Key" , "images/items/keyTakuriumSoAM.webp" , "quest" , 6 , 0 , "questKey" , 3 , "A key needed to access the Sword of Ahura-Mazda. Found in the ruins of Takurium." , 4 )
define cheesyCheese = Item( "Cheese" , "images/items/cheese.webp" , "potion" , 25 , 4 , "Heals" , 0 , "A cheesy food made out of cheesy cheese, Heals 25 hitpoints for 4 turns." , 5 )
define smellyCheese = Item( "Smelly Cheese" , "images/items/smeally cheese.webp" , "reviver" , 25 , 4 , "Revives" , 0 , "A cheesy food so skinky it can revive people and heal them 25 hitpoints for 4 turns." , 70  )
define baitFish = Item( "Bait Fish" , "images/items/bait fish.webp" , "potion" , 10 , 3 , "Heals" , 0 , "A smiple fish used to catch bigger fish. Can be eaten. Heals 10 for 3 turns." , 4 )
define floodFish = Item( "Jamesosian Flood Fish" , "images/items/jamesosian flood fish.webp" , "potion" , 20 , 5 , "Heals" , 0 , "A fish that lives in oasis, lakes and ponds. Very yummy." , 12 )
define crayfish = Item( "Cave crayfish" , "images/items/cave crayfish.webp", "potion" , 9 , 3 , "Heals" , 0 , "Crunchable Crayfish, best served cooked. Very crunchy. Heals 9 for 3 turns." , 5 )
define cookedcrayfish = Item( "Cooked Crayfish" , "images/items/cave crayfish cooked.webp" ,"potion" , 20 , 3 , "Heals" , 0 , "Cooked crayfish is better than raw. Heals 20 per turn for 3 turns." , 20 )
define spicycrayfish = Item( "Spicy Crayfish" , "images/items/cave crayfish cooked spicy.webp" ,"potion" , 30 , 2 , "BoostedAttack" , 0 , "Spicy crayfish is very tasty. Heals 30 and gives you a breif boost in attack." , 20 )
define cookedfish = Item( "Cooked Fish" , "images/items/jamesosian flood fish cooked.webp" , "potion" , 40 , 4 , "Heals" , 0 , "Yummy yummy cooked fried fish. Heals 40 per turn for 2 turns.", 20) 
define redSpice = Item("Red Spice" , "images/items/red spice.webp" , "chemical" , 0 , 0 , "chemical" , 0 , "Can make food spicy" , 10 )
define spicycookedfish = Item( "Spicy Fish" , "images/items/jamesosian flood fish cooked Spicy.webp" , "BoostedAttack" , 30 , 2 , "Heals" , 0 , "Yummy yummy spciy fried fish. Heals 50 and gives you a breif boost in attack.", 20 )
define cookedMeatItem = Item("Cooked Meat" , "images/items/Cooked Meat.webp" , "potion" , 25 , 3 , "Heals" , 0 , "Fried Monsters and other animals, much better than raw. Heals 25 per turn from 3 turns." , 5 )
define spicyMeat = Item( "Spicy meat" , "images/items/Cooked Meat Spicy.webp" , "potion" , 30 , 3 , "BoostedAttack" , 0 , "Spicy adds to the flavour of monster and animal bits. Heals 30 and makes gives you a boost in attack.", 15 )
#define reviver = Item( "Reviver Fang" , "Images/Items/reviver fang.webp", "reviver" , 420 , 1 , "reviver" , 0 , "Delivers health potion to someone who can't drink. Revives a fallen hero.", 100)
define salt = Item( "Salt" , "Images/Items/Salt.webp", "chemical" , 0, 0 , "chemical" , 0 , "Used for food falvor and presurvation" , 3)
define isopod = Item( "Domestic Isopod" , "images/items/domestic isopod.webp" , "potion" , 10 , 3 , "Heals" , 0 , "A tasty chunchy snack and a cheep sorce of food. Heals 10 for 3 turns." , 4 )
define lizardMeat = Item( "Meat" , "images/items/meat.webp" , "potion" , 10 , 3 , "Heals" , 0 , "Giblets of the remains of Dead monsters, best to cook and salt it before eating. Heals 10 for 3." , 4 )
define saltyMeat = Item( "Salted Meat" , "images/items/salty meat.webp" , "potion" , 30 , 4 , "Heals" , 0 , "Salted meat is tasty and lasts longer. It heals 30 hitpoints for 4 turns." , 20)
define reviverFang = Item( "Reviver Fang" , "images/items/reviver fang.webp" , "reviver" , 420 , 0 , "Revives" , 0 , "A quick large snake fang that gives life insted of taking it away." , 50 )  
 


define ladyEgg = Item( "Huge Egg" , "images/items/egg.webp" , "chemical" , 0 , 0 , "chemical" , 0 , "A huge egg layed by a large animal or a jamesianoid lady. They make big ommets." , 15)
#define ostrichEgg = Item Item( "Jamesianoid Egg" , "images/items/egg.webp" , "chemical" , 0 , 0 , "chemical" , 0 , "An ostrich egg. Layed every 45 days. They make big ommets." , 20)

define friedEgg = Item( "Fried Egg" , "images/items/fried egg.webp" , "potion" , 30 , 2 , "Heals" , 0 , "A fried egg, yummy. Heals 30 for 2 turns." , 20 )
define eggMeatCake = Item( "Egg and Meat Cake" , "images/items/eggMeat Cake.webp" , "potion" , 20 , 5 , "HardSkinned" , 0 , "A mixture of meat, egg and leaves. Heals 20 and makes you tougher." , 40 )
define omlet = Item( "Omlette" , "images/items/omlet.webp" , "potion" , 15 , 5 , "Heals" , 0 , "Smashed fried eggs mixed with leaves. Heals 15 for 5 turns." , 20 )
define gilgaFishCake = Item( "Fish Cake" , "images/items/fish cake gilgamorian.webp" , "potion" , 32 , 5 , "BoostedAttack" , 0 , "A spicy fish cake eaten by Gilgamorian Lake people. Heals 36 turns and makes you fight harder." , 40 )

define breadz = Item( "Bread" , "images/items/Bread.webp" , "potion" , 15 , 4 , "Heals" , 0 , "A common foodstuff made of wet ginded grains and farting fungus baked in an oven. Heals 15 for 4 turns." , 15 )
define musselz = Item( "Mussel" , "images/items/mussel.webp" , "potion" , 7 , 4 , "Heals" , 0 , "Fresh mussels found in water everywhere in the Greater Jamesos Realm. Best to cook it first. Heals 7 for 4 turns." , 3 )
define cookedMussel = Item( "Cooked Mussel" , "images/items/cooked mussel.webp" , "potion" , 25 , 3 , "Heals" , 0 , "Delicious cooked mussels. Nice food. Heals 25 for 3 turns." , 13 )
define foodBettles = Item( "Food Beetles" , "images/items/domestic food beetle.webp" , "potion" , 9 , 4 , "Heals" , 0 , "Food for lizards , newts and frogs but poor and hungry jamesianoids will eat them. Heals 9 for 4 turns." , 3 )
define foodWorms = Item( "Food Worms" , "images/items/Food Worms.webp" , "potion" , 17 , 2 , "Heals" , 0 , "The younger fattier food beatles, tasty when fried in oil or butter. Eaten by poor and hungry jamesianoids as well as lizards , newts and frogs. Heals for 17 for 2 turns" , 3 )
define deadRat = Item( "Dead Rat" , "images/items/dead rat.webp" , "potion" , 9 , 4 , "Heals" , 0 , "A rat that is dead, best to cook and salt it before eating. Heals 9 for 4 turns" , 3 )
define cookedRat = Item( "Roasted Rat" , "images/items/cooked Rat.webp" , "potion" , 35 , 3 , "Heals" , 0 , "Tasty fried rat. Heals 35 for 3 turns." , 18 )
define foodLeevz = Item( "Edible Leaves" , "images/items/food Leaves.webp" , "potion" , 7 , 8 , "Heals" , 0 , "Leaves that can be eaten. Takes awhile to munch and digest. Heals 7 for 8 turns." , 6 )
define foodSeedz = Item( "Seedy Plants" , "images/items/food Seedy Leaves.webp" , "potion" , 9 , 8 , "Heals" , 0 , "Nutritious seeds on a edible plant. Takes awhile to get the nutriants out. Heals 9 for 8 turns" , 8 )
define harraFood = Item( "Harra Fruit" , "images/items/Harra Fruit.webp" , "potion" , 10 , 6 , "Heals" , 0 , "A sour fruit native to Harrata, Kawuzhuka and Jamesia. Heals 10 for 6 turns." , 14 )
define fruits = Item( "Dried Fruits" , "images/items/fruits.webp" , "potion" , 10 , 3 , "Heals" , 0 , "Sun dried fruits, a nice side to any dish. A decent snack as well. Heals 10 for 3 turns." , 4 )
define ribbz = Item( "Meat Ribbs" , "images/items/Meat Ribs.webp" , "potion" , 45 , 4 , "Heals" , 0 , "MEAT RIBS!!! Delicious juicy meat with a crunchable bone inside. Heals 45 for 3 turns" , 40 )

define throwableRock = Item("Rock" , "images/items/purple rock.webp" , "javelin" , 6 , 0 , "Yeet" , 10 , "Sometimes a rock is all you need." , 1 )

define monsterBomB = Item( "Monster Bomb" , "images/items/Dead Jakalbite Bomb.webp" , "bomb" , 60 , 0 , "Explosion" , 10 , "Sometimes you need to hide suprizes in your enemies food." , 60 )

define potOAcid = Item( "Acid Pot" , "images/items/Acid Pot.webp" , "bomb" , 15 , 5 , "Burning" ,  0 , "A pot a of strong corrosive subtance. It Burns without a flame and can be used to make things." , 40 )
define throwNet = Item( "Net" , "images/items/net.webp" , "grappleNet" , 10 , 2 , "Entangled" , 5 , "A fishing net. It's quite heavy. If thrown, it can stop foes for 2 turns." , 20)

define clearingJuice = Item( "Clearing Potion" ,  "images/items/Clearing Potion.webp" , "potion", 20 , 3 , "Clears", 0 , "A juice made of blood and milk that cures jamesianoids of all bad effects and heals 20 hitpoints. I also clears negative effects for 3 turns" , 30 )
#maybe a tier 2 version that lasts for 5 turns?

define dollCondition1 = Item( "Old Doll" , "images/items/Doll Partly Restored.webp" , "quest" , 0 , 0 , "dollSubQuest" , 0 , "An old doll found under Takurium Ruins." , 0 )
define tesiDoll = Item( "Tespiz' Doll" , "images/items/Doll 2.webp" , "quest" , 0 , 0 , "TextPromt" , 0 , "One of the dolls in Tesipiz' collection." , 0 )
define korkinDoll = Item( "Tespiz' Doll" , "images/items/Doll 3.webp" , "quest" , 0 , 0 , "TextPromt" , 0 , "A doll of a Zarasikian Korkin given to Tesipiz by Tsekrei." , 0 )

define ironSulfate = Item( "Iron Sulfur" , "images/items/iron 2 sulfate.webp" , "chemical" , 0 , 0 , "chemical" , 0 , "Can be turned into acid" , 30)
define grapplePointShooter = Item("Grapple Shooter" , "images/items/Grapple Point Shooter.webp" , "grapple" , 20 , 1 , "ground" , 10 , "A device that takes flyiers and swimmers out of their confort zone.", 1200 )
define harpoonLauncher = Item("Harpoon Laucher" , "images/items/Harpoon Launcher.webp" , "grapple" , 20 , 1 , "ground" , 10 , "A device used by the Zardonians to deal with flyiers and swimmers.", 1000 )

#lore documents
define tabletDocument = Item("Anti-Stealth Tablet Document" , "images/items/tabletDocument.webp" , "quest" , 0 , 0 , "Lore" , 0 , "A document showing information of the Anti-Stealth Tablet. The Anti-Stealth Tablet is of ahrite construction, it was created around the time of the 2nd Subversion in 552. It seems to show the general area that the Bardaiya-Shahneh is. The emblem in the middle is a press activator. The Astarts had obtained it with out knowing what it does. They had lost it in an ambush raid where it shattered. The Knights of Ahura-Mazda found out when they found documentation in the ahrite ruins in Azerinyih in 554." , 2000 )
define bookGift = Item("The Kinzrama From Heian" , "images/items/tsekrei gift.webp" , "quest" , 0 , 0 , "Lore" , 0 , "A story about a Kinzrama called Nu-eh who came from a place called Heian that is beyond the Sky Above the Sky. She arrived and helped the Karutu led by Herakiliz defeat the Katanian Empire by placing misfortune on the Katanians in 404. Herakiliz was able to get within the Katanian Captial of Kagotasha and force the Emperor to sue for peace. She was made a Kashgyim protector diety and name also became Nweh Kota-Heyan and took on a more Karutu-esque appearance." , 1209)

#idols
define idolOfFazanit = Item( "Idol of Fazanit" , "images/items/Fazanit Idol.webp" , "quest" , 0 , 0 , "loot" , 0 , "An Idol of the Zaratian god of rain, clouds , water , snow , ice and steam. Given to Xerxes by Tsekrei to help him with the magic water system." , 500)
define idolOfSutsshak = Item( "Idol of Sutsshak" , "images/items/Sutsshak Item.webp"  , "loot" , 0 , 0 , "loot" , 0 , "An Idol of the goddess Sutsshak. Looted form the Temple from Takurium." , 1200 )

#other story based loot
define magicannonLoot = Item( "Magicannon" , "images/items/magicannon.webp" , "quest" , 0 , 0 , "loot" , 0 , "A powerful cannon that shoots out magical lasers. Currently out of magic." , 5000) #could turn into a powerful weapon with limited shots used by Volkara later
define versanizLoot = Item( "Versaniz' Helmet" , "images/items/Versaniz Helmet.webp" , "quest" , 0 , 0 , "loot" , 0 , "Versaniz's helmet. He won't be needing it anymore." , 500)
# def __init__( self , name , image , itemType , effectPower , effectDuration , effectType , effectArmorPower , description , cost ):

define deadFalcobite = Item( "Dead Falcobite" , "images/items/Dead Lizardbite.webp" , "Dead Animal" , 0 , 0 , "Dead Animal" , 0 , "A dead falcobite corspe that can be used for many things." , 10)
define astartin = Item( "Astartin" , "images/items/Astartin.webp" , "Foreign Currency" , 0 , 0 , "Foreign Currency" , 0 , "The currency of the Astart Empire. Needs to be converted before use." , 2)
define deadVelosoM = Item("Dead Dude Velociraptor", "images/items/Dead VelosoraptorM.webp" , "quest" , 0 , 0 , "Dead Animal" , 0 , "A dead dino" , 20)
define deadVelosoF = Item("Dead Lady velociraptor", "images/items/Dead VelosoraptorF.webp" , "quest" , 0 , 0 , "Dead Animal" , 0 , "A dead dino" , 20)
#define velosoMFeather
define velosoFeather = Item("Velociraptor Feather", "images/items/feathers VelosoM.webp" , "quest" , 0 , 0 , "Dead Animal" , 0 , "A dead dino" , 20)
define Falcofeather = Item("Falcobite Feather", "images/items/feathers falcobite.webp" , "quest" , 0 , 0 , "Dead Animal" , 0 , "A dead dino" , 20)

#tablet pieces:
define tabletPieceGil = Item("Anti-Stealth Tablet Piece Bottom Left", "images/items/Stone Tablet Zarat.webp" , "quest" , 0 , 0 , "Anti-Stealth Tablet Piece" , 0 , "A piece of the Anti-Stealth tablet that will reveal Lord Bardaiya's position." , 2000 )
define tabletPieceZar = Item("Anti-Stealth Tablet Piece Top Left", "images/items/Stone Tablet Zardon.webp" , "quest" , 0 , 0 , "Anti-Stealth Tablet Piece" , 0 , "A piece of the Anti-Stealth tablet that will reveal Lord Bardaiya's position." , 20000 )
define tabletPieceBal = Item("Anti-Stealth Tablet Piece Top Right", "images/items/Stone Tablet Bala.webp" , "quest" , 0 , 0 , "Anti-Stealth Tablet Piece" , 0 , "A piece of the Anti-Stealth tablet that will reveal Lord Bardaiya's position." , 20000 )
define tabletPieceMak = Item("Anti-Stealth Tablet Piece Bottom Right", "images/items/Stone Tablet Makka.webp" , "quest" , 0 , 0 , "Anti-Stealth Tablet Piece" , 0 , "A piece of the Anti-Stealth tablet that will reveal Lord Bardaiya's position." , 20000 )