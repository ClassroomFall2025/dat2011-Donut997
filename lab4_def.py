#bài 1

def tinh_tien_nuoc(so_nuoc):
    gia_ban_nuoc = (7500, 8800, 12000, 24000)
    if 0 <= so_nuoc <= 10:
        tien_thang = so_nuoc * gia_ban_nuoc[0]
    elif so_nuoc <= 20:
        tien_thang = 10 * gia_ban_nuoc[0] + (so_nuoc - 10) * gia_ban_nuoc[1]
    elif so_nuoc <= 30:
        tien_thang = 10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + (so_nuoc - 20) * gia_ban_nuoc[2]
    else:
        tien_thang = 10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + 10 * gia_ban_nuoc[2] + (so_nuoc - 30) * gia_ban_nuoc[3]
    return tien_thang

#bài 2
def tinh_nguyen_lieu(sl_bdx, sl_btc, sl_bd):
    dau_xanh = {"???ng": 0.04, "??u": 0.07}
    thap_cam = {"???ng": 0.06, "??u": 0}
    banh_deo = {"???ng": 0.05, "??u": 0.02}
    nguyen_lieu = {}
    duong = sl_bdx * dau_xanh ["???ng"] + sl_btc * thap_cam["???ng"] + sl_bd * banh_deo["???ng"]
    dau = sl_bdx * dau_xanh ["??u"] + sl_btc * thap_cam["??u"] + sl_bd * banh_deo["??u"]
    nguyen_lieu ["???ng"] = duong
    nguyen_lieu ["??u"] = dau
    return nguyen_lieu