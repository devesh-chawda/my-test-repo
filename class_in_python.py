class school:
    name = "KVS"
    def __init__(self,subject,marks):
        self.subject= subject
        self.marks = marks

    def display(self):
        print("Subject: ",self.subject)
        print("Marks: ",self.marks)
        print("School: ",school.name)

entry=school("Maths",90)
entry.display()