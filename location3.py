#https://xyzservices.readthedocs.io/en/latest/api.html#xyzservices.TileProvider

import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import folium
from streamlit_folium import st_folium      # streamlitでfoliumを使う
import csv
import sys
from folium import IFrame


# ページ設定
st.set_page_config(
    page_title="streamlit-foliumテスト",
    page_icon="🗾",
    layout="wide"
)

st.title('My Favorite Locations')
st.caption('おすすめの場所')

#img = Image.open('.\picture\moritaHikaru.jpg')
#morita = st.image(img, use_column_width=True)


# 地図の中心の緯度/経度、タイル、初期のズームサイズを指定します。
m = folium.Map(
    # 地図の中心位置の指定(今回は栃木県の県庁所在地を指定)
    location=[36.56583, 139.88361], 
    # タイル、アトリビュートの指定
    tiles='https://cyberjapandata.gsi.go.jp/xyz/pale/{z}/{x}/{y}.png',
    attr='都道府県庁所在地、人口、面積(2016年)',
    # ズームを指定
    zoom_start=6
)

#画像を表示する
#https://ken-ohwada.hatenadiary.org/entry/2023/08/08/131629
FORMAT_IMG = '<img src="{src}" />'

img1 = 'https://lh3.googleusercontent.com/pw/ABLVV877YBko63NJIhLVRzIXfz6PSg7q-HOMNKGHUG_vFGLHyfqOgRjZ0ZvjPfXnkb3Fz7LLpI5eaRSWJwnvY_pGk25Zr1eWbgo3hEmjrswWycIj89AV61eHMwp-IWvrPgJUb6iVYGOQdCxvwemh47SeIigHCmGG8vUMbZxICaha50IRJFmpmJvC7fZOPNowAebDza_YnVutVe5uwxlRn9UECEet0Wt4pICRPz8S8xBpbkd8UHVdbAk48zaHBuA-fH-mfmBuXtCZ2C8avifXOx4lNY2wl6IZYPo8nugT80sk0smfhbxApe0c9OAMsxF3hhjCj_ZhRuOzb4Nse2Oi3aSM_PwD0SGXmL_OzbHdbsd71mVEawuccP-uSNnj7p1qQ1iKyV-hZ15RWg9hD1RFW-rKsB1eRJkJy8Fgj9gdM_blbORBcr6Mg05GsUIMfHJIvK5qr3wlOOav544tHVnn2Ia8CzK3YMHP3RKHJUmXDk6xa9Xl9kcl-kno_aVrlFssQJ43hDAJKCygCgmSSqXq1MVLgwNcS8tdObxte4mOSyBgLQYj2g7EaalphdgddXhicwV9bs4Ej9eO08oP5idxjyHIQhrazfxlfEsUTPhqHMm3hBHwH4vNqKnPPFWtp2Y0NA_2Cyb_0Q2sSUreJ9aNGdEXOCvnkP9wCPf5l5IZEMVsNQ8VGCeJq-x2_9eVsYzjItruFZyTBHvHaxTUaeu6wF1NaaNNaSeqiaCqnN56ElnRwn3z_DBBlRYLYrE8yMJI5cQ-EhhN6JqmQHGlthrlRUU507q21k5DqlLAJW668P7e5CUlRgA8taU88qZ9rgeOb5SdOrv1vSKFXBAbSZvJDSdgJzywVfZ6x3LhRnQQQnJBsF61N1GL58fYoCSq4uX2AIVzfXNMBqEdvYKoKqI1c9hmT0GE3Uk0zGoTeGREv7Zvns07-TnmA5kiB-CYhis=w226-h225-s-no-gm?authuser=0'
html1 = FORMAT_IMG.format(src=img1 )
folium.Marker(location=[36.65139, 138.18111], popup=folium.Popup(html1, img_width=6)).add_to(m)

img2 = 'https://lh3.googleusercontent.com/pw/ABLVV853z8fr8YKhy0YIFUd6qNSMsdKnd35JHosdtU_cYeG4GWdauTOYf7Q4OBqKY66kmTU6-82bVywbg9oK1o1bwZNqEQ1xQdJcIUdEf8ZkYpI79XVSg1OoUNJHN-8OV0ztXFs8-dG79yjGn3pJNrFQSsBG8NQyypjbhfE9zVu9k5j3UNF6WLfy2Ybvkger5l0KkgixSwQU-o2CKbSiLe74ahG7yFQ2daxFB9OUtUFAzOvNPvol5Ej5utghIhW7kq-rrXpStuQPLl-sf-ypAqjZlC8zZuItb26b6ZSA1CBZoUGFKxMfDWrugoyuP8_W3Usk1K6u0lwO73QRKffV08Z0cPaJk8cfq_6jAsO6A3YJNtPMovcZiGL0fle6YqtC9pYguHKT-TjArNb8w3lu_2CpogzrSwnqcjSsWKFa37ta8CYmWuGW2RnVvihEFobLRiX0g-E1l_Ptqv7b4TgvgsyRcb3s3qeJpSMOJbwc8tGIVCBg6pNLGO34eWz8lS1rCC9uD-RHXidVnQ7pmM-ykj6ZQxMfnNjlo3-hsiCPV8WIjSqv_YR2eFZyiGy-h1ztzw-KkQCW9Lfm6JjoNao-3qwDMHbkLNV-m3weV_vIXyAv37e1ajIQR2sqYCjKo1T3Y9K6mPn-1CikpIp9-BWBbAk_PeGY0joeCxS-lFwUpKA3TKJyJmnNsacg3nu597uVAE3UQjPjReKUyA150YWuDfjSb4CyIkwIvaQYheVVcNvi6hKizUDhBXiWMjGRG0WFCOUkQa5cuVA2mvCEjNw1wNbTzH-brD-krCDQ2MijgfmBSh8jBfgqpvYCsai00YrF2TcoPRUHZ52kyx12yx5_rOfbXBWWOezZkPfbpKrJLzyE41JfwbrZQaBuoQRHrQ370FPgshPfYP0W6HIwHEi4oZppuHuU4UvphndYIdPXVbFGXRIwOKKR4wlkakFByhQ=w350-h350-s-no-gm?authuser=0'
html2 = FORMAT_IMG.format(src=img2)
folium.Marker(location=[34.583465, 135.458955], popup=html2).add_to(m)

img3= 'https://lh3.googleusercontent.com/pw/ABLVV86-0o9cVaECcnFgXlcNOhbXWembHPwvUydq4_FIQdrv3waEeUEj7J5mMDbBg4YViyMALxJY5ZYMo3Sr_nCIwBHVQaOEfEXhPdxtGGH6mquBh1a3q4VNRtB8Ra06LLeoW6Yaf-bv1iUCDxac4smT3TKxTwhMLotwEQMdXU2wbFVRUzRkUId4x5JuiXEnQTCu35peZn6Bw470LFizHd3c-iRigclF5HCumGhvholX-LfH-qdM_B0T3RuHLnYErtJtvag-vJnvSpfOMX1T6eneuN0jORidSa4dIvqCLUvnTj3mvaApEIfRMjsz_aboKv-C2Li0NTTrqEG-QApPcNIjMSVLhYDKMHQcpxrEhJQPPVhyGUVER26VajFnIjU0dphz_2VZ4u2rQczPQQSCCXDx4c7QuVUx3eRjL6pKr3hrsqV3VjxKfkSXnf_raMUegH4Cw6UEKZqEQgfllH-cD9Hes1IzTeii1AQVOzn_0yFZAgRrsA9xmfdGswPdRxd7rkeMlo1GLqvlgbMlGYgnWR_G-_9rmU_m_B1ZfCsQUhXjumyv3TPwrKBX3E7e9gHi42ziyHgTaoJXw0ztaIazhx1ovJKp5m3JUEGx1AnOAFrBT_4OhfwoUjAjhby7haRRxl06lVBHaJ_iCUjuyG_TLGxNb4ztlAo5pykkWM0gX2WZZhsJGltxiRtmYPNuXsAx_0uZylprvHuzlTvbgIrSvUu0awH1KiPP-tdZIh-fMuN8km4pp_WLmtcgxk8ODWbQVbQoOVQWaLN1CxaNorgcpqqHTKzHZ4clygTbhpKBpsxMel1ncWbmWhFrNwRnPcyOSR2LaxZ3LnvE-OkCvL4FokfXvQ0DdyXEaEXvJIjjNIaRz4m8yVAAay71Dldl1KuE4dHrdMB6ZV3EndXhl7Alm4J8W2_wBE-YyAGCEq8pVJGvJpFdL2hbjcHN_jvgOOI=w300-h300-s-no-gm?authuser=0'
html3 = FORMAT_IMG.format(src=img3)
folium.Marker(location=[34.352585, 130.840947], popup=html3).add_to(m)



#for i, row in df.iterrows():
#    pop = f"(row['観光名所'])",
#    popup = folium.Popup(folium.element.IFrame(html=html, width=420, height=320), max_width=2000)
#    folium.Marker(
#        location = [row['lat'], row['lon']],
#        tooltip=['都道府県名'],    
#        popup=folium.Popup(popup, max_width=300),
#        icon = folium.Icon(icon="home", icon_color="white", color="red")
#    ).add_to(m)


st_data = st_folium(m, width=1200, height=800)

