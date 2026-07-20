# 2026 關西晚夏行程網站

大阪為基地的 2026-08-26 至 2026-09-02 靜態多頁網站，涵蓋大阪、奈良、堺、神戶及箕面。

## Pages

- `index.html` — 概覽與時間敏感提示
- `daily.html` — 每日時間軸、交通 buffer、可刪項目
- `culture.html` — 五條文化閱讀線
- `museums.html` — 入館焦點、最後入場、展期修正
- `food.html` — 十二個餐段與胃口管理
- `maps.html` — 每日路線與 Google Maps 入口

## Update workflow

1. 編輯 `data/itinerary.json`
2. 執行 `python3 scripts/build.py`
3. 執行 `python3 scripts/validate_site.py`
4. 本地預覽：`python3 -m http.server 8000`

網站不公開訂位編號、姓名或酒店確認資料。館舍時間及路況在出發前仍須以官方公告再核對。
