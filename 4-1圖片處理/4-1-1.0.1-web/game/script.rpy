# 第 4 章第一關
# 角色定義
define p = Character("你", color="#00FFCC")
define aria = Character("ARIA", color="#FF9FE5", image="aria")
define sys = Character("NEXUS-9", color="#FF4444")
define boss = Character("老闆", color="#FFD700")

# 初始值設定
default aria_trust = 0
default score = 0

image question9:
    "question9.png"
    zoom 3.5
    anchor (0.5, 0.5)
    xpos 0.35
    ypos 0.40

label start:
    scene black with fade
    show aria talk
    "整棟辦公大樓的燈光突然熄滅。幾秒後,紅色的應援燈緩緩亮起,四周的虛擬數據走廊開始崩解。"
    sys "【終極警報】Null-Void 發現防線被破,正在切斷 AI 助理的雲端算力!"
    aria "啊……我的核心連線……要被切斷了……"
    "ARIA 的身體開始變得半透明,全息投影斷斷續續,發出沙沙的雜訊聲。"
    aria "接下來的 Layer 4……多媒體應用……我的參與度將降到 20%% 甚至 0%%……我只能提供極少提示,甚至……甚至無法幫你寫任何一行 Code……"
    p "ARIA!撐住啊!"
    aria "相信……你自己的……應用能力……行銷部……OpenCV……"
    "【系統提示:AI 助理 ARIA 已斷線,進入離線託管狀態。接下來的關卡將由學生完全主導。】"
    jump chapter4_1




# ==========================================
    # 4-1：OpenCV 批次去雜訊
    # ==========================================
label chapter4_1:
    "行銷部辦公區。桌上散落著週一盛大發表會的企劃書,螢幕上的產品宣傳圖全部被駭客加上了厚重的條紋雜訊與惡意色偏。"
    boss "完蛋了,幾百張 KOL 合作素材和產品圖全毀了!AI 現在只在螢幕上吐出三個字:『OpenCV』,然後就完全死機了!"
    p "沒時間指望 AI 了。只能我自己寫自動化批次修復腳本了。"
    "畫面上是一片空白的編輯器，你必須在代碼開頭引入正確的 OpenCV 函式庫名稱。"
        
    "【編輯器提示】"

    label ch4_1_input:
        show question9 with dissolve
        window show

        python:
            ans_4_1 = renpy.input("請輸入要 import 的 OpenCV 核心函式庫模組名稱：", default="").strip()

        if ans_4_1 == "cv2":
            $ score += 1
            "aria" "(系統自動日誌) 成功載入 cv2 模組！幾百張圖片在 5 秒內完成批次去雜訊與色彩通道修復，影像完美恢復！"
            "【系統提示: 處理效率與品質評測優良。成功拯救行銷部的發表會素材!】"
            return

        elif ans_4_1.lower() == "opencv":
            "aria" "(系統自動日誌) ModuleNotFoundError: No module named 'opencv'。注意：雖然外包裝叫 OpenCV，但 Python 導入時必須使用其核心縮寫！"
            jump ch4_1_input
        else:
            $  score = score -  15
            "aria" "(系統自動日誌) 無法辨識的模組。發表會迫在眉睫，行銷部亂成一團！"
              
            jump ch4_1_input

            