'''This is the duplicatefinder python file'''


from os import listdir
import re
import hashlib
from skimage.io import imread
import numpy as np

'''make_transforms is the transformation function'''


def make_transforms(img):

    # change hash libs to just standard hash
    transform_list = []

    transform_list.append(hashlib.sha256(bytes(img)).hexdigest())

    turn_0_mirror = img[::1, ::-1]
    turn_0_mirror_hash = hashlib.sha256(bytes(turn_0_mirror)).hexdigest()
    transform_list.append(turn_0_mirror_hash)

    turn_90 = np.transpose(img[::-1, ])
    turn_90_hash = hashlib.sha256(bytes(turn_90)).hexdigest()
    transform_list.append(turn_90_hash)

    turn_90_mirror = np.transpose(img)
    turn_90_mirror_hash = hashlib.sha256(bytes(turn_90_mirror)).hexdigest()
    transform_list.append(turn_90_mirror_hash)

    turn_180 = img[::-1, ::-1]
    turn_180_hash = hashlib.sha256(bytes(turn_180)).hexdigest()
    transform_list.append(turn_180_hash)

    turn_180_mirror = img[::-1]
    turn_180_mirror_hash = hashlib.sha256(bytes(turn_180_mirror)).hexdigest()
    transform_list.append(turn_180_mirror_hash)

    turn_270 = np.transpose(img[::1, ::-1])
    turn_270_hash = hashlib.sha256(bytes(turn_270)).hexdigest()
    transform_list.append(turn_270_hash)

    turn_270_mirror = np.transpose(img[::-1, ::-1])
    turn_270_mirror_hash = hashlib.sha256(bytes(turn_270_mirror)).hexdigest()
    transform_list.append(turn_270_mirror_hash)
    return frozenset(transform_list)


def main():

    # get image file names
    files = []
    for file in listdir():
        if file.endswith(".png"):
            files.append(file)

    # read in images and compare to existing

    answerlist = {}

    for png in files:
        img = 1-imread(png, as_grey=True)  # read an inverse gray scale image
        colorarea = np.nonzero(img)  # identify colored squares
        img = img[min(colorarea[0]):
            max(colorarea[0])+1, min(colorarea[1]):max(colorarea[1])+1]
        shape = make_transforms(img)
        if shape in answerlist.keys():
            answerlist[shape].append(png)
        else:
            [shape] = [png]

    # order the matches appropriately

    order = []
    regex = re.compile(r'\d+')

    for i in answerlist.keys():
        order.append(answerlist[i])

    for j in range(len(order)):
        for k in range(len(order[j])):
            num = regex.findall(order[j][k])
            num = int(num[0])
            order[j][k] = (num, order[j][k])
    towrite = sorted(order)

    for text in range(len(towrite)):
        towrite[text] = sorted(towrite[text])

    towrite = sorted(towrite)

    # write to file
    with open("answersTEST.txt", "w") as text_file:
        for length in range(len(towrite)):
            for lengthmore in range(len(towrite[length])):
                if lengthmore == len(towrite[length])-1:
                    text_file.write(towrite[length][lengthmore][1])
                else:
                    text_file.write(towrite[length][lengthmore][1] + " ")

            text_file.write("\n")

    opentext = open('answersTEST.txt', 'r')
    readtext = opentext.read()
    done = hashlib.sha256(bytes(readtext, 'utf-8')).hexdigest()
    opentext.close()

    print(done)
    return done


if __name__ == '__main__':
    main()
