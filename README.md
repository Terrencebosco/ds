# ds
## File Structure
```
.
├── app_api
│   ├── app.py
│   ├── Dockerfile
│   ├── __init__.py
│   ├── model
│   │   ├── keras_pred_subreddit_model_v5.h5
│   │   ├── keras_tokenizer_v5.pickle
│   │   ├── sklearn_label_encoder_v5.pickle
│   │   └── subreddit_info_cleaned.csv
│   ├── predict.py
│   ├── requirements.txt
│   └── templates
│       ├── about.html
│       ├── base.html
│       └── bootstrap_layout.html
├── code
│   ├── Code_for_API_Endpoint.ipynb
│   └── Subreddit_Predictor.ipynb
├── heroku_files
│   ├── heroku.yml
│   ├── notes.md
│   ├── Procfile
│   └── runtime.txt
├── LICENSE
├── Pipfile
├── Pipfile.lock
├── production
│   ├── Dockerfile
│   ├── model
│   │   ├── keras_pred_subreddit_model_v5.h5
│   │   ├── keras_tokenizer_v5.pickle
│   │   ├── sklearn_label_encoder_v5.pickle
│   │   └── subreddit_info_cleaned.csv
│   ├── pro_api.py
│   ├── pro_predict.py
│   └── requirements.txt
└── README.md
```
## Current File Logic:
We have two applications in our file system. `app_api` is the root of our flask application that has a frontend, model prediction, and dockerfile for production. our `production` folder is the api for frontend to connect to, also had docker specific file. `heroku_files` is the files used for production onto heroku.

## Task
Reddit is a community-determined aggregator of content. It is a social platform where users submit posts that other users 'upvote' or 'downvote' based on whether or not they like it. It is broken up into more than two million communities known as “subreddits,” each of which covers a different topic. The name of a subreddit begins with /r/, which is part of the URL that Reddit uses. For example, /r/nba is a subreddit where people talk about the National Basketball Association, while /r/boardgames is a subreddit for people to discuss board games. Those are straightforward subreddits, but they can get weird, such as /r/birdswitharms, a subreddit devoted to pictures of birds…with arms. 

Reddit is an evergrowing platform that sees thousands of new users per day, some of which are likely unsure of where to post. Post Here helps users find the best place to share on Reddit. Using Natural Language Processing techniques and by implementing a neural network achitecture, the user is able to enter a post and Post Here finds the subreddit that is most appropriate for that post.

## Data Exploration:

### Dimensionality
Dataset Dimensions: (1013000, 4)

70/30 Train, Test Split:
- X_train Dimensions: (709100,)
- y_train Dimensions: (709100,)
- X_test Dimensions: (303900,)
- y_test Dimensions: (303900,)

### Data Cleaning Workflow

For optimal results, all Reddit posts in the dataset were cleaned according to the following workflow:

1. Removal of all HTML line break tags
2. Addition of custom stopwords
3. Tokenization
4. Lemmatization and case normalization
5. Removal of all punctuation

### Length Distribution of Reddit Posts
![WordCount](https://i.imgur.com/vqjXP4N.png)

### Squarify Word Map
This word map contains the top 20 words in the vocabulary. The size of each box is indicative of the word frequency relative to the other words in the view. Colors are arbitrary.
<p align="center">
  <img src="https://i.imgur.com/5GXDISO.png" />
</p>

### Vocabulary Matrix
See the entire vocabulary matrix [here](https://drive.google.com/file/d/1foR_QCQcb3fb9W_3T6Wynq9sjmgrDjRI/view?usp=sharing)
| word   | appears_in | count   | rank | pct_total             | cul_pct_total        | appears_in_pct      |
|--------|------------|---------|------|-----------------------|----------------------|---------------------|
|        | 566496     | 2435031 | 1.0  | 0.039063590753664716  | 0.039063590753664716 | 0.5592260612043435  |
| like   | 390328     | 636698  | 2.0  | 0.010214124627438755  | 0.04927771538110347  | 0.3853188548864758  |
| know   | 309889     | 447384  | 3.0  | 0.007177085419338619  | 0.05645480080044209  | 0.3059121421520237  |
| think  | 278937     | 409689  | 4.0  | 0.006572369482063327  | 0.06302717028250543  | 0.2753573543928924  |
| time   | 269434     | 407695  | 5.0  | 0.006540381059754613  | 0.06956755134226003  | 0.2659763079960513  |
| want   | 262529     | 383150  | 6.0  | 0.00614662186939987   | 0.07571417321165991  | 0.25915992102665353 |
| get    | 256398     | 359679  | 7.0  | 0.005770092150238486  | 0.0814842653618984   | 0.2531076011846002  |
| go     | 227464     | 321469  | 8.0  | 0.005157114408806229  | 0.08664137977070463  | 0.22454491609081934 |
| work   | 198379     | 299179  | 9.0  | 0.004799530691022273  | 0.09144091046172692  | 0.19583316880552812 |
| look   | 212925     | 291777  | 10.0 | 0.004680785303896349  | 0.09612169576562324  | 0.2101924975320829  |
| try    | 206196     | 282536  | 11.0 | 0.004532538056877885  | 0.10065423382250112  | 0.20354985192497527 |
| feel   | 164762     | 279594  | 12.0 | 0.00448534149798509   | 0.10513957532048622  | 0.16264758144126354 |
| find   | 190761     | 250893  | 13.0 | 0.004024910350200552  | 0.10916448567068678  | 0.18831293188548864 |
| year   | 161215     | 238951  | 14.0 | 0.00383333274778799   | 0.11299781841847475  | 0.15914610069101678 |
| start  | 169322     | 229864  | 15.0 | 0.003687556020847532  | 0.1166853744393223   | 0.16714906219151038 |
| thing  | 168447     | 225241  | 16.0 | 0.003613392291492878  | 0.12029876673081515  | 0.1662852912142152  |
| people | 151173     | 220895  | 17.0 | 0.0035436722898109993 | 0.12384243902062615  | 0.1492329713721619  |
| day    | 144461     | 220715  | 18.0 | 0.003540784668940604  | 0.12738322368956678  | 0.1426071076011846  |
| need   | 162507     | 215368  | 19.0 | 0.0034550062867516928 | 0.13083822997631847  | 0.16042152023692005 |
| new    | 155756     | 207273  | 20.0 | 0.0033251435592747468 | 0.1341633735355932   | 0.15375715695952616 |
| help   | 164737     | 207224  | 21.0 | 0.003324357484704473  | 0.13748773102029768  | 0.1626229022704837  |

### Model Architecture
![AltText](architecture/model_architecture_w_batch_v2.png)

This model uses Keras and Tensorflow end-to-end open source machine learning libraries to implement a deep neural network for 1,013 class multi-classification analysis. The model is trained and validated on a dataset of 1,013,000 posts from real users. The posts are pre-processed before entering the network architecture and result in accuracy of 70% on a validation set of 303,900 posts.

### Training and Validation Curves
<p align="center">
  <img src="https://i.imgur.com/DzGgnTV.png" />
</p>

# Flask API for Reddit - Post Here

Gaining acces to api via url:
```
http://production-dev3.us-east-1.elasticbeanstalk.com/predict
```
* final api for build week
* predict route expects json object with key of "port" and value is the users text they want predicted.

## Pushing Model to Heroku from Command Line
make sure heroku cli is installed ([instructions can be found here](https://devcenter.heroku.com/articles/heroku-cli)).

```
git add .

git commit -m "<message>"

heroku create <appname>

heroku git:remote -a <appname>

git push heroku master
```

## Implementation of Docker Image for Heroku Flask App

docker: [download](https://www.docker.com/products/docker-desktop)

```
docker build -t <image name>:latest

docker run -it <image name>

docker stop <container id>

run flask app from local container:
    docker run -d -p 5000:5000 <image name>
```

make new app and push image to heroku:

```
heroku create <app name>

heroku container:push web --app <app name>

heroku container:release web --app <app name>
```

can update image with
```
heroku container:push web --app <app name>

heroku container:release web --app <app name>
```

## Implementing AWS Beanstalk Entity

```
pip install pipx

pipx ensurepath

pipx install awsebcli

eb init

eb create
```

# Docker Workflow:

## Use:
When working with docker its important to understand the purposes of a image and
container. docker allows developers to create applications with standardized executable. when
working and developing an application that runs locally we can create a docker container
with the same variables as our virtual environment so other users can run our application
without the need of configuring dependencies and environment variables.

## Application:
We started working with docker because our tensorflow predictive model was to large
to host on heroku. while looking for solutions we discovered [this](https://medium.com/tarkalabs/docker-deployments-to-heroku-5802b14df4fa#:~:text=Slug%20size%20limit%3A%20The%20maximum,you%20are%20out%20of%20luck.) article describing heroku applications using heroku.

The first goal was figuring out how to run our application within the container and being
able to access it from outside it. we used another [article](https://medium.com/@FelipeFaria/running-a-simple-flask-application-inside-a-docker-container-b83bf3e07dd5)
to understand the work flow of this docker image to build ours. the only difference between this
rendition and ours is how we formatted the application. in the `if __name__ == "__main__` we created the instance of the application when the file is called upon similar to the article. when the file was called the application starts.

This moves us into docker to "store" and use our application.

## Docker In Production:
The main issue we ran into was trying to understand the Dockerfile purpose and syntax. have has a total of 20 minutes of docker experience between the four of us the majority of our time was trouble shooting the docker container.

We initially started with an instance of alpine linux machine to run our docker image
but after several failed attempts and a quick reverence to the [docker](https://hub.docker.com/_/python) python documentation we settled on a pure instance of python to run our docker image.

We froze our pipfile and created a requirement,txt that can be downloaded into the container. created a directory, stored the current code to that directory then ran the application via [syntax](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
in the Dockerfile.

We then build the docker container via command line and tested outside port access. once that was
up and running we implemented the image onto [heroku](https://devcenter.heroku.com/articles/heroku-cli-commands)
