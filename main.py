# coding:utf-8
import os
import random
import PIL.Image as PImage
from PIL import ImageFont, ImageDraw
from id_card import IdCard

try:
    from Tkinter import *
    from ttk import *
    from tkFileDialog import *
    from tkMessageBox import *
except ImportError:
    from tkinter import *
    from tkinter.ttk import *
    from tkinter.filedialog import *
    from tkinter.messagebox import *

if getattr(sys, 'frozen', None):
    base_dir = os.path.join(sys._MEIPASS, 'resource')
else:
    base_dir = os.path.join(os.path.dirname(__file__), 'resource')


def generator():
    global ename, esex, enation, eyear, emon, eday, eaddr, eidn, eorg, elife, ebgvar, template, export_path, avatar
    name = ename.get()
    sex = esex.get()
    nation = enation.get()
    year = eyear.get()
    mon = emon.get()
    day = eday.get()
    org = eorg.get()
    life = elife.get()
    addr = eaddr.get()
    idn = eidn.get()

    # 人像
    # fname = askopenfilename(initialdir=os.getcwd(), title=u'选择头像')
    # avatar = PImage.open(fname)  # 500x670
    random_file_name = str(random.randint(1, 17)) + '.png'
    file_url = os.path.join(base_dir, random_file_name)
    avatar = PImage.open(file_url)

    # print fname
    # im = PImage.open(os.path.join(base_dir, 'empty.png'))
    # 省份证模板
    im = PImage.open(os.path.join(base_dir, template.get()))

    name_font = ImageFont.truetype(os.path.join(base_dir, 'hei.ttf'), 72)
    other_font = ImageFont.truetype(os.path.join(base_dir, 'hei.ttf'), 60)
    bdate_font = ImageFont.truetype(os.path.join(base_dir, 'fzhei.ttf'), 60)
    id_font = ImageFont.truetype(os.path.join(base_dir, 'ocrb10bt.ttf'), 72)

    draw = ImageDraw.Draw(im)
    draw.text((630, 690), name, fill=(0, 0, 0), font=name_font)
    draw.text((630, 840), sex, fill=(0, 0, 0), font=other_font)
    draw.text((1030, 840), nation, fill=(0, 0, 0), font=other_font)
    draw.text((630, 980), year, fill=(0, 0, 0), font=bdate_font)
    draw.text((950, 980), mon, fill=(0, 0, 0), font=bdate_font)
    draw.text((1150, 980), day, fill=(0, 0, 0), font=bdate_font)
    start = 0
    loc = 1120
    while start + 11 < len(addr):
        draw.text((630, loc), addr[start:start + 11], fill=(0, 0, 0), font=other_font)
        start += 11
        loc += 100
    draw.text((630, loc), addr[start:], fill=(0, 0, 0), font=other_font)
    draw.text((950, 1475), idn, fill=(0, 0, 0), font=id_font)
    draw.text((1050, 2750), org, fill=(0, 0, 0), font=other_font)
    draw.text((1050, 2895), life, fill=(0, 0, 0), font=other_font)

    avatar = avatar.resize((500, 670))
    avatar = avatar.convert('RGBA')
    im.paste(avatar, (1500, 690), mask=avatar)

    clor = os.path.join(export_path.get(), name + 'idCard_color.png')
    # bw = os.path.join(export_path.get(), name + 'idCard_bw.png')
    im.save(clor)
    # im.convert('L').save(bw)

    showinfo(u'成功', f'文件已生成到{export_path.get()}目录下,黑白bw.png和彩色color.png')


def getImg(filename, width, height):
    im = PImage.open(filename).resize((width, height))
    return im


def refresh_IdCard():
    global ename, esex, enation, eyear, emon, eday, eaddr, eidn, eorg, elife, ebgvar, template, export_path, avatar
    card_info = IdCard()

    ename.delete(0, END)
    ename.insert(0, card_info.name)

    esex.delete(0, END)
    esex.insert(0, card_info.sex)

    enation.delete(0, END)
    enation.insert(0, card_info.ethnic)

    eyear.delete(0, END)
    eyear.insert(0, card_info.birthday[0])

    emon.delete(0, END)
    emon.insert(0, card_info.birthday[1])

    eday.delete(0, END)
    eday.insert(0, card_info.birthday[2])

    eaddr.delete(0, END)
    eaddr.insert(0, card_info.address)

    eidn.delete(0, END)
    eidn.insert(0, card_info.idNum)

    eorg.delete(0, END)
    eorg.insert(0, card_info.visaOffice)

    elife.delete(0, END)
    elife.insert(0, card_info.validPeriod)


def run():
    global ename, esex, enation, eyear, emon, eday, eaddr, eidn, eorg, elife, ebgvar, template, export_path, avatar
    root = Tk()
    root.title(u'身份证图片生成器 请遵守法律法规')
    # root.geometry('640x480')
    root.resizable(width=False, height=False)

    card_info = IdCard()

    Label(root, text=u'姓名:').grid(row=0, column=0, sticky=W, padx=3, pady=3)
    ename = Entry(root, width=8)
    ename.grid(row=0, column=1, sticky=W, padx=3, pady=3)
    ename.insert(0, card_info.name)

    Label(root, text=u'性别:').grid(row=0, column=2, sticky=W, padx=3, pady=3)
    esex = Entry(root, width=8)
    esex.grid(row=0, column=3, sticky=W, padx=3, pady=3)
    esex.insert(0, card_info.sex)

    Label(root, text=u'民族:').grid(row=0, column=4, sticky=W, padx=3, pady=3)
    enation = Entry(root, width=8)
    enation.grid(row=0, column=5, sticky=W, padx=3, pady=3)
    enation.insert(0, card_info.ethnic)

    Label(root, text=u'出生年:').grid(row=1, column=0, sticky=W, padx=3, pady=3)
    eyear = Entry(root, width=8)
    eyear.grid(row=1, column=1, sticky=W, padx=3, pady=3)
    eyear.insert(0, card_info.birthday[0])

    Label(root, text=u'月:').grid(row=1, column=2, sticky=W, padx=3, pady=3)
    emon = Entry(root, width=8)
    emon.grid(row=1, column=3, sticky=W, padx=3, pady=3)
    emon.insert(0, card_info.birthday[1])

    Label(root, text=u'日:').grid(row=1, column=4, sticky=W, padx=3, pady=3)
    eday = Entry(root, width=8)
    eday.grid(row=1, column=5, sticky=W, padx=3, pady=3)
    eday.insert(0, card_info.birthday[2])

    Label(root, text=u'住址:').grid(row=2, column=0, sticky=W, padx=3, pady=3)
    eaddr = Entry(root, width=32)
    eaddr.grid(row=2, column=1, sticky=W, padx=3, pady=3, columnspan=5)
    eaddr.insert(0, card_info.address)

    Label(root, text=u'证件号码:').grid(row=3, column=0, sticky=W, padx=3, pady=3)
    eidn = Entry(root, width=32)
    eidn.grid(row=3, column=1, sticky=W, padx=3, pady=3, columnspan=5)
    eidn.insert(0, card_info.idNum)

    Label(root, text=u'签发机关:').grid(row=4, column=0, sticky=W, padx=3, pady=3)
    eorg = Entry(root, width=32)
    eorg.grid(row=4, column=1, sticky=W, padx=3, pady=3, columnspan=5)
    eorg.insert(0, card_info.visaOffice)

    Label(root, text=u'有效期限:').grid(row=5, column=0, sticky=W, padx=3, pady=3)
    elife = Entry(root, width=32)
    elife.grid(row=5, column=1, sticky=W, padx=3, pady=3, columnspan=5)
    elife.insert(0, card_info.validPeriod)

    Label(root, text=u'模板:').grid(row=6, column=0, sticky=W, padx=3, pady=3)
    template = StringVar()
    template.set('empty.png')
    Radiobutton(root, text=u'普通', variable=template, value='empty.png').grid(row=6, column=1, sticky=W, padx=3, pady=3)
    Radiobutton(root, text=u'少数民族', variable=template, value='empty2.png').grid(row=6, column=2, sticky=W, padx=3,
                                                                                pady=3)

    Label(root, text=u'导出路径:').grid(row=8, column=0, sticky=W, padx=3, pady=3)
    export_path = Entry(root, width=45)
    export_path.insert(0, os.path.dirname(os.getcwd()))
    export_path.grid(row=8, column=1, sticky=W, padx=3, pady=3, columnspan=5)

    Button(root, text=u'刷新', width=10, command=refresh_IdCard).grid(row=9, column=1, sticky=W, padx=1, pady=3,
                                                                    columnspan=2)
    Button(root, text=u'生成', width=10, command=generator).grid(row=9, column=3, sticky=W, padx=3, pady=3, columnspan=3)

    root.mainloop()


if __name__ == '__main__':
    run()
