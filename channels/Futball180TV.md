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
<img src="https://cdn5.telesco.pe/file/BIyWJRse90IGVeilFk4VGoazZQRUVio0U94t8byJJb6UYCTWWnzNMYo7flh7T2bz_gAAvVWWqH3sxLt65pjATZfNSWObkOjmhstV8sCCj5oZTY0Vf4CpPCo99kRyW3xrXXPS6PuazTZlaEcE_xhk40_ogXOvMVEbM-EnUSYsP9b6f1uIimkQvgHTzyB-Wcex_ZNHgojao7hSQquyGNzEint8KnOJaFCnLJy0HOy78C7HTA0soLqqC5mzOEOnVYcRTLLXH-ztEn_ro66fPURw2Facupr-PjEuEdsDezars8FNHcGRzjlBe6abcyJzh11mM5DWZKxyur86C8DOEDsnwg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 583K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 20:15:07</div>
<hr>

<div class="tg-post" id="msg-99965">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa4c44829d.mp4?token=beN8YY9xdG_jUpyocgHg5ubnAjG2dO_xX5XNN6p3jKdFGHqijgpj1W0UNCs88ix3hQqtnxwHd8TH5HC86lFiHysxZUTre7-YcQ_lR-K0ao-iM1q6DY9mMHMVGH2G0YzD0vYAL6BtTrcWB7Cnp8-4tHpwBzZDeEqP-K7_selH0b4uco6b_-aQGs337FLSN5VM34rOyHr9n8kCXks5rJQ4YFhc9DlfwVuAZK5-pWRQ7pfyQ3F5C0VRUTcplYCKsNJG1YOTxWE02q9l5yNWaFbkz8Yg3-DSbOEhxuk8Fh7M6vPthiseiJVX95263PrmbTk4V_1bDNwsBDiS7lZYFi09Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa4c44829d.mp4?token=beN8YY9xdG_jUpyocgHg5ubnAjG2dO_xX5XNN6p3jKdFGHqijgpj1W0UNCs88ix3hQqtnxwHd8TH5HC86lFiHysxZUTre7-YcQ_lR-K0ao-iM1q6DY9mMHMVGH2G0YzD0vYAL6BtTrcWB7Cnp8-4tHpwBzZDeEqP-K7_selH0b4uco6b_-aQGs337FLSN5VM34rOyHr9n8kCXks5rJQ4YFhc9DlfwVuAZK5-pWRQ7pfyQ3F5C0VRUTcplYCKsNJG1YOTxWE02q9l5yNWaFbkz8Yg3-DSbOEhxuk8Fh7M6vPthiseiJVX95263PrmbTk4V_1bDNwsBDiS7lZYFi09Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
🎙
بیرانوند: اینقدر تو آمریکا وقت کم داشتیم و باید سریع میرفتیم که شورتمون رو یادمون میرفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/Futball180TV/99965" target="_blank">📅 20:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99964">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
هفته بعدی تاجرنیا مصاحبه میکنه که زن یاسر آسانی مخالف برگشتش به ایران بوده و ما تمام تلاش خودمون رو کردیم
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/Futball180TV/99964" target="_blank">📅 19:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99963">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e8095565.mp4?token=X38eOES6gx-M1yEuiwrinweMHK8wFVDjtD2mAgI5EaitlRZoMnGKRx55RMefxthLnVdekK6uKXZv4_oiK3_kxFGeW2Q1LUfSuJ7hn33XDq9d1U6RrBu6amnWCuwDSnDQvNTCYJ3CDB33iuqVEWmByL2TJL9Chy73qTyyAroMMdnW7OxqnFgmLCqLDvj701mgiMKmLOXB5fZEVEjZchhytBXkNt7Xldk7zHgEXkcVdF08SxeCF2gaaQtvzXYkFh3475JdHaY3pqJofk47052jLepxiRskbSgEbvNI9b3bw4BhlsGYaIQgUy3YZZaLIrqu1U9nP_0FZ668Ww1x8Y5EEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e8095565.mp4?token=X38eOES6gx-M1yEuiwrinweMHK8wFVDjtD2mAgI5EaitlRZoMnGKRx55RMefxthLnVdekK6uKXZv4_oiK3_kxFGeW2Q1LUfSuJ7hn33XDq9d1U6RrBu6amnWCuwDSnDQvNTCYJ3CDB33iuqVEWmByL2TJL9Chy73qTyyAroMMdnW7OxqnFgmLCqLDvj701mgiMKmLOXB5fZEVEjZchhytBXkNt7Xldk7zHgEXkcVdF08SxeCF2gaaQtvzXYkFh3475JdHaY3pqJofk47052jLepxiRskbSgEbvNI9b3bw4BhlsGYaIQgUy3YZZaLIrqu1U9nP_0FZ668Ww1x8Y5EEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
پیش‌بینی سه‌هفته پیش نوسترآداموس زمان یعنی مجید جلالی از تیم‌های برتر جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/Futball180TV/99963" target="_blank">📅 19:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99962">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4532025b1.mp4?token=PCfeFhIUbbVeLp3CFtlrJAMpr45y1uy1S9fCfqwfTpGJaDLshNWWDOk0tVqrPvoFbSU1t2lzUK4-UXCL88QTt19R-HT3p1CNuHL2PjgToVrEw8m32hBLkjZep4inZxa1ASCio5oG7WCfhcKqxD0MDiei_6Hbsjsjrp517MufAqIm4Y_Bg9i8ra_fyWQm1m4AuEMeO__l_7TRLz8gjyi3QPnh7RVgx-ZtXArqwF04cO_E2AvH9gmb4zSmqRiiEcvw3tI6BvYvCmallMBouJ0SvFhnpUY-ZsODjSgMVvnssRZhjpuP-EJy25L8IiluBriEdnlNBFNWIlTZ_doZ1lyrOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4532025b1.mp4?token=PCfeFhIUbbVeLp3CFtlrJAMpr45y1uy1S9fCfqwfTpGJaDLshNWWDOk0tVqrPvoFbSU1t2lzUK4-UXCL88QTt19R-HT3p1CNuHL2PjgToVrEw8m32hBLkjZep4inZxa1ASCio5oG7WCfhcKqxD0MDiei_6Hbsjsjrp517MufAqIm4Y_Bg9i8ra_fyWQm1m4AuEMeO__l_7TRLz8gjyi3QPnh7RVgx-ZtXArqwF04cO_E2AvH9gmb4zSmqRiiEcvw3tI6BvYvCmallMBouJ0SvFhnpUY-ZsODjSgMVvnssRZhjpuP-EJy25L8IiluBriEdnlNBFNWIlTZ_doZ1lyrOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
گل خودت رو بزن!!!
🔹
با افتتاح حساب غیرحضوري در باران بانک کشاورزی، از برندگان
۹۳میلیون‌تومن
اعتبار خرید باش!
🔹
۹۳
سال قدمت
۹۳
برنده در هر روز.
🔹
برای شرکت در ‌قرعه‌کشی
اینجا
رو کلیک کن.
شرکت در ‌قرعه‌کشی
🎁
اسامی برندگان تا این لحظه
https://www.bki.ir/fifa2026lottery
⚽️
فقط تا پایان بازی‌های جام جهانی فرصت دارید
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/Futball180TV/99962" target="_blank">📅 19:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99961">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🔵
#فوووووری بیانیه مشکوک باشگاه استقلال: یاسر‌آسانی که توافقات مثبتی برای تمدید قرارداد داشت، بدلیل دیدار با خانواده‌خود در میانه مذاکرات ایران را ترک کرد و بزودی برای تکمیل مذاکرات به تهران برمی‌گردد
‼️
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/Futball180TV/99961" target="_blank">📅 19:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99960">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
‼️
یاسر‌آسانی امروز در تست‌های پزشکی باشگاه استقلال در ایفمارک حاضر بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/99960" target="_blank">📅 19:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99959">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dciATydfgpkhCJDBBviMpZ63IqvVsXZwin-GtsnEWLHmkiyF0l4xT5DElrsCWM4gW3-Cxz5j1zA2r8j9yoZ_TeBlI3vF_CWUaaK5kBHaG3phnk3jmJODuVFwDzBeEElu0-79baiCVX9Gz49kuuF4czOmsl9Sj5FHijw91ypNxzw1AoDRAJ-7XXd7IYE1KRwbL5XAhYzWNxmOXs9I7-10F9arB8baODgcM8diEA2ZclxVYA-wNnd-qpyaKZqeUWCZtaUuxj1Ddti090NMq0jQZ0vLi1zVSQ2cU5DSbiRcDUC828kYex67pCxpQ4uIXd-WipuzkgMSTgaROIraQxOk8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری ادعای رسانه‌های داخلی: تاجرنیا موفق به جلب رضایت یاسر آسانی نشد و این بازیکن ساعاتی‌پیش ایران رو ترک کرده!
❌
باید تا تایید یا تکذیب خبر منتظر واکنش باشگاه استقلال باشیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/Futball180TV/99959" target="_blank">📅 19:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99958">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🔵
#فوری
ادعای رسانه‌های داخلی: تاجرنیا موفق به جلب رضایت یاسر آسانی نشد و این بازیکن ساعاتی‌پیش ایران رو ترک کرده!
❌
باید تا تایید یا تکذیب خبر منتظر واکنش باشگاه استقلال باشیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/99958" target="_blank">📅 19:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99957">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c8b173980.mp4?token=Xt-FL21rl9ZlXBTMbJbIo6USwwNnzdxhrQTYgICRVObtkuAMi7_O1BFQhxGLURY0b5KdoLLkoWT-ZyruwhR8wXo0gHGhdakw2MgLCg-mBQsOfYzgfdcOwKgxxDsakcC5Dk1PU5SPGYT_-bwC3A3s4imFdW6aD7ApfiOTMxlvxzLjOAfCKJrhDt5Xd9s9IDrGUtKV9yOjEDlBKlSQ351TSY3oFNNh8LaqfC0CHq6pIMGVmKINZUgLUmR488lzmrE1LZASo_EARh8um12jZf6wjAdzXsSUQnNkAp1SXpxv0LIYM5mI7kiFptPXFoKC-44ThT2tfDyMkZNIN6lOtuSkYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c8b173980.mp4?token=Xt-FL21rl9ZlXBTMbJbIo6USwwNnzdxhrQTYgICRVObtkuAMi7_O1BFQhxGLURY0b5KdoLLkoWT-ZyruwhR8wXo0gHGhdakw2MgLCg-mBQsOfYzgfdcOwKgxxDsakcC5Dk1PU5SPGYT_-bwC3A3s4imFdW6aD7ApfiOTMxlvxzLjOAfCKJrhDt5Xd9s9IDrGUtKV9yOjEDlBKlSQ351TSY3oFNNh8LaqfC0CHq6pIMGVmKINZUgLUmR488lzmrE1LZASo_EARh8um12jZf6wjAdzXsSUQnNkAp1SXpxv0LIYM5mI7kiFptPXFoKC-44ThT2tfDyMkZNIN6lOtuSkYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی گل منشوری عمو رشید
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/99957" target="_blank">📅 19:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99956">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfgqdLDLqcfRjrlc932ij4fFC85whOM-ybqt5ljFds2FumVYRxaMAsQAGz5kljuXR7sYjvZQx6cjJwSpO-I1Go-rmdlSEvLRJQieGEyN4u-iOAImF_rAEKKsGon0fy9lxVVicHD4Oi7QsE1WG1-cKgm9aAPN_EIm-NYzXB_REXH4g5zhgQBdhQWa1BTQQS62qeO6_ZrX4J5FGHaamx7HFvA6qDjlBCryCdnvyaPMwPKy5GaoyU3uD74Rx_fCZBmv6mz3_5aB51iIJX8aXp2U25AAu_0uxYYnxbRm9icu8oGINE2WajUuJNV8aqx0ceOF1G4n0L-Z0ZPGDouKiQUTNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
لیونل مسی و کیلیان امباپه تنها بازیکنانی هستند که تا کنون در جام جهانی 2026، 30 شوت یا بیشتر داشته‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/99956" target="_blank">📅 19:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99955">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_GO1fYNctcPfvVAEc5Frrg-eC04GacOyxi9Zenz0a46WMwXxgqckoQaNcYQJFeMOAHEZGLgL_WvQO15Fh1lWjhTt6ar2qp8595U8XZYDGTcnQJ0U2P3Gm1fi2dIRnImVlxFhUd0Ofb0cfHC6a5Znq68VZLxNgX8RQqTNh8R7HsrPH4tX2VWr6tH2N4s4gQ3dhTEiKYk31bowXlxspYff5uzblLCHmdzKOaXSryvfJWVGlurn8pInjPwjvM527cTUU1bkCbLSkhaXtuM8nhZ5yn22H2_KfR7vN0YWB5Hhi6vraBTaZvAeDIP59EyCgP7nK55EKA7d7bNmz2VSJp_OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
چلسی طبق معمول اسپرم خرید؛ هریسون پی‌تونی، هافبک 18 ساله انگلیسی، از باشگاه ویگان به چلسی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/99955" target="_blank">📅 19:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99954">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdjM9Q2QEx5go1Mog5DG5jaz-7r6ff0pvdjGn5J_-npJPs5yzpBHmcea-wnm0_XJOXYUQ3M-MIc3jKT2G4CTRYKxSvehSXKWRBPUq9W5LZ0k4KyOcOUQbkkmIZkurXaNlkBkRIonhFGZwEm2LLoa7_LiOpYqWBBw_2Xw_jZz2x75QWuqIgEhnGzajUTXgiGi7sWYgGWcvU08WeR4QEdsPuHTi_KvvtMTzRHW9elpnmEwf6AstfTaqZHIJNESewTBecmkSPcLEevSIcnAUIjy10S1GW8A22cJWVYBGALGuAuqlVFIhkC_jIiX3455EAi8C4QlvGCOllP_zXdJMjKY5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇪🇸
ترکیب تیم‌ملی بارسلونا در نیمه‌نهایی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/99954" target="_blank">📅 19:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99953">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a785f38a0c.mp4?token=NBQdJtg2B4Nen1hT71prX_Xa8KX8aam3kNo1LOQYjMAsBKmbtvS6nzdw3KQHf6Lqaj_pzWsBRtDXPxcj0MXVxCuiE-6ShdLBg3H319US8YiK9iwBPQNZC1LtliZ11xFfIiE4doRc48yw_M264y3_wAZK3FdCcIux33vJVGmTnqQukmOOeAZT86JPuZ7c_GNUIFzYmDZ2bKMY9rzYIWAqUGShD-BbfW0mL3SlI3CGtKgFZCdgZDJVoynHwvMjERbnDkWqiCHS8oeRQcmMMF-GyZiTmJqVu29et0EFma9BTS7KplNCT-T4f5pzt5HYXrs8niolKmCnJu3W9fIgQGdXcBL2ddTe7xYsZKRB-ZwGjN6v7yCilld7LS2nUHx1hfuBvJKZnS9PKyls97Uo2rxWKRiiHCNDm4id7kAgRxxiKq6ZV_0cHWk66BbK60pDgOEsZ5qkoDsfJoyjTmM132mVD-tQ8DWkpKYTPNksP3Ezl4g6K4Pw5dT6w0GYM23iPyLKJJ0N3bhO3FyZy_gG8ZNL3cbbn48f1zZ9urr_3l0XjNc3OByN6O_ZFEm4GHjIPQoUYc1mOODV533egaL_QZJ8pABi-AKHwf6Kqf4ISfboCGOM6e-XMLyr-bB06jNuopTdiWdfJglukoXMtWbNjXJCRIC7H8i8bkgDJC333So6N-U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a785f38a0c.mp4?token=NBQdJtg2B4Nen1hT71prX_Xa8KX8aam3kNo1LOQYjMAsBKmbtvS6nzdw3KQHf6Lqaj_pzWsBRtDXPxcj0MXVxCuiE-6ShdLBg3H319US8YiK9iwBPQNZC1LtliZ11xFfIiE4doRc48yw_M264y3_wAZK3FdCcIux33vJVGmTnqQukmOOeAZT86JPuZ7c_GNUIFzYmDZ2bKMY9rzYIWAqUGShD-BbfW0mL3SlI3CGtKgFZCdgZDJVoynHwvMjERbnDkWqiCHS8oeRQcmMMF-GyZiTmJqVu29et0EFma9BTS7KplNCT-T4f5pzt5HYXrs8niolKmCnJu3W9fIgQGdXcBL2ddTe7xYsZKRB-ZwGjN6v7yCilld7LS2nUHx1hfuBvJKZnS9PKyls97Uo2rxWKRiiHCNDm4id7kAgRxxiKq6ZV_0cHWk66BbK60pDgOEsZ5qkoDsfJoyjTmM132mVD-tQ8DWkpKYTPNksP3Ezl4g6K4Pw5dT6w0GYM23iPyLKJJ0N3bhO3FyZy_gG8ZNL3cbbn48f1zZ9urr_3l0XjNc3OByN6O_ZFEm4GHjIPQoUYc1mOODV533egaL_QZJ8pABi-AKHwf6Kqf4ISfboCGOM6e-XMLyr-bB06jNuopTdiWdfJglukoXMtWbNjXJCRIC7H8i8bkgDJC333So6N-U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
⚠️
ابراز نگرانی عادل فردوسی‌پور: با توجه به جو سازی انگلیسی‌‌ها فکر می‌کنم علیرضا فغانی داور فینال نباشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/99953" target="_blank">📅 18:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99952">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01042c6d55.mp4?token=pRYE4IHW-foVyNPD61JF8n0m4A1WVjN9EzhNn9vNcefXc6icMX_IjeSNY4dEN2afIyUfLFEO62GuS6z_PzyuYgaVU_dPWQ3bA8LYgkLQ-8hajA0vWDQRr9FW5SQVYySj28Uux1CFSidRbernsS17mGFJ2XgR7ySUQX3mZXJW8u1rSMkP2BeS8tf4tElfDsnZld5MoyqACZjKQgW8g-5nscJDj3X__EMh213vmrkJrcCHW43CVOJYB4KdVRR-hV9XABUi7EskKRKFZRSkg8Od782EVUR2QsHmwvuUyxM00IzxqMkowR9aYrkUetEhK96D3ZRLUgn0Pj6BqQdOPAPuMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01042c6d55.mp4?token=pRYE4IHW-foVyNPD61JF8n0m4A1WVjN9EzhNn9vNcefXc6icMX_IjeSNY4dEN2afIyUfLFEO62GuS6z_PzyuYgaVU_dPWQ3bA8LYgkLQ-8hajA0vWDQRr9FW5SQVYySj28Uux1CFSidRbernsS17mGFJ2XgR7ySUQX3mZXJW8u1rSMkP2BeS8tf4tElfDsnZld5MoyqACZjKQgW8g-5nscJDj3X__EMh213vmrkJrcCHW43CVOJYB4KdVRR-hV9XABUi7EskKRKFZRSkg8Od782EVUR2QsHmwvuUyxM00IzxqMkowR9aYrkUetEhK96D3ZRLUgn0Pj6BqQdOPAPuMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوتا کپی‌بی ارزش از رحمت و دختر بیرانوند
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/99952" target="_blank">📅 18:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99951">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
⭕️
دونالد ترامپ: محاصره دریایی ایران از این لحظه آغاز خواهد شد. از این پس، آمریکا به‌عنوان «نگهبان تنگۀ هرمز» شناخته خواهد شد و از کشتی‌ها عوارض ۲۰ درصدی می‌گیریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/99951" target="_blank">📅 18:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99949">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ad476d739.mp4?token=hztgqBez6C_etfhcVNA70UAC11ReCG5PtGyo7YlCgX_otcvlWguTuTtPd0-O67PHOqRn9Yku5JyjWyf_Z3nT0Uag0AQzerOqe5kg72HTdUJwCwVeJ4GEOwjyNb3Pzkvm3fVLe9BDI5EQWXD7XJliBxfH-YMbH2cBJr6rPze4o9vRQdhbqLuh47ndkiyXaUC037zjNDEbX9ZOYJr16TnnBJgkrWpLmTipwEcIGTaQPv8H78ecxer1X7xOyHBnf1vyqOz3dgBJk9YKAe6zJH4b3J6ZrBJEmKSS8OEuy7w8Mk0DeT7byI_ohKh91tYecGD1289_O99iK1NXRNg5MpgKcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ad476d739.mp4?token=hztgqBez6C_etfhcVNA70UAC11ReCG5PtGyo7YlCgX_otcvlWguTuTtPd0-O67PHOqRn9Yku5JyjWyf_Z3nT0Uag0AQzerOqe5kg72HTdUJwCwVeJ4GEOwjyNb3Pzkvm3fVLe9BDI5EQWXD7XJliBxfH-YMbH2cBJr6rPze4o9vRQdhbqLuh47ndkiyXaUC037zjNDEbX9ZOYJr16TnnBJgkrWpLmTipwEcIGTaQPv8H78ecxer1X7xOyHBnf1vyqOz3dgBJk9YKAe6zJH4b3J6ZrBJEmKSS8OEuy7w8Mk0DeT7byI_ohKh91tYecGD1289_O99iK1NXRNg5MpgKcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
حمایت فوق‌العاده مردم روزاریو از لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/99949" target="_blank">📅 18:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99948">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba993e62ea.mp4?token=t_eA3t2fcbl4oiTLatU4mm_HJDQmzxb3Ij5So1Y_EOux9aLOYTHTQ0EWlRuAmRBcVMWD0w_zpbl58-V3bQMyrQZuegFjjLRXPLdsv3nCXaAzS_Lues97gJkHyPebJpmgeSlGE5h10h6MPJ30xJ9OtxSCSgFLmy2zn_QhhdZCoVt6vp21to3rnMtEmX0G2ppKn7Fqw_1MAVTo7N6fPD2n1gymFSnBIlDmULScU3aPBSY2TkpSfD1nIqkxlO9LSEi5XnnybS8JfvxesBOJgFV1jmQx2NO-FVS0hVfie6PecsRpzfG7Sk5Z_ymAvMTNLELQlAYbChRf8juCiMV5JUvL7wh6sF8E5EACHXvDBa5aJQxyaPtWVlzqX7NDld3Obt1YeJL-yEbVD2XD_PinTSgjEUDNq2rGRL5LDwGGrVB3xN53m9xUjLxo0pmiE5TuJBYSluWCJwC6KkqhVgbpR-ih8tqex8pI4BZ7eDrdbVl1rl7N9Lb_M3fMer1rRlIotBtobJQrc0aoUXbGKO3h-EAoVGQqrLf-tMk-RbVq-zfCAXSxERAZnmGv8UtwMQjfvNaPgWSWWwJgRyxuIdn9Z7M5e-4rIXPpiLli9G_8cuFYSBlFTqBrQrENbAKhxws7AWuh07qnJwDyGxOiEMINpYa-U4nQZXBX3HjolB-xU-sDXW4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba993e62ea.mp4?token=t_eA3t2fcbl4oiTLatU4mm_HJDQmzxb3Ij5So1Y_EOux9aLOYTHTQ0EWlRuAmRBcVMWD0w_zpbl58-V3bQMyrQZuegFjjLRXPLdsv3nCXaAzS_Lues97gJkHyPebJpmgeSlGE5h10h6MPJ30xJ9OtxSCSgFLmy2zn_QhhdZCoVt6vp21to3rnMtEmX0G2ppKn7Fqw_1MAVTo7N6fPD2n1gymFSnBIlDmULScU3aPBSY2TkpSfD1nIqkxlO9LSEi5XnnybS8JfvxesBOJgFV1jmQx2NO-FVS0hVfie6PecsRpzfG7Sk5Z_ymAvMTNLELQlAYbChRf8juCiMV5JUvL7wh6sF8E5EACHXvDBa5aJQxyaPtWVlzqX7NDld3Obt1YeJL-yEbVD2XD_PinTSgjEUDNq2rGRL5LDwGGrVB3xN53m9xUjLxo0pmiE5TuJBYSluWCJwC6KkqhVgbpR-ih8tqex8pI4BZ7eDrdbVl1rl7N9Lb_M3fMer1rRlIotBtobJQrc0aoUXbGKO3h-EAoVGQqrLf-tMk-RbVq-zfCAXSxERAZnmGv8UtwMQjfvNaPgWSWWwJgRyxuIdn9Z7M5e-4rIXPpiLli9G_8cuFYSBlFTqBrQrENbAKhxws7AWuh07qnJwDyGxOiEMINpYa-U4nQZXBX3HjolB-xU-sDXW4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
🏆
در قوانین جام‌جهانی سیستم وار در صحنه‌ای که بازیکن به اشتباه کارت زرد میگیره میتونه دخالت کنه و کارت زرد از بین بره. نمونش بازی آرژانتین و سوئیس که پاردس اشتباهی زرد گرفت داور رفت صحنه رو بررسی کرد و بازیکن سوئیس بخاطر حرکت تمارض کارت زرد گرفت و چون زرد دومش بود اخراج شد...
❌
در نتیجه هیچگونه تصمیم عجیب داوری به سود آرژانتین نبوده و مطابق قوانین رفتار شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/99948" target="_blank">📅 17:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99947">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
ژابی آلونسو:
انزو فرناندز میخواهد در چلسی بماند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/99947" target="_blank">📅 17:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99945">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLAi3uEGgNh2_LuGUfF7WyQt8df4PsFsLN5Mhfam4LUWi9At-s8BHt9C_TZN-tIAuRi0LKSpgRj6XM7L7wXt3ynsvpY6bFevLjBtal9n1ONSdyxLjrVKCE_ZFpIjvkNqi-KuYvchIeYCHO1pdNp5596FNpP7fy-HZGzwUJHpRW43YfyLSmK6AchrxyVnqzY6P70angz44fAw3mecwF-xustks1Zh43mqJX8ACbh7Kp1JE5zH7fe2vsNe88ZzeON7xaZwhLbSYlekMo27acp9Iai0WfyBQ_lsavXJ-GAK9tFhCL3WUpWRUlJzHSa0QgEaWHdvl_2OHnNVsCcV77P7kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رومانو: لوکاس دینیه به پاریس پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/99945" target="_blank">📅 17:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99944">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PncgdPLScyhH81lfXf-zbnqdIUDKlpL5p6BwMBLnyDDxRj8-IzSA63d0t8SK846CsUWJ0iC0NUngX1dllEkapoF-ZjZF5d4qIteUzHMi_QGCuXpYPf0l-6CqghQWKPOBRr_pE3zc_jW__FCnRmcTlkqc0PlUdYZRZ2bt_AVjEH3cPCBA2zjAhoJFien2BzVkMxVRpWGrI-cbhkwG-RqFdYROzeSaX44gr1bUUrItHE__kdBKJSuqC9q7grghbAVz4P29jreWDZctWAecwhodq88ism8Jtw4K5WmeVvv_PpGwSKU_oSbQ-NLMUhy7cesgLcINKIaBGd6x4i7kxQwdaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤯
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب احتمالی منچستریونایتد در فصل‌بعدی با توجه به بازیکنان فعلی‌اش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/99944" target="_blank">📅 17:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99943">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/as9Er5NVujF2avYEIwJnYZxLkuHlqeyVQTpQfKNr8C2inqDyMP7kQL3pVkpSj0n1CR27GKIBPf9zdJjNjLfhPHurUdDTXXI0UvRrxDvOcW2XGm1rSm0TflJX-rzQQQDjbZO_-m4EwZeMLokSBoU4OZjZ2deJWuQ4oHQTAPkmjdTYQLn8PAlCnsW_K9VX3aFYAxC78DgEsvcvf_7Fi8lPg9UeGt8wz4S6RKeqohWGRWTaRxPKouOSdkzO26E21ydHF26RXQTG2AICI1d2A44qDeDVjZrldqz42C-Ea4ePiz3cXgK6Y1IOt_Ab47FWr8-UHjMDfUAGjf1pHXjG1DGF0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رومانو:
لوکاس دینیه به پاریس پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/99943" target="_blank">📅 17:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99942">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d594556eb.mp4?token=n7LzaGqi2Z_17xye51obpOp4BcbywFClEwOw4LzJOWVyi-0jtfI9VLLAYMEjhnuJL1EW2cep0OoA7IY_v5Cv444fqDUeDLslKaZovkkm84FDh6ELcs-4zKf_xsNhM0WqrxUjjKEa_u_2SJ1sBSCjYDtH5SGBXwqyQ4vfw42Kr60WDOH4BjegNmM9M7LFp1kLYMDmFR0axXf864Vz0RlErfnnJFwR1rdpYxU1sdRTVuCd5TgPwyRITjwbYmGvWZ3R9Ls__WBETX3Zc4ZnnkSoOMwp74QqacBNM-J5BVJS4o3f6Tj8wt40cWWJn0hh5RU7qSo0P2MmLA5LNwnXX_TSNTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d594556eb.mp4?token=n7LzaGqi2Z_17xye51obpOp4BcbywFClEwOw4LzJOWVyi-0jtfI9VLLAYMEjhnuJL1EW2cep0OoA7IY_v5Cv444fqDUeDLslKaZovkkm84FDh6ELcs-4zKf_xsNhM0WqrxUjjKEa_u_2SJ1sBSCjYDtH5SGBXwqyQ4vfw42Kr60WDOH4BjegNmM9M7LFp1kLYMDmFR0axXf864Vz0RlErfnnJFwR1rdpYxU1sdRTVuCd5TgPwyRITjwbYmGvWZ3R9Ls__WBETX3Zc4ZnnkSoOMwp74QqacBNM-J5BVJS4o3f6Tj8wt40cWWJn0hh5RU7qSo0P2MmLA5LNwnXX_TSNTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🏆
هماهنگی‌جالب مسئولان برگزاری مسابقات جام‌جهانی قبل از آغاز هر بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/99942" target="_blank">📅 17:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99941">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfVhuL4J4tv8xly37QISpmq0MaPN8XjAVDOXjEl64QVF1bL2SIQUlyXR8KWrl18t0vGI1FnSwuAHPoZ4MvFM_DVMNvdrBZDqnaiisgqzrZhyVetIagpRZ68ImKs2fkn01mCvfubFzFbJKX8ZatKdta6HzDCq4UO0xH7N1lKrUo1MfEssZf78kNcdCNa0Wu4GDyo2jFgZxjEixA6VWR6qhAeqndLp5h-9FPgNnlO-tXZcw2i3sBeBm_GH4MA0OA3EOnzGjGosMkUcP1xXFrbuzNYNWQs1hyP4kRmUuAzB82e_7e31d3-YF0EP8l12Jfkaqm4QMFULhJbCQpJFvIKH0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عملکرد امباپه تو 2 جام جهانی اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/99941" target="_blank">📅 16:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99940">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPSLxFIE3l2C0zy-Vbg7VTnOKZXhOBKwYEOqVHqRrKAK_9kYKpALCrAZxzQr1MSk87Yht6sT3lRkNC3P9gMj_fWQDJfnasHKi6oE06oFKeUIGXzQ43v5Q5m9PYNvakiPIjH4I5xIUI_ilHsnxUtsEQ7LOCad7rBsBuyYJAk8iQLxpqN02__TbOBoneA-aT8MdsOO9VYCEH3mzg4CE4mhbGEgEg2-qGSwJ0X9jmruQruIUZ8rrwc5vnY2hDNnenKgOZU9nVk2Og49dWWjHf7ce0adqc9cx2DAs7pyGOKqFJ_kVlcR9mVaID-gpvfVcTCXDT6eaqev-oKzxy2zwEeZQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بیشترین دقایق بازی بازیکنان هر باشگاه تا این لحظه در جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/99940" target="_blank">📅 16:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99939">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/99939" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">❌
با هر 1 میلیون شارژ ،
🅰️
🅰️
🅰️
هزارتومان شارژ اضافی بگیر
🅰️
بدون‌قیدو‌شرط
⚽️
تنها سایت مورد
#
تایید
ما
✅
اپ اختصاصی بدون فیلتر</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/99939" target="_blank">📅 16:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99938">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1pzLui_xaZQY5_Nx4fry0TzUPhHfYKWg-hdVTQTW216---vP9zITokIgP-6_FRMxbp2zcmmktIeNRXmAe9zOXt1cGcI55MxvycjIAW8CkWNsrq5CkOwaM86vjE23qoI_tCAqUc83R9v0bjBbjr88U6UBCryLRujOnz5aMrGpAaKxoH-jBqnqQgz1_Oxe3geu2syv-IRxvv6xmeM8BJjf8Vqx6N8q74bk0y3QWY7XarkSVSSVr7splCTrgQu2PjzpB-iaLM1UbkXPRhu6rCRmguuaAkaC5EVZPZnzV-DIb8LBJByM8I1gNS8g-NsANqBN5JVUPegm9D3998QrszWHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تنها سایتی که ریسک شرطبندی
🅰️
🅰️
🅰️
آورده پایین#بت_اینجا هست،بخاطر اینکه :
🤩
🤩
🅰️
بابت هر شارژ موجوی اضافی میده
+
🤩
🤩
🅰️
کش بک بابت هر باخت
🏅
بهترین فرصت سرمایه گذاری و چند برابر کردن سرمایه :
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
r21
@betinjabet</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/99938" target="_blank">📅 16:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99937">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aef0fc183e.mp4?token=OwbUu9-zNHR1gTOO5yEKDE3C7zvXVkwM9RCb8PXiliE5xPPhER_4zbe4wkdhKeRqBHlTNoaaPzPs0Vj_bm_M126N_a723DAMJOK73D4LJtf9ny-OfGzZZk3kDT5MGHMs5Up8EL_BvwzHJ9JlDrPNrcXt__hmf2bmT5g5Bh5ci3WdY6G5jUjKbnXMYwnBkiafOujTxsKc6DBkGZJyxeCCJFNqEtMQkBanhUPIFyIoAxic-xZCKGnUVD5y5lR7Vnbe5-R5Dr4Sya7KIOsbtqrTIG2QgsvkKj2Qo7MowyQ-0aF4QOaKujYT78JW-tZqE5TfyVK1Z7cWJuAZLW0xR92L5Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aef0fc183e.mp4?token=OwbUu9-zNHR1gTOO5yEKDE3C7zvXVkwM9RCb8PXiliE5xPPhER_4zbe4wkdhKeRqBHlTNoaaPzPs0Vj_bm_M126N_a723DAMJOK73D4LJtf9ny-OfGzZZk3kDT5MGHMs5Up8EL_BvwzHJ9JlDrPNrcXt__hmf2bmT5g5Bh5ci3WdY6G5jUjKbnXMYwnBkiafOujTxsKc6DBkGZJyxeCCJFNqEtMQkBanhUPIFyIoAxic-xZCKGnUVD5y5lR7Vnbe5-R5Dr4Sya7KIOsbtqrTIG2QgsvkKj2Qo7MowyQ-0aF4QOaKujYT78JW-tZqE5TfyVK1Z7cWJuAZLW0xR92L5Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
حمله بیرانوند به عادل فردوسی پور به خاطر اصلاح شایعه مجری صداوسبما. شایعه‌ای که درباره تعریف و تمجید ژوزه مورینیو از تیم ملی ایران دست‌به‌دست می‌شد، با توضیح و اصلاحیه عادل همراه شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/99937" target="_blank">📅 16:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99936">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
مصاحبه جدید املاکی: یک توافق داشتیم و آنها آن را نقض کردند. آنها توافقاتی که داشتیم را زیرپا گذاشتند بنابراین ما فقط قرار است به آنها به شدت حمله کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/99936" target="_blank">📅 16:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99934">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92cdfd4ea7.mp4?token=n4GC2kt3liL7VsZ0EsztDkLNWbJKv2U8LBEdm45LRslW6wE2e4nZ_bER1XIvxaFrNk-eZUvpUl0TgnPimf5UryFHbg4HwtXRmvNN0cONPOlifxQ_PGY4cvQwXHuTtNT57b3sDvqQfkJYHjHGYhghEkD29a8BPmu0d7Igy6SdnkgOW81IMl4dT0giBw6MvqnpLbuw1v5nI8fS7W_yTIB--j7vHAmaxflSMr3TiZdUcbrEdiP0ZYhcQPmD2oa0eORyf5Jr41WojSKNvrE0nJbEQI__xRzeWo4R-vIM9xqBgGVWrMFRq0NQUIfk0qZLGCPrwv9_ygWuv0Dc7TPsZXxc-h9UZ0mpBd_4ojKu4USioa0mO64oUGSVr6sZCA5cxbC4D9WAkLRGfIWXUmtFbqWpsKzTU7UvRrcOE-nzPeqwM2L0ibjeF6y2E5OyJAgLdlpH7tiXHiTgQ2RaN3gEs2BBLNNh7MmLOB0VQ6JL92lTSSDrfEykJ72r0e3TGH3-R3fqsZBzTVHVFRq4DunvCATk8YD3ZGgl0HO7igZOgCp66Fy-MJWsvLD-sxPTauHjQ1YNnMRHU0uGBivX1rNRT08tH4MI_6wX2d4U5UVKAf2y_JkNXP2HmzpZKlBQMXmsmlGQlCkkKoWCex7eGUFWVzlD1dXxkGcmntcOzsZX3FWCm5I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92cdfd4ea7.mp4?token=n4GC2kt3liL7VsZ0EsztDkLNWbJKv2U8LBEdm45LRslW6wE2e4nZ_bER1XIvxaFrNk-eZUvpUl0TgnPimf5UryFHbg4HwtXRmvNN0cONPOlifxQ_PGY4cvQwXHuTtNT57b3sDvqQfkJYHjHGYhghEkD29a8BPmu0d7Igy6SdnkgOW81IMl4dT0giBw6MvqnpLbuw1v5nI8fS7W_yTIB--j7vHAmaxflSMr3TiZdUcbrEdiP0ZYhcQPmD2oa0eORyf5Jr41WojSKNvrE0nJbEQI__xRzeWo4R-vIM9xqBgGVWrMFRq0NQUIfk0qZLGCPrwv9_ygWuv0Dc7TPsZXxc-h9UZ0mpBd_4ojKu4USioa0mO64oUGSVr6sZCA5cxbC4D9WAkLRGfIWXUmtFbqWpsKzTU7UvRrcOE-nzPeqwM2L0ibjeF6y2E5OyJAgLdlpH7tiXHiTgQ2RaN3gEs2BBLNNh7MmLOB0VQ6JL92lTSSDrfEykJ72r0e3TGH3-R3fqsZBzTVHVFRq4DunvCATk8YD3ZGgl0HO7igZOgCp66Fy-MJWsvLD-sxPTauHjQ1YNnMRHU0uGBivX1rNRT08tH4MI_6wX2d4U5UVKAf2y_JkNXP2HmzpZKlBQMXmsmlGQlCkkKoWCex7eGUFWVzlD1dXxkGcmntcOzsZX3FWCm5I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
🏴󠁧󠁢󠁥󠁮󠁧󠁿
تقابل تاریخی انگلیس و آرژانتین چهل سال پس از بازی دو تیم در جام‌جهانی ۱۹۸۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/99934" target="_blank">📅 16:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99933">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MT3p8IiX3zMzJohaocdfM8POq0EJs-QYYNdE7NMkxmW1zEVyFnwBj0kBMd1iF_0PqeOhFA1EanDnbOYE6JJwWtUyoqYxH6KHOfKmpn3erXfMEYphDfWG6TAZMa7QeR7Sil8bKXEV7BUmX1BjTcuid1DBemIwXbNqX8lD1YfWQkVSYJQIa11lcS75QRIUlWSBDfsNWsQnUQOkwdtpnIi8dh2wZoq0KXF1j_RnfcpBr1lD4VDqgBDtMOslbkXOO8dqMXH1O_LgTP67wTe_VDeVaTKkctXKlBke3uKyqvx9TuDO1glegngoG6yGCRENPpzc12dRf_ooozn2mPjhxv4x4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: بزودی یوری تیلمانس به منچستریونایتد HERE WE GO SOON
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/99933" target="_blank">📅 15:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99932">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wn_yrDLVVLfRVvET2XqlqXhOopnVjrdMFjlRB2pvGosIUeEX9zLX-79Kjg-5hFD1HdP85ARwsA3FY9pBWSnmkgxZ387IPfu7qXfoRpxZvy75B7z6MSmfgNIfTVCX1LJq0sE0Z8Vmidz6bjBQTpUfaMWLWMuWAmBwhE0QIeZ4KqH5ZojCopkfKF_-5sLqZXzovCPJ_M-dMxje3Q5GYKuGCaObgm359hbWwH02y8I0_2YcxVnXXLy3yPwpsbgSaxeVs_-S3hAG1IR_-_ZzFUpnPgPCW2df3Pn5Y4uaIeHgRGw6nTV79wOmtr8TeJ9Rwbd7xyxfEuWCPifQjwFGkHkQ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عشق بارسایی ها تو تستهای پیش فصل این تیم شرکت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/99932" target="_blank">📅 15:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99931">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇫🇷
🇪🇸
تیزر جذاب از بازی اسپانیا
🆚
فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/99931" target="_blank">📅 15:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99930">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/155791f176.mp4?token=X3kIjuKnvGD1EDLluy872Vb5nL99gpZmVsnUjpmyRQURMe1D9haL7CiduEBB9EbXElfo3QHEuYpIYrpa30xDdF7rHBBTIxuVDOnKOCSame504bvXRUZm30d0gOSIHZDa35zjNaqHUx6DO0DYCiqQCXG6g2xUMGbynWiW-JNnakcKqycck9Zxqtv_K7v9A0pQXo2nzbdJ-j4xRRZ1-KVzLsggE0wFKIndz9uOqPo8EsaBeJLXSLrxwUYwnew1PSUmY5QUrkXSvAf3BmC5RzTnt4O12P8C5H66n7BEgCrVCNQ0zFaWDlamScB7sYceUlsc6pV4XE29KoVcv-cmgkchEL4txWyL0-rouu57Rnyhg760MLYXVkJ2Bz_YDA_pZIvGpnR3PkIQyFZTE2uMLwplq_1LyGwt7hZCc3ds4P1WFnIz6JKd9w1rclIWUBuJDheSwCJ8VxtdywtngitZ8vUM1b_3Po-ewFnWBJ9mqZh96fHxHwUjx_7Qmv38Y6w_juBTfiTSzqC2Eo074yJGkhQEzWqTj0mej88OjFCAlZG9y6LuvYRom3PJ2qUsUgJG320qKt8F8Tn8mv8IqEdz_lUbnA48qMsOWb3fYiFRixTmIt_z-1XGO-uFl7SSERR9H6zsSlM5K3H1KxApIMkG50km56Qs5nynEKvDTkZGUGxu1Xc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/155791f176.mp4?token=X3kIjuKnvGD1EDLluy872Vb5nL99gpZmVsnUjpmyRQURMe1D9haL7CiduEBB9EbXElfo3QHEuYpIYrpa30xDdF7rHBBTIxuVDOnKOCSame504bvXRUZm30d0gOSIHZDa35zjNaqHUx6DO0DYCiqQCXG6g2xUMGbynWiW-JNnakcKqycck9Zxqtv_K7v9A0pQXo2nzbdJ-j4xRRZ1-KVzLsggE0wFKIndz9uOqPo8EsaBeJLXSLrxwUYwnew1PSUmY5QUrkXSvAf3BmC5RzTnt4O12P8C5H66n7BEgCrVCNQ0zFaWDlamScB7sYceUlsc6pV4XE29KoVcv-cmgkchEL4txWyL0-rouu57Rnyhg760MLYXVkJ2Bz_YDA_pZIvGpnR3PkIQyFZTE2uMLwplq_1LyGwt7hZCc3ds4P1WFnIz6JKd9w1rclIWUBuJDheSwCJ8VxtdywtngitZ8vUM1b_3Po-ewFnWBJ9mqZh96fHxHwUjx_7Qmv38Y6w_juBTfiTSzqC2Eo074yJGkhQEzWqTj0mej88OjFCAlZG9y6LuvYRom3PJ2qUsUgJG320qKt8F8Tn8mv8IqEdz_lUbnA48qMsOWb3fYiFRixTmIt_z-1XGO-uFl7SSERR9H6zsSlM5K3H1KxApIMkG50km56Qs5nynEKvDTkZGUGxu1Xc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😆
امیرحسین رستمی
: در برنامه شوتبال من خیلی از مهمون‌ها رو نمی‌شناختم، به علی علیپور گفتم تو جوونی بپر سریع برام یه لیوان آب بیار خیلی از بازیکنان تیم ملی میومدن توپ رو نمیتونستن گل کنن ولی من گل میکردم اونجا رو کات میکردیم از اول میگرفتیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/99930" target="_blank">📅 15:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99929">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrLYaRZPo9T94UOBy3JmGxFtM-Hfh5T3Fmtw3g2YR1vRytq52w1-TVtHuWtTYVaNQB4RbNfRprjoQSfSg19v4RjsNiAfQiT1jdO8jWdBgl1UVgKe4wdJi_8NzUXnDUntNqAT30Rjx48Qf_gD9Br6p0lf2lpT8BXWmxstBRe4JXI3R4HNulahcs0D3W34ERbXcSDe9INNXXD4aExbEENFOvyufxhVh6ESaD4l23Qb426IH5WsHCz3dM1UzEjHwzAAg2EKU0ZDKxy1uYCOChEIhfsmYOaT8Ut6jI4E51ScPkBoql37EVDj92FzNT3Wh2YOKwK-__SnHc9vH5OtJWaD6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باشگاه رم قرارداد پائولو دیبالا را به مدت یک فصل دیگر تمدید کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/99929" target="_blank">📅 15:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99928">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb6395bcd6.mp4?token=QZm3rr77Q6BAav0mvgDaEoyhe3RgFdSAjt7SljVAHuHRw_jD32GY6JdfLAdN4kmSpIfM2Kcu8RK5xqMWz7TCABa1X2DFDAQE3zHm75evUN4jC1BL9pc3qT_MMLHrzPl4iXTAW5VSFauvmvfaG1sLypu8FOLVEu71PiunPpgtMKRiGgrdx5TOTOmVxirgWE79DDo-XmiOn789uO8xu6zX-cFDF5PaoJPE0fK9MrFcDKSvSqPSOwyLxvP-RBCtLo2jh4sIM8ehkZvozxKGv0WCvUa7ijY1V8PK6cGdfFCRCvba0ZeEhsWNxWq4nf3iF76WGEIzxGxEIm9DnTv5rezFVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb6395bcd6.mp4?token=QZm3rr77Q6BAav0mvgDaEoyhe3RgFdSAjt7SljVAHuHRw_jD32GY6JdfLAdN4kmSpIfM2Kcu8RK5xqMWz7TCABa1X2DFDAQE3zHm75evUN4jC1BL9pc3qT_MMLHrzPl4iXTAW5VSFauvmvfaG1sLypu8FOLVEu71PiunPpgtMKRiGgrdx5TOTOmVxirgWE79DDo-XmiOn789uO8xu6zX-cFDF5PaoJPE0fK9MrFcDKSvSqPSOwyLxvP-RBCtLo2jh4sIM8ehkZvozxKGv0WCvUa7ijY1V8PK6cGdfFCRCvba0ZeEhsWNxWq4nf3iF76WGEIzxGxEIm9DnTv5rezFVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
انتقاد بامزه فیروز کریمی از مهدی طارمی: «میگفتید دونده می‌آوردیم جای شما!»
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/99928" target="_blank">📅 15:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99927">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cee2da53d.mp4?token=j6ZWCSqXe3sXM_HPN08xqMa-GQUjHFzkbBv1I_RuyK8PFVg5vGQ2VnAm3GwFJbxvzWYt3lQbxjf0qbRCTAu2bnoZyDoDfM05n6yi8iRkJEXoTfOOnK1uhmdtBU79vLtwJMxe7R7vGEge-LBp89pGIwf-GgGRxh1tsbGUu0sk7Fo0AQl9HdiBwO8svnNYsQ60qJC3mQ_pg9Xy7js3hdqdWYJQ_J_eOToapji9NRVhcFF2DdYMK7tsrXK8EfJWlxXrHEp3Fs7zG2H428VNl2M8-7lZh4SPnQfOgw8i_LVnMCMARxnxqe99N2UCTHR4GqaNMsxm08Lw3-hzoCinFVlIlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cee2da53d.mp4?token=j6ZWCSqXe3sXM_HPN08xqMa-GQUjHFzkbBv1I_RuyK8PFVg5vGQ2VnAm3GwFJbxvzWYt3lQbxjf0qbRCTAu2bnoZyDoDfM05n6yi8iRkJEXoTfOOnK1uhmdtBU79vLtwJMxe7R7vGEge-LBp89pGIwf-GgGRxh1tsbGUu0sk7Fo0AQl9HdiBwO8svnNYsQ60qJC3mQ_pg9Xy7js3hdqdWYJQ_J_eOToapji9NRVhcFF2DdYMK7tsrXK8EfJWlxXrHEp3Fs7zG2H428VNl2M8-7lZh4SPnQfOgw8i_LVnMCMARxnxqe99N2UCTHR4GqaNMsxm08Lw3-hzoCinFVlIlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😞
😁
عذرخواهی علیرضا بیرانوند از همسرش اکرم بخاطر تشابه اسمی که با اکرم‌عفیف داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/99927" target="_blank">📅 14:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99926">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3c7adc098.mp4?token=lnM058BSfCjjQzilTvQnjGS0yTE6q3ZTs0vOvtZro7tu_e0M_rE-vsbEujBMlI-M0ABQaRKA8PzaMIe3vbiv18gJYzjCrEiVHyq7uB3GRyfCUF91dKIlIEmNeLFNcrEhlxqwG5n3yoTXWidHH9cTqt5dUDq3VVXf9VeFP-T7daAh0ILISZIY-4KmuU2xgLQiBJYWIPCPUUeOflsmouT50YS1nT7bNPDdW0y5pUjnATpEWyiOWLmZBQDrPa59ByrI2nLIFpQ_Rk84qaY351g0pPSe5Aj3OICnFXrFqdw2FJH6l5uhYOEFGWgQKpq2GoeIaXLdiO9YYcySjzf-R9WhcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3c7adc098.mp4?token=lnM058BSfCjjQzilTvQnjGS0yTE6q3ZTs0vOvtZro7tu_e0M_rE-vsbEujBMlI-M0ABQaRKA8PzaMIe3vbiv18gJYzjCrEiVHyq7uB3GRyfCUF91dKIlIEmNeLFNcrEhlxqwG5n3yoTXWidHH9cTqt5dUDq3VVXf9VeFP-T7daAh0ILISZIY-4KmuU2xgLQiBJYWIPCPUUeOflsmouT50YS1nT7bNPDdW0y5pUjnATpEWyiOWLmZBQDrPa59ByrI2nLIFpQ_Rk84qaY351g0pPSe5Aj3OICnFXrFqdw2FJH6l5uhYOEFGWgQKpq2GoeIaXLdiO9YYcySjzf-R9WhcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چهل سال بعد از دو گلِ تاریخی دیگو آرماندو مارادونا، این بار مسی مقابل انگلیس قرار خواهد گرفت.
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/99926" target="_blank">📅 14:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99925">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1294ecf8b.mp4?token=ZISrpEaK0SMs498Sg4SKqxNrRgm1dPRIf013LXy7GAm05lUNQnAcI6H9s0iPvola4Vu8kevL25_T0b5VVmiKfWtyEhEjkmytk63HNbMUS2s6EDnHrtg_QsIBhZ9NlkbAbl_LU9dG8DVKlDfuXp3DCoiz_AnVSe2vOih4DE08g89SSKMW325KUR76BzESLZI85XvAP-Dg_bwWoSooow_oUCN9aT6x5befuwb4Hroa4lEHzxJkD9GocqMOi8UO2l8a8NTeqTO2b0fX0Hm1SDz7RVSKbqU_MjQr9A3R7UmOrjaXlhlsfb6yx30NJmuVRdTLeuJ81-l8RNsKRg1P-3wuyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1294ecf8b.mp4?token=ZISrpEaK0SMs498Sg4SKqxNrRgm1dPRIf013LXy7GAm05lUNQnAcI6H9s0iPvola4Vu8kevL25_T0b5VVmiKfWtyEhEjkmytk63HNbMUS2s6EDnHrtg_QsIBhZ9NlkbAbl_LU9dG8DVKlDfuXp3DCoiz_AnVSe2vOih4DE08g89SSKMW325KUR76BzESLZI85XvAP-Dg_bwWoSooow_oUCN9aT6x5befuwb4Hroa4lEHzxJkD9GocqMOi8UO2l8a8NTeqTO2b0fX0Hm1SDz7RVSKbqU_MjQr9A3R7UmOrjaXlhlsfb6yx30NJmuVRdTLeuJ81-l8RNsKRg1P-3wuyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔴
🔵
علیرضا بیرانوند:
مهدی رحمتی بهم گفت مدیران استقلال نمیخوان‌باهات قرارداد ببندن پاشو برو پرسپولیس من قراردادم رو باتیم استقلال تمدیدمیکنم‌. من‌ رفته بودم که دیگه قرارداد ببندم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/99925" target="_blank">📅 14:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99923">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mpFLp8xjrv-wiG8Oov_xDKoZNabLotV_Btpb8kKFThri54wibq2lkJ1xFDg_pF-vwyo3I5ynKTLu1DIH9_LeMtzBKfj20m3W6x0Ru7bnlkiJveEpolmlZf58gFzwfyuhRcVCamSprVrw1w5aa0oajARmw9GhyYEOngVImKlXa4xZECYdVwoqRA8DW8CeO9M1ccePw_GamSNkDIwHYgRQla5Zdzxxf411jPKsdI0UOh426gIdVzUuj6O1Kz8YnZlk4-ENML6B4Gong-R5ODmDEeJyIVtG1QWgw_FMUbycSTGY_ho-UQk5mKjVNiiizpiuwhH8FSrb98GZ0yOGf4DgwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DF8t1Lc0u-yDpi8fkIICDoumD5IvF8EbKZo9a0eTSb4Vrqr0e59OfWYqBgkAT0jxwXLyd-kIDsmuo8iPzse31CjvybHSjQUrPTY1UbNaMK8242ki9V2-4wMbP-EVbzwUYnpdjcIousFxJVLDT3x3Q90Bg1Tc_B5w1-iCdbfy-m9UTXFe8SOfFOLKIx52qi_Q02ETk7vmc-8QU9vCWbuDI-vO5Zvktven2G6m7nBCIDPeMmITmMMHDsfhEFa1-w2ZPsp9pCideWuVcjRb6uNeOq33gz7GGI43hbeVcE5tuJRUoi5rU_V0taTQOf-cLX1zEy_N6_rSVNZqpbp9_eBNDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏆
دو داور فرانسوی، تورپن و لتیکسیه، از ادامه قضاوت در جام‌جهانی کنار گذاشته شدند. دلیل این تصمیم حضور کشور فرانسه در نیمه‌نهایی است. این دو داور از شانس‌های اصلی قضاوت فینال جام‌جهانی بودند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/99923" target="_blank">📅 13:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99922">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgRoCLaYsARDL_LhEtIsO93xtjwUo_QJ5anYlXscxwvfCHq7Gp2M71zBytmuVEXb5By0-mzf2L06Veswb71IRZZn2stV_5Q-B9s3sufzhlDepeR7S0RF-JhTteEge2n1Nn31f961NOI7p0AaNYbuqLLzq_RfGBiD-qUqpNRVcLhwCITPcXMPk1QdHxUJfT_iKD7fS3qAgqGGDxWk1R4yGN1sgVPXfhvjmYLWZktRjlVImny8zHITHRZZfMHf7d5UWhVuiiCv5LlvZ_KvwKcOMwlGIBLmMsHHzo_InKfm0RdSdfEbQS917q79JAO4qK6X7xlsOh7gNBKqLq2crLyScQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: بزودی یوری تیلمانس به منچستریونایتد HERE WE GO SOON
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/99922" target="_blank">📅 13:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99921">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bae154b9d.mp4?token=OQ6mpAnmbGTNuSHFKEBZ77gFTZiYe_5A2urGIDU2TtqhzTYXN8RqPD6JC6k0SbmDEa5SHFHDU7eGOhCMd3CRB8bJMRaOI1ANs8f7u12ImNsRw09oPisNzKuRwwiuC5lioz1VkZCt7VNIoNl1RLny0EOaZHn6GvI82S8ndgq6tgiMGJ0ZBMQgbTyDNrVOLqSuIh4mKGbfHH8JwwfopXQ1lL3ZkYzpG6TXX0WrOdezoIaCMAioqDTeEhVjFXhQHigdmIf-5l8aj0Lq-Bg33H6MBy2vsgRX62-uQs4FdkA53VQY70Hbcilrd2f0ddavDAulHaQOxZU0RPC8e0YsmkFriw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bae154b9d.mp4?token=OQ6mpAnmbGTNuSHFKEBZ77gFTZiYe_5A2urGIDU2TtqhzTYXN8RqPD6JC6k0SbmDEa5SHFHDU7eGOhCMd3CRB8bJMRaOI1ANs8f7u12ImNsRw09oPisNzKuRwwiuC5lioz1VkZCt7VNIoNl1RLny0EOaZHn6GvI82S8ndgq6tgiMGJ0ZBMQgbTyDNrVOLqSuIh4mKGbfHH8JwwfopXQ1lL3ZkYzpG6TXX0WrOdezoIaCMAioqDTeEhVjFXhQHigdmIf-5l8aj0Lq-Bg33H6MBy2vsgRX62-uQs4FdkA53VQY70Hbcilrd2f0ddavDAulHaQOxZU0RPC8e0YsmkFriw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیرحسین رستمی: وریا غفوری رو یه ایران میپرستن...
‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/99921" target="_blank">📅 13:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99920">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scbTP5wsLTJGDa53mvf8WEBqSyjLqV9gitqEvh3kL7rlnVyJTr5-O36PMka6fkJPA4ZcGbu6xN7mxHSQ-WLk14kkfPCv9ZCVEwXjoNgppjKayz_4Fk9paEJSm9RX-HTqFzaNgWEvDdORVu7klvXfiaaZJxOaUGHXN9xdI-6qflGh8mSAIhM1ses04UwHYj29Jzf_L3g6WBK7oB4qZMv4LLAGiFh6bPYitFXZLttkv3xmro76ScuuUtri4tS345SUm-1go9AzgFEc3VBJIcUHTCK1keg9pK7SEfXbwpyE8pcK_Z0Jehj8ovR3O0V2li7nyAd6psNp74AZyi1yo_-LYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری دیوید اورنشتین: باشگاه منچستریونایتد درحال مذاکره جدی با استون‌ویلا برای جذب یوری تیلمانس است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/99920" target="_blank">📅 13:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99919">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
دیوید اورنشتین: باشگاه منچستریونایتد درحال مذاکره جدی با استون‌ویلا برای جذب یوری تیلمانس است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/99919" target="_blank">📅 13:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99918">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70585e20b2.mp4?token=uldHDi6XMcGZyFCK_xJHaUDwevaofO7ArAwbOk5VzZa6g5AaTTOUJWcc5xfiiOwLzMmgalz8M4fhExdOEQoKUkADdQUzakRKpz1OzdHxY3vuqaxaPfSxsw0Qyq-NNHnuw07yt3e6vbTYAMRdcPyD37GS-YsXxHlIKXKwdiMfrPhAkh86ckza4_d95ZjbjKLTvUfyoe_65TyY7g4O7pBqEW8nfxTuvFpBEskkKP0wlugRqm3p8Ez89a44SzXqCgxttUo7e2dzvriA5UnFxDLUd6uagXaOJLd7hr1LtVtg8u9RcKILcWpx5hzWok6KmUNpxlTsjQQ14St89IYl-I0Xgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70585e20b2.mp4?token=uldHDi6XMcGZyFCK_xJHaUDwevaofO7ArAwbOk5VzZa6g5AaTTOUJWcc5xfiiOwLzMmgalz8M4fhExdOEQoKUkADdQUzakRKpz1OzdHxY3vuqaxaPfSxsw0Qyq-NNHnuw07yt3e6vbTYAMRdcPyD37GS-YsXxHlIKXKwdiMfrPhAkh86ckza4_d95ZjbjKLTvUfyoe_65TyY7g4O7pBqEW8nfxTuvFpBEskkKP0wlugRqm3p8Ez89a44SzXqCgxttUo7e2dzvriA5UnFxDLUd6uagXaOJLd7hr1LtVtg8u9RcKILcWpx5hzWok6KmUNpxlTsjQQ14St89IYl-I0Xgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
تیکه ابوطالب به صحبت‌های اخیر بهاره افشاری: لطفا چمن مارو بذارید‌تو کیسه مشکی اگه خانم بهاره افشاری ناراحت نمیشن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/99918" target="_blank">📅 13:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99917">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7de78bd0d8.mp4?token=C8WNryPMahWxRfhnB2wyDGZ4Amt1folOyLU4lr3atJiX91buyKuHFPYvHPxxeU6064ffr4ttDBoMJgSzn8OQ-EQMPoxJgLagVdkjaHSU2d3rDV9N36saam_DJHUXUIE3YkMbt5GjJul2wGo83cnNfKlWwW0ShUhdSYWWRGWDWZAe-Ew6kSQi87MWGzoNl8trzkhv-JuHHAAaWhGxleLZ-3p5s2n9p9hQPGv1im7aT2tREyAK6bPjaz8eYims5A-9W2g-KxGhrQz_e3O1Svm5T4_fcakzRPgsTRCl7I7CGGptKiFKgWA09rxWObVRBpdab6uhvrgfT3Xdh9QD9w3yFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7de78bd0d8.mp4?token=C8WNryPMahWxRfhnB2wyDGZ4Amt1folOyLU4lr3atJiX91buyKuHFPYvHPxxeU6064ffr4ttDBoMJgSzn8OQ-EQMPoxJgLagVdkjaHSU2d3rDV9N36saam_DJHUXUIE3YkMbt5GjJul2wGo83cnNfKlWwW0ShUhdSYWWRGWDWZAe-Ew6kSQi87MWGzoNl8trzkhv-JuHHAAaWhGxleLZ-3p5s2n9p9hQPGv1im7aT2tREyAK6bPjaz8eYims5A-9W2g-KxGhrQz_e3O1Svm5T4_fcakzRPgsTRCl7I7CGGptKiFKgWA09rxWObVRBpdab6uhvrgfT3Xdh9QD9w3yFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
روحیه ستودنی حمید علیدوستی عزیز در مبارزه با بیماری سرطان
👍
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/99917" target="_blank">📅 13:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99916">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E35c1MilQwzBq7K4IkdOYh6ZNibXP6a0PVf77Zu_2C1HZUc9zYMtX59ayAt_R7eGKqOESvjU3i-tSl_tjD8HL1NiZD9UImxvCnqEzv1X-jIA3qdoVl2hqE1y4_VJBOW-JoiSy5xIGfe4t-CPZOHUKlKowbKLpn9XCeHggqN8KcXY_H3R_sj8jxtPIi_lND7xH6pGZcPjWFGhLdTeUtMdDe01U3xkgusddffN0nlCwEJWvGSt-eV-kVRfUxYGvqNYQCr5LY5-fjzPTs68FJzPX5vlNSGZOneBdlzjhopAq9wtSAVRT8BsrWkXpnXUFEu7CMUbKf98ZJnA8tK3ZoRDfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
#فوری از رومانو: رئال‌مادرید درحال مذاکره برای تمدید قرارداد یک بازیکن بسیار مهم و حیاتی است که این بازیکن وینیسیوس و شوامنی نیستند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/99916" target="_blank">📅 12:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99914">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b696c11339.mp4?token=J_fN7Zc36M4ZkhArVdiw-2DEQEnoVGz1b5v1FXi3-K0F86GujowF_V2eU8rim2XE0yAdc-GIDUHx1YFp4Kg_3h7a-0FfHja38R_YFw_mteh3XTXUAQLLp5YD7CWD6SFews3qcLIU7PSMfa8xymeUpkeGIxK7e18gO3ns1hfpZBt4fVXB40ODnWPr2FVI5jKVzaP4OPw751PZPOtOL5uhOURsMUSB3MDWiT3qqmNma36Sj7Lp3Kh5-kpMoIqU9M_mWzvPm1LEFJrvOiACFtvdYA9WRGVZt_2yUU2vRDMAk2vwt3LR5e3E5vhJif_4tOHAEhSCwOqGhSADUDWBTyKwgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b696c11339.mp4?token=J_fN7Zc36M4ZkhArVdiw-2DEQEnoVGz1b5v1FXi3-K0F86GujowF_V2eU8rim2XE0yAdc-GIDUHx1YFp4Kg_3h7a-0FfHja38R_YFw_mteh3XTXUAQLLp5YD7CWD6SFews3qcLIU7PSMfa8xymeUpkeGIxK7e18gO3ns1hfpZBt4fVXB40ODnWPr2FVI5jKVzaP4OPw751PZPOtOL5uhOURsMUSB3MDWiT3qqmNma36Sj7Lp3Kh5-kpMoIqU9M_mWzvPm1LEFJrvOiACFtvdYA9WRGVZt_2yUU2vRDMAk2vwt3LR5e3E5vhJif_4tOHAEhSCwOqGhSADUDWBTyKwgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
آتش‌زدن پیراهن لیونل‌مسی در مصر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/99914" target="_blank">📅 12:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99913">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb9971900e.mp4?token=BZbRxAB8JXHJXLuTtQYK7WudCXDw7sGrx1Y8kr-pYdpHuT5wh1sfVGmBGbYfS6DU8W4bmRByBZLdZvXHOE16P8pMZXU0e4VLQd-aTl_B_KCZzoIxCyxOczKccqJCKC6mAxtIfAOSDo8OiI5eFDLZI8nDCwI-iAXlZqNVSCLefWj02_O6UdSbhFvEvvFerqroSifcGRaIPZYlQwPRl-997lFGJ6z_Y-UFkshI32Mx546hXupiZfROe3yQvtOQo4DI5QiEILC9AqVhS-SAYD9qdc9AWxCaJAxbHb9m8x4yCltZDX6MLP6d7nkSSYEAF3DkT8MXkYBrZ_dnTFXczOmm5YY6vzt4a5sTQkVEkHNKkDFTgtXh8F7Se7nQZjsMLbuJfOXWH1n_SdtzSZV9-nu-HcvCHDaT7w9VtPNyV6eKMoPP14HTlnpaHaL6j1C75aNvVk0OgC2Xcj1nre1cGA6Fh3a9kzsuI4ct5ohSvN6UjjSx6SwNes2U0ieMqvrh8bU5wgYjZWLZVZqU0D8glzEX5ISPBTpEAdtNqYhqwKSWdOyV7IhrjxTeKyPrl9FjRTCRD5-Ea96bQl20Jh8-bsLQmI5yfBMAiHovyPKrEwcwxXY6EEYX7Q339rwRe_HytFJATTBggw3uZPaENtFql8nv1G_v6U3K_XbAbyofwqotWyM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb9971900e.mp4?token=BZbRxAB8JXHJXLuTtQYK7WudCXDw7sGrx1Y8kr-pYdpHuT5wh1sfVGmBGbYfS6DU8W4bmRByBZLdZvXHOE16P8pMZXU0e4VLQd-aTl_B_KCZzoIxCyxOczKccqJCKC6mAxtIfAOSDo8OiI5eFDLZI8nDCwI-iAXlZqNVSCLefWj02_O6UdSbhFvEvvFerqroSifcGRaIPZYlQwPRl-997lFGJ6z_Y-UFkshI32Mx546hXupiZfROe3yQvtOQo4DI5QiEILC9AqVhS-SAYD9qdc9AWxCaJAxbHb9m8x4yCltZDX6MLP6d7nkSSYEAF3DkT8MXkYBrZ_dnTFXczOmm5YY6vzt4a5sTQkVEkHNKkDFTgtXh8F7Se7nQZjsMLbuJfOXWH1n_SdtzSZV9-nu-HcvCHDaT7w9VtPNyV6eKMoPP14HTlnpaHaL6j1C75aNvVk0OgC2Xcj1nre1cGA6Fh3a9kzsuI4ct5ohSvN6UjjSx6SwNes2U0ieMqvrh8bU5wgYjZWLZVZqU0D8glzEX5ISPBTpEAdtNqYhqwKSWdOyV7IhrjxTeKyPrl9FjRTCRD5-Ea96bQl20Jh8-bsLQmI5yfBMAiHovyPKrEwcwxXY6EEYX7Q339rwRe_HytFJATTBggw3uZPaENtFql8nv1G_v6U3K_XbAbyofwqotWyM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببینید و بشنوید از سرود زیبای بازیکنان تیم ملی آرژانتین در رختکن پس از صعود به نیمه نهایی جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/99913" target="_blank">📅 12:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99912">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
❌
🔴
مدیریت بانک‌شهر بدنبال ایجاد تغییراتی در بدنه مدیریتی باشگاه پرسپولیس است و اگر اتفاق خاصی رخ ندهد احتمالا پیمان حدادی بزودی از مدیرعاملی سرخپوشان جدا خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/99912" target="_blank">📅 12:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99911">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYq0C2JJLZbhl6nAdRV9AuMc7iRCxqv4FMVhG-gHqamd2k1egnGg0_L92xlLLFZ5EwE4sISxuNgFLDV7ztee041D3k7nxnYVUCsX_nzdsvEE0GWpcVLjncnTqPqlbRW3_dc9N4VU6Q1tExCrrMRyyIbtngTEScyLZGUKH1p0fQrSkBS1zFIYgnNPN0FnbZ4e4IVhttNRh4ObZug9pE3DGfClYI1nTdT4h_oSmazFW04HJwz-lavZpT3-F8GJdwfn9F-eMRBz9kaMTTuMgNd9LY2hMJrPAX_sJipnAglE53aRfi5V2epyFOTF2TPKbrNfc4WJVswK5KnlpHB1Z3P7sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
👀
مسیر جدید فن‌های کریستیانو رونالدو :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/99911" target="_blank">📅 12:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99910">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOlBIXjDHxngUmz-Usv_aKtBao7MlmpwOzC4PmIu4C_DoT1Pt7hUl1hKDrXrkMaGb_oZrUAEVSHrsbXOKJayt0KiTOknkC7knJUQQaK95aaoty2kGLpf5utSPoawnwNfSaF5YVhi3FuwyIIhgDIjoxgHbRPmUGGVQ_b8C7wmAEz6F5HhOt3FAFW1o3c3EeHq5O3Bm9TOh4C3-dKIm1eas-vHia4mLB86IKp-ykxL6HtMn0Pryk6_EGpA53EbY3eRVk_RSc-FABQkr8pzPf0hDtuBik2LcleDFbqw79ePivPBm228mE2rcsvn8nVB9WLsxKppK0lx43-SDqt_gTO58g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
🎙
ژوزه‌مورینیو:
«من سال 2003 شروع به کسب جام‌ها کردم و آخرین جامم را در سال 2022 به دست آوردم. این یعنی 20 سال افتخار و قهرمانی. به همین دلیل است که می‌خواهید داستان من را بشنوید. همانطور که می‌دانید، فیلم‌های مستند درباره افرادی ساخته نمی‌شوند که هیچ دستاوردی نداشته باشند.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/99910" target="_blank">📅 11:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99908">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5142dd144e.mp4?token=eZb-OtcScw2zHMx2rEM-Cv1xeAMfzB-puNDT_Cg3UVJUmUnetBUbiB104_NRi024lRY5wtVC2lLedSUEUaHsFj0PPKvKC2DgoZJzp4t-l6tGj5ZlzclSK76deLceXNT3UkvJYd7mV3LIpEr1qx5GuxBksX_1Ox5FKBi-WQBLaI5SrOFI23xSSAR9OTOjGlP2vBKIjVKwQJDQcd_t_ivZgIl7Mkg7A3YuuijybSaRmv_WLJ_6vwrYtLoWEEZsFfiVReuDgdjldgz4QHIXPSydBl1BRRehrkEjOR2_SbD-yFhVZk0O4ZGqF728fxxP4eU2WW29gAru8G-FYhDxksIgVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5142dd144e.mp4?token=eZb-OtcScw2zHMx2rEM-Cv1xeAMfzB-puNDT_Cg3UVJUmUnetBUbiB104_NRi024lRY5wtVC2lLedSUEUaHsFj0PPKvKC2DgoZJzp4t-l6tGj5ZlzclSK76deLceXNT3UkvJYd7mV3LIpEr1qx5GuxBksX_1Ox5FKBi-WQBLaI5SrOFI23xSSAR9OTOjGlP2vBKIjVKwQJDQcd_t_ivZgIl7Mkg7A3YuuijybSaRmv_WLJ_6vwrYtLoWEEZsFfiVReuDgdjldgz4QHIXPSydBl1BRRehrkEjOR2_SbD-yFhVZk0O4ZGqF728fxxP4eU2WW29gAru8G-FYhDxksIgVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
🏆
🇩🇪
سال 2014 درچنین‌روزی؛ آلمان با گل «ماریو گوتزه» در وقت‌های اضافه مقابل آرژانتین به پیروزی رسید و برای چهارمین‌بار فاتح جام جهانی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/99908" target="_blank">📅 11:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99907">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNeQVsFCGTE_IOaTJPe8BRgp9lD0iv5Vzm78rbLPPpnXCYvIBT4OVyI6vgbDec1OaBu194VrgXTKsqlMtLmf1ZVEr1Jd_2-ecfiRgSPYWEizNmLeOfaeRfUQNtOgDwDL7rR6K28qAK30s993UJGIo-sxM2_6aoCwq0Z1goMyERqyd60cSjiyQeG6pQLE2DuIs_MaZLZtWUV_sdFTJXnjWdYzkaZOgoocr_ABpY7ccopJpnzqAC15aXvbtm5hHWgGprWXZSGB1SS0-SWWD5cj--8CMFsSrlHHn7bWU18KE-3uNdjblS-jlSgGZOBSzSK7T7VW7xCYnZDP72JQJMqEZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
لامین یامال بعد از اینکه سال‌ها 18 سالش بود بالاخره امروز 19 سالش شد.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/99907" target="_blank">📅 11:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99906">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/724b974651.mp4?token=ABd-XAgSmzn2O1nLXvcMc_8TSTKf_DrxUMYt1B27euHEKoCkmoowUdJ4e-LtHCUnOq0iD4wn1eSk05eFYD3xDM4RL9zmbKj-SVtKIl7uGQUz3nanUoJo1JXn_lsZ1FYp5M9pEBDgnzkmXyCwLvfdA1R_iBq90VFKEqbSCFAa5tarVV9ym_FGCK3288jG_gqQIhZ_weZmCV6t0mKAlypCif-T_9AC3tpsmdL_ZXvh3tXzffbQfF9njcrJlSXPnsO6aKQBaL3sZg_VXr2haD88gH0MSEC8-YYCjtKKnzEN3jTqAKLz1msDroZhfoxF9XqZpwn7nSgvq1B_TZj3CFNk1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/724b974651.mp4?token=ABd-XAgSmzn2O1nLXvcMc_8TSTKf_DrxUMYt1B27euHEKoCkmoowUdJ4e-LtHCUnOq0iD4wn1eSk05eFYD3xDM4RL9zmbKj-SVtKIl7uGQUz3nanUoJo1JXn_lsZ1FYp5M9pEBDgnzkmXyCwLvfdA1R_iBq90VFKEqbSCFAa5tarVV9ym_FGCK3288jG_gqQIhZ_weZmCV6t0mKAlypCif-T_9AC3tpsmdL_ZXvh3tXzffbQfF9njcrJlSXPnsO6aKQBaL3sZg_VXr2haD88gH0MSEC8-YYCjtKKnzEN3jTqAKLz1msDroZhfoxF9XqZpwn7nSgvq1B_TZj3CFNk1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمو رشید وقتی میخواد از مصدومیت بگه
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/99906" target="_blank">📅 11:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99905">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQLQz7t4rlzAubz99pGUx1XMlZeZmK_DtdzGEj89RQwhVnVlgxEdup7SBIqumsAAncqYESv9-OWsZjzCW3KyWOSRCf1nVV8oXb8vfR3X5ac_4V_MKF7Y5DvgY_lzQcdgyshD7vsqJEAh3gl30ktZHC_up8S0jSmXn6VblWV3u95lrNwj35XCZo-ANHXCbyFestDJd7OrFy9VmDyTuC5debQN9HV6yAFAm9Gi3utMbI904Cbq8C9hjxlCvP0HQ6XB7EHBW_CV4_nhW5dZXt8vCLp1YPQ6jT9nuQuLb0AGU32xHkNTu8N7ybOUQUxSh5bCtluG-NBTZICnjQk2eORC2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🇫🇷
🇪🇸
استوری گاوی قبل بازی با فرانسه:
اونا نمیتونن شکست مون بدن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/99905" target="_blank">📅 11:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99904">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahnvmazHVPX3VIeRs6xyHP8NnC1O47mBFPwKHxn464PgAciB9N-tqJ0NBJixhdU_btwgGb21BK3AY8kAchewtM7NIUoTS_k9QrK5dPA0mOZ2wrVlDZEkL9MNCM0XKZNVHTBIdvDxlp87eZt8UXuHt3LJ0n85L6yKDPpJFI8mzWi0G4DAhvd1v2D90ROfY8epMeQSeoDnK06S87tmo6ZG5dqYYDNPnL--DY8iUh4oa7Elj12paEehhEOY0ch-3hbDIYTNrskDoM7cEJpGZXFQ46pIYUy_nTrweRNdqgBPkdwC2mBdaHkXEH622oRSkIxvB9zGgVcCQEUX5_uCXTSQ2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇳
نیکولو شیرا:
پاتریک ویرا کاندیدای سرمربیگری تیم ملی سنگال است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/99904" target="_blank">📅 10:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99903">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26e42b519e.mp4?token=elBTL3Vns8aQghaiyO7Ktq4g7_OrE-MTL-1cYzLbzp-oL4DVBgNn9gBqvOWdYW6VewvghiG9IY_tHw82jvvA8flOsoe4Zc1V6g_mc7YbFr4Jn_7eaQ3vW-RECnxuvzExBUkcHV0-HZ79UMTDsj58kHXi4YL7RC4FCZ-PM5DqJ7MSo-QcvV5nW4z14IfHoiFQnMTIQ4ZYgRfGH4EI1tUeIdGtP7IOkdXfc1V6Oxi7NcM6Hfudw0IFY8VbSZGG809iKUGecfQn_yP65qkf9YEQneT9QVPwYbMwD20SMcy78GR6quwThCzOp6R6ZrEf3jbuVittGwrW8Vhm4caegrscDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26e42b519e.mp4?token=elBTL3Vns8aQghaiyO7Ktq4g7_OrE-MTL-1cYzLbzp-oL4DVBgNn9gBqvOWdYW6VewvghiG9IY_tHw82jvvA8flOsoe4Zc1V6g_mc7YbFr4Jn_7eaQ3vW-RECnxuvzExBUkcHV0-HZ79UMTDsj58kHXi4YL7RC4FCZ-PM5DqJ7MSo-QcvV5nW4z14IfHoiFQnMTIQ4ZYgRfGH4EI1tUeIdGtP7IOkdXfc1V6Oxi7NcM6Hfudw0IFY8VbSZGG809iKUGecfQn_yP65qkf9YEQneT9QVPwYbMwD20SMcy78GR6quwThCzOp6R6ZrEf3jbuVittGwrW8Vhm4caegrscDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصدومیت لیونل‌مسی در بازی سوئیس از ناحیه چشم که خطر به سرعت رفع شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/99903" target="_blank">📅 10:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99900">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eyz0-HQiR5ITJTj47Wkum4OkjviM65KVqOM147XsN840Brji0Vecmr1CAm7ZIaaVUEWZkqUQDXwDMRgDitBNoa32wilYXeaBQ289hIdI-cPveh2XXe1IJFHRKT53wn1e-_8W400CZPSLFHbut7cizLt6wdBLsH0HOshnyXhFUUB5_JtVZ7aDtcOPmXnSDYAqrB16woRzdKKIs16-VapSAQLOEdPdzmkzINsZzq817sajEzeHG65IDQwhxePx7VkglhppDub7VruO__mAC7g8fgF9Zq0N1Cris1hMA-cjGnlF6BccJTRz399MBHPNdeYG-Nn58FkaOLDlL2scCg1DMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c9F4jbyPOYEo5jEurrtHh0X52lG5g7p14DzSko1gGfUswWq-UO69dpT0ngs6ytlTTADeWlC7GgNAl4ejD6fT53G4ngD0oLu5xBabRNt_jN4HjcXksz0HQmUFtQTgtk7gaekc6ohGFwRkPWo_xwLKsjL_M7hyGgIeorC7M2Tay_nX-zoGlzgCTFpMTkfO-VSClR_gSrem3ItZxZYb4X8Ni7stR49u8U496zNvUWlhHsh6_z9EZ6TCmwK4r0xN5tNng9uS8msbmz0OdOsaJjCE8VvWJL6AXcUAfj6pSF8igxdRBZNkNKg_qGGKXIAOQY_SQuO3rkBpaNZtavXMHaouXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z5SE8mBVHLJe_7Dfk8Cfkqeb8QVmDiTWlriMvrMsBNnzWaZNgixWJGvvB5BiPUpVvY-BjlFqJz1_8_LxesQrScaJNBsfZjRgS6zDxm9UUcnkIEP7bnfN4oGc3nHXhUj-LSsoTRHhORoovoJH8QtC3yOrTRh3CHK5Q2N_8zeMbEcqmGF6IKAP2BILddMkcZ9v_Fzg5wa99SlIkS_XqBYIDzckWpelQhSuWuN9pcEElAWIvwb8EeKle0ZYoTG9MiJgiM2zBie880sR5llIqjcuBh5LfPBJdaSQGqKcwNuPYqW1wSGGFf3dnwHFA6I8QgYQ02gu7LobfkW9hiJRM9MsOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
یک سال پیش در چنین روزی چلسی با برد 3-0 مقابل پاری سن ژرمن برای دومین بار در تاریخ خود قهرمان جام باشگاه های جهان شد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/99900" target="_blank">📅 10:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99899">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7079ceb818.mp4?token=uS56ESUUGgh4l0o710jjXdZATurpj7KaKifDlLM5_lzh0R-SKBkL2qL_QHHqGtVWW-Clgd1qfl8oMJjUfaT4wggN0PLyRqzjZoWofk7u6hu1l814Tf28PLomBWbOE1aioe24ZBpxGJgcnRLKJ4YtP41LoBX_MEaEgkV3W4fgp4-MXAYsgxrFvXPGWUjWtGKgFCTvY1wwuM0GPJUBNq_sH1iqdt4Ug6tcioV6P9dJBE8o87N26NxpmktWRjG4_OKDmuDo3AkqKal2ND82RQjGfkoFwAtaP47rP3kiTXtcEytKZkbLET0oJGSmndn9uAM4fCqS5PhvLuAQMdL_uodaXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7079ceb818.mp4?token=uS56ESUUGgh4l0o710jjXdZATurpj7KaKifDlLM5_lzh0R-SKBkL2qL_QHHqGtVWW-Clgd1qfl8oMJjUfaT4wggN0PLyRqzjZoWofk7u6hu1l814Tf28PLomBWbOE1aioe24ZBpxGJgcnRLKJ4YtP41LoBX_MEaEgkV3W4fgp4-MXAYsgxrFvXPGWUjWtGKgFCTvY1wwuM0GPJUBNq_sH1iqdt4Ug6tcioV6P9dJBE8o87N26NxpmktWRjG4_OKDmuDo3AkqKal2ND82RQjGfkoFwAtaP47rP3kiTXtcEytKZkbLET0oJGSmndn9uAM4fCqS5PhvLuAQMdL_uodaXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
جیدن آدامز؛ روایتی تلخ از درخشش و خودکشی در طول یک جام‌جهانی!
‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/99899" target="_blank">📅 10:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99898">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iuZupoiTs9LC_ONzfnO-xA_Rix5GdAsHJChpVIRjfsKsoq2gDFNSPusyp1tiwy2rQyku-fS6hD0PZCVq1YxMLRk1_yc-8ROXaIIPaVBL_CoTx3eCVDgCFRSgentwo9yLF5dyTFGsvgTeYyzVvjUWGUtWx72rjAxMw_KcbAI4fh8OZQxF8M-UHdwNtE3jQsXdmpP6Y5VTzo5Vt8LXHCZG2lpMadIFIvR_-suDG9665qwq-e1-LHqszdPPfgfglifARK4KsYKszcKJAaPDohWfvEDUg5IT4Kl2z3wN9gL5evYfTmZRC_AcJzWLJhiRuzbJ4EhgfAU7yORm_0s9iP4uJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙️
نيكو ويليامز [
🇪🇸
]: امباپه یک بازیکن فوق‌العاده است، اما ما بهترین بازیکن دنیا را داریم: لامین یامال."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/99898" target="_blank">📅 10:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99897">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2501cb2ee1.mp4?token=DsS-64n7bVd73RjrGSi-m7o6mKEuXm-Qb36UXrdVlUNBHFeq2Vddl8RZvXa5Ql7iE7wCBMttLxMZw6mrDSBxXMcp58CinyNpYfed3xn-TOWrMLbxjs2haY5Br2AxH_Co-EzVesCTLUKIn9drb4hRijzvkp7KEkrK-ZO0rPcq2aaxckO6tZjRy8RDGvd2elUsWxGrrTh5qrM-qlBggW6NA5BHSiPvVYvjKb6hIdTn4bFgwZqCaYNJiBAXGW6gDcE_C3XvF9Nitsi3sQF-MvOvtEzanwwhRgFVr_8-iBibyAGD19YCl8KTTcpeDEqVqEfFkujKtUBxkXQoD-jicS0EFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2501cb2ee1.mp4?token=DsS-64n7bVd73RjrGSi-m7o6mKEuXm-Qb36UXrdVlUNBHFeq2Vddl8RZvXa5Ql7iE7wCBMttLxMZw6mrDSBxXMcp58CinyNpYfed3xn-TOWrMLbxjs2haY5Br2AxH_Co-EzVesCTLUKIn9drb4hRijzvkp7KEkrK-ZO0rPcq2aaxckO6tZjRy8RDGvd2elUsWxGrrTh5qrM-qlBggW6NA5BHSiPvVYvjKb6hIdTn4bFgwZqCaYNJiBAXGW6gDcE_C3XvF9Nitsi3sQF-MvOvtEzanwwhRgFVr_8-iBibyAGD19YCl8KTTcpeDEqVqEfFkujKtUBxkXQoD-jicS0EFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
خیابانی و خداداد عزیزی دیشب نزدیک‌بود وسط برنامه زنده به همدیگه تجاوز کنن که برنامه رو وسطش قطع کردن
😂
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/99897" target="_blank">📅 09:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99896">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f0aac58e8.mp4?token=MFI9qYvAHfq_AyxoqJaE1c5XlfhACcGUpOotvmYRcFVQj_qHVxqCFj269nwmrD6MNUVMEfdKVZbTc61Bm4MtTbXwyEiuHGrhWYvcvfznYbRe1IeRiHCVNMvN9fIhGDxP0FGOcp8qd80rxZH28QdgHoRwXkLQ4sAqmDBOnelBkU9PJZ0MQvXK2yB9nUMw0Oi8XuY-l7CXmhNKc8xdJdq27p2DRYTKRH13Y4GogPO9j-C5wXDKkzAnoC-iK3x0MCgzmzvRcmV_v05U4CC0yAwvuEzJ0nRLMebR8kDG-8DcMlXY976tMyj4AXCfwEjTtxQB0zCnLpsB2A0tKGU63SN4Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f0aac58e8.mp4?token=MFI9qYvAHfq_AyxoqJaE1c5XlfhACcGUpOotvmYRcFVQj_qHVxqCFj269nwmrD6MNUVMEfdKVZbTc61Bm4MtTbXwyEiuHGrhWYvcvfznYbRe1IeRiHCVNMvN9fIhGDxP0FGOcp8qd80rxZH28QdgHoRwXkLQ4sAqmDBOnelBkU9PJZ0MQvXK2yB9nUMw0Oi8XuY-l7CXmhNKc8xdJdq27p2DRYTKRH13Y4GogPO9j-C5wXDKkzAnoC-iK3x0MCgzmzvRcmV_v05U4CC0yAwvuEzJ0nRLMebR8kDG-8DcMlXY976tMyj4AXCfwEjTtxQB0zCnLpsB2A0tKGU63SN4Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
خاطره هاشم بیک‌زاده از احمدی‌نژاد و روحانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/99896" target="_blank">📅 09:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99895">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a56d32af8.mp4?token=piCVvmZybIRhjvv2HAgIDkkGceW91R93TDTLyx_9HG5tPu9dcAg2uluCE5ToTHbG0BolqUKb5cJP0u9umboL5YJpJu-4JGB97f-OszW6RTHLW1ogTFchYJU9WVecfaWBhiShAu98AM-51H0fmqY2XNdJi0JTkfpOduAUTRT8wEtPPBEECc745bTuCNxqqzLKGuQHGUJblJB6aHB5q__rpgQ0EA6S27XByJvvIMUO6tJVJp8wecTRavuRHUnZKUyat37As26BtBD-z-9XystjKYujN9tji9CzcIc8w7dGxSACMn78lI88eRSUVWbWxjckqOqDCy_uzJVxE3F7yvVPzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a56d32af8.mp4?token=piCVvmZybIRhjvv2HAgIDkkGceW91R93TDTLyx_9HG5tPu9dcAg2uluCE5ToTHbG0BolqUKb5cJP0u9umboL5YJpJu-4JGB97f-OszW6RTHLW1ogTFchYJU9WVecfaWBhiShAu98AM-51H0fmqY2XNdJi0JTkfpOduAUTRT8wEtPPBEECc745bTuCNxqqzLKGuQHGUJblJB6aHB5q__rpgQ0EA6S27XByJvvIMUO6tJVJp8wecTRavuRHUnZKUyat37As26BtBD-z-9XystjKYujN9tji9CzcIc8w7dGxSACMn78lI88eRSUVWbWxjckqOqDCy_uzJVxE3F7yvVPzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
🎙
خاطره شنیدنی رضا جاودانی درباره شکیرا
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/99895" target="_blank">📅 09:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99894">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HyhNIu_tvETGUxXQdKoDh07F4ivZCC9GzqV8InDCMsc42eMEPxYNpNiN9aPG4b6Xwzi88C1sVuOzll7CFmkVwSaWK0QJgnb77VTLD6Efo0amtysJOYAG-ivJ2DTztoncl5Ocv3eMGW8WArfu2MY_yXjDpC8_skzR7HHcu1BxeH3HmvEt6b3T7rSedpIr7Sqkrel-ytXxorgCW3TYbkFNYAwZjEfTeITlS6ZeQ_thfWPX4lwpAYmZgGAoRcil1sTbu6gnI6_JY-nctPKFpNFHfoQObstqMdSUKdTpC_x1tkrrky1wFPhLU7frL7AG8msixb-spNT3AdIcQRdGiQ9asA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
🇪🇸
ایوان‌بارتون داور اهل السالوادور بازی اسپانیا و فرانسه را قضاوت خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/99894" target="_blank">📅 08:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99892">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I9ykGQsB3opHWoaXLHx3oEjK2L_LvU7B5jBzuduJR5cy5RHBUEiC6Sh-58aO4xviiiXJlO_106w5LWAbNDiEVX5WvngzdcAfoUnuGdSPuHvgCBytAEs3WkEZYdYDu51Dt9Q4bC1HPBhiJog_6YjqepWeNpdixtqZZs0Z_sGLMugbdtlmnXGrIg3e7PaNSYfVR8uFBrAsUYv3fu2aNawPjEZJsDHkyiFWKnNHoAuynHtgIswnHuPDcAk3ozwVtbdQeDr3wuPAOfz1Fjc79xI6h5Hb-WxPRFtw43iZ_ljz78QLCoXYCKg--Z0rj_qOaKXGZ3HIqWnLxzgTfN4AtHaGPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CLI0sGZIP5DHpvE_sW_TXQNNB5bf1dMvr6_bpgyrYRhzH6ThyFpThHWO3WOyPiz5J2eLkrtr7yZN6cDRnHhtitE1xlKFMQdAYL11FkNYcJQe0aMS3KFvLH6rFCfIvQtOfNJao-FpLhJMv21CC1lJwSgMLRkZGKizXSUrPmaz3jLcBEXClmKk1usIy0sI_io9-u32gI4ubTPYdZ582F9-mQ_xAsuDX1GT-BLBl_RSVKCKBYgxIhZUkFELX8GNaFZ6X4Edt9Iw8EwrhUhjuuRpML5Hqu4cHRcUWpYEXFY6FVBcYlYAE3vkq84U2dUZ4bvrdFJT9TQYeGl0CrvO7ZuuIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست جورجینا در کنار رونالدو با کپشن “Daddy
💘
” که میگه کریس حسابی حالش خوبه، نگرانش نباشید و برید به بگاییای خودتون برسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/Futball180TV/99892" target="_blank">📅 05:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99891">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1MpkHxCuzrwfTG_BpQ_fBb6sB8Xv8u-k1Ue2fAu-LKUmdXd4PnEfoAAOBurYyJmqhsh_IvXTOHCJKiGQBMAnBAm9vtwQjWJanJqiz7xpgGEOpUq9FxVB3tqJabNJiKGxqNxOejVzxehwK8zJJH6oq3CSQVNmgp_tm34Wa_WW2MkSuW70UR94LVpia_KZvTr2KSy4qQQ31bwAXJ1iBGA7xs7j2XjLBhFKFZ8mXmPPVxjPOd1WQ5NRRdqBWugcOn86R7VZbv-KG4Q5T3W8emYhDGMNzo9Iz7wzFEXNbHVFUrBug0qvXQYAMf-pKkN4HyOA9XwxR4gZ8kmEFCIf4ZqNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
#فوری
از بن‌جیکوبز: الاهلی عربستان در ساعات اخیر با ارائه پیشنهادی نجومی به مارسی و دستمزد فوق‌العاده به گرینوود خواستار عقد قرارداد با این بازیکن شده. مذاکرات گرینوود با فنرباغچه پیشرفت خیلی‌خوبی داشته و فقط دلارهای سعودی میتونه این انتقال رو منتفی کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/Futball180TV/99891" target="_blank">📅 02:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99890">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4f230afe8.mp4?token=OPmuzuAp63MhAIxW10_zKYPPq1Im41Ge8qlpsWX0BLFoecMWm2H9-Gob1SnIl__KuMqiFM0SId_15OMOe2wggz_oswgfKpWCNVtZ8LtN1NP_BFLLHm178Zml3GUMIE3dSt5nCW9BUzM1X2UlDEMJ-0aw9gaJOa9q7AT4n6cEcBAW8FH7kNIbbQXuJR6Ux4d2fquh8pjOGUxwXjmNkNOTaXsVyGcEETmNVZR46-CpCJy6srnHTCQZwF-kHmz9gGkwXW7JDVMVHcL6_fCXeIsdxk-IzRYovtm9w1048H_Byz-WOzfVLYEqtjz68f-y5MOEJJmzetCt3Uck78c-bazjyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4f230afe8.mp4?token=OPmuzuAp63MhAIxW10_zKYPPq1Im41Ge8qlpsWX0BLFoecMWm2H9-Gob1SnIl__KuMqiFM0SId_15OMOe2wggz_oswgfKpWCNVtZ8LtN1NP_BFLLHm178Zml3GUMIE3dSt5nCW9BUzM1X2UlDEMJ-0aw9gaJOa9q7AT4n6cEcBAW8FH7kNIbbQXuJR6Ux4d2fquh8pjOGUxwXjmNkNOTaXsVyGcEETmNVZR46-CpCJy6srnHTCQZwF-kHmz9gGkwXW7JDVMVHcL6_fCXeIsdxk-IzRYovtm9w1048H_Byz-WOzfVLYEqtjz68f-y5MOEJJmzetCt3Uck78c-bazjyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🎙
🔵
دختر علیرضا بیرانوند: بابام استقلالیه و دوس داره بره استقلال
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/Futball180TV/99890" target="_blank">📅 01:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99889">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🇪🇸
🎙
خوان لاپورتا: ما تو بارسلونا برای هرکسی دولاپهنا نمیشیم. یه پیشنهادی برای اتلتیکو ارسال شده و هیچگونه تغییری قرار نیست اتفاق بیفته. بزودی می‌بینید که‌پرونده آلوارز به کجا میرسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/Futball180TV/99889" target="_blank">📅 01:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99888">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6_MuqOXpfY33DAfjo5zNjnIXrZkAJ8p8Kh712HkIzH7VdwdJAt-vd44x2qzeAdyXk0m5AP38-s7Uuxs8Hx4Mh_XJEquEBiYjR2hejWEjlKMQWFlYerQWpkQ2rVM60c3mUTGs4LxFP6530qqJTyTLZXBlL-ZvRdmoUOiaSqxzNahLNAWIW4SNysq0B9PZky0Qc_gF5bGDhcwfaMjJGDvr3iSW11Y0BAfifnEcNDzC3_fuwt_WB8Bx5cX3e5MpVhcDCq8q6fwuvqzyOg7MEY_VEISAxEEYIWLuMkIXpaqOyTohANTLs2X5d3FOcxgP2kXdfyZjbBfQ0haVY43k2fotg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوووووری؛ اسپورت: باشگاه بارسلونا حداکثر مبلغ ۱۳۰ میلیون یورو برای جذب آلوارز به باشگاه اتلتیکومادرید پیشنهاد خواهد داد و رقم بیشتری پیشنهاد نمی‌دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/Futball180TV/99888" target="_blank">📅 01:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99887">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0Acijsns4WxkOLd6Fhj8kxHd46Yocc4xjkpKIek8H0yCB4-VKxEUxcF45eFRRuQd_RzDFN-eLrQxCwVuKOp5mmI4LmqsDJOqvXXUnGtzBfJrTv1HhAGw1kjS3ODpZ2CmvLK5xW-6b4HcQgNis5edscKDyZO5_NUyVLyqDwuYsL5pXjrNxpolb9VCxHMG5YdhwxLzpN_fDKYRQJBVDQnVcLFxb_k4e5d7-75dLLqT_esLu30WsoOSJybbNLytQVL3C7qyOOd2sg6Fls-4d1rakInlahUqK_AVost_mAzB1eOQCDOg0QV-an3EIcO5v82CgcjnEnDXD8d9aAu0NqWng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
💪
‏ سوخت‌رسان‌های متعدد در خلیج‌فارس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/Futball180TV/99887" target="_blank">📅 01:08 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99886">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfKeuHeqpE3YnOVqgnSk5NKeIZGe8FEqSXgNCSAEsZJzpni8_R_0whLsYPicSQUS8YZuxYtEJ-u3tqAOLsKycSeRucS0XvxNXAApiBRUazO_QwbXaeYr3PvOMoDEYcCMNnJv_eWNSw3QaDqF79uw8MccL2y9xSk-9b26zKoDpCZ-VuOS0XUazYVVD9M7ZPzuXlX8O2K31JuUYtCOCT9_A6e_ylOTV_5KVUKC5OF7D1NSqFMV6Immkw_NrdpWASfYZYLDbznpHupGCAj7pXCfXOqNRIfD1oCsKZDk6byqrheWKZyXKQBuHaCRHOlcwnvtudyAFq0xp7c23kLE-SlD2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
#فوری
از رومانو: رئال‌مادرید درحال مذاکره برای تمدید قرارداد یک بازیکن بسیار مهم و حیاتی است که این بازیکن وینیسیوس و شوامنی نیستند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/Futball180TV/99886" target="_blank">📅 01:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99885">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FErWYtyi8bZsCU6iNWEMx_uUBjpRrjCDGg6yTpcV5L9wj1UCMTnl31ZnZbgyu2CgK7PCzv-XmUwh-ekr2NMgaUDozWd6VfKcdnuD2wsNYRqK4CDmTtXoClZAuArYxPkHIU7aM_vPaVWhv7lS_XHpGJQxMMEPYwtvBR0eknMD7dkBu9X3bUv973CjEDixsVvlGngKK12Ec7-32xJoiPDro9ut7x82Yls3sY6AJ7fr1BpbSG2Ie9eiF8OA51Art0pNDLmabvg0ni5cvWVsMIWB7jN4CF0RQ7-tQSXmBRlURAzk2xAHx7OlH1wWa5WWZSm8PfeF9F8bmiv88mxPPaHkqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لامین‌یامال با توپ ویژه فینال جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/99885" target="_blank">📅 01:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99884">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abdMW4b_YtumsB6kUuRq9JnvrfUCIr-6Zuccp56HTuUvssTzRZaVdDMRa7ToozIvPI5blJOGA1XRS5TBCjCfHDboacMNO5GmuRxE5-j1YlZNu4a-dJOS490Gpx8hQM0ew-vZVeQ-UZOtqWSKozVwtl6jWM8oYuF6mDcGgXzutAbC7G7g6OJHA6bu8321JFR-pLnO2lzH_-k-_yW9wkdj_tkl2CX-L2Ki54okb_iZVqCHgkP7SDaFlWndIACGmkxnwvz8ciC8uYuEkH3nB2pyWHSd_VMf7RckkFnQMsCIvIYTOYbpk7kP2smXUGmrQCgFDtN3ZuXZ5GoK55Oj5W0ezg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
سنتکام-حمله به جنوب ایران آغاز شد
ساعت ۵ بعد از ظهر امروز به وقت شرق آمریکا، نیروهای فرماندهی مرکزی ایالات متحده حملات بیشتری را علیه ایران آغاز کردند تا به تضعیف توانایی آنها در حمله به دریانوردان غیرنظامی و کشتی‌های تجاری که آزادانه از تنگه هرمز عبور می‌کنند، ادامه دهند. فرمانده کل قوا دستور این حملات را برای پاسخگو کردن نیروهای ایرانی صادر کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/99884" target="_blank">📅 00:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99883">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
💪
انفجارهای متعدد در سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/99883" target="_blank">📅 00:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99882">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
💪
چندیدن انفجار‌های شدید و پیاپی در مناطقی از بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/Futball180TV/99882" target="_blank">📅 00:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99881">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
💪
#فوووووری؛ شنیده شدن صدای انفجار در مناطقی از استان هرمزگان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/Futball180TV/99881" target="_blank">📅 00:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99880">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YZS0DOKpvbReXKkwMtvhZJT7Mk7wcEp3QDUW_L8A5acdqsqQG1O0jJ6NCRQDjgUxWv7_7btKElqcblkYGOpk0wAPu773uqOLtb0t32JojZK8f-hfOsvJBLfQY2yDwzEg8g4evEEDBKldK0ZDN1VaZuTRHnc5Y_6GVvoEK4FXoWs3HOHO7EEKLYOBmKLIjfHw4LYZpFXzUvce-V_G2CdzN4Wt0W7iolhQkuOEXAUjI55AkNdpeTMLDWRBgDe3wWMPk0A82iJhz7y3Jz0KQ1qu-QchHdfD2wwuVysE6AKxXnoWbv9aDH5VdZXEF7jhFbHcqVc9jRwZppffnCRLa96b9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⭕️
💪
پرواز سه سوخت‌رسان از فرودگاه بن‌گوریون اسرائیل به سمت(احتمالا) خلیج‌فارسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/99880" target="_blank">📅 00:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99879">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
💪
#فوووووری
؛ شنیده شدن صدای انفجار در مناطقی از استان هرمزگان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/99879" target="_blank">📅 00:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99878">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab9b193566.mp4?token=fb5unuekUiRE6MLeQP2t0hsAmDjpwuH6sIPGyvumck7nz6w4XNarg6LzxNhgiC8JVCdJ-Gap6_cEmeoZxo3Ta-F1Gk9vU1JMuxWjUAy0JBtv6l3asoenl2A4X_9JVvDJs3TP2j_fda1ny8DLJ0VNKXPvDUeIhozrfa2KdZrsigNgW_o5gXRMz9zp0fFlfYic1AoeS1XILI6HSC8jisu-iMdAPdVd7SeM21gwEWJP_CPp5oNkzbOKJo1b_47HYOj4XWjaxvQpvjflJY6PQZNtot7-wIZQaR6Em5meUNeeN_VRYdel7hEiBGcuwlNuSSHpApJKZJGJmfwA2sLLlxSv7nTr1tgCSW4w0Sz6MvOyvKM_p16WLK_AhGnX2oDU-4hGWX-VJRzOH8vHy9FJ9RTOPLDdaR_MQKE0FvCVWvJZwA_JlGNrFEHiFzTpYcHemswOp2uBDYE83u7GmnmPzBwC5zjkTwN7nsRRvbWZmsNnWJoWFNG95SHM__BQzib5XkNNa6Hk0HoLTWNF53O2dIGKRZ3Ix8Q1ceY7iU95jE1RH0IJW0I54juYZJao4mgozNY6w-E4JAUALZC57DLgjXzJ-a09YOM38IeUNPiOzyInQ3CnOhGx3cYt6hMXK5kKkHHGRTkVKa86-Pxun0deY8f02V0lUYHNW7H6CxPwREtQhVY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab9b193566.mp4?token=fb5unuekUiRE6MLeQP2t0hsAmDjpwuH6sIPGyvumck7nz6w4XNarg6LzxNhgiC8JVCdJ-Gap6_cEmeoZxo3Ta-F1Gk9vU1JMuxWjUAy0JBtv6l3asoenl2A4X_9JVvDJs3TP2j_fda1ny8DLJ0VNKXPvDUeIhozrfa2KdZrsigNgW_o5gXRMz9zp0fFlfYic1AoeS1XILI6HSC8jisu-iMdAPdVd7SeM21gwEWJP_CPp5oNkzbOKJo1b_47HYOj4XWjaxvQpvjflJY6PQZNtot7-wIZQaR6Em5meUNeeN_VRYdel7hEiBGcuwlNuSSHpApJKZJGJmfwA2sLLlxSv7nTr1tgCSW4w0Sz6MvOyvKM_p16WLK_AhGnX2oDU-4hGWX-VJRzOH8vHy9FJ9RTOPLDdaR_MQKE0FvCVWvJZwA_JlGNrFEHiFzTpYcHemswOp2uBDYE83u7GmnmPzBwC5zjkTwN7nsRRvbWZmsNnWJoWFNG95SHM__BQzib5XkNNa6Hk0HoLTWNF53O2dIGKRZ3Ix8Q1ceY7iU95jE1RH0IJW0I54juYZJao4mgozNY6w-E4JAUALZC57DLgjXzJ-a09YOM38IeUNPiOzyInQ3CnOhGx3cYt6hMXK5kKkHHGRTkVKa86-Pxun0deY8f02V0lUYHNW7H6CxPwREtQhVY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
بیرانوند: این نیوزیلند بود که ما را دست کم گرفت و می‌گفت کشور جنگ‌زده هستیم تا بتواند ما را راحت ببرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/99878" target="_blank">📅 00:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99877">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6782dde8a.mp4?token=fPUnqo6z7PokoXT-yIWsKHmQxRQQtyNJ0Aeopp0YUW9a81g5GLkFmMl4GQ4bAwoY2ypd94Ds1d_OvipORoFqXLosMdpH2zCYnhzsM7Br-1Vnw0KXRWU79P8U9VKqZjjl8uCv_iNcD9tB-o4eQTADmDM7RAj8VTSciNpKxQCaczc1hU-hIFhg-KyPyfJsiURk9rQvPlG_kqALwX7PbdlBstIbyh1KDJoiPw6OgOVbfQLOs0RgNoqEAhc-zzT9ryJQ3c8mvnIucQOfDIAH2NeeWkZLPkLKaYpceMiZ3u0FWzLlIFRJDB-M0_0O-1YFr0HAkwn2ewOHGYhXv_NkcIb9kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6782dde8a.mp4?token=fPUnqo6z7PokoXT-yIWsKHmQxRQQtyNJ0Aeopp0YUW9a81g5GLkFmMl4GQ4bAwoY2ypd94Ds1d_OvipORoFqXLosMdpH2zCYnhzsM7Br-1Vnw0KXRWU79P8U9VKqZjjl8uCv_iNcD9tB-o4eQTADmDM7RAj8VTSciNpKxQCaczc1hU-hIFhg-KyPyfJsiURk9rQvPlG_kqALwX7PbdlBstIbyh1KDJoiPw6OgOVbfQLOs0RgNoqEAhc-zzT9ryJQ3c8mvnIucQOfDIAH2NeeWkZLPkLKaYpceMiZ3u0FWzLlIFRJDB-M0_0O-1YFr0HAkwn2ewOHGYhXv_NkcIb9kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😆
😆
بیرانوند: آخرین بازی دوستانه ما پیش از دیدار با نیوزیلند، با کارمندان کمپ تیخوانا بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/99877" target="_blank">📅 00:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99876">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b76e61623.mp4?token=pZ0uC6AHrb4CBhepSWm5zG38ebcA8DSA6Qnzac0dILPI5oMfzvZegGC8gWU2XywJwfeYIv9mWxQxBV_mxG9oobc3WKOVEa-irili6YjvCEk9__udElATOXUe0XlFdzSq6NTj4J5z_jMfs7A3KWxW3Z-S65A6t9IGowt4nT-mrvXY_PVOfrc66TOFlkYXuunXn1_UwPPIkE1rNqIV3Wcx9J0w4b77nT0oqiV-sOofKH8WJGFekicQf1nuk4sVDjcXMPTH-CApbjRKA4Xvg1dRkPaFBPNp_a8KMGaqjEtdxDbzUIwj-i9jxfKor247lDzHJdfnnp2se9t0Z7crQFVlKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b76e61623.mp4?token=pZ0uC6AHrb4CBhepSWm5zG38ebcA8DSA6Qnzac0dILPI5oMfzvZegGC8gWU2XywJwfeYIv9mWxQxBV_mxG9oobc3WKOVEa-irili6YjvCEk9__udElATOXUe0XlFdzSq6NTj4J5z_jMfs7A3KWxW3Z-S65A6t9IGowt4nT-mrvXY_PVOfrc66TOFlkYXuunXn1_UwPPIkE1rNqIV3Wcx9J0w4b77nT0oqiV-sOofKH8WJGFekicQf1nuk4sVDjcXMPTH-CApbjRKA4Xvg1dRkPaFBPNp_a8KMGaqjEtdxDbzUIwj-i9jxfKor247lDzHJdfnnp2se9t0Z7crQFVlKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مجری شبکه سه خطاب به بیرانوند و اعضای تیم‌منتخب فوتبال‌ایران:
از ته قلبم بهتون خسته نباشید میگم
در ادامه رو به دوربین:
به زحمت این بچه ها باید احترام بگذاریم
😐
😐
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/99876" target="_blank">📅 00:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99875">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7990a07676.mp4?token=qhFWZf4vgvUdyWyt7vLh1dXdxs4L9vvvsNah9361qem2SO5UbVmVQv0dzNYHFLzAyh__8yjVyii73vay8gaLPtnqQN0hB4WU3NR40sZPHUmgZ4wyUmoe6p2Xiu9GCLIAqnRdh1i83AEDSBjrapjiusQNBPQbTyvRH6u1Rltft-BESW1kCsWqBpAmoeP2nDmQo8ioEm1BXxT9YuuN0Lin4ak0Asi19o7cCAKaOH83rMUFXKLhcpTWuX45QnzUrSIRonYofUaFBRh9MU64JgSRYeyGQl_EIYJXMJlN7GiNF7yA8UIXEdjgU9k1cImTdBCYIqAoZJgunOsjDG7__oqBAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7990a07676.mp4?token=qhFWZf4vgvUdyWyt7vLh1dXdxs4L9vvvsNah9361qem2SO5UbVmVQv0dzNYHFLzAyh__8yjVyii73vay8gaLPtnqQN0hB4WU3NR40sZPHUmgZ4wyUmoe6p2Xiu9GCLIAqnRdh1i83AEDSBjrapjiusQNBPQbTyvRH6u1Rltft-BESW1kCsWqBpAmoeP2nDmQo8ioEm1BXxT9YuuN0Lin4ak0Asi19o7cCAKaOH83rMUFXKLhcpTWuX45QnzUrSIRonYofUaFBRh9MU64JgSRYeyGQl_EIYJXMJlN7GiNF7yA8UIXEdjgU9k1cImTdBCYIqAoZJgunOsjDG7__oqBAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
علیرضا بیرانوند: هرکسی جای قلعه نویی بود و با این نتایج برمی‌گشت، مجسه او را می ساختیم. خیلی از کارشناسان خارجی گفتند که باید مجسه بازیکنان ایرانی را بسازید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/99875" target="_blank">📅 00:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99874">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZZOjlhTZJZ34prTCP1EJG63AFvM04Zy_dOKlYHMoZDVWmU6HrP8nQ1C2lpMjgU67xOQuKe_55UEWmZREIH9rOShhujHZ5cSRgTMsJMa2V3EhSaAUiUlgwGoR7AdRj3Wsiu1lIQa8wwJ4-Zwga0HEyc0GIHKG2HNy_Nr-YxWj3Ei7sHOwS4994gPeR-KlqD-P81M39sLU4KqH8ZFeExN3-9daftk1vYMVzjAdAQLAOq6h0aiDzSCxUvjzmxJKZ5htg62UMWdLTZLeqFWODKN1AMevwL7bnIuVn9MSdLnWRLsHzLmdltXExkPeWdgEA06rOzirn0OdBgg-5o6EGnSig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
#فوووووری
از موندو: بارسلونا در صورت جدایی فران‌تورس و عدم موفقیت در جذب خولیان آلوارز به سراغ پدرو نتو ستاره چلسی میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/99874" target="_blank">📅 00:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99873">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6FZ2qp_-CN1BPfQOo_1nQ_etZrWTjM2gXH4cS0PttMts9U-spun1DvvQdRZpTxk2YrwZYM3C7wQc5gT5X_qbHZbM9IDdd0nscItMulMHF17c30UEUp9V4E2N_Mhbgsj9WsrnukZtGstrxFA4LVl9B0jW5AALluXA5eCCWzUwNxunFiBqwXY9DJq0gLVVpJ0oWgVdncGw7lIruW8cpDPmh5TGEvx8t2efS7P4vW9f81AZ33r5b1Tpur3JXrfyJJ46v3p2X20uhYyxTwunRmkIlEy9NdeidxWZr-j5Gr1dvvFHsk6dMIGmqlUgEmlUxhws-tCn8ZKjIks5A1abVM2ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
جود بلینگهام با توپ ویژه فینال جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/99873" target="_blank">📅 00:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99872">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
‼️
🎙
بیرانوند: ما بدون باخت به ایران برگشتیم و این برای مردم ما یک افتخار است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/99872" target="_blank">📅 00:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99871">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/99871" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👌🏼
تنها
#سایت
با بونوس های واقعی
😮
به ازای هر 1,000,000 تومان واریز بهتون 1,200,000 تومان شارژ میده
💰
✅
نصب اپلیکیشن بدون فیلتر
🚫</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/99871" target="_blank">📅 00:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99870">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFUGvemmUMCjY4o8OO0aGNeXFYYZxeJKk5QQ4V8QrgJaFfEOuiqWqmOl9sxkI-QGcF0vagqweVBtcqIEFSXePfVmVzMr35IrE2mQHnS7jXXjf1-PpZfLjay4OT1ZfygQVsAogE-zXreYZ7EQ-Cm9SnSb_a7iNkverZE7TmRNJkjulXXtq9_8TSucOOPYIbksIht9QeAGT4ulIAuVzWZhjXnmqWdHXssZ__e-afTV8nngyhkdqtIiS9hCGEzgaYm5lEoD7p2h5UmMIoNgdnLBhL1acvGqQN0YR69q5f1pNcNHYm1zydUeIDzWB3gmKp6uTa6NVxzrcaPn8djjllihMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
هر
1,000,000
شارژ مساوی با 1,200,000 شارژ در سایت بدون قیدو شرط
💖
💵
هر بار حسابتو شارژ کنی
0️⃣
2️⃣
🅰️
شارژ اضافی میگیری بدون محدودیت
🔴
اگر هم باخت بدی همون لحظه
0️⃣
2️⃣
درصد  مبلغ باخت به حسابت برمیگرده.
⌛
همه بونوس ها بی قیدوشرطن:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
a22
@betinjabet</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/99870" target="_blank">📅 00:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99868">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2XecaMBonUOWxHnwy8HlEq7jyS8UB9x_4tMxQxJgABvBnDcmIn-iQuGy1hIFXviihs8fwtDruOiNyyNyeh0vrUH60G1-PyhhJFl77laoQBOVLBd9NF-t3Jp8w5DhyF8O0BpcXRouGOg3RHDsqeJbIjSRyRt6v0P8L3TbQ9dSD9YBJ4YXOyODpji3Q3AV9mE698jqcq6KwMzo7mL63FassQbwHncHiwAtASbGu8QJ1CwQ_8H9CpJqviWVnqPycd1203vjtROU_1wPQbSKUWwG0QnsiPokUDYjG99mhGNKfkFHavsIZXdbeQVOJWfV-pM2s7paJyAdB4Q6OcQPLVM_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#فوووووری
؛ باشگاه لاشخور اینتر درحال مذاکره با جان‌استونز برای جذب رایگان این مدافع مستحکم تیم‌ملی انگلیس است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/99868" target="_blank">📅 00:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99867">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
⭕️
🤩
باشگاه نساجی مازندران موفق به هایجک کسری‌طاهری از پرسپولیس شد تا حضور این ستاره جوان در جمع شاگردان مهدی تارتار منتفی شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/99867" target="_blank">📅 00:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99866">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ow36-Ri_YbJotVcWG2HKhOiO5RMDha8pv5WLocFSedS7ncr_UEsFLyVZQzwfQB73WpKqsiFTR6AnRH2jXWAhzRflCNpMxomjyWnp8f6XD51hu-h-x20mQ8mS3WaPqQ_KQ1E1xyb71hc5Vl277MBCBPPesH3g3RaAcUci2h118Ph3_M3DYyShyrfizr8_0RNqGNjBtS8A92q4VUIr1zeNZj0Oy2y5hXweuVmX8Z4RTWTQhCen4EHEteD1vhak0-xUh22SQsqUoBBgV1FUwrEjn4VqfF7a5uKRffP2jt-aiFXGQaew7Yu_3tNYLrqrdSX0rUHyGlgJ5JRDLlWBWNMvHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری
از فلوریان پلتنبرگ: یوهان مانزامبی ستاره ۲۰ ساله فرایبورگ پس از درخشش در جام‌جهانی با تیم‌ملی سوئیس به استون‌ویلا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/99866" target="_blank">📅 23:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99865">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fDXGpgnjd9LGYPgRIAZbPFgcyz5yGohpSB5gwOQeknH87-cw0MxDRlblqUK2b3q0icaQJ5qal0geO6Ce56RkHl25dsgJgtH_-L1rx9CT77JPtJUPE0AO-t8e1uJ3SRD-_P0qMs8kGIHm7vg4uQDErFLB_cLeJKrKIaKJ7LB8EBGdm06D4UF89Yo-KVeUt0VcaZPWo07ju7yv2nIlxeY1WooDh4s6AXe2Nta9YoHL0bT0x3Ax90pXzKZ19NXOknhZIHoomFlloaN8scRz9vqSUxdpkl5v13wzJnKp7OvhRZ84WIX-V6QOi1TaJvweAv6NvXHT2dT6-Zo1dZVdS_9qnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇧🇪
#فوری
از رومانو: یان سومر گلر فصل قبل اینتر به کلوب بروژ بلژیک HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/99865" target="_blank">📅 23:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99864">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODl_BjU4H9tEmnu2HDwo2ZzYWRJX9LvOnBaiX5Ze7b-yZF1XDF3U-OgSC54FV7URC_Thzo6cZ1zJPbDcZ42-kHFIVzSLCUeOiuBcR1UbuiOJtQpkOGrUEiLyA6M9Ij3CExpVU6XgUzxVtzsW1uM_n4UbFOqQFuYeObZMzzVPxjvuhcDoMBaCfUVFSwyHiwznTYM7qAMXZ19QCxjtiUkG5hunH6TRpFn5xO2T_oTgLIMgKOeXekIBnY9Zc1jh5PnnqP2GVjsbLwQwotsQFDpuuiOV2USQrZNs2Ct-ppkKd9ra7t4SO3671X3uci2-DbmDqx7B4N7MIZCtOeNRG02KMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانو هم دیشب تماشاگر ویژه بازی آرژانتین بوده
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/99864" target="_blank">📅 23:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99863">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRBk1q0Mlx3-YaTia4cm6qQdvyKTv6NCeOthSP_0MuBAjhGXGHNxzR1FqzwcCuNsrUMITOJyx6ZZN9R2qi4557RhzCeoT6Seg0HI5Wjk-_9HE_uTNdMkEtRIYQnvADlhV-ANKjahGN7SgzTp3FXbm-9bcP3-4dmMfqI4dR3hONIjgyH0rWIWeHaIp98_nLlrm1z1up4o49Y59H2Dh1OR2Lrh4sKoD3Y8QbQcO0pFNOHcX7vE893hhg_LrlCMcQg1e1KzxjVhPvv6CEIf5apWBtPKm3LKndRBWe5UXqxpSRlBQQdBtR7No_dBapAoFIDqz3vlBnJ7qqUymOCG46rJlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلوارز و دختر کوچولوش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/99863" target="_blank">📅 23:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99862">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mxjqsbew1HZkMa1rtku_7svR3UEFE8qXDjZxJGo-YrOS3TNo4EVrrFvlqSjJSIpidJY0GAM2u1DVmb9754pLpAJFZZXb23nLbHaj-N_BB7jwf6hpzSjchRDQ5mqTbfhgBaVmemKwkINXV9uUrTOUIvvigD3W8Je7xCwemEPLrll9TF9TspBM5G_xDzJ2HLL_wmdTTyHRMVJxPi0rvcnzEswnQyF3mzPpijFN_2du6vqMHxcXL2bjSDKogfuWV4KgTMiQKfRtUyhHYyJ01JDQmZdZqJd8UzSWXhHwsGlH7Hte42tC2aVZUfHrlymHgWWAkziEgu59PL0t_FJEoPmBYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دیگو فورلان ، سرمربی جدید تیم ملی اروگوئه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/99862" target="_blank">📅 22:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99861">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCc-V9Pj_unT8-ZR0gMNS8RpB5EfUuPuIv9gYI6r8PAXbHfGCTJpAhpsD4HvQoEnVsszbIUlPIatZzpuEa2eBwoaYBbEwhPyWEvApcpKYVzrBx1EtlOM0KH9gQ0-5sT5XNVcpCZYZN2Q3EuS4L0EM5jGsqFqxomLkNodMfxciyonVZsTNgAa2c57yEOGYqisdXdrNwsgWocKP883Hoj6uJBTSGZ9awefOTcQX36X3GlU1mIdVlBGLxpeerkiZz2iqhngmJ3o9-vCVwnWHPc15GJ9K07wptywzoFXISCvYVTiiDDAWfbQY7gc0viRLkVsoKdZkZcXnlRp9bdqB87izg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
کیت دوتیم اسپانیا و فرانسه مقابل هم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/99861" target="_blank">📅 22:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99860">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NO7D3budzRWmABO_GIp_GAF2jYRsf07lFOEbMj43OP36CrfNZi1hXGYT3XwACOUgcE8yFElNK22m-2raHajmmh7HneIjjfC41DYddLchpClVxwcOt8EXB-sM1amcaa0fbOerHaZ0vx-O9aALJpYz2LsoFxDdC-WzQLbpY6748FAWb0lPUGnH-dRNLrwgGXgOUNGmx96YA6NzGkq9yP_abwgxOcah6BLKCB71Mf1NKQb-w5VNsMf51yauTSLAXyhyB7MpXRjU3EW1uboZdTt3jxebnorxQa352eKAcwZtHNU2hQ78fjf75iXmbhsvAc97cTCZDp-XozWsJKTlqAd-Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
کیت دوتیم اسپانیا و فرانسه مقابل هم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/99860" target="_blank">📅 22:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99859">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUXOGyHJP0GC9lC3qDFqlPS-dehpXNhZDm7Ld2tOcpxbfmyLsQqokns3wkRKAaiHiDLPEllIqhAHfK5P-jtee7MFPjLpNtzzhmndzX6xVcbG6I1AZ_WYAyyfIx6Nk3GJfnlQRSSh971uNk0yzXRI_R-7FQnoR1scij3_GTeH80IadhaDIAvRXW3MBPNKad3xS9F6wlmZJUO-KinqAQdZwQReG86rsGeOz6G7dJeEm0NxVmEY1FFZtS-St6UWodbQapMblwlivnduj5W3djEKr9Cw6mzNmsVJ-YWRj43wu2VaN3kBOKXCtGTMqndJ61Rl1OCJrVgRJOzGjiFXtvDydg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دلا فوئنته:
هنوز لامین واقعی را در جام جهانی ندیده‌اید، فقط منتظر بمانید تا طوفانی که ایجاد خواهد کرد را ببینید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/99859" target="_blank">📅 22:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99858">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRtHl0oIdKP88rkiEYi5VvmMsINIZ6SSOa02jzl3pojBtE4mOIuYbG0sDgrHEhCQAQdDLhBNSo0U8EoIN_ZdvbNzakTR30ykqcHOgEn9IZsEA0Ws45a64IeV-j4orCUfQ8c3yfhvYwLj0FOH56lFae9snvDv747UWCvAs6noJdh1x1igZOAglloS8iLq3UQivtzgkzueFQvahBdsNCHGtDNWUwZjWrQ11Bn7mDwn9LaFc2nccXUOJw910aQt6G437lA5mjuBhl9PGrSH7fhEixyysjF_aHOPHgG0bgeaLYNp1rVrOka9boi_dFnoZIsKndVCVUfp4PjSQSN7tIj3Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رئال مادرید معتقد است که اگر انگلیس یا فرانسه قهرمان جام جهانی شوند، توپ طلا باید به جود بلینگهام یا کیلیان امباپه برسد. آنها معتقدند که این می‌تواند شبیه توپ طلای ۲۰۲۵ باشد، زمانی که رودری به دلیل یورو آن را از وینیسیوس جونیور پیشاپیش گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/99858" target="_blank">📅 21:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99857">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
رومانو: آدیمی چهارشنبه در بارسلونا خواهد بود. سپس تست‌های پزشکی و امضای قرارداد، همه ظرف 24 ساعت انجام خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/99857" target="_blank">📅 21:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99856">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
کانال 12 اسرائیل مدعی شد:
ایران قصد داشت ترامپ را در جریان سفرش به ترکیه ترور کند. اطلاعات خارجی این توطئه را کشف و به مقامات آمریکایی هشدار داد، که منجر به تعویض هواپیمای ترامپ با پرواز برگشت او به واشنگتن شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/99856" target="_blank">📅 21:26 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
