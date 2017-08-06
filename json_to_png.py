import argparse
import os
import subprocess 

def main(annot_dir):
    for json in os.scandir(annot_dir):
        if not json.name.endswith('_label.json'):
            continue
        new_folder = json.path.replace('.','_')
        if os.path.exists(new_folder):
            print('png for',json.name,'already exists, continuing next..')
            continue
        p = subprocess.Popen(['labelme_json_to_dataset',json.path])
        try:
            p.wait()
        except KeyboardInterrupt:
            print('\nInterrupted, terminating with progress:',
                  completed,'/',total)
            p.terminate()
            return
        os.remove(os.path.join(new_folder, 'image.png'))
        print(json.name,'converted to png')
    print('All jsons in dir converted to png.')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('annot_dir',help='Directory of json files',type=str)
    args = parser.parse_args()
    main(args.annot_dir)