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

    sys "警告：第二層能源排序模組發生錯誤。"
    sys "數列核心無法自動產生穩定序列。"

    aria "user，我們到第二層了呢。這裡的系統需要照規律產生數字，不然門就不會開。"
    aria "這一關會用到 list、for 迴圈，還有等差數列公式。"
    aria "不要怕，我會一步一步帶你看。"

    call teach_sequence

    aria "差不多就是這樣。現在你已經知道怎麼產生等差數列了。"
    aria "接下來就可以去修復這一層的數列核心了，加油捏~"

    "END"
    return

label teach_sequence:
    aria "首先，等差數列是什麼呢？"
    aria "簡單來說，就是每一項和前一項都差一樣的數。"
    aria "這個固定差距叫做公差，通常會用 d 表示。"

    aria "例如 2、5、8、11、14。"
    aria "每次都加 3，所以它的公差 d 就是 3。"

    aria "題目會用到這個公式："
    aria "term = a + i * d"

    aria "a 是第一項。"
    aria "i 是目前第幾次迴圈。"
    aria "d 是公差。"

    aria "有個很重要的地方喔。Python 的 range(n) 通常會從 0 開始。"
    aria "所以第一次迴圈時，i 會是 0。"
    aria "這時候 term = a + 0 * d，也就是第一項 a。"

    menu:
        "如果 a = 2，d = 3，第一次迴圈 i = 0，term 會是多少？"

        "2":
            aria "答對了！因為 2 + 0 * 3 還是 2。"
            $ score += 1

        "3":
            aria "差一點。3 是公差，不是第一項。"

        "5":
            aria "5 是第二項。第一次迴圈 i 是 0，所以還不會加到公差。"

    aria "接著我們需要一個 list 來把每一項存起來。"
    aria "list 就像一個可以裝很多資料的盒子。"
    aria "先建立空盒子："
    aria "sequence = [[]"

    aria "每算出一個 term，就用 append 放進 sequence 裡面。"
    aria "sequence.append(term)"

    aria "整體流程會像這樣："
    aria "先準備 sequence。"
    aria "再用 for i in range(n) 重複 n 次。"
    aria "每一次都算 term。"
    aria "最後把 term append 到 sequence。"

    menu:
        "哪一行可以把算好的 term 放進 list？"

        "sequence.append(term)":
            aria "答對了！append 可以把資料加到 list 的最後面。"
            $ score += 1

        "term = a + i * d":
            aria "這一行是計算目前這一項，還沒有把它放進 list。"

        "range(n)":
            aria "range(n) 是控制迴圈跑幾次，不是存資料。"

    aria "最後記得 return sequence。"
    aria "因為題目測試時，需要拿到完整的數列結果。"

    menu:
        "要再看一次等差數列教學嗎？"

        "再看一次":
            jump teach_sequence

        "不用，繼續劇情":
            return
