import os

for file in os.listdir('.'):
    if not file.endswith('.txt'):
        continue
    character=0
    word=0
    with open(file,'r') as f:
        for line in f:
            if len(line.split('\t')[0])==1:
                character+=1
            else:
                word+=1
    print('File: %s, character: %d, word: %d' % (file,character,word))
