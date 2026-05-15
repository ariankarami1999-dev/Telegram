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
<img src="https://cdn4.telesco.pe/file/h3kEKV1g-DBCh1LL5Pn8OoBGPJlLpPtovy2nA-0yvA2oDK4dJgJ2t2prDP3TpJFy8S3I2H8ePkxHQr45HAOJnWsfJMMMpWaeFcPsr0JNL4__twBkQnsfoEh02x7o84jGpB4RVuuyNmKUrPkGbJiOdA9gkbs5so5V2EQ5iLvdfkLQ_c48T_WnvyAsEk0_3QDjGIRkU68YjtWDlgn_BXsnfftkHvz7ZvlSDyJ7Xeu-w_FZVuht5CtmAqXAreA_LI4o0_nPCCGFxTT1OTFA7c3bgoDS3n3wTEH-6u12iMc599nHO9xgWlHaZ3ghwY8TiSXyEAYueJP5pCR62YabZg3wDg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 956K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-25 15:58:03</div>
<hr>

<div class="tg-post" id="msg-120186">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d4205c201.mp4?token=qXglAhO6e4RGCsiQ2DUAWIETAO_psBhYQCb8paaO-JF5esYSsxFGTlnTtbGqBTGu7X1HkE0v_qvIZhgaeOVKL4YZvMw2sPMUNiML-HY5B9XvXB-gtgxVpliJQ5Z_NUmDvjRIxt7cES0W5FT8PlN2QzqTnqFEfgqEdl9GbZFN_J97De5Lr48euI-ntvXcrpEWRJ6Nv9XUY5AP4N6iaZTC3pU-XdwvcqGFOwrZ1oksr8MXnQEHFNsqm4K_uzbUeB_CtDZiiF2-XNLOzDepoqyaY65GOahicuI6y4kQyHHdnMIEXiHJZ53ZPntGTs4Tk2OnJzeN-Qg8wYfww8zdN2C2EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d4205c201.mp4?token=qXglAhO6e4RGCsiQ2DUAWIETAO_psBhYQCb8paaO-JF5esYSsxFGTlnTtbGqBTGu7X1HkE0v_qvIZhgaeOVKL4YZvMw2sPMUNiML-HY5B9XvXB-gtgxVpliJQ5Z_NUmDvjRIxt7cES0W5FT8PlN2QzqTnqFEfgqEdl9GbZFN_J97De5Lr48euI-ntvXcrpEWRJ6Nv9XUY5AP4N6iaZTC3pU-XdwvcqGFOwrZ1oksr8MXnQEHFNsqm4K_uzbUeB_CtDZiiF2-XNLOzDepoqyaY65GOahicuI6y4kQyHHdnMIEXiHJZ53ZPntGTs4Tk2OnJzeN-Qg8wYfww8zdN2C2EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: دیروز از دریاسالار کوپر درباره حمله به مدرسه دخترانه در اولین روز جنگ سوال شد.
🔴
ترامپ: شما درباره مورد اصلی صحبت می‌کنید — که در حال بررسی است.
🔴
خبرنگار: آیا می‌توانید تایید کنید که این موشک آمریکایی بود؟
🔴
ترامپ: شما با چه کسی هستید؟
🔴
خبرنگار: بی‌بی‌سی.
🔴
ترامپ: بی‌بی‌سی جعلی.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18 · <a href="https://t.me/alonews/120186" target="_blank">📅 15:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120185">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
عراقچی: اگه به جنگ برگردن این تصمیم خودشونه، ولی نتیجه فرقی نمیکنه و بازم شکست میخورن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/alonews/120185" target="_blank">📅 15:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120184">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
ترامپ رسماً اعلام کرد که یه دور دیگر از عملیات نظامی آمریکا در ایران در راه است:
ما از نظر نظامی در ایران تقریباً کار را تمام کردیم. حدود ۷۵٪ کار را. (البته) ما همه چیز را تمام نکردیم. برمی‌گردیم و آن را تکمیل می‌کنیم. حتی شاید بیشتر!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/alonews/120184" target="_blank">📅 15:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120183">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
مرتس و ترامپ درباره ایران، هرمز و اوکراین رایزنی کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/alonews/120183" target="_blank">📅 15:41 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120182">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
ترامپ درباره استعفای استارمر: من چنین چیزی نمیگویم
🔴
خبرنگاری از دونالد ترامپ پرسید آیا کی‌یر استارمر، نخست وزیر بریتانیا، باید استعفا دهد؟
🔴
ترامپ پاسخ داد: «من این را نمیگویم. در واقع فکر میکنم او مرد خوبی است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/alonews/120182" target="_blank">📅 15:41 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120181">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
خبرنگار : خب آمریکا که شانسی نداشت. این همه بمبارون رو چرا تکرار می‌کنید؟ ۳۸ روز زدید، آخرشم تغییر سیاسی تو ایران اتفاق نیفتاد
🔴
ترامپ : نه، اتفاقاً ما یه پیروزی کامل نظامی داشتیم
🔴
مشکل اینه که سیاسی‌بازایی مثل تو حقیقتو نمی‌نویسن
🔴
ما کل نیروی دریایی‌شونو زدیم، نیروی هواییشونو نابود کردیم، پدافندشونو خوابوندیم، راداراشونو ترکوندیم
🔴
همه فرمانده‌های رده اولشونو زدیم، بعد رده دوم و حتی کلی از رده سومی‌ها رو هم زدیم. الان کاملاً گیج و به‌هم‌ریخته‌ان
🔴
این یه پیروزی کامل بود، جز توی رسانه‌هایی مثل نیویورک تایمز و CNN که حقیقتو نمی‌گن
🔴
حتی به نظرم چیزی که می‌نویسید یه جور خیانته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/alonews/120181" target="_blank">📅 15:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120180">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5d23a0132.mp4?token=sQ-R5RFck_qiDDlI35awnNpfsZ_9abzEhZNTh3a5UHhO8lQpCICAPHcHrE2G8S9Ko8URqguGXO2Beu943GmB8cgtkZZFimCxfLmFE2cw1MOg56LmXq6YI1ZNyLvWQZmGBWx5wjixZyzanbhDcOZ3dcTw2dutIz7-X5TkR2W2kErUleVkWRdmDsA3Pr3cmCWK40E1Fcpl5Ay4VwJSTEENRbDk8g_-8HBnT4FTlXiOC0yErT7lKfLnXUOYxenRpNNiEJDXkLyeccjdcn4G8tVasqcIQAnBXS-bGkdJ1Iit5olD9j8k4yb6cPI1VcXjuHYl4bIN5dTYabOcoACJ49Y0RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5d23a0132.mp4?token=sQ-R5RFck_qiDDlI35awnNpfsZ_9abzEhZNTh3a5UHhO8lQpCICAPHcHrE2G8S9Ko8URqguGXO2Beu943GmB8cgtkZZFimCxfLmFE2cw1MOg56LmXq6YI1ZNyLvWQZmGBWx5wjixZyzanbhDcOZ3dcTw2dutIz7-X5TkR2W2kErUleVkWRdmDsA3Pr3cmCWK40E1Fcpl5Ay4VwJSTEENRbDk8g_-8HBnT4FTlXiOC0yErT7lKfLnXUOYxenRpNNiEJDXkLyeccjdcn4G8tVasqcIQAnBXS-bGkdJ1Iit5olD9j8k4yb6cPI1VcXjuHYl4bIN5dTYabOcoACJ49Y0RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار : در مورد ایران، دقیقاً قدم بعدی چیه؟ دوباره می‌خواید با تهدید بمبارون فشار بیارید؟ چقدر واقعیه؟
🔴
ترامپ : نمی‌خوام بگم فلان ساعت و فلان روز بمبارون دوباره شروع میشه
🔴
فقط اینو با اطمینان خیلی زیاد میگم
🔴
ایران هیچ‌وقت به اون چیزی که می‌خواست نمی‌رسه و قرار هم نبود برسه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/alonews/120180" target="_blank">📅 15:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120179">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
مذاکرات بریکس بدون بیانیه مشترک پایان یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/alonews/120179" target="_blank">📅 15:19 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120178">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
آسوشیتدپرس گزارش داد دور سوم مذاکرات لبنان و اسرائیل امروز در واشنگتن آغاز شده تا دو طرف درباره آتش بس تازه، کاهش درگیری‌ها و مسائل امنیتی جنوب لبنان گفت وگو کنند.
🔴
لبنان خواستار عقب نشینی نیروهای اسرائیلی از جنوب این کشور است، اما اسرائیل بحث خلع سلاح حزب الله را جلو کشیده. همین موضوع گره اصلی مذاکرات است، چون حزب الله پشت میز حضور ندارد، اما بخش مهمی از پرونده امنیتی لبنان به آن گره خورده است.
🔴
این مذاکرات برای تهران هم پیام دارد. هر فشار تازه روی حزب الله، یکی از مهم‌ترین بازوهای منطقه‌ای جمهوری اسلامی را محدودتر میکند، آن هم بدون اینکه تهران مستقیما در اتاق مذاکره باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/alonews/120178" target="_blank">📅 15:11 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120177">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6bdaf1c06.mp4?token=ZtISXqzmeIKd7UzB-F8P2_2_wRKPDzSTekfkg-b4U7BsnRWZw1MvRLOewGnOg8gu67GyJ0-EjHt-rorK3HOZztcV9V8sFtodLXgsMnsDZJ8s7zKk78xbUgnokVCz2KdadtwKI4mm8Obh7WZj1PN2WCWZvpn5wSv6HqOeF1gEK3cjwnWi8snuC5fsI1yk4IhcFZC4bk0tQ_b-F3-sMgePo6_X7CTcXk8N-U4tCknW8Rm2OSHFZafV-tn6HIm42cvcKJcYG8nmyiK0FF9qsuTl429NnqoWakgQk9Rbc08MOoUzM1p8V10lINyrcuydxQvZqIS4izcsRwcozS6xto37sFDLpeefxPpwORCLgfsOr_Y-P-vyxrqlO0NNx9IDsuDqDXYyxtWgvAq0JsU_m1WUP983_o4iu6NTrPZaYYztRpG5Bi8Jzd2tMOLUPVB5AjxNF8GH8W2n6ebaVppQl1bg6Eu8IP6HH1U2eFj132Lpm2I8lNF_z-bC8kZ-iF7XP8movcwh7u__AgLsjQZDw0Nlno_r3bz7ie8mFbhb0xTx8MfYcI5e1UMHLnmSChKAG2yYdy7scPM62e3mRzIqu_jITB7j1HLH1V2M1iQO1AFJntbXL5XVXiYdFCcWD6nlh9lD1wqX_brB1axbO4Q9E_ENtmVCbqi5StDlKjCdbEvIqqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6bdaf1c06.mp4?token=ZtISXqzmeIKd7UzB-F8P2_2_wRKPDzSTekfkg-b4U7BsnRWZw1MvRLOewGnOg8gu67GyJ0-EjHt-rorK3HOZztcV9V8sFtodLXgsMnsDZJ8s7zKk78xbUgnokVCz2KdadtwKI4mm8Obh7WZj1PN2WCWZvpn5wSv6HqOeF1gEK3cjwnWi8snuC5fsI1yk4IhcFZC4bk0tQ_b-F3-sMgePo6_X7CTcXk8N-U4tCknW8Rm2OSHFZafV-tn6HIm42cvcKJcYG8nmyiK0FF9qsuTl429NnqoWakgQk9Rbc08MOoUzM1p8V10lINyrcuydxQvZqIS4izcsRwcozS6xto37sFDLpeefxPpwORCLgfsOr_Y-P-vyxrqlO0NNx9IDsuDqDXYyxtWgvAq0JsU_m1WUP983_o4iu6NTrPZaYYztRpG5Bi8Jzd2tMOLUPVB5AjxNF8GH8W2n6ebaVppQl1bg6Eu8IP6HH1U2eFj132Lpm2I8lNF_z-bC8kZ-iF7XP8movcwh7u__AgLsjQZDw0Nlno_r3bz7ie8mFbhb0xTx8MfYcI5e1UMHLnmSChKAG2yYdy7scPM62e3mRzIqu_jITB7j1HLH1V2M1iQO1AFJntbXL5XVXiYdFCcWD6nlh9lD1wqX_brB1axbO4Q9E_ENtmVCbqi5StDlKjCdbEvIqqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره دیکتاتور بودن شی: این را شما باید تشخیص دهید
🔴
خبرنگاری از دونالد ترامپ پرسید آیا شی جین پینگ را دیکتاتور میداند یا نه.
🔴
ترامپ پاسخ داد: «او حاکم چین است، رئیس جمهور چین است. من به این موضوع فکر نمیکنم. شما با چیزی که وجود دارد طرف میشوید. من به او احترام میگذارم، خیلی باهوش است و کشورش را دوست دارد.»
🔴
ترامپ در ادامه گفت: «اینکه او دیکتاتور هست یا نه، چیزی است که شما باید تشخیص دهید.»
🔴
ترامپ در برابر چین، انتقاد حقوق بشری را عقب میگذارد و بیشتر روی معامله، رابطه شخصی و مدیریت قدرت تمرکز میکند. برای پکن، همین ادبیات یعنی واشنگتن فعلا دنبال درگیری لفظی تازه نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/alonews/120177" target="_blank">📅 15:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120176">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
فروش کانفیگ متصل پایدار با ساب و مورد تایید مجموعه الونیوز
⬇️
🔔
@FastProxyMakerBot
🔔
@FastProxyMakerBot
✔️
با خیال راحت و بدون دغدغه خرید کنید</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/alonews/120176" target="_blank">📅 15:07 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120175">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
عراقچی: این جنگ، جایگاه و اقتدار ایران رو در دنیا ارتقا داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/alonews/120175" target="_blank">📅 15:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120174">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxZoSi8OMass7_iPc4w7IJ7555TLyW2WwrdPjMf54I_En2FSc_u367FIPVwQWthXO40_GL3b0TphgZrsw_ytFNPWG51IA8fHCJXkmMmMIFh148v2HLNZZdz64z8uZZWlPPy8DD8xmk0UwoyGHpFpAdsG_Ygdiu8_SvtpnadThzXIAm57siLEj7xZmPJW5_32OdIrFBWW6X6ie7rQ-fKaWuFxFUZqs5_YAlih0PqIEJANOXxwIQuQXlnd72ebRR1TAxJkShKn77RjcPep6YGJSMbUU32XLLK19wezAUtuiftbCskYQN-rSzLum_16e_t5UMJ4nf2kewx0Eb54fpkK8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ: درخواستی برای باز شدن تنگه هرمز از رئیس جمهور چین نداشتم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/alonews/120174" target="_blank">📅 14:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120173">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
عراقچی: موضوع مواد غنی‌شده ما مسئله‌ای بسیار پیچیده است و اکنون با آمریکایی‌ها به این نتیجه رسیده‌ایم که چون در این مورد خاص تقریباً به بن‌بست رسیده‌ایم، بهتر است بررسی آن را به مراحل بعدی مذاکرات موکول کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/alonews/120173" target="_blank">📅 14:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120172">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
ترامپ به خبرنگار نیویورک تایمز:
پوشش نیویورک تایمز برای جنگ ایران نشان دهنده خیانت بزرگ است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/alonews/120172" target="_blank">📅 14:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120171">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👸
سفر رسمی علیاحضرت شهبانو فرح پهلوی، به چین سال ۱۳۵۱ انجام شده است.
🤔
آن زمان، چین فقیر بود و ایران ثروتمند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/alonews/120171" target="_blank">📅 14:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120170">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Om7izPOkHHIZ73MHeqSLt6mKnPiRSzOsjTAlV7thDL1KIlObGJG4tk8oatOpgxWkqoyXNTYFpaVGPfw7ue-eIsgpLfa745Sozlv6zssMrO2R4A_R4UNBxRtEGhBiEw_XjxYAROP5QX44MMetq61ZYbaJlJyVWSo3lWqG35BhUONd-IIqxtNWzCYh-k5rZlDgZzEFCtkK0NLc6y8E6fL8lXbbaMDNKfZaruuYqU761zD3uMHDeWz-24d65WjVCLIwaxfWiDFXS1_KeVglZ1QO0j2BT5PxEWnuIv3oXF5YFA4DZROgDWtd2ezIf2hBNNEAUD7DnGyhfM36piCkFUCo-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل دستور تخلیه به ساکنان: عین بعال، الخریب، الزراریه، عرب سلیم و عرب الجل (صیدا) در جنوب لبنان صادر کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/alonews/120170" target="_blank">📅 14:53 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120169">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
ترامپ: اگر 9 ماه پیش از بمب‌ افکن‌های  B-2 استفاده نمی‌کردم، ایران اکنون می‌توانست به سلاح هسته‌ای دست یابد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/alonews/120169" target="_blank">📅 14:49 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120168">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
ترامپ: به رئیس جمهور چین گفتم در مورد پرونده تایوان صحبت نمی کنم
🔴
چینی ها عملیات جاسوسی انجام می دهند و ما نیز عملیات جاسوسی انجام می دهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/alonews/120168" target="_blank">📅 14:48 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120167">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
ترامپ: میتوانیم نیروگاه‌های ایران را تنها در دو روز از بین ببریم
🔴
اگر ایران اورانیوم های غنی شده خودش رو تحویل نده وارد ایران میشیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/alonews/120167" target="_blank">📅 14:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120166">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
ترامپ: ما ارتش ایران را نابود کرده‌ایم و شاید باید یک پاکسازی سبک انجام دهیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/alonews/120166" target="_blank">📅 14:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120165">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
ترامپ: وقتی به پیشنهاد ایران نگاه کردم، جمله اول را دوست نداشتم و قابل قبول نبود، بنابراین پیشنهاد را رد کردم
🔴
تحقیقات درباره هدف قرار دادن مدرسه در ایران در حال انجام است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/alonews/120165" target="_blank">📅 14:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120164">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
ترامپ: من به جایی رفتم که شی زندگی می کند، چیزی که به ندرت اتفاق می افتد.
🔴
خبرنگار: اونجا بودی؟
🔴
ترامپ: آره قشنگ بود.منظورم این است که مردم هرگز آن را ندیده اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/alonews/120164" target="_blank">📅 14:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120163">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/701ad40f12.mp4?token=AIiCMkNG3p-NVq721ZXGEnZukLa2P1MfHPGfVXVZYVTHFp_rYtIey-KZoZGh6OKnL99_YyiKdESDLlRSiodpy5iOwjXU4b-lAPuWBmgfqT25qR_xHPRc8O38Pq9jjDvGfAULNJ-B3JBFbKgD4bXpfoGoMtS-OGEottsp9U_4IUkFn9TxK_Dio9BFTzEYw8VcqHmT6-qnPcafCzrALr2Wa14R_u2lNGlyRnR5A7ESrBpXcA3TuClDBgw5zJW_KSIXrnNN53CsuHZpk2B4ithUMjKviV2vLt4kSN-uTaWmOZYEXO1XBOpQ3DLcrwTIgKmhSXg41CH9iswhTPBXmQynTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/701ad40f12.mp4?token=AIiCMkNG3p-NVq721ZXGEnZukLa2P1MfHPGfVXVZYVTHFp_rYtIey-KZoZGh6OKnL99_YyiKdESDLlRSiodpy5iOwjXU4b-lAPuWBmgfqT25qR_xHPRc8O38Pq9jjDvGfAULNJ-B3JBFbKgD4bXpfoGoMtS-OGEottsp9U_4IUkFn9TxK_Dio9BFTzEYw8VcqHmT6-qnPcafCzrALr2Wa14R_u2lNGlyRnR5A7ESrBpXcA3TuClDBgw5zJW_KSIXrnNN53CsuHZpk2B4ithUMjKviV2vLt4kSN-uTaWmOZYEXO1XBOpQ3DLcrwTIgKmhSXg41CH9iswhTPBXmQynTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: رابطه بسیار خوبی با کیم جونگ اون دارم
🔴
دونالد ترامپ گفت با کیم جونگ اون، رهبر کره شمالی، «رابطه بسیار خوبی» دارد و او تا امروز نسبت به آمریکا محترمانه رفتار کرده است.
🔴
ترامپ اضافه کرد که میخواهد این احترام ادامه داشته باشد. این اظهارات در حالی مطرح میشود که پرونده کره شمالی دوباره به یکی از آزمون‌های مهم سیاست خارجی واشنگتن تبدیل شده، جایی که ترامپ مثل همیشه روی رابطه شخصی با رهبران سختگیر حساب باز میکند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/120163" target="_blank">📅 14:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120162">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
ترامپ: 80 درصد از توان موشکی ایران نابود شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/alonews/120162" target="_blank">📅 14:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120161">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
ترامپ : «مواد هسته‌ای» ایران، ممکنه به چین یا آمریکا تحویل داده شه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/120161" target="_blank">📅 14:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120160">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
ترامپ: «من دیگر خیلی بیشتر از این صبر نخواهم کرد. آنها باید توافق را امضا کنند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/alonews/120160" target="_blank">📅 14:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120159">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
عراقچی: پس از اینکه ترامپ آخرین پیشنهاد ما را رد کرد، پیام‌هایی از آمریکا دریافت کردیم که تمایلش به ادامه گفت‌وگو است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/alonews/120159" target="_blank">📅 14:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120158">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
ترامپ: پل‌ها و سایت‌های برق ایران که می‌توانیم هدف قرار دهیم
🔴
ترامپ می‌گوید ایران آتش‌بس را به عنوان لطفی به دیگر کشورها انجام داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/alonews/120158" target="_blank">📅 14:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120157">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
ترامپ: هیچ تعهدی در مورد تایوان ندادم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/alonews/120157" target="_blank">📅 14:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120156">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ترامپ: پل‌ها و سایت‌های برق ایران که می‌توانیم هدف قرار دهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/120156" target="_blank">📅 14:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120155">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
ترامپ درباره ایران: من با تعلیق برنامه هسته‌ای ایران به مدت ۲۰ سال مشکلی ندارم اما باید یک تعهد «واقعی» باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/120155" target="_blank">📅 14:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120154">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c17259012d.mp4?token=BtvIpVphcAO09IFn5hJImpiCEyKTy3zoBlFUIZQtOgsqr5kUFwJPa43JC14dxVO9aI96oH3qRtOBS-RRZNeGVOGzTlyXlgHgiKf3ZPk0vSuQrfE6QDlACjEzS6snixxVOFeSe5w4tIIxdUalANh0TelY66lyqM0yqYqmRRngSatxvoYQdoOR0jLkQeMuqTTuPifEgdnQXYWYzPcTqg0VE8DDyo0E6YF4Qd95Pn5DvPjif7YKHa5plvIjEAoYOZw4IFuRbqPjzAXeS05M2BNHVA7OIm84diQdebjc51fzNgZgsL8jUtx71B_Pi1CUFzs1uQcH2cuQmD3wGtT2vutmMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c17259012d.mp4?token=BtvIpVphcAO09IFn5hJImpiCEyKTy3zoBlFUIZQtOgsqr5kUFwJPa43JC14dxVO9aI96oH3qRtOBS-RRZNeGVOGzTlyXlgHgiKf3ZPk0vSuQrfE6QDlACjEzS6snixxVOFeSe5w4tIIxdUalANh0TelY66lyqM0yqYqmRRngSatxvoYQdoOR0jLkQeMuqTTuPifEgdnQXYWYzPcTqg0VE8DDyo0E6YF4Qd95Pn5DvPjif7YKHa5plvIjEAoYOZw4IFuRbqPjzAXeS05M2BNHVA7OIm84diQdebjc51fzNgZgsL8jUtx71B_Pi1CUFzs1uQcH2cuQmD3wGtT2vutmMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
یکی از صدها موشکی که برگشتن رو سر مردم و جمهوری اسلامی طبق روال همیشه با مظلوم نمایی انداختن گردن امریکا و اسرائیل
🤔
مدرسه میناب جای تحقیق و بررسی زیادی داره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/alonews/120154" target="_blank">📅 14:17 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120153">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
ترامپ پس از پایان سفر خود به چین، درباره تایوان به فاکس نیوز گفت: ما به دنبال جنگیدن نیستیم
🔴
ترامپ به خبرنگاران گفت: فکر نمی کنم با چین بر سر تایوان اختلاف نظر وجود داشته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/alonews/120153" target="_blank">📅 14:12 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120152">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: ممکن است با تامین سلاح برای تایوان موافقت کنم و ممکن است موافقت نکنم
🔴
هنوز تصمیمی برای تامین سلاح برای تایوان نگرفته‌ام
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/alonews/120152" target="_blank">📅 14:12 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120151">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
پیام کتبی سید مجتبی خامنه ای ، به مناسبت بزرگداشت فردوسی: فارسی فقط ابزار حرف زدن نیست؛ بخشی از هویت و اقتدار تمدن ایرانیه.
🔴
مردم ایران تو جنگ اخیر مثل قهرمان‌های شاهنامه ایستادن و مقابل متجاوزها مقاومت کردن.
🔴
اهالی هنر و رسانه باید این حماسه و مقاومت مردم رو برای تاریخ ماندگار کنن.
🔴
باید مقابل تهاجم فرهنگی و سبک زندگی آمریکایی ایستاد و روی پدافند زبانی و فرهنگی بیشتر کار کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/alonews/120151" target="_blank">📅 14:10 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120150">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
عراقچی : تنگه خیلی هم گشاده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/alonews/120150" target="_blank">📅 14:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120149">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
عراقچی:  امیدوارم کشورهای حاشیه خلیج فارس متوجه شوند که آمریکا و اسرائیل نمی‌توانند برای آنها امنیت بیاورند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/alonews/120149" target="_blank">📅 14:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120148">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e412eeab0.mp4?token=se2OJ6V4uhiOYOA0jM-UEYOF296GDVFo31nKOdlQXwEKfodGX5GhceuK4QMvKS-ik-nUK2qnXQ9tTO_lZEYXdhbPu0jHwbRfU5AlSF-qWLADlOWg8cBvRwSikAYsWo_5lMY5k5jDa1dpcP17N7o2WGl0jhgM1ohz0aUuZyfKC83NjPpPmyAY7Qvp8e6J9i-nEZWOQu1mHCzi_8Xfm3LyOGhOMmb-A2XitDc6UPTBzuYuILQFVmiYWvsxAQdfCgBISMQ70FTcVgqIPJqrf-H7qXUh2fbHFYkQtLmK7Tl9hHD6IeRZTarYIAMK84ANQ6wbNTD44BO5wRUHUawYADodDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e412eeab0.mp4?token=se2OJ6V4uhiOYOA0jM-UEYOF296GDVFo31nKOdlQXwEKfodGX5GhceuK4QMvKS-ik-nUK2qnXQ9tTO_lZEYXdhbPu0jHwbRfU5AlSF-qWLADlOWg8cBvRwSikAYsWo_5lMY5k5jDa1dpcP17N7o2WGl0jhgM1ohz0aUuZyfKC83NjPpPmyAY7Qvp8e6J9i-nEZWOQu1mHCzi_8Xfm3LyOGhOMmb-A2XitDc6UPTBzuYuILQFVmiYWvsxAQdfCgBISMQ70FTcVgqIPJqrf-H7qXUh2fbHFYkQtLmK7Tl9hHD6IeRZTarYIAMK84ANQ6wbNTD44BO5wRUHUawYADodDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
نفت به آغوش مناطق ساحلی و جزایر ما رسیده و اینطور در حال نابودکردن است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/alonews/120148" target="_blank">📅 14:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120147">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oMOOOUnCLj0LfTmoT4M3CIDHaR_IW2Zeqdqszq8Yx0_U-Giov-zUb1LQmWVjm-G3qZJ50UWKs7NvgX1BVLJOvexunUlkQyTJK4Y5UhXuAb02uxcDWWW291ADiaTWwcJqtwWy7Wmu4uQozGydIwFk1RMpw_liuU7YZXT1cIky6y6thcS1uhEXe9w1HzHh0IE9ZcDrgiUjKjIFp82G7yIkCMv2_oSuS5gz2v0slJjzDH1etbmtBTnV-zvCaC1WytVOvuy4xc7hy4_UhiqYwj6-s0bGHxXNbsuTxqmIOlRIAkDCrLbyF_O0LAWU1-4Yncbnn4bkmKgVcwYEFVeH7dVr-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زاکانی، شهردار تهران: ما قصد داشتیم قبل از جنگ بیت رهبری رو با معماری جدید بازسازی کنیم، اما آمریکا عملیات تخریب رو که بسیار هزینه‌بر هم بود برای ما رایگان انجام داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/alonews/120147" target="_blank">📅 14:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120146">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XYUixGn2AtJ1qbio33U2_tndXVrwj0r8gDHZwUBDdaVDFdU0rBjVZTSdAyUDwcIA-nyfDHF782Zg5conxEi_c1IJhzPsnlvX9jAlixYyQBaT_TOE0av4yEvisjNivJYatMYNBEHuj52dY1_1vrS8Kyx2s4xEYuGG3ulz1nio2liLJmnSyI7vmw_Ggv-7VlDo7um8YTPDW9nw8XJCXJ-TGtJE9HbmLAhz_Pa010QK3x29bN41U9Sk-7RwwpaGc3cVHVltxEhTL3u6UJ4wGKsMwcjzFoUKOfhBPVMfr30HwVUynZlA5c4SPKC62-uSu3jCZL1n92tJTffvzjnWzl3EwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
اینترنت رایگان و آزاد برای همه مردم
⚡
VPN رایگان
⚡
کانفیگ تست‌شده و پرسرعت
⚡
آپدیت روزانه
⚡
بدون قطعی و دردسر
@NetaazaadVPN
@NetaazaadVPN
اینجا فقط وصل میشی و راحت استفاده میکنی
🫡
👇
@NetaazaadVPN
@NetaazaadVPN
@NetaazaadVPN</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/alonews/120146" target="_blank">📅 14:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120145">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
عراقچی: میانجیگری پاکستان شکست نخورده، اما با مشکلاتی مواجه است
🔴
از هرگونه تلاش چین، هند و روسیه برای حل بحران استقبال می‌کنیم
🔴
عراقچی درباره خروج اورانیوم از ایران به روسیه: مذاکره خوبی با لاوروف داشتم. مشارکت راهبردی با روسیه داریم. با پوتین در روسیه دیدار کردم و در خصوص اورانیوم هم صحبت کردیم، از پیشنهاد طرف روسی متشکریم، این موضوعی بود که باید در حین مذاکرات به نتیجه برسیم.
🔴
موضوع غنی سازی پیچیده است و برای رسیدن به نتیجه با طرف آمریکایی پیشنهاد دادیم این بحث به تعویق بیفتد.
🔴
در حال حاضر این موضوع مورد بحث نیست.
🔴
نسبت به جدیت آمریکایی‌ها شک داریم. آماده توافق منصفانه و عادلانه هستیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/120145" target="_blank">📅 14:00 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120144">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
وزیر امورخارجه: اگر از سوی آمریکایی‌ها جدیتی احساس کنیم، مذاکرات را از سر خواهیم گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/120144" target="_blank">📅 13:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120143">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
جعفر قادری، نایب رئیس دوم کمیسیون اقتصادی مجلس: اینترنت بین‌الملل مهم است اما از همه چیز مهم‌تر امنیت ملی است
🔴
فعال اقتصادی که برای او منفعت و درآمد دارد قطعا برای ادامه کار خود هزینه اینترنت پرو را پرداخت می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/alonews/120143" target="_blank">📅 13:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120142">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
عراقچی: ایران هرگز تلاشی برای دستیابی به سلاح هسته‌ای نکرده است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/alonews/120142" target="_blank">📅 13:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120141">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
عراقچی: ایران هرگز تلاشی برای دستیابی به سلاح هسته‌ای نکرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/alonews/120141" target="_blank">📅 13:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120140">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tzl4d5z2yQg3Q4MS1H1KY3YvaZFv3F54Nyrq-oh1c2QxkeBlICoRzOazv3jeu0wevJ9E1IqYao62Re-K5ZDY31OIHVFZaEi371nHgAOxGKkLR35xjeJPG0Lw9m59nLrSuKrOhGJXyT5xkHMDKsZ94BD86spfR8gl-aQQSIWNxAkU-T-0YR0NVGmjs5HC54seN2k6X9tUecY1CyED5ovTa0zw-q8U2RfQblslvQ8mrMbyPrM0E2T003V-7yuc_yQ1Wn3PqGm--QBXzCRLFbUKP00jWNkOW9c-Rsq2sCLIqeOPzVbu1Azo7l7omrO28ZJdfp51z3JaogFvT2zhy7m98Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افزایش قیمت نفت برنت به ۱۰۹ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/alonews/120140" target="_blank">📅 13:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120139">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
عراقچی: ما در وضعیت آتش بس هستیم اگرچه متزلزل است، اما
تلاش می‌کنیم به دیپلماسی شانس دیگری دهیم
🔴
در برابر حملات تجاوزکارانه و تحریم مقاومت می‌کنیم
🔴
توافق ۲۰۱۵ یک دستاورد بود، اما ترامپ بدون دلیل از آن خارج شد
🔴
آمریکایی‌ها خیلی زیاد نظرشان را عوض می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/alonews/120139" target="_blank">📅 13:41 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120138">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/571bfcee62.mp4?token=SMxpUg9uKVslpy7IsKQ_wzamm3U8AfxNbtj2jynd9i0WSNBYr0ASNVd7ywasIwNy6aDLEZDzjMdpar0ZruzRFIbtKXBt2CqIbBHU0_x8FKmh5ndp4kIhr3s2jQNupvqmv7UwzRnSpEJkbubd_mUsGrLuIskEj2_gy0_o7nHyetiLOqnmFDr5Dp6sGfBlYeKhjVruKY1y7hqXfw_9tU4wRvuepOYZbK_s-6jumcErzjIDPXOYddLDh-TWLYWJN0AY621r2NGW3rPjXbdIeNaOuyajYPPPXaztbVQaF3v-ueNtY0gtbcmln_9k-N3nqQ4_b2kHQQNWPF7P6U8GcVUqxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/571bfcee62.mp4?token=SMxpUg9uKVslpy7IsKQ_wzamm3U8AfxNbtj2jynd9i0WSNBYr0ASNVd7ywasIwNy6aDLEZDzjMdpar0ZruzRFIbtKXBt2CqIbBHU0_x8FKmh5ndp4kIhr3s2jQNupvqmv7UwzRnSpEJkbubd_mUsGrLuIskEj2_gy0_o7nHyetiLOqnmFDr5Dp6sGfBlYeKhjVruKY1y7hqXfw_9tU4wRvuepOYZbK_s-6jumcErzjIDPXOYddLDh-TWLYWJN0AY621r2NGW3rPjXbdIeNaOuyajYPPPXaztbVQaF3v-ueNtY0gtbcmln_9k-N3nqQ4_b2kHQQNWPF7P6U8GcVUqxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ایلان ماسک این ویدئو را از حاشیه‌های خودش و تفاوت با بقیه حاضران در ضیافت شام چین و آمریکا منتشر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/alonews/120138" target="_blank">📅 13:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120134">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3IzFZNngCzOEu5iZxeSyZbsHJcZPxkDPpoO31YzL3nbgddJ1fHQk2X44YTd_UZOXLZeutTCCxGRo53kyB5cGmW9uhDX-gRTD1b6kEa_sLNxwIZuGEq8nGALqNBoN6noReL13CIiIeXTc-X-KsBz4z-CmMsmTFjhRTguflImhfyphDVvoHXxC0Ac2tt3W9UjyOXOTAv7VISU937yrtMXQnVjHZ8-r7mvxVuOWSe36KCtURfsSGq8ubt5HYuLw5cWL8SCPouqF4GTbUtf3Ggb9kxjautzuOMDRiPuOuxS1WXG8pybVGXYOFNamA4fcw7M1Qo0gsC_JSoMpQ9_lHuwDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BXu1HFgjeSUhY7sRb6odnHBuqQ-GHDqraRaYcoU7Dl94fHeuc4LBmADgAeedRSJoBDheOAxGV4GDoD8-A-Fsr8MRgXhFunuOwcaSAtramCoTWo3JLwYyjF9UQR9NMdRGTkaD_skn7nXvYJiu965THXRwmPjIO_Ny1AmJwCrdnBOmw2hPiyqKrj0dRRaYwpqlSx0iQ_-824WlhdhIGEh-NlQf0MH2ouYQjRnKiign1SfOKXGb1nin04kcC6vazpRVRdzL8ZGRF4LBZxxNo2bnk-pVlhfG9jnqcFH2zinKc0EJwIYRkVLi2j3w0VaY3UPzNG0PN63ZAZXHcoU3C8LdXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PuGZ7YD5s4KmfN9FTw3NtT6D9kLhrNjQH5X1au7609j6MvGhJVb5eudxtWm57aqEpeMnHPKVTC3uUdtgergxPBxGN2Rqemb__dDgpg0nSsocpmNTZA68EhwVDrtFni8jHxPfoPYty3iIErrv36xTZVUa6sJ_Bx6Viv08nn-3Loi5ZdVu41UsISx96vm6bZ1DF-aTGxAdXx1HO8XATzkVXi49LJ7zYTCeFZah6NPovs2jR1zfMLdRN47kUGFHn4fDg6blfLxUmHTDl57kAApAGQQVRYqn87uY-MJDAAwZGGKYBPC6bZklN6Q66DF6Jp8ZlBPHb6Q_UMgbokIEUBkh1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ffd59f94c.mp4?token=RYIgFQzcGMeg8IftMvJneWrTHOYrnsfzL8ZL6FxJ7TLYmEr9vSpvwuy6IauW_XtyBwP2BYHKhQ0ZTGw45aIj106XsbWdad9Uwz5dSdTMHLYQvzWVE5Hhqw_FL8vE-2tJmVKda67fhy4li60-f6px5-MvFUaVmuY3YeT9ZnBkNbQsxvcd9RWnQXDFw6YgbtQ4HvGUoPUcIfjp2Nq8gfThej8L7GjZWp7gdPmFbkMyiYIyAGO2OiHrUe8nrXqTHneKM9S-unLN3ScALiJ-TNHlvHYCTWxgdgI6Gxu424ZNYr9NgOC6MNFTQrU8GtqBOIeABkCsOKWI0_65x9ZqwwxryA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ffd59f94c.mp4?token=RYIgFQzcGMeg8IftMvJneWrTHOYrnsfzL8ZL6FxJ7TLYmEr9vSpvwuy6IauW_XtyBwP2BYHKhQ0ZTGw45aIj106XsbWdad9Uwz5dSdTMHLYQvzWVE5Hhqw_FL8vE-2tJmVKda67fhy4li60-f6px5-MvFUaVmuY3YeT9ZnBkNbQsxvcd9RWnQXDFw6YgbtQ4HvGUoPUcIfjp2Nq8gfThej8L7GjZWp7gdPmFbkMyiYIyAGO2OiHrUe8nrXqTHneKM9S-unLN3ScALiJ-TNHlvHYCTWxgdgI6Gxu424ZNYr9NgOC6MNFTQrU8GtqBOIeABkCsOKWI0_65x9ZqwwxryA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات نیروی هوایی اسرائیل به صور "لبنان"
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/alonews/120134" target="_blank">📅 13:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120133">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
روبیو: اگر ایران فکر می‌کند ما برای رسیدن به توافق امتیازاتی می‌دهیم، سخت در اشتباه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/alonews/120133" target="_blank">📅 13:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120132">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XaLNxnPYstlR2tGll5oCbybw-DI58oyPpl3_UrMDmkcGYUeKLhW509coL3aMmTIbmCFGY2mOwBIEgYZFnLxI-wSzlSwTjGak4q-bDEbDVh9ocLi9So4Ng87ycRe_Y11Sy5BHaFLM_zJvvPyAmzJy7h_PFZY5r4VbD3f5ulCQF17jCfDVjvRpsjv7aMiZaKp6_nyAqx0dD7c88wjwGna4326UbLGiPIT68-tzJlm-pnekVYCeALMIy1DqnSkf3naqtky5IJddRN13_urJcyrg-rkMUvmagfBh-_gdaxknySKIy23sGzfaFCUTNBr7wkLy-QKUXjbIkfsZwqST2X3yaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نت‌بلاکس: قطع اینترنت بین‌الملل در ایران به ۱۸۲۴ ساعت رسید...!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/alonews/120132" target="_blank">📅 13:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120131">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
شبکه «کان نیوز» امروز مدعی شد که اسرائیل و لبنان در حال نزدیک‌شدن به امضای یک توافق در واشنگتن هستند.
🔴
در این گزارش ادعا شده است: «این توافق شامل عقب‌نشینی مرحله‌ای ارتش اسرائیل از جنوب در ازای اجرا یا پیشرفت چشمگیر در خلع سلاح حزب‌الله خواهد بود».
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/120131" target="_blank">📅 13:16 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120130">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/658dded15f.mp4?token=AbRblyaQz_zKliQJ85A3fE3fLEPSL4Q3OjUxhoRTz2ZP8ooKnaxFHt_jSjGdb5hLYA92CqkcSTHZkjJ3ioR8Q34gDiTgX3hl4JVnwpR92h6rnyTj9G2kP0EACSWhZJXhsgOIuPgQA3NoauSgDNnwbz5fK9osuFkJXB7Bh9vZTxknOlXryqTjW51t275C6w9Xi0MuQrWx66FVhmqFPZkPhHySATHYT7ejCf2y54qPMKCWngCtd3Win6WhRC6NzNED1PxWi45CmIjf7sqjr2DV8cRzKr__G8gsvcl6jz0tUzutxfQP3x_2nRo_9zbxV4AJe6NLeeMracfGVY3ISIMgLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/658dded15f.mp4?token=AbRblyaQz_zKliQJ85A3fE3fLEPSL4Q3OjUxhoRTz2ZP8ooKnaxFHt_jSjGdb5hLYA92CqkcSTHZkjJ3ioR8Q34gDiTgX3hl4JVnwpR92h6rnyTj9G2kP0EACSWhZJXhsgOIuPgQA3NoauSgDNnwbz5fK9osuFkJXB7Bh9vZTxknOlXryqTjW51t275C6w9Xi0MuQrWx66FVhmqFPZkPhHySATHYT7ejCf2y54qPMKCWngCtd3Win6WhRC6NzNED1PxWi45CmIjf7sqjr2DV8cRzKr__G8gsvcl6jz0tUzutxfQP3x_2nRo_9zbxV4AJe6NLeeMracfGVY3ISIMgLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حزب‌الله فیلم عملیات ۱۲ مه خود را که با استفاده از راکت‌ها و پهپادها، تجمعات ارتش اسرائیل در جنوب لبنان را هدف قرار داده بود، منتشر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/alonews/120130" target="_blank">📅 13:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120129">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
فرمانده کل ارتش : قدرت ایمان است که می‌تواند یک جنگنده اف-۵ را بر فراز مواضع نیروهای آمریکایی در کویت حمل کند، با وجود اینکه آن‌ها پیشرفته‌ترین سامانه‌های دفاع زمینی و هوایی را در اختیار دارند.
🔴
نیروهای مسلح با تمام توان خود از تمامیت ارضی، استقلال و نظام جمهوری اسلامی ایران محافظت خواهند کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/alonews/120129" target="_blank">📅 13:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120128">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
کرملین: روسای جمهور روسیه و چین در یک تماس تلفنی درباره نتایج سفر رئیس جمهور آمریکا به پکن گفتگو خواهند کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/alonews/120128" target="_blank">📅 13:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120127">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuqKev2M4hXb4OCgfpRgGEXQ8-Xln2Rz2mKKiVQCLt8MGa8mvxYGQn2HIDm59mjN_FWvIIjsHqSU-UYAQ3Q9wnhzTDd2gXJKlmwqqKDsXAtF0UnlJ_0AX5TDPrLETFaswNHMvxRv7TRPVlg4I3yePayYaWqeHaLalNm4u-YYkfXlXsQ1j9aIhe1U8ncsKxjeiNQzJMhGPOCUqWpyWDlTD-v6WUSQ9eMEJiQpceHoeKMZ9XEGikPUkgJU6vGIAaPkt3wQncqB_mNggI3dJoiEB-_hVTx42rxxKNyjT-NPzEeAQTgkLSvPIOuCRsViCClgouW00sZg7ysrUWvx9jw3iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خنثی‌سازی بمب یک‌تنی در شهرستان دلفان لرستان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/alonews/120127" target="_blank">📅 12:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120126">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
بلومبرگ: امارات متحده عربی تلاش کرد عربستان سعودی، قطر و دیگر همسایگان خلیجی را به پیوستن به یک واکنش نظامی هماهنگ علیه ایران ترغیب کند، اما رد شد.
🔴
شیخ محمد بن زاید شخصاً با محمد بن سلمان و دیگر رهبران تماس گرفت.
🔴
هیچ‌کدام موافقت به مشارکت نکردند.
🔴
در نهایت امارات عمدتاً به تنهایی عمل کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/120126" target="_blank">📅 12:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120124">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f297a7c3f.mp4?token=pfnKVy_cVkY38ctyduPaLOfc-jQii3gh45w-EMy5_kXrnH4zI4_p_xMEMrlm7rDbEZ2HV9Oqjd6h1y0tUuGB6m8k8NjgZVqigW4lJsHSZZVWs4sbNmClnoHK9iPrX0MtjcWutREmxfo3nR_aKx1UTPetVIepOedkjuUCMjHaXZgBquAQwQH-7YnPvu1l7KHhCFezrT_0B6mLhemQ4yVy_ct9Mze8qhRdCML9qAtAsvZsCYlwpA0nYs-XLHITV5Kky_9ImT3QGM1q7YvGqNordH1oZWPQkDV6pMkSlBWXsFqjyGmXVCh4ngxiin6DHa-y1ToYseHNPx0nzf_I6zuAWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f297a7c3f.mp4?token=pfnKVy_cVkY38ctyduPaLOfc-jQii3gh45w-EMy5_kXrnH4zI4_p_xMEMrlm7rDbEZ2HV9Oqjd6h1y0tUuGB6m8k8NjgZVqigW4lJsHSZZVWs4sbNmClnoHK9iPrX0MtjcWutREmxfo3nR_aKx1UTPetVIepOedkjuUCMjHaXZgBquAQwQH-7YnPvu1l7KHhCFezrT_0B6mLhemQ4yVy_ct9Mze8qhRdCML9qAtAsvZsCYlwpA0nYs-XLHITV5Kky_9ImT3QGM1q7YvGqNordH1oZWPQkDV6pMkSlBWXsFqjyGmXVCh4ngxiin6DHa-y1ToYseHNPx0nzf_I6zuAWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات امروز به کرد های عراق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/alonews/120124" target="_blank">📅 12:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120123">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
روزنامه گاردین با اتمام سفر رئیس جمهور آمریکا به چین در گزارشی اعلام کرد: توافق ترامپ-شی درباره ایران دست‌نیافتنی باقی ماند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/120123" target="_blank">📅 12:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120122">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
کوبا اعلام کرد رئیس سازمان سیا به این کشور سفر کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/alonews/120122" target="_blank">📅 12:36 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120121">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/120121" target="_blank">📅 12:16 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120120">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVarzesh+plus | ورزش پلاس(K_B9)</strong></div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/alonews/120120" target="_blank">📅 12:16 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120119">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
دستگیری ۲۲۳ نفر از اتباع بیگانه غیرمجاز در زاهدان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/120119" target="_blank">📅 12:16 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120118">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiuZ6P4KlXoYyhx5cv_eJQzMwTAWTFBmbu5TSRAKfGBXhxAiBlmsdwaUn0pXlexs38WfTNtOZN_ccP_XbuRVPJToQo6bpc3FacQ9xHdkgT6F-QSknjyzi6ddae7j1aIzQQ82z0rDJScANrjxycgavGmqfwEbItgHeeIadpZlFEK3ChKB7Cy2kiJNFnL0hxSeI8neQcDQ_0RBUrAg_H5psfBpD6zVzzGdIGuwWVdbSsptBdqhaJd_gzRxKtaqZlpMd_I68RNelgADg63sEd9pTp-14J3vdkcKF28WkjGshKgA4p4YNem6tS3uucIGLD_GgQIC3euJRkt-P4qYe6JqAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فایننشال‌تایمز: اگر تا ماه آینده تنگهٔ هرمز باز نشود، به‌دلیل تخلیهٔ ذخایر استراتژیک شاهد موج گسترده‌تری از کمبودهای جهانی و افزایش قیمت‌ها در حوزهٔ انرژی خواهیم بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/120118" target="_blank">📅 12:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120117">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
خبرنگار الجزیره: تهران به‌طور رسمی پاسخ واشنگتن به پیشنهاد خود را دریافت کرده است و ایالات متحده تمامی شروط ایران را رد کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/120117" target="_blank">📅 12:12 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120116">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
امارات ظرفیت صادرات نفت بدون عبور از تنگه هرمز را دو برابر می‌کند
🔴
امارات متحده عربی اعلام کرد تا سال ۲۰۲۷ ظرفیت صادرات نفت خام خود بدون نیاز به عبور از تنگه هرمز را دو برابر خواهد کرد.
🔴
بر اساس گزارش‌ها: شرکت ملی نفت ابوظبی در حال ساخت خط لوله جدیدی به بندر فجیره در دریای عمان است
🔴
هدف این پروژه کاهش وابستگی به تنگه هرمز عنوان شده است
🔴
بسته‌شدن مسیر هرمز در جریان جنگ اخیر علیه ایران، بازارهای جهانی را دچار بحران کرده است.
🔴
امارات هم‌اکنون نیز یک خط لوله با ظرفیت روزانه ۱.۵ میلیون بشکه از میادین نفتی داخلی به بندر فجیره در اختیار دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/alonews/120116" target="_blank">📅 12:10 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120115">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1ee518068.mp4?token=rs6rG4K-TB9wVYXWbscUVTr65UTDJrkWnD5xuR_-x7hYBsyn_HkP7nlk4QT-Jg7i_y-GUG6awbGP3sMmkqlSYAatr-iIpZr7uWQTuYhCRGMLN_ZiqPYA3Y3GrGulwPzx7iIMGxV10Lji6fJjZ-6kSWR4S2JK9d4utuBjztV5iPL20YgHabNaJ-MZjY3SXZM4KgyV__hjjeXc-qWe_8Iv9mwQccUlG7Zwrz30RaFBqsbkmBZyTG27MyyJUM41mgYxP5SJYNId4l3wa7ZgkP0ZXnmHL5aTa3oq3W8R0bywYpSY6nA7diUCtOX5877E0WVM1dbO3kZDiI7_kRRwcNes5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1ee518068.mp4?token=rs6rG4K-TB9wVYXWbscUVTr65UTDJrkWnD5xuR_-x7hYBsyn_HkP7nlk4QT-Jg7i_y-GUG6awbGP3sMmkqlSYAatr-iIpZr7uWQTuYhCRGMLN_ZiqPYA3Y3GrGulwPzx7iIMGxV10Lji6fJjZ-6kSWR4S2JK9d4utuBjztV5iPL20YgHabNaJ-MZjY3SXZM4KgyV__hjjeXc-qWe_8Iv9mwQccUlG7Zwrz30RaFBqsbkmBZyTG27MyyJUM41mgYxP5SJYNId4l3wa7ZgkP0ZXnmHL5aTa3oq3W8R0bywYpSY6nA7diUCtOX5877E0WVM1dbO3kZDiI7_kRRwcNes5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عراقچی : مشکل اصلی اینه که آمریکا هر روز یه حرف می‌زنه و پیام‌های ضدونقیض می‌فرسته
🔴
در مورد ایران هیچ راه‌حل نظامی‌ای جواب نمی‌ده
🔴
این همه مدت هی تهدید کردن، ولی نه نتیجه‌ای گرفتن نه از جنگی که راه انداختن چیزی گیرشون اومد
🔴
هرچی بیشتر تهدید کنن، بیشتر شکست می‌خورن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/120115" target="_blank">📅 12:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120114">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUy7q4qqD0hQyIRJdgn9M1yob8XXjEjq2taliys__yICEsxJ-fQd3PMN8s-nG0oliPm9g7YOoTAQDaleFywvqAl8NWp3MF71Q6CkN4j0t_rdLF3wWoRSbwgfvCHwYmNT-J00eQsy1OHTp-Sv6CW-LRO2OZnyJHF_PIjFYwA15gYsqQ0coMVE8UwA4eK8JuKGJQv7XT_EGwCFNs--trZVpWC-4u6oztJl_W1K2-tuedmPvYWBeVQC6gywRDolJ0iKynRNLXm05EP9Ca9qR_OwYSo2YiWiLURavAZ0zW-L8ABqa-n7n5aJwR0HohhPvUTeVqSICtUFGJaVE0p1Xf9UIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیماهای باری نظامی آذربایجان از طریق حریم هوایی ترکیه به سمت تل آویو در حرکت هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/alonews/120114" target="_blank">📅 12:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120113">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTJaqY4xv1bDcCokOl_qssT9fav4NuygJDmKdCwnz6W5y5QpMe3Kd1BDnF48dcYP9nldynCGsq1Jx-444XEBNWwTLjnYCreXJ14qmJyijSUMst0V163wE8rrJws-tz8nQ4R5Z1LFQXVRZgmgwOc72b21ISkzrMcjjShbbaa37dFIZhfT_jcY2epIxfA_wViRx6ydqDsNspMtqpz7cwc1hKpm8CWusirWUIsrWRYo4HRpRdyUMWmQgCk79s7XyogsgyDanbuO2A28zj27d0cs4lQUGv0iny0FMOjxIKZDZFV--r5i1ZsV_PToShzRvgGshLopAU5WbhrXtmsa1-jEqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جنوب لبنان، ساعاتی قبل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/alonews/120113" target="_blank">📅 12:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120112">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
صدای چند انفجار در اربیل
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/alonews/120112" target="_blank">📅 12:00 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120111">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه چین: درگیری بین ایران و ایالات متحده از همان ابتدا هرگز نباید رخ می‌داد و نیازی به ادامه آن نیست
🔴
یافتن راه‌حل در اسرع وقت به نفع ایالات متحده، ایران، کشورهای منطقه و جهان است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/120111" target="_blank">📅 11:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120110">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
سازمان پخش اسرائیل: ایال زمیر، رئیس ستاد کل ارتش اسرائیل، در طول جنگ با ایران مخفیانه از امارات متحده عربی بازدید و با محمد بن زاید، دیدار کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/120110" target="_blank">📅 11:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120109">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
سخنگوی صنعت آب: ناچار به مدیریت مصرف به روش‌های مختلف هستیم تا بتوانیم آب را تأمین کنیم، از جمله افت فشار آب
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/alonews/120109" target="_blank">📅 11:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120108">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
صدای چند انفجار در اربیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/120108" target="_blank">📅 11:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120107">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
رسایی: جلسات مجلس به طرز بی‌سابقه‌ای تعطیل شده تا در مذاکرات دخالت نکنیم
🔴
دبیر شورای عالی امنیت در نامه‌ای اعلام کردند مصلحت نیست جلسات مجلس برگزار شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/120107" target="_blank">📅 11:49 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120106">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98aee1045d.mp4?token=tSUbiDelKu037PesBf2tUoUIKlAO0wNH3LuBhT5bYOKT2vGiHlN-ej4o7UZEAKUqLlHuqJSrZd3OLmsYczAEoFkDDv6VM0DJZnqpwMROseTSMlmfBByvdew3UL6B8D4uPJX4SZxuZfmzFrx9YDnzL-yJPb2Q_pnEVRUyzc9Eed8-jE0H7GM9tiE6DE-qGV4Hx8go1LCMfueDbvNBzB0-If_Jjow7V2RkUlQ6_4R_NtdcwMo7YJBfRwytId_nMVVL0qAwhZ-1QkVStbphZu6H1ql1jkb0CZV4q3VCyXvf5b7hLOD8bwdkDy-aT0rW9nJ7QgNI77oJe-MBJ3hR4NMVew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98aee1045d.mp4?token=tSUbiDelKu037PesBf2tUoUIKlAO0wNH3LuBhT5bYOKT2vGiHlN-ej4o7UZEAKUqLlHuqJSrZd3OLmsYczAEoFkDDv6VM0DJZnqpwMROseTSMlmfBByvdew3UL6B8D4uPJX4SZxuZfmzFrx9YDnzL-yJPb2Q_pnEVRUyzc9Eed8-jE0H7GM9tiE6DE-qGV4Hx8go1LCMfueDbvNBzB0-If_Jjow7V2RkUlQ6_4R_NtdcwMo7YJBfRwytId_nMVVL0qAwhZ-1QkVStbphZu6H1ql1jkb0CZV4q3VCyXvf5b7hLOD8bwdkDy-aT0rW9nJ7QgNI77oJe-MBJ3hR4NMVew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▪️
خبرنگار:
امیرعلی چرا اومدی تجمع؟!
▪️
امیرعلی:
به عشق رهبرم.
▪️
خبرنگار:
مامان و بابات مجبورت کردن که بیای تجمعات؟!
▪️
امیرعلی:
آره
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/alonews/120106" target="_blank">📅 11:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120105">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/120105" target="_blank">📅 11:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120104">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
فایننشال‌تایمز به‌نقل از دنیس وایلدر، رئیس سابق بخش تحلیل چین در سیا نوشت: بسیار قابل توجه است که گزارش‌های رسمی چین تاکنون هیچ اشاره‌ای به توافق آمریکا و چین بر سر «ایران غیرهسته‌ای» یا مخالفت با «مالکیت ایران بر تنگهٔ هرمز» نکرده‌اند.
🔴
این سکوت، سوالات جدی را دربارهٔ این ایجاد می‌کند که آیا واقعاً صحبت‌های ترامپ به‌نقل از چینی‌ها در این‌ موارد درست است یا خیر.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/alonews/120104" target="_blank">📅 11:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120103">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
نیویورک پست: اداره تحقیقات فدرال آمریکا (FBI) اعلام کرده است که برای پیدا کردن و دستگیری «مونیکا ویت» مأمور سابق اطلاعاتی نیروی هوایی ایالات متحده که به جاسوسی برای ایران متهم شده است، ۲۰۰ هزار دلار جایزه تعیین کرده است.
🔴
گفته شده اون از سال ۲۰۱۹ رسما به فعالیت جاسوسی برای ایران پرداخته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/120103" target="_blank">📅 11:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120102">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f18e93e69.mp4?token=BaE8dqpguSeTs-RC9nFMoyE488fCrr4rfk4vtmCmWknLHOFxUZDLzH2QgUUDlaK5fk09gR3CsQ1f9cpN4DEMOelR-Z2_p3mmtopTzLtFeHXPqT1wz9ws7ZlUZw-8uHsbuDLqeEApedvNSSWXsZPomQpQNGfekERwIrzdaEs_9jzQcJuH078M9OpRq3fEZ9CW7kvaWu6kJMts9dUfIRzr0QE1cBE47zXKKBZFTVgX2gLHyCE0scXMxpl21JrAu8B-d-rLrVueXl6IPpqYTFiPWU8LruZhMyLH19G3ZvyJ8wuWPKBPvT-I-nfisLai2dhYZcLw6Fx7S9bjoFgeV7JhVSGj1PvGFcqVsrz7gBSg-NmxhNZDbOoX33m8gObSlWz07_xwMZIOSoWz4D2N-crjw7-xYvmr8FI7AumEkDzQr_tG_rhKqOxEhJHJMsiYZgqOTTvCT4aVHv164KnkuP6wFSdK7QqqCUDkV4_pWZOXA5Chqgd_0duW6pDXCQCfZ130eHLJhXylq5zFOXc6mkGOKtwlu9Uk6gtWN5qxaf_Qe8pxVFAe6zV-rm7HJOA6nWVip6rrccmCKDMtZeDVv-uSGwWdgYL9tOCIYHvp4BTbmfXPbJaoL2VFfVZ4byOvlu4enPexx30kRdcV4ASx66J1tJUk2gp_5V3nIqKA_MajCW4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f18e93e69.mp4?token=BaE8dqpguSeTs-RC9nFMoyE488fCrr4rfk4vtmCmWknLHOFxUZDLzH2QgUUDlaK5fk09gR3CsQ1f9cpN4DEMOelR-Z2_p3mmtopTzLtFeHXPqT1wz9ws7ZlUZw-8uHsbuDLqeEApedvNSSWXsZPomQpQNGfekERwIrzdaEs_9jzQcJuH078M9OpRq3fEZ9CW7kvaWu6kJMts9dUfIRzr0QE1cBE47zXKKBZFTVgX2gLHyCE0scXMxpl21JrAu8B-d-rLrVueXl6IPpqYTFiPWU8LruZhMyLH19G3ZvyJ8wuWPKBPvT-I-nfisLai2dhYZcLw6Fx7S9bjoFgeV7JhVSGj1PvGFcqVsrz7gBSg-NmxhNZDbOoX33m8gObSlWz07_xwMZIOSoWz4D2N-crjw7-xYvmr8FI7AumEkDzQr_tG_rhKqOxEhJHJMsiYZgqOTTvCT4aVHv164KnkuP6wFSdK7QqqCUDkV4_pWZOXA5Chqgd_0duW6pDXCQCfZ130eHLJhXylq5zFOXc6mkGOKtwlu9Uk6gtWN5qxaf_Qe8pxVFAe6zV-rm7HJOA6nWVip6rrccmCKDMtZeDVv-uSGwWdgYL9tOCIYHvp4BTbmfXPbJaoL2VFfVZ4byOvlu4enPexx30kRdcV4ASx66J1tJUk2gp_5V3nIqKA_MajCW4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لاوروف یک روزنامه‌نگار را از نشست خبری بیرون کرد!
🔴
به گزارش اسپوتنیک، این فرد دو بار با مکالمه تلفنی‌اش صحبت لاوروف را قطع کرد.
🔴
وزیر امور خارجه روسیه به زبان انگلیسی از روزنامه‌نگار خواست که محل کنفرانس را ترک کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/120102" target="_blank">📅 11:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120101">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f43d4a727.mp4?token=McT8xNzJvqpdrb57TAWzEl_gCgeuM7W0lmvfoZhlktcKE9u2bcdQJfYI9zXIIzqbw4rqquhOJCkEfZxWvuo5Bk8GXnisWBLxnQNQJe_vUzgvxlhyNRl3ZZUNudYlnHmUzljg_1n5K16c6G1C0ZoANQXfc9knJM3Zn2aqxntYMujcfM5gpT7VW1Ax4nhhndcr4rjbK-aAPesPGMOoKwjEFRThcvJffaGowlhl75fsIrVlIfVgyBeBgJUEACmuUhD0zAAtu-74LAVBkeWR6fDU5YYzDOHE7ZhP_UAXwT1jz4rQMZDbSS_rX5-BVBJ7ZF4zqJsDVaidHQfwYHzmV-TiUQV2vYYPuqcG_OLkPQUTZnBcEVPK-fvdI-7rmumlyhCG4q-NxWn1a6ms8UhkOOfGba9hV6O3o2x7dY9G82VAzY0Tb_EIIUUN-zwFsmrq1lgom1KfSSqEiT0TZ18ERYnBUW2-6A5Mwl2oNian6OUP1d3vc2c-DA1Xu_W4Zh0WaM65OWImtfv9ZhpT-eajfoYIMTDjHvONC8t7LKEUKFOggpr6QJqlDNbMJrBMiw2KBQX_jIeJk8gZyIJr5eC2XFEK9kpZw90fBYyzc4b-JSIg_pTbeqUqCZva-0OofLfNt-hTrrCG8aFmjsTow7-9O4giKAilA35MFp8ruw5q8GUrRiE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f43d4a727.mp4?token=McT8xNzJvqpdrb57TAWzEl_gCgeuM7W0lmvfoZhlktcKE9u2bcdQJfYI9zXIIzqbw4rqquhOJCkEfZxWvuo5Bk8GXnisWBLxnQNQJe_vUzgvxlhyNRl3ZZUNudYlnHmUzljg_1n5K16c6G1C0ZoANQXfc9knJM3Zn2aqxntYMujcfM5gpT7VW1Ax4nhhndcr4rjbK-aAPesPGMOoKwjEFRThcvJffaGowlhl75fsIrVlIfVgyBeBgJUEACmuUhD0zAAtu-74LAVBkeWR6fDU5YYzDOHE7ZhP_UAXwT1jz4rQMZDbSS_rX5-BVBJ7ZF4zqJsDVaidHQfwYHzmV-TiUQV2vYYPuqcG_OLkPQUTZnBcEVPK-fvdI-7rmumlyhCG4q-NxWn1a6ms8UhkOOfGba9hV6O3o2x7dY9G82VAzY0Tb_EIIUUN-zwFsmrq1lgom1KfSSqEiT0TZ18ERYnBUW2-6A5Mwl2oNian6OUP1d3vc2c-DA1Xu_W4Zh0WaM65OWImtfv9ZhpT-eajfoYIMTDjHvONC8t7LKEUKFOggpr6QJqlDNbMJrBMiw2KBQX_jIeJk8gZyIJr5eC2XFEK9kpZw90fBYyzc4b-JSIg_pTbeqUqCZva-0OofLfNt-hTrrCG8aFmjsTow7-9O4giKAilA35MFp8ruw5q8GUrRiE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره به‌دست آوردن اورانیوم غنی‌شده ایران: فکر نمی‌کنم این کار ضروری باشد مگر از نظر روابط عمومی. فکر می‌کنم برای اخبار جعلی مهم است که ما آن را به‌دست آوریم. من کسی هستم که گفتم ما آن را به‌دست خواهیم آورد و واقعاً به‌دست خواهیم آورد.
🔴
چشم‌مان به آن است. به آن‌ها گفتم اگر نیرویی آنجا بفرستند تا آن را بازیابی کنند، ما فقط با چند بمب به آن حمله خواهیم کرد و این پایان کار خواهد بود. آن‌ها این کار را نخواهند کرد.
🔴
ما ۹ دوربین روی این سه سایت داریم، ۲۴ ساعت شبانه‌روز. واقعاً اگر آن را به‌دست می‌آوردم احساس بهتری داشتم. اما فکر می‌کنم این بیشتر برای روابط عمومی است تا هر چیز دیگری.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/alonews/120101" target="_blank">📅 11:30 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120100">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
واردات بدون انتقال ارز برای خودرو کلید خورد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/alonews/120100" target="_blank">📅 11:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120099">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
لاوروف، وزیر خارجه روسیه: باید جنگ در ایران فوراً متوقف شود و به آتش‌بس دست یافت.
🔴
مداخله غرب، چه نظامی باشد و چه از طریق تغییر رژیم‌ها، وضعیت را در خاورمیانه و شمال آفریقا پیچیده‌تر می‌کند.
🔴
برای رسیدگی به بحران مربوط به ایران، لازم است علت اصلی بحران درک شود؛ یعنی «تجاوز غیرموجه آمریکا و اسرائیل».
🔴
ضروری است که هیچ‌گونه مشکل یا مانعی در تنگه هرمز وجود نداشته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/120099" target="_blank">📅 11:17 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120098">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
آموزش و پرورش: امتحانات پایه‌های هفتم تا دهم با مجوز شورای تأمین هر استان و بصورت حضوری یا غیر حضوری برگزار می‌شه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/alonews/120098" target="_blank">📅 11:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120097">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
فوری / ترامپ : من صبر بیشتری نسبت به ایران نشان نخواهم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/120097" target="_blank">📅 11:03 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120096">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
پوتین ۳۰ اردیبهشت به چین می‌رود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/120096" target="_blank">📅 11:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120095">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
وزارت خارجه چین: در مسئله هسته‌ای ایران، استفاده از زور به بن‌بست رسیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/120095" target="_blank">📅 10:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120094">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
کانال 13 اسرائیل:اسرائیل انتظار دارد حمله احتمالی آمریکا در ایران با بازگشت ترامپ از چین آغاز شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/120094" target="_blank">📅 10:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120093">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQYBczTS4IYIVqNYWOX0xvLkNdnCkAxaSOiD43nAaYqW6djxEHGNZiQBaGljcl9O-XKgC3Kcp7SdmoBxfa5UtnDDw9lq4Yr4xxXxfKctVFHMnnTTLY9oVjQOroXr3wda19axJTJo-4DAjhtEQ6MPsH-AaGt7hJRert7MFqOUBhdyXEpZN6D94LsU_iFeIBcxs7puuhE6MQWOmx2y4JG0qgXkplY3gToBHJSKI6-aEqptCqmN18SkmHoVzv032mTXlvzJmbRkHCXZCLwHo47uYNChZGr0qI_Oaa5b0YuypeVfsk4r3mGEM6X9IsvEflM6_ZMOc7ZfwpXbh1yva3AaCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
👈
ریزش ادامه‌دار قیمت انس جهانی
هم اکنون 4573$
✅
@AloNews
خبر جنگ
‌</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/120093" target="_blank">📅 10:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120092">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JwmQuH3nRQ3eczAcGm0nlDNUwBZzfhnjOzl0q_RSZWpWUPjL3ASvfklQ9P8nZIhVBim7IGTdyNjBw1axCAo__w40TjlqEG_j9ZB8LrWzi7_aX4lUb4ezTGDJEhm5VuIYOojsOjXUua4hMaGHSYw38FKMVEO5mJuLgOuCGFW8KriVTpeFNHqOgOcG7KwtTIX0iXX86iRBMhm3H0Oc_hkcppeAzhgP2DsWFBNSDOhSI6nPOcqrQKKRDa1JmGo7JOxY7_jc2P54txSp9_VrRnd_l84_4SBfPPXeAjpjFGS4CVtJd9jWw-j2qwmKazE_knUTFa1nxL1hvU3DbGem47gVkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ هم اکنون چین را ترک کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/120092" target="_blank">📅 10:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120091">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZ8HlUncLuSYAkt1c_qTDXWBvubremDl35br3cnnwqdMZmTa-Tp1f2khfrS-vPhGW45l7QWLeOFSq2SkEe3SLiVYTp6iuRS-0gIISTCv3LASsZYD42tpRRDM-EzCK2-iTeJloJQpOrV_RKPDkJLFeOcGLWXDt67Xw9f6K9vJWST1yLDjWLapLK_8Gtt_xYirI_fNBhohXa4dGooTn-F7k9KWnbmy0-a8Vb2P8zc0RdgSJX5n2IkH971dM8JVihRjj7wHTTruw1MaLLcr9s5ggjL3YfCumnugENeZgMbbRbMnT88ybEI10dro0VtfRQEa3CzwcR0NTOMrELLxTCgHKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف ویژه فقط گیگی 170 با تست رایگان
✅
اول تست کن، بعد با خیال راحت خرید کن!
❌
دیگه چرا گیگی ۵۰۰ تا ۶۰۰ بدی؟!
اونم بدون اینکه بدونی کیفیتش چطوره
😐
⚡️
تخفیف ویژه محدود
⏳
فقط تا پایان امشب
🌍
آی‌پی استار واقعی + پینگ عالی
🛡
ضمانت بازگشت وجه بدون شرط
🚀
اتصال پایدار و بدون قطعی
خرید آنی از ربات :
Id :
@LexVipBot
تایم سرورامون نامحدوده
❤️
Link chanel :
@lex_server
رایگان گذاشته میشه هرشب تو‌چنل بالا از دست ندید
👌</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/120091" target="_blank">📅 10:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120090">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a3e47e4.mp4?token=ANOZ7LEJH6iQWkpQCKSeT5LwrxqVrpzWe0_fqRH4GbFFeRnqR33jlsmg9qpw9fpNSbM7010IffBTCiDJ29pfQ_foT61Uhdw79msxO3ea8ktdD8i1xXpxPvHMOTps74S2SL5LiIWEa0KZW2LPamZWOLz9G3jZUUCOtCQgRnPNJBmcVg9jUvDNNi4ftAc7luGwtsMsFmHHVTVkQEy6Qe4DumO6x1Btjp5Ha-4UozohYMBA7XRDnsfRYus53ysYBDDCSvf8-I24Hx7LCEcRqDM1_fGr6LPkeFAZkxH9IS-vEzUphFjUmKVTpuXjfn5MqoL4DxQT4_1ifxjCLgOjp2ZvXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a3e47e4.mp4?token=ANOZ7LEJH6iQWkpQCKSeT5LwrxqVrpzWe0_fqRH4GbFFeRnqR33jlsmg9qpw9fpNSbM7010IffBTCiDJ29pfQ_foT61Uhdw79msxO3ea8ktdD8i1xXpxPvHMOTps74S2SL5LiIWEa0KZW2LPamZWOLz9G3jZUUCOtCQgRnPNJBmcVg9jUvDNNi4ftAc7luGwtsMsFmHHVTVkQEy6Qe4DumO6x1Btjp5Ha-4UozohYMBA7XRDnsfRYus53ysYBDDCSvf8-I24Hx7LCEcRqDM1_fGr6LPkeFAZkxH9IS-vEzUphFjUmKVTpuXjfn5MqoL4DxQT4_1ifxjCLgOjp2ZvXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پاسخ مدیرعامل انویدیا به احتمال فروش تراشه به هواوی
🔴
جنسن هوانگ، مدیرعامل انویدیا، در پاسخ به پرسش خبرنگار مبنی بر فروش تراشه‌های این شرکت به هواوی، این سؤال را عجیب دانست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/120090" target="_blank">📅 10:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120089">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
رویترز: سهام بوئینگ پس از آنکه ترامپ گفت چین موافقت کرده ۲۰۰ جت بوئینگ بخرد، ۴٪ کاهش یافت — که بسیار کمتر از انتظارات برای قراردادی احتمالی با ۵۰۰ هواپیما بود که پیش از دیدار او با شی جین‌پینگ مطرح شده بود.
🔴
سرمایه‌گذاران واکنش منفی نشان دادند زیرا جزئیات سفارش هنوز نامشخص است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/alonews/120089" target="_blank">📅 10:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120088">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
بلومبرگ: از روز یکشنبه تاکنون ۹ نفتکش نفت و گاز از تنگه هرمز عبور کرده‌اند/ برخی از این ۹ کشتی همچنان در محدوده محاصره آمریکا در تنگه هرمز قرار دارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/120088" target="_blank">📅 10:17 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120087">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
پایان سفر ترامپ به چین
🔴
ترامپ سوار ایر فورس وان شد و سفر خود به چین را به پایان رساند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/120087" target="_blank">📅 10:12 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120086">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tmj3dqcfe8XbnkJRr5pDUqS353LXmgT2SRH6qACRk8rn6-PgcLzX6T1XuVh7LY8nBbrne5lD5PIdNFIkQVrbHx8_VOUFms9Vi6Iy_L11ZnbsbCO4Su9KQ0THIcnLCXfC7OiECpmt3Sarq32pLmqSZTK5JUJhJ1V7DY8ezNNktiDO0bd5ADeHMyBlVeabDdSHrkGjI1RYwghiEsZdOjgdAXXfMgcM25yG3Z-3pwJxLmfv78ZI4l4WcWeMuV3n5JpcSpHgZzNxaMjMDYxDSA5saI1GwHuLmUrr1vtgnkThOSzZXb-OPE7GxmO7vVU0xTHNOa8GVJBksZtiJiBIijsHsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه ایران، اسماعیل بقائی : هر کس در پنهان خیانت کند، در آشکار فاش خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/alonews/120086" target="_blank">📅 10:01 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120085">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
فوری / آمریکا پیشنهاد ۱۴ ماده‌ای ایران را رد کرد
🔴
طبق اطلاعات رسیده به تهران تایمز، دولت آمریکا پاسخ پیشنهاد مکتوب ایران درباره پایان جنگ را داده است.
🔴
گفتنی است ایران پیشنهاد خود را مبتنی بر مذاکرات دو مرحله ای ارائه کرده بود که در مرحله اول منجر به پایان جنگ در همه جبهه ها شده و در صورت تحقق شروط ایران، مرحله دوم مذاکرات که درباره موضوع هسته ای بود، آغاز می شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/120085" target="_blank">📅 09:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120084">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
مارکو روبیو: هزینه‌ای برای ایران هسته‌ای وجود دارد.
🔴
اگر روزی سلاح هسته‌ای به دست آورند، چه چیزی مانع کنترل آن‌ها بر تنگه می‌شود؟ این موضوع به یک مشکل دائمی تبدیل خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/alonews/120084" target="_blank">📅 09:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120083">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ترامپ در کنار شی جین‌پینگ: ما در مورد ایران صحبت کردیم. احساس می‌کنیم در مورد ایران بسیار شبیه به هم فکر می‌کنیم. می‌خواهیم که این موضوع پایان یابد. نمی‌خواهیم که آن‌ها سلاح هسته‌ای داشته باشند. می‌خواهیم تنگه‌ها باز باشند.
🔴
ما در حال حاضر آن را می‌بندیم.…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/120083" target="_blank">📅 09:54 · 25 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
