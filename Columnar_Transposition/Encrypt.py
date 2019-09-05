def encrypt(plaintext, key):
  matrix = createEncMatrix(len(key), plaintext)
  keywordSequence = getKeywordSequence(key)

  ciphertext = "";
  for num in range(len(keywordSequence)):
    pos = keywordSequence.index(num + 1)
    for row in range(len(matrix)):
      if len(matrix[row]) > pos:
        ciphertext += matrix[row][pos]
  return ciphertext


def createEncMatrix(width, plaintext):
  r = 0
  c = 0
  matrix = [[]]
  for pos, ch in enumerate(plaintext):
    matrix[r].append(ch)
    c += 1
    if c >= width:
      c = 0
      r += 1
      matrix.append([])

  return matrix


def getKeywordSequence(key):
  sequence = []
  for pos, ch in enumerate(key):
    previousLetters = key[:pos]
    newNumber = 1
    for previousPos, previousCh in enumerate(previousLetters):
      if previousCh > ch:
        sequence[previousPos] += 1
      else:
        newNumber += 1
    sequence.append(newNumber)
  return sequence
  

text = input("Plaintext : ")
key = input("Key : ")

ciphertext = encrypt(text, key)

print("Columnar Transposition : " + ciphertext)