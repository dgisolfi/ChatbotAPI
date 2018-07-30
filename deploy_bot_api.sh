#!/bin/bash
docker pull dgisolfi/chatbot_api
docker run --rm --name chatbot_api_prod -p 5525:5525 dgisolfi/chatbot_api
