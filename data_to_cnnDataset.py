import argparse
import os
import shutil

def main(image_dir, label_dir, save_dir):
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
        print('Created',save_dir)
    for image in os.scandir(image_dir):
        if image.name.endswith('_rgb.jpg'):
            shutil.copy(image.path, save_dir)
            print(image.path,'copied to',save_dir)
            label_folder_name = image.name.replace('_rgb.jpg','_label_json')
            label_folder_path = os.path.join(label_dir, label_folder_name)
            label_path = os.path.join(label_folder_path,'label.png')
            label_newname = image.name.replace('_rgb.jpg','_label.png')
            label_newpath = os.path.join(save_dir, label_newname)
            shutil.copy(label_path, label_newpath)
            print(label_path, 'copied to',label_newpath)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('image_dir',help='dir of images',type=str)
    parser.add_argument('label_dir',help='dir of annotations and labels',type=str)
    parser.add_argument('save_dir',help='save dir of dataset',type=str)
    args = parser.parse_args()
    main(args.image_dir, args.label_dir, args.save_dir)