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
<img src="https://cdn4.telesco.pe/file/aziROfLZfeX-RoXJqRolqZOoYeYQVUHx5pY0S8g7epBjBJ5WOZC-sFdm435qJvVzjihMOjy3RPWgQ4OBLxvu_PWoM2JM3xb_BIDV0H2XSJXjnlsiFLIc7rMWNd8NUPbO0JoOU1IJXIbirslyyPlehFy5ktCD0hpDbvtTlxHD9k6bWOnSPhfDhDEWbfDGe6Qd7x6_4LtGgGIKIFT19PgCCiVV76gehBs1bKC45ts8FWtxDJdtuLaVtnYmCvhjPiJTu9hw7aPzJusFR1UgDb1rNbiLKm8dBy5S49IsiHWYGoiboexMsnmmuS05UKevH3eAqbGuYUfcCmNB3hr0swiPIA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.8K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 17:31:58</div>
<hr>

<div class="tg-post" id="msg-131924">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔰
سرویس VIP
🔰
1 گیگ 250T 2 گیگ 500T 3 گیگ 750T 5 گیگ 1.2T 10 گیگ 2T 40 گیگ 5.6T
🛜
مناسب برای تمام سایت ها اپ ها   جهت خرید از پیوی =>  @Winstn_Churchill</div>
<div class="tg-footer">👁️ 182 · <a href="https://t.me/SorkhTimes/131924" target="_blank">📅 16:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131923">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
پژمان جمشیدی به ۹۹ ضربه شلاق محکوم شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 385 · <a href="https://t.me/SorkhTimes/131923" target="_blank">📅 16:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131922">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRBXm8jnraK6bOuhGddjyYWu5esb_CxjbSLjrl9ahl4Yz4W_C84Fpwq5a5VYwn_4K3X0xFu0IGP1xowUg9ygGQymzYpz7fYSjLOLR1uc6YVEC0YCZRoUupSC_42uVNqZrMsxRba4uC4fxzV-eqrqyhsDUSpRZ0b7ct-zkbqgD79TggkdD0yDriNFMAS_cfSZxajMzTNdkZz0cNwp1HiwKTlt0l5BRgpQegc43HcpvgXOZi_xu1K7KOJhZ-k2QUOUNarrV05CEHnikhNedMSpGv0jrWsCP9H0rnR8UN8_wQwD1wofFf6F3Awh9pnzYbdxtecddeYl9grOViPcjaMksg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
احتمالا بخشی از اینترنت زیر ساخت ها در حال اتصال است!
❗️
بر اساس آماری که چارت های رادار کلادفلیر نمایش می دهند،
❗️
طی ساعات گذشته پهنای باند اینترنت کشور افزایش چشمگیری داشته و احتمالا این بدین معناست که اینترنت دیتا سنتر های ایرانی در حال اتصال است.
❗️
احتمالا تا ساعات آینده شاهد وصل شدن بخشی از فیلترشکن های قدیمی در داخل ایران خواهیم بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 403 · <a href="https://t.me/SorkhTimes/131922" target="_blank">📅 16:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131921">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
ادعای خبرگزاری فرهیختگان: آریا یوسفی و مهدی لیموچی در سبد خرید پرسپولیس قرار گرفته اند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 612 · <a href="https://t.me/SorkhTimes/131921" target="_blank">📅 15:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131920">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvpbT_TXDKNOhu2g_AV52_wcrrj4K3s4yaldGvxUl3nVQ9YMqzc4jnobjbhjo0JQIQ7-0-zTHJ4OduBgyXApFtRArqhINBDUINbWc1vw1sOKw4QMdsIUdOL2qp3-ELEP7CViH8pS7G0fytIIqHHVQ3mhMotarvTyu_uKH7RO-BAFTvYafPXswsgRRiN_OsU8pAzspM6s6MmWp_gK62F86KdI3OUBjqueLdTICXpK0LzHcuFixT6Q0CtXEx902hp07RLwgLK5Zko2kwJEXKVEHDb19ptGOD_zvjnc21OJugFBiHKSh_4jElECCf0s1Co4rFueAEI4zgMb_JDU4TL0tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ادعای خبرگزاری فرهیختگان: آریا یوسفی و مهدی لیموچی در سبد خرید پرسپولیس قرار گرفته اند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 624 · <a href="https://t.me/SorkhTimes/131920" target="_blank">📅 15:29 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131919">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
فووری؛ اوستن اورنوف ستاره ازبک پرسپولیس در تمرینات تیم ملی این کشور مصدوم شده و وضعیتش برای جام جهانی نامشخص است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 599 · <a href="https://t.me/SorkhTimes/131919" target="_blank">📅 15:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131917">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">بعد از ۷ بار تلاش سنای آمریکا، با رای ۵۰ به ۴۷ قطعنامه
اختیارات جنگ در ایران
رو تصویب کردن
این اختیارات ترامپ رو محدود میکنه البته احتمالا خود ترامپ اونو
وتو
کنه. مهم‌ترین تاثیرش اینه که دموکرات ها کم کم دارن قدرت بیشتری پیدا میکنن و برای
انتخابات
بعدی دست بالاتر رو پیدا میکنن
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 601 · <a href="https://t.me/SorkhTimes/131917" target="_blank">📅 15:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131916">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔰
سرویس VIP
🔰
1 گیگ 250T
2 گیگ 500T
3 گیگ 750T
5 گیگ 1.2T
10 گیگ 2T
40 گیگ 5.6T
🛜
مناسب برای تمام سایت ها اپ ها
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 715 · <a href="https://t.me/SorkhTimes/131916" target="_blank">📅 12:36 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131915">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICqyx3iIfIdlhkRgjYYQ_5mLDZijHBNsu0SpIXLYrvOhAMSEclG3MqS3HsGwujla2aDudAk85PcHj1n3MpEDb6oAmw3fLaNKVERIVV-PWSFJ02du_RVZyEoqHzIKMOjo_MDFLQ5_GfxDoejRd2oyyOTKjPWuDPOJrygqv29GLjoLKX_WLqFud7UDyibdUVoSl0y9XB0xUPHT2rysQOEnGz0qlAWOLwWwt9ToDgilVQiUxIgcwpunPv1UPPaJPmWcQyOHg89bHmg3vh-tHxXVnmmJrEqDLUkyzHB5iUFRfBImXRQ-mPvIVsIokNdxdXbhL1tqsUKpGp08z1sGaOKSag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
توییت مهدی روزخوش مدیر رسانه ای باشگاه
😂
👌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 694 · <a href="https://t.me/SorkhTimes/131915" target="_blank">📅 12:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131914">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDLSTab9dg4xP3IvMIRtFbwUXaD2k1SYwIvAexD8pU58oQK69E1a-MsBcJkn7-g3X9mVt8RUoC6M9mwwW5qEDjQKjjq6lUMG1SzpNmyJpjqf2O4OLuCCSlKqMJ-t4FyXS187N-fy3CbSjReWfZWQ5YTP0hSwihH-JXcBWW-GvVULVWXtsRMEJw9_IFpEC8HCLFmD16qLuTTws1MZcdyNeYc5YYXdXPnQDj1brg4D7UZxaljQ2etWjMJePWKcKZ6-fHszsTjAYA_Wwa8j8Q5ou8z1p1l_MgguUySgimlw1jRGi_dwe6_K7Q_IyMppgvWia_C3cOD2oh9V0I4Xi9eQuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این روزا قبل از شرط‌بندی بیشتر از خود بازی باید نگران این باشی که VPN وصل میشه یا نه.
😀
ربات تلگرام وینکوبت دقیقاً برای همین شرایط خوبه چون کل سایت داخل خود تلگرام اجرا میشه و دیگه لازم نیست هی بین سایت و VPN درگیرشی:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
میتونی مستقیم وارد بازی‌ها و کازینو شی، پیش‌بینی ثبت کنی، واریز و برداشت انجام بدی و همه‌چی خیلی سریع‌تر و راحت‌تر انجام میشه.
🟣
آدرس دائمی سایت:
wincobet.com
📌
کانال رسمی وینکوبت:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 658 · <a href="https://t.me/SorkhTimes/131914" target="_blank">📅 12:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131913">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
ترامپ درباره ایران: ممکن است مجبور شویم ضربه بزرگی دیگر به آنها وارد کنیم. هنوز مطمئن نیستم
🔹
خیلی زود خواهید فهمید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 634 · <a href="https://t.me/SorkhTimes/131913" target="_blank">📅 12:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131912">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">محمد پروین، فرزند علی پروین:   پدرم به دلیل زخم پا (به علت دیابت) در بیمارستان بستری شده است، اما مشکل خاصی ندارد و به زودی مرخص می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 639 · <a href="https://t.me/SorkhTimes/131912" target="_blank">📅 12:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131911">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0T9VlJawS0_akaZOyWhBrLKRpZfV8w34WpSwEKch8OwGGcLNy9J5bBP_Bp8LwVRNsYlZAdmJUpXF5eoypZNI8HVpsWfiGJD1d2Ezj85YXHFqTN5ZJsIPrFJXr7jDyXBdEL_SLZayoSIQ-m4VIDF1DpzFNWACmxP4lNy2_QtEoCwxge2qFuaY5lgnbkXWocbEolmKMwx6qz5FYSCTp69elOX8FYPbUDEh-4jn-n0fbDTgpU1fCQR3NTvm4gwpjbbJTOPh4lNnCpJ6uVvDCqilMoG5w8W161FJgxrubnNO7DSZmu7YyCCOYN6fhvryAVbS5_kETN4DzQAaYJY76uQ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نیویورک تایمز :
🔴
فیفا قصد دارد دوباره ورود پرچم «شیر و خورشید» ایران پیش از انقلاب و لباس‌های مرتبط با آن را به ورزشگاه‌های جام جهانی ۲۰۲۶ ممنوع کند. این پرچم در جام جهانی ۲۰۲۲ قطر هم محدود شده بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 738 · <a href="https://t.me/SorkhTimes/131911" target="_blank">📅 10:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131910">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
شایعه حضور تارتار روی نیمکت پرسپولیس از کجا آب می‌خورد؟
💸
یک دلال با سوءاستفاده از شرایط جنگی و شایعات درباره بازنگشتن خارجی‌ها ، پیشنهاد داد در صورت نیامدن اوسمار ، تارتار سرمربی پرسپولیس شود.
⛔️
این پیشنهاد جدی گرفته نشد و مدیران پرسپولیس قصد دارند همکاری…</div>
<div class="tg-footer">👁️ 752 · <a href="https://t.me/SorkhTimes/131910" target="_blank">📅 10:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131909">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✅
ونس معاون اول رئیس‌ جمهور در مصاحبه جديد خود اعلام کرد اصلا متوجه نمیشم مقامات رژیم ایران چه میگویند یا چه چیز میخواهند فهمیدن حرف هایشان واقعا سخت است و مدام حرف ها و خواسته هایشان تغییر میکند و نميتوانند به یك تصمیم واحد برسند ، اون 440 کیلو اورانیوم باید…</div>
<div class="tg-footer">👁️ 753 · <a href="https://t.me/SorkhTimes/131909" target="_blank">📅 10:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131908">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
قاتل الهه حسین زاده با اذان صبح فردا اعدام می‌شود.
❗️
استوری خواهر الهه: امشب، قصاص مرهم داغ خواهرم نمی شود... اما شاید کمی از بی عدالتی این دنیا کم کند. الهه جانم...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 745 · <a href="https://t.me/SorkhTimes/131908" target="_blank">📅 10:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131906">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">●
بدترین حس وقتیه که میخوای سریع وارد سایت شی، بازی شروع شده، ولی VPN وصل نمیشه یا سایت نصفه لود میشه.
😑
● برای همین
ربات تلگرام وینکوبت
این روزا خیلی کاربردیه چون کل فضای سایتو داخل خود تلگرام میاره و عملاً بدون دردسر میتونی مستقیم وارد بازی‌ها و کازینو شی:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 900 · <a href="https://t.me/SorkhTimes/131906" target="_blank">📅 00:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131904">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❗️
#فارس مدعی شد ؛ مدیرای پرسپولیس اصراری به موندن علیپور ندارن و اگر اوسمار هم بگه نمیخوام قرارداد علیپور تمدید نمیشه.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 968 · <a href="https://t.me/SorkhTimes/131904" target="_blank">📅 23:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131903">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">⚪️
مهدی تاج: اگر پرچمی به جز پرچم جمهوری اسلامی وارد استادیوم شود به آمریکا نخواهیم رفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 968 · <a href="https://t.me/SorkhTimes/131903" target="_blank">📅 23:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131902">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
⭕️
🔴
حضور حسین کنعانی زادگان و رضا درویش در منزل خانواده زنده یاد الهه حسین‌نژاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 968 · <a href="https://t.me/SorkhTimes/131902" target="_blank">📅 23:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131901">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">⚖
پژمان جمشیدی تو جلسه دادگاهی امروزش: «من قسم میخورم که هیچکاری نکردم و این اتهام درست نیست. من با این دختر کاری نکردم و اصلا بهش دست هم نزدم. به روح مادرم قسم میخورم که من کاری باهاش نکردم.»
◽️
وکیلش هم گفت ادله و مستنداتی به دادگاه ارائه دادیم که بی‌گناهی…</div>
<div class="tg-footer">👁️ 909 · <a href="https://t.me/SorkhTimes/131901" target="_blank">📅 23:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131900">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">💢
مزخرفات خنده دار سهراب بختیاری زاده سرمربی کیسه: یک ذهنیت به وجود آمده است که پرسپولیس عادت کرده است که بعضی وقت‌ها با فساد بازی را ببرد یا به این عادت کرده است که همیشه دستش را  به نحوی بگیرند و کمکش کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 952 · <a href="https://t.me/SorkhTimes/131900" target="_blank">📅 22:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131899">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">💢
مزخرفات خنده دار سهراب بختیاری زاده سرمربی کیسه: یک ذهنیت به وجود آمده است که پرسپولیس عادت کرده است که بعضی وقت‌ها با فساد بازی را ببرد یا به این عادت کرده است که همیشه دستش را  به نحوی بگیرند و کمکش کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 873 · <a href="https://t.me/SorkhTimes/131899" target="_blank">📅 22:19 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131898">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7eae73a44.mp4?token=JtuDKVnhebJF8VfaA9eJr50u0khZcr3p10hbN7wnRv8fupnMi9lEORG8nbYW8jvJZEwBaKGnDInUyU0De6KOR62CxsTfB6N9a5x39plha8MnOIRl3F_RFRGvYfTEG137gPXSGC8QfJssaVKb3FhpmbVHilk0I-nWdG_CXIr6WZpVpXxML463fi-0rQUwhfl6G8dP795X44JHIWXuoCIEkoNnJjwyZv8QQBseMaSiAkhOfgLTNGI4b1TuVPvGuGkRqOVTYgIWV53_3tSlsxUMxa-IljbfXlfS1cnAGd1kPPpOLPn3EOVIYJhVyWmzRjg0TVZ6b8V75ByMIkSf0Jvzug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7eae73a44.mp4?token=JtuDKVnhebJF8VfaA9eJr50u0khZcr3p10hbN7wnRv8fupnMi9lEORG8nbYW8jvJZEwBaKGnDInUyU0De6KOR62CxsTfB6N9a5x39plha8MnOIRl3F_RFRGvYfTEG137gPXSGC8QfJssaVKb3FhpmbVHilk0I-nWdG_CXIr6WZpVpXxML463fi-0rQUwhfl6G8dP795X44JHIWXuoCIEkoNnJjwyZv8QQBseMaSiAkhOfgLTNGI4b1TuVPvGuGkRqOVTYgIWV53_3tSlsxUMxa-IljbfXlfS1cnAGd1kPPpOLPn3EOVIYJhVyWmzRjg0TVZ6b8V75ByMIkSf0Jvzug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
مزخرفات خنده دار سهراب بختیاری زاده سرمربی کیسه: یک ذهنیت به وجود آمده است که پرسپولیس عادت کرده است که بعضی وقت‌ها با فساد بازی را ببرد یا به این عادت کرده است که همیشه دستش را  به نحوی بگیرند و کمکش کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 881 · <a href="https://t.me/SorkhTimes/131898" target="_blank">📅 22:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131897">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
باشگاه پرسپولیس: ما میگیم لیگ برگزار بشه ولی ما رو نادیده میگیرن، اونوقت تیم‌هایی که میگن لیگ کنسل بشه، معرفی میشن واسه آسیا. نمایندگان ایران تو آسیا باید با عدالت و در زمین فوتبال معلوم بشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 859 · <a href="https://t.me/SorkhTimes/131897" target="_blank">📅 22:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131896">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✅
💢
بیرانوند از جام جهانی محروم نمی‌شود
💢
رسول باختر، حقوقدان ورزشی در گفت‌وگو با ایسنا: در رای استیناف آمده بود که محرومیت بیرانوند شامل مرحله نهایی مسابقات بین المللی در تیم ملی نیست.
💢
با توجه به این موضوع، حتی در صورت صدور رای CAS پیش از جام جهانی، بیرانوند…</div>
<div class="tg-footer">👁️ 850 · <a href="https://t.me/SorkhTimes/131896" target="_blank">📅 22:04 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131895">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
نصیرزاده، وکیل علیرضا بیرانوند: در صورتی که حتی رای محرومیت ۴ ماهه این دروازه‌بان توسط دادگاه CAS تایید شود، محرومیت وی شامل جام جهانی نخواهد شد.
⏺
به محض اینکه هزینه دادرسی واریز شود، رای صادر نمی‌شود. تا بخواهند رای را صادر کنند جام جهانی تمام شده است.…</div>
<div class="tg-footer">👁️ 827 · <a href="https://t.me/SorkhTimes/131895" target="_blank">📅 22:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131894">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❗️
پرسپولیس شاکی از بمب درویش/ حدادی: اجازه دهید دلایل را نگویم!
🔴
مناقشه باشگاه پرسپولیس با سرژ اوریه، مدافع سابق این تیم، وارد مرحله جدیدی شده و این باشگاه رسماً علیه بازیکن ساحل عاجی خود شکایت کرده است. پیمان حدادی، مدیرعامل پرسپولیس، با اعلام این خبر، ابراز…</div>
<div class="tg-footer">👁️ 848 · <a href="https://t.me/SorkhTimes/131894" target="_blank">📅 22:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131893">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
ترامپ درباره ایران: ممکن است مجبور شویم ضربه بزرگی دیگر به آنها وارد کنیم. هنوز مطمئن نیستم
🔹
خیلی زود خواهید فهمید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 920 · <a href="https://t.me/SorkhTimes/131893" target="_blank">📅 21:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131892">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2773afe10e.mp4?token=L8Sua2jpvqOHyH0J4R0yy1zR0Bt-Vcy7J8xHOvy4vWK2wzoeLpXmafZ2xiMI_cu81ktuM1U1iZS-60gnoeovJhhptKKZLCbit10Lsm0iGZuzaex-mc-kRS7wD4oJjUZlaSUz7O_68aXHULYnrihGVIUeGqH-V6AGPdv-KfpOK2C-SQNLIc463NejfrejfaXiYkRD8mmDt-9xgJ3dvPqtoQYhyA6ydW2IzdWgMyhHidkJdy8GCh8OT2IYdRuiVQULeVq3Jw7z2tSIQTYGYg_ezC2lydMHjR56sLq3lMheFWSvS7-MgpSXmQQQ_Dn-ifaepfpJnZNaZf_fPyCgjtW_ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2773afe10e.mp4?token=L8Sua2jpvqOHyH0J4R0yy1zR0Bt-Vcy7J8xHOvy4vWK2wzoeLpXmafZ2xiMI_cu81ktuM1U1iZS-60gnoeovJhhptKKZLCbit10Lsm0iGZuzaex-mc-kRS7wD4oJjUZlaSUz7O_68aXHULYnrihGVIUeGqH-V6AGPdv-KfpOK2C-SQNLIc463NejfrejfaXiYkRD8mmDt-9xgJ3dvPqtoQYhyA6ydW2IzdWgMyhHidkJdy8GCh8OT2IYdRuiVQULeVq3Jw7z2tSIQTYGYg_ezC2lydMHjR56sLq3lMheFWSvS7-MgpSXmQQQ_Dn-ifaepfpJnZNaZf_fPyCgjtW_ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ درباره ایران: ممکن است مجبور شویم ضربه بزرگی دیگر به آنها وارد کنیم. هنوز مطمئن نیستم
🔹
خیلی زود خواهید فهمید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/SorkhTimes/131892" target="_blank">📅 19:19 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131891">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
🔴
اگر وحید هاشمیان و پرسپولیس توافق نکنند، تکلیف صدور کارت مربیگری اوسمار چه می شود؟ هوشنگ نصیرزاده پاسخ می دهد
‼️
‼️
نصیرزاده: برای فسخ قرارداد یا برکناری سرمربی هیچ محرومیتی تعیین نشده است و فقط باید غرامت پرداخت شود. اگر در قرارداد وحید هاشمیان مبلغی برای…</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/SorkhTimes/131891" target="_blank">📅 18:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131890">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
باشگاه پرسپولیس با ارسال نامه‌ای به مسعود پزشکیان خواستار جلوگیری از بی عدالتی در اعلام نمایندگان ایران برای فصل بعد رقابت‌های فوتبال آسیا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/SorkhTimes/131890" target="_blank">📅 18:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131889">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
اعتراض کنایه‌آمیز باشگاه پرسپولیس: نماینده ایران در آسیا نباید با تصمیمات سلیقه‌ای و خارج از زمین فوتبال مشخص شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/131889" target="_blank">📅 18:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131887">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✅
با اعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/131887" target="_blank">📅 15:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131886">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">⚡️
حکم جلب رشید مظاهری گلر سابق کیسه به خاطر بدهی ۴ میلیاردی صادر شد، میگن متواری شده!
⚡️
عجیبه با این قرارداد های میلیاردی که داشتن ۴ میلیارد بدهکار باشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SorkhTimes/131886" target="_blank">📅 15:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131885">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
یکی از گزینه‌های اصلی باشگاه ، برای گلر ذخیره جایگزین امیررضا رفیعی آرمین عباسی گلر جوان پیکان تهران است   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/SorkhTimes/131885" target="_blank">📅 15:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131884">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPRLsXSQHiYgaftI4L06nRkBY1NpwhdAzTdOUg_emp7UVbP4e2GxqKlyPFjsgkt7qI1vhiZlpZxEcpPty8H_l9L_os1w3w55WufPNp-OPg7C9cdk0lYqm06s_rs6ms1DE2Pbum2QaYvbBgzPVLRKuiFY_W-JllWqiriFTfPayX7woP_FiKQjWOmuy8FgY6szaRejJ7YhaBQJgc8a253YzLsIEMhHQEvIlMs8_0oIgA4nMadiNfFsv7umX6JHxNlQXJ5FT0njUkWbZFIlw9ecJaxAaUg95_rCcZbu5mXRX9TvWXX25Otu2k4SKjHGcXziDcJ8zDN10bpXPQ--tKFiVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اعتراض کنایه‌آمیز باشگاه پرسپولیس: نماینده ایران در آسیا نباید با تصمیمات سلیقه‌ای و خارج از زمین فوتبال مشخص شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/131884" target="_blank">📅 15:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131883">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
ترامپ درباره ایران : من فعلاً عقب انداختمش، امیدوارم شاید برای همیشه، ولی شاید هم فقط برای یه مدت کوتاه
🔴
چون با ایران مذاکرات خیلی مهمی داشتیم و باید ببینیم چی ازش درمیاد  -
🔴
از من خواستن عربستان، قطر، امارات و چند کشور دیگه که اگه میشه این رو دو سه روز…</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SorkhTimes/131883" target="_blank">📅 12:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131882">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
علوی، سخنگوی فدراسیون فوتبال: دو هفته بعد از 10 خرداد و به طور کلی قبل از جام جهانی باید سهمیه‌ها را به AFC اعلام کنیم/ استقلال، تراکتور و سپاهان الان هستند ولی قطعی نیست؛ باید مجوز حرفه‌ای آنها صادر شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/131882" target="_blank">📅 12:53 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131881">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYJRIYE77Qp3ITBLrVidSDYMN9vRACVkIq2yT3ak_UtF0IX2qzbbwUiU3ug00EpWJt-jq2s4XMrqwdclNQ3L56sTeqmuptPnNCUCKfSvmqN3DTFGu_kUwtsjgzPDisK0_ESkoaEbnpC6iPtbrightIQ_bokDcj-gFjgYOtytYT2K88tyYAH-42KL_WPTj-KfNig8I7H7F_pO6x8jKs7DDqDAvieCHnJe0A2wO0xmB69JAKXPorhDmKYjy-QCLwGED-1xT5J1tgdUUVeILJY22p3EYe7-cfzXNrKl4CwZcJjup6YfH6a9wW9sJbBeDOVfnkqu0tFIe35hTcYoeuG3XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
یک تراکتوری در رادار پرسپولیس
◽️
با توجه به نیمکت نشینی صادق محرمی در این فصل در تیم تراکتور به نظر می‌رسد در انتهای فصل از این تیم جدا شود و با توجه به تمدید احتمالی اسماعیلی‌فر و حضور مهدی شیری در پست دفاع راست تراکتور صادق جایی در ترکیب تراکتور نخواهد داشت و از پرسپولیس به عنوان متحمل ترین گزینه وی یاد میشود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/SorkhTimes/131881" target="_blank">📅 12:52 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131880">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
تغییر بزرگ در نقل‌وانتقالات؛ لیگ برتر ایرانی‌تر می‌شود
❗️
فوتبال باشگاهی ایران در آستانه فصل جدید رقابت‌های لیگ برتر با شرایطی متفاوت نسبت به سال‌های گذشته روبه‌رو شده و به نظر می‌رسد سیاست اکثر باشگاه‌ها در نقل‌وانتقالات تابستانی به سمت کاهش هزینه‌ها و استفاده بیشتر از بازیکنان داخلی تغییر کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/131880" target="_blank">📅 12:48 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131879">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔰
سرویس VIP
🔰
1 گیگ 250T
2 گیگ 500T
3 گیگ 750T
5 گیگ 1.2T
10 گیگ 2T
20 گیگ 3.5T
40 گیگ 5.6T
🛜
مناسب برای تمام سایت ها اپ ها
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/131879" target="_blank">📅 11:04 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131878">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🛜
سرور نامحدود 1 ماهه
Anyconnect
سرعت عالی،یوتیوب رو هم ساپورت میکنه
فقط و فقط 4.5T
🔥
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/SorkhTimes/131878" target="_blank">📅 09:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131877">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mf3Qvra4hxnQhBJfn0RjwFTlSXrNuEhHvRXETZFjo6nG9BMMz80yscOgh4tImG9aTeXPZAk1sDV_2WcDaHtqTjXvocB9esDHDDFD9b-6lL4S45RhektUnIFFikMOBcHzGWnPPscCdtjmLlCOQNOD7eHzAHJDcf5lDed4VeXtSg5OyK3KcQ_2LA_ai-FZk-CaCgypLzeekeHszJfj21NglTPKH7tFI9_m4gAf0wgeXh7wZJTtXDum6bl8foJH5hxLjNXGoTrtKFup6jwL59fF12XH93X7rSZz7WuFB3Rz2UqvwY-BWNVCw7rqVlszWPgjPLDwiqdPDAB0L8FImFrWJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
دسترسی سریع و مستقیم به
وینکوبت
📌
دیگه لازم نیست بین لینک‌های مختلف بگردی یا وقتت تلف بشه.
📌
فقط با یک ورود ساده به ربات رسمی، مستقیم وارد سایت شوید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
⚡️
ورود سریع و بدون معطلی
⚡️
بدون لینک‌های اضافی و گیج‌کننده
⚡️
دسترسی مستقیم از داخل تلگرام
😀
همه چیز برای راحتی کاربران داخل ربات فراهم و قرار داده شده.
🔵
برای تحلیل‌ها و اخبار سایت وارد کانال سایت شوید:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SorkhTimes/131877" target="_blank">📅 02:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131876">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe16cfa21f.mp4?token=SX0I351hp5PStnXEqJvRkqh79TT4NbR1yalixZhBevVdgk-MbdegMWER3qtl4Fd_WbSUMVezqRaQPf6P7ABnqeM7SipXKC1PVA1vMVpZCEqHzCBM7vH21c3LZXSS7sphbOwIilPlDvMXE24HooK06Ap7c95r2gBEOpF_VKXI_GgSoXjdpSmXxRCIHcpkFSxQqFv1WDx9cwCjb9GrThrXABs3y6s7a9HaFUhOWS0jwcDe_VdwFdmDN3MnsXRwsGO0Fcl-IcrC0pH3l2NdOm3J6NQKdjJ6KffR7belHtD2eAr7tk9D4JQ21lB4Rn8K_U4ueBtetuCpq2Z5o6xSjtPhSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe16cfa21f.mp4?token=SX0I351hp5PStnXEqJvRkqh79TT4NbR1yalixZhBevVdgk-MbdegMWER3qtl4Fd_WbSUMVezqRaQPf6P7ABnqeM7SipXKC1PVA1vMVpZCEqHzCBM7vH21c3LZXSS7sphbOwIilPlDvMXE24HooK06Ap7c95r2gBEOpF_VKXI_GgSoXjdpSmXxRCIHcpkFSxQqFv1WDx9cwCjb9GrThrXABs3y6s7a9HaFUhOWS0jwcDe_VdwFdmDN3MnsXRwsGO0Fcl-IcrC0pH3l2NdOm3J6NQKdjJ6KffR7belHtD2eAr7tk9D4JQ21lB4Rn8K_U4ueBtetuCpq2Z5o6xSjtPhSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجری فوتبال برتر: فردا قرار است جلسه‌ای برگزار شود تا چمن استادیوم آزادی را به بهانه ویروسی شدن جمع کنند و سپس طرح هیبریدی اجرا شود.
🔹
ما چمن هیبریدی را در تبریز دیدیم. نکند چمن آزادی هم به همین سرنوشت دچار شود. چمن در فوتبال ایران مافیا دارد. مراقب باشید کاسبی اتفاق نیافتد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/131876" target="_blank">📅 01:48 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131875">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
ترامپ درباره ایران : من فعلاً عقب انداختمش، امیدوارم شاید برای همیشه، ولی شاید هم فقط برای یه مدت کوتاه
🔴
چون با ایران مذاکرات خیلی مهمی داشتیم و باید ببینیم چی ازش درمیاد  -
🔴
از من خواستن عربستان، قطر، امارات و چند کشور دیگه که اگه میشه این رو دو سه روز…</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SorkhTimes/131875" target="_blank">📅 01:28 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131874">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
ترامپ : ما داشتیم آماده می‌شدیم که فردا یه حمله خیلی بزرگ و جدی انجام بدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/131874" target="_blank">📅 01:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131873">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26879febf9.mp4?token=GPcf8Zwy8IolA94yGl8Dy0W76OXyZ93_LUfkG_FBrM_BXi3wrZIYUphv-hh3a2t4jGJG11-iMSZMeq11QJCnRG1Q1QIMJ0XbmRsqEqJh6SV7Bsr7157-o84H24bGOFILYknQCvr2VotilN7VK9zK6mtXYBvZL6eern-po_Q_0h2W0ClFN7Eaw_J38QIw4XoCCdeuu2VgQx3WguF_tVZuNyHkGfFqRBdxp_irXMATXxtIf2IK2FrkT4WsH8yQizY0Rf5-Kn98Q5rLqgH4D3zIQ9sMZyq6jlSr3pJhKD9tSB5c_6TIdAYfGFs4CZRsornZ_GhJ_z4PrxusfCiadVA1pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26879febf9.mp4?token=GPcf8Zwy8IolA94yGl8Dy0W76OXyZ93_LUfkG_FBrM_BXi3wrZIYUphv-hh3a2t4jGJG11-iMSZMeq11QJCnRG1Q1QIMJ0XbmRsqEqJh6SV7Bsr7157-o84H24bGOFILYknQCvr2VotilN7VK9zK6mtXYBvZL6eern-po_Q_0h2W0ClFN7Eaw_J38QIw4XoCCdeuu2VgQx3WguF_tVZuNyHkGfFqRBdxp_irXMATXxtIf2IK2FrkT4WsH8yQizY0Rf5-Kn98Q5rLqgH4D3zIQ9sMZyq6jlSr3pJhKD9tSB5c_6TIdAYfGFs4CZRsornZ_GhJ_z4PrxusfCiadVA1pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : ما داشتیم آماده می‌شدیم که فردا یه حمله خیلی بزرگ و جدی انجام بدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/131873" target="_blank">📅 01:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131872">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0edd05b28.mp4?token=NeMX6wW6bE1TFRfZxCXsz14GVP5kHQIULXA7iG_9YJ4rxRGdK7uBBlZ-4E111427fWYZnaBrwwSwao8CzWKrvpMiiJOlabK6m1PNaFeXY2L-Gm-YUV81YV4JerEUX_3Exq-Z3vVTiYq7qdyDwIM1s1EHRFhgRfyQs1V21dvIBn-UGYdgbTh4j4sd0qP4BCfIdvOx_-3siXzsNdZYniSLrj0PoCYFiE8tEShCLC_0-kNY3977MS_GiENgAeg9lWfv66k3T_eAX1jtlXb6NYmXXi4lAvjP8WG4o0h04jwK5psP9HIW38GfBsCHVYKzQFbjfalTv0tn0cgm-YysGC0jwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0edd05b28.mp4?token=NeMX6wW6bE1TFRfZxCXsz14GVP5kHQIULXA7iG_9YJ4rxRGdK7uBBlZ-4E111427fWYZnaBrwwSwao8CzWKrvpMiiJOlabK6m1PNaFeXY2L-Gm-YUV81YV4JerEUX_3Exq-Z3vVTiYq7qdyDwIM1s1EHRFhgRfyQs1V21dvIBn-UGYdgbTh4j4sd0qP4BCfIdvOx_-3siXzsNdZYniSLrj0PoCYFiE8tEShCLC_0-kNY3977MS_GiENgAeg9lWfv66k3T_eAX1jtlXb6NYmXXi4lAvjP8WG4o0h04jwK5psP9HIW38GfBsCHVYKzQFbjfalTv0tn0cgm-YysGC0jwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جمله عجیب سخنگوی فدارسیون خطاب به تیم‌هایی که هفته اول خرداد تمرینات‌شان شروع می‌شود
◻️
علوی: شاید آنها خبری دارند که ما نداریم؛ ورزش کردن اتفاق خوبی است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/131872" target="_blank">📅 01:22 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131871">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db79861a4e.mp4?token=L1LsgjvwdOuOMY3ZYRa5-GacwNm39QMufMNAuv4OuthXeQZdmWBL8wYvBN269I_BiHOVngdg7w-ARQ0kqgqGW6PWpYtY-e1BRa28qDNfcTgOEuPuMgx515JNnveG-yy8UWimwo_md3a_pwbut7c6Xy124hghpNaQ8cRxuF5GFmGO59WzOdgFVbJuiQ9Dph_38Gszx6bBURFxdhrFZigUKz902CIXh_GindGBzSh4RCqsHnXkpgi-ItCg8BO0SlTlA8MjXhBbmhSemH55xQlD6IvIqy5kqZtNAL0XGupwVIWWl3vqLh96A9zR21RUqXxamcIHAstjLHO3Q9VzYB7dHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db79861a4e.mp4?token=L1LsgjvwdOuOMY3ZYRa5-GacwNm39QMufMNAuv4OuthXeQZdmWBL8wYvBN269I_BiHOVngdg7w-ARQ0kqgqGW6PWpYtY-e1BRa28qDNfcTgOEuPuMgx515JNnveG-yy8UWimwo_md3a_pwbut7c6Xy124hghpNaQ8cRxuF5GFmGO59WzOdgFVbJuiQ9Dph_38Gszx6bBURFxdhrFZigUKz902CIXh_GindGBzSh4RCqsHnXkpgi-ItCg8BO0SlTlA8MjXhBbmhSemH55xQlD6IvIqy5kqZtNAL0XGupwVIWWl3vqLh96A9zR21RUqXxamcIHAstjLHO3Q9VzYB7dHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
علوی، سخنگوی فدراسیون فوتبال: دو هفته بعد از 10 خرداد و به طور کلی قبل از جام جهانی باید سهمیه‌ها را به AFC اعلام کنیم/ استقلال، تراکتور و سپاهان الان هستند ولی قطعی نیست؛ باید مجوز حرفه‌ای آنها صادر شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 987 · <a href="https://t.me/SorkhTimes/131871" target="_blank">📅 01:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131870">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f7d54cae7.mp4?token=S5je6TNRmR-EELH3i4owti1AC-UerdoQdLqdza4ZnmzF2VcpM9zg1FbrVDQO5WLy1PrjcVpeFbbPpihAmNaMAKlokZFsKXCJGdicmLO14qqL7RHfurQBC4-vbEO3V6yJyjFYIpUVMDsl29AVY2LeaLiuO1FPeBlMw2ZBlQcdy_Rd9zOsUf8uG8dI3e6vXi6Z5uii9YY3VIq6a5P6eeLIOmRWLB4-slYfL_Rvvrwep8whJmUuTvc5IhzgIRlPetZbuVpSu1uUgXfNaAIxwMR_5l0cpjFRGA71VfbEhoqZpzMonEgYqScc_BI0K4dPS93DfGxEgYP0HXWzBo0aDliTTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f7d54cae7.mp4?token=S5je6TNRmR-EELH3i4owti1AC-UerdoQdLqdza4ZnmzF2VcpM9zg1FbrVDQO5WLy1PrjcVpeFbbPpihAmNaMAKlokZFsKXCJGdicmLO14qqL7RHfurQBC4-vbEO3V6yJyjFYIpUVMDsl29AVY2LeaLiuO1FPeBlMw2ZBlQcdy_Rd9zOsUf8uG8dI3e6vXi6Z5uii9YY3VIq6a5P6eeLIOmRWLB4-slYfL_Rvvrwep8whJmUuTvc5IhzgIRlPetZbuVpSu1uUgXfNaAIxwMR_5l0cpjFRGA71VfbEhoqZpzMonEgYqScc_BI0K4dPS93DfGxEgYP0HXWzBo0aDliTTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤍
علوی، سخنگوی فدراسیون فوتبال: در حال پیگیری هستیم که باشگاه‌ها از تاریخ 9 اسفند به بعد درپی شرایط اضطراری به خارجی‌هایشان حقوق ندهند؛
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 971 · <a href="https://t.me/SorkhTimes/131870" target="_blank">📅 01:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131869">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔰
سرویس VIP
🔰
1 گیگ 250T
2 گیگ 500T
3 گیگ 750T
5 گیگ 1.2T
10 گیگ 2T
20 گیگ 3.5T
40 گیگ 5.6T
🛜
مناسب برای تمام سایت ها اپ ها
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 975 · <a href="https://t.me/SorkhTimes/131869" target="_blank">📅 00:48 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131868">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سه ماه تعطیلی؛
🚨
🔴
وظیفه اصلی که هیئت مدیره پرسپولیس فراموش کرده
🔺
هیئت مدیره باشگاه پرسپولیس که طبق قانون موظف است به صورت هفتهگی جلسه برگزار کند (و عادت داشت این جلسات را دوشنبه‌ها برگزار کند)، اما بعد از آتش بس چرا نزدیک به سه ماه است حتی یک جلسه رسمی نداشته؟
🔺
در این مدت، اعضای محترم هیئت مدیره همگی در تهران حضور داشته‌اند. در بازی خیرخواهانه حاضر شدند، مصاحبه کردند، واکنش نشان دادند، ابراز نگرانی و همراهی کردند؛ اما وظیفه اصلی خود را زمین گذاشته‌اند.
🔺
مدیرعامل باشگاه بدون پشت گرمی مصوبات هیئت مدیره، عملاً دست و بال بسته است. هر حرکت اجرایی نیاز به تأیید و چارچوب دارد؛ وقتی جلسه‌ای تشکیل نشود، خبری از مصوبه نیست و مدیریت قادر به گره‌گشایی از کارهای روزمره و بلندمدت نخواهد بود. نتیجه؟ باشگاه لنگ می‌زند. قراردادها روی زمین می‌ماند، برنامه‌ریزی مالی بلاتکلیف است و تیم در آستانه فصل حساس، سردرگم اداره می‌شود.
🔺
هیئت مدیره نباید تنها به حضور نمادین در رویدادهای عمومی و مصاحبه‌های احساسی اکتفا کند.
فریاد هواداران را بشنوید: «هیئت مدیره، به وظیفه قانونی‌ات عمل کن، وگرنه باشگاه را بیشتر از این به زمین نزن.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/131868" target="_blank">📅 00:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131866">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
#فوری | ترامپ:
🔴
امیر قطر، تمیم بن حمد آل ثانی، ولیعهد عربستان سعودی، محمد بن سلمان آل سعود، و رئیس‌جمهور امارات متحده عربی، محمد بن زاید آل نهیان، از من خواستند که حمله نظامی برنامه‌ریزی‌شده‌مان علیه ایران را که برای فردا تعیین شده بود، به تعویق بیندازیم
‼️
…</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/131866" target="_blank">📅 22:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131865">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
#فوری | ادعای ترامپ:
🔻
حمله به ایران را که قرار بود فردا انجام دهم به تعویق انداختم
‼️
‼️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/131865" target="_blank">📅 22:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131864">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/372dcfefd5.mp4?token=G4vBEqiR3saGYmDvsiJIzZEVqMShkl0uhbJ7qSqYdLc2xeMD9Oi08uUR5IT75spogVqKIWPx1ssb0BfyY0TstpKPrkoEzjnrtWuSlumWsqh487mMq38JOfEH8f2bbG0IAH2Rlz4Z1-46CzLg8wj0rRzjDsewnObBIU_0hnLxPx9kZC40ebt1xfjPiv8t-WKOJX7KZYejafLRG1HNJxS1V0D4l2IRsMK9ge_CsPdwOiFlVZBr4kKj426GsftsZKOrwCt3iVHDl0AowRhu-Yo7PkJT6O9mWXXy3JLhxCZpI34hKiO5PP4dsfNLsURq5syn_plULn_SVgXt04tSRH266w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/372dcfefd5.mp4?token=G4vBEqiR3saGYmDvsiJIzZEVqMShkl0uhbJ7qSqYdLc2xeMD9Oi08uUR5IT75spogVqKIWPx1ssb0BfyY0TstpKPrkoEzjnrtWuSlumWsqh487mMq38JOfEH8f2bbG0IAH2Rlz4Z1-46CzLg8wj0rRzjDsewnObBIU_0hnLxPx9kZC40ebt1xfjPiv8t-WKOJX7KZYejafLRG1HNJxS1V0D4l2IRsMK9ge_CsPdwOiFlVZBr4kKj426GsftsZKOrwCt3iVHDl0AowRhu-Yo7PkJT6O9mWXXy3JLhxCZpI34hKiO5PP4dsfNLsURq5syn_plULn_SVgXt04tSRH266w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
| ادعای ترامپ:
🔻
حمله به ایران را که قرار بود فردا انجام دهم به تعویق انداختم
‼️
‼️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/131864" target="_blank">📅 22:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131863">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
ترامپ: ایران می‌داند به زودی چه اتفاقی برایش خواهد افتاد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/SorkhTimes/131863" target="_blank">📅 22:28 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131858">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZnUmZTJXUCaUS8zGMkl1ffsn3Rnk98tTIxYiG08T-aOBVN91f7O-Ad2OGmuT61HwJCpEG0_PTaUs_VyLHRb0JIb79YrRMDMusqNFt06G2PiItzO4jb7S3OJcQx5Zw8oxUdn8CyOvMv1F3rRR3TidBrMSYRZ-dZSo_uE40PAuGF7Mc-3YrRw4Twk55_eCAb2lR20xMROywk1G2YQBwjDnY4D92N2q0j3lDgJJqgSxMtwMCKH4O4dICxORexXQMvtVQnguZjIAEwSmnAcB3UNEbZQhPpyPGX-eoTmY8XerW3oL7kxTkIyVfhUHibzfePddhlngD0aKmzTuMLrJgavCvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
یورگن لوکادیا، مهاجم هلندی سابق پرسپولیس، به اردوی تیم ملی کوراسائو برای جام جهانی ۲۰۲۶ دعوت شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/131858" target="_blank">📅 21:29 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131857">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
کاخ سفید: آخرین پیشنهاد ایران که امروز ارائه شد نیز به دلیل ناکافی‌ بودن به صورت کامل رد شد، دیگر بمب ها مذاکره خواهند کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 976 · <a href="https://t.me/SorkhTimes/131857" target="_blank">📅 21:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131856">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
🚨
ممکن است مجوز حرفه ای چند باشگاه مطرح صادر نشود و از شرکت در رقابت های آسیایی حذف شوند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SorkhTimes/131856" target="_blank">📅 21:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131855">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
باشگاه تکذیب کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 941 · <a href="https://t.me/SorkhTimes/131855" target="_blank">📅 21:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131854">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5DYJDkMPK_mcQvvVTB87o3NG7RspGvlfasVhy7HIsYpBlJdmmo-HViH9ajcd_oxnoXoTHtPS3ZEtqv6oYc-vQBhM_WzEvRfkqcOdSoaPQCxSkltY7Z3ohQjnc-1Xs4As4SvSxSmKBdZY8FNLmaZdMGb7fLV2A8WtJS-e7eJGmj3OAeI5rw0F5u4ea6-ZpOj2FlS1NM3BI8ZxYttPLHXYgHAWVMc8cQKbty8S-lnm4TnxBg7gK1rWxCm2nQXVycQ-FukyJW-L94kEtg2fppd7nCEzSZa6NSKQkMcGRFMwr0UTcwr2GXONVsG-onAKrjMN0oEoUBgvid9bIVzsPft0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
🏅
⚽️
واکنش باشگاه پرسپولیس به شایعات در مورد معرفی نمایندگان ایران به AFC
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 917 · <a href="https://t.me/SorkhTimes/131854" target="_blank">📅 21:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131853">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
🔴
اوسمار گفته اگه دوباره جنگ نشه میام و تمرینات رو اغاز میکنیم ولی اگه جنگ بشه فسخ میکنم ولی خب غرامتی نمیگیرم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/131853" target="_blank">📅 19:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131852">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
امروز جلسه ای تصویری میان اوسمار ویه را و پیمان حدادی مدیرعامل باشگاه پرسپولیس برگزار شد و اوسمار برنامه خودش برای شروع رقابت ها و همچنین نقل و انتقالات به باشگاه داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/SorkhTimes/131852" target="_blank">📅 19:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131851">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
⭕️
#شایعات
🗣
اوسمار خواهان بازگشت دانیال اسماعیلی فر و مهدی ترابی شد!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SorkhTimes/131851" target="_blank">📅 19:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131850">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
#فوری |   ادعای العربیه از پیشنهاد جدید ایران:
🔻
آتش‌بس چندمرحله‌ای و بلندمدت و بازگشایی تدریجی و ایمن تنگه هرمز
‼️
🔻
در این طرح از پذیرش توقف بلندمدت برنامه هسته‌ای به‌جای برچیدن کامل آن، انتقال مشروط اورانیوم غنی‌شده به روسیه به‌جای آمریکا، و جایگزینی…</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/SorkhTimes/131850" target="_blank">📅 19:30 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131848">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b6bdc9d91a.mp4?token=QsbNuJoY9BBG_A4pGeThBDL2dMRZTKCuIDcb0pY2qJWoaZddxyegNFQZ5uYE2HBBQXE_DAw_oeTu2VnG6ALPXH0Rz671a3QWi3nK0azVMt7osvWLHqMvJadVugO-W-i9BRWt-x31NhoZHoWJuhDDhoGwDEh5NKmHLNgbCBeFpJLoaT75TvUNhM4SzoNuarIF8Q63Bhs7YkxTHDhU62zK8sbr0bulri8pxhQr_aN9u7d2Jr2n0xCFu8OY_MxvZeBWGZSOosxryKgnhZ9knBis5cSMTDy2-7NWHBSKZmZp_7kJwWXE4yIiqwoQlD2K18gccRmBAjLQ-yTVfNZcGR1mZg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b6bdc9d91a.mp4?token=QsbNuJoY9BBG_A4pGeThBDL2dMRZTKCuIDcb0pY2qJWoaZddxyegNFQZ5uYE2HBBQXE_DAw_oeTu2VnG6ALPXH0Rz671a3QWi3nK0azVMt7osvWLHqMvJadVugO-W-i9BRWt-x31NhoZHoWJuhDDhoGwDEh5NKmHLNgbCBeFpJLoaT75TvUNhM4SzoNuarIF8Q63Bhs7YkxTHDhU62zK8sbr0bulri8pxhQr_aN9u7d2Jr2n0xCFu8OY_MxvZeBWGZSOosxryKgnhZ9knBis5cSMTDy2-7NWHBSKZmZp_7kJwWXE4yIiqwoQlD2K18gccRmBAjLQ-yTVfNZcGR1mZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
|   ادعای العربیه از پیشنهاد جدید ایران:
🔻
آتش‌بس چندمرحله‌ای و بلندمدت و بازگشایی تدریجی و ایمن تنگه هرمز
‼️
🔻
در این طرح از پذیرش توقف بلندمدت برنامه هسته‌ای به‌جای برچیدن کامل آن، انتقال مشروط اورانیوم غنی‌شده به روسیه به‌جای آمریکا، و جایگزینی غرامت با تسهیلات اقتصادی بحث شده است.
🔻
این پیشنهاد بر ضرورت تضمین‌های بین‌المللی، تفکیک مسیر دریایی از پرونده هسته‌ای و نقش‌آفرینی پاکستان و عمان در مدیریت تنش‌های تنگه هرمز نیز تأکید دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/131848" target="_blank">📅 18:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131847">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
🚨
اسامی ٣٠ بازیکن دعوت‌شده به اردوی نهایی تیم ملی در ترکیه  علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد خلیفه  احسان حاج صفی، میلاد محمدی، امید نورافکن، شجاع خلیل زاده، علی نعمتی، حسین کنعانی، دانیال ایری، رامین رضاییان، صالح حردانی  سامان قدوس، روزبه…</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/131847" target="_blank">📅 18:40 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131845">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6FK5VHfImLhJR6_EZIqamwdQOwf_zDvzf6Vh3CS4Lwwee1QOxFdXh3jHEtmVMKW0QtUF5LYyVd5ApZMY087QUGdab9VXAbhHJhc8Bgtae-Qr18gxPsgXpa9oysVbhmokQx7ISbjn9nPwViwCDIiGZedgwwN5QU7ENrro6AnCylZe5CbzgWtOXii_gKnJs01y_AqhptfrwviGpojdL_hVQmBZu5UEBLC_UU0_lDUx7dBpnQBLMVNOAlzW85Z0xIwE4GuDiuOHQVCqXuS8k5VGxV2CjSc8gBQn1gwAwV-S99ds9rG3gao3VKPxOs7lF483yikv3fOUwT557eTpP--uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مدیرعامل پرسپولیس عضو هیات رئیسه فدراسیون هاکی شد
🔺
پیمان حدادی مدیرعامل پرسپولیس با بهرام قدیمی رئیس فدراسیون دیدار و گفت‌وگو کرد. بعد از این دیدار قدیمی با اهداء حکمی، حدادی را به عنوان عضو هیئت رئیسه فدراسیون هاکی منصوب کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/131845" target="_blank">📅 17:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131843">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89becc508b.mp4?token=tLG60c5BqS7GZD-sNEwoJOCcbrXrfLaZjtK5Wywvw9filbWDGJTQ-M5zr0kAxZfKmeG8yDQfkwfXmUutVRfEhgsNxQou-KVtSTipcf6_vF-ADT_sMqdqUpqt25tUfZ6md-h79B1K5p82W2g8XwyIbTUtqeB-6EcvaxsZTGbC8QUv3SIKCYDg-z1xe79CeaLZIbGERNtipsOwjH-LXNQxFm5xX6EtdsgCY7hmePFlpx30WYbX7gpvVWM68MyHJ1JbK_bTvEa5oHbzw--SawP_NCRLR1WtluFifxY_NMx_iLuZWanwuxjb03_L3gQ3hHtyJgI3laUXfhqzcNe10VWoaoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89becc508b.mp4?token=tLG60c5BqS7GZD-sNEwoJOCcbrXrfLaZjtK5Wywvw9filbWDGJTQ-M5zr0kAxZfKmeG8yDQfkwfXmUutVRfEhgsNxQou-KVtSTipcf6_vF-ADT_sMqdqUpqt25tUfZ6md-h79B1K5p82W2g8XwyIbTUtqeB-6EcvaxsZTGbC8QUv3SIKCYDg-z1xe79CeaLZIbGERNtipsOwjH-LXNQxFm5xX6EtdsgCY7hmePFlpx30WYbX7gpvVWM68MyHJ1JbK_bTvEa5oHbzw--SawP_NCRLR1WtluFifxY_NMx_iLuZWanwuxjb03_L3gQ3hHtyJgI3laUXfhqzcNe10VWoaoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
قلعه‌نویی: امیدواریم ویزای ۲۸ بازیکن را بدهند/ ۴۰ درصد عقب‌ماندگی بدنی و فنی داشتیم که ۲۵ درصد آن را جبران کردیم/ شرایط سخت است ولی نباید بهانه بیاوریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/131843" target="_blank">📅 17:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131842">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bfd63331d.mp4?token=XkEEnk_8rn9wonikdpWJG4JxjuujPWvqVYYdxPX3CIB7EU8ed10El0JaH1wwk5_j0tyN4zg24uAyRa1lZTzKWUE08Jnfv8H5COxEBOUFFTKTUIxYtBUxWnMRlON33TQkzj67QKpMZfVoP32o0tHbe2JUwoqyeHIk8MbWF-8BSaoG0VuKXMEwJ8hdm3NymjK0jiOiS5b8SOPPrLLVa3LwU_GbVuubscI8pV-eZlss1dlny8zsdG4n4hvy4VmyvEItfruhmZc2zRmno45CJzaXkpsQUhDpp0rDZrRtgkivT3FtztZgrn55NXAelDJ8F8vrwvvuJWMSV9KZR69BSUZR9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bfd63331d.mp4?token=XkEEnk_8rn9wonikdpWJG4JxjuujPWvqVYYdxPX3CIB7EU8ed10El0JaH1wwk5_j0tyN4zg24uAyRa1lZTzKWUE08Jnfv8H5COxEBOUFFTKTUIxYtBUxWnMRlON33TQkzj67QKpMZfVoP32o0tHbe2JUwoqyeHIk8MbWF-8BSaoG0VuKXMEwJ8hdm3NymjK0jiOiS5b8SOPPrLLVa3LwU_GbVuubscI8pV-eZlss1dlny8zsdG4n4hvy4VmyvEItfruhmZc2zRmno45CJzaXkpsQUhDpp0rDZrRtgkivT3FtztZgrn55NXAelDJ8F8vrwvvuJWMSV9KZR69BSUZR9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ورود کاروان تیم ملی به آنتالیا برای برگزاری اردوی آماده‌سازی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SorkhTimes/131842" target="_blank">📅 17:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131841">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">#
منهای‌پرسپولیس
🚨
یاسر آسانی وینگر آلبانیایی استقلال در آستانه انتقال به ختافه اسپانیا قرار دارد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/131841" target="_blank">📅 16:08 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131840">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🏅
بازیکنان پرسپولیس چقدر پول گرفتند؟
⏺
پیگیری‌ها از باشگاه پرسپولیس حاکی از آن است که بازیکنان این تیم مبالغی بین ۶۵ الی ۷۵ درصد از قراردادهای خود را دریافت کرده‌اند و پرداخت صددرصد قرارداد چند بازیکن صحت ندارد.
⏺
فقط یکی از بازیکنان خارجی پرسپولیس مبلغ بیشتر…</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SorkhTimes/131840" target="_blank">📅 16:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131839">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b213799d6a.mp4?token=plBv5UV0zilgfzsSElwaUC9AfZYY_UcC4r9w6IyVuJblU7oQtUHR2z1SCe_du_XDQjt1sDL1DMkr7fPHeH0KBE_TMuB8LlMXNCPMaaycRILeB4HUcej6ClplgNrpyMeDiqMClDode3lF7P2Ubf3v9CuKS-PqiAwmzds8mVfrXyPjsGjYlpZAaVKQ41GnVyh-X1ujcRUIauk0vhwSaVP0uuW3nO07qldlhEfNcfO0z1szbalmqEvAVkWFmhJVAc_w2zUjhUj9PYMTKiETVR3-Kr_issDmkzgXN46fccXuhxod4WdPuytRh7Ql7ye3WbcgjyQB4WsxrHE95wJIHjgOOA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b213799d6a.mp4?token=plBv5UV0zilgfzsSElwaUC9AfZYY_UcC4r9w6IyVuJblU7oQtUHR2z1SCe_du_XDQjt1sDL1DMkr7fPHeH0KBE_TMuB8LlMXNCPMaaycRILeB4HUcej6ClplgNrpyMeDiqMClDode3lF7P2Ubf3v9CuKS-PqiAwmzds8mVfrXyPjsGjYlpZAaVKQ41GnVyh-X1ujcRUIauk0vhwSaVP0uuW3nO07qldlhEfNcfO0z1szbalmqEvAVkWFmhJVAc_w2zUjhUj9PYMTKiETVR3-Kr_issDmkzgXN46fccXuhxod4WdPuytRh7Ql7ye3WbcgjyQB4WsxrHE95wJIHjgOOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
#فوری
| نیویورک تایمز مدعی شد:
🔻
آمریکا و اسرائیل در حال آماده‌سازی گسترده برای احتمال ازسرگیری جنگ با ایران در همین هفته هستند و این گسترده‌ترین سطح آمادگی از زمان آتش‌بس است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/SorkhTimes/131839" target="_blank">📅 16:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131838">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
لاوروف:پروژه نیروگاه هسته‌ای بوشهر به هیچ‌کس جز روسیه و ایران تعلق ندارد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/131838" target="_blank">📅 15:30 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131835">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">محمد پروین، فرزند علی پروین:
پدرم به دلیل زخم پا (به علت دیابت) در بیمارستان بستری شده است، اما مشکل خاصی ندارد و به زودی مرخص می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/131835" target="_blank">📅 14:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131834">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
#فوری | پست جدید ترامپ درباره ایران  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/131834" target="_blank">📅 13:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131833">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
۷۹ روز از قطعی اینترنتی ایران گذشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/131833" target="_blank">📅 13:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131831">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkSipONf8shuJrXhQ5153YVp6btdsxPmePe1X6h3vC2RKh-8cs0wsF4BOVuTzd3d5Bj1cLyq9b6kzeJsx19sWMrFp1urQJDAmNrqA_J6PaRBsR39bGUJb2_8qpJ3Aar_yYrZMbYp5gcfGugf9zblF_VrjIv0pJC8qTzR-sTULLZtL2BE9ohcwx1eQQ9eM-nZ8dJ-fk9ucyXa4YyvquQRF7OpsocfsUKc7DZzBvvHv8-Jrb99bNwmN9kqqvThzocnao4pxUOfi9Wi0lSA4SIL_11p_dRvPH6JaKKhdfTCSTFaNNur0V8tQwQDW7CBl210GItF9VuAtqQmaChaX-faug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سردار آزمون پس از خط خوردن از لیست نهایی تیم ملی برای جام جهانی ۲۰۲۶، تصویر پروفایل خود را از لباس تیم ملی به پیراهن باشگاهی شباب الاهلی تغییر داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/131831" target="_blank">📅 11:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131830">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇷
بازیکنان تیم ملی و امضای پیراهن های جام جهانی برای تقدیم به مردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/SorkhTimes/131830" target="_blank">📅 11:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131829">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87ff620cb1.mp4?token=OfjaKjlR4keHcXdsGI0t-0Po8OEIfZh5wENRBXfeP3wnvVjaYvOairALSjKnZonIsCKCCRp9lQgpHfC7aqvkNHuGGVHNX0M6QHA9aRN6bfFcvzSjp6SS3eXS584EiSV_90M2k3SGc9h9ORpf-8BoAupiujJAcHutDNUR0l4btCEzio95rPEnsfF5TNnHy2nNfoFxPWfV9mOBBi3rq7Fz7vhBXPRK1LH1OvWVag7mGF9S1wDhqaU4pgnu6QOmkR48GZ6cwmMpUKgNbaDcKHwDjifapaTOcRKkrXXvgSiFPmk_qt8kRF4Pe5EuNa8EApjZqhiPShXErRltwMP6wqfoxjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87ff620cb1.mp4?token=OfjaKjlR4keHcXdsGI0t-0Po8OEIfZh5wENRBXfeP3wnvVjaYvOairALSjKnZonIsCKCCRp9lQgpHfC7aqvkNHuGGVHNX0M6QHA9aRN6bfFcvzSjp6SS3eXS584EiSV_90M2k3SGc9h9ORpf-8BoAupiujJAcHutDNUR0l4btCEzio95rPEnsfF5TNnHy2nNfoFxPWfV9mOBBi3rq7Fz7vhBXPRK1LH1OvWVag7mGF9S1wDhqaU4pgnu6QOmkR48GZ6cwmMpUKgNbaDcKHwDjifapaTOcRKkrXXvgSiFPmk_qt8kRF4Pe5EuNa8EApjZqhiPShXErRltwMP6wqfoxjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بازیکنان تیم ملی و امضای پیراهن های جام جهانی برای تقدیم به مردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 995 · <a href="https://t.me/SorkhTimes/131829" target="_blank">📅 11:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131828">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc0f3d0278.mp4?token=dcf1UG8Yz71i1AlcBqgGuAZJHdVOzUkiTzqqhrJAEBf979GPJh6srYSqUjYFrIQDjDyfdYkvDlJav1kL1CN9Ysj8vQoeE__ny24zT4jeV80O1Ry-EY0O_ETvpz1Kc715VMoHzt8cfgIKABkJv1a0dge4aDIcoZs7n7Y4lbY2nGroPmWG-5jr37h1hX5cUrqFlQYE_90mL__Is1UQCu6WgchKww3qaoru6GYhNZatAlObd961nnRdZhEuQZiwHnZAvQdZyJpcF-OQ9vMEJgTZY_yYNLZgwnlYcS6yxwg6dCy7nbmLfU__Hjx_6qTv1FoK86DXaCKUosB64Vlnsjqigw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc0f3d0278.mp4?token=dcf1UG8Yz71i1AlcBqgGuAZJHdVOzUkiTzqqhrJAEBf979GPJh6srYSqUjYFrIQDjDyfdYkvDlJav1kL1CN9Ysj8vQoeE__ny24zT4jeV80O1Ry-EY0O_ETvpz1Kc715VMoHzt8cfgIKABkJv1a0dge4aDIcoZs7n7Y4lbY2nGroPmWG-5jr37h1hX5cUrqFlQYE_90mL__Is1UQCu6WgchKww3qaoru6GYhNZatAlObd961nnRdZhEuQZiwHnZAvQdZyJpcF-OQ9vMEJgTZY_yYNLZgwnlYcS6yxwg6dCy7nbmLfU__Hjx_6qTv1FoK86DXaCKUosB64Vlnsjqigw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
امیر قلعه نویی و امضای پیراهن تیم ملی با جمله تقدیم به ابر ملت جهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SorkhTimes/131828" target="_blank">📅 11:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131826">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXrwQTysqcPxE7KUA_7Gu_1oXg0Q5K6A1QzPZmeToFIYLEqmtQFL8fL6TSiInu1qF55_PSzi7w9VNwCDOv8hLTbEK9Hs3MT2sH4PxZYuE2KaW54qEVRuOgp92WuVPnGatroGxzBisvqK2iuiuVL5dgUf8YjpohrzeOcrVwMXg2XSAqLGDdI90MzI4B7gFYmFeaJr4u6CLgPdk_kmzDoLqR3Ptnzidvq7yi0rR3Os_FfPWlnMIAZ1LYUajU-HGOGhe_5bcdiZN1K7jLu9bdyv6GOkJq72crZY8awnHelbVik56nqdwE6o7MPcm2YrfjQo17yHyAtJwBBNDXwKYCQIug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ لحظه شلیک مجری شبکه افق به پرچم امارات را منتشر کرد و گفت: خواهیم دید چه خواهد شد
!!!!
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/131826" target="_blank">📅 10:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131825">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2qgVcSp4NQyjDvAaM1jNZLKT1Cn0kPahNhGWmoxR0Lxh2k7u0hyhfHvxWn16mgme8Gkxc6ap-bD99VrL7bqLn6Sox70jfbIp1bcqQHb3s_NmfmNrZEdhTX53YQk9QsgDyZTXARoMVUUroKXVGDSoDZp-oO2qmiOPj7gfCLHg7DIQy1K28dPzpL9Yp1ejEnXhUREoHlKhF-gAoGOmefiisP2g9AkNibDXJXpk4YE3aXHq7kc2XOC30vqUlNnRj4lUZBtlA2RZbUlhPCvYgCIDjxVT8tK_3pFYiTeeR8OoiucN3Opvcp7ZXiaf4EJSRObFMTMoarer8nubhWsyEbPIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پیمان حدادی مدیرعامل پرسپولیس قول داده که درصورت ماندگار شدن وی در نقل و انتقالات تابستانی یک تیم مدعی و جوان را تحویل دهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SorkhTimes/131825" target="_blank">📅 10:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131824">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
امروز جلسه ای تصویری میان اوسمار ویه را و پیمان حدادی مدیرعامل باشگاه پرسپولیس برگزار شد و اوسمار برنامه خودش برای شروع رقابت ها و همچنین نقل و انتقالات به باشگاه داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SorkhTimes/131824" target="_blank">📅 10:00 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131822">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">⚪️
امیر قلعه‌نویی: ما بازیکنایی داریم که همین الان میتونن تو رئال و بارسا بازی کنن. حسین کنعانی چیزی از سالبیا کم نداره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/131822" target="_blank">📅 08:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131821">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/McZRFQVLx943vwQLZAoQzPPewP3-5K32webgHm8iu2I9WR0TT_KuYsRqI_KonY9tmvpYvBh_6hOuV21ml1mvoj_HF6wY8NuXq9RVqFsykMhsQ7_fQxs6vfRmvvgEKjVhQMAc3TfLKryIMR9blgHtrZAMQwD1YF8Dh6e_GXr-UVY8SdocWduub6zcvQybFl3aK3lB0OhFfq9iF53WeNvZ2QsoXxFOuG2SeHZSGwNyge4nxACxikf3pUF3kjQk-BHHvAs8Qt5Ks3lXqIUTL6IaGTwwkHcWfDHQyMJfgWEqFjb08X67nvGwBp93_rdw2zsZGp7MatfF4Z--RTAojF3ycA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
۹۰٪ کاربرا هنوز اشتباه وارد سایت میشن!
تو جزو اونایی یا میخوای حرفه‌ای عمل کنی؟
✅
ورود سریع به وینکوبت فقط با یک کلیک ساده:
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
نه لینک اضافی
📌
نه سردرگمی
📌
نه اتلاف وقت
📌
مستقیم، سریع، بدون دردسر وارد شو!
⏳
دیر بجنبی، از بقیه عقب می‌مونی.
🔗
الان وقتشه مسیر درستو انتخاب کنی:
🤖
@Wincobet_bot
📌
برای تحلیل بازی‌ها و آخرین اخبار سایت جوین بدید:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/131821" target="_blank">📅 01:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131820">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
#فوری | پست جدید ترامپ درباره ایران  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/131820" target="_blank">📅 01:19 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131819">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U9_DdQy1htUzV3bOu5RHb3qBnOh2I2mY3b-cK1rQ5q8HCRguRd8jZR6ux78_jsQ5rGF1nMHzA1HJFUISVBjJjBLOkgf5tbOCB65oyU7550ZlCEKb8cgxgWOyuw-7ZX6st8MfhMkc9v4Po-lJlM5wg4sRQXrR72T6WanKEA1DINBLOZ9Sc-3Nm-ghaOrfcFqycc_3tw23QL4raQH_T-7oHEDJbjmJNlj5gfhxLu3KHeQP76W8lLiW5A559nBcl5ohIVjTkwLMKk33cO4V-oSDqxMkGm8dpi4tM7pNOlxM_yWV95tsXUFyqKG8_Vmi3CnSEiYFNMLa2CGOzbqRac4Ktw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#فوری
| پست جدید ترامپ درباره ایران
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/131819" target="_blank">📅 01:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131818">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
علیرضا بیرانوند: سرود جمهوری اسلامی رو با صدای بلند میخونم و مخالفا هم هیچ کاری نمیتونن بکنن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/131818" target="_blank">📅 01:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131813">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
یکی از گزینه‌های اصلی باشگاه ، برای گلر ذخیره جایگزین امیررضا رفیعی آرمین عباسی گلر جوان پیکان تهران است   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/131813" target="_blank">📅 23:51 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131812">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gb9cDZ4wxlFnex5Wskdvl8RkN8KyNQweFEP-X2N-dK9fa4PAqQ9oN_QTL_L81De2xc0yniGTxGh-YxedgbrY-5KdhfWmBoPmBj_iHeAEjhuNsZMuK7Zm9sSUwjFFmGFajtU_ulEJFoqAFV7pbw3bJn8pzPegdCb1Ye_j1ARSdwhM0jEQNXMEWqY1L80o3g8YmW9l6Kc5sxHMNS2eRVPCY4BSkQttlxCuGGEYUufxRdNhg_hJOuj01PMniPtEJXJcqoIDliYpnK7NZvOJCGml1UjO68BnIk4NSbYkkZMCf10vwAYVlmNpe0nACVnsPvl1B53hjHxlMCLZd3ppUoGfvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
#شایعات
🗣
اوسمار خواهان بازگشت دانیال اسماعیلی فر و مهدی ترابی شد!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/131812" target="_blank">📅 23:49 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131811">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✅
امیررضا رفیعی گلر دوم سرخپوشان پایتخت پس از چهار سال حضور در پرسپولیس از جمع این تیم جدا خواهد شد/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/131811" target="_blank">📅 23:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131810">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K16X-YhDm62YHQbu4bFGOS3NNBPoUTAXXubcju6SWq8kJWhIFzLLfoFi4ZcY3eiK58838Rdax__4IxNPR8v4qvSZ7OA7GdaCygNDMzoq8l6Pwilk27kdboQNrzW8X0khSh_JpSb93r2JdDY7nnzJSGxeZMHFkw0bdSf29zZwOhioE0rjJaWviZnQn3mxVjlsir1tzWMpDy-2q4z5V-Ox-Wu3kmPHnJA8w2NaFNRCq_wrL0pLWsk5lSoeifayhDwE3LdQrIjRWEGzcO681b7UPDL64aSRo63cvYLEK4qDFa0OGjV6WXl9HYoiRuGCYfDYsrMVV_dqJXyL7j5fyzAsdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
مدیران باشگاه کیسه اول فصل رفتن دنبال جذب این بازیکن و براشم پیش قرارداد فرستادن با مهر و امضا رسمی ولی لحظه آخری از جذبش پشیمون شدن حالا طرف رفته از کیسه شکایت کرده و گفته غرامت 800 هزار دلاری میخوام :)
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/131810" target="_blank">📅 23:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131808">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚩
🚩
🚩
🚩
#فووووری
✅
فرهیختگان خبرداد؛واسطه پیمان حدادی مدیرعامل باشگاه پرسپولیس در روز های گذشته جلساتی فشرده با مهدی تارتار سرمربی گل گهر داشته تا این مربی را جایگزین اوسمار ویه را در پرسپولیس کند!!!!   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/131808" target="_blank">📅 22:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131807">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✅
رضا غندی پور پس از استوری علیه قلعه نویی از اردوی تیم ملی امید هم خط خورد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/131807" target="_blank">📅 22:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131806">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
مدیران باشگاه پرسپولیس روند تمدید قرارداد علی علیپور را به اوسمار ویه را واگذار کردند و در صورت رضایت این مربی قرارداد او را تمدید خواهند کرد/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/131806" target="_blank">📅 22:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131805">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
فرهیختگان: یه واسطه تارتار رو پیشنهاد کرده که اگه اوسمار رفت بشه سرمربی پرسپولیس   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SorkhTimes/131805" target="_blank">📅 22:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131804">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووری
🚨
دونالد ترامپ: ساعت برای رژیم ایران در حال تیک‌ تاک میباشد و بهتره است خیلی سریع شروع به حرکت کنند وگرنه هیچ چیزی از آنها باقی نخواهد ماند ، زمان یک عامل بسیار حیاتی و مهم است   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس …</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/SorkhTimes/131804" target="_blank">📅 22:21 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131803">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dpdt_AgGvpdMT4toYucK0_UhQaOfmjFYGF-ZNkfBIaKt60BUy3bXeFu7EPuXODGe_IBGZxooD4-Zo2DAp3Pl0wGxGU5_55FAgk5NVMnzuPPvY6mhcG2Bt7tMx3SIVD35Hl71U48JuPvJ9ImuLYtVMpD4JbShNPGCIKlzl9A-UALFy0n7pWHTtnpmZN53jxUjx2eYlfRxaHwp9cfoxvKg11VFHkjrCNBGEGmoKWN4yPSiuNqwco5Z6eFnt7mTOJyyF6jfk7NMMKm0Mlvo23lRAAGzTKzypevYZJ_6IZ_xORlOOKYYYI72bc9flg9QZs0R6CuYWdlUTmTugKEGM0rilg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فووووووووری
🚨
دونالد ترامپ: ساعت برای رژیم ایران در حال تیک‌ تاک میباشد و بهتره است خیلی سریع شروع به حرکت کنند وگرنه هیچ چیزی از آنها باقی نخواهد ماند ، زمان یک عامل بسیار حیاتی و مهم است
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/SorkhTimes/131803" target="_blank">📅 22:09 · 27 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
