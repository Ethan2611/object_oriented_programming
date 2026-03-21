


class Footabll_pitch():
    goals=2
    pitch=1
    players=22
    refree=1
    def score(self):
        print("A goal has been scored")

stadium=Footabll_pitch()
print(stadium.pitch)
striker=Footabll_pitch()
striker.score()



class Basketball_court():
    nets=2
    court=1
    players=10
    refree=1
    def three_pointer(self):
        print("He's just scored a three pointer")

stadium2=Basketball_court()
print(stadium2.court)
shooting_guard=Basketball_court()
shooting_guard.three_pointer()

