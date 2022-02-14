
import csv
import os


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.car_type = None
        # self.photo_file_name = photo_file_name
        self.photo_file_name = self.check_photo(photo_file_name)
        self.brand = self.check_brand(brand)
        self.carrying = float(self.check_brand(carrying))

    def __str__(self):
        return (f'{0} {1} {2} {3}'.format(self.photo_file_name ,self.car_type, self.brand, self.carrying))

    def get_photo_file_ext(self):
        _, x = os.path.splitext(self.photo_file_name)
        # print("TEST: " + x)
        return x

    def check_brand(self, value):
        if value == '':
            raise ValueError
        return value

    def check_photo(self, name):
        for x in ('.jpg', '.png', '.gif', '.jpeg'):
            if name.endswith(x):
                return name
        raise ValueError



class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'car'
        self.carrying = float(carrying)
        self.passenger_seats_count = int(self.check_brand(passenger_seats_count))


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'truck'
        self.carrying = float(carrying)
        self.body_length, self.body_width, self.body_height = self.read_whl(body_whl)

    def read_whl(self, body_whl):
        try:
            length, width, height = (float(c) for c in body_whl.split("x", 2))
        except Exception:
            length, width, height = 0.0, 0.0, 0.0
        return length, width, height

        # if body_whl == "":
        #     self.body_length = self.body_width = self.body_height = 0.0
        # else: 
        #     whl = body_whl.split('x')
        #     self.body_length = float(whl[0])
        #     self.body_width = float(whl[1])
        #     self.body_height = float(whl[2])

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height

        

class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super(SpecMachine, self).__init__(brand, photo_file_name, carrying)
        self.car_type = 'spec_machine'
        self.extra = self.check_brand(extra)
        self.carrying = float(carrying)



def get_car_list(csv_filename):
    car_list = []
    # try:
        # print("TRY")
    with open(csv_filename, encoding = 'utf-8') as f:
        reader = csv.reader(f, delimiter= ';')
        # print("FILE")
        next(reader)
        for line in reader:
            vechicle = None 
            try:
                if len(line) == 7:
                    car_type = line[0]
                    brand = line[1] #
                    passenger_seats_count = line[2] #
                    photo_file_name = line[3]   #
                    body_whl = line[4]
                    carrying = line[5] #
                    extra = line[6] #

                    if car_type == 'car':                    
                        vechicle = Car(brand, photo_file_name, carrying, passenger_seats_count)
                    elif car_type == 'truck':                
                        vechicle = Truck(brand, photo_file_name, carrying, body_whl)
                    elif car_type == 'spec_machine':                    
                        vechicle = SpecMachine(brand, photo_file_name, carrying, extra)
            except Exception:
                pass
            if vechicle:
                car_list.append(vechicle)

    # except Exception:
    #     pass
    return car_list

if __name__ == "__main__":
    # csv_file = os.path('cars.csv')
    cars = get_car_list('cars.csv')
    print(cars)
    for car in cars:
        print(car)

# car = Car('Bugatti Veyron', 'bugatti.png', '0.312', '2')
# print(car.car_type, car.brand, car.photo_file_name, car.carrying,car.passenger_seats_count, sep='\n')

# truck = Truck('Nissan', 'nissan.jpeg', '1.5', '3.92x2.09x1.87')
# print(truck.car_type, truck.brand, truck.photo_file_name, truck.body_length,truck.body_width, truck.body_height, sep='\n')

# spec_machine = SpecMachine('Komatsu-D355', 'd355.jpg', '93', 'pipelayer specs')
# print(spec_machine.car_type, spec_machine.brand, spec_machine.carrying,spec_machine.photo_file_name, spec_machine.extra, sep='\n')

# spec_machine.get_photo_file_ext()

# cars = get_car_list('cars.csv')
# print(cars)

# len(cars)

# for car in cars:
#     print(type(car))

# print(cars[0].passenger_seats_count)

# print(cars[1].get_body_volume())
# print(len(get_car_list('cars.csv')))