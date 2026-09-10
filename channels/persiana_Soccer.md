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
<img src="https://cdn4.telesco.pe/file/Gw25KyPZv88yv60EfisI_Cju4JAkyVEcxIG2jfX9ziq_Q0WxvUJhLUvuLt4de37kzDhK6hxSDnx67IurxE_rE-sGSRe6g4NoyQ9NiQrf-qtBxllpCWLCwcusaxKOkqkqjrdLqZC6VdS9hRcwWOLePGAoDLR9EEy487QA0BxoHhhJvUP6jpQMHWjEtvTeGGEkyWyXMpE9sy4SrVYml3D9YkGR-AQxIkTqcjtHp_H3aSbM4lQzmqerE4maELtamiCFR8LqbjX1uMoLgEwSjX-9Z5q_9Cx1LsPfkfOWBbM4y7hNfIualOh2rwBiMKjdopu3EA5FqLdN4atFelsb6XALLw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 538K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 02:47:11</div>
<hr>

<div class="tg-post" id="msg-29502">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgwo1kX9_WIj_NVT4O3rW6Pe81v3YbmDEUD4F5I4LuXXOp0aKtfum7iVJv2XpUccPxx3261TsCkKov2rzpqDMUID3OJ2AwM_v8J-fbsSZt1qIeqONNtLxe_b_UkCdLwIJNjNmoC4InX9qVeWcQ-MUyAASOJujVRZlJvbOTSqEBsLPtXj56bij7gWh_9OMx-wlfkk7xecHwnb-JlzsQOpDgo6YMA-ZdhM_m5NOlJHHibniKlm-tnwnEtDaGDmin9if5UWOJoJfMIDIJs6mHPrprGvdSX3pjXBXu2SOIptAvFyvQppzYQnImK6G1U1AzxtVM0RG0ZT-xnzhvxULprj1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
بعدازتساوی‌مقابل آاس رم؛ اسماعیل کارتال از هدایت تیم فنرباغچه استعفا داد و اعلام کرد دیگر هیچوقت به این باشگاه باز نخواهد گشت. کارتال هر بازیکنیکه میخواست رومدیریت‌براش جذب کرد اما نتایج ضعیفی در همین ابتدای فصل کسب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/29502" target="_blank">📅 02:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29500">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a82a62e0d5.mp4?token=DArD41qI5-mmlyfC2GiMg_z0rXJu5Ib8YvWbiCTrzMaSqE3i6YZfR0Vo-pjmv4vqWB_Z9ukzAMUZ6teBfdBJRxJYDShiJi84jNZyxaWt5HzT71ZYCCOOQOrBbj6xQTAVLMUu0Et91TMIlvr7fBvtoyQjAa4svm_cxhx9qxEAWJ4nac-gVYC8UcpJdPQuAl8S2rMAFIzaAZOAuWjv96RnzjTs_uc94_igezBmOuuuO7xAJRwJUNYwSmTZeZ4-mUCdbKpKpf4XZeR4gWEcItgENtZ8Zc-g2yISWRkzzbdxD6JhtjmdMomJHKLSTlnSWePjrn_NOd0UhNduIjzIiALg4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a82a62e0d5.mp4?token=DArD41qI5-mmlyfC2GiMg_z0rXJu5Ib8YvWbiCTrzMaSqE3i6YZfR0Vo-pjmv4vqWB_Z9ukzAMUZ6teBfdBJRxJYDShiJi84jNZyxaWt5HzT71ZYCCOOQOrBbj6xQTAVLMUu0Et91TMIlvr7fBvtoyQjAa4svm_cxhx9qxEAWJ4nac-gVYC8UcpJdPQuAl8S2rMAFIzaAZOAuWjv96RnzjTs_uc94_igezBmOuuuO7xAJRwJUNYwSmTZeZ4-mUCdbKpKpf4XZeR4gWEcItgENtZ8Zc-g2yISWRkzzbdxD6JhtjmdMomJHKLSTlnSWePjrn_NOd0UhNduIjzIiALg4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
گل‌های‌دیدنی‌بازی جذاب و یکطرفه امشب بایرن مونیخ
🆚
بودو گلیمت؛ حتما ببینید از دست ندین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/persiana_Soccer/29500" target="_blank">📅 01:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29499">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIpRo1GGEbxOw0oKqgn4vpwSn833-sv_I-eRHe6RLLuro0i1umi62EhBQKabcqPdbP0brgAZRnjz7CTGy7Nzas7ONYX6rEOKWa4IbQ3L03i6W7rrC6KuHes9BgC_BTm3l92OL3xuzJMiExj52YIq27FUf3qPWcon0Ai_jscQdJclHaymvf9JfLUc7DsfV87bRDOQsTNWVJmjLCBjI8_ImLNt_ms3ouunPh0LH4reHRdYR3FO8uABtUZIPCZP_4NGuQaJW3Hzjsoq_keZ5PvONq05lxJwbu15dONOkR81gLSCnfzroFe1NiPvy0f6W8QJbn_mNAswbbLQnFMnvusXyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمد عمری دیدار باذوب‌آهن رو ازدست داد؛ با اعلام پزشکان باشگاه پرسپولیس؛ رباط داخلی محمد عمری ستاره25ساله‌سرخ‌ها دچار کشیدگی شده و به احتمال فراوان حدود 4 الی 6 هفته دور از میادینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/29499" target="_blank">📅 01:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29498">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivKrwtlbILpLX1AS8lX_BTiVEni2yuScQiaJ0RXxg8CyZV62LiPCeKnnFWv3LnqHFy927PyFLEKbrpoQU7xmBGj7mC_Dc3q6-PGLO9jGHGK1IqX5P-npLqNVVfJnshueFffYAZRtsqnJpFGBqCn-gPjAVl8dVBX7xlFOkIPd-RqHdG4x5-RtO_aQPWPTB4B_v7WcBYSUxA-iGkYuXfSYnPKSxspiTHsqOoAFFSOhtEcXZef4KkagM1vZmOUL8aDUmv1crEI92CtaEUil7yWWqMSTgFgftrsgs37o75_2-lpBHNkAXEjZa2Ut20EB9N55Xm2Lpt_jmGShoWnOoWO2zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌کامل‌دیدارهای‌هفته‌اول لیگ قهرمانان اروپا دریک‌نگاه؛ برگاتون‌بریزه دراین 18 مسابقه 69 گل به ثمر رسیده‌شد که یکی از یکی خوشکل تر و خفن تر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/29498" target="_blank">📅 01:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29497">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFaCNyQKmRpZQRmIjPGZ7yl4myMCf3PBqaAEhvztsAbAi0oYt4dZ0WazxqGmvE3CYVtp0mU3tJp4TAyvXO5jJNZ_7nTKfnwDnnl5IWFuMff42baE20pqbv2wZTGNQL0K6zDpJENgRFI_kY8rnqHg-HyXU-eYOq7z948lFNNfhXM16mr7ZyRW4w1rtJHgwbRKOi2MW1r5UYzKf5iSjfdH8LtBkQW8UtORFSQ7AsY2xscIfwiYOydHTIl8vMgEmBsYblEZTVV9aN-8-dzDE-aCl9k4OpFFSOuS9SrZ7XFhPDcqB8LhBjlVwSZK9vGR-FLuQa0Wi9dmKpn820aLr-ZXaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز
؛ مصاف یاران محمد قربانی با تیم ژوزه مورایس در هفته پنجم لیگ امارات
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/persiana_Soccer/29497" target="_blank">📅 01:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29496">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgDveMCsnu9oaZ-hqpPumqVjEVXmBoHvSXgip6Ro9LmV7fV6bGOJSKmNbNsm1mr0flTSB_SKgFTFaFClK9SRbGzjWsy5zJ2xAloL69AdTClC9zzHleKyQBmTAFaC8AwGNLmEZbl7iBWqqUqxnI6m3isZlHK464l3RuXFKNozgCwT8vpr4uHqnPyNdjsPf6Gv4q3wBOf0qUnKUFbQuBn3v7dsBOGsuGLPGu7DbWl5kp25c0grPT-rBhhUMI-40uEn_LOXoe0qThE_gr8X4UszKOnrRWK601mjSUv3L3h2Vyoh_ldUs_IWL9Y2d5J48nCy6C9W2leSFt_xpbHiI8qCwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از برد آبی‌ها با تک‌گل آسانی تابرد قاطعانه‌بایرن‌مونیخ و من‌یونایتد درگام نخست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/29496" target="_blank">📅 01:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29495">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال رسمی وی پاری | Wepari iran</strong></div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/29495" target="_blank">📅 01:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29494">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">📊
نتایج‌کامل‌دیدارهای‌هفته‌اول لیگ قهرمانان اروپا دریک‌نگاه؛ برگاتون‌بریزه دراین 18 مسابقه 69 گل به ثمر رسیده‌شد که یکی از یکی خوشکل تر و خفن تر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/persiana_Soccer/29494" target="_blank">📅 00:57 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29493">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇪🇺
نتیجه‌دیدارهای شب‌سوم هفته نخست لیگ قهرمانان اروپا و جدول رده بندی رقابت‌ها؛ آتش بازی باواریایی‌ ها و شیاطین سرخ مقابل رقبای هم نام و نشان خود و پیروزی کومو؛ اولیسه باز هم درخشید و داغ فلورنتینو پرز رو تازه کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/persiana_Soccer/29493" target="_blank">📅 00:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29492">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sM73zCvRta__xd_Y-HGxaZI64X8q-idC2aCuo-H9kAWM5EqXFlRFifgOBL1xONTfif57vmng_C1lOYlZa06GBJn131z-vzh0CaAmPsPM5elGmVJ0WoVSd7zjmGnNOzhsGWsk5qdsx6NVZq4LGw7zEXB0DF6XY0A5Gt79_OOoKyWoNSCZthRG87zzrc5tyL29wXl7iwj5UZPlC0LAK9eWLC0PD_xmOoxpT-OOiySA-9STUfA6nXvE5ZX4P8MRjGTQVcqZzDJF84dGGp7pf778iZjLzbYixnoQCccxSCH-8L-1HvDlXiN3dHy2gjdjOCV-JOit8ct6GB2c_BDpK9ho7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتیجه‌دیدارهای شب‌سوم هفته نخست لیگ قهرمانان اروپا و جدول رده بندی رقابت‌ها؛ آتش بازی باواریایی‌ ها و شیاطین سرخ مقابل رقبای هم نام و نشان خود و پیروزی کومو؛ اولیسه باز هم درخشید و داغ فلورنتینو پرز رو تازه کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/persiana_Soccer/29492" target="_blank">📅 00:38 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29490">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YrsGg0GD2xrr4xJGhdsSr4wqqm3xFz-rbJUSFzXQ8LCR8Neb59AItwwFMZ-HX6bZ5RGR-Hhz8WxP_prKF30KGWhtv3cAXJxW4B2WX1bgUZg9CD2NxnII9BmVUXhwdC7yETt2fP8Iom2hgrqdtke3p4Gdtn0tZrfLW07CrdI1r9b5XF6lqHy3scDd06ZVB7vP0e2vvlLODudroRZxcivG9O1V_tcf_Y8SmemUJvfGsd3M5SdBY-GHN4U5b9p2nI7AlzVb7k5HJ_Dt0VWIqvOP7dymDfLiUPWv_cclSNhfGDkYVSUkBnejEjc7ETSEEcKdt3hogzLeT22bi53dQ3US8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b2fW9Ih_7AF1fy2L9R6dn1i17R-fbY7RMrtvVilrJktwyedrTLzMOPU81PX85pHZxsK9kvtR2_ZdcDAcbKV7kOQolfSTaPsI2PJ-b5g_Me-y_jd-0BhiqeHE_pEklitsFLgwT7mJKITAM4yLA358BawikTUOmdL_iM87mVeQWWrbipbRpMq1pAC88_upkYy-6_vcdymy71ZNsgnB5SkxbgSwB-28g48cb7adrpg12Sn3ASEBVjeBAzT1qj6lgqFrcGyC0Sl5RAD4rMndjdhQlOEiM2d-7u8uInhtbRPvzcrF5qHpttwtsorSiGcaefGvBhXpBdgVjvqvKPDKqTxlUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز؛جدال آبی‌ها با پیکان و نبرد یاران کمپانی باپدیده‌نروژی‌فصل گذشته چمپیونزلیگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/29490" target="_blank">📅 00:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29489">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‼️
نادرمحمدی تو روسیه‌تبدیل‌به‌یک‌سوپراستار شده و هرکجا میبیننش دارن باهاس عکس میگیرند. همین روزاس رومانو بزنه: نادر جون به آرسنال هیر وی گو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/29489" target="_blank">📅 00:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29488">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtOAa5smF-du9zR1PjO0edAqx0VXnu2o6ZSEVQguP69BhNSYKs0KZcwfqtv5YAucPGkLEAthqY8PwFlq8rBhF6DwzbbwBTH3M0HZvd0LhekU0iL_xfredb8r6VCxf51dQe7qkTGevccxrQZMSPUtzs4Ejs1VeyshtTTDmjjSH-gjjd2uhjH2wyq5jbKp_wS57Kgm4HeIdCXJJvmwWaay1MyOJMiWs2vO__5yC__SzomMjwD2uU8B_zZdVfclSGej18m-GJKNctLimDS6tnvLgOb4Ow3U_qspCdZApSe16ANWIpwOdXXZHLZC_J2qSDwMe4V37s3KrW0DgNGdV_kzlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هواداران باشگاه فنرباغچه بعد از شکست این تیم مقابل تیم بشیکتاش خواستار برکناری اسماعیل کارتال از هدایت این باشگاه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/29488" target="_blank">📅 23:43 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29487">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLH4OQhePi2rb8Hm-3QkLdbXtZmwCgFX2UQbsgGaQRQ-xB6gFlM41qmaeom0CYMQbX7y_-7lrbte_whEKZTk1n1y1S3NnlV3vmJ8TvirlkFMEI_2YR0o9eUnOQd3AeHLdpYwagHta-iHDkxI5Ibe211JclhLMwmSuvz75TKYEdqFBTuguE84Jv8_EysFUo3rWR8-0YtRDMoPAV8hbXeTWR6N20u3T0DcnejGd21yLuQabAoif_sV1DsHLddNx-bJqy1GQr0Ix9X82gyFIQWsIsNGtGRdfuycrhWyg_git8dJNMoENwkSPZ31CsQ1567XNoEXS4eJOQkgOEc190cAUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تقابل جذاب دو فوق ستاره سابق تیم ملی برزیل رو؛ فلیپ کوتینیو از نیمار جونیور برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/29487" target="_blank">📅 23:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29486">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8AcZdAkWLWZ2h-WCUcW1L2jydAJhn4OOfvjGcDV1H3Y4Mfkg1ele7Pa0I5zX4MvsSZRiASAGVMBkdwFsm2vCv5WRAvMox_K6w7oN8MlP_coJybBeA1pRIRz5Y3VserGDQdzZk7azyCObUhs1Hl6_J8LH4vsI2zR666ORmrDV2uwdWJaNb8WTVedR1gveHkvoMJu-5tGM1QlVHuBGYGzeomOMbPpcgCYjcqMCEJNsQ7gmK9OshtBpEfdvFffRgDcOGSNymiaigqCyctgdD89vN9i0aE6AHcUdHlHz-MIwjreei3mn61mjPglgTOXuKmMUlTxYxA3SPtAO3lF5L7lQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مکالمه و پیامک هم گران شد! از فردا ۲۰ شهریور تعرفه بخش قابل‌توجهی از خدمات ارتباطی افزایش پیدا میکند؛ آنهم تا ۴۵ درصد! برای مثال سقف تعرفه هر دقیقه‌تماس تلفن ثابت با موبایل از ۶۲.۵ تومان به ۹۰.۶ تومان رسیده است. عالیه. همینو کم داشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/29486" target="_blank">📅 23:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29485">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BAigRvbLHCYSM2LGgwGr0dMhB4JRNsGROAWgEfYlwGMWp8QrrjI6Ly1sx1jUqknQUU3jfxN0Qq8YoQraNutVkPl3h2ZX_sGBaHvRht4pf51Cvh7zDMjNwI8JAt5spfYcN-BdjJAlxGSiGVs_zw8TaZRJq6GzoFS3YucvdMPjqQxiZeZvT5mM1kact7LIYkqOuz34BMLJW_c8GvEx10m2-V-WlGZ-f06PDgqSeWxYSyg6lMKMxkUG1SiYk_F_WPyh7gLzLkDEPvUolm5nJmg82DwFrKdZ2lrdb1Jz_SJ91HKVASuuVHZBPofUSRH9g1hBOfIeMN41oNimGPnzUZr4Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌ گفته رسانه‌های عربستانی؛ همسر مارتینلی ستاره‌الهلال که دندونپزشکه رایگان دندونای 50 بچه عربستانی که از فن‌های الهلال بوده رو درست کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/29485" target="_blank">📅 23:07 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29484">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbUxtz-t_Ull1B56eNvdVwsPAXm7ademhkEfamQ0AfODLZbDHbEyIj5sOxwCtf0gGb8XJdZWgQlXgTJe05MX92_Scc4E1iFqsJxSlx2YEDnwHKVFEN30CSallx7Wa-af7v3VfnJPNcaEQrWsElXJ7HQ151p81cVDyTtd3lQb6xR9SNJBQSLqLC7C6I3p3XjvI5zQrw0WCbHZFDkck3B9AQabfGaNVtB-22mMDdorBuxpWLIIsbNUElK0HBkOjy206Oimy7jeZT_hd0NPWFjDGPhutnLiyOOmwq4_3gcaCKu20ODqn8Q_5iKDcKO5-qdjTNku6CvHhql6hOL2sdj2Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🇳🇴
#تکمیلی؛ باشگاه منچسترسیتی انگلیس برای‌فروش ارلینگ‌هالند ستاره‌نروژی 26 ساله خود در تابستان سال‌آینده 200 میلیون یورو میخواهد. از بین دوباشگاه بارسلونا و رئال مادرید هرکدوم این مبلغ رو پرداخت کنند بند فسخ هالند فعال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/29484" target="_blank">📅 22:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29483">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRQJNrRdDemTp4mp96774UKTjU0XLLt6iY8y43ME_WOOKp6S4UadUKD9H56j08b9m8N02VWhmADLZijqka3U39ThAwkY9q61uYS6ziu3b4PH9CAz21J3dmJ6crHOHnMDBAM4MCXgp1V_cxH46C_jyhafSVeTz21rWpzplh1yerP-yXAwmcgpm3z8LWclSFjOwEZRtvdpfI4Tnw-y8eTiDH6dPZ3TC1l3pkJKrDKU8gv-dL-3bKq1Ni6G-U0h9TFMyh8jAIHHudqEduzd5VL-mDAxqSO8AuizBgoFSrgGgfUnzXDVTCRVaWavIo6Yj6DIw3Hf0NpvgdOkH6CWQZnTQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌ شنیده‌های‌ رسانه‌ پرشیانا؛ فرشید سمیعی مدیرعامل‌سابق آبی‌ها درتماس با علی تاجرنیا رئیس هیات‌مدیره‌تیم استقلال‌آمادگی خود رابرای بازگشت به استقلال و پذیرفتن سمت‌مدیرعاملی آبی‌ها اعلام‌ کرده و به تاجرنیا اعلام‌کرده درصورت‌بازگشت تموم مشکلات حقوقی آبی…</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/29483" target="_blank">📅 22:41 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29482">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/At9OEt7s-P0mImJFpuvFaJGwdJdrAUA2Nh1x2YuJg5v8apKTMQwC3SuKD0wmQ-XxUWQ6FjBmEPJztPkxrw_oQsg2_uNzrU4djjxHBqxgD8tNeZqnt2gA0_hbUQXz3yV_xDuXou_g1dqa73HRsAoVuBGiOA2ZPvtGhAt9aA4ElU_q1Rjw88qZ4xokJ5gd8IqNRFRD6YcjrC-JZ-h_rgeOP7qIKEGuZUx3NXgoxFmx9LDPXpnvYHlK_DIDmM-zfqxKHVW1Ucjkyuz9PPaH-K0x6a2Lr41itNXgPjnpAWzlk4OU_IyTsdNjnlmAlvOsF_FaP0JmMnbnenJY-ZtKt2b7-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ ابوالفضل رزاق پور از مدیریت باشگاه فولاد خواسته با انتقال‌اوبه‌باشگاه پرسپولیس در نقل و انتقالات نیم فصل موافقت کنند که گرشاسبی بابت رفتار حرفه‌ای رزاق پور در این پنجره به او قول داده در نیم فصل همکاری میکنه تا این انتقال انجام بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/29482" target="_blank">📅 22:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29481">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFMaoTJJ2XCbN_VWrBs25FRY9lPfVzEm-ATrQ8bFJs3OqIjOx4mNLXQR2PWUN9zYjlX2e8nun3CtvTERdoN36qLD58fuqrRpMfoNYj0_Q-rYqotoZJFj2JmPMFtaPyErDjDB5W6dXkKxzEom-BLEkf_RYY4FCRuy9Lvo20NcrtCeggevfhaWx8J9YKHvdDq7HoiqwF5u2t9QfD9r96NX9Iq1rVApsNcWRo2yae5PQ2REFwk2U884DD0PGEIaBD8LnTfGO8kklY_1z04-l82vp5gootij9BUJsxEdmdzmBS0nahkoSrqoGojNWFMUw6UmakC-zDsmqFdZQu9dpMAnLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇨🇴
با اعلام‌ رومانو؛ خامس‌ رودریگز فوق ستاره 34 ساله تیم ملی کلمبیا در آستانه عقد قرار دادی یک ساله به ارزش 650 هزار دلار با باشگاه آولینو در لیگ یک ایتالیا قرارگرفته است. شرایط‌جنگی کشور باعث شد که خامس از حضور در لیگ ایران پیشمون شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/29481" target="_blank">📅 21:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29480">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q08bj5VbovLU5G-OVJE8KLAFCWLGygzZtoZz7VGnybHfsnFzE5WVMgmemWDcsHFYJa_lqKa5EVzk24ZaCP9j13OEFk71s86yogNvSP2WLIhBMISeKso859z4Zhq6upoobAdGn3qWm_Sjkc2zYSSLimB4djgZc4RyDHx0ENr-fdFDBcfgu1y8ictuofz5ZzgDOcNCGG-kEMDAg1T8DmPfWWUscp71lYDWMkVX20rZj4XT9v11PhaOMt9PWKjuUnxlyrZI3Ft5BTubbUZzrq71uOREILckUznraeCGAdD3rHPIABUOyjNLwb1dD_SrW2ERR8TgiqS0YtuQnq_PUHol6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فکت؛ رافینیا دیاز با گلزنی مقابل فاینورد تبدیل به اولین بازیکن تاریخ بارسلونا شد که در پنج بازی اول فصل برای این تیم گلزنی میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/29480" target="_blank">📅 21:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29479">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYUpTFM8a2caIdz4IRcAkFZcNr0oDefb471BdME6o4pU1x2dNH4-NDdvKTdTRWYBZdEzjtAGVnRkTlJHtkGIh9MYXVt27uvQ-dx8MP6qEiaauHr5nJh3a6PdrMdeeF_MyTcj1pJnnJlnHQ38FcSomJyvn5lZ2RWA23F9T1iTqBr8qqI_TAa3AwWozeyzGG09u2PnTTMJy9YH1BQzCiFIq4WiKAWWP6GZZuwOFmN7kEe74l5LwP4lI6HDVoOC81ELxOP1Fv5ga41ZBZ75SWU2H-9vAffP396VUuk1aDvfH6ROkC_DRmo7fEDL-YcCEWkkvQkeZ_rRY0YvYrXU-ffKhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
🔴
#تکمیلی؛ درحالیکه باشگاه پرسپولیس و کادر فنی اش به شدت به لغو بازی با خیبر معترضه و اصرار به برگزاری‌دیدار برابرخیبر در روزیکشنبه داره تیم خرم‌ آبادی تمرینات خود را پنج روز تعطیل کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/29479" target="_blank">📅 21:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29478">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dw-w7dXQ3oKqJ_APuRX2bAhifm_1gXIAEHHmc9mIL4unFbanqywgf7CUYHv2gmXff2T8FEUeLHadjGWzmiucm_tYSlEmj8UAsKcd2fCk9avn89-jtu-pC6afnHjPsvq5LzehQn8j3POWtqh1ssxncndFNhHtS5Cd68tb2cGLB12I04iFNjYPj1Q7Lootb2APMKcMuDHb9bMZTMap_NX4NACzmyky0a6lCw41SYV_EdO27HmuOrjAR3U0dIH3iqD9y8-scfKfIt5MFi3yjh4aNy7LoMYTE0agrenyQ8A6gSRVYw2pwqVTCUZGs1ocVcQDrPVj-UL4ex8y7zco9XTYHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇹🇷
باشگاه رئال مادرید برای تمدید قرارداد آردا گولر ستاره ترکیه‌ای‌خود تاسال2032 به توافق کامل رسیدند و فوق ستاره به زودی قرار دادش رو تمدید میکنه. پرز دستمزد آردا رو حسابی بالا برده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/29478" target="_blank">📅 21:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29477">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alCsuupyHk7DyfIfrlfMNHH2Uhs8ZnFci1-81_zxOF1q2-D02E2Zs0pvfi9UEwKWGZjHqPzjawKGMTu5yVREqb5rHiwcPROytKsE6f7X_v-8makyyYVHsUwGiUt9mt1ALUR1Z_x4MamB1HwpGVgk-qBOEPXOJhDBd36UTPVIk-86A9yWirRdYwV_a4K4x7pmCESCTql_mbQ-HOlkdcqn8tRy8Iud7NzN_44ZaV4QN1pud5AfLWxhlWTi4qrBTpGOWiBkqZk-VP1KPLkIdCwrvoVKXRrKGAX8eKUgTsQNJNoKNQUVjKEWQD2lL-JgQfwL81QCUR7yb0CWDjMz8DfbBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا
🇩🇪
بایرن مونیخ
🆚
بودو/گلیمت
🇳🇴
⏰
ساعت ۲۲:۳۰
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/29477" target="_blank">📅 21:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29476">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bu1O4uJfM7YEmy-UAPtShIk1Z0nS2FPiE-w-ecWD7_sS7NhveCtt5DDEXwPvgBNe7Ha-M5XjU1XF8LUaG_43eXM-rAjPZP_90B4XghU4K-kKTCz403LFyc7Hs951Q2MXS82T7oGZtVW8lLBwq8hsy7AeAc8gjRonBQXz3lDCDNvpiLCXdQIxaiM3vUO-Zam_y9t7MnAYhXyOhYR-VacS7oZUfEIKdyFDQhUDtUn2axodgOTm5llAYWWNhzr-sQDlQEq8hmknOVkNzvoyP9Q178WSMcN_7S0J_38Jm1I-bQV8ewb3vgQ0ATOroret0plfAbL7GPXnPKpZMjCPCcQsHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته هفتم لیگ برتر؛ کار بزرگ خوزستانی‌ها با بردن تیم جوادنکونام؛ تراکتور بالاخره در هفته هفتم تسلیم شد؛ نخستین شکست‌پرشورها در فصل جدید.
🔵
استقلال خوزستان
1️⃣
-
0️⃣
تراکتور تبریز
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/29476" target="_blank">📅 21:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29475">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ya43awk1tJb12HXYy-01cngsM4WI33ZeVrLu5bSAfRnztw0uCqCKjctTdF63ZkApPSNHYBvs1DOmUFTOWJA-1XtHOZFPJbJWgKi4LUBev_MAV6Msn9Il3Bj-5hl8X-hnWPpvHt8iVGXCZ2sTFYWVmRyOApCXWZRBywbxB19-bi5t9ipJdTds_P2Se_2zAMTvNUtyJbEYok0cckFLLaVQcG1hbvgLZYRZ_sCMtxjOvK_B5S5c_Gpba4T2z2T7-RUsAJFaq9pglTlerNGcxqvkP7pq3jUhry5qV3t9XVSFDwSQYKIen0V5JvYqkN2WbzA8bHowy1VtOWPD5w1Yn8Bd7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی‌تاجرنیا رئیس هیات‌مدیره استقلال: بعد از بازی امشب دوستانه اختلافات رو حل خواهیم کرد. صالح حردانی بازیکن استقلاله اما باید قوانین داخل تیم رو رعایت کنه. او به تمرینات بازخواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/29475" target="_blank">📅 21:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29474">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6cd348634.mp4?token=Rsracwb3ectnY9cBoLysYe0LnTF-cRguq7_f2PVXO3IUtdyxMxWwT0kwv42SbauZnS04xtqtw9i0lCcEBEJOvs08VjyxKObY-jhtcSs64KbmijSCRfhprUekawoqP6Bu3nsLFyrjOA49SGDdfoadqtreP2GADn1SSK8vmALXbN-eGLnIq14zC93LNAPiMjEng7HdZpd2N8sX_7jDynljQiHUzYhn9TZeYPEb9oImLRgekH6aESfmZ1sdFq9DrcCaxffj2H7lPxVJxsK9zcGR8mbzoVJkbAH1BprMdFZR2usX_o-mRLI7v1lnh_6VkCT_-FZl4wA2vrkDsus5ADZn8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6cd348634.mp4?token=Rsracwb3ectnY9cBoLysYe0LnTF-cRguq7_f2PVXO3IUtdyxMxWwT0kwv42SbauZnS04xtqtw9i0lCcEBEJOvs08VjyxKObY-jhtcSs64KbmijSCRfhprUekawoqP6Bu3nsLFyrjOA49SGDdfoadqtreP2GADn1SSK8vmALXbN-eGLnIq14zC93LNAPiMjEng7HdZpd2N8sX_7jDynljQiHUzYhn9TZeYPEb9oImLRgekH6aESfmZ1sdFq9DrcCaxffj2H7lPxVJxsK9zcGR8mbzoVJkbAH1BprMdFZR2usX_o-mRLI7v1lnh_6VkCT_-FZl4wA2vrkDsus5ADZn8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
مهدی طارمی در دومین‌بازی‌خود برای الوصل 70 دقیقه فیکس بود و درحالی که تیمش 5 بر 2 تیم خورفکان روشکست داد نه گلی زد نه پاس گلی داد و نمره متوسط 6.7 از فوتموب گرفت. هفته پیش هم دربازی برابر شباب الاهلی نمره 5.9 گرفته بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/29474" target="_blank">📅 21:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29473">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kuc6kJLety1KXiXxNa7ea4ZQpI41feil3IVjLoHV5Jyb0Nlqfq_vdvpNQLYEAZS5fhT-73T4sCoNjvjDI7O_enZ1LbjHaMcb6OUHuE6pL5gN3eRnSbm0LBLQhxnk9yIdJ4AJQPBmKnay2VhJyPg7Cou_zdqGtG6xRk4Hb0Tz3gAXa67HVR1FpHM1qzTB6M_RQjw39bB-34ttI4hboVzGBbo4F6wKJc0zf0Tk9qjsa3SycBUbC2ETo3mWFtSyyVRyfL3UTs-LkDEZBbcpnBbI5H8Fljxys6BTnv31TOoRF-I5kcQBDkBVYAJNn18iZCCmvw0hUhp0_etfVsbS-P8d-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دو گل آفساید تراکتور در بازی امشب با استقلال خوزستان که طبق گفته کارشناسان گل اول به اشتباه مردود اعلام شد و در شرایط سالم گل شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/29473" target="_blank">📅 21:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29472">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1LjXk6mbL42de3QDUY2jcQpIP8Q07QkisbNQ7nN00cdhU1zGA0Y8SAheKpmBo_2PQ949Br97c9lK7ftQVc8yeb0RsjgdcF_124hhhNq_uCnWrcUZsE3ST25mOktEYTLerDiU4EcGwoRG3CsfRA5vr5ApHEUGSqoEUXKzle4k7hbqC7o2XSeeC8aR8dvDluT1JopUEFC5ixLaNpm3SmjhfevGkE7J0Rvi4EZLxYEkbTavPDNhf-LgDPKqMWqKb3Se-sv5T3Q7q-JgtkVD76ZCe1HTfXJDXtn-DV_ywvCsCVHtRpbG3FYMaSzuRShy2bqSUkYiJCjCxyh9FEbG5v8Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم لیگ برتر؛ پیروزی سخت و نفس گیر آبی‌ها در قلعه حسن با گلزنی ستاره آلبانیایی؛ آسانی سه‌امتیاز بازی‌خانگی‌روبرای سهراب به ارمغان آورد.
🔵
استقلال
1️⃣
-
0️⃣
پیکان تهران
🟢
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/29472" target="_blank">📅 20:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29471">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7Ub2vGUWHAUo8rvibK2NXa5S_F7pu4EDYdpkuaqzBtXiqcsEWmExvQFSTbebf01gHq3eeNaNBYqJnzeNu68_HjDt_qzgdnXnvXJefg5Y1MXIT8ZPQPHsM-hiNO8qLdh1E4kLQgk1HUDNwNhxW_aFSbOK0g-RFr0qDZNGfGrwTE-7jMWoeLA3u-1GoDL0bzTCVH96uOgAym28bCDfiRXEHUM7KTev0vNYGv8ZwnAS2ieoXSP6HZIwatNzz-PvwBgHuBVcNVlAt_vJ6GEo6Ks7C3vJGopIaPKziNeo82vZApJ05-W-YE-Zs-iJF6nWe-HwWduz1wcMEkDWFwGPYJLDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
سومین گل وینگر خارجی آبی‌ها؛ گل اول استقلال به پیکان توسط آسانی از روی نقطه پنالتی دقیقه 76
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/29471" target="_blank">📅 20:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29470">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/399d4e43bd.mp4?token=PWASY6yjGT8X2aySqAQLsNTZo7lvsuBJJl8FitzTnmJMBIaoEmUwFNsmWc6YgAIOcNR5F0dBQW7CcbbKdPAKH0XCtM1gFmB4Oc64eTk7Eq17o1qwEDqijTnWPkpur8HUWkqPGZ_Qg6obGie44Mc3XQVh-sd-jIFkpwDoJx2FMrZ8FR7DFkj33Vu_ZOuELR2DHryQoDu4xYkatRjaH48IFreqrdz0MVJjQRaJJN3KfKYvGuJgFNTjInP-HxL3bz2WMs56trZNDrw8JFhX090oKK5G-A9CtFZGms4F6FaS6dO9cRSdWDsRdG-etkVEnpJCMXGoqjyxbACIY46hLYW4XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/399d4e43bd.mp4?token=PWASY6yjGT8X2aySqAQLsNTZo7lvsuBJJl8FitzTnmJMBIaoEmUwFNsmWc6YgAIOcNR5F0dBQW7CcbbKdPAKH0XCtM1gFmB4Oc64eTk7Eq17o1qwEDqijTnWPkpur8HUWkqPGZ_Qg6obGie44Mc3XQVh-sd-jIFkpwDoJx2FMrZ8FR7DFkj33Vu_ZOuELR2DHryQoDu4xYkatRjaH48IFreqrdz0MVJjQRaJJN3KfKYvGuJgFNTjInP-HxL3bz2WMs56trZNDrw8JFhX090oKK5G-A9CtFZGms4F6FaS6dO9cRSdWDsRdG-etkVEnpJCMXGoqjyxbACIY46hLYW4XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دروازه بیرانوند بالاخره باز شد؛ گل اول استقلال خوزستان به تراکتور توسط رستمی در دقیقه 54
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/29470" target="_blank">📅 20:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29469">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6898eb4b.mp4?token=dla1beoX0-sK-rVjwqagANuf85Pznv076FB9JJ6Zh9p9e0ZofAk0lZwUZyuh2qQNzgxtaGf2Kg37Q1QXm8d-uLvPgN0eUUsjDnVI_4lrulWPU7sHcppHGTzA22eVUmKPnfvhb-WE0p1vww7RBbc5nr3FNdcOgZOFYfW5lpMJt68IDjgmdG_tj26IkE8D4kSehIrOXIBpmD5huvVTVN8MWJj-gUUQvuIsl7IvGHMHbPZfe2ljsvAu_pxoqUgG2v1hUy574R0Oz0wk9Ly2nPzz94KOdTbLbehnaAyvChe79St8oiPpt9e7Mz_JAg7-q9wmdj3EbTXbyE2kguRrQX0wWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6898eb4b.mp4?token=dla1beoX0-sK-rVjwqagANuf85Pznv076FB9JJ6Zh9p9e0ZofAk0lZwUZyuh2qQNzgxtaGf2Kg37Q1QXm8d-uLvPgN0eUUsjDnVI_4lrulWPU7sHcppHGTzA22eVUmKPnfvhb-WE0p1vww7RBbc5nr3FNdcOgZOFYfW5lpMJt68IDjgmdG_tj26IkE8D4kSehIrOXIBpmD5huvVTVN8MWJj-gUUQvuIsl7IvGHMHbPZfe2ljsvAu_pxoqUgG2v1hUy574R0Oz0wk9Ly2nPzz94KOdTbLbehnaAyvChe79St8oiPpt9e7Mz_JAg7-q9wmdj3EbTXbyE2kguRrQX0wWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
شماتیک ترکیب استقلال برای دیدار مقابل پیکان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/29469" target="_blank">📅 20:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29468">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56d96077f7.mp4?token=cQKz5xMye2Cio6euvzq6_qmOKKzuizVIXc8JE7QGTkcQwGJ-UEdE8SdFTiOOOv5VFamydgCrpdJICRSvwdAocD04EG2ta8iRqrk_JMcqRf7fbsSR0M47O6W_6gCuzmRgGtmpI6hvbrf5sWK754LUJb19tWC_Dxyf8YRybA-ys4J38y-YQ1TIfFh-UEka9psrbVDL-YBMpc-sY3jNIo59NelQrF0EVRMvS99JEX3kH6iugS5l7-zZQng7Q7P-l0lIHoPk9nGUtnPQTZ-K-ASVYvpltQxZX_6FE3fg38Uc_Gl9s3V2sKeUNB2VNGlxag7fxnMEvUwiHdKJ5p9VPMlx3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56d96077f7.mp4?token=cQKz5xMye2Cio6euvzq6_qmOKKzuizVIXc8JE7QGTkcQwGJ-UEdE8SdFTiOOOv5VFamydgCrpdJICRSvwdAocD04EG2ta8iRqrk_JMcqRf7fbsSR0M47O6W_6gCuzmRgGtmpI6hvbrf5sWK754LUJb19tWC_Dxyf8YRybA-ys4J38y-YQ1TIfFh-UEka9psrbVDL-YBMpc-sY3jNIo59NelQrF0EVRMvS99JEX3kH6iugS5l7-zZQng7Q7P-l0lIHoPk9nGUtnPQTZ-K-ASVYvpltQxZX_6FE3fg38Uc_Gl9s3V2sKeUNB2VNGlxag7fxnMEvUwiHdKJ5p9VPMlx3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
هفته‌هفتم لیگ‌برتر؛ شماتیک ترکیب تراکتور برای دیدارحساس‌امشب برابر اس. خوزستان؛ ساعت 19:00؛ تا قبل بازی امشب کسی نتونسته به تراکتور جواد نکونام گل بزنه ببینیم امشب چی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/29468" target="_blank">📅 20:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29466">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h7pqlaHnVZB7HBZnq3Yc27n_evPzM65FXzYRrIx6ZoOfAtMAA14JzNQrrx9wte1T8JnCAIcDX3vVtHQxTLJwkWN5bHs5HSEkg3czRDPncTBYuvDe9ylUZr4VtJzRYk65TXMoEz8TlZOgz7Zf66heZB1T8K2rd7urz3JNEDLBvsf-2yQ58enN8dnnDFknJvnnfIDdAUY9O1bzdW7HP7-P-xyFso9CnrvRk0OsaKjWG-BpTbBbyK7WdizzNWRbRHXkysfs1NFeinGJehXmtPdhiTQ9PAOV9i9vwEJ7a6y0toiNgxuIlG--sNE9o4zkOCu1BgH81r1Gpc2NMNUqfv4iPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IjwX6keEv9kFxT6RsCosYEPU8TOl5YwGGEzHrDIJ_WlFCJVny622YUiDlJkCm5vUQgZy8E5uDLtAowI0KKKTNMF5lVe-cGl3lrkSqbtYPRaBVSNdHQegCm26ym8b1bxN3sUVeEFt1Q7FU95xnWGs1aCLkjx8vJmj0c0vJ5jDXf5W6ZfQKPdck4MOgJa8tLuKJJi8ES3EYRaTTr8Vv1pnQkMNl_z9GIk0PrOautSI170VpU1sS2hsXazYk9WnB74x27cg-f5oSqEgONqk1R8ONubxCierUAKuM9TY7EoECKX5AD68ozA1_rIepPBJf1jr8O2zwGkmluxkUHwRNtoSRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇫🇷
دوس‌دختراسپانیایی کیلیان‌امباپه ستاره رئال مادرید در فیلم جدیدش بنام "Drawn Together"
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/29466" target="_blank">📅 20:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29465">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdvMzebALwKQGZ-AtzmRDtQkStJ1yIwOrjrJgUaWM2UF-YtS9izbZtMXtJKUu4VrvJMERMT9z2TVBaPKQu6dhDApbswmlVumIJupxYwbSG9tAKUlsX9gB739VPy_tZZ3kkBlgsYZTkkNJIBWr2jQ7n1x4YoXV0_kXP0bGYM51Lg3GaZOwUfvLTmh2ASt55YRshBUOkgfUX6VxkaWlC5T7DjqY1wLqHiODFZFkhHFXMqU80G9W6_FO7RpG4BDRStsAJVZZaSRM4Yml13C0-mgg1sgT6kUDOg3F_aYdPugtU3zgxGdVekY2pI_R9rRqAhwmOE_Oy9anWFacLBT2Bubpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد فوق ستاره‌ های فوتبال جهان که اصلی ترین نامزدهای‌کسب‌جایزه‌ارزشمند توپ طلا 2026. امشب‌بایرن‌مونیخ بازی داره ببینیم کین چه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/29465" target="_blank">📅 19:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29464">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgqQhzu4jgcGS9mMRgP0V5WFz1Ac02f8otLjjeG3Nco8ZAY9YcKFHwwAyzn-s1BwVMWYfowF1tZQhOByfsYbNMReuH-7DbC2k8f2AFah-nhmeZTIxJTsD-jr234CzSWCAbeZD6vsQ_cEmLhmLgleWdHgLs73BqZIm7z8ex1Iq8rV1ehTbKTcIVP96iMKOBJ_kWQphCOUG_TVqThoP-vo02mmYeUQ3-KiNJB4_IA6gb6ydV1ivE4whxyujQsris0e3nX_l-oZPBJ1uPneAkESFneIy5V3vcjJTMSMXLtjcm-9EtJG08OmQZQGVe7Nix3fNfvtlsG4Xi3r5Mr7LcdfMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویو توییت جنجالی وینیسیوس جونیور در سال 2024 به 490 میلیون رسید؛ وینی بعد از اینکه اون سال توپ طلا رو به رودری دادند یه‌توییت‌زد و گفت برای به دست توپ طلا 10 برابر اون سال که با رئال مادرید قهرمان لیگ قهرمانان اروپا شد تلاش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/29464" target="_blank">📅 19:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29463">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uk3aTE8VjVvcf4HqV_4RVYRxn7hm7WSQs4hnnOXJKhWwyR_Z2dKTWIQXJUqTod0OpPOFbcGVTmUDCrUzlut1dIZrg3J5TMI7fqjntwfj-Lvllv5x3fT2QBc0D2_NXFn3bfn9ZkkDtXsePbql7RWo3LnI0O1_zLNPmAa3rlLhHEqgE8pNn6Xc685MjngKiFNMOXKOikaRc27hhGmBFs63baeK8Vi589Lu75Lv9GHksr5nahEBj2jumGIaEAkpiVEO2cnWiWpuDfIGuyjIsR4EfBVSFb2gR5CczzXp8XkkRKZ1F8qD_1lS9DHhdGQYavIshcwVNHm7TqODPGjqxtHFUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه بازی‌های تیم ملی فوتبال ساحلی ایران در جام‌ملت‌های‌آسیا؛ مسابقات از 28 آبان شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/29463" target="_blank">📅 19:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29462">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cf5ffd776.mp4?token=ZhRz7BOOUtDlKwmVchmBFc1qsdGkH4UVydxSocPp_E_FtsgkBLlbQfZ9jb3pMl-ipcjl-yVNuW7QhPyp0cNf7_lGtJEAaXx27XV2ziHHXGFyDgoI0sWKLlSXYEcA2bwXnPH0LKu9flbG43cZEmQ8--kTyxKK5kYCdjGYOB-A3YKKiRRKqyYNeC0Qiee3YOQNrojXCt7KjdiL8PgH2SzJjHFDj9XPS85vF_mvBmtG7mLC3RNNlD3vTtDU1D2J3Ri-Ad1uEzhhuLjjpa5wK1-a6-HdLBqCerAnj5K3HG3aQbEc9x66dM7NJ44rzFlO--9JWca8tjG-uECgY3xfgG-c-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cf5ffd776.mp4?token=ZhRz7BOOUtDlKwmVchmBFc1qsdGkH4UVydxSocPp_E_FtsgkBLlbQfZ9jb3pMl-ipcjl-yVNuW7QhPyp0cNf7_lGtJEAaXx27XV2ziHHXGFyDgoI0sWKLlSXYEcA2bwXnPH0LKu9flbG43cZEmQ8--kTyxKK5kYCdjGYOB-A3YKKiRRKqyYNeC0Qiee3YOQNrojXCt7KjdiL8PgH2SzJjHFDj9XPS85vF_mvBmtG7mLC3RNNlD3vTtDU1D2J3Ri-Ad1uEzhhuLjjpa5wK1-a6-HdLBqCerAnj5K3HG3aQbEc9x66dM7NJ44rzFlO--9JWca8tjG-uECgY3xfgG-c-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟠
پاس تونی کروسی هافبک مس به امیر روستایی که این بازیکن قدر این پاس برگ ریزون رو ندونست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/29462" target="_blank">📅 19:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29461">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cb94cff9a.mp4?token=DE_hIP2VtMGUIkkrzgsPvC4g47bhwTJes5RveLLJ8mlEtD6YkabMFsmboCYdH4VqIgRZmlRbtI9D0TFMVlGIXuD7mVjYxS2cI6_B2n0D2A0m3IylqbWA5uGY3JjtiM29dP3J9WuP195rRF4Uqpv-4kc-kgp-Te1x-EHJex7zGDWeM4ibQHxgDpQpO1Wn39WlZRh2MB802jbVSWIyGgINrTXYGDV4XsAbur4BauU2drn17fDsyMlBNJV9jzlNIjeWUIgdb2z19aY1WPdhipOjjqkmhBJt56rU4UK0KAlzsd6rC6EfPlt-IfnpqEYkqCcmyNRmiJ5hFj-p8KSOyqxkUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cb94cff9a.mp4?token=DE_hIP2VtMGUIkkrzgsPvC4g47bhwTJes5RveLLJ8mlEtD6YkabMFsmboCYdH4VqIgRZmlRbtI9D0TFMVlGIXuD7mVjYxS2cI6_B2n0D2A0m3IylqbWA5uGY3JjtiM29dP3J9WuP195rRF4Uqpv-4kc-kgp-Te1x-EHJex7zGDWeM4ibQHxgDpQpO1Wn39WlZRh2MB802jbVSWIyGgINrTXYGDV4XsAbur4BauU2drn17fDsyMlBNJV9jzlNIjeWUIgdb2z19aY1WPdhipOjjqkmhBJt56rU4UK0KAlzsd6rC6EfPlt-IfnpqEYkqCcmyNRmiJ5hFj-p8KSOyqxkUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عصر پاییزی چهارشنبه از مدرسه برمی‌گردی و تلویزیون رو باز می‌کنی و این شاهکار رو می‌شنوی. یادش بخیر واقعا اون روزها همه چی بهتر بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/29461" target="_blank">📅 19:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29460">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba1961c125.mp4?token=Wv41oS7biCWKXVnwpBfS2tVEOZjHCFCUzIStzRiczseA9K-w9gpLzR2VG5LBnIaaDalUjJX70urQrOKZERJbaosqsH0sZUl49xLxOheVkJinSDAWQanSbgrej2uZqjq4npHp13bEU0Zz9JHwbEbECjWH7LypJJyGyIQz47JN3GP3xCgGfuQ9Y8WIM592T60Gu47Bs5uVccVb81uq8-OXZLgLobiFKZTMkxPi3pOvm21YPnlAw5oTrAhdc6VuwDJXmvP8tA6-z1TCfVuHDfsoxNRJKA_svhRGApNol0dOp31NN4rRPMPl0UYhwDrwPg_OWzAGhkjU8LXpch02KMPInA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba1961c125.mp4?token=Wv41oS7biCWKXVnwpBfS2tVEOZjHCFCUzIStzRiczseA9K-w9gpLzR2VG5LBnIaaDalUjJX70urQrOKZERJbaosqsH0sZUl49xLxOheVkJinSDAWQanSbgrej2uZqjq4npHp13bEU0Zz9JHwbEbECjWH7LypJJyGyIQz47JN3GP3xCgGfuQ9Y8WIM592T60Gu47Bs5uVccVb81uq8-OXZLgLobiFKZTMkxPi3pOvm21YPnlAw5oTrAhdc6VuwDJXmvP8tA6-z1TCfVuHDfsoxNRJKA_svhRGApNol0dOp31NN4rRPMPl0UYhwDrwPg_OWzAGhkjU8LXpch02KMPInA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌ پرشیانا؛ باتاییدیه کادرفنی؛ سردار آزمون مهاجم 31 ساله شباب الاهلی برای جام ملت‌های آسیا 2027 که قراره در دیماه برگزاربشه بار دیگر به جمع شاگردان امیر قلعه نویی دعوت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/29460" target="_blank">📅 18:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29459">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a4f9a05ab.mp4?token=Y9RFJU97XDfS5IF75ym474naB2delqGpP-wd-KsFHn0OVUGguJ8G9L1sNrQ2FsBRbe6nQnZFhegy0kGERXgTIXF37cHZ2PwGCqOywZiiuISqh6akyS-XqIlS3d0H6ONTngObc_Dl_BYDR8A6Q6g1LVAwNAwp--JJqV13oEwdMYjYd5pPHS6sSE9oVXf3jGJVbu6GtU9XdHLMLGmszna8vQ8nhkhBjEoJ-H-ODo9DZMjfGfmKUyUi6fTL1Icd0OPNrVMEKLg5dRkGzY-sIxXM3YRladsctlTNnp-y333GYBUP6DnT83kXEFH8SzCqJ1eM6E_OzVuVvHSKjk0y0uvUhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a4f9a05ab.mp4?token=Y9RFJU97XDfS5IF75ym474naB2delqGpP-wd-KsFHn0OVUGguJ8G9L1sNrQ2FsBRbe6nQnZFhegy0kGERXgTIXF37cHZ2PwGCqOywZiiuISqh6akyS-XqIlS3d0H6ONTngObc_Dl_BYDR8A6Q6g1LVAwNAwp--JJqV13oEwdMYjYd5pPHS6sSE9oVXf3jGJVbu6GtU9XdHLMLGmszna8vQ8nhkhBjEoJ-H-ODo9DZMjfGfmKUyUi6fTL1Icd0OPNrVMEKLg5dRkGzY-sIxXM3YRladsctlTNnp-y333GYBUP6DnT83kXEFH8SzCqJ1eM6E_OzVuVvHSKjk0y0uvUhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا از نزدیکان مهدی‌قایدی؛باشگاه‌النصر در روزهای گذشته قصد داشته که قرار داد این بازیکن رو تا سال 2029 تمدید کنه که قایدی از طریق مدیر برنامه های ایرانی خود به این درخواست‌پاسخ منفی داده است. قرارداد فعلی قایدی با النصر…</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/29459" target="_blank">📅 18:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29458">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/071cf92014.mp4?token=a4Ont0u32AFyQ62bHYFgY5HZFkfG-H4xWp15kyL4W4F9nrVqOEsuqW73HVMK_QleWMt312Y2QCYg7I1KEFUkNanZ-2Zmvo-wJWAUSJvUmkzgOcfUZ77E3SSRlt72wmoMsvcYLOqcC7jhm5FwUPDEdU2p9zHh2zcxIxYsU8imFxnAk0YIFiG95DPFZ0lR87OS_e67TADSzhnA7olVQ216fxpeNH65ifQIhmUBLwcUM0maslt1dbxzYkEoObc64cHLVvGQ0h3Vg5hoTMSGGG82VGYu_u75felrqvYM6DC1eHKlS-zX7e0-Ie8ow1myxonSQRN-OeTjnntVfS3FFnQyim_HRDvOwLK91CB96KFvgzFHycQGl_5qqFiUox540zhf_RgEzkNX2JDno4LAvAi_aCpREcDlPzzPJzvFybldXlWeo4d4WERcuBYWe6mO1N03FB8Nbqj1Nx0A-6wa0QdyomwyWFDOi_SSAjvyEwFQvSK-WDzhyaaHzP35UIvjGKXLvsFYbXPJ7lhcHGHzwkRuWvXKLOaixQbt8S5kMmkQ_nZhZk6dzh9i5c7crar-OA3yhPwckpZaL4cdedIe5TOF2ZK7KSEwcPr0cStSJ_vBU_RecoFWuVDnSCS5Sj8Uxa0JRvd4Y0lt-5xwKvIWAzpfOYNF-uAVrEcJtK1POvElSu8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/071cf92014.mp4?token=a4Ont0u32AFyQ62bHYFgY5HZFkfG-H4xWp15kyL4W4F9nrVqOEsuqW73HVMK_QleWMt312Y2QCYg7I1KEFUkNanZ-2Zmvo-wJWAUSJvUmkzgOcfUZ77E3SSRlt72wmoMsvcYLOqcC7jhm5FwUPDEdU2p9zHh2zcxIxYsU8imFxnAk0YIFiG95DPFZ0lR87OS_e67TADSzhnA7olVQ216fxpeNH65ifQIhmUBLwcUM0maslt1dbxzYkEoObc64cHLVvGQ0h3Vg5hoTMSGGG82VGYu_u75felrqvYM6DC1eHKlS-zX7e0-Ie8ow1myxonSQRN-OeTjnntVfS3FFnQyim_HRDvOwLK91CB96KFvgzFHycQGl_5qqFiUox540zhf_RgEzkNX2JDno4LAvAi_aCpREcDlPzzPJzvFybldXlWeo4d4WERcuBYWe6mO1N03FB8Nbqj1Nx0A-6wa0QdyomwyWFDOi_SSAjvyEwFQvSK-WDzhyaaHzP35UIvjGKXLvsFYbXPJ7lhcHGHzwkRuWvXKLOaixQbt8S5kMmkQ_nZhZk6dzh9i5c7crar-OA3yhPwckpZaL4cdedIe5TOF2ZK7KSEwcPr0cStSJ_vBU_RecoFWuVDnSCS5Sj8Uxa0JRvd4Y0lt-5xwKvIWAzpfOYNF-uAVrEcJtK1POvElSu8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
👤
ویدیویی‌از آنالیز عملکرد فوق العاده علی علیپور در فصل جدید رقابت‌ها زیر نظر مهدی تارتار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/29458" target="_blank">📅 18:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29457">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dD9hw-HKSqb9QV-rTNP2eq9GQ6oDSe40vga8NzKmAXMhxa-4eq7899QSDEpBPK9H374Jne_gBqGWvcWKBaGl4BsmgqxzAQec6TBlbsN7E4iSgWahXPKBkEV8dgTAZbFRdPu0FXzb7C9bV-b_eW__1PT1Js-FhvLDMR3Hf81WADm0TLHJKthUChvv23o4ohq95ajAlCeIO9-596ecibD3ascS2Q6KD0J8e1qbjaQzeZkqVgmDiwjwk3C7UadprIEaf8Eae9e2eIdBq37PVXSSvXQKngLa-7fnoZAM43eN_Z61UqjXH9IxFcf1LRL8uRWS_9_Zladyz6934VB-GM8FWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
هفته هفتم لیگ برتر؛ ترکیب استقلال برای دیدار امشب‌مقابل پیکان؛ ساعت 19:00 شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/29457" target="_blank">📅 18:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29456">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzyVwQfS15IzKMbDxK19FEamGDggbnOlM2b74NkdCQ7DaSq54q3CvjSO01bBugx0eziJnqMCtAG_w02aNlw4lNLbfLskkk54f-n6kaeznHicNhedHNKCLBl7Wxu01HLZ84z5gdrT1CTd1aOrEeeZjmT_Lgx8eQ1LPjJKyHSGDise_hBNaT__W0-qqgOLDyYwOI_LRuSx90iKYAQNqUuFwAAC2FZYWAST3V7y0MqL6v70H5ZQgiuppHiEc2UJt8v3v7JmGGt8L3yfV-dF_o3BAigHn0ICCAdWZMuGYG1rB4_4w8iZyOl1abFZ-dzcUv4075Qx-SSPXsm1uaL-gJWMKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
هفته هفتم لیگ برتر؛ ترکیب استقلال برای دیدار امشب‌مقابل پیکان؛ ساعت 19:00 شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/29456" target="_blank">📅 18:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29455">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f74RI1WL6YdX6PNLaVIHSeraa2-Uc3SMWlwBPI6WGpgVJZP0MCZAA5VThIuih3TAzbVAkD19fyuYjJ_CbJtEiqiVuxMuEnGOfKgqULMvlZXMY7MwDIczZOUdwQHtFPD5WWaZuaW22q1xTcaKQSCZr7f25psU7-EKLwu6W2JB7mf0WOjpRTmojF8OpUvn8CR3X4GJeZ44rHv2Dc2YwzkFO4A-C28VfLA7KrFF1y1Uj_ubgJTPZIHkQHh0Nz-yOGunyP7gUBxxOO9z0b_1zl5txGZXOJC6KoYBbDvsKwivMp_LEZlilWg2tGXAdZJEjqj1g1UcVZ2BRQf1rCaoOvZ8WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
ترکیب احتمالی استقلال برای دیدار امروز با پیکان: حبیب‌فرعباسی، روزبه چشمی، آشورماتف، سامان فلاح، حسین گودرزی، سامان تورانیان، امیر محمد رزاقی نیا، اسماعیل قلی زاده، یاسر آسانی، حسین اسلامی و سحر خیزان؛ ساعت 19:00.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/29455" target="_blank">📅 18:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29454">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYBgrq6G0rKxeCW6ABUaVDTwnTASaqJx3Lm1TMt_FNsLtuKff6RRKvHhgSYGXiOinBNR5hj8tsDGmFtyUPEzzbudMpXwIpPM-W1LfUtfhei4RkkAD2mgCQMngcyNc3EC74s0AgcqR_Ag5tgheiAG3PjD9k6BdUv0b6PaFmJd5m4j_RHB9mDl9QS_vAEibDvbIZciYSA1xG0_WK0YNAv5_zPF6n04blqW9oskTMC38K8ejPhyvbDPVlryUPZF3UlfVJy_C5TTRwzKCbzROt1LuD3ghn-Wk2FhBMfZzjVjzCtxXRsCPuCWx8lCbCvhW3dPZCwto6uz24L1ia6gol12ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
هفته‌هفتم لیگ‌برتر؛
شماتیک ترکیب تراکتور برای دیدارحساس‌امشب برابر اس. خوزستان؛ ساعت 19:00؛ تا قبل بازی امشب کسی نتونسته به تراکتور جواد نکونام گل بزنه ببینیم امشب چی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/29454" target="_blank">📅 17:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29453">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VThlg64qvBGu0zosifBGQkGMJtAwvFa_lanvsdC3B9vjXOAVaNdTKNEsdR8R2wk74OHtXYhDitghv3tFF3eI8Ja8LxOWqv-F0TW_eHmnJHIb_yg-oABzjcIOYHnna0IVaxIErTjCybA_hbsFZr12AawLVz82t-vzutEK-lRqPRJe-cj3MS4AwhuSnAEjccGuuVKerPEUT7qiTp7xDlHS4WmbsXuJrIzcgt3ItadD6B4iVfu2Hpk8chknjv8l-Z1bKpsq-lxMI9uSFzRUSjGzngXjH9jYKFhQnSaJSZWJQF2DJ8IcK2Vtk-hjL88f5F-4_KXfcmnU6f48DaUtY0VOCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای‌نشریه‌کوپه: براساس برخی مطالعات و نظرسنجی‌ها، هوادارای بارسا تماشای بازی تیم هانسی فلیک روبه‌رابطه‌جنسی در زندگیشون ترجیح می‌هند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/29453" target="_blank">📅 17:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29452">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2-VmLDSxOWyiXAsM7-8i8vucY5ybzaIr6MnkkdAozCiV8woxK2PwQGk9W7SSmWKElJvY9RttUFhjyHF9906KL91hLjcqzct9HS_yMFw54l5pPbD3217sJmMds7EKVpHwyN01pSRMiuRLjRm9kIHelmRywz9lcIEV-RKoHojS7Vld1PE9663CcoEiolRfHSNaEYGCZ15sPcdweq032qByjqnE09C-x8nhqKLB8ss2DHydkNBv452Tss7a54ShvJX4P8jg0Bwo671JMYQ3hDihccXZyO2HTxpto216e51pxb9xWR3J6JT2hihRhTpxZk-FwJt5g5CudT0rDzwck7tjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇹🇷
باشگاه رئال مادرید برای تمدید قرارداد آردا گولر ستاره ترکیه‌ای‌خود تاسال2032 به توافق کامل رسیدند و فوق ستاره به زودی قرار دادش رو تمدید میکنه. پرز دستمزد آردا رو حسابی بالا برده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/29452" target="_blank">📅 17:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29451">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NX8hc2zlKkolUd5TmjYtVy0SdE3k0qnB7n_jR2GiVOivtoPg2BUmI3dkVmKzHzFLDPIDc9ovJSwq1Pe65DtKGybNsHMKciwzbiiX_4O5V6Z9exiSaUkbE-wH7G4GBwRGx03og-t2gpgpZNY7yz3fovBlNHQknwWb_yUrPUVUx9BH9uTJmg6nRevfhsOzEv3INkWNp_r78q-hrgixH9P3idqTyz6b89Urx_mqvZXWx_bpljwFBy0Z-BUyqE8kv-40dWDYt3T-NxiAWyK2sGpPg5PuhLMv4_GVxxx6wDgxD0jz2O9_CMfeUrYiCeDyllZNrn4ZdydFDIcUZTFiFrdaFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات؛حکیم‌زیاش ستاره‌مراکشی سابق تیم‌چلسی با عقدقراردادی دو ساله به بوتافوگو برزیل پیوست. دستمزد سالانه زیاش 700 هزار دلار خواهد بود. سال‌گذشته‌ایجنت یاسرآسانی‌تلاش‌ خیلی زیادی کرد او رو به لیگ ایران بیاره ولی شرایط مهیا نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/29451" target="_blank">📅 17:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29450">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a53c9dadc.mp4?token=doLqVnSDr0cccPbqBeN73XCXwplfjlcIAvfw2B3z66Fgw8US6_8uuAwWBnd6Gg4mBEEFqXd_-rfaXmHiK8CPm3ZtLj6IH1qz-kK1mfEMQ6597GHBeCdiTzY0Wt-bcQU0bVPXGj_5aCtWNYi265ih-qE_CNVlJWFLXS-jRz6b_h1mxVGb27EIBGPr2pii-9KuP-RUixsq62nsMzoVW9SX-L_ugUgQTrvj78pO_WeO_ClWDPJJjHhN2lQlv-zaZPZeuffIGEnGgd07VDJkudnJluKQt7DuCLsn5aDACVYEl3R-P1k94C553iI-ykheDvO6Rvf8nrasXo_SooBqhe6ahg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a53c9dadc.mp4?token=doLqVnSDr0cccPbqBeN73XCXwplfjlcIAvfw2B3z66Fgw8US6_8uuAwWBnd6Gg4mBEEFqXd_-rfaXmHiK8CPm3ZtLj6IH1qz-kK1mfEMQ6597GHBeCdiTzY0Wt-bcQU0bVPXGj_5aCtWNYi265ih-qE_CNVlJWFLXS-jRz6b_h1mxVGb27EIBGPr2pii-9KuP-RUixsq62nsMzoVW9SX-L_ugUgQTrvj78pO_WeO_ClWDPJJjHhN2lQlv-zaZPZeuffIGEnGgd07VDJkudnJluKQt7DuCLsn5aDACVYEl3R-P1k94C553iI-ykheDvO6Rvf8nrasXo_SooBqhe6ahg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
صفحه‌رسمی اینستاگرام AFC با انتشار این ویدیو و موزیک تولد 32 سالگی مهدی ترابی هافبک مصدوم‌تیم‌تراکتور روتبریک گفت؛ ببینید چه اهنگی براش انتخاب کردند. بیشر بخاطر آهنگه گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/29450" target="_blank">📅 17:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29449">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SG72aKJ9Xhq8VQKMZNVY3YKWmdcIroI_Tcn8ovK4YqtMynhlaW1Pszwe3IisBfWG1qs57aPPdpvydontXWzpo6FlrPcdXCcQoo4y8lGIJpr08Bb39PNFxZk6rU9kGPjBKHGmmeV3Th-OGVMZV6BthUddRAsMnaZjUZelMG9A6tCJcopCjg_IMkwnmDGOsVRDrFsoSUeJSO35C16PrJVZMVKpvCY-I-l8Fg_I9luBEloWifkNEHHRYQzQd4wF3vjQodUfu1ya61P02IPYrkBVh9A7M8BEmq0krG4PwfKV7AN0DeUBa0IbNUXVzYntJ6rDAAogHBsjYWBQOgLZCqlulQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍏
قیمت جهانی سری جدید آیفون 18 اعلام شد؛ آیفون 18 تاشو قیمتش حدود 600 میلیون تومانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/29449" target="_blank">📅 16:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29448">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKx1nXOrVt4tiHu8in_ef72Kc6xNfxZ6AyjTRp2Odj6oH3-CVGK-vuYYH8V0_m1cqoYOQ9QSPUQ503CNmBEr-aDjynQLrT5NQQmg0Eb7ujieDwwrwiWxre1yKMiq4vxOGKPRoLdOA0zEChYa5Mtqi9c2uS5sqE75YkKkPA5yoReu_nhUWHlQ9dd_KqSwhRBqPl5ngjJldDF4dpmU2QJMuCcPhhSHSG68DJBoo_7YDmbR0Y0edCPn_46lR-khiWGinBqiopyDAhm1m59xFIG2lIOMhL35RtwgqcocGJNTBElo5hst5B44lYCcAMx5e8AFcwNzi5N5IDZ9jUzDUcQ7yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استارت‌پروژه‌جدید؛آرام همسرسابق‌سپهر حیدری کاپیتان سابق‌پرسپولیس رامین رضاییان رو فالو کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/29448" target="_blank">📅 16:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29447">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOqCHwPgFLKsqRogHApMOTYXz5dADR6dlQWlcK77OLhhpyS-0Xy6y2pKPn6EVc8Ac6d7Wf9Cse1i7BTvLs8u46okmKSF52niRBfCkEUtQkxBS3l-vx5NLBHT_3xYNqreHj2V1xmB2ITxnMBGY0SltL2sK8GhLIXgOddOPM6I2L-UKpaot9UQl_V2xNx8Y5BXOvU045KJ9L3Wq5JNzU3dVbzQ7DSdWMyZ0qwrvArlKcT1j-6j1ABfG08MxccJfLvcR-FjemAcTPrOpNrBhES1uh6PKzBSASFZG8yoYCgrMU5e0AsLD5hJaSFskFFvrWygYhtWFYBfgMKeXLjqRgjV6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌بازیکنان لیگ برتر تاپایان هفته ششم از نگاه سایت متریکا؛ مدافع مغضوب کادر فنی آبی‌ها در رتبه سوم! علی علیپور بهترین بازیکن لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/29447" target="_blank">📅 16:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29446">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9wxNfmmQ3kTzRwRdJTwg8PXZHH7GOVyg9H1OadW_0_LoobN5iw3g-Wauhe6f7meRcYl_oTfYTnnDXLtodriejCsqkeMrwRpHh_XTx8M5aGWV5Xo5MZ510LMJM-lk6yX4ZPlQwOVwjK0MNPjOh6qep42yFaCeWZmE_AQrknHYcihel9LRPd1RHMpP9JzKc4b3VrsxwjUq6w88xBJvdtw0LWxoff8DZH2oNgntbpvOze9jJx8PnZaWeypPoV3gUntbRKkXbKEWzAh9gJu6RrrA38MCTPQ77qRtQ2UEwTWy868DWZMEdrnMKn5ta0FiwZr3MLgVq6q4XGD5wFwl2kZgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
خبرنگارباشگاه‌اینترمیامی هستن که اعتراف کرده بخاطر اخلاق تند رودریگو دی‌پائول جرات نداره در پایان مسابقات این تیم‌ باهاش مصاحبه کنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/29446" target="_blank">📅 16:24 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29445">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSaDRkKtCnOcL60_runzo6N_S3VrARgMycaAcyWMyBkIITddURKEBUxBiKyUKpOUYNfbcfYNsxe_RIdlRQwtdxm1pH8sQQWCfO5goF9Lw2Em_3i48s5B6cW8PGP8cyeh16STsikKYyD4Zh-YV14W3dFNkuuVXumAdcZ8u_ZtQZlaWirTpfF7pRF8IwFKyVS1kvjwV0X5IqFlBt6EdFdGEG348_eBZiBUS3LknWQmdT9Fjm477i9oIvBU238jqgPfS1LzoGHQdm_noawwULRnp_nJ0_mMPYAPSdru49AUGAwaH_H8q5QTiKMUkGUZMBxz_p4KKwcmUfYp2wDfzAiX9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
ترکیب احتمالی استقلال برای دیدار امروز با پیکان: حبیب‌فرعباسی، روزبه چشمی، آشورماتف، سامان فلاح، حسین گودرزی، سامان تورانیان، امیر محمد رزاقی نیا، اسماعیل قلی زاده، یاسر آسانی، حسین اسلامی و سحر خیزان؛ ساعت 19:00.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/29445" target="_blank">📅 16:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29444">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9Sno5lw5UMm660rlKoYdCGnE5XzwQ75h9ckDhTK1V4yKxjoOKMWpfN8NSmwhM_jU8rziOkJXDYj0E0SzmATflOiW6V3uCoOTaHKlVS3NdHuXUl01Dk-RKPJMRl66yWg0ahxfnja2sctiSgeUF-VO3vcgbu51JBa83D_pxy_OL-QGxqExnI8vaAv7R453pom3W6GOx5o_ykxZUoaFc_IqMY2HIwpXCFQlDam6z3UCcvPgvP8Cq3XGv96QjoHkC6naizICjT6OVfBrYrVEtKntjpXKgOy8WPBWqI1pyTyw1JZt4LQyxcBwO6jeDYFBpJCQjtv4aKUlqJdfZUmYm8rSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌ وکیل‌پایه‌یک‌دادگستری امید عالیشاه؛ با شکایت بازیکن کهنه کار تیم گل گهر از خداداد عزیزی ممکنه سرپرست باشگاه تراکتور 6 ماه‌به‌زندان برود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/29444" target="_blank">📅 15:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29443">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afef3ee6a5.mp4?token=Igk89FLcYBIg2fF9NI6H2dDSGLJITrwdrxEpV4C9bBvJ48MHmREfUCBhxYRzytyfZRbW4XjyA1Z8kPCpHRJof3AvmZ7hRECf1Et2Y-6vjlEumZJehtBQMnbCxTxEm_FR-DO4SWfVRGbM65aSUvOol5Hernqut7AXBIRZThaqQlmvuzX4oHWwnLwLAGPxC3mh5bGpIZSRvZjaK8QGo1n5aK2itzUY0luQAtq3bNoR7gffqguwR62qtdPvBscDJ6H8C1Yp6qaQavmuhZnkCGG-1yp2z4d0p9ZpewxCypA0ZgjyTwWziEhOKw2Ql2W7xs6bnIMKcPMe3sFd0kTpWdGBOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afef3ee6a5.mp4?token=Igk89FLcYBIg2fF9NI6H2dDSGLJITrwdrxEpV4C9bBvJ48MHmREfUCBhxYRzytyfZRbW4XjyA1Z8kPCpHRJof3AvmZ7hRECf1Et2Y-6vjlEumZJehtBQMnbCxTxEm_FR-DO4SWfVRGbM65aSUvOol5Hernqut7AXBIRZThaqQlmvuzX4oHWwnLwLAGPxC3mh5bGpIZSRvZjaK8QGo1n5aK2itzUY0luQAtq3bNoR7gffqguwR62qtdPvBscDJ6H8C1Yp6qaQavmuhZnkCGG-1yp2z4d0p9ZpewxCypA0ZgjyTwWziEhOKw2Ql2W7xs6bnIMKcPMe3sFd0kTpWdGBOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گلایه مهدی مهدوی‌ کیا اسطوره فوتبال ایران و باشگاه پرسپولیس از عادل؛ سرنوشت مسی اردبیلی که در ۹ سالگی وارد برنامه نود شد به کجا رسید؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/29443" target="_blank">📅 15:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29442">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TyWOpqSZPVETsrQyqwXWHGgNFO8gDl-SMUy2HdrDGC1JzTjJF-2hNlqWMxDhZP4b84Hw5b0w7z26uXu6PQ94fy8hGSJa_rG7mC_KPMWh2Pcydv9Qopj-yrWyK8xZQPAZYGXqXhOfb-EHy1yoSVNslxXWrfGKFZ1ZtED93VSbrN6ImL-43MLFvSEAWTJGEHwzRQrHXuDUhLlqcimi71933n8Ahs5X9Ox2bjxfO3p5TVbDlqVdQKxPCbUks15bErHKMWwRLGgsFHDi3EW9fZO7LyqI5DwFCgyThhh4dVOU2mtla1kYbTgHUiriZW7gYH2MmcMtNsCanRmD6d64e5HXwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
🔴
#تکمیلی؛ باشگاه خیبر خرم اباد به دلیل حضور مسعود محبی در تیم‌ امید خواستار به تعویق‌ افتادن بازی‌این‌تیم باپرسپولیس شده بود که مدیران سازمان‌لیگ با این‌درخواست موافقت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/29442" target="_blank">📅 15:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29441">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3QOqMrH-blWdJe6nNHRf58otr5o5n2q98d55T6dLzsAeYDjRp96TfxYlIFh0O8h2Fkpb_I0w0rwG8rKvQkg-hwlTE0RiWlC56AwkS5icrG4Q00m9QkLJ94OEWl_lTbLhqrGerQRchQvHZ1VaaMtKkVSwblTWuJZyy3PUeujYAvRdtZhtO7Iw_bSh1OYvaRdtegbZe9rzj0GCXmb_7SiOY__RAKmWcrFSlp--Rq-3MKcdezWBfAZQ7qN4vuVClsc4nxSb_5aNRlmgBWeHF4k_OyQOUiV3nvX4V_bljdG-BnkHuQ3jrSyc5nKO_P0IUUNrtmB1SSTnhjdaKVYEgtTaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اولی هوینس رئیس باشگاه بایرن‌مونیخ: فروش اولیسه به تیم‌رئال‌مادرید؟ ازخنده روده‌بر شدم! حتی امپراتور ژاپنم‌ بیاد پیش ما اولیسه رو بهش نمیدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/29441" target="_blank">📅 15:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29440">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bogkoyqfEczmsu6YJzgIDFoi_VAF7wbWvNJEWIJbPtM764rHm1PjqpmBQ7DSmZNmRw6PlWeIj2JC_EXHQV7dmShAnEgBwQgf81yy3E6QtHlEywcNG4C5cu0wR_izonNsbYn2woaazQf309E7hiM32WBCz1z58_3tDXpiNFVtEKm02QHuWF-TTlarT-BJ0wSdbLC8WFmetAT8anq_IO3xXTogCfoHF3TXz19uBWDcTb9cZrOK23Tth79eQTs1FTafbJ8Kk7ugF5FnwZbOJKPOKxHNwkA-uYdm4XzdDGbbPAE_3CbRM76y4oU-1jXS1LtkxrVASoCqmIaNtVYY8t5RBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته هفتم لیگ برتر ایران
🇮🇷
استقلال
🆚
پیکان
🇮🇷
⏰
ساعت ۱۹:۰۰
🔴
انواع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/29440" target="_blank">📅 15:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29439">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMLatuUnJcDnz1vlTCSHXlQTx8Dwt0ZGbLL75yDTBU3-bbl8tFiXsBVepcf0w2ppzIIi31Bgmzu1zDovfA3zXQAEY_9ArHKmHvZOG2Hw9xMmqrk6BcdJnEu9jbuKSdt8mZHRIBDzPEelYR-NIKU39-XvqhPCBpFL_WDrZ_94qZoFi0YcOzUjHD1KhzikyZqyY160uvIFliK1KlPLZjBoOo6mj5_8wuVDZ8iknICilPo2foVzqJ5b5EZZRFutMt7vHqxixqqjLBwMSXRWd4OP2wWJv_78BwcMSCv4XJwoDv2kqfIy4urSYp4JfFmxRsG3MlbszplTpWX9wYZ_sIP0aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
پرواز تماشایی برای گل شماره 979؛ گلزنی دیدنی کریس رونالدو 41 ساله در بازی امشب النصر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/29439" target="_blank">📅 15:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29438">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5qUHs7vyfT-J1e79gS0pPsb0uhl0wSN_awKn4nL3l7191sUUzEaMvs0jJF1PA6u_uTXmSZQRhBlE27fmnhtrNnJZnqduXRkkzAh81J6lxQs3u8azUVo6n8KlGMMpDADmB5CvxMiAWhEvlSqUcTMX3zIKCDW46_QquosWARiWbm35mTQOXOxkeTLZCZoAaEzoi8BVPh6UE75lsH8XHXw0UkjdMhW1V-eufuavgljov5tnUYeFoEGEfQYbwlsse7gnxgJqJD5ta4TuNxLo0ngD-N0M85JVvM8fWpQ0JhJvUuT3VwgFNd6N1J4z41LiZHUMHOd5aUTy0sdkLW0u2fxig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی‌تارتارسرمربی‌پرسپولیس:واقعا موندم چرا بازی برابر خیبر لغو شد. ما چند بار اعلام کردیم هیچ مشکلی برای این مسابقه نداریم اما سازمان لیگ به دلایل نامشخص تصمیم به لغو بازی ما گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/29438" target="_blank">📅 14:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29437">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZnPzjc4miNR9InR41LW-uhK7z_atxB7uIf5ZQEgZ3BO2W2T418WUiQpIFXwNmzMlllf9ngSPMjQVBn_XUO8D1n6uFweHKgxmLbUnmFzlfiGCRqpwM5EMjdZHo9vxQihqF4Aqk21WyTvdWNsnNoga9O9zVZPXSn3U_WnPb64Ba0mB2dFrmTLZ9rRwtn8whvOd7G7OXDG4CQ-6pUaXRZ-101hTF8j82qGetJv9W00MBYe_cJM-aiDzGW-TnguQzHQvEVxkJye0dGhdPCQP_cyqkXm-ZvItpv3ug0Jg4Vtvv8SyRo7SlC7DgZu3-Ty4vBbHokxPjh7IOMyTZSeE99vrBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تاییدشد؛ باشگاه‌پرسپولیس‌ اعلام‌کرد که هیچ گونه درخواستی برای به‌تعویق افتادن مسابقه با خیبر خرم آباد نداشته و این بازی روز یکشنبه برگزارمیشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/29437" target="_blank">📅 14:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29436">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lL8xtjaMXGW-phpsGgBj3nhZiqHb3U4iGy4XJ7hzlI2fiiAUUdSfxjewOMR-gs3lAruiAN4ItJexAy3RFTVbx485Ik4UFs70YitIh1b9ELco-rx02xYfCwk0CtjOEGif5O3P8Y7w-maNu5xbljYMPgotQGDUfWstF-dUkuCc08zion1NIdrRKKNT3J3eitMdFdhJTUjHR1sfRfMIiIL4Y5ysJ1N-sgZ9t-HVSLTBCHjw36RKdg2LJlmuR6U0ty95A9wOdyORtF9gWB95lcc6mOSm8Np1vR6w1Ftl7uJN3Bl3YUeUHpJ5bjbmNfzfJrcxG-VtWruyRblvaV2SiqM9XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛علیرضامحمددستیار مهدی تارتار در پرسپولیس درروزهای‌گذشته‌با فرهان جعفری و محمد قربانی تماس‌های مفصلی داشته و از آن‌ها خواسته به تمام‌پیشنهادات خود پاسخ‌منفی بدهند تا بانک شهر در نیم فصل مقدمات جذب‌این دوبازیکن رو فراهم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/29436" target="_blank">📅 14:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29435">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNKhGW4x1oTFHhB781V4pQJO4tP4HpKFUnZh4LsXF3hBAcutNHIi0NakfrVTCtwHpkRDsYsaENpsTrutWq-tMOKqv7lcUKWWpBCKFB5IU3WDSkIW4U7AEiN0cJ7tF4-_4WShwPRSvdGFT8ZTn_pDKT99lSlLB1rMDOGeeupb6laTgN_iiQ2RbNtPtdVQcXcfU2mBN40xqMeD9Dfxdtu8H-XmJOoizSdR4fzZmLDeLB5BKXKUyNL9GeaanHGjSqszMbb1_V0Wm3R1MVRCoGCm3v2ih9pFArYRczC5VEn7XOVdtzMPqvdMZkwpJ3z28DaTQygCE4HX-k1j57ir3c6Czg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
بعداز حمله‌شدید هواداران کریس رونالدو؛ دوست‌دختر ژائونوس پیج کریس رونالدو و جورجینا رو در اینستاگرام فالو کرد و برای او کامنت قلب قرمز گذاشت. دوست دختر نوس بعد از اون مصاحبه علیه CR7 توسط فن‌های رونالدو به قتل تهدید شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/29435" target="_blank">📅 13:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29434">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCcKP0vQOyp8wP_Fy89X4sgp61xdlWE9n5PHJ22LdQI3GujL4GwNbAlh0N-FM4urexDeurCsbtFUvIOpknuGAoy-vRrO2CWGE0QWT0QyL0RJqy9r1yVHWeS8N5ZMrUw1BBroBagzE6OZgFpk9Nn6sSHQJXKObUXM3MbMCiZPw9jBtVeW9RCf4o4iARckv9aoxxZX1dqkbFPwNYiPXroCmTbSlqZN5qZ63FRYML6hnaLGVD0P4gSoo3OLd5yVBb9D1M-Z8hRpUSNJnUsImlZ97Zl2v77zGacM_Cz2-4zt66177_2eAW7sOdoWiD7_ajePwtoGPKD3dQKq1GSw01NmVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌رسمی سازمان لیگ چهار دیدار ذوب آهن با سپاهان، پرسپولیس با خیبر، ملوان با خیبر و فجر سپاسی با آلومینیوم درهفته هفتم لیگ‌برتر به تعویق افتاد. این درحالیه‌که باشگاه پرسپولیس دقایقی قبل اعلام کرد هیچ مشکلی برای دیدار با خیبر ندارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/29434" target="_blank">📅 13:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29433">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ga-jT0UEaC2I_Chp94nbmKvqwhsFteOpmzlQCzLlUxVd4WNmgD-aDYp1bKsiRVXM68fBX8lLKZtxEBFaiqe0s8mfONgjKn5X-ipOuU-__bFfnIyed2epKWpVgq6vGiRUKHi6IxexiG9YJUGcYud9H398Zi69NLgEyxNh9n1xdY-hvzjpVif72uWUQo26zv6hrZWDzN7e1pevrEcz1w0VxsGfd7NCmAK96LyAGEodk-zSqG4Ejv2CPgq8VwSna6SDb_zDjUC1jkLm9SYuOmSXrDJUDtaC0t0JfQZyU6IRWYqRZbuhyGDv0339wW-be5h_aNoF0KDB5k7_9cN_2qnGRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تاییدشد؛ باشگاه‌پرسپولیس‌ اعلام‌کرد که هیچ گونه درخواستی برای به‌تعویق افتادن مسابقه با خیبر خرم آباد نداشته و این بازی روز یکشنبه برگزارمیشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29433" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29432">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5LC-Bx0m3KLBZkAGQyrkels9IT7Q1MTzQt8obrOIQnycOBC13LfLY1WJ8U1iT5hFZzm__SUvmhBqeuwHsmQtogOR4hCrHygLCWSJG6WVMGrT41zNLvh4vNxSmWkeaeD-6GH0odtBTTr_PkutNSy5L3RP2dPtPLWI4z6F8ldRJtxvdeKJ0ukBaxl_TTH0I-9z9VYChwrJ3fEoc4vAw0QJ7MImYwxZGaj88G7r6vSw6zSS83YThyCgPnnbA00N0bv8eI9EdW1yCl-sqWC2xIX4rmOZ68mpflXlqPiBYayGld_oyrsYyS2agxY0cb8BGyoqlzN5DMLBWpwVrvBzgtG5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍏
تقویت فوق العاده باتری آیفون در سری جدید آیفون 18 پرو و آیفون 18 پرومکس. قیمت آیفون 18پرو: 1.199 دلار حدود ۲۸۰ میلیون تومان آیفون 18پرومکس : 1.299 دلار حدود ۳۰۰ میلیون‌تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/29432" target="_blank">📅 13:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29431">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNwbQAX2iLI7jLeQdVByvR6YQsPsrYZlqdOGCqfeFoQaS-gKoKSUWVp800N56XEeDAaOHz8uKf1njMKRmRSh3FgIadneRmxb2f3ookRUILzS510aLQFIz8vs4PoNYl1T6b9cPEgTAdUveYC79FbInHigmQqmar9OgW0fPbOPQ59EorTE6IaSR5c_jSXBLhaBEnBmN4hN2n6CJQnOPZeUT0q0gD90MDEPwCK5oTRb2ajUsyJjpkIkCIoGkGaGt9RgiNEqWwzyAxT04plVpO7QnIHTPSO_C9u3QHXcLHi2meujyig9pIVeCwsyDiS1iRsnsScD3xJd7dpWT3jA2FbOqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس تا این لحظه هیچ درخواستی برای لغو دیدار مقابل خیبر خرم‌آباد ارائه نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/29431" target="_blank">📅 12:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29430">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XF4H1US-YLmMmsjv3ZvX_TDAXXU0FysTaNALj_M4Zhuhcqc-KmLBTT_LFkKWKfwyzzOkG54jnRcpV8hqiYXXnUjkI1SMXs6IulXmFQ_Wc7pHL-_oUUcFwl-hUDo3VpYKlLBs9deWenn9kracrTTCR-fjgPWYj-IXt6X9iEjwrkgHiIT7De82BDVkuD5Qzd8zAthj2T7olCaVLE8MHa65Ai9YSTJZ4crpaVdU6XIX187sIKGpDgJ00AYr056_IGGrMLoKxVDTqE7V-NYBJOObtVIaAWcm6h3lsUkHH1b11Ahk3mMnMLnJUySObeksuCDeh6EE8ROLPyBQoz-zLt0jSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتیجه کامل دیدار‌های امشب هفته نخست لیگ قهرمانان اروپا؛ از آتش‌بازی آبی‌اناری‌ها در نیوکمپ تا پیروزی ارزشمند آرسنال در ایتالیا وبرتری لیورپول و پاری‌سن ژرمن مقابل رقبای خود درگام‌اول رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/29430" target="_blank">📅 12:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29429">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f985df7eb6.mp4?token=S1rDw72_oUCET8tmH-A5QnVT2YUdDDXoo4ylf3F1ihYqKh8aaBubC7DMcjihfQ0anyUpYo32HtA6MwCBDf9Ih5aq_gUVqoviiW4RPe-u_zEZ9tJZe-KzAuGrnKS5zii9PmdfXJBagwdJ4YOztaUHvJxfw_-XNRwaS1n51xYZl0nBb7_7uHV7rGq-0nvpW1s4yFou-2PyJL2XMMHRRastYHyP34WlFP0flteknsu9lFNBWr8VoGYdaVRLcd3e7yHifNcOZGZ2wfiYaZ9EwhpdX9irR8n-YaAML5oXHIL_C2vZvhxSK63jCsCEm7AcRcC-A82wRSWuc12wve9PPAzLnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f985df7eb6.mp4?token=S1rDw72_oUCET8tmH-A5QnVT2YUdDDXoo4ylf3F1ihYqKh8aaBubC7DMcjihfQ0anyUpYo32HtA6MwCBDf9Ih5aq_gUVqoviiW4RPe-u_zEZ9tJZe-KzAuGrnKS5zii9PmdfXJBagwdJ4YOztaUHvJxfw_-XNRwaS1n51xYZl0nBb7_7uHV7rGq-0nvpW1s4yFou-2PyJL2XMMHRRastYHyP34WlFP0flteknsu9lFNBWr8VoGYdaVRLcd3e7yHifNcOZGZ2wfiYaZ9EwhpdX9irR8n-YaAML5oXHIL_C2vZvhxSK63jCsCEm7AcRcC-A82wRSWuc12wve9PPAzLnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇺
گل‌های سه دیدار فوق‌ جذاب امشب رقابت‌های چمپیونز لیگ؛ لیورپول با شاگردان سیمئونه، تک گل دیدار آرسنال و ناپولی و آتش‌بازی شاگردان انریکه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/29429" target="_blank">📅 12:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29427">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mEOI7uU2g9W7XL9plGs543CjkbETUtCLUrkQiEVCE-em0-mjHeuscMbvaoT8hW1IvYX4SWZCzg_whoX9mLbi0G-dK4dcDIYMympsZh3CN_k-MTSXq0ih6so3MnnRf9TvUwUWjMTWGqAzZRnaIJl-MdQYLtH9AfqyDN9m70G3e4sAH6XxLnVYpx6-UbeipeyPpKjvQ9epGufZVM78Y7WiW6nynSe2HVPjbnNNsjwSHKNqKdRZCodesF7J3IpAYDHgXQdVdBgkQP1AvvdhPhlfpDmb_M87u5_M_Goh9ci4_r1T41n6h7LAtVRavMtGOJVXc6GLyvZdBWqvasPCb2UvqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XJw6NZIdcesB8d5D9dyUlzlM54GMBTn3YXT9XLDbOaZ7-IGJ64KodgNSqbZZk7jKihHJcmerEP1wALU19O5eLd_9I6U_Ox-xEW777QvBi9DG7Qx2rB6F2YFIg8qdkloArIxKmujWdqmHAHYjpik9RgBcDLgrhU65QocmEz-VAuMRzQCqqCcu_fY-Ux2K8gzat0aHaD_fJM1Emd76rYe07YyGBzylUnFT9AFgX7LjyFuzh_dCSB0ysX4PAY6D5qFp46l5toq-s7sxkgGZQGsZ6-NQRkQdSN4C5zFDjOGSGQ0Evn3NeU1sqiE5aDAZABBPi_4TcjbRZJBeJHGJmsd_DQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟣
🇦🇷
پاس گل دیدنی لیونل مسی به کاسمیرو در بازی بامداد امروز اینترمیامی‌مقابل‌شیکاگو فایر در لیگ MLS؛ بازی با نتیجه یک بر یک به پایان رسید. این423امین‌پاس‌گل دوران حرفه‌ای لئو مسی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/29427" target="_blank">📅 12:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29426">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b139c692a4.mp4?token=pR--xMYep2KMI54_NYF67L2qSPkS_sWefxM9GC9a7Z45kPZAfgXnMMTtWHKkEppJVJeLNFBKnQel9iRAdPp41qf7QM-cZllCUGxwvVkHak7w_igoD7V5d__uGyFlmQLiNGVq6XH6x8rVmC1tkb-HMbltNQeyaXmkQJJAlI-MHlAMAOIEMO66yBGb0aiyVSoDHZGAoq0kE8ATfhAA7nvEadFL8XRcOmRVmTKwcWJkRMBESvHwD_bwdKU4_rF_ZzqKyE9EugG34veRP7B6VaxBN59hmoqXQ3g6G9IzNo3xV39YSnsFnWgZtLGeMtMp9lxrld3dv0ulgf0I6IZQIV9-dReKSODykZxO2gbVDZGDumhfwETjzb7XBesbNpk8OqHAP9bnJI3fteFRsfnCr62o4pwavs_Ez8uvXxIRjoogqEEjxo00yV7cmvkILNTvyJW7ikwooGXqWuTjuQrEs7zej-90z3ldIJ6SeP5E8coN_mhRzpoEm0mMq3ZbQFJFnylz8_PyY-CEcBXLS_REq8L43SBcUdTIJL2RtYPaPwnLvBtZYrDNXhynqDpeedtUbb63BNOIutrkG5sFkX4IHSgaFsav13k41o3WIkETA4sEuvOQhsV5_RF8fTa2V5EzWGHRqm5dsV8lF9tkHl_2kHabnS_D4AbDNe-g-nnpZuh1BWs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b139c692a4.mp4?token=pR--xMYep2KMI54_NYF67L2qSPkS_sWefxM9GC9a7Z45kPZAfgXnMMTtWHKkEppJVJeLNFBKnQel9iRAdPp41qf7QM-cZllCUGxwvVkHak7w_igoD7V5d__uGyFlmQLiNGVq6XH6x8rVmC1tkb-HMbltNQeyaXmkQJJAlI-MHlAMAOIEMO66yBGb0aiyVSoDHZGAoq0kE8ATfhAA7nvEadFL8XRcOmRVmTKwcWJkRMBESvHwD_bwdKU4_rF_ZzqKyE9EugG34veRP7B6VaxBN59hmoqXQ3g6G9IzNo3xV39YSnsFnWgZtLGeMtMp9lxrld3dv0ulgf0I6IZQIV9-dReKSODykZxO2gbVDZGDumhfwETjzb7XBesbNpk8OqHAP9bnJI3fteFRsfnCr62o4pwavs_Ez8uvXxIRjoogqEEjxo00yV7cmvkILNTvyJW7ikwooGXqWuTjuQrEs7zej-90z3ldIJ6SeP5E8coN_mhRzpoEm0mMq3ZbQFJFnylz8_PyY-CEcBXLS_REq8L43SBcUdTIJL2RtYPaPwnLvBtZYrDNXhynqDpeedtUbb63BNOIutrkG5sFkX4IHSgaFsav13k41o3WIkETA4sEuvOQhsV5_RF8fTa2V5EzWGHRqm5dsV8lF9tkHl_2kHabnS_D4AbDNe-g-nnpZuh1BWs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو جالب از حضور ریما رامین‌فر در جشنواره فیلم ونیز با تیپ و استایلی متفاوت و واکنش نقی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/29426" target="_blank">📅 12:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29425">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M7MbyMKf6kk1j3POkDOjBG6SaEdEhSn2l3WfLJ0zbX7Ug4ZM5UiSOlA4ZF4lSr_G8JOzWOOMvaNDc4eQYXIx0pseMnX35tU2rggh9PN6KurKIaJ0f6UxZR0btxJjlwGUQxRhV18pdKFo-iUp3-ypsieT3cXxv4U9o60nwWhGqPdiAzTImcpH8WHviNAeAgZRJ8obEO1ixaG3QYhwYuWhN4FadxVAqb0ctW_qMjA241muiqsHpo6UGU_HXelFIotjZX0ws3lfPVK2sVcPzK3x6vCyL2iW5Uljbjy2RmWEzgd3v0nzjWIuoLi6dOW-N6L4WzVQsyuclF4kAoTbSqAF9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
بازی‌های‌جذاااااب
لیگ قهرمانان اروپا
رو با آپشن های تخصصی در
MelBet
پیشبینی کنید!
🆕
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
🌐
دانلود مستقیم اپلیکیشن اندروید
🤝
اسپانسر رسمی لالیگا
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه ای،مطمئن و درکلاس جهانی پیشبینی کنید!
برای ورود بسایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/29425" target="_blank">📅 12:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29424">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sG12z7HPMSGANSby0F4rCABpWEi8JS-YAXTKFES6HXDA0cxymxuAmER9pBmeG6GO47rTld5Su5ZJsuDuSRFuqC5NERRu0HMFytldCblrPfC0r7v2yI70CxQJeHY1NFHaB9SCXR7gdqmk05qHHhGTjUepVjsbGBVfP_oAkvfkp4xoCkcGbLVF6BpJQni1F692PESymGGgLp6beJ6GXOeKU0RxuowVWLggSvanISn9kgvzVzUJMeYoVDiQJjETCnUf4gp_s94MWNYl9k0WlnpXm8uVzdG8EEnjNM7iBJCqlJjOgwjKJ9vtNtIw2IF9NUYYCsgvqttoe64w2fqwMgYE7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
ترکیب احتمالی استقلال برای دیدار امروز با پیکان: حبیب‌فرعباسی، روزبه چشمی، آشورماتف، سامان فلاح، حسین گودرزی، سامان تورانیان، امیر محمد رزاقی نیا، اسماعیل قلی زاده، یاسر آسانی، حسین اسلامی و سحر خیزان؛ ساعت 19:00.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/29424" target="_blank">📅 11:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29422">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/syQXW9X7RCK1kNuj2l0hUZZ_OQboRAQm4T6J48SFKrJg92Gn2axZVxXvqZvYepkBB5X85k85KWiFTg2Q2p4_as3cwrpegvvmmCBjElYWGpsMBInB4hy-RlSoiJIGn9_gdIodOI3QwKjoz96kVaW2Z92kne9lbwVwEosc8DzYWw8V3R8nvDm4URzkeaftwcgakeU1A_1M7O26gHf2o0QtGbu6Od85VVuYL4j0Y0OfeCXunYcaEXH3uwfiJ4O8Btv5X47sK1fDGXWDydVVt1IagGDUzNqjNcYzXrXbMQ_7dfK-3kO4NpzFGEwb3dbbW7YqdMaudjdPNrUQHJU2wJhSnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cQI4QFnnf1N1XBmhBlDJYn_ZxmcsKB2yp1P72DpR9_ruLeoEwqeFpi6k7FfjLAYUkhLDt3GQCFZ9E46FkzIWkqmzryf_MqDvrtZBjeuHW0HfoljDcZFKcYSlInh60eubP5TNjtxIO6xyv7t-uFUYMEJeLoUEw8hOHjcPX1--e35EcxEJCQzCXbmM5LoYw0mvM9CooAGhsA0IeVTIm0IKIFyZ4GFLVCiLpUMdN4G-dkFYnWFRzsLR_78mYDE_6U34LRq7QDonWCnF_x3Em1KOXO9svYNZNOkXs_fj7guilx-MsFF9cEV1y8XvndKFpBv-EE462OH94v9cN8wj5spfKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚪️
🇹🇷
روزی‌ روزگاری آردا گولر به‌ این شکل با رونالدو وارد زمین میشد الان دیگه شده فوق ستاره رئال مادرید. رونالدو در مصاحبه اخیر خود گفته آردا پتانسیل این رو داره یه روزی توپ طلای فوتبال جهان رو از آن خود کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/29422" target="_blank">📅 11:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29421">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2jAmaqjvYx7ZggABtZQmNThIE6aWFp7zTLI9L2xiBoc2i9453ByegrR383kXKMfNUadBsPEq6k9VTvEQVk2if-C0lbea8Zu2H2lKmOdvtQOJOlCXtUNfquvzlYYaC6rxxLUmepQtqiYD59BNtV7gy5UMUNwfRjvPXEEL9M-CCwfdw_MywXlEaKIy3Sp80l_6tf2bs8fXrODz109N0IYzWiK-LzpEWkORxuUlKsFKoTo00yeiBo3yQZFhAoGtZX33HLGfKvjLu9H2ccC-8dFC3RX4fNP1I0PEyPvtFBeAZKRVtCpnYNUKcXeUQugduKwJXZDZ1R3WbQ_vo-0FQQmKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
ترکیب احتمالی استقلال برای دیدار امروز با پیکان:
حبیب‌فرعباسی، روزبه چشمی، آشورماتف، سامان فلاح، حسین گودرزی، سامان تورانیان، امیر محمد رزاقی نیا، اسماعیل قلی زاده، یاسر آسانی، حسین اسلامی و سحر خیزان؛ ساعت 19:00.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/29421" target="_blank">📅 10:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29420">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05d0b23c5d.mp4?token=l74KthpYsNVOCe21epahonWRenDWyHc-Z1r_Lm-SrbWDl-3v48qRQmurruXOKmy29AA37jHFv7E21ZCndO2iWaNHM_1QYgDbqN8ZWCM0MRbn4txdtL8RTKkPrEZZ7hnEGR1TE7XzxmsfeVVMRuFxaqH7M5yUnS3t69E9WfcxnT0pz14-h07YdRLGdSuCEcazNdyke9lhfBP2VoPutg1MQC7DRus4JFwX0iPvFVnB14V40CL6HzyHMg85ih8DIJ6hHSzTV9ugbu3aPZhTD0R4OHPmEwgtE6gAgUM61pVCr0mVHxhdOdfNs4oHRPI8KBjHhggjyz5LEVClcNwun2XxrU9RNKNABOZBsRPJ80Svd0y3TPGpiXZPpaysmFCF82aQNWXDPjGXkJYqfyLPK8Aei-1lBPPMz7tGYojS0q4FkuIAbL-FJCMfpkBogwXJJF2rhHjc65kJ5FCwuoYRSSluKcPtoJ_XBf4sNrK83Ek5HPFAOwqaqgUrqiZqr2IeFp--JL-Y00mcsZRqzLX3UnB8khjuFDgEYU41T0z2fRBoGnMJedRGxsflXW8a-h0CZucKTjJJac2N9iyVFkAWMVpahnyxq0NJOPty3rPI_yvQgw8P-a4ss_xEAbBluFXueANUFXz0NqHoz1XECRLfvWFsqqgHC-IikxgT48mlaCSxbJc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05d0b23c5d.mp4?token=l74KthpYsNVOCe21epahonWRenDWyHc-Z1r_Lm-SrbWDl-3v48qRQmurruXOKmy29AA37jHFv7E21ZCndO2iWaNHM_1QYgDbqN8ZWCM0MRbn4txdtL8RTKkPrEZZ7hnEGR1TE7XzxmsfeVVMRuFxaqH7M5yUnS3t69E9WfcxnT0pz14-h07YdRLGdSuCEcazNdyke9lhfBP2VoPutg1MQC7DRus4JFwX0iPvFVnB14V40CL6HzyHMg85ih8DIJ6hHSzTV9ugbu3aPZhTD0R4OHPmEwgtE6gAgUM61pVCr0mVHxhdOdfNs4oHRPI8KBjHhggjyz5LEVClcNwun2XxrU9RNKNABOZBsRPJ80Svd0y3TPGpiXZPpaysmFCF82aQNWXDPjGXkJYqfyLPK8Aei-1lBPPMz7tGYojS0q4FkuIAbL-FJCMfpkBogwXJJF2rhHjc65kJ5FCwuoYRSSluKcPtoJ_XBf4sNrK83Ek5HPFAOwqaqgUrqiZqr2IeFp--JL-Y00mcsZRqzLX3UnB8khjuFDgEYU41T0z2fRBoGnMJedRGxsflXW8a-h0CZucKTjJJac2N9iyVFkAWMVpahnyxq0NJOPty3rPI_yvQgw8P-a4ss_xEAbBluFXueANUFXz0NqHoz1XECRLfvWFsqqgHC-IikxgT48mlaCSxbJc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍏
تقویت فوق العاده باتری آیفون در سری جدید آیفون 18 پرو و آیفون 18 پرومکس. قیمت آیفون 18پرو: 1.199 دلار حدود ۲۸۰ میلیون تومان آیفون 18پرومکس : 1.299 دلار حدود ۳۰۰ میلیون‌تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/29420" target="_blank">📅 10:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29419">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/573430f5b6.mp4?token=md-XfXJaNM4MZKApxAcCB3EF-t0WwFWohi4RL5aHLCJcWJSxjSCs4WNgpT1RobFBPnI0gafHio3TcsZL3UdiJv9PgayZ1wV-R930Qf2jHRTMeFAc-R_tLOFXqBLqst96JTuXerlBqbtsbhDy8XxhbmVgLzRaXdEwhIMv9YPkcnvQCT6mm3Xg-e2p-e4heMAmT0Q5GhFhR1A2cQc_QDULOzpQrfKWqqLjSF4vfnC66RdTgjY5_NIY69xmDCCJwTntk7cBD6AWH7X6R5r_UKg2aMOWsXMCnDVfkK31VEmb_905LmTgZVN9BzyfF3jbDz-on7V18a3Lw9IlofqmCuLrwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/573430f5b6.mp4?token=md-XfXJaNM4MZKApxAcCB3EF-t0WwFWohi4RL5aHLCJcWJSxjSCs4WNgpT1RobFBPnI0gafHio3TcsZL3UdiJv9PgayZ1wV-R930Qf2jHRTMeFAc-R_tLOFXqBLqst96JTuXerlBqbtsbhDy8XxhbmVgLzRaXdEwhIMv9YPkcnvQCT6mm3Xg-e2p-e4heMAmT0Q5GhFhR1A2cQc_QDULOzpQrfKWqqLjSF4vfnC66RdTgjY5_NIY69xmDCCJwTntk7cBD6AWH7X6R5r_UKg2aMOWsXMCnDVfkK31VEmb_905LmTgZVN9BzyfF3jbDz-on7V18a3Lw9IlofqmCuLrwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#فکت؛ برای اولین بار از فصل 2017/18 و بعد از 9 سال، ایران هیچ بازیکنی تو لیگ قهرمانان اروپا و پنج لیگ معتبر و جذاب فوتبال اروپا نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/29419" target="_blank">📅 10:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29418">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HD2QDCT4Uf1W_nwY8qT3BkiRIztog_NvHVbCJzhiaybHDN8kogpQyOo0Sl7bxE-BG3D0tWDYGadAEGBw_lSceBfrKLIfSOH5lgP7dtn9g7huYTUUtfUwBqu6c7jfZRVQa9Q52IeuDzQ_1VEnhDdzYOaj3DpZ1PEGN-nx15i97ak1v70yBAlZADQNfd6LFW0UP77DBMex0vsJdxpfcSQlZfAg5bLaOjYiv73ydbqJlJu8lar8Xd0-vyu0QjN1BLcdEkRjcSq3PW9z9krvYbawg_2O9LcPB-T7-UYcbWAw-R-O1u8eyhctJvyY1yrDQ9jKs6UcWk6LQj7DJ32E3-M63w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس تا این لحظه هیچ درخواستی برای لغو دیدار مقابل خیبر خرم‌آباد ارائه نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29418" target="_blank">📅 10:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29417">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58d9326281.mp4?token=DNx_1ZFqHHL1B2o0R8YueP5huKlxzvAti-mSttOOWvgNw9hO4oyJ5bLdkyBaVI2PoXunh0V034cw4KcrO8ER1JP7Mce3qCEtANq5JssukUTJ2pS6QwdzJU3MFGKc_PlRgU7pHRtfqMPjebNebRoAHWsvYXKB0rGWmMxfmB0JDhQuXU33cAfaWWN8dGH2aVYWhcLcq26nenDu_J0cqIL0au-A6-ZtWXdoWsuNpI2-twhUqC95mg81w_Bw-3Z7KvG6xJ8BBnMVhVTQ1geIW6TFrwP8HKss7YWXMLXORdUKByJlh8oQ6sJFPPb0WpBNcJjQqA2RPSC8-rtyKqb072WmJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58d9326281.mp4?token=DNx_1ZFqHHL1B2o0R8YueP5huKlxzvAti-mSttOOWvgNw9hO4oyJ5bLdkyBaVI2PoXunh0V034cw4KcrO8ER1JP7Mce3qCEtANq5JssukUTJ2pS6QwdzJU3MFGKc_PlRgU7pHRtfqMPjebNebRoAHWsvYXKB0rGWmMxfmB0JDhQuXU33cAfaWWN8dGH2aVYWhcLcq26nenDu_J0cqIL0au-A6-ZtWXdoWsuNpI2-twhUqC95mg81w_Bw-3Z7KvG6xJ8BBnMVhVTQ1geIW6TFrwP8HKss7YWXMLXORdUKByJlh8oQ6sJFPPb0WpBNcJjQqA2RPSC8-rtyKqb072WmJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
در شب گلزنی کاسمیرو و لوئیز سوارز برای اینترمیامی؛ این آتلانتایونایتد در لیگ MLS دو بر دو متوقف شد. لیونل‌مسی فوق‌ستاره میامی 422 امین پاس گل کل دوران حرفه‌ای خود را به ثبت رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/29417" target="_blank">📅 09:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29413">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_8g52Lv7x1n0RiJOyEMsyPa9SkzsSENNBa9YYM1Fkl60Ls3vKGoYUIuX9iAOQGCkEEvy044E794Yq1R34g00P8HcehQ9BeP55nNyfiRr7ls7BD8jJHKntcUDMHYwebZKmLG4Op9W0WFbikAvgtnLSmvwyf9yIbLsnCqwWeSo8GX9KiLdHOw8md5ijSHNgD7wgbCKi4xEQ3OX2mmcLjMDtmDA3BChablclZJQEBRMRs9LX1MW_qKKsCnlCbbWLu1qSCctvAz308VuheR-oohYBrATdH1nmG0hRMBLrVByBYa7zNhXiNpz2LKj1wzN_DVxJNSAz-ByEy-Dotx7pwNhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
آیفون ۱۸ پرو رسماً ۱۸ شهریور معرفی میشود
‼️
اپل با انتشار دعوت‌نامه‌ای رسماً اعلام کرد که در تاریخ ۱۸ شهریور ساعت ۲۰:۳۰ شب به وقت ایران رویدادی برای معرفی محصولات جدید خود برگزار می‌کند. انتظار می‌رود در این رویداد علاوه‌بر آیفون ۱۸ پرو و ۱۸ پرو مکس، شاهد…</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/persiana_Soccer/29413" target="_blank">📅 01:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29411">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LF58umuUJX5C7maRGA8_m5jtwzO-r6Lhp_k2gLkT6Mfb6RRXNJ_vQGKPXYlDVaE_Jokqum3ZQcBlS1Msj1Ml4-Cj-RjssQGQUvCs6CpQLl9pG7jkrcoziyL15nEl9H8ycNVFyudiqATiG_jhsofTkYqbKRjIFhfbVBTLb2T-Py5D874vypyxb23MK-soKpr2iunybcO4XQsB9euK-9hBU8CQTt2J8Au2sNWuKRm-X0Ul7LS5lGS-Z5LjrwjjuWIY3rXJqu2VGy5YTUq7c9zyS_v6kwTws9e1Q3mkKm1oG1Twz_YkbHpiJtv42Si6WQ6U-KB-qPqKzPimBLZy6bE9DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ شهاب زاهدی مورد توجه چندباشگاه‌لیگ‌برتری قرار گرفته و احتمال اینکه در نیم فصل به لیگ برتر بازگردد وجود دارد. به زودی اطلاعات دقیق‌تری در این باره خواهیم گفت. حتی شنیدیم ممکنه زاهدی در نیم فصل یاغی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/persiana_Soccer/29411" target="_blank">📅 01:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29410">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1208f58f58.mp4?token=rlkvrwaTy6H6JBz7K0Dbiqz-GlUfIOzq6xmj2mzMcd6e8VWXsP6c5nULK91q0YtkS7ivnBfWGDO58eGS3t_dzMzLnVtJBZnu9bSYrgsDQLWrGKnbBRYjfs6DPGa_7D56pbsEv8uVsOzht9H-tmguHxHEf4IpXoRIJNVqMtWkIRZPGkpD0RZ8euKn9hx5U0Wa_QxmB5U0-KPcEM-gApRczKF1_ng5K31fE80va5my8ubqOEB5oGThZ655aJsjLA-qrvaQ_uWKsEdgX7KguaXkVcU0PGs-HmBSL_O9b8OF6Yeg0xYIg42fXI-NxnBRP7SL8qA-cQbBbcRl3WqMELwh_5aueoMqnGTdTsEX0gkgqii7pLADyD9H3yyYXkFFI3tKzXYn2MC-t_kYJjrc-k3_lugTSLSie0s2wBV_zxIfQIzGmMapSQySEf86xk3VSPxHsy7pihjL8PgmWs7SdJtKpu_0GynADQk8Cv6sBF1VkbCQesRth5B0jROC4StD_4BMYlzLFUg8nJfHXEaHEH8BYKL66m4pPZvNLLcAL67HWFCDgVgz5WCtP0-4qa00I8VW0xtLjlMh0wHBwfjGNKqeqotci36Ii1_b5e-EB_TKx0H479SuqsjONe-CRgxPX12sqVoRpfIDAlrXqBL5PeNWFCgYNn6nFW0rF_TmAFsebIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1208f58f58.mp4?token=rlkvrwaTy6H6JBz7K0Dbiqz-GlUfIOzq6xmj2mzMcd6e8VWXsP6c5nULK91q0YtkS7ivnBfWGDO58eGS3t_dzMzLnVtJBZnu9bSYrgsDQLWrGKnbBRYjfs6DPGa_7D56pbsEv8uVsOzht9H-tmguHxHEf4IpXoRIJNVqMtWkIRZPGkpD0RZ8euKn9hx5U0Wa_QxmB5U0-KPcEM-gApRczKF1_ng5K31fE80va5my8ubqOEB5oGThZ655aJsjLA-qrvaQ_uWKsEdgX7KguaXkVcU0PGs-HmBSL_O9b8OF6Yeg0xYIg42fXI-NxnBRP7SL8qA-cQbBbcRl3WqMELwh_5aueoMqnGTdTsEX0gkgqii7pLADyD9H3yyYXkFFI3tKzXYn2MC-t_kYJjrc-k3_lugTSLSie0s2wBV_zxIfQIzGmMapSQySEf86xk3VSPxHsy7pihjL8PgmWs7SdJtKpu_0GynADQk8Cv6sBF1VkbCQesRth5B0jROC4StD_4BMYlzLFUg8nJfHXEaHEH8BYKL66m4pPZvNLLcAL67HWFCDgVgz5WCtP0-4qa00I8VW0xtLjlMh0wHBwfjGNKqeqotci36Ii1_b5e-EB_TKx0H479SuqsjONe-CRgxPX12sqVoRpfIDAlrXqBL5PeNWFCgYNn6nFW0rF_TmAFsebIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
درمرحله‌سوم‌جام‌اتحادیه‌انگلیس؛شاگردان ژابی آلونسو درحالی دو برصفر از لیدز یونایتد عقب بودند در نهایت به پیروزی پرگل شش بر سه رسیدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/persiana_Soccer/29410" target="_blank">📅 01:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29409">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZZukcBfqS3vcZCrwRJu21KaAOBXtgs7Oy1PSoZz8jYEQyiOq2IpZRFoOUlk9pefNQikLEEdalENLJ8tlEHqqmEU-NUoEZ_3K96rfO5VayamZQ0dIGTZxYkNpqBgazfNsGaTU2qmSHPg8yCbaT6Mkw3AXi9OI_YRmzFaAgCmOBjiNZUJSbuYKOcrYlDDvUPHbuZgUoRG8vlD67IUW1_LBY3edlvcOqIdMpSq3Lnyw1jWKE0XS6IkS2pY26ZwB28XVVf8FQaq7-7SMn9F0J8J31hzNXTkW9_IHOAD7Fq9dqSB7EjTTvOTZ4yckqe1pf8v1M4qMFl8zlp2umFJ7QZfag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#تکمیلی؛درباره محمد قربانی چون در لیست مهدی تارتار قرار داره باشگاه‌پرسپولیس در نیم فصل بار دیگر برای جذب او اقدام خواهد کرد. رقم تعیین شده برای‌ رضایت‌ نامه قربانی 1.2 میلیون دلاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/persiana_Soccer/29409" target="_blank">📅 01:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29407">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aB3tMmE58ZM3YhPwQ31YtGCGl7bgZohF_XRZI7G309SWpUA_buoA6bnpxVCRVVD-rWxxdTmym-U6G9I5q_PfpydDo6_1lPEJ8wLxRjLvlpBYczH-b_JOtUp5SYRBuKDwEzU5jTrAykFwdDNC-NyBV00zfNA7f7feKgCUmXSNquZg1dUiTeA60_-bcGWYYu411Xmv3Uj__xHTYVWNb_sJZ_fnff5CUd5ngSPGYuYxz3bhpW50XCJjB5a5bJGYatZGaPVXzb_VOFuE7Wh3Cik4upyBGDOjO36CbdzGgEvWUdaQbn4VSVtxx3a51rvvysVyjdALaBeca09A7G967YlAyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز
؛جدال آبی‌ها با پیکان و نبرد یاران کمپانی باپدیده‌نروژی‌فصل گذشته چمپیونزلیگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/persiana_Soccer/29407" target="_blank">📅 00:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29406">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sr14r9CgDZiJaz1R4NeBS38q97RXda1zOkCK3zv6p9AIDOqSg1f6LL5Uq9O2n_D3MDKrGgHu0LMG0EvlngppLLFzo6ED2lOZu35bBr4TzKBhgpV0oQOAROXRugrDJRjSh3tY1EYHMiF3pf50qneG69CtXctjmWkMM4bX-nK6vR6S0lq4hJxL4URsDyEPU1GDTej9jMOg9KfDoRlejvLmI4k9jtFD-zFgf_7aR2DShTsMDZBvPD75jbbjwAOWda0ILNHK_3HqSzRsdgwRUmsc0gMoiGKADFbeCfF46XZVUC8S0rKGLKGUiisynM7EhxuN7EawbNL9lF_QlsZpWtAVhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
ازبردارزشمندلیورپولی‌ها در آنفیلد تا آتش‌بازی بارسلونا و پاری‌سن‌ژرمن مقابل رقبا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/persiana_Soccer/29406" target="_blank">📅 00:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29405">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhvXNRgaWwHP_Nj3cpILRMBwsO2UgcFDySqVb80FKA_lHU1zXbg86JAZq2u8KeWl5k4GJ5bUr5bzLjugBKgHyiUZg_CDnN3mG6dpHIPWVFEhfD3chE_Dk1ZNKIJ9eGtjAr1ig8b7enj0zRGjOaAqZllTOf8ctkoDL5_OKHvaQtzdqmS4DGQXKl6SSsZ0XHGGDRJs_XpqZpFGkTq4VlzuQIO6QmqqZQoEoS2sb6y3_5P3I0f6u3i6Xc0VCXWS7MYg7EsEBnPta3vkfLv2if7CugnixB2VyAM151zlTFHbWn_8qT4130GBmKU5bN3c3nhB-WgbxiWLPN9ogvyCjpw9zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
درمرحله‌سوم‌جام‌اتحادیه‌انگلیس؛
شاگردان ژابی آلونسو درحالی دو برصفر از لیدز یونایتد عقب بودند در نهایت به پیروزی پرگل شش بر سه رسیدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/29405" target="_blank">📅 00:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29404">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇪🇺
نتیجه کامل دیدار‌های امشب هفته نخست لیگ قهرمانان اروپا؛ از آتش‌بازی آبی‌اناری‌ها در نیوکمپ تا پیروزی ارزشمند آرسنال در ایتالیا وبرتری لیورپول و پاری‌سن ژرمن مقابل رقبای خود درگام‌اول رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/29404" target="_blank">📅 00:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29403">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwo542z-WTn81lg3Gu3VRubWGpxSIN3iRK_RkvM8Y6F0XgKU2GvA69uHbCts8AUh4sFS-ASPqx7gBytS3s9fwl4BSubSyXBE8jFntnDf5HNaAUmOGCtjvM-6Ez_poqG_-7GPPU9TUdq6QFINe4nJmNA-0MlTLIQ1Qi5pMQMuuETfuHpEXyf3shNe3QaKa19E9N4VwfR5TJYdCTWjcHuqT9jlpN-4hCtlb147s7ocaWqpMJDd9H9uycGkpLgB-mnd8CNtzZu10ygTirR6yAI7MPIGZ2PRwqt1YVz4fNnxEkWwxjG0vTDKTfcvYr0T7LPpjX9K_DkKTDMSjpezE5s0ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا؛ شماتیک ترکیب آرسنال و ناپولی و شماتیک‌ترکیب اتلتیکو و لیورپول؛ خولیان الوارز بالاخره در ترکیب اتلتیکو فیکس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29403" target="_blank">📅 00:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29402">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAsYGlwH2i8x4QxUkHMKRjXLcriQHDeo3lUKVckGG3Tm2ct30-Jzv0-GUiITj8uKsTs6CY1OU8KEAWsCr-wpHJuh5KdyAcjOwsQgR59AUa4nilPFXlqfkCzl7tkox4iZq_2k7Vtn-mvwKxKi13NnwkJiYDL5o8mKf8ju-hxfZr0YB1Z_PqYcPx1TgfeKFsyPz3m8_fa77q_5xtVqEnT-mq7TnvhHi98pJBNtBjzIkc5hzedh-cy-GKsEm_cJLPKGWWfCns-b5pXtaTmwnjuikGW7Tb13m4io5MlhW2IbVzhvRCU6nI1VnSsi6Iiu0tz3acw4KJSa2dmkrrzm_LcxrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🇳🇴
#تکمیلی؛ باشگاه منچسترسیتی انگلیس برای‌فروش ارلینگ‌هالند ستاره‌نروژی 26 ساله خود در تابستان سال‌آینده 200 میلیون یورو میخواهد. از بین دوباشگاه بارسلونا و رئال مادرید هرکدوم این مبلغ رو پرداخت کنند بند فسخ هالند فعال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/29402" target="_blank">📅 00:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29401">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7sVhO302qvoiePHAaKZzacX1E7iX80eRk-VekDpeMn6YM4Rouc6nHBRXESxqp2D4vVxYz4DHIu2ZmM8Miko3aKZIQZCxuuSe5SlROqZwuJv2lqKyx7yOEzZj3CVfsLDUlbr-WmsurLbeweEZIiN5nQIDOKB4AWYCqyQhONgQf6CwwW_SSjcxpEjHnKKVKwupRY8CCCrnRcYDq1OJhMKl21Xvg1yQKh6tQYcMfpeYMlDwSLO1I2OibVuL84q81UhrgISDrN5iiPwSRW_plF6_jJYo-C2NkOn-RUjDMYYNGJWiOF2jCp0xaBVSFA8bqAVFKTFUo8RN59dCt_jXXSRnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇴
طبق گفته اکثر رسانه‌ ها؛ این آخرین فصل حضور ارلینگ هالند در باشگاه منچسترسیتی و لیگ جزیره خواهد بود و در پایان فصل راهی یکی از دو باشگاه رئال مادرید یا بارسلونا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/29401" target="_blank">📅 00:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29400">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39a8082900.mp4?token=Ea9Z-ysYhZpl3F1YxNeuWEs31afTXUHgf7d4cKjowP3uNbnRRMV3uPd4WcHhI3HzdeBbBRoOTVDIxQCuWNB_1UtVkoHruf3y64qJ8ASOOBc0gBRaQ0HVVnpdWudUbBb80ZvLZBo0MGJ7FaVOOcI9-kp2pyP0RsRzSrJIZJJeUWSb90kk1dx5dmUmkwOZYVgg_ayEFNK-mQDBaqBWxSYYcdi7Vu-ECc1VKu8XvNFmkHKd8I6MbzkiJc8hdp_CZAdZr7I1KRxN2kvWG44-nsWqIjCsH7tCX0652YjYck-vMU3s5W4-ErxYlPfkbkYwo0Jp8SPyGcgAQBzHQd2Y_DSziQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39a8082900.mp4?token=Ea9Z-ysYhZpl3F1YxNeuWEs31afTXUHgf7d4cKjowP3uNbnRRMV3uPd4WcHhI3HzdeBbBRoOTVDIxQCuWNB_1UtVkoHruf3y64qJ8ASOOBc0gBRaQ0HVVnpdWudUbBb80ZvLZBo0MGJ7FaVOOcI9-kp2pyP0RsRzSrJIZJJeUWSb90kk1dx5dmUmkwOZYVgg_ayEFNK-mQDBaqBWxSYYcdi7Vu-ECc1VKu8XvNFmkHKd8I6MbzkiJc8hdp_CZAdZr7I1KRxN2kvWG44-nsWqIjCsH7tCX0652YjYck-vMU3s5W4-ErxYlPfkbkYwo0Jp8SPyGcgAQBzHQd2Y_DSziQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ماجرای‌ازدواج‌محمدپروین‌باآناهیتا درگاهی عمه دنیس اکرت مهاجم ملی پوش استاندارد لیژ از زبان داماد سابق علی پروین: پروین بشدت مخالف بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/persiana_Soccer/29400" target="_blank">📅 23:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29399">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6DzvSauzI3s4LqWp8UKVR60pAq38xBHKmvNiFZmvQcD1UKEYFTIrcIM1jRGpry73-zVBjZcoGsGJ47INmobf7zwm6AUN3ZKbQPrHKS7pfRVXYch26qwA6OtE5pD_RSkJWwi2Uw14O9BoVhtdTGB9rrM0vZGkC0N65ASYkKX2Es-aLfGMSTneRIjyNEvmkj0Pi0ruYvXKhfkRtO7Ax3yqCKR3GyNhhLl72bDc2VBA8Oe1CiuiNcANAVq0IOC5dKjnjdHm5uBaLd3ulRpBVXvBxec_0zWIIrPJZUwqwJigyiQhvcnFGgmld7quoqkXNl_ZunGZzUg8bp3cNAo3tW4IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فکت؛ رافینیا دیاز با گلزنی مقابل فاینورد تبدیل به اولین بازیکن تاریخ بارسلونا شد که در پنج بازی اول فصل برای این تیم گلزنی میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/29399" target="_blank">📅 23:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29398">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzByDNX08GR6VUD19GD2ZoJdl9aD0T8Xa9jL0EIwanU2mtVjmQxzdnvTE2x0PpJkWI6fqmOy-JXpHptbAznUmpAgL4okNI519ZorrRQ0sX_JNDxgLIAWsoGkdswtyK9zIUi_jBabpkMvCO24LBgJEoVxux4khYmfiuALhcP0oWOI3HiLlmkKYoIISQf6dRbpKWslIUPDuQoBEyAjijZZvTnSIA3dQFF0T1tbAyiCU2Ogb8HmIbKvCLOm6lWJtuFKwNGGTUloPWygdwtU2uLhPjlg89TYYZBHN9QSxrA0R3aL_Bke3JbCzDGWnzKUg-It-TZbNtn7dM8qxx7fh3gBaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ لژیونرهای ایرانی حاضر در اروپا:
‼️
علی‌رضا جهانبخش: اکسلسیور هلند؛ الهیار صیاد منش و علی قلی‌زاده: لخ پوزنان لهستان؛ محمدجواد حسین‌نژاد: ریوه آوه پرتغال؛ میلاد محمدی: ویتبسک بلاروس: نادر محمدی: دسته دو فوتبال روسیه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29398" target="_blank">📅 23:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29397">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkL-LBnwi_5428GHaeVRBso24bfg1lWFcR5CtgkyVPF3hcDjJ4lA_FE98MPYASgbQBFi7lG4QUPPmzGmtmrxShv9xD7aw_YrjjzzVOw00hBNRrYtM2uFcbFLzWE-6y6947fuTW7dsSs5csI0U6xO0UnCmUIJJgzE0NjgR3GZtm75Vx9vqU1pWxHu9-0HEWSP9gWBAxyfXeddtFL1RXwIrsXMd8PS1MZJ6Svh-5XnJ-bMEE6RXNiUjPLkjwUkzJvVKSEOolFok6AjBSYKgIu3AcozC9laMrz8vXCmhEmfDZQxUkUxmIJ8Lqm6_OZGtHxHV2cMl_hd24GOYJMicOVEhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
نتایج درخشان و خیره کننده بارسلونا مدل هانسی فلیک در این فصل: 5 مسابقه، 5 پیروزی، 22 گل زده، 5 گل خورده، میانگین نمره 9.3 از فوتموب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/29397" target="_blank">📅 22:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29396">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MiI0bhDvs2oUbNYSJ99OLvCdEqwqQC3lIRdyHGH79s6G-TzTxHHkp1NVJTKJf3xXQHPb6mWqVEmnD5VjfDoBZ7g6o6hgvh_BmoJefVNRnSK61gJfTw54wk57v-yIncPCKeXalHjCCvWTcYSIwS3tW9w8TVXj6eKsg-Lo8G7DCiau4kpK1VvcpFrCJYxxN7dGzJ91V1V05aV1QUjHEoSVD-mz8CzgP4lQSVwLZZ8xpVshe5fUPoEEpFbbyZ_r7RYZAcTaCnvEvaV8SsIjMJS5ZB0ilmHZ_GSGwzerZquwtiCYazPpgVKzJOiybniQUC6nAwOBsRLDsq2SRwfhE6ZvAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🇪🇸
در هفته اول چمپونزلیگ؛ شاگردان هانسی فلیک درنیوکمپ آتش‌بازی راه انداختن و با نتیجه پر گل 5 بر 1 نماینده هلند رو شکست داد. 22 گل زده در 5 مسابقه؛ عملکرد استثتایی بارسای فلیک!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/29396" target="_blank">📅 22:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29395">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2m0gPFCbZuWDMDb1gsdx8D2bWZ6FfX3uCd2AeZvukHC3egxcT9-jTVNbCQhljZgGmkmY1saT7zTYB8eyaX47DizvYQk8qb8PxD2UJjz_dpU2o3lccmG5AylDBMSFQgCy-P0P_H1aB6RgMiQ_AdrIfFtXp4Z7VKtiGtMWelnl4GND7SvpAce1a7vw7jBihC0TLgT2dnwJPt3Jz3SxWzKQpbx2ptuzrF5QeKEk5QPtuAYlpCiljQrHGcC97uLZLAritvl8XwbaQKLIBLHPuPlFOziMJBwYlluxrGM6SlgnvI9yA-5bOjN2UnuEPZarSuSGt9weSM8pIhnZb0d5ueTrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
کاشته تماشایی لامین یامال ستاره 19 ساله بارسا در بازی امشب آبی اناری‌ها مقابل فاینورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/29395" target="_blank">📅 22:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29394">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adadb2bd3e.mp4?token=PCwj0IcRyr-kq5Gz65zx5KxVwRt3htxiwvLyFB1VdOsvrUen_Bs5dhtoAz9CyNlgRZ1dWgwr-tuEWRP8sF3DMJzwUEgTvP0DxaQCG86GJnS2G9TD5Xnfw3cY0ZoakQlhvoL4q5wz8eCWyyXfCyaYAGzzZHlm3OKZVbunh-tuPKnbS1vnJ5JHFSxZcb_ALqPLen0XuCOJJIkf_oyZTP9Sqxny352ZLou-nhZ3qcm74OrCQjYtnctAmVCICSk2UrE9WMS1oxcQNsyXZAmz93rnwGKsx1nK-VrAPfKQqi88f_n8WreaDU3h-HVndceJu8ScSmXEOrM6SJ6EcBJTVEhV1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adadb2bd3e.mp4?token=PCwj0IcRyr-kq5Gz65zx5KxVwRt3htxiwvLyFB1VdOsvrUen_Bs5dhtoAz9CyNlgRZ1dWgwr-tuEWRP8sF3DMJzwUEgTvP0DxaQCG86GJnS2G9TD5Xnfw3cY0ZoakQlhvoL4q5wz8eCWyyXfCyaYAGzzZHlm3OKZVbunh-tuPKnbS1vnJ5JHFSxZcb_ALqPLen0XuCOJJIkf_oyZTP9Sqxny352ZLou-nhZ3qcm74OrCQjYtnctAmVCICSk2UrE9WMS1oxcQNsyXZAmz93rnwGKsx1nK-VrAPfKQqi88f_n8WreaDU3h-HVndceJu8ScSmXEOrM6SJ6EcBJTVEhV1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
مقایسه‌عملکردکریس‌رونالدو
🆚
لیونل مسی به مناسبت قرارگرفتن لیونل مسی در لیست 30 نفر کاندیدای توپ طلا و غیبت عجیب کریس رونالدو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29394" target="_blank">📅 21:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29393">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135ac654e4.mp4?token=C-PgiMfiF8CLndr_Ctjz13huFdQVwl01ckZsRSyy2FYdVL-X6YA9IFDY-KjhUyQucjiKQf-X_o8aOarwsGZjiQ2oP05OmdW7VjrpYTeLDsD1JVaNRtt0ziswfKyTvNLtwzDHc0-5lrlhILwoSQUSoYpEQMfBTr0ix34W4EWJEY3BomwqraqIYObFk8Nrjp8rbrOZx6O61fMS6SPZlDJy2Q1B4DHjQRlNDDaYV9MOh_juU0LImdeLDPXHyPteVPiudTD0Eqf9g6X9n6R_dQr8lEyGc25334JFhjydvMH8J3m1oAdIDv-xjzXf9DLKb-YgEt4bdmegXzZy0l0iqploRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135ac654e4.mp4?token=C-PgiMfiF8CLndr_Ctjz13huFdQVwl01ckZsRSyy2FYdVL-X6YA9IFDY-KjhUyQucjiKQf-X_o8aOarwsGZjiQ2oP05OmdW7VjrpYTeLDsD1JVaNRtt0ziswfKyTvNLtwzDHc0-5lrlhILwoSQUSoYpEQMfBTr0ix34W4EWJEY3BomwqraqIYObFk8Nrjp8rbrOZx6O61fMS6SPZlDJy2Q1B4DHjQRlNDDaYV9MOh_juU0LImdeLDPXHyPteVPiudTD0Eqf9g6X9n6R_dQr8lEyGc25334JFhjydvMH8J3m1oAdIDv-xjzXf9DLKb-YgEt4bdmegXzZy0l0iqploRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
سوپرگل‌استثنایی کریم‌آدیمی ستاره 23 ساله تازه وارد بارسلونا در بازی امشب این تیم مقابل فاینورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29393" target="_blank">📅 21:56 · 18 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
