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
    aria "嗨，你現在看到的畫面算是我們對你的職前訓練，我是你的AI助手捏~ :3"
    aria "雖然說我們的時間不多力，但為了你的安全還是要按照程序進行。"
    hide aria talk
    call open_door
    show door:
        xalign 0.5
        yalign 0.5
    aria "這扇門會根據眼前之人的等級進行檢測，原本是要等你先練練再來這個地方的說。"
    aria "可惜我們現在已經沒有更多時間了，只能草草的讓你上場。"

    p "那要怎麼開門"

    aria "哦哦，我現在就用我的權限來幫你開門"
    hide door
    "打開門後你來到堪比五彩斑斕的黑色還黑的房間"
    scene black
    aria "哎呀! 看起來這邊也遭到了波及呢。"
    "眼前突然出現了一段程式碼"
    call open_light
    show prelude2closeeyes
    aria "其實呢，剛剛的突發狀況都是測試的一環!"
    aria talk "很高興你完美達成測試。"
    aria "擁有這些知識，你現在可以開始修復這一層的系統錯誤了呢"
    "END"
    return
    




label open_door:
    show door:
        xalign 0.5
        yalign 0.5
    aria "首先我們來學學在Python裡面if else是如何運作的"
    aria "現在你會看到眼前有一道門，他的程式碼是這樣的"
    hide door
    show if_else:
        xalign 0.5
        yalign 0.5
    aria "第一行的if levels > 10 是指levels這個變數必須大於10才會執行下面的內容。"
    aria "再來是第二行後的縮排內容，是if的條件達成後會執行的內容，這扇門在等級達到十的時候會打開"
    aria "第三行的else:是指如果前面的條件不達成則會執行以下縮排的內容"
    aria talk "第四行後的縮排內容是指如果等級不大於十等的話則會顯示等級不足"
    aria "有個有趣的地方你想不想知道 :333"
    menu:
        "要不要理aria >u< ?"

        "理一下好了":
            aria "if 條件跟執行的內容裡面都可以在塞好幾個if捏><"
        "我要跳過跳過跳過skippp":
            aria "不要無視我好咩!!!"
    hide if_else
    menu:
        "要再看一次 if else 教學嗎？"

        "再看一次":
            jump open_door

        "不用，繼續劇情":
            return

label open_light:
    show if_else_if_else:
        xalign 0.5
        yalign 0.5
    aria "看來這邊的燈現在要打開的話，只能輸入數字來打開了呢 >o<?"
    aria "從程式碼來看，這邊多出了else if，剛好可以趁這個時候來進行教學"
    aria "else if 條件，當上面if的條件為達成且這一行的條件達成後，就會執行該區域的程式碼"
    aria "user有什麼好的想法咩"
    $ choosing_light = True

    while choosing_light:
        menu:
            "該輸入多少數字來打開燈呢"

            "0":
                aria "user剛剛有做什麼嗎oAo?"
                aria "還是趕快把燈打開吧!"
                hide if_else_if_else
            "25":
                aria "欸~燈好像還沒亮欸><?"
                aria "讓我們再試一次吧，試著把亮度在往上調點哦user~"
                hide if_else_if_else
            "60":
                aria "欸~這個亮度剛剛好"
                aria "user這次做的好呦!"
                $ choosing_light = False
                hide if_else_if_else
            "90":
                aria "哇哇哇*A*，現在的燈太亮了"
                aria "user趕快把燈調暗點，試著把數值往下調點呦~"
                hide if_else_if_else


