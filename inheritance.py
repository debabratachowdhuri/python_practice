class Parent():
    def __init__(self, last_name, eye_color):
        print ("Parent class called")
        self.last_name = last_name
        self.eye_color = eye_color

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print ("Child class called")
        Parent.__init__(self,last_name,eye_color)
        self.number_of_toys = number_of_toys

miley_cirus = Child("Cyrus","Blue",50)
miley_cirus = Child("Cyrus","Blue",50)
print (miley_cirus.last_name)
print (miley_cirus.number_of_toys)

