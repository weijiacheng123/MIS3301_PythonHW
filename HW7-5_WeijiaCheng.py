prg = "The concept behind gamification is not new, but certainly the advent of the word has been difficult. The term “gamification” was “coined in 2002 by British consultant Nick Pelling, as a “deliberately ugly word” to describe “apply gamelike accelerated user interface design to make electronic transactions both enjoyable and fast” . This element of gamification can be considered from two different points of view. On the one hand, we have the non-game context, which refers to the many fields where gamification can be applied. On the other hand, the context refers also to the gaming environment where the player is immersed and can fulfil game requirements. As we are going to see in the next chapters, game elements, design and context represent the three main elements characterizing all the gamified experiences."
prg = prg.lower()
special_charac = ['“' ,'”' , ',' , '.' , '-' ]
new_list = []
word_list = prg.split()
for word in word_list:
    for c in special_charac:
        if c in word:
            word = word.strip(c)
    new_list.append(word)
final = [['word','count']]
for word in new_list:
    l = []
    l.append(word)
    l.append(new_list.count(word))
    final.append(l)

print(final)
