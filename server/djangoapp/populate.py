from .models import CarMake, CarModel

def initiate():
    car_make_data = [
        {"name":"NISSAN", "description":"Great cars. Japanese technology", "num": 1},
        {"name":"Mercedes", "description":"Great cars. German technology", "num": 2},
        {"name":"Audi", "description":"Great cars. German technology", "num": 3},
        {"name":"Kia", "description":"Great cars. Korean technology", "num": 4},
        {"name":"Toyota", "description":"Great cars. Japanese technology", "num": 5},
    ]
    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(CarMake.objects.create(name=data['name'], description=data['description'], num = data['num']))
    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
      {"name":"Pathfinder", "type":"SUV", "year": 2023, "car_make":car_make_instances[0], "color":"red"},
      {"name":"Qashqai", "type":"SUV", "year": 2023, "car_make":car_make_instances[0], "color":"black"},
      {"name":"XTRAIL", "type":"SUV", "year": 2023, "car_make":car_make_instances[0], "color":"white"},
      {"name":"A-Class", "type":"SUV", "year": 2023, "car_make":car_make_instances[1], "color": "blue"},
      {"name":"C-Class", "type":"SUV", "year": 2023, "car_make":car_make_instances[1], "color":"red"},
      {"name":"E-Class", "type":"SUV", "year": 2023, "car_make":car_make_instances[1], "color":"black"},
      {"name":"A4", "type":"SUV", "year": 2023, "car_make":car_make_instances[2], "color":"white"},
      {"name":"A5", "type":"SUV", "year": 2023, "car_make":car_make_instances[2],"color": "blue"},
      {"name":"A6", "type":"SUV", "year": 2023, "car_make":car_make_instances[2], "color":"red"},
      {"name":"Sorrento", "type":"SUV", "year": 2023, "car_make":car_make_instances[3], "color":"black"},
      {"name":"Carnival", "type":"SUV", "year": 2023, "car_make":car_make_instances[3], "color":"white"},
      {"name":"Cerato", "type":"Sedan", "year": 2023, "car_make":car_make_instances[3], "color": "blue"},
      {"name":"Corolla", "type":"Sedan", "year": 2023, "car_make":car_make_instances[4], "color":"red"},
      {"name":"Camry", "type":"Sedan", "year": 2023, "car_make":car_make_instances[4], "color":"black"},
      {"name":"Kluger", "type":"SUV", "year": 2023, "car_make":car_make_instances[4], "color":"white"},
        # Add more CarModel instances as needed
    ]
    for data in car_model_data:
        CarModel.objects.create(name=data['name'], car_make=data['car_make'], type=data['type'], year=data['year'], color = data['color']) 
