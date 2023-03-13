import os
import glob
from pyminifier import minification
import subprocess

def minify_file(file_path):
        
    minified_code = f"pyminifier --obfuscate --nonlatin --replacement-length=20 --gzip -o {file_path} {file_path}"
    # minified_code = f"pyminifier --obfuscate --nonlatin --replacement-length=20 --pyz -o {file_path} {file_path}"

    subprocess.run(['powershell', minified_code])
    
    # with open(file_path, 'r') as f:
    #     code = f.read()
        
    # minified_code = minification(code)
    
    # with open(file_path, 'w') as f:
    #     f.write(minified_code)
    
        
def minify_folder(folder_path):
    for file_path in glob.glob(os.path.join(folder_path, '**/*.py'), recursive=True):
        minify_file(file_path)
        
if __name__ == '__main__':
    # folder_path = 'C:/Users/sonia.s/Desktop/pyminifier/ese/ese_snmp'
    folder_path = 'C:/Users/sonia.s/Desktop/ese_obfuscation/test_ese3'
    # folder_path = 'C:/Users/sonia.s/Desktop/MyProjects/encryption/testing'
    minify_folder(folder_path)