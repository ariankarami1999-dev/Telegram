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
<img src="https://cdn4.telesco.pe/file/jW6S-yCiFaKFmxA6l3b4xDlSAI0NDTvuToXB99bn-rwSRY0DCw4KkswGTKG-TYHbPE_3nkr69dqX6pKg6D6aGRQSUwghNo9Zi7nbr2dt38UBQr-Qh8bj1Qrt4XDC_F_tBebH10Kcpwyx3NaPml8yLjpUEeLcI1MeNG7nZqoWT9vEK7jSoUZp-lhYlXCI9hXQgA-62GScjRlZlJFUgs58QMfaPsD3zdJ43VlwSgx-CyXVz8pf3FQuUjz_4ECkSIwWr46UbJe7Dxy_tTuSyCIUbDy9q-abTSWO-t3BWmdIJaKHbxCI-PrUKuFWD6vHlIJhh48VpIwqoh1gC2aKCZj9oA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 978K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 06:07:11</div>
<hr>

<div class="tg-post" id="msg-126678">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hx6pZTGan9hSD0zaLZe637kkoULY7mmxe-20ON5B1EZyzZBzj0A_sfcmDdcetDhaYmTktlgYx6REr4vG_fHkXG2GVsL88PSF1iSrUjzrR932oCOQBHVX1yM6v1Yxb8QZaSKja2aE1SM1dWHjvVnywcscsTNoS4rnOMy09ycgfNKzXgrLIRyuDT84dHp0HWx2MhLOIjyNvCaowaOVdD2u68TVpOpyaWRu8Qj_5312688EolU3roYCVWuSBnt__DgZg3HQwQeGslr2S3Zoob_sxYvQVkscJIFBNwaQ0yJO8ICMYMkMI5-VLMVu0zzI9_WtpVEaitkvjYSSTmwducxLcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
نامحدود فقط 90 تومن
😍
فقط ۵۰ نفر اول
❤️
✅
با سابقه ۵ سال فعالیت مداوم
🛡
حتی بدون قطعی تو دوران جنگ
بقیه هنوز VPN حجمی میفروشن
اونم با قیمتای نجومی
🚀
ما چی؟
💯
💥
VPN نامحدود واقعی فقط 90 تومن
🏷️
✅
این آفر فقط برای ۵۰ نفر اوله رفقا
✅
💥
بدون محدودیت حجم
⬇️
⬇️
⬇️
@NetAazaadBot
@NetAazaadBot</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/126678" target="_blank">📅 02:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126677">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7bc9515c9.mp4?token=G30Dp3OpH73E_V3UechCfylmm8MYk7Oxne-2V18e8xcuvOgVofGGHdSDKGKYOCzSmPD9X4SVTAhDsC4wFiurx0XjiVxSB7Xt2MsHdGdde4wiRdIx9dbrzTgnDe4-XSJV7wfT0fc86eTCE1n_n3j97VbKad6zzBmBI85LB6k0OxwoC-51YokpHGg695WvykW_cAOB6xa8tLyVuXs7km9LbJrJGCVRPYXNPYssZiIIBF03Wzf07Z2LvdUMK9FolF2OXzzXTMLresyOhBDNvS-Z2L-moZi4ycezonlPZiTXlWNydL1URj5q-o-B_xZ6xRjGnuWlilU8_f3gu-NWnbi-zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7bc9515c9.mp4?token=G30Dp3OpH73E_V3UechCfylmm8MYk7Oxne-2V18e8xcuvOgVofGGHdSDKGKYOCzSmPD9X4SVTAhDsC4wFiurx0XjiVxSB7Xt2MsHdGdde4wiRdIx9dbrzTgnDe4-XSJV7wfT0fc86eTCE1n_n3j97VbKad6zzBmBI85LB6k0OxwoC-51YokpHGg695WvykW_cAOB6xa8tLyVuXs7km9LbJrJGCVRPYXNPYssZiIIBF03Wzf07Z2LvdUMK9FolF2OXzzXTMLresyOhBDNvS-Z2L-moZi4ycezonlPZiTXlWNydL1URj5q-o-B_xZ6xRjGnuWlilU8_f3gu-NWnbi-zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون حملات اوکراین به روسیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/126677" target="_blank">📅 02:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126676">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
دو مخزن آب در بخش بمانی شهرستان سیریک در جنوب ایران هدف حملات هوایی آمریکا قرار گرفتند و طبق گزارش صدا و سیما، آب آشامیدنی در این بخش اکنون قطع شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/126676" target="_blank">📅 02:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126675">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eakYz2LhuV78jvPgJ7q5xKc2Y4WcjfL29HeL7ZNx0vEGbltCK2EJdSfP9vW2edx7zknSuOgEFV8BPQbW4ihui6d5VtbPgNeJ2WJFFidIo3skheBFk-cw3SrtRjeu238lLMcNUcwKXjHnVqXZO5FAJQeroaP-Bt5JiN9oRj1Bw6kKWMs3ajssRIntC8XeWdoRDl-vC_tS8DdRAMTITJVw7YaENNVGGA6koZJ9gpGpYc_dDBJ1QEmgGQbrFv4HhW9g00O1hxgLHs7rfnsdpp1FpbVSbr8za_C64IwLZUWckDKD5VHKxCaVfpt_FwxEDP3x7swZXtmzFTS7Q2RyZHiw5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون آسمان منطقه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/126675" target="_blank">📅 02:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126674">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_BJ95VtkqP_vGUR4FxVSnIKAqBq_slZbZdXK992NNldHmAp5l9a3et5RhSwyBGdweLH36oVf__dODMQuJk7q1bCtE3cKG-Sm17Op4r3zDW6lSWJcbZ5u0OQrtnIF3y3yLdPTSL7q3IdDpt3KanrrsCICsXTMzmzmwI3MULltGS4FOIFvoUJTAIP3wSPItQyWECWrHTUpmOmCRiqM35rqLUOeYR0hKGJw5gyjKWthnfVtOJTLy0E_RWM2IuITALmfOt3PoH48zgoInw1Qv7Gq3p72SWgkHO0cgBSkxzBhOAy2tKckRXpKi1jg2Ynk33f-Jyz6uPwUEzfKdgT1d0jwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی : با اینکه توی میدان جنگ شکست خورد، آمریکا باز هم تصمیم گرفت اراده‌مون رو امتحان کنه
- نیروهای قدرتمند مسلح ما هم هر حمله یا تهدیدی رو بی‌جواب نمی‌ذارن
- اگه می‌خواید سالم بمونید، از منطقه‌مون برید
- تاریخ خلیج فارس پره از سرنوشت‌های تلخِ خارجی‌هایی که چشم طمع داشتن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/126674" target="_blank">📅 02:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126673">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
اسرائیل هیوم: ارزیابی اسرائیل این است که ایران به کشورهای خلیج فارس حمله خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/126673" target="_blank">📅 02:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126672">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
کاخ سفید: ما معتقدیم توافق با ایران بسیار نزدیک است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/alonews/126672" target="_blank">📅 02:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126671">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
پولیتیکو به نقل از یک مقام ارشد در کاخ سفید: هیچ تغییری در شرایط بوجود نیامده و آتش بس کماکان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/126671" target="_blank">📅 01:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126670">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
فوری/ گزارشات از حملات توپخانه ای عربستان به یمن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/126670" target="_blank">📅 01:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126669">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
گویا اسرائیل به سوریه هم حمله کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/126669" target="_blank">📅 01:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126668">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
هم اکنون خاورمیانه:
🔴
حملات آمریکا به ایران
🔴
حملات اسرائیل به لبنان
🔴
حملات پاکستان به افغانستان
🔴
حملات ترکیه به عراق
🔴
حملات ایران به بحرین و کویت و امارات
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/126668" target="_blank">📅 01:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126667">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
هم اکنون حملات ترکیه به شمال عراق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/126667" target="_blank">📅 01:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126666">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69604724c6.mp4?token=SyJTwHOSOGzWUCP0dchGfH-zvSBnwyUlNhEN2QBYqDFMyvEoV0ycpubO4kpIho20rA1QT4LBHAh_nmAJAdslQmJuAb0xkxmrq17u3Elc5zX7hsK9_NVM6rhfLB-422vst819QkwNXH2lQAc4FRYPdWS85q60hVWHzcfqX6u-YvZuceG9IUKOeBPcc5e1KIGfYoOcogc56-Il80HYh7FPQVDzRa1yY6sPNysbChO7eB-aHW8XQj78kOwfmYoodZywOUXvRIVqS3BqJrtczbG5dNZqe7k9dzAu1qGXDgaEaUk-TkxQ48_MN3M8htk8hTRVIadvV8DSNSb0_-dITNC4FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69604724c6.mp4?token=SyJTwHOSOGzWUCP0dchGfH-zvSBnwyUlNhEN2QBYqDFMyvEoV0ycpubO4kpIho20rA1QT4LBHAh_nmAJAdslQmJuAb0xkxmrq17u3Elc5zX7hsK9_NVM6rhfLB-422vst819QkwNXH2lQAc4FRYPdWS85q60hVWHzcfqX6u-YvZuceG9IUKOeBPcc5e1KIGfYoOcogc56-Il80HYh7FPQVDzRa1yY6sPNysbChO7eB-aHW8XQj78kOwfmYoodZywOUXvRIVqS3BqJrtczbG5dNZqe7k9dzAu1qGXDgaEaUk-TkxQ48_MN3M8htk8hTRVIadvV8DSNSb0_-dITNC4FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیده شدن پهباد شاهد سپاه در آسمان عراق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/126666" target="_blank">📅 01:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126665">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
یک مقام آمریکایی به سی‌ان‌ان:
حملات جدید به منزله یک شلیک هشدارآمیز به ایران است و ایالات متحده معتقد است این حملات مانع مذاکرات برای پایان دادن به جنگ نخواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/126665" target="_blank">📅 01:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126664">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
رسایی: اینترنت قطع کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/126664" target="_blank">📅 01:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126663">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
فوووووووووری/گزارش انفجار در بحرین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/126663" target="_blank">📅 01:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126662">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
فوری/به بیروت هم حمله شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/126662" target="_blank">📅 01:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126661">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✅
سید مجید موسوی : ‏و ما النصر الا من عند الله العزیز الحکیم
✅
@AkhbareFouri</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/126661" target="_blank">📅 01:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126660">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
فاکس نیوز: از جمله اهداف حملات آمریکایی‌ها در ایران، سامانه های پدافند هوایی و تاسیسات راداری است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/126660" target="_blank">📅 01:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126659">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
گزارش حمله هوایی پاکستان به چند پاسگاه مرزی افغانستان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/126659" target="_blank">📅 01:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126658">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🤩
ارزون ترین قیمت ، با کیفیت ترین سرویس
🌐
❤️
فقط گیگی 2t ، نامحدود 290t
💫
🔔
آره درست شنیدی گیگی
🛍
2
🛍
تومن
👀
5 سال اعتبار ، 5 سال همراهی شما دلیل این خدمات باکیفیت ماست برای جبران این لطف و محبت
☑️
❤️
👇
تست و تهیه اشتراک
👇
@tvpnshop_bot @tvpnshop_bot</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/126658" target="_blank">📅 01:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126657">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
فوری/قطر و کویت حریم هوایی خودشون رو بستن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/126657" target="_blank">📅 01:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126656">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
فوری/به بیروت هم حمله شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/126656" target="_blank">📅 01:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126655">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
فوری/آغاز حملات ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/126655" target="_blank">📅 01:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126654">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ecDS7ZWBiS8EFTzoB9idAjbqhCRgg5Z0N43VylpYPTP8eCcxxLJsaoTfXLt9mzfJIt9nhiBmbvud_AGrwV-QvmhMlzSLch4U-rDJPVU2XKmj8w8WFy00z8GNMoORoOo6R0FNQgtXh30fNcWVFgVKkUkZMCcHOw2rKw94x_V3IIcBquI9YrQnvhELhbQa8hUVupnOozdtRSYrV7RPnqQ4D4PUhYVNnDiObs9XqcpbbkUIWKJvpA6AakcPKaYYQdjmuxKHXNfJwSKFduH7eXZ1vZm-ehaW7zT2OtFNQCkUp3qk-krI-d5hYd45L1NJNpI5QLpvnXZca6_iLtzaY9AKXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مشاور فیلد مارشال محسن رضایی:‏
پاسخ ایران به حملات آمریکا اجتناب‌ناپذیر و احتمالا قریب‌الوقوع است.
🔴
علاوه بر پایگاه‌های آمریکایی در کشورهای حاشیه خلیج فارس، جغرافیای محاصره نیز می‌تواند جزو اهداف باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/126654" target="_blank">📅 01:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126653">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZ3JuJwazGW0lj9mYh03Cr7c9ZT1lL4Qcz1SJKOfobUfHtbp5KVkGnJvJeI4x2wT64Q1TI3o1Ew8OlGw_JEMiA5CATNYuGG0fUyY8e6Jfjlnz0WmFi9FjJHM-gvBBCuJXTsIPeExejIz2asy_ddTop58OB-IwGcZlZlVLe5IopKxSIvr7zFeKaXBQjxQn2JIRnLC6x9jmvCtVP0swRUEzR2AZSPsPgTLiICDgpWElwLJCeZNy8RrpMoM4gjzErxPFWeW_GlYGap2Fy3YIkmOtej3vhfnEzXYSbyN2hYk8M8vKLH861e-bOmqVb8T5feN9bbpvauFozrQhsIMrBHcBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
ارزون ترین قیمت ، با کیفیت ترین سرویس
🌐
❤️
فقط گیگی 2t ، نامحدود 290t
💫
🔔
آره درست شنیدی گیگی
🛍
2
🛍
تومن
👀
5 سال اعتبار ، 5 سال همراهی شما
دلیل این خدمات باکیفیت ماست
برای جبران این لطف و محبت
☑️
❤️
👇
تست و تهیه اشتراک
👇
@tvpnshop_bot
@tvpnshop_bot</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/126653" target="_blank">📅 01:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126652">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
فهرست اولیه اهداف آمریکا:
🔴
پایگاه دریایی سیریک
🔴
پایگاه دریایی جاسک
🔴
موقعیت پدافند هوایی بندرعباس
🔴
باتری موشکی ساحلی میناب
🔴
باتری موشکی ساحلی قشم
🔴
بندر قشم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/126652" target="_blank">📅 01:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126651">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
6 انفجار در قشم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/alonews/126651" target="_blank">📅 01:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126650">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
هم اکنون ترامپ به ABC درباره حملات ایران: فکر می‌کنم پاسخ دادن بسیار مهم است، آن‌ها یک هلیکوپتر را سرنگون کردند و ما همین الان در حال پاسخ دادن هستیم
،
🔴
این پاسخ به کاری است که آن‌ها دیشب با هلیکوپتر ما انجام دادند،من معتقدم پاسخ باید بسیار قوی و قدرتمند باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/126650" target="_blank">📅 01:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126649">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
صداوسیما: حملات موشکی بزودی انجام میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/126649" target="_blank">📅 01:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126648">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
علی قلهکی خبرنگار امنیتی :
بنظر می‌رسد آمریکا در حال آماده‌سازی افکارِ عمومی برایِ «اقدامِ خاصِ نظامی» است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/126648" target="_blank">📅 00:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126647">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
انفجار در میناب
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/126647" target="_blank">📅 00:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126646">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
تاکنون 7 انفجار در سیریک
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/126646" target="_blank">📅 00:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126645">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">📱
لطفا توییتر الونیوز رو دنبال کنین
🔴
پست های انگلیسی در رابطه با جنایت های حکومت به انگلیسی نوشته شده و افراد مهم منشن و هشتگ های مهم قرار داده شده.
🔴
ریپست کنین. مهمترین کمک این روزها جلوگیری از پروپاگاندا حکومت علیه این قتل عام مردم هستش. خونشون نباید پایمال…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/126645" target="_blank">📅 00:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126644">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">💢
فووووووری/هم اکنون تحرکات موشکی شدید سپاه ماسداران
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/126644" target="_blank">📅 00:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126643">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
حملات ایالات متحده با موشک‌های کروز تاماهاوک انجام شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/126643" target="_blank">📅 00:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126642">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
رسایی: اینترنت رو قطع کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/126642" target="_blank">📅 00:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126641">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwlho6-BXXLoKLEP9AsnciJvR4VznoS9SGKI14UWkuJ1JNUN_9HDOwWUGNmAk3Byv9Wpk2kwtd-xiTPNchrzMsZ4-hHccQI3gW2QT6jbybzk3qTW_Br8Z3Q2L0DtmPkDZLHNT2U18D5vjSIKEbpXWNbattnEq7HnNebv9noIsyXOYvDAgds1L45g5qWNSLcQ36Sj5-Z1Q3c-cmeBoYrEbjo4v8S93KoN8SZzdjsoizJWD3u2Q7mexDeyaYKVEhtjpDJijuXxCyu08SBRTbbYo-yyfZxb0RZ7U0k-711Dmh53gYFrI2VcHzVTBzlkjgGiKCrcE2lKh9G0McPdOkStmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/126641" target="_blank">📅 00:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126640">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/126640" target="_blank">📅 00:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126639">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
صدای ۴انفجار در محدوده بندرعباس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/126639" target="_blank">📅 00:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126638">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
فوری/ایالات متحده رسما حمله کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/126638" target="_blank">📅 00:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126637">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
فوری/انفجار در جزیره سیریک
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/126637" target="_blank">📅 00:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126636">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
فوری/گزارش‌ها از هدف قرار گرفتن پایگاه شهید راهبر در بندرعباس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/126636" target="_blank">📅 00:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126635">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
فوری/گزارش‌ها از حمله به بندرعباس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/126635" target="_blank">📅 00:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126634">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fv4NUoUEh3TuGnGciZb24CE59qyrDCDpDDu5JUPMZfpLvFvJ_kd7t8SfCUpMgLgnxVml2rwjGwAUBE8tvKoi55k-qlwMUY4UA0jnq2i8RK-dFmKp1l4QNwihtm6aid87oWvLWPnL_z2hUzcgoa0mh2FbxZjbXEqA8i6m4CSUpF6XDiGDL_S6wd9ut5ocBSKhqgqshFh8O2MCDZmGNRue7kMsqPCRpcuEuQW1yeEzJOa5S7KhKvCtAyPFJ0dSEe5ykL90pIMcntvhQJqcViCJUb_-rVZIwG2B71GJx2IgbIT3IiduH2pIIbXBr3YJaUX9b58F9dqYuEssZKaGCF-5Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حقارت تمام عیار قبل از جام جهانی
‼️
تیم جمهوری اسلامی فردا در دیداری دوستانه به مصاف تیم زیر 21 ساله‌های شهر تیخوانا مکزیک خواهد رفت
هیچ تیم ملی‌ای حاضر به بازی با تیم جمهوری اسلامی نشده
@AloSport</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/126634" target="_blank">📅 00:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126633">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NoxcCLKiIQTawI7U_KuwxM1EL1E6_ZbWNVNr9jgIo0MYynCJ7RJIP77AkBN97242c24RrZD6jYL8G6MDwzoT6xDmT0l1kaWWtNqmcjW3gqwL3F0yNbkWvyvYIot1xFy5NZKu-oGqmuGgXYANGmVSHPxEIGUZdvNwPk2OoxA3Jv6XtZiWdxq5enxEIOnwMx1x4_lA--0fxgDyGXlm1UWnQFDSW0JDkWFDCDuIlcdc2M6lzaTlYdTRmQk7ELtT_lLoEaHdCAmEGEG_Nja34RsvqBzzgNtj45de_5H2x4yDVtEKrGpErgG7njadjBUxxB6lArwfEgvku5GMoPrry92I7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حزب الله به شمال اسرائیل حمله کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/126633" target="_blank">📅 00:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126632">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYD4oRQkULSgs5rJjB8Bc8XgY4scrUubOxrLbWKMVum0g2ltG2SBRug-bMlj5Y4cEohnirO7o-n1vkHnIYw1SlrzMoSr9Y0jK-vxrwfJTv4Pl_s5U58f6RU79pvuI_14hS_XD7S4ohFF2k-nCwiv-3HiXvMQbkD8fSBSljiOE0kTxNU2H-vb1zPn3wdogjkUtQbX-eBEdpIrL_JCSe6O94D8snUEQVkZ9lS9FExQQhZGTdYjKrkXRnBl4DR4ECu32cAPjL6qwSskryH6XZbr-NUvCa6p5fxXwJAUHD3xqE82QC-WrX7yQkbcQ6hjshQiYr80KYCOryJUn_kL7KthRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زیرنویس شبکه خبر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/126632" target="_blank">📅 00:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126631">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">💢
فوووووووووری/پرواز شدید جنگنده‌های آمریکایی در مرز ایران
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/126631" target="_blank">📅 00:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126630">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
شبکه خبر به نقل از منبع آگاه نظامی: هیچ عملیات نظامی هجومی هوایی در تنگه هرمز در ۲۴ ساعت گذشته انجام نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/126630" target="_blank">📅 00:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126629">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
مسکو در واکنش به رای شورای امنیت سازمان ملل به بررسی بازگشت تحریم‌ها علیه ایران : ما به شورای امنیت اجازه نخواهیم داد که تحت پوشش کمیته تحریم‌ها، تصمیماتی اتخاذ کند که محدودیت‌هایی را بر کشور‌های عضو اعمال کند
🔴
چین: تلاش برای بازگرداندن تحریم‌ها علیه ایران فاقد مبنای شورای امنیت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/126629" target="_blank">📅 00:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126628">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNXI8Bw4rw6Nv5VmMj0yW_y3ArQBlX8ZebSMND0xTgYj8DUQ2K13wao51XEzXWyu7Nabw6bh5znNeLfOsZN6wg0VmPDbtA8akJPWzmJ0jGKxHqwNRrgzxCoSgfTrG_jTxfC5Ojgs0oEF07O_GtcVxbvxR5TE8TB1gbYyJ-wOcAQTdsR3ugq5ucU6WZxdjcrmxPQn93A5BXUoh-EikSsxNTFG00WrHHtIPO6rlKuGtLQCvF-VcWGDXew_9vCitih1FVi8_FayMDEequOvcAsjtUZ5YY8CASHXu4TJTgKLqOKuWgDBlDFO-LEW7Ql39odnDMtMzdJknBtcvS-jdp3nkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس: به هر اقدام آمریکا پاسخ سریع و قاطع خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/126628" target="_blank">📅 23:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126627">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
وزیر خارجه انگلیس: خواستار مذاکرات موفق ایران و آمریکا هستیم
🔴
می‌خواهیم شاهد پایان سریع و موفقیت‌آمیز مذاکرات بین ایران و آمریکا باشیم.
🔴
تجارت جهانی از طریق تنگه هرمز باید به سرعت از سر گرفته شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/126627" target="_blank">📅 23:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126625">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
جی‌دی ونس: به توافق با ایران نزدیک هستیم؛ شاید هفته آینده، شاید چند ماه دیگر...!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/126625" target="_blank">📅 23:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126624">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
ترامپ به واشنگتن پست گفت که محاصره باعث شده ایران «بسیار فقیر» شود و گفت آن را تا زمانی که لازم باشد در جای خود نگه خواهد داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/126624" target="_blank">📅 23:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126623">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
دونالد ترامپ در گفتگو با وال‌استریت ژورنال، درباره حادثه سقوط بالگرد آپاچی گفت که "مسئله خیلی مهمی نیست" و افزود که خلبان حالش خوب است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/126623" target="_blank">📅 23:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126622">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
فوری /شلیک موشک از خاک یمن به سمت اسرائیل
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/126622" target="_blank">📅 23:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126621">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
فوری/ خبرنگار: شما گفتید آمریکا باید به سرنگونی آپاچی پاسخ دهد، آیا هنوز هم این نظر را دارید؟
🔴
ترامپ: من مجبور نیستم کاری انجام دهم، ما همه کارت‌ها را در دست داریم. مجبور نیستم این کار را بکنم اما ببینید، احتمالاً این کار را خواهیم کرد، باشه؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/126621" target="_blank">📅 23:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126620">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
ترامپ درباره ایران به ABC: یک نفر باید همه آن زیرساخت‌ها را بسازد، پل‌های جدید، فلان چیز جدید، نیروگاه‌های جدید... آنها از یک تریلیون دلار صحبت می‌کنند، احتمالاً بیشتر...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/126620" target="_blank">📅 23:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126619">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ترامپ: به زودی پایان جنگ و پیروزی آمریکا بر ایران را اعلام میکنم امسال جام جهانی خوبی خواهیم داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/126619" target="_blank">📅 23:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126618">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
فوری /شلیک موشک از خاک یمن به سمت اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/126618" target="_blank">📅 23:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126617">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
هشدار فرانسه در شورای حکام: جمهوری اسلامی ایران مقدار بسیار زیادی انباشت اورانیوم غنی شده در اختیار دارد و مشخص نیست چیکارش کرده و کجاست، همکاری فوری جمهوری اسلامی با آژانس بین‌المللی انرژی اتمی ضروری است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/126617" target="_blank">📅 23:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126616">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
روزنامه نیویورک پست گزارش داد که هزینه بالگردهای مدل AH-64 «آپاچی» بیش از ۳۵ میلیون دلار برای هر فروند است و ادعا کرد که این بالگردها در سراسر دریای عمان و تنگه برای اعمال محاصره به عملیات مشغول هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/126616" target="_blank">📅 23:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126615">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
گزارش ها از شنیده شدن صدای 3 انفجار در نجف عراق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/126615" target="_blank">📅 23:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126614">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
معاون وزیر خارجه ایران به الجزیره:
ایران پشت حمله به بالگرد آمریکایی آپاچی در بالای تنگه هرمز نیست.
🔴
این احتمال وجود دارد که چنین حوادثی به دلیل فضای پرتنش در تنگه هرمز به صورت غیرعمد رخ دهند.
🔴
هیچ هدفگیری عمدی از سوی ایران علیه بالگرد آمریکایی در بالای تنگه هرمز صورت نگرفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/126614" target="_blank">📅 23:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126613">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
ترامپ به ABC : حمله اخیر اسرائیل به ایران لازم نبود، ولی انگیزه‌های اسرائیل رو می‌فهمم
🔴
به نتانیاهو گفتم کاری نکنه که به مذاکرات با ایران ضربه بزنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/126613" target="_blank">📅 23:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126612">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibhzd0XYVyAJTIiasFr6F61PJI0h058IGAoTyWL8KfrB6zs4IUxsqnes1PWPdIoXoEAlPWn1P6fo_V7cWx1spDUKd7D1zZyyorObcYzC5OhrttFSQNN4MfdphNa7aDFcXP1MwlDZGAvIFla1oUEzGjle5m8YB0zkq6rFeeHeFGIn20hjFzzJAFqh8IUiDyZ9X6z4pmRH0mNqlOubsmoX6pYtm5-HOMBrKfPFoPO1T3UeyjK3-DuX7GBhpNgI2DcS4C7-BO1nA-XKtJx0fO6p9Yk5Y_gs6UjlUVCfCXFJ_c0THWf8fi152009GZpt-lGxDybIgRLVzuHN_ioQU6NIsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: تردد کشتی‌ها در تنگه هرمز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/126612" target="_blank">📅 23:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126611">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBvPrC2a6Ip0FDFZNyGmIMvnShQIin6N7FMMytxsge-K60rIxbVJSkwHLP_b-n0VecO6ibeoDGw3fCPH60kEZnSNENf28W3nqAJRJtwPhikG8FUXMTwHXL-uRqPZxWjm72FiDyfG7BAeEOfsbGtHXTIWDSqLhSZGlLJgyIimRii0t3DJHqZAbbthgDmvLhEg7HynTeZdiHG8QqGDZnZlHPdWRs7mnrjAOWG8UTSmITFPeljvYz8kOgbeIhnPfZUEHBmHIoUGNJ6cvoMvnxkmnkbe1aT4d1vTRN1rSiu6dMLjX1hyYRRBeEjCOKMjvemPbjh3z6ajmHzrNGJhBRNbrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
داده‌های کشتیرانی: صادرات سوخت جت عربستان سعودی به اروپا از سطح پیش از بسته شدن تنگه هرمز فراتر رفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/126611" target="_blank">📅 23:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126610">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jhe3lKYlRAKXIcRIVM7MqwxDC9VwYNGTFI9F7-phpHwC3YJANJWpBwmLhBA2xqD37NcMnBJv1J733mMhu7P9_JTh-EjoS4I-VsIaCMHOqH62pCbkAB5ViRf3iEt-s6yChidyjfQIDfaAjZF4WcTZGJDIMTjYVAWBKyL7Q45jSkE6eaveAeWRTkAkIncta2gbt9D2BqLrw4djftG54f_RY5Wpkg863IoNROywVc6m7oq3QHosLOtNt29K51hdVw3sqlK4gAT9bbFpL6tN0PHSUanTP8i737MCjiTlhmWDMq1Z5xDZFtXJB49KTinJDH25SHUNUvNwZH5BbNt-ifFIow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروی هوایی آمریکا هم‌اکنون هفت فروند هواپیمای سوخت‌رسان را در منطقه خاورمیانه به پرواز درآورده است.
🔴
از این تعداد، شش فروند در مجاورت خلیج فارس در حال انجام عملیات پروازی هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/126610" target="_blank">📅 23:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126609">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
طبق گزارش ها تهران در حال حاضر شاهد اختلالات گسترده در GPS و خطای سیگنال‌های ناوبری (Spoofing) است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/126609" target="_blank">📅 23:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126608">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQcrp3-9nZEP7maaaGPEu6hJRhvF1Ohu6dOceSqHG5HPKe0qv72g2lyirvsZRGCCl1t36yrb-Xf6yiz1GCv0M9erVm84srmQzDQCtMJEyGUEF-mEihGRAsF45aAmiDEHC9ki7TwQNx17evC1r-FIwBxeIOPC_tWKc-hTint7Xb_WUxiRyMCDlZetHT4HocptHZKN3SAGNMXkQW_8kLXsob9Hd8USdellNaUP4TWHEA3YEQ6LhEqCM4RvfsuB-6kVXzgxTAUn5BOjjgSRBDz7O-RPC4lUnVDV-eqRCsJIIpqlUr-2eMBLPZ9Qfc4H0NnlqXjXBb0nv4c-0roYtBz05A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/ لیست ترور منتشر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/126608" target="_blank">📅 23:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126607">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
فوری / شورای امنیت رأی‌گیری درباره قطعنامه ۱۷۳۷ را پیش برد و با ۱۱ رأی موافق، بررسی بازگشت تحریم‌ها علیه جمهوری اسلامی ایران را تصویب کرد
🔴
بریتانیا از فعال شدن تمام تحریم علیه  ایران استقبال کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/126607" target="_blank">📅 23:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126606">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: احمد وحیدی فرمانده کل سپاه پاسداران گفته تا جمهوری اسلامی پول نقد دریافت نکنه هیچگونه توافقی امضا نخواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/126606" target="_blank">📅 23:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126605">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
فارس به نقل از منبعی مدعی شد: پیشنهاد جدیدی از سوی ایران برای آمریکا ارسال نشده است.
🔴
اسکای‌نیوز امروز در خبری اعلام کرد که تهران پیش‌نویس جدیدی برای طرح صلح به واشنگتن ارسال کرده و گزارش‌های اولیه نشان می‌دهد که طرف آمریکایی آن را «قابل قبول» می‌داند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/126605" target="_blank">📅 22:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126604">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c298926e7d.mp4?token=YW8zI8JYZ3VgVwMkMD3pmBlCEnPicUarHuMdkPhVPBcSZ-jn1EbHxfwAK-VIOowFuV6zgswykCNQx6Qz6WYB8MGPLh0PpdNIsAUUyinMlNCBfblGTMm34YfmQjdQlrZLW5-5wUxVPX4PH4dL_9edlzsEvcc1-AIVICUTYsqBr_PYSqLrCsg_q-BHvzA9JQTTDCt9HdF94tKcmZBH_6EeZ_FNT2j-NsrHacpirG3twWj4yN2lY_3sQdwuVWKSUgGsdTHGOL2aUPRmsu0T0AMcKKmBly9omXrJHK56habQogtTPYD10kVaZLoB05VRMcNiX9Yj7YuY2VjxgkRzTyInsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c298926e7d.mp4?token=YW8zI8JYZ3VgVwMkMD3pmBlCEnPicUarHuMdkPhVPBcSZ-jn1EbHxfwAK-VIOowFuV6zgswykCNQx6Qz6WYB8MGPLh0PpdNIsAUUyinMlNCBfblGTMm34YfmQjdQlrZLW5-5wUxVPX4PH4dL_9edlzsEvcc1-AIVICUTYsqBr_PYSqLrCsg_q-BHvzA9JQTTDCt9HdF94tKcmZBH_6EeZ_FNT2j-NsrHacpirG3twWj4yN2lY_3sQdwuVWKSUgGsdTHGOL2aUPRmsu0T0AMcKKmBly9omXrJHK56habQogtTPYD10kVaZLoB05VRMcNiX9Yj7YuY2VjxgkRzTyInsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار فاکس‌نیوز در کاخ سفید:
«رئیس جمهور ترامپ احتمالاً در شرف دستور دادن به یک انفجار بزرگ در ایران است... هیچ سرباز آمریکایی در اینجا کشته نشد، اما به نظر می‌رسد که ایران واقعاً، واقعاً سخت تلاش می‌کرد تا سربازان آمریکایی را بکشد، زیرا آنها یک هلیکوپتر آپاچی را سرنگون کردند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/126604" target="_blank">📅 22:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126603">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
حداقل 4 پهپاد کامیکازه شاهد-136 سپاه به یکی از مقرهای حزب دمکرات کردستان حمله کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/126603" target="_blank">📅 22:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126602">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
نبویان، نماینده مجلس: غنی‌سازی ۹۳ درصد می‌تواند به صورت صلح‌آمیز باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/126602" target="_blank">📅 22:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126601">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
فوری/ ایران در حال انجام حملاتی به مقر گروه‌های مخالف کرد ایرانی در اربیل عراق است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/126601" target="_blank">📅 22:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126600">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70603bf6a8.mp4?token=FLRNy7o4dClwwejrc6rnRxbAaA97-QYGjhc98ueZelHNzIGwdqo3JD7zbybD3G82Sys7HcnmQQN-W-IlZKlbm55rIGOH17TJq-_pznUNp8uNWDrI9eyarnF2xPgSLvlyzi_gj5WcJyfMlRzwDEM_BluqeX9K954FXOe792DZZc-gmBaGCm01bWfJgkwF2oEYpwfB7V_RFxZt36Ol8MJQVmC1JViueXECKBeB7fjykAgLHIOekdPsy9vZAGVZ-8aTmAeo4Hwp9QHF4iJJ6qZgo2g2pG1x8qpQJ83ZcNvLNt3saX_6ulhTws2_9Gjzeww4CI-iTkSgPaOPSGb1ecjMng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70603bf6a8.mp4?token=FLRNy7o4dClwwejrc6rnRxbAaA97-QYGjhc98ueZelHNzIGwdqo3JD7zbybD3G82Sys7HcnmQQN-W-IlZKlbm55rIGOH17TJq-_pznUNp8uNWDrI9eyarnF2xPgSLvlyzi_gj5WcJyfMlRzwDEM_BluqeX9K954FXOe792DZZc-gmBaGCm01bWfJgkwF2oEYpwfB7V_RFxZt36Ol8MJQVmC1JViueXECKBeB7fjykAgLHIOekdPsy9vZAGVZ-8aTmAeo4Hwp9QHF4iJJ6qZgo2g2pG1x8qpQJ83ZcNvLNt3saX_6ulhTws2_9Gjzeww4CI-iTkSgPaOPSGb1ecjMng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فعالیت جنگنده ها در آسمان کردستان عراق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/126600" target="_blank">📅 22:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126599">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
صابرین نیوز : باند اپستین در حال تدارک حمله گسترده به بهانه واهی است
این چندمین‌بار است که آمریکا در وسط مذاکره به ایران حمله می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/126599" target="_blank">📅 22:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126598">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
گزارش ها از پرواز جنگنده های آمریکایی / اسرائیلی برفراز سوریه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/126598" target="_blank">📅 22:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126597">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">💢
فوووووووری/حمله شروع شد؟  هم اکنون هشدار در پایگاه‌های آمریکایی
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/126597" target="_blank">📅 22:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126596">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDZo-BrIH7gsBZU-Ruo_PM9AgQmg7O4fmzn2IbOIkcSEEWO9vObZJFY8zhmWvADFvteKtaILls0komFjyMf-IZUxfq1jwmnwrVdduM6VFEOJI-Iu8eDMD5J1uSMpjIfHQC-ZEtBhlUP9reBdH6t7PPVo0kE2KyoqjmwY-NPbfvfv8iXl5qIGfwlQyQqS2-FdQqTMnCV_7sFlnjaNAzfInbutOfz7ELjr9ISlwIZ3GGGZW8llenPC8R-scD-O15-JuCemIkEqg4K6Ny22YvvzjLQeKzJFI8pG6g-o5daXnW8u00UHiHZpsnYM8-HWYpYNn__JJZl9lWvMH6fWPPVkNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فعالیت حداقل 9 سوخت رسان ایالات متحده در خاورمیانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/126596" target="_blank">📅 22:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126595">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
فوری/فعالیت پرتعداد جنگنده های آمریکایی در آسمان عراق گزارش میشود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/126595" target="_blank">📅 22:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126594">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
نیویورک تایمز : مشخص نیست که آیا مذاکرات با ایران پس از تعهد ترامپ به پاسخ به سرنگونی بالگرد، از سر گرفته خواهد شد یا نه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/126594" target="_blank">📅 22:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126593">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
ترامپ: من همین الان توسط ارتش بزرگمان مطلع شدم که دیشب ایرانی‌ها یکی از هلیکوپترهای پیشرفته آپاچی ما را هنگام گشت‌زنی بر فراز تنگه هرمز سرنگون کردند.
🔴
دو خلبان درگیر بودند که هر دو سالم و بدون آسیب هستند.
🔴
با این حال، ایالات متحده باید به این حمله پاسخ…</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/126593" target="_blank">📅 22:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126592">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
یک مقام ایرانی به الجزیره: بالگرد (هلیکوپتر) آپاچیِ آمریکایی بر فراز آب‌های بین‌المللی پرواز نمی‌کرد.
🔴
ایران به هرگونه حملهٔ آمریکا که متوجه این کشور شود، با قدرت و به‌صورت فوری پاسخ خواهد داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/126592" target="_blank">📅 22:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126591">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUsxxDe-Rjcg_htka_wyW1G4LpVu23ky7CbD7RIidoQh1z-wilBUhVci9_IeC9hSjvZuPJfK98j8eXsb9UDNuCI4mLs67JwNbLjQM1Pcxptq0gCQ5hwX6TfI2txkmkmLEl-x4LEl78TahLPQFVyfXQnyA_Mbb4-fvt6Q3jK8VBsckPUoS8bMWJOsQT2p_BxWK7wvy6-ap1YgZszQwaXnLxDw9qTT5Ywvzt7VRZdZES4dhtPI-LmbhB926VttQ1K1t5wIMEPgT2BSB6FeCbwkb_GmycT0JtO1p4uBpOTF_mBGqLZU65K0qsUF9hK2kRaWAwLzX_4AxBT0hiTTs3MfQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۹۱.۳۵ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/126591" target="_blank">📅 22:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126590">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
ترامپ : قضیه خیلی ساده‌ست هرکی قدرت بیشتری داشته باشه، برنده‌ست و ما هم همه قدرت رو داریم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/126590" target="_blank">📅 22:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126589">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
عباس عراقچی، وزیر امور خارجه:
نیروهای خارجی در نزدیکی قلمرو ما به دلیل اشتباهات انسانی خود، حوادث ساده یا احتمال گرفتار شدن در آتش متقابل، همواره در معرض خطر هستند.
🔴
برای کاهش خطر، بهترین راه حل این است که آنها منطقه را ترک کنند.
🔴
ما زبان دیپلماسی را ترجیح می‌دهیم اما به زبان‌های دیگر نیز صحبت می‌کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/126589" target="_blank">📅 22:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126588">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
فوری / ترامپ به ABC : اگه یه عده بخوان احمقانه رفتار کنن
🔴
ممکنه کار به جایی بکشه که مجبور بشیم کل زیرساخت‌های یه کشور رو نابود کنیم!
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/126588" target="_blank">📅 22:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126587">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
فوری / ترامپ به ABC : اگه یه عده بخوان احمقانه رفتار کنن
🔴
ممکنه کار به جایی بکشه که مجبور بشیم کل زیرساخت‌های یه کشور رو نابود کنیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/126587" target="_blank">📅 21:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126586">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m03FuYBgjobL5CM7z51Nh--lL3wu6JPDQ01gRQs3Z6YJVML0u7cw-f3eJ5Sj-HNy5-p_3VBsSo_3kWkL68UUxmOiu7JRG0aEkgK6Dd0pxtxwv6Y05JwIxLEt3WnIdMnkyN1fSLqW6fa8xx6CBSqZdVS649H7ZgdaIoXtRyiB-qTHghk1Lx0tDgNpL5uBq5PJiLJNIAvKisH8hSHNEwYMRop1bONHpYEF9dEKhROi2bGh92WQEcIGjxSD8E1PlBiTc12kIHRQe9MxciLPJQbubIzGr4m7rxPCX8WTXWiT_ICbZ-gSr84ScwV7ji8vbW1T9C0C7bHycCedsnw6DIqt2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون آسمان منطقه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/126586" target="_blank">📅 21:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126585">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
کانال آی ۲۴ نیوز اسرائیل: هشدار نتانیاهو: ممکن است مجبور شویم بدون پشتیبانی آمریکا با ایران مقابله کنیم
🔴
پس از تماس تلفنی ترامپ برای توقف حملات اسرائیل در پاسخ به رگبار موشکی ایران، نتانیاهو به وزیران کابینه خود چنین هشداری داد:
🔴
«ممکن است به وضعیتی برسیم که مجبور شویم به تنهایی و بدون پشتیبانی آمریکا با ایرانی‌ها مقابله کنیم، با تمام هزینه‌هایی که این موضوع به همراه دارد، کمبود مهمات و انزوای بین‌المللی. نمی‌خواهیم به آن نقطه برسیم، اما می‌دانیم که ممکن است برسیم.»
🔴
رئیس ستاد کل ارتش اسرائیل، ایال زامیر، همچنین درباره توافق هسته‌ای در حال شکل‌گیری هشدار داد:
🔴
«از منظر ما در حال حاضر، تقریباً هر توافقی، یک توافق بد است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/126585" target="_blank">📅 21:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126584">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
فوری / سوخت‌رسان‌های نیروی هوایی آمریکا از مکان‌های مختلف برخاسته و در حال حرکت به سمت خلیج فارس هستند!!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/126584" target="_blank">📅 21:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126583">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
فوری / مقام آمریکایی به الحدث: گمانه‌ها حاکی از آن است که هدف قرار گرفتن بالگرد آمریکایی از سوی ایران عمدی بوده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/126583" target="_blank">📅 21:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126582">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
سفارت هلند در تهران فعالیت خود را از سر گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/126582" target="_blank">📅 21:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126581">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
فوری / خبرنگار شبکه فاکس نیوز در واکنش به پست ترامپ درباره سرنگونی هلیکوپتر آمریکایی: به نظر می‌رسد این به معنای آن است که رئیس‌جمهور دستور یک اقدام بزرگ در ایران را می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/126581" target="_blank">📅 21:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126580">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/048590050f.mp4?token=mz3mK9xTjIPusn3irJ7_P3YsQ1Kfu-2ePWxfTqnB3wJrDhtZQRIcWKhu4w0xMGs8IeYTEL1UTzDf_Ww-t8dmlB540sEvZyo-YLPXv8y-BCrbjxKq7wP_qhoI6Bl0I4io2JVsmFwsASGecCNbReuSxnNBsi6_Lk2x8UZSfbhRciwjRGPEjHEpPcp7lBnjiSxBmIqszPKwyUs4Y3aGSqnQ1JB4g_-DUzW2nJ8hRbSD3Ogb6Sd3lek2a8BNe3DUNjyv0xvhN_7z68WIyUaMm2OmRkTQpn-XpZpVeA182kK-HG4rxnjVCsF4WWtJpOvOY3jYeE-1vUT3GqeW0RlABetP_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048590050f.mp4?token=mz3mK9xTjIPusn3irJ7_P3YsQ1Kfu-2ePWxfTqnB3wJrDhtZQRIcWKhu4w0xMGs8IeYTEL1UTzDf_Ww-t8dmlB540sEvZyo-YLPXv8y-BCrbjxKq7wP_qhoI6Bl0I4io2JVsmFwsASGecCNbReuSxnNBsi6_Lk2x8UZSfbhRciwjRGPEjHEpPcp7lBnjiSxBmIqszPKwyUs4Y3aGSqnQ1JB4g_-DUzW2nJ8hRbSD3Ogb6Sd3lek2a8BNe3DUNjyv0xvhN_7z68WIyUaMm2OmRkTQpn-XpZpVeA182kK-HG4rxnjVCsF4WWtJpOvOY3jYeE-1vUT3GqeW0RlABetP_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجار در خط لوله اصلی گاز داغستان‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/126580" target="_blank">📅 21:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126579">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20aff12f03.mp4?token=iJaDo5uud88m-3hbjU0V14k3k-1v1A8EF6aM-FQM7hLedFWy0cvNg9IO0rZuAmgnMfH-D-Y6EVam0udP1DKIOUtHLA6oG_0ZyBBamWB8_6ahkSOkrqKFSuGdtxG4ga5hUdgc_bcTDaYDra7QPQtYQx3Zi3ZvvBiUatThCvtBNLgWkN04DruJxmbB2M7PKiJVtoGf14RH27iurKLUzA1XRyX0xqXB-ZnaGt7zFzWlDC4hne_NSuxj9yYS7MpzzJc4Q7xbpoMz-3W7yEmgO0Fw6erxSgkW_48b0VwUDtxs792cUqK9W4HzEGa5JfKxkC-2bGpUa2jDc1GBG8MrsJtOxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20aff12f03.mp4?token=iJaDo5uud88m-3hbjU0V14k3k-1v1A8EF6aM-FQM7hLedFWy0cvNg9IO0rZuAmgnMfH-D-Y6EVam0udP1DKIOUtHLA6oG_0ZyBBamWB8_6ahkSOkrqKFSuGdtxG4ga5hUdgc_bcTDaYDra7QPQtYQx3Zi3ZvvBiUatThCvtBNLgWkN04DruJxmbB2M7PKiJVtoGf14RH27iurKLUzA1XRyX0xqXB-ZnaGt7zFzWlDC4hne_NSuxj9yYS7MpzzJc4Q7xbpoMz-3W7yEmgO0Fw6erxSgkW_48b0VwUDtxs792cUqK9W4HzEGa5JfKxkC-2bGpUa2jDc1GBG8MrsJtOxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه سرباز
اوکراینی
با
اوربیتال
وِیپورایزر-۲۰۰۰
هدف قرار میگیره!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/126579" target="_blank">📅 21:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126578">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
فوری / رسانه‌های اسرائیلی: «اسرائیل» برآورد می‌کند که ایالات متحده ممکن است در ساعات آینده دست به اقدام نظامی بزند، اما به شکلی که به ازسرگیری جنگ منجر نشود و در عین حال تلاش کند تا حد امکان حادثه را مهار کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/126578" target="_blank">📅 21:18 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
