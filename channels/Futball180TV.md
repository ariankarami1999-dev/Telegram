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
<img src="https://cdn5.telesco.pe/file/LJ5LzHDk-F89vV2ZrM8FrPBTz9I-WH3D28j78MFidbk1xrygZzcTtVO34i5TUqPWhaQY7s1joMUN2X3VEcwzp-aRCMLjhN9r20xsDX-Ilxe7XmxWUSmcXV5XMZXnus4AIBT_nswhmW9ZjijtXULLMzLXVL5sC4RzRGDxVI-aAkqPX8N8x9S3mxF-TuCVTPanZOuBOzQaX4EvFoRI3kHUl0U1iYmBRs0Czo74N2bTAGXsLUqS0q0FcSz_8TmzXQ-WMFqWt1dXEAKD_8Rc7yoOdaVLmvkHSIDrEyrDLs9RehCKnn7VkD1pLI6zMHRkajb83GF6_SeT1GhtnWvHssI9eQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 559K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 00:22:32</div>
<hr>

<div class="tg-post" id="msg-100823">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/184bb0f8b6.mp4?token=gSF2OK2w9krD0zxz1bgkKEn4e6evWY0vqQh3ozh58h88-uPlOEAwOxEis5TVuXlhT5LkCuiGS9d7QZBUaS_MGGQvipJijugrCtaoZHufHwK8SDpiX8t3WPRc7IbYiq4zC8dn0zZFtxYade4Mw0Quls9uYDnaI5GLTSXxrEoK1VYlOqMdiN_ialgB3PjKpCTTasMDZsftYzH2G5mQCfBQ98TM29hvd4y1GrCUkMXOdxdXB0eGz6wxR_mwpR4bY-e0fZwclGbx3ydkah2NbM5gww0MxUpK9uLMzQXzEje52yrTryQ-Z02t3tcmvCIoPPT8fvvduJgjrfrwbTbmbCh6VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/184bb0f8b6.mp4?token=gSF2OK2w9krD0zxz1bgkKEn4e6evWY0vqQh3ozh58h88-uPlOEAwOxEis5TVuXlhT5LkCuiGS9d7QZBUaS_MGGQvipJijugrCtaoZHufHwK8SDpiX8t3WPRc7IbYiq4zC8dn0zZFtxYade4Mw0Quls9uYDnaI5GLTSXxrEoK1VYlOqMdiN_ialgB3PjKpCTTasMDZsftYzH2G5mQCfBQ98TM29hvd4y1GrCUkMXOdxdXB0eGz6wxR_mwpR4bY-e0fZwclGbx3ydkah2NbM5gww0MxUpK9uLMzQXzEje52yrTryQ-Z02t3tcmvCIoPPT8fvvduJgjrfrwbTbmbCh6VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
صحبت‌های جواد کاظمیان از شکست در مسیر عاشقی مونیکا بلوچی
😆
😔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/Futball180TV/100823" target="_blank">📅 00:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100822">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbVg8yP7EGiSWcSwBcb8xzNPiObxFDDmtzjfqcWgDQJLjrhRbSd-0131CitpABdp0Eao-Hac5kPUOTrK6urOLlVRhO9L5HbaYyzFjXZtQS5ZTYzYHTolbay78Qdxnoj7-dGlzU662osiRGoxhI6D1ZzFPPFkYInkPBYnxM8AGlPx-tMI080t2VdufBnt8psfFig3IKKQBC5wjwbawSDwapzr5ZESmeukWK2eRIAvRMGv6_H1Ksp6_y61NoxNxX27gp4fqTpwCUCFf3xRWo0JTWASIbpKm2mwbve1OQjfVpCUuZ35l1C1vYTAXUDIme_WtQwGWt_zyLaEMJ9crQsmQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنر این کوچولو تو ورزشگاه: جود تو منبع الهام من هستی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/Futball180TV/100822" target="_blank">📅 00:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100821">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4e58d0897.mp4?token=k7LG-EKbCCWPHjd3aBuAHcVJzqoOLl3kn7rx2Nf-GJ_-eUwyyh_ipQcHwDKr_zwvZy3pO_Gt6qCJVWLjfWvvYG-IkeDzSeodKpJVoa-Fmr1Bkm6UTm1HXnkUkUXwfMSowV9vnFtoeMzSIHkXi4y1pqKvWyLTykaPwXDu9oYvI8MYwGQOCfmdH5vJ7EeRXna0RzG6SsLv4az3ATvSjlv1l6NgHV_Py5y-06forBx1qgo2eEdNBZjUpu43PnEflz6yR_e_6d2eX0OvUhI2p96mXH4RBLnsx5VzuNLGYJf7rYzjBffQrLj2rjZ70x9w0cGQkptWLaV1KN5i0fYUf3rAIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4e58d0897.mp4?token=k7LG-EKbCCWPHjd3aBuAHcVJzqoOLl3kn7rx2Nf-GJ_-eUwyyh_ipQcHwDKr_zwvZy3pO_Gt6qCJVWLjfWvvYG-IkeDzSeodKpJVoa-Fmr1Bkm6UTm1HXnkUkUXwfMSowV9vnFtoeMzSIHkXi4y1pqKvWyLTykaPwXDu9oYvI8MYwGQOCfmdH5vJ7EeRXna0RzG6SsLv4az3ATvSjlv1l6NgHV_Py5y-06forBx1qgo2eEdNBZjUpu43PnEflz6yR_e_6d2eX0OvUhI2p96mXH4RBLnsx5VzuNLGYJf7rYzjBffQrLj2rjZ70x9w0cGQkptWLaV1KN5i0fYUf3rAIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
👾
▶️
✨
گوگل با هوش مصنوعی یکی از گل‌های خاطره‌انگیز پله را بازسازی کرد
🔺
هوش مصنوعی گوگل موفق شده تا یکی از خاطره‌انگیزترین گل‌های پله، اسطوره فوتبال برزیل که هیچ ویدیویی از آن وجود نداشت را فقط با توصیف افرادی که آن را دیده بودند بازسازی کند.
🔺
گل معروف «Gol da Rua Javari» تنها توسط هزاران هوادار حاضر در ورزشگاه و بازیکنان داخل زمین دیده شد؛ افرادی که امروز تنها تعداد اندکی از آن‌ها هنوز در قید حیات هستند. تنها یادگار ثبت‌شده از آن لحظه، یک عکس قدیمی از ضربه سر نهایی پله بود.
🔺
تیم گوگل با افرادی که بیش از شش دهه پیش این گل را از نزدیک دیده بودند گفت‌وگو کرد و با کنار هم قرار دادن روایت‌های آنها حرکات پله را بازسازی کرد. سپس با استفاده از عکس‌های ورزشگاه، تماشاگران و دیگر بازیکنان حاضر در زمین، تصویری از نحوه رخ دادن این صحنه شکل داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/Futball180TV/100821" target="_blank">📅 00:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100820">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXIdWDPf3aLoB9Pm9e8bI--id26bME89XevG9U6lcM088YCwP3UjWLYYR0d-MMPb24jp5M9NM_coirYrVTDNx1n6_JEroTH6gXP1JVfawIXZwAOCNoTVHRjifk-AZblXJTLq4Yc6Nts4FcB6jO4QXTvDehQf4jViOHH4BqfGcgAb0ZCvasgInnPeUa5aolXQj-bv_w9jsRAhBprjMEDquUGiOptOPtio3jZsVlCoppT1RSbGW9SeQk_e0NDtOox75hN9Qg4RZMPPlCRQCoAjse_9xpUvp4impfNHVdLgzLhpRcxlzL7rtTOvGYYlXAWg-C6HZ8ARGylGZT8r_xe3wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توئیت بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/Futball180TV/100820" target="_blank">📅 00:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100819">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzoglN98xH6HPyvDos2ZqnrR6JkPRXWMQBlC-MOPHLs3IE3C02Esk3UkPOBVf8fDo98rBkvHCMh1oNT1QQbVlswHXGcFyZzheREoe7ym4IRsE7HBAUD_6OVV5VDCym_MtNA7UMe-5c50ZW4HZCjp0SJJlQC1ifTVhIjsg7L8hw9yk_AySxCDizISVbjCVfGVVr-zs0xpvzDvh3piMcUes-jfnAROCIEdK09OYXBcV1x1CKMhdcgbSNT2ltk53jfJNne-FyoPIVdVZ4pET4oMdnDO4x45ww3DmIVVcQqSv_B_XcS8IeG0trLTQIsKCwjeS4RtdB5OTFSJCwecnmkChA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
۱۱۶ میلیون پوند وجه رایج انگلیس در تصویر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/Futball180TV/100819" target="_blank">📅 00:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100818">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
25% پیشبینی رایگان برای واریزی‌های یوتوپیا
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/Futball180TV/100818" target="_blank">📅 00:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100817">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=HzCCq_PWqxhw4_cD26xdp_g18s15Mdjl0zbfMaaFtCJApnlNo3BCOZK1mOGNYkFILKFL_HAjHuqPJeuiWFBMEHRNhdSrUT7c4xnqHLI6V-7i9uRRIXjQNKvpjM35HM4ljGqe8W4lINOv_8bGNLHTMZUBwC-bJkk0v2hcuOs6mq9Qz66Xi8yBWh1XtrtIGgmbFfn2p9Vz3OnXONYBhaOT3ru7_sDYNFNa8YxFmr_tDrsIYYafnJx3avXz0tyyAbs1-XaDRuVpGG_yOEpew2TMuVmRFN6U9VDoDp66mTSOuJKwJbacDVvUPSkoLqeoseHWeawqkq_G8iUqkbJBLfIZWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=HzCCq_PWqxhw4_cD26xdp_g18s15Mdjl0zbfMaaFtCJApnlNo3BCOZK1mOGNYkFILKFL_HAjHuqPJeuiWFBMEHRNhdSrUT7c4xnqHLI6V-7i9uRRIXjQNKvpjM35HM4ljGqe8W4lINOv_8bGNLHTMZUBwC-bJkk0v2hcuOs6mq9Qz66Xi8yBWh1XtrtIGgmbFfn2p9Vz3OnXONYBhaOT3ru7_sDYNFNa8YxFmr_tDrsIYYafnJx3avXz0tyyAbs1-XaDRuVpGG_yOEpew2TMuVmRFN6U9VDoDp66mTSOuJKwJbacDVvUPSkoLqeoseHWeawqkq_G8iUqkbJBLfIZWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌ جهانی 2026
⚽️
فرانسه
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
⏰
شروع بازی ساعت 00:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.000.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/Futball180TV/100817" target="_blank">📅 00:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100816">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UobFyGO8Jvhu2ZexhwYcbMi_ou05KKDGk5yB6ewDc6C29POjki3H0jcJWgHKF47ftehlxLTVhpqnAZT0vOyk08CDKF_iPnFr7k_RkiEcB0vse-Y6gm8y4l7LVLaRuLG54aQwqErYaM7pkb4jEGXWw1ZRvSsn32jZOjiV6sxvdFEwPhkHUw26GTIyyDRwdIWKyY0-rxBT3qyOjEPKV_wR3F-tkO-PsGLEECRscR9WrYjlNJJ7sLx89NKmjnKVHCNhdlNjXhOfm2hNbYZaX2NGNfvSRwavcFZsLGZAn9LQco_gg05SmH5zyKA3P1tlnJifiP4MtrGXLSEA7rUYpHyQLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
فرانسه برای چهارمین بار در تاریخ، راهی دیدار رده‌بندی جام جهانی فوتبال شده است. خروس‌ها در سه‌بار حضور در رده‌بندی دو برد و یک شکست داشته‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/Futball180TV/100816" target="_blank">📅 23:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100815">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k79ABzd36itfeecMk9mToJoBs7tcZzQ8_H7yqG3OmH7Zp6uVnAzqYZEx-iCNkTazTeOYIb12LueyuNGh55NpCwU5oToc5mxfrHHv4tDo6vfm6o8VyWDijQgwm82UykxvnMGo-Xa-_9dOzPqf12mk9VmRwPgQJF-FzSTyLjKb4XojAzW2qhN204rxoPqccT8fA9Ha7T6pfhuUi32nbCd4rc9i5TCELQv-RtrUkfaRc2LuiS3WDYavIxSfdi22aJ26kX6EoYDT_rZIpwGLhJPHOwz-P7IVo26OQ9Gld5GT0YTBVUm9oQkP07aXGMGMBzgTxMdbC5QYhD5Uj8rYJo0-HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دیگه بعد از دست دادن جام اون دیکتاتورِ سابق نمیشه:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/Futball180TV/100815" target="_blank">📅 23:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100813">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/roaE8lpsrELKTUhoa1FypfyxRGpCofzjw_BE4TwHWVbNPZclYBDiHFNUbXx8odsRO3EzC2Bb2Hf4-_P91c1aAnWNrKs3GKWl1b4lPXipvaDiLhWq759udgj4hb8Phrgy8cqjQU6YwsN5tGAZrNzNnCJvuygOEBAKjRjvvM839NqckqcKw1tbi4HSkC3O3x4uhjYIvRvvX4D6h5XWAG9XaSeemzZ0pJWQUrofpvR4DZlbQ-rU7bH7N6Ji7J3T6upiD6wgXZvl1f1LcPNa7siNNYILdFC06xCZo4Ozhxkbh3pMAnONweR2mZA8Aijbs2KidD8S0ScZh_3vApE_K1HEBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tNid6e0mYDj5jmWFyr_yItFcrqFW77Qbo8kk5fW2EY6A6xAVESw-1xbgnCtq5YEj52iiMxCV0L96SbQYyG5viFhIqr3gUUbnaK_NzZnP8koa_xnV6kAjwHorBJewEQ4pyermPUDx4H_ufPhmsoHXZBRnO98_LGWnu3N-P7MCN7l5xK6oVhq2OYtxxIXX43LfTKbKaBn8056VJgZSZxr2IBVtaU_cYl7eQdm8jTVWH6cwYbL66o6OTSxDUOi5PEDWQIb67BbyKC3Ub0e2NqnuccNLl6NxZOv6PI0iDpK5UERzHcgcVjEPZ4qfBtkT3B_nzHpbDxL8Im55RacRuaA4ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این دیگه بعد از دست دادن جام اون دیکتاتورِ سابق نمیشه:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/100813" target="_blank">📅 23:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100812">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EolsdjLoi2OVeX_SwjWMMxh0uBQ0lq-_AlrUhzm6xI2XI6mg_QXuKO-UfI7hy_U4oHzDTUMr2IFqOUoq0CL3jENczUZ2Qi8UHxbcJWl9e_4Cp62fzU9RoL8jJOsOtKwlo1m65q6LsqrhKg2smwlkBxFseXzwFCGBQCVq_hyHsX1kJbWUX7gxYId88gZY5JlK321jPsSlGphL88Aswvs9t5U4hQawNQwgqZ5ZU5gC4fbtBGCN14nGYYxx7QHoic1du4oTrxOlF9C4P4LWhutZSUh5grsj6nebqZiwF6BtS-8cmHwCPKsrxnkF-L4O8FX7xyxJBj8GRAp259tOfTspzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
آخرین دیدار به عنوان مربی خروس‌ها.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/100812" target="_blank">📅 23:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100811">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ایوان تونی برای انگلیس و رایان شرکی برای فرانسه، برای اولین بار در جام جهانی، در ترکیب اصلی تیم‌هایشان قرار گرفتند!
✅
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/100811" target="_blank">📅 23:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100809">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RwkcpZ5NQ9OvQHpCBEkUniskbFK2grx0Y283swyBjyzMtamE-7nIxI_uncb7WnBMCGEJJ11JCjaeuDWx5Esrkmqtx7OcIWFgg3G5ZeP7cwKjTU05uxT8yyvwYOBH1zx54_W_S2CDp0aU2bUy54kuxUtkrQjUnwS1-HVsnKbUxDkcLDq8sQbgx5zLAohCPetjgsJ8OcIwXHcofdZNBT8fjEf4Jr_4R8k36EdKgyYdnV_z4aTG49AyaXoR3BPj_cLSnKe_F4pGXCTeuKqVXZahYZ6mf2J9gTkXGLUDUWX-F5a5Me3UYTOLly_cG3qrlYXiO-h3toN3sKHnyN-t1eQAag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h7uuqOrRts2zEVRAK-xQdlxE5R5dif61kqTLXMrode_q342n6tlE5FDz50v6UCU7bTdI9S1Z_1Q9cqp9yRtYlRoAnE0TJxTfR7SgPmo2vyFTixRBgXIVE2bOHshiuEOHTxLM2KOY-XJGtj5cBS5JHmlafa83-7quXb_uVvYdy-tBiKGgil_VuLXwo_rMz-rKnawpFzN-tM2gJuCLtzQDxwa-SFepoiBKh-ywfAn7H9nR25E5Uq49DEEZI1nzk2XijfIxEOg82vwk4cvwpYGd2EnvmTeUlA9O8lUiWFPRRGI5z-OM8rJQpz_wZXhZiDuQtQoaco4hCbmH5f0_rYv2qQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
ترکیب رسمی انگلیس و فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/100809" target="_blank">📅 23:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100806">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/746e78f138.mp4?token=K5m_8wN-d6pXUIf9uHgtS9JRyb18DWeNgOEx9bhOt8P645o4IRvGPCHWHtowGiuMztuDMXDTwDKhLrSUM_RAfi2XIMsO2BN7fc85iluGN-gqLsE7GMOauMZvJa_oFJ9b7YAnMZGsqGB7YkEas2rZDNUs0tIfTRdr1T77oNSgMesx6mWCPmEJozVJChJqxdcpGiqZI5hp3Jj8EhXnGvdA49FBzhOukv5SvwjnRtAC5MEuTo6tNTTa1H-n0jkWU4edLTLYO07t0LXnJxfWUbgLWoFWnfDdAh1ieYCnaRI6TIMWDwx3VI40MO7opGCwgH6PKaswYW5G3XNHy9RgQXaWFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/746e78f138.mp4?token=K5m_8wN-d6pXUIf9uHgtS9JRyb18DWeNgOEx9bhOt8P645o4IRvGPCHWHtowGiuMztuDMXDTwDKhLrSUM_RAfi2XIMsO2BN7fc85iluGN-gqLsE7GMOauMZvJa_oFJ9b7YAnMZGsqGB7YkEas2rZDNUs0tIfTRdr1T77oNSgMesx6mWCPmEJozVJChJqxdcpGiqZI5hp3Jj8EhXnGvdA49FBzhOukv5SvwjnRtAC5MEuTo6tNTTa1H-n0jkWU4edLTLYO07t0LXnJxfWUbgLWoFWnfDdAh1ieYCnaRI6TIMWDwx3VI40MO7opGCwgH6PKaswYW5G3XNHy9RgQXaWFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
وضعیت جوی نیویورک قبل از بازی فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/100806" target="_blank">📅 22:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100805">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbtKgCRuEkgp-aZSHtBRvGMQHuNie8qM-D71icEwSf9jkPC5n0Av_YPfBNYfReGPprDwPivNbcK3b_SkxMiSis-BUmzmN9WeuUUoxQqydlQ6mZExTaOYjD849QGqg_au4xFoJOVRKR4TAk25nzCBa7HCfLtSIMyzlYbxDloq5nZk6sYpd0dPGCCWhglSFZuvZn0Ft5EPnqZSs8qea8rUaAtSAFe8F6W9rQAId2L4hy_EaTC-WaLa26KfUmsl9bJaP2ciIVtwt_OtAifHKxXHDQLbuNYq9-KI0w4lwWDzz_8A8LwTODZ71iNGODAavOoxHkPc-8bRUh097PYdTLLqew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🤩
#فوووووری فابریزیو رومانو: آلن هالیلوویچ استعداد برباد رفته بارسلونا در آستانه امضای قرارداد با پرسپولیس قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/100805" target="_blank">📅 22:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100803">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gfoxV68U3PrnvtwclzJpex2eGpYyiSTlxSvzt3vWHevUL7RMZGHaM25wxgFpeEEIqFmcPTUsyzPw8EUkqrYpviZ26-I2iXjyX0iZ0Mub__VqmZ23vrS9aO3iT_AJQyhVjv7NhQ27FjW4wspLgd8tbW4nRfOgIALivqE9ngYW8vElhacj4jpJCZ9tCz9iAdp0oveCCjcZJ_XrDgunrfVQG6H8h1pWRd_6lYw3X9D6QsRB7PK9MEPKo8GfXVmdOFhwxuXEUEzY98GxlcorihtC2oUrtLEKhBrVyJD2awN9_bgOSRCpL0TJ1iPs9sA4ww4WYg5pp8OoODsmcWYJXggNLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BTWO4rsA63LXXNyO4IQ_LtHfyCaBcA3mRRhYS1zM0b0blvE_3uvck1a2vSU4kZYXfoftUGNXWASTat-GO0-V8Ak7d4p2QvOB1N3MJlUnYgQ_Rql9fNBR8c2bzAWpDbTh2xgKN7tNGSGZghkwu28ok2eO7EBB_phEW1t_py1zZ1pD_QPhsTuJqINLZ2mcH-XJsDBZKqoVAWUAULQippNG_AyUYqox4XT291xBDPoebZG_8VAy7ohp9STz_qe4BH2Ro8yhHT7hSAtCFuF-6eIH8Gmrp4Hkp6JZ_9Y5PYBJuNHfIrJxch3cOWPJTZG-frlJkPd4JpBhDP8Fl1sdnMY6QA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
کون آگوئرو:
لیونل مسی شبیه پورن استاراست! چون اون ترتیب همه رو میده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/100803" target="_blank">📅 22:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100802">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3ZnGQ6GDHWHIoM0u-XYEpLu9332xu9J3-VNprAhICZJYhkPDkcSoBV_AOAefDL6sgJTHiTvaZjio4ZJ8XTiah8WKXIVYgj0Ethc7GHQN2j4sNGLBrgxLvN1RmKYYDelofItyR06mjce2HhPBqVw38BxNyKHoAV3mdiBh-43xCL9SJkmE1RibBmhVejNCKAd4xH24iufI0-XZ-HTq1wTa6GZGMGfT64e6x1M4J0LLgUSX4pdRIuH0nhXGhbcJyVb3-vClyZpwQ7oW02JL1gM8wsZH1S49er3qAMIlWRdbvBnVo5IpiyNziNzfoyayt90yM_DHlMHBkZslJqFNWPu8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🅰️
🏆
تنها ۲۴ ساعت تا فینال جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/100802" target="_blank">📅 22:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100801">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kieOotFyNVbPqC2sBRSR4aDzkyvHy_uYrRlpszEtit3ssCmT7cwn_8o71c3YBvYBpTS9CMbNDDn9z1gDzXcEgTmyhBIZKhIyKAvz6zIcdsfegkgNe1wDe_T4h_nJKyoKdwPAq1PzIyQzkPpPZdKNVzVZFti5UHry1bjvdbhnSfU1NCLFg3wjxJ1WDCDQrCbXRVrI3CYTz9dgp_Vek79-aiarDz9e3GQhY_v5SiUMFcW6WJ1wRO7ywWgnuxbLbRLRVG-0lmBQ1zED20aC8j2Sb3Pfm30OGOWyr3bEkCHZA5u-zDb17sbjv6w71R6QHsrzWN8RvG6mJweOV-5IrgE0ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🤩
#فوووووری
فابریزیو رومانو: آلن هالیلوویچ استعداد برباد رفته بارسلونا در آستانه امضای قرارداد با پرسپولیس قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/100801" target="_blank">📅 22:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100800">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
فابریزیو رومانو :
🇪🇸
اتلتیکو می‌گوید که به‌طورکلی نمی‌خواهد خولیان آلوارز را بفروشد، اما در صورت قطع رابطه بین آنها، که در مقطعی تصمیم به فروش او در ماه آگست بگیرند، آرسنال هنوز هم می‌تواند به او علاقه‌مند باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/100800" target="_blank">📅 22:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100799">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🏆
بهترین عملکرد تهاجمی در جام جهانی 2026:  ‏
🇫🇷
کیلیان امباپه — 8.93  ‏
🪄
خلاق‌ترین بازیکن در جام جهانی 2026:  ‏
🇦🇷
لیونل مسی — 8.41  ‏
🛡️
بهترین عملکرد دفاعی در جام جهانی 2026:  ‏
🇪🇸
رودری — 8.03  ‏[کنفرانس فدراسیون جهانی فوتبال (فیفا) در زمینه مطالعات فنی]
⚽️
…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/100799" target="_blank">📅 22:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100798">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-8gUoiRrMGYtZ90j0NxP6KriUnLKxmDYZ_iAo6NcGMwf4QfnGEv5eXurdcjTLEHkO1erZAgF6-NU-OFFoYFEjlJLLBuMj08izJNbdpeHHNVrru3yK4oON1sErdxmZV7nHfjJA3PXnw9xpIoSwenQ7MuuVL6sK83tRIfRgO3xvWa3ZqPaMVi54_qTj_rEuuVuW5lAvuF_QyryCoxY5Ay83yqShYju_eiZTKyYQfb8W61Noy__7C3-TqSkwPYHgwtR5gtX1aghsOPOynBhNT-3x34aCxTh3EZFFcILypBm2S0zSI_veNcmBms4ihIJo5ufyQoiTY7QUPJ78FmOFCt-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
بهترین عملکرد تهاجمی در جام جهانی 2026:
‏
🇫🇷
کیلیان امباپه — 8.93
‏
🪄
خلاق‌ترین بازیکن در جام جهانی 2026:
‏
🇦🇷
لیونل مسی — 8.41
‏
🛡️
بهترین عملکرد دفاعی در جام جهانی 2026:
‏
🇪🇸
رودری — 8.03
‏[کنفرانس فدراسیون جهانی فوتبال (فیفا) در زمینه مطالعات فنی]
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/100798" target="_blank">📅 22:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100797">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzPUj5ZdwxvK2s8r7IDpCTZWNtBOHWxNGs1DfWLhldBg8oL3p5tzoZTTqtNIPyoAoZkhtQPGQzB6RJxmGrY87gzORrxAoRWXS6bJjovGrW6LD7mMFrwpCR5nGv3V2B6FM3AAgba6UxEBqqlOcTksM2Gp5LhooMHIfSFsPRUTztni3dUd7-w_inhHo_aXug6fPzryAYEBy6BHnRw-InhgLmgw_32qWjgDgBCGJCGEp2Q753QkDIePZGpUBh0VTtsAXVjnu8pXgrXsosgVGsE2mFymJzD2Q0sRTlwgXliCS7wX481P9mTWKDffZGmA8VA-zvbKChUidgQGSgQjO6k53w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندین کشور تمایل دارند میزبان دوره بعدی سوپرجام اسپانیا باشند:
🇪🇬
‏
مصر
🇨🇳
‏ چین
🇺🇸
‏ ایالات متحده
🇲🇽
‏ مکزیک
‏تاکنون هیچ تصمیمی به طور قطعی اتخاذ نشده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/100797" target="_blank">📅 22:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100796">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPgbSo3BsLYlHxlmMQZ4zJ1q1gBPdVJsQ0X240bfk5SZlY3u9SdpyStdrqdNfeSJw9V0UhO6ZkXNS9BUAyNA4Pi0wOhDNbm2J_Gkp_d-zNvDFPZPPG21uCfuaclYqY5PKvYUiVl-jdMTtBoJuDUmQJreStxrRaPC68BAbdFuUg5nATY-GQmJY_9AnsHDDD83DbG5C1JKwtY6ALCj0Ewpo64aLouWV-0BTLmq6YaN3xlOemtqlomsq_UnnRplomPDlJMgyza4pVBBj8EQF1Uzlh9mP77HOG2Zz8OpqQHMU5gbvx-zXiyA8F6NqEGh5oxPjf7TeEs352TQb9oHiGQWHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خیابان‌های نیویورک، یک روز قبل از فینال جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/100796" target="_blank">📅 21:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100795">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVmk-vVW_LwemtQOI5bPTttiinBUvN84Ecx-TPFNPXvyzjpvK4ZvNrM0FwAzTF4gnIcYgumxZj1TLXkXu7yvUg49xsLZC0eaBJSENEfi3mUg2-pwl_SGtPxqoBVx4nx_S87GtGeNtUHrxr7R5U8hYITWniMpduWKbvosCDNYMSUApoyPiComemxa3sKWQhTEfdnZ5ec8A16Ksc8NZF85chX3pT-V2e4yW1E8HXUm-gSjiCvmtCJe39Cc1pJZ5UTmPTHnS_FuXuwnPA-kr8pJZKeD7NYa4IVl4vzipo6V04PrpYwxW8_X5RooDu0I0Qou2hZEvBKHcNmGjOCqQQZKSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
مورگان راجرز، چهارمین گران‌ترین انتقال تاریخ فوتبال شد:
• نیمار — 222 میلیون یورو
• کیلیان امباپه — 180 میلیون یورو
• الکساندر ایزاک — 150 میلیون یورو
• مورگان روجرز — 137 میلیون یورو
🆕
• الیوت اندرسون — 135 میلیون یورو
• فیلیپه کوتینیو — 135 میلیون یورو
• عثمان دمبله — 135 میلیون یورو
• جود بِلینگهام — 128 میلیون یورو
• انزو فرناندز — 121 میلیون یورو
• ادن هازارد — 120.8 میلیون یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/100795" target="_blank">📅 21:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100794">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDicZdjH952xuR88zRnCbEbDNIW7duCcF_-foa1fkTOC6RQRGi7IBYfqPQI9NCQxO4AoUoLQgKALU3YJx-RzjtKLFbM3286wJZgTMP0Jctxrv9U2LJJtoKf6TlcAsRurkF-o9qyS_ivBacRK5-Ebir95wXWy37mlqpIcUFKq6ilD26Ueh6wg3EM8qWhpdiLSFLydvJmQ6Cv29dSwxG_SMxcvBsie9KJDIjzERD5QhlmVAom-H30YD4_M-Z0U5L76FDQiYLEDwL5Hlk1J_b4jN88KDHM9JkJ6sQfv3Y-5qhGQggiDTp6S3tHnnX-Xhd8cDmUaAo_w85BXM7NbDG_CPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافینیا و بانو تو تعطیلات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/100794" target="_blank">📅 21:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100793">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمجله طلاسی | پلتفرم خرید و فروش آنلاین طلا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6aXVSiaPe_62B7sRhFPMFRUkYd8RppNBWg7sEC1DTR-g1g6108IA3FTK4t7pvkFeB079jwQGP0L4tGI5_5t8OzxYexsTOM8UCmfACFliLxw534r3NkNbLBy6oyBz8V0WVut2SwljjTGqSjeA5RNKy20h37xMxiUnVWvMLp2kFrBNlxPdtdV-TnI64ly1wyqUo372mn8xVpO_RYiG9Tp47G9yyGpDbnfJtWKAgo1KVjJMNAJzPMFzxj-CG9TVkN4QeeN6QeXZ86sE15pF3KJyKaXXUH8dtRhmF4GNehXGxesDrnI7FU3Y1iTwjndtPUYIVHYx4ImFoLfa8wopikLVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرژانتین یا اسپانیا؟
🏆
تنها با پیش‌بینی قهرمان جام جهانی، وارد قرعه‌کشی جایزه
۵۰ میلیون تومانی
طلاسی شوید.
از طریق لینک زیر پیش‌بینی خود را ثبت کنید.
👇
https://talasea.ir/sh/uoa</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/100793" target="_blank">📅 21:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100789">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CXWR_MJ9lufgfIslvcH0Y_Cd8ZckqmOPMKb75UO2S0r_66fAs-tFzySN8XcOukfGJxXd37SVg0F-sKgzMUo8esDdeyV0hWwLLLNH0C-79lcnfx45zE2QdKySg4b3uic5J3rPfxukfa8KSA6y7Wi2TakpR-MPvSA4hp6B5Gfyd_F9eNgpOWA7VzaS9MK4IJiSHFC117B-E8HwQcpAL8jjXeTEDUZPxMrPjelZ7Sz7wrZX9gWwQmGq0ZntOTPn61uuvMGPqY83AqQL1x0VDWsIfJalryKu1SF4XrI7ERUEA4eKMWSiWuo8V-rAM1TQaLw3rDG5bfkfK2B7ubnXqGqMng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U8Wj9FbwriEuqvAlmm4OOxjBiAgn1JGg8ZXYyVJYiAYhPHqinZoh_4Fdk8AXr5ndvgU5o-_xzixcq_4lQ-1Sn8TklCtp_KPaFuSoAfMbbpI0yNT9nhXMMeRyiuxm-rY1IF5EkjccRuIBsWccIamFhYsTGsfTamcUzM2_eW0YfBz06TxJxQy5hqiDBjchXMI9LwO7k-Y1DOpb70ayjdyOBhvlAyosHWasysyzAMqx_GH22d1bHK-piEQOBLVWaaNKvUQeEaxGtAn8ehdfYBmUKSmVkj3LjxeuAIS8PPwKRgSMaeZ-Wmx1G-rV-k7YuIk41-YCC_avTb061wsavfJdBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UKkBK9Y938Ird09Hv1Vl-TOJgZk0TMojfkPalIVA4wAKBuo42B5FL8yfFC8EBnv2jm5_dSl3KycJuXn-qQE3YsPuEBi2G-cuiy1rtTdLTMTH9r8YV6wLJ0ellVf8MkB9mwFTbNa8oKkeuolZb1gf4PWNScylK_AtYPwIwN5Jwxo4GBuwYh0dNDGy54FPd8YGqQzZxQeywZDZnzydBKUr6HtlPevp4P3F8FeiZCMuAkKtmFZPYRwi4imNnk3sYHigvM9XPZpLBm_flGS5M2ulMCTWLPR5LpNPMDfnodFUnKm0XfhuPapO_RBG8Tu4i-NfQVtzTHgiMaDuc9G8CdxKEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
اسطوره مسی شاد و خندان تو تمرینات آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/100789" target="_blank">📅 21:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100788">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0efe47006.mp4?token=qR8pvmTPX4RjrWe5Xg-iS91ih64dIsl4RmdyJIBnwh66a6Sn7GV3EhkBauNpG6fEB48OAtVh3AB-p8ThBnX1dzAfv21qm-0_ZT0gBQ3HffU9kteHpIDozuWDKR1Eel_xwy2d4qbnhXkTOwPjUtNmeuZSP4CKe17nGoqTXsmHqp7CibBrqYmhIpXq-xCs9FeULDh9mctOHK4eYBLiZC39iGvpHyAV6z3F__ocYdEQhBVbt6romPjWP2lY0iSLj3kRsXzDpt_U66QdpSqp9fTjK7d6MyO2OOgkzlywaT3mpWQpOMwMM09dYGlq69uRbEIYmcaywPY_FMg-9N9pqyg0ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0efe47006.mp4?token=qR8pvmTPX4RjrWe5Xg-iS91ih64dIsl4RmdyJIBnwh66a6Sn7GV3EhkBauNpG6fEB48OAtVh3AB-p8ThBnX1dzAfv21qm-0_ZT0gBQ3HffU9kteHpIDozuWDKR1Eel_xwy2d4qbnhXkTOwPjUtNmeuZSP4CKe17nGoqTXsmHqp7CibBrqYmhIpXq-xCs9FeULDh9mctOHK4eYBLiZC39iGvpHyAV6z3F__ocYdEQhBVbt6romPjWP2lY0iSLj3kRsXzDpt_U66QdpSqp9fTjK7d6MyO2OOgkzlywaT3mpWQpOMwMM09dYGlq69uRbEIYmcaywPY_FMg-9N9pqyg0ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درحالیکه بچه سوسولای بقیه کشورا تمریناشونو برا آب و هوا کنسل میکنن، بروبچ آرژانتین تو این هوام بیخیال تمرین کنار لئو مسی نمیشن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/100788" target="_blank">📅 21:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100787">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lk2RNeqiAYn0ByA-L5xvmCqrxC1YzEoVUOSdPibVbDvBXe3-QE2atkTLNnJnXVNkM9Vx4c9TOuVWGNWKA5RzHFDAD-bs8mkxZrDPDNNx8wNFjB7E3ujGuBE6BqhNM7mke1E-OOA6t5ceQwMU-bnIkUC197SAS77i9k7NgKVckfQzPTOPKhLdBCj3EOt1KOIcxFLukfNJ2rbL0kt_dGbLyJepcqlgV5m0XzgH26VariS60SG370n6EZAbws4Nkeg9rSz3Q4pQhtYeUJnKlZAVARCP_0VZBA4PV_cJDQX56FcWZ6wzfZ4mpG48rC6GZ--wmJmpUYN9Bc0UU-p_cwbDLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
۵۰۰ دلار جایزه + ۱ گیگ اینترنت برای هر برنده!
🎁
🇫🇷
فرانسه
🆚
🇬🇧
انگلیس
🔥
دیدار رده‌بندی جام جهانی ۲۰۲۶
🏆
نتیجه را درست پیش‌بینی کن؛
۵۰۰ دلار جایزه
بین تمام برندگان تقسیم می‌شود و
هر برنده ۱ گیگ اینترنت یک‌ماهه
نیز دریافت می‌کند.
⏳
فقط تا قبل از شروع مسابقه فرصت ثبت پیش‌بینی داری!
👇
همین حالا وارد بات شو و پیش‌بینی‌ات را ثبت کن:
https://t.me/betegram_bot?start=p9_r4EF37DCE
جایزه نقدی مطابق قوانین سایت به‌صورت
FreeBet
پرداخت می‌شود.</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/Futball180TV/100787" target="_blank">📅 21:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100786">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEtu7jvWwNOPajKsVy2tC40rAsWciKle3647taYHpACwWdqPJQE_SlnzUaBPR5IfBYGFGnxMFXh98kpUOfzlAzfk3pCA3Hg7KL3TajUrg1PBN28Em8Kw_ZIbBVXWDXtC4ysh1UhKgyDG0EcVrqkNYDq6IY-D1UaAXdFOiOYV_55eYp9pGd5074ex-a4FU-kJbL-t_q__CzPj54wn2ImwMlpc59qx5w4o7et3wUqNnq2A_sxuIK3Z2Oc4-frknV7SdVnCxY4L2rc0Vc-rHSc-jzA-LBET-xCGl0UTHzG9g_Zmv0rHrE4ErJhKMVVklnSupNRacE2aCF6L_e1bpWRJmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رومانو هم تایید کرد.
🇮🇹
✅
HERE WE GO
✅
✅
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/100786" target="_blank">📅 21:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100785">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FhbE6quFOQN-iB249fIJEpDR-HAHr3faFUwYKmhgdzoNKpDs7vRqu1xa7_LtFjRzQl218IG5UQ9Lh3p92dTvposLxvfcjrv17hyUcaS-1Yi2KiVeM2oGcG3U-Gl1sEXUKXTImbgw2HOebSV-rxYTJmh2yJzEHSMls6HeYxylNc2wDwaLsz3r-_u6dnjAIA1IwwMO84E_tcpAz7sopDwHLOsDXRjqKu3GBycbVxW-L5DKGQWpQn5UDhi1hkL0bfT2yo_U6CwcEaC6Ua9zz3AYU9862INw3T2NYLVLS6XrEk9-pUSLFavACyD5XIOjVT-UfWGi51hQwd5IGDQb4TrkWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🤯
#فوووووری از دیوید اورنشتین: چلسی برای جذب مورگان راجرز ستاره استون‌ویلا با رقم ۱۱۶ میلیون پوند به توافق نهایی رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/100785" target="_blank">📅 21:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100784">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdTPYys2wJJCvbZ4UQbX72OgtzQ0Da8MdPZEVVWTobFiVR_KIf3x1NKZITAOB6FD5Cc5_vcsclmhdB1bNXicfzv3NepkvIetylobZnN3YMcaJMAykOMcdQRYijCeOpbYz2M1e3Ky5hBonGmogkiYF7uv9jKDf72txPSSDYfA9LCO2g6uulqTxUBfwjEOEfP04EsXs_HuWuudrPeSVdKLkBAtgVQT-xBo7B3ncApSauNdc4PJKnO-Y0mECPzc5pRrB7Z9YOLeWiB9u_IzuzgiOJ772GnsaaR5qWVI63t-UTP1gWW8OEUoUfiZGp8SC28sHdh84j6IS0aSjULH8g134g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
انتخاب بهترین بازیکن جام‌جهانی توسط ژاوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/100784" target="_blank">📅 21:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100783">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🤯
#فوووووری از دیوید اورنشتین: چلسی برای جذب مورگان راجرز ستاره استون‌ویلا با رقم ۱۱۶ میلیون پوند به توافق نهایی رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/100783" target="_blank">📅 21:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100782">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-y-l5PQjtrgdrAtPuCr3qInM-B1S4mOG4XYhkhPb9MLjMtDLG20HcgHWHDju-8OF0Hy9XDYVKqp4J0KAjQVJyONr4vceZS5nD1sKLHQE_8MBQ31lIGWwjT27WjVD8VJXpEqznU2_tf4MkfJ5grLGggx3ExBal3iREj-vyHPHMM9AeqUc5-DsQEi4OxCMVxaR7W-o_D-4pGmMeOI9VJsbySGMImYfHrmfBEVOLULAi7pIF6WMzlIstO7API_xu50DK6xahXQtlQ_z-6-b5JmfdRu-7v8IbGvoflbyy2HLX3TV2FarpqRs764SKh1AAx3x_buVjyaN43kcz3XnqY5gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🤯
#فوووووری
از دیوید اورنشتین: چلسی برای جذب مورگان راجرز ستاره استون‌ویلا با رقم ۱۱۶ میلیون پوند به توافق نهایی رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/100782" target="_blank">📅 21:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100780">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTm261HGQAoawmWwNdB24aAQYLR9JIpMeTapJ6ZfOoGD_rsd6LK93crC6EZza7FK1coIPciAy9z8HN9IuhVNzM-VlwzdOW8FbEuWU-bTdSQoU9OH1X5NfWGYGhLtFrJrYBbHUwvopXH4fZFVMXZbmCe6Bfc0NZ52GkiYddHOUa8ma9z_gxiNmwjrWwpiDfVSMNdDJS8qO4vvl7jv6Yaofk8y8_HDfVvs3tC26-mQQxML23ZGL19Ny-MgGzKiHIeQR8_NFEinv58E9Cj4uBBnyb9zJgnp6bu-UNHoYyLsgyfZtrqcNF9nMSbbz4LEY-w0F2mw4t-hMItmuUnlDwL7dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔥
نوشته پشت کیت دوم میلان: «بعد از استانبول، همیشه آتن وجود داره!"
🔻
این شعار به دو فینال لیگ قهرمانان بین میلان و لیورپول اشاره داره که اولی رو در سال ۲۰۰۵ میلان در استانبول با نتیجه سه بر صفر جلو بود، اما در نهایت شکست خورد و تبدیل به تاریک ترین شب تاریخ میلان شد.
🔻
درست دو سال بعد، میلان در فینالی که در آتن برگزار میشد دوباره حریف لیورپول شد و این بار با نتیجه دو بر یک پیروز شد و انتقام گرفت. نماد زیبایی برای بازگشت از ناامیدی و شکست
🖤
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/100780" target="_blank">📅 21:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100779">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🔝
با اعلام سنتکام، دو سرباز آمریکایی در حمله ایران به اردن کشته شدند و یک سرباز نیز مفقود شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/100779" target="_blank">📅 20:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100778">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlwRoIOLeYgVZUU4YEazo2JfdIMiWIv4dxvuMRuShxmwX1kNFlrMVgEuPaWRwzjDiZYtXxGYiLDC7jlY1fSS8GzgYyxkI3rGsLq3iU5f3IOC9aCnRWS0dr3v-H47J8RKepgLz--vPFhg6zQpUHOaxmxSoCKtpFlD3s458fPa49dqimNKtlOBgE-Xxh5fVgWW7tpEuh5VfITqlJ-QN5bV4bGIa4YPuQ0qWx0iwpxbrA5wa2jIKmlMiFEcqZckD_CcLBiIcILCssoxfj6srYswCRXjqqXsI7I6yx4ZDK7vFuJXNGbexQIX3GnM7w2ROqN68xRV4-_0AbJUddHzyfaM8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔝
با اعلام سنتکام، دو سرباز آمریکایی در حمله ایران به اردن کشته شدند و یک سرباز نیز مفقود شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/100778" target="_blank">📅 20:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100777">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOyugXVUVwKbjZhRBO8b85H846VMfm2sY5yTtzT6COXzd0PKTLAnhmDazbJegUvz0Ew7tsKRNr0JQghJxb2tl3KnQGKLsynkgaMpS5stCqynj6FeTEOsUP-MjmRlBwkhQt3tHUQ14Ks-Q0PhiZN1klCAFOpsY3EUGKrdMpGWhHDRURz9W75W_ZAe4TJq1ntgCY9gffev3OllCxI9_yl6-Tg2466X3nRgojDLY_T3dQShbrmFyCUfrm8eSjhP1CBBTqJRc6ltqn3LIAdvO0IjlT_AgnPYxW8Rcf78aHMufxcGUHIfuDxYJWkRdeVzmmeqGAfYoQXrjVXWdhay_1ZkoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
|| در تاریخ جام جهانی، سه بازی در مرحله یک‌چهارم نهایی با نتیجه (3-1) به پایان رسیده‌:
• 1938 —
🇮🇹
ایتالیا با نتیجه [3-1] مقابل فرانسه پیروز شد.
🔺
در همان دوره، ایتالیا برای دومین بار متوالی قهرمان شد.
• 1962 —
🇧🇷
برزیل با نتیجه [3-1] مقابل انگلیس پیروز شد.
🔹
در همان دوره، برزیل برای دومین بار متوالی قهرمان جام‌جهانی شد.
• 2026 —
🇦🇷
آرژانتین با نتیجه [3-1] مقابل سوئیس پیروز شد.
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/100777" target="_blank">📅 20:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100775">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utPtGfRJrzsg_OCakKb3461O8PxSWftERkqXSHJbrN0F4rifW125gqZccgjaZs8fYbXa96mlK8wVkRdezHH0j_U_wn3W89_jLX6SRrScB_wafG2I7YAu1iHJ01OQdLyV5gABWYsRikcTysGqr5SyY9lv3IGY40AtmQUiTktMaRcGT1I-IrBgOpPN0Zm5GjSKvJUzMKi1kTVYjczMmoP-_nCZ-6H1W60wxWzRVaij5VaJXrwl7QW1jWq4HrD4RmVBS_N0SLrne51WO7eSCnOj1ZToiAdmL7mmri8JA8hY1dDCndZpNe7Xrphwj28trGmKHamjS63MGreHDSgGGP1Kbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🎙
دمبله: "صادقانه بگویم، دیدن تیم‌هایی مثل آرژانتین که به فینال می‌رسند، در حالی که باید در مرحله یک‌هشتم یا یک‌چهارم نهایی حذف می‌شدند، ناراحت‌کننده است. آن‌ها با تصمیمات داوران به فینال رسیدند، در حالی که تیم‌هایی مثل فرانسه که بسیار بهتر از آرژانتین هستند، حتی به فینال هم نرسیده‌اند."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/100775" target="_blank">📅 20:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100774">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktfA3gxT8PbeRp_q3Rc4vvfMe6AoLOWmoCzsb3OGlBVC1oTrFhqNOdFHG7H0dYf45ERlbccmBQjpFZbu8cWuuljt-RqAvXH8Jxb8_BV6O8eQX3Ybg_MbPi3Bw5dGgRoxfE-kRCsqOTtEQFqYmgkRYJDfLqiWOLZ6q3hDJ2TboDcmjfyKf8T-Pt5A7kCoC6lgyneRBj_iLJOZdjNQDkmwl-Gh85q8c1qkCoyndA9hIsnYTmhwLOl0tx3sryanCEOWzTP0YcvkkCHsAarNdwfzmoLOq7dKuuuNtYaNsROBYu7KkwpLi2NuMUz7etkpxhbnU5q0wpky6H8NDXmKV5LgYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب منچستریونایتد مقابل رکسهام در اولین بازی پیش‌فصل شياطين‌سرخ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/100774" target="_blank">📅 20:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100770">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D9XppHfVa1UfZ4Gwlq8PMDUJat_9EMxtdM-uOp6OFQDbejz3vegf5vr02s8Pdbq13xWLirtuwiB8zwpQAxVjr25szhn0B9Z5z8Xk4PLYU_D2X8IP6IayCBvcUH0dmN3BiuvjEkfBcyHVNXfAxmroB47M9oM2VS9sptzl-okflta5UkinlV6u7lDhjl65YQdA--DvUBMhCHY2jbC75xaq8BzNWrpY3iTu6OgI719Xp6ENx2Ni-DLBd1CSdhWmofyZ87XD0ncrPd79McBufFNN1IEBbiEzxo9vXKozar6OozP-4OUlhvHmTGZnhWSSBXjPUzxT_jQAT7JdJOTfiZFEKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/smDcpSiSYq5prCq1XSWf-IF6neG8yShYMajWZskQqz5TDt_D3xBQDpLoBsGnrcAcqUhOdKxbn-ZRPoQYOP6wZ4OmGD9pIm6bMiLtno9I40XhguGh2QxIvTGCKhJ4z8-F5P1ko_v7kghh1W7DjvWXPRhIlRLBbENAkbeSKQsiQK6_KV8rmS3-0n9xKTq8XExycKR4lL35qP7V92ipPIEQVZSlKSsONQLxl0WEBBOCDkOcmQpnbZ1mA6VX5t4JypzyHvb23sA9IJe6J0Hn7lNu0fm4F_1cdunzAVTyKIbNfSNnUmTjIaN1Q4i8-jWP9ttWLJFDR8xSrYOYrgUqyJUkXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vTmgsbmVUrl8PcwW69PcWhO51YQwmqPdCOlGL0XeOjOWoWAoJo1yE0eQYFrVFE352QTOSdLewwzlfjEx54yfBxbwftigNdgvfS1Qx4L9PJ9xLbRSK9Hgim2heqiXWz32ST88_OL2fVOy6z92tvK-r-0QXgBD6e2_dQ8MiOd7sK0bADlzcZ_2xum9xtMW9b-N4Em9K0RAvUOUhYYvn8bWi1bECBBy7LD1uW6RfxyW3S6K_ypSew2Udr5Gqg6JwvHQLjoV5ZiDucTqQ3k3_Jg2oXKguVImjoN1hV6j4-BYSEX3BXvGZJlbLSnRU8WEf5CFvJPgDeKx9gfy7TRlDHUcgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I13pJeeP6HYF8xhdh3Gdk71zZbRiOIXTatl1le1HBsUqlvHCZq0suEP44gnsIk2p7TSIHSltznSfGHqZJkHX1ev9sVeH55hYfgiIRga9pt3FE6KNl_2QO0HcdaEZnHK0zHz7ZCE1wwAQ-ctVw9D4dr9rpAHB-XYf8VWOjN535BOv8e6B3yXSPrCUJJI2PAFU4ucEK2NX05kxEOyHYGwU1lZEsUgD6Owb7sxSp83agcje3TRAiHwjvqLz9XHPmktRA-pBwORxchvzbP8nUlau4vr1wwJeX-wcueLz_R7_WZFeYb6yHjgH055Isbge0vlEdpw9f2JNFWlMD7c2jr8xWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
🇦🇷
تصاویری از اسطوره لیونل‌مسی در آخرین تمرین امروز تیم‌ملی آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/100770" target="_blank">📅 20:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100768">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A86rOd1uZxGJOfJ0oHd7npssVWsfQnceXb55oy8YmeqA1RrDB9L9u6mRA27IhYvNJUb9XHks_u0eOBLAzYNC0NzMxtjPRxREsrBBB3-Qy14TNTAcgRSROXR6-JHcNLBAriB2oMdAeFLV6ilhbn4JE1aULnoLPtd0IuVG4KZlGacAWVoL6lEBKwwIz-drOsRJt36I5Z00xO5L6FsXyorbrfoGG5xJmMzzUIic5GTr4tjfMrqvwTx7VuvnMTcho8YInNJhmSkP40shMDWePTy7Ef94aCLwPc_S2jxF8dMqkqb_9JqqNiJP3lsL5oTdpwZgFp6iQQVRksD-NdYDIMNSng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/io_CI3YnafVXFQKYDMg9OkZBjTFeayIx7twqPXat0BFWkaXKVwsXMAIJYdSU6lqgfj7d0wlCghjZoyGy9XTJWV9-6MusGlNN8uXNve56B24J5dC47k7fxU8HmtiDXjXBAXxchFMsCq40X2YClFtcJ5n23j5oAS75Kc-rdn5EKL0hdxsHF81Cq7rsEYvXIsG5XhzqL19hBmjFWiCHe6yfEOc3yo3Q5eGUMTgzLcDEFK8uYxW4bWGFt-qTqTjVKHz85L9-5_YxfQ9NQV8esUiLpfS0O8pEHO9M8ZfC7PcU5-3bZBjSNzoKhtIXgQDL7kSswS-yPg3NgmvIA-BvhgoCtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇦🇷
برخلاف پروتکل‌های فیفا، آرژانتین تصمیم گرفت که در شرایط بد جوی نیویورک به تمرینش ادامه بده و با آمادگی به فینال بره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/100768" target="_blank">📅 20:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100767">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/871184ae5c.mp4?token=Ml5QMnG2xcfYrk6t_91GXS1bKlw2PrKA1HRGDFPj-Y69QF2Kd_LEUcJvdCneCoh60x7YvK5SaZAhfT9_9d-uXyz0PYdYGYhmp2VMS36epQJoj1xnl6Ua6uCld8RKtta1L5pVVj-suEXeDZtfrRmSzcqNFeSQ3hzEC4zGAVcq8SK4MVVGxvH38gFRULfTi3a0F6PcFkMFoqUuG33uT9HLYio_aQs-7sS0qRjNnwpURVmevPsYz8B0zBAALtZQOj8k-jSW3uSc9cxiJDdyf2dkxXg6IlEpgtgkztIKI7KBb4TZWCeC6IRYwwUIeWEWbuVP2TkLJScpcvOxm2yU9WiuPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/871184ae5c.mp4?token=Ml5QMnG2xcfYrk6t_91GXS1bKlw2PrKA1HRGDFPj-Y69QF2Kd_LEUcJvdCneCoh60x7YvK5SaZAhfT9_9d-uXyz0PYdYGYhmp2VMS36epQJoj1xnl6Ua6uCld8RKtta1L5pVVj-suEXeDZtfrRmSzcqNFeSQ3hzEC4zGAVcq8SK4MVVGxvH38gFRULfTi3a0F6PcFkMFoqUuG33uT9HLYio_aQs-7sS0qRjNnwpURVmevPsYz8B0zBAALtZQOj8k-jSW3uSc9cxiJDdyf2dkxXg6IlEpgtgkztIKI7KBb4TZWCeC6IRYwwUIeWEWbuVP2TkLJScpcvOxm2yU9WiuPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
این دلیلیه که مسی تو این جام جهانی انقدر آماده اس. به گفته خودش یکسال قبل از جام جهانی برنامه منظمی داشته و صبح و عصر تمرین داشته و سخت کار میکرده، دور از چشم رسانه ها. واسه همینم وقتی هری کین با مسی برخورد کرد نقش بر زمین ش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/100767" target="_blank">📅 19:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100766">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNaPHfHpjg4vQAqsqz6TkdXkQsZ1NmslYqJA62c-gTkGZJCT2VTPMLG59E7Bn8y3FzQSCxL-by5-qv1YeTWnQS8h4cWkUFfhIZMug8cUiYyVlZmwJ8mZO-7qxBcSOHgle9dLAi3az49cu04xG0Fl0gxak9xlD3xQF5M7FHOtNhlYxeWtvj8B8WLgvXKNlTz2gnk0BoGSseFRg4lDEBcIKUBVzVjYz-JUzcygJAr1VzS9JDDKgxWQ_NIwjsM6XeIOYy_UmnL85getNksvSwD8cick4U1i_NN9RkMXujpzU-5MXUC29dtIsNf6mg-bN9lijrxLA6iNgmPfTRl_WGhbuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
#فوووووری
؛ آخرین تمرین تیم‌ملی اسپانیا پیش از بازی فرداشب مقابل آرژانتین بخاطر شرایط نامساعد جوی لغو شد!! ظاهرا تمرین آلبی‌سلسته هم در آستانه لغو قرار گرفته!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/100766" target="_blank">📅 19:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100765">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JiZsuc3yQtMotYQvwY4Aa6gIgO1rjVia2L-xW63ZAHNYAI_IoA6-a0zmO7n1bIr4d1amp8UHRyLIZXB82Ehm-S4pfkmUgj0PKi2kfqzAAn11uFEQhFQINSKRrH9p2Sf5GvkN7__5O7dZvgi6YtJ01PjCtBO7BEpmML6J8Cyfxh6LKJR-iNjfthSQh-OnDOIZZE8V9fBKXHi4ZqD0jPPJG7Wm9x1yL-X-yo6mOIj3W2_4kD_vjfzd5eyHiGD4-PCDnCf8qNdKcSWmpdc4cH5Lj9l1ftBHdSllyjJK-dJYzC_tgsffkeZQVBxiTivrdMgc7mLoZe3RdAwhnYn7hv1n8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😃
🏆
دوتا از رفقای ناب سعید عزت‌اللهی تو باشگاه ردینگ انگلیس قراره امشب و فرداشب تو رده‌بندی و فینال جام‌جهانی بازی میکنن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/100765" target="_blank">📅 19:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100764">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6fa8f4aa0.mp4?token=mtX-AcenUpzwLE65W81patCUJeQ0gkr_c-_gMyyVpv8sUu74QaQAaTR1y0KN5cAFDDJ7hDLbJOqtXrPDtei1V1ixAj01NKzIFaPHo6DL6Lv621KtDRrw5QOZ01tAzw7jRyqYi5i0vMhAueF_xJLkjhkBz6rQZlqUzL2aEP5K17ieoanZlqM1meFFSGrg_C2W9AxNrY43c0fuQskVODWb7Znkj4zBEVulRDcCPuw4nbJolv-_9tODlz06DV6e43KmKrk8itM_zzLP3QGLpd9EegRWUTVGsU39pmn33wiBgw-Ae9VgL64PmrU33vO8xxyHDomDdpx3fG2MOw2ZC0BkVHIZ3RP8NnW2yhQAfjwV_j4DInwMbVyulv2Tx53UkYbAzPodT7E6ZDoz1_ya_QWsPZhqbCP4S3kJnHFa2vXeQzO8cKMkmSqVrwwat9_arsjQLwn7QzgAKfqzz7NicZW9LeKZQCHJPYaXKisXCvZUBvmNx89XOnQKPtv_o91ttAy2nOzNynJmhQ1ydIsJbcFnmLYvvBBNlHs9KFltCUAQaaw5VGGzD89-69T6XOSmFfBHAJe01H5mCiBTJOt_UNLlCv4Jq00FLVb-jExzjq6L-Yy_a8lBiV9dDK_8T-4d66ONPnYXK-xozQDgsQozzMe7rVEEsyRiLBiEnQh2yPv12ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6fa8f4aa0.mp4?token=mtX-AcenUpzwLE65W81patCUJeQ0gkr_c-_gMyyVpv8sUu74QaQAaTR1y0KN5cAFDDJ7hDLbJOqtXrPDtei1V1ixAj01NKzIFaPHo6DL6Lv621KtDRrw5QOZ01tAzw7jRyqYi5i0vMhAueF_xJLkjhkBz6rQZlqUzL2aEP5K17ieoanZlqM1meFFSGrg_C2W9AxNrY43c0fuQskVODWb7Znkj4zBEVulRDcCPuw4nbJolv-_9tODlz06DV6e43KmKrk8itM_zzLP3QGLpd9EegRWUTVGsU39pmn33wiBgw-Ae9VgL64PmrU33vO8xxyHDomDdpx3fG2MOw2ZC0BkVHIZ3RP8NnW2yhQAfjwV_j4DInwMbVyulv2Tx53UkYbAzPodT7E6ZDoz1_ya_QWsPZhqbCP4S3kJnHFa2vXeQzO8cKMkmSqVrwwat9_arsjQLwn7QzgAKfqzz7NicZW9LeKZQCHJPYaXKisXCvZUBvmNx89XOnQKPtv_o91ttAy2nOzNynJmhQ1ydIsJbcFnmLYvvBBNlHs9KFltCUAQaaw5VGGzD89-69T6XOSmFfBHAJe01H5mCiBTJOt_UNLlCv4Jq00FLVb-jExzjq6L-Yy_a8lBiV9dDK_8T-4d66ONPnYXK-xozQDgsQozzMe7rVEEsyRiLBiEnQh2yPv12ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
تیزر جذاب الهلال عربستان برای معرفی کیت‌اول خود در فصل‌آینده مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/100764" target="_blank">📅 19:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100763">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OT2qJq9IrTDCvbgrWHzLwvkaS-TkQTHQ-XuOPh5uTPCeCZv_6XdPzraQoGa1AKxJRXwu6m7YISBJIGq5DxbrnqDzVWHMnctA6qtOFVlGes3PyUP-17o024bSeBHXFtKv9nQRdja8iigvq4JYzco3KZgJjDvwFUrM-Ur6iGoWnc0cbLXuJfkORf0KMhQZyW4V0dKYCbEg3HOYDVixoGmFafLGibnQk4_jzfROurPGLXQkw4dYiFmhdr3VgdmBSAbO8MMwZ7doOdCoFUTljLVCu2LH1wBuik6CNeyhDJPoac1nEiN0-jqhloPSQx3oqmBSqIms5way-1BVlhrj0asBQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔵
کیت‌جدید فصل‌آینده الهلال عربستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/100763" target="_blank">📅 19:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100762">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3cj8w8qDpvY8HfINKFkrWkruqSJA5UKSDdmfeQpoKXfRsOQTDB5JzyT81A9HAhftQpOYcSW253KDqilM_JqvN2090Y9zu3NPS7aWqmvVQBmiljDQTpPyB2nc0W1OIIfmNHpJiGVVhMkyGwJSk70SaY7PDIXRfqv8pjenbQtCSraWcDvCVMutJ0TPZLitDiGa_eBrQLb8AQXN5qQlfq1cV123R8de9nom6ddqu-UManGJ95u6auEz2ZrRddrrxdJAdYtwFjVAmR4QaB5XroSpMF0l9-R_FptL__N0XaLezTsllGhumTZm-nMegllQk_r7TdsVYwKzmG7IOKrNBKjpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🏆
جوایز فردی مسابقات جام‌جهانی که فرداشب به بازیکنان در ۴ بخش اهدا میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/100762" target="_blank">📅 19:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100761">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/778c75cfe0.mp4?token=EP1XhvMyqd97Y60ouzcZzpQwGeZzmlz1pTb8nxAviSmpVRiLucMJMm9gVeACsgi84z_z13nZCItvW-8-ZMgzv9vq3MM5yHIbr5kgT4RCSpV08LOXwuxZmMsJLDdg3XWk8ZO1Au0iqs7wCwXDuADXU1vtNvu080iHoHmMEXjcowX5_0Qefhe5s5AG0zhxwq6BYsa3yHhP0AKxmXykPMwXQb_z3UvOdou5Kx5nCxoQa-gUheKr6AeCgszA1sxKbEJ29tdQORv3MdUMBpYwEwVPFHERUkbqo5Ko2wiQlwD31UIPi7H0hImO5H27zgoDiG7fkk0IgHyjkUyUwD5FO82FNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/778c75cfe0.mp4?token=EP1XhvMyqd97Y60ouzcZzpQwGeZzmlz1pTb8nxAviSmpVRiLucMJMm9gVeACsgi84z_z13nZCItvW-8-ZMgzv9vq3MM5yHIbr5kgT4RCSpV08LOXwuxZmMsJLDdg3XWk8ZO1Au0iqs7wCwXDuADXU1vtNvu080iHoHmMEXjcowX5_0Qefhe5s5AG0zhxwq6BYsa3yHhP0AKxmXykPMwXQb_z3UvOdou5Kx5nCxoQa-gUheKr6AeCgszA1sxKbEJ29tdQORv3MdUMBpYwEwVPFHERUkbqo5Ko2wiQlwD31UIPi7H0hImO5H27zgoDiG7fkk0IgHyjkUyUwD5FO82FNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🟢
تیزر جذاب باشگاه الاهلی برای رونمایی از ستاره جدیدش فرانسیسکو ترینکائو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/100761" target="_blank">📅 18:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100760">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCA08WF3CQaAAePUDc56cOIBwHQljvi-1lmKzmp5h3_bNHmaoefstE1qoJpRw0pEp-8cPQQDBONKWvvER7x6woOLSIyPsUSI3SIpkc75cJFnMr8KfQsamchIqbSWzpDekN2cEHs-rmru5Ct6OaWbLafyxbZZKUpIbS2-85RD8tJ3jRDaCdZk4KD3JEZx2_LUtzwJclW1z-qgvLe-LGJ4QhWS2oXpaSBSn9f5UFHYX_U7u5699kTwFcNA1HLarLSr1qSeebPk9yXI9Uit8xoFKFwE_ByzVfWYgbChYea4GVmIh1y4f970xetONOJ8NSGcYAsWygFRxcd2HrO-RiggYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
#فوووووری؛ باشگاه الاهلی عربستان با ترینکائو بازیکن سابق بارسلونا به توافق نهایی رسید و رقم ۵۰ میلیون یورو به اسپورتینگ لیسبون پرداخت خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/100760" target="_blank">📅 18:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100759">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJGfkUu35HqfCvuYSb5h38UFU4QwXTxT4L3WkmIjF1qL2A60ohaL8Pzbqycw5qhDpA68DmWVbDEguPR6TNH4gfUE6Wn9vkcNoAc_WIQAye8KfHy6UHXuXia69Tb0_yC6PwY7UBrS8rnL8j532__Ll79ZRSLf-DDFiGqT58JG4U7euKLPRcZOk6qhi9WYO5oPj0jHTWOD5GMs57_VXntNW2PdgcvuqOnktKyXMIWpwwlo3Owl6jNm1XBf5FNO-KIEWp3lUf2bCpKSV6Pn0-rePKMHFe308vnz37_flZZ7_H_XRinuAA5cqu0Uu93YMlZZ4n9b39ooxydp64jgZBM1zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🏆
نوادگان یوهان‌کرایوف در آستانه فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/100759" target="_blank">📅 18:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100758">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLsV7r-TN1XINgBOL5Q6OiMxxq1Ob9k4v9zP4cTIWnMVDJ7vHBVf64pcWPfDHYeycjY7D6zsM-53jggCoAFoTofbqGHw4rjPIC1xVTFt7OYZrzzOfpjdY2q61Jitp3Vm43svejUb6AXVZSxxxmQ4r6jHw3oHDmkPF8Ur--FqjK7SErMa5X6NnVyMf3iNuUCjdna0R7DVw_uxIUND5yaX8tMzRdXJmZdio3RyozhQxQYSOBlau1Hz7hsgwPf5GJEQHOB8Bjhv6g5xKbIN9NRfCw0O94dBRALYR_45TkNavlaaQ682XzFR9KtQEfUwKQvHN5H-TDC8oxv2xeJwy33x_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
ترکیب دورتموند در اولین بازی پیش‌فصل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/100758" target="_blank">📅 18:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100757">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jV4YByk4rlQZSO7_Una20MJcr6AjdTGOItOy95ZU2KFdzdoNdw6TsS6w8Bz1o3x3-ntyPrVcX76KXLh6n0nMlHzMAZgSu8j42wjfm-SXRPIN2da54v7blNtAGH_y_R8xBM7oNIeNzlArFLD6C8uPVXZkJG2c5fGj_G_Hw0u3MQK2wU8S4_Ic5yU-ixegBzND4KAB1XJJI-gPoAqGih8MKkvjfkKXJAiboaf3kwzzpYXyBxG7m2bVLbiWxO_pAmTR7LrriZE-FhCC4Tm9agpJCNIotWnQ593QfFxu21O_JXexujCegLdee56NAQSqdrncBrZv2untgCDG6JhPyW5K1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب احتمالی رئال مادرید در فصل آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/100757" target="_blank">📅 18:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100756">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
25% پیشبینی رایگان برای واریزی‌های یوتوپیا
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/100756" target="_blank">📅 18:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100755">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=Q7djhk_Gw2KKkAWeR27uWaivVRk8tvUdoFO3WUgbyKWSOtl_ul2RPn7eNcwBEbjxSTbO91B1d7smN1sKTSS5YchiDcTziR5O8Vp0nSlurmB5WJsu9i9JksoDh_CDGpkN8zh4lugrl4fnlzPdUfPtp3f17f3vnJ5d4JLyBlr1uBG8FlOtyYHwpKolD5wLyAf-QG3Q1nE2Eiz2Yf6JFG5P06mLpj76pEuoIe_6NYZlAwGn1O_70knP6NZXBlEYdErglsCcGV7URQBKacttNv8HhMuMg6uXu9sIDcEbHeUE-O5jCbPAuLE1ZMnEJMpFmSsOgOGVFl14sxvGC2Lp9pdrpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=Q7djhk_Gw2KKkAWeR27uWaivVRk8tvUdoFO3WUgbyKWSOtl_ul2RPn7eNcwBEbjxSTbO91B1d7smN1sKTSS5YchiDcTziR5O8Vp0nSlurmB5WJsu9i9JksoDh_CDGpkN8zh4lugrl4fnlzPdUfPtp3f17f3vnJ5d4JLyBlr1uBG8FlOtyYHwpKolD5wLyAf-QG3Q1nE2Eiz2Yf6JFG5P06mLpj76pEuoIe_6NYZlAwGn1O_70knP6NZXBlEYdErglsCcGV7URQBKacttNv8HhMuMg6uXu9sIDcEbHeUE-O5jCbPAuLE1ZMnEJMpFmSsOgOGVFl14sxvGC2Lp9pdrpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌ جهانی 2026
⚽️
فرانسه
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
⏰
شروع بازی ساعت 00:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.000.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/100755" target="_blank">📅 18:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100754">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fanhDA7-nG8YXlalKEYZgrjEKTrGeVUm6jeMvCUHXYAhvBJDpY7KipS4w7-q5vCwnN2IGqqIev1zj5G1Hx75EftIEs3hkOeVo3ru8rHPNvzhfHCI3gRl_mBzReaIEmu63fjtn2_oPRxFDb2XS40NrlrTXhWKPc6yoLxv7yy6YKMFP1-U1viwPDgB6sELw32S6f5BEFjSkzGqaAjv_z-k2Ox4a6hfmB7HHNTWPlceLL72s6FIF8XXaldbtoxvksNGNedcLxeeUGOoullgwmaSbY91293MxVSHvp_32wHhQg79o_O3q_3ICf0luOISmX6FH33eO5_s9d6rnbD-JE1Pig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فکت
؛ از سال 1986، قهرمان دوره قبلی جام‌جهانی اگر به فینال صعود کرده باشد، همیشه در بازی نهایی شکست می‌خورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/100754" target="_blank">📅 18:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100753">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KqDXUchLyPmM0pF49QO6BG1Y0kc8BuH1T0zmEg7PBCY3rruQrj6qEUb1TlaUQVHM1mLXveGyjhiz0GKUBbzk5pJrvLO2NB2O9P8VLVBV5OL6gEeX-010wKh3BHXiPbzdQ8bZNJ7W1TnmeFNt3IESFl-eE9uIzQjuJHe3MlHFyuofZ7ObISk7zgjGv5dlLk9LvJlKi4RRjEDxRhvbRjEysOxvLznkk-uld8xVBZokM2x922rDiHXPLGWH7Ddqu2X3ouPhQZ4CnJnN0qwK7KH5PzJB12egGSdeSbpNTaMM9TR4H6eG8zkMmva0pVUWNBAeaFS0W7Kawb7gTKqeUJSs2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارش جوایز در «جام همراه من»
واریز ۲۶ میلیارد تومان تا پایان یک‌چهارم نهایی
🔹
پویش پیش‌بینی جام «همراه من» فراتر از یک سرگرمی، یک جریان پرجایزه است. براساس جدیدترین آمار، تا پایان مرحله یک‌چهارم نهایی، بیش از ۲۶ میلیارد تومان جایزه نقدی به حساب کاربران و برندگان خوش‌شانس واریز شده است.
🔹
در این میان جزییات پرداختی‌ها جالب است؛ میانگین جایزه برای هر پیش‌بینی دقیق حدود ۳۸ هزار تومان بوده است.
🔹
البته موارد خاص هم در این لیگ پیش‌بینی کم نبوده است؛ بالاترین جایزه برای یک پیش‌بینی دقیق به رقم ۸۵۷ هزار تومان رسیده که عدد قابل توجهی به حساب می‌آید.
🔹
این پایان ماجرا نیست و طبق اعلام برگزارکنندگان، ۴ میلیارد تومان جایزه دیگر هم تا فینال در انتظار پیش‌بینی‌های درست
جام همراه من
خواهد بود.
🔹
با داغ‌تر شدن تنور بازی‌های آخر، رقابت برای کسب سهم از این جوایز میلیاردی، وارد مرحله جدیدی خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/100753" target="_blank">📅 18:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100752">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D8FjAXviWtUBbYf7fMtKRVpjLudQhk7MbVYyRc74vFgDvCN48lMIa0D140nsZWfOJ1_t9wY6rF6B00g0tufnh8-W4hXrxtGhRW7Ob8SvC9dW4UKpUj7uSMbZCav1NDrfGpt74yqVjYiESVzB4e9rwEwH59dNEJHOTAnc5va8JYkioXdVm5-PAHobhp0pKgFnC-y1sBJlcLamYa3G4uOfnP3sIVrvE2DOBGBb9DkmCaT4SxLAVmIwal5IRSqPKgg42FC9IUrhWsQi6KZGDTxrVc7NkcluHmW5lKZKkbvTZ6FqfgYNUqbkOB6YQokQfhR1W_Zl96qSYt-W3Ft_IDurmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🔥
🇦🇷
استوک‌های مخصوص اسطوره برای فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/100752" target="_blank">📅 17:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100751">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVu7FV3I0ZDUbKf9zqHjHhgaLzMkml-FJrvEl7iDv4hzgCZumUVY-bvCpa8pe5RT__b6Gh916kkPTM7Cp0yUg0hEJZEKay4BOWwbL2SUf0r8JN3PUjRNQeDFkfFvTAWG1AqWFVGxWO0ySLQL4SH78EotK3Fi_EplfTmF-MQlD2f_Xbvr8JX7E21a20maeq8G43Gdq8QMBACroZGjMZGlnqghivcrVYKcAGtIRew_fk8N9qiz9wvRjZ1tUgqD761EsHlWkzEpgXx-ENjNQqrLLF6FLyNKFogyH1iqhSXPksU04fq-V86WXjLMXmAaV1u_IlpqRhdF6mC7rULlNGQykQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
مسی از نظر آماری بر تمام بازیکنان اسپانیا برتری دارد، به جز یک درصد بسیار کوچک در دریبل زدن، که در این زمینه لامین یامال از او جلوتر است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/100751" target="_blank">📅 17:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100750">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qj_jvljXqt5EOnDDDhh9RNuKz7jToseO2DYZGLk3BPrxeex235hLR-6SH27ttdAT3FKO_UW6cOrinHn1b8ZDGn-ZzMwusBNtJaQPAGIRQID3QWe6mF4skw4v7VcaWHTHAMhbFqcCsWaKXTYDAGTdDlybzxrjTgpx6fydgdkiF8GIzpxjcySSLwLTG-Zj7lepk1aK1hF-Y165Ae4zWI-j1Ns_IL8ocT36uIiutZNezhawgyWj_BaUeNxyMq2DL0VTPzq9kYq7c3FldF_Kdt5wyAXUlnsO5RH79QgD691X7WiW7GD5ngkYzkilziLOjxlW_BvwXZpAQeLb58BaoED_FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مارسلو:
من اسپانیا حمایت می‌کنم تا قهرمان جام جهانی شود، چون آنجا زندگی می‌کنم و برزیل دیگر در جام جهانی نیست. فرزندان من در اسپانیا به دنیا آمدند و من 20 سال است که آنجا زندگی می‌کنم. علاوه بر این، پسرم در تیم ملی اسپانیا بازی می‌کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/100750" target="_blank">📅 17:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100749">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WX0-HW6FhUM2RcDjazy6eIiEXF7NjFleSPOez5hko8hxbyjwS-PgDZ_3hC7ekXHfOViAUU2t5mexKhmaEnC9iLuc-y0zd6pZUhgNGOPtn0uUzW8-XXHyyLxDDOuNG6dWu12a_BYVbsJfzLjCg8g0ooS8ZUjy933BdA7YwNk0e9KRsyQgl6lWzJnd7nmrEX4RGnd9v_v97Fx-4LLmHMiw3A06daSQiNM1vJGXTJC9Q70lVOMBBTkavaj6C8qd_SSwVji6lSeZXAXYjw58rDrZovPvhz_QyFztVv0z5y-Q9U25NUyCfv82uIZG0sAEQIIdwTwA9GLzTNT5r3rdgLx58Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب منچستریونایتد مقابل رکسهام در اولین بازی پیش‌فصل شياطين‌سرخ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/100749" target="_blank">📅 17:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100748">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaDkDE9dUp1u5_WqtAUcvATw1nHteWgrZZFHtfcFUWT7-fLboaR5ikeOmy48ABObPF7ntIQj02R5HbbyXw9GFfYEibvswGQF8Z2aABH3PbbYfmEnxmd7xMkAk17VefqMi6wLqk3eQvTcTRHVBHzhCMV2rTbG8I5--YPuZJJFeIFcgeIuNS5IvYvmODcrW9AJyglmzpf9jG1pl8UX493kEyC8uWfW3MzxhFWBHgLEjXfLfRQbXVWnpMv_Wq13-vWQW5ywvf1SyCNzJR-v7HWJUFmWS-Cy4LcxTkpLIDtnPi7Q1_oSK-3qlIyMvAMPV4ryfKYeRt4ZxooAEUu223DI5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
#اختصاصی_فوتبال‌180 #فوری
🔴
🔵
برخلاف اخبار منتشر شده در دقایق اخیر، باشگاه پرسپولیس تا این لحظه هیچ مذاکره‌‌ای با کوشکی و اسلامی دو بازیکن استقلال انجام نداده و این اخبار برای بازارگرمی و مختل شدن روند تمدید قرارداد این نفرات است. گفتنی‌ست که آبی‌پوشان…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/100748" target="_blank">📅 17:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100747">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2480fbbbb.mp4?token=MRwg1v1vQO5YkeB5izGiO0I69xP6YUH2XLIW2bbVCSSyAsUKSWq1nALxUIrJl8hqLY0611wGpax5oj7hcFXFzFmYPEFlBE8X6lyt9dGBVxHVuFXeblFqSxY29FoQpuXZwWQqmLTbUcO5596eCpDCWbUDWxPQ8glP78j3BZOdEt9fCI807mTMOutRpH0LUhdEcEM-LF8wmYxDCSVUrgQz94TSN6qMvSvDkmpVcXlPB8Jq8jN8gW0irStg8q_nMUAf9S2knzqWcGKV165JZBXYxvskcmlSEHznpyJjDb_J3_ONW-Qio1VgGFrFRex0dY3XpnUewBv-tEaFmG3QlgICJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2480fbbbb.mp4?token=MRwg1v1vQO5YkeB5izGiO0I69xP6YUH2XLIW2bbVCSSyAsUKSWq1nALxUIrJl8hqLY0611wGpax5oj7hcFXFzFmYPEFlBE8X6lyt9dGBVxHVuFXeblFqSxY29FoQpuXZwWQqmLTbUcO5596eCpDCWbUDWxPQ8glP78j3BZOdEt9fCI807mTMOutRpH0LUhdEcEM-LF8wmYxDCSVUrgQz94TSN6qMvSvDkmpVcXlPB8Jq8jN8gW0irStg8q_nMUAf9S2knzqWcGKV165JZBXYxvskcmlSEHznpyJjDb_J3_ONW-Qio1VgGFrFRex0dY3XpnUewBv-tEaFmG3QlgICJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
انزو فرناندز که حسابی هواداران آرژانتین رو مجذوب خودش کرده
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100747" target="_blank">📅 17:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100746">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc579a6c5c.mp4?token=bc5kl6ohoPd-PjakYgAjwz2j1t_3oDnCBAsn_bDFwZJGjf2fJzsMWS85yVJbWvrkSwlnoRyh4FMttSxIHH-DAxatibZ0Qb3jnoalBkPq7-c1RgE4aVXYE2XYnuk1bvYd26Zdlg072Et4dvMRb2troVLtQnCVbd68I45xo8JXBsZ5rK0cjk7pEt1rlGqK9pCbpMtx0Pgvz-xCd12mhcg_0PMJuehUrf5S6NkvYJn8m-cNmkU397qQhcInaJL1XeZgKMtsO7CbhsThbtQhJ-nQRoCqR7oI-JWL_t67ZkzX5KDLeucD607DaU6Qlqg1KMAyJXCYQkz52mEXDFEE_36qjWBp4UlWb54GEoXWj9l64KD4mz4utIzU_dsQ7c6PtCc9ndIQG5nrIyY4Zq37ZcWay7ynNQAnfHQnZ0Z_PQMgmmRJaLbrjXbfx_PpcRAmOBhdVWD2jiMbyLE8rXmJwX8zIsZzhhRB6fa9CXdcr5Bb3gsEZuKy7DJ5hS-07DdzHLkp8DV7xHB_wKCIEkFl_9IxRphi3EAeKGmifXu5e512xs5WWdn0gMAKTmKhZJgxReJqNzkEDJj9aP1vXHfHMjuDuPkDcy17gqY4GKW7sK6a96GNyn54YJ5faXBeLB8Xy6csSQ_ILx1S7VSb7A6bQ4-bYhMG2HSU8VQnpPkd_cnphgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc579a6c5c.mp4?token=bc5kl6ohoPd-PjakYgAjwz2j1t_3oDnCBAsn_bDFwZJGjf2fJzsMWS85yVJbWvrkSwlnoRyh4FMttSxIHH-DAxatibZ0Qb3jnoalBkPq7-c1RgE4aVXYE2XYnuk1bvYd26Zdlg072Et4dvMRb2troVLtQnCVbd68I45xo8JXBsZ5rK0cjk7pEt1rlGqK9pCbpMtx0Pgvz-xCd12mhcg_0PMJuehUrf5S6NkvYJn8m-cNmkU397qQhcInaJL1XeZgKMtsO7CbhsThbtQhJ-nQRoCqR7oI-JWL_t67ZkzX5KDLeucD607DaU6Qlqg1KMAyJXCYQkz52mEXDFEE_36qjWBp4UlWb54GEoXWj9l64KD4mz4utIzU_dsQ7c6PtCc9ndIQG5nrIyY4Zq37ZcWay7ynNQAnfHQnZ0Z_PQMgmmRJaLbrjXbfx_PpcRAmOBhdVWD2jiMbyLE8rXmJwX8zIsZzhhRB6fa9CXdcr5Bb3gsEZuKy7DJ5hS-07DdzHLkp8DV7xHB_wKCIEkFl_9IxRphi3EAeKGmifXu5e512xs5WWdn0gMAKTmKhZJgxReJqNzkEDJj9aP1vXHfHMjuDuPkDcy17gqY4GKW7sK6a96GNyn54YJ5faXBeLB8Xy6csSQ_ILx1S7VSb7A6bQ4-bYhMG2HSU8VQnpPkd_cnphgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⛔️
علیرضا فغانی: اگر ایران مانده بودم، صدبار خداحافظی می‌کردم
‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/100746" target="_blank">📅 16:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100745">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e993550cde.mp4?token=Vt5zH1_G_YjNItUAGdh5_5EsL75lbmXEexQeyPRP6C6qGaoWVDw3h4RCE4YwOLzC3tJ1K5exM_b2AydpmBLLeTs7QM6KfD0QjJdQZ7CpN2prlfJ0I1qU0rYA-OgfyIcA_U0c0yBJtWquGuODj54_FZLtcwQBqxPG_bAyEm99SecoVfz5vYM9RL0O-oh-mUurJ-yuu-rAQ3fICZktSA_0QYbuOeKKLBZEpoJsX9EWadPJSdiXUQDyhJx4W5y-Pa0a0I2gt542nFl6Hu-YcIUUMqZDkZndVfwV4gBTVL6xnqp03qdolpeiDz4-N8xuwQg8VXZpviX9IXqQ0j4F5GZjuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e993550cde.mp4?token=Vt5zH1_G_YjNItUAGdh5_5EsL75lbmXEexQeyPRP6C6qGaoWVDw3h4RCE4YwOLzC3tJ1K5exM_b2AydpmBLLeTs7QM6KfD0QjJdQZ7CpN2prlfJ0I1qU0rYA-OgfyIcA_U0c0yBJtWquGuODj54_FZLtcwQBqxPG_bAyEm99SecoVfz5vYM9RL0O-oh-mUurJ-yuu-rAQ3fICZktSA_0QYbuOeKKLBZEpoJsX9EWadPJSdiXUQDyhJx4W5y-Pa0a0I2gt542nFl6Hu-YcIUUMqZDkZndVfwV4gBTVL6xnqp03qdolpeiDz4-N8xuwQg8VXZpviX9IXqQ0j4F5GZjuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⚠️
خاطره‌جالب سرمربی تیم‌ملی اسپانیا از تقابل با مسی زمانی که سرمربی سویا بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/100745" target="_blank">📅 16:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100744">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d4aefcaa3.mp4?token=e5mQ_0SXv6pLRMxVRy1BbCCYJRr0WgpajNSVzQs0xhz71_Lpomkm3A-tYdwNQ7a6LIZqmxlNoA1Qsz7CgjRm4qYWXdqpMAtEPce-_KBVYRQlvmSJ7ZZva7uaYCpmSbqhcJjHqD27d5jRreLNXKdf0ZD5Poy-oO7b5ZhNeY3DCXZkk7RhymOkpkUudHP2EE-5npu6G-LVHdK0sqGnTgPCz8N7dEs8-Qesi7DoR4ZGgWEUh3w_ZLSTK2mnX3lc6ZJiPV3erkfuFQW6kat0skIrxyJcVcnZtiGS3DPz3-yhogAq571Rf-0rAND0pDW8fuwOEtOKU5Yn74ipugg0Dya3zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d4aefcaa3.mp4?token=e5mQ_0SXv6pLRMxVRy1BbCCYJRr0WgpajNSVzQs0xhz71_Lpomkm3A-tYdwNQ7a6LIZqmxlNoA1Qsz7CgjRm4qYWXdqpMAtEPce-_KBVYRQlvmSJ7ZZva7uaYCpmSbqhcJjHqD27d5jRreLNXKdf0ZD5Poy-oO7b5ZhNeY3DCXZkk7RhymOkpkUudHP2EE-5npu6G-LVHdK0sqGnTgPCz8N7dEs8-Qesi7DoR4ZGgWEUh3w_ZLSTK2mnX3lc6ZJiPV3erkfuFQW6kat0skIrxyJcVcnZtiGS3DPz3-yhogAq571Rf-0rAND0pDW8fuwOEtOKU5Yn74ipugg0Dya3zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
هواداران اسپانیا در آستانه بازی فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/100744" target="_blank">📅 16:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100743">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34b9470b1.mp4?token=bjevH0n-3L2vaSTQnt8hLLNDM8qJBQUvrU1BLKlB5rluCBZa4FFhfLIWSFCaPzfGC6ktu4e9mLpeQcBOqGQij5gi_6_u4fd1n7S27LD-jySCfuKC-s3IoT6x2dU0suMo-ICm7WJxHyOdaA_IQrzikjY3SR6bFvbIpfQpLfAl6u_omDlx6h-JSzpEgx9aLUlms6MKGpMlhNCDxUYHsuA2IqbfSiaW1uKO-r76QIXAggetY4ltunblsjZf1gyLVouSnhntL_MoWlzF45aapX8G6LTOw1MF8-WUKsGfhElJFiG6Lg2AonUYFVWz0kTQrpo_2J2e5yTNG0Kx8C9me-CIig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34b9470b1.mp4?token=bjevH0n-3L2vaSTQnt8hLLNDM8qJBQUvrU1BLKlB5rluCBZa4FFhfLIWSFCaPzfGC6ktu4e9mLpeQcBOqGQij5gi_6_u4fd1n7S27LD-jySCfuKC-s3IoT6x2dU0suMo-ICm7WJxHyOdaA_IQrzikjY3SR6bFvbIpfQpLfAl6u_omDlx6h-JSzpEgx9aLUlms6MKGpMlhNCDxUYHsuA2IqbfSiaW1uKO-r76QIXAggetY4ltunblsjZf1gyLVouSnhntL_MoWlzF45aapX8G6LTOw1MF8-WUKsGfhElJFiG6Lg2AonUYFVWz0kTQrpo_2J2e5yTNG0Kx8C9me-CIig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
صحبت‌های پیمان‌یوسفی درباره چرایی عدم‌ گزارش بازی‌های جام‌جهانی از صداوسیما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/100743" target="_blank">📅 15:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100742">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94776f3b42.mp4?token=bc-VVU_8o19laN29ll8NbfLXDWhvM-AxgAY3teuN2vQ8rG6LkCTeRnTP7FbXH76KDIFaZ_NBDww9_3RBYg7AJvLJDxQQ-zHK-AzSGb-UwcZVZyyVlpZ7ULmM66y_KjeYWNUsYTw2z_D_ihyDuW96lvXxEcHJ2txgZaCZdlFe8hVs4lxEPtVgBD7tE57yfClswrOLYU4nxs905E8N0uyYtIgyCVQCHJe3JLqTmyTAN9Ax6KgziK203vlvHzGhydsR-iAcvQBx5JKSBNqhPo-OqA6ND2toJDdeysJZsoavN_-YbeHj0RPNTQnwWgkxiHstbmOT4PNozSVNU991i9dLcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94776f3b42.mp4?token=bc-VVU_8o19laN29ll8NbfLXDWhvM-AxgAY3teuN2vQ8rG6LkCTeRnTP7FbXH76KDIFaZ_NBDww9_3RBYg7AJvLJDxQQ-zHK-AzSGb-UwcZVZyyVlpZ7ULmM66y_KjeYWNUsYTw2z_D_ihyDuW96lvXxEcHJ2txgZaCZdlFe8hVs4lxEPtVgBD7tE57yfClswrOLYU4nxs905E8N0uyYtIgyCVQCHJe3JLqTmyTAN9Ax6KgziK203vlvHzGhydsR-iAcvQBx5JKSBNqhPo-OqA6ND2toJDdeysJZsoavN_-YbeHj0RPNTQnwWgkxiHstbmOT4PNozSVNU991i9dLcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😔
انتظارم از بازی امشب فرانسه و انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/100742" target="_blank">📅 15:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100741">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJuE4lErvwBka7qS79oWXgyEPavJSW9MhDCxm7MLNm_o-JisLwuK4ehdGj8gF3SL4kevCQfJsyhGVrV5D5-Y6HQVi5eqaSCiVFcJGv6tVbWSpK7FHeWtjZiJBi52DgaIfqHXtygplqBjMvnjhlvLwyo5XN2OT6lpVm7OgMFmtRF-aH2tglPKT8a0iXfM3kYzLK-VU33kFrJoD4q7196FPWzFk3Wf1GOvB7LIdyyjGE__gskS34FQdnTyhrxGW9avegMCyvfl1uAMp5jMLSTQqRqGbGKR-ZBy_kB6BoJrtAt5zySE8C_WCwkeDvjA7Ld_w-9GqPJPWwPJbPuuIMmsdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری روزبه سینکی که بیرانوند و نابود کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100741" target="_blank">📅 15:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100740">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EogqKOSwGneKpxunoLChYzOoaneDlYJGiZ6LHiJBv4Vepk1DkZbEIsyBX-OUnHzjUlY-GtgstW952yVlPT2dg_ZaKwca12jRkVcQQs_xf-EKQRU-m7Iomth3IjtfYHKU_EUgaQ0K7nU-QmmVGzrMmbEQO_oOCIDSBBc-v0SYYvooADyv9HHc5AOyvlaWVW1uHQipj8ButSFuk4rc6G2URrm2mHCT4dUvENWCeJvvptrwCBrvulx5iI11C6cSPJDRZ_g_tuQJdoru747K84e-37LFeYyKyk6bJEIxIjMZTmqIXO3faAERgIF_wjuIj-t2GjMMZysCnGzMhYu0QxiZbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">100 روز تا مراسم توپ طلا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/100740" target="_blank">📅 15:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100739">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
25% پیشبینی رایگان برای واریزی‌های یوتوپیا
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/100739" target="_blank">📅 15:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100738">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=K_10uM8_dd_hD9UFghTIp80F-Zx4ZjTXMNJzMLxl6ZKpf3drtEcwLnB5seZ7bbojm4go_xPWQfrjmeOtjYZ-eHJoSJIclK9xlAknWO2agOJBZYv-tBi6nikAw1kE44xwLW_2Ty2l33mmF_EgpXDY40ub6xDWxGimaBooAs1jgJh6yjk0tL4qfH42jePqz4cm2g90qBnHGN3OisaT-IgWhSzpMAyoV49G1ujwPuA9M-MPr_XCFpWOonrdOWvETwaOFIOfziWc91wMCIT85KEqKXOJwwVM7FCFeVOo2C_zkkWtkDqSloj58xqZgWtS5-fm_Sx4Z6rgRqzPvUoN_-v3dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=K_10uM8_dd_hD9UFghTIp80F-Zx4ZjTXMNJzMLxl6ZKpf3drtEcwLnB5seZ7bbojm4go_xPWQfrjmeOtjYZ-eHJoSJIclK9xlAknWO2agOJBZYv-tBi6nikAw1kE44xwLW_2Ty2l33mmF_EgpXDY40ub6xDWxGimaBooAs1jgJh6yjk0tL4qfH42jePqz4cm2g90qBnHGN3OisaT-IgWhSzpMAyoV49G1ujwPuA9M-MPr_XCFpWOonrdOWvETwaOFIOfziWc91wMCIT85KEqKXOJwwVM7FCFeVOo2C_zkkWtkDqSloj58xqZgWtS5-fm_Sx4Z6rgRqzPvUoN_-v3dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌ جهانی 2026
⚽️
فرانسه
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
⏰
شروع بازی ساعت 00:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.000.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/100738" target="_blank">📅 15:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100737">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9511ead233.mp4?token=BCICah6VZ2MO-Y1qRjBWt5PBJ7ihUV3pEUS3Irf_TXNHmvqOPcJzAU1XqaUjKHPxPoqysEKwnfys8_G56ryjWtNczkB86FPjCKHTfDlcDyQA1ZEw-MANOM2dSYxVfkZA1Ihh4FfwYT5T0_dUK4lGLMEKOv1PMjaMJThIBVl-D7lBSLbtzzbl85wCuzEWhNpxhLEmZem_BRjQ0IhAcU_Uw9GHk3dJBfYerkN0rz9gBN22ouK5YOFNT9Nytfe2hjP0Lk7GxMcna42Mam2ee6B1w382XXjrsxS9nKqOcFok088EN0H_ZJNFu0txtAfI7POSRmPVSsEIWIZjVmoQLxwVEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9511ead233.mp4?token=BCICah6VZ2MO-Y1qRjBWt5PBJ7ihUV3pEUS3Irf_TXNHmvqOPcJzAU1XqaUjKHPxPoqysEKwnfys8_G56ryjWtNczkB86FPjCKHTfDlcDyQA1ZEw-MANOM2dSYxVfkZA1Ihh4FfwYT5T0_dUK4lGLMEKOv1PMjaMJThIBVl-D7lBSLbtzzbl85wCuzEWhNpxhLEmZem_BRjQ0IhAcU_Uw9GHk3dJBfYerkN0rz9gBN22ouK5YOFNT9Nytfe2hjP0Lk7GxMcna42Mam2ee6B1w382XXjrsxS9nKqOcFok088EN0H_ZJNFu0txtAfI7POSRmPVSsEIWIZjVmoQLxwVEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
▶️
پپ گواردیولا:
جام‌ها خوشحالم نمیکنند، تجارب انسانی آن دوران که در بارسلونا، بایرن مونیخ و منچسترسیتی کسب کردم، حس خاص بودن به من میدهد.⁣ در حال حاضر هر روز صبح از خودم میپرسم: آیا دلم برای مربیگری تنگ شده؟ و جوابم منفی است.⁣
⁣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/100737" target="_blank">📅 15:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100736">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b0b7dbaff.mp4?token=nxw9t8lMxmSXMc4cp5a7AmAQ71YGLbrkxf6WX05GH8rsHnSEChSCqny8EAejArOkVbBDsMvxh95lkB0Fp8fZb4nQz1qWghSkE8H_1DYO2ftIPh3s1ieVHkqzRbgFD_cfa0mCVJFNFYDSSQJoRMyod_EymynOrRNTWMrDSY994sglXkL0y00-Uu2ze63qUp0A_qrrwDwgdoTn9QQiyH-UzzsGWL9fCZWE_-sFP9ki1Vx1ptAqpIL1JdpBdme1pv5ln8-8BnqQSi_1hDqKREBh-dhjHfFPzgYjJaKCO0meOXGidW82aGYm2WdvLM04woxLMF9XQ_lWiDwOMaclzDU13g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b0b7dbaff.mp4?token=nxw9t8lMxmSXMc4cp5a7AmAQ71YGLbrkxf6WX05GH8rsHnSEChSCqny8EAejArOkVbBDsMvxh95lkB0Fp8fZb4nQz1qWghSkE8H_1DYO2ftIPh3s1ieVHkqzRbgFD_cfa0mCVJFNFYDSSQJoRMyod_EymynOrRNTWMrDSY994sglXkL0y00-Uu2ze63qUp0A_qrrwDwgdoTn9QQiyH-UzzsGWL9fCZWE_-sFP9ki1Vx1ptAqpIL1JdpBdme1pv5ln8-8BnqQSi_1hDqKREBh-dhjHfFPzgYjJaKCO0meOXGidW82aGYm2WdvLM04woxLMF9XQ_lWiDwOMaclzDU13g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
فقط یک نفره هنوز داره به تنهایی میدرخشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/100736" target="_blank">📅 14:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100735">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4652c3d86d.mp4?token=AN-8rxOKwBrfzJ5XK2STAVuyu4Du4zHhaRz9eidKVlB397A91oLXz_MjYkKqNWMmvU3V02-9FxOM06zndBhtxWSbSC8z7__onjQt737ZDLJUN8yCVXEeXSrUnBiRBb8UPGHo3WahZoTn6oJVlaGwxipPzHsEpV8aDChuP3W3BcALw75WNaqYVWI2TLdbC2kO6uyTf8j2hl1wG9Wr_6st4bPQ7lvLsWpSwhIuIx2ax6K3IOKHqB43sZDMyH7fyMf6dYI50yNOWf7HWHFBuSxsVwi5-iNjKcc5hGjYL4sDyHKlBgi9bQ2TXdFe_V3GQG7oBDemghou8Tn56gq4ipBlJjIIqqEy74lAbFJtlrK9FYJtyI6i7TkpfhRLjwttcEoC1cdwFHDN8ZegCB6JBB-ynjXYEoz4F9Tf4DPvQVGSak9uAreMGzq6fruUwsq1rDGRybp7DRt4v3hf8VEAtmBhtJDipmb49OUe4b818Pk-GRm7CAn-tI9KnxId8-yLNQSbBN-iZrlg0CyYsoSuvidg4UHgEAjKiHO6PLuwA7iP41dqXXKJUTzXyx1uNk8QhRSZJRs0JGcljLScRSqcgeSNIb7u0ChPAetn24C2E7LB8h2K4cmiLEl5vhVM0ha-3sK9tSrmiYpV5vPjSEfp0KL5433A8-EmlRLfnd87WQw1MXU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4652c3d86d.mp4?token=AN-8rxOKwBrfzJ5XK2STAVuyu4Du4zHhaRz9eidKVlB397A91oLXz_MjYkKqNWMmvU3V02-9FxOM06zndBhtxWSbSC8z7__onjQt737ZDLJUN8yCVXEeXSrUnBiRBb8UPGHo3WahZoTn6oJVlaGwxipPzHsEpV8aDChuP3W3BcALw75WNaqYVWI2TLdbC2kO6uyTf8j2hl1wG9Wr_6st4bPQ7lvLsWpSwhIuIx2ax6K3IOKHqB43sZDMyH7fyMf6dYI50yNOWf7HWHFBuSxsVwi5-iNjKcc5hGjYL4sDyHKlBgi9bQ2TXdFe_V3GQG7oBDemghou8Tn56gq4ipBlJjIIqqEy74lAbFJtlrK9FYJtyI6i7TkpfhRLjwttcEoC1cdwFHDN8ZegCB6JBB-ynjXYEoz4F9Tf4DPvQVGSak9uAreMGzq6fruUwsq1rDGRybp7DRt4v3hf8VEAtmBhtJDipmb49OUe4b818Pk-GRm7CAn-tI9KnxId8-yLNQSbBN-iZrlg0CyYsoSuvidg4UHgEAjKiHO6PLuwA7iP41dqXXKJUTzXyx1uNk8QhRSZJRs0JGcljLScRSqcgeSNIb7u0ChPAetn24C2E7LB8h2K4cmiLEl5vhVM0ha-3sK9tSrmiYpV5vPjSEfp0KL5433A8-EmlRLfnd87WQw1MXU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
صحبت‌های میلاد‌کرمی از کارهای عجیبش در صخره‌نوردی که میگه هیچ‌ترسی نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/100735" target="_blank">📅 14:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100734">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf5731dc1.mp4?token=YDe9VVvY8buptU36N4lyy9ySbrY7fXC1b8-apFTkJyMB_NCGdAjFeJLihydpdXI7Sxo949BCe33q--LFZB_tPRBEnLI9QTZTsWTREUJwiudB8l2lXGA4Tr3XCTnpeNGTCZvT8cj5KMvcCcOI8183bGKa4tsQVYCMIDDE6xq5iMlwr0M2PzVZofRKUkk2f16yNYvp8d340TzdNuRboYp9vg6wmu392Wf4PzqRZOD7097DBlfCJpInDoRDmuDyrhsWgzrj21s3P6WqfmcakbXS2CRN8S9w2io-gYZd1yOSNwqgvoWsFVjsI6TVShEBkVdXhy4ADtKTwwJgCLEFJ9Z7KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf5731dc1.mp4?token=YDe9VVvY8buptU36N4lyy9ySbrY7fXC1b8-apFTkJyMB_NCGdAjFeJLihydpdXI7Sxo949BCe33q--LFZB_tPRBEnLI9QTZTsWTREUJwiudB8l2lXGA4Tr3XCTnpeNGTCZvT8cj5KMvcCcOI8183bGKa4tsQVYCMIDDE6xq5iMlwr0M2PzVZofRKUkk2f16yNYvp8d340TzdNuRboYp9vg6wmu392Wf4PzqRZOD7097DBlfCJpInDoRDmuDyrhsWgzrj21s3P6WqfmcakbXS2CRN8S9w2io-gYZd1yOSNwqgvoWsFVjsI6TVShEBkVdXhy4ADtKTwwJgCLEFJ9Z7KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب، قلب ایرانه
❤
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/100734" target="_blank">📅 14:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100733">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80daff883c.mp4?token=G3NAvRRgs9rWHX3XbJKl2TMgftitm9BY13YosZo2lmxdqZQ-ciHZIckWY873fw2KjfiuDCKEfsUxhwg7JMO3xI381fcXd4_rRujLqwPA34-llT_ryYmHsCcHxC8phODZWJijfuhfwqTDzXg8jTc27LgA_Po80kSMvkFv2-Hz60Ch6-ZJ1r2EmVH11YNdVms07_ENP89mStuMlqEwCqTm4puhidtjYZpGiMigYBhKf17vB0F4tIuI_Osr_V7yiWwKpnX7IsykkFV5j6O40LUBb3D21V73OBgPwBqWADqlaq2GdIe4ala890NB0Jt568v-CPmbU_vtzsxVhf8x3nRq9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80daff883c.mp4?token=G3NAvRRgs9rWHX3XbJKl2TMgftitm9BY13YosZo2lmxdqZQ-ciHZIckWY873fw2KjfiuDCKEfsUxhwg7JMO3xI381fcXd4_rRujLqwPA34-llT_ryYmHsCcHxC8phODZWJijfuhfwqTDzXg8jTc27LgA_Po80kSMvkFv2-Hz60Ch6-ZJ1r2EmVH11YNdVms07_ENP89mStuMlqEwCqTm4puhidtjYZpGiMigYBhKf17vB0F4tIuI_Osr_V7yiWwKpnX7IsykkFV5j6O40LUBb3D21V73OBgPwBqWADqlaq2GdIe4ala890NB0Jt568v-CPmbU_vtzsxVhf8x3nRq9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
نکونام حرف دل میلیون ها ایرانی رو زد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/100733" target="_blank">📅 14:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100732">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f306dcec7a.mp4?token=PMIC_VludABHU6_BdeUPF6UgcKGlxlGysVxXd07QCRXYhcDD_crminismRA0NqVCWf_A5c20W58znqifk0dTCqEaHhyl31GQMCMhyg-26CpaousIHpq-PCnEdSfnNX-zIAWC8Qh0vhZh0IB5LGcHT2eS7UHlruWG2oPeg5zC_h9jU80MwcyoHZyBRWAhJHsuL1zg0pLWVzdJSLz2GSH3BRTW1i05v7TROagNP3l9zXtsvJNoA9SysrQevDzROBXmnh2WuSNYbbuDNsk9bwTCdTbj-SxY3ulJEjguoBs-921ki37LeFMLFT4d-X5yEfqGtL_3SGaQvaHKrn3-8calySY3vBj9-Ys9JodsSBWqLxrY9KN7QKxCIEhjp6u3JKTSeh-54JeIRvtzOYwKpzL51K49r8WPsMJ_VKrzjZZN5yjhs_WkdN14DtntOlr1Yj-fieDPXhutuMktNivIug7_Jaj-t1NffNTF2jpwHVzqaX6EJp0bfoSGryffS1Frf2qKKxPfvGlvz8Lxn15Jfaiw2xekS-OJFcI9_1MkDgnMvjZJkqfOcLI9UQiATRAKe1n7EwZmEtK-L4dg5JVKGk1sjj6v8EcMll8wMf42Ynv4kasYDV737WTkWzfpIGKJYeu8txbEK2IDZtAsUecwQdGvj2zzeAYr7HbOf2NcocsBg-0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f306dcec7a.mp4?token=PMIC_VludABHU6_BdeUPF6UgcKGlxlGysVxXd07QCRXYhcDD_crminismRA0NqVCWf_A5c20W58znqifk0dTCqEaHhyl31GQMCMhyg-26CpaousIHpq-PCnEdSfnNX-zIAWC8Qh0vhZh0IB5LGcHT2eS7UHlruWG2oPeg5zC_h9jU80MwcyoHZyBRWAhJHsuL1zg0pLWVzdJSLz2GSH3BRTW1i05v7TROagNP3l9zXtsvJNoA9SysrQevDzROBXmnh2WuSNYbbuDNsk9bwTCdTbj-SxY3ulJEjguoBs-921ki37LeFMLFT4d-X5yEfqGtL_3SGaQvaHKrn3-8calySY3vBj9-Ys9JodsSBWqLxrY9KN7QKxCIEhjp6u3JKTSeh-54JeIRvtzOYwKpzL51K49r8WPsMJ_VKrzjZZN5yjhs_WkdN14DtntOlr1Yj-fieDPXhutuMktNivIug7_Jaj-t1NffNTF2jpwHVzqaX6EJp0bfoSGryffS1Frf2qKKxPfvGlvz8Lxn15Jfaiw2xekS-OJFcI9_1MkDgnMvjZJkqfOcLI9UQiATRAKe1n7EwZmEtK-L4dg5JVKGk1sjj6v8EcMll8wMf42Ynv4kasYDV737WTkWzfpIGKJYeu8txbEK2IDZtAsUecwQdGvj2zzeAYr7HbOf2NcocsBg-0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
صحبت‌های تند پایان رافت پیشکسوت پرسپولیس علیه علیرضا بیرانوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/100732" target="_blank">📅 14:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100731">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa83d99e99.mp4?token=lHB-IutMbXycxeurIgvVvXj8US4KcX-H70njQaDR9EiB7Cx_hbJBp4tes4f6h1Mg9Q_oyuTl-vBKXhRDXxIv-91GYsdkKZ3jp3riegCC3Ha-SUp6aHRyvvT0FgG9-kw_XCPiAJKORgkkC3XRaZXHh3XEUNa05gfnDaFde0ZpchAXTxS4vhfiOK5RzTUbxYQ1eu1LUYThlScu2o_UWUoiB-lJIQTFxucjEBZ1NdNqUJHXTyk9WtRDWPXyG2gAcoDe5PhDQyyVkd8Kbi1G5m9lFDR4bFVhTVHb21YjW6Oo_KXy6g9pFIB0Dm3gPINETaEZOQSBrQ3NgufqLp0c3w5rgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa83d99e99.mp4?token=lHB-IutMbXycxeurIgvVvXj8US4KcX-H70njQaDR9EiB7Cx_hbJBp4tes4f6h1Mg9Q_oyuTl-vBKXhRDXxIv-91GYsdkKZ3jp3riegCC3Ha-SUp6aHRyvvT0FgG9-kw_XCPiAJKORgkkC3XRaZXHh3XEUNa05gfnDaFde0ZpchAXTxS4vhfiOK5RzTUbxYQ1eu1LUYThlScu2o_UWUoiB-lJIQTFxucjEBZ1NdNqUJHXTyk9WtRDWPXyG2gAcoDe5PhDQyyVkd8Kbi1G5m9lFDR4bFVhTVHb21YjW6Oo_KXy6g9pFIB0Dm3gPINETaEZOQSBrQ3NgufqLp0c3w5rgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
اسکالونی درباره مهار یامال: بهتره توی رختکن حبسش کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/100731" target="_blank">📅 13:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100730">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d64bba4d4c.mp4?token=YWBi5zlsJSfVENBrB9Px7BYsUV0oNqClO_vx9fgdzWoW2lbz2xrgeNk768ukyTGULVYbxhzVY6E8kSykbQrLChR-RKBQcDYSRkOCqz2I294hUiOZOmnncYcfxTzvFjolO6z-J7GRLWlVeGk2F00hEGA3VskQLbKWZwjGWNtctyMB2E91oO-dDi25-bLBINF1n7UisBtv_aVpqUSIlrWtUv3swKcREOxKpnV-AbQaubMk8mNtPhLtlolhnI3x_flud00O6iP8GakdHQEqIn8EFrCP23Uk7KPcGOlvkbUd6KQwjE1oIetiTie4Q5zLqc502r9OgoyDukcJPy9KhaH4RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d64bba4d4c.mp4?token=YWBi5zlsJSfVENBrB9Px7BYsUV0oNqClO_vx9fgdzWoW2lbz2xrgeNk768ukyTGULVYbxhzVY6E8kSykbQrLChR-RKBQcDYSRkOCqz2I294hUiOZOmnncYcfxTzvFjolO6z-J7GRLWlVeGk2F00hEGA3VskQLbKWZwjGWNtctyMB2E91oO-dDi25-bLBINF1n7UisBtv_aVpqUSIlrWtUv3swKcREOxKpnV-AbQaubMk8mNtPhLtlolhnI3x_flud00O6iP8GakdHQEqIn8EFrCP23Uk7KPcGOlvkbUd6KQwjE1oIetiTie4Q5zLqc502r9OgoyDukcJPy9KhaH4RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🏆
استادیوم‌های جام‌جهانی یکی پس از دیگری درحال کندن زمین چمن‌شان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/100730" target="_blank">📅 13:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100729">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_r0AtnwUSXcQ5E422YydksIEmMA8qlNzaQUOte9e7H6iZt_NKg-VCjt2a2k7a6z3F_QdriwfwND4tlJKYN67WekFwGrIIa2RpmIy6gnhnJeuzLHvlml3EaaHKy5SXqKL4yE05Q6Z5zmNp5mJcPHfwIai5aIkMnEQMiMPOi_Pa2qQX2TXQ2_PClfMRw42eNP9IbOTvikz6DqALDdJd7HXT7UAFVZsdviI_w8e9xkJi8mwEV3jD8kWNtJ7l7Nm20CdPZZAhllhXOpYHf0UkVwemeioJqDuVG0XZ7q8n6i9S2tGlQVKmd0n_fi6snuSmsrc4PD2-SoLzNM7beIKUoPuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
طرفدارای گلزار کم بود بلینگهام هم اضافه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/100729" target="_blank">📅 13:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100728">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6593b1cf82.mp4?token=tsFflwPVFcLlyVobOwmy6_10MkVC-9Rii7g1OdsNKnwZjyvUYPMfgDPG8Y6kvnFcXqM-QTzfz3JSrTMEpK1daHYwifuWAT9B9AY39Bc_SzBYmq01VcY8Bl1tQeispeGgggb07sPhhbsP1tAuqKP4Uh5f-dKiNg0D8VDPoM1eXXyZMb5cAjvg9cDUvk-9EkJKDFoiTKmb0k1Rb7l01FvIl_95IDka8S_Ve6U59ZaA55ydPqlhIL4vBASUSpCcrP5UujFntBSiUTv6C1fTJYy6p8qVIkpvHGe_N6AEyhRN4-RM8lUL7nmNx7DcTOs4iwB-f4TLGU42E_8-CKth0Pwogw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6593b1cf82.mp4?token=tsFflwPVFcLlyVobOwmy6_10MkVC-9Rii7g1OdsNKnwZjyvUYPMfgDPG8Y6kvnFcXqM-QTzfz3JSrTMEpK1daHYwifuWAT9B9AY39Bc_SzBYmq01VcY8Bl1tQeispeGgggb07sPhhbsP1tAuqKP4Uh5f-dKiNg0D8VDPoM1eXXyZMb5cAjvg9cDUvk-9EkJKDFoiTKmb0k1Rb7l01FvIl_95IDka8S_Ve6U59ZaA55ydPqlhIL4vBASUSpCcrP5UujFntBSiUTv6C1fTJYy6p8qVIkpvHGe_N6AEyhRN4-RM8lUL7nmNx7DcTOs4iwB-f4TLGU42E_8-CKth0Pwogw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🎙
جان تری: "برای من که اصلاً هیچ‌وقت بحثی وجود نداشته؛ من هنوزم معتقدم مسی بهتره، فارغ از هر نتیجه‌ای که تو فینال جام جهانی رقم بخوره."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/100728" target="_blank">📅 13:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100727">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cdd66519b.mp4?token=T5DAPD8ZQ_sUetMwQM9yUQIz1_UGx8WcAjZGHgmnBCpz_kpcAqLV1QQgfaAiBg93Sl1TtJRbJCfgH-z3q-vbhE-uhf4bzb7SQjYdVCFpIfH9AbtXmGUQDKfd3hOpuvqgHHXpGIr1qjy_61LRHymLEX7sgFm9MCh63AUx7xD3KNKm_h8aggVp-v_F5_iZfDEZv0mPf4y0bzHsV4XZTNWt45LGL5rjtwd6Pycl6uAiLZ_7UnLtl1bgCVIfnUqWQjpMyKqHCjopAhdy1VmcpjjOiRHR42A5nM9PYfdcsqirtDVOONSKMD2adxghIymX769honQoEUHdv2AjeCjwgXWgSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cdd66519b.mp4?token=T5DAPD8ZQ_sUetMwQM9yUQIz1_UGx8WcAjZGHgmnBCpz_kpcAqLV1QQgfaAiBg93Sl1TtJRbJCfgH-z3q-vbhE-uhf4bzb7SQjYdVCFpIfH9AbtXmGUQDKfd3hOpuvqgHHXpGIr1qjy_61LRHymLEX7sgFm9MCh63AUx7xD3KNKm_h8aggVp-v_F5_iZfDEZv0mPf4y0bzHsV4XZTNWt45LGL5rjtwd6Pycl6uAiLZ_7UnLtl1bgCVIfnUqWQjpMyKqHCjopAhdy1VmcpjjOiRHR42A5nM9PYfdcsqirtDVOONSKMD2adxghIymX769honQoEUHdv2AjeCjwgXWgSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
هواداران جذاب اسپانیا در آستانه فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/100727" target="_blank">📅 13:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100726">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVGinc5dm49l9YEd0OUVutMV41Z_A7Efy8LcwOzfRGegimR7wlGcJqn5jUL-c0zXNN_OjKP8RpJJ5DHONUEdKmarm8_PKDliiJuzZ1p9-WGrIp03aynDtm3qe4dZ2WmM6E3P7nSHl49HcYKITuJOUv6QNCQXrcjlwJT8e34xpjG1iluv21rqhZCvHp5Si102jygY_mjGsJrF1-GH1Fcx0YhPaSl8gjyuiuykx7J2JAnpStGaxW0DIwTsNoKRzBtNRygMnhM7WtYcYe4XbbIj5m3Q7WauYRGhVS0QvNE0h1GfQ5lvWvRYx5kAIY8gAqsAQ8Azg-k9GmPr87Z_r1ON-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🏆
رئال‌مادرید قهرمان جام‌جهانی نمی‌شود؛ در صورتی که کوکوریا با اسپانیا فرداشب به مقام قهرمانی برسد، نام این بازیکن در فهرست چلسی ثبت‌خواهد شد چون در فصل‌گذشته برای تیم‌لندنی به میدان رفته و جزو تیم چلسی به حساب خواهد آمد...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/100726" target="_blank">📅 12:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100725">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32d7d110aa.mp4?token=Y3rnh7L5r2QE8yNVpFe10feNsXA_N5zof2_c4msqmvHI3F96allrOrXT3jm50XuAnRD4KouP4DUrsWHgxQ59RT2uqa5k9mbPoWjxxYL22XV3F0w9UWhxLRo6teZWSfAYOfwvrw6WECR63w_y4Gy6isnjUfAJ2JXjih8hZ6b1cWDJHCx8xOpgAoTdcgPsxknRx-MM4g0_Ikpx1rEZX2TGST_VdoZQhfhFb7kIw6cyf8osXBr0cNeEkzaUsQfRT1kLDsuv30ORgSYUeRIk7RqHENG75WWbIsYz8r2xFGZWHULDHRmadszj1olAqwbdzRZH1Xb9d757QK-rYpClHbN_qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32d7d110aa.mp4?token=Y3rnh7L5r2QE8yNVpFe10feNsXA_N5zof2_c4msqmvHI3F96allrOrXT3jm50XuAnRD4KouP4DUrsWHgxQ59RT2uqa5k9mbPoWjxxYL22XV3F0w9UWhxLRo6teZWSfAYOfwvrw6WECR63w_y4Gy6isnjUfAJ2JXjih8hZ6b1cWDJHCx8xOpgAoTdcgPsxknRx-MM4g0_Ikpx1rEZX2TGST_VdoZQhfhFb7kIw6cyf8osXBr0cNeEkzaUsQfRT1kLDsuv30ORgSYUeRIk7RqHENG75WWbIsYz8r2xFGZWHULDHRmadszj1olAqwbdzRZH1Xb9d757QK-rYpClHbN_qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
خاطره سوپرخنده‌دار علیرضا فغانی از پیروز قربانی؛ بهش کارت زرد دادم؛ داد می‌زد، می‌دونی من کی‌ام؟ من کاپیتان استقلال پیروز قربانی‌ام
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/100725" target="_blank">📅 12:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100724">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/050e680fa7.mp4?token=iSZW9t8kqrG2iCsPAFtTd_wJ2J-8rd_Cq0btSrTRr8QEoKKKVkdtB5H-8rMbbooDtxTLiN_bymHSn_Rafkv7-fWj_4egS8ds02nCLmolnhzUA_pW88Jp8MVF8KcmPwBkUosSxv86eZYNL2r69WKExhDAsq18e_YaRam_42AYKIUKi_sfbDqhh8H9IlyAkBMHIm7-mjvwyBsn_fjqLjn44uCc_LizMp1uKRJpxbc0qdOD59nzMOaSOFOuKRwm4hCsPNAeGS_U8eA78CkRvUWpEnMMwMKPqJX2uqqGrNVL93fGrc-rfnpQoC7eCMAFMKWQLUo5XyrJ7qN5gX50lvroIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/050e680fa7.mp4?token=iSZW9t8kqrG2iCsPAFtTd_wJ2J-8rd_Cq0btSrTRr8QEoKKKVkdtB5H-8rMbbooDtxTLiN_bymHSn_Rafkv7-fWj_4egS8ds02nCLmolnhzUA_pW88Jp8MVF8KcmPwBkUosSxv86eZYNL2r69WKExhDAsq18e_YaRam_42AYKIUKi_sfbDqhh8H9IlyAkBMHIm7-mjvwyBsn_fjqLjn44uCc_LizMp1uKRJpxbc0qdOD59nzMOaSOFOuKRwm4hCsPNAeGS_U8eA78CkRvUWpEnMMwMKPqJX2uqqGrNVL93fGrc-rfnpQoC7eCMAFMKWQLUo5XyrJ7qN5gX50lvroIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
👍
لیونل‌مسی تو مراسم‌ شروع بازی با اسپانیا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/100724" target="_blank">📅 12:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100723">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38913219e4.mp4?token=Y6Y55pA-dJsrZUtZvfkaNxQWqfR3lVhDk1Gx3g8cl_lzCwfs3DyA5kR1qP99v5k16Zn4O0ywIRzt5KA2ecxwMUCWrPJGTyll2XJahb-Sfv9B1JThIL1IoT1m5B4TKwcr3Xomb-l6v4h42Zfx17S2zh2wrhMx9Yvpd8gUREaVe5hDBwOYkCAIGkjzdX_CT61BQT03YFt2QPCI8ul6qbQjOF1fUy5VPHZckfoKF2jYv-rvTHEExHVeFv216XLchgUIkpd9YmYKIhPV4794JHlWgiB1jM6YfjGqwt4ZGUozaaZG1WGSBNS0LSjQRd6eiqQ9IYxYYneIdtv6M75RttqB6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38913219e4.mp4?token=Y6Y55pA-dJsrZUtZvfkaNxQWqfR3lVhDk1Gx3g8cl_lzCwfs3DyA5kR1qP99v5k16Zn4O0ywIRzt5KA2ecxwMUCWrPJGTyll2XJahb-Sfv9B1JThIL1IoT1m5B4TKwcr3Xomb-l6v4h42Zfx17S2zh2wrhMx9Yvpd8gUREaVe5hDBwOYkCAIGkjzdX_CT61BQT03YFt2QPCI8ul6qbQjOF1fUy5VPHZckfoKF2jYv-rvTHEExHVeFv216XLchgUIkpd9YmYKIhPV4794JHlWgiB1jM6YfjGqwt4ZGUozaaZG1WGSBNS0LSjQRd6eiqQ9IYxYYneIdtv6M75RttqB6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
زندگیت مثل گیم شده، مرحله به مرحله داری پیش میری. الان به فینال رسیدی. آخرش چی میشه؟⁣
مسی: من این گیم رو جام‌جهانی قبلی تموم کردم!
😎
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/100723" target="_blank">📅 12:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100722">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e94327741.mp4?token=dJDWcvnFcUYmco03xH-V1Jcqh2xfs64VLuz9K4QDWdIwi9Bto3i8rnB-iEag0MVAZ27i1ZOMdU5bR0YBd9s9pK_Ae3Z9rbJ9B6J8b4aaY36srNwivHnH2eoBHViqagXNST30IXYp-isThYee2fQTBVXz0zXzXhbFnoEqu_uMQY23L68x-Bmlear_zxUMHOZagEPlCKYggj-IWNXhefiPP3ILIm6MUsRuDejYh9nOvxuAfQDapmFo2XuGDZTxBI-j_npmqcarDsimDgjdyOm8VTcH2cgqUdNdfR0JXm9xUanWfCBnPRacH21peTyy9kCjJN9_eqOv9PE4zHwLZolgtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e94327741.mp4?token=dJDWcvnFcUYmco03xH-V1Jcqh2xfs64VLuz9K4QDWdIwi9Bto3i8rnB-iEag0MVAZ27i1ZOMdU5bR0YBd9s9pK_Ae3Z9rbJ9B6J8b4aaY36srNwivHnH2eoBHViqagXNST30IXYp-isThYee2fQTBVXz0zXzXhbFnoEqu_uMQY23L68x-Bmlear_zxUMHOZagEPlCKYggj-IWNXhefiPP3ILIm6MUsRuDejYh9nOvxuAfQDapmFo2XuGDZTxBI-j_npmqcarDsimDgjdyOm8VTcH2cgqUdNdfR0JXm9xUanWfCBnPRacH21peTyy9kCjJN9_eqOv9PE4zHwLZolgtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحنه‌جالب از لیونل‌مسی در بازی با انگلیس :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/100722" target="_blank">📅 12:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100721">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X852GsABEL5Cp4rhr5telnxPuPKrCWbY9uxql1wYCMSEmT4huuYAYldCBZ0GkYaWfxj5uRzxRsqvgFDGPMSgsU35EtW2URxa1vRNRhxgkdySbbY73_1E1dfSfuFWpCajhDofm1KvoEaqZL7SAV5Z5fu2AfgwRKUJKPsTdv_TE7joJyhCR1qJVLSWzds-LW9sv4C9ZthEuJVrTDJ-IIlFdyQHryP72mYOHtHvldhbp76QWwC2s9lDlZdtXi0b772vvddoqNH3SU1h4kFiyvfSgIE-3i9XGoioDtnfwHxdjjSDZkGFhWw9y3daauMGXjQrjDRvhY5XApgV0Z3kz4ZhqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇪🇸
نمایش هوایی جذاب در نیویورک پیش از بازی حساس فرداشب فینال جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/100721" target="_blank">📅 11:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100720">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyIbZNeM1UpO2fHLAQGuCzzYYHgD-FJBkaCZJ0AAy5C2a06AQfVAFhj5j_XZ-xUJctY9Qth7w7Cs4lQnXTlZxqZ9_7zPQ0JW79uMDQvx-BUoeh0ZrasyMbotYblr_Mmf5OxArL4slWVA4uTybCUSs2VkLkl_vH9iIrpgEGEtY42XJCchzpDoWCKp7uJp_7bJJEjJSVJltyzipffdBdik6N1Jhg0LF1uoWX1VwRtg42WlejhPHNJEH7AMfYSGt4zenrzrwqHGF_F08dHu11C0wGFA-ed9avSnFiZxilXVCj911wIJHYv5sGLCwjv4ZwACuphWjt2e-XuG74rY0ofcsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپید نحس
😂
😂
تیمای بازنده عملا قربانی اسپید شدن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/100720" target="_blank">📅 11:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100719">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/474e4374db.mp4?token=fmKitRD8HoBygXpIL1-SziMVZSV1urI3jqyg4Az1y_ErseFO7ZSZLWoagXttBnlUjg3Z0jeHXsYZ-HBAnivYmLHmmX3VYBMg6l3i22TP3sTOY7kn9XmVRWfukqhgfAQhsHG8kcsh6Fl80RGFPkK6766tmHwhBonW1vKGT9Ev72K98D_m9C3WugKJ9GXaQnxopE1OLIjge-deZ5sz3kSdjsFvgmaKGyD-wyWFSJQhaEUKJl1DrUu2bklKzodJJY7cUckoeDiNOj9BFTHqq_2c7LJsRBWgyJ3YAZLxzAgN8kPVksPE7IgXtBAjFtm-qs3R1ppS7iqd0WrGvXUm5aL0sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/474e4374db.mp4?token=fmKitRD8HoBygXpIL1-SziMVZSV1urI3jqyg4Az1y_ErseFO7ZSZLWoagXttBnlUjg3Z0jeHXsYZ-HBAnivYmLHmmX3VYBMg6l3i22TP3sTOY7kn9XmVRWfukqhgfAQhsHG8kcsh6Fl80RGFPkK6766tmHwhBonW1vKGT9Ev72K98D_m9C3WugKJ9GXaQnxopE1OLIjge-deZ5sz3kSdjsFvgmaKGyD-wyWFSJQhaEUKJl1DrUu2bklKzodJJY7cUckoeDiNOj9BFTHqq_2c7LJsRBWgyJ3YAZLxzAgN8kPVksPE7IgXtBAjFtm-qs3R1ppS7iqd0WrGvXUm5aL0sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
سوپرگل میثم‌تیموری بازیکن نفت‌آبادان در لیگ‌یک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/100719" target="_blank">📅 11:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100718">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4iqLNzggj2wwgYkOW5RMticyD2JpJQllgHS5pWcRnosl2tn4ht8Wx3Mvnr4nCxEVlo-bZerlyeK-_IDErEYAbqS8pDbW7-0w_A3H8IvkrWAAacDQfUjIexAp2VxcGY6MUet-ZW2T1r1hcWTuVzAP8_Zq_3JpmFYw33dfy_3H3rlPu7Z1vCXLsN8tndb6McaTvuJU5eQy73R0WjEHYsip9cemzwah-1BGD5xWB7OJXq-xPGFYykJJq2tcGoP8rSnzA7DLCsFj0go_3UBIO1B8G48y2bJ3m0_maXPyqyF4XZbiE-eeR7shnN_EeH1u9IctXGOc__50TzjkInYXKtWWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوووووری
از نشریه بیلد آلمان: اولیسه در تمرینات فرانسه به بازیکنان کشورش گفته که فصل‌آینده قصد داره راهی رئال‌مادرید بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/100718" target="_blank">📅 11:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100717">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5c0ee7122.mp4?token=ojyL2Sfw4d-37xgNQ5wT2YIjCjvZt51Bt97PmuwJgAWmS2DZzai1hfvWLCU-6IedOcABcQZnir46QwVNSELQaGHFbKu1uANVrS9fBhbP-8zw0SDG2weu-DU2BALYVU4JT3WHaWP-b5-uftvtAkO0a3Hd9rn47H7V6t_KDocBFUusrruYWMGTtCL8ssnaYMO_sPs5U5zHbLSFqTI-Sz4Rb6PvV5JNJ4UsMEmPMGc9oZttS88RwTnh2D-FWrUEDKu38AEyGCjcgUgqIkMLKs_u4AW1rs8qV79jJfBHHJ1xH0FoH3A3pG1tI10co6rpOSVc7NYD5qtkSlpMdSDsZ7afIIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5c0ee7122.mp4?token=ojyL2Sfw4d-37xgNQ5wT2YIjCjvZt51Bt97PmuwJgAWmS2DZzai1hfvWLCU-6IedOcABcQZnir46QwVNSELQaGHFbKu1uANVrS9fBhbP-8zw0SDG2weu-DU2BALYVU4JT3WHaWP-b5-uftvtAkO0a3Hd9rn47H7V6t_KDocBFUusrruYWMGTtCL8ssnaYMO_sPs5U5zHbLSFqTI-Sz4Rb6PvV5JNJ4UsMEmPMGc9oZttS88RwTnh2D-FWrUEDKu38AEyGCjcgUgqIkMLKs_u4AW1rs8qV79jJfBHHJ1xH0FoH3A3pG1tI10co6rpOSVc7NYD5qtkSlpMdSDsZ7afIIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇵🇹
علاقه شدید پوریا پورسرخ به کریستیانو رونالدو و عصبانیت او از تیم ملی پرتغال بخاطر ندانستن قدر این اسطوره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/100717" target="_blank">📅 11:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100716">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71ebbda285.mp4?token=sUT5MGR-tYxm3x52H2Wpk5UvY2cgGF50dgvyp6iyvumLWl86vaQgEgT3chq_b2WT54opTY1alsJYxiW89KpHnGi3FsM1C3UprCCMtMWPyDh_R_tsPpmltojjh3D_J6KRMWDN3D-VW41_teO-UJimMnI_IgQ8NMUbijyBCuWlp-ZtIqXYbR5kGVp7_Z4vPh0944I0cUM8Gn7Fo7tLVnBmDqluUxcbA2t5IswkG8FqZfSRfpezSBpwzAvmF9nb7pXIJhPxtpr3olZahebgIOKVc1_OU5GL0uI7IwF7f3IO3hBgDqA9L-pyI-B5fdNBAwXMB9fSQdXZycR8XUue0I3oqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71ebbda285.mp4?token=sUT5MGR-tYxm3x52H2Wpk5UvY2cgGF50dgvyp6iyvumLWl86vaQgEgT3chq_b2WT54opTY1alsJYxiW89KpHnGi3FsM1C3UprCCMtMWPyDh_R_tsPpmltojjh3D_J6KRMWDN3D-VW41_teO-UJimMnI_IgQ8NMUbijyBCuWlp-ZtIqXYbR5kGVp7_Z4vPh0944I0cUM8Gn7Fo7tLVnBmDqluUxcbA2t5IswkG8FqZfSRfpezSBpwzAvmF9nb7pXIJhPxtpr3olZahebgIOKVc1_OU5GL0uI7IwF7f3IO3hBgDqA9L-pyI-B5fdNBAwXMB9fSQdXZycR8XUue0I3oqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
🏆
کوکوریا در انتظار تقابل با لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/100716" target="_blank">📅 10:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100715">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3GoyR8P6lAGWkxU5K1FoVQP8oJpG4r53GoP5bLkYuldy1RUUlYz1JM8U2scCiot5Fv6qXi3yGbrRyduR7YENNlSvJ_DoiKba8CnC6VN4UuKNMkPRBLtDgCB64fz87qhnhzLZBJZ1CQYL4caSsyL-R3oD20Jod6tg-ToR8j3V5M63hIMU1LiOq0VROVi-5j1HCVfunA6Tik19gUiV3JbolrVM4ZUnfspo_sBOGbLcm1miFOzsS4PG9garFcwxzhlC4mudnkVM8idWIoW85vWlP8Ax4wLdR2iOlkpU_VLE3CZkfLow_xRpEsiQM4S9_93DPafaF--gzd8Mx4o-xLKWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جان‌دوران انگلیسی از ژانویه ۲۰۱۵ تا به امروز در ۵ باشگاه مختلف بازی کرده
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/100715" target="_blank">📅 10:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100714">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/638800ce9d.mp4?token=bbUVQXPN7o2szV3wnbsmWnf83vr0lC-9FP2hskNEAgNRCX4bSq-q5aZEfhtJ2bsY0oThTGP82XFN1pH5QTe92Emt031n8-K2PHWG_CtVroaexwdFKTthsE6v_iAKvzJjsifSJuedANBh31XwbfCGDx5A3ycCpGKQxSCRq6XAxxehf0iXO8tN1zlIhj-qHsbEQWkQI6SHPoSp60pnobYHPdaQjpIt3Wa-ULW8NEMtHMM-2IcEkJWyuKERvnudqrmMRC2FS0rg1ZjNZ6ANGfl5ksvG6JBwmsNn3YbpTi6hAnx15kn9WJ5mKgUp994nHlhG6LABlJV2UG4FsktHCtVq1pXVxvDqZqp1QIC7Yeq-RoQWuVt008QQycI132U22WiY6B66j_7iRCc2HY-pnqKNr8_VGcoyCM9U_hJzILe_Pb6VN01U3nypNbKiKgvk_w0veaN_pRRN_Kg1QcvSuJ5l6mZ9otxAhaG5v9dThEwRtpomtivu9liTdoFeShJDCdLhMaibra5qXVw4fMOPU7Nr7Txn5sufjqcdtUWEOuuas7SQ4PFQXWRwcOUEovb8zcYCuHEqP7-r63vMiJoa-YQ6WCRGiob4v1itokYY2iDy5Rw4LpH6sGXHt1QeTHjAVsNUSMy3lxJJ2NUe-AQAapfJtMYs4OyyrF5Sorg128nU3BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/638800ce9d.mp4?token=bbUVQXPN7o2szV3wnbsmWnf83vr0lC-9FP2hskNEAgNRCX4bSq-q5aZEfhtJ2bsY0oThTGP82XFN1pH5QTe92Emt031n8-K2PHWG_CtVroaexwdFKTthsE6v_iAKvzJjsifSJuedANBh31XwbfCGDx5A3ycCpGKQxSCRq6XAxxehf0iXO8tN1zlIhj-qHsbEQWkQI6SHPoSp60pnobYHPdaQjpIt3Wa-ULW8NEMtHMM-2IcEkJWyuKERvnudqrmMRC2FS0rg1ZjNZ6ANGfl5ksvG6JBwmsNn3YbpTi6hAnx15kn9WJ5mKgUp994nHlhG6LABlJV2UG4FsktHCtVq1pXVxvDqZqp1QIC7Yeq-RoQWuVt008QQycI132U22WiY6B66j_7iRCc2HY-pnqKNr8_VGcoyCM9U_hJzILe_Pb6VN01U3nypNbKiKgvk_w0veaN_pRRN_Kg1QcvSuJ5l6mZ9otxAhaG5v9dThEwRtpomtivu9liTdoFeShJDCdLhMaibra5qXVw4fMOPU7Nr7Txn5sufjqcdtUWEOuuas7SQ4PFQXWRwcOUEovb8zcYCuHEqP7-r63vMiJoa-YQ6WCRGiob4v1itokYY2iDy5Rw4LpH6sGXHt1QeTHjAVsNUSMy3lxJJ2NUe-AQAapfJtMYs4OyyrF5Sorg128nU3BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
آخرین وضعیت پل‌‌ها و تونل‌های هدف قرار گرفته شب گذشته در استان هرمزگان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/100714" target="_blank">📅 10:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100713">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e91953d632.mp4?token=Upxe01j-C2CClkZyPUPN9gKztpwEgGhCMv3MTB9b2WUquIwJq48XXfcX42C5ZDVlLBy2rr3A3hou-Pptk1n11y7RWvm2HJhGx7FUzAWZry5mnIGmcLHfN6aYBZVCsZwooISjEQsGJd1G21n_3VL35TwyNOqi4bG-HkKKcF0LkQ5Mv9SudDeZBPt9mkP89oewC-Ooehq0qeifH1OKqDpuLCbKX77Jl47TxT1lhOIyfSMQq11fcnho0uPZUePlNov-jQth6KmKPDiEXjknFJkxB9srkI2ttpjhsBJsDxfZmu_olhEL2MqGWwUUcJcF8P4pN8Esl2z43Y2NyEoLNeEq1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e91953d632.mp4?token=Upxe01j-C2CClkZyPUPN9gKztpwEgGhCMv3MTB9b2WUquIwJq48XXfcX42C5ZDVlLBy2rr3A3hou-Pptk1n11y7RWvm2HJhGx7FUzAWZry5mnIGmcLHfN6aYBZVCsZwooISjEQsGJd1G21n_3VL35TwyNOqi4bG-HkKKcF0LkQ5Mv9SudDeZBPt9mkP89oewC-Ooehq0qeifH1OKqDpuLCbKX77Jl47TxT1lhOIyfSMQq11fcnho0uPZUePlNov-jQth6KmKPDiEXjknFJkxB9srkI2ttpjhsBJsDxfZmu_olhEL2MqGWwUUcJcF8P4pN8Esl2z43Y2NyEoLNeEq1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یامال رفته داداششو برده آرایشگاه قبل فینال موهاشو رنگ زده
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/100713" target="_blank">📅 09:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100712">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2382f600b.mp4?token=iHc9zpFRREH_8rMrCwRyhluXdx1bromiZK_SXXlKXetcjHBzTgwzg4Dn2vEEsz8kHN_6b-D-yBWLpOYcELmC0XAodK-PnymP1Iw2d22mAHqT1aNQTFPIxucmQov8frJLhhVvbcqeIdbmVAshBdpQ2MzzJcBMV0j3kSKWy3XndAD5yVxj89OnMZKfjO7WXHsp5KDGAld1RuAaTaoUaWTqJSe4UsPkRoDAEd0K_F0xQvAOAz44dz9v8y9UGGRmXRPJtl3TmrUt7set1UhsRcQQ4a85AvIVQVFGmCUtFXKpO0el1jleUGSag_abPCY3nHJ_S5AKds21x76t39W5ElXlmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2382f600b.mp4?token=iHc9zpFRREH_8rMrCwRyhluXdx1bromiZK_SXXlKXetcjHBzTgwzg4Dn2vEEsz8kHN_6b-D-yBWLpOYcELmC0XAodK-PnymP1Iw2d22mAHqT1aNQTFPIxucmQov8frJLhhVvbcqeIdbmVAshBdpQ2MzzJcBMV0j3kSKWy3XndAD5yVxj89OnMZKfjO7WXHsp5KDGAld1RuAaTaoUaWTqJSe4UsPkRoDAEd0K_F0xQvAOAz44dz9v8y9UGGRmXRPJtl3TmrUt7set1UhsRcQQ4a85AvIVQVFGmCUtFXKpO0el1jleUGSag_abPCY3nHJ_S5AKds21x76t39W5ElXlmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚫
افشای مکالمه مسی و بازیکنان آرژانتین بعد از پیدا کردن بطری آب پیکفورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/100712" target="_blank">📅 09:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100711">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dccbf84030.mp4?token=HTrFe0JFtLPpVojc0LSInKGDM3aQ-Dgo7yiwvm5gePm_pMubeQLy15LVWvRRttccS5jjkIreAuGEnvDLG56ZMV8DnZxJ45auInLrWnZvvc1cP5bFlUgnHCGwdLQTUtCyorC-WnBQNtHYlqM__UMiDezy6iCecF4_lYSnbviFuLMjpzHIAKMMlihE89qGnEPBgytEgZNmI4O-yxdMeg7ptA5YK7DBR7oN2TLwcuPtQUBx2snrDjuD3plPg1ib2EZXwUR_I58bkwW8xfHorOHLsKGmj6QopBuijjtlIaESqY0sbYNbL9ri5YniWAGsObxlnbL0ZpCZQw_CYobwlC1X0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dccbf84030.mp4?token=HTrFe0JFtLPpVojc0LSInKGDM3aQ-Dgo7yiwvm5gePm_pMubeQLy15LVWvRRttccS5jjkIreAuGEnvDLG56ZMV8DnZxJ45auInLrWnZvvc1cP5bFlUgnHCGwdLQTUtCyorC-WnBQNtHYlqM__UMiDezy6iCecF4_lYSnbviFuLMjpzHIAKMMlihE89qGnEPBgytEgZNmI4O-yxdMeg7ptA5YK7DBR7oN2TLwcuPtQUBx2snrDjuD3plPg1ib2EZXwUR_I58bkwW8xfHorOHLsKGmj6QopBuijjtlIaESqY0sbYNbL9ri5YniWAGsObxlnbL0ZpCZQw_CYobwlC1X0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
صحبت‌های عجیب وحید قلیچ کم‌عقل علیه عادل و کریم‌باقری و سلطان علی‌آقا دایی!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/100711" target="_blank">📅 09:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100710">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIUc9OrnLOfw8R154URMTZwn8rLtODMllx8hQ9mHtT387gdbTqlo5GvJjg4v22XQbFFdLH1uFm2-X7MOyilmjfFePv6l7Ru8jZoq27hDo7NakIOp3uAta3Wq_6x7wEoP4DgrBja4JPHTDjo68tmuFthRXhhvVQKDkt-DW1OzRy7zCTrpNCUb43cDPvIiWXGgC5zHMBdzrcp9elNdADMrzB-B04KQh_zsL_LmGjM33CaCXPa66TqSCv1JqMeMbpPP-zWClp-klkDQJXHCxq1pLql6SxuqkGCzf9k2ddrvJI7njlmu8rIr6M1abhRzbUwJcaW-HEHViKChRwz_joZWKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⚠️
وینچیچ اسلوونیایی در جام‌جهانی فقط یکبار برای آرژانتین اونم سال ۲۰۲۲ سوت زده که تیم اسکالونی مقابل عربستان شکست خورده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/100710" target="_blank">📅 09:03 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
