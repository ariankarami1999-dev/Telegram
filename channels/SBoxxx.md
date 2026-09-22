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
<img src="https://cdn4.telesco.pe/file/rmx4GoyjeyIPANEXiOM8RG-fzUkdWHrF2z_r9lJ1u3iHMmIc0PEABf-fU0FnKwUl5UK_UMdKeDhA75leLsiJjvvyZUkrwiP24KVCDa_f4DwL23hqj1gw4EcaYy4VabghMu68RQXTgbraZQiwR4aSFAB4GxXwQSrQMj4-JRVgz5tGXrqn1oHjZptaLY3xBPkQ1xC96EXn-2m7ZwcYjKVbHSzudQ97iUiJs01YBh7vZRXq-Ro-qIHYag07rFzUVigERVX9T_Zb5IM6G6cjmDgERfKg5Gv90XW6thUkXLd4Io5BMVkGYfvd_OXmL1tQzHKv399P31CMhYD7afb4ZEVruQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.9K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 22:30:47</div>
<hr>

<div class="tg-post" id="msg-21113">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ادعاى ترامپ:   ایران در حال مذاکره با ماست؛ روابط با ایران در حال توسعه است.</div>
<div class="tg-footer">👁️ 490 · <a href="https://t.me/SBoxxx/21113" target="_blank">📅 22:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21112">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06862e3345.mp4?token=CXPRNZoVyyZFHCp8wriXWAWS7lm8QYBsmw0SsLTwgxIXcc-05X4h6IchZi-heqCiK4JXi3_qXGl3lB6Tuq8mKsl2tC4-J_e6gTMEEH_lzE3Cga1xD-5zXAz1wJjGByT8jUq5Ni78NxbYd9x-nf2Rkc1zQ0aG1pHzKcRrlDVR6lUT3-w4WDUCuxFXPoT92OWyp2Ejy-EskEd-xmV6e7dMtU6-UpXOUEtcw8uuYCHRLjrq3G-cTUV6nggoxvSa2Z2tNCSL93PBKaNuIG-BwER9kjh6R4vfxg5eIvrKqSmCmCnVfNqk2rzkWj5j-c4ZStrraNRNOuXcatvYojD9NxYLU2JsFknKU4TkohPgs1cjpdaIyKIRd2bzD1tpbgxOU9p4q6nI1TzEY_t2P6PMCekjc9NGFxs8uwxiDQChoM-OLGkJ_Tb6zpxuAxddhkAkd4DIR5TluMFe6Blol1b-OwVVgLF25UVTYPr8O5PM-xC1VKSTTpKc5B4lrQYQX550qzt_qUr-YMzM3VSI01Ml63jTb1cDhzJFq3g-0m1cRXc2k49-Hb5KRWwc_KA_YXwlPJ6ABPMYJ7xFb2pnSwT9fuKd-40jYAPlY0a_zi2gg0TDsh9J34Vnj3R9COPlZlDYKgCzIx2GTeE4vQtQjaBZq-ncuX__LmYPfxTC-eADIHbx3SI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06862e3345.mp4?token=CXPRNZoVyyZFHCp8wriXWAWS7lm8QYBsmw0SsLTwgxIXcc-05X4h6IchZi-heqCiK4JXi3_qXGl3lB6Tuq8mKsl2tC4-J_e6gTMEEH_lzE3Cga1xD-5zXAz1wJjGByT8jUq5Ni78NxbYd9x-nf2Rkc1zQ0aG1pHzKcRrlDVR6lUT3-w4WDUCuxFXPoT92OWyp2Ejy-EskEd-xmV6e7dMtU6-UpXOUEtcw8uuYCHRLjrq3G-cTUV6nggoxvSa2Z2tNCSL93PBKaNuIG-BwER9kjh6R4vfxg5eIvrKqSmCmCnVfNqk2rzkWj5j-c4ZStrraNRNOuXcatvYojD9NxYLU2JsFknKU4TkohPgs1cjpdaIyKIRd2bzD1tpbgxOU9p4q6nI1TzEY_t2P6PMCekjc9NGFxs8uwxiDQChoM-OLGkJ_Tb6zpxuAxddhkAkd4DIR5TluMFe6Blol1b-OwVVgLF25UVTYPr8O5PM-xC1VKSTTpKc5B4lrQYQX550qzt_qUr-YMzM3VSI01Ml63jTb1cDhzJFq3g-0m1cRXc2k49-Hb5KRWwc_KA_YXwlPJ6ABPMYJ7xFb2pnSwT9fuKd-40jYAPlY0a_zi2gg0TDsh9J34Vnj3R9COPlZlDYKgCzIx2GTeE4vQtQjaBZq-ncuX__LmYPfxTC-eADIHbx3SI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روند ساخت اسلحه های دورزن در یمن!
با همین تفنگ های دورزن، حوثی ها صدها نیروی مخالف خود را در هفته های اخیر کشته اند!
ثانیه 29 جالب است. یارو در دهانش قات می جوود اما دارد اسلحه دقیق زن هم می سازد!</div>
<div class="tg-footer">👁️ 958 · <a href="https://t.me/SBoxxx/21112" target="_blank">📅 22:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21111">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">خاویر میلی، رئیس جمهور آرژانتین:  نسیم‌های تغییر به نفع ادعای ما در سراسر جهان در حال وزیدن است.  اخیراً، رئیس جمهور ترامپ اعلام کرد که ایالات متحده در حال ارزیابی مجدد موضع تاریخی خود در مورد جزایر مالویناس (فالکلند) است.  ایالات متحده در حال بررسی این تغییر…</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/SBoxxx/21111" target="_blank">📅 21:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21110">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ffb8ac635.mp4?token=Uk8K-huiIWR22pf_eclml21CbvgJCP8bfV46RY_kDGgc68w-bJccl6oIXlOmrFLlpvjzTun6CvPPka2EEe8zhfvCaYtmjfthk80HKWonTUTtgnbGWx9YYLRqRaPJdB4CY8zvQxg4lJD_6QRy29W65LqP1ZDkeZ5pxJb7ZlLConHGRORrZzQUrxypjTxdx87ZSz1tg_zw1rSwi6asTFbovOGihGVVcDuxr3SW1-cQPAhzkx6RxKfUuQ0UR9ZGaPOG3LUrhOrfeglfwjt7XOs88zKTm2CrL2ww_eXj6X3xQ5m3WpyEfXKo1_3mQs9hIWb4ZaMXdIx9D4H6_yO0o3CcWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ffb8ac635.mp4?token=Uk8K-huiIWR22pf_eclml21CbvgJCP8bfV46RY_kDGgc68w-bJccl6oIXlOmrFLlpvjzTun6CvPPka2EEe8zhfvCaYtmjfthk80HKWonTUTtgnbGWx9YYLRqRaPJdB4CY8zvQxg4lJD_6QRy29W65LqP1ZDkeZ5pxJb7ZlLConHGRORrZzQUrxypjTxdx87ZSz1tg_zw1rSwi6asTFbovOGihGVVcDuxr3SW1-cQPAhzkx6RxKfUuQ0UR9ZGaPOG3LUrhOrfeglfwjt7XOs88zKTm2CrL2ww_eXj6X3xQ5m3WpyEfXKo1_3mQs9hIWb4ZaMXdIx9D4H6_yO0o3CcWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رجب طیب اردوغان، رئیس‌جمهور ترکیه:  باید برابری حاکمیتی و جایگاه بین‌المللی برابرِ مردم ترک‌تبار قبرس به رسمیت شناخته شود و به انزوای غیرانسانی که بر آن‌ها تحمیل شده است، سرانجام پایان داده شود.  از جامعه جهانی می‌خواهم که «جمهوری ترک قبرس شمالی» را به رسمیت…</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/SBoxxx/21110" target="_blank">📅 20:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21109">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گویا اعراب به دنبال فراهم کردن شرایط دیدار حضوری پزشکیان با قاتل امام شهید هستند.</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SBoxxx/21109" target="_blank">📅 20:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21108">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">آکسیوس:   تا ساعاتی دیگر جلسه‌ای بسیار مهم و سرنوشت ساز در نیویورک میان ترامپ و سران کشور های عربی خلیج فارس در مورد ادامه جنگ با ایران برگزار خواهد شد</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SBoxxx/21108" target="_blank">📅 20:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21107">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">آکسیوس:
تا ساعاتی دیگر جلسه‌ای بسیار مهم و سرنوشت ساز در نیویورک میان ترامپ و سران کشور های عربی خلیج فارس در مورد ادامه جنگ با ایران برگزار خواهد شد</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/21107" target="_blank">📅 20:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21106">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">رجب طیب اردوغان، رئیس‌جمهور ترکیه:
باید برابری حاکمیتی و جایگاه بین‌المللی برابرِ مردم ترک‌تبار قبرس به رسمیت شناخته شود و به انزوای غیرانسانی که بر آن‌ها تحمیل شده است، سرانجام پایان داده شود.
از جامعه جهانی می‌خواهم که «جمهوری ترک قبرس شمالی» را به رسمیت بشناسد و روابط سیاسی، دیپلماتیک و اقتصادی با آن برقرار کند.</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/SBoxxx/21106" target="_blank">📅 19:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21105">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">صحبت های ترامپ درباره ایران !  یا توافق می‌کنند یا جوری جمهوری اسلامی را نابود کرده و آنها را میکشم که نتوانند به هیچ مردم یا کشوری آسیب بزنند</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SBoxxx/21105" target="_blank">📅 19:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21104">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64adfd4dd3.mp4?token=MoOgE1rFeCbRuwGWmRstMcxmBhoEXy_lg7wIoYOaKQBg6dIvRwkidWM__KtEWUQmu6GRV3pzdrWTkJrC9WJTTtPXqmCEER5phAkHgpqF-9V_U2tiFrUFWR-Bl1o1WFjiPEClxWD8z5mFi3LQ0uyK5fcVx1P-QMK3NymbBP5zRLLzEMKjwr2haEJH9rEp9D-ojHQXN5HgtZ32QkG_jDo5yKY5eg7rAaJ4Zxq7WNElep4psf6Qsd6Lh8a41l-qv9gYwNAqdPZBEWOn7V735KCRO9zrTGVeAiMaDtMpV0IbToa1vitmv0PiCV4sJXvc0GxPtpLUT9os8cdLcOj1oXbnnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64adfd4dd3.mp4?token=MoOgE1rFeCbRuwGWmRstMcxmBhoEXy_lg7wIoYOaKQBg6dIvRwkidWM__KtEWUQmu6GRV3pzdrWTkJrC9WJTTtPXqmCEER5phAkHgpqF-9V_U2tiFrUFWR-Bl1o1WFjiPEClxWD8z5mFi3LQ0uyK5fcVx1P-QMK3NymbBP5zRLLzEMKjwr2haEJH9rEp9D-ojHQXN5HgtZ32QkG_jDo5yKY5eg7rAaJ4Zxq7WNElep4psf6Qsd6Lh8a41l-qv9gYwNAqdPZBEWOn7V735KCRO9zrTGVeAiMaDtMpV0IbToa1vitmv0PiCV4sJXvc0GxPtpLUT9os8cdLcOj1oXbnnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های ترامپ درباره ایران !
یا توافق می‌کنند یا جوری جمهوری اسلامی را نابود کرده و آنها را میکشم که نتوانند به هیچ مردم یا کشوری آسیب بزنند</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/21104" target="_blank">📅 19:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21103">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ:
در ۱۲ ماه گذشته ۱.۵ تریلیون دلار در ارتش ایالات متحده سرمایه‌گذاری شد.</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SBoxxx/21103" target="_blank">📅 18:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21102">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">یک مقام عراقی به الجزیره:
«به فرودگاه‌های عراقی اکنون دستور داده شده‌ است از فرود هواپیماهای ایرانی، از نیمه‌شب امشب، جلوگیری کنند.
اقدامات انجام‌شده علیه هواپیماهای ایرانی مطابق با تحریم‌های ایالات متحده است».</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/21102" target="_blank">📅 17:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21101">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ولی من هر چه میشمرم، رفع محاصره یک شرط است نه ۷ شرط !</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/21101" target="_blank">📅 15:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21100">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">— مارکو روبیو، وزیر امور خارجه ایالات متحده:
«ترامپ آمادگی دیدار با پزشکیان را دارد، اما باید بدانیم که تصمیم‌گیرنده نهایی در ایران رهبر معظم است و او یک روحانی شیعه افراطی است».</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/21100" target="_blank">📅 15:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21099">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">به نظر من نوعی کرنش در برابر چین از سمت ایران است که نشان بدهد برای حرف چینی ها تره خورد می کند. چین روابط مستحکمی با سعودی دارد و همین چند روز پیش هم مشخص شد موشک های بالستیک DF-21 در اختیار سعودی قرار داده که با آنها یمن را می زند.  در آستانه دیدار رهبر…</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/21099" target="_blank">📅 14:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21098">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سخنگوی سپاه:   اگر مصلحت ملی ما ایجاب کند که در کنار جنگ، مذاکراتی انجام دهیم، باید مذاکره کنیم</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/21098" target="_blank">📅 14:51 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21097">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - Podcast 28</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/21097" target="_blank">📅 14:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21096">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - Podcast 28</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/21096" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 28
سه شنبه 22 سپتامبر  2026</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/SBoxxx/21096" target="_blank">📅 13:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21095">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">— شرکت هواپیمایی ترکیش ایرلاینز، به همراه پگاسوس و ای‌جت، از ۲۱ سپتامبر تمام پروازهای خود به ایران را لغو کرده و حداقل تا مارس ۲۰۲۷ هیچ رزرو بلیطی در دسترس نیست.
تحریم‌های «عملیات سرد اقتصادی» ایالات متحده آنقدر گسترده است که حتی هواپیماهای ایرباس حاوی قطعات ساخت آمریکا را نیز شامل می‌شود و برای شرکت‌های هواپیمایی ترکیه چاره‌ای باقی نمی‌گذارد.
شرکت هواپیمایی ایرانی ماهان ایر نیز پروازهای خود به استانبول و آنکارا را به حالت تعلیق درآورده است.
اسکات بسنت، وزیر خزانه‌داری ایالات متحده، گفت که خطوط هوایی ایران از ۲۳ سپتامبر با تعطیلی جهانی مواجه خواهند شد و هشدار داد که شرکت‌هایی که به آنها خدمات ارائه می‌دهند، ممکن است در معرض خطر از دست دادن دسترسی به سیستم دلار آمریکا قرار گیرند.
ترکیه یکی از آخرین مسیرهای هوایی بین‌المللی مهم موجود برای ایرانیان بود.</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/21095" target="_blank">📅 13:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21094">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ولی من هر چه میشمرم، رفع محاصره یک شرط است نه ۷ شرط !</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/21094" target="_blank">📅 12:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21093">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4lLWAk5pN7nwm794q6FbtOJMnbzmLJZXsVuO9lnEmkIvE3u3bLIq09yVRqY2gFF5TBn2aKk6WQSZruPgSGCO6xeo6Wx0SUnLByBjNPU6aYgkjlYIq34stdF_5pgosSkHCRjuNk3F3PXP4e_ph_ybFSTCyGUEEuMAaj6N0CWpTuTsYsegvEscEdwoK5NuleNpPclH2mIpj5lIYfWA8LGQ9d1jsXRGYf1F8sT_GBUSEpOF7uTcbTZcyRmHB1RaA6TMIXmQJTRTSMlYUCFpnAvSZ_lB34KM0SYF6QtmZ9eRKvioX3uXwGGWlv4PLUk7rzhd1eCUOjDKPpXCDMsPTpc8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران می‌گوید تنگه هرمز را مشروط به رفع محاصره ظرف ۷ روز بازگشایی می کند.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/21093" target="_blank">📅 12:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21092">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l77-EeM--tMkLtUYHFV9XzibwQ1rqmP7WcidYBbBoZMqYXJVG9AN6eEILJZsFTGTR3UIVL7ga2ljK7CO-6Y9yfKwxql42ePcheVX57xoF4hKj0Q34IcNsxFHfaqxT4xwfpk1G4yRgkPCyjjOMOELyYZM8GgbmTY0UTlGuRSRSDbgz_zV2gAJrKsht1MdMZEmLkZBpGG1_1LOLqGaSat2IPdlrK-YI81t6qI6wSf69TymZRv5frJUPAE6ZOONhmXVtn1-9TDqL4iiHTgWzNqGmd5hm4fYeaPxuXdaJL6B7qeWcvcjfP5XU90-koxiTJzaymf6i-Yhqa2fcaqWZ_ZfeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سه کله پوک پیمان مکه کم بودند، حالا وزیرخارجه مصر فقیر (خر دوم از راست) را هم با آن ریخت و ترکیب ش add to group  کردند!
فقط سیس هاکون فیدان !</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/21092" target="_blank">📅 12:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21091">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJ-AD6B_jssTLoNaqNBVX_MCvK3N-zJza9lIATpvQLXpj8L8zYLl0LpaJrD3XYISvEVxkczLj1hlaAA6t-2jui9r0xJPG7a7qX4jAQGn_HE8IHU3i1uwctXacQADlCH4V1Pd9GWADtskOTJGGRjbizrjwzmEHl6R9oYkrMTGGp3uqcH6_dZi5x-cVwMwbq0imU3WPhntf-TJIKY2oFTqJGya6-GGk_mPf-jHaE-s3reBw6hZ4j0tQoaxcL8ShZFHp6GA8j8RHo8QoC-QPmij9CRX7L9-xsklkrhlBAAii_HKWS1d612K0_EqxkIp1rl3GgLJnk4ceJqBhU80M469jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه FVC کماکان زیر محدوده منصفانه است و هر چه افت طلا بیشتر بشود برای خرید ارزنده تر خواهدشد.</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/21091" target="_blank">📅 12:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21090">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">به نظر من نوعی کرنش در برابر چین از سمت ایران است که نشان بدهد برای حرف چینی ها تره خورد می کند. چین روابط مستحکمی با سعودی دارد و همین چند روز پیش هم مشخص شد موشک های بالستیک DF-21 در اختیار سعودی قرار داده که با آنها یمن را می زند.  در آستانه دیدار رهبر…</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/21090" target="_blank">📅 12:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21089">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">چارت نفت جوری است که به نظر یک کاهش تنش داشته باشیم و دیدار شی-ترامپ مثبت باشد.</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/21089" target="_blank">📅 12:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21088">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ایران می‌گوید تنگه هرمز را مشروط به رفع محاصره ظرف ۷ روز بازگشایی می کند.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/21088" target="_blank">📅 12:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21087">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامپ می‌گوید توافق با دانمارک، «کنترل دائمی» ایالات متحده را بر امنیت گرینلند تضمین می‌کند  ترامپ می‌گوید توافق گرینلند، رقیبان ایالات متحده را از ایجاد پایگاه‌های نظامی در آنجا منع می‌کند</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/21087" target="_blank">📅 12:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21086">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYinTfyKuDi_9aPn7wKa0PEBR3cV2jEu-wyGXnnYbjklI_0jzgxyPLL5loHRZuEasBo-rZKCVUfmjk1AlRsoBOcwPY8XKbUBhvGjPmxOC6v6dF19z0xXE7wl7PDXwEPFs24C42_xUQCeoYSXiS_x0LbcRDynnn-Gjpmk3mKcNp5ldR755vGdeOiVKOtZj7bLUTpjs-6AEQ6Zbx56q9Ymfefjxw9GaeUPqgE90LVTjIQ-rwOgxN6zdIWtEFlDER9lWboaXQBvBwphU3XzZkklqm2rx0HuKyr3mfj5-hTlecES0bpH5izjpgD38qiO3jXOVIZxenkZQ19qGHlW2gO47A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC کماکان زیر محدوده منصفانه است و هر چه افت طلا بیشتر بشود برای خرید ارزنده تر خواهدشد.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/21086" target="_blank">📅 11:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21085">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_h7y-9Bit0zCwEhJwNHYb2ShdEiyhRkGwhg5O0xVrgKtbG7f3zQoZPCsM3fga_bNOLDZrEgrCeNRobyoH7MA2EPe4wsHgpVS3Lh5czc1cU6od9ibPbqrOyf_Vi69hWQHCFJlZ6lzG-TANjDCE0H5VJnwKX_7VEtwnp0kLxrkAxl3YAJ73sLvTulHhqumFroqABCej67cZ1t3ez9U5BmoGtZ7Dgnp5dbW5zpYfPyf0HGbMtTtEMYV5EHMGv9rJpZN2E8m6PgkVts2C4O0ZUELbsHHHA7-d4rTcnr3JxqkwZWI_RBe9oLh7rrzMRuf3J5Wk99pRg5LXfhvnqAsuPYCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح بسیار بالایی است. اما نظر به ریزش سنگین طلا، اثرگذاری اش را گذاشته است.</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/21085" target="_blank">📅 11:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21084">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxb1Ed9I7_YmHeT9Jtnf3ATRX0tTCttvdEkUC0FGkoj6Y6lgIPXlgg1wIYWJh21E_9EFQXPoaHEBmky4P5EAglrY9YEuyvkbwgPBn-49rt4k8R61o9yJKYEHMH80dYnZuyQ7y6gwV6TLGMeHJ2X-gqrnx4uLOSAHz8trz9rG33-U5AUSAhCu90HcG3L03Wd0E55Y98gJjR0Bjqp1wkCw4tLPjlOh4bmic33PzyCqRQDkN2xpVKW9xXbn13rIYffyWJ0LxtZzPsAV0f0yHCF2hDbILdyT0ikdpCWbLFCqB0S_w29n5x1AaHKjBPrdDUeSSdisaXMbxKus4q_CZCDkdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک پله خرید طلا توصیه می شود.</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/21084" target="_blank">📅 11:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21083">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">کاخ سفید، پخش ۲۴ ساعته‌ی «کانال تلویزیونی ترامپ» را آغاز کرد
!
کاخ سفید، پخش مستمر
«کانال تلویزیونی ترامپ»
را از طریق یوتیوب و پلتفرم X (توییتر سابق) آغاز کرده است و وعده داده که سخنرانی‌ها، اطلاعیه‌ها و مهم‌ترین بخش‌های فعالیت‌های دولت را به صورت "به‌روزرسانی لحظه‌ای" ارائه خواهد داد.
کاخ سفید در پلتفرم X (توییتر سابق) اعلام کرد: "شاید همه لحظات مهم در تلویزیون شما پخش نشده باشد، اما اکنون این امکان وجود دارد."
کانال یوتیوب، این پخش را به عنوان
«پایگاه اصلی»
معرفی می‌کند و وعده می‌دهد که مهم‌ترین لحظات و بخش‌های برجسته دولت ترامپ را به صورت ۲۴ ساعته ارائه دهد.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/21083" target="_blank">📅 11:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21082">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sp_Em6Iv1JfECJAMUVSuhdgxdJQvKlzz2ugl3du_2La1W7Y73w0csBirII1rNG5ajEZgU3CzMmmXobEOlDm9IrTuAP4-he5LER1D-QJy9fcV-V_uVMl_w8t9Ub5xU5JKijopTwJhqNruvfe4u8gjxaJQPV_E2bOJ5UGrwd5Jx7VrX94fMm6z4JZ8DLeJLuumAv7LnrpSoMu9QWsHkmJ0XLoghYjUYRPSFgdSdznlxHXrMqH_IlNKlSNJbK38kqM0PVz37mEpSGtmW81oNkjYWYbX7O82uBF8Uu1-_traBzo-MnQLgaSbA-CafWDkwU2oBbIeVqmM2wsKgzWpoHQ5BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح میانه ای قرار دارد و با توجه به افت بهای طلا، به احتمال زیاد دوباره حمله به سقف جمعه و حتی فراتر رفتن از آن را خواهیم داشت (یعنی بالای 4400)</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/21082" target="_blank">📅 10:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21081">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JS14if3DG4DOauBQ2IztQm7tOyfuPydwuSqqjKqFdQqlA0ECkP4jHwcAp7ZFD045x2NsrIKgRazDaktePncqR1KGjlbn3GQsCrwp9zw3PwjQIrftArLNl16I8bKUHzUG9EXh8SStLCdYpB9a-c5ot9EBQ95XzZHzu9CfZLvT8Pmsbv1hWxIF__xN-DYfxakhODyQW3KIn7VnEMsuXXCFBhZ_Io6Sw-KubMsVvxxOa-ES8llpRREyFuar-L3kGd_LoHgzbO-GRa9lAE9F-XhkNnywiLLKI3TnEEmCfqJS4JalRj6NSvCxoVLpn1ZDWOhhni4fjHrbqhctv5x7ob0wRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمونه ای از جامعه ای سرشار از زور و ریا!
حجاب اجباری بر سر دختر می کنیم تا در بلوغ و بزرگی محجبه باشد اما همین الان مادرش بدون حجاب است!</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/21081" target="_blank">📅 09:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21080">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">رئیس‌جمهور ترکیه، اردوغان:
ما آماده‌ایم همکاری‌هایی را که با ایالات متحده در حوزه‌هایی از جمله انرژی هسته‌ای و LNG، حمل‌ونقل هوایی مدنی و فناوری‌های پیشرفته برقرار کرده‌ایم، گسترش دهیم.
توسعه بیشتر صنعت دفاعی — که به‌طور سنتی یکی از قوی‌ترین حوزه‌های مشارکت ما بوده است — هم به‌صورت دوجانبه و هم در چارچوب ناتو ضروری است.
ما می‌خواهیم موانعی را که هرگز نباید بین دو متحد وجود داشته باشد، پشت سر بگذاریم و شتاب تازه‌ای ایجاد کنیم.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/21080" target="_blank">📅 07:51 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21079">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4KlgWuWhsb1IPqEdRuXyG4FHnOZzjPUe1f0BK6zjBmdMf63UmoP8nxO_LWfJ4w09zoblfJ1okIS_mCe4Cgz9LHl0IiODRE_rSyc6O1c2XTuUhpXYd8uiH985_8I3BXcWL4yWSl4epJ3Dobbf62qdzCFJzZkIOG7q8fMvfEuxtU0sHzJjIjgggueuIm-Xd3zuAOeBKmB_JeheUVigwlhwBL2DCJRiva-m_PP-Rmy4AAjHCqJxnt44MNcKq4bWXUpkfRJq2ssMN1u8dsMb1n4IitoD_diaomsspjvu6ulRzfkPm3Rtt7QIAIJzAjzxc1aK14B3GnZo24B2ZCtXdZ5sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
دلار، نفت و موقعیت های معاملاتی گرید از دید موسسه Danske
موسسه Danske با توجه به رشد اقتصاد آمریکا، سیاست انقباضی فدرال رزرو و اثر شوک نفتی، تداوم قدرت دلار و فشار بر یورو و پوند را پیش‌بینی می‌کند.
در بخش معاملات گرید،
GBP/JPY
به‌عنوان یکی از سناریوهای نزولی مطرح شده و ترکیب تحلیل بنیادی و تکنیکالی، افت قیمت تا محدوده 181 را مورد توجه قرار می‌دهد.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/21079" target="_blank">📅 00:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21078">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">— ضرب الاجل دولت عراق برای خلع سلاح حشدالشعبی</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/21078" target="_blank">📅 00:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21077">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">هند نیز‌ به محاصره هوایی آمریکا علیه ایران پیوست؛ گزارش ها از توقف پرواز ها میان ایران و هند!</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/21077" target="_blank">📅 00:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21076">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">هند نیز‌ به محاصره هوایی آمریکا علیه ایران پیوست؛ گزارش ها از توقف پرواز ها میان ایران و هند!</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/21076" target="_blank">📅 22:07 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21075">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiAuG4mbYCcaPQ9G483xqemqc-D6nL2G_spPDfrc77eOZm-kd6F6AU0U2lTQJPhX86SDJc1_IU54WugyV5Cjz7E7Ob9bOkvofdlESqjYFynyLxC0JRCLgNZUZ5dDiZOr13K7JhpF1cNnaoZd70XL9LMgVIsoIl9Bbm3DocZK-8mLCUSVa3cCehOAjRTkyv3JGEL4yQuDJB2V_v4UMi11R2r9Forj6TWkmH50e-NnFqaoJBDXdFnW9bfz5u-Dd4APH_w_OLmIbAfC5VERDumi-_kfHPC7U0t16JAigZ3gaNcI4INqmkYTySihC6EYsUtCUsEe6AOO9_ofgwy9lHUXgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت !  فکر کنید پزشکیان بتواند آن ماموت ۱۵۰ کیلویی را با دستانش خفه کند!  اینها شده اند نخبگان ما!</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/21075" target="_blank">📅 20:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21074">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">رئیس خزانه‌داری ایالات متحده می‌گوید تمام خطوط هوایی ایران در ۲۳ سپتامبر «بسته» خواهند شد</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/21074" target="_blank">📅 19:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21073">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKSQnL9cgX86bdDSnUqS-vijenFbNyQ80oW_c0yChiNv3jbbCpuvSOSZPirHLfrKbjjqmqyh-0fc4X8-cj3B-kvWc4MqIMbGyLmZYtigpOkrzxjs9F8HPwTSTaikgbUUHzEpVX6qt2vOWkOb89AP5Cd_QCcugdxp15P3TAvw3hG8SHvdWr1cQV7Y3xX7PLv9WBua7WvjjsfIMllbAvQB-r2I4zauZyfzMujJhaOnU5IsQOp1DrbzFgND5qQ1F_Ly6BBDYddU1CVSgG5P5R8pKmlOFwvfvppShrrOHaTXrAeov4itumB-YVV6rmPMnC5FOsOaY9vjj4NssdmlU92pFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت !
فکر کنید پزشکیان بتواند آن ماموت ۱۵۰ کیلویی را با دستانش خفه کند!
اینها شده اند نخبگان ما!</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SBoxxx/21073" target="_blank">📅 19:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21072">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اظهارات جِی. دی. ونس درباره قیمت بالای بنزین:
به نظر من، همه ما باید این واقعیت را بپذیریم که تا زمانی که ایران در تلاش برای ایجاد وحشت در حمل و نقل بین‌المللی است، ما طبیعتاً تلاش خواهیم کرد تا در برابر این اقدام مقاومت کنیم. اما به همین دلیل است که قیمت بنزین اینقدر بالاست.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/21072" target="_blank">📅 18:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21071">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdBTW3iXvMWb-8eY4AkkXvRnYWSjeTvYUZMr-zX0DaV347ul1QeZfejsbcXkO56U2nnm6m6f0TbJz6FBOY-DaUjl-JSb-pwyu6QinW1BDzgcZ6Wq3vW7q6bQCZ5DbUX2IJC-m234DR2ZGGgLyOyUpDjEHogkguUYDReBxVG0R6DRPjMgCv-yvxlBTwm1FfPr-59J9IT7nOR2zmy9xVG2vgbuMiPxuCoEx_UIRmOoNpOsMd40x37inuCGIKodKLdFzZbvWZkw8oRbEF8a1McALFcXkTQq0XM9agulMkdPni9O7qK9P36DJi5Wl1qr0PeX6yndNK5SIkemSfHaGDAzPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/21071" target="_blank">📅 17:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21070">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">درگیری های سنگین میان نیروی انتظامی با جیش العدل در سراوان</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/21070" target="_blank">📅 17:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21069">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">رئیس خزانه‌داری ایالات متحده می‌گوید تمام خطوط هوایی ایران در ۲۳ سپتامبر «بسته» خواهند شد</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/21069" target="_blank">📅 17:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21068">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">جان کیریاکو، تحلیلگر سابق سیا:
اسرائیل هزاران افغان را در ایران با ۱۰۰ دلار برای جاسوسی به خدمت گرفت.
کار اسراییلی ها اینطوری بود:
«در این گوشه بایستید و هر بار که این ژنرال را در حال رانندگی دیدید، یادداشت کنید و برای ما بفرستید.» بفرمایید صد دلار.
اسرائیل هزاران نفر از این افراد را استخدام کرد.</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SBoxxx/21068" target="_blank">📅 13:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21067">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ho-wHjvBR3OWK2iTMmNt7kJk4-ElLXF2IuE4c5pGMhjxX69LuAYa4ZRAzNpOjs_K3nSf4wYNUf7PBjoJGgK0fMiAJ4V6R2mCjPk2RM3lYZ9nxm1iKStbU6T98UDmsYUiCSH2SUqXFkHS8HRV0yYD0Q-tk48ICp88mDkNMG6jCt-Zq8SoYGqkVNGQuPfu4edNp9avaDZgcS-qSSzop1B0IOyaXXiRkc7KmZC2SLy2tGi6UE2Wbr9qNkkw_TvcIDeN4i3zDj1A4Q7oN2VYGgAGOLKjd00yluHTYVohpyJxGWuAOS0f7kkmXg3A2RxnRKE8Gq3DCycr_LK21m_VvVcFdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC در محدوده زیر قیمت منصفانه قرار دارد و لذا فضا برای یک رشد در طلا هموار است.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/21067" target="_blank">📅 11:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21066">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WeUgBxZ-eJXcinMY5Tt-qL9Hb9o37SFV4gGU8WvZ90yil0RWfm_tyg5Q5dFMfEBo9770aZNpQ-6uXHgEtJZ5fCwE2MJCCpiBjZUAF9ClXIyHcMwpP7Tkw4yGQkEVNYHXs70lW-OOkiWwIV5bHEsoV1QLWLut4TgB0Vcny395I0cEu9JbApZIZ1MKUdLuJyf_wVE2TGUpg6NE0PbwWlSPQLGqLBaMmSTr4s-Dium3_TJhaO4SAj5NIwsyIMPVs_Ref9JazI2dlosYpxJlG5pXG3sNly2e0ig0FlHFcKjmii6ajeneikRCYCqpH-D3mVHebgGIvfVXxKXdkAibQ0eEqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح میانه ای قرار دارد و با توجه به افت بهای طلا، به احتمال زیاد دوباره حمله به سقف جمعه و حتی فراتر رفتن از آن را خواهیم داشت (یعنی بالای 4400)</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/21066" target="_blank">📅 11:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21065">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">قیمت متوسط گازوییل در آمریکا برای اولین بار از
۶.۵۰ دلار به ازای هر گالن
گذشت. از ژانویه ۲۰۲۶، سطح عمومی قیمت‌ها (موزون با شاخص بهای مصرف‌کننده)
۴.۸ درصد
افزایش یافته، در حالی که قیمت سوخت خودروها
۱۷ درصد
رشد کرده است؛ این امر احساس بحران توان مالی را تقویت می‌کند. دونالد ترامپ، رئیس‌جمهور آمریکا، تمایل خود را برای دیدار با سید پیش‌وا (پزشکیان)، رئیس‌جمهور ایران، اعلام کرد. با این حال، گفتمان طرفین همچنان منفی است. توافق آمریکا با دانمارک درباره گرینلند می‌تواند گامی مثبت باشد (بازبینی یک توافق موجود می‌تواند یک سابقة مفید باشد)، اما عدم اعتماد بین آمریکا و ایران اوضاع را پیچیده‌تر می‌کند.
مِرتس، صدراعظم آلمان، پس از باخت در انتخابات منطقه‌ای هفته گذشته به چپ رادیکال و راست افراطی، سوگند یاد کرد که در سمت خود بماند. به صورت ساده‌انگارانه، نگرانی‌های اقتصادی به نفع چپ رادیکال و نگرانی‌های اجتماعی به نفع راست افراطی است، و روند جهانی به سوی قطب‌بندی سیاسی پیش می‌رود.</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/21065" target="_blank">📅 11:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21064">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJ54HGTK845AdXFyArzBTsCaCjkaTG2f6LQXepZc9OXxwOqg0Zllt6s2Lou4sTppUGY4VhwbmqR9cOCavpnYk7kbFbecBm-HcJ4J0VVg3KqfmIs1hOwRG13e8xt7QPaysAZbcRT23Hloe3WbN6YGSqI_AUPztOKKd0fRo3KkVBB5bTUFJ_AehVckuNQ6CallpcZxgMZuo7d0U3PbE72MJSjfzg28FBDSGHHcSAG_c5bOkm_gEVvxf2jAWpwFJoO-IEJ-VTSAyxsozP8Svr9VKoQJuVG0-tGEHlq6KJxSUeTC3eIfa-nHpN62N2skzrAYPrpD76fVHqmkK1X3i8A6zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چین میزان اوراق خزانه‌داری آمریکا را به پایین‌ترین سطح در 18 سال اخیر کاهش داد.
چین بیش از یک دهه است که میزان دارایی‌های خود را کاهش می‌دهد. این میزان از حدود 1.3 تریلیون دلار در اوایل دهه 2010 به 618 میلیارد دلار در حال حاضر کاهش یافته است.
این کاهش پس از سال 2022 تسریع شد، زیرا چین نگران وابستگی بیش از حد به دارایی‌های آمریکایی شد.
دولت‌های خارجی، خرید اوراق خزانه‌داری آمریکا را کاهش داده‌اند، در حالی که صندوق‌های تامینی و سایر سرمایه‌گذاران، خرید این اوراق را افزایش داده‌اند.
کاهش تقاضای خارجی، به افزایش نرخ بهره اوراق خزانه‌داری کمک می‌کند. نرخ بهره اوراق 30 ساله اخیراً به بالاترین سطح در حدود 20 سال گذشته رسیده است. افزایش نرخ بهره به این معناست که دولت ایالات متحده برای استقراض پول، باید مبلغ بیشتری پرداخت کند.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/21064" target="_blank">📅 10:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21063">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ملونی ممنوعیت پوشیدن بورقا و نقاب را در مدارس ایتالیا اعلام کرد
«هیچ‌کس در ایتالیا نمی‌تواند تصمیم بگیرد که یک زن جوان باید خود را پنهان کند. برابری بین مردان و زنان نه در خیابان‌های ما و نه در مدارس ما قابل مذاکره نیست»</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/21063" target="_blank">📅 10:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21062">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اقدام بی‌سابقه دولت الزیدی:
یک “عراقیِ ارمنی‌تبار” سفیر عراق در آمریکا شد.</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/21062" target="_blank">📅 10:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21061">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajYQec_vSXJjxjhkaPxDbyf6xBkLbqzPF-sklEHf5K1sHmtpC9jc4Cxoyg_QQPDX5vV1nvaEdqW2DeZ6gq2JKgSHqLfiu-kIjPfmnmi61G3cWANN-xyG55SsyH02-GSoDprCsOcU63e1HBRrUQaJVtBl_7ALDnGpAqTfW-ySQ_Wui59y66JfCSFVm7DhqMSVdEGsg6HxqcJ0UsehwfgzRYXNTLPNtadwG-VXZCM2TrqegpMgNvkO2Oli6c56nFM-uqfkbNRzn3xZce0RjhOKbv42YXW8wQCPlQ_CuA5vLXMwnP5Sy_dTiBd0G2D3Vrxj0ieQSE5EWbDCirBZq096qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیده شدن یک هواگرد ناشناش در آسمان تهران امشب</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/21061" target="_blank">📅 01:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21060">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">یعنی همه چیز دیدیم جز قهرمانی....
هعیییی</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/21060" target="_blank">📅 01:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21059">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دیده شدن یک هواگرد ناشناش در آسمان تهران امشب</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/21059" target="_blank">📅 01:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21058">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9e029fb89.mp4?token=krRuIZB7kEz5vps0G7_uZMJKtUAb8dIbHMytzKEIfcPhQcvqzlpDJb_xQW9pYHs8ObFq6c90daeSJkLOLfBuYuRmqzyreb9obQCvGKYVVxZTi0E14SFpucPhns-Wrp0pJIkCgu-luT3WdiCPn18GfoDkRUg3j5EF2JXDpUgaskKUgfhLRl9aJpQ3JbpIYm8fv0UhTcsK_rPhcFPIEZUqcsPV6W_M_Q4jxLlKO0IntosuvyLSeiJjkGECQqtiBvbelgieb9uZXU7kMDND7WzpQ_4XjRIt4W3mxdE1uHMCMeGoF5JJJekO-bw5VmA9fAawaN5qq-o1a8k0_mEf5LbIUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9e029fb89.mp4?token=krRuIZB7kEz5vps0G7_uZMJKtUAb8dIbHMytzKEIfcPhQcvqzlpDJb_xQW9pYHs8ObFq6c90daeSJkLOLfBuYuRmqzyreb9obQCvGKYVVxZTi0E14SFpucPhns-Wrp0pJIkCgu-luT3WdiCPn18GfoDkRUg3j5EF2JXDpUgaskKUgfhLRl9aJpQ3JbpIYm8fv0UhTcsK_rPhcFPIEZUqcsPV6W_M_Q4jxLlKO0IntosuvyLSeiJjkGECQqtiBvbelgieb9uZXU7kMDND7WzpQ_4XjRIt4W3mxdE1uHMCMeGoF5JJJekO-bw5VmA9fAawaN5qq-o1a8k0_mEf5LbIUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیده شدن یک هواگرد ناشناش در آسمان تهران امشب</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SBoxxx/21058" target="_blank">📅 01:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21057">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/304c99ed1e.mp4?token=poE2ev8xshEOAEtBHjH7hpORBLaKVXpGYbj-nZurBpMueNmb5tYgvaTj0SQYmu_HjfUPGp1Tv1z7ec192N9teP7zVlgoe0zdrBnsEDjAmUm7ER2I7Hd0741b-YKjcP0gd55SGkvDmjwSANdO8ELmdOmyp5CpU3uXRtt35aTq_1Zvo7zMyEeujhAqKjd8yHqnuL6NWhhc_-vPP-85OVqhx8FyZk6PRPg37l5M9GcKCu1C6P5oZyGPRc4-61dq8A99IMDdVCA4ZzY-ONPxDjWjpAyvFFqmOmrgalHR4w1U2DaBbswF5vbH_5ZNu6mLayUSvm0TSvgt0vNAx8Wn8lHOMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/304c99ed1e.mp4?token=poE2ev8xshEOAEtBHjH7hpORBLaKVXpGYbj-nZurBpMueNmb5tYgvaTj0SQYmu_HjfUPGp1Tv1z7ec192N9teP7zVlgoe0zdrBnsEDjAmUm7ER2I7Hd0741b-YKjcP0gd55SGkvDmjwSANdO8ELmdOmyp5CpU3uXRtt35aTq_1Zvo7zMyEeujhAqKjd8yHqnuL6NWhhc_-vPP-85OVqhx8FyZk6PRPg37l5M9GcKCu1C6P5oZyGPRc4-61dq8A99IMDdVCA4ZzY-ONPxDjWjpAyvFFqmOmrgalHR4w1U2DaBbswF5vbH_5ZNu6mLayUSvm0TSvgt0vNAx8Wn8lHOMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مستندی جالب از روند ساخت و امکانات شهر موشکی یزد!
بخش عمده اش به نظرم با واقعیت همخوانی دارد اما در بخش هایی از تخیل استفاده شده مثلاً بخش مربوط به نمایش طبعیت و روز و شب برای کارکنانی که 500 متر زیر زمین حضور دارند.</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/21057" target="_blank">📅 01:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21056">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e37KCCoCCvQGJp0h56fB_DsAdZX6tTmJCIm5HC3qrDJjvhfbWBUMeBlp_lpARZqCygoZxPp0mFIUn7ORIx0zizTWpINaha-BFKWShTcUcoAIPdPH0Qhzr84EpQTfU-4cCT_EGueI6KXSv1MYhIM06kJchxN7HIfisSm6eqpP8GjfFZdUhs-SupgK-hbu1vm0GXc0oTLSztR_WyNPRP2oHFMC76pGe6nGoAp6-mNuWoZt4mrmAoHTAxYx5zeyJfJUvIOZXvO3ncwxRH8lsF1b1LrdKSM_1sa0_NAKTRwse7P0d4WVUFy2awmfrTNeDr5nF9p7vbUqx6gXxL6JvshCfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ می‌گوید توافق با دانمارک، «کنترل دائمی» ایالات متحده را بر امنیت گرینلند تضمین می‌کند  ترامپ می‌گوید توافق گرینلند، رقیبان ایالات متحده را از ایجاد پایگاه‌های نظامی در آنجا منع می‌کند</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/21056" target="_blank">📅 01:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21055">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">واقعا تا حالا کسی رو ندیدم  که با این جدیت کصشر بگه
😂
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/21055" target="_blank">📅 00:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21054">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7235f04196.mp4?token=CqWdwR1BTw_PnxNvtYef7gagsbTXXvhUYjhdHvLYlb2EhflgMvTur0e6iK4wRKIvmhwMrDYIFdFJolhCQWI0Jxi_NODxIO9I1bE0TRdD0ug7tuZ4J8GN5d0e9kj5i-nLsmc1TjXSZAeVMaRUpIFUluEaChmvVYvBmwJEqJPitR-rt1rEPhRXOZJQ5-Tg26TzsdbGlE_2htkQLPxglORrM6QDo9CnwruG8fKvaPfvHUqBusv1cVBdxikXBmJ5p7Sb7uqF4HRfkdy4PXM9B6C7YxsoYi22YIuzI12GEovzw_70iVfBgdeBLcrzqN0Kn-XREYwhEeS_84zdJnOzCnGJzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7235f04196.mp4?token=CqWdwR1BTw_PnxNvtYef7gagsbTXXvhUYjhdHvLYlb2EhflgMvTur0e6iK4wRKIvmhwMrDYIFdFJolhCQWI0Jxi_NODxIO9I1bE0TRdD0ug7tuZ4J8GN5d0e9kj5i-nLsmc1TjXSZAeVMaRUpIFUluEaChmvVYvBmwJEqJPitR-rt1rEPhRXOZJQ5-Tg26TzsdbGlE_2htkQLPxglORrM6QDo9CnwruG8fKvaPfvHUqBusv1cVBdxikXBmJ5p7Sb7uqF4HRfkdy4PXM9B6C7YxsoYi22YIuzI12GEovzw_70iVfBgdeBLcrzqN0Kn-XREYwhEeS_84zdJnOzCnGJzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واقعا تا حالا کسی رو ندیدم
که با این جدیت کصشر بگه
😂
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/21054" target="_blank">📅 00:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21053">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFdfgyLYRNJMuFERzGohY7ersChwSuzTQ0RpTRKpt_lqLotgTaHQh5Ik8TPsQMZ0NzsUgMxAeHvbW3YLUQxilEf8uxWhc_ik6EDdUcZowT5oOK8t8mkepTQYJlaAYM22DZqD_h58xPw5PKZ3vbkHkfHeceO3nZFJ-MrqZrmgY3geiXjo6nKZDafkZ_7v2upKIbMf8nDjjyCdLFCIk8xzHw7WxY3v9Q6_zASNeKrjvcFYDkC6GxHpmYlNlMJay6NHNFbikjCVRU4khsG895CYCKu9Iwyv_uXni6dSQq8otjjoXbX71ulRbxDhHcDZSsQSpSZivoORDqdXla-WWkCnww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/21053" target="_blank">📅 23:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21052">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">چارت نفت جوری است که به نظر یک کاهش تنش داشته باشیم و دیدار شی-ترامپ مثبت باشد.</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SBoxxx/21052" target="_blank">📅 23:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21051">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovPZMnfXodrN7k2-iWAy2Rfh-kNwO16GlCbHCXuQErtlcTumH93EfDO5Eu3Nd-anSDahwW5hWV0kXaKHiQYi2LrfZikolQsrKdOoeZqtXnmxZkmiSajhLpGSkm24WIahpQsM8PCzEDSCqgF2lpXv5D_H6y8ZFR_cACUc2Tw5gaz-0dmDhCriZRvajs3cqYpzVxiN0ZM5IKG33LiL7M-moi8qD6VApL64KKSRB9ZcBZrHipBhTGqb5yd0KVQNvE2bye9DFsPOYsDT1IQ16f4piq0TKfEkUSKZQQOzClj4LiaFFBf0cK8f5JmTIwqD6MswU3itBPsCTOKWizJAnMgaYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چارت نفت جوری است که به نظر یک کاهش تنش داشته باشیم و دیدار شی-ترامپ مثبت باشد.</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SBoxxx/21051" target="_blank">📅 23:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21050">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">حریم هوایی اسراییل هم بسته شد.</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SBoxxx/21050" target="_blank">📅 21:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21049">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8oEvYwsmQdBf-69RQrN3zFEqQChMMjE-uwjZkHzmc6Ko__ToLo9d-CKgclzjZ5Qjnr2QWoiIaMVHY1VmF_VAFoTMpcZ7NZQj1xd3XWtFlZAaHz3KWIvBbd5UOlczjOayJIff1-Viv_mLZqn1Gi0dqS48G1PwFxgW0qJkgy84R1GvTYMFV-Y6YotTKB3TBns7gX_hxI9VcpgQ3zcAOSfmAyiiYg1p4RTFlwFY8J1C0jIAavE4Rex-Lv6VyDWq7yyyEkCvuERuGbeY_l70kzSbkrznUTzMti7VYJBU-jMQwIlPl7j7CNwjokEaIKTvuAWcYkQr__UL--fnvBWZruN7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان:   صلحی که دشمن تو را به آن دعوت می‌کند، نباید دفع کرد</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SBoxxx/21049" target="_blank">📅 19:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21048">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">قالیباف:   هم میجنگیم هم مذاکره میکنیم</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SBoxxx/21048" target="_blank">📅 19:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21047">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">📌
تخریب تقاضا در بازار نفت و انرژی های جایگزین  شوک عرضه نفت در کوتاه‌مدت قیمت‌ها را بالا می‌برد، اما تداوم قیمت‌های بالا با کاهش مصرف، افت فعالیت اقتصادی و تغییر رفتار مصرف‌کنندگان باعث «تخریب تقاضا» و کاهش فشار بر بازار می‌شود.  در بلندمدت، اختلال پایدار…</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/21047" target="_blank">📅 18:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21046">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDa-PzB6QRXIM4tspwkHUTsxCsQEvItM1V8_nN2rexZnHxnvgTYkPA4k_hOXpHvQrAzITskWjNl3rN2OxQWs1HKCOTD98m55NRTcwPNPp527X8Bp0JukIuTavv8IXajGSJmFiHEptgUBaMuVkXB534B5Y5vFG4YGj73sWBvKsP7tHeByWWC4FQCwYxh_fvXiMIpoS7vo3eNAJX5OfxHYSEahr0qAO_N-RjSzenVK6voTn58FV9EMTrBeogS5XjPYa8o9MafebWgzjmSdz-skxKg0EQNfCQKXRLlXGJdgcmUGacLijRN7Bk-pYNauzO7zNUjeHu-vOKtxBISjVqPNMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
تخریب تقاضا در بازار نفت و انرژی های جایگزین
شوک عرضه نفت در کوتاه‌مدت قیمت‌ها را بالا می‌برد، اما تداوم قیمت‌های بالا با کاهش مصرف، افت فعالیت اقتصادی و تغییر رفتار مصرف‌کنندگان باعث «تخریب تقاضا» و کاهش فشار بر بازار می‌شود.
در بلندمدت، اختلال پایدار در عرضه می‌تواند سرمایه‌گذاری در خودروهای برقی و انرژی‌های جایگزین را سرعت دهد و وابستگی به نفت و اهمیت استراتژیک آن را کاهش دهد.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/21046" target="_blank">📅 18:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21045">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ به فاکس نیوز:  برخی از مقامات ایرانی مانند موش‌ پنهان شده‌اند.</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/21045" target="_blank">📅 17:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21044">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامپ به فاکس نیوز:
برخی از مقامات ایرانی مانند موش‌ پنهان شده‌اند.</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/21044" target="_blank">📅 17:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21043">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">این هم پاسخ ترامپ به چموشی سعودی های مفلوک در نپیوستن به پیمان ابراهیم و در عوض دست نیاز پیش فاکستان ورشکسته و عثمانی مقروض دراز کردن!</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/21043" target="_blank">📅 17:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21042">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ترامپ به فاکس نیوز گفت:   گزینه‌های فعلی که در حال بررسی هستند، عبارتند از: نابودی #إيران، یا اجازه دادن به فروپاشی اقتصادی آن، یا رسیدن به یک توافق.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/21042" target="_blank">📅 17:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21041">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامپ به فاکس نیوز گفت:   گزینه‌های فعلی که در حال بررسی هستند، عبارتند از: نابودی #إيران، یا اجازه دادن به فروپاشی اقتصادی آن، یا رسیدن به یک توافق.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/21041" target="_blank">📅 17:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21040">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ به فاکس نیوز گفت:
گزینه‌های فعلی که در حال بررسی هستند، عبارتند از: نابودی
#إيران
، یا اجازه دادن به فروپاشی اقتصادی آن، یا رسیدن به یک توافق.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/21040" target="_blank">📅 17:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21039">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">رویترز:  در این ماه، ایران فرماندهان سپاه پاسداران انقلاب اسلامی، مشاوران نظامی و تجهیزات مربوط به موشک‌ها و پهپادها را به یمن تحت کنترل حوثی‌ها منتقل کرد.  یک پرواز شرکت ماهان ایر در تاریخ ۱۳ جولای از تهران به سمت یمن پرواز کرد و بین ۱۰ تا ۲۱ نفر از پرسنل…</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/21039" target="_blank">📅 17:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21038">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پوتین:   رهبران اروپایی در روز های گذشته به صورت آشکار اعلام کردند در حال آماده‌سازی برای جنگ قریب‌الوقوع با روسیه هستند.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/21038" target="_blank">📅 17:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21037">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">قرارگاه مرکزی حضرت خاتم‌الانبیا:
براساس اطلاعات دریافتی، آمریکای جنایتکار .... بار دیگر تصمیم گرفته است با چراغ سبز برخی کشورهای منطقه، در نشست مشترکی در یکی از کشورهای اروپایی، اقداماتی علیه ایران اسلامی را از سر بگیرد.
هشدار می‌دهیم چنانچه آمریکا علیه ایران اسلامی خطایی مرتکب شود، تمامی مراکز استقراری و منافع آن کشور در منطقه، بدون هیچ‌گونه محدودیت و ملاحظه‌ای، هدف حملات مستمر، موثر و دردناک قرار خواهد گرفت.
اخطار می‌دهیم چنانچه کشورهای منطقه با تداوم سیاست دوگانه در قبال جمهوری اسلامی ایران، با تجاوز شیطان بزرگ به ایرانِ اسلامی و مقتدر همسو شوند، همگی در این شرارت شریک تلقی شده و دیگر نمی‌توانند از نیروهای مسلح قدرتمند ایران انتظار خویشتنداری یا نجابت را داشته باشند.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/21037" target="_blank">📅 14:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21036">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">فایننشال تایمز:   عربستان از برنامه تحت رهبری چین که بخشی از تلاش‌های پکن برای ایجاد یک نظام پرداخت فرامرزی جایگزین دلار است، خارج شد</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/21036" target="_blank">📅 14:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21035">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">این هم پاسخ ترامپ به چموشی سعودی های مفلوک در نپیوستن به پیمان ابراهیم و در عوض دست نیاز پیش فاکستان ورشکسته و عثمانی مقروض دراز کردن!</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/21035" target="_blank">📅 14:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21034">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">قالیباف:  جنگ بعدی ناوهای آمریکایی را در هر نقطه اقیانوس هند باشند هدف قرار می‌دهیم!</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/21034" target="_blank">📅 13:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21033">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">این تناقض را نمی‌فهمم:   از یک‌سو ناامنی در کشور تا حدی است که رهبر حتی نمی‌تواند یک پیام ویدیویی منتشر کند،   و از سوی دیگر امنیت در نیویورک آنقدر تأمین است که رئیس‌جمهور و مقامات وزارت امور خارجه بی‌دغدغه در خیابان‌های منهتن قدم بزنند.   آمریکا دشمن خونی…</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/21033" target="_blank">📅 12:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21032">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRaefipourFans</strong></div>
<div class="tg-text">این تناقض را نمی‌فهمم:
از یک‌سو ناامنی در کشور تا حدی است که رهبر حتی نمی‌تواند یک پیام ویدیویی منتشر کند،
و از سوی دیگر امنیت در نیویورک آنقدر تأمین است که رئیس‌جمهور و مقامات وزارت امور خارجه بی‌دغدغه در خیابان‌های منهتن قدم بزنند.
آمریکا دشمن خونی است، اما با بعضی‌ها‌ کم‌تر؟
✍️
پسر سوم‌ خانواده تیبو
@raefipourfans</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/21032" target="_blank">📅 12:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21031">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">قالیباف
:
جنگ بعدی ناوهای آمریکایی را در هر نقطه اقیانوس هند باشند هدف قرار می‌دهیم!</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/21031" target="_blank">📅 12:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21030">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBtTILeNFsy_VM7KBJLO_PXhrtq6DKs2xLVLNGIm78gocjXBKJDQ9LXu87cKU93qBFEVRR686fyEytg04ZppPsMWDYBq0sQwdlWJguGDkdjT6EPbid_xKjcgGr9WGW0OsNIG01Jz_yK5S0AYTDro7yzKyLjlRUaDfJv233_-UDW1EtXrLXjkjAsnmHJXGipAi7KBd95Tby3J0jukieXJbDmwCWhbcWvt1pWusMYTPsF4NlcO4cAFcq7gCM0Yro9Re5MWLljFMdHXrUrmDL5mNRFAPgf0olGpGsZzrw1sxdhNpmzLyRUOIMEovW7Vx1VsDTrBrdXSFCcilpSZprmvGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه FVC نشانگر نزدیک شدن طلا به محدوده قیمت منصفانه است و لذا از حالت حباب منفی ارزشگذاری فاصله گرفته است (به دلیل رشد سنگین از پریشب) هر چند هنوز تا تشکیل حباب مثبت و بیش خرید بودن فاصله زیادی دارد.  پس بهترین استراتژی برای امروز:  خرید…</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/21030" target="_blank">📅 11:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21029">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">کانال 14 اسرائیل:
آمریکا گزینه‌های حمله احتمالی به یمن را بررسی می‌کند</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/21029" target="_blank">📅 11:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21028">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ek1ka1NIFbaPXEgNeofXiKs3wlYNMH3w-jYc3G-1SYV-zEKhaU8ZatTD6rvjXh8VcKqBnb1G8DYJf8v9sNnAvapVRsscxGCuyw0JVNzvCtmhsWOJsiPiMQCi7E9lRj0hD1YRgfiOYEJTh_EpAy3pnNO9MEvLM0NP9lS2UIFWdVpP_d8t82tdNEtqErpv38lN7ItVy9Adg2qFNrH8P8BHVlXPBMFn2GoH0sgBqiCSyTNHE4V_szto6Xmu5sBXaf2VLY4WvMnOuSDwkJVoeNva4RqwJjWPpWI7Qc1MvjPyMz6uJp3vKU9N2-D51_HPoUg2Qcpbx0AkCui9PhOgSuVdgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک حمله پهپادی گسترده در طول شب به مسکو و منطقه مسکو، در روز پایانی انتخابات پارلمانی روسیه، انجام شد.  یکی از برجسته‌ترین اهداف، پالایشگاه نفت مسکو در کاپوتنیا بود که صبح امروز آتش سوزی بزرگی در آن مشاهده می‌شود.  ظرفیت پردازش این پالایشگاه حدود ۱۲ میلیون…</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/21028" target="_blank">📅 10:26 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21027">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">یک حمله پهپادی گسترده در طول شب به مسکو و منطقه مسکو، در روز پایانی انتخابات پارلمانی روسیه، انجام شد.
یکی از برجسته‌ترین اهداف، پالایشگاه نفت مسکو در کاپوتنیا بود که صبح امروز آتش سوزی بزرگی در آن مشاهده می‌شود.
ظرفیت پردازش این پالایشگاه حدود ۱۲ میلیون تن نفت در سال است.
آخرین بار در ۱۶ و ۱۸ ژوئن به شدت مورد حمله قرار گرفت، زمانی که هر دو واحد اصلی پردازش نفت خام آن آسیب دیدند و پالایشگاه مجبور به تعطیلی شد.
تا ماه اوت، گزارش شده بود که توانسته بود تنها با حدود یک‌سوم ظرفیت خود مجدداً راه‌اندازی شود.
اکنون دوباره مورد حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/21027" target="_blank">📅 09:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21026">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4607a666c6.mp4?token=X-wUiZFaOmmO4JHO1r9y6Y9WQptr8ROZ-auOFXdQf13GmimS4U4en5nO48gyjLkuQPvP3gLdT8l56M8rfI3NBOaZQX42-6mVSVkZPyR2P4gXN2o5wqeFNetdPMNrHSSF_qKu73620CJ-GgTkCcbOp1RDz6OU2upZ8MJcAXWSRiafcM_L6gqPMdwMdc6XLZGFE5VN7Rv_xVWtQCeOwz2dI-UwVld016JMdO142Ivbm2c-_nGxsTpWQPzhXXNYCbisR8peldUGGSAvz37aCecclUUk2cbIQkh2ffts2c_xSBm2u3NwqBY3yx11F--2O1mezu75rWHOihKak5eOOwidsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4607a666c6.mp4?token=X-wUiZFaOmmO4JHO1r9y6Y9WQptr8ROZ-auOFXdQf13GmimS4U4en5nO48gyjLkuQPvP3gLdT8l56M8rfI3NBOaZQX42-6mVSVkZPyR2P4gXN2o5wqeFNetdPMNrHSSF_qKu73620CJ-GgTkCcbOp1RDz6OU2upZ8MJcAXWSRiafcM_L6gqPMdwMdc6XLZGFE5VN7Rv_xVWtQCeOwz2dI-UwVld016JMdO142Ivbm2c-_nGxsTpWQPzhXXNYCbisR8peldUGGSAvz37aCecclUUk2cbIQkh2ffts2c_xSBm2u3NwqBY3yx11F--2O1mezu75rWHOihKak5eOOwidsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت امروز من در بازارهای مالی
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/21026" target="_blank">📅 09:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21025">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d8265c9ad.mp4?token=vA6tFKJmJluDud5Pbt61CFV2BrP9Wl2_6GrNJqbFM7_mscIAGbbQCq61FePHQui80Kg4MDrlBVK7U9OuOjNpFa7_RzPmgy5SFw2GQGiJlYCAwiU721r0-qGuXAXNbBf8u1Mm_LGsf-_DrrV5N-IBFlTYFZT_8x_Rr9Xixd0WJ1yjYkRfpRFNEfrqXWiXTqLLv41Wmm3VbaflsCTpodnNtV0tFkTan1pwp-V22C9xc8IMTxi_7QvsheoC0zPhnkvnotjzHhlT-gf-AlSlzzJaQj2DuKm1tQdY_DkaEILI_NBRBfeW7IjwL7YmL5QztYeEKX5hv-dGBLWdbiqXTmEsxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d8265c9ad.mp4?token=vA6tFKJmJluDud5Pbt61CFV2BrP9Wl2_6GrNJqbFM7_mscIAGbbQCq61FePHQui80Kg4MDrlBVK7U9OuOjNpFa7_RzPmgy5SFw2GQGiJlYCAwiU721r0-qGuXAXNbBf8u1Mm_LGsf-_DrrV5N-IBFlTYFZT_8x_Rr9Xixd0WJ1yjYkRfpRFNEfrqXWiXTqLLv41Wmm3VbaflsCTpodnNtV0tFkTan1pwp-V22C9xc8IMTxi_7QvsheoC0zPhnkvnotjzHhlT-gf-AlSlzzJaQj2DuKm1tQdY_DkaEILI_NBRBfeW7IjwL7YmL5QztYeEKX5hv-dGBLWdbiqXTmEsxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از حمله موشکی دیروز حوثی ها به فرودگاه ریاض</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/21025" target="_blank">📅 09:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21024">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ecd762d60c.mp4?token=kTDZ2IIUub2caXD4oFZAkh5uSTG0lbEyah1fVI7GaPpy5SFKLRib4NrsNGoXda7fRwHeOng1PWSFqYYEoGBdSq_opbbvhK8FLns0uY4FluTtFLNDYkfah-tUGFRdAdXvPrGpjoYOEaYANygOQ_puLCUcTbYG_NqmtyW16EjtMzz4miSWjhduBEi6dbTYPWvFizzMrTZwWzMaBEHOgnpRR2dgG0oFd0SltiEuFXTGU8Xd6ZHI8lg6kXJncRs3kMVa9m6q6OLMuYcbNMCQh90LdcQXA3iKKV03r_f-OnNra-MTYlvg3UVTqaAQsZrwhqxNNNT3rYxQMtqJlCe82d5P3w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ecd762d60c.mp4?token=kTDZ2IIUub2caXD4oFZAkh5uSTG0lbEyah1fVI7GaPpy5SFKLRib4NrsNGoXda7fRwHeOng1PWSFqYYEoGBdSq_opbbvhK8FLns0uY4FluTtFLNDYkfah-tUGFRdAdXvPrGpjoYOEaYANygOQ_puLCUcTbYG_NqmtyW16EjtMzz4miSWjhduBEi6dbTYPWvFizzMrTZwWzMaBEHOgnpRR2dgG0oFd0SltiEuFXTGU8Xd6ZHI8lg6kXJncRs3kMVa9m6q6OLMuYcbNMCQh90LdcQXA3iKKV03r_f-OnNra-MTYlvg3UVTqaAQsZrwhqxNNNT3rYxQMtqJlCe82d5P3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/21024" target="_blank">📅 08:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21022">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ می‌گوید باسن ملانیا باعث «نجات» هر دوی آن‌ها در پله‌برقی مقر سازمان ملل شد.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/21022" target="_blank">📅 08:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21020">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">وزارت خارجه آمریکا به تمام شهروندان آمریکایی اعلام کرد که سفر هایشان به خاورمیانه را فوراً لغو کنند.</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/21020" target="_blank">📅 02:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21019">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">محسن رضایی:   محل تپه علی طاهر پیش از حمله تخلیه شده بود و عملیات دشمن شکست خورد</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/21019" target="_blank">📅 00:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21018">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی ایران، از آزمایش یک موشک ضدکشتی که به 80 گلوله تقسیم می‌شود، خبر داد.   به گفته ایشان، این آزمایش بر روی یک ناو هواپیمابر آمریکایی انجام شد و با توفیق الهی به نتیجه رسید.</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/21018" target="_blank">📅 00:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21017">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی ایران، از آزمایش یک موشک ضدکشتی که به 80 گلوله تقسیم می‌شود، خبر داد.
به گفته ایشان، این آزمایش بر روی یک ناو هواپیمابر آمریکایی انجام شد و با توفیق الهی به نتیجه رسید.</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/21017" target="_blank">📅 00:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21016">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">موسسه مطالعات جنگ:
طبق اظهارات مقام‌های آمریکایی به Axios در ۱۵ سپتامبر، تعداد عبور روزانه کشتی‌ها از مسیر جنوبی، با انجام موفقیت‌آمیز عملیات نظارت و مین‌روبی آمریکا، به حدود
۴۰ درصد سطح پیش از جنگ
بازگشته است و عبور کشتی‌ها هم در طول روز و هم شب انجام می‌شود.
عربستان سعودی نیز بنا بر گزارش‌ها صادرات نفت خود را بار دیگر از مسیر تنگه هرمز منتقل کرده است. بر اساس اطلاعات منابع تجاری که رویترز در ۱۸ سپتامبر به آنها استناد کرده، عربستان برای بارگیری‌های ماه‌های سپتامبر و اکتبر حدود
۶۰ میلیون بشکه نفت
را در بندر رأس تنوره در شرق عربستان بارگیری کرده که انتقال کشتی به کشتی آن از طریق تنگه هرمز انجام شده است.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/21016" target="_blank">📅 00:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21015">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c95cb0fd.mp4?token=ab7wjwDEiDFkQiGXY7M1Mq4F8xPaT2SSeY2O4pHphqChTe-e0xn2uF_pIArapTWCGeGsx-QEWfykgYNnnWhEUxf2E-0bAH_kvwMJmqOM9PY2jqfJu8Ni8vawcH7U7uGvSx6PKNLi6Z7BDRUoFZdt7z9dLqeoUbejqo_vGbKpwQHy4OpECE9GQUG1jNd12CyTLwhiIs4nTOKTW2tpgVBQaztv3Nw3FzJ-vkNY8oMS0YhyWCaPq0KqedepkYhUmZ6p9IMGApjn1wFwrSRf77VEFyNP2Cs0Fcq6u7PYJ6FhChkzDwxgnpKfWWInt1JvRQuY-j-HIoYzo8fekJHcxpmNWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c95cb0fd.mp4?token=ab7wjwDEiDFkQiGXY7M1Mq4F8xPaT2SSeY2O4pHphqChTe-e0xn2uF_pIArapTWCGeGsx-QEWfykgYNnnWhEUxf2E-0bAH_kvwMJmqOM9PY2jqfJu8Ni8vawcH7U7uGvSx6PKNLi6Z7BDRUoFZdt7z9dLqeoUbejqo_vGbKpwQHy4OpECE9GQUG1jNd12CyTLwhiIs4nTOKTW2tpgVBQaztv3Nw3FzJ-vkNY8oMS0YhyWCaPq0KqedepkYhUmZ6p9IMGApjn1wFwrSRf77VEFyNP2Cs0Fcq6u7PYJ6FhChkzDwxgnpKfWWInt1JvRQuY-j-HIoYzo8fekJHcxpmNWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خارجه ترکیه گفته که ترکیه می تواند نیازهای نظامی سعودی را برطرف کند!  یعنی در این شرایط که عربستان بشدت به نیروی نظامی نیاز دارد هم ترکیه دست از بازاریابی برای سلاح های ساخت خودش دست برنمیدارد!</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/21015" target="_blank">📅 00:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21014">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUKgJupVUAIuG8-UjvC65068x06Kx6aSIGJUkJCq0F2s4cntDQJimXetsVodRouhalkDF9d3WnsWfzxnE9hCNyXnupxW6CVvlVcddXeezdxM2XzPyzQV4x86zi8w2BJUUtv0WLLancqdLLt5ffUIstDbB9g4Xw-jlfQzKErqYunawgKarPdJZBYFg_ZuzBxcu2OmhxH2_kQN9hXdOAXwmMOsPBAu2_b89hAlBkgUMGbReFEXpN4uPnmHfe8AkGV7XH9GyYT8ayvkoPHJskl5gCPCNcKTqF_0xxkUgfhbSIwIeDSH3bmLcOayzrKMxSpjbJcSEGXVRpc8rD08F6nwcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو دفتر سیاسی انصارالله:   این پیام به ترکیه و پاکستان ارسال شد که به خودتان احترام بگذارید؛ اگر از عربستان سعودی حمایت کنید، ما به شما حمله خواهیم کرد و شما را تنبیه خواهیم کرد، و دست‌های ما از فولاد خواهد بود</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/21014" target="_blank">📅 00:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21013">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHlg36ufTQTHACgyb1xZtZEVPx5Hw06Z2PArr3tUcsCQUuc4YiTP6ZE5QxW5UohsDn_mpt8upG3iQ5DZ99UZbHbhFo5wk9HpqmgJwcxPmrzi5stAoER4zpq3rCKiR_QXZyzOXNpuSyk_Le2EZaf2EoMtTxaaSbsSClwDiqiLHKUXhILCMlJRVRGx-zmGGpGo_upLNl5usfvo4h3GZt4FNlwJ0tVzcz91MQ-hE5YKNR1VL6zFJAQNxmYyM2Imjup1wYEX3GOYCZRiGLflTUG4Z9FQoUrL3aGEIcP83A-u74Hsn9UOLyy8Alew9O2dR-CBhViAGNV8En22gOY2s3L6gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی:   خواهان پایان جنگ میان عربستان سعودی و یمن هستیم و معتقدم یمنی‌ها نیز خواهان دستیابی به توافقی با عربستان هستند</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/21013" target="_blank">📅 00:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21012">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">عضو دفتر سیاسی انصارالله:
این پیام به ترکیه و پاکستان ارسال شد که به خودتان احترام بگذارید؛ اگر از عربستان سعودی حمایت کنید، ما به شما حمله خواهیم کرد و شما را تنبیه خواهیم کرد، و دست‌های ما از فولاد خواهد بود</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/21012" target="_blank">📅 00:09 · 29 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
