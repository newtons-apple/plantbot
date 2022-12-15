import move
import time
move.setup()
move.move(100,'forward','forward')
time.sleep(1)
move.move(100,'backward','backward')
time.sleep(1)
move.move(100,'forward','right',1)
time.sleep(1)
move.move(100,'forward','left',1)
time.sleep(1)