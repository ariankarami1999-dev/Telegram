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
<img src="https://cdn4.telesco.pe/file/SbOpPtLB0rnrLv_RXxKeWzyrbwmiVPw1i3ViWlroa-4cbN7HoBb1uP_tCik65-BrPu772Sl3Gw9XJDMM3NOGJ1lHkvA45ZvN8clMUiQ8xpjj8taSvldogSErnB4Rti0L2QBweZ0IVLW1cC6MZ_5ybuM4vwq6RmEsrZyfCayFBme878uoiZ51COZepCW20vgmfwatvGElwVrJJAPg908A091ZyqpOO5vU_7UGYL2iAzSjLhmkQcQNAHkL3wfe6in-VDLy0i04fXubcJv45DoXXvXCtpfvNgUzLj8AtQZ5qZ6ZC0XGCw65KpSTV-BMKVkHKUNOFA-sy1u-7OzCQP5LgQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 17:23:10</div>
<hr>

<div class="tg-post" id="msg-132641">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‼️
🔴
امید عالیشاه، بازیکن تیم پرسپولیس: در روزهای اخیر خبرهایی درباره سهمیه‌های آسیایی شنیده‌ام که واقعاً ناراحت‌کننده است. از همان زمانی که آتش‌بس اعلام شد، ما خواستار آغاز دوباره لیگ بودیم و حرف‌مان هم روشن است؛ نمایندگان آسیایی باید در زمین مشخص شوند، نه پشت میز. فوتبال باید برگزار شود تا تیم‌ها بتوانند حق‌شان را در زمین بگیرند، نه اینکه بیرون زمین برایشان تصمیم‌گیری شود.
🔺
واقعاً تعجب می‌کنم چرا در اردیبهشت که فرصت کافی وجود داشت، لیگ را برگزار نکردند؛ در حالی که بارها نامه زدند که مسابقات شروع می‌شود و ما هم بر اساس همین نامه‌ها تمرینات‌مان را آغاز کردیم. کشورهای منطقه هم درگیر جنگ بودند، اما لیگ‌شان را برگزار کردند. چرا ما این کار را نکردیم؟
🔺
تا جایی که می‌دانم مصطفی زارعی مسئول صدور مجوز حرفه‌ای باشگاه‌هاست و نیازی نیست درباره پرسپولیس یا نحوه انتخاب نمایندگان ایران در آسیا اظهارنظر کند. تصمیم‌گیری درباره سهمیه‌ها باید بر اساس رقابت واقعی در زمین باشد، نه حرف و تصمیم‌های بیرونی.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 396 · <a href="https://t.me/SorkhTimes/132641" target="_blank">📅 17:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132640">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
اولین بمب تابستانی پرسپولیس؟
🔴
ادعای سایت هفت ورزشی؛ اگر اتفاق خاصی نیفتد آریا یوسفی را باید اولین بمب تابستانی باشگاه پرسپولیس برای فصل آینده لقب داد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/SorkhTimes/132640" target="_blank">📅 15:24 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132639">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/552e7d620b.mp4?token=nAkyShml6osWBSGZf2iTLKu3xaxwzGIKhEPHIeiSpAVIj64AuOCABjaGJEPiTya3FydP1gCaPkDFOcl5cSXUErSmibjWROyoy0UtJvH-RnyPLGz-NIPTctnAFXYO7zC2QarGBo_zMxNv4OBoDG88ki1rl3E9rmsvm85D975N6zQx3RzO42znDdRqQWvVnpAGdkkoolJw67ipKK546cqvCmelnM089pQgsy4sLMDVg9lwtxk4GQVgn4RM1G0vOnBD44N8VEfZ94yqpoJ51xyRrZE6xuvbEf_h00xtrRTFbs-wlGsTC35PKR29RKVDkzZ68pW6AyT80GutdRFe5x98Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/552e7d620b.mp4?token=nAkyShml6osWBSGZf2iTLKu3xaxwzGIKhEPHIeiSpAVIj64AuOCABjaGJEPiTya3FydP1gCaPkDFOcl5cSXUErSmibjWROyoy0UtJvH-RnyPLGz-NIPTctnAFXYO7zC2QarGBo_zMxNv4OBoDG88ki1rl3E9rmsvm85D975N6zQx3RzO42znDdRqQWvVnpAGdkkoolJw67ipKK546cqvCmelnM089pQgsy4sLMDVg9lwtxk4GQVgn4RM1G0vOnBD44N8VEfZ94yqpoJ51xyRrZE6xuvbEf_h00xtrRTFbs-wlGsTC35PKR29RKVDkzZ68pW6AyT80GutdRFe5x98Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
واکنش مجری تلویزیون به آسیایی نشدن پرسپولیس؛ آیا یزد و سیرجان هتل 5 ستاره دارد؟ باید میانگین امتیازی سه فصل اخیر حساب شود که پرسپولیس بالاتر است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/SorkhTimes/132639" target="_blank">📅 14:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132638">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
الهویی، مربی تیم ملی: امیرحسین محمودی  به دلیل مسائل غیر فوتبالی و شرایط غیر  عادی کشور از لیست تیم ملی خط خورد!
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/SorkhTimes/132638" target="_blank">📅 13:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132637">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
مبارک اونایی که تن به ذلت "اینترنت پرو" ندادن. بنظرم کانفیگ فروشا باخت ندادن چون بازم برای اینستا و یوتیوبت بهشون نیاز داری و تا الانم حسابی فروختن.و اما تویی که فکر میکردی خونت رنگی تره برو با گیگی ۵۰ هزارتومنت حال کن نفس
👈
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/SorkhTimes/132637" target="_blank">📅 13:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132636">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔰
سرویس VIP
🔰
5 گیگ 200T
10 گیگ 400T
20 گیگ 500T
30 گیگ 600T
40 گیگ 700T
70 گیگ 1T
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال و مدت زمان نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/SorkhTimes/132636" target="_blank">📅 13:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132635">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
باشگاه پرسپولیس از زارعی شکایت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/SorkhTimes/132635" target="_blank">📅 13:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132634">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e786c6b741.mp4?token=JtG3djLRvpCTyoY_Dv-KsXYa1M7hUTtT1K3px8UtyCXBzsxkxiSCTE32pxASwlqhNUimMYGqb7mc7O9CpsFA8ZO0mrjj6SvVcUav8A9Ty27NUB64BzifYzqWZafzysfqzoJL1bXKya90zDb0nCCd2PLNiUvFEu58LDZ46pVOfZoXK7FEM69LP_oMDGXF1zw5r21TgnmsgU-tA16S0qaZVB-hogo3JycsWekUCO2lNMeypvZN27KQgu1YE6ry3k0-nXxBlSLsjMHzUMOkYFQUbmN8O3YFX6z8kFI0L3g2Cut2L9BGHz0ZOeCpSVahFzNss76OPbddJ1usCaB9R96KOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e786c6b741.mp4?token=JtG3djLRvpCTyoY_Dv-KsXYa1M7hUTtT1K3px8UtyCXBzsxkxiSCTE32pxASwlqhNUimMYGqb7mc7O9CpsFA8ZO0mrjj6SvVcUav8A9Ty27NUB64BzifYzqWZafzysfqzoJL1bXKya90zDb0nCCd2PLNiUvFEu58LDZ46pVOfZoXK7FEM69LP_oMDGXF1zw5r21TgnmsgU-tA16S0qaZVB-hogo3JycsWekUCO2lNMeypvZN27KQgu1YE6ry3k0-nXxBlSLsjMHzUMOkYFQUbmN8O3YFX6z8kFI0L3g2Cut2L9BGHz0ZOeCpSVahFzNss76OPbddJ1usCaB9R96KOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/SorkhTimes/132634" target="_blank">📅 13:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132633">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
زارعی رئیس کمیته صدور مجوز حرفه ای :
🖍
پرسپولیس به هیچ عنوان نمی‌تواند آسیایی شود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/SorkhTimes/132633" target="_blank">📅 12:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132632">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
فرهیختگان: پرسپولیس از بین محمد مهدی زارع، دانیال ایری و مسعود محبی، یک مدافع رو میخواد بخره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/SorkhTimes/132632" target="_blank">📅 12:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132631">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKXXJQruLNIsGMjm5Ql_z3FWpoUFYcLW_QqPxtKaOB9xh2ia-rCeta0YoipJhEhn0WJtFEQBE5RuwSCA45-nyvtQw7TwQKtKhQFQwwap9U1mODCRlDO_QqCVpL1ZCLUgKeNdPDxVyVpJgU8C7j5T1yqxS7WdqzeHKsRH4KXWv_ez9GhuHj4sH1riCcVz8P2xuE11H0sgMebTt21Omh6Li9JwEA-jjMHkEyyLpbyppoEZrk5N8tYnu0rR-yyKMmhD3o4L3C0wwrW7SU21mvWeZKo-7x9DcW90q75Gs8gNdJIZ9xkBz5_lKY5SpXQaFn7oxFfnKM4gb_LCCRNIKFdT_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یه شایعاتی منتشر شده که اوسمار
شاید برنگرده و جدا بشه که امیدوارم دروغ باشه وگرنه دوباره وارد دور باطل عوض کردن سرمربی می‌افتیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/SorkhTimes/132631" target="_blank">📅 12:21 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132630">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gE0zUKzv8mnErpYho9Ty9dZZNo9XaGxA-T-Z-bb1r_3XMrL2cBFUpvXaOe_bQIyScIQYgLFDBK29u6TqCGXIZGFfpbCvRcXw36T-9Szk1RMwUB7zsTgvjtbaCCuOiG3wyWXgCRUrmT4-g2dlxwurb_9B5klt_33NJXmNFr1NVNb3LRM73JPny_sqln2wBWlaV5nxz2ZLEStwzd9XGaIfPbNwSliN4GNv1yKQwvk5nHWvyW4kxcGrXlFS48ngIR4GYXTHPXNUdmtY4_ty2-sZTLmhJ_jQhDCmIpLOHGhCLDKYiiu1gZ0F7AzbTAF4uvEgGnKzMr0a21UbTAXwiifoYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟥
مدرسه پیرمردها رو نوسازی کنید.
🔴
#فرهیختگان
: پرسپولیس با ۸ بازیکن بالای ۳۰ سال و میانکین سنی ۲۷/۶ پیرترین تیم لیگ برتر شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SorkhTimes/132630" target="_blank">📅 12:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132629">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
اوستون اورونوف و ایگور سرگیف در لیست نهایی ازبکستان برای جام‌جهانی قرار گرفتند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/SorkhTimes/132629" target="_blank">📅 12:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132627">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
سر تیتر روزنامه‌ گل   پ.ن پرسپولیس از خودت شاکی باش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SorkhTimes/132627" target="_blank">📅 10:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132626">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBOnNs11iGW8BsUjsuc791yECAzZOMNowR9WC-1seBqZ5_r2axADHKks0XIoxa0lIeb5RKI1nNea7iOKTCZoZpaQ1zo2H-sT-z-0YW8G3t_YRRYaoe6T2tozu739r-xUZAxNHRz2dMEjO0kJdEOIfxbpF2AsLDKSRKzq2pcFbr-QpWvR7ThYJ0sIifXRsWr_GlZ_ACt-AUhGkIMuYhlO6cUhJvN7F-yj1V3hMavJ8eNR4TkflSVtIhfKkHGUH_3foTUHGt9H5qS6AF8j1fli5Q8-x9aDUGziBXPBy7ICma9CaDe9sr1sBivlBvuhlA6SMU6ss5USDgWqD5i3WIL62A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
سر تیتر روزنامه‌ گل
پ.ن پرسپولیس از خودت شاکی باش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SorkhTimes/132626" target="_blank">📅 10:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132625">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✅
تسنیم: مطابق جدول فعلی گل‌گهر، چادرملو و پرسپولیس در رده‌های چهارم تا ششم قرار دارند، تورنمنتی برگزار خواهد شد تا تکلیف سهمیه سوم و جایگزین سپاهان روشن بشود
🔴
مشابه این اتفاق در پایین جدول نیز اتفاق می‌افتد و قرار است تورنمنت چند جانبه‌ای برگزار شود تا دو…</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/SorkhTimes/132625" target="_blank">📅 10:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132624">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
لیست تیم ملی در جام جهانی 2026 مشخص شد؛ محمودی خط خورد!
◽️
نمایندگان پرسپولیس در تیم ملی: نیازمند، محمدی، کنعانی و علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SorkhTimes/132624" target="_blank">📅 10:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132623">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08f4d5075d.mp4?token=BX0--y8GIbOrS51Y50tAPU0iRkO6CR_AYxbOAYy34pUKNTXAZi0WCIpWZZNTCgqlEpse_7p8ppt9LHFdxVqWxKLvXYUyOXQM1KRIcymwXFg9KDxc_DVY86cdd67QfZYfFOSMO9L8910kb_VgaQTVKPb2AXpUetIZyU-1D5RmIGiUG7XP8UC1VqxvMpyp6Pr0ZuC17R2aZzaMUUr-W5nvd_Y0DEJsDitrM9YzaHBXiXsJlmOKCRj-Mk9qEpGTffi_CI7dT7M0jVbS2F24CJhxh4CblFcyqxGK8RakLS8_MQIilXSNYAAcuWMtFm77Dhkj1rTAPrPO079E2Q7vwKu3Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08f4d5075d.mp4?token=BX0--y8GIbOrS51Y50tAPU0iRkO6CR_AYxbOAYy34pUKNTXAZi0WCIpWZZNTCgqlEpse_7p8ppt9LHFdxVqWxKLvXYUyOXQM1KRIcymwXFg9KDxc_DVY86cdd67QfZYfFOSMO9L8910kb_VgaQTVKPb2AXpUetIZyU-1D5RmIGiUG7XP8UC1VqxvMpyp6Pr0ZuC17R2aZzaMUUr-W5nvd_Y0DEJsDitrM9YzaHBXiXsJlmOKCRj-Mk9qEpGTffi_CI7dT7M0jVbS2F24CJhxh4CblFcyqxGK8RakLS8_MQIilXSNYAAcuWMtFm77Dhkj1rTAPrPO079E2Q7vwKu3Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🕹
گردونه شانس رایگان وینکوبت فعال شد!
🎰
هر ۱۲ ساعت یک‌بار شانس خودتان را امتحان کنید و جوایز نقدی متنوع دریافت کنید.
🎁
تا سقف ۱ میلیون تومان جایزه روزانه
✅
فعال برای تمامی کاربران
📌
برای شرکت در گردونه شانس، وارد ربات وینکوبت شوید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/132623" target="_blank">📅 01:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132622">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
تاج: هیچ مشکلی برای صدور ویزا نخواهیم داشت
بخش چهارم صحبت های رییس فدراسیون فوتبال در خصوص شرایط تیم ملی پیش از جام جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SorkhTimes/132622" target="_blank">📅 00:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132621">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
برنامه های تیم ملی تا شروع جام جهانی از زبان تاج
🔴
بخش دوم صحبت های رییس فدراسیون فوتبال در خصوص شرایط تیم ملی پیش از جام جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SorkhTimes/132621" target="_blank">📅 00:38 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132620">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✅
فدراسیون فوتبال: در صورت تمایل امیرحسین محمودی رو جهت حفظ روحیه بر خودمون میبریم مکزیک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SorkhTimes/132620" target="_blank">📅 00:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132619">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c28a044344.mp4?token=baIdN7uDARGxSopbV4-xvKRM448siDxunmz_-9zGMFQ3jTZfTOzWYKk5IW-YL28OEHLgp_PV__RoYUn6CMebw_98HDR1uTMJxuCwFV8XFyBrZk376FY-Ci8z-7JUne5qCP3dw70b1rC2V27AmHtEFzPAlezgRbX6OEoD6GZJ_txJzLZSSpeoZiFfnETKf1edJH_yhK1LLYiyaB8FZw3eVxgWEmqsOy0cBqyVH_npjjL6SaLh4gTcTyCnd7hO3Is814EAVgss6osGURKBO3FMVIGUUqcLtTEmtJ2srJO1MdB_0xqfZBxr9U1ItXWUPp-Ln3i0IIPS_enCQcFqnmVJ-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c28a044344.mp4?token=baIdN7uDARGxSopbV4-xvKRM448siDxunmz_-9zGMFQ3jTZfTOzWYKk5IW-YL28OEHLgp_PV__RoYUn6CMebw_98HDR1uTMJxuCwFV8XFyBrZk376FY-Ci8z-7JUne5qCP3dw70b1rC2V27AmHtEFzPAlezgRbX6OEoD6GZJ_txJzLZSSpeoZiFfnETKf1edJH_yhK1LLYiyaB8FZw3eVxgWEmqsOy0cBqyVH_npjjL6SaLh4gTcTyCnd7hO3Is814EAVgss6osGURKBO3FMVIGUUqcLtTEmtJ2srJO1MdB_0xqfZBxr9U1ItXWUPp-Ln3i0IIPS_enCQcFqnmVJ-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
واکنش تاج به ناامن بودن شهر تیخوانا: کاری به مواد فروش‌های مکزیک نداریم و نمی‌خواهیم هم اصلاحشان کنیم!
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SorkhTimes/132619" target="_blank">📅 00:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132618">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2531fbac09.mp4?token=o4ZslVOOsMhsc00lARpJLsMosMHmoB-15KTuCvG9JYbpCBThykVT9Z0TMY3HphcvCcOokEuZ5SRcSW26TBm0RnlGEJ3FReiYwG4W-XyR2qD6i5DMW4XWAFfzClB7ucjxp1vTsNn20MhzP_I7Ij9pYJR9cheTibhf9uRvzqfWZQHQKmJMVXtveIyTfs01Kn4LKQrEqevjSgN64ZUdnF67mRfFSHo6IEQdvt0ioj5W7EiDUIgQf-y6vPowwGcD5e4z5LolJbHC4NtKsgGlJRrdAaAR3TKtDgYbj_VxlJ2ONkyqnfD8aEQ05zxHR7xvA96FU-NrG-klqF0RODFI9q96MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2531fbac09.mp4?token=o4ZslVOOsMhsc00lARpJLsMosMHmoB-15KTuCvG9JYbpCBThykVT9Z0TMY3HphcvCcOokEuZ5SRcSW26TBm0RnlGEJ3FReiYwG4W-XyR2qD6i5DMW4XWAFfzClB7ucjxp1vTsNn20MhzP_I7Ij9pYJR9cheTibhf9uRvzqfWZQHQKmJMVXtveIyTfs01Kn4LKQrEqevjSgN64ZUdnF67mRfFSHo6IEQdvt0ioj5W7EiDUIgQf-y6vPowwGcD5e4z5LolJbHC4NtKsgGlJRrdAaAR3TKtDgYbj_VxlJ2ONkyqnfD8aEQ05zxHR7xvA96FU-NrG-klqF0RODFI9q96MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
با اعلام تاج امیرحسین محمودی و مابقی خط خورده ها راهی جام جهانی میشن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SorkhTimes/132618" target="_blank">📅 00:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132616">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/988a98ef48.mp4?token=p114WB5nUaNpClavtnC0e5AePJoSj1IEt24Pj98lObIwKw_NYSvtjPyzVLmLYM0wcQLoP88YH5V5DMkN3WOFLfIbeX_0WcRhAYmm2WSmvqdjjcd-qXEu7AqQihyA4ATPiIM29a1nq2SGTimoQuV29Vh0c6DjreNFAvW7XNu5JNxIkajVDQwjNM_cX4drjkMzdNVWU2Qf_MazAOMRy_NEMMRZA2hvgG2wa9W8afTEkEPD1reXCBIf4BbjH9xsh35B-VrIuKs9N8mqIrSQlp2_SBflgM-yhPUGxp_WNvi7DwHeJ-KHUqQ5t3RNYl3-xfY85uaficqIjGittiZ9b8A9Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/988a98ef48.mp4?token=p114WB5nUaNpClavtnC0e5AePJoSj1IEt24Pj98lObIwKw_NYSvtjPyzVLmLYM0wcQLoP88YH5V5DMkN3WOFLfIbeX_0WcRhAYmm2WSmvqdjjcd-qXEu7AqQihyA4ATPiIM29a1nq2SGTimoQuV29Vh0c6DjreNFAvW7XNu5JNxIkajVDQwjNM_cX4drjkMzdNVWU2Qf_MazAOMRy_NEMMRZA2hvgG2wa9W8afTEkEPD1reXCBIf4BbjH9xsh35B-VrIuKs9N8mqIrSQlp2_SBflgM-yhPUGxp_WNvi7DwHeJ-KHUqQ5t3RNYl3-xfY85uaficqIjGittiZ9b8A9Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
تاج: ۱۰۰ هزار دلار به مالی برای بازی دوستانه پول دادیم؛ هزینه پرواز و هتل‌شان را هم پرداخت کردیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SorkhTimes/132616" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132615">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
خلیفه، نورافکن، محمودی، حبیبی‌نژاد و طاهری خط خوردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SorkhTimes/132615" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132614">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🟥
بانک شهر طی اطلاعیه‌ای از تاسیس نئوبانک جدیدش به نام (رد بانک) خبر داد که تمامی منافع این بانک متعلق به پرسپولیس خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/132614" target="_blank">📅 00:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132613">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40e411950a.mp4?token=naYCNpqz1aE7oSBpgwDwjp9xafk8NLlB9xGedT8vEWJxUJonoQgdPPD7eNuFuMOkOn8ceWxDiurtM6CFVb1NphkuZiad3Z3Ysqa4Lxdd9NTi4cdrXe4IyzLNWjqQJn5zrea_lE989mUSk3KFX2L-Cgmi3adRGnFSOXgBRADJR9FthN-OHETNbksibsjuFmIm-RAgv6E1ojgu_vru1cetm-hFqjNc_AyrZfZSWNM_IU0N5synTRanxW6Ox2mZg7OaOIh-bcDvdG9QMXNmaeYk7WLWE-DvR0h7Zurb4_QAklOkt0mGu3KcckfyoNLG4TgJz5w-DdneVyJfVswwR1nHhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40e411950a.mp4?token=naYCNpqz1aE7oSBpgwDwjp9xafk8NLlB9xGedT8vEWJxUJonoQgdPPD7eNuFuMOkOn8ceWxDiurtM6CFVb1NphkuZiad3Z3Ysqa4Lxdd9NTi4cdrXe4IyzLNWjqQJn5zrea_lE989mUSk3KFX2L-Cgmi3adRGnFSOXgBRADJR9FthN-OHETNbksibsjuFmIm-RAgv6E1ojgu_vru1cetm-hFqjNc_AyrZfZSWNM_IU0N5synTRanxW6Ox2mZg7OaOIh-bcDvdG9QMXNmaeYk7WLWE-DvR0h7Zurb4_QAklOkt0mGu3KcckfyoNLG4TgJz5w-DdneVyJfVswwR1nHhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مسن‌ترین تیم‌های حاضر در جام‌جهانی؛ ایران در رتبه سوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SorkhTimes/132613" target="_blank">📅 23:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132612">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
حدادی مدیرعامل باشگاه پرسپولیس: سروش رفیعی همچنان بازیکن تیم پرسپولیس است و با شروع تمرینات باید در تمرین حضور داشته باشد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SorkhTimes/132612" target="_blank">📅 23:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132611">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🇺🇸
ترامپ:   «مذاکرات با جمهوری اسلامی ایران با سرعت زیادی داره ادامه پیدا می‌کنه. از توجه شما به این موضوع ممنونم! — دونالد جی. ترامپ»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SorkhTimes/132611" target="_blank">📅 23:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132610">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/inWUl5acQ1BUFfyMN6IP8rJojTUysWzfBOBgmfEYxMOZTVy5uB5P-Jtt9zfffc2QQnRvczIMVmtr7aIpEXZJ5OQiI8p_uK2QtrO3jJRCjDmIoPIzAv2gDhGG7OGM8Jf7n2lhJXSp0F6Onhb0GAm2ceBxdgzHn_oqz1TtptmzGH3_LsivDugC47Pzn50HaeAw5tbqBCLJW2itfKAmrJtcJi2m6ayWwHxlA8yTnsALpHCVht-CbSKn4c7v4f0M0bwfL2wGu8IueDbTIj1NRSQnM0_4RDltx9Duu24liRMeaZMJUJpACBuR479x1Zf4aboaToyNkP9FogtkZUfP5rkzHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟥
بانک شهر طی اطلاعیه‌ای از تاسیس نئوبانک جدیدش به نام (رد بانک) خبر داد که تمامی منافع این بانک متعلق به پرسپولیس خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/132610" target="_blank">📅 22:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132609">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6LElCC9wjknDCRssu24HjqkOuXJzOJfk_mgQK1vVjxMYdPH9becoyMtMK9TH5-Cw-qpgs4SoNxzYXsQCFJ12YdB1IafWjcXD4xhjUsTZyCO2KgirthpN7yxiFdV5ZVGUnxDdOE98rrYvAbLOLw8CHqEKbiza-om9dXGpbM2sYoi2kEqd5oYnbBhPG-A26-mTfGD1W7e_1YNJOXIKS7rnDNlmHFvqjxanmWrcagUVpuVBsshv6hkfUbYNsqnSym-wzCuVpRYU7LX-dD-ayJd02rlDans-sAslwaRXMdNsy_DwX4DaGMI4Abtom5TpbhO-K9BXe2jVovd91WJFoswZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
«مذاکرات با جمهوری اسلامی ایران با سرعت زیادی داره ادامه پیدا می‌کنه. از توجه شما به این موضوع ممنونم!
— دونالد جی. ترامپ»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/132609" target="_blank">📅 22:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132608">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🟡
سپاهان حذف شد
▫️
گل‌گهر یک بازی اضافه داره
🔸
چادرملو از بازیکن غیرمجاز استفاده کرده
🔴
پرسپولیس برای ۳ امتیاز بازی با ملوان شکایت کرده
⁉️
باید دیگه چه تصمیمی گرفته میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/132608" target="_blank">📅 22:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132606">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✅
هوشنگ نصیرزاده، وکیل بیرانوند در دادگاه CAS: چه قبل و چه بعد از جام جهانی هیچ چیزی بیرانوند را تهدید نمی‌کند. اغوایی توسط تراکتور انجام نشده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/132606" target="_blank">📅 21:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132605">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">💢
ترامپ: من یک تماس بسیار سازنده با نخست‌وزیر بی‌بی نتانیاهو، از اسرائیل، داشتم و هیچ نیرویی به بیروت اعزام نخواهد شد، و هر نیرویی که در راه بود، قبلاً بازگردانده شده. همچنین، از طریق نمایندگان بلندپایه، تماس بسیار خوبی با حزب‌الله داشتم و آنها موافقت کردن…</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/132605" target="_blank">📅 21:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132604">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BO6d_gDQhNodGbM6sP60p5rh3R3LGdbIZFAnN-d00pupoRVZnIwHWkUr_E88WVKPik3sVdOW510f_uZma4jhhweDLU0o9R01tcSNMK-FPihOofWZVagEF1iJq1u90lc-O8KQgrDYz7PlDBLHzY3ecZfDP2Wp8VbMtmWyKIJIHn4dHLBBDayht4FsGsLfs6acuZlHtgt0jnYWd5HTjV9ir8to_zBPvbIwi4e6OIBzas4kNtC0Sg3Yyr0RLkaos2acS9b8cYHZfyMzleZm5ZvPXQUpBAGZUPf7GfWH3uIz80L8Na7BmjIIuLfeivmVY-6k23r0dYckkl05NiaoVZI63w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
ترامپ: من یک تماس بسیار سازنده با نخست‌وزیر بی‌بی نتانیاهو، از اسرائیل، داشتم و هیچ نیرویی به بیروت اعزام نخواهد شد، و هر نیرویی که در راه بود، قبلاً بازگردانده شده. همچنین، از طریق نمایندگان بلندپایه، تماس بسیار خوبی با حزب‌الله داشتم و آنها موافقت کردن که تمام تیراندازی‌ها متوقف بشه؛ اسرائیل به آنها حمله نخواهد کرد و آنها هم به اسرائیل حمله نخواهند کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/132604" target="_blank">📅 21:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132603">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
ایسنا: احتمال برکناری محسن خلیلی از پرسپولیس وجود دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SorkhTimes/132603" target="_blank">📅 21:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132602">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
فرهیختگان: پرسپولیس از بین محمد مهدی زارع، دانیال ایری و مسعود محبی، یک مدافع رو میخواد بخره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SorkhTimes/132602" target="_blank">📅 21:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132601">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
لیست خرید اوسمار به نقل از فوتبالی:
🔴
اوسمار برای هر پست ۳ تا گزینه معرفی کرده و حتی اولویت‌بندی هم کرده
✅
دفاع راست
✅
دفاع میانی
✅
هافبک
✅
دفاع چپ
✅
مهاجم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes ‌</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SorkhTimes/132601" target="_blank">📅 21:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132600">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
از جدول ناتمام تا شهرهایی که آماده میزبانی در آسیا نیستند
‼️
چرا میزبانی این دوره از تیم‌ها در قاره کهن امسال برای فوتبال ایران مهم است؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/132600" target="_blank">📅 20:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132599">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UK2iL8n-WHa5E0qBkWGpYHCaaRQafg5joQ7cB0AHmRTBx7qEnzNQymkEB96m60ST5y6tket9f-wSWAe2dCvalGl1VbIIZj_0tkgSn1hMIWs3NkAQNGEQ05ZDv5ufO5x9GvJ6h3IYDcHWweHQo8Pk4hZlWohSr-SKNdisqs_aiVDu8Sn1wAeAqyilYwZRWt9cqklLTb-6eEnyAHjXvMhTpSxTRspuLXWqS9sBdyY1yRVYgCJVoxyY-5arqdEz2Op1IE63Qlx09VyzXpFi-C8kc42osc4Q7ACWo1FhlU9Er94yNTAA129YiJrQs44oE0IH5LmBFGlLFNoMauiUCpq8KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🇫🇷
مسابقات گرنداسلم رولان‌گاروس رو با بالاترین ضرایب در اسپورت نود پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
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
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SorkhTimes/132599" target="_blank">📅 20:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132598">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
محسن خلیلی: باشگاه پرسپولیس حق دارد از حق و حقوق خود به هر طریقی دفاع کند
◻️
متأسفانه در روزهای اخیر شاهد آن هستیم که برخی افراد از طریق مصاحبه‌های رسانه‌ای و به صورت غیررسمی درباره نمایندگان ایران در مسابقات آسیایی اظهارنظر می‌کنند. این درحالی است که طبق…</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SorkhTimes/132598" target="_blank">📅 20:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132596">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚩
ترامپ: فقط ۲ چیز از ایران میخوام، تنگه رو باز کنن و بمب اتم نسازن، بعد ما میریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SorkhTimes/132596" target="_blank">📅 20:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132595">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejCySO6lgwY8zU76wHNsoyR5snjDXvzV_jNm2Sd2JwFw89_LihwjynqfLhY0K8NGePrIhsBVE4NkEB8oGqLxaVmWOMvhq8JNz7GwcY38jNDYkDRayDuLfy0HldrxGtdUw-85IDX5Aoq0iCSxD1OU4dKdUmQqo6TNb-aUrXojrrOoPEBG01vrCxzO16eBFAGIiy4AOk9wLzDqcPyXJ9JkTB3EjE14BtWy0ZttMoV3sUWPkrIDNwRI46K6MUbpNmZQICmW64tMnjP8Vx3zvkEq9L5Kf6ZFEcZvAHHYV8KAsu66WQlwN8nVY7FMnzjcOGYYqc_r5ujsBtkPUjvyHza5bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇪
آندرس اینیستا با قراردادی 2 ساله سرمربی گلف یونایتد امارات شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SorkhTimes/132595" target="_blank">📅 19:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132594">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32a1bce686.mp4?token=utKI_tm0AblVrERMmJ2CAB2LYjt8H2PFdgt_qt8kNQ6OVVInBmc77n8mbl5F1lvEeFXh20AJjkzdF0DCNLDVCbR38OMdKvENxD9lcXTiy0pJHCejIm8EOg5W3qwTWTcBBZ7gnBuCzVOVX2hZxIWQaMfeYSa71Sv0Y7j75LWZvuxGbApIUPg3_DoTcJWOidKllN2dnBnRpUXe1IvbeTcBkrSAJ245DbjxlM2WNAhhU3Iy8A3tPy75kWrmbvqakiN8JivTlvOR47vuj6c5ZZZ-h6QhYayfBfnasjMxvlOjADBdX1G5OzkKE68u1twkjWj6SlsAiRRc_537xM_zQVyGUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32a1bce686.mp4?token=utKI_tm0AblVrERMmJ2CAB2LYjt8H2PFdgt_qt8kNQ6OVVInBmc77n8mbl5F1lvEeFXh20AJjkzdF0DCNLDVCbR38OMdKvENxD9lcXTiy0pJHCejIm8EOg5W3qwTWTcBBZ7gnBuCzVOVX2hZxIWQaMfeYSa71Sv0Y7j75LWZvuxGbApIUPg3_DoTcJWOidKllN2dnBnRpUXe1IvbeTcBkrSAJ245DbjxlM2WNAhhU3Iy8A3tPy75kWrmbvqakiN8JivTlvOR47vuj6c5ZZZ-h6QhYayfBfnasjMxvlOjADBdX1G5OzkKE68u1twkjWj6SlsAiRRc_537xM_zQVyGUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
دو سال پیش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/132594" target="_blank">📅 18:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132593">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
خلیفه، نورافکن، محمودی، حبیبی‌نژاد و طاهری خط خوردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/132593" target="_blank">📅 18:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132592">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✅
مهدی لیموچی با ارسال درخواست رسمی به باشگاه سپاهان، خواهان فسخ قراردادش با این تیم شد.///قرمز آنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/132592" target="_blank">📅 18:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132591">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
لیست تیم ملی در جام جهانی 2026 مشخص شد؛ محمودی خط خورد!
◽️
نمایندگان پرسپولیس در تیم ملی: نیازمند، محمدی، کنعانی و علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/132591" target="_blank">📅 16:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132590">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
خلیفه، نورافکن، محمودی، حبیبی‌نژاد و طاهری خط خوردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/132590" target="_blank">📅 16:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132588">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❗️
خب سپاهان که مجوز نگرفت. گل‌گهر هم بازی اضافی‌ش حذف میشه و چادرملو هم فاکتورهای لازم برای مجوز AFC رو نداره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/132588" target="_blank">📅 16:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132587">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
لیست تیم ملی در جام جهانی 2026 مشخص شد؛ محمودی خط خورد!
◽️
نمایندگان پرسپولیس در تیم ملی: نیازمند، محمدی، کنعانی و علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/132587" target="_blank">📅 15:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132586">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
لیست تیم ملی در جام جهانی 2026 مشخص شد؛ محمودی خط خورد!
◽️
نمایندگان پرسپولیس در تیم ملی: نیازمند، محمدی، کنعانی و علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/132586" target="_blank">📅 15:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132585">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJhvrpqUMRgtJMsCD08LSQG743wFQUQp856JW1nnN7FBpaItPA4tLGAEA5X3saV-wdPZbUQtOlajyU1Qhq_wgF7Gue7PSty7lZcrS8yNoT7xPHD8JSjBZgiuISlKfn9omaZkjF1YfkWlxKMWEncK65XxlWODQlLe129sx1CHZq9rBmCNKToqRPouA2GSs5MTQDA-9J2TYjkgPuQ0XVfirqziMiE-zhJ3vMK7r8UudfGZZDU0_ltE6ql8C-HcVMVzRaYU4z-FM65ec6sWyrtrBNzcUmagEE0lpGTCUKYpQHXhJU8zW4ZzFN-JjH6EV7NMfP5IPntiNT4OrziLbjPtSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
لیست تیم ملی در جام جهانی 2026 مشخص شد؛ محمودی خط خورد!
◽️
نمایندگان پرسپولیس در تیم ملی: نیازمند، محمدی، کنعانی و علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/132585" target="_blank">📅 15:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132584">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vc6bQFMw-yqbjFYsA6f0vzQlt9h5rqggzSwopQHga-mjLNyyvXJzGGOtG_g1EZdfeA6sdYpCu8qGgq5QcI4FkvPK-y5x1Enm3M2IbWu4YEUNVympm5NTEeDDfSdfBIoKGGB72bIBpp6WEOG5vxUYemZ6eJkxU5aEyj2KsP3eZ6iU7BQzd7x7LbcTvcO9mgnu4MOTD-Nss407zkyNW64SGQU8xrSn8tZBlMn7VXvUmrsiZ47n76Ru1Lf5ET4jkNY1S5s5GxenwEsKJG9gbJtPbxdYH4Md9BcnijPTWTs7xcVxAaRwpwQBruodP-dZYP2yTSgIxiCtsQLlfEVcowIuPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مراسم معارفه مصطفی میر ابوالحسنی به عنوان مدیر جدید حراست باشگاه پرسپولیس با حضور پیمان حدادی، برگزار شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/132584" target="_blank">📅 14:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132583">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9zdgIIyTf_QLCQn7vw_hon3OgHfN4Gw1CgVzuRdaCgd0n9C_rPZ74LZl-zA7sNxCXszYHzGRx_c3yKs7Mp9cLPl7XEAe1zFEOC7tMbAGO9duKALtefYTRqSJhhf4C1l0zfmntBXBlNyuEDAA9YmwDZK7DU0cdC_sio7pvfyCHCr6YoKE_6pyeDUrIuXJWKveFzEPZytTVB2qMTQ47v4nWcIANdwkdoTogYKnKSHlpOvG-Q1rH-AihcOiyJCKYVHcyEecyos1g733gpl_l3iQC4_W32WmVPYFXEPrK_DwAuuCZXLpFNdLx4OhpmSr1ewb7lfLlpo8WIar_NiV2QLBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚡️
هر مسابقه یک فرصت، هر انتخاب یک هیجان!
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
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
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/132583" target="_blank">📅 14:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132582">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❗️
لیست مازاد فعلی پرسپولیس به ادعای تسنیم:
🚨
سروش، پورعلی‌گنجی، سرلک، بیفوما و گرا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SorkhTimes/132582" target="_blank">📅 14:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132581">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
حدادی مدیرعامل پرسپولیس: افشین پیروانی قرار بود به یک کشور دیگر برود نه آمریکا/ او برای رفتن به سفر از من اجازه نگرفت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/132581" target="_blank">📅 14:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132580">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
فووووووووری
🚨
شانس پرسپولیس برای آسیایی شدن زیاد شده و ممکنه با تبصره ماده پرسپولیس راهی آسیا بشه/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/132580" target="_blank">📅 14:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132578">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-OnBsBeoKNW2sBMr0nwwuPn_NdNkeWhGJpfW5N6Iw_rE-n6uuU04XEo-Bom65Rzp8OPna2XBhz4QmOO597gin7PoktWZboHRMWN-2YC76q7JCxq2NIl_JhPgB1CkTZB9uqrUyhDXffLZgnCm9aEjtnMEbCAKfhWmzXvn2nvmSG_3ox4jgnZmfVTpkJrhOz0N4FIVyLrZe5ndobQREH6w6GYm8Ee35CdIlvP9Gier34ovFF5Jfipb83EREETiucaOEVTiwX4NNexh4Cb7kZEae2QcZAeIIP_-U8QNCCl4laZt1tluc9XeXPqYNa9YWBQaQwF0nN2iAkksMFuKnRR-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💭
تقویم مسابقات جام جهانی ۲۰۲۶ در ماه ژوئن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/132578" target="_blank">📅 13:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132576">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cpx5mxiRkBEN7BsruKhs-60IFleLTsxaGqEW3-mewxWGIT-hZZT1IhO7GgzVHjT7edXF1hyGZehb31Y3hxD1-dw5TQtcYNdHJ6Nb8d8gqcdVTSH8ttVLD8lT-bsm7WnxjVjMJ5lHSFgVDSLdoZDe0uNGFIBY0xhEfzjLuIiMmMwnNcBu-189OceImBcgTLB_Bv7Umgb8LPH9LrYpdyvgMEHcdSdQSctgouEZD2evBZCKYcievrFt9vCZOg0KbaClWVr_HRTixzvd_wmzg5DWsFs7UEci2xXshuGnE7nS3zmV-ZTzqqiiRmNHT9dhFgaiB-m0dI3GMSNdaFg9GKnYAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سه سال پیش توی همچین روزهایی؛ پرسپولیس قهرمان لیگ برتر شده بود
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/132576" target="_blank">📅 12:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132575">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkGTftMuLPDsEOS8M6seshPWPuXZllLdAlm9zxCIUtOwdZpSGs1gkxXNQ4H4hdC7Ij6_ewSuONQJrp5qN_dN3WjZ6sH5bb3yKWZR7OrFcHdfRhluFJUFC2PgTyv743cfdkBx1G2uiJWkKZpjg2ob3u2NOTEvKHOoDMfOPI_TEorSt-WcWFUcDapmofDEJxtvj4woz4R2JvRL_mkdtdvkwrm1dnukJFzBESwikdQonbOZzXnJHWwNhMGLDg-Yf2z_9_wE5lDbsEvpuXcqgy01bSCQtzsQKOesqC0gqXdGgKvc-32klsf3XB15hOK-Z5DjKm-4LXrPEjq3l5m7rxkJRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇷
❌
۲ پرسپولیسی در آستانه خط خوردن از تیم ملی
⏺
شنیده می‌شود حضور پیام نیازمند، محمد حسین کنعانی‌زادگان و میلاد محمدی در لیست نهایی تیم ملی برای حضور در جام جهانی قطعی شده اما این احتمال وجود دارد که از بین علی علیپور یا امیرحسین محمودی یک یا دو نفر از لیست نهایی تیم ملی خط بخورند.
✍
خبرگزاری فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/132575" target="_blank">📅 11:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132574">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohQbq-F9QDsuGNE4h0YJgbcqJcOoh_hYk8bncgD-n7VQvbLkeeM-ojSYltc9jAPWLlOGXt8CmXMi3MNwzGjLr-Ql_MG7vVrI629_hrA5UHgG3kMAsozs6hyapQt12vG9f5daR5gqVM-jbfEsUvTw4QMB-gvYtP37E38Ct79jZ9ZQgXhlyWa8F7RX49AdRgTtvAvdE_8O348SBFJ53no7rxCjM3LTJJQyiCn9k-Y_DCoHZlqGEJrzvXnmwyzCGUGFT7wEM9ZJN7agbEZXWxjoKOnaqYI0pVMnKJs7GUG86q2nS-quPvKxBbxvOGpIhUXTBLhGg15gyVGnOD7YA9QbLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست خرید اوسمار به نقل از فوتبالی:
🔴
اوسمار برای هر پست ۳ تا گزینه معرفی کرده و حتی اولویت‌بندی هم کرده
✅
دفاع راست
✅
دفاع میانی
✅
هافبک
✅
دفاع چپ
✅
مهاجم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
‌</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/132574" target="_blank">📅 10:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132573">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
ایرنا: مدیران باشگاه تراکتور با مرتضی پورعلی‌گنجی، مدافع پرسپولیس، برای انتقال تماس گرفته‌اند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/132573" target="_blank">📅 10:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132572">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
قول بزرگ وکیل علیرضا بیرانوند به تاجرنیا رئیس هیات مدیره باشگاه استقلال: پنجره باشگاه‌ تون باز شود بیرو بعد از جام‌جهانی با تیم استقلال سه ساله خواهد بست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/132572" target="_blank">📅 09:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132571">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2xNLWRnMTv7phQ5aOvtUCndpfLTwI9_JBgZuyeEBGel5aIO39mO36kXVoYrJ_-OVoq2pFqWdzRM6-iZ1QMjwfHVJYkTLAWZkPeyg0x7m_rJpodm-w1Yelj0K0vM35u4vGVzNA6yr4uYDfYtHEqYuLrqFkwq4D55ykicvSplF2YZzbOB2e8asVG904Y1951V6Y6SEnrcj7ADKJJtSHSw-U2MRMJ3xWVb_wwMb5gwuP3PZJDO4h3pYSmcECqcmhkwdqUpPcL4iicb0u3VO6IKu7jNrIK7_mattkIFbsRSlV6nHpg1TjOSp7fowytM6eTp61V0YFG7S4Xf2ZRCh-PDXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
‼️
هواداران پرسپولیس حواسشان باشد؛
🔺
برخی ایجنت‌های نزدیک به اوسمار در هفته‌های اخیر فعالیت رسانه‌ای خود را افزایش داده‌اند و گفته می‌شود با استفاده از بعضی کانال‌های تلگرامی در تلاش هستند فضای باشگاه را تحت تأثیر قرار دهند و زمینه را برای جذب بازیکنان مدنظر خود فراهم کنند.
🔺
بر اساس برخی شنیده‌ها، این جریان رسانه‌ای از همین حالا کلید خورده و هدف آن ایجاد فشار روی مدیریت باشگاه در آستانه تصمیمات مهم نقل‌وانتقالاتی است. به همین دلیل احتمال می‌رود در روزها و هفته‌های آینده شاهد افزایش شایعات، اخبار جهت‌دار و حاشیه‌سازی‌های مختلف پیرامون پرسپولیس باشیم.
🔺
هواداران باید با دقت بیشتری اخبار نقل‌وانتقالات را دنبال کنند و هر خبر یا شایعه‌ای را بدون بررسی منبع و اعتبار آن نپذیرند؛ چرا که در چنین مقاطعی معمولاً منافع برخی واسطه‌ها و ایجنت‌ها با منافع باشگاه و هواداران همسو نیست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/132571" target="_blank">📅 09:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132570">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری
🚨
سپاه پاسداران انقلاب اسلامی دقایقی پیش به کویت حمله موشکی کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/132570" target="_blank">📅 09:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132569">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
به تیم ملی جمهوری اسلامی واسه جام جهانی قراره ویزای ساعتی بدن یعنی واسه هر بازی چند ساعت ویزا میدن بیان بازی کنن بعد سریع باید برگردن مکزیک تازه این ویزا فقط برای بازیکنان و کادر فنی صادر میشه نه افراد دیگه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/132569" target="_blank">📅 09:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132568">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8eA39g9akJT_E5W9FDHIDEbaRnBHR6H7kJvwnNGKBngrcT-kYUrqB0p7es0W63iUbpKd6pOntjf-5OR6kmpkNzenjSh0g6Fzd6u2a1sC7-2sH-WOpz_dsxaoUd-iHknimw50pDsMqMXMD-d9B-r2Hy9oCk5njLQw03ZG-W9PUosZIPJX9vce4Z2xPZh6OYy5vImWgRZ9spGNMBML04V_Nior4rO4I8W8U3A_lK_SGUAB3vkIg8JpNVvb4j4-nDrtmkZoACu-_HB-XZGaLGyARb8pBUrp6MX4SLtZpQnVkq5lYRSvWuvNFh1Hip3Ejg-KRGKjeVx2_YuPpnU7fTwCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🇫🇷
مسابقات گرنداسلم رولان‌گاروس رو با بالاترین ضرایب در اسپورت نود پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
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
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/132568" target="_blank">📅 01:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132567">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❗️
بین‌گلگهر و پرسپولیس؛ احتمال زیاد پرسپولیس راهی لیگ دو آسیا خواهد شد. اگه اتفاق خاصی رخ ندهد! گل گهر رضایت نسبی خود را اعلام کرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SorkhTimes/132567" target="_blank">📅 01:19 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132566">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CaMcLldpe_JjpgGb0g_hldgfKdiFR68b80aTTjpd6ApY0kg4E7yiXtLYlzyJI7lp5gqPFBHsc4X_eIEG-9rxJw7g7G_pI1qbE4Q1BzlZYsgfj1a52cS42X29ibVhZkGLBVHeXwVz1VJuLA7Ru1ANnj_FaSdMwNDzqcFVf16OoBodFhoh1A59F9AzqeMctzedB0SuIoKRtpxvAZSxzOXUFK_KciF6ob6T9flijfEYyozoL_FgkhhTKzF6xFy7Ns3n6d1dF5uCMc5XCBSBeuiUECimDMxQUi_73wOqFRNbqZ94UyKRbaSE01X5e89oDVbxqWROgmqQze1LSAN9bT40yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
یه سایت هوش مصنوعی اومده تیم های صعود کننده به مرحله بعدی جام جهانی رو معرفی کرده که تو اینا ایران تو گروه خودش دوم میشه و بالاتر از مصر به دور حذفی صعود می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SorkhTimes/132566" target="_blank">📅 01:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132565">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">⛔️
پلیس مکزیک گفته بازیکن های تیم ملی بعداز ساعت ۸ شب بیرون نرن چون ممکنه لولو بخورتشون..
😂
🤧
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/132565" target="_blank">📅 00:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132564">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">⚪️
مهدی تاج:
فدراسیون فوتبال دارد تلاش میکند که سپاهان از آسیا کنار نرود و اگر سپاهان نتواند پنجره‌اش را باز کند طبق روال جدول لیگ نماینده ایران به آسیا معرفی میشود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/132564" target="_blank">📅 00:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132561">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✅
شنیده ها :مدیران باشگاه پرسپولیس با مدیران‌دوتیم چادرملو اردکان و گل گهر سیرجان تماس‌ گرفته‌اند تا رضایت این دو باشگاه رو برای رفتن سرخپوشان به آسیا بدست بیاورند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/132561" target="_blank">📅 23:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132560">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❗️
لیست مازاد فعلی پرسپولیس به ادعای تسنیم:
🚨
سروش، پورعلی‌گنجی، سرلک، بیفوما و گرا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/132560" target="_blank">📅 22:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132559">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❗️
خب سپاهان که مجوز نگرفت. گل‌گهر هم بازی اضافی‌ش حذف میشه و چادرملو هم فاکتورهای لازم برای مجوز AFC رو نداره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/132559" target="_blank">📅 22:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132558">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‼️
امید فهمی مهاجم جوان سابق پرسپولیس به پیکان پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/132558" target="_blank">📅 21:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132557">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
خبرگزاری فوتبالی: استقلال داره لابی میکنه که قهرمان لیگ اعلام شه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/132557" target="_blank">📅 21:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132556">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✅
ترامپ: بهتر بود اصلاً وارد ماجرای ایران نمی شدیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/132556" target="_blank">📅 21:44 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132554">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✅
اگه تمام نماینده های پرسپولیس در لیست تیم ملی برای جام جهانی باشند چقدر پول گیر پرسپولیس میاد
⁉️
🔴
نماینده های پرسپولیس : اورونوف - سرگیف - نیازمند - کنعانی - ابرقویی - محمدی - علیپور - محمودی
🔴
یکسری از رسانه میگن که الکسی گندوز هم اگه بره جام جهانی پاداش…</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SorkhTimes/132554" target="_blank">📅 20:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132553">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
ادعای نیمکت نیوز : مهدی لیموچی امروز درخواست فسخ با سپاهان رو داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/132553" target="_blank">📅 20:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132552">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
توییت پزشکیان بعد از خبر اعلام استعفای آن توسط اینترنشنال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/132552" target="_blank">📅 20:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132551">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEYHzV8PopPRqUhjCTVj5PZ829MWAQncsGljr-uspRfNvdeyD4VWRZoPWGeDQtjP1ra9sRQ7sefmU7TUeYnJ22KpuQ0T9seFIca2g6NwNRUtFZPcw8lRsZV1ZnuwDW3G82ML86J1VETp7WUbVFmCVheIEJqpzHwK6VVB_9RbSU2G-Jz7vm2jrKr67Mh4fZtlvopeLlVS7dFbsGce8JKgcMOZJ4sdUX6kFwvdhj5WyUsD0E5cmvhm3od5SOc2luLueVzXzlkRAzuagbWZbbIvkyT7cYIxlSU1xbA1ys-LQtNQxLixyuBnirWD29OxUYGi4vhMFFaHq5sQmy5MEMn3yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
خب سپاهان که مجوز نگرفت. گل‌گهر هم بازی اضافی‌ش حذف میشه و چادرملو هم فاکتورهای لازم برای مجوز AFC رو نداره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/132551" target="_blank">📅 20:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132550">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u15c-_jodZ3EMqwd4IX13qjqF1_tupeOS5zbd5EwjV0CJ4bPizpNRi3EInfu65O0rugRlS3Ixz2HigalHvxE4YGssnZj79zh9EACZySXLu40qaX3oqqLdDnhsiKz-tYrLJyvr5xP0blKVqodiCv10-8ilA0TMPPnIfrBvJJGppfG674xo318ycAUlIJtsoPZR49vEOGGJQ9KQEd9bQyeG6QZrhTXP5rwRzCFvHiftWWcYqKDvgesg6ixj35Ru98EkphaHXVgWne54PMUd6ZClgSfd_s094uOardexXBK80yarSo100dnrB-EOKCa3rRqPHUCS0nrk6lVs2sCWtQ-Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
توییت پزشکیان بعد از خبر اعلام استعفای آن توسط اینترنشنال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/132550" target="_blank">📅 20:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132549">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🟡
سپاهان حذف شد
▫️
گل‌گهر یک بازی اضافه داره
🔸
چادرملو از بازیکن غیرمجاز استفاده کرده
🔴
پرسپولیس برای ۳ امتیاز بازی با ملوان شکایت کرده
⁉️
باید دیگه چه تصمیمی گرفته میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/132549" target="_blank">📅 20:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132548">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✅
طبق جدول لیگ برتر؛ گل‌گهر با یک بازی بیشتر ۳۶ امتیاز دارد و رده چهارم است. چادرملو و پرسپولیس هر کدام ۲۲ بازی انجام داده‌اند و ۳۵ و ۳۴ امتیاز گرفته‌اند. در صورت معرفی گل‌گهر، قطعا هر دو باشگاه اعتراض خواهند کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/132548" target="_blank">📅 20:44 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132547">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USFMR2KRRuAkYM7GC2d8dzY0500TgyIEowcAruAnY9aChFxdoJhAewfMUiokDsVXyvTCA4ZKvw2yYhB5B-x2DZo8xNcvCOsavU_Nf9smo-5Efo9P_q08BWiSVpid9wqoa-Lf8KZlqUs-U073huzdItp_fLwW42Zj0UHkMpMSzKCOT94B64bGoSUX7wYRCSnzYuwR6kIm7GXZDiEnACOqnCM6-JrUIpfXb92cvcgcaplpMUJSLK2DKuG8ry5bHPFL4RQvAyjmu_yKVdaLVYJLE5MI4VUlxcZwQ29uH8-H0_k4bfai_jy9Gkt7GdOJRlUWKpHUQ9llUyQIo2d65wvXDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی سریع و مستقیم به وینکوبت
🟢
فرآیند ورود به سایت به شکلی طراحی شده که کاربران بدون درگیر شدن با لینک‌های متعدد یا مسیرهای غیرضروری، مستقیماً وارد محیط اصلی سایت شوند.
📌
این دسترسی از طریق ربات رسمی انجام می‌شود:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
🟢
به جای روش‌های قدیمی ورود، این ساختار یک مسیر واحد و ثابت ارائه می‌دهد که همیشه قابل استفاده است.
📌
کانال رسمی وینکوبت:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/132547" target="_blank">📅 20:32 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132546">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/132546" target="_blank">📅 19:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132544">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
گل گهر، چادرملو و پرسپولیس به ترتیب به علت حضور در رتبه های چهارم، پنجم و ششم در صورت کسی مجوز حرفه‌ای جایگزین سپاهان در لیگ قهرمانان آسیا سطح دو خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/132544" target="_blank">📅 19:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132543">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">فوری
⛔️
‼️
با مخالفت Afc, سپاهان مجوز نگرفت و از آسیا حذف شد
◻️
کنفدراسیون فوتبال آسیا به دلیل اینکه پنجره بارگذاری مدارک  باشگاه سپاهان بسته شده است، مدارک مجوز حرفه ای این تیم را نپذیرفت تا به این ترتیب این تیم از  حضور در لیگ قهرمانان آسیای فصل آینده حرف…</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/132543" target="_blank">📅 19:32 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132542">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">فوری
⛔️
‼️
با مخالفت Afc, سپاهان مجوز نگرفت و از آسیا حذف شد
◻️
کنفدراسیون فوتبال آسیا به دلیل اینکه پنجره بارگذاری مدارک  باشگاه سپاهان بسته شده است، مدارک مجوز حرفه ای این تیم را نپذیرفت تا به این ترتیب این تیم از  حضور در لیگ قهرمانان آسیای فصل آینده حرف شود.
◻️
به این ترتیب حالا  یکی از تیم های گل گهر، چادرملو و  پرسپولیس طبق مدارکی که به ای افرسی ارسال کردند شانس حضور به جای سپاهان را دارند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/132542" target="_blank">📅 18:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132541">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-ynu9SjEIDkUBJWZ1DtxZbjdk0xVHWneYKaZID0_0n1KkDLi0ziwSHmBJpX7lCXLMuoJ8q1qzdIgDTyvtiRAwzz6HUhSEhvOJ2OKPJWSD2zx8K1WrxkXRnTtIjqi9bLjNxbKXl1udeRPY2Rq8wrBG_hth-ZBAjG_8cIIJLBDKhMQNafm4UfzC6FEVBAP3Hel9VzySteWS_oCqLrK7obXiGoyNj_msPFnLxItJDrDVx2h7-9NJSysDjftVVlt511K1djI325WjLqmOcGnucFj_Y-5_dLozTuBrBCfbnAprQAr_crh3IRm4vclLnllDd_rVfl7ih5nreXV2nHtLsP6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سهیل صحرایی، مدافع جوان و آینده دار پرسپولیس، دیروز ۲۳ ساله شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/132541" target="_blank">📅 18:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132539">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
خبرگزاری تسنیم:
◻️
باشگاه پرسپولیس به دنبال جذب چند بازیکن جوان و ملی است تا میانگین سنی این تیم را برای فصل آینده به طور چشم‌گیری کاهش دهد.
◻️
بازیکنانی مانند سروش رفیعی، مرتضی پورعلی‌گنجی، میلاد سرلک، تیوی بیفوما و دنیل گرا از جمله بازیکنانی هستند که به احتمال زیاد فصل آینده در جمع سرخپوشان حضور نخواهند داشت.
◻️
مدیریت پرسپولیس از طریق چند واسطه پیام‌هایی را نیز به چند بازیکن جوان و لژیونر ارسال کرده تا شرایط آن‌ها را برای جذب بررسی کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/132539" target="_blank">📅 17:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132538">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❗️
🗣
حمید درخشان:
🔺
در حق پرسپولیس اجحاف شد؛ در ۸ بازی باقی مانده هر اتفاقی ممکن است رخ دهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/132538" target="_blank">📅 17:23 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132537">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBw3C4kpPHEa_OfACM7fs5taDqPW6ssczr-SoLJoKvUfA4uSwcIzTDIcmt9yBJgm9JkpT59IrSMUCGf942UBu850bn3RdqeY6aHaUyXFsdqbC6gv2o7T4keNAINTymD_FFgI8K4dtNhoKiuczLaNU9oYpkEootbBFY9p3-zqnEZbnnXsfH8uuMIFCCC1oQ2I23Tun1_z03MxdgJchRr7jXbQIL24XBpNk9thiQBsDRzrFpvn5hAXzuo5AEZ2hzaljQOP1IcsZ9T-6bGnvzVekMyp3vM6CdNMQ--yNJY8fPEawxKkMxzhqRpqRmyA1JXltIJPoq1OM_2EGE98LsE3MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قول بزرگ وکیل علیرضا بیرانوند به تاجرنیا رئیس هیات مدیره باشگاه استقلال: پنجره باشگاه‌ تون باز شود بیرو بعد از جام‌جهانی با تیم استقلال سه ساله خواهد بست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/132537" target="_blank">📅 17:11 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132536">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
خوردبین: تیمی که در ایران مجوز نگرفته چرا به آسیا معرفی می شود؟
🔻
آرزو به دل ماندیم متولیان فوتبال یک بار تصمیمی درست بگیرند. آقایان بگویند این تصمیم را با چه معیاری گرفتند. یک مثال بزنند در کجای دنیا با لیگی که ۹ هفته از آن مانده تیمی را برای حضور در سطح…</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SorkhTimes/132536" target="_blank">📅 16:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132535">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✅
ترامپ: بهتر بود اصلاً وارد ماجرای ایران نمی شدیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/132535" target="_blank">📅 16:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132534">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
فوری؛ با اعلام دبیر سازمان لیگ، ادامه مسابقات لیگ برتر برگزار نخواهد شد و نمایندگان آسیایی ایران بر اساس جدول فعلی تعیین می‌شوند. به این ترتیب پرسپولیس سهمیه آسیایی نخواهد گرفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/132534" target="_blank">📅 16:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132533">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huJJ1A1VMTulQOPxxjAPeLhWuo4TIiWSpFJxr3IgfCk3dwzopfynWcV1hZfil-CO3Zv2kmwA1eITDWPuP2R_INgoxDkSlbiDz7kXyfVIKQmydaji-g9zGPNJYy6T0GIjCOEnnpubpHarhNEqCfq_1b-OVbu7ebp9xLsguH57c8_liEfRLDBGi-1ef-3zs4D746zcdj5Etrfaf_OL8buW9vibsKBf-8pMvBQw7bUYWJrRc4Lq9FAmMwk57kry-CvcgNcPYG25D5vhYVjSNHpihzOJq9nFjuYK-WN3pLiRQg4ZNjwBLkZ1m7-ell6bnwx7qiBzs5i_ZjBexSvcMPAZ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
مایل به تمایل…!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/132533" target="_blank">📅 16:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132531">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fbf80TVFaCT3p9cQo9-G_SWHupofYFo-aIbuB-_G58tGZ5wyQE5dSoVeLn8QoUkKVZ9M8b-NZlgIDNSPEJdQsWf2sJF7s2NXxkq8EWdT6_DriF2fCE3TBilIqqhdhCnVbpMtM-tZ1TreElRensXK6H5WR7K_B-IvPaSxEpklraOSJaGC177Er50LAaOIoCi8CXk3ox0UsZ1-dEkWoe2Z5_h1rUiIFK6303sBJeRYfiQJNdCYOSke5vF1O-2gYjgYMgcrVsEHQ5VQpVN1jaOnIxObTq4i_u1ZmEE4Qqn0nSP6nTfV0TDFE9-DOg1Q-uSabYcBPlxZjilbr_OUhL_Qag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دسترسی دیتاسنتر همراه اول به اینترنت برقرار شد
🔴
اولین نشانه بازگشت اینترنت به دیتاسنتر ها  باید منتظر باشیم و وضعیت بقیه دیتاسنتر ها رو هم ببینیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/132531" target="_blank">📅 15:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132530">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
اوسمار به باشگاه پرسپولیس گفته واسه فصل بعد بازیکن خارجی می‌خواد و از باشگاه خواسته اگه جذب خارجی ممکن نیست، زودتر بهش بگن تا گزینه لژیونر معرفی کنه
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SorkhTimes/132530" target="_blank">📅 15:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132529">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e786c6b741.mp4?token=NWU_7EU5uoHVAOxRNo6KvB_mrl50wV5XJKLyi1yzNHS7z95rMFwZw5ZNs2KM-NUqU_Nx7NlonrqNehTzsN1XzktuwJw07jFsg1o75zbsxS4ik4K2wUrOGwcMf_DHfDSW1It9l54QMqFDz67hqNh8CX4YeylcNXanLV0O2MuzcRnf6Gen3RHTUjvOt8sgluOKl9pPh1XzuTbHUMxd7SrKN_0siRqfl0pRAvU4Vy_zqIyPu1dr0ymxWMRTCLWTpMJcPG50n9SincVg2leHYZDLy01S8vhfXYT7KbQIT_YXX4WmiHy89FKF2TwyyydRimgq-3VBzX5c4RqJ8lVA-qunNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e786c6b741.mp4?token=NWU_7EU5uoHVAOxRNo6KvB_mrl50wV5XJKLyi1yzNHS7z95rMFwZw5ZNs2KM-NUqU_Nx7NlonrqNehTzsN1XzktuwJw07jFsg1o75zbsxS4ik4K2wUrOGwcMf_DHfDSW1It9l54QMqFDz67hqNh8CX4YeylcNXanLV0O2MuzcRnf6Gen3RHTUjvOt8sgluOKl9pPh1XzuTbHUMxd7SrKN_0siRqfl0pRAvU4Vy_zqIyPu1dr0ymxWMRTCLWTpMJcPG50n9SincVg2leHYZDLy01S8vhfXYT7KbQIT_YXX4WmiHy89FKF2TwyyydRimgq-3VBzX5c4RqJ8lVA-qunNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▪
︎ اگه این روزا سایتا سخت لود میشن، ربات تلگرام وینکوبت خیلی کارو راحت کرده:
👇
🤖
@Wincobet_bot
بدون اینکه از تلگرام خارج شی میتونی مستقیم وارد بخش بازی‌ها و کازینو بشی، پیش‌بینی ثبت کنی و حتی واریز و برداشت انجام بدی.
▪
︎حالت Mini App داخل تلگرامه و خیلی سبک‌تر و سریع‌تر باز میشه:
👇
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/132529" target="_blank">📅 14:39 · 10 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
