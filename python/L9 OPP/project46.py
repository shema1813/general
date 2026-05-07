class Robot:

    def __init__(self, name, model):
        self.name = name
        self.model = model

    def introduce(self):
        print("Hello! My name is", self.name)
        print("My model is", self.model)

class SmartRobot(Robot):

    def __init__(self, name, model, work):
        
        super().__init__(name, model)
        self.work = work

    def show_work(self):
        print("I can", self.work)

robot1 = SmartRobot("Robot2", "RX-101", "clean the house")

robot1.introduce()
robot1.show_work()