import subprocess;
import time;
URL_PYTHON = "https://fr.wikipedia.org/wiki/Python_(langage)"
URL_JAVASCRIPT = "https://fr.wikipedia.org/wiki/JavaScript" 

process=subprocess.Popen(["powershell",'docker build -f .\Dockerfile-simple -t img_1csimple .'])
time.sleep(5)
process=subprocess.Popen(["powershell",f'docker run --rm -e URL="{URL_PYTHON}" -e LANGUAGE="python" -v $pwd/python:/usr/src/app/python img_1csimple'])
time.sleep(5)
process=subprocess.Popen(["powershell",f'docker run --rm -e URL="{URL_JAVASCRIPT}" -e LANGUAGE="javascript" -v $pwd/javascript:/usr/src/app/javascript img_1csimple'])