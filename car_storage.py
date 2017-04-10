class Car_storage:
    """ This adds functionality and stores car list makes and models"""

    def __init__(self):
        self.car_makes = list()
        self.car_models = list()

    def read_car_makes(self):
        """ Reads car makes from car-makes.txt file """

        with open('car-makes.txt', 'r') as makes:
            for make in makes:
                self.car_makes.append(make[:-1])
        return self.car_makes

    def read_car_models(self):
        """ Reads car models from car-models.txt file """

        with open('car-models.txt', 'r') as models:
            for model in models:
                self.car_models.append(model[:-1])
        return self.car_models

    def create_car_dict(self):
        """ Combines the makes with models and stores them into a dictionary in model: make format"""

        car_dict = dict()
        demo.read_car_makes()
        demo.read_car_models()
        for make in self.car_makes:
            for model in self.car_models:
                if model[:1] == make[:1]:
                    car_dict[make] = model[2:]
        print(car_dict)


demo = Car_storage()
demo.create_car_dict()
# demo.read_car_makes()
# demo.read_car_models()
