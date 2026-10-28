# 第 4 章第二關
# 角色定義
define p = Character("你", color="#00FFCC")
define aria = Character("ARIA", color="#FF9FE5", image="aria")
define sys = Character("NEXUS-9", color="#FF4444")
define boss = Character("老闆", color="#FFD700")

# 初始值設定
default aria_trust = 0
default score = 0

image question12:
    "question12.png"
    zoom 3.5
    anchor (0.5, 0.5)
    xpos 0.35
    ypos 0.40

label start:
    scene black with fade
    show aria talk
    "員工休息區。廣播喇叭正傳出駭客留下的刺耳高頻雜訊(Noise)，福委會的點歌介面整個死當卡死。"
    "隔壁桌那位平時自稱『程式大神』的豬隊友同事一臉自信地走過來。"
    "同事" "嘿！我剛才幫辦公室音樂系統寫了一段修正 Code。我打包票沒問題，你直接部署上線吧！"
    p "等一下……音訊解碼與播放的巨量運算全被他塞在了 GUI 的主執行緒裡，難怪介面會卡死。我必須用多執行緒重構它！"
        
    "【重構提示】"
        #\nimport ________\nt = threading.Thread(target=play_audio)\nt.start()

    label ch4_2_input:

        show question12 with dissolve
        window show

        python:
            ans_4_2 = renpy.input("請輸入要導入的多執行緒標準函式庫名稱（全部小寫）：", default="").strip()

        hide question12 with dissolve
        window auto

        if ans_4_2 == "threading":
            $ score += 1
            "aria" "(系統自動日誌) 審查與重構精準！成功導入 threading。音訊解碼移至背景執行，刺耳雜訊消失，介面流暢無比！"
            "【系統提示: 程式判斷能力評測達標。成功防範豬隊友的二次災難。】"
            return
        else:
            "aria" "(系統自動日誌) 災難部署！未處理主執行緒卡頓問題。喇叭爆發出更大的噪音，整個福利系統伺服器當死燒毀！"

            jump ch4_2_input

