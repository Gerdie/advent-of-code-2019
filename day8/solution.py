fewest_zero_digits = None
ones_times_twos = None
final_msg = None
layer = []
position = 0

with open('input.txt') as input_file:
    string_data = input_file.read()


def count_nums_in(layer, num):
    return sum([1 for row in layer for char in row if char == num])


def reconcile_layers(layer, final_layer):
    assert len(layer) == len(final_layer)
    for row_idx, row in enumerate(final_layer):
        assert len(row) == len(layer[row_idx])
        for char_idx, char in enumerate(row):
            if char == '2':
                row[char_idx] = layer[row_idx][char_idx]


def render_msg(final_msg):
    for row in final_msg:
        printable_row = [' ' if char == '0' else 'o' for char in row]
        print(''.join(printable_row))


while True:
    if position >= len(string_data):
        break
    layer_row = list(string_data[position:position + 25])
    layer.append(layer_row)
    position += 25
    if len(layer) == 6:
        zeroes = count_nums_in(layer, '0')
        if fewest_zero_digits is None or zeroes < fewest_zero_digits:
            ones_times_twos = count_nums_in(layer, '1') * count_nums_in(layer, '2')
            fewest_zero_digits = zeroes
        if final_msg is None:
            final_msg = layer
        else:
            reconcile_layers(layer, final_msg)
        layer = []

print('Part One: {}'.format(ones_times_twos))
print('Part Two:')
render_msg(final_msg)
