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
    scene black
    show aria talk
    aria "現在們我來到第三層了~"
    aria "這層的最開始也要進行慣例的員工培訓，配備有基本部份的教學還有進階部份的教學，那user你想進行哪種呢，雖然兩種都能重複進行啦~"
    aria "基礎篇會教陣列、堆疊、佇列。"
    aria "進階篇會教串列反轉、樹、二元搜尋樹，還有 Graph 和 BFS。"

    menu:
        "要先進行哪種部分呢？"

        "基礎篇：陣列、堆疊、佇列":
            jump basic_path

        "進階篇：樹、BST、Graph 與進階操作":
            jump advanced_path

label basic_path:
    scene black with fade
    show aria talk

    aria "好，那我們先從基礎篇開始。"
    aria "基礎篇的目標很單純：知道資料怎麼排、怎麼放進去的、怎麼拿出來的。"

    call teach_array_and_list
    call teach_stack_basic
    call teach_queue_basic

    aria "基礎篇到這裡結束。"
    aria "現在你已經知道陣列像一排格子，堆疊是後進先出，佇列是先進先出。"
    aria "有了這些觀念，就可以處理資料結構的前幾題了捏。"

    menu:
        "接下來要做什麼？"

        "去進階篇":
            jump advanced_path

        "重新選擇篇章":
            jump start

        "結束教學":
            return

label advanced_path:
    scene black with fade
    show aria talk

    aria "那我們進入進階篇。"
    aria "進階篇比較像在修一台複雜機器：不只是要知道資料在哪，還要改變它們的連結和走訪順序。"

    call teach_linked_reverse
    call teach_stack_advanced
    call teach_queue_advanced
    call teach_tree_traversal
    call teach_bst
    call teach_graph_bfs

    aria "進階篇到這裡結束。"
    aria "如果你能看懂節點怎麼移動、樹怎麼走訪、BFS 怎麼一層一層搜尋，資料結構這層就不會太可怕了。"

    menu:
        "接下來要做什麼？"

        "回基礎篇複習":
            jump basic_path

        "重新選擇篇章":
            jump start

        "結束教學":
            return

label teach_array_and_list:
    aria "那我們就前往比較簡單的這間吧~，試著了解看看陣列以及他的功能"
    aria "陣列可以想像成一排有順序的正方形箱子，每個箱子都有位置。"
    aria "Python 的 list 也很像一排箱子，可以使用索引拿資料。"
    aria "搜索時通常從 0 開始，所以第一個資料的位置是 0而不是 1。"
    aria "如果你要把資料收集起來，最常見的方法是建立一個空的list，再把資料依序放進去。"
    aria "append 的意思是把新資料加到陣列的最後面。就像是你走到排隊隊伍的最後，再把新資料放上去。"
    aria "linked list 也是同樣精神，只是每個節點除了 data，還會記住 next 指向下一個節點。"
    aria "append 是接到尾端，insert 是插進指定位置，delete 是讓前一個節點跳過要刪除的節點。"
    aria "現在考考你一些問題>w<"

    menu:
        "list 的第一個資料索引通常是多少？"

        "0":
            aria "沒錯滴!通常是從0開始。"
            $ score += 1

        "1":
            aria "雖然這比較像是人類的想法，但可惜在電腦上不符合，電腦通常由0開始而不是1。"

        "-1":
            aria "不是喔~這個是最後一個的意思。"

    return

label teach_stack_basic:
    aria "第二個部分我們從Stack開始"
    aria "Stack的規則是後進先出。最後放進去的資料，會被最先被拿出來。"
    aria "你可以把它想成一疊盤子。新的盤子放在最上面，要拿也會先拿最上面的。"
    aria "push 是放進堆疊，pop 是從堆疊頂端拿出來，peek 是只看最上面但不拿走。"

    menu:
        "Stack 的資料取出順序是什麼？"

        "後進先出":
            aria "答對了！Stack 就是後進先出。"
            $ score += 1

        "先進先出":
            aria "這是 Queue 的規則，不是 Stack。"

        "隨機取出":
            aria "不是喔。Stack 有固定規則。"

    return

label teach_queue_basic:
    aria "第三個部分我們來學學佇列吧，佇列的英文叫做Queue"
    aria "Queue 的規則是先進先出。最早進去的，會被最早被處理。"
    aria "就像是你進食堂排隊打菜，最先排的會先拿到食物，這就是先進先出。"
    aria "enqueue 是加入隊伍的尾端，dequeue 是從隊伍的前端取出。"

    menu:
        "Queue使用哪種來處理內容的優先級"

        "先進先出":
            aria "答對了！先送出的工作會先被處理。"
            $ score += 1

        "後進先出":
            aria "這是 Stack 的規則。"

        "只處理最大的資料":
            aria "那比較像某些優先佇列，不是這題的 Queue。"

    return

label teach_linked_reverse:
    aria "那我們就選擇比較難的這間吧，看到這扇門了嗎，這扇門要你是用串列的反轉功能。"
    aria "串列的反種不是把結果倒過來顯示，而是真的要改變每個節點的 next 指向。"
    aria "你需要三個角色：prev、current、next_node。"
    aria "prev是記住前一個節點，current是目前的節點，next_node用來預先保留下一個節點。"
    aria "為什麼要先保存next_node這個呢？是因為你一旦改掉current.next，就可能找不到原本下一個節點了，所以要先把這個給記下來。"
    aria "每走一步，就把 current.next 指回 prev，然後三個變數一起往前移動。"
    aria "最後把 head 改成 prev，整條串列就反過來了。"
    return

label teach_stack_advanced:
    aria "現在我們成功進到這間了，就由我來教教你如何中序轉後序吧!"
    aria "中序表達式就像是A+BxC，人看起來自然，但電腦處理起來時的優先順序就比較麻煩了。"
    aria "後序表達式會把運算子放到後面，讓電腦進行計算順序時會更為清楚。"
    aria "做法是由左到右掃描。遇到字母就輸出，遇到左括號就push，遇到右括號就pop到左括號為止。"
    aria "遇到運算子時，則要看堆疊頂端運算子的優先順序。優先順序高或相同的，要先pop出來。"
    aria "這就是Stack很適合處理暫存符號的原因。它能記住最近看到但還不能馬上輸出的運算子。"
    return

label teach_queue_advanced:
    aria "現在要使用兩個Stack做Queue 來當作測試用的零件。"
    aria "這方法很有趣，那是因為 Stack 是後進先出，Queue 是先進先出，看起來剛好相反。"
    aria "解法是準備兩個 Stack分別為：stack_in和stack_out。"
    aria "enqueue時，把資料push到stack_in。"
    aria "dequeue 時，如果stack_out 是空的，就把stack_in 的資料一個一個 pop 出來，再 push 到stack_out。"
    aria "這樣順序會被反轉一次，剛好變回 Queue 需要的先進先出。"
    aria "簡單說：進來先放 stack_in，要出去時倒到 stack_out。"
    return

label teach_tree_traversal:
    aria "現在我們需要看看這張地圖，有沒有絕得很像一顆樹分支出去，現在要跟你說這樹的功能"
    aria "樹不像 list 是一直線，它會分成 root、left、right。"
    aria "走訪順序不同，結果就不同。"
    aria "中序是左、根、右。後序是左、右、根。"
    aria "層序則是一層一層看，通常會用 Queue。"
    aria "遇到樹的題目時，先試著明白：要使用哪一種順序？"
    aria "如果是遞迴走訪，就先處理子樹，再把結果給收集起來。"
    return

label teach_bst:
    aria "既然我們知道樹了，那就必須告訴你BST 二元樹的功能與使用方法"
    aria "BST 的規則是左邊小右邊大。比根小的資料往左，比根大的資料往右。"
    aria "搜尋時不用整棵樹都看。target比目前節點小就往左，大就往右。"
    aria "刪除節點時會比較麻煩，因為要維持 BST 的規則。"
    aria "刪除葉節點最簡單，直接移掉。只有一個子節點時，用子節點接上去。"
    aria "如果有兩個子節點，常見做法是找右子樹中最小的節點來替代。"
    aria "這就是find_min的用途：一路往左走到底，找到最小值。"
    return

label teach_graph_bfs:
    aria "接下來就是最後了，最後有Graph、DFS、BFS，來試著了解看看吧~"
    aria "Graph 是節點加上邊，適合表示地圖、朋友關係或迷宮通路。"
    aria "BFS 是廣度優先搜尋，會先看離起點最近的一層，再往外擴散。"
    aria "BFS 通常會用 Queue，因為先發現的節點要先被處理。"
    aria "visited 用來記錄拜訪過的節點，避免一直繞圈。"
    aria "最短路徑題會再多記 predecessor，也就是每個節點是從誰走過來的。"
    aria "找到終點後，從終點一路往 predecessor 回推，再反轉，就能得到起點到終點的路徑。"
    aria "現在問你一些問題"
    menu:
        "BFS 通常會搭配哪一種資料結構？"

        "Queue":
            aria "答對了！BFS 需要先發現先處理，所以適合 Queue。"
            $ score += 1

        "Stack":
            aria "Stack 比較常用在 DFS 或需要後進先出的情境。"

        "BST":
            aria "BST 是搜尋樹，不是 BFS 最常用的輔助結構。"

    return