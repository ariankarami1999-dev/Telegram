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
<img src="https://cdn4.telesco.pe/file/rfZxNaZRzCnRMW6V8KuJ2HXJ4OsmCl2Lph3gLhzhzUCurgXYYTKBlj2c08bxWTOOzuIupNWTqTF6xW7fQyv8lR8ZQUO-Z9bNS7lUyYk59tlMBJ7-ZvPzKNFYMBTeH7BnbG18ZObbhWDBDX97g0thnC4hNQdZpe4KA9NU81EtAVH85-TDkh3eOK4AtVxuF1kil0-cES4g_IouISKP6N3qlXs7IkexQvKQ9dj84oNzBKTorIDK7o8vzajmvG7WSqSUAYzRSBRt7rPfz7hNCcXg2ETipvXeJ5mSW_XsJ59lcc8VGzadVlMpwikdwx34-8FNJKZoU0g6DOoYlAL5Pp8-5w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-13 22:09:04</div>
<hr>

<div class="tg-post" id="msg-140998">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
فووووووووووووری
🔴
علوی: هیچ جامی قرار نیست به استقلال داده بشه و بحث قهرمانی این تیم در سال گذشته منتفی شده
😂
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 762 · <a href="https://t.me/SorkhTimes/140998" target="_blank">📅 21:58 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140997">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D84YggrhSgR9JhFpqWPrUujNtTo_TK23Pj9_z4qzIaQZvYOmycwmdSbyOrzPSdzJqULywLFTDi23OO_S6SeVWSUNTGwGfEZnp3pqcgS1Fw7As8HojDwLNOcPiLem7-F8naWh77Nv-XMFB-g5ZmVyC3wEttL3X2vjFDdeVk4f9HbqzgxET3b65ZS3zaxNQ2dxecp0nGOcp1WvbDCLnfJwxMgCu-4BLTSpZmx5pXS1Rp5492Q8yDIES1tBrHdUNgtfzryJZXu6iZsKfQ7__AJPdyI9Ho0Z_d_UVAWUvk-STLYWHJQZ_wd-ys5TuK4atycohYGnRdZSNUniAa38o6ODGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚩
گزارش تصویری از تمرین امروز پرسپولیس
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 853 · <a href="https://t.me/SorkhTimes/140997" target="_blank">📅 21:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140996">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">💚
عادل فردوسی‌پور: دیگه حوصله شوخی‌کردن با قیمت دلار روهم نداریم، روزگار سخت و تلخی که سپری می‌کنیم، شروع فصل لیگ برتر، با دلار 187 هزار تومانی، بازگشتش از فیفادی، با دلار 270 هزار تومانی!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 884 · <a href="https://t.me/SorkhTimes/140996" target="_blank">📅 21:56 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140995">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
گفته میشه دولت قطر به تیم فوتبال استقلال قراره مثل آمریکا ویزا ساعتی بده تا این باشگاه برای بازی با الغرافه مشکلی نداشته باشه
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SorkhTimes/140995" target="_blank">📅 21:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140994">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✖️
✖️
✖️
فرصت طلایی
✖️
✖️
پرسپولیس در هفته‌های پیش‌رو برنامه بهتری نسبت به رقباش داره؛ استقلال و تراکتور درگیر آسیا هستن و سرخ‌ها هم بازی‌های عقب‌افتاده‌شون رو دارن.
✖️
✖️
با توجه به لغو جام حذفی، هفته‌های ۹ و ۱۰ می‌تونه فرصت خوبی برای تارتار و شاگرداش باشه تا…</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/SorkhTimes/140994" target="_blank">📅 21:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140993">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
لحظه گل ثانیه پایانی جوانان پرسپولیس مقابل پارسیان توسط محمدامین قرنجیک
👍
👍
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SorkhTimes/140993" target="_blank">📅 19:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140992">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1mKrZsW2JlxSp7JRkzFP43sc-FFPoNLTQxSmEgAH_XCvwV1vaxaKgO6RmjqnX3gBoBXLU_egign1Kyer4k05c4lcfk60u9iEgyWbOVjuT4Tgp60c3SuWer8X4n6177YdYL-04B2W16WHl4pDlVekGNqm5MoerXp-uLB2QtF8QgtCh6dNN5fTy2x8gVD6tQCc6Sw75nnssyxcPtxXR17iKN8uuWUK6LJhJZXAfElRzDUFZgLMn0Wbmddv1z80eUzKcsyJcMa0lK4O69NgtEWoZjBuljujL_WqavR3VX2BEcQocp5qt6fFlRYhyIg5xe9DtBy2z0vpbV_RfUmzDRZPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
مهدی طارمی زمینه آزادی ۸ زندانی شد
👍
مهدی طارمی در طرح حمایت از حقوق اجتماعی و رفاه زندانیان نیازمند استان تهران، زمینه آزادی ۸ زندانی را فراهم شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/SorkhTimes/140992" target="_blank">📅 19:48 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140991">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
مزایده اموال پرسپولیس با یک خریدار خاص
🚨
در پی شکایت یکی از طلبکاران باشگاه پرسپولیس، دادگاه شعبه ۴۱ عمومی حقوقی تهران حکم به توقیف و سپس مزایده اموال این باشگاه داد که این مزایده در نهایت برگزار شد و بخشی از اموال پرسپولیس به فروش رسید
🚨
🚨
در این مزایده،…</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SorkhTimes/140991" target="_blank">📅 19:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140989">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmN_5mXObZryhu529bywKs6UcZR0y_cJg4nLdfhv5s6PZUQuc8YoxesZv2QnFWmN17kZeq8gnJvZtC1pEpojuGh_J4G2PHNaCOm7QYIpGHb9WFWlwWoZDzyxBGThNA-SaekT7ND8XyPHJ-E4Qq4LopMJXLHpFlHCtlWBm0J6kvdQYPjRpgx4hpwvanzPA_r8wb65UwUlY2eLrwlZxcNtmU7-wpdYQqDR7lWRxOK6saRnFHxbHvRHGKCqD-SirVDq58nMHpa2hMmdO08HBJhjungXxPvI9czXuzaVr91lFAnzglnwYvZ5Wb6lK0rUuoMwhbBE2kqXUvxil9vSmA6BGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نبرد سلسائو با وایکینگ‌ها؛ پرتغال در برابر نروژ، یک شب پر از هیجان!
🔥
⚡️
[
فرانسه
🇫🇷
🆚
🇧🇪
بلژیک
]
⚽️
فرانسه از نظر کیفیت موقعیت‌سازی و عمق ترکیب دست بالاتر را دارد، درحالی‌که بلژیک بیشتر روی ضدحمله و انتقال سریع حساب می‌کند. با توجه به قدرت هجومی دو تیم، سناریوی گل‌زنی هر دو طرف محتمل است؛ اما فرانسه شانس بیشتری برای کنترل نتیجه در نیمه دوم دارد.
سناریوی محتمل: برد فرانسه با اختلاف یک گل.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SorkhTimes/140989" target="_blank">📅 19:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140988">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔵
اعلام برنامه مسابقات هفته‌های هشتم تا دوازدهم و دیدارهای معوقه لیگ برتر
✔️
هفته‌هشتم جمعه ۱۷ مهر
🔴
پرسپولیس - صنعت نفت آبادان ساعت ۱۷
✔️
معوقه هفته هفتم لیگ‌برتر چهارشنبه ۲۲ مهر
🔴
پرسپولیس - خیبر خرم‌آباد ساعت ۱۷
✔️
هفته نهم لیگ‌برتر دوشنبه ۲۷ مهر
🔴
پرسپولیس…</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SorkhTimes/140988" target="_blank">📅 17:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140987">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✔️
✔️
🚨
فووووووووری
✔️
ای اف سی در نامه ای به فدراسیون گفته پرونده فسخ یاسر آسانی مشکوکه و جزییات دقیق خواسته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SorkhTimes/140987" target="_blank">📅 17:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140986">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dsR2LKaG_vslFZnbxA4t5GTIAONt3WVuSn0IkNoPm_AyGV2UMxWrPy5chFgcU2u7q5f8AaRcgDJBTESoL1l9uaoiKBPjs1GLg4oRGNxU1poZCb-nFMsLrIXe6afcUmbl3PyPtn5mubPH1pa9Iccrs7Di1YyK5UBBLzUJo--bj4dItMP2w-AMOkphE_n1xBrpkYvBrktmEb65bmMeuQ11pbCjK5aBdCjGRJb08lMpeCuYRGK6H5QvCSEi-0Xvp-N4-STLg-Nc6OO9ExY9Ve6M6Lm0Nv_OiWLnGVzMC-AWyolzyLoRtSz5mOs4CtVdDD9hEpYiW4EOw2GRtPzcqtxOqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
ساختمان شهدای میناب باشگاه پرسپولیس مزین به تصاویر شهدای مدرسه میناب شد
🔴
به گزارش سایت رسمی باشگاه پرسپولیس، این اقدام، ادای احترام خانواده بزرگ پرسپولیس به مقام شامخ شهدا و خانواده‌های معزز آنان و گامی در جهت پاسداشت فرهنگ ایثار، فداکاری و شهادت به شمار می‌رود.
🔴
باشگاه پرسپولیس ضمن گرامیداشت یاد و خاطره تمامی شهدای مدرسه میناب، بر ضرورت صیانت از نام و یاد شهدا و ترویج فرهنگ ایثار و فداکاری در جامعه تأکید دارد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/140986" target="_blank">📅 17:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140985">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBWPibePsE_21SOM_UqEYhFlTDL8K_gOLGuXPSq710oIWedLQOb604EAncIwPaV_BdXx-UExMnijGyCYSzFU37UR68xPqJ7xkkcciY-tIHWGonsCcsRM9sNTgnd1T9kUbzyuBtppeKfIJBxJ0JQ8aRXAF00VVS6yUKgZhl_kKD8emLryGUF6MzSaHDbTDY0G-WuWibitQ0EsMsaI0c9hIHJIcGxK5Fpn_WrRv2C0pHJ6877g8FwAqi4JJpKDG0Ow6gddqpq_VTQY3ymZdChdcOUOS02FkzZvL9cwVYupVn07CvCBfj0bm0AX04OtZcZ8S7zEWkzu6KsW1GEq9iHN-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
✖️
سیدحسین شریفی به عنوان مدیر صدور مجوز باشگاه پرسپولیس منصوب شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/140985" target="_blank">📅 16:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140984">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
نامه دوم AFC برای بررسی پرونده یاسر آسانی؛ پاسخ نامه اول قانع‌کننده نبود
🔹
کنفدراسیون فوتبال آسیا (AFC) پس از دریافت گزارش‌هایی درباره وضعیت یاسر آسانی و احتمال غیرمجاز بودن حضور او در ترکیب استقلال، در دو نامه از فدراسیون فوتبال ایران و باشگاه استقلال…</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/140984" target="_blank">📅 15:13 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140983">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
کنفدراسیون آسیا جواب فدراسیون رو نپذیرفت
✅
کنفدراسیون فوتبال آسیا برای بررسی پرونده یاسر آسانی، این بار در نامه دوم مدارک و مستندات بیشتری از فدراسیون و استقلال خواسته و تأکید کرده فوراً ارسال بشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/140983" target="_blank">📅 15:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140982">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
کنفدراسیون آسیا جواب فدراسیون رو نپذیرفت
✅
کنفدراسیون فوتبال آسیا برای بررسی پرونده یاسر آسانی، این بار در نامه دوم مدارک و مستندات بیشتری از فدراسیون و استقلال خواسته و تأکید کرده فوراً ارسال بشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/140982" target="_blank">📅 14:51 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140981">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/140981" target="_blank">📅 14:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140980">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✔️
✔️
🚨
فووووووووری
✔️
ای اف سی در نامه ای به فدراسیون گفته پرونده فسخ یاسر آسانی مشکوکه و جزییات دقیق خواسته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/140980" target="_blank">📅 14:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140979">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
⭕️
⭕️</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/140979" target="_blank">📅 14:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140978">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
⭕️
⭕️</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/140978" target="_blank">📅 14:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140977">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
والیبال به میرزایی رسید!
🔴
با حکم احد میرزایی؛ رضا صفایی سرمربی تیم والیبال پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/140977" target="_blank">📅 14:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140976">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
❌
سعید دقیقی در لیست نقل و انتقالاتی خود برای نیم فصل خواهان جذب سه‌ بازیکن از پرسپولیس شده است
🔴
حسین ابرقویی نژاد
🔴
یاسین سلمانی
🔴
محمد حسین صادقی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/140976" target="_blank">📅 14:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140975">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGQsO9_cIDP6MTJbwy2smygqsM3t--cUq3cq889VPJmb8H_v2pOwHWNo0Zunrk6ntOpnV4s8WLeY3svuEDEQ5-yXJJjsJHrxFjXINw-rrIg93PaTbPorfnGjlQizwgmBvLZBDPRl0u_T-XpDNPEf79TRhoDaQFkx-PnOk7QN02PGHZQWCahw8RURe52X_sGaf84QOdJInNlFXK3Ccf6pwOC05fgHXmvSP4qMA5_XjdIquBr79seXVQ2Pfxv9yvhl-B3juXG-8yFM34VSO9KVA82z5DEyblVx0r613VbKzQ4uXZCqeuyAbGW1RzRShE5zTo2lPgdPEQc49tUqmUQS3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
Italy -
❤️
Turkiye
⏰
Tonight 22:15
🏟
Stadio Renato Dall'Ara
⚽️
ایتالیا در ۳ بازی اخیر ۴ گل به ترکیه زده و در ۶ بازی خانگی اخیرش ۴ برد با کلین‌شیت داشته؛ ترکیه هم در ۳ بازی لیگ ملت‌ها فقط ۱ گل زده است. باتوجه به برتری ۴-۱ بازی رفت و برتری تاریخی ایتالیا (بدون شکست در ۱۵ تقابل)، کفه آماری همچنان کاملاً به سمت آتزوری است. احتمال می‌رود ایتالیا کنترل بازی و مالکیت بیشتر، ترکیه خطرناک در انتقال‌ها باشند و باتوجه به‌فرم دوتیم برد ایتالیا با اختلاف کم محتمل هست.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/140975" target="_blank">📅 13:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140974">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✅
✅
✅
#فووووووووری از تسنیم
🔻
جلسه کمیته استیناف برای شکایت پرسپولیس از آسانی امروز برگزار میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/140974" target="_blank">📅 12:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140973">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YISn8odymVu8m8vi3lmBt3KlzeuiqVjurJVdJ55ODWdUg3vv1PQEKyZprPWIplr05u0HhnzQAmZqxwPBzzONcPiFwhy2cVGMpHx6C7WjZnhKEQIspIohtWg4guDV_lgxm4CWKRyAJ713g6i6SMyIBjDoSYOBQxRUqborsqRmcDI8eL10YNBs99MYICrWfwZo27CvYMmVH9Qm5qG2K-e_6OXc86Oo9yl-3_EkzuGKtJ8eYAbB-Fvz8lKJIzLa3FIq7lJlRUzSZLDa7GOIZZAUpguNf8Y9VLYnOWFyVxZrwPQp2jywk-N7kRDroum7e-EK8CGlI0ReORlJJHb4Uqkj9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مهدی تارتار قصد داره از پویا اسمی مدافع ۱۷ ساله‌ی پرسپولیس در بازی‌های بعدی استفاده کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/140973" target="_blank">📅 10:59 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140972">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdEa_chk3_I8w0a9B2ZZ3hf4CXmChJcVNbdU-dan8MxjoAzIpDy1Vq_YSib-DqFit2YHKb-BvzIN78FMg9gKfiRvW5hs7oOmox1DSc2X5DOhpHXPQp6yldzv9Nl4gfc9PIxoZfZ171FjgkIGYIheum-s9R7uoE4QYstsVHv0_A7jMQQAQOu4HBdwmzWZ0tyUlIM88olIlDwspJ5eMNcGVTxPS08FsST_YNbSmjhxF-sZPB7ykkePedm8KMbqStqq1JwhBySnb2Xfjwz9JijIJSIpDYPwy7zEtWVuPWS7dBab07PWdk9MNqoJisLVeOfGm-q32CyJDU6AB3GbBofEwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوووووری
‼️
🤩
با اعلام خبرگزاری برنا
بازیکنی که مدنظر پرسپولیس بود
شرزود آسانوف ازبک بود که بین
دوراهی تراکتورسازی و استقلال قرار گرفته !!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/140972" target="_blank">📅 10:55 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140971">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✅
عادل فردوسی‌پور: نیوزیلند جزو سه تیم ضعیف جام جهانی است. اما برای نتیجه نگرفتن احتمالی، برخی بهانه‌ تراشی می‌کنند. برو بجنگ بعد درباره ویزا حرف بزن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/140971" target="_blank">📅 10:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140970">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✅
✅
✅
#فووووووووری از تسنیم
🔻
جلسه کمیته استیناف برای شکایت پرسپولیس از آسانی امروز برگزار میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/140970" target="_blank">📅 10:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140969">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🤩
حدادی: برای آسانی مدارکی داریم که هیچ باشگاهی نداره؛ فدراسیون هم باید استعلام فیفا رو منتشر کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/140969" target="_blank">📅 10:44 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140968">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✅
✅
تاجرنیا: بیرانوند دوست دارد حضور در استقلال را تجربه کند.
😀
به صورت جدی درباره بیرانوند صحبتی نداشتیم اما به ما هم پیامهایی رسیده است. اما الان فرعباسی و خلیفه را داریم بنابراین بحث بیرانوند یک مقدار این موضوع از ما دور است.‌ در هر صورت او هم شایسته است…</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/140968" target="_blank">📅 10:38 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140967">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZsbHIeghex2gZbh_nUmr2_iyTD2Jrikys964LEtkaW-zVtdCzmRnCEYSXnXrKjavzgkzF0vENfYKV9WuHFj7gNlWPXgGnLRPgTFfScDJ9bVeAaQFpTiaMPyBh0jNxNpNBvTMEI7Hx1fg7X75unSnQjDK1JhLlhcEi6a-JR4a8D6qUJbIY_ZOWkuMEadwiGmatx7xOr1PRs86UpNvN_ZYeBRXo4awRWij8kPb8OfvPWlaBUMa3QSw8jUG1JCwb6g9X788IvFZXibQQmN-4VEkgoXsGz-RDPJiaGbYhZKDbOhqynSqfzg_Vu0W71GVFfGJYUw7Aer5pXzSAkQIHYTWEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شایعاتی از نهایی شدن انتقال فرهان جعفری به پرسپولیس به گوش می‌رسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/140967" target="_blank">📅 10:37 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140966">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">⭕️
⭕️
باشگاه پرسپولیس با خرید امتیاز باشگاه پادیاب خلخال صاحب تیم «ب» شد.
🆕
🆕
🆕
عصر امروز با حضور مدیرعامل و مالک باشگاه پادیاب خلخال در باشگاه پرسپولیس، امتیاز این تیم که امسال در لیگ دسته دوم حضور داشته به باشگاه پرسپولیس واگذار شد.
🔜
🔜
راه‌اندازی تیم «ب» یکی…</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/140966" target="_blank">📅 10:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140965">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
❌
مهدی ترابی در بیمارستان‌ آتیه تهران تحت عمل جراحی رباط صلیبی قرار گرفت و زانویش را به تیغ جراحان سپرد و شش ماه از میادین دور است.    «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SorkhTimes/140965" target="_blank">📅 08:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140964">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✅
حدادی : در یک بازی رسمی از عالیشاه تقدیر میکنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/140964" target="_blank">📅 08:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140963">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8MJzML16UPDtycgIfLPNKACMhI4go31xx7iUXSj5YLctOH6JnvqrlNMJZLkAo4CohiIIX6KF1WQyiYGp9TXffiE2zbjjgimfsAouWhgLdE-qyeFrBqWFkO5sbM61Dfyti2ZDnBVGLsVgvlaaW7bXmPvmA2AOUa9LsCKbYlNoHcYYapDAepoWUfKqEFKz52rFPt0sB2ACgpSAnrpXw0DuMf8aviyzIJEiLkJxSSe0LtckJJEdm422Q2Rq-FtX5AKllae6c5n5nPMqt_geVNbHoUQuABrbpTFKw02H2dMrH1nHIWICin-fBD-_Ic9KZS4IlqgXAMgJ-AbERdRzOZgfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/140963" target="_blank">📅 08:18 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140962">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8U7ICYLjiJuGXMHjfTfTfQM05HjVHDjpbdNy-mIGidK-DaJXiJPCYp-DlrTy3PeoTN7NYbXGbFFzlycOzyUaDzVk7J5acgJ8BvYa6qj2hDDkHnDkSVFaA5Cp_Kzb0ek5OP8SYrVj-E02an3BFWWfbJkEf-NtISF11W25DaACamIrAWEjiYF4i7vkkLmQezWY69PfxRed0k2jf13MqS3Z6J-5iq3NVgygL9isd6Rcb8OwckFysEOUxVxq4MO75El5joRsYun5wvwBj42FU13ms4kwMyeb-tAM0_CCZY9IotG61-4r52xtF1F_tKmzHM7MPyA4KhYEbqe_VVHPfaQDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
France
🆚
❤️
Belgium
⏰
Monday 22:15
🏟
Stade de France
🇪🇺
فرانسه از نظر کیفیت هجومی و میانگین موقعیت‌های خلق‌شده برتری محسوسی دارد و احتمالاً حجم بیشتری از حملات را در اختیار خواهد داشت. بلژیک در انتقال‌های سریع خطرناک است، اما مقابل فشار و مالکیت بالای فرانسه احتمالاً فرصت‌های کمتری برای تهدید دروازه پیدا می‌کند.
✅
برآورد آماری: برد فرانسه ۵۸٪ | مساوی ۲۴٪ | برد بلژیک ۱۸٪ | بالای ۲.۵ گل ۵۷٪
همچنین در غیاب دی‌بروینه و تیلمانس احتمال می‌رود خروس‌ها پیروز میدان باشند.
🟢
با درگاه بانکی اختصاصی و امن وینکوبت، حساب کاربری خودت رو به‌صورت مستقیم شارژ کن و مثل هزاران کاربر دیگه، بدون دردسر از امکانات وینکوبت استفاده کن.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/140962" target="_blank">📅 01:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140961">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">💢
💢
مدیران پرسپولیس به تاج اعلام کردن اگه استقلال قهرمان لیگ اعلام بشه از لیگ برتر انصراف میدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/140961" target="_blank">📅 00:58 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140960">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✔️
✔️
حدادی : نمیتونم قرارداد محمودی رو اضافه کنم چون باید به سازمان بازرسی جواب بدم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/140960" target="_blank">📅 00:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140959">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
❌
فوووووری
🔄
🔄
حدادی: تا آخر همین ماه یه جلسه مهم برای بیرانوند تو فیفا به صورت ویدیو کنفرانس انجام میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/140959" target="_blank">📅 23:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140958">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TH_kn5w57zw3ivNkIHgLefcDyCC4UrOSJjdRRsWi6iGtMAR2X-ou29iEWrspvtYqUCqtigb0DhSZ0W-Jb3aAuFO0GaOiFAz9PUrWMm-CpB1COWH0EsBad0unjS4bYG5v7-bP0cMuTEaayZavZ2cneDIVVnO-ffRRIOFgWerQh4eob2-t7-xMkFhZD5pMJ2JeNz0ZS_Y3SAXZ__3zaCuQY-btpJN5tDm0QvX2b4r6NWMC9Oj7gOL53DqoP-MT1dfB6AELnglBr_atWl9elU7eR9N7fuutoXoxBStwvUNXlW9Uf6p8Kbbk-rVsk6qxh6WFCXD6gD_aKQKYUVOLv9hgmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
⚪️
برترین بازیکنان لیگ برتر تا این لحظه از نظر متریکا
1⃣
⚽️
🔻
علی علیپور 7.7
2⃣
⚽️
🔻
سعادت حردانی 7.49
3⃣
⚽️
🔻
اسماعیل قلی‌زاده 7.49
4⃣
⚽️
🔻
تیبور هلیوبویچ 7.48
5⃣
⚽️
🔻
یاسر آسانی 7.46
6⃣
⚽️
🔻
محمدمهدی محبی 7.45
7⃣
⚽️
🔻
عباس کبیریزی 7.44
8⃣
⚽️
🔻
امیرحسین حسین‌زاده 7.39
9⃣
⚽️
🔻
مجید عیدی 7.37
0⃣
1⃣
⚽️
🔻
امیرمحمد رزاق‌نیا 7.37
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/140958" target="_blank">📅 23:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140957">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✅
حدادی : در یک بازی رسمی از عالیشاه تقدیر میکنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/140957" target="_blank">📅 22:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140956">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
❌
❌
خبرنگار الجزیره در تهران: به نظر می‌رسد که همه طرف‌ها در حالت آماده‌باش کامل هستند و منتظر هرگونه تحول نظامی هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/140956" target="_blank">📅 22:23 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140955">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
❌
قرارگاه خاتم‌الانبیا: براساس اطلاعاتی که دریافت کردیم، آمریکا قصد دارد دوباره به ایران حمله کند. اگر حمله کند، پاسخ دردناکی می‌دهیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/140955" target="_blank">📅 22:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140954">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✅
✅
حدادی: قرارداد علی علیپور با پرسپولیس تمدید شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/140954" target="_blank">📅 22:07 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140953">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
❌
غیبت عالیشاه برابر پرسپولیس/ ستاره سابق سرخ‌ها کجا بود؟
❌
امید عالیشاه در دیدار دوستانه گل‌گهر و پرسپولیس نه در ترکیب تیمش قرار گرفت و نه روی نیمکت نشست.
❌
❌
گویا عالیشاه در ورزشگاه حضور داشته و به دلیل مصدومیت جزئی در رختکن در حال گرفتن ماساژ بوده است. این…</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/140953" target="_blank">📅 22:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140952">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✔️
حدادی : قرارداد همایی فر ۱/۶۰۰ دو سال دیگه هم قرارداد داره فردا قرارداد هرکسو زیاد کنیم باید بریم صدتا نهاد جواب بدیم ، اضافه هم نکنیم بازیکن انگیزه ش از بین میره و راحت می‌تونه فسخ کنه
☹️
☹️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس …</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/140952" target="_blank">📅 22:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140951">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🎙
🤩
پیمان حدادی: به درستی قهرمان لیگ سال پیش اعلام نشد؛  امسال ۲ همت درآمد خواهیم داشت. خیلی از باشگاه‌ها پول نداشتند. پارسال ۵۶۰ میلیارد درآمد داشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/140951" target="_blank">📅 21:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140950">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👀
❓
چرا خداداد عزیزی منتفی شد؟
🤩
پیمان حدادی: سیاست پرسپولیس و تراکتور فرق دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/140950" target="_blank">📅 21:24 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140949">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🤩
🎙
با اعلام حدادی ساخت ورزشگاه به خاطر نبود ثبات اقتصادی و امنیتی فعلا قابل ساخت نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/140949" target="_blank">📅 21:23 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140948">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🎙
🤩
حدادی: یا فوتبال یا یه کار دیگه! بازیکنای پرسپولیس باید حواسشون به فوتبال باشه. شکاری ۹۰ میلیارد از پولش گذشت و آقاسی با استقلال ۶۰٪ بیشتر گرفت. جام حذفی رو هم با تیم‌های حاضر برگزار کنید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/140948" target="_blank">📅 21:21 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140947">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✅
قرار داد 27 بازیکنان ایرانی تیم 1همت هستش.
🔘
اسکوچیچ برای پرسپولیس بالای یک همت هزینه داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/140947" target="_blank">📅 21:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140946">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🤩
حدادی : حتی من لیست تابستونی فصل آینده رو هم دارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/140946" target="_blank">📅 21:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140944">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🤩
حدادی: با همه مدیران باشگاها رفیقم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/140944" target="_blank">📅 21:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140943">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🤩
حدادی: برای آسانی مدارکی داریم که هیچ باشگاهی نداره؛ فدراسیون هم باید استعلام فیفا رو منتشر کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/140943" target="_blank">📅 21:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140942">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">▫️
🤩
حدادی: قرارداد علی علیپور با پرسپولیس تمدید شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/140942" target="_blank">📅 21:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140941">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🤩
حدادی : هرکس نمیتونه توی  جام حذفی شرکت کنه انصراف بده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/140941" target="_blank">📅 21:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140940">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🤩
حدادی : اون ۱۰۰ هزار دلار که بخاطر آقاسی دادیم بخاطر پیش پرداخت یک بازیکن بود که می‌خواستیم حسن نیت خودمون رو نشون بدیم و با اخذ رسید اون پولو دادیم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/140940" target="_blank">📅 21:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140939">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KxlPIxazuerdscunChKXkzb1Tn8KlMpPbVrBvzzL9vIN2T2keaLEIOFc2IFDCmbjEYSbYvAbhq17DSMmM_3ndlJ6HDZURVOzBAGHck4NWQE4nMRP19JGFC69WbpEG-GDZ0oxLkhQJ1I6DJ4ThU86RcaF1fU0OBiG8UIdC3jGeibAI2mtyiNCV61BATp7rWT9v97M3p-TcvzIrnCikPf2WVe6kFcd9a6i42rVVN_FDAHkqFrz1SkkjDVyT_j5JZB6lJvfZfQC717jRSTjD8t0xS6xpHSj4qHEF2IwEBSCFJNGSAkjsP3TDNWvmHGMnwTef8SRAn7IoR0L3GoE6mxTFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
Portugal -
❤️
Norway
⏰
Tonight 22:15
🏟
Estádio Do Dragão
🇪🇺
پرتغال در ۳ بازی این گروه ۷ گل زده و با ۹ امتیاز صدرنشینه؛ نروژ ۵ گل زده و ۶ گل هم دریافت کرده، ضمن اینکه پرتغال بازی رفت را ۲-۱ برده است. از نظر xG، نروژ با وجود کیفیت هجومی هالند خطرناکه؛ اما مدل‌های آماری همچنان پرتغال را شانس اول می‌دانند: برد پرتغال ۵۵.۹٪، مساوی ۲۰.۷٪، برد نروژ ۲۳.۵٪. می‌باشد. احتمال بازی گل‌دار و نزدیک زیاد هست و همچنین احتمال ‌می‌رود هردوتیم به گل برسند.
🟢
با درگاه بانکی اختصاصی و امن وینکوبت، حساب کاربری خودت رو به‌صورت مستقیم شارژ کن و مثل هزاران کاربر دیگه، بدون دردسر از امکانات وینکوبت استفاده کن.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/140939" target="_blank">📅 20:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140938">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✔️
✔️
فووووووووری از حدادی : قرارداد امیر حسین محمودی 3 میلیارد و 200 میلیونه
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/140938" target="_blank">📅 20:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140937">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✔️
✔️
حدادی : نمیتونم قرارداد محمودی رو اضافه کنم چون باید به سازمان بازرسی جواب بدم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/140937" target="_blank">📅 20:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140936">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
❌
فووووووووری از حدادی : تصمیم گرفته بودیم اورونوف و تمدید کنیم و بعد جام جهانی بفروشیم ولی نشد
🙁
🙁
🙁
🙁
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/140936" target="_blank">📅 20:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140935">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
❌
فوووووری
🔄
🔄
حدادی: تا آخر همین ماه یه جلسه مهم برای بیرانوند تو فیفا به صورت ویدیو کنفرانس انجام میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/140935" target="_blank">📅 20:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140934">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
❌
فووووووووری از حدادی : تصمیم گرفته بودیم اورونوف و تمدید کنیم و بعد جام جهانی بفروشیم ولی نشد
🙁
🙁
🙁
🙁
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/140934" target="_blank">📅 20:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140933">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
⭕️
⭕️</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/140933" target="_blank">📅 20:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140932">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
⭕️
⭕️</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/140932" target="_blank">📅 20:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140931">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✅
قرار داد 27 بازیکنان ایرانی تیم 1همت هستش.
🔘
اسکوچیچ برای پرسپولیس بالای یک همت هزینه داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/140931" target="_blank">📅 20:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140930">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
حدادی : اجاره شهرقدس هر بازی ۱/۲۰۰
🫪
🫪
🫪
✅
بازی های میزبان ۴ میلیارد هزینه میکنیم مهمان ۵ میلیارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/140930" target="_blank">📅 20:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140929">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔻
🎙
⚽
حدادی، مدیرعامل باشگاه پرسپولیس: قرارداد 5 بازیکن خارجی ما 4 میلیون و 80 هزار دلار است
⚪️
در نیم فصل و تابستان بعدی بازیکن خارجی نخواهیم گرفت، ابتدای فصل بخاطر همین کادر ایرانی گرفتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/140929" target="_blank">📅 20:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140928">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50712b5d4b.mp4?token=hFOiIxdD_PMHPQXMbU2bWopv9ktBy2o0OvzWI0IJAmxwxjZ4gzOmzdvu_Dsl2UYEDoj7t01mdzNsIyVXqlJvBpCEpllIOZ27__BHUgihdkY6G-2kxI60-XNE1_xm8gs9P4YO3upjZOH8zwv8hdclrXJ6C7INp5cHqzTiUUQN_a2wvz1fWXU1YQPzfhl-XuZmdLXpvrj-NtPYntjd7h7PnbVwGEvdIhdwhG3bIS4j8TFDPXYpAbxtJ8tzBwKVy4By6tNirfr0pvhapNMACaNcYg0Z-GRKZUksgOtX8ro1zyNLFuM_kGNVSU_9mCcBtuQHUEWbgQNjWq8qu3wTMpkJNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50712b5d4b.mp4?token=hFOiIxdD_PMHPQXMbU2bWopv9ktBy2o0OvzWI0IJAmxwxjZ4gzOmzdvu_Dsl2UYEDoj7t01mdzNsIyVXqlJvBpCEpllIOZ27__BHUgihdkY6G-2kxI60-XNE1_xm8gs9P4YO3upjZOH8zwv8hdclrXJ6C7INp5cHqzTiUUQN_a2wvz1fWXU1YQPzfhl-XuZmdLXpvrj-NtPYntjd7h7PnbVwGEvdIhdwhG3bIS4j8TFDPXYpAbxtJ8tzBwKVy4By6tNirfr0pvhapNMACaNcYg0Z-GRKZUksgOtX8ro1zyNLFuM_kGNVSU_9mCcBtuQHUEWbgQNjWq8qu3wTMpkJNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
🎙
⚽
حدادی، مدیرعامل باشگاه پرسپولیس: قرارداد 5 بازیکن خارجی ما 4 میلیون و 80 هزار دلار است
⚪️
در نیم فصل و تابستان بعدی بازیکن خارجی نخواهیم گرفت، ابتدای فصل بخاطر همین کادر ایرانی گرفتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/140928" target="_blank">📅 20:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140927">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❌
❌
❌
پیمان حدادی: ما شفاف هستیم و هیچ مشکلی نداریم نگرانی بابت لو رفتن قرارداد های پرسپولیس هم ندارم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/140927" target="_blank">📅 20:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140926">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">⭕️
⭕️
باشگاه پرسپولیس با خرید امتیاز باشگاه پادیاب خلخال صاحب تیم «ب» شد.
🆕
🆕
🆕
عصر امروز با حضور مدیرعامل و مالک باشگاه پادیاب خلخال در باشگاه پرسپولیس، امتیاز این تیم که امسال در لیگ دسته دوم حضور داشته به باشگاه پرسپولیس واگذار شد.
🔜
🔜
راه‌اندازی تیم «ب» یکی…</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/140926" target="_blank">📅 20:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140925">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
❌
❌
امشب پیمان حدادی مدیرعامل پرسپولیس ساعت ۲۰:۰۰ در لایو ورزش سه حاضر خواهد شد و به سوالات هواداران پاسخ خواهد داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/140925" target="_blank">📅 20:11 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140924">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✖️
✖️
شنیده میشود که رای کمیته استیناف نیز در پرونده آسانی تایید رای کمیته انضباطی بوده و پرسپولیس موفق به محکوم شدن این بازیکن نبوده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes ﻿</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/140924" target="_blank">📅 19:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140923">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
❌
❌
امشب پیمان حدادی مدیرعامل پرسپولیس ساعت ۲۰:۰۰ در لایو ورزش سه حاضر خواهد شد و به سوالات هواداران پاسخ خواهد داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/140923" target="_blank">📅 19:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140922">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
❌
اوستون اورونوف در ادامه‌ی رقابت‌ها نقش موثرتری در ترکیب پرسپولیس خواهد داشت/ورزش‌سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/140922" target="_blank">📅 18:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140921">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">⭕️
⭕️
۶ بازی آینده پرسپولیس در لیگ برتر فرصت مناسبیه برای اوج گرفتن و صدرنشینی در لیگ برتر
✅
✅
✅
ما ۳ بازی خانگی مقابل صنعت نفت ، فولاد و فجرسپاسی داریم و سه بازی خارج از خونه مقابل خیبر و مس شهربابک و نساجی و با توجه به آمادگی و اسکواد خوبی که داریم باید به…</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/140921" target="_blank">📅 18:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140920">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
❌
پیمان حدادی: خدا را شاکریم که سومین برد متوالی تیم بانوان را شاهد بودیم. سه پیروزی ارزشمند که باعث شد در صدر جدول قرار بگیریم و در هر سه مسابقه نیز کلین‌شیت داشته باشیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/140920" target="_blank">📅 18:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140919">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✖️
تارتار به دنبال امتحان کردن امیرحسین محمودی در پست شماره ۱۰ است.
❌
با مصدومیت علیپور، احتمال داره محمودی از وینگر به پشت مهاجم منتقل بشه تا خلاقیت بیشتری به خط حمله پرسپولیس بده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/140919" target="_blank">📅 18:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140918">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‼️
⁉️
‼️
یحیی گل محمدی به دلیل اینکه باشگاه دهوک یکماه در پرداخت دستمزد خودش و بازیکنانش تاخیر داشته اعتصاب کرده و تمرینات تیم شو تعطیل کرده:))))
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/140918" target="_blank">📅 18:21 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140917">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
مهدی تاج: سهمیه ما برای سال آینده 3+1 است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/140917" target="_blank">📅 15:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140916">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
#شایعات
✔️
هیئت مدیره پرسپولیس به سازمان لیگ اعلام کرده که در صورت اینکه نتیجه دربی 3-0 به سود پرسپولیس اعلام شود از بردن پرونده آسانی به دادگاه CAS صرف نظر می‌کند، در غیر این صورت این پرونده‌ به صورت رسمی با تمام مدارک به cas برده خواهد شد
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/140916" target="_blank">📅 15:24 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140915">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b62ce8f42.mp4?token=NQPrCC5It4CnvgO6WabqMuq0INZCh0_sPqRW-Keh2AW4z3GE8nsFtykbdwx7WD9xp7CmFETWgWyJUN1RULP0LniloSPB7Yl1zKCA8HY6Wkd05VZojx2Oi1cxszEG3yn_d6ETIYjm8prwvNEulkAfwXpFTYjY26x6BxwkUukmuI3L5Tf08YB4mnct09Qj9P9Wnsn1Y2jqlH8EjCZI0XfdNLBVkD0bH8EgLRdlIR21k1ER2pl5_5LuA5UoVKBrqGlspXsikM94-sNUc3I3S2fFfTptCf7GnYyugAHaj2xpNUHhRIxX1ppOMuAQJlxevZphEnK5L4SGUJJDNN9IeljnQUVHam41lLBC7L_77sPiimG_8JHYJQWvIRN39BGaJiXf_fHCEBhVc72prg2PCSbyG2MzB2sC5WOoKpExtYF2KM7SEiw0Gv9rBQtGfYdnwV6WYFi8G_73FhNqrTfncLHReYbo4R0xoz9B6xgS0P8YpNiv2dTi2e3hLqwvMZFsDPE6KWei9i1RoEUmi-XC70NsN3xBxA-6vPOSAuf3n3ASiC6R-yuktR8rHRlEfS4vIhKJiJB9-85VPlRSOBCcMjRcsFw_pg0GMzsOeDeLSXbQDvwRrsQVnlnEgtZurRwZKWvOCo9zwFq2Q8jqhTEHMgGEEkd8zSS4pezkOYon14J30KU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b62ce8f42.mp4?token=NQPrCC5It4CnvgO6WabqMuq0INZCh0_sPqRW-Keh2AW4z3GE8nsFtykbdwx7WD9xp7CmFETWgWyJUN1RULP0LniloSPB7Yl1zKCA8HY6Wkd05VZojx2Oi1cxszEG3yn_d6ETIYjm8prwvNEulkAfwXpFTYjY26x6BxwkUukmuI3L5Tf08YB4mnct09Qj9P9Wnsn1Y2jqlH8EjCZI0XfdNLBVkD0bH8EgLRdlIR21k1ER2pl5_5LuA5UoVKBrqGlspXsikM94-sNUc3I3S2fFfTptCf7GnYyugAHaj2xpNUHhRIxX1ppOMuAQJlxevZphEnK5L4SGUJJDNN9IeljnQUVHam41lLBC7L_77sPiimG_8JHYJQWvIRN39BGaJiXf_fHCEBhVc72prg2PCSbyG2MzB2sC5WOoKpExtYF2KM7SEiw0Gv9rBQtGfYdnwV6WYFi8G_73FhNqrTfncLHReYbo4R0xoz9B6xgS0P8YpNiv2dTi2e3hLqwvMZFsDPE6KWei9i1RoEUmi-XC70NsN3xBxA-6vPOSAuf3n3ASiC6R-yuktR8rHRlEfS4vIhKJiJB9-85VPlRSOBCcMjRcsFw_pg0GMzsOeDeLSXbQDvwRrsQVnlnEgtZurRwZKWvOCo9zwFq2Q8jqhTEHMgGEEkd8zSS4pezkOYon14J30KU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
مهدی تاج: سهمیه ما برای سال آینده 3+1 است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140915" target="_blank">📅 15:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140914">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇵🇹
نشریه رکورد پرتغال : محمدجواد حسین نژاد در آستانه انتقال به ریو آوه قرار دارد
💵
مبلغ انتقال : 1/4 میلیون یورو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/140914" target="_blank">📅 15:11 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140913">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
❌
تاج: آزادی باید مسقف بشه؛ شرط AFC!
❌
❌
حالا سؤال اینه؛ سقف‌زدن آزادی چند سال زمان می‌بره؟ ۲، ۳ یا ۴ سال؟ وعده آذرماه هم که ظاهراً منتفی شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/140913" target="_blank">📅 13:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140912">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‼️
دهقانی ناظر AFC در امور استانداردسازی استادیوم‌ها
✅
باید ورزشگاه آزادی را همانند نیوکمپ بارسلون مسقف کنیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/140912" target="_blank">📅 13:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140911">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9db93cfbe3.mp4?token=shinVLdNeMqwIPcH3peIJKHcgh_H0eZ-A-GKwB1Hbu3X8uAAeryNxuV9copGQrBOGBye44hyFZv4w_7hFAkoijTNgX0pj9wwU8wifml0Y4ETSD7SpQFndhCNook6kcSavpZ3hgrpeA8QFu2ESHp0_F2fFbVamPwxuVjl3tFab2e0COCa2fwi9wXvCi4_-_nekt0VKq7-niXj4o3Bi7ghA6iN6DR1z5SHd6Wfvg6F832oLi5S_U61ekNDN_-pgsLgdFVZdi_5XqvLAqUYc7oQmgqHkyID5UF5oZmq4d0lwtBu9Gju3SZA07ehY5RRdOqXlXUElu87Ci5M-GMTtUvOHgnZ57yoxSv_TBRg2IYGHvi-09WbvSJuRmo39tuCaXdKyHHLNHeNSWDff5zPMLwncTvUfKU0pcIsLvPpuKXV_NNWNxo0AdDhZvxzs1xIRpKQTzVEtvv1xbVIPfbYiIqHSWJiKD02fKEcqZnQXj-oB1SnSR1sX5JpG4hfl84lV6GFn7U5JuVQBMpcE63qukHmThNYt8w-bWP-x8V1RI97u1p9S7MYItgNWLYnjFtogwfKXhhI43xkPyxKEPvzmSMaCFdp9GsFPlSHluW_BIkMppR-RCOOADRf2OkEE3iV8x4pIdXxvKLCcaa_la4TCJClB9ciIhfz-J1FyLZbrDDikRk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9db93cfbe3.mp4?token=shinVLdNeMqwIPcH3peIJKHcgh_H0eZ-A-GKwB1Hbu3X8uAAeryNxuV9copGQrBOGBye44hyFZv4w_7hFAkoijTNgX0pj9wwU8wifml0Y4ETSD7SpQFndhCNook6kcSavpZ3hgrpeA8QFu2ESHp0_F2fFbVamPwxuVjl3tFab2e0COCa2fwi9wXvCi4_-_nekt0VKq7-niXj4o3Bi7ghA6iN6DR1z5SHd6Wfvg6F832oLi5S_U61ekNDN_-pgsLgdFVZdi_5XqvLAqUYc7oQmgqHkyID5UF5oZmq4d0lwtBu9Gju3SZA07ehY5RRdOqXlXUElu87Ci5M-GMTtUvOHgnZ57yoxSv_TBRg2IYGHvi-09WbvSJuRmo39tuCaXdKyHHLNHeNSWDff5zPMLwncTvUfKU0pcIsLvPpuKXV_NNWNxo0AdDhZvxzs1xIRpKQTzVEtvv1xbVIPfbYiIqHSWJiKD02fKEcqZnQXj-oB1SnSR1sX5JpG4hfl84lV6GFn7U5JuVQBMpcE63qukHmThNYt8w-bWP-x8V1RI97u1p9S7MYItgNWLYnjFtogwfKXhhI43xkPyxKEPvzmSMaCFdp9GsFPlSHluW_BIkMppR-RCOOADRf2OkEE3iV8x4pIdXxvKLCcaa_la4TCJClB9ciIhfz-J1FyLZbrDDikRk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دهقانی ناظر AFC در امور استانداردسازی استادیوم‌ها
✅
باید ورزشگاه آزادی را همانند نیوکمپ بارسلون مسقف کنیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/140911" target="_blank">📅 13:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140910">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETrUCwrRPRDGSLiVXrQGhb43DFtOD91KqvH8dgVIYnoH6GPOeL1O5zV4HXgxTCQ6dhWk-VNZrGXP7xMhvf5HVx-Ml9kIkLWRb6o0KIcz8Hxm0jMrB10cVRqvkkEcB5-kGg85JbxkAtOyh4hax-FCYjfi6kbtKPCPzyFpIccQX7tTezz06XR4tufb4KekNFeuQw-Oqb1BGqxwy30wjQTsavKONmDFEGMJsWGXQ-mm7PrKCdGNdBfAffl14IjpBiw8vbO7jExyh6Mhuh7LWmUNEjuv_MPV39tJk0mKbbGp7qPBnkkHWDpMsvknZ3txtE21LCxTGTtqRAZutUK556dcHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نبرد سلسائو با وایکینگ‌ها؛ پرتغال در برابر نروژ، یک شب پر از هیجان!
🔥
⚡️
[
پرتغال
🇵🇹
🆚
🇳🇴
نروژ
]
⚽️
پرتغال با تکیه بر مالکیت توپ و کیفیت بالای خط حمله، معمولاً مقابل تیم‌های فیزیکی هم موقعیت‌های زیادی خلق می‌کند. نروژ اما با قدرت درگیری، انتقال سریع و تهدید دائمی در یک‌سوم هجومی می‌تواند بازی را برای سلسائو سخت کند. سناریوی محتمل، بازی نزدیک در نیمه اول و افزایش موقعیت‌ها در ادامه است؛ گل در هر دو نیمه سناریوی جذابی به نظر می‌رسد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/140910" target="_blank">📅 13:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140909">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
تارتار هنوز به یاسین سلمانی امیدواره
🔻
مهدی تارتار این روزها تمرینات ویژه‌ای برای یاسین سلمانی در نظر گرفته و قصد دارد این بازیکن را دوباره به روزهای خوبش برگرداند
🔻
گفته می‌شود تارتار به اطرافیانش گفته اگر تا پایان نیم‌فصل اول نتواند سلمانی را به شرایط…</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/140909" target="_blank">📅 13:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140908">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/azSXm0mOUsbuLf1aLZwUOJ_PvRN5ZokxV2Q0QM5tehAeO00DEUahr--VE5kb_vRBM5Sjj9aW4E1I50ZOEm7iQb70uQP1myfxTP0w_1DKk4ZsNV6QB_V95B4o70D_HjX0OUZeWaw3ODvMUrLRC5HqlrfozX_0TdXfJX62ZMiHQvlBi6iDgmpeIdMFbUp7Dbnm8mRxUQ29RdElbQMyPMP9rJfheYlTNYTd62-J3hZtViLEilVlrkVwxjtAC2z8y7Kr5nMjYy8grmT4jiSYQDfsf0GSWG9eq3u35syMLeW5yvWGToLlIjE1OpklkhQ1pmlxJXyllGdGTFGhrTCD0RbBrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
باشگاه پرسپولیس طی روزهای اخیر درگیر تمدید قرارداد سه بازیکن مهم خود یعنی نیازمند، اورونوف و کنعانی‌زادگان است که تاکنون موفق به توافق با دو نفر از آنها شده است که اون نفر باقی مانده اورونوفه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/140908" target="_blank">📅 13:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140907">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">⭕️
❌
❌
❌
❌
ادعای برگ ریزون یه خبرنگار ورزشی: یه زن اعتراف کرده که باهمخوابی باچند داور برخی اتفاقات فوتبال ایران را باآنها هماهنگ کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/140907" target="_blank">📅 10:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140906">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
حمید ابراهیمی خبرنگار ورزش سه: یه معاوضه دیگه بین پرسپولیس و گل گهر شکل گرفته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/140906" target="_blank">📅 10:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140905">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvsRSo8ord7u9475VA4A4l_yRQ86m0LQsp7nf4VPqPYnMprVrCckSaiC58oeLkAnH_M_zT9d7zu55TS04smnzejYF0crZIz0KpVSZqBv-P4bNJGMWeZIa6fatfLxuqTvnkPNN8Ub6vCD5o4wZIU65xWm-ijkVKESZp8u9r8si7r-c0cj_WQux78ZSxh6PorqflmlTzfb64v6nP2sUq_wyIQ6hsQubN4z6aFObmNGJJju-UsAP68EQlu-V-XMfb62BMtll2xLCd23n0wF8inay_UOsxsZPYqY80QwlnmDsgu5_zgTfYG_6SJE1rzZtpqvZzT9kTtZmKFgZBDFtDu7tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇮🇷
بازی دوستانه تیم ملی که قرار بود در مقابل تیم‌های گینه استوایی یا گینه بیسائو برگزار شود به دلیل محدودیت پروازی و غیبت بازیکنان حریف لغو شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/140905" target="_blank">📅 10:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140904">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✖️
✖️
پرسپولیس امروز استراحت داره  و از دوشنبه تمریناتش شروع میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/140904" target="_blank">📅 10:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140903">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBx7UMvhAatmsBPQ0tJNZdphhF60nnvG5boIM_mI0n8N3ow5OeaIuQrlRJIjQFW_E_v_GmxGTPGm_ZuwHDv3lacLS7XYV2AqevRD2_WjjWM3zYMj3W0LfyR9Ny0NsvmLgdyOKXAMc3hxfVXp6NMxzRmoQb6wgQjYryPtDAJOVFoVRC6HrI5OnB7Yjw3m6zBm-Gcq_TqVfAc96KtZPb4N3LpyCOxC4i-ugnh5CRRLd6DzcS9veJZZAcO6cs5X-7P0zVnBLd9bf6hVNnY7wI0Cqr5Wbwobxo8vtQUuwJxVQCA0e9Bl_BgB3JSy-roKCzZSDadV-Y6vjOBZeX_QfzNM9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
✖️
پرسپولیس امروز استراحت داره
و از دوشنبه تمریناتش شروع میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/140903" target="_blank">📅 09:11 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140902">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">⭕️
بهترین لحظات پرسپولیس در لیگ قهرمانان آسیا در سال های اخیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/140902" target="_blank">📅 09:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140901">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/po4eiCQG0enpfR5YKZF7sve4JiokS5Flv3kqLDK3_dfKkIFVNO7QSjQ5I-EuopWc4twbyQAVwJ_onocaufO-_aNSef1hdfbCX1WD4GkP3QQhXjJmLlRsT5xxQgpomRK0YOVSUtOxgqiXGdEXWe_cUtfNU55MB3nmJOrwhxKJ0-gokZAa7vmrnCKnNXL_P4wZotEylzyFveVnlrmdzvxgMS0qSqMRYLPHBCMLly9dPciYW34S60NWkPcOMDUeJ9xL7XDFUvzmD3SRUaQsROJXJRHVxFcVhyNkaC71kPWwPieQMoG8tedIeZXcMTWlQ8EXX60kCi2mmcSVMl4dUAf1eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/140901" target="_blank">📅 09:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140900">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">■ دیگه دنبال لینک سایت برای ورود نگرد!
🔵
اسپورت‌نود کار رو از طریق ربات مینی‌اپ ساده و راحت کرده، به‌راحتی میتونید پیش‌بینی مسابقات ورزشی و بازی‌های کازینو رو انجام بدید!
🔗
فرآیند ورود به سایت به شکلی طراحی شده که کاربران بدون درگیر شدن با لینک‌های متعدد یا مسیرهای غیرضروری، مستقیماً وارد محیط اصلی سایت شوند.
📌
این دسترسی از طریق ربات رسمی اسپورت‌نود انجام می‌شود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
به جای روش‌های قدیمی ورود، این ساختار یک مسیر واحد و ثابت ارائه می‌دهد که همیشه قابل استفاده است.
📌
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/140900" target="_blank">📅 01:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140899">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
❌
دیدار تیم‌های زنان پرسپولیس و استقلال در ورزشگاه کاظمی با استفاده از سیستم VAR برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/140899" target="_blank">📅 00:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140898">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✅
از این پس امیرحسین محمودی در پست پشت مهاجم بازی خواهد کرد/ورزش‌سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140898" target="_blank">📅 00:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140897">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
❌
دیدار تیم‌های زنان پرسپولیس و استقلال در ورزشگاه کاظمی با استفاده از سیستم VAR برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140897" target="_blank">📅 00:38 · 12 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
