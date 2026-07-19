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
<img src="https://cdn4.telesco.pe/file/XsC6sW3Ug4EOkokJQpk_lMnxVg9_YQ0I4pzD-VZsv1pRr7dvE1TahgD4Brr_EZbxf47ZbsGbKd6K3AgHnImN6wUt4VZ8nGqlOmHEzKTUptt3oEB0AKU-HeL5Y3YLeB2LZFRCGsSul7ZKgIuELS1FMsDvFADoh8vOcBlxewx5omDIpF3zoCBX5L24X2lIlHRzrauF6-Oy_y-TaId4HRaV0aZ_BhaWIQFaZfbWE-ppm8oatz-G-iUXwNWAN2EOByoXic-e4iwxL3e4J-yaM24SeLM9YrsMiMBJ1oDPCdQG5FNx56XGii6V83gZKJ4CIEfKrnDOWIzqkTakku2YyHnuVQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.27M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 08:44:01</div>
<hr>

<div class="tg-post" id="msg-672844">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
غریب‌آبادی: حاکمیت ایران بر تنگه هرمز غیرقابل‌مذاکره است
غریب‌آبادی با رد هرگونه مسیر جنوبی و مذاکره با آمریکا:
🔹
ایران مسئولیت مین‌زداییِ کل تنگه هرمز را بر عهده دارد و ضمن احترام به حاکمیت عمان، با هر هزینه‌ای از حاکمیت خود بر این آبراه دفاع خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7 · <a href="https://t.me/akhbarefori/672844" target="_blank">📅 08:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672843">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
زمین لرزه ۵ ریشتری سالند خوزستان را لرزاند  مدیرعامل هلال‌احمر خوزستان:
🔹
ساعت ۰۵:۵۵ امروز یکشنبه ٢۸تیرماه، زلزله‌ای به بزرگی ۵ ریشتر در عمق ۱۲ کیلومتری، سالند از خوزستان را لرزاند.  #اخبار_خوزستان در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/akhbarefori/672843" target="_blank">📅 08:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672842">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JR3Z62ef_0M3UnpZRNO3XFUX4m_E4YlruZFO7djk3zGfGORZZmAX0TdTlWyzyDy3WawyRGo267Lg51gE3bFB9vmOXSbCZvTL2Ex99g85VJndZEiq3JNIi2wtHQB6bsBp-OwSRgd4kizzA5LxK8fIkfHGAi7-UPqeoDjZAd_E4QzRVLj162xEMMubIhQ3dBJsDfC5flHsbv9hzd2ffK26mJrGSY0puVbu3va1ZbKuhMFRCX3GQZ2juEYjufH_DtsHYIuCWwNEXFN__0GwBi_afne9WjPSpr_GgZY23OjIovKutfsc9NUeenjpB2Fd5TmbSK5YriG1ZPiAolIX5gH7CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پارس‌خودرو هم محصولاتش را گران کرد
🔹
شرکت خودروسازی پارس‌خودرو فهرست جدید قیمت محصولاتش را اعلام کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/672842" target="_blank">📅 08:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672841">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/402fe3c51b.mp4?token=CkIoNMqr4ZrKd3oMduX71LZeEOr_0z7pUwvpFO1HufRb6SVOrrl_XdYAcD3dD9dOqQ8d9uax3elvOVx0kLZqprpNd8I2pYMhZxTucwExpkJ5r74-EQFmfckPM30vzQICSHZ7gzauzqMOucR_jnX3D5VGks1MWAZVJvrVZxn411PyDZfUD0cFSVHe649EPMsupyEOFptIn_G3WnWPwCa1UwhtUhh8kCXNtqj8a8HHiGpCV3jJ91nr2ec1aDNvMCSu1AoyHtPpHJ3V3DT0Rhqj-YWvw56n8rdl-gaa9KkOuOB4UwENMXzqFH7A4g4gT62LiaCSJpma5TO9xAZXoKG34g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/402fe3c51b.mp4?token=CkIoNMqr4ZrKd3oMduX71LZeEOr_0z7pUwvpFO1HufRb6SVOrrl_XdYAcD3dD9dOqQ8d9uax3elvOVx0kLZqprpNd8I2pYMhZxTucwExpkJ5r74-EQFmfckPM30vzQICSHZ7gzauzqMOucR_jnX3D5VGks1MWAZVJvrVZxn411PyDZfUD0cFSVHe649EPMsupyEOFptIn_G3WnWPwCa1UwhtUhh8kCXNtqj8a8HHiGpCV3jJ91nr2ec1aDNvMCSu1AoyHtPpHJ3V3DT0Rhqj-YWvw56n8rdl-gaa9KkOuOB4UwENMXzqFH7A4g4gT62LiaCSJpma5TO9xAZXoKG34g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هند نخستین موشک مداری خصوصی خود را با موفقیت پرتاب کرد
🔹
هند با پرتاب موفق موشک «ویکرام-۱» و قرارگیری آن در مدار ۴۵۰ کیلومتری، به‌عنوان سومین کشور جهان، قدرت عملیاتی بخش خصوصی خود را در صنعت پرتاب‌های فضایی به اثبات رساند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/672841" target="_blank">📅 08:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672840">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnGMjMmCo_b1hFK9nNPmuftI0YBIWQuDKBTY4zkbnafFuHwwv3Tqah5bnUbQk87UW9TjMexJTFBF8PtR4vPKYSGa0O4l0GjjeyQ4P0vDahiKiOQNmA58DezixOIG6J7B7VgYR1xjy_QqEDbFvRSBBrMbRkv9yAgKhxvgZr5UJqLJ8Dc_8gA0ShQDIzpgWenj4IeV3GQOOd4YZ1gwzfXce1eKBhT62gDORX60VE_QYQnWYBKJXN0-WqzMum-zopuEOGCypBkdfIyxL_tzKa-_Hfwo91j8hieRuNHWNXCRxRIb49bv629hqDkOsXU5ebBTsa_XYAh8gBfw5YUBdy8zsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال جام جهانی ۲۰۲۶
🔹
برنامه بازی‌ روز آخر مرحله حذفی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/672840" target="_blank">📅 08:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672839">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49f06efb4c.mp4?token=W3IsnfGxPbjk9Q8atuHUTLAUINakvSVZcXQtWqCw5sf-WD9sUeYjjFV6WZJZbCPN4At5XA6MrsIncDJCh_FiyCZpNjR9EFRopL8iqMFsY8u7JTtFORmy2Y7H3Wwr2DG1wYThJnFL8gnKt2RPluZcW6MWlaP4tPQ7vLvQqzMiJ_pRcJuWHRH-sqUR7MBviaCmdxpGOkZ0_8NNgwjxWDzWxWjZC_p-jVWmnBzpCUaBvOFhXAYiAVgAT16yUyhy6rIVrGjEIhTglvXPdiS40mI1ONJI6upWuzOwPch-8NElwZ0HybinepSQHNb_nj4IrIIzHq0ibYy1YbPuMKreL7QDAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49f06efb4c.mp4?token=W3IsnfGxPbjk9Q8atuHUTLAUINakvSVZcXQtWqCw5sf-WD9sUeYjjFV6WZJZbCPN4At5XA6MrsIncDJCh_FiyCZpNjR9EFRopL8iqMFsY8u7JTtFORmy2Y7H3Wwr2DG1wYThJnFL8gnKt2RPluZcW6MWlaP4tPQ7vLvQqzMiJ_pRcJuWHRH-sqUR7MBviaCmdxpGOkZ0_8NNgwjxWDzWxWjZC_p-jVWmnBzpCUaBvOFhXAYiAVgAT16yUyhy6rIVrGjEIhTglvXPdiS40mI1ONJI6upWuzOwPch-8NElwZ0HybinepSQHNb_nj4IrIIzHq0ibYy1YbPuMKreL7QDAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با انجام این حرکات هم عضلات پات قوی میشه و هم درد زانوت کم میشه! #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/672839" target="_blank">📅 08:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672838">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a02a765c10.mp4?token=RF2ItSkxrv5FrJNFaTjlm57jPi2g3yBGmhMiaY7VJqkj1CplAPyAEYcoRKQjLh1CK-j-xrxEWzMWJSGZoteWyUQOhh2baUbAJ_xnJYK4M0x4nT4qYhvg9R-RI-ooogS6o3uCFbrXNmdnPDXrBzQsOm0rM3sX0MUqiwgIkfIJtgkt_e3wuNtLjq5i1nlpZ6peR5RykjD9eiUQ-A8N3ApvGS74x1dz5AaCjJI-TSVs51-e1GfGZt3OanfmlXaRUIB8YQp5lmqjAy0i_FXr1-R7tij1u9lZ6OG8DwckeCa5Mj1zHif4yZ6v9B5rkMZ4lmgauEYL6rSShxizleVT6k1aoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a02a765c10.mp4?token=RF2ItSkxrv5FrJNFaTjlm57jPi2g3yBGmhMiaY7VJqkj1CplAPyAEYcoRKQjLh1CK-j-xrxEWzMWJSGZoteWyUQOhh2baUbAJ_xnJYK4M0x4nT4qYhvg9R-RI-ooogS6o3uCFbrXNmdnPDXrBzQsOm0rM3sX0MUqiwgIkfIJtgkt_e3wuNtLjq5i1nlpZ6peR5RykjD9eiUQ-A8N3ApvGS74x1dz5AaCjJI-TSVs51-e1GfGZt3OanfmlXaRUIB8YQp5lmqjAy0i_FXr1-R7tij1u9lZ6OG8DwckeCa5Mj1zHif4yZ6v9B5rkMZ4lmgauEYL6rSShxizleVT6k1aoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ضاحیه‌ی داغدار
🔹
ساختمانِ زخم‌خورده در گذشته از تجاوزات رژیم صهیونسیتی در «بئرالعبد» تاب نیاورد و فرو ریخت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/672838" target="_blank">📅 07:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672837">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
زمین لرزه ۵ ریشتری سالند خوزستان را لرزاند  مدیرعامل هلال‌احمر خوزستان:
🔹
ساعت ۰۵:۵۵ امروز یکشنبه ٢۸تیرماه، زلزله‌ای به بزرگی ۵ ریشتر در عمق ۱۲ کیلومتری، سالند از خوزستان را لرزاند.  #اخبار_خوزستان در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/672837" target="_blank">📅 07:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672834">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F7N989uJ7kUiP0SIgd-sDNviAsuxJj9RSAI_8ksUF7fiWgqQjATU5Tw6BeUQpVDltOit7u-dxcEqOoutxr4G4lvO5BEEl9FI16ppgFq8WJpVOBQqseAlPB7m7uLJ2wlHitSEWrHPbfQBX9P0HiqlZrOj3MCSTQSJUSyckhaii51CqDoy8Bbvu3y-WyCT2svJ5pEI51mGQ3nXVVPWTI9YetpMos40YIWIie3cvJAmr7UraSGXHbrG5YV-Cdwf7mbRP-PUVcD7CA3ai0ZoqtAoJ890ptvj_wwCWBecVm_QvXAdeFb5EXLej7XNSEEJl5fcGDr3hUFQihlgCHnEScaB0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LwlRuabs8EUpnPHZ5JGP6n-BU3YLV5NpCkB06E-Wge7-3ar9rpuYHV5-beCW7NWPVAg3dFm51QmwQgs631svLN7pob5YzYUKdQdqwoYiFB9de3ECBLkjRl_OAFYwz9gd3QyjKYSSP3Dh2VphqFtnHDBYyIZPo57nQv8Gx0Q9A7ql4LybT5Q0m2aDH3mi6ALecJyFa9lOh_auEk0IXmE4GfXp-WL1k_dncDddKcm4LWaF8KZDez1OOnf2_m4TOPLKDSW1nqP1osciBDMYCIO6HoPjw4jFicL4H-TJIamtAiZ0KjphHupyZ9yDeAxQ-ZxEwC_OacCnyKer8UcDi9UyRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1694542022.mp4?token=jtJLQ4VM8igAxyFryKYlL52UlLqhS2fcdrP03CbrJOCzEo7J1-1HjsW2jwd3INJu-YaaGdJ1fz1xnmnMnRZZHnfHDRxLcRfQfDCnIF9kdxkDSrES1A1JXruE62XV0XtKXM7lEb-E5V-SzEy4liuGG9hUMmEktd7fIB2xhdYsRk4Hqk34TnJ8AA962KR8xifY-rAezy-rCKiXImwcqbmEcWKo0Z3X8me0L3WMsGljBh07ZAIzrV-ZNdhH-oYcnlGK6bV9ODRAlV5oA8HC6jPKGBDEIn_6EnLPdsHabhQDeALJUuVHlmKzmGq6H9dnSEUgtZPRJht1JzzYHZwYc5C1vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1694542022.mp4?token=jtJLQ4VM8igAxyFryKYlL52UlLqhS2fcdrP03CbrJOCzEo7J1-1HjsW2jwd3INJu-YaaGdJ1fz1xnmnMnRZZHnfHDRxLcRfQfDCnIF9kdxkDSrES1A1JXruE62XV0XtKXM7lEb-E5V-SzEy4liuGG9hUMmEktd7fIB2xhdYsRk4Hqk34TnJ8AA962KR8xifY-rAezy-rCKiXImwcqbmEcWKo0Z3X8me0L3WMsGljBh07ZAIzrV-ZNdhH-oYcnlGK6bV9ODRAlV5oA8HC6jPKGBDEIn_6EnLPdsHabhQDeALJUuVHlmKzmGq6H9dnSEUgtZPRJht1JzzYHZwYc5C1vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیویورک دوباره تبدیل به ونیز شد
🔹
وضعیت نیویورک پس‌از بارش‌های سنگین در روزهای گذشته مورد توجه کاربران فضای مجازی قرار گرفته‌است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/672834" target="_blank">📅 07:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672833">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T24w71XDKlFPfrfCtUGbSVDLLaz6ocqwW3Ki_0oz0eQj-J8XnONvvk9sjMabfqzGuZ4mcbtXoyUgslTDfBrj6tUM5gUlb-6aG2UkVDsSLyk7Spr8BFRyLx_GC54M2g0xfubcIhBDSsKe3qfzPur045Me-TH-nTduHBN9VUbt0FxC8H1GP_ZH5oZrYg58Pe7FdLja8ehmlb2yrgx634Fo2lL-69AIJTVIq0_x3navflJIAUbjciULrH1RiMdK5iSZIgwOZSBi9WTgc8OqjazSu8W4-IQNaga_U-Dt7QZveTddeW9tldiUobLKqCGv6SHhx8MMQnGWAnj_BkVc87zamw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز یک‌شنبه
۲۸ تیر ماه
۴ صفر ۱۴۴۸
۱۹ جولای ۲۰۲۶
یکشنبه‌ها
#حدیث_کسا
بخوانیم
⬅️
متن و صوت حدیث کسا
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/672833" target="_blank">📅 07:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672832">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
زمین لرزه ۵ ریشتری سالند خوزستان را لرزاند
مدیرعامل هلال‌احمر خوزستان:
🔹
ساعت ۰۵:۵۵ امروز یکشنبه ٢۸تیرماه، زلزله‌ای به بزرگی ۵ ریشتر در عمق ۱۲ کیلومتری، سالند از خوزستان را لرزاند.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/672832" target="_blank">📅 07:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672831">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
ستاد فرماندهی مرکزی ایالات متحده:
ما هشتمین شب متوالی حملات علیه ایران را تکمیل کردیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/672831" target="_blank">📅 07:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672830">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
حمله موشکی آمریکا به اطراف شادگان
استانداری خوزستان:
🔹
در پی تهاجم موشکی آمریکا به خاک جمهوری اسلامی ایران، یک نقطه در اطراف شهر شادگان مورد اصابت موشک قرار گرفت. این حادثه هیچ‌گونه تلفات جانی در پی نداشته است.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/672830" target="_blank">📅 07:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672829">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
هشدار قرارگاه خاتم‌الانبیا به دشمن: نیروهای مسلح به هرگونه وحشی‌گری پاسخی ویرانگر می‌دهند
سرلشکر عبداللهی:
🔹
با تبعیت از فرامین و تدابیر رهبر معظم انقلاب، به شیطان بزرگ و دشمن جنایتکار، عهدشکن و حیله‌گر آمریکایی یادآور می‌شویم هرگونه طمع‌ورزی، زورگویی، تمامیت‌خواهی و وحشی‌گری با پاسخ قاطع و ویرانگر رزمندگان مومن، شجاع و مقتدر در نیروهای مسلح مواجه می‌گردد و هزینه‌هایی سنگین‌تر از جنگ تحمیلی دوم و سوم بر آنان تحمیل می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/672829" target="_blank">📅 07:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672828">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db885829ed.mp4?token=lF_VJbH_TfiQZNQgKMYjTPnaFhgCW3yfg6CzP4XvOy9dsyi7gh43DUO3FxzsyBTSSz6IdY_5J2xwZD8QWrV7LmmLA5Pm5ONLh6R4M4pOXXZftesLl6bmzAvaKAUtznxS07X7x5Qp2TjxgTjkWxV8iMxBJh4JY30JX4BQwCgqRHqKraoOtkOcIeNoX8-tsk2chMx2BgecDAAAJbUJMTctxpzQPGNhC1nmfErDHH7vF3__8XTU-LjgMiLC7Scrqez0CRBBeVhsbAfT3gU0tu_vOwHif4YFHHOeZMgTGCWV4ENOX5FxQyj_97IJVlo9L_ubD328r_Op7hrdSLVjMs537g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db885829ed.mp4?token=lF_VJbH_TfiQZNQgKMYjTPnaFhgCW3yfg6CzP4XvOy9dsyi7gh43DUO3FxzsyBTSSz6IdY_5J2xwZD8QWrV7LmmLA5Pm5ONLh6R4M4pOXXZftesLl6bmzAvaKAUtznxS07X7x5Qp2TjxgTjkWxV8iMxBJh4JY30JX4BQwCgqRHqKraoOtkOcIeNoX8-tsk2chMx2BgecDAAAJbUJMTctxpzQPGNhC1nmfErDHH7vF3__8XTU-LjgMiLC7Scrqez0CRBBeVhsbAfT3gU0tu_vOwHif4YFHHOeZMgTGCWV4ENOX5FxQyj_97IJVlo9L_ubD328r_Op7hrdSLVjMs537g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ارتش: دو پایگاه مهم آمریکا در کویت، آماج حملات پهپاد‌های انهدامی قرار گرفت
🔹
در پاسخ به تجاوزات مکرر دشمن، شهادت هم‌وطنان عزیز و حمله به پل‌ها، زیرساخت‌ها و مناطق غیر نظامی، ساعاتی قبل و در مرحلۀ شانزدهم عملیات صاعقه، ارتش جمهوری اسلامی ایران، انبار مهمات ارتش تروریستی آمریکا در اردوگاه العدیری و رادار پاتریوت و رادار هوایی این ارتش متجاوز در پایگاه علی‌السالم کویت را، آماج حملات پرحجم پهپاد‌های انهدامی خود قرار داد.
🔹
اردوگاه العدیری یکی از پایگاه‌های مهم ارتش تروریستی آمریکا در منطقه و در فاصلۀ ۱۰۴ کیلومتری مرز‌های جمهوری اسلامی ایران و ازمراکز مهم پشتیبانی و تجدید سازمان نیرو‌های آمریکایی است که اخلال در عملکرد این پایگاه تاثیر قابل توجهی بر عملیات‌های پشتیبانی ارتش در منطقه می‌گذارد.
🔹
پایگاه هوایی علی‌السالم نیز از پایگاه‌های مهم، مرکز اصلی ترابری هوایی و دروازۀ ورود نیرو‌های نظامی به منطقه غرب آسیاست که نقش محوری در راهبرد نظامی و لجستیکی ارتش متجاوز آمریکا در منطقه ایفا می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/672828" target="_blank">📅 07:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672827">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
حمله مجدد جنگنده‌های آمریکایی به مناطقی در قشم /  ۲ صدای انفجار شنیده شد
🔹
ساعت ۶:۱۰ صبح امروز جنگنده‌های آمریکایی بار دیگر مناطقی در جزیره قشم را هدف حمله قرار دادند.  بر‌اساس گزارش‌های اولیه، در پی این حمله دست‌کم دو صدای انفجار در نقاطی از جزیره شنیده شده است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/672827" target="_blank">📅 07:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672826">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
انهدام چندین هواپیمای نظامی آمریکایی در حملات ایران به اردن
🔹
روزنامۀ وال‌استریت ژورنال به نقل از مقام‌های آمریکایی گزارش داد که در حملات موشکی و پهپادی ایران در روزهای گذشته به پایگاه موفق السلطی اردن که با تلفات گستردۀ نظامیان آمریکایی همراه بود، چندین هواپیمای بدون‌سرنشین و سرنشین‌دار نیز مورد اصابت قرار گرفته و نابود شده‌اند.
🔹
کانال «نایا» نیز به نقل از منابع خود نوشته که یک فروند جنگندۀ اف-۱۵ در این پایگاه در حملات ایران منهدم شده است.
🔹
ساعاتی پیش نیز روزنامۀ نیویورک تایمز در گزارش خود نوشت که در حملات موشکی ایران چند بالگرد نظامی مورد هدف قرار گرفته‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/672826" target="_blank">📅 05:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672825">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
درگیری‌های شدید بین افراد مسلح و نیروهای امنیتی دولت موقت سوریه
🔹
یک رسانه عربی از وقوع درگیری‌های شدید بین نیروهای امنیتی حکومت موقت سوریه و افراد مسلح در استان حلب در شمال این کشور طی شنبه‌شب خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/672825" target="_blank">📅 04:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672824">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
استانداری هرمزگان: تا این لحظه اصابت موشک در بندرعباس نداشته‌ایم
🔹
در حال حاضر آرامش در منطقه برقرار بوده ‌و با وجود شنیده شدن برخی صداهای نامشخص، طبق آخرین گزارش‌ها تاکنون هیچ موردی از اصابت موشک در بندرعباس تأیید نشده است./ تسنیم
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/672824" target="_blank">📅 04:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672823">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
شنیده شدن صدای چند انفجار در نزدیکی مرز کویت و عراق
🔹
شبکه الغد عراق از شنیده شدن صدای چند انفجار در نزدیکی مرز کویت و عراق خبر داد و نوشت: گزارش‌هایی از پرتاب موشک به سمت خاک جمهوری اسلامی ایران وجود دارد. تاکنون جزئیات بیشتری در این باره منتشر نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/672823" target="_blank">📅 04:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672822">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
حملات نظامی دشمن آمریکایی به حوالی قشم  استانداری هرمزگان:
🔹
در ساعت ۳:۴۰ نقطه‌ای در حوالی قشم هدف حمله نظامی دشمن آمریکایی قرار گرفت. در این حملات جدید آمریکا به قشم هیچ مصدوم غیر نظامی یا خسارت به زیر ساخت‌های مسکونی و تجاری گزارش نشده است  #اخبار_هرمزگان…</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/672822" target="_blank">📅 04:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672821">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
وال‌استریت ژورنال: هواپیماهای آمریکا در اردن هدف قرار گرفتند
🔹
روزنامه وال‌استریت ژورنال آمریکا گزارش داد که در حمله موشکی ایران به پایگاه موفق السلطی اردن متعلق به ارتش تروریستی آمریکا هواپیماهای با سرنشین و بدون سرنشین هدف قرار گرفتند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/672821" target="_blank">📅 04:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672819">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
حملات نظامی دشمن آمریکایی به حوالی قشم
استانداری هرمزگان:
🔹
در ساعت ۳:۴۰ نقطه‌ای در حوالی قشم هدف حمله نظامی دشمن آمریکایی قرار گرفت. در این حملات جدید آمریکا به قشم هیچ مصدوم غیر نظامی یا خسارت به زیر ساخت‌های مسکونی و تجاری گزارش نشده است
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/672819" target="_blank">📅 03:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672818">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
ادعای مردم قشم از اصابت‌ ۳ تا ۵ موشک در مناطق مختلف جزیره
🔹
حوالی ساعت ۳:۳۸ بامداد صدای چند انفجار در مناطق مختلف جزیره قشم شنیده شد. براساس مشاهدات میدانی ‌و اظهارات شماری از ساکنان محلی، چند نقطه در جزیره هدف اصابت قرار گرفته است.
🔹
برخی از ساکنان تعداد اصابت‌ها را بین ۳ تا ۵ مورد عنوان می‌کنند. تاکنون هیچ مقام رسمی درباره محل دقیق اصابت‌ها، علت انفجارها، میزان خسارات احتمالی یا تلفات این حمله اظهار نظر ‌نکرده است./ تسنیم
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/672818" target="_blank">📅 03:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672817">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
گزارش‌های تایید‌نشده از صدای انفجار در بندرعباس
🔹
از دقایقی پیش اخباری مبنی بر صدای انفجار در بندرعباس منتشر شد، اما ‌‌هنوز گزارشی از اصابت موشک یا حمله جنگنده‌های آمریکایی نداشته‌ایم.  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/672817" target="_blank">📅 03:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672816">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
گزارش‌های تایید‌نشده از صدای انفجار در بندرعباس
🔹
از دقایقی پیش اخباری مبنی بر صدای انفجار در بندرعباس منتشر شد، اما ‌‌هنوز گزارشی از اصابت موشک یا حمله جنگنده‌های آمریکایی نداشته‌ایم.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/672816" target="_blank">📅 03:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672815">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
صدای انفجار در اهواز تکذیب شد
🔹
دقایقی پیش خبری مبنی بر حمله جنگنده‌های آمریکایی به مناطقی در اهواز منتشر شد که این خبر صحت ندارد و تا این لحظه هیچ گونه انفجار و حمله جنگنده های آمریکایی گزارش نشده است.  #اخبار_خوزستان در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/672815" target="_blank">📅 03:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672814">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccZ68D75Nf4pyHx_opDxK4_Ojcc8T4gbsHdnzLV3R6uOs_EBNuikFHT8R5TZmsb9YaXf_lHUvCgTmYpMQ2oYlLKx_tVnnX_V8QHQaecV-AkqwNRsHJIMv-2LDsq4FmpdX0rlU4IVFATv_i9f2M76ni6QdOo_4ZP-OboqfVYAr2PrL876vsf4evC491I-bIALGSVLng2Jj-P0aXHxBDcljNKQ_eMP9pjx9D5T7in2FFt9bQXHZdp7GZlsidp5_8JmxjAtTtSn8rsmdkHSm5JfR50JmXM1cmISt-RD9jM1zKbzwzwDKdLzLXrzQ19K225RwERmnlSoCBvDNJY_oad-sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مدال برنز بر گردن انگلیسی‌ها
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/672814" target="_blank">📅 03:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672812">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1efef3f4c7.mp4?token=j7BKXw-NJ0gc7F1Vj_V7vZ9R_aFkAe1jJNCR5fURm1Wx1Nk0IdNon_NdYY18nV1OMWrmuDEcHPnd7ROUC40MM8-Z5PMl1g8Fieb0-AB8rfalVzMma9GA9xWkCr8XDkv1M8Dvi2DgpIsOqioZEkzoHjv5tSBjWzz87_8YsTIcM7RG0Bc-V2xTn2xmvz4hGI1XkEzQu2hGynKJsAPAftNmolSA4TIZmJBeZ4MTOB33PwLjXsEhQ-ZPk-jimyaS6R7qNLY9cdXInGM_y1j6WTEd-nHh4vJtVkeV8_otSSj0k9l9_xKAfzsMU6m5ojLmnzTllzA1xTh6WKTPyyGt-6VM2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1efef3f4c7.mp4?token=j7BKXw-NJ0gc7F1Vj_V7vZ9R_aFkAe1jJNCR5fURm1Wx1Nk0IdNon_NdYY18nV1OMWrmuDEcHPnd7ROUC40MM8-Z5PMl1g8Fieb0-AB8rfalVzMma9GA9xWkCr8XDkv1M8Dvi2DgpIsOqioZEkzoHjv5tSBjWzz87_8YsTIcM7RG0Bc-V2xTn2xmvz4hGI1XkEzQu2hGynKJsAPAftNmolSA4TIZmJBeZ4MTOB33PwLjXsEhQ-ZPk-jimyaS6R7qNLY9cdXInGM_y1j6WTEd-nHh4vJtVkeV8_otSSj0k9l9_xKAfzsMU6m5ojLmnzTllzA1xTh6WKTPyyGt-6VM2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظۀ اصابت پهپاد انتحاری به مقر گروهک‌های تجزیه‌طلب در اربیل عراق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/672812" target="_blank">📅 02:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672811">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
فرماندار اراک هرگونه حادثه یا انفجار در این شهرستان را رد کرد
/ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/672811" target="_blank">📅 02:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672810">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
انفجار و حمله جنگنده‌های آمریکایی به قم تکذیب شد
🔹
در پی انتشار اخبار مبنی بر انفجار و حمله جنگنده‌های آمریکایی به مناطقی در قم، مسئولان امنیتی ضمن تکذیب این خبر اعلام کردند تا این لحظه گزارشی از انفجار نداشته‌ایم.
🔹
در حال حاضر امنیت در استان قم برقرار بوده و تاکنون هیچ انفجاری در هیچ نقطه‌ای در استان گزارش نشده است.‌
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/672810" target="_blank">📅 02:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672809">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
مقر گروهک «حزب آزادی کردستان» هدف حملات شدید قرار گرفت
🔹
گروهک «ارتش ملی کردستان» شاخه نظامی «حزب آزادی کردستان» اعلام کرد که مقرهای این گروهک تجزیه‌طلب در ابیل و سلیمانیه هدف حملات شدید از سمت ایران قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/672809" target="_blank">📅 02:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672808">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
حملات نظامی دشمن آمریکایی به حوالی حاجی‌آباد
🔹
در ساعت ۲:۱۰ نقطه‌ای در حوالی حاجی‌آباد هدف حمله نظامی دشمن آمریکایی قرار گرفت. در حملات جدید آمریکا به حوالی حاجی آباد هیچ مصدوم یا خسارت به زیر ساخت های مسکونی و تجاری  گزارش نشده است./مهر
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/672808" target="_blank">📅 02:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672807">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90746d4c73.mp4?token=bDk7T2q_G80w9TGdk96ZxAQH1xY7WGVbx0ko89rigI0v-MJaj4hzi0FPM0V-MvVHe8xQuo5L6tuo75-EQuiZb_s-AA9qk6tmekg619I_2wOSCKd1XCDxOhQo4HJjcuUiGiXPay9VlK9L2kpnP8x33mLfBjtmgwN1cnQXiUhf4g13J1ogtP1d1Vyji0qr93lyRI0SzhcghDWAeR2esQiIZsY5AVC7MhVYgbdQVmcLlRYGGStn473m7NrKY9b9poA7qiTQj3WMemnxIH0bM6t_LjFEwCAXD1oj5jaH0mGKtU8FDHUwWAK7ptUh_niedJJFABBbDeHv22rH2UWZxZ1l0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90746d4c73.mp4?token=bDk7T2q_G80w9TGdk96ZxAQH1xY7WGVbx0ko89rigI0v-MJaj4hzi0FPM0V-MvVHe8xQuo5L6tuo75-EQuiZb_s-AA9qk6tmekg619I_2wOSCKd1XCDxOhQo4HJjcuUiGiXPay9VlK9L2kpnP8x33mLfBjtmgwN1cnQXiUhf4g13J1ogtP1d1Vyji0qr93lyRI0SzhcghDWAeR2esQiIZsY5AVC7MhVYgbdQVmcLlRYGGStn473m7NrKY9b9poA7qiTQj3WMemnxIH0bM6t_LjFEwCAXD1oj5jaH0mGKtU8FDHUwWAK7ptUh_niedJJFABBbDeHv22rH2UWZxZ1l0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک رده‌بندی در حد فینال با ۱۰ گل، گل ششم انگلیس به فرانسه توسط بلینگام
🏴󠁧󠁢󠁥󠁮󠁧󠁿
6️⃣
🏆
4️⃣
🇫🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/672807" target="_blank">📅 02:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672805">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXOwigpkfi4CwhLyRFU0X3fT3B9JZKq5Jre498z56Wd4EwFYx_yg3EXAeHy1lsjS2asyY9Z0KL4d-3XmyIVLFUiK5fEkZ0DUvxK0UGjdRi-dvhnI_i0aAyid79XEmvpZTfGt_kqYP1ZG6pUqI-ZgYT_i4b6p6c5iTY0PEoBcvN2Samr9Vq5aTsfB0GbUxy3dryLrR5HoL4T4xXI3vq_Sp6-AfdD9qjVvhInHVtoFSzNs0_UkUrCuwaJ2filTA5ATGwFZv_Q1zUxNlbLHqhfpUoWC6cK09s3MRuEVAk5CcuXb0T-6gzbueOT5SI-PSc5NZw81T1X9CqWjceWbbEEnuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
انگلیس روی سکوی سوم جام جهانی ۲۰۲۶
🔹
تیم فوتبال انگلیس با پیروزی پرگل ۶ بر ۴ مقابل فرانسه، روی سکوی سوم جام جهانی ۲۰۲۶ ایستاد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/672805" target="_blank">📅 02:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672804">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a14d10202.mp4?token=pBZfSy4UO_yA2IXivzZ0oGmk4ggRpNcP9-C5f0-S_fvz4VNrEUDOuSY4iXJGS2SXzTm7sRIrz1PkcMGCcl3ByEZF5zIt68YrbRQ4d1CjFscXrbOjuOtPK8oxbayXMOCPOZe7Zn30tk3SK2m1cPZiErMwWnQXVuInG55Je4vxeZ9VMOwbL3QVkzriWR-8KgMw2yrefFyxKAl33afE7Ow3IuaqSNjsAI3OGatdQjsOC2KZc4HTPsKh-lUmZnpoIfBD4ZXH87scOp-gevvmlwjvnS1ubgX3YyQDoXLJ3D5pk06pYKJ9tZe61BtBbFXXm0jX8WI-aHgYyV7mPXSL7CKWFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a14d10202.mp4?token=pBZfSy4UO_yA2IXivzZ0oGmk4ggRpNcP9-C5f0-S_fvz4VNrEUDOuSY4iXJGS2SXzTm7sRIrz1PkcMGCcl3ByEZF5zIt68YrbRQ4d1CjFscXrbOjuOtPK8oxbayXMOCPOZe7Zn30tk3SK2m1cPZiErMwWnQXVuInG55Je4vxeZ9VMOwbL3QVkzriWR-8KgMw2yrefFyxKAl33afE7Ow3IuaqSNjsAI3OGatdQjsOC2KZc4HTPsKh-lUmZnpoIfBD4ZXH87scOp-gevvmlwjvnS1ubgX3YyQDoXLJ3D5pk06pYKJ9tZe61BtBbFXXm0jX8WI-aHgYyV7mPXSL7CKWFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل چهارم فرانسه به انگلیس توسط دمبله
🏴󠁧󠁢󠁥󠁮󠁧󠁿
5️⃣
🏆
4️⃣
🇫🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/672804" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672803">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
صدای انفجار در اهواز تکذیب شد
🔹
دقایقی پیش خبری مبنی بر حمله جنگنده‌های آمریکایی به مناطقی در اهواز منتشر شد که این خبر صحت ندارد و تا این لحظه هیچ گونه انفجار و حمله جنگنده های آمریکایی گزارش نشده است.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/672803" target="_blank">📅 02:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672802">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
منابع بحرینی از پرواز پر حجم جنگنده‌های آمریکایی از خاک این کشور برای انجام حملات در ایران خبر می‌دهند/
فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/672802" target="_blank">📅 02:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672801">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2785127527.mp4?token=ECksUq7SEBXAqcrRvvQznPxR_ZIo6aq8w23_fK0iCJreYZaRLkKtbyyk8DDdodEyEbBPXEJRW5S-swy8UrV3nCcPsbeIHke-OrgHvS3VD9ZbaPflEsCynMeK3JtdsHHYR9vDdgT5a5Ug1mqMSPP9gWrm-Te9yureVmG_sPNs1hRxN-Owopl8Ssb-1qxHIPqS3wcmfJrSrXIRXIhYyhWZ4d5hqPscK-rMPu-qJBWMX4S85_wIeZ2lu6vJhoHvlEhkcvq58HWkHVrcCCkb3ZK535cskK-oBxchFLyxJ-POqKImaIO1bqTMtIw9P6M5JKNnA9ngS7FJPyJpDHqtUXBMmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2785127527.mp4?token=ECksUq7SEBXAqcrRvvQznPxR_ZIo6aq8w23_fK0iCJreYZaRLkKtbyyk8DDdodEyEbBPXEJRW5S-swy8UrV3nCcPsbeIHke-OrgHvS3VD9ZbaPflEsCynMeK3JtdsHHYR9vDdgT5a5Ug1mqMSPP9gWrm-Te9yureVmG_sPNs1hRxN-Owopl8Ssb-1qxHIPqS3wcmfJrSrXIRXIhYyhWZ4d5hqPscK-rMPu-qJBWMX4S85_wIeZ2lu6vJhoHvlEhkcvq58HWkHVrcCCkb3ZK535cskK-oBxchFLyxJ-POqKImaIO1bqTMtIw9P6M5JKNnA9ngS7FJPyJpDHqtUXBMmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل پنجم برای انگلیس از روی نقطه پنالتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
5️⃣
🏆
3️⃣
🇫🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/672801" target="_blank">📅 02:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672800">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
استانداری هرمزگان: علیرغم برخی خبرها در فضای مجازی، برخوردی در بند لنگه گزارش نشده است
/ مهر
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/672800" target="_blank">📅 02:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672799">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b93e8cca8.mp4?token=J6Z-Y2IM5lFkTMCbh4zvmX_-qUPxL6a6zpNDeBVq4-JhbeIOm1qTJbHreVE4j1eWVsoQWoGstmZ-dRJ5XeOm5N0YHGh75nTf_Uqu_yzDu6i6Y9bDAr36oz-gTsSSFUHVljDLAWAErtUvYi7NGztA24pncwUqX_A81rWurfeA1p6PQb6HwmZwrz3pSwWtv5zSsu0gQYfYbEJs3epCH3MxRC8WiZu_58rzb0Qmu-Z2Q1vuEwYd78IqlzsjM1Mi4CyCh_Nxcy7wpcf0ZIk4WwAtRt5hSiLNWpnUmYmQ85TEkNjg65scP7Kyk_us7zC1kxi-DDNJPlY6zw3Ip4__dOsVIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b93e8cca8.mp4?token=J6Z-Y2IM5lFkTMCbh4zvmX_-qUPxL6a6zpNDeBVq4-JhbeIOm1qTJbHreVE4j1eWVsoQWoGstmZ-dRJ5XeOm5N0YHGh75nTf_Uqu_yzDu6i6Y9bDAr36oz-gTsSSFUHVljDLAWAErtUvYi7NGztA24pncwUqX_A81rWurfeA1p6PQb6HwmZwrz3pSwWtv5zSsu0gQYfYbEJs3epCH3MxRC8WiZu_58rzb0Qmu-Z2Q1vuEwYd78IqlzsjM1Mi4CyCh_Nxcy7wpcf0ZIk4WwAtRt5hSiLNWpnUmYmQ85TEkNjg65scP7Kyk_us7zC1kxi-DDNJPlY6zw3Ip4__dOsVIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی گسترده در مقر گروهک‌های تجزیه‌طلب اربیل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/672799" target="_blank">📅 02:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672798">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
گزارش‌های تایید‌ نشده از صدای انفجار در بندرعباس و بندرلنگه
🔹
از دقایقی پیش اخباری مبنی بر صدای انفجار در بندرعباس و بندرلنگه منتشر شد که مسئولان استانداری هرمزگان ضمن تایید این صداها می‌گویند هنوز گزارشی از اصابت موشک یا حمله جنگنده‌های آمریکایی نداشته‌ایم.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/672798" target="_blank">📅 02:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672797">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zof9YiBwxSoRclEv-7eX1O2SQUGFOGTBRizXTjbaau4fuomBnxvUWfIro0FXTy2a46aJlzOkrRv11y4ghqyGkgea5DYn5ILJyH2DHhlKQkTPcRaGXRP2G26c5j8ZWJ1CE8zCUcyoclsshz2Y3rudS--bvWOZ3eYYc9eiHrbg3M5J8w6xrDb4fIUeTJsoxMGYMnPv8Rj0AoKb2BUpffBHrg-Mu8pDkN7bYfaRYVODWs7Y5S5nEf93lEZOLDYih6lxGASGVaeDiUHxkI06fXkO_vSHPb5R6nFix8VlfkUPbuYUhg8ccoOze9Xe3y4ZMVK-8FWzfReCyzM2pq63uvI1JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امباپه با ۲۲ گل بهترین گلزن تاریخ جام‌جهانی شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/672797" target="_blank">📅 02:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672796">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
شنیده شدن صدای پرواز جنگنده در کیش
🔹
در جزیره کیش دقایقی پیش صدای پرواز یک یا چند فروند جنگنده را در آسمان این جزیره شنیده‌ شد. گفته می‌شود با وجود شنیده شدن این صدا، تا این لحظه هیچ‌گونه صدای انفجار یا حادثه امنیتی در سطح جزیره گزارش نشده است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/672796" target="_blank">📅 02:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672795">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
ارتش تروریستی آمریکا مدعی انتقام از ایران به خاطر سربازانش در اردن شد
🔹
ارتش تروریستی آمریکا در پیامی که دقایقی قبل منتشر شد، ادعا کرد: «حملات جدید به ایران با هدف مجازات فوری سپاه پاسداران به خاطر حملاتش علیه نیروهای نظامی ایالات متحده در اردن انجام می‌شود.»/ جماران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/672795" target="_blank">📅 02:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672794">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0813f70fda.mp4?token=WmjN64--QkJ9vwdaRMcIeWRdHMvG3yBOkdo3o16qShTV9L6t9UR071gRgqcHtk0dTmZqlSkstifAWsb6jLkzviRnJePlRnW80Dn2MS1-o2ejMHJZtxUIV4VUSIHlHRZInFQJdFttx2G1k8nZt0qMYg5Veq4HtcEw2uMyBmBEKK3FkxgaQR7RzOGBhEUeG5qWtNfUCZevfaSdIE-m8PmT2oPPQwpjmJG6h3CZqZkD8SH3iWXMo9b8_NrT65U5oUnoTe1LS-7b7FwtCh41pFYDcMD0GJJs-TWWXX5ruVO78t3ib6mYrNj47R4cIuqvtUWz_rjNz_Xe12LR0xy0LAiVeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0813f70fda.mp4?token=WmjN64--QkJ9vwdaRMcIeWRdHMvG3yBOkdo3o16qShTV9L6t9UR071gRgqcHtk0dTmZqlSkstifAWsb6jLkzviRnJePlRnW80Dn2MS1-o2ejMHJZtxUIV4VUSIHlHRZInFQJdFttx2G1k8nZt0qMYg5Veq4HtcEw2uMyBmBEKK3FkxgaQR7RzOGBhEUeG5qWtNfUCZevfaSdIE-m8PmT2oPPQwpjmJG6h3CZqZkD8SH3iWXMo9b8_NrT65U5oUnoTe1LS-7b7FwtCh41pFYDcMD0GJJs-TWWXX5ruVO78t3ib6mYrNj47R4cIuqvtUWz_rjNz_Xe12LR0xy0LAiVeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرانسه در آستانه کامبک زدن، گل سوم فرانسه به انگلیس توسط امباپه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
4️⃣
🏆
3️⃣
🇫🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/akhbarefori/672794" target="_blank">📅 02:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672793">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
منابع عراقی از حملات سایبری علیه شرکت‌های گازی اماراتی و آمریکایی در اربیل خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/672793" target="_blank">📅 01:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672792">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
حملات نظامی دشمن آمریکایی به حوالی سیریک
🔹
در ساعت ۱:۳۰ نقطه ای در حوالی سیریک هدف حمله نظامی دشمن آمریکایی قرار گرفت.
🔹
در حملات جدید آمریکا به سیریک هیچ مصدوم یا خسارت به زیر ساخت های مسکونی و تجاری  گزارش نشده است
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/672792" target="_blank">📅 01:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672791">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
سنتکام: به دستور فرمانده کل قوا، حملات هوایی جدیدی را علیه اهدافی در ایران آغاز کردیم
🔹
امروز ساعت ۶ عصر به وقت شرقی آمریکا، نیروهای آمریکایی به دستور فرمانده کل قوا، حملات هوایی جدیدی را علیه ایران آغاز کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/672791" target="_blank">📅 01:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672790">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
منابع عراقی: حملۀ پهپادی به کنسولگری آمریکا در اربیل ادامه دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/672790" target="_blank">📅 01:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672789">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
سنتکام: به دستور فرمانده کل قوا، حملات هوایی جدیدی را علیه اهدافی در ایران آغاز کردیم
🔹
امروز ساعت ۶ عصر به وقت شرقی آمریکا، نیروهای آمریکایی به دستور فرمانده کل قوا، حملات هوایی جدیدی را علیه ایران آغاز کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/672789" target="_blank">📅 01:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672788">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
منابع عراقی: حملۀ پهپادی به کنسولگری آمریکا در اربیل ادامه دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/672788" target="_blank">📅 01:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672786">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c15e9eec1.mp4?token=tfzwm9Fxa01blINuPwP8JmcciD-oe0v7M2lK9yvdtB_BFQTnI7UfBgVC_3wWW1rW5G9_YBLsvO2v9H51kkX7OF09Bu0JQkuTzytnZ0UrXWbn7RvGrXYZr6eOdRhcQrm0dl6yt0jJe5tIfB2ua2BONrMgrRgNJDzSzATyNALxb1TCu-4XRKvz6JqSr3g_hYwBzNb_vuFNfVeMp_KPc_7CA__vROWXVO6ZWTAraGct7IKywAy33qxAtvQuoNaSeUy4A9goOnJnWAkm2LEC-9_JtoevkKTFJJvyWoigmczOtTGvKkTaH3cCMb-YAQhSDAkn7-IOHDPGEzkLYW-YBAINXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c15e9eec1.mp4?token=tfzwm9Fxa01blINuPwP8JmcciD-oe0v7M2lK9yvdtB_BFQTnI7UfBgVC_3wWW1rW5G9_YBLsvO2v9H51kkX7OF09Bu0JQkuTzytnZ0UrXWbn7RvGrXYZr6eOdRhcQrm0dl6yt0jJe5tIfB2ua2BONrMgrRgNJDzSzATyNALxb1TCu-4XRKvz6JqSr3g_hYwBzNb_vuFNfVeMp_KPc_7CA__vROWXVO6ZWTAraGct7IKywAy33qxAtvQuoNaSeUy4A9goOnJnWAkm2LEC-9_JtoevkKTFJJvyWoigmczOtTGvKkTaH3cCMb-YAQhSDAkn7-IOHDPGEzkLYW-YBAINXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع ۵ انفجار در اربیل؛ سامانه پدافند هوایی کنسولگری آمریکا فعال شد
🔹
بر اساس این گزارش، هم‌زمان با وقوع این انفجارها، پهپادهایی نیز بر فراز آسمان اربیل در حال پرواز مشاهده شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/672786" target="_blank">📅 01:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672785">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d35cb592f.mp4?token=LgqikZTzA_L_AKQSNAw7j6zilX4SGosAvHMhhduOm6eqKz_sdNJuMB8Oh3jmUmNQShhalPzzI5uT6qsCxe_GAKR8ou9uK6jKSDLczSZ4PUpcp_qqcl5-vZJL4bhJFPVH2QLBCWL_EAimouMNvMMKFE_eJ8QEjjmNIErgT08PFr5x28Z6X9V3aF24CA70FyXn-rdbyHC4uhfASXWKsflXrCMsscb-1X_GpeyIP6pKeOigLnh4JvLOIYCu3_x9TwsncfqNhcYdYg_SfazUV-q5s7PYKM02uoHxIfMW4nKbhI2ZZmHbbcuZxeQcz1wlwKfeSapWS2Gn-TMtetMYtG6FJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d35cb592f.mp4?token=LgqikZTzA_L_AKQSNAw7j6zilX4SGosAvHMhhduOm6eqKz_sdNJuMB8Oh3jmUmNQShhalPzzI5uT6qsCxe_GAKR8ou9uK6jKSDLczSZ4PUpcp_qqcl5-vZJL4bhJFPVH2QLBCWL_EAimouMNvMMKFE_eJ8QEjjmNIErgT08PFr5x28Z6X9V3aF24CA70FyXn-rdbyHC4uhfASXWKsflXrCMsscb-1X_GpeyIP6pKeOigLnh4JvLOIYCu3_x9TwsncfqNhcYdYg_SfazUV-q5s7PYKM02uoHxIfMW4nKbhI2ZZmHbbcuZxeQcz1wlwKfeSapWS2Gn-TMtetMYtG6FJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرانسه به خودش آمد، گل دوم فرانسه به انگلیس توسط بارکولا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
4️⃣
🏆
2️⃣
🇫🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/672785" target="_blank">📅 01:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672784">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27409c54f4.mp4?token=NJMLnE0deph-dCcBqD8qBhNliBTR9GwZcBzRlOdObshLFJJG2aAYsa_Om0A_6sX50K2hYcf8SWRCfgjVIyEVg_Z0lfG-wMbUqwb4Plrs3WFde8z41RsBYdrUshznlulI7piO7qJ6Tm9YuG-u1bZeGeAZIMlk5CKgdF8LGdH-0GN1Q7Dg0p1ZNFgyY7kpl3UNL0owsNPGcp4yIKPPT6ebrf8LO3ux1kmppHioSFCuP-IpOy_78PCzSLsH7HsrXVl16ZskZbX_11_7lfzHu8REEmxHrVyeL9H5tBGXgxcxrLDMmzaBMPoH8adet43MFnnW5rRgnBFeuDJccsztvNCfow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27409c54f4.mp4?token=NJMLnE0deph-dCcBqD8qBhNliBTR9GwZcBzRlOdObshLFJJG2aAYsa_Om0A_6sX50K2hYcf8SWRCfgjVIyEVg_Z0lfG-wMbUqwb4Plrs3WFde8z41RsBYdrUshznlulI7piO7qJ6Tm9YuG-u1bZeGeAZIMlk5CKgdF8LGdH-0GN1Q7Dg0p1ZNFgyY7kpl3UNL0owsNPGcp4yIKPPT6ebrf8LO3ux1kmppHioSFCuP-IpOy_78PCzSLsH7HsrXVl16ZskZbX_11_7lfzHu8REEmxHrVyeL9H5tBGXgxcxrLDMmzaBMPoH8adet43MFnnW5rRgnBFeuDJccsztvNCfow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول فرانسه به انگلیس توسط امباپه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
4️⃣
🏆
1️⃣
🇫🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/672784" target="_blank">📅 01:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672783">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
رسانه‌های عراقی از وقوع چندین انفجار در کنسولگری آمریکا در اربیل خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/672783" target="_blank">📅 01:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672782">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b1c746642.mp4?token=SdqhU1sUVo0Cl9rDf80-F770vi3-8WFDWgqFqsReTtriDEwX3om6gga3x5KxaVidgXtOzSNnG68Ggk2XsDP060iK78CRX1Ep8gWjphZFHdVVTpmlaqrbZASoOXmrMC-dbAdrMr8PNUvvISVqTjr59P-bTmldMM8mM8q_P-dLZ1mbHnaKFvnchxurqJCXXiNzUG9IVBDnMGa-_A0DWhuPBBNmAzc_e4nDfxAcC4Fxta5EUs2oxh0zzxNO13jD6zV4nBjgxva9r0PPSBZwlshi4_o2xnFzZaj1taq9dWdNtjImyiKxBO43z_cU28ozgJXboYFEiqyjMv1DbmmurWgeRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b1c746642.mp4?token=SdqhU1sUVo0Cl9rDf80-F770vi3-8WFDWgqFqsReTtriDEwX3om6gga3x5KxaVidgXtOzSNnG68Ggk2XsDP060iK78CRX1Ep8gWjphZFHdVVTpmlaqrbZASoOXmrMC-dbAdrMr8PNUvvISVqTjr59P-bTmldMM8mM8q_P-dLZ1mbHnaKFvnchxurqJCXXiNzUG9IVBDnMGa-_A0DWhuPBBNmAzc_e4nDfxAcC4Fxta5EUs2oxh0zzxNO13jD6zV4nBjgxva9r0PPSBZwlshi4_o2xnFzZaj1taq9dWdNtjImyiKxBO43z_cU28ozgJXboYFEiqyjMv1DbmmurWgeRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یورش نیروهای اشغالگر صهیونی  به محله الرامیس، در شمال قدس اشغالی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/672782" target="_blank">📅 01:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672781">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
انفجار در اربیل
🔹
منابع عراقی از شنیده شدن صدای انفجار در اربیل و فعال شدن سامانه‌های پاتریوت مستقر در پایگاه آمریکایی حریر خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/672781" target="_blank">📅 01:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672780">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
فعال سازی پدافند هوایی در اربیل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/672780" target="_blank">📅 01:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672779">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b100100dad.mp4?token=msFrQfjwVfMAcsUMi8FFRrjMCHfUMHxLZgTid0-i5u7nRJjGnY8mEbNLdp2KO0qU0QnR-S7ZrsfzTTyA670UFWS7bHzDfuUbXZJl92aCJxhK19Ck8SuoJ16eOU_Nw_N0VLnnOXn24rYqeeoss202RleLt8kARrVtWInWlgqnGGWr44knipY8Pdfgh0u0GW8ojED-cPmLHZh8o-ZfvW8-S3_frzNxaZW7p6xC0UIzhQUU4rOtMq4tsxDO5kZOJM2eiFjTgx_P1PlxEfiQxDCe_NlFtIVgsMlYTbj90Ne_rPczCnnPIZfH20bqE9tdJk1zp5Q-Qnb0L7KHlYhDEdTpww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b100100dad.mp4?token=msFrQfjwVfMAcsUMi8FFRrjMCHfUMHxLZgTid0-i5u7nRJjGnY8mEbNLdp2KO0qU0QnR-S7ZrsfzTTyA670UFWS7bHzDfuUbXZJl92aCJxhK19Ck8SuoJ16eOU_Nw_N0VLnnOXn24rYqeeoss202RleLt8kARrVtWInWlgqnGGWr44knipY8Pdfgh0u0GW8ojED-cPmLHZh8o-ZfvW8-S3_frzNxaZW7p6xC0UIzhQUU4rOtMq4tsxDO5kZOJM2eiFjTgx_P1PlxEfiQxDCe_NlFtIVgsMlYTbj90Ne_rPczCnnPIZfH20bqE9tdJk1zp5Q-Qnb0L7KHlYhDEdTpww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فعال سازی پدافند هوایی در اربیل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/672779" target="_blank">📅 01:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672778">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2530637954.mp4?token=DLjqnGk3ZVHgdXjDmRWyBdmaYVMpv5Mp7Y_bQbpneQGAOkHs08Y5Qa8MArlaUyuEgxLyJcU84a3xBwXdQKlu-YGxsTYbPHKS4n9JX-3826pFGKSQRknTRGcIZLmOolBhErDtOa0cMJKii4HWrDlA6tKaZZglY9ZcyhVXFR03ATFQm6fileChcZqftnv0RYuPmGfuz-hGsa-L0QnIyYN_2uhWHEx9oW1rZ3jLPA8GfwTwreRB-A8gfhRhk5STYRP4SgQPU2WtLDHIHZFAjHwM8HyQIcRVg4f8WwmRTUmd8zEUkvM0QDIFIeFJ7VLS1ZbFW5G2sZjyRPA4M-_BTU1U9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2530637954.mp4?token=DLjqnGk3ZVHgdXjDmRWyBdmaYVMpv5Mp7Y_bQbpneQGAOkHs08Y5Qa8MArlaUyuEgxLyJcU84a3xBwXdQKlu-YGxsTYbPHKS4n9JX-3826pFGKSQRknTRGcIZLmOolBhErDtOa0cMJKii4HWrDlA6tKaZZglY9ZcyhVXFR03ATFQm6fileChcZqftnv0RYuPmGfuz-hGsa-L0QnIyYN_2uhWHEx9oW1rZ3jLPA8GfwTwreRB-A8gfhRhk5STYRP4SgQPU2WtLDHIHZFAjHwM8HyQIcRVg4f8WwmRTUmd8zEUkvM0QDIFIeFJ7VLS1ZbFW5G2sZjyRPA4M-_BTU1U9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر تازه از لحظه شلیک موشک از کویت به سمت ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/672778" target="_blank">📅 01:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672777">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc83a1fc86.mp4?token=M7Eu83G7nSstAcsdeqRh41kzFE0OVxKbmqDDDTihetk2j_S84jegYd4JecjnhyyneuWFThjaU9vLRjdsHMxCJdtPJ1AZ8l6IBEv8-oPCTvnMZt8qwn4s4PPQGeEhQPC0pDSyeYJ4yfiotAAzg5_BWqX9iX-XFWJ85VhXNsElHUb4NeY982tbeOKuet5HCT1rcg4VcmmW2k13NUeGviANX8IkxAlecqYZu3oidmWoDUDf__O21GMeUHnIVOmXrvt7KVcv7S_LUxA_Ck7Ox2sD-cRne_r4ZQvQSyWFa_VpXygRR17azYIdggsduVzcXXu2Ax4oTbdBQ8sP6Jxc7JTOfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc83a1fc86.mp4?token=M7Eu83G7nSstAcsdeqRh41kzFE0OVxKbmqDDDTihetk2j_S84jegYd4JecjnhyyneuWFThjaU9vLRjdsHMxCJdtPJ1AZ8l6IBEv8-oPCTvnMZt8qwn4s4PPQGeEhQPC0pDSyeYJ4yfiotAAzg5_BWqX9iX-XFWJ85VhXNsElHUb4NeY982tbeOKuet5HCT1rcg4VcmmW2k13NUeGviANX8IkxAlecqYZu3oidmWoDUDf__O21GMeUHnIVOmXrvt7KVcv7S_LUxA_Ck7Ox2sD-cRne_r4ZQvQSyWFa_VpXygRR17azYIdggsduVzcXXu2Ax4oTbdBQ8sP6Jxc7JTOfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل چهارم انگلیس به فرانسه توسط ساکا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
4️⃣
🏆
0️⃣
🇫🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/672777" target="_blank">📅 01:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672776">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b5f17f766.mp4?token=BxhWVSMndOGVCQgGiHTvlF5B0PWa_Q8AKlFTkXts7iEmoUgYXuH4S95MjpStN31igvF3iQfFGoOR1HnHAnxbPEcbw9-7Sd3jKO5DImBfuCNCuH7IE3QEAVEzqGlxDdZFy6rQtX_8qqD4V7ipmqI0OXir3r2N6TdGgEjiLOvNC6q5zqgBOF7-VrElZX-oPxl3549QiIAL_wV0HTkB7BUWQjhuKH2Ge7ExDhYnCdPinJ4wxJNTX2duR_wFZyyg2xBk8n8w8Efb2hjwh11nKeUjavUwYnOYhWUbnwp_vIkOEzTASx1UZVU7iJng0LEg-6dYt4xllA4NkW3B61QXRI2-tpixxjLZCDvVGZmgyIYoutSdvvUN0qKpOYzy-fPR96NBucgWht7_6Ba27Yo8IOawHff5HNXb-UnaHs0lOBZCh_TCARpnnDEUl3Ohl_8oKyyYantevisCJpya_KgDk1I1DY29cDALR1eOpcAoTNP7bl-I7m3fyu20E2eT9A4wWXIOIYhbgb3aht_cbwXcpDqwQxG6XVNYeSxrW65ShkSHeAh7emcVMpDkWGq_k9iiIAqfuYNEXWBYlxMhysZ_oOUwZgr0p5TNqye9r1A7_cqiLtXe1qfts_uYm1lTYF-0qr3-96Dki-0rOdMEF7-ubawwuIcHDEFQNfn3afi-XmTJHyk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b5f17f766.mp4?token=BxhWVSMndOGVCQgGiHTvlF5B0PWa_Q8AKlFTkXts7iEmoUgYXuH4S95MjpStN31igvF3iQfFGoOR1HnHAnxbPEcbw9-7Sd3jKO5DImBfuCNCuH7IE3QEAVEzqGlxDdZFy6rQtX_8qqD4V7ipmqI0OXir3r2N6TdGgEjiLOvNC6q5zqgBOF7-VrElZX-oPxl3549QiIAL_wV0HTkB7BUWQjhuKH2Ge7ExDhYnCdPinJ4wxJNTX2duR_wFZyyg2xBk8n8w8Efb2hjwh11nKeUjavUwYnOYhWUbnwp_vIkOEzTASx1UZVU7iJng0LEg-6dYt4xllA4NkW3B61QXRI2-tpixxjLZCDvVGZmgyIYoutSdvvUN0qKpOYzy-fPR96NBucgWht7_6Ba27Yo8IOawHff5HNXb-UnaHs0lOBZCh_TCARpnnDEUl3Ohl_8oKyyYantevisCJpya_KgDk1I1DY29cDALR1eOpcAoTNP7bl-I7m3fyu20E2eT9A4wWXIOIYhbgb3aht_cbwXcpDqwQxG6XVNYeSxrW65ShkSHeAh7emcVMpDkWGq_k9iiIAqfuYNEXWBYlxMhysZ_oOUwZgr0p5TNqye9r1A7_cqiLtXe1qfts_uYm1lTYF-0qr3-96Dki-0rOdMEF7-ubawwuIcHDEFQNfn3afi-XmTJHyk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل سوم انگلیس به فرانسه توسط ساکا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
3️⃣
🏆
0️⃣
🇫🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/672776" target="_blank">📅 01:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672775">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
مدیرعامل شرکت آب و فاضلاب هرمزگان: تاسیسات آب‌شیرین‌کن بونجی در غرب شهرستان جاسک که در پی حمله بامداد شنبه ( ۲۷ تیر ) ارتش تروریستی آمریکا دچار آسیب شده بود، مرحله نخست بازسازی آن با موفقیت به پایان رسیده است
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/672775" target="_blank">📅 01:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672772">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hpq0LEsDKJilUPMd3UlSZPHvLpdr8WmNByL8VROZiTX-LBFKi1q2m6-6k0cXXPHcQs5n14Q6Vojc1-zsYZQQIvDtQEikJPvgGKsdDKpRZ7mXBZjDV6A_Nm94oIlQJJ0XghNkPFlgIdj-aO09GGGgPgqUMZc57tVk6N3gMuOAMrY4lIqF52Y8Ti9PpEfkjr6nyzLLyODIfszt7vN1Xt9UnNVP5h7IkQMVtCVPLqp2POHzkqVwKqArkNqmXtWfOBoJbt87HlMhq6zDPzzSUA0WSlg8XWFAiYxlloDFtqkUmJvY366MDvF46nvl6vyaGUwc88LpMjTbDpEQycc8spTf1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LGg4TKcoQS8wKG_dKv-W-n7-hAHZ2pW_ieEsCCvgmED5bdldv8lwoKWmu99VC5bQfogin0Rk9wwl2Hl2053y0S5V5Gd5hLETBCfiCpKHUzS3YtIEO3W9JVHSQQQGvYyHCiXp9OCZweq5wRh2VkrQ-83LvOrdAhQL03io_kWzu_naDmlw8I5mCPkXEvKTZYPvkSGpda_cWk8oHUbZ0tBRKocIWNNNsybUjAoAhzVgz42biWSNd_JQBdvZmbhybTEG7lcQHpOQniE21tNB6EmEJ2Zje3conNNRbtxAzmJ0GipzwaNSEPhioS-fyDK9grq3k53WLA6RiJih9FzTlD5a3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4894ed02a.mp4?token=YgtyDC53-89DTF4-_XreBbhZ1cNuOqIw9uGIt_-pL01McNCFBAJtX7Z06-4TRnrpxwcD3lJnBRhKL8v1RDVFWH3HaiMQueQj_vCoNEaIrCQvxeZKla0FUaX6-Q_eO1IyLcutFK74oH3yD0ydhg6rCayxQVR_tc582ERP0OgRcDTIMimC7B4gFT0ME_wnwYbswSVFSDEOEK7ZvJ8voWXlVKBpqdy_o6PeCDjt9GLF05vaOJxSftH2n84oevAV-e7vsDhmSzQ0kHuj0KOAEmv3Gms-KCKu-42iqf8iIP7v8ypciwJSAN8FEL8ard6AdlyA4-M2FZ8JUzgZvQvVgujjpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4894ed02a.mp4?token=YgtyDC53-89DTF4-_XreBbhZ1cNuOqIw9uGIt_-pL01McNCFBAJtX7Z06-4TRnrpxwcD3lJnBRhKL8v1RDVFWH3HaiMQueQj_vCoNEaIrCQvxeZKla0FUaX6-Q_eO1IyLcutFK74oH3yD0ydhg6rCayxQVR_tc582ERP0OgRcDTIMimC7B4gFT0ME_wnwYbswSVFSDEOEK7ZvJ8voWXlVKBpqdy_o6PeCDjt9GLF05vaOJxSftH2n84oevAV-e7vsDhmSzQ0kHuj0KOAEmv3Gms-KCKu-42iqf8iIP7v8ypciwJSAN8FEL8ard6AdlyA4-M2FZ8JUzgZvQvVgujjpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اوکراین به مرکز لجستیکی ویلبریز روسیه در شهر الکتروستا حمله کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/672772" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672771">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خبرفوری
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/672771" target="_blank">📅 01:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672770">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
خوک زرد در گفت‌وگو با NewsNation درباره پایان یافتن یادداشت تفاهم با ایران ادعا کرد: اصلاً برایم مهم نیست #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/672770" target="_blank">📅 00:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672769">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
خوک زرد در گفت‌وگو با NewsNation درباره پایان یافتن یادداشت تفاهم با ایران ادعا کرد: اصلاً برایم مهم نیست
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/672769" target="_blank">📅 00:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672768">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11dfde57a3.mp4?token=hdYbQGURWIye7NrIJGOoKv9L2qJqG6mEqzvosqMOj3eoSKBANZ8m-XDrGO5y-SoJ5mzbXr1ZLj1nIqSeZHEDJoY1tp5FXoG9Jelx-0-Bol8R9z18PdJlErL60pzCUAtHSe0_xdUy-ncc7Fd2zf0n-JFPwQ-yUpxUFWC7pRraY9_IOVhJK2sSlJPXT0SZFszbHr487-ZAxl8Zx1Mu-5te4Gf4lYBJFbK_7jl8O04WKTJLM2wChF3SitghnQVDMA1rQmT7gk7J5beAPQmj_Bw3OHQOF_jauWAVyj8bQXk492p6SAmixQGm-vVH6Zt7wZNknX8jbaeNbmG44EBkgcPqwF4b7LqbBKV3s8War_2trS96SSyPGCCemL0It8GdGkvar9TJEQ5oENpnu-sW4IUIKMiCuuInNY6zCQz1eD3aAshp2pHCDBw0VL6JPSil8SreQ3MnrPSJZjrW1mqFASHBAoPQ0Ohu4arPTZO3JVU4EkiPy-PXEeB-y59iajt50VscmD-bGoWo76JyDFvpjOEveQXIg8rjl8jAiLDNKSFXz5q8pugNSQxLiM_N16asJ_SYXyTbD8_8GqocT2drhhBu3dXjwsaeCkVqa3JqPf4XZz8mlicQf5xiAeX3XVYf4XxQNOh-lz5UUWuQOF_IhDWLythazbjVt-sZvbUcO9RY3P4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11dfde57a3.mp4?token=hdYbQGURWIye7NrIJGOoKv9L2qJqG6mEqzvosqMOj3eoSKBANZ8m-XDrGO5y-SoJ5mzbXr1ZLj1nIqSeZHEDJoY1tp5FXoG9Jelx-0-Bol8R9z18PdJlErL60pzCUAtHSe0_xdUy-ncc7Fd2zf0n-JFPwQ-yUpxUFWC7pRraY9_IOVhJK2sSlJPXT0SZFszbHr487-ZAxl8Zx1Mu-5te4Gf4lYBJFbK_7jl8O04WKTJLM2wChF3SitghnQVDMA1rQmT7gk7J5beAPQmj_Bw3OHQOF_jauWAVyj8bQXk492p6SAmixQGm-vVH6Zt7wZNknX8jbaeNbmG44EBkgcPqwF4b7LqbBKV3s8War_2trS96SSyPGCCemL0It8GdGkvar9TJEQ5oENpnu-sW4IUIKMiCuuInNY6zCQz1eD3aAshp2pHCDBw0VL6JPSil8SreQ3MnrPSJZjrW1mqFASHBAoPQ0Ohu4arPTZO3JVU4EkiPy-PXEeB-y59iajt50VscmD-bGoWo76JyDFvpjOEveQXIg8rjl8jAiLDNKSFXz5q8pugNSQxLiM_N16asJ_SYXyTbD8_8GqocT2drhhBu3dXjwsaeCkVqa3JqPf4XZz8mlicQf5xiAeX3XVYf4XxQNOh-lz5UUWuQOF_IhDWLythazbjVt-sZvbUcO9RY3P4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زیارت
از نزدیک‌ترین فاصله
🔹
فیلم یکی از زائران سیدالشهداء از لحظات با شکوه تشییع و ورود پیکر رهبر شهید انقلاب اسلامی از بین‌الحرمین به حرم حضرت عباس علیه‌السلام
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/672768" target="_blank">📅 00:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672767">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
زمین‌لرزه‌ای به بزرگی ۳.۷ ریشتر بندرعباس را لرزاند
🔹
بامداد یکشنبه، زمین‌لرزه‌ای به بزرگی ۳.۷ ریشتر حوالی سرگز در استان هرمزگان را لرزاند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/672767" target="_blank">📅 00:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672766">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9defb1eb81.mp4?token=hmJUW9ZDIMfkGXfEL5kWD6m7JByrBnBBI7AE0gWUqa07cKnK-bqba6fgRDAZQPifUijL5DTN_RcJjWWn7TBjUODNB9M_CGBPZPATmnyqbeEN4fNdx-SKVbBhEykYgLOngNFh0Oae3GoWK-tcxq5tDMlRBzzs-BfJtsvIzieAhGRau4wbwOUNQTdwXUOM2ys58dpAzMx6SmlatmG1ZQmyANMGNPW3CzRU4l0d75QLqOEX7eZ7OYpsmGpruQyh_TpZnJFcO6lt32z50z6MA4mj3Ljr3lQUeVXySmmoG9YEGDNYrosTPUi5LUc-gDNYRuUdeFz6wCSoPKM7eLDlUbe9bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9defb1eb81.mp4?token=hmJUW9ZDIMfkGXfEL5kWD6m7JByrBnBBI7AE0gWUqa07cKnK-bqba6fgRDAZQPifUijL5DTN_RcJjWWn7TBjUODNB9M_CGBPZPATmnyqbeEN4fNdx-SKVbBhEykYgLOngNFh0Oae3GoWK-tcxq5tDMlRBzzs-BfJtsvIzieAhGRau4wbwOUNQTdwXUOM2ys58dpAzMx6SmlatmG1ZQmyANMGNPW3CzRU4l0d75QLqOEX7eZ7OYpsmGpruQyh_TpZnJFcO6lt32z50z6MA4mj3Ljr3lQUeVXySmmoG9YEGDNYrosTPUi5LUc-gDNYRuUdeFz6wCSoPKM7eLDlUbe9bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم انگلیس به فرانسه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
2️⃣
🏆
0️⃣
🇫🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/672766" target="_blank">📅 00:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672765">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
کانال ۱۲ عبری: اسرائیل در حال بررسی امکان اعمال ممنوعیت کامل پرواز پهپادها در آسمان در پی نگرانی‌ها از تغییر روش‌های عملیاتی ایران است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/672765" target="_blank">📅 00:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672764">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
یک منبع دیپلماتیک به اسکای‌نیوز عربی ادعا کرد: ایتالیا پیشنهاد داده است در کنار آمریکا در سازوکار بازرسی از مناطق مورد توافق در جنوب لبنان مشارکت کند تا اطمینان حاصل شود که این مناطق عاری از سلاح‌های حزب‌الله هستند
🔹
این منبع افزود لبنان با مشارکت هر کشور اروپایی در این سازوکار موافق است و اشاره کرد که ارتش لبنان ابتدا در شهر فرون و سپس در مناطق زوطر غربی، الغندوریه، قلاویه، برج قلاویه و صریفا مستقر خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/672764" target="_blank">📅 00:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672763">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e924394c6.mp4?token=hAd5EVdXAL1UIxFDIBmo5-t8EHO1qcoKdb8Rfw-4xminrWFAEy17J3ErQesl337wkEapinTovBbX0YH38SXjpPrDGzq343dKL4_uI6VzTRbdXR60sNQsJBaUxDbIarNPDLKkRSQB3yK003xXo2XEaZA7bb1chzyK8VRp6rKN5mtwdtSZ8j2e1v-LDxElT_a-KOzveQCCBO-WeMa6_Jcm7xOm07gF2aHJWbRHwgZ3MM7eBXvi1s34srZkTJA2SCMc5sI63JXCB5Kq4EwK8xYXclvCjgYi36mqQ5Zi32C72HDT8nSaawcIIPYPms-KbOSLVyAPsNp6XUppgsSYsk-wIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e924394c6.mp4?token=hAd5EVdXAL1UIxFDIBmo5-t8EHO1qcoKdb8Rfw-4xminrWFAEy17J3ErQesl337wkEapinTovBbX0YH38SXjpPrDGzq343dKL4_uI6VzTRbdXR60sNQsJBaUxDbIarNPDLKkRSQB3yK003xXo2XEaZA7bb1chzyK8VRp6rKN5mtwdtSZ8j2e1v-LDxElT_a-KOzveQCCBO-WeMa6_Jcm7xOm07gF2aHJWbRHwgZ3MM7eBXvi1s34srZkTJA2SCMc5sI63JXCB5Kq4EwK8xYXclvCjgYi36mqQ5Zi32C72HDT8nSaawcIIPYPms-KbOSLVyAPsNp6XUppgsSYsk-wIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول انگلیس به فرانسه توسط رایس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
1️⃣
🏆
0️⃣
🇫🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/672763" target="_blank">📅 00:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672762">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
ضربه به شریان نفتی جایگزینِ هرمز در عربستان
🔹
در حالی که عربستان برای فرار از بحران تنگۀ هرمز، صادرات نفت خود را به بندر ینبع در دریای سرخ هدایت کرده بود، گزارش‌های غیررسمی از خسارت به تأسیسات نفتی این منطقه حکایت دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/672762" target="_blank">📅 00:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672761">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eX7owXoZ2yNQfCghggDUDLhbgE2mazEXU4uwOSlvEybV0BYwPyDHRBI-jf0J6PplgiNGUgGMU8-bEDqVIiTpqZzhru7FNjPF52IOzSbiCHlun1mnYDjn5VS_OTW0u7iC9VUEarSY0Cpe1XsYlg99pMavwIQZTxr6OvNAtiOqFVdcdKVDkGtsDdLJbchfEdauL3UJydSJlRgK_L5CewBszTvsWeHT7AiVboAI8NVCR-Qu7f5-TPYjS4QZCliSwHJL4RmZGd0iwq4PwwdX1XWHQ0XNF83M6d9qbgk0yshUQ0yduwspkAOzCW0PHIDZ1lm9bnafLn0QlR1b5_tOX72Rxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا هشدار امنیتی جهانی صادر کرد
🔹
وزارت امور خارجه آمریکا با انتشار یک هشدار امنیتی جهانی، نسبت به افزایش تنش‌ها در خاورمیانه و احتمال تشدید غیرمنتظره بحران‌ها هشدار داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/akhbarefori/672761" target="_blank">📅 00:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672760">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
نیویورک تایمز، به نقل از مقامات آمریکایی: حمله ایران در اردن به تعدادی از بالگردها خسارت وارد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/akhbarefori/672760" target="_blank">📅 00:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672759">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
نیویورک تایمز، به نقل از مقامات آمریکایی: حمله ایران در اردن به تعدادی از بالگردها خسارت وارد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/akhbarefori/672759" target="_blank">📅 00:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672758">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
شبکه اسرائیلی i24NEWS به نقل از منابع خود ادعا کرد که یک هسته وابسته به حزب‌الله لبنان قصد داشت یائیر نتانیاهو، پسر نخست‌وزیر اسرائیل، را در محل اقامتش در شهر میامی ترور کند
🔹
بر اساس این گزارش، سازمان امنیت داخلی اسرائیل (شین‌بت) این طرح را در آخرین لحظات خنثی کرد؛ زمانی که اعضای این هسته پیش‌تر به طبقه زیرین آپارتمان محل اقامت یائیر نتانیاهو رسیده بودند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/672758" target="_blank">📅 00:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672757">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
شبکه CNN گزارش داد که دولت ترامپ به‌طور اولیه با اعطای مجوز به عربستان سعودی برای غنی‌سازی اورانیوم در چارچوب برنامه هسته‌ای غیرنظامی این کشور موافقت کرده است
🔹
اقدامی که در پیش‌نویس توافق هسته‌ای میان واشنگتن و ریاض آمده و اکنون در انتظار امضای دونالد ترامپ است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/akhbarefori/672757" target="_blank">📅 00:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672756">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c06c16cad.mp4?token=niRMLl8reYd20A5vZ9d6jJ8DdMDGId9RiavFV928pdVM2YeFxwo_jUeCiWhvbBew9v6oebCK-LDh52fe0qcbBxdXTt5JVkRxMXkSzI5u41VzBi1caDAFbrsDI8zJOVaieC4mKXMJ8__atTpeH5r53wYg4K7_oUY0jVtTwKjXjEiMtT-nHrh6f80FOfire1rdFH7X1jOsaHim5B_7SHlQO3kKHF35gDMOQlQ4ma5M92UXjAiRKslCwktmbts28KoFmZGJh_YT7X2-2w4vZZakDR132s2o9rRcg-uI2g88uBSDfg2hfBZSIszojCPJmBGnjImEywbDMre7GdBo0SLCQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c06c16cad.mp4?token=niRMLl8reYd20A5vZ9d6jJ8DdMDGId9RiavFV928pdVM2YeFxwo_jUeCiWhvbBew9v6oebCK-LDh52fe0qcbBxdXTt5JVkRxMXkSzI5u41VzBi1caDAFbrsDI8zJOVaieC4mKXMJ8__atTpeH5r53wYg4K7_oUY0jVtTwKjXjEiMtT-nHrh6f80FOfire1rdFH7X1jOsaHim5B_7SHlQO3kKHF35gDMOQlQ4ma5M92UXjAiRKslCwktmbts28KoFmZGJh_YT7X2-2w4vZZakDR132s2o9rRcg-uI2g88uBSDfg2hfBZSIszojCPJmBGnjImEywbDMre7GdBo0SLCQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امروز روز امتحانه و در روز امتحان جز دفاع از خاک راهی نیست!
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/672756" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672755">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHUHjBtddNmnw4DPgJ0qrBzsqyvoXTHyqRjxWhiHKixPPGEk0OXxcdyj91KUedDVg5w0UYtfB15Sx0w8cXvJn14T1Thd_KZAuvpDE929g6zlXAKVTywJZGCXllHowFfrEvGMtDMiwW8ug1du2P3imo5-NWqc4XgpsQSLll3bxSW9hbvRgLGn1j6QPB-Ox-mOevcgNuDfG8NsfHJgm83INEQE0irv9_HfdrIX6eJ0uvzztyBCm7row9HdgqzSAa596Fa-cFsMNCtcSk0oLvrDgwIrjEJavXQKxO_0ol726bpemJedflmvQg83-WuijaXP9mvIY39uUMQNhO4jWmSnJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پارس‌خودرو قیمت جدید ۹ محصول خود را اعلام کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/672755" target="_blank">📅 00:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672754">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FieSlzgb39gmidLXaobo-teQXDSRDyuBBYb67YfUAAZSaVApRzMiNa1esz-roZdXvWd4ZIK-jO82ToWarx6Bd8Tm2CKa_CYjBHIRXxxAsgQ918xxb3a4JPRLImFkqbAzg59sPzFZ5khp2NLmok0iPyBtqMk4xl9RwcAbVvQiOtzAl_XYJeVJXUuhKgbgVXZfMkwJM_Y67lwyf45yRW00Xsj1OkLi6MMuAoiSp76l_dkcrOop1-MxU5D_N1OpHZtQfWwrRS2VjxLNbfN9Ehxxs3q48el7ub9UQ0RMEpPhBr6VCmFPOc2gIcLDKjAInKLW1pzIU4H9-zsaq4LYBY0m_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اتحاد
اعتماد
انسجام
رهبر معظم انقلاب امروز در پیامی فرمودند:
🔹
لازم است به شما مردم باوفا و سرافراز ایران عرض شود که از جمله اصولی‌ترین امور در این برهه، اصرار بر وحدت کلمه و اتحاد مقدّس در همه‌ی سطوح مردم و مسئولان و در تمام عرصه‌ها برای تحقّق آرمان‌های بلند انقلاب اسلامی و تأمین عزّت و استقلال ایران عزیز خصوصاً در برابر دشمن جنایتکار و حیله‌گر امریکایی است. همانگونه که پیش از این مکرّراً و مؤکّداً تذکر داده شد، صیانت از وحدت و پرهیز از تفرقه و تنازع، اختلافات سیاسی و برجسته کردن تفاوتهای اجتماعی وظیفه‌ی همگانی است و البته نقش مسئولان و عناصر دلسوز و دلباخته‌ی انقلاب و امام و رهبر شهید در انسجام و یکپارچگی کشور، مهم‌تر و حسّاس‌تر است.
🔹
هشتصدودوازدهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/672754" target="_blank">📅 00:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672753">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBCQ6NalIGn0aVD7wGk4k5-DEmQ5izM-AKU05ruySL6kRxCrzZ5w42NaQF39n9idHNZVo_EpgyQ8XoludqtzQDvbMU-QdmYiY9-Qly0ez33-VUdkoXvI5tOunWF-Q_tFspHN7zRdpxw35ikzr5rkM7az4MWzqOd8-0mIxgxzt0QdhUwLXchRfPctqYq7YLHiZAUCy0tBP-c9rN-yX8pMfqEk7FzrLxh4IBBQyMTKVmP_k-I6CbFn0X7cQX7ewu4Ar3ChxwrW9SDqTDe5odLMZxpYffzjzPbR8FHq7--kAeixucKnCEvpFEqUyQHZ14oGdUsLUf96wif-5w6jap9GPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وضعیت آب‌گرفته خیابان‌های نیویورک در فاصله ۲۴ ساعت تا فینال جام جهانی ۲۰۲۶ #جام_تایم۲۶
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/672753" target="_blank">📅 00:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672752">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONXDa5Gp_QvHcOuMA05xI6ncPDsm4WqRshKZ1WVbhTthClOeALyFrcPyIElMYp3V68iUE4MfFa9Jyf935fN0FsF4X9va-Ub0zLOgkj6moADMEUFialozb3KXUZI5lFrNi8c-mZ-Z85Uqdg9m_fiBIQeQCqfhnA73SUSpCGldHmc75J6Qz7RsrUSiV5_MMEvAh3OVFlsPmngzA-IBTWu8FjyEJ3_r8Ni4KHIPbY83UG6GA8OCMhYvtX0W3rQC6gKRQjUkfi7nMrxxU_5ScQYQvWLzH5h8abioUvf_aXasqtsXZgA7XfXjddw4cKs6KpuaoYC0rR0e5bNhKgxEarrJRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اطلاعیه فوری برای سهامداران بازار بورس
به درخواست کاربران کارگزاری آگاه و مفید
کارگزاری آگاه و مفید جهت رفاه حال همه کاربران خود در نظر دارد ، سیگنال های تک سهم خرید گروهی را در اختیار کلیه کاربران خود قرار دهد
https://t.me/+werraAXV39phMDZk
از تیرماه۴۰۵ همه کاربران میتوانند از طریق این کانال پربازده ترین سیگنال های خرید گروهی را دریافت کنند</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/672752" target="_blank">📅 00:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672751">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhPngkEIiKyeNiFdoryuLLyEDmfERf8m2ZkQbJHcbnl71wrAPgY59yqKF1DV-NxnXlZ-nph5uZ_6epPxnukDZBNELOZ8Vv6SP4N3nO_joXnXdz3E8s82diWYP5BNsh660B_r4TuGePPz7r0h2INEdcZJWvJoWpG48Ky2ZcrT0A2q5PKEjOfnBelxUMWhVCkG2pGmzebzxhEJBcVYI9KpH4UbyQ3vOYImFsP7BYoP-chnp3TyJCaUHP35SbW7aXGF2BAyXNV9_9SNPjGZaFAxHydF4LcSDZ5t7fXjs0fe1-1kZJDTmF_4KTrqYfyBuVK-NL0fghYjZZ2C8cVcxN7coQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/672751" target="_blank">📅 00:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672750">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3be390f66.mp4?token=BoB69xWb1iABo4aOKFXku8iEAeTPcnGtZIUYZgwecH105S3v1H63IrdFkj2S3-pgbvWsAq5zD8xz6d60VHvPf7743Y2I-rGrAlZQutiaJUj_k78-xsvAe2_1a-BoXDkM_UInZCZmr0zWEREzx1Cgv7ot3pCX6KXRaDARQupMHmJXiR9UWJmHtBIct7GC_Y_IczgfOOdNi2t3x_MklLb0w_dLwE0JgRM0XgV4r22Wrf7e0Tf0oqMCgB2qdouXCalkhI6tS5CMM_gGMrlUEbO7fdGciT8iRdXOaV8KnXjXBUi-5hmIIS2aBrlRfIags7TFTyrqW_AE1MJC9rL2jhRxcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3be390f66.mp4?token=BoB69xWb1iABo4aOKFXku8iEAeTPcnGtZIUYZgwecH105S3v1H63IrdFkj2S3-pgbvWsAq5zD8xz6d60VHvPf7743Y2I-rGrAlZQutiaJUj_k78-xsvAe2_1a-BoXDkM_UInZCZmr0zWEREzx1Cgv7ot3pCX6KXRaDARQupMHmJXiR9UWJmHtBIct7GC_Y_IczgfOOdNi2t3x_MklLb0w_dLwE0JgRM0XgV4r22Wrf7e0Tf0oqMCgB2qdouXCalkhI6tS5CMM_gGMrlUEbO7fdGciT8iRdXOaV8KnXjXBUi-5hmIIS2aBrlRfIags7TFTyrqW_AE1MJC9rL2jhRxcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خسارت سنگین به آکادمی امنیتی کویت در حملات موشکی ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/672750" target="_blank">📅 23:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672749">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d689600b6.mp4?token=DLBx8Gd--ITfFY_WsIly8pEqDgV_vIdEplWkweqPo97hrPHo1bou0v4u52RfqBo1qAHwoGXwgPmvcKpnwYYhG-0yaLXCWnybUlgpzqeWUhoy9elNo0GZjLEyhksoV8VLLdXSkcTD9io5FOmAKYHeWBCzy8iMzFpvFoGv09Y-FAeCDpXB9tJklWbxDsGPpGl8Qd6V2Q9q89EH816qPRI6XXkpyjPZ_gIcAwXd6rKYE8V6ymKRk-WJaV6kigZrcT0two4iDzHcdVqwTOLef5hcZ6g1QFB085rw_4MDez2ypTCRFa2Fr0OpE-mqhHuccB17-GWZXojVYcTd6f8GjWhPkj9rasIyEImz8-26Os6McjUTZnOBkwGmQonh5MVI2xe9gLj6vdgdkCmMqTMlqVn02tOfnfJL-MbQ59jkB3Sw4ps3jSn9COjZHiosqUrpfbU4YVBVv3dG74o2xQwLmSytPXK756GgCtPpiBrSYy2t1LobhPPhedomV5hozUYYvoa_BtaXyWuEzLyf0JJRwlRxQMZ7PJtqmN7P4ylomsHbblfiI8EGbXNKlM0aRaGcsANGr7nUFWS4P51crwPg61R_eHNo3oZR9JiQx5tjxuW128e4Y_WIrJV1zIfIPibAXOWnBWaJCKRt0fDKCLPSfhFxXUeiJWXg7WBGzTIybjxXLiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d689600b6.mp4?token=DLBx8Gd--ITfFY_WsIly8pEqDgV_vIdEplWkweqPo97hrPHo1bou0v4u52RfqBo1qAHwoGXwgPmvcKpnwYYhG-0yaLXCWnybUlgpzqeWUhoy9elNo0GZjLEyhksoV8VLLdXSkcTD9io5FOmAKYHeWBCzy8iMzFpvFoGv09Y-FAeCDpXB9tJklWbxDsGPpGl8Qd6V2Q9q89EH816qPRI6XXkpyjPZ_gIcAwXd6rKYE8V6ymKRk-WJaV6kigZrcT0two4iDzHcdVqwTOLef5hcZ6g1QFB085rw_4MDez2ypTCRFa2Fr0OpE-mqhHuccB17-GWZXojVYcTd6f8GjWhPkj9rasIyEImz8-26Os6McjUTZnOBkwGmQonh5MVI2xe9gLj6vdgdkCmMqTMlqVn02tOfnfJL-MbQ59jkB3Sw4ps3jSn9COjZHiosqUrpfbU4YVBVv3dG74o2xQwLmSytPXK756GgCtPpiBrSYy2t1LobhPPhedomV5hozUYYvoa_BtaXyWuEzLyf0JJRwlRxQMZ7PJtqmN7P4ylomsHbblfiI8EGbXNKlM0aRaGcsANGr7nUFWS4P51crwPg61R_eHNo3oZR9JiQx5tjxuW128e4Y_WIrJV1zIfIPibAXOWnBWaJCKRt0fDKCLPSfhFxXUeiJWXg7WBGzTIybjxXLiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون حقوقی رئیس‌جمهور: علیه ترامپ در دادگاه‌های داخلی و بین‌المللی شکایت کرده‌ایم
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/672749" target="_blank">📅 23:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672748">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
آغاز دور جدید عملیات روانی دشمن با ۳ محور هم‌زمان
🔹
ارزیابی دستگاه‌های اطلاعاتی حکایت از هم‌زمانی ۳ جریان در روزهای اخیر دارد؛ تشدید القای فشار اقتصادی، تحرک رسانه‌ای هماهنگ برخی سلبریتی‌ها و افزایش مواضع انتقادی چهره‌های سیاسی.
🔹
آنچه ناظران را نگران کرده، شباهت توالی این رویدادها با روزهای منتهی به وقایع ۱۸ و ۱۹ دی‌ماه ۱۴۰۴ است؛ الگویی که در آن زمان نیز به اغتشاشات انجامید./فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/akhbarefori/672748" target="_blank">📅 23:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672747">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0TkhWO6rNdZUc9-A2lyYSjpNNzXRUH0N7FOevHL6dziw8uSnMV2HhmpliTrJ2LzkWpdngGzxJyCnTYOr2FvFVr92KIC9keASaunH3Ks69TVCyFLidbtAuMBGHgr2Bh1iLj63FH-reQ1TQ1oofLEbqSxWQRt8sc2ObZzoDswkIg6qzjZNS16mTrRqm1v07LYDTFXCOog2satlOtMggNBjGMHfsC1J73gMYNrI5IpTjf73b1T-asNsOUzSq_VsfNRL5U6B83TZXyKVMOPgR-iLjiN6m0Gv53OD4rhrlaYR1ZY7uWK4aK9yrHTvxX-1HNoC5ed8HY0R2C8tTyriPwE-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمایی دیگر از حملهٔ موشکی دیشب ایران به پایگاه آمریکا در اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/akhbarefori/672747" target="_blank">📅 23:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672746">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
وال استریت ژورنال: مقامات آمریکایی می‌گویند ایران با استفاده از موشک‌های فوق‌سریع و مانورپذیر که رهگیری آن‌ها دشوارتر است، خود را با پدافند هوایی آمریکا سازگار کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/672746" target="_blank">📅 23:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672745">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c524bb9a28.mp4?token=KHvC_x3RQAne_ntWnLQFREhhETMNxUf-IFyZ5ZhHFt1uEg6gfBLrQ7cWm2XIOKy5L2NaHABr5i0Xzmc16Q9jFzbcOhMV4glBIU57SvXLebl1NsaTkQ4KE8_4f3kobICliB1jnm0eF3HuOo_r5tqN1WMdtWxUSsA6uEQP5Zx1PZRxQAsEWCDBVLBBjzwtDzcy3N1lf_-M1SCNXZN55Q-O2iNcPnOfnk2ol1kKgP-Q4r-oGVH514IqtdoIJOPPDbDYag8l-1frnxnglsXGVFuD4ADQB3_T85ZaB0B5QN_jVrnREvQSNbRR0p10yu6CaCh9Dwr5oA-UrPTfzf_fSmk-hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c524bb9a28.mp4?token=KHvC_x3RQAne_ntWnLQFREhhETMNxUf-IFyZ5ZhHFt1uEg6gfBLrQ7cWm2XIOKy5L2NaHABr5i0Xzmc16Q9jFzbcOhMV4glBIU57SvXLebl1NsaTkQ4KE8_4f3kobICliB1jnm0eF3HuOo_r5tqN1WMdtWxUSsA6uEQP5Zx1PZRxQAsEWCDBVLBBjzwtDzcy3N1lf_-M1SCNXZN55Q-O2iNcPnOfnk2ol1kKgP-Q4r-oGVH514IqtdoIJOPPDbDYag8l-1frnxnglsXGVFuD4ADQB3_T85ZaB0B5QN_jVrnREvQSNbRR0p10yu6CaCh9Dwr5oA-UrPTfzf_fSmk-hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ملانی استنسبری، نماینده کنگره: باید عقب‌نشینی کنیم و از جنگ با ایران خارج شویم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/akhbarefori/672745" target="_blank">📅 23:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672744">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbMeUqRDDoRuZzGwTF06pJWa_QdqGTF-O_5S_OXC9dvOhT7WyRtv2X9R58lzfBL4Sk8CZCHIXrQNDOcmJMQUEZmduajMM0-BlISOv5BozzYeseWcgOZU5ZOid7_c0teWK9mQJmAzSxXec7m3K_29rjWOVI5cH0ccmQfSmNvsFoLmZDvevYirKSmYtr2dQC6dDsX-RatL5UNzCSLQIfSsimQtUbQEapfT8RJdqzgVufJeNC1Xemk8iUVOuokDzzt5lYqz96uzaJntnvEJKSQVjTnjhJiciJ1OGICLm0Cc_wWVamAO6MkxL7sFZ77NZRnuqNaGJFt1NGrvPhP77QoFkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«همه باهم برای ایران»/کمپین ملی صرفه‌جویی در وضعیت این روزهای کشور آغاز به کار کرد
🔹
در روزهایی که دشمن شیطان صفت با حمله مستقیم به برخی زیرساخت‌های حیاتی کشور در تلاش است که اراده ملی ما را تهدید کند، نقش مردم در حفظ پایداری کشور بیش از همیشه اهمیت دارد.…</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/672744" target="_blank">📅 23:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672743">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEeC5IowYgZZjphRK14hYWEAn_tBgdZRKS_hzhT9Wmkm6OJYi42IoVp17sGBuOsC6r7a-2CiTBIqDPnt2M-YyWkle5UWpCEey0OF5BbdXy9xfyBq-iAWe_0cqBXRH0Qi4nfQjgkSl3gwTmVa6e1VuugxKGsScHs2mq4OGmzCr_0JZPwwJd4TxUJPCfMpLiEzYcn98kOvm9DAiEEgnrmev59lncCT1BIBjCvEsEIVG3_8zWgzqUzAvXjehzb78kEhzDeQMySONLe1r5MlZq0G0ubW-mx-GCefR2DEuBr7jK2dW8K12vBMsM-2iCGyYonILHW5oCtIP62xhuG0_ooRnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اوکراین حمله پهپادی گسترده‌ای به کریمه و غرب روسیه آغاز کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/672743" target="_blank">📅 23:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672742">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71053f856c.mp4?token=Y3800GHNLVb0_QXEmXxOpFakztZkeK7djuf8hjj9kXEjSP_169SoTlFXbIwAoBV1gM3a3QGyA42uXwPCaf_KCrs_r0enBf7LGBGWSdX9pJswswb0gtPQJ7rarT0OtpE56oOLO0RCzm-tE3wYTJF33tJuEBgUrfJyOvv3HIeeZKum3gKZ4SDzzaCjkrz7tTyFfSUob5RX79jRq2HVOkXCTJCBJAPQUuvXuB8dnw3GdDQIgeil6PNI9JuMSc2eHZniln2VVnL4RmT5GfDHi7fg2UXEIiEAMB7XBZuC0IIyHPEstmo2kjBgds0AshFyR83zPlQV0QLii1Y_9mAhFXMDZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71053f856c.mp4?token=Y3800GHNLVb0_QXEmXxOpFakztZkeK7djuf8hjj9kXEjSP_169SoTlFXbIwAoBV1gM3a3QGyA42uXwPCaf_KCrs_r0enBf7LGBGWSdX9pJswswb0gtPQJ7rarT0OtpE56oOLO0RCzm-tE3wYTJF33tJuEBgUrfJyOvv3HIeeZKum3gKZ4SDzzaCjkrz7tTyFfSUob5RX79jRq2HVOkXCTJCBJAPQUuvXuB8dnw3GdDQIgeil6PNI9JuMSc2eHZniln2VVnL4RmT5GfDHi7fg2UXEIiEAMB7XBZuC0IIyHPEstmo2kjBgds0AshFyR83zPlQV0QLii1Y_9mAhFXMDZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش فاکس نیوز از خسارات قابل توجه به تاسیسات نفت کویت
🔹
پس از آنکه مقامات اعلام کردند تأسیسات نفتی کویت در حملات مکرر ایران مورد اصابت قرار گرفته است، دود غلیظی از تاسیسات به هوا برخاست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/672742" target="_blank">📅 23:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672741">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TanHNbYmGjybgXQlCJyqJabxA2b3cqK_1sQxwGLun4i2-DUgCWo9_tzdSthJfdW7ab1HcD-xp0dfJwwJK2Sa2viGgbGQubOa8B2lqZlTb5qww7Dtz4pq58f1X83k1UqvTAbE2ajaQIrMEuq_1n0P_KdGaFiRS245PyOW13zBTJHtrCdXPcZP5afKv3Sf5jehJlV9a6pdtcAYrioqTmIZ9pACHQGML00atWt3vKCcwpStsqmPfJ1ArVQPep0AsEeqUgW3GkDqavhC-jbC2bfZVLEnBUmsicodKk1n3AwDnhmvtcTIQge_btoU45DUP0ycEipCM-EFMyAixeFIzsYMFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حملات هوایی مجدد رژیم صهیونیستی به جنوب لبنان
🔹
رژیم صهیونیستی روستای «کفر تبنیت» در منطقه النبطیه، واقع در جنوب لبنان را هدف حمله هوایی خود قرار داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/akhbarefori/672741" target="_blank">📅 23:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672740">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
گفتگوی تلفنی وزرای خارجه ایران و عراق
عراقچی:
🔹
روابط ایران و عراق نباید تحت تأثیر برخی اظهارات شخصی و غیر رسمی قرار گیرد.
🔹
ایران بر احترام متقابل، حسن همجواری و توسعه هرچه بیشتر مناسبات با دولت و ملت عراق تأکید دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/akhbarefori/672740" target="_blank">📅 23:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672739">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را از دست ندهید
🔹
🔹
آماده‌سازی همه‌جانبه آمریکا و اسرائیل برای حملات گسترده به ایران
👇
khabarfoori.com/fa/tiny/news-3231341
🔹
بنزین ۱۰ هزار تومانی در راه است
👇
khabarfoori.com/fa/tiny/news-3231318
🔹
پیشنهاد جنجالی مشاور سابق احمدی‌نژاد درباره پروژه انتقام
👇
khabarfoori.com/fa/tiny/news-3231310
🔹
علت نرفتن تندروها به جنوب برای جنگ و همراهی با نیروهای مسلح چیست؟
👇
khabarfoori.com/fa/tiny/news-3231169
🔹
این سلاح کوچک تعیین کننده نتیجه جنگ ایران و آمریکا خواهد بود
👇
khabarfoori.com/fa/tiny/news-3231295
🔹
خبرها را لحظه به لحظه در اپلیکیشن خبرفوری دنبال کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/akhbarefori/672739" target="_blank">📅 23:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672738">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxhzn5MlViXA-KIcySuOhuINLAKSGW34EQqZhLVSx29LydvNxxhTmvyza2ns9usqe2XyfeVHDuLSsB569vfUOazlZRx0KX3jL1eD7AgCUrzV_WIAwFCI24IrNWlMOfgulSAQnDPw0T8hK6ap8uxVviKThL-2XyJy8XfaIbSXUr6wyfWN125F1mdX2KH9WeFuJlZ-T9qqAFG7wkemkv1Utq39Vg8eRjczKGlvSVhQLFptC4fmLkUh5up3Effk_ZTRWMQH-CRXyirmqscQJh8sX6sdbZv5qZGs_ehY8kRm4CuWIfXXcUpbzCFoTXQRfkRUMgxwm2N30HaFNghJ1DEmUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مردم مؤمن عراق در استقبال از قائد عظیم‌الشّأن شهید حماسه‌ای عظیم و پرمعنا آفریدند
🔹
به محضر شریف مراجع عظام، علمای معزّز و اساتید و فضلای حوزات علمیّه و دانشگاه‌ها، اندیشمندان و نخبگان گرانقدر، اُمرا و سران قبائل و شیوخ عشایر و سران طوائف و مردم بزرگوار…</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/672738" target="_blank">📅 23:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672737">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLCw0AB0ZGhus79-fZOP96KlLVH6EafautKe53qaeFlqKfnABKzjCejd9O7t2TV-83GJgn4_VqyFvriGqpdlhWir63mwEBEaBswvfhoTRXopuOB1QjtRpSC3RQo7wKT1ymU2L6Ms15Q_2BTjRsrL80IqIfpWbssjBJ29E3L-kSUYmQBDcV7foJfdZxl2Fl_avBk9iDYuSQ9FGwUapALqe0CtB6yZuBUw856bLlBHgwZFHn1Bce31KAgEPgg66nGOQaLAotsPUqQPOn22WthTeDUA4W1nVLWs4X2aOfach9MF2cPuNfGRfdanvj7ZJ8hkj95eQUr1pev59jerEck__A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تشییع میلیونی و بی‌نظیر علمدار مقاومت، فصل جدید تغییر معادلات مستکبران
🔹
این تشییع میلیونی و بی‌نظیر از علمدار مقاومت، جلوه‌ای تمام عیار از همدلی و اخوّت و هم‌مرامی بین دو ملّت عراق و ایران را نشان داد.
🔹
بی‌تردید سران استکبار با دلهایی هراسان، تصاویر صحنه‌های…</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/672737" target="_blank">📅 23:07 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
