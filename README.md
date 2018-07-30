# ChatBot API

This ChatBot API is used to send, receive, and interact with GroupMe Bots. A GroupMe bot can be created [here](https://dev.groupme.com/bots). 

### Author

**Daniel Gisolfi** - *All current work* - [dgisolfi](https://github.com/dgisolfi)

## Docker Implementation

The API takes advantage of a docker container and is run using the image pulled from docker hub. The image for this honeypot can be found [here](https://hub.docker.com/r/dgisolfi/chatbot_api/). The Dockerfile found in the root directory of this repository is used to create the chatbot_api image. The Docker file does the following:

1. pull the latest version of Ubuntu from docker hub
2. install the following: python-pip, python-dev, build-essential
3. Create a directory in the image, and copy all of src into it
4. install all python requirements
5. define the entry-point and command to run on startup

## Running the API

To run the API, on a machine where Docker is installed run the following commands:

```bash
docker pull dgisolfi/chatbot_api
docker run --rm --name chatbot_api_prod -p 5525:5525 dgisolfi/chatbot_api
```

Once the container is running and a GroupMe bot has been created the Bot can be registered with the API, this requires four parameters found on the GroupMe bots site.

1. Bot Name
2. Bot ID
3. Group ID
4. An API Token

With the above parameters you may proceed in using the API, to do so open a browser and go to either [localhost:5525](0.0.0.0:5525) or the host ip of the vm the container is running on.

## Usage

All responses to the GroupMe API will have the form

```json
{
    "message":"Description of what happened",
    "data": "Content of response"
}
```

### Methods

#### *Retrieve the API help page*

**Definition**

`GET /`

**Response**

* 200 OK on success

#### *Register a bot with the API*

**Definition**

`POST /registerBot`

**Response**

- 201: created successfully
- 206: missing arguments for creation

```json
{
    "message": "Bot registered", 
    "data": {
        "bot_name": "Gary",
        "bot_id": "12djioadsf8",
        "group_id": 234565234,
        "api_token": "sdlkf88yfas8fa9sy9as8y9xvs09d"
    }
}
```

#### *Get Details about a Registered bot*

**Definition**

`GET /viewBots`

**Response**

- 200: success on bot returned
- 404: Bot Not Found

```json
{
    "message": "Bot registered", 
    "data": {
        "bot_name": "Gary",
        "bot_id": "12djioadsf8",
        "group_id": 234565234,
        "api_token": "sdlkf88yfas8fa9sy9as8y9xvs09d"
    }
}
```

#### *Send a Message as the Bot to the Group*

**Definition**

`POST /sendMsg`

**Response**

- 200: success on message sent
- 400: unable to send message

```json
{
    "message":"Message Sent", 
    "data": "Hello World!"
}
```

#### *Request recent message from the Group chat*

**Definition**

`GET /requestMessages`

**Response**

- 200: success on message sent
- 404: Messages or Groupchat not found

```json
{
  "data": {
    "meta": {
      "code": 200
    }, 
    "response": {
      "count": 1111, 
      "messages": [
        {
          "attachments": [], 
          "avatar_url": 	  "https://i.groupme.com/160x160.jpeg.5ffbb4dc2f9e426b9ea26290178d495f", 
          "created_at": 1532882036, 
          "favorited_by": [], 
          "group_id": "XXXXXXXXXX", 
          "id": "153288203636220194", 
          "name": "Marty", 
          "sender_id": "600556", 
          "sender_type": "bot", 
          "source_guid": "1c997500757b013638de22000b99a321", 
          "system": false, 
          "text": "Hello!", 
          "user_id": "600556"
        }, 
      ]
    }
  }, 
  "message": "Message Request Successful"
}
```














