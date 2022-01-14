import random

class People:
    """ Generate Names + Additional information of Fake People - For use with Test Data"""
    def __init__(self, fname="None", lname="None", vocation="None", age=0):
        self.fname = fname
        self.lname = lname
        self.vocation = vocation
        self.age = age
        
    def __str__(self):
        return "{} {}, {}, {}".format(self.first_name(), self.last_name(), self.vocation_list(), self.age_list())
    
    def first_name(self):
        lines = []
        with open("data/first_names.txt", "r") as r:
            lines = r.read().splitlines()
        random_line_num = random.randrange(0, len(lines))
        return lines[random_line_num]

    def last_name(self):
        lines = []
        with open("data/last_names.txt", "r") as r:
            lines = r.read().splitlines()
        random_line_num = random.randrange(0, len(lines))
        return lines[random_line_num]

    def vocation_list(self):
        lines = []
        with open("data/vocations.txt", "r") as r:
            lines = r.read().splitlines()
        random_line_num = random.randrange(0, len(lines))
        return lines[random_line_num]
    
    def age_list(self):
        r_age = random.randrange(12,75)
        age_string = str(r_age)
        return age_string
class School(People):
    pass
    
def main():
    p = People() 
    for i in range(10):
        print(p)
        
    print("\n--"+"School"+"--")
    s = School(p)
    c1 = School()
    
    print(s)
    print(c1)
    
if __name__ == "__main__":
    main()