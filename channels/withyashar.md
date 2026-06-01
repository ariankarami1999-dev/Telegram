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
<img src="https://cdn4.telesco.pe/file/HUPObd_8U3hSr0IOt507d5OYfmwK3RDDlxaK7_iUm62Q4BLryIRjHqc1sWZlFplgLf32knzUTN1B1sXOpMdyIbn6wNQWXOULvMRy2mRcCescbnVXbiKLHpN6NCh_CuTlbRrjUf0nr0J1CqQg7kiG8Ovwa4161Vv0tPIjTwCJlgbs3rLTjYTKAGBZskpA0g9i_Ltf89zez8oF8CFcZ1p78nIc4QBuA8XxbdkNQIzyXIboVidNptuPrjZ6P6Y4i-WMYmLYRt8E2kPmcgMS4Q9MyMETZNwcR0VylsKm7mbLYGWdFVzaaJKiOu7w-YbZKV_mr5fyO-lmfaxY5H3bVDE31w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 285K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 23:41:19</div>
<hr>

<div class="tg-post" id="msg-13205">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/withyashar/13205" target="_blank">📅 23:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13204">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">این قدم اول هست و ما پشیمون نمیشیم
😃
نیازی ندیدم تمام پلن ها یک جا انجام بشه در نتیجه از همین شروع کردم ، من به تقدیر خودم و مردمم ایمام دارم</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/withyashar/13204" target="_blank">📅 23:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13203">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">دوست گرافیستی که قرار‌ بود اوکی کنه آفلاین بود و در نتیجه اینم خودم با ای آی دقایق پایانی درست کردم که دقیقه ای رأس ۱۱:۱۱ آنتایم حاظر و پست شد ، میدونم و ببخشید</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/withyashar/13203" target="_blank">📅 23:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13202">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐴𝑚𝑖𝑟</strong></div>
<div class="tg-text">فونت پست یجوریه بنظرم
یچیز دیگ بهتر نیس بزاری؟</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/withyashar/13202" target="_blank">📅 23:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13201">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">درود در عکس آخر  کاش بجای  جناب آقای یاشار توکلیان  می‌نوشتید  اینجانب یاشار توکلیان را .... کمی گرم تر بود  البته نظر بنده بود یاشار جار  باز نظر شما محترم است
❤️
ممنون از زحماتتون</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/withyashar/13201" target="_blank">📅 23:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13200">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA.r</strong></div>
<div class="tg-text">درود در عکس آخر
کاش بجای
جناب آقای یاشار توکلیان
می‌نوشتید
اینجانب یاشار توکلیان را ....
کمی گرم تر بود
البته نظر بنده بود یاشار جار
باز نظر شما محترم است
❤️
ممنون از زحماتتون</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/withyashar/13200" target="_blank">📅 23:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13199">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac18e165f.mp4?token=cveDTrGPspYG-JymlTrZ2n_hXfavG5yMg7gIkkYz0RTHroTp1kYUeofTR-ZvGZRqlZXI1EEXmkphTPlVpKocDlcj1LUrGCrVMrmXoiO87pKlauGvcYkP4o2QS65XFT5H9sQ4odQwbyK-IbM6DixTLbXw0zS1oK7dWQ1sMsRIH32uEo-AjSbHeeAkbs27o1bc83t2YCpaKm40MDyubesehJZR34CI1NMRSipLTjJ-uDxQcCA0zehYVzKwuhlEMgnVsA27nq-MH5qTZAR52dpA3m2Z1NdINsFCSnnW9GGwrGAI9Hqnw_ukbLROug24bX1IoqEMt4bHGSbRXxKPlm4psg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac18e165f.mp4?token=cveDTrGPspYG-JymlTrZ2n_hXfavG5yMg7gIkkYz0RTHroTp1kYUeofTR-ZvGZRqlZXI1EEXmkphTPlVpKocDlcj1LUrGCrVMrmXoiO87pKlauGvcYkP4o2QS65XFT5H9sQ4odQwbyK-IbM6DixTLbXw0zS1oK7dWQ1sMsRIH32uEo-AjSbHeeAkbs27o1bc83t2YCpaKm40MDyubesehJZR34CI1NMRSipLTjJ-uDxQcCA0zehYVzKwuhlEMgnVsA27nq-MH5qTZAR52dpA3m2Z1NdINsFCSnnW9GGwrGAI9Hqnw_ukbLROug24bX1IoqEMt4bHGSbRXxKPlm4psg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/withyashar/13199" target="_blank">📅 23:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13198">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/withyashar/13198" target="_blank">📅 23:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13197">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">بیانیه جمعی از ایرانیان داخل و خارج کشور خطاب به شاهزاده رضا پهلوی  پدر گرامی ،  این متن جمع‌بندی مجموعه‌ای از دیدگاه‌ها، نگرانی‌ها و پیشنهادهای طیف گسترده‌ای از ایرانیان داخل و خارج کشور است که با هدف تقویت انسجام ملی، افزایش شفافیت و ایجاد مسیر عملی برای…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/withyashar/13197" target="_blank">📅 23:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13196">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/withyashar/13196" target="_blank">📅 23:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13195">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پست شد اینستاگرام سر‌ساعت
https://www.instagram.com/p/DZDi1pCEfvI/?igsh=MWN3ZWNhdWxqbmk0OA==
لطفاً این پست را استوری کنید و برای تمام افراد مرتبط با شاهزاده رضا پهلوی و شخص خود ایشان و تمامی پیجهای ایشان ارسال کنید.</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/withyashar/13195" target="_blank">📅 23:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13194">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98c544c644.mp4?token=k9yH2OqMPqXNDno5XIgTorGKhkLcYgeY-Ce4Q3NHqASUX0AjeYSBYpWYkKXbQHKPC-Q-0Prx-VIs5xDTDKQ7aJpiqFNu1qb2ds7zHVr42lGJ1C2ZQDJtmUDF5--OFM_1s9RrQ33e1dnIqoyQ_XwRuFJs5As7A_N3uEbZFy0tP-Eg4WXc4xDbaOOKLfP1L4y-RlF-y8rQU2OVv5ojQivW60xHhqkn7G2M6r903r2J4Aco5xJdc52qAnlNc5UbC8b11QdcUJb_aq84nAgUbAilrQ-x0KtjUkjFKU5VnzNtDFqJFFmsGQlAmApQSa14_n33MzBGl6Tmy-GhLcTT4kGXzpDkWuDyJqi-8Kfv82cJxx22TC4q1lObJ1rwSd8ydU4ZomHrbnAY3iB2G9rnsZy6Pu8HZQubXKMNu4C_fAKBiDUWVZKzcoKdLMS585ovUaLmBH6BBNU2Re6UHG1jjUDCGkazCXlPDpzWoq3LyNRoOmgITGiLPERokHO5lvqiFwaXY9nreqxsMXBQNiqY-JNXQaW9DcqdYq5YDuMqJkPN57Q7xoOlAZMT18iK8es1WnEfjnJ-eJqGzzKWS0QK69Lld8pzJjQXL-LMFUVE7P6BSHvuXZ7HoWkICvkzwC7Stt8lAnSz9UYx-TOb0Psyjd1QZMxLpLtgsv83HQu52t4cfZU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98c544c644.mp4?token=k9yH2OqMPqXNDno5XIgTorGKhkLcYgeY-Ce4Q3NHqASUX0AjeYSBYpWYkKXbQHKPC-Q-0Prx-VIs5xDTDKQ7aJpiqFNu1qb2ds7zHVr42lGJ1C2ZQDJtmUDF5--OFM_1s9RrQ33e1dnIqoyQ_XwRuFJs5As7A_N3uEbZFy0tP-Eg4WXc4xDbaOOKLfP1L4y-RlF-y8rQU2OVv5ojQivW60xHhqkn7G2M6r903r2J4Aco5xJdc52qAnlNc5UbC8b11QdcUJb_aq84nAgUbAilrQ-x0KtjUkjFKU5VnzNtDFqJFFmsGQlAmApQSa14_n33MzBGl6Tmy-GhLcTT4kGXzpDkWuDyJqi-8Kfv82cJxx22TC4q1lObJ1rwSd8ydU4ZomHrbnAY3iB2G9rnsZy6Pu8HZQubXKMNu4C_fAKBiDUWVZKzcoKdLMS585ovUaLmBH6BBNU2Re6UHG1jjUDCGkazCXlPDpzWoq3LyNRoOmgITGiLPERokHO5lvqiFwaXY9nreqxsMXBQNiqY-JNXQaW9DcqdYq5YDuMqJkPN57Q7xoOlAZMT18iK8es1WnEfjnJ-eJqGzzKWS0QK69Lld8pzJjQXL-LMFUVE7P6BSHvuXZ7HoWkICvkzwC7Stt8lAnSz9UYx-TOb0Psyjd1QZMxLpLtgsv83HQu52t4cfZU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : بو های مشکوک ، انبوه هوا پیما های آمریکایی در جنوب ایران و ورود به حریم هوایی
@withyashar</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/withyashar/13194" target="_blank">📅 22:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13193">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">وزیر جنگ اسرائیل: در لبنان آتش‌بس نداریم @withyashar</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/withyashar/13193" target="_blank">📅 22:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13191">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دیدبان اتاق جنگ : الان ازسمت کرج موشک شلیک شد  @withyashar</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/withyashar/13191" target="_blank">📅 22:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13190">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">وزیر جنگ اسرائیل: در لبنان آتش‌بس نداریم
@withyashar</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/withyashar/13190" target="_blank">📅 22:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13189">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">حملات اسرائیل به منطقه صور ادامه دارد
@withyashar</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/withyashar/13189" target="_blank">📅 22:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13188">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پدافند تهران فعال شد
@withyashar</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/withyashar/13188" target="_blank">📅 22:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13187">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">همانطور که از هفته پیش وعده داده بودم حدود یک ساعت دیگر ما متنی را برای شاهزاده رضا پهلوی ارسال می کنیم. همبستگی شما در این فراخوان باعث می شود صدای ما شنیده تر شود و ارتباطی بهتری بین ما و شاهزاده شکل بگیرد. ممنون از همراهی و کمک شما. تا می توانید به دوستان خود بگویید و آنها را آماده کنید.</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/withyashar/13187" target="_blank">📅 22:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13186">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">وزیر بن‌گویر: آقای نخست‌وزیر،
شما گفتید که یک نخست‌وزیر قدرتمند در صورت امکان به رئیس‌جمهور آمریکا «بله» می‌گوید و در صورت ضرورت «نه».
اکنون زمان آن است که به دوست ما، رئیس‌جمهور ترامپ، «نه» گفته شود.
اکنون زمان آن است که آنچه لازم و ضروری است انجام شود: حمله به حزب‌الله، آزاد گذاشتن دست رزمندگان ما و بازگرداندن امنیت به شمال.
@withyashar</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/withyashar/13186" target="_blank">📅 21:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13185">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c93913316d.mp4?token=JWMOui8JIu6K7-cZrw1X2MI-53ygQiENCQGGNY7m88nzjqw70mmW2ZCoYu_L4q_ZXnVyvrT6crZ4R-7vc_aClThkabEGty8QVbr2sCB_ijj6s36hZSnZA9rd-QgatfqWcyc_TftCZIAxDrHjeXHUeN6W77jPlQxCdaGir8reH7jR30vC8XexUv2WyNJphUIkK1u7YLE7EheRCOlDFHPumj4-gYc7OESpHSl7Oc-u-r5GAOqMjGa0VAn2xWZC8GKO2YnoeCPqfBAqGUbOBYXI4MWYe7gG4zWuoB5XiKHYWFok3r23aUn3b9RMk1jxhO8jRxm_vst-7xQUp-6xfRS7Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c93913316d.mp4?token=JWMOui8JIu6K7-cZrw1X2MI-53ygQiENCQGGNY7m88nzjqw70mmW2ZCoYu_L4q_ZXnVyvrT6crZ4R-7vc_aClThkabEGty8QVbr2sCB_ijj6s36hZSnZA9rd-QgatfqWcyc_TftCZIAxDrHjeXHUeN6W77jPlQxCdaGir8reH7jR30vC8XexUv2WyNJphUIkK1u7YLE7EheRCOlDFHPumj4-gYc7OESpHSl7Oc-u-r5GAOqMjGa0VAn2xWZC8GKO2YnoeCPqfBAqGUbOBYXI4MWYe7gG4zWuoB5XiKHYWFok3r23aUn3b9RMk1jxhO8jRxm_vst-7xQUp-6xfRS7Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدبان اتاق جنگ : الان ازسمت کرج موشک شلیک شد
@withyashar</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/withyashar/13185" target="_blank">📅 21:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13184">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">۲ حمله هوایی اسرائیل به شهر نبطیه الفوقا در جنوب لبنان انجام شد.
@withyashar</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/withyashar/13184" target="_blank">📅 21:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13183">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsdCfEHS8hNo1NqPCRs9gzLoTaivy2MwG501HWA63CiyBdcIfrpW73vgs1kRyMICYpNnBT-eSzcyq5D6ueRmmUpk0cePhxzP8Qc9gmADxxpLqNemq9mzaPlKJk1k4TrXbYmPwwPMCUtPxk5gHDiJgrJqASdYu53WsFDlERKfWpR4objsa6sI09rz45PPzq7cW_N4s6-womIZSLt50fCsQ5bhBlnM7b8uzFSUd3_4G5m-NCC0oHGu2N8VdKcoLsx0pfBgzHIliRoTQqO2cejuLq-3yE-G1ldkSS4kMk4RhqT5rVGPvvZd1MsT8rBMPXlLRt5EDgcfnUuiSYWDRYAl1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: مذاکرات با سرعت بالایی با جمهوری اسلامی ایران ادامه دارد
@withyashar</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/withyashar/13183" target="_blank">📅 21:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13182">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">شلیک راکت/پهپاد توسط حزب‌الله
@withyashar</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/withyashar/13182" target="_blank">📅 21:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13181">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATxZbVgtCutVNUQI6WPs3CMwfglNVKbAFoROyFz75VZ_zXuBQjmTpuwwwH-AfTLJG8h5wJ78_a9zJR3g0U7pWxDRd2KmJq9tNRgZwtIvwpJLQ2iqF69k8tfkjAGDzqNbT9D2-pjlC_i8GVp84HbZpxPpZsYhhLpVxLVOH4_TEzCm56RbuKBlsr_yTSX9k4uOlR6mVdaE6j0mAnSHBspgNpZ2A3VojWLhctMq9qbCRlMm4-EncNV1rSj5t8E1hiF3MCvYRfzar4veOF4bcsyHRS9KDA2hWirEFk4bTOlz6n_pqUju_yIitGwOzMW_H6vW-WOF0b1tfds-ly3jpq4ETg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«من تماس بسیار سازنده‌ای با بی‌بی نتانیاهو، نخست‌وزیر اسرائیل داشتم؛ هیچ نیروی نظامی به بیروت نخواهد رفت و تمام نیروهایی که در راه بودند نیز پیش از این بازگردانده شده‌اند. به همین ترتیب، از طریق نمایندگان بلندپایه، گفتگوهای بسیار خوبی با حزب‌الله داشتم و آن‌ها موافقت کردند که تمامی تیراندازی‌ها (درگیری‌ها) متوقف شود؛ به این صورت که اسرائیل به آن‌ها حمله نخواهد کرد و آن‌ها نیز به اسرائیل حمله نمی‌کنند.
رئیس‌جمهور دونالد جی. ترامپ»
@withyashar</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/withyashar/13181" target="_blank">📅 21:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13180">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.
@withyashar</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/withyashar/13180" target="_blank">📅 21:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13179">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">رویترز به نقل از دو منبع اسرائیلی: اسرائیل منتظر تایید نهایی ترامپ برای هرگونه عملیاتی در حومه جنوبی بیروت است.
@withyashar</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/withyashar/13179" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13178">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">کانال ۱۲ عبری: تماس تلفنی ترامپ و نتانیاهو بیش از یک ساعت است که ادامه دارد
@withyashar</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/withyashar/13178" target="_blank">📅 20:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13177">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">العربیه به نقل از رادیو و تلویزیون اسرائیل:
با مداخله آمریکا حمله بزرگی به ضاحیه بیروت لغو شد!
@withyashar</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/withyashar/13177" target="_blank">📅 20:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13176">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">منابع امنیتی اسرائیلی می گویند ترامپ دستور لغو حملات به بیروت را صادر کرده است
@withyashar</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/withyashar/13176" target="_blank">📅 20:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13175">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ:در تماس با نخست‌وزیر نتانیاهو فقط میخواهم شرایط را در جبهه لبنان ارزیابی کنم
@withyashar</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/withyashar/13175" target="_blank">📅 20:48 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13174">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">تسنیم: اسرائیل از ترس تهدیدهای جمهوری اسلامی حمله نکرده.
@withyashar</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/withyashar/13174" target="_blank">📅 20:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13173">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">شبکه کان اسرائیل: حمله به حومه جنوبی (بیروت) به تعویق افتاد.
تلویزیون ارتش اسرائیل: عقب‌نشینی میکنیم
@withyashar</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/withyashar/13173" target="_blank">📅 20:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13172">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">کانال ۱۲ اسرائیل: همه منتظر نتایج گفتگوی دراماتیک بین ترامپ و نتانیاهو هستند تا بفهمند اوضاع به کدام سمت خواهد رفت
@withyashar</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/withyashar/13172" target="_blank">📅 20:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13171">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ به CNBC : قیمت نفت به‌زودی مثل سنگ سقوط می‌کنه.
@withyashar</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/withyashar/13171" target="_blank">📅 20:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13170">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اتاق جنگ با یاشار : یعنی‌ عراقچی‌زنگ زده پاکستان چه پیشنهادی داده که پاکستان رنگ زده ترامپ و ترامپ هم فوری‌ زنگ زده بی بی
🤬</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/withyashar/13170" target="_blank">📅 20:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13169">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">تلویزیون اسرائیل اعلام کرد آمریکا دخالت کرده و جلوی ادامه حمله به بیروت رو گرفت
@withyashar</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/withyashar/13169" target="_blank">📅 20:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13168">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">رسانه عبری i24news: اسرائیل حمله در ضاحیه را متوقف کرد
@withyashar</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/withyashar/13168" target="_blank">📅 20:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13167">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">رومن گوفمن رئیس جدید موساد شد.  رومن گوفمن یک افسر ارشد ارتش اسرائیل با درجه سرتیپ‌ژنرال (Aluf) است که سابقه طولانی در یگان‌های زرهی و فرماندهی عملیاتی دارد. او در جنگ‌ها و عملیات‌های مختلف از جمله درگیری‌های لبنان، انتفاضه دوم و جنگ‌های غزه حضور داشته و در…</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/withyashar/13167" target="_blank">📅 20:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13166">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M94AN_P6GM6DNGtSv_ubYAjVYrhXpGaCkpUZAWNgu0Xnn_4ZVlKuQ189wX0RjjklfLcawOCL01Os0KuCJafxTEEizdkw3YNASnr0T9FJkHOBtWmfpEL1VvJiso8K6Ii2vJeHcgvGZotcMqpsqMYYduIEXPp45u5RL1YVIYeBkZwxr_n8GQwkMIVonvZKA04v4UiTr7bMj6V2YDzI-32pmuviBBK3AhA5dIz7RecnrKfTgZff8OFR53hB9DH0-Wcok-PPKi6mGOcozKWqc7SNPJqNsWF4F2KwCgkG6S65nr4tj-j0NzfiZ858RYk8ZNw5jS3EWwg0-rOmamgs2mQgzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رومن گوفمن رئیس جدید موساد شد.
رومن گوفمن یک افسر ارشد ارتش اسرائیل با درجه سرتیپ‌ژنرال (Aluf) است که سابقه طولانی در یگان‌های زرهی و فرماندهی عملیاتی دارد. او در جنگ‌ها و عملیات‌های مختلف از جمله درگیری‌های لبنان، انتفاضه دوم و جنگ‌های غزه حضور داشته و در سطوح مختلف فرماندهی تا سطح تیپ و یگان‌های عملیاتی ارتقا یافته است. همچنین در ۷ اکتبر ۲۰۲۳ مستقیماً در درگیری با نیروهای حماس شرکت کرد و مجروح شد. از سال ۲۰۲۴ به‌عنوان دبیر نظامی نخست‌وزیر بنیامین نتانیاهو فعالیت می‌کند و از سال ۲۰۲۳ نیز در ساختار تصمیم‌گیری و کابینه امنیتی او نقش فعال داشته است
@withyashar</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/withyashar/13166" target="_blank">📅 20:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13165">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مسکو: نقض آتش‌بس عمدتا از سوی اسرائیل است
معاون وزیر امورخارجهٔ روسیه: عمیقاً نگران گسترش تنش‌های زنجیره‌ای به لبنان هستیم و اقدامات ارتش اسرائیل علیه حزب‌الله، دور جدید و خطرناکی از درگیری مسلحانه را رقم زده است.
@withyashar</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/withyashar/13165" target="_blank">📅 20:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13164">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c96df3d233.mp4?token=kHBO0VsRIuEWMHMwTjdFePKtNm3TZybom2POVij5dCJ0NgeMAmWI-cLzHpKEX0rZSueHCtdjeM-hEbMGlPMNUTxrpYZXWZ1lqOsbEIvkb1wUESfdcpHGMBRbVPn62pOkD2FGajHcZXSez9dSiQGQM6Qa-rPFHm7BV0cZkRkhzlj7uvRPB8SQE74LKzRkVahlQcNNABzro3sAwT2MmGGT6FNfpgPn29Oq2qpco7iD9JibMw-X7kM8fgmcvo_1B2tv5fGm9hmlNa-E_wYGAeGgy5tA-GWsoVtRsmj0nPOe2cUt1QuAS-4zUvFruKXBs3AD_-LOxmPqKo35y7OGBo2iag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c96df3d233.mp4?token=kHBO0VsRIuEWMHMwTjdFePKtNm3TZybom2POVij5dCJ0NgeMAmWI-cLzHpKEX0rZSueHCtdjeM-hEbMGlPMNUTxrpYZXWZ1lqOsbEIvkb1wUESfdcpHGMBRbVPn62pOkD2FGajHcZXSez9dSiQGQM6Qa-rPFHm7BV0cZkRkhzlj7uvRPB8SQE74LKzRkVahlQcNNABzro3sAwT2MmGGT6FNfpgPn29Oq2qpco7iD9JibMw-X7kM8fgmcvo_1B2tv5fGm9hmlNa-E_wYGAeGgy5tA-GWsoVtRsmj0nPOe2cUt1QuAS-4zUvFruKXBs3AD_-LOxmPqKo35y7OGBo2iag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/withyashar/13164" target="_blank">📅 20:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13163">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مراسم رئیس جدید موساد به دلیل تماس تلفنی ترامپ و نتانیاهو لغو شد
@withyashar</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/withyashar/13163" target="_blank">📅 20:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13162">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ارتش اسرائیل :  فرمانده یه واحد تو سامانه موشکی حزب‌الله رو از بین بردیم @withyashar</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/withyashar/13162" target="_blank">📅 20:00 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13161">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">دونالد ترامپ به ان‌بی‌سی نیوز درباره مذاکرات با ایران گفت: ما بیش از حد صحبت کرده‌ایم، سکوت کردن خوب خواهد بود.
اگر گزارش‌ها مبنی بر تعلیق مذاکرات ایران با آمریکا درست باشد، «اشکالی ندارد»
ترامپ همچنین گفت: «این به آن معنا نیست که ما برویم و شروع به انداختن بمب کنیم. ما فقط سکوت می‌کنیم. محاصره را حفظ می‌کنیم.»
تحریم‌های ما علیه ایران به محکمی فولاد است و به همین شکل باقی خواهد ماند
@withyashar</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/withyashar/13161" target="_blank">📅 19:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13160">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ: من هیچ خبری مبنی بر تعلیق مذاکرات با ایران دریافت نکرده‌ام
@withyashar</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/withyashar/13160" target="_blank">📅 19:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13159">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">عراق تمام پروازهای های خود به بیروت در ساعات آینده را لغو کرد.
@withyashar</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/withyashar/13159" target="_blank">📅 19:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13158">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">عراقچی یه تماس تلفنی فوری با میانجی پاکستانی برقرار کرد
@withyashar</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/withyashar/13158" target="_blank">📅 19:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13157">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ارتش اسرائیل :  فرمانده یه واحد تو سامانه موشکی حزب‌الله رو از بین بردیم
@withyashar</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/withyashar/13157" target="_blank">📅 19:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13156">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">قرارگاه خاتم الانبیا:
در صورت حمله اسرائیل به بیروت،
ایران پایان آتش‌بس را اعلام می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/withyashar/13156" target="_blank">📅 19:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13155">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/withyashar/13155" target="_blank">📅 19:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13154">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">صدا و سیما: بسیار محتمل است که آتش‌بس بین ایران و آمریکا در صورت ادامه حملات در لبنان به پایان برسد
@withyashar</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/withyashar/13154" target="_blank">📅 19:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13153">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">هشدار قرارگاه مرکزی خاتم‌الانبیا مبنی بر تخلیه شمال اسرائیل:
نتانیاهو در ادامۀ شرارت‌های خود در منطقه، ضاحیه و بیروت را تهدید به بمباران نموده و برای ساکنان آن هشدار تخلیه اعلام کرده است.
با توجه به نقض مکرر آتش‌بس ، در صورت عملی‌شدن این تهدید به ساکنان بخش های شمالی و شهرک‌های نظامی در اسرائیل هشدار می‌دهیم اگر نمی‌خواهند آسیب ببینند منطقه را ترک نمایند.
@withyashar</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/withyashar/13153" target="_blank">📅 19:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13152">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/withyashar/13152" target="_blank">📅 19:19 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13151">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ارتش اسرائیل: به سراسر لبنان از ضاحیه گرفته تا صور حمله می‌کنیم
@withyashar</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/withyashar/13151" target="_blank">📅 18:00 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13150">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">وزارت کشور کویت به ساکنان خود هشدار داد که در انتظار حمله قریب‌الوقوع ایران در مکان‌های امن بمانند
@withyashar</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/13150" target="_blank">📅 17:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13149">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
تسنیم: مذاکرات با آمریکا کاملا متوقف شد!
ایران خواستار توقف کامل تمام عملیات‌ها در غزه و لبنان برای از سرگیری مذاکرات با آمریکا است.
همچنین ایران به میانجی ها اعلام کرده است که بستن کامل تنگه هرمز و همچنین تنگه باب المندب را در دستور کار قرار داده است
@withyashar</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/13149" target="_blank">📅 16:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13148">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تسنیم: ایران تبادل پیام با آمریکا را در اعتراض به جنایات اسرائیل در لبنان متوقف می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/13148" target="_blank">📅 16:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13147">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بعضی رسانه ها مدعی شد تا ساعتی دیگر، پاسخ نقض آتش بس توسط جمهوری اسلامی ایران با حمله گسترده به رژیم صهیونیستی، داده خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/withyashar/13147" target="_blank">📅 16:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13146">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEUDN6NL4zP3VAj-tWQuyXydnhrm8_rFZ5afPD2jGCPUYDcEdsiWrlmPtOIvYdnfV6DmhqfgCTyYd7A1dYdSQ0sI_BMmnA-6rXQ43lpxgxoX-usCqwl7faX7WuHjJNr6TxKXmwP6NYZqxBGkcT7kPIyKmJsfCwQnnvSznld-IKubKsCAaOlaICku6jcseTAVKeruaK6CJlF3wbW1JMPe6T6moMHb5QSviraf-_cMmzEIORrfatGgo-yNJp-nmmyQDra3UMyE_tfpnN300cgAENKsb8K1fbyAlXZki8zED-pwbzodjBJDmav2osofhaOqrh4AIUTo7_x2smkg1iWF4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداسیما طی خبری فوری:
نیروهای مسلح : حمله متوقف نکنن علیه لبنان ماهم حمله میکنیم
@withyashar</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/13146" target="_blank">📅 15:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13145">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که دو موشک بالستیک رژیم جمهوری اسلامی دیشب ساعت ۱۱ شب به وقت شرقی(۶:۳۰ صبح تهران)به سمت نیروهای آمریکایی در کویت شلیک شده است. موشک‌های ورودی سرنگون شدند و هیچ آسیبی به پرسنل آمریکایی وارد نشد.
@withyashar</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/withyashar/13145" target="_blank">📅 15:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13144">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/13144" target="_blank">📅 14:56 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13143">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd86679833.mp4?token=YVp7jwFDnFdeNNkujliCOsCC9dd-FqJJ62d3QroZyI0DmnmfZMWN6EBWIzZvDncQ4FcU4VmVvIji4T1KYRsZgEMUveAKnMTFmIn4KyhOJRskjcv_4aloH8COhbmtoIsmR06WHzLx2HiphWD_SVNuL1feKsQF4avx6coyJHn1WXcRPSf2_UyQ1rxCkaCVTmzUSIXCqgGDkyItgrrhjLajvbkqmDuSL46e1LqnKATX8rKlwGQUp4NnFC7XdlyLa6_cd9MbQ9hLqk750z0RSFC5GtIxMIezAEyPBYFd8YcLYt38qbBkGH7JR03ydqTXbHO4bAPfzEs15vosjIB2LHyoEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd86679833.mp4?token=YVp7jwFDnFdeNNkujliCOsCC9dd-FqJJ62d3QroZyI0DmnmfZMWN6EBWIzZvDncQ4FcU4VmVvIji4T1KYRsZgEMUveAKnMTFmIn4KyhOJRskjcv_4aloH8COhbmtoIsmR06WHzLx2HiphWD_SVNuL1feKsQF4avx6coyJHn1WXcRPSf2_UyQ1rxCkaCVTmzUSIXCqgGDkyItgrrhjLajvbkqmDuSL46e1LqnKATX8rKlwGQUp4NnFC7XdlyLa6_cd9MbQ9hLqk750z0RSFC5GtIxMIezAEyPBYFd8YcLYt38qbBkGH7JR03ydqTXbHO4bAPfzEs15vosjIB2LHyoEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش فاکس نیوز از چند حمله آمریکا به قشم !
@withyashar</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/13143" target="_blank">📅 14:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13142">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">تانکرترکرز: چهار نفتکش ایرانی با محموله هفت میلیون بشکه‌ای به ایران بازگردانده شدند و نتوانستند محاصره آمریکا را بشکنن
@withyashar</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/13142" target="_blank">📅 14:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13141">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">عراقچی:
آتش‌بس میان ایران و ایالات متحده، بدون هیچ ابهامی، آتش‌بسی در تمامی جبهه‌ها، از جمله لبنان، محسوب می‌شود.
نقض این آتش‌بس در هر یک از جبهه‌ها، به منزله نقض آن در تمامی جبهه‌ها است.
ایالات متحده و اسرائیل مسئول پیامدهای هرگونه نقض این آتش‌بس خواهند بود.
@withyashar</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/13141" target="_blank">📅 14:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13140">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36b672cbbb.mp4?token=q1nuyxxQASsylb9jeeVTp8gshR8anaAsB0fMF6VoK-NqLZ4ARVbNaUQ4-WyCAU-DsPRL-3gb7N2Omxk1XM6BAWSSbKIY7uzsXl0Axs2uOoptpXUvrg3GYdnMXfjwAp8mKKqp0vsu-9DMwOaDnJihQVWk2hOpovUeD707CQh0CjCvtqtkb_bVQ5qUPqVtvxcOGpA7RCN1IuUv0rZE3OuRTz2kvAeSxIRIsm14tSfsYkK8g_GFOkEbFA9I1oUqm9sjZCwlREbUQWinM3qyWjm0A8Jhvo4U1a3osh__e0ZDkNP48TNijfFk1-T0vLiuKU-qlp_DNM8c4LYn4hPEW3tMjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36b672cbbb.mp4?token=q1nuyxxQASsylb9jeeVTp8gshR8anaAsB0fMF6VoK-NqLZ4ARVbNaUQ4-WyCAU-DsPRL-3gb7N2Omxk1XM6BAWSSbKIY7uzsXl0Axs2uOoptpXUvrg3GYdnMXfjwAp8mKKqp0vsu-9DMwOaDnJihQVWk2hOpovUeD707CQh0CjCvtqtkb_bVQ5qUPqVtvxcOGpA7RCN1IuUv0rZE3OuRTz2kvAeSxIRIsm14tSfsYkK8g_GFOkEbFA9I1oUqm9sjZCwlREbUQWinM3qyWjm0A8Jhvo4U1a3osh__e0ZDkNP48TNijfFk1-T0vLiuKU-qlp_DNM8c4LYn4hPEW3tMjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کوچ جمعی مردم بیروت پس از هشدار اسرائیل به بمباران
@withyashar</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/withyashar/13140" target="_blank">📅 14:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13139">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">علیرضا فغانی به اولین داور تاریخ تبدیل شد که در ۴ جام جهانی قضاوت میکند
@withyashar</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/13139" target="_blank">📅 14:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13138">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اتاق جنگ با یاشار : اولین پرواز بازگشت زائران حج تمتع امروز ۱۱ خرداد ساعت ۱۶:۳۰ در مشهد به زمین می‌نشیند این عملیات ۱۱ روز دیگر ادامه دارد و در ۲۲ خرداد «جمعه» آخرین پرواز بازگشت انجام میشود , ۲۲ خرداد جمعه هفته دیگر ۲ روز قبل از‌ تولد دونالد ترامپ است و شب…</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/withyashar/13138" target="_blank">📅 13:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13137">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اتاق جنگ با یاشار : اولین پرواز بازگشت زائران حج تمتع امروز ۱۱ خرداد ساعت ۱۶:۳۰ در مشهد به زمین می‌نشیند این عملیات ۱۱ روز دیگر ادامه دارد و در ۲۲ خرداد «جمعه» آخرین پرواز بازگشت انجام میشود , ۲۲ خرداد جمعه هفته دیگر ۲ روز قبل از‌ تولد دونالد ترامپ است و شب آن مارکت هم برای آخر هفته بسته میشود
@withyashar
همچنین یک هفته بعد از آن یک آخر هفته طولانی داریم چون جمعه هم تعطیلی رسمی فدرال است جونتینث  «روز پایان برده داری در آمریکا»۱۹ جوئن ۲۹ خرداد</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/13137" target="_blank">📅 13:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13136">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گالانت : نتانیاهو اعلام کرده خاورمیانه دیگر جای حزب الله نیست و تا نابودی کامل جلو خواهیم رفت
@withyashar</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/13136" target="_blank">📅 13:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13135">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">قالیباف در توییتر(X):
«اعمال محاصرۀ دریایی و تشدید جنایات جنگی در لبنان توسط اسرائیل عدم پایبندی آمریکا به آتش‌بس است.
هر انتخابی، هزینه‌ای دارد و صورت‌حساب آن هم از راه می‌رسد؛ همه چیز سر جای خودش قرار خواهد گرفت.»
@withyashar</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/13135" target="_blank">📅 13:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13134">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بنیامین نتانیاهو به همراه وزیر دفاع دستور حمله به ضاحیه بیروت را اعلام کردند
@withyashar</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/13134" target="_blank">📅 11:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13133">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سخنگوی وزارت خارجه: ما حق دفاع مشروع در برابر نقض آتش‌بس توسط آمریکا را داریم و امروز هم مبدأ تجاوز به خاک کشور را هدف قرار دادیم.
@withyashar</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/withyashar/13133" target="_blank">📅 11:27 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13132">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامپ به نیوزویک : مردم ایران از من تشکر میکنند چون بجای یکبار، دوبار رژیم رو عوض کردم
@withyashar</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/13132" target="_blank">📅 11:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13131">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromThis.is ⁰²:³⁵</strong></div>
<div class="tg-text">داش جان جدت ری اکشن
🤣
رو باز کن</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/13131" target="_blank">📅 11:19 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13130">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/13130" target="_blank">📅 11:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13129">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hl9HR4-O577NuBZwMFUFryWguKO1Z4MMtVB8sbsvAlkAdxnlBwkQAJfRfmDOW_kIsSUsOkx7XW3_s-11awdBOz-lgsItMLWXmB_DFxBkjPMiawkgJKvlNunEDClqamSrao1VcBqrEu3Jhd_2c5brJNlBAvf-1YZT2Spp1_yYn93H9E8neW-3YguP2RpDRPQ7nshs-O-B8gpb0EuVsfe0oC0KCNLWE-nzI3HCVC4BGrNPInMWynnImIYlSNq7p__PkMuEU78R6JVWgG78L4cpUcXHMKtx8O1NzPycAiis8hyPDwO2llpi9pYFmn2bgKGwtYMT9GZtLNPHne1kGXV9Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥴
🤣
@withyashar</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/withyashar/13129" target="_blank">📅 11:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13128">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اطلاعات  تایید نشده بهم رسیده که  اندیشه ترور هدفمند بوده   شخص‌ مورد نظر مسئول قراردادهای بین صدا و سیما و قرارگاه خاتم‌الانبیا بود @withyashar</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/13128" target="_blank">📅 11:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13127">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گزارش های از مشاهده خط شلیک موشک از همدان
@withyashar</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/13127" target="_blank">📅 10:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13126">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">صدای انفجار مهمات عمل نکرده اصفهان پادگان پانزده خرداد
@withyashar</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/withyashar/13126" target="_blank">📅 10:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13125">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">البته توجه کنید که گفته بودند از قبل که خنثی سازی مهمات عمل نکرده دارن  @withyashar ولی با توجه به اینکه سنتکام ساعتی پیش گفته حمله کرده و رادار زده هشیار باشید</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/13125" target="_blank">📅 10:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13124">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گروه تروریستس ۳پا امروز در بیانیه‌ای اعلام کرد در واکنش به حمله ارتش آمریکا به یک دکل مخابراتی در جزیره سیریک، «مبدأ حمله» رو هدف قرار داده و هشدار داد در صورت تکرار این اقدامات، پاسخ متفاوتی خواهد داد.
کویت حوالی ۶ صبح از فعال شدن سامانه‌های پدافندی خود برای مقابله با حملات موشکی و پهپادی خبر داد ولی مبدأ حمله را اعلام نکرد
@withyashar</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/13124" target="_blank">📅 10:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13123">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اتاق جنگ با شما : یاشار تتر داره کندل سبز میخوره همینجوری
این صداهای امروز مثل اینکه جدی تره
@withyashar
اتاق جنگ با شما :نهم اسفند هم همین ساعت ها بود داشتن حمله میکردند خدا به خیر کنه
😂
😂
💔</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/withyashar/13123" target="_blank">📅 09:48 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13122">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/13122" target="_blank">📅 09:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13121">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">صدای انفجار در اصفهان
@withyashar</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/13121" target="_blank">📅 09:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13120">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دوباره صدای انفجار‌ در بندر
@withyashar</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/13120" target="_blank">📅 09:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13119">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/withyashar/13119" target="_blank">📅 09:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13118">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/13118" target="_blank">📅 09:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13117">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeb</strong></div>
<div class="tg-text">یعنی جنگ رو پنهان میکنن ؟؟</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/13117" target="_blank">📅 09:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13116">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اتاق جنگ با شما : صداش دقیقا مثل جنگنده آمریکایی یا اسرائیلی بود
@withyashar</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/13116" target="_blank">📅 09:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13115">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گزارش های زیاد از صدای جنگنده در تهران
@withyashar</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/withyashar/13115" target="_blank">📅 09:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13114">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سنتکام : ما حملات دفاعی به رادار پهپاد و سایت‌های فرماندهی و کنترل در گوروک و قشم ایران انجام دادیم. @withyashar</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/13114" target="_blank">📅 09:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13113">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گزارش چندین انفجار بندر عباس
🚨
@withyashar</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/13113" target="_blank">📅 09:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13112">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9DhopQDPpBKfIYTK4sGs6bw2JBMiBwLfIVj_P4YR0fjZuPyeI7_gTTvyW2pEwVkEiWuBHHMPq-OUD7dwXrnEXtG85-eyYNtujFXJckbvU4Q5yK0-zZnvAMdaliDobGk4rbSWz_-EGwyCLuDUdXjNg5SaBKTXEWWf8xLz9ouwW8T7vDx3zT8Z0IUpCwuJdJAm9WRKs8_EL1bpNsyfZ0KDuhphboQIvNWZNJKrgfulPnKBok5Voa49lvAQSgj0mxmfShd_UgzKIj0kTfYvlpl8YsOfB4AiR8db8W_tb3sD3vNb-PhOh2Di8KJJt9A8fv6_DvUFcauD1OZ7PscQ62PUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رسمی قوه قضائیه ایران(میزان) اعلام کرد که دو نفر دیگر از معترضان دی‌ماه ۱۴۰۴ را به اتهام «آتش‌زدن مسجد»، «لیدری کودتا»، «تخریب اموال عمومی» و «مسدودسازی خیابان‌ها» مجازات کرده است.
نام این دو عزیز که ساعاتی پیش جاودانه شدند، مهرداد محمدی‌نیا و اشکان مالکی اعلام شده است.
@withyashar</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/13112" target="_blank">📅 09:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13111">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">سنتکام : ما حملات دفاعی به رادار پهپاد و سایت‌های فرماندهی و کنترل در گوروک و قشم ایران انجام دادیم.
@withyashar</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/13111" target="_blank">📅 08:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13110">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گزارش شلیک موشک از امیدیه در استان خوزستان به سمت کویت۶:۳۰ دقیقه و ۸:۳۳ دقیقه
@withyashar</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/withyashar/13110" target="_blank">📅 08:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13109">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPfl89oHsvIxZlVMiFFIIqkUAf8HMeH8R0XhhDHvdWMVO1y6JpPWD_lL8VZcO4McW-xQmGEdDIZ2LagiZ93ow-BJ-hcsfVmCUvI3bEeyxT2SfJR7acEj5g2kwn7LGvZ6reYaa_raM85cXH0I0sFU7ckHXjH5zMWfhI5tQHW5VDbnP7K2nH5EOrMDbG9rwtr1yCqsLPrntYbzFE1-VZVR6MQsqu4nanH8GuLIcU-Yrj4v-GqXXZDa-QeHJ5UI3shS5e9p2aLKwLleq09wugDJBoVfA_ygS6XmBbD07fq52P62sCWeYLT713tmc3Vm2M-JYAX102JmrCglYXiBrx1UBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث:
ایران واقعاً می‌خواهد به توافق برسد، و این توافق برای ایالات متحده آمریکا و کسانی که با ما هستند، توافق خوبی خواهد بود. اما آیا دموکرات‌های کودن و برخی جمهوری‌خواهانِ ظاهراً غیرمیهن‌دوست نمی‌فهمند که وقتی بازیگران سیاسی مدام، بارها و بارها و در سطحی بی‌سابقه، با نیش و کنایه منفی می‌گویند باید سریع‌تر حرکت کنم، یا کندتر حرکت کنم، یا وارد جنگ شوم، یا وارد جنگ نشوم، یا هر چیز دیگری، انجام درست کارم و مذاکره کردن برای من بسیار سخت‌تر می‌شود؟
فقط بنشینید و آرام باشید؛ در پایان همه‌چیز خوب پیش خواهد رفت همیشه همین‌طور است!
@withyashar</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/13109" target="_blank">📅 08:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13108">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گزارش‌ها از حمله پهپادی ایران به گروه های مخالف ایرانی-کرد در نزدیکی اربیل، شمال عراق!
@withyashar</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/13108" target="_blank">📅 00:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13107">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5eae745a43.mp4?token=O_MnzgdJzkQ1DStZh3WSCoKRPErXGj_KO4KAQMQXQ4tUltSvkwQO-CGzUflsiNs3uHCbh2r1ZrPJkp4LgmHRPdi7vS7HQuHVR_pvbbzUbfgB3rqRLu3O87tjLODSR_g6-61KLhCCA9F5sYpz5IXTUFpe51QrWcEog-ILap0NeOIh1d0bHNPF_buMs_JFCZu4gElHrVgG55RP0t0Rmx_7Ow6IoAx1QIMSf1uYjybXV4b9wMdXtyW5exEH3aVYRuIXxb_WRMN3NFRD5p3ShZ-GQP92nSgQOYGw686VnDxqtwrtPiej3N4745mjBVd2P4zkOBfsnJaj69ntTBCCdGYP0o0qFxiWdUN_Bm3nanCX2iDQ6NuUTwvjdD7cdIpe4WogMYYtcShXMztP9tfPZo_urjocUcDnYsQ7uFw7E-ncRTgCiRzY_QmSAvq0_j4u0iUgZ9TViRRNKSuC03HdgQrHHDFRG0hqC2Ln0W0DlmlNJzbPp13pALsx-6wvcAZdCgC2i_rR4_eg0bkGuGlPgJVlIVdiE40htG4lHvtVNxVwJQks1eEm1p4zCNQM7RDmq3BK2wnkUUg-UhvuZDtj0saCpxPG4DbOMQd4CxjuMttm2u6GJ7jKqNRFYHMxpyO0i6hl37VF0DW37OlcWJxiU3A5r2tGV2sgLoBndqpjtBPEwAI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5eae745a43.mp4?token=O_MnzgdJzkQ1DStZh3WSCoKRPErXGj_KO4KAQMQXQ4tUltSvkwQO-CGzUflsiNs3uHCbh2r1ZrPJkp4LgmHRPdi7vS7HQuHVR_pvbbzUbfgB3rqRLu3O87tjLODSR_g6-61KLhCCA9F5sYpz5IXTUFpe51QrWcEog-ILap0NeOIh1d0bHNPF_buMs_JFCZu4gElHrVgG55RP0t0Rmx_7Ow6IoAx1QIMSf1uYjybXV4b9wMdXtyW5exEH3aVYRuIXxb_WRMN3NFRD5p3ShZ-GQP92nSgQOYGw686VnDxqtwrtPiej3N4745mjBVd2P4zkOBfsnJaj69ntTBCCdGYP0o0qFxiWdUN_Bm3nanCX2iDQ6NuUTwvjdD7cdIpe4WogMYYtcShXMztP9tfPZo_urjocUcDnYsQ7uFw7E-ncRTgCiRzY_QmSAvq0_j4u0iUgZ9TViRRNKSuC03HdgQrHHDFRG0hqC2Ln0W0DlmlNJzbPp13pALsx-6wvcAZdCgC2i_rR4_eg0bkGuGlPgJVlIVdiE40htG4lHvtVNxVwJQks1eEm1p4zCNQM7RDmq3BK2wnkUUg-UhvuZDtj0saCpxPG4DbOMQd4CxjuMttm2u6GJ7jKqNRFYHMxpyO0i6hl37VF0DW37OlcWJxiU3A5r2tGV2sgLoBndqpjtBPEwAI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : چشم آسمان ، هواپیما آواکس
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/13107" target="_blank">📅 00:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13106">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/13106" target="_blank">📅 23:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13105">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">انفجار در فاز یک اندیشه شهریار خیابان شیشم شرقی در یک ساختمان که چندین مصدوم داشته  @withyashar</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/13105" target="_blank">📅 23:45 · 10 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
