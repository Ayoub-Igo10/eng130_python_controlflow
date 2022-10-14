from reptile import Reptile

class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.forked_tongue = True
    def use_tongue_to_smell(self):
        return "if I can touch it I can smell it as well"

# smart_snake = Snake()
# print(f" This function is called from parent class {smart_snake.hunt()}")
# print(f" This function is called from the current class {smart_snake.use_tongue_to_smell()}")
# print(f" This function is called from grandparent class {smart_snake.breathe()}")


