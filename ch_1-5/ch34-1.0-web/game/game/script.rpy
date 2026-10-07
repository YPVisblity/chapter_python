#序章:(這裡主要描述為何需要去修復機器，以及你所扮演的角色)
#角色定義
define p = Character("你", color="#00FFCC")           # 玩家（工程師）
define aria = Character("ARIA", color="#FF9FE5", image="aria")       # aria 助手（鷹架式引導）
define sys = Character("NEXUS-9", color="#FF4444")     # 系統警報音
define boss = Character("老闆", color="#FFD700")     # 遠端連線的上司

#初始值設定
default aria_trust = 0
default score = 0
label start:
    show prelude2closeeyes:
        xalign 0.5
        yalign 0.5

    sys "警告：第二層除法模組發生異常。"
    sys "偵測到 ZeroDivisionError，系統流程中斷。"

    aria "user，這一區看起來更危險一點。"
    aria "如果程式直接除以 0，整個系統就會停止運作。"
    aria "所以這一關我們要學 try/except，也就是例外處理。"

    call teach_try_except

    aria "很好，現在你已經知道怎麼讓程式遇到除以 0 時不要直接壞掉了。"
    aria "去修復 safe_divide(a, b) 吧，我會在旁邊看著你的 >u<"

    "END"
    return

label teach_try_except:
    aria "先看一般情況。"
    aria "如果 b 不是 0，a / b 可以正常算出答案。"
    aria "可是如果 b 是 0，Python 會產生 ZeroDivisionError。"

    aria "像這樣："
    aria "10 / 0"
    aria "這不是算不出漂亮答案而已，而是程式會直接報錯停下來。"

    aria "try/except 就是拿來處理這種可能出錯的情況。"
    aria "try 裡面放可能會出錯的程式。"
    aria "except 裡面放出錯後要怎麼補救。"

    aria "結構長這樣："
    aria "try:"
    aria "    可能出錯的程式"
    aria "except 錯誤類型:"
    aria "    發生錯誤時要做的事"

    menu:
        "如果我們要處理除以 0 的錯誤，except 後面應該接哪個錯誤？"

        "ZeroDivisionError":
            aria "答對了！除以 0 會產生 ZeroDivisionError。"
            $ score += 1

        "NameError":
            aria "這通常是變數名稱找不到，不是除以 0。"

        "ValueError":
            aria "這通常是資料值不適合目前操作，不是這題的重點。"

    aria "這一關的函式叫 safe_divide(a, b)。"
    aria "safe 的意思是安全，所以它要讓除法變得安全一點。"

    aria "正常情況下，可以 return a / b。"
    aria "但是如果發生 ZeroDivisionError，就 return 題目指定的錯誤文字。"

    aria "這個錯誤文字是："
    aria "Error:除以零"

    aria "注意喔，文字要一模一樣。少一個冒號、多一個空格，都可能讓測試不通過。"

    menu:
        "safe_divide(10, 0) 應該回傳什麼？"

        "Error:除以零":
            aria "答對了！b 是 0 時，要回傳這個錯誤文字。"
            $ score += 1

        "0":
            aria "不是喔。除以 0 不能直接當成 0。"

        "5":
            aria "5 是 10 / 2 的結果，不是 10 / 0。"

    aria "最後提醒一次。"
    aria "try 和 except 底下的程式都要縮排。"
    aria "縮排代表那一行屬於 try 或 except 的範圍。"

    menu:
        "要再看一次 try/except 教學嗎？"

        "再看一次":
            jump teach_try_except

        "不用，繼續劇情":
            return
