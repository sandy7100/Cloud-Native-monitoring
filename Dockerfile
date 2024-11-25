# since this is python application we need to a have python as a base image
#use the official python image as the base image
FROM python:3.9-slim-bookworm  

# we need to specific the working directory now in which all the docker command will run
# set the working dir in the cointainer
WORKDIR /app

# Now we have to copy all the requirements so that docker can have all the requirements and code file to run the application in any machine inspite of the depencies being installed or not
# copy the requirements file to the working directory
COPY requirements.txt .

# to install all the required python packages
RUN pip3 install --no-cache-dir -r requirements.txt

# copy all the code in the this directory (app.py and templates)
# copy the application code to the working directory
COPY . .

#setting the host to local 0.0.0.0
# set the environment variable for the Flask app
ENV FLASK_RUN_HOST=0.0.0.0

# EXPOSING the port to run the flask application
EXPOSE 5000

#Command to run the flask application
CMD ["flask","run"]