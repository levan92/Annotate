import argparse
import os
import subprocess

def main(image_path, annot_dir):
    image_name = os.path.basename(image_path)
    newname = image_name.replace('_rgb.jpg','_label.json')
    new_path = os.path.join(annot_dir, newname)
    if os.path.exists(new_path):
        print('Annot for',image.name,'exists.')
        return
    print('Opening annotation tool for',image_name)
    p = subprocess.Popen(['labelme',image_path,'-O',new_path])
    try:
        p.wait()
    except KeyboardInterrupt:
        print('\nInterrupted, terminating annotation.')
        p.terminate()
        return
    print('Annotation completed for',image.name)
    return

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('image_path',help='path of image to be annotated',type=str)
    parser.add_argument('annot_dir',help='save directory',type=str)
    args = parser.parse_args()
    main(args.image_path, args.annot_dir)