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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 13:59:26</div>
<hr>

<div class="tg-post" id="msg-77323">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">میگن تا الان یه نفر کشته شده 22 نفر هم زخمیه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/funhiphop/77323" target="_blank">📅 13:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77322">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/c0fbfca63c.mp4?token=dlTAySJzy6dQL-h6-x-LLhKBs1B-Y9CqISGxJd4SaBi958QGntda_CzbXeFD-Qg5V52GBk_3VMzgdGvBwEZW_c33Fcsc5OyMoiURTeUeQ3Mpw_Jk_l8ZMfZhXRQX_voPF2IMaXVjLcrL1sNUHRv3xKjXg10eId-jviD2LYG8DZilKAJeDzXP9Sgl4zMnEllOt-oBpKHfs_aQkNH2Q43s93Jd9T_hi-jTu3HYbSY_lyB5UTA21sW0CIl_4gdvdiBfJ5xq6vB8GjgrF1EPrEAlzNj1h1K2Pyd_Xj2bG1loBKU3QH4ke3weIzdmZ4s9CNAf7aikWpLkOD-ETPpO-LFoAA" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/c0fbfca63c.mp4?token=dlTAySJzy6dQL-h6-x-LLhKBs1B-Y9CqISGxJd4SaBi958QGntda_CzbXeFD-Qg5V52GBk_3VMzgdGvBwEZW_c33Fcsc5OyMoiURTeUeQ3Mpw_Jk_l8ZMfZhXRQX_voPF2IMaXVjLcrL1sNUHRv3xKjXg10eId-jviD2LYG8DZilKAJeDzXP9Sgl4zMnEllOt-oBpKHfs_aQkNH2Q43s93Jd9T_hi-jTu3HYbSY_lyB5UTA21sW0CIl_4gdvdiBfJ5xq6vB8GjgrF1EPrEAlzNj1h1K2Pyd_Xj2bG1loBKU3QH4ke3weIzdmZ4s9CNAf7aikWpLkOD-ETPpO-LFoAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگن تا الان یه نفر کشته شده 22 نفر هم زخمیه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/funhiphop/77322" target="_blank">📅 13:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77321">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">تو افغانستان اعتراضات شروع شده نیرو های طالبان هم هر که رو میبینه مستقیم بهش تیر جنگی میزنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/funhiphop/77321" target="_blank">📅 13:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77320">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/if_N7PsXwbzsvaWgRKENC64A_W7k9R7z_Kcj0E4kUsIhP83fh1xALGCu0DNEB74E33APN-gsHOQ75xCdZA4KEBFcNwSw4ASKtgBHOEh8alc25gHVSh5XXCC_KGtEMOifAQipUhpAbk4hDk2s6lRtm-wFTs8oAV1x8hmR_q9tYHPvwwVFXR3X2DfxQyNo8j-0Uvq7y3_eo7T5R3JpxAE27yUip-4F5in_mcAYNXKM6oyTrSYHIEPUW1j_Y_p9z1WnYAIzkn7dIliyB81NjyFnjPbQJysoJTAmJO5M8PyFKM3kPW-K317ZaAWrgsY2o0GxpBjVLtJLUr1FfNsDCYAG_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین حق‌پرست، از معترضین دی ماه به اعدام محکوم شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/funhiphop/77320" target="_blank">📅 13:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77318">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">آتش بس vs آتش کم
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/funhiphop/77318" target="_blank">📅 11:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77317">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
ترامپ در واکنش به سقوط یک بالگرد آپاچی آمریکا در نزدیکی تنگه هرمز اعلام کرد هر دو خدمه آن سالم هستند و کسی در این حادثه آسیب ندیده است.
به گفته او، جزئیات بیشتر این حادثه در گزارشی رسمی منتشر خواهد شد. هنوز علت سقوط این بالگرد مشخص نیست و احتمال نقص فنی یا عوامل دیگر در حال بررسی است.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/funhiphop/77317" target="_blank">📅 10:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77316">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">شدم مجنون مشهور میدون شهر و کیرخر دهن مارو گاییدید.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/funhiphop/77316" target="_blank">📅 09:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77315">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/77315" target="_blank">📅 09:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77314">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/funhiphop/77314" target="_blank">📅 09:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77313">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMXuqdbaWwKz2W1_E0gYCH1mCYTK-W5c_9DPIaJCC2H7MklcLzDAbYTmMIo1iWPmWAdDQL5qzU9LKA9GNM_KRtR152SesdjqZVDZgbzhC-8oHSnDQcpoC2HxvZ4VZkehjIpH1ufjiIECMoNGIFyNS2gxIH-Y-jtnB2UPhIRF4ej5hQmk7SSQK0FuVZhKGDTirVYu6f0Aao96zdklO0Pt8G6_cnM5sHNzqDfn2LfXHHsG_Unmn13-1bzCe_YTq7uTblotRHZbPoOOqAUTjfG9bOso9HAPB-htbnZldCNRUAXYJQw3PX5-JKROY118DJsurUS22K4-YC0Q6LjHllSH-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کصخل این که ایتالیاس
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/funhiphop/77313" target="_blank">📅 09:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77311">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اعزام لشکر  82 هوابرد معروف به شیطان آمریکا به اسرائیل
لشکر ۸۲ هوابرد ارتش ایالات متحده در اوایل آوریل به طور مخفیانه به اسرائیل اعزام شدند، به عنوان بخشی از برنامه‌ریزی مشترک اضطراری بین اسرائیل و ایالات متحده که از فوریه تکمیل شده است، برای تصرف جزیره خارگ تحت کنترل ایران در خلیج فارس و ایجاد قلمروی ساحلی در داخل ایران، طبق دستوری که کن کلیپنشتاین دیده است.
این دستور که در ۷ آوریل ۲۰۲۶ صادر شده، به چتربازان از گردان دوم، هنگ ۵۰۱ پیاده‌نظام، لشکر ۸۲ هوابرد - گردان معروف «جرونیمو!» - دستور داده است که به طور «ماموریت موقت» به اسرائیل اعزام شوند، در حرکتی که پیش از این توسط پنتاگون گزارش نشده بود. وقتی درباره تعداد نیروهای اعزام شده به اسرائیل و مأموریت آنها سؤال شد، پنتاگون سوالات را به فرماندهی مرکزی ایالات متحده (سنتکام) ارجاع داد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77311" target="_blank">📅 01:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77308">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiCxHoeYv11iIkV0Pg4iHRKz1aKs8jB9VGvjMZk0Lr_Rt1fAoHMga0PEwVi8lr7O_7CKbtr9H6rEMv45-3e74idDJC2WL89T1emAw4QoD_TYSJ4SUPMyVKyHvcOzs4rk7-2SaG4RFs629uz-SQCmlZuFWpZo9intmtYptFNHRPsN0ktVt3S3W1lfWxsvAPZLkb0-S9ntbg5r45PHWyc4O7p6OEjUZ303_laAxZaIOSGT_AxVNTh_zkSx2KfkyKOtPMr9o3TQ0sNqRVXcOWhlehOYCbukscBxIWP0-h7emqQojpo0oyndCG9CEwmyM0NKHCD7j-DRS7GAsLaSx3cQdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">والا خواستم یچی بنویسم یادم افتاد چمن و مهدی میرن گونی خودتون تو کامنتا جواب مناسبو بدید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/77308" target="_blank">📅 01:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77307">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ به آکسیوس:
ایران به شدت خواهان توافق است و ممکن است به زودی توافقی امضا شود.
این توافق مانع از دستیابی ایران به سلاح هسته‌ای و توقف غنی‌سازی خواهد شد.
این یک توافق فوق‌العاده است.
ما همه چیزهایی را که می‌خواستیم به دست خواهیم آورد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/77307" target="_blank">📅 00:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77305">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">یک مقام خیلی مطلع و بلند پایه ایرانی به الجزیره:
آمریکا مدام پیش‌نویس تفاهم و خواسته‌ها و شروط خود را تغییر می‌دهد و این باعث سردرگمی و عدم پیشرفت مذاکرات تا اینجای کار شده.
بدون آزادسازی پول‌ها و رفع تحریم هیچ توافقی انجام نمی‌دهیم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/77305" target="_blank">📅 00:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77304">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">یک مقام آمریکایی به آکسیوس:
نتانیاهو برای بقای سیاسی خود در اسرائیل نیاز دارد که جنگ ایران ادامه یابد، و ترامپ برای بقای سیاسی خود در آمریکا نیاز دارد که جنگ ایران هر چه سریعتر پایان یابد.
این تضاد منافع پیش‌بینی آینده را بسیار سخت کرده است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/77304" target="_blank">📅 23:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77303">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اردوغان خوشحال شد
سپاه به مقر تجزیه‌طلبان کردستان حمله موشکی کرده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/77303" target="_blank">📅 23:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77302">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGyWJ2mYVYPirU6gEnlhYP78eQ5DF886bcWGXVtf5qTY-dqowaHOGdxQIoWxzQPenxhJHpW-ds3yPtnvF6kD19QcPWD9myAjtALu8AuK1VZANkqVafdTkdDC6OXVIjKlUjkS1fN4NL3cii6fGWYUIwrcScbQ-4a5hEkn40f4jeC44BtyoFgikJ5bYjetritAt3zHyVmCgt2pwg9n6yQ1M3Cz-rvCervl_Y157PzxiLZVVHbakv2hK46-GK3xFn7ueDA1W3Y01ValD7vhUK2sKvxuRGXQxWE9pLMDGmnwvn2WR7x2Kj3OdKxuUVfAlpKdXHKngFTytkBe7nMm1FZADQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان هر چنلیو دیدید که اینطوری میخواستن خودشونو مردمی جلوه بدن و بگن ما پشت مردمیم
باور نکنید، اینا مهره ی نظامن و هدفشون اینه تفرقه بندازن!
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77302" target="_blank">📅 23:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77301">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">تنها جنبشی که از نظر علی خدابیامرز درست بود جنبش سبز بود
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77301" target="_blank">📅 22:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77300">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یادتون باشه که تمام جنبش های مردمی سالهای گذشته هم راستا و مکمل هم هستند
اگه کسی خواست این جنبش ها رو در مقابل هم قرار بده بدونید که به هیچ وجه طرف مردم نیست
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77300" target="_blank">📅 22:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77299">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sry10_PhNl8cKpHn-HCH-FMO_0ffLLfPj_61X5rNI0HYIIxBG_tqHG1PNW1GotWYozzdj-YLfbV1f1Z5Y4j-rGtFFnNhb4jwENOHXvXaImDqOE4yLDD-PvlZX4Qfe8-sisFWv_PRh6j76ShGMWj57a65_JEzqJmGxzz4TYYDll3Cv4HFGKlBqjly4_juoyO77Xj7icjPjQ3GOe0YZZbnadylsmtfUjquWCwLb_01ePG0i6c-LZlzrtDh7hJvX8e4RLz4OS2KCUjV_3uLxYv3eiKZaJSyWRQ9bZVn_tu9ZKbYxLDxOWp40fYA6d8RuYP7h8HmwHnvP9EkxSG9vqX-4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیل اینکه که گفتم جنبش زن زندگی آزادی درحال‌حاضر مورد استفاده ی اصلاح طلب‌ها و امثال فردوسی پوره، یچیز مثل همین اکانته
🎒
و طرفدار وطن پرستی با بیو "زن زندگی آزادی"
که همون قضیه ی ملا به ماتحته‌
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77299" target="_blank">📅 22:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77298">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">شهید واقعی زیاد دادیم سر جنگ عراق
که اتفاقاً اونا هم جاوید نامن و جاویدنام باقی میمونن
حالا عراق کی بود؟ دشمن ایران
۵۷، برنامه های انقلابی از کجا پخش میشد؟
رادیو تلویزیون حزب بعث عراق با مجوز مستقیم.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77298" target="_blank">📅 21:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77297">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">رادیو ارتش اسرائیل:  ارتش اسرائیل قرار بود در ساعات آینده حمله‌ای بزرگ به ایران انجام دهد که شامل ده‌ها جنگنده نیروی هوایی بود که آماده برخاستن و هدف قرار دادن اهدافی در سراسر ایران بودند. این حمله گسترده با فشار ترامپ لغو شد.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77297" target="_blank">📅 20:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77296">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ به کانال ۱۲ اسرائیل: به نتانیاهو گفتم اگر جنگی تمام‌عیار علیه ایران آغاز کند، او را تنها خواهم گذاشت
من دیشب از نتانیاهو خواستم که به حملات ایران پاسخ ندهد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77296" target="_blank">📅 20:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77295">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پدافندا بیدار باشید باز ترامپ داره می‌ره بخوابه:
یک مقام ارشد امنیتی اسرائیل به کانال ۱۴ گفت که بازگشت به درگیری شدید با ایران ظرف زمان کوتاهی تقریبا قطعی است، احتمالاً در روزهای آینده.
هشدار بالا در هر دو جبهه دفاعی و تهاجمی تا اطلاع ثانوی حفظ می‌شود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77295" target="_blank">📅 20:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77294">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">می‌نویسم امضا می‌کنم آمریکا برف امسال رو نمی‌بینه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77294" target="_blank">📅 20:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77293">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1pMKSYMFDTSvl1Ury6dygW6XUTUzxj_rrIjr8aVloa01Qdqaz9jpbSyR4ohbNCMu9oNbHtpFuYpSl1kys84J3SrCggokBO77MJFcYutLg0c3VIS8Ro05eVsN8kxEpkUCzxGr3Ga2btoJ6sEV2KCW3NkfmtP0ikfhMPt2i0jn_2UBM4aPeylhYIPkSg_JlTiXjfFAsehJr2pMnz2EBEIeV1VQuLayn3rldvjl3TWQi4VM1eTZWHHZW7h49uXmzZ5M0oNE2OI6F2fVmJ6uTLKr0qGbKcuE7AvKVcwnlJTZi8HUH5a6nST1ZY5BZLm8RIWF_zuvusx5FEks_R1ejwlnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان عجیب پروفسور بقائی، سخنگوی وزارت خارجه:
تحقیر نهایی آن‌ها زمانی فرا می‌رسد که درمی‌یابند سلاحی که برای تسلط بر دیگران ساخته‌اند، از بند رها شده و اکنون اراده‌ای مستقل دارد.
در آن بیداری تلخ، فقر واقعی قدرت آن‌ها نهفته است — و آغاز سقوط اجتناب‌ناپذیرشان...
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77293" target="_blank">📅 20:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77292">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">رادیو ارتش اسرائیل:
ارتش اسرائیل قرار بود در ساعات آینده حمله‌ای بزرگ به ایران انجام دهد که شامل ده‌ها جنگنده نیروی هوایی بود که آماده برخاستن و هدف قرار دادن اهدافی در سراسر ایران بودند.
این حمله گسترده با فشار ترامپ لغو شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77292" target="_blank">📅 19:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77291">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ:
حاجی نمی‌خوام چیز کنما ولی انگار یه احساسی درونم داره می‌گه ایالات متحده و ایران به توافقی نزدیک می‌شوند که راه را برای مذاکرات بلندمدت هموار می‌کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77291" target="_blank">📅 19:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77290">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8RCFdpozWckLkd8mfiFlgL82LSW_qME1pB92GQ7QCKoLAfKa6OwTeVbdh5i9Wq-rlslYVSVVgdazVMTqDHgCh3diF-G4o4udQlh-6Kfm8dj022PNxhulGojddlf6FeP_eyZGGAXuT4QqyfOdiTsSnChMKX_XFtrmNpiTH7pfw-6ouXaN47YR5TLytbXmU_4Iq2vEyWwifdIYQ2kZOAVkSpv5pSFOcNfXFELQp_EKo84mT2zeq3fO_sY_x0Yf-wkglFAHN9VrTQzJ5mEJQodWoLvNbnMelFA7OtP2qMFJrMHJdFQkwaWroYWo4hsrV_H50f6IfeOcySM_gW0UlbiDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77290" target="_blank">📅 18:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77289">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">انگلیس از شهروندان خودش خواست به اسرائیل سفر نکنن
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77289" target="_blank">📅 17:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77288">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3rfZY_erNcvp1prpAIHy2WKrH6WggaHRNJexJA-bBBpsv9yFiJRrsGDqVvC6vkSyn2WBRPx80SL3f2HVDwOWRI56kzWllS9cXvk0nmz1Oc3DOBwBlUL-kHQCoToT87pYPLeAD4E1rqUKBH_uZG3UBV1llXDEM22FidKVoFL8_nhadcDY7ZZZMLCrEPvw2hC03y_BXYgk1gNB8CScWptbirADCqgGrcVtR-SDF572xvXge6HcdSHKwvD6EOOH9CzhwP6J6_T62M5beCVTX_zliTxRvar5QY70tWlpcZt1vEf3xalSAmvj2-w-LYHxwlsP2avI0awiscjptNAQ_XltA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنوب لبنان
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77288" target="_blank">📅 17:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77286">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gGbVnnIz9OXa2-0jdjkHmwgePQ5SescZjUObbGIyJ20aTw3dUZgINoVa68NXZ41GFt_2j1eIXV7hdIVz2TVAog_RnVan2xGwN96s0kwBLLLb7X-ofPjmpfStEQURYptgYIr2rqdGB7VInTR9LAzf7vebwsccuqUhLxqg1mTCYHeBQlbJR9J_dGFU6AwhMuo9uUrG7Gm1yZ0INOsMmgq1apVTX_s5MUL8BHdPljYPk9xpigpH8ynq2L3d8ANuv3zKDa8aTJm1xeyhgtOAzLABvnioqriCFSpRnRHdvGdIURzLgWWp7M3ZiQV2LPeqaDT-GjWg2sYlfCX5SNmoaVdscw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PhI_BJ_fzaCQXmbLrNQLW6qAl7Lrcqoh5qy6rjeZqSpjTqcLi6FzWpPuf19UCN7c_F7PVHLUwDZ45KMAKw6I9t40xo3LdYR5onWdTec9utLh9J0KM1hRN7VPkZiJsm8mA9KQtBPe23BJI1nFYCjlqD5N9WLjteZDru2WmrRdMHhJ7obcD-lRle6-XQJYkI1dqJ4LZ4w_ViqCWjAeMVxhUyxrFf-5LRxZ5v2O81g53Up05Gjfz6HaGe8tPudHhNfDvLik3kt4jWQuFZEZepy1r0S2mwThSCU9nVZuBIeDQuC7mNiUD6ZnjCzGyrNwEwwsaxFVjaqcSebFs3m3xvAerg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نعمتی که از دیدنش 10 سال محروم بودیم
🫠
🥲
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77286" target="_blank">📅 17:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77285">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/77285" target="_blank">📅 17:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77284">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/dkklmn0cUriCd1Ih5rNCllqNfg6pH9bGWTMNkjLysqIXbb9ly4O5-Ky_nINb4SdlxzXVURQzcTbYqte6B9xh-td6vB4TXTDh4REjbTy1PLVfm2EWKMnUI6kT20VVIMk1Qu6IW1Qxw1S4jD1H0ke8R1tmdt5SeVhwcWo0L4y7jKkhfnNadCV4DMYPS4bTYEqkbWxGO2Lkv5RjIv_I_F6FiBq2rZc636Z9DG6RBGP0f2mOZaalXmengX5li70PMRR4f7p_e-S_0MWLmbXdE-E9cwsSmzU0MFtLEqAx2uCnHV4atRMp8cLBgn9RE7-qFXTOnffEP9lL1miyh1zeQ4vb2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77284" target="_blank">📅 17:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77283">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHkT9nFRtvjQPeUASCcFwbl8fyWZP8WDMTiAfBrz0v1aczwsQmNdRGvKLut60LZwL4mI4nre-H5hz4r142CvZqbMmQu-C6oaeGUdhY8kPrnZM79LBuBzCNOqCjWxTji8ctB1KMb0-R8nZHinuTRBQ3cldC9USWpx-X5CDnUjhl2dleTT9tJw5TJ0lB4UQ-KxoJG9waiTaFncWibP_-QuJJewFP9xGiYp4FnQGoVBzefXv-RzjXmhEf__R4tzzTjdSDMdpY0GUUhESxoELId-6_khUtz926hdOD26XXyjyEHZKEk35h9mD14AB9BN_6HNsLKR5Hne_GAOP1WnRnAn2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قصدم این بود برخط باشم، دستم خورد رو زبان ترکی تازالیخدا بیردایمیش شدم
@FunHipHip
| Constantine</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77283" target="_blank">📅 16:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77282">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLnUvsRHXpSj9Dr0vHGZGrS0RwdyidHcZh5mBWZ42NCLSuY7bX2sFDNWMet4FNek6zX0sJhic7hF7dsSw_5RIV0krrH8GVcVJc5fXmDEJWfLRV3Ip7Lyb4I7I2rM1mlBJLvhqqHvY8MoJq2cd_DFm3--L4GvP_fUxsJK-uBcujkfyCZ7f-QouKBKrwa3dCsTW5NQ7gcd4OVC79IIQhw5aqiy7Wk_jgVTxATcjKKg_kNk7GP_aG5yoOUNBQTkry0EhVau01pXEE-k_j7c-HgrMFSM9CMjlg_Pf2j9bYTV31eSemKl4mG4M5DjQbwJ9u3qSKL9JvYj6Qyk35l4-n7ozw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استهلاک کمرم هزینه بردار بود
آب هدر می‌رفت چون بعدش باید دستمو میشستم و از مایع استفاده میکردم
هزینه ی عمل دیسک + ۱۵۰ میلیونه
و برا همین خم نشدم که بردارمش
فروپاشی اقتصاد ایران به روایت فان هیپ هاپ.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77282" target="_blank">📅 16:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77281">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بچه هایی که خارج از ایرانید شبا که گرمتون میشه پاهاتونو از پتو ندید بیرون چون ممکنه ی موجودی به نام سروش ولی زاده برای اینکه خنکتون کنه بیاد پاهاتونو بخوره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77281" target="_blank">📅 16:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77280">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qP6hEL-OfogYDd5a_aX5yBG_-veFVfyNWGqbTUxf4hhBoi1S33cNNrlI-LJJeW_ZoidnoOtvF8Rc4OEx4EhThrxAcGdspVgWNrXRgQK0OTyKiCLt_mjbn-M5SWg9QhmyFmB1MGyDiHDY9mnRvayQ6XD9_r4CioH_DlhF38_iiiZJ_189Nh_Jn9DeBYg1cudWKrld_0Zlpn11AEozHYieWhRgTpV4sDTsr0h1vN5uleNNKBOMc-Nw9pYzrHqw46HHlI6xuwWt4LxCrvsYISCgRsdBYj-FU2yO-nTejtFTbAhCzTh-DEiJC60IxUNTUZZCf6xMi0yu-RyYVpS76GlYCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان حاجی پاکستان
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77280" target="_blank">📅 16:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77279">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">الان ملت چجوری به کانفیگ فروشا توضیح بدن مودی نیستن شرایط و تغییر میکنه فقط</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77279" target="_blank">📅 16:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77278">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8BV4ovJaPSQ4tVyu0EBLkP0Vy4arhSBpQugHU12Oz9VQOVpnu0hgr7D2qBAKanBHFYchizZXeDIJzoXJrdWIRltig-5LBvM02VykSqbr505X_5x5Hr2u3fsgH5hJO3O6j4uokpx39fEijAPrOvktIZ7gvc1plOUzhdTDns5uRZzKECekS6_yTNmSmsLMnzp0rF0gZW11lhGLpbgg54rBcFxjqHv8U_kioXaKn3y0DcX4OWXRfTG-D0JciZ454cC00lKtdSVPWN5bnYPYSMXc5U7xzxcfalHbIr6bJGLvGH3L7k6NRrwRXq2BI5VZBzFPzO9GHc8SamGVHVQxPBOiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید کوروش به اسم
تهران 2585
ریلیز شد.
YouTube
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77278" target="_blank">📅 15:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77276">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77276" target="_blank">📅 15:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77275">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRtMXPDU9yVQglKJvAzMFqxxTdfDBEfp4iDdDu3pvNSJ9Ugwpk9-PF20n09O2veAP82PZk4fE4OPQFOMTZdtzqAbWllFTbDjGoR58VCIr42gtJkhtTu9Ng2-R6vY9x7zWVDfxBZdfBIZwnZYuDvacJ6UH3gfc_tlpibUUG-vwiMJDoSgZe8N9OGl5vgy1onJc9HDqt5rFKqNoXmiUVZvoy0Cqi6JfcQFM9oWAs2kopuE0J9F77hsa6mjGGF0naanY5bnKE5LpFZ8DPP2DrygPl0rboEnIBND1pRqmS3VrKEIjT_Cr2n-D_YuAsB_pCAUM14UOpQtymiF0IZK1t23mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرارگاه خاتم الانبیا: از این به بعد درصورت هرگونه حمله اسرائیل به لبنان (حتی اگه به بیروت نزنه)، ما خودمون موشک می‌زنیم تو اسرائیل.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77275" target="_blank">📅 15:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77274">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxOSz5g5XCegs3Ph-E4GbHbNyRdryo8RKJhORydXqelL2ZOQnW_or6lcYj8wb67-C53M2lHQ64J-BbIjDTzNja1NNzhq70DlNU_bmEEPm38uPZzGK8lDwnvrVsulppgFJyd90-wXjycY0QZAY5saJLV56-Un69USscUsb-B54_KKee4lUcHo_wa5k69IH2mDMZVzQDjfiM8H3pNLxeuHpBN4AhpqUn7eolUrhGo6KuqDZvLZNJ3mZacSz8b43vZHSEtUwgkul1cn7cXO9Db7daoBP8fg-WowdOCwWQM8meHIl-xfwtMzwD9pKEJSnmcj_W6rMMhuHsjmERR32sinxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرزیدنت پزشکیان:
اولویت ما امنیت ملی و آرامش مردم‌مان است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77274" target="_blank">📅 15:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77273">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">قرارگاه خاتم‌الانبیا: فعلا عملیات متوقف میشه اما به جان مادرم اسرائیل دوباره بلند پروازی کنه یدونه موشک میزنم.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77273" target="_blank">📅 15:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77272">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اسرائیل هیوم:
اسرائیل و ایالات متحده پیامی به ایران ارسال کرده‌اند که نشان می‌دهد اگر ایران از شلیک مجدد خودداری کند، حملات بیشتری صورت نخواهد گرفت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77272" target="_blank">📅 15:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77271">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ولی واقعا جواب دندون شکنی به یهودیا دادیم، بخصوص اون بخشش که مقر پلانکتون تو بیکنی باتم و خونه خانواده سندی تو جنگل رو زدیم.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77271" target="_blank">📅 15:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77269">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ولی واقعا جواب دندون شکنی به یهودیا دادیم، بخصوص اون بخشش که مقر پلانکتون تو بیکنی باتم و خونه خانواده سندی تو جنگل رو زدیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77269" target="_blank">📅 15:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77268">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">من کسخل‌تر شدم یا پزشکیان واقعا داره چهره ی محبوب جمهوری اسلامی از دید عوام میشه؟
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77268" target="_blank">📅 15:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77267">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">میگن پیت هگزت به مناسبت این جنگ نصف روزه ۵۰ تا شنا سوئدی رفته
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/77267" target="_blank">📅 15:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77266">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">قرارگاه خاتم‌الانبیا: فعلا عملیات متوقف میشه اما به جان مادرم اسرائیل دوباره بلند پروازی کنه یدونه موشک میزنم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77266" target="_blank">📅 14:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77265">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">معاونت ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور:  نگران نباشید نتو قطع نمیکنیم  @Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/77265" target="_blank">📅 14:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77264">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">معاونت ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور:
نگران نباشید نتو قطع نمیکنیم
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/77264" target="_blank">📅 14:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77263">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttvqWHUrEitPDHhdPBvYb3YC3KMvxEPvd7GIW5Fk-L1a5hJ1EhrwmbRqz8kFuMrZOmNQxQdXnGs1meYveN8vIfix3vi_Re6pxhWPFCeGus2xfkd9R3LcL23_wvsLYvEuMmaGEW3BFKNxAwKwKLHRqhoTHui2BsuGzeePw1uYS2sfAloEiweMk0s14G6STaQ6OmtOVYDFbw_Zq-SxsBaWezmqWli6iXzIFDEUrsvavfbZsHqP5asqXaQEv8d7kKb-ROOKhi0OnYxLhNeakd1utWeYkSDf1d0wlR2zGvwt9j8CV8hWAj3PYMiFsoTpqvyfb2Rq_2Wk2ScXgfjF1bHaIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:‌ هر دو طرف، اسرائیل و ایران، به دنبال آتش‌بس فوری هستند! مذاکرات نهایی درباره «صلح» در جریان است، مشروط بر اینکه نادانی یا حماقت مانع آن نشود. محاصره تا رسیدن به «توافق نهایی» برقرار و به طور کامل اجرا خواهد شد. امور باید به سرعت پیش برود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77263" target="_blank">📅 14:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77262">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">منتظرم جنگ امروز تموم شه بتونم بگم این جنگ عین کاگان بود، کوتاه و کصشر
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77262" target="_blank">📅 14:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77260">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdJYr71tOHvlYK61GhOKUhHr5hHZS0W5Wj4VDb4e7oGOMQ-lma_OwJj2S3IVobKUntyYI1NTtaorjrpzhqiRL_PMaWaw16tuPfpmriYieB0td2_Wb1QIJTmtj3Xp_c2ZPbFbI8wDZOOGxgekqBC9yZN2V7_INamX34IHjQioTLpgbqejOwsuqkOcoJzrMkdSH7BCTJ3iDnZL2fcuokwzs9kuQVT2dlWP6NWNLHOckmoL7xwepRISga6_oQ4gCsPwm2PFt2EoaT5QsAP4kmO-HpfiRsCxmrc8WJgiu4_naxXO0TREyLjW2gjh0IJfcByP9dcQqR4BvAsyt3NPzZBhTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرا امروز خداست
😂
شهربانو و الهه منصوریان چون الهه تو مسابقات انتخابی تیم ملی باخته حمله کردن به خانه ووشو و الهه منصوریان با چاقو میوه خوری خودزنی کرده
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77260" target="_blank">📅 13:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77259">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">آموزش پرورش :
جنگ تموم نشه نهاییو مجازی میگیریم
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77259" target="_blank">📅 13:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77257">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j1-pzw0-G7u7kjsiFqg4LgRI7gty4uGfpK7oELPpGwUyQKBZYOGnW-FF_vNOlMutyD9qewnWKwZ0SEnxP9pKqbw1JTtsxyl0dT6at8CzXhpTAhe6vpRkwY7JV6yAAssae1WyuLGsWtmP1-dHKnhGGHOpbjeFadGOnGcp8u-M5-slx62njxTWzyBhD6FHbZfNzgN2beJh94ultETwsh1EKyO7yge_q4ubS3GvTZcA7Zi-OjkqBETDh51o1SAUWpdpgx-ZTwieJVMon-fEBLIf7q1nVpNZboXXhrxQmu4zsOkDyJcyl_tQ1qOPRAlTG7SVVFl9eaQiqUj4LMD8KmNNHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z7PNBlVQ_UNwQxEMCEwCytfSKB4JPswkR2oVyUO-dZEv7LPFuurblAq6mNryQi-DOOv1zHS7qR51CPaqnb5fbbnnxXQan7Qzswd1PfT1pwsfQnIncEU2mygBeMAswfQ_iWMxGcUnBIQJmVNfKXdgkPJu4nY2wOpbFu5Sx_REoU9Fb8xiz9TIUUSxYvh6mAl4SHfpFP85fUkOzR7UMgCCHror_D5vhYAMqx52VUTiG1OxoONaE85_0GTgzDdHgkC5BJg7sM1l-w5Ze5S2e6Tx3j-QBtybUaYKYj8zrKAxs-NfWzp9gAcP7L_gmGO8sT0_2Hh10FAOGuoW_xvIUeaDqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دارن فضای جق زدن هم تو اپلیکیشن های ایرانی براتون میسازن دیگه چی میخوایید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77257" target="_blank">📅 13:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77254">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خاتم الانبیاء :
زدیم دهنشونو گاییدیم اگه باز بزنن میزنیم
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77254" target="_blank">📅 13:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77253">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اگه میخواید بفهمید کی ترور شده کافیه ببینید تسنیم میخواد از طرف کی بیانیه منتشر کنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/77253" target="_blank">📅 13:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77252">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77252" target="_blank">📅 13:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77251">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اینکه نتارو قطع نکردن مشکوکه، میترسم بیان گوشیامونو بگیرن ایندفه
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77251" target="_blank">📅 13:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77250">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترامپ :
ایران و اسرائیل باید هرچه سریعتر جلوی شلیک رو بگیرن
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77250" target="_blank">📅 13:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77249">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e98d055a5.mp4?token=ppuHwGKNAakY7GwTAXiHTML34EobOhbxwF0YYmgR1wr0XSyP5j5_XqbpbO76EQ1k5dofsgu6ozymwsPtzH8rU2UXfRaJiFRkaQd3cbvqJ1hU6XqeUucXkFz1xFzmCFJ0u7Mwl9nno4KmqO296NIRahIvybFthlzCQfwTN5bIE7Js5afZ6GN-tteN2OCAXbVAJqceC0Pbkm07rYYs2jehcoODjKEAbHa3W6Mwdqo7fe-3bby6qq6WZXaJVTqvmL6bWBsecT70DDyL6mvwtM-dHevcQyeP2gp3lUGktJzvY2mshzZ8MqvU7oIozQj3eTk2YaKy0P7l81oOCzfe5EyeNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e98d055a5.mp4?token=ppuHwGKNAakY7GwTAXiHTML34EobOhbxwF0YYmgR1wr0XSyP5j5_XqbpbO76EQ1k5dofsgu6ozymwsPtzH8rU2UXfRaJiFRkaQd3cbvqJ1hU6XqeUucXkFz1xFzmCFJ0u7Mwl9nno4KmqO296NIRahIvybFthlzCQfwTN5bIE7Js5afZ6GN-tteN2OCAXbVAJqceC0Pbkm07rYYs2jehcoODjKEAbHa3W6Mwdqo7fe-3bby6qq6WZXaJVTqvmL6bWBsecT70DDyL6mvwtM-dHevcQyeP2gp3lUGktJzvY2mshzZ8MqvU7oIozQj3eTk2YaKy0P7l81oOCzfe5EyeNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو دوربین مداربسته از حمله خواهران منصوریان به دفتر ووشو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77249" target="_blank">📅 13:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77248">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترامپ بیداره و واکنشی نشون نداده فعلا به ایران و اسرائیل
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77248" target="_blank">📅 13:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77247">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بیایید برید از این کانال پروکسی انبار کنید که اوضاع خیته:
https://t.me/+IJWzPBxj-zJiY2E0</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77247" target="_blank">📅 12:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77246">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">رسانه های اسرائیلی خبر از ترور سردار سپاه، احمد وحیدی میدن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77246" target="_blank">📅 12:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77245">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">رسانه i24 news:
ارتش اسرائیل تصمیم گرفته عملیات «غرش شیران» رو از همون جایی که متوقف شده بود ادامه بده، به‌جای اینکه عملیات جدیدی رو آغاز کنه. ارتش این رو روز ۴۲ عملیات «غرش شیران» محسوب می‌کنه، اونم بعد از یه وقفه بیش از دوماهه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77245" target="_blank">📅 12:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77242">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dHZXCgfsO0B1LGwaKpOjnG_D7bxkKQwCD57W4NHulW5tUkH52XC50nBQbC-ko6m6bIYr3ikAB0xgUwugYyDLaAc9KcFEHcssHRbEw9xLP1GAxDEt42aoTgKxI5DK8dEwIUcS2PXt32PAj3pMM9v2QaxqVgPGXWlcxDObcYHITVJrItgEBy_OPpTJWmUkqfK01UVIHqK-aYOYAtkWFQplHX0iRuEGOEWjFKWcIH9p05ltUQCwt0JiE5UsbUM4d8lv9eA82YNZ2ASecmPEsOMgAsPcV2NFVCY6wK-dWWzr_weur7nxphcJqA8YRktVvUnHELehfC8m6rKfGHwQUYp3-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jGistgdNjMjYXaZL-n-FJFs6ORryoHxpt-X6U5-4hLcMvk484-YF8uK5xaR8SbQB_IyRxxGroGodVj9CCGlYwdLvUuO6g5tFS-hM9BmNjFZap_8FK9psLA3TlglRvr56u91DecwGv0Fx-oJMO3OJ5nrByYbQoDoUYDUtweOoMLWWb-vDf31VKCdQnlmmVwiGAjl8M2A6G498zIHw4EV58hArEIQpcvsRIqGruVZBbMuxIa4o5h49Po9kqXdh4Lwwiij3vKjFL1uBnoz7YbcpGxI_0eXf-3Z5SZBbpXCwgAj8jyyFZAvrL_Ugwsw-k2CVDJJBc2eNCw5mg8iprsRiJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UA5cCjmcuw4CrK3T0lYfP8fX5-QzUwKN_Z5p9zwQjPk-isD_-d-76V6v_yWhfa3jLc_k7rgKqatIl4-h_sr_Kj9tIuyvhp2hGqXjPAjRduqVToOaye6lQ6vyxwK-Rfsq4-cRpajePiGnk-RdMT-XWpuLfNkJYr1wB3g0RCaLq4uxRXAfvHR7gn9usciaCNoLvsERDLQ5Osmt1fbPPwjSie6ba7M85xc_Mi5GIUwKrumiS0AIETi71vlmw6c6nye2s-VkjVdU53oJu7nUx_t8iFr-h5NRkOZZn1vZNeDzharzHUDHqs1vk7D7UlAfFnpXGf_PQ5LzNaCd87OCKKkkbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این وسط که اسرائیل داشت ایرانو میزدن، خواهران منصوریان فرصت رو غنیمت شمردن و اتک زدن به دفتر ووشو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77242" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77241">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رادیو ارتش اسرائیل:
ارتش اسرائیل برای حداقل چند روز درگیری با ایران و احتمال یک کمپین طولانی‌مدت آماده می‌شود.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77241" target="_blank">📅 12:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77240">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سازمان ملل:
we are nigga run
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77240" target="_blank">📅 12:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77239">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پارکینگ های زیر سطحی به عنوان پناهگاه برای شهروندان تهرانی در صورت تشدید تنش ها در دسترس قرار خواهد گرفت.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77239" target="_blank">📅 12:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77238">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">صابرین‌نیوز: خبر ترور و شهادت فرماندهان سپاه کذبه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77238" target="_blank">📅 12:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77237">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سفارت هند در تهران خواستار ترک فوری شهروندان هندی از ایران شد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77237" target="_blank">📅 12:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77235">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بنیامین نتانیاهو با کابینش جلسه امنیتی گذاشته.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77235" target="_blank">📅 12:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77234">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پتروشیمی کارون خوزستان دوباره مورد حمله قرار گرفت.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77234" target="_blank">📅 12:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77233">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">تیپ 10 "سیدالشهدا" سپاه پاسداران در کرج، هدف حملات ارتش اسرائیل قرار گرفت.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77233" target="_blank">📅 12:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77232">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ کونی رئیس جمهور هم مگه انقد میخوابه، پاشو دیگه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/77232" target="_blank">📅 12:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77230">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دانشگاه هوافضای عاشورا رو هم زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77230" target="_blank">📅 11:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77229">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سگ زرد چجوری الان آتش بسه؟
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77229" target="_blank">📅 11:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77226">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">لشکر 8 زرهی اصفهانو زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77226" target="_blank">📅 11:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77225">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">تسنیم میگه تست پدافنده.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/77225" target="_blank">📅 11:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77219">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">فرید جان سلام ما کرجیم صدای انفجار اومد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77219" target="_blank">📅 11:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77218">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e1f36b08d.mp4?token=FyH9vKUzvRyQDKLOWF8VC9DeBw9Nrt0XSczizRjqXLYnh7dPqTPuGdFjmdw2uxXlqiupwsU0g12pnKdcFP4Kyz5HfSc4l1ptMdCQSJ54R6WE9QAuSp9Vg_x2YWpe5BiCysGZqDMLrpQWneXOGgG833sA6oji66Usd3oPTuWcA2DePG6-a5APM8xB-tRNPTFdQhhpKOZYkSQvHqbTnyIZmR9TANkEPLRQDcumJsMmw4GZ3kAUvqT4VqiIP3sAhkWawnp13nl5EB_3eR6VPjpK4TeqTwqU7wMACwQDx1B07idgNGm8rdN_PMsuD_MhpiT3S3OgjLRk22WeOl96BDVfqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e1f36b08d.mp4?token=FyH9vKUzvRyQDKLOWF8VC9DeBw9Nrt0XSczizRjqXLYnh7dPqTPuGdFjmdw2uxXlqiupwsU0g12pnKdcFP4Kyz5HfSc4l1ptMdCQSJ54R6WE9QAuSp9Vg_x2YWpe5BiCysGZqDMLrpQWneXOGgG833sA6oji66Usd3oPTuWcA2DePG6-a5APM8xB-tRNPTFdQhhpKOZYkSQvHqbTnyIZmR9TANkEPLRQDcumJsMmw4GZ3kAUvqT4VqiIP3sAhkWawnp13nl5EB_3eR6VPjpK4TeqTwqU7wMACwQDx1B07idgNGm8rdN_PMsuD_MhpiT3S3OgjLRk22WeOl96BDVfqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ وقتی بیدار میشه میبینه نتانیاهو دیشب گفته بود نه بابا کاری ندارم هرچی تو بگی ارباب ولی همین که خوابیده شروع کرده به زدن:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/77218" target="_blank">📅 11:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77216">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">صدای انفجار در غرب تهران
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77216" target="_blank">📅 11:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77215">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d92631652.mp4?token=KXQQaUhTxAVIlnEwTMLe6qURK9Aak8olOpnJ7y0nNAF-17gSDTkSlnhq57YxYZOqfoOSa2aI2K7D-RVbwMQe3-4ozatwYJFR5BgEWpw1-6tAMriyI18jlg0MwsWK5A64G2k97aLvknwuczXBFCq-Vw1Jnfn4UD9EoOtgU_0PIISOFQX4L9UBqpRB3yeDJtZ11EjS6dO2pyo5sDRq4P8ce_RZBef2szCj61Ow2qA7mEuG--TTR_gkpPIVVGisRvQ1qAkbl5-z7sIqfcsLtPixQ2ZbW7G0EJUBjUWdamF8h-TUZtnrB57U_AJl35gnscjqAMrxkRP8YjU0TjLvacCdIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d92631652.mp4?token=KXQQaUhTxAVIlnEwTMLe6qURK9Aak8olOpnJ7y0nNAF-17gSDTkSlnhq57YxYZOqfoOSa2aI2K7D-RVbwMQe3-4ozatwYJFR5BgEWpw1-6tAMriyI18jlg0MwsWK5A64G2k97aLvknwuczXBFCq-Vw1Jnfn4UD9EoOtgU_0PIISOFQX4L9UBqpRB3yeDJtZ11EjS6dO2pyo5sDRq4P8ce_RZBef2szCj61Ow2qA7mEuG--TTR_gkpPIVVGisRvQ1qAkbl5-z7sIqfcsLtPixQ2ZbW7G0EJUBjUWdamF8h-TUZtnrB57U_AJl35gnscjqAMrxkRP8YjU0TjLvacCdIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77215" target="_blank">📅 11:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77211">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اطلاعیه روابط عمومی سپاه پاسداران انقلاب اسلامی:
در پاسخ به حمله به یک پتروشیمی در ایران، چندی پیش به یک پتروشیمی مشابه در اسرائیل حمله کردیم.
اخطار می کنیم؛ دشمن صهیونیستی با اقدام علیه اهداف غیر نظامی و هدف قرار دادن صنایع نفتی، بازی خطرناکی را شروع کرد، که دامنه آن کلیه اهداف انرژی منطقه را در بر خواهد گرفت و عواقب آن برای اقتصاد جهانی، بر عهده آتش افروز اصلی این میدان، آمریکا می باشد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77211" target="_blank">📅 11:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77210">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نیروی موساد و آمان انقد بدبخته که با یه نت بستن شما نتونه به اسرائیل اطلاعات ارسال کنه اخه؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77210" target="_blank">📅 11:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77209">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTLQaoY9YOCkC3etKFb-1wpCdglJtJ5RrULSy6wSf5kAARlmSM2HzRG5mxvVnInh31n87G571Pq2x2SERbadW2hcKWy1X7q5G_tXAsXhAi2bEpVu_BFaZs_xqG_UH7Do5mkIt2UF_rmLDasKK5Q_X6dDC5gmFwiScTHcVyij7jT_fzJdbQITRXEtJ2cP0p1ONApI0DAGj9DPlBJoAMNNaRycu5bhQJPH_ZK7l3z9xL2kwCRyvVahtKijg_3hK0R2arojjxFEW5sfmyx7orfDGfii1L0UYzqK7RQvEidKclOj9YUqxurEKmACwNLR_F4L5XjYtfnAF6LlCtwT1llxJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقیقا نمی‌فهمم منظورش چیه ولی از اونجایی که چند ماه پیش به یه بنده خدایی گفته بود زهی خیال باطل احساس می‌کنم خیلی حالیشه و در آینده خواهیم دید چه خواهد شد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77209" target="_blank">📅 10:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77207">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سخنگوی وزارت خارجه:
آتش بس نقض نشده ولی اگر اتفاق دیگه ای بیافته که بشه، ما آمریکا رو مقصر میدونیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77207" target="_blank">📅 10:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77205">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">۴۸ ساعت پیش ترامپ: در آن قسمت دنیا آتش بس یعنی کمتر بهم ضربه بزنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77205" target="_blank">📅 10:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77204">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJhOr_jp1a5gP0lkLB-I7kiYIaCrXTW7JBmeve_wQ1CO6FIAYFmKT4hGiDKWQD7NKkhWx98cgrBXCA_EzAhN1XNTlNKDhZpUnfdcEhvqlponNad_OCW94YNmRQaw-7WNYVbGIUVRYSKpVAN4ToiwT6ydQYbSJLNeaJiK3mK8ky5QhFDW-dY60wEQca4j59VZrmVm3ozqizdvJWc93hX7AyEaO_MZfGrxXx70XX4zVr8YoGA3R6nGPnlB71Tvd8yUg3vTfHADeMA69itBBy0SHEGry2smcc-Q3PUo02hrDzC34qiwspQvAdE6F_oQo0QeQZyva_pfaAtA2FmH7m8QAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتحادیه اروپا:
پدر عشق است لطفا جنگ نکنید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77204" target="_blank">📅 10:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77202">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">تا اینجای کار کشتی فرنگی بود، هروقت آزاد شد آتش بس نقض میشه</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77202" target="_blank">📅 10:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77201">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">نگفته بودن آتش بس زنگ تفریح هم داره</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77201" target="_blank">📅 10:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77200">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMm8dUlSysNdP1sRBvtltq2ofwUvrNtyn2whBE8vRpcwyFt_qF7CiVnWx5GiE7ZAjQbEMxiTe18gMvTiEzjHX11dB7tZc8j83k78__tfE-5C60ZwDBE66ik1VlGoJuX4w-HwSH_2MJgarkjZoxEHSzItWvvEoOLwLChaOssS0e6EQoap5PQ69OM-l71aSc6Zhj5IzFXBSv9PgsxtxZwZVpxY9YBK5ue60eNqUkezpDT9OIxLJgWmR9Dh98rCZhj9-YvzEA6HTNIYvjYVWPY0PJIAlu2WN76MXHUX-3xwiPlRXUttN9XJRzkALN7du5w4_JlM9Xq86sp96cbmo13hFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
خو اومد زد، آتش بس رو ادامه بدیم بازم میزنه خب یکی بگه ما چیکار کنیم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77200" target="_blank">📅 10:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77199">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اوه اوه جالب شد، انصرالله یمن اعلام کرد تنگه باب المندب بصورت کامل به روی اسرائیل بسته شد.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77199" target="_blank">📅 09:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77198">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0472fc5f3c.mp4?token=pvEIFVH_nkFMe8ixdX1E0zCDZ6V9Y5RRAfsdowTpgZqmzKQO4J6sY6zvGZYxSE2D6ADX8z3TdMA1XClbey5QsQtNt7ZVLzgBJG--_YC7mYAkWdXykYWy3RTfdyVL-vcOafudUhCC_2OIbKETRohuJ6sA1OTQPNdzDUhiFMPbqFJyAqTRhrk1epMzC8s38SZpIc6n_4_eFxvgk21Ujta6fQow9wt3L4dj7jna1EY-_bAX6zJI_LDh6JS25ewcn6QfRPIMq9LAjOuphRFEf8l3vfyCXT5KcBWalXb20Vq_-R333JMteYG3rrIJPyON10oZhtmYVHWcwQwwDxSZrAMzhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0472fc5f3c.mp4?token=pvEIFVH_nkFMe8ixdX1E0zCDZ6V9Y5RRAfsdowTpgZqmzKQO4J6sY6zvGZYxSE2D6ADX8z3TdMA1XClbey5QsQtNt7ZVLzgBJG--_YC7mYAkWdXykYWy3RTfdyVL-vcOafudUhCC_2OIbKETRohuJ6sA1OTQPNdzDUhiFMPbqFJyAqTRhrk1epMzC8s38SZpIc6n_4_eFxvgk21Ujta6fQow9wt3L4dj7jna1EY-_bAX6zJI_LDh6JS25ewcn6QfRPIMq9LAjOuphRFEf8l3vfyCXT5KcBWalXb20Vq_-R333JMteYG3rrIJPyON10oZhtmYVHWcwQwwDxSZrAMzhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ به عاصم منیر وقتی میفهمه دارن همو میزنن :
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/77198" target="_blank">📅 09:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77197">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">شما رو نمیدونم ولی من یکی خبرای جنگ و این که کی کیو زد بکیرمه</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77197" target="_blank">📅 09:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77196">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZHODtvtDMcO_CtLXxo1NUZcUWtPccfFUp31y8YQn6m6tWQInrlU4K_4ZvSadnCV70rMR5RGu2ZcEBYVMpSr912X18h8TWW33iHXa-Vyy0xnuBaqylFJ5AYfqXvI_BJ0KnplDRnhC35DkVSxv-oQb18OV2RmHQQdCUd_qv9_82yJ0s-lamA8mWQ6dgA1bCq-j5THvImGu7V9tXXT83hDdnNDfi9hf0X4X7c9ysFjy0zn4GGy8SZezIw82uUQByXN3L2CP-qi_HQxsAhi7BY86U_6Q1al_DoLwb2D2spw2-217rlOtt2-uZuTO827DB4ehf6ACjKHmJFGB9wDKqo6Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وحید جان گرم کن بازی تازه داره هارد میشه
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77196" target="_blank">📅 09:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77195">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJkD6i4OPk3Np1CgxWF80I7aXtnOJLxaH_SvGArL6aS8lLq0MzLiT6KNhE0mhzUib04ATLUGW9jlY-Z5bg_1UBYVxReyNXdDQnYGBDl8AIhST908Ta3sCmms_poaxSinBq7iPtVTnc0m8Mqx9FfD7rHHgnFC1zxXco0lvHbGuoUUmKrv--WKvA0tPHU8kLNFDlIgv9D1dTFTI7cQNekIj5Vf99Lb-qMffPlfNitU3ODGej30Xn-QaUHn39lRIxVJ5_jT1SL7yF3kEwAGkFz0NLMv58E2w0nx30ixpW6FVHIxL4pvKJ0L1456caOGt2iF0-5hR2tQvhgsEbFboaBWkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اسرائیل هیوم: حملات صبح امروز اسرائیل به ایران با هماهنگی آمریکا انجام شد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77194" target="_blank">📅 08:07 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
