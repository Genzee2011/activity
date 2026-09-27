class Cricket:
    def __init__(self, player, score):
        self.__player = player      # private attribute
        self._score = score         # private attribute

    def info(self):                 # same method name as Football
        print(f"Cricket - Player: {self.__player}, Score: {self.score}")

    def play(self):                 # same method name, different output
        print(f"{self.__player} hits a six!")

    def get_score(self):            # getter - read private data
        return self.__score
    
    