import os

def find_null_bytes(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'rb') as f:
                        content = f.read()
                        if b'\x00' in content:
                            print(f'Null bytes found in: {file_path}')
                except Exception as e:
                    print(f'Error reading {file_path}: {e}')

if __name__ == "__main__":
    project_dir = os.path.dirname(os.path.abspath(__file__))
    find_null_bytes(project_dir)
