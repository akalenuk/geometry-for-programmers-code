from math import inf
import numpy as np

image = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0],
         [1, 1, 0, 0, 0, 0, 1, 0],
         [1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1]]


def dilate(img, depth):
    # 1. initializing the distance map with infinite values
    distances = [[inf for _ in row] for row in img]

    # 2. doing the first travel: left to right, top to bottom
    for i in range(len(img)):
        for j in range(len(img[0])):
            if img[i][j] == 1:
                distances[i][j] = 0
                continue
            if j > 0 and img[i][j-1] == 1:
                distances[i][j] = 1
            if i > 0 and img[i-1][j] == 1:
                distances[i][j] = 1
            candidates = [distances[i][j]]
            if j > 0:
                candidates += [distances[i][j-1] + 1]
            if i > 0:
                candidates += [distances[i-1][j] + 1]
            distances[i][j] = min(candidates)

    # 3. doing the reverse travel: right to left, bottom to top
    for i in reversed(range(len(img))):
        for j in reversed(range(len(img[0]))):
            if img[i][j] == 1:
                distances[i][j] = 0
                continue
            if j < len(img[0]) - 1 and img[i][j+1] == 1:
                distances[i][j] = 1
            if i < len(img) - 1 and img[i+1][j] == 1:
                distances[i][j] = 1
            candidates = [distances[i][j]]
            if j > 0:
                candidates += [distances[i][j-1] + 1]
            if i > 0:
                candidates += [distances[i-1][j] + 1]
            if j < len(img[0]) - 1:
                candidates += [distances[i][j+1] + 1]
            if i < len(img) - 1:
                candidates += [distances[i+1][j] + 1]
            distances[i][j] = min(candidates)

    # marking all the voxels with a distance lower or equal to the depth value
    for i in range(len(img)):
        for j in range(len(img[0])):
            if distances[i][j] <= depth:
                img[i][j] = 1
    return img


# a simple rule: every one becomes a zero, and every zero – a one
def invert(img):
    for i in range(len(img)):
        for j in range(len(img[0])):
            img[i][j] = 1 - img[i][j]
    return img

# erosion is then just an inverted dilation of an inverted image
def erode(img, depth):
    return invert(dilate(invert(img), depth))

# denoise is now jut an erode-dilate workflow
def denoise(img, noise_size):
    return dilate(erode(img, noise_size), noise_size)

# a pretty-print
def pprint(img):
    for row in img:
        print(row)

print("  image before:")
pprint(image)
print("")
print("  image after denoising:")
pprint(denoise(image, 1))
