#序章:(這裡主要描述為何需要去修復機器，以及你所扮演的角色)
#角色定義
define p = Character("你", color="#00FFCC")           # 玩家（工程師）
define aria = Character("ARIA", color="#FF9FE5", image="aria")       # AI 助手（鷹架式引導）
define sys = Character("NEXUS-9", color="#FF4444")     # 系統警報音
define boss = Character("老闆", color="#FFD700")     # 遠端連線的上司

#初始值設定
default aria_trust = 0
default score =0
label start:
    #scene server_room with fade
    scene red server room
    show aria talk
    aria "現在我們已經來到第二層了，就讓我來教你這一層會用到的部分吧~ :3"
    aria "首先是for迴圈，在Python中使用for迴圈是像這樣，他的作用是把程式重複執行"
    hide aria talk
    show for:
        xalign 0.5
        yalign 0.5
    aria "第一行的意思是設一個i的變數為0後，執行下面縮排的程式，執行程式後把i+1，執行range裡的次數。"
    aria "簡單的來說"
    aria "這段程式碼的意思是：重複執行 5 次。"

    aria "for i in range(5):"
    aria "for 代表重複執行。"
    aria "i 是每一次迴圈拿到的數字。"
    aria "range(5) 會產生 0、1、2、3、4。"

    aria "所以這段程式不是從 1 開始，而是從 0 開始。"

    aria "第一次執行時，i 會是 0。"
    aria "第二次執行時，i 會是 1。"
    aria "第三次執行時，i 會是 2。"
    aria "第四次執行時，i 會是 3。"
    aria "第五次執行時，i 會是 4。"

    aria "接著看縮排的這一行。"
    aria "print(\"第\", i, \"次執行\")"

    aria "只要是縮排在 for 底下的程式碼，就會被重複執行。"

    aria "也就是說，這行 print 會被執行 5 次。"

    menu:
        "如果程式是 for i in range(5)，i 最後一次會是多少？"

        "5":
            aria "差一點點。range(5) 不會包含 5。"
            aria "它會從 0 數到 4。"

        "4":
            aria "答對了！range(5) 會產生 0、1、2、3、4。"

        "6":
            aria "不是喔。range(5) 只會產生 5 個數字。"

    aria "簡單記住："
    aria "range(5) 會跑 5 次，但數字是 0 到 4。"

    aria "for 迴圈很適合用在需要重複做同一件事的時候。"

    hide for

    aria "好，現在我們可以進行下一段部分了。"
    call teach_def

    aria "恭喜你拉，你現在的能力可以去處理這一層的問題了!"

    return
    
label teach_def:

    scene black with fade

    aria "如果我們要寫一個自用的程式的話"
    aria "這時候，就可以使用 def。"

    show def_example:
        xalign 0.5
        yalign 0.35
        zoom 0.9

    aria "def 是用來定義函數的關鍵字。"

    aria "函數就像是一個小工具。"
    aria "你先把工具做出來，之後需要的時候再使用它。"

    aria "來看這一行。"
    aria "def say_hello():"

    aria "def 代表我要建立一個函數。"
    aria "say_hello 是這個函數的名字。"
    aria "括號代表這是一個可以被呼叫的函數。"
    aria "最後的冒號代表：下面縮排的內容都屬於這個函數。"

    aria "接著看縮排的這一行。"
    aria "print(\"你好，歡迎回來！\")"

    aria "因為它縮排在 def 底下，所以它是函數的一部分。"

    aria "但是，光是定義函數的話還不會馬上執行捏。"

    aria "要讓函數真的開始工作，必須想辦法呼叫它。"

    aria "也就是這一行："
    aria "say_hello()"

    aria "當程式執行到 say_hello()，就會進入函數，執行裡面的 print。"
    aria "現在來問你一個問題，測測你的能耐"
    menu:
        "哪一行才會讓函數真的執行？"

        "def say_hello():":
            aria "這一行只是定義函數，還沒有真正執行裡面的內容。"

        "print(\"你好，歡迎回來！\")":
            aria "這是函數裡面的內容，但要先呼叫函數才會執行。"

        "say_hello()":
            aria "答對了！這一行是在呼叫函數。"

    aria "所以 def 的重點是："
    aria "先定義函數，再呼叫函數。"

    hide def_example

    return


