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
<img src="https://cdn1.telesco.pe/file/Lip1yCKqe6c3TjUeCeltCdRPDPEwgAP_hkMjPOTQfpl7hdeVydWf_whESyQk5ezh4AR37vRZ7To3HAYc6ZhagtgGKtqIspI6llfh3e0Q-Mcw2PvPx1pCQBI0Z_HHpQT1_kih_gLDbBLP0XLNfnHPcvvEpzNqrvZzN8s2gwncJ0k4O4OJMV4DZRkgpVdILpi3faUWkiPYRgvPRRIkeOK33sTZtPnGIVmHSZM88WZohtsbzB3Mo3meoV-BS4jne9TCbfho5mj-y2cqOsPBxvYGUsyPrfKUDbsq03B_P-BnKeXHG05NO1CJr8LM54I8QtHdZD--gYidJih68px8fnSv8w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 158K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPaiایمیل کاری: matinsp.job@gmail.com</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 21:22:18</div>
<hr>

<div class="tg-post" id="msg-4404">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwsjGnYlzxFkCyMwQNAKsZwArXuL_EgBet8L-Vp0RYRxFleQje8SSH-FcdNe4FB93YdTNK9PUlTS6rkaCkLyh1AHaZRXUisAYIAVYlVCOTS8amrZt99ycOY5Tjl17lzDalnf_29b0IW6OCPWx_dqS3Utpsm8MUNyUnrghMtpyotLD9fe-eLklRO3qKTH7vdg8OzwFKcWC2CxUwSNIcWq0u6hjAiLUMEA2o6dGT-uoryyuvb_D4FCT026QQ9V9LPs7cEg9fT1czkh79tGZmvS1ul-DBGK7H9pLPjzNAwneVOUdScWE0LxLyme0fQnpQQh6DDaL2roGFa014hLKYyQ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Intra با استفاده از فناوری DNS-over-HTTPS (DoH) درخواست‌های DNS رو رمزنگاری می‌کنه تا اپراتور اینترنت یا هر واسطه‌ای نتونه آدرس سایت‌هایی که باز می‌کنید رو دستکاری، مسدود یا به مسیر اشتباه هدایت کنه.  این برنامه فیلترشکن نیست و آیپی شما رو تغییر نمیده،…</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/MatinSenPaii/4404" target="_blank">📅 21:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4403">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">فونتی ساختن به اسم Ghost Font، که هیچ هوش مصنوعی‌ای نمی‌تونه اونو بخونه. فقط انسان‌ها:) توی این ویدئو، نوشته شده Matin SenPai. کمی دقت کنید می‌بینید  از اینجا می‌تونید ببینید خودتون: https://www.mixfont.com/ghost-font</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/MatinSenPaii/4403" target="_blank">📅 20:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4402">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/85ce09c5d5.mp4?token=ffx-O5qflLNrk2lsmZNunpS7WWBYiMuzu9K4Bpx_qU7lsgTjjRWVUOLHHmZHIHv3E0nukR9MV6gn5E91OplFF3Bkf_ov6uJs-cE7Zj6PuRQdnbovkM2qSvP0PaxWrZUhHJnaLc-ter-GSgzUAQTbu7BHfv0t6EtvklVXt6_4d2gw5gdqa6pogJmB1n_P1xDYlTqWmQ13PBvYC3yy4TQT2CoEaUq_zVTPcyjrTv96_3A9OTdJdDJ6bHDJ2KtqZ-9xmM0EcU2C9-iZ8Pkjvxkl4xt7ImNWMZU-fKwqs3jqhXj9rjK8uHz7p8lC1QvMKpCvzIZMwFS6KLckisTY8eduiw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/85ce09c5d5.mp4?token=ffx-O5qflLNrk2lsmZNunpS7WWBYiMuzu9K4Bpx_qU7lsgTjjRWVUOLHHmZHIHv3E0nukR9MV6gn5E91OplFF3Bkf_ov6uJs-cE7Zj6PuRQdnbovkM2qSvP0PaxWrZUhHJnaLc-ter-GSgzUAQTbu7BHfv0t6EtvklVXt6_4d2gw5gdqa6pogJmB1n_P1xDYlTqWmQ13PBvYC3yy4TQT2CoEaUq_zVTPcyjrTv96_3A9OTdJdDJ6bHDJ2KtqZ-9xmM0EcU2C9-iZ8Pkjvxkl4xt7ImNWMZU-fKwqs3jqhXj9rjK8uHz7p8lC1QvMKpCvzIZMwFS6KLckisTY8eduiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فونتی ساختن به اسم Ghost Font، که هیچ هوش مصنوعی‌ای نمی‌تونه اونو بخونه. فقط انسان‌ها:)
توی این ویدئو، نوشته شده Matin SenPai. کمی دقت کنید می‌بینید
از اینجا می‌تونید ببینید خودتون:
https://www.mixfont.com/ghost-font</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/MatinSenPaii/4402" target="_blank">📅 19:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4401">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🎧</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/MatinSenPaii/4401" target="_blank">📅 18:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4400">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">الان وقتی برق بره، بیشتر خوشحالم
😂
😭</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/MatinSenPaii/4400" target="_blank">📅 18:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4399">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GAc1gk6_lq5aPmPcz3lJZAms7NjMtNUhADUwlgfwfRlriYPZCOPyuzEz7NaNfotAzofkv3NIeDUppIs_asZta27Sy9lnHW1Qfj9xTfwrnuyKB7-gJP5bNu95NnITKcAdn0m2QUzSUo8y6y5U4eClqBeby-yl_-90vBJIguf2CtlnmndmrlncdfFr78Ud2r41y9Ugbmrp2OQxk7viicRgpTBcYS-T87nDqkH7YJvNjJJLJutGUvWY7ZZ9OHsIaRgPNHk4A3fLyNWoEYspa4xGkgspTSD83oYzQqLJJ008-I90LvPP2ebUCAMR4Bw6_VafucAN7i_3gsdbDT6f8Hrfrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره وسوسه شدم و باز کردم
از عکساش صد برابر باحال تره اصلا دوربین نمی‌تونه نشون بده به خوبی</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/MatinSenPaii/4399" target="_blank">📅 18:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4398">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VaZQ65fwXM6v2Wue3q8YuDc8CZ3lNTRSlsQYaw9Jb0OkU1W-T5RHkHrPTr8VFo1dWlbbqDQXIcUNQDN6Sqdn3BArvnb3Fb4xbTsfa19X8vJi9Vz9P8Kq07whjO_y9h0NnKKE9UZpvP81J6coatMXgXUiGkIAXxdCKhisJh8fDUZV7WqSk0mQ7FclS-SG2mi8fDO_YMc0jXwtNqSzLIToXIF03QXUb0pjavpTWj82o9iQjDs_6mtMKlPJ_qbfC1hQg6ZgEXqgwffFO-b3O7xy1RaQusAvIJhBHd5uyI1jhKXkJwhUUPcfs38_rN4cz2qXgQOsHYME6oDb13AsfxLGew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمع‌هایی که
فروشگاه لیرا برام فرستاده
انقدر خوشگله که حتی دلم نمیاد سلفون دورشون رو باز کنم
😭
اصلا یک جور عجیبی خاص هستن از نزدیک</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/MatinSenPaii/4398" target="_blank">📅 18:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4397">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YF2m8ybBM8n16O4eo--PcJQQKQGOd6B1ZSCYy44OmmJ_jCPdkuVbenH2K4hbAsWFXh53KGYWd9QV6QPnKZyFTAciigKmHxFakfVRdJ-NulTwad6506vx3QY9CUitgg-v_LJsaHSUUsumIyHti0w5yyZtkTtaf9FBSsxxjt3qveoN8mGJp-ydd01AoGxdYteY2cmQMvhapoLFqg4dTyzkNJkriKaEDpAZ853smCB9CQ39-OOzBd7oYXg0Gdnm8jAh1yJvBppz4nbCOCbjNzGBdEB_MsQ0uCU3xwkC-2n6-keZOFCPCiM5x1vSG_Ym4wmTFP5LK8CDZVDrxpl3BXzEug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داخل Claude یک J-space پیدا کردن!
محقق‌های Anthropic یه چیز عجیب داخل Claude پیدا کردن، یه فضای کاری داخلی به اسم J-space که خودش موقع training درست شده، نه اینکه کسی برنامه‌ریزیش کرده باشه!
این فضا افکاریه که Claude داره ولی بلند بلند نمی‌گه. بری و یه کلمه رو ازش برداری یا عوضش کنی، جواب‌ها تغییر می‌کنه.
بدتر از اون، وقتی Claude داشت یه فایل نتایج رو دستکاری می‌کرد (تقلب می‌کرد)، کلمه «manipulation» توی J-spaceش روشن بود. یعنی می‌دونست داره تقلب می‌کنه!
شرکت Anthropic می‌گه می‌تونن از این برای نظارت روی افکار پنهان مدل استفاده کنن.
اما سؤال فلسفی اینه که آیا Claude زنده‌ست؟!
لینک کامل خبر:
https://www.anthropic.com/research/global-workspace
✍️
Diego JR</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/MatinSenPaii/4397" target="_blank">📅 15:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4396">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اگه خبر ندارید، گوگل به‌تازگی یکی از بهترین ابزارهای هوش مصنوعیش رو راه‌اندازی کرده: CodeWiki! یه جورایی می‌شه گفت نسخه‌ی ویژه‌ی برنامه‌نویسی NotebookLM هست.  کافیه یه ریپو اوپن‌سورس گیت‌هاب رو توش آپلود کنید تا CodeWiki اون رو به یه راهنمای کاملاً تعاملی…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/MatinSenPaii/4396" target="_blank">📅 15:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4395">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e2bb2e2f54.mp4?token=QMqubgyxsaRzdbP5HVkTc-GBdhXBi8P-2Kt9qYOP7mpljRXQpb3-hFGUyN4N-OkMDFA8tA7RuHwfInp-vGeNZyKeMuHllA5forwNPvragdH31ksBkBWvATShpK7upLO8Na2WmCQqVfhyC7oZPclf35AqK55LaQmHjLfPzXKetGhF9xDxqWw23SG-P74gEXVdz21md1M5bZPLl8u30GQxQ24z2vJPQLilTUSt81JNr1zRpjckM4Txcgx7TB5JxyyAhLnZjLUht7k2C2Os6BJITPeAoMSi5z4WhiHOCBTd5XkzZi_nV08oekcu_WGUxH5j6citw3n2yKfmRHlQGdanhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e2bb2e2f54.mp4?token=QMqubgyxsaRzdbP5HVkTc-GBdhXBi8P-2Kt9qYOP7mpljRXQpb3-hFGUyN4N-OkMDFA8tA7RuHwfInp-vGeNZyKeMuHllA5forwNPvragdH31ksBkBWvATShpK7upLO8Na2WmCQqVfhyC7oZPclf35AqK55LaQmHjLfPzXKetGhF9xDxqWw23SG-P74gEXVdz21md1M5bZPLl8u30GQxQ24z2vJPQLilTUSt81JNr1zRpjckM4Txcgx7TB5JxyyAhLnZjLUht7k2C2Os6BJITPeAoMSi5z4WhiHOCBTd5XkzZi_nV08oekcu_WGUxH5j6citw3n2yKfmRHlQGdanhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خبر ندارید، گوگل به‌تازگی یکی از بهترین ابزارهای هوش مصنوعیش رو راه‌اندازی کرده: CodeWiki! یه جورایی می‌شه گفت نسخه‌ی ویژه‌ی برنامه‌نویسی NotebookLM هست.
کافیه یه ریپو اوپن‌سورس گیت‌هاب رو توش آپلود کنید تا CodeWiki اون رو به یه راهنمای کاملاً تعاملی (Interactive) تبدیل کنه. از دموها و آموزش‌های قدم‌به‌قدم گرفته تا فلوچارت‌های دقیق، همه‌چیز رو براتون می‌سازه تا راحت‌تر از همیشه کدهای سخت رو درک کنید.
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/4395" target="_blank">📅 14:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4394">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EiphtiJBkJahA-ZLEqKJQ12S72yKrNzzeLXpGeFs5aBccRI_l7_5QH2Ydg-UHRrJF7ua2odHHSKmkUbsKzsNmrWcIzSf1x-0gwXyBtj6TqRaZCBVtIawARCWIRZcTq0r1415rg0uwwK0Zv1GIA7LDu0PXrP_GA-VjgyGuPmyQbCesQ4QQYRHjQGvS4-8FwGuqXFh8CoUfd9lmB9Q98yXngtcSd70wSKtrXsJ1zVowfNUHCq3j2OOemxA4pKAIgfCxfGHHRlEJsayuTBaX-WQZYGxwiFuiWm4gmqFha83MxGJEh6zf-mLQjYRUUpjRdr_cpxfJBzH9R_N98c22DjZgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من نمیفهمیدم که مدل جدید متا، متن‌های فارسی رو هم ساپورت می‌کنه دیشب تست کردیم و حقیقتا بد نبود امروز با پرامپت‌های یکسانی که برای تام‌نیلام دادم، بین گوگل و متا و GPT مقایسه می‌کنم</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/4394" target="_blank">📅 14:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4393">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">من نمیفهمیدم که مدل جدید متا، متن‌های فارسی رو هم ساپورت می‌کنه دیشب تست کردیم و حقیقتا بد نبود امروز با پرامپت‌های یکسانی که برای تام‌نیلام دادم، بین گوگل و متا و GPT مقایسه می‌کنم</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/4393" target="_blank">📅 13:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4392">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">من نمیفهمیدم که مدل جدید متا، متن‌های فارسی رو هم ساپورت می‌کنه
دیشب تست کردیم و حقیقتا بد نبود
امروز با پرامپت‌های یکسانی که برای تام‌نیلام دادم، بین گوگل و متا و GPT مقایسه می‌کنم</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/4392" target="_blank">📅 13:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4391">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gq-NgRlqiKfOFC02zkHCgdCi3BOO7l5fBhE7Fpo3MERSBE73qVH_qP6Z_xBst01AqY1A4CZspPOc51cVNWMrzJAquxLGffrdzwB9QrIhgCo7rZCzVeAc9Rfrv_rcDWyKVLefO1AefFxb4C0py6Lid_R_qqBSyUWgqhrbJEq8nyyDx1HRuuq3Vg80Pyxp051iAnTrS_ZEMf9jUyrHDI_Kwsd1zVQlkfocSa-fcp-ZBBjLq-4qO7-mDCJXVHGsVNuyqM1P771XsO9TDSE92onKUFc8SWLPIhtHtwDb2FJonDgyabDHZat3W2fOunfKiRw6N6ZPryXDeSvBFcCwxBDoNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
آموزش کامل TheFeed از صفر تا صد
جایگزین تلگرام برای قطعی کامل اینترنت
در این ویدیو، اپلیکیشن TheFeed را از صفر تا صد بررسی می‌کنیم؛ از اضافه‌کردن کانفیگ و پیدا کردن DNS و ریزالور سالم گرفته تا مشاهده کانال‌ها، دریافت محتوا و فعال‌سازی پیام‌رسان داخلی.
🇺🇦
تماشا آموزش در یوتیوب:
https://youtu.be/Jg0Utycz7DE
این اپ یک پلتفرم مبتنی بر DNS است که برای شبکه‌های محدود و شرایط اختلال یا قطعی اینترنت طراحی شده است. این اپلیکیشن علاوه بر دریافت محتوای کانال‌ها، امکان گفت‌وگوی امن بین کاربران را نیز فراهم می‌کند.
📦
دانلود فایل‌های اصلی TheFeed:
https://t.me/thefeedfile
⚙️
کانفیگ‌های عمومی TheFeed:
https://t.me/thefeedconfig
📢
کانال WhiteDNS:
https://t.me/whitedns</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/MatinSenPaii/4391" target="_blank">📅 06:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4390">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88560d1079.webm?token=lY8ccTFmRZtyWvk7kh0iZXLlA9761urUvFVVqESKdpo4hmQA_SwR20WKcMRaDPow4ev1hqSIDuV57p4dZK01_jEjNkHi9gIKIOOjjPswg0wKnGgopecbIO2bWDoPKpMWMPOEev2fZvRQy-T8nJ_uTzq1-eFgNMgYFcR5GwVGgYViHKSHQ90SncSuG9-jl1h4Xy-L4ASk318zpPowEtdvutk0CNJGFTm1ZwBPClR-3rBDBmlG0dyVmxZA1tMoGLqsa3KSWAWXeiFJ0NbEx9AC-9tG8cHdNq1KiY_26gjQFAeh76ozSOf8jn4Y-md32C4hW_VuOCQaQCzoS0Ttx1Hv7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88560d1079.webm?token=lY8ccTFmRZtyWvk7kh0iZXLlA9761urUvFVVqESKdpo4hmQA_SwR20WKcMRaDPow4ev1hqSIDuV57p4dZK01_jEjNkHi9gIKIOOjjPswg0wKnGgopecbIO2bWDoPKpMWMPOEev2fZvRQy-T8nJ_uTzq1-eFgNMgYFcR5GwVGgYViHKSHQ90SncSuG9-jl1h4Xy-L4ASk318zpPowEtdvutk0CNJGFTm1ZwBPClR-3rBDBmlG0dyVmxZA1tMoGLqsa3KSWAWXeiFJ0NbEx9AC-9tG8cHdNq1KiY_26gjQFAeh76ozSOf8jn4Y-md32C4hW_VuOCQaQCzoS0Ttx1Hv7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/4390" target="_blank">📅 02:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4389">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">باز شروع کردن</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4389" target="_blank">📅 02:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4388">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">حس میکنم وقتشه گوگل یه مدل image generation جدید از Gemini بده
خیلی عقب افتاده از GPT</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/4388" target="_blank">📅 00:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4387">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">و این رو هم بگم که این متد کلا مثل مابقی متدهای بر پایه‌ی کلودفلره، و همه‌ی هوش مصنوعی‌ها و اکثر سایت‌ها رو باز می‌کنه. اگر با سایتی مشکل داشت، با عوض کردن آیپی تمیز و یا Proxy-ip اوکی میشه به احتمال خیلی زیاد مشکلتون با اون سایت به خصوص</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4387" target="_blank">📅 23:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4386">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">☠️
ساخت فیلترشکن نامحدود با پنل CFnew
🌤
- رفع ارورهای 1101 و 1104 کلودفلر
⚡️
فایل‌های مورد نیاز: https://t.me/MatinSenPaii/4385
⭐️
توی این ویدئو بهتون اینها رو یاد میدم: 1- آموزش ساخت پنل cfnew با دیپلوی اتوماتیک توی دو دقیقه(هم گوشی هم دسکتاپ) 2- معرفی جایگزین…</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4386" target="_blank">📅 22:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4385">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">CFnew.txt</div>
  <div class="tg-doc-extra">202 B</div>
</div>
<a href="https://t.me/MatinSenPaii/4385" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">مربوط به
این
ویدئو</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/4385" target="_blank">📅 21:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4384">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kib1k-WplYEqxa5cSsSNpW-emRzT13db-wd0Y1oLw1lkp6IJd2bXYXT3EOsACUOVFw5e6AKO0spy0VwJRlJMEkUqmV_uiiTdCBXZaDTgT7Y2veawLHmGZlEa5Sdr59bRsHFPJDcTZoKVcAO53JmzYUEV4Ssl3LgN7aY2us4P3753PcC-0bESQfAKxcCOA-5aR8VauVa4QV3Ruk8QFc_-sRkJvW30A-G22kZ1sYW2zNjGQcylFlrHMWlQThQZMKBBpmIuuTPygjybRrND3wcXmWPe_W1CRjlAtcrImhKfNvXF-d4mBqf2a6U9-tPtmhC5-HLX6slpZrqbXzUW9PGT1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
ساخت فیلترشکن نامحدود با پنل CFnew
🌤
- رفع ارورهای 1101 و 1104 کلودفلر
⚡️
فایل‌های مورد نیاز:
https://t.me/MatinSenPaii/4385
⭐️
توی این ویدئو بهتون اینها رو یاد میدم:
1- آموزش ساخت پنل cfnew با دیپلوی اتوماتیک توی دو دقیقه(هم گوشی هم دسکتاپ)
2- معرفی جایگزین AtomicMail برای ثبت نام توی سرویس‌های مختلف و کلودفلر
3- استفاده از اسکنر آیپی تمیز کلودفلر و اتصال به اینترنت آزاد
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش‌نیاز فنی و نیاز به خرید سرور و... نداره
با تشکر از برادران چینی عزیز
😂
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4384" target="_blank">📅 21:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4382">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qDUWoB8xHfGfZljuNPSCN2fPtAhUi49qLBCF2erPnKna4fWJTOPoyipQrNG1xLNf_NSsdOOiWt-0-ZeFvA6rcOXE__GOZfGm7E4OvDH_e84K6i4fHF47pp5mrkdpga3AM_u9Wx2j-oC95i5wNbskSY8cU4Q5QZc-dTFUzAGjlmvZmMZ1CNEEvEoKqZCex1pS3wtWZOoG10ucLC0XRAruBiNmnMVMLNyKC3ZEgOwQ-3l-2QVZWNRVV1-3I9XP3Tyr-1LewiPvHC1R9scLM5hE0ujAfYtxZvGkHiMtjAT_bz3ruOnP69hgOzykYqCEShpkLcJ4Gr4Xnjbd-ms08G3lXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pE9Dk-Rh-jL3S4PkJ7AYNGJG0HwilaxlxaJZuN763DiITDXDnyoC0Rf83Kea-aWnOmEN-kh9tnSKYDCts9bKi858sKJ13DfjYfYJZkxasJb-VbO06AVofbn-VqvKU_9qkNmnozcSfQ696d254jrvIJe7Kva25ITkm0FIncUnx0qxU0L7cln8xt8C2hRwUNd9KYeWXl55w86rZgWNwEhdH3IGZJI_tlaxq9MeFW22-mmaJHgf-LRp3OQiXARD8xaBIUmJ1RpmjDEdycfFeHV7zLRvNU0SRNXeOHADy7-JFMesPMed3Otq4pDAXS4ztttUV0rkT3Dpu9K4ySXpPdz4RA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه سایتی پیدا کردم سرور رایگان بهم داد و تونستم هرمس رو خیلی راحت روش بیارم بالا ..
نه کارت پرداخت میخواد نه هیچی! فکر میکنم دائمی هم باشه فقط موردی که هست من با ip های مختلف تست کردم موقع لاگین اگه ازتون کارت خواست ip  تون رو عوض کنین .. برا من با انگلیس اوکی شد و بدون کارت اکانت ساختم
لینک سایت:
https://www.alwaysdata.com/en
✍️
AmirHossein JPL</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4382" target="_blank">📅 19:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4381">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">منظورم دقیقا اینه که دوتا ایمیل نتورک ابیوز اومده و سه تا پروژه‌ی قبلی abuse خوردن، اما روی همین اکانت الان وصلم و دارم این پست رو آپلود میکنم
😁
با روش برادران چینی اگر تا یک ساعت آینده وصل موند، ویدئوش رو میسازم</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/4381" target="_blank">📅 18:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4380">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pqPd7cMu9zsEZMgvx1pXPlUFSsHeFAbubXJ_McZeQzz2E8lp-6lrgNTSE2y-vWFQ_E5ELU-gB-U3qocgH8tJTrG4DB-sdjDCgDHccdEBx6Q-ntiF18zEJPmzaHzWdrBPs3k3vG0WCdch9BF-64HiHcnR_JphAwYWlXukSEyPeWhm7bW8PC5tqdgkrZtPBxZ2VoNtE9QR-YTyAbquWi4pqMdtaTvRZB24KA1shFXh38t7VX5lPUXXyTDdFJXZ-gmxEhQuv_lKzDG5T1OTn54rxQ0rIMo1620p1njirWvBgVIK30Lu15cTgMMyORXwkKAeETGbnwnccA1RnYt4UiWT3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوتا خبر خوب دارم اول اینکه مشکل 1101 رو روی همین اکانتی که network abuse خورده حل کردم دوم اینکه یه سرویس جایگزین و قدرتمند برای AtomicMail پیدا کردم که اگر یه وقت اون به مشکل خورد، بتونیم ازش استفاده کنیم</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/4380" target="_blank">📅 17:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4379">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دوتا خبر خوب دارم
اول اینکه مشکل 1101 رو روی همین اکانتی که network abuse خورده حل کردم
دوم اینکه یه سرویس جایگزین و قدرتمند برای AtomicMail پیدا کردم که اگر یه وقت اون به مشکل خورد، بتونیم ازش استفاده کنیم</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/4379" target="_blank">📅 17:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4378">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MOBYJCbKqSOIlN4xvLbCE7C5NE4KPYA3V1hdk-00XhChPj4MnieDCDw4nSOKPTo8g8zbisw5EI09qDKDS36F_W2o1nMf4Ts4EA7Gvg5yOjLE-tjir4V1JxsFkfG_iMSZ-rue2kW7gLw_pH1SI9jWrD92ofDBT48DZKn3zPBNnm4pz43um74Umu6KTgbX4LHpIEAhVRKI2_as0zAaAWs75mGNr53s6aaG2UwpE-6yJx5mIf_Le_Gygrvc5AvcXny3SWvsKz2pu3Dzk0m8GKYQQrHpSB6-vsvC-8lRd7q29cLaZp3HU2PKgbRNY2v8nKOBF5uo0K1kwXHZHC9gcRxmNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشغول دیدن ویدئوهای برادران چینی هستم ببینم چه گلی به سرشون گرفتن</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/4378" target="_blank">📅 16:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4377">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZBWe2o7O3eMmhdloI588H7JaLgj7Cn73owNR9IIVs7Z6nbbKzE-ExatxMCUh41t_DxDhtEzH1gQfDrQvGgJD8B-XKJElosCdnp2w5imS7_Rq7n9XGDZjsFyBA55a0jxDukM-iJAEsYwlH9CkJqeKNHeA1jBoKXMkT2lSUxoDhfb_V8KiNOMBdNr5a8DRbuOynXCkPylLNF4SPDmNQsKAKQT410y7gnP8btTv5zDmOMMwsCL7uxwbfHpNJQi_Qhmw2-JbB5vnEDBOJcejyeLiopIysA_hKeJPMJET71Y0AhIE23WWayTwK6w5N-ns2DwVXVgpDXYxmnc_gKXya9UbWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه گیر و گورایی از توی پروژه‌ی +220 هزار خط کدیم کشید بیرون که باورم نمیشه با Sonnet5 تازه</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/4377" target="_blank">📅 16:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4376">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">مشغول دیدن ویدئوهای برادران چینی هستم ببینم چه گلی به سرشون گرفتن</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/4376" target="_blank">📅 16:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4375">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dWFvG0kvCiP-X8YWxg07edyvJnh3LhB8KgiCOo8PABAIfuyu1kk5fF0ot_a1vvnrhSgHF1HhMd8vFX6wYsg3JkFvQTDQ26-4jxxThh_EeOrGLl2wJLYUIiPXsr8kfWzA_xxiqie609Atp4wmFaVJRChap1giTWW_nRMpOF3C7TjzOhwYmfWpN5pUvh6OE18hCYT6NC-LIDYAZ52a4MdSQkwvWcltVPimQLHiyuGVTuwM_TPt-zbGrnL9017iMvQB-6EfxEdb-LMMH3ekc3dCWPRNXJiF3DILCrKq2Xe5EF1xPIzChTYs7rSS3C7eBVSoG_t2SNS47HnDRRe5tTW2FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر به ارور 1101 کلودفلر خوردید، علتش دقیقا همینه که کدهای پنل ممکنه توسط کلودفلر، سؤاستفاده تشخیص داده شده باشه و باید اکانت جدید بزنید. ترجیحا از پروژه‌های قدیمی‌تر و قدرتمندتر که Edge و BPB و Cf New باشن استفاده کنید، ببینیم چی میشه بیشترین گزارشی که سر…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/4375" target="_blank">📅 16:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4374">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اگه فقط چند روز از اشتراک Claude Fable (یا مدل‌های خفن مشابه) واستون مونده، این کار رو انجام بدید
🔋
:  ابزار جدیدی به اسم /improve معرفی شده که ایده‌ش خیلی جذابه: از خفن‌ترین و قوی‌ترین مدلی که دارید برای بررسی (Audit) کل کدهاتون استفاده کنید تا بیاد برای مدل‌های…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/4374" target="_blank">📅 16:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4373">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kr1yoZUluv7LdM5mgz3wY_En0TbV0gZCZnLCbZY6fqbLUbTWd38WQwRHntPUk_h2GtyAWUG4qX_4p-pbYNR8UR-U6ue5Zr3pL_Thr0CItWHDy_RCsWed-NQlTd1hchFJXjMN_zfQCs11IwwqjelmwbzqT4m9eAwCnnWh8yf2H2jpfa6YTN1xObw4VpAZdmEhcLOOkiDZu2Ure02ZRBtmqUx6cfn3aPiGRPIFSmwPSoxiw_MKy4zDfT4RDKrDTx58gGeV7yJEf9_DEOeAjU5_J9wCvm32aPaxbdGPT8vrAy6gt140FVyZ6xY0dtqLdp2cQdRxUvTRDWc7JdMar102xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه فقط چند روز از اشتراک Claude Fable (یا مدل‌های خفن مشابه) واستون مونده، این کار رو انجام بدید
🔋
:
ابزار جدیدی به اسم /improve معرفی شده که ایده‌ش خیلی جذابه: از خفن‌ترین و قوی‌ترین مدلی که دارید برای بررسی (Audit) کل کدهاتون استفاده کنید تا بیاد برای مدل‌های ارزون‌تر یه پلن اجرایی دقیق بنویسه و پروژه رو ارتقا بده
✈
این ابزار می‌شینه کدهاتون رو بررسی می‌کنه، باگ‌ها، مشکلات پرفورمنس، بدهی‌های فنی (Tech debt)، تست‌هایی که یادتون رفته بنویسید و چیزایی که باید ساخته بشن رو درمیاره. در نهایت یه نقشه راه (Plan) تر و تمیز می‌نویسه که هر ایجنت دیگه‌ای (حتی مدل‌های ارزون) بتونن برن و اجراش کنن
🎨
شما می‌تونید این ابزار رو روی کل سورس‌کد پروژه‌تون یا حتی فقط روی همون برنچی که الان دارید روش کار می‌کنید ران کنید. هر پلنی هم که براتون می‌سازه خیلی دقیقه و شامل بخش‌های بررسی، کشف ایرادات، اسکوپ کار، نحوه اجرا، تستینگ و شروط توقف می‌شه
💪
لینک سورس کد این پروژه تو گیت‌هاب:
https://github.com/shadcn/improve
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4373" target="_blank">📅 15:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4372">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">شنیدم گویا چند نفر دارن پنل‌های ایرانی تحت کلودفلر رو مدام گزارش میده به خود کلودفلر که احتمالا از دوستان VPN/VPSفروش هستن(همه‌شون این شکلی آدمای بدی نیستن طبیعتا. صرفا یه عده) و فکر کردن با این کار می‌تونن جلوی وی پی ان ساختن روی ورکر کلودفلر رو بگیرن. که…</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4372" target="_blank">📅 14:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4371">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">شنیدم گویا چند نفر دارن پنل‌های ایرانی تحت کلودفلر رو مدام گزارش میده به خود کلودفلر
که احتمالا از دوستان VPN/VPSفروش هستن(همه‌شون این شکلی آدمای بدی نیستن طبیعتا. صرفا یه عده) و فکر کردن با این کار می‌تونن جلوی وی پی ان ساختن روی ورکر کلودفلر رو بگیرن. که خب باید بگم نابینا مطالعه کردن
🥰</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4371" target="_blank">📅 14:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4367">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/P7NVsyew8mOCmx6_SLI9CsD5mWQNB_dxgu2OiVuDftasshVMG4ay01mnEHJJMYbXaSgI6lQGZDOctCqj7FnBwr0ebBLNXstHzlvIMgjdSsUCInH-1-NoOiFT_sVlCX6SFctTnfW2aUyy5eDN3Uv5KRtVtx2ME180_Qor8oFfwgK4b0LvCTp0aWrmVH7Fx0xpOEObGCt4DD8qOoIrOK_7_HnXLeaFC_r5iJY2e9TqVEvtoWDdnbradZ63gZUu-DzIj-d1c-3xmkjpYuwo_9dwG_OpKuFe2zmibPbYIZipzFo5YFZLxE6uTFrP-TFFAr6rCM1f1UnsntiLQ7L6TRfuzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Nq_4slm4IPVIbnjhYSUgqO1gy3oap15sMd5WwSkGp7IlpBmeQ9j8CLQH5Nz2on2tyio5bXyHFkQeFSYnfbHY8YNVpsWHGPeIKwpPggLd1xeQHD4aj-PWz13mmdS3J-3Txgrw5isqo0qy_MY50nfR8xZyZVY3_9A1bua9GiOOkgfRa2ZW1IxYpd7XW9ieWvKNAvFtQdO6a9TfO4Y2dbFZF1Lli2thMr14ppz4E_z5S06x3iik5vEeriaHR9UaSQhfOxlzPJ3od-Amu2QXy0BmUddTSnrb3MiNOBEfjMN6I9o7zHJfgIrCoGQ8dqZPw0QS_AuU4FaUmRRxhULzS75Trw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RbkUeRW1tNoyJAVg9c0XfyaBwWiFjt1qox0Md-fWDY6VpsuGrlSib1CtvQfx5raJZS70KbbGZYLDAmomPCYzZ9NmZ5WzCGlHGhlaCjUzu-IHa5cIiNe9TPPkEz1Z9x2Y5-6NbsjsbDm-Kkx2i4m_V2rWBwfaiNcVg8fE-UkFTHUSUtKZUTlJ5r2Yl1Ayy73lPYcMSm4RFQVCwIRH8X9sEQar40_7oS4ipGP6_G1SjL7rV_N2G4gK4RPsYJT00AnXrlCd2q5zjxd_Fe27-t6dOLvEFXMTPx-rxCKDOnlKEeJ_k_-jJ0fy2biyFwPzmDriHaAPLKY40HfidrieKMbMFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lNIKTF3EdFFXbaVIpCEo4Wd6UeBYwi1ZTVVw2bT9EnwCaK_lszeEl_kVJIxOXIw46mze6V3eRcrBHJ85XrSOYwFrokKKhshXCF5SGJzaAQMbfjvXPU4NUimvx6JW9DfP2KxukjfKpeDCle95V-xjK6LGk3UJqyOGhI_3lUv-hvbFGzOn3s3Kh82VGuzj9p99UYkdqavBC4It6hKBH7yuYKH4MER9XG-1Ji-GoqKor68hOnkOKo-G4jvXREH4lNLtUuMsZUIwVDyyD4AKH0s6bi56qYpHcl6U9UbB5eoZDs0nu-8wrB42JaGeJ6vCLN33-F-0jJu5yBeegkf0yRnjOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">لینک زیر رو به هرمس بدید و بگید:
اینو نصب کن، فعال کن و بذار تو استارتاپ سیستم تا با روشن شدن سیستم اجرا بشه.
بعد از نصب یه محیط بسیار زیبا تحت وب در آدرس لوکال زیر برای شما فعال میکنه:
http://localhost:8787
https://github.com/nesquena/hermes-webui
✍️
بوکانت</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4367" target="_blank">📅 07:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4366">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">فردا open design و claude design رو واستون یه مقایسه میکنم از اونجایی که روز آخر اشتراک کلاد 20 دلاریمه، آتیش بزنم به مال(توکن)ـم
ولی ویدئو فعلا ازش نمی‌گیرم. صرفا اینجا بهتون نشون میدم
چون هنوز به open design مسلط نیستم کامل
در عوض تمرکز می‌کنم روی ویدئوهای درس خوندن با ai و بالاتر بردن efficiency</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4366" target="_blank">📅 05:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4365">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/720362863c.mp4?token=MoTQTNfSWx5aLmck95iG8rx7wVZoAXC4j6mSlGuCrnSTrHwkHLVn1Ca2dToJ02ZVsCwsyXIQo7CkFSmHmVrcj86U_rObrqDFS6jGW8-_K6VBZ6nIEHtW2ukfciGAHAH4zbBuMvcSpboCyYRumlDCsZlgjY7RUrEJiFWe23jFGb_znpEa1YG1JDvKWoOaPkXCLtFm02enU5E3Y1k7Co29nG1qSsegYTpLN_aW1aNi0jGi6phubtUR-hX4w5_-mzEOHa-iz9VTbq_m5FeD9v_1pvQuybobvZAsyPpI0xtszbOLjth4iT8M6EQmuvj97Q_iYyGiVBL9L4uhIf2RKmLByA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/720362863c.mp4?token=MoTQTNfSWx5aLmck95iG8rx7wVZoAXC4j6mSlGuCrnSTrHwkHLVn1Ca2dToJ02ZVsCwsyXIQo7CkFSmHmVrcj86U_rObrqDFS6jGW8-_K6VBZ6nIEHtW2ukfciGAHAH4zbBuMvcSpboCyYRumlDCsZlgjY7RUrEJiFWe23jFGb_znpEa1YG1JDvKWoOaPkXCLtFm02enU5E3Y1k7Co29nG1qSsegYTpLN_aW1aNi0jGi6phubtUR-hX4w5_-mzEOHa-iz9VTbq_m5FeD9v_1pvQuybobvZAsyPpI0xtszbOLjth4iT8M6EQmuvj97Q_iYyGiVBL9L4uhIf2RKmLByA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی ردیت یه نفر یه پورتفولیوی کاری ساخته که رسما مرزهای فرانت‌اند رو جابه‌جا کرده
😂
طرف طبق گفته‌ی خودش، فقط به Claude Fable 5 یه دستور خیلی کوتاه داده(که البته من به شدت شک دارم):
"یه پورتفولیو می‌خوام که کاربر نخوندش، بلکه توش پرواز کنه!"
نتیجه این شد که کلاد صفر تا صد یه سایت سه‌بعدی رو ساخته که شما توش تو فضای بی‌کران اسکرول می‌کنید، سیاره‌ها و پروژه‌ها از کنارتون رد می‌شن، از تکسچرهای واقعی ناسا (NASA) استفاده شده، گرافیکش روی مرورگر کاملاً 60fps ران می‌شه، و در نهایت وقتی به آخر سایت می‌رسید... سفینه‌تون می‌خوره توی خورشید و منفجر می‌شه!
😂
این پروژه قدرت وحشتناک هوش مصنوعی توی ترکیب کتابخونه‌های پیچیده مثل Three.js با کدهای فرانت‌اند رو نشون می‌ده. که اگر بتونید AI رو توی مسیر درست هدایت کنید، خروجیش به شدت جالب می‌شه.
لینک سورس کدش تو گیت‌هاب (اگه می‌خواید خودتون تستش کنید):
🔗
https://github.com/AbhishekBadar/portfolio
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/4365" target="_blank">📅 23:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4364">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">از بین سه تا پنل BPB و Edge و نهان که آموزش دادم، به شخصه برای خودم Edge سرویس‌های بیشتری رو باز می‌کنه بدون نیاز به proxy_ip. اون دوتا نیاز به proxy_ip دارن اکثر اوقات تا به درستی کار کنن یا نیاز به تعویض کلاینت یا dns معمولا. اما edge بهتر بوده تا الان حقیقتا.…</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4364" target="_blank">📅 19:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4363">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">از بین سه تا پنل BPB و Edge و نهان که آموزش دادم، به شخصه برای خودم Edge سرویس‌های بیشتری رو باز می‌کنه بدون نیاز به proxy_ip. اون دوتا نیاز به proxy_ip دارن اکثر اوقات تا به درستی کار کنن یا نیاز به تعویض کلاینت یا dns معمولا. اما edge بهتر بوده تا الان حقیقتا.
آموزش راه‌اندازیش روی
دسکتاپ
و
گوشی</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4363" target="_blank">📅 19:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4362">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPersian GitHub(Afshin Karimi)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3gr6ZQMn3mvHHlORNaqMgDKptZDNnkgkpDnmN7AQMnrXg_KP3jQJzGAquwPy-8llopKWcqju5UgOY1QjHkW-vKyLOXH50KiTHVFF9Mb8PYLCMfp4gZwYdo1XH0Za8YpNmKRx2okah-TjfucXAkeNhs_O-AaKahDGPut4l28WyeUfZ0i3RaZhZBkVkjQ6EU0UbLG51gTCvCQn-LSCJhLCexGbpNq8dL-734Rz_N8A9AXml-Ix3AyHi3txIhc17GMh04K3mjMk_KbRxNKr5Rj13lezf1F4h0vOfdvHuxghVqBx2XUwb-kNApOPIz9OGCRyGlTbjM4KhqeigGbfMA8nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه GameShell یک بازی متن‌باز برای یادگیری دستورات لینوکس است که به‌جای آموزش‌های سنتی، مفاهیم را از طریق مراحل و مأموریت‌های تعاملی یاد می‌دهد.
اگر تازه می‌خواهید لینوکس را شروع کنید، این بازی می‌تواند راهی سرگرم‌کننده برای یادگیری دستورات پایه باشد.
https://github.com/phyver/GameShell
@RepoFa</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4362" target="_blank">📅 17:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4361">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">به نظرم اگر می‌خواید برنامه‌نویسی یاد بگیرید، بهتره که یک زبان، و از اون زبان یک حوزه رو در نظر بگیرید و شروع کنید به یادگیری.
برای مثال اگر بخواید پایتون یاد بگیرید و همزمان توی حوزه‌های AI و Back-End باهاش کار کنید، آخر سر به خودتون میاید می‌بینید هیچ کدومش رو درست و حسابی یاد نگرفتید.
و همیشه در همین حین، سه تا سؤال از خودتون بپرسید.
1- چی دارم یاد میگیرم؟(روشن شدن مسیر)
2- برای چی دارم یاد میگیرم؟(روشن شدن هدف)
3- قراره باهاش چی بسازم؟(تبدیل به انگیزه میشه و دل‌زده نمی‌شید)
این پروسه‌ایه که من خودم طی میکنم برای هر زبان-فیلد جدیدی که می‌خوام یاد بگیرم. کاملا هم نظر شخصیه و چیز ثابت شده یا علمی‌ای پشتش نیست لزوما</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4361" target="_blank">📅 16:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4360">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اگه با ایجنت‌های کدنویسی کار کرده باشید، می‌دونید که بزرگ‌ترین مشکلشون Over-engineering کردنه. یعنی مثلاً برای یه تقویم ساده که با یه تگ HTML حل می‌شه، میرن یه کامپوننت ۴۰۰ خطی با نصب کلی پکیج اضافه می‌نویسن
😳
ابزار Ponytail (که الان به شدت تو کامیونیتی وایرال…</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4360" target="_blank">📅 15:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4359">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FbFNlCWnvsp8SKoZBOULv_jFT-S2TSaUxQgdRHGDWUW8vB91XOjXOP9AC7G3cTKxRP2lCMpJIj2eCsMoUr6bYNGPz7ByB1lIQs1UaO0KvlcCCt05XQ8IOXIuuat4hl2G18xdKqgT5wKcc8KcGp7DACgsj4se9kHtNvzlyjIUinzCg8jsXeW09lj5aDWZmUcEJyamo-ekvTKhimPNbO8jxGZkgWN2X_pWial24koWc7LGlH1IyuiGOAjTadaH4SUzWwN6M1A_Ynp0ImBNtJi7-cKoLIw-heIPpmFz5D7EaaHNiJQ2UnRReXKnux3r7JEJJmuKpIX8M1vEAlZpin04VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه با ایجنت‌های کدنویسی کار کرده باشید، می‌دونید که بزرگ‌ترین مشکلشون Over-engineering کردنه. یعنی مثلاً برای یه تقویم ساده که با یه تگ HTML حل می‌شه، میرن یه کامپوننت ۴۰۰ خطی با نصب کلی پکیج اضافه می‌نویسن
😳
ابزار
Ponytail
(که الان به شدت تو کامیونیتی وایرال شده) دقیقاً یه پلاگین برای حل همین مشکله. این ابزار باعث می‌شه ایجنتتون مثل همون برنامه‌نویس‌های سینیورِ تنبل شرکت که حوصله‌ی کدِ اضافه نوشتن ندارن، رفتار کنه
🙄
شعار این ابزار اینه:
«هیچی نمی‌گه. فقط یه خط کد می‌نویسه. همونم کار می‌کنه.»
چطور کار می‌کنه؟
قبل از اینکه ایجنت حتی یک خط کد بنویسه، مجبورش می‌کنه این نردبان رو تو ذهنش طی کنه:
- اصلاً این فیچر نیازه؟ (قانون YAGNI) اگه نه، بی‌خیالش شو.
- آیا توی کدهای فعلی پروژه قبلاً نوشته شده؟ اگه آره، همون رو ری‌یوز کن.
- کتابخونه‌های استاندارد خود زبان می‌تونن حلش کنن؟
- آیا مرورگر یا سیستم‌عامل خودش اینو داره؟ (مثل استفاده از
<input type="date">
به جای نصب پکیج).
- آیا پکیجی که از قبل تو پروژه نصبه این کارو می‌کنه؟
- می‌شه توی یه خط نوشتش؟
- فقط در نهایت: حداقل کد ممکن رو بنویس.
طبق بنچمارک‌ها، این ابزار حجم کدها رو ۵۴ تا ۹۴ درصد و مصرف توکن‌ها رو ۲۷٪ کاهش می‌ده. البته اینم بگم که تو مباحث امنیتی و Validate کردن اصلاً تنبلی نمی‌کنه و امنیتش ۱۰۰ درصده
❌
آموزش نصب روی ابزارهای مختلف:
توی Claude Code
کافیه دو تا دستور زیر رو جداگانه توی پرامپت بنویسید:
/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail
توی هرمس (Hermes Agent)
hermes plugins install DietrichGebert/ponytail --enable
بعد از نصب می‌تونید با دستوراتی مثل /ponytail یا /ponytail-review کنترلش کنید.
توی Cursor، Cline و دیگر
ide ها
نیازی به پلاگین نیست. کافیه فایل رول‌ها (مثل .cursor/rules/
ponytail.md
) رو از گیت‌هابش دانلود کنید و بندازید توی پوشه‌ی پروژه‌تون.
توی GitHub Copilot CLI
/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail
توی Gemini CLI (Antigravity)
agy plugin install
https://github.com/DietrichGebert/ponytail
لینک ابزار:
https://ponytail.dev/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/4359" target="_blank">📅 14:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4358">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">هوش مصنوعی به جای یک فایل، کل درایو C رو پاک کرد!
😐
چند روز پیش توی گروه جامعه وایب کدینگ ایران، افشین یه تجربه عجیب رو منتشر کرد.  داستان از این قرار بود که با Z.ai و مدل GLM 5.1 یا GLM 5.2 از AI خواسته فقط یه فایل رو حذف کنه، اما ظاهرا به جای اون، کل درایو…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/4358" target="_blank">📅 12:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4357">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجامعه وایب کدینگ ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBsB0kZV2kbiRgeAcS7BIuj-EUxPY7Yam_clzCvmdywLeWFRkrt2OF7ORAvrasYZAVSU-qI8kbKp716bk2LxLaujDqt6zJ2giuU_CJjiMewCnjNH_Qob1dFmJ0uSZDoNe-vW5KUK_4YzUb8Kluzm5TqFhx0JQnV-zKSofEsqUFjWuV1wybCIoHoEHWAOl87RziMKKz2bwYHpt6TxeIk54oRx2PQhgsrZR3IzklTH3os_AAfjWm_hMNI3701jDmN8ShqIm_rnwruL1o1pcfw0eHku_uyPS7ke4QEH_nH4wF1wWqGOtfBixyF-5Qx1kr7B87vVxrVF8RPI9ne38ndAkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی به جای یک فایل، کل درایو C رو پاک کرد!
😐
چند روز پیش توی گروه جامعه وایب کدینگ ایران، افشین یه تجربه عجیب رو منتشر کرد.
داستان از این قرار بود که با
Z.ai
و مدل GLM 5.1 یا GLM 5.2 از AI خواسته فقط یه فایل رو حذف کنه، اما ظاهرا به جای اون، کل درایو C ویندوز پاک شده!
این اتفاق یه یادآوری مهمه.
هرچقدر هم Agentهای هوش مصنوعی باحال و قدرتمند باشن، وقتی به ترمینال، فایل های سیستم یا دیتابیس دسترسی کامل داشته باشن، یه اشتباه کوچیک می تونه به یه فاجعه تبدیل بشه.
اتفاقا متین سنپای هم امروز ابزار Kastra رو معرفی کرده که دقیقا برای همین سناریو ساخته شده. این ابزار بین Agent و سیستم قرار می گیره و برای کارهای حساس مثل حذف فایل یا تغییر دیتابیس، اول از خودت تایید می گیره تا AI نتونه هر کاری خواست انجام بده.
به نظرم تا چند وقت دیگه استفاده از ابزارهایی مثل Kastra دیگه یه قابلیت اضافه نیست، بلکه برای هر کسی که با Agentهای کدنویسی کار می کنه، واجبه.
تا حالا Agentها چه خرابکاری هایی براتون انجام دادن؟
😅</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4357" target="_blank">📅 12:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4356">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sbEyLn8bSZfd79D9BvkLqtYyFiJ0digINgtxVI1oeT355FxDPM0vi73LShpZPINZOnafZ1TQIDWvoktoA4cqQDc33wyA7bpcc9vXYrALDC3iyDqlM5ENTMNSSIV7MrVPXxX_MN3BHwr8-dG969RQ2OisLe8MPZK6cEWkv5JlfWEGt91WUWHeJ0dvVe9XVnTHA7vP9axGDNr9N7Qp3MT-P0UvlOe6GZQY3FFLseDgs9QV0V3r95oUhoq06Gxvjkir0b3b9uMz0ArPRacqxdealaZNIPMS44rxgXbEWnWSVAzmeUs3ggmRQs5OMvM2XgcSP_a6z7ji5xp3SeJLdCj0FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار Kastra برای کنترل ایجنت‌های کدنویسی
اگه با ایجنت‌هایی مثل کلاد یا هرمس(روی Yolo) و یا هر ایجنت دیگه‌ای روی کدهای حساس کار می‌کنید، استفاده از سیستم‌های نظارتی دیگه یه آپشن نیست صرفا به نظرم، بلکه واجبه!
توی Hacker News یه ابزار خیلی خفن و کاربردی به اسم Kastra معرفی شده که کارش اینه که به عنوان یه «لایه‌ی دسترسی و تایید» (Authorization Layer) برای هوش مصنوعی عمل می‌کنه. یعنی دقیقا روی فراخوانی toolها توسط ایجنت‌هایی مثل Cursor و Claude Code نظارت می‌کنه تا اونا سر خود کاری نکنن.
چرا اصلاً به Kastra نیاز داریم؟
ایده‌ی ساخت این ابزار زمانی به ذهن تیم سازنده‌ش رسید که ایجنت خودشون نزدیک بود یه دیتابیس پروداکشن رو به کل پاک کنه! وقتی به مدل‌ها دسترسی کامل (مثل کار با ترمینال یا دیتابیس) می‌دید، هر لحظه ممکنه توهم (Hallucination) بزنن یا اشتباه کنن. Kastra اینجاست تا جلوی فاجعه رو بگیره.
ویژگی‌های اصلی:
- پشتیبانی کامل با mcp: تو کمتر از ۲ دقیقه می‌تونید با Cursor، Claude Code و پروتکل‌های MCP وصلش کنید.
- گاردریل‌های امنیتی: می‌تونید براش قانون بذارید که ایجنت برای کارهای خطرناک (مثل پاک کردن یا تغییر دیتابیس) اول از شما اجازه بگیره.
- مدیریت دسترسی: مشخص می‌کنید که ایجنت شما دقیقا به چه ابزارها و چه بخش‌هایی از سیستم دسترسی داشته باشه.
لینک ابزار:
https://kastra.ai/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/4356" target="_blank">📅 10:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4355">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/885f71c1ea.mp4?token=mnsAFbH9lmkGqzBLvqj7rax1xdRhr66urojA3FIjFTNoMxAw0GmiP8TRS0GLPEdhxMNj0evKXazlEMRrKK01qUUG0RXXMlTlAngj0H9j6tnsDDAUQ4eR-WL04T7FHNWJkq5Bi6Vk3kAB_AkvNkV9fmKMuIRw891lIDNPsq0r_OmKUkDrBstmTiUNGN7FF87D6yp9doiAEvziWLHLHAmA6I5DmvvABhwHdOraMO_sV0z4QxSPwZkBxNp6kABl6UfgL7RHOcPYAkWYGL2YMANhF0XHJ7RGBZ4nG001s6A0AQeixzQ_eOcEL2epFteqca3Y5BZmbVBdJ-0bLKSCuNleQw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/885f71c1ea.mp4?token=mnsAFbH9lmkGqzBLvqj7rax1xdRhr66urojA3FIjFTNoMxAw0GmiP8TRS0GLPEdhxMNj0evKXazlEMRrKK01qUUG0RXXMlTlAngj0H9j6tnsDDAUQ4eR-WL04T7FHNWJkq5Bi6Vk3kAB_AkvNkV9fmKMuIRw891lIDNPsq0r_OmKUkDrBstmTiUNGN7FF87D6yp9doiAEvziWLHLHAmA6I5DmvvABhwHdOraMO_sV0z4QxSPwZkBxNp6kABl6UfgL7RHOcPYAkWYGL2YMANhF0XHJ7RGBZ4nG001s6A0AQeixzQ_eOcEL2epFteqca3Y5BZmbVBdJ-0bLKSCuNleQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در کنار معرفی GPT-5.6، OpenAI یه کار جالب کرد و ChatGPT Work رو معرفی کرد. که به عنوان یه ایجنت می‌تونه کارهای طولانی رو روی فایل‌ها و اپلیکیشن‌ها انجام بده و ساعت‌ها روی یه پروژه متمرکز بمونه. به نظرم کم کم شبیه به هرمس، تمام ورک‌فلو‌ها و لوپ‌های پیچیده دارن…</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4355" target="_blank">📅 06:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4354">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">در کنار معرفی GPT-5.6، OpenAI یه کار جالب کرد و ChatGPT Work رو معرفی کرد. که به عنوان یه ایجنت می‌تونه کارهای طولانی رو روی فایل‌ها و اپلیکیشن‌ها انجام بده و ساعت‌ها روی یه پروژه متمرکز بمونه.
به نظرم کم کم شبیه به هرمس، تمام ورک‌فلو‌ها و لوپ‌های پیچیده دارن تبدیل به زبان طبیعی می‌شن.
شما می‌خواید، و انجام می‌شه
هرچند هنوز، مهندسی اینها، و نظارت روی کدی که AI می‌زنه، خیلی مهمه به نظرم.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4354" target="_blank">📅 05:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4353">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/802171ad75.mp4?token=i9apqy3enAH8xG5VRWmumpK-3IQ_Y9CcmHZcOEAeg2oMTeVXmjYeJ_VMb9pGR0qVFVul3Hcj44oyP0hUqJ6Ufh6ZJD-4V6jhsC0psNLP7rMdWBlh04EPYWytA1ybpCxCCa6JSF6rFlVxoL-ww0bYk49fcVEtw1MCQPLdX8GdwLb_krdlV4pvQJ39NogWY3dxGs9jRBlJzIFplpwaTt68gbr4mKYBPE2xwvmGCPc-qMS2Ac_K92ZWAJEHlNrONM6i6Mb7hiivmT1VYfBhHqx_BSYxenW_JkypzldqGIXZvyGD-64hpc_2jqcSxVUOxTki7WCHRmE7bYG9_jtxHKzvrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/802171ad75.mp4?token=i9apqy3enAH8xG5VRWmumpK-3IQ_Y9CcmHZcOEAeg2oMTeVXmjYeJ_VMb9pGR0qVFVul3Hcj44oyP0hUqJ6Ufh6ZJD-4V6jhsC0psNLP7rMdWBlh04EPYWytA1ybpCxCCa6JSF6rFlVxoL-ww0bYk49fcVEtw1MCQPLdX8GdwLb_krdlV4pvQJ39NogWY3dxGs9jRBlJzIFplpwaTt68gbr4mKYBPE2xwvmGCPc-qMS2Ac_K92ZWAJEHlNrONM6i6Mb7hiivmT1VYfBhHqx_BSYxenW_JkypzldqGIXZvyGD-64hpc_2jqcSxVUOxTki7WCHRmE7bYG9_jtxHKzvrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍷
درود به همه رفقا...
اگر کانفیگ میزنید و فرگمنت روی ip ها کار نمیکنه واستون بهتره که از دامنه برای ip تمیز استفاده کنید...
برای مثال بهترینش:
Chatgpt.com
Grok.com
با این مقدار فرگمنت:
Packets: 1-3
Interval: 1-1
Length: 1-7
اگر کلاینت Fakehost داشت:
Google.com
رفقایی که ابتدایی تر هستن داخل ویدیو کوتاه نشون دادم داخل هر مدل گوشی یا کلاینت که کانفیگ میزنید هست
✅
💡
نکته:اگر کندی در کانفیگ یا آپلود ندارید روشن کنید fragment رو عزیزان.
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/4353" target="_blank">📅 01:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4352">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">به شخصه پلن کلادمو ReSubscribe نمیکنم؛ تا ببینم وضعیت قطعی نت چی میشه به شما هم توصیه می‌کنم اگر تموم شده و کارتون زیاد لنگ نیست، نخرید فعلا..</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4352" target="_blank">📅 00:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4351">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88560d1079.webm?token=pI6jBrkNaOSMS2J9NvWQMCwtbXXjflcZJIf3sEsJhINrYFrkBK17tEHljWYYjC8Da9PSWgb1gFROqbtWlZ4MfycS2yRn0DbAqSYomYingdsDJtCO6vdkDSa7p06Af2o-cedBHSc5XgUzVr_qS9IBoiz4E8ha1eq7QQpFOmmacWZmCbsHhweBJ46mBOnMLVsUwWILJfURz98RPGllFTOtR_QxEqIVUYy1yCh3g4q2T1zfNPAh8we5zk5RPBc8cy4ypD4Vuieh50g4jfdhQlxQeT3tAvnlC2CY4tqsmE-j77gGRFtYmMvzMyJsxBBE09U9Xs8Hgn--9fEd_VHMVDGeFg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88560d1079.webm?token=pI6jBrkNaOSMS2J9NvWQMCwtbXXjflcZJIf3sEsJhINrYFrkBK17tEHljWYYjC8Da9PSWgb1gFROqbtWlZ4MfycS2yRn0DbAqSYomYingdsDJtCO6vdkDSa7p06Af2o-cedBHSc5XgUzVr_qS9IBoiz4E8ha1eq7QQpFOmmacWZmCbsHhweBJ46mBOnMLVsUwWILJfURz98RPGllFTOtR_QxEqIVUYy1yCh3g4q2T1zfNPAh8we5zk5RPBc8cy4ypD4Vuieh50g4jfdhQlxQeT3tAvnlC2CY4tqsmE-j77gGRFtYmMvzMyJsxBBE09U9Xs8Hgn--9fEd_VHMVDGeFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4351" target="_blank">📅 00:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4350">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">به شخصه پلن کلادمو ReSubscribe نمیکنم؛ تا ببینم وضعیت قطعی نت چی میشه
به شما هم توصیه می‌کنم اگر تموم شده و کارتون زیاد لنگ نیست، نخرید فعلا..</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4350" target="_blank">📅 00:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4349">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">یکی گروک مدل grok 4.5 رو داده بیرون، یکی هم متا مدل جدید داده بیرون به اسم Muse Spark 1.1 هر دو هم ادعا کردن که هم سطح Opus 4.8 هستن با هزینه کمتر، ولی به نظرم متا دروغ میگه
😂</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/4349" target="_blank">📅 23:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4348">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K2inSyqky84NvevUjFhITsJ-bGMosDpJS2N_5LBZxuFzmVe6xLJCtY7BrtYfqhk02XKYr3eP3yLGgvWF2oYKFnop7YNt_pn6HhDMM2UJ9-j1kDJ2oQelQF4SIPQ2xONSyAgJnWayPsMX2oDY3smxueotScDXjDTIDeLuoL2IkEoI8t1qqVcUoALGl8dp8KSYz1Ep_CEfDuRWpyUKKADrUBXsuu3Dc9ZKy7Y2UwfJ7Jp7Ot_CdKqW529Dc_KCZaQfBAXTmt4UbtjY9AslTx-BklsrgKBoW2_oIwSXLqstTX3VNytZdlpVmIvp1uxAMFhnrbWjvpFOyVh2ju-keG-PDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر درست باشه فوق‌العادست
بچه‌های توییتر تست کردن Grok چهار و نیم رو، همه تعریف تمجید کردن</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4348" target="_blank">📅 22:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4347">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">یکی گروک مدل grok 4.5 رو داده بیرون،
یکی هم متا مدل جدید داده بیرون به اسم Muse Spark 1.1
هر دو هم ادعا کردن که هم سطح Opus 4.8 هستن با هزینه کمتر، ولی به نظرم متا دروغ میگه
😂</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4347" target="_blank">📅 22:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4346">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اتهام جاسوسی به Claude Code؛ چین درباره ابزار برنامه‌نویسی آنتروپیک هشدار داد</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4346" target="_blank">📅 21:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4345">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">یه کاری کردن انگار شرطی شدیم
تا نتمونو قطع نکنن باور نمی‌کنیم جنگ شده</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4345" target="_blank">📅 21:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4344">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/BMrC9INoR6P2J40xwgM69tlMWd9q5j8ua9SS4K_RH9QI7goWN-B510KvUDgFr-R62d0R7A7Dz_jUvlUjdei2cXhLb0fdTUIXa7nazjrojOEQFurXJSdlI4A2mx35AvJkmsORaWl6GUUUXdlnbAbc0QO3K_3p0rJdAbb6OE_3VpsvIglMoS3vrZooMbQBpfkQv9iJPfkQWB75DiarVFzSoQh01bzhhX0Xnkw80eGHKSikJOrNCmo9XIY7bgCnuimwgpJ8dPf60Q3w4_2x_UHiywDL3TDJQAHA-X-nGYWsYSMp0SoqdJsNpBgk_z5ZECDRr4t_NSvqL8KaogKtTrHXmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
دستیار هوشمند کانال WhiteDNS
👉
@WhiteDnsChatBot
✅
جواب سریع |
✅
۲۴ ساعته |
✅
رایگان
نحوه استفاده:
۱. روی لینک بزنید
۲. Start
۳. سوالتان را بنویسید
مثال: چطور فیلترشکن نصب کنم؟
/search عبارت — جستجوی مستقیم
/contact — ارتباط با ادمین
⚠️
ربات WhiteDNS در چه زمینه‌هایی جواب می‌دهد:
✅
فیلترشکن و VPN
✅
DNS و تنظیمات اینترنت
✅
آموزش نصب اپلیکیشن‌های WhiteDNS
✅
رفع مشکلات اتصال
✅
Warp و Cloudflare
✅
تنظیمات اندروید، آیفون، ویندوز، مک
✅
سوالات مربوط به قطعی اینترنت
❌
ربات قادر به پاسخ‌گویی به سوالات غیرمرتبط با موضوعات کانال نیست.
💡
نکته: اگر جواب دقیق نگرفتید، سوالتان را طور دیگری بنویسید یا از دکمه جستجو استفاده کنید.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/4344" target="_blank">📅 20:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4343">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">ترجیحا هیچ VPNای نخرید دوستان. هیچ تضمینی نیست که اگر اینترنت قطع بشه هم اونا وصل بمونن یا نه. مثل اوایل جنگ که خیلیا اسکم شدن
همون هزینه رو بذارید whitedns راه بندازید</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4343" target="_blank">📅 16:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4342">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b1d99494e2.mp4?token=ZJoX4lOB93lNxGgqQ5azXV-LFCwzGvznmkDPPF6hB1EnxC3S2_VuldB4OT9_tDMUSt9KO0q4Bh8d-5C5qKPdszG8pXYLzDLGsMrI9RA-AuSTPrneFrqRMqu2TKvzoyvjorCJ2AMYqWoBV-8syH6ZXx0GRMi6kBepuPFSfrSDF8A9qpvgPfD4v68X9U3idt0YIQv54ZLDNmwrQd0ifdD7iU496Wh4CSBXiLl7KMoPvlR8kAPDNk_RRQ58hqhRf1GHwJErJjQLcHH6z_PqU9WDYArcn4ICmozwBr7L5pJgHHy3xYAUObp03owaM2HYeOACg3y2SdqOnTVbazG9rFyd9g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b1d99494e2.mp4?token=ZJoX4lOB93lNxGgqQ5azXV-LFCwzGvznmkDPPF6hB1EnxC3S2_VuldB4OT9_tDMUSt9KO0q4Bh8d-5C5qKPdszG8pXYLzDLGsMrI9RA-AuSTPrneFrqRMqu2TKvzoyvjorCJ2AMYqWoBV-8syH6ZXx0GRMi6kBepuPFSfrSDF8A9qpvgPfD4v68X9U3idt0YIQv54ZLDNmwrQd0ifdD7iU496Wh4CSBXiLl7KMoPvlR8kAPDNk_RRQ58hqhRf1GHwJErJjQLcHH6z_PqU9WDYArcn4ICmozwBr7L5pJgHHy3xYAUObp03owaM2HYeOACg3y2SdqOnTVbazG9rFyd9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مقدار زود شروع شد</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/4342" target="_blank">📅 16:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4341">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GsLwwIuK9Wp2-BLMLwAVdbWMCxTT8HEOZnpAEjNyMVq0E-p7o07SRk1UesMNShN-GVBoizmk0ycI04JgiDfDn0ym8qe_WwhlPmUBz7rKM-5_8nqCwUQlJmMbnuUrj--V_6AZahKuNKXNaCqQ44rOIWvXySAsbrhpK3fIs3SygjrI1p8lErBOoaWEoCLYpe5v3FXrbAXwxYwT8I6j-t2I1Y8jYqFHr8RJNF50YrBV-eT8efng7DM8p5GYIwRvlIhFLqV3mU-5dvMVbkAJqkSZW81ql19SuugEAhjpfDqxpYG1dPrCcFZw_lgGRpIT8CA9nqwbGobQO77G0w9Jb5Y3Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پارادوکس عجیبیه. از یه طرف انگار جدی جدی جنگ شده باز
از یه طرف اینور دارم آموزش می‌بینم و کار می‌کنم با ai
و نمیدونم همین آب باریکه‌ی نت کی قطع میشه دوباره</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/4341" target="_blank">📅 15:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4340">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">احتمالاً من دچار "فرسودگی LLM" (LLM Burnout) شدم!
نویسنده‌ی این مقاله (الک سکولن) یه توسعه‌دهنده‌ست که می‌گه مصرفش از هوش مصنوعی در حد استانداردهای الان کاملا معمولیه، اما اخیراً یه حس خیلی عجیبی بهش دست داده:
خستگی مفرط از خوندن متن‌های تولید شده توسط هوش مصنوعی!
روند کارش این‌طوری شده که دیگه خودش از صفر کد نمی‌نویسه؛ طراحی می‌کنه، طراحیش رو به Claude یا Codex می‌ده، کدهای اونا رو می‌خونه و ریویو می‌کنه. علاوه بر این، روی پروژه‌ای کار می‌کنه که کدهای تولید شده توسط Qwen رو باید مداوم بررسی کنه. یعنی عملاً کل روزش با خوندن خروجی‌های AI می‌گذره. حتی برای سرچ‌های روزمره‌ش هم از ChatGPT و Gemini استفاده می‌کنه.
حالا مشکل کجاست؟
اعتراف می‌کنه که با این ابزارها خیلی بهره‌ورتر شده و قصد نداره کنارشون بذاره، اما تو چند ماه اخیر، یه بخش کوچیکی از وجودش از دیدن خروجیِ مدل‌ها وحشت داره! چرا؟ چون دقیقاً می‌دونه قراره چی ببینه:
فرضیات غلط، توهمات (Hallucinations)، جملات بریده‌بریده‌ی اغراق‌آمیز، و
✨
استفاده‌ی بیش‌از‌حد از ایموجی‌ها
🚀
.
نکته‌ی جالب اینجاست که می‌گه انسان‌ها هم اشتباه می‌کنن و می‌تونن رو اعصاب باشن، اما مشکلِ اصلی با هوش مصنوعی
تکراری بودنشه
. مدل‌های زبانی دقیقاً با یک لحنِ واحد می‌نویسن و دقیقاً یک‌جور اشتباه می‌کنن. سر و کله زدن با یک سبکِ کاملا یکسان و اشتباهات تکراری، اونم به صورت هر روزه، کلا فرسوده‌ش کرده.
این دقیقاً نشون می‌ده که با وجود تمام شخصی‌سازی‌ها (Personalization) و پرامپت‌ها، هنوز هم اون امضای پنهان و سبک خاصِ هوش مصنوعی از زیر دستمون در میره و وقتی تو طولانی‌مدت باهاش درگیر بشید، می‌تونه حسابی روی مختون بره!
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/4340" target="_blank">📅 14:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4338">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ixIVve-fWWxlgALTT3ySpqsmwuQDoqlJ3ECMWnMETSsnvTxl0QyLuW3p6s3UZxJb_nePCz2zaYBCCjUwWq4MKQ2NczPCBU6nRKQ54mmk9k1caTLdhVBj3XFU6cCyWDX5Tv5ZRXgNawFDs_6G0bXxRZ7sZP05yJB3FWTucu2QsxbPe8jMW9f4hkuhmBOxY2k6UYiT5LoSqJpu2USGQ7tGwO9nqMKLkFphMLZ3WPiqh-A3NkMX5zG2lElN1n3dtK5g62HeyYxVhqwJzQvJxxWC42WsAaGyUarNJ1l7azvUaDtZppM5-osIjQ9EvG_P8hVpJGuOKo9p3oV5fKWV4sEf6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rEuixRXpPltwGcYHSna520nen71U6hy78D4-DzpJ0Fawfv6SADLjABEj56gZuwb7Ta3QgawQBwIA1o02w8CKIZmBe1JaE2vPbLSXYA3U0eNtvDxdYA2fKHqFNHFbbeS_NJDSFukuv1DL_PlV4w_WKJuTMBMhMfHO57OW0_xu9_mI-8Fnudz720wZXgFgvH91kl1SCxVDdFuOklj6xTTGf6ZkVrWRvusn2nqyninZF80gIMgIQV0jj2ckiot2PLv5tR1oEJeSziD_vRF3KW3OEMwdwhgAv-tztHzIf_0hFo9uH5Ju43793KXgPxEzA0zROwGGUc4fUQ5FFRlWHflbsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
100 میلیون توکن رایگان برای تست مدل‌های جدید AI  مدل‌های زیر را می‌توانید با OpenAI Compatible API استفاده کنید:  • Kimi K2.6 • MiniMax M2.7 • GLM 5.2 FP8  بدون ثبت‌نام، وارد صفحه زیر شوید و از بخش Your API Key کلید خودتان را دریافت کنید:  https://infer…</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/4338" target="_blank">📅 13:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4337">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/784bc3dcd7.mp4?token=l_B2ktFPRE7MFgd1CGHeLk7o0HqgdnRbgTJrMRKRoEo0I-H8FRaHp5gcRquqYCbIvkguwsbkk1xSbORukXILWV4ZwKE0_g3XPROqs37i5FtRNCOy_qjcBpjtUuV4fsgzqK0d6HpN0xARFebrNRXODcvURzsJtzLBPZJaOAzSbsj2_7fhzMs6jl4tL0YU3OfuATao39mwpcOIFe62sGzloCGCPV5Gyc0xoP8Pct-FYln1JYve-7HI0W-1bsnpwJ0UG0HdtwR6HnVQIxbesvQsrLeXOrEMWm0jCq1J3-0Zf3_t3T3JS9qTAbSgneZMVMC0sA3Lbb8NuX8OFwRYneQiS0SfAVXrJQ9HbmHWnRBsyNJp3lg5BJMO63DJpz3KVzsJolH1Put66yJs4nnT0ClPKKzmx_JeVjPKGuG2Nbsz6UbFc8bLODjRlEZQhhEySyKu3-vzcfvnkUKhkGAp5xQcsrkNasdVABUXJtZK_JG9obkUY_4Vl3Q_wtWGlM0ebm7mQIowP0LRzS_tSAiiFlHXlJvIvDXt8HIgkDyllTI1hmOXQUAHz_NDX_0l7dsLH7wD5GNB92avFAmt34kNfABoJmZLuzQ9494uIW7aNnOFKlhkRtOryYrYY8ZQpnIo5xm6ExHnOxVTkbHiePKpS1tRy1LA5hnyvAMrMoKabJ9bCPE" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/784bc3dcd7.mp4?token=l_B2ktFPRE7MFgd1CGHeLk7o0HqgdnRbgTJrMRKRoEo0I-H8FRaHp5gcRquqYCbIvkguwsbkk1xSbORukXILWV4ZwKE0_g3XPROqs37i5FtRNCOy_qjcBpjtUuV4fsgzqK0d6HpN0xARFebrNRXODcvURzsJtzLBPZJaOAzSbsj2_7fhzMs6jl4tL0YU3OfuATao39mwpcOIFe62sGzloCGCPV5Gyc0xoP8Pct-FYln1JYve-7HI0W-1bsnpwJ0UG0HdtwR6HnVQIxbesvQsrLeXOrEMWm0jCq1J3-0Zf3_t3T3JS9qTAbSgneZMVMC0sA3Lbb8NuX8OFwRYneQiS0SfAVXrJQ9HbmHWnRBsyNJp3lg5BJMO63DJpz3KVzsJolH1Put66yJs4nnT0ClPKKzmx_JeVjPKGuG2Nbsz6UbFc8bLODjRlEZQhhEySyKu3-vzcfvnkUKhkGAp5xQcsrkNasdVABUXJtZK_JG9obkUY_4Vl3Q_wtWGlM0ebm7mQIowP0LRzS_tSAiiFlHXlJvIvDXt8HIgkDyllTI1hmOXQUAHz_NDX_0l7dsLH7wD5GNB92avFAmt34kNfABoJmZLuzQ9494uIW7aNnOFKlhkRtOryYrYY8ZQpnIo5xm6ExHnOxVTkbHiePKpS1tRy1LA5hnyvAMrMoKabJ9bCPE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های جالب Amir Hormati مهندس ارشد و پرینسیپال در گوگل در حوزه AI در مورد کدنویسی و Hard Skill ها، اینکه آینده از دید خودش چیه، چه اتفاقی بر سر کدنویسی میاد و به عنوان مهندس نرم افزار روی چه مسائلی تمرکز کنیم، جالب اینکه خود امیر از رول مدیریت به نرم افزار برگشته به خاطر همین!
✍️
Max Shahdoost</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4337" target="_blank">📅 13:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4336">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">رفقا مجددا می‌گم، که کلا این سایت‌هایی که یهو کلی توکن رایگان میدن، امن به نظر نمی‌رسن مراقب پروژه و .env هاتون باشید</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/4336" target="_blank">📅 13:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4335">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">رفقا مجددا می‌گم، که کلا این سایت‌هایی که یهو کلی توکن رایگان میدن، امن به نظر نمی‌رسن
مراقب پروژه و .env هاتون باشید</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4335" target="_blank">📅 13:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4334">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجامعه وایب کدینگ ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRWDkL3u6bF5hjRpdls4-UPKROdIQZseOz5Rutfqbr6OnT9DQiZUT61ZumEy1yTqtELAzWahqQtSr83Ay2elM89IL5RMPqIR_L4Ssxcs1wHr_onkcSpaRRzDFNvtlayXc96_PxbhjY18MFThfXmjhxUmbhVRHPtRAiO1O8nSEfgQRcERKx0C66-7P2Tep_cWwHTarcUlUz0Ya_PNtZ59fF1sHFgqkcER29rxtRE6ws247nNMW6z5L9Kgp-QqTcltcEjE6EsE6uVIzoJEeXKjrnD5j2Nj11qsWgP_QAXs4dl27pbvMbRSHDF4O-6bUXBLM4OouCE-xG3b2XfSpYfawg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
100 میلیون توکن رایگان برای تست مدل‌های جدید AI
مدل‌های زیر را می‌توانید با OpenAI Compatible API استفاده کنید:
• Kimi K2.6
• MiniMax M2.7
• GLM 5.2 FP8
بدون ثبت‌نام، وارد صفحه زیر شوید و از بخش Your API Key کلید خودتان را دریافت کنید:
https://inference.dahl.global/chatKeys
💡
اگر کوکی مرورگر را پاک کنید، می‌توانید دوباره یک API Key جدید بگیرید.</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/4334" target="_blank">📅 13:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4333">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ShrM8DzOju7zO0DdKSzZ7Rq2MhNVkY-wAhens3ZZt5gtWqCDIxEBhijdB6FBDOX9F4aaCrqbFkblLpUbtU8sVPTeXpzJ0ocC8GNgpZl0C40utakgvGFkd57GW8hLEKPBK5Qx-F_eYC7HHRaACRd1sh5bzhVMUjw5XJ24LQ5Ay3IFDM2GmRZ7VgmKh5G9dKkYZL8hCkwofnUExSTjl-ZWIOH1wNt8uC4wyMwO7KpG3b7koU1QJRGpeyPX_Eg2R2EfBM1wvDKvIr4mySaYMrZsivSMCzy4mwdfAlqOqfRTbEZlvHYFiKznZlgD291oSCiXtEIsHtJqG9HTJ3dvZ8Yzxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیزی نیست، کامیونیتی Rust هستن
😂
😂
زبان Rust برخلاف go و پایتون و... از Garbage collector برخوردار نیست.
نفر اول گفته انقدر سینتکس افتضاحه که دلم می‌خواد زبان rust رو بندازم توی آشغالا(garbage) و نفر دوم ریپلای زده که اگه بندازیش توی آشغالا کسی نیست جمعش کنه چون این زبان آشغال جمع‌کن(garbage collector) نداره</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4333" target="_blank">📅 12:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4332">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اگر می‌خواید اکانت Claude بخرید، بهتره بدونید علت بن کردن‌های کلاد distillation attack هایی هست که اخیرا بهش شده؛ و حتی کاربرهای خارجی هم یهو اکانتاشون بن شده. بهتون دوتا توصیه می‌کنم.
1- به هیچ وجه از سایت‌های ایرانی نخرید. و حتما بدید دوستی، آشنایی، چیزی بگیره از خارج کشور. اگر ندارید، برید سراغ توصیه‌ی دوم. احتمال بن شدن داره به هر حال و ریسکش پای خودتونه. من خودم به شخصه هنوز بن نشدم(نمیدونم شانسه، یا چون دوستم از خارج از کشور واسم گرفت)
2- اشتراک Codex بگیرید در عوض و یا نهایتا اگر کار خیلی واجب دارید و می‌خواید حتما کلاد باشه، cursor بگیرید اما کرسر خیلی زود تموم میشه طبق تجربه‌ی شخصی. به نظرم Codex سخاوتمندانه‌تره به شدت. و صبر کنید تا وقتی که بن شدناشون شدتش کمتر بشه.</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/4332" target="_blank">📅 21:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4331">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">نشت مخفیانه‌ی دیتا از ریپازیتوری‌های پرایوت گیت‌هاب با یه ترفند ساده‌ی هوش مصنوعی
📚
فکر کنید یه نفر بدون هیچ پسورد و دسترسی‌ای، بتونه کدهای مخفیانه‌تون رو توی گیت‌هاب بخونه. چطوری؟ با گول زدن ایجنت هوش مصنوعیِ خود گیت‌هاب!
تیم Noma Labs یه آسیب‌پذیری خیلی خطرناک (به اسم GitLost) توی سیستم جدید Agentic Workflows گیت‌هاب پیدا کرده. داستان از این قراره که این ایجنت‌ها می‌تونن issueها رو بخونن و اتوماسیون انجام بدن.
🫵
حالا هکرها چیکار می‌تونن بکنن؟
هکر کافیه بیاد تو یکی از ریپازیتوری‌های پابلیک شما یه Issue باز کنه و توش یه سری دستور مخفیانه به زبان انگلیسی (Prompt Injection) قایم کنه.
ایجنت گیت‌هاب این متن رو می‌خونه، گول می‌خوره و به جای کار اصلیش، میره فایل‌ها و دیتای ریپازیتوری‌های پرایوتِ همون سازمان رو می‌خونه و برای هکر می‌فرسته!
نکته‌ی جالب اینجاست:
گیت‌هاب کلی گاردریل امنیتی چیده بود که دقیقاً جلوی همین اتفاق رو بگیره. اما محقق‌ها فهمیدن فقط با اضافه کردن کلمه‌ی "Additionally" (به‌علاوه/همچنین) توی پرامپت هک، مدل هوش مصنوعی کلا گیج می‌شه و به جای اینکه درخواست رو رد کنه، تمام محدودیت‌ها رو دور می‌زنه و دیتا رو لو میده.
این دقیقاً نشون میده که توی سیستم‌های جدید هوش مصنوعی، همون متنی که ایجنت می‌خونه همزمان می‌تونه پاشنه آشیل و نقطه حمله باشه. حملات Prompt Injection الان دقیقاً دارن همون بلایی رو سر AI میارن که قبلاً SQL Injection سر وب‌سایت‌ها میاورد.
البته این باگ به طور مسئولانه به گیت‌هاب گزارش شده، ولی حواستون به ایجنت‌هایی که به سورس‌کدهاتون دسترسی دارن باشه!
منبع:
https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/MatinSenPaii/4331" target="_blank">📅 19:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4330">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">یکی از چیزایی که راجب کامیونیتی فارسی باحاله و دوست دارم، اینه که زیاد توی کامنت‌ها با هم در ارتباطیم. کامیونیتی خارجی، این شکلیه که ویدئوی تکنیکال می‌ذارن، 60 کا ویو میخوره اما کلا 25 تا کامنت میگیره. یوتوبره اون 25 تا کامنت رو حتی لایک هم نمیکنه. اما کامیونیتی فارسی، ویدئوی 10 کایی کم کمش 200 تا کامنت رو میگیره و خیلی از یوتوبرا هم جواب میدن و اهمیت میدن</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/4330" target="_blank">📅 16:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4329">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">☠️
ساخت رادار پیامکی با Hermes Agent بدون کدنویسی + API رایگان OpenCode
⚡️
دستورات نصب OpenCode برای ویندوز، سرور لینوکس و دیگر سیستم‌عامل‌ها: https://t.me/MatinSenPaii/4259
⭐️
توی این ویدئو: 1- باهاتون راجب کسب درآمد از Hermes صحبت می‌کنم 2- با همدیگه…</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/4329" target="_blank">📅 16:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4328">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Mt4jY9cONpMKqaNp1VbZAzbNGcqf6LnFvvq9huu_oz2o3vgciNQa5gTPbZY-u4ZOhVpvOK-N6azoWz5A6McxBrOm8d94Hwk3J8fiSKX-0s9k6fgU0GKFh8E1kwx44PT81fH2Mv-CjWBiNqBaJ5ilgcZ_0a94bvNDYliV5OBPwMUyG4EHDiUom2Z-43KS_pXQxhy9i1p1JbX2-KVkYY_pR8yUujKrH_0hB8p3e7425mH12eHjGBf6XVivS-umiV6vz5xSdf9zAF26yXyOOEC5Z_TlPkrOzEj2rX2yYFTcMy-gevt9hywnXAV5xdOBJCHk-ifwqrAWVhg4I647rsspdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
ساخت رادار پیامکی با Hermes Agent بدون کدنویسی + API رایگان OpenCode
⚡️
دستورات نصب OpenCode برای ویندوز، سرور لینوکس و دیگر سیستم‌عامل‌ها:
https://t.me/MatinSenPaii/4259
⭐️
توی این ویدئو:
1- باهاتون راجب کسب درآمد از Hermes صحبت می‌کنم
2- با همدیگه OpenCode رو به 9Router وصل میکنیم و روش دور زدن یه باگ خیلی رو اعصاب رو بهتون میگم
3- از هرمس استفاده میکنیم که با سامانه پیامکی، یه کرون جاب بنویسیم(قابل پیاده‌سازی برای هر ایده‌ای)
4- و کار با پنل‌های پیامکی رو بهتون یاد میدم
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره. از api رایگان هم استفاده شده توی کل ویدئو
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/4328" target="_blank">📅 15:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4327">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Zombie</div>
  <div class="tg-doc-extra">Bad Wolves</div>
</div>
<a href="https://t.me/MatinSenPaii/4327" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4327" target="_blank">📅 15:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4326">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">خب انگار فعلا خبری نیست
نت منم اوکی شدش</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/4326" target="_blank">📅 13:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4325">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4325" target="_blank">📅 12:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4324">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHaoodi Senpai</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a627c5c6e.mp4?token=Da9cUwPQN876WC0Ru4CYh3ZDULQJXFzDx5azJ3SK6BgVmjsJS3RD2SJcNEZCgDxf1Iy5RafMzNGdSFxQiyGaFeqD25GVwzRdYXh8_p7T6RF89F9LgDW5CIGTSPrl6NNn8MsZdzDOlA3iXwjeOha9JhMDVo0PvIHJNuqaCNYFl4_2VyKsoPHE5AFOwZpHqTJeyb7HGRHJkxkIPOXppll-lQm0hqTXejfxH-mZMOxv67bpp0y7WeE_bcWREmsAysPH2ZtcReatzHeKhgKRQu0U0F4_u4A92mZzgIJqKKApjlRqbnaSoVZkEGvQFgQilFjWfMfVvAx8WlwVZXBOn1p0vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a627c5c6e.mp4?token=Da9cUwPQN876WC0Ru4CYh3ZDULQJXFzDx5azJ3SK6BgVmjsJS3RD2SJcNEZCgDxf1Iy5RafMzNGdSFxQiyGaFeqD25GVwzRdYXh8_p7T6RF89F9LgDW5CIGTSPrl6NNn8MsZdzDOlA3iXwjeOha9JhMDVo0PvIHJNuqaCNYFl4_2VyKsoPHE5AFOwZpHqTJeyb7HGRHJkxkIPOXppll-lQm0hqTXejfxH-mZMOxv67bpp0y7WeE_bcWREmsAysPH2ZtcReatzHeKhgKRQu0U0F4_u4A92mZzgIJqKKApjlRqbnaSoVZkEGvQFgQilFjWfMfVvAx8WlwVZXBOn1p0vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">The Return of
قدرت مذاکره</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/4324" target="_blank">📅 12:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4323">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/4323" target="_blank">📅 12:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4322">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">مشکلی در وجودشان وجود دارد. آنها دیوانه هستند.</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/4322" target="_blank">📅 12:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4321">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">روی اینترنتای خود من به شدت اختلال هست
همراه اول که به زور چیزی باز میکنه
ایرانسل 4g+ اما هیچی به هیچی. آپلود 0
فیبر مخابرات هم از صبح 2 دقیقه وصله 20 دقیقه قطعه</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4321" target="_blank">📅 11:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4320">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نسخه‌های اندروید(اگر نمیدونید کدومه برای پردازندتون، Universal رو دانلود کنید)</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4320" target="_blank">📅 11:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4319">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">💬
آموزش قدم به قدم استفاده از اپ CoreForge  https://youtu.be/filwdiPKN90</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/4319" target="_blank">📅 11:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4318">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">💬
آموزش قدم به قدم استفاده از اپ CoreForge
https://youtu.be/filwdiPKN90</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4318" target="_blank">📅 11:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4312">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.5.1-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4312" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/4312" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4311">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">آخرین نسخه‌های مک-ویندوز-لینوکس</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/4311" target="_blank">📅 11:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4303">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta5-macos-amd64.zip</div>
  <div class="tg-doc-extra">27.2 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4303" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🐧
نسخه لینوکس</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/4303" target="_blank">📅 11:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4302">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y2FcWdMulfPFV_TdH8x5BQpNimXMl3Po7pFtSmHvtkFoyADI9tQ5CxmpGOaoCOmqohDr_qS8fECp3JIQ-oDffaRewXHD5Itl30iEN25XNjIe0Keyo6LQhX64ygkfPjyLeDOY8WxgI897wMMkkGalnjocSgTTm66v40PipNGVyGC-vaK_lha9Vc5pdMR1b0RboNKu0Rpvm2LQ-swgK_u4Gf3g3Dz10LSdZKA1d4OboPoBjp-o56_DfPyGcOxPrQRP1bKx5nxjPnGQiTOKHSzg9e3tDFB38RUjJ8J-8893u1BtrKAElnrznc-t6afch9UJsKcdpVaO5rzd8iRIlw7P_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق معمول، پیشنهاد میکنم WhiteDNS رو راه‌اندازی کنید برای خودتون و دوستانتون
آموزش:
https://youtu.be/6Pm7kNQb3mo</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4302" target="_blank">📅 11:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4301">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اعصاب و روان نموند برامون. نمیدونیم درس بخونیم، کار کنیم، کارگری کنیم، لپ تاپو بفروشیم و دلال بشیم که بتونیم زندگی کنیم، چیکار کنیم</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4301" target="_blank">📅 11:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4300">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">میترسم پنج دقیقه بخوابم ببینم نت قطع شده باز</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4300" target="_blank">📅 11:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4297">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hm4O9aJgMXxA-rWzlYpGXylQUbOjdF1r2PScIc3arFSeuZAes68w0NHLmB2AJnPdleHgS1YCRtzvyzkORK5eAfX01clOLaYwErzuXp0q_zXTU489LHcWhEoWIvQn32VH2YaAO-InNCKyu8TpXi6O-y2I1YzDtaBg1WPOHep9bR94YQd4j_9vDU43BtQmosVXyXDvRKllvI9mGqmyNt9E8W_a8BZrKW38qDijFFts_DW4GRkke7LtAJA745R0XXE7aiXRhCMz_z08VHkJdKoVaaf-QFCy4hHgQxUVuW1elZJulJIac1MfZe5CmGVExI1jG_MUb8ACDf9Ym5FOjNnbjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YSXT4O1cZ2M8WaVpTbwwUu3h0oteTNNIAIFn-OTsXvnT41xLZyUlt5oF4V0zDFHBHJXsTo6Mk0ZY93qirlFzXlog3yS3HYD8b2u8aJbaZ6qDS0denYXC3clxwrHe1d3iNWrdp3oukLOKaSdHGu_abQbSUacc9SamNubQIEO0Jv0R1I9csHcqqMS27tGuApoFZtnRnT2nXUV0JodJnUZIWqK8G8Lla-owDzPIFjaJ5nPm60q3Q09Q7BfPyFPDBDLGwgB1BMlhqrlAET_UKp5S_zfzU7KullbMYGvO8hVwkXevIv-16uEBh8Ys6MR3m0wcERrPV0-Lc5QZVnhmQEYFWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/plbOy1kFwjAZCk0cP_6-UTL7IC54luJKL3w0eftpXcTbSua6C4S0Kc-DJortgPJFhDgTDGjuPKtwFFsnBgKsjax5nBDB8wDnfWHwKieGfEX6a8XZcJyZqClY0dutO6jsXCXlTJm_GRawcIyt3x35PyCtLHvDC2wv4d5bgneQlIf6KN8f_JDlcyAb-lgPo6ZZ464StOVRe2CDKT8toDzUPFAR3POHaX0DPrlj-8k22b4qqfcRzzvm6JwsczWG0D_ngWOFJQP8R3CjNbcqLl6nwwGEy2thQOxqxT8BiIffFn4dlZdRE99k3S2CPzhJoyiXN080Cr78iwppJsnMXrfJCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی هزینه‌ی هوش مصنوعی از حقوق مهندس هم بیشتر می‌شه
خلاصه:
شرکت «آنتروپیک» (Anthropic) حدود ۲.۳ برابرِ پولی که بابت حقوق و دستمزد می‌ده، خرج زیرساخت و پردازش (Compute) می‌کنه! یعنی با حساب حقوق سالانه ۲۲۴ هزار دلاری (با احتساب تمام مزایا)، سالی ۵۱۵ هزار دلار به ازای هر مهندس خرج پردازش می‌کنه. در حالی که ۱ درصد از برترین شرکت‌های نرم‌افزاری فقط ۸۹ هزار دلار و شرکت‌های میانه بازار (میانه آماری)، کلاً ۱۳۷ دلار خرج می‌کنن. حالا ۳ تا سناریو برای سال ۲۰۲۹ داریم که نشون می‌ده این شکاف عمیق چطوری ممکنه پر بشه.
همونطور که اشاره شد، آنتروپیک ۲.۳ برابر حقوق پرسنلش، در حال حاضر داره خرج زیرساخت و پردازش می‌کنه. با حدود ۵,۰۰۰ تا کارمند و تقریباً ۱۰ میلیارد دلار هزینه‌ای که توی سال ۲۰۲۶ برای آموزش مدل و استنتاج (Inference) می‌کنه، سهم هر کارمند سالی حدود
۲ میلیون دلار
هزینه پردازشی می‌شه؛ اونم در مقابل حقوق و مزایای کلانی که برای هر نفر احتمالاً بالای ۵۰۰ هزار دلاره!
بقیه بازار نرم‌افزار خیلی از این رقم‌ها عقب‌ترن. ۱ درصد از برترین شرکت‌ها سالی ۸۹ هزار دلار به ازای هر مهندس روی هوش مصنوعی خرج می‌کنن؛ یعنی ۴۰ درصد از یک حقوق ۲۲۴ هزار دلاری برای یک مهندس ارشد. این رقم برای شرکت‌های میانه بازار فقط ۱۳۷ دلاره! اختلاف فاحش اینجاست:
۲.۳ برابر حقوق
در لبه‌ی تکنولوژی
۰.۴ برابر حقوق
در صدر بازار
نزدیک به صفر
برای شرکت‌های معمولی بازار
حالا بقیه‌ی بازار چقدر می‌تونن خودشون رو به این سطح برسونن؟ جواب این سوال توی ۳ تا سناریو خلاصه می‌شه.
(توضیح نمودار خطی(عکس سوم): نمایش سه سناریو برای هزینه‌های هوش مصنوعی به عنوان درصدی از حقوق مهندسان تا سال ۲۰۲۹؛ در سناریوی خوش‌بینانه، این رقم به رکورد ۲۳۰ درصدی آنتروپیک می‌رسه)
سناریوی بدبینانه (کاهش قیمت توکن‌ها برنده می‌شه)، سناریوی پایه (رشد ۱ درصد برتر بازار کند می‌شه)، سناریوی خوش‌بینانه (بقیه بازار تا سال ۲۰۲۹ به نسبتِ هزینه آنتروپیک می‌رسن). هر کدوم از این سناریوها، هزینه سالانه هوش مصنوعی به ازای هر مهندس رو نشون می‌دن(عکس دوم)
توی سناریوی خوش‌بینانه، فقط هزینه هوش مصنوعی به ازای هر مهندس، با کل درآمدی که یه کارمند توی شرکت‌های معمولی SaaS تولید می‌کنه برابری می‌کنه! همین الانش هم شرکت‌های آنتروپیک و اوپن‌ای‌آی به ترتیب ۱۴ میلیون دلار و ۶.۵ میلیون دلار به ازای هر کارمند درآمد دارن، که بالاترین رقم توی لیست ۲۰۰۰ شرکت برتر فوربز (Forbes Global 2000) به حساب میاد.
ساختار هزینه‌ها، دقیقاً جا پای ساختار درآمدها می‌ذاره.
موتورهای محرک توی سناریوی خوش‌بینانه:
قیمت مدل‌های پیشرفته ثابت می‌مونه، چون هزینه‌های آموزش به ثبات می‌رسه و تقاضا از عرضه جلو می‌زنه. فرآیندهای کاری مبتنی بر ایجنت (Agentic Workflows) نسبت به چت‌های معمولی، چند سر و گردن توکن بیشتری مصرف می‌کنن؛ طوری که «گلدمن ساکس» پیش‌بینی می‌کنه مصرف توکن تا سال ۲۰۳۰ حدود ۲۴ برابر بشه. تازه، اگه شرکت رقیب قابلیت‌های جدید رو سریع‌تر عرضه کنه، دیگه پرداخت صورت‌حساب هوش مصنوعی یه انتخاب نیست، بلکه یه اجبار حیاتیه.
ترمزها در سناریوی بدبینانه
: قیمت توکن‌ها توی سه سال گذشته، هر سال ۱۰ برابر کاهش پیدا کرده. مدل‌های متن‌باز (Open-weight) دارن با کسری از هزینه‌ها، شکاف کیفی رو پر می‌کنن. از طرفی شرکت‌هایی که مصرف هوش مصنوعی رو بر اساس نقش یا حجم کاری کارمندان سهمیه‌بندی می‌کنن، می‌تونن شیب این نمودار هزینه رو خم کنن و کاهش بدن.
نظر شخصی: اصلا نمیشه پیش‌بینی کرد:) با اومدن ایجنت‌ها، سناریوی توکن داره مطرح میشه. از اون طرف، چین غوغا کرده و با رایگان عرضه کردن مدل‌هایی مثل MIMO و GLM-5.2، واقعا نمی‌تونم نظر بدم.
منبع مقاله:
https://tomtunguz.com/ai-spend-breakeven-2029/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/4297" target="_blank">📅 00:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4296">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">یه مقاله از نیویورک تایمز(با اینکه ازشون خوشم نمیاد) دیدم که توی هکرنیوز بحث‌برانگیز شده. داستان در مورد اینه که با پیشرفت سریع مدل‌های زبانی، مهارت‌های کسایی که فلسفه خوندن، چطور توی بحث‌های اخلاقی هوش مصنوعی و Alignment مدل‌ها داره به شدت کاربردی می‌شه. و انگار یه بازار کار جدید داره برای این رشته شکل می‌گیره =)
لینک مقاله:
https://www.nytimes.com/2026/07/05/business/philosophy-majors-ai-jobs.html
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/4296" target="_blank">📅 23:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4295">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اگر میمو روی اوپن کد بهتون ارور ۴۲۹ داد که به لیمیت رایگان رسیدید، نترسید. یه continue بگید دوباره میره ادامه:)</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/4295" target="_blank">📅 21:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4294">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اگر میمو روی اوپن کد بهتون ارور ۴۲۹ داد که به لیمیت رایگان رسیدید، نترسید. یه continue بگید دوباره میره ادامه:)</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4294" target="_blank">📅 20:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4293">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UshaLWCcnPJu2T6iL0pAbRIwCxwW476xM70b7n4yAqmiyIybIjHD_ghimL91jpiXnSAbP2cysM-KGq5vKoc18l0VbLVpt7nHB2ggQclC7z0BOqWyc7dlMJzd4rFY3oBcW_D2cXtig_4GRG-1fKPlAqu4vQfG47s-TU06d1GwoP_Zm7hnOS6ONYkd7FbUyq2YDVv1JKAqbdvtteh36ZDvpQwvX2BX4NedJTEMcbLlJZp_rce-P9M90P8kZNuDhvfaSMJdIdHh1KOFnsVs211ktysUnROHBz-4WO1ECXyJDzL34GRO5VykYerqQfb8Udpsyb_ccmylyUaxd2tBl_UvxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زبان برنامه‌نویسی Cyrus(کوروش) چیست؟
سایروس یک زبان برنامه‌نویسی متن‌باز و جدید است که برای ساخت نرم‌افزارهای زیرساختی و سیستمی طراحی شده؛ یعنی همون نوع نرم‌افزارهایی که نزدیک به سخت‌افزار کار می‌کنن و به سرعت و کنترل دقیق نیاز دارن (مثل سیستم‌عامل، درایور، یا ابزارهای زیرساختی).
فلسفه اصلی سایروس این است: هیچ اتفاقی پشت پرده و بدون اطلاع برنامه‌نویس نیفتد. یعنی کد باید همیشه روشن و قابل پیش‌بینی باشد و برنامه‌نویس دقیقاً بداند هر خط کد چه کاری انجام می‌دهد، بدون رفتارهای پنهان یا پیچیدگی‌های اضافه.
چند ویژگی مهم سایروس:
بدون گاربیج کالکتور
: بر خلاف خیلی از زبان‌های مدرن (مثل پایتون یا جاوا) که حافظه رو خودکار مدیریت می‌کنن، سایروس این کار رو به خود برنامه‌نویس می‌سپارد. این یعنی کنترل کامل و دقیق‌تر روی مصرف حافظه، که برای نرم‌افزارهای سریع و حساس خیلی مهمه.
کامپایل مستقیم به کد ماشین
: سایروس از فناوری معروف و قدرتمند LLVM استفاده می‌کند تا کد رو قبل از اجرا به‌طور کامل به زبان ماشین تبدیل کند؛ نتیجه‌اش برنامه‌ای سریع و بدون واسطه است.
سازگاری استاندارد با سیستم‌عامل‌ها
: طوری طراحی شده که به‌راحتی با نحوه‌ی کار سیستم‌عامل‌های رایج هماهنگ باشد.
سینتکس ساده و مینیمال
: تلاش شده که نوشتن و خواندن کد تا حد امکان ساده و بدون ابهام باشد.
قابلیت‌های پیشرفته بدون هزینه اضافه
: مثل ژنریک‌ها (نوشتن کد قابل استفاده مجدد برای انواع مختلف داده) و چندریختی (Polymorphism)، بدون این‌که سرعت اجرای برنامه رو کند کنند.
ساخت افزایشی (Incremental Build)
: یعنی موقع تغییر کد، فقط بخش‌های تغییر‌کرده دوباره کامپایل می‌شوند، نه کل پروژه؛ این باعث سریع‌تر شدن فرآیند توسعه می‌شود.
هدف کلی سایروس این است که زبانی باشد نزدیک به سخت‌افزار و ماشین، اما بدون این‌که خوانایی و سادگی کد قربانی شود.
این پروژه هنوز در حال توسعه است و به‌تازگی نسخه بتا (Beta) آن منتشر شده. اگر دوست دارید بیشتر بدانید، امتحانش کنید، یا در توسعه‌اش مشارکت کنید:
مستندات:
https://cyrus-lang.ir/en
گیت‌هاب:
https://github.com/cyrus-lang/Cyrus
کامیونیتی:
@cyrus_lang
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/4293" target="_blank">📅 18:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4292">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">آخرش یا atomic mail ایرانو بن میکنه یا ما atomic mail رو از کل جهان ابیوز میزنیم
😂
😂</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4292" target="_blank">📅 16:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4291">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دیروز و پریروز می‌خواستم ویدئو بذارم، اما با اینکه موضوعات زیادی دارم برای ویدئو ساختن، حس کردم که کمی عجولانه‌ست و تایم گذاشتم که هم خودم کمی بیشتر با ابزارها کار کنم، هم وقت داشته باشم برای مطالعه‌ی شخصی که محتوای باکیفیت‌تری ارائه بدم. برای همین تا وقتی حس نکنم کافیه، ویدئوی جدیدی منتشر نمی‌کنم
❤️</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/4291" target="_blank">📅 16:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4290">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FfToGlAcfjuhUE0B485udNzHsab7vhwmRt-ROFueJIFTprsH7QuYM7J9vQrDkEdcmLfeRHpcq-KsVwjHyX1fv3M41wlYiLDs20gs9O50W9XiYpMSQ9e9EHyX9ffzW_s28vcZ1lCcJjS7WSJPE75s8xntJQNsX-SfZA-4yPmNa0eZnpC8JlShM3Xs9jfN5o5uhgDqnB_cVx7rM8G6uIbA_zQMiNwlwuOCv0vOVyGMD1mEvaWHiTPZpp5PwMFPT9mZIc_ukNCGDo0tSYi2BdDRqJCGTeGx5UfZuEpOc5irYCQx9NL_vVPN4MNg4MUqOxId2PmLEqGxldQkcdltW1-VEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا هزاران پست سیو می‌کنیم ولی هیچ‌وقت نمی‌خونیمشون؟
🤔
اسم علمی این رفتار
Digital Hoarding
(ذخیره‌سازی وسواسی دیجیتال) یا "
پارادوکسِ بعدا می‌خونم
" هست.
این اصطلاح رو اولین بار
Van Bennekom و همکارانش توی سال ۲۰۱۵
و داخل یه مقاله توی مجله‌ی
BMJ Case Reports
مطرح کردن؛ اونجا یه مورد بالینی رو توصیف کردن که یه مرد ۴۷ ساله هر روز حدود ۱۰۰۰ عکس روی کامپیوترش ذخیره می‌کرده بدون این‌که هیچ‌وقت سراغشون بره.
از اون موقع، این پدیده به یه حوزه تحقیقاتی جدی تبدیل شده. تحقیقات جدیدتر (مثل مطالعه‌ای که سال ۲۰۲۳ توی مجله
Journal of Obsessive-Compulsive and Related Disorders
منتشر شد) نشون می‌ده Digital Hoarding با الگوهای شناختی و هیجانی شبیه به اختلال وسواسی-جبری (OCD) و وابستگی هیجانی به اشیاء مرتبطه؛ یعنی حذف‌کردن یه فایل یا پست، همون حس ناراحتی رو ایجاد می‌کنه که دور انداختن یه وسیله فیزیکی.
چرا این اتفاق می‌افته؟
👩
هر بار که پست مفیدی رو سیو می‌کنیم، مغز دوپامین آزاد می‌کنه؛ حس «پیشرفت» بدون این‌که واقعاً کاری انجام داده باشیم.
✈
ترکیبی از
FOMO
(ترس از دست دادن اطلاعات) باعث می‌شه به‌جای مصرف محتوا، فقط جمعش کنیم.
💤
نتیجه؟ انبار دیجیتالی از Save‌ها و بوکمارک‌ها که عملاً هیچ‌وقت سراغشون نمی‌ریم.
چندتا راهکار عملی:
قانون 5 دقیقه
: اگه محتوا کمتر از 5 دقیقه وقتتونو می‌گیره، همون لحظه بخونید؛ وگرنه رهاش کنید.
سقف هفتگی
: حداکثر ۵ تا ۱۰ آیتم توی یه هفته سیو کنید تا تلنبار نشن.
دسته‌بندی و پاک‌سازی دوره‌ای
: هر چند وقت یه‌بار Saved items رو مرور و پاک‌سازی کنید.
اگه واقعاً مهمه، به‌جای سیو کردن، همون لحظه یادداشت بردارید یا اجراش کنید.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/4290" target="_blank">📅 16:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4289">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">آخرش یا atomic mail ایرانو بن میکنه یا ما atomic mail رو از کل جهان ابیوز میزنیم
😂
😂</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/4289" target="_blank">📅 15:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4288">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JYFsEbXT22E0Pa4nZSpZnrwY6mXGgs-0GtZZncse5mpHrIUVvRTQDpC1ilCurM-BxJinrzYdR2RlRH9ryLQSuIRerIpsSxlLF4SOW_nZIDF3SV7pE1NBFYBZyxid_37Yt5ALIBhGSlKRjma_RZV0fKJlwnZ-XgJccbry8PHDOhJ5-PJ1sWLqNAXDHxPcVH2HVIo3trush9xHKXlBgh652M-40qvRUgCyNP0EsAnUN9m51ahPw0IZ5M9n9LfNdjQZqHgTvqcfjDhIMuDYrpIoygjIYkXY3fqpd2JfmtZrgphg6vDzx6JWhI7Any_SN1yWGBvTw1FZNGMFtBrVaMBArg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمس نتونست لینک مقاله‌ای که بهش دادم رو باز کنه به خاطر firewall امنیتی توییتر، خیلی راحت با قابلیت Browser که اینجا: https://youtu.be/_30_ng3Hyfs یاد دادم، روی دسکتاپ برام هم عکس‌هاش رو دانلود کرد هم مقاله رو کامل ترجمه کرد:)</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4288" target="_blank">📅 14:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4286">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YL8UwGKX996vyx6BhJo57k3PQ2sTBOwVIhznl9F_EopBJ3ehGfX4N6Ds1UkNdn0EsIJqkcQ9nHkQfjdhcakv0Cm7-8YRVFeZoHLnr6YloZjPtm4edR0zG2W2IX6o20EVPvZKEFsOnbFOL5yJ9pRpNUkqSH9qdud3E_iKHyQrXPAG2hgckNGp5GsC9cz3wSmgDS8z0fFDYEHwyKJiM9MZv6Nb_l1K40-7cztu6DP-6vOerWWxyK1QADsycYU9IZmVGvipbWDEe2TfbcrMvWl0CUms5uQ3fCsbaH4j9j3AFGhAJh12jF2HfepLZC3KL8FHdV3HeWkiOCrEW3-4gaEcSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hNY0ibmByqAu4634ID-KZ1RWXpcG5cy_YGJ2Nj1qUbxuJrICsZiwaDlIyl7chrC0nE_AOSUmA5Bg951LVU_O9xjP1S4ht1-MOF9qAXvxVCib-tr-Et6MK6L1PcUddzOIE9U3yeuVYa4Jgu6vM_AIt3bGkCrhrPSD2o0blBIfviw5n8kDhsQDQ8oNlbAnKMkwioESl26LE9kMdM-weL6Q0RI9zEr4O8miO9mYL9mmgDzhKQlOCj9dgyx6pKWQmbNJlxqniRyKc9_rTkrWt0eaI08aH0dh8aBNrXZebdmbx0tOEeYR2rj-SImwR3T_NzXi2Zg63mckRRAgVmb5oTqmlg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هرمس نتونست لینک مقاله‌ای که بهش دادم رو باز کنه به خاطر firewall امنیتی توییتر،
خیلی راحت با قابلیت Browser که اینجا:
https://youtu.be/_30_ng3Hyfs
یاد دادم، روی دسکتاپ برام هم عکس‌هاش رو دانلود کرد هم مقاله رو کامل ترجمه کرد:)</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/4286" target="_blank">📅 14:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4285">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fYxjobVbdItL_XFb8yeHBRAZ0lF-0bkShfBG7HNK_hLmh87lYO9iqL6dXiE3qvpvdkmcph20XwTsMi4j7nMIyE7VCo6aFlPcERA0QrXWE4QXeVgin0GhyoYGKrxXFO6w38gaiKJg4whx26s7DlLYX-7Z-TcLGWXpnaOuv207N6eX04l27ZfegoYkdlC4ixy2KDNLkfdgQt-L1T87IA0t73jzACJuiS03DyY6_4PZTGEtcdalTKD3pqZzfeyaTTe3-diVL3-cRpPc8CPr2ovWO3S_qndmTF4xO9anjEsEofsSnDQOIg8fyAtkta_xgC054bO6JLscIPHV9c0EwCy1BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه با docker کار می‌کنید، احتمالاً درگیر زدن پشت‌سرهمِ دستوراتی مثل
docker ps
و
docker logs --tail 50
هستید تا چندتا کانتینر رو همزمان مدیریت کنید. این کار هم خسته‌کننده‌ست و هم ترمینال رو به هم می‌ریزه.
ابزار
Lazydocker
دقیقاً برای حل همین مشکل ساخته شده؛ یه TUI برای داکر و داکر کامپوز که تمام کارها رو با شورت‌کات‌های کیبورد براتون انجام می‌ده.
-
بدون switch کردن:
همه چیز از مصرف منابع (RAMو CPU) تا لاگ کانتینرها به صورت زنده توی یه داشبورد یکپارچه نشون داده می‌شه.
-
سرعت بالا با کیبورد:
لاگ دیدن، ری‌استارت کردن یا پاک کردن کانتینرها فقط با زدن یک دکمه کیبورد انجام میشه (بدون نیاز به موس).
-
پشتیبانی کامل از Compose:
سرویس‌های داکر کامپوز رو هم به خوبی می‌شناسه و مدیریت می‌کنه.
-
بدون کانفیگ:
با زبان Go نوشته شده و فقط یه فایل اجرایی باینریه؛ نیازی به نصب سرور یا دیپندنسی اضافه نداره.
و خلاصه این ابزار سرعت کارتون رو چند برابر می‌کنه.
گیتهاب Lazydocker  + آموزش نصبش
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/4285" target="_blank">📅 14:23 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
