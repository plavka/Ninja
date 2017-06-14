class Vehicle:
    def __init__(self, brand_name, model_name, km_done, service_date):
        self.brand_name = brand_name
        self.model_name = model_name
        self.km_done = km_done
        self.service_date = service_date

    def get_full_name(self):
        return self.brand_name + " " + self.model_name

def list_all_vehicles(vehicles):
    for index, car in enumerate(vehicles):
        print "ID: " + str(index)
        print car.get_full_name()
        print car.km_done
        print car.service_date
        print "" #prints empty line

    if not vehicles:
        print "You don't have a vehicle in your vehicle list."

def add_new_vehicle(vehicles):
    brand_name = raw_input("Please enter a brand of a vehicle: ")
    model_name = raw_input("Please enter a model of a vehicle: ")
    km_done =  raw_input("Please enter number of km: ")
    service_date = raw_input("Please enter last service date: ")

    new = Vehicle(brand_name=brand_name, model_name=model_name, km_done=km_done, service_date=service_date)
    vehicles.append(new)

    print "" #prints empty line
    print new.get_full_name() + " was successfully added to your contact list."

def edit_vehicle(vehicles):
    print "Select the number of the vehicle you want to edit: "

    for index, car in enumerate(vehicles):
        print str(index) + ") " + car.get_full_name()

    print ""
    selected_id = raw_input("What vehicle would you like to edit? (enter ID number): ")
    selected_vehicle = vehicles[int(selected_id)]

    new_km = raw_input("Please enter a new km for %s: " % selected_vehicle.get_full_name())
    selected_vehicle.km = new_km
    print ""
    print "km updated."

    new_service_date = raw_input("Please enter new service date for %s: " % selected_vehicle.get_full_name())
    selected_vehicle.service_date = new_service_date

def delete_vehicle(vehicles):
    print "Select the number of the vehicle you want to delete: "

    for index, car in enumerate(vehicles):
        print str(index) + ") " + car.get_full_name()

    print ""
    selected_id = raw_input("What vehicle would you like to delete? (enter ID number): ")
    selected_vehicle = vehicles[int(selected_id)]

    vehicles.remove(selected_vehicle)
    print ""
    print "Vehicle was successfully removed from your list."

def main():
    print "Welcome to your Vehicle List"

    aygo = Vehicle(brand_name="Toyota", model_name="Aygo", km_done="8900", service_date="31.8.2016")
    punto = Vehicle(brand_name="Fiat", model_name="Punto", km_done="7800", service_date="31.6.2016")
    ibiza = Vehicle(brand_name="Seat", model_name="Ibiza", km_done="800", service_date="31.4.2016")
    civic = Vehicle(brand_name="Honda", model_name="Civic", km_done="5900", service_date="31.2.2016")
    vehicles = [aygo, punto, ibiza, civic]

    while True:
        print ""
        print "Please choose one of these options:"
        print "a) See all your vehicles"
        print "b) Add a new vehicle"
        print "c) Edit a vehicle to the list"
        print "d) Delete a vehicle from the list"
        print "e) Quit the program"
        print ""

        selection = raw_input("Enter your selection (a, b, c, d or e): ")
        print ""

        if selection.lower() == "a":
            list_all_vehicles(vehicles)
        elif selection.lower() == "b":
            add_new_vehicle(vehicles)
        elif selection.lower() == "c":
            edit_vehicle(vehicles)
        elif selection.lower() == "d":
            delete_vehicle(vehicles)
        elif selection.lower() == "e":
            print "Thank you for using Vehicle List. Goodbye!"
            break
        else:
            print "Sorry, I didn't understan your selection. Please try again."
            continue

if __name__ == "__main__":
    main()









