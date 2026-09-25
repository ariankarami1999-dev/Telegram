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
<img src="https://cdn4.telesco.pe/file/fthqcpi9im6uJnsfx2w_IFLZI81MX7W9Zh8ziO3YNfyFPLhz50AWCOSx_hOuWn5Z-BD_1oNIYg954EgctOWUtWC0XRv56QVowvCcuzcOtzA2hGzNuR5ma6jzc-7cYa1RvjySOdqnsJ4Z6zLHJOps6DGUz_l-mt_jU3jisV52qZMg6MPLeuqzJDinzeHJJSYklaF0YN3N-eOsfwuOjvgLWJD6JXI_wqVEBJz_SBkxFE_CClDppJpjuMLWCZoeOAHJtDLLeZaoFvdwaa-OXU57IvQ_ZaAqEKO2-bYEZm3mYosELa3vYwBoARqsR1XX5hpGSLZTaER7KXNJjG0A3OOzcw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 466K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-03 20:53:33</div>
<hr>

<div class="tg-post" id="msg-24161">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ در تروث : رئیس‌جمهور شی و خانم پنگ به‌تازگی واشنگتن را به مقصد چین ترک کردند. این دیدار، نشستی سرشار از دوستی، اقتدار و موفقیت برای هر دو کشور چین و ایالات متحده بود. ما بار دیگر در ماه نوامبر در چین و سپس در ماه دسامبر در اجلاس گروه ۲۰ (G20) در میامیِ فلوریدا با یکدیگر دیدار خواهیم کرد. دستاوردهای بسیاری حاصل شده و خواهد شد. مشتاقانه منتظر دیدار بعدی‌مان هستم!
@WarRoom</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/withyashar/24161" target="_blank">📅 20:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24160">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کنسولگری ایران در نجف : فرودگاه بین‌المللی نجف، حرم امام اول شیعیان و پایتخت آخرین امام آنها، به روی بزرگترین کشور شیعه جهان بسته است؟!
@WarRoom
😂</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/withyashar/24160" target="_blank">📅 20:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24159">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مسئول آمریکایی به شبکه الجزیره: واشنگتن در موقعیت قوی قرار دارد و کنترل تنگه هرمز را در دست دارد، بنابراین عجله‌ای برای رسیدن به توافقی با ایران نداریم.
حدود 40 میلیون بشکه نفت در 48 ساعت گذشته از تنگه هرمز عبور کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/withyashar/24159" target="_blank">📅 20:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24158">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JiwFX-5zVQ5wbqYtPq9wXghUBu-t1jUgPDA5v7t28Ai_xuxUa0S_JNSQitoL7dGusQafjKhr_1HcDzQdb4KNpQW3nRiJpcDAFIEoRCgw940P02s4Kt4lUDW11R09UZm82V32Me1Cmkm9sG9fRTzucEN9TCLIrFfipNWYK832i44eqL8rlZH1wr9aOqTIpGp6Kf6R-Ymhh7JVur_JD73VghZ-PT3_QM7dfI-l7dACyHm8RZrmTpJ8sZ94GT4M8CJJ4tPnlr0uZyWaafdDB_PLsb29yT02UU5XViuqKEr3u2HgeXJ9p7gNHRRSZzrShYnaNUS9mxAIa26iTmdhp7VQxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام:
تفنگداران دریایی آمریکا از یگان اعزامی تفنگداران دریایی یازدهم در حالی که روی ناو آبی‌خاکی
یواس‌اس باکسر (LHD-4)
در آب‌های منطقه‌ای در حال حرکت هستند، آموزش می‌بینند و به اجرای محاصره آمریکا علیه ایران ادامه می‌دهند.
تا ۲۵ سپتامبر، نیروهای سنتکام ۱۲۲ کشتی تجاری را برای اطمینان از رعایت کامل محاصره تغییر مسیر داده‌اند.
یعنی نسبت به رقم
۱۱۵ کشتی در ۲۳ سپتامبر، طی دو روز ۷ کشتی دیگر
تغییر مسیر داده شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/withyashar/24158" target="_blank">📅 20:23 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24157">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نیویورک‌پست: اشیای نورانی مشاهده‌شده در آسمان تهران ممکن است مربوط به سلاح‌های لیزری آمریکا باشند.
این رسانه با اشاره به سامانه
هلیوس (HELIOS)
، گزارش داده آمریکا از سلاح‌های لیزری برای مقابله با پهپادها و موشک‌های کروز استفاده کرده است. هلیوس یک سامانه لیزر پرانرژی نصب‌شده روی ناوهای جنگی آمریکاست که می‌تواند با متمرکز کردن پرتو، حسگرها یا خود پهپاد را از کار بیندازد. با این حال، ارتباط مستقیم اشیای نورانی دیده‌شده در تهران با هلیوس
به‌طور رسمی تأیید نشده است
.
@WarRoom</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/withyashar/24157" target="_blank">📅 20:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24156">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">پرتاب سه موشک از کوهدشت لرستان
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/withyashar/24156" target="_blank">📅 20:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24155">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">یک مقام ارشد ایرانی به رویترز گفت: ایران در مورد برنامه هسته‌ای خود هیچ‌گونه امتیازی نخواهد داد.
@WarRoom</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/withyashar/24155" target="_blank">📅 20:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24154">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">یک مقام آمریکایی به «اکسیوس»: ایران تصاویری از ماهواره‌های چینی را برای اهداف نظامی بکار برده است. واشینگتن به تهران ابلاغ کرد که ایران کنترلی بر تنگه هرمز ندارد و بنابراین حق ندارد درباره این آبراه شرط‌‌هایی بگذارد.
@WarRoom</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/withyashar/24154" target="_blank">📅 20:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24153">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f03282bab.mp4?token=PFJ0P3IVtoe3t-T19qsXMXukHXsO-qFj0JEXbAvb8CmJw6Wt-UyPCIkTZATaTr6v9FK4oguatUD33fpAeuMf3qT4u0UYtuTxTW1VZPg_d8m6UnBTqO75x2dIO4LkoNO01pEGs7rmFE_WhY7lyYNlw1wkAHPr_GpsBXFrWKNRer2a_U_LIpxfcLZxQdAI-G4OsGkrRFDjPMeO00VLSVh2TMjfSY7qO9Hknrg8Y3XzZQH14GftH9nrfTPXAgEnG2m7Yg-wtsgPmyK3Rc12lIE1LQIgzKSuKldfYziNYnVb1dADDmSels1Oum4C2jJ4jM2tezjRZBi5qB0tlSj30OFj-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f03282bab.mp4?token=PFJ0P3IVtoe3t-T19qsXMXukHXsO-qFj0JEXbAvb8CmJw6Wt-UyPCIkTZATaTr6v9FK4oguatUD33fpAeuMf3qT4u0UYtuTxTW1VZPg_d8m6UnBTqO75x2dIO4LkoNO01pEGs7rmFE_WhY7lyYNlw1wkAHPr_GpsBXFrWKNRer2a_U_LIpxfcLZxQdAI-G4OsGkrRFDjPMeO00VLSVh2TMjfSY7qO9Hknrg8Y3XzZQH14GftH9nrfTPXAgEnG2m7Yg-wtsgPmyK3Rc12lIE1LQIgzKSuKldfYziNYnVb1dADDmSels1Oum4C2jJ4jM2tezjRZBi5qB0tlSj30OFj-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا
در مور
د جنگ با تهران با شی جین‌پینگ بحث کردید؟
ترامپ: بله.
فکر می
‌کنم قرار است درباره ایران عالی عمل کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/withyashar/24153" target="_blank">📅 20:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24152">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نیوزمکس, ایران پیشنهاد معامله هرمز را ارائه داد: تهران می‌گوید اگر ایالات متحده تحریم‌های نفتی را لغو کند، دارایی‌های مسدود شده ایران را آزاد کند و با پایان دادن به جنگ در همه جبهه‌ها، از جمله لبنان، موافقت کند، می‌تواند ظرف چند روز تنگه هرمز را بازگشایی کرده و مذاکرات هسته‌ای را آغاز کند.
پزشکیان: آخرین پیشنهاد ما برای بازگشایی هرمز منتظر چراغ سبز ترامپ است.
@WarRoom</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/withyashar/24152" target="_blank">📅 19:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24151">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1621b33d91.mp4?token=fiPeCJILK4IY92mL42PDGkwEbBSUMaHlKdMCRwPll5mJ2H4xq-fOxll7-0MgUJJGZFJ_cXluhgDUwGKJ3UopkZKuE3Xbo_2gMr2HW110V4Kzg9Sw284FDhwg5VcaHzLB0D1NaC4E4zS8GFwYFhzQAByJ6ubsBYXtInsYdhtmVCLAMkUsuPAxeO7kM6n_8bagXkY3y5YLjlqg-YKNhRaBVGrHVqKGi4JKDZv_SIf0o_HEFaSPnFOkU9nW1mDYQ6rFByZFCFKp8P3CwTRzFFWme3KXI3tKqCy5Z5iGfTscwGljXX0VTMD8TZHe_l5n3qfz8fJYuXVEQMb_8O45DHPoRyDRTC2o6iuavDUbtL1CG2pjPBHxdcRenFk0IwMT7Q5ARz1-tn-1os7WorrXHwcib0YtKyjR92uwkUpe0qMjMTXKFKYRMb4SWfSGU9hLSHE8bzIplLVY-PjPpVW5Hyv4xbL83OEMY3pUGY10oFD8_R3Avz7l72m8_tmCo83aEjWENG1jHoPPMULhXCiyPLcxFq5EFKNBR7t2FO6d1dungZWiqHoKufrPciTjtoLikXEBwwqMyGS6LAl40NvbMkO3o6bOCgHb-M80mt3DEbgKzjQ9Q_crzh67FtSP-ttEj2TwdaD46-cD4AyGd1z7YC4V06RzEEQfAmf-6UlLNVNgxIc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1621b33d91.mp4?token=fiPeCJILK4IY92mL42PDGkwEbBSUMaHlKdMCRwPll5mJ2H4xq-fOxll7-0MgUJJGZFJ_cXluhgDUwGKJ3UopkZKuE3Xbo_2gMr2HW110V4Kzg9Sw284FDhwg5VcaHzLB0D1NaC4E4zS8GFwYFhzQAByJ6ubsBYXtInsYdhtmVCLAMkUsuPAxeO7kM6n_8bagXkY3y5YLjlqg-YKNhRaBVGrHVqKGi4JKDZv_SIf0o_HEFaSPnFOkU9nW1mDYQ6rFByZFCFKp8P3CwTRzFFWme3KXI3tKqCy5Z5iGfTscwGljXX0VTMD8TZHe_l5n3qfz8fJYuXVEQMb_8O45DHPoRyDRTC2o6iuavDUbtL1CG2pjPBHxdcRenFk0IwMT7Q5ARz1-tn-1os7WorrXHwcib0YtKyjR92uwkUpe0qMjMTXKFKYRMb4SWfSGU9hLSHE8bzIplLVY-PjPpVW5Hyv4xbL83OEMY3pUGY10oFD8_R3Avz7l72m8_tmCo83aEjWENG1jHoPPMULhXCiyPLcxFq5EFKNBR7t2FO6d1dungZWiqHoKufrPciTjtoLikXEBwwqMyGS6LAl40NvbMkO3o6bOCgHb-M80mt3DEbgKzjQ9Q_crzh67FtSP-ttEj2TwdaD46-cD4AyGd1z7YC4V06RzEEQfAmf-6UlLNVNgxIc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاکر کارلسون می‌گوید پس از آنکه تلاش کرد ترامپ را متقاعد کند وارد جنگ با ایران نشود، رئیس‌جمهور ترامپ به او گفت:
«بله، حق با توست؛ اما در نهایت همه ما می‌میریم، پس اهمیتی ندارد.»
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/withyashar/24151" target="_blank">📅 19:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24150">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf75471ddf.mp4?token=PGNweNsU3fgCfSH6f8i-zSZ2OHnS7WoUYpi8HY1SE73dTp7LCQCiAAdtd-m4HzhCb45RJ6uK3CWGY1i4UOV_j4FGIQMWCKRYsKf3rbqOrUco3nun50XXDVGryXpUWWTlCHnNcDiObHykb0xMxORrG24envdH2meXwsQZuMthQLOL7dnWUjlpIJLoJZXSLK6_yTceWM1_eE0nAuWNZLnjaEHFSi_bQwi3GucFMlh_nNNJYudHYqaS4jw48eBPX5Hh4nkMk2eAmhcIlCuQbfz1aGRUZRNl5P49Fb8gd9a1AfZ1KLcM77fvOhMEOJQhYMnc1oijJFgbcZt4k9vkue4x3Y_WynXHesxcxRd80S5Vg9l2qlnArO984h24_nExS0uXuPZziNhN5MusMwPX0-_uMxA2O1trKgK2y6bemZzp2rgicy92TVEe9-PMU66Y4lNxqhy2gn9p21ANbSYsnziPsPP08_usT2HLMkn0ByrPU4_82Rt6vy0h8fSHmR7CNuiCr1DfTkFIvwZvnkIdr82J7MvB9TAAPjPQ2HPfxWGgMlRS1iyGId_Ax6hmSOb3TV2r2Vg9i5m_ipT0Y4bRzvlMkAwyfTLYP3U63aExvKTqn7FaQd0ZDDbhcIU_utA2SZusd7xTwB-y2VP3emVDT85uhfIY7_zptN4ss08I8uOiYOo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf75471ddf.mp4?token=PGNweNsU3fgCfSH6f8i-zSZ2OHnS7WoUYpi8HY1SE73dTp7LCQCiAAdtd-m4HzhCb45RJ6uK3CWGY1i4UOV_j4FGIQMWCKRYsKf3rbqOrUco3nun50XXDVGryXpUWWTlCHnNcDiObHykb0xMxORrG24envdH2meXwsQZuMthQLOL7dnWUjlpIJLoJZXSLK6_yTceWM1_eE0nAuWNZLnjaEHFSi_bQwi3GucFMlh_nNNJYudHYqaS4jw48eBPX5Hh4nkMk2eAmhcIlCuQbfz1aGRUZRNl5P49Fb8gd9a1AfZ1KLcM77fvOhMEOJQhYMnc1oijJFgbcZt4k9vkue4x3Y_WynXHesxcxRd80S5Vg9l2qlnArO984h24_nExS0uXuPZziNhN5MusMwPX0-_uMxA2O1trKgK2y6bemZzp2rgicy92TVEe9-PMU66Y4lNxqhy2gn9p21ANbSYsnziPsPP08_usT2HLMkn0ByrPU4_82Rt6vy0h8fSHmR7CNuiCr1DfTkFIvwZvnkIdr82J7MvB9TAAPjPQ2HPfxWGgMlRS1iyGId_Ax6hmSOb3TV2r2Vg9i5m_ipT0Y4bRzvlMkAwyfTLYP3U63aExvKTqn7FaQd0ZDDbhcIU_utA2SZusd7xTwB-y2VP3emVDT85uhfIY7_zptN4ss08I8uOiYOo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاسخ پدر جاویدنام ⁧
#عرفان_عبدی_پور
⁩ به اراجیف دیروز پزشکیان در فاکس‌نیوز
@WarRoom</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/withyashar/24150" target="_blank">📅 19:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24149">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دیوید پردو سفیر آمریکا در چین:
ترامپ دیروز به شی جین‌پینگ صراحتاً گفت هرگونه کمک چین به ایران، چه اطلاعات باشد و چه قطعات یا تجهیزات نظامی، کاملاً غیرقابل‌قبول است,
ترامپ مواضع و منافع آمریکا درباره ایران را برای چین کاملاً روشن کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/withyashar/24149" target="_blank">📅 19:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24148">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/627df24333.mp4?token=mwcGgC8r9hjsvLoENK3qDpAY_sbeW9UBGMb2qoHo09lFKzxo7n2enQoNtHjh-jpGBC8Qcuu_EJINkYPXcvoqHJ8Jquaky6TC4V0hl0LeVn1dygxDObpsqEtNTw-aENz7IJlOwB-qPkBZMTSR5sg4xqChWq9J-e13OdJmyCZoIE7rs0vniMoFm2HQ4ml5drDa4v10ZvXe-K49UD-ssStHbiU1S0qlbWeuX4QeVxwAtGX1NoN6IEa4CieHw72xyFuCl5zCSxGTKtyrWna6qX68lrFt_6aaC-OEJ6uPyGFG6yRYLlNPujdual2RYB4uZAcZLCcbI2gGUBIydopwlJ5lYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/627df24333.mp4?token=mwcGgC8r9hjsvLoENK3qDpAY_sbeW9UBGMb2qoHo09lFKzxo7n2enQoNtHjh-jpGBC8Qcuu_EJINkYPXcvoqHJ8Jquaky6TC4V0hl0LeVn1dygxDObpsqEtNTw-aENz7IJlOwB-qPkBZMTSR5sg4xqChWq9J-e13OdJmyCZoIE7rs0vniMoFm2HQ4ml5drDa4v10ZvXe-K49UD-ssStHbiU1S0qlbWeuX4QeVxwAtGX1NoN6IEa4CieHw72xyFuCl5zCSxGTKtyrWna6qX68lrFt_6aaC-OEJ6uPyGFG6yRYLlNPujdual2RYB4uZAcZLCcbI2gGUBIydopwlJ5lYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افزایش تحرکات ترابری آمریکا در ارتباط با خاورمیانه،د
ر۲۴و۲۵
سپتامبر(دیروز و امروز)
، فعالیت هواپیماهای ترابری و پشتیبانی آمریکا از جمله
C-17، C-5M، C-130 و KC-135
در ارتباط با منطقه خاورمیانه مورد توجه قرار گرفته است… یه خبرایی داره میشه
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/withyashar/24148" target="_blank">📅 18:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24147">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">گارد ملی آمریکا اعلام کرده که در
۲۲ و ۲۳ سپتامبر
، هواپیماهای
C-130H3 هرکولس
از گردان ۱۶۶ ترابری هوایی دلاور برای پشتیبانی از عملیات سنتکام در خاورمیانه اعزام شده‌اند و حدود ۱۰۰ نفر از نیروها نیز همراه آنها مستقر شده‌اند.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/withyashar/24147" target="_blank">📅 18:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24146">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">کارشناس نظامی صداوسیما:
در روز های اخیر پرواز هواپیماهای جاسوسی و شناسایی آمریکایی اطراف ایران بسیار افزایش پیدا کرده است که نشان دهنده یک حمله قریب‌الوقوع احتمالی به ایران است.
@WarRoom</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/withyashar/24146" target="_blank">📅 18:41 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24145">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed2fc3da78.mp4?token=kc6WAU3h8czHmzQurIw9SUN-KqDY3oluBVVbrnOnyID7jKSRgLenZZHY1QX_X6AST5EB9HjgRjBjgxPRXDU1S5_7d1tt5rO3HojXAPYM1DZKVr4vfLW0Itldhar_XtF4VqoNk-kL-aqfOFJkP-10TuMKtok2uou6Z-1nhQdS3Jti61WAT3uKYqx-ZIwhZqJCiyqpINoJ2wpZxmiJl-fVmSvlInglnqz0xlu2kQbNBuIZJu08MPq61t9fOdPgFBqNzmauAP4scsGWRe8Gzw3ztssXK_UFzXcPC0m02vGFvO-mPo3-b8SHZqaLQ74i6aDhxv1LH0lYg4iv0sKYRKFBEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed2fc3da78.mp4?token=kc6WAU3h8czHmzQurIw9SUN-KqDY3oluBVVbrnOnyID7jKSRgLenZZHY1QX_X6AST5EB9HjgRjBjgxPRXDU1S5_7d1tt5rO3HojXAPYM1DZKVr4vfLW0Itldhar_XtF4VqoNk-kL-aqfOFJkP-10TuMKtok2uou6Z-1nhQdS3Jti61WAT3uKYqx-ZIwhZqJCiyqpINoJ2wpZxmiJl-fVmSvlInglnqz0xlu2kQbNBuIZJu08MPq61t9fOdPgFBqNzmauAP4scsGWRe8Gzw3ztssXK_UFzXcPC0m02vGFvO-mPo3-b8SHZqaLQ74i6aDhxv1LH0lYg4iv0sKYRKFBEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدای مهیب و ستون دود هم اکنون بهبهان
@WarRoom</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/withyashar/24145" target="_blank">📅 18:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24144">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmPTuecfwX7kv4LJKEztzNr3lVlGO1PhBrEzv_vXpcHPMV0M9PssIW0Ny8NpwJHEUacbyeV-_IXzcivqDjSg4z-CQjZBvvHX6S7ypv8kv1_e9byTfwDPF3Otj4LDV3MLhHo_GA3QLBY-IZcv9vE4GH996YuOHiyZBGODW-iZfxOMiQWHsIqcdNzjqa2wpIrfNa60lfrPBxZvmGzA_JTcZPq-xJeri6vzA6t0n7dxww1DAn7WgGQEr6l7iHqK8AnExEhuCPY5_IADk9FMdQX0qNayLTi9cqpg-mIP1tv77W7xVffA1Js_rOwUo8HbXBWORpREXu88JgUwk6CCeBodaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چین نام رسمی جنگنده پنهانکار J-35A را اعلام کرد:
رسانه دولتی چین، CCTV، برای نخستین‌بار این جنگنده نسل پنجم را با نام
یون‌لونگ (Yunlong؛ اژدهای ابری)
معرفی کرد. در همین برنامه نام جنگنده‌های اصلی نیروی هوایی چین نیز اعلام شد:
J-10 — منگ‌لونگ (Menglong؛ اژدهای نیرومند)، J-11 — یینگ‌لونگ (Yinglong؛ اژدهای بالدار)، J-16 — چیان‌لونگ (Qianlong؛ اژدهای پنهان)، J-20 — وی‌لونگ (Weilong؛ اژدهای باابهت)، J-35A — یون‌لونگ (Yunlong؛ اژدهای ابری).
@WarRoom</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/withyashar/24144" target="_blank">📅 18:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24143">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سفیر آمریکا در چین: طرف چینی در مذاکرات پنجشنبه تأیید کرد که از ایران حمایت نمی‌کند.
دیوید پردو گفت ترامپ به شی جین‌پینگ تأکید کرده که هرگونه کمک مستقیم یا غیرمستقیم به ایران، از جمله ارائه اطلاعات، قطعات یا تجهیزات نظامی،
کاملاً غیرقابل قبول است.
به گفته او، دو طرف همچنین توافق دارند که
ایران نباید به سلاح هسته‌ای دست پیدا کند و تنگه هرمز باید باز بماند.
@WarRoom</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/withyashar/24143" target="_blank">📅 18:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24142">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/945aef0662.mp4?token=IdGw86zpDsApvOAHH2WcPw9_CM9H9bOWulggrWlhobEDHyTfI72nIWaQG6Xf_Gutj2RltaP9lvH9U_Oyy8R6r4n0icm-RDfK8Ye1Ou_gQVoAcNuq5RHRzMn2pP_RsfQHi1QD5LkM9IWYWvZj-GHVzZTJddURcp7tyUWBapUoRSLBkVZ7yqtifZcBqRny-Wf5ly-iV-DPGQw-FTrgXNREBaY6zR17rIh1aLW-s4_Y0FATyFwvlRa_5FXWP9mgWfI0EGfXLtCocedV9ZZ0QKHHWZn2V4-LktYwvUaDuoNDMy13Jzh7VAlzqb6SrwvVGceySbFlkVlbtbjmq4I7G5ZE5wldK75NiQiljM5lsRHY06EU8uGULuUVZ-ZUZdy-zcI1rtCkXmBBPMpzBfaXCmSm7KG-IfO9TmoxwM_cAEQ1mYj0kC31C8SG_J8bR-ajnNIO-BDPL1X9sCYLkI1he-DOXvUoKl0TxbEEBY-48m73xZHWTmqMZulTEsPBTDNFpUJpfPBT2q3joSXT_VbaJ74iCaYtopW-5ZTWsakurTyK1uTFzWOYnM9Jo0R0-eC0Cwdg0AOaKYZbBzmfMX80PDp8tOy8ss3bqbcA6R2JvvAp6XoFaqQxXC-DOhKG0owPzDDIi9Xq_15CX5VxhnkcyLPct03N6p1Zbo-lExRp6wFQL1E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/945aef0662.mp4?token=IdGw86zpDsApvOAHH2WcPw9_CM9H9bOWulggrWlhobEDHyTfI72nIWaQG6Xf_Gutj2RltaP9lvH9U_Oyy8R6r4n0icm-RDfK8Ye1Ou_gQVoAcNuq5RHRzMn2pP_RsfQHi1QD5LkM9IWYWvZj-GHVzZTJddURcp7tyUWBapUoRSLBkVZ7yqtifZcBqRny-Wf5ly-iV-DPGQw-FTrgXNREBaY6zR17rIh1aLW-s4_Y0FATyFwvlRa_5FXWP9mgWfI0EGfXLtCocedV9ZZ0QKHHWZn2V4-LktYwvUaDuoNDMy13Jzh7VAlzqb6SrwvVGceySbFlkVlbtbjmq4I7G5ZE5wldK75NiQiljM5lsRHY06EU8uGULuUVZ-ZUZdy-zcI1rtCkXmBBPMpzBfaXCmSm7KG-IfO9TmoxwM_cAEQ1mYj0kC31C8SG_J8bR-ajnNIO-BDPL1X9sCYLkI1he-DOXvUoKl0TxbEEBY-48m73xZHWTmqMZulTEsPBTDNFpUJpfPBT2q3joSXT_VbaJ74iCaYtopW-5ZTWsakurTyK1uTFzWOYnM9Jo0R0-eC0Cwdg0AOaKYZbBzmfMX80PDp8tOy8ss3bqbcA6R2JvvAp6XoFaqQxXC-DOhKG0owPzDDIi9Xq_15CX5VxhnkcyLPct03N6p1Zbo-lExRp6wFQL1E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏دیروز در مجمع عمومی سازمان ملل، بنیامین نتانیاهو از اردوغان گفت و از هزاران غیرنظامی کُرد که کشته شده‌اند. جمله روشن بود، به انگلیسی، بی‌هیچ ابهامی: Kurdish civilians.
در همان لحظه، روی آنتن زندهٔ ایران اینترنشنال، این جمله سانسور شد به «غیرنظامیان ترکیه».هر دو را در این ویدیو کنار هم گذاشته‌ام. ببینید، و خودتان قضاوت کنید.
@WarRoom</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/withyashar/24142" target="_blank">📅 17:30 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24141">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">فایننشال تایمز: حوثی‌های یمن به اتحادیه اروپا اطمینان داده‌اند که کشتی‌های اروپایی را در دریای سرخ هدف قرار نخواهند داد.
حوثی‌ها گفته‌اند عملیات آنها در حال حاضر
متوجه عربستان سعودی و منافع مرتبط با این کشور
است و قصد ندارند کشتیرانی بین‌المللی یا کشتی‌های اروپایی را مختل کنند. همزمان، پس از مذاکرات با آمریکا با میانجی‌گری عمان، حوثی‌ها به واشنگتن نیز اطمینان داده‌اند که
کشتی‌های آمریکایی را هدف قرار نخواهند داد
؛ در مقابل، آمریکا نیز از تشدید حملات علیه حوثی‌ها خودداری کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/withyashar/24141" target="_blank">📅 17:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24140">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfMX7mRq5IJgItStvbBc6sZ6vvzvHLcvDhq_ynNxsJ0Ha6_B_tDQa07e_MDFLWlIUtzOdVS4fsACPlqr7PrIwRApq5ZzpBTOPubnbksG0IXaO62NpwxkkyI0cUrT9Cf-YBvC2dTGjylZcXLlj4h8uc5jZoza_opu8xuTG08IZJJ-qb7sUKiITtGrVMerziOyTrxX71Ttj1jXh47OFxYKZrTEXG6ABfsuZdmPykMVSH9yj6xrSVnopgEfz9kZEBmF_uFOR4UmKMX3muJSdzQBp-Vk_LWb5n2Nya6iDBJqkCohTnrpZY0sxVd6zx4Bmm4LgEQcSy5ePGtYdhtgsaihaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علنی شدن خونشوران بین‌المللی و لابیگران رژیم، دیدار پزشکیان با دستنشانده‌های رژیم در حاشیه نشست سازمان ملل. رابرت مالی، تریتا پارسی، فرناز فصیحی، نگار مرتضوی.
@WarRoom</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/24140" target="_blank">📅 16:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24139">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">صفحه رسمی‌وزارت امور خارجه اسرائیل به فارسی:
یه خبر خوب.حکومت شرور جمهوری اسلامی سقوط خواهد کرد و همه ما آن روز را جشن خواهیم گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/24139" target="_blank">📅 16:23 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24138">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">دادستانی کل نیویورک از پولی‌مارکت به اتهام فعالیت غیرقانونی قمار شکایت کرد.
مقام‌های نیویورک می‌گویند این پلتفرم بدون مجوز، بازارهای پیش‌بینی ایجاد کرده که از نظر قوانین ایالتی نوعی شرط‌بندی محسوب می‌شود. نیویورک از دادگاه خواسته فعالیت بدون مجوز متوقف شود،
سودهای حاصل از این فعالیت‌ها بازگردانده و جریمه‌ای معادل سه برابر سودها پرداخت شود.
پولی‌مارکت در مقابل می‌گوید بازارهای پیش‌بینی تحت نظارت فدرال قرار دارند و ایالت نیویورک صلاحیت برخورد با آن را ندارد.
@WarRoom</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/24138" target="_blank">📅 16:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24137">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">در‌ حدود ۱۰ دقیقه تنگه ۳ بار صدای ناله اپراتورهای لانچر که کتلت شده اومد
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/24137" target="_blank">📅 14:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24136">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سی‌ان‌ان به نقل از منابع: تصاویر ماهواره‌ای و اطلاعاتی که از سوی گروه‌های چینی ارائه شده است، به ایران کمک کرده تا کشتی‌ها را در تنگه هرمز تهدید کند و حملات دقیقی را به پایگاه‌های نظامی آمریکا در خاورمیانه انجام دهد. این بخشی از بهبود چشمگیر توانایی‌های هدف‌گیری ایران در چند ماه گذشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24136" target="_blank">📅 14:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24135">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">نیروهای دولتی یمن: در یک حمله سریع ما به قله کوه نمان و منطقه دار الکافر تسلط یافتیم.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24135" target="_blank">📅 14:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24134">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">3 رسانه‌ به کاخ سفید بازمی‌گردند
پس از آن‌که دونالد ترامپ دسترسی خبرنگاران سی‌ان‌ان، MS Now و پولیتیکو به کاخ سفید را لغو کرده بود، یک قاضی فدرال دستور داد این محدودیت برای
14 روز متوقف
و مجوزهای خبرنگاران فوراً بازگردانده شود.ترامپ پیش‌تر مدعی شده بود پوشش این رسانه‌ها «دروغ» و تهدیدی برای امنیت ملی است، اما قاضی گفت شواهد کافی برای اثبات این ادعا ارائه نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24134" target="_blank">📅 14:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24133">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">رویترز: فرودگاه‌های اربیل و سلیمانیه در عراق نیز از روز جمعه، پذیرش پروازهای هوایی از ایران را متوقف خواهند کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24133" target="_blank">📅 13:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24132">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">زمین‌لرزه‌ای به‌بزرگی ۴ ریشتر در عمق ۸ کیلومتری، سفیددشت اصفهان را لرزاند
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24132" target="_blank">📅 13:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24131">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67e7fd7acc.mp4?token=fODAL_gbuRMNJxbt4WWCe6JgIaobV2dCS6R9eOspK6D2HaL0asTH4yxEqE6jQiCGJaJp-kc8TKuDVe0b6nOglTBFawXkjmYk13whjhxIkXJCP6Rw4cfEXtMFNnykqGuhu6D5k1uf-1piPoOqSKUVVUM-YK2_OFwmG0pk8LrBOVjt5jL1i88g4ayaIcdZQ5bZAwOrZewxQOFoKt44W48qU7Fhv39MsPQIqS5tmuvu2IF-DRR0wYBMgObgH4wPy4JfBEI0_ZRNezEsuVWRZewGO8lsba0C-3LQKRcphDM-gERoj1w75FoZg43yrj2Q6B2ZhkBGded5e_R1mnZBEaFkGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67e7fd7acc.mp4?token=fODAL_gbuRMNJxbt4WWCe6JgIaobV2dCS6R9eOspK6D2HaL0asTH4yxEqE6jQiCGJaJp-kc8TKuDVe0b6nOglTBFawXkjmYk13whjhxIkXJCP6Rw4cfEXtMFNnykqGuhu6D5k1uf-1piPoOqSKUVVUM-YK2_OFwmG0pk8LrBOVjt5jL1i88g4ayaIcdZQ5bZAwOrZewxQOFoKt44W48qU7Fhv39MsPQIqS5tmuvu2IF-DRR0wYBMgObgH4wPy4JfBEI0_ZRNezEsuVWRZewGO8lsba0C-3LQKRcphDM-gERoj1w75FoZg43yrj2Q6B2ZhkBGded5e_R1mnZBEaFkGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیپلمات اسرائیلی نام تمام کشورهایی که جلسه را ترک کردند یاداشت کرد تا بعد به خدمتشان برسند.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24131" target="_blank">📅 13:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24130">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">زلنسکی، رئیس‌جمهور اوکراین:
«طرف آمریکایی پیشنهاد برگزاری
نشست سه‌جانبه در امارات متحده عربی
را مطرح کرده است.
ما منتظر پیشنهاد آمریکا درباره
تاریخ برگزاری این نشست
هستیم.»
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24130" target="_blank">📅 12:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24129">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01aa2ba27b.mp4?token=uv0SU_UHHAZXIezFS1PD3VodZ7xVuiYxl-Dhkjehem0G8BdYvdDP2KVLVWpZtxUJyyEi0a5Y9W6fR5wAsoxjjmjwzqydqD2sOuODDtmIqxABSVTEZLZmit9Hl-Kn-spIn6QATaiMICyVKEo_NLOSGQiL84I8xgnpfBfFV3CXK-3PdTLudwqAH9jTDhq_sqjZBVAv4tgfaOZ0g6OMMJekEcNCaVtcyG7Ebcv_ar2NiW90cd3nptn68PqcLPV0gOfFnKQX_5opkkJZi-s4VikCgePG2qOKlTIvIAcd3xHLyviigHuAbvsiJU4dTaww6Ll1MAbbX7o1Us3TLFfPiRRiOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01aa2ba27b.mp4?token=uv0SU_UHHAZXIezFS1PD3VodZ7xVuiYxl-Dhkjehem0G8BdYvdDP2KVLVWpZtxUJyyEi0a5Y9W6fR5wAsoxjjmjwzqydqD2sOuODDtmIqxABSVTEZLZmit9Hl-Kn-spIn6QATaiMICyVKEo_NLOSGQiL84I8xgnpfBfFV3CXK-3PdTLudwqAH9jTDhq_sqjZBVAv4tgfaOZ0g6OMMJekEcNCaVtcyG7Ebcv_ar2NiW90cd3nptn68PqcLPV0gOfFnKQX_5opkkJZi-s4VikCgePG2qOKlTIvIAcd3xHLyviigHuAbvsiJU4dTaww6Ll1MAbbX7o1Us3TLFfPiRRiOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدبان اتاق جنگ :  چونفدا ها رالی موتوری برگزار‌کردن هم اکنون میدان آزادی
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24129" target="_blank">📅 12:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24128">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEkZjznGHLfopAI0oU5pcylSgp_OziCfCVm9e5DOoX3VCMiy3mph0RPyhESk3xDM4szNIwgpgVVaNvG0Jr2hQrVIXTdjMlM8Sfu_gu7xLomac5XKyuDh-3NBGRLu1p-lXkPg_IdUo02moOlIL3XDYzso7ux4SfMQ_6bKUYZLDCxBaOhJxeQ4DvnuSU0Qjrh1UUTUHerHWDx96B3xLaSSbzekBntquXC5vCyq_696l-WpVZBv7SP08fLuiz1o3PVxHY8E-AyK7Y0_ThL0AfiTCaMJZarUWcHiIlpY6XZQg1AcxodAgIlMGrz8YEW7UdVaJFZzzx4vnP5YMBsOrYFQLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولید غضبان (دیپلمات اسرائیلی و مشاور در وزارت امور خارجه اسرائیل):
«اسرائیل او را از میان برداشت، اما قاب عکسش مجبور شد تمام آن سخنرانی را تحمل کند؛ به‌ویژه آن بخشی که نتانیاهو با شور و حرارت از فروپاشی جمهوری اسلامی حرف می‌زد»
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24128" target="_blank">📅 12:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24127">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">وال‌استریت ژورنال:
میانجی‌ها
در تلاش‌اند
دور جدید مذاکرات میان آمریکا و ایران را
اوایل هفته آینده در عمان
برگزار کنند؛ مذاکراتی که محور آن بازگشایی تنگه هرمز و تلاش برای پایان جنگ است. این مذاکرات هنوز قطعی اعلام نشده و در مرحله رایزنی قرار دارد.
@WarRoom
حقیقت یاب اتاق جنگ : این اصل خیر است ، مذاکرات هنوز نهایی‌نشده و خبر رسانه های زد فیک نیوز است</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/24127" target="_blank">📅 12:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24126">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دریادار رابرت هاروارد، معاون پیشین فرمانده سنتکام:
«من ذهنیت مردم زیبای ایران را می‌شناسم. آنها به آزادی و زندگی باور دارند. ایران نخستین کشوری بود که منشور حقوق بشر داشت. من
متعهد
به کمک به همه شما هستم.»
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/24126" target="_blank">📅 11:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24125">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDdET9NxlwXQET1bTfTSQOFqtE6Uc_YnDtgkIG4amSDVu-fPBUvem2Z9jTgN-NwdxU3IZcMBfsR9iIKExihAUK7KkY8RU1Ob5ZreqGc1teIIksE-CYM0-dAigsXB7Qz4HHbRQFGDnkt84CQT-EwNqmTR81bSi_pvtyEoOPBd_BFFeykx_90WZOqq-wBHWAf6E0qPhPdfz3lHj9rRyf_NNSvzAnwOyUJx-vvVGBfq8SZRxRjpGRRHg6N2xZWKknGx5G9vPBn-tgoz0OfeUqcLmjmCOTHaNB9ifmYfPsCxGfS_kE7x7iFuMvawwZQu4PrI7f4tiDjBAx-_cWw92p3EEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پی۸ پوسایدون ، ام ۴۰۰ (نمونه مشاهبه هرکولس از ایرباس) و ۴ سوخترسان هم اکنون در حال انجام مأموریت در منطقه خلیج فارس و تنگه
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/24125" target="_blank">📅 11:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24124">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‏ نتانیاهو در پاسخ به خبرنگاری که پرسید پیامش برای مردم ایران چیست،گفت :
«ما با شما هستیم. ناامید نشوید.»
@WarRoom</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/withyashar/24124" target="_blank">📅 11:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24123">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ان‌بی‌سی نیوز:
عباس عراقچی، وزیر امور خارجه ایران، در نیویورک به خبرنگاران گفت تهران از طریق میانجی‌ها طرحی را به مقام‌های آمریکایی ارائه کرده که در صورت پذیرش شروط ایران،
پس از هفت روز به بازگشایی تنگه هرمز و ازسرگیری مذاکرات
منجر خواهد شد. به گفته عراقچی، یکی از شروط طرح، پذیرش مسیر عبور دریایی مورد توافق ایران و عمان در تنگه هرمز است. ان‌بی‌سی نیوز گزارش داد کاخ سفید تا زمان انتشار این گزارش به درخواست اظهارنظر درباره این طرح پاسخ نداده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/24123" target="_blank">📅 11:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24122">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">جروزالم پست:
نیروهای دولت یمن حمله حوثی‌ها به یک مسیر مهم تدارکاتی میان عدن و تعز را دفع کرده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/24122" target="_blank">📅 11:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24121">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کوین‌دسک
:
حدود
۱۸ میلیارد دلار قرارداد آپشن بیت‌کوین و اتر
امروز منقضی می‌شود؛ حجم بالای سررسید می‌تواند در کوتاه‌مدت نوسانات بازار و جریان‌های هجینگ را افزایش دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/withyashar/24121" target="_blank">📅 10:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24120">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">رویترز:
تعداد عبور کشتی‌ها از تنگه هرمز در روز پنجشنبه به ۹ فروند کاهش یافته، در حالی که روز قبل ۱۴ فروند و میانگین ۱۰ روزه حدود ۱۸ فروند بوده است؛ البته کشتی‌هایی اصلی که انتقال را انجام میدهند و ترانسپوندر خود را خاموش کرده‌اند در این آمار نیستند.
@WarRoom</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/24120" target="_blank">📅 10:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24119">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYwXw38Y4-FYzEgGkm9gt6SAKYiggEc0wV2YlaFuyUWlPMnxjhZCO45XYO0JZmQC9hYLE5k23X_zhkMQDuoB4lvS7CMmRktEKnTAqxAo9LDH2V0XJydyKKK2cvY1l70GAjH4UgFF4TTXQgrYT8bZvyB-UgN-OnYXFvAkXPys-O5vP-xVgdqDccJtK3Uos71asG-_Bf0nXPAl5UGkgAecvP7Rq3ut6lnu2nvAkMZoLSqCkx1ML7SNbS59MPJAF-mqfklN7fWJg4G_4gaFnM9MCNa1DMHXrcQ6DyHFVmQQwyXpjTablAPq1x-hDcLRz9hOQESLvOw0ElyOxUjuzuoDwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وار زون
:
یک فروند جاسوسی SR-71 Blackbird با شماره
NASA 844
، آخرین SR-71 پروازکننده در تاریخ، از محل نمایش عمومی خود در مرکز تحقیقات پرواز آرمسترانگ ناسا در پایگاه ادواردز ناپدید شده و اوایل امسال به یک آشیانه دیگر منتقل شده است. این اتفاق پس از انتشار تصویری مرموز از سوی جرد آیزاکمن، مدیر ناسا، از یک هواپیمای سیاه شبیه SR-71 و صحبت‌های او درباره بازگشت به پروازهای بسیار سریع و در ارتفاع بالا رخ داده است. انتقال این هواپیما احتمال استفاده مجدد از آن یا حتی انجام یک مأموریت پروازی محرمانه جاسوسی را مطرح کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/24119" target="_blank">📅 10:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24118">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‏دانیل رافکاس، قاضی فدرال آرژانتین، برای هفت مقام و شهروند ایرانی و یک عضو حزب‌الله لبنان در پرونده بمب‌گذاری مرکز یهودیان آمیا قرار تعقیب صادر و مسیر محاکمه غیابی آنان را باز کرد. محسن رضایی و احمد وحیدی از جمله متهمانی هستند که دستگاه قضایی آرژانتین آنان را به نقش داشتن در تصمیم‌گیری و طراحی حمله متهم کرده است. بر اساس این حکم، توقیف دارایی‌های هر متهم تا سقف ۵۰۰ میلیون دلار نیز دستور داده شده است. بمب‌گذاری آمیا در سال ۱۹۹۴ به کشته‌شدن ۸۵ نفر انجامید.
@WarRoom</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/withyashar/24118" target="_blank">📅 10:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24117">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یه عده سیاه پوست و محجبه سالن رو ترک کردن  @WarRoom</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/withyashar/24117" target="_blank">📅 10:17 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24116">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">نیویورک‌پست: سنای آمریکا بار دیگر طرحی برای محدود کردن اختیارات جنگی ترامپ در جنگ ایران را رد کرد؛ این رأی به معنای حفظ اختیارات فعلی رئیس‌جمهور آمریکا برای ادامه عملیات نظامی است. @WarRoom</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/24116" target="_blank">📅 10:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24115">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">جروزالم پست:
عمان هم پروازهای شرکت‌های هواپیمایی ایرانی را تا اطلاع ثانوی متوقف کرد؛ این تصمیم به تحریم‌های جدید آمریکا علیه بخش هوانوردی ایران اعلام شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/24115" target="_blank">📅 09:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24114">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">رویترز:
عربستان سعودی، ترکیه و پاکستان قرار است در پی تشدید حملات حوثی‌ها، نشست فوری فرماندهان ارشد نظامی برگزار کنند؛ این نشست در چارچوب پیمان دفاعی مشترک سه کشور انجام می‌شود.
همچنین مقام مذهبی ارشد عربستان از نیروهای نظامی این کشور خواست برای مقابله با حوثی‌ها آماده فدا کردن جان خود باشند.
@WarRoom</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/withyashar/24114" target="_blank">📅 09:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24113">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">وال استریت جورنال: بن سلمان ولیعهد عربستان سعودی اخیراً به مسئولین آمریکایی اطلاع داده است که ایالات متحده باید به تحریم‌های دریایی ادامه دهد تا تهران را مجبور به امضای یک توافقنامه جدید کند.
@WarRoom</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/24113" target="_blank">📅 09:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24112">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">کلمبیا در مجمع عمومی سازمان ملل متحد، قطع روابط دیپلماتیک با ایران را اعلام کرد. @WarRoom امشب الهیه صف سفید‌ بازاست فردا قیمت میره بالا
❄️
😂</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/24112" target="_blank">📅 09:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24111">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ادعای احمد بخشایش‌اردستانی، عضو کمیسیون امنیت ملی مجلس: او مدعی شد شنیده است که ایران از کره‌شمالی سلاح هسته‌ای خریداری کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/24111" target="_blank">📅 09:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24110">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مصاحبه‌کننده:
«پس آیا تصاویر ماهواره‌ای چین به کشته شدن سربازان آمریکایی به دست ایران کمک کرد؟»
پزشکیان:
«ما به دنبال کشتن آمریکایی‌ها نیستیم. همان‌طور که اقدامات، اقدامات قابل اثبات، نشان داده‌اند، آمریکا به دنبال کشتن ایرانی‌ها بوده است.»
مصاحبه‌کننده:
«اما آنها در آنجا کشته شدند، آیا شما از تصاویر ماهواره‌ای چین استفاده کردید؟»
پزشکیان:
«نه. اصلاً. نه. نه. اول از همه، من مشخصاً از این تصاویر گزارش‌شده و ادعایی که شما درباره آنها صحبت می‌کنید، اطلاعی ندارم.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24110" target="_blank">📅 03:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24109">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">شی جین‌پینگ: امروز من و ترامپ گفت‌وگویی صادقانه و عمیق داشتیم و درباره بسیاری از مسائل به تفاهم مشترک رسیدیم. این تفاهم، محتوای جدیدی به روابط سازنده چین و آمریکا با هدف ثبات راهبردی اضافه کرده و راهنمایی راهبردی جدیدی برای روابط دو کشور فراهم کرده است. @WarRoom…</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24109" target="_blank">📅 03:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24108">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/24108" target="_blank">📅 03:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24107">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/519484d74f.mp4?token=gSCqAPElk6JpTzXHePPZ1mrpt3ObVz32ZNgFWYEtLKl-ng1rnYGQwWVHWveTTZXWgvN54lp23IUEwzhdg7kNYGmlNSNwZk0jIEU5jlN7hZT0MKW39q-TJGOGyzc6jsaqXFcxLc5d4GE5RrtfBFR0G09G3Xo-r8JZgDpafcz-DHbf3knHMRdHqaQPFlYpsSt-nRU8A4C82dD8YGW7tG0mFMuLKlJvyIGboN4nkKh36ClR5TiDYY_8NaQNfjsCtzNj1eilQWT7Pzu6E5Bq-F3gKLK8W-0zmuT8_FuwgTLhcDP2TQehNy8HrIXerBnppzgrxdf5CJ9BrEEhbjAzbzZ1mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/519484d74f.mp4?token=gSCqAPElk6JpTzXHePPZ1mrpt3ObVz32ZNgFWYEtLKl-ng1rnYGQwWVHWveTTZXWgvN54lp23IUEwzhdg7kNYGmlNSNwZk0jIEU5jlN7hZT0MKW39q-TJGOGyzc6jsaqXFcxLc5d4GE5RrtfBFR0G09G3Xo-r8JZgDpafcz-DHbf3knHMRdHqaQPFlYpsSt-nRU8A4C82dD8YGW7tG0mFMuLKlJvyIGboN4nkKh36ClR5TiDYY_8NaQNfjsCtzNj1eilQWT7Pzu6E5Bq-F3gKLK8W-0zmuT8_FuwgTLhcDP2TQehNy8HrIXerBnppzgrxdf5CJ9BrEEhbjAzbzZ1mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شی جین‌پینگ:
امروز من و ترامپ
گفت‌وگویی صادقانه و عمیق
داشتیم و درباره بسیاری از مسائل به
تفاهم مشترک
رسیدیم. این تفاهم، محتوای جدیدی به روابط سازنده چین و آمریکا با هدف
ثبات راهبردی
اضافه کرده و
راهنمایی راهبردی جدیدی برای روابط دو کشور
فراهم کرده است.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24107" target="_blank">📅 03:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24106">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d93f107e3.mp4?token=dTNcqIWxqixUoCWbCYRJj4-pv558mfnrcJpQ-1DHXrobek4-mEwdKjp3DU9vJyjNZmY8DBdeOzL2aPPOPmNEpTNV8YWQsnupe1skr3Z9b6PlLUB0zptYtFZHVeSUdbeoVDUtRXJh9PL9ayWz984zmQEN8JGg8CnaVccCbG83CcRHjST9zJlYHFKNJz6iOv9ZTmUVitFWQmsQrEIhCihl8uGQXwdttPwHstQ5ygMeUWdWI9P3MEeBC0Bz-6j82aUhASFBpkseh4MLSnwDKWMullczVRDLr2cFabtJxzp-lbQk4GpvcEttXBNE9fSkNLZdz4hNlT174LvK0RmlLhg0zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d93f107e3.mp4?token=dTNcqIWxqixUoCWbCYRJj4-pv558mfnrcJpQ-1DHXrobek4-mEwdKjp3DU9vJyjNZmY8DBdeOzL2aPPOPmNEpTNV8YWQsnupe1skr3Z9b6PlLUB0zptYtFZHVeSUdbeoVDUtRXJh9PL9ayWz984zmQEN8JGg8CnaVccCbG83CcRHjST9zJlYHFKNJz6iOv9ZTmUVitFWQmsQrEIhCihl8uGQXwdttPwHstQ5ygMeUWdWI9P3MEeBC0Bz-6j82aUhASFBpkseh4MLSnwDKWMullczVRDLr2cFabtJxzp-lbQk4GpvcEttXBNE9fSkNLZdz4hNlT174LvK0RmlLhg0zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ
به
رئیس‌جمهور شی جین‌پینگ هدیه‌ای
داد
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/24106" target="_blank">📅 03:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24105">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90b4fb0cfe.mp4?token=OSpIyBci2JQlk3H1pjmoQHE6tj3ef6uaRVJ2u7CtO0MsrSnvruAgcorLtK0HHTbsfPpTYqK6pIRdMRfFxHAwyrNgtbIC3oxpXF9Fj3zQ1M0JImGZ20eFENZM1pgmTTFaMc4YDXGhF5mYgUZ2Ttx6lGCAl-pHebgoxAiKdDnLSYHRbE78p2OHTqQGqUhAB9gpL9aPfQg9rKm10cxqrg9Kx0TvTG0ZyP4g___GbT7OTM16QQMFvlNI2u4KUYkeV9YlE74lqB9Qs8IUnm7D7YnAb8RMKxA7WWYol_b25G21zVGEnFI5UFn5yx-M7UrBQfxqSvnkCouiw3uLBCJFkftOFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90b4fb0cfe.mp4?token=OSpIyBci2JQlk3H1pjmoQHE6tj3ef6uaRVJ2u7CtO0MsrSnvruAgcorLtK0HHTbsfPpTYqK6pIRdMRfFxHAwyrNgtbIC3oxpXF9Fj3zQ1M0JImGZ20eFENZM1pgmTTFaMc4YDXGhF5mYgUZ2Ttx6lGCAl-pHebgoxAiKdDnLSYHRbE78p2OHTqQGqUhAB9gpL9aPfQg9rKm10cxqrg9Kx0TvTG0ZyP4g___GbT7OTM16QQMFvlNI2u4KUYkeV9YlE74lqB9Qs8IUnm7D7YnAb8RMKxA7WWYol_b25G21zVGEnFI5UFn5yx-M7UrBQfxqSvnkCouiw3uLBCJFkftOFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
من و شی هر دو می‌دانیم که نماینده
نظام‌های متفاوتی
هستیم، اما روابط میان مردم دو کشور همچنان پابرجاست و
هیچ‌وقت به اندازه امروز روابط خوبی با یکدیگر نداشته‌ایم.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/24105" target="_blank">📅 03:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24104">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48d197af82.mp4?token=T9XPP6PHBHSp2YyoHYTVml5GDTF6Gcfbh43iU4K1JobEMJC9poocc-Bep53FDjwZCol41sTttJurDd--XuY4_iUnCoTpc8SHG_JpqYsOrpATp34ypCrktO2omZcPvYTnFVWi9Fbc_yCtJbQCekpi0WySzhlPnB1a2RlMZIwZQ1qY2A5NkWAnQbOlUqDcthiKxPrnzphhFLfWpNn4lhfuW5N8okH0VixhJ_sYvatqj8g_qb7BeY-TWCDb7jT-Mke7x_sMDy30NoPdhfrMN9-Y-Kx6GxejU-7vW-OWY5FkoPcQaPzVbJqQsEAQ5ZOgtIIpn7_wwlWp3eC3vIDKIj6D7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48d197af82.mp4?token=T9XPP6PHBHSp2YyoHYTVml5GDTF6Gcfbh43iU4K1JobEMJC9poocc-Bep53FDjwZCol41sTttJurDd--XuY4_iUnCoTpc8SHG_JpqYsOrpATp34ypCrktO2omZcPvYTnFVWi9Fbc_yCtJbQCekpi0WySzhlPnB1a2RlMZIwZQ1qY2A5NkWAnQbOlUqDcthiKxPrnzphhFLfWpNn4lhfuW5N8okH0VixhJ_sYvatqj8g_qb7BeY-TWCDb7jT-Mke7x_sMDy30NoPdhfrMN9-Y-Kx6GxejU-7vW-OWY5FkoPcQaPzVbJqQsEAQ5ZOgtIIpn7_wwlWp3eC3vIDKIj6D7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سؤال: آیا غنی‌سازی اورانیوم ۶۰ درصد را کنار می‌گذارید؟
مسعود پزشکیان:
بله،
در چارچوب قوانین بین‌المللی و بر اساس معاهده منع گسترش سلاح‌های هسته‌ای (NPT)
. هر چیزی که موظف به رعایت آن باشیم، رعایت خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/24104" target="_blank">📅 03:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24103">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
حوثی‌ها مسئول اقدامات خودشان هستند و از ما دستور نمی‌گیرند. ما به‌عنوان کسانی که در منطقه مقاومت می‌کنند و با توجه به شرایطی که به آنها تحمیل شده، با آنها در ارتباط هستیم؛ اما
هیچ رابطه سازمان‌یافته‌ای میان ما وجود ندارد.
@WarRoom</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/24103" target="_blank">📅 03:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24102">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/24102" target="_blank">📅 03:17 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24101">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">تصاویر نمای نزدیک و چشمگیر از بمب‌افکن راهبردی B-21 نیروی هوایی آمریکا (نسل جدید B2)
که امروز برای انجام آزمایش‌های پروازی از پایگاه نیروی هوایی ادواردز در کالیفرنیا به پرواز درآمد.
این بمب افکن مخوف هنوز عملیاتی ‌نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/24101" target="_blank">📅 03:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24100">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48f0f08a00.mp4?token=NkeoTc9zwI_Zn0J1wRYhDJETkyw1i3fip-3NzXAXz0T8vwySMZvev3KY3gQhylA71eycZn7OgAVQmo9jlB0RufBwnDaovEhVs45drLn1Attf6MFH7MWnYiplKTKjqNy0dyN4slTVcOOPppzcKS1aIfZFUJruNpNSUc0eUFf8YENqKmNramoMMR0dXra7HU_COpallmWjZYxHE1TbTFbAs6V96Lj9LkqFPHXGS_msz9eIc5PUItqW2NJBsq0JrEQ1vyVaF8H51mjE7RFbdEFPgvl2a4irskY8LC2GHaqr8IxlodU1YMjHNBfuVwitMLqEcJ4Yvvm_CpKwmHP7-9WleCEF35pI0aZorN8V4oyfkX2_S0B93bes3oJFYkuoDRAnLu-QdAtqIEIQraRFYx1W9B1DCO94U55C0KZA7YPm1-IYFlKQpzoDxhFEDsxaEhrimBY4N7GXXOMa1d7_Jy5oWSMyAJnVyaC7ExgDUsSJPvZX1tlt6oy9LjuZ1fYDPGJdEhhnGhRNL1emIG8xtWHGYOqjRDd_GHxStMprU8smkL-gHNGoU6OHqv2goKUWwc43S4Ll0v1FK6eth9i5u42Y0e9Oa3T38GIes11f8v9MohJaWvXQZRZujSxB4poDQKN8keC_SEPOGHBSeG3iGkkGAuKDX6dIPZXCva_1Ib_KJd0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48f0f08a00.mp4?token=NkeoTc9zwI_Zn0J1wRYhDJETkyw1i3fip-3NzXAXz0T8vwySMZvev3KY3gQhylA71eycZn7OgAVQmo9jlB0RufBwnDaovEhVs45drLn1Attf6MFH7MWnYiplKTKjqNy0dyN4slTVcOOPppzcKS1aIfZFUJruNpNSUc0eUFf8YENqKmNramoMMR0dXra7HU_COpallmWjZYxHE1TbTFbAs6V96Lj9LkqFPHXGS_msz9eIc5PUItqW2NJBsq0JrEQ1vyVaF8H51mjE7RFbdEFPgvl2a4irskY8LC2GHaqr8IxlodU1YMjHNBfuVwitMLqEcJ4Yvvm_CpKwmHP7-9WleCEF35pI0aZorN8V4oyfkX2_S0B93bes3oJFYkuoDRAnLu-QdAtqIEIQraRFYx1W9B1DCO94U55C0KZA7YPm1-IYFlKQpzoDxhFEDsxaEhrimBY4N7GXXOMa1d7_Jy5oWSMyAJnVyaC7ExgDUsSJPvZX1tlt6oy9LjuZ1fYDPGJdEhhnGhRNL1emIG8xtWHGYOqjRDd_GHxStMprU8smkL-gHNGoU6OHqv2goKUWwc43S4Ll0v1FK6eth9i5u42Y0e9Oa3T38GIes11f8v9MohJaWvXQZRZujSxB4poDQKN8keC_SEPOGHBSeG3iGkkGAuKDX6dIPZXCva_1Ib_KJd0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ و ملانیا ترامپ
در کاخ سفید از
شی جین‌پینگ، رئیس‌جمهور چین، و همسرش پنگ لی‌یوان
برای ضیافت شام رسمی دولتی استقبال کردند.
خبرنگاران CNN و MS NOW
اجازه پوشش و حضور در مراسم ورود شی جین‌پینگ به کاخ سفید برای این ضیافت شام رسمی را دریافت نکردند.
@WarRoom</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/24100" target="_blank">📅 02:47 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24099">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/684edd63a4.mp4?token=Tg0zF5bByNCG0gkLN4K1-s9RUJ8TLXMMFfjtaK-bNnkqP9vqpifrf9h1dCX-2HXm7ypqdMvFhk2q7gCbiMGS1nziY9D4f-8pyP3vdhgYXsU30MHI5aNPOBvtrXpm-_nERFJo8-U0-7M6VFAG6IX9IANCXcUzvSaKWb8H6P1uoFfnAeR00XuGKrb6pvVo9DJSwE9cDmvTqL9VdtETIAxI8EWpw4D6ymFL1i0mWgN9bdf9pB149lpOvGNiu2qBAFCheLbs2Zb40gqo6gRKpf-2GzHdcZNXesnK0p-7SuYnTetCICKVfV0sA3W916JUCVjjNBefdzG2YEu81tUKGqZ2QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/684edd63a4.mp4?token=Tg0zF5bByNCG0gkLN4K1-s9RUJ8TLXMMFfjtaK-bNnkqP9vqpifrf9h1dCX-2HXm7ypqdMvFhk2q7gCbiMGS1nziY9D4f-8pyP3vdhgYXsU30MHI5aNPOBvtrXpm-_nERFJo8-U0-7M6VFAG6IX9IANCXcUzvSaKWb8H6P1uoFfnAeR00XuGKrb6pvVo9DJSwE9cDmvTqL9VdtETIAxI8EWpw4D6ymFL1i0mWgN9bdf9pB149lpOvGNiu2qBAFCheLbs2Zb40gqo6gRKpf-2GzHdcZNXesnK0p-7SuYnTetCICKVfV0sA3W916JUCVjjNBefdzG2YEu81tUKGqZ2QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان :
ما هرگز به مردم خودمان حمله نمی‌کنیم.
برت بایر، خبرنگار فاکس نیوز:
اما این کار را کردید.
پزشکیان:
نه، نه. چه کسی علیه ما اقدامات تروریستی انجام داد؟ چه کسی به مدارس ما حمله کرد؟
بایر:
متوجه هستم، اما در روزهای ۸ و ۹ ژانویه، نیروهای امنیتی شما قطعاً شهروندان ایرانی را کشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/24099" target="_blank">📅 02:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24098">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">مسعود پزشکیان درباره اعتراضات ژانویه:
خود آقای ترامپ اعلام کرد که آمریکا این افراد را تجهیز و مسلح کرده بود تا دولت ایران را سرنگون کنند. افراد نتانیاهو اعلام کردند که نیروهایی از استان‌های کردستان و بلوچستان وارد مراکز کلان‌شهری خواهند شد تا دولت را سرنگون کنند. آنها تصور می‌کردند این ماجرا سه‌روزه خواهد بود و دولت سقوط خواهد کرد، اما دولت ایستادگی کرد، منسجم‌تر شد و اتحاد بیشتری پیدا کرد. حتی کسانی که به دلایل مختلف در برابر دولت ایران ایستاده و با ما مخالف بودند، اکنون از ایران حمایت می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/24098" target="_blank">📅 02:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24097">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">از وسطش +۱۸ هست</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/24097" target="_blank">📅 02:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24096">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/withyashar/24096" target="_blank">📅 02:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24095">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
ما
تا آخرین لحظه به مقاومت ادامه خواهیم داد
. بله، قطعاً با مشکلات اقتصادی مواجه هستیم، اما برای اینکه بتوانیم پابرجا بمانیم،
هر سختی و فشاری را تحمل خواهیم کرد و از آن عبور می‌کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/24095" target="_blank">📅 02:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24094">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
ترامپ مدام می‌گفت «می‌خواهم برای مردم ایران هدیه بیاورم»، اما هدیه‌ای که آنها برای ما آوردند
موشک‌های هدایت‌شونده، سلاح‌های سنگین و ویرانی
بود. آنچه آنها واقعاً می‌خواهند انجام دهند،
ایجاد و تحریک حوادث و ناآرامی‌هایی در داخل کشور است که زمینه را برای فروپاشی نظام، جامعه و دولت فراهم کند.
@WarRoom</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/24094" target="_blank">📅 02:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24093">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
اگر دولت کنونی آمریکا بخواهد
در چارچوب قوانین بین‌المللی
به توافق برسد، بسیار خوب. اما اگر نخواهد،
برای ما چه تفاوتی دارد که این اتفاق قبل از انتخابات آمریکا باشد یا بعد از آن؟
@WarRoom</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/withyashar/24093" target="_blank">📅 02:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24092">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
هرکس بخواهد اعتراض کند،
کاملاً حق دارد این کار را انجام دهد
. ما با بسیاری از این معترضان نشستیم و با آنها گفت‌وگو کردیم؛ اما
مسلح‌کردن اعتراضات و تبدیل آنها به ابزار درگیری، موضوع کاملاً متفاوتی است.
@WarRoom</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/24092" target="_blank">📅 02:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24091">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
یکی از مشکلاتی که با آن مواجه هستیم این است که
پول ایران در چین مسدود شده است
. ما حتی نمی‌توانیم پول خودمان را از کشوری که در ازای آن به آن کالا صادر کرده‌ایم، خارج کنیم؛ چه رسد به اینکه بتوانیم از این منابع برای پرداخت به فرد یا طرف دیگری در نقطه‌ای دیگر از جهان استفاده کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/withyashar/24091" target="_blank">📅 02:17 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24090">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مسعود پزشکیان:
ما با ترامپ به توافق رسیدیم. آن توافق امضا شد و بر اساس همان توافق، ما آماده بودیم و همچنان مایل هستیم که مسیر را ادامه دهیم و چارچوب آن نیز مورد توافق قرار گرفته بود. ما تنگه هرمز را نبسته بودیم و تنگه باز بود؛ اما آنها بدون هیچ توجیه یا چارچوب قانونی به ما حمله کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/withyashar/24090" target="_blank">📅 02:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24089">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مسعود پزشکیان:
ما جنگ را انتخاب نکردیم؛ جنگ به ما تحمیل شد. ما به‌دنبال جنگ نیستیم، بلکه هر زمان به ما حمله شود، مجبوریم از خودمان دفاع کنیم. ما هرگز آغازکننده جنگ نبوده‌ایم، اما اگر آنها بخواهند به جنگ با ما ادامه دهند، با قدرت پاسخ خواهیم داد
@WarRoom</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/withyashar/24089" target="_blank">📅 02:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24088">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00e58f2038.mp4?token=IDDvQRvkF2ooHd1S8XB4HRqitjAWsp1a6kWtGcVeMWjRMv7rNwejE3jnex0faPUjbolQ5G_Wf-JQZOGHPt3vb0IywLKbeioEuavC7Il8KwRqH7wx-EmFmuKGc4zUeCW0p_Oio6qC1NXQ9oqD3CV1Z2AYzxW0syAJ_BXR7iHUgan-K9xj3GXwTqb0gbAARG9-TjYUnxpwQAC51SlCc_HYKfHCZBDF3O9KbDzH7Q1XHPNOh8K44E80a4AkqTID-039n4I0864VXedN-78vzZ14AO45i5-jECKNmx10Hgnd_u4qz_jNshNFBZi6QCmZ_dIdotXTJPMh3w4kLxRa7b-8RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00e58f2038.mp4?token=IDDvQRvkF2ooHd1S8XB4HRqitjAWsp1a6kWtGcVeMWjRMv7rNwejE3jnex0faPUjbolQ5G_Wf-JQZOGHPt3vb0IywLKbeioEuavC7Il8KwRqH7wx-EmFmuKGc4zUeCW0p_Oio6qC1NXQ9oqD3CV1Z2AYzxW0syAJ_BXR7iHUgan-K9xj3GXwTqb0gbAARG9-TjYUnxpwQAC51SlCc_HYKfHCZBDF3O9KbDzH7Q1XHPNOh8K44E80a4AkqTID-039n4I0864VXedN-78vzZ14AO45i5-jECKNmx10Hgnd_u4qz_jNshNFBZi6QCmZ_dIdotXTJPMh3w4kLxRa7b-8RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری فاکس‌نیوز: آقای رئیس‌جمهور، منظورم همان حادثه ژانویه است. شما جراح قلب هستید.
نیروهای امنیتی ایران چند ایرانی را کشتند؟
پزشکیان: ببینید چندان هم دشوار نیست. می‌توانید افرادی را به آنجا بفرستید تا حقیقت را مشخص و احراز کنند. آنچه فلان و بهمان نشریه در خارج از کشور گزارش می‌کند، با روایت دقیق و مستند از وقایع مطابقت ندارد. وقتی می‌گویند ۱۰ هزار نفر یا ۱۷ هزار نفر، چرا دست‌کم دو شماره ملی ارائه نمی‌کنند؟
@WarRoom</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/24088" target="_blank">📅 02:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24087">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/withyashar/24087" target="_blank">📅 02:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24086">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c08c2421f.mp4?token=jGbqiRrVmmfmTZImnmPSKGQBR8ksw9_V0kRZIlbFifGlKiyv1wA_64zo18e8bPUTSq5mGnFzQ3u2V3ViXAVoAYnsXELS-oM4uA8PFN_fHw-k1-IiLnw-1O2EaUlxXGnj1Z4LAaz-X_h239Rg0jLyEDJXak2K16kRm3T5mNVHZ1bvHKVZCPSaZcOqTF1hK-xBM1mCgLkBFcPTFU1DGkZ0yc0i6XzVy7k9NzEm-oEQ287tGtpLaXCphwBb8hRuhL_xwSuvEp02OeseITVwVBil34TkEe8mX3TEXr00LlsVN0dYgTfErotmI0TUpGoFbQLmLaSk4uU0TiWUKpr2BOjPKnHxY6QG04WflRyCnB_-pndpnY2hOJKCtYESDDEIkz--SJqf2ksKNYiYEA1AOh3MYnbgZUlFTJIf3iAqy7BGRelC3J-c1Zn8Gt3EMNHujv9WkrVvo6XeXe1BzE-XifHoBTsOK74Z8AL743vht5Pc4d4SlB1UM-mPzlDZuwwYJe37WqJYbDqlOP0li7zGfPpvfLcdHQhZ6zD3OlPun4ngJq4hPENEOsoeDj1nSqtKuvdqUEdI-eIsTqWXzLHKMvAnTUQaK_FIudYbi1Qd1747jlRA3oxNNwCpcLXNeE23d2JSwswsBX09TbMqSQIWcxurKKqG_dwVAij_wxttbcluRj0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c08c2421f.mp4?token=jGbqiRrVmmfmTZImnmPSKGQBR8ksw9_V0kRZIlbFifGlKiyv1wA_64zo18e8bPUTSq5mGnFzQ3u2V3ViXAVoAYnsXELS-oM4uA8PFN_fHw-k1-IiLnw-1O2EaUlxXGnj1Z4LAaz-X_h239Rg0jLyEDJXak2K16kRm3T5mNVHZ1bvHKVZCPSaZcOqTF1hK-xBM1mCgLkBFcPTFU1DGkZ0yc0i6XzVy7k9NzEm-oEQ287tGtpLaXCphwBb8hRuhL_xwSuvEp02OeseITVwVBil34TkEe8mX3TEXr00LlsVN0dYgTfErotmI0TUpGoFbQLmLaSk4uU0TiWUKpr2BOjPKnHxY6QG04WflRyCnB_-pndpnY2hOJKCtYESDDEIkz--SJqf2ksKNYiYEA1AOh3MYnbgZUlFTJIf3iAqy7BGRelC3J-c1Zn8Gt3EMNHujv9WkrVvo6XeXe1BzE-XifHoBTsOK74Z8AL743vht5Pc4d4SlB1UM-mPzlDZuwwYJe37WqJYbDqlOP0li7zGfPpvfLcdHQhZ6zD3OlPun4ngJq4hPENEOsoeDj1nSqtKuvdqUEdI-eIsTqWXzLHKMvAnTUQaK_FIudYbi1Qd1747jlRA3oxNNwCpcLXNeE23d2JSwswsBX09TbMqSQIWcxurKKqG_dwVAij_wxttbcluRj0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج پیغام های  شما از گزارش عجیب ایران اینرنشنال توسط مجری افغان این شبکه مرضیه حسینی که مجاهدین خلق رو مردم ایران میدونه و پرچم جعلی اونها رو پرچم شیرو خورشید عنوان میکنه ! و پروموتشون میکنه !
@WarRoom</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/withyashar/24086" target="_blank">📅 02:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24085">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">کلمبیا در مجمع عمومی سازمان ملل متحد، قطع روابط دیپلماتیک با ایران را اعلام کرد.
@WarRoom
امشب الهیه صف سفید‌ بازاست فردا قیمت میره بالا
❄️
😂</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/24085" target="_blank">📅 01:47 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24084">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulbB09V3cc5xEgbKjm5v6otIGWU4Xu0MFhUVBs3Pj4asLHd1ECJS-oIFjnLIafRuDDyhP5ImZgu8frd2UH98XWyPjkazSLRmBTI7Nlm_hOt23Vftlo-iciWdcx0Mfnu5sLYr0f0h_dBQc5xfA4M1n7fKpo6RGPSwWlsotan-aD9_VeJObrZiu-q13kBy6QugWLtcFGVGE2WjVBeljQ1V8e5jQpJxynrmnMGEPpVNKEkQHcAdFWaIjyH7UZ4AY_vf7SECjW1Xu3M-8Qfz3LfMHN8zoJq1X7cEdLGYwBfGQpF7_0fALS00cvw6H9F6r3K42cWjpnvFxpM452Uq6vgTTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده اسرائیل یه استارلینک میبره برای نمایندهی ایران در صحن سازمان ملل و می‌گه اینو بگیر به کارت میاد. و می‌گه ما عاشق مردم ایران هستیم و برای تغییر رژیم دعا می‌کنیم. @WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/24084" target="_blank">📅 01:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24083">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/137bb832f8.mp4?token=bX5_DS3swzyiIoTSpsiO_RoYX9LtWpMUoLTO1GFVMgINsJniftU9poucigXSSgZnVxwjVjvjPln1wZyNNBDC4UUXtIwECzExmI0AMQr1d1BlaOcFzWrFsyk0c-U47_PsAXa7vu-GwtJCxcWDDYHD0NYA2V49LEd9oZm5nglNP6aJL3WHj0x6LCnf6hldiOIBCE2DSf1UG-aBem8Sknl0873Atz5NbKwAP56Pa2d7N9vGwnSSgu9hugpphvwK-EadhqxaFdYzU229k2aD7z_URCJsDP3Rz02xvz1JsUuouc-wFQdXjpG3coIfS4Znl7Rb9pwfQRVQV13TBp1gujAd0zXojYsyxLFBD0OoTHVhk6LhuGZryPJMYL5wrtlBDlBXNljCZRm_IMCZtNZ7f7-SmTMsLv5LU68oaYZrDR484Kub4_5zG8OgQSkQPyO1x_rBzhJFkREMI4MS55lJdIQGXdO4z_OItsKW2oY-OkXsNA9EVUxMamErf1NF39BmrdzLAZNUWAeuMq3gSNubCbbg8cPwyLjMmcP0affFij-BKPuclhAWNmgZe3t5v61nHy2dBgZ3qpxyrzVxOqwTanHl2kP8U6DJt85e3Jm1X5NdhNO5ZqD2AdfkD4HW83A32wy_H1tPhWphp3bfpw61aggcjg1lX55pK45fO-u5SbHiLMU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/137bb832f8.mp4?token=bX5_DS3swzyiIoTSpsiO_RoYX9LtWpMUoLTO1GFVMgINsJniftU9poucigXSSgZnVxwjVjvjPln1wZyNNBDC4UUXtIwECzExmI0AMQr1d1BlaOcFzWrFsyk0c-U47_PsAXa7vu-GwtJCxcWDDYHD0NYA2V49LEd9oZm5nglNP6aJL3WHj0x6LCnf6hldiOIBCE2DSf1UG-aBem8Sknl0873Atz5NbKwAP56Pa2d7N9vGwnSSgu9hugpphvwK-EadhqxaFdYzU229k2aD7z_URCJsDP3Rz02xvz1JsUuouc-wFQdXjpG3coIfS4Znl7Rb9pwfQRVQV13TBp1gujAd0zXojYsyxLFBD0OoTHVhk6LhuGZryPJMYL5wrtlBDlBXNljCZRm_IMCZtNZ7f7-SmTMsLv5LU68oaYZrDR484Kub4_5zG8OgQSkQPyO1x_rBzhJFkREMI4MS55lJdIQGXdO4z_OItsKW2oY-OkXsNA9EVUxMamErf1NF39BmrdzLAZNUWAeuMq3gSNubCbbg8cPwyLjMmcP0affFij-BKPuclhAWNmgZe3t5v61nHy2dBgZ3qpxyrzVxOqwTanHl2kP8U6DJt85e3Jm1X5NdhNO5ZqD2AdfkD4HW83A32wy_H1tPhWphp3bfpw61aggcjg1lX55pK45fO-u5SbHiLMU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایمان دشتی، دانشجوی دانشگاه میشیگان، در گفت‌وگو با ویل کین از فاکس‌نیوز گفت از عبدالسعید (نامزد دموکرات انتخابات فرمانداری میشیگان) پرسیده آیا بدون هیچ ابهامی با سپاه پاسداران مخالف است، اما به گفته او عبدالسعید از پاسخ مستقیم خودداری کرد. دشتی گفت فقط کافی بود او صریحاً بگوید با «بزرگ‌ترین حامی تروریسم در جهان» مخالف است و مدعی شد شاید عبدالسعید به دلیل حمایت بخشی از هوادارانش از حکومت ایران و سپاه، نمی‌خواهد آنها را از خود دور کند.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/24083" target="_blank">📅 01:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24082">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">خبرگزاری NBC به نقل از مسعود پزشکیان: می‌‌خوایم قبل از شروع انتخابات میان‌دوره‌ای آمریکا توافق کنیم!
اصلا نمی‌خوایم کار به انتخابات میان‌دوره‌ای بکشه و آرزو می‌کنم آمریکایی‌ها قبل از اون به تفاهم‌نامه‌ی آتش‌بس برگردن
ایران برای بازرسی از تأسیسات هسته‌ای خودش اعلام آمادگی کرده
ما به هیچ‌وجه دنبال ترور ترامپ و یا اعضای خانواده‌اش نیستیم
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24082" target="_blank">📅 01:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24081">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/400ab8f284.mp4?token=rBVeqrtz9M1dHsA2hQhFHLT3UXz6mwpxY0HB3Z1n7mxRXDQRnyXA7dxdXKlEu0SzF0s2fIbVOg4NSe1PJWEj-wOQXFM1f-H73rc9VTc8qiK0vzJc-C7HCKo3d0JONVqaUXpZz9M8MR6fL_GqSTvyHcXGl8NQ4CwAgJjHM433MkQMowGcOr9Te8DIXBf3PMbzmxn4qVJbVww-6GCQyk6nuTDSN1rZcogjicvRJ7aNwPwntsT9FFp7BEF-dkEl7FE8b0GvoHnapoyM4rowSIT6nEzFhNkI2AauWVnD8JRAc09p4JtsEzwo3CpFlFGEVhdjdTRP6Gad6RE9hTFVNCv1cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/400ab8f284.mp4?token=rBVeqrtz9M1dHsA2hQhFHLT3UXz6mwpxY0HB3Z1n7mxRXDQRnyXA7dxdXKlEu0SzF0s2fIbVOg4NSe1PJWEj-wOQXFM1f-H73rc9VTc8qiK0vzJc-C7HCKo3d0JONVqaUXpZz9M8MR6fL_GqSTvyHcXGl8NQ4CwAgJjHM433MkQMowGcOr9Te8DIXBf3PMbzmxn4qVJbVww-6GCQyk6nuTDSN1rZcogjicvRJ7aNwPwntsT9FFp7BEF-dkEl7FE8b0GvoHnapoyM4rowSIT6nEzFhNkI2AauWVnD8JRAc09p4JtsEzwo3CpFlFGEVhdjdTRP6Gad6RE9hTFVNCv1cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده اسرائیل یه استارلینک میبره برای نمایندهی ایران در صحن سازمان ملل و می‌گه اینو بگیر به کارت میاد. و می‌گه ما عاشق مردم ایران هستیم و برای تغییر رژیم دعا می‌کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24081" target="_blank">📅 01:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24080">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca7adc972c.mp4?token=eh2XJ8AihzSDPdhXimClWmW-lMrADrHcMW1Dw-0G8iC6PCGJD24bvmUoAaWlZJTsxpbdb1fwEc81WzLCQcc-VEEwponcbjqMGVCFkoqV7VL_iytaQD2I2j62mR9k2M5Y7s4VSjuCIQsU4zjm9EDNTwlNHx9GXJJ_yV2-yDezmQzy9yvYQ8T4vH0alVcB8WdcxBYiAjdW6mq1OhWXwjTRrFPmzGkFOsNt3bL4ezZ0TRfhywJkoAaRgM5Mat2L8ksdTZnerVlnXS6geQYXpBvAQzGwDRodXmD_lFp1WIoVLd2_Y2DzdtlrrsBOMiyQZByzn6lxab0qUQGQ5UdZb30JUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca7adc972c.mp4?token=eh2XJ8AihzSDPdhXimClWmW-lMrADrHcMW1Dw-0G8iC6PCGJD24bvmUoAaWlZJTsxpbdb1fwEc81WzLCQcc-VEEwponcbjqMGVCFkoqV7VL_iytaQD2I2j62mR9k2M5Y7s4VSjuCIQsU4zjm9EDNTwlNHx9GXJJ_yV2-yDezmQzy9yvYQ8T4vH0alVcB8WdcxBYiAjdW6mq1OhWXwjTRrFPmzGkFOsNt3bL4ezZ0TRfhywJkoAaRgM5Mat2L8ksdTZnerVlnXS6geQYXpBvAQzGwDRodXmD_lFp1WIoVLd2_Y2DzdtlrrsBOMiyQZByzn6lxab0qUQGQ5UdZb30JUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان به فاکس‌نیوز می‌گوید مجتبی خامنه‌ای بسیار سالم است؛ «بعلهههه بسیار زیاد. کاملاً.»
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24080" target="_blank">📅 00:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24079">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مدیریت فرودگاه بین‌المللی نجف:
بر اساس دستور رسمی مراجع ذی‌صلاح، تمام پروازهای ورودی و خروجی از مبدأ یا به مقصد ایران از ساعت
۲:۰۰ بامداد جمعه ۳ مهر ۱۴۰۵
(۲۵ سپتامبر ۲۰۲۶) تا اطلاع ثانوی متوقف می‌شود. از شرکت‌های هواپیمایی و بخش‌های عملیاتی خواسته شده تا زمان اعلام رسمی، هیچ اقدام عملیاتی برای این پروازها انجام ندهند.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24079" target="_blank">📅 00:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24078">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">پرتاب دو موشک از نوع ابومهدی المندس ، از سیریک به سمت تنگه هرمز
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24078" target="_blank">📅 00:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24077">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">نیویورک‌پست:
سنای آمریکا بار دیگر طرحی برای محدود کردن اختیارات جنگی ترامپ در جنگ ایران را رد کرد؛ این رأی به معنای حفظ اختیارات فعلی رئیس‌جمهور آمریکا برای ادامه عملیات نظامی است.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24077" target="_blank">📅 23:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24076">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">گزارش‌های تأییدنشده از شلیک دو موشک/پهپاد از ارومیه، به سمت اربیل عراق   @WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24076" target="_blank">📅 23:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24075">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نیویورک‌پست :
ارتش آمریکا در حال استفاده از
سامانه‌های لیزری
برای مقابله با برخی پهپادها و موشک‌های کروز و همچنین اهداف زیرساختی ایران در منطقه هرمز است. طبق گزارش این رسانه، هزینه شلیک لیزر به‌مراتب کمتر از استفاده از موشک‌های رهگیر عنوان شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24075" target="_blank">📅 23:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24074">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سازمان هواپیمایی کشوری امارات اعلام کرده پروازهای شرکت‌های هواپیمایی ایرانی
از امروز ۲۴ سپتامبر تا اطلاع ثانوی
به مقصد و از مبدأ امارات تعلیق شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24074" target="_blank">📅 23:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24073">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">رویترز ـ مذاکرات آمریکا و ایران وارد مرحله جدید شده:
منابع نزدیک به مذاکرات می‌گویند تهران و واشنگتن در نیویورک درباره یک
توافق مرحله‌ای
برای پایان جنگ مذاکره کرده‌اند؛ طرح مورد بحث شامل بازگشایی تدریجی تنگه هرمز در برابر کاهش یا پایان محاصره اقتصادی آمریکا و احتمال آزادسازی بخشی از دارایی‌های ایران است.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24073" target="_blank">📅 23:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24071">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مسئولان جمهوری اسلامی بعد از ترک سالون، عکس قاسم کتلت را روی میزشان قرار دادند. @WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24071" target="_blank">📅 22:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24070">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjcFRfXp_t8pZEesMh6bRZAUXe4iXOYQ1K6sY7XRtHsdEXy8ZVlUN99M4MtyfZ4wjTGXizU-NIh8eq1qbkkn1AKhKeYXxoZH_gY9EyAqCU8coS1Lit_40pm26ERNHH1B0kJ_D0Fd4mQ77EusWlanX1kSzhzKlp1ylynob4oiuFe_bl51WkPBkmwGdJQjTdAxe1_QH36sS7C5XZLmWk8k1lVIsYfxNuqaEoXcXJqFvPg1tMHS5_onlS2b1mQcxzTRyO0bqJGtb7SUIavWN1lC-88dfgpZjzIxXYegG2VySi1gJj0y-n54EwXJhy4tBLTv37_tmLbU7ymUysWIO3zcyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسئولان جمهوری اسلامی بعد از ترک سالون، عکس قاسم کتلت را روی میزشان قرار دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24070" target="_blank">📅 22:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24069">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24069" target="_blank">📅 22:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24068">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24068" target="_blank">📅 22:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24067">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24067" target="_blank">📅 22:22 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24066">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24066" target="_blank">📅 22:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24065">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">نتانیاهو:
در طول قرن‌ها، حکومت‌های مستبدی که تلاش کردند ما را نابود کنند، بارها و بارها شکست خورده‌اند و به خواست خدا، همچنان شکست خواهند خورد. اگر شجاعت خود را جمع کنیم و عزم خود را جزم کنیم، به پیروزی ادامه خواهیم داد.
همان‌طور که در کتاب مقدس آمده است: «נצח ישראל לא ישקר»؛ یعنی «جاودانگی اسرائیل هرگز لغزش نخواهد کرد.» و دلیلش ساده است:
ما انتخاب دیگری نداریم.
از همه شما متشکرم.
חג שמח לעם ישראל
؛ عید بر مردم اسرائیل مبارک. متشکرم.خداحافظ
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24065" target="_blank">📅 22:16 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24064">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e66c6dc10.mp4?token=PjiuqJ4hJuKPCDjTMVi7aTzYgLXkmdwDu3B8pz-jV2gHvAfaycGsFsZJutueDAkGqEG2KGT9pK1d_xq3gRd9gv6jnwt0O3YkMOzLMAw8j-nZQcBGPp-ZmRsN65FzSeqeGiIczprYdSMVcY8X11YKs6YkEIrsp05o44oJMH4wDxuqd41BdFsLBm0l7h0kiHoIuxhr1EZJa2MuE-mcBMmzUnd4slCu4NuoqkedTw4nN84fHlLZuDHGAlb8wUPlfESRKE6fE4K2x7R6SL03kSRwgV_805iiQOgsWxwBHneAc2adeIUElFJkAQH2NwACb7A5TBrIi7WCH-H2Btj9FuxWkFoiMWMvUo66TKqG270kBi7-bJMCTPMiNtKkoYA64wZepjScgwtuUwoO1Gd6bDgtyw3jOZonKtSEEcwJcrxgN745lS9aDJcAh9u0tz8ykvCGbS7Snh2MH4JpXk8vfN1Glz5qEWHvCdYitUGNgMOC28NB6ruhCPdzZ93kEi8P7rAK1DiUZZPu6Inp7UXzG5f3PNiv6DmjLqTN-A_fV2bURjkoRgcVZAoaor7AMQeuNX3-4k5DC2dmOxAYFzs2D7apiA3zNQ7SnexymIb0oY8M4aVFDIDufBKa9xtI9yrzuyLNbAyoMEmjWSq28j3p2m762UANYuX0ehiRlKkKNu-aaJo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e66c6dc10.mp4?token=PjiuqJ4hJuKPCDjTMVi7aTzYgLXkmdwDu3B8pz-jV2gHvAfaycGsFsZJutueDAkGqEG2KGT9pK1d_xq3gRd9gv6jnwt0O3YkMOzLMAw8j-nZQcBGPp-ZmRsN65FzSeqeGiIczprYdSMVcY8X11YKs6YkEIrsp05o44oJMH4wDxuqd41BdFsLBm0l7h0kiHoIuxhr1EZJa2MuE-mcBMmzUnd4slCu4NuoqkedTw4nN84fHlLZuDHGAlb8wUPlfESRKE6fE4K2x7R6SL03kSRwgV_805iiQOgsWxwBHneAc2adeIUElFJkAQH2NwACb7A5TBrIi7WCH-H2Btj9FuxWkFoiMWMvUo66TKqG270kBi7-bJMCTPMiNtKkoYA64wZepjScgwtuUwoO1Gd6bDgtyw3jOZonKtSEEcwJcrxgN745lS9aDJcAh9u0tz8ykvCGbS7Snh2MH4JpXk8vfN1Glz5qEWHvCdYitUGNgMOC28NB6ruhCPdzZ93kEi8P7rAK1DiUZZPu6Inp7UXzG5f3PNiv6DmjLqTN-A_fV2bURjkoRgcVZAoaor7AMQeuNX3-4k5DC2dmOxAYFzs2D7apiA3zNQ7SnexymIb0oY8M4aVFDIDufBKa9xtI9yrzuyLNbAyoMEmjWSq28j3p2m762UANYuX0ehiRlKkKNu-aaJo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: شما درباره ایران هم سکوت کردید، اما من خبر خوبی دارم؛ با وجود این سکوت و آنچه من ریاکاری می‌دانم، روزی قدرت مردم ایران بر حاکمان آن غلبه خواهد کرد. ممکن است این روز چندان دور نباشد. مردم ایران روزی آزاد خواهند شد و رژیم حاکم، که من آن را سرکوبگر و جنایتکار می‌دانم، به‌دلیل دروغ، فساد و ظلم خود سقوط خواهد کرد و همه ما آن روز را جشن خواهیم گرفت
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24064" target="_blank">📅 22:14 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24063">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">نتانیاهو: به هیئت ایرانی توصیه می‌کنم این پیام را بشنوند تا اگر روزی از کشورشان خارج شدند، بتوانند آزادانه داستان خود را در شبکه‌های اجتماعی بازگو کنند. خطاب به معترضان حقوق بشر در خارج از اینجا می‌پرسم: وقتی حکومت ایران ده‌ها هزار غیرنظامی ایرانی را شکنجه و مجروح کرد و هزاران نفر از مردم خود را کشت، کجا بودید؟ آیا تجمع گسترده، اعتصاب غذا یا اعتراضی مقابل نمایندگی ایران در سازمان ملل برگزار کردید؟ درباره مسیحیان تحت آزار در ایران و خاورمیانه چطور؟ هیچ‌کدام
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24063" target="_blank">📅 22:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24062">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">نتانیاهو قول بر اندازی رژیم و جشن همگانی را داد
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24062" target="_blank">📅 22:11 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24061">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ac08257aa.mp4?token=gwpmN3Y6c4i9WMDAo9Xg0g4rHBrMfZl12dpQGihvXRP50yUUm5FHeBl8ThBw75IraGQ9cb7MPcUvw4Y0O2WqJswvYNeNsOZwuSOCFuOTj4_6KqyoalzVcG6G36D912CV5AN8hXvuZeyLdmBT4c6KXtebWs5-LQyHtBiMFXyBn7DoVHXF3zDY9bjR_9txoq4JUhJCnleMRqKnHDxxmK4_92iz_8HUKaN0lcIfHZQ137naEj8L8fV7aSzUL0_vX9gWBmJnsw-UmDtEIXVSlGO5WWVTVQL1zNdcujJ7Q73NFk_8C8KOEqD4gFOAPsA4oTyaiCVINOWLCW2rwGqLfh77jnfYZ-Yy6I4ZOQJ__mhRoeCBNPTnQx2tDAyg5MAtj9iOcHjdKDrwr1HlSn_TiMxP_ZPd0XNHlPh3m7DcAwPDQ7f65AQ1Xc8NugtSPRgzHbWhxbc1cRekDaK_eNRhwS6zjN4KZPclrZLX53SEjvvgxo0RizOQLqSpeQSdF4IRIJJUPaQ71hZCGC5_K3BT06lUMZzDGLVzTN69DBKoDz-N6vNyaKdNDSK85w34hW5QanUTS_ukVYTPtRXEMY4pGD-NNXtPjhfB4-3WKE0Hzkzo_g6LU864QhLS1qz_D_ZDfG7gf-47IepM-X3XafAazPlZ7hr0UbPIHAyDZOiJeZXtAiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ac08257aa.mp4?token=gwpmN3Y6c4i9WMDAo9Xg0g4rHBrMfZl12dpQGihvXRP50yUUm5FHeBl8ThBw75IraGQ9cb7MPcUvw4Y0O2WqJswvYNeNsOZwuSOCFuOTj4_6KqyoalzVcG6G36D912CV5AN8hXvuZeyLdmBT4c6KXtebWs5-LQyHtBiMFXyBn7DoVHXF3zDY9bjR_9txoq4JUhJCnleMRqKnHDxxmK4_92iz_8HUKaN0lcIfHZQ137naEj8L8fV7aSzUL0_vX9gWBmJnsw-UmDtEIXVSlGO5WWVTVQL1zNdcujJ7Q73NFk_8C8KOEqD4gFOAPsA4oTyaiCVINOWLCW2rwGqLfh77jnfYZ-Yy6I4ZOQJ__mhRoeCBNPTnQx2tDAyg5MAtj9iOcHjdKDrwr1HlSn_TiMxP_ZPd0XNHlPh3m7DcAwPDQ7f65AQ1Xc8NugtSPRgzHbWhxbc1cRekDaK_eNRhwS6zjN4KZPclrZLX53SEjvvgxo0RizOQLqSpeQSdF4IRIJJUPaQ71hZCGC5_K3BT06lUMZzDGLVzTN69DBKoDz-N6vNyaKdNDSK85w34hW5QanUTS_ukVYTPtRXEMY4pGD-NNXtPjhfB4-3WKE0Hzkzo_g6LU864QhLS1qz_D_ZDfG7gf-47IepM-X3XafAazPlZ7hr0UbPIHAyDZOiJeZXtAiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو:
این یک وسیله ارتباطی است؛
استارلینک
. ابزاری که به مردم اجازه می‌دهد به حقیقت دسترسی پیدا کنند، انتخاب داشته باشند و از آزادی اندیشه و آزادی بیان برخوردار شوند. به همین دلیل است که رژیم ایران از دسترسی مردمش به چنین فناوری‌هایی می‌ترسد
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24061" target="_blank">📅 22:09 · 02 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
