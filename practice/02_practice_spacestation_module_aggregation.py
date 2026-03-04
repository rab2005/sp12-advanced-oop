'''
OPTIONAL AI GUIDANCE PROMPT
---------------------------
I am a student in an introductory Python class. I am learning many coding
principles for the very first time. I am going to paste in the instructions
to a practice problem that my professor gave me to try before class.
Please be my kind tutor and walk me through how to solve the problem step
by step.

Don't just give me the full solution all at once (unless I later ask for
it). Instead, help me work through it gradually, with clear explanations
and small, easy-to-understand examples. Please use everyday language and
explain things in a simple, friendly way.

INSTRUCTIONS:
-------------
Practice aggregation, meaning independent objects are collected inside another.
1. Write a Module class with name and mass_kg.
2. Write a SpaceStation class that starts with an empty list of modules.
3. Add add_module(self, module) to append a Module to the list.
4. Implement total_mass(self) that loops (no list comprehensions) to
   sum and return total mass.
5. Create three Modules, add them, then print total_mass().
'''
class Module:
    def __init__(self, name, mass_kg):
        self.name = name
        self.mass_kg = mass_kg

class SpaceStation:
   def __init__(self):
        self.modules = []
   def add_module(self, module):
        self.modules.append(module)
   def total_mass(self):
        total = 0
        for module in self.modules:
            total += module.mass_kg
        return total
   
# Create modules
lab = Module("Laboratory", 12000)
habitat = Module("Habitat", 18000)
storage = Module("Storage", 8000)

# Create space station
station = SpaceStation()

# Add modules to station
station.add_module(lab)
station.add_module(habitat)
station.add_module(storage)

# Print total mass
print(station.total_mass())