# Using selenium with docker and remote-debugging activated

## Run everything in docker

### Usage

Modify the script `test_script_inside_docker.py`, insert other python modules required in requirements.txt then:

```bash
docker build -t test_selenium .
docker run -d -p 4444:4444 -p 7900:7900 -p 9222:9222 --shm-size="2g" --name selenium test_selenium
docker container exec -it -d selenium /opt/google/chrome/google-chrome-base --remote-debugging-address=0.0.0.0 --remote-debugging-port=9222 --disable-fre --no-default-browser-check --no-first-run
docker container exec -it selenium /usr/bin/python3 test_script_inside_docker.py
```

Connect to `http://localhost:7900/?autoconnect=1&resize=scale&password=secret` to check results.

Need to rebuild the image with `docker build -t test_selenium .` if you change the script everytime or requirements.txt.
This is the recommended solution for production.
