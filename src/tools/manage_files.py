from pathlib import Path

def list_file():
    """
    Function that list files in actual directory.
        
        Args:
            void
        
        Returns:
             return list file in actual directory.
    
    """
    folder = Path(".")
    return [f for f in folder.iterdir() if f.is_file()]

def read_file(file_path):
    """
    Function that read a file.
        
        Args:
            file_path (str): The path of the file to read.
        
        Returns:
             return content of the file.
    
    """
    with open(file_path, 'r') as f:
        return f.read()