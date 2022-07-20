class Lion:
    def give_food(self):
        print("Feeding a lion with raw meat!")

class Panda:
    def feed_animal(self):
        print("Feeding a panda with some tasty bamboo!")        

class Snake:
    def feed_snake(self):
        print("Feeding a snake with mice!")    

# Animals of our zoo:
leo = Lion() 
po = Panda() 
sam = Snake() 
# Our job is to feed all the animals using a Python script. One way to do that 

leo.give_food()
po.feed_animal()
sam.feed_snake()

# This would work. But imagine how much time would it take to do this 
# for each animal in a large zoo, repeating the same process 
# and code hundreds of times. 
# That would also make the code harder to maintain.






























