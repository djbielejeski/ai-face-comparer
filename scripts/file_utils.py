import os

from deepface import DeepFace
from PIL import Image, ImageFont, ImageDraw

class ImageDistance:
    def __init__(self, file_path: str, distance: float):
        self.file_path = os.path.normpath(file_path)
        self.distance = distance


class ImageResult:
    def __init__(self, file_path: str, image_distances: list[ImageDistance]):
        self.file_path = os.path.normpath(file_path)
        self.image_distances = image_distances
        self.score = 0
        self.hits = 0

    def create_image_plot(self):

        margin_right = 24

        image = Image.open(self.file_path)
        grid_width = image.width
        grid_height = image.height
        for image_distance in self.image_distances:
            child_image = Image.open(image_distance.file_path)
            grid_width += child_image.width + margin_right
            if child_image.height > grid_height:
                grid_height = child_image.height

        # add space for the text
        grid_height += 256

        grid_image = Image.new(mode="RGB", size=(grid_width, grid_height))

        font = ImageFont.truetype("arial.ttf", 84)
        drawing_image = ImageDraw.Draw(grid_image)

        text_y = grid_height - 128

        # draw our text for our source image
        drawing_image.text((0, text_y), text="Source", font=font, fill=(255, 255, 255))

        left = 0
        top = 0
        grid_image.paste(image, box=(left, top))

        left += image.width + margin_right

        for index, image_distance in enumerate(self.image_distances):
            # upper left corner of image, paste
            child_image = Image.open(image_distance.file_path)
            grid_image.paste(child_image, box=(left, top))

            # draw the distance metric
            drawing_image.text((left, text_y), text=f"{image_distance.distance}", font=font, fill=(255, 255, 255))

            left += child_image.width + margin_right

        grid_image.show()


class ImageDirectoryLoader:
    def __init__(self, directory: str):
        self.directory = os.path.normpath(directory)

        self.image_paths = [
            os.path.join(directory, file_name) for file_name in os.listdir(directory)
            if any(file_name.endswith(ext) for ext in ['.jpg', '.jpeg', '.png'])
        ]

        self.image_results: list[ImageResult] = []

    def compare_images(self):
        if len(self.image_paths) > 0:
            print(f"Processing {len(self.image_paths)} images from '{self.directory}'")

            database_file_path = os.path.join(self.directory, 'representations_vgg_face.pkl')

            if os.path.exists(database_file_path):
                os.remove(database_file_path)

            for image_path in self.image_paths:
                print(f"Processing {image_path}")

                data_frame = DeepFace.find(
                    img_path=image_path,
                    db_path=self.directory,
                    model_name='VGG-Face',
                    detector_backend='retinaface',
                    enforce_detection=False,
                    silent=True,
                )

                if len(data_frame) > 0:
                    all_results = data_frame[0]

                    image_distances: list[ImageDistance] = []
                    if all_results.size > 1:
                        # get row 0 (should be the most similar)
                        for index in range(all_results.shape[0]):
                            if index > 0:
                                result_row = all_results.iloc[index]

                                # the smaller the distance, the closer the result
                                # 0.10 is more similar than 0.90
                                image_distance = ImageDistance(
                                    file_path=result_row['identity'],
                                    distance=result_row['VGG-Face_cosine']
                                )
                                image_distances.append(image_distance)

                image_result = ImageResult(file_path=image_path, image_distances=image_distances)
                self.image_results.append(image_result)


        else:
            print(f"No images found in {self.directory}")

        def calculate_scores():
            for image_result in self.image_results:

                # See how many times this image shows up in all of the results
                image_result.score = 0
                for other_image_result in self.image_results:
                    if other_image_result.file_path == image_result.file_path:
                        pass
                    else:
                        for image_distance in other_image_result.image_distances:
                            if image_distance.file_path == image_result.file_path:
                                image_result.hits += 1
                                image_result.score += (1 - image_distance.distance)

        # Calculate the scores
        calculate_scores()

        # sort the results from highest to lowest
        self.image_results.sort(key=lambda x: x.score, reverse=True)

        # Print out the results
        for image_result in self.image_results:
            print(image_result.file_path)
            print(f"Hits: {image_result.hits}.  Score: {image_result.score}")

            # Optional - Show the source image with its matches and their scores
            # image_result.create_image_plot()
