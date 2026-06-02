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
<img src="https://cdn4.telesco.pe/file/mISUfc3zx4DIhEodjzsPfoDuXOdB4KjxGEmg0s996I2AavhSb6H09r75hBcTQiZy-HqaJtU8DzRxkPblpNk6DULn-a0sUQyx81v8vXwfvv8aDQ45ayH2TW8EMsC5s_8V93EGcWUZpEDDiaqvuRz1eTzebyPju5tfYKBTVmmnUZUB-ER8RydLXgc9ASXPCi_I5F9FJqMxhRaLibQNm6O_UCD2brxvqWj0XlI_M20rjIhnuLtpahg3b2mrylZ8x1QVceGc6oE54_3PWDPH-PVz0CCa2_9vXgSeYK25aIoi9ZWIIJYdk07qw90SsGQ80CMs53_r2YFWfrsflALhZXSPZQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 9.86K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 13:15:45</div>
<hr>

<div class="tg-post" id="msg-16863">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">فرستاده آمریکا باراک:   این بخش از جهان تنها زور را میپذیرد</div>
<div class="tg-footer">👁️ 910 · <a href="https://t.me/SBoxxx/16863" target="_blank">📅 12:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16862">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">این تصویر را ترامپ دیروز پست کرده بود.  کلمه discombobulator را پیشتر ترامپ در توصیف سلاح مخفی سری که آمریکا در جریان ربودن مادورو استفاده کرد به کار برده بود و دیروز دوباره گویا به این سلاح اشاره کرده است.  گویا این سلاح به نوعی در مختل کردن کلیه دستگاه های…</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/SBoxxx/16862" target="_blank">📅 11:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16861">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">آکسیوس: مشاجره شدید ترامپ و نتانیاهو بر سر تشدید تنش‌ها در لبنان  اکسیوس گزارش داد که دونالد ترامپ در تماس تلفنی با بنیامین نتانیاهو به‌شدت از تشدید عملیات اسرائیل در لبنان انتقاد کرده است.  بر اساس این گزارش، ترامپ با لحنی تند به نتانیاهو گفته است:
▪️
«تو…</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SBoxxx/16861" target="_blank">📅 07:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16860">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">آکسیوس: مشاجره شدید ترامپ و نتانیاهو بر سر تشدید تنش‌ها در لبنان
اکسیوس گزارش داد که
دونالد ترامپ
در تماس تلفنی با
بنیامین نتانیاهو
به‌شدت از تشدید عملیات اسرائیل در لبنان انتقاد کرده است.
بر اساس این گزارش، ترامپ با لحنی تند به نتانیاهو گفته است:
▪️
«تو دیوانه شده‌ای. داری چه کار می‌کنی؟»
▪️
«اگر من نبودم الان در زندان بودی.»
▪️
«دارم تو را نجات می‌دهم.»
▪️
«الان همه از تو متنفرند.»
▪️
«به خاطر این اتفاقات، همه از اسرائیل متنفر شده‌اند.»
یک مقام آمریکایی به آکسیوس گفته این تماس یکی از
پرتنش‌ترین و تندترین گفت‌وگوها
میان دو رهبر بوده است.</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SBoxxx/16860" target="_blank">📅 07:13 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16859">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from📣خبر فوری ایران💯</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11be99e5c8.mp4?token=ajFOOL8EE6cyAGMvX4_Zlj9hwFqgoryh2eQ_9ph7J22te1OHknXTf4ObNMgmKcYGrok3C_Ei_cB40vCuUyvsttgsc56Sjy4pkA3jjxD_KbLtOSmM_1eqEVxumGFOrSG50VRg3JiOdamaFYRvOGZXwmDs1FvaLIFiDq4Bx_3M4TnFgtfDCA-lGeGCf3Te-YUdYPnN7Kr0j2NDcbKUs4RjvNPseYoMQzBgeR4tP_V58zR4AAmLIMTkU5ZXEuv189IkbIECtANWYmy60jWckhRGkVjH_eUqwZJEKoIi9xsWNHXXq2NrAciawXbmwJlDUpxxIe02zFqRtFVMX_mpcvI4A4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11be99e5c8.mp4?token=ajFOOL8EE6cyAGMvX4_Zlj9hwFqgoryh2eQ_9ph7J22te1OHknXTf4ObNMgmKcYGrok3C_Ei_cB40vCuUyvsttgsc56Sjy4pkA3jjxD_KbLtOSmM_1eqEVxumGFOrSG50VRg3JiOdamaFYRvOGZXwmDs1FvaLIFiDq4Bx_3M4TnFgtfDCA-lGeGCf3Te-YUdYPnN7Kr0j2NDcbKUs4RjvNPseYoMQzBgeR4tP_V58zR4AAmLIMTkU5ZXEuv189IkbIECtANWYmy60jWckhRGkVjH_eUqwZJEKoIi9xsWNHXXq2NrAciawXbmwJlDUpxxIe02zFqRtFVMX_mpcvI4A4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصاحبه با یک خانم فرانسوی در میدان انقلاب تهران که در تجمعات انقلابی این شبها شرکت می کند
🆑
@kh_fouri
🇮🇷</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SBoxxx/16859" target="_blank">📅 00:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16858">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxGOwWnawITHBiF5VD-96VnyCI_lrcx5b9t5yJE8vkAh-_RP03VkmblMp4aTxrWAAWs2hIWW_QapQNCq3lbmhHyhGtGwuH4Cno4twyub9mOz5NRxhdEuONxUM96XdmLmucToS0VblulfY9di5QJ_M4mZnStqD-vI-dIyBjyvMOIivJo0qIA6zOMtFaryOIyUiixmBCy96nMmv705XZjDvzx-M47DpgFLwuEvxk46BNonJUSuzYxzAH64KV7GM4IcUUujeqVrtxWIgeWixQLerhUadIAGB7hmCy_n-lXc7Mbul0L5XMKu4DjbH7kmV3sW8YTVS5Hp-JoG-VHeVcCOBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
قالیباف در گفت‌وگو با رئیس مجلس لبنان: جان ما و شما یکی، و پیوند ایران و لبنان ناگسستنی است
💬
رئیس مجلس و رئیس هیات مذاکره کنندۀ ایران در گفت‌وگو با نبیه بری، رئیس مجلس لبنان:
🔻
حزب‌الله و امل امروز هم از سرزمین مادری‌شان و هم از امت اسلامی دفاع می‌کنند. از این جهت پیوند ایران و لبنان ناگسستنی است و جان ما و شما یکی است.
🔻
در ۲ روز گذشته با جدیت توقف حملات اسرائیل را دنبال کرده‌ایم و اگر جنایت‌ها ادامه پیدا کند نه‌تنها روند گفت‌وگوها را متوقف می‌کنیم بلکه جلوی رژیم‌صهیونیستی خواهیم ایستاد.
🔻
ما مصمم هستیم که آتش‌بس در همه‌جای لبنان و به‌ویژه در جنوب این کشور برقرار شود.
🔻
چنانچه توافقی برای پایان جنگ بین ایران و آمریکا شکل بگیرد شامل توقف حملات در همه جبهه‌ها به‌ویژه لبنان خواهد بود.
🔸
رئیس مجلس لبنان ضمن تقدیر از تلاش‌های جمهوری اسلامی ایران برای توقف جنایت‌های رژیم صهیونیستی گفت: لبنان هرگز مواضع مثبت ایران در این مرحلۀ حساس را فراموش نمی‌کند.</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SBoxxx/16858" target="_blank">📅 00:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16857">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">شما خونه تون مورچه داره؟!</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SBoxxx/16857" target="_blank">📅 00:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16856">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حزب الله پیشنهاد آتش بس را رد کرده و به سمت شمال اسرائیل حمله راکتی کرد!</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SBoxxx/16856" target="_blank">📅 00:24 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16855">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ادعای رسانه اسراییلی: تعویق حمله به ضاحیه بیروت در پی مداخله آمریکا  سازمان رادیو و تلویزیون اسراییل  گزارش داد که طرح حمله نظامی به ضاحیه جنوبی بیروت به دلیل دخالت‌های طرف آمریکایی به تعویق افتاده است.</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/16855" target="_blank">📅 23:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16854">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نمیدانم منظور جناب ولایتی از اشاره به «ذات السلاسل» کدام جنگ است اما بد نیست بدانید که هر دو جنگ موسوم به این نام توسط سگ هایی رهبری شد که هم ضدایرانی بودند و هم ضدشیعی.   یکی توسط عمروعاص (دوست صمیمی رفیق بهزاد ف) ضد وحوش دیگر عرب و دیگری توسط خالد بن ولید…</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/16854" target="_blank">📅 22:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16853">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">نمیدانم منظور جناب ولایتی از اشاره به «ذات السلاسل» کدام جنگ است اما بد نیست بدانید که هر دو جنگ موسوم به این نام توسط سگ هایی رهبری شد که هم ضدایرانی بودند و هم ضدشیعی.
یکی توسط عمروعاص (دوست صمیمی رفیق بهزاد ف) ضد وحوش دیگر عرب و دیگری توسط
خالد بن ولید
حرامزاده ضد ایرانیان.</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SBoxxx/16853" target="_blank">📅 22:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16852">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ولایتی:
بمباران ضاحیه ونقض آتش‌بس عجلۀ رژیم جعلی برای پایان دادن به تاریخ نحس خویش است.
🔹
شما آغاز کردید، اما برخلاف انفعال تماشاچیان منطقه، ایران و جبهه مقاومت تا آخر کنار مردم عزیز لبنان، از مسلمان تا مارونی ایستاده است.
🔹
تاریخ تکرار میشود و پاسخی از جنس «ذات‌السلاسل» در راه است تا زنجیرهای اسارت را بگسلد. «نقطه‌ی پایان این کتاب باماست».</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/16852" target="_blank">📅 22:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16851">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">انتشار اخباری دال بر پرتاب موشک از کرج!</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/16851" target="_blank">📅 21:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16850">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">انتشار اخباری دال بر پرتاب موشک از کرج!</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/16850" target="_blank">📅 21:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16849">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zp15-AxOkCl0nVs9isFavJxEZSts6udqmcCpwfJsenkNNdVwJKi4NBjYWWorb9YxGl0rRij1OGz60MVGhhClsNkwA-DeE7SMsO7tUxRNM2VDE8-SqjMonqvkMIDt3yfIZVlIRHiXUHizJp1ZefuQqEqH3vigvLXAo8tEmwXNaxc-um2ZjHZFUdDv7LT7X29BC5aklDSaf6pwPInJO7kSOvoth9vZwYVlsXNDewtNSzI24YvLsTE4tp3CVqt9nSXRe6gA88kAnjS4IuNgZ2zkjNo61-ck7HYNh-ilaf5LHdot5XbFzhyfG_DF14ZrvmZWK58D6V-eh-pZDiEoZO9n-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با این جهش وحشتناک قیمت نفت در همین یکی دو ساعت، ترامپ مجبور به عقب نشینی است.</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/16849" target="_blank">📅 21:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16848">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">حزب الله از طریق ناهیب بري، رئیس پارلمان لبنان، به ایالات متحده اطلاع داده است که آماده پذیرش آتش‌بس کامل و فوری با اسرائیل است.</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/16848" target="_blank">📅 20:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16847">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">با این جهش وحشتناک قیمت نفت در همین یکی دو ساعت، ترامپ مجبور به عقب نشینی است.</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SBoxxx/16847" target="_blank">📅 20:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16846">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ادعای رسانه اسراییلی: تعویق حمله به ضاحیه بیروت در پی مداخله آمریکا  سازمان رادیو و تلویزیون اسراییل  گزارش داد که طرح حمله نظامی به ضاحیه جنوبی بیروت به دلیل دخالت‌های طرف آمریکایی به تعویق افتاده است.</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/16846" target="_blank">📅 20:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16845">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">— رئیس‌جمهور آمریکا ترامپ و نخست‌وزیر اسرائیل نتانیاهو در حال حاضر در حال صحبت تلفنی هستند.</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/16845" target="_blank">📅 20:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16844">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">چرا میخند؟</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/16844" target="_blank">📅 20:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16843">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">با دوستان مروت؛ با دشمنان مدارا</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SBoxxx/16843" target="_blank">📅 20:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16842">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">محسن رضایی: صبر ایران حدی دارد  تنگه هرمز تحت مدیریت ایران است. اجازه تداوم محاصره دریایی را نخواهیم داد و تشدید تنش در لبنان هم تحمل نخواهد شد. صبر نیروهای مسلح جمهوری اسلامی ایران حدی دارد.</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/16842" target="_blank">📅 20:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16841">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">با این جهش وحشتناک قیمت نفت در همین یکی دو ساعت، ترامپ مجبور به عقب نشینی است.</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SBoxxx/16841" target="_blank">📅 20:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16840">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ به ان‌بی‌سی: ما محاصره تنگه هرمز را حفظ خواهیم کرد.</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/16840" target="_blank">📅 19:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16839">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامپ به ان‌بی‌سی: ما محاصره تنگه هرمز را حفظ خواهیم کرد.</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SBoxxx/16839" target="_blank">📅 19:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16838">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حالا توجه کنید که در همین مدت که آمریکایی ها دهها کشتی تجاری را از تنگه هرمز عبور داده اند، محاصره دریایی شان را کماکان اعمال میکنند و این یعنی کارتی که ایران دارد (تنگه هرمز) در حال کم اثر شدن است اما کارتی که آنها دارند (محاصره دریایی) کماکان در دستشان باقی…</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/16838" target="_blank">📅 19:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16837">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">محسن رضایی: صبر ایران حدی دارد
تنگه هرمز تحت مدیریت ایران است. اجازه تداوم محاصره دریایی را نخواهیم داد و تشدید تنش در لبنان هم تحمل نخواهد شد. صبر نیروهای مسلح جمهوری اسلامی ایران حدی دارد.</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/16837" target="_blank">📅 19:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16836">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdabcsrtYtyBENUsFBcYi-gWxHZrg00kphLaEc6ARZsFCtvESUnrcCJyZI1bxNSK0f5wmVW20_kMYRQR2s7eWuwBs3hJQVXhVP2qnJfngh_xZ3afiMfPq4LP5UE2Isp9ab6iTS015vg08Ga-KKc-S2sLB2YJUJWrUmq5JPLAidaQPqLVjYdzu_MshlmxWSwhAodMdoM3mg6twFKHzjHMGBoq6h5oabSCdn56NKcY9nF6uGQzuoYihfiGu00im_vW3L6Uiux3XH6RmPfG9Juc6Q4AgOlodvjU1gbxxaXAu8z-R0uq-v7ecD4QUXQfICdS3ckxJO2t3uegPhvKj9y02A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایده خوبی است بسم الله!</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/16836" target="_blank">📅 18:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16835">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">عراقچی: نقض آتش بس در یک جبهه، نقض آتش‌بس در تمام جبهه‌هاست  آتش‌بس میان ایران و  آمریکا، بدون هیچ ابهامی، آتش‌بسی در تمامی جبهه‌ها، از جمله لبنان، محسوب می‌شود.  نقض این آتش‌بس در هر یک از جبهه‌ها، به منزلۀ نقض آن در تمامی جبهه‌هاست.  آمریکا و اسرائیل مسئول…</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/16835" target="_blank">📅 18:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16834">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">قیمت کنونی ۱۶۹</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/16834" target="_blank">📅 18:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16833">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">با این جهش وحشتناک قیمت نفت در همین یکی دو ساعت، ترامپ مجبور به عقب نشینی است.</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/16833" target="_blank">📅 17:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16832">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خواننده Secret Box از‌ همان روز توافق میدانست که اندوه لبنان خواهدکشت ما را.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/16832" target="_blank">📅 17:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16831">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">خب در توافق بحث پایان جنگ در لبنان هم مطرح شده و لذا میتوان گفت این بندش هیچ وقت اجرا نخواهدشد.</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/16831" target="_blank">📅 17:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16830">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ایران اعلام کرد که آماده بستن کامل تنگه هرمز و تنگه باب‌المندب است اگر اسرائیل حملات به بیروت را متوقف نکند</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/16830" target="_blank">📅 17:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16829">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سخنگوی وزارت خارجه:
ما حق دفاع مشروع در برابر نقض آتش‌بس توسط آمریکا را داریم و امروز هم مبدأ تجاوز به خاک کشور را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/16829" target="_blank">📅 17:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16828">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">عراقچی: نقض آتش بس در یک جبهه، نقض آتش‌بس در تمام جبهه‌هاست
آتش‌بس میان ایران و  آمریکا، بدون هیچ ابهامی، آتش‌بسی در تمامی جبهه‌ها، از جمله لبنان، محسوب می‌شود.
نقض این آتش‌بس در هر یک از جبهه‌ها، به منزلۀ نقض آن در تمامی جبهه‌هاست.
آمریکا و اسرائیل مسئول پیامدهای هرگونه نقض این آتش‌بس خواهند بود.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/16828" target="_blank">📅 15:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16827">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">برکشایر هاتاوی اکنون بیش از هر زمان دیگری در تاریخ خود پول نقد در اختیار دارد</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/16827" target="_blank">📅 14:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16826">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">بنیامین نتانیاهو به همراه وزیر دفاع اسرائیل دستور حمله به ضاحیه بیروت را اعلام کردند و گفته می شود ستونی طولانی و عظیم از خودروهای مردم به سمت مناطق شمالی بیروت و بیرون از آن در حرکت هستند.</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/16826" target="_blank">📅 13:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16825">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">قالیباف:
محاصره دریایی و تشدید جنایات جنگی در لبنان، گواه عدم پایبندی واشنگتن به آتش‌بس است و هر گزینه‌ای بهایی دارد که پرداخت خواهد شد.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/16825" target="_blank">📅 13:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16824">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بنیامین نتانیاهو به همراه وزیر دفاع اسرائیل دستور حمله به ضاحیه بیروت را اعلام کردند و گفته می شود ستونی طولانی و عظیم از خودروهای مردم به سمت مناطق شمالی بیروت و بیرون از آن در حرکت هستند.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/16824" target="_blank">📅 11:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16823">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">️صدای انفجارها در بندرعباس کنترل شده است
صدا‌هایی که دقایقی قبل مردم در سطح شهر بندرعباس شنیدند ناشی از امحای مهمات عمل نکرده است.
روابط عمومی استانداری هرمزگان اعلام کرد: انفجار‌های صورت گرفته کنترل شده است و تا ۷۲ ساعت ادامه دارد و مردم نگران نباشند.
این انفجارهای کنترل شده از دیروز آغاز شده است و تا فردا سه شنبه ادامه دارد.</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/16823" target="_blank">📅 10:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16822">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">این جریان استعفاهای پزشکیان هم مثل خداحافظی های کریم باقری است.
سبحان الله!</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/16822" target="_blank">📅 09:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16821">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">حالا توجه کنید که در همین مدت که آمریکایی ها دهها کشتی تجاری را از تنگه هرمز عبور داده اند،
محاصره دریایی شان را کماکان اعمال میکنند
و این یعنی کارتی که ایران دارد (تنگه هرمز) در حال کم اثر شدن است اما کارتی که آنها دارند (محاصره دریایی) کماکان در دستشان باقی است.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/16821" target="_blank">📅 09:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16820">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ارتش آمریکا به ۷۰ کشتی تجاری کمک کرده تا در ۳ هفته گذشته با خاموش کردن سیستم GPS خود از تنگه هرمز عبور کنند.  به نظرم این رادارهای ما را میزنند تا توان رهگیری اهداف متحرک از سپاه سلب بشود و سپس کشتی ها را خارج می‌کنند.</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/16820" target="_blank">📅 09:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16819">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ:
ایران واقعاً می‌خواهد معامله‌ای انجام دهد و این معامله برای ایالات متحده آمریکا و کسانی که با ما هستند، بسیار خوب خواهد بود.
اما آیا دموکرات‌ها و جمهوری‌خواهان به ظاهر غیر میهن‌پرست درک نمی‌کنند که وقتی سیاستمداران فرصت‌طلب بارها و بارها با سطحی بی‌سابقه به صورت منفی «نق» می‌زنند و می‌گویند که من باید سریع‌تر حرکت کنم، یا کندتر، یا به جنگ بروم، یا به جنگ نروم، یا هر چیز دیگری، برای من بسیار دشوارتر است که به درستی شغلم را انجام دهم و مذاکره کنم؟
فقط بنشینید و آرام باشید، همه چیز در نهایت خوب پیش خواهد رفت - همیشه همینطور بوده است!
رئیس‌جمهور DJT</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/16819" target="_blank">📅 08:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16818">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrM_cHcp1yu7jGlz7KG9htfhXN4MBUJRUvwL7NE-daK-i4AAhZau7sZY-OM6XO4_GRDx2ruV67MUcEjMCXcOMdxhKps96Udw0ZOb_gxlt2m6VQR0n2Gl2htXJW4fSDhYtV-9llKGKEDm9pFN5Zr9ESSFVozX6bdJ8JZvLsZtF3eRwcoXwzuCs30LWk_wBXTSzUjA5ZXee6h0-7nW6y340KDxrL1CfUnyHzb3pl3KHW61hm8YzhvrbHKbAPKc3MHJf2hxmbrNVlnu1TQokQsBs8OD_fHHh-ZDYeSovV4mj84mX2-TX9Lgel6LyxZzAwO1o6lwPlhXRZv4_h63joTfhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات آمریکا به رادارهای ایرانی و پاسخ سپاه   مرکز فرماندهی مرکزی (CENTCOM) اعلام کرد که حملاتی را به عنوان «ضربه‌های دفاع از خود» علیه سایت‌های راداری و فرماندهی در گورک و جزیره قشم انجام داده است.  در پاسخ، نیروی هوافضای سپاه پاسداران پایگاه هوایی که حمله…</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/16818" target="_blank">📅 08:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16817">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPsOTjyCA7-pI6Q1vxCriYD3ck4kQbWiae4WZ5Rvp6DtL09jn2_amL_2Cvf8JsZpnXCSk9qaRi_2hRrQVHLtFuqtTbESPQuVRdpKF01ON3HKAlpJc4Qd8drH-7O8141SkD1MoQDf8wuG-TLwQeUSjM4DdGd4XFqONBNglBaAOZP4KAlMO1QqfjkFw4Po74NdJt8IeWhajN4CCZrmThHt-Lt-xmXVmv4oCt_hcSG87E3Pdzip1zfQ-wUv6vs8HxrTsfNgyKw1JXTt5djMdnlaacM89qJZOtJa5hjTCHE0zf84GzwProR9A9dPY1iAzx-l9xhS-LJaffgAiaFmJtsBcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با این وضعیت به نظرم دوشنبه نفت با گپ مثبت باز بشود</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/16817" target="_blank">📅 08:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16816">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">حملات آمریکا به رادارهای ایرانی و پاسخ
سپاه
مرکز فرماندهی مرکزی (CENTCOM) اعلام کرد که حملاتی را به عنوان «ضربه‌های دفاع از خود» علیه سایت‌های راداری و فرماندهی در گورک و جزیره قشم انجام داده است.
در پاسخ، نیروی هوافضای سپاه پاسداران پایگاه هوایی که حمله آمریکا از آنجا آغاز شده بود را هدف قرار داد و گفت که «اهداف پیش‌بینی شده نابود شدند».
ارتش کویت نیز این وسط از فعالیت‌های پدافند هوایی در منطقه گزارش داد.</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/16816" target="_blank">📅 08:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16815">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">دیسکامبوباتور.pdf</div>
  <div class="tg-doc-extra">200.8 KB</div>
</div>
<a href="https://t.me/SBoxxx/16815" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این تصویر را ترامپ دیروز پست کرده بود.  کلمه discombobulator را پیشتر ترامپ در توصیف سلاح مخفی سری که آمریکا در جریان ربودن مادورو استفاده کرد به کار برده بود و دیروز دوباره گویا به این سلاح اشاره کرده است.  گویا این سلاح به نوعی در مختل کردن کلیه دستگاه های…</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/16815" target="_blank">📅 00:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16814">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kj_TATNgjfE2NwT1oGR9kEdkIq3VcZoE9pIXRgPXmoiP3GM7e1V1LBXYear8zkK-VEdQCrveDfFfWefWsRYLiGrtRAAcZnaXYXP24GLhYfyqzR21M8npsF4_F9DxL-_UBPnWLFNwTE8ZcTveIAwEfrd7CX2j7L0awXpY_wg9l-phyMfS4O5OXjpQzbImybiYRx9C0DASRY5NejQTKQxWPwa5leCo_bRS04y96ShM42EYcoEdx_t1s_IHd24PTA3Z9PSLWZK1Yqwcu8uGCu5gELFcslpY6hzytJSdwCHvi3KDUnpaKpV3Ochelbz32yWQZnu2BMN-98GHIXD39rohdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا در تهران نوعی خرابی وسایل برقی، نوسان جریان برق، ناپایداری نت حس می کنید؟  بله:
👍🏻
خیر:
👎🏻</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/16814" target="_blank">📅 23:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16813">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">آیا در تهران نوعی خرابی وسایل برقی، نوسان جریان برق، ناپایداری نت حس می کنید؟
بله:
👍🏻
خیر:
👎🏻</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/16813" target="_blank">📅 23:43 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16812">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_hGhRlndIMMnEYsDWRTHHF05Ci2-rJAmbt-BX5MK_TwGBAuijOuwmN8wgqwBU0ZJTRiBzJJz45isncA1GAAfJtiCe1UNXOr4SgEJAAtLkcYq2em1SyYqVJhZGmEnHfUKoeuq-8t39Bq0dfMiYUWng_d1eyWu6nIwbpIXRCtbs6PjFcpu4nlK9Zvu9t1GyvE6WIFIujaoNNNbjgIVfOgpYqzeNLVCCQ5AELEySf5imn3uRe2r69nrC0cXlpxEDm2-0uK5O8xxprdmUT_ronQx2YWVJM8Ymeny5OwRfPv3mnRYxymvwnnDyT_ZKx_d1qEVi1O_aZ41xX5_kA0uIotRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت جنگ در جنوب لبنان!
منطقه بنفش تصرفات اخیر ارتش اسرائیل
منطقه سرخ محدوده بمباران ها و تنشهای نظامی</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/16812" target="_blank">📅 20:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16811">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بسیار کار خوبی است و باعث کاهش فشار روی سرورهای پورن هاب می شود.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/16811" target="_blank">📅 20:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16809">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکاخ رسانه</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HP6sJXqv5NqRjDqyBJgeg25zqmvF3vqXcFzIaVqberTBM3JAG1RWJxAE1i1yWIxoKTXkSAgMwh_SYh2797QquzP2QztMgAx3vI7EomokI602YhvJiXi08Ov5tU5uAMHvx5xxZkY5Zqgmor5ec5sf6k5kaLr91m7K0vIWgKrlGvEghJcdnKkoOwHZJdw5fCgHMoOFTkddenTJm6kSUqvMh6PUFIYaLKGnr3xiWf08bLvwIIagTXFKA90wllS9HTROpogkpE5C_dIj_FYanJK_PhKxkDz0EnONHEZ0RYlWnRGxGUkhY8cgx_w6SoE9n8a15xZ-dS8XzlhfkVieZH0QAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZrpaIpq8oEEGI39QQwDkOua17uXbXR7P1fiGLn8CKQMvZ2f39GFNm9JvgxGZpbDCY69HjVyjTKqjcftQfetXHFaCHLAtTyYNfXM_xjCe8RYdb_uzerHEUnCZjo2yIg619LzvXdDHDN-ZSsGPQ4lf54RXgoCKGBtQJXo6l7NatimycBQbYvxWsO5nSfb-6mQpZG4pCQXydbFnujTlR0i3lXLnBtWbc4Q9Nvqb9HcabgIwRjjJbjyGFigR5g8DsYRtTMwIRV1VysbtlG1a9wPZg6QfaZZUNmjSPkDkv_FrZPSxPcJw6c0o3Vty6QYp7OhE7QPMFoj6HGHRaJB7nTs1kA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یک کمپین عجیب در خبرگزاری فارس
گزینه «قطع داوطلبانه دسترسی به اینترنت بین‌الملل» را فعال کنید!
ایجاد کننده کمپین صالح اسکندری از موسسین حزب شریان است
@kakhresaneh</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/16809" target="_blank">📅 20:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16807">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سی ان ان:
ترامپ با آزادسازی هرگونه دارایی ایران در توافق احتمالی مخالفت کرده است.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/16807" target="_blank">📅 18:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16806">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjtIwK-ZVT9tc4HjdWT7eO5ZeGOCdIJGwfPnLBd54dvfMZHQho96k6rlhBw72VVe9r3JSLCGbkn3c4YD_p91nCeqGOM6tCX252XstwFjeuj5_VE6_wItJBchefN4KK3pvblVQXq2pOoHVJ8ko0QVoZbchmzPqsHIrPWib9zGtPWZvmbkrwQvPxZUSLgdiIQ4h7sGeAjWHjCNax6TZW-mGMj6rzmP6ZUu8qlItMNuOluUK_CoM-s9v5pReiD1mq7sCxFWJxibfmcDCSw6BIzkd5lbBGedftYcNAbV5CRo1AYzMc2kSA5SiEn3xmxUO0RL_DFbd4_NAyzun_u5ddIk1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ فراخوان داده به تماشای برنامه امشب مارک لوین که از محافظه کاران بسیار تندروی حامی ادامه جنگ با ایران است و اساساً توافق با ایران را بی معنی می داند.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/16806" target="_blank">📅 18:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16805">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دقیقاً توصیف موج 4 به زبان ژئوپولیتیک.  بدترین سناریوی ممکن برای روح و روان ما و برای رشد طلا و دلار در داخل</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/16805" target="_blank">📅 18:27 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16804">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhjsBC61jR_Qc5JRWplLrIsfjU-FsHP040pzZyEQdKbgl1rN-IJZPy5QyV4yIrcpDaPjlbp7HUJgHHvc4lE4ZzH1X8hJV_NC6dBwo7HNXY7GB2s0D5rc73dWQ9zU3k6EpC0icQakRcpRPlTvWL3P5VpOIhVqB63GY27x_k1PvOA4gML2xkuRn1SWQyxoeoxmAkXL68j1GecW_0_z1IPCZyfEVdd600dua8MJtOPOD77Zt63OPIUc-rbifzm9Vi3YAj0dHfiJqvT8jTl2COxscbHpyE5Bd2UU06mpVkfJgMZWnD-CkGPa5ocH0sYwGqKBOTUGFN3XnFUz4MXzL-zHVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش گاردین، در انگلستان، سه نوجوان مهاجر که به یک دختر ۱۵ ساله و یک دختر ۱۴ ساله تجاوز کردند، جریمه ۲۶ پوند شدند و آزاد شدند.
فعالان حقوق بشر انگلیسی نمی‌فهمند که این چگونه ممکن است، زیرا حتی جریمه پارک غیرقانونی در بریتانیا ۱۳۰ پوند است که پنج برابر بیشتر از مبلغی است که نوجوانان مهاجر پرداخت کرده‌اند</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/16804" target="_blank">📅 18:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16803">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکاخ رسانه</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/696ee3bdc6.mp4?token=DOny0AYRWVNrynmPHv6-OHzCIBQX9GlNbvs647djKjpTpmmd2M5tKQT2ZbH0LsHB4l0DNMy5L30RWEagDkCu9r3GITYr2tWW62RqPURD3hJd_X6r8MjHpsHqd5DuUJ_yNT-58fnuLCwxb6Sv36cVgmu4hX8LVbbRyi_klKUdYdV-hrZGVyYawivhRGAYB-WgNmzuSINKVsO4dQWG3FTJ0TJgbu-bRhuOJ2mciPMuTGe2posyQL2VdrMi9tOCVhR1zznTiM-bdyAXt0GYv2YNZW4r7p7sy8uAzvSBu8kgkErRj1HpeX78yg4LqdBdiOO_TVJXbGMNdAJhAS76doCl0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/696ee3bdc6.mp4?token=DOny0AYRWVNrynmPHv6-OHzCIBQX9GlNbvs647djKjpTpmmd2M5tKQT2ZbH0LsHB4l0DNMy5L30RWEagDkCu9r3GITYr2tWW62RqPURD3hJd_X6r8MjHpsHqd5DuUJ_yNT-58fnuLCwxb6Sv36cVgmu4hX8LVbbRyi_klKUdYdV-hrZGVyYawivhRGAYB-WgNmzuSINKVsO4dQWG3FTJ0TJgbu-bRhuOJ2mciPMuTGe2posyQL2VdrMi9tOCVhR1zznTiM-bdyAXt0GYv2YNZW4r7p7sy8uAzvSBu8kgkErRj1HpeX78yg4LqdBdiOO_TVJXbGMNdAJhAS76doCl0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو سال طول می‌کشد تا به شرایط قبل جنگ برگردیم
💬
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی و مدیریت راهبردی انرژی:
🗣️
آسیب‌های واقعی کمتر از برآوردهای اولیه بود، اما بازگشت به وضعیت پرچالش قبل از جنگ (با ناترازی عمیق‌تر انرژی) یک و نیم تا دو سال زمان می‌برد.
@kakhresaneh</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/16803" target="_blank">📅 17:44 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16802">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">نیروهای سپاه پاسداران ایران به سایت‌های گروه‌های جدایی‌طلب در شمال عراق حمله کردند —رسانه‌های دولتی</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/16802" target="_blank">📅 17:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16801">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTTTSy0wT5NKxiwss5nWvAPQ8Y1aEyryY6YBciB1zP46GqN5IreJJuP3iJnHiXtCz9fVmTYa8iMIBIQKSVC3XpongRh3Gv34-1-n2vuR_3Ij1T-mT4sm1izgF-yVZY_7GbE1QSW2xiQiYBI8ffmTa8DrW7n2urIWlNmAm8dcCr-htwYtKi3ECLyBh7400Hl9n3B0nGCCvkZeypCr3rOhc8frpC41O7r0g3fILkH4bc47OcIu9fggCL4cGefZnprYa564CigwbFX5pcqv9lMyLDiGcKcoXBo-Zl05ZI72kZeUmgv8wB5z5Leew6q5-adtCOFdllXWNX9xibSrHQdyWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو:
«ما قوی‌تر از همیشه بازگشته‌ایم»
او تصرف قلعه بوفورت در لبنان را تبریک گفت و وعده «تغییر چشمگیر» در سیاست نسبت به حزب‌الله داد</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/16801" target="_blank">📅 15:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16800">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">به گفته یکی از افراد مطلع، اسرائیل در طول جنگ، سامانه‌های گنبد آهنین و نیروهای خود را برای دفاع از امارات متحده عربی اعزام کرد و ده‌ها تن از این نیروها همچنان در یک پایگاه نظامی در این کشور خلیج فارس مستقر هستند.   در اوایل آوریل، عربستان سعودی به آمریکا شکایت…</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/16800" target="_blank">📅 14:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16799">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">صداهای شنیده شده در قشم و بندرعباس ناشی از امحای مهمات عمل نکرده از جنگ رمضان است.</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/16799" target="_blank">📅 14:32 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16798">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">صداهای شنیده شده در قشم و بندرعباس ناشی از امحای مهمات عمل نکرده از جنگ رمضان است.</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/16798" target="_blank">📅 14:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16797">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پاکستان به تازگی ۶ کریدور زمینی به ایران افتتاح کرده است.  ۶ مسیر زمینی از کراچی و گوادر مستقیماً به مرز ایران، گبد، تفتان، و چندین نوع دیگر.  کالاهای کشورهای ثالث اکنون می‌توانند تحت نظارت گمرکی از پاکستان به ایران با کامیون ترانزیت شوند.  بیش از ۳۰۰۰ کانتینر…</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/16797" target="_blank">📅 14:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16796">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمو | مطالعات تخصصی آسیای مرکزی</strong></div>
<div class="tg-text">🔵
اختلاف در سازمان کشورها ترک زبان: قزاقستان مخالف تبدیل سازمان کشورهای ترک زبان به یک اتحاد نظامی
⬅️
روزنامه برلینر زایتونگ آلمان می‌نویسد، مسائل ژئوپلیتیکی موجب بروز اختلافی کلیدی در میان کشورهای ترک زبان شده است: برخی از آنها طرفدار ایجاد اتحاد نظامی ترکی هستند، در حالی که برخی دیگر با آن مخالفند. توکایف اصرار دارد که سازمان کشورهای ترک زبان نباید به یک اتحاد نظامی تبدیل شود. در حالی که اردوغان و علی‌اف برای گسترش نفوذ ژئوپلیتیکی و ایجاد یک بلوک نظامی پافشاری می‌کنند.
🔹
قزاقستان از ایده تبدیل سازمان کشورهای ترک زبان به یک اتحاد نظامی تحت یک پروژه ژئوپلیتیکی حمایت نمی‌کند. قاسم جومارت توکایف رئیس جمهور قزاقستان، این موضع را در ۱۵ می در نشست غیررسمی سران کشورها و دولت‌های عضو این سازمان در ترکستان قزاقستان صراحتا اظهار نمود. این در حالی ست که در ماه آوریل، آندری بلوسوف وزیر دفاع روسیه اعلام کرد که مسکو حضور نیروهای خارجی در آسیای مرکزی را نخواهد پذیرفت.
🔹
رئیس جمهور قزاقستان در نشست مذکور گفت: «اخیراً، برخی ایده ایجاد یک اتحاد نظامی را مطرح کرده‌اند. نیات منفی آنها برای ما آشکار است. همچنین مشخص است که اهداف آنها هیچ ارتباطی با صلح ندارد. قزاقستان معتقد است که چنین موضعی باید قویاً رد شود. تقویت وحدت جهان ترک برای ما بسیار مهم و اولویت اصلی است».
🔹
وی اذعان نمود که سازمان کشورهای ترک زبان نه یک پروژه ژئوپلیتیکی است و نه یک سازمان نظامی، بلکه یک پلتفرم منحصر به فرد است که تقویت تجارت، اقتصاد، فناوری‌های پیشرفته، دیجیتالی شدن، فرهنگ و همکاری بین فردی بین کشورهای برادر را ترویج می‌دهد. وی افزود که کشورهای ترک زبان باید در هماهنگی زندگی کنند و با هم توسعه یابند، بدون اینکه از اهداف خود منحرف شوند.»  توکایف همچنین بر اهمیت وحدت کشورهای ترک زبان با توجه به وضعیت ژئوپلیتیکی بین‌المللی بسیار دشوار تأکید کرد.
🔹
پیش از این، آذربایجان پیشنهاد برگزاری رزمایش‌های نظامی مشترک را داده بود. اردوغان که دو روز قبل از اجلاس در یک سفر رسمی وارد قزاقستان شده بود، اغلب در سخنرانی خود به موضوعات ژئوپلیتیک اشاره می‌کرد و تاکید نمود که بحران‌های فلسطین، لبنان، ایران، اوکراین و سایر کشورها لزوم تقویت دفاع ما و گسترش همکاری در بخش صنعتی را نشان داده است. اردوغان همچنین گفت: «همانطور که بحران تنگه هرمز نشان می‌دهد، پروژه‌های حمل و نقلی که جهان ترک را به هم متصل می‌کند، به ویژه مسیر حمل و نقل ترانس-خزر، برای سال‌های آینده اولویت اصلی ما خواهد بود.
🔹
در این نشست علی‌اف نیز به جنبه های ژئوپلیتیکی فعالیت‌های این گروه اشاره می کرد و اظهار داشت: «جهان ترک باید به یکی از مهمترین مراکز ژئوپلیتیکی قرن بیست و یکم تبدیل شود. آذربایجان به تمام تلاش خود برای تقویت سازمان کشورهای ترک ادامه خواهد داد.»
🔹
این در حالی ست که این کشورها در حال تقویت روابط و همکاری های نظامی خود در قالب های دو جانبه و چند جانبه در داخل خود هستند.  در جریان همین اجلاس مشخص شد که آنکارا و آستانه برای ایجاد یک شرکت مشترک برای مونتاژ پهپادهای ANKA ترکیه در قزاقستان توافق کرده‌اند.
آمو | مطالعات تخصصی آسیای مرکزی
@C5Amu</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/16796" target="_blank">📅 13:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16795">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔸
سخنگوی کمیسیون امنیت ملی: برخی اخبار حاکی از موافقت آمریکا با شرایط ایران است</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/16795" target="_blank">📅 13:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16794">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0QZvPjN0J4dVnN_7R3pXaaqucLeCiSo8CLgkM1cjW2FGxlWYbxhw5SGM3PcFpRKhaWNz56Pzv5YgSZSq_xIJ6mbsh1v0XDrFyRlskh78fpZNEkhbBBcEFRxHdp4rnl7uvqwXLfK9a0TcFfmWMErrDMorkvzxULwAReNo0CqNxdKz6r9oUKglxpSiACmZ-8GKTpeer7J5O2dpuBfBm7M_2CiBNBtHuC2kU09HP-rZbtyyMj-7jZZUBdM55Hen-uR1OT3wtOoz-EizCm3FYknfwC7h1nCl7wDAehnMfDEIO3nQYMi9TtC5YGw6S-f-rbFlxH6_cV10DK0R0L1OkP1kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش نیویورک تایمز با استناد به مقامات آمریکایی، ایران نتوانسته است تنگه هرمز را برای ترافیک دریایی بیشتر باز کند، زیرا قادر به یافتن تمام مین‌هایی که در این مسیر پخش کرده نیست و توانایی خنثی کردن آن‌ها را ندارد.  مقامات آمریکایی گفتند که «مسیرهای امن»…</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/16794" target="_blank">📅 12:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16793">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ابرت کیوساکی: خالی بودن ذخایر طلا فورت ناکس باعث فروپاشی اقتصاد آمریکا می‌شود!   رابرت کیوساکی (Robert Kiyosaki)، نویسنده کتاب پرفروش «پدر پولدار، پدر فقیر»، نگرانی خود را درباره اقتصاد آمریکا با طرح احتمال مفقود شدن ذخایر طلای فورت ناکس (Fort Knox) ابراز…</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/16793" target="_blank">📅 08:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16792">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، یک پیشنهاد صلح تجدیدنظر شده با شرایط سخت‌تر به ایران ارسال کرده است - به نقل از چندین مقام آمریکایی در گفتگو با نیویورک تایمز.   این «پیشنهاد جدید و سخت‌تر» با هدف افزایش فشار بر ایران برای پذیرش توافق طراحی شده است</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/16792" target="_blank">📅 08:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16791">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بن‌گویر: حملات به ضاحیه کافی نبوده است
ایتامار بن‌گویر، وزیر امنیت داخلی اسرائیل، اعلام کرد صدها نیروی حزب‌الله در هفته‌های اخیر هدف قرار گرفته‌اند، اما این اقدامات را کافی ندانست.
او خواستار تشدید حملات به منطقه ضاحیه در جنوب بیروت شد و از دولت اسرائیل خواست عملیات گسترده‌تری را علیه این منطقه انجام دهد.
اظهارات بن‌گویر در ادامه مواضع تند او درباره جنگ لبنان مطرح شده و همزمان با افزایش حملات و تنش‌ها در جبهه شمالی اسرائیل بیان شده است.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/16791" target="_blank">📅 08:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16790">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، یک پیشنهاد صلح تجدیدنظر شده با شرایط سخت‌تر به ایران ارسال کرده است - به نقل از چندین مقام آمریکایی در گفتگو با نیویورک تایمز.
این «پیشنهاد جدید و سخت‌تر» با هدف افزایش فشار بر ایران برای پذیرش توافق طراحی شده است</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/16790" target="_blank">📅 08:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16789">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdKmMAMDvR1vdKJFbCvDJKRyOlcEW1AFtelLk9czQpq2AGaU4vFvF8wZavPTRImQwyqs_bIYVz7G8-zY4vmoUFsDgd_ycy1O-i62z_RQ78bajpFEIKJZoSxARpGP4pWrLKVIjMTIN0O3DowpfJ3sR9KjR7izK9N55M6kSx4ovzApEjdeSCtbnXVU8PHhJb8rqmLS0LKOHNueiSSxwalepNGmIgckaFmFnaKzrulfU9ChcDN0rovdRKK6CRj3W72bcACxWMojathbuS1ZtlGGMJf8ETrmuxHAPQxGdZwGfP4ljvfNF8fDcicPCzUhfa_ILAmscnNCoYs2qVdOwoBh7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه دیدگاه موسسه مطالعات جنگ درباره اهمیت راهبردی کنترل تنگه هرمز در دکترین جدید بازدارندگی جمهوری اسلامی:  مقامات ارشد ایرانی در ماه‌های اخیر بار دیگر بر اهمیت راهبردی تنگه هرمز به‌عنوان یکی از اصلی‌ترین ابزارهای قدرت و بازدارندگی جمهوری اسلامی تأکید کرده‌اند.…</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/16789" target="_blank">📅 01:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16788">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بلومبرگ  گزارش داده که حمله موشکی منتسب به ایران در روز شنبه ۳۰ مه (نهم خرداد) به یک پایگاه هوایی در کویت، موجب زخمی شدن تعدادی از نیروهای آمریکایی و وارد آمدن خسارت جدی به دست‌کم دو فروند پهپاد تهاجمی «ام کیو -۹ ریپر» شده است.
بلومبرگ به نقل از فردی مطلع از جزئیات این حمله که به دلیل محرمانه بودن جزئیات نخواست نامی از او برده شود، گزارش داد که پدافند هوایی کویت توانسته است این موشک که از نوع «فاتح-۱۱۰» بوده را رهگیری کند، اما با این وجود، قطعات و آوار ناشی از آن به پایگاه هوایی «علی السالم» برخورد کرده است.
بر اساس این گزارش، حدود پنج نفر شامل نیروهای شرکت‌های پیمانکاری و همچنین نیروهای نظامی دچار جراحات سطحی شده‌اند. همچنین یک فروند پهپاد «ام کیو -۹ ریپر» به طور کامل منهدم شده و دست‌کم یک فروند دیگر به شدت آسیب دیده است. ارزش هر فروند از این پهپادها حدود ۳۰ میلیون دلار برآورد می‌شود.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/16788" target="_blank">📅 00:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16787">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پاریس قهرمان شد…
تبریک به گل شیفته عزیز</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/16787" target="_blank">📅 22:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16786">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">فوری | فرماندهی مرکزی ایالات متحده:   دیروز، ما یک کشتی با پرچم گامبیا را که سعی داشت با حرکت به سمت یک بندر ایرانی، محاصره را بشکند، از کار انداختیم.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/16786" target="_blank">📅 22:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16785">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">یک کشتی تجاری متعلق به دولت ایران توسط ارتش آمریکا با شلیک توقیف شد و نتوانست وارد بنادر ایران شود.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/16785" target="_blank">📅 22:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16784">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">با این وضعیت به نظرم دوشنبه نفت با گپ مثبت باز بشود</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/16784" target="_blank">📅 21:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16783">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ:  محاصره دریایی ایران برداشته شده و اورانیوم غنی شده آن را خارج کرده و نابود می کنیم</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/16783" target="_blank">📅 21:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16782">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نقش پنهان امارات در جنگ شامل ده‌ها حمله به ایران   به گزارش وال استریت ژورنال، امارات متحده عربی ده‌ها حمله هوایی علیه ایران را از روزهای اولیه جنگ آغاز کرد و تا روز پس از اعلام آتش‌بس ادامه داد،  درگیری عمیق‌تری که تاکنون در کمپین هوایی تحت رهبری ایالات متحده…</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/16782" target="_blank">📅 21:31 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16781">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">تا الان فکر می کردم فقط صیغه ساعتی وجود دارد...
سبحان الله؛ ویزای ساعتی را هم دیدیدم در این زندگی اما قهرمانی توفان سرخ آسیا را در همین آسیا نه!</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/16781" target="_blank">📅 19:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16780">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">حالا خوب است به این ویزا ندهند
😂</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/16780" target="_blank">📅 19:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16779">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمو | مطالعات تخصصی آسیای مرکزی</strong></div>
<div class="tg-text">🔵
بحران ذخایر استراتژیک در واشینگتن؛ تاجیکستان کلید حل بن‌بست تسلیحاتی آمریکا در برابر ایران
⬅️
گزارش‌های اخیر رسانه‌های آمریکایی، از جمله
ان‌بی‌سی
نیوز (NBC News)، از نگرانی عمیق مقامات دفاعی این کشور پرده برداشته است. بر اساس این تحلیل‌ها، واشینگتن در صورت تداوم یا تشدید درگیری‌های نظامی با ایران، با چالش جدی تخلیه زرادخانه‌ها روبرو خواهد شد؛ بحرانی که ریشه در کمبود شدید فلز راهبردی «تنگستن» دارد.
🔹
تنگستن که نقشی حیاتی در تولید مهمات سنگین و تجهیزات نفوذکننده نظامی ایفا می‌کند، از سال ۲۰۱۵ به این سو دیگر در داخل خاک آمریکا استخراج نمی‌شود. اکنون با جدی‌تر شدن سناریوهای تقابل نظامی با ایران، پنتاگون برای حفظ توان بازدارندگی و عملیاتی خود، ناچار به جست‌وجوی شتاب‌زده برای یافتن منابع جایگزین شده است.
🔹
در این میان، منطقه آسیای مرکزی به کانون توجه راهبردی واشینگتن تبدیل شده است. پیش از این، دونالد ترامپ شخصاً بر قرارداد تصاحب ۷۰ درصد از سهام میادین بزرگ تنگستن در قزاقستان نظارت داشت، اما به دلیل زمان‌بر بودن بهره‌برداری از این معادن، آمریکا اکنون به دنبال گزینه‌های در دسترس‌تر است.در همین راستا، نگاه‌ها به سمت تاجیکستان معطوف شده است.
🔹
همکاری‌های اخیر دوشنبه با کره جنوبی برای استخراج از معدن «میخورا» با ظرفیت سالانه ۴ هزار تن، به عنوان یک راه تنفس برای صنایع نظامی غرب نگریسته می‌شود. کارشناسان معتقدند تنگستن تاجیکستان می‌تواند به‌طور مستقیم یا با واسطه (از طریق کره جنوبی)، نیازهای مبرم ارتش آمریکا را پوشش دهد.
🔹
هدف نهایی این تحرکات، علاوه بر آمادگی برای سناریوهای جنگی در قبال ایران، قطع وابستگی کامل به چین در زنجیره تأمین مواد اولیه نظامی است. واشینگتن بر این باور است که بدون تأمین پایدار این فلز از منابعی غیر از چین، حفظ پتانسیل رزمی در برابر رقبای منطقه‌ای همچون ایران، در درازمدت غیرممکن خواهد بود.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/16779" target="_blank">📅 18:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16778">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">- مشاور ارشد رهبر عالی ایران، محسن رضایی:
همان‌طور که پیش‌بینی شده بود، رئیس‌جمهور ایالات متحده برای سومین بار به دیپلماسی خیانت کرده است.
با ادامه محاصره دریایی و مطرح کردن مطالبات بیش از حد در مذاکرات، او یک‌بار دیگر ثابت کرده که تمایلی به مذاکره ندارد و اهداف دیگری را دنبال می‌کند.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/16778" target="_blank">📅 17:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16777">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پییت هگست، وزیر دفاع ایالات متحده، هشدار جدی به چین صادر کرد
پییت هگست، وزیر دفاع آمریکا، در نشست امنیتی شانگری-لا در سنگاپور (۳۰ می ۲۰۲۶) سخنرانی کرد و نسبت به تغییر اساسی در رویکرد ایالات متحده به امنیت منطقه‌ای و همکاری با متحدان هشدار داد.
هگست تأکید کرد که امنیت منطقه آسیا-اقیانوس آرام برای مدت طولانی بیش از حد به قدرت نظامی آمریکا وابسته بوده، در حالی که بسیاری از متحدان هزینه‌های دفاعی خود را کاهش داده‌اند.
ایالات متحده از متحدان خود انتظار دارد حداقل
۳.۵ درصد از تولید ناخالص داخلی (GDP)
خود را به امور دفاعی اختصاص دهند.
کشورهایی که هزینه‌های دفاعی خود را افزایش دهند، از مزایایی همچون تسریع فروش تسلیحات، افزایش تبادل اطلاعات و گسترش همکاری‌های صنعتی-دفاعی بهره‌مند خواهند شد.
وی با لحنی قاطع اعلام کرد که متحدان و شرکایی که از پرداخت سهم خود در دفاع جمعی خودداری کنند، با
تغییر روشن و اساسی
در نحوه همکاری و تعامل ایالات متحده مواجه خواهند شد.
هگست چین را به‌عنوان چالش استراتژیک اصلی بلندمدت آمریکا معرفی کرد و بر لزوم ایجاد «تعادل قدرت پایدار» در منطقه تأکید ورزید تا هیچ کشوری نتواند بر همسایگان خود سلطه یابد.
وی از گسترش فعالیت‌های نظامی و رفتارهای تهاجمی چین در منطقه انتقاد کرد.
این سخنرانی نشان‌دهنده سیاست دولت ترامپ مبنی بر فشار بر متحدان برای تقبل بار بیشتر دفاعی و اتخاذ رویکردی قاطع‌تر در قبال جمهوری خلق چین است.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/16777" target="_blank">📅 11:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16776">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">توهم خطرناک جنگ مدرن.pdf</div>
  <div class="tg-doc-extra">328.1 KB</div>
</div>
<a href="https://t.me/SBoxxx/16776" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">مقاله ای طولانی اما بسیار خواندنی از اکونومیست درباره تحولات جنگ مدرن و خصوصاً بحث استفاده روزافزون از پهپادها و ریزپهپادها.
اشارات گسترده ای به جنگ اخیر ایران شده که خواندنی است.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/16776" target="_blank">📅 10:14 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16775">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAt1H20TrZr8pwhxrNJKi1IrFbJ1XOr91ueZFGrTQhA9H-MujyKrCF1Ns5luqDHWveuc3I-AOpaLOwGlXMo5fcyNbo1lf0AeedIinamppigzRQcLjrfKeOu_mGO-y8MD5YS50NjwqzbwBfZZLSh7oSJDlM4fFKFUHATYe7wt9LPzThYoWi5JOp1fo0aIfBNCiAtvvHuPpMCw1efWDWM5R33MRZeSwEJzWVOQpg9EpEGM6q1q2Jud9k-1--47jQtp33hV1vZf4PxqkIyntbUMdFKywE-kD0SOGwkU0BWVXKdNYdH0-nGZkbpWGjXIM6lhq4Z2_o6vjo30wnjEosJ3hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام هدفگیری شناورهای ایرانی در جنوب تنگه هرمز از سوی ارتش آمریکا</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/16775" target="_blank">📅 09:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16774">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">این فاکستانی ها هم فعلاً ظاهراً بلای خاصی بجز 100 مورد حادثه تروریستی که اصولاً در پاکستان از بارش باران فراوان تر است دامنگیرشان نشده اما فی الحال لیندسی گراهام گفته به آنها مشکوک است و الّا و بلّا باید به پیمان ابراهیم بپیوندند!</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/16774" target="_blank">📅 08:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16773">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">پاکستان از 3 سمت تحت فشار است:  — هند ( که همین دیروز اعلام کرد عملیات سیندور را تمام شده نمی داند) — افغانستان (که هر روز شاهد برخوردهای مرزی در مناطق پشتون نشین پاکستان هستیم) — ایالت خودمختار بلوچستان که در آن نیروهای BLA با حمایت مستقیم هند ( و شاید ایران)…</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/16773" target="_blank">📅 08:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16772">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">تحلیل من این است که ترامپ فعلا میخواهد یک دور کوتاه از حملات شدید را انجام داده و سپس اعلام پیروزی و پایان جنگ کند تا در آستانه جام جهانی، کمتر زیر فشار افکار عمومی باشد.  اما جنگ اصلی برای چند ماه بعد خواهدبود.  در واقع این جنگ کوتاه را می‌توان یک موج B درنظر…</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/16772" target="_blank">📅 07:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16767">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نیویورک تایمز:  بحث رئیس‌جمهور ترامپ در اتاق وضعیت نزدیک به دو ساعت طول کشید، اما او به توافق در مورد یک توافق جدید با ایران نرسید، طبق گفته یک مقام ارشد دولت که با شرط ناشناس بودن برای بحث در مورد مباحثات داخلی صحبت کرد.   دولت احساس می‌کند که به رسیدن به…</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/16767" target="_blank">📅 22:30 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16766">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نیویورک تایمز:
بحث رئیس‌جمهور ترامپ در اتاق وضعیت نزدیک به دو ساعت طول کشید، اما او به توافق در مورد یک توافق جدید با ایران نرسید، طبق گفته یک مقام ارشد دولت که با شرط ناشناس بودن برای بحث در مورد مباحثات داخلی صحبت کرد.
دولت احساس می‌کند که به رسیدن به یک توافق نزدیک است، اما سایر مسائل همچنان حل نشده باقی مانده‌اند، به ویژه آزادسازی وجوه مسدود شده ایران</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/16766" target="_blank">📅 22:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16765">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">تو شیر پیل افکنی !
بزن که خوب میزنی !</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/16765" target="_blank">📅 22:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16764">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">تحلیل استاد خانعلی زاده از توافق ایران با آمریکا!</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/16764" target="_blank">📅 22:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16763">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vt07fdmLQ6_jm_I2-Mz8sMACvaWb_TZo2NAysq02wXHUufCgfyvC3aqN_fmkFeHq8y7BAXmaS74r5XgCZ8r7lEd_na3ko8Ig-hraeFLZw45UTwoLaSunbt9TU6H0diVrXvprIuAElHZsRI7rtwkYy1TNz31FE189-kQSnof4qQkYSNUNI4HCw7Bb5x-0RTBgYOhnch-1F8Hz3SSNJBqNFBEvCV1m9AXUx4KkAKUmZV0ZF5yDpSr-9WReK86VTJs_FjGDP-8qCsxwuRkw1ori5lCPzrJpEKBZeThLNNMFemmR8BOz_Gggn8qf_g1vLMMg1CQHWolRp1DBm0V-kvb4vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحلیل استاد خانعلی زاده از توافق ایران با آمریکا!</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/16763" target="_blank">📅 22:17 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16762">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">نقش پنهان امارات در جنگ شامل ده‌ها حمله به ایران
به گزارش وال استریت ژورنال، امارات متحده عربی ده‌ها حمله هوایی علیه ایران را از روزهای اولیه جنگ آغاز کرد و تا روز پس از اعلام آتش‌بس ادامه داد،
درگیری عمیق‌تری که تاکنون در کمپین هوایی تحت رهبری ایالات متحده و اسرائیل شناخته نشده بود.
محدوده این حملات شواهد بیشتری از تمایل فزاینده این کشور به محافظت از آنچه به عنوان منافع استراتژیک خود می‌بیند ارائه می‌دهد و آن را از برخی از همسایگان خود در منطقه خلیج فارس متمایز می‌کند که رویکرد بسیار محتاطانه‌تری نسبت به تهدید از سوی ایران اتخاذ کرده‌اند.
این حملات با هماهنگی ایالات متحده و اسرائیل انجام شد که هر دو اطلاعاتی را فراهم کردند، افراد گفتند.
اهداف شامل جزایر قشم و ابوموسی در تنگه هرمز؛ بندرعباس، پالایشگاه نفت در جزیره لاروان در خلیج فارس و مجتمع پتروشیمی عسلویه بود‌ه است.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/16762" target="_blank">📅 22:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16761">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">فعال شدن پدافند در قشم!</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/16761" target="_blank">📅 22:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16760">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترامپ:  محاصره دریایی ایران برداشته شده و اورانیوم غنی شده آن را خارج کرده و نابود می کنیم</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/16760" target="_blank">📅 18:30 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16759">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ:
محاصره دریایی ایران برداشته شده و اورانیوم غنی شده آن را خارج کرده و نابود می کنیم</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/16759" target="_blank">📅 18:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16758">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-text">کمیته امنیت ملی مجلس ایران:
قصد نداریم اورانیوم غنی‌شده را به کشور ثالث منتقل کنیم اما شاید آنرا به کشور رابع ارسال کنیم.
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/16758" target="_blank">📅 15:58 · 08 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
