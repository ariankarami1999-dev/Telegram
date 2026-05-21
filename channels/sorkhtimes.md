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
<img src="https://cdn4.telesco.pe/file/NuwE9sj1A53kCkWfzKFiGwMbL4MRsy8YyjnomyDHjsRNGQZ7fDbC6vq03fbkOJFA3sywNiDF7QBjUgcRZbxR6iV0w3lAG1AFxiqJQilj9IzRzBMAfFgGQfhF6gEo3o0_-CAYB6ijSJCWcT76v04KnJFTR1YNKq3-QMBXughHQ5sEaPI5pbkl90GaDzAPjH-iMZ11GGoymrxGn3mNwWEV0uRF1UtPNHGDSLkoyfQWd31FFAbmeO8hFdCikyCMit4nBKg52AReb_6OZHSoZkh_Z8_RrWWwzBIdIrnowuhmNUUthkWxiF6C4Hsz-IkIYH3Rx2dn61I2qnThvZK_MBlWCw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.8K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-01 03:03:07</div>
<hr>

<div class="tg-post" id="msg-132002">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">- همه اون لحظه‌ای که سایت نصفه لود میشه و VPN قاطی میکنه رو تجربه کردیم، مخصوصاً وقتی وسط بازی یا ثبت پیش‌بینی باشی.
😑
- ربات رسمی تلگرام وینکوبت کارو راحت و ورود به سایت رو آسون کرده:
👇
-
🤖
@Wincobet_bot
-
🤖
@Wincobet_bot
- برای کسایی که بیشتر وقتشون توی تلگرامه، خیلی کاربردیه.</div>
<div class="tg-footer">👁️ 307 · <a href="https://t.me/SorkhTimes/132002" target="_blank">📅 01:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132001">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
ورزش سه: روزبه چشمی از ناحیه رباط صلیبی مصدوم شد و جام جهانی رو از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 600 · <a href="https://t.me/SorkhTimes/132001" target="_blank">📅 00:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132000">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcesT2dDKjNVeH2C_h9S9we5JGqLCqKZDFNMIFcu_rtVIFPbT_We36P2SAlI3oH1GDAkNneVJxSI7MLKlg2_GDsVGFHULriFMp9_UxeDOYXBwmsryTIXAos_f-jouzf1UMEgEzMXtNzqcFWsWhhA2rvMDcj0sl_zxFHfJjQp4gxbLZWaCl01AZvEZUdChQFSA_3p0nbgb9gXZwAMOQAQuR182nanBVu1Soe6Mgss6m1MVDUxvQKRo5rKy_Ne2muxK8HlUdAP8WczR8ZAvBGTta0ROYRoAqumHIjK-y-PQEw-be8XWpJL0h4dX3LqWLNLJuLs9dR0lMFLQkTBvSN0jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
🇵🇹
رونالدو به اولین بازیکن تاریخ فوتبال تبدیل شد که در 4 لیگ مختلف قهرمان شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 607 · <a href="https://t.me/SorkhTimes/132000" target="_blank">📅 00:12 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-131999">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمحمدرضا شوکتی</strong></div>
<div class="tg-text">درست میگه دیگه
زمانیکه یه عده داشتن از امثال سروش رفیعی حمایت میکردن و داشت پدر امتیازات تیمو در می‌آورد، بایستی فکر همچین روزی رو میکردیم</div>
<div class="tg-footer">👁️ 709 · <a href="https://t.me/SorkhTimes/131999" target="_blank">📅 23:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131998">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
‼️
مجوز حرفه ای باشگاه صادر شده ولی خبری از شرکت تو مسابقات آسیایی نیست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 788 · <a href="https://t.me/SorkhTimes/131998" target="_blank">📅 22:55 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131997">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 776 · <a href="https://t.me/SorkhTimes/131997" target="_blank">📅 22:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131996">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g_zLCJF4TBq1pwQjcU5J7zWKeEk74LqJEgPdYwflrZJ-lWd7GeMk72t5RUWhn69YlR65yoIgkgtmCg5UH08WrDOPTszHyfaX1c0sNxB0vH6UGquxgGb_eUvNj1iTb8QRPdvOgI4d-zN6LZt6rwMO9nQXG1B4XCyXQxo570hOJT_GmW-xs3PMb-osnErJsX8nYDnhtTik08PfVbx8hHWYY1Buw98UF02UL5DMG__rwLrA9NKyFm7eyQ-Pvv26cOqmz_AIZkPOCbFUCnuIvRoF8U8_PBa_8hdkCYm2xFYsz71tcqhYUea89OFzbzAiWgMbI-JbCv2Dfvm-z4pgQBF1cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی
| العربیه : پیش‌نویس نهایی توافق مورد انتظار بین آمریکا و ایران که طی ساعات آینده برای توقف جنگ در همه جبهه‌ها تنظیم می‌شود:
🔴
۱. توقف کامل، فوری و بی‌قیدوشرط آتش‌بس در همه جبهه‌ها (زمینی، دریایی و هوایی).
🔴
۲. تعهد دو طرف به عدم هدف‌گیری هرگونه تأسیسات نظامی، غیرنظامی یا اقتصادی طرف دیگر.
🔴
۳. توقف کلیه عملیات نظامی، فعالیت‌ها و جنگ تحریک‌آمیز رسانه‌ای.
🔴
۴. احترام به حاکمیت کشورها، تمامیت ارضی آنها و عدم دخالت در امور داخلی.
🔴
۵. تضمین آزادی دریانوردی در خلیج فارس، تنگه هرمز و دریای عمان.
🔴
۶. تشکیل کمیته مشترک برای نظارت بر اجرای توافق و حل و فصل اختلافات.
🔴
۷. آغاز مذاکرات درباره موضوعات حل‌نشده حداکثر ظرف مدت ۷ روز.
🔴
۸. لغو تدریجی تحریم‌های آمریکا علیه ایران در مقابل پایبندی ایران به مفاد توافق.
🔴
۹. دو طرف تأکید می‌کنند که این توافق در چارچوب احترام به حقوق بین‌الملل و منشور ملل متحد است.
🔴
این توافق از لحظه اعلام رسمی آن توسط دو طرف، لازم‌الاجرا خواهد بود
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 802 · <a href="https://t.me/SorkhTimes/131996" target="_blank">📅 22:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131995">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
ورزش سه: روزبه چشمی از ناحیه رباط صلیبی مصدوم شد و جام جهانی رو از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 764 · <a href="https://t.me/SorkhTimes/131995" target="_blank">📅 22:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131994">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
فوتبالی: علیپور مذاکرات مثبتی با حدادی داشته و از لحاظ مالی توافق کرده و اگه اتفاق خاصی نیوفته بعد جام جهانی تمدید میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 760 · <a href="https://t.me/SorkhTimes/131994" target="_blank">📅 22:36 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131992">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✅
وکیل بیرانوند میگه پرسپولیس پولی برای رسیدگی به پرونده(هزینه‌ی دادرسی)پرداخت نکرده و ادعای باشگاه کذبه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 979 · <a href="https://t.me/SorkhTimes/131992" target="_blank">📅 19:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131990">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔽
صدور مجوز حرفه‌ای باشگاه  پرسپولیس با ابلاغ رسمی دبیرکل فدراسیون فوتبال
🔴
رسانه رسمی پرسپولیس:
❤️
با دریافت نامه‌ای از سوی دبیرکل فدراسیون فوتبال، مجوز حرفه‌ای باشگاه پرسپولیس برای فصل پیش رو صادر و به طور رسمی ابلاغ شد.
🔽
این مجوز که بر اساس مدارک ارائه…</div>
<div class="tg-footer">👁️ 961 · <a href="https://t.me/SorkhTimes/131990" target="_blank">📅 19:09 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131989">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❗️
آسوشیتدپرس: عراقچی، وزیر خارجه ایران و قالیباف دیگه به هیچ عنوان مذاکرات رو در داخل ایران پیش نمی‌برن و کنترل کل ماجرا دست سپاه پاسدارانه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 919 · <a href="https://t.me/SorkhTimes/131989" target="_blank">📅 19:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131987">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
رد درخواست خروج اورانیوم غنی‌شده از ایران
🖍
طبق گزارش دو مقام ارشد ایرانی به رویترز: ایران اصلی ترین خواسته آمریکا برای توافق که انتقال اورانیوم ۶۰ درصد است را به صورت کامل رد کرده است.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 957 · <a href="https://t.me/SorkhTimes/131987" target="_blank">📅 18:36 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131986">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔽
صدور مجوز حرفه‌ای باشگاه  پرسپولیس با ابلاغ رسمی دبیرکل فدراسیون فوتبال
🔴
رسانه رسمی پرسپولیس:
❤️
با دریافت نامه‌ای از سوی دبیرکل فدراسیون فوتبال، مجوز حرفه‌ای باشگاه پرسپولیس برای فصل پیش رو صادر و به طور رسمی ابلاغ شد.
🔽
این مجوز که بر اساس مدارک ارائه…</div>
<div class="tg-footer">👁️ 940 · <a href="https://t.me/SorkhTimes/131986" target="_blank">📅 18:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131984">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTI9y2e69vrGHzY-bf7hrSjb0UDLKYp8bdWyQmCkUME0_wEEMq7iatw6NdxQ53UFPaRK0aWHu_5Py4DvvUJNylETofzF-CoZPYrRltDB2G0Ve4Gj_OhXhnXhxYIEs1_daJL-yMrQv5ikupG8y3Zop6WExNBmtaxEcFlcgsVUgAtthmebyyf5lpVtKFybrbheFFyzbMNW8lE0XEPpI9UhZMZcsbJralHyEKZpN64nC1OlNGlFKCuL_IGjDkmQqIQbiagY9AVUm9U979pBoaNjAID28NlbSoSNLfq3mWecoiR0jJnqhweJuWWfrjSzuwLAI3u9O8eqY-x2JV3jS-tksg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔽
صدور مجوز حرفه‌ای باشگاه  پرسپولیس با ابلاغ رسمی دبیرکل فدراسیون فوتبال
🔴
رسانه رسمی پرسپولیس:
❤️
با دریافت نامه‌ای از سوی دبیرکل فدراسیون فوتبال، مجوز حرفه‌ای باشگاه پرسپولیس برای فصل پیش رو صادر و به طور رسمی ابلاغ شد.
🔽
این مجوز که بر اساس مدارک ارائه…</div>
<div class="tg-footer">👁️ 902 · <a href="https://t.me/SorkhTimes/131984" target="_blank">📅 18:08 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131983">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✅
فدراسیون فوتبال به طور رسمی با ارسال نامه‌ای صدور مجوز حرفه‌ای برای حضور در رقابت‌های لیگ نخبگان آسیا را به باشگاه استقلال اعلام کرد...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 858 · <a href="https://t.me/SorkhTimes/131983" target="_blank">📅 18:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131982">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
‼️
باشگاه استقلال صورت مالی شش ماهه (۳۰ دی ۱۴۰۴) رو روی سایت کدال آپلود نکرده است. به این دلیل که مدارک مالی و شفافیت در بخش‌های مختلف باشگاه در راستای حرفه‌ای‌سازی از سال گذشته آماده نیست.
🚫
یکی از الزامات اصلی مجوز حرفه‌ای‌سازی است که حالا استقلال فاقد این…</div>
<div class="tg-footer">👁️ 871 · <a href="https://t.me/SorkhTimes/131982" target="_blank">📅 17:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131981">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
۶ باشگاه ایران در آستانه کسب مجوز آسیایی
⚪️
برای فصل آینده ۶ باشگاه لیگ برتری مجوز حرفه‌ای از کنفدراسیون فوتبال آسیا دریافت خواهند کرد.
🔴
به نظر می‌رسد استقلال، تراکتور، گل‌گهر سیرجان، چادرملوی اردکان و پرسپولیس از جمله باشگاه‌هایی هستند که مجوز حرفه‌ای دریافت…</div>
<div class="tg-footer">👁️ 898 · <a href="https://t.me/SorkhTimes/131981" target="_blank">📅 17:18 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131980">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
👈
ادعای «میدل ایست آی»: به ترامپ هشدار داده شده آغاز جنگ در ایام حج، آمریکا را در جهان اسلام منفورتر می‌کند و به همین دلیل حمله به ایران به تعویق افتاده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 903 · <a href="https://t.me/SorkhTimes/131980" target="_blank">📅 17:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131979">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
⭕️
#شایعات
🗣
اوسمار خواهان بازگشت دانیال اسماعیلی فر و مهدی ترابی شد!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 905 · <a href="https://t.me/SorkhTimes/131979" target="_blank">📅 17:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131978">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RcYtpprGjmC7ikYIPYkjos4uIDP5Wr8cEEQpTQlZOom-dPuKIvNvrynMKjIAxaLA0NPoktqekgTZHEFfyVK7XgblwQGWg8p1S_w68sPL_VBIOMltL6R32RoQAzt7yI-mMe48-3DokOaq8eJMSXXCOHNq3wxlYAecvIgijfobljAjZsEv4npxy65qwRZybuhceupNE46NryVZrUnCn0QApVbSGdsNx06m0mJoVbWshvJXbOVF21VyDPi_d27dxo5UOqPDY2DtHjBeovWYHaSmiR7dV9kT5wy245EmSJ0jNUhv9CEkGdXx3YOOt2sOG8elgURnTbo1LswUJ_Asm7pwGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رفیعی دروازه بان پرسپولیس و همسرش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/131978" target="_blank">📅 12:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131977">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔵
سهراب بختیاری‌زاده: پرسپولیس عادت به فساد کرده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/131977" target="_blank">📅 12:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131975">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
رونمایی از لیست ۶۰ نفره قلعه‌نویی برای جام جهانی ۲۰۲۶؛ غیبت قطعی احمد نوراللهی
👀
امیر قلعه‌نویی در حالی لیست اولیه‌اش برای جام جهانی ۲۰۲۶ را تنظیم کرده که مشخصاً نام یک چهره در این فهرست به چشم نمی‌خورد؛ احمد نوراللهی!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/131975" target="_blank">📅 10:56 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131974">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✅
#فوری | آکسیوس:
🔻
یک منبع آمریکایی گفت ترامپ به نتانیاهو گفته است که میانجی‌ها در حال کار بر روی یک «توافقنامه» هستند که هم ایالات متحده و هم ایران آن را امضا خواهند کرد تا رسماً به جنگ پایان دهند و یک دوره ۳۰ روزه مذاکره در مورد مسائلی مانند برنامه هسته‌ای…</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/131974" target="_blank">📅 10:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131973">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🏅
باشگاه پرسپولیس هزینه کامل دادرسی پرونده شکایت از بیرانوند را به CAS واریز کرد
⏺
باشگاه پرسپولیس که پیش از این بابت پرونده علیرضا بیرانوند دروازه‌بان تراکتور به دادگاه عالی ورزش شکایت کرده بود برای اینکه این دادگاه رای نهایی را صادر کند هزینه‌های دادرسی را…</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/131973" target="_blank">📅 10:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131972">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VaswRZ6vUQaGyhH8ICzIvBAASninXNguoSK7GcVgUg4qjay8QK0JOBQDo41eiRDUY5pAtxqL212o8tWGyg5sOnZaBkpLzC4idlUQE3oz5_66Nurn_Q3kbykyH7EP5lVF4ulAbTOqJdH-QpHlw8vcFisVHJ9EdK_hJQHS6XBhmwCvpnJSe2w_mTgfnnehVmUyupihYs1OL-8dj2nmakSonGNk4ZRe6B8zceqE40-4vGXr4nEYCi7LtwU11lIdJoUXJO_EY75J5VBs-CJK61-_7RHC11ZfPPTXyhcX5H5yV9-Bv1xZKsrf4MoRsz2332ZApP2662QSPHJHJsC0Tf3VHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
واکنش باشگاه سپاهان به باشگاه هایی که با بازیکنان این تیم مذاکره کرده اند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/131972" target="_blank">📅 10:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131971">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">⚽️
❤️
سردار دورسون: از ایران و ترکیه پیشنهاد دارم
🔴
امیدوارم صلح به ایران بازگردد
🔴
از روز اول رابطه خوبی با هاشمیان نداشتم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/SorkhTimes/131971" target="_blank">📅 10:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131970">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❗️
فوری/  عضو کمیسیون امنیت ملی مجلس:  عاصم منیر فردا حامل پیام جدیدی از سوی آمریکا به ایران است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/SorkhTimes/131970" target="_blank">📅 10:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131969">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
| فرهیختگان:
✅
باشگاه پرسپولیس با باشگاه سپاهان سر مبلغ قرارداد مهدی لیموچی به توافق نرسیدند و خود مهدی  نیز دوست دارد فصل بعد در سپاهان توپ بزند چون احتمال آسیایی شدن این تیم بیشتر است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/SorkhTimes/131969" target="_blank">📅 00:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131968">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✅
#فوری | آکسیوس:
🔻
یک منبع آمریکایی گفت ترامپ به نتانیاهو گفته است که میانجی‌ها در حال کار بر روی یک «توافقنامه» هستند که هم ایالات متحده و هم ایران آن را امضا خواهند کرد تا رسماً به جنگ پایان دهند و یک دوره ۳۰ روزه مذاکره در مورد مسائلی مانند برنامه هسته‌ای…</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/SorkhTimes/131968" target="_blank">📅 00:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131967">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SorkhTimes/131967" target="_blank">📅 00:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131966">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✅
#فوری | آکسیوس:
🔻
یک منبع آمریکایی گفت ترامپ به نتانیاهو گفته است که میانجی‌ها در حال کار بر روی یک «توافقنامه» هستند که هم ایالات متحده و هم ایران آن را امضا خواهند کرد تا رسماً به جنگ پایان دهند و یک دوره ۳۰ روزه مذاکره در مورد مسائلی مانند برنامه هسته‌ای…</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/131966" target="_blank">📅 23:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131965">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
عاصم منیر فردا به تهران می‌رود احتمالا خبر مهمی در راه است
🔴
روزنامه ابزرور پاکستان: فیلد مارشال سید عاصم منیر، رئیس ستاد ارتش، به عنوان چهره‌ای کلیدی در روند دیپلماتیک ایران و آمریکا، فردا به ایران می‌رود. در طول این سفر احتمالی، انتظار می‌رود اعلامیه‌ای…</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/131965" target="_blank">📅 23:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131964">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❗️
ترامپ: منتظر پاسخ مناسبی از ایران هستیم تا از تشدید بیشتر جلوگیری کنیم.
🔴
چند روزی منتظر پاسخ ایران خواهیم ماند.
🔴
تا زمانی که به توافق نرسیم، هیچ تحریمی را از ایران برنمی‌دارم.
🔴
در ایران افراد باهوش و بااستعدادی وجود دارند و امیدواریم معامله‌ای خوب برای…</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/131964" target="_blank">📅 23:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131963">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
‏
ترامپ: اگر توافق امضا نشود، ایران این آخر هفته برق نخواهد داشت
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/131963" target="_blank">📅 23:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131961">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✅
سرخپوشان نمی‌خواهند خسارت بدهند
✅
پرسپولیس به‌دنبال تنظیم دفاعیه برای شکایت اوریه
✅
فرهیختگان: سرژ اوریه یکی از خریدهای عجیب باشگاه پرسپولیس در بازار نقل و انتقالات تابستانی بود. در واقع همان مقطعی که رضا درویش بابت خرید اوریه در رسانه‌ها از بهترین خرید…</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/131961" target="_blank">📅 22:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131960">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
خروجی های پرسپولیس تا به این لحظه :
🔺
سروش رفیعی
🔺
میلاد محمدی
🔺
مرتضی پورعلی گنجی
🔺
دنیل گرا
🔺
تیوی بیفوما
🔺
امید عالیشاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/131960" target="_blank">📅 22:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131959">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
🚨
اسامی ٣٠ بازیکن دعوت‌شده به اردوی نهایی تیم ملی در ترکیه  علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد خلیفه  احسان حاج صفی، میلاد محمدی، امید نورافکن، شجاع خلیل زاده، علی نعمتی، حسین کنعانی، دانیال ایری، رامین رضاییان، صالح حردانی  سامان قدوس، روزبه…</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SorkhTimes/131959" target="_blank">📅 22:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131958">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">تأیید محکومیت 15 میلیاردی شمس آذر در ماجرای فخریان
🔴
کمیته استیناف فدراسیون فوتبال رأی محکومیت باشگاه شمس آذر قزوین در پرونده انتقال مجتبی فخریان به پرسپولیس را تأیید کرد و به این ترتیب باشگاه قزوینی باید این مبلغ را به پرسپولیس بازگرداند.
🔴
باشگاه پرسپولیس…</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/131958" target="_blank">📅 22:41 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131957">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
🚨
🚨
#فوری | ترامپ:
🔻
همه چیز تمام شد. تنها سوال این است که آیا ما می رویم و آن را تمام می کنیم، یا آنها قرار است سندی را امضا کنند؟ ببینیم چه اتفاقی می افتد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 983 · <a href="https://t.me/SorkhTimes/131957" target="_blank">📅 22:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131956">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
عاصم منیر فردا به تهران می‌رود احتمالا خبر مهمی در راه است
🔴
روزنامه ابزرور پاکستان: فیلد مارشال سید عاصم منیر، رئیس ستاد ارتش، به عنوان چهره‌ای کلیدی در روند دیپلماتیک ایران و آمریکا، فردا به ایران می‌رود. در طول این سفر احتمالی، انتظار می‌رود اعلامیه‌ای مبنی بر تأیید تکمیل پیش‌نویس نهایی توافق منتشر شود.
🔴
این سفر می‌تواند به عنوان یک نقطه عطف دیپلماتیک سطح بالا باشد، جایی که تکمیل نسخه نهایی توافق ممکن است رسماً اعلام شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 969 · <a href="https://t.me/SorkhTimes/131956" target="_blank">📅 22:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131954">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
باشگاه پرسپولیس با مهدی لیموچی، بازیکن سپاهان وارد مذاکره شده و این بازیکن به همین علت درخواست جدایی از تیم سپاهان را ارائه کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 917 · <a href="https://t.me/SorkhTimes/131954" target="_blank">📅 22:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131953">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00eb689252.mp4?token=JFmSwghiSXye8Sgy5IAchAJc6CLHDYLmISnToAljPmDwMaA3MKYNFjqF3keIgQqoV6efvKUYLAjTj7zY1d8SyiZ6Kg2KfaW9zJJxXSj_JWrpbZp6Ux8zI0o-jjQgR5nrlxlWzlVFW8E_a6AQu4_9S9n6Te-nLSx-WnkzNf9c-sENAskvLmgdCovxcHxpXFeghFxCsGPgL1O1SU6rE_QkpnhkGOHfm7luzBaKXe60oQUPKhzgzEkUUnFN7NMaOIUnqWjP0z9BiXkQHE-FwLRHBLeT08J9xNv2zIS8nJ61NL5kEKjjH1P7f3IGIvbhggqh7kGMNqHiwJP6xRtDg5EqBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00eb689252.mp4?token=JFmSwghiSXye8Sgy5IAchAJc6CLHDYLmISnToAljPmDwMaA3MKYNFjqF3keIgQqoV6efvKUYLAjTj7zY1d8SyiZ6Kg2KfaW9zJJxXSj_JWrpbZp6Ux8zI0o-jjQgR5nrlxlWzlVFW8E_a6AQu4_9S9n6Te-nLSx-WnkzNf9c-sENAskvLmgdCovxcHxpXFeghFxCsGPgL1O1SU6rE_QkpnhkGOHfm7luzBaKXe60oQUPKhzgzEkUUnFN7NMaOIUnqWjP0z9BiXkQHE-FwLRHBLeT08J9xNv2zIS8nJ61NL5kEKjjH1P7f3IGIvbhggqh7kGMNqHiwJP6xRtDg5EqBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
قلعه‌نویی به نورافکن: آقای امیدخان نمیفهمی پای راسته؟ حتی اینم نمیفهمی
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 924 · <a href="https://t.me/SorkhTimes/131953" target="_blank">📅 22:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131952">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1098692638.mp4?token=tI6yCPZg002jIHtUP5bM9MG4FJzl8VtsWDNAaJdnmlqfAwN977MfYYs3WhrAzAVC5NCp7tWXaoBUzEfMcM83VwZkkUsMdJgX4dAq_n7qJTlUfBtfvUorAO1oBpoUwWBsh3E36UIFEiVbxWBcZZ_Bu_fqHcxqOAqmYICmwDzz3pqWR5AwVami29wd8uwP2KNYGw5qUl9W0owzeAEsB8oqlAEeTNkjmNlAT4_1ESbHgSyjkmrcQVKhuhUCV8klUUspHH02qpiHVjElAjZfDjKgDbXRQp_2K5t0UNlN4_RrY2vhbs39X3eQhWzPAHfKiFfH5dPx7APXj6TLarUjMy_OHg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1098692638.mp4?token=tI6yCPZg002jIHtUP5bM9MG4FJzl8VtsWDNAaJdnmlqfAwN977MfYYs3WhrAzAVC5NCp7tWXaoBUzEfMcM83VwZkkUsMdJgX4dAq_n7qJTlUfBtfvUorAO1oBpoUwWBsh3E36UIFEiVbxWBcZZ_Bu_fqHcxqOAqmYICmwDzz3pqWR5AwVami29wd8uwP2KNYGw5qUl9W0owzeAEsB8oqlAEeTNkjmNlAT4_1ESbHgSyjkmrcQVKhuhUCV8klUUspHH02qpiHVjElAjZfDjKgDbXRQp_2K5t0UNlN4_RrY2vhbs39X3eQhWzPAHfKiFfH5dPx7APXj6TLarUjMy_OHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
#فوری
| ادعای آکسیوس:
🔻
قطر پیش‌نویس توافق جدیدی برای کاهش تنش‌ها میان تهران و واشنگتن ارائه کرده است
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 938 · <a href="https://t.me/SorkhTimes/131952" target="_blank">📅 22:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131951">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
ورزش سه: روزبه چشمی از ناحیه رباط صلیبی مصدوم شد و جام جهانی رو از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 935 · <a href="https://t.me/SorkhTimes/131951" target="_blank">📅 21:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131950">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDb3Ac7lxFBC9N94vGczh-5FykNzpH6OGtH8uoHxP001Ku0z9Lxm_ci_pAE1YR-NsgTCvAbrFAvkFSEqlfGw4RwbEG943t9LgIYokME69v3I7FZQ7R_CypHpS9huQUZ_naTb3KmqMpTh5dmDqmcbotwCWvococ1zUcUUSnoPcmoahQAZIEZXiQyJ6gFNDnKJNwP2T1PXs1jNKhqusNMLASbn7pTyKfansVOq-oOJ4eBgFwuNrQh7_TfYwCi34jg6z7O3LofWQc_xbeWvPYMa_IqRBs_oinivRI92XKkEi5XcegokujLoZ0itK_yLUtGztbr3W-r-G3FniW7FSaUU8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
Final Europa League
⚫️
Freiburg -
🔵
AstonVilla
‼️
این روزا قبل از پیش‌بینی بیشتر از خود بازی باید نگران این باشی که VPN وصل میشه یا نه.
😀
ربات تلگرام وینکوبت دقیقاً برای همین شرایط خوبه چون کل سایت داخل خود تلگرام اجرا میشه و دیگه لازم نیست هی بین سایت و VPN درگیرشی:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
براحتی میتونید برای بازی فینال لیگ اروپا وارد سایت بشید و این دیدار رو پیش‌بینی کنید، واریز و برداشت هم بصورت آنی می‌باشد.
📌
کانال رسمی وینکوبت:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SorkhTimes/131950" target="_blank">📅 21:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131949">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
5 گیگ 800T
10 گیگ 1.5T
🛜
مناسب برای تمام سایت ها اپ ها
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 947 · <a href="https://t.me/SorkhTimes/131949" target="_blank">📅 21:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131946">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/050c7fea46.mp4?token=eWncf8bLT1zcUi7NpqqVYd_SjuclxUENljtvqorq1emUNr_Pn9BDD8uRt1k-ltWqVKtVNNksmA8630ApuY5BX0w9qniH1rLKbkBO4oF3Ndo6K7GGQRep3S0QJpx3hFFfnUkkS2zV4hVgteujoHeTl19DoV7W2p56S4ZIaqhhC38X7V1pidpswQbDkZeyXtfOREl_UU1mC7UwvWEaKoMa5dMCRuV5n0lLPk0-R3ojhhlJCLGCSAKyZmpWq9ZfVcAxMmM558I40YZ9HYVDxtU60quRpPZl6GLWDwiHmN0H86rSTrP7YIfjBv3Ckk4cLDywQpQx4QGj4B8mbD2ubZgGOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/050c7fea46.mp4?token=eWncf8bLT1zcUi7NpqqVYd_SjuclxUENljtvqorq1emUNr_Pn9BDD8uRt1k-ltWqVKtVNNksmA8630ApuY5BX0w9qniH1rLKbkBO4oF3Ndo6K7GGQRep3S0QJpx3hFFfnUkkS2zV4hVgteujoHeTl19DoV7W2p56S4ZIaqhhC38X7V1pidpswQbDkZeyXtfOREl_UU1mC7UwvWEaKoMa5dMCRuV5n0lLPk0-R3ojhhlJCLGCSAKyZmpWq9ZfVcAxMmM558I40YZ9HYVDxtU60quRpPZl6GLWDwiHmN0H86rSTrP7YIfjBv3Ckk4cLDywQpQx4QGj4B8mbD2ubZgGOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
❤️
سردار دورسون: از ایران و ترکیه پیشنهاد دارم
🔴
امیدوارم صلح به ایران بازگردد
🔴
از روز اول رابطه خوبی با هاشمیان نداشتم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/SorkhTimes/131946" target="_blank">📅 20:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131945">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GphksWoZDh0N04DfIns5c2VGOFdWovHjKnZueELxMbo_GQNYOoNlsqaYM8f3LDflFBOCodFnvpwW7WJUtZzwNTaV4j2rLgZlCRpWdjZlerY2AqAo6J4R8SLo01qyYz2SjwgaK64uiPKWvarNsDp433ahhbYSdeWrGzHUwMP0bSDd5ZxEyyhV0Jt45GMTbkqOKZwoe9YAqr1PGkJ06hajhtXpSZ687lAlA3Ix_2YhMbYGQC2IUw2E99BF4ABOkd_ycmg0Vka_mpW4ZZefV0jaurhk1fvVNLvO9lzCYf-I6k7WLu5GsrNRIWjogxH4VPaeUYDwpE48Iif96vtWPwa8sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوووووری
شبکه الحدث :
احتمالا طی ساعات آینده، متن توافق ایران و آمریکا نهایی میشه؛ دور بعدی مذاکرات هم باز تو پاکستانه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SorkhTimes/131945" target="_blank">📅 20:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131944">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔥
۲عدد سرور ۱۰ گیگ اف خورده ۱۹۰۰
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SorkhTimes/131944" target="_blank">📅 19:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131943">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84765e9843.mp4?token=IiAIF1LplcN7j0jc9rmH3u3l1lJkauzBuGh7DLTYjEG-gaSJ31OTiXiqU1BX777MX7za7CPVc_3ktdz59l92JusbHoz6hZwiR8wE7Q-SdD3HA5mVDjYxQVVl8XdvsbQhP64ztP7kllY0bCsKrgRHN4YThYGYd35dRs_ZxJte-bbdMjWDZX0YEXU2kIhDr1PspzkO04jUFAsRsC2uGWsUP1QYjddZIR68d0a9WcLz7mdgt5g9J4rla7IM78gSRQgRJBfeBV4Kh-ICP_h8BnjB-hR_aSK_pwOpJWVqchIa-GW9ecwi0gqsEq-B90V15AUrkUB0wX0ZLbrd18ovorv4wzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84765e9843.mp4?token=IiAIF1LplcN7j0jc9rmH3u3l1lJkauzBuGh7DLTYjEG-gaSJ31OTiXiqU1BX777MX7za7CPVc_3ktdz59l92JusbHoz6hZwiR8wE7Q-SdD3HA5mVDjYxQVVl8XdvsbQhP64ztP7kllY0bCsKrgRHN4YThYGYd35dRs_ZxJte-bbdMjWDZX0YEXU2kIhDr1PspzkO04jUFAsRsC2uGWsUP1QYjddZIR68d0a9WcLz7mdgt5g9J4rla7IM78gSRQgRJBfeBV4Kh-ICP_h8BnjB-hR_aSK_pwOpJWVqchIa-GW9ecwi0gqsEq-B90V15AUrkUB0wX0ZLbrd18ovorv4wzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سردار دورسون‌ مهاجم سابق پرسپولیس مهمان امروز تمرین تیم ملی بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/131943" target="_blank">📅 19:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131942">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✅
#تکمیلی | ترامپ:
🔻
یا با ایران به توافق می‌رسیم یا کارهای سختی انجام خواهیم داد و امیدواریم این اتفاق نیفتد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/131942" target="_blank">📅 19:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131941">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
نصیرزاده، وکیل علیرضا بیرانوند: در صورتی که حتی رای محرومیت ۴ ماهه این دروازه‌بان توسط دادگاه CAS تایید شود، محرومیت وی شامل جام جهانی نخواهد شد.
⏺
به محض اینکه هزینه دادرسی واریز شود، رای صادر نمی‌شود. تا بخواهند رای را صادر کنند جام جهانی تمام شده است.…</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/131941" target="_blank">📅 19:24 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131940">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❗️
🔻
ادعای العربیه: ممکن است طی ساعات آینده از نهایی شدن نسخه نهایی توافق بین آمریکا و ایران خبر داده شود  العربیه:
🔹
کار برای نهایی‌سازی متن توافق بین واشنگتن و تهران در حال انجام است. فرمانده ارتش پاکستان ممکن است فردا برای اعلام نسخه نهایی توافق از ایران…</div>
<div class="tg-footer">👁️ 975 · <a href="https://t.me/SorkhTimes/131940" target="_blank">📅 19:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131939">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❗️
🔻
ادعای العربیه: ممکن است طی ساعات آینده از نهایی شدن نسخه نهایی توافق بین آمریکا و ایران خبر داده شود  العربیه:
🔹
کار برای نهایی‌سازی متن توافق بین واشنگتن و تهران در حال انجام است. فرمانده ارتش پاکستان ممکن است فردا برای اعلام نسخه نهایی توافق از ایران…</div>
<div class="tg-footer">👁️ 967 · <a href="https://t.me/SorkhTimes/131939" target="_blank">📅 19:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131936">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✅
🇺🇸
ترامپ: آمریکا در «مراحل نهایی» مذاکرات با ایرانه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 974 · <a href="https://t.me/SorkhTimes/131936" target="_blank">📅 19:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131935">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
ترامپ درباره ایران: من عجله‌ای ندارم، همه میگن انتخابات میان‌دوره‌ای و اینا، من برای جنگ اصلاً عجله ندارم.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 911 · <a href="https://t.me/SorkhTimes/131935" target="_blank">📅 19:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131934">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUv1DSh1qQaZbcmHGMY8kBnP847SRT5jtT-MV9_P2zzQrCljB3_I3mhQasA2dAraKZD2YKzGIRRgp0zgBxChTxFRbBPQ5ersuGP3OOuXGW2WoYZZwl-wq1xmPsPGQFR1gWDKsz9SiEOY5TagjJHtUsh_r9_SR0lLLG0SQ_caVd0cG_cUGaqM-qVZf0IgSTXkk8l3WGY9k7tPs7Nz6Nth2he78GGBpAPZa0Ji9EQQnL15eOO9HLJVbOQjzJZwAj_TWsjUkBp2uX6cbpnMh4tA3HSvgYtKZZSLYhWsMukDVQOU6t91HwO__eYUiTfsmYVnk6Se6lQHTyQ7vvmKHK5aBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
شکایت یک شرکت تبلیغاتی از باشگاه پرسپولیس در دادگاه تجدید نظر رد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 965 · <a href="https://t.me/SorkhTimes/131934" target="_blank">📅 18:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131933">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RcXq6VS5xAqf1Nxzezxc8yrKhx_G84Cd_FMOtK-q3p5ddJVM4upNtviXV-FrPqr6R9w6PEIDhAE4TF-gd0lxvRAoulWGDCys82yCjMYv0oNWTqtTcDk2HfucuVp-7Z__uDEFX8YYXL0GQk8ijGGc8uXcFEEr7MCS4gnicN8i1SX36R8BxXjr449GHD1AV0yK-6C8YHOkM5501jghV9TATDzw5HE4rTqE6DcDS2_y1nINsqUFtUMR3Eh1VR-BNQRnOJvfib7akyfeDpN_P5BCHjDTAhGj7v7lMlvrqdqF2w-7QPjK6fWPzRFLUkHX_PTjl0xxc11Avqog0codArv5wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖍
بازیکنان مطرح تیم ملی سعی میکنند سردار آزمون تو لحظات آخری برگرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 980 · <a href="https://t.me/SorkhTimes/131933" target="_blank">📅 18:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131932">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ab8278f1.mp4?token=aHgIUpZ6q4R8pEVngG5K9eyCkb-FKrOkB3RvVA1RoLLobaPbYtpTFLO5iZ6E8meBQS1yN75nrRPqnw46gVT8IjVgDKzIkSNWjiBB5xEv3OfSQskBVLqFgO1LS3UAXu_EyWkGgr1YIkcaf53E3Qwl3uHxdPA4BPnR3Q7X0mjJJa7O5RHIre2v3KcnlqNfm_JEo19KwKmOTKwvI8whWIEgX1MYkr_SBM1dnBLQA5EZPje9mDvWgm9cOcqqgjvbDf-TJr_EukK4bUaWIlZ0P4tMUKc8axHDJNz4ob7b7p9pGFL4DVwydfDmwM7THOfxQzFv8NyFvX-8Bv231Lsp4C3lJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ab8278f1.mp4?token=aHgIUpZ6q4R8pEVngG5K9eyCkb-FKrOkB3RvVA1RoLLobaPbYtpTFLO5iZ6E8meBQS1yN75nrRPqnw46gVT8IjVgDKzIkSNWjiBB5xEv3OfSQskBVLqFgO1LS3UAXu_EyWkGgr1YIkcaf53E3Qwl3uHxdPA4BPnR3Q7X0mjJJa7O5RHIre2v3KcnlqNfm_JEo19KwKmOTKwvI8whWIEgX1MYkr_SBM1dnBLQA5EZPje9mDvWgm9cOcqqgjvbDf-TJr_EukK4bUaWIlZ0P4tMUKc8axHDJNz4ob7b7p9pGFL4DVwydfDmwM7THOfxQzFv8NyFvX-8Bv231Lsp4C3lJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ورود کادرفنی تیم ملی به کمپ تمرینی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 876 · <a href="https://t.me/SorkhTimes/131932" target="_blank">📅 18:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131931">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcc1b48df0.mp4?token=OLuntjOLA6Q80E2cNCuPcvkVgBHxi0fjobMh7OwdBTPL-IRUvJxvLpNRXJlGZBiIunL1LNBDi87rI_W2Y8KPLQy1DLOvvGE_gz0TQ-Ly2rD4I1itmpxQitSKHd422GKMSXz_57Czaxn7_SgO0TzSFDMNZgkAs-EPYu4DdPNYABxMuFnMQedpOuAFVSqnhX8S_9oHwM4C-mcut5m_5BOX-rmHt_0bWEhUtIpIT3YEbSgV7PiVqYg6gWQeESOdLkVvH_UUbn8Kyqkm5HnnFFZiOk6ZQa6v1PXm9Jv4pEOVX47N6mCZd3Xf5VsnB37y6JPLxxLcdtANcrbC2t1mDjM6pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcc1b48df0.mp4?token=OLuntjOLA6Q80E2cNCuPcvkVgBHxi0fjobMh7OwdBTPL-IRUvJxvLpNRXJlGZBiIunL1LNBDi87rI_W2Y8KPLQy1DLOvvGE_gz0TQ-Ly2rD4I1itmpxQitSKHd422GKMSXz_57Czaxn7_SgO0TzSFDMNZgkAs-EPYu4DdPNYABxMuFnMQedpOuAFVSqnhX8S_9oHwM4C-mcut5m_5BOX-rmHt_0bWEhUtIpIT3YEbSgV7PiVqYg6gWQeESOdLkVvH_UUbn8Kyqkm5HnnFFZiOk6ZQa6v1PXm9Jv4pEOVX47N6mCZd3Xf5VsnB37y6JPLxxLcdtANcrbC2t1mDjM6pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
زمین تمرینی شماره یک تایتانیک، محل تمرین امروز تیم ملی ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 941 · <a href="https://t.me/SorkhTimes/131931" target="_blank">📅 18:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131930">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❗️
پاکستان متن توافقات اولیه را آماده کرده است و مذاکرات بعد از عید قربان در اسلام آباد انجام خواهد شد و تا ساعات آینده و نهایت تا فردا عاصم مونیر پایان جنگ را اعلام خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 946 · <a href="https://t.me/SorkhTimes/131930" target="_blank">📅 18:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131928">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
#فوری | رسانه‌های سعودی:
🔻
فرمانده ارتش پاکستان ممکن است فردا به ایران سفر کند تا نسخه نهایی توافق را اعلام کند. ممکن است طی ساعات آینده نسخه نهایی توافق بین آمریکا و ایران اعلام شود
‼️
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 940 · <a href="https://t.me/SorkhTimes/131928" target="_blank">📅 18:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131926">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e0676b3f8e.mp4?token=G5_s7_U5Xgb4X1U28rcN0OcaV__2peG4w24cvLY5d-aP8Xjl7V5hXoucAU8UIdxcveRMeDuxYySP1sxz5F92YChx7pGC2Ix_tFIRMPggxs7R1aJd8-dpLvyzXvnJTEjeYhyk-KTHp0KhSMciBDj2N0PN0Gwuuo1CESbKDd1jqP_Hzx8AeRNY6KQ6FFeBE6T4uXLrYQPTcqW-KYLmgC3bWu1SGNiBGP88iLWhhN2z85wkEP8q_kj7JpVcNRFjEZ0TGKTS5IelXnajT1x3GMtO2JH0FFvoxeyNMBqAO0o4LaHzQgG5jwJi34I-zojBqXWv7Eeui331atUcoUSsY8hLcw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e0676b3f8e.mp4?token=G5_s7_U5Xgb4X1U28rcN0OcaV__2peG4w24cvLY5d-aP8Xjl7V5hXoucAU8UIdxcveRMeDuxYySP1sxz5F92YChx7pGC2Ix_tFIRMPggxs7R1aJd8-dpLvyzXvnJTEjeYhyk-KTHp0KhSMciBDj2N0PN0Gwuuo1CESbKDd1jqP_Hzx8AeRNY6KQ6FFeBE6T4uXLrYQPTcqW-KYLmgC3bWu1SGNiBGP88iLWhhN2z85wkEP8q_kj7JpVcNRFjEZ0TGKTS5IelXnajT1x3GMtO2JH0FFvoxeyNMBqAO0o4LaHzQgG5jwJi34I-zojBqXWv7Eeui331atUcoUSsY8hLcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
| رسانه‌های سعودی:
🔻
فرمانده ارتش پاکستان ممکن است فردا به ایران سفر کند تا نسخه نهایی توافق را اعلام کند. ممکن است طی ساعات آینده نسخه نهایی توافق بین آمریکا و ایران اعلام شود
‼️
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/131926" target="_blank">📅 18:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131925">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
ترامپ درباره ایران:
من عجله‌ای ندارم، همه میگن انتخابات میان‌دوره‌ای و اینا، من برای جنگ اصلاً عجله ندارم.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/SorkhTimes/131925" target="_blank">📅 17:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131923">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
پژمان جمشیدی به ۹۹ ضربه شلاق محکوم شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/131923" target="_blank">📅 16:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131922">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3fnv4mK47_6tHqDvQibgU08W-9QxpADr6cqGomZRbNg8ZICgP5oaUWunjMKX9k4yeyVxpY0pwQ6b1Z6oL9pIZjF_bXzLQchiIZ9jV5jnA68CzMjGv-IuANkIPpfFy0s24XIEHbisXTxdaWah1LKRnNr0wpbNkBqMuSD_QaoA55WDm8y8j_rUKim3K5f1ZVXRflZjip-X05X6Bx-_z4kDtMYPwDPA8vUsv5XzaVC-OOAVOuzCy3SnC9PpAI2urSk0oYABuhtGcgBdOunQXaGwahQjeslnpAyJA4hfe8aeRXBXXAlxgPB545wKSCsXnK8LU75P4AulMJYkKUMXb1i-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/131922" target="_blank">📅 16:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131921">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
ادعای خبرگزاری فرهیختگان: آریا یوسفی و مهدی لیموچی در سبد خرید پرسپولیس قرار گرفته اند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/131921" target="_blank">📅 15:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131920">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9m2h7lI6mz8YsYyt9xkwSxOhmU-JH8v-ddr2Nq_NNJnLyHtYd-xZvrE-nwI4zZpEUnvj2VAPOquVkCfNCJndbmj3fGMYBXlxC5C9X_hDLVobJ5Ec1SCEKWxnBPqQ2h3exM3g7i0U7tMzXbxUZWc4-4y2LWfEK7anugNnBNknfPANsdHE_NHrrQMfXYKnghkFI-Pkzmlu1kzTLWbPr97XoTXbnkxfzzJSptLG4BCxV-rAsPl7BCnwoDurUsnotS6ZXPlswnLTJUfZZLoUmEpn_V9HHMt19Mpp9OG98JRCouarlsqKbrcfLGTApHI16eD2Xj4PiB21VBHnVcg7WUh-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ادعای خبرگزاری فرهیختگان: آریا یوسفی و مهدی لیموچی در سبد خرید پرسپولیس قرار گرفته اند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/131920" target="_blank">📅 15:29 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131919">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
فووری؛ اوستن اورنوف ستاره ازبک پرسپولیس در تمرینات تیم ملی این کشور مصدوم شده و وضعیتش برای جام جهانی نامشخص است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SorkhTimes/131919" target="_blank">📅 15:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131917">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/131917" target="_blank">📅 15:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131915">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbB-wbcpJ0T7XYnpZ4La_4ZVGfRehsmW-81oNG8UPrMMIJ2oOtm14OBRkOVcsE6NauXFk_dKxsGHfN-Ki5x3J-WwY9TXZxFGYS6bKMMC3UJI6h3K0l8f4mvFd1qplnV0Vo3rz_y0TTiOF2R_DxgE8szkq_RP4q17660O0Jg7wzOUO6P3eDdNyjasY0jGt6ib17Jon67GxwLebrXdtPj5anR36RXqRdrEStnC5Y_2KM5DEUU3vtqGETMGPama8tP9Xid4rIIdPQ1QfgicO9kAoKLKqpBNaVErt60HVOnAlMxdmDt0imfJTWtFMHQLHEEud75O2DDpAGxXWDRzqnsmPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
توییت مهدی روزخوش مدیر رسانه ای باشگاه
😂
👌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/SorkhTimes/131915" target="_blank">📅 12:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131914">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5EmXBs3gl_K7-zpca-cfHD2jhkeL4BuepHV2fPFwSCVu570Vppz7PJcBIT17PpViTQtMX2WOyykxdSSX2iawl9mUdUu_-mCIbRYjSehHNsbQh12S9b39aGbhu9jBLjEpoobIlCCJo6uBUt2_o3Vo_SzqtdEcMiww7L_Orf1EXeyJUSonJ-91STMmMxLGo8odrKARs6EgPzXPgSu42ahWgp2k_G-YL-tSx8-qSLwuSeJ27DHx3z1r0R7VYCFjcijZeyOmYgKuMpHZalvRLjPdi174uQk4g0xmPMvz9XOSKOvt4tkMfgQJWpfzJOImvPUxoY-3bmGLLmiMP_vIG0VmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/131914" target="_blank">📅 12:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131913">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
ترامپ درباره ایران: ممکن است مجبور شویم ضربه بزرگی دیگر به آنها وارد کنیم. هنوز مطمئن نیستم
🔹
خیلی زود خواهید فهمید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 955 · <a href="https://t.me/SorkhTimes/131913" target="_blank">📅 12:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131912">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">محمد پروین، فرزند علی پروین:   پدرم به دلیل زخم پا (به علت دیابت) در بیمارستان بستری شده است، اما مشکل خاصی ندارد و به زودی مرخص می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 990 · <a href="https://t.me/SorkhTimes/131912" target="_blank">📅 12:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131911">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBQUBcpw1j9w6_FiQBdPLhfEnVJKJNE-Z9Rji1k8pt86wdyRDPvZTnF7wqWregYqCSUfbwud88TfeOtfp-5wQX16gMolduZIv38H8nKkecbtJ1uPqhgU4KYxMnGSQg7RXyB0cUrsoBBmRmanpTDwOTXaQ70T5T8x62rAeldcZX7v3RgG69p-eVBEB_cPtD_BAssheCwL22piTYDm_4X5ZOBbHu3_2YABBMn2Dr3LDdpVoZ53rWt9r3sfSTl24rZ-hZT6RgU46tXxHeF7ImjfBr7bd55miVK0iZqUHd_UoSwrehFOih3oRjIrgfNDSVAwmpKcAj5GgXq4gTby4cDH7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نیویورک تایمز :
🔴
فیفا قصد دارد دوباره ورود پرچم «شیر و خورشید» ایران پیش از انقلاب و لباس‌های مرتبط با آن را به ورزشگاه‌های جام جهانی ۲۰۲۶ ممنوع کند. این پرچم در جام جهانی ۲۰۲۲ قطر هم محدود شده بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 980 · <a href="https://t.me/SorkhTimes/131911" target="_blank">📅 10:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131910">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
شایعه حضور تارتار روی نیمکت پرسپولیس از کجا آب می‌خورد؟
💸
یک دلال با سوءاستفاده از شرایط جنگی و شایعات درباره بازنگشتن خارجی‌ها ، پیشنهاد داد در صورت نیامدن اوسمار ، تارتار سرمربی پرسپولیس شود.
⛔️
این پیشنهاد جدی گرفته نشد و مدیران پرسپولیس قصد دارند همکاری…</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/SorkhTimes/131910" target="_blank">📅 10:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131909">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✅
ونس معاون اول رئیس‌ جمهور در مصاحبه جديد خود اعلام کرد اصلا متوجه نمیشم مقامات رژیم ایران چه میگویند یا چه چیز میخواهند فهمیدن حرف هایشان واقعا سخت است و مدام حرف ها و خواسته هایشان تغییر میکند و نميتوانند به یك تصمیم واحد برسند ، اون 440 کیلو اورانیوم باید…</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/131909" target="_blank">📅 10:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131908">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
قاتل الهه حسین زاده با اذان صبح فردا اعدام می‌شود.
❗️
استوری خواهر الهه: امشب، قصاص مرهم داغ خواهرم نمی شود... اما شاید کمی از بی عدالتی این دنیا کم کند. الهه جانم...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/SorkhTimes/131908" target="_blank">📅 10:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131906">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/131906" target="_blank">📅 00:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131904">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❗️
#فارس مدعی شد ؛ مدیرای پرسپولیس اصراری به موندن علیپور ندارن و اگر اوسمار هم بگه نمیخوام قرارداد علیپور تمدید نمیشه.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SorkhTimes/131904" target="_blank">📅 23:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131903">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">⚪️
مهدی تاج: اگر پرچمی به جز پرچم جمهوری اسلامی وارد استادیوم شود به آمریکا نخواهیم رفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SorkhTimes/131903" target="_blank">📅 23:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131902">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
⭕️
🔴
حضور حسین کنعانی زادگان و رضا درویش در منزل خانواده زنده یاد الهه حسین‌نژاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/131902" target="_blank">📅 23:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131901">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">⚖
پژمان جمشیدی تو جلسه دادگاهی امروزش: «من قسم میخورم که هیچکاری نکردم و این اتهام درست نیست. من با این دختر کاری نکردم و اصلا بهش دست هم نزدم. به روح مادرم قسم میخورم که من کاری باهاش نکردم.»
◽️
وکیلش هم گفت ادله و مستنداتی به دادگاه ارائه دادیم که بی‌گناهی…</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/SorkhTimes/131901" target="_blank">📅 23:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131900">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">💢
مزخرفات خنده دار سهراب بختیاری زاده سرمربی کیسه: یک ذهنیت به وجود آمده است که پرسپولیس عادت کرده است که بعضی وقت‌ها با فساد بازی را ببرد یا به این عادت کرده است که همیشه دستش را  به نحوی بگیرند و کمکش کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/SorkhTimes/131900" target="_blank">📅 22:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131899">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">💢
مزخرفات خنده دار سهراب بختیاری زاده سرمربی کیسه: یک ذهنیت به وجود آمده است که پرسپولیس عادت کرده است که بعضی وقت‌ها با فساد بازی را ببرد یا به این عادت کرده است که همیشه دستش را  به نحوی بگیرند و کمکش کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 968 · <a href="https://t.me/SorkhTimes/131899" target="_blank">📅 22:19 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131898">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7eae73a44.mp4?token=aXmJlb-9z_SebO5K6EvSjszjOwU9a1T8LYNBH-ELWNtcBnQNh_owozPgnjge0XzmTZZ3chCbwDzAPJN7Hnt7VnEppi8tVb47tfHQKOzN_UMlXJUdbBFxVmEK2Rw3hRxZ359M-BVy__n8aZzDCkklG8Hnnx7-E-Zh2fSD0m1qEnQZB-uU_SnPxp9P_kyQaMf930gOUO55pWqXYeyd-_lJkcta93kgrS7w2qicRkmxjii4k7Ak5Se2Y4M3kSViG81qwRzZuIWDs4Q_8NL2RddQH7s76RRDtAPYl-PXnj8Y0jK5LOkXWbwTBAxKN5RTzNEO8umgQv-YHY_e6VxLiqFTkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7eae73a44.mp4?token=aXmJlb-9z_SebO5K6EvSjszjOwU9a1T8LYNBH-ELWNtcBnQNh_owozPgnjge0XzmTZZ3chCbwDzAPJN7Hnt7VnEppi8tVb47tfHQKOzN_UMlXJUdbBFxVmEK2Rw3hRxZ359M-BVy__n8aZzDCkklG8Hnnx7-E-Zh2fSD0m1qEnQZB-uU_SnPxp9P_kyQaMf930gOUO55pWqXYeyd-_lJkcta93kgrS7w2qicRkmxjii4k7Ak5Se2Y4M3kSViG81qwRzZuIWDs4Q_8NL2RddQH7s76RRDtAPYl-PXnj8Y0jK5LOkXWbwTBAxKN5RTzNEO8umgQv-YHY_e6VxLiqFTkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
مزخرفات خنده دار سهراب بختیاری زاده سرمربی کیسه: یک ذهنیت به وجود آمده است که پرسپولیس عادت کرده است که بعضی وقت‌ها با فساد بازی را ببرد یا به این عادت کرده است که همیشه دستش را  به نحوی بگیرند و کمکش کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/SorkhTimes/131898" target="_blank">📅 22:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131897">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
باشگاه پرسپولیس: ما میگیم لیگ برگزار بشه ولی ما رو نادیده میگیرن، اونوقت تیم‌هایی که میگن لیگ کنسل بشه، معرفی میشن واسه آسیا. نمایندگان ایران تو آسیا باید با عدالت و در زمین فوتبال معلوم بشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 957 · <a href="https://t.me/SorkhTimes/131897" target="_blank">📅 22:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131896">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✅
💢
بیرانوند از جام جهانی محروم نمی‌شود
💢
رسول باختر، حقوقدان ورزشی در گفت‌وگو با ایسنا: در رای استیناف آمده بود که محرومیت بیرانوند شامل مرحله نهایی مسابقات بین المللی در تیم ملی نیست.
💢
با توجه به این موضوع، حتی در صورت صدور رای CAS پیش از جام جهانی، بیرانوند…</div>
<div class="tg-footer">👁️ 924 · <a href="https://t.me/SorkhTimes/131896" target="_blank">📅 22:04 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131895">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
نصیرزاده، وکیل علیرضا بیرانوند: در صورتی که حتی رای محرومیت ۴ ماهه این دروازه‌بان توسط دادگاه CAS تایید شود، محرومیت وی شامل جام جهانی نخواهد شد.
⏺
به محض اینکه هزینه دادرسی واریز شود، رای صادر نمی‌شود. تا بخواهند رای را صادر کنند جام جهانی تمام شده است.…</div>
<div class="tg-footer">👁️ 962 · <a href="https://t.me/SorkhTimes/131895" target="_blank">📅 22:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131894">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❗️
پرسپولیس شاکی از بمب درویش/ حدادی: اجازه دهید دلایل را نگویم!
🔴
مناقشه باشگاه پرسپولیس با سرژ اوریه، مدافع سابق این تیم، وارد مرحله جدیدی شده و این باشگاه رسماً علیه بازیکن ساحل عاجی خود شکایت کرده است. پیمان حدادی، مدیرعامل پرسپولیس، با اعلام این خبر، ابراز…</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/SorkhTimes/131894" target="_blank">📅 22:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131893">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
ترامپ درباره ایران: ممکن است مجبور شویم ضربه بزرگی دیگر به آنها وارد کنیم. هنوز مطمئن نیستم
🔹
خیلی زود خواهید فهمید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/131893" target="_blank">📅 21:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131892">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2773afe10e.mp4?token=i1Y04TidZfg4wa7RxmF38dxYtchl-HIidVXtf4pSp91XAey252IbSzdEoiQhgvd2ayEgAIUBB_UKG9RtEA8Cs2hG6vztfE3xqfGnq8bwlyqjj-vsd1TV4fPje-tVY-f2NViLgrfMQdtXsIeqgDSSWfxG-VEnwiPBYi6l-MM1sa_QpO_cp5TP0ZbfbxOkTz7KS3kZZgm-c-qo9OPhmfAehomZU0_JNHwITXsN8b6m_W9VTnKgHjXJ5YevMA6iZ7TWlwIHIIK1RId_PWE9Nvh4v4hPcGZvMPq3oxw0LiltyburV7IMoESIfv2NaqdYwZNjJCM9rGCeK2D3F0260XzisQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2773afe10e.mp4?token=i1Y04TidZfg4wa7RxmF38dxYtchl-HIidVXtf4pSp91XAey252IbSzdEoiQhgvd2ayEgAIUBB_UKG9RtEA8Cs2hG6vztfE3xqfGnq8bwlyqjj-vsd1TV4fPje-tVY-f2NViLgrfMQdtXsIeqgDSSWfxG-VEnwiPBYi6l-MM1sa_QpO_cp5TP0ZbfbxOkTz7KS3kZZgm-c-qo9OPhmfAehomZU0_JNHwITXsN8b6m_W9VTnKgHjXJ5YevMA6iZ7TWlwIHIIK1RId_PWE9Nvh4v4hPcGZvMPq3oxw0LiltyburV7IMoESIfv2NaqdYwZNjJCM9rGCeK2D3F0260XzisQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ درباره ایران: ممکن است مجبور شویم ضربه بزرگی دیگر به آنها وارد کنیم. هنوز مطمئن نیستم
🔹
خیلی زود خواهید فهمید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/SorkhTimes/131892" target="_blank">📅 19:19 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131891">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
🔴
اگر وحید هاشمیان و پرسپولیس توافق نکنند، تکلیف صدور کارت مربیگری اوسمار چه می شود؟ هوشنگ نصیرزاده پاسخ می دهد
‼️
‼️
نصیرزاده: برای فسخ قرارداد یا برکناری سرمربی هیچ محرومیتی تعیین نشده است و فقط باید غرامت پرداخت شود. اگر در قرارداد وحید هاشمیان مبلغی برای…</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SorkhTimes/131891" target="_blank">📅 18:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131890">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
باشگاه پرسپولیس با ارسال نامه‌ای به مسعود پزشکیان خواستار جلوگیری از بی عدالتی در اعلام نمایندگان ایران برای فصل بعد رقابت‌های فوتبال آسیا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/131890" target="_blank">📅 18:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131889">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
اعتراض کنایه‌آمیز باشگاه پرسپولیس: نماینده ایران در آسیا نباید با تصمیمات سلیقه‌ای و خارج از زمین فوتبال مشخص شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/SorkhTimes/131889" target="_blank">📅 18:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131887">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✅
با اعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/SorkhTimes/131887" target="_blank">📅 15:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131886">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">⚡️
حکم جلب رشید مظاهری گلر سابق کیسه به خاطر بدهی ۴ میلیاردی صادر شد، میگن متواری شده!
⚡️
عجیبه با این قرارداد های میلیاردی که داشتن ۴ میلیارد بدهکار باشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/SorkhTimes/131886" target="_blank">📅 15:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131885">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
یکی از گزینه‌های اصلی باشگاه ، برای گلر ذخیره جایگزین امیررضا رفیعی آرمین عباسی گلر جوان پیکان تهران است   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/131885" target="_blank">📅 15:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131884">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZqjFxCS7Ri5dXubvi8jkdyxL_7js-n5INBtK_mCdpDHPlDcK5IH7YhyjVsoFSVZvASs_z6Lfaw7zE46RcZOA1D0iimP8FI3lGROT50W-nTpxSyfQxdvYPM1G3gJrzC2rB7rYiql5rFFdV_7_jeabNGkeXhhUf_akWmFXj6dpXpQLWV7D4hnToaKFMDeuOY_CJRJohMUaHbDJzh2LlojH7Z_Hxo-EZo77EG3tTEXcQinlK_5IELC651KAq-Bf3kfs84Y8pcb0_W51vr6oTEyfzQ1ChWzu2EVRMZi92rfOdN_psAfazjsyHCmy95P0-kcOYx5E9Yhq_26_ATWWaIuag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اعتراض کنایه‌آمیز باشگاه پرسپولیس: نماینده ایران در آسیا نباید با تصمیمات سلیقه‌ای و خارج از زمین فوتبال مشخص شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SorkhTimes/131884" target="_blank">📅 15:21 · 29 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
