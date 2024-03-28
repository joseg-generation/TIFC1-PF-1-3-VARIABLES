import subprocess

# Boilerplate function - include this in every test below!
def prepare_and_assert(input_array, output_array):
    # Prepare Variables
    input_string = '\n'.join(input_array)
    input_data = input_string.encode('utf-8')
    expected_output = '\n'.join(output_array)

    # Get Actual Output from Input Data
    output_data = subprocess.run(['python', 'main.py'], input=input_data, stdout=subprocess.PIPE)
    output_bytes = output_data.stdout.strip()
    output_string = output_bytes.decode("utf-8")

    # Test if Expected Output is found in Actual Output
    assert expected_output in output_string

# Test 1
def test_tomato():
    # Inputs
    input_array = [
        'tomato',
        'tomato',
        'tomato',
        'shopping_list'
    ]

    # Outputs
    output_array = [
        "['tomato', 'tomato', 'tomato']"
    ]    

    # Test if Input results in Output
    prepare_and_assert(input_array, output_array)

    # Test 2
def test_pizza():
    # Inputs
    input_array = [
        'Pizza',
        'Pasta',
        'Chips',
        'shopping_list'
    ]

    # Outputs
    output_array = [
        "['Pizza', 'Pasta', 'Chips']"
    ]    

    # Test if Input results in Output
    prepare_and_assert(input_array, output_array)