# 1. Your docker file shall be called Dockerfile and exist within your module_6 folder
# All done.

# 2. Your dockerfile shall use python:3.10 as the base environment
FROM python:3.10

# Create a directory named /app
RUN mkdir /app

# Move to the /app directory
WORKDIR /app

# Copy app.py from teh current local dir into the /app dir
ADD run.py

# 3. Your dockerfile shall install requirements.txt from your module_6 folder
RUN pip istall -r requirements.txt

# 4. Your dockerfile shall expose the port 8080 to be used for your flask application.
EXPOSE 8080

# 5. Your dockerfile shall start your flask application using the command $python run.py
CMD ["python", "run.py"]

# 6. Your python code submitted for this assignment shall be linted to pylint 10/10
# All done.
