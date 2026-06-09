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
<img src="https://cdn4.telesco.pe/file/DKPasx_i3s3ut2xohVdqZou4gfQub5eBLa9_XINWO5BxsUChWTGq2JK9rB-bVqOfYO2azjGJnrdkCvmjMrkM09-Tq5wKFiRG4PWwrHg_rYx7tCvvAsb3M4B5nYXuELiczHaAy8sUJVnJHK6K_rBTCDGS21fTJQgrrKdp8l4LZxm9nCkvPW1rTWoWJ-IoSpcaApDAouEqCp44u7_NJXtwkD-8FK1TsnQ-MWtOgR2O9xHy139e81nsphjRCkHwhYxTHXCzCGDXHto1Jp2Zgd8Ra3DJltlgLyowoSXAerBiyMca1wcMl5xYRDmjp86GLUPUPZG5Ty8lGN_h_4l2q2kqAg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 174K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 10:00:44</div>
<hr>

<div class="tg-post" id="msg-77316">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">شدم مجنون مشهور میدون شهر و کیرخر دهن مارو گاییدید.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 587 · <a href="https://t.me/funhiphop/77316" target="_blank">📅 09:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77315">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bd5c51779.mp4?token=IySSKX6BFHG0u3XT-ylFQQxSmd4zdki6izW43IsPi0Ta0hdhIMiDHBXptWgMeppsSWnTYf69aJHvMwvVZhjJdBddzBT4qu003yowSZ9J0uYc7NxIukn155qc8oBx6PP6xEwkaltN2lc7_kMF3_isj8MurzaAOpEF73i3soI3JVw_efdnzu_uzv4Bqh5stN7kIjWYon10HHLdFw_rvfQ0ZvVIPPp7Lo1NDI36gDtxk2KKiJdwjiCHXhLuzoZSrEytv2oGYip0s7SQDIeEywwWxdDWX6ZfMwr_yFH5S8BDKBEDAo3MRhhy5DCW-YxRhXxJOHLVxWBpeh3JaEJyRvr17Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bd5c51779.mp4?token=IySSKX6BFHG0u3XT-ylFQQxSmd4zdki6izW43IsPi0Ta0hdhIMiDHBXptWgMeppsSWnTYf69aJHvMwvVZhjJdBddzBT4qu003yowSZ9J0uYc7NxIukn155qc8oBx6PP6xEwkaltN2lc7_kMF3_isj8MurzaAOpEF73i3soI3JVw_efdnzu_uzv4Bqh5stN7kIjWYon10HHLdFw_rvfQ0ZvVIPPp7Lo1NDI36gDtxk2KKiJdwjiCHXhLuzoZSrEytv2oGYip0s7SQDIeEywwWxdDWX6ZfMwr_yFH5S8BDKBEDAo3MRhhy5DCW-YxRhXxJOHLVxWBpeh3JaEJyRvr17Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از پیام حسین رحمتی به برنامه طبیب :
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/funhiphop/77315" target="_blank">📅 09:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77314">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5AvldXVJe7ABs1TsSKzNT-x1sQKKmMC9fvk7FVpjU8Bu6T6vP868H8RYoL1urBUeAL9u9LJJVHLoJ1WIIGUGOYdrFNjS0Ye7gIDbWmm42jveCmLdbIbocHzqTZV6o-rLoq1P1M5lqDntfMPqb32hK0rq6kMuBxtazfe3c8efr9WrFpfQKP4Q48quNMzPErVhLpYS0Yafavml11ay2VWj7z6Sa7efaQSzzxOvymIWc8JPVBsWNIvp7waPdz1ZxNhmBbe6I0x7lXK1YmfwfzL6qLQLWuYMx0ZlYA0sZFaw60ionHltpe_uRtVfEcihQc89_aDncIFW3rwCQ94bU-z9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
آرژانتین
🇦🇷
-
🇮🇸
ایسلند
🏆
رقابت‌های دوستانه بین‌المللی
🌍
🕔
بامداد چهارشنبه ساعت ۰۴:۳۰
🏟
ورزشگاه جردن-هیر
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
آرژانتین در
۱۰
دیدار اخیر خود،
هشت
برد و
یک
تساوی کسب کرده و در
یک
بازی شکست خورده است.
✅
ایسلند در
۱۰
دیدار اخیر خود،
دو
برد و
سه
تساوی کسب کرده و در
پنج
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر آرژانتین
۲
.
۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر ایسلند
۳
.
۵
گل در هر بازی بوده است.
🧠
وقتی نتیجه از تصمیم مهم‌تر شد، تفریح تمام شده است.
👍
ورود به سایت با فیلترشکن
R19
🅰
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🤖
ورود به ربات تلگرام ‌بت‌فوروارد
💻
@BetForward</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/funhiphop/77314" target="_blank">📅 09:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77313">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMXuqdbaWwKz2W1_E0gYCH1mCYTK-W5c_9DPIaJCC2H7MklcLzDAbYTmMIo1iWPmWAdDQL5qzU9LKA9GNM_KRtR152SesdjqZVDZgbzhC-8oHSnDQcpoC2HxvZ4VZkehjIpH1ufjiIECMoNGIFyNS2gxIH-Y-jtnB2UPhIRF4ej5hQmk7SSQK0FuVZhKGDTirVYu6f0Aao96zdklO0Pt8G6_cnM5sHNzqDfn2LfXHHsG_Unmn13-1bzCe_YTq7uTblotRHZbPoOOqAUTjfG9bOso9HAPB-htbnZldCNRUAXYJQw3PX5-JKROY118DJsurUS22K4-YC0Q6LjHllSH-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کصخل این که ایتالیاس
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/funhiphop/77313" target="_blank">📅 09:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77311">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اعزام لشکر  82 هوابرد معروف به شیطان آمریکا به اسرائیل
لشکر ۸۲ هوابرد ارتش ایالات متحده در اوایل آوریل به طور مخفیانه به اسرائیل اعزام شدند، به عنوان بخشی از برنامه‌ریزی مشترک اضطراری بین اسرائیل و ایالات متحده که از فوریه تکمیل شده است، برای تصرف جزیره خارگ تحت کنترل ایران در خلیج فارس و ایجاد قلمروی ساحلی در داخل ایران، طبق دستوری که کن کلیپنشتاین دیده است.
این دستور که در ۷ آوریل ۲۰۲۶ صادر شده، به چتربازان از گردان دوم، هنگ ۵۰۱ پیاده‌نظام، لشکر ۸۲ هوابرد - گردان معروف «جرونیمو!» - دستور داده است که به طور «ماموریت موقت» به اسرائیل اعزام شوند، در حرکتی که پیش از این توسط پنتاگون گزارش نشده بود. وقتی درباره تعداد نیروهای اعزام شده به اسرائیل و مأموریت آنها سؤال شد، پنتاگون سوالات را به فرماندهی مرکزی ایالات متحده (سنتکام) ارجاع داد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/funhiphop/77311" target="_blank">📅 01:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77308">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiCxHoeYv11iIkV0Pg4iHRKz1aKs8jB9VGvjMZk0Lr_Rt1fAoHMga0PEwVi8lr7O_7CKbtr9H6rEMv45-3e74idDJC2WL89T1emAw4QoD_TYSJ4SUPMyVKyHvcOzs4rk7-2SaG4RFs629uz-SQCmlZuFWpZo9intmtYptFNHRPsN0ktVt3S3W1lfWxsvAPZLkb0-S9ntbg5r45PHWyc4O7p6OEjUZ303_laAxZaIOSGT_AxVNTh_zkSx2KfkyKOtPMr9o3TQ0sNqRVXcOWhlehOYCbukscBxIWP0-h7emqQojpo0oyndCG9CEwmyM0NKHCD7j-DRS7GAsLaSx3cQdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">والا خواستم یچی بنویسم یادم افتاد چمن و مهدی میرن گونی خودتون تو کامنتا جواب مناسبو بدید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77308" target="_blank">📅 01:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77307">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ به آکسیوس:
ایران به شدت خواهان توافق است و ممکن است به زودی توافقی امضا شود.
این توافق مانع از دستیابی ایران به سلاح هسته‌ای و توقف غنی‌سازی خواهد شد.
این یک توافق فوق‌العاده است.
ما همه چیزهایی را که می‌خواستیم به دست خواهیم آورد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77307" target="_blank">📅 00:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77305">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">یک مقام خیلی مطلع و بلند پایه ایرانی به الجزیره:
آمریکا مدام پیش‌نویس تفاهم و خواسته‌ها و شروط خود را تغییر می‌دهد و این باعث سردرگمی و عدم پیشرفت مذاکرات تا اینجای کار شده.
بدون آزادسازی پول‌ها و رفع تحریم هیچ توافقی انجام نمی‌دهیم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77305" target="_blank">📅 00:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77304">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یک مقام آمریکایی به آکسیوس:
نتانیاهو برای بقای سیاسی خود در اسرائیل نیاز دارد که جنگ ایران ادامه یابد، و ترامپ برای بقای سیاسی خود در آمریکا نیاز دارد که جنگ ایران هر چه سریعتر پایان یابد.
این تضاد منافع پیش‌بینی آینده را بسیار سخت کرده است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77304" target="_blank">📅 23:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77303">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اردوغان خوشحال شد
سپاه به مقر تجزیه‌طلبان کردستان حمله موشکی کرده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77303" target="_blank">📅 23:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77302">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGyWJ2mYVYPirU6gEnlhYP78eQ5DF886bcWGXVtf5qTY-dqowaHOGdxQIoWxzQPenxhJHpW-ds3yPtnvF6kD19QcPWD9myAjtALu8AuK1VZANkqVafdTkdDC6OXVIjKlUjkS1fN4NL3cii6fGWYUIwrcScbQ-4a5hEkn40f4jeC44BtyoFgikJ5bYjetritAt3zHyVmCgt2pwg9n6yQ1M3Cz-rvCervl_Y157PzxiLZVVHbakv2hK46-GK3xFn7ueDA1W3Y01ValD7vhUK2sKvxuRGXQxWE9pLMDGmnwvn2WR7x2Kj3OdKxuUVfAlpKdXHKngFTytkBe7nMm1FZADQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان هر چنلیو دیدید که اینطوری میخواستن خودشونو مردمی جلوه بدن و بگن ما پشت مردمیم
باور نکنید، اینا مهره ی نظامن و هدفشون اینه تفرقه بندازن!
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77302" target="_blank">📅 23:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77301">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">تنها جنبشی که از نظر علی خدابیامرز درست بود جنبش سبز بود
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77301" target="_blank">📅 22:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77300">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">یادتون باشه که تمام جنبش های مردمی سالهای گذشته هم راستا و مکمل هم هستند
اگه کسی خواست این جنبش ها رو در مقابل هم قرار بده بدونید که به هیچ وجه طرف مردم نیست
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77300" target="_blank">📅 22:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77299">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sry10_PhNl8cKpHn-HCH-FMO_0ffLLfPj_61X5rNI0HYIIxBG_tqHG1PNW1GotWYozzdj-YLfbV1f1Z5Y4j-rGtFFnNhb4jwENOHXvXaImDqOE4yLDD-PvlZX4Qfe8-sisFWv_PRh6j76ShGMWj57a65_JEzqJmGxzz4TYYDll3Cv4HFGKlBqjly4_juoyO77Xj7icjPjQ3GOe0YZZbnadylsmtfUjquWCwLb_01ePG0i6c-LZlzrtDh7hJvX8e4RLz4OS2KCUjV_3uLxYv3eiKZaJSyWRQ9bZVn_tu9ZKbYxLDxOWp40fYA6d8RuYP7h8HmwHnvP9EkxSG9vqX-4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیل اینکه که گفتم جنبش زن زندگی آزادی درحال‌حاضر مورد استفاده ی اصلاح طلب‌ها و امثال فردوسی پوره، یچیز مثل همین اکانته
🎒
و طرفدار وطن پرستی با بیو "زن زندگی آزادی"
که همون قضیه ی ملا به ماتحته‌
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77299" target="_blank">📅 22:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77298">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">شهید واقعی زیاد دادیم سر جنگ عراق
که اتفاقاً اونا هم جاوید نامن و جاویدنام باقی میمونن
حالا عراق کی بود؟ دشمن ایران
۵۷، برنامه های انقلابی از کجا پخش میشد؟
رادیو تلویزیون حزب بعث عراق با مجوز مستقیم.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77298" target="_blank">📅 21:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77297">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">رادیو ارتش اسرائیل:  ارتش اسرائیل قرار بود در ساعات آینده حمله‌ای بزرگ به ایران انجام دهد که شامل ده‌ها جنگنده نیروی هوایی بود که آماده برخاستن و هدف قرار دادن اهدافی در سراسر ایران بودند. این حمله گسترده با فشار ترامپ لغو شد.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77297" target="_blank">📅 20:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77296">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ به کانال ۱۲ اسرائیل: به نتانیاهو گفتم اگر جنگی تمام‌عیار علیه ایران آغاز کند، او را تنها خواهم گذاشت
من دیشب از نتانیاهو خواستم که به حملات ایران پاسخ ندهد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77296" target="_blank">📅 20:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77295">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پدافندا بیدار باشید باز ترامپ داره می‌ره بخوابه:
یک مقام ارشد امنیتی اسرائیل به کانال ۱۴ گفت که بازگشت به درگیری شدید با ایران ظرف زمان کوتاهی تقریبا قطعی است، احتمالاً در روزهای آینده.
هشدار بالا در هر دو جبهه دفاعی و تهاجمی تا اطلاع ثانوی حفظ می‌شود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77295" target="_blank">📅 20:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77294">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">می‌نویسم امضا می‌کنم آمریکا برف امسال رو نمی‌بینه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77294" target="_blank">📅 20:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77293">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ERHjQuELyAy4kvUibcB5dQX-7sUbCknwQ-sjeEgeIPiX9cowzr9PkJ8MQ_eO4G2mZcUEexhdf_DnJ3wkInHYymsI5AiT1baymHPuF-UVmM6ZtgcMhXRW66XS24SBZQtbeOVxRwDzx6kKiAgpcreHxwTOv49gIFetx9vk9nnxF4U5IVsZvx4tAI3sTPvYP_fTRyQClx0QcKitqPPgnWMAW9YnzpJUY7bGAmzILs7_Za0D5z-TGA6d5tGobIaPt03D6rd5y3hb7Da_-HwmX6zp3t9zXr9VZtrxdqB03qeLuSvd6hMi7gBBIs787R6Y5Q0ZKrmf9CZa9pJReKYWdXbyjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان عجیب پروفسور بقائی، سخنگوی وزارت خارجه:
تحقیر نهایی آن‌ها زمانی فرا می‌رسد که درمی‌یابند سلاحی که برای تسلط بر دیگران ساخته‌اند، از بند رها شده و اکنون اراده‌ای مستقل دارد.
در آن بیداری تلخ، فقر واقعی قدرت آن‌ها نهفته است — و آغاز سقوط اجتناب‌ناپذیرشان...
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77293" target="_blank">📅 20:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77292">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">رادیو ارتش اسرائیل:
ارتش اسرائیل قرار بود در ساعات آینده حمله‌ای بزرگ به ایران انجام دهد که شامل ده‌ها جنگنده نیروی هوایی بود که آماده برخاستن و هدف قرار دادن اهدافی در سراسر ایران بودند.
این حمله گسترده با فشار ترامپ لغو شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77292" target="_blank">📅 19:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77291">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ:
حاجی نمی‌خوام چیز کنما ولی انگار یه احساسی درونم داره می‌گه ایالات متحده و ایران به توافقی نزدیک می‌شوند که راه را برای مذاکرات بلندمدت هموار می‌کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77291" target="_blank">📅 19:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77290">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFpD6CobCfm2J07X3gnxby5djBw1ovudkk_zuKykQ8ZMkcskeFzj1NbSi0omuCicnQGex1rSAEYbBBQZn4CtA8EhFo2V0aPHfSEPWgaiOK9LgVB_tJXcrhRGJmsNlZtTq2gf4as_tFh93206C8TH6WclTOMi5BiI8hPu4bqthb4tI5lvDR_GTuGO67qs3Oq4baNwlMcGY7NYmUmfEbMw6ftkwudGqNpDeRS7Lpx9BNZdmxFipqrRx6_xT-Ybm5LzqwGi0h2EsUOASMkAvqsxHVr4lRGDCJHTUNWCCJIRJD6pNbfa10VJrOBFZYUTuuvP11TbWN5rlvmBIvy-eTT8IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77290" target="_blank">📅 18:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77289">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">انگلیس از شهروندان خودش خواست به اسرائیل سفر نکنن
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77289" target="_blank">📅 17:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77288">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OjVMzp1HktIJIon4NvdcCrD_WOpuUswjD3jdZvfswjdWr-PXwuqnE34b78wT_F1TuDuCG2BBEHEhpB-bDXuHJDNWet6seOfyvpnUKoQML8-Mko0AqmgIKnZ0PdqjRgpvxV7SIa8tw1sj_eWrVLcCM4a4-e07H3qq2Q_-4zU-1P6WPdifBZztV1Q1-r9Nml3janAgaRy1w2jXg8wJztmO4RC6kI9ousPpdf8bFaO8_2OOtOlsbmk36Gtcw0MsET43WJOn5a-JuWi19Ne8F8n8Nakqz0W6FDkMHp3sL3n40YYcymjfMbfidKm9sXbittr6UmcAlG5X8xcSRi7er69Qww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنوب لبنان
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77288" target="_blank">📅 17:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77286">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C0cA5rlsp7WXgIjZGth6s28xrSXuGM3IFFr0TymDN0bO-qJFLDBRnHh_jUaXP6gTbumyOIW7RX-RVFqBoku0JopDh1JG-9V6VW_6xDJrmVUKFOYRAXrUXeTyahgW4AjevnIy8B3QK3V0g0Ftnsmb4u9zd5rbTLjo8KL-A3ewXLEQD-dh6oJ97I-YbWeGnDzKDDbVIjpNGE8FPT38OSr8zQ0kV-xRXA2jG7mFr9ZhOn5yvmVJ2VVullDD4qtC6uKbBEo-KKyIaAAva4EPHkmUkTaBLEy5fgF7nsZxPznXJUclFUQrxsTRONGq3T4iFw09ybOMcQhLLk4X_lpDGbo5IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pjo5BqHHIUWhm9wFjrnYzQYexT4nE-Jzq59QS-DGt3CAiQ4_RPXWVL3f9KNjeFu0LNc2ZdUh_GadKTJOwzjGMTOqIxtjXhARs-KLezlwvrNMqT-aDyaBo9IWYpKrw63ynlUs-kNg_bikzhH9rANIrjqHA_BKhIa1uEE0KyGq8ngYxaOR-S6TgnQuSXjOCgOF3IGSFsCiT6Txn84mj3WpypJ1OLEt4Vq21tNZ5cn1iNB7szZ4nw9VNbUw-w7OPW8_VeLdUNmxPdC3NQJkgMJstbhKM1EWJXNc65Q3xRZ1KICI32XKHxV_JwGelSkIUMbllZb0wgvKyUC54mVJTz5VKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نعمتی که از دیدنش 10 سال محروم بودیم
🫠
🥲
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/77286" target="_blank">📅 17:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77285">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app.apk</div>
  <div class="tg-doc-extra">51.3 MB</div>
</div>
<a href="https://t.me/funhiphop/77285" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📱
اپلیکیشن اندروید بدون فیلتر لنز بت
🔹
ثبت نام آسان و سریع
✔️
🔹
نصب و راه اندازی تنها با چند کلیک
🖥
🔹
اپیکیشن را روی موبایل اندروید خود نصب کنید و بدون نیاز به vpn وارد سایت شوید
💬</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77285" target="_blank">📅 17:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77284">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/A6nPeeaGLrA7LH7Gqp5vb9cCymLWn6AtUKYZIF0AoybRVkiEa8OZHGAV_QEtDjcfueMfXhZhx1VijCcStVJfs5EZrHtpEx51xRAPGWVfXJ08v2sSAEpXkPrlUqsuyfTP4HjTbFbWcmtqnUx76GM25go6qruO2Tqf7K43mtZlhktyE0CMqAtcrMzeUxNDgYYht34U_8gWR9-nf630_MWTUfRax4KB33oEgH2GBi4MgPaBQZmZFeoc6pzAttaGlW4InpY5vyRc4JP5N2npZudiA-5ClQQE6padclgGUW1bZvonlbvcTztW2-YIvC9bhATBbi4zFuyrW6O_qh4kzPqOPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎊
با لنزبت، دنیای واقعی پیش‌بینی رو تجربه کن!
💳
شارژ فوری با کارت بانکی و درگاه امن VIP
💰
برداشت لحظه‌ای تا سقف 10,000 دلار
💯
بونوس
🔣
0️⃣
0️⃣
1️⃣
برای هر واریز
🎁
جوایز هفتگی مخصوص کاربران فعال
💵
پشتیبانی از تمام رمز‌ارزها برای شارژ و برداشت
🪩
امنیت جهانی و بیمه شرط برای حرفه‌ای‌ها
🔤
🔤
🔤
🔤
🔤
🔤
🔤
G18
🅰
📱
http://Lenzbet.cloud
📱
https://t.me/lenzbet_official
📱
https://instagram.com/lenzbet_official</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/77284" target="_blank">📅 17:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77283">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqQGmMsiPKf59INBBH02ngpsbYm6McwhIIdYhMSx6yqEfLb-7lW5bMlSYgZK5Y5B4udsygh_UXNa7x6SLExXCK0usMobs2XKQgcdCmo31fhnJO3OFzWk6kGSifneU-4r7ZBGBXxHMSgHgLtK1p2kDRFb9Z7d7Tc6fvdwZEDt-22OxDJsQbnf1T7zUuVUpWPFv3JN0KIPOYMFiMOenqm3d6Mr1e3qj3ZW57VGFzfb49doz9j5seaNDlFS8Be2XHKnMpW57X9qFALTwgfppnDreikTo3Ix4-XjUITBhwyQLWnAc7YqlXLA1rLdXYjowJkOeWzs_rQTMuvW95AOtbfBkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قصدم این بود برخط باشم، دستم خورد رو زبان ترکی تازالیخدا بیردایمیش شدم
@FunHipHip
| Constantine</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/77283" target="_blank">📅 16:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77282">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lvb2DO35DbbBv4P3fRnUa3y4M5uN3rFL_VIjQThkK7Q0TAz45wBqFz201oS1a9XhNz6abJuod8jaI2ZoKSm2Jw1hga78n6APfNvHpBo_-3zuWVed7q7gsazpdhzKvLzkdKG_ssIArGIgOgqHld6l-a3VQS6zYIZFZlYLLrHAEATMqxPo8T6s3KTh-saUsR5KfjnZ0o4Ymdw3jwPg4cNydh8GA1GEc5Yl7Rsac8YiqWdQo9yGMamW35e-6S9y3TIU6uJ58D22e6ePg5vGi6hbN_pFcnel7fuFy8RFASqYOGDWdXrVgOtktT1a-9d0TvKkOvgEvToJwruKtd-JHYb_1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استهلاک کمرم هزینه بردار بود
آب هدر می‌رفت چون بعدش باید دستمو میشستم و از مایع استفاده میکردم
هزینه ی عمل دیسک + ۱۵۰ میلیونه
و برا همین خم نشدم که بردارمش
فروپاشی اقتصاد ایران به روایت فان هیپ هاپ.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77282" target="_blank">📅 16:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77281">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">بچه هایی که خارج از ایرانید شبا که گرمتون میشه پاهاتونو از پتو ندید بیرون چون ممکنه ی موجودی به نام سروش ولی زاده برای اینکه خنکتون کنه بیاد پاهاتونو بخوره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/77281" target="_blank">📅 16:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77280">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQPFDscVZVA7wgQnLpB2uce3TvHf6ZQWmSDJjft2dPYhwhLwFqel5kCXtOTTzppesudMaDp91I9z7J8WfzPsop1SfKgEql8uo1oGAL61XkIUpu6khB38ttdjomkYC8VrW70a0vgC9mVLoN-35CRsz1m0I2YwgLdyPhUJgc9GPhhML573Kj-6DPjpUYqV_a_riqY4rSWkuPKbAqFdxKkeEwwZ171ikYZd83y0Nz3PyXUncsqVVc_zJuHMt0oJSywTfPin_ko4nhrcZlgnINsThE4aT47j-lc58Vik8Wqsq8VrgSqtSNgCgOvqfge_Qzz8l3xUakIyLQ9qWX0UhqifDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان حاجی پاکستان
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77280" target="_blank">📅 16:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77279">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">الان ملت چجوری به کانفیگ فروشا توضیح بدن مودی نیستن شرایط و تغییر میکنه فقط</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77279" target="_blank">📅 16:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77278">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7XiF5OeygMMnIurUowBmwvSEEqjr2ms8IdKhvVcfPD0VKzqa6DWsj9ziolv7HUAFL0u7Rq1rolFvdRiuRPoDOnJuhJIeLOR5jn-Bi-tj9TMSPRQTUdZmVkZL0H012FiDTFbnPn47lwJA-rnRWDAtV3BTC_wNSHy7au0-pqJDkME9cy2WBZa931kx2s4pXWff_bKsLdjRCepNVWwH52EolJCnQ75x1dn1_FmDsWENFUuxwR6hztXtN0YkRkUosOszfBf1T-7dOo4OTCNBoPWdRp4k_yqk2uBXSE4RC5WIAADqo6hjCXcqr0TtSCa4I00TI950JDkMmcq7bCoqVomqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید کوروش به اسم
تهران 2585
ریلیز شد.
YouTube
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77278" target="_blank">📅 15:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77276">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اسرائیل
⬅️
لبنان
ایران
⬅️
اسرائیل
ایران
➡️
اسرائیل
ایران
⬅️
اسرائیل
فردا از اول بخون همینو
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77276" target="_blank">📅 15:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77275">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VB9FLS5CY592aWBgBxn7uOR_UVTj4C4LSgfNQ05Svy_5UFqJYVUT_MeMuoPKGRz_irxKVLAHbT_I66nxEWhEaUjUWS_toQxIZwDK-aZz9MxdpyBosekw_eedy00abpJNi9WBDYp1hYWgnMbjP-dsWpxHqRdsZ-u8mch-gMPHJ7pmF6A5wRsIxJ8EN7QBbGe2bLYW3C35kYINEFQtbG6UevhX4zjMNX7g60vSQADvoznjWMaNUtNViRLlfiwQ_0SFIg3HqYjBaJXs2KJkZSiEwFI7prbz-ZnwOuxygTEh4f4sMY-GgL6cmlNPWOTRK4UPPxU5L0ockoT59PGnTUaQ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرارگاه خاتم الانبیا: از این به بعد درصورت هرگونه حمله اسرائیل به لبنان (حتی اگه به بیروت نزنه)، ما خودمون موشک می‌زنیم تو اسرائیل.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77275" target="_blank">📅 15:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77274">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbRGw45BoTJxdgYNm7puJjHS5yiSL8Rs9TEi49XFsiEIGJk1vbHNSZ45q3Mp70glXEjgKJybvVSCLPCm581eOn0c36Db9djJq1V3qoO189fDpvig4NV_Ff1y9JFLkS5wqXCE70l6MZvRjO9qjV8g4eODzj-lnBGUGVJQWShmXwTsnO50881BeLjWx2dP0KsE_eFWJTfmLfVAP9bGlQYwtG-xp9QMTMy3Z6qgy5oiU8EETSZOACpr5wvMGO5vh0xB2f0ZOfDDNDcCwcrCuZEXJq2orDXKB42-KIcsTif2PIlxwNsegoZJA2GmHiC_Hau7Geo6boNQrQcJWkk-OIuVEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرزیدنت پزشکیان:
اولویت ما امنیت ملی و آرامش مردم‌مان است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77274" target="_blank">📅 15:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77273">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">قرارگاه خاتم‌الانبیا: فعلا عملیات متوقف میشه اما به جان مادرم اسرائیل دوباره بلند پروازی کنه یدونه موشک میزنم.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77273" target="_blank">📅 15:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77272">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اسرائیل هیوم:
اسرائیل و ایالات متحده پیامی به ایران ارسال کرده‌اند که نشان می‌دهد اگر ایران از شلیک مجدد خودداری کند، حملات بیشتری صورت نخواهد گرفت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77272" target="_blank">📅 15:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77271">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ولی واقعا جواب دندون شکنی به یهودیا دادیم، بخصوص اون بخشش که مقر پلانکتون تو بیکنی باتم و خونه خانواده سندی تو جنگل رو زدیم.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77271" target="_blank">📅 15:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77269">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ولی واقعا جواب دندون شکنی به یهودیا دادیم، بخصوص اون بخشش که مقر پلانکتون تو بیکنی باتم و خونه خانواده سندی تو جنگل رو زدیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/77269" target="_blank">📅 15:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77268">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">من کسخل‌تر شدم یا پزشکیان واقعا داره چهره ی محبوب جمهوری اسلامی از دید عوام میشه؟
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77268" target="_blank">📅 15:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77267">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">میگن پیت هگزت به مناسبت این جنگ نصف روزه ۵۰ تا شنا سوئدی رفته
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77267" target="_blank">📅 15:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77266">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">قرارگاه خاتم‌الانبیا: فعلا عملیات متوقف میشه اما به جان مادرم اسرائیل دوباره بلند پروازی کنه یدونه موشک میزنم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77266" target="_blank">📅 14:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77265">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">معاونت ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور:  نگران نباشید نتو قطع نمیکنیم  @Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77265" target="_blank">📅 14:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77264">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">معاونت ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور:
نگران نباشید نتو قطع نمیکنیم
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/77264" target="_blank">📅 14:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77263">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5tVvHEGolkG5iCZzMua2MrJLAHREmEndH99BMMuWOE3ifAKnQQf2PTgCvFBFgOvToOyjVxYyjhjvW99O9VRyJ-HG1rwwjlDJwKZOBH8rblB7CrEGWDXTNvrAat5X42xxHEq97zgxwhyGj4Et8j81XWLfDQXvueiaqZWFb0J6xHbY18ia_v3dUMMSxQjZp11-Jwuqv-dJCQ0TNlhJ0GNdy5iEWq-QNUZM3tsgXsoLUSrht_OF0Yr9gZbdWzOAKuHlQRcw2h3FI6EaiTUYQxPLwANWXl1pxPGRr4tI6U_cvtmU7kPCy6XkGB6KMaImM4Xyp_MjzVzhPNH0VGRgowURA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:‌ هر دو طرف، اسرائیل و ایران، به دنبال آتش‌بس فوری هستند! مذاکرات نهایی درباره «صلح» در جریان است، مشروط بر اینکه نادانی یا حماقت مانع آن نشود. محاصره تا رسیدن به «توافق نهایی» برقرار و به طور کامل اجرا خواهد شد. امور باید به سرعت پیش برود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/77263" target="_blank">📅 14:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77262">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">منتظرم جنگ امروز تموم شه بتونم بگم این جنگ عین کاگان بود، کوتاه و کصشر
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77262" target="_blank">📅 14:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77260">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbm5OGDsGn8G4mYAMHRkOZhSImhTtf8wBQY07MwSyyy5yNTI0LzMTWUN1JPeeFS2Od-bKcfSCUbHG2oKxViUDti_iv1bUHeZ98_mJZbUnTK_3ebprqqQJs72QBL88iLlCVF3tsAeyDiVH-NemRJRAy_vELjCppymX5dEQ8rmA59bq17vsAb1Rf97r0oLuyraF_YhBrQgv0_hAb-BOrU_joH616AKWh6odUtdct4p-H_9Sgv2NyUDAUnfMNc0ajXLokbVMSTQHYSoXWHKaRutLXwxmgeBKLBBwlvR4IQY8E3bDstnAm1Clyqqvc64XLmlttullXFUuHIqUNli946Jiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرا امروز خداست
😂
شهربانو و الهه منصوریان چون الهه تو مسابقات انتخابی تیم ملی باخته حمله کردن به خانه ووشو و الهه منصوریان با چاقو میوه خوری خودزنی کرده
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/77260" target="_blank">📅 13:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77259">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">آموزش پرورش :
جنگ تموم نشه نهاییو مجازی میگیریم
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77259" target="_blank">📅 13:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77257">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iAOHoryigP5Nb_G8YBSBHa1LgEuSURa_BS-Mr43rPRVlj6AfXrHvkxPnUH38nubD16uFbdXAFNWAKz8m_jo8mOr5Cu3irs9pxxxNQUZuFkOJdD1ArqW7MFs2tkunIu62Dur5RawG23xZ_sk7m0Yx9IRVIcFn6dIliAjynhGahPYFG4UFj3H-1NWu4gxwGXrvsD5yZcfWVsL07yGlOptXEvHETIz_oBmi5BgXOERGEw55L1Wdy-AxTPpHeLAglhO1zXiWPhIYrfugh6c2t4-KzgJmUSkLl_VC_pW9ARpEEAMzA-v8SPHZp7SBKe2-tCbK2jL1bes65wBJN5Y3NJMprg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ag-T5-K81j2n3tElKW3an3WK2gp2hUEEYS9QgNA78qpBS4XwaDW6HcI4TAQXBAcQbS8G6nQQa1A5vqS--kMMyp1Hf9mgT5IPYd7MIl0hWfWMgcaB4WvtI7p-rsFkbN0LmLtkWsWwboBMtvS42q1242PMS3iHSY40inkcxyzfSFfEEKTTNtjP_ohnqK-6jkT9U7lSp0d75PQRYXq2C9dXv-LM8a7yiVK3784OPAT14r_CiQuLYWNkr1jzat_t7UEz0DX8ZfjpZQ8AbVpqp-odySPLIMqM4GCpdnJy-6ror_EeEJK3sfCzbSY23BgxyjiHP9u04QA6Yswdt28G-lesAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دارن فضای جق زدن هم تو اپلیکیشن های ایرانی براتون میسازن دیگه چی میخوایید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77257" target="_blank">📅 13:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77254">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خاتم الانبیاء :
زدیم دهنشونو گاییدیم اگه باز بزنن میزنیم
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77254" target="_blank">📅 13:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77253">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اگه میخواید بفهمید کی ترور شده کافیه ببینید تسنیم میخواد از طرف کی بیانیه منتشر کنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77253" target="_blank">📅 13:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77252">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Gashtam Shab</div>
  <div class="tg-doc-extra">Alireza Roozegar</div>
</div>
<a href="https://t.me/funhiphop/77252" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آهنگ مناسبتی برا کانفیگ فروشا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77252" target="_blank">📅 13:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77251">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اینکه نتارو قطع نکردن مشکوکه، میترسم بیان گوشیامونو بگیرن ایندفه
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77251" target="_blank">📅 13:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77250">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ :
ایران و اسرائیل باید هرچه سریعتر جلوی شلیک رو بگیرن
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77250" target="_blank">📅 13:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77249">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e98d055a5.mp4?token=UMij0N6RrzLx0fC86L8FI2rxIjCwMKl0OiysImFy5OgqRcpB8pcfa5wcmn_hk_y9d3SOOlNGeYgbWaWTgwuoW85oVVKNQLLv8QQY3V4OVoM36Xz8Oj9H6HLlw78oy_B_NJqyVwzWGbf6Xx1eBT9UnleKL-SvvHY__PU0CcjwuGP4EzLz3RT6nlzFw6IDf8U14vamy4l_0tcfn68KC5zzbtxJAGqGPJfcsiqptnUwNGonC0XBMtC-ksOzRoGLtHJvmHvrI0NVpERa_xPMOZsEoWa-r0Aj4bkiv_Zau2DbxN6Y0m1Kp_Pa02TDd50hHvbEILzUkr7VrySubizreTEoSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e98d055a5.mp4?token=UMij0N6RrzLx0fC86L8FI2rxIjCwMKl0OiysImFy5OgqRcpB8pcfa5wcmn_hk_y9d3SOOlNGeYgbWaWTgwuoW85oVVKNQLLv8QQY3V4OVoM36Xz8Oj9H6HLlw78oy_B_NJqyVwzWGbf6Xx1eBT9UnleKL-SvvHY__PU0CcjwuGP4EzLz3RT6nlzFw6IDf8U14vamy4l_0tcfn68KC5zzbtxJAGqGPJfcsiqptnUwNGonC0XBMtC-ksOzRoGLtHJvmHvrI0NVpERa_xPMOZsEoWa-r0Aj4bkiv_Zau2DbxN6Y0m1Kp_Pa02TDd50hHvbEILzUkr7VrySubizreTEoSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو دوربین مداربسته از حمله خواهران منصوریان به دفتر ووشو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77249" target="_blank">📅 13:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77248">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ بیداره و واکنشی نشون نداده فعلا به ایران و اسرائیل
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77248" target="_blank">📅 13:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77247">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">بیایید برید از این کانال پروکسی انبار کنید که اوضاع خیته:
https://t.me/+IJWzPBxj-zJiY2E0</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77247" target="_blank">📅 12:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77246">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">رسانه های اسرائیلی خبر از ترور سردار سپاه، احمد وحیدی میدن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77246" target="_blank">📅 12:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77245">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رسانه i24 news:
ارتش اسرائیل تصمیم گرفته عملیات «غرش شیران» رو از همون جایی که متوقف شده بود ادامه بده، به‌جای اینکه عملیات جدیدی رو آغاز کنه. ارتش این رو روز ۴۲ عملیات «غرش شیران» محسوب می‌کنه، اونم بعد از یه وقفه بیش از دوماهه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77245" target="_blank">📅 12:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77242">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kdOdUYrCRBOgLyH7inKhVSSHDOn-38sejuePkCcgFmYuRsM2aE-mM11ZG5fkrLz7OWfBfZ_WdIC0bNDM51z3F05mXjcQ28gXi-Hm0MQeBb2cv9sey7BDKWdDaC31LqcbT62O3uXhBFiQK5qaZpilQ-eAi2dl2GFxOHrYiqAY6aXkFkR4Oij_FAphpPNoaJSMW06UV3GretCWotmzy0vKniQKgti3Yxyp-_MVT4LrokHLlTWZBoGak8hiXIkvYhHeKzkx3YuTJipcHwIypeFEfW-1k9IFCW-g8pnqla_Oi9Qh9-6e_UDLxtONmDQoH4EttvI8Dz_vb78dl50pgryVlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ofCy_kID5dpfshQ4RZRqi7BNLUyD3qbozm1eJ-09V8N910EGBJmK0LHvZD3E78A4nFfeimFiKnY03OOxbfmeEdVqSqlcbGxuKdNGqDLOG_5CQqak-YyzNRKqP9CqvlOCBtazyUKk-8kRDe1WOUE4E-42_YbfAOygV4Hu9rbW4eCqyzMo_L04HBik3ZPayzUEf7WtOYG0YeMhZiI1OryfowoPn3nBr8PDujvzSdWTpVOuhee_kVTMJ0jrzWEaM5mGmFZ0ej1NxxBNKBpcAJUgLWXHyhO5k4T4EzK6YMl35qqZm68g3q5xeiZ7F1MY5GmYz9QRapXx4uE8Hn6f5W7d4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tcpemnPDqGqwEyW-2DzsJMSvzaXD0Fyt2GYvSR4JbK2PRNbxtcTEBVUYVlVSr_zmklMcKcC-TkKOc__E9CJaY5n2qEyi5-eQCt4MPYDRwFhkv7iReTWZv4VBs-tJxFcvirWPpYkSvgy0eDV_CSliTlx6ItIbH0PclM2PNQtsS3eLNo72-aDjomZlFRmdGJc0lok_i2vgNkQeSgeMKIjIb4LanwH4lsmi62iwoXylkz_IjnC0C1H3L_UH_YLH62AvZhwPGKtikmB9OyzNyweOGqhmj5zlVHsdquon6TjDlZKwkudTS6G9j_qv0AYadD1FPZ_rdIfHPt7GU7BauIYq3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این وسط که اسرائیل داشت ایرانو میزدن، خواهران منصوریان فرصت رو غنیمت شمردن و اتک زدن به دفتر ووشو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77242" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77241">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">رادیو ارتش اسرائیل:
ارتش اسرائیل برای حداقل چند روز درگیری با ایران و احتمال یک کمپین طولانی‌مدت آماده می‌شود.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77241" target="_blank">📅 12:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77240">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سازمان ملل:
we are nigga run
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77240" target="_blank">📅 12:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77239">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پارکینگ های زیر سطحی به عنوان پناهگاه برای شهروندان تهرانی در صورت تشدید تنش ها در دسترس قرار خواهد گرفت.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77239" target="_blank">📅 12:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77238">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">صابرین‌نیوز: خبر ترور و شهادت فرماندهان سپاه کذبه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77238" target="_blank">📅 12:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77237">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سفارت هند در تهران خواستار ترک فوری شهروندان هندی از ایران شد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77237" target="_blank">📅 12:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77235">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بنیامین نتانیاهو با کابینش جلسه امنیتی گذاشته.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77235" target="_blank">📅 12:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77234">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پتروشیمی کارون خوزستان دوباره مورد حمله قرار گرفت.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77234" target="_blank">📅 12:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77233">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">تیپ 10 "سیدالشهدا" سپاه پاسداران در کرج، هدف حملات ارتش اسرائیل قرار گرفت.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77233" target="_blank">📅 12:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77232">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترامپ کونی رئیس جمهور هم مگه انقد میخوابه، پاشو دیگه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77232" target="_blank">📅 12:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77230">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دانشگاه هوافضای عاشورا رو هم زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77230" target="_blank">📅 11:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77229">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سگ زرد چجوری الان آتش بسه؟
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77229" target="_blank">📅 11:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77226">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">لشکر 8 زرهی اصفهانو زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77226" target="_blank">📅 11:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77225">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">تسنیم میگه تست پدافنده.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77225" target="_blank">📅 11:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77219">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">فرید جان سلام ما کرجیم صدای انفجار اومد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77219" target="_blank">📅 11:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77218">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e1f36b08d.mp4?token=IrAXYJ4x-cfi3xdckawCDS-gdkbnLHPUtkjxQ9KMKr_SFAbzKtSOwMXM3N0yEpiBjcsEbhFVTulFNdl7AxaeZWzpVS2eMdmUhuBQQreL9g9CoTVUNUsVurYPU7RnSrE2YPiXn3kFcCGlxQHI7tgvCSuZ7cwQ-FZpapTkzpEsKC6l7Ztky5DLBnOffNWzRK48gR30imT3XhLHuCtBfILmzZfm3xxljsnQFog85HYb2y6jthTIeFJi36Xm-Og6kt56lFgrYQoI-nvIb6G--YpqLBIzcO5i3pyPHitU_MFW0cx73CZyfYXIraPAZFvPVHB6EfYUo0wdeLbn70Ti7ukqYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e1f36b08d.mp4?token=IrAXYJ4x-cfi3xdckawCDS-gdkbnLHPUtkjxQ9KMKr_SFAbzKtSOwMXM3N0yEpiBjcsEbhFVTulFNdl7AxaeZWzpVS2eMdmUhuBQQreL9g9CoTVUNUsVurYPU7RnSrE2YPiXn3kFcCGlxQHI7tgvCSuZ7cwQ-FZpapTkzpEsKC6l7Ztky5DLBnOffNWzRK48gR30imT3XhLHuCtBfILmzZfm3xxljsnQFog85HYb2y6jthTIeFJi36Xm-Og6kt56lFgrYQoI-nvIb6G--YpqLBIzcO5i3pyPHitU_MFW0cx73CZyfYXIraPAZFvPVHB6EfYUo0wdeLbn70Ti7ukqYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ وقتی بیدار میشه میبینه نتانیاهو دیشب گفته بود نه بابا کاری ندارم هرچی تو بگی ارباب ولی همین که خوابیده شروع کرده به زدن:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/77218" target="_blank">📅 11:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77216">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">صدای انفجار در غرب تهران
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77216" target="_blank">📅 11:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77215">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d92631652.mp4?token=f0YIksxFucuzrWDufD1FadpYJDd1RZkP7PATVhXSHYS35jTX9mws7k305sRKm-UIOkoSKqQqDo3onMfCgoDeIbZXPtPzlJLXKohZQBNCxYht8TQyV57Ta9Qjz2nqNC3jfry-GdDxX9t3199E71Hn9aPO1vzcgdp3nI81Jr2OtduHJapH9WAhQY3p1SqJ-B1OOwavDQPmP6RnH0RlTooMZzimvxhE1B2fvB2_-_kQB-1W6ffR9Cx2kld_AF5-A4HQ7etizZoiiS4QCgx6DaNTiPPKGWd2FY5VzUxTydYFuuyAqPkvjVq44ml2z41QNlmEvPeP7vHeBuVvjB-z022kgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d92631652.mp4?token=f0YIksxFucuzrWDufD1FadpYJDd1RZkP7PATVhXSHYS35jTX9mws7k305sRKm-UIOkoSKqQqDo3onMfCgoDeIbZXPtPzlJLXKohZQBNCxYht8TQyV57Ta9Qjz2nqNC3jfry-GdDxX9t3199E71Hn9aPO1vzcgdp3nI81Jr2OtduHJapH9WAhQY3p1SqJ-B1OOwavDQPmP6RnH0RlTooMZzimvxhE1B2fvB2_-_kQB-1W6ffR9Cx2kld_AF5-A4HQ7etizZoiiS4QCgx6DaNTiPPKGWd2FY5VzUxTydYFuuyAqPkvjVq44ml2z41QNlmEvPeP7vHeBuVvjB-z022kgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77215" target="_blank">📅 11:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77211">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اطلاعیه روابط عمومی سپاه پاسداران انقلاب اسلامی:
در پاسخ به حمله به یک پتروشیمی در ایران، چندی پیش به یک پتروشیمی مشابه در اسرائیل حمله کردیم.
اخطار می کنیم؛ دشمن صهیونیستی با اقدام علیه اهداف غیر نظامی و هدف قرار دادن صنایع نفتی، بازی خطرناکی را شروع کرد، که دامنه آن کلیه اهداف انرژی منطقه را در بر خواهد گرفت و عواقب آن برای اقتصاد جهانی، بر عهده آتش افروز اصلی این میدان، آمریکا می باشد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77211" target="_blank">📅 11:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77210">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">نیروی موساد و آمان انقد بدبخته که با یه نت بستن شما نتونه به اسرائیل اطلاعات ارسال کنه اخه؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77210" target="_blank">📅 11:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77209">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJObP_YgjYGXYKTeA_vYTwU7RK4omDx-xHoj0wHvg-E9cuS3ziLjgC6vUEUyKpgyozuLnR7EJbV-NFzLgvDt3_m9HbMf1C6j1Hd2KnmS_ydfn-NecqFvuIMPCVhEU0Y0VpegDQ5CE8K_tR_-bEufpteu07EYVHrp5PKmuftxi-FhY6CufWT-D4ALn-1IQh3qH9BP2tM4ImNESbsQjbjMGSUoKpoaEFapxcyLINCbivBBd0tHMGq7DsMd9OYrUEUGvCJQtjQQNXaEznwiPRgtpBOoBYFU_0pPu-1yBKUAw58xIjzgtqxMGu-CMYlFEHIKA8Vjo2QQ7mBewI8P9dk-Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقیقا نمی‌فهمم منظورش چیه ولی از اونجایی که چند ماه پیش به یه بنده خدایی گفته بود زهی خیال باطل احساس می‌کنم خیلی حالیشه و در آینده خواهیم دید چه خواهد شد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/77209" target="_blank">📅 10:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77207">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سخنگوی وزارت خارجه:
آتش بس نقض نشده ولی اگر اتفاق دیگه ای بیافته که بشه، ما آمریکا رو مقصر میدونیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77207" target="_blank">📅 10:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77205">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">۴۸ ساعت پیش ترامپ: در آن قسمت دنیا آتش بس یعنی کمتر بهم ضربه بزنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77205" target="_blank">📅 10:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77204">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a26mXtgatzCnDHZ2kq4JEdkwcw6oCV_RoixY2u8ji2mTwq4k42TWuQt5LnCg6XfuNGUn-98FZ6fxxuZV462eVwv1nt61jt_wBKcNxlc9_SxNgO4iaYbSK1LkdGzhIoHP1u6H76l-Ob9NRkRsr1OWFEmoweZQO-ebjzdJ7u4r0yQWpB5eJzC-Ezr-PHel_O1b92eG60ECT9rhLGBD7j-FNd7e12IOYWbLwzCTxgJ6L5Rt5AGmpmBrTXYD_rJUswD58Jk2iWL7agQK9uxEyts7laUpmyH9X5Z-Km2YMn50jspglBK3r7-VP56Z2ni-qnWSbMasvGLJu3dniLm7DSZrPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتحادیه اروپا:
پدر عشق است لطفا جنگ نکنید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77204" target="_blank">📅 10:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77202">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">تا اینجای کار کشتی فرنگی بود، هروقت آزاد شد آتش بس نقض میشه</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77202" target="_blank">📅 10:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77201">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نگفته بودن آتش بس زنگ تفریح هم داره</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77201" target="_blank">📅 10:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77200">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPZgBEV98bWg7iPnSbUonJeYssUJtZqJhRRNOoJa4_heTRV5dqy9KDzrQtSE97q7JD2uVJizN89iC09lbd7kBftOOtBT-rklVMx2tLFYhU4X-854zkkExm6J0wk2rQrjhZHz-5k_RW7QlWqFubSgjhakvGz-46KH5fX9iMP5_OM-8_YRbNqR-HzoPoeCpi5bBeS8MHTxA21zt_MIkpaUSwN9alpBmedv5a5-mlDVnuBIoVj8drYG-AVqzTBtxkipB6olG-CBgKn3qmf54PxVj-p24vjmwo1Iw_koXgVMObH2xqpgFVelYeb2WnfWQacOGh2CzgcLE9sxS9kRxmEPUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
خو اومد زد، آتش بس رو ادامه بدیم بازم میزنه خب یکی بگه ما چیکار کنیم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77200" target="_blank">📅 10:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77199">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اوه اوه جالب شد، انصرالله یمن اعلام کرد تنگه باب المندب بصورت کامل به روی اسرائیل بسته شد.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77199" target="_blank">📅 09:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77198">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0472fc5f3c.mp4?token=ZRRi_ZEvNDhJo9ZbEac6rjloJpsnosrYXZ_zOTL4YhBYQxBJS-fbFSbM_mh2_GHMVZOMNGGjarkl1Z9BNOkyHLS1oicRlW9d8_HWWrb_ikZ1aeTbgC_xv6hwamuoHuwko84xUCFDRM7hZkHeuJ1zsvjcATyrhLlQmkpkJTr6hNADN355AtuJekpnw3avGKCNZjxB7AVDiR1HRUAkCZgNILE1F6j0TIr5W4SmOpng88zEDqwb9G5aFpZzfh4cTf1-f4BVpedIPIJOqQKlXyUGM-KhZjYUmVZUOgvMKDyvaiU1613DT7ztwMHRRxMIytbTa1i_hejl90I5XrJuWXWPzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0472fc5f3c.mp4?token=ZRRi_ZEvNDhJo9ZbEac6rjloJpsnosrYXZ_zOTL4YhBYQxBJS-fbFSbM_mh2_GHMVZOMNGGjarkl1Z9BNOkyHLS1oicRlW9d8_HWWrb_ikZ1aeTbgC_xv6hwamuoHuwko84xUCFDRM7hZkHeuJ1zsvjcATyrhLlQmkpkJTr6hNADN355AtuJekpnw3avGKCNZjxB7AVDiR1HRUAkCZgNILE1F6j0TIr5W4SmOpng88zEDqwb9G5aFpZzfh4cTf1-f4BVpedIPIJOqQKlXyUGM-KhZjYUmVZUOgvMKDyvaiU1613DT7ztwMHRRxMIytbTa1i_hejl90I5XrJuWXWPzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ به عاصم منیر وقتی میفهمه دارن همو میزنن :
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/77198" target="_blank">📅 09:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77197">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">شما رو نمیدونم ولی من یکی خبرای جنگ و این که کی کیو زد بکیرمه</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77197" target="_blank">📅 09:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77196">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pA40nHyjGqnk9_MtPkc1UN-Z_NLtIk6T4o2c0DRz28Zuz5eMx0QGDVjVA1Njt6hhLsPXxSQz8lqo3xKpoOPKmNTWWX52QX1iYskxQIEUISA6TUaCOj1QQtLb8KTfoTOog39a-DgmJw8BYvG4KghRX7VH700GN09844Zi2aQ6l5xNJry80hVh4IZTAZdGp92YDMVvjFhEtc9bJqfq1T9pPb-IMSz1cPEq19LQKFoG7CKlMR57VPT0BIZpocB9S6hehbEDw4DG5pmCFfumWs54qpsCU4O-yfwCyM7KLBmUoD82Hr6t-fAD0QQfsF4k-1xIvmUkJE67deRE3SKZnCfNJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وحید جان گرم کن بازی تازه داره هارد میشه
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77196" target="_blank">📅 09:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77195">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jeQpdLr0VcRMwjU-xIA1G_CIKT9Ezi0_W1cuxVylCUKMX4RbAz0xK0MJTyfj5UusSpums--K9ZAfTDpC5p7_b2iUy1YEDOVlapaE8TlmGsHxLoBBd63KbpaETuZjsUrjxqsFhIhd_I5dH9Tn6u-xV9a_dQdeuo7fP04EricSzGa0PYO1YAEs6gflhqLyMMkPoUXkhDZaomLOWf-Hqs4eyRXapUo5aJp0-FXB3GOpm03t9NPv_G_qDkrsrWO7XEtHUMfQ9-cCyABwH4TX0Hz4QwcIZwXOrD3LUMzP5qktu5PETdK6ah7tWlB0lD3G60AoWI9nQrtGjxAFzDNjUpOx-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
فرانسه - ایرلند شمالی
🏆
رقابت‌های دوستانه بین‌المللی
🌍
🕔
دوشنبه ساعت ۲۲:۴۰
🏟
ورزشگاه پیر مائوروی
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
فرانسه در
۱۰
دیدار اخیر خود،
هشت
برد و
یک
تساوی کسب کرده و در
یک
بازی شکست خورده است.
✅
ایرلند شمالی در
۱۰
دیدار اخیر خود،
پنچ
برد و
یک
تساوی کسب کرده و در
چهار
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر فرانسه
۳.۲
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر ایرلند شمالی
۱
.
۹
گل در هر بازی بوده است.
🧠
شرط ممکن است ناموفق شود اما مدیریت بودجه‌تان هرگز نباید شکست بخورد.
👍
ورود به سایت با فیلترشکن
R18
🅰
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77195" target="_blank">📅 09:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77194">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اسرائیل هیوم: حملات صبح امروز اسرائیل به ایران با هماهنگی آمریکا انجام شد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/77194" target="_blank">📅 08:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77192">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">تایید نشده  گزارش‌ها از حمله اسرائیل و انفجار تو مجتمع پتروشیمی کارون خوزستان.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/77192" target="_blank">📅 08:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77191">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">تایید نشده
گزارش‌ها از حمله اسرائیل و انفجار تو مجتمع پتروشیمی کارون خوزستان.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/77191" target="_blank">📅 07:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77190">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">موشک ها به سمت تل آویو شلیک شدن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/77190" target="_blank">📅 07:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77189">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ایران داره جواب حمله هارو میده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/77189" target="_blank">📅 07:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77188">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سید مجید نقطه زن سریع دیس بکو ارسال بکن
منابع عبری: انتظار می‌ره ایران بزودی حمله موشکی کنه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/77188" target="_blank">📅 05:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77187">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دوستان بخوابید خبری نیست</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/77187" target="_blank">📅 05:07 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
