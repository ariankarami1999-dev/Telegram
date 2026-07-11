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
<img src="https://cdn5.telesco.pe/file/a6TQU73zpo7YSwFtau3smlKrkw8KjNq9ZO6rEtloE4-ELkmHJU859mNADUSa2RQLl0LYQD8H86HSqKqFlfxpEjNoHWYO4CtETlv3CIvcuGfXwDga7aykBMx-IPEExu--xBdkyz-FHXqBuwdoixSv-g2u7eYgPFX7PVNz31_jaSeYbRU1Qspi_MxrjsdMXz_JoncDCSdE5dUtoyuA_AB5SunzL6nJLD7dbzHoRO-z04t-ublL6CUdLjvntt7Th94_rG7qTv52GuWuaAzxpX9VcXgTUKJMyDmAK6RLnu5_hnecrgGIVcnLN2pfJj-ML3JrgmcaYeupBpzQUmWIAe1IGQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 596K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 12:34:36</div>
<hr>

<div class="tg-post" id="msg-99532">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad73d33a3.mp4?token=V_rtCLCi3HZPk39dyOUbyI5P_lrKO7kqBSd7cZxusELG8AT2pMb6NfVI7kcbrElQJKw1uqNGNEUVoMQRrR9nMFuINYZi8To4iN4qkxBAD0kpxqv_kHL78YDR1hAaGJdqDoZhRtaAMf5V6-KCippL5xoQJ5tAF42BSDGoqZsgwEReeOHmbIQ_v6wH0xMBGQZ_WpLzmKlZDNMDK6XXiFDxRXXNfESYZWS0xvlWYlZ8o45oSXrDbN7RzP8De7IhZvHUXDxqf-WPYicw532lOIFlm68cFC8HM7LRTToKXJwrf8uycNpgGjotRejyWsKOtPfzq3D3rn81eJ7jupcpTR8zKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad73d33a3.mp4?token=V_rtCLCi3HZPk39dyOUbyI5P_lrKO7kqBSd7cZxusELG8AT2pMb6NfVI7kcbrElQJKw1uqNGNEUVoMQRrR9nMFuINYZi8To4iN4qkxBAD0kpxqv_kHL78YDR1hAaGJdqDoZhRtaAMf5V6-KCippL5xoQJ5tAF42BSDGoqZsgwEReeOHmbIQ_v6wH0xMBGQZ_WpLzmKlZDNMDK6XXiFDxRXXNfESYZWS0xvlWYlZ8o45oSXrDbN7RzP8De7IhZvHUXDxqf-WPYicw532lOIFlm68cFC8HM7LRTToKXJwrf8uycNpgGjotRejyWsKOtPfzq3D3rn81eJ7jupcpTR8zKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
بعضی وقتا اتفاقات تلخ و سخت باعث تغییر مسیر و زندگی ستاره‌ها میشه...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/Futball180TV/99532" target="_blank">📅 12:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99531">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/882a067f73.mp4?token=JP6eYT8E-lrXKXFeeJ1Ukz7wfKacheiZz7PuL-cew932fpwpjyPDlc58Il6e61kbUmsp90CkHnyssg_Omsn3StuFEsag_WDbPAOsYGVsMZfo8eYTyWMH5mI9Z6RAAdQ_E6rdA9p2iOle0mSSLfb48Q_7ruqg6KBFy-zbATQOB7SJNT5wpPGcEbqYgVwP6ahRWGkEEB0SdfdKZQewSUfc5gVHSdBi4rqGuev1e80gmQbrRjjB5tBVkKn6di0b-JHsxUyRCuLXVSrXUExpH272nBINDqjsNSZPxQ3wmYIrflPIBpiXvD4wpQCXspQuiXmIB107sR-rzCEmU9zQSWzV1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/882a067f73.mp4?token=JP6eYT8E-lrXKXFeeJ1Ukz7wfKacheiZz7PuL-cew932fpwpjyPDlc58Il6e61kbUmsp90CkHnyssg_Omsn3StuFEsag_WDbPAOsYGVsMZfo8eYTyWMH5mI9Z6RAAdQ_E6rdA9p2iOle0mSSLfb48Q_7ruqg6KBFy-zbATQOB7SJNT5wpPGcEbqYgVwP6ahRWGkEEB0SdfdKZQewSUfc5gVHSdBi4rqGuev1e80gmQbrRjjB5tBVkKn6di0b-JHsxUyRCuLXVSrXUExpH272nBINDqjsNSZPxQ3wmYIrflPIBpiXvD4wpQCXspQuiXmIB107sR-rzCEmU9zQSWzV1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🎙
ماجرای شماره گرفتن امیر کاظمی از وریا غفوری: رفیقم گفت آخه بی‌شعـ ـور تو وریا غفوری رو نمی‌شناسی؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/Futball180TV/99531" target="_blank">📅 12:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99530">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrPcvoSRcRIL1AImVh1a_9NnLCudK574NQWXKxBLRHwy7keVMOnsWzLNjG-8ODWtDw1K5BBvsHkxhCTwgtpA_V3SYawtkomnpHC2L0Ghj_vg0AUh62uqS5E-X2XzSz98LePq6Z5GJWQK3p7I1mxtp3Uir4YqVX__TKoN5QhDkXkZrCrKAwt_Q2zmanAdfcz-CE2kZ5r7Oor6-b_H8nyrZtv-16YuqcZAvcwv9n96O1QZSOeDdwUF50eHKcGuDvBELoIP-O1jVAOYZZRpQvmdZtqhbZkn0BgUsEY-oKtXvo35HDCbXNIrbbgH3oyUqJNXIrZghFud8sP2TOwILkvHJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
دی‌مارزیو: کورتیس‌جونز هافبک لیورپول مدنظر اینتر قرار گرفته و در صورت انجام این معامله باید رقمی بین ۳۵ تا ۴۰ میلیون یورو به لیورپول پرداخت شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/Futball180TV/99530" target="_blank">📅 11:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99529">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🔵
🔴
#اختصاصی_فوتبال‌180
#فوری
🔴
🔵
برخلاف اخبار منتشر شده در دقایق اخیر، باشگاه پرسپولیس تا این لحظه هیچ مذاکره‌‌ای با کوشکی و اسلامی دو بازیکن استقلال انجام نداده و این اخبار برای بازارگرمی و مختل شدن روند تمدید قرارداد این نفرات است. گفتنی‌ست که آبی‌پوشان به‌توافق خوبی با این دو برای تمدید قرارداد رسیده‌اند و با توجه به تعدد وینگرهای ترکیب پرسپولیس، شایعات در این زمینه صحت ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/Futball180TV/99529" target="_blank">📅 11:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99528">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d06676f902.mp4?token=MNGDntjKq7EgWhZZKFXf1OFvUBDLtNKMBGCZuWqLmNGMqoML5euyoiyjwl4GUVTkqq4zg7ygiUaYleJ9SCv2YqkSUV2qNzkZ8rC3TjjXEDo6oxKR5Fty6LWjtLQxUk8UDSmeGn4jX7oq2MbwOfTVPuWMT6SAxDj2iahk9tPCBkYwIYJrDdxLxnb4kH_ar1z4RjFdFP2q1VFsWYesuofmWHw1rOw_pS_pLn_LM_CY7tXa6gBSu0JQueDlUVCQHsSypWMqV6HX2zwxeIQLBu1soxQn5CExFF9T-UMx7J5znTJAWii8f36Q2xMz_G8e3U6ylIH50_tEPQzOMsE_ofBQPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d06676f902.mp4?token=MNGDntjKq7EgWhZZKFXf1OFvUBDLtNKMBGCZuWqLmNGMqoML5euyoiyjwl4GUVTkqq4zg7ygiUaYleJ9SCv2YqkSUV2qNzkZ8rC3TjjXEDo6oxKR5Fty6LWjtLQxUk8UDSmeGn4jX7oq2MbwOfTVPuWMT6SAxDj2iahk9tPCBkYwIYJrDdxLxnb4kH_ar1z4RjFdFP2q1VFsWYesuofmWHw1rOw_pS_pLn_LM_CY7tXa6gBSu0JQueDlUVCQHsSypWMqV6HX2zwxeIQLBu1soxQn5CExFF9T-UMx7J5znTJAWii8f36Q2xMz_G8e3U6ylIH50_tEPQzOMsE_ofBQPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
پست جدید صفحه رئال‌مادرید که نوشته شمارش معکوس آغاز شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/Futball180TV/99528" target="_blank">📅 11:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99527">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b08f3a463c.mp4?token=vdXGsZLD_fo57WO9kkkAORR__fUvUW2ztYSEjgaW9AngBD16UGOz5o6d8BCWUt5NoQEnjzHnx825ncrBzrS7RVNBbtJiYOU3axPHghhwrP8jvHSbtBAJ7tryb8fgnYidZ7w-Kimyb3xrGlxcdjD770Wwc8-7bFjxkr31H2kD_7yOMds4WMTn_XN4mlM0vEix3MNM2FA2ka8Iy09LSpK6HGtZuA6c3J1A4MELDPTci_bckrvFjEwUuE3E1U0l0QedZN_TvIjg9LsIBbFCdIb-0aCOSTWM5M7_5ZZXxlYRWWfSw4qcLFTjmdEsyUiLGhTSNiulfXkTjLIXADKzgqAzuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b08f3a463c.mp4?token=vdXGsZLD_fo57WO9kkkAORR__fUvUW2ztYSEjgaW9AngBD16UGOz5o6d8BCWUt5NoQEnjzHnx825ncrBzrS7RVNBbtJiYOU3axPHghhwrP8jvHSbtBAJ7tryb8fgnYidZ7w-Kimyb3xrGlxcdjD770Wwc8-7bFjxkr31H2kD_7yOMds4WMTn_XN4mlM0vEix3MNM2FA2ka8Iy09LSpK6HGtZuA6c3J1A4MELDPTci_bckrvFjEwUuE3E1U0l0QedZN_TvIjg9LsIBbFCdIb-0aCOSTWM5M7_5ZZXxlYRWWfSw4qcLFTjmdEsyUiLGhTSNiulfXkTjLIXADKzgqAzuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇬🇭
پشت‌پرده زندگی جادوگر معروف غنایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/99527" target="_blank">📅 11:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99526">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4raELVTegc2uvgVC9_SYvJmfN26TgscgvoBBSDAKsRBJPQBSfbthl19G_LPEHL9FKhdLBnHttH26HHGkh97lVQRYO7kWwjNlVktM8qSUi02i30OIE5jNSn8eHlk0GfMze-9fBN7hxrmNadJUwPDvuJ8hhJ9K22-t1j7d7N_YqmW3zjCQUxh3Z2THmTcbYp6QO2L0SDYLRcg-9Sgb_jvoEqYlMrMdgHCcls4S0XaNaZYfqbOmH1AHS-L1VBQXeZiZXVawzotQTuyEvZVjuqx67ruEGTOIHG9kvB-Gc2lMLfP5BHHoPMuJOAA0b8JAKwxi96siK_OsIadaOMQoDypqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🔵
رامین‌رضاییان که برای گذراندن تعطیلات خود به اسپانیا سفر کرده، هیچگونه پیشنهادی از تیم‌های لالیگایی ندارد و صرفا برای ماندن در استقلال خواستار افزایش رقم دستمزدش شده که باید دید هلدینگ‌خلیج‌فارس با درخواست وی موافقت میکند یا نه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/99526" target="_blank">📅 11:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99525">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c662948346.mp4?token=dlJs5d-nWTTRO-y-FKdrNAS124e2x-Gx7RfMbe_tKI5Nltm6RqK08yZgBWprWJUr2VGQfIaBpyUXGcskD5SO-PCezZzkHQlkXwTHgUpRVvZnN1ueLHVxcXKheVgQCVAQ80gchrJcAFY8XMrIi8gQZuvFEgT8qBrElTQKbUOQ21mo2-lXeZEouRwlAf5bsrxuZSgKMt8P_KlqmoTDMbvj2Bbykcn_h2gW2gSYt6an7-YPgxLPqJONbykHktTXrug4GCjPSyU4g8uOVNGmznimeA2_vAHrTMeRyLHXSUCHiCVmMyatVZ0xnC5CTqoW89mJDGNB33CKX3s2ZlH_HHBZOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c662948346.mp4?token=dlJs5d-nWTTRO-y-FKdrNAS124e2x-Gx7RfMbe_tKI5Nltm6RqK08yZgBWprWJUr2VGQfIaBpyUXGcskD5SO-PCezZzkHQlkXwTHgUpRVvZnN1ueLHVxcXKheVgQCVAQ80gchrJcAFY8XMrIi8gQZuvFEgT8qBrElTQKbUOQ21mo2-lXeZEouRwlAf5bsrxuZSgKMt8P_KlqmoTDMbvj2Bbykcn_h2gW2gSYt6an7-YPgxLPqJONbykHktTXrug4GCjPSyU4g8uOVNGmznimeA2_vAHrTMeRyLHXSUCHiCVmMyatVZ0xnC5CTqoW89mJDGNB33CKX3s2ZlH_HHBZOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل فردوسی‌پور هم به ۱۰ سانت و ۲۰ سانت معروف قلعه‌نویی کنایه زد
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/99525" target="_blank">📅 11:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99524">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChQaH8x3eAFrFF_yBhhVvVOrAgR8q1v-5h3pk9VHpJezGND1HSVEWRlvaozprVM6Hayt9dOQH5N1AEzYtOOvXWRuLZOp5GA7otZsS9kXisEOnd4JIzfFOovG3VDvhNoKEnQbeX57zfsnbp0YTK_BNoDvJhNeZ-DvpKpkgbRAku9i-76FkRnblxbpQqOtVC4r5ETzOii-mMKguVDjNlBBodhDVSJksUPrqlhVbIGsgGtAC6pW6lYhJh__8P0R-JuewY5-KGiJnndcGU99KWh2rSB2VTPqUyliZ9CxlrxkAoW4bnemD32Aoz11neadYJSDiq8SU-sTxxMErh3e9lpSHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
کوین دیبروینه و عیالش در بازی دیشب
🤍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/99524" target="_blank">📅 11:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99523">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53dd4678ff.mp4?token=bcjD1mWAnbAHHqGMFDlENVY8Mu_9n-qg6u6bXPBF7NIuBT0ai0biE7vc3za2uZ8RKrn4Za2aTRXsZA0YCCCbA5Y_htMvyXDGTxIfpDHgIobztVBYlA5XzMzPkxI37PVdnPxYzxt9Nd-iK_JMYEewgMI67x3DFQgFVGwA8cthS0AfQufMOF2A8nynOL91ofKbkMQnL1SYdUPz_EzyruwN38Dw_sPAmxIP0mRwGFdmrqPmeL_q1ZqsuFAPn45ZaaDWanEdj2NsAZnMedVcmQfL990hAuUKHvqBZr_edMoT3TulcKqyVAzH6VPZW6EwvQeCzbyMVkSGcfmJeHAMeEWQkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53dd4678ff.mp4?token=bcjD1mWAnbAHHqGMFDlENVY8Mu_9n-qg6u6bXPBF7NIuBT0ai0biE7vc3za2uZ8RKrn4Za2aTRXsZA0YCCCbA5Y_htMvyXDGTxIfpDHgIobztVBYlA5XzMzPkxI37PVdnPxYzxt9Nd-iK_JMYEewgMI67x3DFQgFVGwA8cthS0AfQufMOF2A8nynOL91ofKbkMQnL1SYdUPz_EzyruwN38Dw_sPAmxIP0mRwGFdmrqPmeL_q1ZqsuFAPn45ZaaDWanEdj2NsAZnMedVcmQfL990hAuUKHvqBZr_edMoT3TulcKqyVAzH6VPZW6EwvQeCzbyMVkSGcfmJeHAMeEWQkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⁉️
رضا جاودانی استقلالیه یا پرسپولیسی؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/99523" target="_blank">📅 10:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99522">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb0798a162.mp4?token=XVPY9ekOQ14HWq40Vd4lVMzsPfi9vuLIcIDo5qD4gCKWrVB3tUCUJa3EI9cEnO7LxcDxKlenNessv7X0knv7pBIWeJS2ZtNyt9RcQszjgjrov9uVoxyfJV24qGINpSsl5Hqu7M6LM723_-DejqkewTgBsjN2SzJsJHGwB68UVmwxIgV8B8Ou7WPZNtf_nL8CDMGFynxMlrVyffLWlndqG2pQWTDhQuTk8h8jVqbjCAoA3icKH3JZp5xds7DqlfXaR9hmJQVlacq7TiohlTsmTP-7gEwnmqGxgwqk2sbVCXaXFSDwtvHBEFausgq6c5OJc1hPkSwPvoUSF8DkDvOA9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb0798a162.mp4?token=XVPY9ekOQ14HWq40Vd4lVMzsPfi9vuLIcIDo5qD4gCKWrVB3tUCUJa3EI9cEnO7LxcDxKlenNessv7X0knv7pBIWeJS2ZtNyt9RcQszjgjrov9uVoxyfJV24qGINpSsl5Hqu7M6LM723_-DejqkewTgBsjN2SzJsJHGwB68UVmwxIgV8B8Ou7WPZNtf_nL8CDMGFynxMlrVyffLWlndqG2pQWTDhQuTk8h8jVqbjCAoA3icKH3JZp5xds7DqlfXaR9hmJQVlacq7TiohlTsmTP-7gEwnmqGxgwqk2sbVCXaXFSDwtvHBEFausgq6c5OJc1hPkSwPvoUSF8DkDvOA9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🏆
رقابت بر سر توپ طلا هم امسال خیلی جالب شده.
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/99522" target="_blank">📅 10:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99521">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‼️
⚠️
شکیل اونیل ستاره سابق بسکتبال NBA مهمان برنامه ناتالی فریدمن بازیگر و مجری آمریکایی شده که برای او پدیکور فوری میده. هرچقدر از سم بودن ۳ دقیقه بگم کمه
😂
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/99521" target="_blank">📅 10:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99520">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🎙
🔵
🔴
جزئیات قاپ زدن علی‌کریمی الماس فوتبال ایران از دست استقلالی‌ها: فتح‌الله زاده به من گفت دزد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/99520" target="_blank">📅 09:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99519">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae6aa61c60.mp4?token=ud8_GGUhIrhTMy23mm_xqAwW-_PVFfw1enFg0po9ILGGJRnlqikZWuraW2bAHVXVA5au88uWwHEwPPeu4vGRQdVBQI3BQDxEM9fvFBOTP-gkJWAI728E9Yy8TNNHqToJFg-bmEIE7XoZL5rhU7GdJ4EFOb8uj4tl8fs0FCzuIWAV5ZhtT58JJr48mAXh4-F1Qmx8HgrjmSgVyhyoylLdiiI8wGRBtoeVBUBVr5LIrM_yf8I6gdlP0wp2Hwz7B4FPfe2Bgbb2FvKTMc1Z-0BSlzMz0xggMt2D5wB24fQR7VurL7V3p0Xd1pjCcSNiaLLGMHIauxfJfLqg6LRUbYtWzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae6aa61c60.mp4?token=ud8_GGUhIrhTMy23mm_xqAwW-_PVFfw1enFg0po9ILGGJRnlqikZWuraW2bAHVXVA5au88uWwHEwPPeu4vGRQdVBQI3BQDxEM9fvFBOTP-gkJWAI728E9Yy8TNNHqToJFg-bmEIE7XoZL5rhU7GdJ4EFOb8uj4tl8fs0FCzuIWAV5ZhtT58JJr48mAXh4-F1Qmx8HgrjmSgVyhyoylLdiiI8wGRBtoeVBUBVr5LIrM_yf8I6gdlP0wp2Hwz7B4FPfe2Bgbb2FvKTMc1Z-0BSlzMz0xggMt2D5wB24fQR7VurL7V3p0Xd1pjCcSNiaLLGMHIauxfJfLqg6LRUbYtWzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
میثاقی دیشب ناینگولان رو آورده بود آنتن زنده که یه لحظه از دستش دررفت تبلیغ شراب کرد
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/99519" target="_blank">📅 09:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99518">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29484b00cb.mp4?token=S2JY59v1yJgKlez8AMjHjnffvh7yaBof5ez5u6AoLTUwrfAiaOCW3nCPjMUSy-XGy0bLHTQvsc8YkTSKjnlavy-qAoldt0AJ2tI35ynXTr3yl_ae8PJGCh0lnzP0I3KlwlF4eozTCOPrtMCU7aVL5KFe_o5Tk98wZF5GCCKIDLVnLalXKphsXD1TKRqxQeuxLh9tkNkUvozmbEss13JACZd5IvIdhpQ9RfSZWDPnI5eiTRzrLGXMU6d-QQaTXwZg4gHQ3hboKo-G0iiGiufYOw7xkqm_94aTSgCgS7jvoWX4PMVZvjKHmz3qgNnLp7QR4BtJC8Z4NPDrgmTacDB0Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29484b00cb.mp4?token=S2JY59v1yJgKlez8AMjHjnffvh7yaBof5ez5u6AoLTUwrfAiaOCW3nCPjMUSy-XGy0bLHTQvsc8YkTSKjnlavy-qAoldt0AJ2tI35ynXTr3yl_ae8PJGCh0lnzP0I3KlwlF4eozTCOPrtMCU7aVL5KFe_o5Tk98wZF5GCCKIDLVnLalXKphsXD1TKRqxQeuxLh9tkNkUvozmbEss13JACZd5IvIdhpQ9RfSZWDPnI5eiTRzrLGXMU6d-QQaTXwZg4gHQ3hboKo-G0iiGiufYOw7xkqm_94aTSgCgS7jvoWX4PMVZvjKHmz3qgNnLp7QR4BtJC8Z4NPDrgmTacDB0Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🔥
🏆
تکلیف اولین دیدار نیمه نهایی جام جهانی مشخص شد: اسپانیا-فرانسه!
🇪🇸
🇫🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/99518" target="_blank">📅 09:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99517">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovu4gkPkjRyHC8ttvoTuq0JSBKkMmQ-BrG83v2FP5ndm2wZGvY1WXyP5f4D5fwkCzRvNt2VC_LIxHI8V8grihAm5pouh4UFruhMNApSz87zSq2RCZ0bdQ51kL7jNml5ZaB50IhQ-07LSaxH9JTQw5ln6BetPf7-tM7Dq_e63x-BSHIQaBSA5l21DUC-g8ez4_CC6ZIDdF5gx_l9e_iJaHcTY3xqYU5VQ9j8UFPYo-rWCDODhoxjZX-cBpd3r2nvsyZmHaeVju7i9YAx8cbTuAVhhI1Mn3VMbbDdzojVUjQzQf-zRHSKL5RSnXmxNihLnIYwSKTxrQGRBlRgxZIxCog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
نیمار دیشب در تمجید از لامین‌یامال یه کیت با امضای خودش رو به دست ستاره اسپانیا رسوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/99517" target="_blank">📅 08:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99516">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3f60623d0f.mp4?token=Ou-H-ugxpNk_JMhM_By6RPi2W8os0Is0uatYGTqCPgUWHNuxNQsIgUkrdITPI1J1auWjUq4ddnrB5YojSQ0ZUdRJRvyTp4j9oMvVtC-EKRunrhjYcWXL3-H_JfX9QayNzLfIijJdroFXVYCmmbKYaVSd6XlaoYugZiBXYGYpt5o9O5Ju1k4LCec8WNgfwtyMcO9TheXnd55DkbqstwYKrbFpls5j70PFyKCySbfzXfCTeZSLqtGPA1VAxZw7Pe9-Wrc5laAhPGA9W27VZ8fGBuj29qLR1uR6GXAikPPgF-vQT9YVdW1mLM7ErHwDC2m6EJtfY3eIiZP88GYfnAwtGg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3f60623d0f.mp4?token=Ou-H-ugxpNk_JMhM_By6RPi2W8os0Is0uatYGTqCPgUWHNuxNQsIgUkrdITPI1J1auWjUq4ddnrB5YojSQ0ZUdRJRvyTp4j9oMvVtC-EKRunrhjYcWXL3-H_JfX9QayNzLfIijJdroFXVYCmmbKYaVSd6XlaoYugZiBXYGYpt5o9O5Ju1k4LCec8WNgfwtyMcO9TheXnd55DkbqstwYKrbFpls5j70PFyKCySbfzXfCTeZSLqtGPA1VAxZw7Pe9-Wrc5laAhPGA9W27VZ8fGBuj29qLR1uR6GXAikPPgF-vQT9YVdW1mLM7ErHwDC2m6EJtfY3eIiZP88GYfnAwtGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
آغوش گرم لامین‌یامال و تیبو کورتوا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/99516" target="_blank">📅 08:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99515">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
📰
فوری از فابریزیو رومانو:
👑
- باشگاه الهلال خواهان جذب رافینیا است و به شدت به او علاقه دارند، اما در حال حاضر، رافینیا تمایل به ماندن در بارسلونا دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/99515" target="_blank">📅 03:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99514">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gi2xn7TvFn-e8-j7tzPg_43W8UV0G_5gpRwzDxAnye7eWV5VOe2WZB2pxe9ImUwzLOoTAQm_-rk_yALN3VobD6vFFqc9nOKICLOIqDkcD2P8-fZu3efPxb7JFqccweJ4gt8WNdV8hWRz7jlLDXtp1Mbh4tuFhfNzGizBevGYufMeuEDpkxRLpVyJEwYO9ZJ08q7lPC1A9rnVLMxp3z6KT2oBh4ekvX4Pn99_I4a_H7kx_-IXP45O_A3BZWNeB9Su0kUxmycKtFiBOClpRabt1MV9g5yHbEVj5Z7mLYLgSAhYgGVQvUkcvbdZyXzWLujyQgewhIZOeBnUssAEMUVzPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📰
فوری از فابریزیو رومانو:
👑
- باشگاه الهلال خواهان جذب رافینیا است و به شدت به او علاقه دارند، اما در حال حاضر، رافینیا تمایل به ماندن در بارسلونا دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/99514" target="_blank">📅 03:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99512">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfNx7ANWIxc7-LQJuVidzlUbw432kkw1FeeFRackU15ymPtsxVDgQd0nPaAn34mCBPrfCUESjpzKVDzgRxd1tIIOtdpyMpwWTYJhzCEKEiK54cTznZsI8U7AYkD_eVDthbo1lfZT-aY8NbPBzaTrCk9Mn9X88xTi-2ua0mWJg2RC6ur7OfJ8cRDaFegq32y7Vk2sNvSBHQCqBNeYwmmI4SExtIAYsUIc-ECIqA3utfYheupl15zccaw1BbiO2Z-0onuggPWLCiIQfsO5XB-WKmY_EUd2RciCjUX1u9gOgejix94m1E2zw-CqVOSsZTeQrLU0R7l7Mi_KpPHVD_tJZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔵
رومانو:
پاریس سن ژرمن به شدت به جذب فران تورس علاقه‌منده و اونو برای جایگزینی گونزالو راموس زیر نظر داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/99512" target="_blank">📅 03:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99511">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pziDmPVadVDxwSCuJi86xylSPw9yNp5jX7jeCvdTQ3j58xePPXgOnEoubb2J21Z3fXAgQAxoH-TMF2xvTPWEm0aEGNoxWnZddOU9rH4HQP1SpFaQbdUzU0gZpc1RzaTZVvlG6-cBFJQ4heKz0220yBaOUQw87dniZURg4uwBy1oVldKo_9m5CZ4SFV5D-EUd5eb2bdLckT9q6ySNBK5whrZKo81B81AX_zHktSsBooTKiQDCMgHYVoIBUA-ZTs38HL3VitEu0ibiplP_4FJ0VH7Bn672DrJSTXhPqNpiNfN-8a5CziCWgELdlg8ig5D9tmMNQhUEjm7xcJMb5aK2Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هالند پیش زیدی بوده که یکی یواشکی میخواسته ازشون عکس و فیلم بگیره بعد هالند زودتر طرفو دیده و از یارو و زنش عکس گرفته گذاشته استوری و نوشته هی یو
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/99511" target="_blank">📅 03:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99510">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d0867b13a.mp4?token=Qr9uFYepKtEmtEhTL9gXwvUUWA3VIScJUEF4pvS78-k0AJhr6NUxSIrCBRiT46-CiRzd1lUqzsxyTlu9TU6zA3jIbBlDsSzPKe-BmCp0jeBRT-t4HtOSiaKyNEfr7dVs3Cnb2x-63pg1Ry_KLmljD0G9jOS_QlWbGLoeYXgt3YAE44dJxcDpGkucpJZDX0RTOF8msxvp9q0kJWEtI-KwN-tf5n2B7WKYjdDgS6JY0p2FDGdtN7GX10lUQVnuF2esFV4xMcGyo9O6fxK663qefR1mGIEhCm0dwbHs_B6WRCeJKPaqENhCsCm9fmeDL6X75Rypk4-lsc5jJEdh4lA1pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d0867b13a.mp4?token=Qr9uFYepKtEmtEhTL9gXwvUUWA3VIScJUEF4pvS78-k0AJhr6NUxSIrCBRiT46-CiRzd1lUqzsxyTlu9TU6zA3jIbBlDsSzPKe-BmCp0jeBRT-t4HtOSiaKyNEfr7dVs3Cnb2x-63pg1Ry_KLmljD0G9jOS_QlWbGLoeYXgt3YAE44dJxcDpGkucpJZDX0RTOF8msxvp9q0kJWEtI-KwN-tf5n2B7WKYjdDgS6JY0p2FDGdtN7GX10lUQVnuF2esFV4xMcGyo9O6fxK663qefR1mGIEhCm0dwbHs_B6WRCeJKPaqENhCsCm9fmeDL6X75Rypk4-lsc5jJEdh4lA1pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😭
گاهی پایان، با یک سوت آغاز می‌شود...
🔻
امشب فقط بلژیک حذف نشد؛ آخرین جام جهانی نسلی به پایان رسید که سال‌ها از آن به عنوان «نسل طلایی» یاد می‌شد. نسلی با ستاره‌هایی مثل کوین دی‌بروینه، روملو لوکاکو، تیبو کورتوا و اکسل ویتسل؛ تیمی که روی کاغذ، توانایی فتح دنیا را داشت اما بدون حتی یک جام بزرگ، صحنه را ترک می‌کند.
🔻
سال‌ها امید ساختند، لحظه‌های فراموش‌نشدنی خلق کردند و بلژیک را به جمع قدرت‌های فوتبال رساندند، اما جامی که شایسته‌اش بودند، هیچ‌وقت به دستانشان نرسید. اما بعضی نسل‌ها با جام‌ها به یاد آورده نمی‌شوند؛ با خاطرات، با احترام و با تأثیری که برای همیشه در تاریخ فوتبال بر جای می‌گذارند.
🥂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/99510" target="_blank">📅 02:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99509">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dN1Uff_9ILyiPEo7cw8ujHxsAYOIm22Jrz6Q2jXqKzuy5pHE5y2TacdxG7sJs1KqnUn7KrE0IADmk-O41bjodp9h9Z97_RW-98Mdhw3HCBZMmESU2_QFD9-5AlQ6JCCqNN_cqr1eIg6oEHQtZhcBC4utxJsODxM6-hIw94s3cfwngqahL9YUzbp6eHcZ7hkqHnrG1t_Ep8KvEkq9zlbLLMhWNR5-PZX3pIMH1kUk8sOUs76Qc6Nji6_2IcWwglR9MmG67aZU4aoGdisdpWAgh2YXL3odNSXNWGa24yeVl5Tipa2U1V6FU24prXMV9Y-3QorXi_gC3Ec6EB3P-3IJEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
طبق اعلام رسانه های نزدیک به بارسلونا، فران تورس از پاریسن ژرمن پیشنهاد دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/99509" target="_blank">📅 01:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99508">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
طبق اعلام رسانه های نزدیک به بارسلونا، فران تورس از پاریسن ژرمن پیشنهاد دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/99508" target="_blank">📅 01:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99507">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pl9snllZUUePjLsclFdwdvSXXhz1b-3wIudxBcVbCHPA76DE2dR1Y6yriWc2IFfGKaLxLuCY5ry5RvHxzHClvG3YVNvTS70MM_p4qxhXOpplyrOuAefn2G2EyHED3sfYzbTl648002iQytrlrfE7wkcZYggx8P0Qnm-vvoKjsp5bhPujV__iRWUDUYD2lFzPbTYZnUJdSXKlGml0aPEbO4HEHbgCkS039_i0DHuzjpO4xCAcTaitvnN2KTvxggwZx7Kd1KXoihU8tzGDQo_NumFsaGAJ5_SbXpnCYiB44IYqUkE4pZw4Q-Jtu68bEZRSnF38LLC-xKFMPnLl6iV7yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
16 سال پیش تو چنین روزی اسپانیا با شکست دادن هلند قهرمان جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/99507" target="_blank">📅 01:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99506">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLXN0HoXo9pLliHkqLdaEj8sK4HDbQCDVa-l7T1pBadMe_hvnz-ZnUDXg2DQLvBk54GQeVcadcSagl_mXzTWwa-FsqGesYecw3WjRZL0NbC4lM-_2nmQHizXfhG-HdimxI2StGXBMcIxe55xaf7e0OCip3UryzLA_UtIbaO5pL5yj2aXN6zpJdsm-LEZ07gOVsUMkrV5wRQi24_smt4hjoIm7xKPf8qqemP-FPCiHvxPzhmfIdV7XsisdL6efTJMfbNEMKB1MRA_DXcbYt56LPjka7A1_kDmqCzQYRpRM1-rSqjBc8o6Paiq5HhpEUd0fonoeijwXD_WDiO_YwLbsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
🇧🇪
تیبو کورتوآ: «می‌خواهم یک سال کامل استراحت کنم و در هیچ مسابقه‌ای با تیم ملی بلژیک شرکت نکنم، و سپس در مسابقات مقدماتی جام ملت‌های اروپا و خود جام ملت‌های اروپا در سال ۲۰۲۸ شرکت کنم. نمی‌دانم که آیا بلژیک با این موضوع موافقت خواهد کرد یا خیر.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/99506" target="_blank">📅 01:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99505">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gm_E1hxn6MrrYhYfu1tGX38mg5Itoz0eMhxmtAJcX3EJSOoylTQE0rra_EPYSBC1RHqHsK2bz2Gs-xoRPQ-wYNHIcFGsWsLTUIc0rnhY6jzAhHCBw4dRI5GQMuPRwOPhGuEBQugRrJ_O6scVur92Dc05hhfiv6HOs9OKGjD67CKZLiAWHnqAFNXaPyPTtRAjiTOgeYVAdqYMWsznKXephL-voqHcmZqsCJzEuv64zrWIQrB3uBhCScgw4RS6C0OQi9NJm4BT4IY8VDK4sHjzLWS8GIxeIskcpciLVtJC2Nn1RZjLP5ROXcc1oKmnH-ZNbVXAd1f96NtLnidxppGQ3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🚨
🔥
🚨
🔥
🇫🇷
🇪🇸
لامین یامال:
‏فرانسه یا برای بار سوم متوالی به مرحله فینال جام جهانی می‌رسد، یا ما آن‌ها را برای بار سوم متوالی شکست خواهیم داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/99505" target="_blank">📅 01:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99503">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
💔
💔
اشک های تیبو کورتوآ پس از تعویض در دیدار بلژیک مقابل اسپانیا به دلیل مصدومیت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/99503" target="_blank">📅 01:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99502">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqpNpKAT04G9W2yWGC95yAwcvfvDx7Q7EX7OaTJGXLcfW4IFUJt57OnttByk3Eyyjrwe7soxNJMi5znIIeIhMQ1eXD1w7g-N_TgFRiRIeX94uVYn0UCl6Bwu3SxsdelfAsgcRPH1yyhnyueL1i3b_bWUSLhdTkHuRIhJ0D_M1JfOIes05fahsfigqKOYwATPuzLjHl2irgzQ8Y0J-rLN-xO7wUKUa-8qM8mzQ-b5uy7ebo7X0vhu9Mw7VMyHT0VtWlE0Wf1pTaYpClBxEpM8b10vvT0W9QG3zyszPoIwW5pzHvDk2ZGeAeQPe7opam4wiI8n6m9rkgIvrgwhGKf1AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🎙
استارت رجزخوانی لامین یامال: « فکر می‌کنم اگر فرانسه قرار باشه از تیمی بترسه، آن تیم ما هستیم ، چون این ما بودیم که آن‌ها را حذف کردیم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/99502" target="_blank">📅 01:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99501">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b961be455f.mp4?token=dEu72Oa7R5uEig2mw7uQelQPnnWEyHJ3fvuoqw8x7ooAG3UpYkJphtkuCgQfiCupdjYQ-J_NrI69nl3Pe_MVKvWU0s5ftaIRnk7eq1XVDjYlwEeW_GuTInSvtvbeq98GWs_JLN4sWzAaeCbOJL5C6Q2RvAnPqRCSHrsOYnCTiuMLLa6_UT_6N1QqgIhjDLqPmagupv0DesUQpjbD76WIDEPvFchrsTuS9wFGWiTh-FLuhhsOs7RKRC6lP-P2LGsHFtaqi6gySQSdjD2XHCzwoC6Z7lX3yrb3RvHdUu6IIywY244WSYPTudoRvNO95P6UnrhKuWqYZj1Mpd9RIxuT4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b961be455f.mp4?token=dEu72Oa7R5uEig2mw7uQelQPnnWEyHJ3fvuoqw8x7ooAG3UpYkJphtkuCgQfiCupdjYQ-J_NrI69nl3Pe_MVKvWU0s5ftaIRnk7eq1XVDjYlwEeW_GuTInSvtvbeq98GWs_JLN4sWzAaeCbOJL5C6Q2RvAnPqRCSHrsOYnCTiuMLLa6_UT_6N1QqgIhjDLqPmagupv0DesUQpjbD76WIDEPvFchrsTuS9wFGWiTh-FLuhhsOs7RKRC6lP-P2LGsHFtaqi6gySQSdjD2XHCzwoC6Z7lX3yrb3RvHdUu6IIywY244WSYPTudoRvNO95P6UnrhKuWqYZj1Mpd9RIxuT4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش یامال چرا اینجوری میکنه
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/99501" target="_blank">📅 01:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99500">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87d00634e4.mp4?token=S14J4m3IIfErTXe6_6TN9BBHLuJGa0nM29QuLhhl7hJHeg1LhUvd2VtpM-LogPgR0wHBkVLYbSm3mi5HhXA1o1DZuadq1WZlu8SGqbDHexXYpnxnnwrgXsSsC2tn99DM7wRIdN2tvd6a39OMz0iL1INKYoQyMS2z3xHCkKV1uLNkHIh8P2_15StNeKYHmA3125_I3DoM4P1BTQ6fBnv_7cMGhhxzbUQXWJyy1LZ4QM5NqOu0F479GkY-I_rS0XCo3obTEd76ELNN6YsS3Sqsrx27hUWSJa8w43RLPfqG8cH-JhNYszLX0_UcjucAvsgjHPk1j_nzEFdSXOz-q9p-JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87d00634e4.mp4?token=S14J4m3IIfErTXe6_6TN9BBHLuJGa0nM29QuLhhl7hJHeg1LhUvd2VtpM-LogPgR0wHBkVLYbSm3mi5HhXA1o1DZuadq1WZlu8SGqbDHexXYpnxnnwrgXsSsC2tn99DM7wRIdN2tvd6a39OMz0iL1INKYoQyMS2z3xHCkKV1uLNkHIh8P2_15StNeKYHmA3125_I3DoM4P1BTQ6fBnv_7cMGhhxzbUQXWJyy1LZ4QM5NqOu0F479GkY-I_rS0XCo3obTEd76ELNN6YsS3Sqsrx27hUWSJa8w43RLPfqG8cH-JhNYszLX0_UcjucAvsgjHPk1j_nzEFdSXOz-q9p-JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
MOTM
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/99500" target="_blank">📅 00:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99499">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CG3hGOt6vt2ATwBWqHA6PwyQcmQrPit-5CfjDvEvs-GM_K5N50vmtpb1JCX0LRCx0jeigtP1QsgRMSn6JIBXGrvlCLPKhyaK7WIUyGtbt3VZt1s-Q3SwWBtQ_yyfX7uijB3F8tu2h-wCy8a_OjGU5RQ4k7PL7FTyI8HNXv6lFZ6YCaLqQ-DoGTjj49_dETF5FhC1VSM5ljEo6CRtL6xWlnrIo_w51sjHv5JIp8VHhsITGzq_eEvinTp7x1We0cl3PiKWi9uZXa1LiDy3AOdxvJlxGZFjW3tVYESdhIy19WYjNqW7DM0jFTBzbAnT-mnyIuk_rZKjDbGYHxHx4bntyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🤯
🇪🇸
فابیان رویز تا به امروز هیچ مسابقه‌ای را با پیراهن تیم ملی اسپانیا نباخته است:
‏
📊
48 مسابقه؛ 33 پیروزی؛  15 تساوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/99499" target="_blank">📅 00:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99498">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">📊
🇪🇸
مرينو در دو بازی آخر در جام جهانی:
🇵🇹
در دقایق پایانی بازی مقابل پرتغال، او یک گل زد و باعث شد اسپانیا به دور یک‌چهارم نهایی راه پیدا کند.
🇧🇪
همچنین، در 5 دقیقه پایانی بازی مقابل بلژیک، او یک گل زد و اسپانیا به نیمه‌نهایی رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/99498" target="_blank">📅 00:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99497">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQw9-x08b7-dzCEsaYxfWP3vV8-lj_xKmH3Q3_oq77AHVfSYtGUWWq88xq8fW5AWtUS9PGLwvmvGy0TytnnaWHHfs03r9nQ0nCxF6Symn9vRRF2M4Lr3Q17ewAWiq4WWa2uNiriDdqmhCgQ11QaqVhb6sTkaZS2nBbNqDmRhhxhvOU-cUMmrS7kao36EBQnPaaACqIog9V78A4y0N_mrNhHSXdbnoNb6np7rNXk31lZ5j8rArKbTBG4XriIolEj-s7gd1_gkE_rg-O3sLO5rv3LGya8qUtZYxe-VNgR3i7PfoXx3jkSQywMMiILpF0C87yCd0NsvewLLS9VldOGQ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🔥
اسپانیا با پیروزی در این مسابقه، برای 36 بازی متوالی، بدون شکست باقی ماند و یک رکورد جدید در تاریخ این تیم را به ثبت رساند.
✔️
‏آمار این روند: ‏27 برد؛ ‏9 تساوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/99497" target="_blank">📅 00:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99496">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app.apk</div>
  <div class="tg-doc-extra">51.3 MB</div>
</div>
<a href="https://t.me/Futball180TV/99496" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📱
اپلیکیشن اندروید بدون فیلتر لنز بت
🚀
🛡
ثبت نام آسان و سریع
✔️
📱
اپ
ل
یکیشن را روی موبایل اندروید خود
نصب کنید و بدون نیاز به
🔤
🔤
🔤
وارد سایت شوید
💬</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/99496" target="_blank">📅 00:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99495">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ZWOSisUuQFXXlIyBXUs34SLKCDjnN0ewF1L4EeGxp9f-gRf_sw10GqVj1_7BRt_Fiujqje9QgZDylzPHe_F1MjenYMufJZPVCdcrf8u-76MP2cWMDb3g-9Oru5GITRN4jPkMLOxq8qXHq-mA84Qf9XxdttZjgMbTuJX1goHmqLadendVWNlPCH_x6cdenk1XM-xAMvboJuSpv5tEVOc7qtLAbl1vvNRbSSbiR_MPoOSFfQ9zkQU-rnMc4Q75ZohmtD_z8653qrOZL303XtPWxoOjcn6Xs66Nk65bPmn-OeSXbeimKjiFbMrit0UvT7D-Bx_2qZt-uPDQdtJkNFeEgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
قهرمان جام جهانی ۲۰۲۶ از نگاه شما کدام تیم است؟
✨
با پیشبینی قهرمان جام جهانی شانس چندین برابر شدن بردتو امتحان کن
🚀
💥
متنوع ترین آپشنهای پیشبینی در
لنزبت
😮
بونوس
🛍
0️⃣
0️⃣
2️⃣
خوش آمد گویی
💯
بونوس
🔤
0️⃣
0️⃣
1️⃣
برای هر واریز
💯
بونوس
🔤
0️⃣
0️⃣
1️⃣
کازینو
🏦
کد هدیه
0️⃣
2️⃣
🔤
🔤
بعد از واریز
🔣
0️⃣
3️⃣
کش بک هفتگی
📇
امتیاز وفاداری با انواع هدایای نقدی   روزانه مخصوص کاربران فعال لنزبت
💵
پشتیبانی از تمامی ارزهای دیجیتال و کارت به کارت آنلاین برای شارژ و برداشت
🔤
🔤
🔤
🔤
🔤
🔤
🔤
📱
@lenzbet_official
A19
📱
https://www.lenzbet1.living</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/99495" target="_blank">📅 00:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99494">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOjMWq2tf_H4_Lv3fDjBLZ5VKkfZNJMtos6vfHxyPgNFv3i8qgKhmj-O4wJ4HXN7KaGc01kMrXbelCN3buuvbDJnLnMlZGv-GmA-WI2r5uuC_pyi68V69SIiTkCBbsFru4mai-Z-JfB-G-pWcRkA6G_1t-YSQITteN-DUL1BqJ4PhkvwuZtWXpiNq-DVjgkVUSXRPYevG3Dfp1lzzXIF8SUofhrhWUHfQavuUPuy-054vK12_twlj0sVqAVYCTY3Rne0_MciQhAVqcTW1vq4W3eqOFlq-eORRSsH_Eri7PNZbrZOVsDAUTdUulyCJ_hULszm9BbsIuJ3APjM_nvfog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
در 11 بازی اخیر که لامین یامال از ابتدا در ترکیب اصلی تیم ملی اسپانیا حضور داشته، اسپانیا در مسابقات بزرگ (یورو + جام جهانی) پیروز شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/99494" target="_blank">📅 00:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99493">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
؛ دکلان‌رایس، مارک‌گهی و ریس جیمز در آستانه بازی با نروژ به تمرینات انگلیس بازگشتند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/99493" target="_blank">📅 00:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99492">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGC_1qtbeUkckq6-wh35rp1R1xTimI_9hgh9Ua8944CLtGPbJfbQ1-lNGTsN1WzRVbWvond2FSpWo-uC-Xbnh3N_wcpvY4GacWCD41hesbkNK369AlS_MQdqSenHMqQW_zqexC_91iuw_x-AEfGyf6o52EkOGYqipmKcWxa4DYbpXHdQ-UYaXLks9ZDiR8W_Rln0o1bPkCpebQu_SzFoA0xRGCNgRUvDBUA4ulxeEO1bMOLqCqBlvw-NcHoRUO_qmCTkq2GXfFh25-6fuVQdptSqSMOwDVOlN79KI3G97PAJbFP3TnSDhLj8C1Qax_NVu_4x29bq96WqN4lScP5t7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
مرينو در دو بازی آخر در جام جهانی:
🇵🇹
در دقایق پایانی بازی مقابل پرتغال، او یک گل زد و باعث شد اسپانیا به دور یک‌چهارم نهایی راه پیدا کند.
🇧🇪
همچنین، در 5 دقیقه پایانی بازی مقابل بلژیک، او یک گل زد و اسپانیا به نیمه‌نهایی رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/99492" target="_blank">📅 00:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99491">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bajbo-_OEVpm1SOc9t8QExwmwNP41gQb1v4-WVqK9wmYIsuLfPk-Nuil_dzMZ-2ps5l0FYqcXgIX1OeANgwoKtExr4M06cGDQV9rnaprVoThS1vA7YKK7e_KJZq8hk9bLZxJ0le9dqR_X4vsOlEJnjzU7bONz33UGikYZNvBpsPyU3uxoIDh854mQCPpeq8HsDB-1eZZwYKZjnX2N1aDsOwrnflMpYUEIQnDLr4Mt7127Db5uwPel0rm21rck7gUmvA7n8i9VBKHcfUUjVjZB28CHvMFC-jQ0aARtOXgcAz1ZzHxMZK2kHZvOMk-cjFSZVZ9IlrvBfhhfq3I05OrzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
اسپانیا پس از سال 2010 برای دومین بار در تاریخ به نیمه نهایی جام جهانی رسید
‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/99491" target="_blank">📅 00:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99489">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aS8ShKb3REDeVL1b5gMRxCvbt-cHcwyfmBkPFMjkREoRaUc7I9ILmqpf8ZpWN2G7koHqIRC6QRKu9gTJCNLB4eexKy8x7jv0V_wiDdRGfcHtu7PYNGXViuKNrU23aJcuiPWs2urAHZyLyNZ5cpkQlK0ibt1JOgChlLTphAPZxSPSy3m67WPZgTKMWKUSSPuUvWnNQlBvAVL-xdZXo7EVH5qW7rIx7u2MeCu_BmUqS0l9xG0X78o1WXgm_P_iLS3HubYpcZSieRDu02kKrKUATf6j-SepTDYzCYyH9cOUxx-3KtTJOtnnHxRN4KY2Z77HFVA_kb461M7IixRx__hCgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KlJ37RLbzma1207oUkZ4a4hnkm3wu9ETxVJBnW-ICSg2Y4SNcAmYmB-9yg4ryvA-JFLCKLKYLUU0BIwoF8H53qCU0_LR0lgSD1qoeOtx77Do5yTrbt2zzS5OQPHJKWMySIv8Wo5XeN_s6Pfr8MKiR74uIqLGzq7cJ1TbXli9ue-hOkdNXGENOYap6WTWaFtLIqG_heZ12TL5FwPCUZhF9KAz6j21eXmmec0k6dtKvr4Rvs7AadDZSM-U2UB0_K-lSonu8o5dKfDa3gFWDDxrk0dEhkIaQxPliJHanGO5SYdrix7gjII-_35jVM5Pj_7r2qMILfDfxgv4632MgCO4Mg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">داش یامال تو استادیوم
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/99489" target="_blank">📅 00:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99487">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqXbkVSsNODsZDD4ps4UAIA1PEUhYSA_-p_zkzVfDwAEAl4m-a-2Yltlc60WRiO2pu1QKhd38KReuNrQ8PgsEwB33uybRKJ0LTyRPIf6BhnKwT_QmRjnkpNVcPJiMxhN5gnXlVwwbqf44El7U8pIQdvukYKNfj6amqsJ4IJ4kHrUxlxjalnS80ZH3AkqNa1LsYw1BJp-bQkaXVkXvZl9yZ2hNGVwNDwoiQAYDLvGLaZeBZ1sXsxvyKOUSzjStEQMSlsCkbmw0SqbtrNnI-X3W5Vv2TkYk55eeBjdcqopXdrGp_HBLnxwSrcWtiFhlug4bxKDBlPFBiE7A5Tk7nLOKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
🏆
🇪🇸
آمار بازی امشب بلژیک و اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/99487" target="_blank">📅 00:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99486">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnyQ_dIq1Vpf1hM6K8RYA7iiHlzyxuImXHu0CxHSq3o-04m6WBdQyRgIwSdz7coihDD6Xzd0Uf_rIhA-vNj2gfy2KLWmnZWuYgxSSyOAaprWotwZUWqdnhOx80JQRsERVP-2bqdE1jdC3F6L6q-SyE_MujJ8g61bypnRvyhc1IteaA2XXn1nH-v6jwa8CCBf0v2DtIcvQvlYW48fY9rL3vNP6mL9y_AOSYDkxlTA9xfa-mvthwgm6bZ7ReXzae8tMsGEtjw98fuAj-rmOhwpKoPEhk_PPWMToesxlTwgo_2PHsiFPcXvcSVcoMcv0JlBYqux12zMRt4EbSVZMklYyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آپدیت نمودار جام جهانی؛ این سمت که واقعا جذاب شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/99486" target="_blank">📅 00:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99485">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYbQsajnCohoKGUP--80-DCyTsjRkKev3ljjry0uTiCta2BYcXiAmFpCTqF1QC03xip_UunEbPwAhzUTVzeBMm-_V6FZ3Nx7oOz-Qr7YDN8YODyHOg47_axVyZbSUyWy8JY2soYwdvKZZTVLCNhaV9BDwG_XEJr-cR7Z9crmOOjoWhcOeUtehNu-R8hO3ct5Fr16QCxIYlHdl7V7JhfQmvj6OTS0uQ9zt4EaKR0ref7p7n7PmuyA56756TxVktZv6HHomp-wpinhUMpFdzIy-arEB617uMiJURWbT6ADAEvpWsHYrwyJdNhprQXWTUW47XNz1sDoKuMfUUaWK1G78Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|داستان اسپانیا در جام‌جهانی همچنان ادامه دارد؛ راوی قصه ستاره آرسنال است! بلژیک در کمال شایستگی حذف شد
🇧🇪
بلژیک
😃
😀
اسپانیا
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/99485" target="_blank">📅 00:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99484">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YR6Wue2JddB72yEr1W4HCqat42RI99wStbrSApWudC9HsLufI7RkH03G5Lot1ECYXPLFuhLbzW6vHzG4MNfK_hVbV9nzdoS_ncfDwS1epgEB6BWfDdx00Zsg1JLUW5wVir4MX870uSq6P910R2LxeYPcxrolbGi1OcIivVldDh_8vFZx9jCJHWa_MxtOv-jsN9SA68Yy0ez2R0aPpxT6iYoFvOssTZ3UtU43S4k8ysmToj52spKTim1M5qaoA2iDSYW5JV74BwiBfD83deFEdaRFZVcoPJW6QJvA2sPcQ0aq7pKj4vJJZMJNXnzTCVUqkG1E6ev8jr1txpSM1Oih6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🏆
نیمه‌نهایی جام‌جهانی فوتبال
🇪🇸
اسپانیا
🆚
فرانسه
🇫🇷
🗓
سه‌شنبه ۲۳ تیر ساعت 22:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/99484" target="_blank">📅 00:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99483">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oa6qPl1zgotmtQICRTSbMU1s3qRuBOUQh9lR3hkAEpDPiwWv3Lx6fY4fI6DUnULEwOLgJwJ-4KhHcdO9rsHV6_49amd0ZGpUbiM1cfz9FhWExhtFq8n3NBsSgWfN5y31eYI3cLLjnu3upQhcUQkANAmCheTpjwIV90_Z8n1VUCvtxXp4oAISwmIK7BIfFZ3eDrswR_ZlnOixSZwzehEJPQh3DaEnaHzJEVif3dNwChSczgZg7DrAMvX8poNE8BW1Kc_AhEJgVpElGYt131ZWv7_bJSlhiG9iJcDgthF61qoHmcgTkC_VhPen8Q0L1L64qwMQ0cIdTrqJISXk1GKASg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|داستان اسپانیا در جام‌جهانی همچنان ادامه دارد؛ راوی قصه ستاره آرسنال است! بلژیک در کمال شایستگی حذف شد
🇧🇪
بلژیک
😃
😀
اسپانیا
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/99483" target="_blank">📅 00:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99482">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پدری ریدددددد</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/99482" target="_blank">📅 00:25 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99481">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">چه توپییییی در آورد لاپورتتتتتتتت</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/99481" target="_blank">📅 00:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99480">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/99480" target="_blank">📅 00:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99479">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">هفتتتتت دقیقه فقط تا پایان</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/99479" target="_blank">📅 00:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99478">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بلژیک اونجایی که کورتوا مصدوم شد بازیو باخت</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/99478" target="_blank">📅 00:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99477">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e4b3fe7a64.mp4?token=PtjeS38ETg7GFwUek9gDST3nlTl9nHfyFfhFdGnPrQgFhAUq-EzP1KeyVR_HbQY3SS2hY-wWjQyK6sUON-MmOKrDX2Rh3qQFAVfuhUXolB6NiESQIwF5PwdIboEV7palqwSlLXA8Vy40bMPkWP89BZGwBxCTxDF1kV8KvNhqOcZMsujN9rFYnZOZEHMSrHf2EXDy2khA_lwstc5Q0gm_YpVHOVqRqgkZO8M55-Y83MRAkv1kfR70-edW-g3P3KfBt-Fek-2OWLrOGLCGuGIqlh2y-TeDFQdcegGOudUGQk7T9Ru9-tIe54oNR0tC8gJzYr1Nldx5GTY9LXOEyq9b1XUyNnyhPN6COjlqk-GLqhdaaNTcO0qc6YHzEvzxW33fKNOiI6tnjbCtehkMmHmLnatqe09KBFmWQfDryDCuJXhUL8k1zqPKld1qL9MT3GMpdczuXApwlGh1PJ8Z5WOqSME14TkFmkYm2ACECVmaAihBX2IC3Yf5-NNBh0HLyTD1ZKe7TYjFtL7tN65ALE1JbS4VMm5Sjb7B-EWmkalUN8ZQTvSS7XDZaktem3aWRuUmPLRFQ77PbimX-GV-pyf0BP6zrpUkgmOkBV3McAavjQuHl3UyU-7on8lWUYsHUrEVksRKM9N76H6ftdTwDZTPXllQpLLdSowbKZTNK-QDjTo" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e4b3fe7a64.mp4?token=PtjeS38ETg7GFwUek9gDST3nlTl9nHfyFfhFdGnPrQgFhAUq-EzP1KeyVR_HbQY3SS2hY-wWjQyK6sUON-MmOKrDX2Rh3qQFAVfuhUXolB6NiESQIwF5PwdIboEV7palqwSlLXA8Vy40bMPkWP89BZGwBxCTxDF1kV8KvNhqOcZMsujN9rFYnZOZEHMSrHf2EXDy2khA_lwstc5Q0gm_YpVHOVqRqgkZO8M55-Y83MRAkv1kfR70-edW-g3P3KfBt-Fek-2OWLrOGLCGuGIqlh2y-TeDFQdcegGOudUGQk7T9Ru9-tIe54oNR0tC8gJzYr1Nldx5GTY9LXOEyq9b1XUyNnyhPN6COjlqk-GLqhdaaNTcO0qc6YHzEvzxW33fKNOiI6tnjbCtehkMmHmLnatqe09KBFmWQfDryDCuJXhUL8k1zqPKld1qL9MT3GMpdczuXApwlGh1PJ8Z5WOqSME14TkFmkYm2ACECVmaAihBX2IC3Yf5-NNBh0HLyTD1ZKe7TYjFtL7tN65ALE1JbS4VMm5Sjb7B-EWmkalUN8ZQTvSS7XDZaktem3aWRuUmPLRFQ77PbimX-GV-pyf0BP6zrpUkgmOkBV3McAavjQuHl3UyU-7on8lWUYsHUrEVksRKM9N76H6ftdTwDZTPXllQpLLdSowbKZTNK-QDjTo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
گل‌دوم اسپانیا به بلژیک توسط مرینو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/99477" target="_blank">📅 00:21 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99476">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مرینو عشققققققق</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/99476" target="_blank">📅 00:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99475">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">چه شاهکاریه این مرینوووووو</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/99475" target="_blank">📅 00:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99474">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گلگلگگلگلگلگلگلگلگلگلگلگللللللللللللللللل</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/99474" target="_blank">📅 00:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99473">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">گلگلگگلگلگلگلگلگلگلگلگللللل</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/99473" target="_blank">📅 00:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99472">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گل دومممممممممم</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/99472" target="_blank">📅 00:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99471">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اسپانیااااااااا</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/99471" target="_blank">📅 00:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99470">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">مرینوووووووو</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/99470" target="_blank">📅 00:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99469">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گللللللللللللل دوممم</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/99469" target="_blank">📅 00:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99468">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گلگلگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/99468" target="_blank">📅 00:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99467">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">مرینو عشق پرتغالیا اومد</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/99467" target="_blank">📅 00:18 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99466">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6497dfae.mp4?token=LO2C2WIuR26MG9apzKq6zmPqnfhrTOS9XOB-5HeGkAsWeIDsus6s8ljrXXqTbdmryG5fIBbZdvioTgnnxmm6dEyYi-o-G4HIb-EqVURevGn7rxDeeBUzR1M5uI051g62joljO6EfA9vTOoFEpVQ3APAfe5U6npis4rwt41hHiWlNoRVmhyxXEs57oEedWh0KsitmxnhrpixBCl7Yqe6VnJ5NHY6jnAsWzHUiiTQ0zloBZmgaSpAAav1G1fAngPSnx6LO_9Z9zm01H-d2ziG3hSNfBDWmo2wJsH6oenFVFh6W_MrVsu0lsKjyst3mReTrFo0bGbNfBM9oXCT--u6npg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6497dfae.mp4?token=LO2C2WIuR26MG9apzKq6zmPqnfhrTOS9XOB-5HeGkAsWeIDsus6s8ljrXXqTbdmryG5fIBbZdvioTgnnxmm6dEyYi-o-G4HIb-EqVURevGn7rxDeeBUzR1M5uI051g62joljO6EfA9vTOoFEpVQ3APAfe5U6npis4rwt41hHiWlNoRVmhyxXEs57oEedWh0KsitmxnhrpixBCl7Yqe6VnJ5NHY6jnAsWzHUiiTQ0zloBZmgaSpAAav1G1fAngPSnx6LO_9Z9zm01H-d2ziG3hSNfBDWmo2wJsH6oenFVFh6W_MrVsu0lsKjyst3mReTrFo0bGbNfBM9oXCT--u6npg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
💔
💔
اشک های تیبو کورتوآ پس از تعویض در دیدار بلژیک مقابل اسپانیا به دلیل مصدومیت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/99466" target="_blank">📅 00:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99465">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXOxrzZo7K9VVK7DbGN4KxR-JaPMv7EnLsVSVUexd_pB1EHGeeU95QhREO2ZjyQIcK8zwHwt4udI56Sa1kNSoWWjH5tJAhZAV5w74-TqdQlfPkNE8Kle2nz2xACY0zh4vJp-K4tsIxunRMZQpv-nZZBUXRgSiJtERByXELEzAzV7k9CdRAgofuwqKG-bX9CRzu4YTMbVg-hnhAiX3FTsR_9O12teVo3a2Sa78yrrSpllvwiK4PWUDbrtE_Hxksz_YhLjnzJ3vZue0DVj7PNJIpQWgZDosVZYjj-HxJH9ckkSgaa7yplBKGzR3vm8RouKRWYPQ4AlTgAOICkhLUiWRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گریه‌های شدید تیبو کورتوا
🚨
🚨
🚨
🚨
😐</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/99465" target="_blank">📅 00:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99464">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">کورتوا تعویض شدددددد
😐
😐
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/99464" target="_blank">📅 00:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99463">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دو تیم خوب بازی میکنن</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/99463" target="_blank">📅 23:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99462">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بلژیک چه ضدحمله هایی میزنه</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/99462" target="_blank">📅 23:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99461">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">آغاز نیمه‌دوم بازی اسپانیا و بلژیک</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/99461" target="_blank">📅 23:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99460">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
❌
📰
فابریزیو رومانو: انتقال ادرسون ستاره برزیلی آتالانتا به منچستریونایتد منتفی شد. این بازیکن به این تیم نخواهد پیوست.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دلیل لغو قرارداد، بروز نگرانی‌های پزشکی پس از انجام بخش اول معاینات پزشکی بود. (این نگرانی‌ها به ویژه مربوط به آسیب قبلی زانو، به…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/99460" target="_blank">📅 23:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99459">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇪🇸
🏆
• 10 گلی که اسپانیا در جام جهانی 2026 به ثمر رساند:
6 گل در نیمه اول.
4 گل در نیمه دوم.
🇧🇪
🏆
گل‌های تیم بلژیک در جام جهانی 2026:
‏4 گل در نیمه اول.
‏9 گل در نیمه دوم.
‏1 گل در وقت‌های اضافه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/99459" target="_blank">📅 23:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99458">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aaRye7MpPpx2zbr_Up-nWrJPiSM9YlIkFVZqz51JIUIqB73VAOEBIicxhfU8rsuOWlM86ELqi8JlteP_jfEWZdoD64o1qMYOpf00uWNIpXGs7TEylcFserhF-KGULsgQVG2xpLjwh6PguNS5LRrihX24sZ8__ZWFWFczMbLpZIcrAhZQ-7qCMOUXA4pNfHBBoU1iAeJgD3kn2KpVoFF-Fgd4hNJs0ljvFW5nHWYhbT1UPdZJ8VTKoVFOrSaPsJAnWIKg8qu3DZkDSnN5KUShlSdM8l4wN_EIyToS_DxM6ZLKTXax3u6-b4KiaeSrJuFNKLEoeUARYswa-UE19jAUeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇧🇪
دکتلاره (با ۳ گل) به عنوان بهترین گلزن تاریخ بلژیک در مسابقات حذفی جام جهانی، با روملو لوکاكو هم‌رتبه شد.
🇧🇪
🇧🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/99458" target="_blank">📅 23:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99456">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
پایان نیمه اول؛ اسپانیا 1 بلژیک 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/99456" target="_blank">📅 23:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99455">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🔥
گل‌تساوی بلژیک توسط دکتلاره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/99455" target="_blank">📅 23:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99454">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گل تاییده و موردی نداره</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/99454" target="_blank">📅 23:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99453">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">چه ضربه سر خوشگلیییی</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/99453" target="_blank">📅 23:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99452">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">مساووییییی بلژییییک</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/99452" target="_blank">📅 23:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99451">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">گللللللللللللل</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/99451" target="_blank">📅 23:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99450">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xnmr-113yTydgYHUggrDwaKzGU7Ol6puxZFWpeu8mWIG6mJowo6_Aq2_ZnPhUqV9NwbFgBL__Nu0uCS99q8KCTp21bEC5igSpGRAjVvcrtJSv3urYtMegsYDTm-nVGC9h3zcspY06ZaZgF3x7ODHPVBgwfbMRsGay7pP0-weFfb5M2H0z6PdWtTy5WEHPxPRX9CnCnffmXBMDaeBP37KiegZ1J88Vk6ei_zsaQMHKZwgQfL3bE9xj8yfVU-L8QqsfWZR5iw8GYDDUxp1-jaxV4QImUj-Q2Z4bRwN8tjg1Ma1Z3qOseLWkLLAsSPhnkvVmVZ7Zm0IhUUYNC2mJvxlxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور برد پیت تو ورزشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/99450" target="_blank">📅 23:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99449">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خوشگل سیو‌ کرد کورتوا</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/99449" target="_blank">📅 23:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99448">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">چه خووووب زد</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/99448" target="_blank">📅 23:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99447">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/99447" target="_blank">📅 23:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99446">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">چه بازی ای میکنه یامااااال</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/99446" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99445">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یامال دفاع چپ بلژیکو کرده قشنگ</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/99445" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99444">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">خطاااااای خوش جا برای اسپانیا</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/99444" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99443">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🔥
گل‌اول اسپانیا به بلژیک توسط فابیان رویز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/99443" target="_blank">📅 23:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99442">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اسپانیاااااا فرانسسسسه داریم نیمه نهاییییییییییی</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/99442" target="_blank">📅 23:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99441">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ببببببه بببببببههههههه</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/99441" target="_blank">📅 23:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99440">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">بالاخرهههههه شددددددد</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/99440" target="_blank">📅 23:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99439">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">فابیاننننننن رویزززژزززز</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/99439" target="_blank">📅 23:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99438">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اسپانیاااااا</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/99438" target="_blank">📅 23:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99437">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گللللللللللللل</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/99437" target="_blank">📅 23:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99436">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گلگگلگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/99436" target="_blank">📅 23:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99435">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bU3yj9GBzN1CZWbABwPMc7tZBXPLvFUqUj8xNZALNcHQjCp4Hyu__ioQLQiRayGA_x5XTzHPsLlshUOJq9rP50tuuZtfMcEDJKeR4qhdwqde8DT_g03XnLHi6w-KJZ2wnDNGD5R98YdOLCLD2fiGM3muMdWZkOu5YtMJ6CwOUYOFwG3fuUR5tJPhKtVVDJF3chpldg7ck1BLYfAw3kMg3ikQ2QKwo9Mkrbqdjms1ZxAfmq92tMI3Tz8g6mmUTdvp2d_bB02b0EejKw0jh2OJxNfpJse3B-FHYcLiMT1r13jDWsXppCGxxISZwTsGOpb-KFEWxLQo03wHOsVVFcs5BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
❌
#فوووووری
از آرشیو وار: پنالتی اسپانیا مقابل بلژیک گرفته نشدددددد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/99435" target="_blank">📅 22:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99434">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRcURbuozdQt6Xiomc0Cf6kXYv9CZBzogd2290lfLWtW0Qv6dEpTRPxF64p6bVCQ3iA6voiig1Wre0hzUm3au4-0LKfbijUL9Ez6eLYt2c9KA-FoAmU-hufXMosLaC5ww8GjBqicbY9NH4ZsentvJWVz9yMKIcv1_Dem2HIzAhqbCAcxkVTWQSV9380Ax29pOHTX5ZRMH9HEa8SSbeq6T_Qwyh3UKvL5fdf8UzHv3Pmd371X_gA7k_95ihUEgLXMhya0xR7hBe9peATByjk1c0UREd929mw8sctLqQFR64sp22kh0i7C3hy1LaVVpRToBHlwqD5k6IfDAwS9JjJWGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
پست جدید رونالدو: یه پیروزی میلیون ها میارزه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/99434" target="_blank">📅 22:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99433">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CD9gO9FgsfbTW2DH8xEWL7xEg5IEBm1_24sqFz0m_YKZElAA7FqlF5rUNe6hG7SWVdmsKMkEzXfWjHWxkU54bNUk0ZJdGqjzPyr3C7KYOEpq_D7MnP29w_lmLIa-6-U1xlD5eJPwlqSKHjPGf461LaSvuRG4H4KnYLA1UM-1cYtqVghAnTvu8pbv2-5FOQ3lA65T3Y6oE20d6iCSke4h6jDAXrRr3fRgkzpDq6aFGy4SysFKWjXkk1lNDSObUxNyJU2SEIdtYdr2SdHEy_qCVdhDHSAJoxlPg2hIT37a5fdgjmg9FIndEIPY1eERy-lNJ-rwg68NBl76WUFdsOiAKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوست دختر یامال تو ورزشگاهه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/99433" target="_blank">📅 22:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99432">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">⚽
تحلیل دقیق مسابقات فوتبال اگر به آمار، آنالیز و بررسی تخصصی بازی‌ها علاقه‌مندی، این کانال برای توست.
📊
تحلیل قبل از مسابقه
📈
بررسی آمار و عملکرد تیم‌ها
🎯
نکات و دیدگاه‌های تخصصی همراه ما باش و مسابقات را حرفه‌ای‌تر دنبال کن.  @bet_maxxx @bet_maxxx @bet_maxxx</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/99432" target="_blank">📅 22:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99431">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqyZ0KQ4q6G7l5WaLvJunkYl7vBiMMMokeJ-7NpH9yjdbl4az1FopHWtZ4SoAZDoKPzHssU2wTJUcM0b4EY4IL0OCiiwRvBiBiY9vf5CtjWZzGGzmuRdKm-xqVP4fuSQe-Rw3xtYNif4M5Boy9HwJYFzA9b0vqxXYmcVLrvG4aITy8RWkTkFB1BBDpBUnaXI8boXp8E4W9S3MZIuaGypcdkCYZV5mxD4WIMQnrE_mVTT85-vTkquiS54muzX7lSSZn1i8jrM4RlQMBfKv8BdrLf3SaDpS8SxwH8LPhr4D5hX8eM6qykQFFfr_yglKwNsgA8WRLcOiYWokRy8yQf3Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
تحلیل دقیق مسابقات فوتبال
اگر به آمار، آنالیز و بررسی تخصصی بازی‌ها علاقه‌مندی، این کانال برای توست.
📊
تحلیل قبل از مسابقه
📈
بررسی آمار و عملکرد تیم‌ها
🎯
نکات و دیدگاه‌های تخصصی
همراه ما باش و مسابقات را حرفه‌ای‌تر دنبال کن.
@bet_maxxx
@bet_maxxx
@bet_maxxx</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/99431" target="_blank">📅 22:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99430">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">بریییم سراغ بازی جذاب اسپانیا و بلژیک
🔥</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/99430" target="_blank">📅 22:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99429">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇧🇪
ترکیب بلژیک مقابل اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/99429" target="_blank">📅 22:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99428">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQP1Tiab6NdU7bqmzChxgSoMS9jJVS7WdJ4Gvr9O6Mwzg1jARFMDQHAoRBIqNJ5aDlJkSgrCHG5cx9EvK3BgI37eS73trS0W_GStCavGoWYmZCKQOKEuKroLlkSosWDiq474ea73F-rZuPovRDCZgNtyd0uNYGIkbQ820QJ_OR18YUo03UTTWkdGBfZzmfuAm5c37cH0vDcjyLQlD-Ygd7TzAqBprQELsq_AChDFgR5ZLd6zbqmIYjYKJJ498cb9OiIAxauzI34_BZza9EN3Hv10Ckv1m-KZ-RmnY-d2_8J3PVgbJKWdBNP-fdKNDh4G7ArUt1TTz34Ekx-e9Q7inw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
📰
فابریزیو رومانو: انتقال ادرسون ستاره برزیلی آتالانتا به منچستریونایتد منتفی شد. این بازیکن به این تیم نخواهد پیوست.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دلیل لغو قرارداد، بروز نگرانی‌های پزشکی پس از انجام بخش اول معاینات پزشکی بود. (این نگرانی‌ها به ویژه مربوط به آسیب قبلی زانو، به خصوص آسیب غضروف مفصلی که در فصل گذشته (2025/26) رخ داده بود، و همچنین تردیدها در مورد سرعت بهبودی او بود).
تیم منچستریونایتد از نتایج معاینات راضی نبود و تصمیم گرفت این قرارداد را تکمیل نکند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/99428" target="_blank">📅 22:12 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
