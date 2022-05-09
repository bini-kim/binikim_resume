class Car:
     #class attribute
    wheels =4
    doors = 2
    engine = True
    
    def __init__(self, make, model, year=2023):
        self.make = make
        self.model = model
        self.year = year
        self.gas = 100
        self.is_moving = False
        
    def stop(self):
      if self.is_moving:
        print('The car has stopped')
        self.is_moving = False
      else:
        print('The car has already stopped')
        
    def go(self, speed):
        if self.use_fas():
          if not self.is_moving:
            print('The car starts moving')
            self.is_moving = True
          print(f'The car is going {speed}')
        else:
            print('You have run out of gas')
            self.stop()
        
    def use_fas(self):
        self.gas -= 50
        if self.gas <=0:
            return False
        else:
            return True
        
car_one = Car("Model T", 1908)
car_one.stop()
car_one.go('slow')
car_one.go('fast')
car_one.stop()
car_one.stop()
