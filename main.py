#coding=utf-8
import sys,os,time

ffmpegpath = os.path.join(os.getcwd(),r"ffmpeg\bin\ffmpeg.exe")
#检测是否有文件丢失
def check():
    if os.path.exists(ffmpegpath):
        text ="批量avi 转 mp4工具\n"
        text +="免费分享，禁止贩卖\n"
        text +="BY 小莫 - https://mod.3dmgame.com/u/9688990\n"
        text += "程序初始化完成！\n"
        text +="=============================================\n"
        print(text)

        return True
    else:
        print("未找到ffmpeg.exe,请确保已将所有文件解压出来！")
        return False
#执行转换
def pic_webp(avi_file_path,Export_path):
    cmd = os.popen("{ffmpeg} -y -i {input} -vcodec h264 -acodec aac -strict -2 {output}.mp4".format(ffmpeg = ffmpegpath,input = avi_file_path, output = Export_path))
    print(cmd.read())
#开始程序
def Start():
    path = input("请输入avi视频文件夹路径：")
    Export_path = input("请输入导出路径:")
    for (dirpath,dirname,dirfile) in os.walk(path):
        for fileName in dirfile:			#遍历目录所有文件
            try:
                #print(fileName)
                fileType = fileName.split(".")[-1]
                if fileType in ["avi"]:	#判断文件类型
                    #print("正在转换："+fileName + "...")
                    avi_file_path = os.path.join(dirpath,fileName)
                    pic_webp(avi_file_path,os.path.join(Export_path,fileName.split(".")[0]))			#执行转换函数
            except IOError as e:
                    print("文件"+fileName+"转换失败")
                    print("错误:"+str(e))
#欢迎界面
def welcome():
    text = "  /$$$$$$  /$$$$$$$  /$$      /$$       /$$      /$$                 /$$          \n"
    text+= " /$$__  $$| $$__  $$| $$$    /$$$      | $$$    /$$$                | $$          \n"
    text+= "|__/  \ $$| $$  \ $$| $$$$  /$$$$      | $$$$  /$$$$  /$$$$$$   /$$$$$$$  /$$$$$$$\n"
    text+= "   /$$$$$/| $$  | $$| $$ $$/$$ $$      | $$ $$/$$ $$ /$$__  $$ /$$__  $$ /$$_____/\n"
    text+= "  |___  $$| $$  | $$| $$  $$$| $$      | $$  $$$| $$| $$  \ $$| $$  | $$|  $$$$$$ \n"
    text+= " /$$  \ $$| $$  | $$| $$\  $ | $$      | $$\  $ | $$| $$  | $$| $$  | $$ \____  $$\n"
    text+= "|  $$$$$$/| $$$$$$$/| $$ \/  | $$      | $$ \/  | $$|  $$$$$$/|  $$$$$$$ /$$$$$$$/\n"
    text+= " \______/ |_______/ |__/     |__/      |__/     |__/ \______/  \_______/|_______/ \n"
    print(text)

welcome()
if  check():
    Start()
    YorN = input("视频转换完成,是否继续转换?(Y/N)")
    if YorN == "Y" or YorN =="y":
        Start()
else:
    print("程序结束")
    time.sleep(5)