def get_data_list():
    with open('input.txt') as input_file:
        data = input_file.read()
        data_list = list(map(int, data.split(',')))
    return data_list


def set_inital_inputs(input1, input2):
    data_list = get_data_list()
    data_list[1] = input1
    data_list[2] = input2
    return data_list


def run_program(input1, input2):
    data_list = set_inital_inputs(input1, input2)
    current_position = 0

    while True:
        opcode = data_list[current_position]
        if opcode == 1:
            idx1 = data_list[current_position + 1]
            idx2 = data_list[current_position + 2]
            output_idx = data_list[current_position + 3]
            data_list[output_idx] = data_list[idx1] + data_list[idx2]
            current_position += 4
        elif opcode == 2:
            idx1 = data_list[current_position + 1]
            idx2 = data_list[current_position + 2]
            output_idx = data_list[current_position + 3]
            data_list[output_idx] = data_list[idx1] * data_list[idx2]
            current_position += 4
        elif opcode == 99:
            return data_list[0]
        else:
            raise ValueError('Invalid Opcode at index {}'.format(current_position))


print('Part One: {}'.format(run_program(12, 2)))

input1 = 0
input2 = 0

while True:
    output = run_program(input1, input2)
    if output == 19690720:
        break
    else:
        if input1 == 99 and input2 == 99:
            raise Exception('No inputs found that produce the desired result')
        if input1 < 99:
            input1 += 1
            continue
        input2 += 1
        input1 = input2

print('Part Two: {} x 100 + {} = {}'.format(
    input1,
    input2,
    input1 * 100 + input2
))
