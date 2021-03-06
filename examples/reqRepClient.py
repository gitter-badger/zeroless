import logging

from zeroless import (connect, log)

consoleHandler = logging.StreamHandler()
log.setLevel(logging.DEBUG)
log.addHandler(consoleHandler)

# The request client connects to localhost and sends three messages.
sock = connect(port=12345)

for msg in ["Msg1", "Msg2", "Msg3"]:
    response = sock.request_and_listen(msg.encode())
    print(response)
