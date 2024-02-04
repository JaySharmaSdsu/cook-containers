import argparse
import os

from src.read_configurations import ReadConfigurations
from src.manage_containers import ContainerManager

def main():

    parser = argparse.ArgumentParser()

    default_config_file = os.getcwd()

    parser.add_argument('-c','--config_file',help='pass the path to the config file', default=default_config_file)

    args = parser.parse_args()

    config_file = os.path.join(default_config_file, args.config_file)

    configurations = ReadConfigurations.read_configurations(config_file)

    container_manager = ContainerManager(configurations['containers'])

    container_manager.manage_containers()



    return


if __name__== "__main__":
    SystemExit(main())