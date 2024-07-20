decimal_value = int(input("Enter any integer value:"))

# creating a function

def decimal_to_hexa(num):

    conversion_table = {
        0: '0', 1: '1', 2: '2', 3: '3',
        4: '4', 5: '5', 6: '6', 7: '7',
        8: '8', 9: '9', 10: 'A', 11: 'B',
        12: 'C', 13: 'D', 14: 'E', 15: 'F'
    }

    hexa_value = ""

    #for iteration``
    while num > 0:
        remainder = num % 16
        hexa_value = hexa_value + conversion_table[remainder]
        
        num = num // 16

    # return hexa_value
    return hexa_value[::-1]

output = decimal_to_hexa(decimal_value)
print('Hexa value:', output)