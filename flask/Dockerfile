FROM python:3

# set a directory for the app
WORKDIR /usr/src/app

# copy all the files to the container
COPY . .

# define the port number the container should expose
EXPOSE 5000

# run the command
CMD ["python", "./app.py"]