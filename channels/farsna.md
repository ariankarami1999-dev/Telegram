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
<img src="https://cdn4.telesco.pe/file/UvZolvtp92K9s7Snp8sAbm3VdXwsHK1X8g861xxNnFrJKO5zB2w1FBOMyaOcuBENmxOck0gX8e-2mMmTyITPd3vhfk6tGDc6a933qq6u6t9PzTysfWHUj6UV3vZuMxC4OIOAhNMvbMU7mEhnDikGgIZEs34JSLiwMRqmklRp9k0ENEdSZD6gjkRQPCuiYStqPaZSc7EiP9W3o6a5vpZFdca_2XrPQokkvYVE51QT5rIEB_pclemtYkfv2YAItY8Hw_wv3Sj4z5sTkoEFTbJ05EoNZ19pctva_UKvVtASovS7hxT-kQUuAXcn5FWU-luEB_MKmKfFnN8jLC1llljrIQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 17:08:24</div>
<hr>

<div class="tg-post" id="msg-439878">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hv5_s2yNaj70BTsG1n3QrLpHReo2j2SBRtybFvRil6A05Adrrykfa8K68uay6ota5d1FKAHLFxNVrvNI4kosS8Bf2orWOcwSVCaFiib58XG41UGiTlckNDjLxjb73mYqkL-8-FRjarVWvCWzfZ9jqJrIDyHdmgdanT6yJY8XmsiuMpV-82qvzomrmddSeGhHWadgHKMVemb6NwGuLDbSx4NcMbRZLWkj2SurBbhD_QVp7JuXvXtUrJ3LkF4gC7r-odQLuw2LOKY9Q5KmDFFD6jceVj_rgWHowXl0Gj5rBeC0EMLKHsz3pL2IzAnGdfMsh_aejVmSqXI-YpR7zFryqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: حفظ وحدت، انسجام و اتحاد چارچوب و مبنای نظری دولت وفاق بوده است
🔹
با رهبری عالی‌قدر انقلاب تجدید پیمان می‌کنیم که از این سرمایه گران‌سنگ حفاظت و حراست کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 55 · <a href="https://t.me/farsna/439878" target="_blank">📅 17:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439877">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🎥
جشن خیابانی مردم بندرعباس در شب عید غدیر
@Farsna</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/farsna/439877" target="_blank">📅 16:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439876">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2f1aa555f.mp4?token=aT1rt8o5tTLwIhvvPsFDAnDbILUafkWJ2WY_02Y4pP1pk4Qm-OpEMzOGL5ETLIurSbjzAW_0KLQ2Rhu4HwF37cXM_tH-_MdrjOSbDIxb2qMP9Yz8f-BNJT9QlLFvI5u45gQnuWSmmo3t-EhDeEfCLGH90H6Oh4ALZxhboo1EiKG7kUPD0Ujpfu3e15a3ARfM9dCaWCAXJfSR_5aElUvGtOZgx-_yz8dSmItOo4SC_7kJ44IKkOqQjRUqzDhBDXkfoKZyYOQMqGIHwylagaltMwjiJLFH9Y4i6QdV5zDHfjEplWWZriocaNRG2tIw7gm5dfHefJCv5LGf2l9jT4zTvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2f1aa555f.mp4?token=aT1rt8o5tTLwIhvvPsFDAnDbILUafkWJ2WY_02Y4pP1pk4Qm-OpEMzOGL5ETLIurSbjzAW_0KLQ2Rhu4HwF37cXM_tH-_MdrjOSbDIxb2qMP9Yz8f-BNJT9QlLFvI5u45gQnuWSmmo3t-EhDeEfCLGH90H6Oh4ALZxhboo1EiKG7kUPD0Ujpfu3e15a3ARfM9dCaWCAXJfSR_5aElUvGtOZgx-_yz8dSmItOo4SC_7kJ44IKkOqQjRUqzDhBDXkfoKZyYOQMqGIHwylagaltMwjiJLFH9Y4i6QdV5zDHfjEplWWZriocaNRG2tIw7gm5dfHefJCv5LGf2l9jT4zTvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اگه بخوای از رهبرمون آقا سید مجتبی عیدی بگیری چی می‌گیری؟  @Farsna</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/farsna/439876" target="_blank">📅 16:51 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439875">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
خبرنگار شبکۀ فاکس‌نیوز: آژیرهای خطر در شمال اسرائیل درپی حملات راکتی و پهپادی حزب‌الله به‌صدا در آمدند.
@Farsna</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/farsna/439875" target="_blank">📅 16:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439874">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d5e069b42.mp4?token=Y_lmZYtecQOSXIxtirolr7ikpDsSahxUeNqiZvHeysqcYrO4EkACj-PFdhARom95GI3XdalByoNubKNdPWKWK9CwBq2wNq-QsWt-F2gGuhnG-q1g4IpVLdbTr-CEiiQrKfyHmGQT9Fht1idNjBY4VSp7b3kvshUoXANqWnu9rEscPoN_kc7KFw2lmXiZNv-8JBSJ3GiMZtHdorcsytHBf6ou1TNEtHeooqo_G4Ps4fnA3C2JfLqfKtypwipgUx4SoBkOu507qDxutYUSdESeJStju5oMWKr0ROe8SdScnUbLfBhAmSdWF4x0bEts3YNNkw_sqAdbENor4YY0I96arw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d5e069b42.mp4?token=Y_lmZYtecQOSXIxtirolr7ikpDsSahxUeNqiZvHeysqcYrO4EkACj-PFdhARom95GI3XdalByoNubKNdPWKWK9CwBq2wNq-QsWt-F2gGuhnG-q1g4IpVLdbTr-CEiiQrKfyHmGQT9Fht1idNjBY4VSp7b3kvshUoXANqWnu9rEscPoN_kc7KFw2lmXiZNv-8JBSJ3GiMZtHdorcsytHBf6ou1TNEtHeooqo_G4Ps4fnA3C2JfLqfKtypwipgUx4SoBkOu507qDxutYUSdESeJStju5oMWKr0ROe8SdScnUbLfBhAmSdWF4x0bEts3YNNkw_sqAdbENor4YY0I96arw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تا حالا از سید عیدی گرفتی؟  @Farsna</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/farsna/439874" target="_blank">📅 16:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439872">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0631d4a758.mp4?token=NOuVyAjML2TsdHmfg-R9AhpWQ5XPkBcu_PuRtc9twHo-OYCB--BxmeO8n3KeKZ4viaf0kH20KUFWZpZlROXnZePE-cg3Hff8Ym7wSpweG5sIUB0JMAnMysjxT8yvzdvbkYQFOSwuyHbGSv5cmKAgi-VIPNuPoddhQv1c8BYbSehEswSOP6LHia04rdJ0bppXXLPfqEtKnBfza4xk1lzB1Bk6SYKako10kmx6_eUJIrfUBbP2JOzXLRQyTYKSh14rTZuJFd6vlKU1ohTkGfJHIvcZlfotzhrowBLC9j4Fx7ofqsgusCzX4dybheYpQ5pSkz3jjJM7Larq8xrX8f3c0g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0631d4a758.mp4?token=NOuVyAjML2TsdHmfg-R9AhpWQ5XPkBcu_PuRtc9twHo-OYCB--BxmeO8n3KeKZ4viaf0kH20KUFWZpZlROXnZePE-cg3Hff8Ym7wSpweG5sIUB0JMAnMysjxT8yvzdvbkYQFOSwuyHbGSv5cmKAgi-VIPNuPoddhQv1c8BYbSehEswSOP6LHia04rdJ0bppXXLPfqEtKnBfza4xk1lzB1Bk6SYKako10kmx6_eUJIrfUBbP2JOzXLRQyTYKSh14rTZuJFd6vlKU1ohTkGfJHIvcZlfotzhrowBLC9j4Fx7ofqsgusCzX4dybheYpQ5pSkz3jjJM7Larq8xrX8f3c0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حنظله مدعی شد: مدیر ارشد موساد در عملیات بمب‌گذاری به هلاکت رسید
🔹
گروه هکری «حنظله»: یکی از مدیران ارشد «واحد نفوذ جدید» موساد در بخش مرتبط با پرونده ایران، در جریان انفجار یک بمب کارگذاری‌شده در خودروی شخصی‌اش به هلاکت رسیده است.
🔹
این عملیات پس از ماه‌ها رصد اطلاعاتی، تعقیب و مراقبت مستمر به اجرا درآمده است.
🔹
آیا دستگاه‌های امنیتی رژیم صهیونیستی جرأت بیان حقیقت را خواهند داشت یا همچنان به انکار ادامه می‌دهند؟
🔹
حتی افرادی که تحت شدیدترین تدابیر حفاظتی و امنیتی قرار دارند نیز در سرزمین‌های اشغالی از دسترس مقاومت مصون نیستند.
@Farspolitics
-
link</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/farsna/439872" target="_blank">📅 16:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439871">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64842bfe2c.mp4?token=VTecwrWTviBx1QoQyJyOvsFS4a2Ql_TDJomaYJlVAxjjAzgGI-SDZC_gtBNiELDoXt6GENmbMGqy3v4pU83Ahr1GkjIf3tpO_IE_VEwW4FlDy4SK3D1B166mHFIRbrL8ix1zWWNc6s3W4yU4vjicQHjbu2aVU1QiCehcBPBgMC9gaGsaY6VJVHQxPPqcSYmZu3gYS8IK-23ijd8h_cDRyvKESiSF2r6y0YdKSVOx9m8T0g7wnr0KMWvXOFVXHTxwWa4F-jSLR-dk91jW563vxINBPLbXrQrCYd3wICtmsS6qsC0A-Nagwk9-Ta_cUQoPUpes7c19cuvD2b0Td5c85Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64842bfe2c.mp4?token=VTecwrWTviBx1QoQyJyOvsFS4a2Ql_TDJomaYJlVAxjjAzgGI-SDZC_gtBNiELDoXt6GENmbMGqy3v4pU83Ahr1GkjIf3tpO_IE_VEwW4FlDy4SK3D1B166mHFIRbrL8ix1zWWNc6s3W4yU4vjicQHjbu2aVU1QiCehcBPBgMC9gaGsaY6VJVHQxPPqcSYmZu3gYS8IK-23ijd8h_cDRyvKESiSF2r6y0YdKSVOx9m8T0g7wnr0KMWvXOFVXHTxwWa4F-jSLR-dk91jW563vxINBPLbXrQrCYd3wICtmsS6qsC0A-Nagwk9-Ta_cUQoPUpes7c19cuvD2b0Td5c85Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دوست‌ دارید از رهبر انقلاب که سید هستند چه چیزی عیدی بگیرید؟  @Farsna</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/farsna/439871" target="_blank">📅 16:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439870">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‌ یوسفی: افزایش پلکانی حقوق، هفتۀ آینده پیگیری می‌شود
🔹
عضو کمیسیون عمران مجلس: اجرای کامل مرحلۀ سوم متناسب‌سازی حقوق بازنشستگان  و افزایش پلکانی معکوس ۲۱ تا ۴۳ درصدی برای شاغلان و بازنشستگان که در برخی صندوق‌ها و وزارتخانه‌ها اعمال نشده، هفتۀ آینده پیگیری…</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/farsna/439870" target="_blank">📅 16:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439869">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ef46a9d7.mp4?token=Rpx8J1iTOWu8JpVuNxXJW7Yy8qEFItpEv1r3jF8OkeW1_br8iTNNsr63nOF_Mt4G7JAhaA6vubreGFYrMqoKrEuSGzeyDFa5TExP0sYlEzbUHr6IcYJvY6Ov1RnG_ngo-i5WpcNjwhHf4zrp7yCy5hINfZBOJ_R09EIXub42Kw6v-CCJgNdowF8gRY3hhyobHKrMTaCD5iT0VK12qxsLXgDX5G5CXwkhfu6PkxSmwXIbj0XPJLzrFn6DFAvz8bhTyn_Md8iHjiW-d5A2aNwc6glBtrGutLWMAqDYuDEz512i0t0_mvItRbUt6ZECufwCSfZFbjOpe9kBHbct-U9uog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ef46a9d7.mp4?token=Rpx8J1iTOWu8JpVuNxXJW7Yy8qEFItpEv1r3jF8OkeW1_br8iTNNsr63nOF_Mt4G7JAhaA6vubreGFYrMqoKrEuSGzeyDFa5TExP0sYlEzbUHr6IcYJvY6Ov1RnG_ngo-i5WpcNjwhHf4zrp7yCy5hINfZBOJ_R09EIXub42Kw6v-CCJgNdowF8gRY3hhyobHKrMTaCD5iT0VK12qxsLXgDX5G5CXwkhfu6PkxSmwXIbj0XPJLzrFn6DFAvz8bhTyn_Md8iHjiW-d5A2aNwc6glBtrGutLWMAqDYuDEz512i0t0_mvItRbUt6ZECufwCSfZFbjOpe9kBHbct-U9uog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📸
ساعات اولیۀ مهمانی ۱۰ کیلومتری  عکس: محمدمهدی دهقانی  @farsimages</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/farsna/439869" target="_blank">📅 16:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439868">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: اینکه خلع سلاح مقاومت شرط اصلی توافق دولت لبنان با صهیونیست‌ها باشد، به معنای نابودی قدرت لبنان و تهدید موجودیت مردمی است که در برابر اشغالگری ایستاده‌اند.
🔹
نتیجه مذاکرات مستقیم دولت لبنان با صهیونیست‌ها از نظر ما بیهوده، تحقیرآمیز و…</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/farsna/439868" target="_blank">📅 16:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439867">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: قاتلان پیامبران در سرزمین ما آرام نخواهند گرفت
🔹
ما با متجاوزان خواهیم جنگید تا آن‌ها را از سرزمین خود بیرون کنیم و تجاوزشان را متوقف سازیم. @Farsna</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/farsna/439867" target="_blank">📅 16:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439860">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p_4Ukf2jaBbsKdzVYix2EsDsQj2Zn358t8or-nWgQKg_du1bGwfP-Qpc4P4zO0A35KlmyBYvoDPqgXQQ8vGIAqTxgl2HwLx_dBU21lUi78n17vghwYQix7MElLhQLs_fYbYa9C1cyMAiZ65T_cTyZrNhH-nfGRBdQ0I2NdFLqkog--skBUvyBZO9a0Uz1zK5PZp5ipDs3_XYNd1_leYxaUWRCKC_CcUQjyNcoeqyPEi2e52d-STQFrc8NtCsfu9xE1OdvnrrZDpajAptDS4dsfMBfsLw0LYYMvbwnu2nqB-qQPcgX5BtrQ2CSRfh0pAVA-a9-Fn5gZMnHDUmct7IAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rl_KBmDgHL8umt7vgvKu05EZBRTdj_NVUisnjb6S8PQE_2Cqx98Yf4G3gHP0y80SJb6VuaLnv4sUOIrt_Fz6GvaZO6LtYs5pICuEt4v-zpgBxs_KV-y9O5prCew1mxeWQx6tdcAle238Ugp6UiSMGvLz1Rd1V5jTAdZo_lQahVcO3kXM90Z_XKIpeCwqdzv2ES2UPEQtn2NbcAlbfcp_ZIZvt76-hoBzH5wmDhWXnMzxQsDdTyVFqg_911DxZgBX56A4MS-EJpXh4TOiNIDbcLeRdoZC-GkJ7SO59lKCmWqs0fhxH42jAcsbgk0EuFABuJxA4kAZFNhE5uajvylTbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zs-ActBU4otSR5XGVsvw8J0sglUYH06Lo8S6ux5zpvwSqM8Tn-LQ79IMew6RsgbrnKlqm57RVQs2n1CgqCMridko64dfD_dN0YjUyef4ePEXA4U_GKM7V-_jwhM94ShXkGJpByp269IMD3aM94ctMN7Q46ws7HMVnyR3ZliwaAsEbGdX84yoQKEQcbYBviWhDm4u59gQBWomSy6NPcX5tb6_D6j4sn7KXj-uArYWiOWm2IXTyTJMglU8Cl2Dr-Ubtfvtlz3EFZIfMqg_voC1K6cGFS54OdcMftitQFIJpZ9Px4LYzwn4umw9f0_EyXv8vadaoNS7o6RwzmzG1ESldw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gNdXJ0YSOLLX8v8YweXdBEQaMybOPAGg5WlGqmaeT6CXMo_z4x7tRm4GYBISzy0-S0fz2XqeJuwzVG0731m4BK1_mIme_wG9WUaWIKdYW4To2HH65dZpHwopZyq7rgWJ5z7ODvIQIM9P3HIjFOEMLMfFOCvBAcWeyrxvF8W4a6o2LXF_z721xxBkiEiT1qCra2bhTkn9uS2sSqs0U29U6A-MTPgjpQ08gzSGWYU0o2QnK12MJ7oHV8QXFGOYH9HaUe-nmV4J4ZkP-ed0zauUlX9lvIPK36WSgZ3NcZZB0KioevhTvMwI3jW2BRri79tcOoLMlp-1bpBPWGuzPHxKAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nlifdvl11um1aYKvprUimk1EJgnfw70vGwTMjOR2KKjTcMQt2fs-gRYTuP7gx8e4xSXjhlhOsjoskaJxbimMtiVnu-TrWG9j61Vlq9mFe3lDPcr3eUO36tg1gXrNrTSaZG9w7N_AhuclUxe0Dory_9oyg_DOyNzFUNehCKywluIF_t0X2ZgQrtyggmwBFPyWalNHLZItihLEYYU9Nci-iAHJimCbYC_K7TX_M0ta4NbapUitTHe4WPKwlHGmH_AHV3J9pvXVYScJJTarY-CRdhs-fRqPGTSL2ojAM_bq4zoac0pb57VyIaUQcjunOOoj9gyYO79hqO6JDwkMBIjBKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fahRevkSZLM4WrHXh9e6yYrjjP0H_QqETUjAab733fVVBqGxDJeLniADPwvbTg_AfeyNwQnqIrBH1KU8YmvQf42uv_AR2ghjkze9hPseHOXQxfNdObJezLEAN3dtDzz0aTSyFhEVEW3yWhg70vJ6dXnMx_lTwAQi0fohI46jb-lk30osj0SA09iic9KF0kel8KzfJ18oMY-p0JOX5VBR6-CdBLxGv3jGZsuWUgtCX32xrgXIBhu22TEkIlNjqIk6CscnOJ3YCcf8IS3NGV5ffzlqgOyJbE6GzgGnniZRrUnh3YQnWcgxbGXnkGCGMpsVBhamzDZidK_BNmFrryBjlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S9Wuc3MdZKfhQouhKGcK1d65xpO6mQQnb8vv17_ruGqDV_QGua4yFnK7wCiI5kv-AKxAUsjQXYZLbWnqYEF9I31opERIlgM-FCoEnozpO7Yi7uK4dw96VsKQQtkVJwr99vRyOtN1kKtGYS9t1bC9n4zFfcMmfe_9GQ-4k31KM6k5a0OnaeKJ3OUXPJz8Inhk_fuodpV8HVCK8spHv9l3_I3TW200P9Ctn49asdj1Mls9U1Ebta7aa-8Lyhe43aGMlxqi_mtMAM1fErhRQPLKIZJV964zwhDs0XVTOtLExRHiKu5qRa4q4ofq42wTWl0xLuHEgdS8kVCsvPOqglaGTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📸
ساعات اولیۀ مهمانی ۱۰ کیلومتری
عکس:
محمدمهدی دهقانی
@farsimages</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/farsna/439860" target="_blank">📅 16:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439859">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: زمانی که روستاهای ما امنیت نداشته باشند و بمباران و تخریب شوند و مردم ما کشته شوند، شهرک‌های صهیونیستی نیز امنیت نخواهند داشت
🔸
آن‌ها صلابت و شدت عمل ما را خواهند دید. @Farsna</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/farsna/439859" target="_blank">📅 15:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439858">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: تا زمانی که حملات دشمن ادامه دارد، با تمام توان با آن مقابله خواهیم کرد و هرجا که تصمیم بگیریم و بتوانیم، دشمن را هدف قرار می‌دهیم. @Farsna</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/farsna/439858" target="_blank">📅 15:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439857">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: ما به هیچ‌کس تعهدی مبنی بر عدم مقاومت در برابر تجاوز و پاسخ ندادن به حملات دشمن اسرائیلی نداده‌ایم
🔹
تا زمانی که اشغالگری وجود دارد، مقاومت ادامه دارد. @Farsna</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/farsna/439857" target="_blank">📅 15:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439856">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: از ایران سپاسگزاریم که با وجود چالش‌های بزرگ خود، به ما برای بازپس‌گیری سرزمین و حق‌مان در مواجهه با تجاوزات اسرائیل و آمریکا کمک می‌کند. @Farsna</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/farsna/439856" target="_blank">📅 15:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439855">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
دبیرکل حزب‌الله: مقاومت در لبنان از مکتب و اندیشه امام خمینی برای آزادسازی سرزمینش از دست دشمن غاصب در منطقه الهام گرفت
🔹
ما برای سرزمین و ملت خود و از روی طاعت از پروردگارمان می‌جنگیم تا بنده هیچ‌کس نباشیم و نسل‌های ما در میهن خود در کنار هم‌وطنانشان مستقل…</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/farsna/439855" target="_blank">📅 15:48 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439854">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
دبیرکل حزب‌الله: مقاومت در لبنان از مکتب و اندیشه امام خمینی برای آزادسازی سرزمینش از دست دشمن غاصب در منطقه الهام گرفت
🔹
ما برای سرزمین و ملت خود و از روی طاعت از پروردگارمان می‌جنگیم تا بنده هیچ‌کس نباشیم و نسل‌های ما در میهن خود در کنار هم‌وطنانشان مستقل زندگی کنند.
@Farsna</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/farsna/439854" target="_blank">📅 15:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439853">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e04083cc32.mp4?token=tP67_gGjF3Lf1gze9GZPHFEwfYoLomGqsxaofNUlNXLXgHybdwBQrcQG_CceKS5LGucruVa42jgDg53S_FIAngOwk9tJ8LlO4NZXYrlYMBAe3qXqa1AYZ8aeUch0Gq4RDOYr_n6L9JRJjC-HYkzEJO2IwCkkT9ulei8ttWO2DSH6yfNI3a8NunpFtL6YOpVeG5Xs5F9w5QQ5XKDkkOcIA8RaO6aonj5cMwtN2djcKuo9_Sy_iJFisMB-Agds3YmOCJv45uquWm0eKYM85j0Yjz9BUhOvO_tBR3HdDVSj3mhijB5CFZR6XWuthGrQ5WeBlipZh4qZAQBV0HShoJoCZmdumCAhXMPPUsaoL21jWp_LbGabEglVLuO--ojIBB4hhZ0EAoZytg1bSsW3loWlNvKxz3-mwLOcj9PN42mZt7Xex4HQva9d3XD3yRPkH-rBaPa4vgTRbQ7NZ3pm3x3X1RWf9x47sIrZY18ovp0K2Rh88c8GdXoa9rEjuhSba-Vmg5LBAlypWTr-0FpF0qxkJ48gx9rfXNjGpsQGHDyDtAyqdbZY_fDl4heE4-Du-Z_imr8UjORV0OB9UOVdDOxXivY9g9eoAxRdWtU-rFIGL3lYV8AlV61CQv0RF4nesoP1YjdGHzo8g6TOGlDGk343_PiwUU2ysnK7hcQR4UiPJ8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e04083cc32.mp4?token=tP67_gGjF3Lf1gze9GZPHFEwfYoLomGqsxaofNUlNXLXgHybdwBQrcQG_CceKS5LGucruVa42jgDg53S_FIAngOwk9tJ8LlO4NZXYrlYMBAe3qXqa1AYZ8aeUch0Gq4RDOYr_n6L9JRJjC-HYkzEJO2IwCkkT9ulei8ttWO2DSH6yfNI3a8NunpFtL6YOpVeG5Xs5F9w5QQ5XKDkkOcIA8RaO6aonj5cMwtN2djcKuo9_Sy_iJFisMB-Agds3YmOCJv45uquWm0eKYM85j0Yjz9BUhOvO_tBR3HdDVSj3mhijB5CFZR6XWuthGrQ5WeBlipZh4qZAQBV0HShoJoCZmdumCAhXMPPUsaoL21jWp_LbGabEglVLuO--ojIBB4hhZ0EAoZytg1bSsW3loWlNvKxz3-mwLOcj9PN42mZt7Xex4HQva9d3XD3yRPkH-rBaPa4vgTRbQ7NZ3pm3x3X1RWf9x47sIrZY18ovp0K2Rh88c8GdXoa9rEjuhSba-Vmg5LBAlypWTr-0FpF0qxkJ48gx9rfXNjGpsQGHDyDtAyqdbZY_fDl4heE4-Du-Z_imr8UjORV0OB9UOVdDOxXivY9g9eoAxRdWtU-rFIGL3lYV8AlV61CQv0RF4nesoP1YjdGHzo8g6TOGlDGk343_PiwUU2ysnK7hcQR4UiPJ8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یزلۀ ماهشهری‌ها در عید غدیر
@Farsna</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/farsna/439853" target="_blank">📅 15:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439852">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8abebd4f70.mp4?token=dJ4lzttERoyuW9CeC-H9fjslKmvR--JKmVjG9sU0JxQzp6J5qrIwRHZsytF8Cglb7M6mZKF-dv9jjKaaoD6kB2v1S87Hxu7vxc25EBuMzarbD3396PtH-8nUf7d6Mv3ysEBWBvj9cSPEVEPRjMYjmHs4eiNVnmASeHUnyOSFtE7Sd-XdMDrCPzUHmA6pFMA8fbBouuRjL2mGFwx4fTEx8OVJlFZ-r_vFUcZ4nr8azAvoZ4Swxzv0sqhLQFnR4Ifv96wOR9gHxtt8zCg1JPdQyX7WDh9m10SAHW1bww1VFnEWd8Eh6-QElAY5Cnq8o1vQ2WFlxoqgVasz8UjxOdAlCoPS3-f_2w1BmskrCKiLvpwKgXr7c5WP6a-CmavfD5_VFugYsSxvip0b-WVo9hpyOVSuF40DpJ8iBAj2S4LS9TvqE6UMmpFk2o03Dxfk5JE3A79Pt7YvH7fYlz2PIwDhhKJlp-mRzyDQuSPCGws_rgW96t8GET15bML2l1FnJOhsTx-UQqYMpRbwWOqYDqWjFPJQFDgz7UqWKzihzS4Ge60OYP0cv_8gnfeCMX4WDVXom-vHLIaMUcuD5r8YQeBJq6CHd5qn7Ge4xOeMe8wf5uOfuvtbqydtdgDRXyW-LA7ZAVpQkuc-217KPQ8T01ps39vsRKti0nLY2T1EXOk37qM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8abebd4f70.mp4?token=dJ4lzttERoyuW9CeC-H9fjslKmvR--JKmVjG9sU0JxQzp6J5qrIwRHZsytF8Cglb7M6mZKF-dv9jjKaaoD6kB2v1S87Hxu7vxc25EBuMzarbD3396PtH-8nUf7d6Mv3ysEBWBvj9cSPEVEPRjMYjmHs4eiNVnmASeHUnyOSFtE7Sd-XdMDrCPzUHmA6pFMA8fbBouuRjL2mGFwx4fTEx8OVJlFZ-r_vFUcZ4nr8azAvoZ4Swxzv0sqhLQFnR4Ifv96wOR9gHxtt8zCg1JPdQyX7WDh9m10SAHW1bww1VFnEWd8Eh6-QElAY5Cnq8o1vQ2WFlxoqgVasz8UjxOdAlCoPS3-f_2w1BmskrCKiLvpwKgXr7c5WP6a-CmavfD5_VFugYsSxvip0b-WVo9hpyOVSuF40DpJ8iBAj2S4LS9TvqE6UMmpFk2o03Dxfk5JE3A79Pt7YvH7fYlz2PIwDhhKJlp-mRzyDQuSPCGws_rgW96t8GET15bML2l1FnJOhsTx-UQqYMpRbwWOqYDqWjFPJQFDgz7UqWKzihzS4Ge60OYP0cv_8gnfeCMX4WDVXom-vHLIaMUcuD5r8YQeBJq6CHd5qn7Ge4xOeMe8wf5uOfuvtbqydtdgDRXyW-LA7ZAVpQkuc-217KPQ8T01ps39vsRKti0nLY2T1EXOk37qM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ابَرپرچم‌های بیعت با ولایت در مسیر میهمانی ده کیلومتری غدیر تهران  @Farsna</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/439852" target="_blank">📅 15:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439851">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7aGMiIuE8trWTjKm2z7XynDsvr08AhzhMHaeLj9DC1CF7UBniqQ2OshTohm4FIg8qH5o8l_Rpwo2mqHfFGNNRuxXcpnLhtoQivf1D7OyWjpY_jKCB15hP2TzHqqPVLluT2cKsfnIJc2AZDpVX0xC1gIeare6yJJteic4rOkQoSCXKLzT3y7gRLr7fBcMVFWoVcQaVGcwglkXWYr_E5O4nBBxpvw5WMI1Wjnb7s298fFHTU8x5-NM3NVjoBonUhot39v9y8dF3t_eBYH7byLow3lJDssiB_ql8vPhYrT8v428hqjtNMX-3YqNpzNPPgsTpfVsWIYFY2fDrKd_5oXGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
انتشار تصویری از رهبر شهید انقلاب به مناسبت عید سعید غدیر
@Farsna</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/farsna/439851" target="_blank">📅 15:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439850">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79fb369f7d.mp4?token=WXq4gt2Dj9lC0RdNFFN5Zj045m-2w9eMitwB7NTwDTtaf82gP-R8W2CeQXtSj0J5rb8njcjRBhw0zwpe3IsjOKh-IiXZtL4yYmvZ6hohP-jKErQ-NEn3couZVWt6IjI8OeHMCCMNo118lWVO6i9oX2fx7NxAQcbU7malbEWccXfXCcLXAccHKFLkXz7ghq_iDRd_BN81SPeZqQs3YowbfgQK7phkBso3MmxNfG1CglPb__8DLlDBDODRDVDMsRVH1cQykR0hbXotmQg-wpnjOutOLcg1uhCqBm7PekLUwSswq_yMQCxznJ3dhmoRNfkGqRpt8p69M_Jf9xQLThYOqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79fb369f7d.mp4?token=WXq4gt2Dj9lC0RdNFFN5Zj045m-2w9eMitwB7NTwDTtaf82gP-R8W2CeQXtSj0J5rb8njcjRBhw0zwpe3IsjOKh-IiXZtL4yYmvZ6hohP-jKErQ-NEn3couZVWt6IjI8OeHMCCMNo118lWVO6i9oX2fx7NxAQcbU7malbEWccXfXCcLXAccHKFLkXz7ghq_iDRd_BN81SPeZqQs3YowbfgQK7phkBso3MmxNfG1CglPb__8DLlDBDODRDVDMsRVH1cQykR0hbXotmQg-wpnjOutOLcg1uhCqBm7PekLUwSswq_yMQCxznJ3dhmoRNfkGqRpt8p69M_Jf9xQLThYOqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اسرائیلی: با حزب‌الله آتش‌بس نخواهیم کرد
🔹
آتش‌بس در لبنان یک خیال‌پردازی است. حزب‌الله از شمال رودخانه لیتانی عقب‌نشینی نخواهد کرد.
🔹
وزیر امنیت داخلی رژیم صهیونیستی با اشاره به ادامه حملات پهپادی به شمالی فلسطین اشغالی گفت: «حزب‌الله قوی‌ و قوی‌تر شده است.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/farsna/439850" target="_blank">📅 15:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439849">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/645d8440fd.mp4?token=DPeywUtlRrnUmZvep64Xsk2qtQcVcKnShNK6HhkDAod64B7g5y-sAhO40tCzEvMXegywOaEqpy2cSUxpSgEZ8_d8JkUscojDEHp7jrZc22jNLdwWednaRFBxhpily9YmCcEIxzvMwGUrTJWHmdryQgsfCiIv9BqsaV8R7MfNXLkASA-tXD72BzaIjXvKS2O-F6YsGZ1yokZ-sppeUC7tov22vZskQUqp4GGEsS_7eylpVxJEHGP1FVB5xhmftHzC3COvrEcqkwB-Y99NclPjYyQbFRB1AnShskhk3Cb6yo75IS_SPhDlOA_RcDkTxMgP-XN18O4p6qCXaB4Jp6HAc15W3gKBbCPuvFuV9qmNun1DGuBTQq5FvE-xEI--rwte585niIv6JJ_zzAxYvJalPr-vP7Cm1AyRLycUks52sw2BVaR34V2prQcukdMZgVo_byoYs8x6wzNmXSuPWqToqzUPcrmj6gCuc1ZteRCstjYOTvy3LY6hZlxiFzpQ4RMew-kaYQUHgJ6cB5n1LdXMOPtyjY5hqFP2wPrF4MW3Vz3t0O-PE9WPptRHpBLpEEJkQv2gbGc0Nc-l8JQzgnbAGjPgrVbp3OgHYfQnhgcKTCnxQCOWtmsMnWpPUICUzBis0m4FwyOt76LYdLXiYs-ZNxhYIWNSeQGbu1RglcCvAKI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/645d8440fd.mp4?token=DPeywUtlRrnUmZvep64Xsk2qtQcVcKnShNK6HhkDAod64B7g5y-sAhO40tCzEvMXegywOaEqpy2cSUxpSgEZ8_d8JkUscojDEHp7jrZc22jNLdwWednaRFBxhpily9YmCcEIxzvMwGUrTJWHmdryQgsfCiIv9BqsaV8R7MfNXLkASA-tXD72BzaIjXvKS2O-F6YsGZ1yokZ-sppeUC7tov22vZskQUqp4GGEsS_7eylpVxJEHGP1FVB5xhmftHzC3COvrEcqkwB-Y99NclPjYyQbFRB1AnShskhk3Cb6yo75IS_SPhDlOA_RcDkTxMgP-XN18O4p6qCXaB4Jp6HAc15W3gKBbCPuvFuV9qmNun1DGuBTQq5FvE-xEI--rwte585niIv6JJ_zzAxYvJalPr-vP7Cm1AyRLycUks52sw2BVaR34V2prQcukdMZgVo_byoYs8x6wzNmXSuPWqToqzUPcrmj6gCuc1ZteRCstjYOTvy3LY6hZlxiFzpQ4RMew-kaYQUHgJ6cB5n1LdXMOPtyjY5hqFP2wPrF4MW3Vz3t0O-PE9WPptRHpBLpEEJkQv2gbGc0Nc-l8JQzgnbAGjPgrVbp3OgHYfQnhgcKTCnxQCOWtmsMnWpPUICUzBis0m4FwyOt76LYdLXiYs-ZNxhYIWNSeQGbu1RglcCvAKI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع پرشور مردم اهواز در جشن بزرگ ولایت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/farsna/439849" target="_blank">📅 15:06 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439848">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d8f7f6d83.mp4?token=DdRw5-qwzSUXjsvLANXZQTOwF7Kj444PnvtXcoHYvzS0PAwp-gw3_wj32l7-s5j8D0UcjXGHNP5-iEFuwwvIJZCqqH-tAnurwsNnnxdOEi92IDDU1qDJA8jyCeg3w2rnJ3AogslBKJuO85QtcTUy5xVxZ3UtFhf0o4_RI2xMD_u8Uo9DRfvchqkBz21n6plKHyQX1i86Y_UgtsCn20SOHXW2jJZD54DLFOEjwwz_st-uT8uIXNCUzBbNguxY8VugAAF-vjudoo_Nb2GO5bYxCyt34vg4reX5opYdLgnhPVr_l0pr5rc4mv6kM2FO7JeN8ztqCJmI-6Qz9IwTw_HiCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d8f7f6d83.mp4?token=DdRw5-qwzSUXjsvLANXZQTOwF7Kj444PnvtXcoHYvzS0PAwp-gw3_wj32l7-s5j8D0UcjXGHNP5-iEFuwwvIJZCqqH-tAnurwsNnnxdOEi92IDDU1qDJA8jyCeg3w2rnJ3AogslBKJuO85QtcTUy5xVxZ3UtFhf0o4_RI2xMD_u8Uo9DRfvchqkBz21n6plKHyQX1i86Y_UgtsCn20SOHXW2jJZD54DLFOEjwwz_st-uT8uIXNCUzBbNguxY8VugAAF-vjudoo_Nb2GO5bYxCyt34vg4reX5opYdLgnhPVr_l0pr5rc4mv6kM2FO7JeN8ztqCJmI-6Qz9IwTw_HiCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنان علی لاریجانی درباره شهدا، یک‌سال قبل از شهادت
@Farsna</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/farsna/439848" target="_blank">📅 15:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439847">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hma5STNFzTL1pbMaxfmZ4NKL6iZCbtUO0w-urmRXuRB_RN_Op2Ga7kQur4NUCJyADwp3cbv1S6uPpHwdFoi2cq9YOWImqJTCNHUviSMykL8RcijQ21YO8RMjTyXGhc0sO6TWGrq1DU25HWg03Ufp-4hmjhWxyKDBNC2PDCNaanontnb1SG03LnGDvYvNNN7yyfybpxkPAju4m-fTZuApkYhMWay3tvckZANF7syAMmiN4QLiyJLe9X-lRvL_6mQ4UZn9TZslKFjE4WUmi5anGwC29G3G86IkPoC_HgrcoiEEG4zWU9i6_UIAXyxevDBwW4W4SmvcylRIWgGsxzHBtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بطری آب در جام جهانی ممنوع شد
🔹
فیفا در آستانه آغاز جام جهانی ۲۰۲۶، ورود بطری‌های آب چند بار مصرف را به‌تمامی ورزشگاه‌های این رقابت‌ها ممنوع کرد؛ این نهاد پیش‌تر اجازه ورود بطری‌های پلاستیکی شفاف و خالی را داده بود، اما با اصلاح آیین‌نامه ورزشگاه‌ها، این مجوز لغو شد.
🔹
دلیل این تصمیم مسائل امنیتی و جلوگیری از خطر آسیب‌دیدگی ناشی از پرتاب بطری‌ها و سایر اشیا به داخل زمین یا سکوها عنوان شده است. همچنین ورود اقلامی مانند قوطی، لیوان و شیشه نیز ممنوع خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farsna/439847" target="_blank">📅 14:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439840">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mfbHqB2M0ODBZxjtXN7XM31-w78GDr2tzk5A5wGH4gOuRcynq1z3QNzxCDxHMGObOr_XrZzOs4WRouc7Vs9Yy5bmD--0OTmlRQ6BApBbqvpsLDvzR-8MbUh-P-zO4a9kJrygr7T2sicZXVrgjKEPBQB1A2fdNsDpi3B1EqtZpBTsoweZ_N2XrD0IMEhSoFTrqd9n9A3gBlCREC8KV8_wpsinsKO5vroPa4DKJETH3-mIMyPzU6QlWn7lDosDQ25V8Iy3W0k8lf8Ft3mhnNJKapmbDuYr0nk5L3NzHoNUHP-u-8EWqNgvXBdCnIfrZT0Akjf8HVN_S-CJJ6K6Al_V4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oRipd5Tm2_DvXK3z-Dka0rpjK96AekXKRt0CINh4aMVA9PU--HqNVrWYZ1qGoFZJGMkpvrIRI1crR2rejSV-A9f-p4R9VnZFzgt_WowcUysD9R1lJgbLHPt7PBRShFZVMKjsAKbV0uEXwYt-IE41itEtuaUZk7KsYQruCJ8Dknao_K-c7jhcSzJmv88of9InIQox1DCoUYiU5f2-IlzrRYgfr1xLuG8mC1EI_lNv8-X6krV0s2HT22mx6fqUoMHzjBEpBnkqSluxV30jYU4nlgEBTg4b89qFmUkLZUSggchmJ94gicK6k7m5kpsDI7egd733lx_5qjxTXwHx6GtaFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LtDE1zpYyaXOrg6vsy3SX-GU2hXREIuVOqZODqNWuO7T1e__kJiCAg2uC1_TdRC9yUpy6vcBsa3Ew27bEUifhmQBSM6pex0jf58fpeuclPwg0rxqhaeyIfoGpc_dLQ_sLxOLeT1kr1fhy_iFf8vOtvI5tZz6VUwaHqJOCjCNgSqRu3es1o5qKXJdopz-n9WZCJZbxJ7nwxD_eNeGOxnMSJdmnrNFqnoBonQWr2qjJBWoT437VmzXT4NqWk0wGKxxjlnR1Lag1p7EpWq-yKzVvGSufwoqaw5pBnJZfRKsMtcC_VexLqo_fGymN3gNlS0KJV1BtJ-LNj9pmVtxEHsD5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OlfWuqVhkp5ZlL0GozuPAw7IhTIZTiU0-mI6KZrPw4Jr3LsLwEDE4JyARFQ4rDdrCG0VLbO_ZjXFPyZBG498O1DaIFb8FY6NI8GJ3obi2QzcC_h0YClj-MN0Fv7uho16UdM4j6BpxOzdup6qfm-tRfhC9IG2i2bauHbFPqm1Jgn-AJB_H439qz1WcJPuBeEvxr-9ln0Of2M0tRkTmn9rcCeimz_WJHuWd5gYlzKh_oIXiab8p_l1zo2Tp6CRuoHbs7EGIDLuJFkysVJeUFno5Lzmkiqn6yFLqdhcPkqc7sE7HmDPKxpJzeYi7Krw8m3AZXk9UEATTEuPtO5jSjh-lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GGeXMQTWl5JLjH1qAuj71oR6Gvu39JCZBU59jnb6rM9DYehq-qIftocQoxWZh-ke1ihyBSPfLedIPC8ubmifzJqoMEjXlv1nlqDrnq-2Wy_CHeXMDk5DvZWkkxcoiR_2m1QgJJW0H891RzwCfCMOrxySnqzxN3vIovz8tjRn3IjoPOWBR_8aZxtC0JcsPWAfaHkqzq5Zy6T_KL88uEbiA8pKiIIYkvr815b_IVrl8X4ab7S-45VVjK8vpNH0uXx54_-tnhdkv3xMrH6kPFcMuCZsiwyvmWxY91PO4Ud9BETDYnO8pJqk6AwhIgmAo4UINJqBIQIvSFh_EXTAg8bwKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/siWKiDWgrtWVwxqPXrFcysWoZUVKUYREhT-CDRjilm2UdMNT41a_9HGlymdvclddn-F8Iomz0apnzvnZfOgw7srVnLtesHqCD959DUtHY1C9v6fXf0nKz40HtoyrMG-m1DEqIRonScPv7Jc8vpF2pVhD0if9aOzS4ijO_jZCLvdDmF_WelDlSMB4EwMiX3Ny1XugOma5LyV7CNzkq4kExRx2aIkMbFDZNl_EX0q3XCJ4WZFURpa1Ge5h7ffogHFDYR2UrkvENhjHfZGomtAAE1i9ovIRhR-kl6r8YVOBrrqHSmJhzOZQX42eGs83zxx-86UaONINhRRfxjtdcFnbbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XxrVy32pFIZf0FNBq5iC-bTRtpbLFMuTZ7hm61vQpe-8ConS7vvWygSJVETLD1tYTsfad39zno6x5adPVaCRuROy6eKo0rthR_6eaIa9IXFVZbE1eoAxBhaoylFDizPEDw_eytAxx8zebCFs1MCBA2yQyas_7I92lOMh81n_Qd_QWYZ3W_6CRJoai4ApzoVURxarOmlAkIRbWPmVQa7I4lxub3VhIRUSlXpsHYMYpQbn_RsMN0VKoNuYQejMZrzuvMBAVjXf5HSyLRzzCSjB0Pv4fI52NY2XUMsP_TT5qaZvvoKXlSUV_ahgUwCt2sTsUvec8SNRS3gMAUgEz-HiOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
زیر سایۀ حیدر کرار
عکاس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/439840" target="_blank">📅 14:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439839">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سردار محبی: شناخت عملیاتی نیروهای مسلح از دشمن در جنگ تحمیلی سوم افزایش یافته
🔹
یکی از مهم‌ترین دستاوردهای میدانی جنگ تحمیلی سوم، افزایش شناخت عملیاتی نیروهای مسلح از دشمن است.
🔹
اگر در گذشته بخشی از شناخت ما نسبت به توانمندی‌ها و تجهیزات دشمن مبتنی‌بر اطلاعات…</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/439839" target="_blank">📅 14:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439838">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/051dd5187b.mp4?token=NyHFx9TKBf8NsMobrYkTtEX2iwHJeXw2R-e2sLnjY4_jneZcBU8t5AVDh5g3Fv9kSCqYYU7hF9XKf1a1-ktvprLdb3gLDRjtHiDaWs26vWRk_gGGx5XnkqKjQ_GW7xnTNk3nfAtg5W2C92sAVXZHGBNFlWDsKu4aiRQUHSmNWiD7E9pT_323ZJyoNUqcLj0Oy9X8KsKhACkJRBUpAegWQ31_6z0AqChFabdFMSMvayEq5u0PqYxogzUCvV9PLDgeZyztW8ou8LpdCR9o37T5yQJto6w2zthmSm8f3vOxhdDJD9iUIUxRrzdIYmh-40i9zXeKGg9XWo1BhaHzcRWkUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/051dd5187b.mp4?token=NyHFx9TKBf8NsMobrYkTtEX2iwHJeXw2R-e2sLnjY4_jneZcBU8t5AVDh5g3Fv9kSCqYYU7hF9XKf1a1-ktvprLdb3gLDRjtHiDaWs26vWRk_gGGx5XnkqKjQ_GW7xnTNk3nfAtg5W2C92sAVXZHGBNFlWDsKu4aiRQUHSmNWiD7E9pT_323ZJyoNUqcLj0Oy9X8KsKhACkJRBUpAegWQ31_6z0AqChFabdFMSMvayEq5u0PqYxogzUCvV9PLDgeZyztW8ou8LpdCR9o37T5yQJto6w2zthmSm8f3vOxhdDJD9iUIUxRrzdIYmh-40i9zXeKGg9XWo1BhaHzcRWkUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آماده‌سازی موکب‌ها یک ساعت مانده به آغاز میهمانی ۱۰ کیلومتری غدیر تهران
@Farsna</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/farsna/439838" target="_blank">📅 14:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439837">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i73QqLz1Nrc7mAQqIJ0KjR7-AHocSf2vBhla612A1Ssr07bLPhluuElgHStPMXNi3PMT-o5sNvU2nQG5o7ICWbHYU6HZN-cj1-rhrvHfxVayfm3tCb4bQIkDKbc7aZS1DrAUkU40n7x8TU7hwRHLsHPNRswv4HwI-FZQL3uZowmzpVcgeVaebdjto1pZj3IGIzu3DHDK1vm1rMX9Ao0uNPL1U9EDDXvodGX0EXG8061BO4-tQ9dJVKnZKpxuzZILuDR1s0tR2U7zY0Pw8FGetCoJK4yJHKX9kvTaEkVCFaS5Lr0rSTalJkB3UTmJybtWHznf4OqmUdzRi1aQyyZ4TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمدی اولین فرنگی‌کار طلایی ایران در مغولستان شد
🔹
پیام احمدی فرنگی‌کار ۵۵ کیلوگرم کشورمان در رقابت‌های رنکینگ جهانی مغولستان صاحب مدال طلا شد.
🔸
دانیال سهرابی و محمدجواد رضایی نیز در ۷۲ کیلوگرم راهی فینال شدند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/farsna/439837" target="_blank">📅 14:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439836">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dccdd6099.mp4?token=MwiSDGvL68k-8gt61jpQmJvA5WNpmY2lVlvkp7elKR_qCQHx7ZQJZSd4C-eF6bk2cVVWnJUwKync5BHH7ZNnPGpCLJgZ311YyhOwDjyK4JLUqNe8LcTloEMUekB4XA0mCP7eDMdhZ1FWBh0V1rY8dGFiAlsBRloZM0yEAh364zMHHR534MQh-aWZHunD8Q9FhTkFuYhnprMtumK40xmYKtrXmeRK6WV9p8RSdwhwteiRuTAheAv9NbtukNT5D7MmbdPirIAuXyu04K67gXVTxZjBUybgrjOfKvmt9aeugMpZOn2Fbum3HqCNFzsFb045CpQ-K9huj7M1BWwwOugYqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dccdd6099.mp4?token=MwiSDGvL68k-8gt61jpQmJvA5WNpmY2lVlvkp7elKR_qCQHx7ZQJZSd4C-eF6bk2cVVWnJUwKync5BHH7ZNnPGpCLJgZ311YyhOwDjyK4JLUqNe8LcTloEMUekB4XA0mCP7eDMdhZ1FWBh0V1rY8dGFiAlsBRloZM0yEAh364zMHHR534MQh-aWZHunD8Q9FhTkFuYhnprMtumK40xmYKtrXmeRK6WV9p8RSdwhwteiRuTAheAv9NbtukNT5D7MmbdPirIAuXyu04K67gXVTxZjBUybgrjOfKvmt9aeugMpZOn2Fbum3HqCNFzsFb045CpQ-K9huj7M1BWwwOugYqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رضا پهلوی هم «ساواک» را گردن نگرفت!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/439836" target="_blank">📅 13:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439835">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5LKSzrdujVFEQD2mAp4tXvc-lbvvH3dbyGm-lPZKyOScO51qHnBy3AuTJWPdWxlBckPYbHXfeQ7nBDEZRR_3nLHVUs6I_OCMV1lW0G9USERlSHeKBkm_p3sM2bDvXIFnL_x3-Wy46dGVjwdtN0BjrA3ZDvSMeTca53yN0y1ZcxAEroyjc_ewb0N8yoBOudOt5MEuUQkkpL7qTeNQJdgRWJN1VQGsZLSJ1lfK-r3nwIF9F07vrEGgHRwcpjhpuk02mQGI8T34TTFu1n54-rlEfvaecwKZ_dghjCXL6vzt463HjIMDVfo-A3gEAiJnzhxfh__vdDlJOJQt9YaX3dCpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار قاآنی: اسرائیل باید به نقطه قبل از شروع جنگ ۴۰ روزه عقب‌نشینی کند
🔹
پشتیبانی از مقاومت در لبنان، وظیفه همه ما و اسرائیل‌زدایی از منطقه، آرمان دست یافتنی مسلمانان است؛ مجاهدین لبنانی، به زودی نتایج مقاومت شجاعانه خود را خواهند دید.
@Farsna</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/439835" target="_blank">📅 13:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439834">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‌ بازنشستگان تأمین اجتماعی امیدوار به جلسه با عارف
🔹
پنجکی، عضو هیئت‌مدیرۀ کانون عالی کارگران بازنشسته تأمین اجتماعی: در احکام اعلام‌شدۀ احکام بازنشستگان تأمین اجتماعی گفته شده ۱۵ مورد باید انجام شود، اما هنوز نگرانی‌هایی دربارۀ نحوه اجرا و پرداخت وجود دارد.…</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/439834" target="_blank">📅 13:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439833">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">۲ عضو شورای شهر ایلام با دستور مقام قضایی بازداشت شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/439833" target="_blank">📅 13:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439832">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbSSbhJbQr7_RtM29NdtVFNRNXTxpxOcpsUi2tJp9NePtHSQZjuLQWfNd2KSRoG-VgPtK4jdnZl2LsoaazbKS4kMXFpA1cZAHb_Ea9zn5kO6XyQVVhYeZ4c_B5nYZHiuO3QTwSAJ5s1HGP04WTwl4BD0u_iyBYQwEQbtttC8PPgoWZl4QHJRg_T9zMdrdVFJ85PAmdlKSH0oszL-Wr8LhdSo9nmlaDjXs3mzgYtOFS_birLuMvptJo1BSOxUTPMhuQyjZjSWpk0gGYSv33bJ_5K58GiJ1yNhiDiYZ0UOrD3Na3R2Jh7bt0oQgnqp3H-_19kY8qqmPHkRmM27uRyLwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراق در سوگ آیت‌الله فیاض ۳ روز عزای عمومی اعلام کرد
🔹
در پی درگذشت مرجع تشیع آیت‌الله شیخ محمد اسحاق فیاض در عراق، دولت این کشور، سه روز عزای عمومی اعلام کرد.
🔹
در پی این ضایعه، «نزار آمیدی» رئیس‌جمهور و علی الزیدی نخست‌وزیر عراق  با صدور پیامهایی جداگانه،…</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/439832" target="_blank">📅 13:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439831">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7b0549ed4.mp4?token=KTeZuNBZs1szd5Zkc3HJ5Uua0DdD5E4gW7ZKde_CTQMQ69UbWwRqZmGK6hPu2yCoOuPH6Hl_FGEA1m0lkDqmlAF1RxADIn5XRTXsxFPHipM-2PEpIvazLfGIE1MQRvQkiBUhbqduwm9fFN7adyRiiEMC6sf-8EZ3Tdf1zQb6F8Ec9WPcsYVYWdWaF4wDrxygnBEuFgyw5e76pxTJmTsSHNv4xSi0HXcK_QmVsxmQ_5TGt7KgeFBKeN_PJ_RrBJjvMnJ3idV0UpvtqxQdpJHYkz9wR3Bq6qvSnCT5ofrFu5FSP1vie4N97fkTxooeZfGxoCghfxlPtM_tDbsPF2n4TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7b0549ed4.mp4?token=KTeZuNBZs1szd5Zkc3HJ5Uua0DdD5E4gW7ZKde_CTQMQ69UbWwRqZmGK6hPu2yCoOuPH6Hl_FGEA1m0lkDqmlAF1RxADIn5XRTXsxFPHipM-2PEpIvazLfGIE1MQRvQkiBUhbqduwm9fFN7adyRiiEMC6sf-8EZ3Tdf1zQb6F8Ec9WPcsYVYWdWaF4wDrxygnBEuFgyw5e76pxTJmTsSHNv4xSi0HXcK_QmVsxmQ_5TGt7KgeFBKeN_PJ_RrBJjvMnJ3idV0UpvtqxQdpJHYkz9wR3Bq6qvSnCT5ofrFu5FSP1vie4N97fkTxooeZfGxoCghfxlPtM_tDbsPF2n4TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پخت کیک ۲ هزار متری جشن عید غدیر در حرم امیرالمومنین(ع)
@Farsna</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/439831" target="_blank">📅 13:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439830">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dfa54eac8.mp4?token=szPH9YM7umHPm93iriwnWSLboEaL_tPmvBAvN8ysTQKw8WZ8ZKbslbzdCjEcbDBW3RNxTrTsPTYUFUs4gDDyt_HybxoyixC3Vgfe35hk0DY7bYNLzs_sa01Rq4-mEtE7lZQOaCUgI584rr5ZvAuTFtHgn8Y7PPzSBZ3W09K7FJtJtQe_hbZCR551KyUc25oP71iRFNvThIlvDorGR_kqqDqyoZbI6pf804s7o0tW55bmnQqLcJOAUSvwC_E9bN1BdfkRF-w74bbB4A9pvm1AOcWLl2aI1XU0ye4zx7zlKkrfIBhgYU6xC2YFjyuduY2VN2BBMI6sWc1kqs1c8yndL200MwcfoarEQUFnbd7GhtR1s9kkYobQ7kknZlmsyisCkmHtk_tXDI2cCrM9QAaNuGZ2jmpQ6LvR_dbdYvooUcdG5klPcauIWJyx15A4mIxaFgv8uZVkydzzQNrycwo2KoERmeuLhD_EAJxCsAoz6omFDKGo4DEk6XLacsf29qg7Ijz4VaQI4KGjR7RJy3-p3WaJXorqQTbjWESMzNDALUpLfwRj_bCvs85C9wGGn9SvcTdUIY-ASLIU00ZkrdChlagYikCf4XJdT4rCg-Z6m6Wca-sPQRD2QBUxYdtfuLjqAaNzFJ9XdMoeN8iVoMEv02GH4j4RBtXMSE1saG8bxPk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dfa54eac8.mp4?token=szPH9YM7umHPm93iriwnWSLboEaL_tPmvBAvN8ysTQKw8WZ8ZKbslbzdCjEcbDBW3RNxTrTsPTYUFUs4gDDyt_HybxoyixC3Vgfe35hk0DY7bYNLzs_sa01Rq4-mEtE7lZQOaCUgI584rr5ZvAuTFtHgn8Y7PPzSBZ3W09K7FJtJtQe_hbZCR551KyUc25oP71iRFNvThIlvDorGR_kqqDqyoZbI6pf804s7o0tW55bmnQqLcJOAUSvwC_E9bN1BdfkRF-w74bbB4A9pvm1AOcWLl2aI1XU0ye4zx7zlKkrfIBhgYU6xC2YFjyuduY2VN2BBMI6sWc1kqs1c8yndL200MwcfoarEQUFnbd7GhtR1s9kkYobQ7kknZlmsyisCkmHtk_tXDI2cCrM9QAaNuGZ2jmpQ6LvR_dbdYvooUcdG5klPcauIWJyx15A4mIxaFgv8uZVkydzzQNrycwo2KoERmeuLhD_EAJxCsAoz6omFDKGo4DEk6XLacsf29qg7Ijz4VaQI4KGjR7RJy3-p3WaJXorqQTbjWESMzNDALUpLfwRj_bCvs85C9wGGn9SvcTdUIY-ASLIU00ZkrdChlagYikCf4XJdT4rCg-Z6m6Wca-sPQRD2QBUxYdtfuLjqAaNzFJ9XdMoeN8iVoMEv02GH4j4RBtXMSE1saG8bxPk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهیدی که از روز ۱۴ خرداد ۱۳۶۸ رهبر ما شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/farsna/439830" target="_blank">📅 12:52 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439829">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ویزای اول برای تیم‌ملی صادر شد
🔹
رسانه‌های ترکیه اعلام کردند که ویزای کلیه اعضای تیم ملی فوتبال ایران برای سفر به مکزیک صادر و تحویل سفارت ایران در آنکارا شده است.
🔸
علی‌رغم صدور ویزای مکزیک و هماهنگی سفر تیم‌ملی به این کشور اما هنوز روادید آمریکا داده نشده…</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/farsna/439829" target="_blank">📅 12:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439828">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🎥
حجت‌الاسلام قمی: امیرالمؤمنین بالاترین مصداق کلام امام(ره) است که «هرکه به‌قدرت لایزال متصل شود قدرتمند است»
@Farsna</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/439828" target="_blank">📅 12:38 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439823">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QQgeclq_O3BwfOjksjv1CV-khiPIaR0V1hEv33-ZVgM5iZXpxrkl9NOk9XUSyXQBdn2pSn19xJupbqCwqadn3iNYGJaCyka1lSHA-JiVQoLsKf8hFtQfjVH8HVlmMbcrD9Wtvy_vYJIw_Hc5Ct-zim9dFjh9dHuNPF7sbo9G08FhyNT0ApcxEJ2KH8nbgXQyLX1E8l_Q_ew59yHkvLqVp3aKPdUB3iUqYRQDiT2VDmj252sKQCOF0K-Bi4gCgstNStHQvdn1qXp4RDXrQPHkqEmQVsYfa7xxnzt6uG80ZwiSf--WTmv-axdoyruRLlG2Y6poqtPIZHYPlAxkFKCduw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d_kNz7F-bIfzQU5kFLnu54v7L76ShtJkaj7KLQ5D8Ct9trm-pwi_x7P_Y7LSeno9K7_5dqaRmve4iIihAuZ6AYEUO7EG_qLzhYdySO6muSsbdrFmW12tv3f83warkd7W2Oy2ujW_U6eiV1EWMg38ABCTnoExzt4gj13fLQXGvGq6MnDPdRxY3S2gbQ5HPghRdJBtMBI9id1h2_yp_ZZispKpc0kpYSNeDtjpO2RfOGUdZ0-7nUrGlSBS68Ri1UlRMK-Tq-BiMf8RRm3Z1fOoQM_KSDX7SGBQevZwh04zCkJ-p87x8yv2xLEahq-iMgylfP-bySc-_FErRZFRRPuTxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rYuodx6HF90gi5DaP1YDTLWNVFitrRhE7nrB2K-nHfBI5z_17a5zWibrQj_hXogXQmxalkNdMgWyoMX6_18e5DGrJpIQw5MkFBswyxPwrmAlzOfkFkRKAyj8oF42M5lNB0tpEkS25LUfHvXdagcrmfwW8FfqaF6tU9rTkQ5XbO39h5z5nfdRzRwzj8CembH2aVd4ivQ32lWiJIv24LJWQPiKqK8Uyox7nDOZLmVxNoa62e3iI5IPJrcVYSiBwFo7ctQAjcv3ynWyJd6AhSF7xiyqYO7j9VU6Pow4OyjXzTZE_aFdCMmvyXpVy8bcWaFmrldz-yctULarft9gPZ9-sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sNn67JB8gDaRKzdfAVzbJwyRNPmf4ZokJigbKDJsVAC_adRKaqy8PogpQc9SRrxxjjv1-p8z4lxcz5anddtOpE36CJnW7SInpErPgYVv0mUVDOB4RmsFZxYpoeRHzWbv5AvmxvsodwwLEuzr3ijbxO3TfUxUhlBQrFOUsM5pPYwPn1r5K2RNIgbLooR6iaTEZXwHonORcoQ8Q9tTVq0LrH66H1habhrSFVI2tK_oDfKiw5kdWZoq-PKZY8VsAdE_R6pk8nHEvq5Z5TL2JNzs9soNJi9V4iKCAmigsGq2sUotnuCsrsu8kE6Zhzg49Yu7rPABixONv8TQDU0Y-anZQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vL5YIIL4Ppp5c2x2mGgjj8e-zoKV_Ogro7Mo67NhvjWG2a7LkBVbWr3ecoBX0PQ1Ma7WDSZjIv-m_L22wi7O5csug1iTg_bxm3OGdKAMsXWzW-VG-C2fqp20WH5RpbdfazSOk0uErtqG12KozOJ6avbmS94m6YJA5ECiiD-qd_WpE7-DQOXqlMgQERrq7LWSybfaqa3NAVF91CRkxGW0UROE-5nQTQJuBRKAjTgS5U2zgGZHDkCQSXsyMLK02h6XKq5XZSFXqClEzYduisP23N8TeKWiQIifPvbI1T7JC9qHkS9oLiCJzHZiC7rsGfDkVVQWWl6es_2LPItpv0J1UQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عمامه‌گذاری طلاب در روز عید غدیر
عکس:
حسین شاه بداغی
@Farsna</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/439823" target="_blank">📅 12:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439822">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🎥
تجدید میثاق مردم مرزنشین آستارا با آرمان‌های امام راحل
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/439822" target="_blank">📅 12:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439821">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">دستگیری عاملان شهادت مأمور کلانتری باغ‌فیض
🔹
فرماندهی انتظامی تهران: در پی شهادت یکی از مأموران گشت کلانتری ۱۴۰ باغ‌فیض در شب گذشته عملیاتی برای دستگیری عاملان این جنایت آغاز شد.
🔹
مخفیگاه متهمان متواری شناسایی و  هر ۳ متهم حاضر در صحنه جنایت در محل اختفای خود دستگیر شدند؛ متهمان در تحقیقات اولیه به ارتکاب قتل با سلاح گرم اعتراف کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/439821" target="_blank">📅 12:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439820">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0221fca49f.mp4?token=BnbHFz40ujLWMqLIqGyl46TOxn86XoFj8kHUGZ58rkNM4qDH0GlSOTJYTXlwExZ1KpQJDULU0CSgO2JRA0kmSfrRmj8jnlByOqkNmvTTgFWoazLN8wrl-eEJch99Vyjo-PhE_hXcxef6X_9YI7B3u3BrZyFiIc_y663qgz3HyOOMnIYORKrzYq1pNJ5qqAmq6fTp3MXeM_JZD4slBom65-qyh5PRjC-83hLEKu4EQcvpWhj2K4xUoo1vJwxnpMLtBA5ZI4djpJ9IjmYd66egGwK-8V0plt4JsAlqewfdO2xgfV5YpEmVpdEV1eqBATx4nWmN7cRdCMQs4TNAhZc2Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0221fca49f.mp4?token=BnbHFz40ujLWMqLIqGyl46TOxn86XoFj8kHUGZ58rkNM4qDH0GlSOTJYTXlwExZ1KpQJDULU0CSgO2JRA0kmSfrRmj8jnlByOqkNmvTTgFWoazLN8wrl-eEJch99Vyjo-PhE_hXcxef6X_9YI7B3u3BrZyFiIc_y663qgz3HyOOMnIYORKrzYq1pNJ5qqAmq6fTp3MXeM_JZD4slBom65-qyh5PRjC-83hLEKu4EQcvpWhj2K4xUoo1vJwxnpMLtBA5ZI4djpJ9IjmYd66egGwK-8V0plt4JsAlqewfdO2xgfV5YpEmVpdEV1eqBATx4nWmN7cRdCMQs4TNAhZc2Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حمله مرگبار آمریکا به یک قایق دیگر در اقیانوس آرام
🔹
ارتش آمریکا در ادامه حملات مرگبار خود به قایق‌ها در اقیانوس آرام به بهانه مبارزه با کارتل‌های مواد مخدر، به یک قایق در شرق اقیانوس آرام حمله کرد و سه نفر کشته شدند.
🔹
در بیانیه فرماندهی جنوبی آمریکا در…</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/439820" target="_blank">📅 12:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439819">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17981bcf63.mp4?token=OwBGi--sqp075GwJfekijJw9G2LIVK5gatCu4OnFmcNJ38WgR-n46vn0LlGTYcNALpdKDIepOPF4hWuI6C0dWWk5RmCtblHnzyByOARwhcfRJBvtEjO30dz2WRJJUel1J2JU7REwPHmPK-p3AXzx833yzdTnJhlnoBexQgzD_u3gMzXjJfWPd8ZSm810jMkUKblAqqOOv4_xrNy55FpU6onoaQTBFOFL7DUBxOLSITsNEUnL3J_wAS8ngk8GiVRt9lvPsn85Bl3uRPfNpflKZ3uJBTWFxvqvZssJUnPBCnI6SkQ9ZtWOU5plfnk-6OdXjWUCUYg96-IH4PlgTJo9M4M9AdEVfi2q0c-CYTrugvtHUlLgDP2fvBrXdlAmLgu7IwMGgmrZ8-R6nPleTNkQyMfGWjFfu70Ua1bumiHCGnLY9_tKS6cJrwLZoGM1TmLBAv2hq_Bnb-vIWxVYB_FbURHvNQY2wivDS0A4Ap6XK1lupPRduw5atuLfaAyh1G2pHbTt8Z7-msIl2dmIDguC44JWFnPRLorN8d3Pw9bOL9F8KU41zNxNgjayWttP4E3N7AnMocPEvgEjSso_Oh5eh_rEMkBS5R8IkQua7K8QEpZptSM6uHMhMHfhmUgFP8mkK-X_qcU9R8k87nAXS6HX7HX8F1EC6DTIUuEgC6FHplE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17981bcf63.mp4?token=OwBGi--sqp075GwJfekijJw9G2LIVK5gatCu4OnFmcNJ38WgR-n46vn0LlGTYcNALpdKDIepOPF4hWuI6C0dWWk5RmCtblHnzyByOARwhcfRJBvtEjO30dz2WRJJUel1J2JU7REwPHmPK-p3AXzx833yzdTnJhlnoBexQgzD_u3gMzXjJfWPd8ZSm810jMkUKblAqqOOv4_xrNy55FpU6onoaQTBFOFL7DUBxOLSITsNEUnL3J_wAS8ngk8GiVRt9lvPsn85Bl3uRPfNpflKZ3uJBTWFxvqvZssJUnPBCnI6SkQ9ZtWOU5plfnk-6OdXjWUCUYg96-IH4PlgTJo9M4M9AdEVfi2q0c-CYTrugvtHUlLgDP2fvBrXdlAmLgu7IwMGgmrZ8-R6nPleTNkQyMfGWjFfu70Ua1bumiHCGnLY9_tKS6cJrwLZoGM1TmLBAv2hq_Bnb-vIWxVYB_FbURHvNQY2wivDS0A4Ap6XK1lupPRduw5atuLfaAyh1G2pHbTt8Z7-msIl2dmIDguC44JWFnPRLorN8d3Pw9bOL9F8KU41zNxNgjayWttP4E3N7AnMocPEvgEjSso_Oh5eh_rEMkBS5R8IkQua7K8QEpZptSM6uHMhMHfhmUgFP8mkK-X_qcU9R8k87nAXS6HX7HX8F1EC6DTIUuEgC6FHplE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مداحی حسین طاهری در حرم امام خمینی(ره)
@Farsna</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/farsna/439819" target="_blank">📅 12:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439818">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‌ رهبر انقلاب: دشمن خبیث در مصاف با نیروهای مسلح ایران دچار شکست شده است
🔹
به ملت عزیز عرض می‌کنم دشمن خبیث حالا که در مصاف با فرزندان دلاور شما در نیروهای مسلح دچار شکست شده و به خصوص خاطر مواجهه با ضربه قاطع چه در نبرد نظامی و چه در میدان و خیابان تحقیری…</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/439818" target="_blank">📅 11:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439817">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">متن_کامل_پیام_حضرت_آیت‌الله_سیدمجتبی_خامنه‌ای_رهبر_انقلاب_اسلامی.pdf</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/439817" target="_blank">📅 11:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439815">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">متن_کامل_پیام_حضرت_آیت‌الله_سیدمجتبی_خامنه‌ای_رهبر_انقلاب_اسلامی.pdf</div>
  <div class="tg-doc-extra">785.8 KB</div>
</div>
<a href="https://t.me/farsna/439815" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎥
رهبر انقلاب: از خداوند متعال پیروزی نهایی ملت بعثت‌یافته را مسئلت می‌کنم.   قرائت پیام رهبر انقلاب به‌مناسبت سی‌وهفتمین سالگرد ارتحال امام خمینی(ره) @Farsna</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/439815" target="_blank">📅 11:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439814">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04aafbfb01.mp4?token=QSYCE0TxnmkWpG_Xtx5OOIu2AfyQnSFRgQVpFsM41hNU4FliomGjcx25z7w-ns2G8ap6mhOqGLl8SBAQ3B-F5gfeyei9XtpKOtDaA_3Dv8vcR9DpcyIfSkFjMotoUbLaX1_9Yh-YVYmIhPNyYlduZi1GHeB4EqoDRa9gP6syai6mxvoAXKETbgO7JeniA2YvdlyZzK16h2aT0fIvY4mqeEQp4Oxd6UwiRJ0_Bf88S9MOHtMOCqkadUG0NADfzz5flFtP_UxXADf0WUxaYZq47ppmOySklO9dW2VzYykPat53Pm8F9m6FEZRYrr4wJiaoz-rOISKlcGvVDkR80rOrsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04aafbfb01.mp4?token=QSYCE0TxnmkWpG_Xtx5OOIu2AfyQnSFRgQVpFsM41hNU4FliomGjcx25z7w-ns2G8ap6mhOqGLl8SBAQ3B-F5gfeyei9XtpKOtDaA_3Dv8vcR9DpcyIfSkFjMotoUbLaX1_9Yh-YVYmIhPNyYlduZi1GHeB4EqoDRa9gP6syai6mxvoAXKETbgO7JeniA2YvdlyZzK16h2aT0fIvY4mqeEQp4Oxd6UwiRJ0_Bf88S9MOHtMOCqkadUG0NADfzz5flFtP_UxXADf0WUxaYZq47ppmOySklO9dW2VzYykPat53Pm8F9m6FEZRYrr4wJiaoz-rOISKlcGvVDkR80rOrsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر انقلاب: همگان با ایستادگی، روشن‌بینی و حفظ وحدت و اعتماد متقابل و هم‌صدایی‌نکردن با دشمن، نقشه او را خنثی نمایند.  قرائت پیام رهبر انقلاب به‌مناسبت سی‌وهفتمین سالگرد ارتحال امام خمینی(ره) @Farsna</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/439814" target="_blank">📅 11:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439813">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4176f5c05f.mp4?token=NgK-bAid2KElLVjDmUqZ4QVo38j8W5QPCGoxnTGm_ooJTLRAgVcIW1LJH7aQ6TyV6k3aeAy7_bTcacg73whYP94QCDSHrdmvSb33NT9b7ScIMmkGSVI0V3h6kFbCRf6hXsvfO0dOadB8jNuDBVP1Qoaee_YfP3FnaV_ReehJCufmvfn4LIqxPSBtI11tEiTRZcIuEXrxrkCGoajZs5nqmU691RgcelcojIwQK2_XYKy8KoBBa-kAByJkiiSP3Iy0hS0Hyb3IZjVqJkDX-2kepJ0PC84cDoNOSz4wHpxV-_eFaC1B6-UoOXwEsiRZHYg7KrGAXVkxRbiYN45CelF5tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4176f5c05f.mp4?token=NgK-bAid2KElLVjDmUqZ4QVo38j8W5QPCGoxnTGm_ooJTLRAgVcIW1LJH7aQ6TyV6k3aeAy7_bTcacg73whYP94QCDSHrdmvSb33NT9b7ScIMmkGSVI0V3h6kFbCRf6hXsvfO0dOadB8jNuDBVP1Qoaee_YfP3FnaV_ReehJCufmvfn4LIqxPSBtI11tEiTRZcIuEXrxrkCGoajZs5nqmU691RgcelcojIwQK2_XYKy8KoBBa-kAByJkiiSP3Iy0hS0Hyb3IZjVqJkDX-2kepJ0PC84cDoNOSz4wHpxV-_eFaC1B6-UoOXwEsiRZHYg7KrGAXVkxRbiYN45CelF5tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر انقلاب: رهبر شهید ۱۴ خرداد را به فرصت میثاق سالیانۀ ملت با امام خمینی (ره) تبدیل کرده است.  قرائت پیام رهبر انقلاب به‌مناسبت سی‌وهفتمین سالگرد ارتحال امام خمینی(ره) @Farsna</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/439813" target="_blank">📅 11:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439812">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10e059d45a.mp4?token=qsWkNwtvVHNdP-exWoGLqhexxM7gU7zK42cYecuiZdKU6GM8uOVRofcwLIorgGYlO7EMChsGcNVQTxdsTHtlrds4zpDoYslAVLSuDAcBKrKSeVCjqUIZY6VIhZP-bb1wJXBZFsFf8FpivjuLgJmcMTFdCQGYOtXlhF9pbrmohsEEzcz14oet3qXNEdPwoa4Wp2Gr2cRsQINYdyZpWWFUNxHCSXubzE_wwyAeUobwfyZxF_rGlQU_T-u5NwjDnbQghQORn5wVtll1po9yDaAtmNsdZYzOdpazpaPTAu_TivT3uaAFeFV_a5pGufOuvVV3NNk_Yao2dDERJy5gqzlYxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10e059d45a.mp4?token=qsWkNwtvVHNdP-exWoGLqhexxM7gU7zK42cYecuiZdKU6GM8uOVRofcwLIorgGYlO7EMChsGcNVQTxdsTHtlrds4zpDoYslAVLSuDAcBKrKSeVCjqUIZY6VIhZP-bb1wJXBZFsFf8FpivjuLgJmcMTFdCQGYOtXlhF9pbrmohsEEzcz14oet3qXNEdPwoa4Wp2Gr2cRsQINYdyZpWWFUNxHCSXubzE_wwyAeUobwfyZxF_rGlQU_T-u5NwjDnbQghQORn5wVtll1po9yDaAtmNsdZYzOdpazpaPTAu_TivT3uaAFeFV_a5pGufOuvVV3NNk_Yao2dDERJy5gqzlYxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر انقلاب: ملت ایران با بعثت تازه خود در کنار جبهه مقاومت مایه مباهات ملت‌های آزاده شده است.  قرائت پیام رهبر انقلاب به‌مناسبت سی‌وهفتمین سالگرد ارتحال امام خمینی(ره) @Farsna</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/439812" target="_blank">📅 11:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439811">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/658513c42a.mp4?token=R-73HFpJ1LQbibpD3NnKRwpwyIFRCqp42qJ6ewr4VF-al6Xz8WIUjlj2DPUFMKX-egRIyT8T9UpyNwGk_psOP-4ulyO1eghHOFYEwjEo198h517aHBpCidTT6HDI1enZ_ryTW31AKOirAtQS0k6n22aWDa7ipVkG-QWNF6J3X1_7xmVI-MJcEdHJlkLjCEOomyY25l766jlsJ3gjWKfKmepoy7p8J6q4-PjpZtdnPg9wqCtjYCx0iVjfAwFcASKbYIYWIRCsDEakpWmHKKmr7eX0lFFNLuOwlbKS5NoRovEyFBzuSpw7NODzpGsm4QA-5beEdvh33JgRlTZdeXx1hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/658513c42a.mp4?token=R-73HFpJ1LQbibpD3NnKRwpwyIFRCqp42qJ6ewr4VF-al6Xz8WIUjlj2DPUFMKX-egRIyT8T9UpyNwGk_psOP-4ulyO1eghHOFYEwjEo198h517aHBpCidTT6HDI1enZ_ryTW31AKOirAtQS0k6n22aWDa7ipVkG-QWNF6J3X1_7xmVI-MJcEdHJlkLjCEOomyY25l766jlsJ3gjWKfKmepoy7p8J6q4-PjpZtdnPg9wqCtjYCx0iVjfAwFcASKbYIYWIRCsDEakpWmHKKmr7eX0lFFNLuOwlbKS5NoRovEyFBzuSpw7NODzpGsm4QA-5beEdvh33JgRlTZdeXx1hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر انقلاب: خمینی کبیر و خامنه‌ای شهید آمادگی ملت را کشف و احیا نمودند.  @Farsna</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/farsna/439811" target="_blank">📅 11:06 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439810">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb23c1d7e.mp4?token=izJz0gw_3cIUDQqrEhd9UdkTS8rWzT7L-4RxcPeNBeFJ8eW5KuMhLEBs_7g3h-UZ5EYFnTro6fgPcEQRfsK4FF04BS0MaOeVNg2Dg6Ai5hr1QdQ6jW_HGfgihvN2UtvVhNvc2T4po44R4R47IXCAL3eCo1OSF4628xTmeAJK87dpgrL0cjarrOEu0yISHV0-cnzp2RxSOM3xRFFDgxkOsOPKAzW-0XjcBaG6V6eiqiggaHa-bJARS8FMSWM3w-GHxsZUfhKgkgVfZhsMUIRRhFB5UrkiBUYZEZ32lpmI8pmNntPkd2UYxlI4SviKjKlE2NvVbmhSj3ZZSyxONG8z4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb23c1d7e.mp4?token=izJz0gw_3cIUDQqrEhd9UdkTS8rWzT7L-4RxcPeNBeFJ8eW5KuMhLEBs_7g3h-UZ5EYFnTro6fgPcEQRfsK4FF04BS0MaOeVNg2Dg6Ai5hr1QdQ6jW_HGfgihvN2UtvVhNvc2T4po44R4R47IXCAL3eCo1OSF4628xTmeAJK87dpgrL0cjarrOEu0yISHV0-cnzp2RxSOM3xRFFDgxkOsOPKAzW-0XjcBaG6V6eiqiggaHa-bJARS8FMSWM3w-GHxsZUfhKgkgVfZhsMUIRRhFB5UrkiBUYZEZ32lpmI8pmNntPkd2UYxlI4SviKjKlE2NvVbmhSj3ZZSyxONG8z4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر انقلاب: قیام لله زیربنای مکتب امام است
🔹
قرائت پیام رهبر انقلاب به‌مناسبت سی‌وهفتمین سالگرد ارتحال امام خمینی(ره) @Farsna</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/farsna/439810" target="_blank">📅 11:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439809">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78a450c312.mp4?token=dnsUpVdzR0n93UY-Bfw20AgDCjFQPSZ7zhp-25tpRtof7PiusVmD1eqJM5k57ozIYnTK6rJbVzHwzDxaq-S0TC62bq6hXD7jB5KxobcmL7G_KmlZxfHyw5gnVRbZ8cm2WpFpnWcPPlLpuhgyctg9rFXl8UqsNdHyfYm7TcOfqB9K942nTVK44aabdTampIpMKz64n1Bh_I7pN9NYWZzNmhkxq6YzeT9-TWt8DiJSlg9IdIFSXzsqT7P2BXN9NmgKhubLRFGl0aaaL1pdJkqFJN1oO57Ag2XrPQIJ_y0pdfz6K81FHNN4zzn_r1Kv55jgPPwilHKu2yZI9Dt0HqKQjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78a450c312.mp4?token=dnsUpVdzR0n93UY-Bfw20AgDCjFQPSZ7zhp-25tpRtof7PiusVmD1eqJM5k57ozIYnTK6rJbVzHwzDxaq-S0TC62bq6hXD7jB5KxobcmL7G_KmlZxfHyw5gnVRbZ8cm2WpFpnWcPPlLpuhgyctg9rFXl8UqsNdHyfYm7TcOfqB9K942nTVK44aabdTampIpMKz64n1Bh_I7pN9NYWZzNmhkxq6YzeT9-TWt8DiJSlg9IdIFSXzsqT7P2BXN9NmgKhubLRFGl0aaaL1pdJkqFJN1oO57Ag2XrPQIJ_y0pdfz6K81FHNN4zzn_r1Kv55jgPPwilHKu2yZI9Dt0HqKQjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر انقلاب: درک و شناخت امام چراغ راه آینده ایران اسلامی است.  @Farsna</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/439809" target="_blank">📅 11:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439808">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dde0fa23c.mp4?token=KjaTpQHwJQ4XkPX-5QSHEuhe6T9-0qLO-q5FULiRFDPHPyemn8J5eAqluu_8OiBaG9eUbnl-sqPGWsAXN8UcKRD2bvJ328xyiez1t10s2zYXexDf3RvhH_HQYvfrgsKUW2EnhROo54vo5xqEF0boIvVvL8vxqLTt6R0TqCPwVDv8SJVBV91nHerB7K8HWfdK1PgQ6j-D3vowwrx6NWgsg33Tf5dl-cRjFT7Cqvx5meAlB5y0VSah433t4zykLjaQiKEf-_6iibjVbAg_oCqjCEIaaelcFzW6y3UBMpgV1ejnXvstIt1kEhuiwEhZZnE5jooeHLP9bbKh0NbiE6o04w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dde0fa23c.mp4?token=KjaTpQHwJQ4XkPX-5QSHEuhe6T9-0qLO-q5FULiRFDPHPyemn8J5eAqluu_8OiBaG9eUbnl-sqPGWsAXN8UcKRD2bvJ328xyiez1t10s2zYXexDf3RvhH_HQYvfrgsKUW2EnhROo54vo5xqEF0boIvVvL8vxqLTt6R0TqCPwVDv8SJVBV91nHerB7K8HWfdK1PgQ6j-D3vowwrx6NWgsg33Tf5dl-cRjFT7Cqvx5meAlB5y0VSah433t4zykLjaQiKEf-_6iibjVbAg_oCqjCEIaaelcFzW6y3UBMpgV1ejnXvstIt1kEhuiwEhZZnE5jooeHLP9bbKh0NbiE6o04w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر انقلاب: سند افتخار زندگی امامین انقلاب تأسی به حضرت علی(ع) بوده است  @Farsna</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/439808" target="_blank">📅 11:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439807">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/007abf53f6.mp4?token=WsIc-1Bq6crnpKYKaCLdJpJNJXlC8eUaAHwck5uSCE69WaMKJDEoJE8GLtqCq4YP2On1_0kWCYnPbbdks15ULleb_mJUGBSCEjn5Y3SWHOso0m11vLGJ3gDC1UL2fpeeYtpm84Uq1K5-p-tcqVX62_aFV9mwrEl-W7kftVZ7Rrd90n5X8jMxa4kXGpyjaCY4s630RRTa38_ZqYAxUo-O-QrqeKYVpIIGaDSLNIGsAmGhPJBeaXNe5K-XJhVXOZqrmd7Q2ik_W4jFYAMt11jMBK3aVGxwuyxA0w3v77xb3KxXDO3N917kOE21qHN0iU58SY02_GKzhzrKNeL6f0Miyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/007abf53f6.mp4?token=WsIc-1Bq6crnpKYKaCLdJpJNJXlC8eUaAHwck5uSCE69WaMKJDEoJE8GLtqCq4YP2On1_0kWCYnPbbdks15ULleb_mJUGBSCEjn5Y3SWHOso0m11vLGJ3gDC1UL2fpeeYtpm84Uq1K5-p-tcqVX62_aFV9mwrEl-W7kftVZ7Rrd90n5X8jMxa4kXGpyjaCY4s630RRTa38_ZqYAxUo-O-QrqeKYVpIIGaDSLNIGsAmGhPJBeaXNe5K-XJhVXOZqrmd7Q2ik_W4jFYAMt11jMBK3aVGxwuyxA0w3v77xb3KxXDO3N917kOE21qHN0iU58SY02_GKzhzrKNeL6f0Miyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر انقلاب: اولین ۱۴ خردادی است که پدر مهربان امت، مهمان ضیافت الهی شده
🔹
قرائت پیام رهبر انقلاب اسلامی به‌مناسبت سی‌وهفتمین سالگرد ارتحال حضرت امام خمینی(ره)  @Farsna</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/439807" target="_blank">📅 10:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439806">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70e30e2ea4.mp4?token=nHlpghNQZU6czzUZMZ7VmRTkdmcIkX0wJXz_6nCxUjyTBdbezvUWZ__VXk4QXwCCarsZxELafEM_LEbML5AiPxoTdxL2P5m-CqhrM6d7Ih-GUoDmw8kIWvGPfhsP7QInmW5XK3HM0rnK7rSqqcRk4EmmE8Km73feGLWqr1hBuR066clJziztlUji7MbouwSf2Me3MD_ypKcVpmCpAu4Vvk9JfMIWhKvLHqXHcr2258XzYxyuZiA2gDSEaFRjfcKEASOUoLsLs_qdXKWlexVnYjzudHsVooT8PrOT2RO59V9jWHY1F_CzBsjOvgPbeYosaENv6R2CetqKNDQ3bCxmjXGr_R0WNz6SJqrg36RLpb3QYIgYlClOCfDylS6DReEUR1Pc0AnkCJBweNuegJBBU8Nc4MrE-SYNhh8fcWL8iVwwO3fMLoIFEjWE6DvnXAp9__SUI7zGnGOZV5l3gl3lTil---zqCjvS0s2tILxCYXhquj87tN4D8kjQKIHPCwvKeuIydW4ztPnQkYqTihTW1vZPEIMgqmE5t1SOe5lkrtFch-rlznm2ehsYo0L9CnYLC68NhbrNGCxjGNBMYQ9M5En1rSmrUnyiNBIpmXxUaQmvaUMxBexL0Y7KPNwdeBXmDmm7kHvHAQLpMUKPF3mVIBlHeSnKNLBxdkuHQdja9GM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70e30e2ea4.mp4?token=nHlpghNQZU6czzUZMZ7VmRTkdmcIkX0wJXz_6nCxUjyTBdbezvUWZ__VXk4QXwCCarsZxELafEM_LEbML5AiPxoTdxL2P5m-CqhrM6d7Ih-GUoDmw8kIWvGPfhsP7QInmW5XK3HM0rnK7rSqqcRk4EmmE8Km73feGLWqr1hBuR066clJziztlUji7MbouwSf2Me3MD_ypKcVpmCpAu4Vvk9JfMIWhKvLHqXHcr2258XzYxyuZiA2gDSEaFRjfcKEASOUoLsLs_qdXKWlexVnYjzudHsVooT8PrOT2RO59V9jWHY1F_CzBsjOvgPbeYosaENv6R2CetqKNDQ3bCxmjXGr_R0WNz6SJqrg36RLpb3QYIgYlClOCfDylS6DReEUR1Pc0AnkCJBweNuegJBBU8Nc4MrE-SYNhh8fcWL8iVwwO3fMLoIFEjWE6DvnXAp9__SUI7zGnGOZV5l3gl3lTil---zqCjvS0s2tILxCYXhquj87tN4D8kjQKIHPCwvKeuIydW4ztPnQkYqTihTW1vZPEIMgqmE5t1SOe5lkrtFch-rlznm2ehsYo0L9CnYLC68NhbrNGCxjGNBMYQ9M5En1rSmrUnyiNBIpmXxUaQmvaUMxBexL0Y7KPNwdeBXmDmm7kHvHAQLpMUKPF3mVIBlHeSnKNLBxdkuHQdja9GM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پیام رهبر معظم انقلاب به‌مناسبت سی‌و‌هفتمین سالگرد بزرگداشت امام خمینی(ره) تا دقایقی دیگر در حرم مطهر امام(ره) قرائت می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/farsna/439806" target="_blank">📅 10:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439799">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PilY45H3DoQGVa4Od1qLtJCZnO98Qtfqz2vQP3Cq2lprNvdnyfc6sCu-d5SZdg7KPMy-Hg7kF7YheGfyeNPqhtwvfTzykOJEpEHf179orz3xzO8ALVJ9oosAqckzWw41UFT8TGl1Dcv5xEFZW-hjPVM63hrggy7QLE7KH7DGcbh-DvUNgcKKQvcBgutVF9kkD6nGeRs_wWi6Dar1BJeQ6DxQUfCtJleR5v33rz0RfWyTJAtdBvY8E13vWlGLhbbtCwom_XMxSfnqyGsvDHn5Wnzc36_Yt2kZK6qzqv77IrsYKRFChk1gB81HNYeUEVaWubV1OHyawEYBXBUogS-QEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u7r6ijWrs5fgcZbUgB9JZACPX3hPCAwoAl9XYhOeB_hlvmipquovbbStxLI3JDghODPpbSfg183oK29RcDvds3qss1gP20ehYEnf0IbzIokmKZo7np-O3X9hOgDixHjL64vLJOFb5SBrU0cIpuG6E6OdADjaACoZviD7rUSgBFozjF8NOw2fpBIikseJwXoX59HiYbPu7rgfbtdNZ1tzMFvGFUdQxAPmoR-nW2qpmlY0ANR3rrfm6_UvRTRYebOx6JeIPqa5PULag37Vz115oFLGrbgmUmVvNt9h9-TkS36UBYH75LO8jv6GdEZcXggjrS7_tWFVwXoAJWfqXmheJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V7EMAUQ2yo_3tx7DYo-Gv2N3C5Szgw4tsHYx-p5KXymiyRyN7WVL6tVsHAu3bKi-vSJv1rgWxwAm1WiOpzHqAlRonL79qEpLcmG-HFndjpiRvorM5x9_u0zzGj0kaNEDzcvfQWawfvYQZm5AjzSSIpb5lqABMwCqRmXdsKNJKRMtPtCNUypW8mykJGAqN_r3iay603SrtYRFNi_G1fVPwMzO_Ynp43hvGimy_QBX2L_UMXKRdUrX9T_JuFKKXzA-527ts5GM-OEuNLPxHsU3iY3KTjXTA_KKQju6Z8Wj52aQbf6mAoKOyWVSXxdJicKFCrSfO-vc2imOV2EMC_OfCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Klg0nHELTC9sN45AsYvfEZs60TL43eCxO4mkAQi-wbUGL5K3WlpUbrZU0V-q134oGqcTmi0GcFCZQ6XD65ABFPsDk6peG7YT7TRjnYdFX4hAHWXWKHGE5CWOek9enqCM68nLSejKnUr4vNf7wz5Qb9JYcsAV4yLTA3Al3RDBM8MN5GYh8X8XHTVB_fDUfkB4LluOh8dOoolNXQGx1mFVys66Vqr7aGwnV53IJAbpRqLhWENdFotbs5oZ6Ypkcavk0Iv4PYMLDGx1HAnibePrwFRJZc72ojUWKchJhkfthrAe7Q6F8YMDMTbH5Lakr6YHnLJWvBL6EWf_zOTwv4cy9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rMQEEw9C1N9HJ4L6Js6O5Ca4gJN0jlcx9pRxe73IsdYjE_z8rqwrzlqERFqvd1-ZZ3sL7T4UXO4SjqI17BNqtSo-Tdrfy_1PPMFfLmQg5obXcKoKC8wR3bYk4nZWZ7C2Gx3x3EeRGwhosaoOcqCALdb0P5tj_lCFKqLF-NWqFpY0IPknIOFairBK2CJWHxRIFCQOkLJV2MVT9VKOguGb_46NrRqzx8PwnByzIiXZLO2kgYFGeLHolG7ESSisArMN81wPq7ZVlsWYWycUFkNQaEf8rAWi_CbMJvLnqX7Pxg105LHrippO2F0xMGuKxfKKYLSNm5R0ySZBLFhlTHZFEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pTtfkcqUXP3EMTsow6iyQjgggrBD-plU3SmErMxwHuFd2DabgGD-SVQuuqlUFfXwdtByF6YZ-v4e6BaL8NWlEb1v756SvMskV-T6k8PGlHs7itcdg1YM3DnyzSHgtl_y4vidU9H8_2J71VXJF6KV8_aryCxyhEHh2mR4FNlLyzodV5_JjxIEInKMYQsRo-pqjXHtNdhMX_pXEq5ngVuLi6iwcsHQI25V1oIfAsag9kRrjWoz-eeqlyERsq28LZEvdNL51uf5USlD2e_mY5VVToD6OGcpT8BTOO5lqUkeZ2f2oZtGQZyC_FjCfpJq1_GMdoPDPq06AjfWA6QYa3ibWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sm4UtPAJfSwXVXi0IaJZK4N3qht-CtSiu_NvGe8obSynGlplDcLX5RhqabasApeCirYC4t1_-RtgVTv23bv6lyh8T8ZMzMj6ibGHN_Fu3HthtVCblNTkRGJPrgE7yRTRmJDIW_gmn1QE1q6JVgxL8u4iowBIDwJDwmX-zp_iQM5lQ6SLtBDu0G4ci0ZZKa8kbUtW7DgztUiHattTbPhysMPxzcjTwkDbFoT63FD_UEzHg0MUF_TXnFATVPfMTotzmxEpqODC1bY4pAowb1edNuW-YSoRT3gk9VNObyGYDHxFKNdwNUUPDnMAinzepL7iTKYufXPwohx8186R2AHVXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سنت ۲۰۰ سالۀ ندبه‌خوانی و اطعام عید غدیر در یزد
عکس:
علیرضا رجب زادگان
@Farsna</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/439799" target="_blank">📅 10:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439798">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwW4J6-J0P_k4e_RzHmBOyeXWwUTcrTZmfenSdyTikA-gY8XhhfPHdC0B8POsqx9wzd2JoryG__IspZzfLp2eXzNc0K_1gg6WoV3utRyYRC5nFOHpfYkTgtJ4aP1_GoQDAreoWlJOy3CbW_cm6tX6LbN5h9iTtBHDaH1DiTkdiniNnppiTmsy9PTagsJ2IsZEqUcKxBaV4FAjNP9SweZWQmXxlsMQHkWEiXpIm9mASsBw0xaeXqIiziydAgc1RLrA7DzNBsSGX68zaIyv8zG08CQycw_JxkzZkaI6SpM87AaEi8xBXIIivwBoRmSCSdBIMr4x0H1XwLP5WBr4D6dgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراق در سوگ آیت‌الله فیاض ۳ روز عزای عمومی اعلام کرد
🔹
در پی درگذشت مرجع تشیع آیت‌الله شیخ محمد اسحاق فیاض در عراق، دولت این کشور، سه روز عزای عمومی اعلام کرد.
🔹
در پی این ضایعه، «نزار آمیدی» رئیس‌جمهور و علی الزیدی نخست‌وزیر عراق  با صدور پیامهایی جداگانه، رحلت این عالم دینی را تسلیت گفتند.
🔹
الزیدی در پیامی تصریح کرد: «عرصه تحقیق، اجتهاد و علوم اسلامی، امروز یکی از چهره‌های ماندگار فقه و مرجعیتی را از دست داد که تأثیری عمیق در اندیشه و تدریس برجای گذاشت».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/farsna/439798" target="_blank">📅 10:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439797">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
پیام رهبر معظم انقلاب به‌مناسبت سی‌و‌هفتمین سالگرد بزرگداشت امام خمینی(ره) تا دقایقی دیگر در حرم مطهر امام(ره) قرائت می‌شود
.
@Farsna</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/439797" target="_blank">📅 10:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439796">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e690df03ec.mp4?token=ny91sQoZeG4Qe3mN7-ZWVhXAm0uC17FFPiVo7Pcu98F6LKTLq0thEQWoOktiG0f848wS13MQVklJEE2w8UJqkV1OkLg3hvBHlke4ZvBw2b4VuMr550oIwdGbLCU5HRAwkWYK0kZEtIGpmGfUKuxIT_of-fD60kMxyly2fsxWnpsfGasH2DSa1LdHGQJv9l228X9hJZlsFlyxCeqq6ovclgwYxqKzCW3RXyvE8guSmHRr699YVbdR8kIbLNnsMC7nv4E7bhr5rwBo3ptkcX5Mf-kQXImLgdyBncQNV2fJaAThVD94E8TleEUOe4z4xLIV1HLDE9Jjj6REXrtUFm4reg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e690df03ec.mp4?token=ny91sQoZeG4Qe3mN7-ZWVhXAm0uC17FFPiVo7Pcu98F6LKTLq0thEQWoOktiG0f848wS13MQVklJEE2w8UJqkV1OkLg3hvBHlke4ZvBw2b4VuMr550oIwdGbLCU5HRAwkWYK0kZEtIGpmGfUKuxIT_of-fD60kMxyly2fsxWnpsfGasH2DSa1LdHGQJv9l228X9hJZlsFlyxCeqq6ovclgwYxqKzCW3RXyvE8guSmHRr699YVbdR8kIbLNnsMC7nv4E7bhr5rwBo3ptkcX5Mf-kQXImLgdyBncQNV2fJaAThVD94E8TleEUOe4z4xLIV1HLDE9Jjj6REXrtUFm4reg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین حضور رهبر شهید انقلاب در مراسم سالگرد ارتحال امام خمینی(ره)  @Farsna</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/439796" target="_blank">📅 10:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439795">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8103559134.mp4?token=FdUW6yiEfkEcazwecGQjT9xiEPHrfcnWZsL8ogqxsa19yyuVYzmEowT70ozdvfBVckFOjwLL9iRRdlAxOrd-oJuF5-D_rHAsQq5HCWg-TxdACcbK12PGhLdYm4r3OCVuDgfbkeT1nncbRdqhp84eH00qUKDZXZhEKnVU95vzEKwxtiirXrybI3R86sLdAfPO7U0ec0lvtJN3Ptfbcib97AUBRJA96UfeK59SS-TXAHyTr5BZ87pMrD4k5CK6TLtm5SLtl3IcvA76DbzYPAFbVsqe5V3niAqBMj88TV98ZfxHejxUah3VXjk3Qt81jaz9flEes3mGIFMdFf4llGsO2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8103559134.mp4?token=FdUW6yiEfkEcazwecGQjT9xiEPHrfcnWZsL8ogqxsa19yyuVYzmEowT70ozdvfBVckFOjwLL9iRRdlAxOrd-oJuF5-D_rHAsQq5HCWg-TxdACcbK12PGhLdYm4r3OCVuDgfbkeT1nncbRdqhp84eH00qUKDZXZhEKnVU95vzEKwxtiirXrybI3R86sLdAfPO7U0ec0lvtJN3Ptfbcib97AUBRJA96UfeK59SS-TXAHyTr5BZ87pMrD4k5CK6TLtm5SLtl3IcvA76DbzYPAFbVsqe5V3niAqBMj88TV98ZfxHejxUah3VXjk3Qt81jaz9flEes3mGIFMdFf4llGsO2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور حماسی اصفهانی‌ها در جشن کیلومتری عیدالله اکبر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/439795" target="_blank">📅 10:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439791">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ggNF_wl_csSBh8kQsp5TLCJ222Ou1BdfyXONFzaj5MtDofIiRGKbNRoRdEFoGDI2MzDCBefvgM66tseb95ZjyX81B886n25w4d6cvYPb27dlWTUqKpGogqXUISdwAMcAC5V-VkFuYYlhseF8S7_fSxRLWrQCiyFPsYP97hvSmtF4KfFK8Om8OlS3V1lhPgOEXtFQGfyYryH5wDBy39BQiYgT3Jag0SgW3bugYv9ajouwpmaTojnA7ky9lBkZA3pFF09Nc5XM1e9sbwua9ta8c4oVuVWrfq73JTnZQrqoLTYYgvhST4uAXh96q8OY_PeonDQXFZosFLxg1QG6qYlmlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kSpLhNUX4XfFzT5S00GZlkkQOUui1XELj2VtoaGoE2AXTAmYVW95rw9XidkwJkQ-aTHNyt6XQEx1qijU4rnfLiOuj5M-6zFtUK_zYWOdp4TTyp-lskyHNbPRwPLQokppcTLTX2XtA6QeuujT_bTiFMoiCNfg7SEL-x-ppdiu1Q4k9H04woG_v1gj5FLh78X9RMZZU5cptrXFpNSO3bf_oT-meRIIA0UYx7C55vHsXWTfg9TTHeLwiFjMPld2ZcAg24JCM1u9qkOOx46XQrazx01LWlGO1opTUQD2PfiWN6OZaNxf6OWXrN_hY5S6iV8-gipfWXGcF1_goOUyAJ-vbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HHOGFgeyCNgGXQq5m-u02SoftdjppiAp3xxKtKOw8Inqq7yVWvHA5qZrI-o5o2htnn6RBOZ5lWfqPBvCuNCxI73jqcISOAlOkPdVD5gPv7n6TTu5PjPMC7oOHYYdVjWK3TUvsUf6DSYc5pQDXv0SBM87kydgiGiSdw9lDfB4YvXMbDcaFVigGbfoZ4vfGYZaY51pFEEx7i2c-5_L4k695fKV6yB-COUBsyNDqWVBR7rS-e8ou2F4NQfwvvAT1XItKq4gIkOAaPzQypZxlct6l9XSQbR7WPurpENnR97JPdz7spNy-QqZDwszcMA9Pfh6golKRaJBfqfLNUHqs3HHyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OlNBdcQm5aP6v0MjAnzqErXceojw8G1VlNaeDPxkQBRGKj56cJK682e7WmNYebjzeOzYsqxneiLsO1eeEoci3pNPKYEEDLaZhOKiT9DiHHt7vKGf9FOCuV6A-cUgst8i3p9zQrnOu-eBQamnkeCssCPTC0fzYNAPQB24dQw4KbpFgqnPSkAgkv5gAvT7zQDZKJQ02XFL6TrgGigqOblnwmkRJwB7NPMg0JaWdaUw36n771DhKIoHd9woEwXTI78E3YFO3UuRmY04EQbFGiLCUu_0klBvnr7914WYd87temQu6fa4E836QBqLb_djefBKYHYbuOBmJf1hKhFZAxhvCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پیام اتمی جدید کره‌شمالی به آمریکا
🔹
همزمان با ادامۀ تنش‌های آمریکا و متحدانش با کره‌شمالی، کیم جونگ اون از یک کارخانۀ تولید مواد هسته‌ای بازدید کرد.
🔹
خبرگزاری مرکزی کره‌شمالی ضمن انتشار تصاویر این بازدید خبر داد که رهبر این کشور خواستار تقویت توان اتمی کره شمالی شد.
🔹
رهبر کره‌شمالی: میزان تولید مواد هسته‌ای قابل استفاده در ساخت سلاح‌های اتمی طی ۵ سال گذشته بیش از ۲ برابر افزایش یافته.
🔹
پیونگ‌یانگ در مسیر ارتقای توانمندی‌های راهبردی خود با شتاب بیشتری حرکت خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/farsna/439791" target="_blank">📅 10:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439790">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cca8912fe.mp4?token=O6RD73VxJqWO7AslDo9h994ev9AGwhgceqETVuKfImT3ehGLnbups32t6599szq76agDql9eBPxgBrBEPxXm945nRyp2IsXt8HvuxcDW-ReG3ObnrLC8P4TKstDpNDD_9oaY7_4fJgWaBFzWcSjWQb5trRl-VoCaknCSV6a2se2Z8hzRbsVFwZPZEBgGzN-ZTLWvCULycIHvxUTSOpT4c0F8qtSopPLQwdadnkFplr7K4zL_3o6wIxl2VfJsfadzMbRp8EJ56KbQdXYjAnt0WK37yCDRm1GhKRU5E2nnd7qjaCgJJNr2NWxNGuuTSVbZRYtENNjV9YAnci0JCA1qxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cca8912fe.mp4?token=O6RD73VxJqWO7AslDo9h994ev9AGwhgceqETVuKfImT3ehGLnbups32t6599szq76agDql9eBPxgBrBEPxXm945nRyp2IsXt8HvuxcDW-ReG3ObnrLC8P4TKstDpNDD_9oaY7_4fJgWaBFzWcSjWQb5trRl-VoCaknCSV6a2se2Z8hzRbsVFwZPZEBgGzN-ZTLWvCULycIHvxUTSOpT4c0F8qtSopPLQwdadnkFplr7K4zL_3o6wIxl2VfJsfadzMbRp8EJ56KbQdXYjAnt0WK37yCDRm1GhKRU5E2nnd7qjaCgJJNr2NWxNGuuTSVbZRYtENNjV9YAnci0JCA1qxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ابَرپرچم‌های بیعت با ولایت در مسیر میهمانی ده کیلومتری غدیر تهران
@Farsna</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/farsna/439790" target="_blank">📅 10:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439783">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pm-raRdl1pcM-psE9euvTuXY17O7lbGMdtU-kcb8sXE-zpkL_KYiEvREFO1Lb3R-cVZR7pyTQXsl3jfgbvNtVsQYsKbxiYnSOeLLEXSeFPlqj533uFTOnfMqhXvtjuiTaB0pc54AWdcVpL-1y3GJXBHQncXTxlHLyEfho_J6w_SE9krXHQOv8tapfdaYnjDFcuZUaiDk8r77GfXBLnKFyWSZcCuyTHD2nAWO0CrztcN5wpv4nncx5KuGTb7xwCUOIn_ns9G-LvwdA6mk455shuFTN9JfNe4cMISuWMLE3I5k5KPM1hMJBF-J4Z2pWhc06E7tVV5sVuTSZS3uZJ_upQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DlyOibk0ikIUVUt-2du9wpAO33F6RpnywHSPlmaDuN_HUGRpOprDnJXTva8Ul5U8UX0iMKFqBl8ReseC7hMa9g9FTqO1hVhXEf1j6MdaANmSgzFaU93AV_iwc6sV74j9Iv4fkYnDqyVuA54ul7hMmSQ5r6lcMNW_cWKUhl_oXTnkMQ0Grp2bDP-JgXzrx6VMyGsA9ox5CrqS1sF9lAXRfcHdfT1BW7vkXSvSGWjdaaDG5iaO3t0eXXiAsWNTh0ybXxNWDuyOIkLPtsbkosAa5Nq9QoHvEKsHlEghZNM_S-Q9dbZ4xNowtZ5mwdOeMzGueCjD1bc6kwgAEUMtebpJeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KAtqZr7xA2RQcVENPWnVeeN3e9G4QoFBVHHlEpMG3czB5_Z8d3TB-rtQUaT3BMjoCgM3AizCDz3C5fVuk5ArT1-FWMGcmdN6jX4iFQF7YbXayJXy8TAtISyeZHeLMose2-4oNGRzMQrexRiUwaVohqcTC5jyQfkE9OK98cbdQi0Yy_y4nBYULTNP1bF-0XvEjNCW84t6ry_KelMzGAuMyMsI0AX-iMiDIg2VEgXACR4bTWctLxcp4VXnR7xevKlKjfv6KK9_mpZdTqki8W9X3a3x7eK1sb4i3uMMXikjlsg0pWx2dbF-avDvBrnBDowJB_V22vUeK0EzJzLSRCOFcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GVHwcm-GxhEGG_dppupNjKi4AsWsqBtrl7-YqZn_E1CwtVatohX52IPi9IgRFvSF8GZA2EQWiYqPmk6JcbCOEe3G3gcdVQ9iRobeSOxUHCPB5hizxOb3Ch_PQURLCkFvRFBG0Z3BpbRM8alnpgyDFIKM1ytxDQHGN-SZXr8hXw0epeW70IEqjXkgT7vMYroC8aOTtHZEgMDhRvAME78odcOZ8Wwvv0NNn9RG19xRXaYeicWcgZJUZU0qr298lHO4MR7W9cSo_W227zBfbGuK0XspMGJ_-iGIOaALAtrcmxsllXHbicMD1CEubD2U2bSUuHrydj9g6Lf3Iuqx5GlrXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IJ78Rucu4RhwO1QzE8f4lgbmWuNwprCFCh8lKx_Rpq_CfhnWjZJiqN6RQz69LD1YDqABq7gDPXXg75d0oSv5MlGeXrm8mp1ptiE4MxFqeZakMF_Tuhq_chqfFQ2FgCy3znWqHK2jSMsDwRwCrDHR1pupOBQd0Ccf6Va68t0K8C92rXu53Yk8E0i2x0gU2p7YlpDApWKxAiiJ9TPdHN_aYwDjnLQWH3t66MqpyM1J60tkAFDYc9m0GgZUr984o7y4RzNCxrjd7UA4tYsFaNphRijWsoUmQeMrGsQ-kmLMzkwRLcmPymJniV-X9s78Z7JVpLzpoDOVmdFEr4RyEwliUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fw_SIm_RehzXM5nFNa5_vGvqJ4XZCk4Pwndr8rqt2UFb9klR23RipBdoeHPxtPNFTECesqHbo-AFqN8_b1SZcSOl3WrhvGfwpOsekldUOVvcOQZUt7vvdJlpa_dqm7q9LfqxfJFs-Kz53DVsS5tlThKRS89pqkhXWgXaarpXQuZc6_ONlxvs1_0j09RUmFcXpYOrfXTu39BNMmjJz4HBg9F-GzH1CP8uzR96P9Oib3rjwMsbgeOrlLv3mOw5Ji4GA8RGy4ZpxfXAVU9SF-xnAfcR2ii4GKANMh0zit_WhWBSE1cG9E64YEHgN-OI0w5W_UdOjyiyJKg2s-oW3N8jtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vQ1NdKnjPswBrveSIuMruOq7gVnr2Hgll0OC2N8i4E6oVcaxw9vqK2z6Z29XnMot6fj1ZeLnkgDoazrruqT2NEtYwlOiP6WPpGtJ72Wfa1Zt0g60SpmVU7cLPTuok2kC_Odba9kFugvw3fc_CLBXxC4B4l4GomWl3kk1DNU4nnmgntOtxIQtGzTPBY1QCmfhwIOqpzrzaUx4_JCpv4XEQIa1szAzchD7MuI-J-mdlEQPLgaGmjzfS58R8goEqeLMQ9GEG5YPmy5-DrZFEPJtE-GvCrF5tAQwAtyUH-XQdkm-DOCiNEnMYQPWjbLbOnpR--VqB7lDdUkY4a_k1Gv22w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم سی‌وهفتمین سالگرد ارتحال حضرت امام خمینی (ره)
عکس:
هادی هیربدوش
@farsimages</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/farsna/439783" target="_blank">📅 10:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439782">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e653079661.mp4?token=HHrl4iWSUL6x48OyoHnrdfFQKk0-_R0H2A04SdcgzSw5H5VlhtPAW5zutCnhiBNJyeV6P1JaxowILWBjQaRf9wJJC7ddhgY4G2o3KDQ4NmaIkKwfisN6ts9qurc4NTWe4cKoTylIS6qzSadLmSP5T8ch35O_3jEXeHTvWtJTtSUNUWtRt2D5miF5VAN2XP0XaAjKPBEFSDkAk3kpmM7oUBUb5k3BYwTQDLl594WosdCWktCO9-C1jH8n9uLoD7PkwTSs_uIfsby6ArgiCQlBfHo-VI3QfmPbsd4KduGF5R1qe0KsKahg1BzKXN00sWgIJG_zJcMg0H3AgB3_gRRxug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e653079661.mp4?token=HHrl4iWSUL6x48OyoHnrdfFQKk0-_R0H2A04SdcgzSw5H5VlhtPAW5zutCnhiBNJyeV6P1JaxowILWBjQaRf9wJJC7ddhgY4G2o3KDQ4NmaIkKwfisN6ts9qurc4NTWe4cKoTylIS6qzSadLmSP5T8ch35O_3jEXeHTvWtJTtSUNUWtRt2D5miF5VAN2XP0XaAjKPBEFSDkAk3kpmM7oUBUb5k3BYwTQDLl594WosdCWktCO9-C1jH8n9uLoD7PkwTSs_uIfsby6ArgiCQlBfHo-VI3QfmPbsd4KduGF5R1qe0KsKahg1BzKXN00sWgIJG_zJcMg0H3AgB3_gRRxug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز مراسم سی‌وهفتمین سالگرد ارتحال امام خمینی(ره)   @Farsna</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farsna/439782" target="_blank">📅 10:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439781">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1sGRvxjjoIXHzW_EiYMkssPjSBW61_LxzHA3v2tAv59QHPidwzsW1UF5YTcTwWmsC4OVxJDLvdGnFL9iGi9aEMku_gYN0c0RYYIcT9IgmLSit89dcBqlMgYRuv5O-sA1aYZpLkA8F8i7zUFgOK3oTlZV_0hhh1NQrPATM1H79rumKygMNSRXSaHGErpweyrLgJl4ufAxoFXKx1YeJtHnkDcVONlMkX18lqhrqZpjRRqqop4hUxfNzMiJgEe20KmyZAXyyfKHPBfjPFBbFbo9FK7jMpCeqaYQne3kFmd3sq0xuwM-FzrjCQbhWKRTg1-ZHNJDkJp8eN0ZqDbBia6UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمدی اولین فرنگی‌کار طلایی ایران در مغولستان
شد
🔹
پیام احمدی فرنگی‌کار ۵۵ کیلوگرم کشورمان در رقابت‌های رنکینگ جهانی مغولستان صاحب مدال طلا شد.
🔸
دانیال سهرابی و محمدجواد رضایی نیز در ۷۲ کیلوگرم راهی فینال شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/439781" target="_blank">📅 09:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439780">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🎥
آخرین
حضور رهبر شهید انقلاب در مراسم سالگرد ارتحال امام خمینی(ره)
@Farsna</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/439780" target="_blank">📅 09:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439779">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f47cc1de4a.mp4?token=bKil7-lxbs86qwzDi2oxwPnO-d04OZsD0G0opJmxOfecSLb9NV3vFuecvG6s2GAkG1-HjIYIL-OmvE-vQ44Qo4EJ_OF3sTSdW6ogE0pBhI1czt3Znli6F4AW33J4QC3l76sSotITWKQAhOc6xkaM8GMWQf9PqCBgUCsufClQDwAJPXgUeZDmYh4ymB8OCiwnt8OwW8OrJhL3XwtK-nxKO30zcG-mBHRM3f58YjAMTwxYOs9vKNqugnFxDQaU5Xu30wSpyuwkaL8CQCe3gxUZcrzizsRUyas7tzfUkKkHItvWiRiFar6XiMTq7C5buX11iaKpJuGvCiA7yTfcdV98-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f47cc1de4a.mp4?token=bKil7-lxbs86qwzDi2oxwPnO-d04OZsD0G0opJmxOfecSLb9NV3vFuecvG6s2GAkG1-HjIYIL-OmvE-vQ44Qo4EJ_OF3sTSdW6ogE0pBhI1czt3Znli6F4AW33J4QC3l76sSotITWKQAhOc6xkaM8GMWQf9PqCBgUCsufClQDwAJPXgUeZDmYh4ymB8OCiwnt8OwW8OrJhL3XwtK-nxKO30zcG-mBHRM3f58YjAMTwxYOs9vKNqugnFxDQaU5Xu30wSpyuwkaL8CQCe3gxUZcrzizsRUyas7tzfUkKkHItvWiRiFar6XiMTq7C5buX11iaKpJuGvCiA7yTfcdV98-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز مراسم سی‌وهفتمین سالگرد ارتحال امام خمینی(ره)
@Farsna</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/439779" target="_blank">📅 09:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439774">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ey1XV78akM96460uSMEt5qPWZcfxK89RWd56gp004PpdDvlwTEZOiLzPb4OtRvX48GD2t-EN7VeU0-SjH2Z-ir-74VOvJxba34WkEKgjPnU9hA0tLVnghDQ7hesz0QF215p4ycIW3-MPHgMDkN3u4Dz11zAB7x7Pe7MPyc_BrB-FEhtiXW_n6yofaZQSx2ZyQIUOjHNWj1Qa3DPYRAyCtYREf8e2VBA_XAAJJpRx8JFSn09edBEPMenJvAQwMhvoPawDfT-tpuZ48tEQK0rkGkdDR2ECy-iBG1X4dKED2wv2Tf6W1mHyoAVMmSikPbBmINKEpG5J0znEUlZh1J6kGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X-32MTHlrX9HD1Pp9aSI6EWiM6Ffe58gdZ5iYNTtq7JREAxsrjjIl6BGy16cWOmQq8xuUX_qlFJloQqSjq8H6ffRKV8kIfKXsvjGnn6UJ9rHY0j4JY30EflPbyAdXAHbpcxFcRAcgyUJWawwTvRafQ3sRZSwKgB8szEmHTh3aH37DgmIgupXPSf5EKZs81mMX58L08zbk8axr54AmYJRQbF_DHGZC3my66z3lELTB2_bF6KDV_QQBun77KbCXsn5KNagRoUgcRWUq48Bt_sN8wuj-gMM8fnSYdNEYwOBuq1ij3KLLxObMcB-eFpZgwWV8NwrZsvlXw1v7fJ5xFUPjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r2XE8ZpUHscqM0wHHhyflO0F_g-m4JX5Q-5UsGK_-ko6E2wiABWLwHJUiZPGKkH9NLB2SyADRVWE21NEV_uB_Edfr-ObyRVpYBPyKcxzI7BKu5GGCp6NUmZPgVkMdzuoPQHxt5BBX98zxSRhcM6b8zZzrdm2kQ4BbCSD2B4I1AqNtJR4jECXl3ZQplfI2G7V_Ourrs0G19RMFuaBmOtAVK-sDsGTYXhRbwUEejFnmsDdaNYlsWS47d3MlGNAD7L2EXp5eJ3d0w_at099YOvjUtb8yBL9fC-K_wLS1kFF8b5i0HPB8lkiICYy8z4yHwEm-rsYyfsTFC5WqbdgxkdLBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/egsZwhRWpOhpKQZqw0UbqfTkpvdmVm7tVDYa8RfhoMBKEZqXP6ze8ulbd6zhVqV_QCo55fDnCsFpQ-jx45MnTTgh8mST5nBinzRRYaSeepZwY2ykmklbJBy1qKVX3rEUjHxXZe58rY4vB2USYILUi57CImxi7QzzOkjQDv1ykaVkDLpPC7EE_wV8RS3IOuB2IL-0gpLHWmlc-QHs7o7Sdf1qmm32Mn-sSZ_t2-Bvi1G2Bz0uHE4TlJvwEnMahIYq6ieUq-Fd0Yjk00O15j9eMwqmC0VGaOZ1qIt7U1OA8PUzS4W81gdejJS9V546Na6_jjLCQ9MYnJOoCZeJx0aC_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XsNs3emvq-ka8oZHDDouolF_XjXsDakK5WH2qBVE7I_MznE0SnfuR4Ii1zSXRIDUOjXUnTMRceQulv3zRQZQtgHQAUlsIkwxnSC2sSMsAzYcC7IWuJx-vJM3FugSpJy00f20PUpNddRLHUNkyxug2usUZfC-jj5woj5HFukalZhO7o3xMhAdhL42V5-EHCkmyuChwui3OFoihO6rTnd2StOyY3WTBBr8dt30Xawu4ynfvhOgnbyM6nzOyhoK4Bv-72FzPKttuiiGrCZ1i3Lv-uU_3wRqDLj_pCrDgd84bY3T5p5Eo22AtbeM5AJmmoQ_i3LO13EX3OyJizNkPPUymQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مهمانی خیابانی شب عید غدیر در شهرکرد
عکس:
رضا کمالی دهکردی
@Farsna</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/439774" target="_blank">📅 08:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439773">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e2c8a0e05.mp4?token=EKIWKmiLBlhefZbhzc4Qk6fN7oGceHLPTCj3vImHXCTMx0kJpDkki-cmZbp2ScRpXlqHQ3yy81qF8eYUE4u-Xnf1ZY4K48mKynPWZKS2uRSLrJxPZmMt3qX92XFWchDPMzyrg_7EnGXd56Pf66WtNKnE0Yk3evC8Kxo_2eXiojTXtv1Ri-6OkYpF_9bIYPlYRQwXPCuN6aCwrQxAGEhGLpIaJG6Y60jWgbsxikGxnE2v2avpuJOc-KzfullFfjbN2sU7KA7i-DQzc0vz-rNg_VMfS93pAIAhgdWXckIZOtmQ5fD05yfM4mspFcID0o-Ht7CWgDbZija1xxv3Bo59vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e2c8a0e05.mp4?token=EKIWKmiLBlhefZbhzc4Qk6fN7oGceHLPTCj3vImHXCTMx0kJpDkki-cmZbp2ScRpXlqHQ3yy81qF8eYUE4u-Xnf1ZY4K48mKynPWZKS2uRSLrJxPZmMt3qX92XFWchDPMzyrg_7EnGXd56Pf66WtNKnE0Yk3evC8Kxo_2eXiojTXtv1Ri-6OkYpF_9bIYPlYRQwXPCuN6aCwrQxAGEhGLpIaJG6Y60jWgbsxikGxnE2v2avpuJOc-KzfullFfjbN2sU7KA7i-DQzc0vz-rNg_VMfS93pAIAhgdWXckIZOtmQ5fD05yfM4mspFcID0o-Ht7CWgDbZija1xxv3Bo59vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر ماهواره‌ای با وضوح بالاتر از خسارات وارده به یکی از پناهگاه‌های پهپاد/هواگرد در پایگاه آمریکایی علی‌السالم کویت در پی حملات موشکی ایران
@Farsna</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/439773" target="_blank">📅 08:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439772">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">بخشودگی کامل جریمۀ حق بیمه برای وسایل فاقد بیمۀ شخص‌ثالث
🔹
بیمۀ مرکزی: همۀ دارندگان وسایل‌نقلیۀ موتوری زمینی و ریلی فاقد بیمه‌نامۀ شخص ثالث، می‌توانند از روز شنبه ۱۶ خرداد تا پایان ۳۰ خرداد نسبت به خرید بیمه‌نامه اقدام کرده و از بخشودگی ۱۰۰ درصدی جریمۀ حق بیمه بهره‌مند شوند.
@Farsna</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/439772" target="_blank">📅 08:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439771">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0322159ad.mp4?token=JX0qumBEVKuiNB4Su0ACIQ_y0OqnObpd0nk1bQCv_S4U88Qyz1e4L7GdKrbUuPNdUH-X0ztOPzvQ0jPnpIWcZYzohQ77_RHsZfocZcfKHUHXkQyb7aHRPR4Eh-6q-_sfiEai8wQkZBqg2kuMLNQuxI2rL825Y0zJY5hS1eQYmVumdBaVxWPVBfx-u_8MWore7tHih0wVHiqaHCu2icao7lYXW-WVRyMr9HAKiLYx56qsqX06NkNx21HfpDCn7gQSNE6LtgACMWEM4IUT8F7g2V8WeiV013zma74-uFM4fQkikT6djHSVnwasGscXHoNRwDOKI-YzK9rL0Qr57YsbWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0322159ad.mp4?token=JX0qumBEVKuiNB4Su0ACIQ_y0OqnObpd0nk1bQCv_S4U88Qyz1e4L7GdKrbUuPNdUH-X0ztOPzvQ0jPnpIWcZYzohQ77_RHsZfocZcfKHUHXkQyb7aHRPR4Eh-6q-_sfiEai8wQkZBqg2kuMLNQuxI2rL825Y0zJY5hS1eQYmVumdBaVxWPVBfx-u_8MWore7tHih0wVHiqaHCu2icao7lYXW-WVRyMr9HAKiLYx56qsqX06NkNx21HfpDCn7gQSNE6LtgACMWEM4IUT8F7g2V8WeiV013zma74-uFM4fQkikT6djHSVnwasGscXHoNRwDOKI-YzK9rL0Qr57YsbWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دره‌ای شگفت‌انگیز در قلب زاگرس
🔹
تنگۀ سرسبز شیرز، یکی از چشم‌نوازترین جاذبه‌های طبیعی غرب کشور، در ۵۵ کیلومتری کوهدشت و در محل تلاقی استان‌های لرستان، ایلام و کرمانشاه قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/439771" target="_blank">📅 08:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439770">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/022cea969d.mp4?token=qhfVK0LapYHwcWeLbQFb2V2fFAMBRQ0UTIyAyRHyFF1tbK9p3MC8L5KjzpyyW3xsPbWEvYqZWo-fmPcEia60M4renb_ffiW51HPhRHHeSfJqsAMciwTadCp9GP5a02U0ceT_aXOhM90mRI42h0n_iHJbm1sNwjH8hcxR8U9-2Feyi5Y4jNMeR7ind0IKtDWj1kE7uYxyYF1Cw9JIiEhXviNnYo4oSMd30KBp30HtZ41VExI4VBXRmN5l6iV4ddPVgpl8QerHxjeoOzXlVq6qR2BYDb7RF7f2-9w5nlF529P8dlFtx96EkGu0DEOvVr-2BIpdQIDI7iVKtXrCjv7IDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/022cea969d.mp4?token=qhfVK0LapYHwcWeLbQFb2V2fFAMBRQ0UTIyAyRHyFF1tbK9p3MC8L5KjzpyyW3xsPbWEvYqZWo-fmPcEia60M4renb_ffiW51HPhRHHeSfJqsAMciwTadCp9GP5a02U0ceT_aXOhM90mRI42h0n_iHJbm1sNwjH8hcxR8U9-2Feyi5Y4jNMeR7ind0IKtDWj1kE7uYxyYF1Cw9JIiEhXviNnYo4oSMd30KBp30HtZ41VExI4VBXRmN5l6iV4ddPVgpl8QerHxjeoOzXlVq6qR2BYDb7RF7f2-9w5nlF529P8dlFtx96EkGu0DEOvVr-2BIpdQIDI7iVKtXrCjv7IDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جایگاه خالی امام شهید در سی‌وهفتمین سالگرد ارتحال امام(ره)
🔹
صندلی خالی مزین به عکس قائد شهید امت در جایگاه سخنران حرم امام خمینی(ره) حال‌وهوای دیگری به شبستان حرم داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/439770" target="_blank">📅 07:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439769">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🎥
فیلمی دیگر از شنیده شدن صدای انفجار در بوستون و رود آیلند آمریکا
🔹
منابع غیررسمی از احتمال برخورد شهاب سنگ به این منطقه خبر داده‌اند.  @FarsNewsInt</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/439769" target="_blank">📅 06:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439763">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bGXiM0gbERUpI0lk4akLRWNNrQ-SgcGwIDw9dzG4n0xTUitS3_D6_5xlJLQM_tf6AlQIBx-sGRsPOfpvXXu0PUjyN7tsCTk4AcTyh0Wyi8Orz66ty5UUZH7CHHykKK3k-RT_3ld0u9bM8_rFny-rvv0s5zj8bmGkwXjrHBdfjYdjyCK3xKhMjDhvMwXA49dXI0TRlGStq4rjQQ92wenbc1JmZrbrZ8JDmN4YvIBO-hSR4aF22Pzk_-B5H3w-wNNRXXod1D66pkoxvfWwUGZ3fyzzfEVLygtPRXd4dQ6kbx79ycou34rdP9tkIxIx4QbDAqpVfgUSNeS7Pi_yPutg5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vmFiYoV1OcnXZuokYe81S_d6JSNWfviGatI1UfJ-Mq4xSZ-XTOui3Ue39SMWGSSgmlMIyMqSz1-gfXkvOvfR83XDIa_-ZEW93JFcBjPZgjVBGd-QtvCa5WcXM7bQOtlCNAWOZHznJHrwgHnJg1YPfHIGKomV5BAm-iBdtKKitIEQW7F6D46uPsp6jVkY9ccXlYIiQSILXfMDqauCH3PA5peGshL3S6e6SipZm0LEbpC3rmrnTgJOETX5YnJ0swvfnpWNfrxK8lsCykV1tGl7EtqgneeHi0prOuOWMld2YDtjxNs8QrmCwB_9-4RvpAUWc33JsmPY_UHI6arTqyHFMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LYaxB4tgJ9N7SZqOEx79qOEoIHJWHazFnB8GDFDZomcEaUPrbKjXlmW-SNFBK3Y9RWa-LJMgHzlZkB5Xawx4v_FqfrQE7t3ukRNikpajdgrW7sJa4Bzza5776h3OpkN2ZX-iPJ6XXtQOdfVeq1AVw6oi2-PpBduvu40wlyRDfkAuJU1uqPhcZPht6q5JDBnmPNLNvkXc-9wVKiRgM3nlryV06HaebCJ8J9xGYHhK4kqklxNFRvPqcWsAmJvd-fc-tscEZlpQLYVzVa4HPMkjqM7mmqZW_d1FkITEghfMxK7aLJIzKPJDyPGDvEOHik1zQB7bJj1vm048sSvBxYogcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tOztHA4a1n5sPtH2N-9ESgUXxscd3JqpWLMH5fPsXdyVSpnCty3YGq0P5DJR5QwXDtW0z5kBe_SiBPmonAddn2wISi8TX8N12WzqhGOescJry8Ew74arnVj3Fzpd3HLYMFkW7RruDjFxif9byxUGrOeHUWQPg5ZqmeN1NPQnxRBcriti3qZS1yCf1JZhzdemhTSZXy78tHdngqxQyJluhY2mXp3ATlmtcFqyEuYau22yS7YSHYYfCLb_6aD4a3deQ2oBRAFkqdoTNBzX24HswGDpwfwAxs7YnNJtFODEH0IFSxTK9iMjRY9AqlZlAMA8921zkFgm1P4p18CLoj5M9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XETO1ujY5SmNlzzokzcLb9o4pSYPuYZ6v0_gI7OUjhwJvK6_twYNp4z0qdEeIU1A7bHIYeFL5FfXnSvqi-M489Fcs7UkguR-AyqULx6sBcKGQZB71dmKBLvudtfBBWV11sXd7FepDLqgf7D_aRymZBnHJ4nZ38ZF69SM0iZX4mkBkBLPBxSh2Sv1Y9VKvCPGcRPcAxLhBgi6hLfz6TFm1DZZHmgmdhv2iWLgNKyXZePqmEEQHVoqKnTNQvVjmAdPdCA4HcZ3Yj0AnbJe7vupVryDW46JjqwUdonE9z2vyCaUObVs_tZyTlnq-c6moHHCL5QkOJBqYts2BITVNwc_NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PuuJKGz837Iq5VMIcxSTTlImlLeypRWLzcMcfM-dJUXZhjr9N0xpQHjWdjLOx6hvdrLUKsgU5ai0R5jvt491qj7Ya3ZDAbqrbeS3vK3Q1wO4-j2JDQgdKAmTx7Du-WV8noO57e1-xvK-3CXHb_22-0OjaQAUv8GriUCwKnBTUYBAH3Fnl6lJtWw-aYXQs-zZS5iUNHB-jzH-BGygFULFPW9RDpa4XakOVji0Wqts6WI3_5II8C7DsBiT1c_f2lCCJ10zHCF6SgaDyZjuZm-1bHEDObQyP0OLOxpIJ9EKDM0h2LarxvoSouO2ER3gnYuz-uji6vE5brxh7ORYjlDbWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
زاینده‌رود چشم اصفهان را روشن کرد
عکس:
حمیدرضا نیکومرام
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/439763" target="_blank">📅 06:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439762">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekM87x-IOPxMhP97jg4HfzzojncW-5BpAEhR-VWsp6Wl_5OLEtuecdGxmiPF79widgcgVNZ4X2vZXIFvDqkWSeIwlVpq7tbNmqduf7JsXyq0qzw_WQ-hdbHATnB6PILByr_nf5opDW-hQMLM-pOSit4IeR726Xf3r4S39TAUvC4Cy1PsuJf1EdBg4TrVj5w0xnMMaOtDl2C5j_qAtKBZRp6dZL-jq3vSSQrEKBkHmQCMGWkIEeaH6JjH7Y_-vghqL372488n_O0vejwaa5izNBogwl_XvdSSrjCD4n5qESHXhS3WstdAxb_8-rs6oWuFmtjAMHbTk8FBVn8WLKH1sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشفی تازه از تسلط ایران بر تنگۀ هرمز در ۲ هزار سال پیش
🔹
یافته‌های جدید باستان‌شناسی در هرمزگان نشان می‌دهد ایرانیان از حدود دو هزار سال پیش به اهمیت راهبردی تنگۀ هرمز آگاه بوده و بر مسیرهای دریایی منطقه نظارت داشته‌اند.
🔹
باستان‌شناسان از شناسایی بقایای یک دژ متعلق به دورۀ اشکانی در میناب خبر داده‌اند؛ دژی که به گفته پژوهشگران، بخشی از شبکۀ دفاعی و دریایی ایران برای کنترل مسیرهای تجاری و حفاظت از تردد کشتی‌ها بوده است.
🔹
در کنار این دژ، یک خور باستانی نیز شناسایی شده که احتمال نقش‌آفرینی این منطقه به‌عنوان یکی از مراکز مهم دریایی و بازرگانی جنوب ایران را تقویت می‌کند.
🔹
پژوهشگران معتقدند این پایگاه برای پشتیبانی و اعزام ناوگان دریایی به محدودۀ تنگۀ هرمز و نظارت بر کشتی‌های فعال در جادۀ ابریشم دریایی مورد استفاده قرار می‌گرفته است.
🔹
این کشف نشان می‌دهد حکومت‌های ایرانی از دورۀ اشکانی، برای حفظ امنیت مسیرهای بازرگانی و کنترل یکی از مهم‌ترین شاهراه‌های تجارت جهانی برنامه‌ریزی و سرمایه‌گذاری کرده بودند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/439762" target="_blank">📅 05:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439761">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e7aa4433f.mp4?token=aw0i4HWtJIx3yeBfBH6dT88oYHz9pHju-6XUwJloaZc_iRPzP14qlYNp4SLiNLcWH-CN1G_50o8euCK1weVpz09zVf7PIS__JmeJLd__7XLhs2a_RsKSe-Gl5Rky3_WqNXWZhlyETBor2o9G2GiJeh8eWHkTEhecRuPBuWV4NLioK_AG1yyABO5N4byue8cPdxTHD6hPoIbRHMvGEqwxBJR5jfJ8eQBuqAveZDVRz9Q5aa7vyS52Lke6WRZ2Vmrguejgz4sURAC_xPYPCL2WlqvMrYjAmNDVUSEDbqSPLbTS8Y99GYGk4ufVm6fo53bgfy3fnf5AFQ5wVYVY5ckHng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e7aa4433f.mp4?token=aw0i4HWtJIx3yeBfBH6dT88oYHz9pHju-6XUwJloaZc_iRPzP14qlYNp4SLiNLcWH-CN1G_50o8euCK1weVpz09zVf7PIS__JmeJLd__7XLhs2a_RsKSe-Gl5Rky3_WqNXWZhlyETBor2o9G2GiJeh8eWHkTEhecRuPBuWV4NLioK_AG1yyABO5N4byue8cPdxTHD6hPoIbRHMvGEqwxBJR5jfJ8eQBuqAveZDVRz9Q5aa7vyS52Lke6WRZ2Vmrguejgz4sURAC_xPYPCL2WlqvMrYjAmNDVUSEDbqSPLbTS8Y99GYGk4ufVm6fo53bgfy3fnf5AFQ5wVYVY5ckHng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای شنیدنی هدیۀ امیرالمومنین علیه‌السلام به علامۀ امینی!
@Farsna</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/439761" target="_blank">📅 05:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439760">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca2b00b797.mp4?token=fE4TxE8fSSVF2_cPNV6bLIvZbJ_TpWJnGLSICzAiienAhgGJCHTTThgFDbutUWknLCU6v9yEZHsWPzAGbaXDKO4mwjc0lcJxCy0AopjHHrYmHsx3ChNtk_5PVF3EMA5Ta-iPLqOrSg8MI6vU8dZ_Y2kxSqeHzVL9WQi6DKk_3Ae_2azeqHeDr1I50FbR7InUojPOHBBUCVlSxFhD7ED5u2CLRbUwH22GAN6qHBfztfSZj1v4lbQbAyEtXa7B_x0MZtKrql3QC1D-QHHUI3YezAxmBxGFEc4MNFxywQIkk99SZ-1IAFtSVO_kxJ8zMypq1rJBOzwcS6SDfmc48aiKTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca2b00b797.mp4?token=fE4TxE8fSSVF2_cPNV6bLIvZbJ_TpWJnGLSICzAiienAhgGJCHTTThgFDbutUWknLCU6v9yEZHsWPzAGbaXDKO4mwjc0lcJxCy0AopjHHrYmHsx3ChNtk_5PVF3EMA5Ta-iPLqOrSg8MI6vU8dZ_Y2kxSqeHzVL9WQi6DKk_3Ae_2azeqHeDr1I50FbR7InUojPOHBBUCVlSxFhD7ED5u2CLRbUwH22GAN6qHBfztfSZj1v4lbQbAyEtXa7B_x0MZtKrql3QC1D-QHHUI3YezAxmBxGFEc4MNFxywQIkk99SZ-1IAFtSVO_kxJ8zMypq1rJBOzwcS6SDfmc48aiKTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برپایی بزرگ‌ترین شهربازی دنیا در روز غدیر تهران
🔹
بزرگ‌ترین شهربازی دنیا در مهمانی ۱۰ کیلومتری روز غدیر برپا خواهد شد. برای درک ابعاد این رویداد نگاهی به بزرگ‌ترین شهربازی‌های جهان بیندازیم. مثلاً خیابان اصلی «مجیک کینگدام» در دیزنی‌ورلد حدود ۱.۵ کیلومتر طول…</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/439760" target="_blank">📅 05:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439759">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqy4xNZqeSRlehtK4aOgB7oPgs1Skyti1Y-bZSAskuOn4Xa3lZkDgMfIvxu9B4ZfbYDID8FKNrmnHdFEQgIivp2W-UHDyTD64A_WhGeMRccS1iQLfkaJkI2y8bMoyx_QJiuhkjjzU5hO_s1Su9FXbMZFJ8E9fEdPPWWoJ5K_d8e4czY-SG7TYTHCkdLX5kfKNWdE716_G42q2xam6eBkZsHtKo77A0PkIFmzD5yggCGHG1aP0ytT3xwjJXrZ9pUsd8ARQmpdb_MNpiJYvP43I44veoF4fuRoFYxuk1dYOaoZgs60Vi_F91Cgfp8TalKWw1hyjHKw7Ar7xSYa2N2uLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیرکل نجباء: سلاح مقاومت خط‌قرمز است
🔹
شیخ اکرم الکعبی: همه بدانند که سلاح مقاومت خط‌قرمز است و این، امانت شهدا است که با آن، اشک چشمان مادران داغ‌دیده را پاک کرده و دل‌های داغدار مومنان را خنک می‌کنیم.
🔹
با این سلاح بود که ما عراق را از وجود داعش و اربابان آمریکایی آن پاک کردیم و تا جان در بدن داریم، آن را تحویل نخواهیم داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/439759" target="_blank">📅 04:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439758">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8hE8hgOM15SaqTXpPyrZBxazmQWUz4BaunyKcn0OAfq337oCP96B_ageoEM1afrbIlTDoWolJmonUC5X7L3WGgU4ESWnHGZpzAEE0FFqSwo40-jxhmFokgI3RBLzY01sKB0WIeNkNtCHc_BS5Xm2MJk8xIuTEBY03Co5ND0NJaNbmMO2pWeHQc0zxOaTjeTpwsJKvUzBK5FchbdJVUVrzXngYQ4E0wPM9YHdqvc_R9zD-hynVGiqsrDnHn0WZJdN7gKMHTZBMoNOZNJRqGrTcgSjDwbdHuMA3asKYNxRC1t1xM4q31pb2tGLXBZMEykrOeeZa9JNhIpPz0SLVq9Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات هدف مشروع دیگری برای ایران می‌سازد
🔹
نشریۀ فایننشال تایمز در گزارش اخیر خود تایید کرد که شرکت ملی نفت ابوظبی درحال برنامه‌ریزی برای ساخت خط لولۀ جدیدی با هدف دورزدن تنگۀهرمز است. این خط لوله قرار است صادرات بنزین و گازوئیل را فراهم کند.
🔹
در فراروایت این خبر، نتایج مهمی وجود دارد، ازجمله اینکه کشورهای عربی می‌دانند قرار نیست وضعیت تنگۀهرمز به قبل از ۹ اسفند بازگردد؛ درنتیجه به‌دنبال جایگزین آن هستند.
🔹
اما ایجاد چنین خط لوله‌ای، یک هدف دردسترس و کاملا مشروع دیگری به ایران می‌دهد که می‌تواند در تنش‌های بعدی هدف قرار بگیرد.
🔸
دورزدن تنگۀهرمز، پروژه‌ای است که سال‌ها پیش طرح‌هایی برای آن ارائه می‌شد؛ اما تمام آن‌ها به شکست انجامید. هرگونه دورزدن تنگه، درنهایت انتقال انرژی را به دریای سرخ می‌رساند. جایی که بازهم دست ایران برای کنترل بر کشورهای متخاصم باز است.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/439758" target="_blank">📅 04:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439757">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">مقام حزب‌الله: هیچ طرفی نمی‌تواند مقاومت لبنان را مجبور به خلع سلاح کند
🔹
محمود قماطی، نایب‌رئیس شورای سیاسی حزب‌الله: تمام تلاش‌های آمریکا و اسرائیل با شکست مواجه خواهد شد. رویارویی ادامه دارد و مقاومت در برابر تجاوز اسرائیل همچنان پابرجاست.
🔹
آمریکا و اسرائیل هیچ حقی درمورد سلاح‌های مقاومت ندارند، زیرا این یک موضوع داخلی لبنان است که ما درمورد آن توافق داریم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/439757" target="_blank">📅 03:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439756">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ادعای آمریکا دربارۀ موافقت لبنان و اسرائیل با آتش‌بس
🔹
وزارت خارجۀ آمریکا بامداد پنجشنبه مدعی شد که رژیم صهیونیستی و لبنان با آتش‌بس تحت نظارت واشنگتن موافقت کرده‌اند.
🔹
رسانه‌های آمریکایی گزارش دادند که چهارمین دور مذاکرات بین نمایندگان دولت لبنان و رژیم…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/439756" target="_blank">📅 03:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439755">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">ادعای آمریکا دربارۀ موافقت لبنان و اسرائیل با آتش‌بس
🔹
وزارت خارجۀ آمریکا بامداد پنجشنبه مدعی شد که رژیم صهیونیستی و لبنان با آتش‌بس تحت نظارت واشنگتن موافقت کرده‌اند.
🔹
رسانه‌های آمریکایی گزارش دادند که چهارمین دور مذاکرات بین نمایندگان دولت لبنان و رژیم صهیونیستی در واشنگتن به پایان رسید.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/439755" target="_blank">📅 03:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439753">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🎥
شکر خدا که نام علی در اذان ماست
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/439753" target="_blank">📅 03:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439752">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">حملات موشکی حزب‌الله به مواضع صهیونیست‌ها
🔹
حزب‌الله اعلام کرد مواضع دشمن در جنوب لبنان را با موشک هدف قرار داده است.
🔹
همچنین یک پهپاد اسرائیلی را با موشک زمین به هوا در جنوب لبنان رهگیری، و مجبور به ترک منطقه کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/439752" target="_blank">📅 02:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439751">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d86d1c07d.mp4?token=rzhZa6cYWMx1c8v-GYQ8f3ivTDyz_Xfa1RBPKroTUaAhY1Bun9Bdnxq4dbLzxnlzedWJNL2RyLUiFFpGnChH_5W_-tkqhjmMJwwRZRCkQKYVOWB_2RvBLMMkKAlCETx7-ZUWCb1lNUH1ufJxL_i64J7misIvYPuFJIs3tF2_gLwiWJVNUUrKxhr0bsVQsnxQfRUwj-nwnPy48QrpB2XOMWZEWryUSb-tVX2EXLEj2L5x_fuSOiKqpnuRhDwgQ_jKZq8IkvnxD7nYI-RcF5ajf7nvOfYOPOipXNg7DV091ZagM0pWh46QbReB4z7Fv5yPgIiBV3LnF7I9I5oU-5nR-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d86d1c07d.mp4?token=rzhZa6cYWMx1c8v-GYQ8f3ivTDyz_Xfa1RBPKroTUaAhY1Bun9Bdnxq4dbLzxnlzedWJNL2RyLUiFFpGnChH_5W_-tkqhjmMJwwRZRCkQKYVOWB_2RvBLMMkKAlCETx7-ZUWCb1lNUH1ufJxL_i64J7misIvYPuFJIs3tF2_gLwiWJVNUUrKxhr0bsVQsnxQfRUwj-nwnPy48QrpB2XOMWZEWryUSb-tVX2EXLEj2L5x_fuSOiKqpnuRhDwgQ_jKZq8IkvnxD7nYI-RcF5ajf7nvOfYOPOipXNg7DV091ZagM0pWh46QbReB4z7Fv5yPgIiBV3LnF7I9I5oU-5nR-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دل‌هایی که مبدأ قدرت متصل بود و دل از ما ربودند
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/439751" target="_blank">📅 02:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439750">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R58gEoxqQUr0RXnIsS_wqvkF2B8JHi4k0q9olkgdxBuZUjDeYgQp_FkMnV4u24VP_GUbXmkqY6f-ys9Q_rHIdI0I5M7zQUkyh2PjRbIsAnonmNhwdvTunMA6JqMgDQDGYoQ6-BsBKa09xemw4bDgliYghSl-Y30_4nbrhYMchjQunVetPjwhaMs-npKXSZ-ly_9LAzBQ394tZRxuEAw0-HyNQdEVxOCBpNxXKQJWcs38DLRke8-7hmy_ENAJmHxZyEHzccvSpre0C4grZ1FuPPVgsX4mGBQwVJizKmDT8KOtzIBEhgcHNRGW1ib5pSvPwg-2giLdjduVzNmAkHkYGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آهسته برانید؛ «هلیا» و توله‌هایش از جاده مرگ می‌گذرند
🔹
در حالی که محیط‌بانان حیات‌وحش این روزها چشم به تحرکات هلیا و سه توله‌اش دوخته‌اند، محور عباس‌آباد-میامی بار دیگر به کانون نگرانی دوستداران محیط‌زیست تبدیل شده است.
🔹
این جاده طی سال‌های گذشته بارها به قتلگاه یوزپلنگ آسیایی تبدیل شده و حالا ترس آن می‌رود که یکی دیگر از خانواده‌های ارزشمند این گونۀ در معرض خطر انقراض، در مسیر عبور از آن با تهدیدی جدی روبه‌رو شوند.
🔹
برآوردها حاکی است حدود ۵۰ کیلومتر از این محور ترانزیتی در محدودۀ عبور اصلی یوزپلنگ آسیایی قرار دارد، بنابراین نقش رانندگان در کاهش خطرات و حفظ جان این گونۀ ارزشمند انکارناپذیر است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/439750" target="_blank">📅 01:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439749">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd4aeb0d1.mp4?token=PghnY9aQp2FPZzXfIQSR1K5qz9BhrB_mo28XP1L0NAQrI4IuE55wDehIJ-OoLzLwfxv1yx9X5x0i5RuZ2-UV141nJQiWHdsLlNdHN_ULtuWRMVtNQaCkCJkwha4c2BRPAxzI5HjXsdlwtTpxSMSlbAc3xHctVyPfUaZHP42D8UWSpdykPcfhnV2ZQ0Gzk7CG6SRIHF92R0I7choG5ga4_05VPFKKauSHW5H4qseRQeBRbkE2aUy5AThWR-aRt5gSULyv3DZ0UnLFpk3uJrzt8TDvS9EEfLUCOfhdYiwutIhRjO0_h38KEmo7Z7jlQTnA-GgFniueaFHvFtuqPYu-Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd4aeb0d1.mp4?token=PghnY9aQp2FPZzXfIQSR1K5qz9BhrB_mo28XP1L0NAQrI4IuE55wDehIJ-OoLzLwfxv1yx9X5x0i5RuZ2-UV141nJQiWHdsLlNdHN_ULtuWRMVtNQaCkCJkwha4c2BRPAxzI5HjXsdlwtTpxSMSlbAc3xHctVyPfUaZHP42D8UWSpdykPcfhnV2ZQ0Gzk7CG6SRIHF92R0I7choG5ga4_05VPFKKauSHW5H4qseRQeBRbkE2aUy5AThWR-aRt5gSULyv3DZ0UnLFpk3uJrzt8TDvS9EEfLUCOfhdYiwutIhRjO0_h38KEmo7Z7jlQTnA-GgFniueaFHvFtuqPYu-Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با فرزندان اپستین صلح نمی‌کنیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/439749" target="_blank">📅 01:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439748">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4FvcJy0FX7WfpkqwiaAd-vrkiEpVNpc9PsaWwX6KQHFyHDukeu_rytM3Wwui_vfRu0VYYIxYck02FQRvBopdh7B2sMnICQx_GJ1CQKY9GCvzGhNUySnfC1VjYPA4GMAFWw6nd0ZLJvIyWd1259kwVdHTHdj8CQkrorDjIJWqIgFUBjv_XIAqzgx6tFZwdI0wPSJXj2V3n_OvdYBeMxMYgVxSp7dNDrzXhH5KVQVJug-ap_lY4A1WusvWeG0miSt6HHO5Pkn3Xz3GJmjKFSvk5Jd4Pba9kYaLg90TLD_4aSLS5r3OyWxyymVzQ3pztIlFNQ-rbWQHn5XOM81yLZK1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویب قطعنامه‌ای در مجلس نمایندگان آمریکا برای پایان جنگ با ایران
🔹
مجلس نمایندگان آمریکا بامداد پنجشنبه قطعنامه‌ای برای مجبور کردن رئیس‌جمهور این کشور به خارج کردن ارتش آمریکا از جنگ با ایران تصویب کرد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/439748" target="_blank">📅 01:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439747">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15dfcd9da3.mp4?token=GIjAO2bntXNVlW3HM-lPUnF8wk2mBgjY9Z2pIMs3skEN_WzJPS_UQtojxTu9_xN7IgzAheQiFu-RlBsVD2A_OyynsnX4yoatVdfzCkQESeiugC4lsFdatQpaUexR60xc_4k8fDbmZ5vCFARzjbJaxW--XfQrY1vMoTXCMPO8ZwzzUIqD5weSjNaT37GyQi8kRQ-6YUsJ1mFvTge3Oxu783Lcc4LKDWgmz2QudnzBLl6rpe_RVnXxVHNg3ODSqI-2rJO5DcP2e2HV4lGiySzQ_iOcpSEXtbxcnBYZLe1kWdbdNl7poY2V00g_ZYPj9hpvMLouxPoN2SeBRivOAF-U5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15dfcd9da3.mp4?token=GIjAO2bntXNVlW3HM-lPUnF8wk2mBgjY9Z2pIMs3skEN_WzJPS_UQtojxTu9_xN7IgzAheQiFu-RlBsVD2A_OyynsnX4yoatVdfzCkQESeiugC4lsFdatQpaUexR60xc_4k8fDbmZ5vCFARzjbJaxW--XfQrY1vMoTXCMPO8ZwzzUIqD5weSjNaT37GyQi8kRQ-6YUsJ1mFvTge3Oxu783Lcc4LKDWgmz2QudnzBLl6rpe_RVnXxVHNg3ODSqI-2rJO5DcP2e2HV4lGiySzQ_iOcpSEXtbxcnBYZLe1kWdbdNl7poY2V00g_ZYPj9hpvMLouxPoN2SeBRivOAF-U5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از نماز با فضلیت روز غدیر غافل نشوید
🔹
در مفاتیح آمده که اگر می‌خواهید برایتان بنویسند که در روز غدیر حاضر بودید و با پیامبر(ص) برای ولایت بیعت کردید ۲ رکعت نماز را بخوان.
شیوهٔ خواندن این نماز را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/439747" target="_blank">📅 01:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439746">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYNQJZqmVExK38lIP7WMYsK0g9xYvf1ewZSMNOID40QDur9Aoxk1VukwD44eio3daHLWWGnOYJ49VtrHCvvbGtONowVSPHww51d6m51HBS-XnNSNPWCKMF7kEKH2Aw9Jw_Hu8r6UI8neR6uVCM274x1bw5LZsrb_Cm23hiiqgA5xmcaa_9wVX2J8rq-JdN-ChqsU1YbiUmKdkxIm9rLSbGtkAoyI-fs2D49MSwKYL8k-XW2BPbUcAi_YwQv18ImfkVlJc4DzGCGmBIuaf9yH1aEvn2ijrsMzcFAq-NtZo7auhgS7WlIONe373L-Efrm_GevqyJpQsUhbOPhq_3MkCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
برنامه اصلی مهمانی ۱۰ کیلومتری غدیر در میدان انقلاب اعلام شد
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/439746" target="_blank">📅 00:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439745">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8CtPsWNRPYUjTBpNR-jHTMBnJTacSfjF9rzxPxRQRfI9kKzlVna8GZSYHHpj_U7HpUTDNao6XrvO_80IX2EkQSwBx73pTHWknHgOJOwD8M6bg9IRO1Qjd8cczUG8OnAwxCKAMJKRjp7o2TPjMSLyREK8wf2U0iYSKrRH6T13h1bttSHBube137W8TRHn6EltunclQ8Y2tt45qHsic8LQ7cAsjj8SFn_rDQ5eI8n5NfTlOWcP1HJpoSlFw8HRzgzDrQP6aYDh8AGuiUeOa2RvMuD5GrjOhy9YQBnypXbrcl5MD_UeVnZUAtuIBszZncIXiR-yuVAXX-_bpMB0cE7hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گل‌محمدی، در یک‌قدمی سرمربی‌گری دهوک عراق
🔹
در شرایطی‌که طی روزهای گذشته اخباری دربارۀ مذاکرات یحیی گل‌محمدی با باشگاه دهوک عراق منتشر شده بود، از دقایقی قبل برخی رسانه‌ها و صفحات خبری نزدیک به فوتبال عراق اعلام کردند گل‌محمدی هدایت این تیم را برای فصل آینده برعهده گرفته است.
🔸
بااین‌حال تا این لحظۀ باشگاه دهوک به‌صورت رسمی از سرمربی جدید خود رونمایی نکرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/439745" target="_blank">📅 00:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439744">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b7a8c1d97.mp4?token=GYivAB5t0e62Q6lXkJLZS7SonDPtE6kLv8R7_o5-zF-ahmL9aJB1tD2fKOo6E1EAOFUwuzhaVWBsQyM2KGryx4RlkaB6wYLSEyzAh2tks_8SsMd_8IKA0gKiTC9cw_2vvyO8M-vlNGHyw52ryrrq0X1RgNrDDZSfjwPR-s3hGe0q3KEgg8fXqb3tnoLuvAgQgFeISNZNQvOarZrRX1KGnFpoFc9QPf0BTUnd2eCmga6wxVKGnoBS-CCIGPLoBtjVgSCnBigrX6F6HvUEUv5CjOoo8F-0i5kwrfMaxownObTUIVoqdJc-0-1yE9DvAgedUdLCooIgcENsGvga-ugOGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b7a8c1d97.mp4?token=GYivAB5t0e62Q6lXkJLZS7SonDPtE6kLv8R7_o5-zF-ahmL9aJB1tD2fKOo6E1EAOFUwuzhaVWBsQyM2KGryx4RlkaB6wYLSEyzAh2tks_8SsMd_8IKA0gKiTC9cw_2vvyO8M-vlNGHyw52ryrrq0X1RgNrDDZSfjwPR-s3hGe0q3KEgg8fXqb3tnoLuvAgQgFeISNZNQvOarZrRX1KGnFpoFc9QPf0BTUnd2eCmga6wxVKGnoBS-CCIGPLoBtjVgSCnBigrX6F6HvUEUv5CjOoo8F-0i5kwrfMaxownObTUIVoqdJc-0-1yE9DvAgedUdLCooIgcENsGvga-ugOGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: آتش‌بس یعنی شلیک ملایم!
🔸
خبرنگار: تعریف شما از آتش‌بس چیست؟
🔹
ترامپ: آن‌جا [ایران] بخش دیگری از دنیاست. متوجه منظورم می‌شوید؟ در آن منطقه از جهان، آتش‌بس یعنی زمانی که با شدتِ ملایم‌تری شلیک می‌کنید! @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/439744" target="_blank">📅 00:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439743">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">یمن: کشورهای عربی دست از مظلوم‌نمایی بردارند
🔹
وزارت خارجۀ یمن با تمجید از پاسخ ایران به تجاوزات آمریکا، تلاش برخی کشورهای عربیِ میزبان پایگاه‌های آمریکایی برای مظلوم‌نمایی و ایفای نقش قربانی را محکوم کرد.
🔹
یمن در این بیانیه تاکید کرده کشورهای مذکور با سیاست‌های احمقانۀ‌شان صدمات زیادی به خود و مردمان‌شان وارد می‌کنند و اولین بازندگان این نبرد هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/439743" target="_blank">📅 00:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439742">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab704aeadb.mp4?token=n3cSPgG6X8S1mZRP0qXp1v2q_EOFjPGfTxOp_AuxPekkgIjZVN82Hq5WLk94V83bFanVJBjO1Y7NOwTDadZy0Oqd404LOyNMYgovA2y0qHVjdch32A_SShB_w3JZJRiODeDPoeHoeaENXEkOkZKpia45myONvlTuUNKdU1FeNaK4za82ndtIU3rWjz1a8j8joX9b_XB2rs80bnkH4wRZhdjMg5NkCCyvwOgmKmXLROkhZPrfNpJwiEdExEnej9gictcyTa70VDE-werUIPxdeQnVLBCDES4n_BWEt1JhxqeTN31M2_kRWOtfoyNIVdmNrfhDotB932-NtXAQsEIpQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab704aeadb.mp4?token=n3cSPgG6X8S1mZRP0qXp1v2q_EOFjPGfTxOp_AuxPekkgIjZVN82Hq5WLk94V83bFanVJBjO1Y7NOwTDadZy0Oqd404LOyNMYgovA2y0qHVjdch32A_SShB_w3JZJRiODeDPoeHoeaENXEkOkZKpia45myONvlTuUNKdU1FeNaK4za82ndtIU3rWjz1a8j8joX9b_XB2rs80bnkH4wRZhdjMg5NkCCyvwOgmKmXLROkhZPrfNpJwiEdExEnej9gictcyTa70VDE-werUIPxdeQnVLBCDES4n_BWEt1JhxqeTN31M2_kRWOtfoyNIVdmNrfhDotB932-NtXAQsEIpQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: آتش‌بس یعنی شلیک ملایم!
🔸
خبرنگار: تعریف شما از آتش‌بس چیست؟
🔹
ترامپ: آن‌جا [ایران] بخش دیگری از دنیاست. متوجه منظورم می‌شوید؟ در آن منطقه از جهان، آتش‌بس یعنی زمانی که با شدتِ ملایم‌تری شلیک می‌کنید!
@Farsna</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/439742" target="_blank">📅 00:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439741">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22ad2b4c8f.mp4?token=Zl1kv_ifx8rpNYkbCPDSdQoIe7ij87VNr5uA1MVsFyfI8k66BbXRxErAjC7kpIfLYNkrXTAtt8CxuZIAqDKPNpRvRL-f24OgKH3xferXV3c-_EnS6fsLMZDwugpSXKESjQWcNBUA74wN5LuytPiAeGmvaWZPEzCDnV7EG2J-UJPGz3I2gOaJ67YCPMj5nIL0mjLvKyt9W8T7YZ2guwMvD2wmDV5Zt4xU0bpt_pSZdINzUXPJrsC8rpGRbgxi2Tf9tLH7-fdAbjqUO0iT5ij_3mq9uQTXkU1XbLZoA74fuMuLVDU8s-DGYGKbkZkVyBw_aDtMYh-fDuOJyqgM4KrEpx4Ehr1-UbdybLRNxcch6QfUp_0iQC1amYTlh6LXT0sboZEGJ8bWaiRJpQwR9nc9EwRquH-OYTJuYvG46vaQbsW_USZ8v0JSOi_G5BdC6JMQvaZtWkMHptQDTjRtcIsyOHwOcOogK5QQE02twyvd1_e4xrtpBzeAYwDIdyM7qf8ZfZmSY4MoRu_aSeRhIV2jB4MRZ1uROmeBEGAohFA52IlSRfZTgSrmvyYPN0Jp1q9_OOGoroRtZsxoLUuNTcv3k0umYbDpLyg8pFW6WbWzquPkhyCDeR78pzKyZjs6hMvrJkafVeium_rj2rGsQ2tF03NDIk6c64Rd_LdfddXPaM4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22ad2b4c8f.mp4?token=Zl1kv_ifx8rpNYkbCPDSdQoIe7ij87VNr5uA1MVsFyfI8k66BbXRxErAjC7kpIfLYNkrXTAtt8CxuZIAqDKPNpRvRL-f24OgKH3xferXV3c-_EnS6fsLMZDwugpSXKESjQWcNBUA74wN5LuytPiAeGmvaWZPEzCDnV7EG2J-UJPGz3I2gOaJ67YCPMj5nIL0mjLvKyt9W8T7YZ2guwMvD2wmDV5Zt4xU0bpt_pSZdINzUXPJrsC8rpGRbgxi2Tf9tLH7-fdAbjqUO0iT5ij_3mq9uQTXkU1XbLZoA74fuMuLVDU8s-DGYGKbkZkVyBw_aDtMYh-fDuOJyqgM4KrEpx4Ehr1-UbdybLRNxcch6QfUp_0iQC1amYTlh6LXT0sboZEGJ8bWaiRJpQwR9nc9EwRquH-OYTJuYvG46vaQbsW_USZ8v0JSOi_G5BdC6JMQvaZtWkMHptQDTjRtcIsyOHwOcOogK5QQE02twyvd1_e4xrtpBzeAYwDIdyM7qf8ZfZmSY4MoRu_aSeRhIV2jB4MRZ1uROmeBEGAohFA52IlSRfZTgSrmvyYPN0Jp1q9_OOGoroRtZsxoLUuNTcv3k0umYbDpLyg8pFW6WbWzquPkhyCDeR78pzKyZjs6hMvrJkafVeium_rj2rGsQ2tF03NDIk6c64Rd_LdfddXPaM4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم تهران آمبولانس آسیب‌دیده در حملات آمریکا و اسرائیل را گلباران کردند
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/439741" target="_blank">📅 23:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439740">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d79700139f.mp4?token=q1Z395e3USgUB0UpOkYFHCMF3IvHQQntDypQ6_UZ4-QTp4oMamhCuvS6l_zthuwLM_JE2Nk8wTWOZn-Qu9k9aB2fcoJYKDMGu4H_oDsLZHw2AfgCrLyQvmub5g6vimq3k03HGlDsrvqbF9iOavUxn8_WQ4ZbmPN6iPfACAQ7X3qNkaSi-U5rl1TnIUwkGKvfu9KZ8HjMofo4T8WomsOHMy2Sc15reTI9vXUI35Kf-vComyFfhQRJnx3N4zmyNNTWk5wkUIvF2WuisTGIHQIKGB3B45QNBaAISLPOqttQFEGXswmU84Mwvf6dw_v7aXNaLiyobHnT6pCQW1iRTKNO8Ij7yuhtXgrPO07NGnVMsaXS4DoIUyaVma-_NQBIzhIOBBnk9KfnGx3BTqPdBthN1oIAuUWw-3u6M30A0Z8l9esF5EH4FOo7dYwfZGdvJJCn4K2TU2qUeBf2-3QRUOUdm4jVDLv-2kjVisWVSf9z0kccXkOnEL0khpL6YcV6KBL1YiMtHzP267kLzZKJ1Jo2flwpphhvps0iDCG68zsLvRdwGa2Lvvr3PfjobtTGrxSls89Wckd7e9BymrYD_wHgVWm3r2gEciIkaka8TzXKfjKkAMc3m9xjPlGwXpvLRIN_UjFctJlkA-QBQ6XTfx3RA0G_hmF49hOGkBtKFjJpu2Y" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d79700139f.mp4?token=q1Z395e3USgUB0UpOkYFHCMF3IvHQQntDypQ6_UZ4-QTp4oMamhCuvS6l_zthuwLM_JE2Nk8wTWOZn-Qu9k9aB2fcoJYKDMGu4H_oDsLZHw2AfgCrLyQvmub5g6vimq3k03HGlDsrvqbF9iOavUxn8_WQ4ZbmPN6iPfACAQ7X3qNkaSi-U5rl1TnIUwkGKvfu9KZ8HjMofo4T8WomsOHMy2Sc15reTI9vXUI35Kf-vComyFfhQRJnx3N4zmyNNTWk5wkUIvF2WuisTGIHQIKGB3B45QNBaAISLPOqttQFEGXswmU84Mwvf6dw_v7aXNaLiyobHnT6pCQW1iRTKNO8Ij7yuhtXgrPO07NGnVMsaXS4DoIUyaVma-_NQBIzhIOBBnk9KfnGx3BTqPdBthN1oIAuUWw-3u6M30A0Z8l9esF5EH4FOo7dYwfZGdvJJCn4K2TU2qUeBf2-3QRUOUdm4jVDLv-2kjVisWVSf9z0kccXkOnEL0khpL6YcV6KBL1YiMtHzP267kLzZKJ1Jo2flwpphhvps0iDCG68zsLvRdwGa2Lvvr3PfjobtTGrxSls89Wckd7e9BymrYD_wHgVWm3r2gEciIkaka8TzXKfjKkAMc3m9xjPlGwXpvLRIN_UjFctJlkA-QBQ6XTfx3RA0G_hmF49hOGkBtKFjJpu2Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جشن باشکوه یمنی‌ها به‌مناسبت عید غدیر در صنعا
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/439740" target="_blank">📅 23:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439739">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cfac4c46c.mp4?token=KPOeOYO8lFL3XYt8Nhn4AXeXegJrexpfhrfgyrATnILqoZgub9er93SYVi9pjUeDleAoJwQYI5e9yiNRqkqMjPH54ZjrNGTsuQI5KMytXMEEmU-6O3c68YCTnXf4ed2jlob4nAFLxfPvZEhCuxXi8XnNNtppoiLhbbrgNs5oYAUhutI_0jis_favPtb6dn5bNB9piP71C0KHxeo8YZqOpgLer44f0HrkjQiRqEGfgvCYmpYzCW0PbifPPiBU9TXvlNnynkCjOi_bzqpD8OspCakEPl7zQNhJu--9cpeCeahxKMEKQ5coe5aA2rU7fL1phTKsaV4FpZOTkXeeYd7p4zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cfac4c46c.mp4?token=KPOeOYO8lFL3XYt8Nhn4AXeXegJrexpfhrfgyrATnILqoZgub9er93SYVi9pjUeDleAoJwQYI5e9yiNRqkqMjPH54ZjrNGTsuQI5KMytXMEEmU-6O3c68YCTnXf4ed2jlob4nAFLxfPvZEhCuxXi8XnNNtppoiLhbbrgNs5oYAUhutI_0jis_favPtb6dn5bNB9piP71C0KHxeo8YZqOpgLer44f0HrkjQiRqEGfgvCYmpYzCW0PbifPPiBU9TXvlNnynkCjOi_bzqpD8OspCakEPl7zQNhJu--9cpeCeahxKMEKQ5coe5aA2rU7fL1phTKsaV4FpZOTkXeeYd7p4zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جشن خاطره‌انگیز شب غدیر در پیشوای تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/439739" target="_blank">📅 23:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439738">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f019ceaf5b.mp4?token=Hu3ZtOTJmLtBAaYCRBiiuTocl9BbvHVTlgisJuEjrKYLQyUKgc6MkOQNN5GcpjY9QwfIB4n1CxLad8DkxRKKKzxdivtb97ssjw5oqUyPQ09hovDexFZ7FyLe6psqFl9exn8XSyGDKzpbwQqG5jHc8XmmBlSComg6XBLj5Dv1rene81HmMMOmAeI9egSugXFZ2djPKpEUqZBHJjB4FsgFTlKouGfm-TKE9IkY1bPF0dB-lOQzDs9B-D__CsGIFFnsmNKuzppOAnQncW97gLQmXub8C-rkJKmRsZoxZfdf1J-EPz8CYzNGSYd2zZqMLVYopsyKOhZofLzwmUvuvBt-QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f019ceaf5b.mp4?token=Hu3ZtOTJmLtBAaYCRBiiuTocl9BbvHVTlgisJuEjrKYLQyUKgc6MkOQNN5GcpjY9QwfIB4n1CxLad8DkxRKKKzxdivtb97ssjw5oqUyPQ09hovDexFZ7FyLe6psqFl9exn8XSyGDKzpbwQqG5jHc8XmmBlSComg6XBLj5Dv1rene81HmMMOmAeI9egSugXFZ2djPKpEUqZBHJjB4FsgFTlKouGfm-TKE9IkY1bPF0dB-lOQzDs9B-D__CsGIFFnsmNKuzppOAnQncW97gLQmXub8C-rkJKmRsZoxZfdf1J-EPz8CYzNGSYd2zZqMLVYopsyKOhZofLzwmUvuvBt-QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ما باهم برادریم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/439738" target="_blank">📅 23:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439737">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e8a90399b.mp4?token=ScQro4eiTnmyBINATHuFGNxX4eSFnw8JR27sYR9ckB949vnaUFNsDIe6X1Abh_czNYyoxzzQmhTjhbqsEDPQQkHj3qvL2lepxVsjcdVRvkX1NIK-ur7Q3bEWVHQX8Uw8yEV-kzymp7kU9WcHXTQs8dDCVFOWoql8jHQiOlop8c75u_U-n9_GZTJ8nlUYkLYSpYv8uThnIlU61vpd1j807U847RDVduBXZQNJsjm5iCoVhOTFghtPjTzpokR1kr9UySSDEr_YKfD7zLjJLmU9x877g_b08lil-6eySraObdq-cHt_0daiiq9cpVo4HfxCwOpk-0ZFvTNIFpdRX32_3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e8a90399b.mp4?token=ScQro4eiTnmyBINATHuFGNxX4eSFnw8JR27sYR9ckB949vnaUFNsDIe6X1Abh_czNYyoxzzQmhTjhbqsEDPQQkHj3qvL2lepxVsjcdVRvkX1NIK-ur7Q3bEWVHQX8Uw8yEV-kzymp7kU9WcHXTQs8dDCVFOWoql8jHQiOlop8c75u_U-n9_GZTJ8nlUYkLYSpYv8uThnIlU61vpd1j807U847RDVduBXZQNJsjm5iCoVhOTFghtPjTzpokR1kr9UySSDEr_YKfD7zLjJLmU9x877g_b08lil-6eySraObdq-cHt_0daiiq9cpVo4HfxCwOpk-0ZFvTNIFpdRX32_3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خرم‌‌آبادی‌ها: ما پیرو غدیریم، ذلت نمی‌پذیریم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/439737" target="_blank">📅 23:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439736">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54d945556a.mp4?token=IqBIHeXmiv8nPs0yhFuFvpHwzx-X-SUvwQEZk8exW5qkYSBfyE0PRttNqgzWHMwjqlF0x3_7j32TIHY6ExOplTJPV9bm2THAl0k3sY5pEkXJybDOsbBjh3CVTBXIt4JWUzxG2Wg1KHpwA7Va7Xu44CSMw2N9QtTMw1Y1SqrwKM77mjiKlqy894_yPwyS3s1jBk5TGOcXmq0sV0FFeFWzJ-laFUWgYHFC5bk8NshlVnQovj5-LkPDpsVh8DUdXDNFNo9hatS1j3DoIL6nx-zaMR1vw3TNo6jMvptDQjjFSBeC0ljh727UM40fwKfLrlK50_q2NfE8cvyWgHt6FkIkPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54d945556a.mp4?token=IqBIHeXmiv8nPs0yhFuFvpHwzx-X-SUvwQEZk8exW5qkYSBfyE0PRttNqgzWHMwjqlF0x3_7j32TIHY6ExOplTJPV9bm2THAl0k3sY5pEkXJybDOsbBjh3CVTBXIt4JWUzxG2Wg1KHpwA7Va7Xu44CSMw2N9QtTMw1Y1SqrwKM77mjiKlqy894_yPwyS3s1jBk5TGOcXmq0sV0FFeFWzJ-laFUWgYHFC5bk8NshlVnQovj5-LkPDpsVh8DUdXDNFNo9hatS1j3DoIL6nx-zaMR1vw3TNo6jMvptDQjjFSBeC0ljh727UM40fwKfLrlK50_q2NfE8cvyWgHt6FkIkPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت بغض
‌
آلود دیدار بانوی لبنانی با رهبر شهید پس از شهادت
سید حسن نصرالله
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/439736" target="_blank">📅 23:30 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
