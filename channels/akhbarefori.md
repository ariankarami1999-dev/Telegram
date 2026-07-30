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
<img src="https://cdn4.telesco.pe/file/hkrjOUuyViZ1jjCuqIc5TQOzPN2GPYLfNrJcxx3WrsjQ6BUhD-liLfk7oKMaTa7UT4PFsaTSDkP1VwKdpuJeZUXITLCuOy6OUskod1Aj8PxSJZbXhQDxi8AzkM4b6CCvop4PhEmAoMaX6RG-usuhJFJHzTr2VO8eU3SYr794TUtkLLr75ub0se212NSQkwsBmU5UBljNcRDXs3OcAp3khcL_gII6deVcw1vaK69EmXV9kBucpevIIm2nJQbZxJndjdo1kIKc8uN8obIQV1vf4dfMnlo4q39LeXGZ2I44xv7DEtIxHj_GbG92M6b23t19xyouISdl7NlZQFLDKElZJQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.15M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 13:28:27</div>
<hr>

<div class="tg-post" id="msg-676634">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iucTGjxtHPGljVRtfXty4RBVXKJjO41fYv_iRJ3mGIBIdqP3IjM6dZPoIEPzqgNqk0nO5d7oniOycPVxBt_czGlQKVrqTX6Dbyc7xZYExzrvf7PJ7VU8ga3SHZkVJ_-iA8xfoYggKcL-S7xi3cVlqE8oRzqVvI8Z5vRCSOj6ln6BlOImMYLb6ncKfGwaRlaHoX3MkWb67YFElEbRdD7PTYyBBtJV2trjfMnvZqZezwDdRDkqr4CBxktC3iTzpLTDTImGTKefczwNu_jORProZkFE-1Jm6i4KxZlG_GaolWBL2SBc35dWyUNntcDiKiQiwfCIKB5X2KH3acSMbfi43A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت روز طلا در ۸ مرداد ماه
🔹
بازار طلای امروز نیز همچنان با کمی افزایش در سکه تمام بهار آزادی و و ربع سکه مواجه شد.
🔹
قیمت‌های اعلام‌شده از اپلیکیشن میلی، به‌عنوان مرجع قیمت معاملاتی طلا استخراج شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/akhbarefori/676634" target="_blank">📅 13:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676633">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
پکن شایعات ارسال سلاح به ایران را بی‌اساس خواند
🔹
وزارت امور خارجه چین، گزارش‌های منتشرشده درباره ارسال تسلیحات به ایران را «نادرست و بی‌اساس» خواند و تأکید کرد که پکن همواره نقشی سازنده در کاهش تنش‌ها ایفا کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/akhbarefori/676633" target="_blank">📅 13:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676632">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFSHhB2FC-TvdlDBOVRVjzBfXC89E1GEBbRwrKNiuSip1vTEhKMhVjpjW6DGkqYQpdPNnqQXFvi_tyOCYHxyV41MBKIvdX5VLyYBfYpobz6mSuQaS6NLbufeNhpX_i9RjR2JDoMYbigDw1APEQRUxsxtTDbzBhEbmwRbV0DFx3xX8M1EFXpOtaUC7O8RDVAxzE9rPv_7Kb28WaqnuBWNzx91z-sF0YD20P9uZGe2yZhdwovIfzl6YA8jYy60vjYhVQrrXBJnx-x82Nb9SDgPz5upsKv6QavhUcOJCtZ1x3b4XnmEgi8mjrnH3fB1KndX8Oy34zXojt4WYE3dgrZZ3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با پول پژو ۲۰۷ در ایران، در کانادا سوبارو BRZ اسپرت می‌توان خرید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/akhbarefori/676632" target="_blank">📅 13:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676631">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
بازداشت راننده آمبولانس در اسرائیل به ظن جاسوسی
روزنامه «یدیعوت آحارونوت»:
🔹
یک راننده آمبولانس اسرائیلی به اتهام جاسوسی و انجام مأموریت‌های جمع‌آوری اطلاعات برای ایران دستگیر شد.
🔹
این فرد ۳۴ ساله از دسترسی خود به بیمارستان‌ها برای جمع‌آوری اطلاعات و عکاسی از مکان‌های حساس استفاده کرد.
🔹
گفته می‌شود که او از یک «چهره ارشد اسرائیلی» که در حال بازدید از یک مرکز درمانی شمال اسرائیل بود، عکس گرفته است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/akhbarefori/676631" target="_blank">📅 13:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676629">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
بغداد: هیچ مدرکی درباره انجام حملات به عربستان از خاک عراق وجود ندارد.
🔹
مقاومت عراق: گزینه‌های انتقام از متجاوزان آمریکایی-سعودی روی میز است.
🔹
با اعلام AFC؛ عربستان میزبان دورهای نهایی لیگ نخبگان آسیا برای ۳ دوره بعد خواهد بود!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/akhbarefori/676629" target="_blank">📅 13:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676628">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ds5g0OhaBany9ntXKmvc-tRLRcCUGjoAWWehXPMHYKvOMZ-bWDZEYIg4Zp646MOQsjSgOejy9RfhbdMz1Asw-AItev01g1BKzYWAomXkzHPmCxEbe7oZJxG6Eg5O3-nI-b4-07RkW9-hObPDQdho11baNiGcnUb8XFlyrhpMyZMfPjoJhl18MhO-SQomz6qiDEzLxbpVWIQ3gaeWHeVpuMj6m-x14Mg6QaXwNEbFq4ugpMft-6hcOvF8LMDn80W2-mzCnsx4W8C-zotY9ba-cW4zraxVVw_5TseDAsZKunD2JBz6lNQRWdrpK-u1Fhrvo3RKmsaZKmIJ60_Yqyq1Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برای سلامت بدن خود این نقاط را روی پا فشار دهید
🦶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/676628" target="_blank">📅 13:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676627">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c6af8976a.mp4?token=gzt5sLi9QTk8GM7uTroem77mvOw0_5j7qy7eVlVjg6BZeSly3jH7-tQFGIt8etjHM5m2dDUXVz9HJxITFXSPHbLqniRhIPX5pD8Jqg7sU_kmCJWUXLKqfY5ZWeuWfK-i3_IAEmvyEbOfizBh77mg_ewY43eR-54PfNF3erjsMXzqzgZc9n14vBR7Lp0kwyOFdil_SF8IC61sXb7r7Q-fhQvJYmbHOk1dAUOi_Pk8siAmYgkTcriUUupNATX6DSZRMzZZo0ybBKY_syhTkjZssdHi8WYFgzn-snHSqFP7oW1E11kB3DdhzhOid58p0Sb2TzcG3Gedo7Clxz96hB_CCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c6af8976a.mp4?token=gzt5sLi9QTk8GM7uTroem77mvOw0_5j7qy7eVlVjg6BZeSly3jH7-tQFGIt8etjHM5m2dDUXVz9HJxITFXSPHbLqniRhIPX5pD8Jqg7sU_kmCJWUXLKqfY5ZWeuWfK-i3_IAEmvyEbOfizBh77mg_ewY43eR-54PfNF3erjsMXzqzgZc9n14vBR7Lp0kwyOFdil_SF8IC61sXb7r7Q-fhQvJYmbHOk1dAUOi_Pk8siAmYgkTcriUUupNATX6DSZRMzZZo0ybBKY_syhTkjZssdHi8WYFgzn-snHSqFP7oW1E11kB3DdhzhOid58p0Sb2TzcG3Gedo7Clxz96hB_CCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هدیه پوتین به رهبری در سفر به تهران چه بود؟
/ تلویزیون اینترنتی مدار
🔹
قسمت اول گفتگوی متفاوت "پلاریس" را در لینک زیر ببنید
👇
https://youtu.be/RgUM8McWe-g
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/676627" target="_blank">📅 13:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676626">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b785ba8cdc.mp4?token=M_xEc6GkyNTry65Insg53wOb4_t_QIAYfy72rqPAclmTAflOJb6WVj7ysyVhnGH59nTae_eSCx6JxuIK6L4PvprSG_6FID4WSelF7o4JOj7-k1__IUE3BN2r3mRj3dsE2juUKBq3RdGvtuVygsHCIzqsoiyMSmszDZ6YHAWl1Ui9ShcY3LX9XFK_DICSlCyyjWcu2Jbgv_Ibp-6j0sb-_Y58yNaKGf2bitT4RpjnwvkzocjHC28QHNn_E5J7QAxrgpsWzyJTcMhS14xujOyvooPzAqEyxvWkryJJj8OfpKnn6qMHMoDl6Bpm5agAG9VA4W7XzdQOxpYX205EYqTWZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b785ba8cdc.mp4?token=M_xEc6GkyNTry65Insg53wOb4_t_QIAYfy72rqPAclmTAflOJb6WVj7ysyVhnGH59nTae_eSCx6JxuIK6L4PvprSG_6FID4WSelF7o4JOj7-k1__IUE3BN2r3mRj3dsE2juUKBq3RdGvtuVygsHCIzqsoiyMSmszDZ6YHAWl1Ui9ShcY3LX9XFK_DICSlCyyjWcu2Jbgv_Ibp-6j0sb-_Y58yNaKGf2bitT4RpjnwvkzocjHC28QHNn_E5J7QAxrgpsWzyJTcMhS14xujOyvooPzAqEyxvWkryJJj8OfpKnn6qMHMoDl6Bpm5agAG9VA4W7XzdQOxpYX205EYqTWZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت تلخ و دردناک نخبه و ریاضی‌دان ایرانی در آمریکا؛ پرداخت مالیات به کشوری که مردمم را بمباران می‌کند، بسیار ناراحت کننده است
🔹
شایان اویس، استاد دانشگاه و ریاضی‌دان برجسته ایرانی: برخی از دوستانم به‌خاطر پشتیبانی دولت آمریکا از جنگ مهاجرت کردند؛ من هم به این موضوع چندین بار فکر کرده‌ام!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/676626" target="_blank">📅 13:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676625">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86381f1826.mp4?token=oKk6E37pwFxKGt9vOjzc9cFy8474zYa-0tC3d4lQdyXO7wtqQIzYQoLkThwoNSKAYnSRZ6K96ryICqR1v6ROQMqoN909__jHRjIzHiRxsokyKvIABGV5LJjn6IYEHVYDm4WPXEyAkkztDQsihOIIjcAt2XBYAWpqMq5p0TVdZEfA_aBoXEpJArgheCe-V0YFoDYaZ4AXG5BMliMv6XjvBgm9JIgANLfdZKqR58yZUkY9Gw1lI9OYax8YkDxsv2886-RdmG7FapJrolaUCtCOSdTs7J9edVXELMjgwfPoGwBlCee9dikrEl01hyi_Y2OLVLKgZg8ymMfRZa_787sOVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86381f1826.mp4?token=oKk6E37pwFxKGt9vOjzc9cFy8474zYa-0tC3d4lQdyXO7wtqQIzYQoLkThwoNSKAYnSRZ6K96ryICqR1v6ROQMqoN909__jHRjIzHiRxsokyKvIABGV5LJjn6IYEHVYDm4WPXEyAkkztDQsihOIIjcAt2XBYAWpqMq5p0TVdZEfA_aBoXEpJArgheCe-V0YFoDYaZ4AXG5BMliMv6XjvBgm9JIgANLfdZKqR58yZUkY9Gw1lI9OYax8YkDxsv2886-RdmG7FapJrolaUCtCOSdTs7J9edVXELMjgwfPoGwBlCee9dikrEl01hyi_Y2OLVLKgZg8ymMfRZa_787sOVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرواز زیبای منقار قاشقی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/676625" target="_blank">📅 12:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676624">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63ef1a4574.mp4?token=j24B82P7osvz4JAGUoH7Bx6_8IPSL2wnB_WvGMX3vrg812PDOGZJkCCx3Zfh28Mb3tempfTM9E7d0Cio7BI4zUNbVHcN9ztww1Wfu2Xocd770o7CJ5S3gA2RE5H2jY6Iz5twpumihMiTDAEB8mHbQS0OWX-emFenNY7v76pgutkS3-qXFhmkScoLqC4OrU9O__71P_91tPl9Sr_R4DciG49YQ0KnswFXD46hCfWtSafxcsiLENMGLR6wFp_CE-7snUNLj9WhNfpc3oulLFNmT9zQBvVTt7qi2nO9J6ZW353NLcMF9ExRsTeeFybIgB1hSU3VeprjCpw2u8P---WqjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63ef1a4574.mp4?token=j24B82P7osvz4JAGUoH7Bx6_8IPSL2wnB_WvGMX3vrg812PDOGZJkCCx3Zfh28Mb3tempfTM9E7d0Cio7BI4zUNbVHcN9ztww1Wfu2Xocd770o7CJ5S3gA2RE5H2jY6Iz5twpumihMiTDAEB8mHbQS0OWX-emFenNY7v76pgutkS3-qXFhmkScoLqC4OrU9O__71P_91tPl9Sr_R4DciG49YQ0KnswFXD46hCfWtSafxcsiLENMGLR6wFp_CE-7snUNLj9WhNfpc3oulLFNmT9zQBvVTt7qi2nO9J6ZW353NLcMF9ExRsTeeFybIgB1hSU3VeprjCpw2u8P---WqjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معادله عوض شد
دیگر صبر نمی‌کنیم تا به ما حمله کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/676624" target="_blank">📅 12:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676622">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FG9oZG_W4in7P3zWL13gi_qnDNRshv1Ct28jQuFVu07kWRwbajLBZUHiIpiCj90wE_pZXXEzGOfuVl2ixpzA_jzj--6O_rSrBn4ns_iP0Xsdd-M56_QVkr2AQbcAg8XH41Nz6zW093XcsHdLmbJych2Su4wtMRCwdDbonZUjXoIcq3uGa6oG2MJJu-HhXiZJgUhQqFRfqbk7K_FkcXFuIdjrRvlX33rQg-_vVSgvzqPdv7cQTV6rpdLoXVIgmg4QmqwcIHdR-KvxrrN9sHcaUDUGpveCDcLe5bf2D10IwSrdxiuErfdC8-DWM5Prfot8DaawiYLZ39QKXdD4HYtDPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gW99nm300oBq-A6cgRTJD5FIn-zUXWWi-viMCB0zHwz3wmlf_l3cymqbSofu2X56uVA4yxFyvIhEPcGnQ4QunOQavTwgokPX4UL9nudkqOndcxHc2-kKnm1IOTtr4uxCk7qfKwd8_jnJI7aGuRMklbD2z53RSoBv96c75A0wZSnaHJlk52fNRBaTD_-pzIO6Gh4nfwII8hq0gyZBjqiskapDm-NhFVlGrbvfSHGG7qxbw9Jt68u8n3EvAVEw7yh67RBWJ-JCh_gmKCk6S6ARI2eqFNjIxvf7wTXVF2lYHWO87kgJujrd5NU_oxAcCe5Dqyza0kjD5vYKvUELv-QVjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در ایران به ازای هر نفر حدود ۱.۷ سیم‌کارت فعال وجود دارد
🔸
ایران با ۱۷۴ اشتراک تلفن همراه به ازای هر ۱۰۰ نفر در رتبه ۱۲ جهان قرار دارد؛ یعنی به‌طور متوسط به ازای هر فرد حدود ۱.۷ سیم‌کارت فعال وجود دارد.
🔸
ایران از نظر تعداد اشتراک تلفن همراه، بالاتر از کشورهایی مانند چین، آلمان، سوئیس، فنلاند، بریتانیا، آمریکا، ترکیه، عراق، هند و افغانستان قرار گرفته است.
🔸
تعداد اشتراک‌های تلفن همراه در ایران طی دو دهه گذشته رشد چشمگیری داشته و از کمتر از یک میلیون اشتراک در سال ۱۳۷۹ به بیش از ۱۵۹ میلیون اشتراک در سال ۱۴۰۳ رسیده است.
آمارفکت مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/676622" target="_blank">📅 12:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676621">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
نشست اضطراری وزیر دفاع عربستان با ترامپ و ونس در کاخ سفید
🔹
وزیر دفاع عربستان در کاخ سفید با رئیس جمهور آمریکا و معاون اودرباره تحولات منطقه به ویژه تنش فعلی با ایران گفتگو کرد.
🔹
گفته شده خالد در دیدار حامل پیامی از سوی محمد بن سلمان، ولی عهد عربستان بود.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/676621" target="_blank">📅 12:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676620">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
عربستان: ما ادامه تجاوزات ایران به اردن را محکوم می‌کنیم
🔹
ما با اردن در هر اقدامی که در رابطه با حملات ایران انجام دهد همبستگی می‌کنیم.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/676620" target="_blank">📅 12:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676619">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a9b2bff6b.mp4?token=TBoSnqpIwDvJ96delQeVKYipjqBPOCaKqPXh-9svftiTtSoWpzJ9mIvRkvqmzqds-s1wurwIE5FWy71t2SeHv7VqTx_YCr1c3hWY5R7BTjWdqDnLrrJTq2h7MyMmKoQ87R1WaPLI-tVraUhdSBTd9YTU4HjlqlpK-8zdwxcZpAs4YrhLfbzXcmkvysTVwSTwlUeKBWDwCyLjXXQZh_KtbnNqR2uR1EnTCs6JAMdAvJHVfmcXHgrc2RdqJW8EHsZ7jTgltCgMjuOEQQa8O4kOi9OPjgFgGhC85ZODYH6LNJ0EC83g8QHkDcDr57C0L-ujcyz9FhPpKSwscGNFY6YVWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a9b2bff6b.mp4?token=TBoSnqpIwDvJ96delQeVKYipjqBPOCaKqPXh-9svftiTtSoWpzJ9mIvRkvqmzqds-s1wurwIE5FWy71t2SeHv7VqTx_YCr1c3hWY5R7BTjWdqDnLrrJTq2h7MyMmKoQ87R1WaPLI-tVraUhdSBTd9YTU4HjlqlpK-8zdwxcZpAs4YrhLfbzXcmkvysTVwSTwlUeKBWDwCyLjXXQZh_KtbnNqR2uR1EnTCs6JAMdAvJHVfmcXHgrc2RdqJW8EHsZ7jTgltCgMjuOEQQa8O4kOi9OPjgFgGhC85ZODYH6LNJ0EC83g8QHkDcDr57C0L-ujcyz9FhPpKSwscGNFY6YVWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✂️
ریش‌تراش/ماشین اصلاح HAIR CLIPPER مدل GYT-999
تیغه استیل ضدزنگ
✅
| شارژی
🔋
| مناسب اصلاح صورت و بدن
🔸
نمایشگر LED (نمایش درصد شارژ)
📊
🔸
شارژ کامل: ۲ ساعت
⏱️
🔸
زمان استفاده: ۳ تا ۴ ساعت
🔥
🔸
شارژ با Type‑C + کابل شارژ
🔌
🔸
صفرزن و خط‌زن برای اصلاح دقیق
✨
🔸
همراه ۴ شانه اصلاح + روغن + برس نظافت
🧴
🧹
🔸
بدنه پلاستیک درجه یک
💪
🎨
ارسال رنگ رندوم می‌باشد.
💰
قیمت قبلی: 1,698,000 تومان
🔴
قیمت 1,398,000 تومان
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/brief/47608/180124/</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/676619" target="_blank">📅 12:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676618">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59db64932e.mp4?token=IM8XDSTInANPZtqa-wv3Ra3QJqAjiKczdbHMgd8Y3WSC48xykHK2ljOcMY05SwhP-au0BI0_Csb5ZGy8SIex-Nc7sSzMDdC0wKXatxiWmideqCo0gFADo9JdoWanaFIXf0gOMODTiuEMTLYAXyvc7-Oz_RupxoKhgY05bUubdS5X2-bs7Fadk-b1nM2IvHN4tQUL5hwSl93wPLbZoUz4g_lbbEmeGWzkIw2VW1qgQfivAPZhl_lbQKNCYnOA_6bk8i3NBHfmtcIAlRXkXwO6tnYNNlai9hpa3D3GAPBEKMWV5ZTjGtnoyiZa53l8UydpUPkX7X3TSpyfwhAL_exRpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59db64932e.mp4?token=IM8XDSTInANPZtqa-wv3Ra3QJqAjiKczdbHMgd8Y3WSC48xykHK2ljOcMY05SwhP-au0BI0_Csb5ZGy8SIex-Nc7sSzMDdC0wKXatxiWmideqCo0gFADo9JdoWanaFIXf0gOMODTiuEMTLYAXyvc7-Oz_RupxoKhgY05bUubdS5X2-bs7Fadk-b1nM2IvHN4tQUL5hwSl93wPLbZoUz4g_lbbEmeGWzkIw2VW1qgQfivAPZhl_lbQKNCYnOA_6bk8i3NBHfmtcIAlRXkXwO6tnYNNlai9hpa3D3GAPBEKMWV5ZTjGtnoyiZa53l8UydpUPkX7X3TSpyfwhAL_exRpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چه آرامش‌بخش است دانستن این حقیقت که گاهی پشتِ گلایه‌ها و اصرار بر ترمیمِ رابطه، نه خشم، که عمیق‌ترین لایه‌های عشق و دلبستگی پنهان شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/676618" target="_blank">📅 12:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676617">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deb2aa7882.mp4?token=hYpszKgVLrJcOVEgivmkk2V1tDCA22DeYRxv89rlLLzGao01nbQZAerXhlLxaXx2ZUJv-dLIEeqD0ZlEVpEGfB4rlSYQ4XGaLxjS64i7AqSUCRDlgsDnqPGd3tENKaLq5uzooz1wZHe-4F7FKsvY6QDNSOqKNGDDmcUKPtewR6XsVwcp9dJdij1wmOp5_LRnnF-ufRUGdIaXKMkEMnnwS9aSDitQaRq11IIkEcv8lNehM89_NHYjk42CZ0OqWlMEnYjMI-2z7HC6Q7jtLvKdeGbY024A97rizosXmchC3HZrAzRbORyeGc8pNH-P7ROfjz5wiSzGobEMZsnBOlxa1Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deb2aa7882.mp4?token=hYpszKgVLrJcOVEgivmkk2V1tDCA22DeYRxv89rlLLzGao01nbQZAerXhlLxaXx2ZUJv-dLIEeqD0ZlEVpEGfB4rlSYQ4XGaLxjS64i7AqSUCRDlgsDnqPGd3tENKaLq5uzooz1wZHe-4F7FKsvY6QDNSOqKNGDDmcUKPtewR6XsVwcp9dJdij1wmOp5_LRnnF-ufRUGdIaXKMkEMnnwS9aSDitQaRq11IIkEcv8lNehM89_NHYjk42CZ0OqWlMEnYjMI-2z7HC6Q7jtLvKdeGbY024A97rizosXmchC3HZrAzRbORyeGc8pNH-P7ROfjz5wiSzGobEMZsnBOlxa1Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از ‌حمله موشکی‌ آمریکا به منازل مسکونی در قشم
🔹
در پی حمله موشکی آمریکا ‌به منازل مسکونی در محله چاه‌تنگو شهر قشم ۳ عضو یک خانواده به شهادت رسیدند و ۲ فرزند دیگر این خانواده نیز مصدوم و برای ادامه روند درمان به مرکز درمانی منتقل شدند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/676617" target="_blank">📅 12:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676616">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
اگر بنزین گران شود و سهمیه خودروهای شخصی کاهش یابد، حمل و نقل عمومی توان جابجایی مسافران را دارد؟
اطلاعات:
🔹
اگر بنزین را گران کنیم، کدام ناوگان حمل‌ونقل عمومی توان انتقال جمعیت منصرف شده از مصرف خودروی شخصی را دارد؟ مگر در شرایط فعلی چند درصد از ناوگان عمومی اتوبوس و مترو در شهرها خالی از مسافر است که فکر می‌کنیم گرانی بنزین مردم را به استفاده از این ظرفیت مغفول ترغیب خواهد کرد؟ در سالهای اخیر کدام خودروی با سیستم استاندارد سوخت تولید یا وارد کرده‌ایم که اکنون از میزان  مصرف روزانه بنزین گلایه داریم؟
🔹
اگر در سایر کشورها بنزین گران است و مردم کمتر از خودروی شخصی استفاده می‌کنند، در عوض سیستم حمل و نقل عمومی بقدری پیشرفته و با ظرفیت است که استفاده از آن برای مردم صرفه زمانی، اقتصادی و رفاهی دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/676616" target="_blank">📅 12:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676615">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
دقایقی قبل زمین‌لرزه‌ای به بزرگی ۴.۵ ریشتر در استان سمنان را لرزاند.
🔹
گوترش: نگران هستیم که اگر ایران و آمریکا به مذاکرات بازنگردند، درگیری‌ها گسترش یابد.
🔹
سازمان ملل: قاچاق زنان و دختران در سرتاسر جهان ۲۵ درصد افزایش یافته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/676615" target="_blank">📅 12:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676614">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8pZkopDVH6sEyT3fFt4KNpAhb6824y34qX-PSmmj3oukjEeN8MWrxhZ0LrB3Nkx-15sYSRO4pR_J74VAMLyZaF4l3zflThK1dMnAjR1DZAyRklZMm7ySRxwGh4EtaA51p7NnYGiTa1iJkXoFY0ATtb1R7prave6kIQjnLFCeDM2Ppnc5chbdYFgod68yHc1m1wuLjXUfYzATUWJG0aV5x9uPVHCbI626OAjOhoblvDQEkdcg1CYuvWB6rAGxhbF8CSx6RxXab-ZqJavG-CnuR_jo1XrJTR3HIw-cC_lZ90e8-YzuNfXQp9MaP6fsnSQ9M0nToAGscqzwvXg6BvT6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بلاگر متهم به ضرب‌وشتم زنان در لایو اینستاگرام، بامداد امروز در خیابان مطهری تهران دستگیر و روانه بازداشتگاه شد.  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/676614" target="_blank">📅 12:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676610">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cFbKHPqxqMU-3iaBkY7F-NnUvjrLd3EiGOO_swOO9PvSD4eYmMKOhy_NHnchhUkTeB7pA3ua-9xBBAf1iI0Hg5WizSOD6xSf8bNJjav22Fyeab3agwwBmQJ71qc4qYpfPaYeT0dypjmlaJ1ndWwrY8jC7Mu6XlDI1psXOcfawdHMwKZxfqRIiPmfiMJyVAItKjyydQsBHoMW7UERSzIdHxmz7Unj1Sdvvo8rvHOROCIQdr8r8rST8NFqjDyylGY8XutbgRokTB1mYJ5FlV97N4NZV80E6745xw3XJwsrfzrh1Lwm3X-sLnrbA7HTGfoQuEPU3J7mZjBhbkB30XbSOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GyL7m9YDeZLkNN9iPtmGIT1_bMxcUuv_xfcKJCQDaVvDHDg9vaA6A9_0DXNJeIZjLWL5KTXpojAsmlKoUr5jkP_xphzBnHukKYxWex58MvSgE7BWJFOblHslKY25skgzalE2O9P7z9yJJd8qiy8M2DLNnW6tdlZh8jIAbyddeMjrf8F4HW4Eq7bWFIIG-EsxzMkiRfzv9Z0LHae6aP0UU2rnEH0WJ5YIypOjJlr8_KppgqSdgTgF3XVj0pN6sG9EJJle2nl7EQ9FWdiJVW5qbLmlxy15ypRQiQizI5iGR102WFM7xSiaVYxm6i_XYUgcGCaJcogMsX86-mAB8CDEJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lpEBIhXYayzwPrDIB0-ta54tXDqSRNdgdNM0Uxa4JQRDdo0X0wPHkYmprtxk9b2sFo9_VCHqWn2HvZ_pXzdg5Mcddmj1Wr3UZN_Wr1E27aQ-XBl7TF_4dvl9qSl4GVe8oALY97B181E5nFVFQ2RWLivnxex4ZgDvlLbkqLLxkZxFVSw0yejn4ywILmCPOeQbLbJb5c9_EVFmT8kvF_AGuvZUXrQ2dyWh2lw-KEWOtTOl-8BXTDUQbngw7frRqwzNq0j12B0rt5CqX3BzRL70z0RlKdnYzIDi6CkvjulPeb_2hv2fbI3o9_eEVJvk1S65p9XFDcqa3ZMns31zyKvp3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JxJBYtoJl-LSfXlYJxafS6Obn3Th5mjUKQ44hnD2JyviU4sG1d0wV38CUEXgS3QrmzbNpPViPhpxmnkB9d_CirYbDpqKQsMYAh41305QGTOy-d-iX46_KxywlsVMjuWc0HGrVs6HH3MwfMQio1ywpLQmkLRCXCOAXBilMpZ-2f0wEkj-oRPuES_JkdA2tkMSYQM4TfIjs6H2QF5R1ZMZEymKTcq17SFAztLM3SiHhgECwIc7z108rUrWCOuQeYo9v6aqS92RpOY1Ogn2nRFwauumaNDdMwdm7M0Uk7Ll30T3YYoE9Xq454mLn-SFICme3n8NaqyY_CdsHp4dGvT33g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بعد از دیدن این ویدئو‌، دیگه خودتون رو با دیگران مقایسه نمی‌کنید #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/676610" target="_blank">📅 12:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676609">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
نتانیاهو:
در صورت دستگیری در هر کشور اروپایی، نیروهای ویژه اسرائیل برای نجات من مداخله خواهند کرد
🔹
طبق اساسنامه رم، کشورهای عضو دادگاه کیفری بین‌المللی موظف به همکاری در اجرای احکام دستگیری صادر شده توسط دادگاه هستند.
#Demon
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/676609" target="_blank">📅 11:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676608">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
تصاویر دیگر از تشییع با‌شکوه زائران و رزمندگان شهید حشد شعبی در عراق
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/676608" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676607">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693addf9fb.mp4?token=bB8GZ74rZL32Sm0fsvsEUCJihou1FUz_phPQHPAxk3dCS5WAvV7Nkgcy_mkb41zy2BJ34kIDi9HMjSNjVxeeDy_zs_GSR_L_-DGpUxsSfJ-bJcAfOjTSKMqReEve0o0V2fT8wQtmPlri6SnZZU8-nFD35VpwTy-I2YmaNBK40WtyJjn3FCOlTRJcyigAg0h6qGnqNIdvRFM9rgr3WaNTKBOh43WGtpywetStx_Eiwr9gvNuqtI_Zv0XPAxOTX5CkswSZk-RWDWO3LDAtB2maIU3hHT2uKz0GXW4_q7anIt0YlfD_wPl7dYLNu4ki7Sk2Z0RgHbG8FZnoFqajPqXSLJ_Jg3d6JhEZLIBEd7RSbv_RH9YZd9dYLQX56WFrDGDaE2-fLbau0FQ4JReEdl68gGnNvbWiw9gZzciej8Y_SZEWZtiywM_0W3GTLXdXxhYqZUQft_wSl00Vxux47l75ZiWapqrQWUnb_9mPrp9v9y_kUCmmzQY75jaPtQT67cQoHpr-0x5XNv4B7WgyM9GFM0ME1tp6oQKsIEYGPtT3tDiV21BlYqXp1h_oTtWpuVvhQBrXwbHBCBd7YOwMEwcwRIaYs_G05-FajO8vd_1-ZUh6MEjsNAWhhc6ndcw52Seis4MQVWSz6nU1OAfG_vw8zUu6oQM1xRzjG2IVZI4c4fc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693addf9fb.mp4?token=bB8GZ74rZL32Sm0fsvsEUCJihou1FUz_phPQHPAxk3dCS5WAvV7Nkgcy_mkb41zy2BJ34kIDi9HMjSNjVxeeDy_zs_GSR_L_-DGpUxsSfJ-bJcAfOjTSKMqReEve0o0V2fT8wQtmPlri6SnZZU8-nFD35VpwTy-I2YmaNBK40WtyJjn3FCOlTRJcyigAg0h6qGnqNIdvRFM9rgr3WaNTKBOh43WGtpywetStx_Eiwr9gvNuqtI_Zv0XPAxOTX5CkswSZk-RWDWO3LDAtB2maIU3hHT2uKz0GXW4_q7anIt0YlfD_wPl7dYLNu4ki7Sk2Z0RgHbG8FZnoFqajPqXSLJ_Jg3d6JhEZLIBEd7RSbv_RH9YZd9dYLQX56WFrDGDaE2-fLbau0FQ4JReEdl68gGnNvbWiw9gZzciej8Y_SZEWZtiywM_0W3GTLXdXxhYqZUQft_wSl00Vxux47l75ZiWapqrQWUnb_9mPrp9v9y_kUCmmzQY75jaPtQT67cQoHpr-0x5XNv4B7WgyM9GFM0ME1tp6oQKsIEYGPtT3tDiV21BlYqXp1h_oTtWpuVvhQBrXwbHBCBd7YOwMEwcwRIaYs_G05-FajO8vd_1-ZUh6MEjsNAWhhc6ndcw52Seis4MQVWSz6nU1OAfG_vw8zUu6oQM1xRzjG2IVZI4c4fc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی سنتکام ناخواسته مرگبار بودن حملات ایران به اردن و ضعف سیستم دفاعی آمريكا را تاييد كرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/676607" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676606">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLKVghMN4pdolkDTtymDZfTXUDsMs4MeZKRVLmuTCn3IDz-oIlbpk8o0esh5fdS1VNZnfRthJsXV-5ZOuNGBAoxF22koSbzGeu-LjpT4recIqLU1_XWKv8cF6l_inZ9C-cQsYOI4hua5ABtqSLsm-8O6X5V_VCrttDVZKOBEcizqFc6tYQdGqqVTncKV_oFhUPKB3VJkoxMGB92vTPIg0fn8g4cyCJ2ph32jmikSL0U9qAPqJyBsGKPFtBqBcn0pz9FXxe9RwjZ01PTd6ZAst1cHht8xCjTAoZxinnCzjktk1ggnJbENQWBGb40MwwZNup9qM5CDuo4fJ5mnFKMnEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۷ درمان خانگی مورد تایید علم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/676606" target="_blank">📅 11:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676604">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85a3bce682.mp4?token=Ws3I3D4tIoCJwZRCHMLRDi-GvShaGFJ_4tjGh7gWUOnpMPR-tg31uk0OmtAO6Y4u8e8PBnnm88VOQnMB3UGyQksR23eYLecfhmKrWllSrdqTND4cHZtcOXO5PPmlPVxHQBbRr-fPTOHCrroMzdWsjp5HjjShOmWZMZKb-vEOwSiYXXDIf-Ri--ZbTvnyMR5Arif5blenqMbA0tkMgNaSXi2C0jM7qKYEp-PH1ko12mvO0lqq8KKrCrPov7tyuIEJHcBuGqkTsGm28iKBjhT2PdcEYjhhdB8P-ZMGhTQbngaNOp5kbOS3W_NdgFZyRAC-dJRkAhS1push7egTMiYpMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85a3bce682.mp4?token=Ws3I3D4tIoCJwZRCHMLRDi-GvShaGFJ_4tjGh7gWUOnpMPR-tg31uk0OmtAO6Y4u8e8PBnnm88VOQnMB3UGyQksR23eYLecfhmKrWllSrdqTND4cHZtcOXO5PPmlPVxHQBbRr-fPTOHCrroMzdWsjp5HjjShOmWZMZKb-vEOwSiYXXDIf-Ri--ZbTvnyMR5Arif5blenqMbA0tkMgNaSXi2C0jM7qKYEp-PH1ko12mvO0lqq8KKrCrPov7tyuIEJHcBuGqkTsGm28iKBjhT2PdcEYjhhdB8P-ZMGhTQbngaNOp5kbOS3W_NdgFZyRAC-dJRkAhS1push7egTMiYpMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
یا حسین ما انچه در توان داشتیم گذاشتیم؛ هیچی چیز هم نمی‌خواهیم؛ فقط می‌خواهیم ما را به عنوان خادمین خود در اربعین قبول کنی
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/676604" target="_blank">📅 11:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676603">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
پاکستان: یک کشتی در دریای عرب به گل نشست/ نجات ۱۹ صیاد از جمله هشت ایرانی
🔹
نیروی دریایی پاکستان اعلام کرد که طی یک عملیات جستجو و امداد در دریای شمالی عرب موفق به نجات گروهی از صیادان از جمله ۸ تبعه ایرانی شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/676603" target="_blank">📅 11:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676602">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f3790cdfd.mp4?token=olVCULxvasTGsbcc4__DOY-ArBehqP9-8awHLMcpM6-v9Mv4TaxyGF3PT-SFbbmZg3dj3sKf5FfS-FA9-M6XLsUSLL2AhYtfXNHDl0QFlsnKXC7EMGqRjk2o2cfWLHRZuRuFRIbYWWyFLwzV3iwlxceIRbrUlOYvG9ai4NGuFGn4n643AJDcFqqRZDvyTSkqiH1MXQR3NlELd9m7BmC75gQeMkqcO18G_LbA6ipxjZlXa10vc-qDybOtdBmu-gcj27fOpclurIuycTGKmE55i36VyGrqSYvPqb_98PXQJx8pjTJtSKs30akKGsDanFFMeLkaaVbhREnGTxYtxL7tgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f3790cdfd.mp4?token=olVCULxvasTGsbcc4__DOY-ArBehqP9-8awHLMcpM6-v9Mv4TaxyGF3PT-SFbbmZg3dj3sKf5FfS-FA9-M6XLsUSLL2AhYtfXNHDl0QFlsnKXC7EMGqRjk2o2cfWLHRZuRuFRIbYWWyFLwzV3iwlxceIRbrUlOYvG9ai4NGuFGn4n643AJDcFqqRZDvyTSkqiH1MXQR3NlELd9m7BmC75gQeMkqcO18G_LbA6ipxjZlXa10vc-qDybOtdBmu-gcj27fOpclurIuycTGKmE55i36VyGrqSYvPqb_98PXQJx8pjTJtSKs30akKGsDanFFMeLkaaVbhREnGTxYtxL7tgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این ظرف سفالی، ماشین میوه‌شویی ۳۰۰۰ سال پیش در ایران باستان بود؛ بدون برق، بدون صدا، فقط با چرخش آب و قلق مهندسی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/676602" target="_blank">📅 11:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676601">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b537f120d.mp4?token=kslR4CP1-DhFcXH4mJ6nMroLutxXz7ig9VbgOv1ngwjZ5yWNS7jd18VWBez3tF_4twlqMtlHZeWoRTSgdWnoTGWh2JN30KL44nAZXzU_lDtYzycnxv2PgxwRLZdYSucYFUWnHfozt2uTYLQ89ebcy_wTO9V5Yzmp39ssZfXSBUcgRQaBICptQOZQOrbhL3Tpxe2RuNqHMzASZfNB7uayF4rUSFvrhe-F1m2uWCn7IgOWYUTenKO_pqLTy86OUlA5CXcY2MDd1rh1CWR_8kWaplnK1enb2Mz9gtA7vx0gmYOB3EVgtjYgeCqNsftOyBrtk16gEquJdkRRtO341AC4rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b537f120d.mp4?token=kslR4CP1-DhFcXH4mJ6nMroLutxXz7ig9VbgOv1ngwjZ5yWNS7jd18VWBez3tF_4twlqMtlHZeWoRTSgdWnoTGWh2JN30KL44nAZXzU_lDtYzycnxv2PgxwRLZdYSucYFUWnHfozt2uTYLQ89ebcy_wTO9V5Yzmp39ssZfXSBUcgRQaBICptQOZQOrbhL3Tpxe2RuNqHMzASZfNB7uayF4rUSFvrhe-F1m2uWCn7IgOWYUTenKO_pqLTy86OUlA5CXcY2MDd1rh1CWR_8kWaplnK1enb2Mz9gtA7vx0gmYOB3EVgtjYgeCqNsftOyBrtk16gEquJdkRRtO341AC4rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی پربازدید از عادل فردوسی پور و وزیر ارشاد در حاشیه مراسم یادبود اکبر عبدی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/676601" target="_blank">📅 11:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676600">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2ZiNTusisTcoUJj0NsN9CCZH7WuboSGEGtPV_gTaML6iwGkNdRGuCqkTf-efVkU_CupauzqN3G00m7__xcD36I760rouswR6kvR1v1oKC-2IzM1O3GkKKnEOk6VAoZ_qBhVauS2SHZFlIc4SaahNKDBJvav_6Mc3GTMl7nCOU6NORXNaVxNG5-uPma40goukYSFZvZb7RygNnUsLzFo4v5coAV1rpEdl8-EiGtVnEzCXG7tvHQN6s20hnnB_dVjo1z7B7_PtZFZm4D6vI-uYxVUD8_AvZHL2bfo5goIiGblM8WvJUKm4dTt8lL-ttQ-3UQbaMAP79t4ZsAJSKINeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
موسسه واشنگتن: تنگه هرمز به قبل از جنگ بر نمی‌گردد
ادعای موسسه واشنگتن:
🔹
اقدامات تهران نشان می‌دهد که ترتیبات سنتی حاکم بر تنگه هرمز عملاً فروپاشیده و نظام جدیدی در حال شکل‌گیری است که هدف آن تثبیت کنترل ایران بر این گذرگاه دریایی است.
🔹
ایران دریافته است که کنترل تردد کشتی‌ها در یکی از مهم‌ترین آبراه‌های بین‌المللی چه میزان قدرت و نفوذ به آن می‌دهد. تهران در مذاکرات آینده نیز از اهرم تنگه هرمز برای تثبیت نظم جدید دریانوردی استفاده خواهد کرد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/676600" target="_blank">📅 11:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676599">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
رویترز مدعی شد: نتانیاهو پیشنهاد ترور فرماندهان سپاه و ارتش را به ترامپ ارائه کرد
🔹
خبرگزاری رویترز در گزارشی ادعا کرد که بنیامین نتانیاهو، نخست‌وزیر اسرائیل طرحی را شامل پیشنهاد ترور هدفمند فرماندهان ارشد سپاه پاسداران و ارتش جمهوری اسلامی ایران به دونالد ترامپ ارائه کرده است./ جماران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/676599" target="_blank">📅 11:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676598">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nt_v_g-BLFJDkGSAR7OczQLRE-nFJcrYDgi49hCWsrodHH1K55rNpeoYzBG_Ctv4IuHP2DUWwfKSsSiKA07xKEjOImp_iHDsYnNX8uAd8AT0_X_MSvwHDdQqOCuckoZeag7urtD2ei5b0k7b9beXaT8Cho74TT7qXd6wL3cN5px0c39ASjwnQr8WU4i6-vs0V2iFKEQaWflFzHqwl_VtAmX4nu01j2GjdhQ-lVhfZ3nXFPVU8sURi4SnKAxjgOgQP2ZXywEVoTYf0pANjNNs9xaope17EB9b_urHOyvtx130G5X_qDpF4FH27uZ1Jre2hMAPA6i4Fpfje4yA_myvGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اکونومیست: ترامپ در جنگ با ایران وقت تلف می‌کند
ادعای اکونومیست:
🔹
آخرین دور مذاکرات به احتمال زیاد یک وصله ناجور برای یک توافق نخ‌نما خواهد بود. جنگ بین آمریکا و ایران متوقف شده اما پایان نیافته است. تنگه هرمز عملاً بسته است.
🔹
ترامپ از تهدید خود برای حمله گسترده به ایران عقب‌نشینی کرده و اکنون ادعا می‌کند که مذاکرات به خوبی پیش می‌رود. او در این جنگ گیر کرده حالا وقت تلف می‌کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/676598" target="_blank">📅 11:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676597">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
کشورهایی که در کمک به متجاوز دخالت دارند، اگر رفتار خود را اصلاح نکنند، پاسخ سختی دریافت خواهند کرد  روابط عمومی سپاه:
🔹
شب گذشته دو تانکر نفتکش با تحریک پرنده‌های آمریکایی قصد خروج از مسیر ناایمن جنوب تنگه هرمز را داشتند که پس از وقوع حریق شدید در یکی از…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/676597" target="_blank">📅 11:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676596">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
جدید‌ترین تصاویر از حمله به بندر دمیاط در مصر
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/676596" target="_blank">📅 10:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676595">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
کویت از حمله به شمال این کشور خبر داد
🔹
ارتش کویت اعلام کرد درپی حمله به محلی در شمال این کشور، یک نفر کشته شده و خسارات سنگینی به محل اصابت وارد شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/676595" target="_blank">📅 10:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676594">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
پاکستان: برای احیای مذاکرات ایران و آمریکا تلاش می‌کنیم
.
🔹
کشته شدن ۱٠ پلیس در پی حمله افراد مسلح در شمال غربی پاکستان
🔹
زلنسکی: در حمله موشکی روسیه به چندین استان اوکراین، ۸ نفر کشته و ده‌ها نفر زخمی شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/676594" target="_blank">📅 10:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676593">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
اردوغان: دولت اسرائیل به جنگ متکی است
رئیس جمهور ترکیه:
🔹
نه فقط فلسطین و لبنان که تمام منطقه بهای تجاوز اسرائیل را می‌پردازد.
🔹
دولت فعلی اسرائیل که به جنگ متکی است، همچنان از طریق تحریکات و طرح‌های خود، منطقه را به سمت بی‌ثباتی سوق می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/676593" target="_blank">📅 10:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676592">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43e83e267a.mp4?token=OxrnmmfnyNALoUzo3fsDvv69ERqRECLBmanGODfe7uJo8-vRg5SMr3xLkCGhAbrpRiA93cVDtJLwlgOI6ce-sR17ZzFZfl_aojZCxIiZWVZFY1zCd8Q8nCveeGytICzy-GI1XntXcF-AVFxqyMNIhhTwY3z06bvaXOJUVBxfiM5UFfqXFa-0nqql94r0fUlowVPD81D_s_5TWD6BqNDyYi42Q8eGuOiBs6XmykrtbQLppjbQpyRt5jMvum-_V3s1PToCXFiDkA-RvYqFx0DxNn9hhBcT7qYMXKthSvR2dRpUzQqZCffqXfEoECD4PKG4DrGPLwhJhBAMInSBQi1IGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43e83e267a.mp4?token=OxrnmmfnyNALoUzo3fsDvv69ERqRECLBmanGODfe7uJo8-vRg5SMr3xLkCGhAbrpRiA93cVDtJLwlgOI6ce-sR17ZzFZfl_aojZCxIiZWVZFY1zCd8Q8nCveeGytICzy-GI1XntXcF-AVFxqyMNIhhTwY3z06bvaXOJUVBxfiM5UFfqXFa-0nqql94r0fUlowVPD81D_s_5TWD6BqNDyYi42Q8eGuOiBs6XmykrtbQLppjbQpyRt5jMvum-_V3s1PToCXFiDkA-RvYqFx0DxNn9hhBcT7qYMXKthSvR2dRpUzQqZCffqXfEoECD4PKG4DrGPLwhJhBAMInSBQi1IGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا ایران را دوست داریم؟ #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/676592" target="_blank">📅 10:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676591">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
ترور ناجوانمردانه در شهرستان ایرانشهر  مرکز اطلاع رسانی پلیس سیستان و بلوچستان:
🔹
ساعتی قبل افرادی مسلح به سمت مأمور انتظامی در ایرانشهر با سلاح گرم تیراندازی که متأسفانه استواریکم "مهران سالارزاده" به درجه رفیع شهادت نائل شد.
🔹
تلاش برای دستگیری عاملان این…</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/676591" target="_blank">📅 10:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676590">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SyxmjOCVH3cp27U3rKnYWkm6jnomxewQwwcqzOD34jzqds7h-7hzDdG5K_7anjn1gK6MCW0ij-aqdbsTYBEg2ySeiWRT5CERR6znYidGouApJqZXFCUZujBtuzCt215y762UrBZgOcPriPmiqCF7qSvC4bqA6xPcoNGOLbhBMiIxPpTpWP5J4cChBU50tlMgQSoxGD_6Z0ZwPHwVngn8VpaspGWR827Usiers7wUL9sTsRce4WraNBnri5JHyePEYqY0idH2Pi2ymSjqyK2fi7gptpV-VYlnVVxViApQoUFF2duNbWUmQT2sWicaZG41jBZERWmML14wi_mrQD4CEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا بعضی‌ها راحت می‌بازند و دوباره شروع می‌کنند، اما بعضی‌ها سال‌ها در یک شکست می‌مانند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/676590" target="_blank">📅 10:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676589">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0GbDcNoBlbwnwUEvZQKClMVmVoHIEUqsZ7M4u-40EnSeVchTWoMABUS0EN3Cc78Berhg_cOHxTeWRGgovpLg47CvMJCO6xGmhafRoDTUsNuIgd78WOIyDQNZmJw95SNtHoUrma3Kca460iYWvLWu88qjmHI4S-7a59GDhfRXeFc0z4M-7Rlu0IZgG53Pw2YOUmLJ0bKNV1Nrw2h--IjQtopioiVcrGyDJGqPPKKYdy5aNGANfQKEesH9ZlOvcuRTwJO2PgR6Pf0VGmMYvH6AXK1qd_icNx1e9536Jt-qzJjgGuuwXP7ZekIFFFbTpJC5Bcg_iMI1eYXtNmfLrIZNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنگی که ترامپ نمی‌تواند برنده‌اش باشد | تشخیص اشتباه شکست‌های آمریکا، ترامپ را در ایران گیر انداخت
🔹
دونالد ترامپ بیشتر از هر زمان دیگری در رابطه با جنگ علیه ایران در مخمصه قرار گرفته است، این را مارک چمپیون در یادداشت خود در بلومبرگ نوشته است.
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3234105</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/676589" target="_blank">📅 10:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676588">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3567e0150.mp4?token=OURneAJMy1Y6Bu_RdVYn8xkk0jSvEIWdBoKYSrtgZLvfjASTqmJXabaBv3Y7z8Hu3GEB1qxDelil09LfeFjs0-ES1Lj-RilYfWPc9JanVwuwMXc4hrsU9I48QXHi_iHbBnZRjSdwg6RZPbImBB7QCRIBdeQskkDwoR-dTrOPG6Ec7bEjBfPzTSCc9av5PkAWXMwPrFwplLW0keJLBmNx_WzJzCva2H6i0BPn4gWJodZ51PO1ZeGe-FGqSyahy5ldW1iCIJ0TPa69c-L-TLjtbKRVDG2wXym7KVJgMQtQsAWBg7Z0QV36sN1W41ckZvhiDBLg1kC09wJnlRofN-JSgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3567e0150.mp4?token=OURneAJMy1Y6Bu_RdVYn8xkk0jSvEIWdBoKYSrtgZLvfjASTqmJXabaBv3Y7z8Hu3GEB1qxDelil09LfeFjs0-ES1Lj-RilYfWPc9JanVwuwMXc4hrsU9I48QXHi_iHbBnZRjSdwg6RZPbImBB7QCRIBdeQskkDwoR-dTrOPG6Ec7bEjBfPzTSCc9av5PkAWXMwPrFwplLW0keJLBmNx_WzJzCva2H6i0BPn4gWJodZ51PO1ZeGe-FGqSyahy5ldW1iCIJ0TPa69c-L-TLjtbKRVDG2wXym7KVJgMQtQsAWBg7Z0QV36sN1W41ckZvhiDBLg1kC09wJnlRofN-JSgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زلزله در ژاپن با حداقل ۱۳ کشته و ده‌ها زخمی
🔹
نخست‌وزیر ژاپن سانای تاکائیچی اعلام کرد که در زلزله ۷.۱ روز گذشته در استان کوماموتو، حداقل ۱۳ نفر کشته و ده‌ها نفر زخمی شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/676588" target="_blank">📅 10:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676587">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
اکثر آمریکایی‌ها معتقدند ترامپ در جنگ با ایران پیروز نشد
🔹
طبق نظرسنجی یک نهاد معتبر آمریکایی، به باور اکثریت مردم این کشور «ایالات متحده در حال پیروزی در جنگ با ایران نیست.»
🔹
۹۳ درصد از دموکرات‌ها و ۷۳ درصد از مستقل‌ها گفتند که این جنگ «ارزش جنگیدن» را نداشته است اما به باور ۶۷ درصد از جمهوری‌خواهان، این درگیری نظامی ارزش عواقب آن را داشته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/676587" target="_blank">📅 10:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676586">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRK7uXSc0FD8GA1m_g6BDJ-98HgCPcENzf3wjDwdfzTseO0yGNHdEunuzQNe9nDYSjYJK5cYPj3f8aMRackp6C5ADiZiXDXfKmHsClK0AtaRIieyFA_JAPhuC1gCJlcgDDQVBkCXrHHEl5tX2p3C43iocvhLKfISLX6JmBP-lDxiAMtGzDhnQkImGXisb9uN98DHjrwUhRv-VCPZZrh4_v9jYa7qRYYgbcU7l_vNSaZf6t20yUFaVpiF2O1VEY6DSeDjUgeI_Pnfpo_5nMUPFrXFjqIch_cBwYRIq5zFu9FcQg1EZlYnTmTqx5tq_0AKB9-81-lCHDmD0HwH3Ife6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادامه روند افزایش قیمت نفت/ قیمت هر بشکه به ۹۳ دلار رسید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/676586" target="_blank">📅 10:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676583">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rmnfBDbKazL0Zo7idUoM4iwe_IOQ63H-yiz_SA27qSfUkkyLa2d9X48vL1thVj47iReK8KJeggeUXl6hZjUT0Ub55yHaVeniYCYpF-AHDTHRzltMIlNupdyhGQFivhbx1ptVcPFvpIsgeXDzTFr4c3pyshBhPs5427E7-v2OEDNyOdLVHXx_wISS4KUruXbpSKArXtFl2-dJk0WSUDVfV5qQ0ygZ2rM_gfyQaSjRZzII66QmYrGttQ29RMiBEhCdzqxXjvOyN4vtTd_FNhQDRZJYdu5FBXUUo6sfmO-cFgHd04M6-WF3mcf5Ig6fhpzEnVrQtivi3WsYmhWBEqyfCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mzWd_QAr946V8X7gyAL3dIdllSe0Sxj5-n-4taxdr4t-jaNMJvL3n_fCHmjRsSJ6z0LPtuV2QlGXisg4Bk4IERpkC253KS2eKkfYMSP_UXcsZxKuHBFLOi04E7cwjbvQjt6k1mZZk6FxMpsmFOZ4B4_1hUDi17q2XA5iKEmp0OWSOywV6Nqsp9n2Qr5bLysm1RF3F2b2dG2YA4WpyQmlcZwMLyXf4Py8eK_J4vrhmZExMRoG7oZb4D9iOR4DtK_k0EdVDIQlY02cYbMiEefy5P6Y2iotCxbFkqnuuEYpH7EsEjhyuvL0NT3_9bqZfzTXsvyMu9aX83VEABjW3b5ekw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rvDiWSdtSsvcOVwep2Wk9axH7shjtm3UEUb_ev3LEN_fxqyUXjuMaKSNgTC0ZKQ4DV7rfkabJVEmXJvsGBLTSaHGIV0e6FtVlsBNFZp69oUMYlRtNC1Wr5q8dZGOYInF0KBgEgRxVToRXMfTVmGkJ2BQLFzmPufHXZkde0-264-XEck3ldZMAlbhaObZdRamRgHxP80S2sgjez1yAi1CW0YHCInHihY2sy29zOU3UvuENsDPNtMm8gZ6XhKCbLIP0H9zs-L5axp2FYDtQBsup9V1KtTSRqxT30Vr7i9BCkzGWI717J4jEulTL7hKNUoqK-9vAs41zj_VlY4cMM0Zow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر هوایی از پارکینگ مرزی مهران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/676583" target="_blank">📅 10:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676582">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30fc4e3b69.mp4?token=pmaGqRvjQPqHJJzbedV983SvAPNAo5f2z4npZveS_JQCjAFLfIERtfxFQGJ_JTopfIGmfoWuUDpSryU3F1SI47OEhp7w_uXR_VbQQol55DaSrCNJXPrkPkCVjsRWA8-R7SdAJpTWSbRDeMzvzeX9h7EulMlf8K11CngdECDJ4_0pP2bem0Pqg-KB-xA9yuoWYGdZjSK4ein4n6EsMIkqQV2YFRN-qUp1O--Ahd6_o09CaSqMBVfEe00XZWiHETS3rad49o_8OnxdcWDgW-6uAZky-igncf0LG6JI182Iy1Xz3vl2-XZz8dh_8cd04lZEvnDUn_5L_czYZALclWOlSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30fc4e3b69.mp4?token=pmaGqRvjQPqHJJzbedV983SvAPNAo5f2z4npZveS_JQCjAFLfIERtfxFQGJ_JTopfIGmfoWuUDpSryU3F1SI47OEhp7w_uXR_VbQQol55DaSrCNJXPrkPkCVjsRWA8-R7SdAJpTWSbRDeMzvzeX9h7EulMlf8K11CngdECDJ4_0pP2bem0Pqg-KB-xA9yuoWYGdZjSK4ein4n6EsMIkqQV2YFRN-qUp1O--Ahd6_o09CaSqMBVfEe00XZWiHETS3rad49o_8OnxdcWDgW-6uAZky-igncf0LG6JI182Iy1Xz3vl2-XZz8dh_8cd04lZEvnDUn_5L_czYZALclWOlSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا فصل زردآلو تموم نشده، این مرغ خوش‌طعم و متفاوت رو‌ درست کن
🍗
مواد لازم:
🔹
زردآلو
🔹
ران مرغ
🔹
پیاز
🔹
رب انار
🔹
ادویه به میزان دلخواه #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/676582" target="_blank">📅 10:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676581">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QoPYKvRFsOHlx_yEPVgycRI8lfD-l5Q2mkA4WCZs5ioHwy7ww3Tc_RtKSz4z9_iHtJDs5aMeIyiFjV3hq8e50ksRZXJDzMx3L5RxRTN_JqFDMep0Kkcf5K5_k7F-Io8JxM1N3CdtOfR9GgpwL3CYdgYPTMeVL1ZSaFhOzWF9uqkstmPYlECF5zuKfTJYjDs6pIiF2JhU9u7dtKndIgWzZIO1fzL9rKaZ0Hb09acqn4Xka33ISN6q5f5QCpicDQ7n5h15Fy6uVuOBUVCcB6-g8030MadvlOw50B8CvpDxGv2qQZRkx6nPF7hFDd6hrjUCLEQIPKPIIwyY2hOR7fQk-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/676581" target="_blank">📅 09:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676580">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
نتانیاهو: ترامپ را به حمله علیه ایران ترغیب نکردم؛ مذاکره هم روی میز بود
🔹
گزینه‌های گوناگونی را درباره ایران با ترامپ بررسی کردم، از جمله مذاکره با آن برای دستیابی به توافقی گسترده‌تر، ادامه محاصره تنگه هرمز یا انجام اقدامات نظامی
🔹
من کسی را گمراه نکرده‌ام و هیچکس به ترامپ دیکته نمی‌کند که چه کاری انجام دهد.
🔹
قابل پیش‌بینی نبود که ایران تا چه حد می‌تواند تجارت از طریق تنگه هرمز را به اهرم فشار یا سلاحی تبدیل کند./ انتخاب
#Demon
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/676580" target="_blank">📅 09:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676579">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b9669417.mp4?token=NL53sOLyozpf6Sg8PkxbsjanMPM7dRU7Ne6MA9EHz3aDrc0aN6ECPEWdaRHGWjVXvHhUfuLqVo5geMf6hC-AaOfAjLQBPFoBRmtfEvwrnfpIRV8rium1StJpysGMlC5LCgdEWApA9Zgj3NuI8p-Anl4MWuXbbbgYV50suPbBTUnXrdrWGZergmc3-FTaGCBaU16PCml9XGhuKHUT-0auHymidycVs1x82C-u0I8D7fT24Ak_CKdh1yTq3GxiTeWOtF9oQS_ESblAoT16ZTlVrS_GRj2ZQ-Q_bRAMcadFM1g8a4gRHblF5KGg2v5RFeWXxgW0SLSqvYatSIUMeJ24sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b9669417.mp4?token=NL53sOLyozpf6Sg8PkxbsjanMPM7dRU7Ne6MA9EHz3aDrc0aN6ECPEWdaRHGWjVXvHhUfuLqVo5geMf6hC-AaOfAjLQBPFoBRmtfEvwrnfpIRV8rium1StJpysGMlC5LCgdEWApA9Zgj3NuI8p-Anl4MWuXbbbgYV50suPbBTUnXrdrWGZergmc3-FTaGCBaU16PCml9XGhuKHUT-0auHymidycVs1x82C-u0I8D7fT24Ak_CKdh1yTq3GxiTeWOtF9oQS_ESblAoT16ZTlVrS_GRj2ZQ-Q_bRAMcadFM1g8a4gRHblF5KGg2v5RFeWXxgW0SLSqvYatSIUMeJ24sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باید گریبان جنایتکاران جنگی میناب و لامِرد در محاکم قضائی داخلی و بین‌المللی گرفته شود
🔹
بخشی از پیام رهبر معظّم انقلاب به مناسبت هفته قوّه قضائیه و سالگرد شهادت آیت‌الله بهشتی و یارانش
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/676579" target="_blank">📅 09:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676576">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23578c41be.mp4?token=GlIyk0Lz9xfnh95dcmzHRkJXhwGvJn1SMWd2lj87UTpnbAWTOl5MdyeqT-tI1YazfqK8PgZ7hbJlQCR8sYBezzUme9qfNUcm5xfY2Q2GPXkvSM_s7wE0naXtt8G8WfNoqdaQHskTcdWbJ4ZboZX8kG13_IDtChC_SQQMOHrBGASaDCekQauaoeq_8q4mpqge6l-05XeJYhAH2stmf56j7ne7CvcbyveyJLjTukSkCrwprVAUcZLyc0_BxZrMJOUiDk28sP-1ma_Cdmk6cKxubm_D569o-BupDLKmq5rSyQorWRe3SPxodtEkSiQmgzFaRFhJwJx3hiJUmYs36iYObA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23578c41be.mp4?token=GlIyk0Lz9xfnh95dcmzHRkJXhwGvJn1SMWd2lj87UTpnbAWTOl5MdyeqT-tI1YazfqK8PgZ7hbJlQCR8sYBezzUme9qfNUcm5xfY2Q2GPXkvSM_s7wE0naXtt8G8WfNoqdaQHskTcdWbJ4ZboZX8kG13_IDtChC_SQQMOHrBGASaDCekQauaoeq_8q4mpqge6l-05XeJYhAH2stmf56j7ne7CvcbyveyJLjTukSkCrwprVAUcZLyc0_BxZrMJOUiDk28sP-1ma_Cdmk6cKxubm_D569o-BupDLKmq5rSyQorWRe3SPxodtEkSiQmgzFaRFhJwJx3hiJUmYs36iYObA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بادهای طوفانی سواحل سائوپائولو، برزیل را در هم کوبیدند: حداقل یک نفر جان باخت
🔹
اداره دفاع مدنی پس از آنکه سرعت تندبادها از پیش‌بینی اولیه ۹۰ کیلومتر در ساعت فراتر رفت، برای کل سواحل سائوپائولو، از ایتانهام تا اوباتوبا، هشدار شدید صادر کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/676576" target="_blank">📅 09:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676575">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzza9VUsH3PJorRFMxy21c5un09OLjsm4f_Z5koMZL9BLlRKCU9A6A3WOd3o-_f84vIXEUHwX_baPWdJdV2d19iL0oLQkPxDwAcTM_ysBbeXgTtI__s-sTgq0cS0C-kdhqQa10zg-msEH72Rcv2PTw3Fc3HkNKI_aAqy5KN8V9uYMCEe9O_I2DfKJiuGjlFOucnZ6923_B2S__Damv5pN-JNr3PzAnhi8yLf3Y05S4l-PsvXpOe6MKeOHveJEfYznSBlAKijsu5ndvRn8cHzSoyzXB5ft-JIY26fAb7rtsUH8OasXaxiz7iRdAqSQCNBoa8H3mfapLavNl9kWwhNeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رصد پروازهای مخفی بر فراز اردن
🔹
دادهای ناوبری هوایی نشان می‌دهد پس از ناکامی آمریکا در رهگیری موشک‌ها، هواپیماهای نظامی آلمانی و فرانسوی برای رهگیری موشک‌ها به سمت پایگاه‌های آمریکا در اردن به کمک واشنگتن آمده‌اند.
🔹
ناوبری هوایی فعالیت حداقل ۲ فروند هواپیمای پشتیبانی نظامی در آسمان اردن را تأیید کرده است.
🔹
نقطه‌زنی حملات به اردن و گرفتن تلفات در حملات چند هفته اخیر، مورد تحسین فعالان رسانه‌ای خارج از کشور بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/676575" target="_blank">📅 09:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676574">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
بلاگر متهم به ضرب‌وشتم زنان در لایو اینستاگرام، بامداد امروز در خیابان مطهری تهران دستگیر و روانه بازداشتگاه شد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/676574" target="_blank">📅 09:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676573">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MW55CSaaQCBOH4noEvIA4rG0ZgWGtX0kVifI9_TWhe1eB4gaFqO9ihm_nIXxV9Kz4vuZyCDJYUOTswytzf1GDDqu0Bk8__YDuSioj6OjHw7ZOf_iKv-f6dc2Ojz5IXZWTvt4yGwaaSpFC5D5lWhS2szUEwQxhILR9z7TqQLvOIGo66IYLLNslRkv4tv33ievhbXizgYnTd2pat49EwmNSXYpBuF6nMPqMP4h3qG9HZZXUAnXibNNcgLpmwGsWbi1j8xyV9JQ13xGNVglp3KpIpmE067OUu5vP8-gTproarGe_i6JoxYzoOvtJvBYhGfIg8at2sTQq9X2hkpw-M0LEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۵ ماده غذایی برای رفع کسالت صبحگاهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/676573" target="_blank">📅 09:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676572">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3Ne3eZsmPVfDUj6ezUxCDn3YThUN9E1W_GureXn9ELejwgxFxXh4KA1kp6Dx8njeF55eCc01gpjfv5u3jZzx0qmbbwbST90SZMhLW63n4-CAtkrYSqE1tcosIhDYBRRioaUob9uQ6B44w3icXd6iPE08_XvSvY_0ByLDqgT_9BXDIx6sXVLhZGI5xeMrWPED3kscvSkvuN7-4tJGq61e5kZjmbpJpxgJ0Zhgak0iFCNA9izsDxNgjEnUH9iA8RuaZjLo7CVLMhYqU-E4xpAIcrsgdqYHrxBuyHofDa4Iy1lB_8YMsdFMo3RtEG3lGwNzdVklOIJVkfUGiuQTokpUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عبور کشتی قطری از مسیر ایرانی تنگۀ هرمز
🔹
سه هفته پیش تهران پس از نقض تفاهم‌نامه توسط آمریکا عبور و‌ مرور در تنگۀ هرمز را متوقف به تأیید ایران کرد‌.
🔹
این کشتی قطری با داده روشن و از مسیر تعیین شده توسط ایران گذر کرد و بدون هیچ مشکلی به‌سوی آب‌های آزاد می‌رود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/676572" target="_blank">📅 09:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676570">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2455db6e15.mp4?token=R_fsjTWRTDn6Ee2ikDyXifV04STpaY9k6W832m3NtdRVxd_pE8mK2u51c8F1rT2SisAACkG51OiTsb5WbSbcLPqu0d1lvBZ905_c0toBCLms0vX1MsSK39VEIkHZp9W6tflI0CmH-_SVcIMUw88bj0wwR1B0stgxY2EGvIVQ7u-pjMSbAOtO-Buewc-PB2WatywYjS02HIjE1j7A243mJhDgH0lUVUIP6zev4RkexRBtCSK84xawTWAHIsXSxUYpgZERWeSQpQf8MBVTDYOn5qq7wQd9CDKEGcowu3DUYfxKa9vB2by3kXr1uxMvlunoxn-TG-8qVkzFlT5RVBqIeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2455db6e15.mp4?token=R_fsjTWRTDn6Ee2ikDyXifV04STpaY9k6W832m3NtdRVxd_pE8mK2u51c8F1rT2SisAACkG51OiTsb5WbSbcLPqu0d1lvBZ905_c0toBCLms0vX1MsSK39VEIkHZp9W6tflI0CmH-_SVcIMUw88bj0wwR1B0stgxY2EGvIVQ7u-pjMSbAOtO-Buewc-PB2WatywYjS02HIjE1j7A243mJhDgH0lUVUIP6zev4RkexRBtCSK84xawTWAHIsXSxUYpgZERWeSQpQf8MBVTDYOn5qq7wQd9CDKEGcowu3DUYfxKa9vB2by3kXr1uxMvlunoxn-TG-8qVkzFlT5RVBqIeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهر لو پورژ در فرانسه در آتش سوخت و این حادثه جنجال بزرگی را بر انگیخت
🔹
۱۸۵ خانه در لو پورژ سوختند و ۳۴٠٠ نفر از ساکنان بی‌خانمان شده و همه اموال خود را از دست دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/676570" target="_blank">📅 08:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676569">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
کشورهایی که در کمک به متجاوز دخالت دارند، اگر رفتار خود را اصلاح نکنند، پاسخ سختی دریافت خواهند کرد
روابط عمومی سپاه:
🔹
شب گذشته دو تانکر نفتکش با تحریک پرنده‌های آمریکایی قصد خروج از مسیر ناایمن جنوب تنگه هرمز را داشتند که پس از وقوع حریق شدید در یکی از آنها هر دو شناور با سرعت به عقب برگشتند.
🔹
کشورهایی که در کمک به متجاوز دخالت دارند، اگر رفتار خود را اصلاح نکنند، پاسخ سختی دریافت خواهند کرد.
🔹
تنگه هرمز تا زمانی که زیاده گویی ها و تهدیدات مقامات آمریکایی و دخالات آنها در حرکات دریایی در منطقه وجود دارد، قابل بازگشایی نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/676569" target="_blank">📅 08:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676567">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a211f83490.mp4?token=IkqamzEutath2UZ6zKC73dXy9u6tOSaQ-6LIX0UdkJEAzF8e3XhnHqArzvr-TEm9sKj7pWByJW0JSj5MgLy1hpQ21ojA5yw0LZGnXYLLzwb5xWzOAJGbuxwlnFgbi58_IfxP0M0r9DPo1kNw-y1NfEsyvMJAF9CT0vDxMd0gqhnh4EwC5FZLgUdTrAhwcDDOt-c1XiMalEPc-d1UXmN3SSMEVu8I4r69XWifKjcY4ZxpoMH68-twdDms2zzKhTLMlsURrJJP87OzmOeszI8vhip3uapMsRJR0e-mIDxhbDVrRBH66vUXUNnX34cDu65_CN8GLgZkDtMD57UM8cBeXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a211f83490.mp4?token=IkqamzEutath2UZ6zKC73dXy9u6tOSaQ-6LIX0UdkJEAzF8e3XhnHqArzvr-TEm9sKj7pWByJW0JSj5MgLy1hpQ21ojA5yw0LZGnXYLLzwb5xWzOAJGbuxwlnFgbi58_IfxP0M0r9DPo1kNw-y1NfEsyvMJAF9CT0vDxMd0gqhnh4EwC5FZLgUdTrAhwcDDOt-c1XiMalEPc-d1UXmN3SSMEVu8I4r69XWifKjcY4ZxpoMH68-twdDms2zzKhTLMlsURrJJP87OzmOeszI8vhip3uapMsRJR0e-mIDxhbDVrRBH66vUXUNnX34cDu65_CN8GLgZkDtMD57UM8cBeXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از شلیک موشک‌های آمریکایی از خاک کویت به ایران
🔹
پایگاه عراقی المحورنیوز با انتشار تصاویری ویدیویی، از همدستی کویت و بحرین با آمریکایی‌ها در تجاوز به جمهوری اسلامی ایران خبر داد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/676567" target="_blank">📅 08:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676566">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
سه شهید و ۲ زخمی در حملۀ آمریکا به محله چاه تنگو شهر قشم
دانشگاه علوم پزشکی هرمزگان:
🔹
در حملۀ دشمن آمریکایی به منزل مسکونی در محلۀ چاه تنگو شهر قشم، پدر و مادر خانواده و یک کودک ۲ ساله به شهادت رسیدند و ۲ فرزند ۷ و ۹ ساله بر اثر این حملات زخمی شده و به بیمارستان منتقل شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/676566" target="_blank">📅 08:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676565">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TymzKJ3xsFVDglqbl_Vq5IM6cBdnTFM_9KpzRqpMJHTnVnMDe7GD_Mt1CBjczJUW5yML3-a3-Ukq-2PF2FwkHllGQURC8RACJTCVT34itK_11XVFb3YAbmtq4RqS7v7BKO_jzGn3nI4Ns4EzTz5YhDtAUz4uQEwfMbOnZEg8MGaTyB9Bi7s_u7ocT8ZibDn5Z22vbIv6D1bovSCWfJa_51pzk4TW9NTCYctX-HxaxUjJTHtgdwM41krg1Tbqd6MFMwjg1NvwFXUKGUubaYU60tNsXODykeC7ouRKRY1MvTyO6YHj1sSaoxi3qGM13ex8tFbQ3Yi23TIWgq77mCu0aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک تایمز: ترامپ با ایرانی مصمم‌تر در حالی روبه‌رو است که دامنه جنگ گسترش می‌یابد
🔹
با نمایش قدرت از سوی ایران، به نظر می‌رسد دونالد ترامپ بار دیگر در حال بررسی گزینه‌های نظامی است؛ این در حالی است که پیش‌تر طرح‌های تشدید درگیری را رد کرده بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/676565" target="_blank">📅 08:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676563">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8238f76942.mp4?token=jFuuRMY5HsVU5CQdary5KMoG6IPiiX0sKG873JLQ-gPBm4Zo5olXM2TDxg2s_jPk0a6NHLtfxZ8dkw0FXQTUTJX_gj4yKb8kWNDovnunwvj0SsO8zWxvbqLJPJA5YG0HHFCsnv9qmoWN9wwYm4RIEyhWVD4m8xdS-RmP2-cTHDj_y-hlt9zhm6i5ULJciIlNq8f7apGK7b_aC-PF8KEIB2J3CRl_azbytDsBOyi16a1-SuDRFeoX8b3Ui6cPG69GNfDa0Hbkn93ppucZrOak-SBjL56twYhWBvNo0droIrlz6SVbYyyrZGBsAnpKi7xocBpTPbk-lH7i4BFeLJJCQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8238f76942.mp4?token=jFuuRMY5HsVU5CQdary5KMoG6IPiiX0sKG873JLQ-gPBm4Zo5olXM2TDxg2s_jPk0a6NHLtfxZ8dkw0FXQTUTJX_gj4yKb8kWNDovnunwvj0SsO8zWxvbqLJPJA5YG0HHFCsnv9qmoWN9wwYm4RIEyhWVD4m8xdS-RmP2-cTHDj_y-hlt9zhm6i5ULJciIlNq8f7apGK7b_aC-PF8KEIB2J3CRl_azbytDsBOyi16a1-SuDRFeoX8b3Ui6cPG69GNfDa0Hbkn93ppucZrOak-SBjL56twYhWBvNo0droIrlz6SVbYyyrZGBsAnpKi7xocBpTPbk-lH7i4BFeLJJCQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر زانو درد، درد هنگام راه رفتن یا احساس ضعف در مفصل زانو دارید این ویدئو رو حتما ببینید #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/676563" target="_blank">📅 08:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676555">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISAVU7tg-OCLTHuxOTw7YqjjGbwJEJAqW4RwGmh6uIrJLiEXX4sp5qm-3QCHzLHxKhrJixv1QDj5nCBowHt5LbWnhl4gwGCalaV1-K9r3WHIY8tdWuNpAvYP6ZGf466MGPeySJ-NuQ8cUuj_BchB7-LX32pgeV39AiAezX4fpRp0visR2DkzKDGoqZMvcKekb8agAxbABY_EnsIDLE9lpUqz1wgqsLQgk3QC9-TDZCaT0jQPiPg9cBuKradIEXp1IG6wPOz-viZhG6FiPfPQkK5ebGtSeuSYnJBsVMTSGnLI7s4OyVNwuhDZlUbzPnNq6GyIW67CzDJmyNYJ_ffewg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز پنج‌شنبه
۸ مرداد ماه
۱۵ صفر ۱۴۴۸
۳۰ جولای ۲۰۲۶
پنج‌شنبه‌ها
#دعای_کمیل
بخوانیم
⬅️
متن و صوت دعای کمیل
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/676555" target="_blank">📅 07:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676553">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0654b37ac2.mp4?token=RjZArAHkyzeqw5Vjk6TyLcknrj90HJhW5q79hV4aoCXCGBzUyfx-ANE4t-e73POHMi7LdthHQHoCMiqMhMg-n9WNaDmjxhCEi3nTDoGtv2QAlhl62GIO7MeHCH-eVKlluDqUHDhZBKejQm0yYIwRveR4j1-OABQfJ6-KTPi7Zxa6qk2DRH4M5TK8qlwnCvMZ_6qLwJP0_cZiOHWZxG9-3EzK9POInoH-soVm7EFCVpgDy6c4HjydVioggZef4kSoa49HRQg1pVdnOaVHuFTe_jhBap0e5ACqfkDgY6tbWK8gdJrR7WkN1imrkiuqNZ8Ugnyk42levLwGaaGSHQvYQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0654b37ac2.mp4?token=RjZArAHkyzeqw5Vjk6TyLcknrj90HJhW5q79hV4aoCXCGBzUyfx-ANE4t-e73POHMi7LdthHQHoCMiqMhMg-n9WNaDmjxhCEi3nTDoGtv2QAlhl62GIO7MeHCH-eVKlluDqUHDhZBKejQm0yYIwRveR4j1-OABQfJ6-KTPi7Zxa6qk2DRH4M5TK8qlwnCvMZ_6qLwJP0_cZiOHWZxG9-3EzK9POInoH-soVm7EFCVpgDy6c4HjydVioggZef4kSoa49HRQg1pVdnOaVHuFTe_jhBap0e5ACqfkDgY6tbWK8gdJrR7WkN1imrkiuqNZ8Ugnyk42levLwGaaGSHQvYQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از شلیک موشک‌های آمریکایی از خاک کویت به ایران
🔹
پایگاه عراقی المحورنیوز با انتشار تصاویری ویدیویی، از همدستی کویت و بحرین با آمریکایی‌ها در تجاوز به جمهوری اسلامی ایران خبر داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/akhbarefori/676553" target="_blank">📅 06:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676551">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
اعلام پایان حملات امشب به ایران توسط سنتکام
ارتش آمریکا:
🔹
نیروهای سنتکام در پاسخ به حملات موشکی دیروز به نیروهای آمریکایی، موج سنگینی از حملات علیه ایران را با موفقیت به پایان رساندند».
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/akhbarefori/676551" target="_blank">📅 05:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676548">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
حملات تجاوزکارانه آمریکا به نقاطی در ایران
🔹
خبرنگار صهیونیست وبگاه «آکسیوس» بامداد پنجشنبه به نقل از یک مقام آمریکایی خبر داد: «ارتش آمریکا در حال انجام حملاتی به ایران است».
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/akhbarefori/676548" target="_blank">📅 05:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676542">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3995d7f98b.mp4?token=OxMl0uSdJWktnaSmJSq3jqOU1BkQjJPbFFurFUsgvfz2OivjpfdCz4v7GNOxvpyszsMOrHC764t7cfDLh-Bl12fa8hIlVPB67A9oD5EUhkNmxx6l0O0oqVVlKdHo4eMzdDYVnNnENU5qkypWxZV49eQLJZX8JU8X54_Qx9nif4tsW_DcfykjclnbBG-N3RsVS0fcssKxifEMXS4TjcUnE79IxHIAKC5kQoaZS5jUmtVuHAzixTZXfe-Mpb4qIfs30rRvswOqt3ZSzE2In8YhAeIHVbVhK3e6agS5PXdK-puZK0hG5zO1gPLpTXyJi8vcxUgfVzW8KXMvcHHO2bQcNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3995d7f98b.mp4?token=OxMl0uSdJWktnaSmJSq3jqOU1BkQjJPbFFurFUsgvfz2OivjpfdCz4v7GNOxvpyszsMOrHC764t7cfDLh-Bl12fa8hIlVPB67A9oD5EUhkNmxx6l0O0oqVVlKdHo4eMzdDYVnNnENU5qkypWxZV49eQLJZX8JU8X54_Qx9nif4tsW_DcfykjclnbBG-N3RsVS0fcssKxifEMXS4TjcUnE79IxHIAKC5kQoaZS5jUmtVuHAzixTZXfe-Mpb4qIfs30rRvswOqt3ZSzE2In8YhAeIHVbVhK3e6agS5PXdK-puZK0hG5zO1gPLpTXyJi8vcxUgfVzW8KXMvcHHO2bQcNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از حمله آمریکا به یک محله مسکونی در قشم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/akhbarefori/676542" target="_blank">📅 05:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676540">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d885c0805a.mp4?token=UFLjE_joQ3f8fQdNPcRD-5zUsNKTtzkpadWGy6rnXJU_7DaFzgErIeFqJ40WSTwUVr3EM-fBynBpMZqoLnBIyMo7NP2t3ytsiL5ttSwk4JZP6_Tb4IspRc814rgznlajLdWwzAn6m625vlhGyoOowNWhCyIklHF16rMMqbpC__GX0bKQoTIyvjiAgMEbnNpkP0GvDb7cM0MA4_hi8C37porzTP0I0i9yZxY9fXgPmeECkDQZ7aA2d7AxR4hm9u4TpsMk7eCeOM57yRJmqVJcqmEXRjmVUFidk6mQ6DQL4kmHHXKM-vsbGU3gPnN9HV132DmJB3Bt_JWilDza3E8B6nKd1JoTYY7ee7qEaQ8YKmUJPa_UxwrT-q38hsODwWwMgoojZMBFZMNzVipxY_SbTJSRFK1HG-4WbuhwMdQEEMDRNpyqDybNVVuKrfSVvEqi6FTVexUjwC02naaoX8JFsde_fXaU6lVl5s53so5cw9CKDpjK7Z0auIJWIOPjDiC_DM-zBHuCNqu5EmLJu1nPguy_FGxNz3kERMprAbH7sM8JQ8ZKElxZIAYLfmpzdgYFAV6UtT9Fl_fB3o1wouV1VyznZFE7ur_xtcBnBx27Zkom28JV572ifHCNAdrdlun7uMVXFJ8-nw2AX6Bw5QP3_wMPpjgSMKih7M6-anLnofI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d885c0805a.mp4?token=UFLjE_joQ3f8fQdNPcRD-5zUsNKTtzkpadWGy6rnXJU_7DaFzgErIeFqJ40WSTwUVr3EM-fBynBpMZqoLnBIyMo7NP2t3ytsiL5ttSwk4JZP6_Tb4IspRc814rgznlajLdWwzAn6m625vlhGyoOowNWhCyIklHF16rMMqbpC__GX0bKQoTIyvjiAgMEbnNpkP0GvDb7cM0MA4_hi8C37porzTP0I0i9yZxY9fXgPmeECkDQZ7aA2d7AxR4hm9u4TpsMk7eCeOM57yRJmqVJcqmEXRjmVUFidk6mQ6DQL4kmHHXKM-vsbGU3gPnN9HV132DmJB3Bt_JWilDza3E8B6nKd1JoTYY7ee7qEaQ8YKmUJPa_UxwrT-q38hsODwWwMgoojZMBFZMNzVipxY_SbTJSRFK1HG-4WbuhwMdQEEMDRNpyqDybNVVuKrfSVvEqi6FTVexUjwC02naaoX8JFsde_fXaU6lVl5s53so5cw9CKDpjK7Z0auIJWIOPjDiC_DM-zBHuCNqu5EmLJu1nPguy_FGxNz3kERMprAbH7sM8JQ8ZKElxZIAYLfmpzdgYFAV6UtT9Fl_fB3o1wouV1VyznZFE7ur_xtcBnBx27Zkom28JV572ifHCNAdrdlun7uMVXFJ8-nw2AX6Bw5QP3_wMPpjgSMKih7M6-anLnofI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون سیاسی، امنیتی و اجتماعی استانداری هرمزگان: حمله دشمن به یک منزل مسکونی در قشم، چاه‌تنگو؛ عملیات جست‌وجو برای یافتن دو نفر زیر آوار ادامه دارد./ تسنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/akhbarefori/676540" target="_blank">📅 05:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676538">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
انفجارهای مهیب و پیاپی در اهواز
🔹
دقایقی پیش صدای چندین انفجار شدید و وحشتناک در اهواز شنیده شد./جماران
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/akhbarefori/676538" target="_blank">📅 04:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676537">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01ec2c1ce5.mp4?token=WOpMpdOTqGsCgdF-mfGx36DGrWgAoGpp_b6pnjOTZxNBIwtpvQRq5t2une7VnjVMryOIIxYhzIRJs-JCePYf_BmdJZ0rHmeTPTGJ1CUeNrifv5W4rq0eDrXMPwdQRnWbN-O9623EzsuIJqG_0ijqoITK1z_CHtXKl_bl9rVOYB0_Y-Z07GqFNLYc3gFCfF2Hh368TB2fg1qUydQjjyMAgzKoa5_LW3SfAma41j-9OuafsXW1WKPfTfisjfcWT_IDPPL7Jc_F9OgvynbnwW7wTllywqBZ5bdEnVvyrprpi8ZapzNeR7xOnH9Qn79PerKGaxFs5laoB68n-0PJym6Tpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01ec2c1ce5.mp4?token=WOpMpdOTqGsCgdF-mfGx36DGrWgAoGpp_b6pnjOTZxNBIwtpvQRq5t2une7VnjVMryOIIxYhzIRJs-JCePYf_BmdJZ0rHmeTPTGJ1CUeNrifv5W4rq0eDrXMPwdQRnWbN-O9623EzsuIJqG_0ijqoITK1z_CHtXKl_bl9rVOYB0_Y-Z07GqFNLYc3gFCfF2Hh368TB2fg1qUydQjjyMAgzKoa5_LW3SfAma41j-9OuafsXW1WKPfTfisjfcWT_IDPPL7Jc_F9OgvynbnwW7wTllywqBZ5bdEnVvyrprpi8ZapzNeR7xOnH9Qn79PerKGaxFs5laoB68n-0PJym6Tpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادامه شلیک گسترده موشک‌های آمریکایی از خاک کویت به سمت ایران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/akhbarefori/676537" target="_blank">📅 04:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676535">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
معاون سیاسی، امنیتی و اجتماعی استانداری هرمزگان: حمله دشمن به یک منزل مسکونی در قشم، چاه‌تنگو؛ عملیات جست‌وجو برای یافتن دو نفر زیر آوار ادامه دارد
./ تسنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/akhbarefori/676535" target="_blank">📅 04:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676533">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
دقایقی پیش صدای چند انفجار در کیش به گوش رسید
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/akhbarefori/676533" target="_blank">📅 04:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676532">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در کازرون
🔹
منطقه‌ای در اطراف شهر کازرون هدف حمله دشمن آمریکایی قرار گرفته است.
🔹
اخبار تکمیلی متعاقبا‌ً اعلام می‌شود./ تسنیم
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/676532" target="_blank">📅 04:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676531">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
منابع محلی از شنیده شدن صدای چند انفجار در بوشهر و بندر عباس خبر می‌دهند ./ همشهری
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/676531" target="_blank">📅 04:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676530">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5d49cdbe6.mp4?token=Rr5eC5o-VF8622374D51PvFRLNQFvxltCBIrOVaVy4xgWEUSKR0rVCS2iXaWyimaPpJDgT72TrahORPAaKJVaLsQTEy8c7lAFSdwTbCnDMTo3Bt5vMcv5JvrNOtE91rFVhyTDMcJkcAZLG_ZGXkWdYn97qFaPQjY5merHNp41J4ik6nWbK4_8WtKaGEJ7phobEZupNHInmQfYRPIk1ajb6FlZQHTVdCRJnPAeiP43nDDaONJjP7ynhvMNJaFi1X9CV1oDCoWiB09HklRGYfAHl7b0VLwcOW8xwPWelcvoqvuoKLTI8_HSSjoevKBvsahTOnXUMd4EdZ0tftnA59A-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5d49cdbe6.mp4?token=Rr5eC5o-VF8622374D51PvFRLNQFvxltCBIrOVaVy4xgWEUSKR0rVCS2iXaWyimaPpJDgT72TrahORPAaKJVaLsQTEy8c7lAFSdwTbCnDMTo3Bt5vMcv5JvrNOtE91rFVhyTDMcJkcAZLG_ZGXkWdYn97qFaPQjY5merHNp41J4ik6nWbK4_8WtKaGEJ7phobEZupNHInmQfYRPIk1ajb6FlZQHTVdCRJnPAeiP43nDDaONJjP7ynhvMNJaFi1X9CV1oDCoWiB09HklRGYfAHl7b0VLwcOW8xwPWelcvoqvuoKLTI8_HSSjoevKBvsahTOnXUMd4EdZ0tftnA59A-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تکمیلی/
همدستی دولت کویت در تجاوز آمریکا به ایران
🔹
شلیک سامانه‌های موشکی آمریکایی از خاک کویت به نقاطی در ایران همچنان ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/676530" target="_blank">📅 04:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676526">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca5fc7618d.mp4?token=EJI0pmaQjhGoLB7r7h6xZOTlS-5dGsKvwLw1w1s3Kk9lFMexAQ3e6He42glzs3kfd9_dcwnN1gqv0EM3v23sNNRPEqnPG22LR8-NkkqgneZdjuqd5uVHUeS9cMJ4FeEdNIHHR_fX4pDD9AhLWo3zyGkNUPn_fxNwX6HFG7h9GZY-fGr_332F5-7R-7U4cSWctfHIJC1xZhnoLOENWJpxuCby-uYsOqh2-wjeO0tES434bSM7yf4R5NhvVRmZ5SmQCLEpjEAUWUoH8k9CLYfzESXgMANBx2zsTdz0GKaa_jZwrcKbdl6XdViHTHRUpTrcw8eTS0KIzhfFaAxL0aN6GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca5fc7618d.mp4?token=EJI0pmaQjhGoLB7r7h6xZOTlS-5dGsKvwLw1w1s3Kk9lFMexAQ3e6He42glzs3kfd9_dcwnN1gqv0EM3v23sNNRPEqnPG22LR8-NkkqgneZdjuqd5uVHUeS9cMJ4FeEdNIHHR_fX4pDD9AhLWo3zyGkNUPn_fxNwX6HFG7h9GZY-fGr_332F5-7R-7U4cSWctfHIJC1xZhnoLOENWJpxuCby-uYsOqh2-wjeO0tES434bSM7yf4R5NhvVRmZ5SmQCLEpjEAUWUoH8k9CLYfzESXgMANBx2zsTdz0GKaa_jZwrcKbdl6XdViHTHRUpTrcw8eTS0KIzhfFaAxL0aN6GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در اطراف بندرعباس
اژدهایی خبرنگار صداوسیما:
🔹
گزارش‌هایی از شنیده شدن صداهای مشابه در جزایر بوموسی و کیش و همچنین محدوده دریایی قشم و تنگه هرمز منتشر شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/676526" target="_blank">📅 04:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676523">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09e2d8b313.mp4?token=Zu7yYkbm2xny-YVsgZGsheTSkMWCSe5ft4wLXRVDkkKraT_I7ktvCcmzd7d1GObd1jUnFMfTYMzfkFQV3BN3Fzpjg_TWJYe21QE-N4DOWwrbr91y2WJWsy4NCtHgytunmAitBv4_eYkSAVLFDDLIp9lhiVj_BAD1HCTPXGrLNu7mPgAehqzCva4FhZ9Rn2itr49KxF8Qavcil3kVwgyz5ZsIZhD1qb4Wk-zmOis9WCwWZ2uhfWAWbYWmvlZDPWX2zDaLTUa2Hp7t_Z62jiNEmantSFWLB5A47Tvn3IYoCDemFl_O_-MhzkCx48ao1bbeYvf3dcDltoSFFkYDbqRUgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09e2d8b313.mp4?token=Zu7yYkbm2xny-YVsgZGsheTSkMWCSe5ft4wLXRVDkkKraT_I7ktvCcmzd7d1GObd1jUnFMfTYMzfkFQV3BN3Fzpjg_TWJYe21QE-N4DOWwrbr91y2WJWsy4NCtHgytunmAitBv4_eYkSAVLFDDLIp9lhiVj_BAD1HCTPXGrLNu7mPgAehqzCva4FhZ9Rn2itr49KxF8Qavcil3kVwgyz5ZsIZhD1qb4Wk-zmOis9WCwWZ2uhfWAWbYWmvlZDPWX2zDaLTUa2Hp7t_Z62jiNEmantSFWLB5A47Tvn3IYoCDemFl_O_-MhzkCx48ao1bbeYvf3dcDltoSFFkYDbqRUgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شلیک موشک‌های هیمارس از کویت به سمت ایران
🔹
منابع عربی تصاویری از شلیک موشک‌های زمین به زمین هیمارس از خاک کویت به سمت ایران منتشر کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/akhbarefori/676523" target="_blank">📅 03:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676522">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
گزارش‌هایی مبنی بر وقوع انفجار در آبادان و کیش./ همشهری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/akhbarefori/676522" target="_blank">📅 03:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676521">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
گزارش‌هایی مبنی بر وقوع انفجار در آبادان و کیش./ همشهری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/akhbarefori/676521" target="_blank">📅 03:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676520">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f1001d1ab.mp4?token=ruIE9BPuDxK7Fudr9w9lbu3J7glEVeleERlCOfjaJavvvkQKnxK103MkLogbFm6rDyr4OzdAmTrRy4kie7n5s6SbVAGI-UZaGd40kzOmTqEA1Txulz2Erjna7qpOf1iFt90wokOtP7OGQJpP5b9xCNRag1TVhmYApJ3fxPq4DqB73xQ6ysmKXIK3PHguayakbyt8kmC1pOjnnUJTKE7pCTgfYKiQRKOVX8LJp_juNPOhCBN5IqvW9rw1Y1sJG-ra6UCHuXDOdP3rLR0a-K-GVwUedvVeE_MxHhGeP3E048J21taadlxb1kU_1Eqw0FG_CrnlJHEuDgjvP9fFbSC-NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f1001d1ab.mp4?token=ruIE9BPuDxK7Fudr9w9lbu3J7glEVeleERlCOfjaJavvvkQKnxK103MkLogbFm6rDyr4OzdAmTrRy4kie7n5s6SbVAGI-UZaGd40kzOmTqEA1Txulz2Erjna7qpOf1iFt90wokOtP7OGQJpP5b9xCNRag1TVhmYApJ3fxPq4DqB73xQ6ysmKXIK3PHguayakbyt8kmC1pOjnnUJTKE7pCTgfYKiQRKOVX8LJp_juNPOhCBN5IqvW9rw1Y1sJG-ra6UCHuXDOdP3rLR0a-K-GVwUedvVeE_MxHhGeP3E048J21taadlxb1kU_1Eqw0FG_CrnlJHEuDgjvP9fFbSC-NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش‌ها درباره شلیک موشک از کویت به ایران
🔹
رسانه‌های عربی از جمله «صابرین‌نیوز» با انتشار تصاویری گزارش دادند که سامانه‌های موشکی تاکتیکی ارتش آمریکا از خاک کویت به سمت آبادان شلیک کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/akhbarefori/676520" target="_blank">📅 03:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676519">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
حملات تجاوزکارانه آمریکا به نقاطی در ایران
🔹
خبرنگار صهیونیست وبگاه «آکسیوس» بامداد پنجشنبه به نقل از یک مقام آمریکایی خبر داد: «ارتش آمریکا در حال انجام حملاتی به ایران است».
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/akhbarefori/676519" target="_blank">📅 02:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676518">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
پیشنهاد سنتکام به ترامپ برای حملات دو هفته‌ای به ایران
نشریۀ وال‌استریت ژورنال:
🔹
فرماندۀ سازمان تروریستی سنتکام طرحی را به رئیس‌جمهور آمریکا پیشنهاد داده که ذیل آن، تا دو هفته به زیرساخت‌های موشکی ایران حمله شود.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/akhbarefori/676518" target="_blank">📅 02:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676517">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
چند انفجار شدید اربیل عراق را لرزاند
🔹
به گزارش، شبکه اخبار عراق اعلام کرد که پس از شنیده شدن صدای این انفجارها، ستون‌های آتش و دود از منطقه قسری در اربیل به آسمان برخاسته است.
🔹
براساس اعلام رسانه‌های عراقی، هم اکنون سامانه‌های پدافندی کنسولگری آمریکا در اربیل نیز فعال شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/akhbarefori/676517" target="_blank">📅 01:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676516">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjCXb3aBdhceoPe6i5T6J3xziAt5H5mCgR6NPiKgVVn16GH_Ziz5DTrqR9K1ifbtXdc3bQ0YNKcexeYldy6Zc1gVzfXr81o9gRMoCXQ6lZDdwKGtSdVHoEjO4WrO1dbjnemhBEwe-LwM-SYZGwKdYNunIfNNGuhTKLcSjL0aLUD4CegXl-AGDRG_t148GrlDhyYTuEVDhZ3XU7FzgTUpwHbxA8UG5YD8mbDX__vK7ksqIquraCViFmlWyD3gHkiM-2bsav0mMuW03x8XtuamRUhWR0pFrNlAZt0Pl4eRLx_1ZKgJyayBQj36oy1-6UKgZM1I1F8c2pUZ_yfJIZ8jGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر فروشگاه آنلاین داری، این پست می‌تواند هزینه تولید محتوایت را نصف کند.
قبلاً برای هر محصول باید:
❌
عکاس می‌گرفتی
❌
لوکیشن پیدا می‌کردی
❌
ساعت‌ها زمان صرف می‌کردی
حالا کافی است یک عکس ساده با موبایل بگیری…
رقبایت دیر یا زود از این ابزارها استفاده می‌کنند؛ سؤال این است که تو زودتر شروع می‌کنی یا دیرتر؟
@digitall_cast
ارتباط با پشتیبان :
@Digital_cast_support</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/akhbarefori/676516" target="_blank">📅 01:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676515">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a98Y-UX7SNllfACX9ACm2f0_zK-K93mwjkjX--N3f3Y2ypAKyX_-xl8be4qyDlY0RtEBQswBrdCvBT2HbyeoByPCTkeUhabZsmHA2fMzWu4QrYwTup_9f2SNLbXoAolhsBtvE_31aqtW3nQSqDLApwpb9AhPSv-kS_JsO5Jxd_ADvEfIHoNAYWLqUu5nxtOyoWyIU00Zb_g1NMVYUKHaFMefSw-fOH2_M7kWZxIsF2rOgfDlA0rI5MV0vStYIdaQRu489jJy8tGJFB7vSHIWmsOrEGw6OkGNdqIUr9dn4tV3RfbBA3rVTSkvsPxWO_ztzYS8iEOXC50PufV6lNlKnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بسیاری از هواپیماها در خارج از فرودگاه ریاض در عربستان سعودی متوقف شده و فرود نمی‌آیند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/akhbarefori/676515" target="_blank">📅 01:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676514">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKXPOaRheJO9ckjHz5e_G_JBI02DGQ8OD94wU6FpMJFmlpXzMW_N1Y3hvcegzszomiHvdWa8Ynuu2sg16ESrSGeK-FRT2jtVmp2o79Mxgxx_audp0OTwIOBnI3awc0eymfI9PyX4YxllXmUdKfgZySpLMPHQffn0L4myFan1P9irPlVpEtldCibtfZ4QjWR3Lo052mt3nm-em0zNAcDAHqUfv8UZtItmIRD8k7F7FLTNIQv2IU00XogIKlHFezDlFYStaR5FMbhvWIMZkde8bkRPkZg93Z9SgM8_IIGRZ6s6V_BJQM0k8s4ej_YE59qhkAMHdVDSL6GAHfkpJrtAVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعلیق فعالیت فرودگاه «ملک خالد» در ریاض
🔹
منابع عربی می‌گویند که فرودگاه بین‌المللی ملک خالد در پایتخت عربستان سعودی، بعد از شنیده‌شدن صدای انفجارها در ریاض، موقتاً بسته شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/akhbarefori/676514" target="_blank">📅 01:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676513">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
گزارش‌ها از وقوع انفجار در ریاض
رسانه عراقی «نایا»:
🔹
صدای دو انفجار نامشخص، به وضوح در ریاض، پایتخت عربستان سعودی، شنیده شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/akhbarefori/676513" target="_blank">📅 01:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676511">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
روزنامه وال‌ استریت ژورنال به نقل از یک مقام دولت آمریکا ادعا کرد که
دونالد ترامپ همچنان در حال بررسی گزینه‌های خود است و هنوز تعیین نکرده که حمله به ایران در کجا و با چه شدتی انجام شود
/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/akhbarefori/676511" target="_blank">📅 00:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676510">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
ترور ناجوانمردانه در شهرستان ایرانشهر
مرکز اطلاع رسانی پلیس سیستان و بلوچستان:
🔹
ساعتی قبل افرادی مسلح به سمت مأمور انتظامی در ایرانشهر با سلاح گرم تیراندازی که متأسفانه استواریکم "مهران سالارزاده" به درجه رفیع شهادت نائل شد.
🔹
تلاش برای دستگیری عاملان این سوء قصد ادامه دارد و اخبار تکمیلی متعاقبا اطلاع رسانی خواهد شد./مهر
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/akhbarefori/676510" target="_blank">📅 00:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676509">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d3c2975d3.mp4?token=E_0CTGRypleKqo-HQQhYYVd8jI0nBioL1ZsdNpwZIDNfYvUPOMO9r0anOHCktcV0Bj8OcrTkRlPrEylgdxvmIs6xeT2NXbdD2WKKllck5iu0jz7byx8trNmzph-ZLp-xoRuQreXGsZcEiJDuu3dym0TF4qTsw_5ESNMnmvYXSoFMZv5haTibtSJ7-Ser16KDS_bvDppUhNWovToMW3qCzwYC5dOYrQ-I8XY9sbqGuR5L9bKv9nDGZ7U1-ZkORZBMSowSX0yGyHDN31iLgU8bcX7HhNHCbHxlBnVq7PY0MK_663n6KlX1taJkKr0WK-ggvZ-98xv42sBU-4ZOS-Fnyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d3c2975d3.mp4?token=E_0CTGRypleKqo-HQQhYYVd8jI0nBioL1ZsdNpwZIDNfYvUPOMO9r0anOHCktcV0Bj8OcrTkRlPrEylgdxvmIs6xeT2NXbdD2WKKllck5iu0jz7byx8trNmzph-ZLp-xoRuQreXGsZcEiJDuu3dym0TF4qTsw_5ESNMnmvYXSoFMZv5haTibtSJ7-Ser16KDS_bvDppUhNWovToMW3qCzwYC5dOYrQ-I8XY9sbqGuR5L9bKv9nDGZ7U1-ZkORZBMSowSX0yGyHDN31iLgU8bcX7HhNHCbHxlBnVq7PY0MK_663n6KlX1taJkKr0WK-ggvZ-98xv42sBU-4ZOS-Fnyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بین‌الحرمین میزبان زائرین پرشور و عاشق اربعینی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/akhbarefori/676509" target="_blank">📅 00:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676508">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b1a77561e.mp4?token=cEqltR7L2jKL37zBPJKVAUjYdtzs7oWSEbuYGFFqX6HBuKIAupl5GoVD3ZuKFBjBdUrtAnmBMhxRQw9o-SXDXNeUMSq6hyMNjN6N_-N4X_V_TtHVewPxUBkWCf4DoKCK2RjOcgeg2y43wJwm2bGqElnp68b6KCmZM4MerZKuDXWK_83zAFCXwBrvDQdyw5M3iI4ym0-v8vE01rRY9Cqn2r98IE_4F6s0Mp7RwNw2DAyE95qPXWEzbCVTt3MtxXV0zi3rc1dx9a5WhAr0VqnyKCdFuPDRuftjhgvreg4AuDLwe7EfVwMF1tkeR_mjweZlcsyiLr7ivADvcpX448fRcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b1a77561e.mp4?token=cEqltR7L2jKL37zBPJKVAUjYdtzs7oWSEbuYGFFqX6HBuKIAupl5GoVD3ZuKFBjBdUrtAnmBMhxRQw9o-SXDXNeUMSq6hyMNjN6N_-N4X_V_TtHVewPxUBkWCf4DoKCK2RjOcgeg2y43wJwm2bGqElnp68b6KCmZM4MerZKuDXWK_83zAFCXwBrvDQdyw5M3iI4ym0-v8vE01rRY9Cqn2r98IE_4F6s0Mp7RwNw2DAyE95qPXWEzbCVTt3MtxXV0zi3rc1dx9a5WhAr0VqnyKCdFuPDRuftjhgvreg4AuDLwe7EfVwMF1tkeR_mjweZlcsyiLr7ivADvcpX448fRcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک شهاب سنگ آتشین عظیم در آسمان نیوزیلند مشاهده شد
🔹
مردم محلی می‌گویند: «شب هوا کاملاً صاف بود... و ثانیه‌ای بعد، یک چیز بزرگ، شعله‌ور و آتشین در آسمان ظاهر شد.»
🔹
کارشناسان معتقدند که ممکن است بخش‌هایی از این شهاب سنگ به زمین سقوط کرده باشد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/akhbarefori/676508" target="_blank">📅 00:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676507">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SiDJwnQQe0jqGj5n6ToTF7-TS4_Zn_B9cvcyFcT_KMmNgkfyA6tMznRiqPs5XhqvezbnEq2MqtDfXyAzmsX7TQ9xVLyTqpr_vUQ3DqnqBjTGVhpSHi7d1wJDJeebukVJqknxJorl9NQNBU_p3pwlD7lAEBmDGTNwNo0ohYy4Esd5w7lIhdbaCIIvvXQ8VMBB2LNzX_rzOg73AaANjc8WnoGbTFmbdLYmrXKiGLNYgPuxsgktd8v4E7XdLMoDOW6S9yZR8x0RMyGp6WSA-Z_SCdNs5z43gsg85pQCT-T8gVLybvE_nYNeWKmTtuRx9JpUMVXPIPZalHGon-WCVENWYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/676507" target="_blank">📅 00:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676506">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IoZ-jaDt1CwyGp6hTxjdqycheM1Xrj0LzH_plazGLAwaO14XYiz8ij6wCgEpaZwh6UQLC94uYtL1h8RNTVM9AMgA3aJbOCV_uApb_TOIV-aQuNAPTgjTDmEDU_t1oQbtwD9YTZbDC6ghdhWSKIFOymAwR30Tw6gxKcDMKSJHyArHf4E2Nzffq8RxN5mXEhXBVFSvBQWhOtgyB0IKcIvo5hjFTW7Q1xBTrBNH95ax0azd7IpzFRueN06bwDZHVO9QcuYwhM55CPu1N1uHkFyWv-iZeBoGQulsqQHTddrJKe5MpCg2SGqLfoEx8dO6NLhRQkQXVSIYJPUDPa_x3C908Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پشت پرده حمله به عراق/ پروژه مرموز «اختاپوس» توسط موساد فعال شد؟
🔹
درگیری شب گذشته در یک زمان بسیار حساس رخ داد. آنطور که کاظمی قمی، سفیر پیشین ‌ایران ‌در عراق گفته است: حمله به عراق، آن‌هم در آستانه سفر نخست ‌وزیر این کشور به عربستان، نشان می ‌‌دهد، دستی در کار است تا جنگ منطقه‌ ای را تشدید کند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3234193</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/akhbarefori/676506" target="_blank">📅 23:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676505">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9oW2gikRqE4R2Ti5hXJhZY4wIJTyfgc1TFKJAwEWoUxQRGBzEhMeAMLLAKa3Fn7jAh_O6BTQhWF46JYzIsASnWsNriEDNnvmoJGWZT4dyVsIxP_c1Qdyy15lKd3PNgxv6VQzxCIlzYGRv8MlrL-YgtY7y0SlW_uEDB4Kq1YhiZEK6d-La3tMvdRWiJ_3DWQxDTH-NZr4zk3rMwZ37WN6JH7Pnp05ziZDcuHMmGiBpiwFSrUzZbV8QJhdylxGxBLwfPTBFI_rwYZrXWid212GX2bMaekLDlVNnuNkJB8P2RSA-43pQSM4HUbs2z4Y1ZjRbLKGzEjh_vzScSrs7KwPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترکیب جمعیت عربستان و همسایگان؛ چالش‌های پیش روی ریاض
🔹
عربستان با ۳۵ میلیون جمعیت، میزبان ۱۸ میلیون مهاجر پاکستانی، بنگلادشی، هندی و مصری است و از ۱۷ میلیون شهروند سعودی، بخش بزرگی شیعیان هستند که از سیاستهای آل سعود ناراضی‌اند.
🔹
این در حالی است که عراق ۵۰ میلیون و یمن ۴۳ میلیون جمعیت دارند؛ رقمی که موازنه منطقه‌ای را تحت تأثیر قرار داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/akhbarefori/676505" target="_blank">📅 23:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676504">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
‏
معاون سابق وزیر جنگ آمریکا: نتانیاهو با کارت اپستین، با ترامپ بازی می‌کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/akhbarefori/676504" target="_blank">📅 23:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676503">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔹
داغ‌ترین خبرها را هر لحظه در وبسایت خبرفوری دنبال کنید
🔹
🔹
پشت پرده حمله به عراق/ پروژه مرموز «اختاپوس» توسط موساد فعال شد؟
👇
khabarfoori.com/fa/tiny/news-3234193
🔹
ترامپ در مواجهه با رضا پهلوی در مراسم خاکسپاری لیندسی گراهام چه کرد؟ / ویدئو
👇
khabarfoori.com/fa/tiny/news-3233989
🔹
موشک‌ های ایرانی، همسر دوم مرد اردنی را لو داد
👇
khabarfoori.com/fa/tiny/news-3233917
🔹
خواننده پاپ برای همیشه از ایران رفت
👇
khabarfoori.com/fa/tiny/news-3233955
🔹
خروج پردردسر علی دایی از مراسم بزرگداشت اکبر عبدی
👇
khabarfoori.com/fa/tiny/news-3234155
🔹
برای اطلاع از تازه‌ترین خبرها، اپلیکیشن خبرفوری را نصب کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/akhbarefori/676503" target="_blank">📅 23:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676502">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UL5ejQ_wW5R4QSbKZUQ27s4RVbPU8XS5ZE8HqLzA3rtCLDJmuNV3ZKpl4QjRGLaPvImn0c3CYhXK-bpyzeXG4bxNB-fCVxo0GGLDsiYZazj2N3wXfEyvS-Qhn-CG__W1Tym5AFPFHRpcraKgAzkmWK9l8aSD6ZqAAvKlIujm2q731Gc5B9uyPtL_gsVLjJkEEy0aK5zCEYiFCSlgObmLfcDAIBifDw4gRpAVyZ-Mn8xhzApK0zXzvALopc2yp0uIbEXNtuez_1Kg_R7nrnYG5LJYTOZzOEbRPf1F0qDfiFaCwM8zt6uWsDIjmeMzqBXz9Qu1EAzunwLpXORpenJO6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سندرز، سناتور آمریکایی: ترامپ گفت که هزینه دارو را ۱۵۰۰ درصد کاهش خواهد داد، دروغ گفت
🔹
دولت او در حال پایان دادن به برنامه یارانه مدیکر است که هزینه‌های تجویز دارو را برای حدود ۲۵ میلیون سالمند افزایش می‌دهد.
🔹
شرم‌آور است. ما باید هزینه‌های داروهای تجویزی را کاهش دهیم، نه اینکه آنها را افزایش دهیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/akhbarefori/676502" target="_blank">📅 23:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676501">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/haOQYjdDf18YzzjBh4tiOZL3eLsqS1z3edfbUXpe7gpeucCkqRG2TiVfou7FfBMpNAyvWtZE4xUsNWPX6Mu5qlyfnGvVr7nEpHv6DIVPqLDFKcKX9i4snJT1-VN8wJ8_SlHSiuxAcFtLlhdXFrZQv-YCLxTAhsDc-QXek3SfrdC4avRFnZweqymyYDc3j1D6u6WlNZG5lnQJwKufYquEAD6RJ7u-GjlTi-s0IIKg0DNULM3N5oWAsNjJypy4qnbKRIskX8BDD3Jim3S2JVWr4ocCVyWZRM-9ZZLpdg2FG8aORLcrZBvGAxIyY0nz-pGU3ni5lOOUDNGlbc8Q8hU4Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیمی از انگلستان اسیر خشکسالی شده است
🔹
دولت انگلیس اعلام کرد به دلیل«بارش کم سابقه باران و دمای بسیار بالا»، بیش از نیمی از انگلستان دچار خشکسالی شده است.
🔹
این کشور چهارمین موج گرمای گسترده خود در سال ۲۰۲۶ را تجربه می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/akhbarefori/676501" target="_blank">📅 23:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676499">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/etCPak3J73XC0u1gjcB1IunHN06UgloG-_a26doGLHnHoYsN7agBP_y1witMrGZDrtN0-cT6LEz7Y8jZbrzzR21dY8qvQnkpnChQi1KfTp_BSC2UtWiMPd1ESTJOz737MHk0GPUgZG7cB4G674Y8aP2bHDC5SFrJZOF1-o0htKQ0W0jWMEjAWIc6BSY--uULRWA3hbGooN83i2w2cocpyUqxMQ0JYgxcqxs41GNekm2BEF6ODfV3LNF5CRG7OhS1nJ5rA4FEj459pg0AJOWoe3Fv2g_66JGif9qkr7YlDgOyob7KjRmJZRv2oA2idCATk0dwvFYuEBesepvzrO2R9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D_5hd69tYU3adUPXbT8qcos4Y80Jo2P33jM140eA4cAe6duyk0M_Zvyy8dQutFDfpCTKLS39OGKqs_H43KgGbOhXc018wH-8ThGcDX4GisCQhNWrS4vYbQQia-2_v3Lf8gDK1OyNzrW_Va-z-dwD2p7cGjVrYWHIzwIuHFif1pM1_w1OVpZB_dJNrn4xOiJPQt8L7a0qYkWAdmaOq0yHRyJRphkQS1GKmMN07nXalCkVUPWTYAfsjVpRnfyQtqcHk4O7AOGjGzUZKpVlNI5XnBDH7qzq0fuZ0cWDslgZJB76Q6GCRiKPUm1cLLYwYg7bLBy7CDpC2xkjMVkfX87Yvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر برای تربیت دینی نوجوان خود چالش دارید، این کتاب را به فرزندانتان هدیه دهید
🔹
«نامه‌های بلوغ» میراث فکری و تربیتی اندیشمند بزرگ، علی صفایی حائری برای همه جوانانی است که در آستانه انتخاب‌های سرنوشت‌ساز زندگی ایستاده‌اند. او با زبانی صمیمی و عمیق، از بحران‌های…</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/akhbarefori/676499" target="_blank">📅 23:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676498">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9tqzqniFBkhfTeoZUcDnLf-PmcAQ9gFAGcjEDDHiJIN_l2mzxWoRxpFfOijyUOMqc_J5frVGmu1VWTXMYCNnM5oQa2ku5r5y__6MZQ3wZMEHttt_0V_2G_FsJoSErQ1PTRZYVgyoYT4cpNQTwO0EUhCt4qBOd4T5POu5-D7U1YCf4-9BdpIe7KWgdkocQqqwWadMFUh7Ijm1QVW835GaJ957t2xlsOS8bdCBjaTaz0rsUde7xHvAAFrdKpCmfcTr7nx_3WVIxJolNrxr3tx_t4Uj_xHgdRlst6blyoPGnSgO0kW2wDoOOfzo5Q-OXILnBG7b4a2Yw8DBFgLwlT87A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واگذاری هفت تپه متوقف شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/akhbarefori/676498" target="_blank">📅 23:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676497">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یاوه‌گویی خوک زرد: نوبت ما است که ایران را بزنیم
ترامپ:
🔹
‌آنها را بسیار شدید خواهیم زد چون نوبت ما است که آنها را بزنیم. می‌دانند که حمله در راه است. از ما درخواست می‌کنند که این کار را انجام ندهیم.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/akhbarefori/676497" target="_blank">📅 23:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676494">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70a062f9cc.mp4?token=KRV-QNuQRdukYSHUWIpsvdriBUckijCkr9AfwIUZ-cVLFt6knKdHXj7mtQP9crhlVKNXunxpi_mAAeiRRCXGQbPahiZm3KLAqZ6gGfjXspF-mtxo0-lFAaz-Kjn9C93iWJ4kwuviqxO5DL93S5q-2VywwB7Ua4SCUfJGUu5-9JVwto41jLW_4x-ah5Ncl5kFGlDiGgJ-N2oCUI0mucZ-kxQvCUKyvG-T-yXmdNlGMHlK8YXwvZ-S-F-IRD77FC5mQ2HqDE4VQDMvzgNjs8j2D_laQVE6h8q9YWOQWaZbyesfy4FGz363GpyMLy2gOtat63_9z3DzCTlg7F1tTepzVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70a062f9cc.mp4?token=KRV-QNuQRdukYSHUWIpsvdriBUckijCkr9AfwIUZ-cVLFt6knKdHXj7mtQP9crhlVKNXunxpi_mAAeiRRCXGQbPahiZm3KLAqZ6gGfjXspF-mtxo0-lFAaz-Kjn9C93iWJ4kwuviqxO5DL93S5q-2VywwB7Ua4SCUfJGUu5-9JVwto41jLW_4x-ah5Ncl5kFGlDiGgJ-N2oCUI0mucZ-kxQvCUKyvG-T-yXmdNlGMHlK8YXwvZ-S-F-IRD77FC5mQ2HqDE4VQDMvzgNjs8j2D_laQVE6h8q9YWOQWaZbyesfy4FGz363GpyMLy2gOtat63_9z3DzCTlg7F1tTepzVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎦
قبل از حرکت، مسیرت را هوشمندانه انتخاب کن
🔹
در سفر اربعین، انتخاب مسیر مناسب می‌تواند زمان سفر را کاهش دهد، از ترافیک و ازدحام جلوگیری کند و سفری ایمن‌تر و آرام‌تر برای شما رقم بزند.
🔹
با مراجعه به سامانه ۱۴۱، مسیرهای مختلف را بر اساس آخرین وضعیت تردد، ترافیک و شرایط جاده‌ها مقایسه کنید و با آگاهی بیشتر، بهترین مسیر را برای رسیدن به مرز انتخاب کنید.
🔹
برای اینکه بهترین مسیر را انتخاب کنی، بیا ۱۴۱
#چشم_به_راهیم
#اربعین
#سامانه141
#انتخاب_بهترین_مسیر
#سفر_ایمن
#مدیریت_سفر
#سازمان_راهداری_و_حمل_ونقل_جاده_ای
#حمل_ونقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/akhbarefori/676494" target="_blank">📅 23:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676492">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
احراز سن کاربران شبکه‌های اجتماعی از سال ۲۰۲۷ در نیویورک اجباری می‌شود
🔹
از ژانویه ۲۰۲۷، احراز سن برای دسترسی به فیدهای الگوریتمی (مثل اینستاگرام و تیک‌تاک) و نوتیفیکیشن‌های شبانه در نیویورک اجباری می‌شود.
🔹
متخلفان تا ۵۰۰۰ دلار جریمه خواهند شد و کاربران زیر ۱۸ سال نیاز به رضایت والدین دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/akhbarefori/676492" target="_blank">📅 23:10 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
