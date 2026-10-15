# Week 1.3, Session 2: Print PGM image info

# Open a pgm image file
# You can use the relative path ../images/filename
# You could handle file errors with try/except.

# Read the file content

# print image dimension (i.e., Dimensions: width x height pixels)

# print max gray value (i.e., Max Gray Value: max_gray_value)
with open("../images/with_comment.pgm", "r") as f:
    data = f.readlines()

    data = [line.strip().split() for line in data]
    if data[1][0] == "#":
        print(f"dimension: {data[2][0]} x {data[2][1]}")
        print(f"max gray: {data[3][0]}")
    else:
        print(f"dimension: {data[1][0]} x {data[1][1]}")
        print(f"max gray: {data[2][0]}")
    # print(data)