ver = "Beta 1.5 - currently in development" 
import random
import time
import pyinputplus as pyip
import os
from flask import Flask, send_from_directory
import webbrowser
import threading
import logging

def enterPotatoSetup():
  """INTRO SEQUENCE"""
  global battleSet
  playAudio("PeggleSynth")
  print("Welcome to ENTER POTATO,\n")
  time.sleep(0.5)
  print("A game with bad gameplay and even worse writing\n")
  time.sleep(0.5)
  print("Expect some possible bugs and glitches\n")
  time.sleep(0.5)
  print("This game is dedicated to all potatoes in existence\n")
  time.sleep(3)
  print("\nYou will soon become THE POTATO, do you accept your fate?\n")
  time.sleep(1)
  fate_accepted = pyip.inputYesNo('Type a yes or no answer and hit enter to accept your fate\n:')
  if fate_accepted == "no":
    stopAudio()
    endcredits()
  time.sleep(1)
  print("You feel that you will soon suffer\n")
  time.sleep(1)
  print("Firstly, you must answer a few questions\n")
  crimesAmountGoal = pyip.inputInt("How many crimes would you like to commit?\n", min=1, max=5000)
  if crimesAmountGoal <= 49:
    print("You really don't like crimes\nSad :(")
  elif crimesAmountGoal >= 50:
    print("Wow, you really like crimes\nGood :)")
  time.sleep(1)
  difficultyAns = pyip.inputMenu(["Regular", "Betterer"], "What type of potato do you think you are?\n")
  if difficultyAns == "Regular":
    battleSet = 'abcdefghijklmnopqrstuvwxyz'
  else:
    battleSet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  global player
  if not os.path.exists("GameSaveFile.txt"):
      with open("GameSaveFile.txt", "w") as f:
          f.write("0\n10\n5\n5\n1\n0\n0\n" + battleSet + "\n")
  print("This information will be useful later\nThank you for your contributions")
  time.sleep(2)
  print("\nE N T E R P O T A T O\n")
  time.sleep(1)
  print("Game Start!\n\n\n")
  time.sleep(1)
  print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n\n\n")
  time.sleep(1)

def getStats():
  """GETS STATS FROM SAVE FILE"""
  global gameSaveStats
  global savePoint
  global player
  global battleSet
  if os.path.exists("GameSaveFile.txt"):
    try:
      with open("GameSaveFile.txt", "r") as gameSaveStats:
        saveFileLines = gameSaveStats.readlines()
      player = {"health": int(saveFileLines[1]), 
                "attack": int(saveFileLines[2]), 
                "speed": int(saveFileLines[3]),
                "critChance": int(saveFileLines[4]),
                "money": int(saveFileLines[5]),
                "crimes": int(saveFileLines[6])}
      battleSet = saveFileLines[7].strip()
      savePoint = int(saveFileLines[0])
    except IndexError:
      raise Exception("Your save file is corrupted\n")
  elif not os.path.exists("GameSaveFile.txt"):
    raise Exception("Your save file is missing\n")

#################################################################################

"""BATTLE SCRIPTS"""

def battlePRACTICE(battleSet):
  """SETS STATS FOR ENEMY: Weak potato)"""
  global enemyStats
  enemyStats = {"name": "Weak Potato",
                "desc": "Really Weak",
                "health": 10,
                "attack": 5,
                "damage": 2,
                "accuracy": 4,
                "defense": 5,
                "speed": 1}
  """INTRO TEXT"""
  print("This will be a practice battle for you to get used to the mechanics\n")
  print("Weak potato appears to test your skill")
  print("Get ready!\n")
  print("Press 'Enter' to continue\n")
  background('whocanitbenow.gif')
  pyip.inputNum(blank = True)
  time.sleep(2.5)
  battleCheckLoop(enemyStats, player, battleSet)
  background('cat-dance.gif')

def battleOld(battleSet):
  """SETS STATS FOR ENEMY: Old Potato)"""
  enemyStats = {"name": "Sickly Old Potato",
                "desc": "Sick and old, can probably be taken down in one hit", 
                "health": 1,
                "attack": 1, 
                "damage": 0,
                "accuracy": 5,
                "defense": 5,
                "speed": 0}
  """INTRO TEXT"""
  print("Old potato appears!\n")
  print('"Prepare to lose sonny boy!"\n')
  print("Press 'Enter' to continue\n")
  pyip.inputNum(blank = True)
  time.sleep(2.5)
  battleCheckLoop(enemyStats, player, battleSet)

def battleRich(battleSet):
  """SETS STATS FOR ENEMY: Rich man)"""
  enemyStats = {"name": "Really Rich Guy",
                "desc": "Has a lot of money, money that you want", 
                "health": 20,
                "attack": 10, 
                "damage": 3,
                "accuracy": 2,
                "defense": 2,
                "speed": 3}
  """INTRO TEXT"""
  print("Wealthy Man Is Preparing To Attack You!\n")
  print('"Im not going down without a fight!"\n')
  print('"Prepare to Die for your crimes! - Wealthy Man\n"')
  print("You sense that this is going to be a tough battle, must be a *BOSS ENEMY* be careful\n")
  print("Press 'Enter' to continue\n")
  pyip.inputNum(blank = True)
  time.sleep(2.5)
  battleCheckLoop(enemyStats, player, battleSet)

def battleDesertPotato(battleSet):
  """SETS STATS FOR ENEMY: Desert Potato)"""
  enemyStats = {"name": "Desert Potato",
                "desc": "Very angry, and very fast", 
                "health": 15,
                "attack": 7, 
                "damage": 4,
                "accuracy": 3,
                "defense": 3,
                "speed": 3.5}
  """INTRO TEXT"""
  print("Desert Potato Hates Rulebreakers Like You!\n")
  print('"You should always follow the rules!"\n')
  print('"Prepare to Die!" - Desert Potato\n')
  print("Press 'Enter' to continue\n")
  pyip.inputNum(blank = True)
  time.sleep(2.5)
  battleCheckLoop(enemyStats, player, battleSet)

def battleDessertPotato(battleSet):
  """SETS STATS FOR ENEMY: Dessert Potato)"""
  enemyStats = {"name": "Dessert Potato",
                "desc": "Took the name 'Sweet potato' too seriously and covered himself in marshmallows", 
                "health": 18,
                "attack": 8, 
                "damage": 3,
                "accuracy": 3,
                "defense": 2,
                "speed": 1.5}
  """INTRO TEXT"""
  print("Dessert Potato Is A Crime Against Nature!\n")
  print('"I am a sweet potato"\n')
  print('"You should be frightened!" - Dessert Potato\n')
  print("Press 'Enter' to continue\n")
  pyip.inputNum(blank = True)
  time.sleep(2.5)
  battleCheckLoop(enemyStats, player, battleSet)

def battleKatTut(battleSet):
  """SETS STATS FOR ENEMY: Kat Tut)"""
  enemyStats = {"name": "Kat Tut",
                "desc": "God of trivia and is also really funny", 
                "health": 25,
                "attack": 13, 
                "damage": 5,
                "accuracy": 2,
                "defense": 1,
                "speed": 5}
  """INTRO TEXT"""
  print("Kat Tut Is Unbelievably Powerful! *BOSS ENEMY*\n")
  print('"I am the best Peggle master"\n')
  print('"Prepare to lose!" - Kat Tut\n')
  print("Press 'Enter' to continue\n")
  pyip.inputNum(blank = True)
  time.sleep(2.5)
  battleCheckLoop(enemyStats, player, battleSet)

def battleBirb(battleSet):
  """SETS STATS FOR ENEMY: Birb)"""
  enemyStats = {"name": "Birb",
                "desc": "Very scary birb", 
                "health": 1,
                "attack": 15, 
                "damage": 1,
                "accuracy": 2,
                "defense": 1,
                "speed": 600000000000000000000000}
  """INTRO TEXT"""
  print("FEAR THE SCARY BIRB\n")
  print('*Birb laughs maniacally with a horrifying voice*\n')
  print('"HAHAHHAHAHAHAH" - Scary Birb\n')
  print("Press 'Enter' to continue\n")
  pyip.inputNum(blank = True)
  time.sleep(2.5)
  battleCheckLoop(enemyStats, player, battleSet)

def battleSwarmBirb(battleSet):
  """SETS STATS FOR ENEMY: Swarm of Birds)"""
  enemyStats = {"name": "Swarm Of Birb",
                "desc": "HUNDREDS OF BIRDS, HUNDREDS OF ANGRY BIRDS", 
                "health": 40,
                "attack": 18, 
                "damage": 5,
                "accuracy": 0,
                "defense": 1,
                "speed": 5}
  """INTRO TEXT"""
  print("This is a lot of very strong birds *BOSS ENEMY*\n")
  print('*The Birds cackle maniacally with the volume of 500 people*\n')
  print('"HAHAHHAHAHAHAH" - Scary Birbs\n')
  print("Press 'Enter' to continue\n")
  pyip.inputNum(blank = True)
  time.sleep(2.5)
  battleCheckLoop(enemyStats, player, battleSet)

def battleCURSEOFBEES(battleSet):
  """SETS STATS FOR ENEMY: ErmalThaqui97 bee swarm)"""
  enemyStats = {"name": "Curse of 10000 bees",
                "desc": "Its a lot of bees, bees that have been sent to your mailbox", 
                "health": 16,
                "attack": 13, 
                "damage": 2,
                "accuracy": 2,
                "defense": 3,
                "speed": 6}
  """INTRO TEXT"""
  print("BZZZZZZZZZZZZZZZZZZZZZZZZ\n")
  print('*BZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ*\n')
  print('"BZZZZZZZZZZZZZZZZZZZZZZZz" - CURSE OF 10000 BEES\n')
  print("Press 'Enter' to continue\n")
  pyip.inputNum(blank = True)
  time.sleep(2.5)
  battleCheckLoop(enemyStats, player, battleSet)

def battleErmalThaqui(battleSet):
  """SETS STATS FOR ENEMY: ErmalThaqui97)"""
  enemyStats = {"name": "Ermal Thaqui 97",
                "desc": "Scammer", 
                "health": 48,
                "attack": 20, 
                "damage": 6,
                "accuracy": 2,
                "defense": 1,
                "speed": 5}
  """INTRO TEXT"""
  print("Ermal gets ready to scam you!\n")
  print('*This is a very very strong enemy*\n')
  print('"Download SurfNet VPN and i will send $16000" - ErmalThaqui97@gmail.com\n')
  print("Press 'Enter' to continue\n")
  pyip.inputNum(blank = True)
  time.sleep(2.5)
  battleCheckLoop(enemyStats, player, battleSet)


################################################################################

"""BATTLE SYSTEM"""

def battleCheckLoop(enemyStats, player, battleSet):
  os.system('clear')
  if enemyStats.get("speed") > player.get("speed"):
    enemyAttack(enemyStats, player, battleSet)
    if player.get("health") <= 0:
      battleLose()
  elif enemyStats.get("speed") <= player.get("speed"):
    battleMenu(enemyStats, player, battleSet)
  while True:
    if enemyStats.get("health") > 0:
      if player.get("health") > 0:
        battleMenu(enemyStats, player, battleSet)
      else:
        break
    else:
      break
  if player.get("health") > 0:
    battleWin()
  elif player.get("health") <= 0:
    battleLose()

def battleAttack(enemyStats, player, battleSet):
  """GAME LOOP FOR ATTACKING"""
  amountWrong = 0
  amountRight = 0
  for x in range(player.get("attack")):
    oldTime = time.time()
    keytopress = random.choice(battleSet)
    pressed = input("Press {}\n:".format(keytopress))
    newTime = time.time()
    if newTime - oldTime < 2:
      if pressed != keytopress:
        amountWrong += 1
      else:
        critA = random.randint(0, int(18/player.get("critChance")))
        critB = random.randint(0, int(18/player.get("critChance")))
        if critA == critB:
          amountRight += player.get("attack")
          print("CRITICAL HIT!\n")
          background('critical-hit.gif')
          time.sleep(0.25)
          revert_gif()
        else:
          amountRight += 1
    else:
      amountWrong += 1
    os.system('clear')
  if amountWrong <= enemyStats.get("defense"):
    print("Attack successful! >:)\n")
    enemyStats["health"] -= amountRight
    if amountRight > 0:
      print("{} has {} health remaining\n".format(enemyStats.get("name"), enemyStats.get("health")))
    else:
      print("You did no damage :(\n")
  else:
    print("Failed attack :(\n")
    print("{} has {} health remaining\n".format(enemyStats.get("name"), enemyStats.get("health")))

def enemyAttack(enemyStats, player, battleSet):
  """CODE WHEN ENEMY ATTACKS YOU"""
  print("Defend from {}'s attack!\n".format(enemyStats.get("name")))
  time.sleep(1.5)
  amountWrong = 0
  amountRight = 0
  for x in range(enemyStats.get("attack")):
    oldTime = time.time()
    keytopress = random.choice(battleSet)
    pressed = input("Press {}\n:".format(keytopress))
    newTime = time.time()
    if newTime - oldTime < 2:
      if pressed != keytopress:
        amountWrong += 1
      else:
        amountRight += 1
    else:
      amountWrong += 1
    os.system('clear')
  if amountWrong <= enemyStats.get("accuracy"):
    print("You blocked\n")
  else:
    print("Failed block :(\n")
    player["health"] -= enemyStats.get("damage")
    print("You took {} damage\n".format(str(enemyStats.get("damage"))))
    print("You have {} health remaining\n".format(str(player.get("health"))))

def battleDefend(enemyStats, player):
  """DEFEND FROM ATTACK"""
  print("Defend from {}'s attack! DO NOT MESS UP!\n".format(enemyStats.get("name")))
  time.sleep(1.5)
  amountWrong = 0
  amountRight = 0
  for x in range(enemyStats.get("attack")):
    oldTime = time.time()
    keytopress = random.choice(battleSet)
    pressed = input("Press {}\n:".format(keytopress))
    newTime = time.time()
    if newTime - oldTime < 2:
      if pressed != keytopress:
        amountWrong += 1
      else:
        amountRight += 1
    else:
      amountWrong += 1
    os.system('clear')
  if amountWrong <= enemyStats.get("accuracy"):
    print("You blocked\n")
  else:
    print("Failed block :(\n")
    player["health"] -= enemyStats.get("damage")*0.5
    print("You took {} damage\n".format(str(enemyStats.get("damage")*0.5)))
    print("You have {} health remaining\n".format(str(player.get("health"))))

def battleMenu(enemyStats, player, battleSet):
  """BATTLE MENU"""
  print("What would you like to do?\n")
  menuAns = pyip.inputMenu(["Attack", "Defend", "Check"], numbered=True)
  if menuAns == "Attack":
    battleAttack(enemyStats, player, battleSet)
    if enemyStats.get("health") > 0:
      enemyAttack(enemyStats, player, battleSet)
    else:
      pass
  elif menuAns == "Defend":
    battleDefend(enemyStats, player)
  elif menuAns == "Check":
    print("Name: {}\n".format(str(enemyStats.get("name"))))
    print("{}\n".format(str(enemyStats.get("desc"))))
    print("Health: {}\n".format(str(enemyStats.get("health"))))
    print("Attack: {}\n".format(str(enemyStats.get("attack"))))
    print("Damage: {}\n".format(str(enemyStats.get("damage"))))
    print("Accuracy: {}\n".format(str(enemyStats.get("accuracy"))))
    print("Defense: {}\n".format(str(enemyStats.get("defense"))))
    print("Speed: {}\n".format(str(enemyStats.get("speed"))))
    time.sleep(5)
    battleMenu(enemyStats, player, battleSet)

def battleWin():
  print("You won! Good job!\n")

def battleLose():
  print("You lost :(\n")
  print("DEATH - You died to an enemy\n")
  time.sleep(1)
  quit()

#################################################################################

"""ADDITIONAL SCRIPTS"""

def save(savePoint):
  global player
  playAudio("Save")
  saveLoad()
  savePoint += 1
  with open("GameSaveFile.txt", "r") as gameSaveStats:
    saveFileLines = gameSaveStats.readlines()
  saveFileLines[0] = str(savePoint) + "\n"
  saveFileLines[1] = str(player.get("health")) + "\n"
  saveFileLines[2] = str(player.get("attack")) + "\n"
  saveFileLines[3] = str(player.get("speed")) + "\n"
  saveFileLines[4] = str(player.get("critChance")) + "\n"
  saveFileLines[5] = str(player.get("money")) + "\n"
  saveFileLines[6] = str(player.get("crimes")) + "\n"
  saveFileLines[7] = battleSet
  with open("GameSaveFile.txt", "w") as gameSaveStats:
    gameSaveStats.writelines(saveFileLines)
  print("Game Saved!\n")
  stopAudio()

def letsGoGambling():
  playAudio('Lapis')
  completed = 0
  completed5050 = False
  completedWAR = False
  completedGetRichQuick = False
  luigiTEXT = ["You look like a Claude Lobster fan\n", "I, Am Luigi\n", "Have you tried winning?\n", "Theres no shame in losing to me.\n", "You seem like you would lose to Magikarp while having a Tera-Electric Miraidon\n", "You are not the best potato, I am\n", "Even Dr. Mario can't save your wallet now!\n", "You should just get gooderer\n", "Honor dies in the gambling hall.\n", "Your wallet will feel the pain of the tuffles\n", "Imagine losing to a retired 50 year old plumber.\n", "Tiger Drop won't negate the damage done to your credit score.\n", "This casino is very grateful to our generous sponsors: the number three and butter\n", "Potato.. I will cut you down, break you apart, splay the gore of your profane form across the STARS! I will chop you down until the very SHREDS CRY FOR MERCY! My hands shall RELISH ENDING YOU... HERE! AND! NOW!\n", "BEHOLD! THE POWER OF A GAMBLING ADDICT!\n", "I'll let you in on an little something, The Gambling game, it's not like boxing. The guy who gets beat down isn't the loser. It's the guy who can't tough it out until the end, He's the one who loses.\n", "NEVER RETREAT NEVER SURRENDER!!\n", "You are so weak I bet you think that the 1000-THR 'Earthmover' was a hard bossfight\n"]
  print("You have ${} money\n".format(player.get("money")))
  background('luigi-main.gif')
  time.sleep(3)
  while completed != 3:
    print('"Which game do you want to play?" - Luigi\n')
    whichOne = pyip.inputMenu(['Roulette', "WAR", "Get rich quick!", "Exit."], numbered = True)
    luigiMeanText = random.choice(luigiTEXT)
    if whichOne == 'Roulette':
      result = roulette()
      if result:
        if not completed5050:
          background('luigi-win.gif')
          completed += 1
          completed5050 = True
          time.sleep(5)
          revert_gif()
        else:
          background('luigi-win.gif')
          print("You've already played this game, you get no completion points for this\n")
          time.sleep(5)
          revert_gif()
      elif not result:
        background('luigi-lose.gif')
        print("You lost, you get no completion points for this\n")
        time.sleep(5)
        revert_gif()
        background('gigachad-luigi.gif')
        print("{} - Luigi\n".format(luigiMeanText))
        time.sleep(5)
        revert_gif() 
    elif whichOne == "WAR":
      result = sillyGame()
      if result:
        if not completedWAR:
          background('luigi-win.gif')
          completed += 1
          completedWAR = True
          time.sleep(5)
          revert_gif()
        else:
          background('luigi-win.gif')
          print("You've already played this game, you get no completion points for this\n")
          time.sleep(5)
          revert_gif()
      elif not result:
        background('luigi-lose.gif')
        print("You lost, you get no completion points for this\n")
        time.sleep(5)
        revert_gif()
        background('gigachad-luigi.gif')
        print("{} - Luigi\n".format(luigiMeanText))
        time.sleep(5)
        revert_gif() 
    elif whichOne == "Get rich quick!":
      result = getRichQuick()
      if result:
        if not completedGetRichQuick:
          background('luigi-win.gif')
          completed += 1
          completedGetRichQuick = True
          time.sleep(5)
          revert_gif()
        else:
          background('luigi-win.gif')
          print("You've already played this game, you get no completion points for this\n")
          time.sleep(5)
          revert_gif()
      elif not result:
        background('luigi-lose.gif')
        print("You lost, you get no completion points for this\n")
        time.sleep(5)
        revert_gif()
        background('gigachad-luigi.gif')
        print("{} - Luigi\n".format(luigiMeanText))
        time.sleep(5)
        revert_gif() 
    elif whichOne == "Exit.":
      background('gigachad-luigi.gif')
      print("You have ${} money\n".format(player.get("money")))
      print("THERE IS NO ESCAPE FROM THE CASINO!\n")
      time.sleep(5)
      revert_gif()

def roulette():
  win = False
  print("This is a TOTALLY 'fair' game\n")
  time.sleep(1)
  print("You have {} money remaining\n".format(str(player.get("money"))))
  if player["money"] >= 15:
    playOrNot = pyip.inputYesNo("Play?\n")
    bet = int(pyip.inputInt("Bet how much?\n(Max bet = 50, Min bet = 15)", min = 15, max = 50))
    if playOrNot == "yes":
      chance = random.choice(["RED", "BLACK"])
      playerGuess = pyip.inputStr("Red or Black?\n", allowRegexes = ['Red', 'Black'])
      time.sleep(2)
      if chance == playerGuess.upper():
        print("You win!\n")
        player["money"] += (bet * 2)
        print("You have {} money remaining\n".format(str(player.get("money"))))
        win = True
      elif chance != playerGuess.upper():
        print("You lose :(\n")
        player["money"] -= bet
        print("You have {} money remaining\n".format(str(player.get("money"))))
        win = False
      return win
    elif playOrNot == "no":
        print("P A T H E T I C\n")
        player["money"] -= 5 
        print("{} money remaining\n".format(str(player.get("money"))))
  elif player["money"] < 15:
    print("You have no money to bet!\n")

def sillyGame():
  win = False
  deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1]
  random.shuffle(deck)
  random.shuffle(deck)
  youHand = []
  enemyHand = []
  print("You have {} money remaining\n".format(str(player.get("money"))))
  if player["money"] >= 10:
    playorNot = pyip.inputYesNo("Play?\n")
    if playorNot == "yes":
      wager = int(pyip.inputInt(min = 10, max = player.get("money"), prompt = "How much to wager?\n(Max wager = however much money you have, Min wager = 10)\n"))
      print("Welcome to the silly game (Its just war if you've ever played)\n")
      time.sleep(1)
      print("Your goal is to get all of the cards in the deck\n")
      print("You get the opponent's card if your card is higher\n")
      print("If it is a tie, you both lose your cards\n")
      print("Good luck!\n")
      time.sleep(1)
      playAudio('DS_Cinder')
      time.sleep(2)
      enemyHand = deck[:26]
      youHand = deck[26:52]
      while len(youHand) != 0 and len(enemyHand) != 0:
        try:
          enemyPlay = random.choice(enemyHand)
        except IndexError:
          break
        try:
          yourPlay = random.choice(youHand)
        except IndexError:
          break
        print("You played a {0}\n".format(yourPlay))
        print("Your opponent played a {0}\n".format(enemyPlay))
        if yourPlay > enemyPlay:
          if yourPlay == 13:
            youHand.remove(yourPlay)
            deck.append(yourPlay)
            youHand.append(enemyPlay)
            enemyHand.remove(enemyPlay)
            print("You lost a {0}\n".format(yourPlay))
            print("You won a {0}\n".format(enemyPlay))
          else:
            youHand.append(enemyPlay)
            enemyHand.remove(enemyPlay)
            time.sleep(0.05)
            print("You won a {0}\n".format(enemyPlay))
        elif yourPlay < enemyPlay:
          if enemyPlay == 13:
            enemyHand.remove(enemyPlay)
            deck.append(enemyPlay)
            enemyHand.append(yourPlay)
            youHand.remove(yourPlay)
            print("The enemy lost a {0}\n".format(enemyPlay))
            print("You lost a {0}\n".format(yourPlay))
          else:
            enemyHand.append(yourPlay)
            youHand.remove(yourPlay)
            time.sleep(0.05)
            print("You lost a {0}\n".format(enemyPlay))
        else:
          if yourPlay == enemyPlay:
            print("TIE!\n")
            deck.append(yourPlay)
            deck.append(enemyPlay)
            youHand.remove(yourPlay)
            enemyHand.remove(enemyPlay)
      if len(youHand) > len(enemyHand):
        player["money"] += (wager * 2)
        win = True
        os.system("clear")
        time.sleep(1.5)
        print("You won!")
        time.sleep(0.5)
        print("{} money remaining\n".format(str(player.get("money"))))
      elif len(youHand) < len(enemyHand):
        player["money"] -= wager
        win = False
        os.system("clear")
        time.sleep(1.5)
        print("You lost!")
        time.sleep(0.5)
        print("{} money remaining\n".format(str(player.get("money"))))
      stopAudio()
      return win
    elif playorNot == "no":
        print("P A T H E T I C\n")
        player["money"] -= 5
        print("{} money remaining\n".format(str(player.get("money"))))
  elif player["money"] < 10:
    print("You have no money to bet!\n")

def getRichQuick():
  win = False
  playOrNot = pyip.inputYesNo("Play?\n")
  print("You have {} money remaining\n".format(str(player.get("money"))))
  if player["money"] >= 5:
    if playOrNot == "yes":
      moneySpent = int(pyip.inputNum("How much to bet?\n(Max bet = 75, Min bet = 5)\n", min = 5, max = 75))
      chance = random.randint(1,5)
      time.sleep(1)
      guess = pyip.inputNum("Guess a number between 1 and 5\n", min = 1, max = 5)
      time.sleep(2)
      if chance == guess:
        time.sleep(0.5)
        print("You win!\n")
        player["money"] += (moneySpent * 3)
        print("You have {} money remaining\n".format(str(player.get("money"))))
        win = True
      else:
        time.sleep(0.5)
        print("You lose :(\n")
        player["money"] -= moneySpent 
        print("You have {} money remaining\n".format(str(player.get("money"))))
        win = False
      return win
    elif playOrNot == "no":
      print("P A T H E T I C\n")
      player["money"] -= 5 
      print("{} money remaining\n".format(str(player.get("money"))))
  elif player["money"] < 5:
    print("You have no money to bet!\n")

  """Kat Tut Comedy And Trivia"""
def katTutEvent():
  katTutComedyNew = ["You're telling me a shrimp fried this rice?", "Road work ahead, uh yeah, I sure hope it does", "Bird flu, yeah, they tend to do that", "Apartment complex? I find it quite simple really", "If wood fired Pizza? How is Pizza supposed to get a job now?", "What's up stairs? They can't talk", "Chef's kiss? Do they really?", "You're telling me a gar licked this bread?", "Blood drive? It has a license?", "Your all right? I thought you're all LEFT", "Did you know that a frog can jump higher that the Eiffel tower? This is because Eiffel tower cannot jump.", "Re:Fridgerator? I heard about the vending machine isekai but this is getting ridiculous", "Shoes smell? They don't have noses", "Why can't dinosaurs clap their hands? Because they are extinct", "Slippery when wet? I'd be shocked if it wasn't", "Paper jam? Sounds awful, why would you make that?", "Fire exit? Then where am I supposed to leave?", "", "", ""]
  katTutComedyOld = []
  random.shuffle(katTutComedyNew)
  print("You see Kat Tut on stage in his famous outfit from Peggle Nights\n")
  time.sleep(1)
  background('kat-tut.gif')
  time.sleep(3.5)
  print('"You there, in the crowd, come join me up on stage for a game of trivia!" - Kat Tut\n')
  time.sleep(2)
  print("You are pulled up onto the stage by Kat Tut\n")
  time.sleep(1.5)
  print("Kat Tut will start to ask you questions\n")
  time.sleep(1.5)
  print("Good luck!\n")
  time.sleep(2.5)
  amountCorrect = 0
  questionAns1 = ["In Like a Dragon: Pirate Yakuza in Hawaii, Goro Majima gets amnesia and winds up washing ashore on what island?", "Honolulu", "Rich Island", "Madlantis", "Nele Island", "Rich Island"]
  questionAns2 = ["What is the nickname for the 1000-THR 'Earthmover'", "Richard", "Epic Cool Guy", "Benjamin", "Tuberculosis", "Benjamin"]
  questionAns3 = ["What is the name of the obtainable Cosmog in the crown tundra DLC for pokemon S/S", "Fwoofy", "Balloon", "Gengar", "Potato", "Fwoofy"]
  questionAns4 = ["In what game does famous character, Scientist-Form Jimmy Lightning, make his debut?", "Peggle Deluxe", "Pokemon Scarlet/Violet", "Peggle 2", "Peggle Nights", "Peggle Nights"]
  questionAns5 = ["What is the ability of the character, Warren Rabbit, in Peggle Deluxe?", "Lucky Spin", "MAGIC HAT", "Multi-ball", "Bunny Hop", "Lucky Spin"]
  questionAns6 = ["From what game does the level officially named: 'The level colloquially known as 4-s' originate?", "Yakuza 0", "Peggle 2", "ULTRAKILL", "Pokemon Red/Blue", "ULTRAKILL"]
  questionAns7 = ["Who is the main antagonist of the game, 'Pajama Sam: No Need To Hide When It's Dark Outside'?", "Literally Just Satan", "Darkness", "Lightness", "EVIL Pajama Sam", "Darkness"]
  questionAns8 = ["What is the first pokemon?", "Bulbasaur", "Rhydon", "Pikachu", "Arceus", "Rhydon"]
  questionAns9 = ["Who/What is the real-life inspiration for the final boss of ENTER POTATO?", "Kat Tut", "Asher Zost's left toe", "Mr. Francis, high school health teacher", "Doug.", "Mr. Francis, high school health teacher"]
  questionAns10 = ["What is the most hated pokemon by the father of the creator of this game?", "Charjabug", "Pichu", "Wormadam - Trash form", "Golurk", "Charjabug"]
  questionAns11 = ["Who's the captain of the Ginyu force", "Trunks", "Gohan", "Frieza", "Ginyu", "Ginyu"]
  questionAns12 = ["What is the ability of the pokemon Eiscue?", "Ice Face", "Ice Wall", "Ice Spikes", "Fire Body", "Ice Face"]
  questionAns13 = ["What is Kazuma Kiryu's name in Like a Dragon Ishin?", "Mr. Shakedown", "Sakamoto Ryoma", "Special Ketamine", "Kazuma Kiryu", "Sakamoto Ryoma"]
  questionAns14 =["How many calories are in one gram of enriched uranium-238?", "21.86 billion", "413 million", "5^2²", "800 Trillion", "413 million"]
  questionAns15 = ["Who is your rival in Pokemon Sun/Moon?", "Hau", "Prof. Kukui's Abs", "Piplup²", "Samson Oak", "Hau"]
  questionAns16 = ["Who Goku fight on Namek?", "Majin Buu", "Lord Frieza", "King Cold", "Cooler", "Lord Frieza"]
  questionAns17 = ["Who killed Big Boss?", "Solid Snake", "Venom Snake", "Naked Snake", "Revolver Ocelot", "Solid Snake"]
  questionAns18 = ["What is Palworld's version of pikachu?", "Chillet", "Pikachu 2", "Sparkit", "Grizzbolt", "Sparkit"]
  questionAns19 = ["What year does William Woodus famously not remember?", "2012", "2013", "2014", "2015", "2012"]
  questionAns20 = ["What is Mr. Francis's secret class?", "Meth", "Math", "Conspiracy II B", "Advanced Murder", "Conspiracy II B"]
  questions = {1: questionAns1, 2: questionAns2, 3: questionAns3, 4: questionAns4, 5: questionAns5, 6: questionAns6, 7: questionAns7, 8: questionAns8, 9: questionAns9, 10: questionAns10, 11: questionAns11, 12: questionAns12, 13: questionAns13, 14: questionAns14, 15: questionAns15, 16: questionAns16, 17: questionAns17, 18: questionAns18, 19: questionAns19, 20: questionAns20}
  questionsModify = questions.copy()
  while amountCorrect < 10:
    try:
      choice = random.choice(list(questionsModify.keys()))
      questionSet = questionsModify[choice]
      whatAsk = str(questionSet[0])
      question1 = str(questionSet[1])
      question2 = str(questionSet[2])
      question3 = str(questionSet[3])
      question4 = str(questionSet[4])
      correct = str(questionSet[5])
      questionsModify.pop(choice)
      print("Amount Correct: {}\n".format(str(amountCorrect)))
      time.sleep(1)
      whatPLayerSaid = pyip.inputMenu([question1, question2, question3, question4], numbered = True, prompt = whatAsk + " - Kat Tut\n")
      if whatPLayerSaid == correct:
       print('"Bingo!" - Kat Tut\n')
       amountCorrect += 1
       background('cat-breakdance.gif')
       time.sleep(4.5)
       background('kat-tut.gif')
      else:
        print('"Major Skill Issue" - Kat Tut\n')
        background('cat-fire.gif')
        time.sleep(3)
        background('kat-tut.gif')
      print("Kat Tut Comedy Time!\n")
      time.sleep(1.5)
      sayJoke = katTutComedyNew[random.randint(0, len(katTutComedyNew)-1)]
      katTutComedyOld.append(sayJoke)
      katTutComedyNew.remove(sayJoke)
      print('"{}" - Kat Tut\n'.format(sayJoke))
      background('puekeko.gif')
      time.sleep(1.5)
      background('kat-tut.gif')
    except IndexError:
      print("Either I messed up somehow or you are so bad at trivia that you have run out of questions\n")
      time.sleep(2)
      print("The game goes on!\n")
      time.sleep(1.5)
      break
    finally:
      time.sleep(2)
      x = 0
      while len(katTutComedyOld) != 0:
        while len(katTutComedyNew) != 20:
          katTutComedyNew.append(katTutComedyOld[x])
          katTutComedyOld.remove(katTutComedyOld[x])
  if amountCorrect >= 10:
    print("You have answered enough questions correctly to win the game!\n")
    time.sleep(1.5)
    print('"You have won trivia!" - Kat Tut\n')
    time.sleep(1.5)
    print('"Good job!" - Kat Tut\n')
    time.sleep(1.5)
    print('"But first you must defeat me to get your prize!" - Kat Tut\n')
  elif amountCorrect < 10:
    print("You have failed trivia\n")
    time.sleep(1.5)
    print('"I am very angry at you now" - Kat Tut\n')
    time.sleep(1.5)
    print('"You can still prove yourself worthy by defeating me in a battle" - Kat Tut\n')
  time.sleep(1.5)
  battleKatTut(battleSet)
  time.sleep(1.5)
  print('"You have earned your prize!" - Kat Tut\n')
  time.sleep(1.5)
  print('"Here is a powerful weapon for you to use!" - Kat Tut\n')
  time.sleep(1.5)
  print("Kat Tut hands you a weapon\n")
  time.sleep(1.5)
  player["attack"] += 3
  print("You now do 3 more damage\n")
  time.sleep(1.5)
  print("You will now have a higher chance of landing a critical hit\n")
  time.sleep(1.5)
  player["critChance"] += 1
  print('"Good luck on your journey" - Kat Tut\n')
  time.sleep(2.5)

  """Lost Woods Area Puzzle"""
def lostWoods():
  sequence = ["f", "l", "r", "r", "f", "f", "l", "r", "l", "f"]
  random.shuffle(sequence)
  random.shuffle(sequence)
  x = 0
  directionsWent = []
  time.sleep(1.5)
  while x < len(sequence):
    whatDirectionStr = ""
    whatDirection = pyip.inputMenu(["Go forwards", "Go left", "Go right"], numbered = True, prompt = "In what direction will you move?\n")
    if whatDirection == "Go forwards":
      if x > 0 and directionsWent[x-1] == whatDirection:
        print("(Why would you go the same direction if you already know it is wrong?)\n")
        time.sleep(1)
      directionsWent.append(whatDirection)
      whatDirectionStr = "f"
    elif whatDirection == "Go left":
      if x > 0 and directionsWent[x-1] == whatDirection:
        print("(Why would you go the same direction if you already know it is wrong?)\n")
        time.sleep(1)
      directionsWent.append(whatDirection)
      whatDirectionStr = "l"
    elif whatDirection == "Go right":
      if x > 0 and directionsWent[x-1] == whatDirection:
        print("(Why would you go the same direction if you already know it is wrong?)\n")
        time.sleep(1)
      directionsWent.append(whatDirection)
      whatDirectionStr = "r"
    if whatDirectionStr == sequence[x]:
      time.sleep(1)
      print("You got lucky and you didn't get lost! (This turn)\n")
      time.sleep(1)
      print("You continue travelling to the next area\n")
      x += 1
      directionsWent.clear()
      time.sleep(2)
      os.system('clear')
    else:
      time.sleep(1)
      print("You took a wrong turn\n")
      time.sleep(1)
      print("You hear a frightening sound from above you\n")
      time.sleep(1)
      print("A very scary bird appears and attacks you!\n")
      time.sleep(1)
      battleBirb(battleSet)
      time.sleep(1)
      print("After defeating the bird, you turn around and go back to the area previous\n")
      time.sleep(3)
      os.system('clear')

##################################################################################

"""Audio & Graphics Setup"""
app = Flask(__name__)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


current_gif = ""
current_audio = ""
previous_gif = ""

audio_files = {
    "PeggleJazz": ("PeggleJazz.mp3", True),
    "PeggleMarch": ("PeggleMarch.mp3", True),
    "PeggleSynth": ("PeggleSynth.mp3", True),
    "Lapis": ("LapisPhilosophorum.mp3", True),
    "DS_Cinder": ("DS_Cinder.mp3", True),
    "Save": ("CharmlessMan.mp3", False)
}

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>ENTERPOTATO DISPLAY</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                background-color: black;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                overflow: hidden;
            }
            img {
                max-width: 100%;
                max-height: 100%;
                object-fit: contain;
            }
            #audioPlayer {
                display: none;
            }
        </style>
        <script>
            let currentGif = '';
            let currentAudio = '';
            
            function updateGif() {
                if (currentGif) {
                    document.getElementById('gif').src = '/bg/' + currentGif;
                }
            }
            
            function updateAudio() {
                const audioPlayer = document.getElementById('audioPlayer');
                if (currentAudio) {
                    const [audioFile, shouldLoop] = currentAudio.split('|');
                    audioPlayer.src = '/audio/' + audioFile;
                    audioPlayer.loop = shouldLoop === '1';
                    audioPlayer.play().catch(e => console.log('Audio play failed:', e));
                } else {
                    audioPlayer.pause();
                    audioPlayer.src = '';
                }
            }
            
            function checkForUpdates() {
                fetch('/current_gif')
                    .then(response => response.text())
                    .then(gifName => {
                        if (gifName !== currentGif) {
                            currentGif = gifName;
                            updateGif();
                        }
                    })
                    .catch(e => console.log('GIF fetch error:', e));
                    
                fetch('/current_audio')
                    .then(response => response.text())
                    .then(audioName => {
                        if (audioName !== currentAudio) {
                            currentAudio = audioName;
                            updateAudio();
                        }
                    })
                    .catch(e => console.log('Audio fetch error:', e));
            }
            checkForUpdates();
            let intervalCount = 0;
            const fastInterval = setInterval(() => {
                checkForUpdates();
                intervalCount++;
                if (intervalCount > 5) {
                    clearInterval(fastInterval);
                    setInterval(checkForUpdates, 2000);
                }
            }, 300);
        </script>
    </head>
    <body>
        <img id="gif" src="" style="display: none;" onload="this.style.display='block';">
        <audio id="audioPlayer"></audio>
    </body>
    </html>
    '''

@app.route('/current_gif')

def get_current_gif():
    return current_gif

@app.route('/current_audio')

def get_current_audio():
    return current_audio

@app.route('/bg/<path:filename>')
def serve_gif(filename):
    return send_from_directory('BG', filename)

@app.route('/audio/<path:filename>')
def serve_audio(filename):
    return send_from_directory('Mus', filename)

def start_server():
    app.run(host='0.0.0.0', port=5000, use_reloader=False, debug=False)

def background(gif_name):
    global current_gif, previous_gif
    if current_gif and current_gif != gif_name:
        previous_gif = current_gif
    current_gif = gif_name

def revert_gif():
    global current_gif, previous_gif
    if previous_gif:
        current_gif, previous_gif = previous_gif, current_gif
    return current_gif

def playAudio(track_name):
    global current_audio
    stopAudio()
    audio_file, should_loop = audio_files[track_name]
    current_audio = f"{audio_file}|{1 if should_loop else 0}"

def stopAudio():
  global current_audio
  current_audio = ""

server_thread = threading.Thread(target=start_server)
server_thread.daemon = True
server_thread.start()

time.sleep(2)
webbrowser.open('http://localhost:5000')

##################################################################################

"""Loading screen while saving"""
def saveLoad():
    loading = ["Saving ", "Saving . ", "Saving . . ", "Saving . . . "]
    def savingLoading():
        for x in range(4):
            print(loading[x])
            time.sleep(1)
            os.system('clear')
    os.system('clear')
    savingLoading()
    y = 0
    while y != 212:
        savingLoading()
        y += 4

##################################################################################

def main():
  """GAME SEQUENCE (VERY IMPORTANT)"""
  getStats()
  background("teto-house.gif")
  os.system('clear')
  if savePoint == 0:
    enterPotatoSetup()
    savePointZero()
  elif savePoint == 1:
    savePointOne()
  elif savePoint == 2:
    savePointTwo()
  elif savePoint == 3:
    savePointThree()
  elif savePoint == 4:
    savePointFour()
  elif savePoint == 5:
    savePointFive()
  elif savePoint == 6:
    savePointSix()
  elif savePoint == 7:
    savePointSeven()

#################################################################################  

"""GAME CONTENT"""

def savePointZero():
  time.sleep(2)
  battlePRACTICE(battleSet)
  if battleSet == "abcdefghijklmnopqrstuvwxyz":
    player["health"] = 10
  time.sleep(2)
  print("Now that you know the basics, we can officially start the game!\n")
  stopAudio()
  time.sleep(1)
  print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
  time.sleep(1)
  doSave = pyip.inputYesNo("Do you want to save?\n")
  if doSave == "yes":
    save(savePoint)
    savePointOne()
  elif doSave == "no":
    print("Why?\n")
    time.sleep(0.5)
    savePointOne()

def savePointOne():
  playAudio('PeggleMarch')
  print("You wake up in the middle of a forest, you have no idea how you got there.\n")
  time.sleep(1)
  print("But you know that you have one goal, to outcrime the infamous mashed potato mafia\n")
  time.sleep(1)
  print("In the distance you can faintly see what looks like civilization\n")
  time.sleep(0.5)
  prompt = pyip.inputMenu(["Stay in forest", "Go towards civilization"], numbered = True)
  if prompt == "Stay in forest":
    print("You decide to stay in the forest\n")
    print("You are stupid and die of starvation, then get eaten by a rat\n")
    time.sleep(2)
    quit()
  elif prompt == "Go towards civilization":
    time.sleep(1)
    print("As you approach your destination, you know that you were correct\n")
    time.sleep(1)
    print('You see a sign that says "Welcome to Potatoland"\n"We hope you have a very day"\n')
    time.sleep(1)
    print("Enter Potatoland?\n")
    prompt = pyip.inputMenu(["Dont", "Enter Potatoland"], numbered = True)
    if prompt == "Dont":
      print("You try to leave but suddenly 1000 mafia goons drop right on top of you and you get shot {} times in the chest before you can even move\n".format(random.randint(301,401)))
      time.sleep(1.5)
      print("Don't try to escape fate next time\n")
      time.sleep(1)
      print("DEATH - You've been 'mashed'\n")
      quit()
    print("You decide to enter Potatoland, good choice\n")
    time.sleep(1)
    print("You have now officially entered Potatoland.\n")
    time.sleep(1)
    print("While walking around Potatoland, you see a sickly old potato lying on the side of the road asking for medicine\n")
    time.sleep(1)
    prompt = pyip.inputMenu(["KILL", "Ignore"], numbered = True)
    if prompt == "Ignore":
      time.sleep(1)
      print("You are trying to outcrime the Mafia, not be a good person\n")
      time.sleep(0.5)
      print("You get shot in the back by a Mafia Goon and die\n")
      time.sleep(0.5)
      print("'You shouldn't have messed with our target' - Mafia Goon\n")
      time.sleep(0.5)
      print("DEATH - You've been 'mashed'\n")
      time.sleep(2)
      quit()
    elif prompt == "KILL":
      battleOld(battleSet)
    player["crimes"] += 1
    print("You see the sickly old potato lying on the ground, lifeless\n")
    time.sleep(1)
    print("You have now been fully set on the path of crime\n")
    time.sleep(1)
    print("You look around and see a bunch of mafia goons walking around\n")
    time.sleep(1)
    print("You wonder why there are so many in such a small village in the middle of a forest\n")
    time.sleep(1)
    print("What do you do?\n")
    prompt = pyip.inputMenu(["Dont ask Mafia Goon", "Ask Mafia Goon"], numbered = True)
    if prompt == "Ask Mafia Goon":
      time.sleep(1)
      print("You walk up to a mafia goon and ask him why there are so many mafia goons\n")
      time.sleep(1)
      print('"Why do you interfere in the affairs of the mafia?" - Mafia Goon\n')
      time.sleep(0.5)
      print('"You die now" - Mafia Goon\n')
      time.sleep(0.5)
      print("You get violently stabbed by the Mafia Goon and die\n")
      time.sleep(0.5)
      print("DEATH - You've been 'peeled'\n")
      quit()
    elif prompt == "Dont ask Mafia Goon":
      time.sleep(1)
      print("You decide to not ask the mafia goon\n")
      print("Probably a good idea to not mess with the Mashed Potato Mafia quite yet\n")
      time.sleep(1)
      print("You decide that you should go to the local shop to buy some supplies\n")
      time.sleep(2)
      print("But then you remember that you have no money\n")
      time.sleep(1)
      print("You see a rich looking man walking towards a bank holding a bag of money\n")
      time.sleep(0.5)
      print("What do you do?\n")
      prompt = pyip.inputMenu(["Rob Man", "Dont Rob"], numbered = True)
      if prompt == "Dont Rob":
        print("Really? You're going to let a rich man walk away with his money?\n")
        time.sleep(1)
        print("I think not!\n")
        time.sleep(0.5)
        print("You will rob him.\n")
        time.sleep(1)
        print("You walk up to the man and silently motion to him to give you the bag of money\n")
        time.sleep(1)
        print('"You cannot rob me!"\n')
        print('"I am too rich for you!" - Rich Man\n')
        time.sleep(1)
        print("Use force?\n")
        prompt = pyip.inputMenu(["Yes", "YES!"], numbered = True)
        if prompt == "Yes":
          time.sleep(0.5)
          battleRich(battleSet)
        elif prompt == "YES!":
          time.sleep(0.5)    
          battleRich(battleSet)
      elif prompt == "Rob Man":
        print("Good, you're learning\n")
        time.sleep(1)
        print("You walk up to the man and silently motion to him to give you the bag of money\n")
        time.sleep(1)
        print('"You cannot rob me!"\n')
        print('"I am too rich for you!" - Rich Man\n')
        battleRich(battleSet)
      player["money"] += 500
      player["crimes"] += 1
      print("You have now robbed the rich man of his money!\n")
      time.sleep(0.5)
      print("Good job! You gained $500\n")
      time.sleep(0.5)
      if player["health"] <= 6:
        print("After fighting such a tough enemy, you feel completely exhausted and are very beat up\n")
      elif player["health"] == 8 or player["health"] == 9 or player["health"] == 7:
        print("After fighting such a tough enemy, you feel a quite tired\n")
      elif player["health"] == 10:
       print("After taking down such a tough enemy so effortlessly, you feel powerful\n")
      time.sleep(1)
      print("You walk around Potatoland and notice a nice looking hotel\n")
      time.sleep(1)
      prompt = pyip.inputMenu(["Stay the night at hotel", "'Im fine' (Continue without hotel)"], numbered = True)
      if prompt == "Stay the night at hotel":
        time.sleep(0.5)
        print("You walk up to the hotel doors, and head inside\n")
        time.sleep(1)
        print("Inside you see a front desk with no one behind it\n")
        time.sleep(1)
        print("You walk up to the desk and see that the desk has a sign-in sheet on it\n")
        time.sleep(0.5)
        print("The sign sheet says 'Sign in sheet'\n")
        print("(it also says $50 per night)\n")
        time.sleep(1)
        prompt2 = pyip.inputMenu(["Get a room", "I'm not paying $50 (Do not get room)"], numbered = True)
        if prompt2 == "Get a room":
          time.sleep(0.5)
          print("You sign in, slot the money into a bin on the counter, and a room key shoots out at you\n")
          time.sleep(1)
          print("You walk up to your room and see that it is a room\n")
          time.sleep(5)
          print("You slept for the night and wake up feeling refreshed\n")
          time.sleep(1)
          player["health"] += 5
          player["money"] -= 50
          print("You have {} health remaining and {} money remaining\n".format(player.get("health"), player.get("money")))
        elif prompt2 == "I'm not paying $50 (Do not get room)":
          prompt = "'Im fine' (Continue without hotel)"
      elif prompt == "'Im fine' (Continue without hotel)":
        time.sleep(0.5)
        print("You decide that you are just betterer and do not need to heal, your wounds stay fresh\n")
      time.sleep(1)
      doSave = pyip.inputYesNo("Do you want to save?\n")
      if doSave == "yes":
        save(savePoint)
        savePointTwo()
      elif doSave == "no":
        print("Why?\n")
        time.sleep(0.5)
        savePointTwo()

def savePointTwo():
  print("You feel that your business in Potatoland is finished\n")
  time.sleep(1)
  print("You decide to start heading on the treacherous journey to the headquarters of the Mashed Potato Mafia\n")
  time.sleep(1)
  playAudio('PeggleJazz')
  print("As you exit the borders of Potatoland, you see that there is a dramatic change in climate, going from a forest straight into a large, hot, barren desert\n")
  time.sleep(3)
  print("As you walk further into the desert, about 800 feet away from the borders of Potatoland, you decide to turn around to see how far in you are, but you notice that Potatoland has completely vanished\n")
  time.sleep(1)
  print("While you are turned around, you suddenly you hear a voice coming from behind you\n")
  time.sleep(1)
  print("The speaker is a cloaked figure wearing a bright red cape and large leather gloves\n")
  time.sleep(1)
  print("The man also appears to be holding a bright silver scythe\n")
  time.sleep(1)
  print('"I, am MagusPotato, I wander these deserts looking for those who have crossed the line" - MagusPotato\n')
  time.sleep(1)
  print("You ask him what line he is talking about\n")
  time.sleep(1)
  print('"The line of the desert" - MagusPotato\n')
  time.sleep(0.5)
  print("MagusPotato waves his scythe around and mutters some strange words, suddenly a large black line appears on the ground, about 10 feet behind you\n")
  time.sleep(1.5)
  print('"You have crossed the line of the desert, and now you must pay the price" - MagusPotato\n')
  time.sleep(1)
  print("You ask MagusPotato what the price is\n")
  time.sleep(1)
  print('"The price is 12 dollars" - MagusPotato\n')
  time.sleep(1)
  print("?\n")
  time.sleep(0.5)
  print("You ask MagusPotato what he means by 12 dollars\n")
  time.sleep(1)
  print("You suddenly feel your wallet fly out of your pocket and see it fly directly into MagusPotato's hand\n")
  time.sleep(1)
  print("He opens your wallet and takes $12\n")
  player["money"] -= 12
  time.sleep(1)
  print("He closes your wallet and then violently throws it at your face")
  time.sleep(1)
  print('"Ah, I see that you do not have a pair of these nice desert goggles" - MagusPotato\n')
  time.sleep(0.5)
  print("He pulls out a pair of odd looking goggles from his cloak and waves them in front of your face\n")
  time.sleep(1)
  print("You ask him what they are for\n")
  time.sleep(1)
  print('"They are goggles. for your eyes" - MagusPotato\n')
  time.sleep(1)
  print("You sense a magical presence coming from the goggles\n")
  time.sleep(1)
  print("You ask MagusPotato if you can have them\n")
  time.sleep(1)
  print('"They are yours" - MagusPotato\n')
  time.sleep(0.5)
  print('"You paid $12 for them" - MagusPotato\n')
  time.sleep(1)
  print("He hands you the goggles and you put them on\n")
  time.sleep(1)
  print('"They are CHRONOGoggles, when you press the button labeled TRIGGER on the side they will allow you to see the past of the desert" - MagusPotato\n')
  time.sleep(1.5)
  print("You press the button on the side and can suddenly, the world around you changes into a beautiful field full of flowers\n")
  time.sleep(1)
  print("Beneath you, you see a clearing from the flowers that looks like a path\n")
  time.sleep(1)
  print('"Follow this path to the end of the desert, you will be safe as long as you keep the goggles activated and stay on the path" - MagusPotato\n')
  time.sleep(1)
  print("Before you can thank MagusPotato, he says 'It seems that my work here is done' and suddenly vanishes, leaving you alone in the field\n")
  time.sleep(1)
  print("After walking down the path for a few miles, you wonder what happens when you turn off the goggles\n")
  time.sleep(1)
  print("You turn off the goggles and suddenly the field turns back into a barren desert\n")
  time.sleep(0.5)
  print("Suddenly, you hear a loud noise from above you\n")
  time.sleep(1)
  print("Its a desert potato, and it looks very mean\n")
  time.sleep(1)
  print("You ask the desert potato why he is so mean\n")
  time.sleep(1)
  print('"Because you turned off the goggles" - Desert Potato\n')
  time.sleep(1)
  print('"I HATE rule breakers" - Desert Potato\n')
  time.sleep(1)
  print("You ask the desert potato what he wants\n")
  time.sleep(1)
  print('"I want you to die" - Desert Potato\n')
  time.sleep(1)
  print("The potato pulls out a poorly made knife\n")
  time.sleep(1)
  print("NOW WE BATTLE!\n")
  time.sleep(1)
  battleDesertPotato(battleSet)
  player["money"] += 10
  player["crimes"] += 1
  time.sleep(1)
  print("You have now defeated the attacking desert potato\n")
  time.sleep(1)
  print("You try to turn the goggles back on and continue walking down the line of the field, but they do not turn on\n")
  time.sleep(1)
  print("You are now lost in the desert\n")
  time.sleep(1)
  print("You continue to walk in the desert in the same direction that the path was going\n")
  time.sleep(2)
  print("Throughout the barren desert you see many frightening sights\n")
  time.sleep(1)
  print("You see a bird fly into a cactus and get stuck\n")
  time.sleep(1)
  print("A large scorpion shoots out of the sand and pulls the bird down back into the sand\n")
  time.sleep(0.5)
  print("You infer that the bird will not last for long\n")
  time.sleep(1)
  print("As you continue to walk in the desert, you eventually find a path\n")
  time.sleep(1)
  print("You walk down the path for miles and miles\n")
  time.sleep(1)
  print("But eventually, you see something new, a large stone blocking the way\n")
  time.sleep(1)
  print("You see that it completely covers the path\n")
  time.sleep(1)
  print("You decide to leave off of the path and try to walk around the stone\n")
  time.sleep(1)
  print("As soon as you exit the path, you look around to see if there are any more dangerous potatoes around you, but you seem safe, for now\n")
  time.sleep(1)
  print("You walk past the stone, but then the stone vanishes\n")
  time.sleep(1)
  print("In it's place is a large potato covered in marshmallows\n")
  time.sleep(1)
  print("You ask the potato why he is covered in marshmallows\n")
  time.sleep(1)
  print('"Because I am a dessert potato" - Dessert Potato\n')
  time.sleep(1)
  print('"Do you like desserts?" - Dessert Potato\n')
  time.sleep(1)
  prompt = pyip.inputYesNo("Do you like desserts?\n")
  if prompt == "yes":
    time.sleep(1)
    print('"I do not believe you" - Dessert Potato\n')
    time.sleep(0.5)
    print("Now we battle\n")
    time.sleep(1)
    battleDessertPotato(battleSet)
  elif prompt == "no":
    time.sleep(0.5)
    print('"I hate you" - Dessert Potato\n')
    time.sleep(0.5)
    print("Now we battle\n")
    time.sleep(1)
    battleDessertPotato(battleSet)
  player["money"] += 10
  player["crimes"] += 1
  time.sleep(1.5)
  print("Now that you have defeated the dessert potato, you continue walking down the path\n")
  time.sleep(1)
  print("After an extremely long time, you finally see something at the end of the path\n")
  time.sleep(1)
  print("it appears to be a large sandstone wall\n")
  time.sleep(0.5)
  print("You approach the wall and see that it has a large door in the middle of it, and the door is open\n")
  time.sleep(0.5)
  print("It might have water inside\n")
  time.sleep(1)
  prompt = pyip.inputYesNo("Enter the door?\n")
  if prompt == "no":
    print("You decide to not enter the door\n")
    time.sleep(1)
    print("What do you plan to do, NOT enter the door?\n")
    time.sleep(0.5)
    print("You are so consumed by thirst that you decide to enter the door\n")
  elif prompt == "yes":
    print("You decide to enter the door\n")
    time.sleep(1)
    print("Probably a good idea\n")
  time.sleep(2)
  print("As you walk through the door, you see that it was not just a wall, but a barrier that holds an entire town\n")
  time.sleep(1)
  print("The town is pretty small, and all of the buildings are carved from sandstone\n")
  time.sleep(1)
  print("Once you have walked in, you see a sign on the ground near you\n")
  time.sleep(0.5)
  print("The sign reads: 'Welcome to the OASIS'")
  time.sleep(1)
  print("In the center of the town you see a large casino\n")
  time.sleep(0.5)
  print("In front of the casino you see a large fountain filled with crystal clear water\n")
  time.sleep(1)
  print("You decide to go to the fountain and drink the water\n")
  time.sleep(2.5)
  print("You feel hydrated\n")
  time.sleep(1)
  doSave = pyip.inputYesNo("Do you want to save?\n")
  if doSave == "yes":
    save(savePoint)
    savePointThree()
  elif doSave == "no":
    print("Why?\n")
    time.sleep(0.5)
    savePointThree()

def savePointThree():
  time.sleep(1)
  print("Now that you are hydrated, you decide to go into the casino\n")
  time.sleep(1)
  print("When you look at the casino you see a large sign on the side of the building that reads 'LUIGI'S CASINO'\n")
  time.sleep(1)
  print("You walk up to the casino and head inside, the doors immediately slam shut behind you\n")
  time.sleep(0.5)
  print("The casino is full of game tables and people\n")
  time.sleep(1)
  print("Most of the people inside are mafia goons\n")
  time.sleep(0.5)
  print("As you enter, you follow a carpet on the floor that leads you to what appears to be the main desk of the establishment\n")
  time.sleep(1.5)
  print("You see a man sitting behind the desk, he looks like he is in his 50s, and he has a large mustache\n")
  background('luigi-explain.gif')
  time.sleep(0.75)
  print('"I am Luigi, welcome to my casino" - Luigi\n')
  time.sleep(0.5)
  print('"You seem like a potato with a lot of money" - Luigi\n')
  time.sleep(1)
  print("You ask Luigi if you can pass through his casino\n")
  time.sleep(1)
  print('"I am afraid that I cannot let you pass" - Luigi\n')
  time.sleep(2.5)
  print('"Without spending some money!" - Luigi\n')
  time.sleep(1)
  print("You ask Luigi how much you have to spend\n")
  time.sleep(1)
  print('"You have to beat me at 3 games" - Luigi\n')
  time.sleep(0.5)
  print('"But i warn you, i am a very good gambler"\n - Luigi\n')
  time.sleep(1.5)
  print("Luigi leads you to the gambling tables\n")
  time.sleep(0.5)
  print('"Let us begin!" - Luigi\n')
  time.sleep(0.5)
  letsGoGambling()
  time.sleep(1)
  print("You have {} money remaining\n".format(player.get("money")))
  time.sleep(1)
  print('"You have defeated me!" - Luigi\n')
  time.sleep(0.5) 
  print('"You may now pass through my casino" - Luigi\n')
  time.sleep(1)
  print("The doors of the casino open up\n")
  time.sleep(0.5)
  print("You walk through the exit doors of the casino and are now back in the center of the OASIS\n")
  time.sleep(1)
  print("As you walk around the town, you see a concert hall near the fountain\n")
  time.sleep(1)
  print("The concert hall is closed, but there is a sign on the side of the building that says 'JIMMY LIGHTNING CONCERT TONIGHT'\n")
  time.sleep(1)
  print("You decide that you should not go to the concert as you are more of a Kat Tut fan\n")
  time.sleep(1)
  print("But then you see a building on the other side of the road with a sign that says 'Kat Tut Stand-up Comedy and Trivia tonight'\n")
  time.sleep(0.5)
  print("The sign also says 'Free Entry'\n")
  time.sleep(1)
  print("You decide to go to the Kat Tut Stand-up Comedy and Trivia Night\n")
  time.sleep(5)
  print("It is now night and you head into the building\n")
  time.sleep(2)
  print("You see that the building is full of all the fans of Kat Tut\n")
  time.sleep(1.5)
  katTutEvent()
  print("You stay the night at a bench near the performance hall\n")
  time.sleep(5)
  print("You wake up the next morning and see that the sun is as hot as ever\n")
  time.sleep(1)
  print("You decide that your time in the OASIS if finished\n")
  time.sleep(1)
  print("You take one last drink from the fountain and then leave\n")
  time.sleep(1)
  doSave = pyip.inputYesNo("Do you want to save?\n")
  if doSave == "yes":
    save(savePoint)
    savePointFour()
  elif doSave == "no":
    print("Why?\n")
    time.sleep(0.5)
    savePointFour()
  time.sleep(2.5)

def savePointFour():
  print("After leaving the OASIS, you continue walking down the path\n")
  time.sleep(2)
  print("You eventually reach the end of the desert and see a huge mountain blocking your path\n")
  time.sleep(1.5)
  print("There is a cave tunnel leading through the mountain with a sign that says 'Welcome travelers'")
  time.sleep(1.5)
  prompt = pyip.inputMenu(["Trust Tunnel", "Climb Mountain"], numbered = True)
  if prompt == "Trust Tunnel":
    print("You trust the tunnel and travel through the mountain\n") 
    time.sleep(4)
  elif prompt == "Climb Mountain":
    print("You decide to not trust the EXTREMELY INVITING tunnel for some reason\n")
    time.sleep(1)
    print("This will take a while, but you wanted this\n")
    time.sleep(30)
  print("After passing the mountain range, you are now located at the edge of a gargantuan basin completely filled with water\n")
  time.sleep(1.5)
  print("In the center of the basin, atop the lake, you see a large island with a house located on it\n")
  time.sleep(1.5)
  print("Near you, you see a small rowboat\n")
  prompt = pyip.inputYesNo("Take the boat to the suspicious island?\n")
  if prompt == "yes":
    time.sleep(1)
    print("You decide to get in the boat and row to the island\n")
    time.sleep(3)
    print("You arrive on the island and tie the boat down\n")
    time.sleep(1.5)
    print("You walk up to the house and see that the door is wide open\n")
    prompt = pyip.inputYesNo("Enter the house?\n")
    if prompt == "yes":
      time.sleep(1.5)
      print("You walk into the house\n")
      time.sleep(1.5)
      print("There is no one inside\n")
      time.sleep(1.5)
      prompt = pyip.inputYesNo("Go further inside?\n")
      if prompt == "yes":
        time.sleep(1.5)
        print("After exploring for a while, you find a staircase leading down below the house\n")
        time.sleep(1.5)
        print("You quietly go down the stairs\n")
        time.sleep(1.5)
        prompt = pyip.inputYesNo("Enter the room?\n")
        if prompt == "yes":
          print("Once you enter the room, the staircase vanishes, leaving you trapped\n")
          time.sleep(1.5)
          print("Suddenly, you hear a voice coming from around the corner!\n")
          time.sleep(1.5)
          print('"You should not have come here!" - MagusPotato (Whispers into your ear magically)\n')
          time.sleep(1.5)
          print('"This was a trap" - MagusPotato (Still whispers into your ear magically)\n')
          time.sleep(1.5)
          print("You walk around the corner and see:\n")
          time.sleep(3.5)
          print("A three pound box of bees!\n")
          time.sleep(1)
          print("Wow shocking\n")
          time.sleep(1.5)
          print("The bees escape the box and take form into a potato with a name tag reading 'ErmalThaqui97'\n")
          time.sleep(1.5)
          print("You assume that this is the legendary ErmalThaqui97's bee ability\n")
          time.sleep(1.5)
          print("You feel compelled to fight\n")
          time.sleep(2.5)
          battleCURSEOFBEES(battleSet)
          time.sleep(1.5)
          print("Now that you have defeated the swarm of bees, you go further into the room\n")
          time.sleep(1.5)
          print("You see a large chest in the middle of the new branch of the room\n")
          time.sleep(1.5)
          prompt = pyip.inputYesNo("Open the chest?\n")
          if prompt == "yes":
            print("You open the chest\n")
            time.sleep(1.5)
            print("Inside, you find Ermal Thaqui 97\n")
            time.sleep(1.5)
            print('"You should download Surfnet VPN" - Ermal Thaqui 97\n')
            time.sleep(1.5)
            print("You want to fight him\n")
            time.sleep(1.5)
            battleErmalThaqui(battleSet)
            time.sleep(1.5)
            print("SCAMMER GET SCAMMED!!!\n")
            time.sleep(1.5)
            print("You have now defeated Ermal Thaqui 97\n")
            time.sleep(1.5)
            print("The exit reappears and you leave the house and get back in the boat\n")
            time.sleep(3)
            print("After you reach the other side of the lake, you tie the boat to a dock on the shore\n")
            time.sleep(1.5)
            print("As you continue walking away from the lake, you see a large swamp not too far ahead\n")
            time.sleep(1.5)
            print("You are going to the swamp.\n")
            time.sleep(4.5)
            print("You have now reached the entrance of the swamp\n")
            time.sleep(1.5)
            doSave = pyip.inputYesNo("Do you want to save?\n")
            if doSave == "yes":
              save(savePoint)
              savePointFive()
            elif doSave == "no":
              print("Why?\n")
              time.sleep(0.5)
              savePointFive()
          elif prompt == "no":
            print("Why\n")
            time.sleep(1.5)
            print("I will kill you just for being so stupid\n")
            time.sleep(1.5)
            print("Death - You were so stupid the narrator killed you\n")
            time.sleep(1.5)
            quit()
        elif prompt == "no":
          time.sleep(1.5)
          print("You decide to not enter the room\n")
          time.sleep(1.5)
          print("You chose to start this path, you must finish it\n")
          time.sleep(1.5)
          print("You try to leave, but as you do, you are surrounded by a swarm of bees\n")
          time.sleep(1.5)
          print("You die\n")
          time.sleep(1.5)
          quit()
      elif prompt == "no":
        time.sleep(1.5)
        print("You decide to not go further inside\n")
        time.sleep(1.5)
        print("You chose to start this path, you must finish it\n")
        time.sleep(1.5)
        print("You try to leave, but as you do, you are surrounded by a swarm of bees\n")
        time.sleep(1.5)
        print("You die\n")
        time.sleep(1.5)
        quit()
    elif prompt == "no":
      time.sleep(1.5)
      print("You decide to not enter the house\n")
      time.sleep(1.5)
      print("You chose to start this path, you must finish it\n")
      time.sleep(1.5)
      print("You try to leave, but as you do, you are surrounded by a swarm of bees\n")
      time.sleep(1.5)
      print("You die\n")
      time.sleep(1.5)
      quit()
  elif prompt == "no": 
    time.sleep(1.5)
    print("You have decided to leave the creepy island alone\n")
    time.sleep(1.5)
    print("You take the boat across the lake, avoiding the island\n")
    time.sleep(3)
    print("After you reach the other side of the lake, you tie the boat to a dock on the shore\n")
    time.sleep(1.5)
    print("As you continue walking away from the lake, you see a large swamp not too far ahead\n")
    time.sleep(1.5)
    print("You are going to the swamp.\n")
    time.sleep(4.5)
    print("You have now reached the entrance of the swamp\n")
    time.sleep(1.5)
    doSave = pyip.inputYesNo("Do you want to save?\n")
    if doSave == "yes":
      save(savePoint)
      savePointFive()
    elif doSave == "no":
      print("Why?\n")
      time.sleep(0.5)
      savePointFive()

def savePointFive():
  time.sleep(1.5)
  print("You see a sign that says 'Welcome to the SWAMP OF NIGHTMARES'\n")
  time.sleep(1.5)
  print("*You begin to feel spooky*\n")
  time.sleep(2)
  print("For the first time so far, you do not sense any immediate danger\n")
  time.sleep(1.5)
  print("You begin to walk through the swamp\n")
  time.sleep(2.5)
  print("After a while of traveling, you notice that the ground has become too liquid to stand on\n")
  time.sleep(1.5)
  print("But fortunately, you see a boat just a bit further ahead\n")
  time.sleep(1.5)
  print("You approach the boat\n")
  time.sleep(1)
  print("Printed on the side of the boat, you see that it is named 'The Crab Secret'\n")
  time.sleep(1.5)
  print("You are very confused\n")
  time.sleep(1.5)
  print("Regardless, you get in the boat and start rowing\n")
  time.sleep(2.5)
  print("You paddle for a few minutes but then,\n")
  time.sleep(1.5)
  print("You feel like you are going to have a bad time\n")
  time.sleep(2)
  print("As The Crab Secret goes further into the swamp, you are enveloped in shadow\n")
  lostWoods()
  print("After finally navigating through the swamp trap, you finally reach the end of the deep water area\n")
  time.sleep(1.5)
  print("You tie The Crab Secret to a dock and continue walking through the SWAMP OF NIGHTMARES\n")
  time.sleep(3.5)
  print("You finally see sunlight through a hole in the trees, this means you are at the end of the swamp\n")
  time.sleep(1.5)
  print("You rush towards the sunlight and are about to walk through the hole when you hear a horrifying screeching night noise\n")
  time.sleep(1.5)
  print("You are yet again enveloped in darkness, and lose sight of the exit\n")
  time.sleep(1.5)
  print("A huge swarm of birds drops down from above in front of you\n")
  time.sleep(1.5)
  battleSwarmBirb(battleSet)
  time.sleep(2)
  print("*You no longer feel spooky*\n")
  time.sleep(1.5)
  print("The darkness lifts and the exit of the swamp becomes visible again\n")
  time.sleep(1.5)
  print("You walk out of the swamp\n")
  time.sleep(1.5)
  doSave = pyip.inputYesNo("Do you want to save?\n")
  if doSave == "yes":
    save(savePoint)
    savePointSix()
  elif doSave == "no":
    print("Why?\n")
    time.sleep(0.5)
    savePointSix()

def savePointSix():
  savePointSeven()

def savePointSeven():
  print("You have now reached the end of ENTER POTATO ver: {}\n".format(ver))
  time.sleep(1.5)
  print("The full version will be released in like 300-500 business days\n")
  time.sleep(1.5)
  endcredits()

def endcredits():
  print("Thank You For Playing ENTER POTATO\n")
  time.sleep(2.5)
  print("Credits:\n")
  time.sleep(2)
  print("Maddox Mullen: Programming, Story, Character Lines, Testing, Debugging\n")
  time.sleep(1.5)
  print("Xavier Diaz: Testing, Story, Character Lines, Being poor, Sitting through the extremely long debugging process that I rigged against him\n")
  time.sleep(1.5)
  print("Silas Jones: Testing\n")
  time.sleep(1.5)
  print("Asher Zost: Testing, Some Character Lines\n")
  time.sleep(1.5)
  print("Leonard Udell: Testing, Some Story\n")
  time.sleep(1.5)
  print("Special thanks to Peggle Deluxe for being an epic game, butter, and with the number 3\n")
  time.sleep(5)
  os.system('clear')
  print("Ill take a potato chip...\n")
  time.sleep(1.5)
  print("AND EAT IT!\n")
  background('potatochip.gif')
  time.sleep(3)
  quit()

main()