# The Base class named Vehicle
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_vehicle_info(self):
        print(f"\nThe Information of the Vehicle is: made year = {self.year}, brand =  {self.make}, model =  {self.model}")

# The Subclass named Car
class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    # Override the display_vehicle_info method
    def display_vehicle_info(self):
        print(f"\nThe Information of the Car is: made year = {self.year}, brand = {self.make}, model = {self.model} and Total Doors = {self.doors}")

# The Subclass named Truck
class Truck(Vehicle):
    def __init__(self, make, model, year, total_load_capacity):
        super().__init__(make, model, year)
        self.total_load_capacity = total_load_capacity

    # Override the display_vehicle_info method
    def display_vehicle_info(self):
        print(f"\nThe Information of the Truck is: made year = {self.year}, brand = {self.make}, model = {self.model} and Total load Capacity = {self.total_load_capacity} tons")

# assigning the last four digits of a student id s20230452 which is 0452 so we use 452 as we can ignore the zero in the front
student_id_last_four = 452

# Create objects of Car which uses the last four digits of student ID for the year
car1 = Car(make="Volkswagen", model="Polo", year=student_id_last_four, doors=4)
car2 = Car(make="Bugatti", model="Chiron", year=student_id_last_four, doors=2)

# Create objects of Truck which has its load capacity as the last four digits of student ID
truck = Truck(make="MAN", model="TGX", year=student_id_last_four, total_load_capacity=student_id_last_four)

# Display the information related to particular object of a class
car1.display_vehicle_info()
car2.display_vehicle_info()
truck.display_vehicle_info()
