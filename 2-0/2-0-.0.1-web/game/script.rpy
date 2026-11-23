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




#CHAPTER 2：Layer 2 — 應用區（80% 鷹架，有 Bug 需修正）
label chapter2_intro:
    "進入一個像辦公室的空間，但所有門都被紅色雷射網封鎖。電話不停響，卻沒人接聽。"

    sys "【警報】Layer 2 三個子系統異常。通信模組 Lag、日誌系統崩潰、情報爬蟲被封鎖。"
    
    show aria talk:
        zoom 1.2
        right
    aria  "這層的密室比較麻煩。我會給你有 Bug 的程式碼，你需要找出問題並修正。"
    aria "我還是會在旁邊提供錯誤訊息線索，但我不會直接把正確語法列出來了。"
    hide aria talk
    show aria default:
        zoom 1.2
        right


# 2-1：函式與模組
image question3:
    "question3.png"
    zoom 3.0
    anchor (0.5, 0.5) 
    xpos 0.4     
    ypos 0.68


label chapter2_1:
        show aria talk at right
        "一面巨大的白板上貼滿了重複的便利貼，每張都寫著幾乎一樣的程式碼。通訊室的門緊閉。"

        aria  "通信模組的程式碼，同樣的計算邏輯被 AI 複製貼上了七次。而且執行時會拋出 UnboundLocalError。"

        "投影出現有Bug的程式碼："
        #"  total = 0\n\n  def add_score(points):\n      total += points\n      return total\n\n  add_score(10)"
        #"{image=question3}"
        show question3 with dissolve
        window show
        window auto

        aria "這段程式試圖修改全域變數，但失敗了。你知道為什麼嗎？"



        menu:
            "global total 沒有宣告，函式內無法修改外部變數":

                hide question3 with dissolve
                window auto

                $ score += 10
                

                hide aria default
                show aria talk:
                    zoom 1.2
                    right
                aria  "完全正確！Python 函式內若要修改外部變數，需要加上 global 宣告。"
                "白板上的便利貼一張張脫落，匯聚成一個整齊的函式模組。通訊室雷射網解除。"
                hide aria talk
                jump chapter2_2

            "函式名稱add_score需要改成addScore":
                hide question3 with dissolve
                window auto

                $  score = score -  15
                aria  "命名不影響執行。問題在於變數的『作用域』(Scope)。"
                jump chapter2_1

            "return total 應該改成print(total)":

                hide question3 with dissolve
                window auto

                $  score = score -  15
                aria  "return 是將值傳遞出去的正確做法。這不是造成錯誤的原因。"
                jump chapter2_1


    # 2-2：檔案與例外處理
image question4:
    "question4.png"
    zoom 2.9
    anchor (0.5, 0.5) 
    xpos 0.33    
    ypos 0.68



label chapter2_2:
        show aria talk at right
        "資料中心的走廊，地板上散落著破碎的日誌檔碎片，像玻璃一樣發光。"

        sys "【警報】日誌系統崩潰。關鍵修復紀錄遺失 47 筆。"

        show aria talk:
            zoom 1.2
            right
        aria  "日誌系統在寫檔時，遇到權限不足就直接崩潰，完全沒有例外處理機制。"
        aria "我已經寫好了架構，但缺少容錯的機制。剩下交由你來補完。"

        "投影出現需要補完的程式碼："
        
        #"  def write_log(filename， data):\n      f = open(filename， 'w')\n      f.write(data)\n      f.close()\n      print('寫入成功')"    
        #"{image=question4}"

        show question4 with dissolve
        window show
        window auto
        aria "如果 open 失敗，整個密室就會崩潰。你會怎麼改？"
        hide aria talk
        show aria default:
            zoom 1.2
            right


   

        menu:
            "用 try-except 包住 open 和 write，except 捕捉 Exception":
                hide question4 with dissolve
                window auto
                
                $ score += 10
                

                hide aria default
                show aria talk:
                    zoom 1.2
                    right
                aria  "很好！try-except 可以讓程式在出錯時優雅地捕捉例外，而不是直接終止程式。"
                "地板上的碎片重新拼合，日誌檔一筆筆恢復完整。下一扇門開啟。"


                hide aria talk
                jump chapter2_2_1

            "在 open 前加上 if os.path.exists(filename)":
                hide question4 with dissolve
                window auto

                $  score = score -  15
                aria  "這只能確認檔案存在，無法處理『權限不足』或『磁碟空間已滿』等無法預期的錯誤。"
                jump chapter2_2

            "加上 print('寫入失敗') 在最後":
                hide question4 with dissolve
                window auto
                
                $  score = score -  15
                aria  "print 不能阻止程式崩潰，只是在崩潰前多說一句話而已。你需要控制流的結構。"
                jump chapter2_2

    # 2-2-1：額外章節

label chapter2_2_1:
    
        "恭喜你，已經完成了檔案處理的問題了。"
        show aria talk:
            zoom 1.2
            right
        aria  "你想要額外的加分嗎？"
        

        hide aria talk
        show aria default:
            zoom 1.2
            right

        menu:
            "是":
                aria  "那就進行額外的關卡了唷。"
                aria  "不要害怕很簡單的。"
                hide aria talk
                jump chapter2_2_2

            "否":
                aria  "那就繼續進行下一關了唷。"

                jump chapter2_3

            
    # 2-2-2：額外章節的題目
image question1:
    "question1.png"
    zoom 2.
    anchor(0.5, 0.5)
    xpos 0.33
    ypos 0.68

image code_inline:
    "question1.png"
    zoom 2.5


label chapter2_2_2:
    show aria talk:
        zoom 1.2
        right
        
    aria "恭喜你進入了額外的題目。"
    aria "請仔細觀察程式碼片段，何者數值輸入進去會執行except的區段？"

    # 4. 變更角色表情切換，並準備進入輸入環節
    hide aria talk
    show aria default:
        zoom 1.2
        right
    show question1 with dissolve
    window show
    window auto


#額外加分(選擇)
    menu:
            "選項A\n1":
                hide question1 with dissolve
                window auto
                
                $ score = score -  15
                

                hide aria default
                show aria talk:
                    zoom 1.2
                    right
                aria  "錯誤。這裡沒有辦法到except區段，只有到try區段，會出現2。"


                hide aria talk
                jump chapter2_2_2

            "選項B\n0.2":
                hide question1 with dissolve
                window auto

                $  score += 10
                aria  "恭喜你答對了。這個數值會跑到except區段的。"
                jump chapter2_3

            "選項C\n-1":
                hide question1 with dissolve
                window auto
                
                $  score = score -  15
                aria  "錯誤。這裡沒有辦法到except區段，只有到try區段，會出現0。"
                jump chapter2_2_2
 
    # ---- 2-3：網路爬蟲 ----
image question5:
    "question5.png"
    zoom 3.5
    anchor (0.5, 0.5) 
    xpos 0.45    
    ypos 0.65


label chapter2_3:
        "牆壁上出現一個巨大的網路節點圖，其中 ETtoday 的入口閃爍著大大的 403 Forbidden 封鎖標誌。"

        show aria talk:
            zoom 1.2
            right
        aria  "為了獲取外部情報，系統需要爬取新聞。但 AI 寫的爬蟲一直被拒絕。"

        #"  import requests\n\n  response = requests.get('https://www.ettoday.net')\n  print(response.status_code)"
        #"{image=code_inline}"
       

        aria "這段程式執行後會收到 403 Forbidden。你猜伺服器是怎麼識破我們是機器人的？"
        hide aria talk
        show aria default:
            zoom 1.2
            right

        "【投影出現有問題的程式碼：】"
        show question5 with dissolve
        window show
        window auto

        menu:
            "缺少 User-Agent headers，伺服器拒絕非瀏覽器請求":
                hide question5 with dissolve
                window auto
                $ score += 10
                

                hide aria default
                show aria talk:
                    zoom 1.2
                    right
                aria  "正確！沒有偽裝 User-Agent，伺服器一看就知道是 Python-requests 發出的請求。"
                "【403 封鎖標誌轉為綠色 200 OK，大量新聞標題開始流入系統。】"
                hide aria talk
                jump chapter2_clear

            "需要加上 time.sleep(1) 避免太頻繁":
                hide question5 with dissolve
                window auto
                
                $  score = score -  15
                aria  "睡眠時間可以降低被封鎖的機率，但 403 是當下就被拒絕，不是因為太頻繁造成的 429 Too Many Requests。"
                jump chapter2_3

            "URL 需要加上 https://www. 才正確":
                hide question5 with dissolve
                window auto

                $  score = score -  15
                aria  "URL 本身沒問題。問題在 HTTP Request Headers 裡面缺少了關鍵的身份證明。"
                jump chapter2_3

label chapter2_clear:
        "【CG：辦公室空間的紅色雷射網全數消失，螢幕一個個恢復正常顯示。】"

        show aria talk:
            zoom 1.2
            right
        aria  "累計總得分:[score] 分。\nLayer 2 密室修復完成。你的除錯直覺越來越敏銳了。"
        p "下一層呢？"

        aria  "Layer 3……我的輔助會降到 50%%。我只會幫你生出程式碼架構，但我不保證邏輯是對的。"
        aria "你必須運用『測試驅動』 的思維，自己找出漏洞。"
        hide aria talk
        show aria default:
            zoom 1.2
            right
        p "明白了。來吧。"
        hide aria default
        show aria leave:
            xalign 0.6
            zoom 1.2
        show aria leave:
            xalign 0.6
            yalign 5.0
        with move
