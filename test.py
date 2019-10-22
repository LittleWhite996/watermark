import tkinter, win32api, win32con, pywintypes
from tkinter import *
import qrcode
from PIL import Image
from qrcode.constants import ERROR_CORRECT_H
def get_replicate_text(text):
    i, space, str1, str2 = 0, 30, "", ""
    while (i <= 5):
        str1 = str1 + text + " " * space
        i = i + 1
    str2 = " " * space + str1 + "\n\n\n\n"
    str1 = str1 + "\n\n\n\n"
    str1 = (str1 + str2) * 4
    return str1
def generateQRcode(data,imgFn):
    qr=qrcode.QRCode(version=20,error_correction=ERROR_CORRECT_H,box_size=3,border=2)
    qr.add_data(data)
    qr.make()
    # 创建二维码图片
    img = qr.make_image()
    imgW, imgH = img.size
    w1, h1 = map(lambda x: x // 4, img.size)
    # 要粘贴的自定义图片，生成缩略图
    im = Image.open(imgFn)
    imW, imH = im.size
    w1 = w1 if w1 < imW else imW
    h1 = h1 if h1 < imH else imH
    im = im.resize((w1, h1))
    # 在二维码上中间位置粘贴自定义图片
    img.paste(im, ((imgW - w1) // 2, (imgH - h1) // 2))
    # 保存二维码图片
    img.save('qrCode.png')
    return img
def main():
    data='北京艾科网信科技有限公司'
    img='img.png'
    root=tkinter.Tk()
    root.title('选择窗口')
    root.geometry("400x400")
    b1=tkinter.Button(root,text="明文水印",font=('华文行楷', 12), width=10, height=1,command=watermark())
    b2=tkinter.Button(root, text="二维码水印",font=('华文行楷', 12), width=10, height=1,command=watermark())
    b1.pack()
    b2.pack()
    # r1 = tkinter.Radiobutton(root, text='明文形式',  value='A', command=watermark(data,img,1))
    # r2 = tkinter.Radiobutton(root, text='二维码形式',  value='B', command=watermark(data,img,2))
    # r1.pack()
    # r2.pack()

    root.mainloop()
def watermark(data,img,option):
    root = tkinter.Tk()
    width = win32api.GetSystemMetrics(0)  # 获取屏幕宽度
    height = win32api.GetSystemMetrics(1)  # 获取屏幕高度
    root.overrideredirect(True)  # 隐藏显示框
    root.geometry("%sx%s+0+0" % (width, height))  # 设置窗口位置或大小
    root.lift()  # 置顶层
    root.wm_attributes("-topmost", True)  # 始终置顶层
    root.wm_attributes("-disabled", True)
    root.wm_attributes("-transparentcolor", "white")  # 白色背景透明
    hWindow = pywintypes.HANDLE(int(root.frame(), 16))
    exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT
    win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)
    if(option==1):
        text1 = get_replicate_text(data)
        label = tkinter.Label(root, text=text1, font=('华文行楷', '25'), fg='#d5d5d5', bg='white')
        label.pack(side=RIGHT)  # 显示
        root.mainloop()  # 循环
    else:
        generateQRcode(data, img)
        imga = tkinter.PhotoImage(file='qrCode.png')
        label = tkinter.Label(root, image=imga, font=('华文行楷', '25'), fg='#d5d5d5', bg='white')
        label.pack(side=RIGHT)  # 显示
        root.mainloop()  # 循环
def set_para():
    para={
        'data':"北京艾科网信科技有限公司",
        'img':'img.png',
        'option':1
    }
    return para
if __name__ == '__main__':
    parameters=set_para()
    data=parameters['data']
    img=parameters['img']
    option=parameters['option']
    watermark(data,img,option)

