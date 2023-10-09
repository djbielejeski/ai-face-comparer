import argparse
import os


class AIFaceComparerArguments:
    def __init__(
            self,
            source_images,
    ):
        self.source_images = source_images

        if not os.path.exists(self.source_images):
            raise Exception(f"'{self.source_images}' does not exist.")


def parse_arguments() -> AIFaceComparerArguments:
    def _get_parser(**parser_kwargs):
        parser = argparse.ArgumentParser(**parser_kwargs)

        parser.add_argument(
            "--source_images",
            type=str,
            required=True,
            help="Directory containing the images you want to process.  Should be a directory path to a folder containing *.png or *.jpg files."
        )

        return parser

    parser = _get_parser()
    opt, unknown = parser.parse_known_args()

    config = AIFaceComparerArguments(
        source_images=opt.source_images,
    )

    return config
