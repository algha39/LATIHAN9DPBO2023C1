from hunian import Hunian

class Indekos(Hunian):
    def __init__(self, nama_pemilik, nama_penghuni, jml_penghuni, ukuran, foto):
        super().__init__("Indekos")
        self.nama_pemilik = nama_pemilik
        self.nama_penghuni = nama_penghuni
        self.jml_penghuni = jml_penghuni
        self.ukuran = ukuran
        self.foto = foto

    def get_dokumen(self):
        return "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_nama_penghuni(self):
        return self.nama_penghuni
    
    def get_jml_penghuni(self):
        return self.jml_penghuni
    
    def get_ukuran(self):
        return self.ukuran
    
    def get_foto(self):
        return self.foto

    def get_detail(self):
        return str(super().get_summary()) + "\nNama Pemilik = " + self.get_nama_pemilik() + "\nNama Penghuni = " + self.get_nama_penghuni() + "\nJumlah Penghuni = " + self.get_jml_penghuni() + "\nUkuran = " + self.get_ukuran() + "\n"