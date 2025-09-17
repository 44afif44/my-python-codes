class Student:
    def __init__(self,namee,markss):
        self.name=namee
        '''namee is a parameter and self.name is an instance variable(Instance variable = a “data slot” unique to each object.'''
        self.marks=markss
    def display(self):
        print(f"name={self.name},marks={self.marks}")
    def result(self):
        if self.marks>=35:
            print("pass")
        else:
            print("fail")
student1=Student("afif",67)
student2=Student("siam",66)
student1.display()
student1.result()
student2.display()
student2.result()
    

    
           

