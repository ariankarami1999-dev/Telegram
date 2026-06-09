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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 16:54:32</div>
<hr>

<div class="tg-post" id="msg-77325">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تاثیر معدل یازدهم مثبت شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 705 · <a href="https://t.me/funhiphop/77325" target="_blank">📅 16:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77324">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">یوتیوب قراره رفع فیلتر بشه.
@FuunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/funhiphop/77324" target="_blank">📅 15:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77323">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">میگن تا الان یه نفر کشته شده 22 نفر هم زخمیه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/funhiphop/77323" target="_blank">📅 13:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77322">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/funhiphop/77322" target="_blank">📅 13:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77321">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">تو افغانستان اعتراضات شروع شده نیرو های طالبان هم هر که رو میبینه مستقیم بهش تیر جنگی میزنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/funhiphop/77321" target="_blank">📅 13:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77320">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/if_N7PsXwbzsvaWgRKENC64A_W7k9R7z_Kcj0E4kUsIhP83fh1xALGCu0DNEB74E33APN-gsHOQ75xCdZA4KEBFcNwSw4ASKtgBHOEh8alc25gHVSh5XXCC_KGtEMOifAQipUhpAbk4hDk2s6lRtm-wFTs8oAV1x8hmR_q9tYHPvwwVFXR3X2DfxQyNo8j-0Uvq7y3_eo7T5R3JpxAE27yUip-4F5in_mcAYNXKM6oyTrSYHIEPUW1j_Y_p9z1WnYAIzkn7dIliyB81NjyFnjPbQJysoJTAmJO5M8PyFKM3kPW-K317ZaAWrgsY2o0GxpBjVLtJLUr1FfNsDCYAG_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین حق‌پرست، از معترضین دی ماه به اعدام محکوم شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/funhiphop/77320" target="_blank">📅 13:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77318">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">آتش بس vs آتش کم
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/77318" target="_blank">📅 11:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77317">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
ترامپ در واکنش به سقوط یک بالگرد آپاچی آمریکا در نزدیکی تنگه هرمز اعلام کرد هر دو خدمه آن سالم هستند و کسی در این حادثه آسیب ندیده است.
به گفته او، جزئیات بیشتر این حادثه در گزارشی رسمی منتشر خواهد شد. هنوز علت سقوط این بالگرد مشخص نیست و احتمال نقص فنی یا عوامل دیگر در حال بررسی است.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77317" target="_blank">📅 10:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77316">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">شدم مجنون مشهور میدون شهر و کیرخر دهن مارو گاییدید.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77316" target="_blank">📅 09:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77315">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77315" target="_blank">📅 09:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77314">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/77314" target="_blank">📅 09:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77313">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMXuqdbaWwKz2W1_E0gYCH1mCYTK-W5c_9DPIaJCC2H7MklcLzDAbYTmMIo1iWPmWAdDQL5qzU9LKA9GNM_KRtR152SesdjqZVDZgbzhC-8oHSnDQcpoC2HxvZ4VZkehjIpH1ufjiIECMoNGIFyNS2gxIH-Y-jtnB2UPhIRF4ej5hQmk7SSQK0FuVZhKGDTirVYu6f0Aao96zdklO0Pt8G6_cnM5sHNzqDfn2LfXHHsG_Unmn13-1bzCe_YTq7uTblotRHZbPoOOqAUTjfG9bOso9HAPB-htbnZldCNRUAXYJQw3PX5-JKROY118DJsurUS22K4-YC0Q6LjHllSH-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کصخل این که ایتالیاس
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/77313" target="_blank">📅 09:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77311">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اعزام لشکر  82 هوابرد معروف به شیطان آمریکا به اسرائیل
لشکر ۸۲ هوابرد ارتش ایالات متحده در اوایل آوریل به طور مخفیانه به اسرائیل اعزام شدند، به عنوان بخشی از برنامه‌ریزی مشترک اضطراری بین اسرائیل و ایالات متحده که از فوریه تکمیل شده است، برای تصرف جزیره خارگ تحت کنترل ایران در خلیج فارس و ایجاد قلمروی ساحلی در داخل ایران، طبق دستوری که کن کلیپنشتاین دیده است.
این دستور که در ۷ آوریل ۲۰۲۶ صادر شده، به چتربازان از گردان دوم، هنگ ۵۰۱ پیاده‌نظام، لشکر ۸۲ هوابرد - گردان معروف «جرونیمو!» - دستور داده است که به طور «ماموریت موقت» به اسرائیل اعزام شوند، در حرکتی که پیش از این توسط پنتاگون گزارش نشده بود. وقتی درباره تعداد نیروهای اعزام شده به اسرائیل و مأموریت آنها سؤال شد، پنتاگون سوالات را به فرماندهی مرکزی ایالات متحده (سنتکام) ارجاع داد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77311" target="_blank">📅 01:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77308">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiCxHoeYv11iIkV0Pg4iHRKz1aKs8jB9VGvjMZk0Lr_Rt1fAoHMga0PEwVi8lr7O_7CKbtr9H6rEMv45-3e74idDJC2WL89T1emAw4QoD_TYSJ4SUPMyVKyHvcOzs4rk7-2SaG4RFs629uz-SQCmlZuFWpZo9intmtYptFNHRPsN0ktVt3S3W1lfWxsvAPZLkb0-S9ntbg5r45PHWyc4O7p6OEjUZ303_laAxZaIOSGT_AxVNTh_zkSx2KfkyKOtPMr9o3TQ0sNqRVXcOWhlehOYCbukscBxIWP0-h7emqQojpo0oyndCG9CEwmyM0NKHCD7j-DRS7GAsLaSx3cQdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">والا خواستم یچی بنویسم یادم افتاد چمن و مهدی میرن گونی خودتون تو کامنتا جواب مناسبو بدید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/77308" target="_blank">📅 01:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77307">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ به آکسیوس:
ایران به شدت خواهان توافق است و ممکن است به زودی توافقی امضا شود.
این توافق مانع از دستیابی ایران به سلاح هسته‌ای و توقف غنی‌سازی خواهد شد.
این یک توافق فوق‌العاده است.
ما همه چیزهایی را که می‌خواستیم به دست خواهیم آورد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/77307" target="_blank">📅 00:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77305">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">یک مقام خیلی مطلع و بلند پایه ایرانی به الجزیره:
آمریکا مدام پیش‌نویس تفاهم و خواسته‌ها و شروط خود را تغییر می‌دهد و این باعث سردرگمی و عدم پیشرفت مذاکرات تا اینجای کار شده.
بدون آزادسازی پول‌ها و رفع تحریم هیچ توافقی انجام نمی‌دهیم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/77305" target="_blank">📅 00:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77304">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یک مقام آمریکایی به آکسیوس:
نتانیاهو برای بقای سیاسی خود در اسرائیل نیاز دارد که جنگ ایران ادامه یابد، و ترامپ برای بقای سیاسی خود در آمریکا نیاز دارد که جنگ ایران هر چه سریعتر پایان یابد.
این تضاد منافع پیش‌بینی آینده را بسیار سخت کرده است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/77304" target="_blank">📅 23:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77303">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اردوغان خوشحال شد
سپاه به مقر تجزیه‌طلبان کردستان حمله موشکی کرده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/77303" target="_blank">📅 23:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77302">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGyWJ2mYVYPirU6gEnlhYP78eQ5DF886bcWGXVtf5qTY-dqowaHOGdxQIoWxzQPenxhJHpW-ds3yPtnvF6kD19QcPWD9myAjtALu8AuK1VZANkqVafdTkdDC6OXVIjKlUjkS1fN4NL3cii6fGWYUIwrcScbQ-4a5hEkn40f4jeC44BtyoFgikJ5bYjetritAt3zHyVmCgt2pwg9n6yQ1M3Cz-rvCervl_Y157PzxiLZVVHbakv2hK46-GK3xFn7ueDA1W3Y01ValD7vhUK2sKvxuRGXQxWE9pLMDGmnwvn2WR7x2Kj3OdKxuUVfAlpKdXHKngFTytkBe7nMm1FZADQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان هر چنلیو دیدید که اینطوری میخواستن خودشونو مردمی جلوه بدن و بگن ما پشت مردمیم
باور نکنید، اینا مهره ی نظامن و هدفشون اینه تفرقه بندازن!
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/77302" target="_blank">📅 23:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77301">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">تنها جنبشی که از نظر علی خدابیامرز درست بود جنبش سبز بود
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77301" target="_blank">📅 22:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77300">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">یادتون باشه که تمام جنبش های مردمی سالهای گذشته هم راستا و مکمل هم هستند
اگه کسی خواست این جنبش ها رو در مقابل هم قرار بده بدونید که به هیچ وجه طرف مردم نیست
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77300" target="_blank">📅 22:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77299">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0pDo8m01_r7I8yFIwfxwbM_4_su_haSJ_N1B_van9Vl5qyMqrsMV4TBhnzxXKINZ_PqmEhCmnRQFbbeqo-hNaGCCQ2pLtdWCFmz1fnZVmVM_slfVrVoSKm8iLwFb3FTcOh5e-ZU0UZjceC9WlbsZdb_kJySphSCVSuT3q7wehC8M0bPZRkRYnJaeYz34623BS7Wl_uQkrVqfGt_o_rDXFCD5j4rAJf7HWw-Jhri9j2t56RkyOk1ecoicL80Y2RLkyXFDWLhDEq_Udt-R4KGPn4YqORSAVmWF4_lbQTzC33mnGRzCglS-tVR7mJ_t8YaXaJS-kpKYT3lzsRlYgp39g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیل اینکه که گفتم جنبش زن زندگی آزادی درحال‌حاضر مورد استفاده ی اصلاح طلب‌ها و امثال فردوسی پوره، یچیز مثل همین اکانته
🎒
و طرفدار وطن پرستی با بیو "زن زندگی آزادی"
که همون قضیه ی ملا به ماتحته‌
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77299" target="_blank">📅 22:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77298">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">شهید واقعی زیاد دادیم سر جنگ عراق
که اتفاقاً اونا هم جاوید نامن و جاویدنام باقی میمونن
حالا عراق کی بود؟ دشمن ایران
۵۷، برنامه های انقلابی از کجا پخش میشد؟
رادیو تلویزیون حزب بعث عراق با مجوز مستقیم.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77298" target="_blank">📅 21:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77297">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">رادیو ارتش اسرائیل:  ارتش اسرائیل قرار بود در ساعات آینده حمله‌ای بزرگ به ایران انجام دهد که شامل ده‌ها جنگنده نیروی هوایی بود که آماده برخاستن و هدف قرار دادن اهدافی در سراسر ایران بودند. این حمله گسترده با فشار ترامپ لغو شد.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77297" target="_blank">📅 20:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77296">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامپ به کانال ۱۲ اسرائیل: به نتانیاهو گفتم اگر جنگی تمام‌عیار علیه ایران آغاز کند، او را تنها خواهم گذاشت
من دیشب از نتانیاهو خواستم که به حملات ایران پاسخ ندهد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77296" target="_blank">📅 20:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77295">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پدافندا بیدار باشید باز ترامپ داره می‌ره بخوابه:
یک مقام ارشد امنیتی اسرائیل به کانال ۱۴ گفت که بازگشت به درگیری شدید با ایران ظرف زمان کوتاهی تقریبا قطعی است، احتمالاً در روزهای آینده.
هشدار بالا در هر دو جبهه دفاعی و تهاجمی تا اطلاع ثانوی حفظ می‌شود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77295" target="_blank">📅 20:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77294">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">می‌نویسم امضا می‌کنم آمریکا برف امسال رو نمی‌بینه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77294" target="_blank">📅 20:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77293">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7HFh6uSAg-Xacq2191nEgjIhnANo2nta292ITyE0HDIkvPCOVtpym4uSqYlF-UcmufymocUHmp_luI4_RWPXL96LR7jD6F3sBtYtG4t_leo7XuaC16r5tTotWDy5hDE6eAsGaaRD3ht7qb07zN5QSwRIYLLNF9WJs5zse_XfFTizCwi7gUmrDxf5XTj7Q30EFpZMjmt9vb1Hnj3Fh9OCzXg7w4ov2b5EhAcI2ixLe5HicvGFuyNW5OW0zE7r2PmJAeH9Pc5iTVt9yFuMMXxe9S8aOXDWmdnyQ5kGyuV-r2pSdIMPiz47eXt6VIJk6zN4KoVE1hdc_a8SgXlH1BIHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان عجیب پروفسور بقائی، سخنگوی وزارت خارجه:
تحقیر نهایی آن‌ها زمانی فرا می‌رسد که درمی‌یابند سلاحی که برای تسلط بر دیگران ساخته‌اند، از بند رها شده و اکنون اراده‌ای مستقل دارد.
در آن بیداری تلخ، فقر واقعی قدرت آن‌ها نهفته است — و آغاز سقوط اجتناب‌ناپذیرشان...
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77293" target="_blank">📅 20:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77292">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">رادیو ارتش اسرائیل:
ارتش اسرائیل قرار بود در ساعات آینده حمله‌ای بزرگ به ایران انجام دهد که شامل ده‌ها جنگنده نیروی هوایی بود که آماده برخاستن و هدف قرار دادن اهدافی در سراسر ایران بودند.
این حمله گسترده با فشار ترامپ لغو شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77292" target="_blank">📅 19:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77291">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ:
حاجی نمی‌خوام چیز کنما ولی انگار یه احساسی درونم داره می‌گه ایالات متحده و ایران به توافقی نزدیک می‌شوند که راه را برای مذاکرات بلندمدت هموار می‌کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77291" target="_blank">📅 19:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77290">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWxOkat7pgZra_4OpT_hMxzgxzKM6lcWSehPZN-sY0QNcBkmURlQXI0NBdoiMgfVgDOLrTqWTveRX2gCFFuWjnn_iTsFOdMz-vBsTHXJthOIwWu9lj_d-xwPHxyjtzNk6FTYRsNfL5GcN81NQ-wjILwfNiDw46yi8Q9A5gARVpk6ODoCpdHamizV78Bncblo99G3-xkwJzuA_pyIIb7pF08ggEKiNAlpz-6tgNDOpNxxj0bchkE-HUlxn_R4b-GCW4VkFNAx22ZnHnpctYxBIgxY0X5PcAEbtg5T2EEsODCwqIgyl3fl1OLx72Vionj6CAxLkFnCegkLbnq2clMDiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77290" target="_blank">📅 18:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77289">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">انگلیس از شهروندان خودش خواست به اسرائیل سفر نکنن
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77289" target="_blank">📅 17:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77288">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYp5mIDOU-_ugXdF-lDEbEGXO2uUXwbYUmZbvgFq032cyUS-9xcGIEsI5UVDcSqpcCYR9BZHPG74N-W6i42cJTHVL8j2hc0H1nrl60Ih3JtPMOP4MV2Jq-Tag8QdVdLGQgmRmEwqCtHGcAZ6_TPN_w-PDIreyMALRELpivLKANkdApEstYGT86hgLNH2fKt2EtsRKnjUOReO8IgixCZ2lFNFhwXHXS-dTEQs-Uwiu2VEvnT9npY7wzIEdV_R6nwSuXuoVSP2Egvwf67gNAoSRhClrugUY2ABdxcOhPfnf9_6NKu42kWkEfpVq2fNCnNvJNzZxuuO8buigg58Ul64KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنوب لبنان
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77288" target="_blank">📅 17:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77286">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YSjMAwaNnyQn001OwgSpJYppUW0v7qHKTayatvQ7CoAsppMmSvyS1nEvVDmtwkllRTZHtVonID6fZixr_m--GzgTn1fVdw_xpu3rx-tnjbUdtxASXgZxNhWvHlR0bQjkCk8Q2eRlw4z4NjVNRscGjyoD1uvLTtdkHWpEXA4TyaEB-KEIrYN35da4AjnVw4DFe1zvg8kdyH8gGZOYq6VAktooujmJBMH7hWNrsMztHKsZLEX9kV2wue7nG6edIS8WlWOfMZTuHSDpxF9JM2VENUVfE9clgaDCGSmo_63CYXE2el_TLwZPOeXc2O7dhfV2Nnbiq9ZBHnoCrj93ZCcqXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HA89AbttBOERscKc-To2fRPrWQHdnudmxJUkL4lLtwin3xSdRf5haCPfiBKfSbUD9rjtDx4oKyDAeQSYRGSi2zNKS0QpuftIQX8CigHfAT9eA5HW-rNg3ir2IrvgkkdPrDnVww485HHwmvgsjJbdCwW_qzZk1bnbXndN6eKTGTNeVZSHfal3CjCSUpsxbiF94tfSZkG6Xzsb38QIMaEiVthaCf62KGSIz3d9p8HqT_M_2kQAtPpaDou-eu76VwjWsKa5H7H3cctZcVSfwqx5-AHFmsr_npn6t1JKsEs8IwOm72VjgAKQyOINadWau7S6d2JESwKPFfSwTD23dGwCJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نعمتی که از دیدنش 10 سال محروم بودیم
🫠
🥲
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77286" target="_blank">📅 17:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77285">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/77285" target="_blank">📅 17:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77284">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/hlEJmIWDqucNc83I0g5zgiPYzZlKugzcEpc9d1tOQcB8IqL-KpFY9XK3VyTqeSB0wVFfR1jl6IactPA8top3ZKeY2DwmNG4-jKBlvcYfwYVpYN6R8L1zLJ2VAIXgtwtsL-JUaEYNkTGcjPcRlC0ljANTH5aO7h4BAgmpQuCTJzoCPg1vTQBinHFw664zDpH_8WMJnP3wUUsrVKCmC4cx6ocbRixfQjYfBDhObTrBM4HeRiQ0Yph9qqOCaeO769FtFbARDOtQjuXJ3yhwcnUEtmYVcJI4W-G32508brrfkPrxcH92pTUC2Stdh6zRUY33vngNyCe4D3NfIS3TlcLy7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77284" target="_blank">📅 17:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77283">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_dAbfN9poggnSfOLWSi-tp-nsTsYr6r8ykiFo22HrRjffWGM6dZWSVVctsAtbuYtU6Yb_nI1MeUEAMGP0XH69JScpcudsFdGPvMzZdD6tQ5z35ZSp8TfK-mjJMtW38aDyn_RNfIfqQucdBoaaLT3oev5Wj5_AE2Qxknb_yghPwJ0LAnfP0KKjcExan_LYU8KW9Hy1HK9F6a3_gbdJcJ5Q4M9gMUg3c2za20-ZfDRG1CY0P43ddQoe_koGgOOQedpKV700Qz8eY1262vuzCCpw-vM9-BN4EPuxcHjVBz1-j4-W5e5m5UChHEv4I7tPP2AEq14Zi0fZsODmtss94zeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قصدم این بود برخط باشم، دستم خورد رو زبان ترکی تازالیخدا بیردایمیش شدم
@FunHipHip
| Constantine</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77283" target="_blank">📅 16:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77282">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btVv50hOoLT-HhKSDpZMMPA4bWTEPkujItoPyqHu85FSM3-tpPx9Hy26rTu0FPA50DvJjg-q95-y97QJWi4GbgXdyPD1Cvcr7YaF75Z-Y4ZMM9dxuc2lGmRWAzrc6cO8rtsxmPmyeR649dx5Ng5yoLbdptEOHKUy5ZUmYMGQntJ_wZsx3-D4KBvIaJVClmsQ9y1K3V2pZyS-WubcIYDfrDhCIdcxVb2kX6OBy6v0Hn-Rop3q7GhhxiUC8GRH2Dg564Z8jIPLzPkqwoYngwhi3NVdr-1qr4YzaL8houCMlCuTzfbnxoWxcB17G-j06LTuQFBvbcj47_U0pP6Mzx-7pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استهلاک کمرم هزینه بردار بود
آب هدر می‌رفت چون بعدش باید دستمو میشستم و از مایع استفاده میکردم
هزینه ی عمل دیسک + ۱۵۰ میلیونه
و برا همین خم نشدم که بردارمش
فروپاشی اقتصاد ایران به روایت فان هیپ هاپ.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77282" target="_blank">📅 16:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77281">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">بچه هایی که خارج از ایرانید شبا که گرمتون میشه پاهاتونو از پتو ندید بیرون چون ممکنه ی موجودی به نام سروش ولی زاده برای اینکه خنکتون کنه بیاد پاهاتونو بخوره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77281" target="_blank">📅 16:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77280">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBWXR7gO9NBLHVJGIc5xLoFdQKFiCrJXClmgJQQfviap7mGAwi7I1TyzINtCtk2IZNK0KtsilBXJZBIlXdszQw4eOiNT__Dg2p-a5T8iq9ezJ2ZaT_N5BLFkzBcnANc13w2RuH8Hd9WOqL4uvXso0cImPe5iOjKEXuGLO60CtXTOdoW4BjEF6IdFWn0CRLhqMCzawMzL2You2SUOChdOjBwcuYSXfB9OliLoUihQZT5STFOoRWRH-PaRdRdxdSiaFtaKk5QeIuyBlKyLM57NGTuKs2DFE2-zJxFAYAOcA25VUH1vADVuRu2udsA32xlOl9eYmIA0iFhRvHU5E76Lhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان حاجی پاکستان
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77280" target="_blank">📅 16:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77279">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">الان ملت چجوری به کانفیگ فروشا توضیح بدن مودی نیستن شرایط و تغییر میکنه فقط</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77279" target="_blank">📅 16:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77278">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r79G9ZK2gDTzHlLt-qow2t03qJLAgYAFt9g7099qC3kspUannpkNWGvXs3PqZEjTx1TWlFefR43zVwp03mKUn9wg2SwUZnVRLnGGH_sUh9C_jOoBJhAkqN9FcwrESmUWr8lYrRvpZeE5z-Z15IjiU5aDOuje8yx1g4ztrvLWQ19kNt7lPu2vzrwt0k9Z0bs2srafnOIIrZpKd8lDVHeULTwSzWTlPOHN17at7nIUUjca4xWlgj206fL-iwLBSNt9BgFFrm4Fl2eqNQ1a9nCgQ6WjbNLzUtAg6Pk4JHUc5UO_uVenI60Bciwe-_MCrHV5PBJGu9s0Yv_0zqRuhjNzXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید کوروش به اسم
تهران 2585
ریلیز شد.
YouTube
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77278" target="_blank">📅 15:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77276">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77276" target="_blank">📅 15:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77275">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGtp82rfFdjcTZgVpqnmHWLrVDoBBInf5XrSXkfiJnq_vW7l53rGmQkv-_bNK4GyIliH-Zoo7g-GwR7nYco-JWPhsDUCnRqd1w2pD-IyrTyUE4nQC9viWEb5GFTS9ociNGeKtuBPgpDychUDz39GTTAj4cNDDzerrpU8jFUhVTrp05qoB68TOiRTxrdcKfwnmFEfS6dy7DadixrgoMUtkdSFd5PI5ZdksBmskkLphwABu-GqJvyObiVCOKpu_qulGefE0ysjAsyq7xq9tzrGAoSoxdRCKY4TYLt9Xcad20442w-tAY938tfJx2Ez5IHXpcnetfGnvUZ1LVTNSfsR1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرارگاه خاتم الانبیا: از این به بعد درصورت هرگونه حمله اسرائیل به لبنان (حتی اگه به بیروت نزنه)، ما خودمون موشک می‌زنیم تو اسرائیل.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77275" target="_blank">📅 15:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77274">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUHLemiSODSzJhCveIB4y6DAmdvPBh6ARZ9HXfNVJx-Qmnf0OR6K4ZLs76xWJlWIfkprngq9wAVk0xTrAhJMKn_QwYiOhHw-mX1paSnBrJHntaqIeVfHyLDTrGO0GGds2JTOOkcS1gts-vAhQ8R4C3Iu_Ihx5C9N7OFVPRrZ_T2w7nJpkYZkyWKZ6qXg3CZZ4sKI7t9UwceZ_aKvapVI7eSNJzHljPknj2WrntoohcJTPS89aW183ZfksIjxS2xuF6ANYnn8wRyainFfw5DGfVPRgFElnTN4vtWkaJEpY8v2bp61l81eQsDC4xLOBW9lmWupSeC36AA72T329JEKag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرزیدنت پزشکیان:
اولویت ما امنیت ملی و آرامش مردم‌مان است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77274" target="_blank">📅 15:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77273">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">قرارگاه خاتم‌الانبیا: فعلا عملیات متوقف میشه اما به جان مادرم اسرائیل دوباره بلند پروازی کنه یدونه موشک میزنم.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77273" target="_blank">📅 15:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77272">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اسرائیل هیوم:
اسرائیل و ایالات متحده پیامی به ایران ارسال کرده‌اند که نشان می‌دهد اگر ایران از شلیک مجدد خودداری کند، حملات بیشتری صورت نخواهد گرفت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77272" target="_blank">📅 15:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77271">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ولی واقعا جواب دندون شکنی به یهودیا دادیم، بخصوص اون بخشش که مقر پلانکتون تو بیکنی باتم و خونه خانواده سندی تو جنگل رو زدیم.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77271" target="_blank">📅 15:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77269">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ولی واقعا جواب دندون شکنی به یهودیا دادیم، بخصوص اون بخشش که مقر پلانکتون تو بیکنی باتم و خونه خانواده سندی تو جنگل رو زدیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77269" target="_blank">📅 15:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77268">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">من کسخل‌تر شدم یا پزشکیان واقعا داره چهره ی محبوب جمهوری اسلامی از دید عوام میشه؟
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77268" target="_blank">📅 15:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77267">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">میگن پیت هگزت به مناسبت این جنگ نصف روزه ۵۰ تا شنا سوئدی رفته
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77267" target="_blank">📅 15:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77266">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">قرارگاه خاتم‌الانبیا: فعلا عملیات متوقف میشه اما به جان مادرم اسرائیل دوباره بلند پروازی کنه یدونه موشک میزنم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77266" target="_blank">📅 14:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77265">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">معاونت ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور:  نگران نباشید نتو قطع نمیکنیم  @Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/77265" target="_blank">📅 14:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77264">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">معاونت ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور:
نگران نباشید نتو قطع نمیکنیم
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/77264" target="_blank">📅 14:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77263">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2C8EmQzXL9lRefCA10pGq_skY2Z974OqWCjVEstQDoTVfN8UgoMOmC1oFI4Ls_shBJ4ogm0Kw6AB8gqqPwxaF9Bkywpm0ngnPXlzaMe7Voak6YDsqi_y3R9Z7esgaBX1CrmEXmiK4czgilFSSPLmqYLYLDVhf9fhf68AoIGoNQlM_RE-R-THiqT2GKLnaadHvSHsfb3L6UsURSyYEEjV2T7M0qaSYpQYAVrmHiSdHs-Axw1mu6WHA2VhZIT3lZADXA0Amp-zt7G3422tiHEGpWw0ogjV4PVqjtO9WGQNSlJPTs6_mBET4fQ1d3dnlmj9jWvGB6mBrceOio-PoYwUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:‌ هر دو طرف، اسرائیل و ایران، به دنبال آتش‌بس فوری هستند! مذاکرات نهایی درباره «صلح» در جریان است، مشروط بر اینکه نادانی یا حماقت مانع آن نشود. محاصره تا رسیدن به «توافق نهایی» برقرار و به طور کامل اجرا خواهد شد. امور باید به سرعت پیش برود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77263" target="_blank">📅 14:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77262">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">منتظرم جنگ امروز تموم شه بتونم بگم این جنگ عین کاگان بود، کوتاه و کصشر
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77262" target="_blank">📅 14:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77260">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqDENQ0VHZLQC5_CfJDQg9AlGnDWGjrrPFgzQI4Iwp0I5HyiIKYaqMsSr1wRAiUu2UFzlECz41LISBeBvfPgYQxqNaPqi6cHbkeQ6amYdQhxm_44NZAfo6Te6f54QCiTw4UwT0UF_F2fK34r3NmJehCYgdsJbBiNgEiHw7pxE7JRr3ertXsqroeQ0VACiQ3wIs8fDAljRtEl_rx78o_Tytq40otkdQ3oMCGI9d4aUIIdwpXypzbJ1DeMgaWErgda4Cujq9IQxbtEgRwQz0EggYSTzwDVdt5EetwH1HZ5lWif-GfZE2T6Gf26teUa6tQYiqwpmxLkkK0eb3VmMny7VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرا امروز خداست
😂
شهربانو و الهه منصوریان چون الهه تو مسابقات انتخابی تیم ملی باخته حمله کردن به خانه ووشو و الهه منصوریان با چاقو میوه خوری خودزنی کرده
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77260" target="_blank">📅 13:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77259">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">آموزش پرورش :
جنگ تموم نشه نهاییو مجازی میگیریم
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77259" target="_blank">📅 13:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77257">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o4An91t93LhYxEmFwa41EM-pbL3vMaleb_DeEjrFJltDS135tex5zSMsUkua3iWsDNniZ-nD-Ww4X7vaILnuSgdPi5CBOBsoaH-kl2ir9RnkLWowbdYV_oiBBrmfVeuSrIT2ev4QS04HRZjNy24ETaflXtLgX9UT0oGaLqYGqD9UbUvp14eeR8dUf9YjYisyAYlohHOku1YAOetzCLg8n03_H9d_bpc-qqq0PcmgKRD30MwXP8nB12Y3PKnCzX2qaFkaIVV_4TUnBQPpuAJoAyqUXVyCmd_fQpSn1Z3jDwbR3ZPYdxQQKb7-KjgxnBTxei1NsYpXrk1J6iMN2S7rqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ceY525hXgthpysNZYJ74IsPWkjEBaz198F0i_Io4Ot1tM8-ORQTp8DzzL6eo6iXEZ-XEBIht-2aROHE3PeZBfBPTHimACYyln5dJO_eSUwULdAFaxYHcK7IyUQu5tforasa0sR-WaVZr7o2u_-AUlrL3omSnxUPwDmlrdEVAeJI4fbC5nbsVa-b2BatQsUKni1uIuYRn6iNrc4bsCFvwT7bQK_m6Rtvfv8yVq3jn34jJI12n2Y6Tw4grJgkObDAuUwBYRDgbqQ5NOJdVOKw4YusQmqFXKheoM6pMajFEJg-AWe2z8VlOYSdFGgF09xBb2BckVs9fONhFdMWeBVj6Tw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دارن فضای جق زدن هم تو اپلیکیشن های ایرانی براتون میسازن دیگه چی میخوایید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77257" target="_blank">📅 13:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77254">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خاتم الانبیاء :
زدیم دهنشونو گاییدیم اگه باز بزنن میزنیم
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77254" target="_blank">📅 13:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77253">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اگه میخواید بفهمید کی ترور شده کافیه ببینید تسنیم میخواد از طرف کی بیانیه منتشر کنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77253" target="_blank">📅 13:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77252">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77252" target="_blank">📅 13:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77251">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اینکه نتارو قطع نکردن مشکوکه، میترسم بیان گوشیامونو بگیرن ایندفه
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77251" target="_blank">📅 13:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77250">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترامپ :
ایران و اسرائیل باید هرچه سریعتر جلوی شلیک رو بگیرن
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77250" target="_blank">📅 13:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77249">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e98d055a5.mp4?token=mGwYYS_kHhbjbeEp_levczo1RwuAw1Yk5O4110lVQk1cHxlqCwLwaD3oIHlTBeZupnJe-WHhIyuCX4A1lCROuegotmfRRquoHrDbalf1-qXGcn-bV5wjVPJfyBkaKLEODY6ZwjW4aHHgt8P9GKfmn8yb0RLZCcTlpegp_QJOTafOq4ALdg5x9uAbxosDyJJStUVu01RfpygE3DHPh0p8fVoUnbTROK3QqZxewtT9_9BZVzOFQyTDujZYbQGWF_NREymkgBg3rvGD3bLhHPQNUL51yFjweDnDCHS8XypoyRj6_8cgiUDxbJDJNBAaOAQzS6GTVXMAR0tUX9Xjqn1Nkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e98d055a5.mp4?token=mGwYYS_kHhbjbeEp_levczo1RwuAw1Yk5O4110lVQk1cHxlqCwLwaD3oIHlTBeZupnJe-WHhIyuCX4A1lCROuegotmfRRquoHrDbalf1-qXGcn-bV5wjVPJfyBkaKLEODY6ZwjW4aHHgt8P9GKfmn8yb0RLZCcTlpegp_QJOTafOq4ALdg5x9uAbxosDyJJStUVu01RfpygE3DHPh0p8fVoUnbTROK3QqZxewtT9_9BZVzOFQyTDujZYbQGWF_NREymkgBg3rvGD3bLhHPQNUL51yFjweDnDCHS8XypoyRj6_8cgiUDxbJDJNBAaOAQzS6GTVXMAR0tUX9Xjqn1Nkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو دوربین مداربسته از حمله خواهران منصوریان به دفتر ووشو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77249" target="_blank">📅 13:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77248">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ بیداره و واکنشی نشون نداده فعلا به ایران و اسرائیل
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77248" target="_blank">📅 13:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77247">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بیایید برید از این کانال پروکسی انبار کنید که اوضاع خیته:
https://t.me/+IJWzPBxj-zJiY2E0</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77247" target="_blank">📅 12:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77246">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">رسانه های اسرائیلی خبر از ترور سردار سپاه، احمد وحیدی میدن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77246" target="_blank">📅 12:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77245">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رسانه i24 news:
ارتش اسرائیل تصمیم گرفته عملیات «غرش شیران» رو از همون جایی که متوقف شده بود ادامه بده، به‌جای اینکه عملیات جدیدی رو آغاز کنه. ارتش این رو روز ۴۲ عملیات «غرش شیران» محسوب می‌کنه، اونم بعد از یه وقفه بیش از دوماهه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/77245" target="_blank">📅 12:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77242">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T6aQnPySPCgjF9R38jorsF-OdBrIhlPvG759yxnhKyy3NCJiVFYY9iwHwecPTS7Ku12B1Kih72gNvaSUzVL1ipgH_AfiP5RjFojyKxp6HMznssJLnLMqYDJO4byMnrk2d0pjj3-qioFgAZWcRrB3oULinChL0pZekz-zffoFW4kUnf6bKbfiQ9Tit9k1csdjJKWjTc7mL5QZ7v1_NXY_YMqFwWKoZpxuLvwHGQVg8bnlXDgU6dFpc57q9FeXXP5_iE-kqs8L8vQy5e6soUnL3KnSf0y3-kLCqrz-qnnjKm_vHoZabqowW5L4f47s84bFAhl_8lkFf6ryO00kXyt-Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l3P9Ae2cd57x92d-Cka0adGnGQhSNGrzO1qFrK_7IQZR4NwKeYq-efhQk7k0RzR0pmj0Z4d4Clqyfwv72RYl34flpCt9wj9rOgCKy3BhNl-GCxkf1-g6svUW4K9EgvGBt8L2vvXN1ciLrgaXNLpTn5f53jGCPZ898g0l2NDWe8hnvOOZq8PqJpHXFhpP5CMvTIKFw3E33bSP0dHM1R-n47oamDKxXzegqJCND-4THyBRnQCl7QimtMgwoI8bDWyka8Q3J2tXye2IY_6p7TIQuM6jXO2dFtizouS5z16zVe30W4aBBqCGflaOtuMeUix0NfHsOy_Nf9Zg60CarEL3oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C6lXdcgAmMFsZsd9WM3V428yzhfCZOq9tWaKEPkpNqoUnywNhw8VT5sOTIPueC8B9xsnUUvyx4v-noltMaHpj8PxEyeJq-EgaanzL2MBNyFo_2mgES1q0XJWpkQJHjPVUeoqI8Yk_ULF0u8UFuiAPIn4_6MvbnTGFfmmT6_0Ju6V-MyK8dUHJsak79nRy3rpJ6GgjJW4m7gS9XJsstxEVmJyZkO6LrEmN4vc-s4TT12RIEn5dq0akVHgMvjzialwpYbWZ2l-POAaIsdxoPHRzy1pUXdFEd4KRwUYW3pARkS8uRcgBhH_ARvJFZUG3WYdtLCTKDJzgf5kR6tZP_pWeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این وسط که اسرائیل داشت ایرانو میزدن، خواهران منصوریان فرصت رو غنیمت شمردن و اتک زدن به دفتر ووشو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/77242" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77241">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">رادیو ارتش اسرائیل:
ارتش اسرائیل برای حداقل چند روز درگیری با ایران و احتمال یک کمپین طولانی‌مدت آماده می‌شود.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77241" target="_blank">📅 12:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77240">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سازمان ملل:
we are nigga run
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77240" target="_blank">📅 12:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77239">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پارکینگ های زیر سطحی به عنوان پناهگاه برای شهروندان تهرانی در صورت تشدید تنش ها در دسترس قرار خواهد گرفت.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77239" target="_blank">📅 12:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77238">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">صابرین‌نیوز: خبر ترور و شهادت فرماندهان سپاه کذبه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77238" target="_blank">📅 12:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77237">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سفارت هند در تهران خواستار ترک فوری شهروندان هندی از ایران شد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77237" target="_blank">📅 12:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77235">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بنیامین نتانیاهو با کابینش جلسه امنیتی گذاشته.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77235" target="_blank">📅 12:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77234">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پتروشیمی کارون خوزستان دوباره مورد حمله قرار گرفت.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77234" target="_blank">📅 12:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77233">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">تیپ 10 "سیدالشهدا" سپاه پاسداران در کرج، هدف حملات ارتش اسرائیل قرار گرفت.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77233" target="_blank">📅 12:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77232">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ کونی رئیس جمهور هم مگه انقد میخوابه، پاشو دیگه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77232" target="_blank">📅 12:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77230">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دانشگاه هوافضای عاشورا رو هم زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77230" target="_blank">📅 11:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77229">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سگ زرد چجوری الان آتش بسه؟
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77229" target="_blank">📅 11:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77226">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">لشکر 8 زرهی اصفهانو زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77226" target="_blank">📅 11:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77225">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تسنیم میگه تست پدافنده.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77225" target="_blank">📅 11:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77219">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">فرید جان سلام ما کرجیم صدای انفجار اومد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77219" target="_blank">📅 11:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77218">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e1f36b08d.mp4?token=W3SP3WRSr668y_XMoXaNdwwSE3gwcpOWgJzgeIeLcK0KyUwmPGAd-cs4yMbi1tYEUoVbw97PpFjg4g3ZkEgnzFICV49q0wNe0pVzadys0dBeyj_L1hefMVkvnejIMI9N9MaE2lD0h1CJgiVESGkyxPwmCCMwnGUI9CmBT5_GUA1o4pMO9KNgjjWOxLqE6ey2rK1-X90GeutJl2XrL3RjT5AxB1Zef8NYFr_TlmzCD7NX9xUkiKGdczCL5TvTFMS1lGZIn-NDZw7hY1vsGhizH04gW1KVIYpFArwoMQquRumuQew8U8MEyT2snJzLpR3Ultd-yocRGMMbojjc6XS6_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e1f36b08d.mp4?token=W3SP3WRSr668y_XMoXaNdwwSE3gwcpOWgJzgeIeLcK0KyUwmPGAd-cs4yMbi1tYEUoVbw97PpFjg4g3ZkEgnzFICV49q0wNe0pVzadys0dBeyj_L1hefMVkvnejIMI9N9MaE2lD0h1CJgiVESGkyxPwmCCMwnGUI9CmBT5_GUA1o4pMO9KNgjjWOxLqE6ey2rK1-X90GeutJl2XrL3RjT5AxB1Zef8NYFr_TlmzCD7NX9xUkiKGdczCL5TvTFMS1lGZIn-NDZw7hY1vsGhizH04gW1KVIYpFArwoMQquRumuQew8U8MEyT2snJzLpR3Ultd-yocRGMMbojjc6XS6_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ وقتی بیدار میشه میبینه نتانیاهو دیشب گفته بود نه بابا کاری ندارم هرچی تو بگی ارباب ولی همین که خوابیده شروع کرده به زدن:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/77218" target="_blank">📅 11:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77216">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">صدای انفجار در غرب تهران
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77216" target="_blank">📅 11:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77215">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d92631652.mp4?token=NqLGlZ-ttUlOKLkOBujtOCdxA-sl1rje9VYTFgOnc2Fj-Gi2Np7l6HBTvnIEtVKVIthAXidOMjKiz8wYZZfKh2bzn9F3m4oNR-heqdisjYkoilYEXeR_hzGLoASrHhGCotAeEOWhfvjooJXS9bUiv-MG2q6g__N7CBiP4Ph5oBMjMpI4PiMhiURsdH88XZ-Q87UH4dMXz7HhQTtoIJM1s-1OEeAnx8i5YY_4PWHkXIG6XHFu0UkGPi2_2yT95ggYwK_hG_4reXcIaLsGBnOpmgbuPbsDqvnLiHmJCpOiKY42oWHB7jIpNDKOdfldcLodk6moXDRtH0_lGTvkg4UYpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d92631652.mp4?token=NqLGlZ-ttUlOKLkOBujtOCdxA-sl1rje9VYTFgOnc2Fj-Gi2Np7l6HBTvnIEtVKVIthAXidOMjKiz8wYZZfKh2bzn9F3m4oNR-heqdisjYkoilYEXeR_hzGLoASrHhGCotAeEOWhfvjooJXS9bUiv-MG2q6g__N7CBiP4Ph5oBMjMpI4PiMhiURsdH88XZ-Q87UH4dMXz7HhQTtoIJM1s-1OEeAnx8i5YY_4PWHkXIG6XHFu0UkGPi2_2yT95ggYwK_hG_4reXcIaLsGBnOpmgbuPbsDqvnLiHmJCpOiKY42oWHB7jIpNDKOdfldcLodk6moXDRtH0_lGTvkg4UYpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77215" target="_blank">📅 11:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77211">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اطلاعیه روابط عمومی سپاه پاسداران انقلاب اسلامی:
در پاسخ به حمله به یک پتروشیمی در ایران، چندی پیش به یک پتروشیمی مشابه در اسرائیل حمله کردیم.
اخطار می کنیم؛ دشمن صهیونیستی با اقدام علیه اهداف غیر نظامی و هدف قرار دادن صنایع نفتی، بازی خطرناکی را شروع کرد، که دامنه آن کلیه اهداف انرژی منطقه را در بر خواهد گرفت و عواقب آن برای اقتصاد جهانی، بر عهده آتش افروز اصلی این میدان، آمریکا می باشد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77211" target="_blank">📅 11:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77210">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نیروی موساد و آمان انقد بدبخته که با یه نت بستن شما نتونه به اسرائیل اطلاعات ارسال کنه اخه؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77210" target="_blank">📅 11:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77209">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LgfiIE9Aa6BtJaU-p_UEZaIl1_1_PLnPZpwYwL0p5LqdGnSwMAcoqTnyu_bMpaLeWxZX--uEyNCy6YFdaRslmfhTt9VikpuCzzjj_fvrQnmwvouAbRYHCEvoW12E6eDRt618jR6ORn9ovbfN-m93jTOgf_EIiJzlmG1QYVWwWx9ehePk4PZ2o80BifXfW9PNHKviqboQTMu92QKxznVe9FcfWO8TRVqvm86s_bQ-0hk7tt_Wzsf9MUS7GZ_JHfsAi7RU3Fb2VS8RPYupY844gnYcKYFpqwkZN2L3hBt4XuBixY5AxjLOjYhMKYXdtgFsF_-t_PkkwA78N3jRT0fxPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقیقا نمی‌فهمم منظورش چیه ولی از اونجایی که چند ماه پیش به یه بنده خدایی گفته بود زهی خیال باطل احساس می‌کنم خیلی حالیشه و در آینده خواهیم دید چه خواهد شد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77209" target="_blank">📅 10:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77207">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سخنگوی وزارت خارجه:
آتش بس نقض نشده ولی اگر اتفاق دیگه ای بیافته که بشه، ما آمریکا رو مقصر میدونیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77207" target="_blank">📅 10:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77205">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">۴۸ ساعت پیش ترامپ: در آن قسمت دنیا آتش بس یعنی کمتر بهم ضربه بزنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77205" target="_blank">📅 10:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77204">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBswqkozIBHeBlJuT6XxIErfNpjUwrnIW2AfitC6EpOuKjwhIPVnqVWK1pMFUB4j0kA3nUoR0nGQ6ndnsf-HdrV9GWXiea2PScxj8WjSV-sqbrEkeK5Q09QQZ_tMvETiioTW5kYKdNzYURA6mcBZd70CUBQ5BOF9kYBXxaozY0_91AOcAk3wnR2xmLRZD0vvFmVO5Sdl9pQQQTf4VjXNQcoCUYA4KDOSm3dRuO-dVcx7fGOIAIkzD8lmLzYidrSLtwe3QDJlIOmvaQb8GkQs73G7V0AcQXL_ao1n3NCdGdY8h0Gk8DXB8tsIAU9drWQERD34HJXRWL-qNz5GL64cjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتحادیه اروپا:
پدر عشق است لطفا جنگ نکنید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77204" target="_blank">📅 10:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77202">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">تا اینجای کار کشتی فرنگی بود، هروقت آزاد شد آتش بس نقض میشه</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77202" target="_blank">📅 10:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77201">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">نگفته بودن آتش بس زنگ تفریح هم داره</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77201" target="_blank">📅 10:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77200">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4usOjdLeIBJeOZsgAhBsSJ4ZkuZZogrgMKe1pwKtLNMMitVFatp01A55X_bNyXbcI79rFJpvzAn4smxYYpjYNHiSYas3imkeiKQEJitWthYqJNwBRfXA7BRagryw8xYWVDsfexL2gg_2zLp4kYVYec86_iXKmzSI8RAO9Opj1IkZXxM6XAFfMgoXtp3Un1eX-zxOw4ipQtYmfl1MztEkDYuF-Mx0R9K22RyAbxV8Rlv3331q8MWWO5FH_YQOT1-ZmcLp6EWKiYVdK8OuI8frSOKITEBxTsuixDT1NxlWKW8oBRKTUYZrkuE9eagzbPuHE6fX-wq4a8Rteqb-VItZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
خو اومد زد، آتش بس رو ادامه بدیم بازم میزنه خب یکی بگه ما چیکار کنیم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77200" target="_blank">📅 10:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77199">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اوه اوه جالب شد، انصرالله یمن اعلام کرد تنگه باب المندب بصورت کامل به روی اسرائیل بسته شد.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77199" target="_blank">📅 09:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77198">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0472fc5f3c.mp4?token=hECdALwDooo-1_SEMeoaGdQWbQ0-bCLQjM4FuqxwtSG-D0QG0e34Osypur9pkIuTRagibMy24vcUfDh9Hm3VoAw0bQSyPFuucHeQTIVW2qNZYocdhzdzYgxdIE9Q1cNcilUTHcJRn1blvUGkzgCctXKUi2YtsFOgC7si55Wlg0H2QziJgoHVXFM74F5nGP9PaGl15ckuR7FhUOaMEqa0OtcyRYf67Z36vcCzMiXyANEkgX5m3d_do6CvnGnMGh7t4aSJ_s-Bv8PVkEcWH0tFSmazNUa8ekrH1MGM6XdzFUcZqWhTcsh5ygFrc0Gy1_g_SR4_ReR6YuXr-A6LuMRJ0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0472fc5f3c.mp4?token=hECdALwDooo-1_SEMeoaGdQWbQ0-bCLQjM4FuqxwtSG-D0QG0e34Osypur9pkIuTRagibMy24vcUfDh9Hm3VoAw0bQSyPFuucHeQTIVW2qNZYocdhzdzYgxdIE9Q1cNcilUTHcJRn1blvUGkzgCctXKUi2YtsFOgC7si55Wlg0H2QziJgoHVXFM74F5nGP9PaGl15ckuR7FhUOaMEqa0OtcyRYf67Z36vcCzMiXyANEkgX5m3d_do6CvnGnMGh7t4aSJ_s-Bv8PVkEcWH0tFSmazNUa8ekrH1MGM6XdzFUcZqWhTcsh5ygFrc0Gy1_g_SR4_ReR6YuXr-A6LuMRJ0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ به عاصم منیر وقتی میفهمه دارن همو میزنن :
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/77198" target="_blank">📅 09:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77197">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">شما رو نمیدونم ولی من یکی خبرای جنگ و این که کی کیو زد بکیرمه</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77197" target="_blank">📅 09:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77196">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdkDr6BKo2BuIu_PAddfozjjF9z77GeiNXU8FiCW0rIg86G6P74mLQqQLQlbesOaCQEko17kqoZulPKFmW34QCWG30T9BgZly81stoorDSuMKoBi1guds3vfQxtTqQIs1YN81SsjIU2q94R3o9EfVkLUFLNw7fc0zhwO7WGaKgOBAMKjcI51yiQLJM2T1MTVf0EaD3jErI81DCU7w38gfWbfGXhOqav1jjXJkxF0v6YsUkoypNsXbVDmFfXTYpaiGbDMUB04cXa2lqf_bDZ_1mZDgdhj16kHjfCOd1L0IpMQuwgqWEwZduskW1sIIJ5A8lB1_2igkUjrojo02nmzCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وحید جان گرم کن بازی تازه داره هارد میشه
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77196" target="_blank">📅 09:14 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
