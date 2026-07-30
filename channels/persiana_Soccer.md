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
<img src="https://cdn4.telesco.pe/file/gP7Gih_e1TfWC7ws5IrNMdfbarMNY8CbuOJ2deizAjVUQR_Xjf1bv-PDumnegGfyZ4VMQj20Qatd-PPyMjymY4vmltHDziOOEiW3KbcbA8KPW-WKt8Ap9Akx7pKOo6f6lB_mt2IQLg5l8Whn9ZoW8O1Ya4IPzwAyr4PVD_80QG2uKe8-JQ6OWjO3buC9-nZ3C7XV45n-8uxVnLv_Z5UzwwhjoSue5B9uhlrSZbQTDbXx-k-4f0N6mim2Hjkwlfy7BpywY9FseToecF6-KMEM9abKQaYGCcQVtj5ASh2TQVO_gNGOvA2Crj2PafftzmqAygWB-4eglPuCgBHCCe3_bA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 609K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 22:22:45</div>
<hr>

<div class="tg-post" id="msg-26840">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POPEdQE00uvwXeMSQ7Ki6XrKUZlG8qViZMyRQX3kW_wO2wmZYrdYhUVW-Q8cWv9AvMjtIDM_b3pqcrUW-g-0afTtv3qW4YNQwDx8sx2FOzjrC9oDlmK5ydtCCZ-pCqtlcdTSnuUZ7w7ftQWv06lATIcBADGUIjnjJDVuXfTolkbbvF2g-AUGb4S5u3uUnFCegjLYN0aatgTwE7ZVq5AKdI9dPkkiJFBqY1zX6KgS-DKHK52pyGio1mt8jRGzbNNnrI8TuQYdtyLzMLLzRcqLSVI61Yj8lCjrKhzYCx5yp4AK3KKZVrKDf1rfkWw_BGuc_GLeGLc7M8d9A3A-l0DLqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
نشریه‌کوپه: باشگاه‌فولام به‌درخواست آلوارو آربلوا سرمربی‌جدید خود؛ باپرداخت 70 میلیون یورو به‌ رئال مادرید گونزالو گارسیا مهاجم جوان کهکشانی ها رو با قراردادی سه ساله به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/persiana_Soccer/26840" target="_blank">📅 22:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26839">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MqS8sRrVRy5vrVYFO8ANhfqpRkWS9p3x3-X4KV1BDmOGaESKaZkXr5edto7gGKY1VQrRfEoTM2sWVZlhXCVX7F75TiwPOn8fU7HDYOgLPbjmz0UmH6tzSiPD326MC2RILGFyGQUe4thglDrz-GLTsdRzsNfbbD7XiSghOHUiSj-u8uyzrYUmn4B5pCv5vaO1EQyQsQIpH6SghFVx4ZVL8179C83z-TfbfBveWFRI0QBHb11Vgx2AkZrm0zX6a3-S5JCFApSbxIdf3oxmiUDQkHXES75NbR4Si_6M1GIdCzmCI6TmoNicd8MWNWseepCky8idqt0JPxBSxCKyMbPTzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان استونز مدافع میانی تیم منچستر سیتی برای عقدقراردادسه‌ساله با اینترمیلان به توافق نهایی رسید. استونز به‌احتمال‌زیادجانشین باستونی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/26839" target="_blank">📅 21:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26838">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4isEYp0s-xZLLlzq2Di7I2THPTywQ-Hb7i9wF45J4TGZOzoeVWSHWi2j3XW8Bc-f5llxw4nSbz5FKxW8gNryA2D4Dv4Et3c701QQ0ucVzmbGNqextyyPY_3V8MjWNu5enulXAPTSaEB1Vj08z0CvkvuveFphgGjoBEXUZPcKG9SYP8wL137q3EkbjbysWZjKKJi0gy_hG2KvVSntn88VHKVGaSWVDUpmXyTNYD0B3RDI7nCB9kjaw8ffGHPkr_7Bddn5E_E8PeJIdnZr78-FsvSaEN68ara5-Pc-jqJX0sApovSAhSmogRYDcuvWdX850MNjry4p3VqlxJuHnedhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ معاون باشگاه‌پرسپولیس امشب با سامان قدوس ستاره تیم ملی تماس‌گرفته و درتلاشه که او رو برای پیوستن به پرسپولیس راضی کنه. باشگاه پرسپولیس اعلام کرده مشکلی برای پرداخت رضایت نامه 500 هزار دلاری قدوس ندارد و تنها اوکی خود بازیکن…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/persiana_Soccer/26838" target="_blank">📅 21:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26837">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDNLBSHn7CqbtP-LJH_IlkL51XrLIDj2vIldPRcc72f7Y6iRcr3nTcOrFRS_RSyN8TmTVvxhVGEXT1bpt-gluq1JRuU-mFD1DHfq7locnaiw7tS_xI3xajtbkfS8ZFbMLuDkryoAfggaqJGEZVPqqsNg_zlAnRZ6IwMJiegsDY3AMKIixAISi5P_hi1EF50OGOna4XFJnANmp2gHtWUBCtLPxrTReqExz4aVVmrReHwx-TI3yD9FTXUSEZ3DN9oDWr1PNuW2xDD1Vw1YCYfI9mkL0Nblq3S6txC81co3loGeHatqn2sRH5oxR4zBHXe-0zp2VVX_p4ZOCBk1i_yzhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پرسپولیس آلن‌هلیلوویچ‌هافبک‌کروات سابق بارسا رو به‌ اردوی‌سرخپوشان‌پایتخت در ترکیه دعوت کرده و قراره‌ظرف 48 ساعت آینده هلیلوویچ بعنوان‌بازیکن تستی در اردوی شاگردان مهدی تارتار حاضر شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/26837" target="_blank">📅 21:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26836">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vgakwr1s6-mQ5Y0r-t8g2SiHGm43u2XGxsxwnj9vRVAPP2E3TLPmb9ZwzzrK0OCBQKvFOXpy6cNIhwVDAXBVjZ-W0wrDn9-v3TYJSpuxFcFe8sUFlP0dHY-d9s4PHR2dD6na1fHRkM6nF9kNzimcGqKo-qNzF9-bYpseCeNJgIcrezh7gn-pS1cCANOEiBpYoRDVTeueQBtFwowcjqGpeGUUH6XzT4AI3OAnO4lprrsERZgT5QAG2lmfm6OuJgAp39w1la8Dme6d51aPkgvEXEdXM7YbKKGmd7QtZxhcFAiTpEZS2OwlfkjKPQ5VRh1ds5_-s5JC-eFMTH3Koo5LqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌جدیدترین‌اخبار دریافتی‌رسانه پرشیانا؛ روزبه‌چشمی‌کاپیتان‌اول‌استقلال شب‌گذشته با رامین رضاییان تماس‌گرفته و ازاو خواسته‌دراستقلال بماند.
❌
پ.ن: دربین‌تمام‌آفرهای رضاییان رقم تیم استقلال بااختلاف خیلی‌زیاد از بقیه بیشتره. تاجرنیا گفته رقم مابالاترینه…</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/26836" target="_blank">📅 20:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26835">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/391acb06fd.mp4?token=fPdPcXiP40f0IPW9Mw_eWKp3MMFbVZL2GfAlLBwHYNLvay4mUxTknh0DUlKGmalqC0mSTwT4JiyF-oxyBBYFISIKbvTksR5qBuDemVWBlzcc7nN-sti4jCcM6TIee5S1MOTvqYO4LWhx83sl7qcjn82WEn2SP1Um8uyQD3gYCyZDglD3BpziiEp_TiHHPcvEU0tfP3k9EUdnR7V33xY-KdEUM_LyvYhCLQQEzhM69sF6lSzNg_5IvRcAMXjqpWsDL8VZASINvz3yipfMKGP8jo98asfalPZjn6tlkWdf2okmCu0Pg9oPniiwQWTTZ9aDGRPk9a3KwVkhj4FFPG8rTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/391acb06fd.mp4?token=fPdPcXiP40f0IPW9Mw_eWKp3MMFbVZL2GfAlLBwHYNLvay4mUxTknh0DUlKGmalqC0mSTwT4JiyF-oxyBBYFISIKbvTksR5qBuDemVWBlzcc7nN-sti4jCcM6TIee5S1MOTvqYO4LWhx83sl7qcjn82WEn2SP1Um8uyQD3gYCyZDglD3BpziiEp_TiHHPcvEU0tfP3k9EUdnR7V33xY-KdEUM_LyvYhCLQQEzhM69sF6lSzNg_5IvRcAMXjqpWsDL8VZASINvz3yipfMKGP8jo98asfalPZjn6tlkWdf2okmCu0Pg9oPniiwQWTTZ9aDGRPk9a3KwVkhj4FFPG8rTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
کریستیانو رونالدو:
در باشگاه رئال مادرید اگرموقعیت یا پنالتی خراب میکردم، در اتاقم رو میبستم و توی تاریکی با خودم حرف میزدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/26835" target="_blank">📅 20:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26834">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwaFqYb5pvwYCpJJqiQg4-q589168mhir3aIVBv9N6gzxOtKmRWdETp0Zt47Om18aQlHGDk_AD1JkagZq1GmLtwUNo8DA1FSzUUpwsVWNfDM4zNt5OVpbn47wZh-1oi6PhRU3h_CbuX21DOsK4hxGsSlzw3f3zASk8HgbfXb6cXCBNBmOvmZU4i8NHEQs221_ABDHrt9Mx01VEkGQMRrtcYi6y2nN2x-pX9OYEE96oISeUP22iZC9nWD6jnmWTRd5JUqvQwj-nDfzUIL5m3X21uOBRrht0ZhWwvtpMm4h7B1iNwQo3buGDuiq1_CmsudJNprfVlzxeiy3uAGQOSPng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب‌تیم‌پرسپولیس برای دیدار دوستانه امروز مقابل آلانیا اسپور با حضور بازیکنان جدید این تیم؛ مسابقه دو تیم از ساعت 17:30 شروع شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/26834" target="_blank">📅 19:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26833">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vN-VoIX_PKsJKYMQnjmk-DJEJN5MjfVjxGB12oMT698r-NF2s89FUcTQ2G0n7Ygyo739Pji1h-IyYa2y0izIqgAh5nzRMoOOECyBknn8PbyQNascpF8GfBrqU6GL1CJ0ytl-20b2AwQlMNAaYsKpsO-QQuEOjFAJwHz3pEUTOGiQq1yi62p3JtwDaWBSk9O4URqBDH9sLf-p8TT7cRbOWcvZUvCw40m7-2TafufHSjRboNKGqreFGaVadnYgjifLTbDTWyx12LNPZ7G_nthtCO-K8nSHSYkt32U9NHCbyRlI8hmI2Bt3lmIuqElDOkp0ng8lxo8WiXG5Ya35VHKrUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌شنیده‌های‌رسانه‌پرشیانا؛محمد رجائیان مدیرعامل‌سابق‌آلومینیوم‌اراک یکی دیگر از گزینه‌های علی تاجرنیا و هلدینگ خلیج فارس برای مدیر عاملی باشگاه استقلال به شمار می‌ آید. علی فتح الله زاده، سعید آذری و محمد رجائیان سه گزینه فعلی هلدینگ برای سمت مدیرعاملی…</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/26833" target="_blank">📅 19:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26832">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdQ5HU6xbeUIQEIYpsqQ63L7jB1yQWcNiTqqPbaCq9iQKl6O2cfqH1aLulBz-6UCaoDhTk409RoC-_nKPE66s-Xs7YrYfazYso9xaJY4hOxOWCgIzX4M9TwvGVjl8Kay4p-5nkfdsnb0_oyVs0AhqY56wj817aoc56NONMkBfk7vp9JAi4_rmRUEUxc_-fW0reZSRit_sAXKKzMsPSqXhwRyUDvtI_phrQ47_9yEbWneESvjsc8yup-H7B03F2h7zMERoUhsbiPP3-BZoD99XmWagB1J0Ykfes9agA5rIZUgSaWUq3Z7Dzu4C6qt2H9kN-WwXrpdQsXSOBs_Xc-f6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مالک باشگاه خیبر خرم آباد؛ پیوستن مسعود محبی مدافع‌میانی22ساله این تیم به باشگاه روسی منتفی شده‌است و بزودی به تمرینات خیبر باز خواهد گشت. رضایت نامه محبی 70 میلیارد تومانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/26832" target="_blank">📅 18:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26831">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2c2e717da.mp4?token=jI3kZ0u3N094ldqM6Gi-7yXKO95EI69TYAx2zzAaEPBQtATswd4epL9Ax0xGBC12s8Eet-buiorwEaL4l8Aw_UurEXriWr0bXQvj4A8uHt4v1hZGVTUtdN_Bmg7XoxKu4rTmEG4aJXInhKpTbdatR5K8JSF2qbqlkpdgE0DWRD_JuRpL7mMH8s-P-OWZn1ERb5kU47f_SHex2gR4c19-PvGL48fMg-4XUOLrESmhI09x2EYeXopBk04R6iI-Hs3wVCxTMQgVdyJllOrhX2PT8pG-gPQOEMc3FjEqMPM8p9L_3X9bKZ0hdq8wI67QPhTVJLzXD80KKwacUnSfj3MgEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2c2e717da.mp4?token=jI3kZ0u3N094ldqM6Gi-7yXKO95EI69TYAx2zzAaEPBQtATswd4epL9Ax0xGBC12s8Eet-buiorwEaL4l8Aw_UurEXriWr0bXQvj4A8uHt4v1hZGVTUtdN_Bmg7XoxKu4rTmEG4aJXInhKpTbdatR5K8JSF2qbqlkpdgE0DWRD_JuRpL7mMH8s-P-OWZn1ERb5kU47f_SHex2gR4c19-PvGL48fMg-4XUOLrESmhI09x2EYeXopBk04R6iI-Hs3wVCxTMQgVdyJllOrhX2PT8pG-gPQOEMc3FjEqMPM8p9L_3X9bKZ0hdq8wI67QPhTVJLzXD80KKwacUnSfj3MgEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
نصحیت‌جالب‌کریس‌رونالدواسطوره پرتغالی فوتبال جهان به کیلیان امباپه ستاره رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/26831" target="_blank">📅 18:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26830">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRtqEdq0qkVD20Wp77paUnkfx_2rFhDb46Ev_jmQigViCpARdI7ZowrVqT0hG8z0ZqCaEm_pTs2LmbO_HeT75fhq2UVNgeLVmeoIU--d4maJf7Dkns2ZAAowJtkvmp9sRkdxYM-g2BkENbGjAEQPSXApI_Annimjqur-yh6F61sPfTF-1mq0hOZ6PTXz4UVKQQF6aqOfJE0zPrWaT_nXt7yh3laD6W8MxtemS27WLUWbwoDQTqy9eG9b1YPD_0ovRtI44i4TItwRuaavqkfQr5NtBS8LKom8UxZ4l9JTClBuaosvQShLkx3KfIszJlcMTyYek3ySBuasBKvrj3gCBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
کادناسر: تمام‌توافقات‌بین‌دوباشگاه منچستر سیتی و رئال مادرید انجام شده و باشگاه اسپانیایی تاساعات آینده پوستر رودری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/26830" target="_blank">📅 18:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26829">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPfxCx_-Ahoxj7VP5BDT8A5fwR5H87T0T6LbfV28CFobn41KOLwtoQ62V8ph9HD95IX_Hkgo8XrQrYUcBiJZYIv0lgtvC6Sz7JFwgO2QZ8qUymp4_de_m3wKimSXtLVSCx97QujTxnBlyy5GGiB-aELjcf_2uQrmAu9BrQE2Z82BWxDrVYd1LTl8766Vx6byaCcyzAGUHTrwoXCj4upIelDGiPchWJTgVD20GW4qzR_vWuA_eaY4_p5JbEpubIax3oMxihLa-mwf7HLYHaO6xVnrzwEVsc0yvCYW5U46Et5yb77GuWClpWxMYbdAqSRCzt3qTodtShCCEEA0ftmxjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه همیشگی شما
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/26829" target="_blank">📅 18:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26828">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeqhjGsS-1tR7VVlei0Sx5M4jKZT5oZrLY9zGwwDnMdtMWR4_PDa0qKIwDEEHCQMVxZsf2NzmnIFsUO1NJtQUCkw79fCYqPyDQemHVCEZkD8U46Mj7QUZtrGI2UVxhg1wGg44p40aUqATGuSpn2CAmvYf5a0G7OdqCfxVJ9ZYeJ_wKt9rSpdPGR9_BF99GOWrVCjrRrmTs-HK-lObDXv0bYDk06VoKsfipi4c5OIPzqM9FI3eQog8FMa85OlquP57K0CdyioLMgLl-8VJN5s_sN9srgpQ-9EYOgW0lpb9bm5_SEWnk6e7AENWeRrNfYCSdKRpd0wnBuoZfiT5qiAdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مصاحبه‌احساسی همسر انزو فرناندز ستاره چلسی:
تو 16 سالگی باانزو آشنا شدم و بعد یکی دو سال قرارگذاشتن باهمو شروع کردیم، وقتی که دیگه باهم بودیم.تویه‌خونه کوچیک که ایجنتش کرایه مارو میداد زندگی می‌کردیم؛ وقتی دخترمون به دنیا اومد ماهنوز اونقدردرآمد نداشتیم و براش‌ لباس‌های دست دوم میخریدیم صبحامیرفتیم‌ایستگاه اتوبوس و اون میرفت تمرینش منم گاهی وقتا پیاده تا سرکار خودم میرفتم. ماخیلی‌تو اون‌دوران سختی کشیدیم و گاهی وقتاغذاواسه‌خوردن کم‌می‌آوردیم ولی تلاش هممون بود که به اینجا رسیدیم‌. روزی که انزو خواست مارو ترک کنه بهش گفتم به یاد بیار چقدر سختی کشیدیم باهم الان‌که‌وضعمون خوب شدع زندگیمون رو خراب نکن که خوشبختانه‌خرابش‌نکرد و باهم‌زندگی میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/26828" target="_blank">📅 18:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26827">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWuiiR5v7JNVv90V62DUm6FBfSWwJjNMNhF5Io5kA5Rg99jN_lG_nL4sAcQK_ANYyJwu5Uu48tz--A8ziOMb1we627xMBXe9gXVpF8lOovWw2Y1w8XPGxd5ovHYQZyMFt5qs8Md8aUHDg5JKszZz87VjuN_JrR_A1VB2uTZ2zP7ii2S2bkATG8hVlThgEMWTdpHffG7grpErgIA_52uQSCA86uxP_9k3Pm6DQyIMjXQ9l9JRZjgLOD3UXINTYnrjblRhr20hGqCBANumqYgooxMJsY7njINWIth4Qq3aBwiK11utfwg64x0hvIRE4JJVnzyszBhJS_tKT5AQGJviaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب‌تیم‌پرسپولیس برای دیدار دوستانه امروز مقابل آلانیا اسپور با حضور بازیکنان جدید این تیم؛ مسابقه دو تیم از ساعت 17:30 شروع شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/26827" target="_blank">📅 17:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26826">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/337c4609b0.mp4?token=XlhnWBEQ4TDWmZwwVdIFOETBKQWE9s2Fyxyzt2HGrA4zcnN-g2gen9UqFLmCZYTozuZ4j5vlIQPEZWOi3WA4vyUn8r5-1UE5q9EjBogzlfylkJib4usRv7a8Y6yVoZC5KANW2ZOFJxwSFwgRXW7k_0_aU6Emsxb8ABs7vd8Ff4ArLsk2YCf5Jkecrt61kZGLqGsJLH5I6xbZJTfHNqW2Pu1vDf_Y79p8NPAp-k4no-xryQws0-MfuMMn9B5kRRZ4BxzJaTRg9A2nWMkbm0YgOrgD68VYf1Wh1IDsZdIPoOKYjK0Zo7N9Jt_jTgFyYOd6mFxL8kif3W2XAfIgPU6ktg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/337c4609b0.mp4?token=XlhnWBEQ4TDWmZwwVdIFOETBKQWE9s2Fyxyzt2HGrA4zcnN-g2gen9UqFLmCZYTozuZ4j5vlIQPEZWOi3WA4vyUn8r5-1UE5q9EjBogzlfylkJib4usRv7a8Y6yVoZC5KANW2ZOFJxwSFwgRXW7k_0_aU6Emsxb8ABs7vd8Ff4ArLsk2YCf5Jkecrt61kZGLqGsJLH5I6xbZJTfHNqW2Pu1vDf_Y79p8NPAp-k4no-xryQws0-MfuMMn9B5kRRZ4BxzJaTRg9A2nWMkbm0YgOrgD68VYf1Wh1IDsZdIPoOKYjK0Zo7N9Jt_jTgFyYOd6mFxL8kif3W2XAfIgPU6ktg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های حامد حدادی اسطوره‌بسکتبال ایران درباره علی آقا دایی بهترین ورزشکار تاریخ ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/26826" target="_blank">📅 17:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26825">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDz7VcMTMIivY_0ieRuoVgg6DCyAY2I2fVk0GJItEPfp5cICzcW20F0G8V0CkZDoT7G3naWMfMEe-Fd_mky6-H2dg8EsZ5qzd5sZPStGSTOvgqrJ-uuX0SyPxzfH4nAwxWJjL9MDjRd4Impy6bPY18fS8ACSAvvBBczItMmNELtqJkYMkAPYs_fSyCjPCi1Exn6jF156gYzsTC1oykYYoNp-mbBRmr0QKRUcup2i1RQUTl5k2mgbMO3KqhF7SL1QpUSF83q_J7plrYFoj81plDuzNrMA8r2VWkEtm2NmT5L8Td481C969HXbyKTzU4O72Hz45DdlAWUMlIJdYuA1nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/26825" target="_blank">📅 16:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26824">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f949cdb55.mp4?token=b8-UqMNwB_RMaLn1_9fNiN4qS65YHrNaS8jXR7hY6hfDfogBTQOQxBQK-fOSwYiu24caVz2ynZo7U26_eS6_Pkdlt5xE9Ab-4m10KSE6qrte0ORNMN_k0J4tbyoZYAwnvDYljWzAymUIZ9t4VSq9fcqMofTJCV18KKXC4HaJBpQh9XTCAFp65UHRcZqsF62-a2f7RmG5kGKzphYKRJTqZd5hhbi5cHYeKehRtEDz7plRfUAM-_sgnaa26EygCTOOiKOT90y3ENdG6hKrYBIIjJalm75UOBNG30twq8CQhSG5YHUgWGs9vdYz0nE0hZAv2AK1gwPkBRNZ-FsVs4s9jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f949cdb55.mp4?token=b8-UqMNwB_RMaLn1_9fNiN4qS65YHrNaS8jXR7hY6hfDfogBTQOQxBQK-fOSwYiu24caVz2ynZo7U26_eS6_Pkdlt5xE9Ab-4m10KSE6qrte0ORNMN_k0J4tbyoZYAwnvDYljWzAymUIZ9t4VSq9fcqMofTJCV18KKXC4HaJBpQh9XTCAFp65UHRcZqsF62-a2f7RmG5kGKzphYKRJTqZd5hhbi5cHYeKehRtEDz7plRfUAM-_sgnaa26EygCTOOiKOT90y3ENdG6hKrYBIIjJalm75UOBNG30twq8CQhSG5YHUgWGs9vdYz0nE0hZAv2AK1gwPkBRNZ-FsVs4s9jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نیوشا ضیغمی، علی دایی، احمدرضا عابدزاده، علی پروین،نفیسه‌روشن‌وصدف اسپهبدی درحاشیه مراسم ختم زنده یاد اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/26824" target="_blank">📅 16:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26823">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKWme0TEH_Jg-8QPA4e9JThdX-Kt6NO_BBH2JIjrpJFlIkEuIgKwDlRXdQRL5DdaeyBwsq9ymEZb3pP02atK7Z0cCEwOApi7koEo2Lh7V2zrc6c06iTZom7dE5xbUYR5xIQTY6DxDISt-Rnpa7wvUuD2538LFSwmTFV_3EZ13111QRn2681mkO8w4qPtMA-CP-h9tAIIuTBcqCq34pzKxqt0sjftlLZGeY38IAuCY3ayi5bU4cgUhI5Nl9DvY20JJuUNuJcOx7Z2P4BkDjGRdjaGdJ51tBOmGhKy3G_HE-XoYIOSV2tg-wR6img9f-UAXYr06gjIih1fcExuRfPEyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدئوی جدید یامال و دوست دخترش؛ یامال: اگه یه دختر جذاب‌تر و خوشگل‌تر از این پیدا کردید من ابروهامو میزنم. پارتنر من از همه خوشکل تره:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/26823" target="_blank">📅 16:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26822">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1HpVsRpDDNDUP4U7KBDjC0kJwcxnZZJ-X4l_zbYg8j4nrVMMBaurdJZJhE3wF5oFptXUHscqplyxKeWvMf7u9RbM_OGH_PC3dxpaXszOjQ2W9X09xz5vMp-MLbKWlWd24BE5Hh8RhoFryUtlVlGDwJzf3LeKpQKT1ye_-HXeB8bOHTko7fCQLDiZXgxTDcKDOnpDK7b5zGn6MvaAMgT21qhaK0AVjxsiLUFC4e1u6ak9mwgI809CfFpTYHIjZ37y_kf8qtrvui4VELJh5eWxItbQvWTwbtg7xDr7HfXXYxRQsXPB1iYrnrC8fQ8mJNZgEyAPKKbTNNY6gj1Wmxyjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/26822" target="_blank">📅 16:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26821">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1d53ae06d.mp4?token=pQZFSC-stVz8UeE-URCl21zQKohkZAiXC5ZMicFqN7ktSZv1UEb4AOHneF8uJW1Axm4jzf9cozU4BddLE4bjw9e8Ta8ZIB8GJY53nP1zbNOtvNt-R3913R28mJZNropuHNXEYTnTAjngq9MSYo2pvyTN5fyt3vICKciP_ZjsV2s2g3OAViPmuv8WlQiRwY3nQ90lik3hsnEad6vwHmr6ZwG2sKSb4bDNw_pHQ3igul5OZLrhXtZ8XZnXpqELohPlFQwtq8cZICPJ0zTZ14WQ5kW8-k_fp76xVSBo_yXPX2HFWwOOhjIJYvf1Djc2PNXMD8_Ql7g4PQuAom1xthBcDq3I_VxNt9VP021Gfi4ueBgw6ySDYgfYTxk8rGTfhQauMOLd7hdXaf5-ogP68WKyUIqtFc98Rq6wctWrxNsFP9k39xRByo02zkm3nU_ouZOo3pOrS6kcJ2VWl5w3PyV0h4PS838bsDWrU9X04eyx8POAaoIEqovmCoMijzoEEzhrYz2zXiAPULGqScczTZ28wT2GHl4Iqx1h5DclAwypXWIj-YoiDTpJ80k5tR2HKYYgSRY8vz82Mvh8R4tzsQqYphjBdRlQXxGyB9SIzHdBKP2AfKoGPE1LRzB8GWUvycfYuo_K9GY6SRyo8jB4E4Py8GX75NkRTbzi1XxEdWvOwU8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1d53ae06d.mp4?token=pQZFSC-stVz8UeE-URCl21zQKohkZAiXC5ZMicFqN7ktSZv1UEb4AOHneF8uJW1Axm4jzf9cozU4BddLE4bjw9e8Ta8ZIB8GJY53nP1zbNOtvNt-R3913R28mJZNropuHNXEYTnTAjngq9MSYo2pvyTN5fyt3vICKciP_ZjsV2s2g3OAViPmuv8WlQiRwY3nQ90lik3hsnEad6vwHmr6ZwG2sKSb4bDNw_pHQ3igul5OZLrhXtZ8XZnXpqELohPlFQwtq8cZICPJ0zTZ14WQ5kW8-k_fp76xVSBo_yXPX2HFWwOOhjIJYvf1Djc2PNXMD8_Ql7g4PQuAom1xthBcDq3I_VxNt9VP021Gfi4ueBgw6ySDYgfYTxk8rGTfhQauMOLd7hdXaf5-ogP68WKyUIqtFc98Rq6wctWrxNsFP9k39xRByo02zkm3nU_ouZOo3pOrS6kcJ2VWl5w3PyV0h4PS838bsDWrU9X04eyx8POAaoIEqovmCoMijzoEEzhrYz2zXiAPULGqScczTZ28wT2GHl4Iqx1h5DclAwypXWIj-YoiDTpJ80k5tR2HKYYgSRY8vz82Mvh8R4tzsQqYphjBdRlQXxGyB9SIzHdBKP2AfKoGPE1LRzB8GWUvycfYuo_K9GY6SRyo8jB4E4Py8GX75NkRTbzi1XxEdWvOwU8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی نوستالژی از درخشش فوق العاده ایسکو ستاره تیم ملی اسپانیا در فصل 2012/13 با پیراهن مالاگا که باعث شد رئال مادرید او رو بخره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/26821" target="_blank">📅 15:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26820">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2998bd2af.mp4?token=Syhj11ecZhLyhLELzi63Wypi7wdb-Ee8ZmcjE--gObq_KrgdAX2HVyc0gqbneCl1QRIjRAhJ0sEyn6s8opW0RUnwtWLKGwASjC1t9puwI_wR9wiCO5oP30rkSJcj24og6fs1xh1LAL1Dk2YKfl_e9LbjgwDkze6VpD8F3S7EZ5phNgShY4iXWXUDI5ndtrRHtdFij9M7GFawjoBkc3k5l02kwQtSfV8xEvmUVdz7RLVSdKv4JBZNLOP3XvifDwvBISuk5bcSIOevbL2IK_Mco4f0B1M65dkN3uKXhlrmg1nkxc35f_7FpKSvQHt7hdsq1ikAUUodchUuzo7Q68OMBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2998bd2af.mp4?token=Syhj11ecZhLyhLELzi63Wypi7wdb-Ee8ZmcjE--gObq_KrgdAX2HVyc0gqbneCl1QRIjRAhJ0sEyn6s8opW0RUnwtWLKGwASjC1t9puwI_wR9wiCO5oP30rkSJcj24og6fs1xh1LAL1Dk2YKfl_e9LbjgwDkze6VpD8F3S7EZ5phNgShY4iXWXUDI5ndtrRHtdFij9M7GFawjoBkc3k5l02kwQtSfV8xEvmUVdz7RLVSdKv4JBZNLOP3XvifDwvBISuk5bcSIOevbL2IK_Mco4f0B1M65dkN3uKXhlrmg1nkxc35f_7FpKSvQHt7hdsq1ikAUUodchUuzo7Q68OMBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارگردانیکه‌سال‌هابهمون‌رکب زد؛
ویدیویی که از گواردیولا درمجازی‌وایرال شده بود، طوری تدوین شده‌بود که انگاراوروی‌نیمکت برای یک صندلی خالی در حال توضیح دادن تاکتیک‌هاست و همین موضوع سوژه کاربران شد. اما تصاویر کامل نشان داد ماجرا کاملاً متفاوت بوده؛ پپ در واقع مشغول صحبت با اعضای کادر فنی تیم خود بوده و کات دوربین باعث شده چنین برداشت اشتباهی شکل بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/26820" target="_blank">📅 15:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26819">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4W2fumHRq5cUrz5IA8jIb-CGoXV5mC1xXmfMHst50SYt420xy3qIHWr7osrg31Rp9naShJRKjx1Uiso6nrGQKwAO-v7270enVKQmM4XYQudmGlH53xQso1oOrIp_hC_2PMcdKmHPaAT7Dhk8YY9p1Ov0khQZfCfG968Q6O8uy4Cp0HVbU1UOaPWP9wqMGUgM4JD5jJjVCdmmmjyLuFMzgNdLuBscWUgbFfUb5ZETg2VDP_BneD83U8y6BL3PNk8qLgElId6BA7JVlGp4gSbxLguONEdXzxSDqGQc3HeCvZr599kwYM6HdCSg0STe1_oFzG6AsYYSPQTocuEKB4HkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
طبق‌شنیده‌های‌پرشیانا؛ باشگاه سپاهان و استقلال باارسال‌نامه‌ای رسمی به باشگاه فجر سپاسی خواستار جذب یادگار رستمی وینگر چپ سرعتی این تیم شدند. هم محرم این‌بازیکن‌رومیخواد هم سهراب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/26819" target="_blank">📅 15:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26818">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhGF50jp9ycu7cbd56G_4H_S8-Sw5pY-b0BlSEET8jkmjI1AMx1NXP5Om02v5S8W7_oRQ9H01n4IOER-HHG-qdYh0oYhVWzW3wRBoFKXrncPKPvVMYguQ5oonlt5wqnaMRSnLrvJfHfYA8NTqcVxZ8s5ZfBAQM-yQI_3MeJkcRvi0BXeO7AzEJZKDGmx_9RIeP-wGjjx9iS6JKfhpa4JbFRTWRAZz7efRXJZ5uLBuMhDSRonbiUL6OANsJZ5axzSRjZcUTm5vMMaVCYQNuryCdZEE6wgxrGjPNZYHg1Ooll02_GEUx_1XMOAJG8IXpK9XL7uDm4q0Lk_bv6WqMSlzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرط‌اصلی‌باشگاه پرسپولیس برای قرارداد با ستاره‌سابق‌بارسا؛مدیریت‌ پرسپولیس با آلن هلیلوویچ گفته که‌مامشکلی‌برای‌عقد قرارداد باهات نداریم منتها قبل‌قرارداد دراردوی ترکیه بیا چندجلسه با تیم تمرین کن و اگه کادر فنی تیم اوکی داد قرارداد میبندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/26818" target="_blank">📅 14:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26817">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ax5TwQhfiBtAaurLEcFU5J7YwVToA7hygV3yuUqqyfvwBbdaxwDfEE04XKtGBatwcXndzYXnD2cd_5gAwpx9vA4f2bXpr-v2hO6LsQiqjfQ5Va-180sfNmVxwcmPuP3Q1O3m5IBqwNRrUfiQULX0hoXmgUITqrRthKQqb6nNwRotQAjJT3F64GX6EjUKPqb3kuGBJiHNuZwDn6N6jy-iJlQCJ4IgnYYFaxzpyWryd8qI56f3lp0VwtaHigrpA8gM4QneO2ejghjYvj7I4Y0raZDuvn41114hA3BW4W0twpq4xqyIL-eka0b9s3cOGyoNiBmtyKL5VHCAsuIVxVAWng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه نفر راموس و پارادس روبه‌مبارزه دعوت کرده راموس انگار بدش نیومده و پست رو لایک کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/26817" target="_blank">📅 14:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26816">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fvsq_PqlYWkSFU142De9mrVd19dz73UXQyLk-RHXKxtWQ_mni4VinjAUOTI_-whrEA1_ngJ_cfRpqW9mHKwSSi_lkb2TlJo0ly3QLFpxqGQmjqircElMwtTarKX1feucjAVSTSf9QVlgpjeWCXuq_-Gg3QagVQYot7CfU_UeSnb7a6rfPitScvkURXKnBEZZ9qiGxV2M9bXSl432RGOzxUZ8hI_pQfqFOI60Sp6nl7hJRMuxM7gkGnUY7T_--WcMMdSN5KMq0HyPdgLyoh-I8-p3mVhCF9d42rqEpvelp199ZdVBxx4G7hOOgZvQMiip1glueJsr2WlblXa1l_Ydmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بریز بپاش‌های چلسی طبق معمول ادامه داره؛ بعداز جذب مورگان راجرز بارقم 137 میلیون یورو؛ حالا سران چلسی باپرداخت 60 میلیون‌یورو با عقد قراردادی‌تاسال2032 ماکسنس لاکروا مدافع میانی 26ساله باشگاه کریستال پالاس رو خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/26816" target="_blank">📅 13:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26815">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4ld94ilESsDqG4MfwlMjKWkRyFdR4Io3mxHVnX0E482NuEqIu7rZWmB7WG9uouvBNywXCOkQraqMmW6Q28-DYwyyqh6-tQH142stsrsAdYriTo5qoDjmzy25Ajk58oXvHmLcqob4eGWxXO6rRjXfEGUWBQ4uvmv7meVCpeXgz3_t55hBWqG2ArPR9TYD3xBJlDV62SHBWVubDpNsxi0WVh5bAqbVpkl1ekYXdyW8Mz3gK-TgM4OiM3DszfZoFjnSyFb2WdGbUrfvDiOUWZcAd-FiF0vzL5VFfnfKyK9Famea5qmdGAEUnrIbW-ohiIUCwfRKO3cpaMaZRnp_uFnFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛روزبه‌چشمی‌کاپیتان‌استقلال ساعتی قبل قرارداد خود را به‌مدت‌یک فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/26815" target="_blank">📅 13:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26814">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNJUwjSWx7IxA64IMU_-N05J-3WFsKAS1TCwtxnPTATNtkyxXTECbxiPu-xtTCwa58hreidLMS1FhabYYp78hbVOMRolUvZX_4u3YhIvk8WA_HXsQWvk4tSfPA_KCc-ER72h_nFWAYSxlJ_5zcDgz6jEsNCYTrCSlBdAHaJVo5sMSlO2xi11ba6fnp-kIolx1-vATR8hf_sqo8I6qFAW3C2RRJnXuYUzq5wt0LyQa_WxjG_7T9BlxcgAI2vP9tCDBV3Hjvp70KDOVkJ6fKrV1leP61ObPh_llwQRhd5b3CYxxgHZH-WRIS9CBVUbMGpXdMud-1ISV7G3sxuIiC6ZaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه اوضاع کشور آروم باشه دیدارهای هفته اول لیگ برتر روزهای 23 و 24 مرداد برگزار میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/26814" target="_blank">📅 13:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26813">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeqCHsVSmKcwfef0uuAfsyFAN89AmFOEDyXkbeieSqfhqe6Shy6iAieDcrxdALYIJiD0_y9y7hxgmHBSLsCLBdbGfw7PZEaU97bXYJa6ZZzNNz7pLXlmreXIcHiZQC98GH1ULMmWlimvanFblUsydykJbliUbo3xlvpoRoNsYPJD1DGLfFqgL1LFh9rZIXlMl08kndKozqfcy4Flju2B357xN07oF2dPbFsfRwQf5Z9yGpajf5nmaa_zAd5upWA55pNa5KtHrwL5Ky8Tzu3i2H1dBaAM_8eawMbMnlKkwGcoZBGofHcuRrMsZ00lJadZ8HKcpUnR51id61EvPpfi9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ آلوارو آربلوا سرمربی‌جوان فصل گذشته رئال مادرید با عقدقراردادی سه ساله بعنوان سرمربی جدید فولام انتخاب شد و در فصل جدید لیگ جزیره شاهد تقابل جذب او و ژابی الونسو خواهیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/26813" target="_blank">📅 13:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26812">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_zVqty7OpBMxPod8TM7LOLu6TH5agcQElx66oUHF70rQc9rinl-LNM_NwR8qKYCMX0ptzlrIkUYGhWg2YNZ7QswzWBbNw0j_NMZSMgT5zhRy9Ng_oV5X7IimxEzvU7y4W160t65lLyqVWQrplNmCnMj80GttzJr2qWBWGd9eKvH02InGYyOS9l5a64JZzcTx2RqpNaZE5WWsEdSkchMKDsxL9f25kXldK_8bpFjR7Fhj3_q99DrwHOyGMaLE0eQLHm-wlI27VW1AyGgNwAXQXo1O1AnEN7pb3SH-sHuAomsLj4suhgHQ_uLYANsqxkcsOKKGzYpu48D8pjqOHJGOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
"بچه"بالاخره‌کارخودش‌روکرد؛ باشگاه پیکان از عقد قرارداد با جوادنکونام منصرف‌شد و قرارداد یک ساله باساکت‌الهامی سرمربی سابق تراکتور و نساجی امضا کردند. نکونام دو شب پیش با باشگاه پیکان به توافق کامل رسید اما تماس های محمود رضا بابایی باعث شد که قید قرار داد…</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/26812" target="_blank">📅 12:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26810">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEoujU2QW28HpXPT-yPVJcOzLixNW1Z10eTvA_th-lo5rc_971i9-2ZubA_Daxn39lCmmPQnBz4h1uTKER9eqHuhfZGj69REVpajqmJIPbo7AjP4A5cTaBfEVB8ogF3BUeIXadTGpy-P-VFdAJBs5bC8lRjGkepuBkPew-iEoWHGxtuea32kJG3e9fsHs_Hroi2IDHGfdagSzacfBy4q522GGCDxrLGJ4PJHezDkWJ6c-xVBdSqSeQLQDzN0FGkaPMjjize5Hqdpb47Kx43R-Swjrx-icokMQWDax1FP2aenEUNB-rtzyJq5B38aWvNnPqLHknHU8Z63xAP3HCH_4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقای‌اولیسه‌بازیکن‌بایرن‌مونیخ‌هستن در تعطیلات که ویدیویی ازش وایرال شده؛ به قول خودش اگه رسانه میداشت حسابی دهنشو سرویس میکردند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/26810" target="_blank">📅 12:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26809">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7vZombwTJZvayKQ7KQs9Jv3LwT0RbTPZrNG11zVVdBRHuKL-JfxBiCfX5MK1vDtHaXX7oJJc2KjeyR6XWPnJZtOmzYuT7yIVmyZ1riKLcE-PmWV1ZAoRJDQ7h9NBppEaKWHX_dIS6lgG2Sujo0A0n9zgqjblwqd-CQOvkNBWBvRCsonHsm8IrJImNT_m1P5Y3ECGKBBYc5_BzyYUhklfLzFSFzVkeRUHKZMbLPTUbsvI1TTbmWwYn8qxAXBorBNTa5Tol6btyv-lZy047BZp_WyLA15pjcguOtLVJXI18ltsex_c_FEWn7tm3DoDaK4dAew_20KEETabDQDIbZsKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مسعود عبدی مالک‌باشگاه خیبرخرم‌آباد: باشگاه پرسپولیس سه‌بار برای‌جذب مسعود محبی به باشگاه مانامه‌زد و مذاکرات‌خیلی‌خوبی هم داشتیم اما خودِ بازیکن علاقه‌داشت‌لژیونرشود و ماههم به تصمیمش احترام گذاشتیم. محبی راهی روسیه میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/26809" target="_blank">📅 12:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26808">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmBXiVSnDKqMYhlnCCM3WhmCWu1dT0EXB3p3Wbw-EK2jV2f_0-cKt0vEKZ4xfmiu9VPSVhUjq-SaS-yG6e7gBIpB7IJeabMmtSNQzCsXGJeo8S5-K26fkToVQskkqdmAonss9GaFiGTiYbCHhM_PP92UG0RzDtT1nuf4oJDrE7RG0EMs8MsPabMfG0M9ypGWA5212DGp0wg0tDQ7FrNeZYhDohVFvvqjbQFBLdWkOmjWPuKhQUV3RcGeqwv8Z7nP8skwhCrRpe-3t3h192WUnUKeDRm12MLRPFcmykAyjtafgEsJda4Hj46dBDS_55Yjnc0h_RjaFOjE_iKq1KtMPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇲🇦
سانتی‌آئونا:
ایوب بوعدی ستاره‌مراکشی لیل درآستانه‌عقدقرارداد پنج ساله با منچستر سیتی قرار دارد. توافقات بین دو باشگاه در حال نهایی شدنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/26808" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26807">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a69d4793.mp4?token=XI6K0VihnJBbTzpgRavkj46ov3aj_QKjA3Ep6KNXQ02ml1J8d1MWCcwcWboJpUtDvXY5iSvjAnRJFb5TjQDfEyBQ9cmZoWV1gikzi1YOeGkmbsZR9242Z00RRZRxnzciyupndvrn3DcQNdPF0h_nFMYfF2IFWjt6aHFsi8KwTQ6iy6g09LjnWZfAZhnDWqQi9XJZb6omUS8O2XAXaQzsUUghNHJfbVFSuI1ZQbz3RNYh5FRTfgBIHF_o8REMHMBgem6SKPXiTOnGzPuL0nFi0J-AmfdejsrIA9yJXOf46yOWbVLvRWB4XiQk3z23iNnA_U9xJ9FHkg4gF7oCBp233g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a69d4793.mp4?token=XI6K0VihnJBbTzpgRavkj46ov3aj_QKjA3Ep6KNXQ02ml1J8d1MWCcwcWboJpUtDvXY5iSvjAnRJFb5TjQDfEyBQ9cmZoWV1gikzi1YOeGkmbsZR9242Z00RRZRxnzciyupndvrn3DcQNdPF0h_nFMYfF2IFWjt6aHFsi8KwTQ6iy6g09LjnWZfAZhnDWqQi9XJZb6omUS8O2XAXaQzsUUghNHJfbVFSuI1ZQbz3RNYh5FRTfgBIHF_o8REMHMBgem6SKPXiTOnGzPuL0nFi0J-AmfdejsrIA9yJXOf46yOWbVLvRWB4XiQk3z23iNnA_U9xJ9FHkg4gF7oCBp233g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نیوشا ضیغمی، علی دایی، احمدرضا عابدزاده، علی پروین،نفیسه‌روشن‌وصدف اسپهبدی درحاشیه مراسم ختم زنده یاد اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/26807" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26806">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBIEBOR0qy4ny9MvDcJe2F2fJhoK02bLWjlRIt87zslVjeG37G9owh3RAnKb-aL8hNlz1S9CfmSANJoJui7Uvqnt7r7VD-GGCp1r-BKixDM0I-m06Ehr1nwlxH6UqN93HPaah2--7Qc1jnl8LyP9Vt57Vdhp6O5BbO0EztkZ7Ty-BUZlFivilPbjkQ8-EYrJK6hGhS4VpFvsz7zHgIia8w5S-umIfJXQ8lNi0T6dGCt3w-Wv3asde2hHpE7aHeU_XvXM-qP-CBicaoCle-BYqB1safCKGSLTrOQPwlMavYePCfW3SvZysCImo_b8zDErLL0Q07rCWXyhSkw7Y7BFPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐉
توام میخوای به راحتی از فوتبال و باقی ورزش ها دلاری کسب درآمد کنی؟!
⭕️
پس همین الان وارد کانال
Evil Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
💵
اینجامیتونی‌روزانه‌درامد داشته‌باشی و سرمایت چندبرابر کنی
🔗
آدرس عضویت کانال vip:
https://t.me/+TmGWkUYH_8c0OWZk
https://t.me/+TmGWkUYH_8c0OWZk</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/26806" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26805">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0PrpqWZKu1mLPv3lxU6cAmAk9O6-LSyNpx_qKCs0V7hLogWJgR5JzUNKONW_1QnEnmYdGCWyHq4ZtXoHEDgqoVChDULTuwFKcK6HcrqMwQ5z9f89aTofE3_GYpCLNupQUJmN-8JC7e12VnSx_RNoHcmLO-GX49V3Q6wjYHu_ff4mFfH_MDNNwDB47c4Qexd5-EWixvmchKSG0FwMiNpXFrD-964EYClpnsK7D9uDkxqi-5fQ77Kdg4jIfS1M_nA-Moo0HxX63uoD4QU5l1wvyQS8wtpo6kD-YSPwqWnJpwPaw64LzhPKhVwQXLMw1UqyGkjG9h0LAMIrVBjGLkL4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
طبق‌شنیده‌های‌پرشیانا
؛ باشگاه سپاهان و استقلال باارسال‌نامه‌ای رسمی به باشگاه فجر سپاسی خواستار جذب یادگار رستمی وینگر چپ سرعتی این تیم شدند. هم محرم این‌بازیکن‌رومیخواد هم سهراب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/26805" target="_blank">📅 11:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26804">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ple3gSemwVfU3UjSdgxS4UvTAm48R8c54wThlXKU-GM_wa5MrnKlQbyPjM8g68jKO3OLRC0x8tijFxze_sfomRnBEWG6SVM6MgiEmuB_z-sJbNnwiGZ8c99KMDJt5xjFnK2N3LisUSVLWJS8YIc53HPGBAoqwAV6NJNhn5C5qDF29IVN0f3W1whD4Ks_dWRw0JIxbjCQ0keTAFi0Y7AIBtnEdK3A23EHiO9ptk71R9Lwu7lfzLj1mYdbsSEdWqk1ELqQ1eDoNgHn6TqKsoEHHtTWRa3OZ8dhKmnRgh9UxWqz57oOnRMLD8NYFWCoMXBRsjEX-ItJhGzl-IsBCUgLEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
با مخالفت مهدی تارتار؛ باشگاه پرسپولیس با وحید امیری برای‌عقدقرارداد یک ساله بعنوان بازیکن به توافق نرسید و به این بازیکن اعلام شده دیگه در تمرینات سرخپوشان پایتخت حضور پیدا نکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26804" target="_blank">📅 11:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26803">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‼️
ویدیوکلاس‌رقص امین حیایی سوپر استار سینما وتلویزیون به‌همراه پسرش در فیلم جدید «استخر»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26803" target="_blank">📅 11:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26802">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KN4XLSHvtvBLsXKH8UCu2yhZvaggDImoB3mDvmvLc2TjQ52HdlK6jNHBc3NYqycm9bVS0szv4Xm8B2Fj1k-1Jw0CWoGfJyK3-2Zi5b8WmMmO5YC5VX9naIFYXI3Xg8C_aOb1RzyLMgEu51Tq98fV1ydRcgqnepcvALwuoX2XtJ5MNsFdlySi8nPROIN5XIYnxaPZZEL4Y-s7y7Kd6JBfAcMbZBwRuh0Cz9zPVgjMf4K1pzo0uDb3DL6wj1jmii-TasdRm1thkKylS2w25IaBrH3BIEc2araDnws8z7c0ra9KeFrNtwK-gh2CVCDctWhyPCAUQ_V7ogYKhyrOFD2Grw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریه‌مارکا:ظرف 72 ساعت‌آینده‌انتقال رودری کاپیتان تیم‌ملی‌اسپانیا به رئال مادرید نهایی میشود. سران منچستر سیتی تمایل خود را برای فروش این بازیکن با رقم 70 میلیون یورو نشون داده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26802" target="_blank">📅 10:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26801">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78462fd8c6.mp4?token=q256eCaGcVlmd7EbtB_5KeNY2KuWs9R4-KrybX7sLMvjwrHw-tmnL73hICFnVgB66QEQUehBQ9WX5E_lZg_w3cb7yZ9M5pq7tXKtOlShFsmuKB-5QkhzW_wLywqbNGEFRPS9qhjBXj9UIDiPc5CosC6IzJEvt8P8NFuI68LloT9HPFNJTyTcoHG1XoMR-xyTFO0Ok6wJO1r4t2tR_NkOZz93Jcqnb6ZIh0lI4KsRqAAdVIQjNpr4hfDsG5_x6ftwKuBWBORyGiAu8KQUBJeBnip1OLZi7tKK674VetDMhyjdjSF458JhBQCT_Y8qmDwXIZ5DVKRI7Y4Ph4PQYQNPCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78462fd8c6.mp4?token=q256eCaGcVlmd7EbtB_5KeNY2KuWs9R4-KrybX7sLMvjwrHw-tmnL73hICFnVgB66QEQUehBQ9WX5E_lZg_w3cb7yZ9M5pq7tXKtOlShFsmuKB-5QkhzW_wLywqbNGEFRPS9qhjBXj9UIDiPc5CosC6IzJEvt8P8NFuI68LloT9HPFNJTyTcoHG1XoMR-xyTFO0Ok6wJO1r4t2tR_NkOZz93Jcqnb6ZIh0lI4KsRqAAdVIQjNpr4hfDsG5_x6ftwKuBWBORyGiAu8KQUBJeBnip1OLZi7tKK674VetDMhyjdjSF458JhBQCT_Y8qmDwXIZ5DVKRI7Y4Ph4PQYQNPCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
روبرتو مانچینی سرمربی تیم ملی ایتالیا:
🔵
ماجرای‌من و تیم‌ملی‌فوتبال ایتالیا مثل داستان یه‌رابطه عاشقانه است که به خاطر اشتباهات تموم میشه. متاسفم به خاطر اتفاقاتی که در این سه سال رخ داد و تمام تلاشم رو خواهم کرد واسه بازگشت تیم ملی ایتالیا به جایگاهی که شایسته اونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26801" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26800">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇧🇷
نیمارجونیور ستاره برزیلی سانتوس شب گذشته به این شکل برای دختر دومش جشن تولد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26800" target="_blank">📅 10:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26799">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QskX52oZLzwBnYf65er7ITRZBm4ZP3-m8ZkWR127g81tmE_DxN8fstunF8Y8UIah8PRzSF52AJwKmov-8VO-UTWybxv2kuoe9aF5-L_3K8FZ022NSHYlaUgLk6bJ0ynO2eXxAoPaUZmk9WeXu_oncpfO-yfubeON0FJPTT_BKYSe0ZegADF0D4dPFDPKhVrgdu-8A6AGYcOMtIgsa9rqbsLAxGz8AOwcmw5hZNOvP_Zb7Q7d3xpVy7EMz6vrM5PCHlNDX_86KiPCTV7pQqKVHTol6fYbriUKJDDHxHBViYV5n21SWBXdeonZFyZseJSJe49KL_fyx0fOrxzz68H2og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ اکثر رسانه‌ های یونانی از جدایی قریب‌الوقع مهدی طارمی از المپیاکوس خبر میدهند. این‌تیم‌چهار مهاجم داره که گویا سرمربی این باشگاه تصمیم گرفته طارمی رو در لیست مازاد قرار بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26799" target="_blank">📅 09:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26798">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoZi6PF7VZJWzMFzkZKh1qn9FsssHnQ2Bqxhs04kqfD6nFywy--emJ3MFsuRAW4DV_8ARMPuXnRZ4npC7-tSqQWWL9OINw6-28wPVUb7HOB3cFyAHAhZEkOV8xidQ8m9EjoYvugoFeMsOQh0Qhe9rbf432EhQR5fIywhNsQwSRG3mfA5j0Ef7VmN_m6DlwsGYPimajwzJWoDhJMDJReUf_-j8AlXJeK1PNd7sXKr00QxmKAFWAEujgJ9lxuRwgtkayB1rTH5etuDayOD2JLEuM5-BAgDvPhW9Qz2ye3hTeCtRcZ-CzXixNM1HqCetFfMyDEJgwNzl53hFCbTL5zVtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدار های‌ دیروز؛
شکست دورتموند مقابل تیم ژاپنی و برد سانتوس در حضور یک نیمه‌ایِ نیمار
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26798" target="_blank">📅 08:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26797">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzHbMoV6HkYKYPLsQo4YOGKEYJ-Y8UyThsBdfEwyHYkoMHn_UKIIVkUf5sLV2Fqybl1dwtQuXWL5HfiEsfTFofWX3sSzRcb1YKn63cdOyKm_jQmJ7UxYHOfeCUz4PoT8q9gPi_s8VQGtCvIeJ3KzNPb5u53nWTWV0w9XxPtUMGQEwWmfmvp3ygCa0zCGGQ8TDXgw4-SKTtDyqXTniWc-czt6_om9V9K5MI5DcCavu2bEZWMY3yIkWaDWg9byuLHyVyW_MRQMO_JScTXFvO3XWdHaU1anXj8LYbF3F06CLCXYSHvf-4D6DCcJpABWMu_xhjxekNhT3CbFUzVM_Ou4cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26797" target="_blank">📅 01:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26795">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fda6c0e0e.mp4?token=tdQTv7fj_1Bk4pK4l8SM_hxjyWY-MhwKpc9hEPX7CFcGQb9z4wPv381d2pQj95-ckLMk04v2sQrJRD6b2d5OdQVjptMutb6QtOcKwa_7IOVWB0beMSALx9pWVzlO2D8xfufM0vrVRxhFD3tm9xoo0GxVYOUdJxw1izKNQqfJsVhXB9KQ23_DzVdEtKieI1tBiPwtLJN_NY5ljiJ5KFkCG3BgwMv_UEfNZp4_icRErnAU3-mNhyPMs6uiBl0KzL3rcEYU5isNeFvRTKzOjgN8LKHDTmzhXs4nXa0xNSamVJOIx_xKvcPloWE6pbGU3OVj-ed5KXf8TTlLjgyCiKnlKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fda6c0e0e.mp4?token=tdQTv7fj_1Bk4pK4l8SM_hxjyWY-MhwKpc9hEPX7CFcGQb9z4wPv381d2pQj95-ckLMk04v2sQrJRD6b2d5OdQVjptMutb6QtOcKwa_7IOVWB0beMSALx9pWVzlO2D8xfufM0vrVRxhFD3tm9xoo0GxVYOUdJxw1izKNQqfJsVhXB9KQ23_DzVdEtKieI1tBiPwtLJN_NY5ljiJ5KFkCG3BgwMv_UEfNZp4_icRErnAU3-mNhyPMs6uiBl0KzL3rcEYU5isNeFvRTKzOjgN8LKHDTmzhXs4nXa0xNSamVJOIx_xKvcPloWE6pbGU3OVj-ed5KXf8TTlLjgyCiKnlKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دوگل خاطره‌ انگیز از ارسلان مطهری و وریا غفوری به پرسپولیس و استقلال در زمان حضور در نفت؛ هر دو گل هم در دقایق پایانی زده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26795" target="_blank">📅 01:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26792">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKnOAZf9zQoBt2-YwQoOhE1h8lgss4KdT6P80tFWPKJRBvHGQjVvzgWkS6O5Cpgg8c_SKceUM82FY2yYFfa2Hm9N7w6xMvRrdgmclAC_Vu-gap44xOTqSCmeHI71LNuzwom31gNMYlukgGZiValzp2cCeO37fHoa1NzivBj17C-r523laMtWOeWz0Nzmo-yiQYUCeoPa471bSFlOPO-ZOe8RjQaD82LYjiTFIYbRrbg3ZKsw_hM62V8wfvCOKXvJP3o3363gmKKXcXH2tPJEqA8y2X6iYeEAXBj1D837__9X53CX7FCstcu9QR15MnbqfRJp4tTIe4fJ5297iIrVHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کریستین تیو:
وقتی بچه‌دارشدم، همه برام کادو آوردن بجز مسی. اون‌بهم‌گفت‌که کادوی منو تو زمین مسابقه‌بهم‌میده. کریستین‌تیو توی بازی مقابل لوانته هتریک کرد و هر سه پاس گلش رو لئو مسی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26792" target="_blank">📅 01:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26791">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hU49xYALl_zbqfSiOIbPx-Mc3leYBRCAYtXOElYiyaG3LO4tNE_YDNKjZinqvZd-KH2KE2qseMPW1UZIx-Rdn-GBE9Beai5OlEdfx8tvn1eWmorGkikCbFQSGfu2x8lQVLLmHlX7eJ2ONu_WqBEF2UIpmek3AlSP9BZEkTRsFbygZGx5gdrm3swljch7es5JIz3H2-HgC7_PMiQpEu4gKIV9EA-pL40r4q5x_M-TYwzXtj__dcCBI0lGmdiXn51Y90OwRS38EX_EA7bbhMOJX0SabaD9wtr167FDaQcADJur7DR9YyxYDceBJLLUNMlWc2AQOUSbqH_BY4VbitGtGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
اسکای اسپورت: وینیسیوس جونیور این تابستون در تیم رئال مادرید میمونه و قرار نیست که جایی بره. رئال مادرید به تمدید با بازیکن خوشبینه و هر دو طرف خواهان رسیدن به توافق نهایی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26791" target="_blank">📅 01:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26788">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FNuq2so1d3oAhV-5N8_el9Rm7GzigtDF5EkgdLPmaAWKd8aenqYKB4SKDBjZRxu8P_iJSJ0P_YaFtyjkQHt_JVjHmT7JGsG26bx4ZAznLJdPc0TCtkbDuTHI5BssRjXAcO0j-55t_CJccA-qXNpon9nZXVuaZYHTsTiK9VgHr2N0hmcs6c267IWaWqHF7A0-rpqhAxu6CqdpnjHPPVF5AHVOcOj8tEuQF_BSNS1Kr8FYIdiJffuJRA1hJnpggELMKiNETFBBZ-7wGAFCQfi-RyuErc41i-637bRI4SZOGyQQpeK9Xn6KRzLMw5S3cOr_VrSlPNoI1AWRlsSuW0h9rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K4eWskRtDNLd8hJUwhQYpbOBc75EOp6Q_0c4CE2Iw0VVhWbgllbCy_g9JiF-XhIyj1i_TIdPH1p19CYe3SrY50OEnq-zMa889vS2jXhIYYwdnHDaRnmGSWiVkqfB94CkOK9rMJY7TSDEmiuJmFi-IoqZTPPKXOjA19nQlzYlN5zPAM37vFImATmr-8hPkHrVcTiJXIdZkbhRJ-F7LFFHdz-dPDyoREzG-p_lmkTQxlMkeIKX-nPvfjyerumP3o7hk4sLqdpDyspeqoKipfKUeZH3SbSfJ77pX6rqGY25aakzVTyKYd4YU2NETcBhDn2I40mYjicZh8SDBokhgaAjyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇹🇷
تیم ملی والیبال زنان ترکیه با برتری سه بر یک مقابل تیم ملی برزیل قهرمان لیگ ملت های والیبال زنان شدند. زهراگونیش‌بهترین‌بازیکن تورنمنت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26788" target="_blank">📅 00:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26787">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d1f12784c.mp4?token=CTtwwmq_HjAPsfexhGubY-GStRNmIdIU9jrhJTtVLQCVYwiA4Mi5mX6Rz2r7FGbma-hLjWPltlnMwG65gE_j2xKP1FiDKKnN6rb1VtuMj-jclBqdMSOMElJ2_KM4uf5Qwjp4jUKFSHOyRgtez7uIMui7YtW7b9jNuifBXUDSyrpwyiNKTLDqO1zztz1AsD07WKXW1yNMoo61-WNuv4poYIUSmMAL0WcZWEmWPqIxor9J6-CgaC8mAEOGUu-UMXCnLTFb3xW5wB2jj3BK_DjkXodIwQHhameOeyz2Z6aixaY3lUaLwETtClHmpLj2WDZrxJAQJZO2JBE03EzkAmOdJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d1f12784c.mp4?token=CTtwwmq_HjAPsfexhGubY-GStRNmIdIU9jrhJTtVLQCVYwiA4Mi5mX6Rz2r7FGbma-hLjWPltlnMwG65gE_j2xKP1FiDKKnN6rb1VtuMj-jclBqdMSOMElJ2_KM4uf5Qwjp4jUKFSHOyRgtez7uIMui7YtW7b9jNuifBXUDSyrpwyiNKTLDqO1zztz1AsD07WKXW1yNMoo61-WNuv4poYIUSmMAL0WcZWEmWPqIxor9J6-CgaC8mAEOGUu-UMXCnLTFb3xW5wB2jj3BK_DjkXodIwQHhameOeyz2Z6aixaY3lUaLwETtClHmpLj2WDZrxJAQJZO2JBE03EzkAmOdJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛عصبانیت‌آزیتاحاجیان‌ازسلفی‌بگیران در حاشیه مراسم ختم زنده‌ یاد اکبر عبدی؛ مگه عروسی اومدین؟ که لباس‌های سفید پوشیدین و دارین سلفی میگیرین؟ خجالت بکشید بابا. مثلا الگو هستین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26787" target="_blank">📅 00:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26786">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/556eaf6051.mp4?token=iZMhowXJ7cYhBi9qpx-jVC2LYe1nwmZECCasM2wX3_jsB-OgH9yQKqvlz6DYQ1ALadNSB_Gmd_6mEPzQk4SuI9QhTNmfxQ00GvnquLTWB-ka5S_EfH7PQh5a8qpquIslHyH-UHyRG4JeFw2ReUwZOFdfY5HpeuW2YeRSpP7iDcvP6J5yLPqOsnYlbqh0Uv7WRYC2U05e9rAWB1GWLrEaPL8gZSlqtJV45MrOwnmpQad0oJM8JMkD6CltMoB3oBNeqJM98k7dO4QW9l2o3fXJPX6JGjqC60SvbueRqV4RK5mT_inR9vVmNfkAuwuAZE1_RodMui7p_sAwQYFsBm6sqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/556eaf6051.mp4?token=iZMhowXJ7cYhBi9qpx-jVC2LYe1nwmZECCasM2wX3_jsB-OgH9yQKqvlz6DYQ1ALadNSB_Gmd_6mEPzQk4SuI9QhTNmfxQ00GvnquLTWB-ka5S_EfH7PQh5a8qpquIslHyH-UHyRG4JeFw2ReUwZOFdfY5HpeuW2YeRSpP7iDcvP6J5yLPqOsnYlbqh0Uv7WRYC2U05e9rAWB1GWLrEaPL8gZSlqtJV45MrOwnmpQad0oJM8JMkD6CltMoB3oBNeqJM98k7dO4QW9l2o3fXJPX6JGjqC60SvbueRqV4RK5mT_inR9vVmNfkAuwuAZE1_RodMui7p_sAwQYFsBm6sqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
حضور عادل درمراسم‌ختم زنده‌یاد اکبر عبدی که ساعاتی‌پیش درمسجد جامع شهرک غرب برگزار شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26786" target="_blank">📅 00:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26785">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdcGnaAgZZyplM_2ujzIEZ_kNN1TX6X60N7JTjHXWS0P0LHNHeQg8wE3hCuckgMdTflY4EynKFfGqYykl5BqzSe9K1dZjwJJwxt_wxM50wNjPtrO8D7FkeDGKPS7QyHT8FEMZcb9iyshWSXF8NU-8TsFueu_fA_G6pHNKtt0GiFZQ9Ft1DeJ-J9_UUn88ceIMFhlAKSJ7b-W_vKEEn_9Aar0oH4gGGX7hFvdet-jDpGFcL8UIOp5i41MfXyLK88fAndos7yO9JqqPmAIP5AaRpQSnvLZET7GZFHoqUlqFuwKkiOMtlMdENchuLBSMUicALmMvUCw0FRqfbxXu5EhNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26785" target="_blank">📅 23:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26784">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eB1iEw_gQwnAr4hLECf0FPJEcR2Z9wcalLO9kPAPycfz1g7KJFUOujhwehaKxOzP8UGYakBzShi76mlfGHW7w-Y3NOcvN6jJbQcq2NGE-BJElCvsvg_XhEF82tTR7fa6eHy0EWliZH7JLSeVS32mj0PIzu5pi3MfHcGgSx1xYZbydZG0oA3qc22PbiatX6kwkbv8TOR5OjatG-7V38DF7BvPsYezTJsr_5GfNYDQpOdXFmbBqqFXPHvnJ6FY_7Wln2nGrLUjMeLtRKVpE5dhJgs_ijoUF--LWvzept1IACi7ei-qdOJkcdzu1RXKFvuW6LStzHtYdoX39zS0Y2LQJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛
مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26784" target="_blank">📅 23:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26783">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/787ac45905.mp4?token=VQ-1tUAeEeVzBIn6ugeVIi8vqU1GV-DDvkebhfpKM8xi2TQVv4muf0TOaQ46iOm6_JrUS2WT3NItNn0uDrJOa6jH3HX4cKe9V9fZDmfSLy534pJADXAw2qmhGnD6yd_8qc4Fz0fCR_botqP2w22qQZHhC9cLFVt9imCnMwt_ZAoOmAxHFu6ehl7QIMeT8laBSUHWjXyunYHY-X_B3U_jz0nf8XySzaJQcyVe1A-mrvCTRXcA3VOglbEqanr3qp5NDj_TNvZfUB44VZ7oZZbjf4nSYbf-zP4WLyAi4aIW1MmaIUZaNXuoyrpVP5sYKh6vxa6kwGzMJmZ7FePTCavqmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/787ac45905.mp4?token=VQ-1tUAeEeVzBIn6ugeVIi8vqU1GV-DDvkebhfpKM8xi2TQVv4muf0TOaQ46iOm6_JrUS2WT3NItNn0uDrJOa6jH3HX4cKe9V9fZDmfSLy534pJADXAw2qmhGnD6yd_8qc4Fz0fCR_botqP2w22qQZHhC9cLFVt9imCnMwt_ZAoOmAxHFu6ehl7QIMeT8laBSUHWjXyunYHY-X_B3U_jz0nf8XySzaJQcyVe1A-mrvCTRXcA3VOglbEqanr3qp5NDj_TNvZfUB44VZ7oZZbjf4nSYbf-zP4WLyAi4aIW1MmaIUZaNXuoyrpVP5sYKh6vxa6kwGzMJmZ7FePTCavqmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌ازاین‌گفتگوی تاریخی بچه‌های غلامرضا عنایتی با عادل فردوسی پور که عنایتی به بچه‌هاش گفته قبلا مربی بارسا بودم؛ عادل از خنده غش کرد.
امشب غلام رضا عنایتی با عقد قرار دادی یک ساله رسما سرمربی تیم لیگ یکی پالایش بندر عباس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26783" target="_blank">📅 23:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26782">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f6c32deb0.mp4?token=mve7hkoDuHsh3JVY7fYW_5rxPv2Qm4_-3hfVcd0lGSqTsYPn6wQpgAbhkewJobGrJKPlX_ftzSIQTlylHA76UPZrkdpAfGpldjNq1bCxQYFQNtfDKb6UiUfiChLNh9sbG1Tre2ZJP7QHOR_q-xnMFHJkW93ihenIyd2r859Dly6NX2tCdFaPGDOulRCrVtGSodA6EGqbN4aEUEkzYKE2FxgwaxWI_70yKozmYh9CecgO56GnwKs31gEfVkTO6QNTbRo1iU3MCwQ87RVOMwoBXQ2nmaAAbi8H9eMUdIEMrSoE_H-TUHK-o-F7pRepBiGa8YsvHe1bu33q5x18l-7KTHuIed0S5lhiMORCsEnmqmsHRcHnDKxdZ3lz9xCn8rqCO9KhdTaCSLIOtbj5K3Rqb_c8pi94mlSnsaamqYLkf0YYsbPoALBQiqcu8wjUCgn85PY-RzOjivMSvySuPoOiWCE7zgYJ4vD0XfldlxhvLnS8mH1FciFGjv_MTN6rlcUPELGh6GfSPhedYqUC6WciwGX5k5Va9e39cVse7yn5P9tbP30-NM2RMSARu2MbOnvmLNYaQhScRJQERkEZhTwkHeQXTQJ3Yg9ocYlx5bGFosDQ8pW05NAxQ9lsCRFSFhOA5PlK3ikLiBpr_wtosepCLbhCvJNcQHZpXX4rZafpH6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f6c32deb0.mp4?token=mve7hkoDuHsh3JVY7fYW_5rxPv2Qm4_-3hfVcd0lGSqTsYPn6wQpgAbhkewJobGrJKPlX_ftzSIQTlylHA76UPZrkdpAfGpldjNq1bCxQYFQNtfDKb6UiUfiChLNh9sbG1Tre2ZJP7QHOR_q-xnMFHJkW93ihenIyd2r859Dly6NX2tCdFaPGDOulRCrVtGSodA6EGqbN4aEUEkzYKE2FxgwaxWI_70yKozmYh9CecgO56GnwKs31gEfVkTO6QNTbRo1iU3MCwQ87RVOMwoBXQ2nmaAAbi8H9eMUdIEMrSoE_H-TUHK-o-F7pRepBiGa8YsvHe1bu33q5x18l-7KTHuIed0S5lhiMORCsEnmqmsHRcHnDKxdZ3lz9xCn8rqCO9KhdTaCSLIOtbj5K3Rqb_c8pi94mlSnsaamqYLkf0YYsbPoALBQiqcu8wjUCgn85PY-RzOjivMSvySuPoOiWCE7zgYJ4vD0XfldlxhvLnS8mH1FciFGjv_MTN6rlcUPELGh6GfSPhedYqUC6WciwGX5k5Va9e39cVse7yn5P9tbP30-NM2RMSARu2MbOnvmLNYaQhScRJQERkEZhTwkHeQXTQJ3Yg9ocYlx5bGFosDQ8pW05NAxQ9lsCRFSFhOA5PlK3ikLiBpr_wtosepCLbhCvJNcQHZpXX4rZafpH6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌ سراسر سم از گفتگو جواد خیابانی و خداداد در ویژه برنامه جام جهانی؛ خداداد خواست کاری کنه خیابانی کم بیاره ولی ببینید چیکار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26782" target="_blank">📅 23:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26780">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eWvDf1WYv69Bq5L0NpiD9QJ2nFQ-FZmIO9tAwLefHRraKK9goaHOP2XEo3JP2cBG-_-6tMxXhGC2iV54Bpj5iiZ0Hvx2v5H50304HCXufck-66XT6bjQkp1W2up5FXbFNHoKjYJ00dWcqVKHIKUyRFsorsN3rTakBwNOfruESvKMRuJrP0ISILAwu6r1WzIHg7FPhSO8bL2ytKcGzHL94veePi6_GXPCMWHmlvRz-wugxiclUTUTBik_TcG7SJCObAU0KjwjDwAn45rVroewhh1ymfHHG7_QfyfmYmQ8MkVUnnVoMdhj0pSyxBb8Pwh9adwASawWsJmJUQMXyyuGgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KSxM8Y3f9-Gp7sj2tQvZgKmdR-yOYnZX0LeHT7l4VGvJqyZ0qeovQAOMUkJ_JpvnEeyG66y-m7XXFgeBnGtDpGT7zjRKuXfmIySVTZDuRQ8TNSea1NG9rEI2k63aEMkTQLE5dU7-6THo-OCrtmCkXHJfZCI0S4v9cf5YXc428DIw814vrLAQuKa_RHDeE2oMQi5qNHFoj2tFlAdRnbahXLUw6ceDAuOMlNkHEY81IV9V5idd-TMxgIQCJ0JtwDxK3Sw4pCePadnr7iod9kPlONL4l35WDfIOkuXZ8vixCTFgigMckg5f7W09Qz3UdHhHk2_uBDc5PkwRKSyEpsXgNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌دوم‌وزیبای تیم منچستریونایتد انگلیس برای فصل جدید رقابت‌ها که استقبال ویژه‌ای ازش شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26780" target="_blank">📅 22:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26779">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMdDdBvF1ni9pHQeEWf0ae9nUJ5vpTLRtIgeGCBDYnq68i51FmQlEJRLBdU8Xm8zOIhX8WwBsczbcVJgCiQE8671xfltJeU4IJ_i7pZcMqyaU0fZcpR8VtEAmt7SuLZCmdJT3epuh_iyCwm32Sr9v5yy-OHRYfdOEngDcACsB7QQWc1dS6wW7ktKF3FmgmT6ddDQwkZw5WMmOEP6ljzt_PqvGHImvK526i5VupekpxdKhSOO0PtE4k9UyI30M9Of8gT7qTJJ2NwOmq4NqhFlg0BoygLArsQ_3TJJFsytlKojZ_Fb_7MCVCOu9_Dvb-dL8Gs8MSswPBSlxCaBkzALfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال بامدیربرنامه‌های جلال الدین ماشاریپوف‌ برای‌تمدیدقرارداد دوساله‌ستاره 30 ساله آبی‌ها به توافق نهایی و کامل دست پیدا کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26779" target="_blank">📅 22:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26778">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVa1_wqkZdV3Jp6qk-dMINdbL8WbmX4AkTheV_gyHWGUTAdKiTgbpj6qGKGfb2wSfzWeh8keMRn6FhrbOiThLcVYnCW-vHQHuMAswk3wOWjYzN5SSW6rJnnj5UMHr_vOlSk-PDrCuByqWDB5tv-OfdkSNGhqvVhxaJigcyZQJxTHhKLoUmaAS8GPojgYfEm4Mpf6_iVeMF5F9_MdvawXL7zhMmchj7t8c0TtJvO-m2FqpoHrPWzPIcasfM-GoicSy1Y_oxjyN1pOUtkyJMlcDe8H6k_lHS1HHNS6zCiXgyqTG9eX4EhE0u__kISgKJIji4-YMP6S20Knx4Zz1D_PJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
خبرنگارشبکهDAZNایتالیا: آندره‌آ استراماچونی سرمربی‌ سابق‌ اینتر میلان از فدراسیون فوتبال ایران برای هدایت تیم ملی این کشور تا پایان جام جهانی 2030 پیشنهاد رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26778" target="_blank">📅 22:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26777">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUz5ddwLJdHkFruSmqR8vZ5OpgtbW60GcuMnHa1cI53d_yJQkwHYIwduYYSqzO8rn8yFL4ttnvPl9sZllKNU4iI9bmY5mTDuOSWGo0ydJ4XjJc9vNML555Y-XrRFZW0EpFgiEK30yWBd1QSYI2Iz-C5WbQ75LjSg6um1ZYR6DgnE3rAnOSkdSYaqfstyDEqRhIvKAqrrabziEQmdnEEwnhyVt1F1H5fQWdxsnTFu4NW4I1LJGl_7v_qWKyHoAz9kxs6mgXIwmgwzSeU_dn7iY5okLGmMV38v93Zds-GObMxYRUML-lIkZ6IVvdhe7e4JbctElC2BWpx6AB0tGoJsAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
خبرنگارشبکهDAZNایتالیا
: آندره‌آ استراماچونی سرمربی‌ سابق‌ اینتر میلان از فدراسیون فوتبال ایران برای هدایت تیم ملی این کشور تا پایان جام جهانی 2030 پیشنهاد رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26777" target="_blank">📅 21:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26776">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YG9d7oDwTUdq-W2JjpbjlueVfJ1TGw15wi_bebLJB44qns8EaIEA0uU_KMghKnXWt3xGwi2OJgxX3_7T5R_17d20v0kTX4ZJW29EE0I6u69k4HT9BAAyofR1_hRL6h5TVg8XoojpivglfiEXGAtDh0BGHr1Xu95E7yMoU9Mr6bcuHHi1kAE2B3N5HCANFPWab-7q9HUyjD1mDeHdXr8QoZJDCpLZBXthri5BkeEvW3I9Hm_MJGk3KkhRKV9Fn0bD_tUOOLxxyAn4snqbpm2UESeAbvMFk2_STUPNM5C_FCrZXKgFJwUSQB80c6LsKpHY_e9nay8yw8rvMYpu8JMFLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بااعلام‌ایجنت دوماگوی دروژدک مهاجم کروات تراکتور؛ قرارداد این‌مهاجم‌گلزن بااین باشگاه به پایان رسید و هم‌اکنون بازیکن‌آزاد بشمار می‌آید. دو باشگاه پرسپولیس و سپاهان به دنبال جذب او هستند.
‼️
اولش دراگان اسکوچیچ باهاش حرف زد... بعدش مدیریت باشگاه سپاهان با…</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26776" target="_blank">📅 21:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26775">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/762527d0f1.mp4?token=Wga0LaBeaLQFPt4x7PZBQs3S6b0JhlhlplimIU4QZBrS-cPrHlRHyAnQUE8LlSoO_Qomyh9lXN6gNk-nf22_D2Z0MsqurKFADJ_Vq-EJwr4yiqUrSfzfuYyYxQSCJcr0EvCZzyRHL-j6qnA4tWL_ofhOEaOF9Db31PvmZC5d45hVtrYnqZtj1H0ieQpjZd8CBxIts8LSUVyqtUgA9dW9Izl5yWJ6p6lu8qste-XVTqKRC3fcekfsY5QCrb9jrsxaF44AIYuOLaZO9fe5cfj7evvAbwSyrzZOx_Cnlj4mufnSYU0zkK03QWQLCbv8ZOOFOWXiXXreEazpEsL4J7jqrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/762527d0f1.mp4?token=Wga0LaBeaLQFPt4x7PZBQs3S6b0JhlhlplimIU4QZBrS-cPrHlRHyAnQUE8LlSoO_Qomyh9lXN6gNk-nf22_D2Z0MsqurKFADJ_Vq-EJwr4yiqUrSfzfuYyYxQSCJcr0EvCZzyRHL-j6qnA4tWL_ofhOEaOF9Db31PvmZC5d45hVtrYnqZtj1H0ieQpjZd8CBxIts8LSUVyqtUgA9dW9Izl5yWJ6p6lu8qste-XVTqKRC3fcekfsY5QCrb9jrsxaF44AIYuOLaZO9fe5cfj7evvAbwSyrzZOx_Cnlj4mufnSYU0zkK03QWQLCbv8ZOOFOWXiXXreEazpEsL4J7jqrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدشد...بااعلام‌باشگاه‌سپاهان؛قرارداد احسان حاج صفی با مدت یک فصل با این تیم تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26775" target="_blank">📅 21:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26774">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4063938cba.mp4?token=CB6fzu9QCCs_eQ1kpeD5XWH3p2Ewo3b0mFu_8Y4jM-zQ0LBdVRCwja7t7sQ9LKUODCiCYNNlHer-qTPJU7N7UhJ20zs6eBucSTQ3nz5raWq1F_H-fp3cFoL_pm44BX9jJfBrR7qKYwJeaZKGywc_X8S8q8mVSvdgAcOx45BDGiUSkG5EBjNx17yastC_HlKoWdDFUiTvJj5sngjGEHJLCapIlKL3zKCy0rqGSjck70XYThaTgR7N6LvsrX4CIAJOCjiVt1IlecrUzGTXZ7wU6hrj4Dg1XjOOPo6sw68chMnmI86Nmzqk_OGOlUDqCpFyqXG5xU7KoCkSUmQZ0guqZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4063938cba.mp4?token=CB6fzu9QCCs_eQ1kpeD5XWH3p2Ewo3b0mFu_8Y4jM-zQ0LBdVRCwja7t7sQ9LKUODCiCYNNlHer-qTPJU7N7UhJ20zs6eBucSTQ3nz5raWq1F_H-fp3cFoL_pm44BX9jJfBrR7qKYwJeaZKGywc_X8S8q8mVSvdgAcOx45BDGiUSkG5EBjNx17yastC_HlKoWdDFUiTvJj5sngjGEHJLCapIlKL3zKCy0rqGSjck70XYThaTgR7N6LvsrX4CIAJOCjiVt1IlecrUzGTXZ7wU6hrj4Dg1XjOOPo6sw68chMnmI86Nmzqk_OGOlUDqCpFyqXG5xU7KoCkSUmQZ0guqZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
استقبال‌فوق‌العاده مردم از علی‌آقا دایی اسطوره فوتبال ایران در مراسم ختم زنده‌ یاد اکبر عبدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26774" target="_blank">📅 21:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26772">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/owqhezHY1389lErUsgUvluSCz1I1SOmjnJ5nwBiO5f9EM5FRHDZPXFzq7cMH35OPeNE30gGAjXana7rEi7Da3dP7u4lrHBDEWBYTpxpTiWHZ-yF0ufFGXKtU-t9bGGfgd-R_bIb4ybV7Xbdmu1W3LiwiEFOGlnzXS_aTspgwZgIAd11MHUwPXgB30oYun5kPs10rIUPjGdbREubHZ0LRp20bQ_hbsvDl5G6bqB5hLwj4kqru_SrImx__6xBiSF01LakUztjrPVYqfQTROK-lCwNIZ8EtxBahcEHw7ZOelK-Yw_E32wqv9W6QIaVdUF5quyuVPut54gqxWciAellxlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a9qS_Mp1IvVLfdDWjIesBrAXWMBp1lAtUX8GcJaE7tyaW-OTJug4RZYSnTQiUZPQp2z8hqC6mBeVACWQL0OJDmkAh8plzleZODgealM5fM5sPvQujiug2RyWbLB9E8-QjPuSFG0db4vkuToBrbIKxjT0t0l0pSm-hAdpsPk2VWWyC5Ob7I_uLN-1rBJ_8c7KXLUHt7TkWH3kIk66Tlke9_vHis1jKxkuCRVNgoEc3p9wBnHlsHnHC8F-eoTa9fJ3nDWgkP7aADdOjGdHuw681NVri1u5qd1wUi3n-rJRcCGSmR0ML5797_XKH0OoCIWVRCcIJEBJs6jrTGfUaRYPKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
ویدیویی از مراسم عروسی شب گذشته گابریل مارتینلی ستاره برزیلی آرسنال با پارتنرش؛ مارتینلی حدود 8 ساله که با دوست دخترش بود و بالاخره دیشب باهم ازدواج کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26772" target="_blank">📅 20:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26771">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3befee8bbd.mp4?token=hsqycmosYvX89p4ZrwXsOv8thdvp4glyktxdHfr7y24tm4Bo_ReFuErmVwBMtHoqTUA0cszLlolJ_N8SvmCeDcYpEI1HS93Qr1_kM179BTudMLbm98n9b8w4K9QDpBUlwOUvo1-ulSTDZzp4NaNTuByTLAC25zFGQsRTNVxRQly8I8PsYoLNSMtF8ZZD82hkDG_sNe5XlmDcX0n2Gq8yum4UgrdjNjSC37k378zwa9iKP2qR_Xqr-i_B_HLJOpHxcPM2AQwBIdt-sPw10c3aiRWUB2f2z9UO13Y-cdFod8WTls3jfWiblOE4gaqwlvy0RNkRULFATz_5vDDji3PN6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3befee8bbd.mp4?token=hsqycmosYvX89p4ZrwXsOv8thdvp4glyktxdHfr7y24tm4Bo_ReFuErmVwBMtHoqTUA0cszLlolJ_N8SvmCeDcYpEI1HS93Qr1_kM179BTudMLbm98n9b8w4K9QDpBUlwOUvo1-ulSTDZzp4NaNTuByTLAC25zFGQsRTNVxRQly8I8PsYoLNSMtF8ZZD82hkDG_sNe5XlmDcX0n2Gq8yum4UgrdjNjSC37k378zwa9iKP2qR_Xqr-i_B_HLJOpHxcPM2AQwBIdt-sPw10c3aiRWUB2f2z9UO13Y-cdFod8WTls3jfWiblOE4gaqwlvy0RNkRULFATz_5vDDji3PN6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
حضور عادل درمراسم‌ختم زنده‌یاد اکبر عبدی که ساعاتی‌پیش درمسجد جامع شهرک غرب برگزار شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26771" target="_blank">📅 20:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26770">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSdkzK_3-qge--5lUvEeTN2RFoCGj0x280qMB5AQXIitk3975RwAOgqiMEpddynlRYcBEmcgmUHQX0W18RxWVHp3-f1lRFCuuQdPOxBcgn3XYXRxwKoXpwSdSe4d2NBse-TzfpnwBLPZN9o22F2x4FixF-KCO_sz9Tr3Bm26APqhfi-1ZZZBNNQoFXeM1A2briDtufwQHYmWc2l23CnEpFzJ6X4gXWR2FhV3LovhO1FZX-hCE9K-tikUtuyxUP0UmqVGv6XnPGKph-AE3Se-wONK7dQ_ZgwZFHj-T9OR8ZUsd0MsSXsmnkD3951azNZUgYFGxBsqkQEPsPAg_dDuLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇪🇸
🇪🇸
باشگاه رئال مادرید بعداز توافق کامل با رودری کاپیتان تیم ملی اسپانیا؛ ساعاتی قبل اولین پیشنهاد خود را به باشگاه منچسترسیتی ارائه کرد. انتظار میرود که سران سیتی آفر رو قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26770" target="_blank">📅 19:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26769">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzIvZ52mKblHarDojQqhH75QQDTD28GnwEh-_rXNEMtRy2XLTtU1br8MlStB1hcUHIq8w6SP71eVNR0hNf1YSmqSChHoi_dzVLKU-B80ecocxmrMHAqmzMGRXhsPsaMU6cOLGZbCMwbulkRHZ5s2e56-Mx1F4vEREqbR89uwdiQSthgpDGK1qrHR0ZqX_U9Sl18fhzf_JcONDZOBfarV_vKx0Tgooi2RbX_Jg_oMlHn_LHN_qRdRBxY0KrJpGt_4fT-Na09Ijv1wpESXk_yR-JedfbRHwsOnBrtW6gbtP6OP4sw7HeYaB9Inux0GEiHcFCgfRY1eWFwnxPGf6aqeJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
۱۰ بازیکن‌باارزش درمارکت؛
هالند و یامال هر دو با ۲۵۰,۶ میلیون دلار درصدرجدول ترانسفرمارکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26769" target="_blank">📅 19:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26767">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee1553fa64.mp4?token=e86yB-Ae5Xhn7omhhh98J_Henob2hwC-ZhR-3jYmJ5pNY3_tnCCSu4TdHnelMnx02T2t_PDcKKWSiVPgi-WVCAaZd_f-28gkabw67rbElShHtPYUtHHhdO9q6O1iwjs4h_UWPj9mZGh6dnCLvrVbeDjM5Jsr48X5wtMPTproNBcJ-nXxXup8nXzQOmsJk5pLgU8A5SBJlqtMAtIyDZMff0o8qG3oeC_ftw9Zu91QoD2R6OffUS1UL2bJyGIbZna_y1-_jNZ0BDnCCZQ7UnqVXT8oPMc_7RjL8-tJy7qjFylcLSdMI7RG8bFjjzB6-AiHHJReIChwSW5pQYPEVvu_-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee1553fa64.mp4?token=e86yB-Ae5Xhn7omhhh98J_Henob2hwC-ZhR-3jYmJ5pNY3_tnCCSu4TdHnelMnx02T2t_PDcKKWSiVPgi-WVCAaZd_f-28gkabw67rbElShHtPYUtHHhdO9q6O1iwjs4h_UWPj9mZGh6dnCLvrVbeDjM5Jsr48X5wtMPTproNBcJ-nXxXup8nXzQOmsJk5pLgU8A5SBJlqtMAtIyDZMff0o8qG3oeC_ftw9Zu91QoD2R6OffUS1UL2bJyGIbZna_y1-_jNZ0BDnCCZQ7UnqVXT8oPMc_7RjL8-tJy7qjFylcLSdMI7RG8bFjjzB6-AiHHJReIChwSW5pQYPEVvu_-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوان‌رومن‌ریکلمه درباره‌ مسی و مارادونا:
«مسی و مارادونا دو نابغه‌ان. عادی نیستن. کاری که اونا می‌کنن، هیچکس دیگه نمی‌کنه. من عادی بازی میکردم اونا نه. حرف‌های فروتنانه و جالب از مردی که خودش هم هرگز معمولی نبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26767" target="_blank">📅 19:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26766">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxuiWQmqa-xccjd0Ls5PMjfqnuI44xXdK07qcQTih5JE-QuZu3cB_I4L8eBSAySllaPRXg90AIrjGIzZpnZydXwxnbsBYo0naSIYGGOD2m0SEsNtkcn5GKrqJdN2mjjkgmDZa9mkeVbPQuZj0W2oy4VbO7UBqUR2SKcgDiGRfccpncBP92vYM0EJnZm0DVTpAvruXezK5zAeQbu52kSJnSHgpzZ7IpYyWXSzrCOZx2xm4RIcYbXDOqmBhrvlVqaBgFyyOZDUqllTu6Ad4kj4x7ugp-O4EEWFiuWCcMsHHRkiOvv3UX2m0benOvjYmVAzteB73L-EEV8sfLXVB8FWHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
امشب‌محمودرضابابایی ملقب به "بچه" به رفقای نزدیک جواد نکونام گفته "بی ناموس عالم هستم اگه اجازه‌بدم‌باشگاهی با جواد نکونام قرار داد امضا کند.
‼️
سرمربی‌سابق استقلال ظهرامروز با مدیران ایران خودرو برای قبول هدایت‌تیم‌پیکان به توافق رسیده و قرار شده فردا به…</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26766" target="_blank">📅 18:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26765">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_S2yOfDG0QqamokMr2cadLkRhfIG8K8gJNUBynL15B0EybBTEUnxArwWr-UMhGPiLxBjFG2ncsqGCPKDPtGT7-rimvS3HnTVoCpYQfdiGACgfXIJo4w9DbKbNvPZELGoYMaie39WZvEiSuT85IEfOLwkenqoFqIhGa4pmIVb7lm-XY_9nFc2kSldzLxDnSgra0bMkRmywy1YssHZgu357I6jEPc0swnNe8E7SjsppCxMlAhgBaoUuTqsHMDx_QSHNEYqijpjosVyBi_Dawq2GlFW4jFVTxWMyYmfUqBgOUNhAWl7hi5p4QolIBb7_4nr8Yw72q601DUv-7s0y759Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
نگاهی به عملکرد کریستیانو رونالدو در چهار فصل حضورش درلیگ‌برتر عربستان و باشگاه النصر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26765" target="_blank">📅 18:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26764">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97aa505010.mp4?token=Q9YsaiCvLnxI2wrToTfWfGKrwGpKdoDak-3z9NnPwyFflDTM1AAMfzNY520AdJTfkJFzZrV9k8N0c36DwkgzXk5B8BexZq64WhLI159GhGMzjYSelPFsqQWG2cwFMC7M0AxfRL8J8idAv0zQHDyqfvd9tOsHJiyQrvQS0oFZY7XcENRQV_YXwhYTpQiaKaT9W00mdy6HrS_3EMXPiJQUbLrVwrYnfwUx64NLSvZ7pAS34TiqJgHKWkwavnHB15bzz-XdYOE1_Hkn4ssE--UIcnJ2UM5tweEbPT5Ix35rdM9VqLWh_I6N1qI8v6-TxAlTTOc8-Ih-onqAISeVtdi0hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97aa505010.mp4?token=Q9YsaiCvLnxI2wrToTfWfGKrwGpKdoDak-3z9NnPwyFflDTM1AAMfzNY520AdJTfkJFzZrV9k8N0c36DwkgzXk5B8BexZq64WhLI159GhGMzjYSelPFsqQWG2cwFMC7M0AxfRL8J8idAv0zQHDyqfvd9tOsHJiyQrvQS0oFZY7XcENRQV_YXwhYTpQiaKaT9W00mdy6HrS_3EMXPiJQUbLrVwrYnfwUx64NLSvZ7pAS34TiqJgHKWkwavnHB15bzz-XdYOE1_Hkn4ssE--UIcnJ2UM5tweEbPT5Ix35rdM9VqLWh_I6N1qI8v6-TxAlTTOc8-Ih-onqAISeVtdi0hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دقیقه 92 وقت‌الجزایر گل‌برتری زد؛ گزارشگر: 7 تیر رویادتون‌باشه؛ یه‌تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد. دو دقیقه بعدش اتریش گل زد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26764" target="_blank">📅 18:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26763">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhkVV76pv9w1zisvIu6g-ZOCHZEtZHeBQpLcuVf_s7vz5XMY__y1lGBmbUMKZcgXGqU3nKTaJ31bFkTC2o_-L1gekUgX1qVlBywFHAkcZxEcpA5rfabbDMAl5eqHWBT3c-WS-dEPzCWqhT1_558WRQU9emMCgu33PFHFEmMcN3B8LYg8TzRm5GNU93PihlSUSL5Bu1NLbYAAc5_7_Hk-D2fhfLXAirO7zCg9eNNlN78tT0cmipKcIkG7q4lN_BGkDRWfpR-Lyt5fCLeERAq874moYhZbH0hXFaxpWVSPFK3RbvBonAS5litu_ttueBtJb7s1D-OnSKkkkfgqdc7Cbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌گفته وکیل‌ایتالیایی‌باشگاه استقلال؛ ظرف امروز و فردا دادگاه‌عالی‌ورزش CAS رای نهایی خود رادرباره پنجره‌آبی‌پوشان‌خواهدداد. یا پنجره رو بازی میکنه یا بسته میمونه تا نقل‌وانتقالات زمستون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26763" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26761">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4wLDelRoZQs10AlvS_4thB7rH6N0LItSdD3wwj5tyq4lmxcXnLS6tnF-aEiYfMqU3zzpGJeg_r0Hg6HFTeCcZt1elj-LaOZ4jGeTbm7t1ZGFE8mNfhpka4F0amXh0aCCh0qHR8CLqzZc2vX4yqFFXdJUxvhrqigG0UkCr1GK1gUI-uZFbzddJWGDONXV3h_ehZu1eJpZy9nqfnSLE2LlhEL75Tbt97DveidgjaE-02rOpCK8MwrRIVrUrSNL68z-3o5_aNcNiO5J5uCzDgDSV2M_sp1K667USqg0BxsnRHBGIjSd1kvYMle4sKKaYd5yutQcsBAb_aThgCtGAxBvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
دنی‌ولبک مهاجم35ساله سابق آرسنال با عقد قرار داد دوساله رسما به‌چلسی پیوست و شاگرد ژابی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26761" target="_blank">📅 18:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26760">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6E6s-gJgfAyddAYhopBWkTCRvtzHEwXnT1-MaGpuqf3IS_JKOQxSj1hCWgXfcYnTkLhUfUXklyRSZM2MtworkexFudJaGCq42dS_5KSdBkhgRFsVnxER3c_q8mh5UBwcsJMomgrhrj9cIainqz2z092MPJmCIRA7Je7wW7Ge_4ch0ChqrykMsv5qXliQHaPFL1rJg5uHDKKL2ekHX94Brh5ZDFCQbI0eaeQ9aU45ntlMATIAVjYBHYBw9swc-oL4Yi-Id3BP1diyJ8EggjeaDUdmiwDSkegXELkJ4cwZNTadkcyIj97rzk313QyK5oky1cW_2rZRhcfo6-HZ-WT_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
امکان نداره هواداران رئال مادرید این ویدیو کوتاه رو ببینند و بغض نکنند؛ هایلایتی خاطره انگیز و دیدنی از مثلث وحشتناک BBC در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26760" target="_blank">📅 17:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26759">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQogZtxH-Dcsh_xi8fyP7KUplUHWwdNNUWMOmiFDNL25uXktoMlj1_ggFdOvECu7N9fFPN485mdAH2nB0A_WRXHXIWPSikp6d8rQNyGGFuAho7cjpniRf_MOahuUFJvWNNOAfiHow9Q2wlxnbsbajwrNl3bGNErY8RTS9yW8aw7IpwykE8mkPLue9PAuP0RoTtKV8tJ3On7L5d7LofDO3J8bKTO8HDEphIlpld9La24TN9rb4aGtFJuI5M4QzpWFD1x0-BRhrHOLkRuQ1TBfF10RTylAypvWNxkSpHYRFjV7mjQbB6isZkOdsFATSVJRqasd7u2JMEvSxMPZD8HV0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇪🇸
🇪🇸
باشگاه رئال مادرید بعداز توافق کامل با رودری کاپیتان تیم ملی اسپانیا؛ ساعاتی قبل اولین پیشنهاد خود را به باشگاه منچسترسیتی ارائه کرد. انتظار میرود که سران سیتی آفر رو قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26759" target="_blank">📅 17:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26756">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cx3IextV-PVZ1Xmn7CT-oLiyw724P3jRPT-5nv084Ro4xqILyujAV8f60nuo89K0evgqHqkTYMSrnCKRBRXGluDuuT9UdjsV7ryk1-_eMgYYXKcKthh01bttC6kZmoGfaIkM9lZAvWsGNCqB_x6eWLlkWjmD9lTDdFRszmDfne0xJMdWCH1q8aM5JBok3VLXjZsKW4hNurR67UQ6BbhDpCIgq6Yv7gi8oRctd_DZGvbTJmBB2tMrcQKjwWIZEhzEdPVi6ps6O41BmdaicWJzRWlKLfE-EIPPznvTmjdI8gfxehipUysTFvaAauBoxpOwKVNLN7kWfLCHJ0FlUjp_uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LsLNqK2yQmuzzjxA1WBPZq4-qLkHETGn33rfN272LNx3zajwwB9JfcUchedy7iOuvVp30QApyHUYr5cq0OPNvKaSg0KZCvTPH4rcpAQMdOLs2MfLOmhqoNbhWmrMpU8rlBzvvxWQ4ScBmnEeBxwYzWsHhGyaGhBfgm_W1ouoAbq_DcwWCQdoL50Px4_83mj-c-iaxH48-cWk7wIZ0iwR_vbypYVDxxgMWP6fvFtQtjhqPhyDtYpltB2p8U8fiBdHxCzKC2CRRUwDepnfpq4En1_Hd8cLkekO6Z-M6Xxp-t-uiGnNZ8aByqF07AfmVSDxkfZhaQ1V5DElnoGmF1kOWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترکیب‌منتخب‌ستاره‌هایی که تا به امروز به هیچ باشگاهی قرارداد نبسته‌اند و بازیکن آزاد هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26756" target="_blank">📅 17:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26755">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03d21e0c25.mp4?token=kux-5oVqs40BuCNkrefilTEAK7wNYLtnXazXYG6cPeGSJ0Ar2fv6TMuIozrefLgtw1lYOOlXAA-59sIvysHVWKQL-FBakt2yJ7HdfTUFJySKVJYjTm_M95wV6xk2_dWFl_s6qimmwMUBSQ4MtkmjshmAVinWTeNx06qpYvVCKxwTVIEpdknxwgiH_gpR1HczTcdqNqjQQBVcYqewX0WyBIcYRGisMOQFsjSxeoGdZq06iInLcgVkjWvRnsdtvJGhhXzKz9lQAV9lCS7PqnxOZA14DgXSZv87PGp0yAStg5-fcDFUHDA2VNKmqxhLqSCQnAfjzHeBG9oJfWoFm5CrmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03d21e0c25.mp4?token=kux-5oVqs40BuCNkrefilTEAK7wNYLtnXazXYG6cPeGSJ0Ar2fv6TMuIozrefLgtw1lYOOlXAA-59sIvysHVWKQL-FBakt2yJ7HdfTUFJySKVJYjTm_M95wV6xk2_dWFl_s6qimmwMUBSQ4MtkmjshmAVinWTeNx06qpYvVCKxwTVIEpdknxwgiH_gpR1HczTcdqNqjQQBVcYqewX0WyBIcYRGisMOQFsjSxeoGdZq06iInLcgVkjWvRnsdtvJGhhXzKz9lQAV9lCS7PqnxOZA14DgXSZv87PGp0yAStg5-fcDFUHDA2VNKmqxhLqSCQnAfjzHeBG9oJfWoFm5CrmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه‌ویدیو از الان‌وقبل یان‌کولر ستاره‌سابق تیم‌ملی چک و باشگاه‌دورتموندببینید؛فکرکنم کمتر کسی پیدا بشه که بازی‌های این فوق ستاره یادش مونده باشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26755" target="_blank">📅 16:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26754">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nxd2cD6xdjpaawH14mc53vH2UsCqUQCWa_f_Z1vHT-XTtB3PSLzgLEiWZs2way2uWGI9gXlMR5cA8TqZS7GaCnaAwmSIrd3eLB5qo8Z2bNZ96vwPcYj8IPgK3G43gm1y0RMBrg6ss538xbkjwv1JfFni5HqhUJE1mhJLEFCsVD49gAuvS16i8CvsdfTjqDbLM7oJrG6denJImn7I83G2vKVjqF3n2c0eEeU03xh52EEFtlDiA7QX6EemZUZY1OgtJchF1apwUlBARXguufeNOiDvvP03jYwu6xz9IZi1x8I3tBQ5aLQ4ZtxuIl3cyEiTQtkpF36luhcjee-ZsQ2Zhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26754" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26753">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇪🇸
👤
امکان نداره هواداران رئال مادرید این ویدیو کوتاه رو ببینند و بغض نکنند؛ هایلایتی خاطره انگیز و دیدنی از مثلث وحشتناک BBC در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26753" target="_blank">📅 15:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26752">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IcmjBK2th3QxxfYKknNWhaXzYG-6b-f9oP8rg_2mSJP_5NFDffFvxHwSCLJpY2HiYOHOjGCC0JXan66oX3woMKe__i_wTd1D19v9wWgS0xmT46BHMiWQZ4GOcn6SVDhHp2zfISKEIhqxkX4F5yi00NY5u05ZM5-bRK6Mj4uP4CxBLMz0QiMJwiuS35PnD1AzcHsY3TFq_MzCwQZdQA-86Oe6GHIurB5eK0JfBRSpmkarQ2atZzWcCKltKRCbYGkR3MhIBYR0qIRJgSb_5P3jHP77QLxvszLCUUBeEHY8aIN-kXxRbGhOTagR7L2sjA5MHewpGx6c91vehjRT8RgLow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26752" target="_blank">📅 15:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26751">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4c3851e11.mp4?token=MkLlAtNNdYJ5rdcmzwNPjJptJR7Ry4v08WTaDvtf7Xr85GlLBgxor1B6CrrKwW2B5R-R-GkOLh131xjX7v_bT5dcYK62RWgere3s_JLem98ZuW2TztEzsIuriGH1sIJqECHoJv7ZHvH5-07GFZLgP_VC-34oRmgfkpXe-LkjF_K_f0Tu2GN1wYXNqiZKpM9dKFKwWeVon6Q2sSMVulUc7kQhGdBDTqn2vwhZ9AA4VPxpJAv8t0nkx6fjQya76sq85cJiZOFH6zBPIDuLtc_12HatbHL3_o7VexYlAcbjwUWVC2H2thrxLbUNdNkG3Z0h1b7RB1UH4-sHufPuUletIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4c3851e11.mp4?token=MkLlAtNNdYJ5rdcmzwNPjJptJR7Ry4v08WTaDvtf7Xr85GlLBgxor1B6CrrKwW2B5R-R-GkOLh131xjX7v_bT5dcYK62RWgere3s_JLem98ZuW2TztEzsIuriGH1sIJqECHoJv7ZHvH5-07GFZLgP_VC-34oRmgfkpXe-LkjF_K_f0Tu2GN1wYXNqiZKpM9dKFKwWeVon6Q2sSMVulUc7kQhGdBDTqn2vwhZ9AA4VPxpJAv8t0nkx6fjQya76sq85cJiZOFH6zBPIDuLtc_12HatbHL3_o7VexYlAcbjwUWVC2H2thrxLbUNdNkG3Z0h1b7RB1UH4-sHufPuUletIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تعدادی‌از سوپرگل‌های تماشایی سرخیو آگوئرو در دوران حضورش درتیم منچسترسیتی؛ آگوئرو در اوج فوتبالش به توصیه پزشکان فوتبال رو کنار گذاشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26751" target="_blank">📅 15:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26750">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NcS_nzZ5sITWvYv7ftl6Dz5tlcXWXZ9wuM3-pUkiuw6H8HWeTaUVEWyWW1iQabB2JdN_iFYWj3dbruFivLtjBcZ_zc4MeJY_SKjwJ681FAqzY2OaKh5esF5uDwBDhGUHMndQ6ANMIbuQAbE6weSi-3wMEHqEYT-Hv9DJ1nGoxeZp4fbTOKIGO6EoLpZoMlLnqS--yTPyVRqye50cQikUrs_ZQ5XVlHwbQSn1y1wXhKwZ3ZHcZszybeK_M96qK3puxfs1dcjg2hRGaGZLUTUjVpWZHk-XXGDCdeMOpNJ0lwe5j1e3474xjoW_klfGOz_Ta5DggHsnhVf_woibT0nK0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های برزیلی مدعی‌شده‌اند که نیمار جونیور ستاره 34 ساله سابق بارسلونا تصمیم گرفته که برای همیشه از دنیای‌فوتبال خداحافظی‌کنه اما نزدیکانش میخوان او رو از این تصمیم عجیب منصرف کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26750" target="_blank">📅 14:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26749">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjZmodjphvuyUCkpcVck4uxCxYHV4LYDNVaINN8-1nUDyXm3Okv9pkC5sxNW4jjtOhgsLGKKT-I0da7brc8t8rS06MhfBuH5qMmOWcomkhAJuoWNGt5jiywATWJwsVYaHtocGDXHKZvwiLFzak6C7N6PfomXvdHDPmS8L9umHt3z-x3SYXiuEbHoMER9y6gRj7pQw49OpOlj13MwQN_hOlDdfEphOzlEMoiRqQnh3eklACt0_UUUQoB2SdYBoJhUiHlQvVUE4sCeeY_8fH8hsNRu_5rb279-KWt3W2PiXuK18NuixQTR55t_iOKwOQtewvpx_awwyIWgwdSNV00Hcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی روزگذشته‌پرشیانا به عنوان اولین رسانه؛ محمدرضا اخباری با عقد قرار دادی دو ساله رسما به باشگاه گل گهر سیرجان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26749" target="_blank">📅 14:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26747">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sL1K22QnZ_7M6_29_996AUFLYZgXv3r8eXLpwyWWDcl2FT1iyADUSL1fSjdoYQfi6Rh_fChx7Waq5XPS8gnPLDmv4jV7jNjlS6qgSASJ7q5XpqTJE893DH-nDY20mAeoKndWIl-Y-jh-7wGu5Hi6_jvWk5loPY5kP0YXuJ5_j_uHVswnms2AuAHOuzGrCijGukFwpBRi1-EaB9EasUBJ6NBMWVoA9_Q9fTAs3vBCrrxyzb_BGkFz_F445yfNmJ5bfI-0Waj0MSrrzWtFa6pTKbElcGbdAGSZ2F7VH3IKpKvU65oGykgg53nyz3_5Lw8hkJMB8LHxNNQaVmqFYYiMew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dT1T03BmIzTDpVithr0oe8CO416WN8eScH44V3qFH0-YqJr33N6LZxw-Mt7Jjw9WwHIrLEkymXeaBaIhZaXiVPd-_8CpDyLkwYe3ul3bokx9trtOAs-8BSZjTR26LdpCQyHwm_gcnJ4UOUoaAJTF5mz_ufehn1MhFTMyL3RDCmM8X_WWuBF-gFDxlbv77699zO5CtrDs_2_CeBJWr5AM56GW8kqGyD_q0l2iJcG6KuerUJJqQPcNYLRc4oCTKiMZp73fdZVb2S7x6BLWlGsEQ5BDU6qB6_e_fplWf9FSSzTQ5z_254yolGEAAIvf-wLSp7FIWNqcFIVolJHMqhmejQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دوست‌دخترنیکوویلیامز که‌درمراسم‌قهرمانی اسپانیا حضور داشت جدیدا نیکو رو با یه دختره روی قایق تفریحی دیده و تو شبکه‌های اجتماعی آنفالوش کرد و بعد از چند سال با او کات کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26747" target="_blank">📅 13:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26746">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vz8B9Pe8wI_3aiM2_jlzsQ38PFUWW_VkQxuwgqFMQG6IA8n7gyzUIAsv95ibz5qx4EGJ63i17xwLaNfYcJfGmNQVWX1KkX5gFdlXGM4Z2sKx98K2S4l1JwkWuW7_pUjLPmD48WJcTcS78TljnPWQpoB2gCxbyi54g4VmKNShmQBQF-2sQgPM_qo5Zi9WUHy7-7jj4-jAMb0x786gjL2K-HCH5sh0-ggSc1_YjeimfzSGDllM5PWo3UjwuLa6qjM0utDkfpIAaazZH84pPqsXjFD8I024JbPWV5NrX625whFuHtx2-DcHRrBBN-Yntf0R5wAS97mK_MGGb45wN8fz_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد لامین یامال، وینیسیوس جونیور و یان دیومانده در فصل گذشته لالیگا و بوندسلیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26746" target="_blank">📅 13:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26745">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/389ac26246.mp4?token=lBx5v4VUpQjfpxgXo0TNwBGUlcYB1NFUgDulb-fPLOxSJA6puaVPVUr7uJJ_DjnjO5-4rDsXaRzpnA98BH2YzOn_L9mBjlN_Ik-eL6okEOSuJugqyqloTbBdkV2nQbFYBWrIBRy9XiR5Clzl2qpWqg0F5W5byHEDUOYO316OjhVteRjsODSLtZn_ARFByJOXyDPhpFNuS_Ng0EeD5D-ZJU-bjLTff9q799KcIE8QepQD_56-ctMghYWZ8r5wIbaWq2lLhptnvSPGRHU9K7Ci9YKbFV0OY6aEBDNsxTSuLlh89WnIThf6UuvRTu5YXPSZ05ebZe0qIsrV1jYxWWuxOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/389ac26246.mp4?token=lBx5v4VUpQjfpxgXo0TNwBGUlcYB1NFUgDulb-fPLOxSJA6puaVPVUr7uJJ_DjnjO5-4rDsXaRzpnA98BH2YzOn_L9mBjlN_Ik-eL6okEOSuJugqyqloTbBdkV2nQbFYBWrIBRy9XiR5Clzl2qpWqg0F5W5byHEDUOYO316OjhVteRjsODSLtZn_ARFByJOXyDPhpFNuS_Ng0EeD5D-ZJU-bjLTff9q799KcIE8QepQD_56-ctMghYWZ8r5wIbaWq2lLhptnvSPGRHU9K7Ci9YKbFV0OY6aEBDNsxTSuLlh89WnIThf6UuvRTu5YXPSZ05ebZe0qIsrV1jYxWWuxOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛ درصورتی که پنجره استقلال امروز و فردا باز شود مهدی گودرزی، محمد جواد حسین نژاد، محمد محبی و یک مهاجم هدف اصلی‌ترین گزینه‌های آبی‌‌پوشان هستند و قصد ندارند بازیکنان پر شماری رو به خدمت بگیرند.
❌
باشگاه استقلال درکنار این‌ بازیکنان…</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26745" target="_blank">📅 13:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26744">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DrDqVuNkjoHx7ZwXdhiGxE9YRzJV6WgELGsfdKVb6IgLIwhGxs5V6zGJKRZcBslrVjtKy3d7JhRNzx5dj51q_odAt2uYGIH7DgmO2v4-xdUyKo1VFR2Eh9JVClXY0lMBU9qgtjN6ZsS_DVGpM6Zx5Zq7Cm6wl0LY6n6_o9eii90gs8bsgrJkaBC-eePy1rF_xP7TVJmltuaySAwKwuaK_XVaH_9VNUf7BBJrJJPcWHFmOkfqzy3QQO0vfRe97OwVm5yGKeyS37FR3nschYQwe12weQL5fzRlo46BkbFHjJC_anBVLBjqPLo8fxHzNiOBpfNsMpxJj9Yl4gLSdW72ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
رسانه‌های فرانسوی: رودری پیشنهاد باشگاه پاریسن ژرمن رو ردکرده و گفته هدفش تنها پیوستن به‌رئال‌مادریده. او به‌سران منچسترسیتی فشار میاره تا با انتقالش به باشگاه رئال مادرید موافقت کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26744" target="_blank">📅 12:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26743">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMA_VhYHKyf_wW7o7F567ojT6BxB71vYwqX10ggcjyTHxQzzBZq84HhybabCuHnlGLPBFYB9lqRvoGZBuzK1LOQLbiagSRFnwqo75K-yNV4Sh6Yq0rgr91JrxzZCFH_umJ43Fi_IbZT3C9vaJTBSSpU90uJBk_T5j5RqV7nAwh4xx9qzOyncInGkEmfcBF-NEPIuuhAirI0F8jwyGuzLlJboKAoM8Uqdow7yJ91qpQQU4IMjId8wsxfTtSjKGwaUUYifXzhcyjoeiM6KEBzKOBAbJeUvNywNSvX61kxRf-I6l2EOtYDZ3g31axZ9GSfH9yxGP7I0SvpcqcKkoUHM3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛ درصورتی که پنجره استقلال امروز و فردا باز شود مهدی گودرزی، محمد جواد حسین نژاد، محمد محبی و یک مهاجم هدف اصلی‌ترین گزینه‌های آبی‌‌پوشان هستند و قصد ندارند بازیکنان پر شماری رو به خدمت بگیرند.
❌
باشگاه استقلال درکنار این‌ بازیکنان…</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26743" target="_blank">📅 12:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26742">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2cc2d700a.mp4?token=DKx5SAAMUOCNkA8xK0MMZx5OleZC0x9ErCaIwiQoGScjM8ZwG6uYQYmtHHE3sY6e8fVIAhmTnkKxhg0sP2C8ujO1e9MMJzgtfJVawCZo9OZNO3HhKEZYIMv9k603qzUFUCxZ-VqrXwybR1Vhg7MlCmTdNLfhectOpQzUC7okJo6-0Yk2rd6fxvur0DpS8SQs_I8r3ZFrNKLIuCHGvkTGuxj5rAZOSOfsPBoGRmPgUcmqQYDxXX_rCkeu8gob4h3PcCf3DTyqH6ZZmu7tRukxBBJ5uV_DrvOIvMAoUaGOhhg6lspMae3bLyqH1cXmYC4urJ_kPNZQ-7ufoE36w5hRWZ6GtddtsInfhSgjIrpl8SmanPN9P6kbwTw0u6T3Pai00yZ74VRExHGv7NH0KSPRyxN9zFQXVe9cHEzAnM6P5biRYQTXzfgffbIHwzIlHas9XUw5CCsUXcuiiBZK0bhy5uB58tHLdX92SxxSL2thCrfGo3V4zaZMUCjVU9Ij0SknlhjL76eUm-_DR48Gil5bUblygdcULSzArNYcqW-h4EGzjxgvbfnccatS7hu_3SkA36bABzvMuXPQ9mi1CgAl5mgTpsR-ERVMuMmrc_ITPuH6f0eChgPGR4umbnVwZQ2cUvmJfkxl4LGLTfhC9Jmv9J01gr0jnJKcR715l63WWAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2cc2d700a.mp4?token=DKx5SAAMUOCNkA8xK0MMZx5OleZC0x9ErCaIwiQoGScjM8ZwG6uYQYmtHHE3sY6e8fVIAhmTnkKxhg0sP2C8ujO1e9MMJzgtfJVawCZo9OZNO3HhKEZYIMv9k603qzUFUCxZ-VqrXwybR1Vhg7MlCmTdNLfhectOpQzUC7okJo6-0Yk2rd6fxvur0DpS8SQs_I8r3ZFrNKLIuCHGvkTGuxj5rAZOSOfsPBoGRmPgUcmqQYDxXX_rCkeu8gob4h3PcCf3DTyqH6ZZmu7tRukxBBJ5uV_DrvOIvMAoUaGOhhg6lspMae3bLyqH1cXmYC4urJ_kPNZQ-7ufoE36w5hRWZ6GtddtsInfhSgjIrpl8SmanPN9P6kbwTw0u6T3Pai00yZ74VRExHGv7NH0KSPRyxN9zFQXVe9cHEzAnM6P5biRYQTXzfgffbIHwzIlHas9XUw5CCsUXcuiiBZK0bhy5uB58tHLdX92SxxSL2thCrfGo3V4zaZMUCjVU9Ij0SknlhjL76eUm-_DR48Gil5bUblygdcULSzArNYcqW-h4EGzjxgvbfnccatS7hu_3SkA36bABzvMuXPQ9mi1CgAl5mgTpsR-ERVMuMmrc_ITPuH6f0eChgPGR4umbnVwZQ2cUvmJfkxl4LGLTfhC9Jmv9J01gr0jnJKcR715l63WWAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇧🇷
پارتنر گابریل مارتینلی ستاره تیم ملی برزیل هستند که پزشک هستند و گفته دوست داره از بین برزیل و پرتغال یکیشون قهرمان جام جهانی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26742" target="_blank">📅 11:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26741">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9OFsjrE9fKBmHPBwlkcSh9Y3ODBnS54_6w5tC2Epbw2Zx14ILNl1PYghHAR4rxAaRKHeA1hxHQ21e8BPYjeTClgd_6j0Bk9CUQd0XrVK-17zZTcCd9yJXhQjxzGM3-YOSunCSqiqSiour7yFjk_d90-l3wozgyGIusVCj57H3_BwY-bXMlgPfipKTdL80_VmEvphgNwoH20iSDyI71FpEAtAy8pi8tFalx6Bhrz2eg58RlvKZnBcJnu5qqDCN2ySryzx-PyAR5t8kBf0VsuHqX9Wdxr9bTM5XXAfqQcUx6oQwVko9tToj54lJtXQ80jzlBytVwC0wdUe1O-H4KW6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیررسانه‌ای‌تیم‌پرسپولیس: اگه کسری طاهری و دانیال ایری رو‌جذب‌میکردیم بعد از هر بازی رقبا از ما شکایت‌ میکردند و ما هم‌ قید جذب این دو رو زدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26741" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26740">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTWWdfa0QNNaSQjkGTNGp-Woz-Q2NU85a3xMb1I0ZW_lRcoCNc2klpZ1JGGkoS6dxR6A4PDiJgZzV3dLH0rLEgDY7tjVgnkSkjUl3G0cxxol3ovnpZ33KB71r4Y_XT2cxpHuS6GC7XQpecVhpEXKUJ_tmm2xE-QxlsU1djqqD3ALuI6FjWpWh2UOcF7u-ixd3Da9pHNrdz1dEFMTQWGQJMS0jbScC_wMUyShKoqRBkZu2JidvpdqLBYn1UXeGKqde-hg75yKLd77usmr6koMLfToN54F9J47AffwSSnhIk64un--IBOxzyijV0R9Om7pDAA_meLZfgVCzNz0NNP1Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رونمایی باشگاه نساجی مازندران از دانیال ایری و کسری طاهری به منزله ماندن این دو بازیکن در این تیم در فصل‌جدید رقابت‌ها نیست تا روز پایانی نقل و انتقالات هر باشگاهی مبلغ رضایت نامه رو واریز کند این دو رو جذب خواهد کرد. اولویت اصلی نساجی با پرسپولیس بخاطرمذاکرات‌فشرده‌ای…</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26740" target="_blank">📅 11:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26739">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98e9665500.mp4?token=meQTwWkJnoCAEihP_ajucAjrco6ud7qikcpwPZjMeg9TmHOIDy_9a8OxQoKObBqHT-C7OlwFUIfE-YNjK0EKjEl5uTi30vAJ_hMFjIorCC4sLKaOu0t5i4hQeiwMfs1EvsmcHD3M9Abmlr3hXtKSDuRSE3YZljxbusTN52jc2apWlsm7NMm1FORr8JqGxdydXrWvzG5pPBMTW3zCkm94HM4jPcrOb9a7jnhgojWZJTXYvUQeDHaElvYshZSAIuYMsuKdLT847BGZsoKbGJlCyC-OtSI5_iExc9-100ec0kDb4dQCIzoX0y92lpyu0GUciqx6UIzBR0f3W-h6mJWi1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98e9665500.mp4?token=meQTwWkJnoCAEihP_ajucAjrco6ud7qikcpwPZjMeg9TmHOIDy_9a8OxQoKObBqHT-C7OlwFUIfE-YNjK0EKjEl5uTi30vAJ_hMFjIorCC4sLKaOu0t5i4hQeiwMfs1EvsmcHD3M9Abmlr3hXtKSDuRSE3YZljxbusTN52jc2apWlsm7NMm1FORr8JqGxdydXrWvzG5pPBMTW3zCkm94HM4jPcrOb9a7jnhgojWZJTXYvUQeDHaElvYshZSAIuYMsuKdLT847BGZsoKbGJlCyC-OtSI5_iExc9-100ec0kDb4dQCIzoX0y92lpyu0GUciqx6UIzBR0f3W-h6mJWi1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق پیگیری‌های پرشیانا؛ بانک شهر هیچ مبلغی به حساب باشگاه‌نساجی‌مازندران تا این لحظه که این خبر رو اعلام میکنیم واریز نکرده و باشگاه نساجی و مدیرعاملش فشرده در حال مذاکرات نهایی با باشگاه استقلال تهران هستند. علی تاجرنیا و هلدینگ اماده پرداخت پول رضایت نامه…</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26739" target="_blank">📅 10:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26738">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96f6912da5.mp4?token=u7WjBGgaAsawgVr7pzAA6urVjMeDvJ0ozltAosnrtYFOsOUeD2Me-_0ne4e1U5F2uw5vVKnmKGmLJAs_yJt7CsJdbkfoVLOVOtY5YG2HERp9x4st9Sy5KmYwvZAcjSwzQ9aQ55At8v9LiVJP6MQENWQ2O_RRj-K4QUoM3DwAZtMTyyQMa435oNFtrlnqSMZ9tsCUFk-mJeOyCAF3CLXfZvtHh_DZDPanR4mzULfD8tice_VD6_Oo2hJwx1DWqTBRuu7BbsizWpwdemLWCD5_SIT75qVZ-ZO0rIS1VpeQ6-qvEp8IKBe-VNYVQoXO_MqQwb4dXn_276XUAelGqMZ9rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96f6912da5.mp4?token=u7WjBGgaAsawgVr7pzAA6urVjMeDvJ0ozltAosnrtYFOsOUeD2Me-_0ne4e1U5F2uw5vVKnmKGmLJAs_yJt7CsJdbkfoVLOVOtY5YG2HERp9x4st9Sy5KmYwvZAcjSwzQ9aQ55At8v9LiVJP6MQENWQ2O_RRj-K4QUoM3DwAZtMTyyQMa435oNFtrlnqSMZ9tsCUFk-mJeOyCAF3CLXfZvtHh_DZDPanR4mzULfD8tice_VD6_Oo2hJwx1DWqTBRuu7BbsizWpwdemLWCD5_SIT75qVZ-ZO0rIS1VpeQ6-qvEp8IKBe-VNYVQoXO_MqQwb4dXn_276XUAelGqMZ9rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شوخی‌های بامزه زنده یاد اکبر عبدی با همسرش درآخرین گفتگویی که با رسانه‌ها داشت: کسی به من زن نمی‌داد با دختر دایی ۱۴ ساله ام ازدواج کردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26738" target="_blank">📅 10:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26737">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F04CCvFQ8c1bnl6rydNMWvJHljG6IaPrf3ftkW4fNxG4dTzkgnN4_U1fe8Tm8gcPN5t1GVAKAmljt1Uf_-kvPMMW458Niuv6azxjuibBQrZupqLUI-ZhKy11Oq8xlOP9TZfFVbeMx4PI0ll8saxALtrZy7ZzUzHljWdcnAX-WChyhs0LDmjcjxhcI88ghwVVmqhcJiVM1XGtiM9aLuo-TQo_AuQpyebicqOLc0ZvXyE0YefSgr64FXXetIcnpKJyAipz-bTdM-WXsZX1dx5yM3d5pFdU4ankLaGQg-S-SVKJFkFkqdVzJ-Kv2mUgg4XbE6DYMzCpMFYSVv6RFXOGIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26737" target="_blank">📅 10:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26736">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqA63SHwibFWb_6190Q6dYI69mic6EqlKOupXpCCLMlF2yigMYV4DsrL2p9wHzQV5vdUCaOHwYIXI7MEsllyk6jMb9dIcL4izXjB85dGUnOC32A8qPmoUCOPnoE9TEHBY04nbMYS8OIukn3hbxfusPX8pNXtbVEouYiImem4swQ4wx_L9m4-vSkbDyk4Vt6MgQukb7vNBtB-mfZ1eDIxrKIfX4PTVa1v1qkB-q-KZqIGscrmJ1fA80A_G8w9JaPykl8_MCFK4sgs2hU_pm2-nWvcOJQcy9zd23YFbwrfRI9RQMYJbZ24vCTYYEg4j7Gh2a5b39B3b3LtLRD2mMGZSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
برخلاف شایعات مطرح شده؛ همانطور که گفتیم کادر فنی استقلال خواستار تمدید قرارداد جلال الدین ماشاریپوف شده و از مدیریت خواسته که قرارداد ستاره ازبکستانی آبی‌ها رو تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26736" target="_blank">📅 10:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26734">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msgRMgS0D1nIViBlCStWRqdBtvRvICsjnWvN73VrzcOwBO9jOK2JOY-oIO9bud6UWxVpXxs8EXhW4u76JFrDt4Ki6U9kZ3Ms_Ol4ZiWr_zdZSsBvdYl9S9sfnHCBxvfltnaLVuog7g0ljJQGRgepc8QhrblN9ksxluhHY2MNCgIklDHaRhpKrcT5XznVtDDuLYz3vYAYlcUychKSs26ZX1iCdI4GWVs_BpEBWzamRvNexR3GcFFw_yEqGePVX1JPlSEhQ3MuxCx9pK6YSBmf79eqTEWjaP584i4nxOuVNs0er5lwHh3LpCdYyJ5amQsIsig60ptQCBMXVxsuzGdFeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛ ایجنت ایرانی نزدیک به‌ عثمان‌ اندونگ به مهدی‌تارتار سرمربی تیم پرسپولیس گفته که اندونگ از سپاهان‌آفر دریافت کرده اما اگه او بخواد باپرداخت 600 هزار دلار میتواند رضایت نامه این بازیکن رو بگیرد و او رو به پرسپولیس بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26734" target="_blank">📅 09:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26733">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59d676a359.mp4?token=hptb5EtvmQxAa9CmWdoq-9axkbs5hSqmEJSvcB15SloHpwVTf4l2O4CSryfsMKIwCYtG6653_Qw4OwjEMHXZqNvKrStWUlFg1C3GaCXEpxClzGfoadkuRKMcN81KdWrdkFLIIAbPiUkdlbHKyoIjRT-WPRUVq5ln3y2dWAH6W-iEo0VkypfZyCwAe8KBcc4IpQ4TzVCmv6VitllN9CRPe2Zvz3JwH1zVid0xLKPTe5ZggIikgBheKSthw_Pg9LJT6Q3ewACPgiSL8P1EOv1gZSLqDANINFCV_cGnlOQnB4ZRLfChTdrxSRkJUnRkN2Y-G8gz68hDArQEcLBJsrKGPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59d676a359.mp4?token=hptb5EtvmQxAa9CmWdoq-9axkbs5hSqmEJSvcB15SloHpwVTf4l2O4CSryfsMKIwCYtG6653_Qw4OwjEMHXZqNvKrStWUlFg1C3GaCXEpxClzGfoadkuRKMcN81KdWrdkFLIIAbPiUkdlbHKyoIjRT-WPRUVq5ln3y2dWAH6W-iEo0VkypfZyCwAe8KBcc4IpQ4TzVCmv6VitllN9CRPe2Zvz3JwH1zVid0xLKPTe5ZggIikgBheKSthw_Pg9LJT6Q3ewACPgiSL8P1EOv1gZSLqDANINFCV_cGnlOQnB4ZRLfChTdrxSRkJUnRkN2Y-G8gz68hDArQEcLBJsrKGPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
تیم فوتبال چلسی تو بازی دوستانه امروز 3 - 2 از حریف عقب‌ افتاد ژابی هم کل تیمو کشید بیرون و بعد ترکیب اصلی گذاشت تا بتونن کامبک بزنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26733" target="_blank">📅 09:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26731">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01bf39426f.mp4?token=fuVz4oqNs2QkOPHPYJMdm-02D0vKI1C0sRcOJV_tE0QoGrC_VuqUOAtxm2hzac8nAR9CcNdusa8u4ntwNDGzhOUwigDsNFXKxPbckZiBhhipr5nZvN79MCgg2loEkecLObR-IYXSO4zrTZOm4DMaHCDKKmlqan2ju7oJxHcjoFU6SXTgxEzL6BOMbFQSUmwTuoxhdCSLe_gFvHY1A8yi_eFuii7N9aSRrBvfpwHYpU4pBH4LjJbTS94gBhmnV7hDz8rmZWKKKHam_kBbu4HtpuWAHuQppytb6LTgDcdJp4VSxTuim3aW2k2GoEqEfcy-2_sSWX--3YPmEuKpI4cGkjIw8gpXkz7_fhGqb3SKgJPDGP7aVMYj1WWLrmw4gFmO5juU7Z_EvZhIWgzd-HqWB5i8ktSu8NIGhUwDcn-4nYdTx_QWp87qK5XMdWCPiywRjVJ-p0HK-OvE4dOYdwMsxeg2TfF3cE8xTdvPN15BXy1l6dpo4AKLXONlGAh28_Bvr6rpR76ekL3ZixN8vyWoee4iaVgCpp9ZbS4sKcEocMYC_ZSFrDo6euoVnpLHyH7JqbgZOtiKIw_umfSNfNuKwGe0alF95IoYQVnNm_DLAKEPwamHELkQ9zqgKQMvXqnBWYnK-DCHAL-x3PYmnCrZ0-1aNBtYHe4TSg86T-dOxsY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01bf39426f.mp4?token=fuVz4oqNs2QkOPHPYJMdm-02D0vKI1C0sRcOJV_tE0QoGrC_VuqUOAtxm2hzac8nAR9CcNdusa8u4ntwNDGzhOUwigDsNFXKxPbckZiBhhipr5nZvN79MCgg2loEkecLObR-IYXSO4zrTZOm4DMaHCDKKmlqan2ju7oJxHcjoFU6SXTgxEzL6BOMbFQSUmwTuoxhdCSLe_gFvHY1A8yi_eFuii7N9aSRrBvfpwHYpU4pBH4LjJbTS94gBhmnV7hDz8rmZWKKKHam_kBbu4HtpuWAHuQppytb6LTgDcdJp4VSxTuim3aW2k2GoEqEfcy-2_sSWX--3YPmEuKpI4cGkjIw8gpXkz7_fhGqb3SKgJPDGP7aVMYj1WWLrmw4gFmO5juU7Z_EvZhIWgzd-HqWB5i8ktSu8NIGhUwDcn-4nYdTx_QWp87qK5XMdWCPiywRjVJ-p0HK-OvE4dOYdwMsxeg2TfF3cE8xTdvPN15BXy1l6dpo4AKLXONlGAh28_Bvr6rpR76ekL3ZixN8vyWoee4iaVgCpp9ZbS4sKcEocMYC_ZSFrDo6euoVnpLHyH7JqbgZOtiKIw_umfSNfNuKwGe0alF95IoYQVnNm_DLAKEPwamHELkQ9zqgKQMvXqnBWYnK-DCHAL-x3PYmnCrZ0-1aNBtYHe4TSg86T-dOxsY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علاقه بسیار شدید غزاله اکرمی بازیگر سینما و تلویزیون به مهاجم سابق استقلال: غلامرضا عنایتی ستاره سابق استقلال کراش دوران نوجوانی‌ام بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/26731" target="_blank">📅 09:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26730">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atuLuzCCxq4mCZVy1r0yihA80CRlCZDGW9AzIBv18xONLzL-JMVYhpA19r4ZIty7aoX6u0-s9NGmdibnLouN4HcjbZrTuLNA0hYCMd_KkMhmrFi5NNOhznP3tEOLpEki04m4TIP2PfdYqmuOvKmCXy2UfReaqmsjC7DRNyGvjGDin2rQ7rRXhO95uS_QpQxzo0IIPkdzRj8lb8i02HsIeCCFxglmB1F5x2SlHOnLtM-Ypksq_GVNLuPM_TvytFINPQSetMfThg_5WQ2-lKGl6BN6MFkpjTdJc5Lblo7i93PZPIwQ0nyslUE_8zFX0aqvCiVuJn8nUahcxEaO72eU1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
فلورین‌پلتنبرگ: ژابی‌آلونسو برای تقویت خط حمله باشگاه چلسی خواستار جذب دنی ولبک مهاجم انگلیسی 35 ساله سابق باشگاه آرسنال شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26730" target="_blank">📅 09:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26729">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5su6uStzn4BmoreRfOrKljllnA2B0GY1B__ewn_XqEIkaA5B7YmcPSqq-XSNu-Nad4SHf2I9bC1l6QrNFz5YEbuh8kgG3YRVyXIcwtaFC3LCkUwwRJMhX4-LB4S97HqtnW5pDRxxPrEQIIKjz1tYHfGVdT79DkHjvEJVc0GBhTPFOvq0orLb6euKm25vthQYY6OT-ItPhmprS-8uQ_MSHXXyGh893LyNw4K1jOgSF9aKPRR8h_9knPmqrQGlyzQdbaGhwYg6eJ4ovMgFIWlMdMpZXKOmWS3czFZPOEaNzO2bvtZ8-ZIIfr1HO6u8lgmAAA7GDpRtudt_SUAGWpu-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛
از مصاف دوتیم تاتنهام و دورتموند با تیم‌های آسیایی تا دیدار یاران صیادمنش در دور دوم پلی‌آف فصل آینده لیگ قهرمانان اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/persiana_Soccer/26729" target="_blank">📅 07:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26728">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqIOOMrw5Efnt1b5SwToDu48t9rxEZICU2zvPhrueTL7yzKWDDKGQX6ErWDo_t6zIGGt8zxTSMDmftkcZWhFndnjCLJVJ9viOdqpQAT2sQaRoHYzCo8o689NG2eZNDyL6kI_b0ImtsNh49EEjVDayLCY_EvP3VpSXQELSfbm3piB2wTCs3Yy4Oms-hj_VQa4MvmmoojxTE-kX-OFamT339dhGgLIfqUtd0Xi3GDXDEzXq4gzHEqMiylV5MU7aQp86GRG2U2cHRUZCCumuM5CC4Sjde4g6Mqm8bHxK-Daro7iV4_2Y2fwR7Z4A25CWSqAZLGSY2rFdMPeJNZ2VJCJhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدار های‌ دیروز؛
برتری شاگردان آلونسو بادرخشش‌ژوائو پدرو و بردآسان سفیدپوشان مادرید مقابل لگانس با ترکیب دوم
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/persiana_Soccer/26728" target="_blank">📅 07:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26726">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fAIQvG9BdQXarDHiD5ak6HDYTdFcBE8LGNN4oTvbHNMNTmRDoCP6IvUk7KFQPTSP39tAkj7rSe3-9TeSR85-3NVLllSprYY-mBvt770TftDr2DoUJnWmKyyZdwiI_REbbevU3bncDwGkb5pOHSFILeYrGYfNPNIMkf4thnSsinkdDVH4O4LXeA7B9VMqyoD6Yqs6DRF_cFomueJhQDu2IAFrxGRsZEkVdeww_MBq5Juab-ATZb5uZ9RCPUIcaL9JUnfIsfWzk6KZDpBYlnvVMmW4DXXuBExbDb2v4LTIcyPxGQyawS-9vK_T5kN0zQYzrQ_rseZ-DSeJgV7Ua0GAAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PKqW2l9FJsshhWkID7F2-vDcze9nXAysCjSpM1tS4CLvHPBD5Nl0ETwqWq1RwSez_TameX9hrWby7YCEp2MyEkIWCebwnF-X-USwB2FnDqP5ccMHvdjEYdovPNJIa9vYKs4f28DzLSMCLtWthZIhra-QF974Gf2Z8Yw0BDb8xGLtg2gNHhz4Wy165zSAF5tjGL9t0Prui1YulxTq_9jbqObuZ_zcfMOIkYOSIdrdB368EI2VulN3nplnfqNKkwY3w6q6hni_v2B1fNwJSzSk3FHOCRK498jn6H1VgcmrR07p4o44pWZNXTfZ4_RnjGirQT_8OUgpt0nWuIWRta5Lmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه مسابقات سپاهان
🆚
تراکتور تا پایان نیم فصل اول رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/persiana_Soccer/26726" target="_blank">📅 00:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26725">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRyy1BsvEwdplgwAbw-A0mfeWhkUsLxldlY9WwbO3VJF7yKjaDRPDreXxeOi4Uwc7BKMYfXoSCTo95debN5Ls1kA6FBpSiYmY3z1kL8x2NAorYNz-n2BZmJN9VpM2bQamHbm18phdsUYn8JBXTTeIMAL_06lnyBcCmnK8Ri1Wr35rR2xY4xT8DHx1QLMnRwlEy0ellpVdzRwUzkuqPP2GLHTFNsBswWVbhmGcWa8JJYtXfVm6Q2_mw-s-kAXkrtXDKYqp_GIaNiPIbb6yz-_9qI2cd_jldaMtZ1Wl7Lo8G2dfjoeGY4WlHHfCaeCGkKoMCkjN6QXXAw-n_0wxJWXhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ معاون باشگاه‌پرسپولیس امشب با سامان قدوس ستاره تیم ملی تماس‌گرفته و درتلاشه که او رو برای پیوستن به پرسپولیس راضی کنه. باشگاه پرسپولیس اعلام کرده مشکلی برای پرداخت رضایت نامه 500 هزار دلاری قدوس ندارد و تنها اوکی خود بازیکن…</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/persiana_Soccer/26725" target="_blank">📅 00:10 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
