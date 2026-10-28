#序章:(這裡主要描述為何需要去修復機器，以及你所扮演的角色)
#角色定義
define p = Character("你", color="#00FFCC")           # 玩家（工程師）
define aria = Character("ARIA", color="#FF9FE5")       # AI 助手（鷹架式引導）
define sys = Character("NEXUS-9", color="#FF4444")     # 系統警報音
define boss = Character("老闆", color="#FFD700")     # 遠端連線的上司

init python:
    import time
    import json
    import requests

    # 紀錄錯誤發生的時間點
    def mark_error_occurred():
        global error_start_time
        error_start_time = time.time()

    # 紀錄錯誤修復並計算耗時（秒）
    def mark_error_fixed():
        global error_start_time, fix_duration
        if error_start_time > 0:
            fix_duration = round(time.time() - error_start_time, 2)
            error_start_time = 0


# 發送 API 寫入資料庫
    def send_research_logs():
        url = "https://your-api-domain.com/api/save_log"
        payload = {
            "score": score,
            "ai_accept_count": ai_accept_count,
            "ai_reject_count": ai_reject_count,
            "fix_duration": fix_duration
        }
        headers = {'Content-Type': 'application/json'}
        try:
            requests.post(url, data=json.dumps(payload), headers=headers, timeout=5)
        except Exception as e:
            print("Log 上傳失敗:", e)







#初始值設定
default aria_trust = 0
default score =0
default ai_accept_count = 0
default ai_reject_count = 0
default error_start_time = 0
default fix_duration = 0

label start:
    "實驗開始。"
    $ mark_error_occurred()

    menu:
        "接受 AI 建議":
            $ ai_accept_count += 1
            "【系統提示】你點了接受！"
        "拒絕 AI 建議":
            $ ai_reject_count += 1
            "【系統提示】你點了拒絕！"

    $ mark_error_fixed()

    # 直接把數值印出來看
    "【Debug 資訊】"
    "接受次數：[ai_accept_count]"
    "拒絕次數：[ai_reject_count]"
    "修復耗時：[fix_duration] 秒"

#label start:
    #scene server_room with fade

    "昏暗的企業伺服器機房。冷白燈光打在密密麻麻的機架上，警示燈不停閃爍紅光。"
    scene red server room
    show boss talk:
        xalign 0.5
        ease 0.5 zoom 1.4

    boss "喂，你聽得到嗎？NEXUS-9 的核心系統在三小時前開始異常，我們部署的Python專案陸續發生邏輯錯誤，導致崩潰。"
    boss "那些AI自動生成的程式碼產生了未知的錯誤，把系統鎖死成了好幾個獨立的數據密室。"
    hide boss talk
    show prelude1 with dissolve:
        xalign 0.5
        yalign 0.3
        zoom 1.5
    boss "你是我們最後一張牌。進去把他修好。"
    hide prelude1
    show boss awkward:
        xalign 0.5
        zoom 1.4

    p "我一個人？"

    boss "不是。系統裡有一個AI協作模組，代號ARIA。它會在旁邊提供測試回饋和除錯線索，但最終動手的還是你。"
    boss "時限六小時。開始吧。"

    hide boss awkward

    # sfx:sfx_boot（傳送音效） 
    #scene nexus_core with dissolve  #傳送進空間的畫面

    "意識被拉進虛擬空間。眼前是無盡延伸的數據走廊，地板是半透明的程式碼流。"
    scene virtual space
    
    show prelude2closeeyes with dissolve:
        xalign 0.5
        yalign 0.3
        zoom 1.5

    pause(1.0)
    
    show prelude2openeyes with dissolve:
        xalign 0.5
        yalign 0.3
        zoom 1.5
    
    pause(2.0)

    #show aria  at center #AI助手
    hide prelude2closeeyes
    hide prelude2openeyes
    show aria talk:
        zoom 1.2
        right
    aria "連線確認。你好，工程師。我是ARIA，你的協作模組。"


    aria "NEXUS-9 有多個Python專案的執行環境遭到封鎖。每一個異常的專案，都形成了一個無法通行的密室，我會陪你逐一排除。"
    aria "準備好了嗎？"

    menu:
        "準備好了。":
            $ aria_trust += 1
            show aria talk:
                zoom 1.2
                right
            aria "很好。第一間密室是基礎環境與語法測試，跟我來。"
            hide aria talk
            show aria leave:
                xalign 0.6
                zoom 1.2
            show aria leave:
                xalign 0.6
                yalign 5.0
            with move
                
        "等一下，這裡是哪？":

            show aria talk:
                zoom 1.2
                right
            aria "虛擬伺服器核心空間。你的意識已經數位化。別太緊張，你不會真的死在這裡的。"
            aria "大概不會。"
            hide aria talk

    jump chapter1_1

#1-1 Python 基礎 (100%AI幫助)(選擇題)主要教導int、print這些基礎語法。
label chapter1_1:

    pause(1.0)
    show aria default:
        zoom 1.2
        right
        yalign 5.0
    show aria default:
        right
        yalign 1.0
    with move
    aria "再進行修復程式碼前，您需要了解關於python的一些基本語法。"
    "可以宣告一個變數給予一個數值，像是 a=1，在python中不用像是其他語言一樣先宣告int or char"
    "利用print語法可以將其輸出在螢幕上。例如print(a)"

    show aria talk:
        zoom 1.2
        right

    aria "接下來就是你表現的時候了。"
    aria "首先，我們需要向核心提交合法的Python語法來解鎖。系統提供了三段啟動程式碼，但只有一個是正確的。"

    "畫面出現三個程式碼選項，像全息投影懸浮在空中。"

    show aria default:
        zoom 1.2
        right

    aria "線索提示：Python 用 # 做單行注釋，變數不需要宣告型別，print要加括號。"
    menu:
        # "選項 A：\nx = 10\ny = 20\nprint(x + y)":
        "選項 A：{image=ANS2} ":
            image ANS2:
                "ANS2.png"
                zoom 3 

            $ score += 10

            show aria talk:
                zoom 1.2
                right
            aria "正確！這是標準的Python變數宣告與輸出。"
            hide aria talk
            "系統提示：PyBryt基礎測試通過，獲得碎片鑰匙。密室門發出金屬聲，緩緩開啟。"
            show aria default with Dissolve(0.5)
            aria "我們趕緊移動吧。"
            hide aria default
            jump chapter1_2

            
        #"選項 B：\nint x = 10;\nint y = 20;\nprintf(\"%%d\"， x+y);":
        "選項 B：{image=ANS3} ":
            image ANS3:
                "ANS3.png"
                zoom 3         

            aria "PyBryt測試失敗：SyntaxError。這比較像 C 語言，Python 不需要宣告型別，也不用分號結尾。"
        
            $ score = score - 15
            jump chapter1_1
          
            
        #"選項 C：\nDIM x AS INTEGER = 10\nPRINT x + 20":
        "選項 C：{image=ANS4} ":
            image ANS4:
                "ANS4.png"
                zoom 2.5         

            $  score = score - 15
            aria "PyBryt測試失敗：SyntaxError。這是BASIC的語法。我們需要的是Python喔。"
            aria "記住：Python 直接寫 x = 10 就好，非常簡潔。"
            jump chapter1_1



#1-2 基本語法
image question10:
    "question10.png"
    zoom 4.0
    anchor (0.5, 0.5)
    xpos 0.45
    ypos 0.68

label chapter1_2:
        "走廊深處出現一個巨大的資料處理模組，像是一個透明的旋轉鼓輪，裡面的數字全是亂碼。通往下一區的閘門緊閉。"
        
        sys "【警報】資料處理模組邏輯異常。運算結果偏差300%%。"

        show aria default:
                zoom 1.2
                right
        aria "糟糕，這個模組負責病患排隊的資料計算。AI 生成了一段錯誤的折扣邏輯。"
        aria "我已經幫你定位出錯誤的程式碼片段，你來選出正確的修正方式，我們才能拿到下一把鑰匙。"

        "投影出現有Bug的程式碼："
        #"total= 100\n discount = 20%%\n final=total-discount\n print(final)"

        show question10 with dissolve
        window show
        window auto

        show aria default:
            zoom 1.2
            right

        aria "線索提示：Python的%%是取餘數運算子，不是百分比。如果要計算20%%的折扣，你會怎麼寫？"
     


        menu:
            "修正為：discount = total * 0.20":
                hide question10 with dissolve
                window auto

                $ score += 10
                show aria talk:
                    zoom 1.2
                    right
                aria  "完全正確！discount = total * 0.20 才是正確的百分比計算方式。"
                "系統提示：PyBryt邏輯測試通過。鼓輪停止轉動，數字重新排列整齊，閘門開啟。"
                hide aria talk
                jump chapter1_3

            "修正為：discount = 20":
                hide question10 with dissolve
                window auto

                $  score = score -  15
                aria  "測試失敗：數值硬編碼 (Hardcoded)。這樣寫是固定折扣20元，不是20%%。如果 total變了，這個數字就不對了。"
                jump chapter1_2

            "修正為：discount = \"20%%\"":
                hide question10 with dissolve
                window auto

                $  score = score -  15
                aria  "測試失敗：TypeError。這樣 discount 變成字串了，字串不能拿來跟整數做相減運算。"
                jump chapter1_2


#1-3 迴圈與資料結構
image question6:
    "question6.png"
    zoom 3.5
    anchor (0.5, 0.5)
    xpos 0.45
    ypos 0.65


label chapter1_3:
        "空間突然開始扭曲。走廊在眼前無限複製，像鏡中鏡一樣延伸，形成一個無法逃脫的迷宮。"

        sys "【警報】庫存管理密室陷入無限迴圈。CPU使用率99.9%%。"

        show aria talk:
            zoom 1.2
            right
        aria "這就是為什麼密室開始抖動……庫存系統陷入無限迴圈，它一直在重複執行卻沒有停止條件。"
        aria "你來判斷哪裡會造成無限迴圈，並選出最適合管理這個庫存資料的結構。"
        
        show aria default:
            zoom 1.2
            right
        
        show question6 with dissolve        
        window show
        window auto



        #{image=question6} 
        "投影出現有問題的程式碼：\n # 缺了其中一段程式碼"
      #  "  i = 0\n  while i < 10:\n      print(i)\n  # 少了 i += 1"
              
        menu:
            "問題在：缺少 i += 1 讓計數器遞增":
                hide question6 with dissolve
                window auto
                
  
                $ score += 10
                
                hide aria default
                show aria talk:
                    zoom 1.2
                    right
                aria  "對！沒有 i += 1，i 永遠是 0，條件永遠是 True，迴圈永遠不停。"
                hide aria talk
                jump ch1_3b

            "問題在：while應該改成for":
                hide question6 with dissolve
                window auto

                $  score = score - 15
                aria  "這是一個解法，但不是引發無限迴圈的根本原因。看看i這個變數，它有在迴圈裡面被改變嗎？"
                jump chapter1_3

            "問題在：print(i) 應該移到迴圈外":
                hide question6 with dissolve
                window auto

                $  score = score - 15
                aria  "這樣的話 i 根本不會被印出來。想想：迴圈什麼時候才會停下來？"
                jump chapter1_3

label ch1_3b:
        show aria talk:
            zoom 1.2
            right
        aria "很好！現在，這個庫存系統需要頻繁地『新增』和『取出』資料。"
        aria "我們希望最早輸入的資料先處理（避免塞車），也就是先到的資料優先送出。"
        aria "你會選哪種資料結構作為修復的基底？"
        show aria default:
            zoom 1.2
            right

        menu:
            "佇列（Queue）— 先進先出（FIFO）":
                $ score += 10
                

                hide aria default
                show aria talk:
                    zoom 1.2
                    right
                aria  "答對了！因為要避免過期，必須嚴格遵守『先進先出（FIFO）』，所以 佇列（Queue） 是唯一正確的選擇！"
                aria  "完美！佇列就是為了這種先進先出的場景設計的，非常適合庫存管理。"
                hide aria talk
                jump chapter1_clear

            "堆疊（Stack）— 後進先出（LIFO）":
                $  score = score -  15
                aria  "堆疊是後進先出。想像你在排隊買票，先排的人先買到——這是哪種結構？"
                jump ch1_3b

            "字典（Dict）— 鍵值對應":
                $  score = score -  15
                aria  "字典適合用『名稱』查找對應資料，但不擅長管理順序和進出。"
                jump ch1_3b

label chapter1_clear:

        "走廊的扭曲消失，密室解鎖。一扇通往下層的電梯門緩緩開啟，發出藍色光暈。"

        show aria talk:
            zoom 1.2
            right
        aria  "累計總得分:[score] 分。\nLayer 1密室修復完成！你做得很好。"
        aria "接下來是 Layer 2，那裡的 AI 輔助會少一點，你需要由自己負責主要部份了。"

        show aria default:
            zoom 1.2
            right

        p "等一下——你說『少一點』？"

        show aria talk:
            zoom 1.2
            right
        aria  "我不能一直把答案塞到你手裡，否則你永遠無法對抗那些失控的AI程式碼。"
        aria  "準備迎接真正的Debug吧，加油。"
        hide aria talk
    

