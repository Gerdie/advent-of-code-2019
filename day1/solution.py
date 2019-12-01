def get_fuel_for_module(module_number):
    return module_number // 3 - 2


# PART ONE
with open('input.txt') as input_file:
    total_fuel_required = 0
    for line in input_file:
        module_num = int(line)
        total_fuel_required += get_fuel_for_module(module_num)
    print("Part One: {}".format(total_fuel_required))

# PART TWO
with open('input.txt') as input_file:
    total_fuel_required = 0
    for line in input_file:
        module_num = int(line)
        while True:
            fuel_required = get_fuel_for_module(module_num)
            if fuel_required <= 0:
                break
            total_fuel_required += fuel_required
            module_num = fuel_required

    print("Part Two: {}".format(total_fuel_required))
