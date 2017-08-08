import argparse
import os
import shutil

def main(image_dir,label_dir,save_dir,label_dataset):
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
        print('Created',save_dir)
    for image in os.scandir(image_dir):
        if image.name.endswith('_rgb.jpg'):
            label_folder_name = image.name.replace('_rgb.jpg','_label_json')
            label_folder_path = os.path.join(label_dir, label_folder_name)
            label_path = os.path.join(label_folder_path,'label_'+label_dataset+'.png')
            if not os.path.exists(label_path):
                print('label requested not present, exitting..')
                return
            label_newname = image.name.replace('_rgb.jpg','_label.png')
            label_newpath = os.path.join(save_dir, label_newname)
            
            shutil.copy(image.path, save_dir)
            print(image.path,'copied to',save_dir)
            shutil.copy(label_path, label_newpath)
            print(label_path, 'copied to',label_newpath)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('image_dir',help='dir of images',type=str)
    parser.add_argument('label_dir',help='dir of annotations and labels',type=str)
    parser.add_argument('save_dir',help='save dir of dataset',type=str)
    parser.add_argument('label_dataset',type=str,help='classes of dataset used for label, e.g.: dataset1, dataset2, etc')
    args = parser.parse_args()
    main(os.path.pathnorm(args.image_dir), os.path.pathnorm(args.label_dir),
     os.path.pathnorm(args.save_dir), str(args.label_dataset))