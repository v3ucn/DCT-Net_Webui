
import cv2
from source.cartoonize import Cartoonizer
import os
import argparse

def process(img,model_dir):

    print(img)
    print(model_dir)

    algo = Cartoonizer(dataroot=model_dir)
    img = cv2.imread(img)[...,::-1]

    result = algo.cartoonize(img)

    cv2.imwrite('res.png', result)
    print('finished!')




if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Inference code to lip-sync videos in the wild using Wav2Lip models')
    parser.add_argument('--img', type=str, required=True)
    parser.add_argument('--modelid', type=str, required=True)
    args = parser.parse_args()
    

    process(args.img,args.modelid)



