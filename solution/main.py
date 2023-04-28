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

def haversine(plant, farm):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """

    lon1, lat1 = plant[0], plant[1]
    lon2, lat2 = farm[0], farm[1]
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


def calculate_distance(plant: tuple, farms: list[tuple]):
    """
    Loops through all farms given to find closest farm to provided plant
    """
    closest_distance = 0.0
    best_farm = None
    for farm in farms:
        km_distance = haversine(plant=plant, farm=farm)
        print(f'DISTANCE TO PLANT: {km_distance}, PLANT: {plant}, FARM: {farm}')
        if km_distance < closest_distance or closest_distance == 0.0:
            closest_distance = km_distance
            best_farm = farm
            
    return(closest_distance, best_farm)

def main():

    for plant in hardcoded_plant_locations:
        distance_to_farm, closest_farm = calculate_distance(plant=plant, farms=hardcoded_farm_locations)
        print(f'BEST FARM FOR PLANT: {plant}, DISTANCE TO FARM: {distance_to_farm}, CLOSEST FARM: {closest_farm}')



if __name__ == "__main__":
    main()