# Real_img-AVATAR

[![MasterHead](https://raw.githubusercontent.com/Asif12as/Real_img-AVATAR/main/sample/projectINT.JPG)

TO CHECK OUT THIS,
GO TO THE root dir and  then indexx file inside the project dir and run this file
> Convert images  into avatar!


---problem statement---
Title - Avatar Generation from Real Images using Deep Learning

Creating avatars from real images is a fascinating and challenging problem in computer vision and deep learning. The task at hand is to develop a system capable of generating personalized avatar images from real photographs of individuals. These avatars should capture the essence of the person while stylizing them in a unique and artistic way.



## Contents

- [Prerequisites for Google Cloud and Algorithmia](#prerequisites-for-google-cloud-and-algorithmia)
- [Installation](#installation)
  - [Docker](#using-docker)
  - [VirtualEnv](#using-virtualenv)
  - [Google Colab](#using-google-colab)
- [Sample Image](#sample-image)

---

## Prerequisites for Google Cloud and Algorithmia

**These are important steps if you want to leverage Google buckets, signed URLs and Algorithmia's platform. Skip this if you want to run locally / colab.**

### Cloud Run authentication
To use any functionalities pertaining to Google Cloud, you'll need a global authentication file (JSON). You can obtain this JSON by following the steps given here - [Getting started with authentication](https://cloud.google.com/docs/authentication/getting-started)

After you get the JSON file, rename it to `token.json` (so that it's compatible with the codebase). 

Set the environment variable in your terminal -
```
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/token.json"
```
**Notes**:
- You can set it permanently by adding this line to `~/.bashrc`.
- `Dockerfile` already includes the setting of this particular environment variable. :)


### Algorithmia
We used the Serveless AI Layer product of [Algorithmia](https://algorithmia.com/serverless-ai-layer) for inference on videos.
To learn more on how to deploy your model in Algorithmia, check here - https://algorithmia.com/developers

---

## Installation

### Application tested on:

- python 3.7
- tensorflow 2.1.0 
- tf_slim 1.1.0
- ffmpeg 3.4.8
- Cuda version 10.1
- OS: Linux (Ubuntu 18.04)

### Using Docker

The easiest way to get the webapp running is by using the Dockerfile:

1. `cd` into the root directory and build the image
```
docker build -t cartoonize .
```
**Note**: Set the appropriate values in `config.yaml` before building the image.

2. Run the container by exposing the appropriate ports
```
docker run -p 8080:8080 cartoonize
```


### Using `virtualenv`

1. Make a virtual environment using `virutalenv` and activate it
```
virtualenv -p python3 cartoonize
source /bin/activate
```
2. Install python dependencies
```
pip install -r requirements.txt
```
3. Run the webapp. Be sure to set the appropriate values in `config.yaml` file before running the application.
```
python app.py
```

### Using [Google Colab]
1. Clone the repository using either of the below mentioned way:
   - Using Command:
        - Create a new Notebook in Colab and in the cell execute the below command.  
        
        ```
         ! git clone https://github.com/experience-ml/cartoonize.git
        ```
        **Note:** Don't forget to add `!` at the beginning of the command
        
    - From Colab User Interface
 ```
        Open Colab
            └── File
                 └── Open Notebook
                          └── Github
                                └── paste the Url of the repository
 ```
 Note :  Before running the application change the runtime to GPU for processing videos but you for images CPU shall also work just fine.
 ```
            Runtime
               └── Change runtime type
                           └── Select GPU
 ```
2. After cloning the repository navigate to the `/cartoonize` using below command in the notebook cell:

   ```
   %cd cartoonize
   ```
3. Run the below commands in the notebook cell to install the requirements. 

   ```
   !pip install -r requirements.txt
   ```


4. In config.yaml file set: 

   ``` 
   colab-mode: true 
   ``` 
   
5. Launch the flask app on ngrok

   ```
   !python app.py
   ```


## Sample Image

### Emma Watson Cartoonized
<img alt="Emma Watson Cartoonized" style="border-width:0" src="static/sample_images/twitter_image.png" />

