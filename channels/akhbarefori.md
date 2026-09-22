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
<img src="https://cdn4.telesco.pe/file/FgUkLoYSNrrEMpnQmIh38a6wND7OXXNxnBcjHY1ff0ky9HFvZ3y6dXyrlKCI3Tcq5GX0KRumJZ1lpZcszQM9LrmfxJV23b4Q5Gp71IgGFhEFIDkx9Gv8FU7yqsOY5aUk0xgGP4mWhCUoMNwI4ex0GWowMTmEWPkmA3_-hTB0RyJDqD2jUAAHDkhxBhT7Zjyx8aNDhaVeq2UU54mMqSOWKg4_NF0o_v_2cD3otR4vU2bWR7guo1766zGr0iIg3Sxe5kwuf_VvAUeLvW1K2XBjGIRtoAPFWXAkaCANW6YlcesESPIz9WWJN3LRq-x5sJCoUpcNshNJtkFLARfacFnL9w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 13:38:24</div>
<hr>

<div class="tg-post" id="msg-691939">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
خبرگزاری کیودو به نقل از یک مقام ایرانی: ما احتمال دیدار بین روسای جمهور ایران و آمریکا را رد می‌کنیم، اما پیشرفت در جهت دستیابی به توافق امکان‌پذیر است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/akhbarefori/691939" target="_blank">📅 13:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691938">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
احتمال مجازی‌ شدن مدارس در برخی مناطق جنوبی کشور
وزیر آموزش‌وپرورش:
🔹
در کل کشور مدارس به‌ صورت حضوری فعالیت می‌کنند؛ ممکن است در بعضی نقاط، به‌ ویژه در حاشیهٔ خلیج‌فارس، مشکلاتی وجود داشته باشد که در این موارد استانداران تصمیم خواهند گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/akhbarefori/691938" target="_blank">📅 13:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691937">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bef0379982.mp4?token=J9447GZpZ5klQMlsFGW8-0xf7vNzBXcU1h3C06wzfw8OtmDfm4RdctFQ_0IBvng2PFUAAb7xIUMFnGimHsllangMblBBkhNnsyW5GItsSfO-EOFt7OfcMWotjLHLFJXuwFWUUAB4ynrAYOYeoihKwXVYBW61kXFjub4fWqUXKxDC9x9B8qjqVQhkZdgXXTi-vSTMmIOpbjM6Wx_aw-dyEaWpexsyCtf6P5sTp6K1KU4C7UoeRmFYDkl7VsfHwWyx-us8f8IB8Fbv-3pzm4x-vliF7nnICwgEXySoUS7iV_8keGVCMbtNWrnrPPLodObT1_Eu1sp4-F072sQd-WuarA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bef0379982.mp4?token=J9447GZpZ5klQMlsFGW8-0xf7vNzBXcU1h3C06wzfw8OtmDfm4RdctFQ_0IBvng2PFUAAb7xIUMFnGimHsllangMblBBkhNnsyW5GItsSfO-EOFt7OfcMWotjLHLFJXuwFWUUAB4ynrAYOYeoihKwXVYBW61kXFjub4fWqUXKxDC9x9B8qjqVQhkZdgXXTi-vSTMmIOpbjM6Wx_aw-dyEaWpexsyCtf6P5sTp6K1KU4C7UoeRmFYDkl7VsfHwWyx-us8f8IB8Fbv-3pzm4x-vliF7nnICwgEXySoUS7iV_8keGVCMbtNWrnrPPLodObT1_Eu1sp4-F072sQd-WuarA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با کمک این ترفند، در نور آفتاب عکس بگیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/akhbarefori/691937" target="_blank">📅 13:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691936">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
خبرگزاری کیودو به نقل از یک مقام ایرانی: ما احتمال دیدار بین روسای جمهور ایران و آمریکا را رد می‌کنیم، اما پیشرفت در جهت دستیابی به توافق امکان‌پذیر است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/akhbarefori/691936" target="_blank">📅 13:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691935">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWgd0koilSaG99M1Pbqsau6ijuCsKVo1LV7KoA3Ul1DQZ3zP1otv4jSCNxR2oXWL71RIp0Px13Z-dirD8dyX47XAEhI0c_0hFAWfq7oCzto5iXgyxDcHo76beeEI0TQlPxr92bpj8inGoQB14Hwrx0fiaP7IyR8eu4iJ8mflqN3ptk1LJ3Q-drLMg3HaHhbRg6N5ppg59ErVeYp7wNDwxPaC9R9PtnTnWwBQ8zWBUgoYI_0-nvbpkyI5xEdJE02wBzxzCFCD-WKfImL8kFEdm5yg7yqGPbTzGLPFtKGDRWOj56v1Er-LAsm6jPNjbCmP8bT_xVJngIvFUe2l4Vooew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۲۴ شهریور ۱۴۰۵؛ ساعت ۱۲:۴۵
🔹
اسکناس آمریکایی در جریان معاملات امروز روند صعودی داشت و به ۲۳۳ هزار تومان رسیده که حاکی از شدت گرفتن روند افزایش قیمت در بازار دارد/تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/691935" target="_blank">📅 13:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691934">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6093fc394c.mp4?token=bGMbezdxhmjZSxtAoZJo7oY90NEiNlWzVPKX-LWKwfZ2ohJcTTiBPjF-5lDouI8_iRvFoPV9-dQ93zTKujndfQ5Y5Usmi8H1QVJKSwI8kWT78bmjrEiyNF4v7kWCn1wdtP7_BM6BwmaL-QNwkYw8YRYQ2K38mXjowyKMHLFzvQTj5Ya7A7_WuuIfmWiH3XkuFjgzPb_2iZZWdUkedOrg04E1EYlJXoWe742_VyCIzPCERTWXfVeZa25rdMrs0PjRJZfbDXd8G4WUS_1N9EE0yWfOY5zvOdNzbGHcuzRZLGkv5nszknbdLbHQWHqhNf1UjhfQaKzN6wqBKV3N5dFW2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6093fc394c.mp4?token=bGMbezdxhmjZSxtAoZJo7oY90NEiNlWzVPKX-LWKwfZ2ohJcTTiBPjF-5lDouI8_iRvFoPV9-dQ93zTKujndfQ5Y5Usmi8H1QVJKSwI8kWT78bmjrEiyNF4v7kWCn1wdtP7_BM6BwmaL-QNwkYw8YRYQ2K38mXjowyKMHLFzvQTj5Ya7A7_WuuIfmWiH3XkuFjgzPb_2iZZWdUkedOrg04E1EYlJXoWe742_VyCIzPCERTWXfVeZa25rdMrs0PjRJZfbDXd8G4WUS_1N9EE0yWfOY5zvOdNzbGHcuzRZLGkv5nszknbdLbHQWHqhNf1UjhfQaKzN6wqBKV3N5dFW2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قطعات موشک به‌جا مانده از جنایت آمریکا در عروسی سیریک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/691934" target="_blank">📅 13:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691933">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
ادعای رسانه قطری: توقف پروازهای ماهان به ترکیه، عمان و گرجستان  العربی:
🔹
هواپیمایی ماهان پروازهای خود به استانبول و آنکارا را از امروز، ۲۱ سپتامبر، و پروازهای تهران–مسقط را از ۱۷ سپتامبر تا اطلاع ثانوی متوقف کرده است.
🔹
گزارش‌های جدید همچنین از توقف پروازهای…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/691933" target="_blank">📅 13:06 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691932">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رشیدی‌کوچی، نماینده سابق مجلس: بعد از ورود به مجلس، نگاهم به خیلی از مسائل دقیق‌تر و بازتر شد/ برخی می‌گویند امروز «کافر حربی» شده‌ام
جلال رشیدی کوچی، نماینده سابق مجلس در
#گفتگو
با خبرفوری:
🔹
در دوره نمایندگی‌ام صریح بودم که این بلا سرم آمد. در این شرایط مملکت کسانی که مسئولیت دارند در جایگاه سختی هستند.
🔹
در سپاه هم که بودم مواضعم همین بود؛ همان موقع هم با فیلترینگ مخالف بودم. اصلاح‌طلب یا اصول‌گرا نبودم و چیزی که به نظرم درست است، مطرح می‌کنم.
🔹
برای من همه موارد رد صلاحیت را زدند؛ عدم التزام عملی به اسلام، ولایت فقیه، قانون اساسی و جمهوری اسلامی. من از نظر برخی، آقای کافر حربی هستم.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/akhbarefori/691932" target="_blank">📅 13:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691930">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29c721b268.mp4?token=gaQsX6EPG67ts6NGIeZzRnFqFf6QNfC-BD5f8SccaSANpmwZC3zDhDBkx0NnIqgGm2DnabktsUPCxpaAXm4ABAm8YR9pNX8nqkqABH9gD9tumKguNDRDp3Wt6CwXFeiK1lgyby5V3C9aQUXg6KLufoSN4ySMghDQ4t3fUYaJKIKAY-mw_HeDtNEDKDQ7owNenpJYWr6jd3Is3y9EhVIU6Konc84rJZKg8i1D0HqRo-kBcDDtGZS1wAss_z6D0kzswwXuHPJfQwUD2ffXlg8PobXUNJfAuGmG5EQ4NXYJRijSCIa19jK8oKgjHKDH24U3YLGzIunsvQGUDvVtK2MNaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29c721b268.mp4?token=gaQsX6EPG67ts6NGIeZzRnFqFf6QNfC-BD5f8SccaSANpmwZC3zDhDBkx0NnIqgGm2DnabktsUPCxpaAXm4ABAm8YR9pNX8nqkqABH9gD9tumKguNDRDp3Wt6CwXFeiK1lgyby5V3C9aQUXg6KLufoSN4ySMghDQ4t3fUYaJKIKAY-mw_HeDtNEDKDQ7owNenpJYWr6jd3Is3y9EhVIU6Konc84rJZKg8i1D0HqRo-kBcDDtGZS1wAss_z6D0kzswwXuHPJfQwUD2ffXlg8PobXUNJfAuGmG5EQ4NXYJRijSCIa19jK8oKgjHKDH24U3YLGzIunsvQGUDvVtK2MNaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راز ارتباط احساسات و سلامت
🔹
قدردانی
فقط حال دل را خوب نمی‌کند؛ بدن را هم وارد حالت ترمیم می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/691930" target="_blank">📅 12:48 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691929">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
رئیس فدراسیون کشتی: حتی اگر به یک نفر ویزا ندهند، قطعا تیم کشتی را به آمریکا نمی‌بریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/691929" target="_blank">📅 12:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691927">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
سخنگوی سپاه: اگر مصلحت ملی ما ایجاب کند که در کنار جنگ، مذاکراتی انجام دهیم، باید مذاکره کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/691927" target="_blank">📅 12:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691926">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0508acf9c.mp4?token=YZ7tJJolgU5QUru455sJh5z15HOui9jC6ib8vpM5a0f71XFKgHhDyawxvTB_OQoK9UbiziQgrCz3io6JuN-ilUWb1VXCHqHrRM8MA7Lrh7fF2wH7l4p2pYhWIWaUu9BBqeZ3-FzvhwdTHxQ9MezS4d3YdPDcGiF-IdLN0ykS3H-z-8QTinX6ylhcZCBtXCVmMpxkvbDaCftz9sWQUEu2vBHRgmUnyWMznpUPx4tuIqoxkrx4PFJ4tMGrvUeXiRShcs5g6RcbDPag2pFvCoY8bFJSknxTqfC3gETCXzTiIY-epcR8KhF5wJhvhEGICHR2rdni0PTGY_T6wtBMVED8MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0508acf9c.mp4?token=YZ7tJJolgU5QUru455sJh5z15HOui9jC6ib8vpM5a0f71XFKgHhDyawxvTB_OQoK9UbiziQgrCz3io6JuN-ilUWb1VXCHqHrRM8MA7Lrh7fF2wH7l4p2pYhWIWaUu9BBqeZ3-FzvhwdTHxQ9MezS4d3YdPDcGiF-IdLN0ykS3H-z-8QTinX6ylhcZCBtXCVmMpxkvbDaCftz9sWQUEu2vBHRgmUnyWMznpUPx4tuIqoxkrx4PFJ4tMGrvUeXiRShcs5g6RcbDPag2pFvCoY8bFJSknxTqfC3gETCXzTiIY-epcR8KhF5wJhvhEGICHR2rdni0PTGY_T6wtBMVED8MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرقت تراکتور کشاورزی توسط نظامی صهیونیست در جنین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/691926" target="_blank">📅 12:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691925">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
معاون ترافیک شهرداری تهران: استفاده از سهمیهٔ ۲۰ روز تردد رایگان در طرح ترافیک از فردا تا پایان مهر ممنوع است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/691925" target="_blank">📅 12:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691924">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
خبر لغو پروازهای ترکیش ایرلاین به ایران تکذیب شد؛ ترکیش ایرلاین ۸ ماه است به ایران پرواز ندارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/691924" target="_blank">📅 12:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691923">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RiJ7UpwVYK-sYROIhvDd6q61ySyyfkXOuilFg6xWP6dBymrgE9sLaApasYuHMRuRdVqfQmLnH2ffpuK9b6IUt3EzJ2_NW54Ke5l6ZmYq_hoDAR798nWCroDMgsXF2nFLBAzf34YQA22KS_c0UIQz36QofNLAQIwMPXUGAgmK9uRVEwANdEnzo72zztnNb8LM5BOwS-03uvcYym4AfgXCRr2uAvTYFo4v2M0hcC5iRaCy827LO-kFd_f7PqvkWdov6KRtockONPXpIhKqwFKn2k4C5Boj6t_X3lnnxRscCPjpYsdw9UrsTs_HFgVutVIHvIP0Hze1nTT5jGA-J8iOFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آرکاری کاکل‌فرفری؛ پرنده‌ای با استایل عجیب!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/691923" target="_blank">📅 12:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691922">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
افزایش پرداخت حق‌التدریس معلمان
وزیر آموزش‌وپرورش:
🔹
میزان حق‌التدریس به حدود ۱۸۰ هزار تومان برای هر ساعت برای معلمان شاغل و حدود ۲۲۰ هزار تومان برای همکاران بازنشسته رسیده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/691922" target="_blank">📅 12:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691921">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
قالیباف: امروز با موشک‌هایمان بدون محدودیت، به هر هدفی که بخواهیم شلیک‌می‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/691921" target="_blank">📅 12:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691920">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
سخنگوی قوه‌قضائیه: کشتی یک سرمایه‌دار صهیونیست به‌منظور جبران خسارت‌های تجاوز آمریکایی-صهیونی توقیف شده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/691920" target="_blank">📅 12:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691919">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3A7gTGCYG0n40qsI3-bLaFUPI7trcvb55ThwxlY1tcUAh5la4gtSmi5V9n96OeaUdxvnekFqadoTu7vPKn0sV53_btH6ixXCRLsjdgG0Xh7zvZBZuecUfKkGqJq6COZJJQMNDIBOxqW3OJUoyoMeb1bOLTn8c6Hg54C33oAv-5hc3Gk0BmfBfo5_lp6bwVP8qsy7SqMisPW7bLKNBCZgHKATs0L8OokkknH59G_VE9sPbzxHt4VmW2gzXVMRb1Zq3CPze1VB5f0bGBgteh-3t1Gg7NWARMhdt5wBE9vd7LcQ--70f8PfRx0H5YFi_kRBBxmLc4Mxu_nryVr449StQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاسبی از شلوغی پمپ بنزین / ۳۰۰ هزار تومان بده نوبت بگیرم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/691919" target="_blank">📅 12:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691918">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
قانون جدید رضا گلزار در پانتولیگ؛ هیچ زن و شوهری نباید شب‌ها با قهر بخوابند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/691918" target="_blank">📅 12:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691917">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6354ee8937.mp4?token=Mkdiqn83uQMesr4oFl-I5aThrmjKqeJUWModpi2gQ82mlPzaG6nXPj_lXVDCTHYbzrAWCLCtnTaDfJnsTs5mKLxlbnQ2ASS2PJy1_g7fDbL59V8Apo88j_gXI_aFaC4NvMbIWvfTtOVNhQjQciowTp6rjrKCRs2s6c-QK-L8mxvz1FIO0TYRNcLH8cEYt8zzTtYsozum_2dTgfNbFHpreOXse1UXBuzZpwOA3-6RV8EQRTsviUsEscF1zgVt5rVRLRQ_Bf432lX3Ergc4LmhQEF_ps6x_S5XWutVryxUp-VW0eb_nEUe5cj3igRbBDgR_GiOcle6Rd2yZcalEp1VgyztgYOKumb0ysBMtgPh8RWk0XNZvIdpttb8LDoH-bWo-W6_wi0Ci5cU8_svAJI29MY68ZEJ8_p5_D4GFWHL6cbcAOnF_Ht1yg4HUJuvmrKyJWa97G-6PdnAZF2RyNcmdYY_toZo7KN7TSToV3YQpGqbd-vJNDvGgIOnF2JGq7cAnk5BH_TQg9VwlluUXJBcK7ae110OTJrfH4eFu0K0SA3mPxeI7xgd3O2zV3z8OeYYgIKoN5w8Bl05KQQ-Jj1zbuvfK5RhpuecmnKp_yVVw8cbJUeSnkUeG7or9Vwl5JsqwFSsCNRsaSuqK_GqIin71Q3Az2A2caZ6tlQbJ6ou2ZI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6354ee8937.mp4?token=Mkdiqn83uQMesr4oFl-I5aThrmjKqeJUWModpi2gQ82mlPzaG6nXPj_lXVDCTHYbzrAWCLCtnTaDfJnsTs5mKLxlbnQ2ASS2PJy1_g7fDbL59V8Apo88j_gXI_aFaC4NvMbIWvfTtOVNhQjQciowTp6rjrKCRs2s6c-QK-L8mxvz1FIO0TYRNcLH8cEYt8zzTtYsozum_2dTgfNbFHpreOXse1UXBuzZpwOA3-6RV8EQRTsviUsEscF1zgVt5rVRLRQ_Bf432lX3Ergc4LmhQEF_ps6x_S5XWutVryxUp-VW0eb_nEUe5cj3igRbBDgR_GiOcle6Rd2yZcalEp1VgyztgYOKumb0ysBMtgPh8RWk0XNZvIdpttb8LDoH-bWo-W6_wi0Ci5cU8_svAJI29MY68ZEJ8_p5_D4GFWHL6cbcAOnF_Ht1yg4HUJuvmrKyJWa97G-6PdnAZF2RyNcmdYY_toZo7KN7TSToV3YQpGqbd-vJNDvGgIOnF2JGq7cAnk5BH_TQg9VwlluUXJBcK7ae110OTJrfH4eFu0K0SA3mPxeI7xgd3O2zV3z8OeYYgIKoN5w8Bl05KQQ-Jj1zbuvfK5RhpuecmnKp_yVVw8cbJUeSnkUeG7or9Vwl5JsqwFSsCNRsaSuqK_GqIin71Q3Az2A2caZ6tlQbJ6ou2ZI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک کشاورز خوش ذوق ایرانی  ۲۴ میوه مختلف را با یک درخت پیوند زده و اسم این درخت ۵۰ ساله رو دوستی گذاشته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/691917" target="_blank">📅 11:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691916">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LurXYw-j4-Z9eMZ44wI-JZ3EMBa9i_s3RW-Qi6VngFGyPdSxLe1wrH1sKFB6mAcl8PuBGWd0MOMwotBdNt40GobBmg3BGiJzJebFXSJjltE12UOwxoHuY6x7NjNfi-zkugwWteWRtzB-2fBEB_vVdTmv72shKBdc5LHgRyf9MBmDc4VkN-0MStny3Ec7TVyXe5Iwea4j0ilorjCJTKcQXvy8vh6bR19kGQfz1SJDo3SwL-Fh82vdauP-dn94puMi5a2N70NYD8A0z_9uLrIo1cmmF8bqSQBh_4reFOg73qxgZBPpU5ACH45VdaF16GTC2FJPxdgi_nR8MRLFrw2MtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نعمتی طلایی شد
🔹
مرتضی نعمتی در وزن ۷۵- مقابل داود نزمیرادوف از ترکمنستان با نتیجه ۴ بر ۳ پیروز و اولین طلایی بازی‌های آسیایی شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/691916" target="_blank">📅 11:51 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691915">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
اردوغان خواستار لغو حق وتو در شورای امنیت سازمان ملل شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/691915" target="_blank">📅 11:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691913">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2849bc42a9.mp4?token=WVzf8mH9_JQOOgK1KsnPT6jMfS5YBUEMCRO9ZfrGqQMtdyk5YkXjzU9BdPazMq39kuwLdS6s5aPSc4XF5w9U9XaXNyfKB3BoiOcVfSr8TPSI74xD8HWR4Gv5HqpBTKSFVg3au1WZxd7dJJ5c29tsCirkKGgldy8lVehj82A-9k8eNbP5RnL7fBb98bNaUPuDU5WavdjVAehfg_HMaqZ-2NmLjSi-CMqYjbc5ZoR9bPiaVMh5-g5KacM6FTC8Y7SPzyS6SP7NeTCcAbdJ7pml_zZhyLQbIbKEcLutiScN-IRosP1RRHZi_c2F8eJm35jUpOWXlt1Wv9LhFixPr_BZLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2849bc42a9.mp4?token=WVzf8mH9_JQOOgK1KsnPT6jMfS5YBUEMCRO9ZfrGqQMtdyk5YkXjzU9BdPazMq39kuwLdS6s5aPSc4XF5w9U9XaXNyfKB3BoiOcVfSr8TPSI74xD8HWR4Gv5HqpBTKSFVg3au1WZxd7dJJ5c29tsCirkKGgldy8lVehj82A-9k8eNbP5RnL7fBb98bNaUPuDU5WavdjVAehfg_HMaqZ-2NmLjSi-CMqYjbc5ZoR9bPiaVMh5-g5KacM6FTC8Y7SPzyS6SP7NeTCcAbdJ7pml_zZhyLQbIbKEcLutiScN-IRosP1RRHZi_c2F8eJm35jUpOWXlt1Wv9LhFixPr_BZLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون وزیر گردشگری: پزشکیان در سفر به هند با هواپیمای اختصاصی خود، ۱۰ تن مواد اولیه دارویی برای کشور آورد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/691913" target="_blank">📅 11:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691912">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
سخنگوی سپاه: مذاکره به معنای سازش و صلح نیست؛ بلکه صحنه دیگری از جنگ است
🔹
اگر مصالح ملی ما در این است که در کنار جنگ، مذاکره هم داشته باشیم، باید مذاکره کنیم. آمادگی صددرصدی برای جنگ، به معنای نفی مذاکره نیست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/691912" target="_blank">📅 11:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691911">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8205dc702.mp4?token=a2U5-5kpAzfeLZoWKk8jY-J286smTCkDN9u7VYtB50txcoM7wfnZWa1ZsXyHz4jjY9zZikdhPk9Wrb48zRPTQdLmj3QNvGuWHu2mCGuod8iqNBYZN5qzuHUrBZ0jNGrL9GIQFTE9guY_Ob7S7RA8gr3OFBuATO1ICTEdhh6-kEPRfvkCFMD6YsLuP3DZAdfa6zOrWuHJKUJnZOEt-mUWgJ4IYgkcES-rt8cFcktEMOE5n64l_l2ZmxMYX8Agk800kZvwIKNUtQ1LIs1X2KOrsm4axw_c8IZPmDNId86BZR5yPwS_ZaT4lATiARzYs1MH9sFiVHFo2r4AmHtUblCuaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8205dc702.mp4?token=a2U5-5kpAzfeLZoWKk8jY-J286smTCkDN9u7VYtB50txcoM7wfnZWa1ZsXyHz4jjY9zZikdhPk9Wrb48zRPTQdLmj3QNvGuWHu2mCGuod8iqNBYZN5qzuHUrBZ0jNGrL9GIQFTE9guY_Ob7S7RA8gr3OFBuATO1ICTEdhh6-kEPRfvkCFMD6YsLuP3DZAdfa6zOrWuHJKUJnZOEt-mUWgJ4IYgkcES-rt8cFcktEMOE5n64l_l2ZmxMYX8Agk800kZvwIKNUtQ1LIs1X2KOrsm4axw_c8IZPmDNId86BZR5yPwS_ZaT4lATiARzYs1MH9sFiVHFo2r4AmHtUblCuaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غمگین‌ترین زنگ مدرسه دنیا به صدا درآمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/691911" target="_blank">📅 11:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691910">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFjsx31liqXYtMI1E1ua1lQv1dLE9vKzoY6X_kcxDkBnNxnGbKJf6Y6y8tcAfhyDF5RvVl4ISs4wp-AxQRwjwGjydn3ba2cNDzd7RdBvEzknVyBlrLNvNlaJmGkNK06A3uyyyuBojn_ofWNw4MaQMOhLIX-50LHZUgDS6GIVVNmZKSsdVuOA8zI83xZdWtD-FkUZ5Q-b4DVojGl7L9YPOtV4KiG_0Pa0v4dLE67WAxC6L2L12xwWniPR9ePM4dXKULGPpSP4DezIBVAxUD-xgTyC82UunR_pLPxHo1cFr1fVo0kFFZsO_cAscH7tXOijOSm8JVKzhJ5Auq98UUD5Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
پک_سوغات مشهدالرضا
🎁
مجموعه‌ای دلنشین از یادگارهای معنوی حرم امام مهربانی‌ها؛ هدیه‌ای ارزشمند برای عزیزانی که دلشان هوای مشهدالرضا دارد.
✨
مشخصات محصول:
▫️
قطعه فرش متبرک حرم رضوی
▫️
عطر خالص حرم رضوی
▫️
تسبیح ۳۳ دانه فیروزه‌ای
▫️
مهر تربت مشهدالرضا
💰
قیمت اصلی: ۱٬۳۹۷ هزارتومان
🔥
قیمت با تخفیف ویژه: ۱٬۱۹۰ هزارتومان
⏳
موجودی محدود؛ برای ثبت سفارش، همین حالا اقدام کنید.
📩
سفارش:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/691910" target="_blank">📅 11:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691909">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ba18746ff.mp4?token=n6-8Dm3mf6rDlSy5OvwSCjv7nFO9WVlmB5pDZsgqy5S2oWEyDeu8R6EcEPlX8ZdNFJkqgYzSVKfwkRDx-OOzhzNlbsZoOaMqS9fWb-BuEjFJgTUtO3q2UIQx_D7OttnAKXMqJkLchLxnHt1jvUyKK7xMvC2Vl6-4Boewbnu6Zrk5tr7JaE4xuPibdg7HMptrGccZUG2z1v8hz_pRIz24b04ZPFOW8b8aDD83uOGJ0xK6b6rP3dpMVSdTrPC1PcAmgpdJ3Lp-fxKB9hePTVMI4NUfa5pILiX5JI6on2vP04ROvtPYoaLyJy9b5NfCBmJe6VYOCbmQF000-eoGVmH-0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ba18746ff.mp4?token=n6-8Dm3mf6rDlSy5OvwSCjv7nFO9WVlmB5pDZsgqy5S2oWEyDeu8R6EcEPlX8ZdNFJkqgYzSVKfwkRDx-OOzhzNlbsZoOaMqS9fWb-BuEjFJgTUtO3q2UIQx_D7OttnAKXMqJkLchLxnHt1jvUyKK7xMvC2Vl6-4Boewbnu6Zrk5tr7JaE4xuPibdg7HMptrGccZUG2z1v8hz_pRIz24b04ZPFOW8b8aDD83uOGJ0xK6b6rP3dpMVSdTrPC1PcAmgpdJ3Lp-fxKB9hePTVMI4NUfa5pILiX5JI6on2vP04ROvtPYoaLyJy9b5NfCBmJe6VYOCbmQF000-eoGVmH-0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی از لحظه‌ سرقت موبایل یک پاکبان در مشهد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/691909" target="_blank">📅 11:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691908">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
دادستان تهران: با شناسایی حساب‌های بانکی و خودرو‌های متعلق به ۳۹۴ تن از عوامل ضدانقلاب، بخشی از اموال آنها توقیف شد
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/691908" target="_blank">📅 11:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691907">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJWLypyDf2hJS-yWuoXhoGn2Y070cooJbtimZGwDhsp-HFigVKz79uucWgbiZo4TQDaZSEXgcEz-z4ZCalbFeBvECXz90c3HJ6gWNzbCqrVxn33AuhSD7rpxYSwjWdKXlWj9wwO9oNNJIv8t9gbF-DWaUfPKVIrN6WYpQ70-wacCwe2fiRJszIAI05_PeTbmXpBBOFxXOLlSuHzIRbRqEgjBsRtlRti9jPm4196OQErKmpoJgWSuLZCznh0nSEL9mZ5z8O89Me7WQoqVeC306_pZP3cto6MiAS7-iRhqofFxYqwZi89DZGAKBOCfmvSIeLzSKs7hdJhdPJUN_9CBOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حامیان فلسطین در سائوپائولوی برزیل، تابلوی خیابانی را که «دولت اسرائیل» نام داشت، با عبارت «فلسطین آزاد؛ از رود تا دریا» پوشاندند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/691907" target="_blank">📅 11:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691906">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
ثابتی عضو هیئت نظارت بر مطبوعات شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/691906" target="_blank">📅 11:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691905">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
سخنگوی سپاه: مذاکره به معنای سازش و صلح نیست؛ بلکه صحنه دیگری از جنگ است
🔹
اگر مصالح ملی ما در این است که در کنار جنگ، مذاکره هم داشته باشیم، باید مذاکره کنیم. آمادگی صددرصدی برای جنگ، به معنای نفی مذاکره نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/691905" target="_blank">📅 11:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691904">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/189a5c88d1.mp4?token=XCEgT1zf46UaL6mx0d5ipxNTpOw24o9cQP7wjR1JesP5AKv6DSw6fYqNbjaRhiYekNl2ccqRIFwwmDOiVDcDKINSaM5hXMmUFWNRaoB4qiLHaOte7W6egdZWqKr_VS86XAXatGr0pmARVGb6uv2aIzeGOz0RfM1JaHsiKobK9OdlojeLOLo9z3nIDxSQ_gPPmWIJ6PsDz3uaPiFjDLvpNox3V7xaYt-2RS1qrUkB9s2-ogdm8Yml7y_gHNnfATr9e0goLkfHjAxg9kWZ8z_YvyTFV_qV0dXS5NGo5-JXqIYgQER4Apql40CDezv72jR83hr8NNOcF28lU6G50qa_TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/189a5c88d1.mp4?token=XCEgT1zf46UaL6mx0d5ipxNTpOw24o9cQP7wjR1JesP5AKv6DSw6fYqNbjaRhiYekNl2ccqRIFwwmDOiVDcDKINSaM5hXMmUFWNRaoB4qiLHaOte7W6egdZWqKr_VS86XAXatGr0pmARVGb6uv2aIzeGOz0RfM1JaHsiKobK9OdlojeLOLo9z3nIDxSQ_gPPmWIJ6PsDz3uaPiFjDLvpNox3V7xaYt-2RS1qrUkB9s2-ogdm8Yml7y_gHNnfATr9e0goLkfHjAxg9kWZ8z_YvyTFV_qV0dXS5NGo5-JXqIYgQER4Apql40CDezv72jR83hr8NNOcF28lU6G50qa_TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پایان باز به سبک اصغر فرهادی!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/691904" target="_blank">📅 11:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691903">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84c2fcba08.mp4?token=E9SJ3ezd8cutqOhkfeKnwBE8mQc2C6VF5Ori7a7578LFL_2HbgX4N-BsQauIu566Q42kDceY-GBL1QosdrJ0xbeaYjkLzR17yBRjyjlDD3I2MfYZbAevwJ2ee_XDduKdfIkNyJqJ2PNHBb0EiLrpKi-pEhdZ6XmlPplahTdTaiziP8mZ-rSjQs1IPUPP-olfV-uMoCywzqpQQX-uZrZz-zblAV1ii7T_lABpjid7vVW9zG2yasHiU8TxM5hh0EVpVwfSsIpmhm03DrVs_dl1pr1fKr-tIG6ueHT-EVlL9s_F4nswDHg_AMWag2EWq_NaQ-H-L98tJGiQ3MGXmKF5WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84c2fcba08.mp4?token=E9SJ3ezd8cutqOhkfeKnwBE8mQc2C6VF5Ori7a7578LFL_2HbgX4N-BsQauIu566Q42kDceY-GBL1QosdrJ0xbeaYjkLzR17yBRjyjlDD3I2MfYZbAevwJ2ee_XDduKdfIkNyJqJ2PNHBb0EiLrpKi-pEhdZ6XmlPplahTdTaiziP8mZ-rSjQs1IPUPP-olfV-uMoCywzqpQQX-uZrZz-zblAV1ii7T_lABpjid7vVW9zG2yasHiU8TxM5hh0EVpVwfSsIpmhm03DrVs_dl1pr1fKr-tIG6ueHT-EVlL9s_F4nswDHg_AMWag2EWq_NaQ-H-L98tJGiQ3MGXmKF5WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون وزیر گردشگری: پزشکیان در سفر به هند با هواپیمای اختصاصی خود، ۱۰ تن مواد اولیه دارویی برای کشور آورد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/691903" target="_blank">📅 11:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691902">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
ادعای
نماینده آمریکا در سازمان‌ملل: تلفات غیرنظامی در درگیری‌ها عمدی نیست و ممکن است به‌صورت جانبی رخ دهد؛ پنتاگون همچنان در حال بررسی برخی موارد است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/691902" target="_blank">📅 11:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691901">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
چین: با تحریم‌های آمریکا علیه شرکت‌های هواپیمایی ایران مخالفت کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/691901" target="_blank">📅 11:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691900">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
بیانیه ضد ایرانی گروه ۷: اقدامات ايران که قابل اعتراض هستند، یک الگوی خطرناک از تشدید تنش را نشان می‌دهند و هشداری برای وخیم‌تر شدن بیشتر درگیری‌ها هستند  گروه هفت:
🔹
اقدامات ايران تهدیدی برای تضعیف تجارت بین‌المللی و ایجاد بی‌ثباتی اقتصادی جهانی است
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/691900" target="_blank">📅 11:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691899">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/837e110056.mp4?token=OC3PlL8Rfc-hkBWb4db75HArRF0RWlX8QgL0idJ52n7ff3FbfYRrVgcCITIGL4TxvbuJ5ARbTXBU4ASOdobKWAw4yhk4bJZlX4mfLpxFOmNPWardyPZlu_V6ufaI73UbhajibzbWXN8pCkIlRSQJ9rSXsM2W2xAKFma8fnLt1pCTqE3h9tPV5RuCbuakFMokKQ6i_D0wlRPelImj9BG434lfxXbB5gt_FVIwnCbP5cbK7sz5DsyL9HFLIoEFbO5rCBukYExu1D0LC8axwz5HJPFYWMPDAqgh_c9thrdV8xtYce3hiz9UDTzHzqpwgCkivBULioG1Zceq9xk6j-NVRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/837e110056.mp4?token=OC3PlL8Rfc-hkBWb4db75HArRF0RWlX8QgL0idJ52n7ff3FbfYRrVgcCITIGL4TxvbuJ5ARbTXBU4ASOdobKWAw4yhk4bJZlX4mfLpxFOmNPWardyPZlu_V6ufaI73UbhajibzbWXN8pCkIlRSQJ9rSXsM2W2xAKFma8fnLt1pCTqE3h9tPV5RuCbuakFMokKQ6i_D0wlRPelImj9BG434lfxXbB5gt_FVIwnCbP5cbK7sz5DsyL9HFLIoEFbO5rCBukYExu1D0LC8axwz5HJPFYWMPDAqgh_c9thrdV8xtYce3hiz9UDTzHzqpwgCkivBULioG1Zceq9xk6j-NVRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">​
♦️
صحبت های مستانه مهاجر درباره جدایی از پژمان بازغی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/691899" target="_blank">📅 10:48 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691895">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FTsHIw-17fkZmmaqEjboT0Y3DmzAmIeMsRrOfnVBFr3sOCxhlhhYIZHg3BFDJkeLHHzzvEf4c7yeFg03MCaxb6lUTNxhdGf7Zoaq24ShodtFrQZX_mahtBdTmfPUcyG1O0k5vUaZNWHPbJdqH-1y_g5osXWFgnNsxrKHMpXRkgfBuVmWFlt6xshbC19jAXHowP8DGXlxz-l95Jp9YEWmJBl9-ESLt642YTIEU6QFlikIGXMcPyZiwaiVt3uUVLAXm0kk4fGuO-_wpKgDmLE7MWhyYIh-fGX8WVP5sp9CE2bGglFoiuyLm-iEax0cosau0W5OUI9mOAqzi6G6N4PdTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tylj3miEqA3Io14g3jY1wMZnQGClpCsfFBNSIj9dPSwo_Bev26cNsWdZoVw-EMXkx0d5GOuIJpN9tSmiqQR-Qv6qXFBqSXG90ncKZ0fslTyiURXDEOXefe9__gSvOiDIA6KAQu1FR7w37cQQZF-3FLWRNEhmWRo5o0PJNgXNM2gNepvApst_eZ8JOG0x8YwUnd-Gfqaz3_bYCRzc6_DdtrhSmOGNtLD2516jtoJPlwmWwV7hJ6aSegl4Mnlp6YL5vKFofu7npO4ygnIZNWrfFHa5LuUeb11aT6u-j3qYmsgKWMHyJEC14ARMo47CRuYnYqL2EOwbhTDRXd_BAGk2Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A-8CGyxBTQw9lSka0dl89gJTgH3gz65Q-yp_HbHkLwNrLmnyQiagk9kRQMIWu0JgqBg-GaI5jNpQDIcKiei_2uXKwUcyhCIBx4mBr2iWXxBIH2Q-bqbD55qEBhLJGt3q-Tf_CXVgRSTha8V71eO88jNCulwvWdmw3aSEQpDZ3_Mhk5qbKq3PSH2CH2fO8ep8R1HrYb5C07u8EdBt48vWa0yqgb1K6ZDJwuAJe9iuJDtFjdaGrURsqZUmtBGjIut2sRbxLsHebjwTDI2j-gr8vBOuiLz2inQ_Y2GGkJPV2sTAQrNLEDIL2N3BE6Z-RXtaAuI5rdjfQHxlGXfdaPftkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصویری دردناک از آثار بمباران آمریکایی روی صورت دانش‌آموز میناب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/691895" target="_blank">📅 10:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691894">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
پزشکیان: دشمن در به زانو درآوردن ما از طریق نظامی ناکام مانده است، بنابراین به مسدود کردن مسیرهای هوایی و زمینی به روی ما روی آورده است
پزشکیان:
🔹
دشمن در تلاش است تا تمام راه‌ها را بر ایران ببندد تا این کشور را وادار به تسلیم کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/691894" target="_blank">📅 10:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691893">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
ساعت رسمی کشور در پایان شهریور ۱۴۰۵ جابه‌جا نمی‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/691893" target="_blank">📅 10:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691884">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vyJKEBGUprN4nY42kKsqCZjq7YQvGnLDZczXypRFT9N0KrXGUTEpa412V7rAdDh6T4qkqMgqepv-cll5tgPikzR9WrJfEhyBreCbGReAAtDTw501JcWTh9rgU8z-1qqhB7QHEyGmAYquInW9UsutfR1mfTsM4g4mRz6LDCJk0RKArOBVgUY9GswJ1z-xf18wxgVVzEVmtJPCsySKPgn5TQjmKuG77FaEbhLaD10Rpk80R6sOalv_0lTGL5lShJSi8C7Xqt18zhDaDvvqFRjckBXbboKC5a4bDMbNYSvtU4BVDQq55_laOKJCpflYBsuPftmUk3BbKhq7WZ57BoveSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qH7RhxH1sxAdWjUPVGfK6gwwBDjNneHtzPCgmCEc_gw7p_H1Qg-flPTxHr2PoudU84Skh3IcY84k854WWmVV6eK-ZL3tEqUcDI2p4L_AGyQt4sMxAMPwL_RJ3RDZ676RBKEkbbnqi0iLzvlrjjlGysCjElPW8QHdDvcoetDJNLCa9Pr7Ymkg4Uf-KguERz0j7tVW9Tgq-7G4-w7HCwylPOVzBfbWClr1QFYKLcRvHorSoGp7wS6qJYM4KsyJC3h0RvTtq0UMaStrKy-s_0MrWTpDnlnwK2B-LRXqqULCujSxYxP25SOqGq1Ikomec869-zQnoY966Pv_8J5cF913_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bnFxmMLDs8Zc81KZerJNEtIaDXWl4qUwX0wZdnc6tBZerVgiQiwfNFsNtx2vzICrLAI-IfFmNadJ2PqoJuV7zR_EyyXSSz5vIrYPmX166QweuaiApeBcn-8oKhHltAXBrInY-sZG3nhg_RWMfynNy2v_xGHrKXTeJTaS3RBzK-S2X6cijea3zfTduWCa5tT-7X3q4NGTvL7Ts6fdl-pCAEZsE4e9lDK_7hEVzUXwd2F2_Rt-Z34GC9OiifDrwKASH-yKE3Sd5wZy2ntF3Lvicawu4yDwrKOunkJZ3gFB2aOlJvLeyCOceiZ5kNtR0SxMlacrVWj20mxO4PdHeUMKnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/X-lo_hvWFR8LPxd6fzSDbzq9be4__yUzIT9PDjw9_5xiMEJEFoP6UgJZhSA1o0VThfxDBBrbXVgqz-W0TrbYFHa-5A1zI5lH-pEQG4GIZYNNw7qvoojyjjBwTW5rqzBXzcZZhkCKHiaEkm9D49loMWG5xfHZuktUUNw09dtzu2qBlrNqabMCGCfVxEivcP8s8WbuxJTtmR4rSi_9D-jUhYYGxYW3M-ErR-67KIKRbCJHaM171GJGaKAGwzGAp83XMmDShS-_K_Rc8VCu80selU08b8FNptIzC-yT0csAlb3oaxa2fvqzeIGijQh9InguyjHaOZlHc3mBbXz_VjPCww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/B8QejVGbDF0CsiWM7tQfjXJoqxZJtmaRMO0KfLiVTNpsVKHNNAqE7Kw_dhWRmwSMYdT7-ASqHJCJjJQpYltowTnWgpwvWPOensAdkZLLwObBm9dMHI-LVERcO6ZlCyxDWrcEzKRWZHZk28-44zv4q3LlUkmjYX9yc0zu6Mo5d0qYXIXT0qeWlXoOOmEoNuhDYZCG7bEZH_5anWjrdRiAuRK0F9J6_C-nZlCFLw5Nu1-HzR03L_-iagHYB8RL19c6ocg6aIctXwXGiglcwHM8zIawv82J_hfSYAD7MkzclR_p5bIwcinNsaTSNOW-ybdBwmkZek_Oot7mtNcbUkIcmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JbGfiNwL_mjOXsITCXEBHTJWtlM5uVcAvhR2rthqk7SHI7RuKB5aoWP8gzzANtXdIGQKOj_HH2zp5p2aAo36Urb9qKIGqoY6b_paqKsQMk0U9Fex9iNXEkqDepPvIpvP4fOQbeTZmw2t_qTJOMxfH-AlquhK-5138LRkKviHzfNGVVW3vwhMM8ar3qhbh-X_7iE6q_89DcUu9vYVO8uIcGlY-cbF0FfCxpbgOxqdPm_08fn0NNFNT20ePuyEek7lAuD2EsAHTO_NEV8Cnyn2-5mDVBSWaeo7q9jd2U_IYwW6Zp4lQWdpepACy18-Te578MrZk4G4pbkigNhOqNHI2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Zfd3ZvK0I1bTPHbhk8T9RJ3DWVs7mkeQi4AZ6QAGZ_6QmwuQOhyYSJqPubzXSuNCmzKE3XyVHFEZdFi7RtYSfRbQ7J1Rje3elfTptJKfD0iWX9ENjI2Hx1EhLLuw9xA5-iLKjBzdxGWHKuEaiIq1DiGhhdDCXh-9uDRxjmB6Ycmm6x0e_xYRVC190YjgB0Czytd2TB1-TRoXKdCJ3AOExmiutSFTABvicHWpve04BIkVH48xzASHz6AOHxzHAmkdQQq2MHiJk1b3ghtmKVkx2CHf3TTPFiEWIHZzD_s6IpHQxjyQ8IeholaNibdjl0OOzHRtQ69CWhgemQEhqdTBUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/g1OcXlrQTrWg98xVFQBVY1AJ-v2VkQf1zQzoYn7oOROTYW1XgvRUa5kTElXolrQ-iNlN7QJqVFF02Pz8bZzlyMKRTllkASgWuh6jSLko3e5MzXiuMQNwgkeo3NhH3V1Vm0dhy7Z4BNtHbqH6Fi7ghcToNLENY2UjlNGPT6849JEOWMcrr5ibVt_VoOzk1675d_5X3Tqm6mKKKvzryeJWBppf-oC7sgU8iTcoOHzY77o0QwNehPcCIcQhx6SC3Lsvon5TpXMppNuw2LP2W2BaDbXgtFDFD5AmxE4O6YrfPwjkdUv-PZexQ6z_SFj780m8_5bAP_EyPAHVRfJV5y04Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jKPvsjgL55N40EUNCyHoHTOK7A_L3zKHffyc7BR_boJOF0kPV4bbAykPMWWfUQfwEoGnrpskvNtqFiYeM6g1WCHQ5Mi9hJI2vK5w5cq48uCjWLQjINPY0lT4Nz3KrL67V2fKwQp08QUh7yxqOW7FlKK7hFy2oCJuYIALb1jgH8kxU_1gaHmTTyz2z2YEhBF0bbAmZii5g9e8FtefcBbVGxE4asXmybAwcaRF2WhXN3zBbHSRoJ1Ae1EP4Et2CfC16_fX78ihNX98EfYoZp_fCcR8gYUbWZRopwLegGK6KSp9x2fa7g1zak4X0TDE7y8vW0-chbTkhfCbkntVVRn12g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
برای سلامتی هر قسمت از بدنمان چی بخوریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/691884" target="_blank">📅 10:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691883">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3dfa4e80d.mp4?token=L69yc_VVugj-DCOFQa_ndw48saIn6eOU_NzzRN4AdKwZCgAmTuQI26QN4z0uX-Ak_jpL8rq9mM93wP2jSJ-CstLpu6SgzWE3DWWOCm3acdtFdundAwufHn7pVBjl0-ITgr3hogzGMutoD7EBu8ufzqc832AwTtmUiAPCrN6G0bJAHI3k584E61nPVI-XY4kS7AUmMPUU1m4FMEM5i-1uwfpI7XK_M4mKpT2IrImBVcJB_NVILzB4gl6-IgzY2WLjVnwENzbOY0rpSfN3Um65Uld8Ift79CVTJdZVFZLlU3DQZ_w9_BT5SNgj3t8_j70glDcHByGtkqC1DxcZrDEa9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3dfa4e80d.mp4?token=L69yc_VVugj-DCOFQa_ndw48saIn6eOU_NzzRN4AdKwZCgAmTuQI26QN4z0uX-Ak_jpL8rq9mM93wP2jSJ-CstLpu6SgzWE3DWWOCm3acdtFdundAwufHn7pVBjl0-ITgr3hogzGMutoD7EBu8ufzqc832AwTtmUiAPCrN6G0bJAHI3k584E61nPVI-XY4kS7AUmMPUU1m4FMEM5i-1uwfpI7XK_M4mKpT2IrImBVcJB_NVILzB4gl6-IgzY2WLjVnwENzbOY0rpSfN3Um65Uld8Ift79CVTJdZVFZLlU3DQZ_w9_BT5SNgj3t8_j70glDcHByGtkqC1DxcZrDEa9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باورت میشه اینا دورهم جمع شدن؟!
@Tv_Fori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/691883" target="_blank">📅 10:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691881">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b64d4fdbc.mp4?token=dGJrJaPKsBeIXn64DLfjgJH-6YeMYpElqqC40wMZj2Pa_PWFCdN3GaLR0Yo0H8QhgGDdhNsxSwZwJ8FcEWQGYBnlaF70wFXf3Xx7P1oqnJ-xhCMaXqDiV4SgbQ8bbsgzUP84TuJUIJrgZ2lW5NpOol8VninqUioMjClzZBd1hfAOgRsMjZerdkzy-vpOWe0UbHuffty65pHLi-ZlWdIzacCB8iKskoNopvv47mccqp6eHk8zt_YpSGc3jv5VDbjiqpwrOzXKb73p_sZJnOgmSal8x82H4uoaV8Pp0OMUoNDfvOfxMWmSExlrUVJic3hnqh1r-g0DkWcS6hTHL6-ZHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b64d4fdbc.mp4?token=dGJrJaPKsBeIXn64DLfjgJH-6YeMYpElqqC40wMZj2Pa_PWFCdN3GaLR0Yo0H8QhgGDdhNsxSwZwJ8FcEWQGYBnlaF70wFXf3Xx7P1oqnJ-xhCMaXqDiV4SgbQ8bbsgzUP84TuJUIJrgZ2lW5NpOol8VninqUioMjClzZBd1hfAOgRsMjZerdkzy-vpOWe0UbHuffty65pHLi-ZlWdIzacCB8iKskoNopvv47mccqp6eHk8zt_YpSGc3jv5VDbjiqpwrOzXKb73p_sZJnOgmSal8x82H4uoaV8Pp0OMUoNDfvOfxMWmSExlrUVJic3hnqh1r-g0DkWcS6hTHL6-ZHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیروس ابراهیم زاده درگذشت
🔹
«سیروس ابراهیم زاده» بازیگر پیشکسوت سینما و تئاتر پس از تحمل یک دوره بیماری دور از وطن درگذشت.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/691881" target="_blank">📅 10:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691880">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeaba5e2ee.mp4?token=Ubfc3ax2-yM3jxdHRWdhRTBk6dq9b6wmMGlzkWofS-ztDxT69UqA8-Cookab6ccN14Vu41DFfhILSSoALhU5GKl0azLXGL_i5P4d_mgBLaPHmZeWCTzTBM4-RGf8jOogLMWtVpTA4vfG62SJB1e8UDHPFP5HdXE-NxcEvCe4d9aregSKj9ykocDMqI5YYOI9OuonLz00kuvXd47x-NrQpTawIpwgpfB1VI79zy0xcFTAUg3bEr8DHVBRTrtmn639EQZWREXDJ7DgqaCRP8tZ1TGWPRyn748LpZJGIaIGNI6gI1XvELfdUfmD81q5N4uecIxNFZIYjFMZFtVabo9RkjiA5cWgp-j9F1UCw_6oFf1oG3QtObQGpYcAu-1cHk13oN8mGB28UyGUbOhOcKYxDDDTHOO2ldGIqzqKPGy6EkkdtgJuSVyD9Q_kZzo3W6ExrJjcEdbC5uqgcLSvJAi7r2A_QRIkVJjim-fhl1T_x6P-DdVsknRc3Hqb19ZiDFpXS3BxjvZOmR2jsBuQAno6tP1MvvAFNBjADx-Wr8L-veHKyqAFMA6NLq_RUwx29zwp-v7yYJk4xnkdUF__baCOrQeZPd28m-QiIh0W6B1pOJYKHf1zqfBE0g2OBOdAPLdClKgZOF31DqBa-g_UOHY34e72IuNJpOr9JAfVKiYyXKY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeaba5e2ee.mp4?token=Ubfc3ax2-yM3jxdHRWdhRTBk6dq9b6wmMGlzkWofS-ztDxT69UqA8-Cookab6ccN14Vu41DFfhILSSoALhU5GKl0azLXGL_i5P4d_mgBLaPHmZeWCTzTBM4-RGf8jOogLMWtVpTA4vfG62SJB1e8UDHPFP5HdXE-NxcEvCe4d9aregSKj9ykocDMqI5YYOI9OuonLz00kuvXd47x-NrQpTawIpwgpfB1VI79zy0xcFTAUg3bEr8DHVBRTrtmn639EQZWREXDJ7DgqaCRP8tZ1TGWPRyn748LpZJGIaIGNI6gI1XvELfdUfmD81q5N4uecIxNFZIYjFMZFtVabo9RkjiA5cWgp-j9F1UCw_6oFf1oG3QtObQGpYcAu-1cHk13oN8mGB28UyGUbOhOcKYxDDDTHOO2ldGIqzqKPGy6EkkdtgJuSVyD9Q_kZzo3W6ExrJjcEdbC5uqgcLSvJAi7r2A_QRIkVJjim-fhl1T_x6P-DdVsknRc3Hqb19ZiDFpXS3BxjvZOmR2jsBuQAno6tP1MvvAFNBjADx-Wr8L-veHKyqAFMA6NLq_RUwx29zwp-v7yYJk4xnkdUF__baCOrQeZPd28m-QiIh0W6B1pOJYKHf1zqfBE0g2OBOdAPLdClKgZOF31DqBa-g_UOHY34e72IuNJpOr9JAfVKiYyXKY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توضیحات سخنگوی سپاه در رابطه با سلاح جدید ایرانی که روی ناو هواپیمابر آمریکایی آزمایش شد
🇮🇷
✊
@AkhbareFor</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/691880" target="_blank">📅 10:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691878">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gYSWHdIbcPBSJwBgCPkyzT-BbCBOj-mLgYrkwMK4lxa-DgdBICjRUgyBYgvj02zjlJ59m64RYuIh8v3joq0ZQauDADQpKE4kG6edBKUcUTr5UpflNGopX3iEDPJpRsRTCixrMiPfTEIr9E30kUrUD95BvNOcgwb9EOIUvakoE2wnKVfGUExfuw6vpbKaZGKzYp1JTZeb01eo9gOAS0f5aMiYl4aOT3MDTY6Et-OR16sTJUH0_QhaBub3iuGGSc_C2qHctzlnuxcjlw-Y3XzbIBSI3U7GRYPMahq0QEgiq3Q7_YVBhFZfanTlHObb7Nm0r_Bblxhw8AXyVrVH9glA6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nEih4G7wcOmcWw5iQUZeiI89ZftpvyOfrEdNt_wv1z1jQerOgW8OV4R_nFB6ntvDtHq4HeY8WU32lK_U2ql9OaQdapBSIR26vS_eGBjGnahf46X8hK8S80THwSWeG4GlBpCTW2goxgR07GZSb7MA1MrA72P2sY8bctbKmFyz2FSecD42Lo838vbNuzAVZPjs6YeooNVmzdL_SjbVqE8hdar6xhzRZFNLSCohdiunX2gNXIUoRhDzmllzcudlCX-KtFvwX1Rk7GMS5Hxwum3ngc9MyKhOPwmoX8P6sdzQIAHRlOJ2kjwqu44dVY5CjskKvnxo5GTHVk1NdSbR6xXs1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
افزایش ۳۱ درصدی حجم آب در سدهای کشور
🔹
بر اساس آخرین آمار، از ابتدای سال آبی تا تاریخ ۲۸ شهریورماه حجم آب موجود مخازن ۲۴.۶۴ میلیارد مترمکعب ثبت شده که نسبت به سال قبل ۳۱ درصد افزایش داشته و میزان خروجی سدهای کشور نیز نسبت به سال قبل ۲۰ درصد بیشتر شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/691878" target="_blank">📅 10:06 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691877">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
سپاه استان هرمزگان: انهدام مهمات عمل‌نکردۀ تجاوز آمریکایی-صهیونی در شهرستان رودان امروز ساعت ۱۱ تا ۱۵ انجام می‌شود
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/691877" target="_blank">📅 10:06 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691876">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
متن کامل پیام رهبر معظم انقلاب در پی ارتحال حضرت آیت‌الله‌العظمی شبیری
🔹
خبر تأسف‌بار ارتحال استاد معظم، فقیه عالی‌مقام حضرت آیت‌الله‌العظمی شبیری رضوان‌الله‌تعالی‌علیه واصل شد.
🔹
این عالم بزرگوار همهٔ عمر شریف خود به‌جز چند سال اول طفولیّت را در مسیر تعلّم و تعلیم و تحقیق گذراندند و همواره از سوی هم‌ترازانِ سِنّی و دوره‌ای و اساتید به‌عنوان شخصی محقق و ژرف‌نگر قلمداد می‌شدند.
🔹
تسلّط ایشان بر فنون مختلف مربوط به استنباط احکام شرعی با ظرایف و لحاظ دقایق همراه بود.
🔹
مجالس درس آن بزرگوار حتی وقتی که عدد حضّار آن از چند نفر تجاوز نمی‌کرد، به‌عنوان مجالس تتبّع و تدقیق شناخته می‌شد و بحق چنین بود.
🔹
بحمدالله در حدود کمی بیش از سه دههٔ اخیر، عدهٔ زیادی این توفیق را یافتند تا از وجود مغتنم ایشان در حدّ ظرفیت خود بهره ببرند و برای محافل علمی و تدریس خود توشه بردارند. محضر ایشان، محضر اِفاده و استفاده بود حتی آن وقتی که قدم‌زنان بعد از درس به‌سوی بیت شریف می‌رفتند.
🔹
غیر از وجههٔ مسلّم علمی، رفتار متواضعانه و پدرانهٔ ایشان با طلّاب و فضلا هم امری مشهود و درس‌آموز بود.
🔹
بی‌شک فقدان این شخصیت ممتاز، خللی در ردیف محققین تراز اول شیعه در عصر حاضر ایجاد نموده است که شاید جبران آن مدّت‌ها به طول انجامد.
🔹
بنده این مصیبت را به سرورمان عجّل‌الله‌تعالی‌فرجه‌الشّریف و حوزات علمیه و بالخصوص شاگردان و علاقه‌مندان و بالاخص بیت شریفِ عالِم و فاضل‌پرور ایشان تسلیت عرض نموده و از محضر حضرت حق جلّ و علا، علوّ درجات برای آن بزرگوار مسألت دارم.
✍
سیدمجتبی حسینی خامنه‌ای
🗓
۳۱/شهریور/۱۴۰۵
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/691876" target="_blank">📅 10:04 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691875">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| نَبض تهران |</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bc0634a.mp4?token=IuZidXebgLA1b-tfrNooBzdq8VZ_DN-2a0W5YUxA9qfO_gY_4lgQYmi2YcesiJ7k9TsJ2tXGy8psjSF_XLFzHUV78RA3En4_nZ6xIR6AjZExaY_v5zQKqVUEN7xvkDPWiiISKpoXYZKbYCm-5GM6PcN79R3adnbmfK8JGBRlykzOwyCIaQSXaf-bdkWo63birz_MXQ6L5e9Opn9t1BjH059Sj-RdeBRknK3xxrUCdo_t607LAsUXHied53QklnPSluntOS8PsfC_2GGSkxOHO6ZtvUXdgNRJEEAmCJZkE9NFKFlSZy3Jd_3Zo-k2Xgg4FoMgbcnvF03ewuk-6k9fnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bc0634a.mp4?token=IuZidXebgLA1b-tfrNooBzdq8VZ_DN-2a0W5YUxA9qfO_gY_4lgQYmi2YcesiJ7k9TsJ2tXGy8psjSF_XLFzHUV78RA3En4_nZ6xIR6AjZExaY_v5zQKqVUEN7xvkDPWiiISKpoXYZKbYCm-5GM6PcN79R3adnbmfK8JGBRlykzOwyCIaQSXaf-bdkWo63birz_MXQ6L5e9Opn9t1BjH059Sj-RdeBRknK3xxrUCdo_t607LAsUXHied53QklnPSluntOS8PsfC_2GGSkxOHO6ZtvUXdgNRJEEAmCJZkE9NFKFlSZy3Jd_3Zo-k2Xgg4FoMgbcnvF03ewuk-6k9fnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🫲
دست طلب به سوی شما دراز کردیم و مهر پاسخ نصیبمان شد...
🤝
⚡️
برای تابستانی که گذشت، قدردان همدلی‌تان هستیم و قرارمان برقرار است....
❤️
#قرار_همدلی
|
#صنعت_برق
روابط عمومی شرکت توزیع نیروی برق استان تهران</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/691875" target="_blank">📅 10:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691874">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمدیریت دارایی گندم</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uw6BcovvqOiaTrZsPTTNaeuHFXSia1SY3V6Z1tVMEI-kuSdOhMbHiMzoduttd-z-a7IuTyisdOJeiNRFAcFTqRQLBsPPyC1pELSCzNz3zvdTsTn78CKIM1l2WlJ0NTIXPkNkbkMHqAy9HuphSljdpvFRmQYjtV2JRkk1umEi5jxupB_HfEkK0AXo-LcJdXlXg07Xc_S7oglF6DYhuqjnjR3GmSrHdPNdhVx5B3OTkLI3p-EKrXEVhHfGGrlMgnf1l6ibhNns4huh9cNBLD9ht3rEvFn3f-vhj_3sfSBK7YbUoQM-0p__CGU8MoIqmHXD39U5ariSbhKdx0pRO_bEkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پول شما نباید بیکار بمونه؛ بذارید براتون سود بسازه
‼️
↗️
صندوق درآمد ثابت ثمر،
بهترین گزینه سرمایه‌گذاری برای کسانیه که به دنبال بازدهی مستمر با ریسک نزدیک به صفر هستند.
🟡
بازدهی مؤثر سالانه
۴۰٪
🟡
سود روزشمار
🟡
بدون نرخ شکست
🟡
معاف از مالیات
🟡
ریسک نزدیک به صفر
🟡
امکان مدیریت نقدینگی در کنار دریافت سود
👈
خرید با نماد «ثمر»
🔗
مشاوره و سرمایه‌گذاری
🔤
پشتیبانی:
@gandom_mediaa
☎️
شماره تماس: 02192003330
🌾
نقشه راه سودآوری با گندم:
@GandomFinance</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/691874" target="_blank">📅 10:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691871">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/331853fb14.mp4?token=QUUXlE9LayTHW2dyDhwmdDNpFn_C6Dj97wraRFjoL8-kHGyS52lrSPLtYkcnReNl088A6rTiDyOHXzYmG7433Q4jJjd66mCfFhFQ4laBsK8LgGCAIghWO5D4vw-7YmT9Rs3_3ftj6glYOzoB_8qs6-a7JtcqZCN-vv4I9lBbW0Ak1pyvismG4XNIf8xt9JDHZREXIncxdAnjPXn6hjU4sNNdfBA4JyHEtvVn6wqySKjEEZ5Tce0MPSVPBnBPgMUGM3O99xZfHjM-UEsQXRlfuN5dwMPNyITyVSBxTbz0dn1vFxRwcUMgtrv8cdr_KvtGUcul34X0PU60pAffM9XzYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/331853fb14.mp4?token=QUUXlE9LayTHW2dyDhwmdDNpFn_C6Dj97wraRFjoL8-kHGyS52lrSPLtYkcnReNl088A6rTiDyOHXzYmG7433Q4jJjd66mCfFhFQ4laBsK8LgGCAIghWO5D4vw-7YmT9Rs3_3ftj6glYOzoB_8qs6-a7JtcqZCN-vv4I9lBbW0Ak1pyvismG4XNIf8xt9JDHZREXIncxdAnjPXn6hjU4sNNdfBA4JyHEtvVn6wqySKjEEZ5Tce0MPSVPBnBPgMUGM3O99xZfHjM-UEsQXRlfuN5dwMPNyITyVSBxTbz0dn1vFxRwcUMgtrv8cdr_KvtGUcul34X0PU60pAffM9XzYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک‌ غذای فوری و پر طرفدار برای وقت‌هایی که از شام‌های تکراری خسته شدی  موادلازم:
🔹
سیب‌زمینی
🔹
پیاز
🔹
سیر
🔹
مرغ
🔹
نان‌لواش
🔹
ادویه به میزان دلخواه #آشپزی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/691871" target="_blank">📅 09:59 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691870">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
آغاز دومین مرحله پرداخت وام فوری ۱۵۰ میلیونی بازنشستگان کشور
🔹
دومین مرحله پرداخت وام فوری ۱۵۰ میلیون تومانی ویژه بازنشستگان و مستمری‌بگیران تأمین اجتماعی آغاز شد.
🔹
بر اساس دستورالعمل اعلامی، این تسهیلات بدون نیاز به ارائه چک یا ضامن ،بازپرداخت یک‌ساله و اعتبار آن در کمتر از یک‌روز کاری پرداخت می‌شود.
🔹
فرآیند ثبت درخواست و ارائه مدارک به‌صورت غیرحضوری انجام شده و متقاضیان برای ثبت درخواست نیازی به مراجعه به بانک ندارند.
🔹
جهت اطلاع از شرایط و ثبت درخواست، با کارشناسان از طریق شماره 02191551808 در ارتباط باشید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/691870" target="_blank">📅 09:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691869">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
طحان‌نظیف: طرح جدید مهریه در نوبت بررسی شورای نگهبان قرار گرفت  سخنگوی شورای نگهبان:
🔹
طرح جدید مرتبط با موضوع مهریه و احکام پیرامونی آن به شورای نگهبان واصل شده و در نوبت رسیدگی قرار گرفته است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/691869" target="_blank">📅 09:51 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691868">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7d21f3fd4.mp4?token=ZHMuTlbCF7Mxc86915i3PFog6NKGH1OjS_ptBq75_h7RtsEBkX4mdwTuF7WV_p9fDBWi1C7_1z_Ul_VOz7im4KehNwtMAVfxd3ybcuYpOYlUue46nz9_jjD5qhJzsve2k7XSXYxBrX_SylJX8qjmDYkjtx8ge_rwAVOhM-we08jMHWs5TJP8a2biT-fqEnTIH8SS82YE6BONZJ2rj8Uf1JkLzeALADuM-Hwz2llps2HZjkS6X6sOeH8Jkh_xTCzM3wLsMMQw0G_dsJDYnF1PaDwYIX0CISbAt3JwCMtYhvpY6MJ6pePNxztAX4UnDa_HrWs5emQVlBbSL4kGFtt0rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7d21f3fd4.mp4?token=ZHMuTlbCF7Mxc86915i3PFog6NKGH1OjS_ptBq75_h7RtsEBkX4mdwTuF7WV_p9fDBWi1C7_1z_Ul_VOz7im4KehNwtMAVfxd3ybcuYpOYlUue46nz9_jjD5qhJzsve2k7XSXYxBrX_SylJX8qjmDYkjtx8ge_rwAVOhM-we08jMHWs5TJP8a2biT-fqEnTIH8SS82YE6BONZJ2rj8Uf1JkLzeALADuM-Hwz2llps2HZjkS6X6sOeH8Jkh_xTCzM3wLsMMQw0G_dsJDYnF1PaDwYIX0CISbAt3JwCMtYhvpY6MJ6pePNxztAX4UnDa_HrWs5emQVlBbSL4kGFtt0rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرار نوجوان دوچرخه‌سوار همزمان با انفجار در غزه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/691868" target="_blank">📅 09:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691867">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">چله علم النور 4 جلسه 2</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/691867" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
جلسه دوم
؛
شوق زیستن
🔹
نام «
الْبَاعِث»
مانند جرقه‌ای است که انسان را از سطح یک موجود بیولوژیک به موجودی مبعوث و اثرگذار تبدیل می‌کند.
🔹
افسردگی عمومی، کاهش آمار ازدواج، مهاجرت نخبگان و بی‌رونقی کسب‌وکارها، نشان‌دهنده‌ فقر انرژی حیات در یک جامعه است.
🔹
شاه‌کلید درمان ضعف‌های جسمانی و روانی که ریشه در بی‌انگیزگی دارند، در تکرار و اتصال به نام‌های خداوند نهفته است.
🔹
ذاکر حقیقی نام مبارک «الباعث»، می‌تواند با حضور خود به جامعه‌ای که در لبه‌ی فروپاشی روانی قرار دارد، امید و جان دوباره ببخشد.
🔹
غایت دریافت انرژی حیات، مصرف کردن آن در مسیر «خدمت به خلق» است.
🔹
شوق زیستن، مانع از هدر رفت قوای معنوی شده و حیات انسان را «پاینده» و «ماندگار» می‌کند.
🔹
نشانه‌ حیات حقیقی و اولین ثمره‌ی زنده شدن دل با نام «الْبَاعِث»، توانایی مشاهده عمیق جهان و خروج از غفلت است.
#مدیتیشن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/691867" target="_blank">📅 09:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691866">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/668fbba207.mp4?token=m3ih7homrlgB30mRws8FW0OBCVSrPBL0mp__qMYkbf80jjJv296Tqd_y46aTMWY7RPF3tDNTXk0TxI-rAJpXDjnp_KQDb_s1Ufe8GGVUtIaCE5_PmG0GmL-zMtwDoMMg7HGXTJSQeLxFL1TLYtsQWmHGyBFLFH8MKzd8W8Y1gdNDvFN2EebppFx2dWxapYOF31kJux7FGdZiXkXnPsVl42We1dDiLEDUAFngdOKz_uO5ALg1SnuUHMkvVcPucM__oA1TdAs3Zcs46E8AqzdJEMdo9KUoZ5WMlxJcjY-txp0xlMVbokmYyfA6NabJ4MjR876xnt-u926iekrhwH-HFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/668fbba207.mp4?token=m3ih7homrlgB30mRws8FW0OBCVSrPBL0mp__qMYkbf80jjJv296Tqd_y46aTMWY7RPF3tDNTXk0TxI-rAJpXDjnp_KQDb_s1Ufe8GGVUtIaCE5_PmG0GmL-zMtwDoMMg7HGXTJSQeLxFL1TLYtsQWmHGyBFLFH8MKzd8W8Y1gdNDvFN2EebppFx2dWxapYOF31kJux7FGdZiXkXnPsVl42We1dDiLEDUAFngdOKz_uO5ALg1SnuUHMkvVcPucM__oA1TdAs3Zcs46E8AqzdJEMdo9KUoZ5WMlxJcjY-txp0xlMVbokmYyfA6NabJ4MjR876xnt-u926iekrhwH-HFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن رضایی در مصاحبه با الجزیره: اسرائیلی‌ها تونل‌های خالی لبنان را برای تبلیغات و نمایش انتخاباتی منفجر کردند. عکس و فیلم گرفتند و گفتند: «ببینید نتانیاهو چقدر قوی است.» همه اینها تبلیغات است که به انتخابات مربوط می‌شود. با این حال، کار ما بر اساس اصول است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/691866" target="_blank">📅 09:39 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691864">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
فلاحت‌پیشه، فعال اصلاح طلب: اگر رئیس‌جمهور اختیار تصمیم‌گیری درباره جنگ را ندارد، بهتر است که به امریکا سفر نکند. پزشکیان باید حتی با ترامپ مذاکره کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/691864" target="_blank">📅 09:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691863">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
ادعای‌ نیویورک‌تایمز به‌نقل از نخست‌وزیر عراق: ایران اجازه عبور نفتکش‌های عراقی از تنگه هرمز را نداده و به‌دنبال افزایش قیمت جهانی نفت است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/691863" target="_blank">📅 09:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691862">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e04cd3c51.mp4?token=Op8g-fkQAjqH9AEyp4NA6veOgsNhz_0vKxr8tarttBCmQiBRuUCDDdQYlVUAVJVDP5t3NvkTdSWWp6bypMnkkDEqiJ9cRyYJlwrYUcct8zPcM8rAnq9mv-SYejZ8lgsW2GtMVWmhcE8nI9GfVCvyYswEpDY5aS3h9YZkR0o1z9rbDvcmxACVtUSvHtSOX7y1aaFvihRgTC7oE2PnbIZwwNyIMqloSyeYVAuoq46kpx_ZKTbLJWqqJKbzWXNy0VJIrRPzvKQf8cpRkA_MHl13bfqsk_BHT-lVFUM3kvGspUW4GTQtUrbOi8GVBaBKcs5oEF5mBjtjehZwVgEDk1iiJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e04cd3c51.mp4?token=Op8g-fkQAjqH9AEyp4NA6veOgsNhz_0vKxr8tarttBCmQiBRuUCDDdQYlVUAVJVDP5t3NvkTdSWWp6bypMnkkDEqiJ9cRyYJlwrYUcct8zPcM8rAnq9mv-SYejZ8lgsW2GtMVWmhcE8nI9GfVCvyYswEpDY5aS3h9YZkR0o1z9rbDvcmxACVtUSvHtSOX7y1aaFvihRgTC7oE2PnbIZwwNyIMqloSyeYVAuoq46kpx_ZKTbLJWqqJKbzWXNy0VJIrRPzvKQf8cpRkA_MHl13bfqsk_BHT-lVFUM3kvGspUW4GTQtUrbOi8GVBaBKcs5oEF5mBjtjehZwVgEDk1iiJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نقطه‌ضعف حشرات و جانوران موذی از زبان خودشان
🐜
🪳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/691862" target="_blank">📅 09:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691861">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/910f924e10.mp4?token=LM0CaZvOAxGsSmP0-IUWrxlq9jGtROrKtNns5GGwEodp2OGOt2Ae2J03uI1Z0eEGlEZPoF_qZjScTgsVgIHN6kUgXOnhMVbydO-a-kq3UJMzDWKFLqDR232zlaNFosig2XI7Q_DxctY2KOMMt1T4rtveQ6ce5KWtTtDwzfPBiwxc-LMzeIAAUEp54K-0kCJhovfuW30-f1a_Jo29Gas4BC6ki1q6ku48IrVQM7jszkZKzatEfWmbyA9murDkGnRZwSr0oY0ctNM6d8Mv5pyCklg8iEA1JgixAVLTvT_uTjB8H9y-uklDVwEABRl-f_ctf3pNERC0Cmr0vsDUZdad2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/910f924e10.mp4?token=LM0CaZvOAxGsSmP0-IUWrxlq9jGtROrKtNns5GGwEodp2OGOt2Ae2J03uI1Z0eEGlEZPoF_qZjScTgsVgIHN6kUgXOnhMVbydO-a-kq3UJMzDWKFLqDR232zlaNFosig2XI7Q_DxctY2KOMMt1T4rtveQ6ce5KWtTtDwzfPBiwxc-LMzeIAAUEp54K-0kCJhovfuW30-f1a_Jo29Gas4BC6ki1q6ku48IrVQM7jszkZKzatEfWmbyA9murDkGnRZwSr0oY0ctNM6d8Mv5pyCklg8iEA1JgixAVLTvT_uTjB8H9y-uklDVwEABRl-f_ctf3pNERC0Cmr0vsDUZdad2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قطع صدای ترامپ در مراسم کاخ سفید؛ خبرنگاران تحریم کردند
🔹
رسانه‌های بزرگ آمریکا از جمله CNN، فاکس‌نیوز و NBC، در اقدامی کم‌سابقه از پوشش مستقیم سخنرانی‌ها و مصاحبه‌های دونالد ترامپ خودداری کردند؛ به‌گونه‌ای که نبود خبرنگاران، انتقال مستقیم و دقیق اظهارات…</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/691861" target="_blank">📅 09:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691859">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
بیانیه ضد ایرانی گروه ۷: اقدامات ايران که قابل اعتراض هستند، یک الگوی خطرناک از تشدید تنش را نشان می‌دهند و هشداری برای وخیم‌تر شدن بیشتر درگیری‌ها هستند
گروه هفت:
🔹
اقدامات ايران تهدیدی برای تضعیف تجارت بین‌المللی و ایجاد بی‌ثباتی اقتصادی جهانی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/691859" target="_blank">📅 08:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691858">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
ورود به طرح ترافیک بدون رزرو قبلی چقدر جریمه دارد؟
پلیس راهور تهران:
🔹
پوشاندن پلاک خودرو: ۷۰۰ هزار تومان
🔹
نداشتن پلاک جلو یا عقب و ناخوانا بودن پلاک: ۴۰۰ هزار تومان
🔹
ورود بدون رزرو به طرح ترافیک: ۵۲۲ هزار تومان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/691858" target="_blank">📅 08:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691856">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cd4WD10bb-dekHclqZHofP9PQsrg_6ILm1D4ueEUB5g2hP0y_IYI3E1lRvkTD_qiYvOnVs3P9G4mtKBu71c_CBs_R6AWj3pQjpPcLW8x8h_Rghh3zhBOtiDY28HrweKBbVh0d5e4xUsqwKtW9xNNyJJN0OfDLlmd_1klDU8_VPmMDM3uJAaYj1utK_8WPB9dmbDlbBUTb5W-Eu-lLn4_kJtzSi-SQypunSTDKO_vF_96naEu-Lztw6b6kSvRmRWYWPGOf9IzHWSc4zXGbLjgUvlaAaDjE85WdKf4n0brpnJIvKFTaNlkoMdn7WzYJ_l7KbtbPPhXnbzzW9O7R3x64A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاخ سفید از راه‌اندازی «Trump TV» خبر داد و اعلام کرد این شبکه به‌صورت ۲۴ ساعته و ۷ روز هفته پخش خواهد داشت؛ جزئیات بیشتری ارائه نشده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/691856" target="_blank">📅 08:39 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691854">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2053a9052c.mp4?token=jEUOeSBdvA4ZAJs070l1vmhdicKXXLVYscSmlZpIAwt3nYrn7-xo0HhB4a6X6wGXn1oBwEmdDuPxNXn8oI5APDMseIttBI0oV5edAFd-gfOgmYZc5lBsvsyRFXQOlorhyjFNQSl9tFOLMA51XssDGKDMKeEZd3ybHW4DBYeBewxDbxMN9a7MDpcvD_SYRUfzSHd1dkuqiRSUfL5rieFkmcgq9CqeylaBL31PgrbZKBUY5JoZjuTADq9eydwmMeBTGuVpVJ86GO_LGgwdlt3FfGtCrb0gAMJSUHNxtrNv8-71mlQd4htIkROsaLA2NjOfdom0fpVkgNE908sAD6fxBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2053a9052c.mp4?token=jEUOeSBdvA4ZAJs070l1vmhdicKXXLVYscSmlZpIAwt3nYrn7-xo0HhB4a6X6wGXn1oBwEmdDuPxNXn8oI5APDMseIttBI0oV5edAFd-gfOgmYZc5lBsvsyRFXQOlorhyjFNQSl9tFOLMA51XssDGKDMKeEZd3ybHW4DBYeBewxDbxMN9a7MDpcvD_SYRUfzSHd1dkuqiRSUfL5rieFkmcgq9CqeylaBL31PgrbZKBUY5JoZjuTADq9eydwmMeBTGuVpVJ86GO_LGgwdlt3FfGtCrb0gAMJSUHNxtrNv8-71mlQd4htIkROsaLA2NjOfdom0fpVkgNE908sAD6fxBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی از لحظه‌
سرقت موبایل یک پاکبان در مشهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/691854" target="_blank">📅 08:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691853">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/591b48d1e2.mp4?token=oF4OuHWte7DznVBFiHs_Th8bYbWlW_vD1tr7NKSO6jXOpMlg-mlsaVL6ILI2asEuDx5GrMLP4utTEDASsKHSLH02JfbG3SYklT72--rKHkCKYa5s2czCzU3GGEfbQkOLTvOp9n_LJg3cxw8YO_qZXtgx3E3N2mRbLMHU40uaAxQ2M3SLLW3Cu6PncFupgWnUh7z5m0rPCWcazlZiXxetniaWYua6UJ9FHnwRF3ZRyCp2dru1neoQn25wm4Fktbr_iAi94706uzVKPTNmrkJukjcS3oCo8TawZdOhc4g5Fw82O0S0s5zvl7EZGKRXxh0PyXHGdivIAKLmfm-fH90XGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/591b48d1e2.mp4?token=oF4OuHWte7DznVBFiHs_Th8bYbWlW_vD1tr7NKSO6jXOpMlg-mlsaVL6ILI2asEuDx5GrMLP4utTEDASsKHSLH02JfbG3SYklT72--rKHkCKYa5s2czCzU3GGEfbQkOLTvOp9n_LJg3cxw8YO_qZXtgx3E3N2mRbLMHU40uaAxQ2M3SLLW3Cu6PncFupgWnUh7z5m0rPCWcazlZiXxetniaWYua6UJ9FHnwRF3ZRyCp2dru1neoQn25wm4Fktbr_iAi94706uzVKPTNmrkJukjcS3oCo8TawZdOhc4g5Fw82O0S0s5zvl7EZGKRXxh0PyXHGdivIAKLmfm-fH90XGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شبکه‌های تلویزیونی بزرگ ABC، CBS، Fox News و NBC توافق کردند، پوشش جمعی خود از در برنامه‌های ترامپ را متوقف کنند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/691853" target="_blank">📅 08:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691852">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
وال استریت ژورنال: آمریکا به تعدادی از کشورهای غرب آسیا که تأسیسات انرژی آنها در حملات ایران آسیب دیده، وعده کمک ۵ میلیارد دلاری داده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/691852" target="_blank">📅 08:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691851">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6f82ebb23.mp4?token=XQ05CEoe3YICLPIGLl619lxVzfChJihPdwPthpnDSTA_lfAqcHkfm2TV25fAIMYuhfbewdKaBmhNxgoWlyuLcjJgrj6X9CfcW9RXsCmbZC99rHA7gEd6T1NwtthXIGghbeGFOqhVXIb6zXqp1uZEX-5yYWYyh_0x_Qg3vusqPzfpPktUamypKYh1IvId7dmD4d_pmZillmkAnm4fc56NtMJ3knlPEkol87S6AYpSTp0HS_3ISdzxQLzYJlGnr68S7QWUgAJXryEpYkcKY2lkoAXZ6ti5q1xzVZIcoV-_7mGyZcUzKmIsJrgFeu_ZfE0bLs3xN1okvcejwFhhvfoxgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6f82ebb23.mp4?token=XQ05CEoe3YICLPIGLl619lxVzfChJihPdwPthpnDSTA_lfAqcHkfm2TV25fAIMYuhfbewdKaBmhNxgoWlyuLcjJgrj6X9CfcW9RXsCmbZC99rHA7gEd6T1NwtthXIGghbeGFOqhVXIb6zXqp1uZEX-5yYWYyh_0x_Qg3vusqPzfpPktUamypKYh1IvId7dmD4d_pmZillmkAnm4fc56NtMJ3knlPEkol87S6AYpSTp0HS_3ISdzxQLzYJlGnr68S7QWUgAJXryEpYkcKY2lkoAXZ6ti5q1xzVZIcoV-_7mGyZcUzKmIsJrgFeu_ZfE0bLs3xN1okvcejwFhhvfoxgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شرمندگی مفسر سیاسی آمریکایی در مصاحبه با آکسیوس؛ آمریکا از القاعده بدتر است نمونه روشنش کشتار مدرسه میناب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/691851" target="_blank">📅 08:06 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691850">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25fa2dcc43.mp4?token=o6I0nCxKTw2blHPTke6BHi0ZkeycmAAa20OswWUFafTfOdRnrIUjToy7jJJZO24sBks0iWTokXdyOOr2-p023buKfVucmdMLF3ooKmwMWr6oaQt6Lfgc_A4VO11FNiFUqgUrQLuPeJztNyi79veECgZycnA2RPzrjpJPybm8TaETyyDD5JxsRni4oj7JAA5oCM00Z5SIdkvU56L6Q_qDlh0cNILgMx408RMlX_TTmapJFPH5L5DMO-jXpVjEaixTXR7Mt9a54Q9WSkan0wltYOzT7Q-vlsKrLp-ejBW004rcq680FQUUusvkYxCjAi3qWbiZl4r2Nyk1OnuSP79VJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25fa2dcc43.mp4?token=o6I0nCxKTw2blHPTke6BHi0ZkeycmAAa20OswWUFafTfOdRnrIUjToy7jJJZO24sBks0iWTokXdyOOr2-p023buKfVucmdMLF3ooKmwMWr6oaQt6Lfgc_A4VO11FNiFUqgUrQLuPeJztNyi79veECgZycnA2RPzrjpJPybm8TaETyyDD5JxsRni4oj7JAA5oCM00Z5SIdkvU56L6Q_qDlh0cNILgMx408RMlX_TTmapJFPH5L5DMO-jXpVjEaixTXR7Mt9a54Q9WSkan0wltYOzT7Q-vlsKrLp-ejBW004rcq680FQUUusvkYxCjAi3qWbiZl4r2Nyk1OnuSP79VJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این تمرینات ساده، روزت رو پر انرژی آغاز کن #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/691850" target="_blank">📅 08:06 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691849">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
شکار یک فروند زیرسطحی هوشمند دشمن آمریکایی در تنگه هرمز   نیروی دریایی سپاه :
🔹
مردم مبعوث شده ایران عزیز؛ با عنایت خاصه خداوند متعال رزمندگان نیروی دریایی سپاه یکی از مدرن ترین زیر دریایی های هوشمند و بدون سرنشین ارتش تروریست امریکا را در ورودی تنگه هرمز…</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/691849" target="_blank">📅 08:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691848">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
سپاه: آشیانه تعمیر و نگهداری، آماده سازی و محل استقرار جنگنده های F-35 ،F-16 ،F-15 و شلتر جنگنده ها مورد هدف قرارگرفت   روابط عمومی سپاه پاسداران انقلاب اسلامی: بسم الله الرحمن الرحیم قَاتِلُوهُمْ يُعَذِّبْهُمُ اللَّهُ بِأَيْدِيكُمْ وَ يخْزِهِمْ وَ يَنصُرْكُمْ…</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/691848" target="_blank">📅 08:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691846">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
انگلیس به جنگ سعودی علیه یمن پیوست
🔹
«اندی برنهام» نخست‌وزیر انگلیس شامگاه دوشنبه به نیروی هوایی این کشور اجازه داده تا به جنگنده‌های سعودی که علیه یمن حملات انجام می‌دهند،‌ سوخت‌رسانی کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/691846" target="_blank">📅 08:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691845">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b8831bcd7.mp4?token=JydHNpr0rTG6811I_Fafa1MEE-chi1dJev2p8SaD6hO7Qcbn71L6FVMik3UyX8pPxNsD7KKiBxnKNraru1tt4HSH2ug0tG-xxuXlFDMNt6V2gm3tJhE93bbhY9a_ol_Dig62eOua1IyZ2NedBoTPcRIDI3dYWBkUKIRWYsNEWPPDMgZoBFN1slDqpbxJm2fbESYFEmocR6qCOMFtfwIHFUG9wkUa2GeJnBzt2y7PB2dudielfJNgv9u6n38r1osxW4Fem83nO0iyk1Iag8r6Ks5MpNtNsIfwMyq9cwcziDyOTnlYPLj0DQDcEcMPNUqcEGrje4YCEWCwClqPaQd9Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b8831bcd7.mp4?token=JydHNpr0rTG6811I_Fafa1MEE-chi1dJev2p8SaD6hO7Qcbn71L6FVMik3UyX8pPxNsD7KKiBxnKNraru1tt4HSH2ug0tG-xxuXlFDMNt6V2gm3tJhE93bbhY9a_ol_Dig62eOua1IyZ2NedBoTPcRIDI3dYWBkUKIRWYsNEWPPDMgZoBFN1slDqpbxJm2fbESYFEmocR6qCOMFtfwIHFUG9wkUa2GeJnBzt2y7PB2dudielfJNgv9u6n38r1osxW4Fem83nO0iyk1Iag8r6Ks5MpNtNsIfwMyq9cwcziDyOTnlYPLj0DQDcEcMPNUqcEGrje4YCEWCwClqPaQd9Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای‌واهی جدید ترامپ: ایران سلاح هسته‌ای نخواهد داشت و وضعیت آنها اصلا خوب نیست. من امروز جلساتی در این مورد دارم
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/691845" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691844">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPbJYwoS7vUvE3m-Ii_goPmNp9pUPrPKtZHqhiV7CViCe107lIf408TMTnZghBeAYcD5SAyTyDbQ_RS2fJyjtqcRijSzdpyRjAF5RX4GLQkHXXl9_k2iRZqVdPrYGZSlhaW8l0usqLWUiE0uHoEbW9xsMjodLJtzDDZR2SZwExUWB6kC8iz-_W6RcC4zLOaMupyRvteWbMl9JiMWw7-bnWEdGLbdAZq4BT4AW0dM8060NNz_tdFshhHZzRjW8vq-U-C60hhjLsMv0itOXjVRFtYE0UIS1QPu5iTfP1n6Y4y72UMe0I7-l1M0j8mY66Ipj_XEnlHW6VplVFZ0zI6LZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز سه‌شنبه
۳۱ شهریور ماه
۱۰ ربیع‌الثانی ‌۱۴۴۸
۲۲ سپتامبر۲۰۲۶
سه‌شنبه‌ها
#دعای_توسل
بخوانیم
⬅️
متن و صوت دعای توسل
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/691844" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691840">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u26CPuFqhvoJhDxg5KN3U8zDDlJtFlTRo23s7mCOgH_Ca7c6A8Re0gLKjODeaZDOVpv2S2rnrOA2UqIBZfFOuIIYAi775BTQK_7rScZd0Waj3N5340MOAaR01pyymefp2zfUuUZ7YXiEokmPBLsZJydERH-bTiRDW9fwq-2b4kPt3KtdTrQoqELZQnz8BNHZWC90G81H9jN9vSIsS8KXiE1BQzBUNhVvl_6_i1kM0n_n7hmY-bxxJSmcU60JAoEiJ5MuCjRKrPMBClwD8Mdzmk7Pwc9ouT0HXFHXkuBYEyaff-fqRV-tueaKca06ZUsQMr3m0r6KRAx2_ntUMoYgOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08b1ea7144.mp4?token=Yyv00Cr4eZFd2FRavOZ7J1imvQu3fPF_3q1PFlK4CIOsW_fMXNiNJtasq8CPkLrIElOq6hEFl6sAyKKZLOULewrxIFjKTjKIcRg8Zy0SKQTuYeSyLKY7rVqJ4UmBu2dQz41VFqKThwqa6acupeSrjyrRM3VTwggeylyOcjBcpkAdB5Sw508RsblVuQvkAut7m7iRPj425Vd4wFiYPSGw6q8zNk49pgCivOZ-wTmYgVPm9cVGODALjEBRn04Tmojgm4MNAYjiErIGS9dpGkWHw_WZUlUK0IWu9JziiW0QNoEAmhSli3O_g4W7D94HJjfbAk0QyyFIfFRMieC--pjJFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08b1ea7144.mp4?token=Yyv00Cr4eZFd2FRavOZ7J1imvQu3fPF_3q1PFlK4CIOsW_fMXNiNJtasq8CPkLrIElOq6hEFl6sAyKKZLOULewrxIFjKTjKIcRg8Zy0SKQTuYeSyLKY7rVqJ4UmBu2dQz41VFqKThwqa6acupeSrjyrRM3VTwggeylyOcjBcpkAdB5Sw508RsblVuQvkAut7m7iRPj425Vd4wFiYPSGw6q8zNk49pgCivOZ-wTmYgVPm9cVGODALjEBRn04Tmojgm4MNAYjiErIGS9dpGkWHw_WZUlUK0IWu9JziiW0QNoEAmhSli3O_g4W7D94HJjfbAk0QyyFIfFRMieC--pjJFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماساژور تفنگی 4کاره
خستگی و گرفتگی عضلات رو با ماساژور تفنگی ۴کاره از خودت دور کن
💆‍♂️
✨
۴ سری کاربردی، طراحی سبک و قابل‌حمل؛ مناسب استفاده در خانه، باشگاه و سفر.
🛒
🔴
قیمت 1,798,000 تومان
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/brief/63579/180124/</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/akhbarefori/691840" target="_blank">📅 00:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691839">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCwcXAYfZ2PbZaSVPl08z1l9b7LjRHoPZEnEiDIfIhN3rorLDxjU3TFvCqH6pL-ehQayAjZMYuuMoHmAvpGu1OqMP-5WYuMeQijUO2PyciJR22xkCdZNzg-plSQkS3cpjwrONhdZAlCiOv0YW4bwJZkuGye2GpGUBE7jXH8SekFtmnAt8xqo-7CTGnWUk3di4Uvn5NDAAutvmmupdMHEHvZHiGpc3V6iKE5BypgL33cdt4I3C3cuvF4MVebDIPFlbFuQ1iBIbxvY0f_5-Em60LN-ouxHFNpw1pPP-2xPMDsMUfCPPtA5juNFOFC4BnnbqGkDzWl6-yZgw0N5mvyjbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ائتلاف سعودی: ریاض هدف حمله موشکی نیروهای مسلح یمن قرار گرفته است
🔹
ائتلاف سعودی در ادامه مدعی رهگیری و انهدام این موشک شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/akhbarefori/691839" target="_blank">📅 00:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691838">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rq5LhXYHrXbpO5H4kQ0qW3Uf44OsQDmZ9SuvwPyTh0mv03BBOTCyRCThT5TG66sesUcI8x2RHkNlOJdGTkDhFkNQhX6sh9L7OoDAh5SDtj7S8OuCY13QmFCEWDHsVOhvrNqod6ONLB3H4iE322D8ayFe_FVXfxnsCKgoITDQz8p5tjSyF9m5aNAX6DX8KMCxjBNQ8H2Z9Datd3zEmFmssqbJyLtuS2IFVbeGUOoY-Gn4thKDzwB0OZpFjxBX77ZRVFVbeSaVk43qYW9ZDrxAhTDLkAuYl4V_9u1rGMChNjkNINIeZQtSDTV5RTUNdA1iRD21mo8K901yN6DbpqaLLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادویه درمانی
🔹
ادویه‌ها فقط برای خوشمزه کردن غذا بکار نمیان، ببینید هرکدوم چه خواص درمانی دارن و چطوری میتونن به سلامت بدن کمک کنن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/akhbarefori/691838" target="_blank">📅 00:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691836">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
وزیر اقتصاد فرانسه در واکنش به انتقادها بابت افزایش قیمت سوخت در این کشور: «من نه دونالد ترامپ هستم و نه فرمانده سپاه پاسداران ایران»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/akhbarefori/691836" target="_blank">📅 00:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691835">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
نخست‌وزیر عراق: گروه‌های مسلح عراقی، تحویل سلاح‌های خود را آغاز خواهند کرد و انتظار می‌رود این روند تا ۳۰ ژوئن ۲۰۲۷ به پایان برسد
🔹
به دلیل جنگ، ۶۰ درصد از درآمدهای ماهانه نفت خود را از دست دادیم
🔹
اگر گروه‌های مسلح پس از پایان مهلت تعیین شده به فعالیت‌های خود ادامه دهند، آنها را «یاغی» تلقی خواهیم کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/akhbarefori/691835" target="_blank">📅 00:04 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691834">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
تیم ملی فوتبال ایران از ۱۶ تا ۲۶ آبان در تورنمنت چهارجانبه عراق با حضور عراق، لبنان و فیلیپین شرکت می‌کند؛ ابتدا با لبنان و سپس با برنده عراق-فیلیپین بازی می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/akhbarefori/691834" target="_blank">📅 00:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691833">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9_2SiPDAhLRIGni5PxOj_1iI_3aJvUx01AgavRl8sYAzPV_VC6HUwM4arS0QW-7FXxwaX1MK3E4iUfYh7SYrrVkBY36mURCZtUORxuWPSwq12e85LwkFCvNQhHTFIzWXQXmr41mQiVgD34NyM6rTYcbELS3NFRybYRTpX1hMoP3WV0RZxIP3WI2HUWAn2OBXYiu51kOHlxc2zdZpy0tD5BrDR-iKo2kroxvG-YgkUTxQAMIwoVrrw7f36toB2Z_qCGPSbQXPpLM8l1YVTmQy4IgwbqA0J7tTdMw8g7iAuY3wgNoOD4XQU_Lzyl-t4FjKWnslBD1oEcs9gbONvrYEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/691833" target="_blank">📅 00:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691832">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_E9C8qY_GLFBbX0ovs-dOvS_p8JcIMWf5ezTYt9H84kVBt0HyY1eL8Fpl9Dwk230tJKP8yPcg2D_5lVwSNFkaZ6POqBUZokBnu3VVyUfyWHf0ZUlTr_Z1D5IrkoFYOiu737BAvzSPDzrOLL3axF2CNS56LyVjgNcSYKd2dvV7w1L87ZOgFefu9CVjvQNp_8ckJDDNWVxy0t6oMBb0wcdcQdHif_Oi4qQCiw41Rhn2Gt1RlL3Wx5MrfssgsFN5awK7Jo5JqpukEMG3_AizvaL9kcH1g65VHVKOLvcJHxf9a099JFx8EP8HLgByOFh6J7ACRMu8qv0kDhzcapg0_9Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خواص انواع گیاه هایی دارویی و عرقیات رو بدونید
🔹
هرگز در مصرف گیاهان دارویی و عرقیات سنتی زیاده روی نکنید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/akhbarefori/691832" target="_blank">📅 23:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691831">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
عضو کمیسیون امنیت ملی مجلس: احتمال دارد آمریکا جنگی تمام‌عیار مشابه جنگ ۴۰ روزه با همکاری متحدانش علیه ایران شروع کند اما آنچه می‌دانیم، این است که روحیه سربازان آنها خوب نیست و ذخایر تسلیحاتی‌شان هم در وضعیت مناسبی نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/akhbarefori/691831" target="_blank">📅 23:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691830">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/274b445379.mp4?token=AoH_-GVDDX9fNng87_DjjYiv74rzfspMuiDk6JhK-bUyT-e1mKKMFvhn9aPGGykzLG6s3VoRIxCk3RFl1CdJnUaOO2sDScaCm8oa48VSCzkgjW49GKRFIZqgo90Ifmcp79KEE-ED7-GYMWzQIAUMDVwSmDkaraOySmeDmdYRRIkaLKrJdIcm3C9W_p9pApt7ivvN9yO3SZQt6SIIsnqQx3bDtPG_Lz8Z2s59bimwckGryFR31D9YZb3znHmBR2CWA2FujxCu9nJ97a2ew_9zQMV3w_4-_agQRR65rwNuU0wh_EiDQ2Zs2zw0U-PNBNOBBsiUx-5DXulxFbZLzPDtU2l6FvWe9xwwGHa6_OfYN_rbfGCBMXYmarcu3MdcGzqhjpHP_cc-Rjpd9v_WFLKWIJHed_Ytl-xgzpASw9SnafnEvTuJCRCVGHbJpWT9I1j3SU1fJjTw6TkLmMfLRFHyEh4R0QyGfaIcit8AXZQZp0vYwGiXO_EkUVRE6Rd8t_LIvT6pR2jBLimy4bsQD9rYH5Ik9lfFJNQDsLrSVbKfGQVTWItKp-9WNo3j155GoIRsWfpBPNaYE6AV8WYAAih3RhDxjBg6KjSATHzt6xpX_lYlkmy3KfPflMYkjfEhnwVdbWqtTbjac_n8tbYWahUobrj6xvaAolPUY5cqrS1X3n4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/274b445379.mp4?token=AoH_-GVDDX9fNng87_DjjYiv74rzfspMuiDk6JhK-bUyT-e1mKKMFvhn9aPGGykzLG6s3VoRIxCk3RFl1CdJnUaOO2sDScaCm8oa48VSCzkgjW49GKRFIZqgo90Ifmcp79KEE-ED7-GYMWzQIAUMDVwSmDkaraOySmeDmdYRRIkaLKrJdIcm3C9W_p9pApt7ivvN9yO3SZQt6SIIsnqQx3bDtPG_Lz8Z2s59bimwckGryFR31D9YZb3znHmBR2CWA2FujxCu9nJ97a2ew_9zQMV3w_4-_agQRR65rwNuU0wh_EiDQ2Zs2zw0U-PNBNOBBsiUx-5DXulxFbZLzPDtU2l6FvWe9xwwGHa6_OfYN_rbfGCBMXYmarcu3MdcGzqhjpHP_cc-Rjpd9v_WFLKWIJHed_Ytl-xgzpASw9SnafnEvTuJCRCVGHbJpWT9I1j3SU1fJjTw6TkLmMfLRFHyEh4R0QyGfaIcit8AXZQZp0vYwGiXO_EkUVRE6Rd8t_LIvT6pR2jBLimy4bsQD9rYH5Ik9lfFJNQDsLrSVbKfGQVTWItKp-9WNo3j155GoIRsWfpBPNaYE6AV8WYAAih3RhDxjBg6KjSATHzt6xpX_lYlkmy3KfPflMYkjfEhnwVdbWqtTbjac_n8tbYWahUobrj6xvaAolPUY5cqrS1X3n4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محمدرضا باهنر: احمدی‌نژاد و روحانی نفوذی نیستند/ ادعای ارتباط احمدی‌نژاد با موساد، توطئه دشمن است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/akhbarefori/691830" target="_blank">📅 23:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691829">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
عراقچی پس از توقف کوتاهی در قطر برای شرکت در نشست سازمان ملل عازم نیویورک شد/ تسنیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/akhbarefori/691829" target="_blank">📅 23:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691828">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af441ab91b.mp4?token=iqULHrz-wNluKsb2-khCX2pgwfQH0CKRZheJ8FMo3VVt0AsQNWTWhs8piYa0jIUQm1n4gK9buNz51M34LmiaU3gRoyxdRDTe3U4TrB5F9QyRxW7oSTZaO6a_AFjzNUREtjxtPBY73L1W_RXl9dIGEtFP7IErPVydjocoAI8EexfVRldqZzDdS9zwDj9DuD6eZFTarTqDIzfTW-nYauzLCnXa024xAhHn8Io75jtJf91P8JUzfJ7N458kqU3jRajH3oE4P7jUgpnSRSDnzZznS_C7T4ycBr7L0SHeCJ49JeyE-NL5hFsC4faN53yl7sZYVHgs03FYLBMGIQj6opa2Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af441ab91b.mp4?token=iqULHrz-wNluKsb2-khCX2pgwfQH0CKRZheJ8FMo3VVt0AsQNWTWhs8piYa0jIUQm1n4gK9buNz51M34LmiaU3gRoyxdRDTe3U4TrB5F9QyRxW7oSTZaO6a_AFjzNUREtjxtPBY73L1W_RXl9dIGEtFP7IErPVydjocoAI8EexfVRldqZzDdS9zwDj9DuD6eZFTarTqDIzfTW-nYauzLCnXa024xAhHn8Io75jtJf91P8JUzfJ7N458kqU3jRajH3oE4P7jUgpnSRSDnzZznS_C7T4ycBr7L0SHeCJ49JeyE-NL5hFsC4faN53yl7sZYVHgs03FYLBMGIQj6opa2Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای ویدئوی جنجالی آناهیتا افشار چه بود؟
🔹
این ویدئو بخشی از یک کمپین تبلیغاتی برای یک فیلم سینمایی بوده و ماجرای انتشار فیلم خصوصی واقعی نبوده است
🔹
این شیوه تبلیغاتی واکنش‌هایی نیز به همراه داشت و برخی کاربران از اینکه ویدئو در ابتدا به شکلی منتشر شده که می‌توانسته مخاطب را درباره افشای واقعی یک فیلم خصوصی به اشتباه بیندازد، انتقاد کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/akhbarefori/691828" target="_blank">📅 23:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691827">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M80r0WMn74vvYg0LP_Qbr45rTQ4b7Myvp7wrIm9KsfXs6k6jBeulIKjuDhrqfGn5qe7BOuLHBSKBUERrh5OH38wIJBJXXgou5qJAPhQuGB-rM5NDUAjQNFH77ftsWX9EiszwTbBPtlvicqE-CizjyFxG5binoV_1G2OwZKGmINvqFXBevCATAMBDG7F-AUUBsF4boVwOiqb9igj4ThtWfMR3Lwve9G9M5WtgwlubTGvrkgLI3iPAgKypQCwCO_kSCHQa25oPAtW8-HVRaexVe4hmxvPg5UoeHQl6PpmDV9XODtdvDoT93RzOHLDinaGGGvkB47HkRwbhYcrHSCKSoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترس از آینده ریال؛ روایت یک سیاست کم‌اثر | چرا دلار دولتی نتوانست ترمز بازار آزاد را بکشد؟
🔹
دلار در بازار آزاد در محدوده ۲۲۷ هزار و ۵۷۵ تومان معامله شد؛ رقمی که نشان می‌دهد عرضه ارز دولتی تاکنون نتوانسته مسیر صعودی بازار غیررسمی را متوقف کند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3246934</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/akhbarefori/691827" target="_blank">📅 23:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691826">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nez8DDD-FYSa0LNUTa6Bdd_9QJC2Pu8z7m0pMX-vi5OAhROh3QJEhYrs5ZlhT3NP7Ki2f62QxPH3qvqSiwI61S8lfpaIqPH7WZQ3o_qe0-g5Xoxhobvxvo186_DeviAnX31Rv70d-jby1QEb8hwey-BiMs3AKMJdjIHlV8CKMFwYbY4CC9xRGxa5OjNPADPp3SGU-eGz9u3LNAAutXBdb3DEqCqVjbsS0Mj8PlWGeVYHzUSXEmYs7zaIa-94uYbgJPrAYzgyKEOY3SC5YIYNbmw9VulpUXY-gYTNxLEbvNNbUce0MgrtIMQTpfGz8XayLDzO2FrbuRXQbJ9GysGGAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از روز اول مدرسه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/691826" target="_blank">📅 23:38 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691825">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
ویدئوی عجیبی کاخ سفید منتشر کرده؛ ترامپ سکوی جدید فرود هلی‌کوپترش را افتتاح کرد!
🔹
ترامپ مراسم بریدن روبان برای سکوی جدید فرود هلی کوپتر جدید کاخ سفید برگزار کرد، اما اظهارات او به‌طور کامل به دلیل سر و صدای بالگرد که بر مراسم غلبه کرده بود، شنیده نمی‌شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/akhbarefori/691825" target="_blank">📅 23:38 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691824">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FK936RPUJxudcvCQhxg_fe85V5Y-xPswJYtnzTWjGQHS_EUbrvGKu1TWINYdNUU9xt0g4Tg5hMbvBoV0YC77buMUqIdbWVSR70GbG7o7xX9_Eb3gTh-Gx-YqZ3vkw9GoLuSDWmEkJCq_IGsdX9HPHtbvhxoqAvW3A51RJMe0liQcDHAPQR6RuOXd_KS_QLi7O8drkujXg24Zi0dARvLPRVxECkMPToCJ9X5jUUZ1AJkRJw3XwKn5RdhazLxQt5D4to6fFoqvjkFgP6G-lH3_Jt9kgtkYW5QSBmWshMmqYnD7EKcyah5EaefO1ANrMCC5_DwnFkTbSPLrLBc0YL_WMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هواپیماهای سوخت‌رسان آمریکایی در نزدیکی تنگه هرمز
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/691824" target="_blank">📅 23:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691823">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔹
خبرهای منتخب را هر لحظه در وبسایت خبرفوری دنبال کنید
🔹
🔹
شی نورانی ناشناس مشاهده شده در آسمان تهران، بشقاب پرنده بود؟! | شما نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3246809
🔹
جنگ نزدیک‌تر از همیشه | منطقه در آستانه یک رویارویی تازه | آیا نیویورک آخرین فرصت دیپلماسی است؟
👇
khabarfoori.com/fa/tiny/news-3246818
🔹
محمدباقر خرازی آزاد شد؟
👇
khabarfoori.com/fa/tiny/news-3246774
🔹
داستان ملکه عرب که با بشار اسد درافتاد، تبعید شد و به دمشق بازگشت | اصاله نصری کیست؟
👇
khabarfoori.com/fa/tiny/news-3246666
🔹
بازیگر مشهور بازداشت شد
👇
khabarfoori.com/fa/tiny/news-3246931
🔹
صفحه ویژه اخبار پربازدید خبرفوری را از دست ندهید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/691823" target="_blank">📅 23:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691822">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0155b55335.mp4?token=HNOp6hxH-VZY6kV1I_Vr4v4-0w7D10mE_Sn8RfXKezzr9IIccvBKJEZ4iOKB9RotLcq_1ssQ8SNw5AAiuImPMVz4rlTb5mg-M4itYwjNe1Mgz-ZPTjg1sudJ5ggaUglveop8sfOESGARXDF5lytX1y5OrAbiuYkL9xiWop6nz9cEIBRHZtipcn4h3oR9ziUqOb9SEOrlqhMm8lSMdk4QNgjRA2RUK-J1QKdzBleBmTVqxyy_cdTE2h0VF3G8-kL3naI6KIJWbC0w2vVPhN4IA2YKqUQsw34w86M7sOeixNPBMjwx5cFAaIVZiRIWtGvfDEzg1JOAgebGd9cCmGZeVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0155b55335.mp4?token=HNOp6hxH-VZY6kV1I_Vr4v4-0w7D10mE_Sn8RfXKezzr9IIccvBKJEZ4iOKB9RotLcq_1ssQ8SNw5AAiuImPMVz4rlTb5mg-M4itYwjNe1Mgz-ZPTjg1sudJ5ggaUglveop8sfOESGARXDF5lytX1y5OrAbiuYkL9xiWop6nz9cEIBRHZtipcn4h3oR9ziUqOb9SEOrlqhMm8lSMdk4QNgjRA2RUK-J1QKdzBleBmTVqxyy_cdTE2h0VF3G8-kL3naI6KIJWbC0w2vVPhN4IA2YKqUQsw34w86M7sOeixNPBMjwx5cFAaIVZiRIWtGvfDEzg1JOAgebGd9cCmGZeVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه‌های عربی مدعی شدند:عربستان در مرز با عراق بالون جاسوسی مستقر کرد
🔹
گارد مرزی عربستان اقدام به نصب و به پرواز درآوردن یک بالون ویژه رصد و جاسوسی در نزدیکی مرزهای عراق کرده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/akhbarefori/691822" target="_blank">📅 23:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691821">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
نتایج آخرین نظرسنجی ان‌بی‌سی‌نیوز: ۶۲ درصد مردم آمریکا جنگ با ایران را «بی‌ارزش» دانستند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/691821" target="_blank">📅 23:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691820">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad8df78991.mp4?token=t3oZ1wbsObck3Zx1s13mXCEsGfv47WH3-bgS9o9LEWqQ98p4b1uXK44yfp_F-Yv2QnSD6wOFTng5aw8iIpKgvmBJchQr7Ygcr9LDrB37UESsYnrKGkzxnBrxRZcumwDGQKgNYdjLvQzvuf3pNNRJdRjDj8dOWv33_UorTS_sd7CjlUpPFSRmcuqICw7CO-eY4NfuLXVO-FibeiyHOPSq0xfIRMZNAke7JhxbYMqbr3VVfKZYbcXhSk8rdrfm3QNIYfraF9ZGvCdfLta3ywZ8FWKcEVoktp26X35J5bhG42q5FkqnqAdDgJnTW47i50QKgRL2FvhRuA8B4pZnVamY-gXrua2MtplU6DsteQrCmu-Lp9hcyw0XaAhszKVUkYVsd4HRvGzxdFoxhKr5WSZxBsN5unAu8jdkkzZB9-Z2u9ytbytqLH80BE5AFjC6X6ubpgejaeZiIrEzE3sp1Dql2dG0cl_1qj7Jab69cNEBAOs6NyUmTuE5qZ2bIkiHS25uZYmSEiTA2T7TuXL4DtsRyq8qpIJRDkcSl-4Avb9rT3nRFTjyL6EUQbRqH1jCjTF5I-wA5d22AKQeegBKmCXj3p0oWFXGc9sT5vtIx0p8WXxioL4qPtCpXU2LG9uN7Jx9ZebsjlxoKdXgEpfqdkQA6NXXvGf6sVyE5bNJlApfw2M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad8df78991.mp4?token=t3oZ1wbsObck3Zx1s13mXCEsGfv47WH3-bgS9o9LEWqQ98p4b1uXK44yfp_F-Yv2QnSD6wOFTng5aw8iIpKgvmBJchQr7Ygcr9LDrB37UESsYnrKGkzxnBrxRZcumwDGQKgNYdjLvQzvuf3pNNRJdRjDj8dOWv33_UorTS_sd7CjlUpPFSRmcuqICw7CO-eY4NfuLXVO-FibeiyHOPSq0xfIRMZNAke7JhxbYMqbr3VVfKZYbcXhSk8rdrfm3QNIYfraF9ZGvCdfLta3ywZ8FWKcEVoktp26X35J5bhG42q5FkqnqAdDgJnTW47i50QKgRL2FvhRuA8B4pZnVamY-gXrua2MtplU6DsteQrCmu-Lp9hcyw0XaAhszKVUkYVsd4HRvGzxdFoxhKr5WSZxBsN5unAu8jdkkzZB9-Z2u9ytbytqLH80BE5AFjC6X6ubpgejaeZiIrEzE3sp1Dql2dG0cl_1qj7Jab69cNEBAOs6NyUmTuE5qZ2bIkiHS25uZYmSEiTA2T7TuXL4DtsRyq8qpIJRDkcSl-4Avb9rT3nRFTjyL6EUQbRqH1jCjTF5I-wA5d22AKQeegBKmCXj3p0oWFXGc9sT5vtIx0p8WXxioL4qPtCpXU2LG9uN7Jx9ZebsjlxoKdXgEpfqdkQA6NXXvGf6sVyE5bNJlApfw2M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مقایسه زوم گوشی‌های Galaxy S26 Ultra و iPhone 18 Pro
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/akhbarefori/691820" target="_blank">📅 23:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691817">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YZsb-WTU60oX2fVXnwu6uxrNjMndbkvsANgezNCLtID68nBEGgE4DZ4D1rpjamNt3g95KA8RMET8uQgopM2M2ThE9xryMtDl0bMCy3Z913F0kUbYrUUaST_x7N-T-7EODLZNwCiyS3v6iFfhlq7fSO0x3-2igqmZS2ohTUHNHNuAOeuwiyWyyzqaz5-k4OlNyOwMMMbDEbkgregW0ztVdDURXRx3Q3hyDCLoWilCgdAnQbaonflYQ2jaM2PuTFJ0TDX_YPPpSy_Jh812jjUv2Ws-4xavPb_VM1HqSBAs7ChY1x8VPY1bPgu0S5IIkweawkguo2JjyTbcSjY5i6tX4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K83MdvSSISpXN8i0z8TOM3UXxJE-2Ol7prRS6K5AaBeDYZ-amcskvudx8DFmpwPNk0wsVOlhVyfFMC-IMW26zJ4SppxEH1xhfNaOBKkgzylKoDQtWQvdY9Noz9qUVv-0aSB4Ewqr5wMEzAV9msvBPD-5vOutEDJGx3B3vIkqCe-huOeN5oddgAAA1tUErLuVzZeQj-f3IWqCQpCqRyAeXQx6HYheNBG_hTC4Dd-P6nSFlUdiSOZidLZCw4aKTmCs1ucFV20Q_Ac-Kp8-3mEMYDyMJIwkVmCDqHbNe4iWcCgnUdalJPsRYLqEYxwu5sK2zSFGOmMBp9j4S08moghr3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i628xhg-703gIBw7A6IaeLxJFsIYr4_ga--qJRuDaNdziVEf_XJdx8-G5TU3DkJ8SDZr4OwUn4PbJx9OtqGzhVYYHkmnn2F-pRkjWXC7McI_kUdKQNNrnKnYdZIJW4bwBaJbCP1ri9_UvptvxO8j-xQSCdnqEoXNAudM61aCKfpVmCISa0-R6--XzfNmw7aoZVzFjFhhqAAI_Fa927sNdST0ZlDpF_HvUiWFhz4Esiy--Zu_2IkZiOm95s3_vueMQAO3vzcMA-PT0F85IDbnBvMFl9Ul3sgrAIYfl4aSEC8ySv2W2wvsg_SpilDwVZdPQdVKTZSLkpERKbks7QlIQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
وزیر ارشاد: کتابخانه‌های سیار تا پایان سال دو برابر می‌شوند
🔹
سیدعباس صالحی، وزیر فرهنگ و ارشاد اسلامی، از برنامه‌ریزی برای دو برابر شدن نقاط استقرار کتابخانه‌های سیار تا پایان سال خبر داد.
🔹
او در آیین بهره‌برداری از ۴ دستگاه کتابخانه عمومی سیار گفت: در ابتدای دولت چهاردهم ۵۷ کتابخانه سیار فعال بود که با راه‌اندازی ۴ دستگاه جدید، تعداد آنها به ۸۲ مورد رسیده است. همچنین حدود ۴۵ خودروی دیگر آماده تجهیز است و امیدواریم تا پایان سال تعداد نقاط استقرار کتابخانه‌های سیار به حدود دو برابر برسد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/691817" target="_blank">📅 23:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691816">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/428d5f3794.mp4?token=G0zCPzwhSOq-Rv-rjV84rmVHMpuNC_ssm4T4iAIbMXZrzjV2GyB_15cXMm97eVMnTKHweq2dLYveNejI_hCJYJutqFCEWOnyPuAn2m7br8Al0ilKtUcuY4_dC3oatGxnZvAkrEUvGd2HyiS9PSqFqKlKgSCn8RzSBSUjme8rSjxChb7QilBDopDPFg2x1F-3EecLcJ1yuTLyrMut71THsNue9yWqhAHL_ppGFLkB-BBip2hsBC2M540gxQdZhqz5--ZX3kOOf0Dufo8q4dVzBdwljr3f58cCKcZzefEu2j449nu86z48kV6hxcy8-iBI21M4G-e6FyVRGS50qCjvmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/428d5f3794.mp4?token=G0zCPzwhSOq-Rv-rjV84rmVHMpuNC_ssm4T4iAIbMXZrzjV2GyB_15cXMm97eVMnTKHweq2dLYveNejI_hCJYJutqFCEWOnyPuAn2m7br8Al0ilKtUcuY4_dC3oatGxnZvAkrEUvGd2HyiS9PSqFqKlKgSCn8RzSBSUjme8rSjxChb7QilBDopDPFg2x1F-3EecLcJ1yuTLyrMut71THsNue9yWqhAHL_ppGFLkB-BBip2hsBC2M540gxQdZhqz5--ZX3kOOf0Dufo8q4dVzBdwljr3f58cCKcZzefEu2j449nu86z48kV6hxcy8-iBI21M4G-e6FyVRGS50qCjvmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر جهاد کشاورزی: «از جنگ ۴۰ روزه تا امروزبرداشتی از ذخایر راهبردی نداشته ایم»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/691816" target="_blank">📅 23:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691815">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgZZ2OTAX_J4J7EaFQgtyAMzl6MXrSi0vs9AcryWiMJotBq7-4JyTjpky-givHpNX9hHhbxZHhgkA3DfS6Hbu8Q74Akgtuy3qe5HfLsMqMyr9A_8Fj0NP0TannDNko5nhC5JsYmZuX2yod6vUHQVxHYItx2SX4VBdLuVe3HX8xF1tOEjW3wasc4voP0tYOKmu8lFwj9Zy5YX5uvWT5Na5XG7J5lSeeT3n6NvS5_zGFUZWNZI0H9ppQZbmQR4yrcuRL77G0FibvneHdUYxHLwTH9Lwz4N77g7XRCL_wz5V3bhrdytpMJwOBejoC2V9kyeGcd67XEH51wB2Cq_byScJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قابی از طواف پیکر پاک رهبر شهید انقلاب، بر گرد حرم مطهر کریمه اهل بیت حضرت فاطمه معصومه سلام‌الله‌علیها در آسمان قم.
۱۴۰۵/۴/۱۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/691815" target="_blank">📅 23:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691811">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNSyQh3pWnUD5V8Uzm_eGDezACsBvo7ACNVh8TbZ5NkFVC5yTo5mFRQw_U5fAUcZLhjO-R6WvNdh5JyemWlP4zHgz-1H_qaWemo17JSfqc_hrl8zohuIW1IpQbxcAn6ToZ6XcYRrgGMBN76Vzyj8SkvnAJgFvFZ2Vu5upMiu1uo6Wv6J6zl8B-R8BpR7z5oTC46oiBcx9m-Af42TORi6lrrCquq3rTn0HyqxLgn1y_Du8whEy8ljnLdYQspLUWX_DpxIoKhY-gM5D5ND6RB-DOB_1H70Pic9p121cYcpyv0Ahvjf0B7hSysMKqslKB_qxDx-WvajXMxFwCMV4btmsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جشن فرشتگان
🔹
زنگ مدرسه دوباره به صدا درمی‌آید و دانش‌آموزان راهی کلاس‌های درس خواهند شد اماچند صندلی برای همیشه خالی می‌ماند، صندلی‌هایی که در میناب و در مدرسه شجره طیبه صاحبانشان باید با کیف‌های کوچک و لبخندهای کودکانه وارد کلاس می‌شدند، اما در پی حمله آمریکا معصومانه به شهادت رسیدند. امسال نخستین روز مدرسه با یاد شهدای دانش‌آموز مدرسه میناب آغاز می‌شود؛ کودکانی که از کلاس رفتند، اما از خاطره مدرسه مردم ایران هرگز نخواهند رفت.
🔹
هشتصدوشصت‌وششمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/691811" target="_blank">📅 23:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691810">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c09d73eb4.mp4?token=dIqr-RdT1SUvcWsFTtgFS_8gKpRG3ajN8NQVDLKSY-LUy7CJDODf1C305k4KiSsHyYrnKtZxfJndBLveBIX8BaPKoyp3XqDsDWnXcSdvG30m3H0l0YNM8PsrLXWf25jFvXNZr0Gz3GcYSEVgJ78JJJmw4GNlHjaNaQErtSNnx8rwQ0j4-hogDjpT9x64C8Prace90aadN7SXuB0_qfPkS4XBM71iX4LEh1AJTVEr3V3im1SbAftNtbEEQU6UUdfUn-Sc0gbXwPtmj202T_QzXZBJbhgWP3ouZn5o88fCJ_RIgnTs7ky1Biazku7kiGS0QvyP1BI2hS8R4a5NN1t7HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c09d73eb4.mp4?token=dIqr-RdT1SUvcWsFTtgFS_8gKpRG3ajN8NQVDLKSY-LUy7CJDODf1C305k4KiSsHyYrnKtZxfJndBLveBIX8BaPKoyp3XqDsDWnXcSdvG30m3H0l0YNM8PsrLXWf25jFvXNZr0Gz3GcYSEVgJ78JJJmw4GNlHjaNaQErtSNnx8rwQ0j4-hogDjpT9x64C8Prace90aadN7SXuB0_qfPkS4XBM71iX4LEh1AJTVEr3V3im1SbAftNtbEEQU6UUdfUn-Sc0gbXwPtmj202T_QzXZBJbhgWP3ouZn5o88fCJ_RIgnTs7ky1Biazku7kiGS0QvyP1BI2hS8R4a5NN1t7HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چاه بیست متری حفر شده در خانه خانوادگی دو برادری که اعضای خانواده خود را به قتل رسانده و جسد آنها را دو سال در آن دفن کرده بودند   #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/691810" target="_blank">📅 23:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691809">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qb9ZSnIqy9TiEWypUHf4sB3KQVJH8dTmzdgIHdRlYfeK14ivkZI7ITLOpirCGNBH7evlCQ-VsVfwsUdRv6YBqQgAKbIHWqC88ac-uAdgCiDJV7G7MT-ZLkIXBOFqICCOSjwWwjJUEzbwFAi6WpdWIj6sXKuervWzKMrObbCZAIZrJYIFvUs49dvtzbnMCXgP6slCQ7UTjNhc8xAxZANqu7GT8fa4XWFJ4o3xjnFsK1IXSwHup8iagGn1W1ZFnKIiGHoKecnjOk_w9ui1kVCKjlAMo8hQOmy-ENug_y423tjYb0kRN17CQgWlgm7Qlqwx4J3suWblrcyo8S-tO-2OcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شوک به چین؛ ذخایر نفتی ریخت
🔹
ذخایر نفت خام شاندونگ چین در ژوئیه ۳۵ میلیون بشکه کاهش یافت (بزرگ‌ترین افت ماهانه از ۲۰۱۶)
🔹
شاندونگ محل پالایشگاه‌های مستقلی است که نفت تحریمی ایران را می‌خرند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/691809" target="_blank">📅 23:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691808">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">گذر از دجال-جلسه دوم</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/691808" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
دوره‌ گذر از دجال
جلسه‌ی دوم:
تفسیر دعای توسل
🔹
انسان باید از توجه به منفی‌ها، نقص‌ها، غیبت، اخبار بد و عیب‌جویی دور شود و توجه خود را به خدا، اولیای الهی و نعمت‌ها معطوف کند.
🔹
توسل در حقیقت نزدیک شدن به خداوند به وسیله و از طریق اولیای الهی است، نه شریک قرار دادن برای حضرت حق.
🔹
در دعای توسل، دو مفهوم کلیدی، «اعراض» به معنای رویگردانی از امور منفی، و «توجه» به معنای روی آوردن به پروردگار و خیر و نیکی مطرح شده است.
🔹
غیبت و عیب‌جویی خطرناک‌اند، از آنجا که توجه انسان را روی نواقص دیگران قفل می‌کنند.
🔹
دعای توسل در حقیقت، دعایی برای ایجاد اشتیاق، رغبت و اتصال قلبی به خداست.
🔹
بهتر است انسان در دعاها بیشتر به آخرت، عاقبت‌به‌خیری و نزدیکی به خدا فکر کند.
🔹
نجات انسان در آخرالزمان از مسیر توجه قلبی، دوری از منفی‌نگری، توسل درست به اهل‌بیت، و آخرت‌محوری می‌گذرد.
🔹
ایران خاستگاه اصلی یاران امام زمان (عج) است و سختی‌های فعلی نوعی صیقل دادن برای رسیدن به آن نور عظیم است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/akhbarefori/691808" target="_blank">📅 23:01 · 30 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
