

# Upload a new Docker mod_visus image (OPTIONAL Developers only)

Choose the tag you want to expose (note: docker TAG and OpenVIsus TAG can be different

```
TAG=$(python3 Libs/swig/setup.py print-tag) && echo ${TAG}
```

Build the new Docker image:

```
cd Docker/mod_visus/httpd
sudo docker build --tag visus/mod_visus:$TAG  .
```

Eventually debug it:

```
sudo docker run --publish 8080:80 visus/mod_visus:$TAG
# sudo docker run --rm -it --publish 8080:80 visus/mod_visus:$TAG /bin/bash
# open http://localhost:8080/mod_visus?action=list
```

Eventually push it to docker hub (change username as needed):

```
# only first time remember to login
# sudo docker login --username=scrgiorgio 
sudo docker push visus/mod_visus:$TAG

# now push the latest tag (IMPORTANT so latest will be the real last one)
sudo docker build --tag visus/mod_visus:latest  .
sudo docker push visus/mod_visus:latest
```






