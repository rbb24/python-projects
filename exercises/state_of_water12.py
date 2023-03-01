FREEZING_POINT = 0
BOILING_POINT = 100


def state_of_water(water_temperature):
    if water_temperature <= FREEZING_POINT:
        return "Solid"
    elif FREEZING_POINT < water_temperature < BOILING_POINT:
        return "Liquid"
    else:
        return "Gas"
