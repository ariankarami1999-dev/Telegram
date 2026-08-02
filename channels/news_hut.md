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
<img src="https://cdn4.telesco.pe/file/o4bLWi1ynTFG6MP485nQhDfl6LyZBkKmNVQg24VmVRPLvzpmcy1VELVVw3fq1-B03ywU8Y8gllbWetlUlAWgTNGyZAQzzxJE9YoKDtzYEdMCUUBKssz1z0DZTTafEdA4ZdUxz_G1msnl8vr3q3H3dOvRZMqPZnrqjLdzrjAr9DB3r3sDrUcx1-cxp3ZQ-HnCMVXeN4Aqn97geqv2tLVgCWagXeLJw4w67mVd0M9n3uqtG3whyXGeHsyhPYF_JwSvcO4RPwnyqSgkCw3TW_vqCn-6okjheCFwLc6-dTDLQP5St4p56I9bqSKHs5J5tcKGcfeI3bqQwu_uKMD6HgwGwg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 137K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-11 10:57:27</div>
<hr>

<div class="tg-post" id="msg-69409">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66dc919056.mp4?token=VUTrkY8AmNJGwhc6c5fR8NmPkpyt9-ZI9UE_PIfgXfsGysCvttqJ8CCI_7P1pidwKd3twXXQwGo0JBN4MV3mW3wTI2cAMtJcXJrHlPHdBML1SP1849MjN7NY77-1iLjyr0A5Sy2mD4FnIaX5pwpeD4toM5K6uHS7mLXrk04ToSKjBiunFusO8oNBVfycJOMg2wguggCaETD1ohF9MQH0g5SscHXVBgJImOyzwBqwjdmbxYpNdG4WQJCsplcyxomK3o646-YMAj1eZBjn1JZTjI6qjSP1Le6Im6YrLjbFbi4up1f7Q3mI2laOM1GP78N6x7ml4I3pD-dJChlvA8Wq3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66dc919056.mp4?token=VUTrkY8AmNJGwhc6c5fR8NmPkpyt9-ZI9UE_PIfgXfsGysCvttqJ8CCI_7P1pidwKd3twXXQwGo0JBN4MV3mW3wTI2cAMtJcXJrHlPHdBML1SP1849MjN7NY77-1iLjyr0A5Sy2mD4FnIaX5pwpeD4toM5K6uHS7mLXrk04ToSKjBiunFusO8oNBVfycJOMg2wguggCaETD1ohF9MQH0g5SscHXVBgJImOyzwBqwjdmbxYpNdG4WQJCsplcyxomK3o646-YMAj1eZBjn1JZTjI6qjSP1Le6Im6YrLjbFbi4up1f7Q3mI2laOM1GP78N6x7ml4I3pD-dJChlvA8Wq3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
با این حال، تغییر رژیم هرگز هدف اصلی نبوده است؛ هدف، خلع سلاح هسته‌ای بوده است. آیا می‌توان یکی را بدون دیگری داشت؟
🇺🇸
مارکو روبیو:
هرکاری که توی خاورمیانه و جهان انجام دادیم کسی مانع ما نشده و موفقیت بدست آوردیم
رژیم باید تغییر بکنه شما شاید تغییر رژیم نداشته باشید ولی باید اینا تغییر بکنه
اونا میخان
انقلابشون رو به کل دنیا صادر بکنن و باید این تغییر پیدا بکنه
ایران تابحال با رئیس جمهوری مثل ترامپ که مرد عمل هست رو به رو نشده
اونا هنوزم موشک و پهپاد دارن میتونن صدمه بزنن ولی خب سپری ندارن پشتش قایم بشن
از روی قدرت باهاشون مذاکره میکنیم نه ضعف
@News_Hut</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/news_hut/69409" target="_blank">📅 10:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69408">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb72a3070d.mp4?token=qBFQkw1xFqxFuw8olggR7EtfA3suK6JCuQWbrVKYh7f6CesvV8B7UG1zUWumK3qtw7ONQ05-PALBEWglg7xVE748K6osMCcKOlup0YG8aLqjB_FNK2pDcVdOZyk8KVHLNJ7E8RnVpzPd1QtQ0l2NC-yhxd6rRg1oNov1E5oDeQE6D4pvE8dF_PSUnHW5hdLZpM71W-xdqdfmn97fpnXsSySvmvT_DfPO40NKIV8IhkPQNk0gl6r_1dnGd_wWn3pJ_hsv4JsPjg1axJTM86cfFYmEvlQLVkUHMsdcsUBxOOJ4jvncK2CpATJ4yDL5JI2kzU2QOl1EiOEsanB4aBFABg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb72a3070d.mp4?token=qBFQkw1xFqxFuw8olggR7EtfA3suK6JCuQWbrVKYh7f6CesvV8B7UG1zUWumK3qtw7ONQ05-PALBEWglg7xVE748K6osMCcKOlup0YG8aLqjB_FNK2pDcVdOZyk8KVHLNJ7E8RnVpzPd1QtQ0l2NC-yhxd6rRg1oNov1E5oDeQE6D4pvE8dF_PSUnHW5hdLZpM71W-xdqdfmn97fpnXsSySvmvT_DfPO40NKIV8IhkPQNk0gl6r_1dnGd_wWn3pJ_hsv4JsPjg1axJTM86cfFYmEvlQLVkUHMsdcsUBxOOJ4jvncK2CpATJ4yDL5JI2kzU2QOl1EiOEsanB4aBFABg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مرادویسی، تحلیلگر ارشد اینترنشنال:هدف‌های احتمالی آمریکا تو جنگ جدید میتونه شامل این موارد بشه:
1. مراکز نظامی سپاه تو جنوب کشور
2. شهرهای موشکی و پهپادی تو عمق خاک ایران
3. تاسیسات هسته‌ای "کوه کلنگ"
4. مراکز نظامی سراسر کشور
5. سامانه‌های پدافندی و راداری
6. پایگاه‌های هوایی ارتش
7. مراکز و نهادهای حکومتی
8. ساختارهای سرکوب (سپاه، بسیج و نیروی انتظامی)
9. مقامات و فرماندهان ارشد باقی‌مونده
10. مکان‌های نمادین مثل صداوسیما
@News_Hut</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/news_hut/69408" target="_blank">📅 09:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69407">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cbd0e326f.mp4?token=t7Xx-rFRC9O22-7XGm7zb6x2kn7r24I8YL_6I87Ii30o6qdJnRspxYIhP61TzdBZKiyPM_AY9lgy2a429w7jtp7lbjqcGqoHCDVPMf5ZIUr81-PqvTNYFAb8Sl3Tm3SELN8WKNRHNucaFdgBH3nNUe4kNrxM-q9xSyCxG3PPEpDvnpORcjrTQd4fpIOq6PajaLKBymYl9TbBy56Fzbi-ES709SWkKv7GMRlVA276Po_ztF_hjyGfYyd9_rY8NEqs19rPnXX5n6eGuOOj8XGuHi5eGOQc4CTwELt9AhyGrW4VPTIBD-GShV-H221X-RXXqajHL1D6PIGHBqkUq9T_Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cbd0e326f.mp4?token=t7Xx-rFRC9O22-7XGm7zb6x2kn7r24I8YL_6I87Ii30o6qdJnRspxYIhP61TzdBZKiyPM_AY9lgy2a429w7jtp7lbjqcGqoHCDVPMf5ZIUr81-PqvTNYFAb8Sl3Tm3SELN8WKNRHNucaFdgBH3nNUe4kNrxM-q9xSyCxG3PPEpDvnpORcjrTQd4fpIOq6PajaLKBymYl9TbBy56Fzbi-ES709SWkKv7GMRlVA276Po_ztF_hjyGfYyd9_rY8NEqs19rPnXX5n6eGuOOj8XGuHi5eGOQc4CTwELt9AhyGrW4VPTIBD-GShV-H221X-RXXqajHL1D6PIGHBqkUq9T_Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇭
حاکم بحرین:
حضرت محمد (ص) پس از قرن ها تاریکی در ایران به آن عمق روحی، انسانی و معرفتی بخشید، بخاطر تشکر از این کار حداقل دیگه به بحرین حمله نکنید.
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/69407" target="_blank">📅 09:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69406">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s09093O-_hNw6MiFoJRxHd5y2dh10ROsfoQKvhAlfeJoVx1lr-hjVTGDiAt7beVCHE3l1dDW1RJKW5tqc3djfma_qoD-ExHHwc6a4H80Hrq1FFfyPOzUM3RN-tFnGsUu_PGXpXqY9ZgacHwjuvLGLMT_-dFqxoZ78JRjBWResRBcSp4lQBWcYA6y2_LHW_TgeSZqNQHbw3qh4GHc_6QU2xJj4UTgyA6-CcpbxYpGOU3O0hSnEGL8li8zydLmc9viZ0QipO44N0fHtsXHMO_BDbUleUDSXkhXg9q_W5TDVsraPf1rkJxvmcLDJ7QNaVNdTirc4GIZIDt-W8u3M2QI7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ: حمله رو کنسل کردم
!
ایالات متحده آمریکا آماده و مجهز به سلاح است تا علیه جمهوری اسلامی ایران، در سطوحی از ترور نظامی، قدرت و صلابت که از زمان جنگ جهانی دوم دیده نشده است، اقدام کند. با وجود این، ایران و سایر کشورهای خاورمیانه از ما خواسته‌اند که هرگونه حمله‌ای را در چارچوب توافق‌نامه‌ای که مورد توافق قرار گرفته است، متوقف کنیم. این شامل بازگشایی فوری، کامل و تمام‌عیار تنگه هرمز و پایان دادن به تهدید هسته‌ای ایران می‌شود. بر اساس این درخواست، من برای منافع آینده جهان و همچنین بقای یک ایران موفق و مرفه، موافقت کرده‌ام که حمله را لغو کنم، مشروط بر اینکه بتوانم به سرعت به توافق‌نامه‌ای دست یابم. کشور اسرائیل در این تعهد به من می‌پیوندد. همه دست به کار شوید و آن را انجام دهید. از توجه شما به این موضوع متشکرم! رئیس جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69406" target="_blank">📅 06:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69405">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTbWcFqK-wmHBdHOLMQ9B2GqQyRSlPacvcSruz2BUlnwKCqTxddm3s22crvxW9bxiuc_187DWnfFLjEqsMpomKx_F0fI_3ai0SSlnWODZMrjhv3Xf0hi-ToPbyk2Ld9R3UoIJflB19raPq696XBKAR1S6zr5uMLbhool2cPSYSssazbEE5uKhxRAjrOX7i4fCfbocnB1dhTBkAVRW6SDLbaAze0_MLtTRej-_t43zQ-Bw8dOCF_x1Z32Xq-5GyGs4aHzdI11Xm6QwA-kr56EVARlGBcFqzXu0RrTL76OzNWglejlc5CDRa2aX2KftGRkaINyioolzYI9zfIVbjZSZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیکه و ترامپ چیزی نگفته.
#hjAly‌</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69405" target="_blank">📅 02:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69404">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6db9d071b.mp4?token=DwFe2LHFEqJsgnLtepq1V2nYsD8chLLnyTkHVmPhn0hzvA54TBP2unxcAP9-qaR5w-X8OX6CM6I3e2Y4K652cOZI_R9X9OWQKRGpSLftGSxJctTkmsnPSCszYWtOTqc_-uHirS94RwMSB_bWJzns1Ls8cTvonxgAQFHL0SGWEZR1aF1hEH0iurHx7nTzIBVaWsEyPTcKL4qEC7XSBo3SrJuZCUjwrG5MlxW2N54XkdQ3V-iW2M2Se-fcwED3ujIzmNGadb5l23xArRXhW81ygf9lc9Yhe5buwO7C3TSrOZOEtwmH9VwfEEsn06z6mfnRkqVRHBTo8xo5tTFlhAPiIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6db9d071b.mp4?token=DwFe2LHFEqJsgnLtepq1V2nYsD8chLLnyTkHVmPhn0hzvA54TBP2unxcAP9-qaR5w-X8OX6CM6I3e2Y4K652cOZI_R9X9OWQKRGpSLftGSxJctTkmsnPSCszYWtOTqc_-uHirS94RwMSB_bWJzns1Ls8cTvonxgAQFHL0SGWEZR1aF1hEH0iurHx7nTzIBVaWsEyPTcKL4qEC7XSBo3SrJuZCUjwrG5MlxW2N54XkdQ3V-iW2M2Se-fcwED3ujIzmNGadb5l23xArRXhW81ygf9lc9Yhe5buwO7C3TSrOZOEtwmH9VwfEEsn06z6mfnRkqVRHBTo8xo5tTFlhAPiIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آسمان سلیمانیه
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69404" target="_blank">📅 02:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69403">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5cdd81f13.mp4?token=kCvLolWW8UTbQ9Ll5gAaPbP-Y_okmGfprtQPPy3UN4UW3ZKEVh_ZY3mr6gGqdLAcP6lZAqg55GBrXRCfMC5-TFhSfWlsowT1MG1ybPsELfZOp9bbBKA3lkF0Ay5CiP_LCBkk1o2TXa6y5NbYRHv_ht4DJGDRtZxQaqqTgFr3q7TL7lkkT7y0SjxiiIVz09enD6T0kPMRY0Gqy1bwG1mx6j9IZDg4QmiyIuYgNTtootdt9TWe4sd2VL_kPdQMK7h6AfGtAP30jv6ZTC1eUdWn2iQBZgewAqrvEOT3eMwSR0VGvkW7vGTI76ztIOPqkIrt63lhbi07-C92zO_6bz_3xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5cdd81f13.mp4?token=kCvLolWW8UTbQ9Ll5gAaPbP-Y_okmGfprtQPPy3UN4UW3ZKEVh_ZY3mr6gGqdLAcP6lZAqg55GBrXRCfMC5-TFhSfWlsowT1MG1ybPsELfZOp9bbBKA3lkF0Ay5CiP_LCBkk1o2TXa6y5NbYRHv_ht4DJGDRtZxQaqqTgFr3q7TL7lkkT7y0SjxiiIVz09enD6T0kPMRY0Gqy1bwG1mx6j9IZDg4QmiyIuYgNTtootdt9TWe4sd2VL_kPdQMK7h6AfGtAP30jv6ZTC1eUdWn2iQBZgewAqrvEOT3eMwSR0VGvkW7vGTI76ztIOPqkIrt63lhbi07-C92zO_6bz_3xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
حملات سپاه به‌ سلیمانیه عراق
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69403" target="_blank">📅 02:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69399">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PZZpaHFq1WJf3wUvz9j_SqxjYNBdtXjSbSGpJjhDlg-ZcUR2uPVLP9Tg30gCSz-SZ8FkIgqMa0-o8t55Sd04MG0eirUmtVppTocc0IrgnpqXHjIZN6D3sT_VIk9Ao_fy1K_5azdHNWHrGkPGM75wePaIEuwZQQVQc9rfcnln35o4_hyrWz8ViJ3AKENtOe-5uGd00m8-gyfh4YYXpC7rRlZ_0TqA9ZqWII_RX2OPYKzf1of1qZfw69vm_ektA85Gx-w8leL6zGEFCcbRFMcj4uxtIP1OrzwMF2iQfgZi8d6b6HwBtV9EAyYmtl6gRbcqrjXDTuDGISKYhccp3PGXsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tME_uG6_SgkzPmhJACwXCgGWGKH6eM7mAaoPWJCmjGCTQPJOHy9yDoxO0v3JNF4YQlk2iBaq1upfQJ7AySp4xr9YUTzYyGMwMttXaW76LQDrdRk6I0ei6lZfE3ebfFoHAnnFGHBj8WFnnDwPb62ntQxprb0nCqwITyUo3zC8eTBAfLnNoIwaU5ANPkSfaNC2RYJ8uwI9aeHAHro2bzz4GUoxV2qeB0p-dJRkrXM33qP2tvBh_SfzEouYUHM_opup8RcpQ7Ek6bQUYIibNpBbdnzNnyqNdTmhntVNxOCmcKP_oot9abD3cL0_KGi1cn2x6RdIsWkiosrAwkGpGEtyXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ea496ad43.mp4?token=ouZuCmTRrUngWDR4lZKnD6RGL61I9h3M3VHOmGVHhM1bdYwyvUsG8o0RJ-dGCnyWTtNTW-gR6Ex9VMo6s7J8EKgUb0QL8c8CNQ7iAy5VC-7PFOE4C49ZGjz-FquM1xP3_48QDT5Ikp1orvtHVXzucEsC3b-4Si8Lqx5V3ZCat80Oo-hKfwfZjtLD0-kTDRnuUNkAH6HpowNLoiwUy3rKbO0YPEtc7S5lfYJ47culORXYKmQIv_96sqzqgK1YTfD6R06RGGhRDvyfw0gcUVMFQR-M94nDWaUP-8sBSQMUZGp4MCuuqtH9p-zyvECglMmaVk5owNCLWSO7rEz7duNErg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ea496ad43.mp4?token=ouZuCmTRrUngWDR4lZKnD6RGL61I9h3M3VHOmGVHhM1bdYwyvUsG8o0RJ-dGCnyWTtNTW-gR6Ex9VMo6s7J8EKgUb0QL8c8CNQ7iAy5VC-7PFOE4C49ZGjz-FquM1xP3_48QDT5Ikp1orvtHVXzucEsC3b-4Si8Lqx5V3ZCat80Oo-hKfwfZjtLD0-kTDRnuUNkAH6HpowNLoiwUy3rKbO0YPEtc7S5lfYJ47culORXYKmQIv_96sqzqgK1YTfD6R06RGGhRDvyfw0gcUVMFQR-M94nDWaUP-8sBSQMUZGp4MCuuqtH9p-zyvECglMmaVk5owNCLWSO7rEz7duNErg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇷🇺
ساعاتی پیش یه انفجار تو یه رستوران تو مرکز مسکو رخ داد؛
جایی که به گفته منابع روسی، مراسم عروسی خصوصی با حضور چند نفر از فرماندهان ارشد نظامی در حال برگزاری بود.
کانال‌های تلگرامی روسیه می‌گن "الکساندر چایکو"، فرمانده نیروی هوافضای روسیه هم بین مهمون‌ها بوده.
گزارش‌های اولیه حاکی از کشته شدن دست‌کم 3 نفر و زخمی شدن بیش از 20 نفره!
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69399" target="_blank">📅 01:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69398">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">⏺
المیادین:
بر اساس اطلاعات بدست آمده، گروه‌های کرد حاضر در خاک عراق در حال آمادگی و برنامه‌ریزی برای اجرای عملیات علیه جمهوری اسلامی ایران هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69398" target="_blank">📅 01:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69397">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پمپ بنزین‌های مملکت بخاطر حملات احتمالی، دوباره شلوغ شدن.  @News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69397" target="_blank">📅 01:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69396">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff498baa1d.mp4?token=tDjZBT02CoFLAhF9VLv24OJ6BxrLEZgfW6lFLfh6dAe9xFAJ-kwQxCJYw2bu69nvvDvNUxo7_GOhMRMW2FDZho4YbCSUTNmHw9qOJUDqRUJGKvwgBbCS1qIAOfPxBK1uypkvpQz9FlOUV_BJm0TVBxo7uGTH98T-r-Wqv4cKqRFD_eYC-AMETpUVyuk9FpMWE8p7VbLWFx7ucXPR3ve-7Ts02BxHi4hPr_Uw7ljhGpMC8KJ75ZvF9r7ENLJaEMDZHSVdRMxMZ6F4H7pVVbLWm9szzfumBoJXk84zPHGuSuHYYI_VDLzmbeJXPLDTGtIOhxRvje7unc2pm6NrtpXtXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff498baa1d.mp4?token=tDjZBT02CoFLAhF9VLv24OJ6BxrLEZgfW6lFLfh6dAe9xFAJ-kwQxCJYw2bu69nvvDvNUxo7_GOhMRMW2FDZho4YbCSUTNmHw9qOJUDqRUJGKvwgBbCS1qIAOfPxBK1uypkvpQz9FlOUV_BJm0TVBxo7uGTH98T-r-Wqv4cKqRFD_eYC-AMETpUVyuk9FpMWE8p7VbLWFx7ucXPR3ve-7Ts02BxHi4hPr_Uw7ljhGpMC8KJ75ZvF9r7ENLJaEMDZHSVdRMxMZ6F4H7pVVbLWm9szzfumBoJXk84zPHGuSuHYYI_VDLzmbeJXPLDTGtIOhxRvje7unc2pm6NrtpXtXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پمپ بنزین‌های مملکت بخاطر حملات احتمالی، دوباره شلوغ شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69396" target="_blank">📅 01:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69395">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5gRMXxMOv30QPRlU5CMvv6woE9Oj8esdySslew7aioNJF5UFWA2TNtKlHCVHAgPifS3k_vVtW8__BsemugNiSXJe75c2KaLW6NaT-ed0DQSEXctSsd0esXhBgvn93eM7O_MiMAD5O9ovmz9pfrlmbvcjNCdj6_FV65dqIXvJLmlZkrulLyyj-HewnvcBeed4S648UCPmJtCOZck9kn5q4pJSghh6egV7SFIGpVaNxcUFXfU-K6Ci6iGRHAlsfGjPCtx_dtt5rxQEKRGN-XyRhIkifsOZ13wSa2wYfURPJZscW1CJZDRIcy2xvBrhDGDPrQIX0EAwQ5GKuraTsv2vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
توییت اتاق جنگ اسرائیل و اون ساعت شنی معروفش
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/69395" target="_blank">📅 00:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69394">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b418c0b947.mp4?token=d7S_j5aJpuMzOkBK77wggHBTaYBhj8501FdO2z5Q7PfgftwrG0RDLcsXno74noJMdiHG-3gMtkNVQg_q6sRVwuvGWFo-A_LJQVxO1Bq27d50wa-pmaMXAnBCv65coey2B-KD8QWh0MBnJcJk6IqwIt33O6SvfH_CZo46S2oHnnA-vfMOsKDEKBWd7azCX1BsZ27Zz0JE1GL1cV7RHEZFu1Gph_MvRlOvroNcO4ItgCaMyfGf88l7SbDsHrxTwcoEOjXk3_OqVGwN7n0YJKQCoE-UfSgVw4_nyrCGcNGqW21SnAX4O1kniFpihYIa6vtbsLRYkn9wSjINURjg7BM2IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b418c0b947.mp4?token=d7S_j5aJpuMzOkBK77wggHBTaYBhj8501FdO2z5Q7PfgftwrG0RDLcsXno74noJMdiHG-3gMtkNVQg_q6sRVwuvGWFo-A_LJQVxO1Bq27d50wa-pmaMXAnBCv65coey2B-KD8QWh0MBnJcJk6IqwIt33O6SvfH_CZo46S2oHnnA-vfMOsKDEKBWd7azCX1BsZ27Zz0JE1GL1cV7RHEZFu1Gph_MvRlOvroNcO4ItgCaMyfGf88l7SbDsHrxTwcoEOjXk3_OqVGwN7n0YJKQCoE-UfSgVw4_nyrCGcNGqW21SnAX4O1kniFpihYIa6vtbsLRYkn9wSjINURjg7BM2IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
محمود احمدی‌نژاد درباره دستگاه سرکوب جمهوری اسلامی:
نیروهای امنیتی خود افرادی را به میان معترضان می‌فرستند تا با ایجاد تلفات و آسیب به اماکن عمومی، بهانه‌ای برای سرکوب خونین فراهم کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/69394" target="_blank">📅 23:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69392">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JvmPjfQB6pA-28p5r6h4IW2jo10V9nYqJMhcsZXtGAxG6gH4wIdiFbduGoBssoLmz6o_vXddtxQVc4SYtF3resuFqx6UdHtrFmYqD5sMpEZCEetFX80PxqkS2lyN0BbwwbkSgQMmXEaiUC1t0VmLQi5Qcm6roeEt7QcSQ1uBHqk-hv0fwYGMEEZXjC8tnZlMk87rXZCaO_ZL7PIwgdySDvwGG-c11s5KZvb4btufaJvay4jvtMP_0HX_4d9E_VhLfvTblaQpKph99qQUaAjHnDQGbpR0pGa2UYGiKCEMJn7qvuB5KcNK8IVUc31RHzII7LPlIc4DNRqfMmZ6yPqQyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/82ccfb8ec6.mp4?token=X_kPMcTXjrdhbQKrSUJrqk7svNzRm8cZHNJwkeUg7-Nk2OfHG43oAkYBDxhMswI4woTZ7NJKBP_IyqWLdOnfVPQCSTbHl8Ya36yUg6bkXbhT1rcM1Ec_DjD1zD7ceSkPQCjJcBYJdC2Pw7CFlQAstxVrUcoZaucdFggLqUbPs35ZsJFi86l9OqOvvKihEZS9C1yqwtru1No_boGtKpAWOh0agbsHvnrHzNbJ8BUR5pQ3dFB4c6z9VWipQXvAkoU0lmyBUfGu9SmrWiYAga7SG02Xs1RWrSpVyNijxf_CZyl8FWJBQjxMRyomYASly0mvQzSZCT3KI5SxlUF3D7HKfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/82ccfb8ec6.mp4?token=X_kPMcTXjrdhbQKrSUJrqk7svNzRm8cZHNJwkeUg7-Nk2OfHG43oAkYBDxhMswI4woTZ7NJKBP_IyqWLdOnfVPQCSTbHl8Ya36yUg6bkXbhT1rcM1Ec_DjD1zD7ceSkPQCjJcBYJdC2Pw7CFlQAstxVrUcoZaucdFggLqUbPs35ZsJFi86l9OqOvvKihEZS9C1yqwtru1No_boGtKpAWOh0agbsHvnrHzNbJ8BUR5pQ3dFB4c6z9VWipQXvAkoU0lmyBUfGu9SmrWiYAga7SG02Xs1RWrSpVyNijxf_CZyl8FWJBQjxMRyomYASly0mvQzSZCT3KI5SxlUF3D7HKfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زهرا کاظمیان از حامیان جمهوری اسلامی در انگلیس که کارش زیرآب زنی مخالفین رژیم بود، دستگیر شد.
حالا فیلم لحظه بازداشتش رو ببینید که پلیس اومده بازداشتش کنه، میگه تروخدا بذارین زنگ بزنم پلیس
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/69392" target="_blank">📅 23:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69391">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28c29c1e71.mp4?token=I8vSk4_U_kB8scl22EXCYXagXNGdMrhoJsj39ae71eX2OCApAfOEWyIPOc-Y1uW_9UAMh5IoIlxLApizSWfjmNCCjoPClA5bUikmg8dQT1XTL-35NJry-gFmjxpfwqUDWNSWv9O4AeFaQjzWKWHvOwKaYeEJG00CY1oAoYZI84nyIvtH8gBty3IFMlMXzDskQpVvV51R1EukgSHG5Wl7RlgRzQPnXNEb0wgQ3Dq_hReKVZmT4gvkUcCyfPqMsT7dNXZaYBRmPdQK5JQC8Un1N-c_7szQdkSxPCZrfHYVivZarovXwAqPLih90WR00_6xzyrcOq5kbbOMfFLHSuhvFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28c29c1e71.mp4?token=I8vSk4_U_kB8scl22EXCYXagXNGdMrhoJsj39ae71eX2OCApAfOEWyIPOc-Y1uW_9UAMh5IoIlxLApizSWfjmNCCjoPClA5bUikmg8dQT1XTL-35NJry-gFmjxpfwqUDWNSWv9O4AeFaQjzWKWHvOwKaYeEJG00CY1oAoYZI84nyIvtH8gBty3IFMlMXzDskQpVvV51R1EukgSHG5Wl7RlgRzQPnXNEb0wgQ3Dq_hReKVZmT4gvkUcCyfPqMsT7dNXZaYBRmPdQK5JQC8Un1N-c_7szQdkSxPCZrfHYVivZarovXwAqPLih90WR00_6xzyrcOq5kbbOMfFLHSuhvFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
کانال 13 اسرائیل:ترامپ تصمیم خودشو برای حمله گرفته؛
میانجی‌ها که آدم‌های خیلی خوشبینی‌ان و همیشه میگن راه مذاکره بازه، حتی اونا هم میگن حمله‌ی آمریکا از هر وقت دیگه‌ای نزدیکتره.
آمریکا هم از طریق سفارت خونه‌هاش به مردمش تو خاورمیانه هشدارهایی داده که اینم یه نشونه بزرگه برای حمله مگه اینکه ایران همه رو سوپرایز کنه و برگرده به مذاکره.
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/69391" target="_blank">📅 22:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69390">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">⏺
🇮🇷
نیروی هوایی جمهوری اسلامی هم از دیروز تا الان مشغول آماده‌سازی خودشه تا در صورت نیاز، بعضی از اهداف تو خاورمیانه رو هدف قرار بده:
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/69390" target="_blank">📅 22:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69389">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nL1s92kvkA5Ptg-lylyZx5__Mo7O17Irqtw4F6yl3sYC4-4itjPzYzkzm_f9qgtD8vphPSL1qjbwVRw2w78h1gU9kQeJPnh55m_-cqjzrNJs4FWuVZJouhR0XsBRlJLk9TCVoAHyzcjZPpG-kAwlWSse21szA5h5cFOuNj8E4pknqDTbBrV3eJp03RsJnbVEe7uEyCDnmM6Dve4QIlDkNfObLStiF3FrtAMbhDUv6GTT9f1eixWnPtwQ0tBH5Cp5E1t2K9aALWOt4aWE0q9ddIWqF5K_c_AwoVsvueuqKS3X17hfma2O9vlSbQEhEl8y8KhBij02v7jh-YJyEdm1fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:
ترامپ در حال نابود کردن ارزش پول ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/69389" target="_blank">📅 21:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69388">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBBG_1qdu4hhrIBRNVCQnJTRjZEjl8F5O5p6_XQrCz1KHkgPCORrFPRlogjcgNG26571ZISY1G-Z4Uzxnhp-tmqHL9lqat4tH23g3-D1gfI_hp6U74IGthxTYDMFBNgB1kbwSFbs4u037gjYAav3ymLUa1TXQc7Kvl0rWFmt5VslC2_PBCxCxlxoBsIBeS1nlP4Ii0EbvR8IPj6yT7pFFqcXtg1mFBKqQ67QcUzOyNSZIaS5C7cYuXL0pCDNFeK7-OiT18pyidzY_9KIw1iXGnWJJdOtL4JfDGIUS_YQufrtxO_glvzd0Fyyvg-kinUjBdk1n82v3CIa1ihA_fDFtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/69388" target="_blank">📅 21:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69384">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iP0Aa7lfHfh0mFUo_MGLEjZ6T4hzHIksQTI-g_XVrB-V4mmKZYHO5K6UyBjovAt7zkvVLPgs2y4QApzfRaf30jY3usRIc6gbSccWs6Pxtl_MfPJw4PTD9TjAhjP9FvHk7RrRNBensqGYaqgcoP3T2CNB0QWBnyUtM_CNiLiqduG_CCHIAis-DDUvtJnvyt9QwismU2u42z9w_BPnBXTw9QfgUgHRVi0RIQZwaPqZFPSzS2BVKHi-UMV3UdbJmMnqhmwKLt4pjo7ek_r6N1UhcgOozDHbaENP9OzxzvnwBwgwYcSZClRvgJfOWVG_GFkQxFh27VulQljkLUiH6YFdkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eQcLTr4IY-wbLnRXz2_hrXQNgXq2n3BHrOCHgaj3eVVBcr9v-TLvnjj1pvgMQWyfpq-7LZ3lM5kJXrfYcYfzkE0RfAR3pVONgyUKMMZN8cVXMPqfHJ-qvLsgw3l0BhS9M_QPqIN4c3-0GMXNqlk9oi2jpkRIOzOIVkwbWpDYCbCrX5sJTF-PhtLejDQkmvi6wOQMTFW_dwdDHETz_-OIxoIvQgXJIP3zqTvFovngyfg0YQdnHBMVewyHDaTaBwUylr9hvev7STj0gMb18Ir5u4A_CZ8elSFAvFwHbgaXm8EmOGhnn9FoJsXIjZX4eGjtlVsglt62RFkP1J1GUzWu7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MR_aTOIOg2pBNpZ94ARLKL-5qCGW4iYBU8Hflza1sp4UO8gYk1cSSEbIUDRpFRmK_pfGiyvOxB3BQ4jdMBbcZK_f4MvlNrVqAF6xcftwzfZn7XDputhXCdsNkK1UBDdILNctsBlTAmQwRP2Qbu_wBJkWbIwrZqI1vqcxmWA6eSw_24VYSJYX0kf5B5Ct4KtgYwnjMvoWHCyyewqMBtmc-amWMyDN8qotExyRGbrLKKnxo2oohC-XY0AQoIDXSiU6ZIZSDTzTJvnPbqutECE4iPTyHX-8Umo9I7yopTM08xzr4fUkoOcRu8n6vnCQqFbQr0pyXMdpNUTaRyi_BoKv_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y7otGrCrbcsOxhQXEY-yoWBHhVl-Oo5pjxzGYP0aCvsMsXigRo_3Uba4gh29ohBIX30hxIzHM74q5CmBB5Yhc9XXKql1TX1NCbvyQRwKybxxZ-_GaSFlSG2lE1fnboGCc5-zwNBOSH_QnJK6T6zeFDquPsWSy0KTOi7k4TwApiEU8WxM8fqt8Ut02U_jARXsOKfiQi_59QRJTJlfKrer4Hfl8RUuPbwQNm8aclg5x6hVxyK7xYJfoaz6RZRmeKYR0d3ZAm-VG4LGxrpxktMdoH-JPUzrwTHFk701SLL0duRG3VKnNefWYzqOImiEMkihsyDYtMCgYMnXlvAi7If2Qg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
پست های جدید ترامپ
از تصاحب گرینلند تا جنگنده و انهدام ۱۵۹ شناور جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/69384" target="_blank">📅 21:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69383">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJM17yeNfuzPfEYWxUDhjbIE8J7UYie4CvB7XX4lSQEd07TOz0apHJtAq0JexZWe7wPrCulq5V4TTutSe60zyz4Ia6OzgZfCcrofAZHH4jCiZCtee40LMKAc_vIvZxq-T27iPLYREG98B_aKOvY_H9BL-p2_4gRYd-ImWk8oz9-H8G1W7WXkizXfQEwIhmlCjmDwgvMnuc-SGalEdujEjEptu6HJ4VkJb8LhZMZVkTYmBQQx3YVwcPWzBhQTlLfi2Ce-ClxLZYLoPsIZ03A3sDjx0KPKARJ_xzgm7nWATiEk8fKrdHUdGYbZ8-uHQVPC61wMmN2aOqACyz99QE5JOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پست جدید ترامپ در تروث سوشال
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/69383" target="_blank">📅 21:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69382">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRrOuXpU1bwhvctyNWSCxmbU4h1rVkuw1j6Zwm4PvD9LuvtbUBvSX5Z4hRxhwvpjJMoczksfuKNIVcwrz5imunB3T4OExdUCh2ZdOVOXEaOk9YmmoUPA8Y21xpuLegX_F_4RnjDF1BUU03cljF7Gs4V9rVJcJ7fETteTBNSWD_f1rvA8hG7TsjLBEXI8ym6hPK48f-7PYPLIPYDFqEp-tkN6QtJOHhq1DQs0X7PyfME1z6CTaBSUCsZ3zijkOyCegdbPvXzsqymH9afE5gijAfdkDZ5xCAskfmZz-HYBnLezBUCJQmPet51enicbpsr7cYCeAW5_4TUuqtrAzVgzVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مرندی:
بر اساس اظهارات رژیم ترامپ، کاملاً محتمل به نظر می‌رسد که پس از ماه‌ها تهدیدهای وحشیانه، امشب آخرین شبِ وضعیت عادی در قطر، عربستان سعودی، کویت، بحرین، امارات و احتمالاً عمان باشد.
اگر حملاتی علیه زیرساخت‌های غیرنظامی ایران صورت گیرد، زیرساخت‌های حیاتی این رژیم‌های همدست — به همراه زیرساخت‌های رژیم صهیونیستی و شاید اردن — ویران خواهد شد.
مردم ساکن در قلمرو این رژیم‌ها باید فوراً برای تخلیه آماده شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/69382" target="_blank">📅 21:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69381">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
کانال ۱۲ اسرائیل:
این کشور در بالاترین سطح آماده‌باش قرار گرفته و مقامات ارشد سیاسی و امنیتی در طول تعطیلات آخر هفته مشغول رایزنی بوده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69381" target="_blank">📅 20:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69380">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqlMhXYaX_LA2mzQGRhTiaNSNtyG-_wEpiql07n5z7MRv-huyb-EfaZI27MPaMtGCM29lIQZokO_ugvybdbQ0LOX_nltHATK7nRcM2TiDuWRNLSrqi3rIJGAnGJRBup_WmODiZO6iPlZXtYtBgrU4lQ1HLDhtKzWF-dshcjd0ANF5dyLucmERabso7g0HMb6qcjEow9IKUeSYHZnPfI9O3mUtbF62zTL--OZ99LGVfxz9zZKZ8tEEpnRu0NJWJkwsxwUN462gZxXKLWFXkdbt0WhOP4FIdF_MEzytrb9PDMgvXutHBIOzA8mAwGo5fNVPDdTpVQBek2gsUdRSS-b-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
🇮🇱
کانال 12 اسرائیل:یک مقام اسرائیلی؛
«تنش‌ها به بالاترین حد خود رسیده است؛ ترامپ بیش از هر زمان دیگری به انجام حمله‌ای بزرگ علیه ایران نزدیک است.»
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/69380" target="_blank">📅 20:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69378">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/799177ea92.mp4?token=Zyoa9hxNrjUe8ItAajFf707Z52KxKmKgFSJ7ZbC4ouyowVlD6kPmzgA5RksMZwhsxYSXoX8tToWpC5uYNerWk0Py0MMuhOS141x7De-FLFfHRdr6j4Z4YV5GoHpOGLqp0EDGn1-7Q5O3k7i8FQbfGUuokkHsGMX3exdeFlP5w1qzRqPeA4pJZYb6lnNiQhyTyeyn-3CJMpcVbE3I-1L9ypSZeG0CVR_OX5DTCMe0D4tFlWvYbwYUnhzZvjuCGI-QBr2Ic2NogO2i_kVdbz8Sm7-gVmEwzra6qwzuppA1mC0CZBDrcZTM3cEyLYYpB3GWQbWb9E-WmJOhC_YB2wse3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/799177ea92.mp4?token=Zyoa9hxNrjUe8ItAajFf707Z52KxKmKgFSJ7ZbC4ouyowVlD6kPmzgA5RksMZwhsxYSXoX8tToWpC5uYNerWk0Py0MMuhOS141x7De-FLFfHRdr6j4Z4YV5GoHpOGLqp0EDGn1-7Q5O3k7i8FQbfGUuokkHsGMX3exdeFlP5w1qzRqPeA4pJZYb6lnNiQhyTyeyn-3CJMpcVbE3I-1L9ypSZeG0CVR_OX5DTCMe0D4tFlWvYbwYUnhzZvjuCGI-QBr2Ic2NogO2i_kVdbz8Sm7-gVmEwzra6qwzuppA1mC0CZBDrcZTM3cEyLYYpB3GWQbWb9E-WmJOhC_YB2wse3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تخلیه پایگاه های هوایی آمریکا در بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/69378" target="_blank">📅 20:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69377">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/483837b794.mp4?token=c_X3BfL5ocGbQ2b8F5v-9cUN-o6gQhD2D355kv-DnSbSfUhJJTIAZp2x27qv8ott8WMau7BxUghhgiqKSKpl5u28vhx6fL82utFWPBRooojY9OENv3CBCiu9ngQJtyJUJVEUOgBtQWE8kNpGXi6vADRL0MpnGbMM1vfW0G50SJxkEZKm0gCt2Gc5Gu8BAX6a_NnvJH17MupqJl3IOfUWzF0BWfyDwLPk-T8giJUFd1wVaWZFqw4j8FbBZGsRbY0H-y3f0bYSsY1fvrd8RSYtnViYmc3sO3FEi_3_kEYtpf9puhmkOs96sALM7SwTrqld1H3kxIrn2n7ZZaw0fc4dRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/483837b794.mp4?token=c_X3BfL5ocGbQ2b8F5v-9cUN-o6gQhD2D355kv-DnSbSfUhJJTIAZp2x27qv8ott8WMau7BxUghhgiqKSKpl5u28vhx6fL82utFWPBRooojY9OENv3CBCiu9ngQJtyJUJVEUOgBtQWE8kNpGXi6vADRL0MpnGbMM1vfW0G50SJxkEZKm0gCt2Gc5Gu8BAX6a_NnvJH17MupqJl3IOfUWzF0BWfyDwLPk-T8giJUFd1wVaWZFqw4j8FbBZGsRbY0H-y3f0bYSsY1fvrd8RSYtnViYmc3sO3FEi_3_kEYtpf9puhmkOs96sALM7SwTrqld1H3kxIrn2n7ZZaw0fc4dRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کاخ سفید:خداوند سربازان مارا حفظ کند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69377" target="_blank">📅 19:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69376">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c746862829.mp4?token=km0NljHbF8p14YUjAlIgxo5IMYr3EuAA2LDohLfegIqLqe4eQvR3KziUdHoxuK7gCqFV5Ud8lc0ia3HMD_yz2EuL2q3e2lwZMZ0BB4cvxCWvnDUZT74Qxam5-bG2lb2SQGMbwLGesNbjWyLorA-LKqhoCJrdP6FCCvEpgRwYR11nMX2HyInkr_fSFTyMyP-s5TbqYyKmTOobOj9vgceAx7NBgJstfxPOgHWE3RJZ2aq7uuiZS1HAPXKjSfY8Lo6v3v2-CmFpu3xztPwYAkkS4x04GOcOMKYYZamA9Xiyt0Y-Ybh--YbM6b3CigXMy4yDHbQ2srXusGJldnPqy2lJznel4Gx306TH7RQjMei7fUFz73hvejbFzGOtGwFhMuLkR_4tSVOxGF8GQME3mSqfNEETNQQxq7bo4soD3iA_MfnTUW3kzhtce8IW9yhkXHpu59oK5k_ZZ-RA4zFoqmflmIB4CapF_EfqdhufCjFQAYrrI9zzP3_tlbMyjT9vwHpAg5y4S8fjj0IjmowXIpgSyCVq_H-YM_kboIy8TrSOSmEaL0_mUPGhIUUkGiG6LEJ-Vq6Xl81peaKv0UuuM9qQCujalg8L2sKMHX_-14QZ2v-RvHNuZWoxdvqy902qsam4598MogBW3WiVl5QjdTywiBwZ4tZEi5xCMzhklzv-4WY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c746862829.mp4?token=km0NljHbF8p14YUjAlIgxo5IMYr3EuAA2LDohLfegIqLqe4eQvR3KziUdHoxuK7gCqFV5Ud8lc0ia3HMD_yz2EuL2q3e2lwZMZ0BB4cvxCWvnDUZT74Qxam5-bG2lb2SQGMbwLGesNbjWyLorA-LKqhoCJrdP6FCCvEpgRwYR11nMX2HyInkr_fSFTyMyP-s5TbqYyKmTOobOj9vgceAx7NBgJstfxPOgHWE3RJZ2aq7uuiZS1HAPXKjSfY8Lo6v3v2-CmFpu3xztPwYAkkS4x04GOcOMKYYZamA9Xiyt0Y-Ybh--YbM6b3CigXMy4yDHbQ2srXusGJldnPqy2lJznel4Gx306TH7RQjMei7fUFz73hvejbFzGOtGwFhMuLkR_4tSVOxGF8GQME3mSqfNEETNQQxq7bo4soD3iA_MfnTUW3kzhtce8IW9yhkXHpu59oK5k_ZZ-RA4zFoqmflmIB4CapF_EfqdhufCjFQAYrrI9zzP3_tlbMyjT9vwHpAg5y4S8fjj0IjmowXIpgSyCVq_H-YM_kboIy8TrSOSmEaL0_mUPGhIUUkGiG6LEJ-Vq6Xl81peaKv0UuuM9qQCujalg8L2sKMHX_-14QZ2v-RvHNuZWoxdvqy902qsam4598MogBW3WiVl5QjdTywiBwZ4tZEi5xCMzhklzv-4WY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیستون؛
جایی که سنگ،
به زبان تاریخ سخن می‌گوید.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/69376" target="_blank">📅 19:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69375">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2b275487f.mp4?token=R_YOXNtR5wfhaNV86wfRkXXxhRXQ6QTM17KIGc2OPCJ92b1UTjjvIio5xTNtgps3EV_qGBa4avDap5v6fqtYXhOARvoDJcyFKC-dQk4jl1EkmdMuWTk6rIQHSfJ6Ed3Au2PPvLbKGAJ_WXPKuLc2-88xYrNvfZDbHLRUTuSrPOg0vu2D-wq1uewmQTHROaINrATOS0-Nu3iiemtYlcBD3c0TT7r8XjHBQfJksBmnpF3xLBoTlGW7bT8V717LbneMNgEKtDx48k9WfTombTpTOiNtrxGj_W8KPzYwA-dVtH6yIj8LvTSQxrgYBuCyjxBlD1kZLH0HL_ugrbWl0BsAFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2b275487f.mp4?token=R_YOXNtR5wfhaNV86wfRkXXxhRXQ6QTM17KIGc2OPCJ92b1UTjjvIio5xTNtgps3EV_qGBa4avDap5v6fqtYXhOARvoDJcyFKC-dQk4jl1EkmdMuWTk6rIQHSfJ6Ed3Au2PPvLbKGAJ_WXPKuLc2-88xYrNvfZDbHLRUTuSrPOg0vu2D-wq1uewmQTHROaINrATOS0-Nu3iiemtYlcBD3c0TT7r8XjHBQfJksBmnpF3xLBoTlGW7bT8V717LbneMNgEKtDx48k9WfTombTpTOiNtrxGj_W8KPzYwA-dVtH6yIj8LvTSQxrgYBuCyjxBlD1kZLH0HL_ugrbWl0BsAFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇷🇺
دونالد ترامپ، رئیس‌جمهور آمریکا، و ولادیمیر پوتین، رئیس‌جمهور روسیه، در قالب «زوج در حال بوسه» در رژه کانال‌های آمستردام:
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/69375" target="_blank">📅 18:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69374">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f4517b5c3.mp4?token=mcC25WNjfPpe3mFYw0muWlLVsSB0vrKpW-YRQPiZ5QQbbQqNzhf7jPx-xrI-ZBCBDrqzBfxZmTHbpdGNyRhz-M6uuWl8R9cG5fb4jR2mEc1t2Hx2v2iTJdcBBC3XbbPVblnmHegpjQ_R8e7FGRLDRUy7A99i7o3abFXj2uZKqcHnTalpI_fGKk8zdchHUPeiaEutMU3ENc_epEPndef9VR2iNt7LKWq8bpSKkY66F4e5X86RQ2Ta-_CdTPd0o_yUJ4YaN2Lm-jnM7wHMXvvOmozGzKSq6t1-9pt_s9A8MgpMezmOezyr1YuJutrPzoZd37z4oqCzlMg5BJm_wAdLIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f4517b5c3.mp4?token=mcC25WNjfPpe3mFYw0muWlLVsSB0vrKpW-YRQPiZ5QQbbQqNzhf7jPx-xrI-ZBCBDrqzBfxZmTHbpdGNyRhz-M6uuWl8R9cG5fb4jR2mEc1t2Hx2v2iTJdcBBC3XbbPVblnmHegpjQ_R8e7FGRLDRUy7A99i7o3abFXj2uZKqcHnTalpI_fGKk8zdchHUPeiaEutMU3ENc_epEPndef9VR2iNt7LKWq8bpSKkY66F4e5X86RQ2Ta-_CdTPd0o_yUJ4YaN2Lm-jnM7wHMXvvOmozGzKSq6t1-9pt_s9A8MgpMezmOezyr1YuJutrPzoZd37z4oqCzlMg5BJm_wAdLIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
فاکس نیوز:
رئیس‌جمهور ترامپ در حال تشدید فشارها بر ایران است و می‌گوید در صورتی که مذاکرات دیپلماتیک به نتیجه نرسد، انجام حملات نظامی جدید همچنان یکی از گزینه‌های روی میز است.
ترامپ پس از دیدار با اعضای کابینه خود در «کمپ دیوید» اظهار داشت که توان نظامی ایران به‌طور قابل‌توجهی تضعیف شده، اما این کشور همچنان از برخی قابلیت‌های موشکی برخوردار است.
مقامات آمریکایی می‌گویند این حملات ممکن است حتی در همین آخر هفته انجام شود؛ در مقابل، ایران اعلام کرده است که در صورت هدف قرار گرفتن زیرساخت‌های حیاتی‌اش توسط آمریکا یا اسرائیل، آماده پاسخگویی است.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/69374" target="_blank">📅 18:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69373">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f0734246c.mp4?token=ssT2f86cldWalfTpnlFTm4jcsOzg5RYsgxm1DgNsGRNWFk2qWXlhnkBULskYPPRei1Msb-WTnDMgFNudTJUVpXwAlj5m0SYWXvSiBM1MCbAsaHTMUoOur5HCJ-vkZsvMdJ-DuzmCHO1wtDXRIBxxTb3OUvAx8oQWX4R3_Tk7DwfuFYEQjJ0vd-metaFaJvPgLz2ABqvOFzbelEPRQUFCoPYanE0BH882zJFg71M-WjdnxNaBPkJYlCHFFqi_AUEZrrONWFVdwQdYj3NaWv3vQtsPunKt6Ha6_srRQ0bTVkgwKINoLint3Rf3OHRRF5q588Anq-AwaVg8Jgufqyslgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f0734246c.mp4?token=ssT2f86cldWalfTpnlFTm4jcsOzg5RYsgxm1DgNsGRNWFk2qWXlhnkBULskYPPRei1Msb-WTnDMgFNudTJUVpXwAlj5m0SYWXvSiBM1MCbAsaHTMUoOur5HCJ-vkZsvMdJ-DuzmCHO1wtDXRIBxxTb3OUvAx8oQWX4R3_Tk7DwfuFYEQjJ0vd-metaFaJvPgLz2ABqvOFzbelEPRQUFCoPYanE0BH882zJFg71M-WjdnxNaBPkJYlCHFFqi_AUEZrrONWFVdwQdYj3NaWv3vQtsPunKt6Ha6_srRQ0bTVkgwKINoLint3Rf3OHRRF5q588Anq-AwaVg8Jgufqyslgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک هواپیمای سبک قاچاقچیان کلمبیایی در حال فرار از رهگیری توسط جت جنگنده ونزوئلایی.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69373" target="_blank">📅 18:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69372">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f45020b76.mp4?token=THLCWQM79ZxNrfw7RzWz96Y4rwNzr8EpZSTFPhJPWrRfJC9maZYQ8MmN7vPZMDBgjoD-9If6U5izPKSgHEeceUgQZfQDERzeq2ZsUvFpanNceZpznoI93yIH7FetrLikmcwtew-PxT8fBlHyeBE1fLRRte-jhjcutUQ2ZAqWGLjUdYnL0EZ2mVBUizqV-osEMkyvA7BefaOwOjQZkYqL23iGl6tIBPVHFcnCP8QK34lYCoTm8oY3W5GN1YuVJXwrUQY2HZkdliaXWCVfAemcU2H1K5LqhpTNgmNpHEflp2bXt01esHz5ubjuurIML-D6J2FyOBNC0EoZrtyCM4auzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f45020b76.mp4?token=THLCWQM79ZxNrfw7RzWz96Y4rwNzr8EpZSTFPhJPWrRfJC9maZYQ8MmN7vPZMDBgjoD-9If6U5izPKSgHEeceUgQZfQDERzeq2ZsUvFpanNceZpznoI93yIH7FetrLikmcwtew-PxT8fBlHyeBE1fLRRte-jhjcutUQ2ZAqWGLjUdYnL0EZ2mVBUizqV-osEMkyvA7BefaOwOjQZkYqL23iGl6tIBPVHFcnCP8QK34lYCoTm8oY3W5GN1YuVJXwrUQY2HZkdliaXWCVfAemcU2H1K5LqhpTNgmNpHEflp2bXt01esHz5ubjuurIML-D6J2FyOBNC0EoZrtyCM4auzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز صبح تو یکی از حوزه‌های امتحانات نهاییِ اردبيل، 9 تا از بچه‌ها مونده بودن پشت در و داشتن گریه می‌کردن؛
طبق ادعای خودِ دانش‌آموزا، مسئول حوزه ساعت 07:03 در ورودی رو بسته!
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/69372" target="_blank">📅 17:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69371">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
ویدیو وایرال شده از این هموطنمون که در زمان شاه حضور داشته :
زمان شاه به دانشجو هایی که میومدن اینجا درس بخونن ماهی 400 دلار حقوق میداد
اون زمان صدتا نارنگی یک دلار بود
یه اپارتمان سه خوابه تو نیویورک میگرفتیم با سه تا توالت و حمام اجاره اش 210 دلار بود ما ماهی 400 دلار اونوقت حقوق میگرفتیم از شاه
شورلت کامارو یکی از ماشین های اسطوره ای امریکا بود سه هزار و صد دلار
با یک سال تونستم ماشینو بخورم
امریکایی ها میگفتن کجایی هستی میگفتم ایرانی همشون میگفتن شاه شاه شاه
کدوم شاه شما دیدید بیاد تو امریکا براش با کلی عزت مراسم بگیرن که برای شاه ما گرفتن
چه افتخار و عزتی و لوکی بود شاه واقعا نوع بیانش و لباس پوشیدنش هرچیزی نگاه میکردی لذت میبردی
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/69371" target="_blank">📅 16:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69370">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jE9fLWH6pOFQDtAWaRrlGBSZHeflZZk9HVBfdCAbeoMNCA_hEe_mdk8qPJHRWjAbTJ8vpNSxDKD47MPHHSYvBxB_rm6kSaZ4nWGlLy35_g8U1kXkBurxq5yNDCHl87VZ-00lA7WBgyffGYYb2xmopWLPcqNE_11r3kjdTJLqRn5TSbQZowJKf5R5uf3beCl7xbXEAPBgDnnGlW9qyJYgR2pSjP1-cOlm57o2S36hgeJwdip_DO_HV-hU8dNnZ3Yng5NL3AWtKAZ8YjYtqm-S8DK_oPghQRoh5oeEgQqWmrKiTai7jBEprtKH2vOzigB0SyGluDkVNMhrovR8fi1UpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سفارت آمریکا در مصر هم برای شهروندان آمریکایی هشدار صادر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69370" target="_blank">📅 16:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69369">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46327b1ae3.mp4?token=I0WVpleK8FhuxlwBYV3jnDSbd3zr6pAhciMpRuLs8dJCHjJT-hdPSrPJTOaWCVIAH1AWOTkuo1d4-_uf1aHCisCiptLRmOoiOrQ6UAutglBeX1Rl5RhVCIY8AyWb_Vkp1mGudCMGa3lqX4aCmlvHHJ5rw1EG2sOD7vSFaL8FLRBx3L4l9JBoIp-UzMPuqQeNVFgLX5hBEU7lBhrcyXXqEFrSSbE_j-okh65N0gSMY2zz9ZUtP9tSHKfVMq3YlsMjREXeHwqGYlf6LAsqEJAKuQhXiOWcTFyw04iIchKff_GE9cKMAYvCmdIu3gcqagM4ogSOe7_sss1L5pHR29Ioxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46327b1ae3.mp4?token=I0WVpleK8FhuxlwBYV3jnDSbd3zr6pAhciMpRuLs8dJCHjJT-hdPSrPJTOaWCVIAH1AWOTkuo1d4-_uf1aHCisCiptLRmOoiOrQ6UAutglBeX1Rl5RhVCIY8AyWb_Vkp1mGudCMGa3lqX4aCmlvHHJ5rw1EG2sOD7vSFaL8FLRBx3L4l9JBoIp-UzMPuqQeNVFgLX5hBEU7lBhrcyXXqEFrSSbE_j-okh65N0gSMY2zz9ZUtP9tSHKfVMq3YlsMjREXeHwqGYlf6LAsqEJAKuQhXiOWcTFyw04iIchKff_GE9cKMAYvCmdIu3gcqagM4ogSOe7_sss1L5pHR29Ioxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پیرزن ایرانی توی مراسم اربعین، برای اینکه از یه زن عراقی صندلی‌شو بگیره، بهش حمله‌ور شد
😔
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69369" target="_blank">📅 16:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69368">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">حالا ما کجا بریم
😐
#hjAly‌</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69368" target="_blank">📅 15:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69363">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eh3fX4vDRDMJLy6yTLWL-2smCQh__1TilPtaFOYeHh9rEcPOh6E9YD6A_5pcLwe6WsKRxx85VTZ2muu3M53ecf_zhbahSIxDlWPjDeUU3kZAMDgfSJPjIFezAsTYSBCURHgB7eJCkZJkar2YTpIkVh4yQQHCOHPMmQr0A0UxXfQH6EKbwjLFLgSH_B3hjfGahvWDi-1isXdHD6IlcCr2KJlhqbhGXrUAV-BjWJlXpGuPyw2XtRUEotx6GRNgY6U1_XqQrbxbL1ox2p9IQY2-Uejq1zgFlBp7SfhAKORO4-cEF1XhuHVwK4cZx2eFNRf2uxZpl-T2IakeaTsL2QjQ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NBQR8FinZQPg_rF83P-491OUCBhjH4gWDgSw0nxtVCLy336gvZ8vmcb4Bl5l3TofbdIicjwxwuTUsgf6Ho8hwF-PwVxPm5Tp7eqqHS_hU8AlCVLyPyGZ4g5RTi8iRRiItLB5ke5q1SBdKxQ1kxzqgDsKIs31LIyZLL_VK0Ellc7jkTSqxKOcZ930ie_3jk97U_EKQFelsatVsY7Z1TJpulDOlu4ui44wAGYvv5J2O5agnazyYUMCfT1FtZcEFOrxHvMWYXVNVo3AqYQ76V8FfZgB4zWNiDbnubyE9ymRtoM42ZDAAGtL0o75WWoj_VQK1V3NiFVL4z8eoZoRpKsxsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LzPDK1d78ZZrNveDda3ibRqfh7XAgfgc4SHhHbyw3iwYn5diBasuWFCqOzlmT-NzWOLFZMu7YgqueKGGKTfKp5u9Z113lCUsTw5h6NvjsFUsNjLzy5eM3niN60frbq4zXaL4EB8SdCZJBMQJXzbdqvUMhU49CUIzCzcyP2XGW6P8UCwQh0YSO246C6flJ44Dw5h1xvxV3zwdZSMpyHi6P6F0sKpj6dp7MKflBeLqNIBGvGej9OvmgtkxWXb172G71DGIe_-M2CNR-I-kyfNPdXxWkZJ-7xJTEpt3ye2z9XFl1HeNthcswPd6CoThmLeYB7kfGEaxVfVoh9MShysgcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FdyGZEQu2mAS4NnT3tL_aBrONKD8G3ZGd67v5Je3jTQ0lz4DQ9iNyq6UGTnEVU2F__dVUgdjfVL6V0bPFhiKoa9PVBfi3_A2pa2CEMV5PCUKq5Tc7XPMJfoHQL-0K-PrOIyt3rCEG67_J-zdOZQe-gOGluziWzkMvfGzMPBlNJhCu0p9kZukAHJZoEtm-HcNtn514ZKd__xLwqxNATn77Uprzbwl4OUf3bI04JG30jG-k_E3LvWy4zg2kVxnn-Eyg5_-pk30jakyPx4xFGp1rUz8oNnvnk0-JE6iDFYCU-12dEF5ldRsZf57jwwhFl4BP4kQWp0lZxpMMtwmBzRqRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h6INcOXs1TVlfivwevXR6a17Qy0KDutBfl2IwMx253wiS6_8q8Y5U-Txv7oCgrMhQme_-SZkNMDdfNmY3C1xOd3erTcOTolH8e6j4JwrnEOa3zTzBgZfek_MSBmFXFgZzHTh-4sac5d25ufV3XGGHKSxkQkQAUpSsUL3Tel8CaQoAQjlJ0UGhNYZoat8FXUnaqi8SHPbt-Np672cUz61mtDvtsLxwEiOfA66a-Q6_vXdPyjI92t5xHl4piMnZh3nrDdUOZUqdgxZOEdxkUp7Gz0r3Cn2t_NHWwnYKH3bZmt_RrzU_H0C2wm9F9CUCHgOGWvuy-d-E2jqPS9LNZ1MFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
سفارتخانه‌های آمریکا در خاورمیانه یکی پس از دیگری درحال صدور هشدار به شهروندان خود هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69363" target="_blank">📅 15:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69362">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2be758c5d3.mp4?token=J0z7sLuSHzZ23TFekn92ykk3ENt6J-X9e1SvMyYoSL-HXpW-U-bf9mLNyg1Decxfz9ZCE11wRaIBT6UwOKzXUFYOo-DiSWWda0Y-C0eun8tUor9XdsXuseZhvzFL7tI8hdQHsktNrBarQtI7Pt_KJVDtzWLsuU2ku7xE5-AZD5eP_MoT06t1XGJXuViJ6f6bxCH5KO9i2uqAUDWTpDohRzb9A9ogW5OetxYpWA4rkX6ZjOE5n6feHVy2G1ygP6UFN_ezYSlrl2B-sisGynewIOe0pt497B7l2qBAdKY1X6r49fMpX0ywYd9rpyUsWzX8KpDrNy9N7lE-ZXl_ihQRGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2be758c5d3.mp4?token=J0z7sLuSHzZ23TFekn92ykk3ENt6J-X9e1SvMyYoSL-HXpW-U-bf9mLNyg1Decxfz9ZCE11wRaIBT6UwOKzXUFYOo-DiSWWda0Y-C0eun8tUor9XdsXuseZhvzFL7tI8hdQHsktNrBarQtI7Pt_KJVDtzWLsuU2ku7xE5-AZD5eP_MoT06t1XGJXuViJ6f6bxCH5KO9i2uqAUDWTpDohRzb9A9ogW5OetxYpWA4rkX6ZjOE5n6feHVy2G1ygP6UFN_ezYSlrl2B-sisGynewIOe0pt497B7l2qBAdKY1X6r49fMpX0ywYd9rpyUsWzX8KpDrNy9N7lE-ZXl_ihQRGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
زنده‌یاد مانوک خدابخشیان: دو شعاری که کار این رژیم را تمام کرد؛
رضاشاه، روحت شاد.
اصلاح طلب اصولگرا دیگه تمومه ماجرا.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69362" target="_blank">📅 15:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69360">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mgRQT5wDNrXjKSbjYWJligr8Y94xlyMvdtk_8DErBD4iMWcYDSx3rrUocYITrvJScfqoHBYv3GLD65OfB0JQBRIli8TpEkGfoLN-z8JTPMMdk1uIQKsyOU57gwijWMdjGU-exWHH7rfR4SzHNVpYItNUqb0kVaJyO5GXOBNXML27DNZJv5yp4OQ9qAJWPznfUOtb0xwhNpCOSJAT-ygTPnOgQ9reTdzMzuMIKYQSrJ7wACxWO0YKAavhyoC1krJOi1-FxophYg4B6pLnj0p9FUjDRyaB13CF73O5AOOvuFGKfbibZXdTe0IDtx9NqrxkN3D7RD08dn--EqXM-paMEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G_dyHqVFbzlAhCW9qC6bLeHjS_1dIPa4DH_BaaTYBGsqNKrcBWipWFWz7lDHK1uREA84ElSyN4EHmQ9scU9s4C5iaJs_Zu0G02Ja_moEAwEeRFJ--ePMO7NPAhniL1RE2Z-vLznvERf6r8HGEFnqWNx5x34zD4bd8hG6MEm4u-lyVzXxvi3ZzCHL8qsajtVIGVmL9hg1VNFHxCTENVPmSAgIgTVFV7BJP8lBbdP6kFl6wMBkWXv7z56rP7Oft8_38ShP2hNJXiPYgRrOONwS7XocW8Vj8BfG_KqojCRofNYwMVVLlN--A7lVKpWB8zpj6DmNsv-ou9IPAvH1toKIXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
سفارت آمریکا در اسرائیل و عراق:
آمریکایی‌های حاضر در منطقه باید آماده باشند و در صورت تشدید تنش، خروج از منطقه را در نظر بگیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69360" target="_blank">📅 14:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69359">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bz4SiBeuFip66tG-OMYnXwo44le9Vwu22SxgprTP-et7LAUIGMR9kIir3J25MvRZyqJdfzzN5Qi0psPkRoniGE1RBBguqrAqaq_WBMRktVOGbNUcW_az-BaYfN2mu7eTthunjhdzRQyn9EfzGIaRmoV_uyFBXADFgaOFFS5jkEkG6iJ-B3gycrow3mvvR3uO0juIZwNyQqn4i6TQtw5wfnks_22t3wzcyY66OgZ7nkbFWerkLGaJ2tAyza7Ucfwgr3wp8HZfO69PlCXpTe2UESYNuoWRXRhEhe-5GkvkiMCtmk3GedwkjrnAlCXlLxjDQG4c1FTcafoHsjJS7aLAPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تسنیم:  بهمون حمله نشده، گلوله توپ زمان دفاع مقدس ۸ ساله منفجر شد.  @News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69359" target="_blank">📅 14:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69358">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
تسنیم:
بهمون حمله نشده، گلوله توپ زمان دفاع مقدس ۸ ساله منفجر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/69358" target="_blank">📅 14:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69357">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
دقایقی پیش از حوالی اسلام‌آباد غرب کرمانشاه، صدای چند انفجار شنیده شده.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69357" target="_blank">📅 14:13 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69356">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c794c22fb.mp4?token=uDuk4HziZ4Tz6cdkJJITPLRSZR0_y-0Xlhi7JuRICD7xoKvxKMKIuJkbZCkyLBmN6agttQfaV2LdHm6-A8gH_bw1hzKyFGs6qewheKs6ZivwXF2Wkijc-Nn67TweErcsBSw-juhqcPcIOYKItIQhwfqxdL80ufT_HuT8qfghxzoPzop67gZU-JJIvxZzasmrjHqxn26HdlPtCqjz40DMNOtiBwEbf5Ajjri0v7jlkJthA_YixAd8MjnuQkFcG83yb7-yxR52UkNxCZcfKGxRl4EM_05L8o9QSNY_-3ZSNqv9hdHCamuNpjDzLMn0tfsb8GpSEWRDgoYcXqiA6y8olw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c794c22fb.mp4?token=uDuk4HziZ4Tz6cdkJJITPLRSZR0_y-0Xlhi7JuRICD7xoKvxKMKIuJkbZCkyLBmN6agttQfaV2LdHm6-A8gH_bw1hzKyFGs6qewheKs6ZivwXF2Wkijc-Nn67TweErcsBSw-juhqcPcIOYKItIQhwfqxdL80ufT_HuT8qfghxzoPzop67gZU-JJIvxZzasmrjHqxn26HdlPtCqjz40DMNOtiBwEbf5Ajjri0v7jlkJthA_YixAd8MjnuQkFcG83yb7-yxR52UkNxCZcfKGxRl4EM_05L8o9QSNY_-3ZSNqv9hdHCamuNpjDzLMn0tfsb8GpSEWRDgoYcXqiA6y8olw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه جوون عرب داشت به زائرا میگفت بیاید آب انگور بخورید که یه ایرانی رسید و بهش گفت:
آب‌انگور نه، بگوآب‌شنگول
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/69356" target="_blank">📅 13:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69355">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/917485436c.mp4?token=FEOkF7gZuO8e_rhVzD4hp_Yi4tSK-VI2eVseVWC7DpjGTq3eWAco2U9UWPbONzB2TUXzFRYaDXRw4ji59epu_I1jJS3NxyQ1VNlPcC7bJkvRrgDqrw8GOWWyInlDXsaMf6P8FOF-WmIEB98d4A7lervTWwOlsIj3cwfO89sxDG7KuR5IRZ7-M68421MCMmL7tGtL7x_Av8Y-hLHCGgWRPaPO2Ds94Cdo_jWWjQlZy2YV8-IcE3004EBzuX80NihFdk2k9ckqk7gPHaMD6nS72ifAjggxxXfniVkuoG5uHnkoizRcAEk9QW2o2_wSUQSGMEx36qB0rWUwTVqUD0SNRJ_96tkQMBGsrsfvcSGy3wUM2CzzQG2ifjkFJCjZ2WVVmn4anLCqKkDwcbQBW2VpFQgYNWYIlKrdJLG2OYEGX_VaFUdeCEixOnY7hGFktL9G5HODfgBefl--uKC7aTWGgTkGwGGZ6HPVsDvrqjrryPKs48JsULjKnQg_wpO5qAb1x7IKEn9_cEM4HIWAsixJGBKgoR2WTf3j45esqHV4aGMWdG86beY2XyR0g5pwWjyj6mfuOE7Z9o7CaSyuRB7aEa5ypu2XxMBfrZ9ZInQpUBUOaZckMdonNWzfMWHt3BHlFP6yjGSNTEyqpoa1AaX5Da-VD9z-VFnkz--P8xQDcr0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/917485436c.mp4?token=FEOkF7gZuO8e_rhVzD4hp_Yi4tSK-VI2eVseVWC7DpjGTq3eWAco2U9UWPbONzB2TUXzFRYaDXRw4ji59epu_I1jJS3NxyQ1VNlPcC7bJkvRrgDqrw8GOWWyInlDXsaMf6P8FOF-WmIEB98d4A7lervTWwOlsIj3cwfO89sxDG7KuR5IRZ7-M68421MCMmL7tGtL7x_Av8Y-hLHCGgWRPaPO2Ds94Cdo_jWWjQlZy2YV8-IcE3004EBzuX80NihFdk2k9ckqk7gPHaMD6nS72ifAjggxxXfniVkuoG5uHnkoizRcAEk9QW2o2_wSUQSGMEx36qB0rWUwTVqUD0SNRJ_96tkQMBGsrsfvcSGy3wUM2CzzQG2ifjkFJCjZ2WVVmn4anLCqKkDwcbQBW2VpFQgYNWYIlKrdJLG2OYEGX_VaFUdeCEixOnY7hGFktL9G5HODfgBefl--uKC7aTWGgTkGwGGZ6HPVsDvrqjrryPKs48JsULjKnQg_wpO5qAb1x7IKEn9_cEM4HIWAsixJGBKgoR2WTf3j45esqHV4aGMWdG86beY2XyR0g5pwWjyj6mfuOE7Z9o7CaSyuRB7aEa5ypu2XxMBfrZ9ZInQpUBUOaZckMdonNWzfMWHt3BHlFP6yjGSNTEyqpoa1AaX5Da-VD9z-VFnkz--P8xQDcr0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
آتش‌سوزی در یکی از پالایشگاه‌های استان اربیل در اقلیم کردستان عراق
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69355" target="_blank">📅 13:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69354">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/532a951287.mp4?token=aqNQxIZn8qqI52meX3weeRolN44rtf-ffVN1710vghGa2buC7Z7klwwnEW-ZNnPbcuWDNVl_ddJLeTZI691aeXj-Ad_xtQCOW7kRHXr6r06g50_op_zC3QGRgFgC3Dx-U6nJUXGmUGEaa0k8hqWO0CFwbDXMoV4bJBfsXDq7BcL8KPa6Xfr8g5-TB22vKQFGUmU4XaPG98lxdkyd67SeDbJJ6oxyUazu3l7VieEb-Sm3mO09sQDBhswSjZ5pbMNWY4f-l-HVRi2rwhwJOuoVpaUvlKJ4Fygi8yfVVQgg_agnpTglbmCWP3x-nIb1iVrtgWRpz540hcjZKmbbtpntxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/532a951287.mp4?token=aqNQxIZn8qqI52meX3weeRolN44rtf-ffVN1710vghGa2buC7Z7klwwnEW-ZNnPbcuWDNVl_ddJLeTZI691aeXj-Ad_xtQCOW7kRHXr6r06g50_op_zC3QGRgFgC3Dx-U6nJUXGmUGEaa0k8hqWO0CFwbDXMoV4bJBfsXDq7BcL8KPa6Xfr8g5-TB22vKQFGUmU4XaPG98lxdkyd67SeDbJJ6oxyUazu3l7VieEb-Sm3mO09sQDBhswSjZ5pbMNWY4f-l-HVRi2rwhwJOuoVpaUvlKJ4Fygi8yfVVQgg_agnpTglbmCWP3x-nIb1iVrtgWRpz540hcjZKmbbtpntxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه لیلی فیلیپس پورن استار معروف که تو 24 ساعت با 2 هزار نفر سکس کرده بود!
دوس پسر لیلی: من اصلا از این موضوع ناراحت نیستم، چون اون واقعا زحمت می‌کشه.
مهم اینه که آخر شبا میاد پیش من، و اینکه من بوسیدن رو براش ممنوع کردم، اگه با بقیه سکس کنه مشکلی نداره، ولی فقط باید منو بوس کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/69354" target="_blank">📅 13:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69353">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d26851041.mp4?token=oePVWugGZ4dxMJ_85LDfODA2yQQR5yX2VtmIUJXLQCnurt3Ortad1c4rTg4hTS21beTjTV5Il240U-ZhAUWDn40VW-_BOMdbPmvAw_1lNabCByT0LGzFBOtM_p6h2hjF0FJpmvIo72CWl3GLf2josBuYRxSiaeOaElhzcCOGvZ3Ekf4vkYtcKnP9hZj2EdY8cwdpzngBRirAP-mAIWrWqY_rtwGd18DEgdkAKmOfwvgxQ7ngSDcF6DllMNN9VYj1r494JaMogiGnYEw3WR5II0W2lzB9jb3podhm2dCjrzgjQuRoxPNCtv6j4uouwbW-Igf9f2Zz2QmtYfPEDo1Z5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d26851041.mp4?token=oePVWugGZ4dxMJ_85LDfODA2yQQR5yX2VtmIUJXLQCnurt3Ortad1c4rTg4hTS21beTjTV5Il240U-ZhAUWDn40VW-_BOMdbPmvAw_1lNabCByT0LGzFBOtM_p6h2hjF0FJpmvIo72CWl3GLf2josBuYRxSiaeOaElhzcCOGvZ3Ekf4vkYtcKnP9hZj2EdY8cwdpzngBRirAP-mAIWrWqY_rtwGd18DEgdkAKmOfwvgxQ7ngSDcF6DllMNN9VYj1r494JaMogiGnYEw3WR5II0W2lzB9jb3podhm2dCjrzgjQuRoxPNCtv6j4uouwbW-Igf9f2Zz2QmtYfPEDo1Z5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از عوارض خوردن ساندیس زیاد
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69353" target="_blank">📅 12:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69352">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e653ac6e6.mp4?token=BNe1uKx6bCyWZ4ar9S3OjP6zKZZUBM7MpoiiYYm6LzYqIPyQq68Vaoj_DwaTyV2iPY05BwHmRcf7IcNnPVJDoXY_asKPfeawpSdjxbLo-o4I6EBCaF3GcE3rkBtldsMpmvzYKmL05JuNu-TS1i3ls-X7CIAlXLXA7HMD1blhlY7HIILFAW7rDDftbWCTAoz6FfaLt6DLxGasp7xHa3-7huoyam_C1GhszJnveZQlEo2c-pWreMQ9J_ZeSaQrXDLM0uSspY0AiphnWLOx3Z7ujUGe9ze2oZdDCkN9aZlP3vtjCQgJjiIxG_U0tuXAPvTzSD6uhOXE3ZdvAFXP1cIOXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e653ac6e6.mp4?token=BNe1uKx6bCyWZ4ar9S3OjP6zKZZUBM7MpoiiYYm6LzYqIPyQq68Vaoj_DwaTyV2iPY05BwHmRcf7IcNnPVJDoXY_asKPfeawpSdjxbLo-o4I6EBCaF3GcE3rkBtldsMpmvzYKmL05JuNu-TS1i3ls-X7CIAlXLXA7HMD1blhlY7HIILFAW7rDDftbWCTAoz6FfaLt6DLxGasp7xHa3-7huoyam_C1GhszJnveZQlEo2c-pWreMQ9J_ZeSaQrXDLM0uSspY0AiphnWLOx3Z7ujUGe9ze2oZdDCkN9aZlP3vtjCQgJjiIxG_U0tuXAPvTzSD6uhOXE3ZdvAFXP1cIOXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف: میخواستیم خبر شهادت رهبر را ساعت ۸ صبح اعلام کنیم اما تلویزیون‌های خارجی، زودتر اعلام کردند
.
در روز نخست جنگ و تنها یک ساعت پس از بمباران بیت، شهادت رهبر قطعی شده بود.
تا همدیگر را پیدا کنیم و هماهنگ شویم، ساعت ۸ شب شده بود.
قرار شد خبر را فردا ساعت ۸ صبح اعلام کنیم و از مردم بخواهیم به خیابان بیایند. اما تلویزیون‌های خارجی، [ منظور اعلام رسمی ترامپ]  خبر را ساعت ۹ و نیم شب اعلام کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69352" target="_blank">📅 12:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69351">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">⏺
سفارت آمریکا در اردن:
از شهروندان آمریکایی مقیم در خاورمیانه درخواست می‌شود که برای ترک در صورت تشدید اوضاع آماده باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69351" target="_blank">📅 11:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69349">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14b8168f8.mp4?token=P2-xqYBH9PHWhZu6KfvAW8ax2k2FhtRROnGm7OI1x9bafDMCXG8KclYeP_DbVttx40fQMeY-rW-drFwgt8yXL2sKTsm6MpZOiWO4m5jnYuP1kpnPw7q9W6xWPwjYR_pmeL0uVxJzvUhwZ46JrOJzug3B_uzIrJHHU-V8o1-dQ_sG1Moy4tlwgjU3ajR_xGLMyk69dxfXS3KJ9-aMPVVqDk5PmQOwWToBEl_Ymy5LUhMQNTKu-7tflRVHHjupcHBUcyUmkYY0v6SmTgdvsaGyzlC0IeBaShcYaMQbdKXuyYyHWH8sccS2V9exeMrLW2BqwcPkAVffqMIhrWkJ7vRW4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14b8168f8.mp4?token=P2-xqYBH9PHWhZu6KfvAW8ax2k2FhtRROnGm7OI1x9bafDMCXG8KclYeP_DbVttx40fQMeY-rW-drFwgt8yXL2sKTsm6MpZOiWO4m5jnYuP1kpnPw7q9W6xWPwjYR_pmeL0uVxJzvUhwZ46JrOJzug3B_uzIrJHHU-V8o1-dQ_sG1Moy4tlwgjU3ajR_xGLMyk69dxfXS3KJ9-aMPVVqDk5PmQOwWToBEl_Ymy5LUhMQNTKu-7tflRVHHjupcHBUcyUmkYY0v6SmTgdvsaGyzlC0IeBaShcYaMQbdKXuyYyHWH8sccS2V9exeMrLW2BqwcPkAVffqMIhrWkJ7vRW4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
یک انفجار بسیار بزرگ در یک انبار مهمات در شهر خملنیتسکی، واقع در غرب اوکراین، رخ داده است که پس از آن، انفجارهای ثانویه گسترده‌ای نیز به وقوع پیوسته است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69349" target="_blank">📅 11:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69348">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71213a605e.mp4?token=d4x8oB1GNsfqsmTRGHs-cDkcsXkgS666U4-nv4bGgo1V0We-h7dke5LFh3ZEcq1CJmdQ4eu29S1FcAy2khdeaS1vVjydNFzBT3NCD1BXVvjQ2qQt4Ncn2-qJYF28IVupAj1CwgJ-4W-zQWjPaod_HBsfbSh-CrMzbOqfF072gdKu8MZEbVLIOdg0s5vWlBJA4P_-bg-2SwM7rYlA5WDex4ohS9vzMr-w_pTgHBw2W1juZCDY3dO7XnuQrLEErknYeedYUM7EOf_AMFiA5H6nrHjUO3pRnOF1BDMUd42kDdE-45mw3o06sFfnXMNba1aKxp4zjpSSqKzhKR9YdrpMnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71213a605e.mp4?token=d4x8oB1GNsfqsmTRGHs-cDkcsXkgS666U4-nv4bGgo1V0We-h7dke5LFh3ZEcq1CJmdQ4eu29S1FcAy2khdeaS1vVjydNFzBT3NCD1BXVvjQ2qQt4Ncn2-qJYF28IVupAj1CwgJ-4W-zQWjPaod_HBsfbSh-CrMzbOqfF072gdKu8MZEbVLIOdg0s5vWlBJA4P_-bg-2SwM7rYlA5WDex4ohS9vzMr-w_pTgHBw2W1juZCDY3dO7XnuQrLEErknYeedYUM7EOf_AMFiA5H6nrHjUO3pRnOF1BDMUd42kDdE-45mw3o06sFfnXMNba1aKxp4zjpSSqKzhKR9YdrpMnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی تحلیلگر ارشد اینترنشنال:
آمریکا و اسرائیل برای شدیدترین بمباران در روزهای شنبه و یکشنبه آماده شدن و ترامپ دستور حمله رو صادر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69348" target="_blank">📅 11:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69347">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ruV1XNtft5MxRVys6gWCf-_-mDJYagp3XCRk-qCyl8IwUGa1rLdSCVWY1zUTxuC8zrnL_77kk1OJDCZa0k_Kl20cAYDsPDOGHfvEH34Jr4weQUSbp651L_P9vPct3IEJQsclDeoIvGDJE4FwNwJA9P7PT3cR-TuUsn7w6_4fFrtVCXsrB8ywJTA-MiawdYa7sGFQtzWVDNb45nmSdyvfe06Xw02fvnT3Lktrq4FohXLLKo83wfagiuwOqBIcXzqwNoM-VJgCr11DICmJmfdtMBMttxhApVwcEEFgjWu9T_IswMIgs9H1xyWEt-hl9YezJHUfgfAn6nstJzDYMFIbOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دقایقی قبل یک کشتی در نزدیکی خصب عمان مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69347" target="_blank">📅 10:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69344">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/383c08fc2d.mp4?token=UF0Ks1yl7qf4eAs__FRpSs85WvLn79oU61w8Gn39chXugy2h1a87DbgTtaOHTL_2VDtObxEPH21Sc_2fL4pI4pyT2I7xMdN1QNzEQ4FKApNIPMqz3GDo0N9UvfD6GW_cKpqQLSe1c8cIG1zwPMRr_w-YXeQDQkgUUWy_8s996o06X2cZXX5xrYV6jdom_vqkrWjG9eQdgpGjvTk5189zUpKHTK5_VDy0rXpSXpQDnYZ3G-gQWlv4chLoi30oBzoOzYPmWWP64SKp6UJbtutgkQHjTpj4b6eGpNOl2GNOqrT2dnpqQA-rXqFh2PrNLq00T0QBvxTSuC5sdgVUD0AhVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/383c08fc2d.mp4?token=UF0Ks1yl7qf4eAs__FRpSs85WvLn79oU61w8Gn39chXugy2h1a87DbgTtaOHTL_2VDtObxEPH21Sc_2fL4pI4pyT2I7xMdN1QNzEQ4FKApNIPMqz3GDo0N9UvfD6GW_cKpqQLSe1c8cIG1zwPMRr_w-YXeQDQkgUUWy_8s996o06X2cZXX5xrYV6jdom_vqkrWjG9eQdgpGjvTk5189zUpKHTK5_VDy0rXpSXpQDnYZ3G-gQWlv4chLoi30oBzoOzYPmWWP64SKp6UJbtutgkQHjTpj4b6eGpNOl2GNOqrT2dnpqQA-rXqFh2PrNLq00T0QBvxTSuC5sdgVUD0AhVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
بروزرسانی از اسپانیا:
نزدیک ۵۰ هزار نفر از مراکش و الجزایر فرار کردن و غیرقانونی ریختن اسپانیا!
برای کنترل این مهاجرای غیرقانونی پلیس فرستادن که پلیس هم کتک زدن.
این مهاجرا ریختن توی فروشگاه‌ها دارن غارت میکنن، از مردم دزدی میکنن و...
مثلا از یه مراکشی رندوم میپرسن چرا اومدی؟ میگه توی مراکش رفیقمو به قتل رسوندم، مردم هم باهام بد رفتار میکردن، منم فرار کردم اومدم اسپانیا.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69344" target="_blank">📅 10:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69343">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/7cd4da48cd.mp4?token=JolGq-8ytr0C6mPmrV4KRi76ydNyRHbrf3Dy_CZLfTJQFO0b39t4IMqqFMz9frFEdLKTUh25vBnc18pjTsGltnVLG71ftaM8O_h-vKZhnL4XPj9pd0f6S2r8m-WOSgfPVNRr1HPazVjNrX1ySJindUSlc8OSI-6ZGc6cJGA5y0EFN5U2W8wdzacnP3ehnZzRRYM_toBcdhHAutaHl8ETMquF7RO3FnIkrYcgokjjx53cLeQt_8d4f0jB_CUKPb66KT2n4ILJmY7-Y8POJOstNxKN71YgVBTDZoPsKpltmP569OKEVQSLTMuQMhcoKTYnmPv8QCz_PNaI4aNyGkGGdzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/7cd4da48cd.mp4?token=JolGq-8ytr0C6mPmrV4KRi76ydNyRHbrf3Dy_CZLfTJQFO0b39t4IMqqFMz9frFEdLKTUh25vBnc18pjTsGltnVLG71ftaM8O_h-vKZhnL4XPj9pd0f6S2r8m-WOSgfPVNRr1HPazVjNrX1ySJindUSlc8OSI-6ZGc6cJGA5y0EFN5U2W8wdzacnP3ehnZzRRYM_toBcdhHAutaHl8ETMquF7RO3FnIkrYcgokjjx53cLeQt_8d4f0jB_CUKPb66KT2n4ILJmY7-Y8POJOstNxKN71YgVBTDZoPsKpltmP569OKEVQSLTMuQMhcoKTYnmPv8QCz_PNaI4aNyGkGGdzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
صحبت‌های عادل فردوسی‌پور درباره ماجرای دست‌بوسی عباس صالحی :
تو عُمرم دستِ مسئولی رو نبوسیدم!
عباس صالحی وارد مسجد شد و کاملاً اتفاقی روی صندلی کنار من نشست. به شوخی بهش گفتم اگه یه روزی فیلتر 360 برداشته بشه، همه این نشستن شما کنار من رو ربط میدن به رفع فیلتر!
همون موقع که داشتیم دست می‌دادیم و روی صندلی جا‌به‌جا می‌شدیم، شب دیدم یه ویدیو وایرال شده و با یه تیتر زشت نوشتن که من دست عباس صالحی رو بوسیدم.
اگه قرار بود دست‌بوس باشم که الان برنامه 90 رو داشتم و 360 رو هم فیلتر نمی‌کردن.
چطور ممکنه من برم تو اون مسجد، بین اون همه آدم، بیام دست عباس صالحی رو ببوسم و برای خودم حاشیه درست کنم؟
من همین چند روز پیش هم گفتم؛ بله‌قربان‌گو نبودم، نیستم و نخواهم بود!
همیشه روی اصول خودم ایستادم و سعی کردم کنار مردم باشم. واقعاً این حجم از هجمه‌ای که به من وارد میشه حیرت‌آوره.
من عاشق کارمم و اینو خودشون هم می‌دونن، ولی نه به هر قیمتی. اگه شرایطش فراهم باشه، تو فوتبال 360 به کارم ادامه میدم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69343" target="_blank">📅 10:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69342">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75d1e6179c.mp4?token=IpNdKsbFCVakW5lkUGrk-35kE3EgbM72fSK1FrY7-zh8iPHCMrjaJBO89bVRPe-ub7bGL5erjS12AYsGvRLE2z8lyPEwLZvMe6cxai8l4JkFvUen1hRVN63HWvA2a2JXCHVjBSZp-BZYlrshDyG3VoZv2Mk6yc-0EOtAktA9qxF7QN_s_b-VT8wq61mlRlUazdC8tbt9-lHgTakyHH2I7n4NTU9WlNrihXhRRplZldixryv2rhY-ySoIdqnA2DeUYHXLiCSuxkp1b-5E1aH-Iuo9iCpVLeHQw_wPP_ofKMkOosLFQq0zTPkkdWgLEo_1H2emdFsb-o4_OmiFgBNUww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75d1e6179c.mp4?token=IpNdKsbFCVakW5lkUGrk-35kE3EgbM72fSK1FrY7-zh8iPHCMrjaJBO89bVRPe-ub7bGL5erjS12AYsGvRLE2z8lyPEwLZvMe6cxai8l4JkFvUen1hRVN63HWvA2a2JXCHVjBSZp-BZYlrshDyG3VoZv2Mk6yc-0EOtAktA9qxF7QN_s_b-VT8wq61mlRlUazdC8tbt9-lHgTakyHH2I7n4NTU9WlNrihXhRRplZldixryv2rhY-ySoIdqnA2DeUYHXLiCSuxkp1b-5E1aH-Iuo9iCpVLeHQw_wPP_ofKMkOosLFQq0zTPkkdWgLEo_1H2emdFsb-o4_OmiFgBNUww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سیدمحمود نبویان، نماینده مردم تهران، درباره شاهنشاه آریامهر؛
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69342" target="_blank">📅 09:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69341">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی،…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69341" target="_blank">📅 02:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69340">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=hZAY6wir-jVMqJyv70WxhFZ5dkiQecuxUQMwnWNUrjRipL45LPPdbus5egsXyZ1T0fBH3vgQjl_ZIwlzhkuQewzAjxkdUM2yowD51iMOz1dXOzyzpJaS1FCcLD9J5lsMhMALQeqBFpgzwHxUqLsVdYMlmf8ceNF2ldbyWEBFllwKaG_3fpLXuROvXekJBK0whTU0u4YtpbIEjIa4z5V8W1CIgqS9Y8IkXwfv4gdp9bdcGU8xQGLLMt74aSC0tOJvPsVG_qzme4Y6yDrzq4KSMtZ3yiHG2bgOPYzZL57SiU7JcsID5DKIDkGzb0LVIF-SyrSYga_2XAg9n-kAo1b6NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=hZAY6wir-jVMqJyv70WxhFZ5dkiQecuxUQMwnWNUrjRipL45LPPdbus5egsXyZ1T0fBH3vgQjl_ZIwlzhkuQewzAjxkdUM2yowD51iMOz1dXOzyzpJaS1FCcLD9J5lsMhMALQeqBFpgzwHxUqLsVdYMlmf8ceNF2ldbyWEBFllwKaG_3fpLXuROvXekJBK0whTU0u4YtpbIEjIa4z5V8W1CIgqS9Y8IkXwfv4gdp9bdcGU8xQGLLMt74aSC0tOJvPsVG_qzme4Y6yDrzq4KSMtZ3yiHG2bgOPYzZL57SiU7JcsID5DKIDkGzb0LVIF-SyrSYga_2XAg9n-kAo1b6NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی، باشگاهی و دوستانه)
🔹
پیشنهادهای دقیق گل بالا/پایین (Over/Under) و گلزنی هر دو تیم (BTTS)
🔹
بدون ادعای واهی ضریب ۱۰۰! فقط سود مستمر با مدیریت سرمایه.
آمار ما در ماه گذشته خودش گویای همه‌چیزه. فرم‌های امروز رو از دست نده
👇
🔗
[
ورود به کانال و دریافت فرم‌های رایگان امروز]</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/69340" target="_blank">📅 02:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69339">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری فارس لیست اهداف انرژی منطقه رو منتشر کرد:مهم‌ترین تأسیسات انرژی جهان در تیررس موشک‌های ایرانی؛
❌
میدان نفتی غوار در عربستان
غوار ستون فقرات تولید عربستان است و هر گونه اختلال در آن، بیش از ۵ درصد از کل عرضۀ نفت جهان را به خطر می‌اندازد.
❌
تأسیسات ابقیق و خریص عربستان
قلب ماشین صادراتی عربستان که نفت خام میادین غوار، خریص و شیبه را تثبیت و برای صادرات آماده می‌کند.
ابقیق نیز تنها نقطه‌ای است که بیش از ۷ میلیون بشکه در روز از آن عبور می‌کند و هرگونه آسیب به آن، علاوه بر ایجاد بحران در صادرات نفت عربستان، زنجیرۀ تامین پتروشیمی‌ها و نیروگاه‌های داخلی و حتی آب‌شیرین‌کن‌ها را مختل می‌کند.
❌
پالایشگاه الرویس و میدان نفتی زاکوم در امارت
زاکوم دومین میدان بزرگ فراساحلی جهان و صاحب صادرات روزانه بیش از ۱ میلیون بشکه نفت خام است.
❌
میدان گازی گنبد شمالی و تأسیسات ال‌ان‌جی راس‌لفان قطر
بزرگ‌ترین میدان گازی جهان با ۲۵ درصد ذخایر اثبات‌شدۀ جهان؛ راس لفان تک‌مهم‌ترین پایانۀ صادراتی ال‌ان‌جی جهان و مسئول حدود ۲۰٪ از کل تجارت جهانی ال‌ان‌جی است.
❌
میدان نفتی برقان کویت
بزرگ‌ترین میدان نفتی کویت با ذخیرۀ حدود ۶۷ میلیارد بشکه؛ برقان یکی از میادین کلیدی است که در بحران اخیر، ۲ میلیون بشکه در روز از تولید کویت را از مدار خارج کرد.
❌
پالایشگاه ستره و تأسیسات المعامیر بحرین
بحرین به دلیل وابستگی شدید به این تاسیسات، آسیب‌پذیرترین کشورهای شورای همکاری خلیج‌فارس در برابر اختلالات انرژی محسوب می‌شود
❌
میدان‌های گازی لویاتان و تامار اسرائیل
ویاتان بزرگ‌ترین میدان گازی اسرائیل و تامار دومین میدان بزرگ آن رژیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69339" target="_blank">📅 02:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69338">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L48-Po4pf4hBhAMP1L4yys7LfB6uxvyCd1jF5GqRB6773T6ZwCQVVkyfwV4l73cunIJbT943CT8hkgSUvNHqGdxua3MnrLgFYcpsp-5yGb76UQR-WJ3u4mZOUcLXo43oI3wVVLPbiDeRVYIC3tPB4W2b7JBqvtw7w0s3DwheCVrtvikRdT4IR6UdhReGHY12n8sU8TFfOTFTw8ulWdbLQ_G9QGeDKNPoopCzY0-8TPEV8yOeAKzRWJJrZRUaNye9_3zttApkF-FGs0LYcgTH7PLZ4uR4VPMG6bM9WExJDg1od3bUToe3Ss7eK1NNcyDjFVONYKw-g6UPar1b6b3NYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
تسنیم:یه مقام ارشد امنیتی به ما‌گفته؛اگه آمریکا یا اسرائیل بخوان به زیرساخت‌های ایران حمله کنن؛
ایران از قبل یه برنامه گسترده برای جواب دادن آماده کرده.
به گفته این مقام، توی این برنامه، زیرساخت‌های حیاتی اسرائیل و تأسیسات انرژی آمریکا تو منطقه هم جزو اهداف در نظر گرفته شدن.
نیروهای مسلح ایران توی جنگ 40 روزه و اتفاقات هفته‌های اخیر نشون دادن هم توان انجام چنین عملیاتی رو دارن و هم برای انجامش اراده لازم رو.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69338" target="_blank">📅 02:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69337">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIbuiSC-wOEqKgMfniEcqCbvPARZfGG29FcGlsDmxY7i0oDl4rF7-UcFE23LIX5tRIUcoK5U943G8cbQ_2jESg_u_lPPCfdYKgADD7XQ155t5LvRVF1ykZAm_sz7A6qGrAg0tYz_2h8w0NyzAq1fOrXsvkB08S4XgraFA3RheyAhEJX1r8jvtWwFdr1bdbUv787fIjzgrMaDWSNUTuVYi9ThHTDeHdfChj8hE3AUqQzmP5WsdKMVlZsmCVtTflbFZcG_EQ5e-BuVaf5NHPZsYj0hjOuqw1ju9jHKFo-A8qujoPJg4tVMuOf5E4lr4VBxrmcuJnFQlFoO59RhhGtzmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛آکسیوس:ترامپ در حال بررسی حمله به تأسیسات انرژی ایران ظرف چند روز آینده است.
یک مقام آمریکایی روز جمعه به «اکسیوس» گفت که رئیس‌جمهور ترامپ به‌طور جدی در حال بررسی انجام حملاتی علیه تأسیسات انرژی ایران در چند روز آینده است، اما هنوز دستور نهایی برای اجرای آن را صادر نکرده است.
این حملات همچنین ممکن است برای نخستین بار پس از چندین هفته، ارتش اسرائیل را نیز درگیر کند و چنین تشدید تنشی احتمالاً به حملات موشکی ایران علیه اسرائیل منجر خواهد شد.
سی‌بی‌اس نیوز و وال‌استریت ژورنال نخستین بار درباره حملات احتمالی گزارش دادند.
ترامپ در آغاز جلسه روز جمعه کابینه، با اشاره به حمله احتمالی گفت: «خب، ما ضربات بسیار سختی به آن‌ها وارد خواهیم کرد و می‌دانید، بالاخره زمانی فرا می‌رسد که آن‌ها خواهند گفت دیگر تاب و تحملش را نداریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69337" target="_blank">📅 01:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69336">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rBqif8rsWxtYShlD5WIhH-8NgmVxevXlhNL7liqrhBXRwsOD7hoyzqKX-7XqYE5VYmRwm0sTx9w7dSnr3CD9lszCu7jsCqlJ_yTo0Wq7uJCO4c2zLVlGSYDxaVljQT0nDJfjZL8nYKWFnpZ9pJMOwtze56kXNYYzgr2xKYsTe504AaH4l1eTPxS3Og0q3zm6Fy-Ollwj36uCCJY4gMJij1l6Y2vpOd5IkV1RFNPnrIRHHSMGx3Vb0ziEl_JY0zxR5zHIg4xsDSupQ8qbIeinPXDvIRxKNI4oitt0sQfYvKh2tSomQIcTJEYFAMBp1gKBZBPmMR3yBQtcmd84shIsyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
🇮🇱
سی‌بی‌اس نیوز:
ایالات متحده و اسرائیل در حال آماده‌سازی یک کمپین بمباران مشترک بزرگ علیه زیرساخت‌های انرژی ایران، از جمله نیروگاه‌ها و پالایشگاه‌ها هستند.
ترامپ هنوز تأیید نهایی را نداده است، اما حملات ممکن است این آخر هفته آغاز شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69336" target="_blank">📅 01:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69335">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5040574e14.mp4?token=oy_yaktAHIE2v7kKZkkhOWpFDC2OiSj7ys6PfiAp73fLl0zmXgNMyxHUU8sz1y6T2WsrpcQZKldT2V7Ll8o7qGwCbX9twX_sugoIG9-IDe3869Y0wxkohw8cMAeAbbMcBPFqVl7YxFLTYZLI-OqfhAZgTzWq_p_7mPLeQTQnO_mR7QVYDQJXhn_RUfIkyTqggdy2V6ayhNsTJ0a6t8kzWwCrwBPUxvHJzkG1MIMqxMaB8OvNVRioy-q62-uEfZ2vrxjbYRgRsRd9DduQ9PZQQ0aieGE_Uw4VdpPP5BWBHM7q_f6Vn4_k-91xJF2QdT5YkdmulEdREXuf-NsWZsMhsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5040574e14.mp4?token=oy_yaktAHIE2v7kKZkkhOWpFDC2OiSj7ys6PfiAp73fLl0zmXgNMyxHUU8sz1y6T2WsrpcQZKldT2V7Ll8o7qGwCbX9twX_sugoIG9-IDe3869Y0wxkohw8cMAeAbbMcBPFqVl7YxFLTYZLI-OqfhAZgTzWq_p_7mPLeQTQnO_mR7QVYDQJXhn_RUfIkyTqggdy2V6ayhNsTJ0a6t8kzWwCrwBPUxvHJzkG1MIMqxMaB8OvNVRioy-q62-uEfZ2vrxjbYRgRsRd9DduQ9PZQQ0aieGE_Uw4VdpPP5BWBHM7q_f6Vn4_k-91xJF2QdT5YkdmulEdREXuf-NsWZsMhsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک مهاجر مراکشی درحال رفتن به منطقه برون‌بومی اسپانیایی «سئوتا»
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69335" target="_blank">📅 01:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69334">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری؛وال استریت ژورنال:ترامپ دستور حمله جدیدی به ایران را صادر کرد.   مقامات آمریکایی اعلام کردند که رئیس‌جمهور ترامپ دستور حمله جدیدی را به ایران صادر کرده است که هدف آن وادار کردن تهران به تسلیم است؛ این حمله ممکن است از همین آخر هفته آغاز شود و چند…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69334" target="_blank">📅 01:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69333">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHZNgkuwtkyILEzf1kLQP0BY-i8RnACFPoS8sx1xvJ48zJGNIHnR-vU-alR_LDUyDukhaR3zPuFNfqxlJaEES002NMxZPAX3p9zpqMUiczF6DTuwQvYG3C7bT3UKJo9fGfox7Iax-DUS3zEH8mZSSZI-DVhq02F2aS3m02RgXPiOdk8msZJ6ULjkD2Os2ymQ-NyFsKD53TlYkT18gKen0d127BIyJ-ZUTW1suOuEdPEH2OSXlNPMluISMZsW9U2Uwa5-zMKLcQrc51mfPFRMx8aVNxoyNu-w3fzP-b-aVCB_n7--IR6NnTeoN7jr818nZJ79BfTWVRnbuXfLPp-crw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛وال استریت ژورنال:ترامپ دستور حمله جدیدی به ایران را صادر کرد.
مقامات آمریکایی اعلام کردند که رئیس‌جمهور ترامپ دستور حمله جدیدی را به ایران صادر کرده است که هدف آن وادار کردن تهران به تسلیم است؛ این حمله ممکن است از همین آخر هفته آغاز شود و چند روز به طول انجامد.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69333" target="_blank">📅 01:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69332">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">چندین منبع به CBS News گفته‌اند که حملات ممکن است در طول آخر هفته انجام شود</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69332" target="_blank">📅 01:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69331">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3b500b5c2.mp4?token=bNetu_ZQvj8saPHJzROnPlk6gG8mpnakm07byHLsxEy0Qg13qybd7lrQI6gk5BOGUPQJz7KCrAbVtzwswcQ5T01oWjozYJiPqNXWLlfhluXAbdYrjntI5cPtvBm-rSvhj7pI6jy4_M0taPw7Yur6aWeOk0qcHnKMUkkyqcMSpoeUostF97wBYsMVMclP7QX3DExx00-4ecrOwbTYqN8ktnu5O02uMQ_11qiX99UOoHH9fg9a0P6dWX3AaO5A9pZxfbNqzX15qnY34PNHDH5mTB8DYq0IHrwhXBjRn6mfIfnwxT105iOjRg6_E9MhE-EgZKT4QlcAOicofz5JaDQp9Uge3DGA77bH52064Yc2XuURNqlY4Y4Tsy3fFo8ZOPPcaw_3t8p3h_EezgvdzHuhIHAOcbsZVa6UqgSPKCztFF-As3tR9iG2RIa-8mC0ZEoWngp4ufkX61Zvqqc3sVicGCjZEFwMJaTWW3Kd9FmW9to4h2XY7wmPxVl8vVaS1vF4YHbpttialSrRfCs8tfFPZKTuq-WShbFJaVRGyIJDaFxIBljFMW68V7ydjWomkUBcOv0u4nFkmX7yjwvuBTqg2cdLhsBLSPDZRPxb4kCfasclo1Jl4sah1gCT8ETWPCu2RlEuLLJGgibc9_ku2iMucfFDzfZRTNcoJ5N1scBNAyk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3b500b5c2.mp4?token=bNetu_ZQvj8saPHJzROnPlk6gG8mpnakm07byHLsxEy0Qg13qybd7lrQI6gk5BOGUPQJz7KCrAbVtzwswcQ5T01oWjozYJiPqNXWLlfhluXAbdYrjntI5cPtvBm-rSvhj7pI6jy4_M0taPw7Yur6aWeOk0qcHnKMUkkyqcMSpoeUostF97wBYsMVMclP7QX3DExx00-4ecrOwbTYqN8ktnu5O02uMQ_11qiX99UOoHH9fg9a0P6dWX3AaO5A9pZxfbNqzX15qnY34PNHDH5mTB8DYq0IHrwhXBjRn6mfIfnwxT105iOjRg6_E9MhE-EgZKT4QlcAOicofz5JaDQp9Uge3DGA77bH52064Yc2XuURNqlY4Y4Tsy3fFo8ZOPPcaw_3t8p3h_EezgvdzHuhIHAOcbsZVa6UqgSPKCztFF-As3tR9iG2RIa-8mC0ZEoWngp4ufkX61Zvqqc3sVicGCjZEFwMJaTWW3Kd9FmW9to4h2XY7wmPxVl8vVaS1vF4YHbpttialSrRfCs8tfFPZKTuq-WShbFJaVRGyIJDaFxIBljFMW68V7ydjWomkUBcOv0u4nFkmX7yjwvuBTqg2cdLhsBLSPDZRPxb4kCfasclo1Jl4sah1gCT8ETWPCu2RlEuLLJGgibc9_ku2iMucfFDzfZRTNcoJ5N1scBNAyk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«قیمت‌ها حسابی اومده پایین، به‌جز نفت.
دو هفته پیش، وقتی همه فکر کردن توافق نزدیکه، قیمت‌ها مثل سنگ سقوط کرد.
ولی ما یه
توافق واقعی
می‌خوایم، نه یه توافق الکی.»
🎙
استیو گروبر:
درباره ایران، فکر می‌کنید چقدر طول بکشه تا این ماجرا تموم بشه؟ یه ماه؟ یه سال؟
🇺🇸
ترامپ:
«پیش‌بینی کردنش همیشه سخته.
ما ماجرای ونزوئلا رو توی کمتر از یه روز جمع کردیم.
اگه می‌خواید همه‌چیز خیلی سریع تموم بشه، کافیه به یه عده سلاح هسته‌ای بدید!
اون‌وقت همه‌چیز خیلی سریع تموم می‌شه.»
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69331" target="_blank">📅 00:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69330">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7487679e0.mp4?token=blJtAvC_XRtTEvPEETcuVrQLN42LdRPhqveBU8arXnxQ7pyQXWv_cQC6GynemOaplyNhLjKtt3KnwuoSQLwBpZA1hs1XDpJlEBl44OiI9O0S1C4fP_yyASx1sj-9B9nyPC2idkuqa_QCBP3JlM6OshFXM_ebq43va1v5Z_jXeEHVUxf5goc1hGiUtknMPtCIHOTS5j4D1OKZE7BkCeqdVrX6FefHyJukl0A1zu1AbBSHO7xbYbCb1z3oV7uwp2gHIpOiA1nRtffeJTOFb3cMFd8kzysGhTrC0h2E3MfjzO8EcSc67wbqml-rdUbi2AsvlGwL8AFDWN6CdL1qTAw8cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7487679e0.mp4?token=blJtAvC_XRtTEvPEETcuVrQLN42LdRPhqveBU8arXnxQ7pyQXWv_cQC6GynemOaplyNhLjKtt3KnwuoSQLwBpZA1hs1XDpJlEBl44OiI9O0S1C4fP_yyASx1sj-9B9nyPC2idkuqa_QCBP3JlM6OshFXM_ebq43va1v5Z_jXeEHVUxf5goc1hGiUtknMPtCIHOTS5j4D1OKZE7BkCeqdVrX6FefHyJukl0A1zu1AbBSHO7xbYbCb1z3oV7uwp2gHIpOiA1nRtffeJTOFb3cMFd8kzysGhTrC0h2E3MfjzO8EcSc67wbqml-rdUbi2AsvlGwL8AFDWN6CdL1qTAw8cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
توی درگیری با ایران، بسته به اینکه چه آماری رو حساب کنید،
16 تا 18 نفر
از نیروهامون رو از دست دادیم؛ که همین هم خیلی زیاده، چون حتی از دست دادن
یه نفر هم زیاده.
جنگ ویتنام
21 سال
طول کشید. ما تازه وارد
ماه پنجم
شدیم، ولی همون‌ها که آمریکا رو 21 سال توی ویتنام نگه داشتن، حالا می‌گن "چرا ماجرای ایران این‌قدر طول کشیده؟"
من الان دارم کاری خیلی بزرگ‌تر از چیزی که اول گفته بودم انجام می‌دم. قرار بود فقط وارد بشیم، توان نظامی ایران رو نابود کنیم و برگردیم.
ولی بعد دیدم اگه فقط این کار رو بکنیم و بریم، دوباره خودشون رو بازسازی می‌کنن. برای همین باید یه جور
کنترل و نظارت
هم وجود داشته باشه، وگرنه دوباره همه‌چیز رو از نو می‌سازن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69330" target="_blank">📅 00:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69329">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdc86e1f9d.mp4?token=V5xUaGuglRR8hLcEN8UpseaGEk59tVhjgVAZhy47Z1knApOhIq5dus_rSs3U4I0PoR1xAti8XVY_G0y57ScOmhHFspGfEpt0P47_W8MoJQH-EqsT3bxOfF-umuxrCAMUZ4FzDJ_CcpFwsigrW26xo8NUTwbDBTqK0y0HWktSB0KdZq2QCqpzxEagJiN3XXYprUo8h6mVVPbK3LVoby1_nqEQOZNK3lB5vuKfASFFO7v9k95BR9XACWBvzlAqhxJmPw4TmenF5gmSheCc_B2JVURkEEy7t0Cvy1LjHA6exD0HBVu8TtXoLz17EaZJlo2o47HONuUMK77kx7KN9Rz0jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdc86e1f9d.mp4?token=V5xUaGuglRR8hLcEN8UpseaGEk59tVhjgVAZhy47Z1knApOhIq5dus_rSs3U4I0PoR1xAti8XVY_G0y57ScOmhHFspGfEpt0P47_W8MoJQH-EqsT3bxOfF-umuxrCAMUZ4FzDJ_CcpFwsigrW26xo8NUTwbDBTqK0y0HWktSB0KdZq2QCqpzxEagJiN3XXYprUo8h6mVVPbK3LVoby1_nqEQOZNK3lB5vuKfASFFO7v9k95BR9XACWBvzlAqhxJmPw4TmenF5gmSheCc_B2JVURkEEy7t0Cvy1LjHA6exD0HBVu8TtXoLz17EaZJlo2o47HONuUMK77kx7KN9Rz0jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از یه هموطن که تو خونش کره خر نگهداری میکنه و بردتش رو تردمیل تا دلتنگی بیرونو نکنه
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69329" target="_blank">📅 23:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69328">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YobqDl3wKZ85Yt5v2DndDjK0gIJPf6KobH2EPx0FTNMbdKlnUEUWxaLjwVKjh3m7AUG6tIRvERm-6C_z5C5qFU42jUgNubAyDbjRxX8LThZYUB6IuSJ6BqtAksrg7FLgqBQIviEacadEGyT3N1i1Vi195Bckp0qLOUz-o4oeasOpBlpn1RoVa2Ujc4wY9EErU90zsQPDvEHK3zI6a_hBUAySOoQAdiONu49hYlXDdsFnRVWEB_qZVj3VPys3dkWk53m7m6KqMCXRkN5ZNXXR8KcKBt9tiRxzbw_Wyc0pA7X8JGm-clXANskU-VJyGRZ-7Qll0whWdt73tFNPTYx7Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنتکام برای بار هزارم:
تنگه هرمز بازه و ادعای سپاه مبنی بر بسته بودن تنگه هرمز دروغه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69328" target="_blank">📅 23:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69327">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdfe35db6c.mp4?token=h90afPXSU7KFhIvUuVYVT8e_w_5RtrgkABEW8BkyXoMb5hOG3G9v-4-6gO7FhbPklGWVHmOFheaezu1roYR9PBXu9aPXcx36oGuXHkpobLwuX7vlzbiW7u7AiH2sBBz4JDXfmRh7UBUr_ekwTp4tJyETopGb0P1XzlPNxcpOe7b4bqOGd3JQaNg2Fi3Cl7gR937yz8KNrjt_c43a6cBfHaqZtwE6O42b46F7XGvJFfBvpt220Dg-rDwrz-HAX4Ca6GKyGi9NwRbk0deXZ2D_jLxQtxOtLEMKhRjU5vU7aHLa9TTXUCc15125s1PsYqDbX_TyhHKL3DOPxLPr_MTqZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdfe35db6c.mp4?token=h90afPXSU7KFhIvUuVYVT8e_w_5RtrgkABEW8BkyXoMb5hOG3G9v-4-6gO7FhbPklGWVHmOFheaezu1roYR9PBXu9aPXcx36oGuXHkpobLwuX7vlzbiW7u7AiH2sBBz4JDXfmRh7UBUr_ekwTp4tJyETopGb0P1XzlPNxcpOe7b4bqOGd3JQaNg2Fi3Cl7gR937yz8KNrjt_c43a6cBfHaqZtwE6O42b46F7XGvJFfBvpt220Dg-rDwrz-HAX4Ca6GKyGi9NwRbk0deXZ2D_jLxQtxOtLEMKhRjU5vU7aHLa9TTXUCc15125s1PsYqDbX_TyhHKL3DOPxLPr_MTqZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
«این‌ها خیلی وقت‌ها زیر قولشون می‌زنن.
توافق می‌کنن، بعد می‌گن باید
7 ساعت
درباره برنامه هسته‌ای مذاکره کنیم.
من می‌گم: "آخه چرا 7 ساعت؟ مگه نمی‌شه تو
10 دقیقه
جمعش کرد؟"
شما
5 دقیقه
وقت دارید که تکلیفتون رو روشن کنید.
آخرش هم فقط کله منو کیری می‌کنن!»
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69327" target="_blank">📅 22:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69326">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/379fea6ae8.mp4?token=j429dPoiK_MBaP7tTVJH9IsnrSn3NKhtF3vcueoySR97T2rqaCflhv1A-CtOHigzPqHEE3Xc5aEBe8bRsgEWjqUWd12Xftq8Tn8ltAnpTzZTEYJWy6-Dk7A81-FjuHEd7LTT3gBh3LDWmMBhiMFPPMBVh6ywGQgTH0BcZVP7jZ7Ow3ooOTken3b3I1wKCHExVVV-aNRBEOCFgO05XZ5oRU3etS3QiUOc-UbDmHcQVokj6WBwYHcT4ZwOGbrXz2Q47YvyKITn3jvwx8vvRAk7-FVRGHXD42mMLbYjMTaDU_fhlSosTewdwxB8AblRQ7CjpGUhGgC3shpJf2xzUYiH9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/379fea6ae8.mp4?token=j429dPoiK_MBaP7tTVJH9IsnrSn3NKhtF3vcueoySR97T2rqaCflhv1A-CtOHigzPqHEE3Xc5aEBe8bRsgEWjqUWd12Xftq8Tn8ltAnpTzZTEYJWy6-Dk7A81-FjuHEd7LTT3gBh3LDWmMBhiMFPPMBVh6ywGQgTH0BcZVP7jZ7Ow3ooOTken3b3I1wKCHExVVV-aNRBEOCFgO05XZ5oRU3etS3QiUOc-UbDmHcQVokj6WBwYHcT4ZwOGbrXz2Q47YvyKITn3jvwx8vvRAk7-FVRGHXD42mMLbYjMTaDU_fhlSosTewdwxB8AblRQ7CjpGUhGgC3shpJf2xzUYiH9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎤
خبرنگار:
سنتکام گفته حملات اخیر برای کم کردن توان ایران در مختل کردن تردد کشتی‌ها در تنگه هرمز بوده. به نظرتون چند حمله دیگه لازمه تا به این هدف برسید؟
🇺🇸
ترامپ:
«هیچ‌وقت نمی‌شه دقیق گفت.
بیشتر کشورها تا الان تسلیم شده بودن.
ایران هنوز تسلیم نشده و بابت همین باید بهشون اعتبار داد.
اونا همیشه به سرسخت بودن معروف بودن؛ واقعاً هم سرسختن.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69326" target="_blank">📅 22:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69325">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d8357e0fa.mp4?token=v7l0U3msJAMepSaJAq2V-dRgqS8hzusIiSyIs_fzBrDAEd0bZ40EY60thHovBV3c0328bxrhwS50c861wnB2Ps97UcfA6rOyK7-FiSERCwHOI6zXE3DGDZ4knZOO-HyALizfkJ9iMM1_8oIpFJjXxsGWj08fIwccSXo22ndGsU-a59ksfw29bqC1mmgJsg4ZZRskX9PJHs-1Tl3-85Xslt6h5qi4Etc2ngQLoZHYB5ZejvSAo_j8y0iy1S8bWE5izpLV25c4Am8SFG4mNOyQWCc39otQHC3ge-M26zH5oSET6_9PhcpXJTy5kGHCklkUgfxlKlMwUJ6FJZVEqEQIKSTYOqlh7bFHT0vlNb0xxOt0WN0-hOeI23pHQYRW4M3BlUCE_HnLGP-ZchPtYwQOxhN4sfEbIBun0QID51gOTyVlvBZ74G8W31wOyzhQtF2aUIDvvXC6wYpRmJW8IVbl2axcAo-gpu4So10ALFN5BdYfsCEOu9h2VWaWMdclaX6puwp3RSOLx_jFc8MEoP8pPhBOWbwaTfKBbTFni4VEbl8SJmKubSbXtSDmNaa5ggSBI7lH1ERlYYWcrjnIabTb_J2cyw6QEtEL9ibVVN5WBykxzHXsHPzyqGL5_zHUvm3bWCgjSHgLYlLhC5jBltBXDCUISo8C5iLcFKb76mP9KgM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d8357e0fa.mp4?token=v7l0U3msJAMepSaJAq2V-dRgqS8hzusIiSyIs_fzBrDAEd0bZ40EY60thHovBV3c0328bxrhwS50c861wnB2Ps97UcfA6rOyK7-FiSERCwHOI6zXE3DGDZ4knZOO-HyALizfkJ9iMM1_8oIpFJjXxsGWj08fIwccSXo22ndGsU-a59ksfw29bqC1mmgJsg4ZZRskX9PJHs-1Tl3-85Xslt6h5qi4Etc2ngQLoZHYB5ZejvSAo_j8y0iy1S8bWE5izpLV25c4Am8SFG4mNOyQWCc39otQHC3ge-M26zH5oSET6_9PhcpXJTy5kGHCklkUgfxlKlMwUJ6FJZVEqEQIKSTYOqlh7bFHT0vlNb0xxOt0WN0-hOeI23pHQYRW4M3BlUCE_HnLGP-ZchPtYwQOxhN4sfEbIBun0QID51gOTyVlvBZ74G8W31wOyzhQtF2aUIDvvXC6wYpRmJW8IVbl2axcAo-gpu4So10ALFN5BdYfsCEOu9h2VWaWMdclaX6puwp3RSOLx_jFc8MEoP8pPhBOWbwaTfKBbTFni4VEbl8SJmKubSbXtSDmNaa5ggSBI7lH1ERlYYWcrjnIabTb_J2cyw6QEtEL9ibVVN5WBykxzHXsHPzyqGL5_zHUvm3bWCgjSHgLYlLhC5jBltBXDCUISo8C5iLcFKb76mP9KgM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗣️
حسین جنتی، شاعر : سقوطِ زندگیم جایی اتفاق افتاد که سال 89 جلوی علی خامنه‌ای شعر خوندم؛
من سال 89 دعوت شدم به شعرخوانی تو بیت رهبری و شب قبلش بهم گفتن 5 تا از شعراتو باید بدی ما نگاه کنیم، درنهایت یکیشو اجازه میدیم بخونی.
ولی من شعری که اجازه نداشتم رو اونجا خوندم:
گشته‌ام میدان به میدان شهر را، هرگوشه دردی هست
ارتفاع درد از پیچ شمیران میرود بالا
درد من هرچند درد خانه و پوشاک ارزان نیست
با بهای سکه در بازار تهران میرود بالا
گفتم که خواجه در رویای خود از پای‌بست خانه میگوید
ناگهان صدها ترک از نقش ایوان میرود بالا
گفتم جوجه‌های اعتقادم را کجا پنهان کنم
وقتی شک شبیه گربه از دیوار ایمان میرود بالا
فردا صبحش اومدن سراغم و گفتن تو غلط میکنی با ولی‌امر مسلمین شوخی کردی و سقوط آزاد زندگی من همونجا اتفاق افتاد و اصلا هم پشیمون نیستم از کاری که کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69325" target="_blank">📅 22:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69324">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d259260d40.mp4?token=NVYPlDGW_ARRq0aUc9dOzaQsUtHvysHsSNWmGkthlMuGqwry2DKr3CF9y4C4gAtrQryQwj1O91pjD-M8hDzs_4sRjtH-A2U-TlsIEKSJSa90_2jd1LpAg9Qht9axGp7zCMkmbUo1nO7Tglo5O9kFCsK-i1yC0ZNGDK2cHLv-g_Wl9iAM21M2qZyxnQgZahLlfbNlnVMqhIFytHlTQb3b1Wm1HXCfXdFyRaII-NZqxX5ntYmaHF0UyvkOfuYSUyjXOCwtS39ycJgu9LP1wwri3gRBcSM3_6p2-DeoWVPJYtIelH9l1hXEsUSIy7E7oQDE6-EaYPYegZZ8y6-XvXzfZYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d259260d40.mp4?token=NVYPlDGW_ARRq0aUc9dOzaQsUtHvysHsSNWmGkthlMuGqwry2DKr3CF9y4C4gAtrQryQwj1O91pjD-M8hDzs_4sRjtH-A2U-TlsIEKSJSa90_2jd1LpAg9Qht9axGp7zCMkmbUo1nO7Tglo5O9kFCsK-i1yC0ZNGDK2cHLv-g_Wl9iAM21M2qZyxnQgZahLlfbNlnVMqhIFytHlTQb3b1Wm1HXCfXdFyRaII-NZqxX5ntYmaHF0UyvkOfuYSUyjXOCwtS39ycJgu9LP1wwri3gRBcSM3_6p2-DeoWVPJYtIelH9l1hXEsUSIy7E7oQDE6-EaYPYegZZ8y6-XvXzfZYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت های یک عرب درباره ایران:
ایران از جامعه عرب متنفر است، یک تنفر تاریخی.
همانگونه که اسرائیل از جامعه عرب تنفر دارد.
اگر کتاب فردوسی(کتاب شاهنامه و قوم پارس)رو بخونید شک ندارم که ممکنه باعث بشه بالا بیارید.
چرا؟چون عرب را به زشت‌ترین اوصاف وصف میکند.
مثلا فردوسی گفته:عرب در آن مکان خورنده ادرار شتر است،خورنده ملخ اس، ولگرد و کثیف است.
اما فردوسی میگوید اینجا در ایران حتی یک سگ در اصفهان از آب پاک و زلال رودخانه میخورد.
حتی یک سگ در اصفهان شریف تر از عرب در آن مکان است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69324" target="_blank">📅 20:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69323">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea4c431667.mp4?token=uGgcYCy8ERXv6u6Z5E84g4UBdUW0WszWPnhZSi9IfMvqJIWKmYQJWAmE_XvlD-1cf1KF2AkjHUt4b_4QEenzeUUYDo1_iscaJRQ32E2_Qhm_Ei2vmN0ZYj1LaGhRPDuBtPbgXHZM5kh2wH_66rraC2vNi3j670YeUqqK3muCIi3L6xrVW-KGD99j5B1d3iVEQjY7Xh4jWLSSyYoFvF7NKH9RUkjV8tKBD_Z53caiY30E0lM7WqQAV25h7uHeh5kneZz5UdmnqrSmvfZzQ8GJHmK5EqaQH5BfdYRgVPTozeQgcUatcXi7ZWg6OU3kANVleyklMqxUmDCnBST277hFGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea4c431667.mp4?token=uGgcYCy8ERXv6u6Z5E84g4UBdUW0WszWPnhZSi9IfMvqJIWKmYQJWAmE_XvlD-1cf1KF2AkjHUt4b_4QEenzeUUYDo1_iscaJRQ32E2_Qhm_Ei2vmN0ZYj1LaGhRPDuBtPbgXHZM5kh2wH_66rraC2vNi3j670YeUqqK3muCIi3L6xrVW-KGD99j5B1d3iVEQjY7Xh4jWLSSyYoFvF7NKH9RUkjV8tKBD_Z53caiY30E0lM7WqQAV25h7uHeh5kneZz5UdmnqrSmvfZzQ8GJHmK5EqaQH5BfdYRgVPTozeQgcUatcXi7ZWg6OU3kANVleyklMqxUmDCnBST277hFGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🤡
یه بخشی از صحبت های خیلی مهم ترامپ: بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ  @HutNewsPlus</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69323" target="_blank">📅 19:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69322">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/884550e186.mp4?token=NW8WqqNvlQ-xjsMmlWajrnUzg0VnCnXgQQP3Sm5EHCRi6uXNR07EzJWitUm9SrzBKguZy_irkk2pa7038_Z4bDg5Bj3Nx3-JkncGhLQzgvGirzpq8LwcycFAfa5kqtkVkBwOhIGx3AbyAo5LWzUsyDO-0BiLfEm27HLBn7ehlsw4t1zcatpUOo0taU80QO5BTqvDXg4qjOa6JquKUj7B8k65bt94zmnj6Rxa7xuSWcmeqIh2073GXMs6LNw9R-sw5cFlErzAFtpeTF_rIwNVUVltxsMC75A2VTyCKbWpBcAnicrVBUSSAtnUll66lhlaO5P5c1ZdV1CNyANp4gE-jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/884550e186.mp4?token=NW8WqqNvlQ-xjsMmlWajrnUzg0VnCnXgQQP3Sm5EHCRi6uXNR07EzJWitUm9SrzBKguZy_irkk2pa7038_Z4bDg5Bj3Nx3-JkncGhLQzgvGirzpq8LwcycFAfa5kqtkVkBwOhIGx3AbyAo5LWzUsyDO-0BiLfEm27HLBn7ehlsw4t1zcatpUOo0taU80QO5BTqvDXg4qjOa6JquKUj7B8k65bt94zmnj6Rxa7xuSWcmeqIh2073GXMs6LNw9R-sw5cFlErzAFtpeTF_rIwNVUVltxsMC75A2VTyCKbWpBcAnicrVBUSSAtnUll66lhlaO5P5c1ZdV1CNyANp4gE-jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🤡
یه بخشی از صحبت های خیلی مهم ترامپ: بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ
@HutNewsPlus</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69322" target="_blank">📅 19:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69321">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caed943dd3.mp4?token=TzFOkDJjP7-oNFsHQg6H2QUOaTL1cr4YY0pZYLPTg9ke6Qcp9In84mkRGGroETn2gdvk0xBlgWAx1ZLAz2_VY40TahR_gY7ouS3lkrinp2_NEhVu4KKg9LZJGv15VPBjYmz5pUkjJVMfqLc6OFzbMqq5L6G04iVnzvcvw2pqx9wogoBy-vSsCmFe8kWHo2N0Rq_gegLbNCzr_zwBPr8cFf1Szw_pFlR1Ig0EpPLHFoUrkwynEZ8Tzabz6W20wCTRMp-w2AOsmTALbM4oWzo93OOI04ttWUJ4twYCPFgfuo6XFK2eyxvX5Yqp4vMyjUwXEWCOu0nncXZ56_R-PqA58w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caed943dd3.mp4?token=TzFOkDJjP7-oNFsHQg6H2QUOaTL1cr4YY0pZYLPTg9ke6Qcp9In84mkRGGroETn2gdvk0xBlgWAx1ZLAz2_VY40TahR_gY7ouS3lkrinp2_NEhVu4KKg9LZJGv15VPBjYmz5pUkjJVMfqLc6OFzbMqq5L6G04iVnzvcvw2pqx9wogoBy-vSsCmFe8kWHo2N0Rq_gegLbNCzr_zwBPr8cFf1Szw_pFlR1Ig0EpPLHFoUrkwynEZ8Tzabz6W20wCTRMp-w2AOsmTALbM4oWzo93OOI04ttWUJ4twYCPFgfuo6XFK2eyxvX5Yqp4vMyjUwXEWCOu0nncXZ56_R-PqA58w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خبرنگار:
در مورد ایران، گزارشی وجود دارد که نشان می‌دهد شما پیشنهادی از سوی ارتش برای گسترش چشمگیر فعالیت‌ها دریافت کرده‌اید.
ترامپ:
ما از قبل گسترش داشته‌ایم. منظور از "گسترش چشمگیر فعالیت‌ها" چیست؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69321" target="_blank">📅 19:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69320">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">املاکی تو یه جمله همزمان گفت هم می‌خوایم خیلی شدید به اونا ضربه بزنیم و هم می‌خوایم خیلی مهربون باشیم باهاشون
🤡
#hjAly‌</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69320" target="_blank">📅 19:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69319">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0411d5fa4.mp4?token=XtQpQ0UF4CjwlMOr1RlFJTq9uWhrkO63-A-B7Wii9DnNE1H1V5d_mMFBJ-iOHJCTzc8QrWduMvvU0nX5PilzoIL6znM8HheSUdp_id1CjOXDqiRUYUkyPowdkizG2sn8jhKNMTaP9KElHSrnqH1NelEBSAQOyWGv9A_8omZNhlbQ8xGQYsvuj1SDKAxIo0pT9DvORN38gFSjkGHm2CDQ4xzi9L7SoqmT7_uWmpEnDZotdgEUPUChVW7i8pRvLuipfSPL0jKfQZeS64G3r5I1UqtLWBVdaqNpQURZM4N---id0XbzJPYmvarpMNk5vZqBj-OxHNLYrcwyEAuSLwD4WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0411d5fa4.mp4?token=XtQpQ0UF4CjwlMOr1RlFJTq9uWhrkO63-A-B7Wii9DnNE1H1V5d_mMFBJ-iOHJCTzc8QrWduMvvU0nX5PilzoIL6znM8HheSUdp_id1CjOXDqiRUYUkyPowdkizG2sn8jhKNMTaP9KElHSrnqH1NelEBSAQOyWGv9A_8omZNhlbQ8xGQYsvuj1SDKAxIo0pT9DvORN38gFSjkGHm2CDQ4xzi9L7SoqmT7_uWmpEnDZotdgEUPUChVW7i8pRvLuipfSPL0jKfQZeS64G3r5I1UqtLWBVdaqNpQURZM4N---id0XbzJPYmvarpMNk5vZqBj-OxHNLYrcwyEAuSLwD4WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ایران وضعیت خیلی بدی داره؛ واقعاً خیلی بد. اوضاعشون خیلی خراب شده و تحت فشار شدیدی هستن.
تعامل باهاشون هم خیلی سخت بوده؛ هم صادق نبودن، هم قابل اعتماد رفتار نکردن.
ولی این چیزی رو عوض نمی‌کنه؛ چون در هر صورت، حال و روزشون خیلی بده.
ما فقط پنج ماهه اونجا هستیم. اگه به جنگ ویتنام نگاه کنید، می‌بینید آمریکا بیست سال اونجا بود. کاری که الان علیه ایران انجام می‌دیم، از نظر من یک عملیات نظامیه، نه جنگ.
ایران هنوز چند تا موشک داره، اما خیلی کمتر از چهار پنج ماه پیش.
توان تولید موشک‌شون تقریباً از بین رفته و ظرفیت پهپادیشون هم تقریباً نابود شده.
البته هنوز مقداری از این توانایی‌ها رو دارن.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69319" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69318">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b0ec710b6.mp4?token=VqwG6_vdXai2av5vuBEEKn-Eb5otEWhr8RLP_WjA69Hw2HdxMEhi1ubclt3INcoXPyfLcbqOLFGCL-i004vS4Yt2y_94Ll1GOCKhAR9jFMyb_tmL81cVaVmjQuTXbDasr2GJhvncXGDgU65SrBjKrOEwdpuUgMSykLXaLUUAzGiBSYth6fqgOyRIlMhZwlLdX9iSTPTd_XPatDi1IznSYdeo7yTq7JQIvjcfynNAptwhztIVszbLs7FkgdZkq3Ef2Mhvrnsy9lXu8_X11pi2OruT6RX2HEMFEgmMku6Zl0nt-tw11zn9rY-eQ485s7PeaS-MEFggamxaYKne2dSGNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b0ec710b6.mp4?token=VqwG6_vdXai2av5vuBEEKn-Eb5otEWhr8RLP_WjA69Hw2HdxMEhi1ubclt3INcoXPyfLcbqOLFGCL-i004vS4Yt2y_94Ll1GOCKhAR9jFMyb_tmL81cVaVmjQuTXbDasr2GJhvncXGDgU65SrBjKrOEwdpuUgMSykLXaLUUAzGiBSYth6fqgOyRIlMhZwlLdX9iSTPTd_XPatDi1IznSYdeo7yTq7JQIvjcfynNAptwhztIVszbLs7FkgdZkq3Ef2Mhvrnsy9lXu8_X11pi2OruT6RX2HEMFEgmMku6Zl0nt-tw11zn9rY-eQ485s7PeaS-MEFggamxaYKne2dSGNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست:
اگر برایتان سؤال است که چرا حوثی‌ها، با وجود اینکه یکی از نیروهای نیابتی ایران هستند، وارد این درگیری نشده‌اند، دلیلش این است که به مدت ۴۵ روز، قدرت نظامی آمریکا را از نزدیک تجربه کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69318" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69314">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64a849aad2.mp4?token=lbnYfvi25ETZOY_Aql4-pb6KVzZehCBoNn6181pAohIUbKd5ow63VBNtl83n5BeX56nltIp7KEmqB5wjQPFXHWFf5_NmhlqqgDSIElT-wId3iG_ixcIqyrwzlGhOeS2gXZmtGdDNZK17g81Ryb8tzIeZ1YH_5sMtMN46pdaXqAgWClHS6trqxlODFbAGrj34CgEIKIbMQE8ZT7CfVyG58IQHlurWpWyfTkGxTq_x_L0mpl8x2Mlz-nkG5ymb26kOtTfjcikOj8llhxjwLqncXkoiB_Wj3zhWCi5IzjjPzuf3KywGubWWqYLwjP1svtOc9AdWVvdmtC7Cf9YzU9xqOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64a849aad2.mp4?token=lbnYfvi25ETZOY_Aql4-pb6KVzZehCBoNn6181pAohIUbKd5ow63VBNtl83n5BeX56nltIp7KEmqB5wjQPFXHWFf5_NmhlqqgDSIElT-wId3iG_ixcIqyrwzlGhOeS2gXZmtGdDNZK17g81Ryb8tzIeZ1YH_5sMtMN46pdaXqAgWClHS6trqxlODFbAGrj34CgEIKIbMQE8ZT7CfVyG58IQHlurWpWyfTkGxTq_x_L0mpl8x2Mlz-nkG5ymb26kOtTfjcikOj8llhxjwLqncXkoiB_Wj3zhWCi5IzjjPzuf3KywGubWWqYLwjP1svtOc9AdWVvdmtC7Cf9YzU9xqOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇪🇸
آخرین آپدیت از وضعیت اسپانیا:
- مهاجرین غیرقانونی همین‌جوری تو سطح شهر پخش شدن.
- چندین مورد دزدی از فروشگاه‌ها گزارش شده.
- کنترل اوضاع از دست پلیس اسپانیا خارج شده.
- مردمِ محلی گروه تشکیل دادن و دارن هرجا مهاجر می‌بینن، کتک‌شون میزنن!
- تو بارسلون هم مردم دارن خونه‌هاشون رو از ترس مهاجرین، سیم خاردار می‌کشن...
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69314" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69313">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: به زودی، دیگر چیزی از ظرفیت نظامی ایران باقی نخواهد ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69313" target="_blank">📅 19:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69312">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: ایران در تعامل با ما صادق نبوده است
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69312" target="_blank">📅 19:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69311">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14e0b272c3.mp4?token=md_Jc6WNX7NnH6dhfGfL9CfrbkkfN0cbqHKeBLGpUYHziY9tRFkkifNdLo50AeeK0cDjgyswVNR_zd8mGQZwFA3HfcwjVDwtsmYHAYjVpj9qEMIr_jJt42sqiA364uwusNxNkNYg5uNCZam-4gCBi8olnJwub8SY8igdHrpHXXZNUxoqiJOjA2pugrYix90GrXV3xfBi-7izRTYGUgPyKWQrKEGAa_WeP_YZAu02po6IWgqHLmDtAud_KKVB8cqqEbrBswA40kL4ej6-ZC2p4IHcSwLL0pQoXg-xrOijR56Hawdbjcmm4ge_H9qgbrnIsQoQjpaZOfF687xWqOWwfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14e0b272c3.mp4?token=md_Jc6WNX7NnH6dhfGfL9CfrbkkfN0cbqHKeBLGpUYHziY9tRFkkifNdLo50AeeK0cDjgyswVNR_zd8mGQZwFA3HfcwjVDwtsmYHAYjVpj9qEMIr_jJt42sqiA364uwusNxNkNYg5uNCZam-4gCBi8olnJwub8SY8igdHrpHXXZNUxoqiJOjA2pugrYix90GrXV3xfBi-7izRTYGUgPyKWQrKEGAa_WeP_YZAu02po6IWgqHLmDtAud_KKVB8cqqEbrBswA40kL4ej6-ZC2p4IHcSwLL0pQoXg-xrOijR56Hawdbjcmm4ge_H9qgbrnIsQoQjpaZOfF687xWqOWwfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
ترامپ با بالگرد «مارین وان» (Marine One) وارد «کمپ دیوید» شد تا سیزدهمین جلسه کابینه دولت دوم خود را در آنجا برگزار کند.
فاصله کمپ دیوید تا کاخ سفید با بالگرد تنها ۳۰ دقیقه است و رؤسای جمهور آمریکا از زمان فرانکلین روزولت (FDR) در سال ۱۹۴۲ از این مکان استفاده کرده‌اند.
نام این مکان برگرفته از نام نوه‌ی آیزنهاور، یعنی «دیوید» است که توسط خود او انتخاب شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69311" target="_blank">📅 19:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69310">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMieoW43acz60nNSwq-4AwTiJGP-oH6UzSZeuv_lU7NpfmFCeZAk4Jep6mbCYVuQP5SNjIQSt6gmfVTg8vNIktfiFv4KikaSWGWhVj0PKwOMVAQZRpWP6wAJ51f4JACA6SerVxLar768jvLgwlVle7M9mccD8F8NHlinfWNHeduqq_MSeGOrsJTAJQw7RGMy7nv9RcMs41a_UdQOxkF7Vys_UhhL_jce3iDl4LrndYM1bydKfOae4nSJwILyQm9_l9RwkRfPbbJ4qu_ijZ30tFDAQUeEpdKvLgEC2Nt47hJfn1l5SfGRRef6Sr3YPOZQuNxIkO8SwxPVe0fhee0ySQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نهاد مدیریت آبراهه خلیج فارس:
به علت تداوم اقدامات تجاوزکارانه نیروهای نظامی ایالات متحده در منطقه، تردد از تنگه هرمز امکان‌پذیر نمی‌باشد. به محض برقراری ثبات و آرامش، کلیه درخواستها بر اساس ترتیب و زمان‌بندی بررسی و مجوزها به مرور صادر خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69310" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69309">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
حملات پهبادی به جزیره بوبیان کویت
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69309" target="_blank">📅 18:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69308">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31550cb053.mp4?token=JbteBfLfN4awXjQ-i1lhnpP9dahHABkbHB_QdXMAfF82FiXqSFz7tyc8HPtC1Usfn6GLuoF_qmA4DmAspZY7fXFVrpqfmZ2bFcKuaGG9HBH9pB7nwcVLIQfN9Wa8GL3OwIU1ZQs94Xnx4bhRuXKOSpJ983nRi2QyRYxPADM5Z9HX5_DndvgunkeLWM5o4wCMQxFmYmi5rfdhcZUBjewVhfmcLQ1DWVH-UoF-4KZXiPxv9ZKpZ7v2yxeag1_l87FytG8Erj9m3nQDBOx6TTgXj3FxjLWJHtjggz_nvP9GiIIKbxHAjtr6JVrZns3Ub5z6tdEbNSzdD7Ia-MY_hTfyCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31550cb053.mp4?token=JbteBfLfN4awXjQ-i1lhnpP9dahHABkbHB_QdXMAfF82FiXqSFz7tyc8HPtC1Usfn6GLuoF_qmA4DmAspZY7fXFVrpqfmZ2bFcKuaGG9HBH9pB7nwcVLIQfN9Wa8GL3OwIU1ZQs94Xnx4bhRuXKOSpJ983nRi2QyRYxPADM5Z9HX5_DndvgunkeLWM5o4wCMQxFmYmi5rfdhcZUBjewVhfmcLQ1DWVH-UoF-4KZXiPxv9ZKpZ7v2yxeag1_l87FytG8Erj9m3nQDBOx6TTgXj3FxjLWJHtjggz_nvP9GiIIKbxHAjtr6JVrZns3Ub5z6tdEbNSzdD7Ia-MY_hTfyCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس‌جمهور ترامپ در گفتگو با فاکس‌نیوز:
«اوضاع خوب پیش می‌رود. تنها کاری که می‌توان کرد این است که به پیروزی ادامه دهیم؛
آن‌گاه سرانجام اتفاقی خواهد افتاد.
ما ضربات سختی به آن‌ها وارد می‌کنیم و آن‌ها را کاملاً گیج و سردرگم کرده‌ایم، و همچنان به پیروزی ادامه می‌دهیم.
سرانجام آن‌ها چاره‌ای جز بازگشت به خانه نخواهند داشت.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69308" target="_blank">📅 18:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69307">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpQbuniKd50bJyUeH8qsugmadgTY4kLB2DXDXxVGl5cqT30L08WogWnb25aoDND-JcN50J9kNdiZiO_l6iiuppU0RyMKi0-9IVflCVilukFD8DHw4BtH4HMRIScDZuscR93x1cgKpzXKH0GExqeES-W-B4h5MxJnA2QslEK9neBruf8FrNzNWY34Bz_3rZ72FRWNcHANblrP3UhN6T0SBXhKX2w3TAxcSdH6hmgz5ieTCPxH84kkLZqzdqbtZs-Kmo1lWluGGm081tuxlgVo5MbWs8ggMuslq0i0e1M5wJ0zUsp4O0-k2SnGP_pNV5nr9-a4NFWIz9qJP1dKaXwrWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇼
❌
🇮🇷
وزارت دفاع کویت:
نیروهای مسلح پهپادهای خصمانه‌ای که اوایل امروز وارد آسمان کویت شدند را رهگیری و نابود کردند.
حملات ایرانی همچنین چندین سایت نظامی و زیرساخت‌های حیاتی را هدف قرار دادند که باعث آسیب مادی ناشی از سقوط آوار شد، اما هیچ تلفاتی گزارش نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69307" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69306">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4497b03176.mp4?token=fLC_r_ERXcvHkQatcSx4yRtgDIzyiSrndeiPyTNkl9QM8CnZYReLQSMceb7C529lfE4TfC8fT2CkwSh1P_9XBDlCcBUKcgDDxifIDkKTN4CDKh4bpfTHbEQ9YgX8-50bJfcZI_i-AgpsoIAHnriX4ZhMut2QsXUJ-VsOSB3-_9l2fNanV8dKCK1YNZpQRp89wNldrtY8vLAP4_DXLjoYNnKY6vZ1HXhr3Gn-Te_3YDPUlUlpRPrllcRkCTTctsGeMEMd1Jm6vHx0rbkVXOVRA0JFw2PMJgoH7v64F_2AD2ukf6w72ga32ydSluzmhH8YrVbn5H_CjpTrljPy3yxzCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4497b03176.mp4?token=fLC_r_ERXcvHkQatcSx4yRtgDIzyiSrndeiPyTNkl9QM8CnZYReLQSMceb7C529lfE4TfC8fT2CkwSh1P_9XBDlCcBUKcgDDxifIDkKTN4CDKh4bpfTHbEQ9YgX8-50bJfcZI_i-AgpsoIAHnriX4ZhMut2QsXUJ-VsOSB3-_9l2fNanV8dKCK1YNZpQRp89wNldrtY8vLAP4_DXLjoYNnKY6vZ1HXhr3Gn-Te_3YDPUlUlpRPrllcRkCTTctsGeMEMd1Jm6vHx0rbkVXOVRA0JFw2PMJgoH7v64F_2AD2ukf6w72ga32ydSluzmhH8YrVbn5H_CjpTrljPy3yxzCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کابینه ترامپ برای بررسی اقدام بعدی خود در قبال ایران به کمپ دیوید می‌رود.
این خبر ساعاتی پس از آن منتشر شد که ترامپ از توافقی «تاریخی» با میانجیگری مصر، قطر و ترکیه خبر داد که بر اساس آن حماس با خلع سلاح کامل موافقت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69306" target="_blank">📅 17:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69304">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/006b9f5bfa.mp4?token=oxVNYD0b6X00UBsUayhVKJSSrDG8dJJEth2LVMSlf4wIVUBNqJ6l_lAXiutUZZdc-iFdC4h_JBtirQYTDUSJQ4gcBBHzvh2H36kz1CI2UGU1GMdlEoEgFPJPil4uv76lbqndnSXh2OeF_wC9ELPJS-fFceiOyGk_wVITpAeJLATORjz89efBXWl5eOn_JF7iA5XWXfP0_XXtgaTe3x4D4z3zKlmxB0NAs4cLHUIepn7h0H2LMP-7lfna6Wr8w6lj88Y0JeaeIUWozWh88Oh3hUhU1S_r0ddluVt3NxA9M5bVtfN9iMxiy40ueJH8jmbVVKiitIzHhjebIeBQbOdpuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/006b9f5bfa.mp4?token=oxVNYD0b6X00UBsUayhVKJSSrDG8dJJEth2LVMSlf4wIVUBNqJ6l_lAXiutUZZdc-iFdC4h_JBtirQYTDUSJQ4gcBBHzvh2H36kz1CI2UGU1GMdlEoEgFPJPil4uv76lbqndnSXh2OeF_wC9ELPJS-fFceiOyGk_wVITpAeJLATORjz89efBXWl5eOn_JF7iA5XWXfP0_XXtgaTe3x4D4z3zKlmxB0NAs4cLHUIepn7h0H2LMP-7lfna6Wr8w6lj88Y0JeaeIUWozWh88Oh3hUhU1S_r0ddluVt3NxA9M5bVtfN9iMxiy40ueJH8jmbVVKiitIzHhjebIeBQbOdpuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
شهر سئوتا، منطقه تحت کنترل اسپانیا در شمال آفریقا، با یه بحران جدی امنیتی و انسانی روبه‌رو شده.
فقط توی یک هفته گذشته، حدود
1500 مهاجر
با شنا خودشون رو از مراکش به سئوتا رسوندن.
رئیس دولت محلی سئوتا گفته مراکز پذیرش دیگه ظرفیت ندارن، صدها نفر مجبور شدن توی فضای باز بخوابن و مراکز نگهداری از
کودکان و نوجوانان بدون همراه
با
2400 درصد ظرفیت
در حال فعالیت هستن.
الان به‌طور میانگین
روزانه 300 نفر
وارد سئوتا می‌شن و مقام‌های اسپانیایی نگرانن که دوباره بحران سال
2021
تکرار بشه؛ زمانی که حدود
10 هزار مهاجر
فقط در چند روز وارد این منطقه شده بودن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69304" target="_blank">📅 16:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69303">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EfU8z8ZZ--XTpo-fX0qRmU-4ZXVNGC5jBadIAWvu6UU7RL1fb8TeKvSyhrSHGBIGyi7kGPCY1IkbtIKo1NTmbN70eJooPOr0alkBvwkX1jvVDP7xBPbwiDT6-UEgfnqnvV0pNbaJ8upaM4Dmh9oIYvQLX-ipeiMYLoikBPvLjDqfc3PirF-nc2l12QHXSB6k5P06dxBAt4Hx2RM8J8iujg97CotRNpL2bU27fiZiVY9l9W0z71tT01t3w6mJGkAOevsTeQ1RjYbV0aKpmb8Fddoz0VPNxnrHUrNlx9T7Z2zGuM5KvyLgmSk8JdFZp2B5y7Qz1ikA3FYcSEOOKbQaZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پسر رئیس بانک سپه که دهه هشتادیه معاون بانک دی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69303" target="_blank">📅 16:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69302">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_7Nf5oPc0qpPKreJWNTeKfN5KddePsLJd5oJR9TU_D7RfWmjWvPg6XqLAwDArobwIV7QVWj9S6vPHMCfEEoH4gOkq_5Jam41SUOkVeq6-cYVgRrwiXr61AXY-pdMcIh9GUUg5H0vjwOqnDFtmTXnTE1PZATiW2xiFgEla4itSKMmDSqnrV0tV5vX8tHGPJujWdYqH6DobLAwe-NBFMS_UJRST8MebTFcy91kDMaOLNaY5orJmTdkaZgqvZJqeNxXfB9YTViFJ9xcqF6qm4X6U945LY-mT57XEQGmrwpKbzeM3MT3-WDQrpULshOT6V2nF-J4JHUEQlLWjJ3yDcaGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
طبق داده های نت بلاکس دولت ترکیه اینترنت کل مردم رو قطع کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69302" target="_blank">📅 15:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69301">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHiFnRfW8POpjq1k8s8Zv_negB9oHJ69GCtf10XiCBpL2Dq7mjFDnRqeM40Mh5iLJF3fx4VJGzv3u7a-8ToHInZF2ChBAfZreAObxNzxOhnpvnCLrU_JJJWH94whQ4kWATbAcG6YVNUw_V7O8zATfHUqcmlyInJsTFA-jm1nudfRSQWXhfd3vYzERrgZDEwlKzgJRogib8mlP1MviPpvf3hAPHLtQDkf_xE-Y1Zpq9uxnMXYT43LiNPTkIVoVMh9jnFuPe4ArgHBeiv1Fx6gO-FX1hMc7xUAQVeNxHJWXPzHjKvhgbqht3xDAwXPC-rE3VaYJDooVj9H0xPOFHdTFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
گاردین:
عربستان داره خودشو برای یه عملیات نظامی گسترده دریایی و احتمالا زمینی، علیه حوثی‌های یمن آماده میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69301" target="_blank">📅 15:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69300">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🇺🇸
رویترز:
پرزیدنت ترامپ امروز در کمپ دیوید با مقامات ارشد دولت، تیم امنیت ملی و فرماندهان نظامی دیدار خواهد کرد تا درباره مسائل مختلف و از جمله جنگ ایران گفتگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69300" target="_blank">📅 15:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69299">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb0ff0fef7.mp4?token=fW_VUJ8VP88i2xKDDsuvr9q9dHLtTt1Ib5IAKg5rV2459Xi_uL1Cw7E5sY06OljZCHEaShYMeUIhaP_VFyJ3U6vSUWwAvPwMxuEzP42_L0fP5cDw0WA3nB-BerX035WrU0AlVhGvwDXHKU6VxD0dXt3BqfsPRwU6YfgYL409Ckwxn1BpYRq91KmBZnA-HCYjVERU2Uisz_OKHi5ZGFqOUNidK9VA3_eiihiBhNuGkMRqI2c1LJC8qyd1EtXL_XqgxjQM1Jw848hF1kuJB5fvUMA-Z7QwsmkhhJBKPCxauuycRcgdB6ApNu3VjaXq8XyyTU1quxHT1rcbd0paNQaQTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb0ff0fef7.mp4?token=fW_VUJ8VP88i2xKDDsuvr9q9dHLtTt1Ib5IAKg5rV2459Xi_uL1Cw7E5sY06OljZCHEaShYMeUIhaP_VFyJ3U6vSUWwAvPwMxuEzP42_L0fP5cDw0WA3nB-BerX035WrU0AlVhGvwDXHKU6VxD0dXt3BqfsPRwU6YfgYL409Ckwxn1BpYRq91KmBZnA-HCYjVERU2Uisz_OKHi5ZGFqOUNidK9VA3_eiihiBhNuGkMRqI2c1LJC8qyd1EtXL_XqgxjQM1Jw848hF1kuJB5fvUMA-Z7QwsmkhhJBKPCxauuycRcgdB6ApNu3VjaXq8XyyTU1quxHT1rcbd0paNQaQTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
🇮🇱
تلگراف:آمریکا و اسرائیل در حال بررسی طرح محاصره زمینی ایران هستند!
به گزارش روزنامه «تلگراف»، آمریکا و اسرائیل در حال بررسی احتمال اعمال محاصره زمینی علیه ایران هستند تا فشار اقتصادی بر این حکومت را تشدید کنند.
دونالد ترامپ و بنیامین نتانیاهو در جریان گفتگوهای خود در دفتر بیضی‌شکل کاخ سفید، درباره «ابزارهای نظامی (کینتیک) و غیرنظامی (غیرکینتیک)» بحث و تبادل نظر کردند؛
از جمله اعمال فشار بر همسایگانی نظیر عراق و پاکستان برای تشدید کنترل یا بستن گذرگاه‌های مرزی.
یک مقام ارشد اسرائیلی به تلگراف گفت: «اگر مسیرهای زمینی را مسدود کنیم چه می‌شود؟ فرض کنید ایران دیگر نتواند هیچ کالایی وارد یا صادر کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69299" target="_blank">📅 14:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69298">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🇮🇱
وزیر دفاع اسرائیل ، یسرائیل کاتز:
اگر ترامپ از ما بخواهد، به حمله به ايران ملحق خواهیم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69298" target="_blank">📅 14:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69297">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34cbdd236b.mp4?token=cjnfiwd5GjLIprfjPqchpwjoNhB-ndqt0z3N2kHifC5XSmAcT5yvppSn5VRPCedh5ezIlJEPRpk8otEq6hujuOGYg9ppNj430zpQbC4uo8qUt6KIlslVIz5ifxeQHK7kKPxQY-Pv0EzVb9Lvz5mELymI6ArDhc6e5HATQO2NgCNTpMfckl8ruvybJS7RroknzeJ1QykVYXdXzlBqX8FR_jsbsY95hhmV1W03yp_UISEcza1DRwDE7IOwKBSKM2CH7N_zAEp9-YRZqDxBwSnoOpDNiPoEzKYkEpLBUsJml03ykNEzcZOvy_-n6WX4_g6uhn_ZO7s53wyjU5O-nvu_Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34cbdd236b.mp4?token=cjnfiwd5GjLIprfjPqchpwjoNhB-ndqt0z3N2kHifC5XSmAcT5yvppSn5VRPCedh5ezIlJEPRpk8otEq6hujuOGYg9ppNj430zpQbC4uo8qUt6KIlslVIz5ifxeQHK7kKPxQY-Pv0EzVb9Lvz5mELymI6ArDhc6e5HATQO2NgCNTpMfckl8ruvybJS7RroknzeJ1QykVYXdXzlBqX8FR_jsbsY95hhmV1W03yp_UISEcza1DRwDE7IOwKBSKM2CH7N_zAEp9-YRZqDxBwSnoOpDNiPoEzKYkEpLBUsJml03ykNEzcZOvy_-n6WX4_g6uhn_ZO7s53wyjU5O-nvu_Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو عراق اهو گرفتن بکشن بدن به زائرا
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69297" target="_blank">📅 13:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69296">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37edae9b59.mp4?token=mT1xM_xYBBcJ-l4rVaHQ-F31PWklsB9-MQ6uK4ICkVtVd3ewEHkB6nb0zImNimhPC-zXdhEPPYcnDP_h-8l4MW93S-3-FVDqkigGM0qbwN0MelJeBa1qA-ap-VuLnzGG0MOKV7PQDVREum8H-Y5op6nHrBJYMBUnE-D2aGH9-QI55p8v9igkFxHnYhN9Cdw9MK0BqAbt8MWibplyNtYmoWEDa_PLz9ti_x4xzkV4jk0G_djrocHQbOUILrMio1GrngdeUNDPnePDV0ThSGWkQ9jRKkeE2bN58lNEUJTtTjuvuc6UVi_yVfJqB4KlG12dq4-1NOtxRaSZ8M5Yfa6tTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37edae9b59.mp4?token=mT1xM_xYBBcJ-l4rVaHQ-F31PWklsB9-MQ6uK4ICkVtVd3ewEHkB6nb0zImNimhPC-zXdhEPPYcnDP_h-8l4MW93S-3-FVDqkigGM0qbwN0MelJeBa1qA-ap-VuLnzGG0MOKV7PQDVREum8H-Y5op6nHrBJYMBUnE-D2aGH9-QI55p8v9igkFxHnYhN9Cdw9MK0BqAbt8MWibplyNtYmoWEDa_PLz9ti_x4xzkV4jk0G_djrocHQbOUILrMio1GrngdeUNDPnePDV0ThSGWkQ9jRKkeE2bN58lNEUJTtTjuvuc6UVi_yVfJqB4KlG12dq4-1NOtxRaSZ8M5Yfa6tTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
روابط عمومی سپاه پاسداران:
ساعات ابتدایی امروز  ۲ نفتکش متخلف به خیال اینکه میتوانند از مسیر غیراعلامی ما، تحت اسکورت هوایی ارتش کودک‌کش امریکا عبور کنند، بدون توجه به اخطارهای ما، در مسیر ناامن و غیرقانونی حرکت کردند که مورد اصابت قرار گرفته و متوقف شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69296" target="_blank">📅 13:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69294">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ey_gTe1GXzfOHN3q0xyLNPCqpqbLwFszUJyM0pL5tq_xVeAFG3WAbvRGXiC8tsRG02rgKtbHvU0RZAuYCSbEk41TX-nhhZ7UXvA9iOZueMlRxwGbHIAnAFG8mislJIrCv9oJwZnZAPDSIy_OJyTEU31hzQGM-JKm8WdN5Zuqrh4J7battAPzmvcBy8YeJ2jbOdKtL84MlRZ4OcgxZCA0jZ3TfLty_Mo5Mx8Nqb__lFKmR05MjrbrrzVbZ6kBeUA_XVivEV3qUziCoHSkQCvz2pjOskdnYYYRFv_LASntrCz0gTePh-1ogFYLuZ5xUZoZKfqACiF8VUT-8EfGrblM2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bb843e99ad.mp4?token=EA5GmnzDLSgYe7pnmorQQvhuzoV68i8PJUhMbikw8VKyjhMzRGXHlp011tBvSTvaKICJQZK3qUnzYd8ZP1mfK6PKPK0mSRtz8kXQv5ENqSOZ9WWzOjc3lMlZ54tzDbKMmWBZB79EnssGyBaoOxLRG9-J6LG8j774BE76XaTA6qQNKtDOjY07NLoR45hzGIWNWWA4yivdxXAwXvKeaQ_qKNIZJwvnEIAHhRfOfJjoKhTArKn4xVyo58igxhc__U1rM9WQ6W-i9gxFkNyYkznWGuddTavvCmVE78gEAclTMEXmDOVEEkHlVKrsb7RtatHg6TG4xIQ8k8T9AXDO7vrTow" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bb843e99ad.mp4?token=EA5GmnzDLSgYe7pnmorQQvhuzoV68i8PJUhMbikw8VKyjhMzRGXHlp011tBvSTvaKICJQZK3qUnzYd8ZP1mfK6PKPK0mSRtz8kXQv5ENqSOZ9WWzOjc3lMlZ54tzDbKMmWBZB79EnssGyBaoOxLRG9-J6LG8j774BE76XaTA6qQNKtDOjY07NLoR45hzGIWNWWA4yivdxXAwXvKeaQ_qKNIZJwvnEIAHhRfOfJjoKhTArKn4xVyo58igxhc__U1rM9WQ6W-i9gxFkNyYkznWGuddTavvCmVE78gEAclTMEXmDOVEEkHlVKrsb7RtatHg6TG4xIQ8k8T9AXDO7vrTow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای توی کربلا در حال پخش شربت دیده شده
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69294" target="_blank">📅 12:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69293">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSeEYitd4_Sqm4mm-ZPr2Q8RiTsZyi_cKu9wzHOY3uiIABgX9KuDJ-aAzuaw0bAOWGNsiGs5y-glFsDVDYTC9Vn4bV7xDHTIGxRO0V7lDnQLM0fye7nMRQU7IwkY6K9-z90OYydMPNWs0LBrnt2jnUVHl_N_vOMTjx1K9XExSDWG5_VDfQqiDZa1yaJUCuWEcpVl0_AaS2lSeKPBfUX3P2fE-VgAdyeM_pH7DUUb_YnrfU01hGncwJuoDWWiMJlLhLmTULxYUk6tLqZJ95Bbw6BMaDxCpX54rokmqUzycHw6znClo5GtVtXhLdJL6xHlDeRSgk6Cr61Ez05Gp7bOtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
گاردین:
یک موشک بالستیک روسی کارخانه تولید پهپاد در کی‌یف را که متعلق به شرکت «ترمینال اتونومی» (Terminal Autonomy) —شرکتی ثبت‌شده در ایالات متحده— بود، منهدم کرد؛ این نخستین حمله شناخته‌شده روسیه به شرکتی با مالکیت آمریکایی در اوکراین محسوب می‌شود.
این کارخانه پهپادهای تهاجمی مجهز به هوش مصنوعی تولید می‌کرد و گزارشی مبنی بر تلفات جانی در این حادثه منتشر نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69293" target="_blank">📅 12:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69292">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mc8LjJdDQEqhSvBKnjkpfHeMNGvwPIoAXbObXETv9z56cX1SLcn5Sv-aStaVpsvWrRuwwWFlWgAH0Dk47ptaXszJnCX5D9KP8CpKysZwOptdp7XQ-LcQORxcP1tuyGuO0K0qY2GMCs7xptW0gpPL2XXXnpTcEO3i7_Eo-qQrRdk3YwLBYW0eO3eCXJeTHLqyZn49p82Wsht9ubFXLkTpxBxvJ0R6rHBQt5SjsraCCOILSFHkDUJbInwN5nrVfttdb7Pg4DNGW4nWVluoh7TDNL-Os5oYUyed6EK3t0e10L1FbHHWeJ7KjEwy6vJewMXhLh9y1j4xPFnZUhPe1OuH4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
باراک راوید:
به گفته یک منبع آگاه، مقامات سپاه پاسداران از هیئت حماس که برای مراسم خاکسپاری علی خامنه‌ای، رهبر عالی پیشین، به ایران سفر کرده بود، خواستند که در امضای توافق‌نامه عجله نکنند و وقت بخرند.
یک مقام ارشد آمریکایی مدعی شد که ایران تلاش کرد حماس را متقاعد کند تا این توافق را امضا نکند، اما این گروه تصمیم گرفت به این توصیه عمل نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69292" target="_blank">📅 11:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69291">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a885a777d.mp4?token=uKAExttwxj6CZLkgW-aY7iPEo2CiO9m8fAqStAC5it1lDUTw9YffJbejI4cuhbtYsAdeIPQp2NtrTRJPQRgQgZNx1g16G_dGZbR7fuU9XKlwqPVeM9yuBsN7YZ0CjXV7s9vx-V1PcWKmcAerF4NUlhzuPAXPCUy-QTK5GQ5CmRj1pKDtt268MlS8-tqKey8FcGNpo9E5RabRIGtf0t4W8fdIcgIz93R7as8uL6gt3Pgd8uRwHk2ZDrevHPB96mM8kNhrANBEFUeV-4h3uAk5K0u8zpsRGbytsDjfifqOc5AHOxBCrjeyiv-rN3uOlHjSsXIqhreDqhPohsJtoWVOhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a885a777d.mp4?token=uKAExttwxj6CZLkgW-aY7iPEo2CiO9m8fAqStAC5it1lDUTw9YffJbejI4cuhbtYsAdeIPQp2NtrTRJPQRgQgZNx1g16G_dGZbR7fuU9XKlwqPVeM9yuBsN7YZ0CjXV7s9vx-V1PcWKmcAerF4NUlhzuPAXPCUy-QTK5GQ5CmRj1pKDtt268MlS8-tqKey8FcGNpo9E5RabRIGtf0t4W8fdIcgIz93R7as8uL6gt3Pgd8uRwHk2ZDrevHPB96mM8kNhrANBEFUeV-4h3uAk5K0u8zpsRGbytsDjfifqOc5AHOxBCrjeyiv-rN3uOlHjSsXIqhreDqhPohsJtoWVOhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدئو وایرال شده از یکی از مراسمات عجیب آفریقایی ها که با شمشیر همدیگه رو میزنن
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69291" target="_blank">📅 11:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69290">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTL2Z3xrBGa4anaE8a9GBDAZSPFbu6XCvNGNdPQ5Vb3crF8lUKkacV8rVz5Nw6LD-zxDpJ3uMw7NvJ3hC3Si3tfBHUtXEEzzsNniZ0qnKPo7fhUnC71dcAH5c9XTNo2q-HIKWhypAlBmaRA1dwclReIAlBvgIsrekuxZ2VhyNHGd396FC9fpIGKhA8g8_AfJP3ewg1bkUxWd7zXYjcAP-W47cxG26ab2F83z0ADqDY4RXeyWPxgJ3JogjjvHecYqj5tb3dKekvqIb79s6sBK-LgQFWPNUvVVU-8V8Gb23UjplwdvolmwVEFkWcBkJNthCe4Ml2OoJO88ve-kvP5Z0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇱
🇮🇷
تایمز:سازمان سیا و موساد اسرائیل در حال تشدید جستجوی خود برای یافتن آیت‌الله مجتبی خامنه‌ای، رهبر جدید ایران، هستند که از زمان جانشینی پدرش پس از حمله هوایی فوریه ۲۰۲۶، در ملاء عام دیده نشده است.
مقامات اطلاعاتی معتقدند که او در این حمله به شدت مجروح شده است، بیش از ۱۵۰ روز از استفاده از تلفن یا لپ‌تاپ خودداری کرده و در یک پناهگاه زیرزمینی به شدت محافظت‌شده، احتمالاً در تهران یا نزدیک قم، پنهان شده است.
با توجه به اینکه نظارت الکترونیکی سرنخ‌های کمی به دست می‌دهد، جستجو از اطلاعات سایبری به اطلاعات انسانی تغییر یافته است.
مقامات سابق موساد می‌گویند که اعتقاد بر این است که مجتبی از طریق چندین لایه پیک ناخواسته که پیام‌های دست‌نویس حمل می‌کنند، ارتباط برقرار می‌کند و نفوذ به حلقه داخلی او تنها راه واقع‌بینانه برای تأیید موقعیت مکانی او - یا حتی اینکه آیا هنوز زنده است یا خیر - است.
برخی از چهره‌های اطلاعاتی گمان می‌کنند که سپاه پاسداران ممکن است مرگ او را پنهان کند، در حالی که برخی دیگر هشدار می‌دهند که رژیم ممکن است از بدل‌ها برای پنهان کردن حرکات او استفاده کند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69290" target="_blank">📅 10:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69289">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9be197f29.mp4?token=G72MJn56RTGadG-UUozSQAYVvcs9bBd17lF8rM13_tFK_vsxOzFe3quEliF-c6jVjD5_7VBH1j9U6P0mlvWxajQszCPNtOxXasEW-7BIOg0-vnFJuHB-GgWsa5v96eSP7SiMD0__K8lJupnX03R8ycTWpiCh1cNJyCCInTh4qUOd6ldy-yRxnnzrGsdXEwgLRFdC6NpQZ6EyHm3KKOPopbOEajBlI-kgNDhVklddVtNntHkDxFRE9lZoiI-W85ggAgEziaQP9IyUNIzTCXek6y_qt0qlxN82U4QTorDJI8DolH_pMsq3p6IxqjSkdnQv2YQREuePPqDYChKOklIN_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9be197f29.mp4?token=G72MJn56RTGadG-UUozSQAYVvcs9bBd17lF8rM13_tFK_vsxOzFe3quEliF-c6jVjD5_7VBH1j9U6P0mlvWxajQszCPNtOxXasEW-7BIOg0-vnFJuHB-GgWsa5v96eSP7SiMD0__K8lJupnX03R8ycTWpiCh1cNJyCCInTh4qUOd6ldy-yRxnnzrGsdXEwgLRFdC6NpQZ6EyHm3KKOPopbOEajBlI-kgNDhVklddVtNntHkDxFRE9lZoiI-W85ggAgEziaQP9IyUNIzTCXek6y_qt0qlxN82U4QTorDJI8DolH_pMsq3p6IxqjSkdnQv2YQREuePPqDYChKOklIN_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از حمله عجیب طرفداران حکومت به بنر ترامپ و نتانیاهو
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69289" target="_blank">📅 09:52 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
