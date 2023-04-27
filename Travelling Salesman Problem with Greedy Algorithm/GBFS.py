map = {
    'Hà Nội': [['Vĩnh Phúc', 5000], ['Hưng Yên', 6000], ['Hải Dương', 3000]],
    'Vĩnh Phúc': [['Hà Nội', 5000], ['Bắc Ninh', 8000]],
    'Hưng Yên': [['Hà Nội', 6000], ['Hải Dương', 3000], ['Thái Bình', 6000], ['Hải Phòng', 7000]],
    'Bắc Ninh': [['Vĩnh Phúc', 8000], ['Hải Dương', 9000], ['Hải Phòng', 6000]],
    'Hải Dương': [['Bắc Ninh', 9000], ['Hà Nội', 3000], ['Hưng Yên', 3000], ['Hải Phòng', 8000], ['Thái Bình', 7000]],
    'Hải Phòng':[['Hải Dương', 8000], ['Bắc Ninh', 6000], ['Hưng Yên', 7000]],
    'Thái Bình':[['Hải Dương', 7000], ['Hưng Yên', 6000]],
}

def greedy_best_firts_search(begin, data):
    
    #Tạo ra danh sách no visited chứa danh sách các thành phố chưa ghé thăm
    no_visited = list(data.keys())
    #Nếu begin không nằm trong danh sách no visited thì in thông báo và kết thúc hàm xử lý
    if begin not in no_visited:
        print("Thành phố xuất phát không có trong lộ trình!!!!!")
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
                            
            #Trường hợp đã duyệt qua xong danh sách chưa ghé thăm            
            if len(no_visited) == 0:
                check = False  
                #Kiểm tra xem danh sách đã đến thăm điểm cuối cùng có liên thông đến điểm bắt đầu nếu không thì rẻ hướng          
                for i in data[close[-1][1]]:
                    if i[0] == begin:
                        check = True
                        q_d = q_d + i[1]                    
                        break
                    
                #in ra kết quả nếu đúng                        
                if check == True:
                    print ("Đã tìm thấy")
                    for i in close:
                        print(i[1], end="  ")
                        q_d = q_d + i[0]
                    print(begin)
                    print("Tổng quảng đường tối ưu nhất: " + str(q_d))
                    print(close)
                    return
                #Thực hiện rẽ hướng nếu check sai, ý tưởng như mô tả ở phía trên
                else:
                    if len(fringer[index - index_value_erroi_tc]) == 0:
                        index_value_erroi_tc = index_value_erroi_tc + 1
                        fringer_index_vaule_tc = fringer_index_vaule_tc + 1
                        index, close, fringer, no_visited = chuyen_duong(index, data, index_value_erroi_tc, fringer_index_vaule_tc, close, no_visited, fringer)
                        index_value_erroi_cb = 2
                        fringer_index_vaule_cb = 1
                    else:
                        if len(fringer[index - index_value_erroi_cb]) == 0:
                            index_value_erroi_cb = index_value_erroi_cb + 1
                            fringer_index_vaule_cb = fringer_index_vaule_cb + 1
                        index, close, fringer, no_visited = chuyen_duong(index, data, index_value_erroi_cb, fringer_index_vaule_cb, close, no_visited, fringer)
    except:
        print("Bài toán không có chu trình hamilton không tìm được đường đi")

#Hàm rẻ nhánh xóa và cài đặt lại trạng thái của close, no visited, index,...                                    
def chuyen_duong(index, data, index_value_erroi, fringer_index_vaule, close, no_visited, fringer):
    index = index - index_value_erroi
    no_visited = list(data.keys())
    for i in close[:- index_value_erroi]:
        no_visited.remove(i[1])
    close = close[:-index_value_erroi]
    fringer = fringer[:-fringer_index_vaule]
    return index, close, fringer, no_visited
        
if __name__ == "__main__": 
    greedy_best_firts_search('Vĩnh Phúc', map)
        