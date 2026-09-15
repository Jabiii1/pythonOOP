class classmates:   
    def __init__ (self, name, course, section):
        self.name = name
        self.course = course
        self.section = section
        self.pumasok = False
        self.timePumasok = 0

    def PumasokKa(self):
        if self.pumasok:
            print(f"si {self.name} a nasa classrooom na")
        else:
            self.pumasok = True
            print(f"papasok na si {self.name}!")
    
    def wagPumasok(self):
        if self.pumasok:
            print(f"si {self.name} ay papunta na")
        else:
            self.pumasok = False
            print(f"hindi pumasok si {self.name}.")
    
    def orasPumasok(self, subjNum):
        if not self.pumasok:
            print(f"hindi pa si {self.name} pumapasok. Pasok muna")
        else:
            self.timePumasok += subjNum
            print(f"pumasok si {self.name} ng {self.timePumasok} at naka attend sya sa {subjNum} na subject")


stud1 = classmates('jv', 'bsit', '3a')


stud1.wagPumasok()
stud1.PumasokKa()
stud1.wagPumasok()
stud1.orasPumasok(7)

