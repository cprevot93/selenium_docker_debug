# Use the selenium/standalone-chrome image
FROM selenium/standalone-chrome:latest

# install chrome webdrivers
COPY chromedriver .
RUN sudo chmod +x chromedriver

# Install python dependencies
RUN sudo apt update && sudo apt install -y python3 python3-pip
COPY requirements.txt .
RUN sudo pip install -r requirements.txt

COPY test_script_inside_docker.py .
