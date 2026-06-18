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
<img src="https://cdn4.telesco.pe/file/sFw0xdcMFxYsODGSTi_kFLM-1bLwCpBRYV3o0IaNuoyo4UTvWHsF4qzm17hzM1oeUSBtPvUiF2mJNqqfqNkdEReWeDLg69-tDp3UgKLs_x7uEEJmiJ8OlYD7UtA3VhdRIxfUN9YRYNPuIhs4ysvuCUbk2C4QcgCjkm9nVWLkKs7Ew0ROxoixfcFesBxDVMFwBeQUUa9xx1FU9lg3MYnn0rjHcM-F_Nx5D_iOWvW4DPog3s5w3ZYk4EDMbJ56Arv9rgF-CaxEi18Hr89rTLE9cPZR8_X7_x9UZ_MaUHMJ9BU58wVvNXz_GNzxQVDjH7Gp2umCLwCx6bCTEVbv9baR5g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 14:37:40</div>
<hr>

<div class="tg-post" id="msg-133794">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEpHgYdVe79BLVG6LYZaU7W1KZdfvkE4WVJSil2Eos8rZiexRKeo7QY1DthhEKlRsRvDe7UvVgB60wptaI2gTVArNZyTs2eKa0LV3aQO8UU9wP9Tn_d5yDSzT1zTbjaCgzuMmqPgcg6wRs2oDjbhGWJXDo40qTDnkpF8CBXkAqXRmNuHnUNFW-uLdtRM9rgSKra8sj3ptwy2gycm-6JWkd7QEcpMMs4VNp0ZnMCxD-d8bXh2vbTbM-Mvg6FWRcFZxiEYIhzUIKp-tpgALn4CcPKZU_-l_SLHEwWiKfp-3vg8Ew7K-TQ6wpNDQ4Lr0KBasZ6m_C8fIJMMn_wXy8Cl9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
⚽️
گروه B جام‌جهانی ۲۰۲۶
[
سوئیس
🇨🇭
🆚
🇧🇦
بوسنی
]
⏰
پنجشنبه ساعت ۲۲:۳۰
🏟
استادیوم
سوفای
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 399 · <a href="https://t.me/SorkhTimes/133794" target="_blank">📅 14:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133793">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgXXF3XQ7TcYd_cVCEnMwGg0gK8a1v7u-X1ivzaXQT2ZyiscIxTpv7vcSBih-oqJ6DEe2AdBmRvxrKQx1Dg6ZB8Ec5UiY0u6mWbvd2ofArZeV1uMREmZU-TJ816Z7TUgbSArtuw2bRPw_F1KEY-G4FYb3erlVn2qmjjswajn_bRUeEwLg8Jv0E7jf1PyRK_vpc4bQOxa9nfQSKiY29Ld8SlcGspMNaOFG8O9_sZqh9Bp_chmvhyUNV3SKr6ibmdmdwHQDQcUVtNrkstpDDtOV2d2gsI2tGdY34O-q-HzBXPGUVkzjVyAzQoyVvHMr0v93YiPzyx6Mql2MbnrVgTrsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
تصاویری از تمرین سبک تیم ملی در هتل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/SorkhTimes/133793" target="_blank">📅 13:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133792">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
دراگان اسکوچیچ به عنوان سرمربی جدید باشگاه پرسپولیس انتخاب شد. دو بازی بعدی، بازی‌های آخر اوسمار ویرا بر روی نیمکت پرسپولیس خواهد بود!
❌
خبرگزاری فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/SorkhTimes/133792" target="_blank">📅 13:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133791">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
ایرنا خبرداد؛با تصمیم هیات مدیره و بانک شهر اوسمار از پرسپولیس جدا و اسکوچیچ جانشین وی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/SorkhTimes/133791" target="_blank">📅 13:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133790">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
❌
تیوی بیفوما وارد تهران شد
🔻
تیوی بیفوما، امروز (دوشنبه) و لحظاتی قبل از مرز هوایی فرودگاه امام(ره) به تهران رسید تا از فردا به جمع سرخپوشان بپیوندد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SorkhTimes/133790" target="_blank">📅 11:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133789">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">⭕️
⭕️
⭕️
🚨
🚨
🚨
🚨
🚨
دراگان اسکوچیچ سرمربی پرسپولیس شد/ایرنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/SorkhTimes/133789" target="_blank">📅 11:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133788">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❗️
اسکوچیچ با پرسپولیس به توافق کامل رسید و پیش‌نویس هم امضا شده. او به همراه خداداد عزیزی رونمایی خواهد شد؟///ایرنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SorkhTimes/133788" target="_blank">📅 11:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133787">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItZKtpPYYVGEep6NgNOXpmAja9yNDMOazECxKt05N8GgjRNflZUtpekiRyKbmJBOgc3uxUzrybuIVf9jimPtu5hYsvIkp8D_wcBFboEIzwn2hNIggQis1NiCZ9XwPL0sGVWsz9rzopxpoBOaX6OyKtYJvADqOo_1I6mWbYDILemWLgTiV8Zj4k2t1Gl-jR49COOY_3pvJ4ynp3zq42mtmP8Jho2rTR83TVbza-5XYeo_jLCWSqlGcytRhITOAuoLLpjp0HAv8e9Hg82OZAa7zXFvh2kPxFuLCq_Ddh0h4n1xxKQRD-aqSz8DynzUpPv3NJrHXbBqGT75EP4XsZtYLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
اسکوچیچ با پرسپولیس به توافق کامل رسید و پیش‌نویس هم امضا شده. او به همراه خداداد عزیزی رونمایی خواهد شد؟
///ایرنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SorkhTimes/133787" target="_blank">📅 11:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133786">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtbaTUjxqZLZvMmJGRCqAvfAaPla1tAV2U-eO2nTLNk7GhIzVUODRMLkNhMuHikEqqnKkKyffpQRhBbaNlKxl0FUTzR2ZORcitD2kbPS88mOJF294F8V3c2ICyx24gFNxZNsWfqI_ul0CXO9YhptWGZsw8uLvOcK1tBJ04W44vVhu0_NMy2yMKpMhPXM2btg68Eye1DcJZVFqIkwsE9hzv4zyOP2gEvL1P3mxjQ0BXJ_4WUZp5uQJACZPF1RFHMr0i5FgDC4v_0NMDnp4MDrJxRPxU4pyTo2uLWRo4_mhOnbW7qECBC1wVY6-ySr7iYLbkC7pd6D-RjvxXacV9F6_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌رده‌بندی12گروه رقابت‌های جام جهانی در پایان هفته نخست؛ از امشب هفته دوم شروع میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SorkhTimes/133786" target="_blank">📅 11:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133785">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✅
رگی لوشکیا، بازیکن تیم تراکتور ایران به الظفره امارات پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SorkhTimes/133785" target="_blank">📅 11:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133784">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
سپاهان و تراکتور دارن پشت پرده می بندن که آریا یوسفی و لیموچی به پرسپولیس نیان!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SorkhTimes/133784" target="_blank">📅 11:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133783">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e84f37be82.mp4?token=hc2AKYNVgEgIAJCbhOOs2IxlfcPu981WlsfypgqMXXoCG1AaIQhzCApjrBWEu7Z4n1zpiU65m2ICATyT-GzVlRDOkAGRvADQS5oha0uudQhW3DcKLwyt2PhEFDbOflz4ys7krGPw5SfMFuPahNcJEgqqtYJqTBHdsfcUTS7XdXQ5NCySjrufZziV8h8pDLKj3MPZENXyK0CVYnagCaysO2b_kWtncesBoq6LZeYINnpeJQ2ThVhPucwXxP8rwR4fe6YNetzy0iA1fVUTSH3pmRfPNTZ7wCdXEjGJHgVfNfUixwihk8u2lh7u8vrm18X0NxKNhusOM_bDg6-jEhM68A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e84f37be82.mp4?token=hc2AKYNVgEgIAJCbhOOs2IxlfcPu981WlsfypgqMXXoCG1AaIQhzCApjrBWEu7Z4n1zpiU65m2ICATyT-GzVlRDOkAGRvADQS5oha0uudQhW3DcKLwyt2PhEFDbOflz4ys7krGPw5SfMFuPahNcJEgqqtYJqTBHdsfcUTS7XdXQ5NCySjrufZziV8h8pDLKj3MPZENXyK0CVYnagCaysO2b_kWtncesBoq6LZeYINnpeJQ2ThVhPucwXxP8rwR4fe6YNetzy0iA1fVUTSH3pmRfPNTZ7wCdXEjGJHgVfNfUixwihk8u2lh7u8vrm18X0NxKNhusOM_bDg6-jEhM68A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
شادی کارلوس کی‌روش پس از پیروزی غنا مقابل پاناما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SorkhTimes/133783" target="_blank">📅 10:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133782">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">💬
اوسمار سرمربی پرسپولیس: مدیران پرسپولیس کارشان را به خوبی انجام می دهند و به ما کمک می کنند/  دعوت امیرحسین محمودی به تیم ملی؟ ج اگر چه در لیست نهایی تیم ملی قرار نگرفت اما حضور در کنار تیم هم تجربه خوبی برای اوست.
✅
مارکو باکیچ ، بیفوما و دنیل گرا نفرات…</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SorkhTimes/133782" target="_blank">📅 10:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133781">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✅
امضای پزشکیان و ترامپ در کنار هم رو قرارداد توافق
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/133781" target="_blank">📅 08:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133780">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cixMcfShgeppm8nSdz8uEQT1jCAutUZzx2lKu-gaRhRQ2P497Dj3D2ZTbTHgdPQnq70QhrxVxguNP1N7y419xhFELRrC9rc9_lFMzTCEGufgVBV_gislNOSz9pDZmoxmxsJ7pkErfIe0DHl6WdtA-qd6z1C6a7zilEeAMnOLdmfO33kneNByIS8q2T8dI-qdtEEOZmPykN6kYxmVwIGqhm3liAiwK1P3hRNwPyf2GI5y80vFtkhO-OK-9-ex7dgC6O5T6_hcwAxK8pk6tCL6dN7q8r9m0dP5t2_7jKeNG1yzJUhdMcFfFKzj9YFa1M8LKAQLQevmLeu5_h4AyvyfVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
امضای پزشکیان و ترامپ در کنار هم رو قرارداد توافق
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/133780" target="_blank">📅 08:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133779">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/14ae173143.mp4?token=Q0-5gTAaw623ERty2SnmZCyJzNHf3u5IFwUz4CdOB-A7JS3gw6GSxj5Z2LtIlaDf8MloL6sOkVhHry51Su482mZSpt7NIBf91ggqY9N6YWQk_wIg1hSxTI2moDr78bIC831JhdWuAFAstbIjCXwsEBn8qRGhk1EEf3RB1I8J0J3FyDHG5x4EfjRzcK8k3hvz3qG5-H7lDwaDlMXpoapEj00NzeRcc92vhopiyQg9la04C3v0nxI_kn4J8NBJ0hGH-a7YtUrKeIMVeVp7VwOsR79xaok4Vs6TwKxxx6EZBEhqBy5m3bNwUsz_KZ_5ymE0B_i345B1p8bl53T4YAcsEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/14ae173143.mp4?token=Q0-5gTAaw623ERty2SnmZCyJzNHf3u5IFwUz4CdOB-A7JS3gw6GSxj5Z2LtIlaDf8MloL6sOkVhHry51Su482mZSpt7NIBf91ggqY9N6YWQk_wIg1hSxTI2moDr78bIC831JhdWuAFAstbIjCXwsEBn8qRGhk1EEf3RB1I8J0J3FyDHG5x4EfjRzcK8k3hvz3qG5-H7lDwaDlMXpoapEj00NzeRcc92vhopiyQg9la04C3v0nxI_kn4J8NBJ0hGH-a7YtUrKeIMVeVp7VwOsR79xaok4Vs6TwKxxx6EZBEhqBy5m3bNwUsz_KZ_5ymE0B_i345B1p8bl53T4YAcsEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
#مهم
| لحظه امضای نسخه فارسی یادداشت تفاهم ایران و آمریکا توسط دونالد ترامپ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/133779" target="_blank">📅 08:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133778">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔹
حیدری عضو هیئت‌رئیسه فدراسیون:
تورنومنت ۳ جانبه لازم‌الاجراست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/133778" target="_blank">📅 08:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133777">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJVmU--Hle9oa1tc4lDkMcbj95lQaG6ZypkXhA-ZwO5FwCU5qShTozNXni1hAtDV4G8OxPWkMSm3rUnQj9s1P1ihNgC55HCaPXMZXA_UobE_Q_gCl2W7XTbvJFB6Qtd4JCBzKMB-tgHZcj7zO88l0BRH6pqH11B7af8OoFk-imgW-7R_9nvhm8SbEDbF-W8uwvtSTuLt9JtIC3mnxqZmsJYXOevkcQyolNQV0ipEjkyZz-4dZj_qut_xJpsQ7MVsZP8j8krrD4zrSy-cxDpY58WBQHjbd19vAVsjbpDq-GaJojGUXgJu0eHXFQ9MGK4sWdzmFauTGsEnUJOjb8mdtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
⚽️
گروه K جام‌جهانی ۲۰۲۶
[
ازبکستان
🇺🇿
🆚
🇨🇴
کلمبیا
]
⏰
بامداد پنجشنبه ساعت ۰۵:۳۰
🏟
استادیوم
آزتکا
مکزیکوسیتی
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/133777" target="_blank">📅 02:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133776">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPulseGate</strong></div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
یک ماهه
25 گیگ 220T کاربر نامحدود
30 گیگ 280T کاربر نامحدود
35 گیگ 320T کاربر نامحدود
55 گیگ 420T کاربر نامحدود
100 گیگ 600T کاربر نامحدود
دوماهه
50 گیگ
380T تومن کاربر نامحدود
70 گیگ 450T تومن کاربر نامحدود
150 گیگ 700T تومن کاربر نامحدود
200 گیگ 750T تومن کاربر نامحدود
سه ماهه:
120 گیگ 680T تومن کاربر نامحدود
160 گیگ 730T تومن کاربر نامحدود
230 گیگ 800T تومن کاربر نامحدود
320 گیگ 950T تومن کاربر نامحدود
400 گیگ 1.1T تومن کاربر نامحدود
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/133776" target="_blank">📅 01:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133774">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🟦
🟦
فوری و رسمی/تفاهم نامه توسط ترامپ و پزشکیان امضا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/133774" target="_blank">📅 01:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133773">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">⭕️
🚨
سخنگوی وزارت خارجه: متن تفاهمنامه ایران و آمریکا الان رسماً نهایی شده است چرا که دو طرف آن را امضا کرده‌اند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SorkhTimes/133773" target="_blank">📅 01:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133772">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">⭕️
🚨
سخنگوی وزارت خارجه: متن تفاهمنامه ایران و آمریکا الان رسماً نهایی شده است چرا که دو طرف آن را امضا کرده‌اند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/133772" target="_blank">📅 01:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133771">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل اول انگلیس به کرواسی توسط هری کین (P12)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/133771" target="_blank">📅 00:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133770">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">#نظر_شخصی
✅
خیلی ها از من میپرسن تو موافق موندن اوسماری یا اومدن اسکوچیچ هستی، من حقیقتا جفتشونو دزد و دلال میبینم
✅
اوسمار که فیلمش در اومد رسما و سه تا دلال دورش هستن که با اینا کار میکنه که باعث فساد و انحصار شده تو تیم
✅
اسکوچیچ رو با قاطعیت نمیتونم بگم…</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/133770" target="_blank">📅 00:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133769">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">#نظر_شخصی
✅
خیلی ها از من میپرسن تو موافق موندن اوسماری یا اومدن اسکوچیچ هستی، من حقیقتا جفتشونو دزد و دلال میبینم
✅
اوسمار که فیلمش در اومد رسما و سه تا دلال دورش هستن که با اینا کار میکنه که باعث فساد و انحصار شده تو تیم
✅
اسکوچیچ رو با قاطعیت نمیتونم بگم…</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/133769" target="_blank">📅 00:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133768">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✅
درسته با اسکوچیچ چند روزه صحبت شده ولی اصرار از طرف بانک شهر و شخص خداداد عزیزی بوده، و فعلا نه توافقی شده و نه تصمیم قطعی ای گرفته شده.
➖
آقایون دوست دارن زود به استقبال اخبار برن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/133768" target="_blank">📅 00:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133767">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🏅
مرتضی پورعلی گنجی، مدافع پرسپولیس: پرسپولیس در یکی دو سال اخیر با چالش هایی روبرو شد
⏺
بازی نکردن در ورزشگاه آزادی به ما ضربه زد. از وقتی آزادی را از پرسپولیس گرفتند به مشکل خوردیم. هر وقت در ورزشگاه آزادی برگزار کردیم به سمت قهرمانی رفتیم. بازی های فصل قبل…</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/133767" target="_blank">📅 23:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133766">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a6d45ae17.mp4?token=bfyIrSYSqRoD9amx_28D-QIGQzblrZ122EOSDCmpMYcTA6eTM4uDW6golNCXDDJkFmPT4nPMWI4aLwEKHP3RlZjSgSNOkCc65BOEQ5NzUui7GkgQT1WKDXUbRdvXUa5ShwbtsHS-DLyZOsOH2abpVeluMVuTuZhrISrlixFD3iiPLllBzhK1boO0a6bVFs6UZ3-yI_8i2oRoW1C4cL4IF_FTCM3WLArq7eNs9xSqbHYZFAJaILwuvWI1CHzp0744or461gF-BqiRDqL2sONYtpeS0zLI9gZYCbKsJwFOKVgxQKO4Nru3oe3QGypyuIZLo4Mj4pblZ2lOVhpatj3cqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a6d45ae17.mp4?token=bfyIrSYSqRoD9amx_28D-QIGQzblrZ122EOSDCmpMYcTA6eTM4uDW6golNCXDDJkFmPT4nPMWI4aLwEKHP3RlZjSgSNOkCc65BOEQ5NzUui7GkgQT1WKDXUbRdvXUa5ShwbtsHS-DLyZOsOH2abpVeluMVuTuZhrISrlixFD3iiPLllBzhK1boO0a6bVFs6UZ3-yI_8i2oRoW1C4cL4IF_FTCM3WLArq7eNs9xSqbHYZFAJaILwuvWI1CHzp0744or461gF-BqiRDqL2sONYtpeS0zLI9gZYCbKsJwFOKVgxQKO4Nru3oe3QGypyuIZLo4Mj4pblZ2lOVhpatj3cqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل اول انگلیس به کرواسی توسط هری کین (P12)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/133766" target="_blank">📅 23:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133765">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQdQKWoV7Z_m1BwcisECk5_Z9DTSE1CP0Z8sxFOFMxzMBTzggwgOS2V335MkLqKhQd1nCxOmFISptwq3MTE_H9jv0sbKbvexZBGmKGdoFVqkdTREG6bielf-JJvBlI8ZXAlmnzY7QH2bYsp0Fyw8FfVu5DgNOIddkNI4gkaKkLVt59W_03At09HnXYGSdFKjwIzQjNAbWc1ZTNVRAQ_wCQF3LJwuofwVLAS0n-vLGWhq3gT8D-l6EqmBux9H6s7nx2UFP-sRIT89ju03SVioAkfmM79Z8gSgVkCRrCzh7THoreE2ZQodSg98QXRQDwePX7sxeaU_ZKSqagUkxGHJBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
سپاهان به مشکل مالی خورده و داره قرارداد باریکناشو کم میکنه
✅
طبق اعلام خودشون آرش رضاوند و میلاد زکی پور با کسر قراردادشون موندنی شدن اما محمد دانشگر حاضر به کاهش قرارداد نشد و جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/133765" target="_blank">📅 23:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133764">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
دوستان به شایعاتی که توسط قدوسی در رابطه با اوسمار منتشر میشه توجهی نکنید،این عزیز دوست گرمابه گلستان ایجنت اوسمار هستن و تمامی مطالب شون خط دهی شدست تو هوادار رو به جون هم بندازن
🔻
اوسمار از ابتدا قراردادش ۱+۱ بوده و چیز تازه ای نیست اقایون احساس خطر کردن…</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/133764" target="_blank">📅 22:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133763">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
دوستان به شایعاتی که توسط قدوسی در رابطه با اوسمار منتشر میشه توجهی نکنید،این عزیز دوست گرمابه گلستان ایجنت اوسمار هستن و تمامی مطالب شون خط دهی شدست تو هوادار رو به جون هم بندازن
🔻
اوسمار از ابتدا قراردادش ۱+۱ بوده و چیز تازه ای نیست اقایون احساس خطر کردن…</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/133763" target="_blank">📅 22:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133761">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
دوستان به شایعاتی که توسط قدوسی در رابطه با اوسمار منتشر میشه توجهی نکنید،این عزیز دوست گرمابه گلستان ایجنت اوسمار هستن و تمامی مطالب شون خط دهی شدست تو هوادار رو به جون هم بندازن
🔻
اوسمار از ابتدا قراردادش ۱+۱ بوده و چیز تازه ای نیست اقایون احساس خطر کردن که نون دونی شون و دلالی هاشون به خطر بیوفته دارن یارکشی میکنن تا به هر ضرب زوری مربی که قراردادش بوده سال اول تو پرسپولیس ۲۰۰-۲۵۰ هزار دلار رو الان با ۱.۷ میلیون دلار حفظ بکنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/133761" target="_blank">📅 22:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133760">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fwrfs4Nt-YVCc6C4cQhgNhpjnhoGogLqRoWYhHoyCkJPFnyxoRvf_qOuQxUBzAwJenEgDZFHLblWFmKvkmasdpblg0c1CHYZXq5C0c3yHe7naGYTZezxUWCOify3kGdqO-T8BEcvkRiLsifTVC3rYDw4twKa68GRRZOFNwobFHIKOs2Tylnl84DAZ-ZT_U6Zg7vD2lqAyItXbdkDh2pfGRNv1bILAUPoAeF1QY4dbLPyiEW1qkaSNjHYSian-tTMUuWeq3I0JM6amTyGW3sRSyqlKPgCrQpTK_yrEWyk-y3Vk1sVuzTvFHbDIbsiwnOW_TkEYQQqYQg7y5AWlnMNlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
شبکه خبر| انتشار متن تفاهم‌نامه ایران و آمریکا تا دقایقی دیگر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/133760" target="_blank">📅 22:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133759">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❗️
😂
اولین گل تاریخ تیم ملی کنگو تو جام جهانی زده شد به پرتغال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/133759" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133757">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔻
🔻
🔻
فرشید حقیری :
⬜️
⬜️
بانک شهر تصمیم گرفته برای فصل بعد یه تیم قوی ببندد و امیدوارم در حد حرف نباشه. پیش قرارداد برای اسکوچیچ ارسال شده و تا شنبه نهایی میشه. خیلی ها از این موضوع ترسیدن که نتونن به پرسپولیس بیان یا نتونن تو تیم بمونن.
🔴
🔴
اوسمار برای فصل بعد…</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/133757" target="_blank">📅 22:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133756">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🟨
پرسپولیس با چنتا از جوونای تاپ فوتبال ایران مذاکرات مثبتی داشته/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/133756" target="_blank">📅 22:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133755">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✅
ترامپ:
🔸
این یک یادداشت تفاهم است. اگر در ۶۰ روز انجام نشود، اشکالی ندارد، ما دوباره به بمباران بازمی‌گردیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/133755" target="_blank">📅 22:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133754">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔻
🔻
🔻
فرشید حقیری :
⬜️
⬜️
بانک شهر تصمیم گرفته برای فصل بعد یه تیم قوی ببندد و امیدوارم در حد حرف نباشه. پیش قرارداد برای اسکوچیچ ارسال شده و تا شنبه نهایی میشه. خیلی ها از این موضوع ترسیدن که نتونن به پرسپولیس بیان یا نتونن تو تیم بمونن.
🔴
🔴
اوسمار برای فصل بعد…</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/133754" target="_blank">📅 22:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133753">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
❌
گفته می شود په په لوسادا مربی اسپانیایی پرسپولیس اعلام کرده خانواده اش تا زمانی که جنگ در ایران تموم نشه اجازه نمیدن به ایران بیاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/133753" target="_blank">📅 21:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133752">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
بررسی داده‌های سامانه‌های پایش اینترنت از جمله رادار کلودفلر، نت بلاکس و رادار ابرآروان، نشان می‌دهد که اینترنت ایران در حال حاضر در وضعیت پایدار قرار دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/133752" target="_blank">📅 21:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133751">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
کریس رونالدو کاپیتان 41 ساله پرتغال : من میتوانم چهار سال‌ دیگر بازی کنم و در جام جهانی 2030 نیز حضور داشته‌ باشم. حالا حالا ها برنامه ای برای خداحافظی از دنیای فوتبال ندارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/133751" target="_blank">📅 21:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133750">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔸
🔸
🔸
🔸
ایران ورزشی طی یه خبری مدعی که شد مهدی ترابی و مهدی هاشم نژاد در استانه پیوستن به پرسپولیس قرار دارن
☝️
☝️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/133750" target="_blank">📅 21:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133749">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🟨
🟨
فوووووووووری
⬛️
اوسمار ویه را به زودی از پرسپولیس شکایت خواهد کرد/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/133749" target="_blank">📅 21:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133748">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❗️
❗️
فرشید حقیری: اسکوچیچ‌ ترکیه ست و به‌ زودی با امضا قرارداد میاد پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/133748" target="_blank">📅 21:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133747">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔻
🔻
🔻
فرشید حقیری :
⬜️
⬜️
بانک شهر تصمیم گرفته برای فصل بعد یه تیم قوی ببندد و امیدوارم در حد حرف نباشه. پیش قرارداد برای اسکوچیچ ارسال شده و تا شنبه نهایی میشه. خیلی ها از این موضوع ترسیدن که نتونن به پرسپولیس بیان یا نتونن تو تیم بمونن.
🔴
🔴
اوسمار برای فصل بعد…</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/133747" target="_blank">📅 21:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133746">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
فوووووووووووری
🔴
فرشید حقیری: قرارداد اسکوچیچ با بانک شهر شنبه امضا خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/133746" target="_blank">📅 21:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133745">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
#فوووووووووری
🔴
فرشید حقیری: پیش قرارداد برای اسکوچیچ فرستاده شده و به زودی امضا میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/133745" target="_blank">📅 21:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133744">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
❌
فرشید حقیری : بانک شهر تمام سهام سایپا رو خرید، از کارخونه بگیر تا تیم فوتبالش
✅
احتمالا با توجه به این موضوع پرسپولیس ب که سال بعد قراره تو لیگ یک شرکت کنه، جایگزین سایپا میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/133744" target="_blank">📅 21:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133743">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFtmegdvQCKEiFvRnyoAKnylLHCBRWT96xH8IzALublk4fCarizzXObHswVjR6K8cOR2StjMO8GR5TB3KydxYEkqJYh2X_HghT_Wkf_ObxjE1TE62-VsM-WfOCkYglvRUAUizQXPz0KtKH8rHzXoSIIzfl1DDf2km2XtTMghQwNtFedirWL-dWcgUbN4TxvcPD9O1vA8Aw3csYaGgo8a5pffZCXfSlQ9xOiDJ_0BvS6tHkLRIaR3XSjITP7FL-cpEqNUa7oHy9n1SvrYeg_FAKWlFJ-QeRnw1hp_HFqMQL2kDIcs4igQIn82m3_i_OTHIJ17ykTIdup6MmRQGG03fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🌍
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
🏆
گروه L جام‌جهانی ۲۰۲۶
[
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🆚
🇭🇷
کرواسی
]
⏰
چهارشنبه ساعت ۲۳:۳۰
🏟
استادیوم
دالاس
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/133743" target="_blank">📅 20:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133742">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❗️
ترامپ: ما موظف نیستیم چیزی به ایران بدهیم، اما ممکن است برخی بخواهند آنجا سرمایه‌گذاری کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SorkhTimes/133742" target="_blank">📅 20:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133741">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❗️
#فوری | ترامپ:
🔻
توافق با ایران فردا یا پس فردا امضا می شود‌‌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/133741" target="_blank">📅 20:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133740">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U3RIzRh8IvkmyTxribkzF8S1M1vsugegozsUWksEd17ZV_FFSEtoNQy1BzC-r37PW6yWok5HzYfMEGxrS9GiDpsMA6jTXagKFyONr19F5JdHgoCgkjDMRk7yWlGeVDbgxua1Ld4ntdZQuJFTrdM4-nHWZj9_mSaw0wnEAGzWhNta4B7tzwlv-JvRtMt5h0LfPVtO-OG-UqVyKbxt166okMo7kr0KHYM4y4pTZHoudcD99-Kiuq__-Yusn6NPYoXFDkuhURzJDZu0Jg-AoQ3Z3ZAcYvPk_Def5S-j3b4QfoazBIFltHef1_YlS5YJY8j23M4b8MYyOsm11GOBKjVNbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
برخلاف ادعای مدیرعامل گل گهر، انتقال مهدی تیکدری به پرسپولیس نهایی و قطعی شده است.
✅
خبرگزاری فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/133740" target="_blank">📅 20:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133739">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇺🇸
ترامپ :
🔴
رهبرهای جدید ایران آدم‌های باهوشین، خیلی هم باهوشن؛
🔴
به اندازه قبلی‌ها تندرو و افراطی نیستن، فکر می‌کنم واقعاً کشورشون رو دوست دارن و آدم‌های خوبی هستن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/133739" target="_blank">📅 20:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133738">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇺🇸
ترامپ: متن تفاهم‌نامه را نه تنها منتشر می‌کنم، بلکه احتمالاً یک نشست خبری برگزار می‌کنم و آن را کلمه‌به‌کلمه می‌خوانم تا رسانه‌ها آن را به‌درستی پوشش دهند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/133738" target="_blank">📅 19:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133737">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✅
قرارداد تیکدری بزودی امضا میشه/آنا   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/133737" target="_blank">📅 19:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133736">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
پیروز قربانی: من نیوزلند رو با فجر سپاسی شیراز می‌بردم مطمئن باشید نیوزلند اگه تو لیگ 16 تیمی ما بود، جزو چهار تیم آخر میشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/133736" target="_blank">📅 18:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133735">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❗️
نیوزیلند از دستمون فرار کرد و خوشحاله یک امتیاز و گرفته .چون واقعا زورش به ما نرسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/133735" target="_blank">📅 18:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133734">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❗️
❗️
خبرگزاری فارس هم اعلام کرد:
🔴
مهدی تیکدری پرسپولیسی شد...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/133734" target="_blank">📅 16:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133733">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔸
شنیده ها
🚨
🔸
میگن فردا از کسری طاهری رونمایی میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/133733" target="_blank">📅 16:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133732">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❗️
❗️
خبرگزاری فارس هم اعلام کرد:
🔴
مهدی تیکدری پرسپولیسی شد...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/133732" target="_blank">📅 16:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133731">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
‼️
مهدی لیموچی به پرسپولیس پیوست/ خبرورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/133731" target="_blank">📅 16:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133730">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❗️
❗️
با چهار بازی امشب و بامداد فردا دور اول بازی های تمام میشه   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/133730" target="_blank">📅 16:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133729">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✅
برنامه بازی‌های روز پنجم جام جهانی
🙄
سه‌شنبه 26 خرداد
⏰
22:30 |
🇫🇷
فرانسه
🆚
🇸🇳
سنگال
👀
چهارشنبه 27 خرداد
⏰
1:30 بامداد |
🇮🇶
عراق
🆚
🇳🇴
نروژ
⏰
4:30 صبح |
🇦🇷
آرژانتین
🆚
🇩🇿
الجزایر
⏰
7:30 صبح |
🇦🇹
اتریش
🆚
🇯🇴
اردن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/133729" target="_blank">📅 16:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133728">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
دنیل گرا: در ایران احساس امنیت می‌کنم
🌟
شب جنگ جولیانو (مربی بدنساز پرسپولیس) به هتل محل اقامت من آمد و گفت که پرسپولیس قرار است فردا اعضای خارجی تیم را با اتوبوس به مرز ترکیه ببرد. روز بعد ما 15 ساعت در راه بودیم و پس از رسیدن به ترکیه از آنجا با هواپیما…</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/133728" target="_blank">📅 15:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133727">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe69dca3f5.mp4?token=V2puGI60wd3kF2xD3frUJ0-HWeBo0PbapEmLvo5meDgi9y4LpogZR7lB9xArH0fJSvEyFTJ0e4caNdJl3Lkb2H4a7OaLzYB1xbOHfxiyxtQPM0QHnDGUee3pM8-65L0Lwv8mRBnmGtqk-GzKR4EtIekQ3ypxYHjhUEgJhH73ZXtZuqDp6gHSx41mD3XeW7uj7kTskthWk103sVTl5CPHhVYTSlpLqbg7KEEQjaUaUV9l3hO2xGts61svrgk1mVyjhTPk_EI36dk3OeRcgfo-6YfGVy78IJIkpFNNF4p21TbxP-5LbNQK75Jg4VnE5jJZaBI4pJt8LO8Nchq2RnikOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe69dca3f5.mp4?token=V2puGI60wd3kF2xD3frUJ0-HWeBo0PbapEmLvo5meDgi9y4LpogZR7lB9xArH0fJSvEyFTJ0e4caNdJl3Lkb2H4a7OaLzYB1xbOHfxiyxtQPM0QHnDGUee3pM8-65L0Lwv8mRBnmGtqk-GzKR4EtIekQ3ypxYHjhUEgJhH73ZXtZuqDp6gHSx41mD3XeW7uj7kTskthWk103sVTl5CPHhVYTSlpLqbg7KEEQjaUaUV9l3hO2xGts61svrgk1mVyjhTPk_EI36dk3OeRcgfo-6YfGVy78IJIkpFNNF4p21TbxP-5LbNQK75Jg4VnE5jJZaBI4pJt8LO8Nchq2RnikOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
دنیل گرا: در ایران احساس امنیت می‌کنم
🌟
شب جنگ جولیانو (مربی بدنساز پرسپولیس) به هتل محل اقامت من آمد و گفت که پرسپولیس قرار است فردا اعضای خارجی تیم را با اتوبوس به مرز ترکیه ببرد. روز بعد ما 15 ساعت در راه بودیم و پس از رسیدن به ترکیه از آنجا با هواپیما راهی مجارستان شدم.
🌟
با اولین پروازی که می‌توانستم به ایران بازگشتم و به چیزی فکر نکردم چون من چنین شخصیتی دارم که اگر خانواده‌ام به من نیاز داشته باشند، من همیشه کنارشان هستم و اینکه ببینم چطور می‌توانم کمک‌شان کنم.
🌟
هر جایی که بوده‌ام و در هر تیمی که بازی کرده‌ام، تیم خانواده دوم من بوده است و حالا پرسپولیس خانواده دوم من است، به همین خاطر تردیدی به خودم راه ندادم و بازگشتم و حالا تمام توان‌مان را برای آنها به نمایش خواهم گذاشت. من در ایران احساس امنیت می‌کنم، عاشق این کشور هستم و خوشحالم که به اینجا بازگشته‌ام
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/133727" target="_blank">📅 15:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133726">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
فوووووووووری :
🔴
مهدی تیکدری به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/133726" target="_blank">📅 14:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133725">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✅
جلسه آخره اوسمار با باشگاه زیاد خوب نبوده و گویا یه سری اختلافات وجود داره
🔴
به گفته منابع نزدیک اگر اوسمار با باشگاه به توافق نرسه مربی بعدی تارتار و گزینه های ایرانی نیستن ، از مربیان خارجی هم اسکوچیچ دراولویت باشگاه قرار داره.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/133725" target="_blank">📅 14:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133724">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✅
❤️
حسین خبیری، گزینه باشگاه برای مدیریت ورزشی باشگاه است تا جانشین محسن خلیلی شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/133724" target="_blank">📅 14:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133723">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
جلسه اوسمار و حدادی پیرامون قرارداد و مباحث مالی سال دوم سرمربی فردا برگزار می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/133723" target="_blank">📅 14:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133722">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEC0J5BBKD6oZKeZmJKlD0Rv6IYLTgQxJh3Frp90SDtZeGxzwKJE2FVSzLzASHxc80Pw6io-CfPlMK7fTJmfckcb33WxpgVykdJf6GOw38J-RSDRXXZzZKY6UTdh6_WOpQY49JNs739G4EUvukjIYsNHHUFL1qiC7rqRebY2y3gQ10vTzSBCwF5qnVZquVM_SazOVi54bSjzxgYhxwdxHre_CjbIIOrhnAYIw9Cn7zagujqZcaiYcEKXRSQTcUzSqMigPBLQeE-pYHDsd9eqVVo3NxEw3ogfWEeQVcHb09YHQCLzIIa4s56ikbg6x3XprE1XgDQFv5uJxbvjE9dnUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏆
گروه K جام‌جهانی ۲۰۲۶
[
پرتغال
🇵🇹
🆚
🇨🇩
کنگو
]
⏰
چهارشنبه ساعت ۲۰:۳۰
🏟
استادیوم ان‌آرجی
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/133722" target="_blank">📅 14:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133721">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">💬
اوسمار سرمربی پرسپولیس: مدیران پرسپولیس کارشان را به خوبی انجام می دهند و به ما کمک می کنند/  دعوت امیرحسین محمودی به تیم ملی؟ ج اگر چه در لیست نهایی تیم ملی قرار نگرفت اما حضور در کنار تیم هم تجربه خوبی برای اوست.
✅
مارکو باکیچ ، بیفوما و دنیل گرا نفرات…</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/133721" target="_blank">📅 13:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133720">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
خداداد عزیزی : از طریق یکی از دوستان با پرسپولیس صحبت هایی شده، من اگه بسته بودم همینجا جلوی دوربین میگفتم بستم، هنوز قراردادی امضا نشده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/133720" target="_blank">📅 12:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133719">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❗️
❗️
خبرگزاری فوتبالی :
🔴
🔴
اوسمار به مدیران پرسپولیس اعلام کرده برای شرکت در تورنمنت سه جانبه به ایران برگشته و برای ادامه‌ی همکاری در فصل بعد باید فکر کنه و از خانواده‌اش مشورت بگیره.
🔴
🔴
باشگاه هم به خاطر این که فصل بعد در صورت نیومدن اوسمار به مشکل نخورن؛…</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/133719" target="_blank">📅 12:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133718">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇮🇷
❤️
رسانه‌های بلژیک نوشتند که تیم ملی ایران بخاطر سفر از مکزیک به آمریکا، دچار خستگی شده و این بهترین فرصت برای آن‌ها است تا پیروز شوند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/133718" target="_blank">📅 12:04 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133717">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
❌
لوکاکو: بی صبرانه منتظر بازی با ایران هستم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/133717" target="_blank">📅 12:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133716">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔸
شنیده ها
🚨
🔸
میگن فردا از کسری طاهری رونمایی میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/133716" target="_blank">📅 11:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133715">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">#شفاف_سازی
‼️
تارتار هم محصول مشترک پژمان راهبر و فرزاد حبیب الهی هست و در کل ریدم تو دهن هرچی مربیه داخلیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/133715" target="_blank">📅 10:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133714">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVBK72Mafi4s4XbfbziODeDUpXuzXeD8LKo9UvjM3ylkYuyZAaYCQkJtnmeZeMGg4zaPfXGeotVus5IOMfuM-dsBsnWLeuFaCYVgivXk7NSgW-cusssdAK4U7ay4VTRWsr_DB6efdIewFQvx3FxDYj-lJ3_24_dYJZeHylWUa15TLFsP1Spp7PeZWjZppfCaZZp13kn9GcTWEECf9n5y_eMeu_3i7XlYRsfs4LbA3fTPgiJxiiBIuJT6s6VxK1hd_WbqrwC55Q2K0tPVS2-j97II5KgcIXGD4d7OJC2jmGs7cbKysDvWyuiZ4Qm7oi8h0eEkFxqM6avpNmWR_56oHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
اولین هت تریک جام جهانی 2026 توسط اسطوره لیونل مسی به ثمر رسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/133714" target="_blank">📅 10:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133713">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RV2oAGWYRmpk2gC4H5sLEtU3b89wYw_nEL699-MZz-ewbY9KaJP6ITvixO8yCSrzsUVWQtEr1N6SrmcahoV-ZzAekvCXfdmb5hNmXeznGd_EEKZUCBgVFjaSe35chZMtfa7F6eKggCtrWx5pZ9_E8IuNWIanS3ovfPEGurZmaszAtybuUQnieH6lGixkMkNIP-FHgckvJ3DFsZif41heYVRwtifye3tqX36DEohW0DX87n-A7Kx9NfjVicEDxM91387jFLeNjTNx7Sm_viIdAwJOZ-WdqJEnWDJ1ltYAKi_nWA7-2P73V76zw5eSoMFFWIacCkh80gHduyZ0uE7HiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
جدول گروه J در پایان هفته اول
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/133713" target="_blank">📅 10:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133712">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
بانک شهر می‌خواد نقش اصلی رو تو اداره تیم و خرید و فروش بازیکنا داشته باشه، نه فقط حمایت مالی.
✍️
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/133712" target="_blank">📅 09:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133711">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✅
✅
گویا فقط ویزای مهدی ترابی باطل شده و شایع باطل شدن ویزای طارمی اشتباه رسانه فرانسوی بوده
✍️
آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/133711" target="_blank">📅 09:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133710">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efadb3452c.mp4?token=PsOlyM8n8Omo986r3co8r9u5eAQmvogUgYLb9AiMeAJDbNIclqBoLiWeDNIEzxw_s35M8VMAZO6KOMIb5Oaksbo01DZD7ArhFVkbAzN1DhjS1hwmJ2-aJ3Cnf-3f2Pv09zKn9-Us4ts7OQ2OaG3SXtTMwoIAsYR1mf08jnWxK8ByhRxkdXxAWbzUbK8Ni72BPIP1XAEchvggvhFGi3hVv7q2J72CcmDO-5B7cvZsNBuBNkoh_-EKIui9LOcx7caGAOETPlWmai5KWLcU8jp6fFMuguA-xPiRVKA0QcvAK8eXZBCCAX1K3IFiqm0yYFZjqUpLpRxMHiAd_AIVr_t15wmejFsx7d2sJsu9n9dtuRV57aj-RVlPZoR-tgvaUhkZvIyqkHIQYzqcVEkO9GUKfeqcFtg3HOuL4Nnc6FMQJJu1Guz6L4cPyDG1weXweQ8pAe6VyA6j33sMbLkRqdaj9QztO6dLq6Ov_iIFTVbCkS_KcJsCed29C-mtHz77Qs2nx1cuOLVtpHECrmx-LukaDKmYIOzSNoDXmVocsOZ8ZaMn2vScpxPhmSxjoFyRHSIAtk42QfpgV75acSnVHZUdThcx1fCH_dvisk3j2K0vxylDD41sSAY-TwHYoa0olCqgG3DALbg3YIJeAdQCeqoKIa2H9YtcETrX9QTp_yZIQw0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efadb3452c.mp4?token=PsOlyM8n8Omo986r3co8r9u5eAQmvogUgYLb9AiMeAJDbNIclqBoLiWeDNIEzxw_s35M8VMAZO6KOMIb5Oaksbo01DZD7ArhFVkbAzN1DhjS1hwmJ2-aJ3Cnf-3f2Pv09zKn9-Us4ts7OQ2OaG3SXtTMwoIAsYR1mf08jnWxK8ByhRxkdXxAWbzUbK8Ni72BPIP1XAEchvggvhFGi3hVv7q2J72CcmDO-5B7cvZsNBuBNkoh_-EKIui9LOcx7caGAOETPlWmai5KWLcU8jp6fFMuguA-xPiRVKA0QcvAK8eXZBCCAX1K3IFiqm0yYFZjqUpLpRxMHiAd_AIVr_t15wmejFsx7d2sJsu9n9dtuRV57aj-RVlPZoR-tgvaUhkZvIyqkHIQYzqcVEkO9GUKfeqcFtg3HOuL4Nnc6FMQJJu1Guz6L4cPyDG1weXweQ8pAe6VyA6j33sMbLkRqdaj9QztO6dLq6Ov_iIFTVbCkS_KcJsCed29C-mtHz77Qs2nx1cuOLVtpHECrmx-LukaDKmYIOzSNoDXmVocsOZ8ZaMn2vScpxPhmSxjoFyRHSIAtk42QfpgV75acSnVHZUdThcx1fCH_dvisk3j2K0vxylDD41sSAY-TwHYoa0olCqgG3DALbg3YIJeAdQCeqoKIa2H9YtcETrX9QTp_yZIQw0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
رختکن تیم ملی پیش از دیدار با نیوزیلند و صحبت های زیبا و انگیزشی علیرضا جهانبخش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/133710" target="_blank">📅 09:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133709">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubWcVaOT0DAITbjkZxY3V3Z2y308or3pnrBaWRnEdlMgO5Aqkpt0re7CEyz8VWCX8pe2qv6z0rM4hvmQIMSZyd0dR61J5tmasVXWnPv-KybyGn5jYe2xvIF2wI5zTy9BLXUr5aBxDX_-gWAnVPd5cUwRCd7_317PU9UgjTXAp_KiTm7xBuAx0B9DCUo4_4ZtWcpsmn2ZJyh3pISMNvME8z90DwQ6AOvBEOUpKfQ2gcDahCTHoY6fG1VXLkPSn1PuHi2-B_q1uG3_RJ2BZHdR80ya9dbtAc1UkeMs2andkjVyx9jVmbSmc9uGA6evSHBtX2S6LNKI2fw9Bu38YmGEUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏆
گروه J جام‌جهانی ۲۰۲۶
[
آرژانتین
🇦🇷
🆚
🇩🇿
الجزایر
]
⏰
بامداد چهارشنبه ساعت ۰۴:۳۰
🏟
استادیوم اروهد
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/133709" target="_blank">📅 02:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133708">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
#فوری
| سنا با محدودکردن اختیارات جنگی ترامپ در قبال ایران مخالفت کرد
🔻
سنای آمریکا روز سه‌شنبه با اختلافی اندک، طرحی درباره محدودکردن اختیارات جنگی «دونالد ترامپ» را در قبال ایران رد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/133708" target="_blank">📅 01:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133707">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GywlYc2287N81joOzj_ebT40h2vIcFX4jwW_WLIqI7bdKPbH8TkPyXp-o9fHabsa-rjd50C0REVAbt7ynqApN_KpueLQ83j3XdBU054UKC82lsUKutxIpBa311JEd9ZCRE1LgHJ0h00r_O0OH1hvaW7AV6T5ND218bQ5wXHBnLv3zTJRHHaEn0Cl4qcnsHzZgRM79gpOUgjEuRirqU1HRqFV4k6ikG5FD1Xz3WLhcZ05freKWq7By2ZU3envQya26LY2UjYO5DMZENSapEuKpbgNqH_CGmYHekQKLoYe9bbMFlH-C0jjhDbPkJst1EqvYgj4uIex7-q4paD7HW10rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
پست اینستاگرامی اکبر عبدی با عکسی در کنار علی دایی در بیمارستان
🔴
علی دایی، اسطوره فوتبال ایران، با اکبر عبدی، بازیگر سینما و تلویزیون که در هفته‌های گذشته دچار حمله قلبی شده بود، دیدار کرده و جویای حال او شد.
🔴
اکبر عبدی با انتشار این تصویر در اینستاگرام، از علی دایی بابت پیگیری احوال خود، قدردانی کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/133707" target="_blank">📅 01:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133706">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aad4cd3bf3.webm?token=hiT6OeovGqkvZKcwgnVNsvZomBqmE-87pzE8Zsjjr2X0XO5y5kMlxgr3u2_65p4zYUXNaKFdNUWHDj-BlhtGAKJzuq-XsfnYR4Y8910iMsyVT5rov5qsSKYgKTrP1PrLy4jR9qKKqFAWqrNjSs2-M588HVeMMXznPXynUnuRJQ6i366NMVyfMJaw1rUVWoXIoaxZ0A4LRC9BZVELGMGLmBpskFrf1e37ghz3vV2QbD4skV5Yq3lJPRcrwM-JBzqTdSra9Dy57ADF4e_s4W9DGE2KvCzOQOx51lrWmPabf_Nl0Nei3aezZQO7rzh6oFCXzRngJ1o8cxXrA64gaofUaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aad4cd3bf3.webm?token=hiT6OeovGqkvZKcwgnVNsvZomBqmE-87pzE8Zsjjr2X0XO5y5kMlxgr3u2_65p4zYUXNaKFdNUWHDj-BlhtGAKJzuq-XsfnYR4Y8910iMsyVT5rov5qsSKYgKTrP1PrLy4jR9qKKqFAWqrNjSs2-M588HVeMMXznPXynUnuRJQ6i366NMVyfMJaw1rUVWoXIoaxZ0A4LRC9BZVELGMGLmBpskFrf1e37ghz3vV2QbD4skV5Yq3lJPRcrwM-JBzqTdSra9Dy57ADF4e_s4W9DGE2KvCzOQOx51lrWmPabf_Nl0Nei3aezZQO7rzh6oFCXzRngJ1o8cxXrA64gaofUaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
شنیده ها
🚨
🔸
میگن فردا از کسری طاهری رونمایی میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/133706" target="_blank">📅 00:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133705">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
🚨
🚨
🚨
کسری طاهری، تیکدری و گودرزی خریدای پرسپولیسن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/133705" target="_blank">📅 00:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133704">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4F4-7fol0DjGKc4ut0PWGoqd-kuJWCkN02lcEYGtSNj1lUV_qh94wyu5nPWft4_GtYqc8u6JwcRqKyDA8AMHd-KIySUjC9INb9UmaINXwsNtwcfdD7pepIQarpT-MjhNXkPzVHsmKqXiu90DfdItHBENJrjxF4Nb8c6Lw-cKbQ1J9NmWR6YbUl6nq_RKZ0rPsf_wMqXjub2YQyK0AHzP7fjwBnEsx046Zt7Wc-xpIZcIenj2j7N-6aJzCK7JgGyH-81J9MonZ4wSxAMvzfWKA3jKU-sf6bENi9sFL36F5QjVRj0LSLEgfyOUyuUEwekDN4JU6UnVB-Gqqot0ACtCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
سیدجلال: اوسمار پیشنهاد داد برگردم
❗️
صحبت‌هایی در این زمینه انجام شده و آقای اوسمار هم پیشنهاد هایی داده‌اند اما تصمیم‌ گیرنده نهایی من نیستم. این موضوع به نظر مدیران باشگاه و افرادی که درباره مسائل فنی تصمیم می‌گیرند بستگی دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/133704" target="_blank">📅 00:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133703">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feaf2d5596.mp4?token=khpF-LDHdC9i2XHYWsB3JWRmldM7fj0MYelyKn49m2leoqbqX_651HIQQO14Iday8Tt_f4O4genqvMn23v9J6GTcBL631ELvpNUY0Nb6Ze13eqOk-q10lExZe6AuCTHQhO3qqnVbifh___XzZIIKBkuBqrJdvJMUjo7ZGloj2-ko3guQGSZStY7rJWXPydKBfQ-CN9hhD33nHR_AXAQDiIe03G593mc99f_zI3cnyb0aWOAJayJ19PACIrBfjQFnhbE6Bjc9stedDld0TnN6pLKdi7pvVPEYeXdpbxp8d86juW0xJanzEwnMLmQBYRH5QFVME9-nMsJFoTjbdugA5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feaf2d5596.mp4?token=khpF-LDHdC9i2XHYWsB3JWRmldM7fj0MYelyKn49m2leoqbqX_651HIQQO14Iday8Tt_f4O4genqvMn23v9J6GTcBL631ELvpNUY0Nb6Ze13eqOk-q10lExZe6AuCTHQhO3qqnVbifh___XzZIIKBkuBqrJdvJMUjo7ZGloj2-ko3guQGSZStY7rJWXPydKBfQ-CN9hhD33nHR_AXAQDiIe03G593mc99f_zI3cnyb0aWOAJayJ19PACIrBfjQFnhbE6Bjc9stedDld0TnN6pLKdi7pvVPEYeXdpbxp8d86juW0xJanzEwnMLmQBYRH5QFVME9-nMsJFoTjbdugA5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
‏پیروز قربانی سرمربی فجر: با
بچه‌های شیراز نیوزلند رو میبردم!
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/133703" target="_blank">📅 23:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133702">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✅
مهدی لیموچی در یکقدمی پرسپولیس/ایلنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/133702" target="_blank">📅 23:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133701">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0DWFpQonHYPaZ3QeiJeBoz5OTklea9EKWggYpE85wjcP_uI9yn2yo4tldKT_q4O-DGYbAQhj1SnXh9m1gkrrI0KcTpY0kpsfhaxqSKgCQPrnXP2e26Bl8dxiaeLhla5bbQ7MA1iwpm5SSXiGCHCpNYN-SIGbHA681klZVHfJBX3dSN6cMygMbu30jaqMR-0pu75Yuu-CQj3-A8tAtjRCIlN56hnNMvr1JRbUAEW9FQ0tlJopyNQ38QPL32Pnl-HOXPCRiwt3i2harspYhkvXadlX3H_VRUxjKum5dBQyBxtNMOSCfu2GA5YI-gCa6An-savfasI_Lw9a2_jNtBoag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
رامین رضاییان در بین ملی پوشان: میخواهم تا چهل سالگی دربالاترین‌سطح خودم فوتبال بازی کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/133701" target="_blank">📅 22:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133700">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
رامین رضاییان: شادی گل من سیاسیه اما اینجا نمیخوام دربارش صحبت کنم. گلم رو به تموم مردم عزیز ایران تقدیم می کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/133700" target="_blank">📅 22:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133699">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✅
برنامه بازی‌های روز پنجم جام جهانی
🙄
سه‌شنبه 26 خرداد
⏰
22:30 |
🇫🇷
فرانسه
🆚
🇸🇳
سنگال
👀
چهارشنبه 27 خرداد
⏰
1:30 بامداد |
🇮🇶
عراق
🆚
🇳🇴
نروژ
⏰
4:30 صبح |
🇦🇷
آرژانتین
🆚
🇩🇿
الجزایر
⏰
7:30 صبح |
🇦🇹
اتریش
🆚
🇯🇴
اردن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/133699" target="_blank">📅 22:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133698">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPcQuCZ7YOocr_ovy-mfOLQrFDtliP8a3Nd7m_CTbMY7F3XQhydgSq4-_CQlxKMk-HziWXyZFQm077_0-2SsaE9ZxFqbKTkkvl-01Y9C8pvxCizbYxuCS5aKhQolEuump7b-E6cp5gpDFRtAtixjs8uqpmOxM1zsBK6S-u45S4onfYBNxd3czbUOFbAusn_9_GxBvTCE4n5VtmkCZIjlHGN68IzZV-v1EIbn1EaQ_gf_Cf1G4Hce1rcxBjPOOwXCe_w_IJO5rZXwUfEMLyU3krhJUQUI04iqYmOH-tyLvOXc7fSxS3hpODur_BIbR_irchenldINIIxKfDs_hTWCsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رامین رضاییان: شادی گل من سیاسیه اما اینجا نمیخوام دربارش صحبت کنم. گلم رو به تموم مردم عزیز ایران تقدیم می کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/133698" target="_blank">📅 22:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133697">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔸
نشریه‌ معتبر ESPN: علیرضا فغانی که‌ داور دیدار امشب سنگال و فرانسه‌ است اصلی‌ترین گزینه فیفا برای سوت زدن دیدار فینال جام جهانی ست، و اگر اتفاق خاصی‌ رخ ندهد علیرضا فغانی فینال رو سوت خواهد زد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/133697" target="_blank">📅 21:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133696">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NH_yBULggIcPzUsrCFa_3PWm1FnveucrQtThFCxrt3twAwunDtYKVzX3dBg1-nr30k9hXVx8ftf33XwxFa4JSjL8yV699l2ZVH9cRtNFFQ-bG69o1wtritNg-ntzinaUtW8E8riMlBBHTKsuZ3uiHxglIdMbNk_DLq8I5cmzV1UVzidUe9xRmaV6k80vWYMLTiw0FfM2HWphIfz6h_ynxrLYWH5XCtbp0p0xF33n3V1DNlrRB8tMzdagFnhAbJg-25DhCqCeVrYPGcCwPkj4MZeoHKhBmmj7U_eClDEMrP_lwvldiZ0XAclChhr1mmPcVXEOPydoc03kcIKmRvrBxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
نشریه‌ معتبر ESPN: علیرضا فغانی که‌ داور دیدار امشب سنگال و فرانسه‌ است اصلی‌ترین گزینه فیفا برای سوت زدن دیدار فینال جام جهانی ست، و اگر اتفاق خاصی‌ رخ ندهد علیرضا فغانی فینال رو سوت خواهد زد
.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/133696" target="_blank">📅 21:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133695">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
فوووووووووری :
🔴
مهدی تیکدری به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/133695" target="_blank">📅 21:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133694">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WoTIbSEHMzhl3yFjHWDyeZqb2HwoHAOX_FKw57eaG76jH_ExotpA-gPj2DjWnIhC9sb_wxWXgZO31i4maBWlhQLjoOj7ANPqoLSaCZkAiSzLKWlVVpaPF0bClUxiK0cK9hl_cH8EXKfXpZPA0eU3i4mgWHqxrZkftNyBWgqhvx524HVCZxR4sL_TjllXtc2RSndeHbGzh8bVHACzW708LI_XjE2J9zPv4BZHGNUc7CCLJKQD_kJu2Vx8u_22a7m1tOV9L98ZP7-ebZDs91HS_KbQtd44lf_sBICuMC1z9733DOlfz8fceJ6jLjoOpkulc2JAleodOk46wSqr20mCOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
بونوس ویژه جام‌جهانی وینکوبت ادامه دارد!
🔵
FRANCE -
⚪️
SENEGAL
⚫️
جام‌جهانی گروه I
⏰
سه‌شنبه ساعت ۲۲:۳۰
🏟
استادیوم مت‌لایف
🎁
۱۵٪ بونوس ویژه به مدت محدود روی تمامی واریزها فقط با یک گردش روی حداقل ضریب ۱.۸ به موجودی خودت اضافه کن.
⏰
این بونوس ویژه فقط تا هفته آینده دوشنبه ۱ تیرماه ساعت ۲۱:۳۰ فعال است.
📌
همین حالا وارد ربات وینکوبت شو و ازین بونوس ویژه استفاده کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/133694" target="_blank">📅 21:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133693">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❗️
مهدی تیکدری نژاد مدافع راست گل گهر سیرجان با عقد قراردادی سه ساله به پرسپولیس پیوست/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/133693" target="_blank">📅 21:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133692">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
فوووووووووری :
🔴
مهدی تیکدری به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/133692" target="_blank">📅 21:08 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
