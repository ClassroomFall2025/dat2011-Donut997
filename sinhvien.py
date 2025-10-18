class SinhVienPoLy:
    def __init__(self, ten_sv, nganh):
        self.ten_sv = ten_sv
        self.nganh = nganh
    
    def get_diem():
        pass
    
    def get_hoc_luc(self):
        diem = self.get_diem()
        if diem < 5:
            return "Yếu"
        elif 5 <= diem < 7:
            return "Trung bình"
        elif 7 <= diem < 8:
            return "Khá"
        elif 8 <= diem < 9:
            return "Giỏi"
        else:
            return "Xuất sắc"

    def xuat(self):
        print(f"Tên: {self.ten_sv}, Ngành: {self.nganh}, Điểm: {self.get_diem():.2f}, Học lực: {self.get_hoc_luc()}")

class SinhVienIT(SinhVienPoLy):
    def __init__(self, ten_sv, java, html, css):
        super().__init__(ten_sv, "IT")
        self.java = java
        self.html = html
        self.css = css

    def get_diem(self):
        return (2 * self.java + self.html + self.css) / 4 

class SinhVienBiz(SinhVienPoLy):
    def __init__(self, ten_sv, marketing, sales):
        super().__init__(ten_sv, "Biz")
        self.marketing = marketing
        self.sales = sales

    def get_diem(self):
        return (2 * self.marketing + self.sales) / 3