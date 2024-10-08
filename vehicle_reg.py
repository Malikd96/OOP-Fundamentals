#Problem Statement: Create a Python class Vehicle with attributes 
# registration_number, type, and owner. Implement a method update_owner 
# to change the vehicle's owner. Then, create a few instances of Vehicle 
# and demonstrate changing the owner.

# - Code Example: Provide a basic structure for the Vehicle class without methods.

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

#- Expected Outcome: Completion of the Vehicle class with the update_owner method 
# and a demonstration script showing the creation of Vehicle objects and updating their owners.

    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"Owner of {self.registration_number} has been updated to {new_owner}.")

vehicle1 = Vehicle('123abc', 'truck', 'John')
print(f"Vehicle: {vehicle1.registration_number}, {vehicle1.type}, Owner: {vehicle1.owner}.")

vehicle1.update_owner('Bob')
print(f"Vehicle: {vehicle1.registration_number}, {vehicle1.type}, Owner: {vehicle1.owner}")