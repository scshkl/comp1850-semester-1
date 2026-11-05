from image import Image

img = Image()
img.read_pgm("./images/feep.pgm")
print(f"dimension - height: {img.height}, width: {img.width}")
print(f"max gray: {img.max_value}")

img.write_pgm("from_pgm.pgm")