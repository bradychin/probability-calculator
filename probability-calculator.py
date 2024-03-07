import copy
import random
from collections import Counter

class Hat:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.contents = list()
        for key, value in kwargs.items():
            for _ in range(0, value):
                self.contents.append(key)

    def draw(self, number):
        # Copy contents_list
        list_to_remove = copy.copy(self.contents)
        drawn_balls = list()
        # Determine if balls to be drawn exceeds available quantity
        if number > len(list_to_remove):
            return list_to_remove
        # Pick ball from contents
        for _ in range(0, number):
            removed_element = random.choice(list_to_remove)
            list_to_remove.remove(removed_element)
            drawn_balls.append(removed_element)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    satisfied = 0
    for _ in range(0, num_experiments):
        # Draw balls and place into a list
        ball_drawn = hat.draw(num_balls_drawn)
        # Convert expected_balls into same format as ball_drawn
        target_balls = list()
        for key, value in expected_balls.items():
            for _ in range(0, value):
                target_balls.append(key)
        # Determine if expected_balls are in the drawn_balls
        if not Counter(target_balls) - Counter(ball_drawn):
            satisfied += 1
        ball_drawn.clear()
    # Calculate probability
    probability = round(satisfied/num_experiments, 3)
    return probability

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                         expected_balls={"red":2,"green":1},
                         num_balls_drawn=5,
                         num_experiments=2000)

print(probability)