#### Facial detection on the edge

Note: this is only facial detection and __NOT__ recognition.

To get started just install the dependencies mentioned in the `requirements.txt`.

To start the backend just run
```bash
crossbar start
```
that will expose a WAMP remote procedure `io.crossbar.detect_faces` on port `8080`. The procedure expects a single
positional argument of type bytes array.

`runner.py` is a sample python3 client that you may run. The backend was also tested with
Android using Autobahn Java.

Run example client as
```bash
python3 -u runner.py /path/to/a/photo
```
