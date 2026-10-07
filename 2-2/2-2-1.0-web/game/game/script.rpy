# 第 3 章第三關：資料結構教學劇情
# 角色定義
define p = Character("你", color="#00FFCC")
define aria = Character("ARIA", color="#FF9FE5", image="aria")
define sys = Character("NEXUS-9", color="#FF4444")
define boss = Character("老闆", color="#FFD700")

# 初始值設定
default aria_trust = 0
default score = 0

label start:

    scene black with fade
    show aria talk

    sys "【警告】日誌系統無法寫入，修復紀錄正在遺失。"

    aria "這裡是第二層的日誌室。"
    aria "每一次系統修復、每一次錯誤發生，都應該被寫進日誌檔。"
    aria "可是現在日誌系統只要遇到一點問題，就會整個停止運作。"

    aria "這一關要處理的是檔案處理，還有例外處理。"

    aria "檔案處理，就是讓 Python 讀取或寫入外部檔案。"
    aria "例如把修復紀錄寫進 log.txt，或從設定檔讀取資料。"

    aria "先看這段程式。"

    show file_exception_code:
        xalign 0.5
        yalign 0.35
        zoom 2.0

    aria "def write_log(filename, data):"
    aria "這行代表我們定義了一個函數。"
    aria "filename 是檔案名稱，data 是要寫進檔案的內容。"

    aria "接著是 open(filename, 'w')。"
    aria "open 是打開檔案。"
    aria "'w' 是 write，也就是寫入模式。"

    aria "如果檔案不存在，Python 會嘗試建立一個新檔案。"
    aria "如果檔案已經存在，'w' 會把原本的內容覆蓋掉。"

    aria "然後 f.write(data) 會把資料寫進檔案。"
    aria "最後 f.close() 會關閉檔案。"

    aria "聽起來很順對吧？"
    aria "但真正的程式世界沒有那麼乖。"

    aria "檔案可能被其他程式佔用。"
    aria "資料夾可能沒有寫入權限。"
    aria "硬碟可能空間不足。"
    aria "檔案名稱也可能不合法。"

    aria "只要其中一個狀況發生，程式就可能直接崩潰。"

    menu:
        "如果 open 或 write 可能失敗，最適合怎麼處理？"

        "用 try-except 包住可能出錯的地方":
            aria "答對了！"
            aria "try-except 可以讓程式在錯誤發生時進入備用流程，而不是直接停止。"
            $ score += 1

        "只在最後 print('寫入失敗')":
            aria "這樣不夠喔。"
            aria "如果錯誤發生在中間，程式可能根本跑不到最後那一行。"

        "把檔名改短一點":
            aria "檔名有時候會造成問題，但這不是完整解法。"
            aria "我們需要的是能處理各種錯誤的結構。"

    aria "所以我們會把可能出錯的程式放進 try 裡。"
    aria "如果 try 裡發生錯誤，就會跳到 except。"

    aria "例如："
    aria "try 負責嘗試寫檔。"
    aria "except 負責處理寫檔失敗。"

    aria "這樣系統就算遇到錯誤，也能留下提示，而不是整個黑掉。"

    menu:
        "在檔案處理裡，f.close() 的主要作用是什麼？"

        "關閉檔案，釋放系統資源":
            aria "沒錯！"
            aria "檔案打開後要記得關閉，這樣系統資源才不會一直被佔用。"
            $ score += 1

        "刪除檔案":
            aria "不是喔。"
            aria "close 只是關閉檔案，不會刪除它。"

        "把檔案改成圖片":
            aria "這就完全不是 close 的工作了。"
            aria "close 只負責結束這次檔案操作。"

    aria "不過 Python 還有更推薦的寫法。"
    aria "那就是使用 with open。"

    aria "with open 會在區塊結束後自動關閉檔案。"
    aria "這樣就比較不容易忘記 f.close()。"

    aria "最後完整概念是："
    aria "open 負責打開檔案。"
    aria "write 負責寫入資料。"
    aria "try-except 負責避免錯誤讓程式崩潰。"
    aria "with open 負責自動關閉檔案。"

    hide file_exception_code

    aria "日誌系統開始重新寫入資料。"
    aria "一筆、兩筆、三筆……剛剛遺失的修復紀錄正在被補回來。"

    sys "【日誌系統】狀態恢復。錯誤保護機制啟用。"

    aria "做得好。"
    aria "這一關的重點不是完全避免錯誤，而是錯誤發生時，程式還能好好活下來。"

    return