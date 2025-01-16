init python:

    class ArmorSet:

        health100 = Transform( child ="images/Protagonists/Xerxes/Xerxes 3-4 Armored 100-70.webp" , zoom=0.3 )
        health70 = Transform( child ="images/Protagonists/Xerxes/Xerxes 3-4 Armored 069-30.webp" , zoom=0.3 )
        health30 = Transform( child ="images/Protagonists/Xerxes/Xerxes 3-4 Armored 029-01.webp" , zoom=0.3 )
        health0 = Transform( child ="images/Protagonists/Xerxes/Xerxes 3-4 Armored 00.webp" , zoom=0.3 )

        def __init__( self , full , middle , low , dead ):
            self.health100 = full
            self.health70 = middle
            self.health30 = low
            self.health0 = dead
        #------------------------------------------

#---------------------------------------------

# define armor set Objects

# 91 objects by the end of Sword of Ahura-Mazda

# 104 objects by the end of Astarte's Challenge

    # xerxes

define xerxesScaleMail = ArmorSet( Transform( child = "images/Protagonists/Xerxes/Xerxes 3-4 Armored 100-70.webp" , zoom=0.3 ) ,
Transform( child ="images/Protagonists/Xerxes/Xerxes 3-4 Armored 069-30.webp" , zoom=0.3  ) ,
Transform( child ="images/Protagonists/Xerxes/Xerxes 3-4 Armored 029-01.webp" , zoom=0.3  ) ,
Transform( child ="images/Protagonists/Xerxes/Xerxes 3-4 Armored 00.webp" , zoom=0.3  )
)

define xerxesUnarmored = ArmorSet( Transform ( child="images/Protagonists/Xerxes/Xerxes 3-4 unarmored 100-70.webp", zoom=0.3 ) ,
Transform ( child="images/Protagonists/Xerxes/Xerxes 3-4 unarmored 069-30.webp", zoom=0.3 ) ,
Transform ( child="images/Protagonists/Xerxes/Xerxes 3-4 unarmored 029-01.webp", zoom=0.3 ) ,
Transform ( child="images/Protagonists/Xerxes/Xerxes 3-4 unarmored 00.webp", zoom=0.3 )
)

define xerxesArmorSets = [ xerxesUnarmored , xerxesScaleMail , xerxesScaleMail , xerxesScaleMail , xerxesScaleMail , xerxesScaleMail , xerxesScaleMail , xerxesScaleMail]


    #Tesipiz
define tesipizScaleMail = ArmorSet( Transform( child ="images/Protagonists/Tesipiz/Tesipiz Armored 3-4 100-70.webp" , zoom=0.3 ) ,
Transform( child ="images/Protagonists/Tesipiz/Tesipiz Armored 3-4 069-30.webp" , zoom=0.3 ) ,
Transform( child ="images/Protagonists/Tesipiz/Tesipiz Armored 3-4 029-01.webp" , zoom=0.3 ) ,
Transform( child ="images/Protagonists/Tesipiz/Tesipiz Armored 3-4 00.webp" , zoom=0.3 )
)

define tesipizUnarmored = ArmorSet( Transform( child ="images/Protagonists/Tesipiz/Tesipiz 3-4 unarmored 100-70.webp" , zoom=0.3 ) ,
Transform( child ="images/Protagonists/Tesipiz/Tesipiz 3-4 unarmored 069-30.webp" , zoom=0.3 ) ,
Transform( child ="images/Protagonists/Tesipiz/Tesipiz 3-4 unarmored 029-01.webp" , zoom=0.3 ) ,
Transform( child ="images/Protagonists/Tesipiz/Tesipiz 3-4 unarmored 00.webp" , zoom=0.3 ) 
) 

define tesipizArmorSets = [ tesipizUnarmored , tesipizScaleMail , tesipizScaleMail , tesipizScaleMail , tesipizScaleMail , tesipizScaleMail , tesipizScaleMail , tesipizScaleMail]

    #Ato'ssa
define atossaScaleMail = ArmorSet( Transform( child ="images/Protagonists/Atossa/Atossa 3-4 Armored 100-70.webp" , zoom=0.3 , xzoom =-1.0 ) ,
Transform( child ="images/Protagonists/Atossa/Atossa 3-4 Armored 069-30.webp" , zoom=0.3 , xzoom =-1.0 ) ,
Transform( child ="images/Protagonists/Atossa/Atossa 3-4 Armored 029-01.webp" , zoom=0.3 , xzoom =-1.0 ) ,
Transform( child ="images/Protagonists/Atossa/Atossa 3-4 Armored 00.webp" , zoom=0.3 , xzoom =-1.0 )
)

define atossaUnarmored = ArmorSet( Transform( child ="images/Protagonists/Atossa/Atossa 3-4 unarmored 100-70.webp" , zoom=0.3 , xzoom =-1.0 ) ,
Transform( child ="images/Protagonists/Atossa/Atossa 3-4 unarmored 69-30.webp" , zoom=0.3 , xzoom =-1.0 ) ,
Transform( child ="images/Protagonists/Atossa/Atossa 3-4 unarmored 29-01.webp" , zoom=0.3 , xzoom =-1.0 ) ,
Transform( child ="images/Protagonists/Atossa/Atossa 3-4 unarmored 00.webp" , zoom=0.3 , xzoom =-1.0 )
)

define atossaArmorSets = [ atossaUnarmored , atossaScaleMail , atossaScaleMail , atossaScaleMail , atossaScaleMail , atossaScaleMail , atossaScaleMail , atossaScaleMail]

    #Volkara
define volkaraScaleMail = ArmorSet( Transform( child ="images/Protagonists/Volkara/Volkara Neutral Happy 3quat armored 100-70.webp" , zoom=0.3 , xzoom =-1.0 ) ,
Transform( child ="images/Protagonists/Volkara/Volkara Neutral Happy 3quat armored 069-30.webp" , zoom=0.3 , xzoom =-1.0 ) ,
Transform( child ="images/Protagonists/Volkara/Volkara Neutral Happy 3quat armored 029-01.webp" , zoom=0.3 , xzoom =-1.0 ) ,
Transform( child ="images/Protagonists/Volkara/Volkara Neutral Happy 3quat armored 00.webp" , zoom=0.3 , xzoom =-1.0 ) 
)

define volkaraUnarmored = ArmorSet( Transform( child ="images/Protagonists/Volkara/Volkara 3-4 unarmored 100-70.webp" , zoom=0.3 , xzoom =-1.0 ) ,
Transform( child ="images/Protagonists/Volkara/Volkara 3-4 unarmored 69-30.webp" , zoom=0.3 , xzoom =-1.0 ) ,
Transform( child ="images/Protagonists/Volkara/Volkara 3-4 unarmored 29-01.webp" , zoom=0.3 , xzoom =-1.0 ) ,
Transform( child ="images/Protagonists/Volkara/Volkara 3-4 unarmored 00.webp" , zoom=0.3 , xzoom =-1.0 )
)

define volkaraArmorSets = [ volkaraUnarmored , volkaraScaleMail , volkaraScaleMail , volkaraScaleMail , volkaraScaleMail , volkaraScaleMail , volkaraScaleMail , volkaraScaleMail ]
    #Trimdius

    #Xerdza

    #Trimdia

    #Chonzuka

    #Miruki

    #Keiozia

    #Adgilia
