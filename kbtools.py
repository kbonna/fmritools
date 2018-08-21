def append_json(file_orig, file_append):
    '''
    This function simply adds NEW fields from .json specified as file_append
    to .json file_orig and overwrite result on the file file_orig within its
    location. Json fields are automatically sorted.

    Example usage:
    $ append_json('./sub-01_ses-01_task-rest_bold.json', 'slice_timing.json')
    
    Kamil Bonna, 21.08.2018
    '''
    from shutil import move
    import json
    import os

    def load_json(path):
        json_file = open(path)
        return json.loads(json_file.read())

    temp = os.path.split(file_orig)[0] + '/temp.json'
    
    with open(temp, 'w') as fp:
         json.dump({**load_json(file_orig), **load_json(file_append)}, fp, sort_keys=True, indent=4)

    move(temp, file_orig)

