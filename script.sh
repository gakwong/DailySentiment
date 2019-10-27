#!/bin/bash
echo ">>>>>>>>>>>>>>> SETTING UP FLASK SERVER <<<<<<<<<<<<<<<"
export GOOGLE_APPLICATION_CREDENTIALS="/Users/alan/Desktop/service-account-file.json"
export FLASK_APP=PoemNews/
flask run
