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
<img src="https://cdn4.telesco.pe/file/COUeBOHS89lnRK1xf9cHnOL__ll_W_sm3n1t06vwbpUDJr3Mylx_AhC9GzRdIKHozcyjGWUOZShI_wL7wFUNr4wzB1dIjZTmuwLa1Fs1A6hah6wBTLbjkm3gB5WzbNOs52utfIyV1veXQdzvWV8DGuu9ArkPDFqNjxR4k_GOnGaNqiHfN9PA2Bd3xW7BlRhNRHGaNRPQvI0E5mT0z7zmGTOsdCh4bF_LvQ4Ui7l1689Gzyz7Wvjo_BHzG3jL8IT8Mm5tloC5Ts9Rn2Sw_4aeQfHP581eBDsatVFPLiKwR0enivG_IYzYYlz-I0VcRvD_-bqwTdrJAyh7hW0OGIpnLA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 932K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 23:41:34</div>
<hr>

<div class="tg-post" id="msg-137326">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
خبرنگار: شما می‌گویید که با ایران مذاکره می‌کنید. چه کسانی در این قضیه دخیل هستند؟ ویتکاف؟
🔴
ترامپ: تقریباً همه. جی‌دی، مارکو، خیلی از افراد مشغول گفت‌وگو هستند. این موضوع خیلی مهمی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/alonews/137326" target="_blank">📅 23:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137325">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_hDO-vWutDEOx2hCi3HqYIs3sBbBo-JHWI1R4MAqwtyKmuTArLBs3xIqefAJKmrEZ_Im6-P8XHpTkuJgQRRSWLIrIKjDpu4rdUg9HOINLvm8UkdoCw6rKXoIr3zUMIWfn18WPtIFUJlXs4nUTQ1t3CD0CDSnFvjh1g4IhjUhd_zDHbTEVlf27qn9p-7gml6RgWXMxA2w4efsT4TfXu_KOegyKRv3zmmBFUUwmCTny73YbcLD3NPo7he8_4hnRodPOlRxNzIDCgUTg0iCtqNI9NduwJb5ngqepZXvMCjKRP2CJqqKNO8bDiKoORTS86r0XLvJtn1ek6etaFvUiCgIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون بندر الحدیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/alonews/137325" target="_blank">📅 23:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137324">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
ترامپ : ایران، باورنکردنیه، شروع کرد به شلیک کردن به همه‌جای خاورمیانه.
🔴
اگه سلاح هسته‌ای داشت، حتما ازش استفاده میکرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/alonews/137324" target="_blank">📅 23:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137323">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea64c7c35f.mp4?token=fu9WV0lpyqSuhX7shlmY2TPuMlyjqSJd3ORf5_xQnLhZ5FoATdMWBgv4xkgVg8reuxfqiqT7wJTNHxIaPWsOZ4hRN5ZXPA0xyMznu02vCO8bRMOAUZLJT3qTJdWnzHughN7pXQejM5XIo4PX5XF1gPzsWAZbXYT356U19rj4JOXQgU3p8tJuuPk8I36dQejxCQsGbD-efsihnbRgFVVi57BilrWnrEHHWqLIFrCoWF-HHAlvh35HhIN8oMwUHaZqqk6phY9JcLzCZzo_tI60MPpQncQKlDfmyDCb1Al2crV1XrJYfroVIGaQG0WY1wNr-XsSelr3r9bF9BQVP8XRFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea64c7c35f.mp4?token=fu9WV0lpyqSuhX7shlmY2TPuMlyjqSJd3ORf5_xQnLhZ5FoATdMWBgv4xkgVg8reuxfqiqT7wJTNHxIaPWsOZ4hRN5ZXPA0xyMznu02vCO8bRMOAUZLJT3qTJdWnzHughN7pXQejM5XIo4PX5XF1gPzsWAZbXYT356U19rj4JOXQgU3p8tJuuPk8I36dQejxCQsGbD-efsihnbRgFVVi57BilrWnrEHHWqLIFrCoWF-HHAlvh35HhIN8oMwUHaZqqk6phY9JcLzCZzo_tI60MPpQncQKlDfmyDCb1Al2crV1XrJYfroVIGaQG0WY1wNr-XsSelr3r9bF9BQVP8XRFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : باراک حسین اوباما خبرنگاران را تحت پیگرد قرار داد، اما هیچ‌کس چیزی درباره‌اش نگفت.
🔴
وقتی اوباما این کار را می‌کند، اشکالی ندارد؛ اما وقتی من این کار را می‌کنم، می‌گویند اشکال دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/137323" target="_blank">📅 23:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137322">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
گزارشگر: چه زمانی ایران تسلیم خواهد شد و واقعاً پای میز مذاکره خواهد آمد؟
🔴
ترامپ: شاید آن‌ها تسلیم شوند، یا شاید فقط به یک غار بروند و مخفی شوند.
🔴
آن‌ها غارهای بسیار عمیقی دارند که می‌توانند در آنجا پنهان شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/137322" target="_blank">📅 23:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137321">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
رویترز: چندین انفجار در مناطق الحدیده در غرب یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/137321" target="_blank">📅 23:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137320">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
فوری / حملات هوایی نیروی هوایی سلطنتی عربستان سعودی علیه بندر حدیده، در یمن که تحت کنترل جنبش انصارالله قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/137320" target="_blank">📅 23:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137319">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ترامپ : وقتی من وارد ونزوئلا شدم، همه مخالف آن بودند.
🔴
اما دو روز بعد، آن‌ها گفتند: "وای، این فوق‌العاده است.
🔴
بسیاری از افراد همین حرف را درباره ایران هم می‌زنند. بازسازی ایران ۲۵ سال طول خواهد کشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/alonews/137319" target="_blank">📅 23:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137318">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQPTuQ98b3WpOJMUkFqQVywYtduy8xCFKStgKTKM1LfV4U6v0FlQF337HCbG0VCvyYKtaOCdniR8i9pQeqhv3l3t5kPPVjc0Iwexwr8PPp3FPJhTCBL3AjklFA_YqG-B20arrH3OKR_rD5uJRoutcWIDa76yOWlf8s7Pg85RRI_xtvITmixyFCVE3lhkLXinCrygCc67xTwDs77Qr8vBbfIPPpXMHO2S9E1XyLhHjxLNhBvyt7dNuSpxB57SIgvv9yTJNSc_fu3fLCFhFjjiL7N81UOsTZf_uLiJLXTxxVamIxVVGFYtfHloKlKuR1jObOoggz25QgmB-myRL4-_0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون کاهش قیمت تتر
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/alonews/137318" target="_blank">📅 23:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137317">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ترامپ: هنوز درباره اجرای حملات بزرگ آمریکا علیه ایران تصمیمی اتخاذ نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/alonews/137317" target="_blank">📅 23:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137316">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
ترامپ :  من صاحب مسابقات "دختر شایسته جهان" بودم، و همیشه نماینده ونزوئلا در این مسابقات عملکرد بسیار خوبی داشت.
🔴
بنابراین، من اطلاعاتی در مورد این کشور دارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/137316" target="_blank">📅 23:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137315">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc5decfc4f.mp4?token=hApwYK4TTdDaa5Kz2hcdXQCeCCyNldDePnAkaGmNNJkQv9iuJppzRzzVFQTaCGWfkvo5iX_Gk1JN5TPkK9zZ3-c8-WL-CM8ASw-XnJRBL61O4Cf8Z68kbLo3QTN1H9UvKZrFKWeluKR8NAzkHAkyRhNnpfHb4liTL8Enh25j4tnMFEB7nNWcQ8f8XGYYu6JeY5CvXXtooHzyRDv4KSdnBMjgfP_aFIJrOiK6S49ex_rrHJy2DoU4fy14NgWlxsGydC7RI3hWSQD5JkuqapJyw-fZFJiYtao_qqXEe5OGRuu_raoirvHWKstDlGsEL-nEMGxhStwD-Zy-7q6VfNG37w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc5decfc4f.mp4?token=hApwYK4TTdDaa5Kz2hcdXQCeCCyNldDePnAkaGmNNJkQv9iuJppzRzzVFQTaCGWfkvo5iX_Gk1JN5TPkK9zZ3-c8-WL-CM8ASw-XnJRBL61O4Cf8Z68kbLo3QTN1H9UvKZrFKWeluKR8NAzkHAkyRhNnpfHb4liTL8Enh25j4tnMFEB7nNWcQ8f8XGYYu6JeY5CvXXtooHzyRDv4KSdnBMjgfP_aFIJrOiK6S49ex_rrHJy2DoU4fy14NgWlxsGydC7RI3hWSQD5JkuqapJyw-fZFJiYtao_qqXEe5OGRuu_raoirvHWKstDlGsEL-nEMGxhStwD-Zy-7q6VfNG37w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ونزوئلا: ونزوئلا هنوز برای برگزاری انتخابات آماده نیست.
🔴
خانم دلسی کار بسیار خوبی انجام داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/alonews/137315" target="_blank">📅 23:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137314">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما در حال حاضر با آنها در گفتگو هستیم. به نظر من، با گذشت روزها، آنها جدی‌تر و جدی‌تر می‌شوند.
🔴
من معتقدم که توافق، راه هوشمندانه‌تری است، اما کاری که ما انجام می‌دهیم، راه آسان‌تری است. ما آماده ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/137314" target="_blank">📅 23:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137313">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
خبرنگار: وزیر جنگ گفت که چین و روسیه از ایران حمایت می‌کنند.
🔴
ترامپ: هم شی و هم پوتین به من گفتند که در این کار مشارکت نخواهند کرد.
🔴
ترامپ: من به آنها اعتماد دارم. فکر نمیکنم که آنها بخواهند من ناامید شوم
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/137313" target="_blank">📅 23:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137312">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
ترامپ: همین الان که داریم حرف میزنیم داریم با ایرانیا مذاکره هم میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/137312" target="_blank">📅 23:13 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137311">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
ترامپ درباره توافق هسته‌ای با عربستان سعودی: در یک مقطعی، عربستان سعودی به پیمان ابراهیم خواهد پیوست و برنامه هسته‌ای غیرنظامی خود را دنبال خواهد کرد. هیچ گونه غنی‌سازی انجام نخواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/137311" target="_blank">📅 23:13 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137310">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
فوری / ترامپ: مهمات برای یک حمله بزرگ علیه ایران آماده است. ایرانی‌ها باید این موضوع را جدی‌تر بگیرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/137310" target="_blank">📅 23:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137309">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
ترامپ درباره ایران: «آنها میخواهند توافق کنند. گاهی می‌گویند نمی‌خواهند توافق کنند
🔴
دو راه وجود دارد: یا می.توانیم به آن‌ها حمله کنیم، یا می‌توانیم با آنها مذاکره کنیم، که همین الان هم داریم انجامش می‌دهیم.
🔴
همین الان که داریم حرف می‌زنیم، داریم با آنها صحبت می‌کنیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/137309" target="_blank">📅 23:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137308">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=nvnFM8VX9y-JEvePwAWV_sV_UpcO2gi1tSQC4YOGliHCsz0WjosV3qF3ILIS4JUtGq71l-4UIxnkZeU35BGEV_O8s8rNaJPpMaJR4L-RqwQ6CXXFgHCpo-IWc82JhDHdENr0V8rRkxjL_OfkOfH56p8vyh3h7nw6q7Yu8WEyhL8Q1zN4KIrrxQu1KaO3heuIk5t0bQDEyTRM-_7eCggAPpYJqd8iBri3W5bZA22KX8oVKaqeenUXbbK_LROF6xBWCvUGaYfUQw5UafiCMeTZR6kR2fEMEx6-lsQ3tVx5GzOx2sJXE0gvuTrrfOCO0HzvczU5thYDUFmTbZ7ouRWqmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=nvnFM8VX9y-JEvePwAWV_sV_UpcO2gi1tSQC4YOGliHCsz0WjosV3qF3ILIS4JUtGq71l-4UIxnkZeU35BGEV_O8s8rNaJPpMaJR4L-RqwQ6CXXFgHCpo-IWc82JhDHdENr0V8rRkxjL_OfkOfH56p8vyh3h7nw6q7Yu8WEyhL8Q1zN4KIrrxQu1KaO3heuIk5t0bQDEyTRM-_7eCggAPpYJqd8iBri3W5bZA22KX8oVKaqeenUXbbK_LROF6xBWCvUGaYfUQw5UafiCMeTZR6kR2fEMEx6-lsQ3tVx5GzOx2sJXE0gvuTrrfOCO0HzvczU5thYDUFmTbZ7ouRWqmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: شما دارید درباره‌ی منفجر کردن نیروگاه‌های غیرنظامی و پل‌ها صحبت می‌کنید. بسیاری از جهان متمدن این را یک جنایت جنگی می‌دانند. نظر شما چیست؟
🔴
ترامپ: من به آن سؤال پاسخ نمی‌دهم. شما از کدام رسانه هستید؟
🔴
خبرنگار: نیویورک تایمز.
🔴
ترامپ: حدس زدم. همان نیویورک تایمزِ ورشکست
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/137308" target="_blank">📅 23:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137307">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهوری آمریکا جمعه دوم مرداد به چین و روسیه درباره فروش سلاح به ایران هشدار داد و گفت که او اظهارات شی جین ‌پینگ و ولادیمیر پوتین مبنی بر اینکه تاکنون چنین اقدامی انجام نداده‌اند را باور دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/137307" target="_blank">📅 23:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137306">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
ترامپ : اگه عربستان توافق هسته‌ای می‌خواد، باید به توافق ابراهیم هم بپیونده
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/137306" target="_blank">📅 23:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137305">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23ae6c6862.mp4?token=WwW70Cp4eVGB1CwKenWyrOM5d6td7ajyoIJ5wggTV_rj7ntSRn5xm_36LJ4bPaotxKhfj2vPwqkfGxlWVMS1AWNK8owPLg-spfbNoVAemeAvAM1GSZHDx2vJU7nbB-uFjIy2ymeGPluSzOSJQG8X2ITi8uwucuWwZi-xGK2JUUEQFoWNs_3r9m0pGVEEDnDlo3Y3gftCOIQ-2pSJ_ZTfhH6D9l8vyeSEKCDVmu6CEX9mHO-KQ-K4f3Kl-WhDCX5PQ231qs4khUdPRFm7gT4cjaRdTUj-oj7_I3qo3uhrOHrMb_NKnnPvp2AiXTFD5H4sqEvQELaY11S7SgRE-UMU1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23ae6c6862.mp4?token=WwW70Cp4eVGB1CwKenWyrOM5d6td7ajyoIJ5wggTV_rj7ntSRn5xm_36LJ4bPaotxKhfj2vPwqkfGxlWVMS1AWNK8owPLg-spfbNoVAemeAvAM1GSZHDx2vJU7nbB-uFjIy2ymeGPluSzOSJQG8X2ITi8uwucuWwZi-xGK2JUUEQFoWNs_3r9m0pGVEEDnDlo3Y3gftCOIQ-2pSJ_ZTfhH6D9l8vyeSEKCDVmu6CEX9mHO-KQ-K4f3Kl-WhDCX5PQ231qs4khUdPRFm7gT4cjaRdTUj-oj7_I3qo3uhrOHrMb_NKnnPvp2AiXTFD5H4sqEvQELaY11S7SgRE-UMU1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صلاح یکتا که کار آچر کشی و فیزیوتراپی در ایران و دبی انجام میداد رو گرفتن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/alonews/137305" target="_blank">📅 22:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137304">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
فارس:  آمریکا با موشک، یه تانکر حامل گاز مایع رو مورد حمله قرار داد، چون به اشتباه تصور میکرد که این تانکر حامل گاز ایرانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/137304" target="_blank">📅 22:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137303">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
روایت «المیادین» از فشار ترامپ به کردستان عراق برای جنگ علیه ایران
🔴
خبرنگار المیادین که در سلیمانیه حضور دارد،‌ خبر داد واشنگتن بر رهبران منطقه کردستان عراق فشار می‌آورد تا مستقیماً وارد جنگ علیه جمهوری اسلامی ایران شوند.
🔴
المیادین همچنین گزارش داد که دولت آمریکا به مسئولان کردستان عراق هشدار داده اگر با ایران وارد جنگ نشوند، نوع حکومت کنونی آنان (خودمختاری) را لغو کرده و تغییر خواهد داد.
🔴
ایران هم به سران کردستان درباره آغاز چنین جنگی هشدار داده و تأکید کرده اربیل باید عواقب حمایت از تجزیه‌طلبان ضد ایرانی را مد نظر قرار دهد.
🔴
خبرنگار المیادین همچنین خبر داد، ایران به سران کردستان هشدار داده هر گونه دست داشتن در جنگ، با پاسخ مستقیم ایران و حتی عملیات زمینی در این منطقه مواجه خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/alonews/137303" target="_blank">📅 22:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137302">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
بلومبرگ: ترامپ به طور فزاینده‌ای از روند جنگ ناامید شده و می‌خواهد هزینه آن را برای ایران افزایش دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/137302" target="_blank">📅 22:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137301">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
طبق گزارشات سفارت هلند هم در تهران تخلیه شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/137301" target="_blank">📅 22:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137300">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
هشدار سفارتخانه‌های آمریکا در عراق، اردن و اسرائیل به شهروندان خود: در سفر به منطقه یا عبور از آن تجدید نظر کنید
🔴
برای لغو پرواز‌ها و بسته شدن حریم هوایی آمادگی داشته باشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/alonews/137300" target="_blank">📅 22:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137299">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
عراقچی به وزیر خارجه پاکستان:
حملات آمریکا به زیرساخت‌های ایران را محکوم می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/137299" target="_blank">📅 22:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137298">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3crbVK2DXR0TXaiF9SR7LFB9ROueMVbFhcyDE2ioYoooI8EAaEvUfxopDg5a_9ChNveyjsiFuzcTuzx3MuShrizrW2njNM2QHfeNdVOq4KbYF0pJVA-pqtCq4FMJp6QQI1vyaxx5EljxG-fL186YYF4nhW8uvLUC4pbgBlQckmKlRUjp59S_c6PBlu8unngE42LZ6zXbk15ZdTA4FXuxVkJxLqcb5BB2M2PrxvzetQ6FJRNzXx76f3WMktGSJBijkNanNAA7OBnrNDYXv6wS7sNqJcuNNEUDLyuD-0VwGfdUpoP_DnTM7J4H2P1_IB0VKr_al8xRdIUXkWkim6FbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر ماهواره‌ای از نتایج اصابت موشک FP-5 به کارخانه "اویتک
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/137298" target="_blank">📅 22:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137297">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
بلومبرگ به نقل از منابع:
ترامپ به طور فزاینده‌ای از روند جنگ ناامید شده و می‌خواهد هزینه آن را برای ایران افزایش دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/137297" target="_blank">📅 22:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137296">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3dORvbZ-UPqHP_hsGc5kk4lDWVW-8vcI9dtECuebvYS3S9HkpifuD8xIPDssaSv_XAe3g7RDTQ_aWOnZOhXDap1CHeuOGrAQeCXpt63TuBH1KlhoHSSK3zAvuGCOmnL42e3gZ8quqU83t5Mfb8kDcryVPNir87TKmvI0JgS1_1zSLJuf9VVX_zPhXdujHh5ZHE73ie2X8ZPGMKz0UlsYay9z6AcvcyVrRjKRhXyceomrgSw1HSI7SS1lxKCLFz9BlirAXAPQDSyR1Pv-e3VZw3Dcxk6-X5mtRjv6o0ZndkwM2umLRLdVa6BCL1dju_6NnfSiLXsW7V8PU-ktjShpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نقشه جدید برای قتل ترامپ/ کانال ۱۴ اسرائیل فاش کرد:
🔴
بر اساس یک گزارش جدید، چند تن از مشاوران ارشد رئیس‌جمهور هشدارهای اطلاعاتی مبنی بر تلاش ایران برای هدف قرار دادن آن‌ها دریافت کرده‌اند.
🔴
در نتیجه، به برخی از آن‌ها دستور داده شده که از خدمات تاکسی‌های اینترنتی و خودروهای کرایه‌ای به دلیل نگرانی از یک حمله برنامه‌ریزی‌شده استفاده نکنند.
🔴
هم‌زمان، خود ترامپ نیز گزارش‌های اطلاعاتی از سوی اسرائیل دریافت کرده که نشان می‌دهد تهران در حال بررسی طرح جدیدی برای هدف قرار دادن اوست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/137296" target="_blank">📅 22:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137295">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ER_hzgUphm-tXubkRLOK8ZVxmRot4EayGTK0tO6Skkqz8u43fJFG6In1Yp3L8PKYz2mI8zB32pwbDjy2eWJH7PGfiwLzc0heX0AhSVP5NjTg3KvCVAi38Zgace8koC4bUPA7ccJ5ZLypOPu5ZAmKHHf4ueP2MGTM2t7h3Qw7_PwJLqimTXT4y7i8oo5UwMDZkHqglAMoW2SNovo9k190WbRVNiUHOY-7RZp-Bd7uFaeDJdlY1uLkAVsTIvIAlkGPN425IUsJBgsLREAlE4hLp2F3dCNjQ00kKDHMvv18mkkShrSiMkxeLRloszcN3cXIrRuyB3Mv8ORdfs-vo5kogQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار الجزیره در تهران: مسیر دیپلماتیک بین تهران و واشنگتن ممکن است دشوار و پیچیده باشد، اما علیرغم لفاظی‌ها در مورد تشدید درگیری نظامی، دستیابی به موفقیت در هر لحظه قابل انتظار است و بعید نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/137295" target="_blank">📅 22:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137294">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5c80ce599.mp4?token=c7F6_O8_OlMcunwJ0MmDTi_R_VUD8z8pnbLsPYFQ08Ojg5s8d0skQyP9cnUrz2mddmjBUaGqI3UC7TtDCOLl2RL6PAoL5kbsG_Jqu0PUY3vBJ8c-dC72hEFuqkNhF9EtLdbZzXotSouN-9DNOY4g_halosZhPdhsBl3BXySRvRHLQP58-4MEvlQ8JuWwndu7DhCN0cr5RxO6KjcBr77Ugd8KN7GJ0fRvtfKStpqw8DrHGN3-sa15xxf1jd0w2JwKkmBD0FsYvRt01nrpP6UnOmC9xODMsnF5mlPLI-UiKCmjlAnwFxtyBIgUsYSN9LB3xWXD_F7tiEWG6hTTD3IJqGGgpP1g57h5Cpzr7DuW2ynUfuQ1w8ZhZY5C3ud9Ynf1InbxKE0VdCAezE3Mj9FOBe0Qc7q3pvk0VQspqfabdHjVW9JJGrkmH-9eGqlG-enUP5iyoD9ecvd9K4XMcr4DDk8Xa-_SUe9a6pegyoJohurI6IaNHfBDwmQNkQUv5OyeF5MT_7SVKORFnwrQ06lf5i_3qCQm3GEMqQSY4Pzj8YEDgptD-jIIyoXdpr_iAyS8Fz8jBeANNXtT-NCT3Y9vGEzbRsGJ_tULc8Eltkwy6izwvNyi2t0MmA7ynnkRs31pwnoB21Fd8akCiF0mmdrwljse3-C9iLVKEFXR8bmHRRE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5c80ce599.mp4?token=c7F6_O8_OlMcunwJ0MmDTi_R_VUD8z8pnbLsPYFQ08Ojg5s8d0skQyP9cnUrz2mddmjBUaGqI3UC7TtDCOLl2RL6PAoL5kbsG_Jqu0PUY3vBJ8c-dC72hEFuqkNhF9EtLdbZzXotSouN-9DNOY4g_halosZhPdhsBl3BXySRvRHLQP58-4MEvlQ8JuWwndu7DhCN0cr5RxO6KjcBr77Ugd8KN7GJ0fRvtfKStpqw8DrHGN3-sa15xxf1jd0w2JwKkmBD0FsYvRt01nrpP6UnOmC9xODMsnF5mlPLI-UiKCmjlAnwFxtyBIgUsYSN9LB3xWXD_F7tiEWG6hTTD3IJqGGgpP1g57h5Cpzr7DuW2ynUfuQ1w8ZhZY5C3ud9Ynf1InbxKE0VdCAezE3Mj9FOBe0Qc7q3pvk0VQspqfabdHjVW9JJGrkmH-9eGqlG-enUP5iyoD9ecvd9K4XMcr4DDk8Xa-_SUe9a6pegyoJohurI6IaNHfBDwmQNkQUv5OyeF5MT_7SVKORFnwrQ06lf5i_3qCQm3GEMqQSY4Pzj8YEDgptD-jIIyoXdpr_iAyS8Fz8jBeANNXtT-NCT3Y9vGEzbRsGJ_tULc8Eltkwy6izwvNyi2t0MmA7ynnkRs31pwnoB21Fd8akCiF0mmdrwljse3-C9iLVKEFXR8bmHRRE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
درود بر روانشاد
#نوید_افکاری
🔴
#رشید_مظاهری
به سلامت باد
🤔
ننگ ابدی بر عليرضا دبیر و تمامی حرام زاده های طرفدار حکومت جمهوری اسلامی
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/137294" target="_blank">📅 22:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137293">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
نیویورک تایمز: نهادهای اطلاعاتی آمریکا معتقدند که رهبر جدید جمهوری اسلامی، نسبت به پدر و رهبر پیشین خود، علاقه و تمایل بسیار بیشتری به دنبال کردن برنامه دستیابی به سلاح هسته‌ای دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/137293" target="_blank">📅 22:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137292">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/217970b0cb.mp4?token=iSLhazXaXjPsXnWpEDszd2u_-Sh2_58c5gI5_b0An0oygo_5uRx5RvaApVkk477bw7OuJw7wMAUtC6xoytBAUjACwOrseYwbGieCFfsnFH8r7WWqCFCqcaMFUhx-tQWWy66a_zDIkriFvG-rO8T4X7N0T1YKoX3OiKHU5cJfG0m94qz_2Vc07DEFF5pZ0T_uCMB7VV3Qt7M2Qr9okqxOzFzRAcprzpUSeDCaF3LA9g1EEiD0IZJYihldsAF66pG9aiYZ84dsCZfJ1ha_HWjIcnN-fqRgYECKvSGW08waaC2L_duqkuIujeGJy9CIKSjpKxzeeuqP4_xsIBGZW0JEpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/217970b0cb.mp4?token=iSLhazXaXjPsXnWpEDszd2u_-Sh2_58c5gI5_b0An0oygo_5uRx5RvaApVkk477bw7OuJw7wMAUtC6xoytBAUjACwOrseYwbGieCFfsnFH8r7WWqCFCqcaMFUhx-tQWWy66a_zDIkriFvG-rO8T4X7N0T1YKoX3OiKHU5cJfG0m94qz_2Vc07DEFF5pZ0T_uCMB7VV3Qt7M2Qr9okqxOzFzRAcprzpUSeDCaF3LA9g1EEiD0IZJYihldsAF66pG9aiYZ84dsCZfJ1ha_HWjIcnN-fqRgYECKvSGW08waaC2L_duqkuIujeGJy9CIKSjpKxzeeuqP4_xsIBGZW0JEpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک زن عصرحجری معترض به توافقنانه: مردم اگه گرسنه هستن یونجه بخورن، ما انتقام میخوایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/137292" target="_blank">📅 22:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137291">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
المیادین: واشنگتن از رهبران کردستان عراق خواسته در جنگ علیه ایران وارد شوند و ایران هم به اربیل درباره پیامدهای هرگونه همراهی با این جنگ هشدار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/137291" target="_blank">📅 22:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137290">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
پدافند کویت مجدد فعال شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/137290" target="_blank">📅 22:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137289">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ایرنا : آمریکا امروز بعدازظهر دو موشک به سمت یه نفتکش گاز مایع که از خلیج عمان نزدیک منطقه می‌شد، شلیک کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/137289" target="_blank">📅 22:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137288">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409d06d604.mp4?token=Hy88GxpUcAZpVUvL63Cc9c0ohJji2H48vrmvg4frtrgSi5KylCuWfJnUwO968ujavJV-LK_07QIV5QSqzxZvEIW7FEXyDmcD2Cb2kmoQaN8XE9fa_1hX4Iu4OaZLKNWNVXu4GqPRhKP41Cjdm7JQ5XYinsEQsOrE-thy5FkUcMUwuh_ADvt-xR_o4MI0QrMoiNOGTEA8LxNfKEx4VCp6oZ3rn2CFcv5BsElrXe0Fr43g5q1Q606N7F2kGS2zpVJO-KZBwqQCkLGY_qcNVDJGolkv2FfJKOdHACK9oQtSI-5u1ylqDQBPn6MsVmBOuT8lX0AEFyQyM8u64x4xCGcy4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409d06d604.mp4?token=Hy88GxpUcAZpVUvL63Cc9c0ohJji2H48vrmvg4frtrgSi5KylCuWfJnUwO968ujavJV-LK_07QIV5QSqzxZvEIW7FEXyDmcD2Cb2kmoQaN8XE9fa_1hX4Iu4OaZLKNWNVXu4GqPRhKP41Cjdm7JQ5XYinsEQsOrE-thy5FkUcMUwuh_ADvt-xR_o4MI0QrMoiNOGTEA8LxNfKEx4VCp6oZ3rn2CFcv5BsElrXe0Fr43g5q1Q606N7F2kGS2zpVJO-KZBwqQCkLGY_qcNVDJGolkv2FfJKOdHACK9oQtSI-5u1ylqDQBPn6MsVmBOuT8lX0AEFyQyM8u64x4xCGcy4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راز شلوغی کافه‌های شمال تهران
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/137288" target="_blank">📅 22:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137287">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
چندین انفجار شمال کویت را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/137287" target="_blank">📅 22:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137286">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
قوه قضاییه: شعبات ساعدی‌نیا همچنان پلمب هستند
🔴
ساعدی‌نیا هیچ امکانی برای فعالیت ندارد
🔴
موضوع مصادره اموال در حال رسیدگی قضایی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/137286" target="_blank">📅 22:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137285">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdN-xr1YiKohgGensCHCDbCON_ZGe6BhF94HzGmTrILaDDgKVNVdlP8STH3FMlMYdTp8gqxgYY8IpNI1UVndxM6yXNz4CRamj8f8kxgXj-9H_sv6SrqXDlUFIOjdX75Ghux9ZT9344JGcfOJjmA_cnrbXcbSGej_OPggVgsAAVhD1L7n6X-rUorGwNXzAB6MuI2oJfDNQqfOdB7J-Ko2xhX3CD_LZC4vNSBKyN7fkQ8qLTrSigqgZDsibsu3uUStmoW860KWik6_1NCRRKJsGKiks0ZMcL3N9Q5CNO93a6GsEi1_80P2peM3nl01fgOiqPP3A6iSzzEfqvUVQeyjQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
با سرویس های نامحدود ⅓ بهای مخصوص نت ملی هایپرلینک از شر اختلال ها و قطعی های اینترنت خلاص شو
🌟
با ۱۴۷ هزار تومن سرویس های نامحدود و ایپی ثابت هایپرلینک همیشه انلاین باش
✔️
همین الان تست بگیر
کد تخفیف ۳۳ درصدی فقط به مدت ۲۴ ساعت:
Code
:
w
ar33
⭐️
🤖
@hlink_robot
📢
@hyperlink_ch
💬
@HyperLinkSupport</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/137285" target="_blank">📅 21:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137284">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
نیویورک تایمز: ترامپ روز جمعه با مشاوران ارشد خود درباره تشدید حملات علیه ایران دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/137284" target="_blank">📅 21:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137283">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
مقام آمریکایی : ما یه سایت امنیتی ایران رو تو نزدیکی یک گذرگاه مرزی بمبارون کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/137283" target="_blank">📅 21:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137282">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_lc1V2eOSgE3rzUgAp4wJzBxYBeVZByvZQ0y_gqi-QzFbc2deNOBjF6oWKo7dpbGzmTQ2SqdbKiQ68kd1CDteZGfUET_-ih5oE3QJsi5cYFC6LFRs-cXYkpB1h97O67y7Gv9ECZ4X7tH_97Bqxxt2anB3MT0_y0vybeRkOnWXy2oKAp5TkHrfTI49LbgYn6YjLjBVHcBXwhUKxIXz8E1Pr8pwsclY0BS9V-xEwr6gJcLsiWMkSQA3bXkf6DwRH5fwg6sFBhCqCfQyPPN8Do2yJWfcIzoJAp5SDnTK445aHm3EPNSmRXFomrGG4TlpxJ8SRWhhhqs9n1G_x7M9x4vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین پست اکبر عبدی در کنار علی دایی، نوشته بود: حالم خوبه نگران نباشین
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/137282" target="_blank">📅 21:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137281">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
فرماندار جاسک: ۱۰۰ شناور در حملات اخیر آمریکا آسیب دید
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/137281" target="_blank">📅 21:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137280">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
ترامپ: انتظار داریم به‌زودی تعرفه‌های گمرکی سنگینی علیه اتحادیه اروپا اعمال کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/137280" target="_blank">📅 21:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137279">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
العربیه: اسلام‌آباد از تهران خواست تا بر حوثی‌ها فشار وارد کند تا از حملات خود در دریای سرخ دست بردارند.
🔴
پاکستان به ایران هشدار داده است که بستن تنگه "باب المندب" وضعیت را پیچیده‌تر خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/137279" target="_blank">📅 21:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137278">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYqNJJK-yLmJLtwnOCT-a5r62ec65R9FWOi7hvVKW8Ry_l_7fJyf06ZIT_FAog32XzWX8eYp3RSO9djoEshjSu196yzOfH9Vd8d-UV5DrRZNyes323ge5FOEEJWIFJp-6YGQIgrTKg5nD2tgkfNNod3DdS4yaRFd-bamfa010kpn3yBpUdkHBPnckNJA9ZGGhjRNrkq0sYajkz4vKNQYhAgxlV1Suuf4Oa3rtwfitr37o1lcE-btP-oEcxw6O7z4ikjQVSXRF5lWxKJbm4grri7IKTcuZ3uw5H1m2OG7e4UD8Sk4rKE1_l-7ikQrD7nXqmZFBsh0FyfKa6Fsa254Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ، از طریق شبکه Truth Social:
از تمام سناتورهایی که با تلاش مجدد دموکرات‌ها برای تضعیف امنیت ملی ما مخالفت کردند، سپاسگزارم. تبریک می‌گویم به آقای مایک جانسون، رئیس مجلس نمایندگان، و نمایندگان جمهوری‌خواه به خاطر موفقیت بزرگشان در برداشتن اولین قدم به سمت تصویب طرح بودجه.
🔴
از آقای جودی آرتینگتون، رئیس کمیته، چِپ روی، میشل فیشباخ، ویرجینیا فاکس، جیسون اسمیت، مایک راجرز، جی‌تی تامپسون، برایان استیل، و همچنین از آقای تام امر، رئیس گروه اکثریت، استیو اسکالیزه، و همه کسانی که برای برداشتن این گام مهم همکاری کردند، سپاسگزارم.
🔴
این طرح، یکی از مهم‌ترین طرح‌های قانونی در تاریخ آمریکا خواهد بود. این طرح، به تقویت ارتش قدرتمند ما، ارائه کمک به کشاورزان و، مهم‌تر از همه، اجرای بخش‌های قابل توجهی از طرح "نجات آمریکا" کمک خواهد کرد.
🔴
مردم ما بسیار خوشحال و حتی تحت تاثیر قرار خواهند گرفت! از سنا می‌خواهم که قبل از شروع تعطیلات تابستانی، یک مصوبه بودجه را تصویب کند، که می‌توان آن را با اکثریت ساده به تصویب رساند. ما آماده‌ایم که در کنار سنا برای انجام این کار به نفع مردم آمریکا همکاری کنیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/137278" target="_blank">📅 21:13 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137277">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7XtOx5nIsqfax0ICETaFzU3vci2qxj4Fp_ZRL8qIWUAorCrgdb7pdzb8P_ZJeTZQlVd9gen6T26gbrR-dT7mBSu_NJx4psAgdWcBlAzWnxVVz_uRIKBA5Ghachlh-Nda90Miv36_fcYRBoNvJ-0xOg2tT-YTWdz99YO3wgQZKzJixekCB6bluhJCCIulEQpr0-40BgZcsi5JbQS3EpRMLd8tuFtynPUIcs-6SRCAhJoOcRpijY_xRy0roPfdEAs7h2EMEF4ORKYu-4NfUzbGE_LXbmORJ4SwWieceVWC-X4EIh2-uzOMbuYXof8hXIetxYe1Nw41NXasxIPR0Kbrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکبر عبدی، بازیگر سینما و تلویزیون در سن ۶۶ سالگی درگذشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/alonews/137277" target="_blank">📅 21:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137276">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJwjNJeJk5GHe9EAzCw7ZME_L4NJmOHga93HbDWjfsL7GlJ1Mm95Lz9AJYrMwrgeuixkixZmGj7NffX5Pb3I75iDgTMnhZ37aZn_1K-ogCR9IPTxxOEZyP65Vb7rwcGSXAHTPRGVCcNYfVcHzTTFQp1GW9DC8eKXi31jQJTOXM-TgtKSX2QXOYHcaa14HRLmCuUs6voNbKssGOvxF0i3PxrAyMb6MkxcPs6O7HuHEWSFC_j7J5LU5PWFBWz-ubwHGe04JmTI1LZVTcGRj-yfQrBnBvcoo5zDxUFK4awlVZqzIGGTGxTh6tnmkJQR8rvlpA5PptqxyMW9A56a1Tsxhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: تشکر از نخست‌وزیر بلغارستان برای در اختیار گذاشتن پایگاه هوایی این کشور با وجود تهدیدات ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/137276" target="_blank">📅 20:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137275">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hp3MvUbfv3Fik1wU21LW1PjeshpaQdfj46-Hx70Keypcs4Zwtrx0lLFYB3e4mj-Dsn-t0CaeIZ9hxqB-ho52xnpAOuap5ppMSvARAF8uNZzDjfitXiqvY6BUjmjoQ-z4eTxZqZiyeojt7cCSTMaiYasAt_Gd9rWCHfW6-CZ2O6BFhE-Vp0K72ZWUMXgeA3QXsAiGlmN8eS_To_W71YNvGFBt6TRDxZkQMD5rv2C69a_awk_Q7e1xt2vtTi5lf0lHcL0YH3QLQnSjy1mvQwx35RHclbeKgnm-Fwc3ButWrrYDwa4gTahNy6mQ0NBTTquEqyioWRVei0-JebnougLWjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همراه اول قیمت بسته های شبانه خودشو یهویی ۳ برابر کرد و اعلام کرد با مجوز گرون کردیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/137275" target="_blank">📅 20:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137274">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afacd735eb.mp4?token=YTuUdk3efqx1sr9gTdgmW4OnBb9ze5usmpqHOArVb5ZtSME98otv_0GVcB8Y5viKpc95udjcc7f30BWrX3S25d7kg4oaTJxSxj7C0uDGjwWEo8jp1m1qU_rHRATzU9-DGqh714z-FE7tlPKymR1A9lf9iLeCheT8uup9PwVOSLn7DzaXpI3WNsXC55DuTSKEIDXINiUnLUM6fhKVNAUcURMIjx1IWDwlBsK5kFHvpGaUBvuXdXG1YJh9nLXSCRdavZcVGuaHFT9-1kjZOiURcQZORVXc5giOaD7Sn2EFwZw-a7DnVOiW7nlfIyTnwyfUySlUs2nCnDkOz3q812KQ5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afacd735eb.mp4?token=YTuUdk3efqx1sr9gTdgmW4OnBb9ze5usmpqHOArVb5ZtSME98otv_0GVcB8Y5viKpc95udjcc7f30BWrX3S25d7kg4oaTJxSxj7C0uDGjwWEo8jp1m1qU_rHRATzU9-DGqh714z-FE7tlPKymR1A9lf9iLeCheT8uup9PwVOSLn7DzaXpI3WNsXC55DuTSKEIDXINiUnLUM6fhKVNAUcURMIjx1IWDwlBsK5kFHvpGaUBvuXdXG1YJh9nLXSCRdavZcVGuaHFT9-1kjZOiURcQZORVXc5giOaD7Sn2EFwZw-a7DnVOiW7nlfIyTnwyfUySlUs2nCnDkOz3q812KQ5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای از انهدام سیستم دفاع هوایی پاتریوت در اربیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/137274" target="_blank">📅 20:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137273">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
وال‌استریت‌ژورنال: بحرین و کویت در حمله به ایران مشارکت مستقیم داشته‌اند
🔴
وال‌استریت‌ژورنال به‌نقل از منابع آگاه نوشت: کشورهای بحرین و کویت در اقدامی مخفیانه، جنگنده‌های خود را برای حمله به اهدافی در داخل خاک ایران اعزام کرده‌اند.
🔴
امارات نیز با ارائه اطلاعاتی از اهداف و تأمین پوشش هوایی، در این عملیات مشارکت داشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/137273" target="_blank">📅 20:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137272">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpVmnPuGrFPV0WokRDr9FCzrrDXOusGbeSa1XeGPFjJNa88MyP4Pffpj8tKYvGwVPWkCL5fB81pCALYJ3qcpHynhwtH0R_IVWBFvHV_AuUtD3RLSDer3GdcFkZDTWmvkq7y3L6CH32fOU3do1YMhFjlkskJ5AsOKRru3x8qeTwtlnlEtRfz4u2sT82ikzq1IwXQvVo-UBvhD4ubq8W9UgVsRPTutZd6JKnWMFhTfXGh0duJWKrh3Fz6wYFsUqPcS6JvGcrLP8DsCpyP0vhL7ypR96f1V3w9zl_ayjVyjbyyAuUdWH3SSCrenr_BTrq2X3JbwhbM6oD469WpJOHXVJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برخورد پهپادهای انتحاری سپاه به مواضع گروهک های کرد  در شمال عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/137272" target="_blank">📅 20:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137271">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDtztLxgB1cMWWb2NRT0bWsGQoYt1FM7AUYmYsl8Jxh_khmSk5OEYbNTOG-IW84p9hn48rQ8MWwS83BycwCddNNZpzzM3v5tDmFXtj_NiH3X5exgH9pOBszSWqAG00iUxkYXK8yeyBiq8dRl1IWD6EEItoESGuDUcMYyZtLVBvigBHZseOZTBymVJ1Q_vcn-FTaJLzWGnYl3WGgs4dhBf35pycD0LZ1zcJPNdAb4PltSkBhVJZhvj_bEj2LZbMnnj6xDZr3Y6LZYASedwyscE-9ZupXhfe9uIDzMp10__bBrvipOW452DYyyDB7g-nG-OVQdob_WAqQZ98qO6YIoGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برخورد دیشب پهپاد سپاه به پنت هوس یک برج معروف در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/137271" target="_blank">📅 20:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137270">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWuTf1S3YFZKViPjfCsZQ1ELluPb3s84o4H9zuTqGVXp8DLfI2ZStvVYlS-y-Kcd2k1J7DLW5Q0o1vbDu6XMbefnTQzbqSl6ppuFkwX5j0-6dTXN7GctptqF3yyb3DYcsbAHDNQbSqEbT2t3mClTZXn2s62pdjcGJnU4x-K8NpoEpnOakHWX-ufmuObpghsCCmnAYyFlZ3rbMRSqZ96x7k3fVA-RHq5T7xsyi9MwCqdhLP_9-pAhecRUSskvm5iacGBolLQFCDaPxbssQ5NiKnOIcgmdsLrUgbWHlPtvH2eCVC69_qFVFR4AzpOPWw3Su3aJrhk6jJjAtjPB34VLLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق شبکه اجتماعی Truth Social: کانادا دعوت آمریکا را برای افتتاح پل گوردِی هاو لغو کرد، که البته جای تعجب ندارد، با توجه به اینکه آنها مبالغ قابل توجهی به عنوان تعرفه به ایالات متحده پرداخت می‌کنند.
🔴
توافق اولیه، که توسط دولت قبلی به طرز فجیعی مذاکره شده بود، دیگر اعتبار ندارد.
🔴
ما شرایط را تغییر دادیم، به طوری که اکنون ایالات متحده 50 درصد از سود را دریافت می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/137270" target="_blank">📅 20:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137269">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
حمله پهپاد های شاهد به اربیل، هم اکنون
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/137269" target="_blank">📅 20:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137268">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
منابع عربی: صدای چند انفجار شدید در کویت شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/137268" target="_blank">📅 20:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137267">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
گفتگوی تلفنی وزرای خارجه ایران و عمان
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/137267" target="_blank">📅 20:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137266">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
آکسیوس: ایالات متحده و بریتانیا در حال برنامه‌ریزی برای برگزاری یک کنفرانس بین‌المللی درباره تنگه هرمز هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/137266" target="_blank">📅 19:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137265">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
فرمانده مقر خاتم الانبیاء مرکزی: به ازای هر شهروند ایرانی که شهید شود، یک سرباز آمریکایی کشته خواهد شد. ما بلیط‌های رفت و برگشت مستقیم به جهنم را برای شما آماده کرده‌ایم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/137265" target="_blank">📅 19:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137264">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
منابع عربی: صدای چند انفجار شدید در کویت شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/137264" target="_blank">📅 19:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137263">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFAV3LiUUO6zp-SYADyjjLUZZogUHKcRTy-2dhvjQuV-5FpMq6c4AW6r_simyuwwoieXC8FO9oGeLGtZrItmpgKHuL2991o3TDT2w7njVDWFICnQVfjrohYQw05GCGPZOFbqzBuKACQu3egubbLPZGN8MmPE2zfQS1kjt6nNkEAa73pxgnYxhJnRTDjKwsszwwQio8k1AXeHmwJ1m4wKOUlue2oPbg2yvSKWK7wVYnxDwwViFJu_wcDBMjSzKop37Cwdy5rOI-Kh-umHaLB2_RMa-xYIlQw6X-UikaujY4up8V_3drxNDu0Ps7lcYumXRLFjVycNbbBkr5jQvmUE7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاهش قیمت نفت همزمان با انتشار اخبار مذاکرات
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/137263" target="_blank">📅 19:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137262">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oD6TbQ3fnqM9l5JuAXXP6-ZUSs_jNGrFNeuMuriA1IzzZzKVWlUPl0JuSRavxdk6aiw4CCr6uCUckPx60dp-60xL_P6T-cUQn4kuv1bM91XtiLKP4I2sq7DgYH6Gzm_IlkSDk9oEonkMBQS1eedCOzcMmLZAB3nt42Yno3-uQPNzWWSBzxBokuCfP3VU6Uc1iPPsS6TKVQfhDNw5JR4-5SdWkFNNXVclDOP2O4peGBQ_E8GAVsTsMdMkp5oE3ehDBRf-4mn4yXdxcpPrQ-fe73L90CaBvrgmZ9o0aAn3vOd66QSIhNJEpt4KYmn86I4zA0ohAxk1PV51H2aPEicTRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش رویترز، قرار است رئیس‌جمهور ترامپ و رئیس‌جمهور زلنسکی روز سه‌شنبه در واشنگتن دیدار کنند.
🔴
مقامات اوکراینی و آمریکایی در حال بحث درباره پیشنهادی برای آتش‌بس هوایی هستند تا آن را به مقامات روسی ارائه دهند؛ این اقدام بخشی از دور جدید تلاش‌های صلح‌آمیز برای پایان دادن به جنگ است.
🔴
برخی مقامات اکنون معتقدند حملات مداوم پهپادها و موشک‌های اوکراین به روسیه فشار اقتصادی را افزایش داده و ممکن است مسکو را برای مذاکرات مجدد پذیراتر کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/137262" target="_blank">📅 19:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137261">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
رویترز: مومنی وزیرکشور تاکنون ۲ بار در  ۱۰ روز اخیر، به پاکستان سفر کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/137261" target="_blank">📅 19:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137260">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
سفارت آمریکا در اسراییل: آمریکایی‌ها باید به دلیل تنش‌ها در خاورمیانه، آمادگی لغو پروازهای خود را داشته باشند
🔴
آمریکایی‌های خارج از خاورمیانه باید در مورد سفر به این منطقه یا عبور از آن بازنگری کنند.
🔴
سفارت آمریکا در اردن هم اعلام کرد: شهروندان ما باید اطلاعات دولت اردن را در مورد تهدیدها دنبال کرده و از دستورالعمل‌ها پیروی کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/137260" target="_blank">📅 19:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137259">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
فوری/چین وارد شد
🔴
رویترز: چین در کنار پاکستان در تلاش است  توافق ایران و آمریکا را احیا کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/137259" target="_blank">📅 19:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137258">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
برخی منابع:ترامپ به میانجی‌ها اطلاع داده است ایالات متحده حمله محدود به تاسیسات کوه کلنگ را خاتمه جنگ با ایران اعلام کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/137258" target="_blank">📅 19:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137256">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Opm61FuF__JkT-tBup_JW5p9HL7q6mf8z7vaqXUKEIH-zsPN2FhQJD3sMVfER9QPC1oIOyFTwATIC4OGN1AeizGpp0SmwvBV4Frd--7fuG7XowPnjqpqtsyeGyteMlAZPfrPFZZWjTemYRbvAtkFFXO7nQtJE2bznBAoJjhvp0pdbztilntUWVNgc8PL9dLebOd9sZuW6xevU9umNmlitLhjcPuo6CPCZOnQ9wpfW3u931NvNwAXneoOc9MPHfhaANSkrhx6XJMFbauESXBPc3wut2FCxq5DpqEmov1poGPOR_v1rKg3MW8j1E-n_lDNPrmf0hKIx2s2Ynu0VBi9RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی به سیم آخر زد
‼️
🔴
عباس: اونایی که تو کف خیابون و یا هرجایی مردم رو به توافق ناامید میکنن و باهاش مخالف هستن از اسرائیل خط میگیرن
#حق
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/137256" target="_blank">📅 19:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137255">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ay3FRzQ5zvor7PqIf3a0LA429dFaWAtb_QZR5rLBT6rHlxcbRR5se936ny1pWvRG4-JKXvAeumHDC_nAcTt4u2rWUZh6-o0qHkDdFBJbFqlgod35zpze_aEtxA6hHHFpQz8taCrdSkvMQJArEPuCc5hub_fGDKa2jtqf7lLzJUGljcgaR42p8alZ-1X3fQF2djSb2q2JAWF3JmJKcACnG54ScpBX4pqbduDLluf__TSOUovXqdJ8rbk2mcSLJ85SCQtLxjyX06oprtzCU4kooLHHM389infmw1_49Tl4elydto1fRYoPmoCA0txRDsVdYEqm2wzreJDLgNLHX-lD7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال: رئیس‌جمهور شی، در دیدار اخیر ما در پکن، چین، به من گفت که تحت هیچ شرایطی سلاح به جمهوری اسلامی ایران نخواهد داد یا فروخت — و این بیانیه شامل شرکت‌های چینی نیز می‌شود. با توجه به رابطه ما، من به حرف او اعتماد می‌کنم و علاوه بر این، من نیز به او امتیازات بسیار بزرگی می‌دهم.
🔴
همچنین، رئیس‌جمهور پوتین، با وجود جنگ وحشتناکی که در اوکراین در جریان است (رابطه همچنان مانند رابطه با رئیس‌جمهور زلنسکی باقی مانده)، به من گفت که سلاحی به ایران نخواهد فروخت. او درک می‌کند که من سلاحی به اوکراین نمی‌فروشم، بلکه به کشورهای ناتو می‌فروشم. آن‌ها قیمت کامل را می‌پردازند و اینکه چگونه آن سلاح‌ها توزیع می‌شوند، من هیچ ایده‌ای ندارم.
🔴
بنابراین، دو کشور بزرگ که مردم اغلب در مورد ایران از آن‌ها صحبت می‌کنند، به نظر من مشارکتی ندارند. اگر چنین می‌کردند، برای آن‌ها بسیار بد می‌شد — قطعاً در بهترین منافع آن‌ها نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/137255" target="_blank">📅 18:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137254">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
سی‌ان‌ان: ترامپ با اعلام شرط پیوستن عربستان به پیمان ابراهیم، توافق همکاری هسته‌ای با ریاض را به حالت تعلیق درآورد
🔴
ترامپ از این که، وزیر انرژی اش، بدون اطلاع قبلی او این توافق را به طور عمومی اعلام کرده بود، ناراحت شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/137254" target="_blank">📅 18:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137253">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcMN5bjHWWJvkJK_V67HXaiI3Juj220x4NHG8zy-JxqLQJUFHfWp9cG_3cUcLFjD38MTikdZMUprBQmbnunvt_17-5muoKz54LGpQAABYuoz-PiU8FWznslHlux3Y6ZZ9KMpbhUXHjV6v89xdTTkk-He-0wR0aTLtykF_F-IOvljlTLVa9JWa9azxotoN3LuQsUV4opob_G5eu56TMMydA_24KnQeNBnTRw-sRnP-VHFFY5sQ2ANDk2WRin4dmxulP4R3uPHZOc2YR4j5OdQo5XGm5mhtVEDTUwdkd2QIlemtA9yqId3M-RkvSesPOCuUI9fCcVFvhC3OjWqRSrrOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرویز پرستویی:
تا ابد بر پهلوی و طرفدارانش لعنت
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/137253" target="_blank">📅 18:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137252">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
رویترز : پاکستان و ایران دارن راهی پیدا می‌کنن که دوباره مذاکرات با آمریکا شروع بشه؛
🔴
این روند هم با ابتکار چین داره پیش میره
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/137252" target="_blank">📅 18:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137251">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cf8ecb014.mp4?token=sCLBNv-yL2zWdQr5nc9OjrChOplyInyD__JUxnkF6hU9mnFSg20SW4qpEzC3bo4hLUKIZ1C3iBSdZxfjhk6JMGoH1leRacCwCrsRKkfuBFy_E44GRu4lA8sj3XoeWsAy-E9uGS7x44BFoZlhUnb1HT1UUJOhzUDqeQcpPWEgTbSVGtCTT-08-Tcrfzgz9Uc0kAUyMk1vc5UuXD7FKj9t1OnJmFWXohI17_teapQk4T_CorqOPwYf8oaXPlLTZudF2XU6XAUhQQVdCojMqxk8AKaAChXU0G-5EeVm2IeQZFSihZRg2I0WX361XFY1a2sKEBN3K9tRXvuG15BC37iwGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cf8ecb014.mp4?token=sCLBNv-yL2zWdQr5nc9OjrChOplyInyD__JUxnkF6hU9mnFSg20SW4qpEzC3bo4hLUKIZ1C3iBSdZxfjhk6JMGoH1leRacCwCrsRKkfuBFy_E44GRu4lA8sj3XoeWsAy-E9uGS7x44BFoZlhUnb1HT1UUJOhzUDqeQcpPWEgTbSVGtCTT-08-Tcrfzgz9Uc0kAUyMk1vc5UuXD7FKj9t1OnJmFWXohI17_teapQk4T_CorqOPwYf8oaXPlLTZudF2XU6XAUhQQVdCojMqxk8AKaAChXU0G-5EeVm2IeQZFSihZRg2I0WX361XFY1a2sKEBN3K9tRXvuG15BC37iwGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کپلر: عبورهای تأییدشده از تنگه هرمز به شش مورد کاهش یافت که نسبت به روز قبل ۶۰ درصد افت نشان می‌دهد
🔴
به‌جز یک کشتی، همه شناورها از مسیر یک‌جانبه تعیین‌شده از سوی ایران استفاده کردند.
🔴
در مقابل، تردد در باب‌المندب افزایش یافت و به ۴۹ عبور تأییدشده رسید.
🔴
داده‌ها نشان می‌دهد  بازگشت به تردد دریایی در منطقه به‌صورت محتاطانه و گزینشی در حال انجام است و شرکت‌ها همچنان در حال ارزیابی شرایط امنیتی هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/137251" target="_blank">📅 18:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137250">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
حملات اسرائیل به خان یونس در جنوب غزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/137250" target="_blank">📅 18:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137247">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mmjPIk1UwUeHY3ci_2Yosc5GPvJrrSbsNcjMwSUr387nbaD9ovdJwpwlLTsg-3UMKtbzuqp5aDMlK9z7J4-6eBClJ2jfg_GB9Qjzp4SqolgwLKWCd-Weu8jZC0KtJKsyEROYSsklEi469HWHg-nKWsy6BcHXlcyFBA_61hqTVyDfSkpPocwGI0DellMLpSan8qPBC3woQb8nSXI_qSOoRqQ8L56yZIzoPI1qBcYLPG3yqDBV9UxzaDX__KjnQkUYQRWJc62MqniH9B3zY-S4uiU3c8weRigrda0aBYb5iHhxvzKEd5dsrK23O_9GT0rA_K349f3XFCG-DahuB6assA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CEZtWYz6rInDufSMJlqHEm0dPMHS7mNYhH246sdZSSZPY35OHRhGL3FZwaSqSwAhUs2Hx8O3V1t-Mbk5E3KklxUc1NdelU9bENtvzIMQu4G8imTz9vniS5boEhbygNTIitOaNjZtD2MkpRdRBRvAl3IkiflM4I4qhxAcFECBBwMEN5c8c94pxSTah69uuQCzmfBjpv4ArJMHLdGXncOwi1nQaJbxChr9Na77GO_js379jTIrnvTyemvm2LIPZPnZQTDjxIccWnOO8In8DIC4oJO-jGgaX-GlvufqZ3TnNF9OJXoWFfqhnP7dd4Z9i9OpATrPl1U_ibIk6uLceY1l4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VL0Gi7Pdbd-yUA2cU4-lWQIsoP6sRLXL7SlFFKlNcXywIgHMVAkX24LV49ujoknZD4JftSsjWn4tq2wzoJOvucEF8JcMN5v1pb2cl-JMyD_VnyoSq48HWWoAPkl4Zrb8Kn5Cw8osjk82F--hTpZWAxKAN_sJpTiF2scGWVwvZaTy16Au2TtM77k9JReFRM4Nn_Nuu5Advlpv_z0me2veOVWj0lSqW0lyHV89LBS8iaxh_M0vY4P0vUDuk2Mu7D39KoE3uttkrh0MyCx8r0QTdJGPDM3Cl_KilUnoQM-_3oAVcs10AWVV1PLsRxwtuOpZMkSBeL-uJx8f0-SzC5_TWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
سنتکام منتشر کرد :  تفنگداران دریایی آمریکا یک سامانه موشکی هیمارس را در جریان یک تمرین آموزشی در خاورمیانه سوار بر هواپیمای ترابری KC-130J سوپر هرکولس کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/137247" target="_blank">📅 18:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137246">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3927f843ee.mp4?token=lu4eSGaKYSPhmOyBAWYx5N11uxlKLlmz4zTxgHx1pW9ulml6J35VU74lDSZ76iiBgDZcTBmmylKI4ULKUOKzLWGac1uSAw3iuQ5RAToelpwV7OYE6ZGuPV7EVCYRbT4a6yAc6zrOmzIeBZJ6nA2fdjn44NFkMTNBGqqjgCQ1Ez9n0wrESg_JwcfKnKjHzjrHOFDH19Ahu2uWQFSnIzeYI6egxFEuA1Tf9NKQQPfEFlMs-2pfe3QNdxO1mmZPmKAJsXgqh2tfqbXh57utFwIVhmUM1aLq0_6t8OuVC6SD_XrQDO7Ef2-vWib4uVoX65rgmtZyBKv1grQNN5YOYDrs3ii0izKIoYyIh83xm48jU6iYf8TSILF8baueyOktSAMkYhmpc-GEyBqWzsObHgy0H1knIiva5EZy56VOgjr-ktKljiNYtkDTha7HGU2EbtScQRQ0Lu2lMGE2aK5GQLJ8E0Ao0Ad-fYtVqwPIcKEFyKGfh1R-4Ph9NaIdgJ0g1qfWtA-z9iuwMtziGbSuhY0jMJh8CyOv5fqcG9PTk-D_rOg6IHwl2JNep_pvSkhfndVFayUymO4lmIGVMzOgKTDWt_X_i7ObxwIJRmUMUiIkbvYRglmPsv_WgcPe2sIkpVcHmfesQe67yKX7dPKIIyFfSGHz4a6RPdnZThhAp1lJ3mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3927f843ee.mp4?token=lu4eSGaKYSPhmOyBAWYx5N11uxlKLlmz4zTxgHx1pW9ulml6J35VU74lDSZ76iiBgDZcTBmmylKI4ULKUOKzLWGac1uSAw3iuQ5RAToelpwV7OYE6ZGuPV7EVCYRbT4a6yAc6zrOmzIeBZJ6nA2fdjn44NFkMTNBGqqjgCQ1Ez9n0wrESg_JwcfKnKjHzjrHOFDH19Ahu2uWQFSnIzeYI6egxFEuA1Tf9NKQQPfEFlMs-2pfe3QNdxO1mmZPmKAJsXgqh2tfqbXh57utFwIVhmUM1aLq0_6t8OuVC6SD_XrQDO7Ef2-vWib4uVoX65rgmtZyBKv1grQNN5YOYDrs3ii0izKIoYyIh83xm48jU6iYf8TSILF8baueyOktSAMkYhmpc-GEyBqWzsObHgy0H1knIiva5EZy56VOgjr-ktKljiNYtkDTha7HGU2EbtScQRQ0Lu2lMGE2aK5GQLJ8E0Ao0Ad-fYtVqwPIcKEFyKGfh1R-4Ph9NaIdgJ0g1qfWtA-z9iuwMtziGbSuhY0jMJh8CyOv5fqcG9PTk-D_rOg6IHwl2JNep_pvSkhfndVFayUymO4lmIGVMzOgKTDWt_X_i7ObxwIJRmUMUiIkbvYRglmPsv_WgcPe2sIkpVcHmfesQe67yKX7dPKIIyFfSGHz4a6RPdnZThhAp1lJ3mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کاژا کالاس، رئیس سیاست خارجی اتحادیه اروپا: ما با آمریکا توافقی داشتیم و به آن توافق پایبند بودیم، به تعهدات خود عمل کردیم.
🔴
منظورم این است که مذاکرات آسان نبودند. برای شرکت‌های ما مهم است که پیش‌بینی‌پذیری وجود داشته باشد.
🔴
به همین دلیل است که شرکت‌ها می‌گفتند: «به نتیجه برسید، به یک توافق مذاکره‌شده برسید،» زیرا پیش‌بینی‌پذیری بهتر از این است که نتوانید پیش‌بینی کنید چه اتفاقی خواهد افتاد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/137246" target="_blank">📅 18:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137245">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
عباس عراقچی وزیر امور خارجه: رایزنی ها با روسیه و چین مستمر و مستمر است و ما به طور مرتب با دوستان خود در چین و روسیه در هر فرصتی مشورت می کنیم.
🔴
طبیعتاً با پاکستان به عنوان میانجی در مورد ابتکارات و پیشنهادات آنها گفتگوهایی صورت گرفته است. مشکل فقدان میانجی…</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/137245" target="_blank">📅 18:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137244">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
عباس عراقچی وزیر امور خارجه:
رایزنی ها با روسیه و چین مستمر و مستمر است و ما به طور مرتب با دوستان خود در چین و روسیه در هر فرصتی مشورت می کنیم.
🔴
طبیعتاً با پاکستان به عنوان میانجی در مورد ابتکارات و پیشنهادات آنها گفتگوهایی صورت گرفته است. مشکل فقدان میانجی بین ما و آمریکا نیست، بلکه مشکل رویکرد مشکل ساز آمریکایی هاست.
🔴
تا زمانی که اهداف و خواسته های برحق مردم ایران برآورده نشود، طبیعی است که به تلاش خود ادامه دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/137244" target="_blank">📅 18:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137243">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ایرنا: حضور هیئت دیپلماتیک عمانی در تهران
🔴
یک هیئت دیپلماتیک عمانی برای گفت‌وگو در خصوص ساز و کارهای تنگه هرمز به تهران سفر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/137243" target="_blank">📅 18:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137242">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tt4NvkNuhuNef7m3rO5H98z5ok8tiL0dcIr8sRqFjVYsEtEkRpF7xZj5QZvOFsjqx8fGSgGok9q7l0JqlyMu2InjGyY3WRIaeeK40KeTdTtW1_zkyLdeWAI9_ZacoiuJhpYGpcg9f-2wQFbSIvOI-lVW5mSgoIOaIAtkH4rlWX9ri4ZG9eMN23TE4g8BY9Wn0YaxWvBw_x2l9wkqgn7aEEEtFBm5p-cCb6I3tzNhmL2hDdpyB47FL8NECA2TgG4OKetVG1MbZxsxqGO51kDWLSGWONhrVwHOzXu41UMM3pecQeT35ClhxWjKIEVXCpdZ4wsefeUozs_zamQmd3V8Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی هوایی متفقین ناتو اعلام کرد که امروز صبح دو فروند جنگنده اف-۱۶ رومانیایی و دو فروند یوروفایتر ایتالیایی برای رهگیری یک پهپاد ناشناس در آسمان رومانی به پرواز درآمدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/137242" target="_blank">📅 18:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137241">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXifYFdKxfIXDUdUIds--JWNVbO4NY3BpcOy7aHcjQFrGoUpYLVR6CWrb2hhT2rePrA11uLvNGXJDSLvSd0s6qhSVOZYSsx6JjcSduotkUbFpuCrMc9h_Sz45KbxOKHF56XUcnkIInlW5YWGqkkyM715KoOEFWr8BlpZ468HZTelmr91zwt9pNI4OoB_Zb47gYapNOM8-uocM6LEQ79qTgD5JTr8TcPdKMn6FDUre3Yt6M9tPnEXCssBS-FAB3ngKy--RbhltO73_UNnKwam8IneGyOBqNy6MmdfBZlhxGtjaUvFPgspaAy0MHNBmfADIBTRImLZ-RRLjR2ZgX17Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز 2 مرداد تولد جاویدنام نازنین‌زهرا صالحی دختر 13 ساله ایه که در اعتراضات ۱۹ دی تو کرمانشاه کشته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/137241" target="_blank">📅 18:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137240">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا اعلام کرد ۴ فرد و ۹ نهاد مرتبط با ایران را در فهرست تحریم قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/137240" target="_blank">📅 18:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137239">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
عراقچی: ما آتش‌بس موقت را نمی‌پذیریم و این موضوع مطرح نخواهد شد مگر اینکه خواسته‌های ما در مورد تنگه هرمز برآورده شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/137239" target="_blank">📅 18:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137238">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
فوری/ وزارت دفاع کویت: درحال مقابله با حملات موشکی و پهپادی هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/137238" target="_blank">📅 17:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137237">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
بنیامین نتانیاهو روز دوشنبه آینده به واشنگتن سفر می‌کند/وی علاوه بر دیدار با ترامپ، در مراسم تدفین لیندسی گراهام نیز شرکت می کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/137237" target="_blank">📅 17:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137236">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
شورای اتحادیه اروپا امروز با اعمال تحریم‌های جدید علیه ۶ فرد دیگر به دلیل آنچه که «نقض حقوق بشر در ایران» خوانده، موافقت کرد.
🔴
بر اساس بیانیه این شورا، ۵ قاضی دادگاه‌های انقلاب در استان‌های مختلف ایران در فهرست تحریم‌ها قرار گرفته‌اند.
🔴
اتحادیه اروپا همچنین یک مهندس رایانه ایرانی را نیز تحریم کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/137236" target="_blank">📅 17:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137235">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
نیویورک‌تایمز: پنتاگون در سایتش آمار نظامیان آمریکایی کشته‌شده در جنگ با ایران را از ۱۸ به ۱۴ نفر کاهش داد.
🔴
۳ مقام آمریکایی گفته‌اند که دلیل این موضوع این بوده که مرگ این ۴ نفر پس از اعلام آتش‌بس توسط ترامپ در ماه آوریل رخ داده است!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/137235" target="_blank">📅 17:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137234">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WA60LtHgGNA6EzwRhq_KjxwKBM-xqFsAK0mYQ1aL0RVdgKGD3y5BVtAOa751n8RbCw1iP6LOFUvZJCiK_3nlZ5KKqpWb1b3pdQx0BSCnmpU2hH_VNpLU9xglWNIbw1ZHcXQxJt6aJo5c04a0B53j99pREM4y7rgBviOeH-47RX3_O-HmF_Axh9c08rFCR7lL8PmPMYBqWTnDehGmKjQiFWsG4-IiFERQLsdw0hO6MqgcMUKkvipSjNJ-JYOzPspqkQqe5RWsHAdnguo-XmYnSFWJdEvdbQo15Z7ulNUSLCHO87gxKNwet7QsBBQJZP4XUH2ZhrAcQyTAw4YLxtSVBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جبهه پایداری افغانستان(طالبان) اعلام کرد در صورت حمله زمینی آمریکا به ایران ساکت نخواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/137234" target="_blank">📅 17:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137233">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
وال استریت ژورنال:
ترامپ در مورد ایران بیشتر به گزینه نظامی رو آورده و فعلا پلنی برای مذاکره با سران جمهوری اسلامی نداره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/137233" target="_blank">📅 17:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137232">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
سخنگوی وزارت کشور:
برای هرگونه عملیات زمینی دشمن آماده‌ایم.
🔴
روز رزم ما، روز عملیات زمینی است، اگر بیایند به خدمت‌شان خواهیم رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/137232" target="_blank">📅 17:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137231">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
سخنگوی حوثی‌ها بسته شدن تنگه باب‌المندب برای همه رو تکذیب کرد و گفت محاصره دریایی فقط عربستان سعودی رو هدف قرار میده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/137231" target="_blank">📅 17:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137229">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rMcFkLdNZlPuHqunJjCoG2qtFXGy7-Gt8eQSBi79X455R69Cinl6WE8asBtzbQNOEqjD1L32BCMl-2Rht2hWahaN_LRJC9AK11yaUtLcaFrW04peso0mqFg_0dGbk_2FeT92PkgQvVeY18v50A2m_0gVsi_ZD_BlShGW-_1EUQs4FQFxKo6QFwOnHV_cMUZIeGNtnuzTM_wViPL3_JHrvUYXUrzHzvguQNQHVH8a-ypwyL0wmdBJPkyCiLAKvCR9lvoZvvlkRXO9ivrec_mDx7AmwWsfaM1YDWvRFKbetbbAE5CVMgbpxe8GFkh2rr4YX7v4QHCF-jtOMi3QELfLXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YZyPnV6fv9DxUDhGBtLgW8f5VNg48UPQg9kW-6Zwdg7up0ST2RC08W6_fTlf73TjqDMmq4KRtiP9RYvNyom7D8V0XPMX3SpddiqgaaQNaH9MRg9PZ8EuTyL8vhzLe3MzN5KHIKnodPCr2mPLZ-SiYNgxmV0B8A3TMomxbJi-qAcyKwO-qc3tk5AaUUJlEnwVzdvFg0m3Va0mv6FhouMfAlNbhuQ6puJ3RWqCJyvEBuAHsK6lbfZRltyTU89NTX30u8BOgHAcplD4Bpjx6Wo137FV3_Tu-Bc0WKCaUFlHvg1YVD6LVEZ9Ptv-Tz1yQXqiMHMxJFo2-CfVIf7oXERO8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برند معروف گوچی از پوشک جدیدش برای بچه ها با قیمت 88 میلیون رونمایی کرد !
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/137229" target="_blank">📅 16:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137228">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
وزیر خارجه عمان:
تنگه هرمز باید برای دریانوردی باز و قابل دسترس باشد و از هرگونه اقدامی که مانع آزادی دریانوردی و جریان تجارت بین‌المللی شود، خودداری شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/alonews/137228" target="_blank">📅 16:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137227">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2ad0195b5.mp4?token=OJ4VIcQ5L9NKeLr6LeevKw8Ga558m0dRm9XGGfRy96n_e4uoUmo5eeBpJT0jiysfVidmFWJT5yQY4EmL3yKwCjJxHKx3y7VnZcxViXLC48GbBpsekmLFOrewVIOngeDo13sYWF5S6bzirrcsM1F9N7EF7m_bsWvQFC1PBxxLh9bsZvW9vRiADD7dAGk0zCBdE4PaP-Q-dJ5EnACjGFMwhUgJ59wu43sZuqLi5a6Uz3TMB7-0CMtRAxf4MgVGSswOHXblA0snGG6NpOx1AZru9bsq6sUpl1rho5lVv1sQCCIZqmrprT6vVMpCnYN1EIUY-fQ7nCmmomuE9UHtzrV2Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2ad0195b5.mp4?token=OJ4VIcQ5L9NKeLr6LeevKw8Ga558m0dRm9XGGfRy96n_e4uoUmo5eeBpJT0jiysfVidmFWJT5yQY4EmL3yKwCjJxHKx3y7VnZcxViXLC48GbBpsekmLFOrewVIOngeDo13sYWF5S6bzirrcsM1F9N7EF7m_bsWvQFC1PBxxLh9bsZvW9vRiADD7dAGk0zCBdE4PaP-Q-dJ5EnACjGFMwhUgJ59wu43sZuqLi5a6Uz3TMB7-0CMtRAxf4MgVGSswOHXblA0snGG6NpOx1AZru9bsq6sUpl1rho5lVv1sQCCIZqmrprT6vVMpCnYN1EIUY-fQ7nCmmomuE9UHtzrV2Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو عجیب از تجمعات شبانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/alonews/137227" target="_blank">📅 16:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137226">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
چندتا عکسای صحنه‌هاش که منتشر شده رو ببینید
◀️
مشاهده تصاویر  زیر ۱۸سال نبیته</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/137226" target="_blank">📅 16:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137224">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/beaR2rpytZf1KsyWvZRkp9SaJ8DoH9YxsUsYYZ71cfPgV9s8JViupuA2ry5IYGfD1QeRSewTg7EpC0fwAXQ0a5BchkR89MMRdBAp5CQEMOZQ0L6g1-1oEiPXbQJP4WnvmbYIQrF374y_Sh765OztxvP7XgjZRHdt4AC_kZ_-yjSjorMjtJPE7rI9BGOANnlxtIhooEx291raxs4Clv_40qY1E3wZvzfU1dCyzjlNLoFJ6S_echerFzT2tLuWZBrSFX0Sa3lq4CBTNx9EraSngohXnJyGY7GeBh3LP4tsWrPA11HyvqXkNVFwRc-mvioihCbANHaJybEwX2AItcKUGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h0Pul3TrsIAi4Cksr2gVZn1QJupDmMzo6sHLQr1bhL7BLfbdt31L5-av7dA7e3RK3lROOGfz6ne1a0nxOQDVcuQ9LdMGcm0w6IZSGHzPbSqnKb4deQmkj9U4Y-GNq53J_Xa7YO70SbMXX1LTpBAjLKpdpNL5zK3I_j1BkWdEc3bSHnBpl_wCS0ogCbaLCX1pVrBL3LifslUwmmacDkRzHZPvOuNBj-gDn0ZbnSLC-ogLXOfoI5wvXDv-M5Qc5XDN76pn-cITvtHE-S514-nq_cgJUFDKHZTnfNyWVTDWWITky-MshrGpgVtC18NYoBeHYG2MuS8xDY8-cMzaI7VHCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
بمباران فرشی یک پادگان نظامی در غرب شهر اهواز توسط بمب افکن استراتژیک B1 آمریکایی
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/137224" target="_blank">📅 16:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137223">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnRO2ZHCwSc0geOIOwyizz9XBEhw80yrbhVB03462YGHOe5vzHs_Qh8obRCTU1kKxEPExJQsar6uC2rQw99VV-jg3UEAGMisb89ZDAtQPGbrTpXBtbF8wHhmsu85mjDByBejEtc-4rIGvtxbcFadn1YvcWE_RmUr6PPTLwLNH25-jQcKsFglLFkzZAejTq31D7VE5NYDzv0UBaX5ExFEXK2oQbdebEOVumFxZcZtJrekMMhejoI5WkLusK7MGME87qrGZVp5BmG3gOezrYqJbEA2L6HrQgHUBPFKciT4nSPtXIxQ_XAJUO0s0nb4JyW3Ok_RjYdbYa9GjRNkOpvyJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علم الهدی:
آمریکا پول داره اما ما خدا رو داریم
🔴
پ.ن: فعک نکنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/137223" target="_blank">📅 16:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137222">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51678b4c9d.mp4?token=rjGFDyn6KoohNRBTPjpjhadf8QI8xUTzPAI5eD2SgDTmx3n9QIfy5uL83TgljZyvk5a7j-T0Psf7cwhAekmSyoDuiIpuY08RUX05wShzC1-YGr8q60qSTzB0yq8pbK-BrBGVy4dXDoi9DaEFYNhvefVV1JkRJolfAZjpYwIjO3qg2QFocFMxW3O5rK-zQtuLx2aS5fNlB0i6g42VOi9WVUXPaZ2uKWlArY8QBlgUmorQfmrKajpHERIQO3E4joGw2yWcx3BR9UpsHCWbQi5tzMmfEq4SOzgF-ilTW3nY_C4TrFXbG7Uj-TcuNyElGzA9MQzLQ48b7qd0tW3zb8Ml4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51678b4c9d.mp4?token=rjGFDyn6KoohNRBTPjpjhadf8QI8xUTzPAI5eD2SgDTmx3n9QIfy5uL83TgljZyvk5a7j-T0Psf7cwhAekmSyoDuiIpuY08RUX05wShzC1-YGr8q60qSTzB0yq8pbK-BrBGVy4dXDoi9DaEFYNhvefVV1JkRJolfAZjpYwIjO3qg2QFocFMxW3O5rK-zQtuLx2aS5fNlB0i6g42VOi9WVUXPaZ2uKWlArY8QBlgUmorQfmrKajpHERIQO3E4joGw2yWcx3BR9UpsHCWbQi5tzMmfEq4SOzgF-ilTW3nY_C4TrFXbG7Uj-TcuNyElGzA9MQzLQ48b7qd0tW3zb8Ml4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این مجری تلوزیون داره دم از فرهنگ ایرانی و اسلامی میزنه و میگه غربیا و نمادهاشون بدرد نمیخورن و ....
🔴
بعد خودش رو گردنش تتو داره و سعی کرده بپوشونش
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/137222" target="_blank">📅 16:05 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
