import qrcode as q

features = q.QRCode(version = 1,
                    box_size = 40,
                    border=5)


features.add_data("")
features.make(fit =True)
generate = features.make_image(fill_color = 'black',back_color='white')

generate.save("ralujaQr.png")
