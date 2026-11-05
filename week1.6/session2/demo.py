from image import Image

blank_image = Image.create(5, 6, 1, 20)
blank_image.write_pgm("test.pgm")