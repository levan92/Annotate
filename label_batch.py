import argparse
import os
import subprocess

def main(image_dir, annot_dir):
    images = [f for f in os.scandir(image_dir) if f.name.endswith('_rgb.jpg')]
    total = len(images)
    completed = 0
    for image in images:
        newname = image.name.replace('_rgb.jpg','_label.json')
        new_path = os.path.join(annot_dir, newname)
        if os.path.exists(new_path):
            print('Annot for',image.name,
                  'exists, moving on to next image.')
            completed += 1
            print('Progress:',completed,'/',total)
            continue
        print('Opening annotation tool for',image.name)
        p = subprocess.Popen(['labelme',image.path,'-O',new_path])
        try:
            p.wait()
        except KeyboardInterrupt:
            print('\nInterrupted, terminating with progress:',
                  completed,'/',total)
            p.terminate()
            return
        print('Annotation completed for',image.name)
        completed += 1
        print('Progress:',completed,'/',total)
    print('Finished annotating all images,', 
          'num of annotations in', annot_dir,':',
          len([i for i in os.listdir(annot_dir) \
               if i.endswith('_label.json')]))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('image_dir',help='dir of images to be annotated',type=str)
    parser.add_argument('annot_dir',help='save directory',type=str)
    args = parser.parse_args()
    main(args.image_dir, args.annot_dir)