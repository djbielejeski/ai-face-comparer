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
