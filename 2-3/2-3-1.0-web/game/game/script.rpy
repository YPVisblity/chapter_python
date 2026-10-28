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

    sys "【警告】情報爬蟲被網站拒絕，外部資料無法取得。"

    aria "這裡是第二層的情報節點室。"
    aria "牆上的螢幕連著外部網站，但現在每一條連線都亮著紅燈。"

    aria "這一關要教的是網路爬蟲。"

    aria "爬蟲不是蟲。"
    aria "它是一段會自動拜訪網頁、取得資料的程式。"

    aria "例如你想取得新聞標題、商品價格、文章內容，就可能會用到爬蟲。"

    aria "Python 裡常用 requests 來送出網路請求。"

    show crawler_code:
        xalign 0.5
        yalign 0.35
        zoom 2.0

    aria "先看第一行。"
    aria "import requests"
    aria "這代表我們要載入 requests 這個工具。"

    aria "接著設定 url。"
    aria "url 就是我們想拜訪的網站地址。"

    aria "然後 requests.get(url) 會向網站發出 GET 請求。"
    aria "GET 的意思可以先理解成：向網站要資料。"

    aria "網站收到請求後，會回傳一個 response。"
    aria "response 裡面有很多資訊，例如狀態碼和網頁內容。"

    aria "response.status_code 可以查看狀態碼。"

    aria "如果是 200，通常代表成功。"
    aria "如果是 403，代表 Forbidden，也就是被拒絕。"
    aria "如果是 404，代表 Not Found，也就是找不到頁面。"
    aria "如果是 429，代表 Too Many Requests，也就是請求太頻繁。"

    menu:
        "如果 response.status_code 是 200，通常代表什麼？"

        "請求成功":
            aria "答對了！"
            aria "200 通常代表網站成功回應，資料有機會被正常取得。"
            $ score += 1

        "網站拒絕請求":
            aria "這比較像 403 Forbidden。"
            aria "200 是比較好的狀態。"

        "頁面不存在":
            aria "這比較像 404 Not Found。"
            aria "200 代表請求成功。"

    aria "可是這個情報爬蟲一直收到 403。"
    aria "也就是說，網站不是壞掉，而是不想把資料交給我們。"

    aria "為什麼呢？"
    aria "因為有些網站會檢查請求是不是像正常瀏覽器送出的。"

    aria "如果 Python 直接用 requests.get(url)，看起來就很像一段自動程式。"
    aria "網站可能會覺得可疑，然後拒絕。"

    aria "這時候常見做法是加上 headers。"
    aria "headers 就像是請求附帶的身份資料。"

    aria "其中最常見的是 User-Agent。"
    aria "User-Agent 可以告訴網站，這個請求是由什麼瀏覽器或工具送出的。"

    menu:
        "爬蟲收到 403 Forbidden，最可能需要補上什麼？"

        "User-Agent headers":
            aria "答對了！"
            aria "加上 User-Agent 後，請求會比較像一般瀏覽器送出的請求。"
            $ score += 1

        "把 print(response.text) 刪掉":
            aria "不是喔。"
            aria "print 只是顯示內容，不會影響網站要不要回應我們。"

        "把網址全部改成大寫":
            aria "不是喔。"
            aria "網址不是這題的重點，重點是請求的 headers。"

    aria "不過要注意。"
    aria "加 User-Agent 不是萬能鑰匙。"

    aria "有些網站還會檢查 cookie、referer，甚至使用 JavaScript 產生內容。"
    aria "如果資料是 JavaScript 跑完才出現，單純 requests 可能抓不到。"

    aria "爬蟲也不能亂用。"
    aria "要尊重網站規則，注意 robots.txt，不要短時間大量請求。"
    aria "如果網站有提供 API，通常應該優先使用 API。"

    hide crawler_code

    aria "螢幕上的 403 Forbidden 開始消退。"
    aria "紅色連線一條一條轉成綠色，情報節點重新同步。"

    sys "【情報爬蟲】連線恢復。外部資料通道已開啟。"

    aria "做得好。"
    aria "這一關的重點是：爬蟲不是只有抓資料，也要理解網站怎麼回應你。"

    return