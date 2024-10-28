total_jam = 0

def hitung(jam_kerja, hari_ke):
    global total_jam
    total_jam += jam_kerja
    if hari_ke == 7:
        print(f"Total jam kerja dalam seminggu adalah: {total_jam} jam")
        







