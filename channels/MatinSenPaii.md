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
<img src="https://cdn1.telesco.pe/file/tvgg9PMB6BsXOejtfe5ONZI2UMBDF80KP-xNM-EbE8hkWfzMuroHZU6MJuM7i8QYJ6LRV3qzmOOjxGWsur1ZjYtl-S5iIOzT1T_f7VgRSMlg0UlNgN66SUXzZR4jiSjMyzalH3khiOOi7IT32nr_TyoX4hBVeZYoNexIbvOE0q0LedOpVKaFvRwAKOrMeU_bArLzgl1MLJ-k1r3LC5zl9qDFV8BuqlzbRMkpP9Gs1o9FynHALF5NtlwfuYKB1As95s-ICrTEsCwJz1qzyvfu-0YtHSR9oTHLcMAdTmRlz7obfX1GkJ__NShfNpd7-tQTb90gRftvVG94_xfzE2ma5w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 155K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-07 19:12:14</div>
<hr>

<div class="tg-post" id="msg-5088">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">این وسط واقعا چیزی که حال یه جمعیتی رو میتونست خراب کنه خبر کنسل شدن آزمون تافل بود</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/MatinSenPaii/5088" target="_blank">📅 16:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5087">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دلار بالاخره به قیمت ماشین مورد علاقه امیرها رسید
🔥
🔥</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/MatinSenPaii/5087" target="_blank">📅 16:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5086">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">خوب شد امسال مدل‌های AI پیشرفت چشمگیری داشتن توی تولید تصویر؛ تا این بنرهای درب و داغون الکامپ یه کم زیباتر بشه</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/MatinSenPaii/5086" target="_blank">📅 13:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5085">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دلار بالاخره به قیمت ماشین مورد علاقه امیرها رسید
🔥
🔥</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/MatinSenPaii/5085" target="_blank">📅 13:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5084">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گویا  OpenAI تصمیم گرفته قرارداد تأمین مدل‌هاش با Cursor رو تموم کنه بعد از اینکه SpaceX کرسر رو خرید
😂
کامیونیتی خارجی هم به شدت از دستش عصبانی شدن و همه‌اش دارن هشتگ میزنن
#ClosedAI</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/MatinSenPaii/5084" target="_blank">📅 13:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5083">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f91f653dec.mp4?token=bV4v3TA-0rkbO_LIUMn7VIJULNsfy64ZayEDnszpQ7ZjWi0FxeaM0rIkq_9kEOGDUbKd5krlfjvdw8BobYnt1mFHfJAA2u0B7f7wEDz6zhW2KWZdjmB8fD0woMkTZbodVNClJuquzCSdcTZueGIQaivhhgNBbddRvVDz7H_0Nncf23SzPi1P9G0Q0e5EmUUj8jljwLwBR021y5sV9u9NyRXrjn8M9gQiMh9z2sgYs1noSoMiJHHolKHnZa9cbysv0dlqMr_WrtdzQ2k9Ria6uhTmMH2mmqhcaqWbnlPWZ3qP2pWrdXJ_EBWYDWrk75yE9k-PN2_RLKnBTr-v9ui6uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f91f653dec.mp4?token=bV4v3TA-0rkbO_LIUMn7VIJULNsfy64ZayEDnszpQ7ZjWi0FxeaM0rIkq_9kEOGDUbKd5krlfjvdw8BobYnt1mFHfJAA2u0B7f7wEDz6zhW2KWZdjmB8fD0woMkTZbodVNClJuquzCSdcTZueGIQaivhhgNBbddRvVDz7H_0Nncf23SzPi1P9G0Q0e5EmUUj8jljwLwBR021y5sV9u9NyRXrjn8M9gQiMh9z2sgYs1noSoMiJHHolKHnZa9cbysv0dlqMr_WrtdzQ2k9Ria6uhTmMH2mmqhcaqWbnlPWZ3qP2pWrdXJ_EBWYDWrk75yE9k-PN2_RLKnBTr-v9ui6uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شرکت Tencent مدل Hy4-preview رو منتشر کرد
🚀
مدل: Hy4-preview — 770B پارامتر MoE با 49B فعال، کانتکست ۱ میلیون توکنی، لایسنس Apache 2.0  مشخصات کلیدی:  1-مقدار ۷۷۰B پارامتر کل ولی فقط ۴۹B برای هر توکن فعال میشه — یعنی قدرت مدل‌های فلگشیپ با هزینه‌ی خیلی کمتر…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/5083" target="_blank">📅 21:42 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5080">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/WUM8PCrBmIxBS0Ck3mcMQmZNr6ZA7q_z85Gtd2nueEcKk42JCWbWg5ru67JC4475dU_Dp9PcL2LKmsN-91xeAfHCjb4lGB93hB7XTZCArSbmZnlHbhGJDGHsf7GKMkGmn42uq6qjbc1vDxcSpS21mdFSZgBHHQfMScYCG2BtL2uVCSPzZpgF1WGs61rmBX1hF4xHg0FPJ0Hr8mYtI7z304d7qkemZ3JZMgaCYjjEOdOzFczyErQbJZ_41XvmAe8m5TomxnqJSZQEpI7fkgPDykJjlcqHJLSQFGGGM6KhFJ68MkjAyqn-mAVDz9zdKXb_iuwo9oTKIdVnXgwVZE1IqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/Yzly-PDVcn6X75a60sPCmg1JTMSMnSooT_79vTHwP7KztPiaP9RP-uKfu52184ID2AWHia9W6QQ8JsL6Z2c-uPEY6xGPfgPNJ0roIMIexzi_vX-WzvDW3d1fiaGbOY8PK1wZ_uAOF-C0scNsVNesaV90K0V5rQCdNNFTkfkB9dZqAoQpMEf0S_i2r18fE9vMKfggiO3bUkWd77VlctBTtKJR4LcnJ1Lkjw7CgJvWe1KxkEtlj3-3-e7UnWF5fkS75ATws9xSa59YkGrB8LU_oPPUNqs3BSwB3ZPx_eN-zzi0BqFZOdwoBdvfkBp422Q2KfAiIeVMgtlnnpYJK_6DwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/Owigalt8pmhYruHOKOWVaRF96iAEiY7FwUEXl5-KTeDBCcsEEkt0R0KrQ_JMNkFpxmLbLqY2ZG7utb88pMnJ2tj5ufxI-10fSpejdGHkGfnhD9PpuPgRiqIEZZI2Ml2q0OHfG3VzCJFgEaxTe5579OunbEbzPTh-waZWC6ih1R2BE6z8R_nynHpmIdNI4whBTvtG58iZGkQsLp6c9O9o2FNi33VWGECy5_Y4bgMqz8LQ6Ay6yzSqsUNGQQ4mZi_dH1kgWC9mhdo89MxPH3xVEHhhn3AeJSLoTNRGIA4JZuyheVTgTFAO6zHXv1j6vnb7yH1yKL0MOITka_ZPyNmf9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">راهنمای زنجیر کردن  Psiphon Desktop
با
whiteaesther
Desktop
🔥
🔥
اول Psiphon را وصل کنید.
در تنظیمات Psiphon proxy محلی را پیدا کنید. و یکی از پورت های زیر را وارد کنید . توصیه میشود از ساکس استفاده کنید
SOCKS5:1080
HTTP:8080
WhiteAesther را باز کنید.
بروید به:
Advanced
→
Routes & transports
→
Anti-blocking
در فیلد
Dial through a local proxy
یکی از این‌ها را وارد کنید:
socks5://127.0.0.1:1080
یا:
http://127.0.0.1:8080
بعد
Save profile
را بزنید.
حالا Connect کنید. مسیر  می‌شود:
App traffic -> WhiteAesther local SOCKS -> Aether/WARP -> Psiphon local upstream -> Internet
اگر میخواهید که whiteaesther سیستم شما را تانل کند روی Full tunnel و اگر نه از پراکسی whiteaesther برای نرم افزارهای خاص خودتون استفاده کنید
نکته : قابلیت exit chain را توی تنظیمات خاموش کنید
⚠️
⚠️
تیم وایت
@whitedns</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/MatinSenPaii/5080" target="_blank">📅 19:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5079">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مدل GLM 5.3 Flash یا همون Ox Alpha، به صورت رایگان روی Cline قرار داره. Cline هم اکستنشن Vs Code داره هم می‌تونید با npm i -g cline خودش رو نصب کنید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/MatinSenPaii/5079" target="_blank">📅 15:16 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T2dSlvO-zCAtACjrHpuwnOwW4xYN7I0PVp3AflhEtlK5vPM8-IKZiAY08ZBIJpvGo9jhvTGZdOjgyWDGxxJWWiuCL7XXrEdDWIyiza9ohNW0WnGZnxhnP5GJxErxb8Z47agA6neKEQfiYJbj9dwbqOKhFnQ2p21blEwCocITQ6mgvhWRfseeLbWj3ogmlovr-xtIYiur1roHFVlUzHWJvlRIst1Ouec7aNorMgXk-U0eSkDh60E8E-VXRz1BinjSwNxor4bTHbnU-KanMsqF6YFLKkrbALSQQaXETtkHY6s4BsmogGsWOrKmpA-qlMBjBvRDwurz2azVe1PmSRQD9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه‌ای که GLM 5.3 Flash برد برای تمیز کردن گندکاری‌های اون دوتا، مقابل خود هزینه‌های GLM 5.3 که تقریبا 20 دلار شده بود</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/MatinSenPaii/5078" target="_blank">📅 15:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5077">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">این سیستم Re-Stream همراه با بکاپ استریم رو ابتدا با GPT 5.6 Sol و GLM 5.3 در تلاش بودم که بنویسم
اما چون نسبتا پیچیده بود و تانل هم داشت و سر اینترنت ایران یهو پکت‌ها غیب می‌شدن،
می‌خواستم Claude Opus 5 رو بندازم به جونش
تا اینکه Ox Alpha اومد
دادم و کلی از جاهاش رو کامل کرد، جوری که واقعا Glm و Gpt نتونسته بودن انجامش بدن
و در نهایت هم خودش، اما نسخه ریویل شده‌اش(GLM 5.3 Flash) اومد و کاملش کرد و فرغونی که از Gpt و Glm 5.3 تحویل گرفته بود رو تبدیل کرد به بوگاتی عملا</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/MatinSenPaii/5077" target="_blank">📅 15:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5076">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b2XMp9-fnZbKLUDYSExaSIWTdGSD0K0YYsFMF72Fyi4zQH2Q5yUCufONRcOIaqXHjTY6ycXkMD99rblq3jdhGIjBAymX7XTUgDci15KH6g_UvaZ_XFNlaon-fA14MeMVvSSeYf3cKeNCgJ-gszuktCgH9Xm32TUSPviQ3_6pBccupP0ePh53MInl7NCD3QA5AcYD40jpU-TiOkgOKkICMRnF19TCnl4nNHjPoADc2gLdSsRy4ieM8CPlqaxbLsdHCO7da1RnzKjj0MczHV82Q_RWLgGwGkIMeGp07i-ZQa9wuVoii3CD6C_8MgQG27wIckX-aE2fJ6mD58qp_gU9Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاری که انجام دادم برای استریم‌ها این بودش که اگر نت من قطع شد، کل استریم قطع نشه و برای ۱۲۰ ثانیه روی استریم بمونه تا قبل از اینکه من برگردم. دیگه نیاز به رفرش ندارید شما و استریم هم تیکه تیکه نمیشه  و در کل به این میگن سیستم Backup Stream</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/MatinSenPaii/5076" target="_blank">📅 15:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5075">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n_Go-JHD0u8DI1siziFHzTcbr7DFOAdhCEpGFOgO4HKyh9RPo9VPP1DlOPr7TK9sDhRPM3xTc-rY5O0kYYiIJCjtU_eWxFlKh56nBBMAf4qiw11aC8GnDCDZufzUhI9Lwce5kjN-jPIbWHR-B99BnZHQUS0Xfcz54CXOdCzgouNpDcRH5WfUUBIf6VPAhrnczijf9rYA8p3KlehChdMk3DAN23VQlQDZk6mN_fBxrqkly6BMMb1S-4kPkJ0urLRzmPpnuKqneLzJu0yYZfeuHyyN6vqb2g-Di4PqRi0koqhJXkj-ANsaVBh0t__IQgW5yv3IBmF4a4z2oDxyA6tbQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاری که انجام دادم برای استریم‌ها این بودش که اگر نت من قطع شد، کل استریم قطع نشه و برای ۱۲۰ ثانیه روی استریم بمونه تا قبل از اینکه من برگردم.
دیگه نیاز به رفرش ندارید شما و استریم هم تیکه تیکه نمیشه
و در کل به این میگن سیستم Backup Stream</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/MatinSenPaii/5075" target="_blank">📅 14:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sGKFbh2eAFVYfUer5nCjL_UOvy582DH3SnHz2O8jlbGQyhbjw8-YeFo4F9hUT6VRaFBRCMx6m7BBz2PWkqjrd-_RG9IbBl0l39r7u0gg9Ra6vh__DLUk6csW-mnLtgIkkt7kMAa-Y7JZqxBvgpdbSTCzKqdjJliNAJiy3MD1nXF7yGDEqBlaPWPVs9-cBbX2NcfV2NY0B5J3mnKmOrgZCYQoGdMvWunLoyB5GReSPVonUoI7nZzNuzTZ3A8OA_xyPn14O4Di1gfEEYR2KcivzQFH68H_BQJDwRSyONLoBFMaRlnhw1MOmFvsU7Ve2UUXQ7XOuYpILhOvSEwlsIRMVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت
Tencent مدل Hy4-preview رو منتشر کرد
🚀
مدل: Hy4-preview — 770B پارامتر MoE با 49B فعال، کانتکست ۱ میلیون توکنی، لایسنس Apache 2.0
مشخصات کلیدی:
1-مقدار
۷۷۰B پارامتر کل
ولی فقط
۴۹B
برای هر توکن فعال میشه — یعنی قدرت مدل‌های فلگشیپ با هزینه‌ی خیلی کمتر
2- روی بنچمارک
DeepSWE
از ۲۸ (Hy3) رفته روی
۶۴.۳
— تقریباً دو برابر
3- بنچمارک
Terminal-Bench 2.1
: نمره
۸۵.۴
— هم‌تراز GLM-5.3 و Claude Opus
4- بنچمارک
Code Arena WebDev
: رتبه
#5
با ۱۶۳۳ امتیاز — بین مدل‌های متن‌باز
#3
5- ارزیابی داخلی با
۱۶۳ متخصص
: Hy4 با
۲.۹۹/۴
بالاتر از Kimi K3 و GLM-5.3
قیمت API (خیلی رقابتی):
- Input:
$0.83
به ازای هر ۱ میلیون توکن
- Output:
$2.50
- Cached input:
$0.04
اما هنوز، رقابت رو به GLM 5.3 Flash باخته به نظرم</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/MatinSenPaii/5074" target="_blank">📅 13:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5073">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l7up1oXpxs-cBwZ20i9nrfY2hOjsm7qTqQL1kgzdIVanCU-1-sIc5OyyEYN38Mxb10AthTBmatydyzGdgeZGTjQrn5fUquQ-CE2DGgTCBcDn9Uj2CLEZkhcSKW3sZAT62ViuhgPFowiGSG7xNPz2lorR1JnIkttu2qsl9a20Hfg-nOGu6MVy2GeMyy93w9sYhr7wr1bfBpWaWwSne4LKhRKpub6p_VFRIOoZNcWjvGodPuDxxUbq2sJ-yy9R7x4ptvgYShAaehwOQtLKCQqZ-tsxyyVF-2sIf91-D-fUvubCMKjuy5gz910hUFhHS4oDZ7q7tR34juTyn1r5WtYBTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐂
چالش Ox Alpha با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.  هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha: https://youtu.be/FIhoccZtpZQ  برای شرکت در چالش: 1-…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/MatinSenPaii/5073" target="_blank">📅 13:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5072">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h5XtLHmWNNBDSoTNVpcWLFocJOYDQ5nbW5dLO7sRrr12kiqdfG8QryzmZws-O5RuRBPQls885eVuNVqGTVUpFh3UpjpAiKdtMDYd4JcGVxlWPGwjJIEdz7dOdDKRJwlT6BEgXZ5mWFEfe5pUGcV-jo1R6vQGpJiDKD44BwWAccaJ92fHpXxbFtNP3cHuJs6B0aOCClYh2YRfaAepBjt6ip9XsIPUlOMyriFloR2qq734VjXZUU9wXnZf_uTH3C8jafKE-O5YVZVbuyM9ADeC-wu2hwGdaWludm5jupJnwD62t6iwwZdMhAEvPmhdl7yHLLKTJ2LyRsacyK18pw3law.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل ۱۲۵ میلیاردی Qwen 3.8 Flash Next در بنچمارک Agentic Index با ثبت امتیاز ۵۶، توانست Kimi K3 Max را پشت سر بگذارد و با یک قدم فاصله درست پشت سر Claude Fable 5 قرار بگیرد؛ اما نکته شگفت‌انگیز عملکرد آن نیست، نحوه اجرای آن است:
• سرعت: ۲۱ توکن بر ثانیه
• پنجره زمینه: ۲۵۰ هزار توکن
• سخت‌افزار: فقط یک کارت گرافیک RTX 4090 و ۱۰۰ گیگابایت رم اقتصادی DDR4
مدلی با این ابعاد تا همین دیروز به کلاسترهای گران‌قیمت نیاز داشت، اما امروز به‌صورت کاملاً محلی روی یک سیستم دسکتاپ اجرا می‌شود. مرز بین مدل‌های ابری و اجرای لوکال عملاً از بین رفت.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/5072" target="_blank">📅 12:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5071">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a2386a8b3.mp4?token=k5WWw9vplCOHiWc6L5E6pKpDWarqQE3A3ce9LE6iodewmIhv7NXxG_7ZNvqSjn5-hbOeKd600_MrpjxdcJG2ktEJV9RDe-T6YQQZzdUe3n6OVUZUBzozOjwFjDs3oa4DJE1uJnv86O85fmTu9JdHr9Flj8k6HMTwfg1oZMgGniD1P_oBYxKOOhndIyykyaB6AH1_yZVENKkFnew4FMeNSYYVGvVZc1OexI7NF29NHDNHbrc16bjEcisuvHeB2Qo2UY6JXRRpn0UikwTv0uIwyIEoJOTw_R1jb9WS24jp3SzlDy6vCeB13RprUlChelut3iSmF548BHfI6aBbCpdK9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a2386a8b3.mp4?token=k5WWw9vplCOHiWc6L5E6pKpDWarqQE3A3ce9LE6iodewmIhv7NXxG_7ZNvqSjn5-hbOeKd600_MrpjxdcJG2ktEJV9RDe-T6YQQZzdUe3n6OVUZUBzozOjwFjDs3oa4DJE1uJnv86O85fmTu9JdHr9Flj8k6HMTwfg1oZMgGniD1P_oBYxKOOhndIyykyaB6AH1_yZVENKkFnew4FMeNSYYVGvVZc1OexI7NF29NHDNHbrc16bjEcisuvHeB2Qo2UY6JXRRpn0UikwTv0uIwyIEoJOTw_R1jb9WS24jp3SzlDy6vCeB13RprUlChelut3iSmF548BHfI6aBbCpdK9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این لودینگ ها هم جدیدن و خلاقانه خوبیش اینه که SVG هستن و توی سایت و اپلیکیشن و هرجایی می‌تونید ازش استفاده کنید:
circleloaders.dominikakissi.com
@Linuxor</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/5071" target="_blank">📅 18:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5070">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NtTYPmSECCKy8ZFH0Mw3NyKvTr0r2iyWJtTIuAsswL3mPs3-V-yrpG5NuM1BQiWJYlw1LURBgHy15TdY7WIu5GDWCcMJeKkZ6Xu-yvJuABEmaHiMjkJBvmS2DjZoD0TfYRqmf9VI7MvvRID6sgOgAIm5Sph2E7bIPRgfXea60v_yl1J8OL5_YpE5K2P31N_A9pbtiZVFV4404L1FH5SB4aKIyTT6ctISvMJai_mMSFaq1zZsES416y6Sih3-v8kzCbULK4Ru2n-umzifutEQHw-g5ol63JuHd_H9nMv6WU5wNsef2LbjxpYXTZtINmSkZaIrU-Z3KSOcbgyRhaI6Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچقدر از هوشمندیش هم بگم کم گفتم</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/5070" target="_blank">📅 13:49 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YuEGgTaC7HC1gDwT9PdDnXJrLUoAHwKfNxtrOL_WT8gMtbm7Q2yopVla3mVuI4ft9bkJAVw-vQOSPjngY4snV-TTqAmC0OB-_AWWgd-fFr9R_zpztf_9uogiYElE1If8Qoy02faPDBDKTBGCmdXqkhsSYpGtdvbJUKq4y9SwdTrAhWjbxB26z-yIGMNe8UmGQr5rU-TyYDVOhrPpEHb_u3dN1u5qAk-DMI6umBN5bLHcs7VkUH18_Z1eLuutuBEYqjpO8Kc2LubYyhFTZpdltNZMWONoPrEVWDt9qJ7Sj_ITbTtPBDLBxUj6B4ryPLVrl19SAFZ2vLret83ZDSnrzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ Input Cache اش خارق‌العادست
روی خود هارنس OpenCode</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/5069" target="_blank">📅 13:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5068">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GeODLWtiGx5V4PhWsxptQzmcpUEm5cOS8qyS7P9xVweljcnBSZhRm6SKRpQ7HtdYuKPLqa5Dqt1VqZpnEQ8IpSJYJfiOy7VbuGZqutXmLLKzQdrIOj0wyI0QfeJwfyyrBQbU9HFp_4auyBEefO4qRW4Nc9NJKYpYza5VNG8GibQ9Cb6NUaQQZdENad91GrYFqo_Wgtlu4gGtpdHL1cpphhqGQF3e8uj1Xs3qihtGTjNLVHjstXa31k20mcYOQ0a2eyOHep2PFNhP6BO1Q179uYeeyRrqgQgbiwA5t-mWcYiN83ZwW0hbe091_SwS1Mn4UApAe4gYPXJpfOEWacErKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصرفش خییییییییییییلی نسبت به GLM 5.3 اوکی تره
و راجب هوشمند بودنش هم که دیگه یه ویدئو کامل دادم نیازی نیست بیشتر صحبت کنم. باز ما میگیم درود بر مدل‌های چینی به یه سریا بر میخوره</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/5068" target="_blank">📅 13:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5067">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NjhPb1GPrrClcOAktCz4jD6nfzRc4E2zL6IcBJQwDqDUkESodAyknb4FDJbUiqP_w0BPwIyZNjvx1kLPwCMvKTirC5U76shB6SGdhmm_JwWK7nu6wOz4AsHIyoll_f3G9ZKYXv0U6hMX8XH-V75LLx_LMO3WI1ByQ3cbI_YCD6nRO2RduDNBAaJqMIVx-qOC-t1ocfvJLhvUGghgJDxoK4b_AZHkY7dBjE5FU1lsaPy2PmCZddEy4FTaF_-aXlDFZ_SAV-sbwCU7DD0Ds1jfSb1x3y-ll9zj3AH98S6XthWOOGt_btgkuiDfmG3DeRmJLl7yOZvXKY2C6nDwQgsITQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی درد داشت که Ox Alpha رو عوض کردم روی GLM 5.3 Flash و الان دارم واسش پول میدم روی OpenCode Go
😭</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5067" target="_blank">📅 13:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5066">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">خیلی درد داشت که Ox Alpha رو عوض کردم روی GLM 5.3 Flash و الان دارم واسش پول میدم روی OpenCode Go
😭</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/5066" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5065">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🐂
چالش Ox Alpha با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.  هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha: https://youtu.be/FIhoccZtpZQ  برای شرکت در چالش: 1-…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5065" target="_blank">📅 12:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5064">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V1c4I_YN9Os7Im8XT_b3aaU-nxHn-oZISmBDDug93Av1hVh4rpi7Z0rYwlrmSQuF7uVruSDxVns5xzFptbw73UB0pa78_kjkr-7-NlWhuDBhWrp01q7PkL2rMPoDjH5i1LsUESehu5MOUPCc5EFosnwHqM_2sDyRI-jua0_moMUQ-MQawU6esWu-Tnem_bT9I3bbSE0tree1s-ILl3miWW0Ad6RW1HONDHerL8nm5YbGLHGDAZ7CHWcxc2OPD-9V3DKLALwI3ZkOLhdJOYEbfoBlVUDzNg6xPLmQBQe9JgExjNcsucHu-nDLb3SN2pRpGvG94RaHBGNGRHAEEU4q7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM 5.3 Flash یا همون Ox Alpha، به صورت رایگان روی Cline قرار داره. Cline هم اکستنشن Vs Code داره هم می‌تونید با
npm i -g cline
خودش رو نصب کنید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5064" target="_blank">📅 02:26 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BSy6nVtqDaNrLeKxvihhVPW-Z1JOBRX_e6QcPBDh8WQuFCNc3XCyjH3YWfFfgYs0gqPlTNqAh0P_WwvpS1W4eG_JsVj5NDg7gHW422UpiIx9pbUKbDAhAqiqV3Lhxb_niu6BrjjKAZbSdvM9u0yRWHnmOW2V0MIk32zOinvzil9jBU1mkjdV_93JGEtAYJeq4ELTDfLTVQWiS53JilEtlIQgTv5cVRlqE12jYNtC8thZAaDYU84-YRKlkqvFz9MIpoar7cXAQrpY3fagmFn4nu9Xz0l4Oio16yHUbHpm0ChCOdquRi4SEGSbn4yz6DLLsC1aaSfKEr4Wa3tlXkAm6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی این بنچمارکا همه‌اش GLM 5.3-Flash رو با GLM 5.2 مقایسه میکنن سؤالم اینه که چرا با خود GLM 5.3 مقایسه نمی‌کنن؟</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5063" target="_blank">📅 21:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5062">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">توی این بنچمارکا همه‌اش GLM 5.3-Flash رو با GLM 5.2 مقایسه میکنن
سؤالم اینه که چرا با خود GLM 5.3 مقایسه نمی‌کنن؟</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/5062" target="_blank">📅 21:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5058">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bPiOVx6Ih3kl7Qmz6l7O4396tPJiuOx3X2f_UMirLth8XQRvLazL_qXlCoRY2s5oKjy8tjpQ91Zgw7pp_An8NLc2e71hIKWEYoJED7wQ0p-l1gX4aW3rIrvcxr91nP-1vuwCljh-qjQWLhZv2AjFdFOl4w5ZW-qeJQ3n-E_aYf6zFHfRHYA6aKwftxHuNE2HpDpTnRNfXHNz1tlh09BtJaPRxYgUEyRbslQ1GhQt9UsDuMCj6SFzpsrLutHqj4HPMRyh2hnp-5bV1ocRU9mVBIoT-BM7fUnyZqT_b62P4OJB3Ev0GgGiP19CwAGSSmDvV-qWJQV-qR_qYUh3T363yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QOBgEquO5EAsLLUdCE1O4uA7uE2hLHHMcZLMf2qOt-WVvkRhPv5NdgD7RevQ8_QWT0VE3EsR-rn7AapjItFGY69XHuDAilOrD_eLMjD61SqDA-sLIZsw2cYl_5ilxA1vFPGJBVIggGbdGeryOpR79uVaAfDg7LinJC9K-Ewbh2ZY1QHEqpo6ey7EjxyEM_1UjjucosDPTi51_I4HfBIejyhtjpQIXf6kZuBd_JX0nsi3ZI44ZU2CC-Dd9EQ-OKqMEELVWOmpijFHTwYLqhF7ypPHgIKEA1MRrfueFiexjfspErY14GQJHSnSIaYMjJqxRQB8_Im7HkIVbutGmQxfQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PXnse9rk9wCtdIObzUftysjGrR7QWqXTja-2hEAGIW9iO-Yn39AJ3Y6UqwULcU6Srki1yOm0AvKmi0zHOWSQARFh0fcPd-8l-sqRWWyfSu-6X3G3eq-RDTEa1dM8Wf9GxBMoW0d_TX8W8jJFrnzDi-Mh8lRRFz5QgJ8CePfolYYP5oHtCwG3952FnRTABQNV8_koHFMbGznwdFs0rcQIUSN7fDSkcf2A67fr2RcMjdpwWw1-0XWQAOdYDG6x7MmNU2lgUmvRbkqPuAbH44VB5t69Jvb2olNKPWf6okoLc_8btvtAlWPF9RCkHu7iknQooiAp2dkLIouWVNFNvOygCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/b6BzoasnF1-XRYGqIThCXdbgoLlZt6GFlDcAQjsrg5n1nn2y-lTcRWXAJ84gRVyEPj_q1MajgIrORcuPmRL1OQnlvrUQUUWKif3MfRLVAvqUYHDSxzO8Jwk_c9GagLnhMzITwIMmBOxqvE90CdrmTErtfuWOUXoi5FuH6SpRGrpyfUUSIwjTEeNokdtFEcFvoUn-CC3ZIwApwlH0eYUxAp_pLXPWLo2_j3B4pq_HS3rnk0x8mAeSu5BXWeNI3frNZH4jPdRr08m1Z1iHd99zoHRlReC_v_QcSTvp78Nrpi_1XHtGEkmFyAUwCk-hm624rEBACnBngMjE0s99OApFjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معرفی GLM-5.3-Flash و ماجرای Ox Alpha
شرکت چینی
Z.ai
بالاخره مدل GLM-5.3-Flash را رسماً معرفی کرد؛ مدلی با ۳۲۰ میلیارد پارامتر (معماری ۳۲۰B-A18B)، لایسنس کاملا متن‌باز MIT، کانتکست یک میلیون توکنی و قابلیت چندوجهی (multimodal)، که به‌طور کامل روی تراشه‌های هوش مصنوعی داخلی چین اجرا می‌شود.
نکته جالب ماجرا، پیشینه‌ی این مدل است. حدود یک هفته قبل از رونمایی رسمی، یک مدل ناشناس با نام Ox Alpha به‌صورت رایگان روی پلتفرم‌هایی مثل OpenRouter ظاهر شد و به‌سرعت بین توسعه‌دهندگان وایرال شد؛ در عرض چند روز، حجم مصرف توکن آن به رقم نجومی ۴۲ تریلیون توکن در شش روز رسید و صدر جدول‌های استفاده را قبضه کرد. جامعه‌ی فنی با تحلیل نشانه‌های تکنیکال (مثل نوع توکنایزر و کدهای خطای مشخص API) به این نتیجه رسیدند که Ox Alpha احتمالاً نسخه‌ی آزمایشی همین مدل GLM است، تا اینکه بلومبرگ گزارش داد
Z.ai
این حدس را تأیید کرده و وعده‌ی انتشار رسمی وزن‌های مدل را داد. جالب است که Ox Alpha پنجمین مدل ناشناسی بود که طی شش ماه اخیر همین الگو را تکرار کرد (قبلاً Pony Alpha از GLM-5 و Hunter Alpha از Xiaomi هم به همین شکل رونمایی شده بودند).
از نظر قیمت، GLM-5.3-Flash بسیار رقابتی است: ۰.۱۵ دلار برای هر یک‌میلیون توکن ورودی، ۰.۵۰ دلار برای خروجی و ۰.۰۳ دلار برای ورودی کش‌شده. روی بنچمارک کدنویسی واقعی (Code Bench) در همه‌ی سطوح تلاش از نسخه‌ی قبلی (GLM-5.2) بهتر عمل کرده و با Claude Opus 4.8 برابری می‌کند!
از نظر معماری هم ترکیبی از MoE، Sparse Attention، Linear Attention و لایه MTP به‌کار رفته که باعث شده حافظه KV-Cache به ازای هر لایه حدود ۴.۴۴ برابر و محاسبات attention به ازای هر توکن حدود ۳ برابر کاهش پیدا کند؛
خلاصه: هوش وحشتناک بیشتر با محاسبات بسیار کمتر.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5058" target="_blank">📅 18:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5055">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Lu-noBC2OkIx5Je8QtN7IxYB8mqnQqRzNVrDJBU9Oh_c5IaePRIEk0HBnTROzZ4j1QHNo4CkDt0J559mx30lxIk8z29cwqN8Be-bg229k7_roZI2JUQlwdU0gQZWj54kIVCy6Eab0eMerGSpDgc91272Lq73LBdw7q3hfyQOcwYuZMXAscHjJLE2erYSO-S8IUIPSKWWrym3Z1ltO-ki67lEh0xjErwY0LwvnleysA5zLy-4NTRpisl2XZlPPAwSuqn4iGNF02mZ9e_YsFPhsP-35uZVmFdoZoSb9_spJr33JI1Q-Q-wI8m9lATdPCID7AO2p0i3BYUrG7OFu9KoSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SAjTslB9Bz81qWwW_U3VEzU0NF_T3fB0nh0B02ilbbj-kGrQSfqkaJeQH1BMArWIZn1jNgWFSuCbtwK0nlLZDEuA0Bfuj_RSl1OQdIoeoBJgKDPcJOJbtBdQV0325zRJDrp4TuCvoUAIH046k0P5WwTBvzguqylNIQDRgzhywTQDxijqtk2ePkX-X2wTzkG5zxAyMNlKyiosO16uHrRJn_ET8AKrBTxpDhX-ko5MpNP5GXvQZMv0zc2N_GAD5q6-QWG6G74nWhEYH9t01sFlyaCDhE4LKh2VwTpvNDyHBk1D2v9TORd-w3gESVEeUleieJB8GiqMW1uIOt-Ayo_3IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/n9P31Pbg_BX2iVEsmWrYJDREg5w9YOAHDS2F76367FoHqIShq_zyfVS7hWHHBXZNHyTU0AjEsNwbHxKqjVzLgwCAWToN54HkgDOEAo1uJsO3pfME89sc8wWlAl47lPERYd14ga9SwXKrt78MH6s9asEdTTkjEsA_zwLkrlOF2KO0vd1UYtglxgkWl2cKaQZQOlWy5hiXAITvubQnWc39xaY0jMDv6OF6x7CiG2jahdrt3G6e-OuoXBsq3huhpuA3SOcm_v8g55IEz7dDJyzh6jJ-w87KbgqY23unbACKL6d9JrGVCK7pEbZK5oAOcqk9iMh85xgZwIpgq6WWkQ1CFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">باورم نمیشه
running Entirely on Chinese AI Chips
😐</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/5055" target="_blank">📅 18:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5054">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">خبر:
مدل Ox Alpha در واقع GLM 5.3 Flaah بود و گویا حدس همه درست بود و جمنای نبود
🥲
اما....
مگه میشهههههه
مدل فلش از مدل اصلی انقدر قوی‌تر
😭
😭
برم تحقیق کنم ببینم چی شد این دو ساعت که خواب بودم</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/5054" target="_blank">📅 18:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5053">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WUToHdkXr7BK-0G8EWAi_ECvGSrAvKfUEMSVWfpHGqYIHceeR2Rx6_J8DsibnRQ3pVFRR999YabmEdG2ARt7MDwuGZiCu1AY6xC5AdI4G8GKIpM-_c3WytQbEF73SM1LMmCRnhdt3RDdpahLQ9ybsocPHF_CwcQStWt4Mrv9fV3vUhhdApRX6mgj_kimDA2A8mTVg2_ziK5lck5SZZ4-xnwdtxdp0Lw3WLCTt9AgY4z0i2CSCkMejcmTeyhVLTZRjQLLzgfTO52y4B57bB2NnouwAvg0f0j6-1ep1dc6QbjXY2dt3z57bjfEO_MkRo74Ul1LRtfLS0t-pRCSdXOXqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو ساعت خوابیدما
😂
😂
😂</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5053" target="_blank">📅 18:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5052">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🐂
چالش Ox Alpha با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.  هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha: https://youtu.be/FIhoccZtpZQ  برای شرکت در چالش: 1-…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5052" target="_blank">📅 10:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5051">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iPAaK58_sm4IfgH34yzjk-dg5yPVwCk7SbwakAJaejQPaLErBkFZK3wX8HkhIkNj5oj4LTCFqu5p5lV3fUK8OLm9kxpnlUFE0GhGPXiR4JQCztwNImlPuFw1xev7wNZA7yZlz-8ZQqFpgoMA3GJFlFl6QJetwLbA51JmIjNboJ3ISDZ_iGFDDUCcDY8JJfSPWqUB5MOFymePGUSEdKxTbDX8CjaXKnLG9h_pztiKZzJtT8Tr6frfvpnbUAfreDyaMxOMuaZ0f7stKpp48keaHZ-2tajDL2A6zCbiF2QOg8bbniIgb0Nm6M9ZuzkucrOhNXQGLWss2xgWjx4LGjbPWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐂
چالش Ox Alpha
با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.
هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha:
https://youtu.be/FIhoccZtpZQ
برای شرکت در چالش:
1- ابزار یا پروژه‌ای که ساختید رو همراه با یه توضیح کوتاه و ترجیحاً عکس/ویدئو ازش توییت کنید.
2- من رو توی توییت تگ کنید:
@MatinSenPai
3- عضو کانال اسپانسر چالش، Lira Candles باشید:
https://t.me/liracandles
من پروژه‌هایی که برام جالب باشن رو ری‌توییت می‌کنم و در نهایت از بین شرکت‌کننده‌ها ۵ پروژه برتر رو انتخاب می‌کنم.
🔥
🎁
جایزه هرکدوم از ۵ برنده: یک
شمع صدف
و
توت‌فرنگی
از Lira
🕯️
🍓
معیار انتخابم بیشتر روی خلاقیت ایده، کاربردی بودن و کیفیت چیزی که با Ox Alpha ساختید خواهد بود.
تا فردا همین ساعت می‌تونید توی چالش شرکت کنید! چون احتمالا آخرین مهلت استفاده‌ی رایگان از مدل Ox Alpha خواهد بود طبق گفته‌ی OpenCode</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5051" target="_blank">📅 05:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5050">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">به زودی آموزش ویدئویی این ویزا کارت مجازی و روش گرفتن آفرهای رایگان و اینکه چطوری وصلش کنید به Google Pay و... رو می‌ذارم
🎨</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5050" target="_blank">📅 01:29 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5049">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EbNJd4ur16uF98xKtw9eu6L2C6sUIhDNXTxmbFvvu2LMc8ZmZjC47R9bK-afNgqXcfBI7F1WqLHBF27NLvOhIfSf3ZbXYXHgXT4VALZFuN8MxL9i9d6LqxhqEYAm4TtcjcdPVOCD08t3Qy7LCAHPljL0EL0FE3V6JeOI8_Gzi-KH9RXeJkkZdggTz0SubkgPfYLVeuPldnc7u0frxkq70-BXG_u8yxgAv8lGqqQNDqxiYn6-U13aEirLSEIJU2IIrdcsfr6Cqix6mwZwJinsN2K-PNjpl2YY-RfrmAPh62-63_KAL7RBd_BxgXVqY2RB66rTHj4BKPTYZ1NgJdwX9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قدرتمندتر از Fable 5 ولی رایگان! مدل مرموز Ox Alpha
توی این ویدئو رفتیم سراغ مدل مرموز Ox Alpha و اون پروژه‌ای که توی ویدئوی قبلی زدیم رو ارتقا میدیم باهاش! این مدل، به تازگی اومده و یه مدل مرموزه که هنوز اعلام نشده مال کدوم شرکته، اما بررسی و تحلیل می‌کنیم که مال کجا می‌تونه باشه. و همینطور بهتون میگم که چطور می‌تونید رایگان ازش استفاده کنید و کد بزنید
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5049" target="_blank">📅 00:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5048">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دوستان من کمی از لحاظ جسمی مشکل برام به وجود اومده بود. الان رو به راهم
سعی می‌کنم ویدئوی x alpha رو زودتر بذارم
❤️</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5048" target="_blank">📅 22:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5047">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">و خب من نظرم اینه که، Train بشه که بشه:)) مدل‌های قوی‌تر، ارزونتری که الان هستن و داریم ازشون استفاده می‌کنیم، بخشیش از همین طریق قدرتمندتر شدن
ولی خب شما باز اگر نگران «حریم خصوصی» هستید، دور چین و مدل رایگان و contributer رو خط بکشید</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/5047" target="_blank">📅 11:25 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5046">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">به خاطر جالب بودن این پیشرفتش فرستادم. وگرنه به نظرم این نگرانی تا حدودی بی‌مورده.
زمانی که از مدل چینی/رایگان استفاده می‌کنیم، عملا داریم امضا میکنیم که از دیتامون استفاده بشه واسه‌ی Train کردن مدل.</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5046" target="_blank">📅 11:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5045">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6f33bcf78a.mp4?token=pQWTLz2sfZ4oI_SMwsd8sjY0ZEqnHqYFxY7zIU_rqdcNjjFisRGcTA6Bmg75IlNcp4NHHpwuOvCY5iEP47cIobxX3sc2LAhfrrUV50GX1HaN1LVMApC21JhW4Psrh_hzfAq0yQIjQv46c-vNa2FZ-gLOHGJZk7hUBUwkSJK5mcTCciTEtycUjZhyJIKvAsROFmL93gEmoUWB4dKwfkwK0S4HoKz98Z5DXVIbTVcfUZ2_kPXykfWVkekerT5cepfMljVRUzOZG_3usF-aJerQSUhudFR3UPLwYkAgFvdunhg7p-qg644UniMixgw2o41N4_zyz3xWVj5uBvnDDxjkNWhi2Y6SQu3tnplpTXn2CpZyK1KqhWj3HNdc_lshEKLieSGgx3fLxlVHUQLcpQ45ulFi4T-T-aiXNVkOogIZvcKxUYJZW-nz0MaDupKeyW0l20kNpnZl7pkVOFPu1dQZf31mg-_9muYILlJkmIqXzXoJaGmgyjK5B-pq4125CDdUQAci_jl9RthwAzYdevcpMqW-ywrOq5lTwi8uxHc29K9GyzX36kYf1VY61Ik2WbTWA1CZflTGFukcN27LlsUEk-qs1FwlSWSOmjFOJve5Ku4LZ0LFZ7904HDfAmxcelFAu3TkIE97kKzrc1QZHIBtJKoo5-Vio622zyAaa-ymIdc" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6f33bcf78a.mp4?token=pQWTLz2sfZ4oI_SMwsd8sjY0ZEqnHqYFxY7zIU_rqdcNjjFisRGcTA6Bmg75IlNcp4NHHpwuOvCY5iEP47cIobxX3sc2LAhfrrUV50GX1HaN1LVMApC21JhW4Psrh_hzfAq0yQIjQv46c-vNa2FZ-gLOHGJZk7hUBUwkSJK5mcTCciTEtycUjZhyJIKvAsROFmL93gEmoUWB4dKwfkwK0S4HoKz98Z5DXVIbTVcfUZ2_kPXykfWVkekerT5cepfMljVRUzOZG_3usF-aJerQSUhudFR3UPLwYkAgFvdunhg7p-qg644UniMixgw2o41N4_zyz3xWVj5uBvnDDxjkNWhi2Y6SQu3tnplpTXn2CpZyK1KqhWj3HNdc_lshEKLieSGgx3fLxlVHUQLcpQ45ulFi4T-T-aiXNVkOogIZvcKxUYJZW-nz0MaDupKeyW0l20kNpnZl7pkVOFPu1dQZf31mg-_9muYILlJkmIqXzXoJaGmgyjK5B-pq4125CDdUQAci_jl9RthwAzYdevcpMqW-ywrOq5lTwi8uxHc29K9GyzX36kYf1VY61Ik2WbTWA1CZflTGFukcN27LlsUEk-qs1FwlSWSOmjFOJve5Ku4LZ0LFZ7904HDfAmxcelFAu3TkIE97kKzrc1QZHIBtJKoo5-Vio622zyAaa-ymIdc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک نکته عجیب در تست‌های اخیر کاربران از مدل Ox Alpha دیده شده که واقعاً سؤال‌برانگیز است.
همان پرامپت روز اول، بدون حتی یک کلمه تغییر، حالا خروجی بسیار دقیق‌تر و جزئی‌تری تولید می‌کند؛ مخصوصاً در مدل‌سازی سه‌بعدی موتور Raptor که اختلاف کیفیت با خروجی قبلی کاملاً محسوس است.
اما سؤال اصلی اینجاست:
اگر پرامپت همان است و آپدیت رسمی هم اعلام نشده، این جهش کیفیت دقیقاً از کجا آمده؟
آیا مدل در سکوت روی داده‌های جدید Fine-tune شده؟
آیا وزن‌های مدل یا پایپ‌لاین رندرینگ پشت صحنه تغییر کرده؟
یا Ox Alpha واقعاً نوعی یادگیری مداوم دارد؟
اگر این تغییرات بدون اطلاع‌رسانی رسمی در حال رخ دادن باشد، ما فقط با یک مدل بهتر طرف نیستیم؛ بلکه با مدلی مواجهیم که رفتار و توانایی‌هایش می‌تواند بدون انتشار نسخه جدید تغییر کند.
و این، از خودِ افزایش کیفیت جالب‌تر و البته نگران‌کننده‌تر است.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/5045" target="_blank">📅 11:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5044">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">راجب یه پادکست جالب شنیدم در مورد یه تیم نرم‌افزار نروژی که 4 ماه کامل از کلاد استفاده کردن و بعدش کلا بیخیال شدن برگشتن روی روش سنتی خودشون
فردا خلاصه‌اش رو واستون می‌ذارم</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5044" target="_blank">📅 00:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5043">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">نمیدونم واقعا چی بگم راجب اقتصاد
برق
...
می‌خواستم امشب استریم بذارم و بریم سراغ اخبار ai، برق رفت کلا تمرکز و انگیزه‌ام پودر شد.
کلا همیشه ترجیح میدم کمتر صحبت کنم راجب بدبختیامون چون همه جا میشنوید. و بیشتر تمرکز رو بذارم روی کار که کمی از این فضای حال به هم زن اقتصادی کشور دور بشیم...</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/5043" target="_blank">📅 22:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5042">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ما الان داریم دقیقا مسیر ونزوئلا رو میریم.</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/5042" target="_blank">📅 20:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5041">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">راستی بچه‌ها پلن 5 دلاری OpenCode Go رو من با همین روش گرفتم. اگر که خواستید بگیرید میتونید به GLM 5.3 و اینها دسترسی داشته باشید به ارزش 60 دلار مجموعا: https://t.me/MatinSenPaii/4915</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/5041" target="_blank">📅 19:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5040">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/5040" target="_blank">📅 18:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5039">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/5039" target="_blank">📅 18:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5038">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">☠️
آموزش OpenCode، رقیب رایگان Claude Code
☀️
⭐️
توی این ویدئو: 1- با همدیگه OpenCode رو نصب می‌کنیم(کاملا رایگانه امکاناتش و اوپن سورسه) 2- طرز استفاده ازش رو یاد میگیریم و بهتون میگم کجاها خوبه ازش استفاده کنید 3- یه چیز مسخره با میمو می‌نویسیم(توی ویدئوی…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5038" target="_blank">📅 18:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5037">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g8dR0PgiL4_OmBVnu7qGC3YvVJeElBBRWvF85QxwZPA1du_0Bl2na49kGaeuCGHtMDFjYbXWvcKjqohLsP4P_hN8xDV7_d06Kn2J9IhFgLU-jW5wlp1UtYLJCe2hRP00IWCAJ-BtMcPiIstz6BX_mKgvxBEgifj7EDpjmLJx4dcMwj1HKL5HMuKyuWNAJiEaK6jjRNQi68LW2Zjih0DD2_2qt7yyuFwq4bJOcnnPjVs0hWPk981ALxnFLfn0i3Xxb6NfgxN-4lDb8MNVj4I5_QmgLr-5vZ1Vpzq0f6zYyG5ctA9c0HEskKiPwJJOLvoNDRaHbMfVMLr2XZdYX-jJ1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش OpenCode، رقیب رایگان Claude Code
☀️
⭐️
توی این ویدئو: 1- با همدیگه OpenCode رو نصب می‌کنیم(کاملا رایگانه امکاناتش و اوپن سورسه) 2- طرز استفاده ازش رو یاد میگیریم و بهتون میگم کجاها خوبه ازش استفاده کنید 3- یه چیز مسخره با میمو می‌نویسیم(توی ویدئوی…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5037" target="_blank">📅 18:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5036">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E1ja55tUwhWK8wg5epb-0LQb3GWewxeecTKd8DkiM3qe5nsoMYbumTfejdoTa6bmuCQFEoYYVyKvqIDd2NJM4P3lrp1V0sjfmdtqLHd0VCPJ2KBcDlVTEtDhEEBd2ddBpgInxRfmbXk677iXdQa0lXeHYRzDeO2v9RGsTFnkaLNVZDYQZpibNsJM4_oHYmWNya2gTb4b7GFoX6P0tFmbAr39mWlVfj-Z0xTJsPPnIR5J6lt9-ZlJzwNuA_Xsio5GLBzC1MRd5VIp-oSkWW6laBKU6DATy3YzIM72J2jLhR-1EuRcJjsWr3hPPWoAfxEvmwI5ijb2i63zC_hSW9vhaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش OpenCode، رقیب رایگان Claude Code
☀️
⭐️
توی این ویدئو:
1- با همدیگه OpenCode رو نصب می‌کنیم(کاملا رایگانه امکاناتش و اوپن سورسه)
2- طرز استفاده ازش رو یاد میگیریم و بهتون میگم کجاها خوبه ازش استفاده کنید
3- یه چیز مسخره با میمو می‌نویسیم(توی ویدئوی بعدی که پشت این میاد فردا، قراره حسابی ارتقاش بدیم)
4- آخر ویدئو هم توی ثانیه‌های آخر یه چیز جادویی هست. اولین نفر برید ببینیدش
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به هیچ دانش شبکه یا کامپیوتری نداره
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/5036" target="_blank">📅 17:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5035">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">تموم نشو x alpha
💔</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5035" target="_blank">📅 17:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5034">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">تموم نشو x alpha
💔</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5034" target="_blank">📅 17:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5033">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">آموزش مدل‌های AI روی کتاب‌های کپی‌رایت‌دار؛ قانونی یا نه؟
خبر:
اکثر نویسنده‌ها بدون اطلاع و رضایت خودشون عملاً توی ساخت همین ابزارهایی که شغلشون رو تهدید می‌کنه سهیم شدن. TechCrunch یه تحلیل مفصل نوشته که چرا قضیه از نظر حقوقی خیلی پیچیده‌تر از یه «دزدی!» ساده‌ست و Fair Use وسط این ماجراجویی نقش تعیین‌کننده‌ای داره
🔗
https://techcrunch.com/2026/08/23/is-it-legal-to-train-ai-models-on-copyrighted-books-its-complicated/
نظر من اینه که حتی کاری هم از دستشون بر بیاد که انجام بدن، دیگه به چه درد میخوره
😂
مثلا فکر کردن OpenAI یا علی‌بابا با Qwen که خودش دزدی و دیستیلیشن از کلاد هست(
🤣
) و... تره خورد می‌کنن واسشون؟ =)) یا مثلا میان بگن آقا بیا این قسمت از کتاب شما رو قیچی کردیم از LLM چند تریلیون پارامتریمون؟</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/5033" target="_blank">📅 02:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5032">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">خب انگار قسمت نبود
👍</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/5032" target="_blank">📅 01:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5031">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">یه ویدئو داریم واسه Open Code
داخلش یه پلنر ساده می‌نویسیم با Mimo
توی ویدئوی بعدی که پشت سرش میاد، میدم به X Alpha و اصلا یه چیز عجیب غریبی زد.
موندم که واقعا این مدل مال کیه</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/5031" target="_blank">📅 23:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5030">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/5030" target="_blank">📅 20:17 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5029">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">دلار 200 رو هم رد کرد
ولی نکته‌ی دردناک اینجاست که هرچی جنس می‌خریدیم تا الان با دلار بالای 200 بوده قیمتش
الان قراره حتی بدتر هم بشه</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5029" target="_blank">📅 20:16 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5028">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iVmreBxqWSVZ-oIUfxLc1tcpO6pZWpw2vxYXiPmdpkcQIzdoDUJlBguNrKnemK6o94QJbNpXd3MgIxfX1GIYX7ac4VvNWS0D1g6AJZCo_0vE_0e2UbbMUd4NsZEmMIoc1SXnIsOtrphAu-Ry8u5g-MHtapQTl6zPdJX6trZZ6IKwykP6o-L2jX5d5xUpmr3PicF3Xh4OVvcT2AxkZk5MI-Su-x5CoM2MDII-K3GF1OwLQSxbZixMcMma6sTJFguaglilqtYwSgdiEgG2f8axYeTHkP2qvTriSiMiVyiTaPan7IxTSlTD_oGKsTCmXyuc9UCwZ5bVb1z1Ro8_ufBa6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسیدم ۲۰۰۰
تا الان ۳۰۰ هزارتا امتیاز
دو برابر بشه میفتیم زیر ۱۰۰۰
❤️</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5028" target="_blank">📅 19:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5026">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hMuV5W8Da5yLLdAun28PAcEANBIuCfIjIey98tkR-QQLsBd5f_TbQLoBDEp69HmGgv5MmfxHqN8oQz_cceUB-YMTIALnbY6R_cEjshnuTTuLAGB9SZVirgTiDN_nlqOb6fbqSSwue5Fb4ev9pdTN47rQybbNYSyBV6RxRsAELdVBIiECsrXhX8E2BNGAugD5zB4t2aNiCgBGck6c-Gu3MI35fV0gwn41IUAA69HcjXlLo2Ogn0QWOsxFW7W_zpYR-2kf6Xad1VbO7feEDDrsRPwTXRX3zCHbit4qyzJq-NKzL2yz_Tq0n5ygxB50ivi69j-lXrdG92Lwcsuenxe0zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JdRwQ0v-bsB-fw71r2qN13bCu_aa-nUt2ie_J7wjT04I4OtmqF6bCoBnDN7bgoT9AHT9R75Y_28WbZ8cgCIRK1KC6nCuCnJc8o1UpZSbI4DpMNWUFw832icz3ldJppllo0sy2raknGlru3R8JYOq1UrGXemwcHFM6x6obrFu1Jhf1RJk4yOVER9FjXtC887ZaFJFhwRoCYlxo_98xDGGJveD-uLaXbgG8c4MgMNfAMVoQk3_mHPtFTgKBUGryaQDijx80Iz-haBr083qsjtonH8ftFkFieXi6U5C-QuZGG9yJTry4CrlnMN1yKCFSXn4HBL2gejh-g_a0AGqzI5TTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه چیزی دیدم تازگی ترند شده توی توییتر، یاد همستر افتادم
😂
😭
گویا اسمش ووچ(VOUCH) هست و طبق گفته‌ی دوستان کریپتویی، یه کمپین پولساز هستش و فقط هم یه روز ازش مونده.
اگر که تونستم جزو 1000 نفر اول بشم و جایزه‌اش رو بگیرم، یه اشتراک Claude Max میگیریم و روی استریم میریم میفتیم به جون ایده‌هایی که می‌دید. بازی سه بعدی چرت و پرت هم می‌سازیم
😂
فکر می‌کنم نهایتا 5-6 دقیقه زمان ببره انجام دادن این کارها واسه‌تون اما اگر که انجام دادید، هم به من ووچ میده هم به شما:
الف- برید توی سایت
commonsmade.com/vouch
و روی Claim With X بزنید
ب- جوین که شدید بعدش روی پروفایلتون رو بزنید. اینجا باید دوتا کار بکنید:
1- گیتهابتون رو وصل کنید
( گیتهاب ندارید هم راحت بزنید Continue with google )
2- مجددا توی همون بخش پروفایل، یه جای کد تخفیف داره به اسم gift code. کلیک میکنید روش و کد "love" رو میزنید، باعث میشه ضریب 2 بده بهتون.
بعدش بالا، سمت راست صفحه براتون 7 تا قلب ووچ میاد و میتونید به دیگران به شکل زیر ووچ بدید توی توییتر:
Hey @commonsmade, vouch @MatinSenPai
زیر این توییت من می‌تونید همین جمله بالا رو بنویسید:
https://x.com/MatinSenPai/status/2091522197537919325</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5026" target="_blank">📅 17:17 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5025">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DviahiErhkSDAqLINsyE_JF4AyJlALODL71C7cwKpUJlb6zFHOtKVMfTHEZjN3vT5FggmLR-_wOY-hgTdQLUDT4sQ7c7wDN1r5kGxypqZi5-EYBVavwrRNWJSZwF94qBOvDIX62NBd3fyADh8GCOs2o59WIi8-QcG6dmNat7maMllbmJ9TzMqHcDaXcjGK-u0QtXyPVWOgM5_IssOVnJIrqgZcdMdgpYB6yECgbwXMDQLOKVLpDIHVuertoP668Lj3CpiqxG5qBsyiYAXDMd2hy33p7qEZhRxbTLcwmAok8r1XRDaVo2S3uiLkpzwPQn93Lrjds3tBseIWiWN-V61g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به خدا چند ساعت خوابیدما دلار کی شد ۱۹۷</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5025" target="_blank">📅 16:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5024">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1357719d90.webm?token=ia8LhhkDtBRlCG9diaEnOqvee5WmzvsNEAV1fLGyH2R181E5SYx8lugPTyRUCARTXQZF5Xdk27moyJS3cS9IMJ22Kgz0MXohC61l_Duyzk76-FjT3_VN_DzYNv8AdLUiqKpRHU5RcgcQ3qBmox4obcIjIoE8h-iS_opnNKdJGKvu_NHbaJcmWoPtgfWjrLjsqWVtyc4-qVcYN7V6t4dr7PjUQUIr5_f6FvLm_ZGQGSCPHf9cqMhfTNxi2RT07nynZdnE245_BpXTeHe3J5WSC7kZ3b9Kl63Cx_bqJ0fKQDjTZP2Xi_j0kQVJUvI7OFS6daWRcc4Xr7WYcr7xjAO3Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1357719d90.webm?token=ia8LhhkDtBRlCG9diaEnOqvee5WmzvsNEAV1fLGyH2R181E5SYx8lugPTyRUCARTXQZF5Xdk27moyJS3cS9IMJ22Kgz0MXohC61l_Duyzk76-FjT3_VN_DzYNv8AdLUiqKpRHU5RcgcQ3qBmox4obcIjIoE8h-iS_opnNKdJGKvu_NHbaJcmWoPtgfWjrLjsqWVtyc4-qVcYN7V6t4dr7PjUQUIr5_f6FvLm_ZGQGSCPHf9cqMhfTNxi2RT07nynZdnE245_BpXTeHe3J5WSC7kZ3b9Kl63Cx_bqJ0fKQDjTZP2Xi_j0kQVJUvI7OFS6daWRcc4Xr7WYcr7xjAO3Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5024" target="_blank">📅 16:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5023">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">به خدا چند ساعت خوابیدما
دلار کی شد ۱۹۷</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5023" target="_blank">📅 16:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5022">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">حدودا 20 روز هست که دارم با ابزارهای مختلف و AIهای مختلف کار می‌کنم و خودم رو آپدیت می‌کنم و چیزهای جدید یاد می‌گیرم، و ویدئوی جدیدی ندادم در مورد AIها تا هم دانشم بیشتر بشه هم محتوا باکیفیت‌تر. اما طی روزهای آینده، کلی ویدئوی جدید راجب تجربیات این بیست روزم می‌سازم و می‌ذارم توی کانال.
(آرک سولو لولینگ مخفی به پایان رسید
✨
)</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/5022" target="_blank">📅 06:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5020">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CkHeMovUGGDb8_Jffg1672YrMUeculs-83CCw_-k19XBTqGuRrpHVUKJJ3Quzf1WndIeLoZAocwFCiV1lavZNZBzGlnQoKZDLk6JeGd_xByDZvgGs5XwFT61TjKGnPGjOMuKe2EWb3z7JK8EV5L3HvfFziJ7APW8SF5i35IF1zG3H8E_z9FcxXgWyIYo0aRWJTsrVzZdsHBK4jexz2s3u70i-A0BJNby0kmatFvx3Qc11W8Ewx7vkLv9xxKl2Q3l8EM34npg0GWE0ODo1Kpg3u818rzBxv6u3gXI81jIrRanoxwe88FBz90z0_YbfQr0nbTpXXHipNqLOi2zC44quw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PsouvBnvDFN_A0jR1QJAhjQ-qYVZbwExs5O2hXJ5oPkAcBF-IcFl1kyuuz3MSrZ7SWiEx5xaeD6bUK84BapjW_poQk4_Jpl2fYlbrBJ7oMdM6ZECuXN2xEQZHkndT1SFkTBX92Q3x0c9Hv8BX88e0OjGLk2MKkAQQnCGpAgDK8L2P3pb1U8qxkAxhXUqwhQB0d5FQE5r3jbUZ7BP1QH9Pdack1-t3cIsM1xdJ7DG7w0XnhbJxmWNbvWwAFoaittuaPzbFJwpvaqcynPgQL0PtFZTnm2n8UouWSsyA_CQShheTbDn-BB_pJun81AUeAjDt6V_arT86rlVhkWtBjww-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خیلی خوشحال شدم امشب از پیام‌های محبت‌آمیزتون و از اینکه آموزش‌ها چقدر کاربردی بوده واستون
❤️</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/5020" target="_blank">📅 05:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5019">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LM9q-16XCJlTGEKw52auWE0oXD2HlVcjUxnSimONhBzfN-izbigNRPDc6zWWNHSjAcNQ4AKqcUrJ7arVBIernV5RFS2R7_Yd32CiPjvXMIjqwQ1zrFVFpuGTnfe5unVWoxTJO0_626hfwcECUFQrEnOhBcZnit6l3HHrnX49O-sidw6x-EZkaLbvuzMiTGX2TSLAC1oLCBy77sHOK7sGQEYux0oZHi5p1-wxyYvA0UKhFCjkNQfaiNzwpBM9jV5Zlb_F1FXA8qEse1nD4kH6-Oj5c4eorT-zRj2F0RbeRt-0t1e1PB5440CoSSZaTodpIKueBaKwehMf3vEoQJvUXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم یا مدل جدید شیائومی Mimo هست یا به قول یکی از بچه‌های توییتر مدل جدید خود Google(جمنای ۳.۵ پرو). گوگل هم ماشالا ید طولایی داره توی این ناشناس مدل ریلیز کردنه
😂
خواهیم دید چه خواهد شد اما تا الان خیلی خفن بوده</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/5019" target="_blank">📅 17:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5018">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خیلی توی کامیونیتی خارجی بحث و جدل شده سر اینکه حدس بزنن این مدل جدیده مال کدوم شرکته، چینیه یا آمریکایی و OpenCode هم اعلام کرده که دسترسی بهش نامحدود هستش تا هفته‌ی آینده و روزی 100 تریلیون توکن تمام کاربرا می‌تونن استفاده کنن مجموعا و ظرفیتشو دارن
😂
همینطور…</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/5018" target="_blank">📅 16:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5017">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">خب من این آفر سه ماهه رایگان اسپاتیفای رو تونستم بگیرم با همین روشی که اینجا یاد دادم  مزیت بسیار بسیار بزرگی که داره اینه که میشه به گوگل پلی وصلش کرد و عملا توی هـــر بازی‌ای خرید کرد. البته من با VPN آمریکا chain شده رفتم که ساخت این رو هم یاد میدم بهتون…</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/5017" target="_blank">📅 08:23 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5015">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/p_-g5BDK_S_NQ7rSn9qRIqI4UpDDBZnp86oYU9sQhb8S1oA73AHWaOnJq2S6_btNCf6jPFbF5QPrfjj_rl88AIGmPYdZr7uY6W0VqkVr1Df5n6ItfdWoM64BiIPYgw6-Q0OMp_SM1AZvVGuYWaqGAxssrtGSfcj9Rm41Y9PtBhSlSvp-KxwXcxdyATgqO1vNJLKV_s3H2CjPu5M6u-ospU4dtcjnrHax1ZIQlf5BZo3np0QRvTuoNMYr5SqiiHB-896QOHAUSXD3bwJIlnSLHXdOphhJdRIB4xkfmGDd3fQ45noBeG6WA7QkYgi3-vCf2kMPsIRTvcHJPsQOLyFJkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VaVPg79Mkz8L6a0_TgvwpLpfE8tZcVdZfGYJ2-NOhBJYtNbwE7PdeCXiDa6kNvEhz_Ysw7YIxO2dvDQxP1fxyGroZQe99vq9BoOraXjY6Adouzsl_lQAIOXBNUhRKFHAJNf2lDBerEUUo4ll0y8g3fNKEUZAyJX_gzloVQym_R6hDIvXU4cupYO7ibimMrjvIdG3SLc6TsGs9MUDrh2zZNs43_3BHvMzDwXdqyXiHs-FD2g0KdLmvAKsrKVGmRaZYLuU0UT_S193zfgJi7topPTj6z7KvfydyWCFEYsbUD9lgQWhfI5FqBzUiZoCn96LQutIbxEAaZvwWGPnbNFABQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب من این آفر سه ماهه رایگان اسپاتیفای رو تونستم بگیرم
با همین روشی که اینجا یاد دادم
مزیت بسیار بسیار بزرگی که داره اینه که میشه به گوگل پلی وصلش کرد و عملا توی هـــر بازی‌ای خرید کرد. البته من با VPN آمریکا chain شده رفتم که ساخت این رو هم یاد میدم بهتون
تا الان اینها رو تونستم بگیرم باهاش:
1- اشتراک ChatGPT(بیست دلاری)
2- توی کلش رویال کلی آفر گرفتم(رایگان)
3- توییتر پریمیوم(فکر کنم ۹ دلار ماهانه بودش)
4- پلن رایگان Hermes Nous Research
5- همه‌ی پرداخت‌های گوگل پلی(با آیپی آمریکا زدم. و یه سری آفرها رایگان)
6- اشتراک OpenCode Go(5 دلار)
7- آفر سه ماهه رایگان اسپاتیفای پریمیوم(با گوگل پلی. هزینه یه ماه بعدش رو هم کم کرد یعنی ماهی ۳ دلار. حواستون باشه)
و در کل اکثر جاها میشد خرید کرد، تنها چیزی که نشد بگیرم آفر رایگان GPT بود که انگار واسه‌ی خیلیا خارج از کشور هم قبول نمیکنه کلا.
و مجددا همینجا آموزشش و مابقی مزایا و معایبش رو گفتم:
https://t.me/MatinSenPaii/4917</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/MatinSenPaii/5015" target="_blank">📅 08:20 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5014">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gEaJBcNnU6CkCJm8HePKs4hrVHextGF8W-nBXqaCh-XvhU3X3WDmHO7aRMOb2QYj1Iqjkn6OVl6gqtyCenNm-pOYSsVEgYV1muAGuzjPkOSVtJghNz_-yFP1BAPKIH34ELycDDDhpSnfVCU4wry4UKDx0HSZBkKsUSvtfU7eNQz4Z978vgSVLES1GuAxLDfEJZKesSuVHJKRkTHyNs8YiBWmpMjtfv2XqQnOB08QsrwdtiSjAmlyLF7go1k_c_Gov9-ucEkgqes14D-HQft4Q9XDtH0szLUVvc0vrQjjyi58XVeyJQ0LQdblNe0iQ-mmJNbqwNudr3JZy_gbkgM8JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل جدید و مرموز x alpha که روی اوپن کد اومده به تازگی رو می‌تونید این شکلی تست کنید روی 9router: https://x.com/MatinSenPai/status/2090856359117902053</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/5014" target="_blank">📅 08:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5013">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">فکر کنم وقتشه کم کم یه لیست از چیز میزای رایگان و آفر و... هایی که با این سایت تونستم بگیرم بذارم</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5013" target="_blank">📅 07:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5012">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/msDSWrXHAjft41-07yS8_ctFSM78_4GqRwoG3kpH3zBozWN9SqCWrISPy5qHs3JvU_pZ-9JUleFVlJMUTqZkNlCIx7RLphbmoAhoNrZX9HdpGNcayLVRXKPyv9hlOWhj7Yxw-t049MhnN14bUzP4JgnAIm4Oa-LjDx3pRliNWvNlrzkhO9AYK7GyWQbmJM02RFtocVV6AXoEZP0XALbnQL46R-13sGg7e5oJ12CgK7D52VJPPlfyEHLYSWnKgRJGNRC0qwHvSBsKe54rzWBMKR7PfaDf7DrGsc4wzZVC231iWLieTYCKwpGg4PIFPnzqD1jo7WuJOfLqWkNU1lZdgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سریا هم یه جوری شبیه دی‌کاپریو میگن «اوه این پروژه وایب‌کد شده» انگار مچ معلم مدرسه‌شون رو وقتی دستش توی دماغش بوده گرفتن.
همونقد معصومانه و مهدکودکی</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5012" target="_blank">📅 07:39 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5011">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">مدل جدید و مرموز x alpha که روی اوپن کد اومده به تازگی رو می‌تونید این شکلی تست کنید روی 9router:
https://x.com/MatinSenPai/status/2090856359117902053</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5011" target="_blank">📅 23:07 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5010">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ehJKk1Ow3eCUwNj_vSf3N5vvO5JmfMwOGGyacriMjf7uKftxMqpPerTT-mDhUXHlbE-tDoAUzLD9pI96A1kQ3KBBy84zNtJQffx6tVRpasrkkHFfSyDQUC5i0MjIDu4QbhXQqBEHoKhpek9vSYGtlRfY9lpUs0Yrj8aknORPJ5CNSYi_ubgLcv0YJsCSQ0gzyfle7e4VBnAHmXjsMuvyINKlSnNfUVk9HvEBVPgApyo1RJXct-M4_Wfv-26TI3sU4ZA9LTv7oJtyYOdHvCwlQRUgYPT2sLAenAIZuseNdnHpn6l1C7PptElYKns-e4HdKChZLksLFmWZiXbfOp2MeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔗
WhiteAesther Android ورژن جدید
🔥
🔥
🔥
🔥
🔥
نسخه ۱.۲.۱ — رفع سه مشکل اتصال
این نسخه قابلیت بزرگ جدیدی نداره؛ سه تا مشکل رو رفع می‌کنه که باعث می‌شد اپ روی خیلی از گوشی‌ها اصلاً وصل نشه. اگه ۱.۲.۰ داری حتماً آپدیت کن.
🛠
چی رفع شد
1
.پروتکل های wireguard و warp in warp برای خیلی از دوستان اصلاً وصل نمی‌شدن
توی ۱.۲.۰ «ثبت‌نام مشترک بین پروتکل‌ها» رو به‌عنوان یک بهبود اعلام کردیم. اون کار اشتباه بود: وقتی MASQUE هویت رو ثبت می‌کرد، کلید WireGuard روی سرور Cloudflare پاک می‌شد. بعدش هیچ اندپوینتی جواب نمی‌داد و اپ می‌گفت شبکه بسته‌ست — در حالی که مشکل از هویت بود، نه از شبکه.
حالا هر پروتکل هویت خودش رو داره. اگه از ۱.۲.۰ آپدیت کنی حسابت از دست نمی‌ره.
⚠️
در عوض، اون کاهش سه‌برابری احتمال rate limit هم برگشت. اگه زیاد نصب و حذف می‌کنی، حتماً از
Settings ← Identity & access
یک بار بکاپ هویت بگیر.
۲
. عوض کردن پروتکل وسط اتصال، همه‌چیز رو خراب می‌کرد
اگه بدون قطع کردن اتصال پروتکل رو عوض می‌کردی، جستجوی اندپوینت از داخل همون تونل قبلی رد می‌شد — یعنی هزاران درخواست دقیقاً به جایی می‌رفت که قرار بود جایگزینش کنه. نتیجه: هیچی وصل نمی‌شد.
۳
. گیر کردن روی پروتکلی که شبکه‌ات بسته
پیش‌فرض قبلی H3 بود که روی UDP کار می‌کنه. اگه شبکه UDP رو بسته بود تلاش اول شکست می‌خورد و اپ دوباره همون رو امتحان می‌کرد. تا نوبت MASQUE H2 برسه چهار دقیقه و نیم گذشته بود، و عملاً هیچ‌کس این‌قدر صبر نمی‌کنه.
✨
چی جدیده
حالت Automatic — از
Routes ← Manual ← Protocol
گزینه اول حالا Automatic هست و پیش‌فرض هم شده. خودش سریع امتحان می‌کنه ببینه شبکه‌ات چی رو اجازه می‌ده، از H2 شروع می‌کنه (چون TCP روی پورت ۴۴۳ هست و شبیه HTTPS معمولی دیده می‌شه)، و هرچی جواب داد رو یادش می‌مونه تا دفعه بعد از همون شروع کنه.
روی نصب تازه: ۱۴ ثانیه تا اتصال، جایی که قبلاً چند دقیقه طول می‌کشید.
گزارش خطای واقعی — قبلاً اگه جستجو نتیجه نمی‌داد فقط می‌نوشت «اندپوینتی پیدا نشد». حالا می‌گه چرا: بسته‌ها از گوشی خارج شدن و جوابی نیومد (مشکل از شبکه‌ست)، یا اصلاً خارج نشدن (مشکل از مسیریابی خود گوشیه). لاگ خود موتور تونل هم از این نسخه داخل
Settings ← Diagnostics
هست — اگه مشکلی خوردی همون گزارش رو بفرست.
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5010" target="_blank">📅 21:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5008">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jZr1BpSk8ACktJfIfRYuIsZYm6MT1qYGan6Vw1wj9rbIvj13TSuahYkcVhPmyH_vTnlYiXNa1m7D6V8V81N5iTPXzVKr5KeSaidbQhwejPg29RZwgAcswCHoBCl4CBsbG8Z2JM828x_3tY6tJQneGeIu1Y6IGFkMBgL2DH6NB4G5kfst-N1tmQ10IWq8cYtRnuh9X5BAhEZ0TK1C9vK5-2QqZrqd1f58HHIvZRUNaTkLpApd0JTi1HKuo5YMkBFUQGKsZYk5uKfGUtzJu6aDvAxk5vDX6VKrbbbXD5WeJUJAT_Jqfqeob82GQRpgQeYCxePnRS4AhDU65x4GEWTayQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VzOGDLSuT0Qsvj39ovo6lWOv_s2mwbu8GPmlS58Pxkxt4kmKdBaemRoM4nmbLlAe138nSpYBJ3W8XtAlTWYsfuNAQaCxF8q35U87fn-15hJpgKXWON4XVaHuOAt3PPDCqs7C57Ym76aJBOQKQrC4U-rjM-nJR4seg6YthfBLEAnWOycOQh1dBR6gHBh4a3pD_4EcyqpBrxmQfR7se3lvI4hiDVXoQVZW6_4vBBHWr8WOUjO0wLq9c0UyZSHY6qf7TN04sfH0kWmkwNbnSwAHF5ejvYu9-Ny0wU6vXc7DY1FTQDd31FBjfpwj5RWK1C6EmP17MpZZ2FuO8Yzi7-44TQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  چند تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5008" target="_blank">📅 15:11 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5007">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد
PattNG
کرده و لذت ببرید !
https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt
ساب هر ۲۴ ساعت آپدیت میشود.
///
توضیحات:
چند تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری و تست میکنند و سپس کانفیگهای سالم را فیلتر و در اختیار قرار میدهند پروژه‌ها‌ی
https://github.com/0xRadikal/Free-v2ray-Configs
و
https://github.com/itsyebekhe/PSG
و
https://github.com/Delta-Kronecker/V2ray-Config
هستند.
اما این پروژه‌ها دو مشکل اساسی دارند، اول اینکه تست کانفیگها باید از طریق اینترنت و فایروال ایران انجام شود ولی در حال حاضر تست کانفیگها در این پروژه‌ها از طریق گیتهاب انجام میشود، دوم اینکه روی نت‌های آپلود محدود (ایرانسل و ...) عملا اکثر کانفیگهای این پروژه‌ها آپلود محدود هستند و کیفیت بسیار پایینی دارند.
از آنجا که با روشهای زیادی میتوان محدودیت آپلود را روی کلودفلر دور زد، من در پروژه‌ی خودم اومدم کانفیگهای کلودفلر سالم را از پروژه‌ها‌ی اصلی جدا کردم و تغییراتی را برای دور زدن محدودیت آپلود (و همچنین دور زدن فیلتر دامنه) اعمال کردم (در حال حاضر متد fragment+fingerprint اعمال شده). بنابراین کانفیگهای نهایی سالم و با حداکثر سرعت در تمامی نتها قابل استفاده هستند.
برای دور زدن محدودیت آپلود در نتهای آپلود محدود در حال حاضر فقط باید از کلاینت
PattNG
استفاده کنید، بزودی در سایر کلاینتها نیز این مورد پشتیبانی میشود.
https://github.com/patterniha/Free-Configs</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/5007" target="_blank">📅 15:09 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5006">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jIgenidI2ckLI-zATuQlIV7_B_GKzhJ56OzlkWTSdRc2Fctblh5VqvnaPThRBso_icIGEWtxgT8kMbEijw_6lBfU9AL_fd8rf2-DQ2wDp-rHkiHwRD0ltkyUivVAmmS88AxXRieIyLuvD7okDczK6M-f04ElwyTIYFlCEr-1RgpL1xXWnyI5_rkt9LBzBLiC6KsAkQQw7-ZKiBAFmtCiZKw_bJvQDiguxEtZE6T_qwsptfHeNnsP3GKqtDam5YnDiRB9_zUSFYLMLarP0w7nAEKxEuDfOkrEounWriYqwWTv8TW6pQ1diJTOd2pjaQnMgLSa_RC_z31bzHixcqh9eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه مقایسه‌ای دارم انجام میدم</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/5006" target="_blank">📅 03:19 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5005">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">آقا این Muse Spark هم عجب چیزیه:) روی هارنس درست به نظرم شاهکار میکنه. فعلا روی OpenCode به شدت سریع و اوکیه</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/5005" target="_blank">📅 03:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5004">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بیاید بریم Rust یاد بگیریم لایو هستیم روی
🟩
: https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/5004" target="_blank">📅 21:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5003">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">بچه ها بازی Rust نه. زبان Rust:))</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/MatinSenPaii/5003" target="_blank">📅 19:11 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5002">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">بیاید بریم Rust یاد بگیریم
لایو هستیم روی
🟩
:
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/MatinSenPaii/5002" target="_blank">📅 19:05 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5001">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">آپدیت جدید Aether:
توی این آپدیت روی مسیریابی (روتینگ) و اتصال از پشت پروکسی کار شده</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/MatinSenPaii/5001" target="_blank">📅 03:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4999">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">هوش مصنوعی و برنامه نویسی | آینده این شغل
لایو هستیم روی کیک:
🟩
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/4999" target="_blank">📅 21:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4998">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">حس می‌کنم شدم هوش طبیعی متین سنپای که پول توکنش رو نمیده
😂</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/4998" target="_blank">📅 20:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4997">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بچه‌ها شرمنده می‌کنید با استار هایی که میزنید. ممنونم
❤️</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/MatinSenPaii/4997" target="_blank">📅 20:44 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4996">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_efHV3GKa3unCXKdV675K6Vbn01kyx0uh-mMTsEKIsKw0XWcrz5CPVa8BGOqB3aob7NmEJH9cau44w98pxdK4-QDzJA6LY4X89CZWIoRvnGW2X_PY9cmoOti3utpnyvIzAHdfPU6VdoISarAP75a4AKTpRi1YzaJ1TSkplUw_M5hc5Gaa4I092Mi1SOqqM3Ukqig3FweYhY-6Sa297ltLYUUwns24TmlB2ZDVRoMcnFft08V9o63c9TeKLsQz52pPPVdm4us6hFX1N5mgAhZsMCtLAkqiO0aWFIysUzt1OJaJplK4Zu_2HWvKQrrx5bkKhpqPU7aGfHJvAoFZhDUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نصب هرمس وب یوآی با یک کلیک
متین سنپای
بهم گفت که Hermes WebUi نصبش سخته و بهتره با یک کلیک بشه نصبش کرد برای همین روی پروژه اصلی PR زدم که اگر تایید بشه از این به بعد میتونید راحت این پنل رو نصب کنید و ازش استفاده کنید.
لینک PR:
https://github.com/nesquena/hermes-webui/pull/7152
میتونید روش ری اکت بدید شاید تاثیری داشته باشه.
اگر هم تایید نکردن مهم نیست
یک پروژه جدید روی گیت هاب خودم اوردم بالا
لینک پروژه:
https://github.com/nesquena/hermes-webui
میتونید به هرمس بدید و بگید براتون نصبش کنه
خیلی ساده همون پروژه اصلی رو میاد براتون نصب میکنه
حس می‌کنم شدم هوش طبیعی متین سنپای که پول توکنش رو نمیده
😂</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/MatinSenPaii/4996" target="_blank">📅 20:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4994">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/g4S90Faf0dMkSs-rmy22v4_65ts2lEAnmVOLarU8L29R_EsKHRumyH1-1rCMUfKErDBUJwqziFf5N1eyrAsSLBn1-na6ep4aMxT8uGSiGTnYAt3Z32LmuJXyO9frWnnLSntb_3MJFk0u51pgbt6M2yrozL5hnuZdUj2yHAEZ80V-zmhYK6LhvjwbCMFYddcweNw09htbJZ3z5sEg5ODFBDiSLy33X4wpBTD3J80gkeJGwHtIc7zNOAt-q6pymeSJHW5uSuvCCcWjY52cLKq_UP1VrOTBjyQJgC2EfM4SsOklHQ_U7XDC73Knp7ntSV4wRFuNr2YvbCtkAj8JZcm-pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DLEGvMa5rPFxepLdleNFaDAcXqr-u-OoDuXHq_6vUbQTU8m5FamfkDq0GLUj3EHTd9Hfv_VReZ0xInfdWtBqKhV53UmUKBY6J6Cubba-PtR9Tav_mpKMk6rVI7s_KMjhC8AAr2P8urlJ4NAOoA5eH4SdrduZNT3HF6NXQdtgX7mAm4HrqO5qHG3CXS0MeebzmEbKSoHWViH0EsRXRy2sJn6vl1lfi6VbYXhzmCnnQQTCx2qZD7kQnhAohnl6bwSyY0SnacTmEDd0Jhus9QQMG1t1__ONCge8klG9oUegcJkRxqCaTeNt-jW1dOKRSVwLOKuCWTuBM9jo1oU1T4-H1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/4994" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4993">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ggPKZcdFUne8_awF812uGETv6R0Z-7AIg1kOXWuAynmcoBYSrBiqwmF4IfQO5NQjL3I7vvQnukgxAvxvPVfeqPOOYMJqzEJHl-HY79bXNI-ZYGSVHsCX1c4kkdxVJPpE2pidd0sj-RQux0sF7EdemQCMI6fNP06wp__NuOdx9GeTDxYPafe603K_PSj_A5bKCWn1Sc0kqDQa6e2kIgJQcUB-0rggppypLZKO6K3YAAphKQBDGLU-Y1k2uZdpkNf9IxXgeRkuyFpHVD8qGl1TgAlWw4eg8rABtCjZ6Zng6s0qQHTi6XtfkH7IMkH7b-Dq1ug38AtwPzuNcUdgmXfOpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرویس استریم شخصی هم نوشتم واسه خودم که با نت داخلی بیام روی Kick
(تانل rathole
😂
)
هاهاها
به من خندیدین؟
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/4993" target="_blank">📅 08:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4992">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qiew1J0xiJd2xt-QmWGc_IX-HfLlNx2hcLquZ9UrOCx6BCVUMHSOwuFOMsDLpPMnEtmGJb6fEfPnxul04n2Nh2n5jzRO3ZdBBFTozYQ94CY434dw5kaEyHuXutOe06IuGiBkRSnDIivVRGiiv2w3FzFgXi-m7uOazpsAyTJWFYVEzGveol5Z-5jN-XcLpf_1G0ueM5ghrUTaba1UsbuCHzaCzwOQ0V0DSZoAfP-tW8obKZ_kPiRGjvfLkdPZr8sdWmAQSgRzlvPxcq7OER3gc9SN1JvA7L7CJMRVgsSmps6cVTpDk5QHlEsNxnfICVFBeGeWnON0ZTqg7nFkL7XB2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجربه من از 5 روز کار با OpenCode Go
https://x.com/MatinSenPai/status/2089928470801318139?s=20</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/4992" target="_blank">📅 07:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4991">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/edbpIpV_mNaiD_pMEQQUQ0ExwO_XMR1nJOPZ_wOAAACGPBN1GqnSVDwwq9DqEkvTWLjmm8Fjy27Vpu3PRLOyQSP9o_7muNbnxEmHwXDiTktNG1HEYa_h6yzdaSmqvUYJPBBhVygjith6CH-oF9oMLdrh7-KJm5y6q2ALZxzZmkWwnXUXcL_6jIQpcXEWZrHeSLIj2csZmbbiSTNflLr7R5V23sK8Q1hab3DIV0qljzvdvv6v9WUVgwy0yHxZBFS0iNvQjGo36kT2jCn2pEcg18EIpHzxvg5SVPgSzUBt2VUzDCKEjHGK7w_DV1S8s8InPkRRbfcIFE0hJ_SYXZ0gug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب پنل BPB + متد پترنیها + Chain Proxy داره بهم سرعت آپلود خوبی روی آیپی ثابت میده</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/4991" target="_blank">📅 23:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4990">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">لینک داشبورد کلودفلر:
dash.cloudflare.com
لینک ویزارد تحت وب BPB جهت راه‌اندازی:
https://wizard.bpb-panel.workers.dev/</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/MatinSenPaii/4990" target="_blank">📅 20:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4989">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jPu_0k5wOLzG5NBssqgqMxTJwHkdYszIY2kcUwInMHY4daVajyYFiLdNVj4I0iBA5hhRYPV_0BLSmNqP-ZFZD1AciUDe6dMlEms2QQOd69MaTmTJWkBDxJmD40qLHE_CYWKx226DD1p7KEj5dw4HeZ1E88YVuQibAowq5U4MOZi7bb4_W0ZD-HjUvyM1yxKaqCG_9M6y_vnJ4lfYdrrt3nQTNK6RPpdTxyFUjO697h5Jvt1iatpB7VFmUH6BTpw1PSpZvqMfef3sROgF8ZGURD9tr-EnIBf8JbYmFURN9cuiYFjN4XXcJdJT7KA_NFzOlF4hbRDTbh7QjlbrsTLB0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
ساخت VPN رایگان بدون سرور با پنل BPB! ورژن 5
🌊
⚡️
لینک‌های استفاده شده توی ویدئو:
https://t.me/MatinSenPaii/4990
⭐️
توی این ویدئو بهتون یاد میدم که:
1- چطوری با پنل BPB برای خودتون VPN رایگان بسازید
2- روی گوشی و سیستم چطوری ستاپش کنید
3- و برای خودتون و خانوادتون، از یه VPN امن استفاده کنید
ویدئوی آموزش تنظیمات:
https://youtu.be/7G9Fjhe_NxM
ویدئوی بالا بردن سرعت آپلود:
https://youtu.be/dQKfkXnThCE
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/MatinSenPaii/4989" target="_blank">📅 20:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4988">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ویدئوی BPB دیرتر میرسه و می‌تونید اداره برق رو سرزنش کنید
😭
😭</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/4988" target="_blank">📅 19:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4987">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AeQBIwKqltvFWiYUc_Il1Da8QOaAfiihlE4roo31scARkbmGwQAQ3XepuVXte4_z0SpTAA0_VoFR_dmMs45qsULyXC36HhYF985UfLWAcPsUCDbp6sJrVWkYFNjchf58H4Xm0Olcn_UCShof0hd4fLBFX_kMj8Ik5qiGxk8HGRp1uDgYF_C5dB2Ab2QyRRWHmuxN8wsh7zorpfyUxJ7gQLLi7lhM62So39HbFuB0uUgQ-bhMsKcC9Gwy5HUQKv1VI7G8T_lh9_DgdxNmfStGLiDoZPaQ6-6zV3DFgT2FogEtXv4TtH6C-31eHdUKxvIbqksA2vl6_kVWUmB3_YWnEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteVPN دسکتاپ هم سرعتش عالیه. تازه با ساب خودش هم دارم یوتوب می‌بینم</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/4987" target="_blank">📅 13:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4982">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.5.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4982" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">WhiteVPN V1.5.0</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/4982" target="_blank">📅 13:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4981">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWnZzX27mgYGp1ixkWA1ffqS_vJmfwLod-A5ctpvW5RK8JIbErWGbDUS85d8JFJBrB3OyaUtxuk_07TWn4-s7d8-3BJ8R3JQ6HrX5jUXsIhSzdj9KTq9gJyase4lqsnT0ecFSm-jEg2IwqMOhaT-uCB5BRJ2Qz1ZeJyIr_il6-aM2MfPunNDTZfzjjUHE_1n3NBd1UFVRbxVwwFelS9rSiMkviTid2K9tAmIqLv7xTQVO8OO0uo4z5co6EQs4iokk2nV8S-UmyXudGTsecyRBPtfSDmeRp4hGK5ndk8erh4bk10mGTasO-DzrMUkJkRf3lHGVAJyNMaOvetF_45lOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید WhiteVPN v1.5.0
توی این نسخه سعی کردیم پیدا کردن یک اتصال خوب و سریع خیلی راحت‌تر بشه. اول همهٔ اتصال‌ها بررسی می‌شن و بعد، اگر دوست داشته باشید، می‌تونید سرعت هرکدوم رو جداگانه تست کنید.
حالا می‌تونید زمان، تعداد و حجم تست‌ها رو هم خودتون تنظیم کنید تا هم کمتر منتظر بمونید و هم مصرف اینترنت دست خودتون باشه. ظاهر و بخش‌های مختلف برنامه هم مرتب‌تر شدن تا انتخاب اتصال، عوض کردن سابسکریپشن و پیدا کردن تنظیمات راحت‌تر باشه.
⚡️
تست اتصال‌ها سریع‌تر، دقیق‌تر و مطمئن‌تر شده.
⚡️
برای گرفتن نتیجهٔ بهتر، تست تأخیر حالا از سرویس پایدار گوگل استفاده می‌کنه.
⚡️
تعداد اتصال‌های هم‌زمان، زمان انتظار و حجم تست سرعت قابل تنظیمه.
⚡️
تست سرعت دیگه خودکار انجام نمی‌شه و فقط برای اتصال‌هایی که خودتون بخواید اجرا می‌شه.
⚡️
تست تأخیر و سرعت از هم جدا شدن تا خطا و تداخل کمتری پیش بیاد.
⚡️
می‌تونید چند کشور و چند نوع اتصال رو هم‌زمان برای تست انتخاب کنید.
⚡️
انتخاب و مدیریت سابسکریپشن‌ها راحت‌تر شده و از صفحهٔ اصلی هم قابل تغییره.
⚡️
صفحهٔ تنظیمات، تونل تفکیکی، اطلاعات اتصال و چیدمان فارسی مرتب‌تر و ساده‌تر شده.
دانلود آخرین نسخه از گیت‌هاب
https://github.com/WhiteDNS/WhiteVPN/releases/latest</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4981" target="_blank">📅 13:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4980">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">امروز ویدئوی پنل BPB جدید رو داریم</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4980" target="_blank">📅 12:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4979">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q73HBiktXshWnJeU0QX-ZJnUTYtqhdyEJM-KqXD_0FG4ArA--vXXye4PrnSMu7LcgcFBGhyiHTPLm3WMvP1ODV7pzjiBwLc0YgMuweskrujGbBc-DNp63oFxx4DbEAOo-RwoKrb0CKXr60tW0ySpdSQv36Tg_V_YjRbQv_cru-CyDu4HeDI5_kboP4xhT6aihmC2_X8IXGwYUpwoKmsK-aSG_BVZAIQPnzGbG1JLRNO2HBjVweo0GOHoedrRnW1V_vnaftHaKp4MtbYLsT9M-ZejL6-Hl_gBl09omuRQm8Ru-xGWszlAcvYbgsr-e-8oOprgqKz5u_T8iOQar1PX8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دمتون گرم بچه‌ها
مرسی از همه‌ی کسایی که اومدید
شبتون کانفیگی
😂</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/4979" target="_blank">📅 01:36 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4978">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">بفرمایید لایو
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/4978" target="_blank">📅 01:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4977">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اگر دوست دارید استریم‌ها رو دنبال کنید، جوین بشید:
https://t.me/matinsdungeon
امشب یه لایو کوچیک خواهیم داشت که کمی گپ بزنیم و صحبت کنیم راجب اینکه قراره چیکارا بکنیم</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4977" target="_blank">📅 23:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4976">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aeBG-2GMebhz9Lsm5CSzCGC3idmiEyEufYE2uvV09g7iVmbu_RvTmTVLBLJx-Y9JGBo4NTgsClQgWVOJ0rzwkgvJ2R9LL5ecXLBOqCJDPEb2enbWQMThA97lc3U9ODL_AHRQ7A3TIktFWMv8XHy2Io4fMbLcvkhPwiHLEWq40BLQqIxzJA-4CnIpRsXQqHoCrV7xvAE-FdCvK3q0uXnEd3C90YXCjTTkInYirHY3Xn7zOpcum3SrCxRc0k1Bz8GOqQy2EoDlkwdmgbPycC1JjpBBOOgRXxc0-T1U65Eh8gVYwpU-ZgBGin9ve_D0xAzGNLBLZaQ2iTKHLDcF2wKs3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ریپو رو یکی از بچه‌ها واسم فرستاد که دوستش نوشتتش و جالب و کاربردیه، برای گرفتن کانفیگ رایگان
فرقش با بقیه ریپوهای «کانفیگ رایگان» اینه که فقط کانفیگ جمع نمی‌کنه. کانفیگ‌ها وارد یه
pipeline چندمرحله‌ای
می‌شن:
1- اول duplicateها حذف می‌شن و ساختار و endpoint هر کانفیگ چک می‌شه
🧹
2- بعد اتصال TCP سرورها تست می‌شه (سرورهای بی‌راه حذف می‌شن)
🔴
3- در نهایت هر کانفیگ با یه درخواست HTTP واقعی از طریق خود proxy توی
۳ دور مستقل
تست می‌شه
✅
یعنی چیزی که توی خروجی
verified
می‌بینید، ۳ بار واقعا کار کرده. نه فقط روی کاغذ.
🛡
اعداد و ارقامِ آخرین اجرا ( که خودم از روی index.json چک کردم):
- تغذیه از
۲۱ منبع
(۱۶ تاشون الان live هستن)
-
۱۰٬۵۵۲ کانفیگ یکتای
جمع‌آوری شده
-
۲٬۳۶۲ تا
هر ۳ دور تست رو رد کردن و وارد لیست verified شدن
- خروجی‌های
verified
،
fast
،
secure
و
top100
(۱۰۰ تا از سریع‌ترین‌ها)
- خروجی برای
V2Ray/Xray، Clash و sing-box
— اپ‌هایی مثل v2rayNG، Hiddify، NekoBox، Clash Meta پشتیبانی می‌شن
- کل سیستم هر
۱۵ دقیقه
خودکار آپدیت می‌شه
- فیلتر
secure
شامل forward secrecy هم هست و لینک‌های بدون اعتبارسنجی گواهی رو رد می‌کنه
🔐
لینک پروژه:
https://github.com/0xRadikal/Free-v2ray-Configs
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/MatinSenPaii/4976" target="_blank">📅 23:06 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4975">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aHlPgBP_uTFSf8KKa-XSAVeIg2BbOYhX1Vh64X9NVYmwkvYLbyq6TEdQVsqZ37A2gQ-o5gaJ9aoOOF9v6igUhUKqlsr5009fBkvZf7wG3u5qrTukgUxDxzqphNNjBq8Xx-MHzv0qXkPwUIgAtjCQCvzoXsbE3KtCdMdCWa5fmHxGD8ADPnG8kcUl4mHNshX7ZQKKNMxr3ZDyjOmgTCNt-NELwPgSZimnsnJocZN9AmVfjjjyhbIqkdwm4jG_0a3FT9zAzYD_FO1KyAzx1cqQsypdusXC9u3lC05dvGAxGbmn37sHUvCw6OT5RlZYitrW8cgoD8p6c6quUk7AfSWcoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته‌ای که من فراموش کرده بودم توی ویدئو بگم، این بودش که برای حل مشکل آپلود حتما باید Fingerprint رو روی Unsafe بذارید
عذرخواهی می‌کنم از همه بابت بی‌دقتیم
❤️</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/4975" target="_blank">📅 17:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4974">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e6e4dhkmYX6oUC5I9ebEsDvp_y1ySFjzWlqBoNxXh3P0GL_u29uJbJQyFZKWWFltGkbfv9PfSLRVt_Lda-5z5yDwDL0-bJAEwc2wjqT4SxPFyv6gobLmyZ9__6j25IOjU2of_tOUTH1NImkuDu1pWGFrgFJbOPsqKWfiIGne_1dG9QauZRdQHh9BNlkTG6uVVnMEV5I1EVUEZWepDfhwyqLH88KYmyvpt1a1f1jUtpC1AhEQt9PdifAiQrkOHcZZLlyK-aDAZsnAafH1hZRwNfS1dd35tU3A7o_o5lsPAFUVRUk8hXTZhiyLvsIcv4M9gTxpy5Zxm9ccm9c7iLds_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب به سلامتی تا ما ویدئو رو ساختیم رفع فیلتر شد Worker اما هنوزم ویدئو رو می‌تونید ببینید سر سرعت آپلود خدایی که این متد پترنیها میده
🥰
که وقتی ویس می‌دید دو ساعت صبر نکنید آپلود شه
و متاسفانه ممکنه بعدا دوباره بزنن ورکر رو فیلتر کنن</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/4974" target="_blank">📅 11:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4973">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">فایل و نکات مربوط به ویندوز:
https://t.me/patt_channel_x/101
مطالب اندروید:
https://t.me/patt_channel_x/91
اسکنر من:
https://github.com/MatinSenPai/SenPaiScanner
آخرین نسخه V2rayN دسکتاپ:
https://github.com/2dust/v2rayN/releases/tag/7.24.4
اپ PattNG ویژه اندروید:
https://github.com/patterniha/PattNG/releases</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/4973" target="_blank">📅 03:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4972">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eMlppiyGHc54ddZrIusNTVLsI6lYMFu-8zYMtFxHeITLjk5GiPm4mscx_yTiRoLqbAQkPpNSAJigHTRyPfjp1jBvLIJfX-402wySGN1Yu0lb-QcdqT1p-QMNz-WKKpGbxEKm7SKA2cXv4ryMuQejZEYXGgu8do3WFE2B1wkIoK--KDFr6SOrxVtRK2vqscyV5xH-o0TjlEDU0vGmX2QkBQqtB4nfW94-yj0_mNzZtiOvDRb1wQIBhL6eSDA0CGmNk_guCvvYibKzraLsVZ_y3cShe41LYSYxnkLlFghfA69M_3lVeg7D2JiiPoJcycWv89TJet1_aS_yta6YbglkeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
رفع فیلتر کانفیگ های کلودفلر + حل سرعت آپلود
⚡️
لینک‌های مورد نیاز:
https://t.me/MatinSenPaii/4973
⭐️
توی این ویدئو بهتون اینها رو یاد میدم:
1- آموزش دور زدن فیلترینگ
Workers‌.dev
با متد پترنیها
2- از بین بردن کامل مشکل سرعت آپلود روی کانفیگ‌های کلودفلر
3- استفاده درست از اسکنر من توی این شرایط
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/4972" target="_blank">📅 03:00 · 26 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
