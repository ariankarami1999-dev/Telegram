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
<img src="https://cdn4.telesco.pe/file/HtnMrrJ1lQeqaBJfVORtEqAYD1FzMl5-eR46MYMvY2NoziFLXbZyteJ5aV3F6m7RWX99xkXjAlMzccdjhd3sOiNZmaSezJDjku012F-lBnqk216XSOWqECb-N8-6Fla_3b0ybkf1TksxBx_PzePtgo08ACORPe3bn-VRZ_99DqvuxbSRUUvrVM6bztzx-pev0a9VBcaSuIYYqbCIUHzrNeRpRfoHhnuxPwz4tuOhR11v1dMHOOSsvEtIfY61rcHxzjcLbMYhNH15tO0MaMjgoHDn74zhdts16ihTwN4W6G2TqZ4EpQ8MGocn-dKt1-hQjsVH65wLeCGQsnTbH6yUcQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.2M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 18:01:45</div>
<hr>

<div class="tg-post" id="msg-664611">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0IIdtcgNI8_csEmHAvr43VWar9Vpoc6akNfAwynNGpD8GS9w5qZ_JGQN0fbbj-aMrUGeGUdBgowm-uezKAKlyuu7MghZIclfBReXQTX9H9jMQ9Q-_5zgEhf0NHIwKxL7ocIC5i4MufTtQ9GgtQZ9-tIKxnm0U0gv_S6rIY_HF5HfWCZJh8PSvpV24oxAgu6kHMhFqOOUKbZxg-62HK1Ip7R-eRQz8bTCk5VyMLJdSsF_c71JPV-x8KTsBMNRL_NtlxOhzQhviC7gJgZdO49Nd8cAVV1-Ltjft89z5pdsxQhOVm1OSK5eZhl5eoE3GxFMIlVYqQwLcryOdZiRQu2Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بهشتی؛ اندیشه‌ای ماندگار
🔹
سید محمد حسینی بهشتی را بیشتر با نقش او در انقلاب اسلامی و بنیان‌گذاری ساختار نوین قوه قضائیه می‌شناسند؛ اما کمتر کسی می‌داند که او سال‌ها در آلمان به زبان آلمانی با دانشجویان و کشیشان مناظره می‌کرد و اندیشمند اسلامی روشن‌اندیش…</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/664611" target="_blank">📅 18:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664610">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
قطر فعالیت‌های دریایی خود را تا اطلاع ثانوی متوقف کرد
🔹
وزارت راه و ترابری قطر با صدور اطلاعیه‌ای اعلام کرد به‌منظور حفظ ایمنی عمومی، تمامی فعالیت‌های دریایی در این کشور به‌طور موقت متوقف می‌شود.
🔹
این وزارتخانه از تمامی مالکان و استفاده‌کنندگان وسایل دریایی خواست موقتاً از حرکت در دریا خودداری کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/akhbarefori/664610" target="_blank">📅 17:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664609">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
دیوان عالی آمریکا درخواست ترامپ در پرونده «ئی. جین کرول» را رد کرد
🔹
دیوان عالی آمریکا از بررسی درخواست دونالد ترامپ برای لغو حکم پرداخت ۵ میلیون دلار غرامت به «ئی. جین کرول» خودداری کرد.
🔹
پیش‌تر هیئت منصفه در سال ۲۰۲۳ ترامپ را در پرونده سوءاستفاده جنسی و بدنام‌کردن این ستون‌نویس سابق مجله Elle مسئول شناخته بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/akhbarefori/664609" target="_blank">📅 17:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664607">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEhtq4TVscvsVm8W4H4xp5d_W9rE0Qt3Xb0XIqDjqh8kl_s9nThMTEQLiUAIjrkf520kQZBWSvTzzaI1dwjP0Tx-KQQ9lcPICypw_97o8RcpW6NiJUCYYTm0sfVYohG7Mx25j0q1f5ZLr69J5VbhF3mtx2W67PDwAvTxDNp8v7m36Dz3yAmTVpIBXqhGcTGAvPtRSzxFSZEBQOuQBKucX6CCWKHp3AseAlzlqeKSFYlRNNntHAO0Svh1gC0osxo74FKVJG9Q96LmEwJaPnItwLJYQklHSc2tItuv39vwvcPeUZX6_ZnAK6vdwTH6L7Gl0RwGqcQnyTX-oqwYlcmW0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واضح‌ترین تصویر تاریخ از کهکشان راه شیری ثبت شد
🔹
تلسکوپ فضایی «اقلیدس» متعلق به آژانس فضایی اروپا (ESA) با ثبت یک موزاییک کم‌سابقه، باکیفیت‌ترین و پرجزئیات‌ترین تصویر از راه شیری را منتشر کرد که در آن حدود ۶۰ میلیون ستاره قابل مشاهده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/664607" target="_blank">📅 17:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664606">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
تنها ۲۵ درصد آمریکایی‌ها جنگ با ایران را ارزشمند می‌دانند
🔹
نتایج تازه‌ترین نظرسنجی مشترک رویترز و ایپسوس نشان می‌دهد تنها یک‌چهارم آمریکایی‌ها معتقدند جنگ با ایران ارزش هزینه‌های آن را داشته است. این در حالی است که نگرانی‌ها درباره دوام آتش‌بس میان تهران و واشنگتن رو به افزایش است.
🔹
بر اساس این نظرسنجی، توافق موقت اعلام‌ شده از سوی ترامپ برای پایان دادن به درگیری‌ها، حتی در میان بخشی از حامیان او نیز با تردید و عدم اجماع مواجه شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/664606" target="_blank">📅 17:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664605">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
افشای تخلف ارزی ۱۵۷ میلیون یورویی در شرکت پگاه
🔹
بر اساس سندی که به دست خبرنگاران رسیده، گروه صنایع شیر ایران (پگاه) از سال ۱۳۹۸ تا ۱۴۰۳ بیش از ۱۵۷ میلیون یورو ارز حاصل از صادرات را به چرخه رسمی بازنگردانده است.
🔹
این شرکت زیرمجموعه صندوق بازنشستگی کشوری و وابسته به وزارت کار است و حدود ۳۵ درصد بازار لبنیات کشور را در اختیار دارد./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/664605" target="_blank">📅 17:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664604">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eM598rEquyI9ZsGT9VYoNhfPL-t621u2VrbXmRP-R1AN9MU877T5NRhojBhusC-fyEhDNdB7xOy0EJcW7XIcc1e9OX36-Qmat6K0jQSO-bFynzvBvdNWuWn5GiAxNVsfvjGpRINVMq6zPd1akh1Z4fpRhTUpjU14JbzNp_VtQrMQlXyOpnBuY0lCPKjETtetOxv0rv-ykfNa_RR-3zE9QNraDZyVYu8igc_3X4Rc322VW8LRnQpH-qe5hAjJaGe5jEhfvtuRntF79Mf3q3x-2_e2r3eWjIHs2Mw5gZjdf3ad028qRZnDuYlulxjB6K53LeBQzNeG1Rc7FpS16GY0wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری | اختلال در خدمات بانکی
🔹
اگر در ساعات یا روزهای اخیر به‌دلیل اختلال در خدمات بانکی با مشکل مواجه شده‌اید، تجربه خود را برای خبرفوری ارسال کنید.
🔹
اگر انتقال وجه انجام نشده، کارت بانکی‌تان دچار مشکل شده، از خودپردازها یا همراه‌بانک نتوانسته‌اید استفاده کنید یا هر اختلال دیگری را تجربه کرده‌اید، جزئیات را در کامنت‌ها یا دایرکت برای ما بنویسید.
🔹
نام بانک، نوع مشکل و اینکه آیا تاکنون برطرف شده یا خیر را هم ذکر کنید. روایت‌های شما را پیگیری و منتشر خواهیم کرد.
🔸
تجربه خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/664604" target="_blank">📅 17:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664603">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
جزئیاتی از نامه ترامپ به رهبر شهید درباره حمله نظامی به ایران
در کتاب جنجالی رژیم چنج که این هفته منتشر شد آمده است:
🔹
به گفته یکی از مقامات ارشد دولت آمریکا، ترامپ کاملاً در تصمیم خود برای دستیابی به یک توافق با ایران جدی بود و این، برخلاف آنچه بعدها برخی ادعا کردند، یک فریب یا تاکتیک ظاهری نبود. ترامپ واقعاً اطمینان داشت که می‌تواند به توافق برسد.
🔹
ترامپ پیش‌تر به اعضای تیمش گفته بود که می‌خواهد نامه‌ای مستقیماً برای آیت‌ الله سید علی خامنه‌ای ارسال کند. ویتکاف و والتز پیش‌نویس اولیه را تهیه کردند.
🔹
خواسته‌ های مطرح‌شده در نامه صریح بود: مذاکره مستقیم درباره برنامه هسته‌ای، همراه با تعیین ضرب‌ الاجلی برای رسیدن به توافق. بدون غنی‌ سازی. بدون حرکت به سمت ساخت سلاح هسته‌ای. بدون موشک‌ های دوربرد و دسترسی کامل بازرسان به تأسیسات
🔹
ترامپ امیدوار بود این مسئله به‌صورت مسالمت آمیز حل شود؛ اما همان‌ طور که در نامه به‌ روشنی آمده بود، در غیر این صورت اتفاقات بسیار بدی ممکن بود رخ دهد.
🔹
ترامپ سپس پیش‌نویس را برداشت و تغییرات و عبارت‌ های مورد علاقه خود را به آن افزود تا به گفته خودش نامه زیبا شود. او با افتخار درباره این نامه برای اعضای کابینه و کارکنانش صحبت می‌کرد و گاهی آن را برای برخی از مهمانان منتخب در دفتر بیضی با صدای بلند می‌خواند.
🔹
وقتی مطمئن شد که متن دقیقاً همان چیزی است که می‌خواهد، از ویتکاف خواست به ابوظبی پرواز کند و نامه را شخصاً به رئیس‌ امارات متحده عربی تحویل دهد تا او ترتیبی دهد که نامه به دست آیت‌ الله خامنه‌ای برسد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/664603" target="_blank">📅 17:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664602">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0W-G2dnHy90UXLNF82lR8HdLqcvHGw3Icclj0UPVtIjlmdbZbw3HF171HzZrS4oyz-FyFp34l0wR8g2dw5_2ZQIgOhAgd3roZAUp4yQaTOgbIzERh478eh34JstXFanAxummgEuF_2zPl6cOiE43kJjeA1ZOfv0wgPZ5ZoxD1e9Bm6d7w-w6qIN_vTHr287OmHYelmx24iNpMQYWhlT8qrl-7__gOTBTGfrJHdXIYDurrbV2JdYri2v6fC3A9z0B9uJNw2Iny4lda_dfyGO2vB3hKcwxrtNgYHOtSim2denym7rzv-I03O_tW8K7TYDgy-uCRU_J2gglql1Nl3L5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای برخی تحلیلگران درباره پیش‌بینی رویدادها در جلد اکونومیست
🔹
برخی تحلیلگران مدعی‌اند تصاویر مندرج در جلد سالانه اکونومیست به ۱۲ ماه سال تقسیم می‌شود و به رویدادهایی مانند بازداشت مادورو در دسامبر، آغاز جنگ آمریکا و ایران در مارس و برگزاری جام جهانی در ژوئن اشاره دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/664602" target="_blank">📅 17:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664601">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qk9Fy86jkCGN1w_RiKxBW8jyg34NekXS3lS9qiakEIGPf8d4FVAsDvIrJapyZy-BPoKrkJWuJK3t5BisS2mwdsO1ZN9uZAeNcqSqsCb1Kh9x1x3zm9FeW3I-n-k-Mapz6Q28E5cbRB4xmw1s0deJ084xA4Z-Ul26gM4wjYPtNWchETTkHPyuLJn2wmvcQ4gwaiFsyA6yny6QYr1cj_gSZcqwlI9f-fCWlLqz-3HIzsc_8dHkuHC4oLd0_Xsk5Eu9zdoD0_vMLNRF9Ved1WgDhmzt9TcuN1OKhPpbhbqIXIYZWQ8pnN5tQBxwYuCkzKO4e7GSNqQoiluGoqPkmWR9Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بانک شهر برای جذب نیروی «بانکدار» آزمون استخدامی برگزار می‌کند
🔹
بانک شهر به‌منظور تأمین بخشی از نیروی انسانی مورد نیاز خود، از میان متقاضیان واجد شرایط، در رده شغلی «بانکدار» نیرو جذب می‌کند.
🔹
به گزارش روابط عمومی بانک شهر، بر این اساس، فرآیند جذب از طریق برگزاری آزمون کتبی و با همکاری مرکز سنجش دانشگاه آزاد اسلامی انجام خواهد شد و متقاضیان واجد شرایط، اعم از زن و مرد، می‌توانند در این آزمون شرکت کنند.
🔹
داوطلبانی که در آزمون کتبی حد نصاب لازم را کسب کنند، به مصاحبه‌های تخصصی و عمومی دعوت خواهند شد. در صورت موفقیت در مراحل ارزیابی، فرآیند به‌کارگیری آنان مطابق ضوابط، مقررات و آیین‌نامه‌های داخلی بانک شهر انجام می‌شود.
🔹
بر اساس شرایط اعلام‌شده، دارندگان مدرک کارشناسی با حداکثر ۲۸ سال سن و دارندگان مدرک کارشناسی ارشد با حداکثر ۳۰ سال سن (مدت خدمت سربازی آقایان به سقف سنی اضافه می شود) و همچنین داوطلبان صرفا دارای سابقه بانکی با حداکثر ۴۰ سال سن، مجاز به شرکت در این آزمون هستند.
🔹
متقاضیان برای اطلاع از شرایط ثبت‌نام و جزئیات آزمون می‌توانند از روز سه‌شنبه ۹ تیرماه به پایگاه اینترنتی مرکز سنجش دانشگاه آزاد اسلامی به نشانی:
https://azmoon.org
مراجعه کنند. همچنین این آزمون استخدامی در تاریخ 9 مردادماه برگزار خواهد شد.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/664601" target="_blank">📅 17:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664599">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
پزشکیان: برخی جریان‌ها در مسیر منافع ملی سنگ‌اندازی می‌کنند
رئیس‌جمهور در دیدار با آیت‌الله علوی بروجردی:
🔹
هدف دولت در مذاکرات و دیپلماسی حفظ منافع ملی و بهبود زندگی مردم است و برخی جریان‌ها با سنگ‌اندازی در مسیرهای سازنده به‌دنبال اخلال هستند.
🔹
آیت‌الله بروجردی نیز با تقدیر از مسئولیت‌پذیری رئیس‌جمهور در مذاکرات تأکید کرد نباید فرصت‌های دیپلماتیک از دست برود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/664599" target="_blank">📅 17:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664598">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59d49d0083.mp4?token=cP2VE3JPvr4PKNC13kUK2iPqkhd8m3x46G3AlBueTsF2-o6Uj5lKOZ7KMkAm394yD4PZXOfAaEtdArB14zOD_EbjeB1kHEA6SSHBzEhbL2SMSoes4cmbNc8REyxlSliHx04quKfFw0nQH40kfjBUFxKh_DTKbLHQH0CIH-eTvv2S_k8UAW_NIim7YNRpGK11vjR3WohNSDfCb6_wFLklJ5Ucudsj1wfZxF6WzNNzq7w0M-wj90vUFQGPDzZzPsr3KMiH02HXgkdq1pcwq-H9QscR9QyW2LEPIT_ktLoR0HJB02yCx4yCN3Te0LPJwGkuc2GWQwpILhyrfXFJZY9AVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59d49d0083.mp4?token=cP2VE3JPvr4PKNC13kUK2iPqkhd8m3x46G3AlBueTsF2-o6Uj5lKOZ7KMkAm394yD4PZXOfAaEtdArB14zOD_EbjeB1kHEA6SSHBzEhbL2SMSoes4cmbNc8REyxlSliHx04quKfFw0nQH40kfjBUFxKh_DTKbLHQH0CIH-eTvv2S_k8UAW_NIim7YNRpGK11vjR3WohNSDfCb6_wFLklJ5Ucudsj1wfZxF6WzNNzq7w0M-wj90vUFQGPDzZzPsr3KMiH02HXgkdq1pcwq-H9QscR9QyW2LEPIT_ktLoR0HJB02yCx4yCN3Te0LPJwGkuc2GWQwpILhyrfXFJZY9AVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از گردباد عجیب در طبس
#اخبار_خراسان_جنوبی
در فضای مجازی
👇
@akhbarkhorasanjonubi</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/664598" target="_blank">📅 17:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664597">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
اظهارنظر وزیر خارجه عمان درباره دریانوردی در تنگه هرمز
وزیر امور خارجه عمان:
🔹
سلطنت عمان از اعمال عوارض بر کشتی‌های مطابق با قوانین بین‌المللی، حمایت نمی‌کند؛ اما احتمالا درباره سازوکارهای مربوط به خدمات دریایی، مانند افزایش ایمنی ناوبری و مقابله با آلودگی بحثهایی صورت خواهد گرفت.
🔹
سلطنت عمان مشتاق است که دریانوردی در تنگه هرمز برای همه ایمن و آزاد باقی بماند و طبق یادداشت تفاهم، تضمین خالی بودن تنگه از هرگونه خطر مین، بر عهده ایران است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/664597" target="_blank">📅 17:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664596">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
انهدام مهمات عمل‌نکردهٔ دشمن در بندرعباس
سپاه هرمزگان:
🔹
از فردا به‌مدت ۲ روز در حومهٔ بندرعباس عملیات انهدام مهمات جنگ رمضان انجام می‌شود؛ احتمال شنیدن صدای انفجار ناشی از این عملیات وجود دارد.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/664596" target="_blank">📅 16:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664595">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
نخست‌وزیر عراق به ایران سفر می‌کند
🔹
علی الزیدی، نخست‌وزیر عراق اعلام کرد که پس از سفر به آمریکا، در چارچوب تحرکات دیپلماتیک منطقه‌ای، به ترکیه، جمهوری اسلامی ایران و عربستان سعودی سفر خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/664595" target="_blank">📅 16:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664592">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F6Jzw04QA9zu4e9n23M90WYH5qIzD7MbFdZLxkzfcBHTK3I9PwDRv_R6z_VenEPpfOtxzUDOmStviMaiWIt6Htkj41SopojUCyKZCXw9sWcI5BZu8B7YZ_FzzXICdFGz0hY6tF3ewVmfr39Q62KMsWpxCo0y5NpyM6ArDJ2TeE3phivwPY568iJ5MvZ2zbyBxOV_d7DDFQCfNjZae4ge8Z2RF8KUMr8HxNtfxKHhuEUx2XmQhYJeQCicET_PQSrjCbz9gR-smss6tgjYj4JW0JvXMxKjprC_ctA-ew599fJ1KreQiVmI7DF9RI99RNzZTI7v3WK6Fqm5z31kqvhnXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TUATcCCW66lbop-eiPEWZ9Kln7Xp15JXqD-T2RPqoC2_k1eon3xISWIb8_5N5LMfITH-6l05jwl81G4VVbC4h7crP6oyItOAel4bnN9B_Iw8jTDeGv45Eya20GxMdiy2PnEa7crELHB0e9xFdQ2DvjvePvVelJB61urQxlBskWs5R4PQt_F-yswa9y5ApY4PkgYCB0aJN3RLxEZkk62km04hYnQoAe_08TjHzI_KLJ3NCkOIrhgbXWlxriympsamygasesBvOc7C6clZAv1Yd5XFddVuhJdd3rTI0NeznbP4zVeLqA-Ma6mfATVLwXUyiFdoka2Q9oCs_nVnUripdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oAIF7vNStojVdFxaZjWIRAsjMstd1Xx-ZwtM3t-chdXzsRxopToXCGmcnYQN6Nx4C_Vaqq4quEvcqBWyRjTHrrIccLKRjDr7mx2mj8IgW8sokznCXZKRcilEzOP4aqy5moYy5aP4u62O0M-8lJczXlyF9jgFoVjuI6QsqC5sQ4VwRuB4eYrGHLP6Wk3tPYxhcU_t-pDNVRiFUNF8D51HnuH02sYZyYFl3IIGFv4ZXV35x_dkHIX_CJ92A5GM5KpaQ7yyKzA807e7fgUby4HTkhgGnkuV863FmPfAyolfbQtnISye4ukflByL3_WJB138oM13mZknWVXK98vFLM3Bgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ظهور «ماه توت‌فرنگی» سرخ در آسمان شامگاه امشب
🔹
ماه کامل ژوئن (ماه توت‌فرنگی) امشب با رنگ سرخ و صورتی در نزدیکی افق طلوع می‌کند؛ این پدیده کم‌ارتفاع که هر ۱۸ سال به اوج خود می‌رسد، حدود ۲۰ تا ۳۰ دقیقه در این رنگ باقی خواهد ماند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/664592" target="_blank">📅 16:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664591">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
برگزاری نخستین نشست کمیته مشترک عمان و ایران درباره تنگه هرمز
وزارت خارجه عمان:
🔹
کمیته مشترک عمانی ـ ایرانی نخستین نشست خود درباره تنگه هرمز را در مسقط برگزار کرد.
🔹
دو طرف دیدگاه‌ها درباره مدیریت آینده تنگه را بررسی و راه‌های تقویت هماهنگی در موضوعات مرتبط با تنگه هرمز را مطرح کردند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/664591" target="_blank">📅 16:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664590">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نقدعلی: در صورت بازگشایی مجلس؛ استیضاح وزیر نیرو در دستور کار است
محمدتقی نقدعلی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
قبل از دفاع مقدس، وزیر نیرو به دلیل مدیریت منابع آبی مورد نقد جدی بود و استیضاح او در دستور کار بود.
🔹
مجلس بدون دلیل امروز بسته شده است، لذا اگر مجلس باز شود، استیضاح برخی وزیران از جمله وزیر نیرو در دستور کار است.
@TV_Fori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/664590" target="_blank">📅 16:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664589">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDGf2XhjLyP-ib4fRbvnSnZSocIO59nOD6UDUkNxiyFO4H_SOEpBWPUFEaLA4WZkypOi6iaa0SwxhLo1UnOUi-Z8BTdj5HfbaAKsD_QCrG2bd901LasSwepRIvchAcu9xZTDs1TM0hmznKDu5PnEDqNQD-fYcI1AMU7xOx7plgaaBA96zWcL5oty8cn38bUh0mFixIJbq4jLK414w8Ovy29uQ_1UbsHVjsPAIeg12KQkx-Kmu4691WCNZkgG0nkmuqaR6MZQeAinzRQmBMUls76XDF5F64Ze3Si3PLDAbumiiCV5ncwg-zw-fPSK7yeZq_eE-yO-AETRzSqsiy0N9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فشار ترامپ بر سوریه برای مقابله با حزب‌الله | پیام محرمانه دمشق به لبنان | دلیل پنهان فشار آمریکا چیست؟
🔹
در حالی که دونالد ترامپ، رئیس‌جمهور آمریکا، خواستار ایفای نقش مستقیم سوریه برای مقابله با حزب‌الله لبنان شده است، مقام‌های دمشق تلاش می‌کنند به دولت…</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/664589" target="_blank">📅 16:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664588">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9487e29f6.mp4?token=PYRVT3ad3kIGTjaqTPe62jcQ1Zt7WgeGY5kfr8m5oPEUOzu7H2V4MK4wxmAbTraMCJ-mwjXAZXzWBF3vW6tu_nkkYajS4vKJL9ZPa_ANA_d94mfjve2ncs471sFJJO2VCVNVtB8SRixI1uSpAbYPq2C6EScGpRy1hDdKrQjkiQn2kl1IuBWwEzCrh4dMqEoA1lJGJLLw0JTf1LaRpemhpW2iSS7SpxH4YYBj3NCP30_RLnKcbEUjoCJai3ZRcRxKs-FBdQfo8OWFYSoce515SpOVBAh5filGENlIyHrFX6mhYERujhYIShzjwFR9UrzGrQkjcDpzxRIQb464E-Rqrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9487e29f6.mp4?token=PYRVT3ad3kIGTjaqTPe62jcQ1Zt7WgeGY5kfr8m5oPEUOzu7H2V4MK4wxmAbTraMCJ-mwjXAZXzWBF3vW6tu_nkkYajS4vKJL9ZPa_ANA_d94mfjve2ncs471sFJJO2VCVNVtB8SRixI1uSpAbYPq2C6EScGpRy1hDdKrQjkiQn2kl1IuBWwEzCrh4dMqEoA1lJGJLLw0JTf1LaRpemhpW2iSS7SpxH4YYBj3NCP30_RLnKcbEUjoCJai3ZRcRxKs-FBdQfo8OWFYSoce515SpOVBAh5filGENlIyHrFX6mhYERujhYIShzjwFR9UrzGrQkjcDpzxRIQb464E-Rqrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این کلیپ میتونه نقشه‌ راه برای زندگیتون باشه، اول تو حرکت کن، بعد معجزه را ببین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/664588" target="_blank">📅 16:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664587">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esA9x42CIjtq6i_lND07QIYokRFu6DpvmTqDSztOhKTSLL1-H7R2mkPwy6dKljVv_8t8jZaruMywnfrJkwGcfZRXKyJWrkV-nUs1Lm8O_KoCbSa_tnCzLUSHJgWW7PJEnAauqmxd3iQLSLhRreLoVbChL3HzlRzoTLc_s8VCh0IoKp2ngjTOrkTfGAmwtcZ1bCSQ6XOTiYi4i_bIxvt3ts1iYJg1J9J-drUw7PCgCMHJAToi1B5p90eeKcvNfeKHV8Y0A1IhI7nI9LJ1waSLchG2pM4HfmOrMUiyttTsuuJdTGuZsLMyoOLVXv-TykAydMsKW5w6md9vj9r8Cd2MlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمار تکان‌دهنده مصرف پلاستیک؛ سهم تو چقدر است؟
🔹
هر نفر، هر سال، صدها پلاستیک؛ اما تغییر فقط با یک انتخاب آغاز می‌شود  شماهم به این پویش بپیوندید
👇
#نه_به_پلاستیک @Ertebat_baforii</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/664587" target="_blank">📅 16:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664586">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/He9DFHYy8NaIRiZxDkgOqLzQVPbkaYMOKCI09K8U_HYgPI-LfupHggZaTKrFfUkEfjQQyP1Dh17o5sbwZ_dSsWVy4UhjUZzWBTUq84z7s3HMwOYL2-ZUJJFNmRBJr5uAdUr6UvR-NY8gFRGPAotMmWnV6VwjeU0BuECh0MhIb2Y80x2c1SUwFG_p2HHyTdO6FzHktqo9wUkrcUFXiTAUFARTfWn1yEdJ4TOrBOOl9DypFsjq7XyHpjmtsojSTCK2kzdvodeHzePRmqLbF22KZrxuvZ-82bqZ9IpD6JfgFlyQwk-cpSR5jrLmR69zI2Vgwh3BaFhIYg31H9RUKfNSFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سه تکنیک ساده برای تقویت هوش مالی #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/664586" target="_blank">📅 16:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664585">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9729d15bc6.mp4?token=ZZHO2eLKWZ-UoM6rVtyVidgcp53YYtCEX5-teA37MsqEygQz7buSi6eN0PeaMfh30uDWYud2z9B1jDSNbO_obCrKEaG-G-aIPZhjbYSKReCH8cEVlgfQ0M3kjvQx8-ycgI15SC41JQHkGatN9NNgvuXQcch_60OE-iTqaLYfYUZ_6BoqRemGQaTBNFIAKkLYxUrGeDE3obIH6zqzwrDobmCP9Y97S0j0TqJttbkVeUA-accDJTDAyTFvCrkSd136h6WD-uc4Y81UGBhC--8oBLWN4_EzlmQluzguszlofvo4EnmH6YYAk66if9lHFgy09ZOZ2MgGF3wV7SMotnNdDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9729d15bc6.mp4?token=ZZHO2eLKWZ-UoM6rVtyVidgcp53YYtCEX5-teA37MsqEygQz7buSi6eN0PeaMfh30uDWYud2z9B1jDSNbO_obCrKEaG-G-aIPZhjbYSKReCH8cEVlgfQ0M3kjvQx8-ycgI15SC41JQHkGatN9NNgvuXQcch_60OE-iTqaLYfYUZ_6BoqRemGQaTBNFIAKkLYxUrGeDE3obIH6zqzwrDobmCP9Y97S0j0TqJttbkVeUA-accDJTDAyTFvCrkSd136h6WD-uc4Y81UGBhC--8oBLWN4_EzlmQluzguszlofvo4EnmH6YYAk66if9lHFgy09ZOZ2MgGF3wV7SMotnNdDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایندهٔ سابق کنگره: آمریکا در جنگ پیروز نشد و ایران کنترل تنگهٔ هرمز را در دست دارد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/664585" target="_blank">📅 16:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664584">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
ادعای کاخ سفید: به تعهدات خود در آتش‌بس پایبند است
🔹
در پی حملات به کشتی‌های تجاری، آمریکا پاسخ داده و تأکید کرده است خشونت با خشونت پاسخ داده خواهد شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/664584" target="_blank">📅 16:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664583">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/005f8a8af5.mp4?token=pi8a1NiESFz1PKyySj8ZTmuoAJC-BUOS-aUFniQ2avoEgvAcxDuwqbHZM1gBgMU1VkS1JHBofR0wyxg3PjxluK7vzdgbQj5eBZgHiQTqTfy_rPRjACirhu-EEXn1yJBjb5VO7taGMwy5RZutGNs4wvyqhuylxJ2lFisuGpM9a_IhydOrb8GpyF9yMB-P0UvFg1GN-r0AEjKizxSi_2DbK4UM-VxtiYLT1lWf8DTXAZt8LX9LAmFdHBW6VbuaQ1MOTo_giWc_Fbd5NzUYy2oVRL9J4YzSimB_YblKh_fGSxeDbcCxH8iG39pOS4NoKAqYRqL_OnahaUXp9CJCjDWnzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/005f8a8af5.mp4?token=pi8a1NiESFz1PKyySj8ZTmuoAJC-BUOS-aUFniQ2avoEgvAcxDuwqbHZM1gBgMU1VkS1JHBofR0wyxg3PjxluK7vzdgbQj5eBZgHiQTqTfy_rPRjACirhu-EEXn1yJBjb5VO7taGMwy5RZutGNs4wvyqhuylxJ2lFisuGpM9a_IhydOrb8GpyF9yMB-P0UvFg1GN-r0AEjKizxSi_2DbK4UM-VxtiYLT1lWf8DTXAZt8LX9LAmFdHBW6VbuaQ1MOTo_giWc_Fbd5NzUYy2oVRL9J4YzSimB_YblKh_fGSxeDbcCxH8iG39pOS4NoKAqYRqL_OnahaUXp9CJCjDWnzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای کاخ سفید: به تعهدات خود در آتش‌بس پایبند است
🔹
در پی حملات به کشتی‌های تجاری، آمریکا پاسخ داده و تأکید کرده است خشونت با خشونت پاسخ داده خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/664583" target="_blank">📅 15:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664582">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
رویترز: توافق برای آزادسازی ۶ میلیارد دلار از دارایی‌های ایران نزدیک است
رویترز به نقل از منابع آگاه:
🔹
تیم‌های فنی ایران و آمریکا برای بررسی اجرای تفاهم‌نامه اسلام‌آباد به‌زودی در دوحه دیدار می‌کنند.
🔹
به گفته یک منبع ارشد ایرانی، این نشست با محور مدیریت تنگه هرمز و کاهش تنش‌ها برگزار می‌شود و دوحه و تهران در مراحل پایانی توافق بر سر جزئیات آزادسازی نخستین ۶ میلیارد دلار از دارایی‌های مسدودشده ایران هستند که در دو مرحله آزاد خواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/664582" target="_blank">📅 15:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664581">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
فروش آزاد داروهای غیرمجاز و اعتیاد‌آور در عطاری‌ها و سوپرمارکت‌ها!
محمود طاهری، عضو کمیسیون بهداشت و درمان مجلس در
#گفتگو
با خبرفوری:
🔹
متأسفانه حتی یک‌سوم نظارتی که روی داروخانه‌ها وجود دارد، روی عطاری‌ها نیست و برخی عطاری‌ها داروهای ترکیبی غیرمجاز تهیه می‌کنند و به دلیل عدم نظارت، مشتری‌های خاص خود را دارند.
🔹
نه تنها عطاری‌ها بلکه در بعضی سوپرمارکت‌ها نیز، اقلامی به عنوان شربت‌های تقویتی غیرمجاز دیده می‌شود که فروش آن‌ها در داروخانه مجاز نیست.
🔹
برخی از این داروهای غیرمجاز به کلیه‌ها آسیب می‌زنند و بعضی از آن‌ها وابستگی ایجاد می‌کنند و مصرف‌کننده راغب می‌شود دوباره از آن‌ها استفاده کند و تنها اطلاع‌رسانی کافی نیست. مشکل اصلی، ضعف نظارت و نبود برخورد قانونی مؤثر است.
@TV_Fori</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/664581" target="_blank">📅 15:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664580">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOW5biuwyOlFKFvpLVhWyPn4e0sxA2-rsvNuK9VOWfSYnipPgFp_Uxc2Y5dBPk-Nu4F_-j-pjB_yGim5x5U_v4hGWE2pPuBlHDWvHDQQ-QYMUPnh2asIloF_R59D80OiH267SpNTJR9VEYsyEP9o6b5tRkPK-yRrW_-HtmHp6h3BxEVcdZwoQVu5Ducmo9fzgbdlYauGkBCcEnCuigQ0GFMffJsknkcp-jusDMgQ8uLv7rgKCIlo8tcO8vWFZtP_WUfmEjZziHx10aBXbHACJ7vD-fNKRzzTBq1c5Yus4ej-cpmvivlTsbTfslV5DjSYmmUJMQwM4KpR7vjkcWHKPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار درختی مرحله حذفی جام جهانی ۲۰۲۶ در پایان اولین دیدار یک‌شانزدهم نهایی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/664580" target="_blank">📅 15:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664579">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fdf4ba5ee.mp4?token=kZq3yazbJxejXZbFTcyedwHskryFWZEXL4o85CAJzgV5_yh5WJB1AWY67LQLM8jtZQaEioaY0_GR4_4WbjY4GlGKLSDq9llUr_iA4IzNsHXMW6TU7ZtDeSE_8vZDj4IUYdVda2Wlh4MEF0gqlrhVZo5qPjIRq-4R_mamPoGkq92VvU5ar-Co806in8CGE9qXXLa6WBnF02PrVaY2Q-OYHqyyYzVv00hWBfO-jH9p9iL_vDK5pgT3cUZUvh7PIHAfFYVEWAumU9FfXfPxVGfdYI2eGt-5Jwc0djQTGgw0T9PCOhJmM_X1UEE1OluFe_DxDinGTmeUIg6lS6EsVdYhbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fdf4ba5ee.mp4?token=kZq3yazbJxejXZbFTcyedwHskryFWZEXL4o85CAJzgV5_yh5WJB1AWY67LQLM8jtZQaEioaY0_GR4_4WbjY4GlGKLSDq9llUr_iA4IzNsHXMW6TU7ZtDeSE_8vZDj4IUYdVda2Wlh4MEF0gqlrhVZo5qPjIRq-4R_mamPoGkq92VvU5ar-Co806in8CGE9qXXLa6WBnF02PrVaY2Q-OYHqyyYzVv00hWBfO-jH9p9iL_vDK5pgT3cUZUvh7PIHAfFYVEWAumU9FfXfPxVGfdYI2eGt-5Jwc0djQTGgw0T9PCOhJmM_X1UEE1OluFe_DxDinGTmeUIg6lS6EsVdYhbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هشدار نیروی دریایی سپاه به شناورها در تنگه هرمز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/664579" target="_blank">📅 15:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664578">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LebrewVJ-5zYcbdWmL8ye_AN3mByAckQJi0tWeyuD9hnHDpQBEzPEy8TEch2dc64hH8Z4MNHPqVQLtU655kaDZ-LMFCKlE6I0duPrcZ7PbpjIKTadn2evq2b851t9nTi6e-JykkzbDP4Qsi_h_dc_F3L-QfrDTSRyyHux1rKuRopr6Hrq8RFCJE8sDQa5jCO_Tk_zCeWEPx6LEHXnFcOwwXu7zI277B1R7y1-aSav8HJfg3kFuJ6riMgjWc9OPngAT-VX8zUiVDpPZ0KYaTKL5gcABmp_hJlqKloC1PljwfEG8PkpCY0EsAfHroRb049ThpKI69xQhaObIZ1M9ZojA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هیئت منصفه دادگاه مطبوعات زیباکلام را مجرم شناخت
🔹
هیئت منصفه دادگاه مطبوعات صادق زیباکلام را در پرونده اتهام نشر مطالب خلاف واقع و اکاذیب، بر اساس اعلام جرم دادستان عمومی و انقلاب تهران، مجرم شناخت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/664578" target="_blank">📅 15:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664576">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pi0Pp9DmjeQ5OIpJHodZHodfR3x7z91Lv1kgGPrOPxQFRPdtsTR6AzkGQjS5Npr6lDP3_t-_EBoOmhVYX5tuv7eBUj5Zie303Bn1F3biO2RRB8HHkALCCo3sRot4H-ZCbcDHoIEhJ7-LiuJUQoCIjLYsnewNbrkfa7umkVuO3r2BudJmse0oM2ygJAkT9JDcXahUhmxJRMaIgeRBHr4-DNiloTOdwBaduPJNfIyR34g0Yvn0B9kmNhhRb23Uqnsf642tOdsBzlU0cbQcN_cTLp-BQqf7rRxfGcVL1Arid7DISM5ZUmnePZEsvCT6UCnZInOshX5xxLY_dssNvD9AMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
جهش ۱۲۲ درصدی پرداخت تسهیلات ازدواج و فرزندآوری بانک کشاورزی در خردادماه
🔻
تسهیلات قرض‌الحسنهٔ ازدواج و فرزندآوری پرداخت‌شده توسط بانک کشاورزی، طی خردادماه سال جاری نسبت به پایان اردیبهشت، با جهش ۱۲۲ درصدی در مبلغ و رشد ۱۲۷ درصدی در تعداد همراه بود.
🔻
شعب این بانک در سراسر کشور با هدف تسهیل شرایط ازدواج، تحکیم بنیان خانواده و جوانی جمعیت، تا پایان خردادماه سال جاری در مجموع ۲۰ هزار و ۲۹۵ میلیارد ریال تسهیلات قرض‌الحسنهٔ ازدواج و فرزندآوری به ۸ هزار و ۱۲۳ نفر از متقاضیان واجد شرایط پرداخت کرده‌اند. این آمار در پایان اردیبهشت‌ماه سال جاری معادل پرداخت ۹ هزار و ۱۲۷ میلیارد ریال به ۳ هزار و ۵۷۹ نفر بود.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/664576" target="_blank">📅 15:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664575">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ryxR3r9Ie6hV1iyorD9W07zTZktSQngWPOiojtpd2Ngbr_j_RIXTCqmiZEDZ3kjBJQUB-QCe75NFzCX0Jl7j-DrncIdMmGOFWO__j0gxQcUAbf-mtjpT2DEvkO7NH6RM4NzDty2ve7r128deBn-lTxw5KqprfvNSaEUQ4yNL922yzNGsKhonb3-O8ebByDDBCMS1b6a-HV5pSewhaXnqpkyRr-WT_1rHF5Ndm1AhbxTQnxnwZw6XnvCGR_M9pKZanAJR1iWZIDA7DNw8B6FCfHZx2Dmy0tYUQJmpfBIhJ3C3WfLddqb65OvEi8d8IWFXWaqkWEjPiVoODGR1vB_aFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افشاگری کاربران از رنگ‌های احتمالی آیفون ۱۸
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/664575" target="_blank">📅 15:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664574">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ناکامی وزارت نیرو در انتقال آب ارس به تبریز
علیرضا نوین، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
مشکل کمبود انرژی مربوط به امسال نیست و سابقه چندین ساله دارد و باید نیروگاه‌‌های اتمی هسته‌ای افزایش می‌یافت ولی متاسفانه نشد.
🔹
وزارت نیرو در انتقال آب ارس به تبریز ناکام مانده و علی‌رغم تعهدات و وعده‌ها می‌گویند باید اعتبار را برنامه و بودجه بدهد. اعتراض ما در بحث مازوت‌سوزی نیروگاه تبریز به جایی نرسید و هیچ اقدامی انجام نشد.
🔹
در روز رای اعتماد به وزیر فعلی نیرو باید تعهدات و برنامه‌های راهبردی را جدی‌تر می‌گرفتیم ولی این کار انجام نشد و علی‌رغم تلاش‌های وزیر نیرو هنوز نواقص همچنان باقی است.
@TV_Fori</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/664574" target="_blank">📅 15:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664570">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f6tFUdS4KttaieK6MbFwNJoEPOzNzXUmOmIAshsAKeEOXWuTPfBND28qReZKg3ub6GNQo2N29AfKO6GDNN5_7VziicO96Eoct5tJ_ntTkE92MQW1CjIzkspoEBC_CCj-PsXgOWrASKKR2RbEkD958InFI-rONTIcVqFRFYht_SNrO8UKTc4IL4peXYsKMFzPMyUs2A7n-vQolRivq-VZICasoKffPUWAiZBjrPdxbWHAB-Bre5_D8rqKrD77SoHFiI7I1iIDjskGZuKPULOt1Zr2CwN85F5K2wYSkiRhMSzvX4SC_FnWunK6n5nS6I7HFqubNiQPHyc_550TQhNIVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f_xECjPmmUzaJJkDbGIEegQ8nQ9CL9WPoruluHt3n-IfdSRM1MrHqdUWinF1mf0Xq_F3cWDt3zvJzxEdxLgFyWZ21iIByip8aoTcNLDjdBrGmbSBRaKF02w0YPxYue58p6j7u2Z-pgg4gPOIsnkzKjuYkfH_b8GQC6Vdr7u1_ItqXR_8Mv_g1ypXmkDO5h_XqvGrb0bs4hSDftpRhyp4kwfv8fQHtbaIJw2eue41rlqeJo-6mN9pWHGLGwDZmRxNlPXIm0SFTQENIf9noOnJrVMAstDnMwVKK8jrn-fZ0aQxPMXZP_VRjs9UIbDte80ybdn2f7R_hZBX112984V-gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nsCeFnohopRP8X2uvVKB7TOUNzEVsKl1HnjtO_7muSKN76sOcjduK4lcwE76l5plTp3_hJlPmY2xxEcpQ0YaSEDOuDc0jYUuILWXxOcxIDBg3OafqPqzHdguuNzWbc-8YuLDrqvgfb8oZg6DKWEH8byI1xko8S8jAkbED34gu1FhPvcKi4bWKkW67SZyocUTAoSR-z4SK1Se6gGmIJW9G96Tssg4eH8--ZGPOM3PnbMpxA6LQDwJgd59Jx0A_etQJ0E03MjWDNKZFuHYyPzqGte_x1RxhZe1fgYm8MTI_oba1gTS7g_Dq-szE3wdkHQ06yCbHM7uuoeZ5Tnt0DbDfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eudTthtShdUDFuYsrcMnk3VgHMXcfjzPIPIwJI1OYGSHaGIOTr07R3slPftrkEvpdOizeena5Tu3HY3lapK98yHtUKFYlcdm6u-DUF9ciJs32OA4CxgiuQMMohmQkckY8JHsWU19JELl-8C_7blxTEgKFoTduPWuXY6VArEHdxcHc-hd0tf4iO2gaRo_FPM1AfirBRfpd5-b8cQEYJcIbf5bp4fzD0x245bYIUx4aeINCp2vTkeH4HxyG6jztD0kNPG16oFwDimuhABu-ADatMDbuTwImbJtBx4Y8BjV9Muxll1P77SCx1elTAOkxRR9Ywobp1u5GkEChnZyrH74HQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فرماندهی جنوبی آمریکا: تفنگداران دریایی این کشور برای پشتیبانی از عملیات امداد و نجات زلزله‌زدگان در ونزوئلا مستقر شده‌اند
🔹
جان انسان‌ها را نجات می‌دهند
البته بیشتر وقت ها می‌گیرند...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/664570" target="_blank">📅 15:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664569">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GL6k9yw4lOG8zsch5AUfOw8prixEilaty-UCE_HpFBBlf-u2gKdlrhPhqD2ejkp1AljbnKCv8z3h5Cb0Jn191divXBfBXw6mEIHJiHC_zDaPNOHhQg_ub1EeqHhbWdXH1XPiDYDmfmUSQdXh3h8yys7ocrKlYLiDG3mCINGlKBMY88np9jhScaSlH3IEDxfBgDmLQdkeEziOLpCIKiIFogCMDSQD4UxbDxMO6mk-J6Ae5YcNpXTD2zs1o2Xe0z8uK9oIb1VRqVpnJeGYtGOC-4ApTFNeQ0QIFXhvf6fl5TF8YRMWpb7BmqOcYjKhXZ_oTcBbYfh63MHBl_599HKQ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ: دیدار ایران و آمریکا فردا در دوحه برگزار خواهد شد
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/664569" target="_blank">📅 15:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664568">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/333a29ab62.mp4?token=VJ_QZRjf1dWOEvqPoY0Od4HjrPID2zDdf3CSuxX4_DzMAK6wwX11kxQpNik2wb9ydL0KzddiulK0URax1yIMOsJHt4UOPM58hMR9fCFqf2xRvtlxETB1sEukeDiNOxh2RG7G3XOguT1mnd3d4NCoaWPaEOp45OhEiJJGkMwhG09mJl45Q9kbZlAIusxzia7VLtgQL6lOW4Uno9K32343ESf7VDfg1SwYJObAivkaOf5fOw0Tb9mIMeD0HgLhXdWXOY6EueMFl2ZoMlNAw3fo0GSAR1uRktcSm_94f1vvbdZgpaehe3Jqg5gfeeOvulqUNJ750APx3lSd4jp4rrdu5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/333a29ab62.mp4?token=VJ_QZRjf1dWOEvqPoY0Od4HjrPID2zDdf3CSuxX4_DzMAK6wwX11kxQpNik2wb9ydL0KzddiulK0URax1yIMOsJHt4UOPM58hMR9fCFqf2xRvtlxETB1sEukeDiNOxh2RG7G3XOguT1mnd3d4NCoaWPaEOp45OhEiJJGkMwhG09mJl45Q9kbZlAIusxzia7VLtgQL6lOW4Uno9K32343ESf7VDfg1SwYJObAivkaOf5fOw0Tb9mIMeD0HgLhXdWXOY6EueMFl2ZoMlNAw3fo0GSAR1uRktcSm_94f1vvbdZgpaehe3Jqg5gfeeOvulqUNJ750APx3lSd4jp4rrdu5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرتاب بالن‌های حرارتی توسط جنگنده‌های اسرائیل در جنوب لبنان
🔹
جنگنده‌های اسرائیلی با پرواز در ارتفاع پایین بر فراز جنوب لبنان، بالن‌های حرارتی با هدف ایجاد آتش‌سوزی و تخریب پرتاب کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/664568" target="_blank">📅 15:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664567">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
مکرون باز دوباره با عینک دودی در رسانه‌ها ظاهر شد
🔹
برخی کاربران معتقدند که مکرون باز دوباره مورد خشونت خانگی قرار گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/664567" target="_blank">📅 14:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664566">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6ZyIzHDMO2rD-dKVtwxLg2kjFNGFAeaTlfDiM0zET9za7RQVeHmUK2UB7wCWsneW68qZisH_7sqGD2aG5mf1UGIqer5uNuUhJaFOx2bQcyT53H_--iwFKIwALCe5OcFvQ8NYpaRBupJaspjFDbNUQIBTbMt1RYv1HwCvfefK2KuMSYJWAnF06A9MAEP3uEGnJxopRtsKlwhpZT5LdiubbKE0JQDcUjFwZZahD7cFavJThm46cqtUCiAlzOm-uK4Yb9LM9dvToAK59-gParNCyyoNtC2AljjCZZwwnzK7tmgccsQoA7LV4g1udcM-g-ygA_qGBCfOzyJY5S2O2SqDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا نتانیاهو در اتاق جرد کوشنر می‌خوابید؟ | ماجرای اتاق خوابی که خبرساز شد
🔹
در سال‌های اخیر، بارها در شبکه‌های اجتماعی و یادداشت‌های سیاسی ادعا شده است که بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در سفرهایش به آمریکا در خانه خانواده جرد کوشنر اقامت می‌کرد و حتی در اتاق خواب دوران کودکی او می‌خوابید.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3226332</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/664566" target="_blank">📅 14:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664564">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
فعالیت برخی شعب بانک‌ها در روزهای ۱۳ تا ۱۵ تیر
استاندار تهران:
🔹
تعدادی از شعب بانک‌ها در روزهای ۱۳، ۱۴ و ۱۵ تیر فعال خواهند بود و مراکز درمانی، انتظامی و خدمات ضروری نیز به فعالیت خود ادامه می‌دهند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/664564" target="_blank">📅 14:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664563">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1b6ad5aeb.mp4?token=JRLp9TixwJ0G6tcn4bUdH79CCmBYblno7twDHHypY_2YGJ5YvMW189pWapfGccNeOJn_A3ZwEuOvRz0kMs6iO5U6uJiOgL-P7Bn2YER_6V7IB4teqEl3MBmNEA_ajcrGQDoIo69a-4HgLDcx1DS5MZhFm-AC0mNuM0jIopdjx0zpQh4KPRUJRuGFQ6drVYR5JSq9_X5LLVlR2InGF3sE7gv5ikfNMEyrNF8bPy2D0VNzILgj_SJ5XrPuo6vTgRMzSD_9Ux75vTmwOWuPFEIP-RaX808gPLE6X7t12lmFHt_1tkM93j4HWCIQN629AepKKW4xBGAfHGmuRn8USSM-pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1b6ad5aeb.mp4?token=JRLp9TixwJ0G6tcn4bUdH79CCmBYblno7twDHHypY_2YGJ5YvMW189pWapfGccNeOJn_A3ZwEuOvRz0kMs6iO5U6uJiOgL-P7Bn2YER_6V7IB4teqEl3MBmNEA_ajcrGQDoIo69a-4HgLDcx1DS5MZhFm-AC0mNuM0jIopdjx0zpQh4KPRUJRuGFQ6drVYR5JSq9_X5LLVlR2InGF3sE7gv5ikfNMEyrNF8bPy2D0VNzILgj_SJ5XrPuo6vTgRMzSD_9Ux75vTmwOWuPFEIP-RaX808gPLE6X7t12lmFHt_1tkM93j4HWCIQN629AepKKW4xBGAfHGmuRn8USSM-pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنجال پس از گل سوم الجزایر به اتریش
🔹
در کلیپی وایرال‌شده، پس از گل سوم الجزایر، بازیکنان اتریش معترض شدند که چرا طبق توافق پیش نرفته‌اند؛ بازیکن الجزایر هم با اشاره دست، آن‌ها را آرام کرد و نشان داد بازی مساوی می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/664563" target="_blank">📅 14:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664562">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnyT4hNAQ3CDIBFxcg0EqIsp9fLMiczXUkAdlHMGddDFsA96hEIKxTh_Vaiou0J5E01JBX36177QUOzOmnENnWRseZOJanxiIFx6x3KP_nVKryB-p2AMuA0msNAJTFG3CMSKsUUBxt4G0IVVq3frjGLvj3bebCJ7YxNl11S5pRB1smU3M03tGrC_7VybwgR3hot7j0TmS6PURetHmb2rrCuGlMewPIWGg29HVWIdKgafFsegEi41xt1naLdS8A3m_OCy77W7phZ5_3Oygt6AkKNLpFFvoYHqYfIiP7BOYCX2mZQ6z307lBEo7GJDcjKk8qf5c5LEqX84LT-vEFN89w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ درباره انتخابات میان‌دوره‌ای: بالاترین آمار نظرسنجی‌ها تاکنون؛ حتی بالاتر از روز انتخابات، ۵ نوامبر؛ این در حالی است که ایران هرگز سلاح هسته‌ای نخواهد داشت!
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/664562" target="_blank">📅 14:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664561">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
تداوم اختلال بانکی و بلاتکلیفی مشتریان
🔹
با گذشت بیش از دو هفته از اختلال در خدمات بانک‌های صادرات، تجارت، ملی و توسعه صادرات، قطعی و ناپایداری سرویس‌ها ادامه دارد.
🔹
این وضعیت علاوه بر خسارت به کسب‌وکارها، به اعتماد عمومی آسیب زده و به نمادی از فاصله وعده‌های رسمی با تجربه مردم تبدیل شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/664561" target="_blank">📅 14:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664552">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K5uarq7sdeD2nlO6RUic_rp07WcLR7WLgeJ1-zlUQGzTOboKE068JaASva9WTF4fb9Q7ogwcTe9yYXABpGM5e0LYfVKWVyGrb5pM6EdvuxVKcIoqZvzFw_yuQYvyyp_7mBVC2Kn-w1ZMarzRsPFmlDNAI1fkDp7oehiCMA5hVwYSEptWZL84G3NYrSLhoXK0JUqTjqHE0F92gHmaWrhoPLecI677s9xHzmKnpv31ducfgFVHuoUwBtO8qoSs9Avg3hb8sQVwUZgdDev2f6e7miSqK5X_-gHAyeE9MQbBY9LlYuHSaISB9qtOpIVMRX6c9UYv3_vbSdKQ3hRIyGk8eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ecjKfIipRtaClNbqlzdGAT48sbFDrKrejFjhqODdee45ksz6UkrwT2fDtUIx8SoN3Bx3r30Iji-NwJh5vKg57_kItTbU4AFtudQT9Wj9vtICjYM50lTriCpWfKN9IzhPJhDirsnroaJCwwpr6I1Lt7dg48ejJb1LRWJ3nz0yubzWHfijJHWkvublPlOdf5bFibyo6-XKUA6Dr8KeN6t5JUwrZslREzfvTDukGI2UZ4omhmjtk5giFHHIpIZISBgyaFq8JYVZRG8l8QGUqRG3B4F-OoM87gVmYloQXkjzc3D3TP0bCnlvwjhKzn10XFmVqm3Km_JYqFYJ9KmqVxeDJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بارش ۵ متری برف در یکی از استان‌های ترکیه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/664552" target="_blank">📅 14:07 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664550">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
تیزر قسمت بیست‌وپنجم از فصل چهارم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای عبدالکریم حاجی‌زاده که در روز ولادت حضرت زهرا(ص) و بعد از دل شکستگی و بحث با مادر در اثر تصادف روح از بدنش جدا می‌شود و شاهد عذاب و سوختن انسان‌ها به دلیل گناهان مختلف آنها شده و با گذر کردن از آن بیابان به باغ پر از میوه قدم می‌گذارد و با چشیدن طعم به یادماندنی میوه‌های بهشتی بعد از بازگشت به دنیا میلی به خوردن میوه‌های دنیایی ندارد را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: عبدالکریم حاجی‌زاده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/664550" target="_blank">📅 14:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664548">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61ee6d61a4.mp4?token=eHJCFhpB5tPjCyIIiRrO3e4hJmDdgBuQrixzh5YyuEmoZFJy9Nf4XHP58ymdiDyhNOVjbCKgdxDjdlP1ZFw6BLUmxpqv99HQgXy6MUplGD6eL8P593ANk8oEm8PeSrz9iVC33RqJ3umycRRe8KvDQ2ZvUHACJ0VvzyWL6VkBe7dKzlfYi3l25pW82s9_1oYOTxsQe5oll4oOx1_q7qZfazBjezHouRmrPNjnXrya3SeyHBmvrsGkt_7oN9N7Wm9gkcN09q3EeYyeQr6g7yLBoE2A0b0n6tvMTQYjyFXeU_XwbeL0itgFGDdZsuWT-ilkKljlynIFGLR36tsQZ55TpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61ee6d61a4.mp4?token=eHJCFhpB5tPjCyIIiRrO3e4hJmDdgBuQrixzh5YyuEmoZFJy9Nf4XHP58ymdiDyhNOVjbCKgdxDjdlP1ZFw6BLUmxpqv99HQgXy6MUplGD6eL8P593ANk8oEm8PeSrz9iVC33RqJ3umycRRe8KvDQ2ZvUHACJ0VvzyWL6VkBe7dKzlfYi3l25pW82s9_1oYOTxsQe5oll4oOx1_q7qZfazBjezHouRmrPNjnXrya3SeyHBmvrsGkt_7oN9N7Wm9gkcN09q3EeYyeQr6g7yLBoE2A0b0n6tvMTQYjyFXeU_XwbeL0itgFGDdZsuWT-ilkKljlynIFGLR36tsQZ55TpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشاگری جان کری از اصرار نتانیاهو برای بمباران ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/664548" target="_blank">📅 13:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664547">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9bedbfb78.mp4?token=C4MNic8bddl5wNR3oLEtW5vHFL4qPZVnGAFsj6kl5sxWof4W2B3IBfrkF6CzOelfa8HzrBUphP1kwYRIFqX0P-_cabvTgiaJY-pu-B-_gJDiLFu8emN1pUjyq82OjkcLxQE_Enq6lHI5QKNQ8LFUjL0mUJu1jp2mK50SF8jbnohzscdDqKhCpKZ6BgOi9nSw5aom4HR2yO1TiuVzNYeUXlizxs2B8jJYpPuCUCShRKOvFhfuwLL_vpn5R2ineExxpfhaKI3bHW1P7LlHXBeiTYbrafU0_7essqRqC0d_88bnZW8JfYRVb7Eq6kk_Eh9W_Gq6XnSMzEvQbGI1mkdfhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9bedbfb78.mp4?token=C4MNic8bddl5wNR3oLEtW5vHFL4qPZVnGAFsj6kl5sxWof4W2B3IBfrkF6CzOelfa8HzrBUphP1kwYRIFqX0P-_cabvTgiaJY-pu-B-_gJDiLFu8emN1pUjyq82OjkcLxQE_Enq6lHI5QKNQ8LFUjL0mUJu1jp2mK50SF8jbnohzscdDqKhCpKZ6BgOi9nSw5aom4HR2yO1TiuVzNYeUXlizxs2B8jJYpPuCUCShRKOvFhfuwLL_vpn5R2ineExxpfhaKI3bHW1P7LlHXBeiTYbrafU0_7essqRqC0d_88bnZW8JfYRVb7Eq6kk_Eh9W_Gq6XnSMzEvQbGI1mkdfhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جان کری، وزیرخارجه سابق آمریکا: تنش‌ها با ایران قابل اجتناب بود و ترامپ تنها باید برای مذاکره بر سر تغییرات مدنظرش اعلام آمادگی می‌کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/664547" target="_blank">📅 13:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664546">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🏆
به انتخاب فیفا؛ ۱۲ گل برتر مرحله گروهی جام‌جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/664546" target="_blank">📅 13:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664545">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b90205e642.mp4?token=BFoRLmSHTmIdowIMGtzjq6lvUbQorQVEK1p-AyMQaJNbqJw3bSPTZFlaLvA5RGs7Jr9wEjikwPfXTAjwpMbUcL5PjNgmsD4naFJxC_mUHtt0c5n2HoBe83g2tf6RAXdmZ8Ll_xFPHog9EWX3xI8jA0Xnq-6kA_eAEo7S66lKdFt4-q0B6fnRLIwyrPa0zA90CJ94TY8RU5OKFnRgUEhLZcJlh8lcv6ZypCjHIr1A7_hIBCRfAteTtCXswgKru2bm_yoShoQ0HGE5QfJ6AepmwdO-idXh6IW0vnVm5u_b2_2V4mjy7iwG7OGvZL4javy58ACXfG3HrFjeMW2mHqt6xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b90205e642.mp4?token=BFoRLmSHTmIdowIMGtzjq6lvUbQorQVEK1p-AyMQaJNbqJw3bSPTZFlaLvA5RGs7Jr9wEjikwPfXTAjwpMbUcL5PjNgmsD4naFJxC_mUHtt0c5n2HoBe83g2tf6RAXdmZ8Ll_xFPHog9EWX3xI8jA0Xnq-6kA_eAEo7S66lKdFt4-q0B6fnRLIwyrPa0zA90CJ94TY8RU5OKFnRgUEhLZcJlh8lcv6ZypCjHIr1A7_hIBCRfAteTtCXswgKru2bm_yoShoQ0HGE5QfJ6AepmwdO-idXh6IW0vnVm5u_b2_2V4mjy7iwG7OGvZL4javy58ACXfG3HrFjeMW2mHqt6xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۳۷ سال برای ایران؛ روایتی که باید حتما دید
#بدرقه_یار
@TV_Fori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/664545" target="_blank">📅 13:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664543">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
غریب‌آبادی: نشست فنی این هفته برگزار نمی‌شود
معاون حقوقی و بین‌المللی وزارت خارجه:
🔹
نشست‌های فنی کارگروه‌ها این هفته برنامه‌ریزی نشده و خبر برگزاری گفت‌وگوها در دوحه تأیید نمی‌شود؛ رایزنی‌ها از طریق قطر و کشورهای میانجی ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/664543" target="_blank">📅 13:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664542">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c4543ba32.mp4?token=ama8Fpn_YUQgTpJzXrIec3y7QZUdxOR3vKPXhyOEbHcxB4u6gCBw3dLiVBZ5dj4EXoCvAdKll5CkSw8krexjJLPz5O57U7I3i0AJawA36nVX-u6CHQ0G0BWBfzH7pHc2vbameQNB7DLlGUIkCpQD9L_iAneWvR_t5T4ULqZXpFtkHNEIcmHl3ej_udxl_rUvzLmO7cWvyaeapYO2AYnVXmv89OInCvgoGc6C7eW9jG5HVPo0PLzA0SBmy7yOhYyF8JGZhLi3KfXFJxpA-ZOxr9p6oZZEpOut6Kk4md_Nd3LLYLQFgevNrBqKRujrosyl6NIRvkAJfz0CDJi17B39wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c4543ba32.mp4?token=ama8Fpn_YUQgTpJzXrIec3y7QZUdxOR3vKPXhyOEbHcxB4u6gCBw3dLiVBZ5dj4EXoCvAdKll5CkSw8krexjJLPz5O57U7I3i0AJawA36nVX-u6CHQ0G0BWBfzH7pHc2vbameQNB7DLlGUIkCpQD9L_iAneWvR_t5T4ULqZXpFtkHNEIcmHl3ej_udxl_rUvzLmO7cWvyaeapYO2AYnVXmv89OInCvgoGc6C7eW9jG5HVPo0PLzA0SBmy7yOhYyF8JGZhLi3KfXFJxpA-ZOxr9p6oZZEpOut6Kk4md_Nd3LLYLQFgevNrBqKRujrosyl6NIRvkAJfz0CDJi17B39wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمای جالب یک دستگاه سی‌تی‌اسکن بدون پوشش بیرونی و اجزای داخلی آن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/664542" target="_blank">📅 13:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664541">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSvZwgkSBMeEjVC-aFTUcyndz-c3_XKZZb8lYmJVwUmzVFj7Ge2Wa34KNRIrBWWAHwKEki1ohofcy6d3CbZIUy5my-lCLNlE_mGmeqdFYb3af1ey_0H3UWHJ-FuX_VrjeSzVvyedjmU6cbYxg_TVUFqHiyCdcWtv-Ma2XEpXJCm_9e3O5_-2v_Gr6SsvpJlS2YMzkvaNbvmOJQXqmb5aZ0k0USHPh-6oK0mbYDtV7Y5c9M8Q9wpimdkpK_ah_XaPMlase3T5bXMbwEU8B7akzOFE1St5pHZVSLr7zaiQ0RMPfajZq01AqVp5FL9fz07VCd46TGwe6HyXel_8ZkMnKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام اژه‌ای به رهبر انقلاب: خود را ملزم به اجرای فرامین واجب‌الاتباع حضرت‌عالی می‌دانیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/664541" target="_blank">📅 13:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664537">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eL_K_9giA6TZ14GGMkuhWVNB7CYK6GFZ9WnlfkxuCLGOyc19OUZfB2BECN-a7JAbgb6tzYzwcbdTqngzgiEM3Igs5FULkYZQ6xaeusoUGm8tnpYzQZ6C_c3x30loyLA-jZQB84kYDCte__5FmKER1jLoNKhxjlAoudb_iNqi4D1TOcB2iVoytlOhQKmx6cmU4Ds7_w-5-k4eojbq0YJPkLWPlUtSLJDWaU8mhbtv-yS8ftDhkGJZ0I-y_oI1qz6_BuZUiVePTFiddL-bHJb_5nKEzNP0UMV4MemcxEpJTE_-6_VUV8aVLn2_i0DsINj4mP-AOa9JLOSGPvJpLw-_7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش مهدی قایدی بعد از حذف ایران از جام جهانی
🔹
عشق به این پیراهن، با یک شکست یا یک حذف از بین نمی‌رود. ما کنار هم ماندیم، چون دوست داشتن فقط برای روزهای برد نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/664537" target="_blank">📅 13:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664536">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
مشاوره محیط‌زیستی اتاق تهران؛
خدمتی برای افزایش تاب‌آوری کسب‌وکارها
🔺
اتاق بازرگانی تهران با ارائه مشاوره تخصصی و رایگان در حوزه محیط‌زیست، به بنگاه‌های اقتصادی کمک می‌کند با مدیریت بهینه منابع، هزینه‌ها را کاهش داده و تاب‌آوری خود را در شرایط بحران و پسابحران افزایش دهند.
👈🏻
کسب اطلاعات بیشتر: ۳-۸۸۷۱۴۴۷۲ (۰۲۱) و
www.tccim.ir</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/664536" target="_blank">📅 13:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664535">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiO4h3KgBaAm9Mzc0Y_1gYiVe6cUd_yHbqPrhTNOj62798i4DO2fqtHTE1RgqnuKvyb6hiSrqe2ySRwXvu44pv9bIaoqORBG6gHbI330_DeQCwLX1ZzMvBifnZuEPX5I7q4ntADZPr6tLFYB7MfR17WxLkNW0Kjz9vL1RU6x1okxPngCLeyD8rbWN2y4WB4CSiTizAxzTNGEp7s40je5ti-FwXzSZi--xWIwioS5jb31k95K6yXnoIPHZHH1iWfkqLa-xinyVPUzLqgBSsjk18NrHrwIqlJ9tu6uUlYDJvOp9CLry5w1d09l5g-7yvHtMBgoscQaGEkxVtB43tezlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با حضور سعید عزت‌اللهی از تیم ملی ایران
🔹
رتبه‌بندی فیفا از ۱۰ بازیکن برتر در بخش دفاعی پس از پایان دور گروهی رقابت‌ها
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/664535" target="_blank">📅 12:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664534">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c1e624ef0.mp4?token=d4OR1T6O-FV_rrGD0v5k9wrdb-jI0GzJkQRVgAXa0rSDARUb8Z11EaZ3TqZTeltcec6N2b06kBU-W3uKncifWTdA1naEIidCLAEDPE6LPhdjxnq5qAlaqqyTfL-YMuxGWnTzQop8W4QjqSSU4ooXZnFjVHQklS8wvvcp8kjI6faWyOveVd5iy3tqKFXs59NHzTIc5HvoeAHEa4c1f5nTyuBBjXl9zGwuSG66SgYqOV7gw9S_UsmtejRwbAdkGReNTg9Zw7HlitMkd68zEEXLZ16Q_MpME6nnWnh_43AY0KUITGK2d7804e2liHLb96i4BWPgnEWbtLg49kln6nvOKDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c1e624ef0.mp4?token=d4OR1T6O-FV_rrGD0v5k9wrdb-jI0GzJkQRVgAXa0rSDARUb8Z11EaZ3TqZTeltcec6N2b06kBU-W3uKncifWTdA1naEIidCLAEDPE6LPhdjxnq5qAlaqqyTfL-YMuxGWnTzQop8W4QjqSSU4ooXZnFjVHQklS8wvvcp8kjI6faWyOveVd5iy3tqKFXs59NHzTIc5HvoeAHEa4c1f5nTyuBBjXl9zGwuSG66SgYqOV7gw9S_UsmtejRwbAdkGReNTg9Zw7HlitMkd68zEEXLZ16Q_MpME6nnWnh_43AY0KUITGK2d7804e2liHLb96i4BWPgnEWbtLg49kln6nvOKDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس‌جمهور ترکیه، اردوغان: آنچه در غزه رخ داده یک نسل‌کشی است و اسرائیل قطعاً بابت کشتار کودکان و غیرنظامیان پاسخگو خواهد شد؛ ما نمی‌توانیم در برابر این جنایت سکوت کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/664534" target="_blank">📅 12:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664532">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f00387c6b1.mp4?token=TUJ3BuhWmeemTYIdiiZQJePV_fH-vuCdfaYY4gXhM5wphrwLddXbefz_6T_DgfnrYDNO4UwW-K8AhdEikMqbNb7OnB-B60kpICe0AiYzBoBYUIrXvjaU1omPTiL90KKeCYNSxKTYyfmB9GMNXMFlnv-Jb2eI6EpizCq2udckWSL5AAGCLHh7T4-YlN6VjgpSPupA_H5xhBxQW0ODVTEMBriE9Aja1HHNAXuQNPPJScVLPuzmWlV_Lw2PEijybOVYjpCEls9YdVlk8pkNK7Uhd6mxD3o5ob_AbB1tf6YDPJ2XQMiUUdywdVSgdpgsEQDfFDXVzWnfBwOOvuFlh0mLPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f00387c6b1.mp4?token=TUJ3BuhWmeemTYIdiiZQJePV_fH-vuCdfaYY4gXhM5wphrwLddXbefz_6T_DgfnrYDNO4UwW-K8AhdEikMqbNb7OnB-B60kpICe0AiYzBoBYUIrXvjaU1omPTiL90KKeCYNSxKTYyfmB9GMNXMFlnv-Jb2eI6EpizCq2udckWSL5AAGCLHh7T4-YlN6VjgpSPupA_H5xhBxQW0ODVTEMBriE9Aja1HHNAXuQNPPJScVLPuzmWlV_Lw2PEijybOVYjpCEls9YdVlk8pkNK7Uhd6mxD3o5ob_AbB1tf6YDPJ2XQMiUUdywdVSgdpgsEQDfFDXVzWnfBwOOvuFlh0mLPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بنزین هم در روسیه سهمیه‌بندی شد!
🔹
پس از حملات اوکراین؛ روسیه در برخی مناطق بنزین را سهمیه‌ای و سوخت‌گیری را به ۳۰ لیتر محدود کرده است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/664532" target="_blank">📅 12:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664525">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GGue9mktf_kTLURL1NLnacIPDxgbCvRaQ7M_HyKkYQCVLmqrycqz16wFcJkfksO-faVCplKuPDbH8YakMMm8VK-bwOBJX6MZr4OTyquhmKvHwVWT-sLAhhyEeQb7Lj6tE6u4XR08oZ1EKwDhGLKqpjEy_m5-Wn3v4SWSSKLHCwh5Fr_yX0jv8nGmL8VD3RGEWCr1onH-66rvHvzMyBg1qU7urFuzvQS-vngJm0kFyCWtoKdBnJ34tNhZ8BWdlsx3Hte0ram2KsTQI1EgBzNSI3hQZh2e5S_SnUBbZjUn635WB0zW-kwfD7zSQI0cN0SDcJiEHYcZ7X0DLMoDQ_ViPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kBFF1k0OZMDT3NeLDSeP6cum4Ywf9N9ZzXwzRATcO8vK_eWV43kjmZAecRxauMVq8NUs97UT3PKWqcXhD1fILbNwJc9GLmZgOH1ZRKpoTAPSqI4Xo7ZsgGABzzqkGzteQQHMLIzjcTLOoTGq1_dJq8fEWBZPDxlfMKDwsPYEwAZ41p2FaTEzoE94689wUe33SbxktsDVq0-kdonJXv26Cxd-_3fYnjZ8vpCZGhksoFmIn39rK6oQSblbmGCGy4cWP-prgrpc6aXXhUpifzpo-GEEqwL50nfazDZaJQlOtbI5D5FKZQR8-I2Jr-ngSqxnngeudOs9vQK_u5s9xyokOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JCt6oZXoNMRzgPl6Z--zHqf2l8bw5vydAxCv7Dg9iDCJcmJGE0UF9bJBcRpGvXe7rzD5Zbvq4UVMdu3qreGrLNAe9w6RlB6k60EM3YRyMV1-KKT2uOCCS6bLJJjwKbXsV3bOrwzPGaBayKisn5wZkGJIbwKYzk-Db2lFaAa-IXRsQcVwLY4LZrCbbqxEPk7D-AwBpgLDLuamk2dd4dAujynCRDYX5LVMvvTH37FQQtxG9-w2UWT71TlktS6r6q5Uggz3tWcY96eS-Z0nfl9T_vG5ctU0rifpr9dzZeKS2G8wIJMCJbCEjzf45Cw8mP8sWpSfp4uPyZ8ZV7AUf7t_oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RL8jMJAOSoXp_EnARC6C4JEjospsx9vMmIOqIq1VSSSQ-asQuNysLOvS5IipXclmMel_gVw3NcVVtu6iNgyEvWltExbqV03v46Avq66OUNDWHyPgSFAbEPm-TrOkQfkLHWbLZRg1Hbpizgf7BnqTInpfWqDqXf_nLOhhCcmnOPmQ1FtWzLjoaHCuO7pzgdMNBamuYvp1eppoIIBbX2XmqibHNkXeAgdHypL50riU06R7wXBiLgj3S9C5aknifCD-Zeuo83eGd_u04pMk1UB-CUS8yEpI8DLIXFV4sCjuL5p9zv8IjLA5UibB4JCi558eJ_bVGVpMMDbdr-iEp-4ZYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OiOSRsJhcsirItK_Ejd6Z6cubRl0PNBCpBoQbHK1bWUpRi2To3aUt6XOZGrxTNeYyoSZunUgd-wPTFg869TWj1raYYXJR69nX1rM3wq0oUHR8KA3y7-tyC2OPdWuk6OZLKmROI5VhFcoLmjpBic1-7xBGDdx9-7zd2mMpZs-n0mKzz_mowvpyME50wdyObwF4lti1YoG9iW-6splF_pTOuMGRI13JXdMeMSdHvwfKWQ6j2JyPs-q4EveD1rdanYcd91j_9liFXpZf-zPr0ediYQhhSp7LjZ9MH_d9RGXWMF59sOF-msonUnJyjOpZkfgTJVY7J0w8ARYk-VPYw_Nbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MKlamH1Brhw7fM4b3QFZaKH1uALb6aczPPbl0ALDBJ9QjznMvoXtuFCB6uWK3bp55HG6J04P2eIiBCJcgu84cSRjlbTwYcF7GLyEcJH0P-4X4DHAFlfdLxdt4HcqieYTBHI9fQSHnDqg6OJ_Y980_vgydh4lnKq2C-wCw1XUacZa3ysp7gsr20ndZiCdaZH5GivPFOStmWg6WFffd2EFhX304mIhEmZo2mmX0wWEipvp6F10EOGUbMeHiq0zDi9qylV0I1RjWEoc0THeqS3Bwj0se5SO8eHDWpNiALf7eetB2Id1Nh1D47NWtixvslu7rx95zYxKL62Dhd1Khh2MZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hbzh2SBwJfmKmpCaqZPLHx0lav5zJY-aCvdlajDYDoNJvBqaZSN37OP9aqJD7tpWU5p8LMCN_pykxxrT5u7kckAZtyA1e3PpmqxYzKVPg8DR_Kuyh8zSMHY8VO8-LWSXiX1u9thjtyAGrmZf-uwnLrjlESuSygOCjlrfa4BDj_SvmilqXR6RCreeNW8jg0_i17afxA8r-zSYs729uBEQC9JYjGCjl98V6P8nKb2hx8fwD_JfStKdGm6WBLXJahUmDy_lfk1wbJZioD0UC3V8iJZv2cImFlxqte9F6576CtcL3F3xOWOetfRC6JGBcxE1daj5xPHgxsslFOcyxlpQfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نشان حسینی
🔹
قاب‌هایی از شهر شما؛ خانه‌ها و کوچه‌هایی که با پرچم‌های عزای امام حسین (ع) رنگ و بوی محرم گرفته و جلوه‌ای از ارادت حسینی را به نمایش گذاشته‌اند.
🔸
تصاویر خود را با ما به اشتراک بگذارید
👇
#ایران_حسینی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/664525" target="_blank">📅 12:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664524">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dae801529a.mp4?token=hYj1YrMl6hm5bcxcm32X7j8mhQ1S8keyN9IKmaMtzeYo9O-XYodr3c8YOEd8x_XvBUbJpPiQrQA2wv1-A35UEo2ZiQCBmZES_VzG90Q8Y9YNOYF1o_Q0shO9ItNd_hIc5o5j0mzQL7OegnUEO0EJibLn6ZF-LI_BrxQRlKN82VhN-UWQha07tNXJlT2cSpGaDeKzsxrAiGgOEgcqH60iqbxXCS_i55DvNLrpxM84Lo3vJPJhxu489NX69vLOQiBYA-MBMnZLKeg8DcsU_fEfoX3tfdXw7iC53iMzg3itDstuFsicdsSCqKZFk52qv6as6Nzlx1RSBuX8-n5OmcqnNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dae801529a.mp4?token=hYj1YrMl6hm5bcxcm32X7j8mhQ1S8keyN9IKmaMtzeYo9O-XYodr3c8YOEd8x_XvBUbJpPiQrQA2wv1-A35UEo2ZiQCBmZES_VzG90Q8Y9YNOYF1o_Q0shO9ItNd_hIc5o5j0mzQL7OegnUEO0EJibLn6ZF-LI_BrxQRlKN82VhN-UWQha07tNXJlT2cSpGaDeKzsxrAiGgOEgcqH60iqbxXCS_i55DvNLrpxM84Lo3vJPJhxu489NX69vLOQiBYA-MBMnZLKeg8DcsU_fEfoX3tfdXw7iC53iMzg3itDstuFsicdsSCqKZFk52qv6as6Nzlx1RSBuX8-n5OmcqnNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یکی از پیامدهای غذا دادن به حیات‌وحش و رهاسازی پسماندهای غذایی در طبیعت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/664524" target="_blank">📅 12:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664522">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mteA5hPbaMgAmdkuWgXokHjiQQ44I_Ix-519p5kodZgVm6LnrsKVcsqXyoL-K4CmsACZLWnzhyyWnjUdDVtswwuLj2Ld2H3Z8M984z06MmNc6U-OLPf-URwaZF4vaWwMRD5VgV3bBhaKmU3nA9KReHOGwpRfTDkGm1RXxfvTmFSQfiEhwnrn0FCYSlRHMwlm33JnKeF9382biaaRA_BzcjjhDLzNn3ws3vBOMeuMBcKZbPgbqgblxqvI_6Gp_vhpkX3_jS5-B9QrbCClrkcUeGdDI9VweIba6ZA4KN5ZPjphDPPk_LiavYD6MI6uidJHvWcw8aFGbE6DgEnkRQc_Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماجرای رابطه جنسی آقای مدیر و منشی‌اش/ دوربین مداربسته همه چیز را لو داد + عکس
🔹
رابطه جنسی یک مدیر با منشی اش سبب یک رسوایی بزرگ در عراق شد.
اینجا بخوانید و ببینید
👇
khabarfoori.com/fa/tiny/news-3226323</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/664522" target="_blank">📅 12:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664520">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdeLzSIGZ6hj67PHIMDoIjbIqtSuLdM_SyxNKJO7jjmzcMpYmpLZUQ2hv_RkF7bQfSIyaR2GiIHgRr2ApALm0xxpvt0Z0tYSlsIvZjPzGKeZ_AOQGdbHLXxD5Wba11B552xBOWXBR-vHJvzsykawD2Oil1ZmyT2t05ry1Wl_kFCkZ_9grZ-bFtTQoYSnU6tM6VWKnwmRz6nYi0i-wCRJF74UPaYOAF-CRrak55IFoKZJeUH219uCMGIyvZeYJDTXv765A6NrvR129f69kcK1WWiW_f5nd5KJ1tiDjXrj99LoB2NmJBTP157YotsMNcNnDb0R7ngagjWQUEWlZTOM8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از یک پست تا یک پرونده؛ ردپای دیجیتال چگونه زندگی ما را تحت تأثیر قرار می‌دهد؟ #آگاهی_رسانه‌ای
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/664520" target="_blank">📅 12:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664519">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
رویترز به نقل از یک منبع آگاه: گفت‌وگوهای فنی ایران و آمریکا به‌زودی در دوحه برگزار می‌شود
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/664519" target="_blank">📅 12:10 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664518">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvCD8zKsrQKFIfzBCm6ci2atBSifF6D9zwfO1xnYxbCoS62T0KFe-tqeUEwVSLKij7x_5K01MewalReocNexOoN1A3s0tixaMfbjdVErMXOUUA_J5M_TfQkiO0OHeWD98pWBBl748hz3TVX6Y3OXnfUdORfW-pKj_vJqWk2_pYZVGkI0hFePHdCSEnHUmbymcTWAUorvR9FRG-Ky2OHkW3wp_b_T3aDBCxehrI18SjC066ErRqZoiXu56zm4IPmPT5rTHhkBrrCorYOtF21Bagh2RcO44AEcZG_RZMXlRsTjajUPTJz_SVkBGlTAuPBFSKwR6wMqWyZA21Ll3JSRRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انواع آنتی‌بیوتیک‌های پرکاربرد و موارد مصرف رایج آنها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/664518" target="_blank">📅 12:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664515">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9521654c.mp4?token=VPFsxAfoI0DOOeLDZIrBnvOv-pqWkd_lfEZWyOquAfDC9DkxJ5JOQKvUUE41rZ5Gp9y_wc8hkQuHoM3Xj3qwZVqruSJXNVkBHWtiuvVQEaxYI8qiVX0XFbD0X9nJuuV52Psd8Cyr-7SxNUdvmafvIDd_I-pTYUku2vHCPco2XlGbgGqvK3adlNhdiiQl7QxOuxTzf7Sy3mVG4YKnVk3AX7i6jmhersidaK7ef20Q_u4xoQx49io_N_sACW3_pNdHXMWcyuv7H5DQogneCZRZPerGdRPO4x27ZRFBhTUmAq6dR1ReWeUE0xfzHFgUkpi8oijBPp4zRYbuB5w-_sAPoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9521654c.mp4?token=VPFsxAfoI0DOOeLDZIrBnvOv-pqWkd_lfEZWyOquAfDC9DkxJ5JOQKvUUE41rZ5Gp9y_wc8hkQuHoM3Xj3qwZVqruSJXNVkBHWtiuvVQEaxYI8qiVX0XFbD0X9nJuuV52Psd8Cyr-7SxNUdvmafvIDd_I-pTYUku2vHCPco2XlGbgGqvK3adlNhdiiQl7QxOuxTzf7Sy3mVG4YKnVk3AX7i6jmhersidaK7ef20Q_u4xoQx49io_N_sACW3_pNdHXMWcyuv7H5DQogneCZRZPerGdRPO4x27ZRFBhTUmAq6dR1ReWeUE0xfzHFgUkpi8oijBPp4zRYbuB5w-_sAPoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرمربی کره جنوبی، به این شکل بدلیل حذف زود هنگام از جام‌جهانی، رو به مردم خم شد و استعفا داد #جام_تایم۲۶
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/664515" target="_blank">📅 11:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664509">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h_fIF6tOXK-LIQa86zj571T1tme6qrLt76Q0QoCvcYQSa6OUmSQafwjJAbrEuIiqCVvXm1wFzGJYePpX3FZ2HoSahEZ01z6VIZCFlvQmvz5tlUAbVI9z9892LJHoR6bzmHeXVcZsp6dAm49QJNUGjiMeAczomK9ESn3DecbQnYZ1GwEPKEvJ3riL-qSkgERF-lKWdXhKeCDO2APfbVH506CM8d_u43zbDy_HEl7wU-a0TyH5nzQI1FYIJOxikGqz0RTmJLAQXdx3ap96rg6Q8nQreDaYm-tfIaLmqENMCeXreMXRLCrqdaFK6uKVLUOmv16sDx43WCaP9fkD_77G0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YcC6AMy6J-a0EUDTazBdTQ32OAGw_V7B625E66f_isMxOodSjeGdtzTNMm8MnaJnJPs77Pe1QyktlBpXJid_o0sHtpjjMPP4zV_KbbD7A1zp4NwlxNptjJmy_bUkQ3tIbOmFepVwUlv6YexifunK892-enZTKyCmoK9xA_PUU4UDSbR1U7K2xaNwkhdH30OvQKWBFYQtmR3A9lmmG38zU6CSkJV9EueaHcnQRxbAFpZzgmTHyCmCafvJ6_bB8wTAkgX-1mmo8RDY7-gv278qUqJgt71J81PkKVSl5ROtJY9WRLgA4Ge0UMlF8Y4oTiI6-dn7mgRk5prpoI8M2oGicA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hvJ9qfqnxL_doLkbFcGngtJAWbBVOT39shhwYZUytea4-dotwe5DyaoDRHXFkvcrVbbGDx7wsY4zxqponTB-C9NC86GWbU1xeAdUxjXp9hsu7Pq3nJ-GeDNXzHgK8flERDpAD5P2n7nFBwzcAoYN5DsG4R1nxjp_dmHuujHcjO8jj4vfnc6-9WotquiuCIUjkdxAxeabQ6oK9noHQW9rOcTrWQQQwiYJnB8Cj5PMj-cB07g1xS_hvehzJtIIChScChfmzopalC1UWw3jUqowMk7PXYN8Feag81zGINlYTx0asenCJZtJme_CFJ1mwYnO2mbHUVfNXy1sY4-NyPX4Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/diS54rSJanZxZFfmyAewuUXMVCNr7VNQmIXGySur8hsAfraCv6MIMTOT1k9FBTYu491dp3GmBqDHuQG3EKD6AQ1rP8G9OasVHOzxMKDQI49pqDfR0sMzo-vQHoiHWsKit3gjg-M-5j_v-mYZIhoSUsV9bWn8xN6AEVXwmg7ZcbvgsNk1VIC_4IrHeljGHEKRmROr7JpiY7APONo_fzUDpgo1bcrQzH8NZ3COPdiOOzEDBUBytWepY9-ksBLyHduRNctuA-CTe3nbYTXEdPWwQer_GE93WhuoISLeiAp24Jw9TPNAKsfm0abbLGwSHf2DhwT5gbfg_8-NRzikNhyU9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qJ_4zCxvBadJqKU0nqxzcahqrcwWgURL1wW-iL5uzQjiOtgEer66br3rZFBv2Hlq3rXwzokUI23OKJXndBhjk-t2GECZYT8aCfb4deGsEbra_q_T-R1oN2_zv1cUaq5I4qBqwQZS4e5P2Qi_qVnuGTMRBRlG0WKisCDBDsrBwREKtKymgR2kQqYuTxrGNIAtjqpb7rTHz_wBFEJ1wNHjg351x3ps-Vb6IBYX28T7-DYdiHBGZ3SBOu3uR2XDFBAnZVBXhi7g_WrznwzTPbQhpCOcQhJUXFPbfhzKcOgsRAXfsu2q4jcen6I8NZp7WNFGUjodwfPjuJPzRm5FWfxA9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hp1AEJncLG1Cfi85_-GDV0dpdLq6DpVBJVrAysPTAVZ2QKl4DqW-Nv-CYzmvX8FyIEUAjBnImrZdk5nygqdA-ihNVB17LGRynGaJct9dsVBTAgDj_5CDWsHPtYm0XHYvDvas_TlcfG6G7N8zbanOABOYK1JVFoxWLVJSMZUU_bOMwvGGX0pQ1FhOz_qZkqu8x4JDc3goaTspBOp-dj92jp8TyamvI1LWJSCaWB-_aLFLwwO_eBmDsbVYIfbXxKbzXCZCcB_ZMETRXQCV5OZBuLMUzyT681cT_cONXfR-hzvAOVMD0mO7VzgVOegaPU5sjf9IC0w5QXrxdUNgHv1DAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
خاموشی‌های بی‌اطلاع، موبایل را هم خاموش کرد!
🔹
همزمان با آغاز خاموشی‌های بی‌اطلاع تابستان، گزارش‌های گسترده از نقاط مختلف کشور حاکی است که تنها چند دقیقه پس از قطع برق، آنتن تلفن همراه و اینترنت نیز از دسترس خارج می‌شود.
🔹
موج خاموشی، نخستین خدمتی که از دسترس…</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/664509" target="_blank">📅 11:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664504">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dm_0o9cOaoARXFJfYBNqreYeuE7TwipBbZPj3vNO41BzZVZnoQiBuzorf75YpaIYCw9SC-RwoKM8oNGjbaqbSY1-DJNY8Dzt_kUwTD-9dq421bzGRi4Oib9EQMQqNCtHD18hqVCuv1WliMJwtoPwIIXk5TMZq8eaJAV62uWl-xWC6NAYOk3L4F_sRHVwT-RCVadB3Pds2VB5Fw5Jsngv1aijbF2Q4qLPdZ2eKrpG9w94XZo88CN5eklaw62nwAd3SxfTwdfICAovWl07G462IE7UCggOYJ5QgKnEGiSY-z2LIVQdi0V19gmDck0G_DMf4Ny37LBtYY9upEVsCzLpYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با چراغ روشن بنزین، چند کیلومتر می‌توان رانندگی کرد
؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/664504" target="_blank">📅 11:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664503">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
نشست آمریکا و ایران در دوحه    باراک راوید، خبرنگار اکسیوس:
🔹
مقامات آمریکایی به من گفتند که ایالات متحده و ایران توافق کرده‌اند که حملات را متوقف کرده و این هفته ملاقات کنند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/664503" target="_blank">📅 11:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664502">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxiLhxc9NgQFhlAB6UMwLOfJ0fh1R96aJwfI-PIF4AGOEDgF4CZhEz-nfJxZvkKQI_-hztIjszMOxdh7i6iF-DTCdg9ea3xITNXBgnW4dXh2WMndLVO-xlXGOwqX4Nydiu7ejg3VZFa2q27-U-tBRLzO2o7V8gVFtAjSZBX5fcy7l3CvSUAItjVTGkltC_2_dkm7_-Ye6Ky3jpm-JTZwxU8jqLNQS9jv-G2VeZaN457CrRYgjnuVghaHqi6lyydDurkN30Po6aA_Z9gAbpVanCho_GELejxYh3Jqp_2HGl2mOvWXmWUHE3eSJVoSv4fXw7RWtK9L7pliG0qvqgrrpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وعده‌ای که محقق شد؛ عدالت ایستاده است
🔹
گفته بودیم که هزینه خواهید داد و حالا این هزینه، تمامِ دنیایی است که برای خود ساخته بودید
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/664502" target="_blank">📅 11:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664497">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/niZdAqCvMHq8NHGWHyitQoXcWQQ5Wmxf85-UyKBbL_KZrfYSnSIM9uean6ScnHPZgVSrmKLxg-UlDzoQqi61IVbDqHs4HVIdkHuRsUqFfD5WxnmTenT2zrUpcAhT9OTGviNPDADYMlRSm4jS92hQvx4HowqH_ftfPP6UBNuDET7tqNK5E1pIzYF1VFOXO8V-JoVOjC5nJ7O8mQ5l5BNrI2SVGrE7b__ea_ZbidPKLosuXKeKEaXFDUcH976kYriqjwTWjTbGpVdUr7JSpN_RRcaIv35wP4NCPv4FC6iIpXPiO3ucdS-AKyGhRNN_cDC3CWGNlgJadWdm9TsR7mcOzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gub3oLkzGUK7KGcmkKO8bGS4-TEPNAaFb8iZR1176EdCGUtd2OHEQlFhTyeaZ9de0GgIqeHgFacVQ_7MDINVRQVspO4smppbysQcAR8UVX2UaiQtaucRU36ymSEQ3r8mLenr7qEhkvQyUIC7iGLAsAIQctO9o8mMpfQZFkrdVEc3BSWp7Jw0InStw4xtCGFoYRDq5pxfkESPCV7FUQ4p0us9IKf8k1thnkBUwXEa_qvo-ZBwZgaz1UkFSbhaohgl-2aVWfCirmLb6RtN_iwKwUcafwpp5yX6_-PNcMUvxxmNBgkRPGbctFEFQqG3mtzFZt1iz0PG4UT4OO6SGv6VWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vnCp10Hl8t4pC6E-5Qgp7_W9_OZOOISKVfMtAn9gyElKpvA8gJUxUtHSwezkZ2q0GF-VhyrfrKGe7NQgoGu2yd0-664v3zht7uHlXm7E3FVWm6U1DT8eVL70QZXZNXZ5ph2kfN7VPG2_5yfoq-0z4OYY2R0UHXJXhZ5qI9oK3z1Ha3pa-d0sZbi2qwkmxJm2LqSZ8McaEZUi_9HeEI3a2dgyi98blX8E9_7QWi2_fxvkjovBN7gYnCiG7WDfg5zc5mrXOiH1vR9GsipzKTZmDzrpmedIroaJC8ZF4I1xkjHWQLYxBSCR-WE78eURVME6pkZwxJa155YTu4653SmhIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pPdJqOz17NnmMOpDXYXnQ0yYcQwNvlMZ5Wk17y0gSCUkD0LamjjO-inbSUefjEkmSuXUX8AzIOav51FZR20_cfjbaepZL1NTEQeUvU9PYtWAtErwF_N0zcqMK6NeoWfqnI26DvMwqSkzvaWKu0FEaJINL8FoPUKruMu0yrfdjsuxjeCe_QeBQQEQg4frexvDD0TgoqKD3IeG0CwXFn1TJxS-dUOZ-9SX11kiRBae6NrrwCvWnfmZwuEsxNUXUeF2XZw1gA_xWMBUSl9pE_2CKtr29mjdTY5yeRuNxysdndJGWoxR1lLOvyGIvm1o6xQCziQB3P6Oo-F4wFl1oKb2Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RRQhMk8etsday7dy-FBRP3HO2vSOIVL-BQ-h-mvj_oTc_3o-yTjL1D6gRDLfkrRmj-TqAe8sSwKz8wan4js86fP0G3rAUCQUAyyyD6XyIaf1WO-s4QGO5vUfVKg9R9Kn4KlDfu7W1opjKk26JJkiqmJV8muxlqKKM6Ga6MMM90SDVRHjddVPlrTKUjPn_6Eh590vg6ohNgFmqeDqKghKnRzrWfah6nuDlW3E7uEWDKbXQJPAX7C9LDYFhtugd8Ctf5JJ-pFYnr5NDwLNqlGTecn2RD_mXKEKEwcNLbXX13s6g6m6NX87wh6DEq_2To0lLjn3mKK2-Kh2HQM1eUYc3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حملات هوایی پاکستان به سه نقطه در خاک افغانستان  ادعای مقام‌های پاکستانی:
🔹
این کشور بار دیگر مناطقی در داخل خاک افغانستان را هدف حملات هوایی قرار داده است. در پی این حملات هوایی ۳۰ نفر جان خود را از دست داده و بیش از ۱۰۰ نفر دیگر زخمی شده‌اند.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/664497" target="_blank">📅 11:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664495">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
رفع اختلال در سیستم بانکی تا آخر شب
🔹
مدیرعامل شرکت خدمات انفورماتیک ضمن عذرخواهی از مشتریان بابت وقفه دوباره در خدمات بانک‌های ملی و صادرات: تلاش می‌کنیم این اختلال تا پایان وقت امشب برطرف شود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/664495" target="_blank">📅 11:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664494">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
پیش‌ثبت‌نام حج آینده رایگان شد
🔹
پیش‌ثبت‌نام حج سال آینده ۱۲ روز دیگر آغاز می‌شود و امسال ایران ثبت‌نام اولیه را رایگان کرده است.
🔹
پارسال متقاضیان حین ثبت‌نام اولیه ۲۰۰ میلیون تومان علی‌الحساب واریز می‌کردند و هزینهٔ نهایی ۳۸۰ میلیون تومان بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/664494" target="_blank">📅 11:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664493">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtfUbg9K7-jUH1kZrOV14xWX1Mpr1OU0T09bkL66YThqWtunBgfbKnW4lXUvNxirBz3P6TGev-Ajr8C1V2HRzw1sNn55Nz6lKMhfi5E54MQ98bK1ez5pshSWN9XdhaAwKTuRGh1yFMo_qOtD_HioKfO1ILlSXFjYiElbCiZbdjxf1v436JBPf0RYpsdRt__fs_DlswQsxPUIQGVC28eOa3MpLQgr0wWm-aU3WQgXT9ToslLBHu5POUqh18A7d9Xl0ZmeHQE6C5eKFuMMnUinwMMol_BkJwHkIt1LMx6iHykOYG-RprmIejWKQO3qcNt9ZmMhJmb9aIrQQ5Zl8OuyEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توصیه‌های مهم برای سلامت کودکان در ازدحام و گرما
🥵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/664493" target="_blank">📅 11:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664492">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f533fe061.mp4?token=e93794y-RWU6B7hZQhlreFTRFVumRN2e5TI1bEKfkxJueoTQ_EJNjR5IpplBnE2Am3K1nPGfrGzUxHmYQ-yqXd9hqRkUAN1mAQ6R3fr9Fpl-LkJ0LRjy6leQ65aXTY6WlRWrsdxxnjVuZ3poZqXoqXG51M73OE4fhcqmwIDRclsok7dAkoM5qYkAHF9NiBgPHzxuUd965R7moCOccPPSGanVZ2NiEoNQ2hm5ybFYIspbTtQIjwke1nY_Gy1efphVzlzZHOs7bLpshcRcNX8k-n8wvtvKPpsYXBeKt6UrzBNeTq4HU-Etm370G0DrTputn55IK_h_ebWwYwxdw1VMdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f533fe061.mp4?token=e93794y-RWU6B7hZQhlreFTRFVumRN2e5TI1bEKfkxJueoTQ_EJNjR5IpplBnE2Am3K1nPGfrGzUxHmYQ-yqXd9hqRkUAN1mAQ6R3fr9Fpl-LkJ0LRjy6leQ65aXTY6WlRWrsdxxnjVuZ3poZqXoqXG51M73OE4fhcqmwIDRclsok7dAkoM5qYkAHF9NiBgPHzxuUd965R7moCOccPPSGanVZ2NiEoNQ2hm5ybFYIspbTtQIjwke1nY_Gy1efphVzlzZHOs7bLpshcRcNX8k-n8wvtvKPpsYXBeKt6UrzBNeTq4HU-Etm370G0DrTputn55IK_h_ebWwYwxdw1VMdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بومیان آمریکا در مراسم گرامیداشت صد و پنجاهمین سالگرد شکست ارتش ایالات متحده، پرچم این کشور را لگدمال کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/664492" target="_blank">📅 11:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664491">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
رئیس‌جمهور: ۶ میلیارد دلار از منابع ایران آزاد شد   رئیس‌جمهور در دیدار با آیت‌الله العظمی شبیری زنجانی:
🔹
بر اساس برنامه‌ریزی‌های انجام‌شده، ۶ میلیارد دلار از مجموع ۱۲ میلیارد دلار منابع ایران در قطر آزاد و به کشور بازگردانده خواهد شد.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/664491" target="_blank">📅 11:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664490">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5836683886.mp4?token=BFpHDwc6Sa3Xk3J4fodtVbbU23ctv5JzFrQU-ql4b30DY7NskJZs5anCgLVKB6LrsjU9MDMVN5DRdOorNxvlwHt2M-LukO2bKIHrd5WjVZNiwDk6TYifP82LbBIX7Gv8sGYtGT1yM-0mtTY1nQzPXi1hRtln-DBSuz2Est4gQmoiUc2TtpC1FjMpPYkkKkxCOsD4EIIJ7c6v9uL5uhj_2ArRmBEpKsNIr8QtXU8NXyWnlSknGnNOg3HouCrGpxHTjUlvAQ2vYJpjDi8bMqTCA0EIxV6oIigdMu6vqkYHeikBAiRWteGyw4aIVs1vXlmInDjcroFc4XMKr03ZrgFDNVNEPSYQRFZAdhPdcJ4YB931A8HtwZikWCsXQSwMgTLjlz_OpmvuhUl5dkCvwWpO0saTzSeLpH-_ZHGzOcoE4tQpkjtKauJZDsAZltIN5TX0xyRSc_H4keT9LRJgM-w9R-t7HCHr1gbVF1ZAkvqPYRDQthC9gTjVfKsXy2FCsT7IpmeR4Y_vVElhqG2QnncNuxdhRyaGHVAcGhID3_R6NPxLhhYCjX4PN5lh9GVV9TEWU7ghUMVq2ATEOfAslNeQ8G1KYuZjS04U5iBvmzHEW1PEpVEHJSC4dV-b5ncOA9bZByKUgo6RehsA4aEk5nlYOO7TQu9h9_LHJlC_DNfDF_k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5836683886.mp4?token=BFpHDwc6Sa3Xk3J4fodtVbbU23ctv5JzFrQU-ql4b30DY7NskJZs5anCgLVKB6LrsjU9MDMVN5DRdOorNxvlwHt2M-LukO2bKIHrd5WjVZNiwDk6TYifP82LbBIX7Gv8sGYtGT1yM-0mtTY1nQzPXi1hRtln-DBSuz2Est4gQmoiUc2TtpC1FjMpPYkkKkxCOsD4EIIJ7c6v9uL5uhj_2ArRmBEpKsNIr8QtXU8NXyWnlSknGnNOg3HouCrGpxHTjUlvAQ2vYJpjDi8bMqTCA0EIxV6oIigdMu6vqkYHeikBAiRWteGyw4aIVs1vXlmInDjcroFc4XMKr03ZrgFDNVNEPSYQRFZAdhPdcJ4YB931A8HtwZikWCsXQSwMgTLjlz_OpmvuhUl5dkCvwWpO0saTzSeLpH-_ZHGzOcoE4tQpkjtKauJZDsAZltIN5TX0xyRSc_H4keT9LRJgM-w9R-t7HCHr1gbVF1ZAkvqPYRDQthC9gTjVfKsXy2FCsT7IpmeR4Y_vVElhqG2QnncNuxdhRyaGHVAcGhID3_R6NPxLhhYCjX4PN5lh9GVV9TEWU7ghUMVq2ATEOfAslNeQ8G1KYuZjS04U5iBvmzHEW1PEpVEHJSC4dV-b5ncOA9bZByKUgo6RehsA4aEk5nlYOO7TQu9h9_LHJlC_DNfDF_k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بهترین تیم ایران در بدترین جام جهانی تاریخ
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/664490" target="_blank">📅 11:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664489">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
رئیس‌جمهور: ۶ میلیارد دلار از منابع ایران آزاد شد
رئیس‌جمهور در دیدار با آیت‌الله العظمی شبیری زنجانی:
🔹
بر اساس برنامه‌ریزی‌های انجام‌شده، ۶ میلیارد دلار از مجموع ۱۲ میلیارد دلار منابع ایران در قطر آزاد و به کشور بازگردانده خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/664489" target="_blank">📅 11:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664487">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7ce213c07.mp4?token=Jc_0LhHn-ZTqv8aJZjUp59XW2yRjvKzPQGwtzkjYExnJFz_oAHhKi4d9MdSBvlZMtfG77DpNtSWPtASX560p90SzKo_sXIfHy_YicnrKq_Pnux38I4KZda9QNic7WEG7ptUG8yrw_-YEMyzcd43SEH1IYKLaxutV-P2B0zTBXEOwesMHG78EzV3q1R-Qb9qYx1Y4d2AWhkXmluvS0X486BbnkWyTFoTZETLyb6zbAHZwAo3K-gSmQpIKEY0QAoCL1gL3r1MBmjFJGiiYXGxYNeKvrguZpjkdbDFPaBTasotD9deN73Qfzq35-7ZNQZRLVjLrblD7DboT-P80JiPpy0rZUpiizrsEzr6FPwDvbhE0mhyZnYeoBkPLQZHqHxI1dlPzLBaGUWEJpCZmRakGVH2uzlXMJiyFr8Qth1_0NtuIDYEMQJWRmcv701pObyWoP9k3S9Oaafj-3zqJ-_wYEgO7woUuLbK-mPovnoZxPWA7FTVACPYBywDGQVopK1cHxzh6gy-keSkKhULuDT1hOIOYxyf1kxW8lxlFkD6nb_klXhYWlDozQAXMD9pdvXiWT8hmV9fYAKiYoIEjRDqkWM_yk3fLwms8MpCEGHNMkCVL02b2b0L0640LWFQsM_YhSaqtIWQicaoRVCIsR10u0IRIz-a0RLzA58Ai2GtZ6RI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7ce213c07.mp4?token=Jc_0LhHn-ZTqv8aJZjUp59XW2yRjvKzPQGwtzkjYExnJFz_oAHhKi4d9MdSBvlZMtfG77DpNtSWPtASX560p90SzKo_sXIfHy_YicnrKq_Pnux38I4KZda9QNic7WEG7ptUG8yrw_-YEMyzcd43SEH1IYKLaxutV-P2B0zTBXEOwesMHG78EzV3q1R-Qb9qYx1Y4d2AWhkXmluvS0X486BbnkWyTFoTZETLyb6zbAHZwAo3K-gSmQpIKEY0QAoCL1gL3r1MBmjFJGiiYXGxYNeKvrguZpjkdbDFPaBTasotD9deN73Qfzq35-7ZNQZRLVjLrblD7DboT-P80JiPpy0rZUpiizrsEzr6FPwDvbhE0mhyZnYeoBkPLQZHqHxI1dlPzLBaGUWEJpCZmRakGVH2uzlXMJiyFr8Qth1_0NtuIDYEMQJWRmcv701pObyWoP9k3S9Oaafj-3zqJ-_wYEgO7woUuLbK-mPovnoZxPWA7FTVACPYBywDGQVopK1cHxzh6gy-keSkKhULuDT1hOIOYxyf1kxW8lxlFkD6nb_klXhYWlDozQAXMD9pdvXiWT8hmV9fYAKiYoIEjRDqkWM_yk3fLwms8MpCEGHNMkCVL02b2b0L0640LWFQsM_YhSaqtIWQicaoRVCIsR10u0IRIz-a0RLzA58Ai2GtZ6RI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی از آخرین وضعیت میزان آب در سد کرج
#اخبار_البرز
در فضای مجازی
👇
@akhbare_Alborz</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/664487" target="_blank">📅 11:07 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664480">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sZr4BfXTawOVIhKUT4VvFgJFIY4kF_lsUhK5jJRUxTU4McpLPqhILm60M9VUyjCqzYf4uuknY8_qt0oDbFJ8GFwmrRxCwGEUdrJf4t_r76kk5WKL_OA23tQjlJOtAaQO7PVquSiVM7GdIUnJk6w2jPUIiglD64H97UdB1J23Jd6mph6aMkSFSssbpKbDwjqe1FdoMjuJt6Kb7ZC55HPhu6ZjMDcYlvNhjznfUCsnVNYKEB2k2D17DPRqpVQuZaV9_V_86Qt3zeOonD3Dbh6tWQDEyH8NfvmLTLM08IybQy0EWWPgnq8xpPLfI5_2Fzki6Ap3h_ylf47m79jnSToFpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kxe9iVTVp39XhgaRAfn4ybvFHowqGiNatAMYBYiHb-pPFtAkI1U9ViGxUTqh8Ci8_hUhLndHOGKIdS2PpbkaEoiL2baQHs8KL60yzfFMXi8CVk8G0GtzKCzc6LCsd68NGECyQ9oL6lWQutVyxsq7r0PeY-XnyTYeXldXEXER7iVVx79dDGbOQa-Qbqfv7pNWwWw1XnW5OFEuPryKtaNqzq6rFxz05TqeTKXq2x7SKkji1DXSgNaX7LUQYBGMf4zKNO2sihcsei2GoZXP82fyNXAOdwEc4fcf-7RYky61XsnzpsLG6nJz17tOzoC5b2ZJOk_xxSsiMdL0fW4PKXATww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EbGDtAmsbBUTnR1TbmmT5vFBstXdqY3P6a3xNc6lFG8wDH-olc03np-ob1FeyV_nENfyglIST_dm4ZgFs0HsvRZDrzZs2eZp1Fi7izUsNSoqVOUTPlrwgCAR2AG-ItSLEuV6Gsbm2cr452wOCebndOTHMmJuFeQu5Qks-bFWIv0T5knk_Kr2HDKbl2F8dfJNFPwdqscXe-JksXwu6m6EMNHnYo5K1oQ__rSdr2H2s7CGU9rMBdQKzKZi6h0TgrjDBqc6_RQg5XELTp9G5cgZhSZ_38LaDZ6_gNRSky4CGUDpytoacdcHaO8-JqgCTZOI5Y6nwT2HW3tqb37YpkvhSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MW3FMz1xdnkNoEgNA1Q06zAy6iCqH5DLJ-MVHG1Csc3M-c7VGjOMwrrUUvzlpVgJuG50PNnN8yQ65iAzslPBRVuuzMaewfjRO2XztQLP4v6glxHBcMXTzJi_t8BJclb4oSMsNVFTDDdLPmLGZWN3Pyw1VnFitj6XIhuHv9zzF9OW_GCEgkPsmsE5GgLN4F9mougJFZfE3OQGCGGIsGIYd2MOZJZNx2QQh65nOZVSOwT2trH6IF-a26ilcBisLPlriWQ_0y0gs6VM6i60BG9PuHNW8Z3YCmVJ4uDS92L4iVy3VavpIOXwKu32y1WIlPkRlmMezOcA48FQBysSK4nPQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ISvxRPXOkyuCRAHS2DhQOiApdrw1xa8JFXmlywGim9G3N4XrRDWSLUUH9ByVppOtfjCaBiR-K_hx6oerIn7vXP3vRzGEh0CkuF2hcA8sBE-ZBcb7rIqKWigNVzasgXQfcNVuTv48M1VQDV7jptproci6WaLytEb-X6keHOd_jKDUr727wAXn1XZt_55g8hj_U4Zsnx4CW142jnUsRel-sIEwd9W1WyPxR1mdokkITEqGVtlTCfQctN-wzgW0NT0iGU9BnA-ru4WLI2c3bJlKN8o4mt-uPwPtwjfnOHwwujCQBqYyJf_vfL2umV1fF07M-FocrDeCnIDA9jariT5f2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HGjNAN4cZ-Bz-03ldSD58ZlawPtfO5ZDu9rWxGhP9da33-ySO_2MOzNPn7QGpvOKSZXnzZ-A0v6k1Gryv4Ywh4A0za8YGogI3Bf3RC-6KUH4i3u9Dv0u3F4wagjaa8EOy9-vgJLtjtvzIbA7wXplYvPpgz6GMwCQSaJ89BLE6ERBDyDue6ruZO_H0-Bqc9J5rgbRn1EleHBGUbSYt3-UC-MqoX3NtYRcZddeaBDp7FvYURalqx1Ww2iZubVvKfuK2nob2A62b69JL9lZcSDmUZ4KIeqdW3aJzOLlqQPgn5rk2zO9fITw50Jh5O2tj_X1cpTWlWl8964fP8Du0IWLZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HJwQUS7kPuzRud4_C7458CkguwtjLygfIXuBrVC6lERqUKzYGOmzMcEVy2apCjff-khMHevU-wadM0ib4QGUpjcOYF255GSn1M7cIpVpDxwWMlTJGRvlHbxCUQB7EcIuTTnOE84k4qH67tcW0KLaBDhrnUZtP0bnqTSbdYRBrh_KZfApovRYdEm04ZD71eiXUNxhQk_ygyfc3teZQSjj0qzYfWmq9rba96KVgs43lMI9ZD15DInm6AYM81CrK3iuOwFCBZ5x7Zqyei3c0_RxDIf5iLC5uei3rAwwNzVL0uT-tryrRjUHCJF5w8SIsrb-sIa3BRjpqCNQEfGMdYw-ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۷
مدل سالاد جذاب و پرطرفدار
🥗
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/664480" target="_blank">📅 11:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664479">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
طبق اعلام مرکز آمار ایران، نرخ بیکاری جمعیت ۱۵ ساله و بیش‌تر در سال گذشته برابر ۷.۵ درصد و نرخ مشارکت اقتصادی ۴۰.۶ درصد بوده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/664479" target="_blank">📅 11:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664477">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02ea84be9b.mp4?token=d32EhD5nbgv9y9YSBERqp-8Q4X5omjZTf6csE1Vkws9IBfe6hv5eKbm96UA_rI1rg_rNZtElq5O04cNvX3mlXrITL-JkHWAb1sBMvtdQOZaZr2gzVNy1C9odwdEWO_-I2RPUTAMGdmgMEU3PvVVsfUse-LmEouMrU2KQmC01rTGNc2MyQxtM5sOinohQ7IVwKtuQr1c718xYetkRnvYdytP9Wbi5aP1BLg_rTuccm6_FJuJHpVxfElc4pyLMz5TDZWiJpWrdko2n3XATCgwhZ3pqSMiA0w1d4lPqzlwd7Fnk-ff2e6OCFp03MhVai3L0xNgO_anoGSx0bTAo4AKWQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02ea84be9b.mp4?token=d32EhD5nbgv9y9YSBERqp-8Q4X5omjZTf6csE1Vkws9IBfe6hv5eKbm96UA_rI1rg_rNZtElq5O04cNvX3mlXrITL-JkHWAb1sBMvtdQOZaZr2gzVNy1C9odwdEWO_-I2RPUTAMGdmgMEU3PvVVsfUse-LmEouMrU2KQmC01rTGNc2MyQxtM5sOinohQ7IVwKtuQr1c718xYetkRnvYdytP9Wbi5aP1BLg_rTuccm6_FJuJHpVxfElc4pyLMz5TDZWiJpWrdko2n3XATCgwhZ3pqSMiA0w1d4lPqzlwd7Fnk-ff2e6OCFp03MhVai3L0xNgO_anoGSx0bTAo4AKWQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شارژ ماهانه گران‌ترین پنت‌هاوس‌های منطقه یک تهران چقدر است؟
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/664477" target="_blank">📅 10:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664476">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teyzJgIbE6Mo4QWrY6_fwuEhRYmVe_n0fR-lxiDB6pAg6NRhxf8hjmI4qnW8QHHQYt7R12NEs9XoKjbHBSCjapHz88S7nCyUzLDad5S-DtxouzlX8OjXN9ktQpfn6DQnRPMkH8iPneP2MK6RHvdfdyiY3S10oDS4tU9gnI5ohHRu5-b9Q6X7BGR_bzPwVlzS3tzQp378cgDPXTJ0zEKugsmHh8q3l_iV-YeKkJ1c9sG8jmf4HTyMYjgQbWblcTH7fdbhAjlCWx2YJZQaUyJZlP2wFPEP6hTkwPKzD0--Q8kTvLwDoBcQx5NK3rJPZqBmU_NpekaGa6uXF4vICx4DxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری دردناک از تشییع شهدای لبنانی جنایات اسرائیل در الدویر، جنوب شهر نبطیه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/664476" target="_blank">📅 10:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664472">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
بیمه اربعین ۱۴۰۵ در یک نگاه
🔹
هزینه ثبت‌نام:
۲۰۰ هزار تومان برای هر زائر
🔹
سقف پوشش‌های بیمه‌ای:
🔹
درمان سرپایی:
۳۰ میلیون تومان
🔹
جراحی و بستری: ۲۵۰ میلیون تومان
🔹
فوت عادی: ۵۰۰ میلیون تومان
🔹
فوت ناشی از حادثه: ۲ میلیارد تومان (شامل ۵۰۰ میلیون تومان فوت عادی + ۱.۵ میلیارد تومان غرامت حادثه)
🔹
ثبت‌نام در سامانه سماح با پرداخت ۲۰۰ هزار تومان، این پوشش‌های بیمه‌ای را برای زائران اربعین فراهم می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/664472" target="_blank">📅 10:38 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664471">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgkUN-DzjgsIpxynNlKpa6eO_woSdRS-TJItKszMvxzKwrh6FRDgoFttS-ZkpB6DWDqqWEja9q1ndgmTREYrCS_oh8TDe_8lRSrjZ1ipbpbLzvM2k-k-goDWvBXmyT6PhnzRd92RiFjiTI9hMRvib7nQ6y6pChSBQI1_XOGOfMYbNXF1Vd1-9uYjJmXhNaLKGYUSeh5ylceuA3Apa7bQVBWhoJQFqTuZ86r32xrgd3sqZp4BV3dSsM3V75q7WEhTEkXAele8mruFz-sv6bdXtvR-m9IoiWaRen36l9QFy4gu3Qg254rTjcPc46L8hmRfTO4lcbQglA8aUKd8Kzj1KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خاموش کن؛ زندگی روشن‌تر می‌شود
🔹
گاهی یک تصمیم کوچک، می‌تواند آغاز یک تغییر بزرگ باشد.
#مدیریت_مصرف
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/664471" target="_blank">📅 10:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664469">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOft3QjjC_PNsOnDVi3DQx8PkU6IiRRwtw1lTrUEf85PpHCnqEZx1yW-87f2J7szHJV33Uf0TsJPUL0cufPFDYBAl4hw52Q1MvnKf6zGw-ZzezUpUznlYOftaj-m_OoZpypjRIWXFeEzsL8u5eatBLbAEu9yaa4sP8MSQr5WRXuL5GQYV_uraJtRkRBRm69xAVNVf-QnSzRMgQHEHrYgBy7NaEh1BdtyaCOXkV5gcO98hoq3nWsOIO-kamtFgWsKklQLXsIyR_rcPsa58V3RGtP4Rbrp7hxdRUlLEHk_aY6rb8y3kl1wSjJkFxhOQfTD83awtDgiPpFgqqXtNKxCeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e05be977c.mp4?token=gCiSTE61ycRGKEQQtgqsYZMaf5fOEv9Jom4Gt7xqAkHOINglSzBHXxL-T9uTR8mEWFrc96jiQsAjIMBQ3DrqDqIsI19ytjLO7kyVvl-v-9ngLlfgFKy7ROESDFYiGFgYqEGeSgi6nNJJW7hQyMCfoSQm0ePRNmmcHdGjPcq-fjtp6KmIlqowO-EZvGPxIJD8OU-KjwiNKUKCgWaG7bzIWAXPDxa7o1EqBA9_gIjtxDM4pNl111fdYNxBDs2Wo2XznUQ-C4DPZ2zatuKnFle1wF01o1gewM1N0eY0oznxZQV_MmDx0LveAqKZefLUY1OC3nhdvQcuOiPU4S5LdoSP-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e05be977c.mp4?token=gCiSTE61ycRGKEQQtgqsYZMaf5fOEv9Jom4Gt7xqAkHOINglSzBHXxL-T9uTR8mEWFrc96jiQsAjIMBQ3DrqDqIsI19ytjLO7kyVvl-v-9ngLlfgFKy7ROESDFYiGFgYqEGeSgi6nNJJW7hQyMCfoSQm0ePRNmmcHdGjPcq-fjtp6KmIlqowO-EZvGPxIJD8OU-KjwiNKUKCgWaG7bzIWAXPDxa7o1EqBA9_gIjtxDM4pNl111fdYNxBDs2Wo2XznUQ-C4DPZ2zatuKnFle1wF01o1gewM1N0eY0oznxZQV_MmDx0LveAqKZefLUY1OC3nhdvQcuOiPU4S5LdoSP-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی کل پولت خرج پیامک بازی میشه
😁
🔹
در بازی دیشب کلمبیا مقابل پرتغال، یکی از هوادارای کلمبیا که کل پس‌اندازش رو خرج کرده بود تا بازی‌ رو از نزدیک ببینه، به‌ جای تماشای مسابقه، تمام وقتش رو صرف جواب دادن به پیام‌های دوست‌دخترِش کرد و بازی واسش زهرمار شد
😂
🔹
پیام‌های دختر: تو فوتبالو به من ترجیح دادی. «می‌خوای ولَم کنی؟» «اینه؟» «نمی‌دونی چطور انجامش بدی و می‌خوای من بگم؟» «اینجوریه؟» «بگو دیگه».
🔹
پیام‌های پسر: «زنگ زدم بهت که بگم دوستت دارم در حالی که تو چشمات نگاه می‌کنم» «خب جوابت رو دیگه می‌دونی» «ازت خواستم که بمونی بازی رو با من تماشا کنی پس...»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/664469" target="_blank">📅 10:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664468">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed7df23a12.mp4?token=oEM8fP0huRuBzdazhl7GpZjlt1Er136n8JKCqVGKOJaAm_piPu-MvpJSK-nHqbrATev_yjOAPMENug0PitLKvrozNa6lv5hZ4OkTnl5Tt9u7cdOmhgJ3c-qVsikeARBGnwHf4Kn124Z-1TWeiOVzgacGVGYBpYstikKOjHpodKwC0_601GHG3DYIdcSPpHUdgDkD2iMc0UXJg2uhiSZFULo_OetLHDPLiiHO9YezfuiBX30lKEfNC6qqZu-1j50379v4Wh9KhTyQkL12fFChITZJpD5QI4wvIR4QHbygAggxy6ennrZb97LCW1_SYIrNj-q3v_QkQ7wOMkpvwcUmxIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed7df23a12.mp4?token=oEM8fP0huRuBzdazhl7GpZjlt1Er136n8JKCqVGKOJaAm_piPu-MvpJSK-nHqbrATev_yjOAPMENug0PitLKvrozNa6lv5hZ4OkTnl5Tt9u7cdOmhgJ3c-qVsikeARBGnwHf4Kn124Z-1TWeiOVzgacGVGYBpYstikKOjHpodKwC0_601GHG3DYIdcSPpHUdgDkD2iMc0UXJg2uhiSZFULo_OetLHDPLiiHO9YezfuiBX30lKEfNC6qqZu-1j50379v4Wh9KhTyQkL12fFChITZJpD5QI4wvIR4QHbygAggxy6ennrZb97LCW1_SYIrNj-q3v_QkQ7wOMkpvwcUmxIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه رانش عجیب زمین در هند
اخبار هند را از اینجا دنبال کنید
👇
@AkhbareFori_HI</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/664468" target="_blank">📅 10:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664467">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">آیین نامه سوگواره بدرقه یار.pdf</div>
  <div class="tg-doc-extra">260.6 KB</div>
</div>
<a href="https://t.me/akhbarefori/664467" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔹
آغاز ثبت‌نام و ارسال آثار به سوگواره رسانه‌ای «بدرقه یار»
ثبت‌نام و ارسال آثار به سوگواره رسانه‌ای بین‌المللی «بدرقه یار» آغاز شد. این رویداد با هدف ثبت، بازنمایی و ماندگارسازی روایت‌های رسانه‌ای و هنری از مراسم تشییع رهبر شهید انقلاب اسلامی برگزار می‌شود و پذیرای آثار فعالان رسانه‌ای و هنرمندان از داخل و خارج از کشور است.
علاقه‌مندان می‌توانند پس از مطالعه آیین‌نامه، از طریق لینک زیر نسبت به ثبت و ارسال آثار خود در بخش‌های مختلف سوگواره اقدام کنند. همچنین در صورت عدم امکان ثبت از طریق سامانه، امکان ارسال آثار از طریق شناسه رسمی دبیرخانه نیز فراهم است.
#بدرقه_یار
🔹
لینک ثبت آثار:
https://survey.porsline.ir/s/aU5VZuaW
🔹
شناسه دبیرخانه:
@Badraghe_yar
@Badragheyar</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/664467" target="_blank">📅 10:07 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664466">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxpab5NQTa2KI7gZT0rpIGd4MGA-r-3xG2ueXUZy5SxJkAiRLKmZMmqL7HDl3MQXi7iG-9aN_4AI6T5NdUfSQNfFyuGhugM4Vyo0zZADTS3ji-XxBCtIU_GlebwhYjSX_DMm-k3UoU6eCy8jq2-qYI117hvq3VwNagklG_qDkKsuofWaSH0rgCngM64B0XpYvnoe_8FkJHny3TAaMoWBRCL1Uaczss31SV2WTDawdOEM1MCHqiVGtyaCAuwND73sozmvJtimrmaSAr0lGRKgc_za_UQu-L2sKJg6QjpEcArwsbn0xsR_baW_ZK1mHDgi60BdJQx1A-FP4SLrQJ76Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اگر فقط ۲۰ روز افکار منفیتون رو بنویسید، چه اتفاقی برای مغزتون می‌افته؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/664466" target="_blank">📅 10:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664465">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc4e45b02.mp4?token=uFHhHGRX_2Jby2-sJQwlpN35Js9Bdyt4Tdprx81hrsrXOCciTF-lW3KSl2rzXrpTq_frmDqbt5eQ3goS3P0D00vBGWH9YgLZmPPMv2wsPAeIylHQPIT43z4FCxdB7SYEDmAMMezBH0p5jgezF58u0Q5wWeYVVKe42WaS8GtA4F7UX6Zo8Cz5k2KG5GtNYg6vE1D5P3rqGS0AMbQF_hWBtY-nAh0X0sHb5qQglYroXFNpwqZHM5hFGcLnbFJ6CBS9OestYh6DO1Jb7kvp8pXEr34AW_-JBnwkY8ym6y8gYc1dN91OzcdOEaWFt35GuVHZSzgvXjMokO4onKQthdvdaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc4e45b02.mp4?token=uFHhHGRX_2Jby2-sJQwlpN35Js9Bdyt4Tdprx81hrsrXOCciTF-lW3KSl2rzXrpTq_frmDqbt5eQ3goS3P0D00vBGWH9YgLZmPPMv2wsPAeIylHQPIT43z4FCxdB7SYEDmAMMezBH0p5jgezF58u0Q5wWeYVVKe42WaS8GtA4F7UX6Zo8Cz5k2KG5GtNYg6vE1D5P3rqGS0AMbQF_hWBtY-nAh0X0sHb5qQglYroXFNpwqZHM5hFGcLnbFJ6CBS9OestYh6DO1Jb7kvp8pXEr34AW_-JBnwkY8ym6y8gYc1dN91OzcdOEaWFt35GuVHZSzgvXjMokO4onKQthdvdaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری و کمدین مشهور، استاندارد دوگانه غرب در برخورد با تیم‌ ملی ایران را زیر سؤال برد!
ترِوِر نوآ:
🔹
عجیب است؛ بعضی تیم‌ها فقط درباره فوتبال سؤال می‌شوند، اما از بعضی تیم‌های دیگر می‌خواهند درباره تمام اتفاقات دنیا توضیح بدهند. درود به تیم ایران که مجبور است این بار سنگین را به دوش بکشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/664465" target="_blank">📅 10:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664464">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZYGKF5vFfCg80k0EBmSuzOxg7RqqDk7fK4veUFKYXDkEGnWbhJHHbeaP-Fz4KBIrOiYZ7zvtt1NvnnqKmRk6pKkJVpr6WW8WVARPqfdLMJTTWrELin4cK1AN0ujxwUwtiP38wYdP5oE9ejikHOcZICefQ1Iwy1MZMu-2TcXHnyQ5TulK_pA98qXfrKF-NPYb88zXgE0kQ_iiCBmsH4QKh4Bl8vGX8IjwpI2QhwdB8CqyTm3yt7IOuoiPcQ36yXBS6BbGl-wRemX-7e_mlvpthr2NcD9CZ9pcz8IuQGL9NRF52dzuVu6QobadsJ8OsyAb88hZh3AGcuY5-D-krklgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اخبار توافق و مذاکره را چطور بخوانیم که فریب پروپاگاندا را نخوریم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/664464" target="_blank">📅 09:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664463">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33605d2c04.mp4?token=cpuTJZzUx0NAPIeQ5vtaMu930xYijnIF1HaeBE8W4h6chyG7wIyNnE7zkcbXTo7Jk9KakXhXN3j7XtdoxQS4nN8ynoP1ADTMiUO6wUvfIGB9Gd1yBHOW6R2vjwI1VGCO1OeL0c2lrMcmyXVgJ7LO9K24p4bJHZ5_pOSLRt-zC2nNnpdxeHXXd1B15OUsePKgn5UqsA_u3tZNhn7RdKSej31-eT04-bMgLUtqIWz4wpwa-HQlS_oGuOHESn6f0Eq-FtFJO0celfgp7rX6jSStzJ74M_X7YM5-0d-EdXVuN7neatu_gAWU2hVvfzHCBQVtr3HE4Q7n4222wnVUvEbLhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33605d2c04.mp4?token=cpuTJZzUx0NAPIeQ5vtaMu930xYijnIF1HaeBE8W4h6chyG7wIyNnE7zkcbXTo7Jk9KakXhXN3j7XtdoxQS4nN8ynoP1ADTMiUO6wUvfIGB9Gd1yBHOW6R2vjwI1VGCO1OeL0c2lrMcmyXVgJ7LO9K24p4bJHZ5_pOSLRt-zC2nNnpdxeHXXd1B15OUsePKgn5UqsA_u3tZNhn7RdKSej31-eT04-bMgLUtqIWz4wpwa-HQlS_oGuOHESn6f0Eq-FtFJO0celfgp7rX6jSStzJ74M_X7YM5-0d-EdXVuN7neatu_gAWU2hVvfzHCBQVtr3HE4Q7n4222wnVUvEbLhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خسروپناه: خانواده نمی‌توانند از قاتل امام مسلمین گذشت کنند
🔹
قتل امام مسلمین، طبق ادله‌ای که در جای خود بحث و اثبات شده، حکم قصاص دارد.
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/664463" target="_blank">📅 09:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664461">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qwtRko5wAVTz5SrL4yfYP6kD-OYOcIp2WiAKgsyajdupKJcRIIzNV6ti__CLCtNQQzglRCd5x1f9m20JhW8j2h5-AR19JwgkBEKaQkS0jubA-Wt1kFWNovAzCvj1lppExwpPWpd4_DFbzASLpDJPb455ySsdJmfBIIUq3t7id62f5LoovCa5WcYOR5kEExt_q2cYFnooxTwVCk1XzyDSYSlzc6XcaY7JorLjzO6dHhAPQcnSEPohpOx9CiYZUWJimIGrlnRneVA0BUoVUHgkQLmtufar4V9nN4JhzrkMfM-lu-0Jb245twVXtIwVT8KI9wanoNlxpZam5h0TCQZjjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hg5Uf_IN6D2VCtJI96vELZDFz1oAHRTuoX2bDGowFfqSFKu6xaTaQ13XipbCsqhUZk-wi3UbhKHQOiIaK6fb_l7sSb0-vTXr-GUgcO1yvQ9g4odzchAoHLAWTmh3I3bE8-MMV0fAcd3cMjOqxCK_25gjWob4364qfMxTVk0d2SkL6WPebvYwH-jPj27am1cKo-YhNUYLbmsh1oTnqgKzN64uXzMQR5_AepIyDf0P6IwvFJGyIv6kPtt7F3lT7qdavhT04U305ZyciG4zgx7YqxPKvNFPuWsob1531oG7kPiD90misbgLBMqO12jIMFvWQpkFWJbmOhve0-EIkI-vEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
علیرضا بیرانوند: شرمنده‌ایم که رویای صعود را محقق نکردیم؛ اگر ثانیه‌ای حالتان را خوب کرده‌ایم به خودمان می‌بالیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/664461" target="_blank">📅 09:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664460">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/769989de98.mp4?token=iwJnAE7CXxbAnzW-QIAcjk8r085x_uuDx6O0qdMEfP9EjAv5nqujJcc_n38tDNP-cVzG5tt75naVw3o4rkxCbjV7WH4L_DHt1ZQgq4-wxQ4gJl1n9ezjSxklVPKxDLo8t-OYXJGHGizcf_wkgsu8IaXb9gRoyjo59vMLcwClfhEF6IiLge7hyRwMP0Iz8HDvUfTvsusrsgHnMBfJ39nbuJoWGFRIiWZ2w5j4X4WJC4ZWCeEx0UBC2_ot3NlbCOcfXDYfsLzqnuu_G_5X-6TO6aTqeCF8Ux5DmkmnCK4Fh92s44P9V3WSAkITxaqUBrZR4hmNINvR_RC3BfW_4dpoDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/769989de98.mp4?token=iwJnAE7CXxbAnzW-QIAcjk8r085x_uuDx6O0qdMEfP9EjAv5nqujJcc_n38tDNP-cVzG5tt75naVw3o4rkxCbjV7WH4L_DHt1ZQgq4-wxQ4gJl1n9ezjSxklVPKxDLo8t-OYXJGHGizcf_wkgsu8IaXb9gRoyjo59vMLcwClfhEF6IiLge7hyRwMP0Iz8HDvUfTvsusrsgHnMBfJ39nbuJoWGFRIiWZ2w5j4X4WJC4ZWCeEx0UBC2_ot3NlbCOcfXDYfsLzqnuu_G_5X-6TO6aTqeCF8Ux5DmkmnCK4Fh92s44P9V3WSAkITxaqUBrZR4hmNINvR_RC3BfW_4dpoDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کدام مدل گوشی سامسونگ ارزش خرید بیشتری دارد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/664460" target="_blank">📅 09:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664458">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvoAA3M2wrPlY1_fpTlAPdAHg4CV9p6XBG2RFo08Sq_RCBpJtSyLfJ3K9C0V8ufwnQQ_gDhQksH3Pgu2bg1HCzjVhVD8uTAxGXhsgfncPnfidL2AJWa4r7NCuPTfqIzL9cOL40SRyFZj4RV8_5L3UVQMWhaMP__aKjKzMN3WCzgu0rNclJZ-EODmKkBGJxI5UiY0Hlx4I0BJMpba8PMyJCqFiqrjaJYvXlcA11u9DP97rqEKDo2Nb6G9u91V2aT6Mq3YnNRbZxy6hJZGTxiAsFm-lxsoXvPFHF21gizoAzm79tLi6km-necNKK9SFyaqChCAT8V-6FZMin332_9Wxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آتشکده ساسانی زیر و رو شد
یک کنشگر میراث فرهنگی:
🔹
چهارتاقی یا همان آتشکده ساسانی «رُهنی» در فراشبند مورد تعرض پیاپی تاراجگران اموال تاریخی قرار گرفته و ساختار آن به هم ریخته شده است.
🔹
کندوکاوهای غیرمجاز قاچاقچیان درون عرصه آتشکده ساسانی بی‌شمار است و بیانگر نبود نظارت مسئولان مربوطه است/ ایسنا
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/664458" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664457">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8bb3f50a0.mp4?token=dQax8haSP9ui3rHlP_wR5geJVVErTYXnMExJQn7H1Etob-PLSR1xcMxQarK-xErC0_LQgraOgx3TZFifSCt4PowFPNXJYp5tfn8JKTRpYLDp5X8swILPhtryUhJBIdLlgRoGWbzV1_WDXk-AXmgIRUW8gYQ3HiqWLzZ5-V4ZCbKSiy8iQYoK6yCKPWe-pLj-LFvdJv0pDC9D1KstfDRCB_4n4JPriB2RJ7JSAJHu4DduVaMnZPqM7mfHkxgVk8fpA8HNwtdSIFQTeeImq5mvwULm-_b88l4viZ_jttwBbz-mc6jQYrLUhTsd0tQrRVVrCjzf9dfn2ANIAN8jxpDuMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8bb3f50a0.mp4?token=dQax8haSP9ui3rHlP_wR5geJVVErTYXnMExJQn7H1Etob-PLSR1xcMxQarK-xErC0_LQgraOgx3TZFifSCt4PowFPNXJYp5tfn8JKTRpYLDp5X8swILPhtryUhJBIdLlgRoGWbzV1_WDXk-AXmgIRUW8gYQ3HiqWLzZ5-V4ZCbKSiy8iQYoK6yCKPWe-pLj-LFvdJv0pDC9D1KstfDRCB_4n4JPriB2RJ7JSAJHu4DduVaMnZPqM7mfHkxgVk8fpA8HNwtdSIFQTeeImq5mvwULm-_b88l4viZ_jttwBbz-mc6jQYrLUhTsd0tQrRVVrCjzf9dfn2ANIAN8jxpDuMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هوادار یا جادوگر!؟
🤨
هوادار عجیب غنا در جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/664457" target="_blank">📅 09:25 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664456">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
تکلیف کارگران بخش خصوصی در تعطیلات مراسم رهبر شهید
وزارت تعاون، کار و رفاه اجتماعی:
🔹
در صورت اعلام رسمی تعطیلی از سوی مراجع ذیصلاح، این تعطیلات مطابق ماده ۶۳ قانون کار شامل کارگران بخش خصوصی نیز می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/664456" target="_blank">📅 09:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664455">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f18d83442.mp4?token=rQO3myvllcFPS7eTeDUT5nYLpyrNu5v69mhgtljCqc6KORbjRfXNlkxms_ojtYHQAHliopeD5iY5sFIaod1Izae8W0gixaNos9-5h2Z3heRVq4MPs3004HZGvvii8usEtRnTrDdWoUXifH8kN03Jma81YTjdCuHcBrVPQbWL_fQ3cf0U069Q7bNDd2ADdstQLkvwoRQkUNbTblyj9lYvQ1SeGYIxtzgN6snPIQWxvupk2YBhAGrcfifEkxYpiWH9vI0VBaA-ig6Di8Dtfgds4-fcFaqH9jUHGEFPBQ6B8ic68CK-RVE_ixf7sh9zoK7ZSqND64VPojp-eKmT-NDnTRrfKSu6gjmPKVlarc0euvL0-QsmLjsKhcS7cYGLoWftLdA4RUdc-AHhrlqk7XzCkbbV7u87sAxUZgkejO2yrpzpHwK9mt3c-F7riKgMpjER-jbR9Wq8qu2W0tGUf3BJDQu7BQ_e_QT-sm2-wGII2_Ef6F-_F1PJjBiMo8gT_TR3GyOPWgnufaPpMXaKudbmslpez4NST2BxleR4Hl2CAU_R2vbFB-JC_-oJLefh70eCMw3cZkQOC_LAXZlDuBtQ8QPYzkh2EkmdLC0xpCe_c5Qrn3PTFTv6fpejqCSRxV2egU_e6xb_RUJsbM8oJRCF03Gl5rPOng_dEu6IGMTvBkc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f18d83442.mp4?token=rQO3myvllcFPS7eTeDUT5nYLpyrNu5v69mhgtljCqc6KORbjRfXNlkxms_ojtYHQAHliopeD5iY5sFIaod1Izae8W0gixaNos9-5h2Z3heRVq4MPs3004HZGvvii8usEtRnTrDdWoUXifH8kN03Jma81YTjdCuHcBrVPQbWL_fQ3cf0U069Q7bNDd2ADdstQLkvwoRQkUNbTblyj9lYvQ1SeGYIxtzgN6snPIQWxvupk2YBhAGrcfifEkxYpiWH9vI0VBaA-ig6Di8Dtfgds4-fcFaqH9jUHGEFPBQ6B8ic68CK-RVE_ixf7sh9zoK7ZSqND64VPojp-eKmT-NDnTRrfKSu6gjmPKVlarc0euvL0-QsmLjsKhcS7cYGLoWftLdA4RUdc-AHhrlqk7XzCkbbV7u87sAxUZgkejO2yrpzpHwK9mt3c-F7riKgMpjER-jbR9Wq8qu2W0tGUf3BJDQu7BQ_e_QT-sm2-wGII2_Ef6F-_F1PJjBiMo8gT_TR3GyOPWgnufaPpMXaKudbmslpez4NST2BxleR4Hl2CAU_R2vbFB-JC_-oJLefh70eCMw3cZkQOC_LAXZlDuBtQ8QPYzkh2EkmdLC0xpCe_c5Qrn3PTFTv6fpejqCSRxV2egU_e6xb_RUJsbM8oJRCF03Gl5rPOng_dEu6IGMTvBkc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش زدن نمادین متن تفاهم‌نامه توسط یک مداح
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/664455" target="_blank">📅 09:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664454">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crxqJGKgmP4SpzIY-juEp8Rai7lbxK0CFaZyYUNXL3Gxi4ntFLct672c-uVzwFEZ14zDBaQCKbEbdecVRi4Z_Nt0Hz9AkVUQ1Awc1oHzXFCU8N4CCTr9T0wx0gUNJnV7tsOuWYsKKqjLiTAEpBHglR5N7rkosVDLUWkd1koZNaUaAGN8R-JPbwEvChkEdBnNmAyKno3QIAGavpabpkVVfFO7beRWoiIeCLQgPIlM96PLgklSOhuF2_dm8gR1io9pJl3IYbnGy8ejA3pHEfe7PXAz2UUZklQnqiCWXqy3orvOuOeUiBlXTaTfww-XnHVCYzTZUuQS1uhnPSc3qdocjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
لیونل مسی به اولین بازیکن تاریخ جام جهانی تبدیل شد که در هفت بازی متوالی گلزنی می‌کند
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/664454" target="_blank">📅 09:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664453">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
۱۰۰۰ مدرسه تهران آماده اسکان زائران رهبر شهید  وزارت آموزش‌وپرورش:
🔹
بیش از هزار مدرسه در تهران برای اسکان زائران آماده شده است.
🔹
زائران بر اساس تقسیم‌بندی ستاد برگزاری مراسم به مراکز اسکان هدایت می‌شوند. #بدرقه_یار   #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/664453" target="_blank">📅 09:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664452">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8430e98b39.mp4?token=dcW5LO7bth-iddqP7JVp3Ga9VMdcUMXDYw6ikosQOKDwJ-xSn4JqJUVNj4ACD60PSEvWIaTdNo_ZyzwVh0ZQ5pj1dg_Ee2K6bjGqcFKy8AOFSMuimDATEpwAD5E59BAaDWuFr2vFJpQT1u0OVmQ6T37CUJjXi-OY0QV4IK_tqKvmQqxvE8bOtBogHeTVY0psXTe2g8P5dEWShzgRhaEgCKtwADa1N0bASsKL1u2qMkoloLvsC_7QdkKUq-8XKuQY4QPzRXfFai--i5tapcum2PJluN5g-iOFVbcWLu7yJMqBbTUVyBZ5-tzOy21xYeaMoM8-YiNouD49IlpHjucLZ4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8430e98b39.mp4?token=dcW5LO7bth-iddqP7JVp3Ga9VMdcUMXDYw6ikosQOKDwJ-xSn4JqJUVNj4ACD60PSEvWIaTdNo_ZyzwVh0ZQ5pj1dg_Ee2K6bjGqcFKy8AOFSMuimDATEpwAD5E59BAaDWuFr2vFJpQT1u0OVmQ6T37CUJjXi-OY0QV4IK_tqKvmQqxvE8bOtBogHeTVY0psXTe2g8P5dEWShzgRhaEgCKtwADa1N0bASsKL1u2qMkoloLvsC_7QdkKUq-8XKuQY4QPzRXfFai--i5tapcum2PJluN5g-iOFVbcWLu7yJMqBbTUVyBZ5-tzOy21xYeaMoM8-YiNouD49IlpHjucLZ4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راز مهندسی چرخ‌های قطار؛ چرا مهندسان آن‌ها را کاملاً استوانه‌ای نمی‌سازند؟
🚂
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/664452" target="_blank">📅 08:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664451">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1q0PVs6HHqwlv__nb9MIjGacWui9c1syWk4Gk3RkPHED_n2XmrBEfS7AgQIafFXV6wWkAFZFtOoStE8n7KYHOI27lCSt8girwU6MT7J6iglr30CZ3O2T2yeu9liPqoj6WdJoADsVz58feidxq_7ZuhSFsulMmbwVTREXhccBZIbTClLP0DBXUh9po578LZGw7Im8UxWOY3drZe7plLceFPdGqgT1gcV9Xl_KPXRtso7Mc1RgF-G-cBC3D0rWSedueeaeAeJ1ovvfRp0nmJ0EBasHMM1_q1-YaQfgh30SiRO3akHJF9c0rGWFl3w0amSndcaVolfSA9w5WdTcIkWNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه پهنه‌بندی استان‌های کشور در مناطق ۲۲ گانه و مبادی ورودی تهران برای میزبانی از زائران مراسم تشییع رهبر شهید
🔹
بر اساس این پهنه‌بندی، زائران هر استان پس از ورود از مبادی تعیین‌شده، به منطقه اختصاص‌یافته هدایت خواهند شد تا فرآیند اسکان، راهنمایی و ارائه خدمات با نظم، سرعت و هماهنگی بیشتری انجام شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/664451" target="_blank">📅 08:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664450">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uq9ObgmKnxah4vxtKN0jMswysSiWF4wweSDAnToQc5nfXfG1WlcjNUwgd7kKokoxHOJDJAdvB6ETyiZYl4P2L-HfVbpmAx4qj7IZh-SDUvHkwxy5Jg4Rm9Dni3f_7nxf2PKTqoNMgk6vaB3-UmIHJg4aD6wKBw3iGerlmqBp_qtcL1l2-0d1c8NbtCNjt_U-7KysBRuXtWTBq7ChXmlHgrtuR34dvPPgWdjrSE-6nz2BgQDSmJ3VUVDKnNDMkzSALW5yhSWZ8OZ95hW295JlwL9okLeg_rt93343jN6APIlRyEmY4nQPqFog2hehAc1PKHdzTV1hfRRkmoSopLzKCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قول روشن، سرزمین خاموش
🔹
وعده بود اما تاریکی ماند #برق_مردم_کجاست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/664450" target="_blank">📅 08:46 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
