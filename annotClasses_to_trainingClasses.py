import argparse
import os
from PIL import Image
import yaml

# Training Class for dataset_3
# mapping = {'dataset_num':3, 'background':0, '1':1, '2':2, '3':2, '4':2, '5':3, '6':3}

# Training Class for dataset_1 (maps 'furniture usually bg' to 'bg')
mapping = {'dataset_num':1, 'background':0, '1':1, '2':2, '3':2, '4':3, '5':3, '6':3}

def main(annot_dir):
    for folder in os.scandir(annot_dir):
        if folder.is_dir() and folder.name.endswith('label_json'):
            print('Processing',folder.name)
            yaml_path = os.path.join(folder.path, 'info.yaml')
            with open(yaml_path, 'r') as stream:
                label_names_dict = yaml.load(stream)
            label_path = os.path.join(folder.path, 'label.png')
            im = Image.open(label_path)
            pix = im.load()
            width, height = im.size
            for x in range(width):
                for y in range(height):
                    idx = pix[x,y]
                    annot_label = label_names_dict['label_names'][idx]
                    pix[x,y] = mapping[annot_label]
            new_label_name = 'label_dataset' + str(mapping['dataset_num']) + '.png'
            new_label_path = os.path.join(folder.path, new_label_name)
            print('saving as',new_label_path)
            im.save(new_label_path)
    print('All done.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('annot_dir',help='Directory where converted labels are',type=str)
    args = parser.parse_args()
    main(os.path.normpath(args.annot_dir))