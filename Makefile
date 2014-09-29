#Makefile for local deployment of a Django project

venv: 	virtualEnv 
		
virtualEnv: 
		virtualenv .
		
#sourceIt:		
#		source ./bin/activate
		
deploy: instalReqFile makeMigrations makeMigrate runServer		

instalReqFile:		
		pip install -r ./src/requirements.txt
		
makeMigrations:
		python ./src/manage.py makemigrations 

makeMigrate:
		python ./src/manage.py migrate
		
runServer:
		python ./src/manage.py runserver 8888

clean:  
	 	rm -r ./lib ./include ./bin ./src/db.sqlite3

