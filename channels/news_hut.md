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
<img src="https://cdn4.telesco.pe/file/ohJkvxcbBl1svpoh22ptzIfbPgMl0XMzaWEmrgsnZJpNTCho_HFgis0_dxAbh3Y2ik5ra_6q4R82w0G5X_lEXfsI6FBzaDDr-iWzY98DJLGisDiRf60yITCO8Y23QuXs07LIvJNJAhJArDVCpDaUtvHmk3xm-IUlIMU6dv5z2Bj6lTU59IOBsdUAQgEpIZabcT234PBD4LTbLb0Kr5lQTqNS169P_I_l8enRSHcgAOfKXvIAHjbYmXeVVyor4C25gJhOrbN7m177UJIN8TcIgIMTu7Lcn52Nefzy8412r1EZdgBPLdI2UKl_zfvwkULqxea8V3CUxtKjJNwF7BZd6w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 222K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 17:23:16</div>
<hr>

<div class="tg-post" id="msg-66502">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
سخنگوی ارتش اسرائیل:
منطقه امنیتی در جنوب لبنان ۱۰ کیلومتر امتداد دارد و ما به تقویت نیروهای خود در آنجا ادامه خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/news_hut/66502" target="_blank">📅 16:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66501">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMRD-t6PBfy7eytlQbbinwERlnBn8nZgo8mdP0zxWMKEbxlkWYBsmBtxEKxD54DPUxri1PzXMf4IR_3mqeyXNTePBMycdrYQRgWzNwDvsSxLLBlxi-o9F0s3_iGWd34xXbprpR9o2ZfHOnJQ18boaDZ-VfLsCpMHJjTko_Or5jIMRzsVzGWx4269eY3H_f2PPsMAbfkPSLhaE27IDrYxBkN6kvqIQphvBMaL70y5f0Mg6rCZis-JuW2WG8S2TPAeXJihKcay9xFTd0DjJw9FirKAwThISaS_w8Ax6vd3mMYETUonLlpUFgmIqhd1bwfVjta3hlcUBChnjUtqyayA1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اتاق جنگ اسرائیل:
اسرائیل و حزب‌الله به توافق آتش‌بس جدیدی دست یافته‌اند. حزب‌الله از توقف بمباران اسرائیل و پایبندی به توافق‌های آتش‌بس قبلی خودداری کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/news_hut/66501" target="_blank">📅 16:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66500">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxweJoc7pnH1g5r-5om4cwKmhniY6Uv3YjN6yqLTV3gR696-rFvYWjGiLtD-3LQRCHYJAgn3PCEkykrOH0fQweyQqyb1eURMriRk1cWYEXxTrpkq9jsHatAKCHk1Mi7RDHQidIqdzZIdoI3UHucaYiDGA9dVimPC693vmTNbQHdf6PF9hyjEMZgwX4N1lJUNFh09YC1ULXu2ZZG6iRyV8rP171WOhevJv4OoYPBodbBgfC3qG9rcytGpudud2Wx4Bh08Em87ccbI8JMP_Z9sQoEpLIqC0H33OqQBjU0t6XzjtUjTp5vHjSIVu0cTB0FQG4TAo5ZSYf9mWfXa7QPAhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید:
یک مقام ارشد آمریکایی به من گفت: اسرائیل و حزب‌الله بر سر آتش‌بس مجدد از ساعت ۴ بعد از ظهر به وقت اسرائیل توافق کرده‌اند. این توافق جدید با میانجیگری آمریکا و قطر پس از مذاکرات با اسرائیل و ایران حاصل شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/news_hut/66500" target="_blank">📅 16:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66499">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eii3Y-fa_VmtsNkpFOXmBuM8mEUWs9N7B0S_E4thJeZ_10tAuM5maZIyl8PU9ELiC4_Wfo7AmrlXl0RjM7GAMT7K-3MSbMaPvrUeTSrIzVaM1SxeEp3a_7Iu9Gaeqk4CDjyNZU2O0z043OWfY830d8z403_7prJDT8wkIVn8itaYiD7EB8P96_JOSjwtj_0BZYf7W0v9P0b8X7XdqVXF9woFkEn1Wb7mKFjlxxKsNIXAYTHVNvgI1C767qZhPyQu9AggHhcnjO-oDgvY0NL1JVHBdvuwWPkJe3J8F_9YIyxMxmXH4qNWi2IKFxBUaJ6DdV_0mBsHF1_uDIr_-pl_hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما از روی ناچاری ملاقات نکردیم، ایران این کار را کرد. آنها کارشان تمام است! ما 60 روز را بازی خواهیم کرد. آنها نه پولی می‌گیرند، نه ده سنت!
@News_Hut</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/news_hut/66499" target="_blank">📅 16:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66498">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECXuZOVxCW1Yaat6htAQNo9MjlERNgFrtfU1ZFgicGtX0W_nvS7vpwBCvVtB27jaLWoKBgCXShWY3PNTcRhMLUboTtwVP2cuHbzXv-Ips50RibgdGy58i85Xe_lN95VgDunsHJkmfG0QLzDZc2VwpknkJDrd1fw9BS4UyWz0UczRJYpokg7NVv6AGoNj_z12FLd9akKOr4LJunFrj5-5rM-JVSlHqFnt_lbe_J4K-zK_qh3TJkiJnpPSIcW_GdMQCM2DzR3aYJ7AxmX3COWDVSXu6Yo7DqFLsED-CohjQo2XNfp7OO-Ep1g4W2DZ432H5ih5cNW8l7YrVE-3t99FNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
این جنگ ایران را تضعیف کرده است! ایران دیگر نه نیروی هوایی دارد، نه نیروی دریایی، نه تجهیزات پدافند هوایی، نه رادار، و تقریباً هیچ چیز دیگری. با این حال، دموکرات‌ها می‌گویند ایران اکنون نسبت به چهار ماه پیش وضعیت بهتری دارد.
می‌توانید تصور کنید که کسی چنین حرفی بزند و از آن جان سالم به در ببرد؟ بعضی‌ها واقعاً تا چه حد می‌توانند احمق باشند؟
@News_Hut</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/news_hut/66498" target="_blank">📅 16:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66497">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
‏اسماعیل بقایی سخنگوی وزارت خارجه:
آمریکا مسئول حملات اسرائیل به لبنان است. جمهوری اسلامی همه تدابیر لازم را برای صیانت از منافع، امنیت و حقوق خود و متحدانش اتخاذ می‌کند
@News_Hut</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/news_hut/66497" target="_blank">📅 16:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66496">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXn3S1slJUkjN1nUQxIl_a4ei5ekUsnVC1Px_gvlOtZ83htimbt3GjYDEYOfsIirzvK-0hXEEn0hhTJK85lRPWD2-vZ7U8Cip11Olf7-lysjtQ3Ge4HpiWiefNIIguoSa-BSIj4KrlL9tGqvvs7UMpMW5w16aS8m9xWrSbTcCH2vqBbZ2oQ-ZVZINMJDZChfK9xpw5d6XrPe2DM6N1aRmZEnHg6HjtPcCf47DDGjZoLPlUDFKtMJRZLlk5m_x1eBSkNxvJIPxKHWcN7cVX9TtejNxGPu3L-gBMQiV_Y41GBZtapJQJRGzTC-HxhTLu6Y6CbtQwvncoFDIhF5sfNCKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
اینفوگرافی خدمات فعال‌شده پس از رفع اختلال فنی</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/news_hut/66496" target="_blank">📅 16:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66495">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cec2c7bdfe.mp4?token=d8CteydmpcTPYqg0lPLkVhq5i4Z4W9Kz71FSiCyg1kTXXvPPQuDBtJS5Rwrr_qNmmQ9OEzji58VuweTNX0Gp_DPvXPh1GjHcTAYWcRpw3ybCC1-sUtD-KKoLHeU1lxCzLfVJdBM2aL0PuvqwWUYTK-YNb2W9lSQfFQ70iF7kHSTRhyZS_JtGtvvQu6kIrhAOKaLj4yuV1xW_tFL_pE3zc_iawe4JnSe4jJ_K0uDJzVaG22kbHm1X09oQe0VnkCVuQgTjWG1yiyihx8d56XHn9FwnNFN6t4zKAg0cEahqanepga7q5gVYvdez1ySXNvFolTrtm92ivhCK4c0VvQjcvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cec2c7bdfe.mp4?token=d8CteydmpcTPYqg0lPLkVhq5i4Z4W9Kz71FSiCyg1kTXXvPPQuDBtJS5Rwrr_qNmmQ9OEzji58VuweTNX0Gp_DPvXPh1GjHcTAYWcRpw3ybCC1-sUtD-KKoLHeU1lxCzLfVJdBM2aL0PuvqwWUYTK-YNb2W9lSQfFQ70iF7kHSTRhyZS_JtGtvvQu6kIrhAOKaLj4yuV1xW_tFL_pE3zc_iawe4JnSe4jJ_K0uDJzVaG22kbHm1X09oQe0VnkCVuQgTjWG1yiyihx8d56XHn9FwnNFN6t4zKAg0cEahqanepga7q5gVYvdez1ySXNvFolTrtm92ivhCK4c0VvQjcvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران شهر نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/66495" target="_blank">📅 15:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66494">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f017f858a.mp4?token=bRSo0VrTI8_HKg6jMWq0B8XyUQGApQUcHuX6lV7Gy04_KR2zx8BeUxpt2jrNEMAP5nVhWqwdPXQ7wvw0cgMTv7FUXaZWFl0nzRDS67iGZ9Ajb-3yDpgRHhzH2FTxYPAoqgTMgBhWLi13CEwzwQztGp5mPxcDWnSNyZ3WGMaOAlIp_tH3Lrp6uE1AePSTnc1hzAN22RQPqJq-awnjVhiZ4SpJz3mQ7KJ82R76EdHxKyeivafayfhDuRckaz2WEBxXF2yWkNCq8rKqDx27YQh0cbnbpPL-sp3neaotOyaHDIKYhiGiw-Ix_esQYBcYs9troU9O4_DCJDTCtJJ-M-ca7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f017f858a.mp4?token=bRSo0VrTI8_HKg6jMWq0B8XyUQGApQUcHuX6lV7Gy04_KR2zx8BeUxpt2jrNEMAP5nVhWqwdPXQ7wvw0cgMTv7FUXaZWFl0nzRDS67iGZ9Ajb-3yDpgRHhzH2FTxYPAoqgTMgBhWLi13CEwzwQztGp5mPxcDWnSNyZ3WGMaOAlIp_tH3Lrp6uE1AePSTnc1hzAN22RQPqJq-awnjVhiZ4SpJz3mQ7KJ82R76EdHxKyeivafayfhDuRckaz2WEBxXF2yWkNCq8rKqDx27YQh0cbnbpPL-sp3neaotOyaHDIKYhiGiw-Ix_esQYBcYs9troU9O4_DCJDTCtJJ-M-ca7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آیا می‌توانید جلوی حملهٔ اسرائیل به لبنان را بگیرید؟
ترامپ: «بله. آن‌ها احترام زیادی برای من قائل هستند و هر چه بگویم انجام می‌دهند.»
@News_Hut</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/66494" target="_blank">📅 15:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66493">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66493" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/66493" target="_blank">📅 15:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66492">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aS2Kh5Xengf6MSG09GggYGDaIdLMT-CprxpsugsVICc-f36tueEm0NII2iBw40xP4qkVrzObtgYZQwC3C25zqvQQuGLM-TVhzsNqCT5p3cpUpIzcgQJu43zHI2MZsHBpox5QhuIfgT6GD9uF16htyUzOdseg3xteID9KkcWQxTmZ9XrdIgU_iYHgGqqU8yRnjiOWEyK-1FViW7AvDb9kEpm_9spWhiR9EdZ3oSlAuhzm1RH0R5LyIP3QzCk4Tbs8TZ-iUL2vmgX3cAwuuMEY_sLw89mNysI29CZK1M7DX-TKz2UrgpvWBKovl-iSteB-eKKYI1CaSo64Fi6naTAa-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/66492" target="_blank">📅 15:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66491">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUtTHPCXzgDKFClzap6awfBgD8Zi8yZuDY95Zb-UB3GVfMkr3rh1P5mhnWevSxCEbwEHhfvkj1mk3U5Jd2_i3ArbyeQlhxbzxZQAnnYMGz0b4NeEsLN80O2595UEBZxe-4-qjGHtBEbmDBoBej4K9G4OsL3HqnI4hktCUQ3d9tTp-9Oqq-KM92QGhLTVkVNzolrtwIXmBE8yopjcEtoPStGsp0dsfsruw5zs_S-QpBxEP0M34GCYYBjXgB4OuKd8AfDiI7cTGCIR6S4Z2sXDTQOEg_m3lY0b3SpWo61spy1A7TeapGvrO-WuJie0_-xJhpjQHN58gNeIJ96mA72mlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسرائیل به فارسی؛نخست وزیر نتانیاهو:
پس از حمله جنایتکارانه حزب‌الله که نقض آشکار آتش‌بس است، دیشب به ارتش اسرائیل دستور دادم که با قدرت به حزب‌الله حمله کند.
ارتش اسرائیل به بیش از ۸۰ هدف تروریستی حمله کرد و ده‌ها تروریست را از بین برد. متعاقباً، ارتش اسرائیل امروز صبح به مقر حزب‌الله در بقاع حمله کرد.
امروز صبح با وزیر دفاع و رئیس ستاد کل، ارزیابی وضعیت را انجام دادم.
دستور من واضح است: اسرائیل حمله به سربازان یا خاک ما را تحمل نخواهد کرد و بهای بسیار سنگینی را برای این حملات از حزب‌الله خواهد گرفت.
ارتش اسرائیل برای خنثی کردن هرگونه تهدیدی علیه نیروها و خاک ما اقدام خواهد کرد.
همانطور که به صراحت تاکید کردم: اسرائیل تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان باقی خواهد ماند تا از شهرهای شمالی محافظت کند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/66491" target="_blank">📅 15:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66490">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc6524eaa.mp4?token=nktxYXhfu6TIoiH4f-mcTsvXefXq00RtTggsCI5dPcTtS_JJIpp1y_3A9RVqSZi96YzeW7QDoNABuK2dQX4QNcS1Zlx-5-UCKDU1tJ0gyioJfnQcMvB3NeAKNOGOye6lfB8gFyyQlCWZLyVM1qPIpKQnwZXDhfUPRQFpnstxsTC8aVb7MBYZi3Ke4uBeCuA9rqrGtkwn1XzZUDVMakDphB-fsEXSN6V6qLI6hEEfnlvqnK-2YDSBs93z-SiZr-liQyPt_yLaiK4lgp4daIzHnD89no-jECTFphWPqW5qRP5eKl1q7eTPM8ZVxAeajfn9iMo7VdaeyCMycEH60PpTeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc6524eaa.mp4?token=nktxYXhfu6TIoiH4f-mcTsvXefXq00RtTggsCI5dPcTtS_JJIpp1y_3A9RVqSZi96YzeW7QDoNABuK2dQX4QNcS1Zlx-5-UCKDU1tJ0gyioJfnQcMvB3NeAKNOGOye6lfB8gFyyQlCWZLyVM1qPIpKQnwZXDhfUPRQFpnstxsTC8aVb7MBYZi3Ke4uBeCuA9rqrGtkwn1XzZUDVMakDphB-fsEXSN6V6qLI6hEEfnlvqnK-2YDSBs93z-SiZr-liQyPt_yLaiK4lgp4daIzHnD89no-jECTFphWPqW5qRP5eKl1q7eTPM8ZVxAeajfn9iMo7VdaeyCMycEH60PpTeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضائیان: ما در مقابل نیوزیلند لایق برد بودیم/ اگر گل اول را می‌زدیم شرایط عوض می‌شد. امیدوارم خدا کمک کند و موفق شویم.  @News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/66490" target="_blank">📅 15:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66489">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71570c04a1.mp4?token=lqRW-bUdmLTL9VtzXVQ0NrpUh-6prOTEkyIxPsWaU1azjY7MwsUhEo5NtF5dJ4v7cuWh8z7c9imm0-F9BB1EuTEfu7TJmQa-ZQFdaCRT7bLX1cqYzebNec6UCLQcYYNfAEYoGTyrlO3chALdtrjHu8AOLj7Xglg4Hc3R3S5ryoobQf21YQApQh4z6HZ0Nx4GfeQ_ELO9GWCSkOqeJccPtuWPnEuRIrOeB9AuuL036vstWGCqgXWqg4hF3ECMnCnShNKpsyg1N8G8qXAvEb2XC9Ea69ysRs4rk2Xc-mccsx8qMLeKeLLRI6lVF1rBocNgCzAjNmNvK4kz3oNHeHKT5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71570c04a1.mp4?token=lqRW-bUdmLTL9VtzXVQ0NrpUh-6prOTEkyIxPsWaU1azjY7MwsUhEo5NtF5dJ4v7cuWh8z7c9imm0-F9BB1EuTEfu7TJmQa-ZQFdaCRT7bLX1cqYzebNec6UCLQcYYNfAEYoGTyrlO3chALdtrjHu8AOLj7Xglg4Hc3R3S5ryoobQf21YQApQh4z6HZ0Nx4GfeQ_ELO9GWCSkOqeJccPtuWPnEuRIrOeB9AuuL036vstWGCqgXWqg4hF3ECMnCnShNKpsyg1N8G8qXAvEb2XC9Ea69ysRs4rk2Xc-mccsx8qMLeKeLLRI6lVF1rBocNgCzAjNmNvK4kz3oNHeHKT5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضائیان: ما در مقابل نیوزیلند لایق برد بودیم/ اگر گل اول را می‌زدیم شرایط عوض می‌شد. امیدوارم خدا کمک کند و موفق شویم.
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/66489" target="_blank">📅 15:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66488">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b3bba52e8.mp4?token=fTf0RYRyb0b-0E3p552dst6vMNhrQsGJK46AD8YfFsDl3AO9dYivr4vcUiLV-5JFzxqPkFV91nXO81VRsdX3nbfVr12MWTp3voR3tNzcTrfjXlY3WQ4O81H6RY3IlI4PkyCy7IVFg6ZeC7c-L5ifp66xrJW8xErZbkjwI3pFrVWlKHmlEVLoESnvUaVAve7AgD7EMR6z2rkqeVbZLhrbl6NcZosYn4aP7f26GCzdlTEJTxvxVYiDUbzgsOWpGDrCfyIxH6F-WYDIKfe9CL0LfWK7syIgereJ-vS13QbMSPm1EchzehtPQbjmJnPiWUdC7sshostlYWh2hegrsAGeIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b3bba52e8.mp4?token=fTf0RYRyb0b-0E3p552dst6vMNhrQsGJK46AD8YfFsDl3AO9dYivr4vcUiLV-5JFzxqPkFV91nXO81VRsdX3nbfVr12MWTp3voR3tNzcTrfjXlY3WQ4O81H6RY3IlI4PkyCy7IVFg6ZeC7c-L5ifp66xrJW8xErZbkjwI3pFrVWlKHmlEVLoESnvUaVAve7AgD7EMR6z2rkqeVbZLhrbl6NcZosYn4aP7f26GCzdlTEJTxvxVYiDUbzgsOWpGDrCfyIxH6F-WYDIKfe9CL0LfWK7syIgereJ-vS13QbMSPm1EchzehtPQbjmJnPiWUdC7sshostlYWh2hegrsAGeIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
⭕️
هم‌اکنون سپاه در بیسیم کانال ۱۶ دریایی.
“از آنجا که خروج اسرائیل از لبنان و لغو کامل محاصره دریایی و خروج نیروهای تروریستی آمریکایی از خلیج فارس و منطقه از جمله شرایط اصلی توافق بین ایران و ایالات متحده است. تنگه هرمز تا زمان تحقق این دو شرط بسته خواهد ماند، به همه کشتی‌ها دستور داده شده برای امنیت و سلامت خود به تنگه هرمز نزدیک نشود، هر شناوری که از این دستور سرپیچی کند مورد هدف قرار خواهد گرفت.”
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/66488" target="_blank">📅 14:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66487">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
مرندی عضو تیم مذاکرات :
ترامپ بار دیگر ثابت کرد به تعهداتش پایبند نیست.
رژیم صهیونیستی مجازات میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/66487" target="_blank">📅 14:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66485">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">شعارهای دیشب مداح حکومتی در مراسم محرم
😐
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/66485" target="_blank">📅 14:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66484">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddac5fcdb8.mp4?token=EJ9jEvEYK1F8H1zlYZtPq5Amtko_vCYclMkFQpKU3AOQo_vhz_czW9IVBiONveTr0D-U1Qx_eKsIjseLnn9uLMUbKXmj36eGKTjUU7rMx8Ko-QrFSIZKq7BpF-DkOIEGWvhe5DYx62QonE4adTvIiJr3X6rH_I1s2xyoOO2mA46-ofARD23wRyNud0mQAC96L9A8yrKtSx97tq5MbqpUxRZDyURLse_F8FczYA3H6sBtu5u8ZSGYBtFStj5njgBukUt5pCuGwcEchCjINpzFAm4nngPNVwkLweTA8jGQz08-wZw0GArNiOlPDwsgAAGQjoqnUBBw-c3rAKFScIOLMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddac5fcdb8.mp4?token=EJ9jEvEYK1F8H1zlYZtPq5Amtko_vCYclMkFQpKU3AOQo_vhz_czW9IVBiONveTr0D-U1Qx_eKsIjseLnn9uLMUbKXmj36eGKTjUU7rMx8Ko-QrFSIZKq7BpF-DkOIEGWvhe5DYx62QonE4adTvIiJr3X6rH_I1s2xyoOO2mA46-ofARD23wRyNud0mQAC96L9A8yrKtSx97tq5MbqpUxRZDyURLse_F8FczYA3H6sBtu5u8ZSGYBtFStj5njgBukUt5pCuGwcEchCjINpzFAm4nngPNVwkLweTA8jGQz08-wZw0GArNiOlPDwsgAAGQjoqnUBBw-c3rAKFScIOLMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
املاکی در مراسم اعطای مدال هرکاری کرد نتونست گیره مدال رو بندازه داخل و گفت میخوام یک مدل دیگه برات ببندم و مدال رو گره زد و نزدیک بود طرف رو خفه کنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66484" target="_blank">📅 13:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66483">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
‼️
وزیر خارجه پاکستان: مذاکرات سوئیس بدلیل مشغله کاری مسئولان ایرانی در ایام محرم به تعویق افتاد
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66483" target="_blank">📅 13:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66482">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd02588050.mp4?token=rrU1vM-njbgI7s9NXpEVV68a4UMuQn1zLIPPcCBSu5qTX-IaAex4uTBGKS5FwtXfA3INDzVKUl3OzstkIUr3SxT-bQfg4-gH36JePkcMPW8qG1n1m0EeA09TT00RqZ1IQ9l03dgdffI4zFTKk1iV-dM-YHKRA48JJJXJ13znEVAPJ774YgR3amgiKVA6IgxkMhfT9__7UQ4zTlamrkcldDh5tbkJyj_sLgubTjDtJ-h46TIHx4Yx-cz4vdJPjpiir6LihVn4epPgRgUSHvo4SLqlXEMCEDLtRA1o8P0nXf46MOsbIM6uvyEJmQHvKT8A9y3AjerafEz_fy64m_VR0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd02588050.mp4?token=rrU1vM-njbgI7s9NXpEVV68a4UMuQn1zLIPPcCBSu5qTX-IaAex4uTBGKS5FwtXfA3INDzVKUl3OzstkIUr3SxT-bQfg4-gH36JePkcMPW8qG1n1m0EeA09TT00RqZ1IQ9l03dgdffI4zFTKk1iV-dM-YHKRA48JJJXJ13znEVAPJ774YgR3amgiKVA6IgxkMhfT9__7UQ4zTlamrkcldDh5tbkJyj_sLgubTjDtJ-h46TIHx4Yx-cz4vdJPjpiir6LihVn4epPgRgUSHvo4SLqlXEMCEDLtRA1o8P0nXf46MOsbIM6uvyEJmQHvKT8A9y3AjerafEz_fy64m_VR0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تلاش سربازان روس برای سرنگونی پهبادها
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66482" target="_blank">📅 13:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66481">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98d70873ad.mp4?token=ayX_scmRwe86D4WGxqApORG0AXQdFuwW4JWRwgB6F8ejpZSArqq7XZ_715xy3u4mTdOAdEaIOg7gIdoXUDCLJA59UjZ_SldSpwFYdcTUOzHQgYmpTDsPaDVxamQU7lA1r-kgQLDIuhxf2MwGED7yofVbdoc-sWeAO6EsMZNEjSjmKt5QuvBFZeOCVkRQP9ZjUQ2SW4gAx_OojEXdh7FybFveeWLMC6UIZnP6VxuF8x6pFfjifrVpiPKIX4y0rDy7AhsmD237_57tl3UVYzn94EuAIZXuc4xGX-rjXiXHZKU29SxArKSfbcX0oYH9SZhx_s2hu2GK6LrDxuiT3zyxCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98d70873ad.mp4?token=ayX_scmRwe86D4WGxqApORG0AXQdFuwW4JWRwgB6F8ejpZSArqq7XZ_715xy3u4mTdOAdEaIOg7gIdoXUDCLJA59UjZ_SldSpwFYdcTUOzHQgYmpTDsPaDVxamQU7lA1r-kgQLDIuhxf2MwGED7yofVbdoc-sWeAO6EsMZNEjSjmKt5QuvBFZeOCVkRQP9ZjUQ2SW4gAx_OojEXdh7FybFveeWLMC6UIZnP6VxuF8x6pFfjifrVpiPKIX4y0rDy7AhsmD237_57tl3UVYzn94EuAIZXuc4xGX-rjXiXHZKU29SxArKSfbcX0oYH9SZhx_s2hu2GK6LrDxuiT3zyxCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
اسرائیل کاتز، وزیر دفاع اسرائیل، درباره سوریه:
ما آنجا می‌جنگیم. ما به الجولانی نیاز نداریم. الجولانی، تروریست کت و شلواری، نیازی ندارد که بیاید و به ما کمک کند.
ما سوریه را خوب می‌شناسیم. او قرار نیست در لبنان به ما کمک کند. او باید در سوریه بماند، در کار ما دخالت نکند و ما را مجبور به دخالت در کار خود نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66481" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66480">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e15d1aff21.mp4?token=u-6TnmKW1bn8sUlOZQ0OWmewyXxD_qeuhcJuhU1zKvrlk201_ewJFKNfA7cv6eGn8LSMCLwcUKd2SnGCqwUasqmP1QzqBWLOY7UtOONgpd7Ji0EeO422h_6sB8TbOmpGjGUxtTK0kDN3I5bEpmDqp9_xnKjH8gn6AsoTUU3lbQr1Q0Sy4gJ5QNXlYAdfZfo5E3F5k_fmVQ2lD4Mt_b4gYoInyS5TLq-13O48OARIZRygFaiMA-RJZUk19wQtqhaKoAnEnUth5Bd4rE5YIkhig8iT-kLJqJ00y7ZgKbAvnoTHuC9QOdtuwkI9sQELwaOsTxb3E1V7Wyfd8EwJVFKZrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e15d1aff21.mp4?token=u-6TnmKW1bn8sUlOZQ0OWmewyXxD_qeuhcJuhU1zKvrlk201_ewJFKNfA7cv6eGn8LSMCLwcUKd2SnGCqwUasqmP1QzqBWLOY7UtOONgpd7Ji0EeO422h_6sB8TbOmpGjGUxtTK0kDN3I5bEpmDqp9_xnKjH8gn6AsoTUU3lbQr1Q0Sy4gJ5QNXlYAdfZfo5E3F5k_fmVQ2lD4Mt_b4gYoInyS5TLq-13O48OARIZRygFaiMA-RJZUk19wQtqhaKoAnEnUth5Bd4rE5YIkhig8iT-kLJqJ00y7ZgKbAvnoTHuC9QOdtuwkI9sQELwaOsTxb3E1V7Wyfd8EwJVFKZrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
حملات گسترده ارتش اسرائیل به مواضع حزب‌الله
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66480" target="_blank">📅 12:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66479">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae8db95bdf.mp4?token=SfEg6Vj54argJz21lxQGYDKm5qoThN3VhsTjA81fiaegLqRgVY78uf76oEPHK3CTo7ObyIUX2b2YLlIzh6NrX8077D-yJMDM60lo_AtDW7t0nAJKF0_WAWt-Xskedt6ZZ1h00eizCX0VE6-_aSJYD9YBRu_3kBBqaC9FPeorx3JKeVZTtz6fp5m2xbi4QvC7HPs7M2j_Z8yCatR6G2SvOR4ooYx26n2q0jtr7V5scYCxniOA7OiarAxk3k1Q97x2FgboDY63M6USapN38P9wrP2SDRaTl7X5nXvIcxVAk-jpB-fvk2aXna8Y4qs1JrSTybqfe5lsurkHGs0I_eNGTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae8db95bdf.mp4?token=SfEg6Vj54argJz21lxQGYDKm5qoThN3VhsTjA81fiaegLqRgVY78uf76oEPHK3CTo7ObyIUX2b2YLlIzh6NrX8077D-yJMDM60lo_AtDW7t0nAJKF0_WAWt-Xskedt6ZZ1h00eizCX0VE6-_aSJYD9YBRu_3kBBqaC9FPeorx3JKeVZTtz6fp5m2xbi4QvC7HPs7M2j_Z8yCatR6G2SvOR4ooYx26n2q0jtr7V5scYCxniOA7OiarAxk3k1Q97x2FgboDY63M6USapN38P9wrP2SDRaTl7X5nXvIcxVAk-jpB-fvk2aXna8Y4qs1JrSTybqfe5lsurkHGs0I_eNGTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
یسرائیل کاتز، وزیر دفاع اسرائیل:
ارتش اسرائیل باید در آن سوی مرز، فراتر از مرز، از کشور اسرائیل در برابر سازمان‌های جهادی در لبنان، سوریه و غزه دفاع کند.
ما از «مناطق امنیتی» حرکت نخواهیم کرد، نه در سوریه، نه در غزه و نه در لبنان.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66479" target="_blank">📅 12:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66478">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-ivsGm8LTQv__VzsrQP6VUZ3zIELWIn7Z0QPdFC5Wohb998WqWr61iZ_CRlIgxpEAhd8s6b-77GIpiZBwp40rYofjl2KGlTu7rZnAISOtxllqWunNunFeMwGlvjH0n9iwOVliKO2kLt4y9HE2yTwnZE5ifSzAtaKvFvtr4gYWpgIDpHdAegaevOKxhHZ8eT_gVATyn1cQvsz9M4t8ErqYkgXVOGIjKeCgmWR2cGUUd1K-FJXT90Y-3JUYQnORspA3cEeijKZZjiwB0G_Bmj4TT0IVQHz2azYcrsnPgLGpTdKI__L3XbRfptAxwV-vzr8z8aBvPRhPjmxdVjNa6i1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
گوش‌بفرمانیم، وظیفهٔ محول‌شده به ما توسط مقام معظم رهبری پیگیری تحقق شروط و بندهای تفاهم است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/66478" target="_blank">📅 12:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66477">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c84fc04d4.mp4?token=DILODUinwVd05yzzmsx9mFNWaRx-tDRd7grFsWign4kR4yr8FC30PUSaRlBdODffrzv82Pcs1ooT_j5Ji1pt6NaOMZTejTVsI9Sv-Bjr5n--vp1uXWg8U9HRHcauLSbdEcZNXV2_Ipah4qPp614o3W8AGtlZPTCd_k_wSzUdn3z0E3_LpvWFEHpohk_PHPFSXBo45kkYgZxpvplRDQ69mk6zDi5cAsoAooEX8AwxCjxLp0VIbzZg1olqss0XoiyJ3RwMFHKb40zPE-V-L78SyWNfdarDyMqzH-gNsFdE2EoXPkFLF1hOG-Ih7sbYVD41xnkx7ul12XjsbJK8M4FxAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c84fc04d4.mp4?token=DILODUinwVd05yzzmsx9mFNWaRx-tDRd7grFsWign4kR4yr8FC30PUSaRlBdODffrzv82Pcs1ooT_j5Ji1pt6NaOMZTejTVsI9Sv-Bjr5n--vp1uXWg8U9HRHcauLSbdEcZNXV2_Ipah4qPp614o3W8AGtlZPTCd_k_wSzUdn3z0E3_LpvWFEHpohk_PHPFSXBo45kkYgZxpvplRDQ69mk6zDi5cAsoAooEX8AwxCjxLp0VIbzZg1olqss0XoiyJ3RwMFHKb40zPE-V-L78SyWNfdarDyMqzH-gNsFdE2EoXPkFLF1hOG-Ih7sbYVD41xnkx7ul12XjsbJK8M4FxAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
بمباران شدید نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66477" target="_blank">📅 12:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66476">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99cbfc5535.mp4?token=I6m3E8-K1TF1VrwtsDBBdlwF2dfxfyiumNeQZzcha_iEFLpMAVuE9ZfbPZDxbFj8IaqZzR_BCERND5IBwtudqLlnnTeb4pypCyTOKP23d12IiDC9IsZjfNPJKaTODOd9GfiMPJkSugNbxq8aTD23zyUlhUCNOMZEcxSJ87E5XIA6mwZG0AR5952FjAEFiOJ4ailreSfKAHHweMe8KeKhP--_sRPyYOTpOC_XJH3nDRjAT81jaL40T8fST-SlPSGhxm69CxYmcDPb4-Cjs8L4TEPj1nExXtNU-XRPpUwrqTlOjny_3xUjKyW6pPUmn5qtWTN5HNNwu4fsgO7B2vfo3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99cbfc5535.mp4?token=I6m3E8-K1TF1VrwtsDBBdlwF2dfxfyiumNeQZzcha_iEFLpMAVuE9ZfbPZDxbFj8IaqZzR_BCERND5IBwtudqLlnnTeb4pypCyTOKP23d12IiDC9IsZjfNPJKaTODOd9GfiMPJkSugNbxq8aTD23zyUlhUCNOMZEcxSJ87E5XIA6mwZG0AR5952FjAEFiOJ4ailreSfKAHHweMe8KeKhP--_sRPyYOTpOC_XJH3nDRjAT81jaL40T8fST-SlPSGhxm69CxYmcDPb4-Cjs8L4TEPj1nExXtNU-XRPpUwrqTlOjny_3xUjKyW6pPUmn5qtWTN5HNNwu4fsgO7B2vfo3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
اسرائیل کاتس، وزیر جنگ اسرائیل:«حتی اگر ترامپ چیز دیگری بگوید، هیچ‌کس نمی‌تواند به ما بگوید چه کار کنیم و ما قبلاً این را ثابت کرده‌ایم.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66476" target="_blank">📅 12:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66474">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba86fa7681.mp4?token=Ad8G5iQRHfKX0fBQp1ZT12cQbYywwG9tHvrM3EksFGSd-tWsc4wwAKENTT5YhwwM8tACzaUe1aNUAIagXWiva5R2rdoKtg4pcry_8UpHU3bjxMBaLjuh6gHzYpvNDGejLNCTtA7bfQZR94SXkj3wUZ8eupy1gAWeuLZ8nDhTGIaxXgGgs9pC-0z4RLFpnnNgVAUzN151VHJ8Je80QcC6Bx9S1vDt7R_keP0D_f8vI6rE9Qz-9V4ShTeERgn8PM4rF8shzgKXO-f0ppi5mNRjenASlG-pdhL-aNMxsiD3Hd7neWCjtXE9pGP3uGK1kkLijETujv6pICqQMsAMYa6w2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba86fa7681.mp4?token=Ad8G5iQRHfKX0fBQp1ZT12cQbYywwG9tHvrM3EksFGSd-tWsc4wwAKENTT5YhwwM8tACzaUe1aNUAIagXWiva5R2rdoKtg4pcry_8UpHU3bjxMBaLjuh6gHzYpvNDGejLNCTtA7bfQZR94SXkj3wUZ8eupy1gAWeuLZ8nDhTGIaxXgGgs9pC-0z4RLFpnnNgVAUzN151VHJ8Je80QcC6Bx9S1vDt7R_keP0D_f8vI6rE9Qz-9V4ShTeERgn8PM4rF8shzgKXO-f0ppi5mNRjenASlG-pdhL-aNMxsiD3Hd7neWCjtXE9pGP3uGK1kkLijETujv6pICqQMsAMYa6w2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی شبا میری اعتراضات و روزا میری راهپیمایی:
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66474" target="_blank">📅 12:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66473">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc0be5a6ce.mp4?token=eTxN4BmYeEv6UYfGotpkjaiDXAffNR0tS4102689Wdx_ZN8qG2tfn3O76GY_zN5Ukbc9CpxZmw9_RouCTMUtR-TTxlMS4BzUD96EZ-dockFHkaBT-YX9Jz2BNeGbtgDyKBS7wHCL2KMUnMVFcqaoalDo4WURhGinkWyyb_9ZJPs2vfvJbCDf5WukxQvCTP5KbDjYwmgMa7sE9ibKhod0yr_kqbkTkCWan3Wg3zrXHrl0XNY1RicC0TcDOK8Ev_YXxJDXnyKEH62III7UMVO6cTKkFVI8QCIeCv2wmdPK7peH_G8NChmDHybRtKFdCn2F0DpuLvAfCEbxH-Jwl50qDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc0be5a6ce.mp4?token=eTxN4BmYeEv6UYfGotpkjaiDXAffNR0tS4102689Wdx_ZN8qG2tfn3O76GY_zN5Ukbc9CpxZmw9_RouCTMUtR-TTxlMS4BzUD96EZ-dockFHkaBT-YX9Jz2BNeGbtgDyKBS7wHCL2KMUnMVFcqaoalDo4WURhGinkWyyb_9ZJPs2vfvJbCDf5WukxQvCTP5KbDjYwmgMa7sE9ibKhod0yr_kqbkTkCWan3Wg3zrXHrl0XNY1RicC0TcDOK8Ev_YXxJDXnyKEH62III7UMVO6cTKkFVI8QCIeCv2wmdPK7peH_G8NChmDHybRtKFdCn2F0DpuLvAfCEbxH-Jwl50qDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
نبوغ اوکراینی ها در شکار پهباد
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66473" target="_blank">📅 11:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66469">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TMn5mGkLwO0LZSNCD-q9sOL0Csh-GWIURAcyg0xwUrJoTBGebMqPusYpr4DhfoesZ0Ernh-SAmEhHmqTXhd1AwsYnOMIgTj62beYgJsRwIXASdpP9GEN5Ko1jzkWXVQkBBNwPitnQb6vEt3F_EdVos06Y_YvXcx24Sl_bRJuic31uWW-LzFaTlcm6XCEW0QlFuC6BcO8ORJDPuvJe9Y544ETBaoA0Ka2cqUe0ghOEwt_n67EEl4zhKY1_ATrbGLinRUSyM9sWNcWZH7O6cgzc5iPER0IrAk4Hq7FXn5mnUQda0ve8N-ngouZ-3_ZCDQbxfGik0tB-7kAWRQ_ba4qtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t93V6j_buzmEiid7DXcfqKo5sKkLWADHoiIdUYtz0NcOWLlJQDHTjMBSu_BdYaE2-3N-EWD3ZnqEkmC8ecgnQfGVBvlXyjfNWOy5JiJNap4bNC1ws8aNukWiZKbJbOkrPVfgIwQLGjRW9d5nzW-6eHqZvXAmDbdlmcX0V2AVJqSMeslpSKxassJeMsCfybHxdTMBDiSDUNG_gRmXLS-93Zja4CVWBCRRIXeVaUEdqd9kH4Yxpt2GHqGkJcK-mgIfJvQw7I_2SMjNIl-A6lVGHIM7Z6YXO47LxkXcDaXBeaIUJJIJX42OjqRZ9ilRic3oAHwo5gHtPYnwQin2BjK_xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LUDTtfORbLwN1teAYxyB1LCQr6u876uFJNq6zKAvI2Jo7A1B23TBYVfDe3OS7ToMmAdLK9uefgMGDTwqb7viFdXQ66DWP34czze7NcK6PTK24lAI6LMB1eCH8JqEiZNQfCPZfnNjbLNepuunpUFkpIyl9GAwYGSPjc1xkDIZsRGDqhkFkW4ajqVQ66AltjlAyWNBe14wpgwBolMvjIKul59UVXcWg5nG-YrMbjXmNr5MkQRfuAz5TrOKvQJcJslSO9wkCcXerIg4P8jh3xNIdwaAZflA1Qm7V0MJiFK6Ap0TYTjlhRGQzTF8NGu3H4hdhz139zA4yBtxDMbbFJWB7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cb0e601ac.mp4?token=to5gklNbuFoWoFykwN43rqBNvMNf9m2RVsD4xMoIv1GcwkuQQjfGfA2RnNTiV6dHrnCvdX5GG4c16NKsbnlroiLvjcF58B0GV27wv-yJvpBVvbsUaft5Vmgsh19W7FkL6BHb9i-tGGm56GTFf0dJWxIFpGpIG9xEvHQv9y09lHcB0alHQBm7VtyomqQRUZhQvUg-YUF94zEMokQDrwm1xbKxIP4G1kIxYz5cmKmS7F_inRrUsrfYZQQeD-xYkFTwioTP7xlftPuoTAmgT_3_W8lyOLpkyvi-rXRCt2ekAsh9B8MfjcOA_yY1ei2D_BahzdnHs_Bwqi-ZgVhgYKq-kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cb0e601ac.mp4?token=to5gklNbuFoWoFykwN43rqBNvMNf9m2RVsD4xMoIv1GcwkuQQjfGfA2RnNTiV6dHrnCvdX5GG4c16NKsbnlroiLvjcF58B0GV27wv-yJvpBVvbsUaft5Vmgsh19W7FkL6BHb9i-tGGm56GTFf0dJWxIFpGpIG9xEvHQv9y09lHcB0alHQBm7VtyomqQRUZhQvUg-YUF94zEMokQDrwm1xbKxIP4G1kIxYz5cmKmS7F_inRrUsrfYZQQeD-xYkFTwioTP7xlftPuoTAmgT_3_W8lyOLpkyvi-rXRCt2ekAsh9B8MfjcOA_yY1ei2D_BahzdnHs_Bwqi-ZgVhgYKq-kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حملات ارتش اسرائیل به نقاط مختلف در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66469" target="_blank">📅 11:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66468">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNxyC3bzrI713zTE2h7tFcdmy34nyniFeev176wAjDyEAnMnpeAY7DaJJtCjfsijHNVT_NJ3QodcGb2GUzuz-iJi4K_VZweCcYpg3eHqNfiFSEkeGeGu4ZJgKi7XYJRwj8pvzKVpDG-dMCG07KpJliod2loGCDmbkKjy38Asa8N-AI3GhkC5tRp7R6QyvkLVJqU1JFJQbCEBt5jFrbJhYcYKgNquL5n1BFBpUD6dSym6Iyew-HY9heADYitKodxas80DLKPMXs-CT0wX4JtfeQe5bRa9xrycEJZ-E1bp6oAOB4uqzUx_V3iQlcZfu0oqb_dzX10MZOXfIVL0gSeMLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وضعیت ‏مسکو، روز ۱۵۷۶م عملیات نظامی ‌ویژه ۳ روزه پوتین در اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66468" target="_blank">📅 10:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66467">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7be955089.mp4?token=R07LvFqfCtikA5Uy7VXivIQi3m1KK2dhtTg2Q1MoOoti62iNvvyQ4XP5g1bGKrTZ_U5GEdf6J7F7bVu9CHyn89F9Wg28ilrdmgHyXEXO5hYo8Jn-flIpzys3gp8MDlIEBd1MeNxkOKWHiM57njEiY1oCEwDKR-Yg4yWQwGUnGEBblDNLnfdlDtT2ziezpeBALDpdvx8D2veWs78dB8YFmTmo3tY_l0LS94KCpoid0gBS-WlJULhZ6HhNkYt1fZYf7W_HbN8jtyiH4uH8LYjYL12hHl5hM7i6kTMfjbVvQTm7n3UVFi1l_X-k-nIpA2Gd2OX_1fHn3OnRoxBIGld28g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7be955089.mp4?token=R07LvFqfCtikA5Uy7VXivIQi3m1KK2dhtTg2Q1MoOoti62iNvvyQ4XP5g1bGKrTZ_U5GEdf6J7F7bVu9CHyn89F9Wg28ilrdmgHyXEXO5hYo8Jn-flIpzys3gp8MDlIEBd1MeNxkOKWHiM57njEiY1oCEwDKR-Yg4yWQwGUnGEBblDNLnfdlDtT2ziezpeBALDpdvx8D2veWs78dB8YFmTmo3tY_l0LS94KCpoid0gBS-WlJULhZ6HhNkYt1fZYf7W_HbN8jtyiH4uH8LYjYL12hHl5hM7i6kTMfjbVvQTm7n3UVFi1l_X-k-nIpA2Gd2OX_1fHn3OnRoxBIGld28g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری: شما گفته بودید که فقط تسلیم بی‌قیدوشرط را می‌خواهید. اما این تفاهم‌نامه شبیه تسلیم بی‌قیدوشرط به نظر نمی‌رسد.
ترامپ: خب، در واقع احتمالا تسلیم بی‌قیدوشرط است.
مجری: واقعا؟
ترامپ: من این‌طور فکر می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66467" target="_blank">📅 10:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66466">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/040ce8f378.mp4?token=Gak0iytzHiJZ_0foQphZJ8Kgw0x9Rek8zuCVpSUz9cNgWFUhr5YuSFnB5vb_El6DqPMGazK0vJubZ0PCClgG_x5X7nNxThwJlwQcY0QPJq2nQ39tOf-X5mQK1JaX20VmcOzGAdo40Prv37pezYpV2UB_d2iJML9TaJYDF8zYu3f0fxSCd-y0OELhVWi-Eg5KSljYRvB5UYlMd9RxUbyU6qgJeqCxgNujvCVIFrwvWkxkpTdCnGSsgpEJ50YCCGQOx2Wrxo9pPXFDd0IeFjOIAiD-q77CoibNCMstdw3eePFIds1jwwYBlerI6GNwx0qIc1sTiGdoxV7QG6GxjdGilg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/040ce8f378.mp4?token=Gak0iytzHiJZ_0foQphZJ8Kgw0x9Rek8zuCVpSUz9cNgWFUhr5YuSFnB5vb_El6DqPMGazK0vJubZ0PCClgG_x5X7nNxThwJlwQcY0QPJq2nQ39tOf-X5mQK1JaX20VmcOzGAdo40Prv37pezYpV2UB_d2iJML9TaJYDF8zYu3f0fxSCd-y0OELhVWi-Eg5KSljYRvB5UYlMd9RxUbyU6qgJeqCxgNujvCVIFrwvWkxkpTdCnGSsgpEJ50YCCGQOx2Wrxo9pPXFDd0IeFjOIAiD-q77CoibNCMstdw3eePFIds1jwwYBlerI6GNwx0qIc1sTiGdoxV7QG6GxjdGilg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ به شیخ محمد بن زاید:
وقتی انقدر ثروتمند باشی، میتونی انقدر آروم صحبت کنی.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66466" target="_blank">📅 10:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66465">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/635e862fe5.mp4?token=KOUnp3FcX8acP7MJqCuWmDQNlzVXgeWj_R0CwDY5zTVkVXETTVIXW5M38i6LF0nIrBieAJmHK-tzrf7oCBifP3OHbBQirxvPQAnsbV6lABtJlRNL0zJBh-CvlMT82fKE2E5eJat-VVwlI9AUTOWlDymaHHglisDnTzQSPkEpMXWbfTzFKkXejRU495fq8ufnvHI5N1yfZnRmZcObuy8_XVTURYq0kJBt3DVIlGBK67Ot-Sl9-NZq3CmpGir3hw20wz1DCoOPGGynKzhjhOydT49_H1EytzvxoNajb_XK2tCwsdw-h8N7pV_1LdVyS7MqAio3lVKC74yv8dAzzHmMlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/635e862fe5.mp4?token=KOUnp3FcX8acP7MJqCuWmDQNlzVXgeWj_R0CwDY5zTVkVXETTVIXW5M38i6LF0nIrBieAJmHK-tzrf7oCBifP3OHbBQirxvPQAnsbV6lABtJlRNL0zJBh-CvlMT82fKE2E5eJat-VVwlI9AUTOWlDymaHHglisDnTzQSPkEpMXWbfTzFKkXejRU495fq8ufnvHI5N1yfZnRmZcObuy8_XVTURYq0kJBt3DVIlGBK67Ot-Sl9-NZq3CmpGir3hw20wz1DCoOPGGynKzhjhOydT49_H1EytzvxoNajb_XK2tCwsdw-h8N7pV_1LdVyS7MqAio3lVKC74yv8dAzzHmMlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختران حاج گاسم
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66465" target="_blank">📅 09:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66461">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmQ5s-nkuNMuYvOwo7xXEMqBDwI63OivASx4-PsXbOkK9xj_6ciJJ5YcV0FEWAJIMHyDsrqvbQkU31wBX6zib7VqMLEs4bAYAjDglzujy-_aP99TEO3rL_nvRHnkt1BjTALLK9lIxgnG28FpHFdQFD_uMtr2QTYpahGR7VyDZS1fib_2z0up0-HeZ3PSvJs7fGODxn1DdK0FxAc9hsNdpQb-bY3eiX6XGGHDBN-RNN_uZiAJhMxNKnxTzxeqKpsI7m4Yw6qUcy-BhyBua-_HVY9Mcmop1yLGQPHtRO1IYQJPD8kL6DlqLz8l7xG4CXXPzPpGfIBzCXnxwf7NrvVWVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a17f4667.mp4?token=VrtPz57wYLNEmqmVdS6O1_puOTV1IGW4ykdHGYjwRml3LF85yxjzWz8Hmghusc9f7-4E6mEPhWEdEbBGCZUWivy6Hl-BRXjkzTeocHV7H8j9UuDLbpBj4Mv5bwYRQEHda-vpOVSxNYoBipooy84JGJJp7L9_w-_87ba-OYQxhwQ3huEdTqLjG2HOE3q8DtBt_rZ54OMEibhmsaNFB_vGxZnbE-L1zM5vwOXy4MQ66AQA3eDe4FHyf-wIsy6igzeNj91_Hke_efPv-gwl_YXQT_AYGTwPTWmIFfLq-ccBKixMgq5xKb3O0B2oCx9EQv4e_dFvevpfI3ZIoynRMNQanA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a17f4667.mp4?token=VrtPz57wYLNEmqmVdS6O1_puOTV1IGW4ykdHGYjwRml3LF85yxjzWz8Hmghusc9f7-4E6mEPhWEdEbBGCZUWivy6Hl-BRXjkzTeocHV7H8j9UuDLbpBj4Mv5bwYRQEHda-vpOVSxNYoBipooy84JGJJp7L9_w-_87ba-OYQxhwQ3huEdTqLjG2HOE3q8DtBt_rZ54OMEibhmsaNFB_vGxZnbE-L1zM5vwOXy4MQ66AQA3eDe4FHyf-wIsy6igzeNj91_Hke_efPv-gwl_YXQT_AYGTwPTWmIFfLq-ccBKixMgq5xKb3O0B2oCx9EQv4e_dFvevpfI3ZIoynRMNQanA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حملات شبانه ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66461" target="_blank">📅 09:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66460">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66460" target="_blank">📅 01:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66459">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ROgP9uD7M-dTVmcSf0eVxpKVG0Z4xdMtO8DK0XXtTkKlSQ_bqV4S7nOdVkq4-YauQR5-ppFw0D40ybWeVQZf-fH24sFeOifuWJ61TVeOHlaqCCWNzNrXp1-WpPihIc1r2MrTuQHu-kODqywWKd-fh-kn6VuCbXG9tscDISU3AP9DfZMrZbwR6XAX5LqJ2A73WTGM8wg_Usj7BkcKBaJr7E69DQ0UyzwsHHQt4u6maftUC7MpPfGWrIAz6qKX6qmIwLiMyBWM6gAvxU9oajPIaA_OLI3Zhcwr5ipj4bC3-Q-NGSzKeKjCxs6hK7l7NQ8BHco05Or9v_RWINGnrX9kog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66459" target="_blank">📅 01:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66458">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
‏به گزارش المیادین، هیات مذاکره‌کننده جمهوری اسلامی در پی تداوم حملات اسرائیل به جنوب لبنان، سفر خود به سوئیس را تعلیق کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66458" target="_blank">📅 00:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66457">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30a4159b30.mp4?token=JbtPzwMJETEfkLvTc8CIJqpK7wBtQBMIh5zwrmGU2Qpb5AZ7ydNjb-3ru2LKUCttza3edCqtwZDGJJhB6-qVileNec2P8WwqSbXeV4j5HJFsy3WxZIrqnNxmCdrMa3eHmt1fFbh4JRBpBU1PNrT8b_bDTNGH82-Z4ygdySIiTmOFeMrZskQf8UkqrTLlNDJOEu94fcrMLsm9zF2Tnr6eHssp9sIKdZEWMu4VIktfCZnfErw5K4WgJg83D8UyL2z7udyp5zTNsjYKGftLk9gsgSqw7SqGPCoL2O9XockQdfbi_2Gq4wRk7oeEiLVxvvQihNYIy8Thhnq0IBGdW5Q4Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30a4159b30.mp4?token=JbtPzwMJETEfkLvTc8CIJqpK7wBtQBMIh5zwrmGU2Qpb5AZ7ydNjb-3ru2LKUCttza3edCqtwZDGJJhB6-qVileNec2P8WwqSbXeV4j5HJFsy3WxZIrqnNxmCdrMa3eHmt1fFbh4JRBpBU1PNrT8b_bDTNGH82-Z4ygdySIiTmOFeMrZskQf8UkqrTLlNDJOEu94fcrMLsm9zF2Tnr6eHssp9sIKdZEWMu4VIktfCZnfErw5K4WgJg83D8UyL2z7udyp5zTNsjYKGftLk9gsgSqw7SqGPCoL2O9XockQdfbi_2Gq4wRk7oeEiLVxvvQihNYIy8Thhnq0IBGdW5Q4Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جی‌دی‌ونس:
آیا در جامعه اسرائیل افرادی هستند که بخواهند ایران را به لیبی تبدیل کنند، یعنی یک دولت شکست‌خورده با ۹۰ میلیون جمعیت؟ احتمالا بله.
اما نمی‌دانم که بی‌بی (نتانیاهو) چنین چیزی بخواهد.
من شخصا هیچ‌وقت چنین گفت‌وگویی با او نداشته‌ام. گفت‌وگوی جالبی هم می‌تواند باشد.
اما همین را الان می‌گویم: آیا تبدیل شدن ایران به یک «لیبی ایرانی» برای ایالات متحده آمریکا خوب است؟ قطعا نه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66457" target="_blank">📅 00:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66456">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47cfe42200.mp4?token=uG-_dJ7l6D3e9gjghqPjR7NU8MzS0hMt3dhUx_q1S1ulqucl5-_AdeUcLcmCddEnNAVV61-T9waUogxie7kaR8DAGqDU8xmFBk2t9bHUVwMrt17-vGW5TKxtwBcQs6ZsXCVY6zlyPN2EGh8wT0uAzk_d_of4LpZmS8jbvu7KNrgGmlZr7MJXtgxssT4TW1n2MstPSSj7WX30Idscos0p9igdfUxSEpv9fhl-OGx2tAK8kDiZustA1kCxLI-Yc8MpVlNfNwkKwIAllDpV5MDmjIsjuFkYw6-4gZ-tZu3vrsd9_AIYp4vXZpcoA7C-4H5MIHJmRIOtXzd3ZdRBxyU7hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47cfe42200.mp4?token=uG-_dJ7l6D3e9gjghqPjR7NU8MzS0hMt3dhUx_q1S1ulqucl5-_AdeUcLcmCddEnNAVV61-T9waUogxie7kaR8DAGqDU8xmFBk2t9bHUVwMrt17-vGW5TKxtwBcQs6ZsXCVY6zlyPN2EGh8wT0uAzk_d_of4LpZmS8jbvu7KNrgGmlZr7MJXtgxssT4TW1n2MstPSSj7WX30Idscos0p9igdfUxSEpv9fhl-OGx2tAK8kDiZustA1kCxLI-Yc8MpVlNfNwkKwIAllDpV5MDmjIsjuFkYw6-4gZ-tZu3vrsd9_AIYp4vXZpcoA7C-4H5MIHJmRIOtXzd3ZdRBxyU7hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس این انتقام ما چیشد؟
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/66456" target="_blank">📅 23:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66455">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ad18edc1d.mp4?token=cF9MwL7SwZRawDjJ6yQtrJBh2RCsaX_eyPnVnezehQJ_43WXs8t1yefxNi7XXGKXQtOBf_K5KayRr9Myokq2Pm6LQoh5MtpzltC3-JmOvzKOHqN0G0h6l7vvxGu2SruWEiEgVa0Hm9xQ1XIUfk8hxFSM9McntI4yvCJsFiy2zJuodCSyGLPWF4sndk_gilOi2hbyHUqMT2YmpASieLfOm4OQD4IMADHYf5K8aapSo6PC5Cfw9uDwAhy7P791bmLL5uAvRKj_v8S2PKysLHQ4Agq_glGp_U4Q1KXDGELv7xaWPnbp--v4kZK4mkLsZlJxykccg4Mwpv8oYGLOkAw56Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ad18edc1d.mp4?token=cF9MwL7SwZRawDjJ6yQtrJBh2RCsaX_eyPnVnezehQJ_43WXs8t1yefxNi7XXGKXQtOBf_K5KayRr9Myokq2Pm6LQoh5MtpzltC3-JmOvzKOHqN0G0h6l7vvxGu2SruWEiEgVa0Hm9xQ1XIUfk8hxFSM9McntI4yvCJsFiy2zJuodCSyGLPWF4sndk_gilOi2hbyHUqMT2YmpASieLfOm4OQD4IMADHYf5K8aapSo6PC5Cfw9uDwAhy7P791bmLL5uAvRKj_v8S2PKysLHQ4Agq_glGp_U4Q1KXDGELv7xaWPnbp--v4kZK4mkLsZlJxykccg4Mwpv8oYGLOkAw56Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جی‌دی‌ونس:
آنچه من به برخی از منتقدان این توافق که شنیده‌ام می‌گویم این است که آن‌ها می‌گویند: “خب، ایران این همه منفعت به دست خواهد آورد.”
من دوباره همان چیزی را که قبلاً گفته‌ام تکرار می‌کنم و احتمالاً مجبور خواهم بود چندین بار دیگر هم تکرارش کنم: ایران دقیقاً چه منفعتی به دست می‌آورد که قبلاً نداشت؟ پاسخ این است: هیچ چیز.
آن‌ها هیچ چیزی به دست نمی‌آورند مگر اینکه رفتارشان را تغییر دهند. اگر رفتارشان را تغییر دهند، آن چیزی است که باید از آن استقبال کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66455" target="_blank">📅 23:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66453">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‼️
یسرائیل کاتز به کانال ۱۴:
ارتش اسرائیل دستورهایی دریافت کرده است تا در صورت لزوم، برای عملیات دیگری در ایران آماده شود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/66453" target="_blank">📅 22:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66452">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GA_2y2-wF_FHIv_i8nXal6V_9eZ4dhsy54R0bf0VU4ANqZmtHbFMlogLqI0fs6rOQcOoM63gYAbuy1mf1SRrfF96yKB9W4LntECLBzRZwU2oUL0j1c4S5AcLiC854i_v3cWjp6IvS-cOFRqnsEpN7p_KD-kX83l_XerHl-sx80rrgMx2jlGCfj2Zo7azO3WA7-l4Hl-u_ah4SL7E5eJfCoViYPS8yCdmg7EdfvUI-GGREnwIw2SDCg0PwtECCOaOJK69F9rW8aRRXZoBgcUsjGd8KVv5ebPWCCY_Q-orpHI-ASlfF-HtR7yxUKlMdus-4V0gNCqC4eFvSjNkyW-3ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در تروث سوشال:
ایالات متحده به صلح متعهد است و ما همه را در منطقه خاورمیانه تشویق می‌کنیم که به تعهد خود برای پیشبرد مذاکرات ما به زیبایی پایبند باشند. بازارها از آنچه که با کاهش قیمت نفت و افزایش سهام اتفاق می‌افتد، لذت می‌برند. ما انتظار آتش‌بس کامل در همه جبهه‌ها، از جمله لبنان، حزب‌الله و اسرائیل را داریم. از توجه شما به این موضوع متشکریم!
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66452" target="_blank">📅 21:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66451">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">هات نیوز | HotNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/news_hut/66451" target="_blank">📅 21:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66450">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
پیام جدید مجتبی خامنه ای درباره تفاهم‌نامه:من مخالف بودم اما چون بقیه تصمیم گرفته بودن منم موافقت کردم  @News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66450" target="_blank">📅 21:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66449">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">این پیام یعنی پایان پزشکیان و جریان اصلاح‌طلب در ایران، و آغاز حکومت نظامیان به سردستگی قالیباف #hjAly‌</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66449" target="_blank">📅 21:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66448">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
پیام جدید مجتبی خامنه ای درباره تفاهم‌نامه:من مخالف بودم اما چون بقیه تصمیم گرفته بودن منم موافقت کردم  @News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66448" target="_blank">📅 21:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66447">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRQxmI_DYqV_OQjImA-Ov9Ol58mVl45flkVLLo_KCxPyL9ZXWhVvCM9VIIFlsllVR0ODS6UBXZ59-1L14nw9sf37Y9MZjfQoPrn_XQ17J6qkfnUQyvYceznwJjGVY0JMqgHSxgD3ZbEmAp_vtQvGdH65NJDDRJD6FXPjwCCh7aF2wO4jHLCMACgFVV_hynsYHKcgz6oM7C5tTSLJXXX0tahclilZpyOTQ-lRCMODAtZG613i8rKisKtE7aGps-ZWCuWhMjbn1ABL156MIDNFvAkt4kerELz3zWrDokBWJSfgOAcNFnbpJBr0O5PhSiUiQsQ8oEhF-UOBErEn469bzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
پیام جدید مجتبی خامنه ای درباره تفاهم‌نامه:من مخالف بودم اما چون بقیه تصمیم گرفته بودن منم موافقت کردم
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/66447" target="_blank">📅 21:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66446">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3OvTgJOo9m3mLcQ83J6zk4MAiRPHirUSyyMeSq4Q13XHHhq_6RdK0hthcoFNErrdiG-3BuSmiQl1zSf5bUGpXG8xSma1HgVhW-SqwgzpZQP3kt-nxzqTlx2o52CXiB14x2HokjKxkTbGL4BNoBXvxSZ-qBaIx1zA2U0wWnpuBrtfj0KFFDT33u0Jv1JFr_sUm-AMRZIUSV049S01o9H9ta27Y2VIlxfsXWzZoCuiemANk59gwW6xu6OQD84KFBmi_cuqw7IWTqwxiGfYmaTaQETTz4IbW0n_i5Svyce9WNAhXeP1RL6DlC4AcoSGFuZVlImIfyybGUnLHd64-XMpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ: آمریکا هیچ پولی به ایران نمی‌دهد. اخبار پرداخت 300 میلیارد دلار به ایران فیک است. تمام آنچه برای آمریکا وجود دارد، موفقیت، کاهش قیمت نفت و پیروزی است. وضعیت بازار سهام را بررسی کنید. پروپاگاندای دموکرات‌ها در کار است!!!
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66446" target="_blank">📅 20:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66445">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‏
🚨
🚨
🚨
⭕️
سنتکام اعلام کرد، نیروهای آمریکایی محاصره اعمال‌شده بر تمامی ترددهای دریایی ورودی و خروجی به بنادر و مناطق ساحلی ایران را لغو کرده‌اند
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66445" target="_blank">📅 20:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66444">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f51df7dfe.mp4?token=jznQNtTOoO6PvaQ_iqZ6x0V_jnT1-_WlyH6IiR4UWRQO8hdq9CsrhrYuVrWkCLLhg51eHyYcFIJLsTdOApJCZTTldh9HrtxD1D-01f7EGuuBIgzGiPsY9Tdbh3F29affjMzcO66vPgunEIF3RVAV6DGdY0aW1hxRfpsKdEoBKt3fR_nAVLkUty-3SdUS9jNmXOWcUysIT3hLBVkLItQ7oDKYVvTFT0sc0_4YJPSwTrEYn9-09K1L2ouvQ3AH_IMISrTXBNYL0NsDb2xBItzFzE2PBzjs8eTUjOufuwMrB6oxZLz3mrata67Yb-Q8dOyENVABLoQ3FXK0gIbyUamJ8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f51df7dfe.mp4?token=jznQNtTOoO6PvaQ_iqZ6x0V_jnT1-_WlyH6IiR4UWRQO8hdq9CsrhrYuVrWkCLLhg51eHyYcFIJLsTdOApJCZTTldh9HrtxD1D-01f7EGuuBIgzGiPsY9Tdbh3F29affjMzcO66vPgunEIF3RVAV6DGdY0aW1hxRfpsKdEoBKt3fR_nAVLkUty-3SdUS9jNmXOWcUysIT3hLBVkLItQ7oDKYVvTFT0sc0_4YJPSwTrEYn9-09K1L2ouvQ3AH_IMISrTXBNYL0NsDb2xBItzFzE2PBzjs8eTUjOufuwMrB6oxZLz3mrata67Yb-Q8dOyENVABLoQ3FXK0gIbyUamJ8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جی‌دی‌ونس در مورد اسرائیل:
در طول سه ماه گذشته، دو سوم سلاح‌های دفاعی که از اسرائیل محافظت کرده‌اند، توسط آمریکایی‌ها ساخته شده و با پول مالیات آمریکایی‌ها هزینه شده‌اند.
مشکل اسرائیل دونالد جی ترامپ نیست و هر کسی در اسرائیل که فکر می‌کند بزرگترین مشکلش رئیس جمهور ایالات متحده است، باید از خواب بیدار شود و واقعیت وضعیتی را که کشور در آن قرار دارد، ببیند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66444" target="_blank">📅 20:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66443">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab365474cc.mp4?token=e1JeKF51PZQBe7kJ-ntmArJMRpsk92Vmr-JdNs0RP9NmxXW3xMNXT0UBeG_tP8RjAOU3P_-v8X5paFqOYdo3UR3rGfPlRm59VNAb7FdaCME8eLVz0K3Rlv1MibjRsu1ADvlW0RNQ9Fdwel98U2Uo-MDA1l81dOeqakm4mRmBEmnp4PNdcTsadrRMUgJU5O-seIfntqaVwJ1K9lWC4RF-Q31CVRAFGuuaWoPszuJghHxv00dGZXImCR78GivsrAWdJL9C3VMYyazNuZYAx6XFEvqUO2Hgcv0Ia0XeUz52tB77YWOjwfxNEsElPQKLUc_uddrD6fSStstzlpvsJ9_4Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab365474cc.mp4?token=e1JeKF51PZQBe7kJ-ntmArJMRpsk92Vmr-JdNs0RP9NmxXW3xMNXT0UBeG_tP8RjAOU3P_-v8X5paFqOYdo3UR3rGfPlRm59VNAb7FdaCME8eLVz0K3Rlv1MibjRsu1ADvlW0RNQ9Fdwel98U2Uo-MDA1l81dOeqakm4mRmBEmnp4PNdcTsadrRMUgJU5O-seIfntqaVwJ1K9lWC4RF-Q31CVRAFGuuaWoPszuJghHxv00dGZXImCR78GivsrAWdJL9C3VMYyazNuZYAx6XFEvqUO2Hgcv0Ia0XeUz52tB77YWOjwfxNEsElPQKLUc_uddrD6fSStstzlpvsJ9_4Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏جی دی ونس درباره ایران:
آنچه واقعاً اینجا اتفاق افتاد این بود که ما روز یکشنبه تفاهم‌نامه را امضا کردیم. این توافق‌نامه مفاد توافق‌نامه را تثبیت کرد.
چیزی که ایرانی‌ها پیش ما آمدند و گفتند این بود: «ما دوست داریم متن را تا جمعه منتشر نکنیم.» من واقعاً متوجه این موضوع نشدم - می‌خواستم متن را فوراً منتشر کنیم. اما برای اینکه با آنها کنار بیاییم، گفتیم: «مطمئناً، باشه، تا جمعه صبر می‌کنیم.»
و سپس آنچه در روزهای دوشنبه و سه‌شنبه، در حالی که رئیس جمهور در اجلاس گروه 7 بود، اتفاق افتاد این بود که شاید رهبران خارجی با ایرانی‌ها صحبت می‌کردند و آنها را به انجام این کار تشویق می‌کردند.
ما قطعاً به آنها می‌گفتیم: «ما تمایل شما را برای منتشر نشدن متن تا جمعه درک می‌کنیم، اما می‌دانید، ما در یک سیستم دموکراتیک زندگی می‌کنیم. مردم آمریکا می‌خواهند متن این توافق‌نامه را ببینند. ما مطمئناً دوست داریم هر چه زودتر آن را منتشر کنیم.»
و بنابراین آنها به این نتیجه رسیدند که رئیس جمهورشان آن را امضا کند، رئیس جمهور ما آن را امضا کند، و مهمتر از آن، شعار را تکرار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66443" target="_blank">📅 20:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66442">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66442" target="_blank">📅 20:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66441">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kwX6AxQNL_kZHyDujoRRRmrWtHbius_WnaWKEMwEcCwOfgndrhVY1D_r4Hfq1MEA1foXJDOrh776L9rwfZbCfU3zVggdccUYVkrrmLoe5m23No-VJm8dkpfKAiBx4SmgvvmlGKeJgGooM8rYHa7hKBPoT0dcU6EOz4-hkkDQP-vrvepgUYSWkOF-NGGsDbvncY6PdSsRAjSKVyX4bstVpbPMC-4vrofAwuMdNaJXmwPwNRWqvrUZ2oI2cu_Kpp2HjHpz1IFfgUmt2VEoLeX5y7DtrP4OxSWHJ_I10UYbuk5SDE149LM71cZ6LlOQNO0FOkcLgNDH1JzwRpTjER86DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66441" target="_blank">📅 20:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66440">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b31dd3b8.mp4?token=OZ7ZwpNmfT6bWXyUUI2Y81mXN1MvNZtXdrG_WJdRzWzTe7FYBOtEkDZZItRGK1VP5b7GlhABp_CT6-KFuNldS2vQIvj28zkCKYx8Ey-pnu9yLhXkoy5LKO-bjHX30ZO48BQJOdCou2EmqLNx6JnwnipGe1Vwn-E9696X3nlXD87oR9vl5C2efzUqQYIm3lzTjWcKbvDpVuZg5SkGKfAr99l4onuCmmeTTtXauZhb5c7RYPpneShkMIzdf07DBIyKG2z0Y7yN94weICN78L5lebagvxj2eSz5IFb8fm0ksrV3D3_AJ7_DQb0P6HRVNizXooqOUrUWRj29VSp3C9QFfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b31dd3b8.mp4?token=OZ7ZwpNmfT6bWXyUUI2Y81mXN1MvNZtXdrG_WJdRzWzTe7FYBOtEkDZZItRGK1VP5b7GlhABp_CT6-KFuNldS2vQIvj28zkCKYx8Ey-pnu9yLhXkoy5LKO-bjHX30ZO48BQJOdCou2EmqLNx6JnwnipGe1Vwn-E9696X3nlXD87oR9vl5C2efzUqQYIm3lzTjWcKbvDpVuZg5SkGKfAr99l4onuCmmeTTtXauZhb5c7RYPpneShkMIzdf07DBIyKG2z0Y7yN94weICN78L5lebagvxj2eSz5IFb8fm0ksrV3D3_AJ7_DQb0P6HRVNizXooqOUrUWRj29VSp3C9QFfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جی‌دی‌ونس:
ایرانی‌ها برای دومین شب متوالی به هیچ کشتی‌ای در تنگه هرمز شلیک نکردند. تا این لحظه، آن‌ها به تعهد خود پایبند بوده‌اند.
سنتکام اجازه داده است دوازده کشتی از محاصره دریایی ما عبور کنند، بنابراین ما نیز به سهم خود به تعهدمان پایبند هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66440" target="_blank">📅 20:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66439">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTutDcWy2YeMvCin0VqIK7_6nOCKxpODIHB1JLBTYqpw26Aw1nqqpSccdB57Vo_GJwdeNXebIx2EKeF5jEybA2DRYXkbFD66GvgHTYFO4aQNWCR6mAAKa7FsT7R-u5iv5fdPOmUmm6Kl_wu9Raq3WhkiYUsc84jITFTE_J7tdGljm9aYHIj6CUFhz-8Nkz2Pr9DOKL320yM0KYuPoNwz_hetQYTiUqUC4cqZjMJ6hml54jq8SafHI5n8jlTQzdjWspBnoOtaxXnmVVHDET33zUKG2axs5_Ep0XVr4oWRSdp9oNxJScZensJtmg4B-DoBNdtr5sfUnwjxTOP2j1VGpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
فایننشال تایمز :
گزارش شده است که ایران به ۶ میلیارد دلار از دارایی‌های بلوکه‌شده خود دسترسی خواهد داشت تا کالاهای آمریکایی خریداری کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66439" target="_blank">📅 20:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66438">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZhzo0hUG_RUwWTbzMwWoDQq_ahan7ejde0tUUu8e6JOy0rxxI1jpRM8RVx4XAH11Q4cQiK4P0_t84e9L2kn2OTID0uFwLq2cPnztK73QC8REZKUJ5KBggz_yo-_6anYkjvJsaFfxaxI9IeYsy2I3xUJgspOq8nUnUeSLOawx7St8VizqGDLXdhUvEXxh5i6_mE_0BsglxysZa41zztOwqrNIel71cqVVMMNcQmN-DpbHbX-U-8Gse0tTlrDJJ9TkYeWRRRHdtXJkLiwED6RyOHGGJB5FZBWvdSio1-mJ6jTo5ljTQvN6WUVSM1XfGXaqQTId8qNKN3oBYMc3xk5HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
ونس: کجا می روی دونالد! «امام مجتبی» منتظر توست!
دونالد: از روی امام شرم دارم ونس! شرم! توان دیدن جراحات ایشان را ندارم!
ونس: تو هر کار توانستی کردی! تصمیم امام اصلح است بر ما!
دونالد:‌ چه کنم! چه کنم ونس! با این جماعت هزار رنگ٬ که دروغ را چون «رج قالی» میبافند! امام مان تنهای تنهاست! شرم بر من ونس! شرم!
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66438" target="_blank">📅 19:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66437">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd4fb90d19.mp4?token=YodP_5x8QTXvBeWR7jgysAprIz6SoML9UXSZMPoVIM5JibVfYvVcxCfDQjK8hlxNUZqYeQmusq8D3wTCAElNj_dGKEA1eRVrrbMz5J9cxPyiqkgr7VT1y7POyLn5lxqZipoV_AZyXMloHEktYk0Czz4NtLKsByXOKQWlzhKIQSaPPftMdQ_3CNY5t9xQlqtSGE93GqOmBTZE3GEOyPeG1QDmAR5n5I2Eo-Lb-8nqFSCj98AYe4oVLqQ5ETrLHjmoi-qYPbunpLbvEN-BA-zMqhZGXas7Rj8ka9ngYzswrHBY_AfW7JWUDnjZLfj0AHSJTw9bjhrFw1A_vf-LY9GAsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd4fb90d19.mp4?token=YodP_5x8QTXvBeWR7jgysAprIz6SoML9UXSZMPoVIM5JibVfYvVcxCfDQjK8hlxNUZqYeQmusq8D3wTCAElNj_dGKEA1eRVrrbMz5J9cxPyiqkgr7VT1y7POyLn5lxqZipoV_AZyXMloHEktYk0Czz4NtLKsByXOKQWlzhKIQSaPPftMdQ_3CNY5t9xQlqtSGE93GqOmBTZE3GEOyPeG1QDmAR5n5I2Eo-Lb-8nqFSCj98AYe4oVLqQ5ETrLHjmoi-qYPbunpLbvEN-BA-zMqhZGXas7Rj8ka9ngYzswrHBY_AfW7JWUDnjZLfj0AHSJTw9bjhrFw1A_vf-LY9GAsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خبرنگار:یه مرد دانا سال 2020گفت ایران هیچ جنگی رو نبرده اما در هیچ مذاکره ای هم شکست نخورده
ترامپ:کی اینو گفته؟
خبرنگار:دونالد ترامپ.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66437" target="_blank">📅 19:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66436">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AD2tNBR8Ct1_uS5AeifJREA8p6RE230O7wYW4b1Y5bXfO69v7i3k5wWNFbVEo8xX5nL-0w4bNmW2M_YXhlzs6PwPl9ZHGUhC4HjgZiuL_TE_HHB6iaGA1bti2vvp3JcznXtxqU3RVmo-iZg6iIq9hJl53QWp7GVGrOi6bFNaRVbyuW9lj4QiTKU1IeOoR_rpltYEDJ0B3wJjEllQtQ8R29U-rQqxCBX1lZ4Y9GqvnYn9DACywv2YBBC0GguUpw-Y_JAY2uAQbrehgFgJXTXWqFlOzq02UaoGnjKgMFXfdAERgLVxeJ9HtRxpz6tC-uj_Y9d2nfUJV94XQ3OZw59qog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
الجزیره به نقل از تلویزیون پاکستان:
سفر برنامه ریزی شده شهباز شریف به سوییس بدون ذکر دلیل لغو شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66436" target="_blank">📅 18:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66435">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TH-6mla-vKxsA9gCi_1by-djmpilT5t17d8KJ_bqgmiyRxW-TYFKamHsfCLFslJe2uDvV3KTr6cH4OVz85HjsS10-3Lb_Vdb4U3tMLnxvjJClISEAROsRS6AOnRmDOHgzrABuE50_xc0IadnRgOM-v9zMChU4-eEejYAOeWrZkaEmmL83atRGkmZYT69Py_typl0lK4zWQIYuZCKLoCPER5DjCk8Y6AXxehQAnvhjp_CNy5t8CsoZhTmWQqzo7I36MPanY2oABiIRGcj5rWnQbcZwRQqDsfnDB3FKq6pRETzghj4P6Bv00zruKVg8CE3TrXr2Fj1cyrIrYJ1DKghAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
نفت جریان دارد، ایران هرگز نمی‌تواند سلاح هسته‌ای داشته باشد (جهان امن خواهد بود!)، بازارهای سهام در حال رونق هستند، مشاغل رکورد زده‌اند و قیمت‌ها در حال کاهش هستند (قابلیت خرید!). کشور ما قوی، امن و محترم‌تر از همیشه است. «خواهش می‌کنم!» رئیس جمهور دی‌جی‌تی
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66435" target="_blank">📅 18:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66432">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jB0CEXaBhBY8PMrpv6adyh3YOC-RedxzljkimGEsnDRMqTS_eWnyDA38eF-v6biqQtaTKHfQK3LqhgNXj97Z4kie-RCz4dSSFTNhJ-108FrmTt6wk9LQrOECfVlvLqRJPhMFmAoNjkBlJS4QBotOzNuN4lipshl7c_h0VNeK_lCFoa0mOl616h2e2ITLLU2NW6qAWGPWVWnjWyWtbwDrGi88nExmXip4ao8brUBez4dh_CtOfye1HSr5vp0AJg1tXoT2ACoFdF3caEC5heeS9vaO2ESDY573pZY-xey8KCXfckUO_CFIlloshJeYpD1KM8dwZ2QMhxz0SEKPSqvVWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QvjQrlat227AiC6h-DwxRAKzYr1e4TE61VbA6JVIXOGAbIcwQVZ0KtdDQSATgbFnrXgtml1e2TM5YHrpaGGavvvI551uD_A0W4QQzSIHerjYh2hIxcvmp_4U5tGoy1Qxb4h4azioICAD65UbuZMQV1cM_uZWwgGULvQw1EEWIHTRQ_kfUQUGLcNplV994i-OiKP6SIPSVgy2wa-LgUJT-_9waNXhW5EuM5QAi32CyMC3Gc6JTze_MO9DTxeyq_vPEVAj6yKi5cMbDCyaJsuqjRvX9AfS4ANpj9H4zjxbJKI19A8Y0Nps6WENz-N8Sa9To9Gm-IFR9ql7FkNypypwmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13c6e64c5c.mp4?token=TTby7iJ9biP1B1G12iUOZh9e0hiQOESf0Im5qQpnQXqykR9BsodekGAWok7x-AlnKg7c9QOrE3-iErGPXIahAdbc3QHswJe_iJRq1QYKgbK7oq1Plmv0n7UAAX1xSPotyKMwcCollUm5ujP3EYQ77XNGaJ2t6W5FuCyoHMo2K_5xLe7CNb6Bu1lGEY1t_pA4YxZV3YH0Ru3sVqWIBaWVkltw2cB-g_jX4zZYPjAtzqBCiJxq-HbL2Zg-VUIIhL5inI5kk7Ywy9r_yLJR1tyFqMYn8BgPyUAM3M34Yeag4DqjFXKNLwYq7YLUoMSAtru8yHuvbwuTOBfU-8-h0kzn7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13c6e64c5c.mp4?token=TTby7iJ9biP1B1G12iUOZh9e0hiQOESf0Im5qQpnQXqykR9BsodekGAWok7x-AlnKg7c9QOrE3-iErGPXIahAdbc3QHswJe_iJRq1QYKgbK7oq1Plmv0n7UAAX1xSPotyKMwcCollUm5ujP3EYQ77XNGaJ2t6W5FuCyoHMo2K_5xLe7CNb6Bu1lGEY1t_pA4YxZV3YH0Ru3sVqWIBaWVkltw2cB-g_jX4zZYPjAtzqBCiJxq-HbL2Zg-VUIIhL5inI5kk7Ywy9r_yLJR1tyFqMYn8BgPyUAM3M34Yeag4DqjFXKNLwYq7YLUoMSAtru8yHuvbwuTOBfU-8-h0kzn7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پختو پز اوکراین در مسکو پایتخت روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66432" target="_blank">📅 17:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66431">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bf3ba597d.mp4?token=SK7e-k4rbYIffqrtDSkUNinfEvKZPJeOvoIVaGWA8I6XF3KJLi64od-iCFpbgX8gP_GFFrtoAkQRh2r6CwCWWJHoE056Omvkm7D7xMUExn5Ql5o-R2kVPSQd9YPj19u2cEKvEQryFMO8nH9FYx0loTEuUEeFZyf9ytZAc4NSOaqe9CAHQbZTeCIBICs0pIeay5Wj5zC1du64senqj9fzETWJuhOtAKBIdrP9p72SM_b_WrHiPbcFL7I-tOE6EDnstRBZeZx-E-0kMpUXyVPrMXsGhaKgoeWX4JA_JbE76TdwOwkMQa38zQBTu1HqretB5OXgXv_C12ngjgeqbYt5bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bf3ba597d.mp4?token=SK7e-k4rbYIffqrtDSkUNinfEvKZPJeOvoIVaGWA8I6XF3KJLi64od-iCFpbgX8gP_GFFrtoAkQRh2r6CwCWWJHoE056Omvkm7D7xMUExn5Ql5o-R2kVPSQd9YPj19u2cEKvEQryFMO8nH9FYx0loTEuUEeFZyf9ytZAc4NSOaqe9CAHQbZTeCIBICs0pIeay5Wj5zC1du64senqj9fzETWJuhOtAKBIdrP9p72SM_b_WrHiPbcFL7I-tOE6EDnstRBZeZx-E-0kMpUXyVPrMXsGhaKgoeWX4JA_JbE76TdwOwkMQa38zQBTu1HqretB5OXgXv_C12ngjgeqbYt5bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تردد کشتی ها در تنگه هرمز پس از امضای توافق
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66431" target="_blank">📅 17:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66430">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzI2LDCvH5_DuuCBxUmK5rUq2I9tK-hC1eXqUgnUsGo-ivcbgMQ42d8oVeAOLS6GT6XYY3zY8QEfmyimkbOjW91goFqc9AlrSoSUAh0Qv5buVkPB4cK_GF1fC8oRyM5Cb6rUwKpar7DUvysKISm79pCeXn-EIXobms58LyVTduGryynGqBpv7XJWjHgxjkZV1p9rU9r0RhLKWUvn-lr0HmQa8zBNI1LH0HcB-yfWBWul__58FRRIcd6NTnT4Ss3LxOZ2LsizWBrj92y97FXVUClxHV2IoKfpV8yJ9KPUVieI0EyxAOh0-HlwyBgWtaFOXvFD84gGPKazBXN2YE51ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
ارتش اسرائیل؛منطقه امنیتی فوری در جنوب لبنان:
نقشه منطقه‌ای که نیروهای دفاعی اسرائیل در جنوب لبنان در آن فعالیت می‌کنند
بر اساس نیازهای عملیاتی، نیروهای دفاعی اسرائیل در منطقه امنیتی واقع در حدود 10 کیلومتری داخل خاک لبنان مستقر شده‌اند.
نیروهای ارتش اسرائیل در منطقه عملیاتی جنوب لبنان مستقر شده‌اند و به تلاش برای از بین بردن تهدیدها و بهبود دفاع از جمعیت شمالی ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66430" target="_blank">📅 16:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66429">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZaB05o2CYo8_rETqidhoUthUJCuXepLEqmX33usOFY6ecJw7sUUIUL1ACksPrn-MLn3lnOETfHql9InGQOz-iOU1N-zFSXP3E9tCCRZNcdfywaM6q5rMkXZvBTBYKpcikt6mxUsKnBvEi9fbmGFfTpcDsTKReNqABrCtA3JPWuodfXGzLyID7Zwe1iU78WQAFtIkqTQtrP3Nztw2mbD50-8CrVPJWbgOgLQ3T9RTcyAh-HF1EOly7znmC4Nu0tYlFH-1aW9D2rZxmy3dS4w4O5pQMggWziMP4tRalUS0oV1GAbFRJ6Z8UjmQp3Pz0ZJBUYBCS6qFIT2MlMqL_yIQTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان؛این یک سند تاریخی و پیامی از ایران مقتدر است:
صلح در سایه احترام متقابل تحقق خواهد یافت.
جمهوری اسلامی ایران به صلح جهانی با حفظ عزت و استقلال، پیشرفت و همکاری منطقه‌ای همواره متعهد و پایبند است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66429" target="_blank">📅 16:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66428">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/622db6728d.mp4?token=CpxlsnfpmBAxZOUCw58O-1_miR2Iam6hS8T77btB5ytAyFKL953fiKAt_36Tpe6VtMI6OdCrHL4slvjGfn7YJ1r3ecr0ySYmTe2gayyLwclYsbXw6GMcIoSBeC96qd8RvmEJp-NQUzO7pnI3brGoTmnxy-Zao6PADfcoz2kW4EF6nX93BuC49CxCFPH0IeMcy5888_JLuzWZp35jZkwqOmH7FS7H6bWqR8D4WX_kziuDRBLVQLqgQZ808-TinrPAUypA67MXKmsVycqwolJNpCOh0iLYSvNeKk6i8YsqRIsGohSNZjR6Qfx2AbOXZq1DJmI40adVZ1Nw5RGoAGNcNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/622db6728d.mp4?token=CpxlsnfpmBAxZOUCw58O-1_miR2Iam6hS8T77btB5ytAyFKL953fiKAt_36Tpe6VtMI6OdCrHL4slvjGfn7YJ1r3ecr0ySYmTe2gayyLwclYsbXw6GMcIoSBeC96qd8RvmEJp-NQUzO7pnI3brGoTmnxy-Zao6PADfcoz2kW4EF6nX93BuC49CxCFPH0IeMcy5888_JLuzWZp35jZkwqOmH7FS7H6bWqR8D4WX_kziuDRBLVQLqgQZ808-TinrPAUypA67MXKmsVycqwolJNpCOh0iLYSvNeKk6i8YsqRIsGohSNZjR6Qfx2AbOXZq1DJmI40adVZ1Nw5RGoAGNcNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی بعد سه ماه هرشب توی خیابون موندن و پرچم تکون دادن ، بهت میگن اقلیتی تندرو و خون رهبرتم پایمال شده:
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66428" target="_blank">📅 15:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66425">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4faedc1ad.mp4?token=bfNcVg_6N-QOX4ym6imwfKcHp76EgxNjdQKANZ7uRm28rK2eOgIpZhDYmvQVp2eSmAFq5azjnp9jk3TMshlLDNgF4vTT08HpOlEeE4jKE5q4hU4ZIwsgF-TUM7zMfhG7pNqMtzZZWyeK7lURv6PyEH0uwPameO59dLTCkr2P9DCeOahHsj-vbQXuTe0GMHcb9e3R60V1jl4TRWDwnJVRjXG-bG7ATzqvbDDEdxo0H3PJi83QxKBIWYKpkGJzBNSBtqQ4W8QtPfRk-bOmIM7pQSGY_F7_4ABtp4DXcrXCsXka3D1kp4X5OmbdiQZ43cKaSqRHy7ni_F5QeoIXPsBX-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4faedc1ad.mp4?token=bfNcVg_6N-QOX4ym6imwfKcHp76EgxNjdQKANZ7uRm28rK2eOgIpZhDYmvQVp2eSmAFq5azjnp9jk3TMshlLDNgF4vTT08HpOlEeE4jKE5q4hU4ZIwsgF-TUM7zMfhG7pNqMtzZZWyeK7lURv6PyEH0uwPameO59dLTCkr2P9DCeOahHsj-vbQXuTe0GMHcb9e3R60V1jl4TRWDwnJVRjXG-bG7ATzqvbDDEdxo0H3PJi83QxKBIWYKpkGJzBNSBtqQ4W8QtPfRk-bOmIM7pQSGY_F7_4ABtp4DXcrXCsXka3D1kp4X5OmbdiQZ43cKaSqRHy7ni_F5QeoIXPsBX-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حملات سنگین اوکراین به مسکو پایتخت روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66425" target="_blank">📅 14:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66424">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d92b0722cb.mp4?token=ahr0GGjeXeK7QJWDqSfMdx2tGoH0IZt43rVKSZUhhxQPX7T1rHPDCiicLIrncPYnUwLb7LjMszC5kLmNW8hJX-z0mfOfhxLQTCacBYH-lfk3pWOcqe0Daxw8i5vB09488Mm90seZXErHd0GqSDyeirLhHo63SviAAdKu-ZX2nZCIonFlB0Cx7onDDUq_0xG3PZDgDDxyXahv1hsIappvbYlFY4EbiUGk9DpvIR1wLuVr4CSj5zOSo4xrUwL9j57_BgOSKx6LHUbvz_jErLWrbT7RcmbTrFv0gzBNonfe1UQnnDKtB5mKA1NkmAYEmz_7ibeOVYaBRZha9-QNPM2OHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d92b0722cb.mp4?token=ahr0GGjeXeK7QJWDqSfMdx2tGoH0IZt43rVKSZUhhxQPX7T1rHPDCiicLIrncPYnUwLb7LjMszC5kLmNW8hJX-z0mfOfhxLQTCacBYH-lfk3pWOcqe0Daxw8i5vB09488Mm90seZXErHd0GqSDyeirLhHo63SviAAdKu-ZX2nZCIonFlB0Cx7onDDUq_0xG3PZDgDDxyXahv1hsIappvbYlFY4EbiUGk9DpvIR1wLuVr4CSj5zOSo4xrUwL9j57_BgOSKx6LHUbvz_jErLWrbT7RcmbTrFv0gzBNonfe1UQnnDKtB5mKA1NkmAYEmz_7ibeOVYaBRZha9-QNPM2OHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‏جی دی ونس در مورد مسلح کردن معترضان ایرانی:
در واقع تا حدودی دشوار است. می‌دانید، نمی‌توانید همین‌طوری از آسمان سلاح پرتاب کنید. واقعاً زیرساخت لازم برای رساندن سلاح به قلب مردم ایران وجود ندارد.
یکی از چیزهایی که رئیس جمهور خیلی نگرانش بود، همه این معترضان بی‌گناهی بودند که توسط افرادی که چند ماه پیش مسئول بودند، قتل عام می‌شدند.
آن افراد اکنون رفته‌اند. اما خواهیم دید: آیا این رهبران جدید با مردم متفاوت رفتار می‌کنند؟ مطمئناً امیدواریم که اینطور باشد.
و اگر اینطور نباشد، می‌توانیم وقتی رفتار واقعی آنها را ببینیم، بفهمیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66424" target="_blank">📅 14:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66423">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROtDC11ECLvFJxRlsc9sQWuBProMopGo3RPbgNnnNJA_Jiqb_pVmUcqmTqn3RAniaoMG9Icvz-6pLMZteHbIXjv7vX78bYEsdFnxE83ihJXlWQKuuELJQUnYsc8H7NHryUe0euCsTDeale50TmDb-ENa0szNugFE00XelGhd4bA1CRXeFttmnZlnw2aSfsCQ0V2PfS71VA3-pHV9gqnWN6n27oDejrcLzRpFLWXwEsGX4Vt_LgTTGboXd413X0F0gztY8jcmww_p5-rvl76eIWxQT3Bs2pTD8aEsh5sDLUkFhdPTigu-mV91rhyljDrqDANbm5MZRS2e2OEYl2PGHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حملات اسرائیل به جنوب لبنان همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66423" target="_blank">📅 14:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66422">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66422" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66422" target="_blank">📅 14:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66421">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkyfuEh8JFUCSa2Tm2PKP-jWiZpbtDnmXvFnfe54Yc83RLEcm4cQ1ZU2aJY8LJKOhmVA8UHx6Fnrze1mWG8P1jfuTmkIVJ6OxZul9ejOvnX63ZLsBKxcXIwk_p6hkG25j_1fT7IoPEWigIXfSZvSUcJMA9ATHviMWh9CFaNpBWifR9nTovzLyiMTt3bbx1h2amom70sPMiR-mK2cns6TkFu4pHMPvqFc67JMJO5phK601rqMUkUirTBlHcRD4uJz-sIr-sn5XqO4AiArz2JbjALOSQH8kDMe2d5I5D2WD6-fYs7KRSH7QlNo2pHBAcmFPamTXM1sMSfTR4xAUvrscg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66421" target="_blank">📅 14:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66420">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jgikqoh5XmpR-2-bJJCPL8Za2lK7AXYergqcY0cl2sv3fASMldEGMjneTHP23UoD6bF86Anj15UAkxCfD8mop1dIoFWfiJcnWwiAuhNnp75c_4l9Oyu5R3yFgvgeoj--APcO0EqYc1g2YDqQ6fV9mP2X6rt6-n-X8LRg9B85DAu0i4ih32kk0urjaIdnM7ABIQvqVySrGVvnerpB11JprsYEKo-KlwJb2LmAhn6O3KzsyuayOImXM82uB-j6-4gHE9zUKuqjAr6Mu1gP4wkqofjzTurrs_TH5Us69vskypXI3Qpaq-Rh6BeWWD0HMpTlzMfXJSgkDijgwp0lVGdr3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امضای پزشکیان از نزدیک
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/66420" target="_blank">📅 13:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66419">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1890fc432.mp4?token=uAPth8ZMNOxRRNw_JM2x8zO7CIfMHTYiH8FpTyRco98Wuxx7wNgHcCGrbSZrIzip0x8JmwByX92nz4AAjQAnSLpkSH9awNJf7d0cdZm5PN3fEUp5y9rrltKm6Lp-uFIxlg5zepukJ614cv809t9Agarzg89pJUMFvroXx6cOokNy1mPY_Q_IVMtzQ3ZC8YBJwkXHD2t52-YVSZfPU9dt7aAH30wNPZ8UY5LPyzM6t0ertF1R25GyUuPW8LsX4n4puNjN-MbKSE_cQXIcEZH5gxdb0sa2lNPRBeE8Go-E84oQri5sZmNleDoq7nHxU8eEnajuLvQWqK2EO-l3EiRuLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1890fc432.mp4?token=uAPth8ZMNOxRRNw_JM2x8zO7CIfMHTYiH8FpTyRco98Wuxx7wNgHcCGrbSZrIzip0x8JmwByX92nz4AAjQAnSLpkSH9awNJf7d0cdZm5PN3fEUp5y9rrltKm6Lp-uFIxlg5zepukJ614cv809t9Agarzg89pJUMFvroXx6cOokNy1mPY_Q_IVMtzQ3ZC8YBJwkXHD2t52-YVSZfPU9dt7aAH30wNPZ8UY5LPyzM6t0ertF1R25GyUuPW8LsX4n4puNjN-MbKSE_cQXIcEZH5gxdb0sa2lNPRBeE8Go-E84oQri5sZmNleDoq7nHxU8eEnajuLvQWqK2EO-l3EiRuLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
لحظه امضای تفاهم‌نامه توسط شهباز شریف نخست وزیر پاکستان
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66419" target="_blank">📅 13:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66418">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50fdfa7aaf.mp4?token=pb7rerCdtW0MPJYaStE4f3gMS1J3KOZp7x5zK7mCkcymOhQoOnb964-uzznHUMpoHVjfnDkwIyulxpfsOHZplfizU4zp6LNrl9EdAuhKoEnfyBCYFKdaOXDe91ErwQ3QdvV0WLhHa7-rWtKDuDhwT0XHJxqofP2MYBLQkeUVn9qpBRlWLxPNM02hcKvLuOfK4TthMpGsa3actEC54fc29ImYfHCvANYSIAjyOs-L-m1ZJhN50hqYlVgoLTyFtvvnRq1uQWXr8te-w_UNx_spkH9jN-9fAFPrkBI-RUJUIHPkO6IUfLOfF2jk2NKpW-9m67eyB68CrtbcLPX-IItqjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50fdfa7aaf.mp4?token=pb7rerCdtW0MPJYaStE4f3gMS1J3KOZp7x5zK7mCkcymOhQoOnb964-uzznHUMpoHVjfnDkwIyulxpfsOHZplfizU4zp6LNrl9EdAuhKoEnfyBCYFKdaOXDe91ErwQ3QdvV0WLhHa7-rWtKDuDhwT0XHJxqofP2MYBLQkeUVn9qpBRlWLxPNM02hcKvLuOfK4TthMpGsa3actEC54fc29ImYfHCvANYSIAjyOs-L-m1ZJhN50hqYlVgoLTyFtvvnRq1uQWXr8te-w_UNx_spkH9jN-9fAFPrkBI-RUJUIHPkO6IUfLOfF2jk2NKpW-9m67eyB68CrtbcLPX-IItqjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیرزن کسخل مکرون دیروز موقع عکس یادگاری سران گروه 7 نزدیک بود زمین بخوره و شانس آورد ترامپ بغل دستش بود گرفتش
😂
😐
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66418" target="_blank">📅 12:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66417">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">قطار پیشرفت آموزش و پرورش کشور خدایا شکرت   @sammfoott</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66417" target="_blank">📅 12:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66416">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4IfCyfuqhzYPqKODexmP2UXX8pmujMVteTLWOJ9XmWE7-H3jzUvtetS72iY87HspNKGH1FCJpjgkrjxoGZaj521wcWO4QhlRtg7Lv6quQWVJJ8YOYxxFoLxqcsnRWBEttIdv_ocU88EWjwjU_5x2EVDFLR1rr7RAYjL1eM37ypKJvrBu-BViDz3lR7f_o1hR6YHOExWPY0R1-hhnnLL9KdiNWakJe1QJEpSg8Qyb1mwfLA9LAKx3LMOaddPsqb_LSojIGQ9kQZHivpExtVTOPcIV41YXjgHd9CAJ7iPU-qbPPmFgFxS8ZeMmmJlrL_FioT_5K49RgeEUuJZ4cBqAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«این احمق‌هایی که فکر می‌کنند من با ایران به اندازه کافی قاطع نبودم، در حالی که بازار سهام به تازگی به سطح بی‌سابقه‌ای رسیده و قیمت نفت در حال «سقوط» است، یا حسودند، یا آدم‌های بدی هستند، یا احمق. بیایید دوباره آمریکا را بزرگ کنیم!!!»
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/66416" target="_blank">📅 12:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66415">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16c0579b45.mp4?token=Gq38pauXBfSmtFsy-FrMP8-o62IatSJQeQzUvGPdVXRn-yzlq9vL2_VCTp8W9TovdCCzrwWD-QFM2Tep5mUm6Kh3NcI_Pj3BnrO7EcPt57NPG1NSC9Wuj_iW6CddxJMPFV-EcjimO9OJ269CgBYidolyesHEOAZjSYAZNOHBrdG5rRyTtjAQHEqdXDl4-dLb2nt6KhWRRC607egP7zwxEc4ipfQRvNeE6IMJ2Api7kvZjON8GGSgmKBkn7XJQdsaJGxvGzWqUVukCt_iXz3CWqv8tNzoSfIGdEyw15F8rTUrMW90AUXNxVFfdLAr8QXD3xBGuQeTzmqTLWcZQ-G8sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16c0579b45.mp4?token=Gq38pauXBfSmtFsy-FrMP8-o62IatSJQeQzUvGPdVXRn-yzlq9vL2_VCTp8W9TovdCCzrwWD-QFM2Tep5mUm6Kh3NcI_Pj3BnrO7EcPt57NPG1NSC9Wuj_iW6CddxJMPFV-EcjimO9OJ269CgBYidolyesHEOAZjSYAZNOHBrdG5rRyTtjAQHEqdXDl4-dLb2nt6KhWRRC607egP7zwxEc4ipfQRvNeE6IMJ2Api7kvZjON8GGSgmKBkn7XJQdsaJGxvGzWqUVukCt_iXz3CWqv8tNzoSfIGdEyw15F8rTUrMW90AUXNxVFfdLAr8QXD3xBGuQeTzmqTLWcZQ-G8sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط اونجاش که یه موز و دوتا پرتقال بود
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66415" target="_blank">📅 12:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66414">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb19ef0a8a.mp4?token=WLa5LzOkfUjOaIP02SqZFBMOQdfYh0xcU4AmBe4jZG5rkkbhx-rVQ_4ObcSyVnsuBPQzzJB9EHBlskYLIZggqaw8LSe88jpJVgxlfFspHwby9YfeDK7ZLN1xJgAJ2wdXwSO4xgHG1vd6W44oTwoesRsoD8ilV5w16UGlu1IJ64qRHfSWahIpcMrPDmPFvmEWn_q5EPi4qThav68dZvBOTUfkQLXuoigHRIbBmhBoAVePNvoVJ3nfMuVDlfiBJoHcBU_ylfpCibfywrFq8CrJee8yY6JG-edOz14HTAy3IZYdnamH3stm7OitsHfPIaYApb3pMwM7RiUr-CscWKD7_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb19ef0a8a.mp4?token=WLa5LzOkfUjOaIP02SqZFBMOQdfYh0xcU4AmBe4jZG5rkkbhx-rVQ_4ObcSyVnsuBPQzzJB9EHBlskYLIZggqaw8LSe88jpJVgxlfFspHwby9YfeDK7ZLN1xJgAJ2wdXwSO4xgHG1vd6W44oTwoesRsoD8ilV5w16UGlu1IJ64qRHfSWahIpcMrPDmPFvmEWn_q5EPi4qThav68dZvBOTUfkQLXuoigHRIbBmhBoAVePNvoVJ3nfMuVDlfiBJoHcBU_ylfpCibfywrFq8CrJee8yY6JG-edOz14HTAy3IZYdnamH3stm7OitsHfPIaYApb3pMwM7RiUr-CscWKD7_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
با همچین عزیزانی تو ممکلت هموطنیم :(
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66414" target="_blank">📅 11:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66413">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6af0a234cf.mp4?token=PSNga0Ds1A02fLuVfEeFmSnNcO_sPb-cP4buNuVVUhD748X08dEhHRP2JETpW2JJYeg-Y0Eb7EWUbsSX1tnAvxVqKVBVChSHm1XHMw28L9Be4Say_Gl1v3imr4VkEEnONSGcwIE_bxtgsHjOOv2rVH5Eegfj4O4k5n9BBS7FaiKa0_Uh0YV8eQmV4X-A9D40-GFyvWe0q4ROBdFsRzt4gFbvOdgy824dJF_9ZtEkGMCFKpI_wA0DkAu2SkC-PoW3KQjdDFEBjNnP4NzcuMFpLuIKU0EUByRRi-idPf-T-CdU319WW3R8YBzZ043hKLYhZUBnUzGz3WMIA9LMb6B4NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6af0a234cf.mp4?token=PSNga0Ds1A02fLuVfEeFmSnNcO_sPb-cP4buNuVVUhD748X08dEhHRP2JETpW2JJYeg-Y0Eb7EWUbsSX1tnAvxVqKVBVChSHm1XHMw28L9Be4Say_Gl1v3imr4VkEEnONSGcwIE_bxtgsHjOOv2rVH5Eegfj4O4k5n9BBS7FaiKa0_Uh0YV8eQmV4X-A9D40-GFyvWe0q4ROBdFsRzt4gFbvOdgy824dJF_9ZtEkGMCFKpI_wA0DkAu2SkC-PoW3KQjdDFEBjNnP4NzcuMFpLuIKU0EUByRRi-idPf-T-CdU319WW3R8YBzZ043hKLYhZUBnUzGz3WMIA9LMb6B4NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
برشی از سخنان تند شب‌گذشته قالیباف خطاب به ارزشی‌ها و تندروهای کسمغز
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66413" target="_blank">📅 11:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66412">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04da6f24fd.mp4?token=N8gEBBedsKO5UCNL8DDrCDEIAXrTt1Rdav2F0TVaaIyAteYuHtWF9mamcoZ1SjCmua3eKP8MXxR9q4iLrHpWGcjX5GzS573C8m2eGYLee_a-CxDIOx8rQLvR_Z4J9ZY19offudd16NFUL7EPDZzP4_sYoCmwegjzwaGoV8MvVr4XW-wa_M9D1YQyK7ZrAuZQqkfPJqx-5ex_k4nXyLk_7fcpQfNmG-ndCbmEyUHFfcOjqiSUKzB_uwEKPo7IDnGoKeT0MiJu2nCCdp0dC8wPh03fBvc5slIOIZ2yy-2hjsboVCH_LmQ6yxJAFO_avlz0hOY6hngbMovqoKY--vyQFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04da6f24fd.mp4?token=N8gEBBedsKO5UCNL8DDrCDEIAXrTt1Rdav2F0TVaaIyAteYuHtWF9mamcoZ1SjCmua3eKP8MXxR9q4iLrHpWGcjX5GzS573C8m2eGYLee_a-CxDIOx8rQLvR_Z4J9ZY19offudd16NFUL7EPDZzP4_sYoCmwegjzwaGoV8MvVr4XW-wa_M9D1YQyK7ZrAuZQqkfPJqx-5ex_k4nXyLk_7fcpQfNmG-ndCbmEyUHFfcOjqiSUKzB_uwEKPo7IDnGoKeT0MiJu2nCCdp0dC8wPh03fBvc5slIOIZ2yy-2hjsboVCH_LmQ6yxJAFO_avlz0hOY6hngbMovqoKY--vyQFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ببینید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66412" target="_blank">📅 10:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66411">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cc5db481b.mp4?token=OvBHAp_ShBNNbya04bPH9rw_agYRTEUoyu5FadiTSafGiHtRnkDONfIsFVCUdlncbGJBsHPYSWa_AZNZE7Pb1y9uE9aaCNLallzh_aiAELn3BaKTbBz-o4BDnQAlBpzLVbt2JzhRbpcKRd0hXbjx41nFS32UOwtZhGbvzSy0OvVUDF5xkpMcV-xGUZ3dhan-CHhw_tBDF8tghNRTICmvIJotD9wTphqwJJO2n4dFrYu3gleCH-x41mwwrbHpjGP_JDwppolMQSQMX0tkplej9qm0pe_fqiUFBMCaarJlVw2E8t-SX9u2z0gq1hRecRY4LYBT9fAJaDuqUS3j_1KFjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cc5db481b.mp4?token=OvBHAp_ShBNNbya04bPH9rw_agYRTEUoyu5FadiTSafGiHtRnkDONfIsFVCUdlncbGJBsHPYSWa_AZNZE7Pb1y9uE9aaCNLallzh_aiAELn3BaKTbBz-o4BDnQAlBpzLVbt2JzhRbpcKRd0hXbjx41nFS32UOwtZhGbvzSy0OvVUDF5xkpMcV-xGUZ3dhan-CHhw_tBDF8tghNRTICmvIJotD9wTphqwJJO2n4dFrYu3gleCH-x41mwwrbHpjGP_JDwppolMQSQMX0tkplej9qm0pe_fqiUFBMCaarJlVw2E8t-SX9u2z0gq1hRecRY4LYBT9fAJaDuqUS3j_1KFjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش‌بینی عجیب دو سال قبل شاهین نجفی درباره قالیباف:
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66411" target="_blank">📅 10:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66410">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f1770ac7.mp4?token=caF5HXQZjtc2YzgVR8c-fP0p4IPV2y9vtuwdhYJwIJvodFVkxFrMAVHMLY7lPcSY25MlNvahbVUFTCOuhNXrCo2Lvb2xqpxnK7IXBg-LLacN6XDmYpFoscaCZLdgw92B5RN6gzJJDSAAsOacaXGhSub3YzwoL880X7NbtH_IzLnI_VSh82DHumhT_nk2wTtt4J0phtAe85Oqvh-l_VlMG6xZ1LHqsyLldMlCV716ZtZZOfgrmVIV8EEu6lXvId2_7Dp0r3fiViqtGH4bsJQBBtdoE1ssE_bqKXc7l0G_pnLLZGb3dcnUfRj7LFxJQxj9M1bdI7M0KcQd4anOpMUvtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f1770ac7.mp4?token=caF5HXQZjtc2YzgVR8c-fP0p4IPV2y9vtuwdhYJwIJvodFVkxFrMAVHMLY7lPcSY25MlNvahbVUFTCOuhNXrCo2Lvb2xqpxnK7IXBg-LLacN6XDmYpFoscaCZLdgw92B5RN6gzJJDSAAsOacaXGhSub3YzwoL880X7NbtH_IzLnI_VSh82DHumhT_nk2wTtt4J0phtAe85Oqvh-l_VlMG6xZ1LHqsyLldMlCV716ZtZZOfgrmVIV8EEu6lXvId2_7Dp0r3fiViqtGH4bsJQBBtdoE1ssE_bqKXc7l0G_pnLLZGb3dcnUfRj7LFxJQxj9M1bdI7M0KcQd4anOpMUvtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
10ثانیه تراپی روح و روان
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/66410" target="_blank">📅 09:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66409">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d95de07e4f.mp4?token=qzOhCSkMm2BTJq9PtVH6qic9ge8JVOSNg7b6G0BOePQ4QfITk0w0LLwc4inAYAsGba3i7smAJ3S34njxkGB_uPDtP0zgXFh6vQQjwPd_AECsuLzs_IUl_2nULuQk0Pw4RUTzJLJak9IK0_hilK1Jp7EZBV1rYPL-NXX13epN3q4zqpVKFkqE3PD_CaDuzVpYv6yhetoXz5RtPxA3WT0BghG0BsxcTDHK6UGWl3DYPpQX3JwS7nsHHw6Gvq-QrH7JRHXJGDVwIEZBUR3QF5UIU76NPEZ87Mtxm0GGkCmqSCV6eKAMSOXadHzcKLU4ozYmj0ZaypOn5ZnScLJphtZOSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d95de07e4f.mp4?token=qzOhCSkMm2BTJq9PtVH6qic9ge8JVOSNg7b6G0BOePQ4QfITk0w0LLwc4inAYAsGba3i7smAJ3S34njxkGB_uPDtP0zgXFh6vQQjwPd_AECsuLzs_IUl_2nULuQk0Pw4RUTzJLJak9IK0_hilK1Jp7EZBV1rYPL-NXX13epN3q4zqpVKFkqE3PD_CaDuzVpYv6yhetoXz5RtPxA3WT0BghG0BsxcTDHK6UGWl3DYPpQX3JwS7nsHHw6Gvq-QrH7JRHXJGDVwIEZBUR3QF5UIU76NPEZ87Mtxm0GGkCmqSCV6eKAMSOXadHzcKLU4ozYmj0ZaypOn5ZnScLJphtZOSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
خبرنگار: چه مدت نیروهای نظامی آمریکا را در خلیج فارس نگه می‌دارید؟
ترامپ: هنوز به آن فکر نکرده‌ایم. احتمالاً برای مدتی، جای خوبی برای ماندن است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66409" target="_blank">📅 09:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66405">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CwWwPyCS-JnX7E--3xFp81U2sU0bvhkXIkuKh6I8AOv9N8rsLd68805lA4guUkeBeZ2_y9rhMqDaXgC9VgWlOO2Ltsot_PHajZR-rTBZXG0hhz-T51yd9kbuCu8zve1o_xOA7K0LtnGHEyUiG8_86lTcZlyShVOLCYaEumLr8ne1gMvr8r3fEz2hZAK3n9zOglaiYm5CyVCrJzVCTbGCdMdMqPu7ILT6WYUsCCTip1auROlWGXimnkUtpyAtp-4DfwaxQ5vLY-fs5MLmJbNWm9M3s0cqk_XaJSG0PJNyUWYMHZltgWeMbzKH5TfwUpNOkH3PoOR7C6vNZqFhvAHQWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CFSse7ykXSMaiI7gJ-r_JRw5oAXsUO8wYCOa62v-kqqO0Bvb_xEEPcRODMKgzVRjgQ2KZ36vc7MHDBj3yuFOnitWtOJ7r2l9dHRDkagbjWudAMpVj4B2A2ckt3VGL6cNHETGWK33943RmAdN3qY0NqfUPywfLcDWNXfSQw400GQSsG1s0Zn-8Fire_wGpdZVJ9ilTEbzTutKXLD-NiG9OcsgZFgHvVHHVycUp5cGrbtLh9_NlwTyPSSuU1PtvMe08TTBVHGWHlfTBPT28jt14QtFTjmAjlctusgKwT6LdAHs4yTMQ3fZdD4IRvHNiUynyhJwexP_50PE9eCOrFzqiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HG7ZoVDfloY0ePKWZ1nsO_6DXtLztpoe3y0AlvcGJPCAWu0wybg-HYVTPUt6iEiQmWteavAuQnBLnpMsDJlyirQLpAEVkTxEj5BTvVXDb5zxUndm-hvLdpvu7BVV_faGmlvPH-SWTGMmcn-ssTcQkEPrimUZhYuy7OtGIZjzqD1UqkuryjYDstFJPPwE0d7UseC9LHT1j0D6-y9bq4uL9LlCEfY_LrqgVEq2vogbNbJ-KXyVw3K12Ytlh--YuzQSiCN-rKnOjMF01bCIHsjuW0wQxbKzFOxjC_S51dbyPgXDmijANHD0aKBwqITh8Q6oDdLGCAtKmEahHuchgK5aHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇺🇸
#فوری؛ تفاهم نامه صلح توسط ترامپ و پزشکیان امضا شد  @News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/66405" target="_blank">📅 04:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66403">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcB5CLde4e9HQ6B8JQMapbaVnc58EB0uZaQlAPnrEQfXQ64nqt67eLgUJ6i9ndqfUOPyStv9nFyQeichJ1CdgZdtH05Mc_GRxmzz73UtZd_2H43ES-1l2hL_qYO7hDEmJWpF3zaRmmuzhQGo4nLsFdy29SoDkGqPrjid6ejKpmZf7_RH2WZ2DCm4v8QyE5TNHQxqqqhHB-P75K4U4mb0IOqfQCp4OUCYMAXTBsoZMAcmBlg99IeL0phjTG37ghP68b86QGLY_hsL4a6_rfOIRSZO7skP0X3H_BY3DHMHlhQs5m55UCqGEghvhpfPi3KBGd-4MGO083S3B9jo-GkpXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be88e9229.mp4?token=Q-BbJCvOG1cA5kscOBLghCmeod2bTfwh-BcryMHwwzzL37hsO5AIpMS7gQPHyvLzFwnrOvbmhEnTe2Nf0lswTm9l5Ks9WXtr4Lyjx9GIhhX8bzauMHf5wZVdHU5wyVDbrM62CFL1tbHtsTkK1kdoqTPRc7_NgTCl8E-j733NxvXKkm0c7wZbDWShTkN3kFPIJzw1NsMbT9bUiOkemzxtcLuWA2U1cg8Gs-UrZqSg65jSz7cK_535BsO0-EnSC4eMHVp8xcHyqD8RPlwQalf4zlebupmVWf8D1Td5imCAg1l627sczWdY5iKU2rpZsPy_tjJohTVO0uRc3H9NWV5tCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be88e9229.mp4?token=Q-BbJCvOG1cA5kscOBLghCmeod2bTfwh-BcryMHwwzzL37hsO5AIpMS7gQPHyvLzFwnrOvbmhEnTe2Nf0lswTm9l5Ks9WXtr4Lyjx9GIhhX8bzauMHf5wZVdHU5wyVDbrM62CFL1tbHtsTkK1kdoqTPRc7_NgTCl8E-j733NxvXKkm0c7wZbDWShTkN3kFPIJzw1NsMbT9bUiOkemzxtcLuWA2U1cg8Gs-UrZqSg65jSz7cK_535BsO0-EnSC4eMHVp8xcHyqD8RPlwQalf4zlebupmVWf8D1Td5imCAg1l627sczWdY5iKU2rpZsPy_tjJohTVO0uRc3H9NWV5tCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇺🇸
#فوری
؛ تفاهم نامه صلح توسط ترامپ و پزشکیان امضا شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/66403" target="_blank">📅 04:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66402">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/66402" target="_blank">📅 02:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66401">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HPWqK2OTWbffBsP3N6J9XWAUCOPB8yvHG5mEPt8nn9PimtdIT3AdiJq68mn7MU4GP-_8U1r7C4G21XewlSpsytXZU7gqpCwIYrBea736f90SDeWVwnBR7qNdTS8LnynKF-KCqYIk1m8jD6S988ipRb1XJbRSz1yAP3exxVNtZyovVfdLJDN4e6qHkrPtAxctt9G3dPtHZPpI7JjcLk4YtDWakg5IB6cJm8YFsUmbRxTso2kEteKuF2DY647A3MT3ElnevDbBj13ZHj0vzn_VBHqAEKooooDIMYbTQXlhg96ab7EhrphGosVU8WeXGmNi0fUBuDzvCqT6B_XHFUfWNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/66401" target="_blank">📅 02:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66400">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/dYpq39IYUYrH6lFRWAOmv4ugy_FWVNrGJ6HW8RAXAyLDcOO3yX3eQLe4a0Lm715vu9SXywwHX8eMFFCpgVIL3gEMVCvEJtbU577lqgBgb2iZKtLmKR0rsEI2xGvrjSBpJocw8SyzMEYPdV4SYW5lqD9V874JuNoDThM_aieJ4yiYAX5bJWlbw0oT2AV1msweAAzcJLwgoiS3VaN4K2nBY2855KHggSw0TnTfDf5GuyUARLYXOpkXzwQApXveb9GNJuGbeCJ0dGcTpovygxKIpIbl5eg0eOFYMgAggoyT7QIa91zdE9NgKVK1dg716rwy95faT0B33hKeMlFIW2Ic6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/66400" target="_blank">📅 02:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66399">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
متن تفاهمنامه جمهوری اسلامی و آمریکا:
🔴
1⃣
توقف فوری و دائمی خصومت‌ها بین ایالات متحده، ایران و متحدانشان در تمام جبهه‌ها، از جمله لبنان.
🔴
2⃣
هر دو طرف متعهد به احترام به حاکمیت، تمامیت ارضی و امور داخلی یکدیگر هستند.
🔴
3⃣
توافق جامع باید ظرف ۶۰ روز مذاکره شود، با امکان تمدید به توافق متقابل.
🔴
4⃣
ایالات متحده بلافاصله محدودیت‌های دریایی خود بر ایران را لغو خواهد کرد، در حالی که ایران به تدریج ترافیک دریایی را باز خواهد گرداند. نیروهای آمریکایی در نزدیکی ظرف ۳۰ روز پس از توافق نهایی عقب‌نشینی خواهند کرد.
🔴
5⃣
ایران تضمین خواهد کرد که ناوبری تجاری امن از طریق خلیج فارس و خلیج عمان انجام شود، با بازگردانی کامل ترافیک پس از عملیات پاکسازی مین.
🔴
6⃣
ایران و عمان درباره مدیریت آینده و چارچوب دریایی تنگه هرمز گفتگو خواهند کرد.
🔴
7⃣
ایالات متحده و شرکای منطقه‌ای ابتکار بازسازی اقتصادی و سرمایه‌گذاری برای ایران به ارزش حداقل ۳۰۰ میلیارد دلار را آغاز خواهند کرد.
🔴
8⃣
تمام تحریم‌ها علیه ایران، از جمله تحریم‌های ایالات متحده، سازمان ملل و آژانس بین‌المللی انرژی اتمی، طبق نقشه راه توافق شده برداشته خواهند شد.
🔴
9⃣
ایران مجدداً تأکید می‌کند که به دنبال سلاح هسته‌ای نخواهد بود. مسئله ذخایر اورانیوم غنی‌شده از طریق مکانیزمی که توسط هر دو طرف توافق شده، حل خواهد شد.
🔴
🔟
تا رسیدن به توافق نهایی، ایران موضع هسته‌ای فعلی خود را حفظ خواهد کرد، در حالی که ایالات متحده از اعمال تحریم‌های جدید یا استقرار نیروهای اضافی خودداری خواهد کرد.
🔴
1⃣
1⃣
صادرات نفت ایران همراه با خدمات بانکی، حمل و نقل و بیمه مرتبط، معافیت‌های تحریمی فوری دریافت خواهند کرد.
🔴
2⃣
1⃣
دارایی‌های مسدود شده ایران به تدریج طبق رویه‌های توافق شده متقابل آزاد خواهند شد.
🔴
3⃣
1⃣
یک نهاد نظارتی مشترک اجرای یادداشت تفاهم و هر توافق آینده را نظارت خواهد کرد.
🔴
4⃣
1⃣
انتظار می‌رود توافق نهایی از طریق قطعنامه شورای امنیت سازمان ملل رسمی شود.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/66399" target="_blank">📅 02:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66398">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛بقایی سخنگوی وزارت خارجه:
تفاهم‌نامه به‌صورت الکترونیکی بین پزشکیان و ترامپ امضا شده. جمعه هم خبری از مراسم رسمی نیست و فقط هیئت‌های ایران و آمریکا به سرپرستی قالیباف و جی‌دی ونس تو سوئیس دور اول مذاکرات فنی 60 روزه برای اجرای تفاهم‌نامه رو شروع می‌کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/66398" target="_blank">📅 01:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66397">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
سخنگوی وزارت خارجه جمهوری اسلامی: متن توافق با آمریکا نهایی شده و به امضا رسیده
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/66397" target="_blank">📅 01:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66396">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ac08f5fbc.mp4?token=qW4ohp5Wpzd-rX_N1Bj6QsiX2aIFa27wQIiZS5gwrk0iPZqIoewgyKXK6PRA91kB5V99V9LoPaJDKVFgiEDAbveQvK0RT9_N4D9aYqCMDlMKpMyiq1C4i2zWK0haXwTfJV8U3JxGaBF6w84-D3UyReMqCTZ3uRPDUVm_7jq6GE7mkaYAtiRDYdstn_8by_RhDow8hRDelobHNkyTUGELpehCrp7qeivWwESm-LcPTWQRFFmhdv4-PYVaGfVqkCrsxxrP8J8dGunNFwyrWXcTpj3nwVQ8DuTGLwdMmzbOcb7Ir85Y-oIJ040RopFukBOmyaUpYNh3uZ4IsnuI1-4H3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ac08f5fbc.mp4?token=qW4ohp5Wpzd-rX_N1Bj6QsiX2aIFa27wQIiZS5gwrk0iPZqIoewgyKXK6PRA91kB5V99V9LoPaJDKVFgiEDAbveQvK0RT9_N4D9aYqCMDlMKpMyiq1C4i2zWK0haXwTfJV8U3JxGaBF6w84-D3UyReMqCTZ3uRPDUVm_7jq6GE7mkaYAtiRDYdstn_8by_RhDow8hRDelobHNkyTUGELpehCrp7qeivWwESm-LcPTWQRFFmhdv4-PYVaGfVqkCrsxxrP8J8dGunNFwyrWXcTpj3nwVQ8DuTGLwdMmzbOcb7Ir85Y-oIJ040RopFukBOmyaUpYNh3uZ4IsnuI1-4H3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
به محض اینکه آتش‌بس برقرار شد، دیدید که دشمن در خلیج فارس اقداماتی انجام داد و ما بلافاصله پاسخ دادیم.
آخرین نمونه آن حادثه مربوط به بالگرد آمریکایی‌ها بود.
علاوه بر این، دو ناو جنگی دشمن که قصد عبور از تنگه هرمز را داشتند، مورد اصابت قرار گرفتند و دچار آتش‌سوزی گسترده شدند - موضوعی که تصاویر ماهواره‌ای نیز آن را تأیید کرد.
از سوی دیگر، هر فرودگاهی در هر کشوری که جنگنده‌های دشمن از آن برخاسته بودند، هدف قرار می‌گرفت. همه این اتفاقات در حالی رخ داد که ما همزمان مشغول مذاکره بودیم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/66396" target="_blank">📅 23:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66395">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df75a39b35.mp4?token=mXmbdMZW7_6smPTkW7STZkWLKKV61ksxBkJdGdM6q_Q9Kmc9Hisj1ZWvu2iPdRkiJ2etw7NmA8pocD2g62RtH8EpNlWQ5O1HXaSMKjHmDwvEz-pyaEd2GZBrBrM0MesqRsnI9Ln40zxHG4e6zqDIo6lnnUCjs5Fr7ivP1FHdYTnNa8FwPMqtkNbHbbFos0ZE7jZi9ZAqQJYA-xBU0kJFuhdEsghoCSQKYT9DjRLe8Sq8mDXHGKBSFejKv2k6efSzZXOsl6W_vfYO9LKKSvAGLmqC14LjL7tc2I2jrqsNZk77RyX6rRlUruGa4K87u_DyQKlqtKSVy14Oj4jzh2_MzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df75a39b35.mp4?token=mXmbdMZW7_6smPTkW7STZkWLKKV61ksxBkJdGdM6q_Q9Kmc9Hisj1ZWvu2iPdRkiJ2etw7NmA8pocD2g62RtH8EpNlWQ5O1HXaSMKjHmDwvEz-pyaEd2GZBrBrM0MesqRsnI9Ln40zxHG4e6zqDIo6lnnUCjs5Fr7ivP1FHdYTnNa8FwPMqtkNbHbbFos0ZE7jZi9ZAqQJYA-xBU0kJFuhdEsghoCSQKYT9DjRLe8Sq8mDXHGKBSFejKv2k6efSzZXOsl6W_vfYO9LKKSvAGLmqC14LjL7tc2I2jrqsNZk77RyX6rRlUruGa4K87u_DyQKlqtKSVy14Oj4jzh2_MzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏قالیباف:
نه تنها خودم برای حضور در تیم مذاکره‌کننده داوطلب نشدم، بلکه واقعاً از پذیرفتن آن هم اکراه داشتم. پیش از قبول مسئولیت مذاکرات، هر کاری از دستم برمی‌آمد انجام دادم تا این مسئولیت به من واگذار نشود.
یکی از دلایلی که نمی‌خواستم این مسئولیت را بپذیرم این بود که دونالد ترامپ طراح، فرمانده و ناظر ترور قاسم سلیمانی بود.
سردار سلیمانی برای کل جهان اسلام عزیز بود، اما برای من به‌طور شخصی معنای متفاوتی داشت. آیا فکر می‌کنید برای من آسان است که با چنین فردی بنشینم و متنی را نهایی کنم؟
با این حال، وقتی دیدم هیچ‌یک از مسئولان فرد دیگری را پیشنهاد نمی‌دهند و پیشنهادهای خودم هم پذیرفته نمی‌شود، مجبور شدم وظیفه‌ای را که به من محول شده بود انجام دهم.
ما قرار نیست فقط کاری را انجام دهیم که دوست داریم؛ بلکه باید کاری را انجام دهیم که وظیفه‌مان ایجاب می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/66395" target="_blank">📅 23:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66394">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f6d42bdbd.mp4?token=GNBi3aavoXitiyVamnhF8WY8-icWHVmzqKSsg4BK2m4DdZSWcDk368hffImK498P4_IeRZRBf_2gqWqh2BL0YX4803OGzYQPNnSe1ZuMLiKR_kOWyaP4Rr6LiUDAoFiZMVoaVgxXdAXuyzKed3d3GmfojTwrdchWiFwtG9H7Z5kQsn4GkiPvHMC9DG8JriYnJyeCUwW8WoQZtq-vrbco9uh4xlj0mtl0YFd1yKBsWT4WHPmLMThNffuKlrKvxQh3a6Kv2ayTCWs623NCFSpHXg_PVkDFkrYTMTAzYfqJ3JrNdgDU11fr7tX2pmRvHZvz88L22sB2TIVEz1EFzI1ORA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f6d42bdbd.mp4?token=GNBi3aavoXitiyVamnhF8WY8-icWHVmzqKSsg4BK2m4DdZSWcDk368hffImK498P4_IeRZRBf_2gqWqh2BL0YX4803OGzYQPNnSe1ZuMLiKR_kOWyaP4Rr6LiUDAoFiZMVoaVgxXdAXuyzKed3d3GmfojTwrdchWiFwtG9H7Z5kQsn4GkiPvHMC9DG8JriYnJyeCUwW8WoQZtq-vrbco9uh4xlj0mtl0YFd1yKBsWT4WHPmLMThNffuKlrKvxQh3a6Kv2ayTCWs623NCFSpHXg_PVkDFkrYTMTAzYfqJ3JrNdgDU11fr7tX2pmRvHZvz88L22sB2TIVEz1EFzI1ORA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
لبنان بخشی از جبهه مقاومت است. طبق توافق، ایران از جبهه مقاومت حمایت می‌کند، در حالی که ایالات متحده حامی و متحد رژیم اسرائیل است.
بنابراین، طبیعی است که وقتی آتش‌بس برقرار می‌شود، باید در همه جبهه‌ها، به ویژه در لبنان، رعایت شود.
باید از مردم عزیز لبنان، به ویژه شیعیان و حزب‌الله، که در طول تجاوز آمریکا و اسرائیل به ایران ایستادگی کردند و نزدیک به ۴۰۰۰ شهید تقدیم کردند، تشکر کنم.
در حالی که ما در شرایط آتش‌بس بودیم، آنها به جنگ ادامه دادند و همچنان تلفات دادند.
وقتی رژیم اسرائیل ضاحیه را هدف قرار داد، ما ایالات متحده را تهدید کردیم و اولتیماتوم دادیم که خواسته‌های ما باید پذیرفته شود؛ در غیر این صورت، ما پاسخ خواهیم داد.
ترامپ مجبور شد در شبکه‌های اجتماعی پست بگذارد و به نتانیاهو بگوید که حملات باید متوقف شود و دیگر نمی‌توان ضاحیه را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66394" target="_blank">📅 23:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66393">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ed9265802.mp4?token=Xy3qNGgObg-vlSvd9zgzRUhYApaWo8j3rWtNC3e_ic_ASbtYHJDBGLgUA85NLe0uGyxcAdEgARG9ZdC1ZJX-L7WjGNbQxCfdQhjZuUnxYl6XuhF_wph7VdV0Mh6bkrDy7AIy2f-Oz8zyxYAz3SfivkrIVcqMP24c7LBxDMycppbmPaNwoJZ4fACOCtYcQaUaAUVA9mqdmJCndziA3ABF_ea_tXnBxyYmfMDCWt539I_zmjlbh9cwUCfW82iLOAVg1DUwZ5gY9mVd8D_-sE6brEkBJQALpraHceeIO8ELawnjpU_BlHM3wv5GyoRLb70h_R_V_ZcRe7W1KLa04a1tYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ed9265802.mp4?token=Xy3qNGgObg-vlSvd9zgzRUhYApaWo8j3rWtNC3e_ic_ASbtYHJDBGLgUA85NLe0uGyxcAdEgARG9ZdC1ZJX-L7WjGNbQxCfdQhjZuUnxYl6XuhF_wph7VdV0Mh6bkrDy7AIy2f-Oz8zyxYAz3SfivkrIVcqMP24c7LBxDMycppbmPaNwoJZ4fACOCtYcQaUaAUVA9mqdmJCndziA3ABF_ea_tXnBxyYmfMDCWt539I_zmjlbh9cwUCfW82iLOAVg1DUwZ5gY9mVd8D_-sE6brEkBJQALpraHceeIO8ELawnjpU_BlHM3wv5GyoRLb70h_R_V_ZcRe7W1KLa04a1tYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
بدبینی و بی‌اعتمادی من به ایالات متحده از هر کس دیگری بیشتر است.
حتی اگر توافق نهایی حاصل شود و توسط قطعنامه شورای امنیت سازمان ملل متحد تأیید شود، باز هم قابل اعتماد نیست. تضمین ما قدرت ایران است
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66393" target="_blank">📅 23:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66392">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afb769475.mp4?token=sJwjQA0V0nGbBO_9ssyot1R1eZg8v2yBBRX9D09vC-5BV-QZ1qJlbWmVi7i9UF-50vWz_5yPFPW8RFmRv_Q6QQCOiVvSROtKt0oAk93y3L3SJGwHvzgONIn42qkEiq9bEEmzGsZWSlAuSDsJX7XZ3-0Zf5Ej-ManttH_CCVbh37DR2k3lzbrXxfk2s_sO9Qth6F4kPX2YEmnDC4GxAo4bIxBOE08jivynyIlE6am-vUIkKorI2xLEdPNHIVpnRH9Q111PkpY6cMv4e-ieUrn6fenxHKb643JJNbaFrvRmpqw1sWZXWAP7so2POc5PByNNTnBoxLyVzrIbQSovGgjxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afb769475.mp4?token=sJwjQA0V0nGbBO_9ssyot1R1eZg8v2yBBRX9D09vC-5BV-QZ1qJlbWmVi7i9UF-50vWz_5yPFPW8RFmRv_Q6QQCOiVvSROtKt0oAk93y3L3SJGwHvzgONIn42qkEiq9bEEmzGsZWSlAuSDsJX7XZ3-0Zf5Ej-ManttH_CCVbh37DR2k3lzbrXxfk2s_sO9Qth6F4kPX2YEmnDC4GxAo4bIxBOE08jivynyIlE6am-vUIkKorI2xLEdPNHIVpnRH9Q111PkpY6cMv4e-ieUrn6fenxHKb643JJNbaFrvRmpqw1sWZXWAP7so2POc5PByNNTnBoxLyVzrIbQSovGgjxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
ما بر ایالات متحده و رژیم صهیونیستی، که قدرت‌های نظامی پیشرو در جهان هستند، پیروز شدیم و اجازه ندادیم که آنها به هیچ یک از 9 هدفی که اعلام کرده بودند، دست یابند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66392" target="_blank">📅 23:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66391">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a462c62e6a.mp4?token=b4LYbIpY-VYE2SHsONDqo8Rv_4IU3XL-BAg31AMqpIQzeGlSjlWdZruU5Bjh4WhT-sK7qVnlnZAmLBnayajtKU6BGFaiyC5yvrRN-11wqQQSTKViVPj9fWGQ-CvsVbAhwtDgHtDYUy2entm78xUuuISRjP-osYYkn-m0uYxhu7AxVmrTCK4gflnUem8GSxKjKjwZf3_OcIG-SjR4drqF_1JpUJmR4D-5OcVho2H5bDnL7IVZhSdxpB3QPoXl_YfYVXN8flN3VdC_1e7MU6vhiHwF8elx1_J_9v7olfhfgL6FywGSa2IKRPSbPjbnogFcnULldvd3cMPASaD_SI-ghQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a462c62e6a.mp4?token=b4LYbIpY-VYE2SHsONDqo8Rv_4IU3XL-BAg31AMqpIQzeGlSjlWdZruU5Bjh4WhT-sK7qVnlnZAmLBnayajtKU6BGFaiyC5yvrRN-11wqQQSTKViVPj9fWGQ-CvsVbAhwtDgHtDYUy2entm78xUuuISRjP-osYYkn-m0uYxhu7AxVmrTCK4gflnUem8GSxKjKjwZf3_OcIG-SjR4drqF_1JpUJmR4D-5OcVho2H5bDnL7IVZhSdxpB3QPoXl_YfYVXN8flN3VdC_1e7MU6vhiHwF8elx1_J_9v7olfhfgL6FywGSa2IKRPSbPjbnogFcnULldvd3cMPASaD_SI-ghQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
تفاوت بین مذاکرات فعلی و دورهای قبلی این است که امروز دانش و دستاوردهای پیروزی در میدان نبرد به عنوان پشتوانه دیپلماسی عمل می‌کند.
در مذاکراتی که به عنوان نوعی مبارزه انجام می‌شود، نه تسلیم وجود دارد و نه شعارهای توخالی.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66391" target="_blank">📅 23:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66390">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7shyd5Kuonrqcz0QieUt99CAsa0tBi538TxSWjwo7ce93EdlTi25bKuRyFqci9Tb49P-Fewesdufg3ZbBbTd2mruoe6Ry1Wh8_SmPJcXXZqnz8FEfNL9j3cA24oIADDyEiBVeTKWtTsliEigwcGYGqcAcbiApKs1qnIkinjCnSrhG-gKqETZ-AJgfv2RqM8Q4GmZ48yxe_j-jW24_AnU_hFQ-oDggy0uuLQ_6JnxX7fnljeIKiChmV0xPzbH7lBBOHeE-BAt50HQvNybhGpUVL1vu03ahaFD1se3stxCbSKvj-fPv1RzTNottSTe4yJoNds0FvjlHPsx0yW4wYHBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شبکه خبر:
مصاحبه اختصاصی رئیس مجلس درباره تفاهم‌نامه پایان جنگ تا دقایقی دیگر
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66390" target="_blank">📅 22:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66389">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92d9400b7a.mp4?token=YC2hv5QgC_dJlMVaJFprvzbMhevlTWIcIdHVV1pv1W_M3LwHeOIneQuihz5s2VBRRm5mw51wil0UuLmCWemJHTgxgMAhhEEB7Sw_K48cSbIqVPcWAQydyiDaQnYu_N4Bm9LOue-8F-LVa84GIH4joLWYK1tWrIytUwlEEw5ODWDmRmJ0Nh_WlIhV0o7keDbxDcQD-gw0eRbSo4M_LvmaEZ968IZ8iTvpHHXzNGotf_vX8hhp08B-mD6SVCRAq8WqwTvm4giIgrNsMBQGohvuRzYk3goUXQSg63rG4jtzdEMFR64qHnxECBa5oAq1LQsP-KdN4DbDG7hF17yVSiFVmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92d9400b7a.mp4?token=YC2hv5QgC_dJlMVaJFprvzbMhevlTWIcIdHVV1pv1W_M3LwHeOIneQuihz5s2VBRRm5mw51wil0UuLmCWemJHTgxgMAhhEEB7Sw_K48cSbIqVPcWAQydyiDaQnYu_N4Bm9LOue-8F-LVa84GIH4joLWYK1tWrIytUwlEEw5ODWDmRmJ0Nh_WlIhV0o7keDbxDcQD-gw0eRbSo4M_LvmaEZ968IZ8iTvpHHXzNGotf_vX8hhp08B-mD6SVCRAq8WqwTvm4giIgrNsMBQGohvuRzYk3goUXQSg63rG4jtzdEMFR64qHnxECBa5oAq1LQsP-KdN4DbDG7hF17yVSiFVmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
آتش‌سوزی گسترده انباری در سن-سن-دنی، پاریس
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66389" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66388">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syjAEk0L2vXpVDSHXRKL6GoNT8GOVYBwwfR_oXTmxgJl7RzL1m6SX8MzdGEXlJ3K6MvGqCmpJisKNt8FKUC1nA5bF3DNGq64CTzkOKfojjH76QFnD_DatpOIKEg-sqOPktsr-2idgP0G4ovCaD2e2XA3VwRgrHzEVQMvql01jAe2BW4dsZNynXeqEXlDSXxcOhhGE_MfGKwtXfqNKSLETxHSLIIqWsNDspEjyct7YJVK_l8CiTdzqHCXY7fLljJBeaZm_zqxz6iJYozzrqfVKRI2sHNsGBx0lEP18dM6j_5iuaqMHicLLfu8UmwAwe_0Knht9f-tgRaaEaIWVf5asQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیندزی گراهام: من همین الان یک بحث بسیار طولانی و سازنده با ویتکاف  در مورد ایران داشتم.
بعد از این بحث، به نظر من امضای تفاهم‌نامه برای ایالات متحده مفید خواهد بود، تا جایی که تنگه هرمز شروع به باز شدن کند و خصومت‌ها با ایران متوقف شود.اینکه آیا ایالات متحده می‌تواند در مورد برنامه هسته‌ای و سایر مسائل به یک توافق قابل قبول و قابل تأیید با ایران برسد یا خیر، هنوز مشخص نیست، اما من جنبه منفی کمی برای تلاش کردن می‌بینم
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66388" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66387">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b1096f4de.mp4?token=DrrYAEWkh-GBGzmQjLwXORbwSTxSWgoEfoUNL--AK0BuFsROL2IAWfhP0tiCz1WAiu0vfH8PpzqJ4eP-YZ32zrItYPodpdluDLQ9e9PlUCcFUEk5IGEZ2d1cIQUYkOIj4AeKRdFYaxgHQ8XRoT4nq-eSHvdQJMrXXxQ6ij6FgS0NKlRRETWtjdjxjdenlmo35Md0JAvhCSZjBm5vSySPhBBQNP8m7fLmZoitKaKkCTgNvb-OsaYnpEMt4SgBe1p3R4P9Xjfpu_3RD4Nu6LapoiKRw7tMoQck1_voP1yf_ffWTDiY4ffjFM_tmCZJ7l4aw4R6ordKJPAETEkRUEyRhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b1096f4de.mp4?token=DrrYAEWkh-GBGzmQjLwXORbwSTxSWgoEfoUNL--AK0BuFsROL2IAWfhP0tiCz1WAiu0vfH8PpzqJ4eP-YZ32zrItYPodpdluDLQ9e9PlUCcFUEk5IGEZ2d1cIQUYkOIj4AeKRdFYaxgHQ8XRoT4nq-eSHvdQJMrXXxQ6ij6FgS0NKlRRETWtjdjxjdenlmo35Md0JAvhCSZjBm5vSySPhBBQNP8m7fLmZoitKaKkCTgNvb-OsaYnpEMt4SgBe1p3R4P9Xjfpu_3RD4Nu6LapoiKRw7tMoQck1_voP1yf_ffWTDiY4ffjFM_tmCZJ7l4aw4R6ordKJPAETEkRUEyRhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف؛ آن روزی که من پا در میدان دیپلماسی گذاشتم گفتم:
من اینجا آمده‌ام که هم آبرو بدهم، هم خونِ دل بخورم و هم خون بدهم؛ اما اگر کسی فکر کند که از مسیر امام شهید، مسیر انقلاب و عقلانیت ذره‌ای فاصله می‌گیرم، هرگز!
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66387" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66386">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a579da34fb.mp4?token=bK6AwVVx379YvzdRoyP_fm6qgVsS2JGarLdQMjp9emCHsLOwub64XtKKWLOVn87u4mF_N4LG5lp9HGOsL8lCl1tET1Y4jHtZFxl1kKS2847AniU-M5ASbPjGYXlY-8kfQeLfjCYi9VNMiOAXIRS__P62qnPZIeg9vUKUdfYWYad75_TIzZE-hQsgzKOmLXMJpgIwc4JTwwEqhkMBz7GzE_85of6GQzH-UMIS0w6RJs7w6SkaWDO4Zho8pjrICchAiELOFD_30xrC9np-dg-kVaO3QNXG8Th7lp0YaJAtwIpEyjWGJosBw-cWVPitLWaTHYmiJMqZWJBXIECg97QscQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a579da34fb.mp4?token=bK6AwVVx379YvzdRoyP_fm6qgVsS2JGarLdQMjp9emCHsLOwub64XtKKWLOVn87u4mF_N4LG5lp9HGOsL8lCl1tET1Y4jHtZFxl1kKS2847AniU-M5ASbPjGYXlY-8kfQeLfjCYi9VNMiOAXIRS__P62qnPZIeg9vUKUdfYWYad75_TIzZE-hQsgzKOmLXMJpgIwc4JTwwEqhkMBz7GzE_85of6GQzH-UMIS0w6RJs7w6SkaWDO4Zho8pjrICchAiELOFD_30xrC9np-dg-kVaO3QNXG8Th7lp0YaJAtwIpEyjWGJosBw-cWVPitLWaTHYmiJMqZWJBXIECg97QscQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
وقتشه که سنگر رو از بچه های لانچر تحویل بگیریم و یه زندگی خوب برای مردم بسازیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66386" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
