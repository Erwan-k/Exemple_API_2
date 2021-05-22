Hello,

Here you will find the same API I proposed on the Exemple_API_1 project. 

The only difference is that on here you have a Dockerfile.

After you clone this repository I suggest you run the following commands : 

docker build -t name_of_container .

docker run -p1234:5000 name_of_container

Then you will be able to request the api with localhost:1234/connexion1 and localhost:1234/connexion2

Enjoy,

Erwan
