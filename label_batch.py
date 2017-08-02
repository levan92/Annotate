import argparse
import os

def main(image_dir, annot_dir):
    for image in os.scandir(image_dir):
        if image.name.endswith('_rgb.jpg'):
            print('opening annotation tool for',image.name)
            newname = image.name.replace('_rgb.jpg','_label.json')
            new_path = os.path.join(annot_dir, newname)
            if os.path.exists(new_path):
                print('Annot for',image.name,'exists, moving on to next image.')
                continue
            os.system('labelme '+image.path
                      +' -O '+os.path.join(annot_dir,newname))
            print('annotation completed for',image.name)
        else: 
            print('Image format wrong, moving on the next image')
    print('Finished annotating all images,', 
          'num of annotations in', annot_dir,':',
        len([i for i in os.listdir(annot_dir) if i.endswith('_label.json')]))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('image_dir',help='dir of images to be annotated',type=str)
    parser.add_argument('annot_dir',help='save directory',type=str)
    args = parser.parse_args()
    main(args.image_dir, args.annot_dir)