class WordleGame:
  with open("words.txt", "r") as wordlist:
    words = wordlist.read().split("\n")
  commonletters = ["e", "a", "r", "i", "o", "t", "n", "s", "l", "c"]
  positions = {}
  excluded = []
  positionsexclude =[]
  wrongposition = []
  wrongpositionexclude = []
  invalid = []
  frequencies = {
    "e": 0.127, "t": 0.091, "a": 0.082, "o": 0.075, "i": 0.07, "n": 0.067, "s": 0.063, "h": 0.061, "r": 0.06, "d": 0.043, "l": 0.04, "c": 0.028, "u": 0.028, "m": 0.024, "w": 0.024, "f":0.02, "g": 0.02, "y": 0.02, "p": 0.019, "b": 0.015, "v": 0.0098, "k": 0.0077, "j": 0.0015, "x": 0.0015, "q": 0.00095, "z": 0.00074
  }
  def value_word(self, word):
    value = 0
    for i in list(word):
      value += self.frequencies[i]
    return value
  def next_word(self, guess, result):
    if result.upper() == "CCCCC":
      print("You Won!")
      return
    if result.upper() == "INVALID":
      self.invalid.append(guess)
    guessl = list(guess)
    resultl = list(result.upper())
    for i, j, k in zip(guessl, resultl, range(5)):
      if j == "C":
        self.positions[k] = i
      elif j == "I":
        self.excluded.append(i)
      elif j == "Y":
        self.wrongposition.append([i, k])
    for i, j, k in zip(guessl, resultl, range(5)):
      if j == "I":
        self.excluded.append(i)
        if i in [p[0] for p in self.wrongposition]:
          self.positionsexclude.append([k, i])
    for i, j, k in zip(guessl, resultl, range(5)):
      if j == "I":
        self.excluded.append(i)
        if i in [self.positions[x] for x in self.positions.keys()]:
          self.positionsexclude.append([k, i])
    options = []
    for i in self.excluded:
      for j in self.positions.values():
        if i == j:
          self.excluded = [value for value in self.excluded if value != i]
    for i in self.words:
      a = False
      for j in self.excluded:
        if j in i:
          a = True
      if a:
        pass
      else:
        b = False
        for j, k in zip(list(i), range(5)):
          for l in self.wrongposition:
            if l[0] == j and l[1] == k:
              b = True
            if l[0] not in i:
               b = True
        if b:
          pass
        else:
          c = True
          for j in range(5):
            if (j not in self.positions) or (self.positions[j] == i[j]):
              pass
            else:
              c = False
          if c:
            passed_word_d = True
            for z, t in zip(list(i), range(5)):
              for y in self.positionsexclude:
                if z == y[1] and t == y[0]:
                  passed_word_d = False
            if passed_word_d:
              passed_word_e = True
              for z, t in zip(list(i), range(5)):
                for y in self.wrongpositionexclude:
                  if z == y[1] and t == y[0]:
                    passed_word_e = False
              if passed_word_e:
                options.append(i)
    best = []
    for i in options:
      best.append([self.value_word(i), i])
    sortedbest = sorted(best, key=lambda x: x[0])
    cleanbest = []
    for i in sortedbest:
      #if not(i[1] in self.invalid):
      cleanbest.append(i[1])
    return cleanbest
  def play(self):
    print("C = Green \nY = Yellow \nI = Gray")
    print("WORD: orate")
    next0 = self.next_word("orate", input("Result: "))
    if next0:
      print(f"Next word is {next0[0]}. {len(next0)} possiblites.")
    else:
      return
    next1 = self.next_word(next0[0], input("Result: "))
    if next1:
      print(f"Next word is {next1[0]}. {len(next1)} possiblites.")
    else:
      return
    next2 = self.next_word(next1[0], input("Result: "))
    if next2:
      print(f"Next word is {next2[0]}. {len(next2)} possiblites.")
    else:
      return
    next3 = self.next_word(next2[0], input("Result: "))
    if next3:
      print(f"Next word is {next3[0]}. {len(next3)} possiblites.")
    else:
      return
    next4 = self.next_word(next3[0], input("Result: "))
    if next4:
      print(f"Next word is {next4[0]}. {len(next4)} possiblites.")
game = WordleGame()
game.play()