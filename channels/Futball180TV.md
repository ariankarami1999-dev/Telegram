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
<img src="https://cdn5.telesco.pe/file/s8SpB_CmshFs-nxdSTGTlUtibTgEGp6YFOcJpmP1o4qdKfImRNTy7T3IgbK1GHtfZxil2oCx34oWUnNhUsJzYD-SxEMdyTmh2Vjqseoy29tjsXtDRMA3aYjQiAXa6ctKkEn5jaKUThwZQ0lzYlZktxVyZoGOCaQ49NJq4fSrRfv8HIXtDZxvkmoRdtWmw0c4iHYjFZDCRcar0IVwZAc3Ak_llMIk6gMTKk3UR4c5KWFug2S8yUFO5-eiBzawdDNVtWhDusO27vReKX_ztbfhEyHzeoaWLTUk4DyopGmjds5SQoSCgKUOn1FNI4GDWryX9ixllNN3aH2oZVV9iIomDA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 415K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 20:20:35</div>
<hr>

<div class="tg-post" id="msg-106387">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBzX7PRKR61RM84IXQbgLoVowcWefXA-eAt5wSfGJqGS4HtV3szZs-a7vVXSEMOrLKQH3MdBKQIAdICgOTlLHqCXfUbrsl1IcBp3rYOC1eICg2Nj-Tajb7tfeI__auAPWtxXaAtgHLo_EIfNTeGMUUQwK_msilQLkA8VKlHfKc4hHv4qWcpUjBU0U4uH1rhDAtsMzYng-YtQksiH7-hNlXpZomcQ4yAkTAHu-ZUZkd8omf2ngHYlpETSFwKgUsaHlc_A_hyMfM2SzGahUariwP37DiniPOu6_htoE1TG1ymPBS0BJ8sMOomg-8fgRbbo2kKj3RX729Srv6EZR7VxWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇪🇸
پایان بازی با برتری چهار بر دو بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/Futball180TV/106387" target="_blank">📅 19:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106386">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بارسا چهارمی رو زد</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/Futball180TV/106386" target="_blank">📅 19:48 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106385">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ژاوی اسپارت قبل تعویض شدنش ریددددد</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/Futball180TV/106385" target="_blank">📅 19:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106384">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">بارسااااا خورددددد</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/Futball180TV/106384" target="_blank">📅 19:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106383">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گلگلگگلگغگغ</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/Futball180TV/106383" target="_blank">📅 19:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106382">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/868a077e6a.mp4?token=DyqpO5rdhkPR6p1imRjbT5iTbqV_ykHhZ4cIiuvM9c615aXVaWCza2cjKaJg-MPmDSHYA7jPlRiBLDxhcrjt2JjDEzl6iL-a-8cm8sJfkZAospQUKYi2Een5bNLPXXb3l7CtrV9qdUzaRC4SNhNRTyrCFr_VnOR3JCjROVg0O5tcjyHqcfaXeVVW-P1s-DzFJZhltN5G8vM2KdloL5zwB-KSbckg3WBThucdD4qdTlpE0a1gsmbvgwOOniNxA63iSWH4TwUbTa1zwpaCTJg1rYV0bOQKIu5JK_RGQNhkoTLZAzPY7NzrnZcWlkYKUIDrRgHOyZdUE0Mxi8LlkG4lsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/868a077e6a.mp4?token=DyqpO5rdhkPR6p1imRjbT5iTbqV_ykHhZ4cIiuvM9c615aXVaWCza2cjKaJg-MPmDSHYA7jPlRiBLDxhcrjt2JjDEzl6iL-a-8cm8sJfkZAospQUKYi2Een5bNLPXXb3l7CtrV9qdUzaRC4SNhNRTyrCFr_VnOR3JCjROVg0O5tcjyHqcfaXeVVW-P1s-DzFJZhltN5G8vM2KdloL5zwB-KSbckg3WBThucdD4qdTlpE0a1gsmbvgwOOniNxA63iSWH4TwUbTa1zwpaCTJg1rYV0bOQKIu5JK_RGQNhkoTLZAzPY7NzrnZcWlkYKUIDrRgHOyZdUE0Mxi8LlkG4lsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🟥
صحنه اخراج مستقیم فیل‌فودن مقابل یونایتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/Futball180TV/106382" target="_blank">📅 19:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106381">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILSbm3ZehFUQ3xNJJpSdCN4f7igfW82FXVtTlweVSzxH3DzMx1DrKDtvDZjlCIxEwX-oESacrkGJkpR4_sRF4oHKu8_OaSo_vq9ys26JVoIataxQOj9j1JaS4ejQ0WObDqrUuhHRmgVEjKO8XiSVEy0InEogPme20SQQw-YlbBkYIYyDeHXpm4XLmSBWQJWm7WNZU9R3gwlDiAYRIsk1sxTyR_HHVR6dhtqTqY1n0ggJqOwsdTt8KwBVmLIzuosWoM-4qYznFAIAHGWjBekewJrQTqL-Z41JqEs3rgeODT90smhl73uc7xXNTwgK1f6ohXNDo66Veagk7t2-dLYqrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇮🇷
🇶🇦
لباس استقلال و السد در بازی فرداشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/Futball180TV/106381" target="_blank">📅 19:05 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106380">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8f3bfffa8e.mp4?token=Q3dRQbVLbKaS6INwmzm5_2D4uyXQ8r39SxQwTzymE-L7dV5Yr-RcQ7AmZ_7HJNSspTOOpEcohOkS4Izc0RhySnpcMfmkEwtod_zqcVJ22JlRlraUSZIF5ahyQiQXshqiJ28gtZJ68Uwfp5WKAfRMzzjLnscQYydYxKMb1rdzpr_wvCn7Ca2-SbkojOUIdjdoUMBS1B1fPWgMUtMn27uNHxTbRcFXYJqgc2p70KdD3K65pmRq0fBfkTeR1qqHDkAZNwW_Qx1CCwRjYM_aJlQM8Q3PrId7FQfFfDoI_sioSCyD10WIxdij0e3sKQsflfInXCx-aqsvuwKol8dNMZ2erDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8f3bfffa8e.mp4?token=Q3dRQbVLbKaS6INwmzm5_2D4uyXQ8r39SxQwTzymE-L7dV5Yr-RcQ7AmZ_7HJNSspTOOpEcohOkS4Izc0RhySnpcMfmkEwtod_zqcVJ22JlRlraUSZIF5ahyQiQXshqiJ28gtZJ68Uwfp5WKAfRMzzjLnscQYydYxKMb1rdzpr_wvCn7Ca2-SbkojOUIdjdoUMBS1B1fPWgMUtMn27uNHxTbRcFXYJqgc2p70KdD3K65pmRq0fBfkTeR1qqHDkAZNwW_Qx1CCwRjYM_aJlQM8Q3PrId7FQfFfDoI_sioSCyD10WIxdij0e3sKQsflfInXCx-aqsvuwKol8dNMZ2erDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دبل لامین‌یامال و گل سوم بارسا به لوانته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/Futball180TV/106380" target="_blank">📅 19:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106379">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">لامین‌یامال دبللللللل کرددددد</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/Futball180TV/106379" target="_blank">📅 19:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106378">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">گلگلگگلگلگلگلگگلگلگلگاگاگ زددددد</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/Futball180TV/106378" target="_blank">📅 19:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106377">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پنالتی برای بارسااااا</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/Futball180TV/106377" target="_blank">📅 18:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106376">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
‼️
⚠️
🇮🇷
صحبت های تند رسول برگی عضو شورای شهر تبریز درباره اشتباهات داوری به ضرر تراکتور: روزی که مهدی‌تاج برود می‌گوییم شاه رفت! چون کاری که فدراسیون نشین ها علیه ترکا میکنن شاه هم همچین غلطی نکرده بود
!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/Futball180TV/106376" target="_blank">📅 18:57 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106375">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gufzmMNjA8gC7hp-6qerpn1EsajG2wziE4wryVG1K2A1g4WnPpXxyZ-RZZT5YIoY2nZxhWJC4nm867XQeU3PRav0Pgl9uaFw0U0k5gtbKueshkmrdeu-o2AfFfmGHASwQYNSjxC8_dwpfm7x8MKqP_SkSMsh_bfYJXnn9MNTGh7BZ72Te7vg7psMY6ECEuqeMigdnIAz_WMU2eV8Aoq-HfKH_sD1mfMI_3ftxAoP-XTpoFPsWTw3yzueG7vhn_AjfZpsrMZavdC2lnM6eachbEtmYXxP08uCbWd4jszDzmc85wvt8aCVBFkluEYk6HBdoRj-lsPGE4H8hL2h1wW0NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
⚠️
بختیاری نویسنده و کارشناس اقتصادی: چند سال قبل من رو به سمینار دعوت میکردم تا اقتصاد رو با انیمیشن به رئیسی یاد بدم؛ گفتند ۳ دقیقه بیشتر نشه چون ذهنش می‌پره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/Futball180TV/106375" target="_blank">📅 18:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106374">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxk6eNjZJyfw4VUkww2sCnBycF45jrjwWw6yGD6OufD3RaJGF1tQr0i1zNqT9J0xN-goPlR6U4a6s1Sxbcv83_YAPfnRvQWiFK_QQjsJXxRqJsto2dc9O-VuBfQ2nOToolRDrCcZ0GdcRmspSAL5esX_qkArHya1Vo5nRdWOy_ctWYrAe-Q_g3waSpxY2faSFQ2T92ddQC0XmaiKM6vh3o1aHn5qQV-PRwPWF_zq4P1nzFmk3E9BGPDVM5g7BEZ82lEUFrUMPlSXaMeB6W-PN2qDt35g6584k3vMmApbz4wseqrfPgDvxqR3HylYN3tZw1SEvqE1O8oM_AKzipmPPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
💥
لامین یامال در 4 بازی اخیر بارسلونا:
⚽️
⚽️
مقابل رایو وایکانو
⚽️
⚽️
مقابل والنسیا
⚽️
🅰️
🅰️
مقابل فاینورد
⚽️
مقابل لوانته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/Futball180TV/106374" target="_blank">📅 18:37 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106373">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cs5VMhFk7wbb-OiA2zd6QF3eutFkqARhxERV9v7Gdtbj849Za1gZmFoz1SMCWmorrwOmIVz2LaWdrwQ-cET0CL2ffjPSMX0OxxM0YRqOPMzb-ofZvYwEYBF4q_iI9cHlmXAklwhJI87y0J25mp-SE6oOT4Yj5SJsFFWlYYiiZi3FgZXPjPwKchIyhiNU0IN9kXmxDj-_L5yikti3XLcQufv3Hj9UUhIwdUbyA4dTlCRP41hptjO2vmv8GygjbKFNNZ2dWBGiWf-lax7yzKU-4qax-WwSRlR5wfI0BcLsJELc3Bg_ufVjukuazbkIYd1yixFSfZRR52FMOt1u8pPFDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پرسپولیس در دیداری تدارکاتی با ۴ گل تیم شهید قندی یزد را شکست داد
⚽️
مهدی تیکدری (۲۷)، یاسین سلمانی (۵۹ پنالتی)، ابوالفضل زارعی (۷۰) و مجید عیدی (۸۵)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/Futball180TV/106373" target="_blank">📅 18:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106372">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106372" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/Futball180TV/106372" target="_blank">📅 18:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106371">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMUUsufuvWen_OTd-zIll43O7sS2NqZPKhLyXsEEagGyEfpCgr5-0VwwRiqw9895ZFokzv69ckLZq03h7h-0qW37Ad3BiR9V6RHzih7haCaZCOCvh6Ku_bmEz6ax9LmjKeIioXv0I_9O1fGgCHmoOg1OZ4Plmp8GvUZb9ddEsuWzPNSIoUc3awIz8mYpgBudt10oQqxDPhvzSRYrY5ilTDZ7mquNPQaSpP1iXS15MqD5miumpmITU5IPlvLNqfSWR65_QxkPZCGIxBcSETx9-5nDcnHiQ41B-q9_r8h1vlFzfCnNJRgXbDTOzbtNSOOpT6j1gZjaaJidDlxOdvll2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/Futball180TV/106371" target="_blank">📅 18:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106370">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">رافینیا دبل پاس‌گل
😐
🔥
😐
🔥
😐
🔥</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/Futball180TV/106370" target="_blank">📅 18:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106369">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">لامین‌یامال زدددددد</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/Futball180TV/106369" target="_blank">📅 18:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106368">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">گلگلگلگگلگلگلگل دوممممممم</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/Futball180TV/106368" target="_blank">📅 18:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106367">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2SFBqdnM-ga0pBM2mmLT9Rk9d2Z5-UwulUmA7LyGc6f4zkiF3XFt_aNBSuUMww-vSzZCkKi4fABGvQHRgt1sSPkup1nur8PUQNrm8HMb8_7lFO7FoPBvJgXtpcyuhKzCm_0s3yq2AiV4hWJI9SBmrYyQ-8GXilJz8W972oSSCercuztRcm7roHNBimze3YDdO9Ry3yXHQLQTJrg3euzhW5JldgfauI4RXRy0kN-oCvHYIosRKvNSrepvB0TsmMRblVg7OnOIwd4plj_eftbF4dSgiZgTkbPnjRt8eYIT3M01bYlRuGcnv86qDhqqG4WL9dJK5Byi2VVzNHCxGE4KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
ترکیب بایرن‌مقابل الورسبرگ
/ ساعت 19:00
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/Futball180TV/106367" target="_blank">📅 18:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106366">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d40cb71cac.mp4?token=hcWX2aEyurIu2T7t4E80u9bO_HCMXb2nXGgilPZpWw_mGcwTehYL36qJAYyUVhP63FP92OMfVPZLCVsxtrYzr_avgiVIMZfCDIFGc_OuxQAu3FONEmV9q4zaX8s8SF85I_a-KuhzhPXq-V9NnEbPC9DjxU5wOeBu9c6KuAC1iDdJ_h4wm33_HOHUP12GtKPw8p6vk9A_FxzhXnFiEodYWRbkMoEHz4k1Cui8pn3abjsFUnZ0nopQTXXmwDFSpiWuGqINVy4rPHlNpX_f5Ihp2Ga8pzzTOKae-Tql27wrydBiwRjLBgjv2eykbt2xB5wgYoOH_e_wrglN4Ml5ValYl2mA7mLTQSZrG1nFyCZSDuen6FpnKqb_ikQ9xclcWEZLfSwHfCQjct9iJKn9GFbmEJxinajDP0XkiGIZhT_5MqnCBL7xyrFUfx7rMvylxNyzgSDTPgyw74MyU0_0TPZyMn9t5kVB3V8tFZiATiWeQEgCg2o79Cn5J4_JN604vcCri5BpSGzoTyGbCOamp5M14zo4FfpMqiD0gmCyO1AUXB8wVVn-zbiwklOrfFaiHFN4tp2ddXBhFeUrgFPuMSd6YN2DSdeoGjwfgAm0TMV0at55Cbrd9Fi6uRHXLjWuKPFs9h6e4TJlcTrPxvUd4DaEff2YC99uQq9M66j2b54eDLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d40cb71cac.mp4?token=hcWX2aEyurIu2T7t4E80u9bO_HCMXb2nXGgilPZpWw_mGcwTehYL36qJAYyUVhP63FP92OMfVPZLCVsxtrYzr_avgiVIMZfCDIFGc_OuxQAu3FONEmV9q4zaX8s8SF85I_a-KuhzhPXq-V9NnEbPC9DjxU5wOeBu9c6KuAC1iDdJ_h4wm33_HOHUP12GtKPw8p6vk9A_FxzhXnFiEodYWRbkMoEHz4k1Cui8pn3abjsFUnZ0nopQTXXmwDFSpiWuGqINVy4rPHlNpX_f5Ihp2Ga8pzzTOKae-Tql27wrydBiwRjLBgjv2eykbt2xB5wgYoOH_e_wrglN4Ml5ValYl2mA7mLTQSZrG1nFyCZSDuen6FpnKqb_ikQ9xclcWEZLfSwHfCQjct9iJKn9GFbmEJxinajDP0XkiGIZhT_5MqnCBL7xyrFUfx7rMvylxNyzgSDTPgyw74MyU0_0TPZyMn9t5kVB3V8tFZiATiWeQEgCg2o79Cn5J4_JN604vcCri5BpSGzoTyGbCOamp5M14zo4FfpMqiD0gmCyO1AUXB8wVVn-zbiwklOrfFaiHFN4tp2ddXBhFeUrgFPuMSd6YN2DSdeoGjwfgAm0TMV0at55Cbrd9Fi6uRHXLjWuKPFs9h6e4TJlcTrPxvUd4DaEff2YC99uQq9M66j2b54eDLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌اول‌بارسلونا به لوانته توسط ژاوی اسپارت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/Futball180TV/106366" target="_blank">📅 17:55 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106365">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دقیقه ۵ ژاوی اسپارت زدددددد
😐
🔥</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/Futball180TV/106365" target="_blank">📅 17:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106364">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بارسا دوباره اوایل بازی گل زد
😐
😐
😐</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/Futball180TV/106364" target="_blank">📅 17:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106363">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">گلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/Futball180TV/106363" target="_blank">📅 17:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106361">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s1J0x3uhnioGpP7MvSe-nDlXvFOcRaedcw4PHVm9f_im9lNxaRuGHFmziqNd9d_kxXFYmwwFdBy0HlEO9N2ak0cv-Gch54CW50xOObXhkQnuNHTrt7XKtLuk69WxIqxoKY-qiXHWeQNNraWi9cey49im8IDPmZlMi1Lw31CyfOK8TUoSpguiHUCtzDFad0LnAPBSeRJg9Zz5QVpWAxUElSAewMq45m7F2mfqltFmEYisPO0Z_Qy7HOmE8EfrtrrrK52N3e0SfukZQMxAUe8IUIYBedhC4tKmlchTIkXkkk4fnW3jKegzReMu6JP-QCdvtbER2-IfIbcY4RExeDDTMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y6NWmMC7Zm4QLoa36VWDE-Me0w2KCrDBCcXdVp9IdcBCrk3pUfyJS9ebMygXV4H5qzqFtQhYYXI52b-xaGDVIJAN88rwr8PVjm_eLEhLIM4_9-kQjGO4_hASNr92VWXT4i2icmVaEbQVZrO29c9nq_M01GW6VKtKtaLXdKUeABj8PJmsDmuttO8VAilBT8IS3lfnu1WLCs9MTeF9pdXn7oWnUhXBPtO4V1h7FucKX0YCp9aNS-JbruID9kp4h0derMs7kSd9rR3gc1ZUY7MtJgECR0TJePifp20_EmlgA898yu2vwoDrGqpUjQgpggEuTpHZDbZXQ8U4YyjKgs6zRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌چهارم پریمیرلیگ؛ ترکیب دو تیم منچستریونایتد و سیتی
⏰
ساعت ۱۹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/Futball180TV/106361" target="_blank">📅 17:47 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106360">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a36fb349d.mp4?token=i1KdAfcmfUgVC7VdJ3PYjdTHYc9EcZZFtnEQA-9B3Dq6peT2rDNYMJ7rVgWn85fRzmRXseMasxS4z9jhVVfRlvjLTlCyEhUZedvU5hu5WrKEuIaZ6d0Yx8fr8W_HrWgrndgGmJM5l_VbbvJQyODDRIKKutb5nefsPb9FKfSYlle0VJpd-3dSJBOcVWUOI0Br8QAgCGmoIcZ0RULgYFf0d0xmwwjjyZ_8H4YYtmcqX25y-vD0S3hrhyxJeaYUuvV2zkOXumSR2L282G02A7Yj69Dop8ZiZEu0u185hHRtb8gZ0ecAV6xGPoDvY5YRUXqCCAKKoqWOOWcrGJFQWcwsjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a36fb349d.mp4?token=i1KdAfcmfUgVC7VdJ3PYjdTHYc9EcZZFtnEQA-9B3Dq6peT2rDNYMJ7rVgWn85fRzmRXseMasxS4z9jhVVfRlvjLTlCyEhUZedvU5hu5WrKEuIaZ6d0Yx8fr8W_HrWgrndgGmJM5l_VbbvJQyODDRIKKutb5nefsPb9FKfSYlle0VJpd-3dSJBOcVWUOI0Br8QAgCGmoIcZ0RULgYFf0d0xmwwjjyZ_8H4YYtmcqX25y-vD0S3hrhyxJeaYUuvV2zkOXumSR2L282G02A7Yj69Dop8ZiZEu0u185hHRtb8gZ0ecAV6xGPoDvY5YRUXqCCAKKoqWOOWcrGJFQWcwsjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⭕️
⭕️
رادان: بیرانوند شامل قانون سرباز قهرمان نمی شود
دروازه بان تراکتور از اول مهر سرباز است و باید یکی از تیم های ملوان یا فجرسپاسی را برای بازی انتخاب کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/Futball180TV/106360" target="_blank">📅 17:44 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106359">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/US5wH_DsC8Rs2TJHlwvEUJiMW-o8MZLmqTCFUJwxHeWUulx693w19oa-kA07K76A7gvWW9GRJuSfsZEtUugBIhT-3t8HhJGT8hWJmUVsAXkRb1n1vxoByG4Z74ZJc6NuwK1itvh4VURFuhrNYenU2cOeIkFrbDItg7QAcCioew1BdXy2PnxsDr3ABdkUbDV__rWbRXwwqvA1SKtBcWtqlSZNIsB0s5D70QStdmeBis01K_HOI_gHERewyPVgECGELVYO-ZiiMjCjhE1nYfrf2vlOoTxKIpxLNqDb5LovhTa5wnAW0mtyVHNYoOEkPpVyfqGsdKXtfaNcIXQUAMhvdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه گلزنی ستاره‌های جدید بارسا و رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/Futball180TV/106359" target="_blank">📅 17:20 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106358">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEBvG4oUflFjre75ztYUPiaJd61A2yS_Ffz6vln7K1zPm5-Bvv6ZooIYktA4_wqeSCeBLlfpCdJFTsRM9kArMHglq0K12rSC5bzQI_J9M26oT9i_Nt23VrQhtK5ErWv1jAgWkqmAzqmNDoSvLOz4qwLyuFCXluLxF-n9NWF-7A4-F3SXvXeNmlO45vt1E0zrG1eI5QBbZ_o2G4u_SGQCt6Nr5Q_Hy20FiWJrXn5FDManf6JYd7xozgEo19DJlAm1VohJm-JEzfrhKQ4RAxypg-AeDiySMQJK1uppQDP-jfO_jxXzu0u1vJdkO3wD8kO-rmpYuXgy_62woFQ6hSUhyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇪🇸
🇪🇸
شماتیک‌ترکیب بارسلونا مقابل لوانته
⏰
ساعت ۱۷:۴۵ شبکه‌سه سیما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/106358" target="_blank">📅 16:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106357">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53d01737ee.mp4?token=ZBL8_IcMxkL-Li6WxA8XECsfdan6MW9pNn16BziHXZebxMPJRkS80PefNd2JnpEm2arvnhm1PeNe82aHA0BtGlu9usi-6OsWGYXAIzuODN53Tl0AFSnjTEAyq89NZrOA0EP-6XWyGaHNwwG5nIpCpR1xl8Dk9ck0_LZwS2xNqxdhg5eI9dGYXgaxsfrU6kRTmwTbqqMl2r_0GKhElfRAGiODtRPjCQ8gawmBdC3JTXio4EGABjq1SbCsf4TC1mreqb3RpGC68r-e1hb-2BqMBmDiYTWpoim2MZqMF-GHe3_XqZqEnyAQvcEuI7BqiN54Tq_Byum4-z_OqiJ42QtQ8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53d01737ee.mp4?token=ZBL8_IcMxkL-Li6WxA8XECsfdan6MW9pNn16BziHXZebxMPJRkS80PefNd2JnpEm2arvnhm1PeNe82aHA0BtGlu9usi-6OsWGYXAIzuODN53Tl0AFSnjTEAyq89NZrOA0EP-6XWyGaHNwwG5nIpCpR1xl8Dk9ck0_LZwS2xNqxdhg5eI9dGYXgaxsfrU6kRTmwTbqqMl2r_0GKhElfRAGiODtRPjCQ8gawmBdC3JTXio4EGABjq1SbCsf4TC1mreqb3RpGC68r-e1hb-2BqMBmDiYTWpoim2MZqMF-GHe3_XqZqEnyAQvcEuI7BqiN54Tq_Byum4-z_OqiJ42QtQ8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🟣
با وجود محرومیت در لیگ‌برتر، خداداد عزیزی به درخواست زنوزی قرار است در بازی‌های آسیایی سرپرست تراکتور بماند و کنار زمین مشغول چانه‌زنی با داوران باشد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/106357" target="_blank">📅 16:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106356">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l12wq_pJ-fIBGn6FdqpK-rVirHV0KxIgn_R5GS4NgncM9VERTUiHwlADekYQ0J1DKtQCy33dfm5UUqErEKPq2K-uaqJnwmZlm2wfFEVjzimmeyETMLdxvy8DpMFcfbwSQ2ugOPjQCNUhC-UNi1k_dWMT_MHjIOkX7KXj3ODQdkEw2VTuumvCtphCJoKK-dlceRU4BfFPnKNJ_eJ7VYN6EMDaUQnu8D_YFhpDdRraIi4oJiBq6rA6jnf9DTJMd2Y17Z4g5i9ch-2y8w95oy5wrqJe9_Qcz47aEJYFT0c8t3hlJrKpKOJXfr8x5J_YSjFHXkudTfzWAGHyu5ZtTAA4vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇶🇦
السد قطر پس از هجوم هواداران پرسپولیس کامنت‌های پیجش رو بست تا درباره یاسر‌آسانی مطلبی کامنت نشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/106356" target="_blank">📅 15:57 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106355">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfgMUW4bzw3Dk9eEugH7Yr4-nVd0Ia_SRsn7YfwSctoxd-7lZMCpb_-LAyjzU9kKyuVP69YeG4hKFxj05XlH4hk7A5GCN1PXF3BDVffoEILnCpRZ25W1Bb5cGCU7YmkB1MQh4romK2vQoq2oChLn6gczeiO-CRgIVDUCvleiO0jMw1cqkix05PUNW-7arZlQt1OwzMfm7D0pMdEgqiSjsSeZvZYCrQEFTaO82-SlC7a0HQMpfMNo3Yw7jgEQzoJ6b0oMutTxZV7RswnL5wqkZ5tsT3FU1LmQCmEbGMSz03VnMGnBY0t7GzlTLypG-RrWcr-Ojad9OMW0dFSQw6samQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
طبق معمول ده بازی گذشته، مقابل والیبال ژاپن شکست خوردیم و سهمیه مستقیم المپیک به این کشور رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/106355" target="_blank">📅 15:51 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106354">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
‼️
🇮🇷
افشاگری داماد سابق علی‌پروین بعد از 22 سال؛ آرش فرزین: رهبری فرد و باندش، سرمربی پرسپولیس را کله پا کردند!
بیست و دو سال از روزی که آرش فرزین حرف های راینر زوبل آلمانی را ناقص ترجمه کرد، میگذرد و یعد از این همه مدت، حالا داماد سابق پروین، پشت پرده آن روز را افشا می کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/106354" target="_blank">📅 15:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106353">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1b2c19a26.mp4?token=Khr5Ywtc3xO0XlhiaMlbrbeUOwzgoq8-1RlJqGk9pkltmW7htWVZQQLWXq9jJvbGMCQz26Xl_kD-xRY7Qxrb0cx8D77hyijfBi164smiicNht4hBJEFCHDMaErzob0Ez7E41CA4FLms9PVL1AFdydarZEptn7V0Q4e984B63_2rdIIu1DDAWpk3eOMIuw1hFCQZm0wNDasSCw-v5rddKZyTUGoAq9uY1W003PidQIkeBwRcOCFRrDJljtpikYssCllrJZYBAztHV7HcmzLzKtInyErY0ZBPAORQzy9dQT0shloUVhv8E8hOd0Mvk0AAs-C8ItMj6UUSz81_F75NvQ2Xlwjkno3ViPoskn2hFVrirR2E_7F4gpQ98paFLY88mfG0TqMV6yx0Xs7cDv48bVIyAeLTMnWPal-Z3W9YrcOpnHbZk2wicg4vRPigw_zxsqySsp3FQ5m726N1ir6xLoAOZP38X-Gq068idUxsakZXZ4dgi5poyQnCFO8zba_sxez9hvVKr_poY2JG0h_hJrds94bQd4d2DTnuAHVwo1R5DJK0HVsHK3lcRN88DbfLOsKyVLyNMpkxqCNg6hmLkdYEY9y8kPRoj9lqaIfHXMju2ekBcIWhh9TgJy_9Ro8qKzsWri3F9hQ2k3Pm8EmTSjgZxZlsEv6ILiW8H13jGc_o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1b2c19a26.mp4?token=Khr5Ywtc3xO0XlhiaMlbrbeUOwzgoq8-1RlJqGk9pkltmW7htWVZQQLWXq9jJvbGMCQz26Xl_kD-xRY7Qxrb0cx8D77hyijfBi164smiicNht4hBJEFCHDMaErzob0Ez7E41CA4FLms9PVL1AFdydarZEptn7V0Q4e984B63_2rdIIu1DDAWpk3eOMIuw1hFCQZm0wNDasSCw-v5rddKZyTUGoAq9uY1W003PidQIkeBwRcOCFRrDJljtpikYssCllrJZYBAztHV7HcmzLzKtInyErY0ZBPAORQzy9dQT0shloUVhv8E8hOd0Mvk0AAs-C8ItMj6UUSz81_F75NvQ2Xlwjkno3ViPoskn2hFVrirR2E_7F4gpQ98paFLY88mfG0TqMV6yx0Xs7cDv48bVIyAeLTMnWPal-Z3W9YrcOpnHbZk2wicg4vRPigw_zxsqySsp3FQ5m726N1ir6xLoAOZP38X-Gq068idUxsakZXZ4dgi5poyQnCFO8zba_sxez9hvVKr_poY2JG0h_hJrds94bQd4d2DTnuAHVwo1R5DJK0HVsHK3lcRN88DbfLOsKyVLyNMpkxqCNg6hmLkdYEY9y8kPRoj9lqaIfHXMju2ekBcIWhh9TgJy_9Ro8qKzsWri3F9hQ2k3Pm8EmTSjgZxZlsEv6ILiW8H13jGc_o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
ویدیو وایرال‌شده از آغوش گرم دو بانوی ایرانی در جشنواره ونیز ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/106353" target="_blank">📅 15:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106352">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68ecf94960.mp4?token=LSOmYpl-1M_GJ4F_X1l84Ly-70zv7mLEKGqdnUZTbUA_2kLjnkpAoIfSf1cgnwDP1M3Nnplta7nvB0mQwR71QktDrGXLUXoq7VcjACk1qzUxIMG-LvrxIOFy5N6SAb6MNvHywbGLXs_P2RRtuF0F_Wv6cyXOC9a6cWc4BlEhs3poy5ZvXkWUYA2EqmXy92RIlpIFc-aFqCkwNAJ2jL2_-a4kgoLsE9lNaagYIFubtfyMFxUR1FeEXGOIzBMQqj7ChlcDyYn5rvSHQFNUX019WTwNebs6fxlXIqYWkINgw_IbAtxIoS8easFVWic7i5EvkG3N3ZTuRsYVtBQuspFrKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68ecf94960.mp4?token=LSOmYpl-1M_GJ4F_X1l84Ly-70zv7mLEKGqdnUZTbUA_2kLjnkpAoIfSf1cgnwDP1M3Nnplta7nvB0mQwR71QktDrGXLUXoq7VcjACk1qzUxIMG-LvrxIOFy5N6SAb6MNvHywbGLXs_P2RRtuF0F_Wv6cyXOC9a6cWc4BlEhs3poy5ZvXkWUYA2EqmXy92RIlpIFc-aFqCkwNAJ2jL2_-a4kgoLsE9lNaagYIFubtfyMFxUR1FeEXGOIzBMQqj7ChlcDyYn5rvSHQFNUX019WTwNebs6fxlXIqYWkINgw_IbAtxIoS8easFVWic7i5EvkG3N3ZTuRsYVtBQuspFrKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صحبت‌های شنیدنی سعید دقیقی درباره تفاوت سبک بازی اوستون اورونوف و تیوی‌بیفوما دو بازیکن پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/106352" target="_blank">📅 14:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106351">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzmxSoVL9-e-tio4E9OwPgzxr-hbYkThuCYbJgOp6fdFxxWdpHRK6-HdJKWG3SzIJQP81gKjr7WLXyAyqLtB14Eo86U-LkUz4GfLG_WUkKus7BMxcEHaHtKLQioxoQXLBmkv5iTa3h3Q5IC0bJZKf35k01KI4XSbJLt_P3ipKeS6Q7DpcM57gbLoatmAYS1pvR-sTS5xL9r4f3RWj4XTJCtKOB_P25FLY374CVC-ZnFyVWmQxEk_gYchc7OH4RBVP4UGdsctSyjVfjewCBD0UaQuMG4UA7g22MBILJ0MHCSxGtxJdsueeCfchsKDBxXvfWwrJzU3pylg-AtaI-VKlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
هوادارای التعاون دیشب برای اینکه برن روی مخ روبن نوس، بازیکن الهلال، اسم دیوگو ژوتا رو که دوست نزدیک نوس هم بود فریاد می‌زدن.
✔️
👏
نوس هم بعد از بازی درباره این کار مزخرف هوادارای التعاون فقط گفت «امیدوارم حداقل بعدش نرن نماز بخونن.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/106351" target="_blank">📅 14:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106350">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de2eae5e40.mp4?token=O4iZ-AnM68KcfXL4WalGWwzCu2MjvLIlFlgaKsLYwJXrUCl6fSme2V2ifAU25XMhslP-ABILVe3tjLrhivmhvMHB0Z7SsPxpMKI8pNrUUegBRIFOpFfu9BlpwyC1ZgeosfcFh26BpUbvGMwqakKS9Ls80PIYGF9lR1bLdAjCLlbFIBB6vBKc7L7SsYGZWsUPkXQQXv611bwc_pFOucf59cIx8COHp_G4HFcG6J7TQYiWq_83XvxaVidFLNdMWOy6wzfz3oFwrmRPLUGZUyGXqnl1hvKaAv5UGP4raFNC8pttbP0KMxGZN3AWQ8y35FqENDXpYCgXGzP0Lt1MuurCkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de2eae5e40.mp4?token=O4iZ-AnM68KcfXL4WalGWwzCu2MjvLIlFlgaKsLYwJXrUCl6fSme2V2ifAU25XMhslP-ABILVe3tjLrhivmhvMHB0Z7SsPxpMKI8pNrUUegBRIFOpFfu9BlpwyC1ZgeosfcFh26BpUbvGMwqakKS9Ls80PIYGF9lR1bLdAjCLlbFIBB6vBKc7L7SsYGZWsUPkXQQXv611bwc_pFOucf59cIx8COHp_G4HFcG6J7TQYiWq_83XvxaVidFLNdMWOy6wzfz3oFwrmRPLUGZUyGXqnl1hvKaAv5UGP4raFNC8pttbP0KMxGZN3AWQ8y35FqENDXpYCgXGzP0Lt1MuurCkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بدشانسی‌های لیونل‌مسی برای اینترمیامی در بازی بامداد امروز تیمش مقابل نشویل!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/106350" target="_blank">📅 14:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106349">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c6ed3f485.mp4?token=cEHyDPTHR6SwJ2hjSnf2EaKmMPBZY4CkI-5blwuTIotHByLp7zSQF6w13qgnntcIj43tP2UHWVzSl_ubKU_UVLoPMDN42BpSqbOHufogLHqRbfveGNTkiNYYZiOrhgDn3LBFzbPsAvgH2IiwttnWCsq3YLKHRn6K6v_DIv3L1VZfYRx8xgrX15ZGk01jNPcdqRGtIMmNUxikPCU4G7UepUuPp9D6FpoxCfggvQvWbr5wqw8cSWUULOyX_hKxGUPQPynhgcUO5OxPuauc1vbS8n_pUsFgUo-47afRwCz7HbidZZhyII7-E4KQwKz40d6CJFFDZPfpjutgXjLBHjofcIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c6ed3f485.mp4?token=cEHyDPTHR6SwJ2hjSnf2EaKmMPBZY4CkI-5blwuTIotHByLp7zSQF6w13qgnntcIj43tP2UHWVzSl_ubKU_UVLoPMDN42BpSqbOHufogLHqRbfveGNTkiNYYZiOrhgDn3LBFzbPsAvgH2IiwttnWCsq3YLKHRn6K6v_DIv3L1VZfYRx8xgrX15ZGk01jNPcdqRGtIMmNUxikPCU4G7UepUuPp9D6FpoxCfggvQvWbr5wqw8cSWUULOyX_hKxGUPQPynhgcUO5OxPuauc1vbS8n_pUsFgUo-47afRwCz7HbidZZhyII7-E4KQwKz40d6CJFFDZPfpjutgXjLBHjofcIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
یک‌شهر و دو تیم برجسته؛ به دربی جذاب شهر منچستر خوش‌آمدید؛ امشب ساعت ۱۹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/106349" target="_blank">📅 13:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106347">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cY6sYR1WU2MXbghl6Qo-2X-3JqybrMlE3a3PvUqKVaOw8DJYgQDD-9IayYANw8AsnyPvy1f1qh3VAHOkUgmzYS-4VFMT_JFtEfipZwwvQyzae0L3kYyepRteJHV8Ocoy0zfVoXgzs8ohRS4ij4RHtcvPzocPcM143F7P-Oz3-U1ZWkCChMn7xNp-7PjpnnttV_NFfeb-TVqrjz70phGjmkfo7ux92tkVZae_gWLHEVBwKROy3V43mxUgYemTjISS1Xwd44G5fGu67UbiapUhFMLb3ZD5Sv4aLNq30gFgWZAUD39wRlPWkO9CqyJwa6-zhioOhH-rAJhV2g6EcPuGyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qqn6Tts0RyMeR-PKWuTt2RJSfeegebNBLT58YQhCICSrObmP8wb71WKklM5XAVuReAz8OSdd2U14IW_3iPsCwir-KXPdHyr9s-MQE__hVL_aPV3P7BG1QgjtRUKFgI-UgtocMz6xFPMQrJfh5MIVMJZ2zIJpJIvbH2yvu5UikYZ-IhTFFfl-rBRxywlg1TyxsJEycKCCsQLvdMleOdc5NY4u0Q7Nx88jXOx6Dm-3_5fx4Zj4p3fD0nMeu0Cl3IBnUNqu5mNFf7_4zId09RPsF6dWCANCnR-MmjjQN1k4BJ78x61Le1bh1QKJPXBXKUEsFE6eti9hQcUsjErsYPsqSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
بر اساس اسناد منتشرشده، فرشید میرشکرایی، مشاور عالی و منصوب جدید تاجرنیا، پیش‌تر در پرونده‌ای شخصی با موضوع «خیانت در امانت» به یک سال حبس تعزیری محکوم شده است.
حالا این سؤال مطرح است که چرا پیش از سپردن مسئولیت و منابع مالی باشگاه استقلال، استعلام‌های لازم درباره سوابق افراد انجام نشده است؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/106347" target="_blank">📅 13:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106346">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJLnA5aEKDQeVmTE5xVx2Z0QaRNW83hIZVm9vV6Apd1MlqD7qB2wf2Cn7LvddhHJhUJbU6PQAnhDCcM4Aksy6OWM16BqNUL9dPqKT050L-9BsZEQXRk6z6-8GDGISt-WoXWdxfMGE3oxypBlIJABu40EZ_HsXs4N1zuFbwR2lxX1IjTa9Z0wBCrK95bSyYIyOvuOlxkrQY6grlfacCWtYWk_6BnXtmzPFJlsIiX5gCItUku6Tcxj_-5oA4agn-3lmKsfKia-uUmgus7pbfX92nZcuo4yUWrtaSu6hpUzfVpZUbCAYR9KE1-zn10y2rNNNaH0ERQrHil2s8Ay-YasNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
فینال قهرمانی آسیا 2026؛
🏐
🇮🇷
ترکیب تیم ملی والیبال ایران مقابل ژاپن
؛ ساعت 14:00
🔥
قهرمان این مسابقه سهمیه المپیک میگیره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/106346" target="_blank">📅 13:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106345">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddad7e35de.mp4?token=XUuQzSiqsDMlUV1dABYi3ZB62m6vRuQ62bQXXSzllQtUgtyuVekki0Z-8w3XmY-Ws6I6CTwLCHZOhMIjzeyKxdNAoWUeHeZ7dRuCkE4-I1pkTE0YecTYXfOpOx8LhCqIMeMTsXusHLpT3hkc_kAm9rOOr3dnUcjYDr9mPkKkUR2DfMTKB-l5pn30xEBtFiA5d4QdoIueS4yC2DBRD7Xt6i6B4phmJPlQz7Nega5PspV3rOdikCx7retguIh5fKRPi09KHYSlQUQq2jaTDGmwDc-o1D-qwl6kwk4UKUuc7X4RWbd85BL-1vwFr4Jmi7NkpKjlU_SDqm0TbU8V08u-qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddad7e35de.mp4?token=XUuQzSiqsDMlUV1dABYi3ZB62m6vRuQ62bQXXSzllQtUgtyuVekki0Z-8w3XmY-Ws6I6CTwLCHZOhMIjzeyKxdNAoWUeHeZ7dRuCkE4-I1pkTE0YecTYXfOpOx8LhCqIMeMTsXusHLpT3hkc_kAm9rOOr3dnUcjYDr9mPkKkUR2DfMTKB-l5pn30xEBtFiA5d4QdoIueS4yC2DBRD7Xt6i6B4phmJPlQz7Nega5PspV3rOdikCx7retguIh5fKRPi09KHYSlQUQq2jaTDGmwDc-o1D-qwl6kwk4UKUuc7X4RWbd85BL-1vwFr4Jmi7NkpKjlU_SDqm0TbU8V08u-qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
دلجویی آیسان‌اسلامی از هانی‌رامبد پس از مصاحبه اخیر هادی‌چوپان علیه این مربی برجسته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/106345" target="_blank">📅 13:33 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106344">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0dd00f3a7.mp4?token=Z2onH3RWCs2Q4L3YjPjFAxo1NFRgXKxxmbdncrokW55CMS_oZr-cIEJSt8IOJCXCKsYfuo7C7hKI6YI7oLMv4r6WDBqz-_iF6zuGYY4N5rH9OqvREHUsECaYR5L8MPeL1DfYSS0AUlF-JleoZkYCswruhbF4Emh9goL-AApiBRRmSDLCtkQlL_19CeiA33hTy3t9wR-ZS4oy06NAYWpZgdDdt3dXnQpo2TFvGRiLYB3XJQTDKlzYtRRc1qX-Pt1GDyA0bKW4jOUu1vxX6cjNbTWFXjKFDKeIGnwgquaKFq1Jfg8sJ1ofwFawbfcnD0bLabGG96yEuoAewFYcSg_lGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0dd00f3a7.mp4?token=Z2onH3RWCs2Q4L3YjPjFAxo1NFRgXKxxmbdncrokW55CMS_oZr-cIEJSt8IOJCXCKsYfuo7C7hKI6YI7oLMv4r6WDBqz-_iF6zuGYY4N5rH9OqvREHUsECaYR5L8MPeL1DfYSS0AUlF-JleoZkYCswruhbF4Emh9goL-AApiBRRmSDLCtkQlL_19CeiA33hTy3t9wR-ZS4oy06NAYWpZgdDdt3dXnQpo2TFvGRiLYB3XJQTDKlzYtRRc1qX-Pt1GDyA0bKW4jOUu1vxX6cjNbTWFXjKFDKeIGnwgquaKFq1Jfg8sJ1ofwFawbfcnD0bLabGG96yEuoAewFYcSg_lGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
برخورد ناخواسته علی‌حاجی‌پور بازیکن تیم‌ملی والیبال و یک هوادار ژاپنی در حاشیه مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/106344" target="_blank">📅 13:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106343">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUVLMX-pmu-unzU2oE1JsA-9x1K5jg9oyKqhZboKKIA39gGLPq8Ofe1PJx1eiZMtlKg_85Bou_0ObzR4jQGQnrZBykMyEKN6olrdWWxJ2HJa2J4rrmpZ6oO2O29xaQyJ9hr6ZSRE66d-AAfLBn_nphDNkkUg67d0q84Oyq4QkjaAHFfm6Ns8hk6Lc74_spZK9wXv9CTZ8XnevGCPq8qerSDjYz8Rb-bOcedAa7zUaTiTr0yDfa0wuEl-H8Rdc0Kln8rCZjDd8VsmeDz8FjkwjeCKuOnSVBrsBa2aUpHj3V0Sm7LP_XnbzphF358kS0U9Jno9GOonwe3jcyYWuq3xPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
‏
📊
نتایج دربی منچستر در طول تاریخ:
‏
🏴󠁧󠁢󠁥󠁮󠁧󠁿
81 برد برای منچستر یونایتد
‏
🤝
54 تساوی.
‏
🏴󠁧󠁢󠁥󠁮󠁧󠁿
63 برد برای منچستر سیتی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/106343" target="_blank">📅 12:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106342">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siCCvRBTJz27HNH9lutmEXgSD3WKz0tdF9tnlHJNBQ2oCI9_Ec5VDeJfIqGld1JrJvNUUZETIfjDt2saXznjn7PclM4yVa-Hlik2rkGTR2LFY9L50md3WYn1vyc6y-XCUc182B4uNv-yNpzZ0NHESrvt_3acPiuNe7T0EPFQrPNpKfT9e5OlYAa-0Htx3FoZvgJfJmZXsbqSvvufcb3aAeIbMdafMQI6GJdGb1XXf2vJsK4-8hknVd7AQKny8kNLRW_zE-LoY071-BgWTHd1NuMkBjGyS8gjiJ9GlCCywi42aiMpMT2slnW4rKKXjKnZs58wypvfKEs8buXVJk4Z8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
آمار یاسر‌آسانی در رقابت‌های آسیایی:
🟣
آمار آسانی با گوانگجو در لیگ نخبگان:
🏟
۱۰ بازی
⚽️
۹ گل
🅰️
۱ پاس‌گل
🔵
آمار آسانی با استقلال در لیگ قهرمانان آسیا ۲:
🏟
۸ بازی
⚽️
۴ گل
🅰️
۱ پاس‌گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/106342" target="_blank">📅 12:18 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106341">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCKjolIDAYe5aXKnTbeq5hsPhx02Y8nWRLrAUeo06MzkqN45KU2DUENSGSfNtNnkp7dpj6m9wXoc4L1TEjv7unq7vEpSazaCozHAH_UTO6UfEqG278Pd_2t8jPhck2FFS69LUOY4VSjNQbbqqViwZQl70iDTxif0JPpbj12_IYnxQ3pdm-bMDgcssuTvJt16bwcIq2-sC6ZJ6f0CtZXPgh8vtY2lBGhYorpm8luMoCDXR-Tx2ibdC6eJxZ5S2XZA7qn6K2oMGyrT7cTZ5A3W_Hz5K1BX1ykJvcAtleWyYfpxVQBWIkvKWZSTFTPZ9e5GqG-tNSOC4vAKwRQCpxKRmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇪🇸
خولیان‌آلوارز از لیست اتلتیکومادرید برای بازی با رئال سوسیه‌داد خط خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/106341" target="_blank">📅 12:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106340">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de2faf6374.mp4?token=Qd0MG9aGkmVswI8wuROK8RobuQ4_edi5z47d2Vcjh2tBj0IQuCrT0vH1IqGv0lkusVYfC-9JmEEv4-3lq9n3e2cxJfE1ImQDkSgVVWzdPvtvQk4yRchN9B1pu5VYQCjzZ5ox9ijjSmM-7bk7BnyZAVz914vlFL_qfTDVXiSfBTvRCmP1s3zgKW9r1mhBkxTw5qu9U42u2IFy4hriHd15L3xd8gMbujFypF8IFGrcU6lROA8Vb7ty8VoPWpnq6Sqh9Fuxrsv2SEZcn8x4rkjs_v6Q1oaB0vOCnVnHX5S7StdCFahwOc_UAqg7Cqt_ZwVfMNwAQggpA1aLureLqNPh2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de2faf6374.mp4?token=Qd0MG9aGkmVswI8wuROK8RobuQ4_edi5z47d2Vcjh2tBj0IQuCrT0vH1IqGv0lkusVYfC-9JmEEv4-3lq9n3e2cxJfE1ImQDkSgVVWzdPvtvQk4yRchN9B1pu5VYQCjzZ5ox9ijjSmM-7bk7BnyZAVz914vlFL_qfTDVXiSfBTvRCmP1s3zgKW9r1mhBkxTw5qu9U42u2IFy4hriHd15L3xd8gMbujFypF8IFGrcU6lROA8Vb7ty8VoPWpnq6Sqh9Fuxrsv2SEZcn8x4rkjs_v6Q1oaB0vOCnVnHX5S7StdCFahwOc_UAqg7Cqt_ZwVfMNwAQggpA1aLureLqNPh2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کاش دوباره برمیگشتیم به این‌ایام شیرین...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/106340" target="_blank">📅 11:55 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106339">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106339" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/106339" target="_blank">📅 11:55 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106338">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCNBxxPTuEpCXH1orrgrydz4xqVgoHL45ShsSi_jkQah8XeNngi4Hmdw4EfqyyNuHvKScpY4GEKnDvsyU7ASv3nfGbJQbqKTiAdqmVs7b53F8GFbf3bT16b8vr8kCQ0Z447Yvn-e0n0sP24a0xz9q7rR5jFeq0CTm_p32iDqNr1nxEg6PeQh2RmJbb49BPs2bdjmNYt0V0Bv1pStEUy7kT3ZcuaFy47uLlJ5KE8i7ESgRTgYBR47fhmFT1oCRusBWqvvS4rhiY_p_VUxPgOKZt0ErkZFBFoROyItB5MFoIiFE6kY1nPpFQ3pbXPejiYZejb0jwh2QxeMnHCqVo1keA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد بزرگ منچستر در راه است!
نبرد هیجان انگیز
⚽️
منچستریونایتد
🆚
منچسترسیتی
⚽️
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ دربی اخیر منچستر:
⚽️
منچستریونایتد: ۲ برد، ۲ تساوی، ۱ شکست و ۵ گل زده
⚽️
منچسترسیتی: ۱ برد، ۲ تساوی، ۲ شکست و ۵ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/106338" target="_blank">📅 11:55 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106336">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skTV9Mz5yysK708FmhpZhu-mc94C5TZR54la7ElknqLdmG35kEfU1Rre_el3JSiS49dWdEPehSZNrhrw0jHsXo3X5stxnf7qH6AV3hUCZDdhSbZkbFxrjhMoQ-7-4NyX08G0qXPl0JLEdPcm1h8RIaAlGvMlYTiKi6Ku4ISFJxXSvy9Zaavpby22OJSGjizhh1EChUrHi-t8svTxjkDkOwbCmQKlTrulVhzbx5-eE-UGQJ0cSr8BkKa1g61A7WQZ-Vy5NVdWu9ytSw6dZLOPAMQ-0DOgFJdQiomvJ9ccMg7YWt-DUl-1XQcAhLZ_s61uqaCcKd-Dot-jnQpFjiJA7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🇮🇷
پوستر باشگاه استقلال برای بازی با السد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/106336" target="_blank">📅 11:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106334">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe38a96709.mp4?token=ft_rTSsO4XL3pNiVCd_uC0xT1DKKKvtUvakg_4Ip6d58D6Ef5Z1XfOpBRIXf7vu7JB_NxKmfVwlEJaXAq3RVcQfs_6rvMgS2gEcoDZNZMxgNsdN_rlE2GTMNi4WRovGVC2xL-Jugi2_7HEje0ihfi5m0pxjbIVc47j4win5gfK0wIdWvwze6vWVxwqLH1XLTeIWMB0h8vC2_VCIwB0Gy2EGHa9dcYl-9jttlSqi6oTk5S3aITAl66XdiUi0G5lEpVvxPZLj4KL0rh7qiHVNF7WyepDoS6lFMFaVh_5w1lyyr3w2ErRHgQ4tfFiwjgUzYDJ_63-nnCQMsDX5mUFbmaXsE8L2mguvMPPizq4s_xpXCm1_kv6m5KdxInyKDDf0_82XXWvrZ1EkGqDKjkoNAlvg8fdZPhtwQfo2Heg8e2D66ktXAtz7mMU0sLqgsbGiiQv5s2OS03BtiQM1k2iFjZcAA7bmmpI1-VOKVqXZ_5mBThVuXSmAHXV_DwBnfFzbhBS9Iyfm1OOtCFgFJ_0wzYrkGpJz_wURksKwWI0aEAvq-ox1f5ncz1uuSzzB9T-TGv-HoBHpFFUQk1Yu7VNWLax4cNWiy9EkNoGI4_7nH3aSxEeSgY-mYco47itpOt-tIFgEJ1TTFyNadTJ_DRE_Xreky26q7rb9fouf6m0PrSXE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe38a96709.mp4?token=ft_rTSsO4XL3pNiVCd_uC0xT1DKKKvtUvakg_4Ip6d58D6Ef5Z1XfOpBRIXf7vu7JB_NxKmfVwlEJaXAq3RVcQfs_6rvMgS2gEcoDZNZMxgNsdN_rlE2GTMNi4WRovGVC2xL-Jugi2_7HEje0ihfi5m0pxjbIVc47j4win5gfK0wIdWvwze6vWVxwqLH1XLTeIWMB0h8vC2_VCIwB0Gy2EGHa9dcYl-9jttlSqi6oTk5S3aITAl66XdiUi0G5lEpVvxPZLj4KL0rh7qiHVNF7WyepDoS6lFMFaVh_5w1lyyr3w2ErRHgQ4tfFiwjgUzYDJ_63-nnCQMsDX5mUFbmaXsE8L2mguvMPPizq4s_xpXCm1_kv6m5KdxInyKDDf0_82XXWvrZ1EkGqDKjkoNAlvg8fdZPhtwQfo2Heg8e2D66ktXAtz7mMU0sLqgsbGiiQv5s2OS03BtiQM1k2iFjZcAA7bmmpI1-VOKVqXZ_5mBThVuXSmAHXV_DwBnfFzbhBS9Iyfm1OOtCFgFJ_0wzYrkGpJz_wURksKwWI0aEAvq-ox1f5ncz1uuSzzB9T-TGv-HoBHpFFUQk1Yu7VNWLax4cNWiy9EkNoGI4_7nH3aSxEeSgY-mYco47itpOt-tIFgEJ1TTFyNadTJ_DRE_Xreky26q7rb9fouf6m0PrSXE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
هوادارای التعاون دیشب برای اینکه برن روی مخ روبن نوس، بازیکن الهلال، اسم دیوگو ژوتا رو که دوست نزدیک نوس هم بود فریاد می‌زدن.
✔️
👏
نوس هم بعد از بازی درباره این کار مزخرف هوادارای التعاون فقط گفت «امیدوارم حداقل بعدش نرن نماز بخونن.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/106334" target="_blank">📅 11:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106332">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/933458c59b.mp4?token=fU24EJzIPm7gzda-O3h2w33RCnb1mGWl4X3Iak6d3tcHf1x_TLH0SJZXR2UZqC2umsSKQaGm7ParCadmbHscl_J35gaD_YGU4NJ0CTE2vq3aBcNP22fWq8Z98fQF1kpT-34Sfrajy2G6EqHdAjt2tbx4KD3zYPP4WgZXrZtXnmQXPw5z6dr8GuDTazgTQCWXSn4KdGEuoasXouCqW7qsCmC-h4OFmTwYMvXezHdepmDaWhFuEhRYsHLwdVlHiZHlupBuJtfS18XkDnUHNhBP4GcHJJmQlZqYWOlXxaOgNuGGqLWoTzfUl0BlXTYLCuMWS1K8VbGozLrXzz8WWBul5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/933458c59b.mp4?token=fU24EJzIPm7gzda-O3h2w33RCnb1mGWl4X3Iak6d3tcHf1x_TLH0SJZXR2UZqC2umsSKQaGm7ParCadmbHscl_J35gaD_YGU4NJ0CTE2vq3aBcNP22fWq8Z98fQF1kpT-34Sfrajy2G6EqHdAjt2tbx4KD3zYPP4WgZXrZtXnmQXPw5z6dr8GuDTazgTQCWXSn4KdGEuoasXouCqW7qsCmC-h4OFmTwYMvXezHdepmDaWhFuEhRYsHLwdVlHiZHlupBuJtfS18XkDnUHNhBP4GcHJJmQlZqYWOlXxaOgNuGGqLWoTzfUl0BlXTYLCuMWS1K8VbGozLrXzz8WWBul5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برادر به پوچی رسیده و انگار دیگه هیچی قرار نیست خوشحالش کنه.
‼️
⚠️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/106332" target="_blank">📅 11:05 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106331">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1hfRalGFvUDbd4BD7WXUu4rSBI7UpCqaxtNDNQE4feorLlcOzom3sa92TXeKxnPDTP6FwEgcV6EoTLQTRpbC1cynk6WiKA-rWbNP5FTwsEQayf9_nKnS6kzpARpXyg_0p5OSfc42bDLia5YeZ3s4MHDC7uNxzpBJDvytLA2gRtxxoU8mXAmeRolsM1fYZVD-gguGmtY1DMnwi9gt1cJKfFZEKArCmUGo2lT03Ykx-zV1CkWZd8BLMWJgxeAFPJ-GOOXIJ5srmhEgGMnkQPVv2O5CQpQgr-qRjSKOn3MZMBA2kvF3R9bPVUCDck8Xj0c000Tu2EB8Ux7WQ55tg_fcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
📊
‼️
جدول بهترین گلزنان لیگ‌MLS
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/106331" target="_blank">📅 10:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106330">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a30251b5d.mp4?token=KJEOyhl5fbQ9qDOLI9UZINsGwCtYnawDszAhDJ13SeUT1KhfvYu4H1ViCR-nvpPTRQAGjtatIYREiAAWCuiMGT1JtoE2oQEfEn9owdj3QqbneqTsZ0aAJeu5kKVC7mabPNrQ4Yob2z_25SXjLBW0P7i__6Ynh8FlTaJ7Cagu9cnwzJMz9uBK46-_7MksDc13ef6KEzer1a8wK9UOZ0Pb-7KdrTyOlfTJi3D-b36XtzAV_5LfpAHEEbCJPD2qaXHYQsffvE3gb3oDEajDU8qI1PBP_sypTnnTFrm0s37XPoscQAZqo1kUwCtpVRzeeCvIS8_ceE-MsfqPZ4cxHnpIpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a30251b5d.mp4?token=KJEOyhl5fbQ9qDOLI9UZINsGwCtYnawDszAhDJ13SeUT1KhfvYu4H1ViCR-nvpPTRQAGjtatIYREiAAWCuiMGT1JtoE2oQEfEn9owdj3QqbneqTsZ0aAJeu5kKVC7mabPNrQ4Yob2z_25SXjLBW0P7i__6Ynh8FlTaJ7Cagu9cnwzJMz9uBK46-_7MksDc13ef6KEzer1a8wK9UOZ0Pb-7KdrTyOlfTJi3D-b36XtzAV_5LfpAHEEbCJPD2qaXHYQsffvE3gb3oDEajDU8qI1PBP_sypTnnTFrm0s37XPoscQAZqo1kUwCtpVRzeeCvIS8_ceE-MsfqPZ4cxHnpIpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کودکی‌هممون در یک‌قاب
👍
💥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/106330" target="_blank">📅 10:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106329">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70a4aea1dc.mp4?token=d52Fv2QkmhZ9LRogw6sIJiijLUTswgX9js8WQ67gDdiHKdpYxbSnhaLIrygj8DE6g0k3fhi-Zmg-ehCZAkLVVfKzns10i_wgCYKvajNrW4O4jL0D2N3Rhq81wEFyVVltYsVkyMMbeNPP-rESfDQ_3i789D2EyXySucApqsOPrLgL-thX8vI77XUlh_cRv3HVKnHjabWZBLyZl--dXolSoynqrb5M1O26mXulX5mtoLOlcWL8At4LKrQzcVun3zsKfOxj1FL2xCq328U6Si1xgjVFZ8wfqBQmVRD6OXMjdlIJaHUQjhjzC7Bt_pUplwvcXwVDMsQp3lUTwZQre6JZTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70a4aea1dc.mp4?token=d52Fv2QkmhZ9LRogw6sIJiijLUTswgX9js8WQ67gDdiHKdpYxbSnhaLIrygj8DE6g0k3fhi-Zmg-ehCZAkLVVfKzns10i_wgCYKvajNrW4O4jL0D2N3Rhq81wEFyVVltYsVkyMMbeNPP-rESfDQ_3i789D2EyXySucApqsOPrLgL-thX8vI77XUlh_cRv3HVKnHjabWZBLyZl--dXolSoynqrb5M1O26mXulX5mtoLOlcWL8At4LKrQzcVun3zsKfOxj1FL2xCq328U6Si1xgjVFZ8wfqBQmVRD6OXMjdlIJaHUQjhjzC7Bt_pUplwvcXwVDMsQp3lUTwZQre6JZTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عاشقانه‌های مسعود شصتچی و خانومش در مرد سه‌هزار چهره؛ عجب شاهکاری ساختن
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/106329" target="_blank">📅 09:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106328">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrtzYowXs6Yt3XAUzCZmElLi054Ux-_Q8btyr85z5rR_oS0Ubc_LjqNmKRrlrAatBztGQ5NutLFV_WLNc02LlUWmyBf30i2y2mf-rsCGsz6OvlpKVBY34KZmVu1Tpogbv0-Afg2-a4tW2pTt_lTN8FadDK0XqI9dkDYKnPby9h3APmpdMJT-CZv6Nu88b5VNxh8VdmkZiV4tEh5gP34hA7OsY303xe5ynnImFXfP84zHtKwWEUjnJ-IN3p10DKWHQakzuYiltADjF2NmjFBTqE4GrTfSmhuFGzUBiUl42_b6W3Z4yghN1TIHMhrX014yxj3ic56Pb_SrHIuzMSokgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
مقایسه آمار برجسته ترین گزینه‌های معرفی شده در بین نامزدهای توپ‌طلا در سال ۲۰۲۶
🇩🇪
هر‌کین 73 گل و 8 پاس‌گل
🟣
لیونل‌مسی 45گل و 30 پاس‌گل
🇪🇸
کیلیان امباپه 58 گل و 13 پاس‌گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ارلینگ‌هالند 58 گل و 11 پاس‌گل
🇩🇪
لوئیز دیاز 30 گل و 23 پاس‌گل
🇩🇪
مایکل‌اولیسه 27گل و 35 پاس‌گل
🇮🇹
لائوتارو مارتینز 30 گل و 10 پاس‌گل
🇪🇸
لامین‌یامال 25 گل و 20 پاس‌گل
🇫🇷
عثمان‌دمبله 26 گل و 14 پاس‌گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/106328" target="_blank">📅 09:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106327">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0452f0d7e.mp4?token=Ms_1P8iYdmzRz14LpPC0_8VU7SAjRFjfO70hSzVxxXAkCTg5HYmPeAIZSHbko7MtExAF9OvjMk-LJcrNjHBht_0Fd8_D1HvrwTpgVSDaP9EIZ7oDif0gHZhLz9YdlI-rc3wJjh7Am2LCSlM4nEmOlhj0i70a7zCmQK3F3wmdXGbqmn7FE8xOinArjLQCf5kaNAbrYnspQYMpfiFZGZc0BExPolccAGXn4Cm7DrggJNQXMFLriobKkJhIqT6sp2HH96OVWOYD-I7Q5x6Lz6U-4nW8dbbI59lrHkeMpd2vsKGjfhianl0SiiiziqIKrRGdqoypmyJ6cu62ABa1j4rZaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0452f0d7e.mp4?token=Ms_1P8iYdmzRz14LpPC0_8VU7SAjRFjfO70hSzVxxXAkCTg5HYmPeAIZSHbko7MtExAF9OvjMk-LJcrNjHBht_0Fd8_D1HvrwTpgVSDaP9EIZ7oDif0gHZhLz9YdlI-rc3wJjh7Am2LCSlM4nEmOlhj0i70a7zCmQK3F3wmdXGbqmn7FE8xOinArjLQCf5kaNAbrYnspQYMpfiFZGZc0BExPolccAGXn4Cm7DrggJNQXMFLriobKkJhIqT6sp2HH96OVWOYD-I7Q5x6Lz6U-4nW8dbbI59lrHkeMpd2vsKGjfhianl0SiiiziqIKrRGdqoypmyJ6cu62ABa1j4rZaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ال‌نینو دوست‌داشتنی چه هیولایی شده
🥊
🏋️‍♂️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/106327" target="_blank">📅 09:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106326">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9R1kkmjbXpCQrg2ClLY66FSybWvEFSDErI4PfpASWSoPqD3lrOLnMoI4KGBBO6LUdsKfecEnC-dbiqWJQSQa3ml7AJuartgkOsBIvahg5scI2eD0iGsVy88u86EDwbSnftWb7J7trvL3KBi8FPwCwfgpJQe_QfF5scgTXAnKaSBSBvf-_BxrUCAsnp3QNY4TXQ30ud7-qauvUmtLqkNyVrbWlZ7g5aK1aiszk5UZLPyWRM5lpWghzeVPe0moCU2uKvh0fiRAA2_1pYixvPwDkhG26v0laWqZWbUtVM2GoCkOCwzxClBo_zaP0uVBBz2L9sJ9BQeowtpjZUaAdo6NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
🇶🇦
رافا موخیکا بهترین مهاجم السد قطر و آقای‌گل فصل قبل رقابت‌های لیگ‌نخبگان آسیا با ۸ گل زده، بدلیل مصدومیت از فهرست تیمش برای بازی با استقلال خط خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/106326" target="_blank">📅 08:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106325">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bde925455e.mp4?token=QgFXfkKYUhbPq6KC1MTIE2rgObf-8-5F83tN0N1-r2TsXLZHJK1auhVPz30oOlrYn-rNQFMNn9KGH4l6yz_EyJOjZcYBtPYkthmGsWPfu-bcD_2_OC61RKLgDyHH7FqdZORjXN_iw_K1cdcm29T6-0jcXF6Bk1-sUw4VOq5aJQMRKh-nhIk9Z2_hms1dd_3DCzYz0JoWeVzG5i0xMAYtZUoyMeLl-_n9U1ogo-migeT-e5jeNUdcbmyG5PwJq2x_6kbamlpYC23zWNaCRATWpBAZ53kQ5sPfG_tZlssWzZ4GiZk-4D4_kl_gPtoHhq0CeSEj_e8O6e3Bv1T2v7f39g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bde925455e.mp4?token=QgFXfkKYUhbPq6KC1MTIE2rgObf-8-5F83tN0N1-r2TsXLZHJK1auhVPz30oOlrYn-rNQFMNn9KGH4l6yz_EyJOjZcYBtPYkthmGsWPfu-bcD_2_OC61RKLgDyHH7FqdZORjXN_iw_K1cdcm29T6-0jcXF6Bk1-sUw4VOq5aJQMRKh-nhIk9Z2_hms1dd_3DCzYz0JoWeVzG5i0xMAYtZUoyMeLl-_n9U1ogo-migeT-e5jeNUdcbmyG5PwJq2x_6kbamlpYC23zWNaCRATWpBAZ53kQ5sPfG_tZlssWzZ4GiZk-4D4_kl_gPtoHhq0CeSEj_e8O6e3Bv1T2v7f39g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👍
صحبت‌های شنیدنی لاله‌مرزبان پس از دریافت یک جایزه در جشنواره فیلم ‌ونیز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106325" target="_blank">📅 08:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106321">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gN_phEB1bQpcIuB2KIlT0QWlAQY94r4H805vjW-ZNwrjWD_WAC12EkjXw-vrr-0xAYjMQ2KT8ut4ZBSJHXJlrq_esa7U5kLuv-nx4OjRMABPqFZUUm4p8UWLdlbQEDik41IqQIB1F0RYcNjRZcX9G3WbNXfTbyijYEFcKUkjDJtb_P7n1dj25UgVgr3-eJwYrAfFHqfxBllkyCVWx-DuQrmrHx1W9g-MM9afD8LQMwNuAPYSF-_Q3e9nD91GVdXbMw-azNimS8qq946POguKtAJUV1pjie6kRfRIKYkCy-xBMdx8Szev3t1oaqkIrV69N9va8ix8gLdc7xlkJtrkbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌چهارم پریمیرلیگ؛ آرسنال همچنان درحال یکه‌تازی؛ ساندرلند هم مقابل تیم آرتتا زانو زد
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
😀
-
😏
ساندرلند
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106321" target="_blank">📅 00:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106320">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edVVV2omMCy5ygXFt6tNuXjf4ksmKeO8gTfdce_M2RgusOnvWnLI_4oPYiN0fi4lMuGzGVFDae3J8kkUQwu7XGI-1YoonFxEmUE8lOeFVtfjNiEgoRxdGw5vGF315fC0vWuNGSLkqZPhcvDsoXCPNCjC-b9AWW3j8TvolHEuP9K5nMfECOTpRmNeoK0k490uNB-lLCMa6SJBrrFcnz__h8hacUCI34E7vcq0iVtT6c6RjRMW2MCMFlTicShA47RXClb2IHLu5oiGrNk70QrGiwibivT3939BiqaUCv0RB-wC4ZZCChSQcQ6Z2UG_EPd9y4zWkyi5yMhOxiW4SvHwQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔥
کیلیان امباپه با رئال‌مادرید در تمامی مسابقات:
🔺
۱۰۹ بازی؛ ۹۳ گل و ۱۲ پاس‌گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106320" target="_blank">📅 00:33 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106319">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnSZI-eNMJeqxpLdWpOfd1OIUW7cZigBRELRs02YHoCPlNCBro-G9dKFFX9zzkg2YXdln5Z_WG0LpxXyJSaq7LxwZkNANJT8tlgRXe3xM7No7zlDcuHc97le6qI16jT7N_R0du36JPaSDjmuIXFL2Qluy0YfzJXykhKlphlfKaQt3jP5LdmLxIhuBmI4BTCiBOmOePvWXesS88BcHgFqq0Z88IgZu68AYf-jszpyJLktPClCq8bAXQ0zJmV4BkaMDWtYBGg1BH9kGscykkfA2SeD3icnzLGWVvfs4dOe4RXSjbNZs78xo9u4980UX--lstwdWuXY6mUgmwt8JjF0Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
گلگلگگلگلگلگلگگلگل برنده واقعی توپ‌طلا</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106319" target="_blank">📅 00:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106318">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6MFA8XiP4dBg0njg8Rj2QNrqJPeHC16s7BxcCGIq5odCuLh_GIr-VjrVOqVqth8QwODkGxm5DhwWETTzRNfigXdvZD_WmPtncWm1FJoIOfy7_nK9HEIDsC_ZcC9Flet42CyH7Ic0f7WGd-hFcJjf_72ILRu8zuhGQHTjeJrReEe8bfSgKar27txw1bCok_xwoLBqyy-3x2f-iP4fDugnDF4vUHnERt0P_U6BSnPqkYrSl8D4ynktUlWdK-iDaxQqY8LsSN_-UNqKUTVXufhS9Ma1ls-8CLXRC3_uNfXC9TtZ6WO2m_26xtIOUuekM3wA9aZvjUAySVl5hApB8NGzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌چهارم پریمیرلیگ؛ آرسنال همچنان درحال یکه‌تازی؛ ساندرلند هم مقابل تیم آرتتا زانو زد
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
😀
-
😏
ساندرلند
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106318" target="_blank">📅 00:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106317">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0f6e034671.mp4?token=qq4LaLU-PmTdx9TWZl1rW2LUXKZ7jwbj8RPoUR7myccIY7KWDQ5yfrb1fH5SqwLx1GmriI9ugi46Vx1smx9L-8EduhnHx2uEtpOWXODwO4O3RXvmll78IJYwH40lXjX5EcZLHEpXZTlNuuaTSJZJFcm9plNrKeVBnaK2r03FECd6IJ0pXS9MCCVgP5w9961JGFYHRB5V0A2_ep1TbdZJrzdMT9X-1Aq0cCzQ8Y9hDZBWu5LTtyXS1OL3mSqZMv7TByDrxSybOE0pF1nem51MhzNYo4VUB6GFnv4P-S9lPuxSoGOghxqWrIth8md1AhfJrMfUlDw15jxNEp0YXkGGRg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0f6e034671.mp4?token=qq4LaLU-PmTdx9TWZl1rW2LUXKZ7jwbj8RPoUR7myccIY7KWDQ5yfrb1fH5SqwLx1GmriI9ugi46Vx1smx9L-8EduhnHx2uEtpOWXODwO4O3RXvmll78IJYwH40lXjX5EcZLHEpXZTlNuuaTSJZJFcm9plNrKeVBnaK2r03FECd6IJ0pXS9MCCVgP5w9961JGFYHRB5V0A2_ep1TbdZJrzdMT9X-1Aq0cCzQ8Y9hDZBWu5LTtyXS1OL3mSqZMv7TByDrxSybOE0pF1nem51MhzNYo4VUB6GFnv4P-S9lPuxSoGOghxqWrIth8md1AhfJrMfUlDw15jxNEp0YXkGGRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
گلگلگگلگلگلگلگگلگل برنده واقعی توپ‌طلا</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/106317" target="_blank">📅 00:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106316">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اونور آرسنال دومی رو زددددد</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106316" target="_blank">📅 00:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106315">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">برنده واقعی توپ‌طلا دبل کرددددددد
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106315" target="_blank">📅 00:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106314">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">رئال چهارمی رو زدددددد</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106314" target="_blank">📅 00:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106313">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKylk8HjsuQwQbdoiGDMpr-ELbEYLJzbQFagNec0LdDGkKWKe61zU9N3FZXya29hqjpGPJ8FLx2bAlz01MCYfLqyTcWrw7PBh9XKdgex7Zi84A_CaDjp2nZ7cKs-oLmOwzQ5rF9-W6UAvuts71jekm8z-f6N1-44cK2g5rwqqapQY9oWEuyWK4ahxneTKh2CV9nuWcb85tT06znmqG91hCeWBftIn7UlQtFy3ANimuJW63RQkrV9cbYKdoctH5vi4Fj0EvcLJTMJhivdMSVJsic4eU3YJsABMAczYycy9am3HT_vlBTMj_5YiMbWMtWy5-PYgYxg_n-jw-YLJH-5ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
🇶🇦
استقلالی خبر جدید براتون اومد؛ مارسلو بروزوویچ از النصر به السد پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106313" target="_blank">📅 00:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106312">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cm-min-W_R359sNqAt0Xzx7YbOgVMOgo5ZwCnZxLVHdxfVzmokbCMowJ225NcSdTA0eP0bGbNJZhkOxddfz7v26pq5ZSuN3dyKXJuXFxCW1P5uwgQCvubG7TjIw0zReLtUR1WbabkyyZrjaZjmvogB3waQE7bh6Zfj6ENnLhyY1Q90FCyGAptrZOmTCAqfhMLXLi5n9NrgIWiQrZM1fszQvsRzDR4QoovzeLA8whrzKIBb3UcKTozL1AIYdhfkU6LAg7SuMiJhLdXdZvMmZAYSvpfO-eh0t63xlr8CCEZwoCw0buO4AG0DKbCmq9GcxnnH9ELL9ZV5tC6B9UtJAlRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صالح‌حردانی چه دلبری از سهراب میکنه
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106312" target="_blank">📅 23:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106311">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d53729e95b.mp4?token=MhjQhIRGRszuJttD7sEd0QUNYaqHf1bfsOeT6Y4KpzESTdNttC5u_ih20POAClqYcwUzIk2M5K9EY0lggQyHBcPhHeTJGrTo_cXdFjU-wpBHdZOVWLrDxdMgZeCMOq4kLD98WEV70eEKXv21qz-_jyXiWV8CJWyQmmk3Jjg6IM7_O7wxaRzaLgZ92HRVBjILZtZCH0nYrB2Dc3JuoGTH2eFSPOc5Zlmf8hGEZ2tX16DIYlHp9jKvQs335ABpc7tMkF_MTHPgmLJSwEsKHhSVCYzyYE1ZK1IllYrkQ2jJ2XXFcEysjNjgedeLvVWa3pH_FkOWxSqx3Ho4Z8qaBigj6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d53729e95b.mp4?token=MhjQhIRGRszuJttD7sEd0QUNYaqHf1bfsOeT6Y4KpzESTdNttC5u_ih20POAClqYcwUzIk2M5K9EY0lggQyHBcPhHeTJGrTo_cXdFjU-wpBHdZOVWLrDxdMgZeCMOq4kLD98WEV70eEKXv21qz-_jyXiWV8CJWyQmmk3Jjg6IM7_O7wxaRzaLgZ92HRVBjILZtZCH0nYrB2Dc3JuoGTH2eFSPOc5Zlmf8hGEZ2tX16DIYlHp9jKvQs335ABpc7tMkF_MTHPgmLJSwEsKHhSVCYzyYE1ZK1IllYrkQ2jJ2XXFcEysjNjgedeLvVWa3pH_FkOWxSqx3Ho4Z8qaBigj6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل اول رایووایکانو به رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106311" target="_blank">📅 23:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106310">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/152a6c453c.mp4?token=ZrdilJ2-fPXgtthrQHXRxQA4lSUu9rcnuoKF1t4W-RXKeJHolcJEUW_MPxt30ERUxmkJp87Ox3LgaBMhSD3ZBNfKn3yxY-tmdbe6pQTDa-YM0Fk3TYbZoDcxd44XVKuOPxKMQPel-gLTmDIkgOTy1PyazvIFUZTmRqLPcBp7WfHWF1kB5WAZVUsd-YVren0c0BiFGnEBWzTZhfpbd5kPVcDoeyxZMGSdAkOees6IeJjCVQlHOUa26QfvgxK_kHt6Udq6GndTUdRhGGdZYq4DBJW8hOc4e_cgVUnSBsO4STaXy17nu1i9n8ZYEs1xhiXa3-w2n2SBQoTAS_bbX0YHrg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/152a6c453c.mp4?token=ZrdilJ2-fPXgtthrQHXRxQA4lSUu9rcnuoKF1t4W-RXKeJHolcJEUW_MPxt30ERUxmkJp87Ox3LgaBMhSD3ZBNfKn3yxY-tmdbe6pQTDa-YM0Fk3TYbZoDcxd44XVKuOPxKMQPel-gLTmDIkgOTy1PyazvIFUZTmRqLPcBp7WfHWF1kB5WAZVUsd-YVren0c0BiFGnEBWzTZhfpbd5kPVcDoeyxZMGSdAkOees6IeJjCVQlHOUa26QfvgxK_kHt6Udq6GndTUdRhGGdZYq4DBJW8hOc4e_cgVUnSBsO4STaXy17nu1i9n8ZYEs1xhiXa3-w2n2SBQoTAS_bbX0YHrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌سوم رئال‌مادرید توسط جود بِلینگهام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106310" target="_blank">📅 23:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106308">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بلینگهام هم سومیو زد</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106308" target="_blank">📅 23:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106307">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a23278bfb7.mp4?token=H-fOzAocCPUwy1ItCmd536Qu3OxXsC-pa81Yjicljoa2e_F7Me43KrRoboVHPaicIj_Uhth44mt7uUX8XzL501jxCeCFz5zP8_XuR_zxcMHHNJDpuyIcigen9UnARE_KJllKRJc-1Rz31VZRxULn8wGqz0OzNhEOA9bqIshXX2ov72-Ye1nDtQf6JkGX3O85YmlTvaQTzkytXaBY4PWPiSmXqH5C9U-mrjw9BjaD6d64sgLpVYL5GFhN5mVPmgAzZmHj34sE5ow9uVeCBOIbv7A6j-qF01-6UPUadcbyXVdBa2eBAUfyC2CkLNN-w6gSkmQH_33TjnV06u0VeKaDjIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a23278bfb7.mp4?token=H-fOzAocCPUwy1ItCmd536Qu3OxXsC-pa81Yjicljoa2e_F7Me43KrRoboVHPaicIj_Uhth44mt7uUX8XzL501jxCeCFz5zP8_XuR_zxcMHHNJDpuyIcigen9UnARE_KJllKRJc-1Rz31VZRxULn8wGqz0OzNhEOA9bqIshXX2ov72-Ye1nDtQf6JkGX3O85YmlTvaQTzkytXaBY4PWPiSmXqH5C9U-mrjw9BjaD6d64sgLpVYL5GFhN5mVPmgAzZmHj34sE5ow9uVeCBOIbv7A6j-qF01-6UPUadcbyXVdBa2eBAUfyC2CkLNN-w6gSkmQH_33TjnV06u0VeKaDjIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌دوم رئال‌مادرید توسط کارراس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106307" target="_blank">📅 23:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106306">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2689afdf46.mp4?token=WJbHD_ZRao6luU0F8yqtlgbBW4uxGOiVa_xLgNsmsP5ZARHoHSgRAtN3AfxrrOISdBPRkrYhOBVn2KrN7Ly16GoeKJMPSznVITZ9rdIupBAx_TvvtEKNUXm6KTiQaVcvPt81gnQhmYGlNaWe9BEDY8xmuy_zNWcKGA3iXziIQl9fI21BGIldDYLpaz-yB1O2JgyWe5epmlsG67xMt_a8AzA-0jixI58g_H4xBWUWs1rmDsFNdGJTsFVCP9KS8RU6gU4g2vVYT1RgECtwBZUdYM_81Y_JbyhRgsJ0WRWUc7QKPILl--dKj101LauvoXrviA6H6QSAWSMRszpX_inHKA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2689afdf46.mp4?token=WJbHD_ZRao6luU0F8yqtlgbBW4uxGOiVa_xLgNsmsP5ZARHoHSgRAtN3AfxrrOISdBPRkrYhOBVn2KrN7Ly16GoeKJMPSznVITZ9rdIupBAx_TvvtEKNUXm6KTiQaVcvPt81gnQhmYGlNaWe9BEDY8xmuy_zNWcKGA3iXziIQl9fI21BGIldDYLpaz-yB1O2JgyWe5epmlsG67xMt_a8AzA-0jixI58g_H4xBWUWs1rmDsFNdGJTsFVCP9KS8RU6gU4g2vVYT1RgECtwBZUdYM_81Y_JbyhRgsJ0WRWUc7QKPILl--dKj101LauvoXrviA6H6QSAWSMRszpX_inHKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پنالتی امشب اسطوره توپ‌طلا امباپه
😍
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106306" target="_blank">📅 22:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106305">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ریال امشب حشریههههههههه
😍
😍
😍
🔥</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106305" target="_blank">📅 22:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106304">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">کاررررررااااااااس زددددددددد
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106304" target="_blank">📅 22:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106303">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گلگلگلگلگگلگلگلگل دوم رئال‌مادرید</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106303" target="_blank">📅 22:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106302">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5ZzT8G3j3OLuJgrJodBlY9FZanAed6GbGS3OHxDwRkdM4Y_c9wKdwU3R1fTZIuJV8j-WWj6VrCIdmcPmSTRU0EFkWj8Q-DJKlBdG9blpiS0PjVdQLIG_Rn-64wxJ1jVYO50PE8f6G-gQWdP4K_ZhmAMGEqEqRtE9eiR2FviAgGP4AEt49P5uv2EZmVs4CHNcnEFmbS02WJmH4dIc4Bb7z7MLkADeizCwpto4bIiJgeonF1hc-LM8e4_nQRQSDDGCpc1Mb0DayOj1SfQKBwgoXiSATbQGpznmGwZbNmGovkTlMgRXmq0_Lp4UQBSoA2Kq30Kjo6xoNeW5vZPEWTfpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده واقعی توپ‌طلا
🔥
🔥
🔥
🔥
🏆</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106302" target="_blank">📅 22:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106301">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">رئال‌مادرید زددددددد کیلیان‌امباپه
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106301" target="_blank">📅 22:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106300">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گلگلگلگلگگلگلگلگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106300" target="_blank">📅 22:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106299">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">پنالتی برای رئال‌مادرید</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106299" target="_blank">📅 22:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106298">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6SEJdhB-PjkZVJ4BQZEwzf_0b04kwOobxJEZPVZxWRMsofboMwkv6m4vw_6c7r3S--Xy9P7VKQbtpgpKAbyIgoYeXBUFNGwg6O_FZbDPS6ImD3lHY4r63nRSmVH699K-m_rnxnC_Ny5Y63xJ0By_K8zM-C9tBs4eiDZt_inOEOFVGkkYO91eXiUtyBZHgc2vebblVqhdykwS_v9Rp1nEdtDaIxoRu-GJ7wEYB-SeBQ_jTF7ApJzP0smh9UJ_cEMcGqi6Mr1vFfBQORP0INz1AHgguzXCjkz-lS2VsUTHJI80LeldWFAWSJWwSIwnWxGx1FmBpWVrbZajc3WpQhJ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
شماتیک ترکیب رئال‌مادرید مقابل رایووایکانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106298" target="_blank">📅 22:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106297">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇪🇸
🇪🇸
🇪🇸
یادی‌کنیم از فینال سوپرکاپ جذاب اسپانیا در سال ۲۰۲۵ در قلب عربستان شهر ریاض!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106297" target="_blank">📅 21:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106296">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9y2Zeep8K-idvFNNW1JmJTLWSXVx4PjtO8DLtBIZApykY4bjDSGNIHmOGJtL8WRXXXoYxd9VmSyX-Z9KXzeHmyUsNwGq2IAT1ns91Flq4ZPosmaCwknsqLDlhh3k5zyQCvgR3-uC6RM0kMRIDttTSFGD--XVHTtMeCKt01OPO-Pice4scabtux5yNVdibXA2PwBXNxIoA7Gr1VUNEU11_KWTAKFjekv7Qf-Cf1fdhWOONuWwt6oPgzqls6Ealogu-DyWuDyxeXMsUP3RXjTv__3JQyGIRN0PcKMq4sMhlgCAL0-nnq0YKfvz_HkkLMozM_YsOVGlQGL-o7HRmgtUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇮🇷
🇶🇦
پوستر السد برا بازی مقابل استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106296" target="_blank">📅 20:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106295">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prLcow-zqKTfqp32qrD_alV4D2Di7UOJTrNzg0zbPzwzX3dFJ0F3igZtlqWePqOzOKYVw56fqjU520Yn7Cwqgjn0MIymEw_S1zUNXrQ_mREyoF9KzjtX__b9D6RwEy6Q7_EN7USXAxsNuSA2YaXgxRPoerGTQPLm1eCCffKA81TgxikgE7TrRFQ5WkPPklt9avVDkllHZZvBKKLvYbYkCOgtUkbvG3s6DxZYn1FwoVnrD7H0l5amGwSYrsX3kkh1PfqCfa0e7zFXr6e_9_hRjn_6kAiFN8YlTUftz35X7ZmqEVqfuhqCxh2MjVqbBMPBWzk0eyIl5NL7Tb590iNxrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
😱
قیمت PS5 Pro در ایران به حدود ۳۰۰ میلیون تومان رسید
🔻
قیمت کنسول PS5 Pro در بازار ایران به حدود ۳۰۰ میلیون تومان رسیده؛ در حالی که این کنسول هنگام عرضه در ایران حدود ۷۵ میلیون تومان قیمت داشت.
🔻
یعنی قیمت PS5 Pro در مدت نه‌چندان طولانی تقریباً ۴ برابر شده و حدود ۲۲۵ میلیون تومان افزایش یافته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106295" target="_blank">📅 20:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106294">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhtvBFAH4VWCMizG3zP2i_8EQAlF38FxJAZ7zwi2RDGbUoeTGy48buu3Uo1_C2eLfb9FSabC8UScJ8emrJ76BagQMOHHiPEShRmy_9ydIBQ2Fl-QiBWtlB4gPQM5iQ3YPTpgb9oMaJj4pPAqJmJI0e3qRHWBynIt6SWqGEgDczYA5nLA_AeimIdUAcfPdoXh9pVubIyjiI4DJ1BlUaJGUArfZwMLiMihUWAvK7Uf86kOOYUy9UQlnjWt8m2y9-dZmabnR6wcUHySw5nmTiuFDjDReUITttzq8tWuBJdIg27n2YgGLlLBxbw4aYx2zO3B28z-JYiRCXQiXMRGLJck2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
ترکیب النصر مقابل الخلیج با حضور GOAT
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106294" target="_blank">📅 20:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106293">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BG2tfRsft7igP7skacLzh5DF5REWVAZR8zdiVpL9YM35mqifDbmJ5PlDJfd_vcbuH-0crLKekL15ckWKM9F-CpOuWyx322b3kANgu3_Dd21UIPpq7fboTcjtk6KMfrD9BVV8BaHoG4vo91ayY7FO4YZmtXKJId9r8jkUudE-Y5LXF8U63oKQuJTZtUvLsFtJnF5f8zJb88fIBcTHrUThzHmS7yIPnKynlF5YQeZGyzT8SnNBzPgw_trBP72Ywlq079UNKbk1e4T46u7Q8cqle-NLySFZwEZCGzYNjS7zPgeFsGLCZASm_E3q-W55cEbFZpiqYUoFOlZPzNHk-_Gk_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
🇶🇦
استقلالی خبر جدید براتون اومد؛ مارسلو بروزوویچ از النصر به السد پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106293" target="_blank">📅 20:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106292">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✅
▶️
صحبت‌های‌جالب یک‌بانوی ایرانی شاغل در آکادمی باشگاه چارلتون انگلیس که بسیار شنیدنی و جذابه. حتما ببینید از دستش ندید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106292" target="_blank">📅 20:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106291">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/045726ccbe.mp4?token=P96ju6vZU77apxEmRyR3WKf_vUUb5abeui_CTe1qi8vYzE8ra0qMokIuVA4f_nXtlzdkQ5dq2WoZiPdFr_-7Gd2tndKTWu1zvSj9yADDEbS2z6-VeuPRHiZJ1Fw3Vh7AozlSycijbLMH67fEtrLrLKeCdNeF_Q0PX3qVoaoKsjxlTLRTArzipwOa-zlmu-2gr_C6LqeOqcJtSLTN4FmRwPmulHoYAT7Jf8CaTLxtC_iQMtCIkRFDgpGvjCSNaoy69-J6aNw-NJHQFGD247sTVLlYvHxAtzw6BHoCjjqIHJg_P3VpPYE0pXQbh-FivH1wedxwkDBt51AfzUIofp0u1w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/045726ccbe.mp4?token=P96ju6vZU77apxEmRyR3WKf_vUUb5abeui_CTe1qi8vYzE8ra0qMokIuVA4f_nXtlzdkQ5dq2WoZiPdFr_-7Gd2tndKTWu1zvSj9yADDEbS2z6-VeuPRHiZJ1Fw3Vh7AozlSycijbLMH67fEtrLrLKeCdNeF_Q0PX3qVoaoKsjxlTLRTArzipwOa-zlmu-2gr_C6LqeOqcJtSLTN4FmRwPmulHoYAT7Jf8CaTLxtC_iQMtCIkRFDgpGvjCSNaoy69-J6aNw-NJHQFGD247sTVLlYvHxAtzw6BHoCjjqIHJg_P3VpPYE0pXQbh-FivH1wedxwkDBt51AfzUIofp0u1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔵
گلزنی گابریل‌مارتینلی در بازی امشب الهلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106291" target="_blank">📅 19:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106290">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1_g34ct-CQ4NOdVN2JIspdJGkIrG9sUbkAK-cKtj3UhRr0Rk3D6LaHn0en5R3zbMK7cqr6UUfnOCUvy46mMyYsG-3U4uuuWLNrRyNXueIAu1bfbNEsPYE8hpSh2hTjifbFPvQTPsfIYMwAHQVevZcGE12B9B5DiUXccbu63pqOEH_QfuAKu-CFON1vpf5Whyb3khOLOTK8iqwqjsrPRGAQTn2Zu8mR8mIW9subvyedJvFnAOhP8TAePy6rdMku8ga0S9XXQGV8VByLAgVrOslYYm_o8nrxlfpFcUK7T9GNF4pgha_HqGjSNjQW1Ys0dv3q_ZW26f7lhFxI7virIEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست بارسلونا برای دیدار فرداشب مقابل لوانته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106290" target="_blank">📅 19:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106287">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41e5692356.mp4?token=Ku8iMYOruJz0neukEsxxluC3YPU60fIhUwsqnGkiS9OBraWIySZGgECNAG-8SB4rWqtIryhBxJo4Q_6GYMaV_rw74kbczI5m3kgc4Xa1_29vZ7ANOhWsc7IQC6OL2jqjtIKX9tnL9A2lm9A9wNT8-qe74MOp5I73eg3vRIFjHJ0GmoUJYdjYV486SfNiHLIsp-7bFrYIkE2E8QJ0IXf-MpM3QRxn-c214pyyc5eqm5s8J9tlFb1N9VvuuDZo4TrUrK2pgjKxKKs_TM4df8GA6XrBUefgMSBcDjFHb-Cfv9eB5wFy0p-07U77iy0qtXQ3qyAS9F_TufQmosc9QurOEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41e5692356.mp4?token=Ku8iMYOruJz0neukEsxxluC3YPU60fIhUwsqnGkiS9OBraWIySZGgECNAG-8SB4rWqtIryhBxJo4Q_6GYMaV_rw74kbczI5m3kgc4Xa1_29vZ7ANOhWsc7IQC6OL2jqjtIKX9tnL9A2lm9A9wNT8-qe74MOp5I73eg3vRIFjHJ0GmoUJYdjYV486SfNiHLIsp-7bFrYIkE2E8QJ0IXf-MpM3QRxn-c214pyyc5eqm5s8J9tlFb1N9VvuuDZo4TrUrK2pgjKxKKs_TM4df8GA6XrBUefgMSBcDjFHb-Cfv9eB5wFy0p-07U77iy0qtXQ3qyAS9F_TufQmosc9QurOEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
تفاوت صحبت‌های چوپان قبل و بعد جدایی از هانی‌رامبد! نمک نشناس هم که هست ظاهرا!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106287" target="_blank">📅 19:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106286">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArT_HhR9go0-E5ZTghcDvjx-iAMGxa2bPzw0jw5fTuJWBlxoo2xH52o2mUy5E6mF9aJDZw6s8yVNk6_93o4bjIcePhfldxq5kzb74frIBg3mvYDCXZjVTBKa3dAkMnsJg4tUH_5KliJBOduEUxFHDy-j23zanM7l1pttZ2u0j3dfiUV0r2zaHsqRZ2nRUBWeou22GSvhF8pxQY9V88jlLnIGKNpZVfMnKnLWF25sJ85Fwrd2Qemdnb5LozO8RRjLHtrj0nSEVGWgQYCw0zUH8_iaKx_opNj-er-nvhG4F9Y5Al9-V2v_7Lw6Sr4zbPvHnes0nGgtzaTvJahBqG27gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇺
جدول بهترین‌گلزنان تاریخ لیگ‌قهرمانان اروپا؛ هالند و امباپه با همین فرمون پیش برن به راحتی رکورد رونالدو و مسی رو میزنن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/106286" target="_blank">📅 19:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106285">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90c64420bb.mp4?token=SDnlPL1S7YYoiQy94ys16TE1takEaNzx2HPhAwScf1-dHI5TSvtrYVA8xGJCrK3UAlAWOj1phiop9byxJ4X_3IK9D9VkZ5a0dsV1y1HphjsOmmBQwyDCUe-9jq_YZ10bTxjRnCjjXUoNFGffYs7Zem0xvJ6-7_f6FOVEELiR1BfVbUvBUto4vFZ1Um8Nst77oXd9KUNfdcFmNmwdeYP2m8mir5I4LQTXLpXK168PcVVxxDBr_fw-7rGUASg9lnDjkxgqEWjnVW4c0S6yX81uf73g9j8IA3W3eQ7_scdE7CsKVisi0eabAma8GOSTNmObSJwkHNqU-bMnaO4W-guT4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90c64420bb.mp4?token=SDnlPL1S7YYoiQy94ys16TE1takEaNzx2HPhAwScf1-dHI5TSvtrYVA8xGJCrK3UAlAWOj1phiop9byxJ4X_3IK9D9VkZ5a0dsV1y1HphjsOmmBQwyDCUe-9jq_YZ10bTxjRnCjjXUoNFGffYs7Zem0xvJ6-7_f6FOVEELiR1BfVbUvBUto4vFZ1Um8Nst77oXd9KUNfdcFmNmwdeYP2m8mir5I4LQTXLpXK168PcVVxxDBr_fw-7rGUASg9lnDjkxgqEWjnVW4c0S6yX81uf73g9j8IA3W3eQ7_scdE7CsKVisi0eabAma8GOSTNmObSJwkHNqU-bMnaO4W-guT4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🫣
🥲
دردسر‌های کیلیان امباپه هنگام دیدن سکانس‌های فیلم زیدش اکسپوزیتو :)))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106285" target="_blank">📅 18:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106284">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/833fb28b6e.mp4?token=Ad_3KQ7H1WAVt_buaKUAf5pW2tockc1P-6Kh-TBpoN7YmQcYxZxKvaVNj_J7qpku6yLqOwsS5E3hJ1xYBGrUMbclD4vv4PFUEM_-o-SvnZHRcTeRNV4yZLIxvM9Th-cycwxsEj4LFncau6_ta0Yp_KV_AGBOccSJ3T1FEEHVQuCbDx_kJGAzvcDXecjAPu4Ihr9YCcXDHd6RjSztakMDI-mj1j9mJ1Zd-YxDnbEg-SlH7UQbpjSBCerfrNJG98g9YJzOAW5G1CYoySIunP9l8UYBFI072sqbn-svAxvjsfMQjFz7xwaczpmrL_JuA7q437sRHh-aUohYf2LlwYWzoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/833fb28b6e.mp4?token=Ad_3KQ7H1WAVt_buaKUAf5pW2tockc1P-6Kh-TBpoN7YmQcYxZxKvaVNj_J7qpku6yLqOwsS5E3hJ1xYBGrUMbclD4vv4PFUEM_-o-SvnZHRcTeRNV4yZLIxvM9Th-cycwxsEj4LFncau6_ta0Yp_KV_AGBOccSJ3T1FEEHVQuCbDx_kJGAzvcDXecjAPu4Ihr9YCcXDHd6RjSztakMDI-mj1j9mJ1Zd-YxDnbEg-SlH7UQbpjSBCerfrNJG98g9YJzOAW5G1CYoySIunP9l8UYBFI072sqbn-svAxvjsfMQjFz7xwaczpmrL_JuA7q437sRHh-aUohYf2LlwYWzoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
ریدمان دیشب داور اسپانیایی بازی لیگ عربستان که بجای کارت زرد اشتباه کارت قرمز نشون داد
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106284" target="_blank">📅 17:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106283">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9242df0ef5.mp4?token=fbjPS4eu4v1OswI9swEZwwLr95H3Ca5HOCdMXcQ93ZBKLabigCGM97zuz5Vz57bipmV93Ou0A2ep31gBbaSSvV1frzzdnTPwdI7U02lJhdBHf0tjvG_GWtMP8303gBQgu81dVmxeoSDAaIgQJskySFI-qchPWIqtI7atjsCVRU11IimipjM2yYYjWJ4YFf8J-KqzjfLF3t-Mw8XPMoQeHp6xAU0KjFiyWUoHh73XfZHOtHRxM-QUfkD3iukaUkC08YkhPgtyQhupYEr8RS7d5Dj4-SSOh9OEvCfotDUp0a4t6I97gNzDWJMU6uR8AziMWRz9P_8DOH_q46atbBHEOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9242df0ef5.mp4?token=fbjPS4eu4v1OswI9swEZwwLr95H3Ca5HOCdMXcQ93ZBKLabigCGM97zuz5Vz57bipmV93Ou0A2ep31gBbaSSvV1frzzdnTPwdI7U02lJhdBHf0tjvG_GWtMP8303gBQgu81dVmxeoSDAaIgQJskySFI-qchPWIqtI7atjsCVRU11IimipjM2yYYjWJ4YFf8J-KqzjfLF3t-Mw8XPMoQeHp6xAU0KjFiyWUoHh73XfZHOtHRxM-QUfkD3iukaUkC08YkhPgtyQhupYEr8RS7d5Dj4-SSOh9OEvCfotDUp0a4t6I97gNzDWJMU6uR8AziMWRz9P_8DOH_q46atbBHEOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
افشاگری جنجالی محمد سيانكى: برخی تیم‌ها در سفره خانه هاى تهران بازيكن جابجا ميکنن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106283" target="_blank">📅 17:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106282">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFl7iztFlnAeGiGnmHUrAmqEg-WxeqeNft9Sa3yUgUyf5KS-ewVV_l-C9Mp8D_kU9hrCwcmkaWokMxO7ctWcFpoarD70ooaYrsWOPuB3mbizYh9FfDh6XmNu8cd5A41mFle4W7t3WJNwgDBDecwdSLp7uIBow-rXbarVk7R8wWEAm3RwZNjt0wkgviLlCjDXKVrMeWddcrUqGpYrIM_vtcAX6ripCjPjue_m9TO6ws_MeCEqZtCpoPLt20JF0PdG5uZMJ2uwvWtx_T1Uiz608YjUyC5uW6cMsqENpyC3L7kfITnSovkiXKalzBLy3kxz4ipox5mzYDH9XBVgIp3v-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
🔥
🇪🇺
عملکرد تیم‌های انگلیسی در هفته‌اول UCL
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106282" target="_blank">📅 16:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106281">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc8b60637a.mp4?token=XA_Mt3W22WuZsosuiH3DrFH81AgkZYWQUvNl2QnCDabWsI0OVcyt_Z_7G4z-FFS26qjhNmW60NRtH54mnzuR8TEyzCBw__5ukxGIfRXTBjZnmzWIq6eSxwrIlDz4l08pSLp0pZBAgmZIehGuIBST0AZNpRS2Z8HoatMI3BfaIfPRlgl7Mqcfgby9FjufZlJ7aNM5DGp-qAne3uTURIX0oZmEJTynyZNkBkdrTr8Zqc4UCsKBQ6GMUm3H7Aq7TJnoo3KYV7gqwbgrNhBDyQvBa6aDwfn3tqL4L9eYGE0yiXH6jeebijMN15iWuUHpqXXfkvARw_b6dzTyhK5il1hZng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc8b60637a.mp4?token=XA_Mt3W22WuZsosuiH3DrFH81AgkZYWQUvNl2QnCDabWsI0OVcyt_Z_7G4z-FFS26qjhNmW60NRtH54mnzuR8TEyzCBw__5ukxGIfRXTBjZnmzWIq6eSxwrIlDz4l08pSLp0pZBAgmZIehGuIBST0AZNpRS2Z8HoatMI3BfaIfPRlgl7Mqcfgby9FjufZlJ7aNM5DGp-qAne3uTURIX0oZmEJTynyZNkBkdrTr8Zqc4UCsKBQ6GMUm3H7Aq7TJnoo3KYV7gqwbgrNhBDyQvBa6aDwfn3tqL4L9eYGE0yiXH6jeebijMN15iWuUHpqXXfkvARw_b6dzTyhK5il1hZng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولی تو تاریخ لیگ‌برتر ایران هیچ‌شادی گلی مثل این نبوده و نخواهد اومد
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106281" target="_blank">📅 16:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106280">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5318ea7807.mp4?token=Zpn4kkncK2Mw7rjXyrCDOKHyFpN9dNvytV4IG21UG6ruP1az4hU-IFv0iPA8GiyJ1kBspZkIOb2y99BWKAjJSaF8QG6GaUiFLvcSqPJ4OGWV83XfS7Y3EU9Soe7dbLeTKQAWVI8ZyzyXyVVPuIWBNCsSfPQyClo-5R8Ar8BVr3HHPGF_OZ5jvE63_iBbLtKVVaun2ltLNVE7p87irQY2HaixQtNXqOM61SOYo7cUpsGWc0ontTe9bMGHHDJK46xomo-3OzgFJLhVmrecjKa82YPd1S6CNCBAHTafA8QCtfqqgchRQG7Imc1xc5HqACnjIjXbbio2BckjgV2mqM82wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5318ea7807.mp4?token=Zpn4kkncK2Mw7rjXyrCDOKHyFpN9dNvytV4IG21UG6ruP1az4hU-IFv0iPA8GiyJ1kBspZkIOb2y99BWKAjJSaF8QG6GaUiFLvcSqPJ4OGWV83XfS7Y3EU9Soe7dbLeTKQAWVI8ZyzyXyVVPuIWBNCsSfPQyClo-5R8Ar8BVr3HHPGF_OZ5jvE63_iBbLtKVVaun2ltLNVE7p87irQY2HaixQtNXqOM61SOYo7cUpsGWc0ontTe9bMGHHDJK46xomo-3OzgFJLhVmrecjKa82YPd1S6CNCBAHTafA8QCtfqqgchRQG7Imc1xc5HqACnjIjXbbio2BckjgV2mqM82wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🥶
باریک‌ترین خودرو جهان با عرض ۵۰ سانتی‌متر ثبت گینس شد! وزن خودرو ۲۶۴ کیلو هست و حداکثر سرعتش ۱۵ کیلومتر بر ساعت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106280" target="_blank">📅 16:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106279">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76c27ec481.mp4?token=Nfk4yjMKMtmFOOQn5EHbUGvrwJfUZ6-EMxLTFKvti9VztdbWv1GxMsONvKMdku73acHIr5viDMIfnRrtBqeD0Y0h0Qm3tf5SePzYWO1d3EIpHEOIXbGJC0vNK_KhkrnzRD6cO3v9wEE7yLVTegJ55G0F8KXoXa_RRSAS_06C1CYZ6stKGEv1V82lHsYeosrKNPSs6w8wVIx77JGT_2PCoKkOF6DFiOFHM7w18fm_Tv_zMQG8jsOunp-7lmLwpUCXTl5Zl97iICNFcdrTiqY7cfMTI0XJwJ-mJ4tAuMTmVqT274Nu6s_Gs_HMwQLnyBmsHqcWvVmUjTB-mntb3qceMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76c27ec481.mp4?token=Nfk4yjMKMtmFOOQn5EHbUGvrwJfUZ6-EMxLTFKvti9VztdbWv1GxMsONvKMdku73acHIr5viDMIfnRrtBqeD0Y0h0Qm3tf5SePzYWO1d3EIpHEOIXbGJC0vNK_KhkrnzRD6cO3v9wEE7yLVTegJ55G0F8KXoXa_RRSAS_06C1CYZ6stKGEv1V82lHsYeosrKNPSs6w8wVIx77JGT_2PCoKkOF6DFiOFHM7w18fm_Tv_zMQG8jsOunp-7lmLwpUCXTl5Zl97iICNFcdrTiqY7cfMTI0XJwJ-mJ4tAuMTmVqT274Nu6s_Gs_HMwQLnyBmsHqcWvVmUjTB-mntb3qceMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚫
🎙
هادی چوپان درباره کلیپ رقصی که در دی ماه از او در صداوسیما منتشر شده، توضیح داد این برنامه دو ماه پیش از اتفاقات دی‌ماه ضبط شده و ارتباطی با حوادث آن روزها ندارد
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106279" target="_blank">📅 15:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106278">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f692d60102.mp4?token=t7_YiMq8-34Y751_h2kWNc1z2wzFNKJnH2UstWXi4K8PbJ2AH6tkf0aCEm2oBhspk4VbvMn0qY-MR44JOCcO3XCIje65LXJrfWkFpknkYHHMp8L7JxcsMbaeQCHVb1xT5GtizBgXdT98sDdBjg8DeryQyqarukX_WpbfRyuwtLBZQqOKDUqy20P5s2riGm_MNrecrMUR4o7CHLMr_xQ8i33FQieFCZVd9FRrq-IDDzbLeieJ5DWVrlxfQ2lWMutp5ywnVaeYSeBxYHDj8jBc4wtJOoI3Le7VEFZWd-3y3bz3KlAj5pCZj6p4t7jxnt6jXXirGg8HTMPIYkFaLjQpIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f692d60102.mp4?token=t7_YiMq8-34Y751_h2kWNc1z2wzFNKJnH2UstWXi4K8PbJ2AH6tkf0aCEm2oBhspk4VbvMn0qY-MR44JOCcO3XCIje65LXJrfWkFpknkYHHMp8L7JxcsMbaeQCHVb1xT5GtizBgXdT98sDdBjg8DeryQyqarukX_WpbfRyuwtLBZQqOKDUqy20P5s2riGm_MNrecrMUR4o7CHLMr_xQ8i33FQieFCZVd9FRrq-IDDzbLeieJ5DWVrlxfQ2lWMutp5ywnVaeYSeBxYHDj8jBc4wtJOoI3Le7VEFZWd-3y3bz3KlAj5pCZj6p4t7jxnt6jXXirGg8HTMPIYkFaLjQpIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
✅
تو این شرایط اگر از اینترنت زیاد استفاده میکنین برای مدیریت هزینه‌های خرید بسته، این ترفند راه خوبیه. برای دوستانتون هم بفرستید
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106278" target="_blank">📅 15:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106277">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb9d15a53b.mp4?token=VMsfB2lLFanWrUr5cwgl0LnoK_BCfgCOWkqu3w5pLHbr6JvYYoyXeuCKkAru7yTxovPwSBJAmb00ETXHCBegW5wIf67oNFqy1DyLlwYMirAlYJN3hGPMl0UfbMN8Wi_Y3LePdwcznArt_wft713oRva7YKQ6Sh4CL3n5Om2HQmeqwB8eKOBoLSBzslKRXmj1VDRooYME9H0wpjIp6wIOvwwL9BglMwHofdHOXgnp5UCg5sYUKYt5ucSLUw9LiYMggha3zoXc_dHaV0a_xp-wJv62KYg5YOBX7mG9Gw5tRq48Oagn93LYdiLTCzDWaSoONv7JgyciDyC8sryo4dZHsSjqOQlo96KKodf2mO4HwCwh-EhyOo4Ot1pPJnJxD3es_bWXQfG6RFQQNoG2wxyOChsUVuJabM_UiPy_1JrYvvvI4voQSbYW3nFhAq4yeAqvekRkd4fosgne71jU_E2ZL-lHuxPK_SWcOIkDV3Tyd_WMCxUVjAYoOGB7Bhg6-1FLlw9vWc0SgifumNFnkxL5U0PPBUxeqR1zMTxypmgcMmFjGj8tybxkJq8z4xOarMI1VK_e4qFgx8IcvP9BLkVUH0VqnxJKQZPoVWTOTuz_bGcIQJi-DTGxmky3NZkUX7xUIde2ocVatKy2fOktrImY9VI6jr5FCNR4JuXYWTbE9Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb9d15a53b.mp4?token=VMsfB2lLFanWrUr5cwgl0LnoK_BCfgCOWkqu3w5pLHbr6JvYYoyXeuCKkAru7yTxovPwSBJAmb00ETXHCBegW5wIf67oNFqy1DyLlwYMirAlYJN3hGPMl0UfbMN8Wi_Y3LePdwcznArt_wft713oRva7YKQ6Sh4CL3n5Om2HQmeqwB8eKOBoLSBzslKRXmj1VDRooYME9H0wpjIp6wIOvwwL9BglMwHofdHOXgnp5UCg5sYUKYt5ucSLUw9LiYMggha3zoXc_dHaV0a_xp-wJv62KYg5YOBX7mG9Gw5tRq48Oagn93LYdiLTCzDWaSoONv7JgyciDyC8sryo4dZHsSjqOQlo96KKodf2mO4HwCwh-EhyOo4Ot1pPJnJxD3es_bWXQfG6RFQQNoG2wxyOChsUVuJabM_UiPy_1JrYvvvI4voQSbYW3nFhAq4yeAqvekRkd4fosgne71jU_E2ZL-lHuxPK_SWcOIkDV3Tyd_WMCxUVjAYoOGB7Bhg6-1FLlw9vWc0SgifumNFnkxL5U0PPBUxeqR1zMTxypmgcMmFjGj8tybxkJq8z4xOarMI1VK_e4qFgx8IcvP9BLkVUH0VqnxJKQZPoVWTOTuz_bGcIQJi-DTGxmky3NZkUX7xUIde2ocVatKy2fOktrImY9VI6jr5FCNR4JuXYWTbE9Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
داش‌علیرضا منصوریان درحال یاد دادن ترفند سرمربیگری به اسطوره سندروم‌داون استاد علیرضا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106277" target="_blank">📅 14:50 · 21 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
