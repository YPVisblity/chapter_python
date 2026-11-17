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

    sys "【警告】第三層核心地圖損壞。節點連線無法判斷。"

    aria "這裡是資料地圖室。"
    aria "前面我們學過一排資料，也學過資料怎麼進出。"
    aria "但現在資料不是排成一直線，而是分成很多路線。"

    aria "這時候會用到 Tree 和 Graph。"

    aria "Tree 可以想像成一棵樹。"
    aria "最上面的節點叫 root。"
    aria "每個節點下面可以接其他節點。"

    aria "如果是二元樹，每個節點最多有兩個孩子。"
    aria "通常叫 left 和 right。"

    aria "例如一棵樹可能長這樣："
    aria "根節點是 10，左邊是 5，右邊是 15。"

    menu:
        "在二元搜尋樹 BST 裡，比 root 小的值通常會放在哪邊？"

        "左邊":
            aria "答對了！"
            aria "BST 的規則是左邊小，右邊大。"
            $ score += 1

        "右邊":
            aria "不是喔。比 root 大的值才會往右邊放。"

        "隨機放":
            aria "如果隨機放，就不是 BST 了。BST 有固定規則。"

    aria "BST 的好處是搜尋比較快。"
    aria "如果目標比目前節點小，就往左找。"
    aria "如果目標比目前節點大，就往右找。"
    aria "不用每個節點都看一遍。"

    aria "接著是 Graph。"
    aria "Graph 是由節點和邊組成。"
    aria "它很適合表示地圖、道路、網路節點，或角色關係。"

    aria "如果我們要從起點找出口，就可以使用 BFS。"
    aria "BFS 是廣度優先搜尋。"
    aria "意思是先找離自己最近的一層，再慢慢往外擴散。"

    aria "BFS 通常會搭配 Queue。"
    aria "因為先發現的節點，應該要先被處理。"

    menu:
        "BFS 通常會搭配哪一種資料結構？"

        "Stack":
            aria "Stack 比較常見於 DFS，因為它適合一路往深處走。"

        "Queue":
            aria "答對了！"
            aria "BFS 需要先發現先處理，所以很適合 Queue。"
            $ score += 1

        "字串 string":
            aria "不是喔。字串是文字資料，不是用來安排搜尋順序的主要工具。"

    aria "搜尋 Graph 時，還需要一個 visited。"
    aria "visited 用來記錄哪些節點已經走過。"
    aria "不然如果路線繞成一圈，程式可能會一直重複走同樣的地方。"

    aria "所以這一關的重點是："
    aria "Tree 是有層級的資料。"
    aria "BST 用左小右大的規則加速搜尋。"
    aria "Graph 是節點和連線。"
    aria "BFS 會一層一層搜尋，通常搭配 Queue 和 visited。"

    sys "【資料地圖室】節點連線恢復。"

    aria "做得很好。"
    aria "現在你已經不只是會處理一排資料，也能理解資料之間的路線和關係了。"

    return