# Storyteller
A twitter bot to provide interactive microfiction!

This python3 program uses tweepy and nltk to create procedural quest dialogue and post it to twitter for all who tweet at it.

## Build Docker Image to Test
 1. Run the command in the bash shell from the project directory:

     ```docker build . -t storyteller-bot```

 2. Test your build from powershell with
   
     ```docker run -it -e CONSUMER_KEY="key val here" -e CONSUMER_SECRET="key val here" -e ACCESS_TOKEN="key val here" -e ACCESS_TOKEN_SECRET="key val here" storyteller-bot```

## Build and Deploy Docker Image
Note: Everything is in the bash shell for this part! This is also for digital ocean droplets, and `twitter-bot-drop` is the name of my digital ocean droplet that I'm making and `storyteller-bot` is the docker image name.
1. If you don't have anything registered as a docker-machine (which controls multiple instances of docker images) then you make one.
   
    ```docker-machine create --driver digitalocean --digitalocean-access-token YOUR-ACCESS-TOKEN-HERE twitter-bot-drop```

2. Then this command sets your current shell environment to be your docker-machine shell environment
   
    `eval $(docker-machine env twitter-bot-drop)`

3. Then in your new shell you build your docker image
   
    `docker build . -t storyteller-bot`

4. And then deploy it! The only difference here is the -id instead of -it which just tells it you want it to be detached from your shell.
   
    `docker run -id -e CONSUMER_KEY="key val here" -e CONSUMER_SECRET="key val here" -e ACCESS_TOKEN="key val here" -e ACCESS_TOKEN_SECRET="key val here" storyteller-bot`

Et voila! Functioning docker image running on your droplet (which is called a docker-machine)