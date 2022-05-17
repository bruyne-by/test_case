from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

class Tests:
    def openVideoApp(self):
        poco(text="华为视频").click()
        try:
            poco("com.huawei.himovie:id/hiad_skip_text").click()
        except:
            pass
        sleep(secs=3)
        poco.swipe([0.3, 0.8], [0.3, 0.2], duration=0.5)
        poco.swipe([0.3, 0.2], [0.3, 0.8], duration=0.5)
        poco("综艺").click()
        poco("android.widget.FrameLayout").offspring("com.huawei.himovie:id/recycler_view_pager").child(
            "com.huawei.himovie:id/item_view")[1].child("com.huawei.himovie:id/mall_adimage").click()

        sleep(secs=5)
        keyevent("BACK")
        keyevent("HOME")
        sleep(secs=2)

    def openMusicApp(self):
        poco(text="音乐").click()
        try:
            poco("com.android.mediacenter:id/hiad_skip_text").click()
        except:
            pass
        sleep(secs=1)
        poco.swipe([0.3, 0.8], [0.3, 0.2], duration=0.1)
        poco("com.android.mediacenter:id/btn_play_pause").click()
        sleep(secs=5)
        poco("com.android.mediacenter:id/btn_play_pause").click()
        poco("com.android.mediacenter:id/iv_media_playlist").click()
        poco(text="周深 - 起风了").click()
        try:
            poco("com.android.mediacenter:id/iv_arrow_down").click()
        except:
            pass
        poco("com.android.mediacenter:id/iv_media_playlist").click()
        poco(text="张韶涵 - 破茧 - 《斗罗大陆》动画2020年新主题曲").click()
        try:
            poco("com.android.mediacenter:id/iv_arrow_down").click()
        except:
            pass
        poco("com.android.mediacenter:id/iv_media_playlist").click()
        poco(text="晴天").click()
        try:
            poco("com.android.mediacenter:id/iv_arrow_down").click()
        except:
            pass
        poco("com.android.mediacenter:id/btn_play_pause").click()
        keyevent("HOME")

def run():
    test = Tests()
    global text
    text = input()
    if text == "Huawei video":
        test.openVideoApp()
        return(text,"Huawei video finish")
    elif text == "Huawei music":
        test.openMusicApp()
        return(text,"Huawei music finish")
    elif text == "exit":
        exit()
    else:
        return(text,"input error,input again")





if __name__ == '__main__':
    while True:
        print("open ")
        run()
        print(run())