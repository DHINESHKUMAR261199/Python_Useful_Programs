import qrcode
q=qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
    )
d="https://drive.google.com/file/d/1j-5uArvXJkFLvQeeB6BueyqRySeZgYl7/view?usp=sharing"
q.add_data(d)
q.make(fit=True)
i=q.make_image(fill="black",back_color="white")
i.save("1.png")
