<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/ke3b3Gc471rX_h0QW-7LvCQQIhGdjPTTFbT9vtWB-DVPMhbzrA_OG7pX3TxZoD5X9oSv8QZX08TOIblWwfUkBhCNPxfOcP_QNoL5QIFWFJ1jA65qG9oiXk4bQgj56OsJJ9Ve-UraBGRC--1hu0jT0SjtvXkoMh63rKTXfiQ1-b6NotS6pE84nyHVC9JIF_GeHEtzy8ZgtQacCd0I8cpCQHwNAJDjesPJl76r_ifUpMbhGhTJEjTAQsxvuYkqvCuFA-MhGoyfLEeHmCBGkWOsTJpaQi19Y8ygkBFhCbLFin_yV4Fv2yqWtI-kOWTg4h6ybrqZYIQwC5Icfh2bhzMgEw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 169K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 16:54:32</div>
<hr>

<div class="tg-post" id="msg-23056">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQxHKV6Ia_zKH58kfAd2YcFkDMEO2ZsfyYHIUuGYZrmE6bm1oOoGcxrehrWL9NV-KDrZz3PZEfXYAvv5CnHBJGDpMZVMbgwsPsn5N_MBNLWcwshUk8TeZrXrLYFXGsWFoJwQUOzXfp8SwenwlZL2dxkn1KvhrKp0t2XlAqle87r9C1Bmg6Kcr22euH9W-OVlh0XUhJGGNDWPc7lylD0mhmNI0WZHuxeBrPewJ9fy_Jeo0g-_YXVUgFfDEFq9PIuWA625T4JrDtEvScEi9B9KUaHCCnn7htSddlS__clhgdMCkA1uVK3fTXRP2WVbXo9Ph3xz1c67SS9im2o5CPTkFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فلورین‌پلتنبرگ‌خبرنگاراسکای: علی رغم تماس های تلفنی با هانسی فلیک؛ خولیان آلوارز ستاره 25 ساله اتلتیکو مادرید از پیوستن به تیم رئال مادرید استقبال کرده و گفته اماده این انتقال هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/persiana_Soccer/23056" target="_blank">📅 16:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23055">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9MwsZGnibxUquhxbGl3NFi6qWZXNHB6OIcISwdTBnFbd_zVOf_-UwN-4vIflGfG2iSt1DZyyjgcMathPgB9-ZNshmoL7rGV0kUQWnax3lJWpgsd1wNtWmKbxBx_UwVtNcpfg9D59qbBq5h0cMmgsqhBgUWt_rQRFKis42UDcmK244M9JIKRhJGadD0j_KxLGu_nR6UJ9FvJKo7LTLjvzHd7PHcuhVW332nYy9mDn6WaIlsB0zijdy3Rh-whgmcxVaFoJQauBcU-Gk3LOw96kHFem_m3ZNEiykVifsvHMO4HFTdxpRg04eJhahgR6gPGo7tdnmBltOGDhnCcaJt5Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
عدالت در میدان، هیجان در جهان؛ جام جهانی با بزرگ ترین تیم داوری تاریخ‌فناوری های پیشرفته VAR و قوانین جدید پا بمیدان میگذارد از شمارش معکوس‌برای‌اتلاف‌وقت‌تا اختیارات‌بیشترکمک داور ویدئویی؛ همه‌چیز برای‌تصمیم‌های‌دقیق‌آماده شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/persiana_Soccer/23055" target="_blank">📅 16:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23053">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tq1_ZVeFLnwqlfLideuB7NQqyb2yNzJujAV3AGRP84uQPOmuS86ZBiUOs3Zkf9SprMQRRt43pskOmf3tiTPT6VafZj2aMvSulZCCPghH9ZKjFwrjo4lssKfmINkjyS7q--KRVUPco1xqw6mXBFQvGGNQ6JtDIe1Up6sMkkqikuUgqdO4IFeS865iwJtBxepAfhtEdMg7dss4xD6ao6dQWRhlN3vbmH6-ELC4hD_DcptKj4g77cr5AJw7Xwp5cDGPTLEhOhuGgqWgGXKUyVHDHOT7GXmJOlRFFiWkQ3xOygfjXs2HxYMdcuEYgSo5MRNQjCSG3-wBAzxfQ-5jQFanHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ اوسمار ویرا امروز صبح‌درتماس‌بامدیران باشگاه پرسپولیس اعلام کرده که به قراردادش با سرخپوشان پایبنده و به‌زودی برای پیگیری تمرینات تیم وارد تهران خواهد شد اما توقع داره که در نقل‌ و انتقالات تمام بازیکنان مدنطرش توسط مدیریت…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/23053" target="_blank">📅 16:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23052">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6daa12069a.mp4?token=NzcHMK4QQzN8Hg_YQ52-U_W35kcq7UXQ6B5H5x8iWQGEfteFTCFjmKjoeqabDz164sCtrUvM1thQDej8Ws_2bl6am4vGiWK1uqIxvZdSQmo_D-sUFA9jWGlmYQA9kJ-nYpqCkNM_s0T-XBUc4AtIjOExTXUg3Zmtks66n-mLN3VMDhVj4n-LgP0E6SviPTRQRWBgoViqQfOIKq1Np-SVfyuWdil0fhSs_Zpu2pW5acGNYGZutbPxqBvf4wlcdhOJ4Q733WJN4Um9FKhA6O5oKHcyUx_lKE2Bmy3CG1tQR0WvclDmeCOogiXsrooGT0Q5uin1Mb9uvC1Iuwf7l6VBV7EfO22BOODjVktlSPLmuh31BPyKQ8uqenDFdc0bcjDEnHv1jKcOktVSULTWTiR0sFmNVzPb5rEsplpxKj-oi8EdfdCwEEx2m2zbpTVzCqagmhDW0YX6xM0JYieh7jffGjY8jV4e7onYblk1bq6tZ4N4Amol5SBAfUiBaGtADfzHGQc8ZnoIN4uhalIWsSZc1IkM0gX_-kTlUDmbBENRynYCVgwMsbVSNAgFts3iakepstbmekPGoannmpNhtSzz9I7CVqIGAhepVFEVKQVnY096epMy1M8C6996T7j38ylU1Imh3Fb5T6zPCSnY_IUomdATEUVxZvjWPvb_wljuYhs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6daa12069a.mp4?token=NzcHMK4QQzN8Hg_YQ52-U_W35kcq7UXQ6B5H5x8iWQGEfteFTCFjmKjoeqabDz164sCtrUvM1thQDej8Ws_2bl6am4vGiWK1uqIxvZdSQmo_D-sUFA9jWGlmYQA9kJ-nYpqCkNM_s0T-XBUc4AtIjOExTXUg3Zmtks66n-mLN3VMDhVj4n-LgP0E6SviPTRQRWBgoViqQfOIKq1Np-SVfyuWdil0fhSs_Zpu2pW5acGNYGZutbPxqBvf4wlcdhOJ4Q733WJN4Um9FKhA6O5oKHcyUx_lKE2Bmy3CG1tQR0WvclDmeCOogiXsrooGT0Q5uin1Mb9uvC1Iuwf7l6VBV7EfO22BOODjVktlSPLmuh31BPyKQ8uqenDFdc0bcjDEnHv1jKcOktVSULTWTiR0sFmNVzPb5rEsplpxKj-oi8EdfdCwEEx2m2zbpTVzCqagmhDW0YX6xM0JYieh7jffGjY8jV4e7onYblk1bq6tZ4N4Amol5SBAfUiBaGtADfzHGQc8ZnoIN4uhalIWsSZc1IkM0gX_-kTlUDmbBENRynYCVgwMsbVSNAgFts3iakepstbmekPGoannmpNhtSzz9I7CVqIGAhepVFEVKQVnY096epMy1M8C6996T7j38ylU1Imh3Fb5T6zPCSnY_IUomdATEUVxZvjWPvb_wljuYhs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یکی‌از آندرریتدترین‌مثلثهای‌تاریخ؛
شاید اگه بیل فکروذهنش گلف‌ نبود و ژوزه اخراج نمیشد، چن جام از جمله قهرمانی در پرمیرلیگ رو بدست میاوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/23052" target="_blank">📅 16:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23051">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yew2zAadQ_MFxtB3ZcgHzWzgOoUVanpvxJBpD0sHHEQ_iDUx331AQaYHTvg0Z6GnxV0munlYb1TB6fTJ7lclcDbAAu5UisWzDvr8YULL3XXHpxe-kRNd-Xx0KOclgS6_c-sw1MOl_UCLqsQYX-F1TvLGq2zV28cSvjOLZK5WHe_ZSZBM8AonWoXE-H2oCx9Iuo1-llfdzpxNQLHUq6n2Mg0QL8AZfirnYKoOjFV6ZsgDxhRDavqGeJPoUr09O7fd_l9OoNfMgTrco3hRdvvqP56-rvjMLqTFRr8ifipwh-vJuUwXvByJNMdsPM0lDznRh6DEjYCc-_4G2bXOvH7l_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام نماینده مجلس؛ یوتیوب و واتساپ تا پایان هفته کامل رفع‌فیلتر خواهند شد. دیگ میمونه اینستاگرام، تلگرام و توییتر؛یعنی یه روزی در آینده نزدیک میرسه این سه تا هم رفع فیلتر بشن؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/persiana_Soccer/23051" target="_blank">📅 14:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23050">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcda08a029.mp4?token=buWMit-iRtLDuIvztztIzRbLd2mxJhl5DsgLzWy4PpLbR6FYjboe_6EJC3s20yqhcBxMG54fUr3JqPFLPDz6L-pnN-RtSVT3YgGGisTi2yrQSpEM_NyQDjJbegUsi6UsKipgxpyyuBSig7AtX-T35RN6ZiMQhnktvl6ruiWB5Tl1uAamHukx1sBtpdOaz2Os4B5HMHHZrVudBkzG-ZmYfCV100ONaS_BOWYjjsdjyWKK2P2uZofU1-HB1rqzYWsCwjrcc96AmKt9CTlnVtPp6Gx6iX5zFYm0wLctcnaUILlQTW6w4T2PFliZnI56kGGDwocgv_oPZG2D8aCD5JgBzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcda08a029.mp4?token=buWMit-iRtLDuIvztztIzRbLd2mxJhl5DsgLzWy4PpLbR6FYjboe_6EJC3s20yqhcBxMG54fUr3JqPFLPDz6L-pnN-RtSVT3YgGGisTi2yrQSpEM_NyQDjJbegUsi6UsKipgxpyyuBSig7AtX-T35RN6ZiMQhnktvl6ruiWB5Tl1uAamHukx1sBtpdOaz2Os4B5HMHHZrVudBkzG-ZmYfCV100ONaS_BOWYjjsdjyWKK2P2uZofU1-HB1rqzYWsCwjrcc96AmKt9CTlnVtPp6Gx6iX5zFYm0wLctcnaUILlQTW6w4T2PFliZnI56kGGDwocgv_oPZG2D8aCD5JgBzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
تیم برزیل در جام جهانی ۲۰۲۶ با هدایت کارلو آنچلوتی و باترکیبی‌ازستارگان‌باسابقه و جوان، فقط با هدف پایان دادن به انتظار ۲۴ ساله برای ششمین قهرمانی‌جهان‌واردمسابقات شده. اندریک قبل از آغاز ماجراجویی‌هاش در اروپا، تمام دوران رشد و شهرت اولیه‌شو درکشور برزیل و بویژه در باشگاه پالمیراس سپری کرد. اون با درخشش در فوتبال برزیل به یک پدیده جهانی تبدیل شد. رسانه‌ها هم سر شوخی رو باهاش باز کردن و روز تولدش رو با پله که اونم ۲۱ جولای بود و ۱۷۳ سانت قد داشت مقایسه میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/persiana_Soccer/23050" target="_blank">📅 14:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23049">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tsg2etBdzN4lX2AiQmYHts1zp0oFDD6-4C4Xwg3I8_LvQDtBqzrNkl-7TgmvSn6jt3oJ6z7U-hFsI7dsJlpcfXnh2rtZYKJvJ6WnUhmzxfLQ4wnVmupzplYzCNRId3hw4yujFdQZLJodt-kGUKu4NXQWznckh27FUgR5kZaW6HGteYZi1jfsVbRqUyBn-TYOYs6NXIdD8AlyxDueKA2ScI5ZokJvc0BBLNZNA59vNGP0PUkLXeMyrw8MhDfFuz2pBCN4m4De2MZAPLU7rJbQ7v7HffwAwz0FH6ww9V-N95egjMtMmd7qglWcClqoQl5LYvkOvFOmj-XT2T2d1m8YBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/23049" target="_blank">📅 14:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23048">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TT7wmEM6szrPOtr-U-zQ6KrBqt9cEfo3eoA8hT5l6NSP6LtjVTWvI-A1ZMPDBvvCorO0sgvAov5UCavA--fkVdh6wRKP8Gfb7OYDj8LVwvUE_9kBqCcebB8gRj69FblmEsBbZlZbehnf26re4SQbtkb4C12kKGpOQJ6znB48h_o7WNwzB9GuuB6lCLmk5BGvj39pauOlYDKwm5dcKd7xrRcXHLs4b1M7P__PHeP6h_wVIg7ZoqUQzB9bnPDHZ4dz_aDJsIBLZO2xFNUeE8DBb2d_CeHIC0Hqt3BJ8VQtHWF56059pivj121jnB6Uw4YHOn0cjVLVGPFAF6Cz04Wezw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/23048" target="_blank">📅 14:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23047">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2qe33IPj1kC7tjToouMyU-j_R7N0pq7ASENWGUfNcHrtpIbHaql1HPUdtBG8mcWlXTUZhC1t7GZaKeizMYvXSBAwJM4XaXRPBr89Vx8UMAPmzBT0RlIoJuPCaL6kSW5Hk9sJbizY1H3m_RwZrHviEzQ5YOdg52xs2LwDQzxf5QpKPOBYiP7iuAsUOvD2tLT6emHl3krhMEuyBZTuKd4fnhvgAqXKLQMuWr8Do2dLYiubRcQXv-sOayI7WiSLvekNyNV0mSddN5YSgjEYYqbAx-C8gFH_hyMT1hXsvzUEzgaRrMteZI22dpugQm-OCAa5ISnuWa77q9u2uXvwPvfJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
طبق شنیده‌های رسانه پرشیانا؛
باشگاه استقلال مبلغ رضایت نامه عارف آقاسی مدافع 28 ساله‌خود را 80 میلیارد تومان اعلام کرده. گفتنیه باشگاه تراکتور به دنبال جذب این بازیکن هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/23047" target="_blank">📅 13:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23046">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMLc16rviNJ38l7Q40CCFvHXoVtGlwHt8iixuLDaUHv2ULvIFOAepM-jpZYRBDrno41t-bUYskQZf9e-V8t_A5cTl0f8uXSJmInT1eDG1yiLQpYWP3gZyEgIzNFFz4ZpiCMeGFKaZkMnCCfauvQEeodkqzusiJfJYI48JixwF4FrskME_oSl5APEu10fz5St2tY08_ps3uW3L1COXTF_2MTu50K97XD5PNAPwBPHB9t4oq9G_s7aW1TFDFET7gU9jc5digrLZOS-ftIXYaJWboU1zUnOgniHHo95usdaLwOBV3XxL42Dn-P0Zr5PMzM4L_4C4L9RZKiKSqbDtsFw8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ ‏گویا پیام‌رسان واتساپ در برخی نقاط کشور رفع فیلتر شد. از یوتیوب، توییتر یا تلگرام به عنوان هدف احتمالی بعدی نام برده می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/persiana_Soccer/23046" target="_blank">📅 13:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23045">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aef75c0b0e.mp4?token=krlPoOcEYfklLDQ8a60NUu2DbF1fgL0a_h-FvqAJGI7LHemY8nGyB8x9Pj1Rp6xN8LaI8zyM9c5K99RMqcmT_jmcR9rxkXAIZzee6wzLv2ejiVJGxCCPsT5SQKr2Vxc7OrcSeA-sO3ngGPooZPP9RrYcP0AeZkVJZyPbQ6JHXXjcJC4wk7c5zlVpM0PzUMoJo06VTlaVSeV3O_gcC5ghNEm_LLFFywzATkXYPRwsAZSJY1D3pVy-Ugpip1oyEOL4XyCAu-zuueMzwkIYY3spdIaoqQ2i3aj5HkwEbGsLJZSTaePlMmoKgNGstCMH-l6ii-H6OEHRlQU1nr-BsKZKnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aef75c0b0e.mp4?token=krlPoOcEYfklLDQ8a60NUu2DbF1fgL0a_h-FvqAJGI7LHemY8nGyB8x9Pj1Rp6xN8LaI8zyM9c5K99RMqcmT_jmcR9rxkXAIZzee6wzLv2ejiVJGxCCPsT5SQKr2Vxc7OrcSeA-sO3ngGPooZPP9RrYcP0AeZkVJZyPbQ6JHXXjcJC4wk7c5zlVpM0PzUMoJo06VTlaVSeV3O_gcC5ghNEm_LLFFywzATkXYPRwsAZSJY1D3pVy-Ugpip1oyEOL4XyCAu-zuueMzwkIYY3spdIaoqQ2i3aj5HkwEbGsLJZSTaePlMmoKgNGstCMH-l6ii-H6OEHRlQU1nr-BsKZKnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
انتخاب آنتونیو رودیگر و لروی سانه بین کریس رونالدو و لیونل مسی دو اسطوره تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/23045" target="_blank">📅 13:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23044">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmbZLcXnc3z2dLT-Nj6eeDUZehMj7eOWysATl40qXTdtUMuEK6LldRKd68uyPC62jvU0gMx3dMhETN_D6HpWA4kImZZlfnhuV6KNLcSqckBH0AfNvgfcipwCeFom6AO2gkq4HZ9KhjTzQkwZmLmZHJhbZq45G3YCMQltClXRv52vrHd5yWbQPrGrl_XPc23p8GHX7UMhTSt2kEgZOrJsKpUb-V9W22ZKT0bb7njaaGFooNPuGJGkV5PfCx1Jsemy6BE96BU2G8cu88u9YOQZpfIILB0TJx4PXoyABBRnxp0gx-1IUdpwd8nnk4ye5ZEf_NqGSX1s6H-HoBNAs6lnnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: خوزه مورینیو از فلورنتینو پرز خواسته هرچه سریع تر از بین یوشکو گواردیول و ریکاردو کالافیوری یکی رو قطعی جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/23044" target="_blank">📅 13:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23043">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WAQ7DVWmQi-xpsbtMiqYZk7vvo06l3WF-hO2OxCSZUsoOAMXZES_B6esQWVo3rSB_c-C-5EqQia9s8RwZOFBSAJ9EJxGSbzJ54Zfb_Nqm3r9szzl51VoFu0CCPWfLNvpJXm4CrCBYV6fmiFEi0RVyRHeth1gy3YDV6-lNeyjekjjfS9XIuvrQXyNSUMqf7lKbKXSNqFy2qldWBsaZw0ksc-Bqf0u8Lgq5307wCUrpxhvXAbR4vVKMBZiTcjO7QekkFZ0uROCECJbhEtES3MmwZGLnlHzJNm3XvpiqqJvPgAjE_64Q_aaK6cOJxBf30TgLWp8ADRYoCTJx6OEvNK2zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تمامی‌قهرمانان‌ادوارمختلف‌جام‌جهانی؛ برزیل همچنان پرافتخارترین تیم تاریخ جام جهانی فوتبال است و با ۵ عنوان قهرمانی صدرنشین است. پس از این تیم ایتالیا و آلمان با ۴ قهرمانی در رده های دوم قرار دارند و آرژانتین با ۳ قهرمانی در جایگاه بعدی قرار گرفته است. جای…</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/persiana_Soccer/23043" target="_blank">📅 12:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23042">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LknVww9Df7rY128ET6TqIfQcmYZG8CeKReUxUjUjVHQwccTEgj3L94ETjWuHk2MvvQuTTrkMR9Sichg33SU5OzzxXJB--T1e7VH3qGK5UKkJlYEco5Aa2au7ahzOg3noMV0CRBHyg9ixn5XJ6UJBpLB6NHcUTuVa-u66WrQYDDnnXWyKSkUO-wFkoL44hIJCOjFfYuecHNd5_p7ZrOWg0jpx8jmWt9z-TgwkAkOKMsYHqSnmo5lYDwThrBbolRGxmHPMcHyOGVBY_xUYKMQLlliSGa-Keg_1E-KIIHVGjZiOE3UDGkQki9xHZ2bcGCUdhqVc86K4zKGfbfBFQnAT0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تمامی‌قهرمانان‌ادوارمختلف‌جام‌جهانی؛ برزیل همچنان پرافتخارترین تیم تاریخ جام جهانی فوتبال است و با ۵ عنوان قهرمانی صدرنشین است. پس از این تیم ایتالیا و آلمان با ۴ قهرمانی در رده های دوم قرار دارند و آرژانتین با ۳ قهرمانی در جایگاه بعدی قرار گرفته است. جای…</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/23042" target="_blank">📅 12:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23041">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXWBv2UqgRD1JqoB54itNYpcBzCKDZD2JrGGPysBj3g6FTMCHFChL9N8LkLIIatpMDWAODsAcoSIplMhS6UCcr6QPnGqGxQ0lGk4zcom8UTzO4fsBpgowC_vh4fcpDhvp5MMETBuX4jd4E0LzRqEUT8UfOPMsjkShAnwlJsY3thvoAg6OjnpY5nKA3CRkFH1NHWsTLmU3K5yOxGODO_y3BmNjbOlDRrG-3wSUWKqtEYnY8sDTLFZSrb22eFxdadANeKBrenb971w13mQoA_zMZs6jnxMbGp9B1QpogVp8Rf_ASTfKCP3Smzd8t9UnhjRXphUWFQEfo8HY8jloUqPBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
یادی ‌کنیم از مصاحبه تاریخی مورینیو بمناسبت بازگشت دوباره به‌یکی‌از داغ‌ترین نیمکت های جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/23041" target="_blank">📅 12:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23040">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiWqMVfXBMKmOjRFgaJLfLdkqWw6Wm4RWeVZ_ALp-cEli-bSfSUVUshIv94mHqGimVJP8jKIwXleknD967Woe1hyKDZX7EnWdDz3tuYZ_BXiZYOGYtjmxzn-XiN0GYGBewRBB9-KtByaAkE6qB8dz3mXP_1b51QVlw9vHfqbFx8Ucb8h2qwa51uGqviVydxsSguzJU-PyODWVkucq-XEYyUR-RAOs6lWKAKc6HINLtSZyWTODgkarbQBS02oPYVZC2n78L3dXlIUY2yXGbt3BJhLfxyYeBTWqvVuF0q6MOII95R80Mk9OJEwL9KtRLpLlLS0HtIv23Bl8DE7N4Ti3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ ایجنت کسری طاهری به مدیران باشگاه روبین‌کازان‌اعلام‌کرده که این بازیکن برنامه‌ای برای بازگشت به لیگ روسیه نداره و قصد داره ادامه فوتبالش رو در لیگ برتر بگذرونه. باشگاه روسی‌ هم اعلام کرده هرباشگاهی یک‌میلیون دلار پرداخت کنه رضایت نامه طاهری رو…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/23040" target="_blank">📅 12:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23039">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4860b42130.mp4?token=Lmnm8DG2TunWKJ7frftE_hO1vaDOeWq3EY_8kMlvD01Geypzz4_DuKUy_w_EtauNWP_ZwSk3RGpDn9Jpvic5_o5Hq3x6BW_832YD2KBFDjW6EPh5B70PlmxSVAMNeordSCz3HfYwkx-rG-aeX5s_aQU8evxWnnNy7XpwzqUvnNaulUD21Vfi1-imaWPEaMJbz6QRdhuOankSyP2ZPmFhT2vetXGrK6nq5LIofqK0v9rHR1rpZXmQhKx9WVruJDWLzmeqiV-U1utp2bEqiimBEIxSf5b-UdHsFfM6nVYMscK2WY-E2tYiVoyCO-RL96PPipcRX8qBOPQBlmk55fIW8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4860b42130.mp4?token=Lmnm8DG2TunWKJ7frftE_hO1vaDOeWq3EY_8kMlvD01Geypzz4_DuKUy_w_EtauNWP_ZwSk3RGpDn9Jpvic5_o5Hq3x6BW_832YD2KBFDjW6EPh5B70PlmxSVAMNeordSCz3HfYwkx-rG-aeX5s_aQU8evxWnnNy7XpwzqUvnNaulUD21Vfi1-imaWPEaMJbz6QRdhuOankSyP2ZPmFhT2vetXGrK6nq5LIofqK0v9rHR1rpZXmQhKx9WVruJDWLzmeqiV-U1utp2bEqiimBEIxSf5b-UdHsFfM6nVYMscK2WY-E2tYiVoyCO-RL96PPipcRX8qBOPQBlmk55fIW8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویژه برنامه جام جهانی با گذر زمان؛
از عادل به یک مجری وسطی بازی بدرد نخور رسیدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/persiana_Soccer/23039" target="_blank">📅 12:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23038">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjGtL0dw4cwnA9p6SsJt2nUOaDD6H9hzuL5uzG7f_Vqk3p2-3o5Zi0DS0WyLFcJu-4UDCvVCU23pNqNYuWoqfEc8EtV32N_mKMQPXpGj9kPvtl06YqZcgM_XBIk1A4--ObTsaKkp7nFXHvhxG9MRvZTNHkPm-CZGvflZSOJm1_RTIXa-kRIPz8wodLZltj86gcaLFRP7f6auYu7h7KIeEdc2NatF356sIhQiqc9Lge5WFkNy2AluaNH1uwCraa9zOadZ3LREZU_v2Jos8y19Girm94iwkwo6Jt7hYG2Ef4JkLVs_0qSqrCs8P-oSXmwG-8oWCeMMu9XqlIA_AD4GHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تیم‌های ملی رکوردار بیشترین تعداد پیروزی در تاریخ رقابت های جام جهانی؛ برزیل در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/23038" target="_blank">📅 12:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23037">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0yGhn08Hof9fUgq2T1Y1QvlT8-WHWP7jAfSWd6BgmuWe33ZfHAYRS-OD8x53O62nkoh0vkEEDoLMhfLRAjK_3qDx1rfCocLpWgjzWllZbmJcRQJXezlHaG9jZofN3AwtFOMS__nr2CTPIIewtE1Oo07p1beeejOHw4BZQXh_bObOONKEp2oYEd5eiBVSfBc0jspAGHKfavVK-R0duaO7teComT9cN3NdJcLKg0vpxUaPedS21LSIKfDwQcYIKihcFKHv0bhO3ChACbY9dbGtIiqFIVd3vXkPt6URqW--JHhZAWX-4YA2fI_ygwxtjuVEXItjUCHr0eGElwngjEUbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕔
انتظارها به پایان رسید
📃
از سایت وینرو رونمایی شد.
معتبرترین سایت ایرانی
🤩
🤩
🤩
🤩
بونوس‌اضافه‌به‌ازای اولین واریز
💰
🔴
فرصت تکرارنشدنی به مناسبت افتتاحیه
🔴
⚡️
هر چقدر شارژ کنی، بیشتر هدیه می‌گیری
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
و هزاران امکانات خاص دیگه
💰
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا er19
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/23037" target="_blank">📅 12:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23036">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M43gtN222JpIanS2WYvTfdFpKaH2Qfnb094ZReo3HaRzNiKkboo1kcqn8OciXCg3yUdxWJdge20OrEwTzR7JloGKYvUl7Oi0JrAybae9btGhDjQd_TlTEhzKh0UwHIKgUPZ7IlGjrGjr4c75llOQbznaCqf3CTjkAoGxk72jNG6RDdvtO66QqcAqQYinZzybrEUYvZ_WD2I3F8s-Cjc5fwPyjtD31AJXf7gP7QxGlRtJ0kYBkOVYokO9mkhZWYyFyiLkL9RNQEn7TChIiOV--trHIyaggYyJCwB_HxlXE4DnycjcOCtNxOov-PSpKj6t6GD_6DXwvaGaCMcLDAHh2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ پنج مکمل‌ ضروری و مهم برای رفقایی که بدنسازی کارمیکنند. هرچند با این شرایط اسفناک اقتصادی مملکت خریدشون شاید سخت باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/23036" target="_blank">📅 10:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23035">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3RhCZ9anrdLFf2QfGWe7b8PVRe2TfBA0iajAPjBJMyxNb8Q8xBAS2VglrY_fWAIYyzawB93o_CrI3v6R77k_-0c-ZutdKECHcx9nizigLzlQ2QJ_-rxbOe09TqCSGPJA4GpTVR1mXQKj3ECqb2hLl2aFGe6IrvE-I3H5RP6y_38UeYC0vnFB-9tA_a7YlhSloJIGBApeRc4hucXuj_6DAogg_BjevkBG0ewGtZxHl7uAQagtIEpSOe-DHMUxIaVcri9CJ0t9zeSd7o0UBfS6R6mVr10tsJ1tWH_0Ffe4XzaYiZYlzIYrDufpmQuhDBh14UtawRKC3GLARurPaFisw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
سوپرگل استثنایی مایکل اولیسه ستاره فرانسوی مدنظر رئال مادرید دربازی دوستانه امشب فرانسه ایرلند پیش از شروع رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/23035" target="_blank">📅 09:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23034">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCaXGm5RyyCJFbozdJzf6XSutEqafz7ppi7FdWipmRZhhD3LLsSUbbhNaaPo5d006GrZB_8B3-ytGVqne4RqxzA3Ahq9l2IF_aMI2MTEujgQ_M4j8dbTpVs3pRFECOIESwBLcFsvs6iplRcND884S692Hag55rXuYXwlTLyOY3Lbx63Drq3p1QmLoUdcfuRNFUHhRi9bjTmjulzoNSMA_5UelRULfX0gLebYXxQHvPg8B1ioaJ0S1Kos7egWYEc4HU2ZKpzKbRocvpE3HlLJhbwjoqgPYrg2Wb71gsIIl9l5Nih4OrZjrQ9E5ibv-rVHkCwEo4BWfwQEoOLBMd5tWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات
|دیمارتزیو:
فرانک کسیه پیشنهاد تمدید قرارداد 12 میلیون‌ یورویی الاهلی رو رد کرده و میخوادبه‌رقابت‌های‌سری‌آ ایتالیا برگرده‌. یوونتوس علاقمند به عقد قراردادی سه ساله با این بازیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/23034" target="_blank">📅 09:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23033">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j16g0JHaoOcYGUS5ejxQOtefppzEGSTnXQqHWfmZEdVEitKzM389Bm4py03I0_F7OHXtr7eTqNdF6M2bMS2rB4wYPfH1-bke_MVVx3YKj7AhvLGVRJuBqVq7RWWiJHo3lYGRVo9aAbx3dlK_b6mBAsLyAlnzAbJJvesFpnXRwz6XAaWSkRVnwWMpfyEgIDlQgHk4-LlaMmPxYNTdJG8J13XpaXu4dphr4e76w6yPh0KOmO48culHhCarxX3w4xkBXMrA0ksxIWC3t5xiP4jH7bSBNzWTqv50t3Qlgvt3kIRs7Z6a5w34gsPnzImleBgJpHZyoV-49vo39uVt614rLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛برخی‌دیگه‌ازشبکه‌‌های‌ماهواره‌‌ای‌که‌بازی های جام جهانی رو به بهترین شکل پوشش میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/23033" target="_blank">📅 09:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23032">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9BKKOWpPrn0xAlsesRggXa368rH6NB0TYvs-xbbBtuskhCQQ320xD143xHSPLhb_l7khi--qLKQiQolgX4vA50CfuoZQ4-gVFZe3aBMh9ZSUocqJhb_8N2ZdcnrgY-RQp-e56j216roi5zCOoo2UdCxYILu94BMgFVw2VUy3tfFB6FjM1cy2bp1VYXVeSlCLfOuEr4UwblwiCp5iyFZom4MI2PEQ3jOrawdhsjQ0q0LXqZzh3Hvo7Aiu1HAXuP2KhFxNL2HxQnmyDeIolWzi74x6nOABjfr0GJFhhXGNsaWqgWO4HRLJw8ok9eE9_mVUXBYlEPuswR2WDaEIT0p2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان خطاب به نماینده محمد امین حزباوی: هر باشگاهی او رو میخواهد 70 میلیارد تومان واریز کند تا رضایت نامه صادر کنیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23032" target="_blank">📅 01:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23031">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8torLvQiBYaqHZl_jscxmntEGCy1ZQo9aEZzY7xgEnl5YHJMWanMlFwCAAI1UJwFgxtZJXQ3o8FNH_xw2dgk96R6iHXYrQvHBaFijywN0A7cfwFHNQLC830FJanb9xAxckhiXtuC4h8bYf6UBlw29LKDqNfqyACzC-7UBLk934nOwUpvo168oRe6Muxj8UOWMslaRVgx2SP8bL0cPHA5ElrwPBGqVjBXu87PLcXXDpzrOxDvrtFr5RbB6zNzS0pZr6baXHdyl0VAKORE17KD7CZOTdp4raGaay6IlWonSGY59KFJs8vQ9-hspl7V19y88swlKzzzd-pcHNMZCHT5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه ‌‌‌دیدارهای ‌‌‌امروز؛
نبرد تدارکاتی ماتادورها مقابل تیم ملی پرو در صبح امروز در فاصله تنها 48 ساعت تا شروع بزرگ ترین تورنمت تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/23031" target="_blank">📅 01:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23030">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_sEoDag8A7Srtv4-x_Zupv-hN0AWk1OiNpIp5FUZSMvbmpYzJCChRZY2dIsdfw1T9g6ehXyi-iJMLDuBjjeOtNkJzTGSVYKkOT_LKlEUm5S1ReDIRkwv8rti39Ta8N29nSIczH8LGWztRhoKdh8ZBUEMCYDrMrQgKkiUkpEk4Nyn7p1_0naIhQhfbX7WwY-2V1WSS9_RNlqcxAktJUXqJzWxJyVxQiMsk5jHpN91zZcb1s3AoIKBizltrAzh6j8XWvNEBnj504dmyrSyiV8m3W1CE8VZRjqFFwDgdqw4oRgmBf1p74PE38ah7cdgFDRY-BDcTANofr3jr-dAAuoqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌دیروز؛
ازبردسخت‌هلندی‌ها مقابل ازبکستان تا برتری خروس‌ها در شب هتریک اولیسه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/23030" target="_blank">📅 01:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23029">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb89dc70af.mp4?token=KMZTRbMbN9JpUT-mrybGjjQtoL6wqI1iZwND5fgqFLx-R7Hw7IC619dj9x0Zf8_7JlxInOfLHsaNsDFkcL8IGk5LAcWyeAD0qD0EvxjBiwEm8PDgrLMw7icdXbPk5ne4i4R2BJ_DFiM7PCoXXfMUxGsQpoQ7y3qRHa30OvnQuPPRg5kbi4r1kJHDo9m46eo_hoXRB5SamKGXQTxkbaUNCsBY76SMtq7twwsyVHN1Iu0fIMeK7ggHLGLDTOC7ErjLEPX0nMP_tBGDEFosM6sPrnxh4zS8B-uqvCBFsI-95BvAwbWTHmpVPFwXIJRQJktGRt6L2PvwmpcmyR-PLfS87g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb89dc70af.mp4?token=KMZTRbMbN9JpUT-mrybGjjQtoL6wqI1iZwND5fgqFLx-R7Hw7IC619dj9x0Zf8_7JlxInOfLHsaNsDFkcL8IGk5LAcWyeAD0qD0EvxjBiwEm8PDgrLMw7icdXbPk5ne4i4R2BJ_DFiM7PCoXXfMUxGsQpoQ7y3qRHa30OvnQuPPRg5kbi4r1kJHDo9m46eo_hoXRB5SamKGXQTxkbaUNCsBY76SMtq7twwsyVHN1Iu0fIMeK7ggHLGLDTOC7ErjLEPX0nMP_tBGDEFosM6sPrnxh4zS8B-uqvCBFsI-95BvAwbWTHmpVPFwXIJRQJktGRt6L2PvwmpcmyR-PLfS87g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
سوپرگل استثنایی مایکل اولیسه ستاره فرانسوی مدنظر رئال مادرید دربازی دوستانه امشب فرانسه ایرلند پیش از شروع رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/23029" target="_blank">📅 00:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23028">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtvR_6xuUZhJ-e_koPDkzaZIg0vlO73DjWsOPLJeT5MEyiDjVC8wGjfaiVvlUZfkdnT8-_9-8mGjOSQDhYOf8XN2PxnzKTElqkc2M3XzZnoMz209EVgjGavkuAv20jFGgsLP46xH8fLfKDmykKDNG0uQCsHahl7yCnbGnrkVeagZmRuuTHVhigSc4Rr-OxX5EKGgtqo1vhCUHxoSVZrlXGdzmAhhveYUxNiZuFLGDbooDk2PmCGyFDuXmC6MC8zPFfVjBxeAxqx-2iWpaVU5wxuUJwSRL_TEkI2_MEfBBKicvz9i4w0griEMx-XyuREi-hPPzrNV941oaXlVS8BYZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
🇵🇹
برناردو سیلوا:
فکر می‌کنم قهرمانی در جام‌جهانی‌پایان‌بی‌نظیری‌ برای دوران حرفه‌ای کریس رونالدو خواهد بود؛ رونالدو همیشه‌سخت‌‌کوش‌‌ترین بازیکنیه که می‌شناسم و لیاقت بردن آن را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/23028" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23027">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91f877f10f.mp4?token=X8hJYnzePk4xaM8jHdZKzjvCJk_FvLOOVungrXR5MhB9nu_Y1AipTMBo7SO6iDSHyfst7YuoUq2p2DoQiQJurdmVpjLeHTWEmVrVa78tyiVIa1YgnXXOFHzuM8CIPeHCKFIwQHw8eqWHiLf5lTsxWcJTuMnucDSjvu89hLYIB1k-eR2_rECYDe_1paq16dvLBHmuTpZ7EoUfLIBDCd1ZNgvTPpAI0HQIbohzVUCc0eD7RTsvhDLQBGHXRmSuh4mI-kusCwXS6w4tECAVT2QXgt2QR_6XlDnKjLejsIry6aJTgG5jONKm_W4qXUbUHfnJ_4ZrWsQJNDI8_FGVQS_jnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91f877f10f.mp4?token=X8hJYnzePk4xaM8jHdZKzjvCJk_FvLOOVungrXR5MhB9nu_Y1AipTMBo7SO6iDSHyfst7YuoUq2p2DoQiQJurdmVpjLeHTWEmVrVa78tyiVIa1YgnXXOFHzuM8CIPeHCKFIwQHw8eqWHiLf5lTsxWcJTuMnucDSjvu89hLYIB1k-eR2_rECYDe_1paq16dvLBHmuTpZ7EoUfLIBDCd1ZNgvTPpAI0HQIbohzVUCc0eD7RTsvhDLQBGHXRmSuh4mI-kusCwXS6w4tECAVT2QXgt2QR_6XlDnKjLejsIry6aJTgG5jONKm_W4qXUbUHfnJ_4ZrWsQJNDI8_FGVQS_jnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
باتاییدرامون‌آلوارز؛
مورینیو سرمربی فصل جدید رئال‌ مادرید برای کنترل‌کامل رختکن تیم رئال، پپه رو بعنوان دستیار خودش انتخاب کرده تا بتونه حواشی بازیکن های داخل رختکن رو کنترل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/23027" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23025">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61689d1d82.mp4?token=lJ__Ac87F3B9yXCcq5bl_hOm5tlczZA9ab0hex773P4jvYDxtXYNSXDRAYd5XYf22b28UtdbBmoRFY6fqHSV_kbqlUsOwgZFE8PM8qY7J6L4BBLkwzkeeO7417RVyYxHc0KHH-QAMRMI_b3PxCZcWgcjgunmGgoGDcJAuGlSqlZGiqZmqWNZlp-ZVSpiojypwJw4OC5ylaElTCXF0Y3ggK8WZHmHDsdBhDXMvbE3T98NqzFOsmTcW1nTcZhKMcgvcwbQG2sf-n4mX3ylyDqnfU5_j-qEvTy7YCKQo7HCcNNBEBxA4oByqDyeThOQVXOY0cOsqhKGx102hqN3O23-yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61689d1d82.mp4?token=lJ__Ac87F3B9yXCcq5bl_hOm5tlczZA9ab0hex773P4jvYDxtXYNSXDRAYd5XYf22b28UtdbBmoRFY6fqHSV_kbqlUsOwgZFE8PM8qY7J6L4BBLkwzkeeO7417RVyYxHc0KHH-QAMRMI_b3PxCZcWgcjgunmGgoGDcJAuGlSqlZGiqZmqWNZlp-ZVSpiojypwJw4OC5ylaElTCXF0Y3ggK8WZHmHDsdBhDXMvbE3T98NqzFOsmTcW1nTcZhKMcgvcwbQG2sf-n4mX3ylyDqnfU5_j-qEvTy7YCKQo7HCcNNBEBxA4oByqDyeThOQVXOY0cOsqhKGx102hqN3O23-yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
خوزه فلیکس: فلورنتینو پرز در کنار اینکه 150 میلیون یورو برای جذب مایکل اولیسه کنار گداشته؛ 150 میلیون یورو برای جذب یک فوق ستاره دیگهه کنار گذاشته. پرز میخواد این پنجره دو فوق ستاره به‌ارزش 300 میلیون یورو برای مورینیو بخره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/23025" target="_blank">📅 00:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23024">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05fac563f1.mp4?token=Ha-ANJEzsPqUnyH8xRDjXq41zqJxGxt6zQYh8dFLtKmcmJXcxJnEcrXu5JVlVpi6nz2Y_dx5cxNIG4yk2cCrisyWZ4JkhIYfa_duePkp10hI_yN0BT2k8uT49_j0ANtXoT6aJZZLutyvMGe0ehSBSflDa3RFi6_00eFMjMYHcgw6ATf_ugGok3B2vcJuGzZFg1DhIcJKyN8Ut_kHM_y8-B5bMpyL2zHkEOSG7ljfFkyfeM0ocd9jolUs8DmT6WN-gp_1X5NLRa5Ep-HRXdD4k7W8v1RgKSQarGmUyuEG6XNjatNu9B0R5W0dt5qD3mO69F_iqUUShQKSgq-YBE59FlYF4zZdijW-MbAnv_a76BCaOkxixhOPnVxtwVnKHwYLPBPohQjGgcRPyCO1JxTiPNaZCSdxsme9ID3rz8DE0r7bNYuskZshbd7gFmUdasQMhCnCgq4-AnlAbAoJ2EjRo-WYa-Ez3YOVtCEpZvfLbuthvnnXJMEVFXAYyUlBH9d5B36-9J14jN0JpiItbkgGFDGf-YFL6cV4BkfejtdnAAb_cFXicyuVLHNS0jBNaBx3JPEZtfp4yj9bP1d5d_c1rvQvi-cCIRmnMZl2byzPMLH1h38NbT2YbfbMa5RJlJR4Kl9U9nvFNP90tqcVqHEadfwwEwl_B14N-bzmbzR5hA0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05fac563f1.mp4?token=Ha-ANJEzsPqUnyH8xRDjXq41zqJxGxt6zQYh8dFLtKmcmJXcxJnEcrXu5JVlVpi6nz2Y_dx5cxNIG4yk2cCrisyWZ4JkhIYfa_duePkp10hI_yN0BT2k8uT49_j0ANtXoT6aJZZLutyvMGe0ehSBSflDa3RFi6_00eFMjMYHcgw6ATf_ugGok3B2vcJuGzZFg1DhIcJKyN8Ut_kHM_y8-B5bMpyL2zHkEOSG7ljfFkyfeM0ocd9jolUs8DmT6WN-gp_1X5NLRa5Ep-HRXdD4k7W8v1RgKSQarGmUyuEG6XNjatNu9B0R5W0dt5qD3mO69F_iqUUShQKSgq-YBE59FlYF4zZdijW-MbAnv_a76BCaOkxixhOPnVxtwVnKHwYLPBPohQjGgcRPyCO1JxTiPNaZCSdxsme9ID3rz8DE0r7bNYuskZshbd7gFmUdasQMhCnCgq4-AnlAbAoJ2EjRo-WYa-Ez3YOVtCEpZvfLbuthvnnXJMEVFXAYyUlBH9d5B36-9J14jN0JpiItbkgGFDGf-YFL6cV4BkfejtdnAAb_cFXicyuVLHNS0jBNaBx3JPEZtfp4yj9bP1d5d_c1rvQvi-cCIRmnMZl2byzPMLH1h38NbT2YbfbMa5RJlJR4Kl9U9nvFNP90tqcVqHEadfwwEwl_B14N-bzmbzR5hA0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیوخفن‌ببینید اززوج‌های‌مخوف‌حاضر در جام جهانی؛ مراحل‌حذفی‌قراره‌بازی‌های‌جذابی رو ببینیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/23024" target="_blank">📅 00:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23023">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7x35l6y5pb0X2_VWxkRrS4PLf1cj3T3NUx-f_DbQdYR_0V_9CTTC5AfFlP7srTCCm66AqK6TMlAHG8xVU6yyWtlPJd6jfFByKCkAIha2rIS4v2Ne2-_KqWtQ7_fJBBZeGeDqWh38SJ6AjbODc0uxvPvHBU8V4VTh2tHZ8CAn-TnLK25hrMiE7mndThessg7MK1Nr5QcVM-oheJMaqAmZ9ZMQ2AnvyQ_ZzljpbM4YZ_s9OGeWKieZea-MU9LpEmFWdBeG34oPQNKuNdFDKBKxHsBvmz1CwdacUE5UQdxlm4QZwq7bMKQ0MZPGqj8hvI9WwYRePoiAjWhkMEZm2uKgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جام‌جهانی‌فوتبال‌قراره از 21 خرداد شروع بشه. لیگ‌ملت‌های‌والیبال هم از 22 خرداد شروع خواهد شد؛ برنامه‌دیدارهای‌هفته‌اول لیگ ملت‌های والیبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23023" target="_blank">📅 22:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23022">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9su5uUHDZv13ifItH1MDNVxbIL_cyTcbJeIlOkLKhembWD_c0KG3ip0A-EE2Ddp2XUfAPoxj3vPXdU6HleHZXQsqaQEquL-NmYJQj_CYul2R_CCpqZZ9egRjo4jdCbJUVyx0ePYHitVIZtruhz0hvgI1WCKIwNOGGCKQ9rhnkrVENGZRbGoC6qJmwxd334shEssEyPWepPntnbxwEqvh4SPFzDlpZ8lLFt0MfHMode3veECCEmX1mqZcpdp-PdZMIZ6vA4TA6S-VDsupv1Wb3B3O8_PG_3XTn7Wj_PovkjBcul-77EfID_3UxXWAEImEZ7GjkRcBWibHWHmvL9TWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23022" target="_blank">📅 22:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23021">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eI6dAyJ9M5RdZkvu6C5YI30L1Auv-9-ljqz_BDCa718dqgTxb3bpdfUoOhsAwrEQPDeMAURwnXhh4aRzgdFW-V9dtnM1fEOTsj1XXXbiJ7XFWOhLMJUrfsUKaGvm4BVkVlGuODUH7JYdMiAwBHodTcOtQgHYKZ7Yb-8v-ROJ0q3PvIe916pNUlL9F1vnXrxqEQQt47w1vonc0p1wBpd0ma99q5lRR1yA4koyUFScMpBNhcn9_iC_8ivOGqI9mC2aA7_An4msxJNv6EELI_18RDV8sWEOKhddZKtYo1e0BIbIjgV01nbMaMXA0pGzndJRpD9C6_qogCatjnAaAMw-qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رودریگو لاسمار، پزشک تیم ملی برزیل، نیمار جونیور از مصدومیت درجه۲ساق پا رنج می‌برد و ۲ الی ۳ هفته از میادین دورخواهد بود. به این ترتیب، نیمار دو دیداردوستانه‌مقابل پاناما و مصر و احتمالا اولین دیدار سلسائو بامراکش را ازدست خواهد داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23021" target="_blank">📅 22:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23020">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f3b11f90.mp4?token=My_O1A98D8LJ0ezyM2yD4fgc9PL4SKLsKbbnkCaw6sfq5wgpBI3jTAjKM_P2qE_jA-Qjcu-GgDpQ7BrCdG9i-t0q6lsLfPYXEbdIKyz83FS0sLZVBol3gFPzr3hQVdmQi-scG0ItdlRue9dbQ0IaRM_E8IVMMzldydNg2vAdeyZzLkvS1iPfntVFJRcJBCsVyUjEtPpziLSHQ0nTnCxC7wgbPl_lMZcvfyeKwQ_i5QJzsZRcQSUiEGuvTKTzgUosR7Sodwff2N3o8ZcWQDHqDAuP9msmFX_iwJptRmOvubZlOl7KzlbaEyWwE66sirV99nMowAUtUAmTZgiQcHaBQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f3b11f90.mp4?token=My_O1A98D8LJ0ezyM2yD4fgc9PL4SKLsKbbnkCaw6sfq5wgpBI3jTAjKM_P2qE_jA-Qjcu-GgDpQ7BrCdG9i-t0q6lsLfPYXEbdIKyz83FS0sLZVBol3gFPzr3hQVdmQi-scG0ItdlRue9dbQ0IaRM_E8IVMMzldydNg2vAdeyZzLkvS1iPfntVFJRcJBCsVyUjEtPpziLSHQ0nTnCxC7wgbPl_lMZcvfyeKwQ_i5QJzsZRcQSUiEGuvTKTzgUosR7Sodwff2N3o8ZcWQDHqDAuP9msmFX_iwJptRmOvubZlOl7KzlbaEyWwE66sirV99nMowAUtUAmTZgiQcHaBQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تایید خبر اختصاصی‌پرشیانا توسط علی تاجرنیا رئیس هیات مدیره استقلال: وکلای ما خبرهای بسیار خوبی درخصوص‌پنجره‌باشگاه به ما دادند و تا هفته آینده پنجره نقل و انتقالاتی باشگاه باز خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23020" target="_blank">📅 22:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23019">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CoOk__lUQxzF-um1A9asGb1MxMX9ZaLYYwi1BF3LHS8dy9SQFoMZ4xAoISnnAKgUqHFHx2MLDKMmYw6HuwAXprR9p5W3Rl1tvJ-Fv8GTpe55_xlSLW_Kz7B7PwcOHd4DiDLj1tX0dg8Imv-bIT3cWI8L6aJ-x2qeEhn6wRG242j4KTDkXUH62XZsZ1tPUfYWZmvGcWIuc_1yrtvajLeOTQeeFyWC7AvioyP0KXWLmEUcLFFGfUI-ApGNLo7UARu-BG6q4aiy_N9QZxW_siLvTJUAZWlHhPZP2av9_O5PNSbkoDD9QeRePFI0t3SJZOWKavDdGRcOp-B6SfiI8Kzyxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛نشریه‌مارکا: فلورنتینو پرز عزمش رو برای جذب خولیان آلوارز در همین تابستون جزم کرده و میخواد بزودی 150 میلیون یورو به حساب باشگاه‌اتلتیکومادرید پرداخت کنه و این فوق ستاره آرژانتینی رو از چنگ فلیک و آبی اناری‌ها در بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23019" target="_blank">📅 22:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23018">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvWc0HnfG2oGFKYiaYJGXYkn0jtbkR1ZgF00WiCJcdiOxNy-MGNCjMRThvgG8Dlz4vU7xYyaWCUfvgQ0IiMdvaAP6FlfKsbfoEJvlSr49MzBXO4dpikKn-nxtIHpIaBkyNiG7CRv4qp9SSpYYzGeuXNBHKNJn1dIOd8i-Z5QY9jrrhVR7z-DiCwVq3AFJ9v3LYYWp3aoyAJPpCNIahegAUBUMSQhWQj2-TxH55KrL0uyLZjTAHIHN4R0WWZhWrp2k08yn1kf8JMouiyfoDSeQl9HJa2xzN42CpBOQB7dDZMKQyHw9NzTYDg6xFRz-5wyjUGQD48dn6PZKKP2fuNpJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
علیرضا فغانی اسطوره‌داوری ایران در اعتراض به کشتار بیش از ۵۰ هزار نفر توسط نیروی سرکوب جمهوری اسلامی در جریان انقلاب ملی ایرانیان، با بازنشر یک‌ویدیونوشت: «برای بقای کثیف خودتون، جون عزیزانمونو بلعیدید. قرار ما با شما؛ نه دادگاه، نه‌بخشش. رقص و پایکوبی روی…</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23018" target="_blank">📅 21:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23017">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2huXpSMcXWKFDAAzzYxHQ58XrtJRGCTwwPlZnTq4wIlmaN82YeSBUApT0Z8CFqEqQlSSPeoC2TN6neS2Dtoni4Z6Cipjm_HxdnSHGsr0v4qudEwpA35MJ_64KL-jaDyKXzBzL332qGz4EHW-tGVL3EHKPsv4MklDPUos7rT90rwJUbzHHIV1lDBsFvGfGo7NLNf8oEEhNI2reNoYSlQ94BOBNZP2U5XB58c8ZNeAtaSMyqJBzGUUaWXVwF5D7P-1Hz3LUAiRVscO122_FtlfmB5J1ZZ8vwbVd4urKMp2xN0_djcINopcnmUdtVH5RfIAcdqx1JUmClZV9bgUUY2Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇦🇷
جدول رکورداران کسب بیشترین تعداد جام دربین‌بازیکنان؛ لیونل‌مسی بااختلاف درصدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23017" target="_blank">📅 21:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23016">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Icg5iHs-Bt91nXWzbCzbgfCIIgt6Y0fID3paa5J2UGA9oU7fDio_IPudUSJ1s9aRALB97TE6PYPy2mZzncRbfrZFqfvDE1ndlK0R14H6BsHeIN2xVLPzwJRvoPahr6tjKJC4mT1RcIuGByJrz6xirPxMfn276cRYWhuI1XoXnhfExldTDy2CD6gbZUF7vMdmoSDLpyLdaPb9QxWpfKdoN7bCcWZi-PXL2PNKMkvboUGtQ7O4oPSZC_YeqZn-QPiDv_fcNBMo5n-Q9QfFCQRcXXLbIiIpjEF8OMJr_wf6IHZ_rwALxQ-NIdpmp4kkJe8r8EiEE_0s4Aw2zh3p66q8mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23016" target="_blank">📅 21:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23015">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaJQHMYTuGdH_S9a_ljN3jFkygTHOlCMENvw_6lTmwn_H_MBI07Mm1hxqr3e691ncGi4Npmog2_X7WFAIm9KZfRMejKcSINYtJPx-tL1FdbjSzEfp3blljH_xe0S-3k-ZWro2_mmAqCnwJk-pEaotyhXidyjeSKDAlGsjdhy890VcnBG1jQSrqBNLXBbBW_Xy0DKQnyiUQIZxYO-lSZ9PUMX2ipxop6xCiJv6iAscRwgKx8Ais8lJBsczHVfbCcWT3eZ0u9_1PG-Dp6RMIdrtpnxwRoeIYVUyv4ZfYZa7w03ZuuFUhkkI7VNoWcXgzE1z4YNPczoUH95mJDkUOkBMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ اینکه خبرمیزنن پنجره نقل و انتقالاتی باشگاه استقلال بازشد زمانی صحت داره که درسایت استعلام فیفازمانیکه‌نام باشگاه استقلال رو سرچ کنی بالا نیاره. شماهمین‌الان هم نام باشگاه استقلال دو در سایت استعلام پنجره فیفا سرچ کنید بالا میاره چون هنوز بسته است…</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/23015" target="_blank">📅 20:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23014">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60571c2f92.mp4?token=DppUm95xTTqmLmn5RGd19EbS5_CF3GZ8HAG3g6HZN-QX53SyRlbIdnXJHpc0QvWhkWSGb22l03Pjb2gL4BkeyGIPsWj2m3PYeSikUPJlFxMV14An0WKahzjcGVrEzQ3DrU-n1HJ-8KmdH-h9E4-6YH1EuXnKrkEMoYnxrfrASLDF28lBNo6JPHVz1xuV66lFUDK8ZaN6habY13qnWpe6FC-TKQd_pXkwvFd0n6iPkXDrkh1JNw4Jw_FPftVMVtoZFzxBzljUCCWAObG4g_qguKnYHlwKfcGIv7TS_3Z26rAvG2OKC4sS-mO8deU_Los_op3oL3LMf2gbvgQR2b86Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60571c2f92.mp4?token=DppUm95xTTqmLmn5RGd19EbS5_CF3GZ8HAG3g6HZN-QX53SyRlbIdnXJHpc0QvWhkWSGb22l03Pjb2gL4BkeyGIPsWj2m3PYeSikUPJlFxMV14An0WKahzjcGVrEzQ3DrU-n1HJ-8KmdH-h9E4-6YH1EuXnKrkEMoYnxrfrASLDF28lBNo6JPHVz1xuV66lFUDK8ZaN6habY13qnWpe6FC-TKQd_pXkwvFd0n6iPkXDrkh1JNw4Jw_FPftVMVtoZFzxBzljUCCWAObG4g_qguKnYHlwKfcGIv7TS_3Z26rAvG2OKC4sS-mO8deU_Los_op3oL3LMf2gbvgQR2b86Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ما
مردمی بودیم
عاشق فوتبال، تو فوتبال هیچ دستاوردی نداشتیم ولی باز هم عاشقانه دنبال کننده بودیم و دل‌کنده‌نمیشدیم‌حتی وقتی هربار بعد از یک شکست‌جمله‌کلیشه‌ای "این باخت چیزی از ارزش‌های تیم ما کم نکرد" میشینیدیم. بامردم ایران که در جام‌ جهانی 2018 روسیه بابت خراب کردن اون موقع طلایی مقابل پرتغال اشک ریختن چیکار کردین؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/23014" target="_blank">📅 20:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23013">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GI2jzO_6c5VZgFdSNKiw0SN-ZKtpKSZwApDsv3F4vzLWxwc1HzG3ewPtQ474rJyzgn_okS12CNw5OlFDjkNuL9qF1ByncVOqKMxPDCV0wuXQXPmvoWPYoGyKFaMbk46T03dL1qqPMqIRVxZT0ulWANb4zgXEuXBDveh0uwYZF1_jv11dtvkTya6TUL27a5SwyOvbIx5Z49pS7pbVDtFMzNwyKDa0BSehhJaRR--WWkt8-QUMSB8FZ2AqCEP0QOZtNkljws1In3fFUb-Ig-IVC8Ydv01RkB4VVtw8_b7NzhkXqPGU8Foc6lcQR10FRzJd93q2fvicN4SwTLYWTDMuYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛اسکای‌اسپورت: رئال مادرید امروز شرایط خولیان آلوارز رو از اتلتیکومادرید جویا شد. اتلتیکومادرید اعلام کرده هرباشگاهی 150 میلیون یورو پرداخت‌کنه رضایت‌نامه آلوارز روصادر میکنه.
‼️
فلورنتینو گفته دوتا ستاره 150 میلیون یورویی میخواهدجذب‌کنه.مایکل‌اولیسه…</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23013" target="_blank">📅 20:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23012">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDY62AdFHHmjaLQzYqO-NMRmbtD9aWGo0QweKZZy73Hh9qU1x2b1_c8RjU6lZ3Eo46PCy-8fnVUSGP1IMkadbtyK37-ZclBLwRhiW76gAhmVCnmSStA_OXXObnBXtYR8JBRMPk4yO9-RC36BJDSzfnhiNJUYiLhNLKCJKwXuMhokdlPYAV9ORYuFXJGtnR3DjkTJHJRUhxqAjn3EW6840y38yf6If2pDSouANpus6-J9idWhTKiROgp085iI2wq-KMWZajispOaRzoULI_ibUStZTfL-dKG5mLHeHKt-8pnXTtoXshkei0ysBdXSl2SkYQg2MR92ir4piDP543Af4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23012" target="_blank">📅 20:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23011">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29259cd165.mp4?token=bVoT18kU10gmC-Rfp9CMIJYqysj2pDix-ws9vRQos3PIyfr8tDMt4rQ0q4OH_ikQIIISscqqSBVDXmSuCNXpU-KWhNLhd1cPNsUdZf9AmtspcDtSzCudWrWpPIYKzDMaBjGPFmYqFsOFdv52CBig_wZM66ZV6MKbD0S2JcItSOS0q3sqKuRkfDsCwQLG5_mWBPAmpZs36xfiS6KFgL3LryJqsvHxBPz7oWbv9A1C1DyppC4jURYiKXFp8aEoXBoKRq_yGFh4t1ZWfG2rxZVvcUQd7qOdrSZ0JgP5DsqnegpA_hFld-Eete3u3asqrz_83zgSesk3YN2vppvrQcYygrsSG2rzxfPmSvWC2Z1Zv00OErO9IUFUs5WfBHILYoqZBrKRxFA3tw8tDkyKa9hvH2dqWzQeYOS8aaTfLj8nrTRmo7emNAjcgDeB5BKjFHWHAZ0GxJ7lHoCsGpNIWvAyGLiYCCq5jHtTvPD1i9xxB70GoBB0ItgNcOJM-vssPrHPC1rCIbARoz3z8Y5LLzcgwj183gIORm_yqbsETy-5BtdnLg1wp2Bq2nSk-PSG6w53_9XzoW5BsI916Ifu0uZxW2Sqpda9OnnA6pXzdpPv0wL6jC_7kbwK_c3GuwsIn3VMeTesALibAi5YOuq-_yvaYqNO25w9IGCUK5fZxqcQX9s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29259cd165.mp4?token=bVoT18kU10gmC-Rfp9CMIJYqysj2pDix-ws9vRQos3PIyfr8tDMt4rQ0q4OH_ikQIIISscqqSBVDXmSuCNXpU-KWhNLhd1cPNsUdZf9AmtspcDtSzCudWrWpPIYKzDMaBjGPFmYqFsOFdv52CBig_wZM66ZV6MKbD0S2JcItSOS0q3sqKuRkfDsCwQLG5_mWBPAmpZs36xfiS6KFgL3LryJqsvHxBPz7oWbv9A1C1DyppC4jURYiKXFp8aEoXBoKRq_yGFh4t1ZWfG2rxZVvcUQd7qOdrSZ0JgP5DsqnegpA_hFld-Eete3u3asqrz_83zgSesk3YN2vppvrQcYygrsSG2rzxfPmSvWC2Z1Zv00OErO9IUFUs5WfBHILYoqZBrKRxFA3tw8tDkyKa9hvH2dqWzQeYOS8aaTfLj8nrTRmo7emNAjcgDeB5BKjFHWHAZ0GxJ7lHoCsGpNIWvAyGLiYCCq5jHtTvPD1i9xxB70GoBB0ItgNcOJM-vssPrHPC1rCIbARoz3z8Y5LLzcgwj183gIORm_yqbsETy-5BtdnLg1wp2Bq2nSk-PSG6w53_9XzoW5BsI916Ifu0uZxW2Sqpda9OnnA6pXzdpPv0wL6jC_7kbwK_c3GuwsIn3VMeTesALibAi5YOuq-_yvaYqNO25w9IGCUK5fZxqcQX9s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
یادی ‌کنیم از مصاحبه تاریخی مورینیو بمناسبت بازگشت دوباره به‌یکی‌از داغ‌ترین نیمکت های جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23011" target="_blank">📅 20:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23010">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Al4wgPfaMTtPrv4CLKHM4v3Snzfja1yRRVQZvCBlMpNV7gtl7yGCAvd8nuyhETlNuaQY7d9uGeJTxBMIF_mgFssxXyXx1anH_VCcQKonSoLM_GR83Q-f59Mz2oJ6GCR2-ycM-qsMYbx4CACeTUO972EAif3JiUa2dEk4RXENDEoQ9abZg-xCRWbO0lCJCYosXDoQbwitpsQoX7D_Vy9tkxCtaqDBLaP-eyK39Ryg0lO4kQh9-M7b12_eV_50NhsnENileJqweQkLnJOjjFuyBTZMN4nTavyNC4iINtnfQdqtitn2cueiffszeOvaXIlDgG9uiQ1La278PBMZS7HFhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ ایجنت محمد جواد حسین نژاد به باشگاه‌استقلال اعلام‌کرده‌مبلغ 1.5 الی 2 میلیون دلار برای رضایت‌نامه حسین‌نژاد کنار بگذارند. خودِ حسین نژاد موافقت خود را با عقد قرار داد سه ساله با آبی پوشان پایتخت در این تابستان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23010" target="_blank">📅 20:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23009">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IghHO_X6bNK_582iH6olu0ehG9QGqbCgNBVzC7lw7pDcRPAe845JWV7kjzguzgf-z8tHtxmj62mhU-lJr33uNILIeWvmMjWVf22HHWiQ_HDlhReLIK7UtfMNy4PraagY4ifuxijH1ciyKoHRt2Xoy9rzwNz0QIa5xe0tvRVMWHNwpQCzbT0xa9D5BcIffTNYl2Khj9WFDRheRbOT9WERFeAOo924_7YNraIhHLAdgnlcfWIK73dMz3vJ2E0ps9zSP2Ehew7KAsQWMWOMN6H20G0479uCQcwSZZ52D6SkrcHFkca2G2HeWxxqCBsuZd_XNXbtVhTsEIxfDB3ur739YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
لیست ورودی و خروجی مدنظر اوسمار ویرا برای فصل اینده رقابت‌ها به دستمون رسیده و بزودی کامل پوشش‌خواهیم‌داد. علت اینکه یه چند روز صبر کردیم این بود که همه دوستان عزیز کانال به اینترنت دسترسی پیداکنند. ویو کانال قبل‌جنگ 65 70 کا بود الان با وجود اینکه نت وصله…</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23009" target="_blank">📅 20:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23008">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bc2809ee8.mp4?token=g1FfT-Y7K1Hl0qWdVEpb5zbqGNudFaoTp0sD_s0vDS0j7C-1gLhtdhKlrB4Fiyuxi1Zy8ONGMH_yDD9WdCCp49UutsW1mfxMvFj7cBTNQAEgiJPJcnwaNEhJPk_lHn4R188je4prX3AJOjAO6AzvQGYKAX7AaM9OuOuj9UnX2_9iS2dmNaS8rplOS15BLwaaHF6C85KjB-W6yQeZe9cUCjw-59qLqhwdmMuOuR0k-BOitJ9g5IKHu3eJzE36M5saXFWVArFU7howOayojUbONnhYxv9E5VzSvIVIyafxJu4JK0HU3fvDs6LQg1J6DqwJw3T0HsjjNjpcW7FmwZKNIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bc2809ee8.mp4?token=g1FfT-Y7K1Hl0qWdVEpb5zbqGNudFaoTp0sD_s0vDS0j7C-1gLhtdhKlrB4Fiyuxi1Zy8ONGMH_yDD9WdCCp49UutsW1mfxMvFj7cBTNQAEgiJPJcnwaNEhJPk_lHn4R188je4prX3AJOjAO6AzvQGYKAX7AaM9OuOuj9UnX2_9iS2dmNaS8rplOS15BLwaaHF6C85KjB-W6yQeZe9cUCjw-59qLqhwdmMuOuR0k-BOitJ9g5IKHu3eJzE36M5saXFWVArFU7howOayojUbONnhYxv9E5VzSvIVIyafxJu4JK0HU3fvDs6LQg1J6DqwJw3T0HsjjNjpcW7FmwZKNIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از کواراتسخلیا و کول پالمر تا میتوما و فرمین لوپز؛ 30 غایب بزرگ جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23008" target="_blank">📅 20:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23006">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Avh0wr9x3h48O4DiEB_BumcHrLL8_wR4-M8arQEWIQfZyMJAI9EH1GAQQy4SM7YpscOgiol3GV14Xu2VIRsl2PqLfkzz6fklQUrwhRA5tOrH7OvY5iTMcRW9juOWfdKn4hBPqYsVBKP7uiNKXEKkOfcFzgY1UtW-dX9G5Cx6v1pQXt4iHJfEjg0gAfDUaKVU2sMj6-1Uj_OmiJt0CIjpEFnwelWOQz9kD3tXLYSGHzEBA32H7I9BrPeQqoXnW-0IBvJ1sncXfW8-D0GbmRvCBI4-L1Sw9xKKFoCDXRSCiXLMtuWfYrDjKnSvdwWpyT1qVp5SxVQDo_EE4lyUJh-lyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
دبل اولیویه ژیرو ستاره39ساله لیل در بازی شب گذشته این‌تیم‌درلوشامپیونه؛ ژیرو در این دیدار نمره 9.0 دریافت کرد و بهترین بازیکن زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23006" target="_blank">📅 18:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23005">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BpzkzKDqO1nBcLZCwprVP4X3mbCzt2QtFPybGp5PeADqZoqw0_QZdhwF7_BQnC9aoKYHZVhsjMqbUQ3Vfjg25DwR0-qVBjN-MaS0T-dHT8_ZuQA3fNQFIwXVva-D-05N-5ZJrZHhhlCTCrizc7-VRihX1a11iaRygsx4MgYbI5mgaqs831IhdBAhxzslljD9ZQjuwOk2_BiuVbCeBdYxp8NlJFU5OeUgidTNlMr4SJwEGHKaysnB__gV-1pIXDoOJG4jbULOTCvdUBbrY9PseLmrurVk3P4743B-u-k3V9I7fubwSCCxuY3ybaBOiBVBEYfv5X1ha4ABlGthaesdtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه رسمی فیفا: دیدار دو تیم ایران
🆚
مصر قطعا دیدارافتخارهمجنسگرایان‌خواهدبود و به هیچ عنوان این رویدادلغونخواهدشد.  دراین دیدار ارزش های همجنسگرایی را به جهان نشان خواهیم داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23005" target="_blank">📅 18:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23004">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11a90d5e78.mp4?token=voYd28R1sn60G5M4noke9EXo4tTYWUV8wv1R3zUm0druCVntw-S6jVozkpcUrnJJc99XgMnHJj3OKQRpSNertQaXZcu2HiNA-6akGg3v5sH4hh9JdvJbM5pw6En4d0AhBKrz_o9BhrymTSRSh-WYqAxK48-Hbiw7e4NWSomeNP8ELqJoIBG9vfVI2hTtgMAC74M0ysOh3YY7G9qcMQnt29IuZPE81RZS87PgRVBC7SuiQGlzDr7JkLLaofQMjFCAy37rN3Z3yAm2nC7Sq_gq3EIYuhNOp4yDNV2kUjs0eRQiuQYPeM3EnMpF2Pe2R_CU1mRt7yQr28TQOl471quG_ppCypY0vL-Wxhp_lT_M815KTFSLUcWVnBRp37yICAfqgsUk2mT0sVFDNQjnW3shDKKcvC84XZEK4U_g3vjgcCBKva-YFO5HOOEiVlChnMtC4uayBayMKSSlOKc535nQYsjp7tMZErkPtspEhvsAhPhJi8KRVPb4D9WssMq2_6QmVEIAPzU7xeSqzwPGQKZ8Sk9CIernbYTksljOpXrputdKsPmZgDTGPqRLrzid9hf-4IvYYs_822_FektG8hTpfgqK5eNjU2JLUjFyEfPaBfR8zdMX69wlwvXIqWnBpsX49nq_7gqHAYpoiE1bYcpgx0ZqmeZL5gP5aHHqWef0iy8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11a90d5e78.mp4?token=voYd28R1sn60G5M4noke9EXo4tTYWUV8wv1R3zUm0druCVntw-S6jVozkpcUrnJJc99XgMnHJj3OKQRpSNertQaXZcu2HiNA-6akGg3v5sH4hh9JdvJbM5pw6En4d0AhBKrz_o9BhrymTSRSh-WYqAxK48-Hbiw7e4NWSomeNP8ELqJoIBG9vfVI2hTtgMAC74M0ysOh3YY7G9qcMQnt29IuZPE81RZS87PgRVBC7SuiQGlzDr7JkLLaofQMjFCAy37rN3Z3yAm2nC7Sq_gq3EIYuhNOp4yDNV2kUjs0eRQiuQYPeM3EnMpF2Pe2R_CU1mRt7yQr28TQOl471quG_ppCypY0vL-Wxhp_lT_M815KTFSLUcWVnBRp37yICAfqgsUk2mT0sVFDNQjnW3shDKKcvC84XZEK4U_g3vjgcCBKva-YFO5HOOEiVlChnMtC4uayBayMKSSlOKc535nQYsjp7tMZErkPtspEhvsAhPhJi8KRVPb4D9WssMq2_6QmVEIAPzU7xeSqzwPGQKZ8Sk9CIernbYTksljOpXrputdKsPmZgDTGPqRLrzid9hf-4IvYYs_822_FektG8hTpfgqK5eNjU2JLUjFyEfPaBfR8zdMX69wlwvXIqWnBpsX49nq_7gqHAYpoiE1bYcpgx0ZqmeZL5gP5aHHqWef0iy8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیووک اوریگی مهاجم31ساله سابق لیورپول ساعتی‌قبل‌خیلی‌زود از دنیای‌فوتبال خداحافظی کرد. اوریگی با اون گل تاریخی‌اش به بارسا راه قهرمانی لیورپولِ مدل یورگن کلوپ در UCL رو هموار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23004" target="_blank">📅 18:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23003">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1416a6883e.mp4?token=epaFUaxkcYZA7HUbQM2iN3hWjsG3ljhv7CSYq5k0KyT-l8I66ryMx_44eeGk9UtUyQXSYlUlH-QC6LzvyPsdVYNaVJxUsE6K1sbOC0n3i3_BQwp-seNRsHmdL-LCEUljk3YxRC7VFh3w3mH5ohLmnfC3fUPtn1ZFsR1BKZWbYNL7dGT4Tf-HDb9Fwmp9GI0JO8aEGObSbt4UYINR_lEk-VAl4a19gLNqSKPIgqJa1GBH8pFqLp9oPbgXXWp_cbJ74TZWn8PwhzD3h4TtBvALzl2Zoo0WXIDaSjsB4MYHJIgQmcp4q_IMnIl3XQLEEtn50qCxOZKr2hnOV9kNo9nNiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1416a6883e.mp4?token=epaFUaxkcYZA7HUbQM2iN3hWjsG3ljhv7CSYq5k0KyT-l8I66ryMx_44eeGk9UtUyQXSYlUlH-QC6LzvyPsdVYNaVJxUsE6K1sbOC0n3i3_BQwp-seNRsHmdL-LCEUljk3YxRC7VFh3w3mH5ohLmnfC3fUPtn1ZFsR1BKZWbYNL7dGT4Tf-HDb9Fwmp9GI0JO8aEGObSbt4UYINR_lEk-VAl4a19gLNqSKPIgqJa1GBH8pFqLp9oPbgXXWp_cbJ74TZWn8PwhzD3h4TtBvALzl2Zoo0WXIDaSjsB4MYHJIgQmcp4q_IMnIl3XQLEEtn50qCxOZKr2hnOV9kNo9nNiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
رحمان عموزاد شب گذشته در حالی که مسابقه اش‌رو 8 بر 0 از حریف‌بلعارستانی‌خود عقب بود در نهایت با یک کامبک تاریخی 17 بر 10 پیروز شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23003" target="_blank">📅 17:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23002">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OasSSZ-AAqXn1WXZP6n4O7XmCjwGjWhipehN5Kjx3OmFu-VDzfSVfnISJ05FwlbPnXTrOsUAJkeq5SmlPVmaQE7Z6fH2c3rRwxR7gXyAO92tOqqhPegUxe8bSno3CNTI3VNuiy4azM4ZxIGjNowsHgDjp7FQEMkWnxeXRf-MZElCD6fMuCkeV63sI4vhqdFzhcu38p0AyKp0amBOm8JzuWaX3uOfIedgQHhhVJknY1qmTpyo3TA1q_6Kf_moupd4k7_DKGV-nBl2KdILwh4tLEhS5AbdYEN_zp35ojmQ4hvqstVtbzHsj_Sg8IEps4xoTqg0Ylq9p3g2bepNAW8TdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
پُردرامدترین بازیکنان حاضر در جام جهانی 2026؛
کریس رونالدو با اختلاف در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23002" target="_blank">📅 17:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23001">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-zBfuYuGAJ0kOtetTvl6MXYJXxJUkt0K_TxkU34jqStpUZZ2QWfyEVkMgs6yAjtIsGOyAq4kYrRXR8QAOUVV7YGCKtuWMtLreud05URI3pyVKnQQM_QpX5dMtHxSMR3wESSN45hsLd3CSh9ml1y8_Ig0m5qGOVX1eSo7DPFMly49EmfKO6Rks9fNX31kyrRrPAiCkDX2tjeUxhg34o1uW2YNyXrOWJ1MvJHoRDRZiwvyW-ecN7k7WGJoEG_qqn_pY-RSDPNzSq3-YIf5sncEw-LRyKCY5DbyoEUxDyF2bzpC9d6TlhzDd2NfyrrDkvMRMTbqSwoI7qViH8v67P5KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌پرسپولیس‌بزودی‌باانتشار بیانیه‌ای جدایی مجتبی فخریان و یاسین سلمانی رو اعلام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23001" target="_blank">📅 17:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23000">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FmuPKj9ycJkE0jFqvsXX0TTuCZAlpofV2bQ20GQlzwC4r8zgj7spTWhvIigdbOIFpilo3lhIgv-r1oUDWJkueVE9Udo0hC6lrNyDWrhwSv4zF-lbvnMjYUIv3pxQaPO-H2UC1lfNErr9_p9O8eJLBpOFDD6f63lgztlsJXZbe0fW24zvhr7-QdpbxODfLAW-O04a2Pjy3G8Q-RO0dGiETqD2wo7IRdqgVi2csN-XONBfU9P-KDUA9gzlMD4Y1HhSv5Z5NY3lXBN9t9Ly9SxJqejJ015cduB1iZJIVcw9rltvbNCsEaCC-6BCw8Q8SUOjRQUdpuAo65L5Vgvn6GLGvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در این تیم، همیشه جایی برای پیرمردها هست؛
ایران و پاناما پیرترین تیم‌های جام جهانی ۲۰۲۶
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23000" target="_blank">📅 16:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22999">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5-cBQY-UFPc2niDn6Pjqk4SABPgl_nBW5Wx2gBsbvz2oCly4jHn7t8gwVz5bJmTiNIyXroqrJOXTBmK5ukDhD45ulvCqrss9Yrpf7vyZbt1bXqDnBG6v-dgOTcompgTVKzeCn9tSg_a6cWLuZMwUgeDMogUvtkkTo1rQ0fxc-0khHUzbX6UHMAUEHepsYjC6rl2XMbXvsfT7f4cbQXQPGPKYUDnLTxVMIkBEZNifIN0qfINOK_Nd-fdI20DLqtmnqj3UejxlTt_nQSfWkQhXqnz2E0IqCJ6WohJ9v5ZbVlax29gORPvNIdif6XyLGIUWzg8aaFByRhQbP0caLFoag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛برخی‌دیگه‌ازشبکه‌‌های‌ماهواره‌‌ای‌که‌بازی های جام جهانی رو به بهترین شکل پوشش میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/22999" target="_blank">📅 15:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22998">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFA7IbQObt_XIzJDaie7ekGpwKyJ-KMF7RAbUvkdutsq-JhZbic6AiIPOgmQfEj-N3Re1CszYzAsRC1rB_o9UplQA9tHhchj-YKLhjjyVe5ZJgnlmoFgsyuTyuyDG7mhPBbYyCYlVETX0HuhrHg2sknZCiEKTv9a92Wxwr3n1GE2S2-KfeprVhSNBt4VpvG2mgMZ_nfhG44IsK6WEWht4rmZOLpmBvhvDhlGYVQFQE-3Wjwh3yhZ73iBXAKzliJYNlKA3SfgEwxr9Uvm2JKFeGDmkKTE-Da8StjXKeFptItw6RJgjvBawspOJKHifyuhESQM9E9w0mR6jG5i1zuicA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛اسکای‌اسپورت: رئال مادرید امروز شرایط خولیان آلوارز رو از اتلتیکومادرید جویا شد. اتلتیکومادرید اعلام کرده هرباشگاهی 150 میلیون یورو پرداخت‌کنه رضایت‌نامه آلوارز روصادر میکنه.
‼️
فلورنتینو گفته دوتا ستاره 150 میلیون یورویی میخواهدجذب‌کنه.مایکل‌اولیسه…</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/22998" target="_blank">📅 15:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22997">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UuoJ-KXOcNQL11gpQigUaBausNUjV6tafqR0_Un2b7qVdseplK_ff6al91NIzfYpbQoQV0g1iyof1n9-FAYvENkBQ30Y9Nm4LeTqhaPaouA1TbPDihmE-1Nh67fJDDx6mKgwQ58KHKHPiHsE3P6DEp_QP18jPcDoE1MNc7gbRtEPpTZDoYjFwC2j4s8-6GZ9ezbQepHnVP3FSzP6RdBT7zJJjR0ob-NBkawUc5pQtw_WKc2zvejQNiVAm8PiSggzhCF-hx7S0l15hPFmVTtUiFcp_ojJ-Bc5MtjrjM_xwVBGBL3QXb108wLiD_lrXYE9OoSG9FrUtbWU2sRxmrrudA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
#تکمیلی؛ رئیس‌اتلتیکومادرید: هر باشگاهی خولیان آلوارز رو میخواهد باید 150 میلیون یورو به حساب باشگاه ما واریز کند. نماینده آلوارز به ما گفته که اولویت او پیوستن به باشگاه بارسلوناست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/22997" target="_blank">📅 15:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22996">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6d3e29ee7.mp4?token=Tck1scQOnxBsA7pBPHWbviFfgLindA8b-4WIawwgeEU6Z4PontcG01rMChJTjw8hdtMte9wjIXyOBS0jpBnF96eK2x3NnkPLkP_Rn0LbGB1YHtwghIrtf6eBQWEK3v09jm3Tgc_1Hk0bLatV7X_SjO8zTQZhKhYKMbykj1xI8mfYyhDyIT2BegSC39zF9w8zoVkAnMj_gRhFNh0yHi1cReqBoJ3pByCSFBJifXPWcn33h6XerSKjw8EbG9yJ5J-J1oF3W7Tdl9QUKD027jEXDwxv4qukUI_iYQvk05sGGOQiqCb3QPsNddncnm8lVWqLsy4JALd8EBQ_O6-RKW5Z5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6d3e29ee7.mp4?token=Tck1scQOnxBsA7pBPHWbviFfgLindA8b-4WIawwgeEU6Z4PontcG01rMChJTjw8hdtMte9wjIXyOBS0jpBnF96eK2x3NnkPLkP_Rn0LbGB1YHtwghIrtf6eBQWEK3v09jm3Tgc_1Hk0bLatV7X_SjO8zTQZhKhYKMbykj1xI8mfYyhDyIT2BegSC39zF9w8zoVkAnMj_gRhFNh0yHi1cReqBoJ3pByCSFBJifXPWcn33h6XerSKjw8EbG9yJ5J-J1oF3W7Tdl9QUKD027jEXDwxv4qukUI_iYQvk05sGGOQiqCb3QPsNddncnm8lVWqLsy4JALd8EBQ_O6-RKW5Z5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین‌یامال ستاره تیم‌ملی اسپانیا و بارسلونا درباره دلیل بستن باند روی دستش در حین بازی‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/22996" target="_blank">📅 15:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22995">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y17pAczvUzOoRiNyjfN8QEIZ_NUAoq0Y9onL2x5KPZZ3o_7ftP1T5AgizN9tZE0jPk4wcL_iWI9B-3dry2yhU7N7zPyznNxPFBnJ8AO8aHgiwZvgP86EvFfUBpJve83zwtRUg7OF-utHg-VLyNaRTDSAhRT0GT7JUQCMQjGt6ZlLlLfawQLvVq8vlDvZYj1DqCoWP34V104RcJ7pQNUwjHDkDbDa5ZABC-9cpXSDyS_AIvHCAwKnJ9YrIkpGAg7MVt8voNr2Hxo6_m1FDAj8QSGe8Qc18WURotB7uAt097MZF4rzHzmL8PqOjekjVggy0OGjAWL10TgJ-s6HW5O2CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نقل و انتقالات تابستانی امسال برخلاف تصورات بخاطر بحران‌ مالی‌ باشگاه‌ها؛ بمب های بسیاری زیادی ترکونده خواهدشد. هم پرسپولیس هم استقلال و هم تراکتور و سپاهان خرید های خفنی خواهند داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/22995" target="_blank">📅 14:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22994">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b9e0c4e99.mp4?token=RVZRqS2THUjZwVT_WGk5SxOwVP--D_UuV1cflm8S80BGsqxFbWaKVk2f7WCk5c-oRx0tjm900zaY1sKXsqjGdlFgEZ9cexNIDwIl8kFQ_SdKFPOW2cVQduxKS4nCrrBFF1Jq64l3BzSYgaiMFCUkX6AUs1P7GkHh-F5XfJfAdrO_YCHxcpMwsYrfnxsEJvEjePlAoYl2JeiKp6ykixtx4x2emvuAoUuwVBV-xSpge8FtNwdotP9Ijl1tFj8S60CSkXng4wtsv42OK4khoYLXuhsXN_YlalItsfqnPeq4bYyaYfUR2LFpNp-YGvyE2TShIuMqSdKxfMBiHyvpZ-qZPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b9e0c4e99.mp4?token=RVZRqS2THUjZwVT_WGk5SxOwVP--D_UuV1cflm8S80BGsqxFbWaKVk2f7WCk5c-oRx0tjm900zaY1sKXsqjGdlFgEZ9cexNIDwIl8kFQ_SdKFPOW2cVQduxKS4nCrrBFF1Jq64l3BzSYgaiMFCUkX6AUs1P7GkHh-F5XfJfAdrO_YCHxcpMwsYrfnxsEJvEjePlAoYl2JeiKp6ykixtx4x2emvuAoUuwVBV-xSpge8FtNwdotP9Ijl1tFj8S60CSkXng4wtsv42OK4khoYLXuhsXN_YlalItsfqnPeq4bYyaYfUR2LFpNp-YGvyE2TShIuMqSdKxfMBiHyvpZ-qZPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بازیکنای تیم ملی فرانسه بعد دیدن اون عکس و ژست سمی رایان چرکی اداشو درمیارن
😂
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/22994" target="_blank">📅 13:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22993">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5w_SR0q278tvKXWroz0OibIUdzyfSYoDX7Tn62MtRcle5tvnlJ5ga6R-gMlkq2yDPab31nzNQoahJcAUmjwUoY52oQ3plzY_AInmLd-LbwdOiBHfZcq77gBtz6pP-FJ9zFY5GpVkg0FQ_1NSzz_W6v2URnEQOg0_TrJPRX72W-Xx2L_tTX1KHDtjU6zspVdUh-AKbVREu2B9f9VOyWvapEYeM3dIC3MT3OmU0FnLRYsrnEufqIgFJcPdrNI1iABMrVnGzUMcXC8NMBrkchBg7G7nCA-MMWazr14D4I5URp3cy9Op4Dd_OHrrn0IID4BBsq7yx92XkVXxHXeE3O-gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/22993" target="_blank">📅 13:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22992">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-NFo26pEmCRVixmy2ewstA9uOUrZpk537oZ2IORW7DzX7saOLOud9TSdbOTG2U3LAGIqYSA3zvq76lcTBiCKOp71jjHrt6Ebj9szSg0L0B-SPj0HkVrfwvhBbbcsXOaFlMWx4h9CTljynfEtB0cJ8SGcbnD4q682FWmb77sfn08-dAOfNHZvhjw8dZ5uZOIkP0Tb6Yt4bkOD3WpWTwFFiD_hPw5JfWR92QdNRYfbaGVqltRdBABdTVe2sIkL2m4KfMOD5q-YmfYDHIK7hc74pr-oJbh3SPnfhTTuTU9UlV-HBIdLUeZvZshlDfxYlUTb2yGZOv33s8tE7iF-hdHVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ محمد جواد حسین نژاد یکی از بمب‌های نقل‌وانتقالاتی تابستانی امسال فوتبال ایران خواهد بود. حسین نژاد به ایجنتش اعلام کرده قصد داره به لیگ برتر برگرده و راهی تیم محبوبش بشهه. بزودی جزئیات دقیق تری در این باره خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/22992" target="_blank">📅 13:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22991">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2579758a5.mp4?token=vRRdrNS1KYG9REDrwAYpTlUCLGgXFapkY5afQplLOIIq0RC6c4oZ80yG1Ie7p4hu7Ck-kEgZJG7e1AP_7_j96Wq3Bx5FveeMSJSOndaECQDiyKMHhgvzQmfiPlxOODMuUFghu5GI7qL238Sx7CXGjAIg-n2uDNq8C8dS0APwmcGb5IAfnYZUTTT2ZInIBskh_jOz3iNYh50zIjrzMj1BmCLHkDULn9XQwL01PjWJ_ieffsK7kTQ73JMn1qHID9jy_RyOLQGZrvoLrnM0rm9Z3r4Gb3QtV4zUUhkfgJuuyX7itgev2F4kL_9RhLXO55r7oq3bdqcSf8sg8wqB16cS9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2579758a5.mp4?token=vRRdrNS1KYG9REDrwAYpTlUCLGgXFapkY5afQplLOIIq0RC6c4oZ80yG1Ie7p4hu7Ck-kEgZJG7e1AP_7_j96Wq3Bx5FveeMSJSOndaECQDiyKMHhgvzQmfiPlxOODMuUFghu5GI7qL238Sx7CXGjAIg-n2uDNq8C8dS0APwmcGb5IAfnYZUTTT2ZInIBskh_jOz3iNYh50zIjrzMj1BmCLHkDULn9XQwL01PjWJ_ieffsK7kTQ73JMn1qHID9jy_RyOLQGZrvoLrnM0rm9Z3r4Gb3QtV4zUUhkfgJuuyX7itgev2F4kL_9RhLXO55r7oq3bdqcSf8sg8wqB16cS9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرد البرز که بهترین خط دفاعی لیگ یک را دارد و هیچوقت دریک دیدار ۲ گل دریافت نکرده بود. اما فرزاد حسین خانی با چای نبات و شاگردانش در مس کرمان موفق شد در ورزشگاه خانگی فرد البرز به این تیم ۲ گل بزند و ۳ یا ۴ گل هم ۱۰۰ درصدی هم نزدند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/22991" target="_blank">📅 12:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22989">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNGR9Hz0pesKS3RgmT3XMNtmdnaPcCKy93QafL5gYNgsfZHMPYJGCdnlgOx7kMu-CdVxKfW8NQOncCXOO2UeE0cfmWeCNiSjtiA1tjlp1R2JY71GA8J6O6p7mpLqwj3cJyoTnjkmSSrmZgkB5wr43sqXblv6iuj9ItZCIdj8Vyd1lha-48Ft0Tmw2oClif6HAlm8-Z76GNHDWtuPqQGybigORQusK8T6bAkIRr4W_o_jYgBgiBxxztZUUdPHPry4S5rs9blpN5Qvzf9TF8oTaJw2CZK5s-D2_RH2YKi-GBPhu_grkr4mv4qOiSgL3_JlXUqS9l9okv_kxGieTORYxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اگه‌اتفاق‌خاصی‌رخ‌ندهد؛ اوسمار ویرا برزیلی چهارشنبه یااواخر همین‌هفته‌وارد تهران خواهد شد تا برنامه‌های‌آماده‌سازی‌پرسپولیس‌را از نزدیک دنبال‌کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/22989" target="_blank">📅 11:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22988">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMWcB5lQb9txbAt9In5EVx-G7Bu8oliQs2Xf_SHid6nGXoU8IhibqzUH6c71bS4YI6rhEIIdhd_RA_LJWejMgfbG04zBAOX_puVB-JCDvczxa2lGMvFC1hvmOU9x37kwhPlxMCewqxgmea_nd9tLEm6NBOEqt0Wk-QZNgqu6vg7VFTS62vxk1R3oJDsTKzJrusXWX3mhackgXgv4zNHDs_G69dlqGQ4clubQIO6vYuauOMlDmhXlx90FDf6d8n7BO9qkVP7TmqzloWDrBhISeNFcP15Jx7R42MhQ4VilcTqxRb78jisFt2WhSzgztbz5Hc_qSv0xvkISOH8B_lW-fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛طبق‌ اخباردریافتی‌رسانه پرشیانا؛ بعد از مطرح شدن نام جواد نکونام بعنوان سرمربی جدید گل گهر سیرجان؛ مهدی تارتار از مدیریت این باشگاه دلخور شده و به دنبال جدایی از این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/22988" target="_blank">📅 11:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22987">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c19cf6b3c.mp4?token=QbWTpl-bPLRiLyD9Me07_HZHTDdlYVfQclUZUUyj3JUXekvU6sJolIcnu49LfwawLYc4fPIpKaCdigCjxqaKj8iwO_mRAsWGIzROj37T1RXU5OTXnqFUQi6mmR6mzClxJW9gZS8ZTQL3DT2uB4aXyPtPl4ofwnWW9UAz_2dzsTd9pJBfbR8xKXQF6B4F6EvqqnmUJONq2ZxCQPBRRqm0DqKxxnDZeaHR6SZlAJY_48zhxYuY44an3TJM0G_VlcixCAB-J8Pv-TiIz7FhxAydg7P5DZ-tR0tgE24lwL68goZEpKog18haF6xl8bFMwAhJbNXm-MUa4cmgTs4zQuN5xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c19cf6b3c.mp4?token=QbWTpl-bPLRiLyD9Me07_HZHTDdlYVfQclUZUUyj3JUXekvU6sJolIcnu49LfwawLYc4fPIpKaCdigCjxqaKj8iwO_mRAsWGIzROj37T1RXU5OTXnqFUQi6mmR6mzClxJW9gZS8ZTQL3DT2uB4aXyPtPl4ofwnWW9UAz_2dzsTd9pJBfbR8xKXQF6B4F6EvqqnmUJONq2ZxCQPBRRqm0DqKxxnDZeaHR6SZlAJY_48zhxYuY44an3TJM0G_VlcixCAB-J8Pv-TiIz7FhxAydg7P5DZ-tR0tgE24lwL68goZEpKog18haF6xl8bFMwAhJbNXm-MUa4cmgTs4zQuN5xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نه‌داداش جبر جغرافیایی توی پیشرفت آدما اصلا تاثیر نداره؛ محمدصلاح اگه تو مازندران بدنیا میومد:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/22987" target="_blank">📅 10:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22986">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d73e5ee7c.mp4?token=IagftBkVha9b5mByOvH7GKO3BNJKOWCg7Y3NbZupOtlePzyBCRGFo-s09W91ulhUUXnoLlgJ5fiW1dA3Si1RJQCtEO7ckIrmrpR50TYjTS5ViHALDxJ_ZJjfztOTayNTXeA3Ea1v_G7lDFsHd5E15CWQTpJzfsdQO7sgWHmXPNmrrdMARUaHJOQR5VrB6rWKk-pnllzDl4tzeXrn5prQeA5NOknXrWZwjiQWTXp_og3sFGvS2fpjePUWXHy9478bqC0aC5NboLbmV8jMGw_IRd_eE9XRQHISJSIp02s7ApAI_eDDDA2jw_-DpoOTixoOmgDQQdvsR_j-a9eOa_tblA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d73e5ee7c.mp4?token=IagftBkVha9b5mByOvH7GKO3BNJKOWCg7Y3NbZupOtlePzyBCRGFo-s09W91ulhUUXnoLlgJ5fiW1dA3Si1RJQCtEO7ckIrmrpR50TYjTS5ViHALDxJ_ZJjfztOTayNTXeA3Ea1v_G7lDFsHd5E15CWQTpJzfsdQO7sgWHmXPNmrrdMARUaHJOQR5VrB6rWKk-pnllzDl4tzeXrn5prQeA5NOknXrWZwjiQWTXp_og3sFGvS2fpjePUWXHy9478bqC0aC5NboLbmV8jMGw_IRd_eE9XRQHISJSIp02s7ApAI_eDDDA2jw_-DpoOTixoOmgDQQdvsR_j-a9eOa_tblA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
#فکت‌تلخ
؛
مردم‌ایران تنها مردم دنیا هستن که‌موقع جنگ‌بیشتر از اینکه استرس جنگ رو داشته باشن استرس قطع‌شدن اینترنت بین‌الملل رو دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/22986" target="_blank">📅 10:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22984">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g63Q5dFZ_JsOP5xeuSKAEN6Sh4MGioFfo2_5meBJ8_3dg9ygpfsXKVp4iymORRIxIrMelvelFxt5zTUFkqjMlpMS1btAiG_U065bREC236vwGlszdtID_kASbSFEUg-LU9cptFyr-obr9x4lVBeRqCvPjOMXczPFRM4gZm_LGgggFnV2ujqSptjRXrOS4FsWZN6Q_Kt3zNQ-FNo3oPw2f_jVbV13banZPDtuWDOQq4aWK2WmcH89nP3QOQlhNeJov4-1sNx8PwJ0Ph4zX9I9gRvtXh_cUt6ei5mhU8rl168zD2J0fuaJFYhk4nUzTqPSQx-zsfzz0LY7sT3oCmFC9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nJ96utiUTURQpspiSlz_UV0dRycHDGz_qOdtMwzF2VEmkHTI70zy6Iqll_rMCwfqBMXCMpmCqGMa04grugez_CPfxot-InbVLYsqiQ5wAE6dXw4pMp7XrXiO1uzyJhqr9Nu_EfbMraJabV2-PnDHpyqHp0wtv02raBJ4HKJOqOc3qpSDttJh_XWRdo_BUo7jW0C6OT99pVClOQRghzpLncNk8PY_zUQdRJdAXclqV7XegYsY8rgyUxGiF-ioa6UX0bbxrscSF-1C8upb8Mayb3p2SvPfPyML3gaZe3wOeRa8dp6hJcFIOquujfQXzvP-FUs6DDSaGOcFzAp9Y4oYDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
بماند به یادگار؛ یه ریاضی‌ دان آلمانی به نام Joachim Klement که قهرمان سه جام جهانی اخیر را با مدل خود درست پیش‌ بینی کرده، معتقده قهرمان جام جهانی ۲۰۲۶ هلنده.  مدل او که عواملی مانند تولید ناخالص داخلی، جمعیت، فرهنگ و رتبه‌بندی را در نظر می‌گیرد سناریوی…</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/22984" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22983">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fa0118288.mp4?token=q5eM0nyjO36EO0jBFLenAsT9HH0l-hANzO8HTNjm-27C2jGGs-EcoEb-OIxzpxQIeyKFsab1u3QnlV8XNAmkZXJv2oUDhdsY6AJUaE4UvsOMLjVwuRvQL8upvigl2HMqDJCkVay-mRXCtg758mxsoPt839IDBibXqTI64MxM2RiMGbxuScw5reRepPqOroyJzQL5GBiqZyn1a3guP9UT2wmnMpV_9QBeYUdkFNMMKmPXJDOB19e1Ub12nkdCMedh2SCJ6STptL7Okrq3cIYxDWcILYUdxA1fGLXtp197D8yihhLz01-c24v39fJrMA2nJv0yK7sIcRgI1zKd6Gkvig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fa0118288.mp4?token=q5eM0nyjO36EO0jBFLenAsT9HH0l-hANzO8HTNjm-27C2jGGs-EcoEb-OIxzpxQIeyKFsab1u3QnlV8XNAmkZXJv2oUDhdsY6AJUaE4UvsOMLjVwuRvQL8upvigl2HMqDJCkVay-mRXCtg758mxsoPt839IDBibXqTI64MxM2RiMGbxuScw5reRepPqOroyJzQL5GBiqZyn1a3guP9UT2wmnMpV_9QBeYUdkFNMMKmPXJDOB19e1Ub12nkdCMedh2SCJ6STptL7Okrq3cIYxDWcILYUdxA1fGLXtp197D8yihhLz01-c24v39fJrMA2nJv0yK7sIcRgI1zKd6Gkvig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
نشریه ESPN: بازی دوتیم ایران - مصر در جام جهانی به احتمال فراوان بازی حمایت از همجنسگرا ها خواهد بود و فیفا نظرش رو تغییر نخواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/22983" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22981">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEPu8feoRWR3baADSRkAxc0dKCe59EVtO_9yC8g-bToHMDQv9qwl6Fx4rOI2E623OYYNDM4sojHXGf941_WkK2U6YQ1yeC94wmpGBTQ-86LiroR8H3AI2VetpMcL5G9RUfRvH8rh0A1rUDCm66O_6Ul0cLN9GBg0nYGBruzTPvcpStpXk4qhl2-G7cTD_J047IPJ66rwfPVTs14kjrPu85CZpjwTkinDhUbqScdnjSjHwVGUKuA7joVoG95bs0zbE0v_iPWT5Pe1I8tJiGxvDzU6eA_IlZT2etWV99Z6opgjM7fEDito7pBfLHQGbCO67KGZi4X1N1nP-p_2HqQ-8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان تااین‌لحظه نتونسته مجوز حرفه‌‌ای خود را از AFC دریافت‌کند و ممکن است درصورتیکه مجوزحرفه‌ای‌این‌باشگاه صادرنشود یکی از دو باشگاه گل‌گهرسیرجان یا پرسپولیس تهران جایگرین این تیم در سطح دو رقابت‌های لیگ قهرمانان آسیا شوند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/22981" target="_blank">📅 10:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22980">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pq0D6fFvA0A5PiMolsoZG4vkRxTvHbTBBz9E812wVFD2tyAPK9m1DroE6CVhDW49SrZTrb0eQ5dIwqV8s_iGGJitkO-1IliH0eV2sYiEwb1nZLmhlBBjnFBNU3GZSkdzt0BezIzJOpEeDjVUL5U18LCkDJLefxjzXtG0AiuFA-AQB9fJ3Gi17_5xmRPDgF4zbPhcaQ0_GPTlECjgbZw3Bt29TmjL_GylWc7CfI21bffVBJU6ulVS8UdzYwsEGnNBpt_8us8rbz5Gag4Ocw2Lnrmee7K8ZjOxVkyCSf0o-um0mXvLVSZreDeBFk5WtNBh_g9ADKiM_xy_lJ5m6tsJwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌انتقالات
|موندو:
مارک‌کوکوریا به سران چلسی گفته که دراین‌تابستون‌میخواد از این تیم جدا شه. اولویت‌او بازگشت به بارساست. چلسی برای این انتقال حدود 50 میلیون یورو از بارسا میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/22980" target="_blank">📅 09:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22979">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nebWP9PgcIcfk0I2k0Yfyj6cf6ekZSxEJF7RUrXNRCvwaWUt-4HlklCZtDtOXBnTEswAI8wD_AikrhcKmFO6I0SR0U3-WkeS8OIDZDxs8TbYVxI9wbVDaqoKH0ojp7nJdCTDsD4n99vc5TxbGO4V6Ns6qw3FnNz2rnMZEwRHT7HjshJCXUCuA5irNZ_8LMAptMNhdONcivYhBO6tm0B3ie154TiyfbNcTU-wvTcbJtNBIcxc1eJSjqVdoGWb53KOfymA-tzVIN16BRCmiSpfMGO_p8MNMCP4QUudiWkXKtc9Bn0FAR4I8umXMhT97G6PH8hEwQq53HhV_uy_eX6IQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تموم شبکه‌ های ماهواره ای مختلف که قراره رقابت‌های جام جهانی رو با کیفیت پوشش بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/22979" target="_blank">📅 09:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22978">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REkQ5jV6EJ4HyiFdS2WlBy_lSwQA-_lGw-RM8YSP6VAdc7VMwOJkDFkxFJ5cen-oZBHvBTCNY1Gf681KAJK4aefxmpcC65Fu1g9Z1tjXrADaRy9fhdxxN4jVJRGkNMBssaYX1K-Z8AFzi4CXwrc5sa_Y7YqabhNa8WmAEOTz1pcrXEjcEfG3sThRAN_N4rxFBmU0yRu8VP6_GX8wHS-SP8pnR_AU_bWoLy1KLVazuwqrjTRoJEIrUIQ8zJMIUrXZa5hk7lyIUAk5TWFTM_6zzNJEVdetYgxsfuWd1l_FHzd85a2InBwRDlH9XEfacvEG7cVRL9IMBlGYJSVo7mENTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/22978" target="_blank">📅 02:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22977">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmmr_5jKkJh3hgKcWwAcbqFtnL23YavULZTh97M81u7cKAd_0_DLV5NptO3Wt5iwzOKo6SIBiUe5niQiRGr_oqHYAnxza6FmrEIlxrvXaWmFWDzF7CE6oCl6h4BS_6Nk-CNR-P7RaJhIaKbnMrzBUy7Pm2Px_oZCAzmKQ5rUCQPBJDUPZc4OgqENSMn0apDfd5-UYl0aDujFuzaCV9ezMw0rlh43UuO2VURFHR3WMootsH5PN-h1tvGerAtTEAviU8zXbe8sekfTDldyNLH4bhcvWJK5NNixcCgjpKNZgc7553g0GMo04_AxQFyIvltlL_VTly6bcbRepma5M9Qzug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/22977" target="_blank">📅 01:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22976">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOdnZfDv7AxbGMy_ZelrJvhNDvlbcbiIgx6kD9bTxBS3JAUf-XBZmD0h2NmcsNzGznZK8P4icbN6EU9ZVGAw7agjqK8iAACyYwcSUprlzfAv2P54UYnWz8QpWkWNB9s6baYyMpqUxwulfqhuzmoL82N_bBd22cuUo-B34xM90EKJkAdWu-H30WONtTuEERUWr0VplBPM5eAOZzn5U3X3bopJT8tx78BonBFXazIXqzvxPpbzCBaKvnmxyTKAJemhmyB4Tw5lbyvK1EQBCq-JZL8-QUllnGhi3RK1Ec3AGKpyFxZtPMGKLn20cGiSDAfIxP9vUU5UVC3LZR9JrH2XMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛پرسپولیسی‌های‌حاضر دراردوی تیم ملی از آریا یوسفی مدافع‌راست سپاهان خواسته‌ اند که برای فصل بعد راهی این تیم شود. یوسفی از پرسپولیس آفر قابل توجهی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/22976" target="_blank">📅 01:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22974">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofkfhxNz70D7YiaFfo_2ZwRyOdU7rEuGHt4ddGc9SLWvCPVydKofz1V-Uy-1dqP83dVPc4CXk_Ar6Kwp32wXpjygkV1-hjVDxVnh1w92SBSITvOYf3e9metot7DBju3wyhW0Xy9SlCf7LiEHEdvkc245WZSntu-dsFQvkmScgf_itqW2Tc7Hfjv7JPuV2NyyoKlf-7hcicT9Ct0xBStUzl-pg_SgZ5NdBoQdlLMKxhx3okZWn9yQa8ft5GxR5x-9Pf1u58tet_2l99vAOroMxHzH4eNcNbX2fSodJqMmdyFaVd-o15n_VEG92wfr4cSEWzqCmjnQkZtifURZAMjhDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌دیدارهای‌‌‌امروز؛
از دوئل تدارکاتی شاگردان کومان و کاناوارو تا آخرین بازی فرانسوی‌ها پیش‌ از سفر به کشور آمریکا و جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/22974" target="_blank">📅 01:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22973">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KpHrNZHbd4FIF0oEQHjVcu6VPSRLPPvk3pwfZSV_03EAYqCDM5ZZ3R2qvQ7VmhdWsYtVgbGKnym5yOgx0y2Nucj0Wq--pknf4JESnU1pHAeEoI5ShS6Orzz8qJsPfTF6qtDU6QyXPSsWcH87--0CewoAgeurRzNcrPpFnzwK-lQ-ol9ms6-9TpRulGNR-L0yTqlPvzcoaz4Qr4hWhIERBC9Jny1drTLcgHTkQJwmxpgdWBnYeyFG56VFecOtJTJG50z4ldAYtW2sjjsYx_h6p3mj07D54d-8YtxFdxfnUfUw8RQPEozwXqtwUOBo5aVKqMgfcdQZMcuIyo34MZlBVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌روزگذشته؛
از برد آرژانتینی‌ها در شب‌‌استراحت‌مسی‌تاتساوی درجدال نروژ و مراکش
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/22973" target="_blank">📅 01:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22972">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUeYaWPDTnPlcK1h5HCQo-XR_3tWVjQnrtCwzWO1cHgGljA2QWBwlmfIBmT4kcXHQlR3628LSgaE6qMxeLNs81RKn-C48mrQTa_2CcG5BdUgym7RsZ1vfBkibSiijT3sUF5Ty0ml_JdIOo46Oh40KbUrTRyQyfXd7w_nNsWKwnSIw_jfOxqR_K2ygGM5K03_3pvDqoJJ-SqcxXVTf9dXtRqosBRh4vBXQduqRsCy4Ta8zz92ld-dF3AM1E4Qu9IrSFyKspM9S0dUKalcPDo-xfBEU-JcUAqEe52NSSlp9YgFJ6jyP4qiFz7OKCBXxOohtStU2-3dwqI78C_ugB4QDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوشش‌کامل‌اخبار جنگ در کانال مردمی مجله 21؛ نمیدونم چرا سرنوشت ماها اینجوریه. انگار نباید آب خوش از گلومون پایین بره. امیدواریم که حداقل نت‌ ها باز قطع نشه که هم اخبار داغ نقل و انتقالات تیما رو بزاریم و هم برای جام جهانی دور هم باشیم بازی هارو پوشش بدیم…</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22972" target="_blank">📅 01:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22971">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a6fa71d1.mp4?token=MoRXXcYfkiFFuWaTngI4ah7pN_RPUmPe_Xh_nquJcwNe31CdBmWdAex-45Eh8NT38Ehc_qnfYZ42ztVU0Rx0o-Czm3cz5SklnaaWtuTmnmHZb20uFHY9eAJCHhgl4l7bw23duRxEO15Dxal2ie6WoBIpvcmXYDRzarsC4QFB8uRAoFcxG5pGzU77W0KGmCittS38I-0A0W6OfXFvorJ4FXEm8ywj9j7O2Ke_RabqUBuNwSzN4z4Lxy2rObTjGIZ3QkTlGyxBjwqY_15dPw49-9c2qlDO54m0IqiEXqwO4vp659z1cd1RhCG2Nl8pZYMJ-Dnfiw-cKRvwpI88QQ8Nl2fNfbGxwtVDU8t6od7lug6obU0EYFmjnH_bwdAvC6vivSKJgTgF4kfeqIcwZXOU0iQzyW3CNOyE3lTxqLFbHhqs8QDuugdOZvUwNuXjcu4yHx5jKEH1YYneev7932MfpuYlIlBNuV5QvhN2LI0vkYHl38QoAdA7BTacnxE5pDpkweICluja9IBYKx0XEPDuqhpNUUE2amnNQQHXhE6OcVbfr-ZOigqOwC8ZDNHL5rypZhX9UL_lPLGqD1B4LBuW3m1tyFABawlb19UX6PaNvwPJSEXT2oAo9eH06sAMFn2wIYCJKfRMYalr-LRRhuVmR0UYx5Y1-O3jGLEtLkgQ7hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a6fa71d1.mp4?token=MoRXXcYfkiFFuWaTngI4ah7pN_RPUmPe_Xh_nquJcwNe31CdBmWdAex-45Eh8NT38Ehc_qnfYZ42ztVU0Rx0o-Czm3cz5SklnaaWtuTmnmHZb20uFHY9eAJCHhgl4l7bw23duRxEO15Dxal2ie6WoBIpvcmXYDRzarsC4QFB8uRAoFcxG5pGzU77W0KGmCittS38I-0A0W6OfXFvorJ4FXEm8ywj9j7O2Ke_RabqUBuNwSzN4z4Lxy2rObTjGIZ3QkTlGyxBjwqY_15dPw49-9c2qlDO54m0IqiEXqwO4vp659z1cd1RhCG2Nl8pZYMJ-Dnfiw-cKRvwpI88QQ8Nl2fNfbGxwtVDU8t6od7lug6obU0EYFmjnH_bwdAvC6vivSKJgTgF4kfeqIcwZXOU0iQzyW3CNOyE3lTxqLFbHhqs8QDuugdOZvUwNuXjcu4yHx5jKEH1YYneev7932MfpuYlIlBNuV5QvhN2LI0vkYHl38QoAdA7BTacnxE5pDpkweICluja9IBYKx0XEPDuqhpNUUE2amnNQQHXhE6OcVbfr-ZOigqOwC8ZDNHL5rypZhX9UL_lPLGqD1B4LBuW3m1tyFABawlb19UX6PaNvwPJSEXT2oAo9eH06sAMFn2wIYCJKfRMYalr-LRRhuVmR0UYx5Y1-O3jGLEtLkgQ7hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از کواراتسخلیا و کول پالمر تا میتوما و فرمین لوپز؛ 30 غایب بزرگ جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22971" target="_blank">📅 01:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22970">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32598b0bc1.mp4?token=HMyhIV_BRnEIrylyAdMF3MtILgFhbWWap_jMw2xfpa_dEIiIZxW6bPDf1lGVh7_2bZTcPhcqJQIkatgsqatyZl8XOwUdxK_ka6Q7IRzzStnke6oauPhgT2aVAX_5X2LhEDdA6EeekAgTcT2cT9vwMdieovIU8i8W2OS8yQI2X7UT1Fcrg14YcvKvP34LSGzbBJyTkzLXjQhvcJ7KNhpfW5pg3tvwp-cKsxv04hGKu9QdgtdOcxCo78xNUd_I37Sa9AZvNp902WEL8PeuVMcfd82PL36i9Fxp7PorN68cDztQ4BHrIhadBnPodycYBy3moUrxdcjh9rCeIiXaYf40vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32598b0bc1.mp4?token=HMyhIV_BRnEIrylyAdMF3MtILgFhbWWap_jMw2xfpa_dEIiIZxW6bPDf1lGVh7_2bZTcPhcqJQIkatgsqatyZl8XOwUdxK_ka6Q7IRzzStnke6oauPhgT2aVAX_5X2LhEDdA6EeekAgTcT2cT9vwMdieovIU8i8W2OS8yQI2X7UT1Fcrg14YcvKvP34LSGzbBJyTkzLXjQhvcJ7KNhpfW5pg3tvwp-cKsxv04hGKu9QdgtdOcxCo78xNUd_I37Sa9AZvNp902WEL8PeuVMcfd82PL36i9Fxp7PorN68cDztQ4BHrIhadBnPodycYBy3moUrxdcjh9rCeIiXaYf40vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ایکرکاسیاس گلراسبق رئال‌مادرید در مصاحبه با روماریو: «مسی خواب‌وخوراک‌رو ازم گرفته بود.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22970" target="_blank">📅 01:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22968">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bm3-sl6himYLbYFCVHD_9N_Ab9FMB93-w89QzBFGmbBjFOWleuxTJYw4DzSnAeSsATXi3KTTVoCmmY9uvHFOsymOdLaCee74BUeriUVYSARhi2bjagm9zc6nfHGLB7ESxVMpuzfX1vNSB09UyybYOu4_cxy1KLYq-f0n4NRfz625JYnhWl4JWS4WP4KTCQ11dF5nrvcvw0VGLWACEMYukXQxq0JPf8683M4CpQL6JLtHgIPOcQsLs9iDrg90JJvkQC3f0kvSaic0scXEwfZ3qxmQaHyj-81fbJpFVHa_n3EdNInUMHRwosPcovJGXXWhzg_h8gB5g9fr29HSdIxGDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای رسانه‌های روسیه‌ای: دو باشگاه ایرانی خواستار برای جذب کسری طاهری ستاره 20 ساله روبین کازان روسیه به این باشگاه نامه زده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/22968" target="_blank">📅 00:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22967">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca6abec005.mp4?token=mZABs93FiKVfToHxSJesDqAni64DZjZ8SM3hNxXCMuqZA4ZDdL4eX-8EG_VrRpNevS3Iv35Docssylp8ov2OC5r839g5HcTUW76UIuvdRjCv5ZcPFWBHRANAoENospNdZsMVv7OIBQNlWWGg7Dik9GEvu_XsNZTL6Vp0fWxWNi6d-osfHlJfVpOafWWecW3b01vpXDTM2qVe3Av6hgUZDOELPOVKOa-U82h3rc6K85KHx0SMndw9vAcvkV_mHM0IFw6ayP3tZYHSguTlKCTxFeulskPa0aT5pNtUAbTnVzEL42WruFK7KhPOMzTi9ZpXKgzdIEPpn-yaF93R0EDe2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca6abec005.mp4?token=mZABs93FiKVfToHxSJesDqAni64DZjZ8SM3hNxXCMuqZA4ZDdL4eX-8EG_VrRpNevS3Iv35Docssylp8ov2OC5r839g5HcTUW76UIuvdRjCv5ZcPFWBHRANAoENospNdZsMVv7OIBQNlWWGg7Dik9GEvu_XsNZTL6Vp0fWxWNi6d-osfHlJfVpOafWWecW3b01vpXDTM2qVe3Av6hgUZDOELPOVKOa-U82h3rc6K85KHx0SMndw9vAcvkV_mHM0IFw6ayP3tZYHSguTlKCTxFeulskPa0aT5pNtUAbTnVzEL42WruFK7KhPOMzTi9ZpXKgzdIEPpn-yaF93R0EDe2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
🇵🇹
امسال مدعی ترین پرتغال رو پس از سال‌ ها در جام جهانی داریم اما جای یه نفر خیلی خالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/22967" target="_blank">📅 00:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22966">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWsn__aZeeCf_wGszxMU2Nc267rjzP5am51S1Hfrq1mhwVWYs7mq3rlkbUrR8DMf5Ytg7SrIZBbmgDlEWnCU1NTRGeETEWXqlKfjeLsUm_NL-CIi6EOfm13NuUEdaCaciHDifUqx-AOu5Xggckl0jidjg_lA-RezlZVEzZWxzWfMzoxzlHq02gRLXyPMOLvvEREWDE3JNIv0cdd9iOXWqZrX3Fw2YbHAP3oj1sYNgoobqwVakW68geNgsJAiUp19Jl-szX8IeXFG_4p8kRs58Sb5fk5iHI7TI6YPNVR6vrzTWthSGX4XbNttsRsKP93Scrdtbx25O2jOORz_H_lQ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال خطاب به‌تیم‌های خارجی که خواهان به‌خدمت‌گرفتن امیر محمد رزاقی نیا هافبک 19 ساله این باشگاه هستند: 3 میلیون یورو پرداخت کنید رضایت نامه این بازیکن رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/22966" target="_blank">📅 23:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22965">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RACaGWXtHsDCY7v0fiELZputqo4-t7m8icReFI6tUYZuj5u29NFDMbS8lNlmrQO2olMrhC8hG9mxkdUxWg-uIGx6gkSYrmzkoo6Q3KhlYKLiVV6KHiFQp7ZWvw6J4uTljmqi20B6ozY9IV1xmq4IDktDXfgK7FbeCFXi9Ndo4R3GfMMmchea_5RJKBSZk716aZCK9GsZkRTJLMtYfRthoTJ-g7mh4b7_B13GmLBLy_kGQoUvLB1XKoipE6STVFpy4q6f57AqoVuIRhYMSBcDtPU6zjKEQBPniW7oBUUIJhEr-oXsHwl5sELdBwPYu0xrnEOGMQuA-7WxJErXOh17gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوشش‌کامل‌اخبار جنگ در کانال مردمی مجله 21؛ نمیدونم چرا سرنوشت ماها اینجوریه. انگار نباید آب خوش از گلومون پایین بره. امیدواریم که حداقل نت‌ ها باز قطع نشه که هم اخبار داغ نقل و انتقالات تیما رو بزاریم و هم برای جام جهانی دور هم باشیم بازی هارو پوشش بدیم…</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/22965" target="_blank">📅 23:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22964">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eaff3256e.mp4?token=l8I8UNul6ON5xspeuViRNlcm0i9Cs8O01w0nI8SihloxGkk4B-DzYFKPcTWrGTEOpgdbCDFooecBtsYYRfEU8JeBkJWQrMT1co-VgQCcl32zUhqNztxe5mttwL0ZZJ1OcosBszU3Ia4_dmmoncpHKAaT3cTGgcSGhPGClOVUEGYHbzdwWnCYmOvFJi1Fk1XvfYUALywz_kANXk2_bCcHZJPktYwvqQVRnyGKBEwFDE-X4PYpzJHiqW8RZJWHh6Tji5UW4g4WfbUDuHTa8xYqa1vkAMeKskJRWEMcNglCAcT8CQjp_WP47XtjjV3OS055FKnrpD1PPWv8UNKv3wWpWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eaff3256e.mp4?token=l8I8UNul6ON5xspeuViRNlcm0i9Cs8O01w0nI8SihloxGkk4B-DzYFKPcTWrGTEOpgdbCDFooecBtsYYRfEU8JeBkJWQrMT1co-VgQCcl32zUhqNztxe5mttwL0ZZJ1OcosBszU3Ia4_dmmoncpHKAaT3cTGgcSGhPGClOVUEGYHbzdwWnCYmOvFJi1Fk1XvfYUALywz_kANXk2_bCcHZJPktYwvqQVRnyGKBEwFDE-X4PYpzJHiqW8RZJWHh6Tji5UW4g4WfbUDuHTa8xYqa1vkAMeKskJRWEMcNglCAcT8CQjp_WP47XtjjV3OS055FKnrpD1PPWv8UNKv3wWpWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/22964" target="_blank">📅 23:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22963">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇱
🚨
شمال اسرائیل آژیر ها روشن شد دوباره  موشک ها از تبریز و کرمانشاه ارسال شد</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/22963" target="_blank">📅 23:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22962">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SA8q7z8wwGAoA7kBHhGee_itz8xhIoaJR7iVjV2DnPQozaeVIz-csk_xd7BKS-GZnQ5jNpwjNk-azWWWP-ElyF1mE2IFpK9LM4ds_PJctxjLWGl1mZJw1LqSNdF8wStTXPv_kIkyFgzeEmiEWASnEYhgKCPF0NfZW8WXmznEJ3hVk34ia5Wf4mhkG04T_k3Efn7BU14Le4x0JGgbJMAEZ7op2Qb45O5-KRxK_kZTXV841InDvORYoM7-EUdEMIc6St8fCnrQpOmgCGebs1A_ovyjGid7Y03jkV-4-FxDuB5boOyM4lZW1ozYDjpUNOLZW0ACjQVyNL0Mrp6UN3PndQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اتحادیه‌فوتبال دانمارک رسما اعلام کرد کریستین اریکسن هوشیاره و تحت شرایط خوبی قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/22962" target="_blank">📅 22:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22961">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKxmjzx4gUAQbU2yEWH434ppC5YnBspAQtKqTle1FSWtE4wwuGIN3v87nTwca58DXqmoYzpW_9Ka3a507twfiZhE4HScN3Mdf-GI930JJRyZPO4vepPo_p8B2ikllWmTir5NCHoSGm9-gSlz2CS3sPGwcr_5u7cRFolSVhKiMe8XKZy_Ai_NiUUqwk1geHEydd8ndpDdlQ7n2nCh-pLK8y1Soi99Z_sMG1FOf6c8ljPoS4vejCCVlHTVscoVfGWecZh6cJ8HfVHa5GsVrEhVwlkuL2Uwn2TQdYiG0Sz6gib4-8HHCIQOOOaNPsbVjnve42NoKhqQj7EVo1PFB_hMLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ انریکه ریکلمه از پس پرز برنیامد؛ فلورنتینو پرز بااختلاف‌آرای بعنوان رئیس‌باشگاه رئال مادرید به مدت چهار سال دیگر رسما انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/22961" target="_blank">📅 22:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22960">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiScv30gSo-WVrTCUOD9xLqa15zDxyFWLYpIJSKijPhtpY5vTEFfYsdb0pst7Uq_JtL0bO_vP0bCIYWBRjcJV35uO0rujiLf--HwU9jpLGhdPcIIQK38pzizwTJN4d5Z3T2BBt6vUY4ODX8JHAXX_u-yZ7GxxlZP_VsTnrbUS-95mkDVa-6Dk125HEtAq5ExQqRYDJrneuihIL4_9nWd4ua0gSOokUnISmMac09OQGoN2fhBBQdf5qHbhMCJnRRdGKn_H8SQJEZuYxKWfWyahUCQ1CD4RhGk8frwjofV0Ocpc1FUgbnzW8ZHcP3eM2XE5F7ukoZfGlKbsSUWg2zxwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری
؛ شنیده‌میشود محمد عباس زاده مهاجم سابق پرسپولیس، فولاد، نساجی و تراکتور به دلیل مشکل قلبی از دنیای فوتبال خداحافظی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/22960" target="_blank">📅 22:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22959">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDnG-BMVunQ-FQDdAH87uTL9nEcqeWgDHpvMD1ZNVN-36w5NRuxmESoPxoCjcnbT5PPose2ksJh4vYwYrIuWXQswsb6LXzOWU2ei0c7zguJHjKOXyrxPLJGqKdtOW6lTrAQB6y0PCpLO3P7PCGt5FBht9i78N6R3xF3i7vYqqHMj21JRA2msJa3J6XYsFkm3RfN_EkDnWoHIo3emxxy5SVtStqBfsioqCpngX3Tqv-Gjaxhc45vR7OszVHygCYmGkXJp0sojE0jO34XgNsWfLyi4HJpE9sLoiil1fy0wSChhhKXixW9VjjAy0TzG-6bQapgJ631Ebw8P8DcADkcKmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#فوری؛ کاپیتان‌دانمارکی‌ها بازهم سکته کرد؟!
‼️
دردقیقه64بازی‌دوستانه‌امشب‌دانمارک-اوکراین؛ کریستین اریکسن کاپیتان دانمارکی ها همچون یورو 2020 دوباره بیهوش شد و بازی نیمع تموم به پایام رسید؛ امیدواریم اتفاق حادی رخ نداده باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22959" target="_blank">📅 22:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22958">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bffa01c1d.mp4?token=vGjJYmsfxmELKvk3iML9hVphhwRVm73LLDfye3vwJnRMKmG8oNnpeYLH71lxrbm9Jmigq_iv6VgLWq8GhC6DdCZX1O__dDWx1gGqo4vHMj7dp8tDzk_q24FBymk2fkiD9aFiiTwNCV4PbpUPwbIzCXWb-zEpmNanaAx34589pe1GKDNCokZ5ZnF0LxLCxqVfi7t6L_NABHK6s42OopKuFhwOo0E-HaHzfkglTnKgx0-XlFb6KjVWcgCWljY6Ghg3WcFfB_0_1oKEV7w-b9PjMMm09mI9V4Hj1pfABPkE0lPMYk6qzlCOFPZIiPwTauUYe77qUZBACz6kNsBpZR3YyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bffa01c1d.mp4?token=vGjJYmsfxmELKvk3iML9hVphhwRVm73LLDfye3vwJnRMKmG8oNnpeYLH71lxrbm9Jmigq_iv6VgLWq8GhC6DdCZX1O__dDWx1gGqo4vHMj7dp8tDzk_q24FBymk2fkiD9aFiiTwNCV4PbpUPwbIzCXWb-zEpmNanaAx34589pe1GKDNCokZ5ZnF0LxLCxqVfi7t6L_NABHK6s42OopKuFhwOo0E-HaHzfkglTnKgx0-XlFb6KjVWcgCWljY6Ghg3WcFfB_0_1oKEV7w-b9PjMMm09mI9V4Hj1pfABPkE0lPMYk6qzlCOFPZIiPwTauUYe77qUZBACz6kNsBpZR3YyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#فوری؛ کاپیتان‌دانمارکی‌ها بازهم سکته کرد؟!
‼️
دردقیقه64بازی‌دوستانه‌امشب‌دانمارک-اوکراین؛ کریستین اریکسن کاپیتان دانمارکی ها همچون یورو 2020 دوباره بیهوش شد و بازی نیمع تموم به پایام رسید؛ امیدواریم اتفاق حادی رخ نداده باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22958" target="_blank">📅 22:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22957">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjAHFHxE_UWkO8jaL_jq0rY2NQgnory_ylwZeYMQY-sHCG-Oq0OBuI-36WLK3APyVEWlQyJiqpIGowZe837QYMQtbLNIHHupR3yjmhz6FLqAzJTLccLVNk7OLxUspiZuYDgosP2wUF3ur4FQZlF4Zo5EeYs8eN4SrfzWq5HsZuD333-vHO9t1Lo7LwI5Linn_AcCKL1UJn4HaFAuR7qOTvQ5-qbkZxv7uB1kFtuKy5NHOJ23b5Lo-J8NH3ERiPcvcpkhcI3aELFkwA105LaX3aI3Kmpw2kmCjVy1DBCS44iZoZXsogWzR6ByZURWFgOUIjU_YCCDUEdEhGFljUk6PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛ به‌احتمال فراوان آنتونیو آدان راهی لیگ امارات خواهدشد. او دو آفر از باشگاه‌ های اماراتی‌دریافت‌کرده.همانطور در روزهای‌قبل خبر دادیم جدایی آدان از استقلال قطعی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/22957" target="_blank">📅 21:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22956">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b1b174faf.mp4?token=NrFELOM58VLIAjnkdU_MbyuuP-96rv_v_1hC7o-Ujc6U90RFQVKEtG17F7guSzkz8fj5h81R0xgQ0GP3i8tPMyX0sV-AzM7fRdJLSHpxOuA95mEA9rgittN_87qyiuz4P4GRnL6Iqgp5esZdlHuQDiMow4HTVDRfVyeKLBju8fWK8n1fVYOVhiQqEBHs_Rp0dagMo6GdGgPB8k4RiI6S4CNHFrPFY1Ta4ajCHMwlAm_zLyRZBLUDrvVUE47S3tjNmpWdiqX3sZHI4B38585_Kw_8Rx-QotTX6nIJEFs4XeEW9L1CyoZhzoropI1kcMk-xAc6yICcoyflUY1ZG_exbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b1b174faf.mp4?token=NrFELOM58VLIAjnkdU_MbyuuP-96rv_v_1hC7o-Ujc6U90RFQVKEtG17F7guSzkz8fj5h81R0xgQ0GP3i8tPMyX0sV-AzM7fRdJLSHpxOuA95mEA9rgittN_87qyiuz4P4GRnL6Iqgp5esZdlHuQDiMow4HTVDRfVyeKLBju8fWK8n1fVYOVhiQqEBHs_Rp0dagMo6GdGgPB8k4RiI6S4CNHFrPFY1Ta4ajCHMwlAm_zLyRZBLUDrvVUE47S3tjNmpWdiqX3sZHI4B38585_Kw_8Rx-QotTX6nIJEFs4XeEW9L1CyoZhzoropI1kcMk-xAc6yICcoyflUY1ZG_exbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#فوری
؛ کاپیتان‌دانمارکی‌ها بازهم سکته کرد؟!
‼️
دردقیقه64بازی‌دوستانه‌امشب‌دانمارک-اوکراین؛ کریستین اریکسن کاپیتان دانمارکی ها همچون یورو 2020 دوباره بیهوش شد و بازی نیمع تموم به پایام رسید؛ امیدواریم اتفاق حادی رخ نداده باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22956" target="_blank">📅 21:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22955">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqoDGtmhCPXw9lkwmLen0Pamy3qb2EEhdzqOhMf4-UFyS_hDVlenNYgT0E7IpnoDndGVZHxgLZipV1g0sIxVdQcrUBnA0hdSeX2RHb-XAoYKuOXt-Ooq8-lERnwV55RVo-l1Uvqc9p0YtZqI5uYXriTBgw13vW2Ht2tgibzwZ9lTC9C3LyqYAWI526ZBoKpspSQuITcknycZC6xd19ciTJLQjJ3TX4ptjajY4Ge7K3K9-BVGdeXHfGsqlGZInghe5cEZll4qVEN1v-HIfMCntlMTGAoqexWCDzq5ZXDRnYhrkSf_uLhm9zxUZs7pMtgqDnj5QNnM4ETz7hP2O6oyUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#تکمیلی؛ کادناسر: بعیده که‌سرانPSG ویتینیا یا ژائو نوس رو با رقم 150 میلیون یورو بفروشند. برای هرکدوم از این دو نفر حداقل 200M€ میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22955" target="_blank">📅 21:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22953">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/om5cHjv5uD8O3jNbHmGlHi-tbAufEnmG4kcQ_1f67OrlVsMje4kCWQSJg-V5K6x0hppCrYaMtkbucJLtPZaG9RxBCMoehOmKMOnGGpwlo24FrvlSrgKplbYDdjT_1g1gQbIC2yQTPDhUq_qGjJb3AI7LUmMNMu2IfANjF6Hf1YqCg3fN42Zcw7dEOXjZwZetOXJ4X4zvkgutstlMmZfwBY7tUUBdZ-vjaClAipwY1WUGp5X_1xhhYJ4eE3TKDsu9VN-mPY73GdxzSYTF7hBT1Vf68-rNIqWA0YFXrVdvVU1wQ0gTMs7VxgsqU9QYMg5zrmyw0InVebgl8E1VvJcxVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DlJl2hp_cb8-gmEXhgc7idwvYPEz3cilapN66cWYBYTi1ujf4mbPTHV2s5njKoDCneZ8Dzyr2mGRjJl04FKRwB2qfwUXqrCs5Oqh9wc5hatk7GUSRnH8eltl0WlCUgXf3WDu8GyQxk2LtEB1NEIaN9Z5U8BkzGpUK4XzTEI-yifCsfIjWBPP_-UDLaeEow0W_M6Z6jBz0AK0LFAhDU-88u3xn9QrjzDiA6R6TNqa73I2PY8GJ9mz2Z_lzIKfUAI5RxH3dHi3cCtERRYx7i9gRXLABBoE2mqV7LLsaTbHyqiVbgNgwz_tEW7MWXe70Y_M1bFB-dRraKcAwHHfhPBI0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ انریکه ریکلمه از پس پرز برنیامد؛ فلورنتینو پرز بااختلاف‌آرای بعنوان رئیس‌باشگاه رئال مادرید به مدت چهار سال دیگر رسما انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22953" target="_blank">📅 21:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22952">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHg-6ZnJH63Q0-AlUPvtCrtSEgBeX4-k2ZPuz5U4j0FLyiLqMHMAF8gOeTSoG8v6kro2jF1lajxNfuJ444r-7Oz8_4OpOD9WLsUKwIkDIIYsvxBsGGvs6DzpYRfhmZSyj34ljCWbDL3MMs5KX32rMQf0Tvjhqyq7cTv7z_c9xrgdMm-5WBGruOx7LEuWH39_dGtRwv_arwEUlnLDyTZkwPkpS83mvsrnIV715Wm1q7xYaYU9Uwwg4Ws296hfcZTL2YiNgyNAIHwcnwI4YQfeOJntO5vPIQw14XIGcLbJjY9nLptBYJ02a5CBUphlvnrSh0GOOc9i0aeKGJS48MyQ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
حواشی‌ دیدارآینده ایران
🆚
مصر در رقابت‌ های جام جهانی 2026 از نگاه هوش مصنوعی ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22952" target="_blank">📅 21:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22951">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c25ae3aa7.mp4?token=NyNZl0ENKujNtAayR3-_Mq_F_P2pWn30A5KQI4mhtyyQMJOGRy-Y47CkIYxbOHryecNgpQj9cyDPPGVdwee9YV4xlVYr1H_v-Mg69y-i315WcFkXZIlB1UySWMVViKtX1zvK90eJOg2PG3RQ4_ARYzdG3aoxc2BUklF9sCkNC1nJttsF7bI5xeY8B0M2A8HknJyI9Q-fBPQqQGdMyWs-MYvRCjON7ChDSg5Xi4GrhgcR_1gMnZEIKaQsxT3YJ6Oqr03Ji2XJ1JeQsiwyB3Dq1kL3mT4iKvLJ66Gyxa7pnHDkCqJsd5vaw_zn2x0VE41pdHcVfcyos5WVcFPrqF9AFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c25ae3aa7.mp4?token=NyNZl0ENKujNtAayR3-_Mq_F_P2pWn30A5KQI4mhtyyQMJOGRy-Y47CkIYxbOHryecNgpQj9cyDPPGVdwee9YV4xlVYr1H_v-Mg69y-i315WcFkXZIlB1UySWMVViKtX1zvK90eJOg2PG3RQ4_ARYzdG3aoxc2BUklF9sCkNC1nJttsF7bI5xeY8B0M2A8HknJyI9Q-fBPQqQGdMyWs-MYvRCjON7ChDSg5Xi4GrhgcR_1gMnZEIKaQsxT3YJ6Oqr03Ji2XJ1JeQsiwyB3Dq1kL3mT4iKvLJ66Gyxa7pnHDkCqJsd5vaw_zn2x0VE41pdHcVfcyos5WVcFPrqF9AFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
تیکه‌های سنگین ابوطالب حسینی به تاج رئیس فدراسیون فوتبال درباره عدم صادر شدن ویزاش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22951" target="_blank">📅 20:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22950">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohdGhPGT4XGDKPkTqA5zBwVj01x93gmCl9HEG6gJCcAJ3z3v1zp414YKVk_4ltf9RbeooQh8orJYliZVzG4E7jb3xWGx2LcAkABiTSYhlb2z35ILi-3BYbIn0W9-WH-EWW0Krp1Ee6iBuC3f3lrviPeDE58qXH-xSBazCMmN2MlyrH9dewivOLN55qmlGKugvUIITf8pNnwy4Nl8u7L_jBsClFYStmnzALF3qwKYvMHuiNJo26eZwkXGc6r_GQfdCWvcAhm2IROdkHpl1kCqHzTjTRWZFCNjPiaKCi8oVpD05ofZTdgADeRwGCKJoRbEPBGGvKvj9Gz3Bw1KOEDpzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ سهراب بختیاری‌زاده سرمربی‌فعلی‌آبی‌پوشان موافقت خود را با پذیزفتن دستیاری دراگان اسکوچیچ درصورت عقد قرارداد با استقلال به علی تاجرنیا اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22950" target="_blank">📅 20:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22949">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbl180frSxfCyTFFJwAJf4impWPiFsxsAzMDr1PqOQvE8ZwLFD5IpeVtikeu5fJ7z2QSIJahXdHICerbIF1wkZe4V0WA6o1MeX2QYkKTa1-6-wOXEWLdqOBhdbjpHjl-t-ak890LdX0xMqzmELm9ib7EUDMJgXQlifw2bRYdVlm1msseQIyfpwxzgi-VCusnTLKVYQNPlNKLEHhbqSoXh6JL_WmiGdcACoiEUgwbVF1B5qcN0uVnKRSsYQX2fDyV2_W1u59UYw6iUeSdALnLARKjtmbEuJC-HDc3XrEET98Exre2ZFgvSqt5fxj_L3dsi4wE5KlLcwxM4Jsmv2cfxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#فکت؛ اگه کریس رونالدو در جام جهانی 2026 موفق به گلزنی شود؛ به مسن ترین بازیکن تاریخ این رقابت ها تبدیل خواهد شد که گلزنی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22949" target="_blank">📅 19:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22948">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmGKyNLC-YWR8hxfPr603Djc7D84n03iLD6mKJLamh8QidkYVC7rLrZUYRXZHMwVi2VqilBgFCrPpxt-gO4Fo2JRUPTrLdtjK00KTS_O6sExBKhKWRATKHON7VvoscSAdinvqDxKeFlG5hkW-unSWqPqfsNELoPbR3TAxGf-zjXP-ed5S3qz_tpPrYdUBC8O9vhjvpnI0MXGzTICQe_Q2nMhTAzJqAnvefbyfAf1QgL5jGYoLUst8Y6vSSw9s7uQunWYaOcXtqF-C6IvSAYTGoiL7CKk5ytebV81Bt9gydK0DSMfydnnlz72YRYlT9fUPKNgCHbf6qAmaddxy3ql9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ باشگاه روبین‌کازان‌روسیه به مدیر برنامه‌های کسری طاهری اعلام کرده هر باشگاهی که کسری طاهری رومیخواهد باید مبلغ یک میلیون دلار بعنوان رضایت‌ نامه به‌ باشگاه ما پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22948" target="_blank">📅 19:17 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
