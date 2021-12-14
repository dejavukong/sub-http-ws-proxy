# sub-http-ws-proxy
Start a local http server and revice substrate POST request, sand to a websocket endpoint and return the recv to POST response.

## env
```bash
python -m venv venv
pip install -r requirements.txt
```

## run
```bash
python main.py
```
By default, this command will start a http server on `127.0.0.1:9933`.