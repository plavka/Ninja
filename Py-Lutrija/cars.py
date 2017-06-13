class Cars(object):
    def _init_(self, brand_name, model_name, km_done, service_date):
        self.brand_name = brand_name
        self.model_name = model_name
        self.km_done = km_done
        self.service_date = service_date

    def add_km(selfself, new_km):
        self.km_done = km_done + new_km

    def update_service_date(self, new_date):
        self.service_date = new_date



def list_all_vehicles(vehicles):
    if vehicles == []:
        print "There are no vehicles listed yet. Please add the first vehicle."
    else:
        for index, vehicle in enumerate(vehicles):
