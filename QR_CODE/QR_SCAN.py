from pyzbar.pyzbar import decode as d
from PIL import Image as m
l=d(m.open("1.png"))
print(l[0].data.decode())
