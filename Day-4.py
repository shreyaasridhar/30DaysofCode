class Person:    
 		def __init__(self,initial_Age):
 		    self.initial_Age = initial_Age # Add some more code to run some checks on initial_Age
 		def amIOld(self):
 		    if self.initial_Age < 0:
 		        print "This person is not valid, setting age to 0." 
 		        self.initial_Age = 0
 		    if self.initial_Age<13 :
 		        print "You are young."
 		    elif self.initial_Age>=13 and self.initial_Age<18:
 		        print "You are a teenager."
 		    else :
 		        print "You are old."    # Do some computations in here and print out the correct statement to the console 
 		def yearPasses(self):
 		    self.initial_Age+=1
T=int(raw_input())
for i in range(0,T):
    age=int(raw_input())         
    p=Person(age)  
    p.amIOld()
    for j in range(0,3):
        p.yearPasses();        
    p.amIOld();
    print ""