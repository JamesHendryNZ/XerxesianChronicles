
init python:


#map update for te squddies to squad

    def updateMap( squads , levels , playerLocation , playerLevel ):

        squads = [ squad for squad in squads if len(squad.squadTroopers) > 0 ]
        for squad in squads:
            squad.checkLine( levels[playerLevel] , playerLocation )
            if squad.targetLocation != squad.location and squad.location != playerLocation and squadMapCheck( squad , levels , squad.level , squad.facing ) and squad.location != playerLocation:
                squad.chasePlayer( levels[playerLevel] )
        
        return squads
    
    def check4Encounter( squads , levels , playerLocation , playerLevel ):
        squadsInCombat = [ squad for squad in squads if squad.location == playerLocation and squad.level == playerLevel ]
        for squad in squadsInCombat:
            if len(squads) > 0:
                return squad
        return False
    
    def check4LevelRetreat( squads , levels , playerLocation , playerLevel ): #for enabling and disabling the retreat option
        squadsInCombat = [ squad for squad in squads if squad.location == playerLocation and squad.level == playerLevel ]
        if levelSpaceAvailable( squadsInCombat , levels , playerLevel , "u") or levelSpaceAvailable( squadsInCombat , levels , playerLevel , "d" ) or levelSpaceAvailable( squadsInCombat , levels , playerLevel , "l" ) or levelSpaceAvailable( squadsInCombat , levels , playerLevel , "r" ):
            return True
        return False

    #checks if it is possible for a squad to keep Moving on a 
    def squadMapCheck( squad , levels , level , targetDirection ):
        #check 4 map contrainsts
        if targetDirection == "u":
            nextLocation = [ squad.location[0]-1 , squad.location[1] ]
        elif targetDirection == "d":
            nextLocation = [ squad.location[0]+1 , squad.location[1] ]
        elif targetDirection == "l":
            nextLocation = [ squad.location[0] , squad.location[1]-1 ]
        else:
            nextLocation = [ squad.location[0] , squad.location[1]+1 ]
        
        #check level constraints
        if nextLocation[0] >= 0 and nextLocation[0] < len( levels[level] ) and nextLocation[1] >= 0 and nextLocation[1] < len( levels[level][squad.location[0]] ):
            if levels[level][nextLocation[0]][nextLocation[1]]:
                return True
            else:
                return False
        else:
            return False

    #checks to see if it is possible for player to flee in a direction
    def levelSpaceAvailable( squads , levels , level , targetDirection ):
        #check 4 map contrainsts
        if targetDirection == "u":
            nextLocation = [ playerLocation[0]-1 , playerLocation[1] ]
        elif targetDirection == "d":
            nextLocation = [ playerLocation[0]+1 , playerLocation[1] ]
        elif targetDirection == "l":
            nextLocation = [ playerLocation[0] , playerLocation[1]-1 ]
        else:
            nextLocation = [ playerLocation[0] , playerLocation[1]+1 ]
        
        #check level constraints
        if nextLocation[0] >= 0 or nextLocation[1] >= 0 and nextLocation[0] < len( levels[level] ) or nextLocation[1] < len( levels[level][playerLocation[0]] ):
            #check if theirs a sqaud occupiing that block
            for squad in squads:
                if squad.location == nextLocation or levels[level][nextLocation[0]][nextLocation[1]] == 0:
                    return False
            return True
        else:
            return False


#squads are parties of foes that patrol an area or hunt the player
#this will be used in
#gilgamorium
#miidos palace
#bala-axerium palace
#riuka complex
    class Squad:

        isActive = False
        location = [0,0]
        targetLocation = [0,0]
        facing= "u" #faces up down left right (should only need the first letter so u d l r)
        turning2 = "u"#the direction to turn if the player moves out of their line of sight when targeted.
        squadTroopers = [] #
        level = 0

        def __init__( self , setGoons , goons2Add , squadSize , location , facing , level=0 ):
            self.location = location
            self.targetLocation = location
            self.facing = facing
            self.turning2 = facing
            self.level = level
            if setGoons:
                self.squadTroopers = goons2Add
            else:
                counter = 0 
                while counter < squadSize:
                    self.squadTroopers.append( copy.copy( goons2Add[ random.randint(0, len(goons2Add) - 1 ) ] ) )
                    counter += 1


        def checkLine( self , map , playerLocation ): #checks in a line for presence of player 
            counter = 0
            if self.facing == "u" or self.facing == "d":
                if playerLocation[1] == self.location[1]:#pays if the player is even on the line
                    counter = self.location[0]

                    if self.facing == "u":
                        while counter > 0:
                            if self.checkLocation( map , counter , self.location[1] ):
                                self.isPlayerThere( [ counter , self.location[1] ] , playerLocation )

                            else:
                                counter = 0 
                            counter -= 1

                    else:
                        while counter < len(map):
                            if self.checkLocation( map , counter , self.location[1] ):
                                self.isPlayerThere( [ counter , self.location[1] ] , playerLocation )
                            else:
                                counter = len(map)
                            counter += 1
            else:
                if playerLocation[0] == self.location[0]:#pays if the player is even on the line
                    counter = self.location[1]

                    if self.facing == "l":
                        while counter > 0:
                            if self.checkLocation( map , self.location[0] , counter ):
                                self.isPlayerThere( [ self.location[0] , counter ] , playerLocation )
                            else:
                                counter = 0 
                            counter -= 1
                    else:
                        while counter < len(map[self.location[0]]):
                            if self.checkLocation( map , self.location[0] , counter ):
                                self.isPlayerThere( [ self.location[0] , counter ] , playerLocation )
                            else:
                                counter = len(map[self.location[0]])
                            counter += 1

        def chasePlayer ( self , map ): #moves 1 step per call towards player
            if self.facing == "u":
                self.location[0] -= 1
            elif self.facing== "d":
                self.location[0] += 1
            elif self.facing == "r":
                self.location[1] += 1
            elif self.facing == "l":
                self.location[1] -= 1

        def isPlayerThere( self,  checkLocation , playerLocation ):
            if checkLocation == playerLocation:
                self.targetLocation = self.checkLocation
            elif self.facing== self.turning2:
                if checkLocation[ 0 ] > playerLocation [ 0 ]:
                    self.turning2 = "d"
                elif checkLocation[ 0 ] < playerLocation [ 0 ]:
                    self.turning2 = "u"
                elif checkLocation[ 1 ] > playerLocation [ 1 ]:
                    self.turning2 = "r"
                elif checkLocation[ 1 ] < playerLocation [ 1 ]:
                    self.turning2 = "l"
            elif self.location == self.targetLocation and self.facing != self.turning2:
                self.facing = self.turning2

            
        

        def checkLocation ( self , map , x , y ): #check if the location exists or is obscured
            if map[x][y]:
                return True
            else:
                return False #can't see through solid walls
    #patrolsquad and hunterSquad will be sub classes of squad