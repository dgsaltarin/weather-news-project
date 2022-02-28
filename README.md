# weather-news-project

## Description:
Weather-news is a project that provides weather information and most relevant news from a particupar city, in order to do that users must provide the name of the city in English.

## Structure:
To build the application, it was divided into a backend and a frontend.

## Skills:
Some of the technologies that were used to build this solution are:
- [Python3.9](https://www.python.org/downloads/release/python-390/)
- [FastApi](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [MongoDb](https://www.mongodb.com/)
- [Angular](https://angular.io/)
- [NodeJs](https://nodejs.org/es/)
- [AWS](https://aws.amazon.com/es/)

## Backend: 
For the backend side of the application, was using python as main language, along with fastapi framework to build an API that provide the informtion, also is in charge of save the user search history into a mondoDB clouster
![Screenshot_101](https://user-images.githubusercontent.com/53949337/156016455-6854133d-1496-41c2-8506-9e8939ac0959.png)
### Deploy:
The backend was deploy using docker, the docker container it now running into a aws ec2 instance located here:
http://ec2-3-21-162-118.us-east-2.compute.amazonaws.com/docs


### Frontend:
For the visual part of the application was used angular to create an web app that allow us to display the information related to the weather and the most relevant news of the request city:
![Screenshot_102](https://user-images.githubusercontent.com/53949337/156017016-0c307906-7595-48a9-a96f-9acecad0eadd.png)
