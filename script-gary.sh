#!/bin/bash
echo ">>>>>>>>>>>>>>> SETTING UP FLASK SERVER <<<<<<<<<<<<<<<"
set GOOGLE_APPLICATION_CREDENTIALS="C:\Users\gbobt\Deskto\service-account-file.json"
set FLASK_APP = PoemNews
flask run
$SHELL
