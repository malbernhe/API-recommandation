
# Marc 08/04/2020
# Arret et suppression de l'instance et de l'image précédente
docker stop jobirl_api
docker rm jobirl_api
docker rmi jobirl:latest


docker build -t jobirl .

docker run -d --name jobirl_api  -p 5000:5000 jobirl:latest

# -v /home/ubuntu/jobirl:/app 

curl http://127.0.0.1:5000/


