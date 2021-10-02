prg = "The concept behind gamification is not new, but certainly the advent of the word has been difficult. The term “gamification” was “coined in 2002 by British consultant Nick Pelling, as a “deliberately ugly word” to describe “apply gamelike accelerated user interface design to make electronic transactions both enjoyable and fast” . This element of gamification can be considered from two different points of view. On the one hand, we have the non-game context, which refers to the many fields where gamification can be applied. On the other hand, the context refers also to the gaming environment where the player is immersed and can fulfil game requirements. As we are going to see in the next chapters, game elements, design and context represent the three main elements characterizing all the gamified experiences."
word_list = ['gamification', 'game', 'gamified', 'gaming'] 

print("the word gamification has been repeated", prg.count("gamification"),  "times.")
print("the word game has been repeated", prg.count("game"),  "times.")
print("the word gamified has been repeated", prg.count("gamified"),  "times.")
print("the word gaming has been repeated",prg.count("gaming") ,  "times.")

count = prg.count("gamification")+ prg.count("game")+ prg.count("gamified")+ prg.count("gaming")

print("overall the words in the list have been repeated",count ,"times.")

wordlist = prg.split()
lenlist = len(wordlist)

print("the strength index is {}/{}".format(count,lenlist))
