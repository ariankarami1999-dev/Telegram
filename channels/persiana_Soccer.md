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
<img src="https://cdn4.telesco.pe/file/pCk9_c_qhult3DUj9RBj2Xzs3hwBSwngvklLjKDB71KNhdH2qW1AvEXPih4h_k9Zso0vyj75CB6toKmqFcD63cuqcKoC0YAIO0hWTO1K6PuHnIR5oYtjOprRbg6CK1-OLdnD__dARESixlNWr5XFyB-eIzjs-VctMl3E0nohqX57le2pALfM4KAQMtfLzhxWVKrTyVlUoNrjBfj09esFWulovy4MOrFuyUgHJ0xUGhOkQQ8cZAUow_thLzXJAgOMgl8e5naPGBtHXSdidUvfnk5ZsG17xAJKc4kP_JVmTXL-2E8hpPQM-IZj_Shq4D4AMuF9QPSwNeHElGtrBSXmsg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 460K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-01 01:50:47</div>
<hr>

<div class="tg-post" id="msg-30269">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/204e06fbc9.mp4?token=Z7dqT-9j3v7q-7E-m6ROEIjV-bHUEtkjx2d5oMMTNQoq8M2uqerHhalOB2tsOGCi3tZLSlk7XLE7D244K7ffh7H9uDALOQ9zLsfY-RdrTOWrkXsp4_nyrIEXvCpfPOo7omWDMr8-_HxihTDzqm-XiVINmIm0GflZ2EMRScCdKhoT5h-dMPLCtqW3TS4ucAYluio4C1cFIbpeE3h6BUs9K-ly7UMuKjmcEPO5eiQXnpJ3oh205UFTc9zi9-2N4lTLSc-xrN_JP2qz9DqWN9TjkQJTNbCeT66EEzpDn0oF7N6f-GNsR-x5f27IG5kdQPAZm2A8_V7LtOo6u8iM5SAsHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/204e06fbc9.mp4?token=Z7dqT-9j3v7q-7E-m6ROEIjV-bHUEtkjx2d5oMMTNQoq8M2uqerHhalOB2tsOGCi3tZLSlk7XLE7D244K7ffh7H9uDALOQ9zLsfY-RdrTOWrkXsp4_nyrIEXvCpfPOo7omWDMr8-_HxihTDzqm-XiVINmIm0GflZ2EMRScCdKhoT5h-dMPLCtqW3TS4ucAYluio4C1cFIbpeE3h6BUs9K-ly7UMuKjmcEPO5eiQXnpJ3oh205UFTc9zi9-2N4lTLSc-xrN_JP2qz9DqWN9TjkQJTNbCeT66EEzpDn0oF7N6f-GNsR-x5f27IG5kdQPAZm2A8_V7LtOo6u8iM5SAsHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌‌های ابوطالب حسینی در قسمت اول برنامه جدیدش که هر هفته سه شنبه ها قراره پخش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/persiana_Soccer/30269" target="_blank">📅 01:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30267">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-ojI5rTqTEJl1-6O8uT_eDMO_393YAl4-qUgRax277zc12_OUWvGt0YXpnKg2E2uLttoEAu7uEAd_kOgvszTax7fLFYTCUb-0Tqeh8OGIBJjvSvILM0-XLjkpiwsu_kUpn_-8M6UJps6BQOFzu1Wx8VGeC-1Afd9eZI-U_-Y49DLbRMxNNOlSp4UbNt3e4b24EnVGq9ER0ZqUWw-JiuuqFwLZ0DUrr02wyEjwvg8hdNIS_vz537P7wWtqyPBEKaejVz3DJdBPu_mdMg8nT-CnU2ev8qTzMig2tLrAVvEenp2g3sxabOOuThD6f8ujK_bxKz09KRN7XWOPrA3GHXWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها ‌‌‌‌‌‌‌دیدار مهم امروز
؛ بازی تیم‌های امید ایران و کره‌شمالی برای صعود به ‌عنوان صدرنشین در ناگویا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/30267" target="_blank">📅 01:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30266">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e0067ddce.mp4?token=SuIs2X8c0F3M4dym_WOrh6FPclEM4yyYSab_Wq9eYwSh3MoV5iDtm1BwUrQittpPhZpPiWxrkuM67xoPtzGxDxQP7ANa8zEyWhaYesqGp-T0m0CvGw7dw6F4cqQoZ7e8ExpopaE7qaRSF25ozR5oq3gApm-K_Y07g9GxM25axKho2BfPYFT3bWZSf4-mR3KFStKIs3Pbhf-ai57dKnqRAfCP-WlEsdhflGk8rmhLtxuO6Xz14NxsEaev2nCKGpBIjDMmXEZx__fSDGvPGdDvtNCI9ymJj-1KQBBxNYK48XOn2xzAvvzi3ByrIHV39HKbyBns7rKTov8ko6UpFYC3yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e0067ddce.mp4?token=SuIs2X8c0F3M4dym_WOrh6FPclEM4yyYSab_Wq9eYwSh3MoV5iDtm1BwUrQittpPhZpPiWxrkuM67xoPtzGxDxQP7ANa8zEyWhaYesqGp-T0m0CvGw7dw6F4cqQoZ7e8ExpopaE7qaRSF25ozR5oq3gApm-K_Y07g9GxM25axKho2BfPYFT3bWZSf4-mR3KFStKIs3Pbhf-ai57dKnqRAfCP-WlEsdhflGk8rmhLtxuO6Xz14NxsEaev2nCKGpBIjDMmXEZx__fSDGvPGdDvtNCI9ymJj-1KQBBxNYK48XOn2xzAvvzi3ByrIHV39HKbyBns7rKTov8ko6UpFYC3yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
توصیف‌های عباس قانع گزارشگر مسابقات فوتبال از لیونل مسی فوق ستاره آرژانتینی تاریخ مستطیل سبز که تنها یک بازی باقی موندهه که از دنیای مسابقات ملی برای همیشه خدافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/persiana_Soccer/30266" target="_blank">📅 01:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30265">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/blIGIZUYWmubhiYrMYq7z_WEAo5h4UHAXDa0w8VJ9uTxFYuVsXvLSINCme0RG5ruLwM1gmMmjb4rGKSXEqL8rAxnUCxRLKW8xKg3ogxeez54nimdrPPtR1VMsFukqHoikZlU-lDOG3EM_mVJDaepoSpljA5wNXKg5xriX2M2euEILz3w2nHQoiN4e7DKhm9Q2Godo15xjOxDczbbyKGYzO-goaZVo5lzJxAE1YIeIfM_mh7FZFgMNpD-HT9aS4rZPhgPhC9HaOhVoP_zjaKAIroHMq7mRpUJBYzruG3ofnFc7coz-f7Vk0_o7-KFpUg5CzLd4_PzNv4HUXtea8Y3og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
💎
🤩
روزهیجان کازینوبا
🤩
🤩
🤩
بانس
شنبه،دوشنبه،چهارشنبه وجمعه
🔔
ویژه پروایدر Playson
🎮
بیش از هزاران بازی محبوب اسلات
🆕
متدهای پرداختی ریالی و دلاری اتوماتیک
💵
🤩
🤩
🤩
بانس جبران خسارت بازی‌های کازینو
🧬
ورود به دنیای کازینو با هدیه‌ای ویژه
همین حالا ثبت‌ نام کنید و برای واریز اول از بانس خوش‌آمدگویی کازینویی تاسقف
🤩
🤩
🤩
میلیون ریال بهره‌مند شوید
🔝
فرصت‌های جذاب در انتظار شماست
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/30265" target="_blank">📅 01:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30264">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxrTEK5bjsdlOw-kegsmh4KunPpm7C7x1Ov0p1nlQ817ZC6-ygHpWU1bmw3AUSfzSQBqtXBEUnvArSgovxL8jgtR6BuybYsCjO5eYJ9tfNCCouAWTpN0a9V2GNQLlMl_KZNb1VBXh5W-NhtbATxEMFybeSsWMvv3j0SyVrGUmUUm4HG9ymfxEMK6VgxGX_9pJqQaovTYrezF4-EtbUCOxKcvew709UJl1hfefj3pB-UJd9XuhC8NQd_xnVXgZW9R6y9xK-QiWeWWxNjvR6rINlFbJ7fsnwaSXDHrcsvrrgoC3gzEMlyHbAoOvOSopk_QOcIscnLI7a3Eq4_y_zGr5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه عملکرد رافینیا و وینیسیوس جونیور در این فصل رقابت‌ ها؛ جالبه بدونید وینی سالانه 24 میلیون یورو دستمزد میگیره درحالی رافینیا در بارسا سالی 16 میلیون یورو حقوق میگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/30264" target="_blank">📅 00:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30263">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/896a798b5e.mp4?token=PEu1dmKUkQEB7VjcCG2G7GQHG1jY2h9vl2kL3O46dAbz826Zauxl_GzxEU9Gl-smdceh8oDQ6J-Qll0GzcXjUEYJQUFVKnDj2he3vrqHDBVab4pN4GLsMNCsfpMMv2CYLp05JuoJEvMQmTMxF3w0taUZRj5Nt0-EI1BGiVGTnYNjpUEizIKE1yhvr0_MmqsqVmZLTBPwAJmQM6ymzt6EllygjRiiLaL3KDlje-dcMW0K_IQUZBYFXYCQZRJn_-RMGlhm3NMr-PlLSEPzeP8gp_VDODdynYAfmup7_x7M5xL3VNirhn66a73qDannC9-vbSecbpk5aiTtZj54xCRuEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/896a798b5e.mp4?token=PEu1dmKUkQEB7VjcCG2G7GQHG1jY2h9vl2kL3O46dAbz826Zauxl_GzxEU9Gl-smdceh8oDQ6J-Qll0GzcXjUEYJQUFVKnDj2he3vrqHDBVab4pN4GLsMNCsfpMMv2CYLp05JuoJEvMQmTMxF3w0taUZRj5Nt0-EI1BGiVGTnYNjpUEizIKE1yhvr0_MmqsqVmZLTBPwAJmQM6ymzt6EllygjRiiLaL3KDlje-dcMW0K_IQUZBYFXYCQZRJn_-RMGlhm3NMr-PlLSEPzeP8gp_VDODdynYAfmup7_x7M5xL3VNirhn66a73qDannC9-vbSecbpk5aiTtZj54xCRuEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بالاخره‌تابستون‌لعنتی با گرما مزخرفش و قطعی برق پیاپی اش تموم شد و وارد فصل دلنشین پاییز شدیم. باشد که روزگار هم روزی به کام ما بچرخد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/30263" target="_blank">📅 00:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30262">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9fyzlFBoxThjZPJcKq4D1qJQUSfjtlVWn_kuQBRdnsvcjdT66zWUBjpbhJcpH2188BED9dbnf1MzqnN0hI75dR8VP8lW4GM33HB3xJYYnAwAxOAiZzFafs-I6MSxmjSd0J7ToZcOq4hiOfdlCayQMmnTue2i3isErjU13QswUfJak9G6AUds7dZQC9k5BflG19_AEZYb2bejJT6BaJgLWgVTjiGC8R-WNxjtR8rUXOSIqgYSARLaehaUIgJp79LJNWcB2XAOAvCNOkbJZbBOfq_Y5XrKV3NijoBZvwG33sklg0X7OLkJk9NkiUJGgj7ipQLEfP64TjQvRlacRTUWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
شب گذشته تیم زیر 17 سال النصر در لیگ برتر عربستان با نتیجه 2 بر 1 از سد الاهلی گذشت. هر گل النصر رو پسر کریس رونالدو به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/persiana_Soccer/30262" target="_blank">📅 00:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30261">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bP_57tllRopNbf_eXcOf9UvcHmbPW1ZTicNK0rD4MSYAM05mjwQoWP3I0P57HNioWIJdxNHMqLWLMzO8z0Le7z6NiOU4NOADcntpmgdjFeUK6tFI4aOwJG3pe60SRzj4Du7Dm4n9C12R2SBwqdOZTcJ2NAuaPPp25IyF0_DpXsUACOUWmg6qIBX9TCaFtH0DbmtDFR99EBszN8NmCqPJTjmBV1EUXlZ3s0PjrRYIy8KppNGhtNuJ8eW55XEsDOe3lBkJdc5JhzVAw_Tz7HLfLpfVbJAdAberJQ55450vvnjS2tbsFqnGo_LHw8krSJOCvr71PpeAd9WHcRMZKIN5fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام کمیته داوران لالیگا؛ لی کانگ این ستاره کره‌ای اتلتیکو روی این صحنه خطا روی فده والورده کاپیتان تیم رئال‌مادرید بایستی اخراج میشد که داور جرات‌این‌کار رو در ورزشگاه متروپولیتانو نداشت. به احتمال فراوان مسابقه این بازی محروم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/persiana_Soccer/30261" target="_blank">📅 23:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30260">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJIYSPKzNq5pfaZn8oN4kTSULncEx6k0Du-8xRHvR50f-lAZWw_6bjeURdop5N3QxBSpbjuFxvv-Fj8vMEEQKDOTdVotFF-RAuDA_DBGXu8HpjwKCP9o6JEAwPY3SiRnGiRKIP2MKpMZY5VKouQ3fG2yT2YuLGqYFDzOdplKbrgs108u8fgeoQ1QwbFsIJ3S9elHWx3eY-bzRWYFP_ajM_JAsJCFC1r3jPdn80w7TDeoqXRKSqDKh-rLRLnGCVT0bamws4OulIKqvnEUFpIWVaIEbiA72CmKAPti611n-8DKW3T-1FZlHQUE1tt-XkMAGirkXzZUPaULgUYvb97Fxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رقم رضایت‌نامه‌سه‌فوق‌‌ستاره‌ایرانی ماخاچ قلعه، الوحده امارات‌والنصرامارات: مهدی‌قایدی: 2 الی 2.5 میلیون‌دلار،محمدجوادحسین‌نژاد: 1 الی 1.5 میلیون دلار و محمد قربانی؛ 1.2 الی 1.8 میلیون دلار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/persiana_Soccer/30260" target="_blank">📅 23:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30259">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‼️
چالش فوتبال دستی بین تیوی بیفوما ستاره تیم پرسپولیس با زهرا خواجوی گلر بانوان پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/30259" target="_blank">📅 23:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30258">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siKMJrE3UMsUPWgfI-C7a8uorMQojRi1kCtEDbEIFT93z0oWB6Tn1w1LF2wfynJNNcyggo5bCyzis7QRmGH3DH5P5oper8lcm6fROc0OvNQRGT1iTkB4FbBMqGxGDe_xT3gg-zAzdZcSuItFJ5PAETJcU91Tz8aWif5ScBY6c97g_6R7bbE0WfifkgjzfAnLDnuh4mfRjDlT6J9_41S4z-_HvykPrfJKZbd3lve6QGrRE8F82_ztFgW4PCtJGCyWazlFaHIBId_X2YAOV6-Wa3SDpbrxsL1P3uLHKFmeOe8GvtYLf3sQHzEjWuHz5NXbtlFY-qo6s2k0cuBVJ21iGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
🔴
در جذاب ترین دیدار دوستانه امروز؛ تیم منچستریونایتدِ مدل کریک مقابل شاگردان روبن آموریم در آث میلان با نتیجه چهار بر شکست خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/30258" target="_blank">📅 22:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30257">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h53c7m7GgZmBbXWpaQOLlI0H_kDoE-8uW9KqO9APisiJEXl_8-flPxG8HzAVpA9yUjRjRaSOhZ816KMOrOx3TH20kGAptOItIND2W8k7vtlxAAebv5oQa5c6IthxbzacJ9PsBliYBffku3P570rW8XgZDwIopLe3fc1d_y9CyYVliafFWSmeNQXfgzszNsLaniWm5ekR0vifnJZp-xhqoNTfQwmInVluBnksOtJCvlh_Z3Jf6cQENh2lUfIrgmi3PQu6udRnxOpUiq6LYdW_8lfv6aKggADXav3R9Q38V890cUVuzNaFW1CqOsHJf9qRQbnYgtmFDhCtlBO7eDfvtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/30257" target="_blank">📅 22:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30256">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eeacd25b6.mp4?token=MDWYKdSv856HleChpn2PRgYOUACV6Ty4w1jckgPNXOFUa8epqD0b62se90aqNOpuYCNpWEbdSYYLMkgfzjwFP2trD6rjYvpi2IapTtTXc82uMh8M218dnlf3KAnS1b1meTjtuTFZQl0MC00VQScukEC9-c_FwDhZa5AYIA8jVN9Azow6HkVZO9yNsFcYZMLXWKnRGc0MDPmEVnXYYh016F7-X_IB671JsiUng2tB4QlzXRlD-mUJBu3APetv-PaeRyFqfqURb_cpEYRdEx9kvOSWohHAzvLf0e8vPLpkA7MlOiwCSfErRvxmJ-RrngxppxKOgscQgIOLlEluzyPhB7lkrEfL5pKYTkqD1FbVwG-6dQDF_eqc9FDNDowAmyKmoGJwy6BuL5Df_sUCxPhqZo3x85MRigWkhwQD34DGNZhaNlQJhlV2wtWlDrgnW30KVlDfIHBaZQUEgXkvyk4WkP93j95sohOTM-UOJKkjoqokzrZR9taAe8ebuhIdg4XoVuoOBAdipZaFJ4QxLrlXK-c1SzJLguyzYWziwVpdYttH0OmEZBKphyAoi91YLanAwWwTgp9eIiV59E7hH5CD0OGXrR0NU3F02CCKvesRfdDyCR5rrM8Htk6dcGy90IW-up8cApHj_VrVymj6DPuu0CKeARrmmhB1mX-vHe_duUM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eeacd25b6.mp4?token=MDWYKdSv856HleChpn2PRgYOUACV6Ty4w1jckgPNXOFUa8epqD0b62se90aqNOpuYCNpWEbdSYYLMkgfzjwFP2trD6rjYvpi2IapTtTXc82uMh8M218dnlf3KAnS1b1meTjtuTFZQl0MC00VQScukEC9-c_FwDhZa5AYIA8jVN9Azow6HkVZO9yNsFcYZMLXWKnRGc0MDPmEVnXYYh016F7-X_IB671JsiUng2tB4QlzXRlD-mUJBu3APetv-PaeRyFqfqURb_cpEYRdEx9kvOSWohHAzvLf0e8vPLpkA7MlOiwCSfErRvxmJ-RrngxppxKOgscQgIOLlEluzyPhB7lkrEfL5pKYTkqD1FbVwG-6dQDF_eqc9FDNDowAmyKmoGJwy6BuL5Df_sUCxPhqZo3x85MRigWkhwQD34DGNZhaNlQJhlV2wtWlDrgnW30KVlDfIHBaZQUEgXkvyk4WkP93j95sohOTM-UOJKkjoqokzrZR9taAe8ebuhIdg4XoVuoOBAdipZaFJ4QxLrlXK-c1SzJLguyzYWziwVpdYttH0OmEZBKphyAoi91YLanAwWwTgp9eIiV59E7hH5CD0OGXrR0NU3F02CCKvesRfdDyCR5rrM8Htk6dcGy90IW-up8cApHj_VrVymj6DPuu0CKeARrmmhB1mX-vHe_duUM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم
؛ سال 2011 در چنین روزی؛
وین رونی فوق‌ستاره‌انگلیسی تیم‌ منچستریونایتد این سوپر گل دیدنی و به‌ یاد موندنی رو وارد دروازه سیتی کرد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/30256" target="_blank">📅 22:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30255">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fM8iVPTsqZA98Fi79nn-01QokNnzJruzx7da6YgvCOP-QuBBhW68toOmt5wchIjG229cO061zK9x6nZfzWj9u15oypokbzc6fXRZP2uALtNcs4l4jz1KLQaG4CgxePWECM8LzTvFuEvw6pVNPe4VcGihyv16BEYzg9KoRRYg3nJMZqng3-UGIWHBvJOcMDN-WtxQH1oi1V8ojtHYy1xJNLo_0_ZhexA9_pu7mcYP1Hz4QJttRGuIqi2bd5pPVYvQACrn-0TKU08TxHcss259lwwrc8T5j60P0x8qQdSq1k7lNfaxaBj1hjNhgQ0nHbbAZC0Ozcuukv97KJvCkcF2SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
تاریخ‌فراموش‌نخواهد کرد که کریس رونالدو فوق‌ستاره‌پرتغال تیم ملی کشورش رو با این اسکواد و در خاک فرانسه به قهرمانی یورو 2016 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/30255" target="_blank">📅 21:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30254">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHIj1Nkhvp5MnOLtmuILXjECSJTr23bU10YWqBcIRJGFOkAFfKTi2Qyv2QzIPAFA9IS1S_CPTp0slCLTWlVFl5Z7mIMtvGPUzd3Sf3InLXzx9dv9fAEGXdhwD85fpqjvBRJl1DQXCRkw-qyu7TrC75eoOV1uvsmmApoo5PzsHHv-anqTWEBX-gVFA-4PtXh0GyX2IUmJ7ZB3eB76SSXQNltCNuphBMTVKf9W4OU35uE84rdMJCiZMalKU6V5fsRtHQVbSnWv8BhyhLLXCpeugOHV5lCMS96ywg2PlyFJZm1EHgtelnX1cQw1LPvzwiFVWVSuJGa8HLm2_zzivJCR8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
دراقدامی انسان دوستانه؛
لیونل مسی 2.6 میلیون یورو برای‌کمک‌بساخت‌مرکز مراقبت و درمان کودکان مبتلا به سرطان در شهر بارسلونا اهدا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/30254" target="_blank">📅 21:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30253">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mS41kz7ioSBK0291U9p1E8YgukCTOnQeajopz4CPRg1ak5PuPY00fFMkzIiV5-6XWKZQ9sDG3FBivBxMCoAev5tiQ7IkmDl95z9fjl-WoPGKt0ZSPvX4X9Pe5XrnyVwS3enzx6TWo_jAplHbswfw8CI2BXts6nQfXUQyD40LLZRq0cB2o9zUhfq_0GsTM0-PLqP_pPOUnczMI0xii8IwT3b5PFtYSRj0Izkme2aMeMiPh9CuiMe7H1j4lx6RQ2ABfBV0aWvxRjbvdWo0ECFNto9fbL5IwkyJx3ORQWhG_TOJfOAdy2O3ji6q8D2QZ8hJpsaUrVFGzrTn7LijdNMmXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
نمایی‌واضح‌تر از خطای‌شدیدی که باعث شد فده والورده حدود یک‌ماه دور از میادین باشه. تموم کارشناسان گفتن اینجا اتلتیکو مادرید باید دهه نفره میشد اما داورمسابقه بازیکن‌حریف رو اخراج نکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/30253" target="_blank">📅 21:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30252">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjW1Ox9FJRHNC-MCzHIwTcHwKKNl2cEnCK9lrPJHrneko-kY1NJ5MQy3Zl8ptU8O5x2JSvsJU9O5pyHcBjF-PK1XDuM5r1afvT6ptCaY3Gnli5AqNfb3I0W2ReHOt2eXhWEGPbPs2pgguZfnTjpFLVcFEhnRjXfNFMep5z0Kfbi5K2nQeidGKAlD6LYgIIYczdgsT0GV3U9qi_1yEK9orNP9P9BQFB_4HiCWS7KBX187JB_1VccE-MLyAOCZ1-eALUEWXo7xFIya3JLWBG2fM5b_16qD87pIf_s_Dqlf3gCO4mALmVIE0tlI695pp9F889PMp3JFzuzSromjp_83fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ خدمت سربازی فرهان جعفری 28 آذرماه به پایان میرسه و با شروع نقل و انتقالات نیم فصل از ملوان انزلی جدا خواهد شد و راهی یکی از دو باشگاه پرسپولیس یا استقلال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/30252" target="_blank">📅 20:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30251">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e95eba0c95.mp4?token=KVDFMjLEStyEtv4sv8N2djgkr0hBUoVbmyUQuGKie1F4LMrAjioST8iTAPcSNyjTxZK4zDUw-zWQvsQf5EBzFwwSUj4eTYOICDwB2N5Erp_yoFMa1h0AJxCYBXHfyezXPBXKlpjxKxTAjnR38kkvfP-DF411AiVCuGKKe_aYqWHlKgi_G_2nHYdJDOWpqeA2kQl4lfILseztGkWQMsv2n_J9EkueA19QF7xkUv0PM2ghee4kdwp9WCTcMoiBqW5C10WGSi8Zsn631-Np7NkhottbLct6gJBvuKIjBcFflI6E-eE5q_aIoICnfcjq4EmOD3zfTPsvw2HisboyYU80H01-inSsUJxPg1eFsKYFbSGJ8tkWX2OTcpOzXNNBlBLX48yp3X_CJT09wbrDCu9UX4T8jpzMGQc3wuwieEelAvrkwWg6MSDRoo9l3A6fygV4SR8nQjedOBtHwUUxMb24nLCyLSy8UL8A5HbR5aPrTypXrSijvsruINxpdLIjQbNYGU1mI-HoJgGNWajDJd-5HM0EiJegjIOxk3Bcdp66l2OCSHS8Uhe0kcAgfX-51JGbk_RLZDqNiQs8JCN5a6SvEN-DFAS-xAhIkxmul8rzwii-1zZUWRpbP9McuojDV9DOkiG0QglWtxYiwEA2ovp8kG5tgfg5zqrQSVqjdxSVIYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e95eba0c95.mp4?token=KVDFMjLEStyEtv4sv8N2djgkr0hBUoVbmyUQuGKie1F4LMrAjioST8iTAPcSNyjTxZK4zDUw-zWQvsQf5EBzFwwSUj4eTYOICDwB2N5Erp_yoFMa1h0AJxCYBXHfyezXPBXKlpjxKxTAjnR38kkvfP-DF411AiVCuGKKe_aYqWHlKgi_G_2nHYdJDOWpqeA2kQl4lfILseztGkWQMsv2n_J9EkueA19QF7xkUv0PM2ghee4kdwp9WCTcMoiBqW5C10WGSi8Zsn631-Np7NkhottbLct6gJBvuKIjBcFflI6E-eE5q_aIoICnfcjq4EmOD3zfTPsvw2HisboyYU80H01-inSsUJxPg1eFsKYFbSGJ8tkWX2OTcpOzXNNBlBLX48yp3X_CJT09wbrDCu9UX4T8jpzMGQc3wuwieEelAvrkwWg6MSDRoo9l3A6fygV4SR8nQjedOBtHwUUxMb24nLCyLSy8UL8A5HbR5aPrTypXrSijvsruINxpdLIjQbNYGU1mI-HoJgGNWajDJd-5HM0EiJegjIOxk3Bcdp66l2OCSHS8Uhe0kcAgfX-51JGbk_RLZDqNiQs8JCN5a6SvEN-DFAS-xAhIkxmul8rzwii-1zZUWRpbP9McuojDV9DOkiG0QglWtxYiwEA2ovp8kG5tgfg5zqrQSVqjdxSVIYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇦🇷
هایلایتی‌از عملکردخاطره‌انگیز و فوق العاده لیونل مسی درتقابل‌خود با منچستریونایتد و کریس رونالدو در فصل 2007/08 لیگ قهرمانان اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/30251" target="_blank">📅 20:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30250">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bea7e3926.mp4?token=WpQN-GPbfWgguyOl9RRy7l-te_iOlt1LmxTbH8SDmuGj4LbTs__xX80idVHglhjjQgWtiKEIiLxgmJpZ3oMynDkAS4lnDq5pus-HLodwYISoKEiNEDGFxkV7n9IWh-pI0jxhXLXP4R_pzF7H-vU0EjPHazFSr_FjmSCq4OkepJFy0hde7Cdi53i6zu7Rabsvd9FwnbQr95nQXBShxBnYEXVJ8vv0yCKCutE_GMAH2Tgqbrm20NFcasBh3ZZ1b46c0QEPhgzefSEhC1f2XcYn91EfRfNTiwadsA1KVKCrIUuJlolH-QdL3UeSe8IgYY1Hi6kyvT9Zbl5uorRfYX1CwoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bea7e3926.mp4?token=WpQN-GPbfWgguyOl9RRy7l-te_iOlt1LmxTbH8SDmuGj4LbTs__xX80idVHglhjjQgWtiKEIiLxgmJpZ3oMynDkAS4lnDq5pus-HLodwYISoKEiNEDGFxkV7n9IWh-pI0jxhXLXP4R_pzF7H-vU0EjPHazFSr_FjmSCq4OkepJFy0hde7Cdi53i6zu7Rabsvd9FwnbQr95nQXBShxBnYEXVJ8vv0yCKCutE_GMAH2Tgqbrm20NFcasBh3ZZ1b46c0QEPhgzefSEhC1f2XcYn91EfRfNTiwadsA1KVKCrIUuJlolH-QdL3UeSe8IgYY1Hi6kyvT9Zbl5uorRfYX1CwoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌از اولین‌مصاحبه‌کریس‌رونالدو 18 ساله با زبان انگلیسی بعد از پیوستن به منچستر یونایتد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/30250" target="_blank">📅 19:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30249">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ib28Ar0idDyVXn-aLjzj3NNEVDEZbChNnBRYFm8vBiaTFPHW3FDPtJne0XzCZIP3-gCYxJg08v-nMdqmw3w9I_mjS-XJs1k3lw1aEQuFlI_BUqeximq4iRGSMwjXaL0iLmJu6s5SFW5M7544wVCdKkK3opunAREnbhPr2LZTTdVhrgD2IMQ9UtUR1nES2mHFMJA5dyBcR9lPFeZEJ_nXOiKJjYMDhUi0K83mizJjs4fiq1ASGfMh6hMptHlWQ1i1NnCQiQHCAoX4-rblVlDMtQ-pVHNhmLwmPx4sRfOCOReh1mFCvh8QorgrCX7EHMug5HTsmIkr-BApZBT5pVlBVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شیخ دیاباته آقای گل سابق لیگ برتر:
استقلال باشگاهیه که حتی آدم مرده رو به بهترین فوتبالیست تبدیل میکنه. حقیقتا من‌قبل اینکه به باشگاه استقلال بروم هیچ تیمی بدلیل مصدومیتایی که داشتم باهام قرارداد نمیبستند اما اومدم استقلال پیشرفت کردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/30249" target="_blank">📅 19:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30248">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7f2af2337.mp4?token=he82DyMKikySUZz3wtuooAoFYmM67hCOFy-bIYZr_xtmWaqtnQsTCaHM1TqZJX_ejMA-KZ1JIT37NqmeKBtTeM9WZiYk3hxHDcN-nS47g9Uf04Nh2KExz84-rUFmJB2K8l7VmsyEQBMJ498PEjkYunYiV26xOAnEe1fbVxGPVDA2mezhLb3PoCvXoyGWp9j5WEAZGbt12rDa7qvC92BLV6gfPr1iuYQFLgh-Mv8SoRQC_JTlsz6iM75BeDNoUaXgYJduf8zNarYKXWsLyrHg9T4ISfDKMAj8jV6EBXP3l6vKyHkavzmPSJIwzy2Ov2n2-06LRMh4Tk1dMzF1zgnutA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7f2af2337.mp4?token=he82DyMKikySUZz3wtuooAoFYmM67hCOFy-bIYZr_xtmWaqtnQsTCaHM1TqZJX_ejMA-KZ1JIT37NqmeKBtTeM9WZiYk3hxHDcN-nS47g9Uf04Nh2KExz84-rUFmJB2K8l7VmsyEQBMJ498PEjkYunYiV26xOAnEe1fbVxGPVDA2mezhLb3PoCvXoyGWp9j5WEAZGbt12rDa7qvC92BLV6gfPr1iuYQFLgh-Mv8SoRQC_JTlsz6iM75BeDNoUaXgYJduf8zNarYKXWsLyrHg9T4ISfDKMAj8jV6EBXP3l6vKyHkavzmPSJIwzy2Ov2n2-06LRMh4Tk1dMzF1zgnutA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇫🇷
صحبت‌ های جالب و فان ابوطالب حسینی درباره مایکل اولیسه ستاره فرانسوی بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/30248" target="_blank">📅 19:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30247">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDMAMWxspcSyEjz6ckOOw-9XzKfFKu-t2ap0XWHAD2T25FbxX6F6hOM7oqF47dbhNo9jM9qOgWJAgPEzgnvT1GXQo4DVCb8iQf-zVvjwTqqmsKScSKIzH-xUSIpCTrpNxzEpFheiH40TDbjHfZZ51JD-10A0ZuAYLhtmtMnHj3DY0U9aWv43oQQvMvwwyt8fICIEJRIGYwBu8JFh-HXUljhiRz1C3nHDpZ6rqDCCZRxYummI5nK5Uy0grl6Cvq6_s6Xcq6ZqXD4vjz_doEqrUGfe02vaB6RPHQFmNEsD08k6ReSuHidREFHyFhIeDldkjsrA655qJROikIqR3nhh5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه عملکرد رافینیا و وینیسیوس جونیور در این فصل رقابت‌ ها؛ جالبه بدونید وینی سالانه 24 میلیون یورو دستمزد میگیره درحالی رافینیا در بارسا سالی 16 میلیون یورو حقوق میگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/30247" target="_blank">📅 19:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30246">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MA2LIj926JayhKk0G7JmtupN733f6K1drSCiOdv3fwIMQgFlvawwqWUwaPtW96a7nYqsmgJbEC7cLN4HDRPKu-8doRnXjvHJ0i1Zd68oa46Z_P7mgKTu5TZUEbrbgAIHIwtO1hQV1BYdFRCRc07S6lAF7YkU-o7Azyi6K9ajrz4T7PpYeTdvUjStp_nEZMQQxlK_vSGoEZUGvRHQk4RMRvsUeQ83tVthBnJ1O9SIMhkS0hW_QnuXKvYUv5C8SnJgsk7arqu6v6dW0-zNy1hlsszLC85V1nPelBCG-qu5Q4g8O-cO09i0-Lm5hwvzyKhacB_QoQFerl1fl2lnCtvcXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی Yekbet
💎
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🔔
فرصت ویژه اولین واریز دلاری در یک بت
⭐️
یک واریز
🤩
دو جایزه
🎁
⚠️
یک انتخاب هوشمند، دو هدیه ویژه
تجربه متفاوت با اولین شارژ دلار
ی
🤩
🤩
🤩
فری‌بت ورزشی +
🤩
🤩
فری‌اسپین کازینو
👀
با اولین شارژ حساب از طریق ارز دیجیتال، یوتوپیا ووچر یا پرمیوم ووچر، هر دو جایزه رو دریافت کن
🗓
شرایط استفاده
🤩
⭐️
فری‌بت:شرط میکس حداقل ۲ مسابقه با ضریب حداقل ۱.۸۰ برای هر انتخاب
⭐️
فری‌اسپین:قابل استفاده در بازی Yummy از POPOK
﻿
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
g31
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/30246" target="_blank">📅 19:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30244">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fcduz4YIwh0vSVNtbfz4FyfckC5Avqi4sWdzonCXR5Pycu0zhTM6CzSgFZIp2fm_xMe4ZJN3wvedd7GXgzwoO-unGDFlZE4nYsbT3OrMxLHYswo1dj7C3T22iQIEWlBsRtbP-nQTkXSg7Uglke4BLJLlIxLSejzrGWNpHmOgCpDBuG1TCKzKdZSS8nhoK2--HvG4aFr4Zv8KXurD3o47y4OzE-0sjmG0dCV0Xmqd3lzKi38ELyMz4N3_nQb29u6zSOPBvITpLfc8pM128isq8UzNv1rdEX8vT1wlWuyIvm3qjqQlcTxr5azjaMrhePF3C39kjE48-GbuDp-YVbUYwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/peMdUzxsSRgtI35luBy3UR0yzWP_AMCzvHSdmf8IY2XWZpIm16hTKpyT6dtQRjc28h8vJgdxp4aGkQK5kvrEpDha368g9OG-Ypki7oC0pLHTEhAAKWQUJKHW0BrvC2j2ASk4LkL9ZEtPG59v_0yKgxiTwgbwS_4RdZtwD-qyO25hX0KvvHKsXbS9MIbo82blcRXc2OrYXvTylWk5WVsF-QZQVUQH-iIcovNqDZLn3Q1rUQZe97ZisHULQF8dilHdwQT1PAlfXu_Gkkk0FAtmKiCGF4YMdR4PgYTk0nZ0wf0BnjXeJFiVviK3mQWhPipgbJJ42olysXr-J4_ANd_e0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
🔴
برسی عملکرد خیره کننده خط دفاعی استقلال و خط حمله پرسپولیس در این فصل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/30244" target="_blank">📅 18:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30243">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HaPiOKHtAqgyxBKJGaHpeuDQgI25WQXIMsJFP5RK63Pl5ozxe0njWNipN8SjAMkWy2z2VXvbyjUSiYm3FzHfe8DoPE1CL803fCNwhEUb_Im7pbcGNR2bbmYqHarpmrFzoahXQbnRRr-e6cBSIgb_HvH35Si_TL-1mlKAfYTLBJflrgK35gbSLTnKeJzL_3mJnTtBv0XWxSTu8KyVcxGhTz3oKWwuOahkB17BuVD7HM-DtDR7egNkCksp_vFZX7T33LS-sa2l3VU_i0STfWpcuz2gV0KAM56j15Qxo28RgFldYy5M6LEoj5kr0cVq_ztj0yflJwvzBAjyuq-zJDuzlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
نمایی‌واضح‌تر از خطای‌شدیدی که باعث شد فده والورده حدود یک‌ماه دور از میادین باشه. تموم کارشناسان گفتن اینجا اتلتیکو مادرید باید دهه نفره میشد اما داورمسابقه بازیکن‌حریف رو اخراج نکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/30243" target="_blank">📅 18:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30242">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mq8J5Gil3iLMbZfPM3_Gty0q1naQERyECOHVeb8Au-TWNPANgAf1N7BS69f1lKloiwUuYg3287Bsrh_jz7ZikT159dJ2YjMgYj_ax6HnH-b4zRkccGOqLFlLw6OrpqW4fheSMWFZNaqTMP6qMbTH4iOhRKKovEH29JszF6HZOdg4XSRnvH7ynYYOmJB0v_cr-dvvKQyWxQPQcjBimwcNUsAxmq9Oo08SwGYRiaWWQARHD8ZoZEud1CfPlTCuRAO9TEU6zmL4mhHMGNLEK7ZxIj7pTwvWhNWNSl59Bbz5TsulVgyTI-GCM5jwrU7Dbq_pP92G79C49qleVpyHKiuevQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیلیان امباپه ستاره فرانسوی رئال مادرید رسما داره از تمام تکنیک‌های نامزدهای ریاست جمهوری مملکتمون استفاده می‌کنه برای کسب توپ طلا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/30242" target="_blank">📅 17:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30241">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vemRVjDrBO00ZMzPXrul0YY66ge7YHAxRcIjJlOSeA7FkqGnbUGhjxvdMt8ze2pP6N3mIsgaLcEDxbJKvLT6uoMgzUNugEfw-Sk_aDVcuzyqM_HOoanY-M92FCXCCVAPI7bvklL1erXZrmsYxEZPqT614X-lBpUxebRdjQ1NqJQxHH4W9w8Iot9i-CbkNaRzHX9C6NCbtmwMp3jHyLFJs_iFFx4KrP-2RBoeITkNGI-ct75zkS01Lmp0wxgbd0wC8X7i183dlQE7dy6VTPP6gDvPOdtrW78EjU2ySlE9GZsjQsFP9IzzvT4pxLCDpiGRpC_w8tnwbTBgjKy_DRvkEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
واکنش‌جالب‌ومتفاوت کیلیان امباپه، لامین یامال و لیونل مسی درخصوص جایزه توپ طلا 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/30241" target="_blank">📅 17:38 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30240">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xr8NSJ6TxSBxPMiQPxHWTw_rthXTGf3xl8LiVkb8Wmz3PLs2rsoXfKEJsiOECK3yaEbn_X3QmDtXGogq8zGcoHqzj9c3R1VRJbppFT19_ywTcwx30hbFADFZ-owsR5L9vpWqDv-8UIJK5Z8Of5rGhPT-BHL2UxQYO-yQR1oV2wYsRU5cK6jhzmfj7VCyx8UR3MJe5B4yyy_GVlhGNnmJSJdlhgIbI7kqFxuA9s7jf8ivun5lYFtZqekDprQizLXKkUyd0BG56_xPIWhW-66SN9jhU0sA5MqiAYGilR2DiKl5qQ2h80Ubt4iEImYfEme26umpVHSOvAQrAqAIQTNj_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌حضور دریک باشگاه در پنج لیگ معتبر اروپایی: رایان گیگز ستاره سابق منچستر در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/30240" target="_blank">📅 17:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30239">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c947cd77ba.mp4?token=S0s2effkQ5DgSPdDBJ78FPL1JdDDFMoVFG9ZnvgJf3ETBlfrVJ1_Aww_AdQh1ntfY640QnwPXMiCK-P8Un6Ag9duqRL2-HlofrBA6PiMQt101XrUt76Sa7WRawAgm8Ddm0hAreykD9MDzYNE1mJh64x17xrDG-f85v8tLdwSX6BvICZ6snwxZ8HdjiGhV7qFpWRmmT_wY1AuOpn4MEBgijRlazs9m4kDbKogV2uibV6AyOLXGi1aHe8UHgJY8KAbgkaSNSVfXLTZtSvHvgXx5bwFpfHuV093UugfQTYXPJLqDa-b70kS2tmHqT526UYOaCxtbAv0kXBEAgW1081C4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c947cd77ba.mp4?token=S0s2effkQ5DgSPdDBJ78FPL1JdDDFMoVFG9ZnvgJf3ETBlfrVJ1_Aww_AdQh1ntfY640QnwPXMiCK-P8Un6Ag9duqRL2-HlofrBA6PiMQt101XrUt76Sa7WRawAgm8Ddm0hAreykD9MDzYNE1mJh64x17xrDG-f85v8tLdwSX6BvICZ6snwxZ8HdjiGhV7qFpWRmmT_wY1AuOpn4MEBgijRlazs9m4kDbKogV2uibV6AyOLXGi1aHe8UHgJY8KAbgkaSNSVfXLTZtSvHvgXx5bwFpfHuV093UugfQTYXPJLqDa-b70kS2tmHqT526UYOaCxtbAv0kXBEAgW1081C4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
واکنش‌جالب‌ومتفاوت کیلیان امباپه، لامین یامال و لیونل مسی درخصوص جایزه توپ طلا 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/30239" target="_blank">📅 16:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30238">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwUirU6A_vfySeaPgZPU7J5Y4wi4fwkGkCns_8M6BFTsI7-izFqXBqEQZefsMjP6mdkipRaajyHYB9tXn6Q5wfjcN0bJz4bFxl_wh__z7VtHNhtQaBNVGDBqN3GdAweIX8aCHtd0FvGH7yKw7qHceyQ-FzNUXQbN8ORNwziZ2Uu3j_6pw5m8Qpj1S0cZs7IdsIEYpO0KDDLtYvs5kSg-N8A8wmGAb-16XXRiENeqimc17-wrr5MzcMlc-snF5fktPdb-zx0lmtPLebORbJ3hGvlfDE5Cxy8LD9sBgiCzHJg484WYCI8w-2gUJnUgBBZkTdo0FgyIbbNwMdObpQETfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
نشریه‌مارکا: جانشین‌ خوزه‌مورینیو سرمربی فعلی باشگاه رئال‌‌مادرید درآینده یکی‌از دو نفر میکل آرتتا و سسک‌فابرگاس دواسطوره اسپانیا خواهدبود. این فصل خوزه مورینیو برای رئالی ها جام نیاره در پایان فصل قراردادش با کهکشانی‌ها فسخ میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/30238" target="_blank">📅 16:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30237">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfc524ab0f.mp4?token=MbbtthMVFPxmt2y8v617jf5u2-sEuXxIN3nOfuOYlWW-ly481hGnm1Etq8UJmVhPWgE2r_BSeO4_JFXgzglim684dn2CQymgxaeAMILhn8NFRXHG7qLvpDqTVCxqZiHlAJGpAFqHnwnJxTn2JcpMLQ8TiBsyfgF19osczKf4rSPGJ2Gde8fmp7_5TrmRycqyFwdA0doFUoKPUA4ofTmJmm6koRiB_pTK4rdEPf0DxyTPR2VaQac0nz_cYPhCGI32tkJeacVxhGGaWzPP6aC3bChU_D1Oo7ZBmsHlLsLzk_fPJWmrH4Gz4b232gOCZO2-fq9_WLxBYF-hYd0w0TJrWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfc524ab0f.mp4?token=MbbtthMVFPxmt2y8v617jf5u2-sEuXxIN3nOfuOYlWW-ly481hGnm1Etq8UJmVhPWgE2r_BSeO4_JFXgzglim684dn2CQymgxaeAMILhn8NFRXHG7qLvpDqTVCxqZiHlAJGpAFqHnwnJxTn2JcpMLQ8TiBsyfgF19osczKf4rSPGJ2Gde8fmp7_5TrmRycqyFwdA0doFUoKPUA4ofTmJmm6koRiB_pTK4rdEPf0DxyTPR2VaQac0nz_cYPhCGI32tkJeacVxhGGaWzPP6aC3bChU_D1Oo7ZBmsHlLsLzk_fPJWmrH4Gz4b232gOCZO2-fq9_WLxBYF-hYd0w0TJrWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعریف و تجمید عجیب و غریب علی رضا علیزاده از نوید عاشوری بازیکن تیم گل گهر: اگه زن نمیگرفتم میاوردمش پیش خودم باهم زندگی میکردیم. عادل میگه چرا تموم مهمون های ما اینجوریهه.
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/30237" target="_blank">📅 15:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30236">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMM9X5svIBxEro4wDmnVZRHtfgfV5i57fw0nwjBpLsnVuboJ9xZSlAxBieBOzrkiZ6Uwn6Qwf-hpNY1fHgzemk5XMqR0Jc4e_vpLM2ShWlbYl8Arodtg7saJ2hwYVi_5f4If045naP0AAE6o35Tmhg9in45VWxA2C5-svul45jsruVih9uA1FVAMah3OM5ukjM4YOlrElvk-IVEQgPNNKqFuOMsU4pTTPgtWsCAPiJ_PmGZuyG3hYjOAAM-3oUa_eLz95PN5ZnMwRB__2HaXYPPMNqns_DwZFtowaNIMrcovmg7hfpnINsPcEF3HqlaL2X5vtdXEcB-W6pHzQIATrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
درشب‌پیروزی پرگل و چهار بر صفر ترابزون اسپور مقابل گالاتاسرای؛ محمد صلاح ستاره مصری ترابزون با ثبت 3 گل و 1 پاس گل یه تنه سه امتیاز ارزشمند این دیدار رو برای تیمش به ارمغان آورد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/30236" target="_blank">📅 15:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30235">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqPXRnAg_2TfW_JIKdJ1wY5K_VPObrs8_ysBORNVmymMTw_aOu-zWfeO_J3mYXkmeb5boqEYetlVV3FweB5zVt65dsHWNV2ykuyB3rjTFruo1qOsbGhvIKGa7O0A7q2Sla0es7HPih46ptAYCIqDRTwp5CB98qU0Kzm30l-6RwHQwd4xBYVFaN6wFszqu_Icv-N6jj6D0_Um7CGix4_KQnWRItNzGSV5u1wfBmVRkduQB06UJxqEDp92ibIw09rYACOsjQrTvK7oXjxtEIRGHOx79bNvrE69D7dDUSKHFI3HsGlnwrroQMf6nnojl1ouNkuOVq1M2BXCKhzBWT_Y4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعدِ لغو بازی‌ با خیبر در هفته‌‌هفتم؛ شاگردان تارتار درپرسپولیس امروز عصر در دیداری دوستانه با نتیجه چهار بر صفر شهید قندی یزد رو شکست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30235" target="_blank">📅 14:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30234">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab687654a6.mp4?token=cazmaSpgxTN-HK3ZiFo2pA_lK4BYQ17rfSV4g_tkImnbMksIL_DKiX3kC7x8G_8HeHzReEb2uxp5WxexQe8MS_UoQuJ17N845P9l65nd1rsoVlgzeSFypPFRX9eBUAFeXOWvIzz1SveP_shzDKWaMRw2eqUKgIVvNYVx_ZACN7Wssangu6sXv3ut_WFd_cjkTEoeJlbXSU3pNQLd09E0bLarKavkAJU2xPE5a1ApmZyJQ6aURDCYcvICmEnUkuKVpRMzESBNHFOqkwgxCpu8Y9QOBGM12VvnmQVe0mr7NIkjXZTtJ2dxBmzKzyPmS4hc55V_efxHm_coXg5jn6oYcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab687654a6.mp4?token=cazmaSpgxTN-HK3ZiFo2pA_lK4BYQ17rfSV4g_tkImnbMksIL_DKiX3kC7x8G_8HeHzReEb2uxp5WxexQe8MS_UoQuJ17N845P9l65nd1rsoVlgzeSFypPFRX9eBUAFeXOWvIzz1SveP_shzDKWaMRw2eqUKgIVvNYVx_ZACN7Wssangu6sXv3ut_WFd_cjkTEoeJlbXSU3pNQLd09E0bLarKavkAJU2xPE5a1ApmZyJQ6aURDCYcvICmEnUkuKVpRMzESBNHFOqkwgxCpu8Y9QOBGM12VvnmQVe0mr7NIkjXZTtJ2dxBmzKzyPmS4hc55V_efxHm_coXg5jn6oYcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی‌خاطره‌انگیز و تماشایی‌از سوپر سیوهای تماشایی و خیره کننده دروازه‌بان در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30234" target="_blank">📅 14:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30233">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSYZqSyVbbfIr9WMC-OB12R1UV4C1oxUznBZuevUaEbQrnmd5Bv-2hwq1HcJSVSAfe-v4peOk86dTj5Q1vhsYOVeAA1llmUOrW7NKqzqTe3a6w8IPCfZgjn2IbVrIsnDau6p3RWsClUR-b6nNXPWHg2fb0Zu5yMiooAXI1iCdYh9U_LWF_55LsHQ_a5x7nQJfBg3tUs5VntfwRkgPSFIFQRyrSJka_T60Id-FvCjZEVYwe_EGA_1TMv_ovt3BoyuKAc3w2CHGiNuqnYdLHDT6RUFqxlOPLNH4pXDcFSnAyLf2G8AQXkW0aBcYntOmI8Hn51l8dC3vLXiula3tb_QJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
👤
#فکت
؛ آخرین بازیکنی‌که تونست تو یه فصل باپیراهن‌باشگاه‌یوونتوس 20 گل یا بیشتر بزنه کریس رونالدو بود اون این‌کار روتوی‌همه فصل‌هایی که برای یووه بازی کرد انجام داد. از وقتی هم که رفته هییچ بازیکنی دراینمدت نتونسته‌ازمرز 20 گل‌هم رد بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30233" target="_blank">📅 13:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30232">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8babc4d6af.mp4?token=NzA7MxAAPc9gPVnaWNpyOgeobcsSUVOVjcvKM3lmTHAuEEw_PyVkQRP2Wnnq5oTFTy37mRz07FaNllQFSD5DGlAugemE62-JYnSAVlPVqDUiIkXXUgJy8Aqbm0ZTCyNji3j25C4RIDlw49doUMCvy22mo6i3fxbmG2iMUFjewdY6H7FhpStPKUv-08TMYGpU8q18gOsK1jHg2zmUOA1jT6Zo00fGx2ysdSgvru5UvTKVneYThNvgkbk-2l1jaGObbw_Aqt7Mw-jbL1zqSAO60Qk5bdYB4457KMuH5bYFFNWntz6IGk2j2mTF_sQZxIXqiZ6toN_EoOIyTK0Rczkm2oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8babc4d6af.mp4?token=NzA7MxAAPc9gPVnaWNpyOgeobcsSUVOVjcvKM3lmTHAuEEw_PyVkQRP2Wnnq5oTFTy37mRz07FaNllQFSD5DGlAugemE62-JYnSAVlPVqDUiIkXXUgJy8Aqbm0ZTCyNji3j25C4RIDlw49doUMCvy22mo6i3fxbmG2iMUFjewdY6H7FhpStPKUv-08TMYGpU8q18gOsK1jHg2zmUOA1jT6Zo00fGx2ysdSgvru5UvTKVneYThNvgkbk-2l1jaGObbw_Aqt7Mw-jbL1zqSAO60Qk5bdYB4457KMuH5bYFFNWntz6IGk2j2mTF_sQZxIXqiZ6toN_EoOIyTK0Rczkm2oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی‌خاطره‌انگیز و تماشایی‌از سوپر سیوهای تماشایی و خیره کننده دروازه‌بان در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30232" target="_blank">📅 13:38 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30231">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0KFtwtKduU32TLv5mt2EtU_51i_ItWoVHA1CJy7FN6igxNJaF9PuSytZCNfUImgSTsztjYFqSACYsXI077-Ui7N0xHzdhyUte7bgkxxDtbVMWwQJaFoNm1JB0txOiz0u2ilWzWZctxhTUo-rO-gYW6QY_AA3bJUGiyCn2c6vDVbrOZURKRht9TaO2_gHmXleJWmMYtjHp2XVl6AWk83ndEjimPqC9ZtM8xAp5jLu1YjhOY6mMdtlTSqmWwfpnRSTwcXM0-AP9jxIt_zIgs_dql1WVlFumPgDO_vog8-e8nkbo-cxin3yWSevJDDU_YgHITwTSLXs7VUgQ86EabKrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
منصور عظیمی معاون ورزشی باشگاه تراکتور که ارتباط خوبی باستاره‌های‌ایرانی و خارجی داره بعد از اختلاف بامالک‌تراکتور از این باشگاه جداشد. در طول سه سال‌اخیر عظیمی‌مسئول‌مذاکره با بازیکنان بود و مذاکرات حرفه‌ای او باعث شد که تراکتور ستاره های زیادی در طی این چند فصل جذب کنه. هر باشگاهی عظیمی رواستخدام‌کنه از همین حالا نقل و انتقالات نیم فصل اول رقابت‌های لیگ برتر رو برده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30231" target="_blank">📅 12:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30230">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPyAJd6kXgeVAZyDZzQyM3sBRQMpiGoE5rY-aGO03c29SGlUzlTm_X404p1eaLUIhmzZuZ8hcYKmyLk7w_8Q79syQfVtpnzHTY0-1JBFw--Ste2H7j88tnxg4va9IWPqFRARtbbYR2TdYOsm3YSl4Fq2_MgGbXl2h53TeKWUb9TzeYanjDou1Rf2y69oJDHUJ__j4LNgneQDRW_FReHSQBD7oiHhmwP_STadOW2E13FbEuRar1fpCADJXqo1LSIbwc3shieIYXo3j-MxaCtPwe9zzs8rVj76VIlw-h3Ydd3iLAb4BFR1FKiyKcc9ajAdV8UwZHm21hIm37zzT0kUeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سعید الهویی مربی‌تیم‌ملی: با اللهیار صیادمنش در ارتباط بودیم و قصد داشتیم در این فیفادی او رو به تیم ملی دعوت کنیم اما مخالفت‌هایی شد. منظور الهویی احتمالا اون تتوی شیر و خورشید اللهیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30230" target="_blank">📅 12:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30229">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‼️
ویدیوکامل‌قسمت‌اول‌برنامه‌جدید و فان ابوطالب حسینی برای‌حواشی‌فصل جدید رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30229" target="_blank">📅 12:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30228">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال: توپ‌طلافوتبال به بهترین بازیکن دنیا داده میشه نه‌اینکه‌بدن به بازیکنی که فقط 80 گل‌ زده چون که برای‌گلزنی جایزه آقای گلی رو میدن. اینا خیلی‌ متفاوته! بهترین بازیکن جهان کسی هستش که وقتی به عنوان گزارشگر یا تماشاگر بازی رو بخاطرش میبینی لذت‌میبری…</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30228" target="_blank">📅 11:59 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30227">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MIlqWQADpCKCTgrHr2EwvZHz4MIsSYpl-l_su1ShNGD_wwUyT_gD1JfkIY3an0FUTYLv2Tslz9ZSCfeFSpiE16BFiUErUQWRoAmRbijdbyTweKV5g6BJKSveFcJoxO6-_JkpihAI1ygrxSzrQufjCchlFEZrWPHllb3jIqgjYKq7Tk6cGduknpA6Irqn9TkZnidfLfJgh2A618OtLy8YUmBjpA--OROf5Aa8fa3ObZ76wQVUenMmLCbwNJfme8DtNohR-oh-M70SU2xjFmz-mBxAYyHSK7NPlXRamelS8tnrkR37TMj0arh0L2nxMDnrgK6v6l6l15unkrMNo3mwbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
مسی درتعقیب‌رکوردی تاریخی؛ لیونل مسی حالا تعدادگل‌هایش‌از روی‌ضربات ایستگاهی را به ۷۵ گل رسانده و تنها ۳ گل با مارسلینیو کاریوکا، برترین گلزن تاریخ فوتبال از روی ضربه آزاد، فاصله دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/30227" target="_blank">📅 11:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30226">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇫🇷
ویدیویی از اولین تمرین تیم ملی فرانسه بعد از جام جهانی 2026 تحت هدایت زین الدیت زیدان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30226" target="_blank">📅 11:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30225">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46dfa14d7e.mp4?token=Tf6M_WYAaynGSNmwPkugI7EJxPmLH7uJLmIm5d0N2Fmpj6L75cDZYjC4PXzcjoSBqgw5kIURJmXzloR2UyJsGlnmOsz4BmRqasu9gtx-KzeD7WNybjvjgSb0GSRWqscJDwKh-SkmmPZMNV-YvAJ5cW4g3nGA7pbse3_F_0bb3J0jagQ3W8v3vZXy6vZyVKMDxqvQ8jxWEsR9IRxyrNvipBPygm-zL8w6CcW2-ZZby013en0vbyyUiXsLFTMAEFjlKS6XmQntAh4ri0_5jlYIgWJGrhYUYkg0pNzt7Udctxk72tEGdkcsnuRKJ6sO69r8-2QYkRJu6Qob8ECtzl4Muw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46dfa14d7e.mp4?token=Tf6M_WYAaynGSNmwPkugI7EJxPmLH7uJLmIm5d0N2Fmpj6L75cDZYjC4PXzcjoSBqgw5kIURJmXzloR2UyJsGlnmOsz4BmRqasu9gtx-KzeD7WNybjvjgSb0GSRWqscJDwKh-SkmmPZMNV-YvAJ5cW4g3nGA7pbse3_F_0bb3J0jagQ3W8v3vZXy6vZyVKMDxqvQ8jxWEsR9IRxyrNvipBPygm-zL8w6CcW2-ZZby013en0vbyyUiXsLFTMAEFjlKS6XmQntAh4ri0_5jlYIgWJGrhYUYkg0pNzt7Udctxk72tEGdkcsnuRKJ6sO69r8-2QYkRJu6Qob8ECtzl4Muw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پارادوکس‌شبانه‌ابوالفضل‌جلالی‌روی آنتن زنده:
من هیییچ جایی نگفتم که از بچگی استقلالی بودم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30225" target="_blank">📅 11:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30223">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/619db5893c.mp4?token=gM7DwPvwz_zwWhEIXxniElhY49277VlZXKL8Ibo52rbZ_AksybeCd3F7cuGMp_C0xTBOT-LcoNKhIdm8LKTI3OJF8yClWNoydlO6iDWDemsVtyQaqbDiZXeQ8SWGi3KOOr_I_PHh8dLc6NpgbvRapqz-vD5ycxF9kpj1wbp_q0N50d7x4xjHVUcwIQSb9AGOqQzFfgyezeV-V9gCWEp8ASKhLo_wF3WkXpaKuyNLdALyyq-QIs9DXSmv2gcZWvL0VXlVd9QeUDizkZtEtbApJ56JmOUT32hhgRZXzUQc_pjYsAqcCIBpVd_7QXfdJG-_0T7jFJEuJhlq_w4gU9zGrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/619db5893c.mp4?token=gM7DwPvwz_zwWhEIXxniElhY49277VlZXKL8Ibo52rbZ_AksybeCd3F7cuGMp_C0xTBOT-LcoNKhIdm8LKTI3OJF8yClWNoydlO6iDWDemsVtyQaqbDiZXeQ8SWGi3KOOr_I_PHh8dLc6NpgbvRapqz-vD5ycxF9kpj1wbp_q0N50d7x4xjHVUcwIQSb9AGOqQzFfgyezeV-V9gCWEp8ASKhLo_wF3WkXpaKuyNLdALyyq-QIs9DXSmv2gcZWvL0VXlVd9QeUDizkZtEtbApJ56JmOUT32hhgRZXzUQc_pjYsAqcCIBpVd_7QXfdJG-_0T7jFJEuJhlq_w4gU9zGrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقاد ضیا مجری‌سابق‌صداوسیما که بعدِ اتفاقات 1401 از این سازمان اومد بیرون درباره خداداد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30223" target="_blank">📅 10:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30222">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4c1024d94.mp4?token=vgnq1FiGXCvIpVmQA9dp9R9LYQikjFk5nFomwnL2mSG442v0d_reqk6qG9Yxj7GWw84pFpMLMevw33oMkV5PV3u8INXPfbPNaQ8c-XPXYL-MwZRp-xj60xhOu_PXeOgLRsqA_kAt2si8y7vDQFNdlN2R7wXakHsLb1ws9ojXqycQE7slPkgnhzi0hdtI-j-BtCmNqtrsxeHNW_hKThzGO2VpOA96APXqP39TZXimSAe8_3NZPIbrNULXdLDSrKUcjiRyO2OOuU8UilwsFiQ_YGwtHv1sXUVY5Y_KxlceAjmwHICMc6DCVGr7a0KobYcJiw7vle-uWrlM-guc6JxWcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4c1024d94.mp4?token=vgnq1FiGXCvIpVmQA9dp9R9LYQikjFk5nFomwnL2mSG442v0d_reqk6qG9Yxj7GWw84pFpMLMevw33oMkV5PV3u8INXPfbPNaQ8c-XPXYL-MwZRp-xj60xhOu_PXeOgLRsqA_kAt2si8y7vDQFNdlN2R7wXakHsLb1ws9ojXqycQE7slPkgnhzi0hdtI-j-BtCmNqtrsxeHNW_hKThzGO2VpOA96APXqP39TZXimSAe8_3NZPIbrNULXdLDSrKUcjiRyO2OOuU8UilwsFiQ_YGwtHv1sXUVY5Y_KxlceAjmwHICMc6DCVGr7a0KobYcJiw7vle-uWrlM-guc6JxWcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیس‌سنگین‌ابوطالب به خدادادعزیزی در قسمت اول برنامه جدیدش: قلب آدم صاف باشه نه پاهاش، شما قلبت پرانتزیه آقای خداداد عزیزی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30222" target="_blank">📅 10:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30221">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9vX6oj7CZ9cv6hqNViACR4x7X9vU_4x9HJxjcIc9wTwp0anY2zDSbrUGCqO1wPafLQkHucN7M-efvrg4mgA5V-VGAQa_gyziJiE1RtARFx8x_ko8-PV2MLZ45uxxM28yzTOEW_UlnNfbQCssTmTbacr-ejNynuzf3G1XHvyy5nFMjI1b8o7kS21T0eKse7R-HjUDthg3CcS5G9iR89iPlHE7PxK2AHzqZaZm8rL64JwMoYln-I9xR4wMsZBCXXPvrLMSrbvVDXbVRszVGuBG2sJYpg8Qj8FDFCJeccqO2ulB6mmh0MVgmu8Hwo-WfVJ_JZWsAq6KBttFU-Ji9LB9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویری از علیرضا بیرانوند در روزهای آینده در سالن تتو کارها. این‌بشر شده کل بدنش رو تتو میکنه مثل بدن امیر تتلو تا بالاخره معافیت رو بگیره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30221" target="_blank">📅 09:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30220">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0ywFHAwxftJZsYQ88xzEJ9RLRLNHkf7EJKZCqfah8DFzWs_pNDxm2gTrzasvw1sBi8qCH4YpYETFpxPSScHXMuKsume_uSDPMNpKxuDRBKZ1V2gDYCCj4KU7kHoyDjo599XtNIrF6RKG31aw9CFOuFOLzfx_LFZu4Nyl9ZkdH3clml81X_Zkonvyfb3wEXRQ9VqrmHcjMGyxMj53S77x6bug_HWtm1mhaUIseMgzjYk8CdjhIKc8sCJRNXI54BYldU4PknQzmSNDKfkCMjbmIBb1kK25MFCKwdNEQp72UwI6M5kXQwDpfE9HTdZ9EaftNZP6viTphT4W8jK-o2miw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
استوری مدیربرنامه‌های یاسر آسانی در تایید خبر ظهرامروزپرشیانا: همیشه به‌آبی وفادار خواهیم ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/30220" target="_blank">📅 09:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30219">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67b45eb828.mp4?token=vBuN8psvUDecOLm81wPOVBSwdHQccmluaxuSr4M8jOdPodYxjhLfEym4NBWmC2HD-RuRE7gGuntw7965QnKy-44haxh7_-a_K7gj25FxuT-zYJ6xG1po2QpO8m-8YDyMgvnu9KRPSS4wQ38fqZjCHgnJO0OoBvTZ5m8P9kAmWAgk2TzpdwWHHtXiKnH-zr31EY-M9no-8BurAWzKwOLQp2Z34qmp-ZIyN0KOinmvzbGdpV9sUDI_Eequ7xcalo1Ge6KiNTrQFwBk7WXxGgeLnWL-eAe_qnFvqvS9-Q3NKHMVEHasmCEpnYhaR1daSRSbQwI4n7ZDcWfzipPdNEho0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67b45eb828.mp4?token=vBuN8psvUDecOLm81wPOVBSwdHQccmluaxuSr4M8jOdPodYxjhLfEym4NBWmC2HD-RuRE7gGuntw7965QnKy-44haxh7_-a_K7gj25FxuT-zYJ6xG1po2QpO8m-8YDyMgvnu9KRPSS4wQ38fqZjCHgnJO0OoBvTZ5m8P9kAmWAgk2TzpdwWHHtXiKnH-zr31EY-M9no-8BurAWzKwOLQp2Z34qmp-ZIyN0KOinmvzbGdpV9sUDI_Eequ7xcalo1Ge6KiNTrQFwBk7WXxGgeLnWL-eAe_qnFvqvS9-Q3NKHMVEHasmCEpnYhaR1daSRSbQwI4n7ZDcWfzipPdNEho0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش‌بینی‌هوش‌مصنوعی‌از قهرمان فصل گذشته لیگ برتر؛ رقابت بین دو تیم تراکتور
🆚
استقلال!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/30219" target="_blank">📅 01:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30218">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JrTVK0mkTDmU1u3xAlJMtHdwVuSKUZUrR-VO4DQdBgoVOPEK8MKkksq5ANigtiACDo-M2vnKp_hPrJTrMzlrGfkAKC6GwaO5YaHhwm5d4yTAShlk4weNYaUjWyymmdPXcHv54Xy_PyQMnqlW8kByjzSETuSzxiFZadS8IxfB6H-mLX_HhCLN9jjMrSAsNRhTv_WUsNoOoyuz3mAG_hRM-hvJDz8GYMU1MYi6y6-dmMwKZujRnbtsXLYiEfw37sNOMvHQ21E3aezwtt9G1ln2iTdQ3_8I2GeGC6ZdveiI7b2B7nFhPwNomkF14CJIVpQ6npbC33Fad_wH9vAaJjZ9vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صحبت‌های تند و جنجالی اللهیارصیادمنش فوق ستاره ایرانی لخ پوزنان: میدونستم قلعه نویی هیچ اعتقادی به سبک بازی من نداره. تا روزی او سرمربی تیم ملیه هیچوقت برای این تیم بازی نمیکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/30218" target="_blank">📅 01:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30217">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOMfz9roCdVhVmhghuRrj-ffNSy-6SC0GYeIkzcNhPoAXq19RYlkR-CKP901CfAaw4tXLC8Umr--FNW4hCF4KRqdSUdfL9yKqNNVP2deUb5bZnVDdIBNDE_BFYqkn3VzL-oWbSUnId8JwbLjxTq-jLtARWFWknSoXK0bBjvRDem9J2nwgyVEwSbROOZTdi0GJPDyDabihSobRNnJnhoK7ChXqoCgCCHfjHPe0ER9ZLNN1Xha46cRWljmZgPMcud3Z5gBgl5dnSsQ0CGNIretqlE6E3CYx-o8INnlzFx77DoT5yzocZ10Vr5larPKPzf_3ABBBthicfMteudDLqu5lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فرشیداسماعیلی‌بازیکن‌سابق‌ آبی‌ها: رفته بودیم اردوی کیش با چندتا ازبچه‌ها عکس گرفتیم بعد از ۳۰ ثانیه همون عکس بین فن پیجا پخش شد. از اینکه به این سرعت عکس پخش شده بود تعجب کرده بودیم. بعداً فهمیدیم که خودِ سید حسین حسینی ادمین فن پیج خودش بوده و اون عکس…</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30217" target="_blank">📅 01:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30215">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‼️
سعید الهویی مربی‌تیم‌ملی: با اللهیار صیادمنش در ارتباط بودیم و قصد داشتیم در این فیفادی او رو به تیم ملی دعوت کنیم اما مخالفت‌هایی شد. منظور الهویی احتمالا اون تتوی شیر و خورشید اللهیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/30215" target="_blank">📅 00:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30214">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff5c924093.mp4?token=A1-TOO5GWa33sgx0-9By1mkhqybnCaRWMWDyNgZ9fQC-aMRowgHgTAGXANYKniQk4bdkEYXeWsNDC56o0q31P6GPx6UNcTTg7cg-aNbLN00GbiccescMeDt4H5PwpGjlqkRMEoiRIjPF3kn8biYTJ7y-imBoMcUhjxxPo1myJgv3jP1C7HFdjII1BAdIorragLNhZY91hiaXjrKInC6IoAodJA4O4ML81SHmxaQjH6CZ6Su3qF2bhT3GYIQ-hp0aa4paIZqcO-jjjVe0LpDbyrgI-pKg2ENfC91dvkkHOhOr7GTZlznFKukaMAuKeyRe588uaXND_HzJsAh_lLvTEmKNWf5vAWN-R_hn9cmclETt-L4sGS38WhT2Q8AwQsyu8o9jZE1L8BGMsnsvk4HdVHwcNSvW7gcfaVPQFtLO5Cy9ftJQXp0T4K7IrsjK5qZP0dZUL8r-EPLm5VGzoYkw82qWXFyHl-vvuaZbKc3nxm6CZ5rbjC5kcJxiB-LKASjP1Fgo7BBjNPL2WmMkA1Wsh3QxmK8Tro-b5v9bd5i1PBTKIGvyLG3wNQTlEiX1dxzF2jd4nZKzVqqGRp22xhMZMZ1TlqBCLytWdKW_zLUE8ORExYcFHZWBS1Fltk3AkJaCz8LQh5vhiPIIqCjsLIgfoCx_jPG74z3iOEEMhFJBTCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff5c924093.mp4?token=A1-TOO5GWa33sgx0-9By1mkhqybnCaRWMWDyNgZ9fQC-aMRowgHgTAGXANYKniQk4bdkEYXeWsNDC56o0q31P6GPx6UNcTTg7cg-aNbLN00GbiccescMeDt4H5PwpGjlqkRMEoiRIjPF3kn8biYTJ7y-imBoMcUhjxxPo1myJgv3jP1C7HFdjII1BAdIorragLNhZY91hiaXjrKInC6IoAodJA4O4ML81SHmxaQjH6CZ6Su3qF2bhT3GYIQ-hp0aa4paIZqcO-jjjVe0LpDbyrgI-pKg2ENfC91dvkkHOhOr7GTZlznFKukaMAuKeyRe588uaXND_HzJsAh_lLvTEmKNWf5vAWN-R_hn9cmclETt-L4sGS38WhT2Q8AwQsyu8o9jZE1L8BGMsnsvk4HdVHwcNSvW7gcfaVPQFtLO5Cy9ftJQXp0T4K7IrsjK5qZP0dZUL8r-EPLm5VGzoYkw82qWXFyHl-vvuaZbKc3nxm6CZ5rbjC5kcJxiB-LKASjP1Fgo7BBjNPL2WmMkA1Wsh3QxmK8Tro-b5v9bd5i1PBTKIGvyLG3wNQTlEiX1dxzF2jd4nZKzVqqGRp22xhMZMZ1TlqBCLytWdKW_zLUE8ORExYcFHZWBS1Fltk3AkJaCz8LQh5vhiPIIqCjsLIgfoCx_jPG74z3iOEEMhFJBTCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
منفجرشدن عادل از حرف پوریا پورعلی؛ عادل پرسید مهدی زارع تو حموم چرا اونجوری شد پوریا گفت من و مهدی باهم بودیم که اونجوری شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/30214" target="_blank">📅 00:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30213">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U15fXZRnB5QF9whGHDCKFFOs40adJGH6owwYJmO1T8EJKNfVwqbnGnliYZ7DUfQPsVrsZ2FL_7ZRg0UXyJOmZHZx4MHA6Xl7A41JL23EkIlBNsKIVPcW8_yeQn1VOiUPFo9dXaeKbXg6WAL0V6B8n3eEx_eMNus3kuMzGizGXZSSalMIDVi2h24bWYXxT6GypE2nwn56zecA6JaeAxuq4ax31W1qwzfeupfHjQlowYNsM5SKlMjNmQBCTzI84dxNW2lqbhBhVL2Cdz-Zgiwt2GBEVXdQFUUAJkne1rIZgW23_MQ0jZDq01PUDppgvTJ9bbG91VR0lWgg91XSqrWPnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
نمایی‌واضح‌تر از خطای‌شدیدی که باعث شد فده والورده حدود یک‌ماه دور از میادین باشه. تموم کارشناسان گفتن اینجا اتلتیکو مادرید باید دهه نفره میشد اما داورمسابقه بازیکن‌حریف رو اخراج نکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/30213" target="_blank">📅 00:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30212">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n48OWScJmM7jZ4WsEc0QD6OIZVR2EruQp9dZeSzvAXGb9_Li7Ze4SOOHzDbhIOIedCI1_TALgCmuthhTd47BTFMg3vhd9JsMjDo51J-VFHp8kcsIQ4mO-nr2UV1xGEHo7kUE9W0pZp9YgLtOIZ-CwS31aXfP1LLayyt0nkTcx5W9P4TxiyHgbnDSrbp5wTZ0e638MUDAnuNJdzOD8CgCxtBZWjP3G3Bxc-k9dPwY9gco_7CmJV4HILgCf2bMW0TAsDZEvFQHqsalH5Ng1Fw8K3iZHNOQBOXrWrS2FW1vihqCyGlaUM_Tjh2qhf8J2IrhJf9PGC69CPy0fN253cxXGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سعید الهویی مربی‌تیم‌ملی: با اللهیار صیادمنش در ارتباط بودیم و قصد داشتیم در این فیفادی او رو به تیم ملی دعوت کنیم اما مخالفت‌هایی شد. منظور الهویی احتمالا اون تتوی شیر و خورشید اللهیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/30212" target="_blank">📅 23:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30211">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCtzqe29GyAT3AipdsDODSiChaeYhgD5VAgaVTDCJcFWXkrg_chwG2EQKeaw-P2H4L6a_OzTbosC1Lui1BUpgjUoFqRbci9E2FcDv3osKk5IBgSyHgtiU9he9zpS2oz53csgF3hEx1zcakG9jMtUrfl9h2iKJMn1iK8_d8PnG-oRHCrj86IfLkFJ1_22Wq3WxL3TVAv53EbIBOK_icrlbBfpmDOHtM_6BiqwuFZ8jxw3Eh3LAOXO-IdcjFQIwiMVt3izc1ysvjlbWmMDSxil9-VSTzGHmkei9RzWW0xCupEdhgwAw0zoTkCU_i6DGQcf9farYsdmBZDK7CF8R2McRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
طبق‌شنیده‌های رسانه پرشیانا؛ کادر فنی تیم ملی با اللهیار صیادمنش برای حضور در جمع شاگردان امیرقلعه‌نویی برای مسابقات جام ملت‌های آسیا تماس گرفته و این ستاره 24 ساله که عملکرد درخشانی در اروپا داشته احتمالا به تیم ملی دعوت خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/30211" target="_blank">📅 23:23 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30210">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8d4ab1809.mp4?token=o-LkSdsyqa3U-vT2uAdiKrqxbvcMeGbfW5rdaeVx2w_C6Nz1QVw-MIvfwFcJPwwA624wVqYzqZDTPeFjLxUFrTwxUQcPC_gxrm5byc2HGhYJerGqFEMk3NpnhPpFj_SlbNdSmL0hHRuyitbIKC0EKW_7LeDBf9Hry5md_zysb15poTaRSsnVd4IyXZfEefSA0zjrO_E2nog-EPEwgX6ycWwF9wELthZupAq3AYBzhe_4TXZ44cEIgFcQlINYim-rkS84kr5Oe0A2vu9xVY6aC77H0qn5QKZOiELWBzd4YPrvdnJax45GhzKDzIxMgWc7Wep9fOmh3kg8m0kwq-4z1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8d4ab1809.mp4?token=o-LkSdsyqa3U-vT2uAdiKrqxbvcMeGbfW5rdaeVx2w_C6Nz1QVw-MIvfwFcJPwwA624wVqYzqZDTPeFjLxUFrTwxUQcPC_gxrm5byc2HGhYJerGqFEMk3NpnhPpFj_SlbNdSmL0hHRuyitbIKC0EKW_7LeDBf9Hry5md_zysb15poTaRSsnVd4IyXZfEefSA0zjrO_E2nog-EPEwgX6ycWwF9wELthZupAq3AYBzhe_4TXZ44cEIgFcQlINYim-rkS84kr5Oe0A2vu9xVY6aC77H0qn5QKZOiELWBzd4YPrvdnJax45GhzKDzIxMgWc7Wep9fOmh3kg8m0kwq-4z1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دلیل خط خوردن قایدی از اردوی تیم ملی توسط قلعه نویی رو میتونید تو ویدیو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/30210" target="_blank">📅 22:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30209">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d21acb31ef.mp4?token=HCcF75Bo8Zv8RtjGTLB94t9sdohGwfSd1WwyRcygUUg0rYLluyc1Tk4bDcbKv4Dp5OVab7Lpyb0UoWQsFWclKjX8GE14hLY-_PpNNZiLjk7vl3aQ051bvMMZUMeXQ-03QQWBNO5NI7WLwQiN2vhQw4sgv8pE-NsMssV5UVkEEhLSjGo7NlaZN6qyS0gKoZbuioNmenn2lxtWGsCMFY28y41RYBg9b-dB5xvcLpsnkXsy4XlF-QN2_a_QwxCzvsb95_JmVjWon9LO5IOfkYdXTawQQQ7eogYEaNtlqEODEr3zVy8WhZ6vO_ivcZ4sX-5I2MVglpkyR5bkRh5BtXf0KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d21acb31ef.mp4?token=HCcF75Bo8Zv8RtjGTLB94t9sdohGwfSd1WwyRcygUUg0rYLluyc1Tk4bDcbKv4Dp5OVab7Lpyb0UoWQsFWclKjX8GE14hLY-_PpNNZiLjk7vl3aQ051bvMMZUMeXQ-03QQWBNO5NI7WLwQiN2vhQw4sgv8pE-NsMssV5UVkEEhLSjGo7NlaZN6qyS0gKoZbuioNmenn2lxtWGsCMFY28y41RYBg9b-dB5xvcLpsnkXsy4XlF-QN2_a_QwxCzvsb95_JmVjWon9LO5IOfkYdXTawQQQ7eogYEaNtlqEODEr3zVy8WhZ6vO_ivcZ4sX-5I2MVglpkyR5bkRh5BtXf0KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش‌جالب‌عادل‌فردوسی‌پور به برگزاری دیدار دوستانه شاگردان امیر قلعه نویی مقابل ازبکستان: دیگه پدرمون درومد ازبس با این تیم بازی کردیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/30209" target="_blank">📅 22:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30208">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaHlem7RMLEpQ7VddLiRQJniP1B79hB8dv8wIPzg8NmeITdtdPJuBr1lG7FscmqYUw4v3-FeZ-4qtK9RPYSoFtXuOWSiAMB_ryAx5MT3COtA5N8L_TNZuIFUZ9uYQFk8cvsOqloy5WmQZRLoxcbl4bZ79Va-FLOMy9WOzq_eNTPKfZIHjIItf79QfeuI1l3MovfnwydK3ChiwaSg-SkKZ7MPm1nyGEUJ9CGwB3IF0JV9nkyzRlK1Ky278d5dzrTIgJaoUH4-u6TXFCWgHOfXmjMGwZMKmQIQMnZHvWA_M7YL6AscFi3bKB3RolCAapas9vTYJeBQNNjRlBtzuYeQ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سال2022دورتموند هالند رو داد منچسترسیتی سال‌بعد منچسترسیتی‌قهرمان UCL شد. سال 2023 دورتموند جودبلینگهام روداد رئال‌مادرید سال بعدش قهرمان UCL شدند. سال 2026 دورتموند آدیمی رو داد به بارسا، یاران فلیک قهرمان UCL میشن؟
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/30208" target="_blank">📅 21:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30207">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbrnefYkOjtp1Ddi1mXS28pc0H7v85p88f0wwdi2TIWGSGkBsLbta_YSQEo4wzc47p_ZuFnrO2h1DBb9fcHLGApcOKkINbx1RA6qzFW9QG1xFzYNXst2HzChAoJfbKx4GpctUj8XcPJ0QI8oUzd0OjHZh6c0bhNE6HqNAOkkJRpHhDX3j1DcLQkj8GiqwsA5moapr0GgOBfGoj75vVqBUt_YtuioW9kh7IKl00uQD_OqQe4cMrRYow02miGpxXEuF3rwBxPPOExfHCNukilVFdi3B7Ve7CqJYJw7JcMBm2gZzPIt6qE0VLOuyg2oR_hdcX0tMzUcnUSZ7_LNxeCyGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
👤
گلزنی تماشایی لیونل مسی در بازی بامداد امروز اینتر میامی در لیگ MLS؛ این 930 امین گل لئو مسی در کل دوران حرفه‌ایش در فوتبال بود‌.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/30207" target="_blank">📅 21:17 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30205">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N76StXBuXlKNVZAn0hMKIJNBQjLzRhWymUS8_PW04_A7_BOpKqhnWXMYCFNDWTaSU_JPErMZmRoR-7CpqaRd6Jv9yqjS8zsNkDwmtCxuK6fgZSHX-PCMyRVqeqgCCTtkiSPq74UWz5Kkxeqlq9vmui6L1h-HlM20KCPl0eK6PuihBRw_1db7bNZtprtpBNoB9S7yrd8HLLSt_3itIM63ohiZg9nx_axtA88tF_3PC9rhDvxALqXp4g3w_bDGTfBlApQI-B_yH0zPxfy9Q1P4xnvPe7FmOVN7kXiDL5AlzLFt_u8ppVJpgPfyF0le4jHaiMJ2s1lVG0Q6R_hI2j-POA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VsVU_uvVOKKQgv5wFNJlrnFDgvXhZFSiSO-fyUGjEiBFv8AtpSs22ugUD4sbWN3b4YRBwjINUIHGyi_aAZ72Vf2iKGH_Wg5WMTC5llvN5IP-pjV6T5mRp0qXpWuonhUMcGwP9uFUFM98aV_xe6UKencl0tCN2vKGbW8zQE6hUv5ywtByr5ak-vL2Mr1Jv_DB8zRlo9qH2TBslt_FNDl2U0XzUXGuTGNEka7p5tqkjHiIZXSa6oVGpivek3J2CvDMsEYPuerybhoFAZ5e3kuHUAuDM1DZRZo_oQ7pGWioiYl_KdKc33MNWhRlBwPjJbQgrApoWYTODDqWHnmGQYyuAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
پنج بازیکن برتر لالیگا و لیگ جزیره در فصل جدید تا پایان این‌ هفته از نگاه سوفا اسکور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/30205" target="_blank">📅 20:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30204">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oI7YpwtGBhdqM88QUYUlgpU2FU-HkNxH435xzE9jicEriKc4Dem6kYCJffaa575_PF1HYFVInxRvJrs-SGZ4HjqN0fRR9RixKFbw6qOZxaPixhBA4CLkqdxK_bqDG1geEUzD76T37pcaXUkBA0jzGTOnk1mYBHgTmJdNudABekTkg4FFpxsAEcpSCnNyBGBx_7eLrP97bC_Rxj4fQkfHrkcsWz2poOjHNLdunMWtbtoll25LGEQM-alaJS2pjxs6qYs5mP2Ke_Mp6YpvNm8l8fccKlkxs5mw8Eqsn3e7xQQgERmnn71IUfMfhFLSg2fqqgcdLm9WdraAOLcIWR0YlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشود عربستان‌ سعودی و چند کشور خاور میانه‌ در آستانه‌ شروع رقابت‌های جام ملت های آسیا بافشار به فیفا به دنبال تعلیق فوتبال ایران هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/30204" target="_blank">📅 20:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30203">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ada5d0f44.mp4?token=BU7TodNjB-Iuz5hBxtet7rp8Kp5PoGrAbhLa-MIlR5PTNj95QAxKzg6Rwuh8RpTf0g5JcEN_YnP-Q-mEvsG6fLSmP9cTNhxla-Ak38oeqWRXbq0oDJGDz3BwIJDzTE210DTT8BMHO-Q5H_BQo0suC7louRoR6BB_pyGROWl9dIh2lVAfGzUDV3tqOVYxZ4ZWD4kLFstXg_1I6GApW1Ihfnd_-CR5DoO1ZrQIwwi6dbhLhj1KKM0aX2H6VKS-G6fnajLEf0ZSNb5dYDkJsAKDbSjBdFLht0KvLSNmEMCH8siR0SSMnRL_3d-viZTN2Sz7EBnSvKOkExZb0B9WwSA6hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ada5d0f44.mp4?token=BU7TodNjB-Iuz5hBxtet7rp8Kp5PoGrAbhLa-MIlR5PTNj95QAxKzg6Rwuh8RpTf0g5JcEN_YnP-Q-mEvsG6fLSmP9cTNhxla-Ak38oeqWRXbq0oDJGDz3BwIJDzTE210DTT8BMHO-Q5H_BQo0suC7louRoR6BB_pyGROWl9dIh2lVAfGzUDV3tqOVYxZ4ZWD4kLFstXg_1I6GApW1Ihfnd_-CR5DoO1ZrQIwwi6dbhLhj1KKM0aX2H6VKS-G6fnajLEf0ZSNb5dYDkJsAKDbSjBdFLht0KvLSNmEMCH8siR0SSMnRL_3d-viZTN2Sz7EBnSvKOkExZb0B9WwSA6hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
فوق‌ستاره‌ای که بعد از خداحافظی از فوتبال نه تیم ملی کشورش روز خوش دید نه باشگاه‌اش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/30203" target="_blank">📅 20:23 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30202">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3f47656d4.mp4?token=JqkmQdeoh1VFopcF4kmc8coCmnHW1dQu7931d8Ac-GpZoDfN7CSopOwfLzlfTOqh7iKsnOUarriBeBw434KTKI8-yYRV8CBfFrPZedmDajwRYZrO0p2LwawWERRFUJmhQzPhX97o5E--490kl0N-IXxPtenz9dA8fRTJy8J-6zwXpq0QEyY7kJG6hu2bJJcdF6yLgZLkE2sUisw8wgaI3Tt0nrttGUQvqf9ebAK4YCNL0zu_nuTwt3yB9oqn2LE2TcweRKiRDTRoygpaXmYLblyOYzt-R9xdO82g2P5i_ICDpF2sojJcD4DHuKyDRHTOLw52BTq1KWkHthi1pUP5pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3f47656d4.mp4?token=JqkmQdeoh1VFopcF4kmc8coCmnHW1dQu7931d8Ac-GpZoDfN7CSopOwfLzlfTOqh7iKsnOUarriBeBw434KTKI8-yYRV8CBfFrPZedmDajwRYZrO0p2LwawWERRFUJmhQzPhX97o5E--490kl0N-IXxPtenz9dA8fRTJy8J-6zwXpq0QEyY7kJG6hu2bJJcdF6yLgZLkE2sUisw8wgaI3Tt0nrttGUQvqf9ebAK4YCNL0zu_nuTwt3yB9oqn2LE2TcweRKiRDTRoygpaXmYLblyOYzt-R9xdO82g2P5i_ICDpF2sojJcD4DHuKyDRHTOLw52BTq1KWkHthi1pUP5pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
فوق‌ستاره‌ای که بعد از خداحافظی از فوتبال نه تیم ملی کشورش روز خوش دید نه باشگاه‌اش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/30202" target="_blank">📅 19:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30200">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Amg_nFuGMIH1LiCK78bRAJszPU8EGr36MKEfia5YXhd0pmOEh-1uc9LWgfLdku-jE17NIPmCV33iIGAFqbNuZNWQCZ5HHGbnpegCre8g8gNnXFPYoi-Gk7aAQ6-7PoOIGJR9K4iri_SmBhr5Szxz0jtyxcAizAO70FYYuCMzS4PnvBAGJ37cTyBKQm5sP015w0HW-A9oZmVcPukvtjj7T4DiQ6BVABeDLYPdwCJvybokMwKqRYmTkOrFUWFmTcI0-dP9HKAlhkgSCBe4cozALiXZ4VMWfVgKb1WFtijetW6Tegolwg-QFc70f6HA3_xdrkidqJ5TrCa_QQWhLwz6bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BjBVqnjTgjY_D6PT6mtp9CnyhjnOXiYRQTkznGLIO4YC0_-_f0BlenStVTf0fzuNUWY3v4NhrcGL8OzDzg72OpxbH7JgLlbSsoktsej6tlJIeHYofIFfb1reRnI5QEX19pszfTfWjVn3WobenPl8nJhA48NKLBA_JwNVYBA1J7L4tvpGWRp47Cfg2qECDTAml-HeQengacoTuM3gAGkSGRrdyaYhPWgR9rsK_rdCuNp8hB2N0QUqC8kR2RCyQuGdUV24v5cSMDk1WZ4BUg2v3wo6X2bVVVyuiIX66KI7SZMNZ8o3Np_mZOikY3iEMEwr0l9iDCk5bQJ19hA6S_SDsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
👤
تعداد خیلی‌زیادی‌از هواداران منچستریونایتد از مدیریت و کادر فنی شیاطین سرخ خواسته اند که در نیم فصل کریس رونالدو رو به این تیم برگردونند. قرارداد 2.5 ساله با CR7 و خدافظی از دنیای فوتبال باپیراهن‌ منچستر یونایتد رویای هواداران این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30200" target="_blank">📅 19:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30199">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIN7Z6REg-j1AsDpAsbErHKnGyXp1SFo982GTfzUmfFIgiVFPXS5OGm2UUvho1yXRvafSHyuxRRuePYkRgkZtpPe59u-p0pbW5pslPqgG3qCfG8fmFhUFhYv71Jbjdv_bWLzXoo3hDQHlSEX_vahRGdk-vAbcwcNXMnzH4U758FuUNyx0EXLXymLkbQe3goysBdd9EjADnzzy1HPInQ1JYatuzuSKevoTuPmJkYTGGSZf2U64GdAA5qQVBSOf-muAQMQE_IGKDdZ-reDIL-U_z-Mw0t1ZblHeCk9juc9teJWtEu-2ovven1CXcARGoDevlg9i9DgJuUXUAWfATdxfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قهرمانان10سال‌اخیر تمام لیگ معتبر اروپا؛ پاری سن ژرمن و بایرن رکورد قهرمانی در لیگ‌هاشون‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30199" target="_blank">📅 19:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30198">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_QjrZWpi23sAx1W1DE9H4Sm-o1BWrbIKQjcbAwIMLYgn-pTdj-C70JR8vNiUC7Is3-BLb9Dd1ZfxUnWD3hKVDE_KOIx4OSWBM0KFeTDgDShd0I4yZ9u0ht4qbeJL1GhiOQI6WaM_b7ZMsorZ1Pn3guC8xSOk35Pgqmz5kumSbgQBPxIkJI0yoEDxXTZxX2kEpVMAifVJgVvCgP-A_IQO0j6ROIlgg_tFtKGJswm_tYfHBYkZcC3lt8yuoYlSsXVLgxsmdziIGvEJ5QLHPnCPmL8FzH1de0_CMtrgiFPOQcBkK_xxjxtvlVVyO5t-MRByiBo5VK0ByXCc-qE5182ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه عملکرد رافینیا و وینیسیوس جونیور در این فصل رقابت‌ ها؛ جالبه بدونید وینی سالانه 24 میلیون یورو دستمزد میگیره درحالی رافینیا در بارسا سالی 16 میلیون یورو حقوق میگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30198" target="_blank">📅 19:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30196">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21bbbf6ac4.mp4?token=IXkzwEx5ni6QuU29k116kYR2O6h8m3b0el09VoZ0MVOCRFhpK9MF8eXypOIkIQRluq77pU-sK87s-zz22qVTPbuFRbZ_D6DXu-XeUZlD_M6MTIAR1aqJCNzWwJ9jwYsBAFiXAIJoAGXp7jC9V0ao0_Wn23UA1Qs-LVVOiDSMGZ_2jVQRDSFlE3REcQy-cyOGGEAtIH8-0TfHNDs7nZeKFJsp475J2LiW-abrRrMMLUB1uAPLW488-HR4Z5PZmNjAWi0isFn7iVLcNp5xOJsnpufl3UmmdraIpVRMW6rrnIY4tQ-QaC2X6kL2WtepMsE6_teUZ3yMjed5LbGSDq_sNGE1g1Rx9R6PdEbBaWaed2BwSn8KlrVnqOxkwvmYEAaktKEDHZoNuQesXKELxpvxGNUZP37YejidvDgAZmr1mhXAd_YuCsrZ_i4VizRUX7XpnJ1tQgildSl4bIOyWptUWHogAx8OMBD4UcjyBPNZlXIed86Bq9RFKaPoQPWVPHZhFh9pQ_p18B21OmG_rAPoQlyr1V_CK18icIaK5305WqH16lkWpbYS1kH_U6qXoWj5WjbtYLh4bWE64fWKzUCjamt45t3xGoeXKzvW3rq5OQ3Hw3dxI49SE1jDyyG-4SUcCItrD_PuzotLQTRQVIgo6yGH_HaOwdhHa2NVnk_teho" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21bbbf6ac4.mp4?token=IXkzwEx5ni6QuU29k116kYR2O6h8m3b0el09VoZ0MVOCRFhpK9MF8eXypOIkIQRluq77pU-sK87s-zz22qVTPbuFRbZ_D6DXu-XeUZlD_M6MTIAR1aqJCNzWwJ9jwYsBAFiXAIJoAGXp7jC9V0ao0_Wn23UA1Qs-LVVOiDSMGZ_2jVQRDSFlE3REcQy-cyOGGEAtIH8-0TfHNDs7nZeKFJsp475J2LiW-abrRrMMLUB1uAPLW488-HR4Z5PZmNjAWi0isFn7iVLcNp5xOJsnpufl3UmmdraIpVRMW6rrnIY4tQ-QaC2X6kL2WtepMsE6_teUZ3yMjed5LbGSDq_sNGE1g1Rx9R6PdEbBaWaed2BwSn8KlrVnqOxkwvmYEAaktKEDHZoNuQesXKELxpvxGNUZP37YejidvDgAZmr1mhXAd_YuCsrZ_i4VizRUX7XpnJ1tQgildSl4bIOyWptUWHogAx8OMBD4UcjyBPNZlXIed86Bq9RFKaPoQPWVPHZhFh9pQ_p18B21OmG_rAPoQlyr1V_CK18icIaK5305WqH16lkWpbYS1kH_U6qXoWj5WjbtYLh4bWE64fWKzUCjamt45t3xGoeXKzvW3rq5OQ3Hw3dxI49SE1jDyyG-4SUcCItrD_PuzotLQTRQVIgo6yGH_HaOwdhHa2NVnk_teho" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی از انالیز دقیق عملکرد خیره کننده بارسا هانسی فلیک در این فصل از رقابت های لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30196" target="_blank">📅 18:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30194">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QwGfkYUNFhWSDKAryKcA3ArDDecPrNG-pMKei92oj36BP4Q1NM37EXpc_48Kkq6MH3pr1CZiVPxYn5WshW_V_ZhtoyoqJ2iZMlpGnIjlcmOZAqeIc9c3iB1_RFo8ImyomY7Lw7hzk_8m-7ovrht-TNC_s6UANk6c-4STBofYcWWGYVoOgFyrF3T53wXuKmpudvyGhDf66mfVBwIUBawr3zjeYap_7ya1rdtoIHuqJZuP4-mRpm-dTTUvQzUERXd_LcjLfRIXuZ9-T3aHzfnd1B3Ttttg9BxsQkXjOKx1smWvWCkYGJTIQEyAEav1KgPBJppcthz0ZhxY_OCa0AuQNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pqI83ushcQWme15uu88qfEUrd_44eW1bM4CJgU0mCIOjoNmHFWv8gbYTFOGjWFKWbjAbD-_rRUVOBQwkns3hEX-o8sp-EFKT4E4P9VgMwIgfeMSU2Bbasc1LhCIzcEUcLvdqEGDr9jUUomD-aWEVgLvFFIX0mtNAMQGYf3qGOx3g6Uslh44PNYfjscSRb-vO-6TQR1Z-luJEEvZiHSFmfixuAbpxo9X0jXieLAZjo3h_Ub7BJUZRkMd1_h-lb_1KiMXsb8EHzuIhCDXlmqN3-aMPWXgcAM5IHauHFyqwdPMzrMUbjkxGPHdRz5dwj6GED5C9ih2kO_y6a64914dIqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛ میلانِ اموریم در دیداری خانگی با سه گل از سد تیم‌لچه گذشت. میلان با این برد یازده امتیازی‌شد و در رتبه پنجم جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30194" target="_blank">📅 18:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30193">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2-QU8nlZV97NNN-N1ENKucbI2BAguD_e3pe4qlfI1hdo9AQah4E9EP0P8A1PceNX_tvrUirjrUjdegaXmG7icvkNk39sIOuj-Zw4sHbMu29pD-t7NeRP4Dz0OaERpxHiZkb788WZECY0JEAlgqaSxYVTfT7ftwkGqkvirhT15rO71UCkiEklFlZvfcBZNA2eI_XiPKIGTVjWkEVqCnwAyRc6OKEIudHR_OAhpqfC9vlYMG0Q3MEBs-tae8Edg8OKwPYw5hDqcONqZceiCEjvh3PqGGDl73Q-0s_HhyVcdiqcvRZTwORm4KIg8tE9mBQqgOeVlsy-NtQYOvC8FNn5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
برگام‌این‌چه‌درخواست‌هایی بوده که بیرو داده!
‼️
علیرضا بیرانوند درخواست معافیت پزشکی داده و دو درخواست از کمیسون پزشکی داشته که اولیش این‌بوده‌گفته‌چون تتو زدم مشکل اعصاب و روان دارم دوم اینکه گفته در سال‌های گذشته رباط دستم بار ها پاره شد و با این دو دلیل…</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30193" target="_blank">📅 17:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30192">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4kdYsWcdpPo0jI-F_QBzjgKWed3Hef_afqFKQ3LtjXVNTstVyUJtZ43qT7bdiiiuT0ZTM98uXc3iTs9V7PX9WNxDfMxaV0eCIruZBBoWIiz-q2ksfnNJopXn_d9ES8m-77erkk5s0I-WCKH82hRnVPBvzqpeQfshw12ie7Nw4KXAhLYnd_JXbc1AsJ_CuB3sSUIxQJQyNp7qS15uf6j0Qi2DStABNcSuIlzQ4C3bMthYAPhOz21n4oJ3oCnqr9izLxxWCa9G9bfZSYA8ZTYj1Z-AFgkxrTG76BUmYiyh-qOK4ifzMGwLoAUhEA1yrryTyANuapt9V_QnhZ-m-0KBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
خبرنگار:
بارسلونا این‌فصل خیلی خوب بازی میکنه‌نگران‌نیستین؟! ژوزه مورینیو: از نظر تاریخی و فرهنگی رئال مادرید با هیچ تیمی قابل قیاس نیست از مقایسه های مزخرفتون دست بردارید. بعد مسابقه الکلاسیکو از زدن این حرفتون پیشمون خواهید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30192" target="_blank">📅 17:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30191">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa95e86e27.mp4?token=HsHAgLjWS_1UcI2LYH8I6bp6x1vz7aibUYim3kBbNSCt5x77l5LNHJXaXZI4Msvisl-lddvXpyECTyZxEIs2VaUrzhequ6xuKg4SMNwx8l3i8YwWOffwRbLgTz3P3QYBCcuij23NTylZgBHczDHxDpVIFZ3a-Ph77dgEY7YrSy4J-M7oozEmhBwHqqz2Tn3CXsH4FwNKHzdWjZBIQwRfhGWbEaclZAnrKU2FbOF1t3Z2UGwhCBVh5B6L4QSKIdzVyYc3JUKhBH-rBz39AbwhjbcmaVfbXN6LohpjHV_vFCvFA6iUbNY9Wd3oMlVi2v5MP1TJ7141Q5vNMGMSeCbwIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa95e86e27.mp4?token=HsHAgLjWS_1UcI2LYH8I6bp6x1vz7aibUYim3kBbNSCt5x77l5LNHJXaXZI4Msvisl-lddvXpyECTyZxEIs2VaUrzhequ6xuKg4SMNwx8l3i8YwWOffwRbLgTz3P3QYBCcuij23NTylZgBHczDHxDpVIFZ3a-Ph77dgEY7YrSy4J-M7oozEmhBwHqqz2Tn3CXsH4FwNKHzdWjZBIQwRfhGWbEaclZAnrKU2FbOF1t3Z2UGwhCBVh5B6L4QSKIdzVyYc3JUKhBH-rBz39AbwhjbcmaVfbXN6LohpjHV_vFCvFA6iUbNY9Wd3oMlVi2v5MP1TJ7141Q5vNMGMSeCbwIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صدرنشینان لیگ برتر تا پایان هفته ششم رقابت های لیگ برتر؛ هر هفته کدوم تیم صدر نشین بود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30191" target="_blank">📅 17:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30190">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTHOib_DlzGdXwg1tjiJ6sKw6NvW5B5TirJGz7ybWUcn04YaDybeC3aqecyNnEEMx5uNqGQ_MHCsorGyd0vxivr8fHoAsqlkXptzXVWZot3oGJPrWhaLlXxyoFKI8_yTH6e10dUD4ql1N3WhY8x3xoDbtB9h3xXeymqijaPLjonucgN_37yq-yRWJFa5J3tUZxJLiGMzmFvw0G0FUIBFhoklmBIDjzEj1kXLLZF2sYAPLjW3aVURXAXtJ1x0zrNxzNRGN74NQvX6Z1K_G5afpbgtUA_mAfoHoa4nV-gOa_hHky1pDKgIdbFwMfZgu31WHQcoDRWI3lx67JGquwwAiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سلیمانی وکیل علیرضا بیرانوند امروز صبح بعد از کلی رایزنی باعث شد که سربازی‌ این گلر تا اوایل آذرماه به تعویق‌بیفته. او به بیرو قول داده که تا آذر ماهی راهی برای معافیت کامل او پیدا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/30190" target="_blank">📅 16:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30188">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e07dd6207.mp4?token=j8ctvCZgDoTuSktLLylFbpPGCvumNycdDdD5rAYQ5Vs902ec_FUdI5YG5X_JmzqY-AZLHLvkpYWBRvWoqeYjrs3tY_DUpf4B8TYs1otBbX9m80We4NZlxsp7N-E_3AFe3qkxHUBkC6lvXGoH8a_fmuWTkS0j7vhi9HxVQJfjwXi-rgP1G1mE3JhzhwetH6SDwU1yNg-4t0IjZNVgLtmwhPgAwq0iuZ810mns_47F6Qc04ycVWqiy-TLAQAnWnIFj35DfK6lukwHyUgyw6B7tq08xYfpNJzOwH9GmNk29cgBuV5jqjJBoMeOLGu9y8Vm-utbFCtDZE2o8y9JGqCiMRDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e07dd6207.mp4?token=j8ctvCZgDoTuSktLLylFbpPGCvumNycdDdD5rAYQ5Vs902ec_FUdI5YG5X_JmzqY-AZLHLvkpYWBRvWoqeYjrs3tY_DUpf4B8TYs1otBbX9m80We4NZlxsp7N-E_3AFe3qkxHUBkC6lvXGoH8a_fmuWTkS0j7vhi9HxVQJfjwXi-rgP1G1mE3JhzhwetH6SDwU1yNg-4t0IjZNVgLtmwhPgAwq0iuZ810mns_47F6Qc04ycVWqiy-TLAQAnWnIFj35DfK6lukwHyUgyw6B7tq08xYfpNJzOwH9GmNk29cgBuV5jqjJBoMeOLGu9y8Vm-utbFCtDZE2o8y9JGqCiMRDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برسی‌لیست‌بازیکنان‌دعوت‌شده به اردوی تیم ملی برای دیدار دوستانه با ازبکستان و روسیه.
‼️
اللهیار صیادمنش،مهدی‌قایدی، سامان قدوس و علیرضا جهانبخش در این فیفادی غایب اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/30188" target="_blank">📅 16:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30187">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JG1AOQMcl3VKwM_Vif8Dcwvkoyn4aFU62-lw3mnlv5LlGJMea1euVn7JwmwKedWQI0HicM1l1HRsK9r4hrIYuAHTkhLP32lDUJSdvEgtv0uGc-8BPzihFcmn2MDQTbfLPVJ7a5-CIBPBruf5wrzLE__1Qc6La3aZl_IP4upEzS9e1hxtmjXlmP0pRoI1Rb9cQb-rUmyqSp_M_0bn_8PttWtWJQZJPYtRg-KjLxLUmytnV56226GoXv0Dd0moNzrLK8i11JeOjVwcGQgDRpWKROVa0-blXpcif2tUiwMvSviz44BGTZxe-dK_oD-URYffoempDfTJmItmZ3XXlE9uYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گرانیت‌ژاکا ستاره‌ساندرلند تحت‌یک‌پیگرد قانونی قرار گرفته زیرا گفته میشود کارت واکسن کرونای او جعلی‌بوده و بازیکن‌حاضر به زدن‌واکسن نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/30187" target="_blank">📅 15:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30185">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ODxlmw30DH0oKj9wqNkI46LD1SNAXlsbHC1uq0g3Q3txMPs08XikHbOkpm-799Mz17siWqTppbhtfQIcCZvTVBbn8XX4nIY2n-ZcIx25ysILocs1uRUzXuUEvGPFcw9O24sBsOZjcwzdV0rISLGykyWqdt2liw5RvwAw8tgQbKUukByILV6lZc4bjp2ILCIu5aXMJRrNlcVTKbLkWh4oLXUxs015FOTTALfwhuYLRIy4zlajXQDakjbRX2gIhC9ccOBzYlET13Wch37-hIul9zZmIJ_2DtC4E7b5_kbA3ZB8meanOnXbX9_hImftwoIWfpZW1dRFiijrTZ8Fs9lxGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dui-9PFu5jnFPcIF2Tap8nY6cyYbM5I-dJDgySrEkUvE0EbQtxKnRSS-Isv9QZLbVmJiX3xEeu1dMmdszZEuwmSeR8_2VQW76R8VMLUgMVtkS2BbGHVAi2-2MlYe8EIq4vncBf7cGynzz8jthzTJb0GsF5BFfarQj0OtmipT6nuSdCpDBSNQpvVMDIaRo04cCzQuHlBquIgk-Rb2yx8rIn3FCKhZWJng_fR-6us0fiq5-cuYYPrL-0Txf9R-7EGU9N2Ft9ChF1Mi8_uFMJaIbYVdbzZCrPTozubD6zqPuYhKEov1o4STN2oPUnMRvFtAUUy9uj73BCrOmG7s6O1C_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیانا؛ سردار رسما به تیم ملی برگشت؛  فهرست هشت لژیونر دعوت شده: علی نعمتی، محمدمحبی، سعید عزت‌اللهی، محمد قربانی، طارمی، سردارآزمون، دنیس اکرت و شهاب زاهدی 8 بازیکنین که برای دو دیدار دوستانه برابر ازبکستان و روسیه به اردوی تیم ملی ایران…</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/30185" target="_blank">📅 15:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30184">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPGmcg9vKPSSF_hVGYos7FV13NC2VFGPHalwasEifPd73-ZxHDhEyn7jjGT0dfziD-yjEoxfOk6yip10jMDYcB2AYYDHil6fwsv_4sSCAv0qlugvFBAuxor_jW6F56DOlmpNkw4bZKIZSAd4r_z8PtNTlFBNXzpW43wL_ZNZ7Fg-hoMvPdmHhhwXFfoDrpufwNtgqkiAiB7LXqEX_EvHykEITTVifklkwKVpfHpm24YVLX2QfQAUOlAtVbjOK1fpYL_EHqcBDTjVmkjURi6vKOndr29X0gomvGVGY60dBKXPY5sAsSNVJHU4t7UUnMoIA1784bJ3otAkLczEcETY2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
👤
گلزنی تماشایی لیونل مسی در بازی بامداد امروز اینتر میامی در لیگ MLS؛ این 930 امین گل لئو مسی در کل دوران حرفه‌ایش در فوتبال بود‌.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30184" target="_blank">📅 14:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30183">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SjL95f0TclIjCrGm8rRvqRz9KM5GYxAW0B2rPSeQGgqw-pWt6ad7Ge8gyvPLpDZQZe9IFuXdnPItP6PRYocdD73_Dw3Ke2gHyK1lrcPEdom7gPTq0jNvxrQV0G3mpjHV0U3TW0qGyIU8TlKZsODBxJyDCmC4nbDS4JJCjOPUCFkHnTGZpTmM6sK_Eakccp_rFVK-DkmFo5DUnv-qMvgLVtapTsgbZ9WA3mI75zYY5mO44j184qgupVBw0VxKKiEgJCwuX5L6idT9lXtGtRlagDV-wjjsVnU1hbSFySFKEfkxNmaxcSiskijihnbnamb7SxbXikYA1osOyVcSfjMWgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیانا؛ سردار رسما به تیم ملی برگشت؛  فهرست هشت لژیونر دعوت شده: علی نعمتی، محمدمحبی، سعید عزت‌اللهی، محمد قربانی، طارمی، سردارآزمون، دنیس اکرت و شهاب زاهدی 8 بازیکنین که برای دو دیدار دوستانه برابر ازبکستان و روسیه به اردوی تیم ملی ایران…</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/30183" target="_blank">📅 14:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30182">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXlqUWDKBSfDWBmRiml-2jcgzsz6AyQVxf-NqxxQYFui4--HXS98PrsAYB6K_bXNRFuRF8y7GaQGhNXKqyuIdWBhOIPbZOmZ9Btw_FLEdfGAksj4q1v7eSnWgiwKKYJn5diCMDUw12FmGIIOrpXCBe5nyMzyf43mDTHxt2tIWQxoeOVDQexbsd0qekkzK9ZsFtOJMH1ODRjgHPOYyKCADONruXjmUSNdf-HMKRG6QGpSLSLjE5XqJ4tBdgc1Zjk9SkcJ_EnM9OqazJwdt9gLRXTcOkvOJkV2-qFn3rizKRYD9P9prSh9z1xsgFCdEC6qEc55JiBBeuwQT_Vp-0DP5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمد عمری دیدار باذوب‌آهن رو ازدست داد؛ با اعلام پزشکان باشگاه پرسپولیس؛ رباط داخلی محمد عمری ستاره25ساله‌سرخ‌ها دچار کشیدگی شده و به احتمال فراوان حدود 4 الی 6 هفته دور از میادینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30182" target="_blank">📅 14:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30181">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‼️
آرزویی‌که محقق خواهد شد؟ درحالیکه خبرنگار فنرباغچه چندروزپیش‌ گفته‌بود آرزویش اینه رونالدو به این تیم بیاد حالا رسانه‌های عربستانی مدعی شده اند؛ رونالدو در نقل و انتقالات زمستانه به فنرباغچه خواهد پیوست و شاگرد کارتال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/30181" target="_blank">📅 13:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30180">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_7VaJypfqAl4D1ssekWp8K8AcC77av1ciP4wXP07k4juT842qkbp11VFjtXJK3pE4-JMLOZ2Mu0mS_izG2qspqxJoFMuHEWq18TEok3lGLALWugXOnIxHqX3HbZjZsvjU-2w_bJ-ifyYe_V5i-ZxRwNlyCfboIjsQarBPMl-FYAspzLdJ4TVvFkV1qeifZ3RJhMPdCjrzUs6fu6zDXl2YdY7ImOb4d1fADwp1_yF0ika6e6K__-UvcW4MY1S--1kz1E5C7bDbhKwCYUZX-4-o8Q-snD9vx24pSjedSAl8rgFj9XOwg9b7ONq9mtX9qJyBk-IrDayrQGjp2Objtayw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
برگام‌این‌چه‌درخواست‌هایی بوده که بیرو داده!
‼️
علیرضا بیرانوند درخواست معافیت پزشکی داده و دو درخواست از کمیسون پزشکی داشته که اولیش این‌بوده‌گفته‌چون تتو زدم مشکل اعصاب و روان دارم دوم اینکه گفته در سال‌های گذشته رباط دستم بار ها پاره شد و با این دو دلیل…</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/30180" target="_blank">📅 13:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30179">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WyTJyXp7J0MBCzDnOzyhVeVDCKv8yhXHB7oYmNtYbhjJqnRF99z8C5Eg-uJI5txJmF2yoQuPfVIc1crsR_XM754eWNuegFm59zHTbbQKt0OS0Zf7gA2lAAxIcbwFG60isJMQkT21mDZpnJ-D2gL7l-srgXX3C21zQ3PalHnTNC23kBm7Vl0WMxs4YLE0qqmd4y8bWo1Tr1UDnDM8NVWg0EM96s9XsWjVjfY3JuXDTQi-yzKoCrYcpiF5oT15WX6lz0Zpzd59viGAAKaP3KxcfJPgAwl89A9oPboIXhmgtDhZDLq6QQ_gCeuDbu3rlinNpAXiM7JRgC-p_QixIyp6Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
طبق شنیده‌های رسانه پرشیانا؛ سردار آزمون فوق‌ستاره‌خط‌حمله شباب الاهلی برای جام ملت های آسیا 2027 به تیم ملی ایران باز خواهد گشت. بازی های جام ملت های آسیا دی ماه برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/30179" target="_blank">📅 12:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30178">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H71rDvw0tkz-sz5Gt-Dgo7PveBz4zezACU026aGezDrtOV7sv8_wFB2aR2EBUuzKwhEK1anGcsBBIK1N_9GZ0AiTjMf9XmrgJQDEjp5p8dJu-XLZOJRCPH4lePASE_bcifnfnJkKmuRo8ykZUgFtcrhGjbGZujVgTbYkZP4n0MntJhABbC6iBF4KKceJaD1z6qqba2UE528hOHPUq__qJvy4ePlUiseo_s5XmxwKJNK9BLZ0NnLaJL-n5hUEruts-YOmkIQf6_A0j2cVUUJ7xhhug53uFUmwZJgKVVM_j630GNN_knBO5mkYsaxNYpPflBCmpDx4m5akFcTjn4v0QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا بیرانوند دروازه بان تراکتور در جدیدترین درخواست خود از سازمان نظام وظیفه خواسته کهه یک ماه سربازی‌اش به تعویق بندازند چون مریضه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/30178" target="_blank">📅 12:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30177">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RbzIV-njOaIiAXxY4X2u9YwdruvqsRVeL8yTQWgy-RUOHeLM4JorEf9RI-8ydjRkpNM09TfTlOAXACrUqOEUGXM4c1XRxHRdRpn_MAAPrkaBXv24GJGdfVsMb5CjYVrkUW00eeFGb4w7xQbvUScb_oOj3TiXIoZQ1M7RjBs6MKsl7hRIkPv6JCP1cjL4JQu9osnQd2WREhzCKoHCJSpZdbruG6CAdvItjMW8msX5NkYXD7q5hSAtJNwj5LnvKYjc9w3FzMXLO5oRMdJkPCJxowlskNJSzHKRzo3zsjzK79q08DYWzPL2kzbxgf1-kVFfIFTPnilKZpCqtFlSnWZy0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
نمایی‌واضح‌تر از خطای‌شدیدی که باعث شد فده والورده حدود یک‌ماه دور از میادین باشه. تموم کارشناسان گفتن اینجا اتلتیکو مادرید باید دهه نفره میشد اما داورمسابقه بازیکن‌حریف رو اخراج نکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30177" target="_blank">📅 12:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30176">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b904658a51.mp4?token=BlQkJJ6yJlEtbrpj-p3p3tiubmGwV1sIo1vfIKhpeXtRSogNfehPSos3O0DkHrYbGxx7G9efqQEf4dR3UhuTl7e-DSfNYr6kJLbabKRxpBEDp-8J3oCRp2ci4FOxfxw1vQn7h3LcH0P8m-c-rdqYYll9m-P6Mbbaw7fIFK1TTjcQu8w4OA1VoSqQSvVfum95R4LOKrrmhWweIE6Bh4A_dCtl8FreEfTNzFG3WJCt1v5ybRZttIg0HTK8wGRToKzgE86kftM2BgYeLDCec8kPvZNB-J5uusKp-uOqbdiH1cs4VRUWhxAxY9pC7O8tX4dAlfhh6AKHrq1Y_BTfSNN0ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b904658a51.mp4?token=BlQkJJ6yJlEtbrpj-p3p3tiubmGwV1sIo1vfIKhpeXtRSogNfehPSos3O0DkHrYbGxx7G9efqQEf4dR3UhuTl7e-DSfNYr6kJLbabKRxpBEDp-8J3oCRp2ci4FOxfxw1vQn7h3LcH0P8m-c-rdqYYll9m-P6Mbbaw7fIFK1TTjcQu8w4OA1VoSqQSvVfum95R4LOKrrmhWweIE6Bh4A_dCtl8FreEfTNzFG3WJCt1v5ybRZttIg0HTK8wGRToKzgE86kftM2BgYeLDCec8kPvZNB-J5uusKp-uOqbdiH1cs4VRUWhxAxY9pC7O8tX4dAlfhh6AKHrq1Y_BTfSNN0ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توصیه‌های‌محمدسیانکی‌گزارشگر بازیای فوتبال به شاگردان در مستطیل سبز که منجر به گلزنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30176" target="_blank">📅 12:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30174">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42e997aab4.mp4?token=lEV3uwiwl7LGAeAlr12436FPIftoGBiXdR2tnRbwdMR6UUms876H8T_z3X1GqOO0E8rmX7bFCXZNSTc0pb8lsCLVk53phX53YoeHnWD7vNL77d4_co53EkFcVFgqruUJGIJc2XKyuRxhJnooLzudUb1ZnXKLC_6QLOgTk_H9DC2ZXiU0POYvBZMUKfE7Yy4Qn0Df4OHKZrjoW4FHdQsi5CN0Khfx4Nerp5HADpLg4F5q32XgMjkuj0vRG9Wk9z4r-EzYifwPbKFrR97_YmWMyn56Dke0dkWzRzc9ELkEknvS2ODn6qtTt3hhYephl-RbMp25Z1b2pAkt53VP8HBLeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42e997aab4.mp4?token=lEV3uwiwl7LGAeAlr12436FPIftoGBiXdR2tnRbwdMR6UUms876H8T_z3X1GqOO0E8rmX7bFCXZNSTc0pb8lsCLVk53phX53YoeHnWD7vNL77d4_co53EkFcVFgqruUJGIJc2XKyuRxhJnooLzudUb1ZnXKLC_6QLOgTk_H9DC2ZXiU0POYvBZMUKfE7Yy4Qn0Df4OHKZrjoW4FHdQsi5CN0Khfx4Nerp5HADpLg4F5q32XgMjkuj0vRG9Wk9z4r-EzYifwPbKFrR97_YmWMyn56Dke0dkWzRzc9ELkEknvS2ODn6qtTt3hhYephl-RbMp25Z1b2pAkt53VP8HBLeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کل‌کل‌کردن دوستاره‌انگلیسی و آرژانتینی در بازی امشب رئال مادرید
🆚
اتلتیکو مادرید: جود بیلینگهام: تو لیگ قهرمانان اروپا داری رو من تکل میزنی؟ کوتی رومرو: تو جام جهانی داری با من حرف میزنی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/30174" target="_blank">📅 11:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30172">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BK1T_hyG8ZISNSpHjG09JPZlqmMg829u3Pq7gg995vKzW9OJvw7R2LY9yPCNgZriLBqZIOyBiqKBB_xpvM-ugnWzJ84Y7WmbEZUJcPpbMXxdA_PVa51csJzRNG475lXh4ajg1Vheer8nY2-TMkX_wXXTulzcgBdmHK9lQl0_INdFUv1oHOtITRajdfMpT3Zg98RFx3XT6zxiFWhNfR5kh9nLfxwVJXHTrjuKIvcyx1id9AB6YvjYgis6QEUJPui9ONONIxKh2nNkkeMslPMR9hVuCUJLfBm5VO-FTJ7OiT-IZhrF51Z9B0g8qHtBjwHJsSNHGxW8V_Sw3fmtFGLEkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
دو مسابقه استقلال-شمس‌آذر و تراکتور - فجر سپاسی شیراز در هفته یازدهم رقابت های لیگ برتر به دلیل بازی های آسیایی این دو تیم لغو خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30172" target="_blank">📅 11:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30171">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPT303kkRQGNzqk1b7ZPn2q6JfOibdvT4kcwm-e-6m28h7bEAZRc_5N7HSZnRmxPVlzQjuwSvHLymc6FZ4aL1eqw_zCsERBgsxw6GPgr1H76UjOOshOTC2jM0lDe8Qrp3BxsJEDvBOl2pXkapjKEZzwuYmgm6u_lKTfFX5YBDe5Z4KhzUqxxZr_UXAAi0y93jwg8mZwJVNDP9dV5DoV0lp9YHAWMReBY3doXIJZxYGu5rrNh76k7aNPYQs1WdGKsPwHm8G1UscCpiBtBd7CYtKJcO4N3P9p15rs0cvAHUIp6Roops66CORgS6agEpoFrR94bpVmL3hFEdrPueo3oww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت نهایی سه نوع آیفون 18 پرو، پرومکس و دائو اعلام شد؛ آیفون تاشو یک میلیاردتومان ناقابل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30171" target="_blank">📅 10:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30169">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/stBhkiw_zmeKzHgy3JrDedZZkQcIYHfJ9ACOmLyw7AxQgluyWGMz_ny4zARpE2Mi2AQ4qbaozhllkIThFzNeWwQHifIvEtpzaNPgzEo3sWquwLesXam6zjVu18IQCdVkAT_8I26j1P-qVJSp86LDGUZdhJjoYy-iBiNKqovNHwzOJKK_gN4EgxIpR8O-4PIeXVBvts1DjaJKGG2FlUOzhjQ8LzOR7SXfkyzeHZnD-YWdZ3bBHBPaRLy6ImLY0YSv5zyOB-HNIX5nWlSiIr36UCpgXjCxii2azw2CU06aNGvENLWMJCxsAca--MBA_othN4cqGP4RYedROlkGOjyMyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wzq11AwF16-pliEKLbVJUq8Gax5b27ui5fJ1mNM3vl4QnLWeDAe9W3QvT512iWy5vUM42FIGlCykAsLPN1Wj96P_YpdxTaljdWWFjqGeZzuCRqPmFrvdRJHbVDa9I9zLbYWXYoaLBvOpq0kncPB2f7NnRVx273Z6fZ5h5XFIlyJRKsqTRXixB28Ko7V_TbUp7vQ7rcjtUi6V1_ViKs4njOc5Q4oxgRmn_nkj5TJVuiglsDUNidL7oQ_UQAb3EeilVR98o96w9iN0b84S6N1ANlERN9aXSSvFDgaXGceFdE6ly40LvDiTy-CunKY6yMeKDyH3sX_Rc4iQoPHAcyd3rw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
برنامه دیدارهای آینده استقلال، پرسپولیس، تراکتور و سپاهان در تمام رقابتای لیگ و ACL.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30169" target="_blank">📅 10:31 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30168">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3jM9jK83vLsJVH7-_phNvAMg8v3EVOQ3z-BQ-EqLt66qpLF3onu859LSxnQ-bSCWvyFh0BaT9AfWNQMm7nzpsylKq7kZbcUe5VLF_vn7mqpKGZZMsgl6Ng-I6OWGpIsfaudtEP6P38Nsz8VrEsNxUtp3P-8sxhyC-hFxpvJHdK7i6pgPTtBchipcQzjNxjYMn1ynbY4vgWroI6rGodtj7-sDDBOAmdQKj3WI786OXcgDacNebabewRqe-7_pZdPVIk7mk8q7cCDyi9f6q2om-vOSqNj7BLnmpHQyTlBXFr8hHNJnpz-40Rir9I4zO9xxmMrpFHokMbW47BTAdCK0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اولی هوینس رئیس باشگاه بایرن‌مونیخ: فروش اولیسه به تیم‌رئال‌مادرید؟ ازخنده روده‌بر شدم! حتی امپراتور ژاپنم‌ بیاد پیش ما اولیسه رو بهش نمیدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30168" target="_blank">📅 10:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30167">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015580725f.mp4?token=NwUDomFUPgEoiOVdryvYIEya_Q69ls2xGWkium2yZHxJHnopwpBQaSJsqkeYz7wv3XfMPnuQvqm6n1OE0ekEAWBUVObb_kk0ppq2PvWENLejaatxv2SenxagvDD-h2of_sy4j-x3lJBUgAaIUYF_7WdH8LfYgS2lVAuU_eZIR9UHCTg2b1z_ln9mF56ng-KknZR-VIggmYxtPWBkgQIAv2UXvk3YPt0eku_un_AskoNi2KPbWNKzE2WowujHW1zfhEH7gk0VCWt-SGWejoEZXr7_UGMkiNtfNBHWl4L8gOs4LTr27JcPfJz5Ao2JNQaS-mHD2izgJ3JMi5sI81Q4lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015580725f.mp4?token=NwUDomFUPgEoiOVdryvYIEya_Q69ls2xGWkium2yZHxJHnopwpBQaSJsqkeYz7wv3XfMPnuQvqm6n1OE0ekEAWBUVObb_kk0ppq2PvWENLejaatxv2SenxagvDD-h2of_sy4j-x3lJBUgAaIUYF_7WdH8LfYgS2lVAuU_eZIR9UHCTg2b1z_ln9mF56ng-KknZR-VIggmYxtPWBkgQIAv2UXvk3YPt0eku_un_AskoNi2KPbWNKzE2WowujHW1zfhEH7gk0VCWt-SGWejoEZXr7_UGMkiNtfNBHWl4L8gOs4LTr27JcPfJz5Ao2JNQaS-mHD2izgJ3JMi5sI81Q4lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
👤
گلزنی تماشایی لیونل مسی در بازی بامداد امروز اینتر میامی در لیگ MLS؛ این 930 امین گل لئو مسی در کل دوران حرفه‌ایش در فوتبال بود‌.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30167" target="_blank">📅 09:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30166">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWm2CxBEKh9FEZ-nu7Je2Mf4ofOoQfnFXn4H6L1PVsMkhI7rieefSahuaD9ttAnWUxZyptDBpWeYQR5kIiKt3z0JsnYjAThIZ_WIXWVdYcZJe4m4o_6wT6vOQMgr4QhkuYZlLPaT9_aE03kXqVlToQExyrBRI_jfyCKVpAmsxhUWLX_8i1mo9IGfdNrvYSrhMVftTOS2tcx5buFHI6x4-ZkoAe8QpUt8uUjuhRmyemSHTeNVaB-jbSKmJu9p4Mvv_Ve9fYtYqF2g4qxEc8VD0A8IlMPbYmgM7R09QTuZQtr0BDjAM0YSLJ4f2fnfUSoS-dKMU3MT03ugbf78mKDcdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛ میلانِ اموریم در دیداری خانگی با سه گل از سد تیم‌لچه گذشت. میلان با این برد یازده امتیازی‌شد و در رتبه پنجم جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/30166" target="_blank">📅 09:22 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30165">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed8af73188.mp4?token=IDgWDw8yErK9iPgoYQ9l9W3PSp30hH4XqA-Xj7Pixm6Ll2IWi1jDXfH_O8ARkXwED6O97Lcq_yQw5hxgNnkCPphGpfS4HS1bcY3An0ma4r_n9jFHkGUBkRxGvamCkYGZBG7OsNxokFKTPoIu6Z4TMtFzmJHZUHz1RwDyAFj0sCtN2cKPXy-IBP9lbLyGiW-eZZjSl-4es04e4oexPqetZKs6e_Tfxr-unsg6xQaTykK3XzrQfAfjIALjZDOb02IldE4gXMSljU5G3yS3ipNh-v50NdexHR4gSKWQvkeO6Wy2_wBh0Bq5CpqFPB_FDPxiE0USsjMb17ld9Y8x2gVVug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed8af73188.mp4?token=IDgWDw8yErK9iPgoYQ9l9W3PSp30hH4XqA-Xj7Pixm6Ll2IWi1jDXfH_O8ARkXwED6O97Lcq_yQw5hxgNnkCPphGpfS4HS1bcY3An0ma4r_n9jFHkGUBkRxGvamCkYGZBG7OsNxokFKTPoIu6Z4TMtFzmJHZUHz1RwDyAFj0sCtN2cKPXy-IBP9lbLyGiW-eZZjSl-4es04e4oexPqetZKs6e_Tfxr-unsg6xQaTykK3XzrQfAfjIALjZDOb02IldE4gXMSljU5G3yS3ipNh-v50NdexHR4gSKWQvkeO6Wy2_wBh0Bq5CpqFPB_FDPxiE0USsjMb17ld9Y8x2gVVug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
مقایسه جذاب از عملکرد کریس رونالدو و لیونل مسی که ابر ستاره تاریخ در فوتبال اروپا رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/30165" target="_blank">📅 09:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30164">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGtD8Vl6x4KjKwG7JOOpdXErRybCDtTFfhoG7igMMOOX4n_SJwK1Zc9RkXBRCF2wfWhAQXkAiqOeZbLEAGIjCpemKnwyazvnNvy1f6oA1Pg60JgLYnONGO_xDrZObizEUmTJisIBAv6N1fdf0gvKawHfWn8JD2hd0ptWI-HaqWfUpKS2iPul7fTgstOpT9coKHL5KLxMPYAIEXNXCJzyFohmbO4GmoxGme61oOkx-8ywc6T2g3oCCPlkVp5sADSDjNgyFiYvRL4XmVYH9T5NvJaZfTCV3whjjdFcKMT4ROrdk1LWUv9fXrmrO4aAtzKPBypW9mYJTAUrIivuPvlL6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
پوریاپورعلی‌هافبک‌پرسپولیس درگفتگو با عادل: عروسی خواهر زادم بود ولی وقتی شما زنگ زدین دیگه قید حضور تو عروسی خواهر زاده‌ام رو زدم.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/30164" target="_blank">📅 00:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30163">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDSWVxVKmk9xmCK_lkN4Id7RM-3-lA4nvgZI6GNrsqkntH_Np_t3Ftl0VirJxdWN-BnAAG2Q4QCaDMoUMADllUTD548tYci2JF6ThC96d3LB4YACx51TSiH1uEcNU9QClxGk8V72SATWBcS_wn7_um_ad_llycYO3EfjNkS7Hx7ophHokA1DkkjbV_8wjwsQr7QjwqWkLBNUuN-cCzPsFYkty75P1Aq-yNnbGLQevNo7x9DqARCrny1S4ieDjrlL4Xkn1KO134H2sKkvGqgNCsE7syK_ZMCDS4n9Rv0xclDRN0NO6kk5b9zLvVrOcxMFadr-WZESqqCi3xH5Y3tpEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
الریاضیه‌عربستان:جدایی‌کریستیانو رونالدو از النصر در ژانویه قطعی شده. رونالدو قصد داره به فوتبال اروپا و لیگ جزیره برگرده مگر اینکه باشگاه الهلال پیشنهادی نجومی و سنگین به CR7 بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/30163" target="_blank">📅 00:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30161">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HF2FzpFMQ7be4V8ETZOpeG3rXAmzv2g7p8kQetwVG-ZWsuHWbqATknKmDNDwazUNLTUqLJa1SatNBp_XCTN3a4oBcyBED-9Z8S8rVPeq9TY1M95S_Kbv56HZ3BpzutFNuAS8Bim7N3SPy8rBrZe3YX5H_hiFdNqvJOi_RqCpKPtOqdUJ_8LbOMLabHp5hwxoJ6de-ITAAEJGB62XRaIhBlkW6Lc1j7e43UFrM0efqBl5NmoDjrY7lk5Aa4HdRwB2gecT0hVklWenDzhGUo0tteDm-r5GCnRqEj34306tqCKCTR3n-3QbC6ye9bS5n8JXDFOj3LiQs6WgWRK__6j4xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها ‌‌‌‌‌‌‌دیدار مهم امروز
؛ جدال خانگی لیونل مسی و یارانش باسن‌دیگو پیش‌از آغازفیفادی و بازی‌های ملی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/30161" target="_blank">📅 00:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30160">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llxBalL3Z1KD2JHfLIJOVDfucg8YM9QnKVPFzInlEmSuWAwwieMqtYuu79WzvK0Bzbo5r8pi8jRUGHL97GlaLzlBwdSXQdxGBbyb2QjrYJXQMfHUWPTlZRwIrEjQizxHl-G7YcBbNZavigFApkJxoKB60h2MPnoDeX2r_7ReVfFjfgqzxa7QJJ01vTIF6j0uaS0ZSz5vLagakxrguYy88Ii_AvMv2UXRGqrXE52NGpHF5zhDAWMDLyxMrfuyb_RF8XzaBNi4cpusBiFzM3r_ViVNPX0-B7-NKbzES01BzmvPFDiZNiAlrl94RjNoI18uzeuGYR5N_aZjl9mrnTpfWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
برتری‌بزرگ‌ال‌چولو در دربی مادرید و برد اقتصادی لیورپولی‌ها با تک‌گل ایساک!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/30160" target="_blank">📅 00:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30158">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛ میلانِ اموریم در دیداری خانگی با سه گل از سد تیم‌لچه گذشت. میلان با این برد یازده امتیازی‌شد و در رتبه پنجم جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30158" target="_blank">📅 00:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30157">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba92349391.mp4?token=QfyU33NBqSs-iOyBLoJLRV-aRyKWXcjsFjjUKx7hUn-C0ITk48FTXYRNWGQBsamx8JVY_LldTHXFWfwrxfKzj3E82cYmtXA8AgRMkeo1hv5rv6w2QlfH4w9alFKBcVX3nQZjwJ2zsRHRLJffwKuAP-HXt9AXeUoXmMoWZauUrVwgrUIdZksd0Hb3mQuSMWKAlv_qWtfdpVwd9ZE4z1oXXP4EzbzZN49cPKWlm4JhIj7ZPji4884orMfcN60ziyD7qtg-8MpNmXBIEyODr9t5tHVYVMMw0VzRyfp2DXVqHbJyM9L_R465kiZ68zGAs3r-tfsq8Jm2PUY_nChD4k_NWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba92349391.mp4?token=QfyU33NBqSs-iOyBLoJLRV-aRyKWXcjsFjjUKx7hUn-C0ITk48FTXYRNWGQBsamx8JVY_LldTHXFWfwrxfKzj3E82cYmtXA8AgRMkeo1hv5rv6w2QlfH4w9alFKBcVX3nQZjwJ2zsRHRLJffwKuAP-HXt9AXeUoXmMoWZauUrVwgrUIdZksd0Hb3mQuSMWKAlv_qWtfdpVwd9ZE4z1oXXP4EzbzZN49cPKWlm4JhIj7ZPji4884orMfcN60ziyD7qtg-8MpNmXBIEyODr9t5tHVYVMMw0VzRyfp2DXVqHbJyM9L_R465kiZ68zGAs3r-tfsq8Jm2PUY_nChD4k_NWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛
میلانِ اموریم در دیداری خانگی با سه گل از سد تیم‌لچه گذشت. میلان با این برد یازده امتیازی‌شد و در رتبه پنجم جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30157" target="_blank">📅 00:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30156">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fc0vltAVatL0oSejLui8sZVEbV9B_MPS8VgoPz5BcTcdHDUx1BEmwe_Xy1pLa3o2_jR7G7kOgDuAZUq9ugW_aUN0Z025bhfMiJxFy5Ss7gEy0Zd70Wm-Qvu92DfOJ_usl-oPIMPU9wrrFTzk8E3wHRYNXhKvKCRjPuyL8bQCCMqNqzRVIzi7vLN2KT4Zdo7aJPuJYPHS0hZ40RhdGSRYxcoTSrOoQtG3X0Yh4OCLKtmHpaPiiHNSq68ovOTq4kPdNgXPmb89LCdZICd2jkAyQO9h4lAnxUHHZVPavS4p1VAJ622KIvOM4eBjDhnzC0R9ckuE3HglqMbaG9Ti1vVw3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇦🇷
کریستین رومرو با سران اتلتیکو مادرید برای عقد قراردادی چهار ساله با این باشگاه به توافق کامل رسید. رومرو در دوهفته‌گذشته پیشنهادات دو باشگاه آرسنال و بارسلونا رو رد کرده و گفته بود به سیمئونه قول داده بعد از جام‌جهانی‌راهی اتلتیکومادرید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30156" target="_blank">📅 23:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30154">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b64B4wD3wugz-wxnxfj6E2tCdgAhV-FDAhH1H7GhMCgcyhsd7Rg475AtvckjmLadFJF3nMbFVXvydbSkoGNdN8F6a_qf9dq2uhS99t2ZjHioEZzRRpU0bK_oLkeO6G-6jIT1hkDUayRf0q5PjL2_B0ZRCACYXqgk3MswRmhIdOqDxXIAVXc73RHhk8Zcd818RrSqMYywcsvRfahjhI4n4Ax9eHwf-wjzQZLXVs-0blrcM2eZqhMqOVm1v1RcBoKj9wTSJUKUeHh8MPK5k0BNFoE6hIgcRmygmxJ9DIko8frqVm-mRwWuperohwkjqTmgYmo7b5CyQyrRWL44Hzy7eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dj4mD0G-arZ45Tj8yyVMee9E4-VcF0D65G6_W0zwd7l7vlfj9tZEZamAsTyfRpniRJ34YSbAZCTIHt5Oxwm5QtasFh2ujU1eKKJOEDHs2OacxahY8J69xucaPZqZ3bii4pMNVDMv0_zWEaK1lyzs6SiUlPVTm_-LAt6Cq4MnomPIzVJXbLjdG0lPAKuUo9jajXwWWtGaiOsY_ArWerbrCg2_lOrShVFwTtmYtTki_YmmS2pfzwNbHldAf6u8XYAjdi3lwlWc3dM42F0A_EJtoSJqRIffI3qE7XA2ik2hK0jo1mRNJ8jNeTdeYPxPm9i9BLBCLaRD0mZlb0jx5CpDfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
عملکرد رافینیا و یامال درفصل جاری همراه با عملکرد کلی رافینیا در بارسا؛ بازیکنیکه بعد از ژاوی داشتن میفروختنس فلیک احیاش کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/30154" target="_blank">📅 23:40 · 29 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
