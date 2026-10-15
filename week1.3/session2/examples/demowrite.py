
with open("demo_output.txt", 'w') as f:
    int_val = 55
    str_message = "How are you?"
    f.write("hello world\n")
    # f.write(str_message)
    f.write(str(int_val))
