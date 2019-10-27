#!/bin/bash
echo ">>>>>>>>>>>>>>> SETTING UP FLASK SERVER <<<<<<<<<<<<<<<"
set GOOGLE_APPLICATION_CREDENTIALS=C:\Users\gbobt\Desktop\service-account-file.json
set FLASK_APP=DailySentiment
flask run
$SHELL
