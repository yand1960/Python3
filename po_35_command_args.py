import sys
from po_34_logging import logger

print(sys.argv)

try:
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    z = x + y
    print(f"{x}+{y}={z}")
except:
    logger.error("ERRRRRRR!")

# x = int(input("X: "))
# y = int(input("Y: "))

