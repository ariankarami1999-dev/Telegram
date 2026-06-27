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
<img src="https://cdn4.telesco.pe/file/EyvECTPmCiQCNQqT5mVNFW_ZH6HX-FF-Dc3bqDcQuU37IRoMUE8WnlkQGIV4T1TVBOKDKkPAVkhdP8ajb0xgP3wEzgcmwPTSEON2EOuotCoKmuOKUpGedLYGANf8yCPBWTtP6QayHk33P_dLrqb09e9gfjvAyOJy8c83jp5aemEETyDxGIxbYHdXc6tABbxSJYkDyCdz9uXJi1cmvTp1dELdEPgVE9Mme01HspdLKhPr75xUsVyLrkYhlZ1AZTvONdkt7YWvMw-jCe2ylAi_Jrhl1-Kgyh3_FCjQFCIewisChzJkwqE5gAr6wlqZu5AeM8NfMqsgpF7KnFI_px7WCA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 19:16:34</div>
<hr>

<div class="tg-post" id="msg-18047">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">⛔️
دولت ترامپ ، دسترسی به 2 مدل هوش مصنوعی آنتروپیک را برای کاربران غیرآمریکایی مسدود کرد</div>
<div class="tg-footer">👁️ 262 · <a href="https://t.me/SBoxxx/18047" target="_blank">📅 19:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18046">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/raatHvNeoW9sXxv_f8JdquiuqYxeL_bVbaJGiaolRtlbVtIh_jPIW8295kgd8jnw-iMgzgHme1eU6t_wcC6FKATioU1uK6Z87WISA2SZX-vvffm1aYqO3Ypy11Ql1GLj472KEKpZnsxPY8fIwKrdGyp_fhQf15L3nJYwTb1ldz5bvSsP7Kn9E0W0RVOehiQ4XfqedVVibpAnTJqKGgAEZdqssVzws6cN6iioxkmB0P2MBUxuH26la1CVi8crACjhr6i7f175neH25oKCy7DJyG26InqPB-gMT1rJusNeUWjiZr5tRJfMG2EKqxpQi9Iy7hQ2-8Tt9FdYMwNUPPSnoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شادی فلسطینی ها در غزه پس از گل مصر!  مصر برای اینها چه کرده؟!   دیوار کشیده تا از شهر موشها (غزه) به درون مصر سرازیر نشوند. یک بار هم ارتش مصر فاضلاب خود را به تونلهای حماس سرازیر کردند که باعث شد چند ده تن از اعضای حماس به دیدار خالد بن ولید بشتابند.  آن…</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/SBoxxx/18046" target="_blank">📅 18:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18045">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dafd3cf871.mp4?token=hhn7sKgJr7HLw9t7BYnQfhQq0DnprLc3tSxO0y6W3nf-U0gmi5Vsu_ym15lyvhEU7TcV2Gk-2PED8rj_4SAlcp4ADnTI0Nw0CtW-bzDvLw1LbEkwri8VJv0q3du8R_EcMMyT-MtvSrrIavsCvXBhJIWpg8qoj8wJqUUsKHQoAgfqXKb1Sj2Da9zp96N44w7u_NxyUvXiLsG2bz35cNnVjvVPh7oB_LJbs5cWUHhiAqXec1n6XvPNRpejsw7MjwsCLWczTVYwruOkpkRXJdq1zIVYQFkwnyqskNBW1JPNz2aJSDoY2m1xkglURkglohEOv0Irw22mPz_0W6mQNH2Sbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dafd3cf871.mp4?token=hhn7sKgJr7HLw9t7BYnQfhQq0DnprLc3tSxO0y6W3nf-U0gmi5Vsu_ym15lyvhEU7TcV2Gk-2PED8rj_4SAlcp4ADnTI0Nw0CtW-bzDvLw1LbEkwri8VJv0q3du8R_EcMMyT-MtvSrrIavsCvXBhJIWpg8qoj8wJqUUsKHQoAgfqXKb1Sj2Da9zp96N44w7u_NxyUvXiLsG2bz35cNnVjvVPh7oB_LJbs5cWUHhiAqXec1n6XvPNRpejsw7MjwsCLWczTVYwruOkpkRXJdq1zIVYQFkwnyqskNBW1JPNz2aJSDoY2m1xkglURkglohEOv0Irw22mPz_0W6mQNH2Sbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی فلسطینی ها در غزه پس از گل مصر!
مصر برای اینها چه کرده؟!
دیوار کشیده تا از شهر موشها (غزه) به درون مصر سرازیر نشوند. یک بار هم ارتش مصر فاضلاب خود را به تونلهای حماس سرازیر کردند که باعث شد چند ده تن از اعضای حماس به دیدار خالد بن ولید بشتابند.
آن وقت هواداران جمهوری اسلامی، ژنده پارچه چرکین کشور خیالی فلسطین را با خود به ورزشگاه برده بودند و این هم جوابشان!</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/SBoxxx/18045" target="_blank">📅 18:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18044">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">UKMTO:
گزارشی از یک حادثه در تنگه هرمز دریافت شده است.
کاپیتان نفتکش گزارش داده است که توسط یک پرتابه ناشناس مورد اصابت قرار گرفته است. این کشتی به پل فرماندهی خود آسیب دیده است؛ گزارش شده که همه خدمه سالم هستند. در حال حاضر هیچ خسارت زیست‌محیطی گزارش نشده است.
به کشتی‌ها توصیه می‌شود با احتیاط عبور کنند و هر فعالیت مشکوکی را به UKMTO گزارش دهند، مقامات در حال بررسی هستند».</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SBoxxx/18044" target="_blank">📅 13:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18043">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">رودان هم جز میتوانست جزو گزینه ها باشد که ولی خب.</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SBoxxx/18043" target="_blank">📅 13:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18042">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سبحان الله! با Secret Box روزنامه فردا صبح را داشته باشید.</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/SBoxxx/18042" target="_blank">📅 13:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18041">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سبحان الله! با Secret Box روزنامه فردا صبح را داشته باشید.</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SBoxxx/18041" target="_blank">📅 12:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18040">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">الان است که اربیل یا بحرین را بزنیم!</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SBoxxx/18040" target="_blank">📅 12:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18039">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">الان است که اربیل یا بحرین را بزنیم!</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SBoxxx/18039" target="_blank">📅 12:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18038">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5RjispZqOVFobjpfzrCFnAimo7VDTeoyBC9BdOqFeMdFds-1lqCUbvm9DMnsXIJKhoca35oeG9T4_iZ0XZ-TV0nyHv_boL6Zo00XgpLht-WwDf8CPimLZIkSxEAiE0KX6JG7DdDP0FTN4-wZmCa40WvsIbi4mHmKXuPReItCRryPjGb97IPEp-dGRaYoPt789Dsi0uaqCHz4zKBbaUPiBnd1fMbcsuH_zFSwWqnymq5DukbeOmPi_lmgXxzkAJtY0toPMRiw14Xy1VXhayxGOTl7P_ZoxHxT14B0lKuzyqJFfDAhCknpH2z35RaVbJxsR3yJX1BJ_Y-Uu8txXsXmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذخایر نفتی آمریکا و جنگ با ایران
آمریکا از ذخایر راهبردی نفت به‌عنوان ابزاری برای مدیریت شوک‌های بازار و کنترل فشار انرژی استفاده کرده و کاهش اخیر این ذخایر باعث شده بازسازی آن‌ها به یکی از اولویت‌های مهم واشنگتن تبدیل شود.
برخی تحلیلگران معتقدند کاهش تنش در خاورمیانه می‌تواند علاوه بر اهداف سیاسی و امنیتی، فرصتی برای افت قیمت نفت و خرید مجدد نفت در سطوح پایین‌تر جهت تقویت ذخایر راهبردی آمریکا فراهم کند.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SBoxxx/18038" target="_blank">📅 11:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18037">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPdz2r4Ur455o5qUMoH0TDEgcIMSuMpTH8CH6Htq4JSnNFj8PPbdZ6Uf4CdqWiaqVSFHp4bs6AiKEhMnHtoBIsQ-soVA0aPFe7MhMhN9RbkkwCWTxqWuD9-Yqtal9_dwEDnao-p6h52SMtbJa_YKxS_iPNOIOzhklU9UwB6vX4UXu1hFC2j4GQk_ojQ1vXEDholGya2r6sbOEMZoXUoayvmNWzTmy4_TlhfR6qBS3-lFH3_55le3t3XvYx2I3NY8eiohnoD0dKoCi0RIO4aXqyB3cKxumoDnwzl1MAVoqCJArs4fvlLH8MaGDKWjVGVJ1nwZv33eyRJOYxv1tz0Dig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه بازی</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/18037" target="_blank">📅 09:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18036">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sc1nuYOJUwh8qlkaGlEiS6V4jiBWMvavMZi02ljnXOsyfiZH3ncPOjgdSmtKQxDE5Udle810_VHiWwOxnfDELNFNkdMmNAtLC9lbxUaleZh4--f9EaJQ7bIwy_-aoAEOz8l3qA8QqJdTGjHERuUWNCmGbvNXx4iLWHandggVFGAoYXRv_hAd66jN8zuzSu3ONdpFKIB_r6jWhbVzMyoD5mIcjfTSCl0tR569IC1KhE4ieLepeoRrN8Cysj1I1FNfBTPCd_0ked33YBVNSQ4DOWSeAc55nbc-kBrvlB9CI-1jLJUsE6P1hiKkWG-aJN52YeXotrC94Tad_CB3jusxeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SBoxxx/18036" target="_blank">📅 08:54 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18035">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتوییتر فارسی</strong></div>
<div class="tg-text">الان تو زمین بگی محمد‌ حداقل بیست نفر تو زمین و ده هزارنفر نفر تو تماشاچی‌ها برمیگردن‌ میگن جانم؟
• میرزا •
@OfficialPersiaTwiter</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/18035" target="_blank">📅 07:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18034">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">رسانه‌های دولتی ایران: سپاه پاسداران چندین پایگاه ارتش آمریکا در منطقه را هدف قرار دادند</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/18034" target="_blank">📅 02:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18033">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">رسانه‌های دولتی ایران: سپاه پاسداران چندین پایگاه ارتش آمریکا در منطقه را هدف قرار دادند</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/18033" target="_blank">📅 02:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18032">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی مجلس ایران: ترامپ هیچ تعهدی به اصول مذاکره یا آتش‌بس نشان نداده است</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/18032" target="_blank">📅 01:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18031">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">متن اعلامیه سنتکام:
حملات ایالات متحده به ایران در پاسخ به حمله به کشتی تجاری
تامپا، فلوریدا — به
عنوان پاسخی قوی به حمله دیروز به یک کشتی تجاری که در تنگه هرمز در حال عبور بود، نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) در تاریخ ۲۶ ژوئن حملاتی را علیه ایران انجام دادند.
پس از آنکه ایران در ۲۵ ژوئن با یک پهپاد حمله یک‌طرفه به کشتی M/V Ever Lovely حمله کرد، هواپیماهای آمریکایی به محل‌های ذخیره موشک و پهپادهای ایرانی و سایت‌های رادار ساحلی حمله کردند. این کشتی باری با پرچم سنگاپور در زمان حمله ایران در حال خروج از تنگه هرمز در امتداد ساحل عمان بود.
این تجاوز بی‌دلیل علیه کشتی‌های تجاری توسط نیروهای ایرانی به وضوح آتش‌بس را نقض کرد. علاوه بر این، رفتار خطرناک ایران آزادی ناوبری را تضعیف کرد در حالی که تجارت به طور فزاینده‌ای از این گذرگاه حیاتی تجارت بین‌المللی عبور می‌کند.
نیروهای CENTCOM به ارائه هماهنگی و حمایت برای عبور ایمن کشتی‌های تجاری از تنگه ادامه می‌دهند. نیروهای نظامی ایالات متحده همچنان حضور دارند و هوشیارند تا اطمینان حاصل کنند که همه جنبه‌های توافق با ایران رعایت، اطاعت و به طور کامل اجرا می‌شود.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/18031" target="_blank">📅 00:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18030">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">حملات تروریستی گروه های تجزیه طلب به ایستگاه های مرزی در بانه</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/18030" target="_blank">📅 00:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18029">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سنتکام   به دستور دونالد ترامپ و در جواب شکست آتش بس توسط جمهوری اسلامی عملیات محدود ما در ایران آغاز شد</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/18029" target="_blank">📅 00:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18028">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0LQwKkXYIV11qP1IvfiSxKYDLa9C425vQ7MtgYTWaZ4LZ49UJj7KFErWn0e0bsw845cGPm-F6N93CgJWokHEqr1sVL93th7cVvVGyhtCGjpvBzKWxudArdlTDLWaDnUJHiZM4NFbu3a4XMQJ55--el4cb5go1MSjpvoO44JnBSjekZEb2PpmhfGmAhD4KPwhpIZAdXSzB3xTVZXU1e1rmfYRkAwi4TKjuBoKktL7gN4T_v1ItOT2DANVlTBsxCb0eKwsrG6Fa72lxhYg053Si-5O-g5g4K0eRC5-YRFjY7fooeueGi1mjpSskp3XYnTELNELpIKqaxdlvoVGhfjwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ مثل ما نفت را خریده.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/18028" target="_blank">📅 00:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18027">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">الان است که اربیل یا بحرین را بزنیم!</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/18027" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18026">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">چادرملو! صد تبریک! / مردک نزن تو سیریک!</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/18026" target="_blank">📅 00:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18025">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">فعال شدن پدافند قم!</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18025" target="_blank">📅 23:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18024">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پزشکیان را آوردند که جنگ نشود؛ هر 36 ساعت یک بار جنگ داریم!</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18024" target="_blank">📅 23:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18023">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">به نظرم بهترین پاسخ زدن رودان باشد؛
هم آتش بس نقض نمی شود هم به هر حال پاسخ داده ایم و هم دل جمع بزرگی از مالباختگان خنک خواهدشد.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/18023" target="_blank">📅 23:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18022">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5Nff7yPgHFiO-EdIkB1enS52g-oVBChZ2YFI07q3-m7kFydR1C-15uqTMoUnT_mH603QkGJ2_YB4h4jH3BfHtDAflXvxatT7q0oNLB5mjvq-I3byToPUvzmX0kQ-J81y01j8ukusnwpkXeA2vjspbM9Lk4k6oDWWw-a5XyIdPtStesJxuwrzBJNctqyfxPhlywEXduzhFWgvIbdU9dBvCzH0UqDjqfGbq35OteG_i7htoB0zKEmgmRRI761idVmvPxAzODoOOf105Op8G7DKC8f7vSMMQx1QcpvBZsIY8IkBq2ZYyFoSC2zFybuI3p6xCFKhkh6WJ6cGQmjv9jKGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تایید حمله آمریکایی ها توسط یکی از همراهان باوفای Secret Box در بندرعباس!</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/18022" target="_blank">📅 23:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18021">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">این مواضع ضد و نقیض تعریف همان موج کذایی 4 است.</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/18021" target="_blank">📅 23:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18020">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سنتکام
به دستور دونالد ترامپ و در جواب شکست آتش بس توسط جمهوری اسلامی عملیات محدود ما در ایران آغاز شد</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/18020" target="_blank">📅 23:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18019">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ اشاره کرد که ارتش ایالات متحده ممکن است پس از نقض آتش بس توسط ایران با پرتاب پهپادهای تهاجمی به کشتی‌ها، با زور پاسخ دهد.  "خواهید فهمید! آیا من پاسخ خواهم داد؟ خواهید فهمید."</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/18019" target="_blank">📅 23:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18018">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ اشاره کرد که ارتش ایالات متحده ممکن است پس از نقض آتش بس توسط ایران با پرتاب پهپادهای تهاجمی به کشتی‌ها، با زور پاسخ دهد.  "خواهید فهمید! آیا من پاسخ خواهم داد؟ خواهید فهمید."</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/18018" target="_blank">📅 23:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18017">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ ایران را به نقض آتش بس متهم کرد</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/18017" target="_blank">📅 23:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18016">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">هیئت مذاکره‌کننده ایرانی قبل از مذاکرات، کتاب ترامپ را مطالعه کردند  طبق یک گزارش، مذاکره‌کنندگان ایرانی قبل از ورود به مذاکرات مستقیم با ایالات متحده، سبک مذاکره‌ای که دونالد ترامپ دنبال می‌کرد را از نزدیک بررسی کردند. این نه تنها شامل روانشناسان بود، بلکه…</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/18016" target="_blank">📅 22:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18015">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">هیئت مذاکره‌کننده ایرانی قبل از مذاکرات، کتاب ترامپ را مطالعه کردند
طبق یک گزارش، مذاکره‌کنندگان ایرانی قبل از ورود به مذاکرات مستقیم با ایالات متحده، سبک مذاکره‌ای که دونالد ترامپ دنبال می‌کرد را از نزدیک بررسی کردند. این نه تنها شامل روانشناسان بود، بلکه آنها کتاب «هنر معامله» ترامپ را که در سال ۱۹۸۷ منتشر شد نیز مطالعه کردند.
این مرحله نشان می‌دهد که چگونه ارتباطات غیرمنتظره‌ای در مورد فعالیت‌های ترامپ در رسانه‌های اجتماعی در طول درگیری پدیدار شد. بنابراین، طرف ایرانی سعی کرد درک سیستماتیکی از الگوهای مذاکره او ایجاد کند.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/18015" target="_blank">📅 22:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18014">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">آمریکا، اسرائیل و لبنان یک توافقنامه چارچوبی امضا کردند که بر اساس آن اسرائیل یک منطقه امنیتی در لبنان را حفظ خواهد کرد.
ارتش اسرائیل نیز آزادی عمل خود را در این منطقه امنیتی حفظ خواهد کرد -</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/18014" target="_blank">📅 21:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18013">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامپ:
بنیان‌گذاران ما در اعلامیه استقلال چهار بار به خدا اشاره کردند. چهار بار.
من حتی یک بار هم ذکر نشدم. من بسیار ناراحت هستم. حتی یک بار.</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/18013" target="_blank">📅 21:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18012">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sj4P-tvuEYumugpCi2QYWM6iyI34VH1haz5Wgohn0kf75VFXOjnykt7LGShQx_E8oHpiObRjUDg67eifh3BzFW-qiu-UVML9iVaYwMVUg2sewbfOgdHXG3-eKGvnrmkQe6Ffo2lol_uCeMa-xvcZDbH-2FOQZxP0TrTcYpHMm-bdw9RCXvBdb6e2mprxdRCLbHSlzQfR86ecY8vW3jdIW6uIuHk6lp1n84R8cOVH-jHHT512ovDAkJj0bvEpsYlrU5UwDxDpdkT4leOnRlNON9nU_bWbiaWlwa5YRcwgPXhpyU5JSS1gym-8Db9GL6A_1egtcz8GzMVqmuZ2ChS_XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ ایران را به نقض آتش بس متهم کرد</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/18012" target="_blank">📅 19:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18011">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ ایران را به نقض آتش بس متهم کرد</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/18011" target="_blank">📅 19:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18010">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">انتشار اخباری تاییدنشده از پیشروی نیروهای زرهی اسراییل در جنوب لبنان</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/18010" target="_blank">📅 19:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18009">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLnjjUzhjmlnrCfwlAWiG7iPxk1yKwhfFJXhcvetu9qNDVBaBWjNyT2DZwMRzJkYqenD2yIFOA68CEqofYyOY1sPxX9sRtK0Oh8rF3aa2KYrmXQ6lbsc2PgfjxVirocw0UHmBZUXv1FhlBiHHpQ6c7-YmKb4moFVic0tGOub3sKtHUCH59IUvDNsoTYy3R0Gc6LH59DRpcgNf3VFgEKbH5xbCgankkswWNA0BxnfVvy6XbX5C_dxCPQKouealPEFK2rafCvQebPW6EacDX5RjLEGRwe_61e785qNpsmW_3OdcwlWCsqSbUc8W9eFz69od9-l4SvnaXFRlLwTJkwSZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحقیق کنید.</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/18009" target="_blank">📅 18:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18008">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بانک ملی ایران در اطلاعیه ای از اخلال مجدد در خدمات کارتی این بانک خبر داد</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/18008" target="_blank">📅 18:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18007">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">بانک ملی ایران در اطلاعیه ای از اخلال مجدد در خدمات کارتی این بانک خبر داد</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/18007" target="_blank">📅 18:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18006">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اسرائیل درصدد به‌رسمیت شناختن «کشتار ارامنه»  وزارت امور خارجه اسراییل پنجشنبه شب اعلام کرد که «گدعون ساعر» وزیر خارجه این رژیم روز یکشنبه آینده پیشنهاد به‌رسمیت شناختن «کشتار ارامنه» را در دولت مطرح خواهد کرد.  شبکه المیادین نوشت: بر اساس این گزارش، این اقدام…</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/18006" target="_blank">📅 18:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18005">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvc6SKNw5mYZmf2GELO7VZKkEAAPsfp8k1zauuVQ-qi-wPzpEZMQZUcRz0ZK7Nk4CrE1vkpfoa7bztCN4Mqidx3R5UGCgx0hnQeokN336Mx35YxGD1QIKVRw8o2z4dXCZDzpd1hqG2edHDhOE_Z4dcpkKuQ9dJaYshKTWkxX_hxAZ-HfvlerhIyKCndWAfe6FLkZOwKLDW3c1fQe02LX69xY8Cqkzmi3h8RuGOU_Xw40OnoCyqMuYY1w83z4z-0puq1L_OIN4VO9R7E4I0EnOZwalPZly5YJ4_LowmQeG1zVxZdH1ovcmdwKT_xSC6posVvLZKKJ_8FMP6eOddbQDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">.
🟢
وقتی دکتر مسعود، نمی‌تونه از کاراکتر دوره جَوونی‌ش فاصله بگیره!  پزشکیان [در سفرش به پاکستان] به نشان دوستی یک درخت تو اسلام‌آباد کاشت که رسم پاکستانی هاست.  ولی نکته جالب اینه که هی شهباز شریف نخست وزیر پاکستان اشاره میکنه مسعود جان بسه کم خاک بریز. نمادینه…</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/18005" target="_blank">📅 18:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18004">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8vhjUfDJsTrT_RLB43e350YpEqsgKUcDhiOZp6WozegJj6jvQYmcUsXMnZeXI-jYsL6Vw6XSUH6w5yFIyPkCwm3JdID0UgvmaPwy363ix0zg1b2M2kmfTygI2xgHrSVLBK95OPGqZLKQRFeU2FtHrIZOLc3l2gsrO2OBmTreGRBPx15_Vvb8MF-JRj1wLuDLurDnyjf06vR4ebwSyTO8wrEJodL8HmSJjPEZVd_UccsUt9ZXQh3SdGxTJ83rDZaSbHJewWUQWCyVSQL7DNEF0OdiJsAHNCXNSXplLuWtjJkAYbjXyFXUWVtpFlyeHI3zHMpQvF6ZPlXBAyQJ-riBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاتز وزیردفاع اسرائیل ضمن تهدید فرمانده سپاه قدس، آمده عراقچی، پزشکیان و قالیباف را هم تگ کرده!
در یک لیگ دیگر است.</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/18004" target="_blank">📅 16:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18003">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6B-llv71vc0KZHXl-UoaDjrdZ2VF1QH0jHebyHj_8v-dq7pLCGC80WbbEdMEM5Q5KNTw6in5NW4rsDXO3OghURV4iQfkeiVZwbdNJi1MVxFFcEV778_3kyhFg8uojHN82cZaWiWBjqliIgL_cT1gzrR5JSOlElbb-S40QfCfbN2nqmKUwoq5I4KizE-HRAteS8Y6jmA2xirEL9cYDRdMOkhxKZjefVr1ZGg1V3iHWZaJ5smEZIho8SEFtRL_p-acbQGl1zoJn6DC3E0JDNDdDJzrwOt21jH8T8K38HNnyl3dM9n_fu3krOE3A_LurHAcY01r9xsBmomvGrTXXBJnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتشار اخباری تاییدنشده از پیشروی نیروهای زرهی اسراییل در جنوب لبنان</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/18003" target="_blank">📅 15:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18002">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">فرمان پوتین برای ساخت نیروگاه هسته‌ای در ماه تا سال ۲۰۳۶   این نیروگاه انرژی لازم برای زیرساخت‌های سطح ماه را تأمین خواهد کرد  پس از سال ۲۰۳۶، روس‌کاسموس قصد دارد خودروهای هسته‌ای را به فضا بفرستد</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/18002" target="_blank">📅 15:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18001">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">مسکو با فروپاشی بنزین روبرو شده است.  پهپادهای اوکراینی عملیات بزرگترین پالایشگاه مسکو را مختل کرده‌اند  و این واحد تا سال ۲۰۲۷ تعطیل شده است، - رویترز</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/18001" target="_blank">📅 15:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18000">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">انتشار اخباری تاییدنشده از پیشروی نیروهای زرهی اسراییل در جنوب لبنان</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/18000" target="_blank">📅 15:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17999">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/17999" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_تحلیل_روزانه
#اپیزود_394
🗓
june 26, 2026
✔️
تحلیل گزارش PCE آمریکا
✔️
بررسی تقویم اقتصادی روز
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/17999" target="_blank">📅 12:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17997">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OSRyoFJ9rcP4MghZKm3CBTPtHqeGvx_aWP_sxQXZT5jiGyi05GFqfHrVwRiZrch7ZhJOkL_0VCIvcHhurLHeIcNmSoyUgAQB7LWTiFeRNUcL_WGsUNZfmroAZBsnmbUPPOftRXPTGzAZg9Ak8H16KTK-DWUW1PQNC8L_Ubn70UFnAnQX_Rbg-yxNHmJXs_vCKaKTf7PqetbMrse-zEqLiHrDQMXNik_mrWONpwdirNql9MY7--kO7XpMaEgUHvcl6OTYRcSynnOueAlvirYPFIlAeYLRnXkvEkiRcu5ks66PBdSGBx3kmuxuoNN0L7ip4Q4J2myjP7RsRH4LJASG1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i7uqZhqojRpeyZQ03iPtcPaMxmNMAOFJFSZmpQIPECJ46VJSwpldCrIv_N8hFZN40C-DMQ8gISzSNFhGhyVHg51vpxuNFPcnQU8S_PlkBLwPHzHzarjFwG7m7n4V5-fvnGf7FQDYWz4AORjqZIjhIjIQh4E1Z7VB0AC0X0_RQdlTKjPMOf6wfGuADxA4AWOqaltxKLxLYdu73qe4QCoN_j6LbEvGN6zLW4sXJ2ppEAym-Bfl0LUBkj7Fx9JD_YknQiO8QJg3-kkZMMR8Mtofb4PY-iOJGmXbJRQ_h40Ao0V8gYjdpqWi9TO5QIlmWhYn2nlxljoxJo9yjO1Jv570Jg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بیانیه وزارت خارجه ضد مواضع مشترک آمریکا و کشورهای عرب خلیج فارس</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/17997" target="_blank">📅 11:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17996">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">پنتاگون در حال بازنگری در استقرار خلیج فارس است و جابجایی نیروها به اسرائیل را در نظر می‌گیرد
طبق گزارش‌های رسانه‌های آمریکایی بر اساس تصاویر ماهواره‌ای، ایالات متحده در حال بازنگری در وضعیت نظامی خود در خاورمیانه است و در پی آسیب‌های گسترده به پایگاه دریایی کلیدی بحرین، جابجایی برخی از پایگاه‌های خلیج فارس به اسرائیل را در نظر دارد</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/17996" target="_blank">📅 11:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17995">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">بیانیه قرارگاه عملیات مرکزی خاتم‌ الانبیاء (ص) :
تحرکات و حضور جنگنده ها و هواگردهای ارتش تروریستی رژیم صهیونیستی در آسمان برخی کشورهای همسایه به سمت ایران را اقدامی خطرناک و تهدید علیه جمهوری اسلامی ایران می‌دانیم.
اعلام می‌داریم چنانچه آمریکا قادر به مهار و کنترل رژیم صهیونیستی نباشد جمهوری اسلامی ایران هرگونه تهدیدی را علیه خود تحمل نخواهد کرد و پاسخ به این اقدامات خطرناک را حق خود می‌داند.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/17995" target="_blank">📅 10:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17994">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ حرامزاده تا کنون همه ملت ها و رهبرانشان را — از کانادا و مکزیک تا اروپایی ها و عرب ها — تحقیر کرده جز:
— چین
—ترکیه
اولی را به خاطر قدرت خودش و دومی را به دلیل مجیزگویی رهبرش
برو قوی شو اگر راحت جهان طلبی
که در نظام طبیعت ضعیف پامال است</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17994" target="_blank">📅 10:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17992">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">یونجه و سویا واسه من
تنگه و دریا مال تو</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/17992" target="_blank">📅 10:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17991">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">بوی گندم مال من  هر چی كه دارم مال تو</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/17991" target="_blank">📅 10:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17990">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">#نمیپذیرم</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/17990" target="_blank">📅 10:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17989">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ:   ما یک بازار جدید داریم، نامش «کشور دوست‌داشتنی ایران» است. جای زیبایی‌ست. کسی دوست دارد برود؟  برای تهیه مواد غذا مشکل دارند، قرار است مقداری از پولشان را بگیریم و  گندم، سویا و ذرت، بدهیم.  به مقدار زیاد. روندش به زودی آغاز خواهد شد. معامله بزرگیست.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/17989" target="_blank">📅 10:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17988">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ
:
ما یک بازار جدید داریم، نامش «کشور دوست‌داشتنی ایران» است. جای زیبایی‌ست. کسی دوست دارد برود؟
برای تهیه مواد غذا مشکل دارند، قرار است مقداری از پولشان را بگیریم و  گندم، سویا و ذرت، بدهیم.  به مقدار زیاد. روندش به زودی آغاز خواهد شد. معامله بزرگیست.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/17988" target="_blank">📅 09:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17987">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">📡
ترامپ فرمان جدیدی برای ساخت کامپیوتر کوانتومی قدرتمند تا سال ۲۰۲۸ امضا کرد
دونالد ترامپ با امضای دو فرمان اجرایی جدید دستور داد تا تلاشها برای ساخت یک کامپیوتر کوانتومی قدرتمند تا سال ۲۰۲۸ سرعت بیشتری بگیرد
این اقدام با هدف تضمین پیشتازی ایالات متحده در رقابت با چین در حوزه های هوش مصنوعی علم مواد و شیمی صورت میگیرد
همچنین آژانسهای دولتی موظف شده اند تا سیستم های حساس خود را تا سال ۲۰۳۰ یا ۲۰۳۱ به رمزنگاری پساکوانتومی مجهز کنند تا در برابر حملات سایبری آینده ایمن بمانند</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/17987" target="_blank">📅 01:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17986">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">الهام فعلا استراتژی مالش را آغاز کرده تا مثلا خود را در دل آمریکایی‌ها جا کند، غافل از اینکه ارمنستان با چرخشی عظیم به سوی غرب، در دلبری از واشنگتن و تل آویو ، گوی سبقت از باکو خواهدربود.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/17986" target="_blank">📅 00:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17985">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFokRsAsg6TeC4G7vYMosdF6WNEps-mBlzdj4Jg5hTgpN8Ts-Cu6h2nWqKWK8j2RLSFkuxEzzMNydvc9advJxYr3iWpoHA4ITg--4R240oWdGih3DEC3Qx6PFFXLz9gNpvl2sH-_cOSy3saq_ELf0Bf0oRRfiTqDdXfmynBwJyAPAs1jcRLp9S6SO1pWzbomPicPKDx7TPap1y7hhGGPgYjMV7OtS28y9UHZUs0mKXc1pDgvw908PT2Arf6xHXJlYaEq4pyafE_CR1W09EyMHTXuZBWCuhxqBVxWP0mM9xSbYh4RdNDatp7WoXrRTmEkYjmBN8WNt9aH2KxrKxfVrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا پس از انتشار این گزارش، حساب بسیاری کاربران ایرانی مسدود شده است</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/17985" target="_blank">📅 19:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17984">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">● این میم در مورد مذاکرات ایران و آمریکا توسط خیلی بازنشر شده.  @Milita_Camp</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/17984" target="_blank">📅 19:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17982">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نبرد دریای سرخ: اسرائیل نمایندگی دیپلماتیک خود را در سومالیلند افتتاح کرد  اسرائیل چند ماه پس از به رسمیت شناختن استقلال سومالیلند، یک سفیر برای این منطقه منصوب کرد. دیپلمات مایکل لوتِم پیش از این سفیر اسرائیل در کنیا، آذربایجان و قزاقستان بود.  در ماه ژانویه،…</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/17982" target="_blank">📅 18:56 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17981">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aM9HSBRg2kLornB1Uc7AJtYb_zLnlfJRvWBj7t1IAgCfIWsuB4WDpQyalAAcgLiPqE2Jpw2RzJUJhMOpbNoBlrIGoeYdV6ZD68QjFjJjNOrDEZFBUzT8z_ajbblk08VgjW3IkCuDWSldI8MjbShuJleaaeYJzIUNc6qsF4G0n87ZXag0qV1EEQ7mRLTPB9fP_I-VG5m5zJnFNQgouew_Bf5hNdOUHOex3JOa2Z_42Ldj40WXBp5RZEMtT4MyCuBLENy5PBcsDpMmPID-xbbC2_ktsyHs20gMwIY9CGSKiXhNccFu681sFXunMXRe8dgIEXP1tCmYnOl6Nr7yf3ERvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">- نیروی دریایی سپاه پاسداران انقلاب اسلامی با یک کشتی در فاصله ۷.۵ مایل دریایی از سواحل عمان درگیر شد.   این کشتی تلاش کرد تا از تنگه هرمز از طریق مسیری غیرمجاز و بدون هماهنگی با اداره تنگه خلیج فارس عبور کند.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/17981" target="_blank">📅 18:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17980">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">در واقع دارند می‌گویند از مسیر عمانی ها نروید چون اینقدر خطرناک است که ممکن است ما بزنیم تان!  سبحان الله!</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/17980" target="_blank">📅 18:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17979">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcXzbIpk2-CiApgAWOdgEqf4FtK7Hs7bMsNshfFQK9F2b9KZvLfMovFurOTd0i4Ysh-NrSfJZmv9IBk19tGGMq3Gkh5k93kpBTCh9_SCHmmTsV9tutZNmgC7SlhtUx834El1Unw8sHVD04VErNF7XLtTGteevq9v9bdxh5MAuTNjrWpLAKcUB0gsdDERe58mkK8-8ABnY7D3sJwaWaZe87kuxJ7_P0QuD-R5mu_Q8W_udVwb8m17QMcMyGXBrp4OwMtRFJdvOm5QyZToUk4FItPDB9PJ7AyF6x0po5_AfEo_CkfqCW906dwh5OwBQnrbyqNmHpRCueHxQ62wm5Gelg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش وال استریت ژورنال، ایران ۳.۸۴ میلیارد دلار را از طریق صرافی رمزارز CoinEx منتقل کرده تا تحریم‌های آمریکا را دور بزند.</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/17979" target="_blank">📅 15:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17978">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMILITA CAMP</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JF-48ngj5vkh_yLNnLbr4NUuPLE3VY55sS5w5UEakpO0IdFZTnbFkfqRDELLIrT-HhHY0W_zIoTkkx3yP8yBax3G915iU9b2MAaF_bzkQFkfkfKHaB-M2JgrXQmBElIvqi7k5g9Suj2OVsNlT18_YopK5sYTlzcf_h94FtkMuWGyyf2yCH-RalTGpLx604WlntT-zQ6ASd8lzVypXEbjoKMcRcAgTCVEeypAET29b0xJRtmCPio1-EebTuv2Hfk8sWkFLX5nERzla36GAW5fTXHgnAS4VXkbuVad4N9e4MBqVkmDq3J9qpolxBzlbkEV78lbAW8VtvmA-66q5LldWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">● این میم در مورد مذاکرات ایران و آمریکا توسط خیلی بازنشر شده.
@Milita_Camp</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/17978" target="_blank">📅 14:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17977">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">پس از آنکه عمان اعلام کرد که یک کریدور دریایی در جنوب تنگه هرمز ایجاد کرده سپاه این بیانیه را منتشر کرده است:
🔸
ساعاتی قبل بدون اطلاع و هماهنگی با جمهوری اسلامی ایران از طرف برخی مراجع مسیر جدیدی برای تردد کشتی‌ها در تنگۀ هرمز اعلام شده که این مسیر غیرقابل…</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/17977" target="_blank">📅 12:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17976">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پس از آنکه عمان اعلام کرد که یک کریدور دریایی در جنوب تنگه هرمز ایجاد کرده سپاه این بیانیه را منتشر کرده است:
🔸
ساعاتی قبل بدون اطلاع و هماهنگی با جمهوری اسلامی ایران از طرف برخی مراجع مسیر جدیدی برای تردد کشتی‌ها در تنگۀ هرمز اعلام شده که این مسیر غیرقابل قبول و کاملاً خطرناک است.
🔸
به اطلاع همه می‌رساند
تنها مسیر مجاز برای عبور از تنگۀ هرمز همان مسیر های اعلام شده از طرف جمهوری اسلامی ایران می‌باشد
، و تردد شناورها در خارج از این مسیرها بسیار خطرناک و ممنوع بوده و اخطار می‌دهیم از هرگونه تردد در خارج از مسیر های ابلاغی جدا خودداری نمایید.
🔸
هماهنگی با نیروی دریایی سپاه برای عبور از تنگۀ هرمز از طریق کانال ۱۶ الزامی است و
با شناورهای متخلف برخورد خواهد شد.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/17976" target="_blank">📅 12:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17975">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مسکو با فروپاشی بنزین روبرو شده است.
پهپادهای اوکراینی عملیات بزرگترین پالایشگاه مسکو را مختل کرده‌اند  و این واحد تا سال ۲۰۲۷ تعطیل شده است، - رویترز</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/17975" target="_blank">📅 12:46 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17974">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">به
گزارش وال استریت ژورنال، ایران ۳.۸۴ میلیارد دلار را از طریق صرافی رمزارز CoinEx منتقل کرده تا تحریم‌های آمریکا را دور بزند.</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/17974" target="_blank">📅 08:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17973">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دو سناتور جمهوری خواه با تغییر رأی خود از لایحه محدود کردن اختیارات جنگی ترامپ، باعث شدند که لایحه کاهش اختیارات جنگی ترامپ لغو شود</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/17973" target="_blank">📅 08:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17972">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دو سناتور جمهوری خواه با تغییر رأی خود از لایحه محدود کردن اختیارات جنگی ترامپ، باعث شدند که لایحه کاهش اختیارات جنگی ترامپ لغو شود</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/17972" target="_blank">📅 07:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17971">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ درباره اردوغان :
او دوست من است و از جنگ دوری کرد.
می‌دانید، او کاندیدای اصلی برای ورود به جنگ با ایران بود.
شاید در کنار ایران، چون همانطور که می‌دانید، طرفدار  اسرائیل نیست.
و من از او خواستم لطفاً دور بماند، و او این کار را کرد.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/17971" target="_blank">📅 00:05 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17970">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4506e64b21.mp4?token=EvFSnQbhAckqebKOksC8Cv3Mb5NoqFM-WygFnTnaMxP6-fMv4_Fdwbw0GpqeD6gYGAIb0I6tscVc2oSpKmofF-abj9G81TA9EEEqbVa3xl0bahZ5t4hhOLXXYLZ2cZBXtSrJy-ynymn5Pv7AbRimCkp84PtthFmlyK6H3ur0NDh7g6EAJaPQd9HsuWCXuqBiTECQENv_FIWAmTxWQVrUXoRuz14acF17VjzX6K88vR6YNISLn5SIq8MAc2YfEHp_K3ewWnUxzMcS486n-6fgbOVlaxknrcUghD_ujAzfO3PQtDM-tpNRiI1i4OE4KSndUvOLSyqa6CH4MPp4d5tn5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4506e64b21.mp4?token=EvFSnQbhAckqebKOksC8Cv3Mb5NoqFM-WygFnTnaMxP6-fMv4_Fdwbw0GpqeD6gYGAIb0I6tscVc2oSpKmofF-abj9G81TA9EEEqbVa3xl0bahZ5t4hhOLXXYLZ2cZBXtSrJy-ynymn5Pv7AbRimCkp84PtthFmlyK6H3ur0NDh7g6EAJaPQd9HsuWCXuqBiTECQENv_FIWAmTxWQVrUXoRuz14acF17VjzX6K88vR6YNISLn5SIq8MAc2YfEHp_K3ewWnUxzMcS486n-6fgbOVlaxknrcUghD_ujAzfO3PQtDM-tpNRiI1i4OE4KSndUvOLSyqa6CH4MPp4d5tn5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/17970" target="_blank">📅 00:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17969">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ادعای ترامپ: ایران امتیازات بزرگی می‌دهد  جنگ خیلی خوب پیش می‌رود. همانطور که می‌دانید، ما با اختلاف زیادی در حال پیروزی هستیم.  ایران امتیازات خیلی بزرگی می‌دهد. خواهیم دید چه اتفاقی می‌افتد.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/17969" target="_blank">📅 22:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17968">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ادعای ترامپ: ایران امتیازات بزرگی می‌دهد
جنگ خیلی خوب پیش می‌رود. همانطور که می‌دانید، ما با اختلاف زیادی در حال پیروزی هستیم.
ایران امتیازات خیلی بزرگی می‌دهد. خواهیم دید چه اتفاقی می‌افتد.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/17968" target="_blank">📅 21:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17967">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">#USOIL — W  در تایم هفتگی به کف یک کانال معتبر هفتگی می رسد و از اینجا ریزش بیشتر توجیه بنیادی ندارد.  این یادداشت را هم بخوانید.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/17967" target="_blank">📅 19:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17966">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEMjjVEwFzz6zYKdAJHAn0lgTOraXdqn6miyFMF1T-x0DXCbGhZqFC0fFr7KAxvpqobRDo8LnAQbk29rv6jh4kxxTyZwO-3E3DvROXA313i-W2l6Tfx5_oYOsr-cBRvyFJNdsos9q7EQUw2i4RhLtaiYsSn8c3awR3c8sMkbn0jBWzzmu_IPUDId12-uX10FzXkdNorjz98vplbJgrvVKyBx9p55uxfR-cDrrCSHMSL8-vhHP_690_Wvu-VbLBif4fa_OQUG0OsswljdLbU7AbOt3L8Ybb-V3jY5zTBliXwDtPQsrKo9-1QUz1Dy-6cczkzwLgOTR0Z23vRObPKVCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — W  نفت همه رشدی را که به خاطر جنگ ایران تجربه کرده بود برگشت و اکنون در حال نزدیک شدن به نقطه شروع حرکت است و زین پس دیگر هیچ ریسک پرمیومی برای جنگ در قیمت لحاظ نشده.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/17966" target="_blank">📅 19:29 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17965">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دلار 166 هزار تومان!
بخشی از این رشدها به خاطر کثافت کاری ها و باج هایی است که به طلاداران داده می شود. وقتی اونس سقوط می کند دلار را بالا می برند و بر عکس.
تارگت های 240 و بالاتر همچنان در دسترس هستند البته اما  این رشد دیروز و امروز برای این است که گفته شد.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/17965" target="_blank">📅 19:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17964">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTtgGLI_uqT5lVm12lMiksoCbGDxxnpybbp3JfNAowhkorZYLH_SbAwMZky3mCr_vpu0Py7KXZB0zmycKGYotqLs1spvDwLKN6mFhrZryp5nKtUmwqPbG5v4sC7h3nLZqet95NZQUPaAWD1-En3GTa_SosAkweea0Py6x7Ced39yUx6xSsK2qyDBKnweI4Zc_THwGyJfWPdOWs2s3aVqs7LJz3W8NP4gEQsGv5LgTNzjtXdQbYySKZwu_o-PS9T6TC3KWGDjH0b_I5fn8XnOVrvZ-ieo7_ErYQTPKoKjtZv1BTv4fRQcuU8fESSy8KnHJJH8drvX1yb8blzpasD33Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H2  در محدوده مشخص شده می شود به دنبال موقعیتهای خرید باشیم.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/17964" target="_blank">📅 19:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17963">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">رئیس‌جمهور ایران مسعود پزشکیان رسماً نخست‌وزیر نارندرا مودی را به شرکت در مراسم تشییع و تدفین چندروزه رهبر عالی‌رتبه آیت‌الله علی خامنه‌ای در ایران دعوت کرده است.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/17963" target="_blank">📅 16:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17962">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">رئیس‌جمهور ایران مسعود پزشکیان رسماً نخست‌وزیر نارندرا مودی را به شرکت در مراسم تشییع و تدفین چندروزه رهبر عالی‌رتبه آیت‌الله علی خامنه‌ای در ایران دعوت کرده است.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/17962" target="_blank">📅 16:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17961">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">رویترز:   سپاه پاسداران انقلاب اسلامی سلول‌های مخفی در عراق ایجاد کرده تا حملات پهپادی علیه کویت، عربستان سعودی و امارات متحده عربی انجام دهد. این سلول‌ها از جنگجویان شیعه نخبه عراقی تشکیل شده‌اند و مستقیماً به سپاه پاسداران گزارش می‌دهند؛ بین آوریل و مه حداقل…</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/17961" target="_blank">📅 16:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17960">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حقیقتا «الکسیس میانرودان» لقب شایسته ای برای عراق نیست؟!  تل آویو - اسرائیل برای پشتیبانی از عملیات هوایی خود علیه ایران، یک پایگاه نظامی مخفی در صحرای عراق ایجاد کرد و حملات هوایی علیه نیروهای عراقی انجام داد که تقریباً در اوایل جنگ آن را کشف کردند.  به گفته…</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17960" target="_blank">📅 16:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17959">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNPdIS6nM6gl-UsP9PVryQap8URK984un-EmImQvFiULOAcbeyuwT8pe54UrE08gqxkMK5tLUfA9AzbFMTMXa_t71O9wnc_EoSQKx61fRMdCC0uRV6oXKa4eOB_gx-BkwBRU3AkRteYngY_pKg_B_tQ3V-6plkUDYkZ7HyIX_S7FUtygEr77t14rJ8jw5PnSqHGAiqxU8P4Gf6qUlC0FjzZIs78BhxzyI0QZeLjk9O7yniKPJ_CwNeujpa6wxcKsNq3ov0OrhKZLwHnK7PldwsPaMYT5lYosstVcgG1wPDdg1zR55U5pVo4KVFYU1k16XcPkBvwrDzITHG5pOrIUfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#DXY — W  پس از یک سال رنج زدن، شاخص دلار به صورت کوبنده ای رهسپار تارگت های اعلامی شده.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/17959" target="_blank">📅 16:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17958">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKpvB-Hhsrn68OlEuZyW1Uz__DZ9ZVLtZWxgAAqHOxy1jCw65SJQHn5D5A74mCpaswSwCYD8N4gxx-0epHrT6asOMsr92LAQEkbe9KAStv7SQuAybNou_pEIvE1wsQ2pHHJsXHrA7BDQl3q3lIN8YLmhFv-jie8n-vHvdH2iW6xFU74MjvevxR03oKFNDMsk6JDEe2uRa4F0lFqdgl7MUfNKCEKGKeu2ZO-PX1kt-ToPBMvbulA-QqggOS-q_m_oioGl7NIkVGN1knmJJBzyy11X7PJiXG4Eec5inTpaDD03eliFmmxQoB1vpzPJaYrnE90_zZrP0goQ1WvlMYqiOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#DXY — W  رسید به کف کانال هفتگی!  از این هفته فروش دلار که ممنوع است هیچی، خرید هم در دستور کار قرار می گیرد.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17958" target="_blank">📅 16:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17957">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ: ۵۰۰ میلیون دلار در ابتدا برای خرید کالاهای آمریکایی به ایران داده می شود</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/17957" target="_blank">📅 15:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17956">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/925922fd6b.mp4?token=I4EJPs0ACNTdrkWEzSlF9NGvpocYmhl_9Xey3X2jalppVH44Oxhr-7a8Orfb-kYZILziUR1VIJgXsT7OOeoYPgaREclVUN38VcCAAVkNxeIq7Ey_oC7NzqtP7tABWEyZbmpaG2_29bEOeot00jb6reFQQt4nVoA6nXP-mcm2-MTKR_ALskjKin82DD0v3OD-HZHmahu1nkSm4wvf6t9l7bt-F1Mn_TfIVu3pX_qchLoJp7ZMzjtWScsnAbS6F8HlQ88-qNmiPrIa2If2oIlOLN-DGz1iFXYGn44B2N6UBAU-JmnAJ1gCy2y5P6P4UbO9EQhcM0KQz2fNJ8_YoKi33Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/925922fd6b.mp4?token=I4EJPs0ACNTdrkWEzSlF9NGvpocYmhl_9Xey3X2jalppVH44Oxhr-7a8Orfb-kYZILziUR1VIJgXsT7OOeoYPgaREclVUN38VcCAAVkNxeIq7Ey_oC7NzqtP7tABWEyZbmpaG2_29bEOeot00jb6reFQQt4nVoA6nXP-mcm2-MTKR_ALskjKin82DD0v3OD-HZHmahu1nkSm4wvf6t9l7bt-F1Mn_TfIVu3pX_qchLoJp7ZMzjtWScsnAbS6F8HlQ88-qNmiPrIa2If2oIlOLN-DGz1iFXYGn44B2N6UBAU-JmnAJ1gCy2y5P6P4UbO9EQhcM0KQz2fNJ8_YoKi33Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خارجی ها مخ شان سوت کشیده و فکر می‌کنند بیرانوند راننده یک تراکتور است!  سبحان الله!</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/17956" target="_blank">📅 14:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17955">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">یسرائیل کاتس، وزیر دفاع اسرائیل:
«حتی اگر از سوی آمریکا درخواستی مطرح شود، ما از لبنان عقب‌نشینی نخواهیم کرد.
دویست هزار نفر از ساکنان [شمال اسرائیل] هنوز به خانه‌های خود بازنگشته‌اند.
ما تمام رهبری حوثی‌ها را از بین برده‌ایم، به‌جز عبدالملک الحوثی که در تونل‌ها مخفی شده است.
اگر او در تیررس قرار بگیرد، کشته خواهد شد.»</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/17955" target="_blank">📅 14:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17954">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIjsK2l10tr-fe2nbF7mHXq1fDgEA8-2SN3sZ6YOYRLx0fa-vVa7Ij__iBN73XaZQCiuaYi6JvM-axUAqpcKJ-ZGI9i3QEtE_yvCDVeuaF1Zsos8cA-HdDu4Sl1pWJjmTZkfncirHzRJUl1XK6TqPbwdgbqgfP6VDdD5kBYf9Edz3jXtH9Ix_VJp5sJL5lLsCgR4gpjpd4U3emG4M8MEZCYiDs6cdH2YQr15X53bHG5JnVtfZcVoBhaEgPFKgNjEdW8GFnHIkiRrym-NeCTXIfF-oKkLDjxJoGPBvY9_-0qNEGjJQhpi2g4PWmxby4PozmFxyNJPr0NNRFRvEj-jfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/17954" target="_blank">📅 14:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17953">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdphL6pxLXY74UU7qp3OrlOgseBa6SiTgjfSfAUyv2J6vGKpeOsOQ6OE-2F49YFf_W231ba6urjDWlf9kjE2UAMvjkvgPydBd1-HEYHp-G6E111PGDXoXjmaIe3ntoYwk2M-Be-PW8BMXkaDnZBNJjGASmlTzdJ02CoPKqJqu9gOa-DrfnTz4JDNx5dE8jRIp6JOqCkO5sYVLQXfRrOgzl_jfhJtAp6ZdDy7PkzhBS8oSk_BsnHwJMlmtLb5SVvYY_Wd79CmDpnPLjL9_9iZCKhX-TakOjt6yKrvtLoHh0ZN1O3eAXDt2X16wOnTX1W89S0vtXj6CxkvrtU7-FRQzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#طلا
بر اساس نمودار، احتمال ثبت یک کف دیگر پیش از پرواز دوباره قیمت بالا است.
بهترین محدوده خرید میان مدت 14.2 میلیون تا 14.9 میلیون است و تارگت حداقلی 29 میلیون تومانی فعال خواهدشد.</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/17953" target="_blank">📅 12:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17952">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">هاآرتص، با استناد به منابعی در ارتش اسرائیل:  ناامیدی و احساس ناتوانی در میان افسران در لبنان به دلیل عدم قطعیت ایجاد شده توسط اقدامات نتانیاهو و کاتز.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/17952" target="_blank">📅 12:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17951">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">برخلاف تصور رایج، «لابی کشاورزی آمریکا» یکی از قدرتمندترین ائتلاف‌های ذی‌نفع در واشنگتن است. اما این لابی یک سازمان واحد نیست، بلکه شبکه‌ای از انجمن‌های کشاورزان، اتحادیه‌های تولیدکنندگان غلات و شرکت‌های بزرگ کشاورزی است.  نکته جالب اینجاست که این لابی، برخلاف…</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/17951" target="_blank">📅 10:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17950">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">توییت ترامپ در مورد ایران:  با وجود اعتراضات و اظهارات نادرست آنها، همراه با تبلیغات مکرر اخبار جعلی که همه تلاش خود را می‌کند تا پیروزی آمریکا را کوچک و بی‌اهمیت جلوه دهد، ایران به طور کامل و جامع با بازرسی‌های هسته‌ای در بالاترین سطح برای آینده‌ای نامحدود…</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/17950" target="_blank">📅 10:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17949">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">هاآرتص، با استناد به منابعی در ارتش اسرائیل:
ناامیدی و احساس ناتوانی در میان افسران در لبنان به دلیل عدم قطعیت ایجاد شده توسط اقدامات نتانیاهو و کاتز.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17949" target="_blank">📅 09:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17948">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتحلیل و رصد</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a0802e26a.mp4?token=TIYfdQCbLVJcm59VAovwXRYIG-oQOo3Xmc0RLePpKTl8RrxAyWVLJPoqS4ErUxcOmaRsM1irw-LahO9Kc6jXJqt9waaJV6RONQGoIiLN2M-3I-6JS2LHmFgjTnh4F0zB45kei9Rw9ZSqfrEaW523E77O-6uWU29lPUEnN2rnN0OWDHJ0v-7AMEwnG3sX81Z8-gMNkS8bl6Dn94LMkWhm-S0EaQDxKIJ_ecug2yIXmjmuuD4tZJMpLl_CJEY-1QLJH8vdd3Gyh5iMdJNMEFd1Vur4obh6ajaztCBKa1mbSYpnS3bMwVhNiqVUb3Lz99zIGyPQLT_Lo9WlAIDsYaMH-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a0802e26a.mp4?token=TIYfdQCbLVJcm59VAovwXRYIG-oQOo3Xmc0RLePpKTl8RrxAyWVLJPoqS4ErUxcOmaRsM1irw-LahO9Kc6jXJqt9waaJV6RONQGoIiLN2M-3I-6JS2LHmFgjTnh4F0zB45kei9Rw9ZSqfrEaW523E77O-6uWU29lPUEnN2rnN0OWDHJ0v-7AMEwnG3sX81Z8-gMNkS8bl6Dn94LMkWhm-S0EaQDxKIJ_ecug2yIXmjmuuD4tZJMpLl_CJEY-1QLJH8vdd3Gyh5iMdJNMEFd1Vur4obh6ajaztCBKa1mbSYpnS3bMwVhNiqVUb3Lz99zIGyPQLT_Lo9WlAIDsYaMH-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">.
🟢
وقتی دکتر مسعود، نمی‌تونه از کاراکتر دوره جَوونی‌ش فاصله بگیره!
پزشکیان [در سفرش به پاکستان] به نشان دوستی یک درخت تو اسلام‌آباد کاشت که رسم پاکستانی هاست.
ولی نکته جالب اینه که هی شهباز شریف نخست وزیر پاکستان اشاره میکنه مسعود جان بسه کم خاک بریز. نمادینه ولش کن. ولی مسعود هیچ رَقمه گوشش بدهکار نیست و فقط بیل میزنه.
@tahlilvarasad</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/17948" target="_blank">📅 09:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17946">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">⛔️
کارشناس اسراییلی تشریح کرد: ۸ کانون تنش بین ترکیه و اسراییل؛ ترکیه ایران جدید است  یک کارشناس اسراییلی با اشاره به اینکه تنش بین ترکیه و اسراییل به بالاترین حد خود رسیده است، به بررسی ۸ کانون تنش بین طرفین پرداخت.  ایتان لاسری بر این باور است که اسراییل…</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/17946" target="_blank">📅 23:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17945">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">نخست‌وزیر پاکستان، شهباز شریف:
«کشورهایی هستند که می‌خواهند توافق را مختل کنند، و من می‌گویم که بدون ایران نمی‌توانند موشک‌های بالستیک داشته باشند. استانداردهای دوگانه قابل قبول نیست و منطقی نیست که برخی موشک‌های بالستیک داشته باشند در حالی که ایران از آن منع شده است.
یادداشت تفاهم (MoU) به مسئله موشک‌های بالستیک ایرانی اشاره نکرده است».
«این یادداشت تفاهم به موشک‌های بالستیک اشاره نمی‌کند. هرگز روی میز نبود؛ هرگز در دستور کار نبود.
طرف ایرانی هرگز نخواست حتی درباره آن بحث کند».</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/17945" target="_blank">📅 20:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17944">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🟢
پاسخ به توهم برخی درباره شکست احتمالی نتانیاهو</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/17944" target="_blank">📅 15:57 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
