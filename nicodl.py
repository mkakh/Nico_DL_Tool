#-*-coding: utf-8 -*-
import requests
from lxml.html import fromstring
from urllib.parse import parse_qs

# ID
video_id = input("ID> ")

# セッション作成
s = requests.session()

# アカウント設定
params = {
	'mail_tel': '******@gmail.com',
	'password': '*******'
}

# ログインしてCookieを取得
r = s.post('https://secure.nicovideo.jp/secure/login',data=params)

# 動画本体のURLを取得
r = s.get("http://www.nicovideo.jp/api/getflv?v=" + video_id)
flv_url = parse_qs(r.text)['url'][0]

# 動画のタイトルを取得
r = s.get("http://www.nicovideo.jp/watch/" + video_id)
doc = fromstring(r.text)
title = doc.head.find('title').text.split(' - ')[0]

# ファイル名に使えない記号を削除
for c in '¥/:*"><|':
	title = title.replace(c, '')

# 動画をダウンロード
with open(title + '.flv', 'wb') as f:
	r = s.get(flv_url)
	f.write(r.content)

