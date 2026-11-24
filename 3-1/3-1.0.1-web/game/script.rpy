# 第 3 章第三關：資料結構教學劇情
# 角色定義
define p = Character("你", color="#00FFCC")
define aria = Character("ARIA", color="#FF9FE5", image="aria")
define sys = Character("NEXUS-9", color="#FF4444")
define boss = Character("老闆", color="#FFD700")

# 初始值設定
default aria_trust = 0
default score = 0
default mpl_return = "chapter2_clear"
default mpl_done = False



label start:
    label chapter_mpl:
    "財務部辦公室。整面牆的螢幕上，原本應該顯示營收走勢的儀表板，現在只剩下一片扭曲的線條。"
    boss "完蛋了！財務長剛剛說，下午的報告要用這張圖，可是圖表整個亂掉了！"
    sys "【警報】視覺化模組異常。圖表輸出錯誤。"

    show aria talk:
        zoom 1.2
        right
    aria "這間密室的任務，是用 Matplotlib 把資料畫成圖表。它是 Python 最常用的繪圖套件。"
    aria "我已經把資料準備好了，不過畫圖的程式碼，要靠你來決定。"
    aria "第一步，先把繪圖工具匯入。Matplotlib 有一個固定的匯入寫法，所有工程師都用同一種。"

    "投影出現三種匯入方式，只有一種能讓後面的 plt.plot 正常運作："

    hide aria talk
    show aria default:
        zoom 1.2
        right


# ---- 第 1 題：匯入慣例 ----
label mpl_q1:
    menu:
        "選項 A：\nimport matplotlib.pyplot as plt":

            hide aria default
            show aria talk:
                zoom 1.2
                right
            aria "正確！pyplot 是 Matplotlib 裡負責畫圖的子模組，as plt 是業界通用的簡寫，之後只要打 plt 就好。"
            "螢幕上的亂碼閃了一下，右下角出現一個小小的圖表圖示。"
            hide aria talk
            jump mpl_q2_intro

        "選項 B：\nimport matplotlib as plt":
            aria "AttributeError：module 'matplotlib' has no attribute 'plot'。plot 這些畫圖函式放在 pyplot 子模組裡，不在最外層。"
            jump mpl_q1

        "選項 C：\nfrom plt import matplotlib":
            aria "ModuleNotFoundError：沒有叫 plt 的模組。plt 只是我們自己取的簡稱，不是真正的模組名稱。"
            jump mpl_q1


# ---- 第 2 題：畫折線圖（x、y 順序）----
label mpl_q2_intro:
    "工具載入完成。螢幕上出現兩串資料：每個月份的編號，以及對應的營收。"

    show aria talk:
        zoom 1.2
        right
    aria "資料長這樣："
    "x = [[1, 2, 3, 4]\ny = [[10, 20, 15, 30]"
    aria "x 是月份，y 是營收。畫折線圖要用 plot，但是兩個參數的順序，會決定哪一個在橫軸、哪一個在縱軸。"
    aria "財務長上一次的圖，就是因為 X 軸和 Y 軸倒轉，才差點做出錯誤的決策。這次要特別小心。"

    hide aria talk
    show aria default:
        zoom 1.2
        right

label mpl_q2:
    menu:
        "選項 A：\nplt.plot(x, y)":

            hide aria default
            show aria talk:
                zoom 1.2
                right
            aria "沒錯！plot 的第一個參數是橫軸（x），第二個參數是縱軸（y）。月份在橫軸，營收在縱軸，趨勢才會正確。"
            "螢幕上，一條向上起伏的折線沿著月份緩緩延伸。"
            hide aria talk
            jump mpl_q3_intro

        "選項 B：\nplt.plot(y, x)":
            aria "這行不會報錯，但畫出來的圖，營收跑到橫軸，月份跑到縱軸，整張圖是歪的。財務長看了一定會誤會。"
            aria "沒有錯誤訊息的 Bug，反而更危險。畫完之後，一定要檢查兩個軸。"
            jump mpl_q2

        "選項 C：\nplt.show(x, y)":
            aria "show 的功能是『把畫好的圖顯示出來』，它不負責畫線，也不接受這樣的資料參數。"
            jump mpl_q2


# ---- 第 3 題：標題與座標軸名稱 ----
label mpl_q3_intro:
    "折線的方向終於正確了。不過，財務長看著螢幕，眉頭依然沒有鬆開。"
    boss "線是畫出來了，可是我看不出這是什麼圖啊？沒有標題，也不知道橫軸縱軸各代表什麼。"

    show aria talk:
        zoom 1.2
        right
    aria "他說得對。一張沒有說明的圖，就算資料正確，也很難讓人看懂。"
    aria "Matplotlib 提供了一組函式，專門用來加上標題和座標軸名稱。請選出正確的寫法。"

    "投影出現三組程式碼，只有一組能同時加上標題、橫軸名稱和縱軸名稱："

    hide aria talk
    show aria default:
        zoom 1.2
        right

label mpl_q3:
    menu:
        "選項 A：\nplt.title('Revenue')\nplt.xlabel('Month')\nplt.ylabel('Amount')":
            $ score += 10

            hide aria default
            show aria talk:
                zoom 1.2
                right
            aria "完全正確！title 設定標題，xlabel 設定橫軸名稱，ylabel 設定縱軸名稱。"
            aria "最後別忘了呼叫 plt.show()，圖表才會真的顯示在螢幕上。"
            jump mpl_clear

        "選項 B：\nplt.label('Revenue')":
            aria "AttributeError：pyplot 沒有叫 label 的函式。想一想，標題和軸名稱，各有各的專用函式。"
            jump mpl_q3

        "選項 C：\nplt.print('Revenue')":
            aria "print 是 Python 輸出文字到終端機的功能，不會把文字畫在圖上，pyplot 也沒有這個函式。"
            jump mpl_q3


label mpl_clear:
    $ mpl_done = True

    "牆上的儀表板一塊一塊重新亮起。折線清楚地沿著月份上升，標題與座標軸名稱整齊地排在圖的周圍。"
    boss "太棒了！這下財務長終於能在下午的報告裡放心使用了。"
    sys "【系統提示】視覺化模組修復完成。圖表正確性評測通過。"

    show aria talk:
        zoom 1.2
        right
    aria "你學會了匯入、畫線和標示說明，這三步就是 Matplotlib 最基本的流程。"
    aria "接下來，我們繼續往前走吧。"
    hide aria talk

