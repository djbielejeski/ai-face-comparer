import os

from deepface import DeepFace

class ImageResult:
    def __init__(self, file_path: str, distances):
        self.file_path = file_path
        self.distances = distances

        # todo: calculate the distances

class ImageDirectoryLoader:
    def __init__(self, directory: str):
        self.directory = directory

        self.image_paths = [
            os.path.join(directory, file_name) for file_name in os.listdir(directory)
            if any(file_name.endswith(ext) for ext in ['.jpg', '.jpeg', '.png'])
        ]

        self.image_results = []

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

                    distances = []
                    if all_results.size > 1:
                        # get row 0 (should be the most similar)
                        for index in range(all_results.shape[0]):
                            if index > 0:
                                result_row = all_results.iloc[index]

                                # the smaller the distance, the closer the result
                                # 0.10 is more similar than 0.90
                                distance = result_row['VGG-Face_cosine']
                                distances.append(distance)

                image_result = ImageResult(file_path=image_path, distances=distances)
                self.image_results.append(image_result)


        else:
            print(f"No images found in {self.directory}")


        for image_result in self.image_results:
            print(image_result.file_path)
            print(image_result.distances)

