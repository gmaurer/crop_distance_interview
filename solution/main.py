from math import radians, cos, sin, asin, sqrt

hardcoded_plant_locations = [
    (38.513253, -90.145310),
    (38.512092, -90.143185),
    (38.516561, -90.138432)
]
hardcoded_farm_locations = [
    (38.520671, -90.157317),
    (38.508210, -90.142351),
    (38.515713, -90.115004)
]


def haversine(input_one, input_two):# CREDIT: https://stackoverflow.com/questions/15736995/how-can-i-quickly-estimate-the-distance-between-two-latitude-longitude-points
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """

    lon1, lat1 = input_one[1], input_one[0]
    lon2, lat2 = input_two[1], input_two[0]
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    # Radius of earth in kilometers is 6371
    km = 6371* c
    return km


def calculate_distance_plant_to_farms(plant: tuple, farms: list[tuple]):
    """
    Loops through all farms given to find closest farm to provided plant
    """
    closest_distance = 0.0
    best_farm = None
    for farm in farms:
        km_distance = haversine(input_one=plant, input_two=farm)
        print(f'DISTANCE TO PLANT: {km_distance}KM, PLANT: {plant}, FARM: {farm}, AVAILABLE CROPS ON FARM:{farms[farm]}')
        if (km_distance < closest_distance or closest_distance == 0.0) and plant[2] in farms[farm]:
            closest_distance = km_distance
            best_farm = farm
            
    return(closest_distance, best_farm)

def read_in_file(file_location: str):
    info = []
    with open(file_location, 'r') as file:
        info = file.read().splitlines()
    info.pop(0)
    return info

def coalesce_farm_crops(farms: list[str]):
    farm_crops = {}
    for farm in farms:
        farm = farm.split()
        if (float(farm[0]), float(farm[1])) in farm_crops.keys():
            farm_crops[(float(farm[0]), float(farm[1]))].append(farm[2])
        else:
            farm_crops[(float(farm[0]), float(farm[1]))] = [farm[2]]
    return farm_crops


def main():
    farms = read_in_file('/Users/gkvrg/Documents/projects/crop_distance_interview/farms.txt')
    plants = read_in_file('/Users/gkvrg/Documents/projects/crop_distance_interview/plants.txt')
    new_farms = coalesce_farm_crops(farms=farms)
    new_plants = [(float(plant.split()[0]), float(plant.split()[1]), plant.split()[2]) for plant in plants]
    for plant in new_plants:
        distance_to_farm, closest_farm = calculate_distance_plant_to_farms(plant=plant, farms=new_farms)
        print(f'BEST FARM FOR PLANT: {plant}, DISTANCE TO FARM: {distance_to_farm}KM, CLOSEST FARM: {closest_farm}, CLOSEST FARMS CROPS: {new_farms[closest_farm]}')


if __name__ == "__main__":
    main()