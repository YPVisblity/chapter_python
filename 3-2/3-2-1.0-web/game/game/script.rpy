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

    sys "【警告】第三層資料通道堵塞。任務順序無法判斷。"

    aria "這裡是資料調度室。"
    aria "系統裡有兩種資料通道，一種是 Stack，一種是 Queue。"
    aria "如果用錯資料結構，資料就會照錯誤的順序被處理。"

    aria "我們先複習一下。"
    aria "Stack 是後進先出，最後放進去的資料會最先被拿出來。"
    aria "Queue 是先進先出，最早排隊的資料會最先被處理。"

    aria "假設現在有一疊維修卡片。"
    aria "你先放入 A，再放入 B，最後放入 C。"

    menu:
        "如果這是 Stack，第一個被 pop 出來的是誰？"

        "A":
            aria "不是喔。A 是最早放進去的。"
            aria "Stack 會先拿最後放進去的資料。"

        "B":
            aria "差一點，但 B 不是最後放進去的。"

        "C":
            aria "答對了！"
            aria "Stack 是後進先出，所以最後放入的 C 會最先出來。"
            $ score += 1

    aria "很好。Stack 很適合處理需要『回到上一個狀態』的情況。"
    aria "像是撤銷操作、括號配對、遞迴呼叫，都常常會用到 Stack。"

    aria "接著看 Queue。"
    aria "現在有三個修復任務排隊：A、B、C。"
    aria "A 最早進來，C 最晚進來。"

    menu:
        "如果這是 Queue，第一個被 dequeue 出來的是誰？"

        "A":
            aria "答對了！"
            aria "Queue 是先進先出，所以最早進來的 A 會先被處理。"
            $ score += 1

        "B":
            aria "不是喔。B 在中間，不會第一個出去。"

        "C":
            aria "這比較像 Stack 的結果，不是 Queue。"

    aria "Queue 很適合處理排隊任務。"
    aria "例如列印工作、客服等待、下載佇列，還有 BFS 搜尋。"

    aria "所以這一關的重點是："
    aria "Stack：後進先出。"
    aria "Queue：先進先出。"
    aria "選對資料結構，資料才會照正確順序移動。"

    sys "【資料調度室】順序修復完成。"

    aria "做得好。下一關就要用這些順序觀念，去處理更複雜的資料地圖了。"

    return
