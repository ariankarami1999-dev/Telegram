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
<img src="https://cdn4.telesco.pe/file/my-KxriZJMXFVhT6rCa8SYVNuzSrFEIjoU0oDsRvyH1Dx4tLCNJa61i8z6tTEeWXabaz-U3igWCi2eG6McHUm1s9xOzWGiq5ptVfN7_eBUFyIB_YAa1aqcZQ7Fct7CqxoodiUXeXqUGWMnVLxK6wXtcKkxjH0YVynGXkhsJdgMFFQC_-JDs8L0xdeiC3RnVsoTywhpiO9fnVRp7w-i8VXEtbnjyETSgl0H9uoB2OqNPptgof47kxUv6f8HuQeVSHt3lsr5UCJhwtTwnJBfXFY_YJaX8okzVxFx1WxsM4-2DMuGXrBuFdc_axnpOjwqoAQYz9LZTsp8HBs015esmLMA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 20:29:25</div>
<hr>

<div class="tg-post" id="msg-17862">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">💢
لیندسی گراهام: به مسئولین ایران می گویم؛ اگر گوش می‌دهید: وقتی از حزب‌ الله برای حمله به اسرائیل استفاده می‌کنید، سیاست جدید این خواهد بود که ما به ایران حمله خواهیم کرد.   @StrategicNews_ir</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/SBoxxx/17862" target="_blank">📅 19:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17861">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار استراتژیک</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d0bcc2190.mp4?token=OUpQ3W4vLq9zB7FwwcJsje1dMqOGhNtRdn-nTM7Adq5pLOx_wT-yNM-Ccxz_BbXhs0qTxLIL_d5FYWmEkv9KdBXDXWJyvYRc_PvASQBpGP_k4ZMQ8bMFr0-e8MyPyDv9gvE7QLG2Zl87GFM31_kZdRNw-TezJd34SNUQqhhVAKiUjftxYwgDrda5gVtkka2KQX-yk-wdQ33KCHo0JNvNCvapSiTRIozbmhX7hsj8MYWAxe13Jmgaw94M1JGeZ-2G8HZw0eAvoR9ws_bPcYoP0vxEFg_u4ZMRFar9os-BeZ7pDDMtHv6oMmp3KBVtx7APbFvPYB5g33l7fLYsWVP2rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d0bcc2190.mp4?token=OUpQ3W4vLq9zB7FwwcJsje1dMqOGhNtRdn-nTM7Adq5pLOx_wT-yNM-Ccxz_BbXhs0qTxLIL_d5FYWmEkv9KdBXDXWJyvYRc_PvASQBpGP_k4ZMQ8bMFr0-e8MyPyDv9gvE7QLG2Zl87GFM31_kZdRNw-TezJd34SNUQqhhVAKiUjftxYwgDrda5gVtkka2KQX-yk-wdQ33KCHo0JNvNCvapSiTRIozbmhX7hsj8MYWAxe13Jmgaw94M1JGeZ-2G8HZw0eAvoR9ws_bPcYoP0vxEFg_u4ZMRFar9os-BeZ7pDDMtHv6oMmp3KBVtx7APbFvPYB5g33l7fLYsWVP2rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
لیندسی گراهام: به مسئولین ایران می گویم؛ اگر گوش می‌دهید: وقتی از حزب‌ الله برای حمله به اسرائیل استفاده می‌کنید، سیاست جدید این خواهد بود که ما به ایران حمله خواهیم کرد.
@StrategicNews_ir</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/SBoxxx/17861" target="_blank">📅 19:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17859">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ درباره لبنان:  من ناامیدم که اسرائیل نمی‌تواند حزب‌الله را از بین ببرد. آنها بدون خراب کردن ساختمان‌ها نمی‌توانند کاری انجام دهند.  من نزدیکم که این کار را به سوریه بسپارم چون او کار دقیق‌تری انجام می‌دهد</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/SBoxxx/17859" target="_blank">📅 18:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17858">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">به گزارش الاخبار، جولانی در جلسه‌ای محرمانه وعده داده که از حزب الله انتقام خواهد گرفت. وی گفته :  «حالا نوبت حزب‌الله است و ما انتقام خود را فراموش نخواهیم کرد»  به نظر می‌رسد  که در صورت حملات آمریکا به ایران، جولانی از وضعیت برای باز کردن جبهه‌ای علیه لبنان…</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SBoxxx/17858" target="_blank">📅 18:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17857">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">من دقیقا نمیفهمم روی چه چیزی به جز پایان موقت ۶۰ روزه جنگ توافق شده؟!  لبنان؟! تنگه هرمز؟! موشکی؟! نیابتی؟!</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/SBoxxx/17857" target="_blank">📅 17:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17856">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ:  اگر ایران تنگه هرمز را ببندد، مذاکره‌کنندگان ایرانی به کشورشان باز نخواهند گشت.</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/SBoxxx/17856" target="_blank">📅 17:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17855">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">قراردادهای میان کشورها تحت فشار (Under Duress)  در حقوق بین‌الملل، قراردادها و معاهدات میان کشورها باید بر پایه رضایت آزادانه (free consent) منعقد شوند. مفهوم Under Duress یا تحت اکراه زمانی اعمال میشود که یک طرف با تهدید غیرقانونی، نیروی نظامی، فشار اقتصادی…</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/SBoxxx/17855" target="_blank">📅 17:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17854">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مدیر Secret Box از اعضای تیم دیپلماتیک کشورمان ممنون است و به شرافتشان درود میفرستد!</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/SBoxxx/17854" target="_blank">📅 17:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17853">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQVL20eEte9l7bo4p0pO-DBtsdbBBILIanC9gOjYcZeXIxw8BQUNkFeeATcPTU52ReCfd-VgeHRTmF8j3ZVB24bDUQwuxm5KiG7MmCZZG2zHDkPqULID_b6PNaeh3BoBUMD6zdLWt7BpEYXrkrDXdTfJ1T6zt1KFsr3rBkBkA884VMXNoe3VwK2xjZaAeUQkjqp8v9T3YXIb2d7df4MtSs815I56V59cXrgPDmSQdzmVNla8VoTdbh9OvZH2gbLIBJhGQshBH38Isp_W-Bd_06Mc9kUCLR5CHz7SONDJSNnjIlKHL7n3-pQSaM9JUciTLkiDOniz68rPN8NnJFWA9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثل اینکه یمنی ها در باب المندب فعال شده اند.</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/SBoxxx/17853" target="_blank">📅 17:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17852">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامپ:  اگر ایران تنگه هرمز را ببندد، مذاکره‌کنندگان ایرانی به کشورشان باز نخواهند گشت.</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SBoxxx/17852" target="_blank">📅 17:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17851">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ:
اگر ایران تنگه هرمز را ببندد، مذاکره‌کنندگان ایرانی به کشورشان باز نخواهند گشت.</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/SBoxxx/17851" target="_blank">📅 17:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17850">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">— وزیر دفاع اسرائیل، کاتز:
"هیچ محدودیتی برای سربازان ارتش اسرائیل در لبنان برای اقدام به حذف تهدیدها وجود نداشته و وجود ندارد.
آتش‌بس دیروز اعلام شده، ارتش اسرائیل را در تمام مواضع خود در منطقه امنیتی که جوامع شمال اسرائیل را محافظت می‌کند، باقی می‌گذارد.
همانطور که نتانیاهو و من روشن کرده‌ایم: اسرائیل از منطقه امنیتی در لبنان عقب‌نشینی نخواهد کرد".</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/SBoxxx/17850" target="_blank">📅 14:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17849">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j69eTMa9mh-JxRhcJ5fWC1DHj9knDcR3F0BQ7iySgymKCO4dbFsEv3RunTwJdGMChMkNyrZGz8quI6Vb5eH4hYbTHswYFHVjn3hL8kx4ZzEEPb_7CyNGcEiEG4vqrC4ksES5vSZYVBl7SKH82k1xuFri4G5TsUCIgM_1C0jtkMO_47Mw3yzncXH0F5G4Y4JP6Mxh5Ok9N8lH-qYCjpJfveb8gXXzA2y80vkAEqCSJ0hTlWuin3okvWfQOiICf7uWpsMYMp39-lUaqurZkMP-ucWu14JlsNuv3hg9JjPY-ScbWMAet6eW3MniuzofUCXKCbgfJlNxIvwUEnTBa01Umw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
فدرال رزرو و پیام Hawkish به بازارها
در نشست فدرال رزرو آمریکا در ۱۸ ژوئن ۲۰۲۶، نرخ بهره بدون تغییر باقی ماند، اما لحن سیاست‌گذاران به‌وضوح
Hawkish
بود.
✔️
اعضای کمیته
FOMC
تأکید کردند که ریسک تداوم و حتی تشدید تورم همچنان بالاست. همچنین داده‌های
Dot Plot
نشان داد که بسیاری از اعضا احتمال یک مرحله افزایش نرخ بهره در ماه‌های آینده را منتفی نمی‌دانند.
اگرچه در داخل
FOMC
اختلاف‌نظرهایی وجود داشت، اما دیدگاه غالب این بود که
Rate Cut
در شرایط فعلی چندان مناسب نیست و در صورت لزوم حتی گزینه
Rate Hike
نیز می‌تواند مطرح شود.
🔽
واکنش بازار سریع و قابل‌توجه بود؛ پس از انتشار بیانیه،
USD
تقویت شد و انتظارات معامله‌گران نسبت به سیاست‌های انبساطی کاهش یافت.
نکته مهم اینجاست که بازار انتظار یک
Full Hold
(ثبات نرخ بهره بدون هیچ‌گونه سوگیری مشخص) را داشت، اما فدرال رزرو با اتخاذ یک
Hawkish Hold
نشان داد که همچنان نسبت به تورم نگران است و برای حفظ سیاست‌های پولی انقباضی آمادگی دارد.
🕯
جمع‌بندی:
فدرال رزرو برخلاف انتظارات بخش قابل‌توجهی از بازار، سیگنالی انقباضی ارسال کرد. این موضوع باعث افزایش تقاضا برای
USD
شد و تا زمانی که فشارهای تورمی به‌طور محسوسی کاهش پیدا نکنند، می‌تواند از دلار حمایت کند.
💬
برای کسب اطلاعات بیشتر، با آیدی آموزش (
@CWedu
) و یا شماره تماس 09908006002 در ارتباط باشید.
@CyclicalWaves</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/SBoxxx/17849" target="_blank">📅 12:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17848">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⭕️
رئیس سازمان بازرسی کل کشور
:
سرویس اینترنت پرو متوقف شد و مبالغ کاربران باید عودت داده شود</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SBoxxx/17848" target="_blank">📅 12:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17847">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🗯
دونالد ترامپ ؛ رئیس دولت آمریکا
:
آنتروپیک دیگر تهدیدی برای امنیت ملی آمریکا نیست
وی در مصاحبه جدیدی اعلام کرد که پس از اقدامات اخیر شرکت آنتروپیک، دیگر این مجموعه و مدیرعامل آن را تهدیدی برای امنیت ملی آمریکا نمی‌داند. این موضوع پس از آن مطرح شد که آنتروپیک در پاسخ به دستور دولت، دسترسی کاربران خارجی به مدل‌های پیشرفته Fable 5 و Mythos 5 را مسدود کرد
اگرچه ترامپ از سرعت عمل و رفتار مسئولانه مدیرعامل آنتروپیک تمجید کرد اما همچنان احتمال استفاده از اختیارات اضطراری قانون تولید دفاعی را برای خود پابرجا نگه داشت. در‌همین‌حال، شرکت آنتروپیک نیز بر تعهد خود برای همکاری با دولت آمریکا جهت حفظ امنیت زیرساخت‌ها و پیشتازی در این فناوری تأکید کرده است</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SBoxxx/17847" target="_blank">📅 12:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17846">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MAJpe4MrPLzHRqZgMASF7FNWnQNOYH1DC6rg0ZVHUSmQoHR06hX0jlBdhYoignm5U5dNKrhmGOQGRSGTv52ErQolTZIXVhhEWA0CiX4GZOF1XkSccy7EluR643-BXkXspw_Uq4S8Q2j9YcusKcsda8st27zgymTF1IBvBjMbja8oKmq1WCUWzE0PkLOmX16XiFLMJvH0hSqNnRteB535LEPPegwRjnAP-jcLOynUFrFZ5lPkaICiMA_02iCqtKYRBQXnAWnDKNPJu9Np6y6N9PYGKNFv9pmvs5smIlVVO_GMxFDRLtgyoVyk9RWefb9HO6LVvq9F6Y5X5frqJzt7mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمیدانم ولی اگر بیعت کرده قطعاً مصعب سرش کلاه گذاشته بعداً</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SBoxxx/17846" target="_blank">📅 11:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17845">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پزشکیان:  تنها نکته آمریکا این است که ما بمب اتم نداشته باشیم؛ این موردی است که رهبر شهید هم بارها فرمودند ما بمب اتم نمی‌خواهیم. آمریکا گفت همین را بنویس و امضا کن، ما هم امضا کردیم.</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SBoxxx/17845" target="_blank">📅 11:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17844">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پزشکیان:
تنها نکته آمریکا این است که ما بمب اتم نداشته باشیم؛ این موردی است که رهبر شهید هم بارها فرمودند ما بمب اتم نمی‌خواهیم. آمریکا گفت همین را بنویس و امضا کن، ما هم امضا کردیم.</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SBoxxx/17844" target="_blank">📅 11:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17843">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">حسین شریعتمداری: مسئولان نظام برای بازگرداندن  بحرین به سرزمین اصلی ایران اقدام کنند  حسین شریعتمداری نوشت: «هموطنان بحرینی‌مان بارها اعلام کرده‌اند که خواستار پیوستن به ایران یعنی وطن اصلی خود هستند و انتظار آن است که مسئولان دست‌اندر‌کار نظام این خواسته…</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SBoxxx/17843" target="_blank">📅 11:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17842">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نبرد دریای سرخ: اسرائیل نمایندگی دیپلماتیک خود را در سومالیلند افتتاح کرد  اسرائیل چند ماه پس از به رسمیت شناختن استقلال سومالیلند، یک سفیر برای این منطقه منصوب کرد. دیپلمات مایکل لوتِم پیش از این سفیر اسرائیل در کنیا، آذربایجان و قزاقستان بود.  در ماه ژانویه،…</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SBoxxx/17842" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17841">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">شریعتمداری:   مسیر دفع محاصره دریایی آمریکا؛ شلیک موشک‌های ۲۵۰۰ کیلومتری با کلاهک سنگین به سمت باب المندب است</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SBoxxx/17841" target="_blank">📅 10:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17840">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">روزنامه وال استریت ژورنال:  آمریکا پیشنهاد داده ایران فقط برای خرید دارو، غذا و کالاهای بشردوستانه به ۶ میلیارد دلار دارایی مسدودشده‌اش در قطر دسترسی داشته باشد؛ ایران هنوز این طرح را نپذیرفته است.</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SBoxxx/17840" target="_blank">📅 10:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17839">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">روزنامه وال استریت ژورنال:
آمریکا پیشنهاد داده ایران فقط برای خرید دارو، غذا و کالاهای بشردوستانه به ۶ میلیارد دلار دارایی مسدودشده‌اش در قطر دسترسی داشته باشد؛ ایران هنوز این طرح را نپذیرفته است.</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/17839" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17838">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">آقایان عراقچی و تیم همراه علیرغم ادامه و تشدید حملات اسرائیل به جنوب لبنان عازم ژنو شدند!</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/17838" target="_blank">📅 09:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17837">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامپ:   «در طول دوره آتش‌بس، به مدت ۶۰ روز هیچ عوارضی در تنگه هرمز دریافت نخواهد شد و پس از انقضای این دوره ۶۰ روزه نیز هیچ عوارضی دریافت نخواهد شد، مگر اینکه توسط و برای ایالات متحده آمریکا وضع شود، در صورتی که توافق به پایان نرسد، به عنوان جبران هزینه‌های…</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/17837" target="_blank">📅 08:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17836">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ:
«در طول دوره آتش‌بس، به مدت ۶۰ روز هیچ عوارضی در تنگه هرمز دریافت نخواهد شد و پس از انقضای این دوره ۶۰ روزه نیز هیچ عوارضی دریافت نخواهد شد، مگر اینکه توسط و برای ایالات متحده آمریکا وضع شود، در صورتی که توافق به پایان نرسد، به عنوان جبران هزینه‌های گذشته، حال و آینده برای خدماتی که به عنوان فرشته نگهبان برای کشورهای خاورمیانه ارائه شده است».</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/17836" target="_blank">📅 08:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17835">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">هشدار فوری مجدد نیروی دریایی سپاه روی سیگنال رادیویی برای گشودن آتش روی هر شناوری که به تنگه هرمز نزدیک شود.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17835" target="_blank">📅 01:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17834">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کمرنگ شدن اهرم هرمز؛ چگونه امارات در حال خنثی‌سازی یکی از مهم‌ترین ابزارهای فشار ایران است؟  برای بیش از چهار دهه، تنگه هرمز یکی از مهم‌ترین اهرم‌های ژئوپلیتیکی ایران محسوب می‌شد. حدود یک‌پنجم تجارت دریایی نفت جهان از این گذرگاه عبور می‌کند و هرگونه تهدید…</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17834" target="_blank">📅 01:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17833">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlmxc6V38210dh3cIcwHvI3MaUqZo1LfJnlDiO523Yg5FS6sSgbTgdwolSVRVp2kQ_Roe9MVwU3oweTxCIIuN4_Ivz3-5FwLp39s4MbTOggrF3ysgC7IoLu4TCndXlb8tPqFdQpmTuS18A5ILAMLkgphtuEQ3A3HrrASDOY_oSL47xd9Q-YWIj5Xbdawl1O1xKwsrXu6stm23BZWWi-Li-gOtxjMyjpsnzxLd_4Yg2e1hcasRE9n1B72WhwbTB94zy45g2HUpwKOk4FZ9tbk6Amd1LJPmcAji2wL8vtvud79TaT4qEh01kVh7aCKFlBmbhn0qPUSL4Z-i23N1jlpSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادداشت ترجمه شده: جنگ آینده، جنگ سیستم‌عامل‌ها  دانیلو تسوک، رئیس مرکز هوش مصنوعی وزارت دفاع اوکراین، پیش‌بینی می‌کند که جنگ در سال‌های آینده با یک پارادایم جدید مواجه خواهد شد: جنگ سیستم‌عامل‌ها. او معتقد است که هوش مصنوعی در حال تغییر بنیادی شیوه جنگ است…</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/17833" target="_blank">📅 00:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17832">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e185e8d16.mp4?token=RuV2DcuGyBY-afZeDDVdY-56Y6V9GueLYsDuxRY01mOf1fTJKBvaC1zwgLX84h9HR0xVCBxf21lvSAbr-N4U6jjW-t1FHJSKwiCrA6gS9dJS3abnoMqMcq5pIM4k8nQLYX1F4-bpA6LFIKzhY4EQol6VEnTpWJny6AsblfsEsyHok8620YaxUUJw5LCU62sdwvMXXqtCD4Lj5hmT2g_e-G647bYmKYmfqlRoBXQqfVfRi9GlTo0OjuS4U_Cd4eO3vqHfSVncwKoIRTBP-_SoQL_uVAZsBQx8kpGLAvG7xuj3As5_TOJGtwND3ck_Cnkg-6S4o__Pb02nT5LY7DGdNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e185e8d16.mp4?token=RuV2DcuGyBY-afZeDDVdY-56Y6V9GueLYsDuxRY01mOf1fTJKBvaC1zwgLX84h9HR0xVCBxf21lvSAbr-N4U6jjW-t1FHJSKwiCrA6gS9dJS3abnoMqMcq5pIM4k8nQLYX1F4-bpA6LFIKzhY4EQol6VEnTpWJny6AsblfsEsyHok8620YaxUUJw5LCU62sdwvMXXqtCD4Lj5hmT2g_e-G647bYmKYmfqlRoBXQqfVfRi9GlTo0OjuS4U_Cd4eO3vqHfSVncwKoIRTBP-_SoQL_uVAZsBQx8kpGLAvG7xuj3As5_TOJGtwND3ck_Cnkg-6S4o__Pb02nT5LY7DGdNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حالی که سنتکام میگوید تنگه هرمز باز است، اژدهای بندر نظر دیگری دارد!</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/17832" target="_blank">📅 23:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17831">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">رسانه های اسرائیل:   عملیات ها در لبنان متوقف شد اما نیروهای ارتش اسرائیل هیچ عقب نشینی در لبنان نخواهند داشت.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/17831" target="_blank">📅 20:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17830">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اوکراین در حال جایگزینی مردان از دست رفته با وارد کردن  مردهای بیگانه است!  در هند، بنرهای دولتی اوکراین نصب شده‌اند که هندی‌ها را تشویق می‌کنند به اوکراین مهاجرت کنند تا «خانواده‌ای تشکیل دهند» و «شغلی پیدا کنند». این بنرها زنان اوکراینی جذاب و مجرد را نشان…</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/17830" target="_blank">📅 19:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17829">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjB6AszOgJqjtQpF9hlJZG145S3StlA0clRuORP8v-FrJsbhfwXRA6A6YY_hIjk_cFm0PQndejILvYQktV7wNW8Ga5PA5TYvMZxVtba33KIXpNhvMIc4jw8jJZvmSfDGfAMwvfahRTZN6Zce4na3A7VpqIWJ3zFaSBbJAwIiFKMOrqylt1feK4xN9bIwYTNzUFv6jmiDT8bd0qpuNMPT2SbL74udPPzi3jaf7-L45odTVgc2dwPAgbqCstu1UASGem-7vQjYdVziuWbXHLV-wnvKS_ZIGLACpD3CCyd63AmM-bq8XlXIoddvU0PhebRF1kF95RFUKPZfRNX3OsEfKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوکراین در حال جایگزینی مردان از دست رفته با وارد کردن  مردهای بیگانه است!
در هند، بنرهای دولتی اوکراین نصب شده‌اند که هندی‌ها را تشویق می‌کنند به اوکراین مهاجرت کنند تا «خانواده‌ای تشکیل دهند» و «شغلی پیدا کنند». این بنرها زنان اوکراینی جذاب و مجرد را نشان می‌دهند. در هند به دلیل فرهنگ پسرپرستی، کمبود زنان وجود دارد و زنان اغلب در صورت اطلاع از دختر بودن جنین، سقط جنین می‌کنند.
در مرحله اول، برنامه‌ریزی شده است که ۳۰۰٬۰۰۰ مهاجر وارد شود.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/17829" target="_blank">📅 19:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17828">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">رسانه های اسرائیل:   عملیات ها در لبنان متوقف شد اما نیروهای ارتش اسرائیل هیچ عقب نشینی در لبنان نخواهند داشت.</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/17828" target="_blank">📅 19:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17827">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCtJ9vZG9Y92J2iLwDC0WHh9LDspX4DL3nDUw8fX5jQbP8vRHcqm8xjGXRKY2PcUeOzamIb8rhRcoxiih4wr6CITjSQXVUErcQ8C3zqZ9A65xcUPNNL8VrhTnHb7FpYRwbOhlLQUzP_DGiBgMBZdmAZDk_o7dJ5nw9XOZ8ElBx7Uv5ejKktqEu0LMJEM4W67EScIa7Rm890r33MQ_QSJgN7W04OL9H_fqWbLqybloGSVflc9OeNyN2QbWsLB7j7hJN4fMJejItenddlpj2WfQYAyBAuH8fUBkB-DVevdPnPhX7kFDctpL9oaQfN1VT4k_J60qRqjcWwedWQPW3ZzHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عثمانی ها جوری مهمتچیکلر فوتبالی شان را بدرقه کردند که انگار دیگر نیمه نهایی در جیب شان است!  اکنون با 2 باخت 0 امتیاز دارند و بازی بعدیشان هم با آمریکای جنایتکار بی رحم است!  ُسبحان الله!</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/17827" target="_blank">📅 18:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17826">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">رسانه های اسرائیل:
عملیات ها در لبنان متوقف شد اما نیروهای ارتش اسرائیل هیچ عقب نشینی در لبنان نخواهند داشت.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/17826" target="_blank">📅 18:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17825">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">قرارگاه مرکزی خاتم‌الانبیا اعلام کرد نظر به بدعهدی و پیمان‌شکنی آشکار آمریکا نسبت به‌عدم اجرای بند اول تفاهم‌نامه پایان جنگ، و در واکنش به نقض بی‌وقفه و مستمر آتش‌بس از سوی اسرائیل در جنوب لبنان و همچنین با توجه به‌عدم عقب‌نشینی ارتش این کشور از لبنان، تنگه…</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/17825" target="_blank">📅 17:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17824">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">قرارگاه مرکزی خاتم‌الانبیا اعلام کرد نظر به بدعهدی و پیمان‌شکنی آشکار آمریکا نسبت به‌عدم اجرای بند اول تفاهم‌نامه پایان جنگ، و در واکنش به نقض بی‌وقفه و مستمر آتش‌بس از سوی اسرائیل در جنوب لبنان و همچنین با توجه به‌عدم عقب‌نشینی ارتش این کشور از لبنان، تنگه…</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/17824" target="_blank">📅 17:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17823">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">قرارگاه مرکزی خاتم‌الانبیا اعلام کرد نظر به بدعهدی و پیمان‌شکنی آشکار آمریکا نسبت به‌عدم اجرای بند اول تفاهم‌نامه پایان جنگ، و در واکنش به نقض بی‌وقفه و مستمر آتش‌بس از سوی اسرائیل در جنوب لبنان و همچنین با توجه به‌عدم عقب‌نشینی ارتش این کشور از لبنان، تنگه هرمز مجددا بسته خواهد شد.
قرارگاه مرکزی خاتم‌الانبیا اضافه کرد این گام اول «پاسخ به عهدشکنی دشمن» است و در صورت ادامه این وضعیت، گام‌های بعدی برای «پایبند کردن دشمن به اجرای تعهدات»، برنامه‌ریزی و اقدام خواهد شد.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/17823" target="_blank">📅 17:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17822">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">یارانۀ 2 دلاری خرداد به حساب سرپرستان خانوار دهک‌های ۴ تا ۹ واریز شد</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17822" target="_blank">📅 16:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17821">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tur9U36vkBPZH8-Aw56gdYBXvfCacI8QybbfOSafjaqWUZjg6meCZ7mkDMfs3C_-DXtFZy_qJAFKVQrjaGzq1oCZNy3Kzpnq-MQYWDULfef-nr9fajh37iSOQdAS9CeQixKiabVd0riRfIVyBT0Q6-Vwup8_MuzD5TF9tN3TcA5MhUvj42Y52kwtP789udG0s5-gDsF3Ghbi45VfvzSFtCVFSYnIWLIw1saJcC-DwWxyIaKyMGELqhicHjvUHRVqV-VmxokJTWW4Oz8tAMcOVIDZVi8_3KaUk743Awwxku20THP6QbegdFmXW8lq9VWshUn_oKvY15gRWh7ncf7SoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لابد چون نظامیان می دانند درگیر شدن با ارتش اول دنیا و یک قدرت هسته ای با فنآوری بالا با توییت ریدن زیر کولر متفاوت است؟!
یک بار از بچه های پدافند و لانچر و ... بپرسید شرایط چطور بود؟!</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/17821" target="_blank">📅 16:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17820">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">همه ایران و انیران خواستار ابطال این پیمان هستند جز باقر!</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/17820" target="_blank">📅 16:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17819">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">همه ایران و انیران خواستار ابطال این پیمان هستند جز باقر!</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17819" target="_blank">📅 16:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17818">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بخدا سوگند که ما هم خواستار ابطال این تفاهم نامه هستیم!</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/17818" target="_blank">📅 15:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17817">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmMoFkjoSBpwi1lsmqB2voUTVy1TEnu3bkDPG644XezpujqTepLY9opGfo9kyajgpqvbIjYm7K5b6paksMMHN5Ei6Je9dasN-e8a1BjFBiVZaaZCkbhT3pF29SfWwydCBlo-iVwJdZtGXSR_he6iUioeo7wRMneuVD8zrd5h19hhSc6jvIA0iyYDyYmAtQWlHsMkqSKiV7eoawWCw1L1m-1jnxz4yRUekEI_k-Hi-vTibv4Goyht4TiPk4qaqBkUGJgHu5WZgg7_y-QKRJlZ73EM39KHKc2lAZfPKxEHWYUvanZX-Hcg_KPNgBUA529kGNtCUHqB68P2498reVc2eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/17817" target="_blank">📅 15:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17816">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">آقایان عراقچی و تیم همراه علیرغم ادامه و تشدید حملات اسرائیل به جنوب لبنان عازم ژنو شدند!</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/17816" target="_blank">📅 15:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17815">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">آقایان عراقچی و تیم همراه علیرغم ادامه و تشدید حملات اسرائیل به جنوب لبنان عازم ژنو شدند!</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/17815" target="_blank">📅 15:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17814">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMOoYZovzT8RFw133pZ_uUiqG_aDMnePDqSQOkNyzIy4DWH7l7ZxdwHO4W0a15-TwmIKXtuzcMgtpzSbe5jXX7JI3bwb1GJx03LLQ7Gj6_MIKXyKghPR6UueZqgFbFpc1jTGsiMq1Lgh6v7xxl4jAQCg7mT4-DveerquboLuZibeFh7D6yKJ0xKBxACw51Fn_YhLsKkgoHPEP2DWMOjkFQsz9bwHXXica9r3p6q2LRtiIw0Ap9Q-rZnvN49OqwHbwvuoZLRJxwG4oofFD3gZmCnIk4gVYVMt6aP9Tg3y2p23Ac6uJEysU1nGiF9YEyrdkLYnhQ6Vk49RE6CmM4P0wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادداشت ترجمه شده: جنگ آینده، جنگ سیستم‌عامل‌ها
دانیلو تسوک، رئیس مرکز هوش مصنوعی وزارت دفاع اوکراین، پیش‌بینی می‌کند که جنگ در سال‌های آینده با یک پارادایم جدید مواجه خواهد شد: جنگ سیستم‌عامل‌ها. او معتقد است که هوش مصنوعی در حال تغییر بنیادی شیوه جنگ است و در سه تا پنج سال آینده، اگر درگیری با روسیه ادامه یابد، جنگ به رقابت بین سیستم‌های هوشمند تبدیل خواهد شد.
اوکراین، که پیش از تهاجم روسیه در سال ۲۰۲۲ سرمایه‌گذاری چندانی در پهپادها نداشت، اکنون به پیشتاز جنگ پهپادی تبدیل شده است. این کشور از هوش مصنوعی برای برنامه‌ریزی عملیات رزمی، تحلیل حملات موشکی روسیه و هدایت پهپادها استفاده می‌کند. تسوک می‌گوید: سیستمی که داده‌های بیشتری دارد و بهتر آنها را درک می‌کند، راه‌حل‌های بهتری پیشنهاد می‌دهد و برتری خواهد داشت.
مرکز هوش مصنوعی اوکراین، که در مارس ۲۰۲۶ تأسیس شد، در حال توسعه یک سیستم عامل واحد است که تمام داده‌های میدان جنگ را تحلیل کرده و تصمیمات را از سطح یگان‌های جلویی تا فرماندهی استراتژیک تسریع می‌بخشد. هدف، ادغام سلاح‌ها و سیستم‌های داده‌ای در یک ارگانیسم زنده واحد است که به صورت هماهنگ عمل کند.
جنگ اوکراین به یک مسابقه تسلیحاتی فناوری تبدیل شده است. شرکت‌های خارجی مانند Palantir سیستم‌های خود را در اختیار اوکراین قرار داده‌اند و پروژه Brave1 Dataroom  برای اشتراک‌گذاری داده‌های میدان جنگ با متحدان ایجاد شده است. روسیه نیز در حال توسعه قابلیت‌های هوش مصنوعی خود است و از آن برای برنامه‌ریزی حملات پهپادی و موشکی استفاده می‌کند.
تسوک می‌گوید: سوال این است که چقدر سریع می‌توانیم راه‌حل‌های خود را بسازیم و چقدر عملی آنها را پیاده‌سازی کنیم تا تأثیر اصلی را در میدان جنگ بگذاریم.  اوکراین در حال حاضر بر اصل حضور انسان در حلقه تصمیم‌گیری تأکید دارد، اما تسوک هشدار می‌دهد که ممکن است روزی برسد که سیستم‌های خودمختار آنقدر سریع عمل کنند که حضور انسان، تصمیم‌گیری را کند کند. در آن صورت، سوال این خواهد بود: چگونه می‌توانیم با تصمیماتی که سیستم‌های خودمختار پیشنهاد می‌دهند، همگام شویم؟</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17814" target="_blank">📅 15:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17813">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iodp0nAtmfWRIbVoY53mU_bRpnFxmFIwx4HxiNyWTxjzc6qRioogZZwpvWVt-U6jKPx5GoNKn6tkAk0iAmu9ta1GakphdfBw0beTwhSOWeN48FrEp8BUglH7D3DnKkK1ocOgI6QGSN3Wqhm8P4PlhYIQVvq06ZUMJ2NtJBUPYLKLy-RBMgkfRAW5wI9vr_t3YstXnRalj-41qPOp65jyQdhkTtjA5Irv1qpZAe4o4b1eb8tCeYdFrTLgdUDoFeidAotvY0GC3pR9aNq9i2dGpLi00v8g3cr7QsozVRXB4YTh0MxEV6P3ZWnHQW4B_U6wJCYhDphONR3CfpxftwDjPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عثمانی ها جوری مهمتچیکلر فوتبالی شان را بدرقه کردند که انگار دیگر نیمه نهایی در جیب شان است!
اکنون با 2 باخت 0 امتیاز دارند و بازی بعدیشان هم با آمریکای جنایتکار بی رحم است!
ُسبحان الله!</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/17813" target="_blank">📅 13:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17812">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وزیرخارجه فاکستان هنگام استقبال از مهمانان نشست اسلام آباد زمین خورد!</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/17812" target="_blank">📅 13:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17811">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e024f4add.mp4?token=sJUFx2ZiKLJB5Z4AJVSx8UOdw_CPiwV7qIko5oEBopw_iN0TDMcNA4GJQYatZC19bc-ShQ9MAqxaUeJZk5-dESndOaty8EUDWDNv2COiU0UWvs0GHLNZcFGyfpyAVBSNNPXxpLPO_Z6ZnZQpYDUFZvD3ozW5iY_5Rlvba9gsEOQicbRn5fFLkFUbngvxEGKRCt6Wh8OkQ-2iv4Uce_KZXoEEZAe6nWtdWX56M-zcasnb5Kx2kZ4TSNbk4CaKeXdgjdzjkTWuovRXmQQC3kUyxd3KPpM7QL8GDFAHdL3cpZafl4Zh8mvLwDuSd415kKu6TIw3lTcFgB3efB9hjK4v2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e024f4add.mp4?token=sJUFx2ZiKLJB5Z4AJVSx8UOdw_CPiwV7qIko5oEBopw_iN0TDMcNA4GJQYatZC19bc-ShQ9MAqxaUeJZk5-dESndOaty8EUDWDNv2COiU0UWvs0GHLNZcFGyfpyAVBSNNPXxpLPO_Z6ZnZQpYDUFZvD3ozW5iY_5Rlvba9gsEOQicbRn5fFLkFUbngvxEGKRCt6Wh8OkQ-2iv4Uce_KZXoEEZAe6nWtdWX56M-zcasnb5Kx2kZ4TSNbk4CaKeXdgjdzjkTWuovRXmQQC3kUyxd3KPpM7QL8GDFAHdL3cpZafl4Zh8mvLwDuSd415kKu6TIw3lTcFgB3efB9hjK4v2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیرخارجه فاکستان هنگام استقبال از مهمانان نشست اسلام آباد زمین خورد!</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/17811" target="_blank">📅 13:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17810">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">➡️
استارلینک با مجوز دولت عراق ، بطور رسمی در این کشور فعالیت خودرا آغاز کرد</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17810" target="_blank">📅 11:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17809">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">📡
طالبان با دستور مستقيم ملا هبت الله آخندزاده رهبر این گروه در افغانستان ،  استفاده از گوشی های هوشمند را برای تمامی کارکنان نظامی و غیر نظامی خود ، ممنوع کرد</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17809" target="_blank">📅 10:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17808">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pq7w9rBEUh6uuh9KgCLRwXA0MrRa7CUWcHMVRqKX8IICNmKLljWOjPxb3YFhqG4e_iaacLy-kw8Hnhx1WiA77DBMfJZmoz4jtCWxsev26X6dt8sVygrfdyvBKwnPOLVfKwXcZgk3i5m9bHZzuhR5_IhOedhQlPqje1iFNdMeg0Dq_CGgv_CinunNLltHfmAuxziRqEFllbR5bsgH1dLjAxxfvlRUtEBkXwjYvW-pOtBZ8QAd7ooho42az8hTUtFm1-_-2vTAKOuywuuaLKNbIPNtG0E-OkJHldvwto1j1WMjmbZ19BHlaLJjpvYN8raLYaUkURekixHSsiYycN8f0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ این مردک مجاهد خلق را رهبر اپوزیسیون ایران معرفی کرده!
این همان گهی است که 24 سال پیش برنامه هسته ای ایران را لو داد</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/17808" target="_blank">📅 10:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17807">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">بلومبرگ: اتحادیه اروپا برنامه‌ریزی برای شراکت استراتژیک در زمینه مواد خام با ایالات متحده علیه چین کرده است  اتحادیه اروپا در نظر دارد با ایالات متحده بر سر نقشه راهی برای شراکت استراتژیک و توافقی درباره مواد معدنی حیاتی به توافق برسد. هدف کاهش قابل توجه نفوذ…</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/17807" target="_blank">📅 09:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17806">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smrde3y0Vg7TJU6mWHp48w8deyrVRf99wRilXhRStpyPULdLNf3B18Vr03KdC9Ned3Cma7DfGgQxxBTpjH6gaNZRkUdIRyiPpOel-QZPpcl2pK40-wldviVE_4PNH-l8G0gt6lQTkBXBHYYXwdyfgt0JwPwhRUMSrgN1vnwrrt9QlmJjwmKP5oJmfbZuJVJdqr0-Vdrim3N7OMC-ZtMCzXfZc_OSQAAjGoUjUlAG0sdbiPJ8EwcTmXjyBdoJ8MGxH1ehjEUCp9Tf3PCNnXp8Pi-Tu5Kf48wVl4mern0uzDoJOCQDS1r2E4tLFzyDjOF1NMUNDAKlY9yt9UBhXQdHgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شورای شهر نبطیه اعلام کرد با توجه به خطر احتمال بالای اشغال شهر و شدت درگیری مراسم تاسوعا و عاشورا لغو از شهروندان می‌خواهیم از شهر خارج شوند.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/17806" target="_blank">📅 01:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17805">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eeWYJYCBO5Ok9tZKBG0hw5wJ3Ko8dvj9jQPeSHANf24XsOmRsF6X5Rs7oTnK8y5SRw4ZkhGpX9GS5V9YGu0TPReAvULUESSNGRdZPUg45Qe41_ADSJGqdo6CgDsgfI2Tq6CDNJVtUpYw-3mZ3q_td1_I7D9ftNd5p1v0Dt1DdE73e0PQSGcZE4ao0St7gnFlOrDiA7nAirFehkE-VD5BlNcRJfp9PiDgKhqwM5inHajGZQe7JeCHrvwL4lOPfMsiL2Nm_sg5XrySWKPU4rmJD6jmfYQc1V23_2Cwcj3_XueGfM0RvAeE8V7aUr3LMhooYZJZ0DIroMQWprfMATDv9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقایقی قبل ترامپ در توییتی اعلام کرد که ایرانی ها مسئول سقوط بالگرد آپاچی آمریکایی در تنگه هرمز بوده اند.  او اعلام کرد که ایالات متحده باید به این حمله پاسخ دهد.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/17805" target="_blank">📅 00:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17804">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">محسن رضایی:
به خطای دشمن شدیدتر از آنچه بوده پاسخ می دهیم.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/17804" target="_blank">📅 00:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17803">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">جی‌دی ونس درباره پیشنهاد آمریکا به ایران:  «گزینه اول این است که همچنان مانند یک حکومت تروریستی رفتار کنید؛ در این صورت، به‌معنای واقعی کلمه هیچ چیزی به دست نخواهید آورد.  گزینه دوم این است که مانند یک حکومت عادی رفتار کنید؛ در آن صورت، ایالات متحده واقعاً…</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/17803" target="_blank">📅 22:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17802">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">چقدر این ونس ترنس گه می خورد آخر هفته ای....خفه شو دیگر</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/17802" target="_blank">📅 22:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17801">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">— رئیس‌جمهور آمریکا ترامپ:
"ایرانی‌ها، مردم بسیار باهوشی هستند. آن‌ها نوعی نابغه‌ی بدوی هستند، اما باهوش‌اند.
آن‌ها اسرائیل را منفجر می‌کردند.
اگر من نبودم، اسرائیل امروز وجود نداشت."</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/17801" target="_blank">📅 22:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17800">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">چقدر این ونس ترنس گه می خورد آخر هفته ای....خفه شو دیگر</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/17800" target="_blank">📅 21:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17799">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">خود عربها هم گفته بودند
که قرار نیست سرمایه گذاری بکنند</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/17799" target="_blank">📅 21:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17798">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">متن توافقنامه به روایت فارین پالیسی:     تفاهم اسلام‌آباد بین ایالات متحده آمریکا و جمهوری اسلامی ایران   ایالات متحده آمریکا و جمهوری اسلامی ایران و متحدان‌شان در جنگ فعلی، با امضای این تفاهم‌نامه، خاتمهٔ فوری و دائمی عملیات نظامی در همه جبهه‌ها، از جمله…</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/17798" target="_blank">📅 21:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17797">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">این هم‌ در همین راستا است:  — مقامات اسرائیلی از انتقاد تند معاون رئیس‌جمهور ایالات متحده، جی‌دی وانس، از وزرای کابینه اسرائیل و هشدار ظاهری او مبنی بر اینکه حمایت نظامی ایالات متحده از اسرائیل بی‌قید و شرط نیست، شوکه شدند.  رهبران اسرائیلی عمدتاً از پاسخگویی…</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/17797" target="_blank">📅 21:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17796">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">پس بند 1 توافقنامه که رفت روی هوا.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/17796" target="_blank">📅 20:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17795">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حزب الله عملاً دارد سیگنال ادامه حملات به شهرک های شمال اسرائیل را می دهد؛ یعنی اقدامی که پس از آغاز جنگ آغاز کرد.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/17795" target="_blank">📅 20:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17794">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‌  بیانیه کامل  اتاق عملیات حزب‌الله
🔹
رد ادعاهای دشمن اسرائیلی درباره نقض آتش‌بس توسط حزب‌الله، مقاومت اسلامی تأکید می‌کند که دشمن هرگز از ۲۷-۱۱-۲۰۲۴ تا ۱۶-۰۴-۲۰۲۶ و همچنین نتایج تفاهم اخیر ایران و آمریکا که در بند اول آن پایان جنگ در همه جبهه‌ها از جمله…</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/17794" target="_blank">📅 20:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17793">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‌
بیانیه کامل  اتاق عملیات حزب‌الله
🔹
رد ادعاهای دشمن اسرائیلی درباره نقض آتش‌بس توسط حزب‌الله، مقاومت اسلامی تأکید می‌کند که دشمن هرگز از ۲۷-۱۱-۲۰۲۴ تا ۱۶-۰۴-۲۰۲۶ و همچنین نتایج تفاهم اخیر ایران و آمریکا که در بند اول آن پایان جنگ در همه جبهه‌ها از جمله لبنان تأکید شده است، به هیچ توافق آتش‌بس پایبند نبوده است.
🔹
بلکه دشمن اسرائیلی در نقض‌های مکرر آتش‌بس افراط کرده و کشتارها و تخریب ساختمان‌های مسکونی و زیرساخت‌های غیرنظامی را مرتکب شده است، و به حملات زمینی خود از طریق تلاش برای نفوذ و کنترل روستاها و مناطقی که پیش از توافق نتوانسته بود به آنها دست یابد، ادامه داده است. تحقیر اسرائیل نسبت به آتش‌بس به حدی رسیده است که رئیس ستاد ارتش دشمن، جنایتکار آیال زامیر، دو هفته پیش اعلام کرد «در لبنان آتش‌بسی وجود ندارد»، و سخنگوی ارتش او دیروز مجدداً بر ادامه فعالیت نیروهای اشغالگر در جنوب لبنان تأکید کرد.
🔹
و طبق عادت خود، دشمن برای جبران ناتوانی در مقابله با مجاهدان مقاومت و پوشاندن شکست‌ها و خساراتش در میدان نبرد، به ارتکاب کشتار علیه غیرنظامیان و هدف قرار دادن روستاهای امن روی می‌آورد، همانطور که امروز پس از مقابله مجاهد دلیر با تلاش پیشروی به سمت تپه علی الطاهر در شب گذشته رخ داد.
🔹
مقاومت اسلامی همیشه آماده مقابله با هر تجاوزی است، مجاهدان آن با شجاعت و روحیه حسینی کربلایی از خاک و مردم خود دفاع می‌کنند و با تیرهای خود ارتش دشمن را به سختی می‌زنند، ده‌ها افسر و سرباز آن را کشته و زخمی می‌کنند و در تجهیزات آن آسیب‌های ویرانگری وارد می‌آورند، و میان ما و آنها روزها و شب‌ها و میدان نبرد ادامه دارد.
-جمعه ۱۹-۰۶-۲۰۲۶‌
-۰۴ محرم ۱۴۴۸ هـ</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/17793" target="_blank">📅 20:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17792">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">شیخ نعیم قاسم: ما نقشه‌ای بلندمدت طراحی کرده‌ایم و به راه خود ادامه می‌دهیم.  ما تصمیمی حسینی و کربلایی گرفتیم؛ تصمیمی بدون حد و این تصمیم همچنان پابرجاست و هیچ بازگشتی به وضعیت پیش از ۲ مارس وجود ندارد.</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/17792" target="_blank">📅 20:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17791">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">شیخ نعیم قاسم: ما نقشه‌ای بلندمدت طراحی کرده‌ایم و به راه خود ادامه می‌دهیم.
ما تصمیمی حسینی و کربلایی گرفتیم؛ تصمیمی بدون حد و این تصمیم همچنان پابرجاست و هیچ بازگشتی به وضعیت پیش از ۲ مارس وجود ندارد.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17791" target="_blank">📅 20:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17790">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اطلاعات آمریکا هشدار داد که اسرائیل احتمالاً توافق هسته‌ای ایران را تضعیف خواهد کرد</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/17790" target="_blank">📅 19:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17789">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">در راستای افزایش مخالفت با اسراییل در کشورهای غربی:  آلمان طبق گزارش RIAS، بالاترین تعداد حوادث ضدیهودی را در تاریخ خود ثبت کرد؛ ۸۷۲۵ مورد در یک سال.</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/17789" target="_blank">📅 18:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17788">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27b325ce33.mp4?token=E7n4eI4KUG1z5crs7e8ADcXNTbNNFMTzd_-NczICW4hDgRrBzf24Ela_Zqz-nKabzr-nmk6cIdzeaz1ZUvB7F0BhSGVabKFzGKhuK6Bw1_fY7I0AjqFb0DJZ6rVrIhevvssQhiZaL5yVvdwxi_W-fAGDd1xOdUNLCVdPQ6S0lMS3hN71hzxw8JwCXXz033CE8hj-HNKusPP8hs-6b7NmLXZiP6CG6eWUF5oVL7h7N1z4TxDL3stsSXBD6XGiPKyiJeslvkZWtkUdtFQ3ouefK8T7EKGViEcr9cJ0tQqSwHQJpCRBL7qF5HqMQFFtRag2_9Us9MD7ToyyanHfp0WQnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27b325ce33.mp4?token=E7n4eI4KUG1z5crs7e8ADcXNTbNNFMTzd_-NczICW4hDgRrBzf24Ela_Zqz-nKabzr-nmk6cIdzeaz1ZUvB7F0BhSGVabKFzGKhuK6Bw1_fY7I0AjqFb0DJZ6rVrIhevvssQhiZaL5yVvdwxi_W-fAGDd1xOdUNLCVdPQ6S0lMS3hN71hzxw8JwCXXz033CE8hj-HNKusPP8hs-6b7NmLXZiP6CG6eWUF5oVL7h7N1z4TxDL3stsSXBD6XGiPKyiJeslvkZWtkUdtFQ3ouefK8T7EKGViEcr9cJ0tQqSwHQJpCRBL7qF5HqMQFFtRag2_9Us9MD7ToyyanHfp0WQnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس!</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/17788" target="_blank">📅 18:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17787">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">مسئول ارشد اسرائیلی:   ما در آتش‌بس هستیم؛ اگر حزب‌الله به ما حمله نکند، پس در زمان جنگ نیستیم اما نیروهای خود را در جنوب لبنان نگه می‌داریم</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/17787" target="_blank">📅 17:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17786">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">مسئول ارشد اسرائیلی:
ما در آتش‌بس هستیم؛ اگر حزب‌الله به ما حمله نکند، پس در زمان جنگ نیستیم اما نیروهای خود را در جنوب لبنان نگه می‌داریم</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/17786" target="_blank">📅 17:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17785">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ظاهرا معنی آتش بس از دید نتانیاهو صرفا توقف جنگ از سوی دشمن است.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/17785" target="_blank">📅 16:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17784">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">یک حمله هوایی اسرائیل حدود ۵ دقیقه پس از آغاز آتش‌بس، منطقه نبطیه الفوقا در جنوب لبنان را هدف قرار داد.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/17784" target="_blank">📅 16:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17783">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">یک حمله هوایی اسرائیل حدود ۵ دقیقه پس از آغاز آتش‌بس، منطقه نبطیه الفوقا در جنوب لبنان را هدف قرار داد.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/17783" target="_blank">📅 16:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17782">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامپ:  جنگ ایران را تضعیف کرده است! دیگر نیروی هوایی، نیروی دریایی، تجهیزات پدافند هوایی، رادار یا تقریباً هیچ چیز دیگری ندارد، با این حال دموکرات‌ها می‌گویند که وضعیت ایران اکنون بهتر از چهار ماه پیش است. آیا می‌توانید تصور کنید که با این موضوع کنار بیایید؟…</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/17782" target="_blank">📅 16:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17781">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ:
جنگ ایران را تضعیف کرده است! دیگر نیروی هوایی، نیروی دریایی، تجهیزات پدافند هوایی، رادار یا تقریباً هیچ چیز دیگری ندارد، با این حال دموکرات‌ها می‌گویند که وضعیت ایران اکنون بهتر از چهار ماه پیش است. آیا می‌توانید تصور کنید که با این موضوع کنار بیایید؟ مردم چقدر می‌توانند احمق باشند؟</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17781" target="_blank">📅 16:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17780">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ونس:  برخی عناصر در اسراییل به دنبال ایجاد یک دولت شکست خورده مانند لیبی در ایران هستند!</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17780" target="_blank">📅 15:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17779">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43093b929e.mp4?token=q6etNi8j0pq6U0BcXXaTwBFhXny6h05vSyTggXIuOwqFyLprqpfZ71gyO_Bjqoh7mhJ8GQ8X4nBWLLpCT9C6vNgBnRg-ywv40aXpvd3ZaBJZHAR4jIa0Gr98IxH7JOVWc-bLJdNACWB_MvA3hsHpH2jPTzP2dLVzaPTk0PndYrQL6R1iKGnv9BxBGwLQ8rKrt5VX5xcWumwuwaCfQQDAP-m586k6wZp7OE4ac-Jmd7a8n3ymoq9rEMrZ7ESsBVlcIthv27ZCMkV4mLUEDdx_1RlkTr8YfaXUBIE4kERYeJXHnvcpgKyOfUk1fOHxlAClSdI5D4Z02aHmngRTVq6HOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43093b929e.mp4?token=q6etNi8j0pq6U0BcXXaTwBFhXny6h05vSyTggXIuOwqFyLprqpfZ71gyO_Bjqoh7mhJ8GQ8X4nBWLLpCT9C6vNgBnRg-ywv40aXpvd3ZaBJZHAR4jIa0Gr98IxH7JOVWc-bLJdNACWB_MvA3hsHpH2jPTzP2dLVzaPTk0PndYrQL6R1iKGnv9BxBGwLQ8rKrt5VX5xcWumwuwaCfQQDAP-m586k6wZp7OE4ac-Jmd7a8n3ymoq9rEMrZ7ESsBVlcIthv27ZCMkV4mLUEDdx_1RlkTr8YfaXUBIE4kERYeJXHnvcpgKyOfUk1fOHxlAClSdI5D4Z02aHmngRTVq6HOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دکتر رییسی نژاد استاد تمام عیار ژئوپولیتیک است اما خواننده Secret Box از ۷ ژوئن میدانست متاسفانه استراتژی اسراییلی ها به سمت پلن B یعنی زدن زیرساخت‌ها و ایجاد یک دولت ورشکسته چرخیده است.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17779" target="_blank">📅 15:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17778">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سی‌ان‌ان به نقل از منابع آگاه:
آمریکا به ایران اطلاع داده که اسرائیل حملات خود را در لبنان تشدید نخواهد کرد</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/17778" target="_blank">📅 15:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17777">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sa0EYcidF_LuPg15p45j9ebiPZ6FNHzn8WyTlFXSY7-e_MhuvjDVu8NWF7MBaocfyIoJBc4uemwtHcxvYF1XgLhzKRw4H2MJ6OmpraZjtCG0R7zp1sTtVMxGyISxK6fVGntZNh_hhKfxMTXe7yO4TYAmfXKobUY4-Hq12lBCOOeDWx6PaAaAi9acvsFGUH_hKtwW0y4PfYyDHczVPZccbpTBZ6Gx09W5-_o2UxbFTuZb4HXqtiTgyxNpEFt8C2kxwFFaLgIhGse-TkbesSt-xm_uM52hjwC72fe3zgj-zUq2CV0jCPkucWAX5tKptCI4yUg5S5cti3FEB9R0WGHLaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرندی</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17777" target="_blank">📅 14:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17776">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">نهاد مدیریت آبراه خلیج فارس:   با عنایت به امضای تفاهم‌نامه اسلام‌آباد و ابلاغ دستور مقامات ذیربط، به اطلاع متقاضیان عبور از تنگه هرمز می‌رساند در بازه زمانی اعلام شده، عبور کشتی‌هایی که درخواست عبور خود را با رعایت نکات لازم ارسال نمایند، انجام خواهد شد.</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17776" target="_blank">📅 14:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17775">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نهاد مدیریت آبراه خلیج فارس:   با عنایت به امضای تفاهم‌نامه اسلام‌آباد و ابلاغ دستور مقامات ذیربط، به اطلاع متقاضیان عبور از تنگه هرمز می‌رساند در بازه زمانی اعلام شده، عبور کشتی‌هایی که درخواست عبور خود را با رعایت نکات لازم ارسال نمایند، انجام خواهد شد.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17775" target="_blank">📅 14:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17774">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نهاد مدیریت آبراه خلیج فارس:
با عنایت به امضای تفاهم‌نامه اسلام‌آباد و ابلاغ دستور مقامات ذیربط، به اطلاع متقاضیان عبور از تنگه هرمز می‌رساند در بازه زمانی اعلام شده، عبور کشتی‌هایی که درخواست عبور خود را با رعایت نکات لازم ارسال نمایند، انجام خواهد شد.</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/17774" target="_blank">📅 14:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17773">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">کلا تا اواخر دهه ۱۹۷۰ میلادی، عمده احزاب اسراییلی مبتنی بر ایده های سکولاریستی و مدرن بوده و اغلب سیاستمدارانشان هم اروپایی تبار بودند .
اصرار زیاد بر جذب مهاجران یهودی خصوصا از خاورمیانه و آفریقا (عراق، ایران، یمن، اتیوپی، مراکش …) باعث شکل گیری جوامع عقب مانده حاشیه نشین در اسراییل شد و حزب لیکود هم بر پایه خواسته های اینان قدرت گرفت.
اکنون این سفاردیم ها به سرعت جمعیتشان از اشکنازی ها در حال پیشی گرفتن است چون زادوولد بیشتری دارند و به نظرم از عوامل خشونت های اخیر در غزه و … همین ها بوده اند.</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/17773" target="_blank">📅 14:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17772">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">شاید…</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/17772" target="_blank">📅 14:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17771">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">وزیر امنیت ملی اسراییل ، ایتامار بن گویر:  امشب تهران باید بسوزد!</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17771" target="_blank">📅 14:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17770">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گزارشهایی مبنی بر پیشروی سنگین نیروهای اسرائیلی برای محاصره کامل و تصرف نبطیه!</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/17770" target="_blank">📅 14:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17769">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">در جریان درگیری‌های ۲۴ ساعت اخیر در جنوب‌لبنان تاکنون ۴ سرباز اسراییلی کشته شده و ۱۷ تن دیگر زخمی شده‌اند.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/17769" target="_blank">📅 14:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17768">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">داداش مسعود الان لابد فهمیده  چرا الان آدم حسابش کرده اند!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/17768" target="_blank">📅 12:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17767">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">شریعتمداری:   مسیر دفع محاصره دریایی آمریکا؛ شلیک موشک‌های ۲۵۰۰ کیلومتری با کلاهک سنگین به سمت باب المندب است</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/17767" target="_blank">📅 23:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17766">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">شریعتمداری:
مسیر دفع محاصره دریایی آمریکا؛ شلیک موشک‌های ۲۵۰۰ کیلومتری با کلاهک سنگین به سمت باب المندب است</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/17766" target="_blank">📅 22:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17765">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DscZ0I0ZeQm44BQPjIrdOJm5DoF4m-9jRwT_JFZP4dZ6LLev90G5ggdYhjNNmi9PNO5kMGppqkps52oqF4vsjQRswjTm6KhwSIQleHUTwtnFWX9KoY0Kd1KfJkSSBhQUo0qgsE-n-VAOJ_It2C4S3Nuivu73sLQipBqTkJJeCC4zHCfO4VUSRzeOVJLFdI3C87I1Df_7d85Tkj1iJiqDqG2zrv0BHeW1F5QgH5zWTQBvnxkgBW-E1rEZkmJ8Bn213ymTH2NPmi3DWkeoQYCdmOPZYS-YG8DmM33fBDXEbPqXopluBNl8FtasGeB_TTYwnf1IbR39a5iSzHj9xfQBLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس شبکه خبر از چکیده پیام رهبری</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/17765" target="_blank">📅 22:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17764">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">چه کسی گمان می‌کرد روزی این امضای موزگونه زیر برگه ای بخورد که امضای ابوایوانکا هم روبروش باشد؟!  سبحان الله !</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/17764" target="_blank">📅 22:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17763">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ :  «اگر به نتیجه برسد، من اعتبارش را می‌گیرم. اگر به نتیجه نرسد، جی‌دی را مقصر می‌دانم.»   «بهتر است مراقب باشی، جی‌دی!»  «او هواپیمایش را برمی‌گرداند و از اینجا گم می‌شود.»</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/17763" target="_blank">📅 22:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17762">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">متن کامل پیام رهبر انقلاب اسلامی خطاب به ملت ایران درباره تفاهم‌نامه رئیس‌جمهوران ایران و امریکا
🔹
بسم‌ الله‌ الرّحمن ‌الرّحیم
ملّت پرشور و باوفای ایران
همانگونه که مطلع شُدید، تفاهم‌نامه‌ای بین رئیس‌جمهوران ایران و امریکا امضا شد. در مسیر رسیدن به این مرحله، مسئولین امر، از سر دلسوزی و با حُسن نظر، تلاش‌های زیادی را به‌عمل آوردند و البته این رئیس‌جمهور آمریکا بود که از روی استیصال، از انواع اهرم‌ها برای این امر استفاده می‌کرد.
🔹
بنده علی‌الاصول، نظر دیگری داشتم ولی از باب تعهّدی که رئیس‌جمهور محترم به‌عنوان رئیس شورای عالی امنیّت ملّی از طرف خود و سایر اعضا در پاسداشت حقوق ملّت ایران و جبهه مقاومت به بنده دادند و تصریح به قبول مسئولیت آن نمودند، اجازه‌ی آن را صادر نمودم‌. ایشان همچنین تصریح کرده‌اند که اگر طرف آمریکایی بخواهد زیاده‌خواهی کند زیر بار آن نخواهند رفت. از این لحظه، ما یعنی شما ملت سرافراز و این خادم ناچیز، منتظر تحقّق شروط گفته‌شده خواهیم بود. امّا بدیهی است مذاکرات حضوری که در آینده برقرار خواهد شد، به معنی پذیرش نظر دشمن نخواهد بود. امیدواریم که دعای خیر سرورمان عجّل‌الله‌تعالی‌فرجه‌الشّریف انواع نصرت‌ها و فتوحات، برای ملّت باشرف ایران به ارمغان آورد.
🔹
والسّلام علیکم و رحمة الله و برکاته
✍
سید مجتبی حسینی خامنه‌ای
🗓
۲۸/خرداد/۱۴۰۵</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/17762" target="_blank">📅 21:30 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
