#!/bin/bash
echo ">>>>>>>>>>>>>>> SETTING UP FLASK SERVER <<<<<<<<<<<<<<<"
export GOOGLE_APPLICATION_CREDENTIALS="/Users/evelynwu/Desktop/service-account-file.json"
export FLASK_APP=DailySentiment/
flask run
