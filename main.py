import os

from scripts.argument_parser import AIFaceComparerArguments, parse_arguments
from scripts.file_utils import ImageDirectoryLoader



if __name__ == "__main__":
    # Parse input arguments
    config: AIFaceComparerArguments = parse_arguments()

    for root, dirs, files in os.walk(config.source_images):
        for dir_name in dirs:
            subfolder_path = os.path.join(root, dir_name)

            image_directory_loader = ImageDirectoryLoader(directory=subfolder_path)
            image_directory_loader.compare_images()


    image_directory_loader = ImageDirectoryLoader(directory=config.source_images)
    image_directory_loader.compare_images()
