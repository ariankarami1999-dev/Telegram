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
<img src="https://cdn4.telesco.pe/file/FJrvpWPIZfyRb1Tjfumk2UA7qKznMrc8RPcdeb_QiaruklC7tacA1YT7XxELDrjYu1d2dW77P33Si-_-hkGDZtkf-2iYsFnbvdc2ypAjAPTaSPkn1CuENGU2iV56-i3InAlchjY9P7ARAXaxhfd_79QmO_coqG29B54aOOQF98B7gXfnqfcZANLPPZSAXbUSkBQ-HbTKWsB5Hv0iNUTW3hug9jOjvgUHL2Rf2kBOef6qLszkpcxlWQTxnWLt75jSnJRtH3SAl-h6ZNLzHFrA6y4DP_iSXeN1S75LhzW0gX1XN8ZVnFZlG0kEoiWhRLrP8V8BknfzUKFa1bfl1J0xSw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 21:30:16</div>
<hr>

<div class="tg-post" id="msg-134105">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❌
مدیران باشگاه پرسپولیس برای توافق با بیفوما برای جدایی کار بسیار سختی دارند! / فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/134105" target="_blank">📅 20:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134104">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❗️
پایان کار میلاد محمدی در پرسپولیس؟
✅
طبق شنیده‌ها، قرارداد میلاد محمدی با پرسپولیس به پایان رسیده و باشگاه هم فعلاً برنامه‌ای برای تمدید ندارد. از طرفی، خود این بازیکن هم احتمالاً قصد دارد دوباره لژیونر شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/SorkhTimes/134104" target="_blank">📅 20:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134103">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❗️
باشگاه شاید قرارداد میلاد محمدی رو تمدید نکنه.چون قیمتش بالاست ...سر همین داستان دنبال جذب ابوالفضل رزاق پوره///قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/SorkhTimes/134103" target="_blank">📅 20:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134102">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_6214Tgn5g18Ff1q6JGrP9dF1iVaIMrEGpGxOl6-O2lMwCaH_SjsjfJjidkiwfLmws8mVAOSPGPhEGntGAbGKeYC6723x2X2FAOdOvx8HNfDec8vxxUCvX7tDGmCQSFit-vTjgIu55vsmSRF-V5ucbQ-Q39O6gFV-eUsqDHBZlFS0PTDOMKSpBhw2A3vRl-g4q6q7ss3XEWGw7xff83LLLsyQM8rdNs6MjzSKqkH1l6jlO4NEM2tJnhqHTyqAeLS2bfudDoC0QxDkDoHZjkoXxo7vfrbDwQZJjhwTz23d-96pfNEUWKTg8GuGm5_yN9KGAimY6R2zH3VShNvsZpOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
بازی‌های جذاب و هیجان‌انگیز امشب جام‌جهانی رو با بونوس ویژه وینکوبت پیش‌بینی کن.
🎁
تنها چندساعت تا بونوس ویژه جام‌جهانی
6⃣
2⃣
0⃣
2⃣
همراه با وینکوبت باقی مانده!
🎁
🔣
5⃣
1⃣
بونوس ویژه روی تمامی واریزها فقط با یک گردش روی حداقل ضریب ۱.۸ به موجودی خودت اضافه کن.
⏰
این بونوس ویژه وینکوبت فقط تا امشب ساعت ۲۱:۳۰ فعال است.
📌
همین حالا وارد ربات وینکوبت شو و ازین بونوس ویژه استفاده کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/SorkhTimes/134102" target="_blank">📅 20:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134101">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">⭕️
🇮🇷
اگر سازمان لیگ با تأیید و مصوبه هیئت‌رئیسه، سازوکار تعیین نماینده سوم ایران در آسیا را از طریق تورنمنت سه‌جانبه تصویب کرده، سؤال ساده است؛ چرا هنوز نامه رسمی این تصمیم به AFC ارسال نشده است؟
❌
وظیفه دبیرکل فدراسیون، اجرای مصوبات و پیگیری امور اداری است،…</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/SorkhTimes/134101" target="_blank">📅 20:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134100">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brVGrs7cKapy31KhrcpyGttqSTYaU0WcMvpJMZN6pgv4tNkQnKb8OOiYd37LryYf6PBCHNOxdn8kMqSffVfnJkXsnzUNIRrirCc8J_hlQnRj7DwF4xMLSa5K8w5gMtXUYH4XlviitXgEhvHsvUGKHNbWIBQOEonjSBuZwRNAPfaWouEe1eZ70-YEjyyJB_D1110XeazYwaK4a575y1_UL1NKXCYDCwkgLLazekNHUvRpMx-3BRtobnNKImCj3qiRL9U6qLbN14yXIVBV1VsXyKsitcfCYCBhpku2NTJ0VcxOSO1r-vFH5Gw96eyM8jkHpDjA44n-ecTSd4qsf09gHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
🇮🇷
اگر سازمان لیگ با تأیید و مصوبه هیئت‌رئیسه، سازوکار تعیین نماینده سوم ایران در آسیا را از طریق تورنمنت سه‌جانبه تصویب کرده، سؤال ساده است؛ چرا هنوز نامه رسمی این تصمیم به AFC ارسال نشده است؟
❌
وظیفه دبیرکل فدراسیون
، اجرای مصوبات و پیگیری امور اداری است، نه معطل گذاشتن آنها. هر ساعت تأخیر در ارسال این نامه،
ابهام بیشتری درباره سرنوشت سهمیه ایران ایجاد می‌کند
و حق سه باشگاهی را که باید در این رقابت شرکت کنند، تحت‌الشعاع قرار می‌دهد.
❌
آقای هدایت ممبینی
، اگر مانع قانونی یا اداری وجود دارد، آن را شفاف اعلام کنید. اگر مانعی نیست،
چرا مصوبه هیئت‌رئیسه هنوز روی میز مانده و به AFC ابلاغ نشده است؟
فوتبال ایران بیش از هر زمان دیگری به شفافیت، پاسخگویی و اجرای دقیق مصوبات نیاز دارد، نه سکوت و تعلل.
❓
هواداران و افکار عمومی منتظر پاسخ روشن هستند؛ اجرای مصوبه نباید قربانی ابهام یا تأخیر شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/SorkhTimes/134100" target="_blank">📅 20:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134098">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❗️
با تصویب هیات رئیسه فدراسیون فوتبال بیست و پنجمین دوره لیگ برتر ( فصل ۱۴۰۵-۱۴۰۴ ) به دلیل حمله وحشیانه دشمن به کشورمان به صورت نیمه تمام باقی می ماند و جدول لیگ نیز با شرایط فعلی متوقف می گردد.
🔴
ضمن اینکه براساس این جدول ۳ نماینده فوتبال کشورمان برای حضور…</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/SorkhTimes/134098" target="_blank">📅 19:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134097">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✅
اعلام ساز و کار لیگ برتر در فصل آینده/آغاز مسابقات از ١۶ مرداد؛ تورنمنت سه جانبه برگزار می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/SorkhTimes/134097" target="_blank">📅 19:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134096">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✅
شروع مسابقات لیگ برتر فوتبال ایران سال آینده از ۱۵ تا ۱۹ مرداد خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/SorkhTimes/134096" target="_blank">📅 19:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134095">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eb150d050.mp4?token=IKuAfX1pwkDIrumr3mWyiXsx5GtV3eSD_qc4ZcFPINJxvN5FQs5oCi61VH8s9FFOJFxUAmQqC6UsB3nJIJmvLadxkKV4KEvLP4jkBDx_PB0y16wOFj6uiP3PyrQRMh3m8l3rkMSklNOX5lJd1dcijUgIgWejunYq0ozYuXIWofi_Z0CWyQntcz0fN1NfpGf2bqOZdbD5KReS62NCrmY96MmD3fy-ykeIyW4XgJo8DbM7NkCpCmQvs1bkr34z7O45Pq1DDOceJk1l3CIGYhQm502nVll6f-RIDgeE1pzEloXmYih7p9OlUBk2qqoXo53_OUKcUb6M7DpNNKkzq-rJzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eb150d050.mp4?token=IKuAfX1pwkDIrumr3mWyiXsx5GtV3eSD_qc4ZcFPINJxvN5FQs5oCi61VH8s9FFOJFxUAmQqC6UsB3nJIJmvLadxkKV4KEvLP4jkBDx_PB0y16wOFj6uiP3PyrQRMh3m8l3rkMSklNOX5lJd1dcijUgIgWejunYq0ozYuXIWofi_Z0CWyQntcz0fN1NfpGf2bqOZdbD5KReS62NCrmY96MmD3fy-ykeIyW4XgJo8DbM7NkCpCmQvs1bkr34z7O45Pq1DDOceJk1l3CIGYhQm502nVll6f-RIDgeE1pzEloXmYih7p9OlUBk2qqoXo53_OUKcUb6M7DpNNKkzq-rJzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
تتوهای خانوادگی مارکو باکیچ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/SorkhTimes/134095" target="_blank">📅 18:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134093">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YijTJWTAr7OUoRom14LRdjlIFiJ6C3hRywKgKmLuJe-xdJCVu_EFbzlpL5EeEWktMBYqDB42eibFisISs_AgIX77oldlT58Yot6YmLs52Q4AQjzZjzn6WFJF_mm9hqjO8vJ1Pnk0mdEivLi1mbi1ovbxCcM1QYRFWXvoE8l44KxpJbi2UljUJ_KYcPd-EYFW-WwUMYv28N5Y8Wnu0a1nMWWCeX9LFayqfMqtiPhvMY0xIWei7UluLPkZO1vzrEOES8iF2TC0uXKDn-j-6o_q9D1amh777duqIAkKDDixkS8v6b0OxhXXpEVVwCeTZcw8VOMtCJ_eV4E9pI13ODHw7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
ملی‌پوش پرسپولیس چشم کورتوا رو گرفت
🔴
تیبو کورتوا پس از دیدار بلژیک و ایران در اینستاگرام حسین کنعانی‌زادگان را فالو کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/SorkhTimes/134093" target="_blank">📅 17:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134092">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🔴
پیمان حدادی: تا پس‌فردا بین اوسمار ویرا و دراگان اسکوچیچ یکی رو بعنوان سرمربی فصل جدید انتخاب خواهیم کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SorkhTimes/134092" target="_blank">📅 17:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134091">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
هادی حبیبی نژاد در آستانه عقد قرارداد با پرسپولیس/ ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SorkhTimes/134091" target="_blank">📅 17:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134090">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
🚨
محمودی رسما در لیست رزو تیم ملی قرار گرفت عازم امریکا شد  امید نورافکن و کسری طاهری که قرار بود با تیم ملی به آمریکا بروند، به ایران برگشتند و امیرحسین محمودی ، خلیفه، حبیبی نژاد مسافر آمریکا شدند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/SorkhTimes/134090" target="_blank">📅 17:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134089">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
سخنگوی باشگاه:
✅
« اوسمار به کار خود ادامه میده و تمرینات تیم زیر نظرش برگزار میشه. هر اتفاقی رخ بده، از طریق رسانه رسمی باشگاه به اطلاع هواداران عزیز میرسه. »
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SorkhTimes/134089" target="_blank">📅 17:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134088">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
بازیکنانی که به صورت قرضی یا حتی دائمی احتمالا از پرسپولیس جدا خواهند شد:
❤️
امیررضا رفیعی
❤️
محمدحسین صادقی
❤️
سهیل صحرایی
❤️
مجتبی فخریان
❤️
ابوالفضل بابایی
❤️
علیرضا عنایت‌زاده
✍️
خبر ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SorkhTimes/134088" target="_blank">📅 17:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134087">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtH69HI4J9Ywe9a2wMM_-FpczyjFawEm8p3sOvALBEbQJipoJmhPFt1KkojoM4BsbIkWdFqe9gzL-LBIiGFjZJ6y7uZOvZo6WNCCpuZ3gzF3p3XOZ5Q_txrhAhWWcAcHvzSN3BSKsJTkjGgR6Wr_EYoIhoOZTww08YWfQjplCB1qPaQL5Mz1n8jb2jVgamw4blYn9G-3tlcTh3T6AO_KSwXuYJ0tbxv50pF5zJh1VYcvEDcoaWsCiddxIM7K_eKmWGz7DUPBScSbdFFmceuTh3798_-HYEYqxrE4W6mP3UbzoT8FAa4GShAiLDzJoTj7xCnt8lf-Xf8wwCB4IayZvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
فقط کمتر از
2⃣
1⃣
ساعت تا بونوس ویژه جام‌جهانی وینکوبت باقی مانده!
🎁
🔣
5⃣
1⃣
بونوس ویژه روی تمامی واریزها فقط با یک گردش روی حداقل ضریب ۱.۸ به موجودی خودت اضافه کن.
📌
همین حالا وارد ربات وینکوبت شو و ازین بونوس ویژه استفاده کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SorkhTimes/134087" target="_blank">📅 16:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134086">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🎥
گل‌های روز گذشته جام جهانی ۲۰۲۶
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SorkhTimes/134086" target="_blank">📅 14:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134085">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
#شایعات
🔴
اوسمار به دلیل اینکه مهدی لیموچی درگیر مصدومیت بوده و کمتر به میدان رفته با جذب این بازیکن مخالفت کرده  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/134085" target="_blank">📅 13:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134084">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
فرزین معامله گری، علیرضا همایی فر، علیرضا عنایت زاده، سهیل صحرایی، محمدحسین صادقی و محمد گندمی به اردوی تیم ملی امید دعوت شدند   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SorkhTimes/134084" target="_blank">📅 12:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134083">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
ثابت‌قدم، مدیرعامل شرکت توسعه: تا هفته آینده نصب صندلی‌های استادیوم آزادی به پایان می‌رسد/ عملیات چمن هیبریدی هم آغاز شده و تلاش می‌کنیم به اوایل لیگ برسد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/134083" target="_blank">📅 12:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134082">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✅
نساجی مازندران به لیگ برتر بازگشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/134082" target="_blank">📅 12:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134081">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDSx0-jGglLb9LAkdll6ihGlvo9M8IOEEV4nOcMlktIJJADqyzqUTBqRAnekFF0W04OekIDcaEeqBVibNiupf5zVJb1u_lqaRPcpZRtn6IvHeWxjcJR5e4_4DLLg64FsDvMZ_GCiYJHd5oNHVd30PF6XLoSlGRnJ-ffuNWpZ2MMfMuBssulIyGJxrLT2OgyYda2AsbU1vnnst2Gn2ulfnk0_w3ZKTk1e_nC219Rh7fez1KORsnJowS9g5ik-8JWstjsZrcQ81WxYJybzv2NGOPi_xwzzn__wLtqncoHnxvGw4EacTXAiwnb-ad-6gjZEVnTgu11jubnzDWlw8KQv6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بر اساس تصمیم اتخاذ شده، فقط فصل آینده 18 تیم برگزار خواهد شد و در پایان فصل آینده چهار تیم راهی لیگ دسته اول خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SorkhTimes/134081" target="_blank">📅 12:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134080">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/652cdc4d67.mp4?token=TK5l8u2IgZK7UWp9M2ycVZtr7afVKDbJYTwHyUI_NrIM522N_liT9ZvaBBi0XvxdQQrVJrVf1MY22qAJOg9ybJ9BhbwJvqVeVNcL2SVikLzaB40UllqiQ6JHMoc3nynRyFwvgipgncUZHqX-hOrGiX3ne2XBXk2N8NM_T7udGWMyAZSxn6V2R2IcuDaXtjNARw2XAyKOGX0M7strHnCtdLbKrsSKAjHHSrdBimg9I9em8zwkMRcA4gt-a-QWF0KHlaD_cArIEE86862LutWgI7ivAGzxgnIzlr1RdyNLGNkuTemgyAjHZuXFwsV1owHbyjGPsUC2jWinAyscz2Ohkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/652cdc4d67.mp4?token=TK5l8u2IgZK7UWp9M2ycVZtr7afVKDbJYTwHyUI_NrIM522N_liT9ZvaBBi0XvxdQQrVJrVf1MY22qAJOg9ybJ9BhbwJvqVeVNcL2SVikLzaB40UllqiQ6JHMoc3nynRyFwvgipgncUZHqX-hOrGiX3ne2XBXk2N8NM_T7udGWMyAZSxn6V2R2IcuDaXtjNARw2XAyKOGX0M7strHnCtdLbKrsSKAjHHSrdBimg9I9em8zwkMRcA4gt-a-QWF0KHlaD_cArIEE86862LutWgI7ivAGzxgnIzlr1RdyNLGNkuTemgyAjHZuXFwsV1owHbyjGPsUC2jWinAyscz2Ohkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پدر کسری طاهری: کسری فصل بعد پرسپولیسی ست و قرارداد داخلی امضا شده
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/134080" target="_blank">📅 11:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134079">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cfc110b2c.mp4?token=W-Dc1GdmyThV99MGeWkkx3OEg1Vnue7VbVn8cdGM8RTHZkv7xLCvX7v3rwSaBk_pJ2Gcy0XiHxQ0h8HOW4-vjoPPc3ftp59eDr13sRWHtXRwEH_e5x5oHaZthOCIVElxHsg68VvicOE3VlAxxy8v-TLQVwXnSkZ65YYAHoobV57HpjSL1-2nDvMrejso64sQly40m0ER-sefBKyiuB336zFdUAQt4rdunj5t2jfA8fNEXgxmFMBmCBapYikLtIuQ_3eHdg3uLQ1wwROQl1mBAT8kYrX3JWLfYcRpCw9YY7SkP8U_v0n2TX7xYG_YO3zEau55xi1-09nQcVJBTVybm5Z83bgAmdXqoFUvKTKznVpUOuWkEfQJJEoQ1IdAiKCo4Wf_icN7feMNy98dOiUBJTKXb_ZqTId33yDguCOcBhYvCH1gwFdDruTv0G26FAQg_67xEAPqgIquQ3IRIpHT1KVK7CNLJatUcwGwwt2aMbteLA1olKLeczhQ_edov3qM62WGRwnGmMNsh-Y6noASpqkcgLDVL_1j45bjycIc6irz4pUyRKoq1kp481rRqAwHd18sWelrAEd25V_x6Pp0VMz_aVcOGjwswI5uGUEV8qIew5eYLnDjlaLEHsWB1789Dcj2qDqbU1rOSSeh2jHZR6yZkg0PZwbgwhJGeJ04Spg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cfc110b2c.mp4?token=W-Dc1GdmyThV99MGeWkkx3OEg1Vnue7VbVn8cdGM8RTHZkv7xLCvX7v3rwSaBk_pJ2Gcy0XiHxQ0h8HOW4-vjoPPc3ftp59eDr13sRWHtXRwEH_e5x5oHaZthOCIVElxHsg68VvicOE3VlAxxy8v-TLQVwXnSkZ65YYAHoobV57HpjSL1-2nDvMrejso64sQly40m0ER-sefBKyiuB336zFdUAQt4rdunj5t2jfA8fNEXgxmFMBmCBapYikLtIuQ_3eHdg3uLQ1wwROQl1mBAT8kYrX3JWLfYcRpCw9YY7SkP8U_v0n2TX7xYG_YO3zEau55xi1-09nQcVJBTVybm5Z83bgAmdXqoFUvKTKznVpUOuWkEfQJJEoQ1IdAiKCo4Wf_icN7feMNy98dOiUBJTKXb_ZqTId33yDguCOcBhYvCH1gwFdDruTv0G26FAQg_67xEAPqgIquQ3IRIpHT1KVK7CNLJatUcwGwwt2aMbteLA1olKLeczhQ_edov3qM62WGRwnGmMNsh-Y6noASpqkcgLDVL_1j45bjycIc6irz4pUyRKoq1kp481rRqAwHd18sWelrAEd25V_x6Pp0VMz_aVcOGjwswI5uGUEV8qIew5eYLnDjlaLEHsWB1789Dcj2qDqbU1rOSSeh2jHZR6yZkg0PZwbgwhJGeJ04Spg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ثابت‌قدم، مدیرعامل شرکت توسعه: تا هفته آینده نصب صندلی‌های استادیوم آزادی به پایان می‌رسد/ عملیات چمن هیبریدی هم آغاز شده و تلاش می‌کنیم به اوایل
لیگ برسد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/134079" target="_blank">📅 09:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134078">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5172bbee52.mp4?token=HKCiiLPHHC2d68KQ8_-koI0j4Xjv9Ihq0sKcTQVNuF-jTMFdTTEqOyA5v78FRPBgVgP4VHgH5SQn2BuM3zyvHP8e6wcQn11uQUeAp9-kcq8u0K4IC1zPjqOwjowwUza43akFEQRfp8vZnkmzC4PBkIbr_ZKpPGK7ZvYVuctfbpKP_QJeZAVTGU7c3gGFDhEJr3hwcuz9OmqzRPQJpNdI718esgbZ4lkjO6rcNek7JSTxIEhM5cmC4y0esn3rPhhTfASMldWjJEOndzOBywPv5nSvwemLhvkDRhkbE1dV4HhobRz231ew5xkalu0V5EQGznqSsQPtbms9rQ62aoOIiX3Sw4pFWfF_eyP37Zopy_rmj_o_v4YIRPsCgtp29_kVvVzcn5iDsDThwwEby7O99C8OZ47HGuct0aMsxJtSDb3NRUJsGrmAmViCXLE-0Lz5f6951W_2ngsD8Qdw4GCAOxN3su7jAj8GrM5glbar7TgpczPW5VqaHD6rlpyTImf6LapyYYWPSC0lhGMvtBhCP6bkA8o9i1U8K-pXv4aebWCt60Fd1gLlHuHSJ7h2IwLRBkIDw9rdMr02HhBg7AWm9wGO_G4utqE5mswhXUv0sp8j34LA9OFWVpYKb8K7F1UCXepJ50yM5-DjD-OxPzxHR9hChscAlaX9cv_VV47GSPo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5172bbee52.mp4?token=HKCiiLPHHC2d68KQ8_-koI0j4Xjv9Ihq0sKcTQVNuF-jTMFdTTEqOyA5v78FRPBgVgP4VHgH5SQn2BuM3zyvHP8e6wcQn11uQUeAp9-kcq8u0K4IC1zPjqOwjowwUza43akFEQRfp8vZnkmzC4PBkIbr_ZKpPGK7ZvYVuctfbpKP_QJeZAVTGU7c3gGFDhEJr3hwcuz9OmqzRPQJpNdI718esgbZ4lkjO6rcNek7JSTxIEhM5cmC4y0esn3rPhhTfASMldWjJEOndzOBywPv5nSvwemLhvkDRhkbE1dV4HhobRz231ew5xkalu0V5EQGznqSsQPtbms9rQ62aoOIiX3Sw4pFWfF_eyP37Zopy_rmj_o_v4YIRPsCgtp29_kVvVzcn5iDsDThwwEby7O99C8OZ47HGuct0aMsxJtSDb3NRUJsGrmAmViCXLE-0Lz5f6951W_2ngsD8Qdw4GCAOxN3su7jAj8GrM5glbar7TgpczPW5VqaHD6rlpyTImf6LapyYYWPSC0lhGMvtBhCP6bkA8o9i1U8K-pXv4aebWCt60Fd1gLlHuHSJ7h2IwLRBkIDw9rdMr02HhBg7AWm9wGO_G4utqE5mswhXUv0sp8j34LA9OFWVpYKb8K7F1UCXepJ50yM5-DjD-OxPzxHR9hChscAlaX9cv_VV47GSPo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
فیلم خلاصه بازی نیوزیلند 1 _ 3 مصر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SorkhTimes/134078" target="_blank">📅 09:27 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134077">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✅
جدول گروه G جام جهانی در پایان هفته دوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/134077" target="_blank">📅 09:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134076">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❗️
قلعه‌نویی: معادلات گروه را بهم زده ایم و به دنبال صعود به عنوان صدرنشین هستیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/134076" target="_blank">📅 09:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134075">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✅
جدول گروه G جام جهانی در پایان هفته دوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/134075" target="_blank">📅 08:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134074">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✅
جدول گروه G جام جهانی در پایان هفته دوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/134074" target="_blank">📅 08:58 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134073">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUgzWTSDN56Mv3LBdfNGv8GYJKLbVTmiJundFwoBnAByFBkgSdQc6suqV1mQXbZZQkLDNTxZtO0iqBDkzKvhUWXAMUb8byzPVFpPuVgLqdEdJsDTrZaOUVI4H-SJ1Kqq81EuA2vaxiZtxZbaQZgdJLTScseTp3wk0snaGXJWb4ubX7D24L2w-15BsPbisiZoWWmn66GENQDo_GPyNsSfEIRIXszLV_0kHgMQNSYS7-1aVg34bCFtH0e4XVrhOG_QhoWiN8GA4jxVk2FtilCUuoDwDL5u8Nw53Ci1ytLYEHQO5d4772D15S2CqIdPgT5zS9Ci7BxU37VxPN7WdwSVYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جدول گروه G جام جهانی در پایان هفته دوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/134073" target="_blank">📅 08:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134072">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/if8H3oQ_V_mttY3yoI3KXRYhBYsWKrQ-84M4bt-Uh3d6YiuIlaBtH3Sjx7EC9t1-QO6wguMKOnE3bgBVOk17-xgkC3JCi3Y5Arsg9FtlGRzkTb0AJUiO0oybtTT8OfTsVonkSJan67pNPnGsU1MTrgZ9wzWiQDVX7qT_IevQX_b3T0e5RdGO2sXIkW4NDglo-kEHhjUM892j9eKN9RbJbLVhEhizk7DP3mfOpYQVC0s2l7FI47npe5Sj2mcoMIouUSI-g_ELCK8-xt7782mfOvt-5RUzpqZtZm_z4jxtRDdnhx2Zo_5yeJjgOeyym-DRzk5cD0XbwY_QznwugWHdpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
نتیجه بازی های دیروز جام جهانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/134072" target="_blank">📅 08:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134071">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reoKrnHZ2DmTjBFFqF2GpFJ_EAV5sY0j5QFS-HCz7Lee_CR85ixY4slOABPrVCLKJqS1cb2YmwMRWdQciHlhmEisg6QbUaZBvmz3gOGKph1r11yVOTv0amB5ElZ62slNXH2wDR2eJqaF2-Y9VT0DtsdTvb_ZkcpacDo9lEXCHWT750mxRGSbpFiyPZyHb71zeaAWKf6kMHqlmvc_pd1iaEOb9imG7urrF668h5mvgnrlOGidV_yY_EDv9YNJwHKR4VTIkZFVbKxICmD5KZ-HYCHOfR1Sw_tS35mxTjLdvm0pgB0T5j10yxx_ziSa2_KUnxowE7ZtdIqDW8u-f7Wqrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
ژوزه مورینیو:
بیرانوند هر توپی میومد سمتش رو می‌گرفت، بعد از همراهانم پرسیدم این پسر کدوم تیم بازی می‌کنه؟ و گفتن تیم ایرانی انتظار داشتم بگن یک تیم بزرگ اروپا و فقط محکم زدم تو سر خودم چون حق بیرانوند این نیست
❌
اگر یک دروازه‌بان بتواند آن واکنش و مهار توپ‌ها را مقابل بلژیک انجام دهد، یا باید برای یکی از بزرگترین باشگاه‌های اروپایی بازی کند یا اینکه استعدادیاب‌های فوتبال آدرس او را فراموش کرده‌اند. بعد از بازی امشب اما فکر نمی‌کنم آنها دیگر آن را فراموش کنند و به سراغ او خواهند رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/134071" target="_blank">📅 08:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134070">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mp_x8XYAm1gL9zg8dwCmmgKKJ9sHt2x0irsj6DXb5LD-gbh6IRONvzzSrBbeMgYnZpIQ6P3r5rF0JVQxUlpNo5a0FI4Jz-50PNjfD6oJxs8HlTrP8c75OBXulSl-tIyIhnW2Vc6-65nQlDqsj-2tyizICtUvjnBnxA9F0dCbZes-BdeyDs1gOI_ztkKcFW1uIC8Ac216XGAJPJ2AccKQC_hDDXnPwwrb8ZFPY_amm7fyQVZc3HcKJUOs4vEhdidLZoRE3Wu57cr2wZTlPVa3YMr1rQILGIli0DEm2afJ3TZUnBW6Z_pexqS7VzBzk6WVjwFS4ovfWHjoyDX_TaWgcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
⚽️
گروه G جام‌جهانی ۲۰۲۶
[
مصر
🇪🇬
🆚
🇳🇿
نیوزیلند
]
⏰
بامداد دوشنبه ساعت ۰۴:۳۰
🏟
استادیوم
بی‌سی پلیس
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/134070" target="_blank">📅 01:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134069">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✅
جدول گروه در پایان بازی ایران و بلژیک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/134069" target="_blank">📅 01:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134068">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpa8YtdO4_XJdINT9-IhcVsWaT7fSindVTaiTPLIx0DDP1xtGuielGAqzTZljewy4k7Qx816avO_zXfvSqHAuhZqjHXN3_WH_-wd3Dt0QenKag792p9KrrvVSuivYFAHFiRRB0bRfuDNaq3NO66XFLq4cmud1xpppxwAmVY5lmsqvNRjx4PREadibk_Nkz8n1SRmZT3zvyrjqqbhEhLMkP1D6mp1DEqi1VVtRKIUkloWOLZDO0TieMhtZOBDflbTouMPlP_3msaU1G6H-kse7xgyN0S2UOMaSPmiic-4ghzB0Hqb6a4s6eSjlijwc8uG6Kka71xd9oxNzTbFG8YA0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جدول گروه در پایان بازی ایران و بلژیک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/134068" target="_blank">📅 01:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134067">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PycMVdEa8iTqm7gnp3cM3wp4d9ntn5Ge-4VBuiLQS4tuioy6QKoTS6fc9yzuVufHhFtpJulOliauYOIPMd8rT6kHMxDRaCa7-zP07XqCRFWBaN6qW4GXd6Bd1ep5rDl1fDIVWJinURIg2ogaFraSKCW65q8LeAhlwBIEwUmv-qYCuinK_NBF_VAnlIYvshoNn7ZPezz65LVXkZKoOCDQRL5-f8wkznzjEHFbuCnXnSdW2cCJpiEBPk24eIJqnBYxSAOgVMcR2Mlu6lvgpT6EVr8_Wdwz3UVt635Bsi6omzNQIplIh5xn0kE6Gw3zSRIRXHySoEOzJhXGjET_6fROeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نظرت در مورد بازی ایران و بلژیک ؟
🔴
ابراهیموویچ : نزدیک بود نیمه اول خوابم ببره و نیمه دوم واقعاً خوابم برد
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/134067" target="_blank">📅 01:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134066">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmkEbROXPt6wSXikO1DWfJZ9V_PmkFYpiozMiZ4f2Wm1HKstb_-eW0iJSpxSzCTz4-DcyDfQPlcOe5a7ozinaI-YMIHn6eCYtTmmR8dCole6orwbdv-rAHyANNPCxb8o6hVQiV5oEXsvVS4jMtOWK1Rx1jS5iogPjCyoAW__KDbSvrZAx6ISgxK5Np4gvzjvrGmZVUve2Flh94GiuiTJEJ-dHSRyUVyt8kpWIEQ1Lvpk9egjeMJLvfPAtfUU1yaGedxArESRgPP8oqmQ8oW3eZTUJu54_lQo4I5lovj7fIuLXYV3_cmvLUFj9W__0B1yrVWtfvFFU1AATW_kUE2W-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
بیرانوند و جایزه بهترین بازیکن زمین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/134066" target="_blank">📅 00:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134065">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nddIX0Nv8FH_IVl40j44J9cIkf3iZzzgxfWiqE1IlX4hfmBIlMUZ9peVbomH5GGWxsO4V5bCfRpT0i-OsMg6YSXiuAWXfldR_PgIzfAFMFit5maWhvssB86R1Q2Aat2NKjvBFYhKLpyY10z9k3dVQ_uw5R8_L3A1lvfSAxps3grReGG6qmnOt5O2xrhsHokxCdlbXV260z1cy561RVXeMv2WG3yWqjY-WczFOczGmJ5zqo_o_nWnP3K6sPcPu7tyw2kLuPZTnLISSJsr2l4Tbkohw_O3K5cTEczEWT1QsRS-yu91mJN8Oy9kD2BuuLy7-IZBSWfSLVIL1cJUw4VOjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سرطان اخرشب بیرانوند در کنار مسی، تونسته نمره 10 بگیره(:
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/134065" target="_blank">📅 00:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134064">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135ac7b305.mp4?token=aFrwW1dIUKoyZGU3Nrb6VZc4pNzuFxnen_kRUOqA3HrWLxkgyPdoZRfoo43Vb1zuLPLJogIiVkvgHNEzpW20QhY-Y-f_rEKkKhMmtil9xpW58xEVtRlBnbRJamAqd2MocBFF8eTpJqJRguw4dPFa4fI9n27bvQemh9aLmGWHx9Ib_iSNCnP31FmDNKL5xzmRucesiMCb_YygJ_5JwUYJMvuiTd2DEPDKhAQghTmmYhiwKpJchYcKDqXdPNB5V1voG2eD4AjRQxyudLsqwniKEs_eiH_8qt24VzInOzFaVTv6_h24Ki7xjVUVZOFQb8JO88GcDfAj5AP2XcKu3RDDF4mQOwakG1x1-D3ZZA9Y41Q08FFrwZ3e6OHvCJ4nVoTmMlf8IfRoerSo3_V-wQRYR6IGQw-ZwvrXODjEGyAQj-3wB03sIMNLbb03mLRURAIyGXMJ6aKnerwxNFaEBb94fn3ljuOZy1sdTKWLLQzLb19FTCLOKgM7BhOiA93KvtjmGLYrMeqyuJ2gmOONT8_3gUiotsBl37L4SBKwkPZJh0B9uh3FRKKcKHWh1b8dfAdik19Xckncd20HwwoWPgY6iTs0iAfrp9J9wEmDy6H8Z5bRP-amQwZc4Am-BVel2rdfVaSJtYwXWe4UpXJZL0EoB6Vw-yQW4ISZPT0fKUwY5Ik" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135ac7b305.mp4?token=aFrwW1dIUKoyZGU3Nrb6VZc4pNzuFxnen_kRUOqA3HrWLxkgyPdoZRfoo43Vb1zuLPLJogIiVkvgHNEzpW20QhY-Y-f_rEKkKhMmtil9xpW58xEVtRlBnbRJamAqd2MocBFF8eTpJqJRguw4dPFa4fI9n27bvQemh9aLmGWHx9Ib_iSNCnP31FmDNKL5xzmRucesiMCb_YygJ_5JwUYJMvuiTd2DEPDKhAQghTmmYhiwKpJchYcKDqXdPNB5V1voG2eD4AjRQxyudLsqwniKEs_eiH_8qt24VzInOzFaVTv6_h24Ki7xjVUVZOFQb8JO88GcDfAj5AP2XcKu3RDDF4mQOwakG1x1-D3ZZA9Y41Q08FFrwZ3e6OHvCJ4nVoTmMlf8IfRoerSo3_V-wQRYR6IGQw-ZwvrXODjEGyAQj-3wB03sIMNLbb03mLRURAIyGXMJ6aKnerwxNFaEBb94fn3ljuOZy1sdTKWLLQzLb19FTCLOKgM7BhOiA93KvtjmGLYrMeqyuJ2gmOONT8_3gUiotsBl37L4SBKwkPZJh0B9uh3FRKKcKHWh1b8dfAdik19Xckncd20HwwoWPgY6iTs0iAfrp9J9wEmDy6H8Z5bRP-amQwZc4Am-BVel2rdfVaSJtYwXWe4UpXJZL0EoB6Vw-yQW4ISZPT0fKUwY5Ik" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
❤️
علیرضا بیرانوند: هنوز هیچ چیزی تمام نشده است؛ از همه مردم تشکر می کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/134064" target="_blank">📅 00:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134063">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❗️
بلژیک رو هم الکی گنده کرده بودن چون واقعا تیمی نبود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/134063" target="_blank">📅 00:36 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134062">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
ایران با ی بازی سرد و بی روح و دفاعی و بکش زیرش  ...بازی و صفر صفر تمام کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/134062" target="_blank">📅 00:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134061">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
بریم برای نیمه دوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/134061" target="_blank">📅 00:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134060">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🔴
پیمان حدادی: تا پس‌فردا بین اوسمار ویرا و دراگان اسکوچیچ یکی رو بعنوان سرمربی فصل جدید انتخاب خواهیم کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/134060" target="_blank">📅 00:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134059">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❗️
ایران با هشت دفاع و بکش زیرش و خوابیدن روی زمین .تونست نیمه اول و صفر صفر تمام کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/134059" target="_blank">📅 23:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134058">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✅
بله آفساید اعلام شد ولی گل قشنگی بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/134058" target="_blank">📅 23:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134057">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✅
بله آفساید اعلام شد ولی گل قشنگی بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/134057" target="_blank">📅 23:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134056">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❗️
❗️
جونم ایران ‌‌..گل اول و زدیم ولی فکر کنم آفساید باشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/134056" target="_blank">📅 22:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134055">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇮🇷
🇮🇷
کم کم برای دیدن بازی ایران و بلژیک .امیدوارم خوب بازی کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/134055" target="_blank">📅 22:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134054">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇮🇷
🏟️
🇧🇪
ورزشگاه سوفای لس آنجلس دقایقی پیش از آغاز دیدار ایران برابر بلژیک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/134054" target="_blank">📅 22:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134053">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇷
🏟️
🇧🇪
ورزشگاه سوفای لس آنجلس دقایقی پیش از آغاز دیدار ایران برابر بلژیک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/134053" target="_blank">📅 22:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134052">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FRXZR8vJxSbeVKwASte3DCByYXFNveNV3fh-G2kdReccEk1TTwgbeBTEKtEBm2xihxic62U9afQ1tBS95NbeWFNwqL9XxBy4RWqWFlosxt5UY1iWjmGgB3Q3mVK3XaO0m-ou5MNggoH6Nq_4YMgAtcXzXhcPt_pffbprYMo7_X0kxHfXsJGuOqbexk6kbJWSpeYIoGYsh_uv6XTKMBR11Hp1gLvvjyYDa0ubfll5Bcvhjvv2C5HlFeR2fANfRaZepBmUrd04ldmtzHaaTmIfBRCJQMtYehF-DeNK2-VLhCRThFvF5RfFTSUTfvvGhkfJctp7R3rag4J-HfLmfrdBKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
رودی گارسیا سرمربی تیم ملی بلژیک: برنامه ویژه ای برای مهار رامین رضاییان داریم!
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/134052" target="_blank">📅 22:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134051">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRYhZDaS5KRXzVwL1sV6ZBNhETVtbjSLqBTRBpz50AW5650OnUS5rMW3yrr_4fGEgh6Mt4fwapWKNKuwHo1y3VVvmat3GyGvA-Va78pHLJLHrH2Ni-pBwrqkU3qbCOB8SmcAnCNbn1ar18jrEL7emhNo1u0O6hq0Ooz_kxmHPSiadRlwoASDZfk-8XmiVeQ1PtZ7sB04QAogXaXesMktJuoc7GYt5gNi6clqriBoVPwTFB0Xm5PEJU30GodEJjKLDv-Qp5jdfhsYpBjlBpXO2nyv1fHNFEzZDZF8Rrkkq9hEqadmKjTP2wYbE36pwwYkzrvZ00nVOk7mcu3s33gOoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
به نظر میاد ترکیب 5 4 1 هست و با پنج دفاع بازی می‌کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/134051" target="_blank">📅 22:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134050">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✅
با توجه به قانون جدید که فقط هر تیمی میتونه 4 بازیکن خارجی داشته باشه، اسکوچیچ از پرسپولیس دورتر شده چون باشگاه بهش گفته بازیکن خارجی نمیتونی بیاری/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/134050" target="_blank">📅 22:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134049">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff62ed07ca.mp4?token=JxJqJyxTBN5n70yDdPtkLhxfqLsyUtaK367W9aNw7yt351REJbrmnhQ22jA0-S3Fj6ofU7jPwmopt3BaaSI8shyxMn_cDwcQW5kUJvwV_kGJBRj6ewWSr71unTAn7pXUbSD_tgRjEGMOU3ZS6vYhVVX_FtdRNssHfh9BwriyuC0cNEh5-LHbcgdu79b4XKDMg3sK4aPQS2KZlUsgnYHJLgIElpYcUu1RhZ4Fkmzk-SsY4omkqRLM5y4G2c35Cw0FHF2oV5a-WfQHciePFQj2U2wyQSZBmZgFV9Osu8HjaE-06znw1igEANc9JqPbDFLBt93lki0MZCT6_MPSNui8lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff62ed07ca.mp4?token=JxJqJyxTBN5n70yDdPtkLhxfqLsyUtaK367W9aNw7yt351REJbrmnhQ22jA0-S3Fj6ofU7jPwmopt3BaaSI8shyxMn_cDwcQW5kUJvwV_kGJBRj6ewWSr71unTAn7pXUbSD_tgRjEGMOU3ZS6vYhVVX_FtdRNssHfh9BwriyuC0cNEh5-LHbcgdu79b4XKDMg3sK4aPQS2KZlUsgnYHJLgIElpYcUu1RhZ4Fkmzk-SsY4omkqRLM5y4G2c35Cw0FHF2oV5a-WfQHciePFQj2U2wyQSZBmZgFV9Osu8HjaE-06znw1igEANc9JqPbDFLBt93lki0MZCT6_MPSNui8lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
گرم کردن بازیکنان ایران و بلژیک پیش از شروع بازی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/134049" target="_blank">📅 22:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134048">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/onuBOjQI2hIEF1Rt-Ox-2LskUuaGUC91JScoK9DdwY0kMmm3OgZsjPCXAEUP-EpeH6LJhyZWNK_TzGrKsEMIX_K-OWBP4iUHwfu3O_5EN9qykVvvORyImPG8R5FbqYUl58ODOoVWMBi7R1phM5BLyfROKHXJ7vs1COVPso78n96fCyvrhXbUY5cbHXdrS7n0g-g-vtPMKBZ9x20IwaKVbV2vRjVpexK31IFQqPztqG3c_r-D8LvEbs0k-wSu7pc--tYj6Lw2hTNR_I9UnaDeC24_hiVw_ASWXAa_AVuGgtColZNdjlObZXrnwHQp_FDRUNHLHZ-RMg1NkdYL-Wn39Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇧🇪
تصاویری از رختکن تیم ملی ایران و بلژیک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/134048" target="_blank">📅 21:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134047">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
#فرهیختگان؛ بین اوسمار و مدیرای پرسپولیس بی اعتمادی شکل گرفته و حتی اگه اسکوچیچ منتفی بشه احتمالا اوسمار رفتنیه و پرسپولیس به سراغ مربیان داخلی میره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/134047" target="_blank">📅 21:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134046">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
گزارشگر پرشیانا اسپورت: قلعه نویی یجوری ترکیب چیده که کل رسانه های دنیا هنگ کردند شماتیک این ترکیب چیه
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/134046" target="_blank">📅 21:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134045">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
گزارشگر پرشیانا اسپورت: قلعه نویی یجوری ترکیب چیده که کل رسانه های دنیا هنگ کردند شماتیک این ترکیب چیه
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/134045" target="_blank">📅 21:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134044">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
ترکیب ایران مقابل بلژیک
🔴
علیرضا بیرانوند، صالح حردانی، محمد حسین کنعانی‌زادگان، شجاع خلیل‌زاده، علی نعمتی، سعید عزت‌اللهی، احسان حاج صفی، رامین رضاییان، سامان قدوس، محمد محبی و مهدی طارمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/134044" target="_blank">📅 21:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134043">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPulseGate</strong></div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
یک ماهه
25 گیگ 220T کاربر نامحدود
30 گیگ 280T کاربر نامحدود
35 گیگ 320T کاربر نامحدود
55 گیگ 420T کاربر نامحدود
100 گیگ 600T کاربر نامحدود
دوماهه
50 گیگ
380T تومن کاربر نامحدود
70 گیگ 450T تومن کاربر نامحدود
150 گیگ 700T تومن کاربر نامحدود
200 گیگ 750T تومن کاربر نامحدود
سه ماهه:
120 گیگ 680T تومن کاربر نامحدود
160 گیگ 730T تومن کاربر نامحدود
230 گیگ 800T تومن کاربر نامحدود
320 گیگ 950T تومن کاربر نامحدود
400 گیگ 1.1T تومن کاربر نامحدود
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SorkhTimes/134043" target="_blank">📅 21:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134042">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❗️
شبکه ۱۴ اسرائیل: قطر و پاکستان از ترامپ خواستند تا پیامی برای کاهش تنش تنظیم کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/134042" target="_blank">📅 21:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134041">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❗️
🇮🇷
ترکیب تیم ملی ایران مقابل نیوزیلند
🇮🇷
🇮🇷
🇮🇷
علیرضا بیرانوند، شجاع خلیل‌زاده، علی نعمتی، میلاد محمدی، رامین رضاییان، سعید عزت‌اللهی، سامان قدوس، آریا یوسفی، محمد محبی، مهدی طارمی و شهریار مغانلو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/134041" target="_blank">📅 21:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134040">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✅
فارس و تسنیم : مذاکرات بخاطر تهدید های ترامپ متوقف شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/134040" target="_blank">📅 21:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134039">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZEzgk0ZbIHjP_sVcbGqbh8gx6ozfgURcwD7GxWUnYJgkSEqZzcBhkgaysXCA9_wJUgZThwBuKtZIfL4bL7t8vw47PfC6u3BFiraA0KuXyi8ouJQUTrS1zYDuzQSih9jf05L8FgO9yR2koFqlUBlN-G8sVd5EjHy1rtxG7B4o8waRMWBTRjAgKpPj_lHmC40SWcGOpiZ_UDV57fiEhCiJz5f_llTALeSUy5iTy60LCspkfWB8Vp6EcqtqfVZy2kQOhcX6RhUkm7KV1Yk8vr2flNvFdLgn1aQ6c66p293TGebfVBgbMpM9_L3miRT1KivHciXI75KGCx3sBgTYFaEag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
⚽️
گروه G جام‌جهانی ۲۰۲۶
[
ایران
🇮🇷
🆚
🇧🇪
بلژیک
]
⏰
یکشنبه ساعت ۲۲:۳۰
🏟
استادیوم
سوفای
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/134039" target="_blank">📅 20:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134038">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
کسری طاهری اعلام کرد با پرسپولیس به توافق نهایی رسیده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/134038" target="_blank">📅 20:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134037">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✅
فارس و تسنیم : مذاکرات بخاطر تهدید های ترامپ متوقف شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/134037" target="_blank">📅 20:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134036">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c475ba2cf.mp4?token=JGP8uVDHf6ltaMban0kT9xrG_WduEr_c2GHqYuyGi9HWQykSLKzur66i3agp_nbSltj7MTGRTvbiNwK1U0os20PDdpVnra3dxIwB3FiHz3tXAJ7HpBZLt22WpRlCujUdxFuj9LcmIu422Sff6rMZQXD5yfFAgrlIVduv_ecfDDp5UomCU3DoXnQ_88OddTfrA-rVi53ELuZlfxzCL1MyZdtIpR_S8Dukl1WyugOGCfYYxs_bwcBaRyeHmJnv0i3P1pK8SHo3yrUZwm-15BsmaeA5IejLw0dhx4hX9aUXLtYRWW7x1lUa6oNAPm4gb-YUmLvYb5uSsSR78_D6eBiqpw9kD2xhPu7Zmzh-2qEWCu3e1AdlK8d77DH--LB6VGW8D50FBVlGBS0YV7HUw6voCZ3iTh8yp0IqGkBFDtqMFHaPDGavytv4zdtM_x4GylD0CZfnnfcbOHw58tegPTcErU1CSob2iRZDAHoW1jtUkS0awDOpZjNAATjrYN6Kd98warIeWinXHTykVqBK3vMmAb5E1BDDqnl99y8X_zQmq_YTpIR0iP6xBCIPw2u-wtGaHeaT0VN78WJg42KMBE4BXTXZoxCV3sLXgeAIId_gtjAYWIjzhTdVAbSUbdmL2TRiS22IISte4tQA_7EWobjxti9NKBVX1bbgIslnUW8e8yY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c475ba2cf.mp4?token=JGP8uVDHf6ltaMban0kT9xrG_WduEr_c2GHqYuyGi9HWQykSLKzur66i3agp_nbSltj7MTGRTvbiNwK1U0os20PDdpVnra3dxIwB3FiHz3tXAJ7HpBZLt22WpRlCujUdxFuj9LcmIu422Sff6rMZQXD5yfFAgrlIVduv_ecfDDp5UomCU3DoXnQ_88OddTfrA-rVi53ELuZlfxzCL1MyZdtIpR_S8Dukl1WyugOGCfYYxs_bwcBaRyeHmJnv0i3P1pK8SHo3yrUZwm-15BsmaeA5IejLw0dhx4hX9aUXLtYRWW7x1lUa6oNAPm4gb-YUmLvYb5uSsSR78_D6eBiqpw9kD2xhPu7Zmzh-2qEWCu3e1AdlK8d77DH--LB6VGW8D50FBVlGBS0YV7HUw6voCZ3iTh8yp0IqGkBFDtqMFHaPDGavytv4zdtM_x4GylD0CZfnnfcbOHw58tegPTcErU1CSob2iRZDAHoW1jtUkS0awDOpZjNAATjrYN6Kd98warIeWinXHTykVqBK3vMmAb5E1BDDqnl99y8X_zQmq_YTpIR0iP6xBCIPw2u-wtGaHeaT0VN78WJg42KMBE4BXTXZoxCV3sLXgeAIId_gtjAYWIjzhTdVAbSUbdmL2TRiS22IISte4tQA_7EWobjxti9NKBVX1bbgIslnUW8e8yY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇧🇪
خداداد عزیزی: اصلا بگو دوکو نباشه لوکاکو هم نباشه، ما به صورت تکنیکی و فنی و بدنی هیچ جوره به بلژیک نمی‌رسیم و نمی‌تونیم رو در رو بازی کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/134036" target="_blank">📅 20:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134034">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
فوری | العربیه:
🔻
جلسهٔ دوم مذاکرات اندکی بعد آغاز می‌شود
🔻
هیئت ایرانی به سالن مذاکره بازگشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/134034" target="_blank">📅 19:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134033">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❗️
فرهیختگان: حدادی اصرار دارد که قرارداد اسکوچیچ یکساله باشد چرا که ممکن است با ناآرام شدن احتمالی منطقه، این مربی خواهان پایان همکاری شده و آن وقت درخواست کل قراردادش را بدهد.
✅
اما اسکوچیچ با این خواسته حدادی مخالفت کرده و اعلام کرد در صورتی به پرسپولیس…</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/134033" target="_blank">📅 19:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134032">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
اوسمار خواهان ترابی و هاشم‌نژاد شده ولی تراکتور با فروش هردو مخالفت کرده/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/134032" target="_blank">📅 19:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134031">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✅
ایسنا: پس از ۸۰ دقیقه، نشست ۴ جانبه ایران و امریکا با حضور میانجیگران پاکستانی و قطری جهت مشورت‌های داخلی متوقف شد و برای تنفس جلسه رو ترک کردن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/134031" target="_blank">📅 19:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134030">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
لحظاتی پیش مذاکرات ایران با آمریکا در سوئیس شروع شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/134030" target="_blank">📅 19:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134029">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس مذاکرات با دراگان اسکوچیچ به سرانجام نرسید و اسکوچیچ منتفی شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/134029" target="_blank">📅 19:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134028">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
❌
ترامپ:
🔴
هیچکس نمی‌خواست به ایران زمینی حمله کنیم، نه؟!
🔴
حتی اگر همین الان هم بهشون حمله میکردیم، رهبران و فرمانده هاشون فرار میکردن به غار هاشون که زیر کوه های گرانیتی ساختند.
🔴
این کوه ها خیلی محکم اند و نابود کردن شون سخته.
🔴
الان از غار اومدن بیرون…</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/134028" target="_blank">📅 19:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134027">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❗️
❗️
بیفوما با وجود اینکه جایی در برنامه‌های پرسپولیس نداره، به خاطر قرارداد ۷۰۰ هزار دلاری فصل بعد حاضر به جدایی نیست و باشگاه برای فسخ قراردادش به دردسر افتاده.
✅
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/134027" target="_blank">📅 19:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134025">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس مذاکرات با دراگان اسکوچیچ به سرانجام نرسید و اسکوچیچ منتفی شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/134025" target="_blank">📅 18:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134021">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
|
#فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس مذاکرات با دراگان اسکوچیچ به سرانجام نرسید و اسکوچیچ منتفی شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/134021" target="_blank">📅 18:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134020">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/134020" target="_blank">📅 17:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134018">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
به گزارش خبرنگار قرمزآنلاین، مدیران باشگاه پرسپولیس تاکنون در دو دو نوبت با دراگان اسکوچیچ وارد مذاکره و بر سر کلیات قرارداد، تقریبا به توافق دست یافته اند. مانده جزئیات قرارداد بندهایی که هنوز به توافق نرسیده اند. دو طرف در حال صحبت هستند.
✅
البته برخی می…</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/134018" target="_blank">📅 16:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134017">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
❌
قدوسی : با یه مقام ارشد باشگاه صحبت کردم، بند تمدید اوسمار فعال نشده و غرامتی قرار نیست بهش بدیم
❗️
حدادی و خلیلی در حال انعقاد قرارداد با اسکوچیچ هستن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/134017" target="_blank">📅 16:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134016">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
🔴
قدوسی : پرسپولیس و اسکو به توافق کلی رسیدند و فقط دو بند جزئی مانده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/134016" target="_blank">📅 16:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134015">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✅
فوووووووووووووری
🔴
گفته میشه اسکوچیچ خواهان دو بند بسیار مهم شده
✅
1_ حق فسخ قرارداد در صورتیکه جنگ بشه!
✅
2_ اختیار تام در نقل و انتقالات و انتخاب تیم مدیریتی (سرپرست) و رسانه ای و کادرخدمات تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/134015" target="_blank">📅 16:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134014">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
آخرین خبر از روند مذاکرات پرسپولیس با اسکوچیچ
🔴
مذاکرات مدیران پرسپولیس با دراگان اسکوچیچ سرمربی سابق تراکتور، در ترکیه ادامه دارد. پیمان حدادی مدیرعامل پرسپولیس، محسن خلیلی و علی اینانلو در ترکیه حضور دارند و در حال مذاکرات با اسکوچیچ هستند.
🔴
برخلاف برخی…</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/134014" target="_blank">📅 15:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134013">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❗️
خبرنگار الجزیره: ظهر امروز به وقت محلی قرار است مراسم نمادین امضا و مبادله متن توافق مرحله اول میان دو هیات ایران و آمریکا برگزار شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/134013" target="_blank">📅 15:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134012">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqLxq_X6O8JuYBfwK-_2Z9_obKZLt0p8uaI2LNZXwjkkNCBONDD6JM8D58XWqUjFdmHkQi6Ie1hEYiLToke77hWMd3JAcF97DcgqsJXZHj51FfuJfGnvkKZaqFKTg9Aqsp6ngC8twFgCjTBnGK54Wr-ydz-IMobc0Pdw3rhOAI8uV8dXlltaVqM6biTPDuXPhfUHSodx1OaPXvzkO2qxeU1Eq5MLwWc7FHK3_-4XC_Wk5Hyb-Or0D5ZODweS41YEXu8KIQBZQnfrH777xoOT4krkfTSm_M4tOqpQSraNZUlJuc_HUvxCNWEf7hG09_2ZuKIEvyEH7dDVHATCVkhDuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇧🇪
غیررسمی: تروسارد از ناحیه کتف مصدوم شده است و احتمالا به بازی مقابل ایران نخواهد رسید
❌
پ.ن فکر کنم تا شب که بازیه کل بلژیک نرسن به بازی
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/134012" target="_blank">📅 15:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134011">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rn2AFg2cjdevFHCMjCMxnBs_UiLtUjpkz3dqih1Y-XDVIYwACzHqmoLFKTKczOLM8s4LW4ezkD1cwLr057EKkhCNCY43zazfIrFIVT9w9xpH4ba-XpvIpmVgp-rJDEHBxLpOnmFUMd12sQZlww6FtWuTdQZJ8HnUZf-_4Y2Y5PUB4XnmLAZu91B3rNkCOj_cT48yMJc0kXGG7W5AXbaHOu6DX1oUf8x1nhtERHDSZoTCa5OIVy2-ILc_XyrtHqCp2RhJH3K3igH246phGcsBEc5yve-qjuA5fAGdtGcCVpPz2yehxTb9sj5tOzb7VUgqwDpxNmbCcm_usBsxOpYAiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فووووووووری / آنا
✅
پرسپولیس با اسکوچیچ به توافق نرسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/134011" target="_blank">📅 15:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134010">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">⚽️
خداداد: هنوز با پرسپولیس قرارداد امضا نکردم
💢
درمورد اسکوچیچ هم از نظر فنی و اخلاقی واقعا حرف ندارد؛ هم در تیم ملی و هم در تراکتور نشان داد مربی قابلی است. اگر پرسپولیس او را جذب کند برد کرده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/134010" target="_blank">📅 15:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134009">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPFc9W77yMIIEYtluyIQnEKXw6jLaCh-gQAJnM1slo4GE48Zd8kzpKoBQJyp76xdIZywtDoG1Iwmf62oFNxL5sk01IBjGGmQgsyKNuxd_4BtwjCgu0u3RV0tsSm_njgZ_Alw4FLwUSMOA70EZ632Md8Kkxyna8fEnaot_WTaHeyVk0cO6XRnICF-r1J4ML4Tfx5iL7f4ukylnL3dizjdSa80tdPjhUjaO9Orl0PwnwB8FIot9X3VqHLtCb5OAF_TzSHRYVlYKXZibrJ0IRH5_kkkQ-gmEy0W_gkF0WiJpZ3B4QNRgQw8PYO6UM0IueAqoVz0s1E6-biOMIgnrlxy1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سهراب بختیاری زاده با عقد قراردادی دو ساله برای بار nام سرمربی استقلال شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/134009" target="_blank">📅 15:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134008">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✅
🇮🇷
برگزاری تورنمنت سه جانبه برای مشخص شدن نماینده ایران قطعی شد
⬛️
طبق اعلام کارگروه متشکل از اعضای هیئت رئیسه فدراسیون فوتبال و مسئولان سازمان لیگ، در صورتی که کمیته استیناف اگر تا 31 خرداد (امروز) رأی کمیته انضباطی درباره 3 بر صفر شدن بازی گل‌گهر - چادرملو را تأیید می‌کرد، گل‌گهر به‌عنوان نماینده سوم ایران راهی لیگ قهرمانان آسیا 2 می‌شد و اگر تا این تاریخ رأی این پرونده صادر نشود، یا رأی به سود چادرملو باشد، برای معرفی نماینده سوم ایران تورنمنتی سه‌جانبه بین پرسپولیس، گل‌گهر و چادرملو برگزار خواهد شد.
⬛️
به این ترتیب و با صادر نشدن رأی دیدار گل‌گهر - چادرملو، برگزاری تورنمنت سه‌جانبه بین پرسپولیس، چادرملو و گل‌گهر قطعی است و تیم‌های پرسپولیس و چادرملو باید 5 تیرماه به مصاف هم بروند و برنده این دیدار 9 تیرماه رودرروی گل‌گهر قرار خواهد گرفت تا تکلیف نماینده سوم ایران در آسیا مشخص شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/134008" target="_blank">📅 14:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134007">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvDj2uwAFqrKd19cLCGyHGtXBiBiayjwCt8g2gKTgvkPRmkup6wrZT1Sv5Ultaq5pBJ6AMyV_yx6Mix4s-8RAbjUDaVWGp55luvIE91VcTRBGmWDChFyiyAxIBjIeg-cFSaTFD-JPAYR_2l3BeoDMbm0gTTiZW9xH6-sGisv4jQYAOIYA5wqq-jtxWsiOdSpkNC8K2cTNcFjJgLOO3WXmvJaUb4Uq-siVC5_fzrnfol12pUTDnCQpAttV7h98vVOgfxRr3pKMNv0zGZPBt1jUrCgh4dETpCAACUl68XWVdYRb0b0xbpumXQtD6cFeAbha2KTOq36y3ka_bRLT7UrFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس ویژه جام‌جهانی
6⃣
2⃣
0⃣
2⃣
همراه با وینکوبت ادامه دارد!
🔴
Belgium -
⚪️
Iran
⚫️
جام‌جهانی گروه G
⏰
یکشنبه ساعت ۲۲:۳
۰
🏟
استادیوم سوفای
🎁
🔣
5⃣
1⃣
بونوس ویژه به مدت محدود روی تمامی واریزها فقط با یک گردش روی حداقل ضریب ۱.۸ به موجودی خودت اضافه کن.
⏰
این بونوس ویژه وینکوبت فقط تا دوشنبه ۱ تیرماه ساعت ۲۱:۳۰ فعال است.
📌
همین حالا وارد ربات وینکوبت شو و ازین بونوس ویژه استفاده کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SorkhTimes/134007" target="_blank">📅 14:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134006">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BirXQExN43bW1JYnetXO29Jo_sNbfkv-GMjgUi51vVAPR3NhI0P_aUM4iFwv-uV4RH5kctoYi21kDipK0C4LwocaK6vFCx2LSCKPY2jgE6Gm-Sb5dwt32ZtSfIldJRvKi_nkSqsLmjOqzIS8CCZmwwsL1dh6z5zEmntXJ0CDTZPyWIKDk4L5CRQ7jrsaN5xtiS9fmjqfPGP9eWlwv7OD9-K_rHIAEqIcGZOWPbUfkBePAFNyG1PLdcesrFoUVz7yvoOTdcY0UuTgdOkDJMC5yKGhM0ahdlPDyypFZphv5DXPMKO55UI9HJnkVMa8H2Q_pZ40d7kHnzQBlECDSk0O5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آخرین خبر از روند مذاکرات پرسپولیس با اسکوچیچ
🔴
مذاکرات مدیران پرسپولیس با دراگان اسکوچیچ سرمربی سابق تراکتور، در ترکیه ادامه دارد. پیمان حدادی مدیرعامل پرسپولیس، محسن خلیلی و علی اینانلو در ترکیه حضور دارند و در حال مذاکرات با اسکوچیچ هستند.
🔴
برخلاف برخی اخبار که حاکی از توقف مذاکرات اسکوچیچ و پرسپولیس است، این مذاکرات ادامه دارد و احتمال توافق نیز پائین نیست. همچنان مذاکرات در خصوص برخی بندها ادامه دارد و در صورتی که در برخی شروط به توافق برسند، احتمال توافق وجود دارد.
❌
همچنین در خصوص فعالسازی بند تمدید قرارداد اوسمار و احتمال شکایت او از پرسپولیس، مدیران پرسپولیس مدعی هستند مهلت فعالسازی بند تمدید قرارداد او دهم اردیبهشت‌ماه بوده که در آن تاریخ این بند فعال نشده و قرارداد اوسمار تمدید نشده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/134006" target="_blank">📅 14:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134005">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❗️
جنجال بالا گرفت؛
❌
پاسخ باشگاه پرسپولیس به صحبت‌های تاجرنیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/134005" target="_blank">📅 13:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134004">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-MAGLlqclKy02QbjEx8HKu8Uu2wfi6ULy_Oe7OeHDQJBlXxAGNVs1hw9wCRiB4gfVec6xhMHqtUmAaTyP0W-SkgHVED_Zar4aJgUPFzsmqPN_q8hDI7HZpDl4aNQAtnBl19M5eHLY_PUNujBKO6KBB6OFjm2GmmjvLJpWOd78WjPmTv38DQVAsv1DsyjxlmvLuJEiPWWvlvk6AO7R_8laWzhpeNoDUTy5xKq18GcRCDXTi38OiHZLrzW3i-uTxUaAMIqr4c6-_30JZLYO5VL3LsIq3blo_gHOAu9rDFL2libbJa-OeZNqWxNV0gM_fvwNTVan6SiTyTDX1HDZOkow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تاجرنیا: جام قهرمانی رو بدید به استقلال دیگه  واسه سهمیه سوم هم جام حذفی برگزار کنید
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/134004" target="_blank">📅 13:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134003">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✅
مذاکرات پرسپولیس و اسکوچیچ بدون توافق به پایان رسید / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/134003" target="_blank">📅 12:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134002">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✅
فوووووووووووووری
🔴
گفته میشه اسکوچیچ خواهان دو بند بسیار مهم شده
✅
1_ حق فسخ قرارداد در صورتیکه جنگ بشه!
✅
2_ اختیار تام در نقل و انتقالات و انتخاب تیم مدیریتی (سرپرست) و رسانه ای و کادرخدمات تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/134002" target="_blank">📅 12:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134001">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
با وجود توافق اولیه بر سر مبلغ قرارداد، طبق پیگیری خبرنگار تسنیم مذاکرات بر سر دو بند همچنان ادامه دارد و توافق در مورد آنها تا این لحظه حاصل نشده است. طرفین امروز بر سر این دو بند که مربوط به مسائل مالی نیست؛ مذاکره می‌کنند تا در صورت توافق، قرارداد رسمی…</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/134001" target="_blank">📅 12:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134000">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">⚡️
جزئیات قرارداد دراگان اسکوچیچ با پرسپولیس:
⚡️
قرارداد دراگان اسکوچیچ با پرسپولیس برای دو فصل تنظیم شده است. اسکوچیچ فصل اول، یک میلیون و 200 هزار دلار خواهد گرفت و برای فصل بعد 10 درصد به آن اضافه می‌شود.
⚡️
در قرارداد اسکوچیچ، 500 هزار دلار به عنوان پاداش…</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/134000" target="_blank">📅 12:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133999">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
#فوووری
✅
ورزش سه طی خبری مدعی شد؛مذاکرات با اسکوچیچ بدون توافق به پایان رسیده و با توجه به تخفیف اوسمار ، احتمالا این سرمربی برزیلی در پرسپولیس موندگار خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/133999" target="_blank">📅 12:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133998">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❗️
❗️
ورزش‌سه: پرسپولیس با اسکوچیچ به توافق نرسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/133998" target="_blank">📅 12:35 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
