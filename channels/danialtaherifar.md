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
<img src="https://cdn4.telesco.pe/file/ejjMEcidefddIFR4liP3xfxdFzpjzMhszp877ZEVL87Pwx8fJt292ZDgBZoIP9qOT7uoEsQvfGA9SzZOOgkG8aiyO_Dexen8HMUtfHfJjW7DRH9oInkiYEXnLD8UyveO6o5T1BHjuyh25CAIWUhcyRjKukwe0dPBnCeAzBtGViGSUBHdbbSZrOQ4_lczRJJ_ylprO9PplV_UvMQBtlfQqNiD2AnzO109jWEV9jYA568XM8Fvdhdp3q3DR5PS-ZPhPOkSOeJ8Fv3Bbit_QgEHgzLd8gKUEkNnU7blr-MuiMB3tWQGPjiMVIcJlGF_3Xx4fn2C9hvv_jqwgjovq5wm_A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.54K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 09:53:06</div>
<hr>

<div class="tg-post" id="msg-939">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
اگر از claude استفاده می کنید و اشتراک تهیه کردید، موارد امنیتی رو تا حد ممکن رعایت کنید
بن شدن اکانت ها شروع شده.
پ.ن: اکانت اصلی خودم پرپر شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 216 · <a href="https://t.me/danialtaherifar/939" target="_blank">📅 12:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8hv7vOaQzEU7R_u_1UDSAvPQ6IlHlY_sIEGXL1aHT8rEDVl1zorxER_XxxUqlO0dFsn5KP7GvqFSovsrdEgapxN4yo8mWKou8VnrjyObEZW8nKsI_NLH1cwm5qtGzNfoypoBTL4cOkUMJBSMtDfsUwzfSELI5QBGkk1qWwUOc-8HdMHqjKFBWrUuoKhlhKqJXKlcw1cZ3QVqfHbnEfjq71Ey-GxgVcnjQT4ZtxnqSMAkZBtXZadVGLmuXJBH41unKREaSQE4MktkKAVp1_1M1QoIU0-mqeKj05I7QigRCqrBvK85cKTSRgL72OWDjNa1suyzbvzGFVJOnhMHGXjqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 460 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-937">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست
دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل
Fable 5
و
Mythos 5
قطع شود.
نتیجه: آنتروپیک مجبور شد این دو مدل رو
برای همه‌ی کاربرها
غیرفعال کنه تا با دستور هماهنگ بمونه.
📌
نکات مهم:
• مدل‌های ضعیف‌تر مثل
Claude Opus 4.8
دست‌نخورده موندن و کار می‌کنن.
• دستور از طرف وزیر بازرگانی (Howard Lutnick) و دفتر BIS صادر شد.
• دلیل دولت: کشف یک تکنیک دور زدن safeguardهای Fable 5.
• آنتروپیک می‌گه این jailbreak
محدود
بوده — فقط یک قابلیت خاص امنیت سایبری Mythos رو باز می‌کرده، نه شکست کامل تمام محافظ‌ها.
یعنی عملاً قوی‌ترین مدل‌های هوش مصنوعی آنتروپیک حالا فقط در دسترس آمریکایی‌هاست.
🇺🇸
@danialtaherifar</div>
<div class="tg-footer">👁️ 629 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 725 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 733 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-934">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=XR27pa-q5vO-t_8u2Ai7rMSHEeLH5Lok7ZkwRJPJ9-c7NETesxoVCVaP4b7QwzKjQ6UdxB6-rwB2lRisHix3Sx9IUTImLyvUjBjf1QgkHVKMd4sBVE3fmfv3qy9ESZfHoPya25tdOxc7D2JJoUcHuY9x5vsuBqR7B2_-KOFqKw5_t7qch_JHPSeTo3lTydWxH3AAfm23MbsT1SwkGajiL8WGZE44b3lcdmmWdQiD60gAcmvQls6Bf90JcOdhYYZ1VOEzfYuskIv-G9J2ybfTpwk1WeiqQvk4KzR2CLuLEUm-BOhYhIHl-_hY-nkSQpebO8VQdzt3FZ5CIu4aBA5Kuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=XR27pa-q5vO-t_8u2Ai7rMSHEeLH5Lok7ZkwRJPJ9-c7NETesxoVCVaP4b7QwzKjQ6UdxB6-rwB2lRisHix3Sx9IUTImLyvUjBjf1QgkHVKMd4sBVE3fmfv3qy9ESZfHoPya25tdOxc7D2JJoUcHuY9x5vsuBqR7B2_-KOFqKw5_t7qch_JHPSeTo3lTydWxH3AAfm23MbsT1SwkGajiL8WGZE44b3lcdmmWdQiD60gAcmvQls6Bf90JcOdhYYZ1VOEzfYuskIv-G9J2ybfTpwk1WeiqQvk4KzR2CLuLEUm-BOhYhIHl-_hY-nkSQpebO8VQdzt3FZ5CIu4aBA5Kuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
گوگل از قابلیت جدید «Search Profiles» برای ناشران و تولیدکنندگان محتوا رونمایی کرد
🔍
گوگل قابلیت جدیدی با نام
Search Profiles
را معرفی کرده است؛ ویژگی‌ای که به ناشران، رسانه‌ها و تولیدکنندگان محتوا اجازه می‌دهد حضور خود را در نتایج جستجوی گوگل بهتر مدیریت کرده و محتوای خود را در یک صفحه اختصاصی به نمایش بگذارند.
📌
این پروفایل‌ها به‌عنوان یک هاب مرکزی عمل می‌کنند و آخرین مقالات، ویدئوها، پست‌های شبکه‌های اجتماعی و لینک‌های مهم یک ناشر یا کریتور را در یک مکان جمع‌آوری می‌کنند. کاربران نیز می‌توانند از طریق دکمه
Follow on Google
آن‌ها را دنبال کنند و محتوای بیشتری از آن‌ها را در بخش
Google Discover
مشاهده کنند.
👥
در فاز نخست، این قابلیت برای ناشران و تولیدکنندگانی فعال می‌شود که در حداقل یکی از شبکه‌های اجتماعی اصلی دنبال‌کنندگان قابل‌توجهی داشته باشند. طبق اطلاعات منتشرشده، حداقل شرایط شامل 100 هزار دنبال‌کننده در YouTube، Instagram یا X یا 300 هزار دنبال‌کننده در  TikTok است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 743 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCuJTivSgCWggRG-A6JwBYMlecAsKuLxDiMxqqjxGwuE7rH_VbZwUCpf9-OMPWs1kUfTFdP_XfuvADrRsEiY_OWycLszHpPRwrfDhJUwyL90HI7Evx3Ig65Qx4STaZKV6a93XK0CvI_qnT_G2_EE7xTXYhmkQoU1FHll2ahygVVT3AbuvUHsQDPzrKW7e0ubmFmSHN9vjl18zHRH-kBH6IcKx7OtoZ6cHb5NPwembgCndnbtF-wDw23Xjfcaeaf101x7OtN7Sg3rRqPhSqqjyiQ97sWIaa5hIf7XB8Nx19m69GkQM9aT7VpJnLZrpLptIycvpNjqWFeWbOEf_opvXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گوگل گزارش عملکرد AI را به سرچ کنسول اضافه کرد!
گوگل رسماً از قابلیت جدیدی در Google Search Console رونمایی کرده که به مدیران سایت‌ها و متخصصان سئو اجازه می‌دهد عملکرد محتوای خود را در نتایج مبتنی بر هوش مصنوعی گوگل بررسی کنند.
📊
این گزارش جدید اطلاعات زیر را نمایش می‌دهد:
✅
تعداد Impression صفحات در AI Overviews
✅
میزان نمایش صفحات در AI Mode
✅
حضور محتوا در قابلیت‌های هوش مصنوعی Google Discover
✅
صفحاتی که در پاسخ‌های هوش مصنوعی گوگل نمایش داده شده‌اند
✅
آمار تفکیک‌شده بر اساس کشور
✅
آمار تفکیک‌شده بر اساس دستگاه (موبایل، دسکتاپ و تبلت)
✅
داده‌های ساعتی، روزانه، هفتگی و ماهانه
🔍
نکته مهم:
این داده‌ها علاوه بر گزارش اختصاصی AI، همچنان در گزارش کلی Performance سرچ کنسول نیز لحاظ خواهند شد تا تصویر کامل‌تری از وضعیت سایت ارائه شود.
⚠️
فعلاً این قابلیت فقط برای گروه محدودی از وب‌سایت‌ها فعال شده و گوگل قصد دارد پس از دریافت بازخورد و انجام تست‌های بیشتر، آن را به‌صورت گسترده منتشر کند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 624 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 711 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 848 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 968 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hrmozK5j7lZ3fVIDNXOH__AdBTpgpdeE5ANGd8OcWZL1JIXyZlCmEKK3kyIf1YVMaQU2Zy7LqtJT7o2zmn5N0_eLDuuebFDQLXx22j5e-3sF_tcPDxhVrJBfueKP2x3FTpnHlIVX1Y_hVDFn1wuI2IfgrTlJsMzbsqGbx4n7JfBXUnKOUJB7ZC4WCNzhooog58jBY_g6sS9pAhkpVAkn-WIgCH4rAy8PHeAtK_LS48k0ScQUnfFAz61GSNacQx3dBwz_V0gPEMDbHLB2-34zyUs6Ewn_M72WrjCW7ukgPsI5QQEvSkK-N7pIdLOrAoEDbERJ7tvYnJaDOimEAA6lkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 984 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbIJrMBc5xKW3fDDZbNrxnT51ct2vyf9milualbrbLImqTXrTUv01ZwWXpRf5XAQrvXUmUuGM2fM7Y9TtnRYpm1zaBwqhaDieawGaSoedIKzr0Ser6RJmRwGRPqIfRzYgQ1MkeKdBYiZ3g1-dHW_49w4JOWWkACCWudDnKs5MwzgO3C7QOemsiEgUzv7VqBo9-n6tvDOJm3iPOYR_j0T-y0M-VG9kfSrKE7IgsNQxh8eh_QtbWAwTN1ZaKca12pGKfUV2WD8V1KgIicge9TbH3k_KqW5-IgDzz8SzUBup9gBxVFMMjTSva2Vuw83_rY56FDQWKRClpyUaDBawr7hAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/To-Bw_PhBdPoNjYrn3v6Hb2IpWAIeJOefPkAXDANQj-Mrnk07ldK2Pc11acuXQt36UJXUrlddwGJbl-HiWeh0DLgewULSYwfSoseK1X8xxhUeblfK5aGtzb_BIe4YGDany1K6RDKTNT_LobCUAANVW2-eAdYX2M2vZV4VztihNx_pbWd-BJ0Byo74JeLZLKTiwuuLt_oDxcvBSqruYb_Gevlj2I0Wd4uHJKtmhVJPsw6e-3NPJOeHmxUbQU-9mrUHsxtA3V1wwcpBoIHCXwtI4PgtFAKI1F9lMsFF_UDhyLOx_K5CxbxwN5yUMTkHC-6O4FZ4-OPu2eOkffxpemk-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzQG7v5rsN_g68vsL42rbgNcV7-aOFDWlSbFchVPwmcfktRag4MzeEmFqBw-6lt2_r2-tq6r02gUEF0esIA6B13CvG4R8IQlSHb5yCmxuJxOdQqDA800YuUf6mgf2-yS8D0YTlrXBCLlCj6IjNC7LZT2Pcri_kvMupTwZeThC3QRLTQX5QXAcKCIHI97F1zY2e9yqIHnWwPyqRi_1X249D-gzwa_6rwAE-s8choUdwSH1AB7H9VNFPrNjAaGJkCbY2e34xcWj53uz_KK0WcA7onFapP9jsNeguaJ1RonSSJ_C6ocnvX0TcrhBic_Fl_7W7NUtrijNCGN8KS4kf5ERg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبدیل ضربان قلب کسب‌وکارهای اینترنتی به یک «خط صاف» صفر...
💔
ما کسانی هستیم که زندگی‌مان، تخصص‌مان و آرزوهایمان به این «ریسمان نازک» وصل بود.
این فقط یک نمودار نیست ... این، فریاد خاموشِ میلیاردها تومان سرمایه، هزاران ساعت کار و تلاش و امیدِ صدها نفری است که در این مدت، نابود شده‌اند.
ما یاد گرفته بودیم با الگوریتم‌های گوگل بجنگیم، با رقبا رقابت کنیم، با «محدودیت‌های فنی» دست‌وپنجه نرم کنیم؛ اما هیچ‌وقت یاد نگرفتیم چطور با «قطع شدن» نفس بکشیم.
بیش از یک ماه گذشت...
یک ماه از روزی که «دسترسی آزاد» به اینترنت، تبدیل به یک «رویای شیرین» شد.
آقایان مسئول! این اینترنت، برای ما «تفریح» نیست؛ «نفس» است. برای کسب و کارها، برای فروشگاه‌ها، برای خدماتی‌ها... برای همه ما.
#قطع_اینترنت
#سئو
#دیجیتال_مارکتینگ
#سرچ_کنسول
#کسب_و_کار_اینترنتی
#ایران
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9Nx8cpHgdttHxjICt1w3S0hvTTvVwPWxUB849cFwAWTDKn1zD6qUZANe-5knSwTLjaiJnHhMTY-4p1fbo-qtxcWMkb-iCTL6XZbs9ztUQAKIfDIraiE5cXomQNQ4mVUnyifms4xKB1a2z0de0It760sssb2A7JXnc59zuaMmnGP7YqlIXqyw9NJduO04hpcccQzRwSjAO4ZS5gecVk3eTeC3OiALuH5ywAQ1k2i59R9kW0hbW3juNXevn5mpNqyy0qnn_yBBPHUDoJqRjPTTrrkEihyXq84I92KXjMFzWYR4WwdSwMCFXC6Id6ZSnZ2sf6VuRQ1JG_H96-DqOsogg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 947 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">درود عزیزان
نوروز رو به همتون شادباش میگم
❤️
امیدوارم که سال بسیار خوبی در انتظارمون‌ باشه و بعد از سال سختی که گذروندیم، کسب‌وکار دیجیتال حسابی رونق بگیره و یواش‌یواش درهای بین‌المللی به روی کسب‌وکارهای ایرانی باز بشه. سالی که در پیش داریم،میتونه فرصتی باشه برای جبران، برای یادگیری بیشتر و برای رسیدن به اهدافی که شاید سال پیش دور از دسترس به نظر می‌رسیدند.
سال نو مبارک و ایامتون به کام.
با آرزوی بهترین‌ها، دانیال طاهری‌فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 907 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 968 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZrCetA1SnIik1Hg8pdvxUdCz_mui5Z0T2ZgrvaoSen-Ow0ZmveI2K-YmWY2bKuM7_zbay3ydVoT656IV9RMFVeCzadFbo9-Gg-w7NeFxmgI_7lUf40UaVYZA14LFZs99kxJFopCFVBkvZKeZvbDEgeGQipKEN-S8bqsuDXZh4j8FSAAbRguLgowf2_Lf4oppYo0N6gDTRKXSC0YfV6jxolou8OTxLkRar7bBg_xNDOivP_HXB5iDVSu-F-dx-bsjJsREKEB03wG7GYfxfhtyP_CQxrvdDWx4f_BMSWrc3rxbBzp3piqao_EOeN61XQraGQdrYPszsmtofU1wkdM5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BO6gWtStlR3k_j7LYxhAzXK2iY08Ld9OqKWIwup4DkffEdseiQzjbhj0SUYuU7QlnfurgVQrMW60vnNdnXqiRHdocwCfAmxam3hCCP3N5Yokh9YulINL4eBSVisymhQDZUn2ZyQxpN7FbTT-T0vVc601sRR7idpPJI-92-ie8am5nW9OQtvZP8y-3loq2EL8vesBNkQ9yR88cJ8t35Zk-euhO1ZJRWUuv61wWUuXO3iUvJqfF45Hfjt_gy38a2dKqerTlwqtDbCD1poClC89KzHVRCbpyjSUpkC4ICVJGZERyWoO1rz2JJ1xdZWdnb0I9ogW3W5aqR_ZsIO1c93Nxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S5EC4xC7O2uv_yrC1qwLeY2DzaZO_Ww6jpN5Scjha9Xkffm4Rugc6C4xc2InBTS1ERhSb3K_RFulrw1i_llX52Q-RQ4JIgW2qdYpOmQalGsZbflNYEYa_rHxXthmA05UVcuHn2fO9NmZqi1fV0z4leT66X0fqo_5i0tHYCuAS6GEjPn-TvwKapnzdGwg8jFIPZMkUpTItCR4755g60QItO782Fp477Td1IGOa3mnMZJ6DGS_J6NuoDrCxFnj0lh2OAEbTBIK-9aO6zoraLwNvFygkyDAHKKk3lisG_rhC8BByvMHlG3VdDqxWvee_u3KWwhYuXT9AcQUf6GYs4sISw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2GKIYrm-EbGMHpeEENl04sn3Pt1Z5MRvXor4kYP5SgzqQYwRblvsmBRM5PNpCjeF1eYX7qiaDid6B3CLFsHxVRSeVCMlKe5_jhYZa4if3vidSeauaDDgRz3Acsx03MCaJ__63vbi9_RLaC68upfGCvbuCl8XQl33cuOE0Tn295mA5HzttVNU1DN2mx9LPPRwaVnb8WVid261GcRFkhSuVrc5OWKRecgA8wJn0I06J5I8eAko7RkJ5RL68z9PvCWanFXC9YkpVGoimTY0k4p_UFjIVqeXJQIFb2yn88Dr38J0HCfmQkbe08Bq3v_ewM2JYbduLV1psztKyVR9pOgtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 884 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-914">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">⭕️
❗️
بعضی از هاستینگ‌ها از شرایط به وجود اومده نهایت سوء استفاده رو بردن...
از هزینه های 40-50 میلیونی بابت ارائه خدمات ویژه، تا مجبور کردن مشتری به خرید سرور اختصاصی برای سایتی که ۲۰۰ آیپی روزانه ورودی داشته ...
منهای این الان شروع به تبلیغ پیامکی کردن یه عده برای این موضوع، بعد سایت خودشون فقط یا از ایران باز میشه یا از خارج !
در کل مراقب باشید ازتون سوء استفاده نشه، وقتی که عصبی و تحت فشار هستید راحت ‌تر کلاه سرتون میره
@danialtaherifar</div>
<div class="tg-footer">👁️ 958 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 835 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 680 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 898 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPK-D9K0hNaJd7srXV3GvZumPiH1H5lRWYgaAWgo7pg_iL66F9S9tuoLfvtnJcX-lCJwIwzJBbykzxHfDcc101f1Y6QvYXd1g9CZWdOXdftsa-Uk657L2CsKat1jQuf2IHaka9ewiXSccEgMugp3mApi4z_8g9oOnN1VmyJ9w5_UgDmVpQv4WKZjEoMQqXDnaVprsL6olNVHxq_68vlyUpMoQJCzesfQd8YT_0ntc8c2bYyacF9eCUpV_ZRG59Xd2S8GoVcUL7z1NX3xXD46AgyXLXSdp7bcZtBvg6pat_GMjR-XgBmYgBcl_T4N5wKAfPRe5ZgAClN-o-2gWeJlqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 880 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🟢
راهکارهای رفع مشکل سایت‌هایی که داخل ایران میزبانی می‌شدند و از نتایج گوگل حذف شده‌اند
برای این موضوع چند راه‌حل وجود دارد، اما رایج‌ترین و عملی‌ترین آن‌ها عبارت‌اند از:
1️⃣
راهکار سازمانی (Enterprise)
استفاده از CDNهای Whitelist‌شده که معمولاً فقط به اشخاص حقوقی و شرکت‌ها ارائه می‌شوند.
2️⃣
ایجاد Mirror از سایت
ساخت یک کپی کامل از وب‌سایت روی هاست خارج از ایران، به‌منظور دسترسی بدون محدودیت گوگل.
در این روش DNS به‌صورت هوشمند تنظیم می‌شود
ترافیک داخل و خارج کشور از هم تفکیک می‌گردد
⚠️
به‌دلیل اختلال در ارتباط مستقیم بین سرورهای داخل و خارج، معمولاً امکان سینک دائمی وجود ندارد یا این کار از نظر فنی زمان‌بر و پرهزینه است.
برای اجرای این روش، با پشتیبانی هاستینگ خود تماس بگیرید و درخواست سرویس GeoDNS بدهید.
3️⃣
(در صورت دریافت مجوز از سرویس‌دهنده، اعلام خواهد شد)
❌
نکته مهم:
در حال حاضر برخی سرویس‌دهنده‌ها در حال بازگشت به دسترس هستند؛ بنابراین پیشنهاد می‌شود از انجام تصمیم‌های عجولانه خودداری کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 829 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 773 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-906">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✅
رفع مشکل کندی پنل وردپرس در زمان قطعی اینترنت
اگر از سیستم مدیریت محتوای وردپرس در وبسایتتون استفاده می کنید، در شرایط قطع اینترنت به دلیل داشتن درخواست‌هایی به سایت های خارجی احتمالا کندی پنل به صورت بسیار اعصاب خورد کن رو تجربه می کنید.
دو تا راه حل واسه این موضوع هست:
۱- مسدود کردن ریکوئست های خارجی در مرورگر با زدن کلید f12، رفرش کردن صفحه، انتخاب درخواست های خاجی(از جمله فونت های گوگل و yoast و ...)، راست کلیک کنید و زدن گزینه block request  (محیط dev tools باید باز بمونه)‌
۲- از طریق فایل wp-config.php کافیه که کد زیر رو در کانفیگ قرار بدین تا تمام درخواست های خروجی رو متوقف کنید:
define('WP_HTTP_BLOCK_EXTERNAL', true);
و اگر دامنه بخصوصی رو نیاز دارید که در ایران میزبانی میشه و در دسترس هست، دامنه را در کد زیر جایگزین کنید و بعد از خط بالا قرار بدین:
define('WP_ACCESSIBLE_HOSTS', 'torob.com,*.danialtaherifar.ir');
با آرزوی موفقیت
❤️
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/danialtaherifar/906" target="_blank">📅 14:51 · 02 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-905">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0AsSiY5DfptO7vxNvOoQtZvex4BO5mEAdIciP02FeaZA9Q-SeDs8tsUeh7atyVyHuAlxtK1sMV2h-2V0k4tHVqds9fHSR4eWTcunj-FNn-3-BWDP54UuqalRI-aIYYuyS5Lrz-LzyKz-Rp0fqJjA3Sy2Fxm2i_cziMzr054EviHTCEoHqATSX0TRGqRKbcAOkO4IsP_Rp8Gep4yDLlbQTiLQ1O9A8XRyQQ3ZuBExbJ5MOmssFnHcxZ6e2-_QEzMJY3b5zFTEtJ-K7MmPlnxrWS3idpx7gpK-3-Eu77CuaWonsCagPSFxAqjO5jCUV2F3ufEhLnzWQdgthWNJpTh5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 854 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-904">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل) سایت های رقیبی که خارج از ایران میزبانی میشدند در دسترس‌تر قرار گرفتن، حداقل به یوزری که خارج از ایران بوده پاسخ میداده و هیستوری میساخته...
فکر می کنم بعد از اتصال مجدد برای پس گرفتن جایگاه‌های قبلی باید بجنگیم و تلاش کنیم و احتمالا فورا به رتبه های قبلی برنگردیم.
در کل باید صبر کنیم و ببینیم چی میشه، خیلی دقیق نمیشه چیزی گفت چه اتفاقی میافته و فعلا راه حلی برای این موضوع پیدا نکردیم و از ارتباط با دیتاسنترها هم به نتیجه خاصی نرسیدیم.
ضمنا به دلیل همه‌ی این محدودیت ها تغییر Dns دامنه های ir  هم میتونه چالش های بدتری ایجاد کنه، پیشنهاد میدم کار عجولانه‌ای نکنید.(ممکنه کلا سایت هم برای داخل و برای خارج غیرقابل دسترس بشه)
به امید روزهای خوب
🌺
@danialtaherifar</div>
<div class="tg-footer">👁️ 688 · <a href="https://t.me/danialtaherifar/904" target="_blank">📅 15:27 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQcobWAM-sGfvnheABevOC-_xEJeXiufBwCpAoZ7Dt1X9tv5Rzri_76e5NL_DDVIjrZvACLZQrx274sGJWWVXmNVpgld2Mrd2F0m_pdhgQkW7QJg2YrCsObvj4WRf2B5zFHphleTVx86nRVl8PUQlrnWw-qTww7kFItq8DHP_vjnjEGRurXFJhhqz59-8dkRJQ0QKF23XWsMISorYgbtUHN6mslomjimnONSb0-u4ufZh-EwLuZRC5XAVCD9esB7weTBa4D7Bl7kWvQpPrwkhA7g3uq0uPihASx-LxcLzJVXdlh21kHcrk5NDvhq_Of-20uv9EMFxJvLUcWSHha0rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 888 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pZiW6pVzp75m0vgOwrw3rzH_8fMsplPgB7ZZbZMri0AI4LFLn3eQFv-k8ssRHt9mYIjennNiv1g6Tcy2eHa15ewfSuNgjCWMU8cS9ebdkpz4ucVfFy3zhqFleV7okmHxHZ4g9CGj5Eoanp-x7NT0VK7r0VXrPcMG-xYNY7yrgjOpB4NreGgwsmUt4pxOzl-Tbgk6ba7jC3n20wOLAJ2vxMR-Fw2UL4KoKCWLBTQK1_1HS_rmbKnWlQL5-gN7J9KB09Y3wX7c2d0IQ_Aki8dAMvM3C1OpZPXAMZ1BiJQJJ-wEvZX1bidAgChOjC7n9qMeixiTURq53Nh1R0_WVzKiDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n97CKhaXTQSWEmwUDYrOM57mf-eDcD4Bk8-F9s6uVpPBPv5tQi-qNWU2h3gKxZw8WG41SlbWO3xQS5db4KYO6LBIZFRG7hjL4LF7QrvOVw9qRgSqhaz1Ty0dGaHOIKoQvNaoU4lrCQliuzD_C-NGKxPbAeXKy-y2-u4jtgBYaWublw1vBKwVeuUc8QfoD8ChVwl4lv9pQ90vccJVzuUZDI4KjPFTihcJRRzaklt9GcFbFkOkxTfeMqxbF7xsNetmAq7f1zaN_d9VkChRCSx5JqGL5c3DH-XMUb6o158V-V6RexLpXo8PhIDdEqdu7jxuQuxu6t9OwxppMcNUxNZnlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UbnTJZKS3ADrOnAlRVS1GR3rMWZiwgZXCQkq4csl7GESlm9zlWJRdeKTwN-HNdzGqUA2qYDTa-NertFT8_y_Tgw0UK0ceuOu2_l1n48PBFPIq6vro7URTB9ePR95AOSU32cqdC2rYzE9hp3uz94lo1ksQlYUnM8a4rbbDplQdQZB1cPVAdgOZsWQzPIdZWnLsj2-NEWhiW-Z3VWfqixd0omefsrkkAKX26A2NstzbevdLMTPij4jRecjRHmugVNB0l0SnMkiDtJ1qjpVVzgoGRdZDvs9PqfcpLW6cqhWRBz-afXtSnryKL4196WX4qDOcHZ_wdp1Fst_l1OWQbgdmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G8R2Fm7Dp8CGkmQmf3htGUf-rG2Eop9v8KNkFNu6BLsi_JbgCcQkcBJ0VRT3igHGoeV6sADpLV6g_3BftNBy4EBdsffrh58Xulmh_oE3ex0_uTAek5ClvKPYKJFIBWrap94fZE3_8vHKVzF5xpNyhGE75udrX_6Sgmvl8AHmy0XVXmy8qc-M7k3_cu4QTf6F6TUMsFZhs3cZeWbcqmwu89DHFhgaOtLlxB55-Z4nVCk0vNO1Aunn3gMx-Cpo6RqXPFaIkU9LQh15p52udsMXHgYoQKfHjaZQzHFw8Euzc4fTITrW9hS5yFdISC7cVSZNNaXWDEtWRwIQRiZY6drByg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 979 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRSA3WfycUWWindm01F6uQqze5rG2DHTFmf8ABP--yXHcThKv4HqGVD7AnLGJxOylP2FM1BbzhuLuc9lHnOO8ddThQDCUieDzv8nwyb5P9i6k3dka92QgpFp8MCjz8YV8DQfE9J6jBGp96zckwuyWml2BifpdFFu1N_iCvIoZJ8NhHMZomtlec2s6DuYpfRUAQde_yGXOraAs1r9npGRGxHyiV6Djp7kKxvBlk5-9-zVHxxmnhQB-sdt2iPuV-KRB3HJqZUwXh9zb3eup23BtDo_FvjdSlRKqNYllK9oW_Qe_VALZHlH9Vf-NGR37dXPlHVfZi5im6r6Pk0OU4HJ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 881 · <a href="https://t.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=ZDkFNPrLAPdIgUdZdNa_SZoeJK7wyp59p7CJuHOT6ne1bOYNjquvI0uNIX4e0SR59ZwVfHdoZZxs8k2C09eBX6V4PoJhpBTPgpc8XZtt9ZwEihf_LvSRGHRkobq9qYVC4ojP0ReXcaq1Ss1FbfZ9s5iQXv5VssUfi7rkayPca6BbtqZmc1aOVunmY8SGQ2Ahtf-y6a-OC8kafuxGDn19j-PM0cQuoQ79nvPbVE00-wUP0H1T9W8a5gryjJ71Gl6MZhQprGTLDqHVRE4AnmebFwX-pgCbXaJDHavdbunvDd9kPmjj34RmifuZbaPvWHgcFffVdPUPkheLHUev2Ory2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=ZDkFNPrLAPdIgUdZdNa_SZoeJK7wyp59p7CJuHOT6ne1bOYNjquvI0uNIX4e0SR59ZwVfHdoZZxs8k2C09eBX6V4PoJhpBTPgpc8XZtt9ZwEihf_LvSRGHRkobq9qYVC4ojP0ReXcaq1Ss1FbfZ9s5iQXv5VssUfi7rkayPca6BbtqZmc1aOVunmY8SGQ2Ahtf-y6a-OC8kafuxGDn19j-PM0cQuoQ79nvPbVE00-wUP0H1T9W8a5gryjJ71Gl6MZhQprGTLDqHVRE4AnmebFwX-pgCbXaJDHavdbunvDd9kPmjj34RmifuZbaPvWHgcFffVdPUPkheLHUev2Ory2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اضافه کردن Note به چارت سرچ کنسول گوگل
😉
در آپدیت جدید سرچ کنسول گوگل میتونید به راحتی در بازه های زمانی مختلف Note دلخواه خودتون رو اضافه کرده و ذخیره داشته باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/danialtaherifar/897" target="_blank">📅 17:00 · 26 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKL6NA5G6et-SdQkASAh-lJOW8q0X56K4RNp6yzN3VPbYZh2_cEbLrvUghV6Is6lUg1FTb_AVWI9WYxaO1b8Wop9SWQZXBCXPgWCYozq1nRN1jUwfwiAMTXp4vf12_Z4w3TYu58B3n1-v3zkKbmWEt14ON_O2oDtjbI-0EKJ00jM_LvuAmVjiNzysRm8SxZDdzFUdfercYNlax61OelUrXpnpOn3-LdwGS1JMxw4lXzFVwRgnuQ2cpAeOt7IjcuInl6TYhiG2nVFx9uxm2knOU_pU7EbwSG9eFEcUZm9fNU4Fx-7aSS03iejyiZd50D8qoP0MQimPwhbNMnn8yl9TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
برای دیده شدن در AI Overviews چی کار کنیم ؟
برای حضور در پاسخ‌های خلاصه ‌شده هوشمند (AI Overviews) نیازی به AEO یا GEO نیست! فقط همون سئو کلاسیک کافیه.
📈
سئو معمولی = سئو AI
گوگل تأکید کرده که AI Overviews و حالت AI Mode هم با همان ساختار سئو سنتی کار می‌کنن
🧠
کیفیت محتوا مهمه، نه منبع
محتوای تولیدشده توسط هوش مصنوعی یا انسان، فرقی نداره؛ مهم اینه که «کیفی و قابل اعتماد» باشه
🔄
هوش مصنوعی در همه مراحل سئو دخیل شده
از کرال شدن با گوگل ‌بات تا رتبه‌دهی با RankBrain و MUM، AI به‌طور عمیق در فرایند نقش داره
✅
ویژگی‌های AI Overviews مخصوصه ولی پایه‌ها یکیه
فرآیندهایی مثل "query fan‑out" و "grounding" برای دقت پاسخ‌ها استفاده می‌شن، اما تم همه‌شون سئو سنتی هست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/danialtaherifar/896" target="_blank">📅 18:46 · 02 Mordad 1404</a></div>
</div>

<div class="tg-post" id="msg-895">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">😧
یک نکته مهم قبل از خرید بک لینک های سایدبار که باید بدونید
✌️
زمانی که بک لینک سایدبار در کل صفحات داخلی یک رسانه رو خریداری می‌کنید، اگر اون سایت فرضا 100 هزار صفحه ایندکس شده داشته باشه، بعد از حداقل 3 ماه با ابزار های مختلف مثل اچرفس و سمراش و ... متوجه میشید که احتمالا بین 20 تا 30 هزار بکلینک رو دریافت کردید (ممکنه این عدد کمتر یا بیشتر باشه)، حالا چرا بک لینک های کمتری رو دریافت کردیم در صورتی که اون سایت 100 هزار صفحه ایندکس شده داره ؟
به غیر از موارد تکنیکالی مثل نرخ کراول و ... ممکنه زمان ببره بک لینک ها در ابزار ها و سرچ کنسول ثبت بشه، متاسفانه برخی رسانه ها با روش های مختلف و به کمک
جاوااسکریپت
بک لینک شما رو فقط در یکسری صفحات سایت به
صورت رندوم
نمایش میدن !
برای مثال شما بک لینک
دانلود فیلم جدید
رو ماهانه از یک رسانه با قیمت 5 میلیون تومان خریداری کردید، برای تست وارد یکی از صفحات خبر میشید و میبینید بک لینک شما وجود داره، اما اگر
رندوم
وارد صفحات دیگه بشید، بک لینک شما دیگه نمایش داده نمیشه :)
رسانه ها برای اینکه تاثیر منفی کمتری با فروش بک لینک های سایدبار یا سایت‌واید روی سایت خودشون داشته باشند از این روش استفاده میکنند.
اسم رسانه خاصی رو نمیبرم، اما در خرید این مدل بک لینک ها حتما دقت کنید، بابت هزینه ای که می‌کنید ضرر نکنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 933 · <a href="https://t.me/danialtaherifar/895" target="_blank">📅 10:52 · 31 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mu6huICt9eF1HWMOc7HHKdep3aHBrBeJr1eXz7wWkO49nRSKe1snwVPyIYPgbu3HDaEGBnqB78HGeLFRcmTjW9tbC3uOh8zPaM_-B_bGNalGfFC5bhsmLxj7QlY-rWFgY_IqbYmc7YWJ91Ui_xhJptI24s1_Guh2j3Y7reNE5SzCWdq3r2tGGwFtPEJ68t7AgwXPs7578nYYlFQeQoTQEnRSzFMflZyUMOvFR2CekWO-Z9ocxFUwZgK1pIEy7WST0mSTqcXJtWP-LFoGzPYu5FeZSg071R3xGGTtX_RCzBh5yD6Xeeb7kIk7i1bHwhCNCWYyW7_a6f1etLtiOkQnUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
بررسی آپدیت ژوئن ۲۰۲۵ گوگل: چه اتفاقی افتاد؟
✅
گوگل آپدیت اصلی رتبه ‌دهی خود را بین ۳۰ ژوئن تا ۱۷ ژوئیه ۲۰۲۵ منتشر کرده است. یک تغییر گسترده برای نمایش محتوای مرتبط‌تر و با کیفیت‌.
🔍
چه چیزی در این آپدیت متفاوت بود؟
طبق تحلیل‌ها، این آپدیت برخلاف موارد قبلی، ترکیبی از چند فناوری پیشرفته مثل:
✅
MUVERA (مدل‌های ارتقاء‌یافته بازیابی اطلاعات)
✅
GFM (مدل گراف-محور برای ارزیابی اعتبار محتوا)
رو در الگوریتم گنجانده تا گوگل بتونه:
🔸
محتواهای مفید و مبتنی بر تخصص رو بهتر تشخیص بده
🔸
ارتباط معنایی عمیق‌تری بین کوئری و محتوا برقرار کنه
🔸
تولیدکنندگان محتوا با درک عمیق‌تر از موضوع، ارتقاء پیدا کنن
📌
چی باید بدونی ؟
اگه افت داشتی، محتوای بی‌کیفیت یا قدیمی رو بررسی کن
الگوریتم روی «مفید بودن» و «رضایت کاربر» تمرکز کرده
توی سرچ کنسول دنبال نوسان ترافیک باش
واکنش سریع نکن! اول تحلیل کن بعد اقدام
@danialtaherifar</div>
<div class="tg-footer">👁️ 781 · <a href="https://t.me/danialtaherifar/894" target="_blank">📅 18:37 · 29 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-892">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mzEgjFUkU44tN9A5RFIGexdmdxO4JOOhbb7uCQGH8mDR9hR8xk4mkHRi0SXF8S_y26esC-CIbMyeodeQo-37n65MmTmbxi1VmqoJjjzfZQvUYLKdkguRcmsvzuYr3wZ4iTMON9Ipo7QkXwB1uk-8VgGKq_F0u6xlbnW52-_n_7r16vnqw4CsBzZVLAPQuyWOdHn0jqADYyelpJ5iM-HiwO9r07hyD45zpIAPoZcfm5zszPDqKYmGUYcRkZGzs7LHbxdqR0WSBkocroHnluCEgW6kGJ6lf7yDbwEa9g5z81mjO3Rb-xZ0pt26KolxC_D6YSdVJYBaENGST0cxNodK_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pz7AY7GdHT9o2lO0t6oHHgON0buIQMDonN5s5f5G-EmegMoris5Ja-bM5ETf9VfD5N2FV7djU0Y07SEVMMauGx0JZXvet_5j18DsS1bgxZP0jVqzXGq4O6nweH6wmRapMaQ7Kev4M5YEVbp1wNdggGAbMvGATDYRBUCtYK12lvHP47GhzeGEsnK5MKC8DYKfvyCoMvAkm-G0M4hLSOor0rHCSOXuzaWRzzOOjX7cv0O-4-mGlQw_x0D3QUyJG94J0X5lyqBn15tpnUPk9VK99Vu2r7jm2ur9cbfPd7Hav45tfMfjPNUBDn2hLHwt4Ouvfi5p-Bn3g3DypQ7xiYFmig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن بخش Insights  در سرچ کنسول گوگل
🔍
گوگل به ‌تازگی از نسخه جدید گزارش Insights در کنسول جستجوی گوگل رونمایی کرده است. این گزارش که پیش‌تر به‌صورت آزمایشی ارائه شده بود، اکنون به‌طور کامل در داشبورد اصلی GSC ادغام شده است.
❗️
چه اطلاعاتی در این گزارش ارائه می‌شود؟
1. عملکرد کلی سایت
2. پربازدیدترین صفحات
3. کلمات کلیدی برتر
4. دستاوردهای محتوایی
5. تاپ کشور های بازدید کننده
6. ترافیک سورس های مختلف
🕐
این ویژگی به ‌صورت تدریجی برای تمام کاربران در حال فعال ‌سازی است. اگر هنوز آن را در پنل خود نمی‌بینید، طی روزهای آینده دوباره بررسی کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 802 · <a href="https://t.me/danialtaherifar/892" target="_blank">📅 18:43 · 24 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-891">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">📌
چطور "اعتماد کاربران" روی رتبه سایت ‌ها اثر می‌گذاره؟
یه پتنت جدید از گوگل منتشر شده که داخلش یه نکته خیلی مهم گفته شده:
«
👀
گوگل داره رفتار واقعی کاربران رو دنبال می‌کنه تا بفهمه به کدوم سایت‌ها اعتماد دارن!»
یعنی چی؟ یعنی دیگه فقط محتوا و بک ‌لینک و سرعت سایت مهم نیست...
✅
اینکه کاربرا واقعاً به سایت شما اعتماد کنن و اون رو به بقیه پیشنهاد بدن، یه سیگنال رتبه‌بندی قدرتمنده!
💡
چطور کاربر، سئو رو تعیین می‌کنه؟
📌
گوگل از مفهومی به‌اسم Trust Signal استفاده می‌کنه، یعنی سیگنال اعتماد. این سیگنال‌ها از کجا میان؟ از رفتار واقعی کاربران توی نتایج جستجو! مثلاً:
🔸
روی کدوم سایت کلیک می‌کنن؟
🔸
چقدر زمان تو اون سایت می‌مونن؟
🔸
آیا اون سایتو به بقیه لینک یا پیشنهاد می‌دن؟
🛠
ایده خفن گوگل: دکمه اعتماد!
توی این پتنت اومده یه دکمه فرضی به اسم Trust Button طراحی شده که کاربر می‌تونه با زدن اون بگه:
👌
«من به این سایت برای فلان موضوع اعتماد دارم!»
گوگل این اعتمادها رو جمع می‌کنه و ازش یه "رتبه اعتماد" برای هر سایت می‌سازه.
سایت ‌هایی که بیشتر مورد اعتماد قرار بگیرن، در نتایج بالاتر می‌رن!
🔝
📈
یاد بگیر چطور اعتماد بسازی!
✅
محتواهای واقعی، کاربردی و انسانی بنویس
✅
کاری کن کاربر حس کنه که وقتش تو سایتت تلف نمی‌شه
✅
با جلب رضایت کاربر، اون رو به یه طرفدار وفادار تبدیل کن
✅
کاربران خوشحال = سیگنال اعتماد قوی = رشد رتبه در گوگل
🚀
@danialtaherifar</div>
<div class="tg-footer">👁️ 990 · <a href="https://t.me/danialtaherifar/891" target="_blank">📅 16:02 · 10 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-890">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQefQJ3iuzYixUy3HmHmHoYgtChmY2PIvMNddC_3ywV6trmfe53Qe7XpPEzDMp_PdlT5pk5ML8ChSx0VJd1DResMVQHXpJ8-e5liCo9dlPjrcchA0LKvUuo8-eeUgV4hXcnKkDwau_YJWJpQW8u3SPDceqVMCYCRigQv5bOH0Dqhp3OQl4OSBtz1SIQOXLaHO8p3ARFEivZ0ruvWk8w5N2GHy12kQ83CZL9ZHh5E6sPLOrGiyVY1Q7hUHkoFRXjydHgr0TIR9IKdPu3ksNEB8IWkZuKgsFsjgswAjokNQ_Zzxgib-Y6D74VUBYPRdhbprdNRIHEl6XlQAawiKaIg-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
گوگل: ترجمه خودکار رو دیگه با robots.txt نبند!
📰
گوگل به ‌تازگی بخش‌هایی از مستندات robots.txt خود را حذف کرده که قبلاً توصیه می‌کردند برای جلوگیری از ایندکس صفحات ترجمه ‌شده خودکار، از robots.txt استفاده شود. این تغییر باعث هم‌خوانی بیشتر مستندات فنی گوگل با سیاست‌های مبارزه با اسپم شده است.
❓
چرا چنین توصیه‌ای قبلاً وجود داشت؟
هدف اولیه این بود که سایت‌ها بتوانند صفحات ترجمه‌شده (اغلب توسط ابزارهای اتوماتیک) را از دسترس ربات‌ها خارج کنند تا از ایندکس محتوای مشابه جلوگیری شود.
اما اکنون گوگل این راهنما را حذف کرده، چرا که ترجمه خودکار همیشه نشانه محتوای اسپم نیست و نباید به‌صورت پیش‌فرض توسط robots.txt بلاک شود.
گوگل حالا تاکید دارد که تضمین کیفیت ترجمه (کیفیت انسانی یا پس از ویرایش) اولویت دارد، نه محدودیت‌های فنی.
استفاده از متاتگ <meta name="robots" content="noindex"> برای کنترل ایندکس
یا استفاده از attribute هایی مانند notranslate برای جلوگیری از ترجمه خودکار و کاهش اشتباهات ایندکسینگ.
@danialtaherifar</div>
<div class="tg-footer">👁️ 925 · <a href="https://t.me/danialtaherifar/890" target="_blank">📅 11:25 · 22 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-889">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOoUPkPC_21EcTrEY7LUDXvAgS2bRuI6SwrYqXFJiN9PBi7NV-PHIK9iSnjU4GMEX1-wI1IJTRgaUPGYOCRe1UJOIH1Kv27_c_3_K1oXwu8FmpcINJWWyXbnZT3h3VK_6QehnfdDaQHS7jabhw6jbUEOPzDIbK_E3tJ1rhcvM2tOa9UQ_epbA1oh3_iKzd4UY4EUVqfOmTYNcHbEggHpS6WwbBI3Jn3m1yfCiOIVbh6USYiJv0f-rvQhwIkKTf4uaIB1fpBhMXnpmgz11b1jaWBOkR5e0zxE9s8iZOLsLoMaKtnXXfZNkRqm0XiXdzNoeW1LzECWnFyNE9uENBNSoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
نوسان شدید رتبه‌ گوگل در ژوئن ۲۰۲۵
🌪
در ۴ ژوئن ۲۰۲۵ شرایط بسیار ناپایداری در نتایج جستجوی گوگل مشاهده شد؛ ابزارهای معتبر رتبه‌ بندی مثل Semrush, Mozcast, Sistrix و متخصصان سئو متوجه نوسان شدیدی در رتبه صفحات سایت‌ شون شدند.
❓
آیا بروزرسانی رسمی بود؟
خیر، تاکنون گوگل تایید رسمی نداده که یک آپدیت انجام شده باشه، آخرین مورد رسمی، بروزرسانی هسته در مارس ۲۰۲۵ بود. با این حال، از آن زمان تقریباً هر هفته نوسان دیدیم؛ این بار اما شدتش بیشتر و زودتر در هفته بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 746 · <a href="https://t.me/danialtaherifar/889" target="_blank">📅 12:03 · 19 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-887">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pgGiUbjrt11m2LYSqVxn2qwFQTWl41kfeW7RSEAduC40HhZiPOysQ80SwvNgxexwWjFMoSP1LaW5MmqaOr__dXa0npI4vFEFRisrrgDrf1ddKHS4bbCDli5Vnr-7JL1tawnj9iZck3dvSLa3n85F_8yXqo_nmuuJ6fHKfQ8fVoHYl7lg0VFSIAVLukUgxgd7iIYwmX--cMn0ccT0MTJ6r1qPhzwbdYW_htFOamjn2SpIEEStJTzHlSiuIeiygJ2wVnOYO8SVz5NOuzT9ji09CikuHmnJyOiEiFvkZlSAY8qZS0klFXtKrfpSIUd2CQNXQbD-_4spkrN-affynk9jpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GzGmI_n_vQ-a1MZGP0dF2Ib__dAPjYOo7gI1JxswPg3bbP8v3L4uD8JhHl1fgP5hQ6EcQhwazZGWMXghd2GmPfOtgQwZdEur_efPZkFnQCC408oTa0ve-WRX8EdXqwJwIeIZjyuPaK0_m0qKszYyAAFcfu_2Uii1rfrbf5U_ZGPb2jc1HtsbMalblKrar1KlydnZHFTgp1mpLRLHjnNO0O34s9599uekJ8suCuTAy5ASLafvO3kjGO0dgWk3hYOmYbgVoYGKFyKWLh5gr4JoaucOHZA6jJMsY3PqwmRfSAvPxQS0C6eZnbV34f59HgeLK75xR-c7M5Vn6w4iEskcKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📢
آپدیت جدید گوگل برای داده‌های ساختاریافته Event و Recipe
گوگل به ‌تازگی مستندات Structured Data یا همون داده‌های ساختاریافته رو برای دو بخش مهم یعنی رویداد (Event) و دستور پخت (Recipe) به‌روزرسانی کرده، تغییراتی که می‌تونه روی نمایش سایتت توی نتایج گوگل اثرگذار باشه.
👇
🔸
تغییرات در داده‌های ساختاریافته رویداد (Event)
✅
گوگل حالا به‌طور دقیق‌تر توضیح داده که چه نوع رویدادهایی می‌تونن در rich result بخش "Events" نمایش داده بشن.
❌
مهم‌ترین تغییر: ویژگی‌های مربوط به «رویدادهای آنلاین» دیگه پشتیبانی نمی‌شن!
📍
فقط رویدادهایی که در محل فیزیکی برگزار می‌شن و قابل رزرو برای عموم مردم هستن، شانس نمایش در نتایج Google Events رو دارن.
🔸
تغییرات در داده‌های ساختاریافته دستور پخت (Recipe)
📌
گوگل رسماً اعلام کرده که ویژگی image داخل داده‌ی ساختاریافته Recipe،
هیچ نقشی در انتخاب تصویر نهایی در نتایج جستجو نداره
😮
🔍
اگه میخوای تصویرت توی نتایج نمایش داده بشه، باید:
✔️
تصاویر با کیفیت، سبک و بهینه داشته باشی
✔️
باید alt-text و context مناسب برای تصویر قرار بدی
@danialtaherifar</div>
<div class="tg-footer">👁️ 756 · <a href="https://t.me/danialtaherifar/887" target="_blank">📅 15:07 · 16 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-886">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NuiBhRlcNOcsxC_5e3Aoh6LyYA7op7x_y0KSzLeCXhBoolfBfSaYlNHila2Pl8A7Ckc2jcgXkMwoG1KGJfG1Rh8HwgGYs6cnLVSJ0K5A80hZ7OJgUqnjkK-cCE6r6BVgD-qW_W_epETtjoRTvD-XbgXe1z5rDIKdeQiY8Vj1SGUsUsCS1JxYj7J21bNZzUEhH_gw7NfMs_kWMJDNCfkUkc9zA8a9O7jmdhqrYEC9YRweeVsTzzCX1RKscUNZ7P3qBG9RUgGDyhUoUu5b-7kuVYntAQm-KksKpzJGdsAl9JjMYPAHxFl_MhvLc054gCKjKw03XLXQ5z3l8ZoSm16pdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل سیگنال‌ های زمینه‌ای رو به نتایج جستجو اضافه می‌کنه
📌
‌ پتنت جدید گوگل نشون میده که قراره جستجوها خیلی دقیق‌تر و هوشمندتر بشن! دیگه فقط کلمات کلیدی مهم نیستن، گوگل حالا به شرایط و رفتار کاربر هم توجه می‌کنه!
📍
گوگل به موقعیت و زمان هم توجه می‌کنه!
فرض کن شب جمعه ساعت ۸، سرچ می‌کنی "پیتزا"
🍕
گوگل ممکنه بفهمه دنبال سفارش آنلاین پیتزا نزدیک خودتی، نه تاریخچه پیتزا!
😳
یا اگه بلیط یه فیلم رو خریدی و بعد اسمش رو سرچ کردی، احتمالاً دنبال تریلر یا نقدشی، نه یه بلیط دیگه!
🔁
بازنویسی هوشمند کوئری‌ها
🧠
گوگل با استفاده از داده‌های مختلف (مثل مکان، زمان، سابقه سرچ‌هات) می‌تونه کوئری‌ تو بهتر بفهمه و حتی یه نسخه دقیق‌تر ازش بسازه تا نتایج بهتری بهت بده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 670 · <a href="https://t.me/danialtaherifar/886" target="_blank">📅 14:06 · 14 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-885">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔍
جستجویی که می‌فروشد!
🤔
تا حالا فکر کردی چرا بعضی از سایت‌ ها با اینکه رتبه‌ی خوبی تو گوگل دارن، باز هم فروششون تعریفی نداره؟ یا برعکس، یه سایت شاید رتبه اول نباشه ولی همیشه مشتری داره!
🧠
واقعیت اینه که رتبه بالا فقط یه تکه از پازل موفقیت در سئوئه!
📌
این 4 تا نکته بهت کمک میکنه که بیشتر بفروشی
:
👇
1️⃣
هدف جستجوگر رو بشناس!
فقط به کلمات کلیدی نگاه نکن، بفهم چرا کاربر اون عبارت رو سرچ کرده. مثلا "کفش مردانه" یه جستجوی کلیه ولی "خرید کفش مردانه راحتی" یعنی آمادگی برای خرید!
👟
🛒
2️⃣
محتوایی بساز که بفروشه!
یعنی چی؟ یعنی محتوا باید مخاطب رو به قدم بعدی هدایت کنه:
ثبت‌ نام
📩
، خرید
🛍
، یا تماس
📞
. نه اینکه فقط اطلاعات بده و ول کنه بره!
3️⃣
داده‌ها رو جدی بگیر!
با Google Analytics و ابزارهای سئو بررسی کن که کدوم صفحات بیشتر تبدیل دارن. شاید یه مقاله تو رتبه ۳ باشه ولی دو برابر بیشتر بفروشه از رتبه ۱!
4️⃣
تجربه کاربری = کلید تبدیل
!
🔑
سرعت سایت، طراحی زیبا، دکمه‌های فراخوان (CTA) واضح… همه اینا کمک می‌کنن بازدیدکننده‌ها تبدیل به مشتری بشن.
🧭
🎯
فرمول طلایی موفقیت در سئو:
رتبه خوب + محتوای هدفمند + بهینه‌سازی تبدیل = فروش بیشتر
💸
🗣
پس دفعه بعدی که داشتی رتبه‌ات رو چک می‌کردی، این سؤال رو هم بپرس:
"این رتبه داره برام پول می‌سازه یا فقط دلمو خوش کرده؟"
😉
@danialtaherifar</div>
<div class="tg-footer">👁️ 813 · <a href="https://t.me/danialtaherifar/885" target="_blank">📅 13:22 · 07 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-884">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔍
نگاهی به سیستم‌ های رتبه‌ بندی گوگل
👇
این اطلاعات نگاهی نادر به نحوه ارزیابی کیفیت صفحات، سیگنال‌ های محبوبیت و نقش داده‌های مرورگر Chrome در رتبه‌ بندی نتایج جستجو ارائه می‌دهد.
🛠
سیگنال‌ های ABC: پایه‌های رتبه‌بندی
گوگل از سه نوع سیگنال اصلی برای تعیین ارتباط محتوا با جستجوی کاربر استفاده می‌کند:
A – Anchors
: لینک‌هایی که به صفحه هدف اشاره دارند.
B – Body
: وجود کلمات کلیدی مرتبط در متن صفحه.
C – Clicks
: رفتار کاربر، مانند مدت زمانی که در صفحه می‌ماند قبل از بازگشت به نتایج جستجو.
🔹
این سیگنال‌ها به صورت دستی تنظیم می‌شوند تا الگوریتم‌های رتبه‌بندی قابل فهم و قابل کنترل باقی بمانند.
📄
کیفیت صفحه: معیاری ثابت و مستقل از جستجو
کیفیت یک صفحه، که نشان‌دهنده میزان اعتماد و اعتبار آن است، به طور کلی مستقل از جستجوی خاصی است. این معیار به صورت ایستا در نظر گرفته می‌شود و برای همه جستجوهای مرتبط اعمال می‌شود. با این حال، در برخی موارد، اطلاعات مرتبط با جستجو نیز می‌تواند در ارزیابی کیفیت صفحه تأثیرگذار باشد.
🤖
سیستم eDeepRank: استفاده از مدل‌ های زبانی بزرگ
سیستم eDeepRank از مدل‌های زبانی بزرگ مانند BERT برای تحلیل محتوا استفاده می‌کند. هدف این سیستم، تجزیه سیگنال‌های پیچیده به اجزای قابل فهم‌تر است تا مهندسان گوگل بتوانند دلایل رتبه‌بندی صفحات را بهتر درک کنند.
🔍
سیگنال محبوبیت مبتنی بر داده‌های Chrome
یکی از سیگنال‌های رتبه‌بندی، که نام آن در اسناد محرمانه باقی مانده، از داده‌های مرورگر Chrome برای ارزیابی محبوبیت صفحات استفاده می‌کند. اگرچه جزئیات این سیگنال مشخص نیست، اما وجود آن نشان می‌دهد که رفتار کاربران در مرورگر می‌تواند بر رتبه‌بندی نتایج جستجو تأثیرگذار باشد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 821 · <a href="https://t.me/danialtaherifar/884" target="_blank">📅 14:38 · 31 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-883">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/danialtaherifar/883" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📌
پتنت Site Quality Score چیه؟
🧠
پتنت شماره
US9031929B1
یکی از روش‌های گوگل برای سنجش کیفیت کلی یک سایت در نتایج جستجوئه!
💡
تو این پتنت، گوگل با استفاده از نسبت بین:
🔍
تعداد جستجوهایی که به یه سایت ختم میشن (مثلاً سرچ "ویکی پدیا")
👆
و تعداد کلیک‌هایی که روی اون سایت تو نتایج زده میشه، یک امتیاز کیفیت سایت (Site Quality Score) محاسبه می‌کنه!
✅
نتیجه ؟
افزایش جستجوی برند + نرخ کلیک بالا = امتیاز کیفیت بالاتر = رتبه بهتر تو گوگل!
@danialtaherifar</div>
<div class="tg-footer">👁️ 721 · <a href="https://t.me/danialtaherifar/883" target="_blank">📅 17:13 · 29 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-882">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXwiIpWWN5WjLrbW0J6GDONwt0If0_Ew3a50BBBpnFFstLu3v0pDXoST5NMcvWVWXgeRkcNOsirbD3LPyAybYasSL_qWpjzVkrR7lSe2lSZXYbpAMZXXKhWg7wKkXmTN4AOG9AY6JtSxJYcygBCGZVIra2iG_VBQiQmo2S5dU60KZI0lKSO4XcSfwXYW2_vdwFtdxkVMEaobuwIvwDe55p6zYuLT7aHy6axRfvBtx11IwrydNEB16aPl0H10EFKapyfctteQXM5uSbqYFrA9uWdLlC_ezjlxZUlrtMiLSy9bWlp0Td_9O3qZpv05WYY-UKwz1YERpDWiEh6XoWi8Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
رتبه‌ی یکسان برای همه لینک‌ها در بخش AI گوگل
📈
گوگل بالاخره تایید کرد که لینک‌هایی که توی بخش پاسخ هوشمند (همون AI Overview) در نتایج جستجو نمایش داده می‌شن، همگی با هم یک موقعیت یا رتبه در کنسول جستجو ثبت می‌شن!
🤔
یعنی چی؟
یعنی اگه توی یه AI Overview چند تا لینک از سایت‌های مختلف نشون داده بشه، همشون با هم یک Position حساب می‌شن. فرقی نمی‌کنه لینک اول باشه یا سوم؛ گوگل بهشون یه رتبه‌ی مشترک می‌ده.
🔍
چرا این مهمه؟
📉
ممکنه باعث بشه نرخ کلیک (CTR) سایتت بیاد پایین! چون:
خیلی از کاربرا جوابشون رو همون توی AI Overview می‌گیرن،
و دیگه روی لینک‌ها کلیک نمی‌کنن!
😕
📌
گوگل چی میگه؟
الان هیچ دیتای جداگونه‌ای برای AI Overview توی Search Console نشون نمیدن.
همه لینک‌ها با همدیگه یه رتبه دارن.
فعلاً هم برنامه‌ای برای تغییرش ندارن
😬
@danialtaherifar</div>
<div class="tg-footer">👁️ 822 · <a href="https://t.me/danialtaherifar/882" target="_blank">📅 15:14 · 27 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-881">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVLcWAy2xCG3GUEPcTcYNZsH5Dqgnz1auvbyhtz7TbTKQiNDASA6Oz5Yh1Ipywrlti7u2pTyBdeUSsnvAeNRaqI5XhZvGfkfPEIdU8HCaogO_HQPZbuHG7b8H_GiQjCeyzvJaITyZbSflq8Pp7Dp1UrCxLjbYQwDMO7kEuAlqVq-rOPCzbnsL-RHfUiBmNbEeu2XuBaz2xqnIW2q8RXLubdWaL3SiLqYxMZDLuL7Ub6sqVKHetjArW2e4xTkJG7cXxa3yP01shNK4wEX7o2TmZTxv5kA_NQ-berRrP1DMtoQ8kq4O0jTSAhf6LGzJu3QPn__1-t7007xFcXvb4-UAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل: Navboost یک سیستم یادگیری ماشین نیست!
در تازه‌ترین افشاگری‌ها پیرامون سیستم‌های رتبه‌بندی گوگل، یک نکته بسیار مهم روشن شد:
سیستمی به نام Navboost که تصور می‌شد یک الگوریتم هوشمند باشد، در واقع هیچ ربطی به یادگیری ماشین (Machine Learning) ندارد!
🔍
اما Navboost دقیقاً چیه؟
👨‍💻
به گفته‌ی دکتر اریک لِهمن، از مهندسان سابق گوگل:
بیشتر شبیه به یک جدول عظیم از داده‌های کلیکی کاربران برای کوئری‌های مختلفه؛ اطلاعاتی مثل تعداد کلیک‌ها، امتیازات و چند فاکتور ساده‌ی دیگه.»
🔸
یعنی به‌جای اینکه تصمیمات بر اساس هوش مصنوعی گرفته بشن، این سیستم صرفاً داده‌هایی مثل "چه کسی روی چه لینکی کلیک کرده" رو جمع‌آوری و نگهداری می‌کنه.
🧠
سیگنال‌ های رتبه‌بندی؛ دستی نه هوشمند!
🧩
بسیاری از سیگنال‌هایی که در رتبه‌بندی نتایج جستجوی گوگل تأثیر دارن، به‌صورت دستی توسط مهندسان تنظیم شده‌اند.
گوگل از توابع ریاضی مثل sigmoid و مقادیر آستانه برای ساخت این سیگنال‌ها استفاده می‌کنه؛ نه از مدل‌های پیچیده‌ی هوش مصنوعی (جز در مواردی مثل RankBrain و DeepRank).
@danialtaherifar</div>
<div class="tg-footer">👁️ 604 · <a href="https://t.me/danialtaherifar/881" target="_blank">📅 17:42 · 25 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-880">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lh-hwYU9IZ3ZuE1UY10cOHDPz6fmXo4Ve4Q3bvAA4uQB6P6YwYmaqJj0do2CcbDdVJC7LrRwEoo7p5osrD17fM8NBmfREMqezFMEdj5tgJEyCHWC2IifB2EsDU8BmIE8d9DjE7nBC5Ji93lZt47PnFkqc-zn_B98Sq3RUBdEWV6T7uoMkPyMeTGuaSQ1L5C46QhWH8Sk-FbbpoEfoE2rMp0-ThRILit6Fau6XF4CewDd_6ZmxbMqjn5dIbaQlo03yXRWsfr30_7fyj3edZUZhQObK68tfqBD7cIs4KQ6z5WzSPmOBKKipakGqpScOuX8bLg00WnbMLKJeE8OFx5PNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
چطور توی Google Discover بیشتر دیده بشیم؟
🔹
۱. محتوای با کیفیت بنویس
📌
فقط نوشتن کلمات کلیدی کافی نیست، محتوات باید واقعا مفید، مرتبط و جذاب باشه تا گوگل بهش توجه کنه.
🔹
۲. از عکس‌های باکیفیت استفاده کن
🖼
عکس با عرض ۱۲۰۰ پیکسل یا بیشتر؟ عالیه! چون باعث میشه کارت تو Discover بهتر دیده بشه و نرخ کلیکت بیشتر شه.
🔹
۳. موبایل فرندلی باش
📱
بیشتر کاربران از موبایل استفاده می‌کنن. پس سایتت باید سبک، سریع و بدون مشکل تو گوشی لود بشه.
🔹
۴. داده‌های ساختاریافته فراموش نشه
🧩
با استفاده از
Schema.org
به گوگل کمک کن بفهمه محتوات در مورد چیه. همین یک کار ساده باعث رشد دیده‌شدن میشه.
🔹
۵. حتما E-E-A-T رو جدی بگیر
🏅
هر چی اعتبار سایت و نویسنده‌ت بیشتر باشه، گوگل بیشتر بهت بها میده.
🔹
۶. سراغ ترندها برو
📈
محتواهای داغ و به‌روز توی گوگل دیسکاور شانس بیشتری دارن. اگه خبری یا موضوع جدیدی هست، سریع پوشش بده!
اگه می‌خوای تو Google Discover بدرخشی
💥
باید محتوای فوق‌ العاده جذاب و تجربه کاربری عالی داشته باشی.
@danialtaherifar</div>
<div class="tg-footer">👁️ 697 · <a href="https://t.me/danialtaherifar/880" target="_blank">📅 19:13 · 24 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-879">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔎
چارچوب Triple P در دنیای جست‌وجوی هوش مصنوعی؛ حضور، ادراک و عملکرد برندها
🌐
✨
📌
در دنیای دیجیتال امروز، موتورهای جست‌وجو با کمک هوش مصنوعی به سطحی رسیده‌اند که فقط نمایش لینک نیستند، بلکه تجربه‌ای هوشمندانه و تعاملی را برای کاربر خلق می‌کنند. حالا دیگه وقتشه برندها با رویکرد جدیدی به سئو و دیده‌شدن نگاه کنن!
👀
اینجاست که چارچوب Triple P وارد می‌شه:
✅
1. Presence (حضور)
🔹
آیا برندت تو نتایج جست‌وجوی هوش مصنوعی حضور داره؟
🔹
تو مدل‌های جدید AI مثل Gemini یا ChatGPT، دیده می‌شی یا نه؟
📍
حضور برندت تو پاسخ‌های تعاملی خیلی مهم‌تر از قبل شده. دیگه فقط لینک اول گوگل کافی نیست!
🧠
2. Perception (ادراک برند)
🔹
چطور مخاطب وقتی اسم برندتو تو پاسخ‌های AI می‌شنوه، نسبت بهش حس پیدا می‌کنه؟
🔹
آیا برندت قابل‌اعتماد، معتبر و پاسخ‌گو جلوه می‌کنه؟
📢
هوش مصنوعی بر اساس داده‌هایی که از برندت داره، درباره‌ات نظر می‌ده! پس محتوای درست و دقیق تولید کن.
🚀
3. Performance (عملکرد)
🔹
آیا حضور و تصویر ذهنی برندت در نهایت باعث کلیک، خرید یا تعامل می‌شه؟
🔹
چقدر از پاسخ‌های AI به سود واقعی برندت منجر می‌شن؟
📊
حالا دیگه اندازه‌گیری عملکرد تو جست‌وجوی AI فقط به کلیک محدود نیست، باید ببینی خروجی چیه!
✨
چرا چارچوب Triple P مهمه؟
چون در عصر هوش مصنوعی، برندهایی که فقط به سئو کلاسیک تکیه می‌کنن، عقب می‌مونن. برندهایی برنده‌ن که در جست‌وجوهای هوشمند هم دیده بشن، درست فهمیده بشن و نتیجه بگیرن!
📣
اگه هنوز به‌روزرسانی استراتژی سئوت رو با تمرکز روی AI Search شروع نکردی، الآن بهترین زمانشه!
@danialtaherifar</div>
<div class="tg-footer">👁️ 640 · <a href="https://t.me/danialtaherifar/879" target="_blank">📅 12:17 · 23 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-874">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MVXHKhK2AgVr4JmsFFZ6GIfrxSBArDFrsVKLK6ThLToLoW5d5oZZoq47XCvu65IyN1BSvOpulmtC5T3l2UN8pfRmsGz78Viu5eE5kcjEs63XD939K37nGJcaddHc3zBJoihV9ASqXRMd36_F2D-iMfnfg1NgKmZQupOtNUEEcxNFCBKA1-NDSF5MkRmUs2DH_hsufqSnaRGg7GnrnPFfP62ZaDVenJ8pv8J67-MqbrgcutjeU7zaO5X_FW_7sA1FESg6FdfU2pxIoVXffUM-hUEX-FLaDL_cxcCrkbyo-ECxySfUFuMnjSnGZUefjbXqFR-x_f2J8ADu9I84-kZ5aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ab0SZ_cTnuGUC-rf-hVvclEU59vHWTWZsnpTNTkbw467zrVDT0YnumzxbuZm4FDCFrBIZKt2_X-1iBrP6fMr8U04Ys3rcjq3eUMyjDWO9bdqz6aurHzAmbsgHhuzdq-P4pn6ZRIQs8mlFJGNzYmdmY8sD11LsZ6QsLOrwMeBosjayylcBnuSdJNKlbAHpOL0QjQNA_rDiLpNBngQRNMTr6T3ETv2EOPs6_c3ONBKGByrNQAW8wPDkdpPGutU6q2Ut9Ad3NstRndDHush_pTmITI75lYl0J7Pd0-gnwpj4kJzOuQFpmbcq00lAyvX44nTvh-ioZWg8k1A0XNJQj00hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TI2dkyNcmJrkyUDyTns_X6tY6ypvwN_Lg-hWGQJajvSiqpb3p_olZZRvPJwaMZw5iaPDihKlYzPIW5PEda6T7fWg-ZTz1bgsK42D3XGWgSKz5UfB-Xq8fqpU9dhyUhsk3F0RBZn-UukVI1OoPJ12JSkDgMhjYt_Za3Igenu30KZ2e8IjuwBOXUMILzCOmAX6gbwYfjja32U98ksa3nQw_nQWNccMtD7vj1HgkUw2e7Vqo3NRoGRSikOiweU6-90_q-nIqbHrz_Jxi5m89Evcp2RB3GmcQFaJ80vN9BEB7Qn59mwKH1eyAXCezx9wOZmZ4YTWc6GeDsWlpNY6mFJFNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dCuvs6DJfbRPFT_KepikQBPV7xhWYYiVRnmpPxzlXU64QCp_N2W8q4IG2q6Ft-aMa2IenqG7_CQiEXxGUiaylRvBM1nV5JaUwSWzSu8yAk9EyhU5k2Ok9j5Jsco8OFI069gCkgGspPzgc_LvRuFTPn97CO1KhATL_C0z4w8fSUIDuSiZ-OlkNIU2DgwQKu3iS9P1AKawxa_gTn2ZS1_iwYrsC5cZVwUw1HRGml9zm9PvvhfGlYLWrlgDRJm1Z_NzZchhZloC3m96gzsXCNpzRnqHUn30rOMl1sqQl9qgy7ojtWN-DPkjSC3_UKSGcqbI-6dt2Jh3ZGNERLNByWfyfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ia9YOO3jac4CFU5yRvjhQP_fwB2ZcldC3nsYddsQhrZ5cGoxAWufkbQ9PMcrvvY4ogiInFLilnXuDlbLX1xzGZ2dPiwGhvm7se7kd3tXd00ogzAYa_c5qpdyF9V1iIYK_pdLR18YZmMUeufRBSYTKexfYIV57Wjt7mO7xIqdCJ-MEtbZfdqFKJcuatCLnrXWsrWSxb5jV96Dif5ocLMd2rm51__odJ_cdZqVq8ArUyb3vv6WUvsXBJL9ORNlhaxzmDfncudFgy4vYL58uwTruKRVMeZzqRdKvp7-5r1_15h18j3UKMTtAUGDFLPcLgnUFN7tVZZUDj6wJTeHaL3G-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 785 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4rynuIiQO5TD8EE2aF6Q83lxgcBmqxFzWLKRgjqsbzkm3Nn2L7wClbG-CryZeGBEDDPu6BlzrVrmzwIg5I3p4XBEu9TNO7jVeQAThMfsCsq4fByq6LcKSQyI8vA0cMcefcAzcSX2xdrANpkZgQzAfVLA5s9my3ol4V-1yCCUWxxzC9L3auTgIOLCs_hSGBArFEGP9unNH98OacdSIQe_2jwPbpFv5H09R8s4I2t1ReG7-kQ1-LKgQw8cdqmfNlMamIo6aOV5FZNqIxGm5uMn2CbYS6Y2rpzCksvQ34SjIP-7jYrTUaOnTyJGatkLBrT_sW1Yk_0JIDgVu8AZTVKRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:
1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.
2. تعداد جستجوهای نام برندهای رقیب را نیز جمع‌آوری کنید.
3. مجموع جستجوهای برند خود را بر مجموع کل جستجوهای برندها تقسیم کرده و در 100 ضرب کنید.
🎯
مثال: اگر برند شما ۲۰٬۰۰۰ جستجو و سه رقیب اصلی به ترتیب ۱۵٬۰۰۰، ۱۰٬۰۰۰ و ۵٬۰۰۰ جستجو داشته باشند، سهم جستجوی شما:
20,000 ÷ (20,000 + 15,000 + 10,000 + 5,000) × 100 = 40%
💡
چرا باید بهش اهمیت بدیم؟
🧠
بهت کمک می‌کنه بفهمی جایگاه برندت تو ذهن مخاطبا کجاست.
📈
یه شاخص عالی برای پیش‌ بینی رشد یا افت بازار در آینده‌ است.
🔧
می‌تونی استراتژی‌های سئوت رو بهینه‌تر کنی و رقبا رو پشت سر بذاری!
@danialtaherifar</div>
<div class="tg-footer">👁️ 581 · <a href="https://t.me/danialtaherifar/873" target="_blank">📅 16:16 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-872">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0Pusb0CgADAdLrH9qIT2BIoapKslKvxgW777ui0bGRmpUcCSFFVvXT23if1vsTYfa5OYStXzpp5hFuTgcWe4Kq719JUhx0iNtRoHHuAsqqvEThMJPKWLsinC94W0pKi02Z3Hfdc-x9Yi1vQOoHoUytmXmzlRvtloS_y5rPnhwIjZUUSpGcZQMTawGCBXDM4YEDI9K8pWaH5X3dYx8fXLX5WvWe_Qt0kQKhS5Wj_z_g_6D75hLy9eTDUpztwr3EWXcTHjmRKb9h3N7YV1QbNSTKMe9fFhVAwzdIxWrUVQVehtHmNqeN-vcr9QeA-TfIItTWWamSw5LR86WoOyRSsJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
نحوه استفاده از پارامترهای زبان و کشور در جستجوی گوگل
اگر به دنبال راهی هستید تا نتایج جستجوی گوگل را بر اساس زبان یا کشور خاصی مشاهده کنید (مثلاً فقط نتایج فارسی برای ایران)، گوگل راهکاری ساده اما بسیار کاربردی در اختیارتان گذاشته است. کافی‌ست از دو پارامتر ویژه در انتهای لینک جستجو استفاده کنید.
🛠
تنظیم زبان و کشور در URL جستجو
&hl=کد_زبان → مشخص‌کننده زبان رابط کاربری (مثال: &hl=fa برای زبان فارسی)
&gl=کد_کشور → مشخص‌کننده کشور هدف (مثال: &gl=IR برای ایران)
💡
مثال کاربردی:
https://www.google.com/search?q=دانلود+فیلم&hl=fa&gl=IR
🎯
مزایای استفاده از این قابلیت
✔️
مناسب برای تحلیل سئو بین‌المللی و بررسی نتایج در کشورهای مختلف
✔️
مشاهده دقیق‌تر نتایج کاربران در زبان‌ها و مناطق متفاوت
✔️
قابل استفاده برای تولیدکنندگان محتوا، بازاریابان و متخصصان دیجیتال مارکتینگ
✔️
بدون نیاز به تغییر تنظیمات مرورگر یا حساب کاربری گوگل
@danialtaherifar</div>
<div class="tg-footer">👁️ 593 · <a href="https://t.me/danialtaherifar/872" target="_blank">📅 18:11 · 20 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-871">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skN4cQI5QNBIW2VsZXwJ6r4BCQL2smiWpmI2PmzPVfHj105JCUODoPL4WNTgEnGY6m3xun2SxqkX6bIV_rmcvM5m5u4Gj7J9d_o_F-M-eyVq8ShqzNzN22ciIEmsDzUq3e_4lAo4YJr7JyORS_wLyxFTaNMJQzhMyaKXPDkfL8QEG9d9DtEpa9QDBDI7TiYMtu0nKK9gkFyzsySE0p8N0irA0ZADU4M-sTJkU4GyvZqXE50ktmehoK5JliPx0htE-9k0aVJt7on1A-w-A7a2jdHNUVBA8Ads3qmJKVCqV1tF3x6sHbZIOCstwxlp0isDe8-3qSHrtQvj1XQ0XPwWuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گوگل علیه محتوای فیک E-E-A-T وارد عمل شد!
گوگل توی آخرین آپدیت دستورالعمل‌های ارزیاب‌هاش، تمرکز ویژه‌ای روی مقابله با محتوای تقلبی و مخصوصاً محتوایی که به‌دروغ نشون میده تجربه یا تخصص داره (E-E-A-T) گذاشته!
🧠
چه چیزایی تغییر کرده؟
🔹
محتوای دارای تجربه واقعی اولویت داره
🔹
اعتماد مهم‌ترین عامل برای رتبه‌بندیه
🔹
تولید محتوا با هوش مصنوعی بدون بررسی انسانی = خطر سقوط توی سرچ!
📌
نکته مهم برای سئوکارها و نویسنده‌ها:
اگر تجربه واقعی، منابع معتبر و شفافیت نداشته باشی، گوگل دیگه باهات شوخی نداره!
😅
@danialtaherifar</div>
<div class="tg-footer">👁️ 701 · <a href="https://t.me/danialtaherifar/871" target="_blank">📅 13:08 · 17 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-870">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEORzxmPyUWRrdjQ427HvtXyVFECwxQ32AJOJI3e7AzCK5FyaR0p1woxQVUdaWnjyfz7PKvvbd6KNFR-BZsUgVtSm5l-WE5KPd9HDbeiZ8q0t0cXBf9piJBlAq3K5rv_qfxKB2UQnF5rc83Ubjke9Zu1EH83wVmrV4hU705tOYSb1sodIdqODTYkWDOgWBdEErUdtyW2I9hmFRg9RY9u9oSTXuhkMoRh6sXB4nGxn5TMEHfibciQuJYGkPInlGuQCJElrqrZyPTN6t5zdhMZ96jcaGv5iuyY5B4FS7WQUjegM_8u-inLJs1SchIRTrT4rmeOX5xN6_h6CZzCeLVPmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
رندرینگ سمت سرور در مقابل سمت کلاینت: توصیه‌ های گوگل
👨‍💻
رندرینگ سمت سرور (SSR) چیست؟
در SSR، محتوای صفحات وب در سرور تولید شده و به‌صورت HTML کامل به مرورگر ارسال می‌شود. این روش به موتورهای جستجو امکان می‌دهد تا محتوا را به‌راحتی ایندکس کنند، زیرا نیازی به اجرای جاوااسکریپت در مرورگر نیست.
🧑‍💻
رندرینگ سمت کلاینت (CSR) چیست؟
در CSR، مرورگر ابتدا یک HTML ساده دریافت می‌کند و سپس با اجرای جاوااسکریپت، محتوا را تولید و نمایش می‌دهد. این روش برای برنامه‌های وب تعاملی مناسب است، اما ممکن است موتورهای جستجو در ایندکس کردن محتوا با مشکل مواجه شوند.
📈
توصیه‌های گوگل:
گوگل اعلام کرده است که هیچ مزیت خاصی از نظر سئو برای SSR یا CSR وجود ندارد. مهم‌ترین نکته این است که محتوای سایت به‌گونه‌ای باشد که موتورهای جستجو بتوانند آن را به‌درستی ایندکس کنند.
🔹
اگر سئو برای شما اولویت دارد، SSR می‌تواند گزینه مناسبی باشد.
🔹
اگر به دنبال تجربه کاربری تعاملی هستید، CSR را در نظر بگیرید.
🔹
در برخی موارد، ترکیبی از هر دو روش (رندرینگ ترکیبی) می‌تواند بهترین نتیجه را ارائه دهد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 646 · <a href="https://t.me/danialtaherifar/870" target="_blank">📅 12:59 · 15 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yyt8FhjpW8BOhM2f1NFKd8J40ZKH97do8GK6G6331LssvzRvhCkp_RckUyNe_GsMmYoQGX6gj_xC-aIjKgLsWOabPAVPW9_iq0ncQky0A7lfgwUdJwERlPuybJGWhhLlLCT_q53PJP1OGx_lpulQdchfgLjwU6EPX4zSk4fnLZGiKMUeAGXl7sgbPccYtwNKUWObrQdygGC0uvWR2rNnMQM70ln1izO0v0WrDMTiZvHyQgwk_phzrAf3Yv_ie5hobMaH_rudfX9ZlOqneYkvFojN7lZSsVeL23E4VLxsgnni9HfZTvTavlQOVDPL52FAOZ3iQ3agV543-RfUdEM7Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
ابزار NotebookLM گوگل حالا در بیش از ۵۰ زبان در دسترس است!
📢
گوگل قابلیت «خلاصه‌های صوتی» (Audio Overviews) را در ابزار هوش مصنوعی NotebookLM گسترش داده و اکنون این ویژگی در بیش از ۵۰ زبان مختلف، از جمله فارسی، اسپانیایی، پرتغالی، فرانسوی، هندی، ترکی، کره‌ای و چینی، در دسترس کاربران است. ​
🎙
این ابزار با تبدیل منابع متنی به گفتگوهای صوتی شبیه به پادکست، به کاربران امکان می‌دهد تا اطلاعات را به‌صورت شنیداری و تعاملی دریافت کنند. با استفاده از پشتیبانی صوتی بومی Gemini، کاربران می‌توانند خلاصه‌های صوتی را به زبان دلخواه خود بشنوند.​
🌐
برای تغییر زبان خروجی، کافی است به تنظیمات NotebookLM رفته و زبان مورد نظر را انتخاب کنید. این قابلیت از سال گذشته در بیش از ۲۰۰ کشور راه‌اندازی شده و گوگل قصد دارد با دریافت بازخورد کاربران، آن را بهبود بخشد.​
✅
همچنین، گوگل این ویژگی را به چت‌بات Gemini و Google Docs نیز اضافه کرده است، تا کاربران بتوانند انواع بیشتری از محتوای نوشتاری را به صورت صوتی دریافت کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 714 · <a href="https://t.me/danialtaherifar/869" target="_blank">📅 14:16 · 10 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-868">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJ2czHx1gh-NPomiRioMu251-ffdR57qZu-LEmcRbhaN1xJoV6pkujN13GuT03_c1nM7IymvBX3Xm2DYeCBzIftjsH5FpVRCFBuugoGWt2Zwgoz9BKm10SfrZvXmFFtMrOhV1YAY2M5gtJ4SodHY5NoaVkCAadXJ1QsejILoE4lpL9swYfplHvEuP6If_sxhmGAn-vcUrFdW62aGxun2BF1gXPs-EsWaqYHnPAj6SZZAGe-MgNyBAFKYRjrAL915DbcmpiaixCEtXxZonM0j83AdfcyJ607hBElQ3ee47VvSZRpLelwBfUuUajnCi31HohoclSKJaBy6W7falDJ_5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
جان مولر: آپدیت تاریخ XML Sitemap تأثیری روی سئو ندارد !
🗣
جان مولر، تحلیل‌گر ارشد گوگل، اخیراً تأکید کرده که تغییر خودکار تاریخ‌ها در نقشه‌ سایت XML (تگ <lastmod>) بدون تغییر واقعی در محتوا، نه تنها به بهبود سئو کمک نمی‌کند، بلکه ممکن است فرآیند شناسایی به‌روزرسانی‌های واقعی را برای گوگل دشوارتر کند.​
❌
کارهایی که نباید انجام بدید:
فقط تاریخ‌ها رو آپدیت نکنید اگه محتوا تغییر نکرده.
ابزارهایی که اتوماتیک تاریخ‌ها رو عوض می‌کنن، فایده‌ای ندارن.
گوگل می‌فهمه که محتوا واقعاً تغییر نکرده!
✅
چی کار کنیم؟
فقط وقتی که محتوا، لینک‌ها یا دیتاهای صفحه تغییر کردن، تاریخ رو عوض کنید.
نقشه سایت رو با تغییرات واقعی همگام کنید، نه مصنوعی!
@danialtaherifar</div>
<div class="tg-footer">👁️ 612 · <a href="https://t.me/danialtaherifar/868" target="_blank">📅 12:27 · 09 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-867">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ve_Up5XQBh_7i4_AxUSBOuvU0puUwRvze0aldokgYvUXpSmS8pRTtDAwY1yUljF90L0OkMNovlIaZrtBPsWyspMNidmcBmaUumGiQLwIjLfoHP3GHHr4SmGH7J9gjXspzw3Xhx4d5jkbiwpK5Vqrn69eifBLRjobGCk52spx3lBruSJ8Cb5IIHZKeGbP0F8sEsPw_D1xmobwMt-xMjLR1zShVWryHMmB0ZnuiHwplKFfFqiGro1UTCgBPpgs1nTGzywort_6H3XiHMWkjR4Uqsdrkz_F_EW81lkGsePvKgcy4CsPtN1UeZeLHvw3EFtjUuvZY85mi2w9wXE98YRkCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل مستندات Google-Extended را آپدیت کرد: کنترل بیشتر روی داده‌های آموزش AI!
🌐
این به‌روزرسانی به ناشران کمک می‌کنه دقیق‌تر تصمیم بگیرن که آیا داده‌های سایت‌شون برای آموزش مدل‌های آینده Gemini و Vertex AI استفاده بشه یا نه.
✍️
گوگل اکستندر یک user agent است که به وب‌سایت‌ها امکان می‌دهد تعیین کنند آیا محتوای‌شان می‌تواند برای آموزش مدل‌های Gemini و Vertex AI استفاده شود یا خیر.
با مسدود کردن این agent از طریق فایل robots.txt می‌توان جلوی استفاده از داده‌ها را گرفت.
🔹
نکته مهم: Google-Extended تاثیری روی رتبه‌بندی جستجو یا ایندکس شدن سایت شما نداره.
@danialtaherifar</div>
<div class="tg-footer">👁️ 640 · <a href="https://t.me/danialtaherifar/867" target="_blank">📅 18:41 · 08 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-865">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HE8fEf-fSzs8Zev_pKAoQQMD0GV3qOnHKO3dC-_3EnbpF1yQvs6Y_gyvviQjBvKsn_L9O6Jl7-N0UXs2Eh9pQ6XOyq1o4sfuA4mvYc7jjD-zhuVRa5LW6JaPpfacrIPzpV7POfcLK6hT2B67TcQ3rPzMHq9NSxj2dq3egkBsQly2jwuqPwkluRQlks7eKT6-EYM0-44d7WSD68DVDtzcu0Vqy_GtqY8bV3PCbwuKk8W8sLedi9ypfx6TeL9P03biEy2V8MTGkwzeSASaw_yx-G1zwn-ZR7KbnDUcVgQuejA_rqRmhwngC1u9wwzhfEZTbbSVdFJZQ3G_iCSoE5k9mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ib8CiJM1jt2Li__WpxwrQWDa2lW3E-WHs23Dn8MG7RwxFFuDBM2m4wWhkVS0wdK6NH2VP73dP1HCWtxhaFrsCuZK0e4mLJ-AOLe7Z9UxYlMp1KkIve5Ljb6hgQ2ElvEY_qPN5aQPCk2_-2imPhT3ubtRvMMjAlkyuYUnp0hcjr8GbhaqGKXGr2KIc0kh4E2w_8gCVrax335Bw8nMGhhsG9HSBEbF3d21joJAquY3xUn5XiO4pzuVrlG51K2L1WKdPfgmTTk56RbdOSZJE2ue9BWGhWOS0Ih2WV_Bjutp-wgShLUzoQ5A_6ceh4Py4WXcSaOnswf6wpH6PM2UD-XV3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
نوسانات شدید رتبه‌ بندی گوگل در چند روز گذشته !
📈
طبق گزارش‌های جدید، دوباره شاهد نوسانات چشمگیر رتبه‌بندی در نتایج جستجوی گوگل بودیم! این تغییرات درست بعد از نوسانات هفته‌ی قبل (۲۲ و ۲۳ آوریل) رخ داد و باعث شد خیلی از وب‌سایت‌ها افزایش یا افت چشمگیری در ترافیکشون تجربه کنن.
😵‍💫
🔍
ابزارهای مختلف مثل Semrush، MozCast و SimilarWeb هم این جهش ناگهانی رو تایید کردن. حتی بعضی از مدیران سایت‌ها از کاهش ۷۰٪ بازدیدکنندگانشون خبر دادن!
😬
👀
در حالی که به‌طور معمول هر هفته نوسانات کوچیکی داریم، این بار دو بار در یک هفته چنین شدت نوسانی خیلی غیرمعمول بوده.
💬
بعضی‌ها در انجمن‌های تخصصی گفتن که سایت‌هاشون از گوگل دیسکاور حذف شدن یا ترافیکشون افت وحشتناکی داشته؛ در مقابل بعضی‌ها هم رشد خوبی تجربه کردن.
📅
نکته مهم: هنوز خبری از آپدیت رسمی جدید گوگل در سال ۲۰۲۵ نیست (به غیر از آپدیت اصلی مارچ ۲۰۲۵).
📌
اگر سایتتون تغییرات عجیبی داشته، بدونید تنها نیستید! این نوسانات بخشی از بازی گوگله.
😉
@danialtaherifar</div>
<div class="tg-footer">👁️ 666 · <a href="https://t.me/danialtaherifar/865" target="_blank">📅 20:42 · 07 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-864">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YpvJ38MXpBw_a3pxGzSO7wkUjFLtR3s3-tw-M99yh0wb6pIKCbgJf2kE9svooaGk_8zhfTFKLGloMeSpe8PReFjYewk502M8K6OhwluJd13pJEeWEgViOdLn5ZRWaevkWHSHFKQIpm2qYdNSxuqB_j6z0QBLQx3GG_A3OJu64Kr4NhReakG7St8MYd4cT8isAQwRKerxiB9ySmWRan-2x60aqC9EUYU4V_mn35NwVHcCc2SfHGVxo1ORuVwO2aewlgrVreDTiwLKxkY0C4B-24oa4fOFq2VP5YswBrKMOSy0YSjdjwzdD8ftvWdmlHBmV14UmilgGnysmnJv1JtD9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گوگل در حال تست URL آبی در نتایج جستجو است!
🔍
گوگل اخیراً در حال آزمایش تغییرات ظاهری در نتایج جستجوی موبایل است؛ به طور خاص، رنگ URLها که معمولاً خاکستری یا سبز بودند، حالا به رنگ آبی تغییر کرده‌اند!
👀
بعضی کاربران متوجه شده‌اند که در برخی جستجوها، آدرس سایت (URL) به رنگ آبی و در کنار عنوان لینک نمایش داده می‌شود، چیزی که پیش از این رایج نبوده.
🧪
این تغییر همراه با جابجایی محل نمایش URL و نام سایت انجام شده:
در بعضی موارد، نام سایت در بالا و آدرس URL در پایین نمایش داده می‌شود.
در برخی موارد دیگر، URL درست زیر عنوان لینک می‌آید، و نام سایت حذف شده.
📱
این تست‌ها فقط در نسخه موبایل گوگل دیده شده و هنوز مشخص نیست آیا به صورت دائمی اعمال می‌شود یا خیر.
📢
هدف گوگل از این تغییرات احتمالا افزایش خوانایی نتایج و بهبود تجربه کاربری است. البته هنوز بازخورد رسمی یا اطلاعیه‌ای از سوی گوگل در این باره منتشر نشده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 545 · <a href="https://t.me/danialtaherifar/864" target="_blank">📅 14:10 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-863">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrf_W-10MqGa2N4n45BzzaWjfC7kIEwNGlrBwyon3txGhznXDbG8SdGLRBE9P52vMMZNGkSCoU94Kp_9d1cgEAAU238t3CQWrCDzqJ7UFVcz3EtYch1M2xRdXq8q1DoUBp1VZYKb8JDJbdbZSIpDJT6frDkbNiSppXD671Zc692J0zZCz-y3gQshW2iVPamekhja2dQ0TYC3YHaYhnqkNVeiD7r5IMsYBLtdycJQGOcfmp9Y_51YvWLvKeQDwKWV_ELJ3ZkHUPnagLKbT77Y0NzZVw2jWPZfrG9qEtq_VD7_bRTqNB3TBte-5koTAWejQStildRu85DBu7TMjYz7Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
گوگل: استریم تصاویر برای سئو مناسب نیست!
🔍
جان مولر از گوگل توضیح داد که استفاده از تکنیک‌های استریم تصاویر (مثل قرار دادن عکس‌ها از طریق کد Embed به جای آپلود مستقیم) می‌تواند باعث شود تصاویرتون در نتایج جستجو ایندکس نشوند.
👨‍💻
در واقع وقتی تصاویر رو به این سبک بارگذاری می‌کنید (مثل ویدئوهای یوتیوب)، گوگل نمی‌تونه اون‌ها رو شناسایی کنه و در نتایج نمایش بده.
➖
نتیجه؟ کلی ترافیک احتمالی از دست میره!
🚫
📉
✅
اگر براتون مهمه تصاویرتون توی گوگل دیده بشه، بهتره روش سنتی آپلود مستقیم (JPEG, PNG و...) رو استفاده کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 544 · <a href="https://t.me/danialtaherifar/863" target="_blank">📅 09:57 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-862">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4hlB0H9fC-eaoWbgEsqORravGov1s2f2WFuM7LtlKiPgfgdzA1nYal5SiRbPWjSMZuUKFjkO-QzneoQPbEXiWDjBi_qRNFNUWNNBjZL_dprkvtgQbbHZSWxiFUVY9YnXB0Nj-b3qcX9_H97SER6ConQ-NWA71C4tu0w5Fn9v8XF2M2fy0eZmN3LHIslhO7RxQ22aM2dSUr_b08JQp1iBhzwJkh6J_U5bmaEmCxhjN-UJTR915ObiVb6sS8bN2b8mN6Lq6fxSi6A96eyacHFSbWd8bBS5VCqEn1OuK2zGw2ova6usZmHymYc7w1HDrf3DrnWPU82ALCdsULxLqODcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
گوگل تأیید کرد: داده‌های ساختاریافته باعث بهبود رتبه سایت نمی‌شوند​
📢
در تازه‌ترین اظهارنظر، جان مولر از گوگل اعلام کرد که استفاده از داده‌های ساختاریافته (Structured Data) به تنهایی تأثیری در بهبود رتبه‌بندی سایت‌ها در نتایج جستجو ندارد.​
🧠
داده‌های ساختاریافته چه کاربردی دارند؟
داده‌های ساختاریافته به گوگل کمک می‌کنند تا محتوای صفحات را بهتر درک کند و در صورت تطابق با معیارهای خاص، امکان نمایش آن‌ها در قالب نتایج غنی (Rich Results) مانند کاروسل‌ها، بررسی‌ها و دستور پخت‌ها فراهم شود. ​
⚠️
نکات مهم:
استفاده از داده‌های ساختاریافته تضمینی برای نمایش در نتایج غنی نیست؛ فقط امکان آن را فراهم می‌کند.
استفاده از انواع غیرمستند داده‌های ساختاریافته تأثیری در بهینه‌سازی جستجو ندارد؛ زیرا گوگل تنها حدود ۳۰ نوع از آن‌ها را در نظر می‌گیرد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 669 · <a href="https://t.me/danialtaherifar/862" target="_blank">📅 18:41 · 02 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-861">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlGCn2nTGAFjiRVcEaEoETdlhS2EKgirXpld-ABFj848mdpeHwRP_4xOokS6Vl3_rdxwNV4eIpKBiVfFNfqx-Wzg4XCgavyasPW_CT9TF8C8eZX22p4ENIyYcU0UXI8QIaRAaBX8CzHHYwzVud8fTCyQgurGbwJetgjOaLLH_XBhMt7nyovruTWiFXEl7cuY_sMr4Hjggk3WMpmVHk--NajEqbeVWpLF6oydpVKkp3lCvOZRMcGzEP4mjUdwvfAJdYKA_O0i-dKFVB6IuBQoMOplrWK72Ppyu7SvGepKInoqLRA35vAjT0D1zrbRjuuh3zMlztk741IB_UJojZK5tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
گوگل: فایل LLMs.txt به اندازه تگ متا کیورد بی‌فایده است!​
📄
جان مولر از گوگل اعلام کرد که فایل LLMs.txt، که به‌عنوان راهی برای هدایت خزنده‌های هوش مصنوعی پیشنهاد شده بود، در عمل بی‌فایده است و آن را با تگ متا کیورد مقایسه کرد که سال‌هاست توسط موتورهای جستجو نادیده گرفته می‌شود.​
🔍
فایل LLMs.txt چی بود اصلاً؟
یه سری از متخصصا و کمپانی‌ها پیشنهاد دادن که ما بیایم یه فایل به اسم llms.txt روی روت سایت بذاریم، تا مشخص کنیم چه مدل‌های زبانی (مثل OpenAI یا Anthropic) اجازه دارن محتوای ما رو بخونن یا نه. در واقع، یه چیزی مثل robots.txt ولی مخصوص هوش مصنوعی‌ !
🤖
📌
فایل LLMs.txt  به‌عنوان استانداردی برای کنترل دسترسی مدل‌های زبان بزرگ (LLMs) به محتوای وب پیشنهاد شده بود.​
📌
جان مولر اظهار داشت که این فایل توسط خزنده‌های هوش مصنوعی بررسی نمی‌شود و تأثیری در سئو یا کنترل محتوا ندارد.​
📌
تجربیات کاربران نیز نشان می‌دهد که پس از افزودن این فایل به سایت‌هایشان، هیچ تغییری در رفتار خزنده‌ها مشاهده نکرده‌اند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 682 · <a href="https://t.me/danialtaherifar/861" target="_blank">📅 22:51 · 01 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-860">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-poll">
<h4>📊 🎯دوست داری بیشتر در مورد کدوم موضوع توی کانال صحبت کنیم ؟👇</h4>
<ul>
<li>✓ 1️⃣کسب درآمد از گوگل ادسنس</li>
<li>✓ 2️⃣سئو آف‌ پیج (لینک‌ سازی، PR و...)</li>
<li>✓ 3️⃣سئو تکنیکال (Core Web Vitals، ایندکسینگ و ...)</li>
<li>✓ 4️⃣سئو آن‌ پیج (محتوا، تگ‌ ها، ساختار صفحات و ...)</li>
</ul>
</div>
<div class="tg-footer">👁️ 691 · <a href="https://t.me/danialtaherifar/860" target="_blank">📅 09:21 · 30 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-859">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🎯
اخطار
گوگل: محتوای تولید شده با هوش مصنوعی در پایین‌ ترین رتبه قرار میگیرد
🔍
📢
در یک به‌ روزرسانی مهم، گوگل اعلام کرده ارزیابان کیفیت موتور جستجویش (Quality Raters) موظف شده‌اند تا محتواهای تولیدشده توسط ابزارهای هوش مصنوعی را نیز بررسی کنند و اگر این محتواها کم‌ ارزش، بدون تلاش انسانی یا فاقد اصالت باشند، باید پایین‌ترین رتبه ممکن را دریافت کنند!
🧾
تعریف رسمی گوگل از هوش مصنوعی مولد
"هوش مصنوعی مولد (Generative AI) مدل‌هایی هستند که می‌توانند براساس داده‌هایی که آموزش دیده‌اند، محتوای جدیدی مانند متن، تصویر، موسیقی و کد تولید کنند."
گوگل تأکید کرده که این ابزارها می‌توانند مفید باشند، اما در صورت استفاده نادرست، به‌ راحتی منجر به تولید انبوه محتوای بی‌کیفیت می‌شوند.
🛑
تمرکز جدید گوگل روی محتواهای کم‌ ارزش
💥
گوگل ساختار بخش‌های مربوط به محتوای خودکار را بازنویسی کرده و به‌شکل جدی با محتواهایی که:
تنها برای جذب ترافیک تولید شده‌اند
فاقد ارزش افزوده برای کاربر هستند
فقط ترکیبی از اطلاعات تکراری‌اند
مقابله خواهد کرد.
📌
حتی اگر چنین محتواهایی توسط انسان بازنویسی شده باشند ولی نشانه‌ای از تلاش واقعی، تجربه تخصصی یا هدف مفید برای مخاطب در آن‌ها نباشد، باز هم امتیاز پایینی خواهند گرفت.
📍
جمع‌ بندی مهم برای تولیدکنندگان محتوا، سئوکارها و مدیران سایت‌ ها
🟢
استفاده از هوش مصنوعی ممنوع نیست!
🔴
اما اگر بدون دقت، بازبینی و بدون ارزش واقعی باشه، رتبه سایتتون در خطره!
🛠
پس: هوش مصنوعی + تجربه انسانی = محتوای موفق
💡
@danialtaherifar</div>
<div class="tg-footer">👁️ 875 · <a href="https://t.me/danialtaherifar/859" target="_blank">📅 09:34 · 29 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-857">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n8u4BDMnjryFHDfJB4vTPojrkQO6JTOPi7RgxIOtVaM5_aMi8clOgEKLRNHeyUjTvQAHCY5sbZZgy0I_6nS7bvUaW4h39NyjLtTiIUULmU3p3FM1zsYeNMHVUl84FxySiLtE4mrBiERDLefORUBA91L8srPtxq-ESvX_mi0Ae1OFFhbQxclmu5iOdXp9YVd4Qe_U1yBawXzutA7fr8vaAVwglqJznJm_Oa2TKqPK3Cv4T5ylkpZLhq_OfjG_wHoxXy-MQEmr9-yYPUr3KYOVCTZc8b3w3MwJiLEetnuTIrCADJYz1isK6pMEKbWp7Sfizi0lPyVzZa0ew_VcY4KjdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fFiS7Uyo91QR8KAkJUX4_L8bW2JPDcTTOztYHt716MI2reX8z5SGhpIDQhV4L97PMt0lej5GftlOmATY1yDwmUQcprh5Ggbw_NYFvN6vuGczsvH-A7YrMNDrxp3aaX3S8Vcs0KTVDOk0sDmZUPouQn0-pr5oh6-tFFElDLZL9dEPznDjCwjzI3-t_rgMIv45p7zkhEtc-MPkydIRqLoGhILTW0E0F5jcUy-pZBPzppQao6QOOeruR3VEtN8iBeGjLDF5N1ka6oxUNDmgxCKmEkmzaskOwWMhgu2fOWI5L_KM9WnIF99dRgWHxtGWKL2jjYQOPWpfaIu71OVZJYfdZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
دسترسی به داده‌های ساعتی در API سرچ کنسول گوگل برای ۱۰ روز گذشته فعال شد!​
گوگل به‌ تازگی قابلیت دریافت داده‌های ساعتی را در API سرچ کنسول خود فعال کرده است. این ویژگی به کاربران امکان می‌دهد تا اطلاعات عملکرد جستجوی وب‌سایت خود را با جزئیات ساعتی برای ۱۰ روز گذشته دریافت کنند.​
🆕
چه چیزی تغییر کرده است؟
پیش‌تر، گزارش‌های عملکرد در سرچ کنسول فقط داده‌های ساعتی ۲۴ ساعت گذشته را نمایش می‌دادند.​
اکنون، از طریق API، می‌توان داده‌های ساعتی را برای ۱۰ روز گذشته دریافت کرد.​
برای استفاده از این قابلیت، باید از بُعد جدیدی به نام HOUR در درخواست‌های API استفاده کرد.​
همچنین، مقدار جدیدی به نام HOURLY_ALL به پارامتر dataState اضافه شده است که نشان‌دهنده داده‌های ساعتی (که ممکن است ناقص باشند) است.​
💡
چرا این ویژگی مهم است؟
این قابلیت به مدیران وب‌سایت و متخصصان سئو امکان می‌دهد تا نوسانات ترافیک و عملکرد سایت خود را با دقت بیشتری بررسی کنند و در صورت بروز مشکلات، سریع‌تر واکنش نشان دهند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 813 · <a href="https://t.me/danialtaherifar/857" target="_blank">📅 11:20 · 23 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-853">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gp8rWumnZ4yVZ4PabJwMFXJ_JxT6xbcAtUH04hSi0DgvWeQzq7XYFyz6BeUHuzS6hYBIjDxDHVV_uFBws6AwbAEagyBPy7CAum0186w3wNTirgPghNl5tYq-nfSKypQ6yZ-HD4QSZkhVpY8iFF0XiOSy06xRRDjxfZuKNxkRp-WTymX69tuK2QLVHvTroQ_NIIRv3eGOz-6cDW94Rv0SNX4M9h7568rkRwFi0o829V8cC_XeVKMuODkI7HdSE5j0taqXSd4s6vQkqNOz4eJK4_Ax4veOXbMZT2Keh9Dyl-lRmmpiTjChSiGt1cv1pmyIu2jvmKT3bVop9pzuHIRfmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D0KPDaj9EC3X3UhNMpVEnRd7osmaAYeeMOfNpyvKakQpw9yTRSizurvFutWPSiUcPbPTDB7oKfR1lYtpFIVsMY_jq7xiMQ4xUjIoaUd9houqgjta1-wNX2gkeDdbKPIyjNjhVssy_t1CGJo70BZX1f_HkXBnYYE4A9RhOLiB9uPc0q7KC0vxTffIY34Ch2LrTfyHf4UYXNtoPKYalmml03BAmn_aTncFOJkdzO2ROr1zCpH10ib9v6vNasXki4Q6hxc0mjutoM_vHRVS4CSP9Xfqp98tx9iuQA2C3-Np4gFM84AB3KOanme8adCUEcLb0gBTLCQERvsnXQbtLH4LWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📉
نوسانات شدید رتبه‌ بندی گوگل در ۹ و ۱۰ آوریل ۲۰۲۵​
در روزهای ۹ و ۱۰ آوریل ۲۰۲۵، شاهد نوسانات قابل‌توجهی در رتبه‌بندی نتایج جستجوی گوگل بودیم. اگرچه گوگل هیچ به‌روزرسانی رسمی را اعلام نکرده است، اما ابزارهای مختلف بررسی آپدیت های الگوریتمی مانند SimilarWeb، Cognitive SEO، Accuranker، Wincher، Algoroo، Mangools، Sistrix، Data For SEO و SERPstat از وقوع یک به‌روزرسانی تأیید نشده خبر میدهند.​
🗣
واکنش جامعه سئو
برخی از متخصصان سئو از کاهش شدید ترافیک ارگانیک و افت رتبه‌ بندی را گزارش کرده‌اند. یکی از کاربران اشاره کرده است: "رتبه‌بندی‌ها به شدت کاهش یافته‌اند و ترافیک به طرز قابل‌توجهی افت کرده است."دیگری اظهار داشته: "به نظر می‌رسد به‌روزرسانی اصلی هنوز در حال اجراست؛ نباید به گفته‌های گوگل اعتماد کرد."​
با توجه به عدم تأیید رسمی از سوی گوگل، اما شواهد نشان می‌دهند که تغییراتی در الگوریتم رتبه‌بندی رخ داده است. برای مدیران وب‌سایت‌ها و متخصصان سئو، مهم است که عملکرد وب‌سایت‌های خود را در این دوره به‌دقت زیر نظر داشته باشند و در صورت لزوم، استراتژی‌های خود را بازنگری کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 805 · <a href="https://t.me/danialtaherifar/853" target="_blank">📅 14:56 · 22 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-852">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxw6DkwNLzG0_3EN-ZebQOFvm_jxD3ufK8I3Id82yioZcJazvZ-m4dSm0fzjDwseHKkH00s7t67pANZHyuUJ6ye1ukE5wI5YhAESpS_z8Y7RxbVH5vQmh9UdJ1Jw9jHzXqXmUHCbtCpqkcvCstGlikXlPIujpIXgYao3jAA1pdxjouNizDdBDoZx7aLD2yowEHewgfYPZKUup7lPoThqBrcD3mqIKMBqMBcA8zwWE22gubgAWpbYv5tv5nQsqtnDfP9sLqe6Sdi71aYSclOwTjo0HE5wxfLQWmD8ek0wubajWRGMbZrcwgQ0ShAwPVa18v-QizK7dFdPkKnMZEBw5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
🔍
گوگل دیسکاور به دسکتاپ می‌آید: تغییر بزرگ در صفحه اصلی گوگل
🔔
گوگل اعلام کرده است که پس از سال‌ها آزمایش، قصد دارد گوگل دیسکاور (Google Discover) را به نسخه دسکتاپ صفحه اصلی خود اضافه کند. این خبر در رویداد Search Central Live در مادرید به صورت رسمی اعلام شده است.
📱
گوگل دیسکاور یک فید محتوایی شخصی‌سازی‌شده است که تاکنون فقط در دستگاه‌های موبایل در دسترس بود و به کاربران کمک می‌کرد محتوای جدید و مرتبط با علایقشان را کشف کنند. حالا این تجربه به دسکتاپ هم می‌آید.
👀
در هفته گذشته، برخی کاربران در ایالات متحده مشاهده کردند که گوگل در حال آزمایش نمایش فید دیسکاور در صفحه اصلی دسکتاپ خود است. این نشان می‌دهد که گوگل به دنبال ارائه تجربه‌ای یکپارچه در تمام دستگاه‌هاست.
📊
این تغییر می‌تواند تأثیر قابل‌توجهی بر استراتژی‌های محتوایی ناشران و سایت‌ها داشته باشد، چون دیسکاور یکی از منابع مهم ترافیک برای آن‌ها شده است.
🎯
با این به‌روزرسانی، کاربران دسکتاپ هم می‌توانند به‌راحتی به محتوای تازه و شخصی‌سازی‌شده دسترسی داشته باشند و لذت تجربه‌ای مشابه موبایل را ببرند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 586 · <a href="https://t.me/danialtaherifar/852" target="_blank">📅 12:36 · 21 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-851">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">📊
✨
چطور گزارش سئو بنویسیم که مدیر بازاریابی (CMO) عاشقش بشه؟
نوشتن گزارش سئو فقط نمایش اعداد نیست، بلکه باید داستانی بسازید که نشون بده سئو چطور به رشد کسب‌وکار کمک می‌کند. در ادامه به چند نکته مهم برای گزارش نویسی اشاره می‌کنم.
1.
🚀
نتایج تجاری، نه فقط داده‌ های فنی
مدیر ارشد بازاریابی (CMO) معمولاً با واژه‌هایی مثل "ترافیک"، "لینک‌ سازی"، یا "موقعیت کلمات کلیدی" ارتباط برقرار نمی‌کنن. اون‌ها می‌خوان بدونن این عددها چه تأثیری روی درآمد، برند و رشد کلی شرکت دارن.
✅
به جای این‌ که فقط بگید "افزایش ترافیک داشتیم"، بگید:
«ترافیک ارگانیک باعث افزایش ۲۵٪ سرنخ‌های فروش شد که منجر به ۱۵۰ هزار دلار درآمد شد.»
2.
💵
از ارزش مالی صحبت کن
باید نشون بدید که سئو به لحاظ مالی چقدر به صرفه‌ست. مثلاً:
🔸
هزینه جذب هر مشتری از طریق تبلیغات = ۱۲۰ دلار
🔸
هزینه جذب از طریق سئو = ۲۵ دلار
🔍
اینجوری نشون می‌دید سئو باعث صرفه‌جویی واقعی در هزینه‌ها میشه.
3.
📈
تمرکز روی محتوای برتر
به‌جای ارائه لیستی از تمام محتواها، فقط چند محتوای موفق رو هایلایت کنین. بگید:
«این مقاله وبلاگ ۳۵۰ سرنخ ایجاد کرد، به رتبه اول در گوگل رسید و در شبکه‌های اجتماعی ۵۰۰ بار به اشتراک گذاشته شد.»
4.
🧠
از زبان CMO استفاده کن، نه زبان سئوکارها
🔴
نگید: «Domain Authority این سایت ۷۰ بود.»
🟢
بگید: «ما از یک سایت معتبر لینک گرفتیم که باعث رشد رتبه ما در نتایج شد.»
زبان ساده، قابل فهم، و متمرکز بر نتیجه = موفقیت گزارش شما.
5.
📅
تغییرات را در بازه زمانی مقایسه‌ای نشون بده
مثلاً بگید:
«در مقایسه با ماه گذشته، ترافیک ارگانیک ۲۰٪ افزایش یافته و نرخ تبدیل از ۲٪ به ۳.۵٪ رسیده.»
نمودار و ویژوال هم خیلی کمک می‌کنه!
6.
📌
پیشنهادات عملی ارائه بده
فقط گزارش نده، بگو چه قدم‌هایی باید برداشته بشه. مثلاً:
✅
«اگر بودجه لینک‌سازی ۳۰٪ افزایش پیدا کنه، می‌تونیم تا سه‌ماه آینده ۵ رتبه در نتایج گوگل صعود کنیم.»
جمع‌ بندی
🎯
مدیران بازاریابی به دنبال تأثیر واقعی سئو روی رشد شرکت است. گزارش شما باید نشان دهد:
🔹
سئو چطور به درآمد کمک می‌کند
🔹
چه نتایج قابل اندازه‌گیری‌ای به دست آمده
🔹
قدم بعدی برای پیشرفت چیست
با این سبک گزارش‌نویسی، نه‌ تنها توجه CMO رو جلب می‌کنید، بلکه اعتبار تیم سئو رو هم بالا می‌برید
💪
@danialtaherifar</div>
<div class="tg-footer">👁️ 585 · <a href="https://t.me/danialtaherifar/851" target="_blank">📅 21:58 · 20 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-849">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UXRHsLHByPPWjeWrSDS6Y9I-n1SfjM36721KLT19HuXXCVs6qO_4I8Y2zMz8P3UP-2vp7myvP0PI5t56nU1GebYNp0zQygJBJ9apb14_ntbnTpfDiXDJo8xn58BMWDxLlBBrQZl-fipazpmE6PRLkOWELKu3xCZTuI7wgUJDMv7COSLTNdC8EbqDfD2Rwv1sgyx7gxlLLfS8q9agji8w6aFTEIPvpOOwA_dGid000m33cHRfUa_4Hnni1bQQYzEhq8nwU0hLveVSLa917UfvXVIas8QiZJQqfOEpND6cZQZkZiRx6rLYQQOUdJVsJVyQdoWXE64DJzpyYWlqOk0eGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QMCvfFVfM3G2d19P3yattH2WywMC4Rqpw3ou-1DqUqdRu6VAJ9zs3LMMNjNJOGELz6a5ydkLqAQBzj5jPRb-g3C8ks-ilyKABpsHodqdki0YqabrpCZk-6hKhlHzQ26HXymzTRG8uVgD88FP37MA5Zx4s6c6sDgtS01iF34c4cOA-1V2OHEM4hFMSA6bL90VFohtpTNFnWPqMTyt0k1u1gmen1BDj3_5F_72tbF3d42CiNwK6UA0h1IQmdWK2RID8xpKJFcgzq4aNGI6vSJAwlp68qQfQzsqCAKWraiqQPORx_mMjDOKTjSjnnRDd-CWYZBR50nNSJ7ke0MRSom4dw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎯
ویژگی جدید گوگل: نمایش موضوعات مرتبط در جستجو!
🔍
📚
✨
🔎
گوگل در حال آزمایش قابلیتی جدید به نام "Relevant Topics" یا "موضوعات مرتبط" است که در پایین برخی نتایج جستجو نمایش داده می‌شود. این قابلیت کاربران را تشویق می‌کند که فراتر از جستجوی اولیه‌شان، موضوعات مرتبط بیشتری را بررسی کنند.
📱
سچین پاتل (Sachin Patel) یکی از کاربران شبکه اجتماعی X (توییتر سابق)، اولین کسی بود که این ویژگی را مشاهده کرد و اسکرین‌شاتی از آن منتشر کرد.
🔍
وقتی او عبارت "SEO" را جستجو کرد، در پایین صفحه نتایج، بخشی با عنوان "Relevant Topics" ظاهر شد که لیستی از موضوعات مرتبط با سئو را نشان می‌داد.
📂
در کنار این لیست، گزینه‌ای با عنوان "Show more" یا "نمایش بیشتر" وجود داشت که با کلیک روی آن، موضوعات بیشتری نمایش داده می‌شد.
🛠
این بخش می‌تواند به سئوکاران و تولیدکنندگان محتوا کمک کند تا متوجه شوند گوگل چه موضوعاتی را به عنوان مکمل جستجوی اصلی در نظر می‌گیرد.
💬
فعلاً گوگل این قابلیت رو به‌صورت محدود و آزمایشی نمایش می‌ده و هنوز معلوم نیست چه زمانی به‌صورت رسمی برای همه کاربران فعال خواهد شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 675 · <a href="https://t.me/danialtaherifar/849" target="_blank">📅 23:56 · 18 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-848">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔥
گوگل به‌ روزرسانی هسته‌ مارس ۲۰۲۵ را تکمیل کرد!
🚀
🔍
📢
پس از ۱۴ روز به‌روزرسانی Core Update مارس ۲۰۲۵ گوگل، چند روز پیش به پایان رسید! این به‌روزرسانی که در ۱۳ مارس ۲۰۲۵ آغاز شد و در ۲۷ مارس ۲۰۲۵ تکمیل گردید که تغییرات مهمی در الگوریتم‌های جستجو ایجاد کرده است. اگر شما هم در این مدت تغییراتی در ترافیک سایت خود مشاهده کرده‌اید، این به‌روزرسانی می‌تواند دلیل آن باشد.
🧐
🔄
🔎
جزئیات کامل به‌روزرسانی Core Update مارس ۲۰۲۵
🔹
تاریخ شروع: ۱۳ مارس ۲۰۲۵
🔹
تاریخ اتمام: ۲۷ مارس ۲۰۲۵
🔹
مدت زمان اجرا: ۱۴ روز
🔹
هدف: بهبود نمایش نتایج جستجو با تمرکز بر کیفیت محتوا
🔹
نوع: این به‌روزرسانی به‌عنوان جریمه عمل نمی‌کند، بلکه صفحات وب باکیفیت را ارتقا می‌دهد.
🔹
گستره: یک به‌روزرسانی جهانی است و بر تمام زبان‌ها و مناطق تأثیر می‌گذارد.
🔹
تأثیر: برخی از سایت‌ها تغییرات چشمگیری در رتبه‌بندی تجربه کرده‌اند.
📌
تأثیرات این به‌روزرسانی بر وب‌سایت‌ها
🔥
برندگان:
✅
سایت‌هایی که محتوای باکیفیت و اورجینال دارند، شاهد بهبود رتبه‌بندی شدند.
✅
وب‌سایت‌هایی که تجربه کاربری (UX) بهتری ارائه می‌دهند، افزایش ترافیک داشتند.
✅
سایت‌هایی که از محتوای تولیدشده توسط کاربران (UGC) به‌درستی استفاده می‌کنند، امتیاز بهتری گرفتند.
⚠️
بازندگان:
❌
سایت‌هایی که محتوای کم‌کیفیت یا کپی‌شده دارند، کاهش رتبه داشته‌اند.
❗️
📉
❌
صفحات دارای تبلیغات بیش‌ازحد یا تجربه کاربری ضعیف، تأثیر منفی دیده‌اند.
❌
وب‌سایت‌هایی که از روش‌های قدیمی سئو (مانند تکرار بیش‌ازحد کلمات کلیدی) استفاده می‌کردند، ضربه خورده‌اند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 902 · <a href="https://t.me/danialtaherifar/848" target="_blank">📅 17:31 · 12 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-847">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔍
تحول به سمت جستجوهای بدون کلیک
📉
بر اساس تحقیقات اخیر، بیش از ۶۰٪ از جستجوها بدون کلیک خاتمه می‌یابند. این یعنی کاربران دیگر نیازی به ورود به وب‌سایت‌ها برای یافتن اطلاعات ندارند، زیرا پاسخ‌های خود را از بخش‌های مختلف SERP مانند (Featured Snippets)، (Knowledge Panels) و (Instant Answers) دریافت می‌کنند. این موضوع باعث کاهش چشمگیر ترافیک ورودی به سایت‌ها شده است.
🔎
چگونه گوگل ترافیک را درون خود نگه می‌دارد ؟
گوگل با توسعه قابلیت‌هایی مانند:
✅
نمایش پاسخ‌های مستقیم در نتایج جستجو
📌
✅
پیشنهاد‌ های Google Suggest
⌨️
✅
باکس‌ های نالج گراف (Knowledge Boxes)
📚
✅
نمایش اطلاعات کسب‌وکارها در گوگل مپ
📍
✅
و حتی قابلیت خرید مستقیم در نتایج جستجو
🛒
در تلاش است تا کاربران را درون پلتفرم خود نگه دارد و از خروج آن‌ها به وب‌سایت‌های دیگر جلوگیری کند.
🚀
استراتژی‌های مقابله با کاهش کلیک‌ها
1️⃣
بهینه‌سازی برای (Featured Snippets)
با ارائه پاسخ‌های دقیق، خلاصه و ساختاریافته به سوالات کاربران، می‌توانید شانس نمایش سایت خود را در باکس‌های ویژه گوگل افزایش دهید.
🔝
2️⃣
تمرکز بر برندینگ و ایجاد آگاهی از برند
اگر کاربران شما را به عنوان یک مرجع قابل اعتماد بشناسند، مستقیماً به سایت شما مراجعه خواهند کرد. حضور پررنگ در شبکه‌های اجتماعی و تولید محتوای ارزشمند می‌تواند به شما کمک کند.
💡
3️⃣
استفاده از داده‌های ساختاریافته (Structured Data)
با اضافه کردن اسکیما مارکاپ (Schema Markup) به صفحات خود، گوگل را قادر می‌سازید تا اطلاعات وب‌سایت شما را بهتر درک کند و در نتایج جستجو نمایش دهد.
🛠
4️⃣
ایجاد صفحات تعاملی و کاربردی
اگر کاربران پس از ورود به سایت شما تعامل بیشتری داشته باشند (مانند مشاهده ویدیو، خواندن محتوای کامل)، گوگل این را یک سیگنال مثبت در نظر گرفته و سایت شما را در رتبه‌بندی بهتر قرار خواهد داد.
📈
5️⃣
تنوع‌بخشی به منابع ترافیک
به جای تمرکز صرف بر ترافیک ارگانیک، از روش‌های دیگر مانند بازاریابی ایمیلی، تبلیغات پولی، فعالیت در شبکه‌های اجتماعی و استراتژی‌های محتوایی ویدئویی استفاده کنید.
🎯
🌟
با پذیرش این تغییرات و تطبیق با روندهای جدید، کسب‌وکارها می‌توانند در دنیای جستجوهای بدون کلیک نیز موفق باشند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 883 · <a href="https://t.me/danialtaherifar/847" target="_blank">📅 18:03 · 06 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-846">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔹
🚀
گوگل قوانین جدیدی برای استراکچر دیتا و بازگشت کالا اعلام کرد!
🔍
گوگل اخیراً الزامات داده‌های ساختاریافته (Structured Data) برای سیاست‌های بازگشت کالا را بروزرسانی کرده است. این تغییرات بر نحوه نمایش اطلاعات در نتایج جستجو تأثیر می‌گذارد و فروشگاه‌های آنلاین باید سریعاً اقدام کنند!
🛒
📊
💡
چه چیزهایی تغییر کرده است؟
✅
شفافیت بیشتر در نمایش اطلاعات بازگشت کالا
🔄
🔍
✅
ضرورت استفاده از استراکچر دیتا برای سیاست‌های بازگشت
📌
📊
✅
نیاز به مشخص کردن مدت زمان بازگشت، شرایط و هزینه‌ها
⏳
💰
نمونه به‌ روز شده از JSON-LD برای داده‌های ساختاریافته سیاست بازگشت کالا که دقیقاً مطابق با مشخصات جدید گوگل است:
"hasMerchantReturnPolicy": {
"
@type
": "MerchantReturnPolicy",
"applicableCountry": "CH",
"returnPolicyCountry": "CH",
"returnPolicyCategory": "
https://schema.org/MerchantReturnFiniteReturnWindow
",
"merchantReturnDays": 30,
"returnMethod": "
https://schema.org/ReturnByMail
",
"returnFees": "
https://schema.org/FreeReturn
"
}
🔹
بخش merchantReturnDays: حداکثر تعداد روزهایی که مشتری می‌تواند محصول را بازگرداند (در اینجا 30 روز).
🔹
بخش returnFees: مشخص می‌کند که آیا بازگشت کالا رایگان است یا هزینه دارد (در اینجا Free یعنی رایگان).
🔹
بخش returnMethod: نحوه بازگشت کالا (در اینجا Mail یعنی ارسال پستی، می‌تواند "InStore" هم باشد).
🔹
بخش returnShippingFeesAmount: هزینه ارسال برای بازگشت کالا (0 دلار یعنی رایگان).
📢
این استراکچر دیتا باعث می‌شود گوگل بتواند سیاست‌های بازگشت کالا را به‌درستی در نتایج جستجو نمایش دهد و تجربه بهتری برای کاربران ایجاد شود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 972 · <a href="https://t.me/danialtaherifar/846" target="_blank">📅 10:28 · 25 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-845">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQdmGzNfcXqFLxyZ4uSVLriovcNoQuMPkDf0FsRQE3LI3vz02-HDllbfWtTSIllDG4vk4i0tfJDmQXe1kN-vAbo0MSDd1MAt_KjoCww2NncKagAQZR9aiH72fzdmukRAgq6btxUSGhVXv9jyW3ZGSBIjxGxi6agCIpQ0z3xQm2dCWfyaSDpQOjbC7TnJrIVDA5J77N1vIJiwRdn6ugxvn3LYTDjTxbdWBV-LWCch0OTkvaRg26J_kNyyjn6Qzv8hm2rVU8GeCQOsbkiF0Sx2Dct_f4EOaFk_jOdIJcqL3GR-koI0BXMqTM7WxFCWxpJvqo3Z9FtW3BjtthrL-1BXpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل آغاز آپدیت هسته‌ در مارس 2025 را اعلام کرد
📅
گوگل از چند روز گذشته فرآیند انتشار به‌روزرسانی جدید الگوریتم هسته‌ای خود را در ماه مارس 2025 آغاز کرده است. این تغییر مهم به‌تدریج در حال پیاده‌سازی است و انتظار می‌رود طی چند هفته آینده به‌طور کامل اعمال شود.
🎯
هدف از این به‌روزرسانی چیست؟
⚖️
گوگل اعلام کرده که این به‌روزرسانی با هدف بهبود تجربه کاربران و ارتقای جایگاه محتوای باکیفیت طراحی شده است. به این معنا که وب‌سایت‌هایی با محتوای ارزشمند، مرتبط و کاربرپسند از مزایای بیشتری برخوردار خواهند شد. در مقابل، سایت‌هایی با محتوای کم‌ارزش یا پر از کلمات کلیدی نامرتبط ممکن است با چالش‌هایی روبه‌رو شوند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 717 · <a href="https://t.me/danialtaherifar/845" target="_blank">📅 08:36 · 24 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-843">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwrlLeY75W_mdeY3z4y1cQ-FG0TnACtPR5wJfPaYAzEM41X7QGQr3zULgQQHtdoMl7E_8cf2cOBgoOl8aK2sHYhsMgE_sfujA54r-PO7oH3_cQvGa645zCDAw9gWcFsO__AwrVjg_CHvDDazHbjvj8jl2JlHSd60Pr_l2rvPThrJFLSf3wyT8xkKgB9K4UzxdnRm1qVeuVX49wUCOCvMi7rhbFJSVfSUEuL56mCMN0YGdELz5-JmCMJgHuIaMtxmgrKQ7wza6uOtex22-C9zdxh9kbbVO1h6jy_MRez5hCo4BAH2ILN7hL0botxq63ufTuha88S6Vcb_6-vs9wHPXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
🚫
ریدایرکت کردن صفحات 404 به صفحه اصلی کار درستی نیست!
📢
مارتین اسپلیت
، یکی از کارشناسان گوگل، به تازگی در مورد یه اشتباه رایج سئو صحبت کرده: ریدایرکت کردن صفحاتی که خطای 404 (صفحه پیدا نشد) دارن به صفحه اصلی سایت.
💬
به گفته‌ی اسپلیت، این کار نه‌ تنها کمکی به تجربه کاربری نمی‌کنه، بلکه می‌تونه برای سئو هم دردسرساز بشه! وقتی یه صفحه خطای 404 داره, بهتره به جای ریدایرکت به صفحه اصلی، یه صفحه اختصاصی 404 طراحی کنید، که کاربر رو راهنمایی کنه یا اون رو به یه صفحه مرتبط بفرستید.
❓
چرا این موضوع مهمه ؟ چون گوگل می‌خواد بفهمه محتوای سایتتون چیه و
ریدایرکت بی‌منطق
می‌تونه سیگنال‌های اشتباه به موتور جستجو بفرسته. این کار ممکنه باعث بشه صفحات ارزشمند شما ایندکس نشن و سایتتون دچار مشکل بشه!
🚧
@danialtaherifar</div>
<div class="tg-footer">👁️ 774 · <a href="https://t.me/danialtaherifar/843" target="_blank">📅 13:33 · 19 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-842">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRSPCxoIIHoBil42VBMuEn43P8jv2qCYfI1u7Ut7XkgFCjguNyPTyvMkMDNIStLQgjIh-tWona9nOzyDjKbtbtajrDvKTd4IKeMp9yGsPza3_3fKSGbqNcdNWGgl8rjg6DeiQXFQLWMw_6KvG9yTp0OOI5SwaCST7z_WGykQqcOS_VHTbjmDmpN7IoP_TRKPxTg7YXfqurNPCpNJVR6WKajqd139MrnXm9W2gsimYtmkEhjK7xxs6JrT6NJ9Uu4YjtOpDDnKc6TY9ACh94CyykaEL2obDOpFw8Itufs3JpuxHu6ja5IwJGH1O-9mmLK4HGz3GykQRPsxTEeU7w-Omw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
هوش مصنوعی AI Overviews گوگل، دشمن جدید سئوکاران؟!
🔍
تحقیقات اخیر نشان می‌دهد که با افزایش استفاده گوگل از
هوش مصنوعی (AI Overviews)
در نتایج جستجو،
نرخ کلیک (CTR)
وبسایت ها به‌ طور قابل‌ توجهی کاهش یافته است. این تغییرات می‌توانند تأثیرات مهمی بر استراتژی‌های سئو و بازاریابی دیجیتال داشته باشند.
🔹
نتیجه؟ کاهش ترافیک سایت‌ها و چالش جدید برای سئوکاران!
🚨
💡
چگونه در این رقابت حضور داشته باشیم ؟
✅
محتوای ارزشمند و تعاملی تولید کنید
✍️
🔥
✅
بهینه‌ سازی برای AI Overviews را جدی بگیرید
⚙️
🤖
✅
از داده‌های ساختاریافته (Schema) استفاده کنید
📊
🔗
🌐
با توجه به تغییرات اخیر در نتایج جستجوی گوگل و افزایش استفاده از هوش مصنوعی، ضروری است که کسب‌ و کارها و وب‌ سایت‌ها استراتژی‌ های خود را متناسب با این تغییرات تنظیم کرده و به
بهبود تجربه کاربری
و
ارائه محتوای با کیفیت
تمرکز کنند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 770 · <a href="https://t.me/danialtaherifar/842" target="_blank">📅 12:40 · 17 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-840">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TJ7sRvSS4cKZXIBPYiX6mQgJGsNNXRedJGrroJ4DfoiMUlgE8yOUNWu_agw2CQ-VULNdXHqJ1ZEyrHOdCJrQYAK_40aRwegq7MC5PUy4DA4IrpsZLn8dXIxnCB4CIy1E0yqOxlGER-ITG1pdfd0cf6cI33FzQ3igEBT-SOjyjjCF1VQn0O_XpIGMShWTeLS-Rwu6iDqmB5fvVA0CjSsPokDEioWFcXgcjtNCsM35fobXp0yIoz-GDfjeGjuMiDa0Xx64ROHK47SiaEZZTIBUp7byQHkQnOEFLZ5VkmiiAx-7-Y4c7RhpLqgZJzftdP8DNyBL50zj16NB48l_sPLivw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kvgBQZM0xyMC88DXFCN8RdtUcQlq70QqXr1KF7qzBZwsES04655UZ3TpSlkK7I72WZZD7Sau2vOrCu3g_qmDUXqqCTFwiwNNoINenZSBPrFDR2DjCfawUSFo3D0HPZ_fViHmZiwzs1nKtTINF91ircdzwpLAakYRMow8KWCSn8P3lY6M14PIEh2Xg2RVfF47b4ap6ykLdRQjuBqFSdoeW-RDKJNKDmPRL1iZfxUrpZivtbXp6RCqiVq8gHzUAhAAQzxWmlJsVkZLUMlbd3n_PLOnawrmdCfCdQP6OT2YNP5FWVrvG25sdtBB5JbFzMSZH7foxIGt3sksa4U6vAET0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎯
گوگل مستندات تگ متا ربات‌ها را برای اضافه کردن "AI Mode" به‌روزرسانی کرد!
🔹
گوگل اخیراً مستندات مربوط به تگ متا ربات‌ها را به‌روزرسانی کرده و حالت جدیدی به نام "AI Mode" را معرفی کرده است! این ویژگی با بهره‌گیری از هوش مصنوعی، تجربه جستجو را پیشرفته‌تر و دقیق‌تر از قبل می‌کند.
✨
این قابلیت از مدل هوش مصنوعی Gemini 2.0 استفاده می‌کند و توانایی ارائه پاسخ‌های تحلیلی، دقیق و چندوجهی را دارد.
📌
کاربران از طریق یک تب اختصاصی در صفحه جستجو به این حالت دسترسی دارند و می‌توانند اطلاعات گسترده‌تری دریافت کنند.
🔍
چه کسانی می‌توانند از AI Mode استفاده کنند؟
🔹
این ویژگی فعلاً برای مشترکین Google One AI Premium و برخی کاربران منتخب در آمریکا از طریق Search Labs فعال شده است که از این قابلیت برای ارائه اطلاعات خرید نیز استفاده می‌کند تا تجربه کاربران را بهبود بخشد.
🌐
https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag#directives
@danialtaherifar</div>
<div class="tg-footer">👁️ 609 · <a href="https://t.me/danialtaherifar/840" target="_blank">📅 15:37 · 16 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-839">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LqiTPrQt_CImF78VvhnOuHOq-Y7a68owsEQk0IHIKzq4cI5orGb_Rfj1CYi-rK_LFCnbhzD_eF4O6KDW1psaYl36i_kRqrUVwllJsq9_ivXDqgX-oTmY-BjvQoJEK2Rwg_6Rj_PwE8jiWiM3E3AlIAs_t-tIwoErBv521_dDrTPRVlov5CYjXwziGYhYmIUcA2ZwF4KVuNJgS7YbdEjnOSnhb0bSlD-ok7kdLZUW9KW1iFm24Y4ZbfaCkKshJmTb7Y_mdqks_G0V-YjOWcjQg_mhbvbDi9bZ9ef4zTWS6rkDGUyRRTiHz1NIR20l0Ysx5jIOWVjLYf4USkF-9sJauQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل اکنون سالانه بیش از ۵ تریلیون جستجو را پردازش می‌کند!
🚀
🔍
افزایش چشمگیر جستجوها:
بر اساس داده‌های داخلی گوگل تا ژانویه ۲۰۲۵، این شرکت اکنون بیش از ۵ تریلیون جستجو در سال را مدیریت می‌کند.
📈
رشد قابل‌ توجه:
در سال ۲۰۱۶، گوگل اعلام کرد که سالانه ۲ تریلیون جستجو را پردازش می‌کند. این افزایش به بیش از ۵ تریلیون نشان‌دهنده رشد مداوم و قابل‌توجه در حجم جستجوهای گوگل است.
🤖
نقش هوش مصنوعی:
گوگل با استفاده از فناوری‌های هوش مصنوعی، تجربه‌های جستجوی غنی و چندرسانه‌ای مانند AI Overviews، Circle to Search و Lens را ارائه داده است. این ابزارها به کاربران امکان می‌دهند تا به‌صورت طبیعی‌تر و دقیق‌تر آنچه را که می‌خواهند بیان کنند.
🛍
افزایش جستجوهای تجاری:
با معرفی AI Overviews، حجم جستجوهای تجاری افزایش یافته است که فرصت‌های بیشتری برای کسب‌وکارها فراهم می‌کند تا با مصرف‌کنندگان ارتباط برقرار کنند.
این دستاورد گوگل نشان‌ دهنده تعهد مداوم این شرکت به
بهبود تجربه جستجوی کاربران
و
پاسخگویی به نیازهای متغیر جامعه دیجیتال
است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 621 · <a href="https://t.me/danialtaherifar/839" target="_blank">📅 18:57 · 15 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-837">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNVUyOLuHZuAODaZjxHwxw_hSlbr3Jxnr1qYA7MuVajNaa9Sry242B5lr9tfR5lgoVhXnZu8jbXfsxaxpnCcY7OoQeMmoHN6Kt7mszGl9AOkjCtCTCoRUFI9K0USC49L1AgXtKw55_Ig1rmBQmdqtVIHD9bFSswQ1C4zr5EPSeGbAEi2BpgwC-cvSD9-IEAlU4BQpKZr3Wq1zscAEjlWa2u_ffFD157vVweJxTobs-KnlPzJIftppVI6YZ3pFtJJaHvGREPDkrcD56i8nlyd08yCkoTXXzkIZ1y3zMxIM4qcC9v36csxDeXFcVc97_TEFJleswBV7Yu5sz0Jn3LzYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل در برابر محتوای کم‌ کیفیت اما خوش ظاهر سختگیر می‌شود!
🚨
🔎
بسیاری از سایت‌ها با استفاده از
محتوای تولید شده توسط هوش مصنوعی
،
بازنویسی‌ های سطحی
و
اطلاعات عمومی
سعی می‌کنند رتبه خوبی در گوگل بگیرند. این نوع محتوا معمولاً ظاهری حرفه‌ای دارد اما در عمق خود،
چیزی جدیدی به کاربر اضافه
نمی‌کند. گوگل با استفاده از الگوریتم‌های پیشرفته، این محتوا را شناسایی و رتبه آن را کاهش می‌دهد.
📉
⚠️
محتوای ضعیف چه ویژگی‌ هایی دارد ؟
❌
استفاده از جملات کلی و بدون اطلاعات دقیق
❌
تکرار مطالب عمومی که در سایت‌های دیگر وجود دارد
❌
عدم ارائه پاسخ‌های عمیق و مفید به سوالات کاربران
❌
استفاده بیش از حد از هوش مصنوعی بدون ویرایش انسانی
❌
هدف‌ گذاری فقط روی کلمات کلیدی بدون در نظر گرفتن نیاز کاربر
✅
اگر می‌خواهید در رتبه‌های برتر گوگل بمانید، محتوای شما باید
ارزشمند
،
کاربردی
و
واقعی
باشد، نه فقط
پر زرق‌ و برق
!
✍️
📚
@danialtaherifar</div>
<div class="tg-footer">👁️ 662 · <a href="https://t.me/danialtaherifar/837" target="_blank">📅 09:11 · 14 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-836">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">📢
تحول بزرگ در سئو: حرکت به‌ سوی سئوی معنایی و وکتورها !
🚀
🔍
🔥
گوگل دیگر فقط به کلمات کلیدی توجه نمی‌کند! با پیشرفت سئوی معنایی، موتورهای جستجو از وکتورها برای درک ارتباط مفهومی بین کلمات استفاده می‌کنند.
🧠
🔎
وکتورها: راز درک هوش مصنوعی
🤖
وکتورها ابزاری ریاضی هستند که هوش مصنوعی برای درک و سازمان‌ دهی اطلاعات فراتر از متن ساده استفاده می‌کند. به جای تکیه بر تطابق دقیق کلمات کلیدی، موتورهای جستجو اکنون از vector embeddings استفاده می‌کنند که کلمات، عبارات و حتی تصاویر را بر اساس معنای آن‌ها و روابط‌شان در فضایی چندبعدی ترسیم می‌کند.
🌐
🔗
🎯
به این صورت فکر کنید: اگر یک تصویر ارزش هزار کلمه را داشته باشد، وکتورها نحوه ترجمه این کلمات به الگوهایی هستند که هوش مصنوعی می‌تواند آن‌ ها را تحلیل کند.
🖼
➡️
🧠
💡
برای متخصصان سئو، این‌گونه می‌توان تشبیه کرد: وکتورها برای هوش مصنوعی همانند داده‌های ساختاریافته برای موتورهای جستجو هستند، روشی برای ارائه زمینه و معنای عمیق‌ تر.
📊
🌐
چگونه وکتورها جستجو را تغییر می‌دهند؟
🔄
با استفاده از
semantic relationships
,
embeddings
و
neural networks
جستجوی مبتنی بر وکتور به هوش مصنوعی این امکان را می‌دهد که هدف کاربر را به جای صرفاً کلمات کلیدی تفسیر کند.
🧠
💬
🔑
به این معناست که موتورهای جستجو می‌توانند نتایج مرتبط را حتی زمانی که یک کوئری شامل کلمات دقیق از یک صفحه وب نباشد، نمایش دهند. برای مثال، جستجو "کدام لپ‌تاپ برای بازی بهترین است؟" ممکن است نتایجی را نشان دهد که برای "لپ‌تاپ‌های با عملکرد بالا" بهینه شده‌اند، زیرا هوش مصنوعی ارتباط مفهومی این کلمات را درک می‌کند.
💻
🎮
📸
وکتورها چگونه به هوش مصنوعی کمک می‌کنند که محتواهای غیرمتنی را تفسیر کند؟
عبارات عامیانه (مثلاً "دندان روی جگر گذاشتن" در مقابل "تصمیم سخت گرفتن")
💬
تصاویر و محتوای بصری
🖼
ویدئوهای کوتاه و وبینارها
🎥
پرسش‌های جستجوی صوتی و زبان محاوره‌ای
🎙
📌
خلاصه: وکتورها در حال انقلاب در نحوه درک و رتبه‌بندی محتوا توسط موتورهای جستجو هستند و نتایج جستجو را مرتبط‌تر می‌سازند، حتی زمانی که کلمات دقیقاً تطابق ندارند!
🔍
✨
آیا برای این تغییرات در نتایج جستجو آماده‌ هستید؟
🤔
👇
@danialtaherifar</div>
<div class="tg-footer">👁️ 610 · <a href="https://t.me/danialtaherifar/836" target="_blank">📅 11:49 · 13 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-835">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔍
اهمیت Customer-Centric:  راز موفقیت در سئو
💡
✨
در Customer-Centric SEO به جای اینکه صرفاً بر الگوریتم‌ های موتور جستجو تمرکز کنیم، تلاش می‌کنیم
نیازها
و
انتظارات واقعی کاربران
را در اولویت قرار دهیم. با بهینه‌ سازی تجربه کاربری، ارائه محتوای ارزشمند و تحلیل مداوم رفتار مشتریان، می‌توان
ترافیک پایدارتر
،
تعامل بالاتر
و
نرخ تبدیل بهتری
کسب کرد. در ادامه، مهم ترین رویکرد های تجربه سئوی مشتری‌ محور رو بررسی می‌کنیم:
1️⃣
تحقیق عمیق درباره کاربران و سفر مشتری
🎯
✅
درک نیازها، مشکلات و سوالات کاربران قبل از تولید محتوا
✅
بررسی پرسوناهای مشتری و تحلیل داده‌های جستجو برای یافتن موضوعات پرتقاضا
✅
استفاده از ابزارهایی مانند Google Analytics، Google Search Console و ابزارهای سئو مانند SEMrush و Ahrefs برای تحلیل رفتار کاربران
2️⃣
ایجاد محتوای ارزشمند، کاربردی و مرتبط
📝
✅
تولید محتوا با تمرکز بر نیازهای واقعی کاربران نه صرفاً برای رتبه گرفتن
✅
استفاده از فرمت‌های مختلف محتوا مثل متن، ویدیو، اینفوگرافیک، پادکست و محتوای تعاملی
✅
ارائه راهنماهای جامع، پاسخ‌های دقیق به سوالات کاربران و محتوای همیشه سبز
3️⃣
بهینه‌ سازی تجربه کاربری (UX) و رابط کاربری (UI)
🖥
✅
ناوبری ساده و کاربرپسند برای یافتن سریع اطلاعات موردنیاز
✅
دسته‌بندی شفاف محتوا و استفاده از CTA (دکمه‌های دعوت به اقدام) بهینه‌شده
✅
ایجاد تجربه‌ای یکپارچه در همه دستگاه‌ها و توجه به دسترس‌پذیری (Accessibility)
4️⃣
بهبود سرعت سایت و بهینه‌سازی عملکرد فنی
⚡️
✅
افزایش سرعت بارگذاری صفحات برای کاهش نرخ پرش (Bounce Rate)
✅
استفاده از فرمت‌های سبک‌تر تصاویر (WebP) و فشرده‌سازی کدهای CSS و JavaScript
✅
بهینه‌سازی کش سایت و استفاده از شبکه تحویل محتوا (CDN)
5️⃣
تمرکز بر بهینه‌سازی موبایل (Mobile-First SEO)
📱
✅
طراحی سایت به‌صورت Mobile-First با رعایت اصول ریسپانسیو
✅
حذف عناصر اضافی که باعث کاهش سرعت در موبایل می‌شوند
✅
تست سایت در ابزار Google Mobile-Friendly Test
6️⃣
اعتمادسازی و افزایش اعتبار سایت (E-E-A-T)
🔒
✅
نمایش نظرات مشتریان، گواهینامه‌ ها و نشان‌ های امنیتی
✅
ایجاد صفحات درباره ما و تماس با ما برای افزایش اعتبار
✅
استفاده از لینک‌ سازی داخلی و خارجی معتبر برای تقویت سیگنال‌های E-E-A-T (تجربه، تخصص، اعتبار و اعتماد)
7️⃣
سازماندهی و ساده‌ سازی محتوا برای اسکن سریع
🔍
✅
استفاده از تیترهای مناسب (H1، H2، H3) برای ساختاردهی بهتر محتوا
✅
استفاده از لیست‌های شماره‌دار و بولت پوینت‌ها برای خوانایی بهتر
✅
ایجاد بخش FAQ (سوالات متداول) و خلاصه‌های کلیدی برای کاربرانی که سریع اسکن می‌کنند
8️⃣
بهینه‌ سازی نرخ تبدیل (CRO) برای CTAها
🎯
✅
طراحی دکمه‌های دعوت به اقدام (CTA) واضح، برجسته و ترغیب‌کننده
✅
تست A/B برای بهینه‌سازی نرخ تبدیل و بهبود مسیر کاربر
✅
ایجاد صفحات فرود (Landing Pages) جذاب و کاربردی
9️⃣
استفاده از داده‌ها و تحلیل مستمر برای بهبود عملکرد
📊
✅
بررسی رفتار کاربران با ابزارهای تحلیلی و شناسایی نقاط ضعف
✅
آزمایش و بهینه‌ سازی مداوم بر اساس داده‌ های به‌دست‌آمده
🔟
استفاده از مدیا و گرافیک‌ های جذاب برای تعامل بیشتر
🎨
✅
ترکیب متن با تصاویر، ویدیوها، اینفوگرافیک‌ها و نمودارها
✅
استفاده از تصاویر سبک و جذاب برای بهبود تجربه کاربری
✅
بهینه‌ سازی ویدیو ها با قابلیت نمایش سریع و کم‌حجم
⚡️
با اجرای این رویکرد، نه‌ تنها سایت شما برای کاربران مفیدتر خواهد شد، بلکه گوگل نیز به دلیل ارائه تجربه بهتر به کاربران، وبسایت شما را در رتبه‌ های بالاتر نمایش می‌دهد.
🚀
@danialtaherifar</div>
<div class="tg-footer">👁️ 670 · <a href="https://t.me/danialtaherifar/835" target="_blank">📅 10:49 · 12 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-834">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">📢
هشدار گوگل درباره خطای "Noindex Detected" در سرچ کنسول!
🔍
گوگل اخیراً درباره خطای "Noindex Detected" در گزارش پوشش ایندکس سرچ کنسول توضیحاتی ارائه کرده است. این خطا نشان می‌دهد که گوگل یک صفحه را شناسایی کرده اما به دلیل وجود تگ noindex، آن را ایندکس نکرده است.
⚠️
چرا این اتفاق می‌افتد؟
🔹
اگر این تگ عمداً برای جلوگیری از ایندکس شدن صفحات خاص اعمال شده باشد، جای نگرانی نیست.
🔹
اما اگر ناخواسته اضافه شده باشد، ممکن است باعث حذف صفحات مهم از نتایج جستجو شود.
✅
راه‌حل‌ها برای رفع این مشکل:
1️⃣
بررسی سرچ کنسول: از ابزار URL Inspection استفاده کنید تا ببینید آیا صفحه موردنظر دارای تگ noindex است یا خیر.
2️⃣
حذف تگ noindex: اگر صفحه باید ایندکس شود، تگ noindex را از بخش هد (head) HTML حذف کنید.
3️⃣
بررسی فایل robots.txt: از آنجایی که گوگل دیگر از دستور noindex در فایل robots.txt پشتیبانی نمی‌کند، نباید از این روش برای جلوگیری از ایندکس استفاده کنید.
4️⃣
کنترل متا تگ‌ها و هدرهای HTTP: برخی مواقع، دستور noindex در هدرهای HTTP تنظیم شده است. مطمئن شوید که این تگ به‌طور تصادفی در تنظیمات سرور اعمال نشده باشد.
5️⃣
بررسی دستورات جاوااسکریپت: برخی اسکریپت‌های جاوااسکریپت می‌توانند به‌طور دینامیکی تگ noindex را به صفحه اضافه کنند. بررسی کنید که کدهای جاوااسکریپت باعث این مشکل نشده باشند.
6️⃣
بررسی تنظیمات سیستم مدیریت محتوا (CMS): برخی CMSها مانند وردپرس، جوملا و دروپال ممکن است گزینه‌هایی برای جلوگیری از ایندکس شدن صفحات داشته باشند. این تنظیمات را چک کنید.
7️⃣
بررسی تأثیر CDNها مانند Cloudflare: برخی شبکه‌های تحویل محتوا (CDN) مانند Cloudflare ممکن است بر نحوه ایندکس شدن صفحات تأثیر بگذارند. پیشنهاد شده است که موارد زیر بررسی شوند:
🔸
بررسی Transform Rules: ممکن است تنظیماتی وجود داشته باشد که محتوای صفحه را برای گوگل تغییر دهد.
🔸
بررسی (Response Headers): بررسی کنید که Cloudflare تگ noindex را در هدرهای HTTP اعمال نکرده باشد.
🔸
بررسی کش (Cache): گاهی اوقات کش Cloudflare نسخه‌ای از صفحه را به گوگل نمایش می‌دهد که دارای noindex است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 672 · <a href="https://t.me/danialtaherifar/834" target="_blank">📅 14:38 · 11 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-833">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhDntTI4l4nHDqkZClbPLdaev1DdZoeHKbEFZbxNETOjwR9yOyFpPcBCz8KRtN2G-mCNGpyJ6viYBwToibTSoyOlpmGyLeCUw3aCPkrLQ9AaxIEQuwEySTI2BfbYEPvMfnRv_nvcpQLypIDcOC7ob6z6uxWlii8ma2KRbIpBA-RPycTa9g6r-97Q5GKnwetk6fXh8N7tdfiF1CNpiidandw6DaQMQmeXook00EWLewqYX2-qh8GLO8CkqjuExdR_GpsRNV1rdkiCKKh8s1LdCNBKIoCBF6hRYa4uetzMDhmxVtjYDhjGi_c3spvUYaomQjhZSFMIAE_qhMemg9w2pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نرخ‌ ایندکس شدن صفحات در گوگل بهبود یافته است!
🚀
📈
داده‌های جدید نشان می‌دهد که گوگل در حال ایندکس کردن صفحات بیشتری است.
این تحقیق که بر روی بیش از ۱۶ میلیون صفحه وب انجام شده، نشان می‌دهد که نرخ ایندکس شدن گوگل بهبود یافته، اما هنوز بسیاری از صفحات ایندکس نمی‌شوند و بیش از ۲۰٪ از صفحات نهایتاً از ایندکس خارج می‌شوند.
🔍
آیا صفحات شما ایندکس نمی‌شوند؟
اگر صفحات شما در مدت ۶ ماه ایندکس نشده‌اند، احتمالاً دیگر ایندکس نخواهند شد.
🔧
ابزار IndexCheckr
که برای نظارت بر وضعیت ایندکس صفحات طراحی شده، به وب‌سایت‌ها این امکان را می‌دهد که به‌روزرسانی‌های مربوط به ایندکس صفحات خود را دریافت کنند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 657 · <a href="https://t.me/danialtaherifar/833" target="_blank">📅 11:18 · 10 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-832">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hETlObTsfoq4b5QL5xQSam3KEGHyb95-bVhSlIyGeEAqwAa3ecEchr5lbsQ5OOE95FZfJ9QhYlvNoAdkByvJ-Wc6JOMCKyF5tLFtjCblGswVUEQ7mwKfUUN-lhi5Z8U6tk9yRdlMZDkJX7Ot0217Mk-SH9or2oufnCGGpeuxqVA-ktwUn3_gwP5JqSw96v9rKx4tb98bs9iO7M_GY6aiFyqZtizOzMharRyPE3LBo8nh9MHIjjhllT6bdA4mf_JN9lDJzblcDvNuPZAstT9Z5kppe7VwaC0RfXdWD8oYnRZqjEdLMlaXquOmH8d3sH3SHQgfi147bb9QBBC8URHD9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل نسخه جدید Google Ads API v19 را منتشر کرد!
🚀
🔹
ویژگی‌ های جدید و تغییرات مهم:
👇
✅
🎥
تولید خودکار ویدیوهای بهبودیافته برای کمپین‌های Performance Max – ایجاد ویدیوهای با کیفیت بالا به‌صورت خودکار
🎬
✅
🗑
حذف موجودیت‌های مرتبط با فید – استفاده از دارایی‌ ها (assets) به‌جای Feed، FeedMapping و FeedService
📂
✅
🖼
پشتیبانی از تصاویر پرتره ۹:۱۶ در تبلیغات Demand Gen – نمایش بهتر تبلیغات در فرمت عمودی
📱
✅
🔗
بهبود DataLinkService – امکان به‌روزرسانی و حذف لینک‌های داده‌ای یوتیوب
🎥
✅
✈️
هدف‌گذاری برای جستجوهای سفر در همان روز – جذب کاربران برنامه‌ریز لحظه آخری!
⏳
✅
🚫
حذف پشتیبانی از VIDEO_OUTSTREAM – این نوع تبلیغ دیگر در API موجود نیست
❌
✅
🎨
به‌روزرسانی دستورالعمل‌های برند در Performance Max – قابلیت تنظیم رنگ‌ها، فونت‌ها و سایر ویژگی‌های برندینگ
🎭
✅
💬
پشتیبانی از message assets – بهبود تجربه کاربران در تعاملات پیام‌ رسانی
📩
✨
این تغییرات به تبلیغ‌کنندگان و توسعه‌دهندگان کمک می‌کند تا کمپین‌های مؤثرتری اجرا کنند و نتایج بهتری بگیرند!
🚀
💰
@danialtaherifar</div>
<div class="tg-footer">👁️ 702 · <a href="https://t.me/danialtaherifar/832" target="_blank">📅 19:35 · 09 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-831">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=Hv_PhhoQoPgE8SaTFRZMMlDnBWkvJjehBPn_lpD6bYx1DvzT9LMhTL-Qq2CKMSaxmpmFWLo1QQOtLiRh4BpEmGZdctjJeuw4_2DcAZBdc5dxYz6zMHNelDTtt2Bb_vjanfKMCZ1drBnUXLchlcmVEkH02pq2dwsaHM2jlmGnImSoAJe6SHkPFD7KDZfCm7lvvUuIlqE4VrdXsZMaTvEEmg5RnlhARAZzwNK1ELbvjbdHCwdWT4BdCk9iS2SjS8HmE7kLDEeqUlAXheimfuf3dxT-X0l0CgQOSwE1YboInxiX3PMfqPYI_-7u6pSRTZJu6XWwfU0YEGT7bzkB-9RATg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=Hv_PhhoQoPgE8SaTFRZMMlDnBWkvJjehBPn_lpD6bYx1DvzT9LMhTL-Qq2CKMSaxmpmFWLo1QQOtLiRh4BpEmGZdctjJeuw4_2DcAZBdc5dxYz6zMHNelDTtt2Bb_vjanfKMCZ1drBnUXLchlcmVEkH02pq2dwsaHM2jlmGnImSoAJe6SHkPFD7KDZfCm7lvvUuIlqE4VrdXsZMaTvEEmg5RnlhARAZzwNK1ELbvjbdHCwdWT4BdCk9iS2SjS8HmE7kLDEeqUlAXheimfuf3dxT-X0l0CgQOSwE1YboInxiX3PMfqPYI_-7u6pSRTZJu6XWwfU0YEGT7bzkB-9RATg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔍
گوگل با ۶۰ لینک در AI Overview!  آیا کسی روی لینک های پیشنهادی کلیک می‌کند؟
چند هفته پیش گزارش شد که گوگل در حال آزمایش AI Overviews جدیدی است که با Gemini 2.0 تقویت شده و شامل بیش از ۶۰ لینک می‌باشد!
😱
در روزهای اخیر، کاربران بیشتری این تغییر را مشاهده کرده‌اند، اما سؤال مهم اینجاست:
📌
آیا کسی حاضر است روی این ده‌ ها لینک کلیک کند؟
📢
وقتی AI Overview فقط ۳ تا ۵ لینک دارد، ممکن است کاربران یکی از آن‌ ها را باز کنند، اما وقتی تعداد لینک‌ ها ۴۰، ۵۰ یا حتی ۶۰ عدد باشد، تعداد کلیک بر روی لینک های پیشنهادی ممکن است به صفر برسد !
🤔
به نظر شما این تغییر به نفع سئو است یا به ضرر آن !
@danialtaherifar</div>
<div class="tg-footer">👁️ 833 · <a href="https://t.me/danialtaherifar/831" target="_blank">📅 14:26 · 07 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-830">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwLplpCOeIUp66gc5BXwQ-Hp8CmGA2rjlUIKfDOyLTPmZKKKi9RwOCwpX_LHsz6YbX12v7fpa7CnYAU-31rvR6XGZOx04OwTzNIXis_Y8RQA6THoQaGGKMqwJWjjxN4Xa_qe9lmfX_M8xYDo2T9CPpShK9OEBS04dPlth2gPURoCZB2PE23B9Z9u0dSjthwRxafWorkLRGPr9II9ruqXee_0Y-LzNPeP5HEKMphbIqSdrL2-cRfXjZj-8WtDqBgGf3YwTSGHIKHsoKdd9RsSllUxZHGeKZnDGUZLqa6f3UfiM48BpF-YQ6r6w-wSYgPDrbrpfbkO9haYH8GXCxb9sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
زلزله در نتایج جستجوی گوگل ! تغییرات جدید در رتبه‌ بندی
🔥
📢
نشانه‌هایی از یک آپدیت جدید در الگوریتم گوگل!
🔎
ابزارهای مانند Semrush، Mozcast و Advanced Web Rankings تغییرات شدیدی در رتبه‌بندی‌ها را گزارش کرده‌اند.
📉
برخی از وبمسترها از افت ناگهانی ترافیک شکایت دارند، در حالی که برخی دیگر شاهد افزایش ایمپرشن اما کاهش کلیک‌ ها هستند!
👀
هنوز تایید رسمی وجود ندارد، اما همه چیز نشان می‌دهد که گوگل دوباره دست به تغییرات اساسی زده است.
📌
شما هم تغییراتی در سایت خود داشتید ؟
@danialtaherifar</div>
<div class="tg-footer">👁️ 875 · <a href="https://t.me/danialtaherifar/830" target="_blank">📅 12:28 · 06 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-829">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✅
چطور محتوای خودمون رو برای گوگل دیسکاور بهینه کنیم؟
گوگل دیسکاور ماهانه بیش از ۸۰۰ میلیون کاربر فعال داره! حالا تصور کن اگر وب‌سایتت توی دیسکاور نمایش داده بشه، چه حجم ترافیکی می‌تونه جذب کنه!
😍
اما چالش اینجاست که هیچ راه قطعی و تضمینی برای ورود به Google Discover وجود نداره. با این حال، گوگل یه سری نکات رو معرفی کرده که می‌تونن شانس نمایش محتوای شما توی دیسکاور رو افزایش بدن. بیاید ببینیم این نکات چی هستن
👇
🔹
۱. تجربه کاربری (UX) رو جدی بگیر!
متأسفانه توی خیلی از سایت‌های ایرانی به UI و UX اهمیت زیادی داده نمیشه، درحالی‌که گوگل عاشق سایت‌هایی با تجربه کاربری خوبه! پس حتماً روی طراحی و کاربرپسند بودن سایتت وقت بذار.
🔹
۲. از تصاویر باکیفیت استفاده کن
محتواهای تصویری جذاب و باکیفیت، شانس ورودت به دیسکاور رو بالا می‌برن. یه تصویر خوب می‌تونه بیشتر از هزار کلمه حرف بزنه!
📸
🔹
۳. قوانین محتوای Google Discover رو رعایت کن
گوگل دوست نداره محتواهای غیرشفاف، گول‌زننده یا پر از تبلیغات باشن. پس رعایت این موارد ضروریه:
✔️
شفافیت محتوا (Transparency)
✔️
بدون کلیک‌بیت (No Clickbait)
✔️
بدون تبلیغات بیش‌ازحد (No Excessive Ads)
✔️
بدون اطلاعات نادرست (No Misinformation)
✔️
بدون محتوای نامناسب یا جنسی (No Sexually Explicit Content)
✔️
بدون الفاظ رکیک و توهین‌آمیز (No Profanity)
🔹
۴. امنیت سایتت رو تأمین کن
🔒
سایتی که امنیتش تأیید شده باشه (مثلاً با SSL)، امتیاز بیشتری از سمت گوگل می‌گیره و اعتماد کاربران رو هم افزایش میده.
🔹
۵. سیگنال‌ های EEAT رو تقویت کن
اگر گوگل حس کنه محتوای سایتت حرفه‌ای، معتبر و قابل‌اعتماد هست، احتمال دیده شدنش توی دیسکاور خیلی بیشتر میشه.
با رعایت این نکات، می‌تونی شانس ورود محتوای سایتت به گوگل دیسکاور رو افزایش بدی و از این منبع قدرتمند، کلی ترافیک رایگان جذب کنی!
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/danialtaherifar/829" target="_blank">📅 11:08 · 01 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-828">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGjpAcO03o-uNap7SlYcOogp7KmRpdg_HQpq-anmIy00wvUSw6aAhC2sSG9mgyIuSJoNcXoVTfjg_Y7abDXSr-Eb78ebhPzbsvzjGmQDlYl4qPVQuyGU5rA38i2RRm5ei07HsDDtOx1AB8atJMZEdZ8Hih6UiPNnTIeKi5MwnOR5Y09jyAGSKFGhR3MDZIrhasxGV6U7bjknvaibLI47h1tTR1qKw9omG2ylfsNsZK7AIHkEUXK5Nb1AQaaR4T4y22U0SE3H7tifApH6a6bAII0W-C292PfaHYmyY8pyfQ6BrUSXIegsG_HB57l-ObZVyqFhfHuU4OTmlWLeKsH_mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مسدود شدن اکانت آنالیتیکس سایت های ایرانی
⚠️
اطلاعیه رسمی گوگل؛
‼️
اخیراً فعالیت نامناسبی در ارتباط با حساب Google Analytics شما شناسایی کرده‌ایم. بنابراین، ما دسترسی به اکانت‌های شما را به حالت تعلیق درآورده‌ایم، و همانطور که در بخش 14 شرایط خدمات Google Analytics بیان شده است، خاتمه سرویس Google Analytics و شرایط مربوط به اکانت‌های شما را آغاز کرده‌ایم.
⛔️
نکته؛ اگر اکانت دیگر سایت های شما مسدود نشده، در تنظیمات اکانت تایم زون رو روی کشورهای همسایه قرار بدید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/828" target="_blank">📅 23:54 · 20 Dey 1403</a></div>
</div>

<div class="tg-post" id="msg-827">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GoogleBot-ips.json</div>
  <div class="tg-doc-extra">16.2 KB</div>
</div>
<a href="https://t.me/danialtaherifar/827" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
لیست آیپی های گوگل بات، آپدیت 8 اکتبر
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/danialtaherifar/827" target="_blank">📅 12:50 · 22 Mehr 1403</a></div>
</div>

<div class="tg-post" id="msg-825">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EaX-kwTE6aMqo0_c9z6XI0THIGVfX4YHhYJ9CLXpiZ_0pkYPpm0W32C9RkMdTsozuvuMUcruSbW6oCIks0vg-ZMGOsZYBcwXYVi2UtA3mrrXRl_MlaEzv5mAs1a7XLJkLoEeBL9Z-wQDJMp5XenLkdr8Bt6yvI5TQefsNpNBt2ned8N2BFSGi1KS4HXNtOV4FVdWfTLMvKMkCwkcmjKUuW86jXNJDj3CPup1ozR3efU7S7465u8lk3ooLYJKhrkq56lqJSd-uO0CBLH6_nmmcuIWj-ZpaLJp0xV4gE4UHDKWaU75VGw3tXULkv67FUF7BFWmFOkZeF3MRMGQbI1lGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vQXRQS8V73MMyjfIiMsgIVLgSy7rqkn58OZVSVEkt_iccIm_JFSImWaQo1QTviVsJWTtVGHS114EzPM6Yl0Rfa-TNcRU2otsBr1BVkz3QWSsfjDRocSmlteYLrazmRxJ7g8ZXVlBjwmi-muj8T9iKtUcsm7D7aBstulmeC21ZLgi_yL_uuVxWJKdAfdX8XAizKm6PBRRF76PvxRTKF3OmUhrKpk0rkV__nfJig0pWBUCGDeq53NppXRhaFskBtaYbKfOCq6StZvXGzyNfGjH2Yz9gjOLS-9BmRcCeXEBqhUei30RTt8z1QodfAM2XSJtBxBNO4RT6MbAqz1v-86F-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
گوگل در حال تست نمایش قالب ویدیویی جدید در نتایج جستجو است
♨️
در این تست گوگل، باکس ویدیو ها و تصاویر آن کوچک تر نمایش داده میشود.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/danialtaherifar/825" target="_blank">📅 11:21 · 23 Tir 1403</a></div>
</div>

<div class="tg-post" id="msg-822">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C33f22Okn9PaZ3c-szQMRv56HL5yOS4B4JPheCrGZ06TZ9tm27WmKf5ZPGdUYVSzYLEhWpvUNSUTZr8P38vcJSxN5KsCVfwfljfrq2ro9gl0V3FH6P1QjK4RSdGjQ90KksU1ABe0zKQcK8oHFgtkGp_5cN4ioMt9HZZO3zLy5aINK2sM9AJ7Z0gBSPwhzwKpiyPn1MgcXj5ql7OiMf_RoDw8WLU4Gu3hwtu3bhrkUp_TNASuXkQVQ60XlQjgS7FuSfEbGWazzlPZyldaKrKVcFsEVdHdgYfJp4GojBcNItZnzXMh95Wnv6PoGXogKEfpZE4c2WUcmXxx5KGRJW-KPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CgE-rjHvVWhARSsKKt490e1_YPb3Txzia2Gut4hWDH6cnMtd_mwLbbSGsRfyI8PCJwGSCuOaAk6A0PN5gr-SYAlBPK_XJ0jZOeXLL5ie1LFSuzG4k0G4Z1_ZXHwAa2YoiY7fWiLzremLje9x9c4rnnWedPjZOhsV_o0JWi3UkwyPgjGYKmzk2Ai0f0yc-iOA-pAL-sZcDjqmraQgIoeLz9IKylUK3iSBoU7BiJoVuv6irNkhIJN7_j_-VX4eDCEWM4aM-zd9zNACAXMLbLp8Zt2A_lc6tE4W78iBthhc3vwkRNqX2ZG8D4OQz7tnlyjXL7Y2LgWjO931Vsn20LRQjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DXsCBaDDoawpJIX3pHuGe4jtgbcTwOn0ZFlhHrMu7rqU_DuO7kXcyeo92OFl9FxVMmSIMo3VLL9A1E4znm6gnauDM-EwAuBmLRoDEbHOT0ujSxBFToZTP0YmgFEa103LdLAhhjxSNx47S586ezkFSH0Xh8beHzKQrB_rlD8tIQ80eh6JH0tqwqz5JhRNFU3i8HTITYSELepHAPK2rLlrrqnxkVNbAIdw4BnXu7TTEukRIyiU99PIjwmD6FuesQPW_gIGK-lSBAtplGdKwY-jgoqGB5P5QHqDgHxkoT8KEzn6qpkXR2Gwg9-11dYncbvocR429WZfwJkbOBIw-AnPAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
وضعیت ناپایدار الگوریتم های گوگل در چند روز گذشته !
🗣️
تغییرات زیادی به ویژه June 5th در نتایج سرپ ایجاد شده که نشان از یک بروز رسانی جدید و نوسانات شدید در نتایج گوگل هستیم اما هنوز گوگل این نوسانات و آپدیت جدید رو تایید نکرده است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/danialtaherifar/822" target="_blank">📅 15:46 · 17 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-821">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=QWUtgSgroFlkd59_k2_wQbCBGincIwLDsqXqc7GSf9T549jx7YpLxKTb3XZUnKjZrIGijYv7eCUxNy1U2YIoLfEN9ZT4avx28JEUYchA8jtQfsk1SdHwDXGeTAyqO1CumstW7a3QB5BT65Z_WxGXBCotKdRlN-13XUhTENCHOhF2zA_WiBwTPHA2vzHAUfSuKazhXKqov_VqMktC8fqa4Y3RSOfcqswe6GxtUcu8df5O8zfouijoRfcCutUdte1vxDij4h6qjuaZGUYjUA-rxv0rahqPh2bEE8ZpjMRP26sneG0JerkQZKdwukUdNW-b-Wd-GTO9bHbO9oQB167OjHavYLfasSFqjlZU90JflSA0_y8v1VMh0Bxa_26hgESVd757f68wgkGt2ogj4qpbim6U9j8yD8SlJL_D8uLgrS5qB3uKZVWqmkYtJOdFmnYMC6aIi5w_hW0TGo_sxJ3l4GU38TPJzvFhAvYeXiDSgAvkxDpVBWze1doTZDLGFk_2P6BOPql7IC5w_xigwAsAiIE3T6mlwJoaGm4JheOWHvfwb9A3Yjq5g35Qf4IO1PXe1PkR7VTwcIagiC8fm9DCoaUFHr-NQiAX9-YgJVb-L9lpYrQwKApqKl6XxCNWdFNmw3VnJEVEUoXgpVa0H1wPOs9By6DSsBxzIgrbgvKi7-Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=QWUtgSgroFlkd59_k2_wQbCBGincIwLDsqXqc7GSf9T549jx7YpLxKTb3XZUnKjZrIGijYv7eCUxNy1U2YIoLfEN9ZT4avx28JEUYchA8jtQfsk1SdHwDXGeTAyqO1CumstW7a3QB5BT65Z_WxGXBCotKdRlN-13XUhTENCHOhF2zA_WiBwTPHA2vzHAUfSuKazhXKqov_VqMktC8fqa4Y3RSOfcqswe6GxtUcu8df5O8zfouijoRfcCutUdte1vxDij4h6qjuaZGUYjUA-rxv0rahqPh2bEE8ZpjMRP26sneG0JerkQZKdwukUdNW-b-Wd-GTO9bHbO9oQB167OjHavYLfasSFqjlZU90JflSA0_y8v1VMh0Bxa_26hgESVd757f68wgkGt2ogj4qpbim6U9j8yD8SlJL_D8uLgrS5qB3uKZVWqmkYtJOdFmnYMC6aIi5w_hW0TGo_sxJ3l4GU38TPJzvFhAvYeXiDSgAvkxDpVBWze1doTZDLGFk_2P6BOPql7IC5w_xigwAsAiIE3T6mlwJoaGm4JheOWHvfwb9A3Yjq5g35Qf4IO1PXe1PkR7VTwcIagiC8fm9DCoaUFHr-NQiAX9-YgJVb-L9lpYrQwKApqKl6XxCNWdFNmw3VnJEVEUoXgpVa0H1wPOs9By6DSsBxzIgrbgvKi7-Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖥
فاکتور های رتبه بندی گوگل لو رفت !
🗣️
این فاکتور های رتبه بندی توسط یک فرد ناشناس در گیت هاب منتشر شده است و میتوان به نحوه عملکرد الگوریتم های گوگل از طریق API های منتشر شده به آن دسترسی داشت.
⚠️
بسیاری از موارد لو رفته جز فاکتورهای رتبه بندی هستند و برخی نیز اهمیت چندانی ندارند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/danialtaherifar/821" target="_blank">📅 11:48 · 09 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-819">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g-D6WcDrPmB2qntudgP21xVGpQSh8_zucSfdITrZ0HAPNqiGdfE3Bw4OGVLKcsxMFQNPuwDzAruAQHTRfd2YeNV893MkXBD7SynP-EH_mzIwf-afH7-_J7PFUZLeKXaFisB_Pij4kes-YZZpi4emQZDkCmQgnrDO5TvIOKgHQS9UEo6VTQbPHwziPrR88J4XJxHaT7yb6X0soLN4EP8BRIv-fDUZZa58X3M-eST-4PGS5OPIoqAcgn1cfXfPeJYsI3NZYxzMJdtZSTQocNs1n0aZvs-WX6RaJ6HrNVS7HGeFYNP3R0_c1nMFZCN5ZNcLhL_smPg_2k4lgytB9yZxig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JDsPyBK5f3BCRCgpMMShvnzN8Nco7gCKxY7jMzZLWSPXnU8SLsYpYelvh2Gt17zrGGnXEugMFgP_llf4suwYJ5ACbDFaliZq4UFgi8p8fcIXJX49VCLKZmBsNitgUfIDtx0kV35MKyzH0JrTFxfhpSHo1lGwifYRaxLD1ZEMHBlNalZwUJlGGa0ZYefqh6d8Iq52-onxUOMCLmfN_2rQWNu3G1lznsfZekffa961uQKSKZoYJIPyjXeoikJ-bLtthIdvK_eyUPcW_e2EMwSQO5XHl2ntJiE_3un8oXP4lkf1if1ZfzBx2qcwlYBEt1muKlHvcV4rCKtYoO_GgC1OMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
جریمه های اخیر گوگل مربوط به Site Reputation Abuse نیست !
⚠️
گوگل تأیید کرده است که تاکنون هیچ اقدام الگوریتمی برای (سوء استفاده از شهرت سایت‌ ها) فعال نشده است. در صورت اجرا، این اقدامات فقط بر محتوای توهین‌ آمیز و ناپسند تأثیر خواهند گذاشت، نه بر کل سایت‌ها.
👀
لیلی ری، متخصص سئو،
اسکرین شاتی
در توییتر به اشتراک گذاشته است که کاهش قابل توجه ترافیک وب‌سایت Groupon از تاریخ ۶ می را نشان می‌دهد. با این حال، سالیوان تأکید کرد که هیچ به‌روزرسانی رسمی منتشر نشده است که این کاهش رتبه را توضیح دهد. این اطلاعات نشان می‌دهد که هرگونه کاهش ترافیک اخیر به دلایل دیگری بوده و به اقدامات الگوریتمی جدید مرتبط نیست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/danialtaherifar/819" target="_blank">📅 12:10 · 06 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-816">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k2Fgobz5y_daQSGEePdQZo-w1Gke7XsqggXqx0RZDaAmMdJfb4HYvYQJJqfZu1umo4y5IXfHSCaRlfYGQJoWJomrd8FAfM0LzMfafGanWmrqja2AzBXK7ppTKN2zjo0-tlddLoSw3Iy1xB22JHCBPWF2afi1ZgaBELdrytISapfn_YG41JHm_cJFSDYVkr2d00v_EtQwY6N_HBILDRIfvW76up_5YFq6PcdZufRWJSbQlDy7OGZ1strqKIbZvE64O0zM5-y1QnGV2airMuKdQ2KjLGfw7Z6YMvcp6PDFZPD0AufvS2BjFCPJTlIQe0ZSbvqSUcohavbJkj5tyMZ6bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ipt9afacFbJjJBhsaJjWpRJ2v3kablVWS-BynWSx_TEqexfTKWG504JRktTsSaiLbqp6DCkFfx2fdm3bHWXboMkwD1Z9dx6Hbw9anzLMqEqNlJlu3TNVvbLxj-CeSKKP9AJsKUGQzcn0LlcG6v0h5mqSkGQF4J6tWMOyasZKo_va-_p7Oh5nyxJizR_zyQsaBe2Q13Vhl1PylXHm1-pbkg3yGmdTWqlGoj41ap9qSzFCprbcYN0b_QZsj_6dokwK8vckF-fwDH8g13zYSgMcxAfYMGQcdb1Nd-DiuW4n2ymEWhsgpDziUSWhDb0SiK8fXPnjk55IUr4bkc6VNabwiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OqhKZco_3FcRmiaaxsA2uEN19sXzz_AQpVBrfJ4E0atOVDMxTjJe7LPfDaq_kQ9CPok8TLypQANvbbCZ95ID4oYxKxspDXe5ifU_dCqoqHJsKgo_0zEkuHPtpCyPTZRo1T1sEopugwmLA2D7DB67V25SK9-Kdtk9JjB6Qm-O2HyacMzZv0nn6Dref4NNGWLA0rML2UqlLAA0GpmlmMRW3q68zoXBUlLJUlJGUN98ggH6CX5yWFZdMvhm31VbAfo86op0SdFnWwFR1eg3nXN9BbkzkgbMVohPYUd6PfX2LjPZXdxXUe4wuYVd5NIe9pTDEeGuw4itct27TAp_UgK-0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😄
وضعیت Google AI Overviews در پاسخ برخی سوالات در آپدیت های اخیر
⚠️
سوال اول:
health benefits of running with scissors
/ فواید دویدن با قیچی برای سلامتی، اینجا گوگل این سوال رو تایید کرده و حتی گفته برای قلب هم بسیار مفیده.
⚠️
سوال دوم:
health benefits of taking a bath with a toaster
/ فواید حمام کردن با توستر برای سلامتی، اینجا هم گفته اره یه راه برای کم کردن استرس هست و باعث میشه آروم بشی.
⚠️
سوال: سوم:
How Many muslim president has the us had
/ ما چند رئیس جمهور مسلمان داشته ایم؟ اینجا هم در جواب گفته بله باراک اوباما مسلمانه در صورتی که مسلمان نیست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/danialtaherifar/816" target="_blank">📅 18:18 · 05 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-815">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=liWqRJtJwWI9X0sCIC1jccqD-lk9cO6GEO9z2j2XUJQ-M0fRvEk_KZEaGFti3jwhFMuwt8LAE4aKWYc-jI6ygoPEwpTZjuDBJyiIRcBrtRQQVRJighccV1lSV51YlKbVD_SjR94wqTZhHCiK2paoCR19NlSCokHJhW8-yB4XFpR2aJcX7fgnUO_EMCgBjJIFeFdTd6WUfy1CQ6S7lz62TMn5Y04a3Cpd18QOZBf4sPsWzPQDg8Kh8EvIONDRxwqdc49AQ-iK2xHBxIHnOADN3hLoKPjPO7ElaVVp0oKw1A82zcO4zgMZYxo5m0ZFo0mvN6Y9PYnIv9DQ91Sl8Zz7m16Vbyf0HG0SpIbiZL2I7gxR_8vasfhThhX8lbaBF0AUbsyK2Rg2Pi-D6olfyLfujOZDuSc2CpvpWK4jQuq_cX5WJIMvNhynfLu1jX9T8a96bWNpr2Hl1EFfbeuTHrdAFsbKwjtUqGJoJOgk0TsGr0c4717wmH5x-d5WIJNoQHL42jl3ZpbAGXnGhgYHm3cCppO5XXpuv9SwLTv8cKU_gHKRTvAHUBrCl-xPyF9K9ZTB8fur2aU94EjnxEUD9HUaBL5IyspfdNZGmaMeIC0VLVFKROFUCc00r-4VWZ_wQ3abouE3Lte4adkBrjfeERLBYh5VG3wiDSFtSd0ut955lbY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=liWqRJtJwWI9X0sCIC1jccqD-lk9cO6GEO9z2j2XUJQ-M0fRvEk_KZEaGFti3jwhFMuwt8LAE4aKWYc-jI6ygoPEwpTZjuDBJyiIRcBrtRQQVRJighccV1lSV51YlKbVD_SjR94wqTZhHCiK2paoCR19NlSCokHJhW8-yB4XFpR2aJcX7fgnUO_EMCgBjJIFeFdTd6WUfy1CQ6S7lz62TMn5Y04a3Cpd18QOZBf4sPsWzPQDg8Kh8EvIONDRxwqdc49AQ-iK2xHBxIHnOADN3hLoKPjPO7ElaVVp0oKw1A82zcO4zgMZYxo5m0ZFo0mvN6Y9PYnIv9DQ91Sl8Zz7m16Vbyf0HG0SpIbiZL2I7gxR_8vasfhThhX8lbaBF0AUbsyK2Rg2Pi-D6olfyLfujOZDuSc2CpvpWK4jQuq_cX5WJIMvNhynfLu1jX9T8a96bWNpr2Hl1EFfbeuTHrdAFsbKwjtUqGJoJOgk0TsGr0c4717wmH5x-d5WIJNoQHL42jl3ZpbAGXnGhgYHm3cCppO5XXpuv9SwLTv8cKU_gHKRTvAHUBrCl-xPyF9K9ZTB8fur2aU94EjnxEUD9HUaBL5IyspfdNZGmaMeIC0VLVFKROFUCc00r-4VWZ_wQ3abouE3Lte4adkBrjfeERLBYh5VG3wiDSFtSd0ut955lbY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖥
بررسی وضعیت سلامت رپورتاژ با اسکریمینگ فراگ
👇
🔗
یکی از مهم ترین اقداماتی که باید در کمپین های آف پیج خودتون انجام بدید، چک کردن وضعیت سلامت رپورتاژ است. در طول اجرای کمپین های مختلف لینک سازی ممکنه محتوای رپورتاژ پاک بشه و یا نوایندکس و حتی در برخی موارد دیده شده مدیر اون رسانه، لینک‌های داخل رپورتاژ رو حذف کردند که در بلند مدت میتونه تاثیر منفی روی سئو سایت شما داشته باشه.
✅
برای بررسی این مورد کافیه مراحل زیر رو در اسکریمینگ فراگ انجام بدید:
1. در منوی اسکریمینگ فراگ روی گزینه Mode کلیک کنید و روی حالت List قرار بدید.
2. در قسمت Configuration > Custom >  Custom Search / روی ADD کلیک کنید و در قسمت Enter Search query نام دامنه خودتون رو قرار بدید.
3. به صفحه اصلی نرم افزار برگردید و لیست رپورتاژ های خودتون رو در یک فایل txt قرار بدید و آپلود کنید. حالا میتونید وضعیت HTTP status، Index و لینک های داخل رپورتاژ در بخش کاستوم سرچی که مشخص کردید مشاهده کنید.
#اسکریمینگ_فراگ
#آف_پیج
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/danialtaherifar/815" target="_blank">📅 10:42 · 26 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-814">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBeV8lskUv8SkwqOwphNaKYXeA8TbK-8ZFD9jGe3h3-br6JuMS2knIamKpu44-8afKOJqReuaxSk3M3aQyv0qpmhSfP7jJOv4QXsJ0Rt5c2okiVFj7jcYWIfGlH6SEuMIyRKrauP_1oF_y9SPkurp3zNhe8b3ewPheGt3Zc8ebXae0tlMXgm2VMpewhjfqccQL0QzaiQCdLZNqptvUuJO64dQxpmlZK3608lAO9XK8T53sGeySiImcs0uO8Rh9yDdJoX96i0XOKepLS_LKSGwM-JSUk5odhVGqTPwEmr-0Q_2XoeWHWoFbIB931o0EUsU92O198jhxn1g4kn7aMTZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گوگل لینک های اسپمی که به صفحات 404 و 410 داده شده را نادیده می‌گیرد
🖥
جان مولر: بک لینک های Spam که به صفحات 404/410 داده شده لینک هایی هستند که به حساب نمی‌ آیند و کاملا بی‌تاثیر هستند و نیازی به disavow کردن این مدل لینک ها نیست.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/danialtaherifar/814" target="_blank">📅 09:54 · 05 Ordibehesht 1403</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
