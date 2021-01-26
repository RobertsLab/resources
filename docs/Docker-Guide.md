###  Roberts Lab Docker Help File
 
##### <em>This file is intended to provide a brief introduction on using Docker and the Dockerfile, [Dockerfile.bio](https://github.com/RobertsLab/code/blob/master/dockerfiles/Dockerfile.bio), for the Roberts Lab.
 
 For Mac/Windows users, it is written as though you are using/launching Docker via Docker QuickStart Terminal, which is only available as part of [Docker Toolbox](https://www.docker.com/products/docker-toolbox)!</em>
 
 There are five sections of instructions, each with increasing usage complexity:
 
 - [Build an Image](#build)
    - Required to begin working with Docker.
 - [Starting a Container](#basic)
     - Instructions on running a container from an image.
    - Lacks the ability to interact with files on your computer.
 - [Using Jupyter Notebooks](#intermediate)
    - Instructions on how to run a container and use Jupyter Notebooks in your computer's browser.
    - Lacks the ability to interact with files on your computer.
 - [Interact with Files on Your Computer](#advanced)
    - Instructions on how to run a container that can interact with files on your computer.
    - This will be the most useful container and will likely be the default setup you use from here on out.
 - [Semi-important Supplemental Info](#supplemental)
    - Instructions on how to limit and reduce Docker image disk space usage by re-using existing images/containers and/or deleting old/unused images/containers.
 
####  <a name="build"></a>Build the Docker Image
 
 - Only needs to be done once.
 - Items in all caps (e.g. NAME) can be replaced with text of your choosing and does not need to be uppercase.
 - ~8GB in size
 
 1. Download and install [Docker](https://www.docker.com/) for your operating system ([Docker Toolbox](https://www.docker.com/products/docker-toolbox) if using Windows/Mac!!).
 2. Download the Roberts Lab bioinformatics Dockerfile: [Dockerfile.bio](https://github.com/sr320/LabDocs/blob/master/code/dockerfiles/Dockerfile.bio). Ideally, clone this repo. Otherwise, the Dockerfile should be saved in its own, dedicated directory (i.e. no other files in directory).
 3. Open a terminal.
 4. Change to the directory where you saved the Dockerfile.
 5. Build the Docker image:
     1. On Mac: 
         1. ```eval "$(docker-machine env default)"```
         2. ```docker build --tag="NAME/bioinformatics:v11" --file="Dockerfile.bio" .```
   2. Non-Mac:```docker build --tag="NAME/bioinformatics:v11" --file="Dockerfile.bio" .```
 
 Explanation:
 - ```docker build``` constructs the Docker image from the instructions in the Dockerfile. The Dockerfile tells Docker which programs should be downloaded, installed, and where/how to install them in the Docker image.
 - ```--tag="<name>"``` Allows you to give the image you build an easy to remember name. It can be anything you like.
 - ```--file="<dockerfile_name>" .``` Tells Docker the name of the Dockerfile and to look for it in the current directory (the ```.```).
 
####  <a name="basic"></a>Start a Docker Container (Basic)
 
 These instructions will run the Docker container from the [image built above](#build) with no "frills." See the [Intermediate](#intermediate) instructions to begin using Jupyter Notebooks in the Docker container.
 
 - Requires that a Docker image has already been built
 - Mac users: If opening a new Terminal window, enter the following before proceeding:
 
 ```eval "$(docker-machine env default)"```
 
 1. Identify existing image(s):
 
   ```docker ps -a```
   
 2. Start a Docker container (replace IMAGE_NAME with desired image name from Step 1): 
 
   ```docker run -it IMAGE_NAME /bin/bash```
 
   You will now be inside the docker container. The container is basically a specialized computer that has very few programs besides the bioinformatics programs specified in the Dockerfile. Feel free to move around and try things out.
 
 3. Exit the container: Type "exit".
 
 
 Explanation:
 
 - ```docker ps -a``` Lists all images on the system in order they were created, newest to oldest
 - ```docker run``` Starts a Docker container. Requires an image name.
 - ```-it``` Starts a Docker container with an interactive terminal (i.e. a terminal window to type in).
 - ```IMAGE_NAME``` The name of the image that should be used to start the Docker container.
 - ```/bin/bash``` The command that the container should run when it starts. In this case, we tell the container to start bash. Bash is the command line stuff you use when using Terminal.
 
####  <a name="intermediate"></a>Run Jupyter Notebook in Docker Container (Intermediate)
 
 1. Start a Docker container with specific port mappings:
 
   ```docker run -p 8888:8888 -it IMAGE_NAME /bin/bash```
   
 3. Start Jupyter Notebook (enter this inside the container):
 
   ```jupyter notebook```
   
 4. In a separate Terminal window, outside of your container, check the IP address of the Docker machine:
 
   ```docker-machine ip```
 
 5. Run Jupyter Notebook in your browser:
     1. Enter URL (in a different window or tab than what you're using for R Studio):
         1. Mac users (use the IP address from Step 4 above): e.g. ```192.168.99.100:8888```
         2. Others: ```localhost:8888```
 
 Explanation:
 - ```-p 8888:8888``` Tells Docker to create container that binds your computer's port 8888 to container port 8888. Allows you to use Jupyter Notebook in your browser.
 - The port bindings for your computer can be changed (the first number in the 8888:8888 part of the command). It's recommended to stick to port numbers greater than 9000 if they need to be changed. The port bindings for the container (the second number in the 88888:8888 part of the command) should not be changed, since Jupyter Notebooks are currently configured to connect to those ports of the container. 
 
####  <a name="advanced"></a>Access Files Outside of a Docker Container (Advanced)
 
 - WARNING! The current setup of the Roberts Lab Dockerfile.bio runs the Docker container as the "root" user. Any changes made to volumes on your computer that are mounted in the Docker container will be executed without asking for a password! If you mount the wrong directories of your computer, you may do serious harm (like, render it inoperable) to your computer when making changes to the directory mounted inside the Docker container!
 
 IMPORTANT! 
 
 - Mac users can only mount directories contained in the ```/Users``` directory! 
 - Windows users can only mount directories contained in the ```/c/Users/``` directory!
 - Requires that a Docker [image has already been built](#build)
 - Mac users: If opening a new Terminal window, enter the following before proceeding:
 
 ```eval "$(docker-machine env default)"```
 
 1. Start a Docker container with specific port mappings and volume mount points:
 
   ```docker run -p 8888:8888 -v /path/to/computer/folder:/path/to/container/folder -it IMAGE_NAME /bin/bash```
 
 Explanation:
 
 - ```docker run -p 8888:8888 -it IMAGE_NAME /bin/bash``` See the [Basic](#basic) & [Intermediate](#intermediate) guides.
 - ```-v``` This flag tells Docker to mount a volume from your computer in the Docker container.
 - ```/path/to/computer/folder:``` The location of the folder on your computer that you would like to be able to access from your Docker container. If the folder doesn't exist on your computer, Docker will create it.
 - ```/path/to/container/folder``` The location of the folder inside the Docker container where you will be able to access the folder on your computer specified in the first portion of the command.
 
 Example: 
 
 ```-v /Users/Sam/Downloads:/home/srlab/junk```
 
The above command allows me to acces the files in my Downloads folder on my computer. Once I'm in the Docker container, I would change to the "junk" directory to interact with the files in my Downloads folder on my computer.
 
 
Note: You can mount multiple volumes by adding multiple ```-v``` flags followed by the desired local and container mount points.
 
#### <a name="supplemental"></a>Supplemental Info
##### Reuse an existing container
 - Most users should follow this once they've built and run their first image/container.
 - Requires that a [Docker image has already been built](#build)
 - Requires that a [Docker container has been created](#basic)
 - Mac users: If opening a new Terminal window, enter the following before proceeding:
 
 ```eval "$(docker-machine env default)"```
 
 Every time the ```docker run``` command is used, a new container is created (even if you use the same exact ```docker run``` command). This can lead to clutter and confusion. To reuse an existing container do the following:
 
 1. ```docker ps -a``` Lists all existing containers
 2. If the container STATUS is listed as "Exited" use one of the following options:
     1. ```docker start CONTAINER_ID``` Replace "CONTAINER_ID" with the ID of the desired container.
     2. ```docker start NAMES``` Replace "NAMES" with the name of the desired container.
 3. If the container STATUS is listed as "Up", use one of the following options:
     1. ```docker attach CONTAINER_ID``` Replace "CONTAINER_ID" with the ID of the desired container.
     2. ```docker attach NAMES``` Replace "NAMES" with the name of the desired container.
 4. Press CTRL-c to enter the container.
 5. When finished, leave the container using one of the following options:
     1. Press CTRL-p, then press CTRL-q. This will detach the container and leave it running. This will allow you to skip Step 2 when reusing the container.
     2. ```exit``` This will stop the container. You will have to start at Step 2 in order to reuse the container.
