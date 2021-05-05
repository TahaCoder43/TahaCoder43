class programmers:
    def __init__(self, name, skills, patience_level, programming_level, is_learnig_python):
        self.name=name
        self.skills=skills
        self.patience_level=patience_level
        self.programming_level=programming_level
        self.is_learning_python=is_learnig_python


    def is_honorable_programmer(self):
        if self.programming_level > 9000:
            return "honor_level_of_programmer is over 9000"

    def Future_programmer(self):
        if self.is_learning_python:
            return "\n\nrHey you,yeah you the man from the future"
Taha_The_Python_Executioner = programmers("Taha", "High", "Extremely_high", 14122, True)

print(Taha_The_Python_Executioner.skills)
print(Taha_The_Python_Executioner.is_honorable_programmer())
print(Taha_The_Python_Executioner.Future_programmer())