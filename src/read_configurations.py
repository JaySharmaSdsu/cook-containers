import yaml
import os

class ReadConfigurations():

    @classmethod
    def read_configurations(self, path, file_name):
        _configurations_file = os.path.join(path, file_name)
        
        try: 
            with open(_configurations_file, 'r') as _file:
                configurations=yaml.safe_load(config_file)
            
            return configurations
        except yaml.YAMLError as exc:
            print(f"Error reading YAML file: {exc}")
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            
