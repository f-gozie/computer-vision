# Face Detection and Recognition using Python, and OpenCV

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all the dependencies in the requirements.txt file

```bash
pip install requirements.txt
```

## Usage

#### Step 1: 
To obtain data to train for the facial recognition, go into the facial datasets directory `cd facial_datasets` and input the following command:

```bash
python build_face_dataset.py --cascade haarcascade_frontalface_default.xml --output /{path-to-storage-folder-indexed-by-username}/
```
and use `k` whenever you see a green rectangle outlining your face. It is advisable to save as many as possible, in order to properly train the model.

#### Step 2:
Copy the created images and save them in the `facial_recognition/dataset/{username}` folder. Then navigate into the facial_recognition directory `cd facial_recognition`. Then there are commands to run before the facial regonition can be used.

###### Command 1: 
```bash
python extract_embeddings.py --dataset dataset/ --embeddings output/embeddings.pickle --detector face_detection_model/ --embedding-model openface_nn4.small2.v1.t7
```
###### Command 2:
```bash
python train_model.py --embeddings output/embeddings.pickle --recognizer output/recognizer.pickle --le output/le.pickle
```
 Then depending on whether you are running the `recognize.py` (to recognize faces in an image), or `recognize_video.py` (to recognize faces in frames of a live video), you accompany the command with:

###### Command 3:
```bash
python recognize_video.py --detector face_detection_model/ --embedding-model openface_nn4.small2.v1.t7 --recognizer output/recognizer.pickle --le output/le.pickle
```

And then watch the facial recognition program in action.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.