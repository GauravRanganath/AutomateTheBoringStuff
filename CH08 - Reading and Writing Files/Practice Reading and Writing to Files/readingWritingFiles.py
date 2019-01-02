helloFile = open('hello.txt')
helloContent = helloFile.read()
print(helloContent)

lyrics = open('3005Lyrics.txt')
lyricContent = lyrics.readlines()
print(lyricContent)

baconFile = open('baconFile.txt','w')
baconFile.write('Hello World!\n')
baconFile.close()

baconFile = open('baconFile.txt','a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()

baconFile = open('baconFile.txt')
baconFileContent = baconFile.read()
baconFile.close()

print(baconFileContent)
