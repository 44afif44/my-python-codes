class Student:
    def __init__(self,namee,roll_numberr,markss):
        self.name=namee
        self.roll_number=roll_numberr
        self.marks=markss
    def display(self):
        print(f"\n name :{self.name}")
        print(f"\n roll number :{self.roll_number}")
        for subject,mark in self.marks.items():
            print(f"\n {subject} :{mark}")
    def total(self):
        self.o= sum(self.marks.values())
        print(f"\n total marks :{self.o}")
    def percentage(self):
        p=self.o /len(self.marks)
        print(f"\n percentage :{p}")
        return p
    def grade(self):
        x=self.percentage()
        if x>=90:
            print("A+")
        elif x>=80:
            print("A")
        elif x>=70:
            print("B+")
        elif x>=60:
            print("B")
        elif x>=50:
            print("C")
        else:
            print("F")
s1=Student("afif",666,{"bangla":78,"english":89,"math":90})
s2=Student("siam",777,{"bangla":68,"english":79,"math":80})
s1.display()
s1.total()  
# s1.percentage()
s1.grade()
s2.display()
s2.total()  
# s2.percentage()
s2.grade()
        
        
              