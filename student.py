# Add these methods to class student - full_name, year_of_birth, initials.
# Create two instances and verify the work as expected

class Student:
    school="Akirachix"
    def __init__(self,first_name,last_name,age,county):
      self.first_name=first_name
      self.last_name=last_name
      self.age=age
      self.county=county
    
    def greet(self):
        return f"Hello {self.first_name} welcome to {self.school} you are from {self.county}"
    
    def full_name(self):  
     return f"Hello {self.first_name} {self.last_name}"

    def year_of_birth(self):
      year_of_birth=2022-self.age
      return f"{year_of_birth}"
    
    def initials(self):
        x=f"{self.first_name[0]} {self.last_name[0]}"
        y=x.upper()
        return y

  
    

          

    
    

    
    
