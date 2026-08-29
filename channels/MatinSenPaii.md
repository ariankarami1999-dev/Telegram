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
<img src="https://cdn1.telesco.pe/file/t-_niAPOhw4vAk3euT3W57xgJE1ELhNAEYz7TXZUvnoy_lAJV4xOZLXbo9KxGgNCsqnL0TZvC67e-QLmenkVwdKdB931aGYy5LnxpIyUlg3N8c89-qugFqap_QaKFejN5X4NSblSbYVXmBhNRiTfswwGNXyn_dthRZUQMxiD34jbQAsczKbNo4BNHX9RBoJbMBgkO2loVN4JlEQ2Y8sUQ1xwiHIbrjRkrPHXckkFYff7Bra1988QqLiI3Sha4ldY0ugYiAlrjQ8ypSms5ozZJ5Hk6KT5GTOh62-ej-fUF59y7PIeDaFjXbnlltg7blkcj02701EAiYMqapSm1PzkSg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 155K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-07 14:44:54</div>
<hr>

<div class="tg-post" id="msg-5086">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">خوب شد امسال مدل‌های AI پیشرفت چشمگیری داشتن توی تولید تصویر؛ تا این بنرهای درب و داغون الکامپ یه کم زیباتر بشه</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/MatinSenPaii/5086" target="_blank">📅 13:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5085">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دلار بالاخره به قیمت ماشین مورد علاقه امیرها رسید
🔥
🔥</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/MatinSenPaii/5085" target="_blank">📅 13:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5084">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">گویا  OpenAI تصمیم گرفته قرارداد تأمین مدل‌هاش با Cursor رو تموم کنه بعد از اینکه SpaceX کرسر رو خرید
😂
کامیونیتی خارجی هم به شدت از دستش عصبانی شدن و همه‌اش دارن هشتگ میزنن
#ClosedAI</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/MatinSenPaii/5084" target="_blank">📅 13:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5083">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/MatinSenPaii/5083" target="_blank">📅 21:42 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5080">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/MatinSenPaii/5080" target="_blank">📅 19:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5079">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مدل GLM 5.3 Flash یا همون Ox Alpha، به صورت رایگان روی Cline قرار داره. Cline هم اکستنشن Vs Code داره هم می‌تونید با npm i -g cline خودش رو نصب کنید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/MatinSenPaii/5079" target="_blank">📅 15:16 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TISBfrTkrN5UVb5eKeFRIC5APEaSbJaUpHE7TPVajCyapIXUyPX1ht64S9yXveayVKdjcnFGvW0Zw57KOAO4WOktIJ2Kq1wi5_y2P9xImWOw9j7BMupYG5Ag-ftCZbpp-amYOCjrGPJ5rD-k-IqxcNehAdCpjrC2ZsXNhaRbJP6dFrBqv5jzmo76gKEeeJvaJc1n_J0D58W2ZV7FI2miezX1KTd72BbvunGwxG_oav5oTb3EB0-MPP7huB5Ex8JLht1ccyf0piqzN_nxR477uNLfBaaAVX1DynqEgEhkaQXo8SLKsaN5S8q6-zXqJS98tclGovt_BftNePvguRtGsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه‌ای که GLM 5.3 Flash برد برای تمیز کردن گندکاری‌های اون دوتا، مقابل خود هزینه‌های GLM 5.3 که تقریبا 20 دلار شده بود</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/MatinSenPaii/5078" target="_blank">📅 15:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5077">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">این سیستم Re-Stream همراه با بکاپ استریم رو ابتدا با GPT 5.6 Sol و GLM 5.3 در تلاش بودم که بنویسم
اما چون نسبتا پیچیده بود و تانل هم داشت و سر اینترنت ایران یهو پکت‌ها غیب می‌شدن،
می‌خواستم Claude Opus 5 رو بندازم به جونش
تا اینکه Ox Alpha اومد
دادم و کلی از جاهاش رو کامل کرد، جوری که واقعا Glm و Gpt نتونسته بودن انجامش بدن
و در نهایت هم خودش، اما نسخه ریویل شده‌اش(GLM 5.3 Flash) اومد و کاملش کرد و فرغونی که از Gpt و Glm 5.3 تحویل گرفته بود رو تبدیل کرد به بوگاتی عملا</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/MatinSenPaii/5077" target="_blank">📅 15:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5076">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QnE9-dyr00_CgSEjJqG6BLDho9fSqP6WKbARG1SNQTjHJk04ozSsgEGTZWHz57CD2tQw8ayBdOw3_C1F4jccUVSnUEJcsdpakw_ZmjFSV1XmvXmDZgGSUw6m-gXSZSqQTua93og9KZyrMJDyzdVVWbHJ4JdF0e05AffvySBaCAgpYSov18Nq4-uY6nwq1XaMA8x2GGQu1UhiI1j5ilFNRImi3mPBqdn1no0u_9BbAN700E5w2v198Egi1_MJ7gDIt30E4LbkfOtkLYmPOh4QEDZyL8yNl3rP2Y8PiPdMNpDfdFWNT23bLotNEo4Fs0X85RKZtfq0B3QMmiKmTtGqiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاری که انجام دادم برای استریم‌ها این بودش که اگر نت من قطع شد، کل استریم قطع نشه و برای ۱۲۰ ثانیه روی استریم بمونه تا قبل از اینکه من برگردم. دیگه نیاز به رفرش ندارید شما و استریم هم تیکه تیکه نمیشه  و در کل به این میگن سیستم Backup Stream</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/MatinSenPaii/5076" target="_blank">📅 15:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5075">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n_Go-JHD0u8DI1siziFHzTcbr7DFOAdhCEpGFOgO4HKyh9RPo9VPP1DlOPr7TK9sDhRPM3xTc-rY5O0kYYiIJCjtU_eWxFlKh56nBBMAf4qiw11aC8GnDCDZufzUhI9Lwce5kjN-jPIbWHR-B99BnZHQUS0Xfcz54CXOdCzgouNpDcRH5WfUUBIf6VPAhrnczijf9rYA8p3KlehChdMk3DAN23VQlQDZk6mN_fBxrqkly6BMMb1S-4kPkJ0urLRzmPpnuKqneLzJu0yYZfeuHyyN6vqb2g-Di4PqRi0koqhJXkj-ANsaVBh0t__IQgW5yv3IBmF4a4z2oDxyA6tbQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاری که انجام دادم برای استریم‌ها این بودش که اگر نت من قطع شد، کل استریم قطع نشه و برای ۱۲۰ ثانیه روی استریم بمونه تا قبل از اینکه من برگردم.
دیگه نیاز به رفرش ندارید شما و استریم هم تیکه تیکه نمیشه
و در کل به این میگن سیستم Backup Stream</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/MatinSenPaii/5075" target="_blank">📅 14:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/MatinSenPaii/5074" target="_blank">📅 13:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5073">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l7up1oXpxs-cBwZ20i9nrfY2hOjsm7qTqQL1kgzdIVanCU-1-sIc5OyyEYN38Mxb10AthTBmatydyzGdgeZGTjQrn5fUquQ-CE2DGgTCBcDn9Uj2CLEZkhcSKW3sZAT62ViuhgPFowiGSG7xNPz2lorR1JnIkttu2qsl9a20Hfg-nOGu6MVy2GeMyy93w9sYhr7wr1bfBpWaWwSne4LKhRKpub6p_VFRIOoZNcWjvGodPuDxxUbq2sJ-yy9R7x4ptvgYShAaehwOQtLKCQqZ-tsxyyVF-2sIf91-D-fUvubCMKjuy5gz910hUFhHS4oDZ7q7tR34juTyn1r5WtYBTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐂
چالش Ox Alpha با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.  هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha: https://youtu.be/FIhoccZtpZQ  برای شرکت در چالش: 1-…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/MatinSenPaii/5073" target="_blank">📅 13:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5072">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h5XtLHmWNNBDSoTNVpcWLFocJOYDQ5nbW5dLO7sRrr12kiqdfG8QryzmZws-O5RuRBPQls885eVuNVqGTVUpFh3UpjpAiKdtMDYd4JcGVxlWPGwjJIEdz7dOdDKRJwlT6BEgXZ5mWFEfe5pUGcV-jo1R6vQGpJiDKD44BwWAccaJ92fHpXxbFtNP3cHuJs6B0aOCClYh2YRfaAepBjt6ip9XsIPUlOMyriFloR2qq734VjXZUU9wXnZf_uTH3C8jafKE-O5YVZVbuyM9ADeC-wu2hwGdaWludm5jupJnwD62t6iwwZdMhAEvPmhdl7yHLLKTJ2LyRsacyK18pw3law.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل ۱۲۵ میلیاردی Qwen 3.8 Flash Next در بنچمارک Agentic Index با ثبت امتیاز ۵۶، توانست Kimi K3 Max را پشت سر بگذارد و با یک قدم فاصله درست پشت سر Claude Fable 5 قرار بگیرد؛ اما نکته شگفت‌انگیز عملکرد آن نیست، نحوه اجرای آن است:
• سرعت: ۲۱ توکن بر ثانیه
• پنجره زمینه: ۲۵۰ هزار توکن
• سخت‌افزار: فقط یک کارت گرافیک RTX 4090 و ۱۰۰ گیگابایت رم اقتصادی DDR4
مدلی با این ابعاد تا همین دیروز به کلاسترهای گران‌قیمت نیاز داشت، اما امروز به‌صورت کاملاً محلی روی یک سیستم دسکتاپ اجرا می‌شود. مرز بین مدل‌های ابری و اجرای لوکال عملاً از بین رفت.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/MatinSenPaii/5072" target="_blank">📅 12:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5071">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a2386a8b3.mp4?token=GLgmzMvNZARjrS0wswawTr24e51Zk254Hn3ztm7BrUViT2CUsBX_Tn2kIbcB4n31Qf3e4n36mGqmgpUAY5414ztvvdbisyFw-evh9lGDOoxUt7kRZ7v2ohXi10MuGWlBzk4X_NUr0LXXpYPgi8FFCQUaSH4KGMk3oeZTwyK8Iw1LvA32As4wi75JAMgn3nHKJ_bR2v9OQFsf1pNexPrub61Hm-hGdo8Ue6aJS-OJ-8bNLVxIGtP3AjdQo4P6q3Q_HtHe7FfWZRNl-ubGYB6MS5DUSMkFSaqsrpthsuid-jn_Wg50-eoTarqDnanAXMkMufbXcyFVph_xYG5G7ybWZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a2386a8b3.mp4?token=GLgmzMvNZARjrS0wswawTr24e51Zk254Hn3ztm7BrUViT2CUsBX_Tn2kIbcB4n31Qf3e4n36mGqmgpUAY5414ztvvdbisyFw-evh9lGDOoxUt7kRZ7v2ohXi10MuGWlBzk4X_NUr0LXXpYPgi8FFCQUaSH4KGMk3oeZTwyK8Iw1LvA32As4wi75JAMgn3nHKJ_bR2v9OQFsf1pNexPrub61Hm-hGdo8Ue6aJS-OJ-8bNLVxIGtP3AjdQo4P6q3Q_HtHe7FfWZRNl-ubGYB6MS5DUSMkFSaqsrpthsuid-jn_Wg50-eoTarqDnanAXMkMufbXcyFVph_xYG5G7ybWZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این لودینگ ها هم جدیدن و خلاقانه خوبیش اینه که SVG هستن و توی سایت و اپلیکیشن و هرجایی می‌تونید ازش استفاده کنید:
circleloaders.dominikakissi.com
@Linuxor</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/5071" target="_blank">📅 18:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5070">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NtTYPmSECCKy8ZFH0Mw3NyKvTr0r2iyWJtTIuAsswL3mPs3-V-yrpG5NuM1BQiWJYlw1LURBgHy15TdY7WIu5GDWCcMJeKkZ6Xu-yvJuABEmaHiMjkJBvmS2DjZoD0TfYRqmf9VI7MvvRID6sgOgAIm5Sph2E7bIPRgfXea60v_yl1J8OL5_YpE5K2P31N_A9pbtiZVFV4404L1FH5SB4aKIyTT6ctISvMJai_mMSFaq1zZsES416y6Sih3-v8kzCbULK4Ru2n-umzifutEQHw-g5ol63JuHd_H9nMv6WU5wNsef2LbjxpYXTZtINmSkZaIrU-Z3KSOcbgyRhaI6Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچقدر از هوشمندیش هم بگم کم گفتم</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/5070" target="_blank">📅 13:49 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YuEGgTaC7HC1gDwT9PdDnXJrLUoAHwKfNxtrOL_WT8gMtbm7Q2yopVla3mVuI4ft9bkJAVw-vQOSPjngY4snV-TTqAmC0OB-_AWWgd-fFr9R_zpztf_9uogiYElE1If8Qoy02faPDBDKTBGCmdXqkhsSYpGtdvbJUKq4y9SwdTrAhWjbxB26z-yIGMNe8UmGQr5rU-TyYDVOhrPpEHb_u3dN1u5qAk-DMI6umBN5bLHcs7VkUH18_Z1eLuutuBEYqjpO8Kc2LubYyhFTZpdltNZMWONoPrEVWDt9qJ7Sj_ITbTtPBDLBxUj6B4ryPLVrl19SAFZ2vLret83ZDSnrzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ Input Cache اش خارق‌العادست
روی خود هارنس OpenCode</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/5069" target="_blank">📅 13:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5068">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GeODLWtiGx5V4PhWsxptQzmcpUEm5cOS8qyS7P9xVweljcnBSZhRm6SKRpQ7HtdYuKPLqa5Dqt1VqZpnEQ8IpSJYJfiOy7VbuGZqutXmLLKzQdrIOj0wyI0QfeJwfyyrBQbU9HFp_4auyBEefO4qRW4Nc9NJKYpYza5VNG8GibQ9Cb6NUaQQZdENad91GrYFqo_Wgtlu4gGtpdHL1cpphhqGQF3e8uj1Xs3qihtGTjNLVHjstXa31k20mcYOQ0a2eyOHep2PFNhP6BO1Q179uYeeyRrqgQgbiwA5t-mWcYiN83ZwW0hbe091_SwS1Mn4UApAe4gYPXJpfOEWacErKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصرفش خییییییییییییلی نسبت به GLM 5.3 اوکی تره
و راجب هوشمند بودنش هم که دیگه یه ویدئو کامل دادم نیازی نیست بیشتر صحبت کنم. باز ما میگیم درود بر مدل‌های چینی به یه سریا بر میخوره</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/5068" target="_blank">📅 13:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5067">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NjhPb1GPrrClcOAktCz4jD6nfzRc4E2zL6IcBJQwDqDUkESodAyknb4FDJbUiqP_w0BPwIyZNjvx1kLPwCMvKTirC5U76shB6SGdhmm_JwWK7nu6wOz4AsHIyoll_f3G9ZKYXv0U6hMX8XH-V75LLx_LMO3WI1ByQ3cbI_YCD6nRO2RduDNBAaJqMIVx-qOC-t1ocfvJLhvUGghgJDxoK4b_AZHkY7dBjE5FU1lsaPy2PmCZddEy4FTaF_-aXlDFZ_SAV-sbwCU7DD0Ds1jfSb1x3y-ll9zj3AH98S6XthWOOGt_btgkuiDfmG3DeRmJLl7yOZvXKY2C6nDwQgsITQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی درد داشت که Ox Alpha رو عوض کردم روی GLM 5.3 Flash و الان دارم واسش پول میدم روی OpenCode Go
😭</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5067" target="_blank">📅 13:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5066">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خیلی درد داشت که Ox Alpha رو عوض کردم روی GLM 5.3 Flash و الان دارم واسش پول میدم روی OpenCode Go
😭</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/5066" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5065">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🐂
چالش Ox Alpha با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.  هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha: https://youtu.be/FIhoccZtpZQ  برای شرکت در چالش: 1-…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5065" target="_blank">📅 12:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5064">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V1c4I_YN9Os7Im8XT_b3aaU-nxHn-oZISmBDDug93Av1hVh4rpi7Z0rYwlrmSQuF7uVruSDxVns5xzFptbw73UB0pa78_kjkr-7-NlWhuDBhWrp01q7PkL2rMPoDjH5i1LsUESehu5MOUPCc5EFosnwHqM_2sDyRI-jua0_moMUQ-MQawU6esWu-Tnem_bT9I3bbSE0tree1s-ILl3miWW0Ad6RW1HONDHerL8nm5YbGLHGDAZ7CHWcxc2OPD-9V3DKLALwI3ZkOLhdJOYEbfoBlVUDzNg6xPLmQBQe9JgExjNcsucHu-nDLb3SN2pRpGvG94RaHBGNGRHAEEU4q7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM 5.3 Flash یا همون Ox Alpha، به صورت رایگان روی Cline قرار داره. Cline هم اکستنشن Vs Code داره هم می‌تونید با
npm i -g cline
خودش رو نصب کنید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5064" target="_blank">📅 02:26 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BSy6nVtqDaNrLeKxvihhVPW-Z1JOBRX_e6QcPBDh8WQuFCNc3XCyjH3YWfFfgYs0gqPlTNqAh0P_WwvpS1W4eG_JsVj5NDg7gHW422UpiIx9pbUKbDAhAqiqV3Lhxb_niu6BrjjKAZbSdvM9u0yRWHnmOW2V0MIk32zOinvzil9jBU1mkjdV_93JGEtAYJeq4ELTDfLTVQWiS53JilEtlIQgTv5cVRlqE12jYNtC8thZAaDYU84-YRKlkqvFz9MIpoar7cXAQrpY3fagmFn4nu9Xz0l4Oio16yHUbHpm0ChCOdquRi4SEGSbn4yz6DLLsC1aaSfKEr4Wa3tlXkAm6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی این بنچمارکا همه‌اش GLM 5.3-Flash رو با GLM 5.2 مقایسه میکنن سؤالم اینه که چرا با خود GLM 5.3 مقایسه نمی‌کنن؟</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5063" target="_blank">📅 21:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5062">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">توی این بنچمارکا همه‌اش GLM 5.3-Flash رو با GLM 5.2 مقایسه میکنن
سؤالم اینه که چرا با خود GLM 5.3 مقایسه نمی‌کنن؟</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/5062" target="_blank">📅 21:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5058">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JizCXxJu6kI2ImCEWCrOXLDt9zDVGPo3A-XnIuw9mRFReQH8oBDC8Usd8vkX3DJBtgbniYpXpawMUSUZDTZtnPs-lDxbvMiTXZOxfWtOqS6QC4XvGuNuvjOx0GRHR4M3CSaNu2r2zumnYd3b-vx07fYOLqn3hztnWaHkpxcbdDNJZBgj7Nr0IalQMa_BQo264CLMx5oHijzSP6jQ_MhWeF5L3yKTF5NYOR1vJf01ee5ExDdY1kQjNNFUPm6MbL1TrC_1Zmv9GdJanlKBpyWZ1mWu552OEOKPdN_C3FYkUGzcN-bG5nKkJiM7uVuOznow4--5rwbSyLeDe2stidtvKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/od3_xLEylb9MdQ6hlVsjJjAYE9bA-3U3R_TkH6965wlz8XO_GgrQF0BBdcl5U4MDp4RWeja32jSHQZsnYILGEC9DcBushTZ_AxXNsgtlFvHI6sQsBzDnS73L3xw0uT2av1FXWXZFopW71NNQiVREZzBN6WSAi0RYYYF2lHNud4HikxuYTdUpyLB0eMJJORHezMg13wzxJVOADUryo05qcr9e91_lzewcJV0Ioif7-5qYeH_sT1kjqHgU4PQiEEsn8_O_N11ivPsUZ9T1qsTHHcE3rr6Jnnh9SI9-emYQJQGkJSNVI-fLmu6uw8kDHA3JcTDyVIIXL79o3v790vGZzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PCqNR-4sDf7dDfbm8JZE-hsNb74yucIOckt_gy-tFF_tGABxEvxsrRHt70qKOenNZnFHGjEvhT083_ciqtRgMz0pzWmGD0qKAuKiPT2gM6P_CsY8J-HLsy7Ec8hZ_r0LfGGpRk5we-e-aTv6BB5x38bTBqPdUYtFRnYEXcktNU-vUSsKINqfE3MQZnIQPQZWiGlpMoC1UkfO0CHo67NfqjJ_pYfDT6VyNxRgcwAycJp6czyu7uEiVAJKM84q20GKSioSMrfYNTapDnDuj1d63AYXxqWMs7b-Qksceu78xDBEIM872w8RJwmhX8cem5CKiKwyvdBtgxxn5cGzQ4n9Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SyhuUhnyw_MudPB7H4psONf69A1BEgLafUtup3Khy2E59e42F5e1F1i2QF67w2jIRjuvIpRtI6TFvifY7nCU5_A_cK_Dd8SsAzhajQL4P-Nn0V9273Hswy_FYcQX5Tivh5h8RVq_OPqcAnV3HaYh2hKENyZvSmIBnzGkwhCEwDY0ozUam6JoNZwien5y6p6JYD1glb1TOWebt8WNBUTlcYNFqlY_iyzziUWuCWeI3Td8XBWgJlU-_m4C94XPzrsjzrgHKSuiZgzIYxsqOgyiRHp54nPD1g61v9O-WV5dIaDzRLc-o8d7QHRGpJ-xDdWnhYaP_-ByRz3_CxxBK_euMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5058" target="_blank">📅 18:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5055">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T8aA1iKi4dloRzppi-F9-nrthTW1JYsX3sJ93rTUJrJSwQKvRZ3YyNqXl8Q-GXa5Qt0fhA-jXhimx60wi9jLEjWcdni0vghMwjU7_gdiwrUsFuREBtsjSnDCaXAh7Xe1ifhIil-qcNJ455eCMGqmPdGcTQSRIe8r6YCaEVBsnW46h2aP3krTo0b01kOCS_BG9dmD6joYWyx5wYCFk0sJvFxSf3VC-DcULDXnU64kY_eVxZ5u1HrZ0akotaNoKTxREDB9tqsluKswc2gK76CJMMqAAa-_pHj6QfMJuBGXTlsNIpXNn-jZs6SXZTCCbV4D8XNJM-meJYdeQZMlPU77VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GZEkjibCCD0k937Qnp8WTIk-YlNx-MI8AzFmP-Rw_s6jJcRJkeiKO9kzz9hjDj5O-A9CXWmEbv_74lRCCfPe2vQHE2s4Hj04Va2niNpzgd_ZShdhCt26e2G5i0Tf97JocAJQBnLw-4u9FIZtjGyRE9cfTuDjxTKYVdKc976E-VHsqfkHYYASQEahAHsY7YQtu4kPQp2Zi0jKFxO0Vgx6W-ah4teTyVTKvOyjNFBKYN9yar7Y-jo2OLwaT1Pq68l-SF8jDXuo8_jCkGCug_lOr8I0zskR_aYeMOVKP3be36BHKYQH9uMB8F2v30iUGQxBj4WJqknG9oBA3psiu_07wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OfBee8ckgspxgNWgnZd3TCHoyUta_MxVpYBVFq1SgH4Pp3Dnt6JIq8h3Vy3kBZrnVm_i7sZZImv-WeHP9SWm4NbM5I_Tz2BTZGuozcn3Rz5zTjfMPbmmq35U3fBkwfvsAesWc8GGMuoaQjKWxtwE6R2QOBHrNGUJ9ur7Iolslln9MXJaKETM8aZUB-G1y5SeNrVsuNXi6SlDNMRj08SGVHUc1gS7V6F30b45AZ88g_4SDMU0cqiSPXIkXz_Bxoy7XP3VvrAPuhhlizeHdj2SfkWUCt-vd_wtMk76wjA-Y71Ghzz4HAjSqmHAPAx6op7ZN914PV-8hxXIIzf3RKYStg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">باورم نمیشه
running Entirely on Chinese AI Chips
😐</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/5055" target="_blank">📅 18:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5054">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">خبر:
مدل Ox Alpha در واقع GLM 5.3 Flaah بود و گویا حدس همه درست بود و جمنای نبود
🥲
اما....
مگه میشهههههه
مدل فلش از مدل اصلی انقدر قوی‌تر
😭
😭
برم تحقیق کنم ببینم چی شد این دو ساعت که خواب بودم</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/MatinSenPaii/5054" target="_blank">📅 18:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5053">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gv6wQ9hB6mjG727N8Meq9EasSq4VRlZJv_WFHQ8gu9mZPCPESrSCO3Ofafl4qGLVkTAoo6zLhT79YGobjjeQ4YAsKv3qUdLpp8FjgQdMmF_xAewp3gg6AXrRrIhPmGXeUQkk0ErJKEU3O_70tki6blm9x7tQl2rFo3zw_WQ0INYtEK3pbjTIpSSAPxH2ZBebJQ7GXaKmjwQUJ28IijfyEwg5nxHRbnf-PV7Pzlx__XfdHaSN7y2zMPYd3jjr0nT8kz7_f9DImrjK7yiPnhlI6SGMV29H7GN85P64vAW7sShLkk0L4j42xRzd_ZlBodhvsJqu2BdKtoKex1qSoGKSdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو ساعت خوابیدما
😂
😂
😂</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/5053" target="_blank">📅 18:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5052">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🐂
چالش Ox Alpha با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.  هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha: https://youtu.be/FIhoccZtpZQ  برای شرکت در چالش: 1-…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5052" target="_blank">📅 10:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5051">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5051" target="_blank">📅 05:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5050">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">به زودی آموزش ویدئویی این ویزا کارت مجازی و روش گرفتن آفرهای رایگان و اینکه چطوری وصلش کنید به Google Pay و... رو می‌ذارم
🎨</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5050" target="_blank">📅 01:29 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5049">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EbNJd4ur16uF98xKtw9eu6L2C6sUIhDNXTxmbFvvu2LMc8ZmZjC47R9bK-afNgqXcfBI7F1WqLHBF27NLvOhIfSf3ZbXYXHgXT4VALZFuN8MxL9i9d6LqxhqEYAm4TtcjcdPVOCD08t3Qy7LCAHPljL0EL0FE3V6JeOI8_Gzi-KH9RXeJkkZdggTz0SubkgPfYLVeuPldnc7u0frxkq70-BXG_u8yxgAv8lGqqQNDqxiYn6-U13aEirLSEIJU2IIrdcsfr6Cqix6mwZwJinsN2K-PNjpl2YY-RfrmAPh62-63_KAL7RBd_BxgXVqY2RB66rTHj4BKPTYZ1NgJdwX9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قدرتمندتر از Fable 5 ولی رایگان! مدل مرموز Ox Alpha
توی این ویدئو رفتیم سراغ مدل مرموز Ox Alpha و اون پروژه‌ای که توی ویدئوی قبلی زدیم رو ارتقا میدیم باهاش! این مدل، به تازگی اومده و یه مدل مرموزه که هنوز اعلام نشده مال کدوم شرکته، اما بررسی و تحلیل می‌کنیم که مال کجا می‌تونه باشه. و همینطور بهتون میگم که چطور می‌تونید رایگان ازش استفاده کنید و کد بزنید
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5049" target="_blank">📅 00:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5048">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دوستان من کمی از لحاظ جسمی مشکل برام به وجود اومده بود. الان رو به راهم
سعی می‌کنم ویدئوی x alpha رو زودتر بذارم
❤️</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5048" target="_blank">📅 22:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5047">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">و خب من نظرم اینه که، Train بشه که بشه:)) مدل‌های قوی‌تر، ارزونتری که الان هستن و داریم ازشون استفاده می‌کنیم، بخشیش از همین طریق قدرتمندتر شدن
ولی خب شما باز اگر نگران «حریم خصوصی» هستید، دور چین و مدل رایگان و contributer رو خط بکشید</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5047" target="_blank">📅 11:25 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5046">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">به خاطر جالب بودن این پیشرفتش فرستادم. وگرنه به نظرم این نگرانی تا حدودی بی‌مورده.
زمانی که از مدل چینی/رایگان استفاده می‌کنیم، عملا داریم امضا میکنیم که از دیتامون استفاده بشه واسه‌ی Train کردن مدل.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5046" target="_blank">📅 11:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5045">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/5045" target="_blank">📅 11:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5044">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">راجب یه پادکست جالب شنیدم در مورد یه تیم نرم‌افزار نروژی که 4 ماه کامل از کلاد استفاده کردن و بعدش کلا بیخیال شدن برگشتن روی روش سنتی خودشون
فردا خلاصه‌اش رو واستون می‌ذارم</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5044" target="_blank">📅 00:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5043">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نمیدونم واقعا چی بگم راجب اقتصاد
برق
...
می‌خواستم امشب استریم بذارم و بریم سراغ اخبار ai، برق رفت کلا تمرکز و انگیزه‌ام پودر شد.
کلا همیشه ترجیح میدم کمتر صحبت کنم راجب بدبختیامون چون همه جا میشنوید. و بیشتر تمرکز رو بذارم روی کار که کمی از این فضای حال به هم زن اقتصادی کشور دور بشیم...</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/5043" target="_blank">📅 22:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5042">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ما الان داریم دقیقا مسیر ونزوئلا رو میریم.</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/5042" target="_blank">📅 20:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5041">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">راستی بچه‌ها پلن 5 دلاری OpenCode Go رو من با همین روش گرفتم. اگر که خواستید بگیرید میتونید به GLM 5.3 و اینها دسترسی داشته باشید به ارزش 60 دلار مجموعا: https://t.me/MatinSenPaii/4915</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/5041" target="_blank">📅 19:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5040">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/5040" target="_blank">📅 18:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5039">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/5039" target="_blank">📅 18:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5038">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">☠️
آموزش OpenCode، رقیب رایگان Claude Code
☀️
⭐️
توی این ویدئو: 1- با همدیگه OpenCode رو نصب می‌کنیم(کاملا رایگانه امکاناتش و اوپن سورسه) 2- طرز استفاده ازش رو یاد میگیریم و بهتون میگم کجاها خوبه ازش استفاده کنید 3- یه چیز مسخره با میمو می‌نویسیم(توی ویدئوی…</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5038" target="_blank">📅 18:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5037">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nffHrrdtL5AuVM4Z0Cg3iuxKjHP9H_PEbfcXJHPo195CfsOASnNXAJXypElhH6R-la7y7NwoQKX0guoLEdjs3WSTG52BrWvQLF3KHIH4h9CwhAqpq1naWur-yWF9T9q5sTAZr-y-GIhblEmoAJV2rgonoHyRTWsCMpDIWN6sseWQutpf_wxJ3MNVaCc9N9NI2gGH7u2w_C5VXNOZ_WuiBFNZCt8GK8czxkwdx3uTAMNDfowduZF8f8W_0mMBYXGQttQ4xFRnSJBKLr5Wl2C3eEuqjtGy5wrOLljHY4-kJakKK_mUINpjfruVlbjCPVC0dnXH6F4Dk1VXxhZJqpOniA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش OpenCode، رقیب رایگان Claude Code
☀️
⭐️
توی این ویدئو: 1- با همدیگه OpenCode رو نصب می‌کنیم(کاملا رایگانه امکاناتش و اوپن سورسه) 2- طرز استفاده ازش رو یاد میگیریم و بهتون میگم کجاها خوبه ازش استفاده کنید 3- یه چیز مسخره با میمو می‌نویسیم(توی ویدئوی…</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5037" target="_blank">📅 18:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5036">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vNMVxOu8Wvzyxj7jB28y2-r3WFMURnyFsTDmajTCyzhMOr_Yl5s4iJlppPUG3Pcv9NO5EdUIiiGE5D8ArCFNleBnWbgSBwpVD2h-B4lsGfRJFIjzHpwQVMaDY9IjTFKBfFOU3g4epAvULU1Ta5nsIx5V4r6ih6WFOxsAYravLVWAeAxVIFx-zU-gzhTm5c0u-KwhlO9PNAvegSHh1yXfDWYlzPmUK6Ky0NP00kdyrgIHFmPD497AbJGiwHxAqIW3hIknKJ36P7KLzYciuyVSVr8zIelkxaj8YfReCEEuSrcEECEZCUydNRINw-FSaw0sZk9R4yGvRjLODIh9oqWURg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5036" target="_blank">📅 17:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5035">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">تموم نشو x alpha
💔</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5035" target="_blank">📅 17:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5034">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">تموم نشو x alpha
💔</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5034" target="_blank">📅 17:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5033">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/5033" target="_blank">📅 02:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5032">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خب انگار قسمت نبود
👍</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/5032" target="_blank">📅 01:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5031">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">یه ویدئو داریم واسه Open Code
داخلش یه پلنر ساده می‌نویسیم با Mimo
توی ویدئوی بعدی که پشت سرش میاد، میدم به X Alpha و اصلا یه چیز عجیب غریبی زد.
موندم که واقعا این مدل مال کیه</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/5031" target="_blank">📅 23:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5030">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/5030" target="_blank">📅 20:17 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5029">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دلار 200 رو هم رد کرد
ولی نکته‌ی دردناک اینجاست که هرچی جنس می‌خریدیم تا الان با دلار بالای 200 بوده قیمتش
الان قراره حتی بدتر هم بشه</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/5029" target="_blank">📅 20:16 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5028">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iVmreBxqWSVZ-oIUfxLc1tcpO6pZWpw2vxYXiPmdpkcQIzdoDUJlBguNrKnemK6o94QJbNpXd3MgIxfX1GIYX7ac4VvNWS0D1g6AJZCo_0vE_0e2UbbMUd4NsZEmMIoc1SXnIsOtrphAu-Ry8u5g-MHtapQTl6zPdJX6trZZ6IKwykP6o-L2jX5d5xUpmr3PicF3Xh4OVvcT2AxkZk5MI-Su-x5CoM2MDII-K3GF1OwLQSxbZixMcMma6sTJFguaglilqtYwSgdiEgG2f8axYeTHkP2qvTriSiMiVyiTaPan7IxTSlTD_oGKsTCmXyuc9UCwZ5bVb1z1Ro8_ufBa6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسیدم ۲۰۰۰
تا الان ۳۰۰ هزارتا امتیاز
دو برابر بشه میفتیم زیر ۱۰۰۰
❤️</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5028" target="_blank">📅 19:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5026">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/l00x9713z6ucKqc1Y4GILrY1mVC7VdatQhrCn_-Wik09nCSgjnv4dlSR0FHfJ7eCLAA91rzZ3FOCjYGR-cJ952WR89FWVIxLU7Sw1lErnwd9GFR-mhheNb0V-GTjRhG0MsxbtoP_QkJPrLyGu8B6pHJgy_5DO-vqWKy_uisdEa4ilFEh6t6tdjMnmQ2NO6WKOA6HXGpPB04H5N3YXcAvZoMUge5UcMEmpTIXeJsALTwZGH27Hp_dcO_tinNfWXW4BSp-fyYoEZQ0OODCIuIniPNrJPoDw6BkUsAbNeytY79tzzq7gqSOE9GCrndB75y1ecOrOKfhmH1PVCw9sYaZHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/f-cD2F-3dENuwssSqle_U9PgJForKnTdAMCvvWFV1KitrVmqqbWHtIRGkXJGCkcixclrJ0I2Y7s0TPNjhCSWcgX1astVR4cuOxiDd-9ThQRioymQwPl46jNDSI6UFcDiuqTqkDRtu-yOZFsMsKNQQnasX6pBNhpOI9OCvQtwxwUHrYTvLb0YIlWQrMf_dUOoVSduQ3H2jChd6cEK0DUDqd049ob6QYGvGpvskdsq0Ea2aUUgIXAaZWwDLTQrpvsIzmKgBWbbzKPPlWFz99M66vtMDtCa8vW7nV39uPvzBpI4OrGagmIkRUmsKiI8k0MQMPEO2NKcY3hY7HgaQEsKtQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5026" target="_blank">📅 17:17 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5025">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WT0oIb8KitTP9Xr5qq-R5Qp3efiaAeyHOWAC75qtPY9tYINKB3wHzo0f56HdOSilEL2umt6jfnWzX1y0NMI_esQ7aOhmHmuFUnbN-_LCnVtLUqIrRrLSE7VF4MYByQoGcbgk06hq8TPa8ONe18bx0FGpBzwHxDDJpAXaoTu4zFnpG94k_g315xqBLSMsN3pfaVUBBdjPRrUMcun_fQn4UweSqmB8SAkgXOsHkb4QqvdaEH8lY215EQYTB2szAEFkykbLv-vrUWLLmPisGkBLtvuPZykUnVKx06ZarN8FHy8v_itRaitFlqhrKdZp2fYRmx_p8hdPC9Of4MwD77tjIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به خدا چند ساعت خوابیدما دلار کی شد ۱۹۷</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5025" target="_blank">📅 16:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5024">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1357719d90.webm?token=IhO08U8CIwViPJNyMgfKPlBabcZrsX8sv6cv08WZslIjYV4NLoahVyxwW8ZbNOQfEG8R8aqJu7cmAIYtaz0H_ackvxPABL9l_9FcjzmdLRmwaNsER1s8yrgPdWKgc7xAJhJal9yC6QiP48Ym_TQYQEeZ801ZSlGEkYPNeh1W2b14UOUxZqqoo_PALU-wEifb9QzueOy5fJfQQ6_vvPVolF4R-H6uT1gWNh2WuncoJPAT9W4gNcSfO2DyzhNqv9sX-w5AjN6fbZnfxuePAaF5wNcpNM-blwv0fIcYsqbcRcZ4FVuZh7lvtcE_sYVPuyZEL9_dLUJYTfkRP9T4S_In7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1357719d90.webm?token=IhO08U8CIwViPJNyMgfKPlBabcZrsX8sv6cv08WZslIjYV4NLoahVyxwW8ZbNOQfEG8R8aqJu7cmAIYtaz0H_ackvxPABL9l_9FcjzmdLRmwaNsER1s8yrgPdWKgc7xAJhJal9yC6QiP48Ym_TQYQEeZ801ZSlGEkYPNeh1W2b14UOUxZqqoo_PALU-wEifb9QzueOy5fJfQQ6_vvPVolF4R-H6uT1gWNh2WuncoJPAT9W4gNcSfO2DyzhNqv9sX-w5AjN6fbZnfxuePAaF5wNcpNM-blwv0fIcYsqbcRcZ4FVuZh7lvtcE_sYVPuyZEL9_dLUJYTfkRP9T4S_In7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5024" target="_blank">📅 16:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5023">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">به خدا چند ساعت خوابیدما
دلار کی شد ۱۹۷</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5023" target="_blank">📅 16:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5022">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">حدودا 20 روز هست که دارم با ابزارهای مختلف و AIهای مختلف کار می‌کنم و خودم رو آپدیت می‌کنم و چیزهای جدید یاد می‌گیرم، و ویدئوی جدیدی ندادم در مورد AIها تا هم دانشم بیشتر بشه هم محتوا باکیفیت‌تر. اما طی روزهای آینده، کلی ویدئوی جدید راجب تجربیات این بیست روزم می‌سازم و می‌ذارم توی کانال.
(آرک سولو لولینگ مخفی به پایان رسید
✨
)</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/5022" target="_blank">📅 06:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5020">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CEtPc25bBKZjSDkapZAILqBZziXcILwlR3PVjLyfHEvjZNozewJ-V4thE68Pd6hRrwH5b70xqhuZShhxV28SCmbptcl_jRNxeHng6JNhStmBHjz-2D7_BTCfBpA3E98RBaCJlAPaZaoSPKdDlIxP5r3TVi_G41C6C-l32j-asChTPVD_baphN6zCISSZD4viNet8L6ZleXr7cEdNy3ShEf1TVKh591OqtF3Op3b8y_r7s6rK8t0WMtWpFM21e_waFVIKXQ__vACYIjI-UjNnW_fRxSpYaxeWGQUuptwXJkB_SNo9JgmnhpHutF0EoO2qj0pGMpmtTpZmYYUrbNvXtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZT3Fx1kmneVoAIAHxeA2VYpoC_L_0pVgbM8x6_PjMiaFyr1bvCMVMr12Ov9hDNfA9a9b-TruOQo4MUXNvXYUp804mMREDzPr8Jd8ZUqISifOh_zy2I4Qy7umR-Ouae92cDHF_M5mKmZnJRMBactZM2H5OHtWBaBKfXn19zAYr6BaJquZW-Gt4RoO7WhH8o89b8Pqew_WSJ4iUrBEvj0s6SeS4zO--En3nPBmWDk9ySIyJ4pXWAOZNnQBrtQ2_xpibWkNr8D5bJ22Et1CJTI01S9TPt9ZOWJuetkAkAKWWuM8nXTN3_nBLP9po6N8rnPNIrQS5--_nw1YdtmBEWZ9iQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خیلی خوشحال شدم امشب از پیام‌های محبت‌آمیزتون و از اینکه آموزش‌ها چقدر کاربردی بوده واستون
❤️</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/5020" target="_blank">📅 05:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5019">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LM9q-16XCJlTGEKw52auWE0oXD2HlVcjUxnSimONhBzfN-izbigNRPDc6zWWNHSjAcNQ4AKqcUrJ7arVBIernV5RFS2R7_Yd32CiPjvXMIjqwQ1zrFVFpuGTnfe5unVWoxTJO0_626hfwcECUFQrEnOhBcZnit6l3HHrnX49O-sidw6x-EZkaLbvuzMiTGX2TSLAC1oLCBy77sHOK7sGQEYux0oZHi5p1-wxyYvA0UKhFCjkNQfaiNzwpBM9jV5Zlb_F1FXA8qEse1nD4kH6-Oj5c4eorT-zRj2F0RbeRt-0t1e1PB5440CoSSZaTodpIKueBaKwehMf3vEoQJvUXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم یا مدل جدید شیائومی Mimo هست یا به قول یکی از بچه‌های توییتر مدل جدید خود Google(جمنای ۳.۵ پرو). گوگل هم ماشالا ید طولایی داره توی این ناشناس مدل ریلیز کردنه
😂
خواهیم دید چه خواهد شد اما تا الان خیلی خفن بوده</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/5019" target="_blank">📅 17:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5018">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خیلی توی کامیونیتی خارجی بحث و جدل شده سر اینکه حدس بزنن این مدل جدیده مال کدوم شرکته، چینیه یا آمریکایی و OpenCode هم اعلام کرده که دسترسی بهش نامحدود هستش تا هفته‌ی آینده و روزی 100 تریلیون توکن تمام کاربرا می‌تونن استفاده کنن مجموعا و ظرفیتشو دارن
😂
همینطور…</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/5018" target="_blank">📅 16:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5017">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">خب من این آفر سه ماهه رایگان اسپاتیفای رو تونستم بگیرم با همین روشی که اینجا یاد دادم  مزیت بسیار بسیار بزرگی که داره اینه که میشه به گوگل پلی وصلش کرد و عملا توی هـــر بازی‌ای خرید کرد. البته من با VPN آمریکا chain شده رفتم که ساخت این رو هم یاد میدم بهتون…</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/MatinSenPaii/5017" target="_blank">📅 08:23 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5015">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WVzO0thtiOWVR_2eRxG-3w0y6odwMOtNax4-SEuY8-90u8ZcBhbb--ajZ0cJq9zIGltlC9lltk4zbLl51xOw3r2QNUUi-F94vbgJjJ_LTKvW3Fn5krVxDjl5PDttYBDxTjYULh8q1RXz3l1-GY19TaWTLm4EU6_KeuBYxqYZkXWszp3b_VbX04XIo0-qx8mW6tvwlHYuaaZ0dty7upkp8SeGgHmgWwqe7JjG72jHvXvDh0EeiFvaVWbYXsY7OFpnc5lApzyKKsP811XUlQWjOAxJSfYSZP--xkLIgZq-uihOZaq3_-P6s-pIMAnmEaq7-ocEq80jTLZETQAsOvANhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qJlWYe6NalYyQvLQw4dT5rEnf-xae1__RSn32ibj-nzbrXK69ILDZoF6k-MaZZxnYe317As6v5j-mhaIY64DB813UO7OzVNhGFIKasBPqsVWgQS-MGDy_cG4g_FU11nxnrcPtmrWq9jmgSL7LlOLlq_WBjEODS8M84MZLTMMuM3BGGlCZsq8Oio9uUgpBb300TOIcUg_4x-TRzt8EfJDBJunATF8qxFB-NjAOqdAvtSLvYs1dnk96NEJu8sZCe-wDOs7ZYlMZ_QnmVo35-7_ljCpZ08W2mwU5y_4DaIC4TTl8g4fWveE7JEWMieEIi7ZjDljkfeUmKEw0gX9b_dENw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/5015" target="_blank">📅 08:20 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5014">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HUQQuQCJBrqfgaGQg7Ttfkfvsq6ovPogK6wA6dCbqrKdYTaHLZkn401awqR_d1j6qEBieutSMbKAMChRfAnTPi1hL_3wQjwDoXY_pDdYF_x5gPELzITj1Yw25n6EpsTYppcSGPG4QcO2lKU6QOIOidijuGL9Cs-G9J9sRpEjaz8S6Ca_kwurHTGhO3XFGDf_OVeqvpWx22BzM1Pg9BaxzKVEY-CKyZMfAfvh4SON5BM5X6QoF-0ci_zggFZF4x7SPFDoW0m9xrSoyO2lTIgDQj1Jb184K3TzImbIYIC5YqYYIG82LfsWRYoodOC6X-JlenwJrs-450P_nOWWErzTZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل جدید و مرموز x alpha که روی اوپن کد اومده به تازگی رو می‌تونید این شکلی تست کنید روی 9router: https://x.com/MatinSenPai/status/2090856359117902053</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/5014" target="_blank">📅 08:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5013">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">فکر کنم وقتشه کم کم یه لیست از چیز میزای رایگان و آفر و... هایی که با این سایت تونستم بگیرم بذارم</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5013" target="_blank">📅 07:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5012">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qWaKHDBCUBkIuKW35PFqjnizyMCz66Kiz5i1TCnLwhPN8H7ZRBt1pDuqWYA0fgGhQ3yAtnMb1pMlhus2cNg_HoOCdL0WU1XARGjAyL6glGNKck-64GMhCU3Qv2zxuEEF7P8lJE9_cvvx6rbgllzYbb0LVPFyHt-HSA0_-ddnhJbHZ6_mYSp_Kclk0XQ4GB-eIwdq8mkvzBaWN84_WtADNqPRI2TxkhVOJcl75v0Xm6cvE_gQAEhAtlIlcIVUyE7iBYNL_g3Nx0i12jPCX98gk42zhKg_iWYUdb2-WrTWUeF7P4QNa4AYpWXwmYMFj6h1NHdMLd7Pk-ayEfD7AOIS6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سریا هم یه جوری شبیه دی‌کاپریو میگن «اوه این پروژه وایب‌کد شده» انگار مچ معلم مدرسه‌شون رو وقتی دستش توی دماغش بوده گرفتن.
همونقد معصومانه و مهدکودکی</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5012" target="_blank">📅 07:39 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5011">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مدل جدید و مرموز x alpha که روی اوپن کد اومده به تازگی رو می‌تونید این شکلی تست کنید روی 9router:
https://x.com/MatinSenPai/status/2090856359117902053</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5011" target="_blank">📅 23:07 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5010">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/UCjikNPga-vTXfXUrByh049WpYOaRk63CaruAeg6LVdmiu1pq400sy5iGJzirFo-54oPuwzZwUgtwES8t5undtw1AFnt-MnD7pRFrcpjWNr7wOF-M8y0j7fvRLVSC9VTUDB8AvITAJCtIdYE94aK53WZmlOgjUILIq4u7YiLuuSCNK8-jNsXNb3vMV0BXV65wp_F2CS8fzPM8WMeILwwZwRKe8wqMMVcVhiaBxLvWQX9LQIZ_zF4yef1rO2HTNuNKMVF0MupysEseafowM5e0q14j7fVeXy-h-Tdc446dludpCDTnel_YFidQu132F0-qHSK9m8p0pKw-McZkdQeuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5010" target="_blank">📅 21:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5008">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UoRBI_OBFHIzlb-j7sTydA0yJGNYz-awTeT4-4RUEYXFOMZgZgNkHQ-I9ibM3iKP9XpycL3_2iBs5f1aUFgdHeDVfHrIlUhzS0k9l7gPNfGBy4Z6XJEtiOTuFkrs3r3G1NzFof6O9IEJspj6OWpSVsc7UyJfWe0CVhGTFL-Cv4cH6L-FkQynE7PNs5pzsemmrm_Odw1faWkNbxPgYgYg6LYTuABxBVfiEetslU2bc1IudKB3CMmEG8roNFTLmM7iD1FpvqXfpUxyz9llaoCba6lzTniyixz290Ye_0d_0TaTjOko3GopjS0Jhp6m-Uoladdw5grZ80ROMREFx0OKAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PcQjehV34elo1ae9zOOhF-QTeuMjrLW-k-Z-t_428pUm7kMiWvWANyXu7MngzT06MnjaSwXwUtr7YF53U7KThZDnzImDDATprj1pLeFepn3fsBpEnmD56OaRGFU9pOaliNAU5axUnEqJvRbdiuSRxWYXw5KCK6PieI8gGaHJi7f4I4XUA7tj9zbclKCoEZ4OprdRA4PCWU2rxd8l3Zd-DEZeEDUjNI5OOTuCiMsDbLsKqnJnFN-Bakkc0LP4uz4XB36Is9XOxVLKedmIXy8wh4pWnhuOghkZM-r2hYZQUl9xZKt9C32V9xJVgqdkgrkcCCAPzkXT00aVMIGsXhoOew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  چند تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5008" target="_blank">📅 15:11 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5007">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/5007" target="_blank">📅 15:09 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5006">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jXBWBcWa26YYexznOcanQWj-aKlic98EY5uPvw9vjKEibAr86zWGEY0nFFv5Fiu-7XXPHIQBD_2SQdgHj-ojR3iX5rCk4jJKglniLidXLc6-hkMITVJ4aky9meC_sF4n3TKD2V1TEsVBmCXKOAYPv9FLq03ykM52hhPiD_D6RzIbZGRW1wX_VN2mdb_UyI8ztEGTNB6cNt-i2_mRQuCvS3KkB2Ub-ODkX0Xrc9Yl8Wc18WhS_-N_9PhaVWQ6Tm4khgofeOYgriFLtTf7tpmIFqZ0jy1SfFC6-uR-QzL_ISdkDPTg3n4W00V0aaZflqierVb0wJfcpObw5HAgFVB79w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه مقایسه‌ای دارم انجام میدم</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/5006" target="_blank">📅 03:19 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5005">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">آقا این Muse Spark هم عجب چیزیه:) روی هارنس درست به نظرم شاهکار میکنه. فعلا روی OpenCode به شدت سریع و اوکیه</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/5005" target="_blank">📅 03:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5004">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">بیاید بریم Rust یاد بگیریم لایو هستیم روی
🟩
: https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/5004" target="_blank">📅 21:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5003">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بچه ها بازی Rust نه. زبان Rust:))</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/MatinSenPaii/5003" target="_blank">📅 19:11 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5002">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">بیاید بریم Rust یاد بگیریم
لایو هستیم روی
🟩
:
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/MatinSenPaii/5002" target="_blank">📅 19:05 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5001">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">آپدیت جدید Aether:
توی این آپدیت روی مسیریابی (روتینگ) و اتصال از پشت پروکسی کار شده</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/MatinSenPaii/5001" target="_blank">📅 03:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4999">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">هوش مصنوعی و برنامه نویسی | آینده این شغل
لایو هستیم روی کیک:
🟩
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/4999" target="_blank">📅 21:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4998">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">حس می‌کنم شدم هوش طبیعی متین سنپای که پول توکنش رو نمیده
😂</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/MatinSenPaii/4998" target="_blank">📅 20:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4997">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">بچه‌ها شرمنده می‌کنید با استار هایی که میزنید. ممنونم
❤️</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/MatinSenPaii/4997" target="_blank">📅 20:44 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4996">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fk6cdVvRqCkNCMO30705VrsTFMLkiu2LiG1wtc7kBXOiezbwAs3JZXWVnGGsyWahBgGrBOd6zf_W_YbJqhL3nOAtM5k78OFoBRHpMvAwLzA_oFc-fBTsNQVpj98mUJRkKBGW03oP_yEcTgtzTvXklisQaFz6w-o4IG8rjGJWVkReLo8Tfti6tlJWoCs8WG0yKayU5pU1qvVVJupsp8fzVpy0TmTGEVNXHBmqu_7l9PYo6FuCSgQbme_d8LUguIZKKvfCZ7x-cfyZrR9Ca-aYzMjCx1CnOWwAaWEojlsYLn6Dh_OBVgRBOjU5WVNIS4gz05aXqoCp-R268flzoZDQyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/MatinSenPaii/4996" target="_blank">📅 20:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4994">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LBUitJuzIWq0CzWXfcQhesH8M58F8pJCdLNa2A8LUV9WqD7O4z7coa5PpXrFY5KhFGoZvlpddZDsP-DQkSb7O9mTJsehkl_ECxhA5xFs9CJPJaHnz4dEdRhnEvTqtLvti1ePLFt9ZPmm7wX4_1R6pr8_7HNZ8He3Z4VzlCtjBDAJWoYMROHfrpW95uQjvTKUhD2DJZz94wZYJWSKQN-JNx_MrvvQPPWX9ibjqhU_YevP-HX8FV6wUUvSG1DiiMfLMeiQMzd8RXks9frYhWLNsOu0d-98XPh8_pK9XXKLu8lA2aN0tmEjgFkg2yU-cJLPBh7EGb4xKsYAAd4FdPcTNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FpmDr8s6GWzgvv_lz2rKfxdkxRRVdY1ByNiVlZ27KGzwpNwRmANY0jYgP-wUf8lY8I6fXDwgf3qMEkflswqblsy896QGNl557lLYaOdXlRTNujXAj-r_UFNT_Ot_b6T7qDltsWFzTXpC-OWzBldabNPtQ9d_C3f1bRlB3qOdo5NdtevEpncZlJhbFFYOsabi0qvtoTkyASEU2i0pkoK_AKgAFG8TIgIkky6g4EI_NzcFAumKc3rFiBg4cGOH9qV7_MBhu_Ddh7FC_ro6FLhnDAnuzoEYNKTiLmWajR_oiZ0cp0EaKE_-aRaWCu32WPi8fgnCXCHkOHs5gny6XFJc-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/4994" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4993">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MWAc3H3aAPlgwnouMyZia1YBG7c8oBodI4RTD0khrSmM9vcVXoLajK2D5MEyLaqxrYxWU31dMDxXwywWqMfo3EfWdRqW-GgtS8VMBVF4AjbrObwyXc1i1eITim478uxgZuHqSzlqSiH6cgff-4gzD98NgJqHmdZP35Wl5iINHOOmDBpD3GO9HBGajq_Ufg50GA5d2rIoIFLQSI5XhmVOogcwmuWWs54kzdmaJvKWQ-JgFmdtXvCvm7aIhMBr-WEWCbxUTZ9AL0NwTEtXjq0YU5j_RJD6Rpt1IiRDKn490lfdj1CPtF1eTxvxxkfNnLChTV81lyMUpOkw6JFlqVdTZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cZrwHquH3gxdlA6jOOiSUq1c2Fm1g_6UF8NjqyQqpSYVyRSRuBIoNf-8FHM4YCBxQ1PK7BOtSr7ripUyNGv64UNcDSwq78Jl23Y-6dfnbbf2urlAaL-GpkWx2RylRmOQIOp7ImHbuMKX-qx2JnUlvELbx-h7KzrzHdpmSPg4RImm9Ax7KNxR9284y15qosyKNwWU-QK0l1HOL9uJK3rsfm4T9UnsAbCtcnfq1qE0UP3h9_K2yDj7WRRvfKE3lYoE6pyGteXHGBVoO6hlkUkpiQ3dVAwwMINQ2DtIq_4YvHTzpU9oja6b4SNjHmEZCXNnTKArUCj9-5pbF2wWf-G5Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجربه من از 5 روز کار با OpenCode Go
https://x.com/MatinSenPai/status/2089928470801318139?s=20</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/4992" target="_blank">📅 07:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4991">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/by2glaXVJMZBWUNPFINt6zrRqiAGGCbgOTnFD3CtuMWi4JsjSCpGm2ozYNI0C1Zfh_wzjm1ZDXpKwTFWcq5j19oFiRKIYf_12ak5EW3CZWJWP38TU-Siet7Q852PrTSyX_UkMkV09rSAtlb0D0y8UR3iz7YEQQ_Ko0QsJ50ZJQenTdR3wbKfa3TWUfWxUOrYgVEss-sxujEjW2PmGgK14hzADm3vdRMhHo7iVxihgiNhmCFFKmL1TOHFx9aAsrJwrmczoPNDAgbMa7DPzjMFcqcdWIv9pxgJ4JSwUIQD6lLE0JD6bIKDVNX6_1ZJpSqTNege6bklqwS2xXIsKnvOhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب پنل BPB + متد پترنیها + Chain Proxy داره بهم سرعت آپلود خوبی روی آیپی ثابت میده</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/4991" target="_blank">📅 23:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4990">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">لینک داشبورد کلودفلر:
dash.cloudflare.com
لینک ویزارد تحت وب BPB جهت راه‌اندازی:
https://wizard.bpb-panel.workers.dev/</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/MatinSenPaii/4990" target="_blank">📅 20:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4989">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Shiz3ON6i3-6wqSRGmH1gKrRD11oa9KBe0Du5o77WiKh_WQj8Cz0CDohYF3aZqTlnabOVUQ3F6EGvqCgAcpp9qRqtGii-ne1lYqEbCqyol8z5faoKKYhtUfPkCAOZyzccPQqApDTQEcS-sWvBAeVTDKNxXTAd7KNMznPKrq61N1QlGC9oGwM5yL8TbUshoBExdQiFT5v7iIEFLSoQmzcHihFsavBP-CM7gQ7H8G_zTD3txtoZldyNmpacAtyr1RkeaHMoMbcrcaRNO2hCRoCLZtgZlhJABZDcjRAHIX4wTwh4aBVy2aUYNeLyz96PHy-pBTKYa3avH4qkyNK07FZIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/MatinSenPaii/4989" target="_blank">📅 20:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4988">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ویدئوی BPB دیرتر میرسه و می‌تونید اداره برق رو سرزنش کنید
😭
😭</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/4988" target="_blank">📅 19:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4987">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K5HLXz69p_KNNVyLMGYFiDHbyLFpqDCfWU4uXfs32rfN3OPXM0NuX8XcoJmaO265TGkOqi_7asgQTSRoynImxVFDVEIQnjteSNhVB6SJaxdL8zgt6eUYzkxGra_Q2J1t9gDkv6XKBEyEKr_nhDxTUixN-bAp9cUsezkNlXKuL_RMjEpNyDOX1nFUePaEUcdIC6laY4Yk6pioM0SWwClUdyBSputJ-mCsib2LDUGayflYsConW7AOXYUOk49cmtVMp7JFEmmr8cAh3icYqx85UM5HZx6GoLPFeqHVPBZxie5AMmf_aYi5xOBmQU549lwNxw_39REFLCLYRGyrorAvdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteVPN دسکتاپ هم سرعتش عالیه. تازه با ساب خودش هم دارم یوتوب می‌بینم</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/4987" target="_blank">📅 13:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4982">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4982" target="_blank">📅 13:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4981">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIkogc_Qaap_3LqtjfaiOre1_eqbx5zjUApFFpAqyOMFV3JLrJ8_LFWyih1zYUv5An6H_nqT5_EowX-TaKkkFEB70kWiP1sMf78xh8SDX9OhJYAJTCwcvL57y2JrBeEYWIHXfmmujt5NvEI9QmworJKHzENSo_1OE8QkcqFcH2ZEb-Mbz_EN2LGh7uWn3QoOyoaaNgOXGpBCXaLBeilWA8ISM-9u0N_2g46iHfLaPI6rSAsXK50pI9MIdKdkjMwBWcGJsOK8--6gbWPTUZzsMwJJSD0IpPgz4fn4oG4lNx7eDaZ4LHssQs2mF-TjSy92mSLcvtNtWPLZ3y4_Z_0b4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/4981" target="_blank">📅 13:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4980">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">امروز ویدئوی پنل BPB جدید رو داریم</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4980" target="_blank">📅 12:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4979">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XOm2Sdp44eFJLVpn4Qz0MdDU425J-pApj15Prjx3jwRYjxZdnSHPAb-JSCjakEXl1QMHYyJsOv5vTOA4509-OWXmpsuLJA4ccI0vWY8WFZPDwKzOEf75DbnK2VETP12rvBLBoq9odUgJIggDZHkSby8EP1hpgzAA3dbmipsad0V3wtv4p_HfA_7efWGpQbMk43OkCqgAVZRpVfvziSVmwFLXE834JwvOJZQOdS6ryGPXyUpyzPDLdNZ-E7F8lF4IdQ-9bYL41LPgGigNFyqTsEiEMP6zP0gACylIpOhA0TB7pHR5TvqNGP-VymHpQGLEtfZj3q4r2RJOQzMnAZIDWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دمتون گرم بچه‌ها
مرسی از همه‌ی کسایی که اومدید
شبتون کانفیگی
😂</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/MatinSenPaii/4979" target="_blank">📅 01:36 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4978">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">بفرمایید لایو
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/4978" target="_blank">📅 01:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4977">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اگر دوست دارید استریم‌ها رو دنبال کنید، جوین بشید:
https://t.me/matinsdungeon
امشب یه لایو کوچیک خواهیم داشت که کمی گپ بزنیم و صحبت کنیم راجب اینکه قراره چیکارا بکنیم</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4977" target="_blank">📅 23:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4976">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ec6_qfrWNR6hyfEOSiWJVg0t_3pfDFZXSLWkvO2u-s6OtRlATnut-aYT-hZ0LV5-VM2hDsB4vOWt7bzuVRLgSNfuLrhFoJahuX0B7YN8by5LXsfl927vLvG8OkPNVmj7VY8CUzzQ4WInok61wR7iNfpaPVtsiIrkID1N1EE2V07GZuZQV6pg6JDGxSQtlVLq0knuK2unMx5QXf4784YiO82CHRXk1uzOjUeGWT7EfS6gro6askHRTBf4vGuh2-Njxaruj7RdkHU7R82LYk9B3_0hoiI6iEkiS5iJYEE7CxAVh3AWln1ekBusFvVxL4g0tRu8nwMDuBsqQSIQnJAN7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/MatinSenPaii/4976" target="_blank">📅 23:06 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4975">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IWMbLaqvN1zcRWKBd2D-gkRLXak_3eWdqvfBkNJpOoKReMWE2GY9Bwk9jFvp1sRKDWau2q3DyedNTTke7j8MBCvKqA3CglpmDht4Oy9YVy12OEpFMqtWSI4DzXYm3u1QhXCQEL8TV6xwBjdRwQoM39DcPPCEcsXlUe0fmoa6kcVI9Wg59SiE1hJgFDk-x0ekau6RWxEM103R5VMjZ-Q8axiySO_LmE5GeLDdj10Uwwgj5uoPB0hDmL5mX4eBwuqUdbxDqc_c0EGTPD6F-RwKJAIit_Gk-xg6ajhIGF_H9Js3gNarzufzlnMUYWp4KZd_QZPKwcvbTAt3dR3X0_pYvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته‌ای که من فراموش کرده بودم توی ویدئو بگم، این بودش که برای حل مشکل آپلود حتما باید Fingerprint رو روی Unsafe بذارید
عذرخواهی می‌کنم از همه بابت بی‌دقتیم
❤️</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/4975" target="_blank">📅 17:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4974">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r-Ei7rU2OmoLuq8lS2Eirw7heYN4fsfCX3QBoYvTuNdC8FnNPJFqKA-wtOLYAYZUALq-sC2AAX6kJBGJS0jjTiaAGIxVMT5yLc3T9jlQzeOqn_mlnlD9jZJMXwlX5uofypzO3KHFRaaLvism9lWwEnfIAT51CT0z7SadsNcxYVMscnF4uWmlHLK82J8REjSUkd_2bu5VivXxHX0DXsp-BWC8QUtJSgt49npgZWERMdYDlmPc05rfSHI_LUYlXKr6gMFLcSlg4xKDcmgv5KXdiharQxgOKyu0s9oAQO5KO48ybLJFLppWqbLtXnyW6lBCrL-meCUefKL8HIslFgA42Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب به سلامتی تا ما ویدئو رو ساختیم رفع فیلتر شد Worker اما هنوزم ویدئو رو می‌تونید ببینید سر سرعت آپلود خدایی که این متد پترنیها میده
🥰
که وقتی ویس می‌دید دو ساعت صبر نکنید آپلود شه
و متاسفانه ممکنه بعدا دوباره بزنن ورکر رو فیلتر کنن</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/4974" target="_blank">📅 11:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4973">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/4973" target="_blank">📅 03:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4972">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BVSn9oTGM5ap1EmiQGZegPhPG1JOeFBVpAP2ISd6LYml-TNd0DDhZl0pils0hpuyxvYTT0c41vBCPE4TnTjsKQ1Pfcjlv_R2Gh3MG1gvOnusshHRobNtJilsosJl2Ijsq-E0Plfv27apodkzaMhVhkHHG8j-BEESnM6KJb4aFV843iXrOYMHt2zYjsYV5oKwwy5p8C-kr11jDvQ8F-RLBv4tM1RO45By1JnlbDL4GJG2o3JT4CWWamjnEr8TmbBL-fm7c5FX6F8US1m3A3L8rBwdcNl6XTh13SGJQjD1qFYK4kmxc_hBgRhiMmLEfmRM-U3dn9Qy9YU0x1zDZ4I1oQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/MatinSenPaii/4972" target="_blank">📅 03:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4971">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ویدئوی رفع مشکل آپلود کانفیگ‌های کلودفلر و دور زدن فیلترینگ
Workers.dev
در حال ادیت توسط ادیتور عزیزه و به محض اینکه تموم بشه، آپلود می‌کنم واستون</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/4971" target="_blank">📅 23:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4970">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UnCEnFg9waRJEbJI8nLN8z1m4Z1ZCJPG1GG-KtoWi3sj9xOvcSf9gHbpGR9aoVL9E0BP8RT4dCOq4i7PNPSkpo_Wylv9bYi-VSmszPYaN-tpTcWJwNZBWH2LzaoxhebNmsRmc-scbwNkYRnTSuT0Wii8Weg3JIQokwyLSXBuxbGDd9Z9JN9fyaf6zRmB-b8MdXRDAfwGhEcZYiXvywV4KkXnydyU3ec2dSxJUhl_MOHxfxe6hRo8A0SUU_ofOV79lZztU8z5K9pFpwK8mNQzfFFCO0tcEg_Uoi0v_Bg8FGDo1C09SODMICYLwQIONe7_sjc3-WPM1oN-ew93jyLuzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیزهای باحالی قراره داشته باشیم به زودی
🔫
از
🟩
می‌تونید فالو کنید اگه دوست داشتید:
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/MatinSenPaii/4970" target="_blank">📅 19:57 · 25 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
