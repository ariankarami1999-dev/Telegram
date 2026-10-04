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
<img src="https://cdn4.telesco.pe/file/O9LKj1Nmkh2fkDLMfdNxOlU_C0KkNVDgd85j-_4C_s2nLcreJANANuxd_vx-_kEb9vSA0_j4KocvTmmZJnHEB7SCxpycY_CfEFy6dtpgvcXpegT5HdnMSapQDvXVxKxa3jvqVaN0yQsrjOvalTilxbYCBMeHY7vuZLSl6iHlo9Nuo8c9-3mxTZEKetnU2I59psxegz4931VMLAHmMx-MfRy77CUNhmzy_rhmw-RNP_aW19tSVXxd9xMn57uak-uyIcr270EgNFElnIvKZ4UsP7QRdWHFdSjnSUuIX6lNIf77EySW1gJkChw6BxlM9j2_0u7u_hOwK49hIx2jWsoGaA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.31M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 03:45:05</div>
<hr>

<div class="tg-post" id="msg-695347">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگروه آموزشی و مشاوره‌ای آسمان</strong></div>
<div class="tg-text">📌
رتبه ۶ کشوری کنکور تجربی
به‌نظرتون امیرعلی اگه برگرده اول سال،
چیو عوض می‌کنه
🧐
⁉️
1️⃣
قسمت اول، مصاحبه با:
👤
امیرعلی راوندی
✍🏻
پایه دوازدهم رشته علوم تجربی
🏢
دبیرستان علامه حلی۱۰
📆
تاریخ مصاحبه: ۱۰ تیر ۱۴۰۵
+دیدن این ویدیو رو از دست ندین
😎
🔥
✈️
@aseman_org
✈️
@aseman_moshavereh</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/695347" target="_blank">📅 00:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695346">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyrmpbEn1XyCInrr7RGILTPAhMu1wFmRgJoia5OHH6sW8oKXKrxWAXbLb_d59rE5J4_iHoBvnUa8DdOQDieeHUUYRvYkd6VeetXBw3zHb3wc1VtAyJd_leN6hRO4GRXmxdatpUgIOcSwWGVpsQR_cHyQGD3nrd18HYy9ccIR9HTpghPTWIB1P7XsZtexieAGf8GYfmSncCvn7HEOugH0I5okUoHFHaxRd-QCfP0PZXQBL8xvVHZJM9K9ykjGO3gaNdnzV9W1Dx24JtE-qe7yDvsHZqeEs4jZI3f7kCHUYcQMH6c3DK5CHuIqYiutiTxe6d5FarnmU-Bc58T9oLRB7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚗
🧹
جارو شارژی خودرو با مکش ۴۵۰۰Pa
🔥
این جارو رو می‌خوای؟ قسطی هم می‌تونی بخری!
سبک، کم‌حجم و شارژی با ۲۰–۲۵ دقیقه کارکرد!
⚡️
اندازه جعبه : 16*16*6 سانتی متر
مکش نیرو:۴۰۰۰ - ۴۵۰۰Pa
ویژگی های خاص:قابلیت استفاده به صورت خشک در خانه و ظرفیت باتری ۲۰۰۰ میلی آمپری
🔥
قیمت نقدی ویژه امروز: 1,389,000 تومان
🏠
پرداخت درب منزل
✅
امکان پرداخت  در 4 قسط 400 هزار تومنی
💳
خرید قسطی در ۴ قسط، بدون چک، ضامن و سفته
🛒
خرید
👇
memarket24.ir/product/fast/26903/180124/</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/695346" target="_blank">📅 00:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695345">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8000901fc1.mp4?token=lHDmiyrMChBF9E2N710eTMcG3geZdxGlERiObg4XawWd-Cju5IJ_JpTRkUvtv1rtswe4P0hN1yLePxYk6dGS0EckAPyG76YAG1qdmZx1-AI1EdtZyYQ-nx5AE-dbhtsLbBrHuVjnesdCDin1cPv9NRG6Oi8TNdeS0cTIaQ5ZXbuOpUtkE8VE8EH7l1ClZVTPUTtCD0MUAj9RB5DoYAEZyzNWson571bI9jn8YGG4dx-j32TDndK55ZgT3H9UI-WhbTBmafVPepaAS0_oO1nGQxsaaMuey3AgXL7qm_ts1oX93KJuk92Jl4OPw1gaUyZYU4Sng_xv7rFQPzdJ6fPipw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8000901fc1.mp4?token=lHDmiyrMChBF9E2N710eTMcG3geZdxGlERiObg4XawWd-Cju5IJ_JpTRkUvtv1rtswe4P0hN1yLePxYk6dGS0EckAPyG76YAG1qdmZx1-AI1EdtZyYQ-nx5AE-dbhtsLbBrHuVjnesdCDin1cPv9NRG6Oi8TNdeS0cTIaQ5ZXbuOpUtkE8VE8EH7l1ClZVTPUTtCD0MUAj9RB5DoYAEZyzNWson571bI9jn8YGG4dx-j32TDndK55ZgT3H9UI-WhbTBmafVPepaAS0_oO1nGQxsaaMuey3AgXL7qm_ts1oX93KJuk92Jl4OPw1gaUyZYU4Sng_xv7rFQPzdJ6fPipw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گسترش شدید آتش‌سوزی در پالایشگاه آرامکو در ریاض
🔹
تصاویر ماهواره‌ای نشان می‌دهد که شدت حرارت در ساعت ۱۹:۱۰ به ۲۰۵ مگاوات رسیده است، در حالی که در ساعت پیش از آن این میزان بین ۸ تا ۷۴ مگاوات بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/695345" target="_blank">📅 00:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695344">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRU4Iuf0IrNMAfb3xy00ZeWrBzDbdqzS5FlpDakE1AFfns6lmhNKR0sD4cRGh6pJ3Jvxl-KqGVy7btlOQxre_g5yNbLSn17c67l9gnhMJV5Okr9PlRKVNUDsoQLl56bQ4Cfd9k55zRAq6ydQRFNI8dpPTgN2xSW4mBCPTPg3eVLb4C0ieLATj796ReyVu4FY_JSnt0Bw8iXJFPIoNvD2nKwfUEnNPgEqYOUXrA7QvbwViKRhwHxZFtAwwRMYSyXaj1yUdz2W6Vukq8qRGxodNcsFc3yv0tHKtnSapOLkkDsDZALen37VCW3E0Th5EPxLAeK4XvZS_7t_5HyMLAi99A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۹
ترکیب شگفت‌انگیز خرما برای سلامتی بیشتر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/695344" target="_blank">📅 00:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695343">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IwxY9UlURpBbXC8T47JexTKUWbeXhA7TF_JsqlgldxE2jG3R8Vq4DjwEbD7BDvtbsu5Ubups47qrGqIIRqK3-XraokGYCeHEYori6D3sdbnJK6p7cUSd1_JjJ-P5WgFdR5-nK_gUjUQNcowrrom7H12jQFhUx5slANjsJUWhBGEcWa5RV_1Px2LjR4RBFgJB_yNls2GPKl8Wynr4AGwUwePHqPz8__GLPiLRBC3McDN9f13xnIMu9riJ0QKkezu-_1Qqn9ja0tDXGIEsqPzU4uNItxVvJuNKzuRKPQD8lVmSn8OvvWR3TqOnbexFkbQptua5qA0Kz60tNBcLc3HLhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاییز؛ دریاچه چورت ساری
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/695343" target="_blank">📅 00:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695342">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKjTIMmy0QcNjJ40r191s5u4PXH4ZFxDjGZAafQVUWoKgoq_y1odQtd5uKRdSyNxlyvwlCV-FhjYqRfNEX8Vz7aMf2RZj8PDxv8EnusgRJltQiqDKPTDIOTwVuniEkQ0ksiFN8AfMYR3hBKQj1NMyaXomjQbsOq1eEpEKhJSROH6iwtxbCDx9N1Hjc9Pgn-jaaVjH0GzdBg3I0dvUxj-n8Uq5S5iz2UAK5mNvshujtWt8Vgb38F3q6n76QFe0tdazcKXjzLNJfTHwhYMQa2PG_1biKOdXBAMhcThAOKj9bZTKfZhZVajkwLH3bKbD9xYclI2Wy531F0fwO_BzRXdzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/akhbarefori/695342" target="_blank">📅 00:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695341">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
در لابلای خبرها، داغ‌ترین‌ها را از دست ندهید
🔹
🔹
آماده‌باش پنتاگون برای اعزام ۲۰ هزار نیروی آمریکایی به خاورمیانه؛ ۳ ناو هواپیمابر در راه منطقه
👇
khabarfoori.com/fa/tiny/news-3249575
🔹
جزئیات جلسه محرمانه کمپ‌دیوید درباره ایران | افزایش پرواز سوخت‌رسان‌ها؛ زمان حمله معلوم شد؟
👇
khabarfoori.com/fa/tiny/news-3249675
🔹
روند افزایش قیمت دلار و طلا تا کجا ادامه دارد؟ | شما نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3249618
🔹
جزئیات طرح ادعایی لاریجانی و خرازی برای پایان جنگ | پوتین از چه نقشی برای لاریجانی سخن گفت؟
👇
khabarfoori.com/fa/tiny/news-3249574
🔹
سهمیه‌بندی جدید در راه است؟ | رمزگشایی از «توکن بنزین» | سامانه سوخت در مسیر جمع‌آوری داده برای سهمیه‌بندی جدید
👇
khabarfoori.com/fa/tiny/news-3249614
♦️
خبرهای جذاب امروز را در لینک زیر دنبال کنید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/695341" target="_blank">📅 23:59 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695340">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
باهوش‌ترین درخت دنیا رو می‌شناسین!؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/695340" target="_blank">📅 23:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695339">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4109444e1.mp4?token=sr9nTcNjfJKEkYkdBBLdKYmAppFYANx8yI8GzejzAdcmqOvCHneHk6HjzQry99QaFI6eK67sjgMmfn8Qr3ecE2UecdhmgIiU5kfNcX_dimvb7SL1ZFCIJeZfFAciYhlN9mKUuDaDnUKyU1gmlMrHeqXPrlADq_ESicadB2tUFS4_b8aI8rIWUM8VkJctnFPz8Z-JDowkDn7KfAzKH7H4Z_fAhtQXUhjrLYl8CNqlNH_h3kXU-gfQVfo_XV3KTLzPjPkDAz7RhCJ-71Kw5nG1ldE6tBLtB4aKu-w0RX4akvOa_CtiucAwZguGZ_LoNVBfSum39S52Jj-RotDOaip1wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4109444e1.mp4?token=sr9nTcNjfJKEkYkdBBLdKYmAppFYANx8yI8GzejzAdcmqOvCHneHk6HjzQry99QaFI6eK67sjgMmfn8Qr3ecE2UecdhmgIiU5kfNcX_dimvb7SL1ZFCIJeZfFAciYhlN9mKUuDaDnUKyU1gmlMrHeqXPrlADq_ESicadB2tUFS4_b8aI8rIWUM8VkJctnFPz8Z-JDowkDn7KfAzKH7H4Z_fAhtQXUhjrLYl8CNqlNH_h3kXU-gfQVfo_XV3KTLzPjPkDAz7RhCJ-71Kw5nG1ldE6tBLtB4aKu-w0RX4akvOa_CtiucAwZguGZ_LoNVBfSum39S52Jj-RotDOaip1wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلم دیگری از سیل امروز عظیمیه (بام) کرج
#اخبار_البرز
در فضای مجازی
👇
@akhbare_Alborz</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/695339" target="_blank">📅 23:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695338">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
ادعای نیویورک تایمز درباره حمله به پایگاه فیرفورد با حمایت ایران
🔹
به فرماندهان نظامی درباره حمله‌ای با حمایت ایران به پایگاه فیرفورد در انگلیس هشدار داده شده بود. طرح حمله به پایگاه فیرفورد پس از رهگیری ارتباطات و سایر اطلاعات فاش شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/695338" target="_blank">📅 23:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695337">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1391f0eb1.mp4?token=KTEtqaFGwWCz_RSXhoeWhSliHiRDrCMtHnXrnz2M0ZThvsiyzSCSNeTFyA3MRFHrJK3RFvy-9pDLws0hJYTSkgc6uatznxrQCBeS50DS4MtFBah13hUwjwzadX30ybkwTQCC_QYmmqMBTnPFfvYJ3dXaCrrC-EN4oqrrfF9YJLpGSOcp3556WKv3zPnYhASt4vlZ8PROv9K5puz6PWOl6K0UvY90C3v3Gh07UQ6YN4J8CAmlFFEuZCM-P1hqOge2-ARLD9h1J6TYdbs4mW03tIsEHA_jtz8TUzPse858HzpXxcXAdqy1rw7T6pdC89CEIpkOdRNuJXS1q5eQnXJZpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1391f0eb1.mp4?token=KTEtqaFGwWCz_RSXhoeWhSliHiRDrCMtHnXrnz2M0ZThvsiyzSCSNeTFyA3MRFHrJK3RFvy-9pDLws0hJYTSkgc6uatznxrQCBeS50DS4MtFBah13hUwjwzadX30ybkwTQCC_QYmmqMBTnPFfvYJ3dXaCrrC-EN4oqrrfF9YJLpGSOcp3556WKv3zPnYhASt4vlZ8PROv9K5puz6PWOl6K0UvY90C3v3Gh07UQ6YN4J8CAmlFFEuZCM-P1hqOge2-ARLD9h1J6TYdbs4mW03tIsEHA_jtz8TUzPse858HzpXxcXAdqy1rw7T6pdC89CEIpkOdRNuJXS1q5eQnXJZpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت عجیب امروز در دریاچه چیتگر
🔹
وقتی هشدارهای هواشناسی رو جدی نمی‌گیریم
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/695337" target="_blank">📅 23:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695336">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e255cac876.mp4?token=cJdlHg2dTaNVtIdcodxtfIXosIhhfuKHBmDIXjknJxX09kvq4_xtibnuTWrL-5EhkLCcyCwnhzFFOYvTv5Ed7Eab8FwSFY_T8vxUdJ56WJbQuawhZQ53tqGj7yUSRgT0nQGGOzSIdK1Gn3bzDDK4RYks51Mjb3cdler5uHD6KSo8MM7HdpCg6WeMWU_gX3C8i6leFQ-1KK5ABlQlwJbRegT2eLuR_kw2ueWrXe5bjFrJ_hAq3mfMnX3NEanY8ePrt0nPvO0QQontKyiEAwEU9nZ_JzS2F_brro2Y8tGwwwVFsTh4lnusKa3Wvc1PEsLARwAi5hJ91A59V9IIuu0UBYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e255cac876.mp4?token=cJdlHg2dTaNVtIdcodxtfIXosIhhfuKHBmDIXjknJxX09kvq4_xtibnuTWrL-5EhkLCcyCwnhzFFOYvTv5Ed7Eab8FwSFY_T8vxUdJ56WJbQuawhZQ53tqGj7yUSRgT0nQGGOzSIdK1Gn3bzDDK4RYks51Mjb3cdler5uHD6KSo8MM7HdpCg6WeMWU_gX3C8i6leFQ-1KK5ABlQlwJbRegT2eLuR_kw2ueWrXe5bjFrJ_hAq3mfMnX3NEanY8ePrt0nPvO0QQontKyiEAwEU9nZ_JzS2F_brro2Y8tGwwwVFsTh4lnusKa3Wvc1PEsLARwAi5hJ91A59V9IIuu0UBYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار نخستین بار | لحظاتی از حضور شهید سیدهاشم صفی‌الدین در کنار شهید سیدحسن نصرالله
🔹
به مناسبت سالگرد شهادت مجاهد شهید سیدهاشم صفی‌الدین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/695336" target="_blank">📅 23:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695335">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3a2ab2d10.mp4?token=U_xV8zK7GJXAp5mLeH3MnLdhikaGv2TNanrgE0NlD1Ux8eioGVW9qF2F2E_D7Ym-3MDpFfsxgnMIA2GyaI7KVevCH5FWuBpxvX8GqaqO4nzyw-dk_LTtDOc301ZnV-F0ckHjwlapk_nW0LGFmhYMW1v-K_rUi0i8_EopYjAEsQIU82rNgFqv1WIO8GRNVeEDJ9ONE503tXsNHX06onMBiIGU5sLdSHcFXnUpZMrlurFHL9I6jIo2KbS_Bwzi202gJ015Lf3goZ_VDG8rWQ6bd2JYjzns-x8xm1N2fdE6NBMcL4CfASDanwPirpHIEuyGfKBeSgsWnuHYOxFtAkbSoDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3a2ab2d10.mp4?token=U_xV8zK7GJXAp5mLeH3MnLdhikaGv2TNanrgE0NlD1Ux8eioGVW9qF2F2E_D7Ym-3MDpFfsxgnMIA2GyaI7KVevCH5FWuBpxvX8GqaqO4nzyw-dk_LTtDOc301ZnV-F0ckHjwlapk_nW0LGFmhYMW1v-K_rUi0i8_EopYjAEsQIU82rNgFqv1WIO8GRNVeEDJ9ONE503tXsNHX06onMBiIGU5sLdSHcFXnUpZMrlurFHL9I6jIo2KbS_Bwzi202gJ015Lf3goZ_VDG8rWQ6bd2JYjzns-x8xm1N2fdE6NBMcL4CfASDanwPirpHIEuyGfKBeSgsWnuHYOxFtAkbSoDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«لوازم تحریر» یا «لوازم تحقیر»؛ وقتی خرید دو تا دفتر بادیگارد می‌خواهد!
/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/695335" target="_blank">📅 23:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695334">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ci-TX_HWAFkV4pMeP61KuKXy88qBWALJIBwdvvIYbLFeMho-6iwQFfZNtfNK6gUPHFS0-PUs0tVqdwAhOx-SdNeZM5i9rPya8KR9XO0SqXRs8nsmHiKAVXA6oCgJn60dzbGCZNSriYJbNerg8HeI-e6DsGxsZfnS3dHk5mv8BjhhXx0GGechFWluQUmRTxOM5JA4h6Zqtv4wy7as0fJMHuQa-_i3YXMUX68XMYrCgF3v4q8U4AYLZlY_csfL3aI-noCgDndz2LyLB499qASU05t_0qfRxiV_HRrdIiJxEzb8aE41Vu9ZdjuwHCvXJ_cE8xY2WwPeCw2jDAYLP_j3_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعرفه ارتباطی در ایران ۸۷ برابر ارزان‌تر از منطقه
🔹
بررسی‌های رویداد۲۴ در خصوص قیمت خدمات ارتباطات سیار در کشورهای منطقه نشان می‌دهد هزینه یک دقیقه مکالمه در کشورهای دیگر، ده‌ها برابر گران‌تر از ایران است.
🔹
این در حالی است که بخش قابل‌توجهی از هزینه اپراتورها برای توسعه و نگهداری شبکه و تامین تجهیزات، بصورت ارزی است.
🔹
توسعه فناوری‌هایی مانند 5G و حفظ کیفیت شبکه، به مدل درآمدی متناسب با هزینه‌های توسعه نیاز دارد.
گزارش کامل را اینجا بخوانید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/695334" target="_blank">📅 23:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695333">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U14ZHlLgPRlpzLsA808qqOrMwKfJvMOEJ3V0uesB2h1zEbDV6bjP1YzOsj0Mi8cAbz6bwrZe9R4f180qHVZZ5cNGMoo4Z1mMeG3pWGyye6VWF9AEM-eFv-rZYQF6Z6XRtdzEnlNhsFzRu2VetGCAssXvUM4EkMjtZYHyqCpR0JD6F23oPrMKSlUV6T02abFx6fV1kwBX-Qyy5Fxj2AxUUxZuva1mf7juxHuveA_HeoV7D6Y3vdgO306RaKzENlLasRoAzbtZunDsGUCfFUelahpqLS044HTMBd_MeAVFCWYduqxX7OYAx82m9EBE65q8C_NqkaOpdh7MIxrPXwd6Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همه‌ چیز درباره نبرد سرنوشت‌ساز/ تعز؛ کلید فتح یمن/ انصارالله عربستان را کیش و مات می‌کند؟
🔹
اهمیت تعز پیش از هر چیز در موقعیت جغرافیایی آن نهفته است. این استان میان مناطق تحت کنترل صنعاء در شمال و مناطق تحت کنترل نیروهای تحت حمایت عربستان در عدن در جنوب قرار گرفته و به‌عنوان یکی از مهم‌ترین گره‌های ارتباطی یمن شناخته می‌شود.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3249718</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/695333" target="_blank">📅 23:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695332">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
هگزث: ایران در حال بازسازی توان موشکی خود است  پیت هگزث، وزیر جنگ آمریکا:
🔹
ایران تلاش خواهد کرد تا قابلیت‌های موشکی و پرتابگرهای خود را بازسازی کند. آن‌ها یک کشور تروریستی هستند، بنابراین همیشه تلاش خواهند کرد تا قابلیت‌های خود را بازسازی کنند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/695332" target="_blank">📅 23:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695331">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
عضو کمیسیون امنیت ملی: برای تأمین دارو منتظر رفع تحریم‌ها نمانید
امیر حیات مقدم، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
موضوع تأمین دارو، در صحبت‌های اخیر ایران و آمریکا مطرح نشده و صحبت‌های منتقل شده از سوی میانجی‌ها در حد کلیات بوده و وارد جزئیات موضوعاتی مانند دارو نشده است.
🔹
در شرایط فعلی توافق یا تفاهمی برای رفع تحریم‌ها وجود ندارد و بنابراین وزارت بهداشت و بانک مرکزی باید برای تأمین داروی مورد نیاز بیماران به‌ویژه بیماران خاص، از مسیرهای دیگر راهکار پیدا کنند و منتظر رفع تحریم‌ها نمانند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/695331" target="_blank">📅 23:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695330">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTbR_h1cI_IyULIIrvnaqDlf4sPy0OtK7c47heLN2QFnoIyeFr9jYaLPosU3uhZbko7hrUAPyIE5H-mKsB1BkSehq31Hg01hknOLBtZBPxQuGda5mHopkdxpAgPVyiAXaPzVTEmOYo1f6nXYmGcYjSrqBqeMn0q_XQVCMWFxzPoUybZf8DAFWXVmte6jZuGFgO3nkAeYRSV4jBi5DF_IdZ50FiQ6yojIxf0bcp91NPYUMSk1sXiUZ27UkThbhlDjgmUAsw-Eqt6j9C552_ZGz7m7MidmedyJmi8Iu6nsV0nVdD0q3-7Da89soBoSk61McltFCB5zyzBdYmf03zAWsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیه وزرات خارجه درباره خروج نیروهای اشغالگر آمریکایی از عراق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/695330" target="_blank">📅 23:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695329">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pejYDxMMgr3ZPnmwuoPGuysaVUlD47vQB6H1ZW50f39tPAWzaKTr_NTG_j9BB7qKSQzRi53DUlV409S_dIE-Fms8i9K614usZt0rmSHOORTOvJx9i1Gjf5ej0xnIZCFE9b6I1GtPZrav13uj2QfzVe217-tkYdfaz83tFfsHorCIwfOtOnOIZXb2fTXN3W06IyAnMjyeQZjsYAQt6gxftKCpbdVglFvvB2pbZ-VElt0QVj9yXBcWEVn5CcMGMkudOxBNbuUBuJv1NfoEpPOn-50JYN9xAFaPXBwmstGVliMur2WWyzVSULdBmBfdChDlxw7tYuD8hz0lCOPQvR7-pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
موج النینو زودتر از موعد هر سال، به ایران رسید
🔹
تصاویر ماهواره‌ای از هفته‌ای پربارش در غرب کشور خبر می‌دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/695329" target="_blank">📅 23:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695328">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
ادعای آکسیوس:
دو دیپلمات ایرانی، پس از آنکه دستورات مکرر وزارت خارجه برای ترک این کشور پس از مجمع عمومی سازمان ملل را نادیده گرفتند از آمریکا اخراج شدند، یکی از آنها شب جمعه و دیگری صبح شنبه نیویورک را ترک کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/695328" target="_blank">📅 23:23 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695327">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61ccebe799.mp4?token=Sw-lqw5qK9BAoutOmjGC85qfBqmT5WIB39dsfsenEdp3cOD_s24RKu52WB-Drj0I8m6g8UpdML0u66j3t1lXqWNiFti-XMzmFZ-3MPButjbwyUZDhUQzWMtzULBSbhFmYoCxufFmiX8sKlElhZ7mWuCTBdajjtZlJcIW2gS9aikOCK2aG8vqQZFBPSZ7v85JXUw0VTb-Qf8kpJEuB8Hgnz-C7VOZagDBqAvRSkyp0j9XgA8VCuFNt3VsbOd7kLVfqbCrTIYg9VWx_xUm10vd_tpDAGjivFz0Od-wbIOjXTGaCNVpSXGbscFlMRl9nPiuGaPDgLUBvhLOl2-1t0CuBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61ccebe799.mp4?token=Sw-lqw5qK9BAoutOmjGC85qfBqmT5WIB39dsfsenEdp3cOD_s24RKu52WB-Drj0I8m6g8UpdML0u66j3t1lXqWNiFti-XMzmFZ-3MPButjbwyUZDhUQzWMtzULBSbhFmYoCxufFmiX8sKlElhZ7mWuCTBdajjtZlJcIW2gS9aikOCK2aG8vqQZFBPSZ7v85JXUw0VTb-Qf8kpJEuB8Hgnz-C7VOZagDBqAvRSkyp0j9XgA8VCuFNt3VsbOd7kLVfqbCrTIYg9VWx_xUm10vd_tpDAGjivFz0Od-wbIOjXTGaCNVpSXGbscFlMRl9nPiuGaPDgLUBvhLOl2-1t0CuBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روش ساده و شیک برای بستن بند کفش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/695327" target="_blank">📅 23:19 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695326">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
صادرات گازوئیل از چین هم ممنوع شد
🔹
چین تصمیم گرفته صادرات فرآورده‌های نفتی به بازارهایی خارج از هنگ‌کنگ و ماکائو را متوقف کند. این دو منطقه نیز جزو مناطق تحت کنترل پکن به شمار می‌روند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/695326" target="_blank">📅 23:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695325">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/WN5CDazZelDZ7raNZZjGrpbZEkJw76uHreEFvXHdOpqLBBRQOEKFvB-Yeg_KFZNxN-LJtkMp6n5pnqTmnZkI_fyHrUHSIfJm0bVm9tDffwev4hoMkyPYDQM4O0_TQM8qM8euBMZlHKS35Omc4ayZB4iTdSfza6so3nqWeH51uRN-tJ0hPbyIMNtUfF_fvLFgkvGUVy24hDs0MUx-FPfnJV7b4bBniQLMHuMPtcS2jONI0lM4XD_DiRcLKQQIWlt2OgS6fsfF9MIqCBdBm-aTjuZ72G6uGBHswYuFng2ZubTOZxWZfDOiwKUMPCtydwf4sLe1zVi72S8BalKYIMYFJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سوتی در شرح برنامه‌های صداوسیما: حتما پخش شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/695325" target="_blank">📅 23:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695324">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caa5e1a8a5.mp4?token=eds--atdNtl5ksX6Pgwl1iYSqjuCfVTttLo-VINAXXXMaDsomxMQmgK77Zxx67B1_kLy0zuFdAxi6gc5xf59gBREc9izcEo6IzLoTcO5Rw5vjbaHqyVw5fNVA1gocH0EEPoM5Sx4J7BPOQ3tE9EbwVHM55tmbz8ovY4URiG7gRg9IuYjVaodkBgrs9-3nbIE5obANRWVLj0DPphNiwVOmrvtiiBuvpXjYAm8w6WYHrTZM5dHRs4fDzeNVoQXfImtrjp6MY27IstxuK3DvGm73V7YUgzHSZFZkzQwmdtqnV1V2WgpxEEtXX5tZnMO2jcZcrV1Bwu5GDnnwjXmii5v8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caa5e1a8a5.mp4?token=eds--atdNtl5ksX6Pgwl1iYSqjuCfVTttLo-VINAXXXMaDsomxMQmgK77Zxx67B1_kLy0zuFdAxi6gc5xf59gBREc9izcEo6IzLoTcO5Rw5vjbaHqyVw5fNVA1gocH0EEPoM5Sx4J7BPOQ3tE9EbwVHM55tmbz8ovY4URiG7gRg9IuYjVaodkBgrs9-3nbIE5obANRWVLj0DPphNiwVOmrvtiiBuvpXjYAm8w6WYHrTZM5dHRs4fDzeNVoQXfImtrjp6MY27IstxuK3DvGm73V7YUgzHSZFZkzQwmdtqnV1V2WgpxEEtXX5tZnMO2jcZcrV1Bwu5GDnnwjXmii5v8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیوی وایرال‌ شده از یکی از رتبه‌های برتر کنکور که همزمان با چند موسسه آموزشی کار کرده و از همه هم راضی هست!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/695324" target="_blank">📅 23:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695322">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnq-BzLOHag6ZvmxiZIFdXpKugbo-rt3fmP7bQFOKEwpu48pLchcOiCUkbFW1zyHBwK7oweuqEfx7vcLQpIrFU5mOs8F79TaD4tJokgWeJLWxjYGTyvxKaCiChnGK9qVUA13ZUfHa0koNd_SFvkfXrrbBR55Xlr2T2jw-_0pYrneVBu6ug7aDRy_ohJgNXNkQ-eOex4sG6z_XErf0eqkd5wB2XMeHF-2yu_k-fzAPyMZ9sFDXgeQo9aFc9pI9xlQu3bJewSh-iXil8yMW-FiZpcQecigW4BxNqvpmeMhzylrVvIiZPYMZiYfce6Eace_ISugZVmUkp5z2k32Fhd7hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان درباره جنگ اقتصادی: دولت برای مدیریت شرایط ویژه آرایش جدید گرفته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/695322" target="_blank">📅 23:06 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695321">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">صد میدان 5- میدان پنجم، ارادت</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/695321" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
شرح صد میدان خواجه عبدالله انصاری
🔹
میدان پنجم، ارادت
🔹
پس از آزادمردی و جوانمردی با فیضی که از سمت پروردگار جاری‌ست، نور ارادت در دل و جان تک‌تک‌تان جاری خواهد گشت.
🔹
ارادت خواست می‌باشد و مراد در راه بردن؛ نیتی‌ست که بدون هیچ تردیدی به فعل تبدیل خواهد شد.
🔹
مبنای رفتار جهان‌هستی با ما بر اساس ساختار ذهنی‌ای‌ست که درون ما شکل می‌گیرد.
ارادت سه قسم می‌باشد:
🔹
ارادت دنیایی محض: در زیادت دنیا به نقصان دین راضی بودن_از درويشان مسلمان اعراض کردن_حاجت به مولا به حاجت‌های دنیا گرفتن
🔹
ارادت آخرت محض: در سلامت دین به نقصان دنیا راضی بودن_موانست کار درويشان داشتن_حاجت‌های خود به مولا به آخرت افکندن
🔹
ارادت حق محض: پای بر هر دو جهان نهادن_از خلق آزاد گشتن_از خود باز رستن
#صد_میدان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/695321" target="_blank">📅 23:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695320">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jTNiE3vQ6cAmMh_oNGI1Jp5Ft_MQUR-bJAIle3hQddSW2AV7ptkG2lPzDtmB8myTYf-ZZR9XLIYGNEDShEJ4wal2LFuPTV1jFGFFGcSvGji3E_8U7vweIKeprA7zRo8fWibaMhVmW4hAwapIAU7yoJCgTgezsta2eFhqf1ReJoCHguOmuOAWv1upSa8gc8E8Nf2ORaDegYxeKdEaUNtgvHMwvqTJkIK23zNzCFzgzRoOwVKdjplSHyVcZ6tV4qb_8UypnY3UVJjLs_cWHjaQY1FwgcXqa_3fzVYKEyEn6BpDCc_OpYHQ7Yx4sf9sTAKAaPyJlDWsNVgYo8ipEaTBbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
ست هودی و شلوار بخر، کفش ورزشی هدیه بگیر!
👟
🎁
سوییشرت + شلوار مدل Mpower
رو بخر و یک جفت
کفش ورزشی مدل Pavlo
هم هدیه بگیر!
💳
پرداخت در
۴ قسط ۵۵۰ هزار تومنی
💰
پرداخت نقدی فقط
۱,۹۵۰,۰۰۰ تومان
🏠
پرداخت درب منزل
🔄
ضمانت تعویض ۳ روزه کالا
📌
مشخصات محصول:
🧥
ست سوییشرت و شلوار Mpower
• جنس: پلی‌استر سبک و باکیفیت
• مناسب سایز
L / XL
• مناسب برای هوای خنک بهاری
👟
کفش ورزشی Pavlo
• سایزهای
۴۱ تا ۴۴
• زیره
PU
نرم و راحت
خرید تلفنی
👇
https://memarket24.ir/product/fast/58354/180124/</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/695320" target="_blank">📅 23:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695319">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eec1ce1be7.mp4?token=AXnintcP8ehO2uecljdFE6romxY9W7KxVsBPlsYGHF4HLj8piNj_YI4oHUa3cdpxYOf2I2FQzl0PhZ88cHgvTFTpMIMjVag_g3AwNGoc7REX7ugq0QJAsqOr5gGM8k7f-CPguMDW6UOcjnI_olm90A9gN8SFYsaNu6lrWDPLLfXUJ6KvqSwvSXm-IJ62K0TIMFmkTdxYMW5qhHApWecLBIsx77PnOWwGq6ofmldL3rriAPdLMYn1r4ore59zqDdeYhM6q9bdDQrOT63IPKtbQ32XBmqrCbDfPVo9tC7_aEwXfkX4E7Ji_li-efaIS-gHjpE-Z5ZV1maTGx8_JRBDsmhYKY8KPLn3L8oNs7Cmh4bLiqpdh7roXBxSe4iKVVmKTfA2Vzgrt98LzuuI-_XHxlaLV-EyBju9zoaXKXIhtZ1cMs6CbbQ88_DyMRXeMs9hrtBjcRMiIAxagXVETUnBWBsy48GvGHn6tLdlSfMnKTXjVibx4sVgL3Y6OaaGz3SmRKMpw5C794TCszWRIfI7lKQLb982MAdV9j9oUnuNA9-cQcWeapZa3XxF89BYpTgiBtGfj2GtZ08Y2_1dvTX5gHiGFHLrRXQsfx-FLBFw6o4FfEbVSI0wVfIDFgCyfDZPfZR36I4xQz2OrJHZqj5Edjto1VA--WpGQJzshYs61jI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eec1ce1be7.mp4?token=AXnintcP8ehO2uecljdFE6romxY9W7KxVsBPlsYGHF4HLj8piNj_YI4oHUa3cdpxYOf2I2FQzl0PhZ88cHgvTFTpMIMjVag_g3AwNGoc7REX7ugq0QJAsqOr5gGM8k7f-CPguMDW6UOcjnI_olm90A9gN8SFYsaNu6lrWDPLLfXUJ6KvqSwvSXm-IJ62K0TIMFmkTdxYMW5qhHApWecLBIsx77PnOWwGq6ofmldL3rriAPdLMYn1r4ore59zqDdeYhM6q9bdDQrOT63IPKtbQ32XBmqrCbDfPVo9tC7_aEwXfkX4E7Ji_li-efaIS-gHjpE-Z5ZV1maTGx8_JRBDsmhYKY8KPLn3L8oNs7Cmh4bLiqpdh7roXBxSe4iKVVmKTfA2Vzgrt98LzuuI-_XHxlaLV-EyBju9zoaXKXIhtZ1cMs6CbbQ88_DyMRXeMs9hrtBjcRMiIAxagXVETUnBWBsy48GvGHn6tLdlSfMnKTXjVibx4sVgL3Y6OaaGz3SmRKMpw5C794TCszWRIfI7lKQLb982MAdV9j9oUnuNA9-cQcWeapZa3XxF89BYpTgiBtGfj2GtZ08Y2_1dvTX5gHiGFHLrRXQsfx-FLBFw6o4FfEbVSI0wVfIDFgCyfDZPfZR36I4xQz2OrJHZqj5Edjto1VA--WpGQJzshYs61jI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هگزث: ایران در حال بازسازی توان موشکی خود است
پیت هگزث، وزیر جنگ آمریکا:
🔹
ایران تلاش خواهد کرد تا قابلیت‌های موشکی و پرتابگرهای خود را بازسازی کند. آن‌ها یک کشور تروریستی هستند، بنابراین همیشه تلاش خواهند کرد تا قابلیت‌های خود را بازسازی کنند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/695319" target="_blank">📅 22:56 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695318">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
ادعای وزیر جنگ آمریکا: محاصره را متناسب با شرایط تغییر می‌دهیم؛ خبر خوبی برای ایران نیست
🔹
هگست: ایران یا مسیر درست را انتخاب کند یا با روشی دشوارتر تغییر می‌کند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/695318" target="_blank">📅 22:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695317">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cce820b59.mp4?token=UeiLP4owW7YuL8SWHZ8Xn1dXUtfWW0YPOVactAEApvzXJt7GX18P1bt3N6jjeiv1P_hIrr1yyFfivcNbCnc4qFr81WfwSN7mLyC771UmwPgQXbmE7DrxHhGC6bq05k6J7rRtMazXhDLo-62YbgN1NHlNXnXqqS6t8cWPyzdAOQ2aLqnBmw_zGEiBYclDPOgmKJ5IUDgUzke9sVP4b_QD2z31ilDUlLAOrIK-iujyeCX04qHG5rX7G13_AXcc1XyMFFm1OPK5Wec74OmtgV3bCY7Qdb7LE7sIfuqE7BWxMp8UMoqIfKF_AkYOvirSixl3C_8OwNmyqhSLSalolzh6YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cce820b59.mp4?token=UeiLP4owW7YuL8SWHZ8Xn1dXUtfWW0YPOVactAEApvzXJt7GX18P1bt3N6jjeiv1P_hIrr1yyFfivcNbCnc4qFr81WfwSN7mLyC771UmwPgQXbmE7DrxHhGC6bq05k6J7rRtMazXhDLo-62YbgN1NHlNXnXqqS6t8cWPyzdAOQ2aLqnBmw_zGEiBYclDPOgmKJ5IUDgUzke9sVP4b_QD2z31ilDUlLAOrIK-iujyeCX04qHG5rX7G13_AXcc1XyMFFm1OPK5Wec74OmtgV3bCY7Qdb7LE7sIfuqE7BWxMp8UMoqIfKF_AkYOvirSixl3C_8OwNmyqhSLSalolzh6YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مالیدن چشم‌ها می‌تواند منجر به پیوند قرنیه شود!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/695317" target="_blank">📅 22:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695316">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecd6879d9a.mp4?token=tzmGSkdceVYIm9UUS2EKW4-Gp20ajMpx-VqDzRA1BPx3XtZgaPTLv54YjRzfusVtDXRGUoRtQtfyIvwutiqTAua57lKgop5GOIv4ocwMkJ5pItimX5qqdOMjNNDyWWlV4uzxVw9HiR5rBPGoFlJPau7Z8TqsXhU-fzHajw40UtX7Jbgn9uImQvdmVFcb6IwsbGLYhJcV4R9muHjjLJ6WWwq1DZeljSvlHbdUimIc-ZuB6b2kkJ4aI_vQ6H8zSaAoFF-9wlTRCiX-6zW73nDK2bGxi4qv1iz2J_ExSQl_BrS_kzDYNlb765LyMpGsswNDqFOibiPINI0y9yrF45AQSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecd6879d9a.mp4?token=tzmGSkdceVYIm9UUS2EKW4-Gp20ajMpx-VqDzRA1BPx3XtZgaPTLv54YjRzfusVtDXRGUoRtQtfyIvwutiqTAua57lKgop5GOIv4ocwMkJ5pItimX5qqdOMjNNDyWWlV4uzxVw9HiR5rBPGoFlJPau7Z8TqsXhU-fzHajw40UtX7Jbgn9uImQvdmVFcb6IwsbGLYhJcV4R9muHjjLJ6WWwq1DZeljSvlHbdUimIc-ZuB6b2kkJ4aI_vQ6H8zSaAoFF-9wlTRCiX-6zW73nDK2bGxi4qv1iz2J_ExSQl_BrS_kzDYNlb765LyMpGsswNDqFOibiPINI0y9yrF45AQSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من الله
لِلّه
إلى الله</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/695316" target="_blank">📅 22:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695315">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1800e7f594.mp4?token=Fypla2vIjzEAYKfTE7Z4S-pgtA7k_epQeJ9xTqDZ2JT_cZT6WsEH6FkuioePn6-mtk1X9_rIVvRfeN2PxU_-HNSjEoM8NMQJbAuR1WQgsckKktMuHLVePu5BgdIZBgUvdDBcHTA2S5q5Bzu9PS2oJ5oL2IfVFBH26GaeKwJIfhsSgiW8TNwlNhkKHpNS1ikUZwiT0hgclOiMkd-3ez-EFwlrZXS5DbOnz_rT5ONl0-05TcAti-NvdYUMXgix4EeqbLBoXTrad_pa4f5jrErJXhgmm1iXCH60dwPmI058zwZjUK-xhXj14aMpkUibrQAlVGWwjCgG-RCA-LHMcRPU4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1800e7f594.mp4?token=Fypla2vIjzEAYKfTE7Z4S-pgtA7k_epQeJ9xTqDZ2JT_cZT6WsEH6FkuioePn6-mtk1X9_rIVvRfeN2PxU_-HNSjEoM8NMQJbAuR1WQgsckKktMuHLVePu5BgdIZBgUvdDBcHTA2S5q5Bzu9PS2oJ5oL2IfVFBH26GaeKwJIfhsSgiW8TNwlNhkKHpNS1ikUZwiT0hgclOiMkd-3ez-EFwlrZXS5DbOnz_rT5ONl0-05TcAti-NvdYUMXgix4EeqbLBoXTrad_pa4f5jrErJXhgmm1iXCH60dwPmI058zwZjUK-xhXj14aMpkUibrQAlVGWwjCgG-RCA-LHMcRPU4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیت هگست، وزیر جنگ آمریکا:محاصره ما مستحکم است و ایران باید انتخاب درست را بکند، وگرنه ترامپ همه گزینه‌ها را روی میز دارد
🔹
ایران هرگز بمب هسته‌ای نخواهد داشت؛ این منفعت حیاتی ملی آمریکاست.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/695315" target="_blank">📅 22:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695313">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/txe66vYrrKfGpKfmO3-nbnw20OTVXRe2lCZxV5xdtS-i_RL9dJtTKryIPruhMdPsYsFIoM6yHNJdKToB-iG7OLKNJNvPW-hVUeC0dJ65NNZXGK5anNdsnXDx5_nKT1hWwCKOSWHmy86xgmGWRqJdMFObbcpdz7Wr8ZRt0eQwcTHRn_u_Omdilrcdk4p67boDJW01gSpWpfTHl4PbQZApcXhGGs9jcfAnu-I_SYEcS0RHAsa8ocRSu_2g92L5yC0vhNftP7jWyBfzg1a1sp1aJksX0MSja_TPX8MRUnHbfKeSKiB7sHsW2LIAW06QwMBMWXhWX9xniwcgl1eqqht9Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EaPaXCmxkPQzRoUUxM9fKl6Z5_6O5TqVAxGADGMzNqsYf6SZKDlmHDnya6nCkP3ZvHwezWTwDSNI3bfOpL3a5TPE1c62ZKuiFDqA2aLglCAGVVWePczlTUgSlrCbuyKO73A0JWomDhYlTbv0uxbdCl-j4r3seSZ5CnnzlRHkRhb6jk3U5bMGvQPebdUMj0kvsn65rlVM6KwtIxSncry0CTVrNYQyEApSuuibkqlWXuZDMh2sJ0clHdK9s7HK5w7bORQNSdilLhJlr5QL3ZRo2wYcCI4txQEdUlsOBWqC5_nRnVX523cp7us2IK7ajxC5Z08YjI4KfUSVBwweJkr84g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصویری تماشایی از رعد در آسمان شهرکرد
#اخبار_چهار_محال_و_بختیاری
در فضای مجازی
👇
@akhbarchaharmahalvabakhtiari</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/695313" target="_blank">📅 22:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695312">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
توصیه پلیس فتا پس از کلیک روی لینک آلوده
🔹
فوری با پلیس فتا تماس بگیرید یا برنامه ناشناس دانلودشده را حذف کنید.
🔹
دسترسی برنامه‌ها به پیامک را بررسی کنید، بدون هماهنگی با پلیس، گوشی را ریست نکنید.
🔹
گوشی را در حالت پرواز بگذارید و با پلیس فتا هماهنگ شوید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/695312" target="_blank">📅 22:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695311">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6684ffdfba.mp4?token=nd1th-X842Qw9iAqoid2M1LRWc5a9w6Q1Spe6sY9lodGzD4xmI_3OVortUPaZC4A8a1hxIUWIVLnjYXpQrvlslKF12KbuOXGv1afRaGTnv7-1L0PZPRvFX0-Gvf1pKy_GxQP8ehAA25jM1htVzma-eo2VFcGkQa1KP3nLgTYiKSJ9fYKZLrTaYIg74pR6ux3ZktH0S1ak7A70-yKpMvFUmiaHmPufkHOQ47p58wdObSHw8ONh-whZZ-PYt5FDCwaDv_Nt5YLWGJz-bkAlZgPllJr9p7mrC6YaYg5vA0xJEuFDwzjR4q9womqCrTkuQQyNn62m4EIvEz6f2H9-4PhLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6684ffdfba.mp4?token=nd1th-X842Qw9iAqoid2M1LRWc5a9w6Q1Spe6sY9lodGzD4xmI_3OVortUPaZC4A8a1hxIUWIVLnjYXpQrvlslKF12KbuOXGv1afRaGTnv7-1L0PZPRvFX0-Gvf1pKy_GxQP8ehAA25jM1htVzma-eo2VFcGkQa1KP3nLgTYiKSJ9fYKZLrTaYIg74pR6ux3ZktH0S1ak7A70-yKpMvFUmiaHmPufkHOQ47p58wdObSHw8ONh-whZZ-PYt5FDCwaDv_Nt5YLWGJz-bkAlZgPllJr9p7mrC6YaYg5vA0xJEuFDwzjR4q9womqCrTkuQQyNn62m4EIvEz6f2H9-4PhLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ناخن طلا ۲۵۰ میلیون تومانی برای اینکه خانم نخواد ناخن بکاره!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/695311" target="_blank">📅 22:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695310">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
گروهی از زندانیان ایرانی که سال‌ها در زندان‌های امارات به سر می‌بردند، آزاد شدند.
/ صداوسیما
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/695310" target="_blank">📅 22:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695309">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osKa19LqU1rci8Z8SmHrtiQKK68DwnSN2BTgm-YAQkSK1ae5V9xykEGH4mJxbPFnRgQY5u1hDozNNUOGkcijxuUNMMJEMLfCRJWTltWQYKLSIRitdrAPwTomG-_Dk-3--i6UJK2Y5WQo_PjEBgzYjwiOp47r2DEBNlU13mr9wnB_J5_oDBF9el2RZyPGJluI7a4ybYYMUdujSH6sOw3zjeZx6fbQuzNm0aNupYRCbkCqRJzYaViAafmfe5j94xSD5fKMhZorrtYnTwLwSmPEepOghq7eZ_nmoEUz4oX1Vb8JUzPjl0ewjxvd7ar8tbjAIkpFpEjn4D6y28CcVjfjTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دخل و خرج اینترنت سیار به هم نمی‌خواند
🔹
افزایش شدید هزینه‌های ارزی، تورم، رشد هزینه انرژی و نیروی انسانی در برابر تعرفه‌هایی که طی پنج سال کمتر از ۸۰ درصد افزایش یافته‌اند، اقتصاد اپراتورهای موبایل را تحت فشار قرار داده است.
🔹
بخش مهمی از تجهیزات شبکه وارداتی و وابسته به ارز است، در حالی که درآمد اپراتورها ریالی است. نتیجه این شکاف، کاهش توان سرمایه‌گذاری، کند شدن توسعه 5G و فشار بر پروژه‌های پوشش ارتباطی مناطق روستایی است.
🔹
ستار هاشمی، وزیر ارتباطات می‌گوید در حالی که قیمت بسیاری از کالاها و خدمات طی پنج سال ۲۰۰ تا ۵۰۰ درصد رشد کرده، افزایش تعرفه خدمات ارتباطی کمتر از ۸۰ درصد بوده است.
گزارش کامل را اینجا بخوانید
👇
https://www.etemadonline.com/tiny/news-793433
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/695309" target="_blank">📅 22:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695308">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
معاون شورای امنیت روسیه: جنگ علیه ایران باعث شده کشورهای زیادی به دستیابی به سلاح هسته‌ای فکر کنند
🔹
ازنظر برخی، دستیابی به سلاح هسته‌ای می‌تواند تضمینی برای جلوگیری از درگیری‌های بزرگ‌تر باشد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/695308" target="_blank">📅 22:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695307">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmqnMFidH6iKsb0geq6FAHQjBJ8mft2yXtnWSC-8rk0V2AjTKPxVjmpbBRRhiqc6bEEC2cmqZICKm3D6BmbCx_QXirBUKy1FM4J6_DsdLkFUfuPfAKjC41vqfUO_rWwzzZkDlI8bqAxyeAFroQsx7M6VvvJYVApjrQGRvuckTRPjakHFbEdshk1-bJZF7uXa2KPBK3SRxGYBkpriDuxqFL94TGPiPnWgTaxjNs0Nm7esS1DpAjH-H5L2S3H6C2sd6fLOMP6OPPmHauLsPdkjuDHpn5SwKDrF8eFRXE93_Nu_hkTxwn8dP7WXkbdgGYBQYkcxKVC0MRuR0r0Efj9V9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سهمیه بالا نشینی
🔹
نتایج رتبه‌های برتر کنکور ۱۴۰۵ اعلام شد. اما آمار ۵۲درصد تهرانی ها از رتبه های برتر  بیش از همه جلب توجه می‌کند. آماری که بار دیگر فاصله آموزشی پایتخت با سایر استان‌ها را پررنگ می‌کند. در شهرستان‌ها نیز بخش قابل توجهی از رتبه‌های برتر در مدارس سمپاد و غیردولتی تحصیل کرده‌اند. آماری که بحث درباره فاصله میان مدارس دولتی و غیردولتی و همچنین تفاوت فرصت‌های آموزشی میان تهران و سایر استان‌ها را جدی‌تر کرده است. فاصله‌ای که از منظر عدالت آموزشی، نشان‌دهنده نابرابری فرصت‌ها و نقش امکانات مادی و موقعیت جغرافیایی در مسیر موفقیت تحصیلی را نشان می‌دهد.
🔹
هشتصدوهفتادوششمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/695307" target="_blank">📅 22:27 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695306">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7dHCrI3NLVRGj5F_rraEIAeyZsZxBCVq3QSFHHvNszFZuempyfV5y82kXGCG2EE0E0Vj6Vp-M4A-X2xvqqqeUIpf2W9SKrOxYQ5Lv6eEw52PkPyQy95J0fFT2jMYeFrp_SnJkMUzTlOwlGO1FR-wAtiNd8JUVrozsHtjaHn9NgITFpx_t05uWVm2dqgy4baGrQljLgdfe3HRe4rdOvBC5f6dG8-XdjffjlKJtoMNlqiqpvwsDPJ76qxtaWcxtGC_XJYL7Yyx3A-SYwDxVaDlmz_Ek_l0sNDrYAVvLdXnz6l7oyWfevUQJRpoeZdAoom8peuP7PejuCNrtMnoPkVpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس سازمان هواپیمایی: پروازهای شرکت‌های هواپیمایی ایران و عراق از فردا (یکشنبه ۱۲مهر ماه) برقرار می‌شود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/695306" target="_blank">📅 22:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695305">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
پیت هگست، وزیر جنگ آمریکا:محاصره ما مستحکم است و ایران باید انتخاب درست را بکند، وگرنه ترامپ همه گزینه‌ها را روی میز دارد
🔹
ایران هرگز بمب هسته‌ای نخواهد داشت؛ این منفعت حیاتی ملی آمریکاست
.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/695305" target="_blank">📅 22:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695304">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9229ecdfa.mp4?token=khbuBSUvfJ07Og5iQ_ww9uSZdE9zQVEuzrrMrLRJ0Se_mtAOSIsOtCurNqMpy6RP7NJ6zwaqW5b0MhzsSHVPVdTJkRbkd0ZUs4C-yot0TYO-30NvPD-hxGgWTMStHYfFBt9vbwyb-59XyH8ln2aFQjhDgQluj44BqTT1_V3QZltHy9cN3UUxlktR96mOBPGbDIGH1Ikk8FWfj9jXRhQluXlPRQi9zirlOWWck4pRDtXvmXHGbasVffoZOs7becT8ySxXZ2xAX7XU982RZUzw4fxM3A89S-aDjSZ-Ifzkbw4BgLIxl5Ghz-bvgclwUucCONJSWPXIre08YXR1NjcLBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9229ecdfa.mp4?token=khbuBSUvfJ07Og5iQ_ww9uSZdE9zQVEuzrrMrLRJ0Se_mtAOSIsOtCurNqMpy6RP7NJ6zwaqW5b0MhzsSHVPVdTJkRbkd0ZUs4C-yot0TYO-30NvPD-hxGgWTMStHYfFBt9vbwyb-59XyH8ln2aFQjhDgQluj44BqTT1_V3QZltHy9cN3UUxlktR96mOBPGbDIGH1Ikk8FWfj9jXRhQluXlPRQi9zirlOWWck4pRDtXvmXHGbasVffoZOs7becT8ySxXZ2xAX7XU982RZUzw4fxM3A89S-aDjSZ-Ifzkbw4BgLIxl5Ghz-bvgclwUucCONJSWPXIre08YXR1NjcLBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون شورای امنیت روسیه: جنگ علیه ایران باعث شده کشورهای زیادی به دستیابی به سلاح هسته‌ای فکر کنند
🔹
ازنظر برخی، دستیابی به سلاح هسته‌ای می‌تواند تضمینی برای جلوگیری از درگیری‌های بزرگ‌تر باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/695304" target="_blank">📅 22:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695303">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
شورای‌عالی هنر و ادبیات تشکیل شد
🔹
هیئت دولت با تصویب تشکیل «شورای‌عالی هنر و ادبیات»، سازوکار جدیدی برای هماهنگی و سیاست‌گذاری در حوزۀ هنر و ادبیات ایجاد کرد.
🔹
اعضای شورا چه کسانی هستند؟
🔹
رئیس شورا: معاون اول رئیس‌جمهور
🔹
دبیر شورا: وزیر ارشاد
🔹
وزیر میراث فرهنگی
🔹
۲ وزیر به پیشنهاد وزیر ارشاد و تأیید معاون اول
🔹
رئیس سازمان برنامه‌و‌بودجه
🔹
معاون رئیس‌جمهور در امور زنان و خانواده
🔹
رئیس صداوسیما
🔹
دبیر شورای‌عالی انقلاب فرهنگی
🔹
رئیس فرهنگستان هنر
🔹
رئیس حوزه هنری
🔹
مدیران خانه‌های تئاتر، موسیقی و هنرهای تجسمی
🔹
یک نماینده از انجمن‌های صنفی ادبی
🔹
۶ هنرمند، استاد و صاحب‌نظر؛ با حضور حداقل ۳ زن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/695303" target="_blank">📅 22:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695302">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
معاون شورای امنیت روسیه: با شرکت در مراسم تشییع رهبر شهید ایران انسجام ملت ایران را دیدم
🔹
من در سفر خودم دیدم که مردم ایران علی‌رغم همۀ مشکلات به زندگی عادی و حمایت از کشور خود ادامه می‌دهند.
🔹
روابط ایران و روسیه در بی‌سابقه‌ترین سطح خود قرار دارد /نیروگاه…</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/695302" target="_blank">📅 22:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695301">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ob-pfxbbJBUnFDgLz77N_ot-fxOEzmxABhKWY-fNv2UpubudziVotI181y06p4jHVojtEUV3RGf7NodRcE3texHkpa-hjZciZk1CDEaQh9bSddp4U7-kuw4Qs4VhrWqfiaWoTFboLitYLSBmBPM5MqQZiv1OKi3zO0rgXl4xoYT5DMLQc36bd2jSq3t938W8WBMiLV5rvtT9R63r0ZT1TkY1HCCXh4gdlSLzST5z83VSpOOOjCX1tBlv1gUuxROxhWvwUmWM3laQLYyWRwaGX4rBXKwtYquZUcRHKrFhucjovkca1O8scs6i1EUxzsNyo5Pq_hplh8GjEQXGC9RNaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سهمیه‌بندی جدید در راه است؟ | رمزگشایی از «توکن بنزین» | سامانه سوخت در مسیر جمع‌آوری داده برای سهمیه‌بندی جدید
🔹
شرکت ملی پخش فرآورده‌های نفتی اجرای آزمایشی طرح «شناسه‌دار کردن کارت‌های اضطرار» را در ۵۴ جایگاه منتخب تهران آغاز کرده است؛ طرحی که هدف آن افزایش شفافیت اطلاعات، شناسایی مصرف‌کننده و فراهم کردن زیرساخت لازم برای مدیریت دقیق‌تر مصرف سوخت عنوان شده است.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3249614</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/695301" target="_blank">📅 22:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695300">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93b8a01907.mp4?token=GRVHwyblPkc4N85BRTf_D1qbGtb8cQIizcZSzrQxkPlgFvEDBLfT11QOG9atDlt6ZYzzJ6gd-5fv05yPQp59Ct1CH2N8kdmBPMfpJBpnggnpm7LLNISAHmpsJmq5PzFia5B_5u0x3FgQ-nGckUjkr01dCtnayb7jGLSe_C-4UbdiSbUiBNSw5aMtJlIbqdIq7W2wJXS11L8jjy5MP9dSBiw4TuKGabXn_jEtuxAgpXUOPndcYled0vpbuIppnoD_1Aa4dZPyzI5Z52YjlksSagkAQ5OPXF3c-AeB5SW7EJzZveqpeYiyDn2HIV-eUOI83oX00i-UhBkTbtizyBQ38g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93b8a01907.mp4?token=GRVHwyblPkc4N85BRTf_D1qbGtb8cQIizcZSzrQxkPlgFvEDBLfT11QOG9atDlt6ZYzzJ6gd-5fv05yPQp59Ct1CH2N8kdmBPMfpJBpnggnpm7LLNISAHmpsJmq5PzFia5B_5u0x3FgQ-nGckUjkr01dCtnayb7jGLSe_C-4UbdiSbUiBNSw5aMtJlIbqdIq7W2wJXS11L8jjy5MP9dSBiw4TuKGabXn_jEtuxAgpXUOPndcYled0vpbuIppnoD_1Aa4dZPyzI5Z52YjlksSagkAQ5OPXF3c-AeB5SW7EJzZveqpeYiyDn2HIV-eUOI83oX00i-UhBkTbtizyBQ38g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کدام روغن برای کدام درد بهتر است؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/695300" target="_blank">📅 22:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695299">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b1b30b20a.mp4?token=uvDaCsLfzrmySNDVFoJuxxecgHaHfTmGWTTqFapujMV8ysH8BHKnXnjZoTc4jMcM1Ojbi33Z3uXBYqakQrNHNqKjzLxdMU-OqvwRaqDrvNaTrVhMw7o08YUW10VBl6VvKYBcaNiINH_NxWWMeVutGebX-nZQFyfytztcLi74D7rUh35PzXsdbGfrBrMW0PUJrIsD6CwLIT-mCJPoCMevibY2xSM5UkDsU4CaQxPGTmzYvJBUvMeIwZ_n9wurO88HdPMl6528s2G-a9LmdcPyaA4FAlvbn8CACO-RCQJsRukofrNF-33UrQCZjvdKj550DgHcQN_jn1o265_vlRMH4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b1b30b20a.mp4?token=uvDaCsLfzrmySNDVFoJuxxecgHaHfTmGWTTqFapujMV8ysH8BHKnXnjZoTc4jMcM1Ojbi33Z3uXBYqakQrNHNqKjzLxdMU-OqvwRaqDrvNaTrVhMw7o08YUW10VBl6VvKYBcaNiINH_NxWWMeVutGebX-nZQFyfytztcLi74D7rUh35PzXsdbGfrBrMW0PUJrIsD6CwLIT-mCJPoCMevibY2xSM5UkDsU4CaQxPGTmzYvJBUvMeIwZ_n9wurO88HdPMl6528s2G-a9LmdcPyaA4FAlvbn8CACO-RCQJsRukofrNF-33UrQCZjvdKj550DgHcQN_jn1o265_vlRMH4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون شورای امنیت روسیه: با شرکت در مراسم تشییع رهبر شهید ایران انسجام ملت ایران را دیدم
🔹
من در سفر خودم دیدم که مردم ایران علی‌رغم همۀ مشکلات به زندگی عادی و حمایت از کشور خود ادامه می‌دهند.
🔹
روابط ایران و روسیه در بی‌سابقه‌ترین سطح خود قرار دارد /نیروگاه هسته‌ای بوشهر همچنان فعال است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/695299" target="_blank">📅 22:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695298">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adnkIIpkw0TNuEEG-YQCjYyaZ3WPHXCZyWEWJXzWHByKgl77c6AlI9nb_LasBrWAAOkEum6c-_lj1n3ZeS_MDMWS2IOTrUNYdF5yiqo9fdfR8UBFhbnqIt4qUNbgTnJfBU7rRcrefi3IS-LHmycTM0G7Ywe0TSd01ECABDl1Qkmjhg82qcAMjOem0ydRCc10YScHX4m-ww55VTP5aSIg2cX3uuBHDRogD3c4LAUYlWXQv-4V2Ll5jUapNgjoqzatqOGVS50Ibek5705W3QqPZzA6ANCtnDQHd7cEjVzuGLSKYWs06KTmEMILVd-AWyS0UIkq-kUEYsTnZ7kGB5G3yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا مردم اخبار دستاوردها را باور نمی‌کنند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/695298" target="_blank">📅 22:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695297">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fdb8b388b.mp4?token=jGRtCgVmRa4BOxi98bQMoRZDywyc09RhQQ4IavVO0rseafCwcoE6fXqDEftapDgQYh2mqoK4NM3zht4wMw3mAL75bsxV0ovcGfvBZFP8G5CyvvPyf2CysPwaWv_tM2UCK7fkME8gqLP8lewKip8yJEwJZUrFQNxvVz90IQYACGyZDn2c9ShpTnc8Gwk_Vj7kRO9a8hKiF1XjV_ehaCCXLR25XPv9F47-ghOda7VZ8BLUIEPLBEQXuGEGtuKg9O0EXgkTdIfYNfdX4q1p6Vhjh_Zomn37rXzkuHYQn2KsNojQd0V3xbS_ZaKGrwhUQFjItV28JSqZAmqbG4agcfHdejxiOsZ40VDPWXAolORuhu1acgNtL8eDv0RFGQ4jkEneMMamCk5Ev_T4QfONZcLKjkeXWLXofqOZ9IO5bu-_bSF2pairlLJaeM2SIWyPTAYkbuuZru92jBs_w597vv_wiVTxSt4vck48p2s6_eF-C1n9D4Rdg2HFH9wTcGPIiBs-1GUTqy3spD0yEVWzfGYeAcuODF52FNoTACO4oIfIKwkTcxpdi_NcRT-Tg2TF8f1zoGehhQWwjSefY2tpZHkO9Sed7lrPoTz8ZnzYKKYIvw5jAwYZybo9meh7ribQYtSNg8vDVTNl4jiQiFcYH3uXmJbWYoY5Wg6mgG4CLr_PHEI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fdb8b388b.mp4?token=jGRtCgVmRa4BOxi98bQMoRZDywyc09RhQQ4IavVO0rseafCwcoE6fXqDEftapDgQYh2mqoK4NM3zht4wMw3mAL75bsxV0ovcGfvBZFP8G5CyvvPyf2CysPwaWv_tM2UCK7fkME8gqLP8lewKip8yJEwJZUrFQNxvVz90IQYACGyZDn2c9ShpTnc8Gwk_Vj7kRO9a8hKiF1XjV_ehaCCXLR25XPv9F47-ghOda7VZ8BLUIEPLBEQXuGEGtuKg9O0EXgkTdIfYNfdX4q1p6Vhjh_Zomn37rXzkuHYQn2KsNojQd0V3xbS_ZaKGrwhUQFjItV28JSqZAmqbG4agcfHdejxiOsZ40VDPWXAolORuhu1acgNtL8eDv0RFGQ4jkEneMMamCk5Ev_T4QfONZcLKjkeXWLXofqOZ9IO5bu-_bSF2pairlLJaeM2SIWyPTAYkbuuZru92jBs_w597vv_wiVTxSt4vck48p2s6_eF-C1n9D4Rdg2HFH9wTcGPIiBs-1GUTqy3spD0yEVWzfGYeAcuODF52FNoTACO4oIfIKwkTcxpdi_NcRT-Tg2TF8f1zoGehhQWwjSefY2tpZHkO9Sed7lrPoTz8ZnzYKKYIvw5jAwYZybo9meh7ribQYtSNg8vDVTNl4jiQiFcYH3uXmJbWYoY5Wg6mgG4CLr_PHEI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناس صداوسیما: چین ارسال تصاویر ماهواره‌ای به ایران را متوقف کرده است
🔹
مجری صداوسیما: چین به ایران گفته ابتدا مشکل خود را با آمریکایی‌ها حل کنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/695297" target="_blank">📅 22:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695293">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f96c6caec.mp4?token=GhcQwuN1Xpqt4GpyiDOekpUHO4WKRzeS4iLd46tQXEdt0rFp2-M5e1f0mMyJ2O0nbEFC6f-vWAjM3DG6Pnn6xBYx8PsyRkjZbLWGfAhVcXGFDeQBsvu_XMS2ZrF7hRJeTy9bNyGiMiiWaB7N2xf1O9fN03OpSHcjHRz4mNXTjCq--UaEMmqSyKuuS_RS3nR5KfE9nG5dOtNLUpePavCvYmpqZeOyiUlLdhNIitMGFevHhDXD8rVxCRlOgVVKCMvMl6-ZBsAxN2S6INWKL7WjD6PC6fSiHPV81GFKMLC2H0Ye21WUUgSXTkZa-_Zw6WfGef2bzaCPiP1lMbk2cHI86g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f96c6caec.mp4?token=GhcQwuN1Xpqt4GpyiDOekpUHO4WKRzeS4iLd46tQXEdt0rFp2-M5e1f0mMyJ2O0nbEFC6f-vWAjM3DG6Pnn6xBYx8PsyRkjZbLWGfAhVcXGFDeQBsvu_XMS2ZrF7hRJeTy9bNyGiMiiWaB7N2xf1O9fN03OpSHcjHRz4mNXTjCq--UaEMmqSyKuuS_RS3nR5KfE9nG5dOtNLUpePavCvYmpqZeOyiUlLdhNIitMGFevHhDXD8rVxCRlOgVVKCMvMl6-ZBsAxN2S6INWKL7WjD6PC6fSiHPV81GFKMLC2H0Ye21WUUgSXTkZa-_Zw6WfGef2bzaCPiP1lMbk2cHI86g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همسر بیژن‌ مرتضوی: به جای نفرت‌پراکنی بیاید کمک کنید ما بتونیم از پس عکس گرفتنای مردم بر بیایم
🔹
تصاویری از گردش بیژن مرتضوی و همسرش در تهران.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/695293" target="_blank">📅 22:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695292">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
آموزش؛ کالای لوکس یا حق همگانی؟
🔹
با شروع سال تحصیلی، یه چالش همیشگی بین مدارس دولتی و غیر دولتی وجود داره؛ سراغ شما والدین محترم اومدیم تا بپرسیم چرا فضای طبقاتی حتی مدارس رو هم درگیر کرده؟
🔹
پاسخ‌های متفاوت را در این ویدیو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/695292" target="_blank">📅 21:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695291">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/892233c8a1.mp4?token=KdP_KWk0_2qcttNwFnoOF0y9sAEnJmqki6Nb8NpQaPEW1SEKayrFbj2vQIO3Tz14QkgtpF3qz57dWs8PRaRTN-JvEv-4rdLEKXnlyrzOuvaPXZZO9qc6f9p4fEDbWxa7OiR8jVZ6_s_MWnP20xWKnw5D8SRgQIdEkvEcslb1__Gs0gWeUMdn_syVQFvx9hwNixYq-O90oIBCQtuPynCDTZmfbMU556ohgJryfD37-_WowIvjnAeO2I-do70uktKfNam0FHZlRjh3hwe0t8fkiIQzMa6Gd4plu7zVTdmXHd83it_JtFX7xUYawZdr3calcnsbKDJAwI0H-sbHhJBmuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/892233c8a1.mp4?token=KdP_KWk0_2qcttNwFnoOF0y9sAEnJmqki6Nb8NpQaPEW1SEKayrFbj2vQIO3Tz14QkgtpF3qz57dWs8PRaRTN-JvEv-4rdLEKXnlyrzOuvaPXZZO9qc6f9p4fEDbWxa7OiR8jVZ6_s_MWnP20xWKnw5D8SRgQIdEkvEcslb1__Gs0gWeUMdn_syVQFvx9hwNixYq-O90oIBCQtuPynCDTZmfbMU556ohgJryfD37-_WowIvjnAeO2I-do70uktKfNam0FHZlRjh3hwe0t8fkiIQzMa6Gd4plu7zVTdmXHd83it_JtFX7xUYawZdr3calcnsbKDJAwI0H-sbHhJBmuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فکر می‌کنی همه آمپول‌های ویتامینی یک کار می‌کنن؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/695291" target="_blank">📅 21:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695290">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a710bd78a8.mp4?token=aZqxd06Bikedjlz2WE_3h02tFXUW9CiFWhB-1QhwO2Ytl-YLqlImfbycytQHYOkczgTs-1DEJTC4fZca-ZmlT-lmi3ie2kVrFLPfqn9_DK-kYIS7WYWUS1Kvn2tTHigVFsvwdYuJhbpf1mNqtxWfV9FeH_vW1c_VxPcMY0NaI1kX7HOatTdu9bk_YMTxmHzuIhZ0OyAocrW2aHriIt7pvQeQ0aU-SK0ubossWdbNyFMrFkHvRCCbKx68Z7Rj-UVrtXj164xCKcG_2mN7RkeutSBvw4HXCeewK2A7bikwslR7kkv5VecciRJiRaGJb6iELIG3hH2OivfdMOEWdDB3hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a710bd78a8.mp4?token=aZqxd06Bikedjlz2WE_3h02tFXUW9CiFWhB-1QhwO2Ytl-YLqlImfbycytQHYOkczgTs-1DEJTC4fZca-ZmlT-lmi3ie2kVrFLPfqn9_DK-kYIS7WYWUS1Kvn2tTHigVFsvwdYuJhbpf1mNqtxWfV9FeH_vW1c_VxPcMY0NaI1kX7HOatTdu9bk_YMTxmHzuIhZ0OyAocrW2aHriIt7pvQeQ0aU-SK0ubossWdbNyFMrFkHvRCCbKx68Z7Rj-UVrtXj164xCKcG_2mN7RkeutSBvw4HXCeewK2A7bikwslR7kkv5VecciRJiRaGJb6iELIG3hH2OivfdMOEWdDB3hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه نجات یک کودک در حال سقوط توسط مرد جوان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/695290" target="_blank">📅 21:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695289">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFtcuqU8IXQ9SNXq3SW0B_b1N0oTATyhO8xk6KhqZ_79tFwxRFcHYGHfHckBZvfJnqnkiCBU1HwIeRT1TqcnpYtip2RoT-m-slCNRsXdT862i1u8EvRZGNx5gjFijg9SpC_1Bfk0vXpGCV9uidrEYVQM5CRqSeMmKtYoBTZtf9GK6ORL6uUAYPgRACxTyy-xnG63MKZTG3FzlR1kZnSRPCN8Wq3rbz0mmz5xuAVl9K34iKWyJh9_fQsUXAhIXBmPovD7_RY1-qKLASJPbnwi-R2KZpi7VALJKYo76epP-onxwkyROcpfIFETqZvHy0GmNytMJDaxMjWPBxMk5rfcoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از حضور دوسال پیش فرزندان رهبر شهید انقلاب در دفتر حزب‌الله لبنان در تهران به منظور ابلاغ پیام تسلیت ایشان برای شهادت سیدحسن نصرالله
. ۱۴۰۳/۰۷/۱۰
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/695289" target="_blank">📅 21:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695288">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
عضو کمیسیون امنیت ملی مجلس: ذخایر مواد غذایی کشور ۲۰ درصد فراتر از برنامه‌ریزی‌ها است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/695288" target="_blank">📅 21:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695287">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad3a15c064.mp4?token=ZC544riCO5pYxfCcilni689TWU1jl2geRhzZThZlGErfKAGZHqhgQL6atFjS4NpmBl54ac7L3QZpxeKu3hdN2F7YCTPzyc_-bu38aYvxnzbRbmW3CttvYtEp3tvcxJgeGC96xpYzP6-I6e_0rOZtXTtsRgZQAmcY1ToNrrIih3F4VgqgkxNekBw3uDbZ57zE1hiMD70lIooqmhfBmQ9HGU4Oy1M9vNU5aUvVGZGnuxwxnCKqKQ99NItx8jM9pVM1CWowhE_J2Hee105jUxpBrd-9-adt1bYfFans7Xs4alLmZ86pz0uaXpFZHQKlwjSUZCrKv2nsw8CmKWWj2YjMWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad3a15c064.mp4?token=ZC544riCO5pYxfCcilni689TWU1jl2geRhzZThZlGErfKAGZHqhgQL6atFjS4NpmBl54ac7L3QZpxeKu3hdN2F7YCTPzyc_-bu38aYvxnzbRbmW3CttvYtEp3tvcxJgeGC96xpYzP6-I6e_0rOZtXTtsRgZQAmcY1ToNrrIih3F4VgqgkxNekBw3uDbZ57zE1hiMD70lIooqmhfBmQ9HGU4Oy1M9vNU5aUvVGZGnuxwxnCKqKQ99NItx8jM9pVM1CWowhE_J2Hee105jUxpBrd-9-adt1bYfFans7Xs4alLmZ86pz0uaXpFZHQKlwjSUZCrKv2nsw8CmKWWj2YjMWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیروز در مکزیک یه گزارشگر داشت از وضعیت خرابیِ کنار جاده گزارش تهیه می‌کرد که همون لحظه یه ماشین لیز می‌خوره و تصمیم می‌گیره گزارشگر و فیلمبردار رو زیر بگیره
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/695287" target="_blank">📅 21:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695283">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AzSGQsHmkiZdO_08iw_YtRCeNVl7JY8KgszWQmabZXOHAWAAbdp0zAoSDRcjn0hMZbSCpYEYqodEjVzsnsuUoCu7VFj-i1Bj-NXT95HavxHa3h3_uhOZF9SDtZyuTPVC0f3rVMrwh8YDpp2sbqJCDTFclsk8RVCFYew63likb0kYice5INcW7ibbjqJQxPzQtw1VmaySPBAfpR9oiORJLIErrssveArN2m-PuHfIomrNnF7jPIO4ayW9m3kpyfvEOvC-hT7fMJz8xsDlnD1ldxRVdymubCde-EdhJ_q2dsHpWETi47ITErTBdSA7FS91XiThvn06c8LjJBMON8XzWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WQhJOIXfIwdCO7szi5ShUkjd85qqUYLk0HHwqiO3qtzi26MPGPdUa4z2KKh_nLwVVxBp1oDIQHna1UWbzfW4iqpNHaWdJuhql-yRDhj-ecabz92Tguvl1PNyfTDRRvDCHY-0IZlTnJJVPyjJNVSrn5iWqnee9-LGKarpVGAKPbD_w4NUPLynjG6xIimMtqUXpJFvUsjZDL81rhCfHpsxThdsmp43Iet90T75Yd4zVYC-SKIbeG25kvjXmBrv61Y3byGuvnUTq4ocXaNw7GjnOfS7lvNUNbi7n3DvtDxshRtV85u_fsamhJPkYOwaV5TSz15CagWs8-9be-Gr6ZX2tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WqFEGvNXEH5wFZ81TlvQlNV5fd4Trw0jq30Ed4k2BcG66iI1zp351P0iyioAKH2VudZQzdbZj020aPAa0dL50pVpIMrrp-2YC50xK52cnk2ba-ce4SI82bnk_JL_CK057mYDLUKazE8EXkQJ-Cmyw6nefEjx2zO0rBe-3zjpjdj2S0biAvdZlMJTTvof9t0_Nb2OlkCMjwAxALy3Z-wAuVHrYXb7gPB9WlNIPFRJOA6IWqpD2DzNR4PhqtcxYrKXEmGEKGzUhusBwyCxhPT0cqEZ8-oRcB3XE1hogjNlezFp8FMwLSh93EKQSBnPNajKCWYiSLAJ20QMqoOIvJXjow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nlWPXADIRy3ZyBukUyMzX4NPGVwlb6BuVHhPbWVRFjpYHguEWebawFgDcbcCHkEjHQx6bXaOzvdpRV2FKcI4oOYdySHh46BdHJPmdH1MUKrTIEo2Jcd54wLFqj0IEesRHYEwdn39hU0kHwkhktv34UJnToOEd3ZXOeMPhnBjk-Cy_Q42G0L9TttZ-dpSUuK9f99MTSNgsENdF-hVBFjfzqbSpVGDJ5zdoX4x-wAgCvRDDcsLwWBSKtyuwyiDpvZrPt-6pPGmuE3N9hQHXelBq84_sCl82cxiN_FhC9mT9H1VHZuSGVjtZpqxduKm4flZTi6H1uX_5wvaOLBri96xIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کدهای مخفی ChatGPT
🤖
#هوش_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/695283" target="_blank">📅 21:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695281">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2882858491.mp4?token=klvx7ebs4l4relihRjLTax2mELrBS4z4u4zfa_RjGv7Fg1Ia6OEQd0kFkTClIZFdAy9qq-gM41g8Rt-LzFQeI4WT3gnvEQfbtQTdQ7LNl5MyzVLkVETSf9J6UMh1seC0J9YzX2MJYnOReCZ42_dbtt6-XesVevuPJWFqjN7EEKI69bwzISptTT9icyMC3PogKymFWfwdv_CFIi0ntOtMs-jktmcjmRlCxTW-W7TLgCSipgnGhki4oMZ6NqXzZZUa-AfF9KsqgYZ_e5Qu13ITbCAXSQKap8Ew5R7d1p1wrXfOGetCnRDalcUDEHxakpbmk3vaXvJdSJz6mAV9a0HH1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2882858491.mp4?token=klvx7ebs4l4relihRjLTax2mELrBS4z4u4zfa_RjGv7Fg1Ia6OEQd0kFkTClIZFdAy9qq-gM41g8Rt-LzFQeI4WT3gnvEQfbtQTdQ7LNl5MyzVLkVETSf9J6UMh1seC0J9YzX2MJYnOReCZ42_dbtt6-XesVevuPJWFqjN7EEKI69bwzISptTT9icyMC3PogKymFWfwdv_CFIi0ntOtMs-jktmcjmRlCxTW-W7TLgCSipgnGhki4oMZ6NqXzZZUa-AfF9KsqgYZ_e5Qu13ITbCAXSQKap8Ew5R7d1p1wrXfOGetCnRDalcUDEHxakpbmk3vaXvJdSJz6mAV9a0HH1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه تخریب برجک زندان گوهرشت⁩⁩
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/695281" target="_blank">📅 21:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695280">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f50698e369.mp4?token=VYUuYhzD_Yx-ZVoWEJhvaUV2y1EFJsvxCd1DS2lgjBvTVcuUcoqBXq-SNtidwwDk7eECFGbuxIEAeWLvM1A3uZPbUitgt13M6O9XVh6Zj17CyVvnmq4tJHeKIBy46Z5wydxle8hhGixnNhbb06TdEQ98Qoetjwqft501UDgIBj0H-3rlNVwBdlWqEhqCtsb84GgZ7HZF_Zcvo-kwI-daeVqI9eX-4E7LgKG3mTG-4MtCZaky2q1ZzWoi5Jx--N4gDV6ntqT3W121_DmjP63ROZtzleImboJ2pwntsBwsOaRFnPo7gjNaKfQzi2ybkvYsKHHb9M3CH9Zqr9tRvBGOXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f50698e369.mp4?token=VYUuYhzD_Yx-ZVoWEJhvaUV2y1EFJsvxCd1DS2lgjBvTVcuUcoqBXq-SNtidwwDk7eECFGbuxIEAeWLvM1A3uZPbUitgt13M6O9XVh6Zj17CyVvnmq4tJHeKIBy46Z5wydxle8hhGixnNhbb06TdEQ98Qoetjwqft501UDgIBj0H-3rlNVwBdlWqEhqCtsb84GgZ7HZF_Zcvo-kwI-daeVqI9eX-4E7LgKG3mTG-4MtCZaky2q1ZzWoi5Jx--N4gDV6ntqT3W121_DmjP63ROZtzleImboJ2pwntsBwsOaRFnPo7gjNaKfQzi2ybkvYsKHHb9M3CH9Zqr9tRvBGOXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اثری که مکیدن انگشت روی استخوان فک و دندان ها میزاره رو جدی بگیرید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/695280" target="_blank">📅 21:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695279">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
ادعای وزیر دفاع انگلیس: ایران نیات خصمانه دارد و تهدیدی برای ما و متحدانمان است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/695279" target="_blank">📅 21:19 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695277">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bcc3c3cd9.mp4?token=c-KjVl-Yw1EJrlfYt4UQxIDg-4xmAHj4w-7E2V1Zg7yVDhdwtbmvSXKWoc_VAPVhoQoAWOrUd5wDtIN6V5H6iT-eG3hXZZxdIDsCxSfgxVqqerPaob5j-_yYqaOHnD8eFTtFhNDKRogeSz-NuEhOotjNz2yRZ47WBGZKNMo35JEdUle0Zyn2i02H5F5HLRf1YFbaxoXwNNedzUdKgjwqPxgQRxvvJ0CMW9mk4Tlu1b54fFTfjifvtPJmqWbevESxKNe-I3snwU4oE6ixhRugh6jqc7OMrUf8VD9S3ry3FUllvSpxDv2eZVj-MEPpUlTMGzwpYYm5XmXT0F5EndNRPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bcc3c3cd9.mp4?token=c-KjVl-Yw1EJrlfYt4UQxIDg-4xmAHj4w-7E2V1Zg7yVDhdwtbmvSXKWoc_VAPVhoQoAWOrUd5wDtIN6V5H6iT-eG3hXZZxdIDsCxSfgxVqqerPaob5j-_yYqaOHnD8eFTtFhNDKRogeSz-NuEhOotjNz2yRZ47WBGZKNMo35JEdUle0Zyn2i02H5F5HLRf1YFbaxoXwNNedzUdKgjwqPxgQRxvvJ0CMW9mk4Tlu1b54fFTfjifvtPJmqWbevESxKNe-I3snwU4oE6ixhRugh6jqc7OMrUf8VD9S3ry3FUllvSpxDv2eZVj-MEPpUlTMGzwpYYm5XmXT0F5EndNRPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیل امروز عظیمیه (بام) کرج/ خودروها را آب برد
#اخبار_البرز
در فضای مجازی
👇
@akhbare_Alborz</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/695277" target="_blank">📅 21:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695276">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcUNWlsvnG_LkQOg1Q9MJZAlzdrOSr6Re3PEDRGr1r4KycGmt9rg2HHoSdmM-UrdhsRbV-KCPvOOHgnynPDgHf2DblAUFohzuS55c_HkQRTF60Iwc8kUWCE0C09NBZ7WZg4ivjJSKzAzJlAaskD8O0-RjhtdTZ2dmV3OS0bYXhh8mRwhnnMF-1mj6OXh_FKKrqhlW5hOVCIXTnmYGwrEe0-5Gz88inA0eSVk9FdgrvHreVeudxO7lYJfH8e6wykYnyuXxPIDt2SlK9gLJJ7k1hXyn8RhmZQHFufaTKDyyrCOTKyyeHueWY86SMg1Z2iYCUTxTJqtunDn0tsn_jD3Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گلشیفته فراهانی در راه بازگشت به ایران | نشانه‌های بازگشت او چیست؟
🔹
انتشار خبرهایی درباره احتمال بازگشت گلشیفته فراهانی به ایران، بار دیگر نام این بازیگر شناخته‌شده سینمای ایران را به یکی از موضوعات بحث‌برانگیز فضای مجازی تبدیل کرده است؛ با این حال، برخلاف برخی روایت‌های منتشرشده، تاکنون خبر معتبری مبنی بر قطعی‌شدن بازگشت او یا تکمیل مراحل اداری این سفر تأیید نشده است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3249711</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/695276" target="_blank">📅 21:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695275">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlFuYHhmUhBGOSobz3U1FwxB8oh9k4bTD6t6yq9Wk4-e9004DpFS91Jw0XWY68YqQ0n60aPCK955zeNgq4YXl7QXh1DrXlALOeE4U1CHtuQAOjEI_unmZUeCyOLZxO6UXGSW2FtLXGMwFyhvzSewEbiaz56fwoG1bNqpWnU5ejbJ5XxLfcVeF6soKzaETctWAWaX1G1qfTLVAJnz1pkonFOtGUmFlRhTOY25ytQc8zOuAu9R2use5cjde5oc03QoRiEswI71EK4ts0P6W28zD4EISlpWRCvbE4g3x9UfjUkmzBqe8nfQe7sBNJIwJ8t_yMr5Xcv7dh2h7iVTMmipHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قانون ۲ دقیقه‌ای؛ شروع کن، حتی خیلی کوچک!
جیمز کلیر نویسنده کتاب عادت‌های اتمی این‌طور می‌گوید:
🔹
شروع کردن همیشه نیاز به انگیزه‌ زیاد ندارد؛ گاهی فقط باید کار را آن‌قدر کوچک کنیم که ذهنمان دیگر مقاومت نکند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/695275" target="_blank">📅 21:09 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695274">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
منظومه شمسی زودتر از تصور ما نابود می‌شود
🔹
پژوهش جدید: پس از مرگ خورشید، مدار سیارات بیرونی حدود یک میلیارد سال بعد ناپایدار و منظومه فروپاش می‌شود. زمین، عطارد و زهره پیش‌تر در مرحله غول سرخ از بین می‌روند./ دیجیاتو
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/695274" target="_blank">📅 21:09 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695272">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqZkpLGzAbypYXfSJl-SDTF_vDlmj89wEGwARz0rtwYXWW_luVdvtcGn4Uv0LcPQWCZ6TgztlvAVcz3cvMFcLB_PYt5H9pgT3cPuvkCrc8qgZ1szwg7zo8uyg4xneoUos-nxThm8XdBV9gsUUqxABFM5rFU9hOq-Bj44M8lTqaUzqFJlfStWKNQ0_TRDymE0fc39fjOW3tm8CSn7qIuEAMaul25gpJqSi14A_buKQlo-gUywiqCh400Kn5AJ1sXRz2g62wl9TGb-CvS9Yx75ZE0gbH1PSNnKsydmc3njH_Y9yPRA6Ye90gzwELtkr8iGTQdrGlP89HRXRgX2wR7PrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd9fe5b7e4.mp4?token=caw-APB030aOXagdNJObeyt9LCrPS3LaKWfe3E2c5IxeXBRgJpJXfYPM-a4fktxKPaYvYadKyjsbpIOV5Z8sS9direbggSNZPO1x8JMRb4Z8Ldt0XqFQ0Mg4GImyM6JEeFB5k_o7PfaQ9F-HfbqrdYWslqnFyJjfhZWD2SUt9lrEXat2VotCxeaEsmZ6dDIq7sIbdpENfk856el2hIYFkg80ZE7Roiz9YjOaiLqF9ydfWlT7GQFIDIE91P7wSEZZYw0GxwmTfxlmK8p-5nc1GsdDjXxoCFlW9gJWqmlChQlfHmwzqR6iiPBsc6iAOTyYQ2Ffbakw6Uanjb1JvcOKoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd9fe5b7e4.mp4?token=caw-APB030aOXagdNJObeyt9LCrPS3LaKWfe3E2c5IxeXBRgJpJXfYPM-a4fktxKPaYvYadKyjsbpIOV5Z8sS9direbggSNZPO1x8JMRb4Z8Ldt0XqFQ0Mg4GImyM6JEeFB5k_o7PfaQ9F-HfbqrdYWslqnFyJjfhZWD2SUt9lrEXat2VotCxeaEsmZ6dDIq7sIbdpENfk856el2hIYFkg80ZE7Roiz9YjOaiLqF9ydfWlT7GQFIDIE91P7wSEZZYw0GxwmTfxlmK8p-5nc1GsdDjXxoCFlW9gJWqmlChQlfHmwzqR6iiPBsc6iAOTyYQ2Ffbakw6Uanjb1JvcOKoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری نزدیک از آتش‌سوزی گسترده در پالایشگاه سعودی آرامکو در ریاض، حومه جنوبی شهر ریاض، در مرکز عربستان سعودی
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/695272" target="_blank">📅 21:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695271">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsOhGw_zO_PdN1_eCmjZ7BrYnH0OxkOEv3FAyyoHvdOGgJfJ84yC8VPBIzQddG-xASeItbFJ44uLHBVbTsqPvvykWBnsn24H76WC4g5XY4HwtPBMb6uDk6rHRkGMap3o1lXRkd6YzCC_h8oB1vCNpIhg5uvH_I2-6Tqlxde6aP_lvVkISaqEzeZMA8lWq91YoPS5yI7wdIDJfiI4VM8HksKcPxJ-NkkVg7urCN-jVGzY0RbyTh6mTszT81U5SWbwtIh_vtjrMzMaw-DckRZNS8Pox1f-3YR10QM5EseCWRnqVC-RLEpQWueHLJJgFUExBiNZulgCruXV3NMeyr0AMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون علمی رئیس جمهور:  قدرت یعنی حق انتخاب؛ هر فناوری باید یک گزینه تازه پیش پای ایران بگذارد
🔹
دکتر افشین معاون علمی و فناوری ریاست جمهوری، در جمع نخبگان و سرآمدان فناوری در
مشهد مقدس
با طرح این پرسش کلیدی که «از تمام دستاوردهای علمی چه میزان قدرت برای ایران ساخته‌ایم؟» تأکید کرد: قدرت معنایی تشریفاتی ندارد؛ قدرت یعنی حق انتخاب.
وقتی زنجیره‌های تأمین مختل می‌شوند یا فناوری‌های راهبردی را به ما نمی‌فروشند، داشتن دانش فرآوری و فناوری داخلی یعنی وابستگی صفر و حق انتخابِ حداکثری.
کشوری که فقط یک گزینه دارد، در لحظه تصمیم‌گیری آسیب‌پذیر است. مسیر پیش‌رو مشخص است: از علم به فناوری، از فناوری به حق انتخاب، و از انتخاب به مرجعیت فناوری.
@AkhbareFori</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/695271" target="_blank">📅 21:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695270">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08eb3b2263.mp4?token=QSXmbZSJ1GHKOtHb2dYzcoMEqv_h1xAH3nRamx6Zv75IchPCtG-eWI0EdATjPL4ltbkhE4-IMcThbAxwT4Pks5-67LAA297tYLULOhxdLWDim-S5oWT33hgUBNiWA4Zp38_utxSNjmcoiUaxWdBSyUIIHnC3GUHBgfpwSrZimsfGcHg4FnTN-ciWKHkwLIMvsED8KXNIXlZYk_CqcrGAUIUFfpnfkp7k_1ebGY0uA_vtA4wr5bW1F1z2qYlNahJPuepAnjlLsQTM_hjND4gTwJ4HY5cHB3p9XHS0nB9wIt7BHxwp6e6eJM_mTWjZZkFLSdvOF6m_dy8DhPB8JJB61g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08eb3b2263.mp4?token=QSXmbZSJ1GHKOtHb2dYzcoMEqv_h1xAH3nRamx6Zv75IchPCtG-eWI0EdATjPL4ltbkhE4-IMcThbAxwT4Pks5-67LAA297tYLULOhxdLWDim-S5oWT33hgUBNiWA4Zp38_utxSNjmcoiUaxWdBSyUIIHnC3GUHBgfpwSrZimsfGcHg4FnTN-ciWKHkwLIMvsED8KXNIXlZYk_CqcrGAUIUFfpnfkp7k_1ebGY0uA_vtA4wr5bW1F1z2qYlNahJPuepAnjlLsQTM_hjND4gTwJ4HY5cHB3p9XHS0nB9wIt7BHxwp6e6eJM_mTWjZZkFLSdvOF6m_dy8DhPB8JJB61g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فعالیت پدافند در آسمان قشم
🔹
پدافند هوایی نوین نیروهای مسلح کشورمان در قشم موفق به رهگیری یک پرنده متخاصم و اجرای آتش در آسمان این جزیره شد./ تسنیم
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/695270" target="_blank">📅 20:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695268">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FWAip9C_OKXdJCtdsAON4GBuRAMibKn_osQE3JwIGl3yrX_O3ThPfmyDo7aZyBsgJ7vPFkwLP30jyOY7Bpo--WxIy6lJ1gAoHfMWxBsEGXLxgy4RemPOi-oezUNOLeBssGhAlAL9DmU1rtw9aa2tKePXTJoAt1lkllENUtxsm7J_56sKbXsLQwb5caHAA0ehw9P0dN8b5FxhRo-dipSmZN3C9JgnvurTmM1O1YLvldcngz4cnNGqF63trYlM1eDhK1vxHX12kw3W3iDgTcWJQ3W9ntikXWWRlGL2CRBP2lqdbK0WkWWeViB72S5j191sXZ-bvEs3SL1u05v-HKcqIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FNSeregDENQ7f0ern0i-INqtfug4uKogrQMtiWyS85KqN-xTMm0iRJYDxdOaE7dFdOdkCw7iaIn61hFa1giuQQS_yH81-6Y0abDLcr3eYSBw91Jv4ApCa0wtQVAlh3mswuaJnmmAmwPgDTIRBAFIIg_1RrQ8uDgxmFyOh3LT6ZzAuVYsDc0NsgK6g3BNBETqemq0bSoQtS3msyKYyFPAFj2uo4VHFRNIdZyG6cPv9hMdV6ECIIi9cSyC572rq3ZVGXjIxkuUNGXX7LKaLnzXeZJpIMlijG2hlS9xKGV8AvQUnemkoRNrKYX3haIYV3nrvsrZm6-nwMHiFp5yLLXkmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
موشک‌های پدافند هوایی «صیاد-۳» ایران در جزیره قشم شلیک شدند
🔹
این موشک‌ها بخشی از سامانه توانمند «۱۵ خرداد» هستند و حضور عملیاتی آن‌ها پس از دو جنگ اخیر، نشان‌دهنده اقتدار و بازسازی قدرتمند پدافند هوایی ایران است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/695268" target="_blank">📅 20:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695267">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
خرید نفت ایران توسط چین قبل و بعد از جنگ چه تغییر کرده است؟
🔹
پیش از جنگ، چین معمولا روزانه حدود ۱ تا ۵/۱ میلیون بشکه نفت ایران خریداری می‌کرد. این نفت عمدتا با تخفیف و خارج از بازارهای رسمی و در شرایط تحریمی معامله می‌شد. پس از تشدید فشار بر صادرات نفت ایران، اما جریان نفت ایران به چین به‌ شدت کاهش ‌یافته است./ روزنامه اعتماد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/695267" target="_blank">📅 20:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695266">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
ادعای برخی رسانه‌ها مبنی بر سفر عراقچی به امارات تکذیب شد/ عراقچی در تهران است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/695266" target="_blank">📅 20:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695265">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7379ba0ed1.mp4?token=j5Lzd-s-sJiJX2Zs8isig9w0LBv34y7ZvP3sUSIwpgdmNrP_z8RiPCTNKVKK8RdCqkRncL32hUDV7LyRjP6baXfLjvnfBg3PCyLcHM2OKrcSRwBciLyLpoD664_PaXTpiplajz7zfT6uDVZZHqilGOo-EIQsmCrbTQEs-RxoQBEVR7QnI_XTreNlymHBUhQ02VLR5t8ng0Nd_OZ8URchSh09POEJDqfH90yFiP9JF7rziT_jw-7b1oFjyCpv9ZriZLOYZRO9zQmhl0d9wQzhw-Kj9DuavLKXlxa_vBMMMNFGvCUAYVxVAwdUqQumOT91tJZ9wLpKXl5EfK8GHUzJyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7379ba0ed1.mp4?token=j5Lzd-s-sJiJX2Zs8isig9w0LBv34y7ZvP3sUSIwpgdmNrP_z8RiPCTNKVKK8RdCqkRncL32hUDV7LyRjP6baXfLjvnfBg3PCyLcHM2OKrcSRwBciLyLpoD664_PaXTpiplajz7zfT6uDVZZHqilGOo-EIQsmCrbTQEs-RxoQBEVR7QnI_XTreNlymHBUhQ02VLR5t8ng0Nd_OZ8URchSh09POEJDqfH90yFiP9JF7rziT_jw-7b1oFjyCpv9ZriZLOYZRO9zQmhl0d9wQzhw-Kj9DuavLKXlxa_vBMMMNFGvCUAYVxVAwdUqQumOT91tJZ9wLpKXl5EfK8GHUzJyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کاملا واقعی؛ با یک پیاز، شکر و مایع ظرفشویی کف قابلمه‌هات رو برق بنداز! #ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/695265" target="_blank">📅 20:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695264">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77c92db990.mp4?token=Co8IPFpOfP_cwK4a1mfbfcfTQpn01YjszU-91iz33bHLFb6_uLDIcarLwzUyUmo0Te21MP3TecdBnvlCbvbdNVdAASFm6FQQ3UKKF_xh-I70xQvUe7Iwz79Ne1Q4oBxGvS2IzMjRyc6F3yuQPAX32QBCCUmQI2XvZqNy1hmUsJHFuvJw9qd7Btd6J4r7cqZFHBaoivdH35h7-DsC6Fe8L22DMYZpUYIWeCw7CDaZIdIfAuimOZPuu2l4cZVN2nMzfd3FNSg8iq73os8Fg6u5G3k60pq-gTJuLHFnOvIdi5U_uJ9PpTGC7Qnm8DsGLu_LWcwVKZe2k2ZI_ZDH2je2Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77c92db990.mp4?token=Co8IPFpOfP_cwK4a1mfbfcfTQpn01YjszU-91iz33bHLFb6_uLDIcarLwzUyUmo0Te21MP3TecdBnvlCbvbdNVdAASFm6FQQ3UKKF_xh-I70xQvUe7Iwz79Ne1Q4oBxGvS2IzMjRyc6F3yuQPAX32QBCCUmQI2XvZqNy1hmUsJHFuvJw9qd7Btd6J4r7cqZFHBaoivdH35h7-DsC6Fe8L22DMYZpUYIWeCw7CDaZIdIfAuimOZPuu2l4cZVN2nMzfd3FNSg8iq73os8Fg6u5G3k60pq-gTJuLHFnOvIdi5U_uJ9PpTGC7Qnm8DsGLu_LWcwVKZe2k2ZI_ZDH2je2Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درگیری آسمان تهران با برج میلاد امروز
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/695264" target="_blank">📅 20:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695263">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
معاون علمی رئیس‌جمهور: برای تحلیل دقیق‌تر کنکور به جای ۱۰ نفر اول، باید یک درصد اول بررسی شود/ منابع آموزشی یکسان در اختیار همه دانش‌آموزان نیست
حسین افشین، رئیس بنیاد ملی نخبگان در
#گفتگو
با خبرفوری:
🔹
هفته آینده تصویب دو آیین‌نامه برای حمایت از بازگشت نخبگان و استفاده از ظرفیت ایرانیان خارج از کشور در دستور کار دولت است.
🔹
منابع آموزشی مناسب هنوز به شکل یکسان در اختیار همه دانش‌آموزان نیست و برای تحلیل دقیق‌تر کنکور به جای ۱۰ نفر اول، باید یک درصد اول بررسی شود.
🔹
برنامه‌های جبرانی برای دانش آموزان جنگ‌زده جنوب، در اختیار آموزش و پرورش است و وظیفه بنیاد ملی نخبگان، شناسایی و حمایت از استعدادها است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/695263" target="_blank">📅 20:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695262">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLBR0YXiCamHN4gixN6zODbI0XJxXZxylGbp46k26HKJN5MeoiPWgjQ0qwbEXGfP564tdjgw0i7qP9HelhXeSQtzdPWkUckRwkcoO4CTcCHQlqApwTHDFHg9LGUlsXTa_2FttIz5ljZ1vG61PzrCAUpnqG8fYg7hr-fI5IqjH2M_w0Xk-VJ4AxL7Pl-WFW2o0ppxD0rhW-1OsphhkBBiRxWW2rv8FJcKl1K_rcO87g1lR6kYF1CH4zWgaip_Y6PXA5pl2wCZfgGsECykCwEoaODm7JJMlMW_txCS98COhqIO3GEupetQ-6dmmVluVOEih6YD4TPOzJuNkrL_nOIEDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پدر و مادر رتبه‌های برتر کنکور چه شغل‌هایی دارند؟
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/695262" target="_blank">📅 20:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695261">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
مجوز روزانه ۴۰ پرواز ایران به نجف
🔹
رسانه‌های رسمی عراق از توافق برای انجام روزانه ۴۰ پرواز شرکت‌های هواپیمایی ایرانی از مبدأ و به مقصد فرودگاه بین‌المللی نجف خبر دادند؛ شرکت ماهان از این توافق مستثنی است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/695261" target="_blank">📅 20:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695260">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
محسن رضایی، دبیر شورای عالی امنیت ملی: شرایط کنونی از جمله دشوارترین مقاطع کشور است /روند مذاکرات بسیار جدی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/695260" target="_blank">📅 20:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695259">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-Wkp6RUpWH2ZBGAxwK3R6m3SbvNGlvvfFF2RNx2a_JbQr_J2IKHVeKPdWdQ5DSfDmMhlFLJq6WCYY2QS8BkctWzJQBZfAR9oKchk_QeuabESiS3pqpmOWlFfRfCWEcSo-9Qs7rw1wgVjGnmhrfvrpWR0CHPgQLyLQ7tw1IeE_hLYObMIinFdCvuWiUOKnt2wKucL3j4EL0svS8jOeByATWQKx5JSG6Cj-urnCPa6WSgwtN59OnFAb3U3EkxWI80-lptWeO6uwZlyBcNSltZog8oFrzgIXxRkiksiMluG5yCboxKv1fwL_oxfYnVl1VIn7l7bVTPfp2pg1_tcegL_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
قاب گل متبرک فوق ضریح حرم مطهر امام رضا (ع)
ساخته‌شده از گلبرگِ گل‌هایی که روزی خادمِ حریم پاک رضوی بوده‌اند؛ یادگاری معنوی و ارزشمند از آستان حضرت رضا (ع)، برای نگهداری در خانه یا هدیه به عزیزان.
ویژگی‌های محصول:
✔️
اثری هنری با تکنیک رزین
✔️
قاب از جنس پروفیل
✔️
قابلیت نصب روی دیوار
✔️
دارای شناسنامه اصالت
💰
قیمت اصلی:
۷۹۸,۰۰۰ تومان
🔥
قیمت با تخفیف ویژه:
۶۸۹,۰۰۰ تومان
📩
برای ثبت سفارش و دریافت اطلاعات بیشتر:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/695259" target="_blank">📅 20:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695258">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/328f198eff.mp4?token=p8IPswX9ZfhJ5wL8BaZdz55Ko8LH1IXNabtPUL_zkBGCRka4Ky2iQBZ1-WiYTA9rW7VYK5Z2gQ9kRJ0fvYtuZjijqt5mVlkBa_hYa0DQCGyzSQXU9BjxgSJNDO5W5v2cEnrNg66PqOydyo90sBwCuvZzdyJuBcOr7AeSHX3K3Zi4Oen2mN3glUXilt6w8EKNZszShsVTw5tzMmEZk6OxF3ihSss0lD7_s6Ogk4_3vbIbRIJ1PXxF8d53BzMPtLjygjz2vG1Gv1-CtROcA1scejpFR0B82ldHa77iy2WyuSX2e7EV6MBSPH5KkYPZR8IofC1xi5__1p5sBx5uVS776w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/328f198eff.mp4?token=p8IPswX9ZfhJ5wL8BaZdz55Ko8LH1IXNabtPUL_zkBGCRka4Ky2iQBZ1-WiYTA9rW7VYK5Z2gQ9kRJ0fvYtuZjijqt5mVlkBa_hYa0DQCGyzSQXU9BjxgSJNDO5W5v2cEnrNg66PqOydyo90sBwCuvZzdyJuBcOr7AeSHX3K3Zi4Oen2mN3glUXilt6w8EKNZszShsVTw5tzMmEZk6OxF3ihSss0lD7_s6Ogk4_3vbIbRIJ1PXxF8d53BzMPtLjygjz2vG1Gv1-CtROcA1scejpFR0B82ldHa77iy2WyuSX2e7EV6MBSPH5KkYPZR8IofC1xi5__1p5sBx5uVS776w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی جدید از سیلاب امشب کرج
#اخبار_البرز
در فضای مجازی
👇
@akhbare_Alborz</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/695258" target="_blank">📅 20:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695257">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
این کلمه‌های دو معنایی رو یاد بگیر و با یه تیر، دو نشون بزن! #زبان_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/695257" target="_blank">📅 20:19 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695256">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Frdj7ZY2Yb1WqU6s-UDV2lbyApFeu8ZK2gVdQasBBdBqLw2VRgJh3yu0prb7xLBqHtbG_hXMcGArmTiXRMjXKmZDY8zC_-WGDVun9ejjp_eb6rl9Vf_qXV8BAsVlz3SfyBDuHWiesXeJJsaha1SQ1cU6Sy3nSBQX30BODWaP8jw8yAwASNvRb8PDQWq_Ar_t_iQ7FllxJdvX5YLfjqpEcn3_24odvK5U1fkmRRq9fuJPcrf3r04QxwS9wf_MYQz9rAWKB_xSHODoIU-qtU81GOu4th0194WosX-eRu342UNsMqAt1FtzFDd9_vST7JnOzIYfjWiSsGF6IJCH_aUYfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نحوه استفاده از سهمیه جنگ برای کنکوری‌ها اعلام شد  رئیس سازمان سنجش:
🔹
متقاضیانی که ساختمان محل سکونتشان در جنگ‌های تحمیلی ۱۲ و ۴۰ روزه تخریب شده و قابل‌ سکونت نیست، با تأیید مراجع ذی‌صلاح می‌توانند فرم تسهیلات پر کنند
🔹
ساکنان شهرهای تهران، اصفهان، شیراز،…</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/695256" target="_blank">📅 20:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695255">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
دستیار رئیس بانک مرکزی: اگر تورم را کنار بگذاریم نرخ امروز ارز با سال‌های ۹۷ و ۹۹ یکی است/ افزایش کنونی قیمت ارز گذراست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/695255" target="_blank">📅 20:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695254">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzWbgEHkZMPuTpYQ7z85J9BJ0gSoZSSRSZ0KFTZJ9xYIiOvjRz_cgyqeR4lCPpZMZViwWzmL9tym3dGkiOzbCMfIW67QeB95aRnsQJsqtRgbCmM2g-gKgLsE7z5y9IwzXSUUuog3Ax9iraYkSWIVylMCNbZroSDgse_BpC4P-1UUvUwkDDXNxvTJ9eWeZnVDBg5gqWQ-uxKLgXYeoApGsJ6Ec97tXcb1vo7aOy4ptDAco7fidYI7syc7TBpDHWTX5d5b-wp57mBu_gwGbUrPmDjdBRS4HR9F1Xtgzv2I8KYG4KfhVdxpORluvasvDE-DOCIALH64jJNV5ke3gCoXHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جزئیات جلسه محرمانه کمپ‌دیوید درباره ایران | افزایش پرواز سوخت‌رسان‌ها؛ زمان حمله معلوم شد؟
🔹
گزارش‌ها از برگزاری نشست چندساعته و اعلام‌نشده مقام‌های ارشد امنیت ملی آمریکا در کمپ‌دیوید حکایت دارد؛ جلسه‌ای که در آن، گام‌های بعدی واشنگتن در جنگ با ایران و تحولات مرتبط با درگیری عربستان سعودی و حوثی‌ها در یمن بررسی شده است.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3249675</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/695254" target="_blank">📅 20:12 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695253">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJj4tQrjYC8GImRaxNCfrOlOpQseykvxCNyHfjcGL1pHYWEZxT5dG12KHZnt8tRmbCjZNlwl4iuQxQeGJj7i4EzpIlU1KnzqjLPGCcQvOY4BHjwcQLiXqnTeOhy_jq5PlpvgEHGKV2g1xliMr1impyEmv-AWZGm84zN5uHgU0r1I5nW6J0uKYqdPvpe39uhauroCETcBLOkC0v3XSArVE4q4GR3VzEiMPdvt3021ovrH1IrEyKZu2Eg6V2cy8E_CSJ5OKb-G0tl-SbWPOMePtT-vVUReVpNxD3M5rG_KdgNsctEIBdIr7gERcgtumRhubPXBDS2Zs5EdwcFM-pZHtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی: گام بعدی ایران، اخراج کامل آمریکا از خاورمیانه است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/695253" target="_blank">📅 20:06 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695252">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c30420132b.mp4?token=M4moYPJXYV3Q4TKKc2UILdtisacQi1FsYkt0QtrlRpf1pg7QGdRAcBMMilx5I39AgRhINUITNXr98V9-y2RxXB74YmLJEB0cgCKDKqUW4AiORnA32YVDdtD7HWarZrMr_b7teYC_ObZftE5t5EMqllRUKlShi51lfhFyEbeMTLdCQiKgIy3MUH6HrQL-lX7RETfRvl0GT6VxXUEMZ6rsRQUXh5LDsBB62BnIoZfDkHNVgfeOI3cLA2vnVge6_uEE-esr4ssFXhiKlNXkiBrErXuwriMJyIul_bUeOZDBbnPACRBSBjughWKWypzXN97Hn1GUKUvzjSpkDOXT6xthuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c30420132b.mp4?token=M4moYPJXYV3Q4TKKc2UILdtisacQi1FsYkt0QtrlRpf1pg7QGdRAcBMMilx5I39AgRhINUITNXr98V9-y2RxXB74YmLJEB0cgCKDKqUW4AiORnA32YVDdtD7HWarZrMr_b7teYC_ObZftE5t5EMqllRUKlShi51lfhFyEbeMTLdCQiKgIy3MUH6HrQL-lX7RETfRvl0GT6VxXUEMZ6rsRQUXh5LDsBB62BnIoZfDkHNVgfeOI3cLA2vnVge6_uEE-esr4ssFXhiKlNXkiBrErXuwriMJyIul_bUeOZDBbnPACRBSBjughWKWypzXN97Hn1GUKUvzjSpkDOXT6xthuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای سرهنگ بازنشسته تفنگداران دریایی آمریکا، مایک جرنیگان: ترامپ، در حال آماده شدن برای جنگی دیگر است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/695252" target="_blank">📅 19:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695251">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJYoUwHCZVeo6gnXpyC9AQ8zpx4GqmNzuDJaRzqeJCqgBLkQmsW_NjNmruUfUcDnUvjdKkdgLTDMJIK9FVIJSP-InRettgf7PSH0wcXa5XzNHcZ3iLKDLy-EzHTyL8yqtgSlMAnIi4pZDkXXlAOETiRV7Ga0DXodtKBpey5EOKV5Tn7UYZedluFjsKhp4ybB4F-0Tw5JXcl5QO_qZ1AsN8l7xyc5jLOgFSPF2OrFkemCYdxYHyFRVOM_-WFFHYzYRBFI-gtxiFXN-rUkQt_jgcYsm-T36k4tPQUx98s_A8VrX1J5VHvfgIigP5xVsgHDxWLCrphyM_EV2kjc_OCNXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزافه‌گویی وزیر دولت امارات: امارات خواستار پیگیری اشغال جزایر سه‌گانه تنب بزرگ، تنب کوچک و ابوموسی توسط ایران است!
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/695251" target="_blank">📅 19:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695250">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
ادعای الجزیره: فرانسه پیش‌نویس قطعنامه‌ای جدید درباره آزادی دریانوردی در تنگه هرمز توزیع کرد
جزئیات اعلامی:
🔹
آزادی دریانوردی و حق دفاع کشورها از کشتی‌هایشان
🔹
حمایت از راه‌حل دیپلماتیک پایدار برای درگیری‌های منطقه
🔹
تشویق تلاش‌های داوطلبانه برای مین‌روبی و اسکورت دفاعی کشتی‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/695250" target="_blank">📅 19:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695249">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/181095730a.mp4?token=dzuC6hffYuabbHLI08i1ljGEN6ReG5q-yAySFOZTMzuRGm0Cd_Kt_GqSrQqlx2yHThkh33vqOKWd6GfxOA3mq-SefU8cpplD57xBAu0CuVcDxcjVJlMeukELb0f4NkR46hLHcD3arayzfdyyL-B7DwFs5NymA2IoHU_OHlK3XSlY7YoRr1tYJE2lZ-GcU9hDu7BM7rPtc1O4dXS70P-1k9l3iV7FvM_whWfBsckfCD46B0wm0fFRsvpdKtC6gfzx4t1w0qzw6P0PJ3ssiwEFGyaITcwP58LnHNhf0ExwPAslOPeSzsZ9tvy3ZQhHSGHKMcULnd-HImzn4MQDGeIhsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/181095730a.mp4?token=dzuC6hffYuabbHLI08i1ljGEN6ReG5q-yAySFOZTMzuRGm0Cd_Kt_GqSrQqlx2yHThkh33vqOKWd6GfxOA3mq-SefU8cpplD57xBAu0CuVcDxcjVJlMeukELb0f4NkR46hLHcD3arayzfdyyL-B7DwFs5NymA2IoHU_OHlK3XSlY7YoRr1tYJE2lZ-GcU9hDu7BM7rPtc1O4dXS70P-1k9l3iV7FvM_whWfBsckfCD46B0wm0fFRsvpdKtC6gfzx4t1w0qzw6P0PJ3ssiwEFGyaITcwP58LnHNhf0ExwPAslOPeSzsZ9tvy3ZQhHSGHKMcULnd-HImzn4MQDGeIhsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری بیشتر از شدت طوفان و گرد و خاک در قم   #اخبار_قم در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/695249" target="_blank">📅 19:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695245">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QcpME37wulqdpHF6xusu6NL0xyUScUha6DdhiSVx_vHggKUzcFyCy4MNknmHg8CwLqTa3hRhM35IU5vcsyY9qGmuq6gNBWKT7jna3XRESFV3fsZGLaUWg8gUSHZHVT25YAId1yi9tc6l7D_EnjcR14CuC0hH80IfuwwTeFcP-aV_Uqs3iwHUoJ_HOXf0QaLrqEZEjoCRrmmIP3hIV4BmTKn3PMnDO8Th71e2YjM9S3yqgmxDekbY2X_fhK8ocWWUW7B2G4WaaUaWGjEiLsHut6_JH5qWLk3xdNdzDjkAJL2gDI_ITzCE6q0gmObmz5Wrw2E_KVnoHqMUZEIJ-CQIuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MumsGHTECmlmUMq--4UJq0lgE_AMlG0q91zi8aX6tfbdgQ01EYSfQpzLDwf7DgLhU3DsEsYBvP3Te0HhO-6PSrREGucGSlaQvNJBD6Hoh5WvPNoklZk4V2Vl5WBarTi6Rh_tATBf5mv-TRDZtraX5BhtbOg76HbrFRZk08ad7ssLxCuL1pVKXsOLIw-jGUoouin-QZ_5TuVQHMKNhqcBbfnjIo7pCZWyncNOkZxUBRJ7uNW7kIdQQ_e0XYwed8JT3MADUu6vDgNU6IFVx9B0Il4aWc2QgLkTC7kcUXYGhMMWI0PgxzHu9eiF6fFNlAlUOx20Pxq2KVUpUOnLOTomcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WDTWjk_Qg0RUO5-SQC6UDRzETg0OEFINQO0CwsJ9JBPgQf3NHpKpY1CNPNcTYJjU1nhjuaEQuuBwDgNU1dxkxgUMM5p3vkA9PuOCugTaipY0tUWUPpjZWxEKBbKx6fXjm0g83o_a6xY0nR6Ahp4jsK4Xp_XDHCKurs-4S0FJxKiz-qKs3CxZxmNtxqe_THIHnKaGr3hBE9wzQ-DLTgMd05n41BYsAcsfHz1abOoLhvgLDAMUKHcAl-jHbjlvxiOJppWGmY2kRGdPAnrqbPfeSpd2iOZdjpv5dZlE8zLde2Eu1G4-84Kw5uXIEQHO58WSNk9CjxNfo6EqW_mhKk6T0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YboScde2vF2O8R5qb5E9O3E9jAS5QigeqIcu28VKaSGWpyPfFrsllTtDPvzVyPK24Pt3JajvYqIwn5xCvthnnYCkkwRnYVDgyYCHl0jMt1YXXhJkCbX1nglfocKvBmNarze8leSCPmoKe31B-XaertvevL7NdqoEpP4cx4udJ7nTC1Qb06cxu6Zs-2PwcCnfkaykZ_ioqgnOZYdKtVqyqlqCuQkOdD2V2YeWDkWGeTreRVmDDUyYk9AQaQ_2xxaUGlnVt0t-5c8SDiDKbU7DizsR-ey3nqWz4VrZFOgP3mYKxaNgCz2WTNPBFpMQFr42LOMhxFKWEG9vBjo8hpK-uA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری باکیفیت از خسارت‌های به‌جا مانده از پاسخ ایران در پایگاه شاهزاده سلطان
🔹
پایگاه شاهزاده سلطان عربستان سعودی میزبان هواگردهای آمریکایی که از محل اسکان نیروها، سازه‌ها و آشیانه‌ سی۱۳۰ توسط نیروهای مسلح ایران هدف قرار گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/695245" target="_blank">📅 19:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695244">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43cb2e134a.mp4?token=Fz08XNSE4GA2ijfHGarMP9qxPQ_erwFvxErU3oF54IlI8xtt7mMvaXFX96HFohP5cu-DQ5r-kWgCJ3-02FNlTIMFzBWOB-g9crrS0wDnoq-mhvn7WKmZxg_xezHTnJSfDKxwmDQDzWfty6AZsukln2MhPwTfv1diVSWjVDVEmfpU6QK66Ks6e8f_4eMaeO0D7mEV3Iv_3tzeNBa0JDQxYV3OPOYWAPMJGbj_TYadbpdmIN4jZy1LRfIsGSNNG7-eZ__-Zo7-jI-5EbMiPIJChuRSRSLCggvcByE44N4As8VrXDF8G6k4-wJa79lPhV7d6WIyywmTBLDmfEGNG82qyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43cb2e134a.mp4?token=Fz08XNSE4GA2ijfHGarMP9qxPQ_erwFvxErU3oF54IlI8xtt7mMvaXFX96HFohP5cu-DQ5r-kWgCJ3-02FNlTIMFzBWOB-g9crrS0wDnoq-mhvn7WKmZxg_xezHTnJSfDKxwmDQDzWfty6AZsukln2MhPwTfv1diVSWjVDVEmfpU6QK66Ks6e8f_4eMaeO0D7mEV3Iv_3tzeNBa0JDQxYV3OPOYWAPMJGbj_TYadbpdmIN4jZy1LRfIsGSNNG7-eZ__-Zo7-jI-5EbMiPIJChuRSRSLCggvcByE44N4As8VrXDF8G6k4-wJa79lPhV7d6WIyywmTBLDmfEGNG82qyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زنی که دو بار اعدام شد و زنده ماند!
🔹
کریستا پایت، قاتل همکلاسی‌اش در ۱۸ سالگی، ۳۰ سال است که در انتظار اعدام است. دو بار تزریق کشنده، دو بار زنده ماندن. دستیار قاضی: یا روش را عوض کنید یا جوخه تیراندازی.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/695244" target="_blank">📅 19:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695243">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32ba9bdbdc.mp4?token=VbtLRCzRqs5v3tpk-grVTUX_VOe-o7y7A8TWJcv9IPf29uYS-99rWOUHHAhK0V7b7UU_16p9kl8P31vvGNHjKky3q0EpO0ia0UimwJacaw2zufWViCmQAthQQwQ3YRXgY44FXIOFTFuJpVAIiEjqBNV9WrCDvu8OXPCJrXYu45MGecumlq5-g-K_-Qj724xNCAQ_oJuAdxeO1S9LZFKHKik-WkHS7_GKaVgoKm5F1FRJo5vNgJqhTqwudcskGz4bE0XTxmH2eWqu2py4GJ5gPnth8z6cPCrVjzoInI8sVnknzMk_LO2iUT0LuZwCMAh2CaTKGuU4EZ7XpQMgwGg9lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32ba9bdbdc.mp4?token=VbtLRCzRqs5v3tpk-grVTUX_VOe-o7y7A8TWJcv9IPf29uYS-99rWOUHHAhK0V7b7UU_16p9kl8P31vvGNHjKky3q0EpO0ia0UimwJacaw2zufWViCmQAthQQwQ3YRXgY44FXIOFTFuJpVAIiEjqBNV9WrCDvu8OXPCJrXYu45MGecumlq5-g-K_-Qj724xNCAQ_oJuAdxeO1S9LZFKHKik-WkHS7_GKaVgoKm5F1FRJo5vNgJqhTqwudcskGz4bE0XTxmH2eWqu2py4GJ5gPnth8z6cPCrVjzoInI8sVnknzMk_LO2iUT0LuZwCMAh2CaTKGuU4EZ7XpQMgwGg9lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساسان زارع سخنگوی ستاد مردمی جانفدا خبر داد؛ تشکیل ۱۰ هزار یگان مردمی امداد و نجات با مشارکت «جان‌فدایان»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/695243" target="_blank">📅 19:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695242">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
آموزش گام به گام اعزام به خدمت سربازی
🔹
آماده‌کردن مدارک: کارت ملی، شناسنامه، مدارک تحصیلی و مدارک لازم.
🔹
مراجعه به پلیس +۱۰ : درخواست اعزام به خدمت رو ثبت می‌کنید.
🔹
دریافت برگ آماده به خدمت: تاریخ اعزام مشخص می‌شود.
🔹
انجام واکسیناسیون: واکسن‌های مورد نیاز رو می‌زنین.
🔹
دریافت برگ معرفی‌نامه: محل مرکز آموزشی مشخص می‌شود.
🔹
روز اعزام: در تاریخ تعیین‌ شده به مرکز اعلام‌ شده مراجعه می‌‌کنید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/695242" target="_blank">📅 19:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695241">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b4c5ac571.mp4?token=ukvVwCsT4OwaPKjGO-jZR3lBeYNC7K7147SI0cRAfRWqK5uUnmxkPeNEnKqg06jXlmAwVDxSI882Twotz4e-RWL3DxJsWap_q19y4gzwNBb20hEe0wEyOzyyYkbop4Zvg2_wwUQ-XBVRAQxnmw3JBCm_0Ey6yj7qohCsyt6s96CPDG3iCPvvGrj9GBq91D06GzPa_LMq3Suzo2c8SWVgpnU4WhZq0PP-I7fajfUMAanjzuLzKN5DJYcjiV9wvVsGuXRnKBeOj8eoIIkGWUE4L67FyyIWmWLdyhZR2Txi1o9IbOLwJP3d6oEEMxK98H_WgQIu994NSzwAvG0l3dL27g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b4c5ac571.mp4?token=ukvVwCsT4OwaPKjGO-jZR3lBeYNC7K7147SI0cRAfRWqK5uUnmxkPeNEnKqg06jXlmAwVDxSI882Twotz4e-RWL3DxJsWap_q19y4gzwNBb20hEe0wEyOzyyYkbop4Zvg2_wwUQ-XBVRAQxnmw3JBCm_0Ey6yj7qohCsyt6s96CPDG3iCPvvGrj9GBq91D06GzPa_LMq3Suzo2c8SWVgpnU4WhZq0PP-I7fajfUMAanjzuLzKN5DJYcjiV9wvVsGuXRnKBeOj8eoIIkGWUE4L67FyyIWmWLdyhZR2Txi1o9IbOLwJP3d6oEEMxK98H_WgQIu994NSzwAvG0l3dL27g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
الهام علی‌اف، رئیس‌جمهور آذربایجان: آمریکا و چین دو ابرقدرت جهان هستند؛ ابرقدرت سومی نیست
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/695241" target="_blank">📅 19:23 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695240">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dd059bda8.mp4?token=gqOp9Kq9Qgh_bPfWpapIS_6f3IiZahmRF-xaLankk6T2QJjmWk_VuuTdSy38ur2TXbPrHsZmfNCX0sCFsSIwju3qwF9pQEPhXrODqJbCK2bB0uPyHFuQTX5jzcc6s9W4X46ySV3iJGHEa3ruVE4wU4CCATqW2CU6nAsjN6VpCiAqaD9gTFCpAqKXcQhhSCRtCQ7RwMM28gOm1fbsKa7KSz2RQir2PAsYhlHt4tksGyGnglCtS1LmoAelzdAXy3PyoDIVkMiQQZ9iPF3bmgzIzcOYiht_UAmtakqTRZH_SpPEZS9WFVaJQ6cShJhV7b3Ps6D04l0C35E8uB91H_MhsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dd059bda8.mp4?token=gqOp9Kq9Qgh_bPfWpapIS_6f3IiZahmRF-xaLankk6T2QJjmWk_VuuTdSy38ur2TXbPrHsZmfNCX0sCFsSIwju3qwF9pQEPhXrODqJbCK2bB0uPyHFuQTX5jzcc6s9W4X46ySV3iJGHEa3ruVE4wU4CCATqW2CU6nAsjN6VpCiAqaD9gTFCpAqKXcQhhSCRtCQ7RwMM28gOm1fbsKa7KSz2RQir2PAsYhlHt4tksGyGnglCtS1LmoAelzdAXy3PyoDIVkMiQQZ9iPF3bmgzIzcOYiht_UAmtakqTRZH_SpPEZS9WFVaJQ6cShJhV7b3Ps6D04l0C35E8uB91H_MhsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیت هگست» وزیر جنگ دولت تروریستی آمریکا مدعی شد: امروز نفت بیشتری از تنگه هرمز عبور می‌کند زیرا خلبانان شگفت‌انگیزی بر حریم هوایی کنترل دارند
🔹
این در حالی است که هر روز چند نفتکش در تنگه هرمز هدف تیر غیب قرار می‌گیرند وآسیب می‌بینند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/695240" target="_blank">📅 19:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695239">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hif6KRxOFMCb31odca_ziE8_v-_HnA3mFK991-2G73FuKYG1XmtPFJ3GoXOP9YooqF2OwILuoyBdrbZLg_Dz8p4xDKYu4KGs1k-WlNJ6pM072k3ooGrBdqDul_dzIdv_h4cXfdnj1oDyQzagFLN_GBhozxy2B7g8RN5cgZ4f_VeqQAm-Cpte7lXcVvnn4nOx-hpJCHOIg44O46qwZ7f13wYpA7WGmjZFs2wkT31bsis9M-HI4633jHDdJLQUxU8Drcwm7pTgnwMqmL-_tTA9bfPp-G9Nl7dJgWGSQbwhSAxhIk0Ug7qI6nAhBZW4Z_h3l7LrRDtnsmsN1w9I74cOWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چیزهایی که ایرانی‌ها خیلی قبل‌تر از تصور ما ساختند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/695239" target="_blank">📅 19:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695238">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/444bcd3338.mp4?token=s64hZDapL0HHP8doRXEpEaJzPW5kl6QeVp1sICOCEvbp_C17Gy9aNTF7TEsAfyzUchYoQAxbOsyp6TQsylU1-FOrSYy0LlowvPdzGGCFGD2PR1nVdYI7SyM9DRillL_F_nrXMAPq031eo5TVr-m2ywwwsUhFopqkpaeeMccfv7Wc9OtEBk-txLLXsb12aiLLTGyFmzaUowOWzjSauu32zIEHf5yS9W0ect7GziE15MLz5BooTWdn9TQCZsfIoClXndzndQdaZKZvL3COeLpcy5GLQnMqpsSe7h5U6azQhOG80pTGILVCnyCxUCOvWI6_jFpPkeGV5a-KdFthnVe4GXEwTd_yx4sT1uAwNX0lWhJeZRnNBG2uR_5xUS28HmRaM0SzA35_GyqRJD6CcmEg6kQWghdvVa5K_lFuW0A5NeAzSvtLSn6Og1ZJWmQIgdP8_G9UrrlQfT-LAFv4EGXYxZ_sZVge1P-PRr2CigRjRQai8cNIbjLgD4nHDm5y1DqyaPobeDGBarY-TXefYSHzlWzvmRXFoIjVao1JKFuzWNajy3-HMELm_JqmcTl2bWkyrDShIoGW5578_9ok0oLXV6k0mTIh10LFabbjYjl2ZYM9guqMsy0NdQkVFAEl0U9Zd6p6KBHLXsoJnYnstIJVaYKgMhbM93_GoF44hRyeWks" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/444bcd3338.mp4?token=s64hZDapL0HHP8doRXEpEaJzPW5kl6QeVp1sICOCEvbp_C17Gy9aNTF7TEsAfyzUchYoQAxbOsyp6TQsylU1-FOrSYy0LlowvPdzGGCFGD2PR1nVdYI7SyM9DRillL_F_nrXMAPq031eo5TVr-m2ywwwsUhFopqkpaeeMccfv7Wc9OtEBk-txLLXsb12aiLLTGyFmzaUowOWzjSauu32zIEHf5yS9W0ect7GziE15MLz5BooTWdn9TQCZsfIoClXndzndQdaZKZvL3COeLpcy5GLQnMqpsSe7h5U6azQhOG80pTGILVCnyCxUCOvWI6_jFpPkeGV5a-KdFthnVe4GXEwTd_yx4sT1uAwNX0lWhJeZRnNBG2uR_5xUS28HmRaM0SzA35_GyqRJD6CcmEg6kQWghdvVa5K_lFuW0A5NeAzSvtLSn6Og1ZJWmQIgdP8_G9UrrlQfT-LAFv4EGXYxZ_sZVge1P-PRr2CigRjRQai8cNIbjLgD4nHDm5y1DqyaPobeDGBarY-TXefYSHzlWzvmRXFoIjVao1JKFuzWNajy3-HMELm_JqmcTl2bWkyrDShIoGW5578_9ok0oLXV6k0mTIh10LFabbjYjl2ZYM9guqMsy0NdQkVFAEl0U9Zd6p6KBHLXsoJnYnstIJVaYKgMhbM93_GoF44hRyeWks" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درخواست مردم دیگر کشورها برای پیوستن به جانفدا در جنگ با آمریکا و رژیم صهیونیستی به روایت سخنگوی ستاد مردمی جانفدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/695238" target="_blank">📅 19:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695237">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/162a2a67d5.mp4?token=Wq-awkcF8g3XNs6Ecp2r0kEVDLVR5pBhVv2L-3XJHTOhtsMpWj0v9l4ylglp0YBdCtDNsmFuLikxqFXAtZNpj4diQShIg5wmmuNyIlllhjemcha6KthEvehAWAVJ86IW6sfAXXWRD8w6f7gbU99mxBExQTBJ_FGF14XwDouBiXQuVhk1h2mB6nd1Y48qppGAbJMacDnD0qY_86uiEvc88Al_du2MhZt4sBCEel5cQmO8srRYVDQWrZ81dSJyN2Jh4Jq8UxMCeTuX-kMQU_pc3rFsc3u9HcpsPhl9rvDt6wypkgUWS26Hqd1ILa20sGy3OZfkSbNlDIvtwpwo8__mJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/162a2a67d5.mp4?token=Wq-awkcF8g3XNs6Ecp2r0kEVDLVR5pBhVv2L-3XJHTOhtsMpWj0v9l4ylglp0YBdCtDNsmFuLikxqFXAtZNpj4diQShIg5wmmuNyIlllhjemcha6KthEvehAWAVJ86IW6sfAXXWRD8w6f7gbU99mxBExQTBJ_FGF14XwDouBiXQuVhk1h2mB6nd1Y48qppGAbJMacDnD0qY_86uiEvc88Al_du2MhZt4sBCEel5cQmO8srRYVDQWrZ81dSJyN2Jh4Jq8UxMCeTuX-kMQU_pc3rFsc3u9HcpsPhl9rvDt6wypkgUWS26Hqd1ILa20sGy3OZfkSbNlDIvtwpwo8__mJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای حجم آتش‌سوزی‌های رخ داده در پالایشگاه آرامکو در ریاض را نشان می‌دهند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/695237" target="_blank">📅 18:56 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695236">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee328bd43.mp4?token=NgU9_t07vpjvsUfAe5nLP7TLa6I-bPE-UKdE0KKaTJU1CvL-sToSpg3OauMrrMWH6JBJKvpBC-rTPsF4KA6cw-kjSDvXMhXNzTDr5Kb6p3fFPyq7ezCQtr_s3nNXoh-um47vYf4jo5uzm49u_K7JPfHfH1BKwBFs0MyztV3dcLXQ7AwFXaC4vBHgq8-hHEWp0f--kjjGYgwr-h_YS_M7Uu8jJzdg-O-8uwlcfb2i5r4s8bZwJYK-Oxsxf3u0DqKB5hQ04ncEXqisoeUJhQCk1aMT6SnfoKQQpH8vPyq1zPA1vzinmv6aZU_ReA176zpKw2u60YJC4gaHLyycl3Xyxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee328bd43.mp4?token=NgU9_t07vpjvsUfAe5nLP7TLa6I-bPE-UKdE0KKaTJU1CvL-sToSpg3OauMrrMWH6JBJKvpBC-rTPsF4KA6cw-kjSDvXMhXNzTDr5Kb6p3fFPyq7ezCQtr_s3nNXoh-um47vYf4jo5uzm49u_K7JPfHfH1BKwBFs0MyztV3dcLXQ7AwFXaC4vBHgq8-hHEWp0f--kjjGYgwr-h_YS_M7Uu8jJzdg-O-8uwlcfb2i5r4s8bZwJYK-Oxsxf3u0DqKB5hQ04ncEXqisoeUJhQCk1aMT6SnfoKQQpH8vPyq1zPA1vzinmv6aZU_ReA176zpKw2u60YJC4gaHLyycl3Xyxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمک‌گرفتگی پر و بال، معضلی جدی برای پلیکان‌های سفید دریاچه ارومیه
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/695236" target="_blank">📅 18:56 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695235">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/259f28e509.mp4?token=Evu_CWBzimIP9Lhusc__GXO8pq91hKjMJZ5n02M1-IXronffPMlctEaXC9lAQWxC0wXVRXKe6jhdXm9BrlMhhDhuO7tmbkfZAQBoUqEyNLm7nm1qqUCco1K7bBPp4fAAZBRJGkORA0OvAikk5NcNM1O5QXVRedzgv5iTTGaRBwFXPjeIuLq_cuu8YRhqjCWwQKxtCUwomW7RPGZXWjIgAdZKOCMeKK_lDReMMniQC6w6KaR1hMocZGoXd1PV0C7N9y0BMIDzsVhPiSG8jWUoCx29PqH2T5ktyRBE6_5iiZZY5uFvtROdsrlsB0e-FlfszDJXO-ro3HEs1qUm9wXDCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/259f28e509.mp4?token=Evu_CWBzimIP9Lhusc__GXO8pq91hKjMJZ5n02M1-IXronffPMlctEaXC9lAQWxC0wXVRXKe6jhdXm9BrlMhhDhuO7tmbkfZAQBoUqEyNLm7nm1qqUCco1K7bBPp4fAAZBRJGkORA0OvAikk5NcNM1O5QXVRedzgv5iTTGaRBwFXPjeIuLq_cuu8YRhqjCWwQKxtCUwomW7RPGZXWjIgAdZKOCMeKK_lDReMMniQC6w6KaR1hMocZGoXd1PV0C7N9y0BMIDzsVhPiSG8jWUoCx29PqH2T5ktyRBE6_5iiZZY5uFvtROdsrlsB0e-FlfszDJXO-ro3HEs1qUm9wXDCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طوفان و گرد و خاک شدید قم را فرا گرفت  #اخبار_قم در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/695235" target="_blank">📅 18:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695234">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d3228e40c.mp4?token=HHAozP6yf46yqZLvEUx7BMXmTBO-K0eYE_txs84DLVeCg9yBurQRwR08fqJBk4-GdeQep7Msah9dMZvYgvwMXR3H_iLfs5EYjrIhnZft_n4n0xrp27Cp_dfLxnxtGtbkckQHw2v6eFd_dftW8wYUAv986GuVZepdrHi4Ddxpuwtrx4d8RgOLdBZiTL8S47W3-K37bqFbWaGzte3vW_-Bgyn7QBST6N-Zby8azuQol_dK4fU7qd2pVJqkbKJV6VXQLqolY2xH6cfALTouPCB46ijSlFLD8GS5RowSYI_cx5n_zvmxgwqHppO-Oy8sjBvUMnbgZUm4wl0xVfpymRp_Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d3228e40c.mp4?token=HHAozP6yf46yqZLvEUx7BMXmTBO-K0eYE_txs84DLVeCg9yBurQRwR08fqJBk4-GdeQep7Msah9dMZvYgvwMXR3H_iLfs5EYjrIhnZft_n4n0xrp27Cp_dfLxnxtGtbkckQHw2v6eFd_dftW8wYUAv986GuVZepdrHi4Ddxpuwtrx4d8RgOLdBZiTL8S47W3-K37bqFbWaGzte3vW_-Bgyn7QBST6N-Zby8azuQol_dK4fU7qd2pVJqkbKJV6VXQLqolY2xH6cfALTouPCB46ijSlFLD8GS5RowSYI_cx5n_zvmxgwqHppO-Oy8sjBvUMnbgZUm4wl0xVfpymRp_Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مدل جدید Fable 5.5 در ۱۵ ثانیه آثار هنری ۴۰ هزار سال تاریخ را ساخت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/695234" target="_blank">📅 18:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695233">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7e6a788a7.mp4?token=cXhbRIeyUZOqhi-hHXDchFBoKfSV2ZvYObUzZvzlp6MkSqqf7gP8jk-4qhGzXL0uGaiV7kRxCeumegOOlVxSYaYtOG3DudGoELB3Oz5PnghMdnyhrRcQwZMV7zcduIM1rAH083DKQMPRfGZ4gL9-4njEZeNvLouQ8LBAGn4NbjfKA_lrWfEbpCiDC09hcfd6M2xHVfdAzVxLijPBFKbBy_vtZmfwpezIAGBUmtY1aDmiVjqtIND17ncxN18ktMXyAJndPfUDN4Nj-J7V-EUBQmlEoG8cP0GjSWwMljR7nb1q8EmpCxkrgNQRCPhUmiGEzIhxTH5nA4yVwG4izeh-LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7e6a788a7.mp4?token=cXhbRIeyUZOqhi-hHXDchFBoKfSV2ZvYObUzZvzlp6MkSqqf7gP8jk-4qhGzXL0uGaiV7kRxCeumegOOlVxSYaYtOG3DudGoELB3Oz5PnghMdnyhrRcQwZMV7zcduIM1rAH083DKQMPRfGZ4gL9-4njEZeNvLouQ8LBAGn4NbjfKA_lrWfEbpCiDC09hcfd6M2xHVfdAzVxLijPBFKbBy_vtZmfwpezIAGBUmtY1aDmiVjqtIND17ncxN18ktMXyAJndPfUDN4Nj-J7V-EUBQmlEoG8cP0GjSWwMljR7nb1q8EmpCxkrgNQRCPhUmiGEzIhxTH5nA4yVwG4izeh-LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ارتش، پای کار جانفدا
🔹
دومین پایگاه آموزش نظامی و امدادی جانفدا با همکاری و محوریت ارتش جمهوری اسلامی ایران افتتاح‌ شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/695233" target="_blank">📅 18:44 · 11 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
