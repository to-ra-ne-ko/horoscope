import sys
import os
sys.dont_write_bytecode = True  # do not make '__cache__'
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msg
import json
import requests
import datetime

li_places = [
    '牡羊座 ♈', '牡牛座 ♉', '双子座 ♊︎', '蟹座 ♋',   '獅子座 ♌', '乙女座 ♍',
    '天秤座 ♎︎', '蠍座 ♏',   '射手座 ♐', '山羊座 ♑', '水瓶座 ♒', '魚座 ♓'
]
str_today = datetime.datetime.now().strftime("%Y/%m/%d") # 'ex) 2025/01/15'

url_h = "http://api.jugemkey.jp/api/horoscope/free/"
url = url_h + str_today
res = requests.get(url)
result = json.loads(res.text)

print(type(res))
print(res)
print(type(result))
print(result)

def make_star(num1:int=0):
    return f'{"★"*num1}{"☆"*(5-num1)}'

# 占い結果を取得する関数を作る
def get_uranai(num1):
    # '''任意の星座（どれでもいい）の結果を辞書型で取得して表示する関数'''
    zodiac=int(num1)
    view_uranai(result['horoscope'][str_today][zodiac] , zodiac )

def view_uranai(dic , zodiac):
    '''辞書型の引数を受け取りキー["content"]の内容を(とりあえずprint文で出力する)'''
    global Label0,Text01,Label1,Label2,Label3,Label4,Label5,Label6,Label7
    global img, onchan
    # global canvas


    print(dic)
    str1=f"結果 ： {dic['sign']}"
    Label0=tk.Label(root,text=str1,bg="lightcyan")
    Label0.pack()

    texttitle=f"本日の占い♪　{str_today} {str1}のあなたは・・・？"
    root.title(texttitle)

    # p_dir='image/'
    # p_dir='date/0116/image/'
    p_file_list = [
        'seiza_mark01_ohitsuji.png',
        'seiza_mark02_oushi.png',
        'seiza_mark03_futago.png',
        'seiza_mark04_kani.png',
        'seiza_mark05_shishi.png',
        'seiza_mark06_otome.png',
        'seiza_mark07_tenbin.png',
        'seiza_mark08_sasori.png',
        'seiza_mark09_ite.png',
        'seiza_mark10_yagi.png',
        'seiza_mark11_mizugame.png',
        'seiza_mark12_uo.png' ]
    img_path = p_dir + p_file_list[zodiac]

    onchan = tk.PhotoImage(file=img_path)
    onchan = onchan.subsample(4) # resize
    img=tk.Label(root,image=onchan)
    img['bg'] = root['bg'] # lightgray clear
    img.pack()

    str1=dic['content']
    Text01=tk.Text(root,bg="lightcyan", height=5, width=50)
    Text01.insert(0., str1)
    Text01.pack(pady=5)

    str1=f"ラッキーアイテム ： {dic['item']}"
    Label1=tk.Label(root,text=str1,bg="lightcyan")
    Label1.pack()

    str1=f"ラッキーカラー ： {dic['color']}"
    Label2=tk.Label(root,text=str1,bg="lightcyan")
    Label2.pack()

    str1=f"仕事運 ： {make_star(dic['job'])}"
    Label3=tk.Label(root,text=str1,bg="lightcyan")
    Label3.pack()

    str1=f"恋愛運 ： {make_star(dic['love'])}"
    Label4=tk.Label(root,text=str1,bg="lightcyan")
    Label4.pack()

    str1=f"金運 ： {make_star(dic['money'])}"
    Label5=tk.Label(root,text=str1,bg="lightcyan")
    Label5.pack()

    str1=f"トータル ： {make_star(dic['total'])}"
    Label6=tk.Label(root,text=str1,bg="lightcyan")
    Label6.pack()

    str1=f"ランク ： {dic['rank']}"
    Label7=tk.Label(root,text=str1,bg="lightcyan")
    Label7.pack()

    make_return()

# すべてのボタンを消す関数
def clear_btn(event,num1):
    for val in btn_list:
        # print(f"delete {val}")
        # val.destroy()
        # print(f"pack_forget {val}")
        # val.pack_forget()
        # print(f"place_forget {val}")
        val.place_forget()
    # print(f"clear_btn  num1={num1}")
    get_uranai(num1)

def make_btn():
    # for val in btn_list:
    #     print(f"make {val}")
    #     val.pack()
    for i in range(len(btn_list)):
        # btn.pack()
        i_x=145*(i%3)+10
        i_y=(i//3)*100+10
        # print(f"i={i} x={i_x} y={i_y}")
        btn_list[i].place(x=i_x,y=i_y,width=140,height=95)

def make_return():
    '''もどるボタンを表示する'''
    global button_back
    str1="もどる" 
    button_back = tk.Button(root,text=str1,font=32,bg="lightgray")
    button_back.bind("<1>", back_main)
    button_back.pack()

def back_main(event):
    '''スタート画面に戻る'''
    del_list = [button_back,Label0,Text01,Label1,Label2,Label3,Label4,Label5,Label6,Label7,img]
    for btn in del_list:
        btn.destroy()

    texttitle=f"本日の占い♪　{str_today}"
    root.title(texttitle)

    # 次に生む
    make_btn()

p_dir  = 'image/'
p_file = 'image/seiza_mark01_ohitsuji.png'

if os.path.isdir(p_dir):
    print(f"1_1_OK")
    pass
else:
    print(f"{p_dir}が見つかりません。")
    p_dir  = 'date/0116/image/'
    p_file = 'date/0116/image/seiza_mark01_ohitsuji.png'
    if os.path.isdir(p_dir):
        print(f"1_2_OK")
        pass
    else:
        print(f"1_2_NG : {p_dir}が見つかりません。")
        msg.showwarning('メッセージ', f"{p_dir}が見つかりません。")    #「警告」のメッセージボックス
        sys.exit()

if os.path.isfile(p_file):
    print(f"2_1_OK")
    pass
else:
    print(f"2_1?NG : {p_file}が見つかりません。")
    p_dir  = 'date/0116/image/'
    p_file = 'date/0116/image/seiza_mark01_ohitsuji.png'
    if os.path.isfile(p_file):
        print(f"2_2_OK")
        pass
    else:
        print(f"2_2_NG : {p_file}が見つかりません。")
        msg.showwarning('メッセージ', f"{p_file}が見つかりません。")    #「警告」のメッセージボックス
        sys.exit()

root=tk.Tk()
root.configure(bg="lightcyan")
texttitle=f"本日の占い♪　{str_today}"
root.title(texttitle)
gx,gy=448,418
root.minsize(gx,gy)
# root.withdraw() #隠す

str1=li_places[0]
button00 = tk.Button(root,text=str1,font=32,bg="lightgray")
button00.bind("<1>", lambda event:clear_btn(event,0) )
# button00.pack()

str1=li_places[1]
button01 = tk.Button(root,text=str1,font=32,bg="lightgray")
button01.bind("<1>", lambda event:clear_btn(event,1) )
# button01.pack()

str1=li_places[2]
button02 = tk.Button(root,text=str1,font=32,bg="lightgray")
button02.bind("<1>", lambda event:clear_btn(event,2) )
# button02.pack()

str1=li_places[3]
button03 = tk.Button(root,text=str1,font=32,bg="lightgray")
button03.bind("<1>", lambda event:clear_btn(event,3) )
# button03.pack()

str1=li_places[4]
button04 = tk.Button(root,text=str1,font=32,bg="lightgray")
button04.bind("<1>", lambda event:clear_btn(event,4) )
# button04.pack()

str1=li_places[5]
button05 = tk.Button(root,text=str1,font=32,bg="lightgray")
button05.bind("<1>", lambda event:clear_btn(event,5) )
# button05.pack()

str1=li_places[6]
button06 = tk.Button(root,text=str1,font=32,bg="lightgray")
button06.bind("<1>", lambda event:clear_btn(event,6) )
# button06.pack()

str1=li_places[7]
button07 = tk.Button(root,text=str1,font=32,bg="lightgray")
button07.bind("<1>", lambda event:clear_btn(event,7) )
# button07.pack()

str1=li_places[8]
button08 = tk.Button(root,text=str1,font=32,bg="lightgray")
button08.bind("<1>", lambda event:clear_btn(event,8) )
# button08.pack()

str1=li_places[9]
button09 = tk.Button(root,text=str1,font=32,bg="lightgray")
button09.bind("<1>", lambda event:clear_btn(event,9) )
# button09.pack()

str1=li_places[10]
button10 = tk.Button(root,text=str1,font=32,bg="lightgray")
button10.bind("<1>", lambda event:clear_btn(event,10) )
# button10.pack()

str1=li_places[11]
button11 = tk.Button(root,text=str1,font=32,bg="lightgray")
button11.bind("<1>", lambda event:clear_btn(event,11) )
# button11.pack()

btn_list=[button00,button01,button02,button03,button04,button05,button06,button07,button08,button09,button10,button11]

make_btn()

root.mainloop()
