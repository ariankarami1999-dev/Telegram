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
<img src="https://cdn4.telesco.pe/file/ZPSi90vRTDu91IdczzyjE9fw1FWiyCs2jDhaycyQK1U3sOidwlYF83dvDkwBfMmKM_SR7h-ydBliikj3CZvytwqdnHuT6u91Ogrlvt108zv0-jMkpPA6jyK-sNdHQ7LX7xroOg7r5dL7URCrmVKcvpSJzpa5jzzxYhmJidIqIVTRfe0huENWHehycAXVtemd9-G8RQHl4ff2C_uBEIjvqCqom8EJfMpuQ0MToUeyK1qQ2EW_H2KhGjkLAk_teovl5acPVX0d3nHEcRuNNbsG5CMunicQ1RkIWqQwCOlUxBRD7qYhJCOmAM79aiwTf7pUB7JMwcclVxps4Ht8wzEQrw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 996K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-30 09:11:44</div>
<hr>

<div class="tg-post" id="msg-148491">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
نماینده آمریکا در سازمان ملل: درِ بازگشت ایران به میز مذاکره همچنان باز است، مشروط بر اینکه این مذاکرات با حسن نیت انجام شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/alonews/148491" target="_blank">📅 09:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148490">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ibD9uIHzRzxdypIwYGGrU6e8jpRZ4zKyKp5C8jL2j9q7FhcDzRozSCh8I-GWhSKBBG5QwdYrhcetgZ_CXinqyaZJyciHkU9r1luqp1aNxR53NZOVZcmUcMUMqvQRv_vMOCaF31kpW5YNhyKwuHkSfdP1eFZFEwdC7vfqVLz5M6N1pY8NG2ie4K_Y9WmaUfl6QNP4czsWYlwtMPgbdig4a-mqHLTPBdz4gVXr8hC1PhvBONRTphJ4wEPFJ9mN9Tlp2qfcsV2pM5ZXviMmBL6GX0hhmUZ1Ev0eydoClgnyWjNup9JOZcVpgBwu0Gqb6Eqvyo1DhF4wDba9wGj1V2i2cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروی هوایی اسرائیل منطقه اطراف ارتفاعات علی الطاهر در جنوب لبنان را هدف حمله هوایی قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/alonews/148490" target="_blank">📅 09:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148489">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9LORCYKRvdQdTAd5LS-2ymlFkVaPrH2C-OONapH9UjlwfJrEVA47VCAarTTBFVEBob77n1EWTrZReyLOfbFt8Z6wtlC8bevgmCm1Yrjjmqer7tXH--axCzNq13UPAZJW9Sp6EwzW10egaRVVLKUZ-Vk7cnU3OAILqUjmTbJqdOesdN-jQrJOYA7TgEhwkbipUa36KVE0pMk3RVCohMVodxbE0Y1aWZx1ChKQIeuY-t0KpWfWgQTUqdGR3BEai00PDE1JkoRDZho9qyZEd87HVoUV6JAvQuC1NApRAK397vJP6NmUgWqfSthilw_jhFo7Gg3Sj87H8-7bUtWpl0BPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله هوایی پاکستان به شرق افغانستان
🔴
الجزیره به نقل از یک منبع دولتی افغانستان: جنگنده‌های پاکستان به ولایت کنر در شرق افغانستان حمله کردند.
🔴
در نتیجه این حمله شماری کشته و زخمی شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/alonews/148489" target="_blank">📅 08:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148488">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
سپاه : لحظاتی پیش انهدام یک پهپاد MQ-1 در آسمان تنگۀ هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/148488" target="_blank">📅 08:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148487">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpC2tNIMExLq-3cVICW9OELS7UqH0uA9wq_ZZRVmu3bEfBSA7-Lrebp4cxlwJf_DhcNK1c1-olVPuDSz0S2FT6gurW8gPvuRpHkLyDcNsQ9F1c0kBEb6KxPG0TGWSg5gARkj-eJTBUEkSdDoKyfbzZDtKznhGDvGqqFuVAn_9pT8UV5NYYImsvCI-zc70OCD18RGSQVoCpd3DpFw_7OoKVCZI3e3G4xilpIJyZKr6nXSCSFdB8zC7fP6PhHxm_MH-TsC73jmXrC9xMRXn2yyzrVQRu2PNLZ4vnmUxcfBbG7PrmWtdJWVGz7ftuOgPRKH4yFXH8AQ2GxJzDSiAmDE8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: قیمت بنزین و بیشتر کالاها در دوره بایدن بالاتر بود
‏
🔴
دونالد ترامپ، رئیس‌جمهور آمریکا، با مقایسه وضعیت قیمت‌ها در دوران ریاست‌جمهوری خود و جو بایدن، مدعی شد قیمت بنزین در دوره بایدن به‌مراتب بالاتر بوده است.
‏
🔴
ترامپ همچنین گفت این تفاوت تنها به سوخت محدود نمی‌شود و به ادعای او، قیمت «تقریباً همه کالاهای دیگر» نیز در دوران بایدن بالاتر از دوره ریاست‌جمهوری او بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/148487" target="_blank">📅 08:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148485">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6EQPGUltpP8qURBp4f5HBgDfDXeQH5MpGag21UPBWnUAET33VLvXSzQ7mEY781vK5UJ3A-q8TH93ZDNwKdE-MgJ_eRJmcRIvcnDUsSAJ4A8aIkx1xiIc7YUaeHt92KbVd0xk2EspOWGa-oYydLqzGhNOqOJB-MVGAA2Ay_kaZMdvOmV5NFquBl0bRQrDSLTmrbx8OaHThNkMeGw5jF7Rowv8UiUrC7sXXHXZ_Ro5JMeQn1fRolFWFJCrVppvJAL21Qvu27GiqNruQHFcTnULoVQgI66W2fj1EdYY2K5rC38EFSxgLjEJxB0-xFHjy7VK3ZmfDHNZGeBThOIdkfxmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f270a07dae.mp4?token=ScslekD_TsfeEe4HbUyVcwRISfX3YkriDIWh3gxOwlcDtHqx3VrsZIDXOtiMLpSWPiEaf_sKIDnDExjewrYJGjfpk1dhuU0hynKQQM1r_m-akrKAN-ARN3nNCKY0-By3A4w3OsP5BGcmQry9ZT_qkziWFMB2ZJYTlGCPNa7LGRU5H4ggKID0KhYbsdPeAYvF5SQO9MBlIcRX0Ddnp1GTBnOiigWTukMaKQeyNDZHDaQwq5n08bHSEjC00F99DygtC0zVrrCktjT5Fkr9cZdBNnJEAbdJcBXoG_hPDX7ktz2iA0gFvUBJA8D3b0GSr7p-KXxqNTcfgn02PscRvUw9KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f270a07dae.mp4?token=ScslekD_TsfeEe4HbUyVcwRISfX3YkriDIWh3gxOwlcDtHqx3VrsZIDXOtiMLpSWPiEaf_sKIDnDExjewrYJGjfpk1dhuU0hynKQQM1r_m-akrKAN-ARN3nNCKY0-By3A4w3OsP5BGcmQry9ZT_qkziWFMB2ZJYTlGCPNa7LGRU5H4ggKID0KhYbsdPeAYvF5SQO9MBlIcRX0Ddnp1GTBnOiigWTukMaKQeyNDZHDaQwq5n08bHSEjC00F99DygtC0zVrrCktjT5Fkr9cZdBNnJEAbdJcBXoG_hPDX7ktz2iA0gFvUBJA8D3b0GSr7p-KXxqNTcfgn02PscRvUw9KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امشب مردم تو آسمون شهرای مختلف این تصاویر رو ثبت کردن و فکرکردن سفینه آدم فضاییا رو دیدن درحالی که از این بادبادک های چراغ دار بودن
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/148485" target="_blank">📅 08:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148484">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6VmyhU6R6iAx87K2RnpsP7MG_GsKqdYAeFTcBo_RVlL_7-9qlAR9WRW6HlNurQc2oejQcote4xPCAfDveQqAZKhHsXLMyU3h9EL1Kl0UFGFipXXeIE-zMlJzP4xvsQDyBaQ_GXYU9a_4Bqk-6BHUcyDzmS6x-U-GSqHidX8OTFaaCVHlj8JISD4oVWE-79L_hko3fLcOMEDRUxAFv-Ko2ej_4O0U8JL5XQ1uRZ_in8ZcBh5NeaRGGTNz8FRWwWg7DLS0cBaH_1GExw2Lhkggr-gfmlVE6CZXUaxhh_7qsd62klswKt4LKvxrkFGHhebd-EDYSeijn0ML6qck4r9sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت ۱۰۱ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/148484" target="_blank">📅 08:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148483">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEBhDSzLdjzaAC4NiEuiwaA7iDCyGG_N9jyiZ25KH8ebqulIzgmNoogL473zbZ076nlCH5mD2yAtsf0ytYwN8MwqLrJsbwO2OjN4BDEs2EJ6X56TMQ_YKNp1IvDm_HO3F4HF-buGqqpcUElIq2etNKMSIFDlolFGIihqFILtdMvQi1_x84Ah9dV0Ysebo6bY2eEMKEXzFJ5eDNOEuFLq03cH-V3LFshMnyLRVW7R3Xx-QOz8MDk-lbNP5PMogjTgoFrN4epFuXEdtgvDt_OiyaNZqlqQtL-NA0vNdBGHwMr-QH2SlCpXB0UdgCNRBX-SLFNzeGW4CMrUUSAbPEKBmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: تنگه هرمز ظرف دو سال آینده بی‌اهمیت خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/alonews/148483" target="_blank">📅 07:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148482">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJCC3gt1fShD66YG112j32FT1OXXp3pmzaiiToa9O5ydVxJNmK07EPhBufkXOoOjNZjxH_IMNrqRCgWKBkwMZ-j2c-_ZGfEovxdni_xL7t5LtPctX15nHVL9v0ynvz5HHUiSLTAd2JyvZsy9fTFvTuqNjXV8YELKNJkM52Md-oacJTv95gz1YS3YSivXal7vZVEWqumaYE1wcauoz431wXvdJbD3qCLAHSqo7CoeIPmMQbf-cQS8ljywP6eiT_4OKJxeDwsLgzhF_9b9USbMCG8S78KPBz_lESKRkGoYFOYDALDPZ28d9JOnwitUWc7ZOBGFo--drUbmhuwz0a7pYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس:
شماری از دستیاران و حامیان مالی سابق
کامالا هریس
معتقدند او ممکن است در نهایت در
انتخابات ریاست‌جمهوری ۲۰۲۸ آمریکا
نامزد نشود.
🔴
آکسیوس با
۸ دستیار و مشاور سابق هریس
گفت‌وگو کرده که
۵ نفر
احتمال نامزدی او را کم دانسته‌اند،
۲ نفر
شرایط را ۵۰-۵۰ ارزیابی کرده‌اند و تنها
یک نفر
انتظار دارد هریس وارد رقابت شود.
🔴
با این حال، هریس هنوز
تصمیم نهایی خود را نگرفته
و همچنان در حمایت از دموکرات‌ها فعالیت می‌کند و با مقام‌های این حزب در آستانه انتخابات میان‌دوره‌ای در ارتباط است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/alonews/148482" target="_blank">📅 07:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148481">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GsyRwQKPNZKC11DkCLcN8ldfi3jaNgRfh374l3qbRXfPuh2P0o-oPtYkRe2gzCDuLJPDPB6H2AU6ZNHWKrP97bqSkzawC_Q8IPzkf2C6RjUpUq1CuLlIfWpl0W1yFKaGRvWkK1eAUNVvOR30aVw03-zk8fU-rfhP05s2N-02FWKVvquYtdAFD8a8_Z_9gLAJHnmgQCIp81TjIGo33qlNtTf3-0qfUXNGIL1zBExt5PcHGTpgWN4Lg2LB-n5_8PvXUhxyEmVjkon1-8B3TGC3Ubrg-6YQO2Jz0qN8p_iyEP1EDeiInMXmZwjb6jAx-u877CKNrdZuRcwq7z-Xq6OBxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
مدارک رسمی «دیپلم تا دکتری» فقط در ۱۰ روز!
✅
قانونی، قابل استعلام، کاملاً غیرحضوری
✅
مناسب مهاجرت، استخدام، ارتقاء شغلی و ادامه تحصیل
✅
ترجمه رسمی و تأیید توسط تمامی نهادها
☎️
مشاوره تخصصی و رایگان
:
https://t.me/irantahsilat_support
📺
عضویت در کانال
:
https://t.me/+1I9Ex4YFtcZkOTY0
https://t.me/+1I9Ex4YFtcZkOTY0</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/148481" target="_blank">📅 02:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148480">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75f25a1f47.mp4?token=RUriKayR-5vtvyErcGjYEH1sDgl-AkERZUE7NKDd3CFYkesFsrw-eX7E843cnKYsdSZfX8eeRxTnahBaOjNKUA7oWHuzyaPCs5m55c5LtH4dhndbao44vLXko5VFtRyRDpdfnjC01ApBJdsTaEX5vwKmAqd3WWEXkNxUcN9MYyHdcbBaCj2llWvUXgnuQ71ewvFEt0mRX6XDVq0fwZAKDJ-AJzaQYarxo-Od4Zc0lTUycL2LDfUgPhv6_br6N91bZp74MbsMsPVYis0n2q2zJV6khF2vxifM7zhcDTi5keKawLQ0Wu2D3u1CsXrNPeDT94hE6lJgQ4vaOiVy89QbGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75f25a1f47.mp4?token=RUriKayR-5vtvyErcGjYEH1sDgl-AkERZUE7NKDd3CFYkesFsrw-eX7E843cnKYsdSZfX8eeRxTnahBaOjNKUA7oWHuzyaPCs5m55c5LtH4dhndbao44vLXko5VFtRyRDpdfnjC01ApBJdsTaEX5vwKmAqd3WWEXkNxUcN9MYyHdcbBaCj2llWvUXgnuQ71ewvFEt0mRX6XDVq0fwZAKDJ-AJzaQYarxo-Od4Zc0lTUycL2LDfUgPhv6_br6N91bZp74MbsMsPVYis0n2q2zJV6khF2vxifM7zhcDTi5keKawLQ0Wu2D3u1CsXrNPeDT94hE6lJgQ4vaOiVy89QbGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجار انبار مهمات در اطراف حلب، سوریه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/148480" target="_blank">📅 01:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148478">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a1ac39bc78.mp4?token=t7MeXavsehpkIl3UUaFDMzU6O18jnoH8LjIpcQCZgQ2fZWCjuEJjfHMgeRxosMurpB7c4HnwffwhQyFr9BzfuGNeoyTULx75vXSxt2sT-ssV66pyrzHMWLl1VpsT_5gH4jUzgmjX8aJVpgTNutOqd-UEtZBq0yXUtej6r21I89GHNTMkgzWF-nVqwtJdQ1kjJe4ba_rhOt1UIBwg211aIsd_gWuVCnqZFUKetUzfILqEQSfzqqqk1gFHvawkE9ZPNO7RXriJ7BOOuyAa_1oAlmf4Akc3-Cd1d9gmSDoR5Lnt30jXCvXidYqoC1gRLdZM-VLN-wA_LXgKzQwnNHME4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a1ac39bc78.mp4?token=t7MeXavsehpkIl3UUaFDMzU6O18jnoH8LjIpcQCZgQ2fZWCjuEJjfHMgeRxosMurpB7c4HnwffwhQyFr9BzfuGNeoyTULx75vXSxt2sT-ssV66pyrzHMWLl1VpsT_5gH4jUzgmjX8aJVpgTNutOqd-UEtZBq0yXUtej6r21I89GHNTMkgzWF-nVqwtJdQ1kjJe4ba_rhOt1UIBwg211aIsd_gWuVCnqZFUKetUzfILqEQSfzqqqk1gFHvawkE9ZPNO7RXriJ7BOOuyAa_1oAlmf4Akc3-Cd1d9gmSDoR5Lnt30jXCvXidYqoC1gRLdZM-VLN-wA_LXgKzQwnNHME4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو آسمون مشهد هم بشقاب پرنده دیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/alonews/148478" target="_blank">📅 01:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148476">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7acf398c7.mp4?token=hy6UjUj7JPitmwz57jZw30NMLpGm93lQNXr3vm-ui7SdNSCspmQ1dyMFMiJwaOocjSwIlOQs_YulQDaGeNz8yHID-pHGV_aaQN_Wr2NAk4uXKNSARenxazowQuVzgYNsOViEWdcUv1CAptQQStnKINPrueALuOrsYHAgUMqX3QlGK_lQS10Ll7P-y2hl03PVv6x2OhLhkkPVL2xnSEotao6CJzjeoPhm2Mk8bSNSsK-t84L3jsSdcpOlMzC21XSSFby4mKm44iwV3o3LUF2YmDvru9HxLWtU6SeVeYYpcFzn0iXMATYFpGUz6tSlsjUi12oW-qbqxOaovw-rutw_gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7acf398c7.mp4?token=hy6UjUj7JPitmwz57jZw30NMLpGm93lQNXr3vm-ui7SdNSCspmQ1dyMFMiJwaOocjSwIlOQs_YulQDaGeNz8yHID-pHGV_aaQN_Wr2NAk4uXKNSARenxazowQuVzgYNsOViEWdcUv1CAptQQStnKINPrueALuOrsYHAgUMqX3QlGK_lQS10Ll7P-y2hl03PVv6x2OhLhkkPVL2xnSEotao6CJzjeoPhm2Mk8bSNSsK-t84L3jsSdcpOlMzC21XSSFby4mKm44iwV3o3LUF2YmDvru9HxLWtU6SeVeYYpcFzn0iXMATYFpGUz6tSlsjUi12oW-qbqxOaovw-rutw_gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دقایقی قبل در آسمان تهران شی شبیه به بشقاب پرنده دیده شد و بسیاری از مردم گزارش کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/alonews/148476" target="_blank">📅 01:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148475">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
هم اکنون فعالیت‌های گسترده سوخت رسان‌های آمریکایی در خاورمیانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/alonews/148475" target="_blank">📅 01:22 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148474">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">علی رضا تقوی نیا، روزنامه نگار نزدیک به سپاه:  وضعیت کاملا جنگی به نظر می‌رسد و آماده‌باش صد درصدی به نیروهای مسلح اعلام شده است.</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/148474" target="_blank">📅 01:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148473">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bd5cJDI4EpncXKGjdt75dJuomZ2HECkbI6O34expBwZjJ7WQ-wEPFFRpCpY1PSeBoAeFnXy5ZCQGNa1gGsF3P8yfcyZxVAog_3_WHnpKHub1jASjaQ_GK8zOtrKZieHnTnrNXak4N59CBdeajI-F_57atIckJGRSoyuOdYmiUcNa_7Q04RHqIkJ4CC0y3KU7ndGI4DSL7E04rSat5Xug1fZMapW6D-1W22801VRR02LSL5YR30GHMbgoHKPrYB9MT8D9mPhwX3XkLq0gJNOAnvrLkdTyJ7YLNmg4CG_mWSrKYU-Z3NHCCfs3GmqpHEeac2VRBi6JboKL1e5hQu0_-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
ترامپ:
نیمی از جهان متعلق به ماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/alonews/148473" target="_blank">📅 01:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148472">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
فوری/انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/alonews/148472" target="_blank">📅 01:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148471">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
ترامپ: بزودی همه چیز مشخص خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/alonews/148471" target="_blank">📅 01:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148469">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
خروج از ان‌پی‌تی منتفی شد
🔴
عضو کمیسیون امنیت ملی مجلس میگه طبق نظر مقامات عالی، ایران از پیمان ان‌پی‌تی خارج نمیشه. این حرف رو در حالی زده که بحث خروج از ان‌پی‌تی مدتی‌ست مطرح شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/alonews/148469" target="_blank">📅 00:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148468">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTP5sSCVL5WwpThypMwTdUehBzJDL6zq7Acau4LdVSnIx_vso4oHsrqZ8l4k-3pwN6Zdb8PVJUhSUHajaEmku4pbmIXY-Z3TDy9R3Bo9qvORb_3HbVNou_vbuC0Y6ytMKxZ7m-2U_yjfg2Imhzxtz4zJgec978Wc4mpadvxHLxUdYYIh4U_-MWWFzYRg6e_rRdobdx9PiB1KiNT88KWglg8g5fQDqyE53mWav420Il0IJnx0yrPFMJlNTnLoVlXw0gJ-6oaSSfi-n1v-6-cE2PUdxFKpU86K7xiB6Y9yONTLDHrg2c3YTvBJP52sK8v-WWPrKUcR_qtW7TD_iOsDlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آیت‌الله شبیری زنجانی درگذشت
🔴
وی جزو مراجع تقلید و در ۹۸سالگی فوت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/alonews/148468" target="_blank">📅 00:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148467">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-iCK5wmo73kSRvOWcvX45X9tybqXlqw3YdKOsbMJ4Jnd6xzzCdX9hQKMtGBFIKt5nc-jkzlgql4MJ9Fk9EuyPsCXrcdg_Axh-e6PZH9rhGiVpWqBwFf7wDF-3UPDAboGj_7kZyGVgQR4hXR8QKElOCQF0QN8L4NQK01QUSnY1K-hZ1wUDDb22Dwyh5jKaoTLxANVxUD5NBEcc5xawgIDDP-ALutgvUl7NKuOt4XzynrGGIM6P_9HrDrYdLXwA7yQkpmzF89yWD0Cvx-c56_33MB4RyOmkZBo_J-EHbtkSvPGl4rdQWW2wRyS6-OYQAn4tjmewg38WGmxRdQ6knutg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این وسط تتلو ۳۹ساله شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/alonews/148467" target="_blank">📅 00:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148466">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BP9iRsrM69k0SNrM4ovGyLRslhry9Pd3iLr0cqKTZHfa1gXsq24GB_-TBtVnKdlSn7BwixeC8DqRQdq0TKJU95yX1VyQ00wcoPEX49AXGLPLSRMqVFx8RGEHJ8oYsQuMQ3_FHE4OnQYDW37kBL_l0g4aV1SWQJj5PXyFjo6NOINLv_elK2mxsrjHudzR4T4w649WJ44wloPqJzzqkSVwOGfCFFBGwzIQGij1UzOjCBFUwFCu686v3hkaC_dgRxuf2XIHWbwLikudUXIrw7vcREufVJJeuJC-izfsnqLDZD7WGtTP1MW67aNHdkVDmgLMjKpVCN9LQPrZ3SOe44VY8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی:
طولانی شدن جنگ تقصیر پزشکیانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/alonews/148466" target="_blank">📅 00:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148465">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دیشب محسن نامجو که به تازگی برگشته ایران، شروع کرد وسط خیابون با صدای بلند آواز خوندن که یه هموطن با دو کلمه
«کیر،
خفه‌شو»
دهنشو بست  [@AloTweet]</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/alonews/148465" target="_blank">📅 00:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148464">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
یاشار سلطانی: سپاه، دلال نفت هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/alonews/148464" target="_blank">📅 00:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148463">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
وال استریت ژورنال: آمریکا تحریم‌های گسترده‌ای علیه دیوان بین‌المللی کیفری وضع می‌کند
🔴
وال استریت ژورنال یکشنبه شب گزارش داد، دولت دونالد ترامپ رئیس جمهور آمریکا قصد دارد تحریم‌های گسترده‌ای را علیه دیوان بین‌المللی کیفری وضع کرده و دسترسی آن به نظام مالی بین‌المللی را قطع کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/alonews/148463" target="_blank">📅 23:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148462">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/alonews/148462" target="_blank">📅 23:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148461">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/alonews/148461" target="_blank">📅 23:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148460">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
فوری / گزارش شده است که تجهیزات نظامی و تدارکات لجستیکی ترکیه و پاکستان وارد پایگاه‌های سعودی شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/alonews/148460" target="_blank">📅 23:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148459">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
وزیر انرژی قطر: اظهارات وزیر خزانه‌داری آمریکا درباره اینکه تنگه هرمز ظرف دو سال آینده بی‌اهمیت خواهد شد، «اشتباه» است
🔴
تنگه فقط برای انتقال نفت و گاز اهمیت ندارد بلکه مسیر مهمی برای انواع تجارت محسوب می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/alonews/148459" target="_blank">📅 23:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148458">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
وزارت خارجه فرانسه اعلام کرد: این کشور پس از تعطیلی مرکز زبان در تهران، اقدامات مناسبی را انجام خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/alonews/148458" target="_blank">📅 23:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148457">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAzL9AUhpHnblDiO7JsAE2WnaRA2axFTie3n-7wXnfsgSMLSfaP46a9PKuJ2gd5TtNHYoturESUsr0z_9Z3vepIya_rr_NNZgo5N2YJvlwnlLz5S1jXui0eGDmLq_sx0piwgA0Q9IyGKtnxWg4uGDsQktFysZzrJMsQ6QS6-u-QCrK6p79Eryf4jw0esrVn-G1UCeSSRKhXDgr8znK3hekDQzFpc8e0wfIpNAO7XGADnHsODVnL4VoqaBNGHHlc2UicxU8xnevobBJYRZM3gV5UvnmDTwTlcsqn1csFsJ-piVMhAZN1kAutMTRStOSVxbG9uVrg1DeSzt62b0t7LsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / منابع عربی: آسمان اسرائیل به طور کامل کلیر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/alonews/148457" target="_blank">📅 23:36 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148456">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RiLbyZPyR3d5PeiodLYtKDdnB43JMuP-RufgK2vg3fOEG2g8lSC_0wrkRkCjkCvSyOHl6gTA73UFGmCBUfLDJxBKDHP6Wt3Q5bqCCC4A1d4O2byp1UKsm8rJvYbx-jQmVnQFcIFYHHB08sEcOCth8S5nyoM8pPqdW6hfbklAJninRmq-4IOoAmYobqzyGvmkfFCh3m67OXsi-8rzIq5ivWj-U154BCadEX7LfFu2BpCgoERtLr9J5-U6sAnXcv5xTCHQ2xD2QHTpF_9tYjoBU9rjR_Z0b8Mn7TcCsV4uRE3pGi6EFbXleaaVY8h7HRLYrRrsOJsb0FZbaxAcG6MabQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قلهکی:  تحرکات جدید برای مذاکره از سمتِ آمریکا، بخاطر وضعیتِ بُغرنجِ دولت ترامپ در انتخابات آتی این کشور است؛ «آمریکا اصرار دارد ایران باید تا ۴۵ روز آینده وارد مذاکره شده و همه موارد را توافق کرده و امضا کند»،
🔴
«مباحث هسته‌ای از روز اول مذاکره مورد بحث و بررسی قرار گرفته و روی آن توافق شود»، «تنگه از سوی ایران باز شود» و آمریکا نیز متعهد می‌شود مذاکره تا قبل از برگزاری انتخابات آمریکا به نتیجه برسد!
🔴
دستاوردی هم که آمریکا برای ایران در نظر گرفته، «رفعِ محاصره» و «آغاز نکردنِ جنگ جدید با خسارات زیر ساختیِ بالا»ست که هیچ تضمینی وجود ندارد که بعد از انتخاباتِ آمریکا، مجددا ایران مورد حمله گسترده آمریکا و متحدانش قرار نگیرد!
🔴
باید دید ایران از خطوطِ هسته‌ای _یا به بیان بهتر ۷ شرط برای توافق_ عقب می‌نشیند یا خیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/alonews/148456" target="_blank">📅 23:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148455">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
هم اکنون پرواز جنگنده های ارتش در آسمان تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/alonews/148455" target="_blank">📅 23:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148454">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVG0hXO2nRmY132Ee0msshNHf7GZWe9wZsbVify95-kBBPxtjRxzx0jNb8x_wNuMHx2vTV3xRnQEp1bN46a83GHb94IDqW_xQ0WhBkWR57Zanwse-A9Xo4M23E0qCqHB1hpB1xRL1_iNtFy16NEW3EpG4L8--T8imyIjG_I3jGXWfMAYWvnagsM3FQkca4qJLRfGz2OTk8oo10kxpqoXQatGnMLxVcg8qtJBhGCR2Dm83Gtj09YgwWn0A7ghrtaVxbXkf3L7sR-4JlP62q9ovh80JbscrwPf5FC6LVT-cYuHKmgmZ2DKK6WJhHS6uuxpqwZrL3GIJ9ZoFR-1Hrw1Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفارت مجازی آمریکا در ایران از تمام شهروندان آمریکایی حاضر در خاورمیانه خواست برای احتمال لغو پروازها و بسته‌شدن حریم‌های هوایی آمادگی داشته باشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/alonews/148454" target="_blank">📅 23:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148453">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
خبرنگار دولت: ادعای ترامپ برای دیدار با پزشکیان آرزوی محال است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/alonews/148453" target="_blank">📅 23:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148452">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
خبر لغو پروازهای ایران و عراق از روز سه‌شنبه تکذیب شد
🔴
به گزارش خبرنگار مهر، طی ساعات اخیر اخباری مبنی بر لغو تمام پروازهای هوایی میان فرودگاه‌های عراق و ایران از روز سه‌شنبه در فضای مجازی منتشر شده است.
🔴
در همین راستا، مجید اخوان، سخنگوی سازمان هواپیمایی کشوری، در گفتگو با خبرنگار مهر ضمن تکذیب این خبر اظهار کرد: تاکنون هیچ اعلام رسمی از سوی دولت عراق، وزارت حمل‌ونقل یا مراجع هوانوردی این کشور درباره توقف کامل پروازهای میان ایران و عراق منتشر نشده است.
🔴
وی تاکید کرد: ادعای لغو تمامی پروازهای میان عراق به ایران و بالعکس فاقد تأیید رسمی است و این خبر تکذیب می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/alonews/148452" target="_blank">📅 23:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148451">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
انور قرقاش، مشاور دیپلماتیک رئیس‌جمهور امارات: ارتباط با ایران ادامه خواهد داشت؛ به‌ویژه با مسعود پزشکیان، رئیس‌جمهور ایران
🔴
قرقاش تاکید کرد باز نگه داشتن کانال‌های ارتباطی با ایران می‌تواند به منطقه برای عبور از ماه‌ها درگیری کمک کند.
🔴
او دیدار اخیر ولیعهد ابوظبی با پزشکیان در حاشیه اجلاس بریکس در دهلی‌نو را نشانه اهمیت حضور «صداهای عقلانی» برای بازگرداندن صلح و ثبات دانست.
🔴
این مقام اماراتی در اجلاس رسانه‌ های عربی در دبی گفت: «تا زمانی که خصومت‌ها متوقف نشوند، نمی‌توان آینده را بنا کرد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/alonews/148451" target="_blank">📅 22:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148450">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jvwa9WCEU_BOIa3ohiCkDv30rxdFm2bKj52lLMviKnksIVXR3ZrMj6ijVePabXf7gdkIznVLI77Vbh8mrsR0uQETG_Oi4VDVFIOmXF13OdfYUEWNBS4L4DKfhOlDfv1_ZtxLw86XQADDxuySgeYgRu9_WLGiqxDQil08xL2IEdAX4uH86YliATFUhVX3LDw-u1q8rtwFOldRqxxuc_uyuqnQvTJK6Ssnf0a2qR33gvN7qNeBRB_-TmjhaJJeKmS36H6-9BcOWT3-u_sI5FFVaprupYv4Folr4s8WgK0FCZWm05pYsBCZ_mOKH1cSXZAw5jwiOAT9w0LrwhFxaH0Jhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمدعلی ابطحی: اجلاس سازمان ملل جای مذاکره و احقاق حق مردم مظلوم است
🔴
اجلاس سازمان ملل بزرگترین‌ اتفاق سالانه دیپلماسی جهان است.
🔴
از پارسال تا امسال به مردم ایران ستم شد و ملت ایران سرافراز و سربلند باقی ماند، آنجا فقط جای مذاکره و‌گفتگو و احقاق حق مردم مظلوم ایران است.
🔴
گفتگو و به دست آوردن‌ رفاه برای ملت تحت تحریم وحصار اقتصادی حقی است‌که مردم ایران طلب می کنند و‌ دیپلماسی جای حل آن است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/alonews/148450" target="_blank">📅 22:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148449">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
این وسط وزیر کشاورزی به ازبکستان رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/alonews/148449" target="_blank">📅 22:44 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148448">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOrTGeJH_ol1em4tVMX9Fxj1uU4jGRGdIJT6tz0YjsDcITz_rHqdkCe_acWbR95AQmFNsjWDm8-03VT3HVJNqKGWeoU5stPMIa3pkIhNJ1vKPv9139YykYKz6fEjjid_kI2G4XCEcbeKD6zbVHtqeCXY74sMmLIFmvuwXrtY_pVSbg6Jd6fkeuCYPsqX1aAPNEpxWeHS4RoYOLEcYMQ5pXKTD1Wu4t8ivfCXCa0C0Zb1jVMslrBE96pO6IX4uMWLMwhZlCfEJNmkMdbahN4nSpRQUDaXpHPTOibkU27uEhvoCKvV3GFVb8v-FJmAA7HCw7wCk8iCIrsgedMXiButjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی از دوحه راهی تهران شد تا یحتمل امشب راهی نیویورک بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/alonews/148448" target="_blank">📅 22:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148447">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
آذری جهرمی به پزشکیان:
سفر نیویورک را لغو کن و نرو!
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/148447" target="_blank">📅 22:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148445">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bu2u3a90wF2ZrLUTGT_F99lQOoTAU8WuSFvGxPJ40HdaaUR_oLwyIhLjyK8FSQmDG6F6wT6XoR-lgX_VIdsC1GBRCI4XIlIWjzZtYEt09fvZbiTln-cCdPj6H3NmV_qHoEKe4Cop1SmUSYD4B9IRuyuaLrMea65o4D5_uBfywouT54r9EvswmnOtXgTX8LDJO8fbFbIT_nq-FSeiVc8VlEnuYF5YE7dNgzwDmLtuXWgutg7fGJCxKbdpP2l0uAV10E0giapWL0OHu7sldmI8tm7AWkubO58cNou5p6k15VC9SannGicdHco75vqJ69q3xyK5hySB1o2NKQIYDvkDXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lettlCirh98-qiCx2GGEoWFGWpcn8BPquzAcel2U8Hw7LSTx0N3y-nzn1MQWOE0vzEdS6qSVcZ8SIlLTXs8vx3PUQzt6OF7QemCeHBnPKT7x3DzjsZbJZr3gGmn63HKxV-qyhvEtYZPbDPRmuzhB73k3eMaqSbScC_CwNsbYrDrLldkiITTAt2xN4ArKKiewg6COXZzq7dVYTv2b5lqoIWf1EcpgFBu2ZGL__Xdv4Osvqmp9QeDbl1DxLwbWj5zLQyHOZ1AR858O0zDyOtB8mTMBJ9kqofTw8wDD5LwCBJpBkK1CHBIIU5fiQPKXmqgrTgAJ7dmHm8DD02o20B1cLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای که امروز صبح گرفته شده‌اند، نشان می‌دهند که عربستان سعودی به طور همزمان هفت تانکر بزرگ نفت را در پایانه های رأس تنوره و جوایمه در خلیج فارس (معادل حدود ۱۴ میلیون بشکه نفت خام) در حال بارگیری بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/alonews/148445" target="_blank">📅 22:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148444">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
ولودیمیر زلنسکی رئیس‌جمهور اوکراین:
من تازه با پرزیدنت ترامپ صحبت کردم. این یک گفتگوی مهم بود و توانستیم درباره بسیاری از موضوعات بحث کنیم.
🔴
ما توافق کردیم که در نیویورک دیدار کنیم و این دیدار می‌تواند تغییرات قابل توجهی را به همراه داشته باشد. یک پویایی دیپلماتیک در جریان است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/alonews/148444" target="_blank">📅 22:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148443">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
حوثی‌های یمن (انصارالله) اعلام کردند که جنگنده‌های سعودی در ۲۴ ساعت گذشته، ۲۸ حمله هوایی انجام داده‌اند. این حملات با استفاده از جنگنده‌های F-15 و تایفون از پایگاه‌های هوایی خمیس مشیت و طائف صورت گرفته است
🔴
این حملات مناطق طعز، الجوف و مأرب را هدف قرار داد و در مجموع، تعداد حملات هوایی سعودی‌ها در طول این درگیری به ۷۶۰ مورد رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/alonews/148443" target="_blank">📅 21:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148442">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
فووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/alonews/148442" target="_blank">📅 21:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148441">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
فووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/alonews/148441" target="_blank">📅 21:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148440">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88138fc09e.mp4?token=Sn4Wn2k8XgjcZHP6721eDMNlvepzBPY4Czr47S4-3Ahw6bnXQ0V97xwm_nMDEs-JGahIyFlH1KqrzgWVNHC0vFGt1WVBSix5km73saMhyYAZCqTFOclF2iPURuS3Tus4YlEXV_BirkQt43hGcYUF5Qqn_tlVfwGJG79vEBQwdsLESZQQm8UCf75quppcfbCLmYzTA_xjCsVrMvykFTVLmsR6Lc0_8k9cNjHftrfU4scZsqwyFPnnmvq7pyDzq_rURFWmY9L-Fnw9Zfs8aSjCeQ_JNzKwPJW_xneKA6a7qxQ_t8udPiPvX473owD-wLEbb-KtGtgpHRF1twOIXuSp4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88138fc09e.mp4?token=Sn4Wn2k8XgjcZHP6721eDMNlvepzBPY4Czr47S4-3Ahw6bnXQ0V97xwm_nMDEs-JGahIyFlH1KqrzgWVNHC0vFGt1WVBSix5km73saMhyYAZCqTFOclF2iPURuS3Tus4YlEXV_BirkQt43hGcYUF5Qqn_tlVfwGJG79vEBQwdsLESZQQm8UCf75quppcfbCLmYzTA_xjCsVrMvykFTVLmsR6Lc0_8k9cNjHftrfU4scZsqwyFPnnmvq7pyDzq_rURFWmY9L-Fnw9Zfs8aSjCeQ_JNzKwPJW_xneKA6a7qxQ_t8udPiPvX473owD-wLEbb-KtGtgpHRF1twOIXuSp4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بر باعث و بانیش تا قیام قیامت لعنت
#رقص_میله
#رقص_پرچم
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/alonews/148440" target="_blank">📅 21:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148439">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
سفارت آمریکا در ریاض: به دلیل وضعیت امنیتی جاری در عربستان، از تمامی شهروندان خود می‌خواهیم هوشیاری خود را حفظ کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/148439" target="_blank">📅 21:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148438">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
فوری / عراقچی پس از توقف کوتاهی در قطر برای شرکت در نشست سازمان ملل عازم نیویورک شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/alonews/148438" target="_blank">📅 21:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148437">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0sfTN1-beRFKW5alDNSHeAW_0BnDGAEcwnO8FWOlRAMj84pdJu7Swqu7T_EPWIdo769wIVdYnaWY-kyWsSJ265LgAiQMHXVpo8aOlo_7nTtT2Qh6NDOCT_yuX-KDLXM9ofN-y72euZRxmAIzSnOCOWYZGe-1kr1QtLfLC21AB9r-6JUvlhZcUXuoZXYjWAV9Dl0SAeiuBAoMA66KNVSEBUoPtM5H8SzRuTFT-Xy6XB4jC0vMuJ-sxcqBk5tUIJi3tspQlRlVR4kqBqyFxnMpHSoFvbHZnQQJrE56aZysyB98daZDNibre4YSmH_iAJjpt7xvNjvKI3BnNmyPI-zAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روزنامه واشنگتن‌تایمز: دونالد ترامپ قرار است شخصا در فرودگاه پایگاه مشترک اندروز از شی جین‌پینگ، رئیس‌جمهور چین، استقبال کند.
🔴
طبق اعلام مقامات ارشد دولت آمریکا، هواپیمای شی جین‌پینگ روز چهارشنبه در این پایگاه فرود می‌آید و ترامپ برای خوش‌آمدگویی در آنجا حضور خواهد داشت. این کار غیرمعمول است، چون ترامپ معمولاً از رهبران خارجی در کاخ سفید استقبال می‌کند نه فرودگاه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/alonews/148437" target="_blank">📅 21:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148436">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDxcomRzG7LbCL1URiVY1N_HaK2GKIa8X8zrd9qMGrpvAvgqGXt_9f16YS6SOw6Y8_AGqAhVPz33xmuFxoH8qdRYJyOfPDtTk9ovOyohKeadFyHDW44hJi7PIDPvKyHenjh1t67fooNVevJVMpeF0zmrJCocaxDxg9kaOj9nrptGzxiOEMzWYJ2F1zi9ybVnKp8V6QfTsHybfKmQRmuYyaw1FTJT-Nqoe9y_NWOHTMl2H4c64n4l1Vp0dFOUu5yrO0muw2oQRlyewuZZ-Bm-VrD44rDMVd6woYRJBjbuiBbUBw14QHQyX0TGR1s2n66tiQISB9pva7m53RYyx7O6vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار آزمون با تاچ دیدار کرد
@AloSport</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/alonews/148436" target="_blank">📅 21:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148435">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‼️
افزایش شدید قیمت دلار و طلا تو تاریخ......
پیش بینی عجیب نوستراداموس ایران
😳
👇
https://t.me/+sN8qmnF1jDJlZGRk
https://t.me/+sN8qmnF1jDJlZGRk</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/alonews/148435" target="_blank">📅 21:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148434">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
صابرین نیوز عربی : دولت عراق تصمیم گرفته است که تمامی پروازها به و از ایران و از تمامی فرودگاه‌های عراق را از روز سه‌شنبه آینده لغو و متوقف کند.
🔴
ترددها فقط از طریق مرزهای زمینی بین دو کشور امکان‌پذیر خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/alonews/148434" target="_blank">📅 21:26 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148433">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
امام جمعه قم: شرایط الان جنگیه و هرکی اعتراض کنه خائنه و باید کشته بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/alonews/148433" target="_blank">📅 21:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148432">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXpW5ul47SQwD8wNelC9sJJ7t5GLqS_bq5x_J_WJlYAoEQmkrDFAf0DDCTr4R1J4QmOs47irpsX_1qpL0JQWKvGGYwW6MIdBAE70fXTw7ZGlx6p97bc701IpN7qTSfms_K5Y6_lmrSP0uppbW9OnO0P4OPzQdFsqYKw8beCR_u6y66w1C707X1cnuyWJleNBzKwOi6tnucHfEDPJZnF-GetRARO4STBHkKR2WC3pfyLnE6qKFpmmCVjc38h_3pzZY1_8Qu-R4mPFYV_UhJb0il2R8m7L_UzNni1Kt-yQtIJ3Q6rahhpjMzcxjIYC42Fi5L3m4neQNwBLKHxXJiqQDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد باقر قالیباف، رئیس مجلس:
این وضعیت شبیه به شرودینگر است: امپراتوری در کابینهٔ سوه با ظروفی که در حال افتادن هستند، هژمونی را به تصویرk می‌کشد اما کاملاً عریان شده و سعی دارد ایران را خفه کند بدون اینکه عواقبی برایش پیش آید (که غیرممکن است).
🔴
این پایان‌بندی قابل مدل‌سازی نیست. آن گشوده خواهد شد و دست ایران از قبل روی اهرم است
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/alonews/148432" target="_blank">📅 21:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148431">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
کارشناس صدا و سیما: ترامپ بارها اعتراف کرده که ایران پیروز شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/alonews/148431" target="_blank">📅 21:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148430">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
یمن: نیروهای سعودی از تمام مناطق ساحلی غربی یمن اخراج شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/148430" target="_blank">📅 21:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148429">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUtU04Bla49D948zkOtd_rsQROgGOW3ryl4a5wPv0FcSWkWeOqn7SKbmEQdPOhpysunQ6ByI52Cn94Nu3mgQMXmqyNmTdYwsOJ8VhMPGwdEdE5xGAUCSvmBtGxgfEqwBSUC7-A0i0SCd7Z8gki2QiGCTmeuWcGmshymRbq2GY27MDGjTlvY_6E3QMWkdGd27Pk-G4pjx4bNwh_DdIpXHMcelo82z9zIeBw0GZZ5jVvmUU7bB_Am2aGfjcDz0pWXWHWnk_3sjXM7ekZorUMD00Zb0H1R20MzuVR3eIJ69KIQTaYAZcQivTtlR2Z2BbY35RxurGQpsX0xbQ24EIDkR6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تمرین چین برای حمله به جت‌ها و سامانه‌های پدافندی آمریکا و ژاپن
‏
🔴
وبگاه بردی افریک: چین نمونه‌های هدف گیری جنگنده‌های F-35 و F-16 آمریکا، سامانه‌های پدافند هوایی پاتریوت و هواپیمای هشدار و کنترل هوابرد E-767  ژاپن را در یک میدان تیر ساخته است.
‏
🔴
چین از سال ۲۰۲۱ تاکنون، نمونه‌های تمرینی تجهیزات نظامی آمریکا  و ژاپن را در بیابان‌های سین‌کیانگ برای تمرین تیراندازی واقعی و کالیبراسیون موشک‌ها می‌سازد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/alonews/148429" target="_blank">📅 20:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148428">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ترامپ فردا در جریان بازدید خود از سازمان ملل، با ممدانی شهردار نیویورک ملاقات خواهد کرد‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/alonews/148428" target="_blank">📅 20:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148427">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee7db5a25f.mp4?token=L9yegoO_IuA9DeT7hzUx2tPPCEzMyDcaOqEOWZPY_fXTSn89ZPKmjrhgTW90HXNV1d-oaLDOEf1gfazp3TGfd6Qw2QFOzZPP14U-jIY5J4-O0GPckDFjIl35PNytfMLLt7GTJ8hxFyNAqIXIU0k0YEcKsRicFWBKgVpGMqgf_rnUZ8d--33pwFqkvTCM7oLQ6U1cs9aRtTzWI6kVMdsHSnX5rKayuEcu2Cpi-JCjbfMstfuQ2DonKnW3LIP0b6pUc2tRenCZBj24406g7EkSJluZ_N1gtjV8LX-6jT-3hbIuLpSX1N7fzLM6EEx00GdsYL0cVwWGX4siFC3FplbrEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee7db5a25f.mp4?token=L9yegoO_IuA9DeT7hzUx2tPPCEzMyDcaOqEOWZPY_fXTSn89ZPKmjrhgTW90HXNV1d-oaLDOEf1gfazp3TGfd6Qw2QFOzZPP14U-jIY5J4-O0GPckDFjIl35PNytfMLLt7GTJ8hxFyNAqIXIU0k0YEcKsRicFWBKgVpGMqgf_rnUZ8d--33pwFqkvTCM7oLQ6U1cs9aRtTzWI6kVMdsHSnX5rKayuEcu2Cpi-JCjbfMstfuQ2DonKnW3LIP0b6pUc2tRenCZBj24406g7EkSJluZ_N1gtjV8LX-6jT-3hbIuLpSX1N7fzLM6EEx00GdsYL0cVwWGX4siFC3FplbrEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لیلاز، استاد دانشگاه: روزی که تفاهم‌نامه را دیدم گفتم چرا ترامپ باید چنین امتیازاتی را به ما بدهد؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/alonews/148427" target="_blank">📅 20:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148426">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c28266dd36.mp4?token=mLdvF84LUczFq0sRqjqyd3PeAA-VBZiKsoGAY64PwMIDVi4vGMRFWVWpA9DGA9pWjRg9AGjWyhvLqIZ25dxWM_9jbSX93wEOKHNjsu_Hu5TGpXUZ2nfKImXOicX8TSwbjnqxxwNldRZBMBTANPajRPY0_iytC0mxpaitx7RwDglt56YD79MEkjYJLh4BLPsL9bpxfl-2H_HTEvUlzPqzsZ7hhC4RAEqVf2yxTm-8DcdgF4yFHV1bvZp4BL148FasqoiKkpkGebi-8e2eBW3ibX-JWtYhElsBuE5S2YTy_0bdyOSybi7PmI7X7MEY-tb8pX_HEEdyRYbdqARrN5v-bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c28266dd36.mp4?token=mLdvF84LUczFq0sRqjqyd3PeAA-VBZiKsoGAY64PwMIDVi4vGMRFWVWpA9DGA9pWjRg9AGjWyhvLqIZ25dxWM_9jbSX93wEOKHNjsu_Hu5TGpXUZ2nfKImXOicX8TSwbjnqxxwNldRZBMBTANPajRPY0_iytC0mxpaitx7RwDglt56YD79MEkjYJLh4BLPsL9bpxfl-2H_HTEvUlzPqzsZ7hhC4RAEqVf2yxTm-8DcdgF4yFHV1bvZp4BL148FasqoiKkpkGebi-8e2eBW3ibX-JWtYhElsBuE5S2YTy_0bdyOSybi7PmI7X7MEY-tb8pX_HEEdyRYbdqARrN5v-bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لیلاز، استاد دانشگاه: شکی در اصل مذاکره وجود ندارد اما به هیچ وجه نباید از مواضع‌مان کوتاه بیاییم
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/alonews/148426" target="_blank">📅 20:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148425">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
هفت هواپیمای سوخت‌رسان نیروی هوایی آمریکا در نزدیکی تنگه هرمز در حال پرواز هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/alonews/148425" target="_blank">📅 20:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148424">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O-2z2lfiIAZ248xmTvT0kX9NvBOeR3b53CHtpFNEUApVkB-UADc66afi2RTSwOYIyb6vA0IBN6f8UbrypvjtrQpaFB-yRU79oAScW-hTYAy5KrxoFE6EjRaY03fvMjUikCx8RZvxZM0G8ATPN5pdDD8kRos1xkGJU1wML9EWL5ymCfYAtwfEsxuYKbAJ9YE4TgAD6lDT4nKJ5SF8mYiHZGKKHLH3XpsYnokTh9YMqgAzgG6Aj5LlDy__7ij1ws8cwXIO78H3L_GURUibqj9srkc2iLve2Tc0pjK4YvT6P4tKo8MVUTnBXxPa5OZg2dGbGOhILHvmOkXVligEVAxNOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ دیس به خبرگزاری هایی که اجازه ورودشون‌به وایت هَوُس رو نداده
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/alonews/148424" target="_blank">📅 20:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148423">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
ارتش : انهدام یک فروند پهپاد شناسایی پیشرفته اوربیتر بر فراز تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/148423" target="_blank">📅 20:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148422">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
آمریکا به‌دلیل شرایط امنیتی، تردد کارکنانش در عربستان را محدود کرد، سفر به «طائف» و «ینبع» نیازمند مجوز ویژه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/148422" target="_blank">📅 20:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148420">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNiu7rLeW8GdJzLv8xUoAy8tOACViNkJ28TrxvLtEnJXGYOXr7q5lw7GbREsEw45m_IM1T8jQYz5rTYf730XRTMGQlLFXLIMZTim0UMhmEAUm3GISpw85AEgPOG1Pcy5CtRzDsjE9_HffTD6OhrG27En5i4Hk-KjrGsrsSMBRsJg2dtCMh9D-5bLYttL_YYZktgmkOY94WNzFMsUxoP6vq3A1OK6I3LH0TeJlKsxuYAeR996EY99YvECafU_WrSxb2KESvtX35SCQGICCcoYjQQ7y9tzRzDh1xiHXGZqqZFpadAr7mop5WnQ6bb1vNAIo88uzFhUFqjw-LMp2n8lnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دو حمله هوایی نیروی هوایی اسرائیل، مناطق مرتفع علی الطاهر در جنوب لبنان را هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/148420" target="_blank">📅 20:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148418">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
فوری / راشا تودی: عباس عراقچی، وزیر امور خارجه ایران، وارد دوحه، پایتخت قطر شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/alonews/148418" target="_blank">📅 20:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148417">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⛔️
بیایید ببینید هوش مصنوعیه یا نه
😂
⚠️
مشاهده فیلم</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/148417" target="_blank">📅 20:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148416">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
حمله پهپادی به اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/alonews/148416" target="_blank">📅 20:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148415">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHpeV6vnoo_8kP7_tnZuRRLP6L7jx5pL4U07axR1XlwlcPJBI12qfD7dlImrHIMtrV0yfoG8X11PT8Xr7a10AAqmb2LO8KCRMT58R2FZHuK9sVath7_Bsu9p5xeHV8zmleZCRvBYZnpQHxvybZc1gASbYLZWtpXaO6iQCoXxN-FPa2cOe81UAXMmPKEX_QjnV73xjBvPOigPFxwD1R63Gu5HHFX2oemKocE2W6BsJQpgNzjsz_HnfllNCsqz6bTSjFK7jiGS6riECwmReB8GCcgqVunlhTCFEzkchA2ml8NNiy5Xvdcc6cL-wPJiYRlfvYze2E6YYgvtPuy14XMWlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هفت هواپیمای سوخت‌رسان نیروی هوایی آمریکا در نزدیکی تنگه هرمز در حال پرواز هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/alonews/148415" target="_blank">📅 20:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148414">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ترامپ: مایلم با پزشکیان در حاشیه اجلاس سازمان ملل دیدار کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/alonews/148414" target="_blank">📅 19:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148413">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda312692a.mp4?token=Q1Y1WeR5a5GgI73cxtMvD6V7IYWEd-s7tLvHWRIv9SfyPPDg2lQ7-ZfSFKPop4bi9K-6l1QfHHG8ul2NKKe7CDfgwkvRec2jS2CNiBtPT9_4zZIAidkO4ruE_P4eZ2ca0iw5c9zaI2-ZAU3fl8wa_OHdILWrWFqkwhn3AgsWTYfz1JPQc2YAJ-OiMhqrR87U5mVHNAHIUtfmogwrlHzGAH0HIor3bTzPcXJ174YwiMGXGa3il1X_vPtiyp5njVepY379hYI-opWzHAlj3mBqpldYqFm5vMq_qzwUc5jfkZe4MsAxyS3nDPJpz1xId6d9ZxBscdfhua-j1aTwJNNCYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda312692a.mp4?token=Q1Y1WeR5a5GgI73cxtMvD6V7IYWEd-s7tLvHWRIv9SfyPPDg2lQ7-ZfSFKPop4bi9K-6l1QfHHG8ul2NKKe7CDfgwkvRec2jS2CNiBtPT9_4zZIAidkO4ruE_P4eZ2ca0iw5c9zaI2-ZAU3fl8wa_OHdILWrWFqkwhn3AgsWTYfz1JPQc2YAJ-OiMhqrR87U5mVHNAHIUtfmogwrlHzGAH0HIor3bTzPcXJ174YwiMGXGa3il1X_vPtiyp5njVepY379hYI-opWzHAlj3mBqpldYqFm5vMq_qzwUc5jfkZe4MsAxyS3nDPJpz1xId6d9ZxBscdfhua-j1aTwJNNCYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مسعود قدیریان بعد از قهرمانی در مسابقات جهانی بدنسازی گفت که مدال طلای خودم رو به رشت میبرم تا تقدیم مادر جاویدنام مسعود ذات پرور کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/alonews/148413" target="_blank">📅 19:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148412">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
فرود اضطراری ایرباس در مسیر استانبول-تهران در تبریز
🔴
مدیر روابط عمومی فرودگاه بین‌المللی تبریز:   یک فروند ایرباس A330 «هما» که از استانبول عازم فرودگاه امام  بود، به‌دلیل نقص فنی اعلام وضعیت اضطراری کرد و در فرودگاه تبریز به‌سلامت فرود آمد.
🔴
تمامی مسافران در سلامت کامل هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/alonews/148412" target="_blank">📅 19:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148411">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
اولین ربات تحلیل اقتصادی رایگان
‼️
🔴
اگه نمیدونی کجا سرمایه‌ گذاری کنی یه سر به اینجا بزن
👇
@Sygnl_bot
@Sygnl_bot</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/148411" target="_blank">📅 19:36 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148410">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
محسن رضایی: برای یک جنگ سرنوشت‌ساز کاملا آماده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/148410" target="_blank">📅 19:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148409">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
رسانه قطری : به نظر می‌رسد وزیر امور خارجه ایران عراقچی در حال سفری فوری به قطر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/148409" target="_blank">📅 19:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148408">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
خبرنگار سی‌ان‌ان‌: جلسه ترامپ در کمپ‌ دیوید، جهت بررسی و رایزنی درباره گزینه‌های حمله به یمن بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/148408" target="_blank">📅 19:26 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148407">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eY9jbgftV7dNzvQ2xTWnYKOE41-uDdiVKIBGTt9fthONg1HKWrSUs65KekAvWDCtPRwySuKbKHQah_HTzS1kMy_Zf3NwNShCoq0RLBQYLghPxUOWZncqDBupxqQ7oofme9RUV7R8qCubtFRjhpiO9KVIRWeJsLHJj-4IIpFTitItUcDSmX6bu2Q8_oY113uOLFltStvXmMKlkOCQoclFeDZb11OUxGCM3IusrrfvHoCS_ghMJS-J7viP2-TAL94CcHXAStNUgnR0B32CELmxrwsuJyD4sbrFlGkZ3KRNy1NlwRByBw70iqP8YtCbFYC-KjoSA-bvMHel-y3Rf0ICvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار معاون نخست‌وزیر چین و وزیر خزانه‌داری آمریکا
🔴
اسکات بسنت، وزیر خزانه‌داری آمریکا، با «هه لی‌فنگ»، معاون نخست‌وزیر چین، در نیویورک دیدار کرد
🔴
این نشست در آستانه دیدار دونالد ترامپ و شی‌جین‌پینگ انجام شده است
🔴
بسنت، وزیر خزانه‌داری آمریکا در تشریح این نشست مدعی شده این مذاکرات به زمینه‌سازی برای پیشبرد منافع اقتصادی آمریکا و کسب نتایج ملموس برای مردم این کشور کمک می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/148407" target="_blank">📅 19:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148406">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8497b2ccea.mp4?token=cGepdfdg2a-y4XWDj_ShRlQmCiwI_cxcpmCGvOKp0vGVq0JzgCEpZOQHZJBTmDYfk5GpU55Hm9wTn79wAan2qWwspxShd1_OS1JRUwPlKybCFbChrOczwn_ZKe7qojqkkxVZxLTKO5OGGA8gqYKyXmj-TAonCBcWmxmUYxJbVELqWxjZIjPnyp5OkJ0mbhKvZWcBWxmZi_0u86KsbJ5NyQ4u-aXV9tr0vqqcLcdkLcxdfgJ6R0FIJoFXf8yCMjZxvUoQ1J59IMpEDHn5JUuGagGTwwgyzCgatpAQVxlsJfNju08BOWjWnA-0YyqMoCePZw5KQIDUSXLf5gv9DW0Gaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8497b2ccea.mp4?token=cGepdfdg2a-y4XWDj_ShRlQmCiwI_cxcpmCGvOKp0vGVq0JzgCEpZOQHZJBTmDYfk5GpU55Hm9wTn79wAan2qWwspxShd1_OS1JRUwPlKybCFbChrOczwn_ZKe7qojqkkxVZxLTKO5OGGA8gqYKyXmj-TAonCBcWmxmUYxJbVELqWxjZIjPnyp5OkJ0mbhKvZWcBWxmZi_0u86KsbJ5NyQ4u-aXV9tr0vqqcLcdkLcxdfgJ6R0FIJoFXf8yCMjZxvUoQ1J59IMpEDHn5JUuGagGTwwgyzCgatpAQVxlsJfNju08BOWjWnA-0YyqMoCePZw5KQIDUSXLf5gv9DW0Gaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از لحظه حمله به پالایشگاه مسکو که یک شهروند ایرانی آن را ثبت کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/148406" target="_blank">📅 19:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148404">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srHNP_U6Ayg-15IodhyhiWZPv29J72XBOGZ8ux798btyguoOTqwtzcseLov9obYD4WhBhjW7NIUQdfJAArraTkB8a0pVUBOrorMqd0wvV1i-PRsgyNd7chTbiU9qCpduW2w-VzUabbXj3FOVy9paJoTDhG7Kc0LUero7jFYzan_3WwMqLbmUUmJpghJ3O1izipTBubJZNSJWeYUfMlY9HiEEKBPzrMqLRccyb3NLqBeqk3Ua7obtFQGLchhbEsZK6kiPWCzzP-WQCjxiXwFiCd2uyvzkwBrOBZR-2n1jiIa6r-lcWhJRX9QYIJJPDffkpCqGXbhiChRVCGJUgMAZ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/آسمان اسرائیل کلیر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/148404" target="_blank">📅 19:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148403">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
تا ماه بعد وضعیت طلا چجوریه؟</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/alonews/148403" target="_blank">📅 19:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148402">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه قطر:
ما از مقامات دولت آمریکا تضمین‌هایی شنیده‌ایم که آمریکا می‌خواهد به توافق برسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/148402" target="_blank">📅 18:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148401">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hR36Rx3T-ccYSZZfql-ECedcJrcWVZhRRRWdflOGsSmwFrAZVYL5EMZWN1ks3JO5x986aPMQ5Jt7R8PEfEdnG7gkOiJTilxaN9CCrAOMrhKTWatPUMV_VBmSdg1vzyLX7RZjdWd9FN75uAt6HJPLcNcCUf64rHxC9lbJJBWKFtjGLhEjw3G7ArnzUBb7E8llTu4RLbOtyRAZzUpdUfusXNoKjUzyJkkrVVfMMmolrcH2M7EfNY-C8ua1TdI-nNICh_57wLlInwZS10P5qYzJOdiGfYRHGulL8vT5vZtZs_-aXsQoX5sGoCesqDqkhO3JKRshZVaAaAgtF-yRQgPWGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد که نیروهای آمریکایی، به عنوان بخشی از محاصره اعمال شده بر بنادر ایران، مسیر حرکت 109 کشتی تجاری را تغییر داده‌اند.
🔴
این تعداد شامل 4 کشتی بیشتر است که از آخرین به‌روزرسانی که روز جمعه منتشر شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/alonews/148401" target="_blank">📅 18:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148400">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
ارتش اسرائیل:
نیروهای ما در تمام جبهه‌ها در آماده‌باش کامل، مستقر و آماده هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/148400" target="_blank">📅 18:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148399">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c78f54f4ca.mp4?token=gbOQsA7b-3dRJZzn9yQlPJN8XGoBMvKXrHpBOa03_-4UDuq73Ee7DgNZLx9vHzD8pBP_kef_apLhbFIGYZW1yheKPbiADIrq_leAsv4uyf1wN4fLUde-7zByOMhHy_DUfH3aocmqHZ-NSw_ZtnZw7T1BzL3IRa6eAvb1S_epWXXjJ79ctPfmvyPR6PGwUVLgpZeRJIBVRDg0AenN3sAPiy_h-BbUCsto4vOYZoR8WUKY5TblwMt5JlQs4WhKgNIfOiWAM9IT2nugTPINp1pGzFZp2_YADEuvoQYucfQOne5BdZZdfsfNucU3afRbz06A7sgcW5bE5ZBBfmPcfZ_s9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c78f54f4ca.mp4?token=gbOQsA7b-3dRJZzn9yQlPJN8XGoBMvKXrHpBOa03_-4UDuq73Ee7DgNZLx9vHzD8pBP_kef_apLhbFIGYZW1yheKPbiADIrq_leAsv4uyf1wN4fLUde-7zByOMhHy_DUfH3aocmqHZ-NSw_ZtnZw7T1BzL3IRa6eAvb1S_epWXXjJ79ctPfmvyPR6PGwUVLgpZeRJIBVRDg0AenN3sAPiy_h-BbUCsto4vOYZoR8WUKY5TblwMt5JlQs4WhKgNIfOiWAM9IT2nugTPINp1pGzFZp2_YADEuvoQYucfQOne5BdZZdfsfNucU3afRbz06A7sgcW5bE5ZBBfmPcfZ_s9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله پهپادی به اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/alonews/148399" target="_blank">📅 18:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148398">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
وای‌نت: بیمارستان‌های سراسر اسرائیل به حالت اضطراری تبدیل شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/148398" target="_blank">📅 18:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148397">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_kciZ2hs6bsoVuQNFdoR_y633RHpPFHDkxW6-jxmcg6h-XehuGtIZNEaLzSsnPeFew3TwfNZWPKizDXfcHaMnobJwWmyWRt1dcOVARBMzfUpV01NiTKSYH5zDkMykPtBNMaruz2KycbF2vQGCQH0CqJBVhaxQCPwSLuwfOoWQRe1mMJBntESfQsShZhxdW9PqXFAVNvjC9Anj82bdReZL7syFJ5iCxNM8G4sPegICzF-3IO4ilQAdrXkW-egBH_QfDFc1VRX3CUw8hV_WLv9Vq2YpeOAH8NET3FwlOXhzWBuAOGUzaQQB-EwZRL9-YxoIvU0WNBPJrPW0Q7NyzaoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاهش قیمت صندوقهای طلا پس سخنان ترامپ مبنی بر دیدار با پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/alonews/148397" target="_blank">📅 17:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148396">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
رئیس سازمان سیا، اطلاعات مرکزی آمریکا به صورت ناگهانی وارد خاورمیانه شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/148396" target="_blank">📅 17:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148395">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7129a2730c.mp4?token=JCZH1tA2GwKvvqzy46-xfzpFwczqUHFthzmHqy_SDvmd9yrEOJAICCrifjgjsRTxVuSCz6S8Yaz3wyekzaE2MubNz-CMW_sWontigDGIBXPCXLlULhNwc-uQH-Q5b_sTbbTagcMLQJtIBXNythhU6wrl2X0LNBrXr5fqaFjkTbapnGwFdKK62kfO1l-T5ZpWKx2WxEJ525YQwjlXVi13wTP5Qn8fpm5wNtFgaIgWL8yyvQcro_XMZuvvczhjl53uI-M0xIYWkxAtPDNftI3ki3sZDBaTzjo4dsGmylq-yZYxjwcu6Cyt9Lw1r-aOfJDRGKrk3iGPkCQPTZwLc9bSCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7129a2730c.mp4?token=JCZH1tA2GwKvvqzy46-xfzpFwczqUHFthzmHqy_SDvmd9yrEOJAICCrifjgjsRTxVuSCz6S8Yaz3wyekzaE2MubNz-CMW_sWontigDGIBXPCXLlULhNwc-uQH-Q5b_sTbbTagcMLQJtIBXNythhU6wrl2X0LNBrXr5fqaFjkTbapnGwFdKK62kfO1l-T5ZpWKx2WxEJ525YQwjlXVi13wTP5Qn8fpm5wNtFgaIgWL8yyvQcro_XMZuvvczhjl53uI-M0xIYWkxAtPDNftI3ki3sZDBaTzjo4dsGmylq-yZYxjwcu6Cyt9Lw1r-aOfJDRGKrk3iGPkCQPTZwLc9bSCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز:
برخی از مقامات ایرانی مانند موش‌ها پنهان شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/alonews/148395" target="_blank">📅 17:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148394">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7979df2c0d.mp4?token=LFZI5FbFyMnS1Ekz4mWbDYvBs4-_Bnh5G7xWk7PgIIPeqIgl3vIQ0L3J6c2OBFKP73_D1as562hyqatFdMEWuPIvR4YOc1X0KiZ0X88H0FfnZnuZ2WXv9dY6c4Nig7kk2futYrN8WD6tIl3M3feeX83Q1Dwn_s8MWbbxEFXWueI3Rr8tFGywW_352Tc89KoimAW__nfvX3J9yN8QioBVMEliIPRR83u4QSrKHYVT4aROdfxKyDF29C_ot5GnCHl-rXX3xVwNBvuqAlHtvcuE7sLMMzCvkR_KiXEGL-QAi_QZZjdi5M393oiZO3qKDLD9k2ICSuRP0gLSbRvMC95A3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7979df2c0d.mp4?token=LFZI5FbFyMnS1Ekz4mWbDYvBs4-_Bnh5G7xWk7PgIIPeqIgl3vIQ0L3J6c2OBFKP73_D1as562hyqatFdMEWuPIvR4YOc1X0KiZ0X88H0FfnZnuZ2WXv9dY6c4Nig7kk2futYrN8WD6tIl3M3feeX83Q1Dwn_s8MWbbxEFXWueI3Rr8tFGywW_352Tc89KoimAW__nfvX3J9yN8QioBVMEliIPRR83u4QSrKHYVT4aROdfxKyDF29C_ot5GnCHl-rXX3xVwNBvuqAlHtvcuE7sLMMzCvkR_KiXEGL-QAi_QZZjdi5M393oiZO3qKDLD9k2ICSuRP0gLSbRvMC95A3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز:آمریکا در ارتباط دائمی با حوثی‌هاست، و آن‌ها توافق کرده‌اند که با آمریکا نجنگند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/148394" target="_blank">📅 17:26 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148393">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: برخی از مقامات ایرانی پنهان شده‌اند و یافتن افرادی که قادر به انجام معامله باشند غیرممکن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/148393" target="_blank">📅 17:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148392">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: گزینه‌های فعلی روی میز، محو کردن ایران، رها کردن آن به پوسیدگی اقتصادی یا رسیدن به توافق است.‌‌
🔴
سوال من این است که کی و آیا قرار است تمام ایران را منفجر کنم و آنها بهتر رفتار کنند.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/alonews/148392" target="_blank">📅 17:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148391">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‏
🔴
فوری/ترامپ:  ممکن است به‌زودی اتفاق بزرگی در مورد ایران رخ دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/alonews/148391" target="_blank">📅 17:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148390">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‏
🔴
فوری/ترامپ:
ممکن است به‌زودی اتفاق بزرگی در مورد ایران رخ دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/alonews/148390" target="_blank">📅 17:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148389">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc1502a1e1.mp4?token=oHsxIYa-a2E9iGSaOhddAQOUw-jhaNywkted5lmVuxGdlbIjwiDNUuHAcTUEaMy3CZxuY5k2CDw8UUd54-nR2cHgs0dEvz0Cd1S0M3Rb-J9KWxkvTC8-dYrfLAJXHQCulwNEJ9C4gLvKj-RbicEwcpw5-kBtvXDF3h57AVnOLnNJzCW2pRQCHjxMfT6d6qqnQw9yx8fFOfqw9mm1ReD0V8p_60yFMK7YmYIH90MGcybe8ziJzQ1OvAWas_PM34DQtr8TnktPt10WYqclehnJSX27v3FzisCE-_zUozHCGcltAVgXA4KhI9IwEqFXFTF4uzkXZTh6Y_mFHouzVrB-3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc1502a1e1.mp4?token=oHsxIYa-a2E9iGSaOhddAQOUw-jhaNywkted5lmVuxGdlbIjwiDNUuHAcTUEaMy3CZxuY5k2CDw8UUd54-nR2cHgs0dEvz0Cd1S0M3Rb-J9KWxkvTC8-dYrfLAJXHQCulwNEJ9C4gLvKj-RbicEwcpw5-kBtvXDF3h57AVnOLnNJzCW2pRQCHjxMfT6d6qqnQw9yx8fFOfqw9mm1ReD0V8p_60yFMK7YmYIH90MGcybe8ziJzQ1OvAWas_PM34DQtr8TnktPt10WYqclehnJSX27v3FzisCE-_zUozHCGcltAVgXA4KhI9IwEqFXFTF4uzkXZTh6Y_mFHouzVrB-3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تداوم حملات عربستان به استان‌های یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/alonews/148389" target="_blank">📅 17:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148388">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
پزشکیان: صلحی که دشمن تو را به آن دعوت می‌کند، نباید دفع کرد
🔴
نمی‌توانیم قانونی بنویسیم که ضمانت اجرایی ندارد؛ گاهی به نام دین بر روی مسائلی متمرکز می‌شویم که اصل نیستند
🔴
ایجاد توقع در بین جامعه بدون در نظر گرفتن ردیف بودجه معین و پشتوانه مالی، نادرست است
🔴
از بیان حرف‌هایی که حتی فرع هم نیستند، دور شویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/148388" target="_blank">📅 16:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148387">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
خدمت اجباری سربازی در آلمان مجددا از سر گرفته می‌شود
🔴
وزارت دفاع فدرال آلمان در برلین: نیروهای مسلح فراخواندن مردان ۱۸ ساله برای خدمت سربازی را که علاقه خود به خدمت را ابراز نکرده‌اند، آغاز کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/148387" target="_blank">📅 16:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148386">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t51QJlrCKsXNmUXnG2uW6jMTrPbHEFqhmWfZjVAAqcjfuHCCZ5vcdy4FyVrefVtCl4Zztz6QZWsnzkG6g6HcsTJg-A-L7f-6e1zN-oLdUQVn0aPYceMRMQMAj4FvQb6Ylb0UencDz6P0Kv5nm069Vs6Wb00S56dyQ7w4pktermER0_JAAUbTJokNJ6cBtYslXWb_IXSXVkmjJasgW24p7rNGsf5-feiQyi5pW7yCyNafEc6F8QuuofoXHf5G8RiBmUz3A30bW4Pg3gOwdap7RDmv9y4rHiHHZdhn0E9Svss2ReiXp7ZLgDIFZ94dzSGGx_Pg1VIhNb68zzl4egt7Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تاکنون، بیشتر هواپیماهای تانکر سوخت از قطر تخلیه نشده‌اند و بعید است که ایالات متحده قبل از تخلیه این پایگاه، حمله‌ای را آغاز کند، زیرا تقریباً 20 درصد از هواپیماهای تانکر سوخت ایالات متحده در این پایگاه مستقر هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/148386" target="_blank">📅 16:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148385">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee1d9cbe58.mp4?token=i7JUNN2brRQkO6wGJuf8xdxQQ9btRt8Pu2BTnjEPtSMhDAlKAnNKLhNtOvx2elxATVtpEhuzhxCFMQzQnQ4vwv6YItAffwzcecW_2DtBdGGWcgYDIdv0vkMQaX-in4VwebgyEGC-kbY2M9zcxY-x_cHyZYFnKwcgHqF9NhxA1DIpxOwiby86eJTOmxJ3PkvvMkiW7ebTITaqjpV8n80mjAGO3QLy53tjMO_rX5VkLf2YNsBBlwW2pd2IVrZFzsgnlu2JpCOkvTjOSDzmcEbWs2JxUe0JU7ANaB4R3P3xwT1uDgYjgG_JwaR5a80KGI-zho0zSU4gUHKNucX-n4A7tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee1d9cbe58.mp4?token=i7JUNN2brRQkO6wGJuf8xdxQQ9btRt8Pu2BTnjEPtSMhDAlKAnNKLhNtOvx2elxATVtpEhuzhxCFMQzQnQ4vwv6YItAffwzcecW_2DtBdGGWcgYDIdv0vkMQaX-in4VwebgyEGC-kbY2M9zcxY-x_cHyZYFnKwcgHqF9NhxA1DIpxOwiby86eJTOmxJ3PkvvMkiW7ebTITaqjpV8n80mjAGO3QLy53tjMO_rX5VkLf2YNsBBlwW2pd2IVrZFzsgnlu2JpCOkvTjOSDzmcEbWs2JxUe0JU7ANaB4R3P3xwT1uDgYjgG_JwaR5a80KGI-zho0zSU4gUHKNucX-n4A7tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان به فالوور گفت تعقیب کننده
🔴
پزشکیان: حالا فالوور نگیم صداوسیما گیر نده بهمون
✅
@AloNews</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/148385" target="_blank">📅 16:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148384">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
فارس: یگان‌های واکنش سریع ارتش در مرزها مستقر شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/148384" target="_blank">📅 16:40 · 29 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
