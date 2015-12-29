from time import sleep

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            sleep(1)
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pickets full of shells"])

#happy_bday.sing_me_a_song()

#bulls_on_parade.sing_me_a_song()

or_text = ["I twist the truth",
                    "I rule the world",
                    "my crown is called deceit"]

orgasmatron = Song(or_text)

orgasmatron.sing_me_a_song()
