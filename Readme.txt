Add python modules in requirement txt 


#Build docker image 
docker build -t app .
docker images 

#Launch container from docker image app 

docker run -d --name flask1 -p 80:80 app
docker ps -a 

