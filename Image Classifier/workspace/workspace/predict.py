import torch
import argparse
import random
import os

from torch import nn, optim
from torchvision import models
from utility_functions import imshow, open_json, process_image, predict, prediction_test
from model_functions import load_checkpoint

images_d = 'test_images'
random_file = random.randint(1,102)
r_image = random.choice(os.listdir(f'{images_d}/test/{random_file}'))
r_flower = f'{images_d}/test/{random_file}/{r_image}'

parser = argparse.ArgumentParser(description="Image Classifier")
parser.add_argument('--image_dir', type = str, default = random_flower, help = 'Path to image')
parser.add_argument('--checkpoint', type = str, default = 'checkpoint.pth', help = 'Path to checkpoint')
parser.add_argument('--topk', type = int, default = 5, help = 'Top N Classes and Probabilities')
parser.add_argument('--json', type = str, default = 'flower_to_name.json', help = 'class_to_name json file')
parser.add_argument('--gpu', type = str, default = 'cuda', help = 'GPU or CPU')
arg,unknown = parser.parse_known_args()

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

class_name = open_json(arg.json)

model = load_checkpoint(arg.checkpoint)

checkpoint = torch.load(arg.checkpoint)

image = process_image(arg.image_dir)

probs, classes = predict(r_flower, model)

prediction_test(class_name,classes,probs,random_file)