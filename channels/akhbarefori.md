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
<img src="https://cdn4.telesco.pe/file/WaIisjjQRvtJP1DajXDstszTfTRPLKR4X8fQf9fJ5EnPMvBY97-C01z0C0_7slXrTk5fAmPmlzff651eV_Rqikq0CPN4umyDoRlxKU0mujeJrTN16nisPHESGFUIWArJzqtoMhDaUpvL8iIxxxmIcIVjwj6jKDHsBHgug0rD8-C90saEmHAEVoRNVrLrlhRISXPwoxR6CcnujSdQcGf6sMkNcZSJdqXm-fGCHB2VMANqHb8wdnlXg6MLJXGSiuZdtoMoA1T3jf20-4SFa7rj9LGKXH4Py9A-os4xiJPr92bSm2izwv4l6-u-jcYj8z2ue8JJjNBwDXnJxEF5v0-Eyg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.59M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 03:18:49</div>
<hr>

<div class="tg-post" id="msg-657851">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
منابع خبری عراقی: مشاهده جنگنده های آمریکایی در تعداد بالا درحال پرواز در آسمان عراق در نزدیک خط مرزی ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6 · <a href="https://t.me/akhbarefori/657851" target="_blank">📅 03:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657850">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
گزارش ها از ادامه انفجار ها در بندرعباس خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/akhbarefori/657850" target="_blank">📅 03:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657849">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
فاکس نیوز به نقل از یک مقام آمریکایی مدعی ادامه حملات آمریکا به برخی مناطق جنوبی ایران شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/akhbarefori/657849" target="_blank">📅 03:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657846">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b372cea86a.mp4?token=r94pPkQJsGYe4WbYyKWs7Tmr-9PA4plIqpCS-8iYdXvNgHOU2x8HxAI9ghGwvxa4EHj0vF53L_Vl1a1mVwFa87X9USyl3W2gey5iUbxtSd8V82CXO9QcIxDrdMb58ZEDk0CaWbGvuha3RxbZGWxHdvVjzthLtCyx3Mzepmi9QnyVYAe_a8cKkdSYXyW-EpK1rgkneeLjzvLIUNOnkOvARuJCx7i-X5CMPqB9Et1fdrAdCcx-rd6cQmPD0DS_pp6W5jQrYcLNaXZCmI0xJGTr60NUN6brgiPgCrzawP9J6O0Waju552MVgXuJY1PsUNSWqVICzCO0yRI_a9hZLc_XwzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b372cea86a.mp4?token=r94pPkQJsGYe4WbYyKWs7Tmr-9PA4plIqpCS-8iYdXvNgHOU2x8HxAI9ghGwvxa4EHj0vF53L_Vl1a1mVwFa87X9USyl3W2gey5iUbxtSd8V82CXO9QcIxDrdMb58ZEDk0CaWbGvuha3RxbZGWxHdvVjzthLtCyx3Mzepmi9QnyVYAe_a8cKkdSYXyW-EpK1rgkneeLjzvLIUNOnkOvARuJCx7i-X5CMPqB9Et1fdrAdCcx-rd6cQmPD0DS_pp6W5jQrYcLNaXZCmI0xJGTr60NUN6brgiPgCrzawP9J6O0Waju552MVgXuJY1PsUNSWqVICzCO0yRI_a9hZLc_XwzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ، عصر دیروز، درباره هو شدنش توسط هزاران آمریکایی در محل برگزاری فینال لیگ بسکتبال، گفته بود «فکر می‌کنم بیشتر تشویقم کردند» اما این ویدیوها چیز دیگری نشان می‌دهد!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/akhbarefori/657846" target="_blank">📅 03:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657845">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
ادعای اکسیوس: یک مقام آمریکایی می‌گوید دور دوم حملات در ایران در حال انجام است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/akhbarefori/657845" target="_blank">📅 02:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657844">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
ادعای اکسیوس: یک مقام آمریکایی می‌گوید دور دوم حملات در ایران در حال انجام است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/akhbarefori/657844" target="_blank">📅 02:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657843">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
شنیده شدن مجدد صدای انفجار در شهرستان جاسک
🔹
دقایقی پیش، صدای انفجارهایی مجدد در محدوده شهرستان جاسک از سوی منابع محلی و ساکنان و روستاهای اطراف گزارش شده است.  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/akhbarefori/657843" target="_blank">📅 02:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657842">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
شنیده شدن مجدد صدای انفجار در شهرستان جاسک
🔹
دقایقی پیش، صدای انفجارهایی مجدد در محدوده شهرستان جاسک از سوی منابع محلی و ساکنان و روستاهای اطراف گزارش شده است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/akhbarefori/657842" target="_blank">📅 02:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657841">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0f35de44f.mp4?token=CY9y_GJwQ9FSab952NV9dwoMANmgdXKl1aWB2woGu4k4yc8VMAwxF4O4NZFUj5FmGdHmAuEedENw4erJl4sfjjoo1VtFqiu9DDF53hD_eByBzVHeoVSamRZEU34PQoTlu_EX1Uzy4YWzuTKvYm6J3t3cAXYtserGrlC5LS4hCiH-su6l-p1L69e9lPWLNJdsEV6fRXugV6LX1QIxl5_jsfLSsOWsR37dnRm-9EBYRlFYh8i5memwk7MgVh9bDGPRfATU-j_paSmdKgtGlIa_hJYctvN6qaIFUfmxCXuhfb6OOwcnOGsRKzLslZyIIrxrHhrew-9zosRL7CbjMgKN_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0f35de44f.mp4?token=CY9y_GJwQ9FSab952NV9dwoMANmgdXKl1aWB2woGu4k4yc8VMAwxF4O4NZFUj5FmGdHmAuEedENw4erJl4sfjjoo1VtFqiu9DDF53hD_eByBzVHeoVSamRZEU34PQoTlu_EX1Uzy4YWzuTKvYm6J3t3cAXYtserGrlC5LS4hCiH-su6l-p1L69e9lPWLNJdsEV6fRXugV6LX1QIxl5_jsfLSsOWsR37dnRm-9EBYRlFYh8i5memwk7MgVh9bDGPRfATU-j_paSmdKgtGlIa_hJYctvN6qaIFUfmxCXuhfb6OOwcnOGsRKzLslZyIIrxrHhrew-9zosRL7CbjMgKN_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع سه انفجار در خط لوله گاز در منطقه داغستان روسیه
🔹
وزارت امور اضطراری منطقه‌ای روسیه گزارش داد که سه انفجار در یک خط لوله گاز در شهر کیزیلیورت در منطقه داغستان روسیه در قفقاز شمالی رخ داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/akhbarefori/657841" target="_blank">📅 02:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657840">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
نماینده پاکستان: شکست دیپلماسی، مأموریت حیاتی راستی‌آزمایی آژانس بین‌المللی انرژی اتمی در پرونده هسته‌ای ایران را مختل ساخته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/akhbarefori/657840" target="_blank">📅 02:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657839">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
گروه هکری حنظله: مختصات تمام نیروهای نظامی تروریستی آمریکا در کشورهای خلیج‌فارس به سپاه پاسداران انقلاب اسلامی منتقل شد
🔹
به‌زودی به پهپادهای شاهد-۱۳۶ «خوش‌آمد» خواهید گفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/657839" target="_blank">📅 02:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657838">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
آماج‌نیوز افغانستان: لحظات پیش جنگنده‌های پاکستانی اهدافی را در ولایت‌های خوست، پکتیکا و کنر بمباران کرده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/657838" target="_blank">📅 02:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657837">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df42fc015a.mp4?token=Sx3x6WQtwWQHVLpxbYUu5roLcm_hPPD2_7GFzg0DJ3T0wftl5wSJnqckZ9ulGCiFzd8RiLaFZNNnOwlRpVr5MO45Hejn8E4V34YFQ3TsxnzrLZBNUmbo2HMqQgUstt4WnQWYbMLp-zJi88Ua-UJGQtopTh0AN5I12vD7NMu5A3kyFV8emre1ij3HSpcqcRim1eoDdOHssspzZkKPGra0ZTCqDwdEf8RpaE8I0vhB-iu9kqIeD9ePFONFipz83VcixXETON0MNXo-A5XJzrZ3jGtxG_roE-xXauEq0wuDneTUfmYIIy5qwKwiAO8tMxfUcVQj8E6AZprXilThf2M7vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df42fc015a.mp4?token=Sx3x6WQtwWQHVLpxbYUu5roLcm_hPPD2_7GFzg0DJ3T0wftl5wSJnqckZ9ulGCiFzd8RiLaFZNNnOwlRpVr5MO45Hejn8E4V34YFQ3TsxnzrLZBNUmbo2HMqQgUstt4WnQWYbMLp-zJi88Ua-UJGQtopTh0AN5I12vD7NMu5A3kyFV8emre1ij3HSpcqcRim1eoDdOHssspzZkKPGra0ZTCqDwdEf8RpaE8I0vhB-iu9kqIeD9ePFONFipz83VcixXETON0MNXo-A5XJzrZ3jGtxG_roE-xXauEq0wuDneTUfmYIIy5qwKwiAO8tMxfUcVQj8E6AZprXilThf2M7vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش تحلیلگر فاکس‌نیوز به ادعای تکراری ترامپ مبنی بر «نزدیک شدن به توافق» با ایران، همزمان با ادامه تجاوزات آمریکا: اگر فردا بشنویم که به توافق با ایران نزدیک‌تر شده‌ایم و تقریباً به آن رسیده‌ایم، فکر می‌کنم کمی پذیرفتنش سخت باشد!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/657837" target="_blank">📅 02:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657834">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
حمله تروریستی آمریکا به  دو مخزن آب در سیریک
‌
🔹
در پی حمله امشب دشمن آمریکایی به سیریک، ۲ مخزن آب بخش بمانی مورد اصابت قرار گرفته و آب آشامیدنی این بخش قطع شده است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/657834" target="_blank">📅 02:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657833">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
هیچ بندر تجاری در جزیره قشم هدف پرتابه های دشمن قرار نگرفته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/657833" target="_blank">📅 02:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657832">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPnSv5ULXpCexjwndxBmH8UmspxWk9tWfcjeI9vEcDAOf_FX-eWoLb6Y4WXkaX9_BO9NTflf3nZ21NYx_4wEuCJBybT7fWb1rD3Lf4hw4sCc-tvZcl7DiBYWbPmxDn2tBVTlP0RHfPLkCtm5tKIfk_Qeue1XNFjm3nFUBa7oI8wKn3G95VchlD04-iBrGydF6pQTFc1NFP6ugkoUPFMbMtWLHAAnpZJWZJ9205UnrltBLWyt3q80VYZbXgijZRoqCV8CJ5zexhVRxkXhi00jw5vevBrdpJa4F7jo4lIm2z8XoCLawdVGzNx0danqnLGv63hbZOthnGwI_iUWkM_V7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: آمریکا با وجود شکست‌هایش در میدان نبرد، تصمیم گرفت اراده ما را بیازماید
🔹
نیروهای مسلح قدرتمند ما هیچ حمله یا تهدیدی را بی‌پاسخ نخواهند گذاشت.
🔹
اگر خواهان امنیت هستید، منطقه ما را ترک کنید.
🔹
تاریخ خلیج فارس فصل‌های زیادی درباره سرنوشت شوم بیگانگان…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/657832" target="_blank">📅 02:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657831">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
عراقچی: آمریکا با وجود شکست‌هایش در میدان نبرد، تصمیم گرفت اراده ما را بیازماید
🔹
نیروهای مسلح قدرتمند ما هیچ حمله یا تهدیدی را بی‌پاسخ نخواهند گذاشت.
🔹
اگر خواهان امنیت هستید، منطقه ما را ترک کنید.
🔹
تاریخ خلیج فارس فصل‌های زیادی درباره سرنوشت شوم بیگانگان متجاوز دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/657831" target="_blank">📅 02:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657830">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
پولیتیکو: یک مقام ارشد کاخ سفید ادعا کرد که دونالد ترامپ همچنان معتقد است توافق صلح با ایران نزدیک است، حتی در حالی که ایالات متحده امشب حملات تلافی‌جویانه‌ای علیه ایران انجام داد
🔹
هیچ چیز وضعیت کنونی توافق را تغییر نمی‌دهد.
🔹
این مقام تأکید کرد که توافق با تهران «هنوز نزدیک است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/657830" target="_blank">📅 01:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657829">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMZmPGuDpUTVUoO4DjYSO_DlIcRnGBKyhY7ruUnvSM2FyLzVJwBHkmeW_D6-yb-2kkR9zYSbkIZsD-QZ5q8-wadMfMEVZAfKrUlg_DJwkzFf5KEabU_E-sPmLwmfQthPX3nC_DHqtAdD6re2vcHibG58Ekq9qF-qOqvFE-2n6EDnWB45SnSNjwutU_fWTMEPpfY3NgKTTRS2M4FyvlfP8yT0M-5U2gEjhOQt9bW0pjzPguX_SQLiVmkZp2qZF0a25EL1lMEMe3mQLXEeLhCvuhJCn1I0aTr9k43FTSLT6WGQE9_3a2oWPs8aFrwk8OU2yckpTXNjQGWRXs2OzRz48A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هم اکنون، آسمان منطقه و وضعیت پروازها
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/657829" target="_blank">📅 01:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657828">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
موج حملات آمریکایی ها در جنوب فروکش کرده است و بعد از اقدامات خصمانه در قشم، سیریک و جاسک و کوه مبارکه جاسک، هم اکنون وضعیت آرام گزارش می شود/مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/657828" target="_blank">📅 01:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657827">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
نامۀ عراقچی به شورای حکام درباره پیش‌نویس قطعنامۀ ضد ایرانی
🔹
وزیر امور خارجۀ ایران در نامه‌ای به اعضای شورای حکام، پیش‌نویس قطعنامۀ ارائه‌ شده از سوی آمریکا و ۳ کشور اروپایی را اقدامی سیاسی و از روی بدنیتی خواند و از اعضا خواست اجازه ندهند آژانس بار دیگر به ابزار سیاسی آمریکا تبدیل شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/657827" target="_blank">📅 01:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657826">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/960b224ee4.mp4?token=MK8sFAuDINroiIbsiYScW9pSLvUycU0q0wWIRH3uesxCRwyWYTSNSjgFOnkEZebNC9l9HyyhLmm4qhL7Ikjr0h5B6Wv7hTNaubk2yZmiusbUn8CO6OFEjU9gUNJCh3qe1tgC08YWE1j2bOO0mStqpUABtkmCM2cqETvxdPrtRa9nkzqH0LVH754B8DbqpyT-Jy6dRe2ylL70J0c0PHZ7Ij0Lw_y5n_vFbUAANB2PYr9q9ZNgqWQ0KjTGqJk8mHBuF7VUnPU9ikD6pASAvKkDJdNOlC8NZz4WnJrNrSwGLAXEjORM9JeJhKaMXjxqy_lUiUWxYNFme-W-1vg1-iCTfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/960b224ee4.mp4?token=MK8sFAuDINroiIbsiYScW9pSLvUycU0q0wWIRH3uesxCRwyWYTSNSjgFOnkEZebNC9l9HyyhLmm4qhL7Ikjr0h5B6Wv7hTNaubk2yZmiusbUn8CO6OFEjU9gUNJCh3qe1tgC08YWE1j2bOO0mStqpUABtkmCM2cqETvxdPrtRa9nkzqH0LVH754B8DbqpyT-Jy6dRe2ylL70J0c0PHZ7Ij0Lw_y5n_vFbUAANB2PYr9q9ZNgqWQ0KjTGqJk8mHBuF7VUnPU9ikD6pASAvKkDJdNOlC8NZz4WnJrNrSwGLAXEjORM9JeJhKaMXjxqy_lUiUWxYNFme-W-1vg1-iCTfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع عراقی تصاویری از یک پرواز شاهد در آسمان این کشور منتشر کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/657826" target="_blank">📅 01:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657825">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
خبرنگار اکسیوس به نقل از مقام آمریکایی: نیروهای آمریکا به چندین سامانه پدافند هوایی و سامانه‌های راداری ایران در اطراف تنگه هرمز حمله کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/657825" target="_blank">📅 01:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657824">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
سامانه‌های پدافندی در کویت و بحرین فعال شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/657824" target="_blank">📅 01:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657823">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
مقام آمریکایی: هدف از حملات آمریکا ارسال پیام هشدار به ایران است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/657823" target="_blank">📅 01:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657822">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDIC7iDAbaEBcnGlk8_ZXh4iv2_z74P5bTw7vuY9OolrL94ZGHiU9ZdXhn0c4X7FEBDGVYqwfJ8A2e1QhH0aQLFELPopjVcvT82xYAQMtQEcCSGOF7aIJPTZSS78WHdK1ywiMElwzr2phjgmwFR9NLvQH8fQoTOPA3ie2VxDtWJTc-bObNqx61k7_W9rL8F34wSeiDVx6bwI6HqDfz3BQI1UpCTS4POCjR_BDQmSFQl01jEoidhUtylKBNbkFLxKoc0WBLuVjzRehbQPa8cmeMuHncAM_t-woL8Wr43i-k7PzSxyqFfdR4GlWBUmbqzwPlZSq-9Ja21BTpPfQl1LTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سید مجید موسوی: ‏و ما النصر الا من عند الله العزیز الحکیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/657822" target="_blank">📅 01:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657821">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
فایننشال تایمز: قیمت نفت پس از حمله آمریکا به ایران اندکی افزایش یافت و به ۹۲.۳۰ دلار در هر بشکه رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/657821" target="_blank">📅 01:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657820">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
حریم هوایی قطر بسته شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/657820" target="_blank">📅 01:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657819">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
گزارش های غیر رسمی از پرتاب موشک و پهپادهای ایران به سمت اهداف آمریکایی در منطقه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/657819" target="_blank">📅 01:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657817">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
ادعای مقام آمریکایی: حملات علیه ایران همچنان ادامه دارد
🔹
یک مقام آمریکایی در گفتگو با الجزیره ادعا کرد که نیروهای آمریکایی به انجام حملاتی علیه ایران برای دفاع از خود ادامه می‌دهند و عملیات هنوز در جریان است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/657817" target="_blank">📅 01:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657816">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
دو نقطه در جاسک و کوه مبارکه مورد اصابت پرتابه دشمن قرار گرفته است
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/657816" target="_blank">📅 01:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657815">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
ایران به تجاوز آمریکا پاسخ خواهد داد
‌
🔹
ایران همچنانکه ساعاتی پیش نیز هشدار داده، پاسخ قطعی به تجاوز آمریکا که به بهانه سقوط هلیکوپتر آپاچی انجام می‌شود، خواهد داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/657815" target="_blank">📅 01:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657814">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
اصابت پرتابه در قشم، صداهایی شبیه هواپیما شنیده شد
🔹
در قشم صداهایی شبیه صدای هواپیما و اصابت چند پرتابه گزارش شده است
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/657814" target="_blank">📅 01:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657813">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
منابع عربی: بالاترین سطح هشدار در پایگاه‌های آمریکا در کویت، بحرین، امارات و قطر صادر شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/657813" target="_blank">📅 01:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657812">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
صدای انفجار در اطراف بندرعباس نیز شنیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/657812" target="_blank">📅 01:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657811">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
ترامپ: باید پاسخ انهدام بالگرد را می‌دادیم
🔹
رئیس‌جمهور جنایتکار آمریکا به خبرنگار ای بی سی نیوز گفت: باید انهدام بالگرد آپاچی را پاسخ می‌دادیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/657811" target="_blank">📅 01:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657810">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
تمام کشور های عربی حاشیه خلیج فارس از بیم حملات ایران  در حالت آماده باش کامل درآمدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/657810" target="_blank">📅 01:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657809">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
به گزارش خبرنگار صداو سیما در قشم دقایقی پیش یک مکان در قشم مورد حمله قرار گرفته است
‌
🔹
به گفته یک منبع آگاه ۶ صدای انفجار در قشم شنیده شده که بر اثر پرتابه های دشمن بوده است.
‌
🔹
ظاهراً این پرتابه ها از جنگنده شیلک شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/657809" target="_blank">📅 01:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657808">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
سیریک اصابت یک پرتابه تایید شده اما مکان و نحوه اصابت مشخص نشده است
‌
🔹
برخی منابع از شنیده شدن صدای انفجار و فعالیت پدافند در بندرعباس، قشم و سیریک خبر می دهند.
‌
🔹
خبرهای تکمیلی متعاقبا اعلام خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/657808" target="_blank">📅 01:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657807">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در مناطقی از هرمزگان
‌
🔹
دقایقی پیش صدای چند انفجار در مناطق شرقی هرمزگان از جمله در کوهستک و سیریک و میناب شنیده شد.
🔹
هنوز منشأ و محل دقیق این انفجارها مشخص نیست اما منابع محلی از فعالیت پدافند در برخی نقاط استان نیز خبر می‌دهند./فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/657807" target="_blank">📅 01:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657806">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
سنتکام: حملات نظامی علیه ایران با دستور مستقیم پرزیدنت ترامپ انجام شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/657806" target="_blank">📅 00:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657805">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
صدای انفجار و فعالیت پدافند در قشم و بندرعبا
س
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/657805" target="_blank">📅 00:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657804">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
برخی منابع خبری مدعی شدند حداقل شش انفجار از موقعیت نیروی دریایی در سیریک گزارش شده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/657804" target="_blank">📅 00:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657803">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tke4B5EPfqfqdUhEQvxAxz9ShNxcg-ky3r90_3FVYU_62QWw6P99HE5JslItthrlH4EW004GA_SQz-TKzvFXlcc7Vl7GeJOMpKSdy-V-GXagu9Z2x_I_LWIlB7sgxtaMVFn0BOEtZmz9vOGovc4LtyndcRAV_XxwV8YPaxr89ruYzg3YizMnF-Yzi00yLM3keZhOkzJpkloKey9s4GCqTQXJmTAbnC9cnsmmCj3jSqCTrk8XZHeh6igoJkon48jq8KqQhi45YPws21ONyawIgae68cFsc1CzGsbf2UqtcnRXNNVZDjAAsonNvTm9aeWADErte2HyRbghGrUyS-rSyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازمان تروریستی سنتکام اعلام کرد که در واکنش به سرنگونی یک بالگرد آمریکایی، حملات تجاوزکارانه‌ای را به چند نقطه در جنوب ایران انجام داده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/657803" target="_blank">📅 00:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657802">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
ادعای فرماندهی مرکزی ایالات متحده (سنتکام): نیروهای سنتکام، به دستور فرمانده کل قوا، حملات دفاعی خود را علیه ایران از ساعت ۵ بعدازظهر به وقت شرقی امروز، در پاسخ به سرنگونی یک بالگرد ارتش آمریکا از نوع آپاچی در دیروز، آغاز کردند
🔹
این عملیات، پاسخی متناسب با اقدام غیرموجه ایران است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/657802" target="_blank">📅 00:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657801">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهایی در محدوده بندر سیریک
🔹
ساکنان محلی بندرسیریک از شنیده شدن صدای انفجار‌هایی در محدوده این شهرستان خبر دادند.
شامگاه سه شنبه، صدای انفجار‌هایی در محدوده شهرستان سیریک از سوی منابع محلی و ساکنان بندر سیریک و روستاهای اطراف  گزارش شده است./مهر
گزارش لحظه به لحظه حمله آمریکا
👇
khabarfoori.com/fa/tiny/news-3221874</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/657801" target="_blank">📅 00:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657800">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
خبرنگار کانال ۱۴ رژیم صهیونیستی: ترامپ تلافی می‌کند هرچند کوچک
خبرنگار:
🔹
پیش‌بینی‌ من این است هرچند صمیمانه امیدوارم اشتباه کنم؛ ترامپ در پاسخ به سرنگونی بالگرد آمریکایی، یک حمله‌ی جزئی و نمادین انجام خواهد داد، مثبت یک ایستگاه راداری و چند سکوی پرتاب ضدموشکی در منطقهٔ تنگه‌ی هرمز، یا چیزی مشابه
🔹
یعنی حملاتی از جنس همان حملاتی که قبلاً هم بیش از یک بار در جریان آتش‌بس دیده‌ایم، نه چیزی که جنگی را شعله‌ور کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/657800" target="_blank">📅 00:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657799">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
الحدث: نتانیاهو و ترامپ امشب درباره ایران و لبنان تلفنی گفت‌وگو کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/657799" target="_blank">📅 00:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657798">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-qns_WZxVGDz4fyjUCmYXGfzYah4jhzK0uyZ4Awylk6IGQ0cvIzaqL1eenhh4QySXWQZbEstQy-pDCwlfFWZNrdJSu4md9GmJ7YJYidz2Em_VuyiGTWRd3MxTzhrrhz6FxQX5u6II6mSfJlnjyZWpklwg1DFYGBF0Rl91k9Ft7853tCA-F3tzYQOw1ztHBX3IphkZlwZl-CEvUGAmJYCerZNBqAJnqYYYYzxGiEgpkkqFJwyiLu9nvdUgrsxidmHFkpruhemwjHD3iU869EB9Mulqgmt0e4LEEDbXEPyhdFdYdoTLRc_uMRumexa5p_I_OYBkY5kS5YpFnDQNVQ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترکیب عالی برای درست کردن شربت بهارنارج که برای هوای گرم خیلی مفید و دلچسب هست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/657798" target="_blank">📅 00:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657797">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83de2e39f8.mp4?token=tnicuHkgkII6Gz_V8yPL8_uF6Wkb3W1OHXQXtRAkeRfz8YY9luafFtAUVrEUoX5pVyAXcrfNnssLyN_y-abFV3aRIFgqm3DpljKtBjOX7HmbrgRDuRzgTi99qwrWGoD80emKeR63jNMB6KdX2i6rhsjXGQCBNp5GI9zorIMWNzzOjDbHm42pNcjsPLLEOTugAPAux5-3F-Cqge6UXasy5DiFjVT8tMboeQl9DGgQjgzldRJUyGvK5LCrRuwdikSP8jECrWcDdWchzm_mwum5g2XaHS05-AP0o36aXbH5Nc9tv2eW3F-oL7kA0S4fPPyrF3fOhHJOE8P-NILWbU0cFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83de2e39f8.mp4?token=tnicuHkgkII6Gz_V8yPL8_uF6Wkb3W1OHXQXtRAkeRfz8YY9luafFtAUVrEUoX5pVyAXcrfNnssLyN_y-abFV3aRIFgqm3DpljKtBjOX7HmbrgRDuRzgTi99qwrWGoD80emKeR63jNMB6KdX2i6rhsjXGQCBNp5GI9zorIMWNzzOjDbHm42pNcjsPLLEOTugAPAux5-3F-Cqge6UXasy5DiFjVT8tMboeQl9DGgQjgzldRJUyGvK5LCrRuwdikSP8jECrWcDdWchzm_mwum5g2XaHS05-AP0o36aXbH5Nc9tv2eW3F-oL7kA0S4fPPyrF3fOhHJOE8P-NILWbU0cFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
🏆
سوت شروع «جام وینگری‌ها» زده شد!
اگه فوتبال رو دوست داری، جام وینگری‌ها همون جاییه که نباید از دستش بدی.
😎
⚡
چالش‌های جذاب
🔥
رقابت‌های هیجان‌انگیز
🎁
کلی هدیه خفن در انتظارته
منتظر باش؛ این تازه شروع بازیه!
جزئیات و نحوه شرکت رو توی سایت وینگری‌ها ببین:
🔗
wingeriha.ir
⚠️
هیچ خبر و جایزه‌ای رو از دست نده!
همین حالا عضو کانال شو و ما رو دنبال کن:
🆔
@en_bank_ir
#وینگر
#وین_کاپ
#جام_جهانی
#وینگری_ها
#بانک_اقتصادنوین
🔗
www.enbank.ir
▫️
02162740</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/657797" target="_blank">📅 00:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657796">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dj2qJvM07apHrnUWJXSH9PIpYyPxUFQP57HvIQkg1nm0gG19Jqdv1vUv90Bqa4oaQpXMTBqvI6kq1Q-6166_CpZX_X0orROfuRh-4SqZs1gSc9QYFzx78hHMo-fZnVcGCaYDab0Fh0ehdwP68v1OrbDphU2Ru95r1kojzjFihq1o3cSVT5mHY88tChWrcQgmLgqf0FFRsrLJunri7afV-VhGTi58ryK0DzrygC3vZwUQCW9dCc7nci7FRe6PoKtkyKBgqXAEOBPV9sDDI-2zczL4q9WK7AJX7q8gJWtKgSwTOaWFjhKSMyPPsVU9kAHfrsF961OPcFpxLgl4gIBqWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آرژانتین تنها تیم جام جهانی است که تا به امروز تمام بلیت‌های بازی‌های مرحله گروهی‌اش به فروش رفته است
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/657796" target="_blank">📅 00:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657795">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
معاون وزیر امور خارجه ایران در مصاحبه با الجزیره: هیچ هدف‌گیری عمدی از سوی ایران برای بالگرد آمریکایی بر فراز تنگه هرمز صورت نگرفته است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/657795" target="_blank">📅 00:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657794">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
صحبت‌های جنجالی مشاور اسبق هاشمی رفسنجانی: پیامبر چطور با پادشاه حبشه صلح کرد، ما هم همان کار را بکنیم
!
محمدصادق مشایخ، مشاور اسبق رفسنجانی و رئیس کمیسیون اقتصادی بیان امید ایرانیان در
#گفتگو
با خبرفوری:
🔹
سال ۱۴۰۳ گفتیم اگر سفارت آمریکا باز شود، مشکلات حل می‌شود ولی انگار می‌ترسند این کار را بکنند، به هرحال ما داریم ضرر می‌دهیم. ما یک اشتباهی کردیم که سفارت آمریکا را گرفتیم، الان هم ۴۸ سال است که داریم تاوانش را پس می‌دهیم.
🔹
باید آمریکا را همان چیزی که هست ببینیم و باید دید پیامبرمان با پادشاه حبشه و دشمن چیکار کردند و چطور توانستند مکه را با صلح فتح کنند تا ما هم همان کار را بکنیم. بارها این روایت را آقای هاشمی‌ رفسنجانی مطرح کرده‌ بودند که ما بیایم و با آمریکا بسازیم و از این وخامت اوضاع جلوگیری بکنیم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/657794" target="_blank">📅 00:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657793">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QawPMYGzyIwj9rDIxTPtZmTQr31TRruukEt8VTzl-VsTD1ZkdOdeote9AaAD2vyZSYjZNYjckZX9bP3RJ9y-mebGrtIk2UFCS1wnkmQTDdsp57NY7fdaXFzyKAkSNRff9LN7X2PmhojbkRM7njGXCFHpYyWuUjIJOPEeR2fQ6I9UpuixDr64RfbpY9nBvNnvnhiolAvwGh7QrN4VQO2AFoCWBtxoc805YVbfB1CFlR7BnF2NN5gYo9bYGwUsfwg6g5mP-N7oflzTpiicvRx8q8EN8UKhTjP8nM6dAWiXi7f7isQiyfVlEWoXP3CovXSaIuB4PrEvVGLVtADx-4Q2Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله به مقر کمله‌های تجزیه طلب مخالف ایران در اربیل
‌
🔹
مواضع کمله‌های تجزیه طلب مخالف جمهوری اسلامی ایران در اربیل در شمال عراق هدف حمله قرار گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/657793" target="_blank">📅 00:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657791">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UA8_O9sUpNCOuPJxVdZcySwmlfp3exUwD7vnVl0iRC9UwDARqGAifGkepLHFo87T71DpYRwjt2nINvFCw2fu5zBbQ--BaHJZ9kcxcfnpFbvb5mj8a7-rGOcrr4_Wnht2Wpn99Idao3JdogvwFmuOQNIZpTomDCgF4yedtnyLNJoFRJrFij5T01NWwWxWlozqCyoSqt3N2K7VklSaO0Bkxuc9yyfoBF4t86_PksShZCxum3gc-H9gAQo6Wlb1zhJtetJWfE1iHSOpEwOBE60T87n6upb_aO74il8DgeCXih8ewTE3-zaoqALzQJP5GGqHvNAE-uw7dBss7NC2zEnSTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/657791" target="_blank">📅 00:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657790">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
ونس: ایران برای ما یک باتلاق طولانی نخواهد بود  جی‌دی‌ونس، معاون ترامپ در گفتگو با یو‌اس‌ای تودی:
🔹
مطمئنم که دخالت آمریکا در جنگ ایران ظرف یک سال پایان خواهد یافت و به یک باتلاق طولانی تبدیل نخواهد شد. آمریکا یک سال دیگر درباره جنگ ایران صحبت نخواهد کرد.…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/657790" target="_blank">📅 23:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657789">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
ایران: قطعنامه ۲۲۳۱ شورای امنیت سازمان ملل در ۱۸ اکتبر ۲۰۲۵ منقضی شده است
نمایندگی ایران در سازمان ملل متحد:
🔹
باز هم نمایش دیگری از ریاکاری و استانداردهای دوگانه در جلسه و بررسی شورای امنیت سازمان ملل.
🔹
تعدادی از اعضا، به دستور ایالات متحده، ادعاهای بی‌اساس علیه برنامه هسته‌ای صلح‌آمیز ایران را تکرار کردند و کمپین دروغ‌پراکنی ایالات متحده و رژیم اسرائیل را طوطی‌وار تکرار کردند.
🔹
قطعنامه ۲۲۳۱ شورای امنیت سازمان ملل در ۱۸ اکتبر ۲۰۲۵ منقضی شد و تمام مفاد و وظایف مربوطه را به پایان رساند.
🔹
هیچ مبنای قانونی برای کمیته موسوم به ۱۷۳۷ وجود ندارد، هیچ قطعنامه تحریمی شورای امنیت علیه ایران باقی نمانده است و هیچ توجیهی برای تشکیل جلسات تحت دستور کار «عدم اشاعه» وجود ندارد.
🔹
این سوءاستفاده آشکار از اختیارات شورای امنیت و تلاشی عمدی برای گمراه کردن جامعه بین‌المللی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/657789" target="_blank">📅 23:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657788">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
نروژ با «آشپزخانه کامل» راهی جام جهانی ۲۰۲۶ می‌شود
‌
🔹
تیم ملی نروژ تصمیم گرفته برای حفظ آمادگی بازیکنان، بخش بزرگی از غذاهای سنتی خود را به همراه کاروان این تیم به آمریکا منتقل کند.
‌#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/657788" target="_blank">📅 23:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657787">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
نماینده مجلس: زمان پرداخت پاداش نیروهای مسلح مشخص نیست
موحد، عضو کمیسیون اصل نود مجلس شورای اسلامی:
🔹
موضوع پرداخت پاداش و حمایت از نیروهای مسلح به عنوان یک دغدغه جدی در میان نمایندگان مجلس مطرح است و ضرورت پیگیری آن مورد تأکید قرار دارد.
🔹
در حال حاضر زمان مشخصی برای پرداخت این پاداش‌ها اعلام نشده، اما تلاش بر این است که راهکارهای لازم برای رسیدگی به مطالبات نیروهای مسلح در اسرع وقت دنبال شود./ جریان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/657787" target="_blank">📅 23:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657786">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
ترامپ تهدید به حمله کرد؛ ایرانی ها بالگرد پیشرفته ما را سرنگون کردند، ناچاریم پاسخ بدهیم
👇
khabarfoori.com/fa/tiny/news-3221841
🔹
اسرائیل دوباره آتش‌بس لبنان را نقض کرد
👇
khabarfoori.com/fa/tiny/news-3221698
🔹
مرگ تلخ اینفلوئنسر ۲۷ ساله پس از سال‌ها میوه‌خواری
👇
khabarfoori.com/fa/tiny/news-3221683
🔹
سقف تراکنش بانکی اعلام شد
👇
khabarfoori.com/fa/tiny/news-3221829
🔹
عکس گوگوش با تیم ملی فوتبال ایران | خواننده زن چرا حجاب دارد؟
👇
khabarfoori.com/fa/tiny/news-3221720
🔹
ویدئوهای جذاب ما را در وبسایت خبرفوری کلیک کنید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/657786" target="_blank">📅 23:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657785">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhhC8yFNdiAIuLkXa8JC3MWdJEvRhyI1buKPoi6rNVO6P5RABAhKPEekhGK6yULqjjlTYC9udL6mfE910R4pfygbQanxlKmrXptCTDflg3lrhEz6WGyDVSRwpn_QW4q7Bef3Yv7bSDCkJAbunS4mjlLetdLWdEPm9Lq1mAjDfKN7dU1iMXfTntNmVyOAdvnSTZdrXGWNWkeB-MGz8jzmQ9vMsuwInu8VqigGVBzezscxQx88m0E4fzwvbl-ARptisrVdEj8eCq64qocAQR4LxewpqW1Joob09E3E4c-DqVl1po4pQD6bzOHObsbpSx1SvJGnScvGpdqhY9j9yXAtqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
You will be drowned in blood
در خون غرق خواهی شد
#WillPayThePrice
#هزینه_خواهید_داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/657785" target="_blank">📅 23:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657784">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگروه مالی فیروزه | Firouzeh</strong></div>
<div class="tg-text">💎
شمارش معکوس IPO فیروزه آغاز شد
شمارش معکوس برای عرضه اولیه
#وفیروزه
آغاز شد! در این ویدئو با رامین ربیعی، مدیرعامل گروه مالی فیروزه درباره چشم‌انداز این عرضه و شرایطی که فیروزه در آن عرضه اولیه می‌شود، گفت‌وگو کردیم.
00:40 - دو دهه اخیر فیروزه درخشان و سخت بود!
01:11 - تاب‌آوری و استقامت فیروزه ادامه‌دار است...
01:50 - ارزش‌گذاری فیروزه چگونه بود؟
02:17 - دارایی‌های ارزشمند هلدینگ فیروزه
04:00 - داشته‌های پنهان و ارزشمند گروه مالی فیروزه
03:58 - رکورد مشارکت در وفیروزه شکسته خواهد شد؟
🛒
شرکت در عرضه اولیه
«وفیروزه»
در تمام کارگزاری‌ها با ثبت سفارش خرید از طریق سامانه معاملات برخط امکان‌پذیر است.
💎
گروه مالی فیروزه
سرمایه‌گذاری، برای همه مردم ایران
🔜
+982179672000
💎
@firouzeh</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/657784" target="_blank">📅 23:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657783">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed7aa1ed5.mp4?token=ZUVOdZ6vy6Uz5Lw1QDRzPtK2vj6NiEe8BLzxdz0_2qUwnvHZMTaPMPvUV1ULbOWFUqVFbWYmgLF_JaA5QuAr9GRh9PUeuVUu0_mPtT1XRjWvws1iCotAScViLMnatwj7pRVdOjatQOGWSy0I6DKWHC1ahnRr_NdfZcDIaiiJmuIfFl3VBxgmqApyH8sGrM44Dv69eQGCA32UqcWXrEMStDnJ9OjIzZbEj0UQ0_AXeXEAKPvjbW-fIifvD4iqfGDfoRhnp7gmatShJUm8n8FzaNET_z7V538Gefaaf7XEJ2YKx-S1WOHYh3ggRXYjxct3zi3pa3ADMR3YKtrunANiS4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed7aa1ed5.mp4?token=ZUVOdZ6vy6Uz5Lw1QDRzPtK2vj6NiEe8BLzxdz0_2qUwnvHZMTaPMPvUV1ULbOWFUqVFbWYmgLF_JaA5QuAr9GRh9PUeuVUu0_mPtT1XRjWvws1iCotAScViLMnatwj7pRVdOjatQOGWSy0I6DKWHC1ahnRr_NdfZcDIaiiJmuIfFl3VBxgmqApyH8sGrM44Dv69eQGCA32UqcWXrEMStDnJ9OjIzZbEj0UQ0_AXeXEAKPvjbW-fIifvD4iqfGDfoRhnp7gmatShJUm8n8FzaNET_z7V538Gefaaf7XEJ2YKx-S1WOHYh3ggRXYjxct3zi3pa3ADMR3YKtrunANiS4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ابراهیم رضایی، سخنگوی کمیسیون امنیت ملی مجلس: ما از بازگشت به جنگ فراگیر ترسی نداریم/ خطای بزرگ آمریکا این بود که فکر می‌کردند ما آماده نیستیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/657783" target="_blank">📅 23:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657782">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
گروسی در مناظره‌های ژنو میان نامزدهای دبیرکلی سازمان ملل شرکت نکرد
🔹
خبرگزاری «تاس» گزارش داد که رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی در مناظره‌های تلویزیونی میان نامزدهای سمت دبیرکلی سازمان ملل متحد که در ژنو برگزار شد، شرکت نکرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/657782" target="_blank">📅 23:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657780">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea91344616.mp4?token=KDhT_CDdhquuu7NgYNwdMJvWv_icXaRyWyLFJ_D9QL33j8dEjwFcmuxcDcKxdouBRx-7hWFkXKO1AqrTIhmYWCoPMh09fr6S5g3rYyEQM-ylV9LcUZPL-kI171-GIV8bhupQY0EWEq8ZzFvyZNRPlHBzEfqbxh_hqc9b7xEkj3rVSw3CaMLF1KV5SYHwJSJLxq3YNbFsvbjvq8rKYaD-MQCSufxZiMcn7YqBlpC4xRs7R6HGy9xXWRxlVtNJqtVXYwlRWCRt4ATipgXbGi_mt5iN9sR8K6YHew7Tarw2vj0h7qzzztgkqQlRvnrxRxlqC7Z9Ikj-UzmmTpbB2Ohf2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea91344616.mp4?token=KDhT_CDdhquuu7NgYNwdMJvWv_icXaRyWyLFJ_D9QL33j8dEjwFcmuxcDcKxdouBRx-7hWFkXKO1AqrTIhmYWCoPMh09fr6S5g3rYyEQM-ylV9LcUZPL-kI171-GIV8bhupQY0EWEq8ZzFvyZNRPlHBzEfqbxh_hqc9b7xEkj3rVSw3CaMLF1KV5SYHwJSJLxq3YNbFsvbjvq8rKYaD-MQCSufxZiMcn7YqBlpC4xRs7R6HGy9xXWRxlVtNJqtVXYwlRWCRt4ATipgXbGi_mt5iN9sR8K6YHew7Tarw2vj0h7qzzztgkqQlRvnrxRxlqC7Z9Ikj-UzmmTpbB2Ohf2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پروتکل امنیتی سختگیرانه آمریکا باعث اعتراض برخی تیم‌ها و افراد شده است
🔹
ویزای عمر عبدالقادر که به عنوان بهترین داور آفریقایی سال ۲۰۲۵ انتخاب شده بود رد شد و با اینکه وی با پاسپورت دیپلماتیک به آمریکا رفته بود با اعلام فیفا او نمی‌تواند در جام جهانی داوری کند
🔹
ایمن حسین عراقی پس از ورود به آمریکا حدود ۷ ساعت تحت بازجویی نگه داشته شد
🔹
تیم ملی آفریقای جنوبی خیلی دیرتر از موعد مقرر به آمریکا رسید زیرا به بخشی از اعضای هیئت اعزامی ویزا داده نشد
🔹
اعضای کادر تیم ملی سنگال مجبور شدند کفش‌های خود را دربیاورند و مورد بازرسی‌های طولانی قرار گرفتند که باعث اتهامات نژادپرستی شد. تیم ملی ازبکستان با سگ‌های بمب‌یاب بازرسی شد
🔹
درخواست ویزای بسیاری از هوادارانی که قبلاً بلیط خریداری کرده و محل اقامت را رزرو کرده بودند رد شد تا منجر به ضرر مالی هنگفت آنها شود
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/657780" target="_blank">📅 23:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657779">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: به نتانیاهو گفتم نمی‌خواهم کاری کنم که به توافق آسیب بزند، اما گفتم: شما باید از تشخیص خودتان استفاده کنید، فقط بروید و از تشخیص خودتان استفاده کنید، اما نمی‌خواهم توافق آسیب ببیند
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/657779" target="_blank">📅 23:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657778">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
یک مقام ایرانی به الجزیره: بالگرد آپاچی آمریکایی بر فراز آب‌های بین‌المللی پرواز نمی‌کرد
🔹
ما به هرگونه حمله آمریکا به ایران با قدرت و بلافاصله پاسخ خواهیم داد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/657778" target="_blank">📅 23:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657776">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GLujaBmhDGX2TiGAXUyhuKpy7cVC7HAjrRLGGpLKLFDTOOj9FQCs_pg2_0SmkI5ZS7KHW-VXDdjOrDLfX0r-HVCypcz9TpiGT9wWw3135offnwhA2vlIS2H2Phw_vhcm0Et3wETnIdx-0FHsTLR23nTXDWgx76oyPv0-vIpIHoVuFQEaTaH0UFTFIc3IZxzRAKXUJ1Y6P2U1_-oHOQ5XFGUBGCMKDd-nvfGpaCmbPJgbLgtdGRf1oRE1cwH7IFZoQROWviTyWhV8p3BnhgQ4wUWJo7kvOqDTMDy0PMSGTiTndduROIgLgWXwp08CUVIskIAJNFTUoigvWvoRfkhlxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TW56S9-G7gjkrKhkPvRJ5-rUZZdiO0Ec5tV6fpbDwrsK_QO5pTQl6GipH3BjK3ziboDo8F3JiZyCV0QCNrGiSvlhjNcyiaM2NhctSHhJphTAzVzbYQBF87ZWJwaSnTbzyWXcPbzGlOdKXHtBjlYDvHZef_wgSvQ-oMNuh4W1EMG2_lAkzTQVVJAWMMpEv3FsCl03nZeFo6yRkBVwJCCLAZr0KF9dE-bU4KQLn96Mp23HUm4rDZDHU_5nNpL8p5hFS8r9nESaQp2BUtyOUmeJdd4_cm043r8uE3XHtZrkZ8FaJf9usAJIPoWUkLqPgHJzxdGv3-iPDLoPqOBRKqvBwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
جزئیاتی از عملیات «نصر»؛ از نواتیم تا تل‌نوف زیر آتش موشک‌های ایران
‌
🔹
در جریان عملیات موشکی آخر ایران علیه رژیم صهیونیستی، اهدافی از جمله پایگاه نواتیم، پایگاه طبریا به‌عنوان یکی از مراکز پشتیبانی زرهی در شمال، فرودگاه نظامی رامات داوید و مرکز پهپادی تل‌نوف مورد حمله قرار گرفتند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/657776" target="_blank">📅 23:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657775">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72a33ce334.mp4?token=p5QwystnW6WbHMviqeK5opEpQGVhIqIwlqBbeFIL3b9fztzqMgqCqiUiMW6xsEe2aICQmerqnfhBrQiKsI70RUKya-putyMkVEdOrCkXdyaXQXb5cAENFgt91ccFw7TxOy6pur_aiqAMR0kYvIPbI0APPbhAYb8HQGRxyTJIIOhknBeEvCmnjkKLW1qrg-zgEWaRsx5k9pn-CRIexg6Y9ZtxtoA4EyAL4XqSx1OMOatDEH6ZmgdPDaqghr8wMEo0MfBM_6O7DaSuleM3nhHVmk8rGWJU987yoC72-v6olPD0JW2oUsnaUV9CJPslJXxdYTQBRO41fklGE9yopBewTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72a33ce334.mp4?token=p5QwystnW6WbHMviqeK5opEpQGVhIqIwlqBbeFIL3b9fztzqMgqCqiUiMW6xsEe2aICQmerqnfhBrQiKsI70RUKya-putyMkVEdOrCkXdyaXQXb5cAENFgt91ccFw7TxOy6pur_aiqAMR0kYvIPbI0APPbhAYb8HQGRxyTJIIOhknBeEvCmnjkKLW1qrg-zgEWaRsx5k9pn-CRIexg6Y9ZtxtoA4EyAL4XqSx1OMOatDEH6ZmgdPDaqghr8wMEo0MfBM_6O7DaSuleM3nhHVmk8rGWJU987yoC72-v6olPD0JW2oUsnaUV9CJPslJXxdYTQBRO41fklGE9yopBewTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا ایران می‌تواند تجارت جهانی را فلج کند؟
/ جریان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/657775" target="_blank">📅 23:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657774">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 شما بیشتر کدام گروه از صنایع دستی ایران را می‌پسندید؟</h4>
<ul>
<li>✓ ظروف هنری (میناکاری، خاتم‌کاری و ...)</li>
<li>✓ مجسمه، سفال و ...</li>
<li>✓ دست‌بافته‌ و رودوزی‌های سنتی</li>
<li>✓ صنایع چوبی و چرمی</li>
<li>✓ فرش و قالیچه و گلیم</li>
</ul>
</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/657774" target="_blank">📅 23:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657773">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f59f2eb425.mp4?token=c56Frk4pLG6oWEaa-hRH-B4DYtM3tCKpYrSj-0wMibc7_VxWwP6Kn_GLbiGymZGtRHF0ZOKjGSQwIg5InvL_HWIZhf3ICl8jiaw3z2uDsFu2vYtUL6YFBrVNJPkFeZ2XThm341B1TAW2Qctn9kCLpfFAU7xpDz5hZ3PY2C-D0At6SRhLYpIoLSYDzeQml0YoNyAKIpymI1DARaZkwE6gHUX41HHhj0WsYc8YRM9RzBvh7UXait4gaCssIf7zbwV2NrJ6RbXBWbLCL8rE3ZE0UXNtDl9_ZBJRjyFdK1Tc6AP8YVg8004a_41VDMGaXOGHcHXnF8O8xlEDm-Gran_RyoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f59f2eb425.mp4?token=c56Frk4pLG6oWEaa-hRH-B4DYtM3tCKpYrSj-0wMibc7_VxWwP6Kn_GLbiGymZGtRHF0ZOKjGSQwIg5InvL_HWIZhf3ICl8jiaw3z2uDsFu2vYtUL6YFBrVNJPkFeZ2XThm341B1TAW2Qctn9kCLpfFAU7xpDz5hZ3PY2C-D0At6SRhLYpIoLSYDzeQml0YoNyAKIpymI1DARaZkwE6gHUX41HHhj0WsYc8YRM9RzBvh7UXait4gaCssIf7zbwV2NrJ6RbXBWbLCL8rE3ZE0UXNtDl9_ZBJRjyFdK1Tc6AP8YVg8004a_41VDMGaXOGHcHXnF8O8xlEDm-Gran_RyoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ما ذره‌ای از انتقام ‌خون رهبر شهیدمان عقب‌نشینی نمی‌کنیم
!
🔹
رهبر ما را شهید کرده‌اند باید تاوان بدهند!
#WillPayThePrice
‎
#هزینه_خواهید_داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/657773" target="_blank">📅 23:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657772">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d950ab048.mp4?token=JpGWT9E6AvUbbqgXicI04O-BbdbCzI9zyAB3-uY-6Ko-r9uzAYNoR6u8BDdL8vUtHxHf9X-kiBv8m0ftv2cUvsKkcd-IevTOlW1VAHkGNtBtytiGbyk3prtTsQP-RT8GlM-i-ZqXAm8XsFtOqqn3KUZ7MQt5dH7HCjuZZ3HgyH58vvnvJcTfmWYwvGVlElH4pDiFDpPBX7Vt_YKy7rq19ocUES0by910KRWNv6baBW1ZDDMYfKKPRSj71q5KkMZfP6wuWSgBDYbOS3wlHpEkGGzuAs8DZ9tJ6doThrNz2GccFV3OMPu6ZeX8nGi9vTOh8k3cPJVdaMJqVl72Ade5nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d950ab048.mp4?token=JpGWT9E6AvUbbqgXicI04O-BbdbCzI9zyAB3-uY-6Ko-r9uzAYNoR6u8BDdL8vUtHxHf9X-kiBv8m0ftv2cUvsKkcd-IevTOlW1VAHkGNtBtytiGbyk3prtTsQP-RT8GlM-i-ZqXAm8XsFtOqqn3KUZ7MQt5dH7HCjuZZ3HgyH58vvnvJcTfmWYwvGVlElH4pDiFDpPBX7Vt_YKy7rq19ocUES0by910KRWNv6baBW1ZDDMYfKKPRSj71q5KkMZfP6wuWSgBDYbOS3wlHpEkGGzuAs8DZ9tJ6doThrNz2GccFV3OMPu6ZeX8nGi9vTOh8k3cPJVdaMJqVl72Ade5nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فاجعه چاقی در بانوان؛ ۸۷ درصد زنان اضافه وزن دارند
@Tv_Fori</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/657772" target="_blank">📅 23:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657771">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a01d81fcb.mp4?token=qC-DRyiElGHwmZAJIz55wh_wRQg9KKPGRBtbQIVDUpCkkcGSoCvG6zblv047RLoNUjXdOPCtXm9bgwDr50XEfWW78f_6W_B_OShXdYDE_-3dFf5N_MKRHnlBgozJo2E_nSdNr8ulelde7JvBeevzB_B5jJ6JkezFRIux4R9N4lXr4CmUny1qbEL-Gzz7VWi4pokNiJKdh24A7C7KEK2jeKGGkLnyjs3lZDOVfgEDxkAmbm1zfZWOYIHMP_nUMwvUS0BxKFziz4qOfTZZ5MyLcL5zbdrRLom6w9c_dM1C8L_kmQ8Z8basTpoTtBynLHIr2nbELVDe8SIkquvYkT9LKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a01d81fcb.mp4?token=qC-DRyiElGHwmZAJIz55wh_wRQg9KKPGRBtbQIVDUpCkkcGSoCvG6zblv047RLoNUjXdOPCtXm9bgwDr50XEfWW78f_6W_B_OShXdYDE_-3dFf5N_MKRHnlBgozJo2E_nSdNr8ulelde7JvBeevzB_B5jJ6JkezFRIux4R9N4lXr4CmUny1qbEL-Gzz7VWi4pokNiJKdh24A7C7KEK2jeKGGkLnyjs3lZDOVfgEDxkAmbm1zfZWOYIHMP_nUMwvUS0BxKFziz4qOfTZZ5MyLcL5zbdrRLom6w9c_dM1C8L_kmQ8Z8basTpoTtBynLHIr2nbELVDe8SIkquvYkT9LKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت تکان‌دهنده جواد موگویی از برخورد صدها هزار ترکش در یک لحظه به شهر لامرد
🔹
ترکش‌ها حتی آسفالت را هم سوراخ کرده‌اند و به هر خانه صدها ترکش خورده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/657771" target="_blank">📅 23:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657770">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_P1y6llo8_dD7ap9CoxskmLhpl2MtzGuqwBmw7gSvrJyRadusIIZmynNG1UcZt6jjVKZGywWQgSVuuNzntn0pjGcfow_iPcY7O_MAkhBvfixhlmG_uJsldZgymjcvYo18JlI5hMp6fGaB_mt4hdtYnOKiFPXKiD9ib7E5sRs_ZYK-x35gXAnNw4mf3BM5w4yOhOdKGSDNmMapgD0GVqKn7nHq6nnuLNUZ9nyQs5TfGQuUb1UPyl6piviXjfmyDjw06BEJ3iSv4OfiI-EWUdZjqz4XltQ-SwC3dpsmZe1106KAdNkBgtfpx9JE6ZqAkhcWwraNlTLISRA2PWOGYuqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رونمایی رسمی فیفا از جایزه بهترین بازیکن زمین جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/657770" target="_blank">📅 23:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657769">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KiQnfq7HCzZxqq8ME24n0xlbv0VNrQPTKbwsJBnd8QWxSo86_s0ZYMwDy2PIzin_lPYxOk56mlRZnM0isRg2VRydod8adknX0SEsTT_HS56nkUAbJJOhOoKmIJ68tvznVjOfL735t_9pDNb1pQql-RuUKE5t6bR4N_JaUJN6SDer9aGIlkchK4CeocCtVrc4ELN7aEPpXkAAAYL56l9ho_J4aHMYaOjOvgYV8_woNHf44WA_x43x3CYodkKqH65VxaL_eO84h_INXP1QtQipeFyeyoRiBYPk0uOJmXnYeibNp9SMxagJhQH92470ShXh9lbCAIRHmOnN3382gWoQfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نه صدا نه سیما
🔹
انتقادهای اخیر از عملکرد صداوسیما نسبت به دولت به جایی رسیده که واکنش رئیس‌جمهور را نیز در پی داشته است. مسعود پزشکیان با گلایه‌ای تند از رویکرد برخی برنامه‌ها و فعالان رسانه‌ای در قبال دولت، هشدار داده که تداوم نقدهای غیرمنصفانه در شرایط حساس کنونی به پاسخ متقابل دولت منجر خواهد شد. با این حال در کنار انتقادها به عملکرد رسانه ملی، برخی منتقدان معتقدند دولت نیز در زمینه اطلاع‌رسانی، پاسخگویی و گفت‌وگوی شفاف با مردم درباره مسائل و چالش‌های موجود کشور عملکرد موفقی نداشته است.
🔹
هفتصدوهفتادمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/657769" target="_blank">📅 22:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657768">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهای شدید در اربیل عراق
🔹
منابع خبری از حمله موشکی و پهپادی به مقر گروهک‌های تروریستی تجزیه طلب وابسته به آمریکا در اربیل عراق خبر دادند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/657768" target="_blank">📅 22:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657767">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
یک منبع آگاه نزدیک به تیم مذاکره کننده ایرانی: پیشنهاد جدیدی از سوی ایران برای آمریکا ارسال نشده است/فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/657767" target="_blank">📅 22:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657766">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99f52d14f4.mp4?token=Sc4vQWEqPips-VYkPtcDjJ1y6ZHJlBf2wTOunvJo3iMaTvVC5CNdTtUhMZ3JEbXkdAcdwX9-dninvgclYAiOFHIiB_EAS958gNV2MIAU3841CtbboktNwcw4rkoKd_I4htjvpcsWSZvN4bHgDR4jpA1uIycyEVfcs4j93zw_jXExICx9upa0FO5Vmw2rg9Mb2CHZXdz3TaQ1QRcBwO24q_XtrJ7TrEwU9sFFoggLwMEaVidqfY1HCJXF1Q2aw0dRQ4MKT2W2iWYmsIwEJgZwFk_jiZYUfKpGN0auwO4UY3TXGfeL3PNIjoZpC-Qv68RwOs8Q9DB4yZqwjEtZZiuqig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99f52d14f4.mp4?token=Sc4vQWEqPips-VYkPtcDjJ1y6ZHJlBf2wTOunvJo3iMaTvVC5CNdTtUhMZ3JEbXkdAcdwX9-dninvgclYAiOFHIiB_EAS958gNV2MIAU3841CtbboktNwcw4rkoKd_I4htjvpcsWSZvN4bHgDR4jpA1uIycyEVfcs4j93zw_jXExICx9upa0FO5Vmw2rg9Mb2CHZXdz3TaQ1QRcBwO24q_XtrJ7TrEwU9sFFoggLwMEaVidqfY1HCJXF1Q2aw0dRQ4MKT2W2iWYmsIwEJgZwFk_jiZYUfKpGN0auwO4UY3TXGfeL3PNIjoZpC-Qv68RwOs8Q9DB4yZqwjEtZZiuqig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قشقاوی، عضو کمیسیون امنیت ملی مجلس: نسل جدید جوانان ما بسیار مطالبه‌گرتر از ما دیپلمات‌های پیر است
🔹
نسل زد می‌گوید چرا ما از تنگۀ هرمز نباید عواید مالی داشته باشیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/657766" target="_blank">📅 22:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657765">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
یک مقام ایرانی به الجزیره: بالگرد آپاچی آمریکایی بر فراز آب‌های بین‌المللی پرواز نمی‌کرد
🔹
ما به هرگونه حمله آمریکا به ایران با قدرت و بلافاصله پاسخ خواهیم داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/657765" target="_blank">📅 22:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657764">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhr0cmEfaaot0F6sagcRAvunQ1eYZQyxZDr2b7Wr0thHQpvYUgCfhvC9slAS0DXKaJCcBqhxumCFdGDWDBKNLN_h0EqCzevJbssKVCbF4a2cHiG_Bx1GeeayaWQ2CFbd2HR0R-sd2zoNVWFMBHtm1jY0wGfz0R1chiQqphWBoKoX8bfjkOGJ1urOTewJhoS7T9o7IGcn-vLtV2CcRAPe2V9AjEUesxR8By2jVH92AmErbXBrrn39KyPW52NGYpDldGLXLtHOOtN1zoCX4USdSg3N2BIDKfh3MceGjXn1ft_-6PywwbnYe9TT5fgHFmzUYXEKB61gl48R_PqFukAP5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشتازی منطقه آزاد کیش در مبارزه با رانتخواری؛ بازگشت ۲۴۳ هکتار زمین به بیت‌المال
🔹
سازمان منطقه آزاد کیش در یکی از بزرگ‌ترین اقدامات حقوقی و ثبتی سال‌های اخیر، موفق شد ۲۴۳ هکتار از اراضی بلااستفاده و فاقد ساخت‌وساز را آزادسازی و به بیت‌المال بازگرداند. ارزش این اراضی بیش از ۲۰۰ هزار میلیارد تومان برآورد می‌شود؛ اقدامی که علاوه بر صیانت از حقوق عمومی، گامی مؤثر در مقابله با زمین‌خواری، جلوگیری از انباشت دارایی‌های راکد و افزایش شفافیت در مدیریت اراضی به شمار می‌رود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/657764" target="_blank">📅 22:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657763">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
ستاد تشییع امام شهید به ریاست عارف تشکیل جلسه داد
معاون اول رئیس‌جمهور:
🔹
مراسم تشییع و وداع با امام شهید خامنه‌ای باید با رویکردی مردمی برگزار شود.
🔹
در این مراسم همه میزبان هستند و هیچ‌کس مهمان نیست؛ تنها برای ایجاد نظم و هماهنگی، جمعی از افراد مسئولیت مدیریت امور را بر عهده گرفته‌اند.
🔹
برخی کشورهای همسایه اعلام کرده‌اند که بیش از یک میلیون نفر از شهروندانشان متقاضی حضور در مراسم هستند.
🔹
ظرفیت‌های کشور محدود است و امکان پذیرش همه متقاضیان وجود ندارد.
🔹
برخی کشورها حتی اعلام کرده‌اند که تمام امور اجرایی و اقامتی شهروندان خود را بر عهده می‌گیرند و تنها خواهان صدور مجوز ورود هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/657763" target="_blank">📅 22:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657762">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBF-bc-E2YCKgCZEWqtOUPR8S_lXaPlU_L9syEjGSzZ9GcwVMif7WTM0UH6KZQbta_sAjWCz_zque8BPNuc_2KIE4asrvRS4UhDDOmpV4d2ZePEpQuH43vnCJt5uAPg81pFSubtNbKg19PTb6bXdJWe7UPnaAS0Y9JPWEp3VeiG5mQZluu_n_9657DDFTA3-8cDBwcaY3gNV5vQYqU_rCQIB2f3YU3JQTmq93U5Qv7ZMLMbiRSkTd4IuOdlH4CGLQtiTFY2DWNlxQ4ONEoo1UgBjoZwqUQhCLLmhXFuk5p0A8iQNu_pAO4xWXGdSGGmPQYt-f-9mQYNForWGvwJ5MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار حنظله به نیروهای آمریکایی‌: آمریکایی‌ها درصورت هر اقدام علیه ایران باید جنازه سربازان خود را از مخفی‌ترین پایگاه‌های خود خارج کنند‌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/657762" target="_blank">📅 22:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657761">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e92c29ad0a.mp4?token=cjenjw1_O8-mhsUSzexexazgGPNWBkXYgcTHFhZqesqpFgqofkyDoZk6PAJQqJtL9Zg-Jr5C38rD7VPb445-ohePiYzAtlB6norfa_Y7CHcKJK4VTSsSGXq16_hDBeKXo4gBFWpMR4DVEcBK3TFZX2CjOtfTxFu6uGpZlVfhnFdgW83DINMNXarCpThnB_xmy11LwOS1kRKM2G-C_UR-CYoMZUJfWQUfQCMu8vx3JoHMvOt2uTMvRJl3tWpQDF7BFAu4I7pq32Lt4s1e-QaN1GUGf7XQ87xDx_RR0WM-YZ9aVZ_tvr8gbWRgG8y5ybdAOmUj-ow0tQW-IohLcr9OlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e92c29ad0a.mp4?token=cjenjw1_O8-mhsUSzexexazgGPNWBkXYgcTHFhZqesqpFgqofkyDoZk6PAJQqJtL9Zg-Jr5C38rD7VPb445-ohePiYzAtlB6norfa_Y7CHcKJK4VTSsSGXq16_hDBeKXo4gBFWpMR4DVEcBK3TFZX2CjOtfTxFu6uGpZlVfhnFdgW83DINMNXarCpThnB_xmy11LwOS1kRKM2G-C_UR-CYoMZUJfWQUfQCMu8vx3JoHMvOt2uTMvRJl3tWpQDF7BFAu4I7pq32Lt4s1e-QaN1GUGf7XQ87xDx_RR0WM-YZ9aVZ_tvr8gbWRgG8y5ybdAOmUj-ow0tQW-IohLcr9OlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آمریکا در ۳۰ ثانیه ۷۲۰ هزار ترکش بر سر مردم لامرد ریخت
!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/657761" target="_blank">📅 22:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657760">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
وقتی از ترامپ در مصاحبه با ABC پرسیده شد که آیا آمریکا در بازسازی ایران پس از جنگ کمک خواهد کرد، او گفت که کمک خواهد کرد اما افزود ما نصف نفت‌شان را خواهیم گرفت
ترامپ:
🔹
کسی باید تمام آن زیرساخت‌ها را بسازد، پل‌های جدید، این‌های جدید، آن‌های جدید، نیروگاه‌های جدید... آنها درباره یک تریلیون دلار صحبت می‌کنند، احتمالاً بیشتر... به همین دلیل است که احتمالاً ما در بازسازی دخالت خواهیم کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/657760" target="_blank">📅 22:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657759">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
کانال آی ۲۴ نیوز اسرائیل: هشدار نتانیاهو: ممکن است مجبور شویم بدون پشتیبانی آمریکا با ایران مقابله کنیم
‌
🔹
پس از تماس تلفنی ترامپ برای توقف حملات اسرائیل در پاسخ به رگبار موشکی ایران، نتانیاهو به وزیران کابینه خود چنین هشداری داد ممکن است به وضعیتی برسیم که مجبور شویم به تنهایی و بدون پشتیبانی آمریکا با ایرانی‌ها مقابله کنیم، با تمام هزینه‌هایی که این موضوع به همراه دارد، کمبود مهمات و انزوای بین‌المللی.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/657759" target="_blank">📅 22:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657758">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2eb207decc.mp4?token=N9X8CTUkHTI24ukvCVeUyZUdfEcU4rKD-RbU8fagmhf76KC-ZFKE0LwkrgjR3DJQ0Yt91-pvJRR_vLw2Bd668s4DqRrsTVYaOS-x6YpEdOyvn7sU_0G77OpmVZAYnjeTuZbRnbV0Zj9fjDzUH2YtbcKv3aisZ1PIGxV9gSPOpXeJIYe9RJlQpk_-U-j4_bmCXC1f01skbaPHaQENZ_oIxfQIvANi4-eOGmvdJc0C-eikuWeVWz0KpsBQKOnIHHbUtHiRXHKojb1JucOMCw0YL1PvpLHbZOl9udXDjKFTlbSXnxD6kMe5w-PF0uY4F0HwYXbxva8i_YTZeXjIQKbzfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2eb207decc.mp4?token=N9X8CTUkHTI24ukvCVeUyZUdfEcU4rKD-RbU8fagmhf76KC-ZFKE0LwkrgjR3DJQ0Yt91-pvJRR_vLw2Bd668s4DqRrsTVYaOS-x6YpEdOyvn7sU_0G77OpmVZAYnjeTuZbRnbV0Zj9fjDzUH2YtbcKv3aisZ1PIGxV9gSPOpXeJIYe9RJlQpk_-U-j4_bmCXC1f01skbaPHaQENZ_oIxfQIvANi4-eOGmvdJc0C-eikuWeVWz0KpsBQKOnIHHbUtHiRXHKojb1JucOMCw0YL1PvpLHbZOl9udXDjKFTlbSXnxD6kMe5w-PF0uY4F0HwYXbxva8i_YTZeXjIQKbzfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی مجلس: ضربات کوبندۀ ایران به رژیم‌صهیونیستی نشان داد آمریکا حداقل در ظاهر از حمایتش نسبت به اسرائیل عقب‌نشینی کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/657758" target="_blank">📅 22:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657757">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKqYfol_49t1snw-ONzHYoxVDvab7Y8KrWjhukh2Bg6O54kr358ZAZwjEEdqBacspmTEE6HS1Ym6hvZwMTxW3oAPfF0bThvXiPOpSvgMzDr9Lf2Bjrp4SSsy_cZ0Ha8BGpANY9tb-oOnd5a6mN52RZG9TfpJPbrfmn5BmNdgV1ukb80HTKsISiDZqxfRj3UsqvakPW6JIaibgUc6HX7n2TPZkFzWFXWj-whPn3qXh6wtZlTERz7F36QTmbFw9c8IJUu5mJIhqlPt7GJDhOAUMK8Myf1TpfiZrympQWhX6zQPElfa15hPoRx3ypsSba6onpk_8ZT3yFchJirQiMinoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آخرین قیمت نفت در جریان اتفاقات اخیر  ۹۱.۳۵ دلار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/657757" target="_blank">📅 22:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657756">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2abcc4f63.mp4?token=l_4sEnFpW4hJM6pprBQ3plupHoOG0lye3juaTYmPZw5B2V6DriMg2Pp2TPKQQVhC67UXh4XlMugqxGohJo4L9aggFXAwJKvFJ2LSX1ZwjorNGB15n6hF9OygO5hPhZqGohiZmBMC0Grp0sRdm6uCojBbOBGzCt5fctVriPY8HLAeI_Un9I0aW8j6avOyS9nk5T-6IwXkyoAZ65U2m-2QGcMdm9fSk90ARXn5vLhK_uQglnkxZ16ifT9_hgrHJpBfGqAnOxQVPs7yjz7iVPR_AyVjiK40iBE7VZg0hXLiUhyWAg-EDXnOvFBHOtE6DPyUm4qt0j_ILfmYQZ9PIgIB6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2abcc4f63.mp4?token=l_4sEnFpW4hJM6pprBQ3plupHoOG0lye3juaTYmPZw5B2V6DriMg2Pp2TPKQQVhC67UXh4XlMugqxGohJo4L9aggFXAwJKvFJ2LSX1ZwjorNGB15n6hF9OygO5hPhZqGohiZmBMC0Grp0sRdm6uCojBbOBGzCt5fctVriPY8HLAeI_Un9I0aW8j6avOyS9nk5T-6IwXkyoAZ65U2m-2QGcMdm9fSk90ARXn5vLhK_uQglnkxZ16ifT9_hgrHJpBfGqAnOxQVPs7yjz7iVPR_AyVjiK40iBE7VZg0hXLiUhyWAg-EDXnOvFBHOtE6DPyUm4qt0j_ILfmYQZ9PIgIB6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💫
زابل؛ قاب‌هایی از دل‌های مهربان | بخش سوم
💫
🔸
#گزارش‌تصویری
از توزیع ۱۲۰ کیسه آرد در روستاهای کم‌برخوردار و مرزی شهرستان زابل، به همت
#هیأت_قرار
و دستان مهربان خیرین عزیز
💳
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇
5029087002135690</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/657756" target="_blank">📅 22:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657751">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uY7HI7DFU3-A-BJEmzAEn6PIwFz1qxE3ayRCJ2TyZ0rQNZ6V39GYCH2DcKnYciZiP8CRv-RkGTmdV4HqiqIUVCpr8xemVa2cOHEICCodBWo12r-uIrTJ2G8iiu66v1r1JxGNNr-Bwv5XPez-Jlt82H-SZ7QpHILcdNDk5IQYeTGxrU2VU1UQEzwndMW5Ta4kr9vxs1FUPj59Zh8nOxlIol8B8uhJPOSddUQorI_x0Valyp8Gq-HmvT8l8G3WFz01ChcFKGcua1ZsNkZzPYd7SGhgci1nEuuBbkghYOkb1XTiEHfFoazEwPk2qNxf0xsS2UcFG2Vx5-qiAzQ9KSrjQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gKcMtAmEwYccBatejZ-cdCsXqSjpDObr2gkd_uVMmpTWUJcqeVEgsD6QKwtUFe1zSXR-ZJhKkp6B3-jyMokO1Q4NAw0Kt0-QreYeUEvm2UHfk7fqd8xNKi3dakIOrHdelRZyhbwuEOkzbbtfdkIrTxjwCz5eAWDFsqmsAR8Wj9ZTotew856gzQmJ_g8YY3Diz7vIu7mNKQ52wlX0f1ikOD7C9tzp2CaQqSQi7aYIAa-Db0ldnkIOo4RYuYKHbCUrdwzSBoBo7PKx3EFEf1Ml6XdaUAqvTOgygUo0Gh_bxxLCKRxBULqIXkV1Tm-dF23lvJ07z6e7r_xz8pDHVcEH-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AtaFGhlNK8CAIIFQh4UqzI3TLIHGT8TuKesBBgz7U9fW-eUDrJtuJqNQVjTafNJ3WoufrCWb1RXt9F4NK7dquY5Z2IvQRTxkSCapVdL4PFuZy32aVLw3B6OG7R9CLlbj4xm4sw-40nTyH_vmirYHvajv540EuqAVpTiTX3AgQ2P8H29qvBR6ZIOksy87P-j8dAOYJXe8WmFNMGF3MnNbzapixUbv2q71_rmfXfF03l1HHrCJl1FKKxdNIQneANthPNll4mdRbls_QEpoWS7yxtABpbL87VmpWFTAcsrw2hFTsP54Aniq-yYYL1MtwVBA_ia2MjEDxb46A-aAgqht-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WWek70UJxdTBlyFEUTOaWCG4VUSZvK9XjT8uSB6TZwkXNXswu-FWIkt8kIDMX6ab0i4SF5buqGoMLo-8aryIx7oqM7GM2LMPlD0UxPV9TQ9sEQeF20DcM9CDdvT0tnr4aRsUO8D3yaA-2O37zX037iD26caJS9RZqjK_CHnHB6c4ojhJHsuaeQRmaMby7kxl0tA7N36chAarLrWr7GvJ47XchCBWo3t1CD7K9kw42lOjHHwrY_ek-jxdCqsEoo0YzDK8HR95RUB1SqHLwE8fmOD0XAlGtenRFHPUdDnDcv3tNSuiDljC2UdjPulevdIj38-mXLlHYOrRqGkZXqB_Ug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از اسکورت اتوبوس تیم ملی توسط گارد ملی مکزیک
🔹
اسکورت تیم ملی در مسیر هتل تا محل تمرین در تیخوانا که بازتاب گسترده‌ای داشته است؛ گفته می‌شود به دلیل اعتراضات اخیر در مکزیک و برای حفظ امنیت تیم ملی، این تدابیر شدید امنیتی در نظر گرفته شده است.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/657751" target="_blank">📅 22:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657750">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
ترامپ باز هم ایران را تهدید کرد: ممکن است مجبور شویم کل زیرساخت‌های یک کشور را نابود کنیم
‌
ادعای ترامپ متوهم:
🔹
خیلی ساده است، کسی که قدرت دارد برنده است. ما تمام قدرت را داریم
🔹
وقتی از ترامپ پرسیده شد که آیا آمریکا ممکن است بعداً به بازسازی ایران کمک کند، او پاسخ داد: «بله»، و آن را با طرح مارشال مقایسه کرد و سپس افزود: «اما نیمی از نفت‌شان را خواهیم گرفت»
🔹
اگر احمق باشند، در نهایت به جایی می‌رسیم که مجبور شویم کل زیرساخت‌های یک کشور را نابود کنیم.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/657750" target="_blank">📅 22:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657749">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pte9QrWtrH8WedXJcEnukjZUN1R0iMSqPImCwzTeMOZFWQegSUsIcDowcVmv_rr_GEeALBqw7D1_kP3-r7hRHkcsDbIQo7L30qoVZicRAao_HrDQN14eDd-EeWUSDUuNFKZBBhIald9fkPfinQOfX5Bp8Ricd2K1946sg61NXSxcg33ma2kjamI_zW9Ivvu2C_58Nr5-tZtYweWDQ5vjPjBT_rbrY9Ur6W2jbbczR7MltcIMOj3rdsSS7L3XEVEzIFtln7eyAuoxtNdcQvdNd-HD7cFXRtY3F6SE9BOmWZ9JwFNA6rcCsi1cNsek4l8MwaDc3EF7Uv-eOJs89541RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر پربازدید و تهدیدآمیز از لیست عاملان و آمران ترور رهبر شهید انقلاب در رسانه‌های بین المللی
#WillPayThePrice
‎
#هزینه_خواهید_داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/657749" target="_blank">📅 22:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657748">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGExIZhGk21EUCWTzNS0fDlHJ02B3lDAgJNrsdHo3Np4eeK2G82Un_PQHAUysDo6V-K2j0XijSgB7ewNm-g8uumIV18FxGbCaSg9uC6jMGEgN9xONlvbJpA-nvGOPyXJsRFLjHQcubXIC7U1yemTE-UEkW83VFxxuEXBPWpFAisvW1piK1I8uigIlHD8XlmQiQJFTvmaa02z5lHREFuZmX4JcComvoJM-DlaJ1OlDHjq-41B_QhEhnYnevE9BnNrT-CFJAmShrrXej6KHuU4GN749NKn1iepj_UvN6TY-i39aKFT9tiNKHIWa0_CHaY1HKg-LELfjsX6B2J7XEoUiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هنوز ۵ گیگ اینترنت رایگان نگرفتی؟
برای شروع پیش‌بینی‌ها:
1️⃣
وارد اپلیکیشن «همراه من» شو
2️⃣
گزینه زمین بازی (جام جهانی) انتخاب کن
3️⃣
مسابقه‌های جام جهانی رو پیش‌بینی کن
4️⃣
۵ گیگ اینترنت هدیه بگیر و برای جوایز میلیاردی رقابت کن
🏆
⚽️
در «همراه من» پیش‌بینی کن و برنده شو!
👇
👇
https://www.mci.ir/-4S0XAJB</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/657748" target="_blank">📅 22:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657745">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_QevxQdh-xZG3C4_YfdRjZGq79P3b3RRrp5Mtzu4sRJ5gOUyDPHJUfheQjlTI_AyWda87ea4Cj9uQ6GQstjE0psxz4YxfJvODZbRpXc3BA8cFZ6JS3IbpUDaTHqbwMjz7M7iJ1WLqoBhIWN-UT2i_RbcKeXiIbPM7McnxJ9lD4MNt3C9uYL2MND9zjQANxxo0x7Q1SdWuZBICZHQxOaK6t19Nl9Ye2wFEzeMjPP8Gb6gA7raxupJ1WpVHjHbD5dhC76MpPm74kRoosknVD0MIQ6jasPANY3fuuQGgK_96wJDZ1Nqu1S8Mv35v6UQG2GuzfhtCgJb4JllSSmtJTiuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
بدون قرعه‌کشی، طلا ببرید!
صندوق طلای «رز ترنج» فرصتی فراهم کرده تا اولین تجربه سرمایه‌گذاری در صندوق طلا را با دریافت هدیه و بدون هیچ هزینه‌ای داشته باشید.
در این طرح،
از ۱۰ تا ۱۰٬۰۰۰ واحد از صندوق طلای «رز ترنج» به‌عنوان هدیه
اولین سرمایه‌گذاری به شما اعطا می‌شود.
📌
اینجا کلیک کنید وسرمایه‌گذاری امن و مطمئن با دریافت هدیه طلا را آغاز کنید
.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/657745" target="_blank">📅 22:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657744">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48568ab659.mp4?token=Nfx7V4usxKKYiczoCi_iTOCS-cHrKiDU647wkvhyD6bnlXKAQgFaXLJZe4UrgDa9oVhpfsJyDaL6FUe07zX6IaufY9KAwEbkRfsx_4LB9RvZL42bVnp0mz8yRXVwEaOLjRc-NUHQevVUwHA13SKKKP9kbx2UV_dTMb7Hb0k0pPXiOI6tAi5dxUrIa_FtAxggrbMMeYds9Xct51-3KXAqaXje4MGlRwi--hCvf1-r2b7pcBnRqbXNl42b5O3Y1o1nUGlkUeJWQwvRA0RrYVygOmtdP3-aSeVtX92sdfeUszWFkw-Fx4KyO8fURaix9nKhpgQIU2X9HVyzFh_czWRLDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48568ab659.mp4?token=Nfx7V4usxKKYiczoCi_iTOCS-cHrKiDU647wkvhyD6bnlXKAQgFaXLJZe4UrgDa9oVhpfsJyDaL6FUe07zX6IaufY9KAwEbkRfsx_4LB9RvZL42bVnp0mz8yRXVwEaOLjRc-NUHQevVUwHA13SKKKP9kbx2UV_dTMb7Hb0k0pPXiOI6tAi5dxUrIa_FtAxggrbMMeYds9Xct51-3KXAqaXje4MGlRwi--hCvf1-r2b7pcBnRqbXNl42b5O3Y1o1nUGlkUeJWQwvRA0RrYVygOmtdP3-aSeVtX92sdfeUszWFkw-Fx4KyO8fURaix9nKhpgQIU2X9HVyzFh_czWRLDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قشقاوی، عضو کمیسیون امنیت ملی مجلس: تا در کل لبنان آتش‌بس برقرار نشود، امکان ندارد جنگ به پایان برسد
🔹
کسانی که ایران و لبنان را از هم جدا می‌کنند اطلاعات تاریخی ندارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/657744" target="_blank">📅 21:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657742">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cX5nH2ugsNvFqTlYZP43ExtuFrW7NI7d286FFuUeMsImPaEKhaIgX5NQudUTPbh36tr8Qxan0eKySwxEUbKQN0i-zBMXuWjRtW_kyJPZbX6Et2z0tc5zP6JLMfv05M3UZ9aWO4DIJcGGce03fnbtC_cnd2Hhy4S2i35KlY9DZ2G0Tc-Jh3qiYuEHtXaZJztB2M0-6kVirS__DIXP-9IKDXAFGwo5OJvHGNEmzW4Ak4Pcn3tWvZpV2G_RFEkBOjM0xgEUrRaHtYfpFZaoUc5ioS7trkHb_BkcZL2zIYAs0IJ9EWyQpQd27zmzEv-UtWW0G4uDQ-fROolrGrAWERvx1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qWPUAJGKxRDP6xPCnIsEGh6ll_Di09tR48rchri-3gn1pIpN-OjMxXzsC70DUwcXjMq1U5nQ5zkKHqaP-xON3pOqiaJibnC0u0YCACOlhTMiJtUQBCbmWUJ2WVYwwvwYhtid9TynHcj5ICGFm3ZLwt7yL8Zy50GVLtdyFt4Wuo_M2cBMBUNliYtQFYnk1pEWJgQs4sLlLifip-X6i4RkcXOfUjvHLHuwy6f2hmkK-aQv23_0soy6AgypxbRDEEx_eW0dklL8XYsNqtSwfG9oer5GoeNlRHtrfcTMLMTEmk5seP_kU9o1tXlZYlxUc6t2wTERxkb7uhrmB-uXBxWbcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هشدار عراقچی نسبت به هرگونه خطای احتمالی دشمن در خلیج فارس، دیپلماسی را ترجیح می دهیم اما سخن گفتن به زبان های دیگر را نیز می دانیم
وزیر امور خارجه:
🔹
تنگه هرمز در آب‌های بین‌المللی قرار ندارد، بلکه میان ایران و عمان مشترک است و هزاران مایل از سواحل ایالات متحده فاصله دارد. مرزهای دریایی کاملاً روشن و بدون ابهام هستند.
🔹
نیروهای مسلح قدرتمند ما به‌طور مستمر در حالت آماده‌باش قرار دارند تا با هرگونه نقض حریم هوایی، زمینی یا دریایی ایران مقابله کنند.
🔹
نیروهای خارجی که در نزدیکی قلمرو ما قرار دارند، همواره در معرض خطر هستند؛ چه به‌سبب خطاهای انسانی خود، چه حوادث ساده، و چه احتمال گرفتار شدن در تبادل آتش.
🔹
برای کاهش این خطرات، بهترین راه آن است که نیروهای خارجی هرچه سریع‌تر این منطقه را ترک کنند؛ منطقه‌ای که هرگز پذیرای حضور دشمنان نخواهد بود.
🔹
ایران زبان دیپلماسی را ترجیح می‌دهد؛ با این حال، همان‌گونه که رزمندگان شجاع ما به جهانیان نشان داده‌اند، ما به زبان‌های دیگر نیز سخن گفتن را به‌خوبی می‌دانیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/657742" target="_blank">📅 21:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657739">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
چگونگی ترمیم نمره سوابق تحصیلی اعلام شد
‌
دبیرکل شورای عالی آموزش و پرورش:
🔹
از سال تحصیلی ۱۴۰۵ - ۱۴۰۴ ترمیم نمره برای اولین مرتبه به صورت تک درس و یا تمامی دروس مجاز است.
🔹
متقاضیان ترمیم مجدد نمرات دروس آزمون نهایی به شرط انتخاب تمامی دروس نهایی پایه مورد نظر می‌توانند بدون محدودیت دفعات نسبت به ترمیم نمرات آن پایه اقدام کنند.
🔹
نمرات اخذ شده در این آزمون ملاک محاسبه نمره کل سابقه تحصیلی خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/657739" target="_blank">📅 21:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657738">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rf8g5kdJ85a0AzNLgtdM-nUiyINq-KGYBbamjAphDCsOLiLZidciLcAITe9aBiOxWBXZl9jwec_MP_VpEKuu7aMCHfL7Ts6Hpia6TUhq8IsLCC9WsaTD5srDAo_Ym6MdngTEFTbceqMwCbW-JYvUycyt9O99Gd_f9P_UgY2boiivdYPs7RkRFll2dgw83NI1TtRlmu7SHaiNIfz3SXcS_mctJ7zotcojiv-qcTvM1WhXakrAM6XZAOoG6mUPAmJeQM8g6TUqErtNczvrGdgxk6ksVOK3keGo1Sa-RJBad33wYHXV3wuQlTzMEW0aCndVcm5TJR3eA_I5Ke_atNZvrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام تقدیر و تشکر دکتر محمد مخبر مشاور و دستیار مقام معظم رهبری از ملت ایران به مناسبت بیش از ۱۰۰ شب ایستادگی تاریخی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/657738" target="_blank">📅 21:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657737">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awUaRLR_QzhJpwB1vyjOi_fOP5qjbDlaJQDSt3VMQoc4h8DHZruNYxn8mB6VQ6Opfta1R58REVJWz0EBCL9sdAD4PerlF9PwluY809DOoPNmIKMIGOC9JvGTePxJq9ZfsGTYY7rnHJouoXRK4ict6DR1ptHFgkVfiMMlz6Aq1FZO9qiXrqMBSM23FlowgJed_A6kRwS8FnJLX1V0FYAvXU304Y_8AEB0goTF6TPZ7y3a6x0Xd4evPmb738duZlxMceDlzYxBYaqQ_C5BtVPxXtBMEEYHA11v-7H6AEr84lzHSPydQ_kHgSx80TaYs6QoNfPSiTX0YEVicARU2RZYqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هند از استارلینک به خاطر جنگ ایران ترسید
ایندیاتودی:
🔹
طبق گزارش‌ها، ورود استارلینک به هند با مانع مواجه شده است و سازمان‌های امنیتی به دلیل نگرانی‌های مرتبط با عملیات جهانی آن و استفاده گزارش‌ شده از پایانه‌های آن در طول جنگ ایران، مجوز نهایی را به حالت تعلیق درآورده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/657737" target="_blank">📅 21:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657736">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
کنسرسیوم رویه‌های استثنائات تجاری ایران: ممنوعیت واردات لوازم خانگی تورمی و قاچاق‌زا است
🔹
کنسرسیوم رویه‌های استثنائات تجاری ایران نسبت به مصوبه محدودکننده واردات یخچال، ماشین لباس‌شویی و ظرف‌شویی از مسیر رویه‌های استثنائات تجاری هشدار داد و آن را فاقد بررسی کارشناسی اقتصادی و اجتماعی کافی دانست.
🔹
به گفته این کنسرسیوم، انسداد این مسیر واردات نه تنها به افزایش فشار تورمی دامن زده، بلکه توان پاسخگویی به تقاضای بازار را مختل کرده و زمینه را برای گسترش قاچاق کالا فراهم آورده است. همچنین این تصمیم بدون بازنگری، باعث اختلال در ساختار رقابتی بازار، افزایش قیمت تمام‌شده کالا و آسیب به زنجیره تأمین و مصرف‌کنندگان شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/657736" target="_blank">📅 21:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657735">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
ادعای رسانه غربی: هواپیمای اماراتی دیروز ۳ میلیارد دلار پول برای ایران برد تا از جنگ جلوگیری کند ‌
🔹
رسانه اینتل‌واچ مدعی شده هواپیمایی که روز گذشته از ابوظبی به تهران آمد، حامل ۳ میلیارد دلار پول بوده که از امارات به تهران داده شده تا اعتماد ایران را جلب…</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/657735" target="_blank">📅 21:13 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
