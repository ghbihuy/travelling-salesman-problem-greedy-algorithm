from PyQt5 import QtGui, QtWidgets
from app_nguoi_du_lich import Ui_QMainWindow
from PyQt5.QtGui import QTransform
from PyQt5.QtCore import QLineF, QRectF
import os
import math

class app_ui(Ui_QMainWindow):
    def __init__(self, Mainwindow) -> None:
        self.setupUi(Mainwindow)
        
class run():
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.appUI = QtWidgets.QMainWindow()
        self.app = app_ui(self.appUI)
        self.appUI.show()
        self.map = {}
        self.toado = {}
        self.khu_vuc = ""
        self.thanh_pho_xuat_phat = ""
        self.pixmap = None
        self.co_xuat_phat = None
        self.x_bd = 0
        self.y_bd = 0
        self.x_xp = 0
        self.y_xp = 0
        self.x_kt = 0
        self.y_kt = 0
        # Chỉnh không cho người dùng nhập vào bảng thông báo
        self.app.thongbao.setReadOnly(True)
        #Tạo các nút trên map
        #nút trên map tây bắc
        self.map_tay_bac_nut = QtWidgets.QButtonGroup()
        self.map_tay_bac_nut.addButton(self.app.nut_lao_cai)
        self.map_tay_bac_nut.addButton(self.app.nut_dien_bien)
        self.map_tay_bac_nut.addButton(self.app.nut_hoa_binh)
        self.map_tay_bac_nut.addButton(self.app.nut_lai_Chau)
        self.map_tay_bac_nut.addButton(self.app.nut_son_la)
        self.map_tay_bac_nut.addButton(self.app.nut_yen_bai)
        self.map_tay_bac_nut.setExclusive(False)
        #nút trên máp đông bắc bộ
        self.map_dong_bac_bo = QtWidgets.QButtonGroup()
        self.map_dong_bac_bo.addButton(self.app.nut_bac_giang)
        self.map_dong_bac_bo.addButton(self.app.nut_bac_kan)
        self.map_dong_bac_bo.addButton(self.app.nut_ha_giang)
        self.map_dong_bac_bo.addButton(self.app.nut_cao_bang)
        self.map_dong_bac_bo.addButton(self.app.nut_tuyen_quang)
        self.map_dong_bac_bo.addButton(self.app.nut_lang_son)
        self.map_dong_bac_bo.addButton(self.app.nut_thai_nguyen)
        self.map_dong_bac_bo.addButton(self.app.nut_quang_ninh)
        self.map_dong_bac_bo.addButton(self.app.nut_phu_tho)
        self.map_dong_bac_bo.setExclusive(False)
        #nút trên đông bằng sông hồng
        self.map_dbh = QtWidgets.QButtonGroup()
        self.map_dbh.addButton(self.app.nut_vinh_phuc)
        self.map_dbh.addButton(self.app.nut_bac_ninh)
        self.map_dbh.addButton(self.app.nut_hai_duong)
        self.map_dbh.addButton(self.app.nut_hai_phong)
        self.map_dbh.addButton(self.app.nut_ha_noi)
        self.map_dbh.addButton(self.app.nut_hung_yen)
        self.map_dbh.addButton(self.app.nut_thai_binh)
        self.map_dbh.addButton(self.app.nut_ha_nam)
        self.map_dbh.addButton(self.app.nut_nam_dinh)
        self.map_dbh.addButton(self.app.nut_ninh_binh)
        self.map_dbh.setExclusive(False)
        #nút trên bắc trung bộ
        self.map_btb = QtWidgets.QButtonGroup()
        self.map_btb.addButton(self.app.nut_ha_tinh)
        self.map_btb.addButton(self.app.nut_nghe_an)
        self.map_btb.addButton(self.app.nut_quang_binh)
        self.map_btb.addButton(self.app.nut_quang_tri)
        self.map_btb.addButton(self.app.nut_thanh_hoa)
        self.map_btb.addButton(self.app.nut_thua_thien_hue)
        self.map_btb.setExclusive(False)
        #nút trên nam trung bộ
        self.map_ntb = QtWidgets.QButtonGroup()
        self.map_ntb.addButton(self.app.nut_binh_dinh)
        self.map_ntb.addButton(self.app.nut_binh_thuan)
        self.map_ntb.addButton(self.app.nut_da_nang)
        self.map_ntb.addButton(self.app.nut_khanh_hoa)
        self.map_ntb.addButton(self.app.nut_ninh_thuan)
        self.map_ntb.addButton(self.app.nut_phu_yen)
        self.map_ntb.addButton(self.app.nut_quang_nam)
        self.map_ntb.addButton(self.app.nut_quang_ngai)
        self.map_ntb.setExclusive(False)
        #nút trên đông nam bộ
        self.map_dnb = QtWidgets.QButtonGroup()
        self.map_dnb.addButton(self.app.nut_binh_duong)
        self.map_dnb.addButton(self.app.nut_binh_phuoc)
        self.map_dnb.addButton(self.app.nut_dong_nai)
        self.map_dnb.addButton(self.app.nut_hcm)
        self.map_dnb.addButton(self.app.nut_tay_ninh)
        self.map_dnb.addButton(self.app.nut_vung_tau)
        self.map_dnb.setExclusive(False)
        #nut đồng bằng sông cửa long
        self.map_dbscl = QtWidgets.QButtonGroup()
        self.map_dbscl.addButton(self.app.nut_an_giang)
        self.map_dbscl.addButton(self.app.nut_bac_lieu)
        self.map_dbscl.addButton(self.app.nut_ben_tre)
        self.map_dbscl.addButton(self.app.nut_ca_mau)
        self.map_dbscl.addButton(self.app.nut_can_tho)
        self.map_dbscl.addButton(self.app.nut_dong_thap)
        self.map_dbscl.addButton(self.app.nut_hau_giang)
        self.map_dbscl.addButton(self.app.nut_kien_giang)
        self.map_dbscl.addButton(self.app.nut_long_an)
        self.map_dbscl.addButton(self.app.nut_soc_trang)
        self.map_dbscl.addButton(self.app.nut_tien_giang)
        self.map_dbscl.addButton(self.app.nut_tra_vinh)
        self.map_dbscl.addButton(self.app.nut_vinh_long)
        self.map_dbscl.setExclusive(False)
        #nút trên tây nguyên
        self.map_tn = QtWidgets.QButtonGroup()
        self.map_tn.addButton(self.app.nut_dak_lak)
        self.map_tn.addButton(self.app.nut_dak_nong)
        self.map_tn.addButton(self.app.nut_gia_lai)
        self.map_tn.addButton(self.app.nut_kon_tum)
        self.map_tn.addButton(self.app.nut_lam_dong)
        self.map_tn.setExclusive(False)
       
        #chọn miền
        self.app.choose_TBB.toggled.connect(lambda: self.chon_mien(self.app.Tay_Bac_Anh, "Tây Bắc", self.app.input_TB, self.app.Tay_Bac, os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), "images"), "tây bắc.jpg"), self.map_tay_bac_nut))
        self.app.choose_DBB_2.toggled.connect(lambda: self.chon_mien(self.app.dong_bac_bo_anh, "Đông Bắc Bộ", self.app.input_DBB, self.app.dong_bac_bo, os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), "images"), "Đông bắc bộ.jpg"), self.map_dong_bac_bo))
        self.app.choose_DBSH.toggled.connect(lambda: self.chon_mien(self.app.DBSH_anh, "DBSH", self.app.input_DBSH, self.app.DBSH, os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), "images"), "DBSH.jpg"), self.map_dbh))
        self.app.choose_BTB.toggled.connect(lambda: self.chon_mien(self.app.Bac_Trung_bo_anh, "Bắc Trung Bộ", self.app.input_BTB, self.app.Bac_Trung_bo, os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), "images"), "BTB.jpg"), self.map_btb))
        self.app.choose_NTB.toggled.connect(lambda: self.chon_mien(self.app.Nam_Trung_bo_anh, "Nam Trung Bộ", self.app.input_NTB, self.app.Nam_Trung_bo, os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), "images"), "Nam Trung Bộ.jpg"), self.map_ntb))
        self.app.choose_DNB.toggled.connect(lambda: self.chon_mien(self.app.Dong_Nam_Bo_anh, "Đông Nam Bộ", self.app.input_DNB, self.app.Dong_Nam_Bo, os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), "images"), "Đông Nam Bộ.jpg"), self.map_dnb))
        self.app.choose_DBSCL.toggled.connect(lambda: self.chon_mien(self.app.DBSCL_anh, "DBSCL", self.app.input_DBSCL, self.app.DBSCL, os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), "images"), "DBSCL.jpg"), self.map_dbscl))
        self.app.choose_TN.toggled.connect(lambda: self.chon_mien(self.app.Tay_Nguyen_Anh, "Tây Nguyên", self.app.input_TN, self.app.Tay_Nguyen, os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), "images"), "Tây nguyên.jpg"), self.map_tn))
        
        #chọn thành phố miền bắc
        self.app.Luu.clicked.connect(self.chon_thanh_pho)
        #chay
        self.app.run_button.clicked.connect(lambda: self.greedy_best_firts_search(self.thanh_pho_xuat_phat, self.map))                    
        
    def drawsomething(self, x_bd, y_bd, x_kt, y_kt, mau, chiphi):
        #Lấy ảnh để vẽ
        self.pixmap.setScaledContents(False)
        pixmap = self.pixmap.pixmap()
        pixmap_size = self.pixmap.pixmap().size()
        
        #Vẽ đường
        #Chuyển tọa độ từ label sang pixmap
        x_bd_on_pixmap = int(x_bd * pixmap_size.width()/self.pixmap.size().width()) + 10
        y_bd_on_pixmap = int(y_bd * pixmap_size.height()/self.pixmap.size().height()) - 8
        x_kt_on_pixmap = int(x_kt * pixmap_size.width()/self.pixmap.size().width()) + 10
        y_kt_on_pixmap = int(y_kt * pixmap_size.height()/self.pixmap.size().height()) - 8
        #Cài đặt thông số để vẽ đường
        painter = QtGui.QPainter(pixmap)
        pen = QtGui.QPen()
        pen.setWidth(5)
        pen.setColor(QtGui.QColor(mau))
        painter.setPen(pen)
        painter.drawLine(x_bd_on_pixmap, y_bd_on_pixmap, x_kt_on_pixmap, y_kt_on_pixmap)
        
        #Vẽ chữ
        #Cài đặt thông số để vẽ chữ
        font = QtGui.QFont("Arial", 12)
        painter.setFont(font)
        text = str(chiphi)
        #Tính toán độ xoay sau cho chữ vẽ trên và nằm giữa đường thẳng
        line = QLineF(x_bd_on_pixmap, y_bd_on_pixmap, x_kt_on_pixmap, y_kt_on_pixmap)
        text_width = painter.fontMetrics().width(text)
        text_height = painter.fontMetrics().height()
        dx = line.x2() - line.x1()
        dy = line.y2() - line.y1()
        angle = math.degrees(math.atan2(dy, dx)) + 180
        #Xoay hình vẽ và vẽ chữ
        transform = QTransform()
        transform.translate((line.x1() + line.x2()) / 2, (line.y1() + line.y2()) / 2)
        transform.rotate(angle)
        painter.setTransform(transform)
        painter.drawText(QRectF(-text_width / 2, -text_height / 2 - 15, text_width, text_height), text)
        painter.end()
        #Update sự thay đổi về hình ảnh
        self.pixmap.setPixmap(pixmap)
        self.pixmap.setScaledContents(True)
        
    def chon_mien(self, anh, khu_vuc, input, trang, link, nut):
        #Làm mới số liệu
        self.map = {}
        self.toado = {}
        self.khu_vuc = khu_vuc
        self.thanh_pho_xuat_phat = ""
        self.x_bd = 0
        self.y_bd = 0
        self.x_kt = 0
        self.y_kt = 0
        
        #Làm mới giao diện
        self.app.thongbao.clear()
        self.pixmap = anh
        self.pixmap.clear()
        self.pixmap.setPixmap(QtGui.QPixmap(link))
        for button in nut.buttons():
            button.setChecked(False)                    
        
        #Chuyển Trang
        self.app.dieukhien.setCurrentWidget(self.app.page_2)
        self.app.input.setCurrentWidget(input)
        self.app.Map.setCurrentWidget(trang)
        
    def chon_thanh_pho(self):
        self.app.thongbao.clear()
        tp = list(self.map.keys())
        thanh_pho_bat_dau = ""
        thanh_pho_ket_thuc = ""
        chiphi = int(self.app.tcp.toPlainText())
        
        #khu vực Tây bắc 
        if self.khu_vuc == "Tây Bắc":
            thanh_pho_bat_dau = self.app.tinh_di_tb_2.currentText()
            thanh_pho_ket_thuc = self.app.tinh_ve_tb_3.currentText()
            self.thanh_pho_xuat_phat = self.app.tinh_xp_tb.currentText()
            if thanh_pho_bat_dau == thanh_pho_ket_thuc:
                self.app.thongbao.setText("2 tỉnh đi và về không được trùng nhau")
            if thanh_pho_bat_dau == "Lào Cai" or thanh_pho_ket_thuc == "Lào Cai" or self.thanh_pho_xuat_phat == "Lào Cai":
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Lào Cai", self.app.nut_lao_cai)
            if thanh_pho_bat_dau == "Lai Châu" or thanh_pho_ket_thuc == "Lai Châu" or self.thanh_pho_xuat_phat == "Lai Châu":
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Lai Châu", self.app.nut_lai_Chau)
            if thanh_pho_bat_dau == "Yên Bái" or thanh_pho_ket_thuc == "Yên Bái" or self.thanh_pho_xuat_phat == "Yên Bái":
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Yên Bái", self.app.nut_yen_bai)                
            if thanh_pho_bat_dau == "Điện Biên" or thanh_pho_ket_thuc == "Điện Biên" or self.thanh_pho_xuat_phat == "Điện Biên":
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Điện Biên", self.app.nut_dien_bien)                                              
            if thanh_pho_bat_dau == "Sơn La" or thanh_pho_ket_thuc == "Sơn La" or self.thanh_pho_xuat_phat == "Sơn La":
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Sơn La", self.app.nut_son_la)
            if thanh_pho_bat_dau == "Hòa Bình" or thanh_pho_ket_thuc == "Hòa Bình" or self.thanh_pho_xuat_phat == "Hòa Bình" : 
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Hòa Bình", self.app.nut_hoa_binh)
        
        #Khu vực đông bắc bộ        
        elif self.khu_vuc == "Đông Bắc Bộ":
            thanh_pho_bat_dau = self.app.tinh_di_DBB.currentText()
            thanh_pho_ket_thuc = self.app.tinh_ve_DBB.currentText()
            self.thanh_pho_xuat_phat = self.app.tinh_xp_DBB.currentText()
            if thanh_pho_bat_dau == thanh_pho_ket_thuc:
                self.app.thongbao.setText("2 tỉnh đi và về không được trùng nhau")
            if thanh_pho_bat_dau == "Hà Giang" or thanh_pho_ket_thuc == "Hà Giang" or self.thanh_pho_xuat_phat == "Hà Giang":
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Hà Giang", self.app.nut_ha_giang)
            if thanh_pho_bat_dau == 'Cao Bằng' or thanh_pho_ket_thuc == 'Cao Bằng' or self.thanh_pho_xuat_phat == 'Cao Bằng':
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, 'Cao Bằng', self.app.nut_cao_bang)
            if thanh_pho_bat_dau == 'Bắc Kạn' or thanh_pho_ket_thuc == 'Bắc Kạn' or self.thanh_pho_xuat_phat == 'Bắc Kạn':
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, 'Bắc Kạn', self.app.nut_bac_kan)                
            if thanh_pho_bat_dau == "Tuyên Quang" or thanh_pho_ket_thuc == "Tuyên Quang" or self.thanh_pho_xuat_phat == "Tuyên Quang":
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Tuyên Quang", self.app.nut_tuyen_quang)                                              
            if thanh_pho_bat_dau == "Phú Thọ" or thanh_pho_ket_thuc == "Phú Thọ"or self.thanh_pho_xuat_phat =="Phú Thọ":
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Phú Thọ", self.app.nut_phu_tho)
            if thanh_pho_bat_dau == "Lạng Sơn" or thanh_pho_ket_thuc == "Lạng Sơn"or self.thanh_pho_xuat_phat =="Lạng Sơn": 
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Lạng Sơn", self.app.nut_lang_son)
            if thanh_pho_bat_dau == "Thái Nguyên" or thanh_pho_ket_thuc == "Thái Nguyên"or self.thanh_pho_xuat_phat =="Thái Nguyên": 
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Thái Nguyên", self.app.nut_thai_nguyen)
            if thanh_pho_bat_dau == "Bắc Giang" or thanh_pho_ket_thuc == "Bắc Giang"or self.thanh_pho_xuat_phat =="Bắc Giang": 
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Bắc Giang", self.app.nut_bac_giang)
            if thanh_pho_bat_dau == "Quảng Ninh" or thanh_pho_ket_thuc == "Quảng Ninh"or self.thanh_pho_xuat_phat =="Quảng Ninh": 
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Quảng Ninh", self.app.nut_quang_ninh)
        
        #Khu vực DBSH
        elif self.khu_vuc == "DBSH":
            thanh_pho_bat_dau = self.app.tinh_di_DBSH.currentText()
            thanh_pho_ket_thuc = self.app.tinh_ve_DBSH.currentText()
            self.thanh_pho_xuat_phat = self.app.tinh_xp_DBSH.currentText()
            if thanh_pho_bat_dau == thanh_pho_ket_thuc:
                self.app.thongbao.setText("2 tỉnh đi và về không được trùng nhau")
            if thanh_pho_bat_dau == "Hà Nội" or thanh_pho_ket_thuc == "Hà Nội"or self.thanh_pho_xuat_phat =="Hà Nội": 
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Hà Nội", self.app.nut_ha_noi)
            if thanh_pho_bat_dau == "Vĩnh Phúc" or thanh_pho_ket_thuc == "Vĩnh Phúc"or self.thanh_pho_xuat_phat =="Vĩnh Phúc": 
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Vĩnh Phúc", self.app.nut_vinh_phuc)
            if thanh_pho_bat_dau == "Bắc Ninh" or thanh_pho_ket_thuc == "Bắc Ninh"or self.thanh_pho_xuat_phat =="Bắc Ninh": 
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Bắc Ninh", self.app.nut_bac_ninh)
            if thanh_pho_bat_dau == "Hải Dương" or thanh_pho_ket_thuc == "Hải Dương"or self.thanh_pho_xuat_phat =="Hải Dương": 
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Hải Dương", self.app.nut_hai_duong)
            if thanh_pho_bat_dau == "Hưng Yên" or thanh_pho_ket_thuc == "Hưng Yên"or self.thanh_pho_xuat_phat =="Hưng Yên": 
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Hưng Yên", self.app.nut_hung_yen)
            if thanh_pho_bat_dau == "Hà Nam" or thanh_pho_ket_thuc == "Hà Nam"or self.thanh_pho_xuat_phat =="Hà Nam": 
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Hà Nam", self.app.nut_ha_nam)
            if thanh_pho_bat_dau == "Hải Phòng" or thanh_pho_ket_thuc == "Hải Phòng"or self.thanh_pho_xuat_phat =="Hải Phòng": 
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Hải Phòng", self.app.nut_hai_phong)
            if thanh_pho_bat_dau == "Thái Bình" or thanh_pho_ket_thuc == "Thái Bình"or self.thanh_pho_xuat_phat =="Thái Bình": 
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Thái Bình", self.app.nut_thai_binh)
            if thanh_pho_bat_dau == "Nam Định" or thanh_pho_ket_thuc == "Nam Định"or self.thanh_pho_xuat_phat =="Nam Định": 
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Nam Định", self.app.nut_nam_dinh)
            if thanh_pho_bat_dau == "Ninh Bình" or thanh_pho_ket_thuc == "Ninh Bình"or self.thanh_pho_xuat_phat =="Ninh Bình": 
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Ninh Bình", self.app.nut_ninh_binh)
        
        #Khu vực Bắc Trung Bộ
        elif self.khu_vuc == "Bắc Trung Bộ":
            thanh_pho_bat_dau = self.app.tinh_di_BTB.currentText()
            thanh_pho_ket_thuc = self.app.tinh_ve_BTB.currentText()
            self.thanh_pho_xuat_phat = self.app.tinh_xp_BTB.currentText()
            if thanh_pho_bat_dau == thanh_pho_ket_thuc:
                self.app.thongbao.setText("2 tỉnh đi và về không được trùng nhau")
            if thanh_pho_bat_dau == "Thanh Hóa" or thanh_pho_ket_thuc == "Thanh Hóa"or self.thanh_pho_xuat_phat =="Thanh Hóa": 
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Thanh Hóa", self.app.nut_thanh_hoa)
            if thanh_pho_bat_dau == "Nghệ An" or thanh_pho_ket_thuc == "Nghệ An"or self.thanh_pho_xuat_phat =="Nghệ An": 
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Nghệ An", self.app.nut_nghe_an)
            if thanh_pho_bat_dau == "Hà Tĩnh" or thanh_pho_ket_thuc == "Hà Tĩnh"or self.thanh_pho_xuat_phat =="Hà Tĩnh": 
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Hà Tĩnh", self.app.nut_ha_tinh)
            if thanh_pho_bat_dau == "Quảng Bình" or thanh_pho_ket_thuc == "Quảng Bình"or self.thanh_pho_xuat_phat =="Quảng Bình": 
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Quảng Bình", self.app.nut_quang_binh)
            if thanh_pho_bat_dau == "Quảng Trị" or thanh_pho_ket_thuc == "Quảng Trị"or self.thanh_pho_xuat_phat =="Quảng Trị": 
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Quảng Trị", self.app.nut_quang_tri)
            if thanh_pho_bat_dau == "Thừa Thiên Huế" or thanh_pho_ket_thuc == "Thừa Thiên Huế"or self.thanh_pho_xuat_phat =="Thừa Thiên Huế": 
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Thừa Thiên Huế", self.app.nut_thua_thien_hue)
        
        # khu vực Nam trung bộ         
        elif self.khu_vuc == "Nam Trung Bộ":
            thanh_pho_bat_dau = self.app.tinh_di_NTB.currentText()
            thanh_pho_ket_thuc = self.app.tinh_ve_NTB.currentText()
            self.thanh_pho_xuat_phat = self.app.tinh_xp_NTB.currentText()
            if thanh_pho_bat_dau == thanh_pho_ket_thuc:
                self.app.thongbao.setText("2 tỉnh đi và về không được trùng nhau")
            if thanh_pho_bat_dau == "Đà Nẵng" or thanh_pho_ket_thuc == "Đà Nẵng"or self.thanh_pho_xuat_phat =="Đà Nẵng": 
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Đà Nẵng", self.app.nut_da_nang)    
            if thanh_pho_bat_dau == "Quảng Nam" or thanh_pho_ket_thuc == "Quảng Nam"or self.thanh_pho_xuat_phat =="Quảng Nam": 
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Quảng Nam", self.app.nut_quang_nam)    
            if thanh_pho_bat_dau == "Quảng Ngãi" or thanh_pho_ket_thuc == "Quảng Ngãi"or self.thanh_pho_xuat_phat =="Quảng Ngãi": 
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Quảng Ngãi", self.app.nut_quang_ngai)    
            if thanh_pho_bat_dau == "Bình Định" or thanh_pho_ket_thuc == "Bình Định"or self.thanh_pho_xuat_phat =="Bình Định": 
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Bình Định", self.app.nut_binh_dinh)    
            if thanh_pho_bat_dau == "Phú Yên" or thanh_pho_ket_thuc == "Phú Yên"or self.thanh_pho_xuat_phat =="Phú Yên": 
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Phú Yên", self.app.nut_phu_yen)    
            if thanh_pho_bat_dau == "Khánh Hòa" or thanh_pho_ket_thuc == "Khánh Hòa"or self.thanh_pho_xuat_phat =="Khánh Hòa": 
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Khánh Hòa", self.app.nut_khanh_hoa)    
            if thanh_pho_bat_dau == "Ninh Thuận" or thanh_pho_ket_thuc == "Ninh Thuận"or self.thanh_pho_xuat_phat =="Ninh Thuận": 
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Ninh Thuận", self.app.nut_ninh_thuan)    
            if thanh_pho_bat_dau == "Bình Thuận" or thanh_pho_ket_thuc == "Bình Thuận"or self.thanh_pho_xuat_phat =="Bình Thuận": 
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Bình Thuận", self.app.nut_binh_thuan)
            
        # Khu vực Đông Nam Bộ
        elif self.khu_vuc == "Đông Nam Bộ":
            thanh_pho_bat_dau = self.app.tinh_di_DNB.currentText()
            thanh_pho_ket_thuc = self.app.tinh_ve_DNB_2.currentText()
            self.thanh_pho_xuat_phat = self.app.tinh_xp_DNB.currentText()
            if thanh_pho_bat_dau == thanh_pho_ket_thuc:
                self.app.thongbao.setText("2 tỉnh đi và về không được trùng nhau")
            if thanh_pho_bat_dau == "Tây Ninh" or thanh_pho_ket_thuc == "Tây Ninh" or self.thanh_pho_xuat_phat == "Tây Ninh":
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Tây Ninh", self.app.nut_tay_ninh)
            if thanh_pho_bat_dau == "Bình Dương" or thanh_pho_ket_thuc == "Bình Dương" or self.thanh_pho_xuat_phat == "Bình Dương":
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Bình Dương", self.app.nut_binh_duong)
            if thanh_pho_bat_dau == "Bình Phước" or thanh_pho_ket_thuc == "Bình Phước" or self.thanh_pho_xuat_phat == "Bình Phước":
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Bình Phước", self.app.nut_binh_phuoc)                
            if thanh_pho_bat_dau == "Đồng Nai" or thanh_pho_ket_thuc == "Đồng Nai" or self.thanh_pho_xuat_phat == "Đồng Nai":
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Đồng Nai", self.app.nut_dong_nai)                                              
            if thanh_pho_bat_dau == "TP. Hồ Chí Minh" or thanh_pho_ket_thuc == "TP. Hồ Chí Minh" or self.thanh_pho_xuat_phat == "TP. Hồ Chí Minh":
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "TP. Hồ Chí Minh", self.app.nut_hcm)
            if thanh_pho_bat_dau == "Bà Rịa -Vũng Tàu" or thanh_pho_ket_thuc == "Bà Rịa -Vũng Tàu" or self.thanh_pho_xuat_phat == "Bà Rịa -Vũng Tàu":
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Bà Rịa -Vũng Tàu", self.app.nut_vung_tau)
        
        # Khu vực đồng bằng sông cửu long
        elif self.khu_vuc == "DBSCL":
            thanh_pho_bat_dau = self.app.tinh_di_DBSCL.currentText()
            thanh_pho_ket_thuc = self.app.tinh_ve_DBSCL.currentText()
            self.thanh_pho_xuat_phat = self.app.tinh_xp_DBSCL.currentText()
            if thanh_pho_bat_dau == thanh_pho_ket_thuc:
                self.app.thongbao.setText("2 tỉnh đi và về không được trùng nhau")
            if thanh_pho_bat_dau == "An Giang" or thanh_pho_ket_thuc == "An Giang" or self.thanh_pho_xuat_phat == "An Giang":
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "An Giang", self.app.nut_an_giang)
            if thanh_pho_bat_dau == "Bạc Liêu" or thanh_pho_ket_thuc == "Bạc Liêu" or self.thanh_pho_xuat_phat == "Bạc Liêu":
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Bạc Liêu", self.app.nut_bac_lieu)
            if thanh_pho_bat_dau == "Bến Tre" or thanh_pho_ket_thuc == "Bến Tre" or self.thanh_pho_xuat_phat == "Bến Tre":
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Bến Tre", self.app.nut_ben_tre)                
            if thanh_pho_bat_dau == "Cà Mau" or thanh_pho_ket_thuc == "Cà Mau" or self.thanh_pho_xuat_phat == "Cà Mau":
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Cà Mau", self.app.nut_ca_mau)                                              
            if thanh_pho_bat_dau == "Cần Thơ" or thanh_pho_ket_thuc == "Cần Thơ" or self.thanh_pho_xuat_phat == "Cần Thơ":
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Cần Thơ", self.app.nut_can_tho)
            if thanh_pho_bat_dau == "Đồng Tháp" or thanh_pho_ket_thuc == "Đồng Tháp" or self.thanh_pho_xuat_phat == "Đồng Tháp":
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Đồng Tháp", self.app.nut_dong_thap)                
            if thanh_pho_bat_dau == "Hậu Giang" or thanh_pho_ket_thuc == "Hậu Giang" or self.thanh_pho_xuat_phat == "Hậu Giang":
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Hậu Giang", self.app.nut_hau_giang)                                              
            if thanh_pho_bat_dau == "Kiên Giang" or thanh_pho_ket_thuc == "Kiên Giang" or self.thanh_pho_xuat_phat == "Kiên Giang":
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Kiên Giang", self.app.nut_kien_giang)
            if thanh_pho_bat_dau == "Long An" or thanh_pho_ket_thuc == "Long An" or self.thanh_pho_xuat_phat == "Long An":
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Long An", self.app.nut_long_an)
            if thanh_pho_bat_dau == "Sóc Trăng" or thanh_pho_ket_thuc == "Sóc Trăng" or self.thanh_pho_xuat_phat == "Sóc Trăng":
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Sóc Trăng", self.app.nut_soc_trang)
            if thanh_pho_bat_dau == "Tiền Giang" or thanh_pho_ket_thuc == "Tiền Giang" or self.thanh_pho_xuat_phat == "Tiền Giang":
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Tiền Giang", self.app.nut_tien_giang)
            if thanh_pho_bat_dau == "Trà Vinh" or thanh_pho_ket_thuc == "Trà Vinh" or self.thanh_pho_xuat_phat == "Trà Vinh":
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Trà Vinh", self.app.nut_tra_vinh)
            if thanh_pho_bat_dau == "Vĩnh Long" or thanh_pho_ket_thuc == "Vĩnh Long" or self.thanh_pho_xuat_phat == "Vĩnh Long":
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Vĩnh Long", self.app.nut_vinh_long)
                
        # Khu vực Tây Nguyên
        else:
            thanh_pho_bat_dau = self.app.tinh_di_TN.currentText()
            thanh_pho_ket_thuc = self.app.tinh_ve_TN.currentText()
            self.thanh_pho_xuat_phat = self.app.tinh_xp_TN.currentText()
            if thanh_pho_bat_dau == thanh_pho_ket_thuc:
                self.app.thongbao.setText("2 tỉnh đi và về không được trùng nhau")
            if thanh_pho_bat_dau == "Đắk Lắk" or thanh_pho_ket_thuc == "Đắk Lắk" or self.thanh_pho_xuat_phat == "Đắk Lắk":
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Đắk Lắk", self.app.nut_dak_lak)
            if thanh_pho_bat_dau == "Đắk Nông" or thanh_pho_ket_thuc == "Đắk Nông" or self.thanh_pho_xuat_phat == "Đắk Nông":
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Đắk Nông", self.app.nut_dak_nong)
            if thanh_pho_bat_dau == "Gia Lai" or thanh_pho_ket_thuc == "Gia Lai" or self.thanh_pho_xuat_phat == "Gia Lai":
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Gia Lai", self.app.nut_gia_lai)                
            if thanh_pho_bat_dau == "Kon Tum" or thanh_pho_ket_thuc == "Kon Tum" or self.thanh_pho_xuat_phat == "Kon Tum":
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Kon Tum", self.app.nut_kon_tum)                                              
            if thanh_pho_bat_dau == "Lâm Đồng" or thanh_pho_ket_thuc == "Lâm Đồng" or self.thanh_pho_xuat_phat == "Lâm Đồng":
                self.lay_toa_do(thanh_pho_bat_dau, thanh_pho_ket_thuc, "Lâm Đồng", self.app.nut_lam_dong)
                 
        #Out khi chưa đủ dữ liệu 
        if thanh_pho_bat_dau == "Chọn" or thanh_pho_ket_thuc == "Chọn" or self.thanh_pho_xuat_phat == "Chọn":
            return
        
        # Thêm thành phố vào map
        if thanh_pho_bat_dau in tp or thanh_pho_ket_thuc in tp:
            #Thêm thành phố vào dictionary trong trường hợp cả 2 đều nằm trong dictionary
            if thanh_pho_bat_dau in tp and thanh_pho_ket_thuc in tp:
                if self.check_input(thanh_pho_bat_dau, thanh_pho_ket_thuc) and self.check_input(thanh_pho_ket_thuc, thanh_pho_bat_dau):
                    self.app.thongbao.setText("Đã tồn tại trên hệ thống")
                    return
                tp_lien_ke_tinh_bat_dau = self.map[thanh_pho_bat_dau].copy()
                tp_lien_ke_tinh_ket_thuc = self.map[thanh_pho_ket_thuc].copy()
                self.them_tp_vao_map(thanh_pho_bat_dau, thanh_pho_ket_thuc, chiphi, tp_lien_ke_tinh_bat_dau)
                self.them_tp_vao_map(thanh_pho_ket_thuc, thanh_pho_bat_dau, chiphi, tp_lien_ke_tinh_ket_thuc)
                
            #Thêm thành phố vào dictionary trong trường hợp 1 trong 2 nằm trong dictionary                                            
            elif thanh_pho_bat_dau in tp and thanh_pho_ket_thuc not in tp:                    
                tp_lien_ke_tinh_bat_dau = self.map[thanh_pho_bat_dau]
                thanh_pho_ket_thuc = thanh_pho_ket_thuc
                tp_lien_ke = []
                self.them_tp_vao_map(thanh_pho_bat_dau, thanh_pho_ket_thuc, chiphi, tp_lien_ke_tinh_bat_dau)
                self.them_tp_vao_map(thanh_pho_ket_thuc, thanh_pho_bat_dau, chiphi, tp_lien_ke)                                     
            else:
                tp_lien_ke_tinh_ket_thuc = self.map[thanh_pho_ket_thuc]
                thanh_pho_bat_dau = thanh_pho_bat_dau
                tp_lien_ke = []
                self.them_tp_vao_map(thanh_pho_ket_thuc, thanh_pho_bat_dau, chiphi, tp_lien_ke_tinh_ket_thuc)
                self.them_tp_vao_map(thanh_pho_bat_dau, thanh_pho_ket_thuc, chiphi, tp_lien_ke)
 
        #Thêm thành phố vào dictionary trong trường hợp cả 2 đều không nằm trong dictionary                
        else:
            thanh_pho_bat_dau = thanh_pho_bat_dau
            thanh_pho_ket_thuc = thanh_pho_ket_thuc
            tp_lien_ke = []
            self.them_tp_vao_map(thanh_pho_bat_dau, thanh_pho_ket_thuc, chiphi, tp_lien_ke)
            self.them_tp_vao_map(thanh_pho_ket_thuc, thanh_pho_bat_dau, chiphi, tp_lien_ke) 
            
        #Chuyển tọa độ sao cho số luôn nằm về 1 phía
        if self.x_bd < self.x_kt:  
            self.toado[thanh_pho_bat_dau + "-" + thanh_pho_ket_thuc] = (self.x_kt, self.y_kt, self.x_bd, self.y_bd, chiphi)
            self.drawsomething(self.x_kt, self.y_kt, self.x_bd, self.y_bd, 'black', chiphi)                
        else:            
            self.toado[thanh_pho_bat_dau + "-" + thanh_pho_ket_thuc] = (self.x_bd, self.y_bd, self.x_kt, self.y_kt, chiphi)
            self.drawsomething(self.x_bd, self.y_bd, self.x_kt, self.y_kt, 'black', chiphi)    
    
    #Kiểm tra xem thông tin đưa vào có trong dictionary không        
    def check_input(self, thanh_pho_1, thanh_phi_2):
        for i in self.map[thanh_pho_1]:
            if thanh_phi_2 in i:
                return True        

    #Lấy tọa độ các radio button và bật khi chọn tỉnh thích hợp
    def lay_toa_do(self, thanh_pho_bat_dau, thanh_pho_ket_thuc, thanhpho, nut):
        if thanh_pho_bat_dau == "Chọn" or thanh_pho_ket_thuc == "Chọn" or self.thanh_pho_xuat_phat == "Chọn":
            self.app.thongbao.setText("Thiếu dữ liệu")
            return
        if thanh_pho_bat_dau == thanhpho and thanh_pho_ket_thuc != thanhpho: 
            nut.setChecked(True)
            self.x_bd = int(nut.pos().x())
            self.y_bd = int(nut.pos().y())
        if thanh_pho_bat_dau != thanhpho and thanh_pho_ket_thuc == thanhpho:
            nut.setChecked(True)
            self.x_kt = int(nut.pos().x())
            self.y_kt = int(nut.pos().y())   
    
    #Thêm 1 thành phố và chi phí vào 1 list có key của 1 thành phố khác
    def them_tp_vao_map(self, thanh_pho_bat_dau, thanh_pho_ket_thuc, chi_phi, tp_lien_ke):  
        tp_lien_ke = tp_lien_ke.copy()
        tp_lien_ke.append([thanh_pho_ket_thuc, chi_phi])
        self.map[thanh_pho_bat_dau] = tp_lien_ke.copy()
        tp_lien_ke.clear()

    #Hàm GBFS và cũng là hàm chạy chính của chương trình        
    def greedy_best_firts_search(self, begin, data):
        self.app.thongbao.clear()
        #Tạo ra danh sách no visited chứa danh sách các thành phố chưa ghé thăm
        no_visited = list(data.keys())
        #Nếu begin không nằm trong danh sách no visited thì in thông báo và kết thúc hàm xử lý
        if begin not in no_visited:
            self.app.thongbao.setText("Thành phố xuất phát không có trong lộ trình!!!!!")
            return
        #Tạo ra danh sách fringer mang ý nghĩa của 1 hàm đánh giá
        fringer = []
        #Tạo ra 1 danh sách lưu các điểm và chi phí đã ghé thăm
        close = []
        #Thêm giá trị chứa khoảng cách và begin vào danh sách
        fringer.append([(0, begin)])
        # 2 biến số dùng để chuyển hướng đoạn đường lớn thi đường đi ngắn nhất không liên thông đến điểm bắt đầu
        index_value_erroi_tc = 2
        fringer_index_vaule_tc = 1
        # 2 biến số dùng để chuyển hướng đoạn đường con nằm trên trường hợp đoạn đường lớn để duyệt hết mọi trường hợp
        index_value_erroi_cb = 2
        fringer_index_vaule_cb = 1
        # Chi phí
        q_d = 0
        # Vị trí con trỏ đang chỉ đến ở 1 phần tử trong fringer
        index = 0   
        
        try:
            while True:
                #Xếp theo thứ tự tăng dần, xóa phần tử đó ra khỏi no visited và lấy 1 tuple con đầu tiên trong 1 danh sách mẹ mà vị trí index đang trỏ đến trong fringer đưa vào close
                fringer[index].sort(reverse=False)
                tam = fringer[index][0]
                fringer[index].pop(0) 
                close.append(tam)
                no_visited.remove(tam[1])
                index = index + 1 

                #Thêm các điểm lân cận khác mà điểm đó nằm trong no visited
                if len(no_visited) != 0:
                    fringer.append([])
                    for i in range(len(data[tam[1]])):
                        if data[tam[1]][i][0] in no_visited:
                            fringer[index].append((data[tam[1]][i][-1], data[tam[1]][i][0]))
                            
                    #check xem điểm nằm cuối danh sách close hiện tại chứa các điểm nằm trong no visited không
                    """ 
                    Vì trong 1 số trường hợp điểm chưa kết thúc danh sách đã duyệt có những điểm lân cận không nằm trong no visited
                    Do đó cần kiểm tra nếu đúng thì xóa phần tử cuối cùng đã được thêm vào close chuyển đổi con trỏ của fringer và chạy tiếp
                    Vì fringer chứa các điểm chưa được duyệt nếu và đã dùng pop ở phía trên điểm duyệt tiếp theo sẽ khác
                    Ví dụ:
                    fringer [[A], [B, C, D]]
                    Nếu B có các điểm lân cận và các điểm đó không nằm trong no visited thì thêm vào [], con trỏ(index) từ 1 sang 2
                    fringer [[A], [C, D], []]
                    vì [] không có gì để xét xóa tất cả các danh sách từ index trở đi chuyển index vào số 1 rồi tiếp chạy
                    fringer [[A], [C, D]] và điểm xét tiếp theo là C và cứ tiếp tục như vậy
                    """
                    check_nut_cuoi_hien_tai = True
                    check_so = 0
                    #Kiểm tra xem các điểm lân cận của điểm cuối cùng trong close có nằm trong no visited không nếu có thì chuyển check_nut_cuoi_hien_tai thành false
                    for i in data[close[-1][-1]]:
                        if i[0] not in no_visited:
                            check_so += 1
                        if check_so == len(data[close[-1][-1]]):
                            check_nut_cuoi_hien_tai = False
                    #Nếu check_nut_cuoi_hien_tai là false thực hiện như mô tả trên        
                    if check_nut_cuoi_hien_tai == False:
                        no_visited = list(data.keys())
                        for i in range(1, len(fringer)):
                            if len(fringer[i]) == 0:
                                index = i - 1
                                break
                        del fringer[index + 1:]
                        del close[index:]
                        for i in close:
                            if i[1] in no_visited:
                                no_visited.remove(i[1])
                #Nếu đã duyệt qua xong danh sách chưa ghé thăm            
                else:
                    #Kiểm tra xem danh sách đã đến thăm điểm cuối cùng có liên thông đến điểm bắt đầu nếu không thì rẻ hướng
                    check = False         
                    for i in data[close[-1][1]]:
                        if i[0] == begin:
                            check = True
                            q_d = q_d + i[1]
                            break
                    #in ra kết quả và vẽ đè lên đường màu đỏ đường đi thấp nhất
                    if check == True:
                        text_edit2 = ""
                        for i in close:
                            text_edit2 = text_edit2 + i[1] + " - "
                            q_d = q_d + i[0]
                        text_edit2 = text_edit2 + begin + "\n"
                        self.app.thongbao.setText("Đã tìm thấy\n" + text_edit2 + "Tổng chi phí tối ưu nhất: " + str(q_d))
                        print(close)
                        list_toa_do = list(self.toado.keys())
                        for i in range(len(close)):
                            key = ""
                            key_toa_do_1 = ""
                            key_toa_do_2 = ""
                            try:
                                key_toa_do_1 = close[i][-1] + "-" + close[i+1][-1]
                                key_toa_do_2 = close[i+1][-1] + "-" + close[i][-1]
                            except:
                                key_toa_do_1 = close[i][-1] + "-" + close[0][-1]
                                key_toa_do_2 = close[0][-1] + "-" + close[i][-1]
                            if key_toa_do_1 in list_toa_do or key_toa_do_2 in list_toa_do:
                                if key_toa_do_1 in list_toa_do:
                                    key = key_toa_do_1
                                else:
                                    key = key_toa_do_2
                            self.drawsomething(self.toado[key][0], self.toado[key][1], self.toado[key][2], self.toado[key][3], 'red', self.toado[key][4])  
                        return
                    #Rẻ nhánh
                    else:
                        if len(fringer[index - index_value_erroi_tc]) == 0:
                            index_value_erroi_tc = index_value_erroi_tc + 1
                            fringer_index_vaule_tc = fringer_index_vaule_tc + 1
                            index, close, fringer, no_visited = self.chuyen_duong(index, data, index_value_erroi_tc, fringer_index_vaule_tc, close, no_visited, fringer)
                            index_value_erroi_cb = 2
                            fringer_index_vaule_cb = 1
                        else:
                            if len(fringer[index - index_value_erroi_cb]) == 0:
                                index_value_erroi_cb = index_value_erroi_cb + 1
                                fringer_index_vaule_cb = fringer_index_vaule_cb + 1
                            index, close, fringer, no_visited = self.chuyen_duong(index, data, index_value_erroi_cb, fringer_index_vaule_cb, close, no_visited, fringer)
        except:
            self.app.thongbao.setText("Bài toán không có chu trình hamilton không tìm được chi phí")
    #Hàm rẻ nhánh xóa và cài đặt lại trạng thái của close, no visited, index,...                
    def chuyen_duong(self, index, data, index_value_erroi, fringer_index_vaule, close, no_visited, fringer):
        index = index - index_value_erroi
        no_visited = list(data.keys())
        for i in close[:- index_value_erroi]:
            no_visited.remove(i[1])
        close = close[:-index_value_erroi]
        fringer = fringer[:-fringer_index_vaule]
        return index, close, fringer, no_visited
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    UI = run()
    app.exec_()