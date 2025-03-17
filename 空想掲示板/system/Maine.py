import webview

def create_window():
    # 500x500 のウィンドウで指定のサイトを表示
    window = webview.create_window("空想掲示板", "https://sites.google.com/view/uto-tz-nm/%E6%96%B0%E6%8E%B2%E7%A4%BA%E6%9D%BF", width=500, height=500)

    # 実行
    webview.start()

# ウィンドウを作成して実行
create_window()
