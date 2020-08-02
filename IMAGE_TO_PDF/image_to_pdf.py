from PIL import Image as m
i=m.open("Python(Basics)_HackerRank.png")
j=i.convert("RGB")
j.save("Python(Basics)_HackerRank.pdf")
