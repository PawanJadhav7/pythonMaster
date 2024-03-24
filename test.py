def char_indexing(input_string):
    even_str = []
    odd_str = []
    if 2 <= len(input_string) <= 10000:
        for s in range(len(input_string)):
            if s % 2 == 0:
                even_str.append(input_string[s])
            else:
                odd_str.append(input_string[s])
    even_str = list(map(str.strip, even_str))
    even_str.insert(len(even_str) + 1, ' ')
    odd_str = list(map(str.strip, odd_str))
    return even_str+odd_str



t = int(input("Enter the number of test cases:"))

if 1 <= t <= 10:
    for i in range(t):
        input_string = input("Enter the string:").strip('')
        output = char_indexing(input_string)
        out_str = ''
        print(out_str.join(output))
