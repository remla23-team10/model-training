import os
import yaml

def test_dvc_files_exist():
    """
    At this point, dvc repro has been run, so all files should exist.
    Test that all files in dvc.yaml exist
    """
    with open('dvc.yaml', 'r') as f:
        dvc_config = yaml.safe_load(f)
    for stage in dvc_config['stages']:
        for file in dvc_config['stages'][stage]['outs']:
            assert os.path.exists(file), f"File {file} does not exist"