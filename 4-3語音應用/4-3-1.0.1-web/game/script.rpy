# 第 4 章第三關：
# 角色定義
define p = Character("你", color="#00FFCC")
define aria = Character("ARIA", color="#FF9FE5", image="aria")
define sys = Character("NEXUS-9", color="#FF4444")
define boss = Character("老闆", color="#FFD700")

# 初始值設定
default aria_trust = 0
default score = 0

# 4-3：總機房 TTS 語音合成解鎖
image question13:
    "question13.png"
    zoom 3.5
    anchor (0.5, 0.5)
    xpos 0.35
    ypos 0.40

label start:
    scene black with fade
    show aria talk
    "終於來到了最深處的總機房大門前。然而大門被厚重的電子鎖鎖死，畫面上顯示出駭客最後的嘲諷字條。"
    "字條 『想要重啟系統？密碼隱藏在底層的加密文字檔中。但本大門只接受語音聲學頻率解鎖，你們的語音模組已經被我報廢了，慢慢猜吧！』"
    boss "客服部的無障礙語音導覽與自動回覆系統完全故障了！如果沒辦法用語音把密碼『讀出來』，我們就一輩子被關在辦公室裡了！"
    p "這是最後一關了……AI 參與度 0%%。我必須完全主導，當場寫出一個 TTS (Text-to-Speech) 語音合成模組！"
    "畫面上是一片黑暗的終端機，你需要引用 Python 最經典的文字轉語音函式庫。"
        
    "【終端機提示】"
            #\nfrom ______ import gTTS\ntts = gTTS(text=password， lang='en')\ntts.save('lock.mp3')
    label ch4_3_input:

        show question13 with dissolve
        window show

        python:
                # 測試學生是否知道 gTTS 函式庫導入時的模組名稱（全小寫）
            ans_4_3 = renpy.input("請輸入正確的 TTS 來源函式庫名稱（全部小寫）：", default="").strip()

        hide question13 with dissolve
        window auto

        if ans_4_3 == "gtts":
            $ score += 1
            "【系統提示: 密碼文字成功轉換為清晰的語音輸出:'NEXUS_RESET_2026'】"
            "機房大門偵測到正確的語音頻率，發出機械解鎖聲，轟然開啟！"
            jump chapter4_clear
        elif ans_4_3 == "pyttsx3":
                # 如果學生打另一個知名的離線 TTS 函式庫，也算他對！但給予對應的劇情台詞
            $ score += 1
            "【系統提示: 成功調用 pyttsx3 離線語音引擎，成功初始化 TTS 語音！】"
            "清晰的電子合成音在大廳響起：'NEXUS_RESET_2026'。大門轟然開啟！"
            jump chapter4_clear
        else:
            "aria" "(系統自動日誌) ModuleNotFoundError: 找不到該名稱的語音合成函式庫。大門毫無反應。"
            jump ch4_3_input            


label chapter4_clear:
    "一陣強大的綠色光芒由機房中心擴散至整棟大樓。所有的螢幕瞬間亮起，恢復成熟悉的辦公室介面。"
    sys "【系統通告】Null-Void 病毒已被全數清除。所有業務部門系統重啟完畢，運作良好。"
    "全息投影閃爍，ARIA 的身影重新凝聚，露出了欣慰的笑容。"
    show aria default with Dissolve(0.5)
    aria "連線全面恢復！工程師，你成功了！在沒有我提供語音與程式碼邏輯的情況下，你竟然獨自完成了多媒體與自動化測試的重建！"
    return   
    # 計算最終成績    
    # if score >= 60:
    #     show aria talk:
    #         right
    #     with move   
    #     aria "最終結算得分:[score] 分！你展現了極高水準的『測試驅動思維』與『獨立應用能力』，你是真正的核心架構師！"
    #     boss "太感謝你了！明天的週一例會，我會正式宣布晉升你為我們的首席資訊長(CIO)！現在，給自己開一罐慶祝的啤酒吧！"
    #     "【辦公室數據密室逃脫——成功！THE END】"

    # else:
    #     show aria talk:
    #         right
    #     with move   
    #     aria "最終結算得分:[score] 分。分數未達到標準，最終修復宣告失敗……"
    #     "【辦公室數據密室逃脫——失敗！THE END】"
   
