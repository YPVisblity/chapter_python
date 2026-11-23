#序章:(這裡主要描述為何需要去修復機器，以及你所扮演的角色)
#角色定義
define p = Character("你", color="#00FFCC")           # 玩家（工程師）
define aria = Character("ARIA", color="#FF9FE5")       # AI 助手（鷹架式引導）
define sys = Character("NEXUS-9", color="#FF4444")     # 系統警報音
define boss = Character("老闆", color="#FFD700")     # 遠端連線的上司

init python:
    import time
    import json

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
            renpy.fetch(url, method="POST", json=payload, headers=headers, timeout=5)
        except Exception as e:
            print("Log 上傳失敗:", e)


#初始值設定
default aria_trust = 0
default score = 0
default ai_accept_count = 0
default ai_reject_count = 0
default error_start_time = 0
default fix_duration = 0

label start:

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


    jump chapter1_0


label chapter1_0:
    "數據走廊的盡頭，是第一間密室。門上沒有把手，只有一塊閃著綠光的終端機螢幕。"
    sys "【警報】密室控制程式啟動失敗。執行環境缺少必要元件。"

    show aria talk:
        zoom 1.2
        right
    aria "這間密室是基礎測試：執行環境與變數。Layer 1 我會全力協助你，放心。"
    aria "所謂『環境』，就是程式能夠順利執行所需要的一切：Python 本身、版本，還有各種外掛套件。"
    aria "先看看螢幕上的錯誤訊息吧。"

    "終端機顯示：\nModuleNotFoundError: No module named 'requests'"

    aria "線索提示：requests 不是 Python 內建的，它屬於『第三方套件』，必須先安裝，才能 import。"

    hide aria talk
    show aria default:
        zoom 1.2
        right


# ---- 第 1 題：環境（安裝套件）----
label ch1_0_q1:
    menu:
        "在終端機執行：pip install requests":
            $ score += 10

            hide aria default
            show aria talk:
                zoom 1.2
                right
            aria "正確！pip 是 Python 的套件管理工具，pip install 套件名稱，就能把第三方套件裝進環境。"
            aria "實務上，工程師還會為每個專案建立『虛擬環境』，避免不同專案的套件版本互相打架。"
            "終端機跑過一長串下載進度，綠色的『Successfully installed』閃了一下。密室的第一道鎖開啟。"
            hide aria talk
            jump ch1_0_q2_intro

        "再寫一次 import requests，多試幾次就會成功":
            $ score = score - 15
            aria "import 只是『使用』已經安裝好的套件，套件根本不在環境裡，重複再多次也一樣會失敗。"
            jump ch1_0_q1

        "把 Python 整個刪掉重新安裝":
            $ score = score - 15
            aria "太誇張了。Python 本身沒有壞，只是少了一個外掛，補裝這個套件就好。"
            jump ch1_0_q1


# ---- 第 2 題：變數命名 ----
label ch1_0_q2_intro:
    "環境修復完成。螢幕切換成另一個畫面：一排空白的資料欄位，每個欄位都在等待一個『名字』。"

    show aria talk:
        zoom 1.2
        right
    aria "接下來是變數。你可以把變數想成貼了標籤的盒子：標籤是名稱，盒子裡裝的是資料。"
    aria "例如 score = 10，就是把數字 10 放進叫 score 的盒子裡。"
    aria "但標籤不是想怎麼取都可以。系統提供了三個欄位名稱，只有一個符合 Python 的命名規則。"
    aria "線索提示：變數名稱不能以數字開頭，也不能包含減號或空格，底線則可以使用。"

    hide aria talk
    show aria default:
        zoom 1.2
        right

label ch1_0_q2:
    menu:
        "2nd_score":
            $ score = score - 15
            aria "SyntaxError。變數名稱不能以數字開頭，Python 會把它當成數字的一部分。"
            jump ch1_0_q2

        "user_name":
            $ score += 10

            hide aria default
            show aria talk:
                zoom 1.2
                right
            aria "沒錯！由英文字母和底線組成，而且沒有用數字開頭，是合法的變數名稱。"
            aria "好的變數名稱，還要讓人一眼看懂它裝的是什麼，user_name 就比 a1 好得多。"
            "一排欄位亮起綠燈，資料欄位各就各位。"
            hide aria talk
            jump ch1_0_q3_intro

        "total-score":
            $ score = score - 15
            aria "中間的減號會被 Python 當成『減法運算』，變成 total 減去 score。想連接單字，請用底線。"
            jump ch1_0_q2


# ---- 第 3 題：變數重新賦值與動態型別 ----


label ch1_0_q3_intro:
    "最後一道鎖，是一面浮在空中的程式碼牆。牆上寫著幾行簡短的指令。"

    show aria talk:
        zoom 1.2
        right
    aria "Python 的變數有個特色：不用事先宣告型別，同一個名稱也可以隨時放進別的資料。"
    aria "這種特性叫『動態型別』。請你判斷，這段程式碼最後會印出什麼？"
    



    "投影出現程式碼："
    show question1:
        xalign 0.35
        yalign 0.75
        zoom 3.5

    hide aria talk
    show aria default:
        zoom 1.2
        right

label ch1_0_q3:
    menu:
        "10":
            $ score = score - 15
            aria "10 是第一行放進去的值，但第二行已經把 x 重新賦值了。想想看，盒子裡現在是什麼？"
            jump ch1_0_q3

        "ready":
            $ score += 10

            hide aria default
            show aria talk:
                zoom 1.2
                right
            
            hide question1
            aria "完全正確！第二行用新的值取代了舊的，x 現在裝的是字串 ready，所以 print 印出 ready。"
            aria "這和 C 語言不同，Python 不需要先宣告 int 或 char，變數的型別由當下的值決定。"
            "程式碼牆一行行重新排列，最後一道鎖解除。"
            hide aria talk
            jump ch1_0_clear

        "TypeError：不能把數字改成文字":
            $ score = score - 15
            aria "在 Python 裡完全可以。變數沒有固定的型別，每次賦值都可以放不同型別的資料。"
            jump ch1_0_q3


label ch1_0_clear:
    show aria talk:
        zoom 1.2
        right
    "密室的大門緩緩滑開，走廊的藍色光帶往前延伸。"
    aria "走吧，下一間密室在等我們。"
    hide aria talk

    # Layer 1 其餘關卡啟用後，改成 jump chapter1_1
