set APP="docker.test"
docker build -t %APP% .
docker run -d -p 56733:80 -v %CD%:/app %APP%