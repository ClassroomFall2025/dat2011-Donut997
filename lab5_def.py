
class sanpham:
    def __init__(self, ten_sp, gia, giam_gia):
        self.__ten_sp = ten_sp
        self.__gia = gia
        self.__giam_gia = giam_gia
        
    def get_ten_sp(self):
        return self.__ten_sp
    def get_ten_sp(self, ten_sp):
        self.__ten_sp = ten_sp
        
    def get_gia(self):
        return self.__gia
    def get_gia(self, gia):
        self.__gia = gia
        
    def get_giam_gia(self):
        return self.__giam_gia
    def get_giam_gia(self, giam_gia):
        self.__giam_gia = giam_gia
    
    def doc_giam_gia(self):
        return self.__giam_gia
    
    def ghi_giam_gia(self, giam_gia_moi):
        self.__giam_gia = giam_gia_moi
        
    def thue_nk(self):
        return self.__gia * 0.1
    
    def nhap_san_pham(self):
        self.__ten_sp = input("Nhap ten san pham")
        self.__gia = float(input("Nhap gia san pham"))
        self.__giam_gia = float(input("Nhap gia duoc giam"))
    
    def xuat_tt_sp(self):
        print(f"San pham: {self.__ten_sp} co gia {self.__gia} duoc giam {self.__giam_gia} va phai dong {self.thue_nk()} thue nhap khau")
    def __str__(self):
        return f"San pham: {self.__ten_sp} co gia {self.__gia} duoc giam {self.__giam_gia} va phai dong {self.thue_nk()} thue nhap khau"
    
# sp1 = sanpham("beer", 20000, 10000)
# print(sp1.doc_giam_gia())
# print(sp1.ghi_giam_gia(10000))
# sp1.xuat_tt_sp()

