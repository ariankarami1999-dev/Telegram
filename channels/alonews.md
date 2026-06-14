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
<img src="https://cdn4.telesco.pe/file/uCVdvWSDkQODwAOmJb-g6QbP0m0HQFHmxtnM6sCoAA1bxKjjXG_8093pOXGRdESjfMyLPAkoII7rPicFnG47zm36b6gTLarRFlm7iR5yWABDvznaYOVpu5x_2nTR7zftdIO_xuuoC9laJM3mOXa2x8OTVsEzVlGQrz9GH2BIHJqNZVik2dmKNHlfJVHVgaRW6hY75H45lXh8Hl4g8M_M6WfKJOiJDxBsPAqLQrHDiXRW-MbYiHNJxKlXia4hr2FnVxOZwKqOPZzSsJ4Lr8qaTxiRe-l7WQZbVjGgcXNGS0zLQIlpAP7H6gqRk7Unwn4JBx_9Neo7Vg-G9UIlXGBBPA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 980K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 15:50:01</div>
<hr>

<div class="tg-post" id="msg-127862">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
عراقچی: سرمایه اجتماعی و انسجام ملی، امروز یکی از مهم‌ترین مؤلفه‌های قدرت جمهوری اسلامی ایران در عرصه بین‌المللی است و طبیعتاً هرچه این پشتوانه مردمی تقویت شود، قدرت چانه‌زنی و تأثیرگذاری دیپلماسی کشور نیز افزایش خواهد یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/alonews/127862" target="_blank">📅 15:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127861">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
آی۲۴عبری: اسرائیل در حال حاضر از اظهارنظر درباره اینکه آیا هماهنگی یا اطلاع‌رسانی قبلی با واشنگتن قبل از آخرین حمله به بیروت وجود داشته است، خودداری می‌کند
🔴
به دنبال حمله قبلی در تاریخ ۷ ژوئن، موضع رسمی اسرائیل این بود: «ما در تماس مستمر با آنها هستیم و آنها با سیاست ما آشنا هستند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/127861" target="_blank">📅 15:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127860">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
عراقچی: امنیت منطقه نمی‌تواند بر پایه نادیده گرفتن ایران شکل بگیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/127860" target="_blank">📅 15:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127859">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
نتانیاهو: ما به اهداف حزب‌الله در حومه جنوبی بیروت حمله کردیم و حملات علیه خودمان را تحمل نخواهیم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/127859" target="_blank">📅 15:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127858">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkx6vxj6S1IMyu5bP7gC4Ur2SVCW2fdgOyzxZ19sirkcAObpnTur2C9PsM9ho6Z_wCicnqtDf9GhuCIFjuO_VyHbm5GzN-IJgQefca6pnr9uWaf7tNpBq-fNXvoWEBxONWYnZMarH1pzD3JtvUdJHWGyEvbavyhu1lCN_0j5xm5_ymH3THOmxQtFngCiQroWqda09wP-lVfQCyj2--oVp2roOqhN-F9koXIPFagjtzHlBmM9Dv221OlxMPWxuflzXRX6tMbWJLMPlcRCQC8hTyyh3IhffkVXE0HrdF_79gGhw66Gw1IPE5ekV00kHKk0IkmUSgUWx32tXHCrdGxgjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت اکانت اسرائیل به فارسی !!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/127858" target="_blank">📅 15:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127857">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
خبرگزاری رسمی اسرائیل: حمله به حومه جنوبی بیروت توسط دو هواپیمای جنگی انجام شد که چهار موشک هدایت‌شونده شلیک کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/127857" target="_blank">📅 15:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127856">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJJHs2c3aQ5Q_0ut3hVggpbbRrPIF3LWZUf0DX7YvwuLfQnSPnaI37sVBndE88JBJkKVMGVvvxj_CRUWe5Y2ktnjJ_VMb6er0gKBPHstrvLWjZU-aZbtR1scUecfYjMp414-ocZbMyAa9weXafLKeUSLvKJXTpM9CykVyeWYE9d-Pm2_p9E9HumqRTTJw-1FNEQm1lwd5p1cv8PCBpmvAZiYfrGRpRHzj3Cmf5Ivba7T1AunsNye2Tqbk_OMxRR0JSsZzZfcOVWN6l72qun2YOD601e1gUkT8ST169NVjG-8vtZKwzoL5r8azkdebvQYHIRpFD39PJgE7o9W3TpdHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/ سخنگوی کمیسیون امنیت ملی:
نباید اشتباه محاسباتی کنیم
🔴
حتی اگر بخواهیم به توافق یا تفاهم برسیم، راه آن انضباط دادن به رژیم صهیونیستی است. اگر این سگ هار کنترل نشود، امضای تفاهم خشک نخواهد شد و پای ما را خواهد گاز گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/127856" target="_blank">📅 15:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127855">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
خبرنگار صداوسیما: تنگه هرمز طبق اعلام نهاد مدیریت آب‌راه خلیج فارس تا اطلاع بعدی همچنان مسدود است و هیچ کشتی خارجی حق ورود و خروج ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/127855" target="_blank">📅 15:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127854">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEEvyTxIC7TnbRjmMTD2XHGu11EG_RSYkXJ_iam3v2dvrf2zMHCoTOVFRUZSep4Q9aGfG8T5NfOoobcqHjbyglt6PDt_y-7Msu9iMtm7IC01cmQQSpo75jSM99MTlhoW4t1EUJXTZjJ4wg6cEZwSXTJofCWJwoUY6XmNDRdvSCM_wBqdDeLK1rzb6z2CUTA400TqvTPaJcpj6a2WFkL-NJDbqIQUE_QTtdvmx9eSzrIzred_h7xwKjX5eg5QNR1knnzYm3DPb0aZkt6XDUY2IKYDVecWjC8o-j34fBvcaKVXFcn35IElzqUdF_pdR0dDXLQk1I4QTlC3PcHFC33Jew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید(اکسیوس) : ایران همونطور که گفته بود، حمله به بیروت رو پاسخ میده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/127854" target="_blank">📅 15:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127853">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
خبرگزاری العربیه: قطری ها و پاکستانی ها فشار زیادی می‌آورند تا تشدید تنش رخ ندهد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/127853" target="_blank">📅 15:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127852">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
فوری/ منابع عبری: ارزیابی‌های کنونی در اسرائیل نشان می‌دهد که ایران تعادل را حفظ کرده و به حمله در حومه جنوبی بیروت پاسخ خواهد داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/127852" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127851">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
سخنگوی آتش نشانی تهران: دود مشاهده در قسمت شمالی شهر تهران، مربوط به حریق فضای سبز در محدوده ولنجک است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/127851" target="_blank">📅 14:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127850">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: هدف حمله هوایی در ضاحیه جنوبی، فرمانده ارشد در سیستم ارتباطات حزب‌الله بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/127850" target="_blank">📅 14:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127849">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8K-NqQWxc_OmrMZatO9JS2HU3wQZSi87CtSB6umTIpJQpq9cs5fz-8YFHkMD999MBhJ97FfUhZKr2UE7511Wj9XBmlAxMMd9EObo9PPZD-9iRl0kTjMtpMPBa1QyWzhnkJTMuwiwiv906NpAYP9hR7nGA5GrCYuxvf4_3w3-4D0RoR7LVIOsbj6MZg2dqbSOIn5S9cNmJtNM9a-YqNcDB2PsYMbEDMaEZAnkr1ygmB_Khap3DSkF0xVI_GvBcQxqZThasgLpLV-V1s-MwzNzy6qD26Epvp9sQKQCr-5Yi9iXTTqiF7h_uBc7vOee-d_0BmutJeEu05LtaLC1NTdWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل: مرکز فرماندهی حزب‌الله تو ضاحیه بیروت رو زدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/127849" target="_blank">📅 14:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127848">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
بیانیه نتانیاهو و کاتس: ارتش اسرائیل اهدافی متعلق به حزب‌الله در ضاحیه جنوبی را هدف حمله قرار داد
🔴
زیرساخت‌های حزب‌الله در ضاحیه جنوبی را با دقت هدف قرار دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/127848" target="_blank">📅 14:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127847">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
رسانه های اسرائیلی از اماده باش کامل ارتش اسرائیل برای حمله احتمالی ایران خبر می‌دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/127847" target="_blank">📅 14:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127846">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
شبکه ۱۴ اسرائیل : ما جشن تولد ترامپ رو امروز تو بیروت جشن گرفتیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/127846" target="_blank">📅 14:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127845">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
فوری / کانال 12 اسرائیل به نقل از یک مقام امنیتی: این بار، ما حتی پرتاب یک موشک از ایران به خاک اسرائیل را تحمل نخواهیم کرد.
🔴
اگر چنین اتفاقی بیفتد، اسرائیل آماده است تا یک حمله نظامی گسترده و خردکننده علیه زیرساخت‌های نظامی و اقتصادی ایران انجام دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/127845" target="_blank">📅 14:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127844">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69e99d5be0.mp4?token=JxEQDYqsuh5BO59-pYsSf3g84aeYvYl5Rm1MIgdBR8cSY8wezAVXMc8LEQW4h0FXnp3SuU_1mainSe1BCR8j7OGvSODaGYZPxVUEWKVuypyL5iNYMPEm0QEy2fgqv8UCVg8xFRkx6Vm6ua6N7-X5to3TKnV3u6M_7MDv0mZXk2GU64ZIiKoThZqIsDqf8n6uFtR0odjR_kiiSmoHTC16oVno-BGyZCSrQoch5fq1KJl8UB31t80q9b89C12RuB6rd4JemgL9Mpy9ZxAApy_aGT1SRY6pvveiq-oCpc0fdGULU5E5GF_UtDW_4uuUpQ_Ug-tTPZXxDpsdGDWhB77e2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69e99d5be0.mp4?token=JxEQDYqsuh5BO59-pYsSf3g84aeYvYl5Rm1MIgdBR8cSY8wezAVXMc8LEQW4h0FXnp3SuU_1mainSe1BCR8j7OGvSODaGYZPxVUEWKVuypyL5iNYMPEm0QEy2fgqv8UCVg8xFRkx6Vm6ua6N7-X5to3TKnV3u6M_7MDv0mZXk2GU64ZIiKoThZqIsDqf8n6uFtR0odjR_kiiSmoHTC16oVno-BGyZCSrQoch5fq1KJl8UB31t80q9b89C12RuB6rd4JemgL9Mpy9ZxAApy_aGT1SRY6pvveiq-oCpc0fdGULU5E5GF_UtDW_4uuUpQ_Ug-tTPZXxDpsdGDWhB77e2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل ویدیو‌یی از حمله‌ِ به ضاحیه بیروت منتشر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/127844" target="_blank">📅 14:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127843">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWT4nW7uf5FLg2408AqQuvLSqD5PdMkDv5wMpK6Cx0mHHMDW_BdFN_W3ZKQWR5QIynRB2S0K_ouQTbizK9mgvOCkmjsmeTWZEf-1G7o5FaE-noe8S1-ezWzEf2zp0t4RrnkQ37VAKEDWZ7m-q5W6YQ_JRT9Ds9FsPxnIPAzpWCyskSbGvRMWiSEXnmwjAiTXIZzqflh4SSdDtBmWJk69nm_9q6Uv1e_YVTbZ1ftpVd9KY8-1YuOuZgX8v8Qt_AITXCoAM25xLJy-l7B3f2y3rBbfDmnqvfpJbe_7eV92_QT_AyKmNy4KnA__20rtFyNYTDKgLgCxSMnCnT1_jtFP3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خسارات وارده به ضاحیه بعد از حمله اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/127843" target="_blank">📅 14:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127842">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
فوری / کانال ۱۲ اسرائیل: هدف در حمله به ضاحیه جنوبی نعیم قاسم بوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/127842" target="_blank">📅 14:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127841">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
فوری / کانال ۱۲ عبری: اهمیت این حمله در لبنان این است که ایران قبلاً تهدید کرده بود به هر حمله اسرائیل به بیروت پاسخ خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/127841" target="_blank">📅 14:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127840">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbQWRWWMgsKsEDFyA-T-7smcbewBACDDy_E7gxeexmNz2ko-Cnq6zFvXGOSsOgsKeQbfnpqfWt9sGpcyMPX3kqHfZfIwQPdm-p0l7B4aj0TFQwYQu-LUpd_d5hVGGAIdjkt62WVxAPmro1qL4ikvGVNTzY0mH9TGTjAOIYLoIFzMZH0Fjwd5Azxje0H6QpqUBpIFTOb36W0fVHuBMcjl6UXGWcvzRz9kj47-O1E6-m88NSzwjMvCn5DKIktYzH2B6tdlGiuYgmeBzBtG0GHFRjlH90w2oFgzPsTPyjy98r1FFzalHmQyYGpmbd6bZ8plsDGd5CcX7qqbNUiZplDWPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ضاحیه بیروت هم اکنون
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/127840" target="_blank">📅 14:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127839">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab3645c40.mp4?token=hED4U0yEVpqPt4g7LOyoXtJSjIigaEIn1JTSojU7JD4p2xELTWTHIuLuCCvSBMLKOUTAE5UMWtmstAxG1S8EWGVOuBhlJVK1-HnzcVpBpyr-ynnLW4RThvXKQhR9x4eKYBp0kCzi3K-1LUTbREiOfj15NlDmWBg0BXzuB75rD2i6rn_f7WgzuJ30wqekhqcG9ITbaWOBlmWyC0T-wjydCRedAxObMNM0E_gWHr3POJyufiiz0bfCQdz4I8aS7iKbf-9-x-LTiUM28gYfskb9A2IQkaNFSULmhAevS3JwYDcK2bWtn5AJIfL5uYhcf_Q3RuhD8coltpmqJMdftI0JTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab3645c40.mp4?token=hED4U0yEVpqPt4g7LOyoXtJSjIigaEIn1JTSojU7JD4p2xELTWTHIuLuCCvSBMLKOUTAE5UMWtmstAxG1S8EWGVOuBhlJVK1-HnzcVpBpyr-ynnLW4RThvXKQhR9x4eKYBp0kCzi3K-1LUTbREiOfj15NlDmWBg0BXzuB75rD2i6rn_f7WgzuJ30wqekhqcG9ITbaWOBlmWyC0T-wjydCRedAxObMNM0E_gWHr3POJyufiiz0bfCQdz4I8aS7iKbf-9-x-LTiUM28gYfskb9A2IQkaNFSULmhAevS3JwYDcK2bWtn5AJIfL5uYhcf_Q3RuhD8coltpmqJMdftI0JTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی از محل حمله اسرائیل به ضاحیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/127839" target="_blank">📅 14:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127838">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
فوووری/رادیو اسرائیل از آغاز حمله موشکی به بیروت خبر داد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/127838" target="_blank">📅 14:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127837">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eW_gkEqCHw9PY5oW-zyS1iZPJ6aRqSfwae9heVEKyoKHS210ZpKj-UQ2jtqWqQvGsVBXNgz6RdSyZ3S3cTlx_WHJYNMvqbvBua3ETUZvl4l4YnS18hUS8rk7ctx3Qq9JAJKQUBI-BKajkbvSJYJtshujA1Xo55pjK3GH6CK0AtQnucM8UDjUT8QeIn5S9ypyHdiip5MyQ7L2XMqsCrDl70UT_3WjHyxkM1ZQKPitGzUN86Fqew5cXmbPL_idXIsgDz1zG0iI3ZlTk5aAaWc_uYw9PVoNwg6aixUTQ3MPGzWnup6RVuAr1lDjc541iLnLHN2EVr8d9I7WxwiQILraXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوووری/رادیو اسرائیل از آغاز حمله موشکی به بیروت خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/127837" target="_blank">📅 14:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127836">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=IEs7gE67KIfJX7ckWlYMzitBJv6Bv5odGmVt6gz3oD3yw_Gfq_b6gIWYOA2k0Md0GOkcUSC9ixO_py9edJvsar13atSnrJ32LI_qT1vSEzbTyshyORvFqMHF_N4ijq36DLfdGkuA_ODuVrsg-I4wC0NOMnbJlgWE4owzdRKSkRPWjm2F8vJC4d7t9w5P3dKOlZbtvfPyjA3tDXr9lQ8_T0_PtEytnlToh7w16TR2L1zZBEufbfGvMjCoYdrSV6LIy0IBwovslsgkTan231v0-I6fe8REk_-onIcV7qJHW-cPxjHCfKw41TDkjAUo-FfsuayXz6VHcIrsvJYwp91gTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=IEs7gE67KIfJX7ckWlYMzitBJv6Bv5odGmVt6gz3oD3yw_Gfq_b6gIWYOA2k0Md0GOkcUSC9ixO_py9edJvsar13atSnrJ32LI_qT1vSEzbTyshyORvFqMHF_N4ijq36DLfdGkuA_ODuVrsg-I4wC0NOMnbJlgWE4owzdRKSkRPWjm2F8vJC4d7t9w5P3dKOlZbtvfPyjA3tDXr9lQ8_T0_PtEytnlToh7w16TR2L1zZBEufbfGvMjCoYdrSV6LIy0IBwovslsgkTan231v0-I6fe8REk_-onIcV7qJHW-cPxjHCfKw41TDkjAUo-FfsuayXz6VHcIrsvJYwp91gTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان تو مراسم امین ایران : رسول خدا و اصحابش، تو جنگ رفتن لت و پار شدن و شهید شدن و برگشتن
😐
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/127836" target="_blank">📅 13:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127835">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
مقام ارشد ایرانی : طبق پیش‌نویس توافق، آمریکا قراره حدود ۲۵ میلیارد دلار از دارایی‌های بلوکه‌شده ایران رو آزاد کنه؛
🔴
از جمله انتقال مستقیم پول و همکاری در سطح منطقه‌ای
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/127835" target="_blank">📅 13:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127834">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
العربی الجدید : ایران هنوز تأیید نهایی خود را برای یادداشت تفاهم اعلام نکرده است.
🔴
به گفته یک منبع آگاه ایرانی، احتمال امضای توافق در روز یکشنبه منتفی است و بررسی‌ها در داخل ایران ادامه دارد؛ هرچند ممکن است تهران امروز نظر نهایی خود را اعلام کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/127834" target="_blank">📅 13:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127833">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAWhs_2UQ-W4oXWyMvJzfgJjIRWTC2BN6tVlmyoCKIVqxuHXnte8mA96_irbVwv9kkPcsKMg8HOt4w9efmmi5AbojS9Z3KWWOhIHjcEsU-Yi8fhSpud8mHXJGrQ7FGdTy4E0k4lKQZQCn08wnPluebpARa_pInp56jDpa1nT-nUbcfqlITT7WV9OWQo6lbM6TUemDbaNu5AC575vjl9SEerWzYGeVu340GZs-3oltLR1eOjJDOHPpA8gBdAdeEkE4j9sVWFKI5i3sFwPT3j3suyJrI-V_-DEBb7IWAHLgnwLG6ayz0DXZQ17ByS_zCCeJ3T89_J0Hu7QOyLzFAYbyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ناو هواپیمابر فرانسوی «شارل دوگل» پس از پایان دوره مأموریت ادعایی خود در مدیترانه شرقی و دریای عمان، در حال بازگشت به پایگاه نظامی «تولون» در فرانسه است.
🔴
بازگشت ناو «شارل دوگل» به فرانسه، در حالی صورت می‌گیرد که پیش‌تر گمانه‌زنی‌هایی درباره ارتباط این تحرکات نظامی با فرآیندهای دیپلماتیک مطرح شده بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/127833" target="_blank">📅 13:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127832">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‌
👈
انور قرقاش، مشاور دیپلماتیک رئیس‌جمهور امارات متحده عربی: ما هرگز طرفدار جنگ نبوده‌ایم و همچنان طرفدار صلح و ثبات خواهیم ماند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/127832" target="_blank">📅 13:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127831">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
رویترز به نقل از مقام ارشد ایرانی : طبق پیش‌نویس توافق با آمریکا، ایران قبول کرده دیگه دنبال ساخت یا گرفتن سلاح هسته‌ای نره
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/127831" target="_blank">📅 13:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127830">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
رویترز به نقل از مقام ارشد ایرانی : طبق پیش‌نویس توافق با آمریکا، ایران قبول کرده دیگه دنبال ساخت یا گرفتن سلاح هسته‌ای نره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/127830" target="_blank">📅 13:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127829">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eeb7fe4ee.mp4?token=HoHwqf4GriS-zRk-oQUSN2WY_KNlsdRhVEyvRtgPqM_CBKLQMIHDY-ANwEoEVFM6xw5YfdS7IRmiYQmIipaBPAtUkFi_b-1crY4YjhW8pKrHFDZVmdU3qCVwBpn1HVSuAq0LmI-XtoWiysiLqyS2bX87Fc-3BKFhzKTAQ8Yzcb2vunRdo4pUYVxQ0sI0VdiyJd30r5-MechkhmdXFXYBoYEWBlTCh-frnmvmJ064FJ6CNEtsMiLj04bVAnSFSybpM-epq-fE9aD5bPqxyY0HjZVUAn2HmQ2vNoLfODhJnLFYRamBQE9zTNDikEvb0NGpI_7_NeJQszQaMqpZ8ItygQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eeb7fe4ee.mp4?token=HoHwqf4GriS-zRk-oQUSN2WY_KNlsdRhVEyvRtgPqM_CBKLQMIHDY-ANwEoEVFM6xw5YfdS7IRmiYQmIipaBPAtUkFi_b-1crY4YjhW8pKrHFDZVmdU3qCVwBpn1HVSuAq0LmI-XtoWiysiLqyS2bX87Fc-3BKFhzKTAQ8Yzcb2vunRdo4pUYVxQ0sI0VdiyJd30r5-MechkhmdXFXYBoYEWBlTCh-frnmvmJ064FJ6CNEtsMiLj04bVAnSFSybpM-epq-fE9aD5bPqxyY0HjZVUAn2HmQ2vNoLfODhJnLFYRamBQE9zTNDikEvb0NGpI_7_NeJQszQaMqpZ8ItygQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صدا سیما: پاکستانی‌ها برای میانجی‌گری به ایران نمی‌آیند، بلکه مرتب پیام تهدید و‌ ترور می‌آورند
!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/127829" target="_blank">📅 13:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127827">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hFbUzisM3rspx6KVrBM9UOfuK4xk21seAarxGKt8j8k4YnC8SVj5De_Vz3JgzzhTGEpXzjnBH5uPmclAaXVc4U_19ejVw5Pmnlv4tP-3lbKa5i-bl6e5g1OH2TllSaRUZLKyrwO5Mf88e_FRw_-XLb0aVODrqFpoihFETRrzLgdlQS35dV57-oQjIMp-9uVW_LrRv4muzTxxdV7FufWNjiE6pneNxBWTpm968S_hna1IW5-4NcVgO7xYU4qVuH2uzVJdxLLAAZuxVZIICnU9CL9jLvyaEzCcHjfs_C2cji7v44btl7Wrxu0SA0bFahL2AzrlG2Fh7lQ1hvj_EykAbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iXE13sSTfAiOJjBPaPjm22PTLnA3uJ3lRiAf1vlaVPsamcsG7EdiKZfhnkh3CXPz99hQO0xUQeC6invNwKj-e-6J8H53eUbOV48ZcxX0CKW6PZIg5eOxMNg3cY98YwKEVTIEq-vPFaN410X0_798r_52V4d0fPYG4AztNNvukuz4G5O041bWLkgRFdOu1O1JV6ncx1oNYKYUO05CvcYddLJ6WZO9QFhWJR1AMvQ_unqKot8GTjGbx9Cder7ef1f1feKzMFServkMYhFc3uI3tf-zA6AnNzJ5Tyez_CU-DpqPSS6a8Clu-_KbnZGdupvc0khOULh8orKRhPAlsN511Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
صندوق سرمایه گذاری قطر اعلام کرده بعد از گلی که دیروز بوعلام خوخی در دقیقه‌ ۹۵ به سوئیس زد، ۳میلیون دلار به همراه یه رولز‌ رویس فانتوم آخرین مدل به ارزش ۵۵۰ هزار دلار پاداش خواهد گرفت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/127827" target="_blank">📅 13:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127826">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
شرکت نفت و گاز پارس: چاه جدید فاز ۱۱ پارس جنوبی وارد چرخه تولید پایدار گاز شد
🔴
افزایش تولید از فاز ۱۱، در بالا رفتن سهم برداشت ایران از این میدان عظیم گازی اهمیت ویژه‌ای دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/127826" target="_blank">📅 13:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127825">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
جزئیات متن تفاهم ایران و آمریکا از زبان مشاور رئیس تیم مذاکره‌کننده
🔴
مهدی محمدی، مشاور راهبردی رئیس تیم مذاکره‌کننده جزئیاتی از متن یادداشت تفاهم ایران و آمریکا را تشریح کرد که به شرح زیر است:
🔴
۱. توقف درگیری‌ها و تضمین‌های امنیتی
🔴
در گام نخست، توقف کامل عملیات نظامی علیه ایران و لبنان و جلوگیری از هرگونه اقدام نظامی جدید در دستور کار قرار دارد. همچنین طرف آمریکایی باید تضمین‌های لازم را برای جلوگیری از تکرار تنش‌ها ارائه کند.
🔴
۲. آزادسازی دارایی‌ها
🔴
براساس چارچوب مورد بحث، بخشی از دارایی‌های بلوکه‌شده ایران در ابتدای اجرای توافق آزاد خواهد شد و همزمان روند تعلیق برخی محدودیت‌ها و تحریم‌های اقتصادی آغاز می‌شود تا امکان افزایش مبادلات اقتصادی و فروش نفت فراهم شود.
🔴
۳. رفع محدودیت‌های دریایی و تجاری
🔴
یکی از محورهای اصلی توافق، تسهیل تردد کشتی‌های تجاری ایران و کاهش محدودیت‌های دریایی است. هدف این بخش، بازگشت تجارت دریایی ایران به شرایط عادی و رفع موانع موجود در مسیر حمل‌ونقل بین‌المللی عنوان شده است.
🔴
۴. مذاکرات هسته‌ای در مرحله بعد
🔴
در متن مورد مذاکره، مسائل هسته‌ای در مرحلۀ نخست توافق قرار ندارد. براساس این چارچوب، ابتدا باید تعهدات اولیه طرف مقابل اجرا و راستی‌آزمایی شود و سپس گفت‌وگوها درباره موضوعات هسته‌ای وارد مراحل بعدی شود.
🔴
۵. لغو تحریم‌ها و بازسازی خسارت‌ها
🔴
در مرحلۀ نهایی، لغو تحریم‌های اولیه و ثانویه آمریکا و همچنین پیش‌بینی سازوکارهایی برای جبران و بازسازی خسارت‌های ناشی از جنگ و فشارهای اقتصادی مورد توجه قرار گرفته است. این بخش از مهم‌ترین مطالبات ایران در روند مذاکرات به‌شمار می‌رود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/127825" target="_blank">📅 13:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127824">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
نیویورک‌ تایمز: تهران معتقد است ایالات متحده آمادگی ورود به یک جنگ گسترده دیگر را ندارد و دونالد ترامپ ترجیح می‌دهد به توافقی برسد که تنش‌ها را کاهش داده و ثبات را به بازارهای انرژی جهانی بازگرداند. این موضوع به ایران فضای بیشتری برای مانور می‌دهد و احساس نیاز آن به دادن امتیازات بزرگ را کاهش می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/127824" target="_blank">📅 13:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127823">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
آی۲۴نیوز عبری: امروز ونس و قالیباف طی جلسه مجازی تفاهم نامه را امضا خواهند کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/127823" target="_blank">📅 13:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127822">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
نیویورک تایمز: جنگی که آمریکا و اسرائیل طی ماه‌های گذشته علیه ایران انجام دادند، به اهداف راهبردی اعلام‌شده در آغاز آن دست نیافته و در عوض واقعیت سیاسی و امنیتی جدیدی ایجاد کرده است که ایران را به کشوری مقاوم‌تر و آماده‌تر برای پذیرش ریسک تبدیل کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/127822" target="_blank">📅 13:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127821">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
ایوو دالدر، سفیر پیشین آمریکا در ناتو معتقد است که ایالات متحده در شرایطی که تمایلی به ورود به رویارویی مستقیم با روسیه ندارد، به فاصله گرفتن از اروپا ادامه خواهد داد.
🔴
به اعتقاد وی، آمریکا آگاهانه و فعالانه در حال جست‌وجوی راه‌هایی برای ایجاد یک نظام امنیتی مستقل از اروپا است.
🔴
دالدر افزود، ایالات متحده از بیم واکنش احتمالی روسیه، نه تنها استقرار سامانه‌های تسلیحاتی دوربرد و دقیق را در خاک کشورهای اروپایی متوقف کرده، بلکه متحدان اروپایی خود را نیز از تجهیز به چنین سامانه‌هایی بازمی‌دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/127821" target="_blank">📅 12:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127820">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
دو پهپاد حزب‌الله امروز صبح به یک منطقه نظامی در شمال اسرائیل نزدیک مرز لبنان حمله کردند، طبق اعلام ارتش اسرائیل.
🔴
ارتش اعلام کرد که در این حادثه هیچ زخمی گزارش نشده است و موضوع همچنان در حال بررسی است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/127820" target="_blank">📅 12:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127819">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t30KPqxoC--gNUq4SNExYrkAp08-7VXTa6DHcyzcYeVa5a08jSQdA6rf-oijJb15L4PXH3Nvt46QjSnBr7_0hzV_7ZWPH6odsTW_dELIa1w0s6DgBnaX4R3J5MfWCfSwZicY8pIn_yna6FSKZrfDUvH04eav6Azp10GcwFa5qVzfuMLod6mkLUOSNbxDIHmIxv8-YDdUgIcWtDoLhzgAgfZG32IUhTTXsqAkwfOcMEt8rCQiiiY2g7vC2BXR_L2IoRr5ALKJkvsrPJW11VyyNsVDVWGm7nm6oAfEULddclNREWk9WTNOavtjQcPGRsJumqSnZFonv8xND8Q73dnYng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مانوک خدابخشیان - تحلیلگر سیاسی چندسال پیش، قبلِ درگذشت :
- اورانیوم رو میدن توافق میشه - بازی تازه شروع میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/127819" target="_blank">📅 12:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127818">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
کانال ۱۲ تلویزیون اسرائیل: توافق آمریکا با ایران، اسرائیل را به حاشیه رانده و موضع تهران را تقویت می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/127818" target="_blank">📅 12:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127817">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKf7hbHjLxy5AcOp1ds_bP4r7nmTxT2AJT_lVHW-dYqla1a1anY1dNqwrXgamtaHf5MGNN4BDGUh-fSd1HYNFmyfhaXuwgYbvD3zPgeQU9tMrXiD4WwU0f_K4YO_CcFT_uuDwt_UgPEaCgyqFCwRwx_AbqW9M-xbr6Jy4TMar-RJXKVUsoqLZUZ6u5yZY2Ijm50eBpmmtzeMRR5p-H33KimSowgqsx5JYOxp_7HDsmbAVmwPaMMZpuNC4-4KXQVAuDskcd1HFIxGpq7ulLc-AiOs7OuWhPed5Kckq7VZFa5rO_PMmnG7n9ehijAamX8JbJvdDY75_6DOCU7vgPiTtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس در پایان معاملات امروز با جهش ۱۲۳ هزار واحدی به ۴ میلیون و ۸۱۹ هزار واحد رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/127817" target="_blank">📅 12:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127816">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
یائير لاپید، رهبر اپوزیسیون اسرائیل به روزنامه بریتانیایی تایمز : اسرائیلی‌ها در وضعیتی از یأس و بدبینی غیرقابل تحمل زندگی می‌کنند.
🔴
نگرانی در اسرائیل به دلیل عدم تحقق اهداف اعلام‌شده جنگ حاکم است.
🔴
روابط ما با ایالات متحده به‌شدت آسیب دیده و دولت آینده باید این خسارت را ترمیم کند.
🔴
ما از زمان ۷ اکتبر تاکنون این میزان یأس و بدبینی را در میان اسرائیلی‌ها مشاهده نکرده‌ایم؛ سطح ناامیدی به حدی رسیده که قابل تحمل نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/127816" target="_blank">📅 12:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127815">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار ناشی از مهمات عمل‌نکرده در تبریز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/127815" target="_blank">📅 12:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127814">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1101d09a88.mp4?token=p0ON-Yuq935EcvRPcJPlR5ho5JprCP4MwjRsalUc_DQixSN8n1byqNuyLH4iB2zbiZARxI1XS6hls-eSTTqz3EtZtSujD_W0XsL0rluO-TJRGs_nYV80f4M7OWCdeZHSfYvkzweg5Nwn9anggz2fIwzdMkIbCf_6tm2OxKQZD35zT2qbqgZVFppJmuJ8A4QuE17u3o1Y6e4yXAkRsdd_ZzMBmsNIqUVtt-KnfSTT7_u3rQWNr-8NjzXYKCessZevrOR0cSiqwTPp5T-XBAdvGXllcP_k9c0dpGr3YYN294yR9sFif_8BS2pPD_pjTxlHf-2lqhJUZ1c_BVJ6pXp4hjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1101d09a88.mp4?token=p0ON-Yuq935EcvRPcJPlR5ho5JprCP4MwjRsalUc_DQixSN8n1byqNuyLH4iB2zbiZARxI1XS6hls-eSTTqz3EtZtSujD_W0XsL0rluO-TJRGs_nYV80f4M7OWCdeZHSfYvkzweg5Nwn9anggz2fIwzdMkIbCf_6tm2OxKQZD35zT2qbqgZVFppJmuJ8A4QuE17u3o1Y6e4yXAkRsdd_ZzMBmsNIqUVtt-KnfSTT7_u3rQWNr-8NjzXYKCessZevrOR0cSiqwTPp5T-XBAdvGXllcP_k9c0dpGr3YYN294yR9sFif_8BS2pPD_pjTxlHf-2lqhJUZ1c_BVJ6pXp4hjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دو پهپاد حزب‌الله امروز صبح به یک منطقه نظامی در شمال اسرائیل نزدیک مرز لبنان حمله کردند، طبق اعلام ارتش اسرائیل.
🔴
ارتش اعلام کرد که در این حادثه هیچ زخمی گزارش نشده است و موضوع همچنان در حال بررسی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/127814" target="_blank">📅 12:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127813">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
داداستانِ استان اردبیل :  یه تالار تو اردبیل به خاطر برگزاری عروسی مختلط پلمب شد و صاحبش هم بازداشت شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/127813" target="_blank">📅 12:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127812">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
عصر ایران: کسانی که با مذاکره مخالف‌اند و از جنگ دفاع می‌کنند حاضرند لباس رزم بپوشند و نه در جنوب لبنان با اسرائیل ، بلکه در همین جنوب ایران خودمان با دشمن بجنگند؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/127812" target="_blank">📅 12:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127811">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69fb367f9b.mp4?token=Hrqe6VpEjIBylHag_FmzlosYuR2fe3HAlhJlIl_gXCkeRNwnkyvFcHk7eH2Jo0YEJTLCezAK4FYbqhIoag4h005NRKsndRcEeggjqUQq5r_sjz-AEFQyF4cioCqn-L6vCehktnylFAsa20Vh7nxoYvOWQHxHoR7_TSaTgRl3aEALOwCie2uhuueZoml1mKNmD6My5kJo5eOwY5y46LfaDvto9d4Mk8XWJjOVQvy8S6PtqAGHvLaBm_RylI7k0miTWINiCSfo-GFfestPkKUubGR9o0oWC16WJmhwpSVe0DHsEU3aMostDT9Bhjndw3YYsEUkOetrZbCBKVqRCBcg8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69fb367f9b.mp4?token=Hrqe6VpEjIBylHag_FmzlosYuR2fe3HAlhJlIl_gXCkeRNwnkyvFcHk7eH2Jo0YEJTLCezAK4FYbqhIoag4h005NRKsndRcEeggjqUQq5r_sjz-AEFQyF4cioCqn-L6vCehktnylFAsa20Vh7nxoYvOWQHxHoR7_TSaTgRl3aEALOwCie2uhuueZoml1mKNmD6My5kJo5eOwY5y46LfaDvto9d4Mk8XWJjOVQvy8S6PtqAGHvLaBm_RylI7k0miTWINiCSfo-GFfestPkKUubGR9o0oWC16WJmhwpSVe0DHsEU3aMostDT9Bhjndw3YYsEUkOetrZbCBKVqRCBcg8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قابل توجه جبهه پایداری
🙂
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/127811" target="_blank">📅 12:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127810">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FGblJBS7RUVv0NCTnci4auumSk1BGNy5T30RLzZ1-EvjcLeSVE_idbLC2lQZ_xLMsc9Td8RTsBZksb91OA2UbxMbshDd7sTvwcroqRvS5G7zGFUIIdNCFijCUNCuftqb27nmlttGyUDJS3Yog1WqnvmsMF73XoAmK74xE0UU7DVIhF5M5vbWb4PX4ePykWHARsrodabp81DWr8jr_moo1O9YE8cgSpBBtkXVFuHxeA6vkNjF5GAjQIo-8lf5XiYe2mHq-nFviVr8CHZ_I9Me84Hd9puXL3rnFaZKQuzLB99yVhVH7HjQQmJKIAhAjgHyrIIopMOiIBJHv8qmJMtFZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کودتای تندروها علیه مجتبی
‼️
🔴
جلیل محبی: اگر رهبر هم قبول کنه ما قبول نمیکنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/127810" target="_blank">📅 12:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127806">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f47e6bdbbb.mp4?token=ZJj-LALVngoaFplAORmRx-U_WIqmPweDfrayYSYhhxxAd9MfvLeyWzaM3nk-XWvhAuB4pCHmwc1xP3vLQFzB7mT3xptiikds2Xc48NnrMSAM6JmaR09bL_YywCh2_uzHemCOHLcnoVqUvw1V7l3Aw5y2fuH1-t5SNudQNvgp7hF_3bzBRrha1ibJqZQOtZWhQnhP0wbj5HFR8fWRMY_u5qWbkegzVF4r0FNQbJ6QJ-EzC8m4E_xv6nT-BaXMKpZ5FcX9uVSUUCmJ_TiUgmms4aNu5tTe2NTYp-RoxMshnfBO6jTDS5NFr_wVeiaIyWxpNp1KP-2qII4LwQJDzP7cYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f47e6bdbbb.mp4?token=ZJj-LALVngoaFplAORmRx-U_WIqmPweDfrayYSYhhxxAd9MfvLeyWzaM3nk-XWvhAuB4pCHmwc1xP3vLQFzB7mT3xptiikds2Xc48NnrMSAM6JmaR09bL_YywCh2_uzHemCOHLcnoVqUvw1V7l3Aw5y2fuH1-t5SNudQNvgp7hF_3bzBRrha1ibJqZQOtZWhQnhP0wbj5HFR8fWRMY_u5qWbkegzVF4r0FNQbJ6QJ-EzC8m4E_xv6nT-BaXMKpZ5FcX9uVSUUCmJ_TiUgmms4aNu5tTe2NTYp-RoxMshnfBO6jTDS5NFr_wVeiaIyWxpNp1KP-2qII4LwQJDzP7cYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اوکراین تأسیسات نفتی
روسیه
رو هدف قرار داد
🔴
حملهِ پهپادی به یه مخزن بزرگ نفت، تو یاروسلا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/127806" target="_blank">📅 12:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127805">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
آخرین قیمت دلار: ۱۶۹.۵۲۰ تومان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/127805" target="_blank">📅 12:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127804">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
نخست وزیر انگلیس کیر استارمر: صبح امروز دستور حمله به یک نفتکش ناوگان سایه روسیه که قصد عبور از تنگه مانش را داشت، صادر کردم
🔴
این عملیات موفقیت‌آمیز ضربه دیگری به روسیه وارد می‌کند و به کسانی که به جنگ اوکراین دامن می‌زنند یادآوری می‌کند که ما اجازه پنهان شدن آنها را نخواهیم داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/127804" target="_blank">📅 12:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127803">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
بلومبرگ: ایران احتمالاً در طول آتش‌بس سلاح‌های پیشرفته روسی را به ذخایر خود اضافه کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/127803" target="_blank">📅 11:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127802">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3fd105e87.mp4?token=pEKsDdjt_76Eab0uB9RCKzNgOlGKIws79lcEAV8f-AGf8dsUNJOLSkZue7TOJKwyYCAHK8KRxvrvl-OHu6HC143DluZB-zDYc_ntnmJW-5VUWlFWCuSMKV4XsbfSbILdgTDuDfHY47rGBAXwOll9n_tDQzvL3AsSu3s_z2VIqR31FL94Ako1o2KMbUKgM6CPiC14tsJCdOlTgCsf9MYyIe3yKU26ZxISLY051L3UC7zSGTIpQS_IQuWux2GD79EXp4Q9jee2AMnwTcX4udMqePaO92TyFyuxrNxbcvBR2S3zNn3MiJnfQFzqzu1BIHONSk-spfXjkiW3kv0t7E-Wyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3fd105e87.mp4?token=pEKsDdjt_76Eab0uB9RCKzNgOlGKIws79lcEAV8f-AGf8dsUNJOLSkZue7TOJKwyYCAHK8KRxvrvl-OHu6HC143DluZB-zDYc_ntnmJW-5VUWlFWCuSMKV4XsbfSbILdgTDuDfHY47rGBAXwOll9n_tDQzvL3AsSu3s_z2VIqR31FL94Ako1o2KMbUKgM6CPiC14tsJCdOlTgCsf9MYyIe3yKU26ZxISLY051L3UC7zSGTIpQS_IQuWux2GD79EXp4Q9jee2AMnwTcX4udMqePaO92TyFyuxrNxbcvBR2S3zNn3MiJnfQFzqzu1BIHONSk-spfXjkiW3kv0t7E-Wyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترافیک تنگه هرمز نشان دهنده عبور کم تعداد کشتی ها از مسیر جنوبی تنگه مطابق مسیر آمریکا
🔴
نکته قابل توجه گشت زنی دو شناور نظامی آمریکایی در تنگه هرمز ، البته نوع این شناورها مشخص نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/127802" target="_blank">📅 11:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127801">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6-JJcU7KWd6KTYDFz1o1rzT8kdz3MrWI7Jx6KdUcnHoqZTo5KQjIRf77u-TZAd382ZT_Qzf6PBJNtPbPKckxuM5ECCJ8-EMCxMnnvibRYoX7ZWW0o_rSdPlyT0sGYRue3inM5b4Dcj0p1ALdQHawNeLA0xvyS69tg3AicMWBCr75yc6lioBHr2mmo76YnMbfkA4OvkCHaIhOApE4oJf4cUjZnwW-Nq9PatNWdN3AdTCJ5AplaSCYjtPMP2QjYtDADn3AKPdSqwGzCF5vTA5G1Uf-Gba6XFYBeCIWT1CqBPojFHxK1Wml5Rw127-r4Ruse_M8nunaKTWznRBsEvR6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ امروز ۸۰ ساله می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/127801" target="_blank">📅 11:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127800">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8WlNmP5uiSlTmFuMcQY82aErgWhlwufgCHGoyGhVa1T10XS_BWyg2Uiz-4SidXO7T49rwbOQItqxAu9AFM5wWS0V0W3CYBUZ27t8w8SgpeCMmprnJP9x_-wZBxvyP1wrCyo3SgaWZ7N_OMyVS1jU0ySZTIcMONqtRJg3KlzrDyn0gqB7719VIfNVNlzRSwz8jfIsmhqVsEZEaYqxOzd-HQ_r6GNwEsCadIMO-eQ6TniF9T6S7UwejTD-Vw3-07OOGir1Hxq4PpmXWTjfdectGfFHa6Pr6e82j1Atp2HHQ2H72AgEd0ewMYkCI9BRy84VFOR2LVcMml4LivD8ByuHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایندیپندنت
:
ذخایر نفت آمریکا به پایین‌ترین سطح در بیش از ۴۰ سال اخیر رسیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/127800" target="_blank">📅 11:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127799">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
مشکل خدمات بانک‌های تجارت و صادرات رفع شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/127799" target="_blank">📅 11:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127796">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IXif8_hhZxUtDFyDliBov9hY1SPcZAsAYKZbTOJAQxW4yE7wdOvRN0lUUzBWfHRlNYKeVdxU7IA3-gHs5RsFVHzVyD4ilKvnhMsk1YV6DZC97s4l2quPmzRSbKrwFkdGAkuF5t8SL4AmKuAbj4JchydypHa5sQ3v1J8Idqsgz1INRMhIJGeEFEcrDlzNpRefKi3ONGnmMAHzGObjFessMx7r-s-A2EB4cMqzMB1B6nWn4XAglLFLLXB-aGyLh8r16NDd2DNnP_MYnqYPBmPRFFB3xEfjRSHGbGlYRNf0mpcm9vYtUMnO8Ws8GNLZ3U06aVLis-w7wkiBTGgY_viBwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FL6WJV5C7XSID0Fu1W3yTrJeFF4qJHR_Lry_NOo2JrT5euMsABCvq4NlbKeAPrGyNSh_8LakMu1YdDLzgJ0zYHHCIkFBbMn2aXfUzvicHDI8T7TTKQAp_C30qo0kmUZGtXmQWlDlluoayr2n_mZEsqUVs7L03ayH0m5sxpg6Dmx665DSrDNH4lKKBQdTQ3Y8ZcxGeoHWgflIgsfCBL0ebePdB8vi1nCohP89e0RnFWZh60Ft_k0EngnrLVrWnMU1tzXsq1InhqrzSX1kAKoyMH9lB1j4J5hisZiUPYcZm-9MWH5nmIWB5XX6c-DlQUQW_YmdL_FOD4hu_VtupcGtBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86af934eb1.mp4?token=eCRbepeXGxyRxBYE05gB654RCgbgeFvtcP55WSJCDtzOp3nyN_UE0mrEqeNJeIk1s3vwCUO1wqBgP0BYHA8222LEBfIdpinbohS10M8WxnXz6Oj_JmCTPwOzoj7nhIS7clj5gcRVZOLY0awUjYdzLsmtY4J9ldTnEJp9fcUyBArxE520H8KYTop6Zjek2m2z69GD1EDB9D02M1xUFJRS9TNw71WmWGMFk6c1YfcDMw3gNTgp5q3nCFWRvSZWqGEiOdGAwe__jq9PkWDL6Pj5HSATcNr-0RHFcsgarmYAfVNH2j2CDxfl7_B9aET0Xpf_7UtdRBvVBDz0MMn11A4NIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86af934eb1.mp4?token=eCRbepeXGxyRxBYE05gB654RCgbgeFvtcP55WSJCDtzOp3nyN_UE0mrEqeNJeIk1s3vwCUO1wqBgP0BYHA8222LEBfIdpinbohS10M8WxnXz6Oj_JmCTPwOzoj7nhIS7clj5gcRVZOLY0awUjYdzLsmtY4J9ldTnEJp9fcUyBArxE520H8KYTop6Zjek2m2z69GD1EDB9D02M1xUFJRS9TNw71WmWGMFk6c1YfcDMw3gNTgp5q3nCFWRvSZWqGEiOdGAwe__jq9PkWDL6Pj5HSATcNr-0RHFcsgarmYAfVNH2j2CDxfl7_B9aET0Xpf_7UtdRBvVBDz0MMn11A4NIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملهِ به لُبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/127796" target="_blank">📅 11:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127795">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
منابع العربیه: قالیباف و ‌ ونس توافق صلح ایران و آمریکا را آنلاین امضا می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/127795" target="_blank">📅 11:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127794">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
وزارت امور خارجه قطر: نخست وزیر و وزیر امور خارجه کویت ابراز امیدواری کردند که واشنگتن و تهران به زودی توافق را امضا کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/127794" target="_blank">📅 11:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127793">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
خبرگزاری فارس : جمهوری اسلامی هنوز تصمیم نهایی خودشو درباره تفاهم‌نامه، اعلام نکرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/127793" target="_blank">📅 11:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127792">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
ایهود باراک، نخست وزیر اسبق اسرائیل:
توافقی که به‌زودی میان ایالات متحده و ایران امضا خواهد شد را می‌توان در یک کلمه توصیف کرد: بد. و در دو کلمه: بسیار بد. و اسرائیل بهای غرور و کوربینی نتانیاهو را می‌پردازد، و حتی بهای مانورهایی را که او تلاش کرد علیه ترامپ انجام دهد.
🔴
ایران قوی‌تر از قبل بیرون آمده است؛ در مقابل، اسرائیل پس از شوک هفتم اکتبر دستاوردهایی کسب کرده است، اما ضعیف‌تر شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/127792" target="_blank">📅 11:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127791">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
رویترز به نقل از یک منبع آگاه: تیم مذاکره‌کننده قطری صبح امروز، به عنوان بخشی از تلاش‌ها برای دستیابی به توافقی برای پایان دادن به جنگ، به تهران سفر کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/127791" target="_blank">📅 10:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127790">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkmH9RM7AqVzTu1jXeY5p_6iyYwkG0Sx5GfhJCSDrFPO5O1PnS58Nwpn77C8uN0ON18pODtyTjqRT_yqIKTI5FsD28Djsk-1ebKKgB6bL_QpM11fUiW-Xblb9t2OVxxSBeJ4gJdz7Ox9QucYcBDiT_JJ8Smk8eajk8GLspK-wVktzGGO97hRg8HVCToUXqTxHR1xbaz1mZPoS5Ds4-C4n5ToZVl8xqIX0znrN-OEQINOKgle7T-nksuoelwu93Gs6TNHylglqT68fc-fWzbbDWmI5EcntoSNqpnHnYCbnxSbcFC4eDomXqGISdxnLESGPb1VpU02-XN_2zJXjICNgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کامران غضنفری نماینده مجلس پس از تهدید مسعود پزشکیان به استیضاح: آقای عراقچی غلط کردی دور دوم برای مذاکرات تعیین کردی!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/127790" target="_blank">📅 10:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127789">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
سی‌ان‌ان: مذاکره‌کنندگان قطری برای نهایی کردن تفاهم راهی تهران شده‌اند
🔴
شبکه آمریکایی به نقل از یک منبع مدعی شد که مذاکره‌کنندگان قطری صبح امروز در هماهنگی با ایالات متحده به سوی تهران پرواز کرده‌اند تا به تسهیل روند نهایی‌سازی توافق (یادداشت‌تفاهم) بین ایران و آمریکا کمک کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/127789" target="_blank">📅 10:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127788">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
العربیه: امروز نشست مجازی میان هیئت‌های آمریکا و ایران برای امضای توافق صلح برگزار می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/127788" target="_blank">📅 10:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127787">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
الحدث: پس از امضای توافق، محاصره بنادر ایران برداشته خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/127787" target="_blank">📅 10:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127786">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
الحدث:یک نشست مجازی میان هیئت‌های آمریکا و ایران با حضور میانجی‌گران پاکستانی و قطری برگزار خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/127786" target="_blank">📅 10:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127785">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
اسموتریچ، وزیر دارایی اسرائیل: به ازای هر حمله‌ از لبنان ۱۰ ساختمان در ضاحیه باید تخریب شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/127785" target="_blank">📅 10:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127784">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
وزارت دفاع انگلیس اعلام کرد که نیروهای انگلیسی صبح امروز در کانال (احتمالاً کانال مانش) به یک نفتکش متعلق به «ناوگان سایه» حمله کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/127784" target="_blank">📅 10:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127783">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
گروسی :نظارت و راستی‌آزمایی آژانس در هرگونه توافق هسته‌ای احتمالی ایران و آژانس نقش محوری خواهد داشت و این نهاد با هماهنگی شورای حکام برای آن آمادگی دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/127783" target="_blank">📅 09:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127782">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
الجزیره: ایران هنوز تصمیم نهایی خود درباره تفاهم‌نامه را اعلام نکرده
🔴
می‌توان انتظار داشت که توافق امروز نهایی شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/127782" target="_blank">📅 09:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127781">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/247968d991.mp4?token=OxjzbqNdh5j6R7sP3JhB6Au8P7DNEtog1s86MNCwzG2Z6gSJ3i4K23ARuLonJE8EYfKIEyf_OO4nejLUOBGSEssXaFLf-Su-Qw3h5op9E5XovmSlpIexchgFEGI8THleaYimSj198NvROVAAp-Lcb7btNYQVk2Pg4PgjvZnFf9xbUmduBcT5DwCwDpprOzOqNza8y8tObHz0H8DS6sgZOBgDCtxMDKOC0rUQaU-6uiWIuVeFrXr_Z7MSTHrtJV3HeGbusQMG-VJWpKQqDVHaIJxJbMPaA4mUC_8mShfsE6gQcOOlx4XNMdP1bs2LK9q2YIMrfemwq64gsP7omySwPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/247968d991.mp4?token=OxjzbqNdh5j6R7sP3JhB6Au8P7DNEtog1s86MNCwzG2Z6gSJ3i4K23ARuLonJE8EYfKIEyf_OO4nejLUOBGSEssXaFLf-Su-Qw3h5op9E5XovmSlpIexchgFEGI8THleaYimSj198NvROVAAp-Lcb7btNYQVk2Pg4PgjvZnFf9xbUmduBcT5DwCwDpprOzOqNza8y8tObHz0H8DS6sgZOBgDCtxMDKOC0rUQaU-6uiWIuVeFrXr_Z7MSTHrtJV3HeGbusQMG-VJWpKQqDVHaIJxJbMPaA4mUC_8mShfsE6gQcOOlx4XNMdP1bs2LK9q2YIMrfemwq64gsP7omySwPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمید رسایی: اجتماعات خیابانی فقط با محو کردن اسرائیل از روی کره زمین تمام خواهد شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/127781" target="_blank">📅 09:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127780">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6NrvdvI6Vux3q_1Mb-pl0T50NIUg7yjx9DvCuMWAjs2EkhyqrG_J5h98NDRZtHxVrY_aIfUO1fzPJi7Cya2iRe3TTo99fn8mHSutyZCmKWsSuAaz9CYX-5MSVHOExe22NlCJfyzFjJFiIPsH0zVbfV0uNId20o3BjucINAFQYB6v936uzYTU1ALMU-Zai4qdYKT5YXwjDfdegeCWsxUrMHE2KaS8JycV916eGaA9qYu-m2F8Del-mX0u4p1Bgxvv8ySWFyyPb2FbkCTP7I7dbuNs2I4-3a3KNzYdPwQurIAIrAIh4AiQBfLZ3tnRTYgRX2KxoFRzClaNcWx9AWBtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رشد ۱۰۳ هزار واحدی شاخص بورس/ یک واحد تا کانال ۴.۸ میلیون
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/127780" target="_blank">📅 09:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127779">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
وزارت امور خارجه قطر: نخست وزیر و وزیر امور خارجه کویت ابراز امیدواری کردند که واشنگتن و تهران به زودی توافق را امضا کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/127779" target="_blank">📅 09:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127778">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
فاکس نیوز به نقل از یک مقام بلندپایه در دولت آمریکا: معتقدیم به توافقی عالی و بسیار مستحکم دست یافته‌ایم
🔴
ایران تنگه هرمز را بدون دریافت هزینه مجدداً باز خواهد کرد
🔴
محاصره آمریکا هم‌زمان با بازگشایی تنگه هرمز لغو خواهد شد.
🔴
مرحله بعدی بر عملیات مین‌روبی در تنگه هرمز متمرکز خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/127778" target="_blank">📅 09:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127777">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsMHwhlSml3mpbkc303s9eEjIIE-tJXnQtX8YT_tUskqZMBI7eclEIGCcuCGFl0vTMM2Ac5aQ2e5Rtavv5D5jeMe2CZv2LpQzCDDDMcREF6yTZNU2CN7GpghuFiE3gxrja3o54V48uw0iS0-GkGoC9GRn3PzR1AQXSC4iMfi7KbQmbMMHtxF3-06f4qKAxqbsj53WsO1PRnBOAgC9y15Sl2TfRqOKKqOD19C-X3v35ONRhlx17ODEcq-fYYPj9ffPXv_jHlj_xqJ1_JSPCH90rNWNHP1JeE5b8vUfVeJTZvorz5iHrQ8Hu4U-SXkGJTckx-sOHtgqIwmYcTwA6_6nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/127777" target="_blank">📅 09:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127776">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
آغاز توزیع کارت آزمون‌های سمپاد و مدارس نمونه دولتی از فردا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/127776" target="_blank">📅 09:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127775">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
سازمان هواشناسی امروز (یکشنبه) برای مناطقی از شمال غرب کشور و ارتفاعات البرز رگبار باران و رعدوبرق پیش‌بینی کرد.
🔴
این شرایط فردا (دوشنبه) در برخی مناطق شمال غرب، شمال شرق و استان‌های ساحلی دریای خزر تداوم خواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/127775" target="_blank">📅 08:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127774">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
وزارت علوم: تمامی امتحانات دانشگاه‌ها که زمان برگزاری آن‌ها با مراسم تشییع رهبر  تداخل داشته باشد، به زمان دیگری موکول خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/127774" target="_blank">📅 08:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127773">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvUnohc3Z2FiXpTfws_fDGHv5Njtmb7VOERXq6d8MAXN8DVPgW3bjGYYhF4PFeRhSL_F6ge0mFsaXaMUc-MQjrdY4EjQip6bfF8qHaf7Kc84tzT9195O2vSwsQqO6LqsAPFdmIYhegDLPy3HfdAeeQh-MGQKhwXLGQsSx290g4_wP_Bd-N_mzVi4fxcAxWQkKGarvnuzwZ6KQ0PeRtE2oJu5cgU5hgspwURoZXkvBTbUMolB76AZRk_6wxc4TJAM31xXLpvSUHovvNkVGDdd4_2C-uJ0d9JTr5IpIhQGisq6SGLOjqZACfg6Kq7-7U4oT0r3zHF4l5U3R6qbFSkphw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت خارجه کره شمالی: تأکید و اصرار آمریکا و کره جنوبی بر خلع سلاح هسته‌ای این کشور، بی‌فایده است.
🔴
خلع سلاح هسته‌ای موضوعی مختومه و برگشت‌ناپذیر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/127773" target="_blank">📅 08:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127772">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
نیویورک تایمز: ترامپ می‌گوید توافق صلح روز یکشنبه امضا خواهد شد، اما ایران درباره زمان‌بندی آن تردید دارد
🔴
نیویورک تایمز نوشت: یک مقام ایرانی تلاش کرد انتظارات را تعدیل کند و گفت هیچ برنامه‌ای برای امضای توافق در روز یکشنبه وجود ندارد و ممکن است این توافق در روزهای آینده به امضا برسد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/127772" target="_blank">📅 08:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127771">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
انفجار کنترل‌شده در محدوده مبارکه اصفهان انجام می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/127771" target="_blank">📅 08:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127770">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
کابینه امنیتی اسرائیل امروز تشکیل جلسه می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/127770" target="_blank">📅 08:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127769">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24c5f37363.mp4?token=Mzr_IkwLqBp4k6DG4EgUfxj2bDk7aiBKUCkPJbWWZ7kTiD9GGoFKQhmM6hQRa8ZfNL-z5BjsprVe0dkKiGJmvt4V4cm-Khy1jtiDYlqzxZlFBozfLNOOC6Q3bKD2fhCo122ruwv2JakQH9O1--pWtQ5KuzV8X9fPme-3jrj0cSpjpngqDzL1rT0dEHwFs6UyA2RH2OcdQfcAsl7TL-iiy1FJT5th8NfbzfmkMnoJJMkZzKsYP1pP0WHe-zd19ZHjZ1auHxGU__5BL1rS7gst6PznriFvlkABAgdxwpTxUveQHc5NSUEQVuIsseNA0nsK0_DpR71x-ciISmliPf2f2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24c5f37363.mp4?token=Mzr_IkwLqBp4k6DG4EgUfxj2bDk7aiBKUCkPJbWWZ7kTiD9GGoFKQhmM6hQRa8ZfNL-z5BjsprVe0dkKiGJmvt4V4cm-Khy1jtiDYlqzxZlFBozfLNOOC6Q3bKD2fhCo122ruwv2JakQH9O1--pWtQ5KuzV8X9fPme-3jrj0cSpjpngqDzL1rT0dEHwFs6UyA2RH2OcdQfcAsl7TL-iiy1FJT5th8NfbzfmkMnoJJMkZzKsYP1pP0WHe-zd19ZHjZ1auHxGU__5BL1rS7gst6PznriFvlkABAgdxwpTxUveQHc5NSUEQVuIsseNA0nsK0_DpR71x-ciISmliPf2f2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کلش ریپورت:یک فروند جنگنده اف/ای-۱۸ هورنت متعلق به ارتش تفنگداران دریایی ایالات متحده روز شنبه در جریان یک پرواز آموزشی معمولی در نزدیکی دریاچه ریم‌راک در ایالت واشنگتن سقوط کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/alonews/127769" target="_blank">📅 08:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127768">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
بریتانیا در رتبه‌بندی جدید ناتو در جایگاه ۳۱ از ۳۲ کشور عضو قرار گرفت و تنها بالاتر از ایسلند (که فاقد نیروهای مسلح است) ایستاد.!
🔴
این ارزیابی میزان پایبندی اعضای ناتو به اهداف مربوط به توسعه و نوسازی توان نظامی را بررسی می‌کند و همچنین توان ارائه برنامه‌های واقع‌بینانه برای تحقق اهداف دفاعی این ائتلاف را می‌سنجد.
🔴
طبق این گزارش، بریتانیا همچنان با چالش‌هایی در زمینه نوسازی و افزایش توانمندی‌های نظامی مواجه است، هرچند دولت این کشور امیدوار است با ارائه یک طرح سرمایه‌گذاری دفاعی جدید، جایگاه خود را در آینده بهبود دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/127768" target="_blank">📅 08:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127767">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
فاکس نیوز در خبری مهم اعلام کرد که ایران تنگه هرمز را در عوض لغو محاصرات دریایی آمریکا باز خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/alonews/127767" target="_blank">📅 03:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127765">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P-65hkGdcwKXJV35preZclO4LirtQqlxvKuts-S3Ie8WFiS9weGIgw0R10S2AeF5hfOMLJoa_G5IpZB3lqd2Y5KDsDkvjZGanJf7lkH1BqmwQmhN2LALi6a7FUGmi3wOPJYOMWJGuxPKQ2v_0p1IxFDz7IL1HTOd5GUtL3x6hXrhyZ57CdOsax4UN4WlMWxdHqdLurUZBrrPpYYEFbVg4XpKUVq5WA8sLDt1la2RTRauckjF5n2p4IjDo1dywbqb39AudGV593g8ppn8hMbhwahI9njEfC998WEf1h-XW-1adF-h8ysyOW954v6a5eUkmD3u_-03uL1bs_1YMF7OfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KAx-HraalUlhgvMk0OMEm1NE31F9TKCN1zx6MuOtDi6WGLjTqq6DOD0Xg_JrNXBrvccp50c4WItE34LnCMSopR6t3S904VHxZqcKz79puzHjmKPi9pA6sD_YRrWnu13zypWLdO1V47dPAD4jkDij8fiiuqtNi8458mSqRHkTpfkF28mOQu9kyK_6dcxpXbtZUbKTQhicewjsXckpzAxoHVCz9JJSIqt6eqZPDezVcOjrfEyeT4aeV6ecrRNJQ3lZA5g0G9v_n-GCqeDg5HCkben4Tdt67SjO-gPvOApVLnzf4X7VQq4jmMHa4RPLI45Yby0SkVmsAZn8erLRFscp_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
امشب تولد‌ ۸۰ سالگی پرزیدنت ترامپه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/alonews/127765" target="_blank">📅 01:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127764">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1ee53f0561.mp4?token=lunLw-PwOi7Ko2B3YLXAj7Ey2fqh5lkn3Z0wZl9K3kR2XWBjC4OyyUpCbI95sdN0SWuGW2blKTd8Q2kMpucml7GJQz6zaHsaEU4Jtdp67EQY21urKcUuHPX2lWXnKEYVnkBQ-TZ-WY4e95-m_FfWg3bA7d4OUkYb9KFgOoMROZ-AHHOvZ5LXA84ts4Swfh4s4TbjAgXJzjdVCZrwL9FyGDl5lCwn68oA1tdHPawqFD3ZBm5gW-JZTxGbeCRkcaww8dzz_CaZTq9PSdHyOee-2Wvs46nx6N994UytNtNA7a4HrObhp-2p0AtgomQbQGnWEeS4tHYt8T9P9IjdBWl7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1ee53f0561.mp4?token=lunLw-PwOi7Ko2B3YLXAj7Ey2fqh5lkn3Z0wZl9K3kR2XWBjC4OyyUpCbI95sdN0SWuGW2blKTd8Q2kMpucml7GJQz6zaHsaEU4Jtdp67EQY21urKcUuHPX2lWXnKEYVnkBQ-TZ-WY4e95-m_FfWg3bA7d4OUkYb9KFgOoMROZ-AHHOvZ5LXA84ts4Swfh4s4TbjAgXJzjdVCZrwL9FyGDl5lCwn68oA1tdHPawqFD3ZBm5gW-JZTxGbeCRkcaww8dzz_CaZTq9PSdHyOee-2Wvs46nx6N994UytNtNA7a4HrObhp-2p0AtgomQbQGnWEeS4tHYt8T9P9IjdBWl7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صدا و سیما: خدا شاهده همه اماما اهل مذاکره بودن و با دشمن‌شون گفتگو میکردن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/alonews/127764" target="_blank">📅 01:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127763">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLkcW4ovvGyZt2IqzMCfhds4OrU3Jc1pzYbsU3aP5qlHOFA1f0XroX_2Nrzr4QX4DFXyeLbhRKQGDjLdHDjs3Etn7jBXcrG4_No78PcNPQcg0JRaQhlhmw_41fIeppa5lWwTCaVAwAoRg5Sxi46Wizr6vksrlQYwTjwG7kFa2AEogyzLBxFaPjw6RXF3gJ_cbyrGLcQ8qWwFygt7pFkWm4sNADb8voGAGbRFF18Fhl1WTOvoopkFXAKWUIV4lThCqbjXhVKvoQgJdI07i8ur_vgB3EboihdP7SZoiCQWMJqPYY0phK6uI5YT6iyFCeDoOXwH70j1JT2DcR4aM4S74A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رائفی پور: میتونیم رمز ارز به نام علی خامنه‌ای بسازیم تا همه بخرن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/alonews/127763" target="_blank">📅 01:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127762">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
آبروریزی تندروها در همدان
🔴
صابرین: ساعتی پیش در همدان و در مراسم شهید شادمانی درگیری رخ داد؛ عده‌ای خاص با برخوردی تند و ناشایست (مخالف مذاکره) مانع از سخنرانی بقایی و حاجی بابایی شدند و حتی به فرزند شهید تنگسیری نیز اهانت کردند!
🔴
دختر شهید شادمانی سمت آقای بقایی رفت تا از دلجویی کند اما این افراد در مراسم شهید شادمانی به دختر شهید اهانت کردند و علیه او شعار بی شرف دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/alonews/127762" target="_blank">📅 01:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127761">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfkiVg0ukla3g6LqobxWN_5z5o2z8Ph8_OPSCd410Rs1FD14WSKXa4bewbEdSIZg9W6SQVunwFLKJc_Ck6tQLfTBn3_ykNCPy_4HJ4yKB1tOnPNCE4LP0Z2m3Uh4pkd9QxW7czfFzOrNnVuTUi2NjA3pYXbzUuMmWdBAYJuyJAO40bmsYlrN7Pt4ii50EtsQfqhiLD72zY6L_OXP0bL7Yqd_6f72OqRxDwMJCj70n_JjqTfVOvrGEqGz1VWlkVzzP0L6Q_oB-JSe23vR-pK_vwER1r7tyu9Rd-fqlz3M5RUgU2K41NAyfOWbCpSbA1wMCx_oh2yjQ8DKD3yswFuzNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش‌ها حدود ۱۰ فروند ترابری c17 از کشورهای منطقه بارگیری کردند و عازم اروپا شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/alonews/127761" target="_blank">📅 01:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127760">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adca31cc4f.mp4?token=rTVZAU8kUTkWAQpVNhZSKockszdaUJoTxoTQ9Lv6FRY71BN8YomcUarVk7vy2iTaJHEj-2BYH7Lt_u0VJjpZeciG8On374UeDUhtJ6H9gLpUaCFgM1ZWQeeMwlAJpYiA1Lm70F4Cgo_mKLGk4rW_3QJXFzeMUzzPEVBOJu1B_V3pM4SP4Z5rvPy92f9xFEmfXfxZbeHjYEk5nh74nzV18Tuw9MPVorINsjWz2eV6m0vSRIDAXgJt56zwFziVTJklRz8wwP1K8xBGvT8V3cRgObm5q25EYEv4i8qQEh2EEXKSzdTBvmSeGWcPZLC0CmeTp7829FODqeaT-I9AqwIO0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adca31cc4f.mp4?token=rTVZAU8kUTkWAQpVNhZSKockszdaUJoTxoTQ9Lv6FRY71BN8YomcUarVk7vy2iTaJHEj-2BYH7Lt_u0VJjpZeciG8On374UeDUhtJ6H9gLpUaCFgM1ZWQeeMwlAJpYiA1Lm70F4Cgo_mKLGk4rW_3QJXFzeMUzzPEVBOJu1B_V3pM4SP4Z5rvPy92f9xFEmfXfxZbeHjYEk5nh74nzV18Tuw9MPVorINsjWz2eV6m0vSRIDAXgJt56zwFziVTJklRz8wwP1K8xBGvT8V3cRgObm5q25EYEv4i8qQEh2EEXKSzdTBvmSeGWcPZLC0CmeTp7829FODqeaT-I9AqwIO0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحبت‌های یکی از لیدرهای شلوغی‌ها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/alonews/127760" target="_blank">📅 01:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127759">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LkEQQEb8mhNq2VaJV2Yp7jjDZwmcCSkmTGdnDadGaSK_EbaZZFUmtg01ob-SHxUCWxPKAgJ81c52iNLBCQ_pTtoqxgQxDtLAK4xsBFO5cxn_TpzweVtZ1K1aXDv51QrThhA6G8bs7mmuI98xhSd6GvG-dMjVqiuf9uV1OM0ncyztoLC562S2j-DMxOfRryTI7CsgaUCRH5GUgPQ3SG_JM_4cT1HvHc8phcMwyQo8RlTY5UojTgoavrDR8yPNchP1Tjd06nAnaQ_cM1uWfbghkL12KR5TDq7HUgqERI0edcHH7GQq_oXEH414ZlaZPz8zYyHfaFD6UGxRMUR1c4Oblg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فقط عباس میتونه جوری توافق کنه که:
جمهوری اسلامی ناراضی باشه
مخالف جمهوری اسلامی ناراضی باشه
اسرائیلی‌ها ناراضی باشن
آمریکایی‌ها ناراضی باشن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/alonews/127759" target="_blank">📅 01:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127758">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
خروج تعدادی از هواپیماهای سوخت‌رسان آمریکایی از فرودگاه بن‌گوریون!
🔴
تصاویر ثبت‌شده در روز شنبه نشان می‌دهد که شماری از هواپیماهای سوخت‌رسان آمریکایی پس از ماه‌ها حضور، فرودگاه بین‌المللی بن‌گوریون را ترک کرده‌اند.
🔴
تنها تعداد اندکی از هواپیماهای سوخت‌رسان آمریکایی در محوطه فرودگاه باقی مانده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/alonews/127758" target="_blank">📅 00:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127757">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yz5UfQ_X5OIFh_F8HEgGCaSXXSNE_j38NIGoc427ZdU4g9McX3GNzc2vRi6t44GyBUtz2TomvvZBTm9xHN35UWlwdXGAlTsFiXre2FMVlLx3H5zfS44HQT90ewFnmJaFw7cMDHhEEdN1_RJu5SQ2DYNUXTUXQmoQBE0N34_WnsMBYc7V9dW-B_OU9pYlm0aZz74L76TAgaECs9yF4Lqjr7-pjyhLlghKGsaAZ2GG1_II7UPWygC45nn77xfM0J6g99FR0KheQhsZzJcThprsLpgK91LOJcpU26JwaIbTsd5oZDBvgth_Acz6GRfzKBmtH9M_PrVgIycCw64U4KUnDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حسین طاهری مداح در میدان انقلاب: تندروهایی که امروز شلوغ‌کاری کردن هم ردیف طرفدارای پهلوی هستن که شلوغ کردن، باید مطیع رهبر بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/alonews/127757" target="_blank">📅 00:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127756">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56d1d99919.mp4?token=jUGehgZd2QJlvq5TXV_Tg_FMdj0DU3zWhivE5gq9nhsb-TsmcW3nlf0RW79yr7sdpaNpBABYh5sXpqy4GEQIxJkAdB9iXQbUlRQjzxFwrXqjTyNnGmjidNhkFt8be1Rq5PaPagXjEkkwYpo-I1VufJmgxnPichZVeGsogEi16AOAd6A31Nk1cth0rxIXVWNl9Aynz6enRvJYczqBHP3fzN1iKNCW4uwyq5H5ps_9wGuNOu7UoTqnUGTqe2eVmpmTsamMhTjOD5Y2LEd2jB-YK8rF-40sDBlAuthNz9Kr27guK1QjgeISu14_SByXckBJm68kOBWfS2n9XuGjl5-xxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56d1d99919.mp4?token=jUGehgZd2QJlvq5TXV_Tg_FMdj0DU3zWhivE5gq9nhsb-TsmcW3nlf0RW79yr7sdpaNpBABYh5sXpqy4GEQIxJkAdB9iXQbUlRQjzxFwrXqjTyNnGmjidNhkFt8be1Rq5PaPagXjEkkwYpo-I1VufJmgxnPichZVeGsogEi16AOAd6A31Nk1cth0rxIXVWNl9Aynz6enRvJYczqBHP3fzN1iKNCW4uwyq5H5ps_9wGuNOu7UoTqnUGTqe2eVmpmTsamMhTjOD5Y2LEd2jB-YK8rF-40sDBlAuthNz9Kr27guK1QjgeISu14_SByXckBJm68kOBWfS2n9XuGjl5-xxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعار در تجمعات امروز: اگر چیزی امضا شه، مسئول باید کشته شه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/alonews/127756" target="_blank">📅 00:49 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
