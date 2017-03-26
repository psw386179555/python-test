import tkinter as tk
from tkinter import messagebox
from tkinter import *

# 输出txt文本数据
def writeToTxt(list_name,file_path):
    try:
        fp = open(file_path,"w+")
        for item in list_name:
            fp.write(str(item)+"\n")
        fp.close()
        print("sucess to open file")
    except IOError:
        print("fail to open file")


# 窗口开始       
window=tk.Tk()
window.title('传热学编程作业')
window.iconbitmap('D:\\python\\s.ico') #设置窗口图标
window.geometry('800x600')
l=tk.Label(window,text='本应用程序由流体1401彭思文制作，请按照要求输入对应的内容，',bg='white',font=('Arail',12),width=100,height=2)
l.pack()

def do_About():
     messagebox.showinfo(title='关于',message='本应用程序由流体1401彭思文制作，如遇任何问题请联系qq386179555')
#菜单栏
menubar = Menu(window) #当前窗口创建菜单栏
filemenu = Menu(menubar, tearoff=0) #菜单栏位置
filemenu.add_command(label="New", command=do_About)  #子目录
filemenu.add_command(label="Open", command=do_About)
filemenu.add_command(label="Save", command=do_About)
filemenu.add_command(label="Save as...", command=do_About)
filemenu.add_command(label="Close", command=do_About)

filemenu.add_separator()#分割线

filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu) #添加大目录

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=do_About)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=do_About)
editmenu.add_command(label="Copy", command=do_About)
editmenu.add_command(label="Paste", command=do_About)
editmenu.add_command(label="Delete", command=do_About)
editmenu.add_command(label="Select All", command=do_About)

menubar.add_cascade(label="Edit", menu=editmenu) #添加第二大目录
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=do_About)
helpmenu.add_command(label="关于...", command=do_About)
menubar.add_cascade(label="Help", menu=helpmenu)

window.config(menu=menubar)#设置菜单

# 定义需要获取的值
var_x_divide=tk.StringVar()
var_y_divide=tk.StringVar()
var_restrain=tk.StringVar()
var_diedainum=tk.StringVar()
var_text_notice=tk.StringVar()


# 设置输入框
tk.Label(window,text='x-分度( 正整数 ):').place(x=20,y=50)
tk.Label(window,text='y-分度( 正整数 ):').place(x=20,y=100)
tk.Label(window,text='收敛误差(例如：10e-6 ):').place(x=20,y=150)


entry_x_divide = tk.Entry(window,textvariable=var_x_divide)
entry_x_divide.place(x=200,y=50)

entry_y_divide = tk.Entry(window,textvariable=var_y_divide)
entry_y_divide.place(x=200,y=100)

entry_restrain = tk.Entry(window,textvariable=var_restrain)
entry_restrain.place(x=200,y=150)


# listbox
var_arr=tk.StringVar()
var_arr.set(('这里显示数据','计算结果分行显示'))
lb=tk.Listbox(window,listvariable=var_arr,width=60)
lb.place(x=350,y=50)

# 计算数据        
def calculate():
    x=var_x_divide.get() #获得x等分数
    y=var_y_divide.get() #获得y等分数
    d=var_restrain.get() #获得收敛误差
    if (x and y and d) :
        pass
    else :
        messagebox.showinfo(title='提示',message='请输入数据')
        return 0
    if (x.isdigit() and y.isdigit()):
         pass
    else:
        messagebox.showerror(title='错误',message='非法数据类型')        
        return 0 
    if 0<float(d)<1:
        pass
    else:
        messagebox.showerror(title='错误',message='收敛误差必须在0-1之间')        
        return 0
    x=int(x)+1 #获取循环的次数，表示点
    y=int(y)+1 #获取循环的次数，表示点
    d=float(d) #输入的收敛误差
    
    m=float(0) #收敛误差
    k=int(0)   #迭代次数
    all=[]     #上个数组
    arr= [None]*x 
    for i in range(len(arr)):  
        arr[i] = [0]*y
    for j in range(len(arr[0])):
        arr[0][j]=100
    #初始化数组
    e=[None]*x
    for i in range(len(e)):  
        e[i] = [1]*y
        e[i][0] = 0
        e[i][y-1] = 0
    for j in range(len(e[0])):
        e[0][j]=100
        e[x-1][j]=0
    #初始化用于储存上个数组的数组
    while 1:
        for i in range(1,x-1):
            for j in range(1,y-1):
                arr[i][j]=float((arr[i-1][j]+arr[i][j-1]+arr[i][j+1]+arr[i+1][j]))/4            
                m=abs((arr[i][j]-e[i][j]))/e[i][j]
                e[i][j]=float((arr[i-1][j]+arr[i][j-1]+arr[i][j+1]+arr[i+1][j]))/4
                all.append(m)               
        if all :
            m=max(all)
            if m<d:          
                break
        all=[]
        k=k+1
    # 迭代
    writeToTxt(arr,"data.txt") #输出文本
    var_arr.set(arr)           #程序端输出数据
    var_diedainum.set(k)       #程序端输出迭代次数
    var_text_notice.set('在同一目录下已经生成data.txt文件！')

# 设置计算按钮
btn_calculate=tk.Button(window,text='Calculate',command=calculate)
btn_calculate.place(x=100,y=200)
tk.Label(window,text='迭代次数为:').place(x=20,y=250)
tk.Label(window,textvariable=var_diedainum,font=('Arail',24)).place(x=100,y=250)

tk.Label(window,textvariable=var_text_notice,font=('Arail',24)).place(x=20,y=300)

window.mainloop()
