import chunk_string


#TODO (confessin): Write proper unit test cases for this.

RAW_TEXT = """
Batman is a fictional character, a comic book superhero created by artist Bob Kane and writer Bill Finger. The character first appeared in Detective Comics #27 (May 1939), and since then has appeared primarily in publications by DC Comics. Originally referred to as "The Bat-Man" and still referred to at times as "The Batman", he is additionally known as "The Caped Crusader",[2] "The Dark Knight",[2] and "The World's Greatest Detective,"[2] among other titles.
In the original version of the story and the vast majority of retellings, Batman's secret identity is Bruce Wayne, an American millionaire (later billionaire) playboy, industrialist, and philanthropist. Having witnessed the murder of his parents as a child, he swore revenge on criminals, an oath tempered with the greater ideal of justice. Wayne trains himself both physically and intellectually and dons a bat-themed costume in order to fight crime.[3] Batman operates in the fictional American Gotham City, assisted by various supporting characters including his crime-fighting partner, Robin, his butler Alfred Pennyworth, the police commissioner Jim Gordon, and occasionally the heroine Batgirl. He fights an assortment of villains such as the Joker, the Penguin, the Riddler, Two-Face, Ra's al Ghul, Scarecrow, Poison Ivy, and Catwoman, among others. Unlike most superheroes, he does not possess any superpowers; he makes use of intellect, detective skills, science and technology, wealth, physical prowess, martial arts skills, an indomitable will, fear, and intimidation in his continuous war on crime.
Batman became a very popular character soon after his introduction and gained his own comic book title, Batman, in 1940. As the decades wore on, differing interpretations of the character emerged. The late 1960s Batman television series used a camp aesthetic which continued to be associated with the character for years after the show ended. Various creators worked to return the character to his dark roots, with varying results. The comic books of this dark stage culminated in the acclaimed 1986 miniseries The Dark Knight Returns, by Frank Miller, as well as Batman: The Killing Joke by Alan Moore and Arkham Asylum: A Serious House on Serious Earth, among others. The overall success of Warner Bros.' live-action Batman feature films have also helped maintain public interest in the character.[4]
A cultural icon, Batman has been licensed and adapted into a variety of media, from radio to television and film, and appears on a variety of merchandise sold all over the world such as toys and video games. The character has also intrigued psychiatrists with many trying to understand the character's psyche and his true ego in society. In May 2011, Batman placed second on IGN's Top 100 Comic Book Heroes of All Time, after Superman. Empire magazine also listed him second in their 50 Greatest Comic Book Characters of All Time.[5]"""

barx = "http://en.wikipedia.org/wiki/alexander%20the%20great"

if __name__ == '__main__':
  ins = chunk_string.CreateChunks()
  xxx = ins.start_chunks(RAW_TEXT,
                         keyword='bat man super robin batman')[0]
  print "number of keywords::%s" % len(xxx)
  print xxx
