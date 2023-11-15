# ai-face-comparer

#### Command
```cmd
python "main.py" --source_images "source_images"
```

Source images should be a directory containing your people's images that will get compared with each other

```
- source_images
    - David
    - Bob
    - Sarah
    - etc
```


#### Example output
```
source_images\PXL_20221123_224337061.MP.jpg
Hits: 82.  Score: 58.962542112367615
source_images\PXL_20230804_220655323.PORTRAIT.jpg
Hits: 81.  Score: 58.30793635357012
source_images\IMG_20230821_165950.jpg
Hits: 79.  Score: 57.91023323102564
source_images\PXL_20221105_011053188.MP.jpg
Hits: 82.  Score: 57.73867708056598
source_images\IMG_20110423_181250.jpg
Hits: 78.  Score: 56.56335279322644
source_images\IMG_20230217_112954.jpg
Hits: 78.  Score: 56.51224985767183
source_images\IMG_20230101_094345.jpg
Hits: 79.  Score: 56.176979792697836
source_images\PXL_20221022_153547675.PORTRAIT.jpg
Hits: 80.  Score: 55.64468732452013
```

### Pre-Requisites

1. [Git](https://gitforwindows.org/)
2. [Python 3.10](https://www.python.org/downloads/)
3. Open `cmd`
4. Clone the repository
    1. `git clone https://github.com/djbielejeski/ai-face-comparer`
5. Navigate into the repository
    1. `cd ai-face-comparer`

### Activate Environment and Install Dependencies

```cmd
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```

#### Run

```cmd
python "main.py" --source_images "C:/source_images"
```

#### Cleanup

```
cmd> deactivate 
```
