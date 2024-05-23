# This is a test program of a simplistic, text-based adventure game I am working on.
# This game is called Fallout: A Text Adventure


# Welcome statement and user name choice

print("Welcome to Fallout: A Text Adventure")
userName = input("Please enter your character name.")


# Attribute selection explanation

print(" ")
print("Welcome, " + userName + ". You will now choose your starting attributes:")
print(" ")
print("Strength: How strong you are, physically.")
print("Perception: Your awareness of your surroiundings.")
print("Endurance: Your ability to withstand things, physically.")
print("Charisma: Your ability to communicate.")
print("Intelligence: How strong and fast you are, mentally.")
print("Agility: How fast you are, physically.")
print("Luck: How lucky you are.")
print(" ")
print("You have 40 points to distribute how you see fit. Attributes can be from 0 to 10.")
print("At the end, you will have an opportunity to redistribute points if you would like.")
print(" ")
print("NOTE: IF YOU ENTER A NEGATIVE NUMBER OR A NUMBER GREATER THAN 10, IT WILL RESULT IN")
print("AN ERROR AND YOU WILL HAVE TO START THE APPLICATION OVER.")
print(" ")


# Selection of each attribute
def attributeSelection():
    pointsLeft = 40
    userStrength = int(input("How many points would you like to allocate to strength?"))
    assert -1 < userStrength < 11
    pointsLeft = pointsLeft - userStrength
    print("Your remaining points are " + str(pointsLeft))
    userPerception = int(input("How many points would you like to allocate to perception?"))
    assert -1 < userPerception < 11
    pointsLeft = pointsLeft - userPerception
    print("Your remaining points are " + str(pointsLeft))
    userEndurance = int(input("How many points would you like to allocate to endurance?"))
    assert -1 < userEndurance < 11
    pointsLeft = pointsLeft - userEndurance
    print("Your remaining points are " + str(pointsLeft))
    userCharisma = int(input("How many points would you like to allocate to charisma?"))
    assert -1 < userCharisma < 11
    pointsLeft = pointsLeft - userCharisma
    print("Your remaining points are " + str(pointsLeft))
    userIntelligence = int(input("How many points would you like to allocate to intelligence?"))
    assert -1 < userIntelligence < 11
    pointsLeft = pointsLeft - userIntelligence
    print("Your remaining points are " + str(pointsLeft))
    userAgility = int(input("How many points would you like to allocate to agility?"))
    assert -1 < userAgility < 11
    pointsLeft = pointsLeft - userAgility
    print("Your remaining points are " + str(pointsLeft))
    userLuck = int(input("How many points would you like to allocate to luck?"))
    assert -1 < userLuck < 11
    pointsLeft = pointsLeft - userLuck
    print("Your remaining points are " + str(pointsLeft))
    while pointsLeft > 0:
        print("You have " + str(pointsLeft) + " remaining total points.")
        print("Where would you like to allocate these remaining points?")
        allocation = int(input("1-Strength, 2-Perception, 3-Endurance, 4-Charisma, 5-Intelligence, 6-Agility, 7-Luck")
        assert 0 < allocation < 8
        if allocation == 1:
            amount = int(input("How many points would you like to add to Strength?")
            assert amount <= pointsLeft
            userStrength = userStrength + amount
        if allocation == 2:
            amount = int(input("How many points would you like to add to Perception?")
            assert amount <= pointsLeft
            userPerception = userPerception + amount
        if allocation == 3:
            amount = int(input("How many points would you like to add to Endurance?")
            assert amount <= pointsLeft
            userEndurance = userEndurance + amount
        if allocation == 4:
            amount = int(input("How many points would you like to add to Charisma?")
            assert amount <= pointsLeft
            userCharisma = userCharisma + amount
        if allocation == 5:
        
attributeSelection()




    
    