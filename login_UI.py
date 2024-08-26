import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.font as font
import csv
import os

# 창 생성
window = tk.Tk()
window.title("4조")
window.geometry("260x130")  # 창 크기 조정
window.resizable(False, False)  # 창 크기 고정


def login():
    # 입력한 아이디와 비밀번호 가져오기
    entered_id = id_entry.get()
    entered_password = password_entry.get()

    # 아이디와 비밀번호 확인
    if entered_id == "관리자" and entered_password == "1":
        # 로그인 성공 메시지 표시
        messagebox.showinfo("로그인 성공", "로그인에 성공했습니다.")
        # 로그인 창 닫기
        window.destroy()
        # 새창열기
        open_new_window()
        # 프레임 붙이기
        create_frames()
    else:
        # 로그인 실패 메시지 표시
        messagebox.showerror("로그인 실패", "아이디 또는 비밀번호가 올바르지 않습니다.")
        # 비밀번호 틀린 횟수 체크
        check_password_attempts()

def open_new_window():
    global new_window
    new_window = tk.Tk()
    new_window.title("환영합니다")
    new_window.geometry("1200x440")  # 창 크기 조정
    new_window.resizable(False, False)

# 비밀번호 틀린 횟수 체크 함수
def check_password_attempts():
    global password_attempts
    password_attempts += 1
    if password_attempts >= 5:
        messagebox.showerror("비밀번호 오류", "비밀번호를 5번 틀렸습니다. 프로그램을 종료합니다.")
        window.destroy()

# 아이디 입력 레이블 및 엔트리
id_label = ttk.Label(window, text="아이디:")
id_label.pack()
id_entry = ttk.Entry(window)
id_entry.pack()

# 비밀번호 입력 레이블 및 엔트리
password_label = ttk.Label(window, text="비밀번호:")
password_label.pack()
password_entry = ttk.Entry(window, show="*")  # 비밀번호 입력 시 *로 표시
password_entry.pack()

# 로그인 버튼
login_button = ttk.Button(window, text="로그인", command=login)
login_button.pack()

# 비밀번호 틀린 횟수 초기화
password_attempts = 0

# Frame 생성 함수
def create_frames():
    left_frame = tk.Frame(new_window, width=400, height=440, bg="lightgrey")
    left_frame.grid(row=0, column=0, sticky="n")

    # 가운데 프레임 생성
    center_frame = tk.Frame(new_window, width=300, height=440)
    center_frame.grid(row=0, column=1, sticky="n")

    # 가운데 프레임을 위와 아래로 나누는 프레임 생성
    top_center_frame = tk.Frame(center_frame, width=300, height=220, bg="white")
    top_center_frame.pack(side="top")

    bottom_center_frame = tk.Frame(center_frame, width=300, height=220, bg="white")
    bottom_center_frame.pack(side="bottom")

    def list_files_in_folder(folder_path):
        file_list = []
        for file_name in os.listdir(folder_path):
            if os.path.isfile(os.path.join(folder_path, file_name)):
                file_list.append(file_name)
        return file_list

    folder_path = r'C:\Users\sr48g\OneDrive\바탕 화면\hansol\monthly_income_outcome'
    monthListfiles = list_files_in_folder(folder_path) # 월별 가져오기
    
    file_names_without_extension = [file_name[:-4] for file_name in monthListfiles]

    def centerFrameScrollbar() :    
        scrollbar = tk.Scrollbar(top_center_frame)
        scrollbar.pack(side='right',fill='y')

        listbox=tk.Listbox(top_center_frame,yscrollcommand = scrollbar.set, selectbackground='yellow', selectforeground='black')

        yearMonthList = file_names_without_extension # 월별 가져오기

        for line in yearMonthList :
            listbox.insert(tk.END,line)
        listbox.pack(side='left')

        scrollbar['command']=listbox.yview

        return scrollbar, listbox


    # 오른쪽 프레임 내부 상단 프레임 생성
    right_frame = tk.Frame(new_window, width=400, height=440)
    right_frame.grid(row=0, column=2)


    # 오른쪽 프레임을 위와 아래로 나누는 프레임 생성
    top_right_frame = tk.Frame(right_frame, width=400, height=220, bg="yellow")
    top_right_frame.pack(side="top")

    bottom_right_frame = tk.Frame(right_frame, width=400, height=320, bg="orange")
    bottom_right_frame.pack(side="bottom")

    def cal_tax():
        tax_calculation_label.config(text='가게 매출, 지출에 대해 세금계산을 시작합니다.')

    def cal_tax_advice():
        tax_advice_label.config(text='tax_saving_advice 함수를 실행합니다.')

    taxCalButton = tk.Button(top_right_frame, width=7, anchor='n', text='세금 계산', command=cal_tax)
    taxCalButton.pack()

    taxAdviceButton = ttk.Button(top_right_frame, width=7, text="세금 절약 방법", command=cal_tax_advice)
    taxAdviceButton.pack()   

    tax_calculation_label = ttk.Label(bottom_right_frame, text="", font=font.Font(family="휴먼명조", size=14))
    tax_calculation_label.pack()

    tax_advice_label = ttk.Label(bottom_right_frame, text="", font=font.Font(family="휴먼명조", size=14))
    tax_advice_label.pack()


    # 왼쪽 프레임에 목록을 표시할 Listbox 위젯 생성
    listbox = tk.Listbox(left_frame, width=30, height=20, selectbackground='yellow', selectforeground='black', font=font.Font(family="휴먼명조", size=18))

    # 목록 추가
    with open(r'C:\Users\sr48g\OneDrive\바탕 화면\hansol\monthly_income_outcome\2023년.csv', 'r', encoding='utf-8') as storeFile:
        csvReader = csv.reader(storeFile)
        i=0
        for storeList in csvReader:
           listbox.insert(i,storeList[0])
           i += 1
    
    listbox.delete(0)
    listbox.pack(fill=tk.BOTH, padx=10, pady=10)


    def on_listbox_select(event):
        global store_name, sales, expenses # 전역함수 지정
        selected_store = listbox.get(listbox.curselection())

        if len(listbox.curselection()) > 0:
            scrollbar, _ = centerFrameScrollbar()
            listbox['yscrollcommand'] = scrollbar.set  # 스크롤바와 리스트박스 연동
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        else:
            scrollbar, _ = centerFrameScrollbar()
            scrollbar.pack_forget()

        store_name = selected_store
        sales, expenses = find_store_info(store_name)
        
        if sales and expenses:
            selected_label.config(text=f"{store_name}의 매출: {int(sales):>10,}원\n{store_name}의 지출: {int(expenses):>10,}원", font=font.Font(family="휴먼명조", size=14))
        else:
            selected_label.config(text=f"{store_name}에 대한 정보를 찾을 수 없습니다.", font=font.Font(family="휴먼명조", size=14))


    def find_store_info(store_name):
        with open(r'C:\Users\sr48g\OneDrive\바탕 화면\hansol\monthly_income_outcome\2023년.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # 첫 번째 줄(헤더) 패스
            for row in reader:
                if row[0] == store_name:
                    return row[1], row[2]
        
        return None, None  # 가게명에 해당하는 정보가 없을 경우 None을 반환


     # 가게를 클릭했을 때 이벤트 처리 함수
    listbox.bind("<<ListboxSelect>>", on_listbox_select)

    selected_label = ttk.Label(center_frame, text="선택된 가게", font=font.Font(family="휴먼명조", size=14))
    selected_label.pack()
   
    # center_frame 내부에 selected_label을 위치시키기 위해 place를 사용
    selected_label.place(relx=0.5, rely=0.8, anchor="s")


    new_window.mainloop()


window.mainloop()
