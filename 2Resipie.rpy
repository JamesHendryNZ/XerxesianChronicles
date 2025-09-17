init python:
    
    class Resipie:

        startItems = [[ 0 , 1 ]]
        endItems = [[ 0 , 1 ]]
        resipiName = "Pure Nothingness"
        timeTaken = 0

        def __init__( self , startItems , endItems , resipiName , timeTaken = 1 ):
            self.startItems = startItems
            self.endItems = endItems
            self.resipiName = resipiName
            self.timeTaken = timeTaken

#----------------------------------------------

#item craft resipie-----------------------------------------

define yellowBombResipie = Resipie( [ [ yellowBombMakitKit , 1 ] ] , [ [ yellowBomb , 1 ] ] , "Make Basic Yellow Bombs", 10 )
define tanBomResipie = Resipie( [ [ tanBombMakitKit , 1 ] ] , [ [ tanBomb , 1 ] ] , "Make Strong Tan Bombs", 10 )

define cookedFishes = Resipie( [ [ floodFish , 1 ] ] , [ [ cookedfish , 1 ] ] , "Cook the Fish", 4 )
define spicyDaFish = Resipie( [ [ floodFish , 1 ] , [ redSpice , 1 ] ] , [ [ spicycookedfish , 1 ] ] , "Spice up the Fish", 5 )
define cookedMeat = Resipie( [ [ lizardMeat , 1 ] ] , [ [ cookedMeatItem , 1 ] ] , "Cook the Meat", 5 )
define spicyCookedMeats = Resipie( [ [ redSpice , 1 ] , [ lizardMeat , 1 ]  ] , [ [ spicyMeat , 1 ] ] , "Spice up the Meat", 6 )
define cookedAsMussel = Resipie( [ [ musselz , 1 ] ] , [ [ cookedMussel , 1 ] ] , "Cook the Mussels", 4 )
define flamedCrayfish = Resipie( [ [ crayfish , 1 ] ] , [ [ cookedcrayfish , 1 ] ] , "Cook the Crayfish", 4 )
define flameyAndSpicyCrayFish = Resipie( [ [ crayfish , 1 ] , [ redSpice , 1 ] ] , [ [ spicycrayfish , 1 ] ] , "Spice up the Crayfish", 5 )
define flamedRat = Resipie( [ [ deadRat , 1 ] ] , [ [ cookedRat , 1 ] ] , "Roast the Rat", 4 )
define acidOfSulfur = Resipie( [ [ ironSulfate , 1 ] ] , [ [ potOAcid , 1 ] ] , "Make some ACID!", 15 )
define saltDaMeat = Resipie( [ [ lizardMeat , 1 ] , [ salt , 1 ] ] , [ [ saltyMeat , 1 ] ] , "Salt the Meat", 2 )
define saltedRodents = Resipie( [ [ deadRat , 1 ] , [ salt , 1 ] ] , [ [ saltyMeat , 1 ] ] , "Salt the Dead Rat", 2 )

define friedLadyEgg = Resipie([ [ ladyEgg , 1 ] ] , [ [ friedEgg , 1 ] ],"Fry the Egg", 3 )
#define friedEgg
define omletCook = Resipie([ [ ladyEgg , 1 ] , [ foodLeevz , 1 ] ] , [ [ omlet ,1 ] ],"Smash the Egg Up", 5 )
#define omletOst
define omletSeedy = Resipie([ [ ladyEgg , 1 ],[ foodSeedz , 1 ] ] , [ [ omlet ,1 ] ],"Smash and Seed the Egg", 5 )
#define omletSeedOst
define baityFishCakes = Resipie([ [ baitFish , 3 ] , [ redSpice , 1] ] , [ [ gilgaFishCake , 1 ] ] , "Compressed Baitfish", 10 )
define floodFishCakes = Resipie([ [ floodFish , 1 ] , [ redSpice , 1 ] ] , [ [ gilgaFishCake , 1 ] ] , "Floodfish Cake", 10 )
define crayfishCakes = Resipie([ [ crayfish , 2 ],[ redSpice , 1 ]], [ [ gilgaFishCake , 1 ] ] , "Crayfishes get Caked", 10 )
define isopodCakes = Resipie([ [ isopod , 3 ],[ redSpice , 1 ]], [ [ gilgaFishCake , 1 ] ] , "Isopods get Caked", 10 )
#define meatAndEggCake = Resipie([ [ lizardMeat , 2 ] , [ ladyEgg , 1 ] ,[ foodLeevz , 1 ],[ salt , 1 ]],[ [ eggMeatCake , 1 ] ] , "All in one Food",1)
#ostEgg
define saltyMeatAndEggCake = Resipie([ [ saltyMeat , 1 ],[ ladyEgg , 1 ] ,[ foodLeevz , 1 ] ],[ [ eggMeatCake , 1 ] ] , "All in One Food" , 10 )
#ostEgg
define ratMeatAndEggCake = Resipie([ [ saltyMeat , 1 ],[ ladyEgg , 1 ] ,[ foodSeedz , 1 ] ],[ [ eggMeatCake , 1 ] ] , "All in One Food" , 10 )
#ostEgg

#item craft List--------------------------------------
define itemCraftResipies = [ yellowBombResipie , cookedFishes , spicyDaFish , cookedMeat , spicyCookedMeats , cookedAsMussel , flamedCrayfish , flameyAndSpicyCrayFish , flamedRat , acidOfSulfur , saltDaMeat , saltedRodents , friedLadyEgg , omletCook , omletSeedy , baityFishCakes , floodFishCakes , crayfishCakes , isopodCakes , saltyMeatAndEggCake , ratMeatAndEggCake , tanBomResipie ]

