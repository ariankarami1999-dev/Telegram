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
<img src="https://cdn4.telesco.pe/file/YUoH69Vdj4udi-rPH0tDbJPYDXXM1ahcTRg09dYIwqgYE6tlC8hn1NgyoVjLB4ge8R928UTdVlBiaUNbpgXfdLPg5ThxgTPGXjFMpXamt3AfRdU5VGlVt9gV3qpA5tkKtOHErmVbbOIubJqZq0s5KU9xYRIF0sB7uNJif6q5J-RDJL4SAANK-V7y_gy94Uqi_n2JyeyHnsQrtDpFIdaOUY9x5HeSMHBd_iUt82yOYfVHNnrQnYVDvbYHh3tvOqUG6h_FWBXEfxaOE-iGQ_l3hQv2YzZnjdF6dP5mwse5a3tz-0LNJD7QPdyiupz9UxDBPqPSCvrSce7TPVgr-uSIig.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.43M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 05:04:34</div>
<hr>

<div class="tg-post" id="msg-696781">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14b1c7cc7f.mp4?token=SBXjTW1u_YkdAgnq-NmFEZDJeYUyq1UA9hfVZEGsF86nNSx6jffqqg89FMrvEMijHWdL-pupNyGoEaJwYkpLeEJ295fstnNAQ9luJSuevl95cpZeESTbycPAre57r10iwuO2HomeKCIwUS9ODCBZ01bAlR5QHXAOUp15ec4uHU9PBPIjvR4kZ6v4yF2ydvZwA7tA8ayoijoGBcJm1Fs1i1e3pai0eLMEwIqlYJxxwaXWwqtNnraRppeMeljuNyvyRCfoY0T-hOdWOjz-D09dX-HZJ1aaZ_1D72SNrLWbYwANy80o6s8Tb5n3ifaQU6XUROySyG57iIzp5vXPtN3rMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14b1c7cc7f.mp4?token=SBXjTW1u_YkdAgnq-NmFEZDJeYUyq1UA9hfVZEGsF86nNSx6jffqqg89FMrvEMijHWdL-pupNyGoEaJwYkpLeEJ295fstnNAQ9luJSuevl95cpZeESTbycPAre57r10iwuO2HomeKCIwUS9ODCBZ01bAlR5QHXAOUp15ec4uHU9PBPIjvR4kZ6v4yF2ydvZwA7tA8ayoijoGBcJm1Fs1i1e3pai0eLMEwIqlYJxxwaXWwqtNnraRppeMeljuNyvyRCfoY0T-hOdWOjz-D09dX-HZJ1aaZ_1D72SNrLWbYwANy80o6s8Tb5n3ifaQU6XUROySyG57iIzp5vXPtN3rMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🎥
#_این_کلیپ_را_حتما_ببینید
سلام و عرض ادب و احترام
💔
یک بچه نیازمند 2 ماهه ساکن روستا داریم که مبتلا به بیماری هیدروسفالی شده و نیاز به عمل جراحی داره،هزینه عمل جراحی160میلیون میشه ولی هزینه شو ندارن و بچه داره عذاب میکشه‌ و روز به روز سرش بزرگتر میشه و باید هر چه زودتر عمل بشه
😔
😔
🔹️
این بنده های خدا هیچ کس و کاری ندارن،امید شون اول به خدا و بعد به شماست تا کمک کنید،فکر کنید بچه خودتون هست هر چقدر که توانایی شو دارید کمک کنید و بفرستید به دوستان و آشنایان تا کمک کنن،خدا به مال و زندگی شما برکت بده
💳
شماره کارت
#رسمی
بنام قرارگاه شهدای گمنام(کلیک کنید کپی میشه)
5892107050067480
📌
جهت اطلاع و ارتباط با مدیر قرارگاه
@Hoseinfahmide313</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/696781" target="_blank">📅 00:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696780">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHo62uvjaiO5Kwg6l7xxUsDVAr4NG8W2cx3q9fYyUCIuNGQpIdDi4Gt9Zy6o2t53gA_Bf_YzKXirRHMLS4GX_BmXFo6OB6CKW-y29l09aIQIQD28lqE-PVX4s4EuEfOX8wNxppOV56c9ZfYtiSclJ74nJAz9X7XWB8w12tKLrwvVBV7abqjr-94fyOGnX7_6GL6BW-6Ebn-FolDWKUgWi-DQrW4Y_sLVty4jXhqdikbKRz9s6RUUUu9OxgemqeiNyr4zpoh_H0n9YDLpSEGdJ7WhE47boU1-YeY_21VxdvalUdXfCS5lKCAgqgs0sjhnvr1CGbZ5CJofbVtzPJ8KNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏁
استایل اسپرت، شیک و آماده برای هرجا!
🖤
اگه دنبال یه ست مردونه‌ای که هم
خوش‌استایل باشه، هم راحت
، ست
Motorsport
رو از دست نده!
🔥
👕
سوییشرت + شلوار؛ یک ست کامل برای استایل روزمره
✨
طراحی اسپرت و جذاب با رنگ مشکیِ همیشه‌مد
🧵
جنس پلی‌استر نرم و سبک
📏
فری‌سایز، مناسب
L و XL
🏃‍♂️
مناسب استفاده روزمره، دورهمی، پیاده‌روی و استایل اسپرت
💰
قیمت ویژه: ۱,۶۵۰,۰۰۰ تومان
💳
الان بخر، بعداً پرداخت کن!
🔥
امکان
پرداخت قسطی در ۴ قسط
برای خرید راحت‌تر
🔄
ضمانت تعویض ۳ روزه کالا
🖤
یه ست کاربردی که هم راحت می‌پوشیش، هم شیک دیده می‌شی!
https://memarket24.ir/product/fast/47547/180124/</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/696780" target="_blank">📅 00:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696779">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0f0xWrgqOCIp6_BMn_MpWHsForZH2Y33su5WK0MIVLZ9do_K-_jV4KwuKHB8Oge2f5W_C_2nyZe3BQzariXjaLyzZNJ3-w6iIPz9rqlZSX5Ojx9A_ruheRpRPjgBG1QuyifA3MIOhlb3ZqKD09AyZLF2PZBijyFjuzCl3VEdZGqF7wWYatvF1C7xtMxlKvhC4x1YrMtz_vb6rcWGwCc5xUkiF3y7zD_97EnLl1Ise5aIv4ZtZoQjg6m7ijVpm8d49hqLvd0FSV8pqbM2GlCIyHmeRQb8y6CAMKRBmrXrBmjMNw_tKQl-gTMkc2jB6mvoAv7Fc8MmFBqfL__gLF9Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
‏
به نظرتون منظور شهید لاریجانی چه کسانی بود؟
‏چه کسانی در داخل، به ترامپ قول همکاری داده بودند؟
🔹
‏شهید لاریجانی: ترامپ تهدید کرده بود بعضی‌هاتون از داخل ایران به ما پیغام داده بودید که اگر حمله کنیم، به ما می‌پیوندید؛ اگر در این شرایط نیاید، لوتون می‌دیم.
در ویراستی خبرفوری پاسخ دهید
👇
https://virasty.com/akhbarefori/1791479390834090361</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/696779" target="_blank">📅 00:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696778">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef79e239ad.mp4?token=eQX-tsZXPRflbjzfPWtecRa2my-_zJFK6md8GNhFjMekrxG_vHsupSRyaSKXgz4XbzbC2DZq7BD_XbYNgvWy11SsiUWHWUO7pyCMMqt2bCqpoL7QWXbGX8I9DjqQXiXsIpQF7GOMAcJabgJzkQkntoq5BX8diFak4YCTc1jtIaK6c8jSl_ZUX5_CTRIICpVuVy968H63wKjsAy5DtUlSojQAjzPj_P9rRHsJQU2wVEwV21FUbDiFhf4oTZy1Nm4xkn1TK16d00VC_GfqyXC6Tv-bfOy-Oi1fmZU_4Z01GGDVKQHGJ_sTH3rwkJBi3xYrrT6Idy01SKAJjx9zOJYaNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef79e239ad.mp4?token=eQX-tsZXPRflbjzfPWtecRa2my-_zJFK6md8GNhFjMekrxG_vHsupSRyaSKXgz4XbzbC2DZq7BD_XbYNgvWy11SsiUWHWUO7pyCMMqt2bCqpoL7QWXbGX8I9DjqQXiXsIpQF7GOMAcJabgJzkQkntoq5BX8diFak4YCTc1jtIaK6c8jSl_ZUX5_CTRIICpVuVy968H63wKjsAy5DtUlSojQAjzPj_P9rRHsJQU2wVEwV21FUbDiFhf4oTZy1Nm4xkn1TK16d00VC_GfqyXC6Tv-bfOy-Oi1fmZU_4Z01GGDVKQHGJ_sTH3rwkJBi3xYrrT6Idy01SKAJjx9zOJYaNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۶ دقیقه مطالعه قبل از خواب باعث کاهش استرس به میزان چشمگیری میشه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/696778" target="_blank">📅 00:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696777">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PeR-rDVx0QJpUF9QH2y-plB6DVTthVX2R0oZiuwQwEqHROvKRne_D7clD7krf3uLeE6ehtytD-xZwLL3JvrpFjgf_Opu9LEgA87CfhFScArSAY_-TyVSjHdDK8tWPiHQys0qqJDGIW6_1MjibMur6AmCxy9O3IIlIpHrnHBqXuidNuK_gVtwx2Q15bnux80PqtyDhngPC5Uj8kFLEWxyWLDJKyzi-JVMyJNC0meB3XuDShzhLBqd-7v-AbXS20_37RAhQbwjmZkC7OjiJAMJC8zkP00OlXvUdqn3DejyjkafRAS1escM0OSoRf2FMbloVdexofoYVUCIhs5YuB-vVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طبق تصاویر منتشر شده، طی حمله یمن به فرودگاه بین‌المللی ریاض، دست‌کم ۳ هواپیما آسیب دیده‌اند
🔹
یک فروند، به طور کامل منهدم شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/696777" target="_blank">📅 00:22 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696776">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6883170c06.mp4?token=rbdOvZszcaYKi5wPs2dxMS3aqoGUL_p_Pew9TGeVyGx6tcSRDjGUPLK7MN2ia2Fi9w3DNvgYh0OLZ9V6k8qJ9sNtS4HSGjfyGvV70MiXoHzioSLySIdCqeuwtMB-R0PSFXu4OC1Doy-QNxy5s2_8WeOyikXmrvR8toh9uMVn2O5hOb271ZEHUqOmklG-FPyRF15j1P_qpRGMh7ZrKJlAc5pKCHeXVaZT62cLXis2hCVtkoBRwszW2PPSW8m5cV3DhXzagQ1sxkwTNNkvwMZvSn6tCvir1gzfLjIUO9tX_TvbKhRyGMxH2K0E7f4OJywSTsDxFySVga8nll1K3YqnlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6883170c06.mp4?token=rbdOvZszcaYKi5wPs2dxMS3aqoGUL_p_Pew9TGeVyGx6tcSRDjGUPLK7MN2ia2Fi9w3DNvgYh0OLZ9V6k8qJ9sNtS4HSGjfyGvV70MiXoHzioSLySIdCqeuwtMB-R0PSFXu4OC1Doy-QNxy5s2_8WeOyikXmrvR8toh9uMVn2O5hOb271ZEHUqOmklG-FPyRF15j1P_qpRGMh7ZrKJlAc5pKCHeXVaZT62cLXis2hCVtkoBRwszW2PPSW8m5cV3DhXzagQ1sxkwTNNkvwMZvSn6tCvir1gzfLjIUO9tX_TvbKhRyGMxH2K0E7f4OJywSTsDxFySVga8nll1K3YqnlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ملودی نوستالژیک گوشی‌های نوکیا؛ می‌دونستین این آهنگ ۹۲ سال قبل از اولین گوشی، ساخته شد!؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/696776" target="_blank">📅 00:18 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696775">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROSCVFn2M5xGk-3r88sh4VJsf_DwmbPxAa_AUbewgeHfoyF7SA6tqUlWUKMNIAlk5nhzXesycOSed9IAZ-w7sWkzHTFw2uS6K1qrVqnI7VyFnQRwhNw0YD5jpPcevMviVnDvr2x-He7G5jJmnN92lM707RWm0cpR6NwMdCjahH9XKPgPRds9ijG62wnS_pW-A-mjXx2-161NH_cVNOFxLSMP83GyV7SMDOsxc8lv54iFKAdq7WKyJqeSz6-WF4jgRn-8BBP7iMR2MFLkMieMOTkNbtkV9WgnuYJ_Yg_gL34kDw-6vaTA-xcqiYyaifXpz0tFAAbAQEVCICnYld5RLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توییت معنادار باراک راوید، خبرنگار آکسیوس
🔹
نگاهی به گذشته: در ژوئن ۲۰۲۵، پیش از عملیات «چکش نیمه‌شب»، کاخ سفید اعلام کرد که ترامپ «ظرف دو هفته» تصمیم خواهد گرفت که آیا آمریکا به جنگ اسرائیل علیه ایران می‌پیوندد یا نه.
🔹
اما زمانی که این اظهارات مطرح شد، ترامپ از قبل تصمیم گرفته بود به تأسیسات هسته‌ای ایران حمله کند.
🔹
در ۲۷ فوریه، کمتر از ۲۴ ساعت پیش از آغاز حملات آمریکا و اسرائیل علیه ایران، ترامپ ادعا کرد که هنوز درباره ورود به جنگ تصمیمی نگرفته است.
🔹
اما در واقع، او پیش‌تر تصمیم خود را گرفته و مجوز حملات را صادر کرده بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/696775" target="_blank">📅 00:14 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696774">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
وکیلی: استیضاح عراقچی، بازی با مهره‌های محدودی است که هنوز در کشور حضور دارند
محمدعلی وکیلی، نماینده سابق مجلس در
#گفتگو
با خبرفوری:
🔹
استیضاح ابزار نظارتی مجلس است، اما استفاده از آن در زمان نامناسب و مطرح‌ شدن استیضاح‌های متعدد، این ابزار را لوث می‌کند، به‌ویژه در شرایط فعلی که وزیر امور خارجه در خط مقدم مذاکرات قرار دارد و استیضاح او یعنی بازی با مهره‌های محدودی که هنوز در کشور حضور دارند.
🔹
انتظار می‌رود آقای قالیباف با توجه به مسئولیتش در تیم مذاکره‌کننده و اشراف بر شرایط کشور، اجازه ندهد فضای مجلس و کارکرد نظارتی آن لوث شود و انگیزه مدیران اجرایی نیز از بین برود.
@TV_Fori</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/696774" target="_blank">📅 00:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696772">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd532d101d.mp4?token=U5AGaNRISv4o0EbKBgeO5byt-Xd_hv9x1bGy6l5ossA_RgiMgAEen14VXlicTnHHbinE8i8d8ugqnIlS0eVUUfF5OMcI0J-B38pc727Q3WExO_fvckQUtFKhtP3HlBCZsnQghstF13Mi_WKbpTtaE4Y3S3zLpwLUBiwLKcCeSZ-Lr33moaqmUL2tvn148XjuWeyiiY8YzEYK4kf9dxMRzqdCeL2WuMXe-e4l7XL1bcVPR70PO5KGA71muo3IU7btXExGsL6k7q_EH5ku2gpQkE7a0zwMIXIG21jznurQd1Yx68pszzNaokLHLhQC3JwoQ7vatDYPDsQEyip24ZEpPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd532d101d.mp4?token=U5AGaNRISv4o0EbKBgeO5byt-Xd_hv9x1bGy6l5ossA_RgiMgAEen14VXlicTnHHbinE8i8d8ugqnIlS0eVUUfF5OMcI0J-B38pc727Q3WExO_fvckQUtFKhtP3HlBCZsnQghstF13Mi_WKbpTtaE4Y3S3zLpwLUBiwLKcCeSZ-Lr33moaqmUL2tvn148XjuWeyiiY8YzEYK4kf9dxMRzqdCeL2WuMXe-e4l7XL1bcVPR70PO5KGA71muo3IU7btXExGsL6k7q_EH5ku2gpQkE7a0zwMIXIG21jznurQd1Yx68pszzNaokLHLhQC3JwoQ7vatDYPDsQEyip24ZEpPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تازه‌ترین تصاویر از اعتراضات گسترده در خیابان‌های فرانسه  ‏
🔹
معترضان فرانسوی معتقدند بخش قابل‌توجهی از بودجه کشور به جای اختصاص به حوزه‌های آموزش و بازنشستگی، صرف هزینه‌های نظامی و ناتو می‌شود.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/696772" target="_blank">📅 00:07 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696771">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6jXd9jLoP6Nat_OorZBY5YiZV2p_243kUPUmuVNPaUCxe83X1frlYrVTNobXCdpx8jgPkYgOqmk9YWXAFeD8FV288sbI0HcePfY0UiL1mbBHy_9lQrMFknhZjR9raZ8vNvIbbMDWNYoqGw78j4tlmmxo9PP1is3PE13flitFR3KdSdFroS4vwDewTjO9N1JiF7668dUMEj1U10aaf8-sPbFmHyJdbmlDqk6V6pyc8LiV32Otljkf9OeQWNhvaZg-AmxlkHA6F6s0bQfetSPz70aa8lB1xIfWKA_pczu1Su8eBywIumNSwcxIzxVEP9DBE1cD6ah8W69bXA3IDNlJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیلگر ژئوپلیتیک و امنیت ملی آمریکا: اسرائیل درست قبل از انتخابات میان‌دوره‌ای آمریکا به ایران حمله خواهد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/696771" target="_blank">📅 00:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696770">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpGIfznEg66AcMuV56sbhbj3jPUFEfEvpOLMBCzqoaYhpUhE9gWUTaw8c2f35_Pke_jK9AxauJuRlunGUxho2maNRfKimxdOta5j6YkDXF9hNCeAdVmSXZqBvYlXv9A8MrtXQzpEpK5ilk1cDw0iRoEYR6i0gGrvhzhVEeLnUmMLUdIm2rLO_mOkWyM7N4HOUF7fgveuG6eR-nGk1JWtlra-p3mv5QFNfYoQsEfCx9xdHh0JuClezrjQ2hDBb1hPCA5SrtF3FTpSdh8A4wTdqpJ7ViXPLrJi2duL5lRjNs7Mr1feCgYN5RXLxqGDoRg9G_msd537aR_RKR_gOLeNKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/akhbarefori/696770" target="_blank">📅 00:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696768">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/620d948bad.mp4?token=RFJCSS326be71enLN2ckxO7ctCC_Jyiqr1i6T_GzxYZTsC-hAMFcUkMZ-WPiBhw4_w_LBIGOJowK8ZScZT0QP3K07JRWctUkSXXL02iZBIyP0q7Bm2lhqswGOyK00BfQOhTIIvL7lcMLGmkKkoXlnIlCQAvBaRJ-LACkTziZW1FhbBuKqR_9hJB_d3B5m_DUmibZaPnPtGba671wxxeTI6xY0H2ii4J-wLHva-4bOuCoBRgU3O-aSF-b9UNqN1aV1H5ajrL9A8UZqbQ4rC7_rhDU5_P4O-xU1DEkVYAAn_wzWsGembv3D9fXuD-J9P4PIX-Y0Tpqyx8vio9E5s2ltr4XYPjf3I2aEEhkEzMxjx8TUKW_vo2-qSFRzDTZuDKipcFJLXGBqk7uWuZChQfdsTLnuIW3k9otzxlxZyrsBxEdTo9dsJvHjrtfMlWhqkjUnuuiuTbECv9zVYNCPGtVlDC_dFsZ-Uom89y8pt7wvKLK-2g2kyh2Zvte_NtuCWuk-se93Hoc3bcvg1T5rcSRoy5tG3gnAUFCN4_BAyJlF2IiPAU4VMi8lqyW2lAKyt-mOone-C3jkD4lCO5iarpMq2TVLePEcmGQopwMA6JnK_uPAiu9LWa5MxcNqSkTnW0LfKIesyUrxb7hf8Rk6YIHO_ihFuzP-8SdNnkijKUeqAo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/620d948bad.mp4?token=RFJCSS326be71enLN2ckxO7ctCC_Jyiqr1i6T_GzxYZTsC-hAMFcUkMZ-WPiBhw4_w_LBIGOJowK8ZScZT0QP3K07JRWctUkSXXL02iZBIyP0q7Bm2lhqswGOyK00BfQOhTIIvL7lcMLGmkKkoXlnIlCQAvBaRJ-LACkTziZW1FhbBuKqR_9hJB_d3B5m_DUmibZaPnPtGba671wxxeTI6xY0H2ii4J-wLHva-4bOuCoBRgU3O-aSF-b9UNqN1aV1H5ajrL9A8UZqbQ4rC7_rhDU5_P4O-xU1DEkVYAAn_wzWsGembv3D9fXuD-J9P4PIX-Y0Tpqyx8vio9E5s2ltr4XYPjf3I2aEEhkEzMxjx8TUKW_vo2-qSFRzDTZuDKipcFJLXGBqk7uWuZChQfdsTLnuIW3k9otzxlxZyrsBxEdTo9dsJvHjrtfMlWhqkjUnuuiuTbECv9zVYNCPGtVlDC_dFsZ-Uom89y8pt7wvKLK-2g2kyh2Zvte_NtuCWuk-se93Hoc3bcvg1T5rcSRoy5tG3gnAUFCN4_BAyJlF2IiPAU4VMi8lqyW2lAKyt-mOone-C3jkD4lCO5iarpMq2TVLePEcmGQopwMA6JnK_uPAiu9LWa5MxcNqSkTnW0LfKIesyUrxb7hf8Rk6YIHO_ihFuzP-8SdNnkijKUeqAo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خواب مجلس در روزهای سرنوشت‌ساز خزر! / هشدار درباره باز شدن پای بیگانگان به دریای شمال
مهدی خورسند، کارشناس مسائل اوراسیا:
🔹
در حالی که دولت بررسی کنوانسیون رژیم حقوقی دریای خزر را به مجلس واگذار کرده، تعطیلی و انفعال نمایندگان، منافع ملی ما را در این منطقه حساس به خطر انداخته است. اگر مجلس نتواند چارچوب حقوقی را به تصویب برساند، با بهانه‌جویی کشورهای دیگر، پای قدرت‌های بیگانه به خزر باز خواهد شد./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/696768" target="_blank">📅 23:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696767">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51421db204.mp4?token=ALQpfysu7Rg1_6PUaqQ3MIbgPcR5AsipP1gkFH7-HfbfynoSNEBYjokb1XLfvTbx-_FTjk8yBFpwYec0XzfSMaqCJe4e6xlD9hxwb209xohrHO9A5hzCz3HXHh1U5B4RN9_7q3Kq7wV0N47vqTVhTIlChujm_aBCUkCx1ZrAVL3F0l09z87NDbi2yzX7nFGDW6i6_pmxEey8VX427ogJflx-mh18Ryr0xD5d6CYJIzhronghmQywUJ_m26qzNUg40NJB7k-2t5LM1z_vNBF1LVdgd_fs_MgRoHIln0AtL0XSsXYQgzFvAWCDkek5pmKiBc_tPPLWY8jCeSfMbdbLpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51421db204.mp4?token=ALQpfysu7Rg1_6PUaqQ3MIbgPcR5AsipP1gkFH7-HfbfynoSNEBYjokb1XLfvTbx-_FTjk8yBFpwYec0XzfSMaqCJe4e6xlD9hxwb209xohrHO9A5hzCz3HXHh1U5B4RN9_7q3Kq7wV0N47vqTVhTIlChujm_aBCUkCx1ZrAVL3F0l09z87NDbi2yzX7nFGDW6i6_pmxEey8VX427ogJflx-mh18Ryr0xD5d6CYJIzhronghmQywUJ_m26qzNUg40NJB7k-2t5LM1z_vNBF1LVdgd_fs_MgRoHIln0AtL0XSsXYQgzFvAWCDkek5pmKiBc_tPPLWY8jCeSfMbdbLpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظات نفس‌گیر کادر درمان برای نجات بیمار در قائم‌شهر
🔹
‏خرابی آمبولانس در ورودی بیمارستان رازی قائمشهر مانع ادامه امدادرسانی نشد و یک پرستار هنگام انتقال بیمار روی تخت، عملیات احیا را ادامه داد.
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/696767" target="_blank">📅 23:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696766">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b81e58d9f.mp4?token=L8E_5xlGMZUKSvITR_4h3frnhTV5rJK8LtDVyzVDYfk10hnWRBgZKQwXT3Sxtw3TWNAXLmPiiZZPnOLgC8Ur8iMh9lTQRHYEUEaKBgtiH2MZtiVSqsENFjHxHCWUVUqT63BS6zegKk5_H4nzKPdfPBC4K9zXFXAaU4MVkRM1fmiL4Nz8dG-fFvsRzDDkHizuAVBhdIv7vweAiHC2PGDrPJRcnu57mFg5pZ-s_M-aGwNd2Oo2FlFa21h_nWiQOVlGx2pFcG8I3bOWDzWEBwfVxUnusvTLGFMTA-WPlOM0va-T1SWdT8M5WKoi7dxELFKXVNTArR792H-YudXMw-UhvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b81e58d9f.mp4?token=L8E_5xlGMZUKSvITR_4h3frnhTV5rJK8LtDVyzVDYfk10hnWRBgZKQwXT3Sxtw3TWNAXLmPiiZZPnOLgC8Ur8iMh9lTQRHYEUEaKBgtiH2MZtiVSqsENFjHxHCWUVUqT63BS6zegKk5_H4nzKPdfPBC4K9zXFXAaU4MVkRM1fmiL4Nz8dG-fFvsRzDDkHizuAVBhdIv7vweAiHC2PGDrPJRcnu57mFg5pZ-s_M-aGwNd2Oo2FlFa21h_nWiQOVlGx2pFcG8I3bOWDzWEBwfVxUnusvTLGFMTA-WPlOM0va-T1SWdT8M5WKoi7dxELFKXVNTArR792H-YudXMw-UhvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جولانی دورترین گل لیگ را زد
🔹
امیرحسین جولانی بازیکن تیم فولاد، در جریان بازی امروز تیمش از فاصله‌ای از زمین خودی توپ را وارد دروازۀ مس شهربابک کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/696766" target="_blank">📅 23:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696765">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/764ba72122.mp4?token=KRMDCeFpzmU2Fgd9r_d9KRayxcHImG6lnMnm9w8gOVuhyCePE2B0HHs-yCNowawZug3AIRgE9jbI7DXc5p9a4AWvY3WRw1AGxVRA6KyBjFPTSjUyaC2VXHxee2Ebvz8B18lLRIvyh_TzgoYgwJxsUlKdg_LzXjoDiXqLcurjAT5lqTxw1SqfjvuwRAthoJigmq1-lUfp2Zh9PuOIYmYWfezR80ALUu4dYrBWnd25xoyesWtiHdAtRG-T-6PnWmCKtBhbAYxEGhfOfwGubdVhOQ9blPgJp9OvwqJOuz10Jh5xb0deR4Rtgup6yPSuuSHeRWmdHhU7m-P167_Eog1mpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/764ba72122.mp4?token=KRMDCeFpzmU2Fgd9r_d9KRayxcHImG6lnMnm9w8gOVuhyCePE2B0HHs-yCNowawZug3AIRgE9jbI7DXc5p9a4AWvY3WRw1AGxVRA6KyBjFPTSjUyaC2VXHxee2Ebvz8B18lLRIvyh_TzgoYgwJxsUlKdg_LzXjoDiXqLcurjAT5lqTxw1SqfjvuwRAthoJigmq1-lUfp2Zh9PuOIYmYWfezR80ALUu4dYrBWnd25xoyesWtiHdAtRG-T-6PnWmCKtBhbAYxEGhfOfwGubdVhOQ9blPgJp9OvwqJOuz10Jh5xb0deR4Rtgup6yPSuuSHeRWmdHhU7m-P167_Eog1mpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طبق تصاویر منتشر شده، طی حمله یمن به فرودگاه بین‌المللی ریاض، دست‌کم ۳ هواپیما آسیب دیده‌اند
🔹
یک فروند، به طور کامل منهدم شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/696765" target="_blank">📅 23:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696755">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZxQj0_3UBKnR_gCTZffWxBhg7tLzM-lE8wSUSGdfmPdXHW81z9ecIYeVSPtf_4FnwlwMPri6_WvenqVL8sOsaMD1Gm0d_Uo0xXWLkXk0YtvST43QvhYaaGguYNvIWBGsbFkRfLqm3TzckR3qXIFHKoNqNg7ogOuuE7DF0MdtUn731iGpt8pe-uGqTbdoMQvqED_Itz7Y5xjVcQqmCFq7rfHuFgOubT-pHCTK4q2KJbIXMqKJmE93wzBq3vt-Sv80E3zzkiJVCWe3z0fbaijV2ePZGnP7eSzbE5SxUZlfDmggDnaL1YTV-9EeU7WO_bJaCA2XiMaOLGplrGC4hgzD7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YQGTZAVYt0afXugaibZCM83NH9NJsaVMILHUFVZMfsb2hz55QBV3rGkC7zh6KYD7VnJyJYF_zI85XnfrkhfEhK_N8mM8k-EEcCqArpMmLxTFu9zvGO4-qBPzaL_77He4plWp4r5xDcFJzjybrP7xqMDTej2KIGZobXmuR9iaTGEjLwpMgOwL-6Bf5DfGplph771KYy3ZaXQasRXQQd2s8GVQLnqmPKOQHks1dK1jAxm2NvCl4eZX01Y_LMyDMdiQJRYJTQBnH_F8hX2KVtqnlfrh2C6EjGY7O9UZ_NKwnaOnY2ocfaj7eku-qx0FrzXR9Izi6IjS5ViRPfRE9CnU-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cZPQFfa9P6P5h44whFwKIeQSsPIjR_ltXf_DPAGlegDAoxLts-vFh9XjKx-trQwiEh9Dgg7nq5B56MC1tAXIxL7BrPwsZfTBR_s4UWsst9zzlY0aHHbAdnXC9gAuvABe5r7YqeIpbAA-aBS94ZjhAfZ9_uWyhz3AOzlwNrsAwOrbf3kSnP5_0xk96ZpDKZIMVTtiTNggqCewPZBOYFT86Onl3zr4g88VgTXoOVc1NqoNsH6YuGnbW8k87XMAam3xlpWJiBKOIuymeDGMmRwToq6Yb4TOiuZi8Mt4uFX2NU-DERMqeHmOI6qTSrv1HDDLEsHTmnGD-blknGAPbaV7LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RZP5S8xPDwol0JPE9BA-i4_kIFK3LR0-SP9tCaKSANg0JJJk3exsqcaZUtNRe0by60bhKH6-6whxqzpB0avC_eGb2d_m02bTqcnvu8ZKYKU8CDJCPh3cB4Pv9aIqKpLNSi4cOmvLk4tppghXfw8p9aWMUkWv5IyeiDH4FQJLNwFlB48St7GBzXdb7q0cJYk3calz-5R5o6uC7tAdDAu6eCLHTlmtidJhch0KFOUqFnc-oiiDCpJeYb5JSftBW-eQz-Ys_hbSp8vzVz91exWLI5LzM4G25-C9y81g8okxlSt-dOp94L5hyJ_vPcpR3jMQQKrzeH3BSftqvLTTIVzOow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hLE2uaeF7JxgowXUUileBL7LDY0nPVBmcRYri1xSmH8gdMnvcfTA3DL5eLN8Jim09vAUEV38EIjdUVbc72AAXPOGsKViYYch62LPopJkTWMEfZ6vjXBaqwkU65LZlvF125NGll0geuiWlI-tk8ErVyK7bG87nE_HPnkUhGe0_Rpi9QOuphzxHKBzcnUA8L10hoQZ6VYyMJTAVuFcQtDpTXd1V9JJY5zZWmav254SiGFa_LCS1VXXLdalQk9sn22gruQpahm-rOTEHSemJyCVUgtDGD9Q_l_My4C65Cnk0qaiiWrxBuxGjzgcRdEiDCqB-1OVkgpjDqAePJYG5m5SeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S2x7OJ_rLteIyUrN66Sqred3y2Oy1MErLR9ElKL_UV-VFVPJV7xk08YDWmgXRXDqTYpey2CFzIIgt2JmY8i1quHz2Wd7X4uV1mc9rO96qThq2NQ9EaBbZB2CiSRXO0pvDCmEV2XvjNVbefzCeDg4Z-jj2b0W4aAuFlCbieZ7Jlv9MmNIJNJC9W9GFGu8gwsJEGT2wewJjYVnGYJwwLP8kpdgwuFQROMG_Gcnth3P2KeypjQSZyFO3lRG3j_Js5RXdo3jCqw-oIn-32v4pN9JRHctzww3dZEoSHtooSpNVU5R4r4tDwhnsV5fxdaWcmt2SSMJ_N1TtLGAWwBEP_3u5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/veHNBJyQCs3vxd7P7eTbnPVtEqPYTgbSghjIhtlaB-S6aeAxpNJZ7q7DKqikhdiZW1b7qkAQqTx7wPyq7gCRNTdN0gUOU9I3q5fcKtdSrTLFCaCnF8Enq3ASnI33YfO5-kRPvFkdv34FJDFy7W6j3cQ-sEXoZGoE6YCxHv6KHYU-B18eYXcTCEOV0cDyguN58j-3HsRI9_rop0FvSRs98ByHU9uCHEMBOKSTNzEYPliMPoO-iNiKjfnjwPV-NaogX4_XioLHGbVY_5eA8IZw8C67m6FTCO7G5dMUge3AuK_c9Q6tuqCbwNGdgCB2h0nKF8xqmcELMv7Y7WtsfK0i1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RAwBG0zkuu4YS9SxQkUGvn2kUkdR9JDeUGD70REnCMgXVWy-h3yb0JnGIKrhDh6AyUvJwzQKJgs87bYkw3Oyx9ByMJ7-Lmy2QancrKpIXAl_3_4sKdSCBBwT7zsfXbPeKpfkXQVkDr94Nx2sG7rCeJTfPwxArT3H2ZRFpDYerBbJeaWcH65uhZ4hBAbk16RI3vnBEZ1jIhqN3mlVPoGoi71HgfDK6gpVE21ScybyghidLTQ6z-Z14psaYhcQtxxHTDlC4CI4FJ1YOWYwXRgeWn-p4OW6BXJkF1sSTCVM6jEmy7Avg_3j8CUYJo5p9JWiTZP8u1C2ZCSCo0QELFcI3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vwXHdQ2uWlCBb3e8otXJwCUlK7kjTBpc3JdTH8s_eix7zwJACsZjYtAH_t03hVbX5YEI5nEuOOdWYxklN9boK9QPlJxem-TUc5B5q_XGMeUSwo7Q4KYbVE_ERX8OHn_mQ3_dSbK7NcoIc7BMKWs9pV_Pi901j0W0iG3MYLYNavQHJe1PahLSTLwSN2tfDF6yb4KsKsPwhrdJVrJ9EEdxWVetHTGl48v-uSWO9VB5EqAPbLslQlb349v4BWedpQNU35waV8C1QeGhsi_GNTlnG_cU0JL7_x5AbcXNAktXvxUY3UT7F5AoOtwQyNZiHSzQPwgOdiJ9QpUGmCANh1f8xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KQIucKq0VOdO9_Oi1a7BctZU-QadZeQz5vpr7ktWIULug2pxP3o2zW-MH05ILVvTJEGeblJlLu31X4H5aXQLaH44NyxTvSL8KQJU4ccOS4Wy5rUoBhffx4mZOGxErKAA5LDFu8RGpZCv6QtnVishR3vUrayScgRkcDlpShmxHgaPiffc5HFDzKF2_5NS8irhdXM7CPEOdk8W8v2fTJ9LJsI0bZ6JKcnaxRQ1jzW68LJXqAZ3_4k-ud4KQ9lRd2it-neQS4FbfIZ_6mJlSXeREE31c5pSAk_s2yxFQ1pfc0bNvytJTpc-vB62qGUjLE6AGYXC5qy6HAR1hkVp7ZpkfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">راهنمای یونیسف برای استفاده ایمن کودکان از هوش مصنوعی
🔹
یونیسف برای استفاده ایمن کودکان از هوش مصنوعی، مجموعه‌ای از راهکارها برای والدین ارائه کرده است.
🔹
والدین باید AI را ابزار یادگیری بدانند، نه جایگزین تفکر مستقل؛ همچنین حریم خصوصی و میزان استفاده کودک را مدیریت کنند.
🔹
گفت‌وگوی مداوم با کودک، حفظ روابط واقعی و همکاری با مدرسه، به استفاده مسئولانه‌تر از AI کمک می‌کند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/696755" target="_blank">📅 23:48 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696754">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b21e8ddcf1.mp4?token=GyLkqvgmgipyx4sW9ueQtUoshAWFGLemxXmSz4MPIQH5_CWZfaxb4HabactXUW9S7FC9lNvQe-BYlkv2Y3PMC8Q7hGTMAw8-VbtTkJfbxahLABU7kgT8FZMEyD0iGrJfUxlsEcYO6k3Mz0rmhxeBlwISBkzXSI6pWXRIMrXDy_xF3SdSOEKfto5O9olbQfWV-KrVCVtHPDrRJR3hJ6y4am5u_75140sTWt-_TH7RAfPCXhBvsAC7kmrY9TbZLB7RjCI44z0JIMV2l1eM5Log2PR3W8qP6gIBOvpHCrdcONdMDXFQWwt3A_ynBP8C4GX6txuKj43axO3nhxXmrClX1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b21e8ddcf1.mp4?token=GyLkqvgmgipyx4sW9ueQtUoshAWFGLemxXmSz4MPIQH5_CWZfaxb4HabactXUW9S7FC9lNvQe-BYlkv2Y3PMC8Q7hGTMAw8-VbtTkJfbxahLABU7kgT8FZMEyD0iGrJfUxlsEcYO6k3Mz0rmhxeBlwISBkzXSI6pWXRIMrXDy_xF3SdSOEKfto5O9olbQfWV-KrVCVtHPDrRJR3hJ6y4am5u_75140sTWt-_TH7RAfPCXhBvsAC7kmrY9TbZLB7RjCI44z0JIMV2l1eM5Log2PR3W8qP6gIBOvpHCrdcONdMDXFQWwt3A_ynBP8C4GX6txuKj43axO3nhxXmrClX1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه شهادت نیروهای گردان پدافند لشکر ۳ حمزه سیدالشهداء (ع) سپاه در ارتفاعات شمال‌غرب کشور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/696754" target="_blank">📅 23:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696753">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Saram Bazare Mesgarhast ~ UpMusics.Com</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/akhbarefori/696753" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
آهنگ "سرم بازار مسگرهاست" که این روزها در فضای مجازی بسیار شنیده شده است، این اهنگ با هوش مصنوعی ساخته شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/696753" target="_blank">📅 23:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696745">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BXOxpj9ExSzXQZL-SIZINnj_nkYv70OyiUPNAb-ojA8DTT5R-pRtJsbF5jePFoYAaOT_lnzhcSDuwkNauGoZ_Cq-nxv_DrwLmCQfjOV9zeLeogsrU51i_0YpGK7vo_yWzO_JlFo068LfUGQyJMFOcxULJi1sd3W2P0RXA0Yf7-BetJ1d1LmpL9pnuGJtwcrx5qPJQHvCT0ptQln5XINl3PaTZfx2ASBy2O8erGIniZU5_luD9AE2i1WEY-mSAUg5WNnYrFOK8XUwdZUG5zKNTwtZKyXYDTaRLf5OfB_nHqHUvSH3nARGVIFK8HrES8_owuNIqN1I9cFbqhtEoURoTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E5vteG1iBNqasIt-V9JAKDmlqdeT_fHcGTm685jbG2lovQbpvJSB83qi1VgG9p2VNj_c8TKqyX4gDXZaeo8wY9Uhtt_NVtSyfMp64SXGA1IB33ytJMhY8E6bt6F3W49JZxiGPHGyJj-9LkIuTu-N0chiw-KOuEEvH98eE7QOY9pJa8Ng-TZapJzvWF9rjqp4Tyy0-SR_ex6BWjkmF0fpzq9tZ5EmUMyp0tLsboR5uck5NdATopbSfLGl4ho1vjjH-ExIWjiBem4VqlZAT4m20M1Rf8B0-iy0xQuZPcSJlVbp2ER1Gt6FQEPTzUqInQpPHqPLB_QYj57ER8R20Ekdag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tfK5RBV2QhaXDSylLjMkgyP5JrjbAu9K4sVx2J7FyfgymgBs1nBm8hIHzhXsO5cNVTQ7zZiudU0UXqz8RT2gC_TIFTevIrm0pLOyLLr0zIRGKWPay9yjuZ2QHcs90Y553U_tsI6Q59LpIho03dacKgnYn9c5c7TKs115ypVA6eX57rpL1Fnb2VGgZOoSdXUt1SgNdcgCcpz2wfXEsQZukJIdVhAh6SQ389t3KXDVy1XukL_dyl-vrdexzrOcf0ndmwVruw_FPNAXnnBFPk7yKkIptOEZaLDskx4qpZUo58VPFpXMvx1TH0BogjF1x8qFNePJqF3ScSfovYcVH2jHNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RJuuGa5jv7Ce57OuQ9SdRE67YB4CWXmAe0Voim7rzqajwWBb7dolwxxWoLDs8Grqn4Z0rV3JGye61TxVolzPxo6iqBnY6-4kg0In-NP_dk2Q6dQO7MB9L5Eou-m488NbripR7SrxulGze33Xm1jyASxQV4elT4zZSQp9JwcWd6u7vIgWHlXfRHl9SmV0fqgGMG0MtVXrtygvDrHnTWZnjo7EDpjIxKaPuHbhL9DsS1bwQzBQDuLMAGSgTvLe4_ysNuUuKwWNgTAlbVFiqb6rVZW35y2Ft9-mmjO3vjPUqBxPemSyk7GAYFrLUHQpiEAzCQvFS31pedYtvN_TbZ5PxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iq5iMKbbmauY3pt8vAfNAV4EfgNn4OPIQCjmoOtySc9T46d29Ghof-hZ3uQcOdMN-xG66f1InReNnd771qMHOtJIFRdttOSTezO2Ydy17Hvm8poB_Cyb41bYgxnrxg-BlaC_53ckJ6S0bbKRAbUpaKTXCoMaFjW4pzzvyddWZyfJmU8KMbzueEJDM0V2Ti3AkD07zv5LqdnOFCD4IPJVE8L2DgjDmSlSHk_F0Ye_JkG1lV-6V04n7F0jVo30kk0KJYfeaSVB3DqKhX1vUkPzUaMPvPYan7ewaz2PcwLTJ9AmYLyXwGWtUtqUc9iZsvJIJEpfRjYUDn-wPqaMHNVhhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AABRKiKt2Ww-IRqygEBM8apYsbdyxXnVuSTqtc-X3wjgkSr5GKrXR6Pt07yHmIGGZEvgbrzWmVyyJeSIbSOcablZ0FgG_FoSROsch1pzuofdRgcHjNDS8FySxL_hk560aQOeQbVv3EJkxVZY9PCcrRX1UhNUhVZttofhPc0AkcYjDO66fDQxCkDRO-jRjqgygdI85iVPveVSv3hOomolc8UbzBCvVp-t1tyCgPgGXB4TmSs4M0oywysDd7fP_aqOVIs_ZfqnE8u963Dz6xR70LRY-cRo37UoiH2cVjdcvDqHbSYRAAIAZ6MpaQDG9UHwJGu87_KUFDVavZCv-ud9_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cf3chtz_OChdY11y61kE6gfsnmbSIh2tt6DVam22M1dOXMcabwZfRk2WdjCBYJaBY6Sy4TpAUIbCQwa3PQgUtI7SrGdQvy2-dGnuxeSdX-s0AMo3u7daJjSPYZr9ePZccqxw0KAWkblnVKAd6pDBxsn--99Qgm7FS_y3gltDdO300HZf_E-y5UewntR2sR5KA28yI5X33TBrYRXaeM7eS133lDz3_QmdB9Bk1vBHS43R_0ZndaRdf7yK_qktf9Xj2QqgYm4ntQJeJaBxJvFr9afZrABagdCdlZysHhZCfeLjLR-nQ5VaZno2GjY4_iIfFN3be96xepR9TdCOACjrZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vyu6lqGuJn1FAj-44S3cVw9NAT6TUVFlVLO8eYjjSTSfsn6g931PqGa6z0-06FtyPx8e90IYoKfvzN1oy4cZZggFjnmGBbgDQ-Q86MzUpVwMMxcZy7WkGwRq8YdaOLbKLIloub1PJeQ6w1OBemX_CgEJaUaP4Xjo0gShIeUbrcwB6-X-R-JL5Q3jNNmNXQaIWMGh4hDUOyoNpEwooCxiXsGJ3BuRrbhllOAGc_nlZA1PNebfKYdR0UH9MFDvI4NFkFbc04MtOSZ3hhR-ixQgdM1bw6ZtIRfB_-zzLA5Kv7ewj2XL747KCJ_Ql7mHIDK5ShelwuV714FGAXXec-M3Hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نزدیک‌ترین و مهم‌ترین گذرگاه‌های زمینی ایران
🔹
ایران در قلب منطقه ۷ مرز زمینی با کشورهای همسایه دارد؛ جاده‌هایی که شهرها، بازارها، مسافران و مسیرهای تجاری را به هم پیوند می‌دهند
@TV_Fori</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/696745" target="_blank">📅 23:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696744">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEioi0zF6hT_f53bYPpAFxdI7sF6V-Ie280QIlxwVfNu-ewzALrFU60MCulIRlFkYAKxuZukV50X22_cpAE5dJxQVFUY2P4-2LjcvMi2kT8ssn1CjAKs6S6MAose8s3VpRmHgikhrA9eB6bhYFg0xGfoZSGrhNxH4xnYKbfn0lz4WHLbCtgNtH9D7Tz7E9I3T1eCDM017CVehplkrXFao3Toi3GhyJfEKmJNA87407zZ4rUBZ6bdiGrdTjlE4qiRq3RZubJKj4fRvNDcaUTVTGZXKrIwlOQ3X7aPT3SaVZcQdECvllI7Yl8JG3E6OJtXaLEFmGNUvEYFQbFDSdKfLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برت اریکسون: محمد بن سلمان مایه شرمساری است
🔹
عربستان سعودی بی‌دفاع است. فرودگاه‌ها دارند آزادانه و بدون مانع هدف حمله قرار می‌گیرند. زیرساخت‌های نفتی هم به‌ راحتی هدف قرار می‌گیرند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/696744" target="_blank">📅 23:38 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696743">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
نفتکش‌های متخلف روی مین‌های تنگۀ هرمز منفجر شدند
منابع موثق نظامی:
🔹
دقایقی پیش چند انفجار سنگین در معبر جنوبی تنگه هرمز رخ داد که ناشی از اصابت نفتکش‌های متخلف با مین‌های منتشره در منطقه از دریا می‌باشد./ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/696743" target="_blank">📅 23:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696742">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLu3u8Z6xnPlcfWwy-Qj-mEOzSpJr5yCHTulw0g4gk3MAB7XYptlaEME1ZgR7nvTEBI7vPEXCbXj13MdH9Rat2z57hg9SsGv3GJqYhU9GBh8PEIpODUIPiSqq2V4CX98dOYTQ9NFsgjtztiF4rr_X1fYY64GQaV9kGz0UPZY4QwOfrC9cjkc6OZx-nhIDc9PoxXg6LmdI5aILkCq6dEJZvB2zRyP309qCDlEoCDWymkrPdPGqVWPrIESkAfWgzfe3eelJkGMwRldvT8lsH0SYwCXnlostINuekDGvIaI2CSrT6sSV85jAk2bHPSRg086KnqPOT6IOs_JDH4j57txJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استقبال سندیکای دارو از عرضه بلوکی شفا دارو؛
اختراعی: بخش خصوصی بهتر صنعت را اداره می‌کند
🔹
عرضه بلوکی شفادارو با استقبال سندیکای تولیدکنندگان مواد دارویی مواجه شد؛ فرامرز اختراعی با تأکید بر ضرورت واگذاری بنگاه‌های دارویی به بخش خصوصی، اعلام کرد که بخش خصوصی توان و چابکی بیشتری برای اداره این صنعت دارد و خصوصی‌سازی در صورت انتخاب خریدار دارای اهلیت و ایجاد فضای رقابتی، می‌تواند مسیر بهره‌وری و توسعه صنعت دارو را هموار کند./
متن کامل خبر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/696742" target="_blank">📅 23:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696741">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
سفارت آمریکا در اسرائیل: شهروندان باید برای احتمال لغو پروازها آماده باشند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/696741" target="_blank">📅 23:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696740">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
رویترز به نقل از رئیس ستاد ارتش فرانسه: پاریس در حال بررسی گزینه‌های نظامی و امنیتی متعددی برای تأمین حفاظت از بندر نفتی «ینبع» در عربستان است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/696740" target="_blank">📅 23:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696739">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
ادعای رویترز: حملات به نفتکش‌ها در تنگه هرمز به بالاترین سطح هفتگی از آغاز جنگ رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/696739" target="_blank">📅 23:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696738">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
در لابلای خبرها، داغ‌ترین‌ها را از دست ندهید
🔹
🔹
ترامپ به حمله دوباره به ایران پیش از انتخابات فکر می‌کند؛ جنگ برای رأی؟ | پشت پرده بررسی حمله دوباره آمریکا به ایران
👇
khabarfoori.com/fa/tiny/news-3250780
🔹
سیاست جدید ایران در خلیج فارس؛ آغاز حملات شدید شبانه به نفتکش‌های متخلف | واکنش آمریکا چه خواهد بود؛ بشکه باروت منفجر می‌شود؟
👇
khabarfoori.com/fa/tiny/news-3250874
🔹
جزئیات دو عملیات تروریستی امروز در جنوب شرق کشور | از حمله به خودروی پلیس تا شلیک به مینی‌بوس ارتش
👇
khabarfoori.com/fa/tiny/news-3250857
🔹
حقوق بشر؛ ابزاری که بهانه سؤاستفاده سیاسی شد!
👇
khabarfoori.com/fa/tiny/news-3250902
🔹
چرا مردان پورن می‌بینند؟ پاسخ شاید آن چیزی نباشد که فکر می‌کنید
👇
khabarfoori.com/fa/tiny/news-3250703
🔹
صفحه ویژه اخبار جنجالی خبرفوری را اینجا کلیک کنید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/696738" target="_blank">📅 23:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696737">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYqOQSulgKqPEbRyylAgCrP1feKsh4GeHDnmOKZ6pZaYKWn6btTlulkXEUrwzhZGAIGa4hwfmbFWz5pha3u6cPJGSynfH9XHgDQSNR2sEAGK1rlJ9Da92EskaFLglf7MM0yR50NM8_FQZ3MO7u0tndlg5BRboQA4dKdRYy8MjybmoKCyaBP9JI0r7p6ZLcENApH_ok2JCrf8LJIsuS9dtWW7evhQ5DGBo-tDsR_gYhm6sBKJfoBhf0lad0AaAJHdz7cKxHdgmX8pwvIL5I4B72-Ih7cp7IWGkugybf5T2ywDQ2xKu8NhhkJQX2u_dgP4Oc8Reh2rYbxVu_OD6vNnKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ساعاتی پیش OpenAI با انتشار پیش‌نویس اثبات ۷۲۲ مساله‌ بسیار چالش‌برانگیز ریاضی توسط یکی از مدل‌های هوش‌مصنوعی داخلی‌اش جامعه علمی را در بهت و حیرت فرو برد
🔹
مساله‌هایی که بسیاری از آن‌ها برای چند دهه باز بودند و حل آن‌ها توسط ریاضی‌دانان بلافاصله به دریافت جایزه‌ فیلدز منتهی می‌شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/696737" target="_blank">📅 23:23 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696736">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddcbdcb298.mp4?token=F6hlN8Kr4m_lhZwYMWu6rAVRCrEHp6gcypG3EF1Hr8qGtB2lOOdZ-pwJc19LE7-WKqwGZuMve2SK-f_HLzhlk1U-8l6khZFAMTMd3jNryz-4p67lYE0ytAgV3pDiDa71Xk18EvkEix14SIfPbZPbM4hfRojEtf6PxcAfLssDFkRoE5TPODAr1KIjoH5vtCj5HO38LQNrviG9Fli-TuHMX12uT_f7KFi-Ff0a0FA3oqPu9cT2lxiSlsrKBH-9vZxNH5rAg35ecKA1HV9JXuULK4jn9Ho1_X5BzHBnyVOAx29VAWAPqLfjPil0Ln9RibMb0DTZ0jpV6hYuSyinK7IFlYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddcbdcb298.mp4?token=F6hlN8Kr4m_lhZwYMWu6rAVRCrEHp6gcypG3EF1Hr8qGtB2lOOdZ-pwJc19LE7-WKqwGZuMve2SK-f_HLzhlk1U-8l6khZFAMTMd3jNryz-4p67lYE0ytAgV3pDiDa71Xk18EvkEix14SIfPbZPbM4hfRojEtf6PxcAfLssDFkRoE5TPODAr1KIjoH5vtCj5HO38LQNrviG9Fli-TuHMX12uT_f7KFi-Ff0a0FA3oqPu9cT2lxiSlsrKBH-9vZxNH5rAg35ecKA1HV9JXuULK4jn9Ho1_X5BzHBnyVOAx29VAWAPqLfjPil0Ln9RibMb0DTZ0jpV6hYuSyinK7IFlYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا جای واکسن روی بازو می‌مونه؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/696736" target="_blank">📅 23:17 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696735">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">صد میدان 9- میدان نهم، ریاضت</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/696735" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
شرح صد میدان خواجه عبدالله انصاری
🔹
میدان نهم، ریاضت
🔹
ریاضت سختی‌‌ایست که به زندگی انسان ورود پیدا می‌کند تا در پایان نرمی‌ای را در نهاد انسان جای دهد.
🔹
ریاضت توسط افرادی که طلب پاکی دارند انتخاب خواهد شد.
🔹
اذکار منفی که شامل غیبت، ناسزا، اخبار منفی و از این قبیل می‌باشند؛ سرنوشت ما را بسیار تحت تاثیر قرار خواهند داد و اینها چیزی جز کلامات شیطانی نیستند.
🔹
پیش از آنکه جهان‌هستی شما را با سنگ آسیاب خود نرم کند، خودتان به جوانمردی و فتوت روی آورید.
ارکان ریاضت به سه صورت زیر هستند:
🔹
ریاضت افعال به حفظ به سه چیز است: اتباع علم _غذای حلال _دوام ورد
🔹
ریاضت اقوال به ضبط به سه چیز است: قرائت قرآن_ مداومت بر عذر_ نصیحت خَلق
🔹
ریاضت اخلاق به رفق به سه چیز است: فروتنی_ جوانمردی_ بردباری
#صد_میدان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/696735" target="_blank">📅 23:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696734">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
کانادا هم نسبت به اعمال محدودیت‌های جدید در حریم هوایی در عربستان، به شهروندان خود هشدار داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/696734" target="_blank">📅 23:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696732">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d26f81183.mp4?token=YJk3anzUnpX6E9zXwnbvK_0IoNpDlriebXngjIBKmDotv2ATVU5TjllSEONYnz-WAbSye7064mbCYqwWSRfYV1fEtuLIpD974mDTScWnZOfUo8xUwPN3jBAbOvzY8yiHAws9R0aUFfs5AQURmOZFxxtE_yk4hNycX2BLZzYvLpWwdDzqK9eIqG7bUTvZ-uZ7LlEcNZPsz05GcpBIzaRK5yzUcrIefHgQNZYdolSBLXoYNH_z-VPOo6_60_QaGCA4nYkI7PvJgQThKCqh2um7gfhC4g_jawD8ieTAS5T6GKMGGpXZ6VKjUta7pa3DK4V3iof8CYKVTKOASPZEsD57Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d26f81183.mp4?token=YJk3anzUnpX6E9zXwnbvK_0IoNpDlriebXngjIBKmDotv2ATVU5TjllSEONYnz-WAbSye7064mbCYqwWSRfYV1fEtuLIpD974mDTScWnZOfUo8xUwPN3jBAbOvzY8yiHAws9R0aUFfs5AQURmOZFxxtE_yk4hNycX2BLZzYvLpWwdDzqK9eIqG7bUTvZ-uZ7LlEcNZPsz05GcpBIzaRK5yzUcrIefHgQNZYdolSBLXoYNH_z-VPOo6_60_QaGCA4nYkI7PvJgQThKCqh2um7gfhC4g_jawD8ieTAS5T6GKMGGpXZ6VKjUta7pa3DK4V3iof8CYKVTKOASPZEsD57Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری دیگر از حملات پهپادی به مقرهای گروه‌های معارض جدایی‌طلب در اربیل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/696732" target="_blank">📅 23:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696731">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db808e8502.mp4?token=PbDbBdF7NPvAjywvQfxwvVg0pkLbMelBy0F0d6ZaJhe82n7CQ0bhcWS0SwUC5E6Ena8Nk8dULsPh7GfUtux__xuOiyvu0n-88RnpAblWF1n4yWq-BXGTTRIjnILldfGF-CQutRPeRjV2-gvruUmAACkS81xWBRJt9Syrv64ISosEqv-rPYLcVsJ9ZZcoHRzoBy6JiRUCaMee0rzwYQT3JC3Q1S3O5ctLSANL5NxxTrEeP31GfifOTnoKkcJSOh-BO0zMqt3RHPKQ_zdFjOr7yKQ-EnWhsla6DrUfeJjuuy81TQTmDhQrITfANqVqVFGhMq-grJzXzmiaP63F6-eESQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db808e8502.mp4?token=PbDbBdF7NPvAjywvQfxwvVg0pkLbMelBy0F0d6ZaJhe82n7CQ0bhcWS0SwUC5E6Ena8Nk8dULsPh7GfUtux__xuOiyvu0n-88RnpAblWF1n4yWq-BXGTTRIjnILldfGF-CQutRPeRjV2-gvruUmAACkS81xWBRJt9Syrv64ISosEqv-rPYLcVsJ9ZZcoHRzoBy6JiRUCaMee0rzwYQT3JC3Q1S3O5ctLSANL5NxxTrEeP31GfifOTnoKkcJSOh-BO0zMqt3RHPKQ_zdFjOr7yKQ-EnWhsla6DrUfeJjuuy81TQTmDhQrITfANqVqVFGhMq-grJzXzmiaP63F6-eESQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع عراقی از شنیده‌ شدن صدای انفجار در مقر گروهک‌های تروریستی در اربیل خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/696731" target="_blank">📅 23:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696730">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
استیضاح عراقچی به هیئت رئیسه ارجاع نشده و فقط در سامانه ثبت شده است
عباس گودرزی، ناظر هیئت رئیسه مجلس در
#گفتگو
با خبرفوری:
🔹
دولت پس از دو سال فعالیت و با وجود فراز و نشیب‌های مختلف، باید نسبت به ترمیم کابینه اقدام کند، این کار به افزایش سرمایه اجتماعی دولت کمک می‌کند و وقفه‌ای در خدمات‌رسانی ایجاد نمی‌کند، زیرا رئیس‌جمهور می‌تواند بلافاصله گزینه‌های جدید را معرفی و مجلس با سرعت و دقت آن‌ها را بررسی کند.
🔹
استیضاح وزیر امور خارجه به هیئت رئیسه ارجاع نشده و صرفاً در سامانه ثبت شده است، در شرایط حساس دیپلماسی کشور، هیئت رئیسه باید با تدبیر و درایت مسیر را ترسیم کند.
🔹
استیضاح‌های متعددی در سامانه نمایندگان ثبت شده، اما وضعیت آن‌ها متفاوت است، برخی صرفاً در مرحله ثبت و امضا، برخی در مرحله بحث و بیان، و برخی ارجاع شده و در نوبت اجرا هستند.
@TV_Fori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/696730" target="_blank">📅 23:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696729">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
منابع عراقی از شنیده‌ شدن صدای انفجار در مقر گروهک‌های تروریستی در اربیل خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/696729" target="_blank">📅 22:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696728">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_K_cWydbL-vw-aihbugHJ8lF7JUW3JQk7mk5vPArMs2RWQYdENiv-JPdEnb70I2YiURdpfik8KfYppW02IjdlvGCFtuwgQ0s6edFxZdmaMPsS2NXqa3bjuNQUPXoSrztPhc6BNrA9W4TBDukPw_z1Dbxf49OkHHm3kxO9USgOQtyA7wrKoiAi1ifp_iLbQm6t78U6jME1X4NH21Qq0EfgtmZxc28Vr2qS3ZZLr2rvPiC8_u5c_6jAtjDhwShVTPx0f2ydxEOAXbChfy37Cag9ivLqqEYM0em2tMUpQ4UwKySJSwBuna2J4EN44d2WSTca8KLbqScHpBfyzz185cNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ به حمله دوباره به ایران پیش از انتخابات فکر می‌کند؛ جنگ برای رأی؟ | پشت پرده بررسی حمله دوباره آمریکا به ایران
🔹
آتلانتیک گزارش داده‌ که کاخ سفید از پنتاگون خواسته است گزینه‌های حمله به اهدافی در ایران را بررسی کند؛ حملاتی که ممکن است حتی پیش از انتخابات میان‌دوره‌ای ۳ نوامبر انجام شوند. این موضوع در حالی مطرح شده که در چند هفته اخیر نوعی آرامش نسبی بر جبهه‌های جنگ حاکم شده است.
ترجمه این گزارش را در وبسایت خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3250780</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/696728" target="_blank">📅 22:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696727">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
پزشکیان در دیدار با پوتین: ما هیچ‌گاه میز مذاکره را ترک نکردیم
🔹
در حال حاضر مشغول جمع‌بندی پیشنهادها هستیم و پس از آماده شدن متن نهایی، آن را از طریق میانجی‌ها بررسی کرده و همه پیشنهادها را منتقل خواهیم کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/696727" target="_blank">📅 22:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696726">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28cb1d0a01.mp4?token=eeTqQudrnlV2TwJSnVqullhaIfBOBw1kjo1t4GhfTj66RUBJTLeFcy6NZeFhATSD0-Q6GH2Kv_cOyODTylNP66lEomdpan_zMIPgLcAYUsGjaJvuaRUAyago6M2TlV3-uk7q56AQXRVzecVPolXLa801lXwibrRVgmB6ztkV0E_GPP-LvUILypUkOsQ_7ysgw-Sg8Pe7O6tddgJFLZM5MNKAOao7dzKO_FZ5HRxHzDrKa8myZ1nH4VeqoOd_-CCfvWwzAj9oHK-yy_MBqpj_lZdq40U-HpLNSWtlQ_-MoPtRGwLyYhRE-lYGTUd37mU3IoN5MIM6PqppqpVn_KOo9jro6uK-08U6hM5tV_n53go4t9KmrihKrKiqPEoYPOp6rLEelUxb3uHDXBcLBv_gCRM8HtTegB36Unf7ZwSpUvMeyRs_z0N7uL4NU6CRr5orexaWUqkE2TRZ5D_w50kxAsv6RbaFXF4xLrUSmIfRdF8eo_6T6b0dt0m3dlkPOa78okno6HA816KylAdcUq27nxmOpJparkxThD7-AZ4P_cRV-9Qc6zxtnT0iJiyPFnemO37xHW6Hpml1xvYKRE4MBxOJ808QJDuOywil0nmgkE16WMFLDOnm0RGvol5O_GfqiN0hc_dK7-Fk1VReRJEywEhv325_KCLFkdUjbH0h9Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28cb1d0a01.mp4?token=eeTqQudrnlV2TwJSnVqullhaIfBOBw1kjo1t4GhfTj66RUBJTLeFcy6NZeFhATSD0-Q6GH2Kv_cOyODTylNP66lEomdpan_zMIPgLcAYUsGjaJvuaRUAyago6M2TlV3-uk7q56AQXRVzecVPolXLa801lXwibrRVgmB6ztkV0E_GPP-LvUILypUkOsQ_7ysgw-Sg8Pe7O6tddgJFLZM5MNKAOao7dzKO_FZ5HRxHzDrKa8myZ1nH4VeqoOd_-CCfvWwzAj9oHK-yy_MBqpj_lZdq40U-HpLNSWtlQ_-MoPtRGwLyYhRE-lYGTUd37mU3IoN5MIM6PqppqpVn_KOo9jro6uK-08U6hM5tV_n53go4t9KmrihKrKiqPEoYPOp6rLEelUxb3uHDXBcLBv_gCRM8HtTegB36Unf7ZwSpUvMeyRs_z0N7uL4NU6CRr5orexaWUqkE2TRZ5D_w50kxAsv6RbaFXF4xLrUSmIfRdF8eo_6T6b0dt0m3dlkPOa78okno6HA816KylAdcUq27nxmOpJparkxThD7-AZ4P_cRV-9Qc6zxtnT0iJiyPFnemO37xHW6Hpml1xvYKRE4MBxOJ808QJDuOywil0nmgkE16WMFLDOnm0RGvol5O_GfqiN0hc_dK7-Fk1VReRJEywEhv325_KCLFkdUjbH0h9Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عجیب‌ترین چیزهایی که از داخل بدن انسان پیدا کرده‌اند
😳
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/696726" target="_blank">📅 22:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696725">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
دولت انگلیس در تازه‌ترین بیانیه امنیتی خود، به شهروندان این کشور توصیه کرد از هرگونه سفر به مناطق کلیدی و شهرهای مهم عربستان خودداری کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/696725" target="_blank">📅 22:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696724">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
پزشکیان در دیدار با پوتین: با ادامۀ یک‌جانبه‌گرایی آمریکا دسترسی به صلح غیرممکن است
🔹
ما از شما به‌ دلیل موضع‌تان در مورد وضعیت منطقه تشکر می‌کنیم. روابط ایران و روسیه در تمام زمینه‌ها درحال گسترش است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/696724" target="_blank">📅 22:47 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696723">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
شهادت مامور فراجا در حملۀ تروریستی در فاریاب
🔹
سرگرد مهدی جمشیدی، از کارکنان نیروی انتظامی، دقایقی پیش در پی تیراندازی افراد مسلح ناشناس در مرکز شهر فاریاب، به شهادت رسید
#اخبار_کرمان
در فضای مجازی
👇
@kerman_news</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/696723" target="_blank">📅 22:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696722">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
پوتین در دیدار با پزشکیان: بهترین آرزوها را ازطرف من به آیت‌الله مجتبی خامنه‌ای منتقل کنید
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/696722" target="_blank">📅 22:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696721">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
دولت انگلیس در تازه‌ترین بیانیه امنیتی خود، به شهروندان این کشور توصیه کرد از هرگونه سفر به مناطق کلیدی و شهرهای مهم عربستان خودداری کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/696721" target="_blank">📅 22:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696719">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
سخنگوی وزارت دفاع: تولیدات وزارت دفاع در سال اول دوره شهید نصیرزاده، ۸۰ درصد افزایش یافت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/696719" target="_blank">📅 22:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696718">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xln-wkxRigAWLPKHGsindA2IhmiDhcvq8X2HMdbVzgQ0_GhbDyf5XE5y2wqvtcEhztmc0rxq5XZFvrkfaZ95slb1L6Xtv3M6k1HRFmh6n_S-Vt71yj8dcnTBRuYEtopXZwU9y6rGbM3tP47kdLoy9_3Gb8LoKsWfpRlXHauJ4runilGB_xAuxQPtz0W-K-K9ivDlrWv6Tl59YPSDgJqsBV0_kTL7duXVhGDTfLuoA6M0q2u_HUCcSLM58Sfmfopj2M_ix-wTUs6Pz7QjKcudPlp9JTlZs_6lrEXVurv8GyZiA6FbUakFeB8Dl-PkYFqWQKHQm_GlCMnYiwZE-hJfDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کارنامه مالی هفته
🔹
در هفته‌ای که گذشت، بورس با رشد بیش از ۲.۸ درصدی بیشترین افزایش را میان بازارهای این جدول ثبت کرد و در مقابل، انس جهانی طلا ۰.۷۵ درصد کاهش داشت و سکه بهار آزادی بدون تغییر ماند.
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/696718" target="_blank">📅 22:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696717">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
سخنگوی وزارت دفاع: تولیدات وزارت دفاع در سال اول دوره شهید نصیرزاده، ۸۰ درصد افزایش یافت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/696717" target="_blank">📅 22:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696716">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39c6f84fd8.mp4?token=S0b7BAsDh-MCsieverRlTtUZAqum0rY9qCl_jPcnvUCabggq0iATPt0ywdAC7LTUF5_OqnE4V8XEOZ5sBeCDb1E3hA7pFfGp13-2i9nVdKfa-2KNsq4wkSYR-f-yAzmibqtTypKo1hf_s6X2Miof_u14ZVwW0SWyZNMl_6I3Tey23ClS_oxneBCQ7Z2qWY1Dc7BQvHE94KTnfRxBSTS2drYILHQTF0qYSrhf-LFz_uK2XuE0FvzCVxD4EpZUQX1uo3opKtsoTZbQkUcdyEZ6tHkG-iV3bJW1xJ_W_V9UktTByEwBZE9wIwnyCkh7PHt9nJRCk3KSyvwKJ6TS2VsBjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39c6f84fd8.mp4?token=S0b7BAsDh-MCsieverRlTtUZAqum0rY9qCl_jPcnvUCabggq0iATPt0ywdAC7LTUF5_OqnE4V8XEOZ5sBeCDb1E3hA7pFfGp13-2i9nVdKfa-2KNsq4wkSYR-f-yAzmibqtTypKo1hf_s6X2Miof_u14ZVwW0SWyZNMl_6I3Tey23ClS_oxneBCQ7Z2qWY1Dc7BQvHE94KTnfRxBSTS2drYILHQTF0qYSrhf-LFz_uK2XuE0FvzCVxD4EpZUQX1uo3opKtsoTZbQkUcdyEZ6tHkG-iV3bJW1xJ_W_V9UktTByEwBZE9wIwnyCkh7PHt9nJRCk3KSyvwKJ6TS2VsBjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای وزیر جنگ آمریکا: ما قصد نداریم در ایران دولت‌سازی کنیم
🔹
همچنین نمی‌خواهیم شمار زیادی نیروی نظامی را در ایران مستقر کنیم و کنترل مناطق مختلف را در دست بگیریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/696716" target="_blank">📅 22:23 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696715">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
پارلمان اروپا با صدور قطعنامه‌ای ایران را به نقض حقوق بشر و خشونت علیه غیرنظامیان محکوم کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/696715" target="_blank">📅 22:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696714">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5Vw2bLGI8u95BEZbdKxXf-xMNPWPvmkSb7Y4l6jsFVbf8cOsVQhj1KfpPTryWEwiG1QBPqbXkSc8UoUfhENQupC2qF035N_rkMVcvqiIYUMhiOQBi8ja64_aq8buCWWc3q5z0NS9jrDBu6b4gG6WQpWPG1xylkmanx-0Xc-UedqNfzeRgI4dH28Dbskz-XBtGq2zc099qU8rw3Q6otccSxyakl3D5aG-eWcqsg9p4caLXkwGq_mjbJX443BwUoEd7NJI1JvWrehtSXk2VQJ3W9mFAZNrsGbkgLjoBVTPH6O_xjuGI1ioCp1BbjlGnL6B2sy4OJXXcKfjVDDaO3aJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نایب‌رئیس هیات‌مدیره سندیکای مخابرات: صنعت ارتباطات کشور با وصله‌ پینه اداره می‌شود
🔹
فقدان توسعه زیرساخت‌های ارتباطی در یک دهه گذشته، سرکوب دستوری تعرفه‌ها و فشار مضاعف بر شبکه موبایل به دلیل تضعیف تدریجی اینترنت ثابت، شبکه ارتباطی ایران را در وضعیت بحرانی قرار داده است. بحرانی که به گفته فعالان این حوزه، دیگر به قطعی یا کندی اینترنت محدود نمی‌شود و مستقیما امنیت ملی و اقتصاد دیجیتال کشور را نشانه است.
🔹
به گزارش پیوست، فرامرز رستگار، دبیر و نایب‌رئیس هیات‌مدیره سندیکای صنعت مخابرات ایران، در گفت‌وگویی با بررسی دلایل افت شدید کیفیت اینترنت و چالش‌های اپراتورها، تصویر روشنی از وضعیت امروز و فردای صنعت فاوا (ICT) در ایران ارائه می‌دهد.
🔹
او معتقد است ریشه مشکلات شبکه نه در تحریم‌های بین‌المللی است و نه در کمبود ذاتی منابع مالی؛ و در حقیقت کج‌اندیشی در سیاست‌گذاری، سرکوب غیرمنطقی تعرفه‌ها و بی‌توجهی به اقتصاد ارتباطات، این صنعت را به لبه پرتگاه کشانده است./ پیوست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/696714" target="_blank">📅 22:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696713">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
ادعای آکسیوس: آمریکا، اسرائیل را در جریان تدارکات برای احتمال آغاز عملیات علیه ایران ظرف سه هفته آینده، قرار داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/696713" target="_blank">📅 22:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696712">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxDbY1FXg204zb7nlN3yRV82Lp_H7d9FhLS_b2KQoEfSdK9o2BiX5fVC-GkNz6AqIcOO98PFI7j8vtes8HwVweIAgy1-GVp0AAt7nMIHX0o_szwYeO3pPNii5fh-0myfhH_3uCx3uTCAlGHodMmyBw391MJxmoK_R17SvqJs20YU9UWX7Ob-gipgaq_uO00gbnhnT3mWYiDHsNaqX1ixXnQSFfcj2qK8HE_crY0H4ZzF4uJh9p0CfHN-nnOvlv9catAq4UI0ySsFjUFDxomXM2zBSH7dtc_rSSQGXyr80X9FhMtXrmizQxyfUtZcXjOuYRqeo7kgCR3fiLkZT7hbyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با چند تغییر ساده در تنظیمات، شارژدهی گوشی را دو برابر کنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/696712" target="_blank">📅 22:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696711">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
رئیس اداره آموزش و پرورش کیش: تمامی مقاطع تحصیلی در کیش، از ۱۸ مهر به مدت یک هفته در قالب غیرحضوری فعالیت خواهند کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/696711" target="_blank">📅 22:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696710">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3LaDSwo_I5B_oT1YQcXY08hceSDOrC4kB8fFoM28yK7c8eBsf4OB1YTcOgw1yhFCYKzDYDe-klgGMAnG3Fl8l3FV0vJzz6IWl6PX_yWnXhig0CJj3P1IrJvCHnJRtzRTHhJf4sRrYc5K9Q3i1bEh_VbPn31LjhiVzlA9yOhfg4_271-hlPNA__s5HlhPC5lbtl93sxZ9OPFM9Y8LXpKumwEkNerawajMH0d3L1PJwjbILuX2RFgccYyZJiGjpUMfILvDOKilqdCmwhQ1VlBlohvucQRQM3P5iw7kGU760738hh7n7f_22zviU_ywUvlGrHRpOn9bgX0NB6wPfgx8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طوفان در تهران و وضعیت دریاچه چیتگر  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/696710" target="_blank">📅 22:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696709">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8K2pIEOgQD1OocbpC4QC0gPhoAnuekCEzhqYdVisLt0VBHtcUmA8kArRswqffCtIvRI5zpQ3p8rcZrf4-cjKc5nLRZhXp66-kAXDpseDXkwpQ_p5a2eYcV6SjHarVeWcVQu5CmIpZ947fVICHtU7vIARqhSA947Wl4cAsoRXudOhwgOtM6BTSR8ZzAsLpvINMiTPa9g047yo5CR_xLu7VgfbUrtcjf78htZRTmejdXmXSu6i_qjwLzNJ88mSHL682Bzae18TeR4NL0-qS_gcznac-9ZbkzrL-JL7ytihTtQUl7JfFroT6wmzjUrnSNPM64nwW2WculHZsXqW6AYIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاروان مردمی دوچرخه‌سواران ترکیه از دیاربکر تا میناب
🔹
حسین دیوسالار، معاون توسعه همکاری‌های علمی و فرهنگی سازمان فرهنگ و ارتباطات اسلامی، از حرکت کاروان مردمی دوچرخه‌سواران ترکیه از دیاربکر تا میناب خبر داد.
🔹
این کاروان متشکل از دوچرخه‌سواران مردمی ترکیه، طی حدود ۲۳ تا ۲۴ روز مسیر خود را در ایران طی می‌کند و با عبور از چندین استان، به میناب می‌رسد.
اعضای کاروان پرچم‌های ایران، ترکیه و فلسطین را همراه خواهند داشت و کوله‌پشتی و هدایایی برای کودکان میناب حمل می‌کنند.
🔹
به گفته دیوسالار، این حرکت مردمی با هدف ابراز همدردی با مردم میناب، ادای احترام به شهدای دانش‌آموز این منطقه و انتقال پیام صلح، دوستی و همبستگی میان مردم ایران و ترکیه انجام می‌شود.
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/696709" target="_blank">📅 22:04 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696708">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
پوتین در دیدار با پزشکیان: بهترین آرزوها را ازطرف من به آیت‌الله مجتبی خامنه‌ای منتقل کنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/696708" target="_blank">📅 21:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696707">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6aed0c7da9.mp4?token=i2UmcwzgiTOtMEfZdOpTyudRxZTDoBENrwvzcfYIncvQUVh53GN5QzS9iACvcNlt0MtRzwOKDNi9Avc43leS9XImPu9vSOmC3vJciwRF7NsMbhvQRtLDy5UZVOxy43FQvJkVnBe5F5R4SQ1PLWU5Xjz1UsJRSvzV9gFB-UJO7g-W3Wvcrr-1fYRI8Vz3VCoNwUUw4xlxK1iIDp8XOXouuUwRXVPbo9AedX7QwOKjhbIo1rPjT2ll--YxrrdByAQeVoqg5j5S5MVL7PPzi4K1gQ8pH7NX9qIREQEwGS9fdnsls4yUUe5ZQxG4LV7ki7cw4vxoPorx1NdPwX13z0b61A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6aed0c7da9.mp4?token=i2UmcwzgiTOtMEfZdOpTyudRxZTDoBENrwvzcfYIncvQUVh53GN5QzS9iACvcNlt0MtRzwOKDNi9Avc43leS9XImPu9vSOmC3vJciwRF7NsMbhvQRtLDy5UZVOxy43FQvJkVnBe5F5R4SQ1PLWU5Xjz1UsJRSvzV9gFB-UJO7g-W3Wvcrr-1fYRI8Vz3VCoNwUUw4xlxK1iIDp8XOXouuUwRXVPbo9AedX7QwOKjhbIo1rPjT2ll--YxrrdByAQeVoqg5j5S5MVL7PPzi4K1gQ8pH7NX9qIREQEwGS9fdnsls4yUUe5ZQxG4LV7ki7cw4vxoPorx1NdPwX13z0b61A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن زنگنه، نماینده مجلس خبر از واگذاری بیشتر از ۱۱۰ هکتار از خاکِ ایران به افغانستان برای سرمایه گذاری افغانستانی‌ها داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/696707" target="_blank">📅 21:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696706">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4764ca307.mp4?token=rIjkmx9IA-zTHY7A_Jy7c1JrofTyGEsSdccJ1QtqS0ES5SrUL4YEtosTP5xKhNRuG9afisAwrCtmcqDXvJGtzVf9bYwBT5_-7hPW6b2O8Xadyuj4VBiWPQNn8O87MtrAJCbJxL_xtaBFwhtVX6bQrFntvFuNuco1YDyO-k1N1bAKPM4gdLi1TjnoSaiuWdPbrR5xkfRTerP9nEPB-Hr4Jg4woB0Q9E07jhFFLcnh1R6lGYWBOr6eC0V6bo24iGGPCPfph5QClyHrNPKhfrXZxa_8ifcX5GavaEJG3_BW79_qmXx7WBFjrczI4LjTDqXYFfcxuJo9i-9nImz31T2Q-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4764ca307.mp4?token=rIjkmx9IA-zTHY7A_Jy7c1JrofTyGEsSdccJ1QtqS0ES5SrUL4YEtosTP5xKhNRuG9afisAwrCtmcqDXvJGtzVf9bYwBT5_-7hPW6b2O8Xadyuj4VBiWPQNn8O87MtrAJCbJxL_xtaBFwhtVX6bQrFntvFuNuco1YDyO-k1N1bAKPM4gdLi1TjnoSaiuWdPbrR5xkfRTerP9nEPB-Hr4Jg4woB0Q9E07jhFFLcnh1R6lGYWBOr6eC0V6bo24iGGPCPfph5QClyHrNPKhfrXZxa_8ifcX5GavaEJG3_BW79_qmXx7WBFjrczI4LjTDqXYFfcxuJo9i-9nImz31T2Q-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علیرضا بیرانوند: به جان بچه هایم به دنبال معافیت پزشکی نیستم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/696706" target="_blank">📅 21:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696703">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WTpTIrYuujT9x8PChafLKerGxUsbQPtDf7frpI9WAnJZtoudXnSC5z1jsqF-fYmUe5yna9FkA8PSDmoj1hGFFS5PkVgJHYEb_-nHOj1oM_Uyf656kqBkdg3Vw3KTmkrgDYHcwSE8s0KR2AaX_cTODgqNC-nzZ7rWjHPGiIIxQ1inX9SMc8zwVyfCnWuJ6p3TqTRCbl2Wa2pixriywwXnQF2vD1qaP42dYUzUiANg_v0wbooI78jFHsdlRRdFqBbtEVrNHMefOsLuJ6x6HV3eomCj13NnO6oD2zOyZtHOJT_fsBQOpgQfC9fk0zQ145aXvZWZ-TDNXmJRS9v2OUPGRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eIQsM7H94od4ruJFRNW605Q7Tv0DY8WcIn1eax-GA_ASO_4VrK4q9JY0SoyCuCvdLFqRlOx6s2oFTO-ews0Z7gRjkqHJs26xbmvLv-wIe7ZCkhKSltbp1WuDkWmguhpCm5iWJN2c17kWMU9__FHKMWAIQq2qzZCIsSCyiUNq--zTaUQOnNsxDL82JPdhpO_aHEvQ2JDvfitARgElRLHBLn3QebvlrBRaoq88lONHlbX5F3cyYX2XXwh3OD5PVR35JyN4sbR4N-rysW48GfwrQeKCCxMxSFrtJUVKhHQQz-OSIQm49L2DheDLg1X0TTcK1FvGDCXe1oNEQEm_l1o9Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q0Fr2X5iOYYujpsU4dd8xAEMPw3-VRXjTRbkOKLYGJr3QW9b4m3OFsYits7Gj1f6oCfzVgz6OTiNYyxOifAMoCPg3Q7YcArxhIzC6XuwbUige8seWABxWdTlSbow3-JfwDKBAD2V9pj4TMNYK4IekXK--0r4SRCcyA2_i8XGBz8-mf-O7GkIal4OD2YcQXCKFN5DE1NuN6784ASnsUvUR2PhuluIgO7GKFhsRSU7bSgL6QvaKLHVFLA6H0e8eKEMw4to7sfjOtwlPNw9t6UWMUU5t-q0R5afkpjGE5yyWbUm9yAr2rIWPuOBC2nT6J348UJwj4tUlIccYdjsxWFp_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
سه تصویر از خطر، هشدار و فرصت اقتصاد ایران
🔹
رشد نقدینگی در شش ماهه ابتدایی امسال در کنار تداوم رکود و کاهش موجود مواد اولیه، زنگ خطر اقتصاد ایران را روشن کرده است. از طرفی شاخص مدیران خرید هشدار انقباض فعالیت اقتصادی را می‌دهند.
🔹
در مقابل، رشد کشاورزی و افزایش ظرفیت صادراتی نشان می‌دهد هنوز فرصت‌هایی برای تقویت تولید و ارزآوری وجود دارد.
#رادار_اقتصادی
@TV_Fori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/696703" target="_blank">📅 21:47 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696702">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b327c4dfe2.mp4?token=bQ9X_zafboeOk-mNrsmZe4N4Jputmjd6uIiqmj4-RmfZAzpEt3vTJv9vjfy8PuPg_gv3Ph8WSQ8zCqPW-Gc-Bnse2YH5LeiMJHHXxJeMqbhDXSPNOG3Ao6cGJOwwjWQUEic6ftrvvmL0xuTwRG1Bij9XMi-QlGqrqIxCQtJdG75BVK7OB1-LbValmenvtRgBdnei7L67kfNW1A782cUr_L_qSwEpRogNX9-_6UnfUegRA56HIZzJgcOx8ho5JuJQM92FaFa2Xnsq3a2YSo_OpjAWFsUgx-c8SWa__ndFztUsbWSTMDHIFg59dZBgqye1bZDAQysyHYHxlR1Emu6Lig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b327c4dfe2.mp4?token=bQ9X_zafboeOk-mNrsmZe4N4Jputmjd6uIiqmj4-RmfZAzpEt3vTJv9vjfy8PuPg_gv3Ph8WSQ8zCqPW-Gc-Bnse2YH5LeiMJHHXxJeMqbhDXSPNOG3Ao6cGJOwwjWQUEic6ftrvvmL0xuTwRG1Bij9XMi-QlGqrqIxCQtJdG75BVK7OB1-LbValmenvtRgBdnei7L67kfNW1A782cUr_L_qSwEpRogNX9-_6UnfUegRA56HIZzJgcOx8ho5JuJQM92FaFa2Xnsq3a2YSo_OpjAWFsUgx-c8SWa__ndFztUsbWSTMDHIFg59dZBgqye1bZDAQysyHYHxlR1Emu6Lig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنگ نهایتا ۲۰ درصد در تورم نقش دارد/ دولت باید فورا بودجه جنگی ارائه دهد و نیازهای غیرضروری را حذف کند؛ شش ماه از سال باقی مانده و دولت دارد کشور را با بودجه‌ای که در بهمن پارسال نوشته، اداره می‌کند!
داود منظور، رئیس سابق سازمان برنامه و بودجه:
🔹
بودجه‌ای که الان در اختیار داریم بودجه شرایط جنگ نیست، چون در دی و بهمن سال گذشته تنظیم شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/696702" target="_blank">📅 21:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696698">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tIbHbJTR1D5nTnd0q-4LwK7xMMqvnyxWO8jIEgjImb7Fe6VeS97cT3C6PfYD66FHemouWkyrK6VkhVM64NOU28r9yOiievkkR6Q0OkfmLO4YiiDzUyV9g_t_dP4-0YFEyP0AkfWCdzs1LhOt1KWO5N_2aVyqgq-EWl2A_4cT-Jk1w1pIuFY_vgPCfojBB4iL4imf7tYOjyOiEjPfdxErb4n1gI7FV6qmrVNkCCK3O8Zl1d-PKkNvaPfJ-IozS5Zwv1A21C_YNkQqwFhC2ui4lRltv_BkNi-QytlmDJdGiTZii_zZ_73lcAb2xH5ZNEkCUyQHAfU9o0MSla0gbgIiXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GrPmxgbDPBCrfFDcW7f8oi6l2z9e5HYkSGUe26FFtDbktg1PV-rejqjiNivxN1CMSB9QUeYadlJJxM4-Oj6mzU5QFrzQEy7fKRU9RNCUumh4oEv56UTMnEelCPCJUNmN1_nHxpK0eZKdsobS9GVvmMkCReBsZR4--vt4ornmD4wgd9fFB-L3q7t173iO9elTvei3HA0XrYeGWaN5yP3041yMXUvWW0m6WfisHEkTNRm2S1d6DcWaTQShl-XLs8t7tBLmMJLozXda2QMi_1XYiR_xprPL82vUlRxkIJTKjiCN20jE0a7G_OS5FOwwY1XeX9zWPuk0rhQOnjwER0oSPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t3ETZ-jcZnXE0fvEZpVefJjabKFhsOPodjU5MQ_hsXAc_zRzimY99cATizw3JaBR3gjIcnhUdSBiNNIVPcQj5n5uhbGdZD5IYkTQ-VKhIr8YOBU4u9EyCLRgvXvNPtp2enhKm5MM1M_WZIOBIDytZWUkhanxBYsnDWDDlAY4E6bces561vbsP-FILsC8dk21ksJFH6_u04jwrCNnfVnUowKOp03zdK1cUmHVnlZbDalZ0lYajd0XwHcMPukaJIY9Ea8zzO8kUG7vfwmB33chJZKFI_tMGdRdgb1o-0S2cOxUCE0WbSvt2Fp62TKiEPWSgOba6y3DfNyhtiLlkBslBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JxiBmvuydvbpIk9K2F2EPgGiL4T2bU6YjxMMgkS-OEOpsqnPVWKw9Vp8u0UYCH19tAaykg_oAOFFzCX5FZ8HdHHnvYBb3tVG58GdzlFmJQfTQCOp7n8vDVpUKaPAqYChHCTMt5P--7zdezWuUI9Nl1-AQXHbVm9MNMdh4gpTflhEe48eo5-wtwRYnXvGMC85ny67HHMQ7Yhh3GtHORzww356JDbRBKqSvkExXBU1R13rMg4RJYjyddGeu1CBcjGi7fhgBtCASjbNh6WzUAqyXKYcCngyjspG6Av6zpAsIUBTWs5x8AbScCfkGs2ZcKwwSX5yiTZYLsLqvoLQ1MwI2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هوس هر خوراکی می‌تونه نشونه کمبود چه مواد مغذی توی بدنت باشه؟
🍕
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/696698" target="_blank">📅 21:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696697">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
ترامپ برای حامی مالی‌اش سنگ‌تمام گذاشت: ایلان ماسک توماس ادیسون عصر ماست!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/696697" target="_blank">📅 21:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696696">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfmYQ9kZoLHtgnVB4ORY7BmL1LePB4QGpbjDSyzcroqG-Jzg5wBS3o0sgslT7v3OhY8u0QtYLkSq4PfSpcU2oP9DOYvSeSgDUk-7PCcP2MYwsq0FP2HAYjePT_8-ZFR7KQ2FSW44tU-v2PGfFQDQrbaf0UmAmG_Hq6ablOcF0oOVKAaUyueqbtwuTFzqGWO5g66FKpYm8PWh_6VRW3efY9QUWGrR7INn5FOgYZk0IBd43ssYy6r7l0_qJcs3AgBNTEOB8jLhOa7QQUUJlZm-xFUqn6muykWsH7M9mDLvU3a4Imase1rcVzXjOswuNYvACfvrxVS06FWB4--QGsUOHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهرزاد مشیری عضو هیأت‌مدیره بانک شد
🔹
شهرزاد مشیری، مدیر باسابقه نظام بانکی، به عضویت هیأت‌مدیره یک بانک درآمد. او پیش از این از مدیران ارشد بانک کشاورزی بوده و سابقه فعالیت در حوزه‌های بانکی، ارزی و بین‌الملل را در کارنامه دارد.
🔹
مشیری در بانک کشاورزی مسئولیت معاونت امور بین‌الملل و عضویت در هیأت عامل این بانک را بر عهده داشته و در حوزه روابط کارگزاری و مبادلات بانکی بین‌المللی نیز فعالیت کرده است.
🔹
وی همچنین در سال ۱۴۰۳ با حکم وزیر جهاد کشاورزی، معاونت توسعه بازرگانی وزارت جهاد کشاورزی را بر عهده گرفت و در حوزه تجارت و بازرگانی خارجی فعالیت داشت. مشاور وزیر خارجه و رییس شورای پولی و بانکی این وزارت‌خانه از دیگر سمت‌های اخیر مشیری است.
🔹
انتصاب مشیری به عنوان عضو هیأت‌مدیره، بازگشت یک مدیر باسابقه و متخصص حوزه بانکی به سطوح عالی مدیریتی شبکه پولی کشور را رقم زده است.
متن کامل خبر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/696696" target="_blank">📅 21:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696695">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quIW4VzZ9smmi-yaKjK5HuX7q75qps5ULOd2ALaS2dtyrh-pspa4wngbprBz8U1dLm0IO_9Gv6wIX4Sd9aZ9rdsMPr1v9Fp9MH_3vvSLRHpj-5Mr4eKRwQNLZCtP_f3cgXHBiU0cKOdfE7dEQEeMsG2vV3TvcpVn4CZwUAQyCllxcp3jwcbv3X4-pOGkJtJmwqUIsBb9sFk-uvlBQelSC0uyTWlP921RVse1_ZTyjdGBPNep6WvGOLq4ejvjO8iOvDXzjvNx35eDgnEWPWORQ4ZG3Pd94YnTgrWYRMlzZiJUfnpN8J5zVRn8u-Hn4YH1jH2ZjzFk06-QQYrMiKRx0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با اعلام باشگاه تراکتور، علیرضا بیرانوند به دلیل مصاحبه بعد از بازی با استقلال از این تیم کنار گذاشته شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/696695" target="_blank">📅 21:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696693">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر TV</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ni6y-dbp1W5_7_ayQSatfLvbNhy-_ex9B1ceF24Fbs8zKqckzEiXZf7H2aU5G2CGU2QmjuZB7ZfnQ1QvOqEfzoAFw9dR88a5HfnZ0ZtCNtWQXCr6g9NxCI-f8I_1ElQSTCEc0XGvHxVxQNAzXH1aXbbKg_6V9YiCJMtk5K1q9kUxyKH5iy-tm-WxeTMSvpYUc2eXE3VIM5jQFEhaC-yYbHZn9UFU89Rj5Was51w5RUJHEokk64VUAgaSPBhArrK8IbENpClVNIVUbiPuc6Hmyr2cqKrAbTYNaCHnC3CWgekZ35sx8AYwwaFIPnKNwitRdeCUVfKO8y3Vgd7Te5QuXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DuaL7jwdqjTC9sOVdOpZeu5N06NHrHyz6vTe2Ra2hDLENBipV_xA5mnhdg9yLXHe_Ikvn44KNBpsKRPfft5P14inx4N2qtV-f72eXrIF3gV6kn89ZctZd4OE_O7Gj41D4kPnNagoTJP2lxAhH2dSYqTiSpSxES2EjP3b3EAjXNCtJi2bGeQBhy4zN4ocn2p_7UhWZ-xHsmijYekAua9YMlzsQMo4wv1jXiSjF-u9HP7yMH4nMkzdnIa9rMgnc856Z5t3aexn3U9RzRMkOeyMV3NeUnX3gnRmZmwslN2Z0HKv9b8WAPnkJvHBCyOz-rAzUbTkafTjj_AFisxeGBIs1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
#اینفو_تیتر
| خرج بازی فوتبال از جیب سهامداران ؛ چه کسی پاسخگوی این حیف‌ومیل است؟
@tv_titr</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/696693" target="_blank">📅 21:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696692">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1061234e79.mp4?token=ViHE6mu8ILL-AVtZL4TJq2Wnfcx9f9oP_ntpTrihnk1Ts9NmnOlMsG8MRLzLOP_9utXvS479O8-VOgZ2PnNZvuUZoJLearymVqzoNdBlu-X0AbAyZi_9uRx1vpTlLGoFwMb7wrGp3bV9EROu2aCF3nVb2jBX34CGM-4pW69hCMjnza_BoMBKn-lx0b8oBxwDisTGmzw7LQKieEdebxMHUd240MYCIEdyYzUA2-hgime-KsWfJSv_LRyrnqjzSXl96JdoMruFPKATLzKPmTZ6FeR-uTyP1A4irILvSWkDACnB0BNzvDUv7Xk2vFohSxI5QoKsxV82gfF6qObKSdsMzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1061234e79.mp4?token=ViHE6mu8ILL-AVtZL4TJq2Wnfcx9f9oP_ntpTrihnk1Ts9NmnOlMsG8MRLzLOP_9utXvS479O8-VOgZ2PnNZvuUZoJLearymVqzoNdBlu-X0AbAyZi_9uRx1vpTlLGoFwMb7wrGp3bV9EROu2aCF3nVb2jBX34CGM-4pW69hCMjnza_BoMBKn-lx0b8oBxwDisTGmzw7LQKieEdebxMHUd240MYCIEdyYzUA2-hgime-KsWfJSv_LRyrnqjzSXl96JdoMruFPKATLzKPmTZ6FeR-uTyP1A4irILvSWkDACnB0BNzvDUv7Xk2vFohSxI5QoKsxV82gfF6qObKSdsMzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۵۰ پرامپت وایرال برای ساخت تصویر با Chat GPT #هوش_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/696692" target="_blank">📅 21:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696691">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae90cd2c5c.mp4?token=gFnjJuM8PVz9wZY4r6dx65k9enXgIMzyWG0HiQZXMkbWIPOUsI7K3qMbfxM6Xs4uFthWo0xlM7GRNGO55jPRucN9SWMX1YBVLNJVU0AdJCyxo6L4tHlUoy_8JTNU3a9ucgfVc-ZoVTU5bVHvM84SRiufpyuBNiiS1SvaPNZvfWQN2FbA9smYcsBphsAQh0jl9Bx-5mIo1y2zQrDyoEag4TkpZb1yus0AK5RNXj6fDdCbT9nVbhqRI512Tx4OSJC47zfAe4zGa9BF8iNNpiIGXlp13VaNyhsrd0MGDOPZhGo9Aj0QEqKNnghoPv4mVn9f7P0NqcUSN2Wx8nFhGqVwHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae90cd2c5c.mp4?token=gFnjJuM8PVz9wZY4r6dx65k9enXgIMzyWG0HiQZXMkbWIPOUsI7K3qMbfxM6Xs4uFthWo0xlM7GRNGO55jPRucN9SWMX1YBVLNJVU0AdJCyxo6L4tHlUoy_8JTNU3a9ucgfVc-ZoVTU5bVHvM84SRiufpyuBNiiS1SvaPNZvfWQN2FbA9smYcsBphsAQh0jl9Bx-5mIo1y2zQrDyoEag4TkpZb1yus0AK5RNXj6fDdCbT9nVbhqRI512Tx4OSJC47zfAe4zGa9BF8iNNpiIGXlp13VaNyhsrd0MGDOPZhGo9Aj0QEqKNnghoPv4mVn9f7P0NqcUSN2Wx8nFhGqVwHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امید در‌ دل ویرانه‌ها
🔹
تصاویری از بازی کودکان در میان خرابه‌های غزه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/696691" target="_blank">📅 21:16 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696690">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
ادعای الحدث: میانجی‌ها از ترامپ خواسته‌اند پیش از هرگونه حمله احتمالی، مهلت بیشتری برای مذاکره با ایران در اختیار آنها قرار دهد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/696690" target="_blank">📅 21:13 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696689">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
۱۵ تا ۲۰ میلیون نفر هنوز سهام عدالت خود را دریافت نکرده‌اند
غلامرضا شریعتی اندراتی، دبیر فراکسیون سهام عدالت مجلس در
#گفتگو
با خبرفوری:
🔹
حدود ۱۵ تا ۲۰ میلیون نفر همچنان نتوانسته‌اند سهام عدالت خود را دریافت کنند و فراکسیون سهام عدالت مجلس در چند جلسه با متولیان این موضوع و دیوان محاسبات مسئله را بررسی کرده‌است.
🔹
پیگیری‌ها برای تعیین تکلیف جاماندگان و افرادی که سود سهام به آن‌ها تعلق گرفته و همچنین وضعیت شرکت‌های سهام عدالت در استان‌ها ادامه دارد.
@TV_Fori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/696689" target="_blank">📅 21:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696688">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dA5VHOSN_Cw_PuLIMzjcBWrF3i21qhbnR3KqcQJS1hKzWUY70oFWz_MX_2MF5WalSpg7RBHtbLfOKSUG0sLDY3sdwWreJwmGPTC_SEqlsi6CHiUB-u5d5bs45L18zem-A5Bhm4mAGgywYzy1u8pxJWxFYxZIlMznaBw89GzgnDalwFBVC1uYMIXnVZpWTh8l3--uY_i1dJjFYYU76-m5G7-3sd6BtV1E4DpVBKoXj4KJDqfWnEsiDobzvkNm2CPKQohFWDQPJiAaF4DhFrQgrlRVwbIoWE_wOp9UOm5kEy1vtvrN7CdqBh4EqR_9GEEgBQmIipcNJF67w6nX1USMTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از افزایش شدید بارش و رعدوبرق در شمال کشور برای روز شنبه خبر می‌دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/696688" target="_blank">📅 21:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696687">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
رهبر انقلاب: استفاده از فناوری‌ها و هوش‌مصنوعی نقش مهمّی در کیفیت مأموریّت‌های فراجا دارد
🔹
تقویّت همه‌جانبۀ نیروهای حافظ امنیّت از جنبه‌های مختلف انسانی، سخت‌افزاری و نرم‌افزاری خصوصاً ارتقاء فنّاوری‌ها از جمله استفادۀ هدفمند از هوش مصنوعی در تحلیل داده‌ها…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/696687" target="_blank">📅 21:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696686">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
رهبر انقلاب: ممکن است خیلی از اوقات زحمات و فداکاری‌های حافظان امنیّت، نزدِ برخی افراد عادّی‌انگاری شود و همین مظلومیّت و گمنامی است که اجر آنان را در پیشگاه الهی افزون می‌سازد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/696686" target="_blank">📅 21:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696685">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
‌‌‌رهبر انقلاب: امنیت کشور، مرهون رشادت و شجاعت نیروهای فداکار فراجا است
🔹
امنیّت، از مهمترین نعمات الهی است و برقراری آن در نقاط مختلف ایران عزیز، از شهرهای بزرگ تا جزئی‌ترین واحدهای جمعیّتی در روستاها و محلّه‌ها، از مرزبانی‌های سخت در شرایط دشوار آب و…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/696685" target="_blank">📅 21:03 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696684">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
رهبر انقلاب: نشانه‌های تأثیر پررنگ فراجا در جنگ‌های اخیر آشکارتر شد
🔹
نقش پررنگ فراجا در سطوح مختلف از رده‌های فرماندهی و ستادی تا کلانتری‌ها و پاسگاه‌ها برای تأمین امنیّت در سال‌های اخیر برجستگی بیشتری یافته است و نشانه‌های این تأثیر در جنگ‌های تحمیلی دوّم…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/696684" target="_blank">📅 21:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696683">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
رهبر انقلاب: نشانه‌های تأثیر پررنگ فراجا در جنگ‌های اخیر آشکارتر شد
🔹
نقش پررنگ فراجا در سطوح مختلف از رده‌های فرماندهی و ستادی تا کلانتری‌ها و پاسگاه‌ها برای تأمین امنیّت در سال‌های اخیر برجستگی بیشتری یافته است و نشانه‌های این تأثیر در جنگ‌های تحمیلی دوّم و سوّم آشکار‌تر شد.
🔹
تمرکز و اصرار دشمن جنایتکار امریکایی-صهیونی برای ضربه زدن به رده‌های مختلف فراجا از بالاترین سطوح تا سرپنجه‌های آن نیز اهمیّت این نهاد را بیش از پیش عیان نمود. امّا این تلاش مذبوحانه و ضربات خباثت‌آلود به ارکان نظم و امنیّت جامعه که مشابهی برای آن در طول تاریخ موجود نیست، باعث نشد تا نیروهای شجاع فراجا ذرّه‌ای از مأموریت خود کوتاه بیایند و حتّی در خیابان‌ها و خودروها، همان نقش و وظایفی که در اَمکنه و مقرهای خود ایفا می‌کردند را به انجام رساندند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/696683" target="_blank">📅 20:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696682">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
سفارت آمریکا اعلام کرده است که از وقوع حملاتی به فرودگاه ریاض مطلع شده و از شهروندان خود در مورد وخامت اوضاع و احتمال بسته شدن فضای هوایی هشدار می‌دهد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/696682" target="_blank">📅 20:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696680">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BpGbOdhrsrNAoVG4RBIYOQR7dn-kEDgPbRC3hyy2ZBylKr2WXTGH3DceohejBzrZ7eRLHmA-dKOEbxm4e0lfruBdsDfjg3lsrYG2aLo9TSgzTG9NMnQ6bDXKade6mVZHW1w7ldkcxHONxr0bvmPwZVFkOAO-AeqtSdK74-RURjMDZE-_MbgFnyvbvHCu_wBme_gMEOKtbC2CuKWpBP_7Pb9dzVuuiZFsCjCNA0JU23QOYoQ0Jg3d2OzTPx3BfCbSOHcyLgWZbV6y6FStEM0bqLT0isZ7fllf9Va1IF-Ds1Kw-SFr6KFegmbcMJVerGrHXow5Os0ogD9ygQ9awlglvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجاهد یمنی: به خدا، حتی اگر تمام جهان متحد شوند تا ما را مجبور به ترک آرمان قدس کنند، ما با تمام جهان خواهیم جنگید. ما به اراده اسرائیل تن نخواهیم داد. ما پذیرش حکومت عربستان سعودی را نخواهیم پذیرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/696680" target="_blank">📅 20:47 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696679">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
وزارت خزانه‌داری آمریکا: تحریم‌هایی علیه چندین کشتی فعال ایران اعمال شد./ الجزیره
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/696679" target="_blank">📅 20:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696678">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-text">"از نسلِ ابراهیم"
روایتی جذاب از تقابل خیر و شرّ از ابتدای تاریخ تا به حالا!
تماشای این کلیپ به همه پیشنهاد میشود!</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/696678" target="_blank">📅 20:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696677">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17b206f257.mp4?token=Sc3EjgTRPr3BADVarV0HGuYl9WQYmzEiMrSrl0UU97_ppoxdUE4E4LT2YVNYqnBppsD6PRyb21kvpGn_MaxsZCGzXDvOJOi8cLtF-iXN4u3i-QNzqBYgdUNRlQmqEiMobdtGmV9BF5JxDRYQ9MpG_Rtmai4Z1Tg9R5SUc0isJgOCbAMwkruCSisti6p_6PY7Hg2qhRsOSFvNeip9DIW8-4qTANLHfA2lUNawqeJCmccWwjxTKLgdDU3swMb-zFO-ZhhLnCCMvJ0CrVhLKNb66M1d6ujZcgF5OFZlby6-sekrOwfKkh1nE_cg3TrBbE07EuVIdgJfug-aVO-xoLKMIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17b206f257.mp4?token=Sc3EjgTRPr3BADVarV0HGuYl9WQYmzEiMrSrl0UU97_ppoxdUE4E4LT2YVNYqnBppsD6PRyb21kvpGn_MaxsZCGzXDvOJOi8cLtF-iXN4u3i-QNzqBYgdUNRlQmqEiMobdtGmV9BF5JxDRYQ9MpG_Rtmai4Z1Tg9R5SUc0isJgOCbAMwkruCSisti6p_6PY7Hg2qhRsOSFvNeip9DIW8-4qTANLHfA2lUNawqeJCmccWwjxTKLgdDU3swMb-zFO-ZhhLnCCMvJ0CrVhLKNb66M1d6ujZcgF5OFZlby6-sekrOwfKkh1nE_cg3TrBbE07EuVIdgJfug-aVO-xoLKMIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمونه یک سنگ اورانیوم و مقدار استفاده‌هایی که از آن می‌شود چقدر است؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/696677" target="_blank">📅 20:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696676">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
وزارت خزانه‌داری آمریکا: تحریم‌هایی علیه چندین کشتی فعال ایران اعمال شد./ الجزیره
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/696676" target="_blank">📅 20:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696675">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
دراپ سایت: تردد در مسیر عمانی تنگه هرمز آنقدر برای خدمه کشتی درآمد دارد که انجام تنها یک سفر، آن‌ها را برای تمام عمر ثروتمند می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/696675" target="_blank">📅 20:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696674">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b629ff176d.mp4?token=uYoheliyE7g7VEW_6M1cYvv-QLI6-sUuIORchGiFcwfEQm5TE-Ii981E50cnNDBWxHyg29GitJonVsDwyccMg0cLYogznI4T3j1NIbTCzVNm8AVhQ1NKLCCZ_-hoLgEsZiZ6IFm9TvBxfvCKmeOyC7BfBMRiw_log2w1-G2ko87ll0ikx1OSRGUtcejipSjNz7i9N4384ro3VWkMgIDTUkjS89j2EN34qWh008KJ8TGSn5KER2KvMXz1aEHfNmka9Ep63oOFw-EJgjQVFq5TtP3P6UmSbTFZ9HX3pskP2L3b5BiC4YBrS6edtoKKm-kEYioM0cknrwM7uUnyst5BUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b629ff176d.mp4?token=uYoheliyE7g7VEW_6M1cYvv-QLI6-sUuIORchGiFcwfEQm5TE-Ii981E50cnNDBWxHyg29GitJonVsDwyccMg0cLYogznI4T3j1NIbTCzVNm8AVhQ1NKLCCZ_-hoLgEsZiZ6IFm9TvBxfvCKmeOyC7BfBMRiw_log2w1-G2ko87ll0ikx1OSRGUtcejipSjNz7i9N4384ro3VWkMgIDTUkjS89j2EN34qWh008KJ8TGSn5KER2KvMXz1aEHfNmka9Ep63oOFw-EJgjQVFq5TtP3P6UmSbTFZ9HX3pskP2L3b5BiC4YBrS6edtoKKm-kEYioM0cknrwM7uUnyst5BUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی احمدی‌نژاد هنوز «احمدی‌نژاد» نشده بود!
🔹
قاب‌هایی که باعث شد انتخاباتی رقم بخوره که کمتر کسی تصور کنه صاحب این عکس‌ها، ۸ سال روی کرسی ریاست‌ جمهوری ایران تکیه بزنه!
#پشت_قاب
@TV_Fori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/696674" target="_blank">📅 20:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696673">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efb7303b1f.mp4?token=TsOVVj8I_709huKUoLe70h7OkTxDAHotphC_aWFYHF9qyZq8NTLIk5gD9OByJ01SEVck5yQafjZ1W07cJ7IKjgbRhKLDaFfxHm5LRxzNhfByQtnfGjM8c4NuXxb8mbWQyKFLsRDB5rvTaFEhFyDCEu7oCnLDM0qCfXrQcNZP3UbCeqHZffeh-V3OywtqKtzgFCFdNrw6PoiZEIzM01BItCfPWiCxtHKcNnEK6OMW4vmUjVZcdtPzLd0XKX961z2Rjzrj7BjIThILIHezhiFmTJ4RpOuDKu3Gqv3mPOt8sFKLm87JXGZjFUlvLe3fmnJk8ot1Y_BK2aqqC25ZGh0zeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efb7303b1f.mp4?token=TsOVVj8I_709huKUoLe70h7OkTxDAHotphC_aWFYHF9qyZq8NTLIk5gD9OByJ01SEVck5yQafjZ1W07cJ7IKjgbRhKLDaFfxHm5LRxzNhfByQtnfGjM8c4NuXxb8mbWQyKFLsRDB5rvTaFEhFyDCEu7oCnLDM0qCfXrQcNZP3UbCeqHZffeh-V3OywtqKtzgFCFdNrw6PoiZEIzM01BItCfPWiCxtHKcNnEK6OMW4vmUjVZcdtPzLd0XKX961z2Rjzrj7BjIThILIHezhiFmTJ4RpOuDKu3Gqv3mPOt8sFKLm87JXGZjFUlvLe3fmnJk8ot1Y_BK2aqqC25ZGh0zeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۱۰۰ جمله انگلیسی که باید بدون فکر کردن بلد باشی!
🇬🇧
#زبان_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/696673" target="_blank">📅 20:24 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696672">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S29RAQ1MdL59KvOdoW9eBBHGqEZk5TKSGsgLlj6V4IK9pypUYl7mxxg_QmDj6L5Z_Uj5i8VEfTpZwfLvDOPwEHFHotBAeBd4cbweApSWkfYZgyx_cpIefu0_Lg_1IzALPQsnj6FweQhsgeXwAKKSegUfsglJWBS4T1fkDGX0HGLbzCSOn-6wr7HQQiuWVryG83WXDobfnmCba8_nZMkRDwxR4It6E7S7coaAdosZV2bZDnJ9uhkNh7f5qapdC7sQBKHqTffQzjL1625fN2SaM9QqMlvSbz8hsf60nZI7Q4Vw8-kB8pH0YD9NRIW4J-nol8T_JEDUmEhGVdiWVXruNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توطئه غرب برای شرق
🔹
امتداد جنگ آمریکا و اسرائیل علیه ایران با توطئه و مکر آن‌ها به پاره تن ایران یعنی سیستان و بلوچستان رسیده است. با شدت گرفتن فعالیت‌های تروریستی در این استان، به نظر می‌رسد این تحرکات می‌تواند روی دیگری از طرح آمریکا و اسرائیل برای درگیر کردن ایران از داخل باشد. سناریویی که آغاز آن با ایجاد ناامنی و اختلال در مرزهای جنوب‌شرق کشور همراه شده است. پازلی که از ۲۳ خرداد ۱۴۰۴ آغاز شده و به نظر می‌رسد در یکی از مراحل آن، ایجاد درگیری مرزی و ناامنی داخلی با هدف تضعیف ایران و حتی فراهم کردن زمینه برای فروپاشی نظام سیاسی ایران طراحی شده باشد. از این منظر، ترورهای سیستان و بلوچستان را می‌توان بخشی از تلاش برای آماده کردن شرایطی در جهت آغاز دور دیگری از جنگ ارزیابی کرد.
🔹
هشتصدوهشتادویکمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/696672" target="_blank">📅 20:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696671">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8651a8c2e8.mp4?token=GiR5YfAf3E60EZVS1bpaO5jyDGEQZk8jx7iZAayr-MeJKhUL0St2rh2ffrjh2QzqF2wwZwesSTuyIbgm3blpj4rmlJAUdeGcGzcdsv4ZgHAw18PUNgzOTSzXzSdULUZ2kyiYFyiufhop0Q7kR8FAxU-fZD3B5NaB5LobPHagSF21rcEP_4OB42T9_lj25jzrwxnQeg9FGNdYXOgJqOepJzhTpUMV7y6Kks0e_Yt6WR7QhwyNauzoL-pEcfK04Do5bhHZEHftDrvNbYqEPDNgLVXZbye1gIdHooYLlXo4u4CYxOq9g2XVvL7eSP_CNGGmu45Q_CEfsgN59dg0TMx-ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8651a8c2e8.mp4?token=GiR5YfAf3E60EZVS1bpaO5jyDGEQZk8jx7iZAayr-MeJKhUL0St2rh2ffrjh2QzqF2wwZwesSTuyIbgm3blpj4rmlJAUdeGcGzcdsv4ZgHAw18PUNgzOTSzXzSdULUZ2kyiYFyiufhop0Q7kR8FAxU-fZD3B5NaB5LobPHagSF21rcEP_4OB42T9_lj25jzrwxnQeg9FGNdYXOgJqOepJzhTpUMV7y6Kks0e_Yt6WR7QhwyNauzoL-pEcfK04Do5bhHZEHftDrvNbYqEPDNgLVXZbye1gIdHooYLlXo4u4CYxOq9g2XVvL7eSP_CNGGmu45Q_CEfsgN59dg0TMx-ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رپ پرطرفدار فارسی در تجمعات شبانه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/696671" target="_blank">📅 20:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696669">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">23-2 Ane Manaee (1404-02-10)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/696669" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه بیست‌وسوم؛ بخش دوم
🔹
تفاوت میان علم حقیقی متصل به ولایت الهی و علم مادیِ متکی بر ابزارهای فناپذیر [00:00]
🔹
تجربه‌های نزدیک به مرگ، انعکاسی از علم حضوری و شهودی اهل‌بیت در زمان ظهور [03:14]
🔹
فهم ملکوتی لایه‌های آفرینش و نقش ملائکه در تصویرگری نطفه و باز کردن قفل‌های دلها و رحم ها! [08:16]
🔹
سرّ "لا فرق بینک و بینها الّا أنهم عبادک"، نقطه تلاقی اراده انسان کامل با اراده خداوند و بازچینی هستی به دست ولیّ خدا. [12:33]
🔹
جایگاه حقیقی انسان، نقطه نزول قرآن و جایی فراتر از توهمها و سایه‌هاست. [19:30]
🔹
حقیقت در تبعیت از قرآن و اتصال به حبل‌الله است، نه در اوهام و محاسبات غلط شیطانی.  [22:38]
🔹
لایه لایه قفل‌های خلقت در رحم، نشانه‌هایی از تدبیر دقیق، لطف پنهان و حکمت جاری خداست. [30:20]
🔹
کلید نهایی درهای همه عوالم، انس واقعی با قرآن است، نه صرف قرائت، بلکه عرضه، استنطاق و دریافت اشارات الهی [35:52]
🔹
حضور قلب در نماز یعنی بریدن از حدیث نفس و دل‌سپردن به نجوای حقیقی با خدا.   [43:40]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/696669" target="_blank">📅 20:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696667">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
ادعای ترامپ جانی: تا پیش از انتخابات میان‌دوره‌ای ( ۳نوامبر ) به ایران حمله نمی‌کنیم/ ما در حال انجام مذاکرات سازنده‌ای با ایران هستیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/696667" target="_blank">📅 20:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696666">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">فروش ویژه «چرم مَنطِـ»
به مناسبت روز جهانی دختر
تا %𝟳𝟬 تخفیف تمامی کالاها
➕
𝟮𝟬% تخفیف بیشتر
و
تا 𝟮,𝟬𝟬𝟬,𝟬𝟬𝟬 تومان هدیه اولین خرید
⏳
به مدت محدود
دریافت هدیه
👇
🌐
manteofficial.com</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/696666" target="_blank">📅 20:01 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696665">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAdad │ آداد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D01KFn3a1U6GZ22G5GgxiOX6zE5fzkyBDBxWnwRp4zzHWuDzX9GtGRAIhhsv30eUDq_bjT56eEPNPNuL3oecNXYL0No3A7XT46R9qlGpu4S3ohewfctUx_neJIlUE5AzUOoX6y0gi4tVFVrxPrWSMgEx8B9-47CSgZgwQucTOc9Nddu52olK6FxrtWxPF7GvuFVCwN1Xk785lGMuOigFVE0ceSrschsyHBfIE3ZZ1ZNcmgydYQbxoEzzFegoxItu0j2VIRk6ddnzopq4FErhYY77wjfpBu37glP_RnrpNOIMGXW8-HA0hFigGy74ano1A09Q5g-VqpEXo6Otg1yjeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
پیش از امضای قرارداد، بدانید دقیقاً چه تعهدی می‌دهید.
یک بند مبهم یا یک‌طرفه ممکن است بعداً هزینه‌ساز شود. با «آداد؛ دستیار حقوقی هوشمند» قرارداد خود را بررسی کنید تا بندهای پرریسک، تعهدات و ابهام‌های آن را بهتر بشناسید و برای اصلاحشان پیشنهاد بگیرید.
👇
بررسی قرارداد با آداد:
https://go.adadai.ir/wkHN1Rb</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/696665" target="_blank">📅 20:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696664">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
انفجار و آتش‌سوزی در دومین پالایشگاه بزرگ ونزوئلا/ آتش‌سوزی این تأسیسات را به تعطیلی کشاند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/696664" target="_blank">📅 19:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696663">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GcGskWM7ly7Id8KcakywxR01yxeDjrIYfelANEv0MDQBApAoAf5U1VQeJ_tqXRKMuHSTvNoHvw_MxVLM9Wt8mKx8bkxlerafOrMh71WmjyClfIZrUusyXLzKiei62cSTMsf4LCauVYD3KhNm1k_cWeDRQnCEWBRVtmeLqD-_bi1rUN2lDvpTQjzUKVYVCgYoUERzeBe0k3adcIoUZuhf_YVs18ctV6A3LEVFkgl1lT-tDDbHK1hCNBoFeuJ7WUEbN6p9laiA2lH_-LN5zfmCL4_QkSTj_Mx7bTUvsYfS1tu1j-PX9qS5x9DwVfnfr2QakqQvAYC4Pk21CEjrE_vitw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اظهارات ترامپ دیوانه: اگر می‌خواهید مشکلات را ببینید، اجازه دهید آن‌ها به لس‌آنجلس حمله کنند یا به مکانی مانند سن دیگو. اجازه دهید به یکی از شهرهای بزرگ ما حمله کنند/ این همان چیزی است که به آن "مشکل" می‌گویند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/696663" target="_blank">📅 19:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696662">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9964c26be.mp4?token=Mc6YbFkUbe8Oq_psoy7ft4jwm13oPghbsY0_cPw9gHCDp5sJxYHHiAtTdD2exCAqSLM6pS2hOv066MbWIBo7XyIWO7HBNo0K3_5-rgHyuin7xc51oJ9Bc9s8QitIu4dv7dgJPdjPpXnEXc0aw0H_nL_qRQIgj_bMuTSsg9gHlc4ej520mh_Nj6frHIxNHLerun8hVOe_DUjvzTUhR1zGaZSOQHChL4GRreEmIOEk3SRuUML2hmbhPzR_J6WWGxu5ds8I6__h1vxLngdbGTMTu-LziUmDJkNWe9CDFe1fu-VVIRmUv2edRDP8PS8lIJzCjLs3MQcIH-CEQoLlxw8iOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9964c26be.mp4?token=Mc6YbFkUbe8Oq_psoy7ft4jwm13oPghbsY0_cPw9gHCDp5sJxYHHiAtTdD2exCAqSLM6pS2hOv066MbWIBo7XyIWO7HBNo0K3_5-rgHyuin7xc51oJ9Bc9s8QitIu4dv7dgJPdjPpXnEXc0aw0H_nL_qRQIgj_bMuTSsg9gHlc4ej520mh_Nj6frHIxNHLerun8hVOe_DUjvzTUhR1zGaZSOQHChL4GRreEmIOEk3SRuUML2hmbhPzR_J6WWGxu5ds8I6__h1vxLngdbGTMTu-LziUmDJkNWe9CDFe1fu-VVIRmUv2edRDP8PS8lIJzCjLs3MQcIH-CEQoLlxw8iOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در پی درگیری لفظی میان راننده یک نیسان و یک موتورسوار، موتورسیکلت واژگون شد و نیسان نیز در آستانه واژگونی قرار گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/696662" target="_blank">📅 19:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696661">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
وزیر آموزش و پرورش قول افزایش حقوق معلمان را داد
ولی‌الله بیاتی، سخنگوی کمیسیون امور داخلی مجلس در
#گفتگو
با خبرفوری:
🔹
در جلسه کمیسیون با وزیر آموزش و پرورش، مباحثی مانند سرانه‌های آموزشی، حقوق معلمان، ارتقای کیفیت تحصیلی و کمبود معلم مطرح شد، بخشی از گزارش وزیر قانع‌کننده بود و بحثی نبود اما وزیر در این جلسه قول افزایش حقوق معلمان را داد.
🔹
دولت در حال حاضر به دلیل شرایط جنگی، توان تأمین منابع برای افزایش حقوق را ندارد، هرچند تورم و گرانی فشار شدیدی بر مردم وارد کرده‌است، اگر منابع درآمدی تأمین شود امکان افزایش حقوق وجود دارد.
@TV_Fori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/696661" target="_blank">📅 19:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696659">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aega7VnfJ2f2eWCIm1asT_A7DHYgv1d8bGSpJj-ghU1Oze8S3tGNWAsthqgEyuulHnjP5Z0pZTTExNkYdzLuTB5-ucqmcApGdwj0kSjjILTI7jS5ZqAakipX6QY54WxwVEJSPAwvc0K5NP4iOV2l0h5Oki9hUXdfw4NoFzWoMBU9L0ltkCcueuj1OzjlQFOf90qF2kwIXkufJ_pHkNNaBMB74gmLYjAzn7Wq0Oy0Mh12RTy8Iasv1NTT6ugrSdIwbemaUvhjjWeM1VySLD6jmdsqEDD6ylO-wQwt7VhDMRxaiDFE6FiuxP40psy3A3wjqqwExlAnyZW_bqPL7v_rAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1182817ce.mp4?token=DCAlnWDf6PQq6zwdjUdmzFOejEMkkgUlf-Gw1YTKxfcnwa-ay8DEr-BxpXhuVuXlkSMlrdMuNGfsyyTMZ9mxjcyWw1LSJFda4pLRY-i1Ycgcs2sLmvwngXUcez75KxjvZzHwJapNxvf7-3u3CYDz1174bZtWp7PdBORSvOA75HbmL1pfGQIveKOd3oWjernKfv5V4Vhlqgd424IBTLOOiIbx-yM9thhyDjs7X1JoWp9vWhFWFqQCmVNMtEnPxueeZniojqc2yvHucaXklw5Jmr1pU2_MrIu7LPDz9L6DULNxdjdBQaHxtjrid1SFkAUo3gv7M0jwZuk_ubjWLDwcWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1182817ce.mp4?token=DCAlnWDf6PQq6zwdjUdmzFOejEMkkgUlf-Gw1YTKxfcnwa-ay8DEr-BxpXhuVuXlkSMlrdMuNGfsyyTMZ9mxjcyWw1LSJFda4pLRY-i1Ycgcs2sLmvwngXUcez75KxjvZzHwJapNxvf7-3u3CYDz1174bZtWp7PdBORSvOA75HbmL1pfGQIveKOd3oWjernKfv5V4Vhlqgd424IBTLOOiIbx-yM9thhyDjs7X1JoWp9vWhFWFqQCmVNMtEnPxueeZniojqc2yvHucaXklw5Jmr1pU2_MrIu7LPDz9L6DULNxdjdBQaHxtjrid1SFkAUo3gv7M0jwZuk_ubjWLDwcWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله به بزرگترین پالایشگاه نفت روسیه
برت اریکسون، استاد دانشگاه:
🔹
ویدئوهای اولیه ظاهراً نشان می‌دهند که پالایشگاه نفت اومسک روسیه پس از حملات اوکراین در آتش می‌سوزد.
🔹
این بزرگ‌ترین پالایشگاه روسیه در سراسر این کشور است. همه‌چیز برای بازارهای انرژی دارد به سمت بدتر شدن پیش می‌رود.
🔹
یک مفسر آمریکایی جنگ روسیه و اوکراین: این پالایشگاه، یکی از جواهرات ارزشمند  است؛ این تأسیسات روزانه ۴۴۰ هزار بشکه نفت را فرآوری می‌کند و...
🔹
۱۱٫۵٪ از بنزین روسیه
🔹
۹٫۲٪ از سوخت دیزل روسیه
🔹
۱۵٪ از سوخت هوانوردی روسیه
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/696659" target="_blank">📅 19:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696658">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOVss--1gXjjVDmchoQmVRiBGmJC1WSaDx7PUwVlBkttpanVmPiyt_xWZt9LqUFOHpsGhV8flfwxHrc9L602AwwEMonA1Jr83385b1FSaw5BBl_8wX4wLsXh6FC7mvV_coKlkiRxr5iZsMXveacvBYsSSnGQG5Zn3qjwxwlyNq0NoxDjBTKl_b1HDTcCrjP8aKKAtiSmzdsaGMUoEi3Y8iiL0wZovuFQbCqIBOnsvGDrqcJ9FTQaBQ_FQgatOQqcY9EyhaFNN0AtAGQD9N36DN4xTYg3iODBdvfKVQpH41aw764wfSQ8C1X-rWNRflWWRm00ak-ZbGg-pK0J408iYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ستون‌های دود در پالایشگاه ابقیق در شرق عربستان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/696658" target="_blank">📅 19:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696657">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVuWS1_fBuS636E0ch_9II7petqLNpLJnVbUyUlx6MnT7pnykD8IzoRpwvya5ntAYg7srtLRmFMpkRg1eSC-hAbSqbpt6CIePHmkp7QWGq-fTicZnUN_JsJPLfzAsLALxEMMjClE8z44mqn1qlQ3XP_nymgzCSkkEScon7AhP0NPM030CK4c0SBfY73VlKiXuiPnT1GNPmdSoQI1fHYbSspn9oruGBj514eUAYRkzKgLehBRbktCra8k0FPCdNOQy8O5XMD9vTA45_o5MJYcjEF360vHHt7jkHaa4RPi-h416Vx58AOSPkYPEGsa9Ykp9j2Kf0iiL7p46DMspahWXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سی‌ان‌بی‌سی: یک ابرنفتکش برای حمل محموله از سواحل خلیج مکزیک به چین با کرایه ۷۶ میلیون دلار اجاره شده است؛ رقمی که ۱۰ برابر سطح پیش از جنگ است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/696657" target="_blank">📅 19:24 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696656">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار مشهد</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dba5db5421.mp4?token=OhHrpJiShMjTycuRmKK_rz8MPpQEYOgvvB21abOWN2rNjOilfKRqkyGxvbjzsz4WwijMR7kxXOxo1hv5gvHIY3XQyXQfxqrwzC5rpHrLfOEYKELdaE92Dp0WvO-K10xn4mo5HmN2bJRRx-PXFtfWN0SH3H_YG2mxoCpX86B2P74W5DzbAhlvVm3uJ2UPi6hOcnXM9vSmtmBq085l1JRkJ0Wf3nl11BcWW0AHvrzWuq-aH36g5vEGiBtVYv0zja0RpiuZAmQ01ZZhS0O1bYCWI4KX7M-5gCi2Sbx9Vl3UvATrEgVZc_dR091vWTOaKiD25UOMOPI_CsU9l8oSyVk3b0nui0iO-vKb35z1QmL3i8kAPxgDQvxx0PaNKLOyVBA3J0GgVvqEeopc5_5xA1-sH1ptyLDrnZp3GWspZHFZ_RDNeIihJFK9RJOT1KTqDlI8FMHZaVmqaCC3aA_SU3y6enIritD6HzanvGav8OOLFp_VSiJ7brtc-wR4qQhe4-xcELsBvDhanr2ejDhf7FwjAy826gAc62ergBj_GBVp-AwHGz5cdaUjCQqAUfOM5QOfuVej_HEQbUBL-kDFs8NGnOo6TeeLytUj5jB9-9cysDFF9W9InnWLnNz30z7Z8w4vNS_Ox_ec0_8SWyQxDfdkkbU8E1Phgp6DagDkB1kGK5U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dba5db5421.mp4?token=OhHrpJiShMjTycuRmKK_rz8MPpQEYOgvvB21abOWN2rNjOilfKRqkyGxvbjzsz4WwijMR7kxXOxo1hv5gvHIY3XQyXQfxqrwzC5rpHrLfOEYKELdaE92Dp0WvO-K10xn4mo5HmN2bJRRx-PXFtfWN0SH3H_YG2mxoCpX86B2P74W5DzbAhlvVm3uJ2UPi6hOcnXM9vSmtmBq085l1JRkJ0Wf3nl11BcWW0AHvrzWuq-aH36g5vEGiBtVYv0zja0RpiuZAmQ01ZZhS0O1bYCWI4KX7M-5gCi2Sbx9Vl3UvATrEgVZc_dR091vWTOaKiD25UOMOPI_CsU9l8oSyVk3b0nui0iO-vKb35z1QmL3i8kAPxgDQvxx0PaNKLOyVBA3J0GgVvqEeopc5_5xA1-sH1ptyLDrnZp3GWspZHFZ_RDNeIihJFK9RJOT1KTqDlI8FMHZaVmqaCC3aA_SU3y6enIritD6HzanvGav8OOLFp_VSiJ7brtc-wR4qQhe4-xcELsBvDhanr2ejDhf7FwjAy826gAc62ergBj_GBVp-AwHGz5cdaUjCQqAUfOM5QOfuVej_HEQbUBL-kDFs8NGnOo6TeeLytUj5jB9-9cysDFF9W9InnWLnNz30z7Z8w4vNS_Ox_ec0_8SWyQxDfdkkbU8E1Phgp6DagDkB1kGK5U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
واکنش وزیر آموزش‌وپرورش به مشکلات معیشتی معلمان
علیرضا کاظمی در گفت‌وگوی اختصاصی با تلویزیون اینترنتی «مدار»:
🔹
شکاف حقوق معلمان همچنان وجود دارد و اقدامات صورت‌گرفته کافی نیست؛ با پیگیری ویژه رئیس‌جمهور و برنامه‌ریزی‌های انجام‌شده، به‌دنبال ترمیم اساسی این شکاف‌ها در بودجه سال آینده هستیم.
گفت‌وگوی کامل در یوتیوب
👇
https://youtu.be/m5c6CNUMRxY</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/696656" target="_blank">📅 19:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696654">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vl8iWURtsbpBBOEyQ27qNCXauaDK4k4ALQdEt2H3UiDNVHGnUe2qfvYuXZth-aIYS8-8f9jXpFr4amjvobBRNUyvsGSXCrV4AUqr7id35AVfmcVo2Tn8gUd6DGtXdZV2cMcWCT1_qUD_0nUkKaUpy0YL6IBtMPfPGLBBY7JjfLXTIfXdRaNtvsgV4OHA0TTZ-K8GaVwSMjmWtq-4Fr--jnDD7zjO9TTr1a5OruQEnBoY6HcWEm1g0KbNBzCO_nwvjj8sJZhjl4pdJ6idAABN8yJG3kiRpH5a3I0RXHjfzrogAY6MLM6GAwsclkLpaq5sEygzHg-oxmF3bDF2SPaMAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6172a23e39.mp4?token=n6PrwzuaLSAbqKyF6uuxYAmICr5zhoHJB2e_xnenRhya4EgOh9uWK23JDF0ejEUyVNShwZPaW2WapcxcHXdbKT0GdN6sxZXX8rrE0MsPIWubwPEIXHmqRVT_4gdl8YM6AJCC87fz6l98G1dId3o8DEJhKE0JmmdNGAuuN2znuyLNbvLvnxlrQC5IngHjfb-tNnnsntRH6pXXRg6-dT3mhC6T7cQDxENCfwjAG7dNHEsfZ4Si358SZzdBsmkoVjJ2MJZajxVyToDof3H_Uri7UfXVJdFeohaJWY1oTv3EHJf6JwFbpCRSMf9hI6Y-apDo2htrRI6i1o9PhOI-glsuug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6172a23e39.mp4?token=n6PrwzuaLSAbqKyF6uuxYAmICr5zhoHJB2e_xnenRhya4EgOh9uWK23JDF0ejEUyVNShwZPaW2WapcxcHXdbKT0GdN6sxZXX8rrE0MsPIWubwPEIXHmqRVT_4gdl8YM6AJCC87fz6l98G1dId3o8DEJhKE0JmmdNGAuuN2znuyLNbvLvnxlrQC5IngHjfb-tNnnsntRH6pXXRg6-dT3mhC6T7cQDxENCfwjAG7dNHEsfZ4Si358SZzdBsmkoVjJ2MJZajxVyToDof3H_Uri7UfXVJdFeohaJWY1oTv3EHJf6JwFbpCRSMf9hI6Y-apDo2htrRI6i1o9PhOI-glsuug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از فرودگاه بین‌المللی ریاض پس‌از مورد هدف قرار گرفتن توسط یمن
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/696654" target="_blank">📅 19:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696653">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qshm2EyBW_fVDXSKcSw320iujku2XVD5CEUdoYMcrDyJWYc2WENC5CsvXJFAwSA-yUw8Qyc_n0SaZhTFayP8BuRvn_6akR-gTcLtR7eoYyqmNzo6V5AWPlX0pXFAl2hc1LU2ecLNQBBEmocSNwndssPLRnjAqZ9jWASu_1uPhkWYAZXjLxlFq6oWNdzI_2DDwxLJfm5u7wxlc2YtsQjybbO5SIPw8aocIvkvEwnSynBzaT4AX6UiY8CpGyo_DD1WvAw0S0yXSGBCVkbSqmoHlKbCv9j9JF_m_MuJGrEYyHGg8Cu23BrMuMoKKsunAGlbUdKTMg1lhmVsNfcBVRBffQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک هواپیما از نیرو هوایی پاکستان وارد تهران شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/696653" target="_blank">📅 19:19 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696652">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
واشنگتن‌پست: خروج مخفیانه بمب‌افکن‌های B-۱ آمریکا از پایگاه فرفورد بریتانیا، نشان‌دهنده توان ایران در استفاده از جنگ نامتقارن برای تحت فشار قرار دادن آمریکاست
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/696652" target="_blank">📅 19:17 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696650">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c3730114.mp4?token=FalOBowk2zhXuDTSbUgww-FFJuiFJczJsuxiyV17_Vfq91poTeWbIEg5uew-NPhjmHPHzNqy0dJ1jTrBo8ZpWlNg-Y0sRb9yVQ8oZVGYjbSrgaCFUOah64eyeg9_YNnuZ-kzG0IRQb35qsw2o93mU7Osmjh5qJXVwTu4KVpMHkdRTRcSTEtLAnbPG-SJa1zOatZ7riKMhY7E-Aw5spzhcvArOI6o-jXEG7vrrpVr94HW2TMOtHvhZVj2qyuqR_p_kaiW7EQIpRl4mHAuLj6KyV0zyPe4-lTw-TtlaI_AD7UqZ2q5gCdCakUifJ-_6J_D6HC8jpZKWtwSfeuLE6KFDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c3730114.mp4?token=FalOBowk2zhXuDTSbUgww-FFJuiFJczJsuxiyV17_Vfq91poTeWbIEg5uew-NPhjmHPHzNqy0dJ1jTrBo8ZpWlNg-Y0sRb9yVQ8oZVGYjbSrgaCFUOah64eyeg9_YNnuZ-kzG0IRQb35qsw2o93mU7Osmjh5qJXVwTu4KVpMHkdRTRcSTEtLAnbPG-SJa1zOatZ7riKMhY7E-Aw5spzhcvArOI6o-jXEG7vrrpVr94HW2TMOtHvhZVj2qyuqR_p_kaiW7EQIpRl4mHAuLj6KyV0zyPe4-lTw-TtlaI_AD7UqZ2q5gCdCakUifJ-_6J_D6HC8jpZKWtwSfeuLE6KFDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هنگام توقف پشت تریلی یا خودروهای سنگین، فرمان را کاملاً صاف نگه ندارید و کمی بچرخانید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/696650" target="_blank">📅 19:07 · 16 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
