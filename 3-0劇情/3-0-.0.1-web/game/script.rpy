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



label chapter3_intro:
    pause(1.0)
    show aria default:
        zoom 1.2
        right
        yalign 5.0
    show aria default:
        right
        yalign 1.0
    with move
    "進入公司12樓的投資分析辦公室，這裡留了一封內部郵件和權限受限制的AI助理，這時警報突然大響，主控台上出現了AI助理的聲音。"
    sys "【警報】警告！警告！投資數據和資料被駭客入侵了，趕快去分析辦公室處理。"
    aria "這裡會很麻煩。我會給你有Bug的程式碼，你需要找出問題並修正。"
        
    aria "從現在開始，我的AI 參與度降到 50%%。我只能幫你盲目產出 Code 構架，但我完全無法檢查邏輯對錯"
    hide aria talk
    show aria default:
        zoom 1.2
        right
    p "也就是說，你寫出來的東西可能是垃圾，我得自己寫測試去抓你的 Bug？"

    hide aria default
    show aria talk:
        zoom 1.2
        right
    aria "是的。你必須扮演『最嚴格的驗收官』，用測試驅動的思維來糾正我。我們第一個要救的是財務部！"
    hide aria talk
    jump chapter3_1

        
# 3-1：Matplotlib 座標軸測試驗證
image question11:
    "question11.png"
    zoom 3.5
    anchor(0.5, 0.5)
    xpos 0.35
    ypos 0.40
    
label chapter3_1:
    "財務部辦公室。財務長(CFO)正對著筆電瘋狂敲擊鍵盤，臉色慘白。"
    boss "完蛋了！下半年的『全球投資分析儀表板』數據全亂了！Y 軸和 X 軸數據嚴重拉曲、甚至倒轉，高層差點做出賠上數百萬的錯誤決策！"
    aria "我試圖調用 Matplotlib 自動重新繪製圖表了……程式碼已經吐在全息螢幕上。"
    "全息投影浮現出 ARIA 自動生成的 Matplotlib 程式碼，但圖表的座標範圍(xlim)極度詭異。"
    aria "請你撰寫一段 Python 的『斷言測試 (Assertion)』來驗證圖表的 get_xlim() 是否回傳正確的區間 [0, 100]，以防錯誤圖表被導出。"
        


label ch3_1_input:
    "【全息投影提示：請補完驗證測試碼】"

    show question11 with dissolve
    window show

    $ ans_3_1 = renpy.input("請輸入正確的 Python 測試斷言關鍵字（注意大小寫）：", default="").strip()

    hide question11 with dissolve
    window auto

    if not ans_3_1:
        "系統" "編輯器未偵測到任何輸入，請輸入測試代碼！"
        jump ch3_1_input

    # 嚴格驗證：只接受 python 內建的 assert 關鍵字
    if ans_3_1 == "assert":
        
        show aria talk at right
        aria "測試通過！成功使用 assert 進行自動化邊界驗證！圖表的座標軸自動縮放回正常範圍，數據曲線變美觀了！"
        "【系統提示: 圖表正確性與美觀度評測達標。財務長的血壓降下來了。】" 
        jump chapter3_2

    else:
        show aria talk at right
        aria "驗收失敗！輸入錯誤或使用了無法自動化驗證的語法。財務長看不懂亂掉的趨勢！"
        "【繼續加油，你可以的！】"
        jump ch3_1_input

    # 3-2：人資部影音完整性檢查
image question7:
    "question7.png"
    zoom 3.5
    anchor (0.5, 0.5)
    xpos 0.35
    ypos 0.40


label chapter3_2:
        "人資部(HR)辦公區。走廊上堆滿了新進員工的教育訓練資料。"
        boss "新進員工線上培訓一小時後就要開始！但影音伺服器中了病毒，影片庫的下載功能失效，有些檔案甚至變成了毀損的空白檔案！"
        aria "我已經用 Python 寫好了一套自動化下載與重組影音流的邏輯。Code 就在這裡。"
        p "你確定這套邏輯能載到完整的影片？"    
        aria "我不確定……我現在只管吐 Code，不管邏輯驗收。你需要撰寫測試案例來驗收我的程式碼。"
        aria "線索提示: 功能完整性的驗收，關鍵在於檢查下載後檔案的格式與檔案大小是否大於 0。我們會用到 os 模組下的路徑與大小檢查工具。"
        

label ch3_2_input:
            "【全息投影提示：請輸入正確的 os 函式來獲取檔案大小 (Bytes)】"#if os.path.______(video_path) > 0:\n    print('下載成功')
            
            show question7 with dissolve
            window show
            
           
                # 測試學生是否知道獲取檔案大小的函式是 getsize
            $ ans_3_2 = renpy.input("請輸入正確的 os.path 內建子函式名稱：", default="").strip()
    
            hide question7 with dissolve
            window auto



            if not ans_3_2:
                "系統" "編輯器未偵測到任何輸入，請輸入測試代碼！"
                jump ch3_2_input

            if ans_3_2 == "getsize" or ans_3_2 == "getsize()":
                # 防呆：如果學生加了括號，幫他過濾掉
                
                show aria talk at right
                aria "精準的測試！我的下載邏輯裡確實少判斷了未傳輸完成的情況。使用 getsize 成功攔截了 0 KB 的壞檔！影片庫功能完全恢復了！"
                "【系統提示: 功能完整性評測通過。新員工影音系統上線成功。】"
                jump chapter3_3

            else:
                show aria talk at right
                aria "測試漏洞！這個方法無法正確讀取檔案大小，畫面上流過了好多 0 KB 的毀損影片，人資部要暴走了！"
                jump ch3_2_input

    # 3-3：IoT 環控系統空值清洗
image question8:
    "question8.png"
    zoom 3.5
    anchor (0.5, 0.5)
    xpos 0.35
    ypos 0.40

label chapter3_3:
        "突然間，辦公室的冷氣發出劇烈運轉聲，溫度瞬間掉到 16 度，會議室的智慧燈光開始瘋狂閃爍。"
        sys "【警告】總務部智慧辦公室 IoT 環控系統暴走。數據讀取到大量空值。"
        aria "駭客切斷了感測器 API 的部分數據，導致系統一直讀到 None。我的程式碼沒有處理空值，直接把空值帶入計算，系統卡死了！"
        p "快把你的 API 接收 Code 丟出來，我來寫資料清洗測試！"
        

label ch3_3_input:
            "【全息投影提示：請輸入防呆判斷，當 data 為什麼時給予預設值 26 度？】"#if data is ____:\n    data = 26
            
            show question8 with dissolve
            window show

           
                # 測試學生是否知道 Python 的空值型態是大寫的 None
            $ ans_3_3 = renpy.input("請填入 Python 的空值關鍵字（注意大小寫）：", default="").strip()

            hide question8 with dissolve
            window auto

            if ans_3_3 == "None":
                
                show aria talk at right
                aria "完美清洗！環控系統成功跳過了駭客製造的空值陷阱，冷氣和燈光恢復正常了！"
                "【系統提示: API 接收正確性評測通過。Layer 3 數據密室全面解鎖！】"
                jump chapter3_clear

            elif ans_3_3.lower() == "null" or ans_3_3.lower() == "none":
                show aria talk at right
                aria "注意！Python 的空值宣告與 JavaScript 或 SQL 不同，且大小寫極為嚴格！請重新檢查。"

                jump ch3_3_input
            else:
                show aria talk at right
                aria "不行啊！錯誤的判斷式導致程式拋出 NameError 或 TypeError，系統陷入無限重啟！"

                jump ch3_3_input



label chapter3_clear:
        "成功修復辦公室的Debug了，資料數據慢慢恢復了。"

        aria "Layer 3密室修復完成！你越來越厲害了。"
        aria "接下來是 Layer 4，那裡的 AI 輔助會降至20%%~0%%，你需要由自己負責主要部份了。"

        p "等一下——你說『變少甚至沒有』？"

        aria "我的核心算力正被 Null-Void 強制剝離...這是我最後能維持的連線了。"
        aria "接下來的路...請相信你這幾層樓累積的直覺，加油。"
        "ARIA 的身影閃爍了一下，逐漸變得透明，虛擬空間的雜訊聲越來越大。"        
