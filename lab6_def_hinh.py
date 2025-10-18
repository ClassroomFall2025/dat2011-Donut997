class chunhat:
    def __init__(self,chieudai,chieurong):
        self.chieudai = chieudai
        self.chieurong = chieurong
        
    def get_chuvi(self):
        return (self.chieudai + self.chieurong) * 2
    
    def get_dientich(self):
        return self.chieudai * self.chieurong
    
    def nhap_thong_so(self):
        self.chieudai = float(input("Nhap chieu dai:"))
        self.chieurong = float(input("Nhap chieu rong:"))
    
    def __str__(self):
        chu_vi = self.get_chuvi()
        dien_tich = self.get_dientich()
        return f"Dai={self.chieudai}, Rong={self.chieurong} | Dien tich={dien_tich} | Chu vi={chu_vi}"

class vuong:
    def __init__(self, canh):
        self.canh = canh
        
    def get_chuvi(self):
        return self.canh * 4
    
    def get_dientich(self):
        return self.canh * self.canh
    
    def nhap_thong_so(self):
        self.canh = float(input("Nhap canh:"))
    
    def __str__(self):
        chu_vi = self.get_chuvi()
        dien_tich = self.get_dientich()
        return f"Canh={self.canh} | Dien tich={dien_tich} | Chu vi={chu_vi}"