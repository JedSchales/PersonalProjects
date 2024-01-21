#Open the file to grab data.
with open('coding_qual_input.txt', 'r') as message:
    unsorted = list(message)

#Initialize working variables for list sorting.
maxIndex = len(unsorted)
sorted = [0] * maxIndex

#Parse each line from the unsorted list.
for elem in unsorted:
    loc = ''        #Build an empty variable for numeric data.
    word = ''       #Build an empty variable for alphabetic data.
    for char in elem:
        if char.isalnum():
            if char.isnumeric():
                loc = loc + char
            if char.isalpha():
                word = word + char
        else:
            if char.isspace():  #Ignore the space between numeric and alphabetic characters.
                continue
            else:               #Skip to the next element once the "\" character is read (each elem ends in "\n" from the newline character.
                break
    sorted[int(loc)-1] = word   #Assign each word to its proper location in the final sorted array.

#Initialize working variables for message decoding.
secretMessage = []
lastPos = 0
increment = 1

#Grab only the relevant word from the end of each pyramid line.
while lastPos < maxIndex:
    target = lastPos+increment
    secretMessage.append(sorted[target-1])
    lastPos += increment
    increment += 1

#Present the secret message in the desired format.
decryptedMessage = ' '.join(secretMessage)
print(decryptedMessage)
        
