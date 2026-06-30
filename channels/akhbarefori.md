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
<img src="https://cdn4.telesco.pe/file/GoxK92jFV1TD4kSacUT0namVFn_4mZHzbld4AdeZRTyZUvQK3LX8-qrXbdECKfsvB8KxpghfmuK2m5h9R5A5dAqdT4tcQtdUrUuXqOnhzmTZSeT3GzPjn_0UO6DKWkILbfUlaPbtww67hdjGMpe7EeYQByyydbTSLOqRtqGxxXEzzgprf5DK1mJm6pUI0NlsdXNX2H22kIiMsD401o0VH8il0UBaDjBFSWLNpXjKy-MfUr9K7tXgFOcL8PUcDufH8xGSWGtGtVpCjhLWNxmfHqezdOjrLn8eFO8IuqsFTmRt9kLMzxr3m-OAjt4xkG_PK6-huLK-8CkZr_AXKZ3o9Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.16M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 02:18:09</div>
<hr>

<div class="tg-post" id="msg-665164">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0riwx0AhSVM1IrEpJugjgW8MomccLkMt1x7HM8qA2VR8aMKAhO5ZqsNEhXcUNIrWQPkBJgzJy2Vp8YM2NOIlBJ9s0-dikfBhSLQE8LadWr-HnmKOAN9u75T2-A2YFPhzmdCtKVR3uzh3WCeumvCv3yBYYfbTmu0NfeL684l2p5LntrlI_rkxO_wsN7ix-cgdwi5QT8eup8DrRMQ51zRSvYX6X1tat7NBPxdClJj4i6yZeYdtSURv6xn6XL4Mm-9CeeLxJwhER5ikkWCvGm5hsVBus8hWj9J4dX6i73n9xJNIsN0A5VWAVLtdBiORsL-kbHHCQbK7oU51DOYsxoAbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
طلای آنلاین، بدون دردسر
خرید و فروش طلا دیگر نیازی به نگهداری فیزیکی و دغدغه‌های همیشگی آن ندارد.
سرمایه‌گذاری روی طلا، ساده‌تر و در دسترس‌تر از همیشه.
🔰
خرید و فروش آنلاین طلا
🔰
بدون دغدغه نگهداری فیزیکی
🔰
شروع سرمایه‌گذاری از مبالغ کم
👈
برای دریافت اطلاعات بیشتر کلیک کنید
📄
#طلای_آنلاین
#سرمایه_گذاری
#کارینکس
💎
با ما همراه باشید
اینستاگرام کارینکس
|
لینکدین
|
تلگرام
|
وبسایت
|
اینستاگرام آکادمی</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/665164" target="_blank">📅 01:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665163">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
وزارت خارجه قطر: نخست‌وزیر و وزیر امور خارجه این کشور در دیدار با «ویتکاف» و «کوشنر»، آخرین تحولات مربوط به مذاکرات میان واشنگتن و تهران را مورد بحث و بررسی قرار دادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/665163" target="_blank">📅 01:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665162">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9789db7080.mp4?token=pRLVfv6KvZvBU5JyeYtxCLie1DWIoWsdQQnKGS0VniYlgj82Zv3zfultcMPk9QORHjaZ8Sopgsm-LG3EF54is1W1lvLwuJYTFIaB3Vkn5flVQwz1zgCYoxwlyEEStSsdUzPYUBFKSv1svPqcv_Ydee1HkPeQwUXedqs_bwPOl2J-bV-4Z8oBcu_aEH8LZo810EHoTxYy0ANb9azIgxiIPebrT8_Pw-r633wk2TiO3qN6ht3OtEkOCErP4I6D0IBvFTLWNU7PWL9CP_KkVfKk4T6G3iUPnQw74X-qZfLXPf2WHmGSoqOW15wb1S3OdSnofY58KwtPTuBJOIEsfsqUhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9789db7080.mp4?token=pRLVfv6KvZvBU5JyeYtxCLie1DWIoWsdQQnKGS0VniYlgj82Zv3zfultcMPk9QORHjaZ8Sopgsm-LG3EF54is1W1lvLwuJYTFIaB3Vkn5flVQwz1zgCYoxwlyEEStSsdUzPYUBFKSv1svPqcv_Ydee1HkPeQwUXedqs_bwPOl2J-bV-4Z8oBcu_aEH8LZo810EHoTxYy0ANb9azIgxiIPebrT8_Pw-r633wk2TiO3qN6ht3OtEkOCErP4I6D0IBvFTLWNU7PWL9CP_KkVfKk4T6G3iUPnQw74X-qZfLXPf2WHmGSoqOW15wb1S3OdSnofY58KwtPTuBJOIEsfsqUhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول فرانسه به سوئد توسط امباپه
🇫🇷
1️⃣
🏆
0️⃣
🇸🇪
🔹
طرح طلای بیمه زندگی پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/665162" target="_blank">📅 01:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665161">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f4d30836a.mp4?token=JOYKMSbd0AlCa-ijNsdhN_6bGGvvPeljrdoUqwD05tR_WnAoP0lDvRZeB6-ftnVcJTV8TZp8WMQmEGqQSWPt_bVN6370v6t5MZLuPYQ12-6jronVSneJOWP7T_xvrksErSWnbwXYOzpRmlty-SJAD9DdRtxH07funOFwBzwgkWLqNSpirulOjtetHMOGrLxffig1Xn9L_N6nPyX6s27lh0dfTg-Qf9bqWZkQqcZrfAqvHhvQY9a5WByfllXmMSFPzGiDhX026IgdkR57w0XkMkrxHTVL697qhitiD5fB2kr_ZKy4jewbNgzWFAtae53ReLAUyn84qxpgzOV7x7kE6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f4d30836a.mp4?token=JOYKMSbd0AlCa-ijNsdhN_6bGGvvPeljrdoUqwD05tR_WnAoP0lDvRZeB6-ftnVcJTV8TZp8WMQmEGqQSWPt_bVN6370v6t5MZLuPYQ12-6jronVSneJOWP7T_xvrksErSWnbwXYOzpRmlty-SJAD9DdRtxH07funOFwBzwgkWLqNSpirulOjtetHMOGrLxffig1Xn9L_N6nPyX6s27lh0dfTg-Qf9bqWZkQqcZrfAqvHhvQY9a5WByfllXmMSFPzGiDhX026IgdkR57w0XkMkrxHTVL697qhitiD5fB2kr_ZKy4jewbNgzWFAtae53ReLAUyn84qxpgzOV7x7kE6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنایتکار افراطی اسرائیل: آماده‌ایم شمال غزه را غصب کنیم،شهرک‌های صهیونیستی بسازیم! فقط نتانیاهو بگوید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/665161" target="_blank">📅 01:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665160">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
صداوسیما با قطع برنامه گزارش قالیباف درباره اجرای بندهای تفاهم، به‌جای فراهم کردن بستر پاسخ‌گویی، مانع آن شد   روزنامه خراسان:
🔹
قالیباف اگر سکوت کند، متهم می‌شود به پنهان‌کاری، اگر بخواهد گزارش دهد، صداوسیما ترمز پخش را می‌کشد. صداوسیما باید روشن بگوید،…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/665160" target="_blank">📅 01:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665159">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
آستان حضرت عبدالعظیم(ع): حرم از ۱۱ تا ۱۵ تیر شبانه‌روزی پذیرای زائران است.
🔹
استاندار تهران: تهران از نظر امنیتی در وضعیت بسیار مطلوبی قرار دارد.
🔹
وزیر پیشین رژیم صهیونیستی: الجولانی تروریست کت‌وشلواری است!
🔹
رونالد کومان از سرمربیگری تیم ملی هلند استعفا داد
.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/665159" target="_blank">📅 00:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665157">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
عصبانیت صداوسیما از افشاگری قالیباف درمورد توافق خاص دولت قبل با آمریکا
🔹
صداوسیما زمانی مصاحبه قالیباف را قطع کرد که او در حال اشاره به توافق ناکام با آمریکا برای انتقال ۶ میلیارد دلار پول ایران از کره به قطر برای مصارف بشردوستانه (غذا و دارو) بود.
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/665157" target="_blank">📅 00:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665156">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gh7FttZ1pCCXrn2zFq9pradg-QJRjh63zIALo9LnJEiAqsTu3M0M-_ujgHNjpP_gnMLOnLd3z-phYqi7N_ljZ2GFqh60KzEAmwn3qGkuSAq4XnSdITNtwBxFvf6toliBMmMRxE7CdfzHIK_3k-WTNUdU9Nxat8i4yJYFjPB59mTM0vxdRd0UvkdapqooQpKhm-q-2fJiZZJpM3wCU_T9oY78pHl8WKmWaERWPeGm18wGPeZTX5O7SIiWeWYyFRJGkAWKX-M_Ikc5NgD_lQs9YWWnjikvyUzsTGcoys_GuI1IoiMD6cfx3MW3HNYTcMEb8DWeZKk9EBncnT3GODw2kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی ستاد تشییع رهبر شهید انقلاب: پیکر مطهر امام شهیدمان تا کنون نه به خاک سپرده شده و نه به ودیعه دفن شده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/665156" target="_blank">📅 00:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665155">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
رئیس‌جمهور ترکیه، اردوغان: آنچه در غزه رخ داده یک نسل‌کشی است و اسرائیل قطعاً بابت کشتار کودکان و غیرنظامیان پاسخگو خواهد شد؛ ما نمی‌توانیم در برابر این جنایت سکوت کنیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/665155" target="_blank">📅 00:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665154">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5feed3638f.mp4?token=CVttPJ8hUpN52toQEAccE2CvPkDbo1D_Wler0elXlRvaiVKbCqne3nJaXIBUwXOo070txbnX77PdlqxV-YsOzoH6SQ1F2xvbtlDIQuy1qEy3CWwIf_lgQN5iIszbMIX0TMshbJnYv7ujAYOZN1t-Y7vawknmE9b3mR4vL_Y2BW83DQzBQqQUvnECVU6D4IrQrAD_Kp_T0bgm_XmxL4W2FYut5TT4ekY91ODMs--I4jWdoEgnLbKjpzYckCk3ptpK3ignCVU4aStCUeYvj_MefsBJZZDcClOqzXsjyRe7mkS0d8kylDEz12iZQI_wWf8_kMjR6421LUdXT39FhPFrYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5feed3638f.mp4?token=CVttPJ8hUpN52toQEAccE2CvPkDbo1D_Wler0elXlRvaiVKbCqne3nJaXIBUwXOo070txbnX77PdlqxV-YsOzoH6SQ1F2xvbtlDIQuy1qEy3CWwIf_lgQN5iIszbMIX0TMshbJnYv7ujAYOZN1t-Y7vawknmE9b3mR4vL_Y2BW83DQzBQqQUvnECVU6D4IrQrAD_Kp_T0bgm_XmxL4W2FYut5TT4ekY91ODMs--I4jWdoEgnLbKjpzYckCk3ptpK3ignCVU4aStCUeYvj_MefsBJZZDcClOqzXsjyRe7mkS0d8kylDEz12iZQI_wWf8_kMjR6421LUdXT39FhPFrYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتانیاهو: کمک‌های آمریکا را نمی‌خواهیم؛ می‌توانیم خودمان تأمینش کنیم
🔹
کمک‌های آمریکا را نمی‌خواهیم و می‌توانیم خودمان تأمین مالی کنیم؛ روند قطع این حمایت‌ها باید امسال آغاز شود.
#Demon
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/665154" target="_blank">📅 00:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665153">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
دبیرکل سازمان بین‌المللی دریانوردی به الجزیره: هیچ قاعده‌ای وجود ندارد که به هیچ کشوری اجازه دهد بر تنگه‌های دریانوردی بین‌المللی عوارض وضع کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/665153" target="_blank">📅 00:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665152">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25696b8476.mp4?token=JX8OnDDgN0DthG_acn6EOQ68aK0_Tj5KfTQQslZ9tXgP3aJqqe49IH0irHD9jd3rPcFgk3ahv_CjU_d3H7OsPT_w3AgQrGIzQhb7inzEKffKU0ix6UuzVDwKRLHnvLI_-uWVmmu61AFG_m5WwG6TvF26C_pJbrY-OHxwTNbW0pyGgbTzi3p0hYw0nz5Eti4j676scJ95eXAJMZrgfVMysH_2RFo5zG8p2Q4oycTAzCJGn5jWujbMgIIuE6qDgAQ3NzSG4q-5EcribMpcBphEN2G_N7oCZt40h3qsVzDWIsE1auGbe_x7_8I4wdycJdKSbLZ54ZAvgQSN-x0-h1KusA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25696b8476.mp4?token=JX8OnDDgN0DthG_acn6EOQ68aK0_Tj5KfTQQslZ9tXgP3aJqqe49IH0irHD9jd3rPcFgk3ahv_CjU_d3H7OsPT_w3AgQrGIzQhb7inzEKffKU0ix6UuzVDwKRLHnvLI_-uWVmmu61AFG_m5WwG6TvF26C_pJbrY-OHxwTNbW0pyGgbTzi3p0hYw0nz5Eti4j676scJ95eXAJMZrgfVMysH_2RFo5zG8p2Q4oycTAzCJGn5jWujbMgIIuE6qDgAQ3NzSG4q-5EcribMpcBphEN2G_N7oCZt40h3qsVzDWIsE1auGbe_x7_8I4wdycJdKSbLZ54ZAvgQSN-x0-h1KusA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنرانی جنجالی مدیر تلگرام درباره نظارت جهانی و حریم خصوصی؛
کاربران در دنیای امروز عملاً بدون حریم خصوصی هستند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/665152" target="_blank">📅 00:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665151">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b76af2785.mp4?token=aLuFjvRs3XWqO8C5gGwHBQ-SqdPXvH-nXSv2hkLjl6hL6_vU6m9VGCFPQ7aSWmEyUcmd7csJdE2-McNZRUsvTSoNxWEPJmkP3n4uJimOzgLnyrXLmYN1tCb9JeyEoRpO7QicVJYEZ_J7-FDkrjbMM2wjsF17-CRGK0GOS_hP6wXGJem7xDwzCd-m39jBayWu0jTWBNsgsl73QVvM8iF03k7F46KyvpNGqnemt13-wHgQCLQC-o8ClzsP0foQyND9P2npx_8pHy3jZluA9E50PTQ9Tguw-CJjTSkCflySpc6gd5lkGl6lKQc5sFhNSjgRIk6YCoo1LOfBEZ523c2toypBe9QmXxgmOGpZilQmYY8DdMg5kNIiUX-A57wTIUh2RWMhUsuOiP2BKpkuyaLQlfC6rvpydwmi64zRL2rlR-TFMuQ_IEGhvQ9h5J9spI8NZrhcik3czXrXdYQv5UJF8LiICf2BOhGvF4bbFd-5a9AMzQvGNVf-z0sjHg8zLPEbqZpBB3PIMTwTo6LG06uyAcskWjEzTYtgEFvQuaeP1vro5215bnm9xWVWtjo8zHt0P_dV-S25vMvliBQ5cm9Rt7vltzigbTaF3P5ouldlw4xGJguw4UPrkmhD4JJZEXjtsdN6Bra_Rt2OSAJ720Z7-QxG-CN3t8RD047UQIBjPXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b76af2785.mp4?token=aLuFjvRs3XWqO8C5gGwHBQ-SqdPXvH-nXSv2hkLjl6hL6_vU6m9VGCFPQ7aSWmEyUcmd7csJdE2-McNZRUsvTSoNxWEPJmkP3n4uJimOzgLnyrXLmYN1tCb9JeyEoRpO7QicVJYEZ_J7-FDkrjbMM2wjsF17-CRGK0GOS_hP6wXGJem7xDwzCd-m39jBayWu0jTWBNsgsl73QVvM8iF03k7F46KyvpNGqnemt13-wHgQCLQC-o8ClzsP0foQyND9P2npx_8pHy3jZluA9E50PTQ9Tguw-CJjTSkCflySpc6gd5lkGl6lKQc5sFhNSjgRIk6YCoo1LOfBEZ523c2toypBe9QmXxgmOGpZilQmYY8DdMg5kNIiUX-A57wTIUh2RWMhUsuOiP2BKpkuyaLQlfC6rvpydwmi64zRL2rlR-TFMuQ_IEGhvQ9h5J9spI8NZrhcik3czXrXdYQv5UJF8LiICf2BOhGvF4bbFd-5a9AMzQvGNVf-z0sjHg8zLPEbqZpBB3PIMTwTo6LG06uyAcskWjEzTYtgEFvQuaeP1vro5215bnm9xWVWtjo8zHt0P_dV-S25vMvliBQ5cm9Rt7vltzigbTaF3P5ouldlw4xGJguw4UPrkmhD4JJZEXjtsdN6Bra_Rt2OSAJ720Z7-QxG-CN3t8RD047UQIBjPXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بازیکنان تیم ملی بعد از جام جهانی رفتن مرکز خرید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/665151" target="_blank">📅 00:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665150">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
معاون ترامپ: ایده دریافت عوارض از کشتی‌های عبوری در تنگه هرمز «بی‌نتیجه» خواهد بود.
🔹
نتانیاهو: رابطه‌ام با ترامپ «خوب» است اما اختلاف‌نظرهایی وجود دارد.
🔹
مقام یمنی: اجازه ادامه محاصره کشورش از سوی عربستان را نخواهند داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/665150" target="_blank">📅 00:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665149">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMHqyD3nxrGa6ukHCdw1bNo6oMShL4QkoMQMf6NcPRwE4G4kEN95X488po-0AMEiDzbGebrrEBQVV0mTi95QxoKZOoCbs7EW-ovQeJxFsnRhaYPiHWisXUMK3pGV4mSaj2VGlFoNR3Yhp-MQy1srE8v2WP_9DYQmsBDMdqWqBSAyp_KoppNRCB8zbdZ5A6Z3mNt1xmO0_4Kxc5RX7cVGVmsi-wSbYSes3K91jQQDN2FyZEef1-jc7FvA2DwfMZTsi-dy5-_-QxrXcRHikV6g7yO-IJwusel17GDZNzEjGrTKg-ExH6QvLSq_kr4wa_98ZOwKbNDVpYBiMFDCtLPWFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/665149" target="_blank">📅 00:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665148">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6276572559.mp4?token=PWTvIuGPdRDGvnfHNubwf1YzeiDbAMLUocwfqgkeUT1yk6sit4WWn2aEw3zLBMg0QF4tvFQxUwNcjtCQtzx1MqL-bg74aaT-WvcGp5nxfG9TTrQF7RDwGRtLPxgEMHIIz7xWsqQsRMfHePgCYhGurfqn5PrM2BMEjazKDMaC8A-kkccdaeLxV6kXErbc6tkro-QNneLLJQ_w1T8cpv4pnOA4sLTUTYohilg64_xAVNx25qmpjJ5epi3gi4_31GpLuTaVH4-Q5uEs8SaIzAVoD_i9ZANHStUJpj3KLVvkW8OkvE-zyCqJ0eNd2CqK3ZfQBTjiHtap5WQuygeIxnCl7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6276572559.mp4?token=PWTvIuGPdRDGvnfHNubwf1YzeiDbAMLUocwfqgkeUT1yk6sit4WWn2aEw3zLBMg0QF4tvFQxUwNcjtCQtzx1MqL-bg74aaT-WvcGp5nxfG9TTrQF7RDwGRtLPxgEMHIIz7xWsqQsRMfHePgCYhGurfqn5PrM2BMEjazKDMaC8A-kkccdaeLxV6kXErbc6tkro-QNneLLJQ_w1T8cpv4pnOA4sLTUTYohilg64_xAVNx25qmpjJ5epi3gi4_31GpLuTaVH4-Q5uEs8SaIzAVoD_i9ZANHStUJpj3KLVvkW8OkvE-zyCqJ0eNd2CqK3ZfQBTjiHtap5WQuygeIxnCl7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس پلیس راهور در برنامه پرچمدار: هیچ وسیله نقلیه‌ای حتی دوچرخه حق ورود به نزدیکی مراسم تشییع رهبر شهید انقلاب در تهران را ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/665148" target="_blank">📅 23:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665147">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
چه کسانی در شورای عالی امنیت ملی به تفاهم نامه ایران و آمریکا رای مثبت دادند؟
👇
khabarfoori.com/fa/tiny/news-3226858
🔹
پایان برنامه‌ رسمی مقتل رهبر شهید در نزدیکی بیت در پی تحصن تفرقه‌انگیز یک کاروان که از خارج تهران آمده
👇
khabarfoori.com/fa/tiny/news-3226744
🔹
ضرب‌الاجل دولت عراق به گروه‌های مسلح نزدیک به ایران برای خلع سلاح
👇
khabarfoori.com/fa/tiny/news-3226770
🔹
پیشنهاد بی شرمانه تهیه کننده متاهل به بیتا سحرخیز در حضور همسرش
👇
khabarfoori.com/fa/tiny/news-3226967
🔹
کشف لباس زیر زنانه طلا در بازرسی از خانه نماینده پارلمان عراق/ عکس
👇
khabarfoori.com/fa/tiny/news-3226863
🔹
ویدئوهای جذاب ما را در وبسایت خبرفوری کلیک کنید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/665147" target="_blank">📅 23:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665146">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9275accc3b.mp4?token=pnq0IALwofjDymRlRL7Ng5uR2JgRWaV8vxbtd5Vo0cklzSDnHMXm9Aj9CoZjepKe3fSqWylUNg8SxFGPgV8HV6NfWas9AIuy3mTftEDjiw5uVLcoYEf-NcIwg-7JRpXMMuBTxZgH76QmIr21t91LS8qXRjzwse2JY4OE65sD3CMGuovb0YeDUPNETAfuucocnclc3P8XguUOrHXRITbJ7rpJQ9wklzQqCUQPK8VZeSwkDhU9-8ylatXgP5Y5aD7m-Q4vXVERI-3JxEtEikfwh7Rz5JW7c6TauJ0M1gl9B5vyy88xYz_OB7K08iHxetmeveEbc9QDSwuZg4m5IvT3Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9275accc3b.mp4?token=pnq0IALwofjDymRlRL7Ng5uR2JgRWaV8vxbtd5Vo0cklzSDnHMXm9Aj9CoZjepKe3fSqWylUNg8SxFGPgV8HV6NfWas9AIuy3mTftEDjiw5uVLcoYEf-NcIwg-7JRpXMMuBTxZgH76QmIr21t91LS8qXRjzwse2JY4OE65sD3CMGuovb0YeDUPNETAfuucocnclc3P8XguUOrHXRITbJ7rpJQ9wklzQqCUQPK8VZeSwkDhU9-8ylatXgP5Y5aD7m-Q4vXVERI-3JxEtEikfwh7Rz5JW7c6TauJ0M1gl9B5vyy88xYz_OB7K08iHxetmeveEbc9QDSwuZg4m5IvT3Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتانیاهو کودک‌کش: دو بار اقداماتی در ارتباط با ایران انجام داده‌ایم؛ احتمال تکرار وجود دارد
#Demon
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/665146" target="_blank">📅 23:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665145">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
قطع ناگهانی مصاحبه قالیباف در صداوسیما
🔹
پخش مصاحبه قالیباف از شبکه خبر درحالی امشب ناگهان قطع شد که شنیده شده یکی از مدیران صداوسیما که قبلا و در پی مصاحبه جنجالی نبویان استعفا کرده و رفته بود، امروز مجددا به کار بازگشته است./ جماران
🇮🇷
✊
@AkhbareFori |…</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/665145" target="_blank">📅 23:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665144">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/137315edac.mp4?token=ol0dlbDSLX-QK0U375EKjNjEc-gv8dGOYJGm5CS8f5BfuIsw38Sm4iClV5W1W7_Dc6YjrWG2dG87-CZw3ZFWx_wEnbqcBpjHcJRp3qyvI30xrnwygyoVLCcXrF-YWGYmWuTJXTKRSzunymfOppJREtveikh51Vg9MQlJh47xyCI1SEmatalmFq1TtZxATH4LY7BgxxzN9giblRm23c1XbhbFoY0n3eD3nQMurRO8AsBOg3aaf0Tgcs7W1odBUAeqLxTdbg6pZ8CmU3spPYj7yN3s2nFGQdztSaNLpOUoH0ZmPgkxX-uRAy4bfEHioUjeI8MRZaT0PiUy0Glhm1gONg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/137315edac.mp4?token=ol0dlbDSLX-QK0U375EKjNjEc-gv8dGOYJGm5CS8f5BfuIsw38Sm4iClV5W1W7_Dc6YjrWG2dG87-CZw3ZFWx_wEnbqcBpjHcJRp3qyvI30xrnwygyoVLCcXrF-YWGYmWuTJXTKRSzunymfOppJREtveikh51Vg9MQlJh47xyCI1SEmatalmFq1TtZxATH4LY7BgxxzN9giblRm23c1XbhbFoY0n3eD3nQMurRO8AsBOg3aaf0Tgcs7W1odBUAeqLxTdbg6pZ8CmU3spPYj7yN3s2nFGQdztSaNLpOUoH0ZmPgkxX-uRAy4bfEHioUjeI8MRZaT0PiUy0Glhm1gONg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این بار هوش مصنوعی زودتر از انسان واکنش نشان داد؛ عملکرد تحسین‌برانگیز تسلا مقابل آمبولانس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/665144" target="_blank">📅 23:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665143">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
ونس: تاکتیک مذاکره ایرانی را درک نمی‌کنم
🔹
ما خواهان تعهدات پایدار هستیم که قابل‌تأیید باشند و با بازرسی‌هایی پشتیبانی بشن که ایران، کل کشورش رو از سلاح هسته‌ای پاک می‌کنه
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/665143" target="_blank">📅 23:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665142">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f386220b.mp4?token=UH08RvY1Y8pg7uwlgBzPBPRs5U54IV89vuGSjJOvMGtRzKpAMcPz_aGFb9IFri3NhztLDB4uuwaI9VphOZRLxCTCG2VMqGQWB26izyhzBYCe5JorrGHsI9V9O067_qAzGdHFgt5jtVNKy_IjoJWIdbB5Sl0bHm1lMk-QF3FoySj6CVOvtJhccjK4DDzJhNBh8m3S8N_WgF00ICREA2kx8wM7HEb411TWSjJh7iuhiHRYH0n9Gz_drjJf_OrW-vfGsxAqVnoYj3QBXwIiJvLtbKk41sSTWIobnxFej_P-y9G2NZg7rsiaQRXwTF_W0GftlAWENy7Zs6jZXSbvzTyXHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f386220b.mp4?token=UH08RvY1Y8pg7uwlgBzPBPRs5U54IV89vuGSjJOvMGtRzKpAMcPz_aGFb9IFri3NhztLDB4uuwaI9VphOZRLxCTCG2VMqGQWB26izyhzBYCe5JorrGHsI9V9O067_qAzGdHFgt5jtVNKy_IjoJWIdbB5Sl0bHm1lMk-QF3FoySj6CVOvtJhccjK4DDzJhNBh8m3S8N_WgF00ICREA2kx8wM7HEb411TWSjJh7iuhiHRYH0n9Gz_drjJf_OrW-vfGsxAqVnoYj3QBXwIiJvLtbKk41sSTWIobnxFej_P-y9G2NZg7rsiaQRXwTF_W0GftlAWENy7Zs6jZXSbvzTyXHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعلام وضعیت اضطراری پس از خروج قطار از ریل در آمریکا
🔹
یک قطار در نزدیکی منطقه «فیسترول» در ایالت پنسیلوانیا از ریل خارج شد که به دلیل نگرانی از نوع محموله، وضعیت اضطراری اعلام شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/665142" target="_blank">📅 23:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665140">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I7smrcg9rLgnJBibWyf8MYVxtQTgXP-L05GjCVNzWyfvMhYsC-c2wRcNKJTotgxgogm1JMZDWQrHk1g1HfOuIWALbcdsqoJgByNqRKuchwwXAqjA6Vzep7AW98JQWGwLzpnneHHi6p6B-JPI52Rujc6rcrlDgBHBJz-Pt7LD591IYsO3s6ztjcdnD-dyE6u8ANDzQhqdQStTBrn6pYwSlVIHzuizRM2yvUDdjPfbm40Gxi6k6Bud9jzGkT_Doji8W3g1B3gZcO24OL8Ww4Mrefaf1581oa_Cp5GlJtAS70JgQUyFjWGoWlsGCmhRD8htmu1YZYofMkAVvr1Sm66ESA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BsmypDGgjp1962ofOxlFPMqnTIyeoe_7UTWXdRkvFospgBhU6iS3Dj9tqUuv5rZZ7GFBI3Rnw_8ZzkJ6vO3t22qCR2x977RiEQH7wPQVIXyeXYQuEY2biryZlYCCU5l1jGKtOT44FN1ztYW6myOWr-xync9AfU0qGevK4QtfVVts1wiuukXNL-CloDC8wa38IRDDOJ2PtvWF2PD4iJdeFsJ5uRPW4MvC27bPuNK8cnTsEViAdgYBo22FQ7kBjINlaonDnEH1eAy-x0YfG1kG_j8KIURiYAg6Y2RppsXa2V64DH4XFRUgG85q1VgGExNCkDRCsU0UVk_zmxI031WAVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">چه کشورهایی بیشترین ظرفیت تولید انرژی از زباله را دارند؟
🔹
چین و ژاپن از پیشتازان تبدیل زباله به انرژی در جهان هستند.
🔹
در اروپا نیز کشورهایی مثل بریتانیا، نروژ و سوئیس با توسعه زیرساخت‌های بازیافت و انرژی‌سوزی، سهم بالایی در مدیریت زباله دارند.
🔹
در ایران، سهم تبدیل زباله به انرژی کمتر از ۵٪ است و هنوز در مراحل اولیه توسعه قرار دارد.
@amarfact</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/665140" target="_blank">📅 23:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665139">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
اعتراض آیت‌الله مدرسی یزدی به بازگشایی اینترنت بین‌الملل بدون ملاحظات کارشناسی
🔹
عضو فقهای شورای نگهبان با انتقاد از بازگشایی اینترنت بین‌الملل بدون بررسی کارشناسی، این اقدام را تهدیدی برای امنیت، اقتصاد و سلامت روان جامعه دانست و هرگونه تصمیم در این زمینه باید صرفاً از مجاری قانونی و با نظر متخصصان متعهد اتخاذ شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/665139" target="_blank">📅 23:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665138">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1AduajvwcSXScrt8KcY9boXYqWZYPrTyXlsyzElVv8c-dckRBQWQJ54p-cnAQBk7p3knYlRl3mYrZgpvYrCuSVcGYvdG2o0l4tu4J8BmqELRA94n4Wpm24bf-Wp1dyn815BBFVIHNwwnDknmR05esnXGZkN0M0VxmprEl6jyXgYRv2TNZjAFE6Sig0sm789M8OJzwbcrCKFcy_XbY3Gb7LBbeje0X2wOtD7OGEOOE745XBN6zhieO6zg2dQ31ZkfsBCKGTZa51Nuc33E4hu21M2XE3IMzYsRiWHLeKp8UmtBFVXD9tSIAahws1NwZk_Kl7AfLMv8CPOFnNy2ILDiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویر خبرفوری از روند آماده‌سازی مصلی تهران برای تشییع «رهبر شهید انقلاب» #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/665138" target="_blank">📅 23:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665137">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
نتانیاهو: رابطه من با ترامپ بسیار خوب است، اما در دیدگاه‌ها تفاوت‌هایی وجود دارد
#Demon
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/665137" target="_blank">📅 23:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665136">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e795bbab88.mp4?token=N55SqugbSJqLjFxFChMj7lJ3CcLpYxGk_njMFinwgjX9XyJ1TfRuIYxPdDmVHVbvGBEoHjlImK-xkPM3XQqMz-Hn86R41XQ-dD5gU4tMuXk8dCGq9HIG-RC_h-QZnEg4dnMvAJ-pV5UmHjxh3rWK1A3gtGGnJNekEbn4C1hhhBUo2h5J-jpmgIQDSnj-pW7uoNPPCumq85ULKN-tyvKCsiEvsWUeSG4fuSsACh6iZxpul6eiXNrovfA6IPfFzJodreDMmh3z6gBpMjAcmTS8VOFQFUz42GrmSFn0xJ24IMpoV6GWSppT4mfDFnef3gV6Gr1t5NEgzvyTbLTN2rZtTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e795bbab88.mp4?token=N55SqugbSJqLjFxFChMj7lJ3CcLpYxGk_njMFinwgjX9XyJ1TfRuIYxPdDmVHVbvGBEoHjlImK-xkPM3XQqMz-Hn86R41XQ-dD5gU4tMuXk8dCGq9HIG-RC_h-QZnEg4dnMvAJ-pV5UmHjxh3rWK1A3gtGGnJNekEbn4C1hhhBUo2h5J-jpmgIQDSnj-pW7uoNPPCumq85ULKN-tyvKCsiEvsWUeSG4fuSsACh6iZxpul6eiXNrovfA6IPfFzJodreDMmh3z6gBpMjAcmTS8VOFQFUz42GrmSFn0xJ24IMpoV6GWSppT4mfDFnef3gV6Gr1t5NEgzvyTbLTN2rZtTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
قلعه‌نویی
:
ما نرفتیم مرحله بعدی ولی کلی دست آورد بدست آوردیم اینم عزتی بود که خدا به ما داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/665136" target="_blank">📅 23:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665135">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
به خاطر مشکلات سیاسی با منِ قالیباف، حقوق ملت را از بین نبرید
🔹
کسانی که حرف ترامپ فاسق را قبول می‌کنند، یک‌بار هم حرف برادر دینی خود را بشنوند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/665135" target="_blank">📅 23:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665134">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
قسمت هشتم مستند احیا و حقیقت | ایران امام رضا(ع)
✅
بعضی نجات‌ها را نمی‌شود با اعداد و محاسبات توضیح داد...
🔹
آن روز، میلیاردها ترکش آهنین، آسمان و زمین را شکافتند. هزاران کارگر در سایت های فولاد خوزستان حضور داشتند و هر پیش‌بینی، از وقوع یک فاجعه حکایت…</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/665134" target="_blank">📅 23:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665133">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e21f427ab.mp4?token=ijCKeino_14_N1G2YPaMoaOrUjlk8ARXtaopz_HSyc2-muMwa6n1fiHauJ9UBxh3Ojl3Rg_R_jE2CwhDmN253wdeW1-u0cNsu9pAcYTqYMRw0s0dVVLP53HqQI3ylIO9ld2FHJmeGjJipamoPsScIDNWu5r3NLDKEH1xhLLxly-lVFcAVmV8EhkMQNyXRB_1AYa4bn3sYEd7xDB9HRSMjYjBcvNhEvMIys8tYr0o3QhOAhAUueN3ovl3pybd8CeHzDMRdQI6j_WIOVF_f6i0q9r5fYOzZ3OBxMfCmLg8r784eLxcIwqfpfD0D4f-y8FRzmN3socLq1DQKPr78byCCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e21f427ab.mp4?token=ijCKeino_14_N1G2YPaMoaOrUjlk8ARXtaopz_HSyc2-muMwa6n1fiHauJ9UBxh3Ojl3Rg_R_jE2CwhDmN253wdeW1-u0cNsu9pAcYTqYMRw0s0dVVLP53HqQI3ylIO9ld2FHJmeGjJipamoPsScIDNWu5r3NLDKEH1xhLLxly-lVFcAVmV8EhkMQNyXRB_1AYa4bn3sYEd7xDB9HRSMjYjBcvNhEvMIys8tYr0o3QhOAhAUueN3ovl3pybd8CeHzDMRdQI6j_WIOVF_f6i0q9r5fYOzZ3OBxMfCmLg8r784eLxcIwqfpfD0D4f-y8FRzmN3socLq1DQKPr78byCCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این ویدیو از ذوق‌ زدگی این دختر کوچولو بعد از گرفتن کادوهای تولدش، حسابی تو اینستاگرام وایرال شده
🔹
به قدری بازدیدش خوب بوده که در کمتر از یک روز، بیشتر از ۱۰ میلیون ویو در اینستاگرام داشته!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/665133" target="_blank">📅 23:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665132">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c252ff6209.mp4?token=MD8T9t9yH5J6Aqjp2KxLvyK4-9DyKnQ5y48_bxIJQAejMVWstWZjET-Cyut3cHD1EMnqLwyxifUbcJx6CJpo4ztnr77paIvwzRX-XS9h31x89sBTeyptdRWfZ9BXaQJnhDkVePzEJJ7aoDSGuwqiogYO5904CzGQ8D920LB8L-4xTNxyKA_L6KosZby4KfWySyY6WObn5UXPv6fyGIrwGLQ5jFZdl6E59OwApo0UMftwfa-tdMzJ-HREg8Wq8QosEyLSKjCyRPdmVrzFrS5mPlQSMsZ06EYlGv0OWUexB3-iYVwcoGji4GwXz8chnOBlH2x7hX6WL0UjgaMhzmtwSFCDFRPRP6f6CfZlBsVW_g_zgX6cLfp85ofbZQvjhiaUrcFUx5vsuVDThDhIlVEAtv69uqlBZVdHX0CN4ImRVKAxigj1aKkJtTFC2vRFaIKgpLsQytjq-RpjHf-KQRTqHM0qcL06wXR_Y2nfvAwBfl0nhQC09nNu6GXlmDW47jE7x88AIIWwzz0_l81O-Fpc7vjJACNQamGFe4o-hEulNkWNLFjPIQJl95f4lFcpu5p2tGIyHbu5wxEy6giIA_Wb0pvguCe5O7en8Vd2nQTownoEOkl6qeD95cyMGoNipFz1mikjI26_H6Gk5StmhwayfK3Phai9qzoODD2ZgKHts7o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c252ff6209.mp4?token=MD8T9t9yH5J6Aqjp2KxLvyK4-9DyKnQ5y48_bxIJQAejMVWstWZjET-Cyut3cHD1EMnqLwyxifUbcJx6CJpo4ztnr77paIvwzRX-XS9h31x89sBTeyptdRWfZ9BXaQJnhDkVePzEJJ7aoDSGuwqiogYO5904CzGQ8D920LB8L-4xTNxyKA_L6KosZby4KfWySyY6WObn5UXPv6fyGIrwGLQ5jFZdl6E59OwApo0UMftwfa-tdMzJ-HREg8Wq8QosEyLSKjCyRPdmVrzFrS5mPlQSMsZ06EYlGv0OWUexB3-iYVwcoGji4GwXz8chnOBlH2x7hX6WL0UjgaMhzmtwSFCDFRPRP6f6CfZlBsVW_g_zgX6cLfp85ofbZQvjhiaUrcFUx5vsuVDThDhIlVEAtv69uqlBZVdHX0CN4ImRVKAxigj1aKkJtTFC2vRFaIKgpLsQytjq-RpjHf-KQRTqHM0qcL06wXR_Y2nfvAwBfl0nhQC09nNu6GXlmDW47jE7x88AIIWwzz0_l81O-Fpc7vjJACNQamGFe4o-hEulNkWNLFjPIQJl95f4lFcpu5p2tGIyHbu5wxEy6giIA_Wb0pvguCe5O7en8Vd2nQTownoEOkl6qeD95cyMGoNipFz1mikjI26_H6Gk5StmhwayfK3Phai9qzoODD2ZgKHts7o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قهرمانان واقعی کشور ...
🔹
این فقط چند جمله نیست؛ روایتی است از نگاه رهبر فرزانه شهید به قهرمانان واقعی این سرزمین.
🔹
حرف‌هایی که شاید ماه‌ها گفته شد، اما امروز بیش از هر زمان دیگری معنا پیدا کرده است. این ویدئو را ببینید و بشنوید قهرمان واقعی از نگاه او چه کسی بود.
#بدرقه_یار
@TV_Fori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/665132" target="_blank">📅 23:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665131">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75b314ee9d.mp4?token=MU5YDFwPvvCmwaFjXw8NFUWB2Pq9NPGmMXFD3rHQU2vSlL9iVK9g-F1_N5lDmQYXiM_hNuLbhh8mbWVDz_i5xALbORWOJa63hilZ2lYnjdyIucSEUWhjBsyWClYDfKmMHsqmwxbUxFkY_fyE0pMC95RXza6HixUvmdN8Rba4zE76VaC4Dbb4x3kv3Rd8fwhQR0k11YewV1jrlcBuoBuyfNLBjWiX6GEoCmAyGrxvhGT122j8vJUS6j5KeTb-RXCI99begTFr4P_-8UhawAUq12Vtp5uj1xvS_IsHiaGp7Ss0TjHGHAztvr7Cr8TIgroJE0quDo-3pmn1Y1fsIHpjYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75b314ee9d.mp4?token=MU5YDFwPvvCmwaFjXw8NFUWB2Pq9NPGmMXFD3rHQU2vSlL9iVK9g-F1_N5lDmQYXiM_hNuLbhh8mbWVDz_i5xALbORWOJa63hilZ2lYnjdyIucSEUWhjBsyWClYDfKmMHsqmwxbUxFkY_fyE0pMC95RXza6HixUvmdN8Rba4zE76VaC4Dbb4x3kv3Rd8fwhQR0k11YewV1jrlcBuoBuyfNLBjWiX6GEoCmAyGrxvhGT122j8vJUS6j5KeTb-RXCI99begTFr4P_-8UhawAUq12Vtp5uj1xvS_IsHiaGp7Ss0TjHGHAztvr7Cr8TIgroJE0quDo-3pmn1Y1fsIHpjYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت حداد عادل از سفره جمع کردن آقا مجتبی!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/665131" target="_blank">📅 23:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665130">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24b10c272e.mp4?token=nsRgaq7TUqd-41NjUAKtSz4mlZaH1BpDRzOXNqF5Nhyvo88s4R1l-srcH40BuvjmJWxhPKuK_ySIJ-TiydyGyQbQCQRJNVweZiR9fOgtyNcYhAD1gEYZhOdVP0qgpG7j0JStckLGVUDQH4W1NljGNDikb94OYITXQt3nwerLSMhBuc3JWbVu7b3kdzfvssmhf72tG7E45U6mIx3paYLF9UQfOxmfaJYB9wgkqYx2U1iEA7uv7M1E0iNJuobYAlV4uFMrtSvNr_-3eUSu32t0NaDXku0jmGhi89ptcuhEsjb-xxEH8vWPHrruH3eEn2lWNaWw5y9CHH9txvjnfmeBTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24b10c272e.mp4?token=nsRgaq7TUqd-41NjUAKtSz4mlZaH1BpDRzOXNqF5Nhyvo88s4R1l-srcH40BuvjmJWxhPKuK_ySIJ-TiydyGyQbQCQRJNVweZiR9fOgtyNcYhAD1gEYZhOdVP0qgpG7j0JStckLGVUDQH4W1NljGNDikb94OYITXQt3nwerLSMhBuc3JWbVu7b3kdzfvssmhf72tG7E45U6mIx3paYLF9UQfOxmfaJYB9wgkqYx2U1iEA7uv7M1E0iNJuobYAlV4uFMrtSvNr_-3eUSu32t0NaDXku0jmGhi89ptcuhEsjb-xxEH8vWPHrruH3eEn2lWNaWw5y9CHH9txvjnfmeBTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
پوستر فراگیر در ژاپن؛ پیام تند زنان ژاپنی به مردان: به‌جای ریاکاری، خانه خودت را تمیز کن
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/665130" target="_blank">📅 23:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665129">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/772d1c33e9.mp4?token=kGW2xDKBA8NaAz3qYFyzZiT-MJ2r-zR5qBkqKuErRHmakTDkyjQMjtkuGdle-j3mxKJGKFXPBlYZBVfCr1qsz7JZzcYQJY4_BfSGz0XrVLnoYYDdu9MJxK-8YfAhTVD17jY2sstcyExy3-cXYy6Y1OhsTSRcjIcUUkxwCl8jgQLucw-DsNIaCOoaZtKTN4WPsmGPdVqTlot1t_5cHveh0fafn7L90ld5k1DAarJUD-rhnBgrGPlw9QgwNgC_kY0xKKtsCkY45kFGwAxfZJNbIN5GXc_z5k5souXvSISdUlUlH_nEc4GE-Pe9RxPA9A8m-llJF4ZRAIte7EC1UmnqDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/772d1c33e9.mp4?token=kGW2xDKBA8NaAz3qYFyzZiT-MJ2r-zR5qBkqKuErRHmakTDkyjQMjtkuGdle-j3mxKJGKFXPBlYZBVfCr1qsz7JZzcYQJY4_BfSGz0XrVLnoYYDdu9MJxK-8YfAhTVD17jY2sstcyExy3-cXYy6Y1OhsTSRcjIcUUkxwCl8jgQLucw-DsNIaCOoaZtKTN4WPsmGPdVqTlot1t_5cHveh0fafn7L90ld5k1DAarJUD-rhnBgrGPlw9QgwNgC_kY0xKKtsCkY45kFGwAxfZJNbIN5GXc_z5k5souXvSISdUlUlH_nEc4GE-Pe9RxPA9A8m-llJF4ZRAIte7EC1UmnqDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به خاطر مشکلات سیاسی با منِ قالیباف، حقوق ملت را از بین نبرید
🔹
کسانی که حرف ترامپ فاسق را قبول می‌کنند، یک‌بار هم حرف برادر دینی خود را بشنوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/665129" target="_blank">📅 23:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665128">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14b449e24d.mp4?token=RTAOehEbX4a93aTVLX-8pXQYbQri40lWVzGDPkxVtUkPt46QtBsAVVRqlk46gwGPZXZVttZVho9fJT0J_VZyFpVUL67Y4cC-Q_8BHOEB6WGBRur7vaYJaWH5wgPElNfPNZAMrIfKy_Plak098u8BuecM6ZOJVLet-vfq4Ch_6tZP7dh2T21oVcJ9pmnTBZSkt3qzj1dMAejN2UUfy7FeOYZJYEkfGRP6dRaIvbpn2Ti8smg9_IHogy33UekMdb0YKtV-NABu8hqTxNXQwEYqIx5NNSp7hIRxmV8TNRArmh5ILTxpmayrBVWWSN2D-6oFPtogndwQdWSym6K2IG_ynA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14b449e24d.mp4?token=RTAOehEbX4a93aTVLX-8pXQYbQri40lWVzGDPkxVtUkPt46QtBsAVVRqlk46gwGPZXZVttZVho9fJT0J_VZyFpVUL67Y4cC-Q_8BHOEB6WGBRur7vaYJaWH5wgPElNfPNZAMrIfKy_Plak098u8BuecM6ZOJVLet-vfq4Ch_6tZP7dh2T21oVcJ9pmnTBZSkt3qzj1dMAejN2UUfy7FeOYZJYEkfGRP6dRaIvbpn2Ti8smg9_IHogy33UekMdb0YKtV-NABu8hqTxNXQwEYqIx5NNSp7hIRxmV8TNRArmh5ILTxpmayrBVWWSN2D-6oFPtogndwQdWSym6K2IG_ynA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: باید فشار اقتصادی را از روی دوش مردم برداریم؛ ما این کار را با عزت انجام دادیم و این سند شکست آمریکاست
🔹
بر اساس این تفاهم‌نامه، از مجموع ۲۴ میلیارد دلار دارایی ما در کشورهای مختلف، قرار است ۱۲ میلیارد دلار در اختیار بانک مرکزی قرار بگیرد تا هر…</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/665128" target="_blank">📅 23:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665127">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
قالیباف: عبور از تنگه بدون هزینه فقط برای ۶۰ روز است
🔹
ایران تحت هیچ شرایطی از حقوق خود در تنگه هرمز کوتاه نمی‌آید.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/665127" target="_blank">📅 22:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665126">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00a1121f6c.mp4?token=RyrY6PJ3o7REdw5w8e3PCauSwuOG1dZPGuLkvz_7Ys3RURTbHNRPIfp7n1qqZPvfmNMSfyvjW_UiyiF7g3I7XXTcRkI2o4o_apOTopLKcXycRosiWGjqWOCqOcjb6dTlcqqZ6__FhDbNy42cDFhQixsC-uEuRsSiTybHhMe88oXfGPEZy0EuuiJc3DssPWMr4Ws2O-bDNfwR9cIUd_EntTdfIHcpyLXm_sXWWxLoAXJ4kCg8aDUbGVwhwuLeEmck7O1EkssOYu2IdHMQ6v3d409nPQZFvwO96uIGYxd2FM7UNVQoN_qZ9e5e7LYJHmxOJ--0Iu5XKKDqZTZjHXFmyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00a1121f6c.mp4?token=RyrY6PJ3o7REdw5w8e3PCauSwuOG1dZPGuLkvz_7Ys3RURTbHNRPIfp7n1qqZPvfmNMSfyvjW_UiyiF7g3I7XXTcRkI2o4o_apOTopLKcXycRosiWGjqWOCqOcjb6dTlcqqZ6__FhDbNy42cDFhQixsC-uEuRsSiTybHhMe88oXfGPEZy0EuuiJc3DssPWMr4Ws2O-bDNfwR9cIUd_EntTdfIHcpyLXm_sXWWxLoAXJ4kCg8aDUbGVwhwuLeEmck7O1EkssOYu2IdHMQ6v3d409nPQZFvwO96uIGYxd2FM7UNVQoN_qZ9e5e7LYJHmxOJ--0Iu5XKKDqZTZjHXFmyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ونس: تاکتیک مذاکره ایرانی را درک نمی‌کنم
🔹
ما خواهان تعهدات پایدار هستیم که قابل‌تأیید باشند و با بازرسی‌هایی پشتیبانی بشن که ایران، کل کشورش رو از سلاح هسته‌ای پاک می‌کنه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/665126" target="_blank">📅 22:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665125">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcNYYWrbFpR44irP8rhU6zysGvObG7sHyDW-d7rEuXWwoRW4CcDy5ZizUxlEBLoJ9YPnB8qPP6tlq7GHwZc2Rad7iBsX0bEMOosmEHOBvDByHbptsJhCdEZK2FSWg22RS3FJS2pg9nl-aBPpneipZBRRM17O8Pix00bot6NcLA9JrZc1c0oUQAoGdbhjq0VsZHschr7B0bvhXpUZvaIkRoZ0vmlK5eO8oTWv2r-zGid5_y0I0Nsy2tIaB5iHpOCkfMnReZfOyRcfyn3XH8qhto6W26c7d1phMhiuEwa5BLLxzTbpVrk5kFyHKXHG4pre0DLH12m31f15QGc1Q-5Tag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کسی که عدالت را پایمال کند، روزی در برابر آن خواهد ایستاد
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/665125" target="_blank">📅 22:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665124">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/554e01cd3d.mp4?token=To-pwVz5-8dsSclSP8AZjuwXYsM2PBbeZ1i784JTD8FmlMAc8HdzQM8mg5jwPa5cKP-K_Le5U4hYBS0WvbV5gmB7yERwR2e2hTI10M3JdIBPwjv96bDbFxscqGKBISMWdMyjD71YeNF1MNeNfYZ9d_jKg34bsCybhcXDqZbMbEGuE1-cDiFSbqsJ47C-RE5q-iDtPggWxiD_tXHeKhYkkGuziGjMR25csa4Cz_NWJlTJK8rU4lRnuyMUqdZKy4vbbJuZeBs7gsdQcMWBJJUSLpT1XgTnEHpUZcsfvyqV-_i3hGnyKn0JI7SIfL6s7Kjbgroy-euUZc8V1dmHboCyZiXk4J57TU7mPPikOgE34r2SSzeIDwmopAIJLoP-rVrZ2PZkdrsMnAQgjxTfRf2h3GI3x0eoRjdE8be7PZQUz1N9vzw0WbsRHOBCFWs_0Pi-4w0ek0Weidyp2jXxL69BgLEJxF3LK36nAv67B065A16o_oA-JK8UgJEEE0WEPP2HJXcXcAihO2L8iHq5L3xJ-im95OIwy9-M8i4miMCW2Q2jMkPobzdY6vK79c3PEdTFH52KKcK1QZl5l7aTEQh0GIPGn4yVNB9z1EbliRWl-4pb2w8V51y-z_sYwO7irdiejHj4niN9fcUDPpDBz1eqWeWrSFYjDvg9P1XoibPmsVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/554e01cd3d.mp4?token=To-pwVz5-8dsSclSP8AZjuwXYsM2PBbeZ1i784JTD8FmlMAc8HdzQM8mg5jwPa5cKP-K_Le5U4hYBS0WvbV5gmB7yERwR2e2hTI10M3JdIBPwjv96bDbFxscqGKBISMWdMyjD71YeNF1MNeNfYZ9d_jKg34bsCybhcXDqZbMbEGuE1-cDiFSbqsJ47C-RE5q-iDtPggWxiD_tXHeKhYkkGuziGjMR25csa4Cz_NWJlTJK8rU4lRnuyMUqdZKy4vbbJuZeBs7gsdQcMWBJJUSLpT1XgTnEHpUZcsfvyqV-_i3hGnyKn0JI7SIfL6s7Kjbgroy-euUZc8V1dmHboCyZiXk4J57TU7mPPikOgE34r2SSzeIDwmopAIJLoP-rVrZ2PZkdrsMnAQgjxTfRf2h3GI3x0eoRjdE8be7PZQUz1N9vzw0WbsRHOBCFWs_0Pi-4w0ek0Weidyp2jXxL69BgLEJxF3LK36nAv67B065A16o_oA-JK8UgJEEE0WEPP2HJXcXcAihO2L8iHq5L3xJ-im95OIwy9-M8i4miMCW2Q2jMkPobzdY6vK79c3PEdTFH52KKcK1QZl5l7aTEQh0GIPGn4yVNB9z1EbliRWl-4pb2w8V51y-z_sYwO7irdiejHj4niN9fcUDPpDBz1eqWeWrSFYjDvg9P1XoibPmsVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: عبور از تنگه بدون هزینه فقط برای ۶۰ روز است
🔹
ایران تحت هیچ شرایطی از حقوق خود در تنگه هرمز کوتاه نمی‌آید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/665124" target="_blank">📅 22:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665123">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
‌ قالیباف: وقتی می‌توانیم گره‌ای را با دست باز کنیم آیا ضرورتی وجود دارد که آن را با دندان باز کنیم؟
🔹
بعد از سفر ما به سوییس حجم آتش‌ها و درگیری‌ها و شهدا در لبنان سیر نزولی داشته است. البته هنوز اشکالاتی وجود دارد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/665123" target="_blank">📅 22:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665122">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOjFxBHxM_uKCERe3yVe1sctzC7J72vKKLY9WSQl26NiruXhFSyLODCCVNCIbEvwfD_-O1Cp1q2czF6Ql0zaSxBEPqZRmTdAqHZz6npoA-EwzdJi6X5bAEugmpa1K_zUHXug6xZGoX0muM-ECMDMfg4-AsaIqpGxAHqPnXyqmjoUUyLVzpgUsRKU7D3dKKI6lr9SQJJVmog1DF8dYg5FkMnVbi820p95VSlPSTbaDDxb-uUPk-_fQ7B2LbUsyY1qaBJdiz0fsSOnhfo_7LMTlIoSg2AZEx_iEgfyFZsAZ4W008iLaEfN9Sc98nRqbuSgv5e2fm5f8cZ1HwSFdyn-Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راه کج
🔹
تنگه هرمز امروز فقط یک آبراه نیست، مهم‌ترین برگ برنده ایران در معادلات منطقه‌ای و مذاکرات با آمریکاست. به همین دلیل، تلاش برخی بازیگران برای سپردن مدیریت یا امنیت این گذرگاه به طرف‌های دیگر، صرفاً یک اقدام دریایی نیست، بلکه تلاشی برای تضعیف اهرم راهبردی تهران است. در این میان، استفاده از ظرفیت عمان یا ایجاد شکاف میان تهران و مسقط نیز می‌تواند بخشی از همین سناریو باشد، زیرا هر اختلافی میان دو همسایه، مسیر اجرای طرح‌های ضدایرانی را هموارتر می‌کند. واقعیت این است که امنیت پایدار تنگه هرمز با حذف ایران به دست نمی‌آید. راهی که بر نادیده گرفتن نقش تهران و ایجاد شکاف میان همسایگان بنا شود، همان راه کجی است که سرانجامی جز بن‌بست نخواهد داشت.
🔹
هفتصدوهشتادوهفتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/665122" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665121">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
مروری بر سیره حکمرانی قائد شهید انقلاب؛
«به یاد اویی که ما را صاحب‌خانه می‌دانست»
🔹
بزرگ‌ترین تفاوت رهبری با خیلی از مسئولان، در یک کلمه خلاصه می‌شد: «باور به مردم». در سال‌هایی که خیلی از پشت‌میزنشین‌ها تصور می‌کردند حکمرانی یعنی نوشتن بخشنامه‌های پیچیده و جلسات طولانی، او دقیقاً در نقطه مقابل ایستاد و بارها خط بطلان کشید روی این تفکر که «مردم متوجه پیچیدگی امور نمی‌شوند و باید کار را به مسئولین سپرد.»
🔹
او اقتصاد و فرهنگ را زمانی موفق می‌دانست که کلیدش دست خود مردم باشد، نه در انحصار حلقه‌های بسته مدیریتی. او معتقد بود در یک نظام اسلامی، مسئولان چیزی جز خدمتگزار مردم نیستند و مشروعیتشان به میزان گره‌گشایی از کار مردم بستگی دارد. در منطق او، نقد منصفانه و جریان دائمی نظارت مردم بر کارآمدی مسئولین، نه یک تهدید برای امنیت ملی، بلکه تضمین‌کننده‌ی سلامت نظام بود.
🔹
رهبری که می‌شناختیم، تا آخرین روزهای حیاتش به ما یادآوری کرد که هیچ حکومتی بدون تکیه بر آگاهی و حضور مردم، عاقبت‌به‌خیر نخواهد شد.
🔹
میوه و ثمره‌ی این نگاه او به مردم، خود را در روزهای سخت ابتلا نشان داد؛ آنجا که این باور او، به «بعثت مردم در جنگ» ختم شد و همین حضور بی‌دریغ آحاد مردم در میدان بود که سپر بلای کشور شد و ثبات و امنیت کشور را حفظ کرد. از همین روست که امروز، خط‌کش سنجش هر مدیری در نظام اسلامی، میزان وفاداری او به این میراث بزرگ است.
شیخ محسن رمضانی
دبیر نهضت مردمی بعثت خون
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/665121" target="_blank">📅 22:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665120">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9174733cfd.mp4?token=PxQpLOJ1a4isBdai3f3Fh_9RsgsU-aw8XKgEOsnmxII1gwOhG9hR3y4APRwdUFvpDze7VjVPISRzlGS8wt9fQUkZCaxKOKDJtdTeMkjllohXst5jOKlwLX_oSlUrFscw4vz50A-VV25lCjMkTCaMUlosekhwjNLoYKEmzNC-hljTnMItNL0d6yYT2HpYpe0SuAfM_rZCbSbxVatvsccQRuZ6BIBhlajzOFtSohyFuA8SwsmivqGs-RW6hs2Bocf7NPNvp59ulT4KAa-MbHpc0uaWpTYRu_C_YnMABnN_jBAipX0_NHBbyQNP4jC73rw407_SV1E7wqgRoWPkzm-K9DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9174733cfd.mp4?token=PxQpLOJ1a4isBdai3f3Fh_9RsgsU-aw8XKgEOsnmxII1gwOhG9hR3y4APRwdUFvpDze7VjVPISRzlGS8wt9fQUkZCaxKOKDJtdTeMkjllohXst5jOKlwLX_oSlUrFscw4vz50A-VV25lCjMkTCaMUlosekhwjNLoYKEmzNC-hljTnMItNL0d6yYT2HpYpe0SuAfM_rZCbSbxVatvsccQRuZ6BIBhlajzOFtSohyFuA8SwsmivqGs-RW6hs2Bocf7NPNvp59ulT4KAa-MbHpc0uaWpTYRu_C_YnMABnN_jBAipX0_NHBbyQNP4jC73rw407_SV1E7wqgRoWPkzm-K9DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محمدصادق شهبازی، دبیر سابق جنبش عدالت‌خواه دانشجویی: پسر پیغمبر رو وسط تهران زدن، باید انتقام خون رهبر رو بگیریم، رهبر رو با درهم و دینار معاوضه نمی‌کنیم
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/665120" target="_blank">📅 22:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665119">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
‌
قالیباف: وقتی می‌توانیم گره‌ای را با دست باز کنیم آیا ضرورتی وجود دارد که آن را با دندان باز کنیم؟
🔹
بعد از سفر ما به سوییس حجم آتش‌ها و درگیری‌ها و شهدا در لبنان سیر نزولی داشته است. البته هنوز اشکالاتی وجود دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/665119" target="_blank">📅 22:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665118">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7178bd3b8.mp4?token=uagIDhQpfp75ASqWTJQFSp3iwOkFQNSC3j2T3LM0Bgnjo2Lzrbyaun0phG-E3ESt_CzXfSy0Pp9ZoBQ6mtPr9upI3QktGo2Aahg1cq-E7zN-0rs6F4fJ3iUhfJ2fQxnMRgZ6wtIpCh5W4y04bL8JSZ39fLgbEuVsJune-IPYER3e0jJM9KGMV1W-Vysow808-WLAcplv8RktGjSXqE9D-xiJzIQP8EogRsMS4JGdUwOOkGMnhTbpfrE37lePi40Xo_-sChiBro8pIldzBxYcB1fAd8U9z6krlPFnVGmt1GIT8f4CL9CeLwpnEDySdiYYS4gYyikB97yjlCc3Z9VMJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7178bd3b8.mp4?token=uagIDhQpfp75ASqWTJQFSp3iwOkFQNSC3j2T3LM0Bgnjo2Lzrbyaun0phG-E3ESt_CzXfSy0Pp9ZoBQ6mtPr9upI3QktGo2Aahg1cq-E7zN-0rs6F4fJ3iUhfJ2fQxnMRgZ6wtIpCh5W4y04bL8JSZ39fLgbEuVsJune-IPYER3e0jJM9KGMV1W-Vysow808-WLAcplv8RktGjSXqE9D-xiJzIQP8EogRsMS4JGdUwOOkGMnhTbpfrE37lePi40Xo_-sChiBro8pIldzBxYcB1fAd8U9z6krlPFnVGmt1GIT8f4CL9CeLwpnEDySdiYYS4gYyikB97yjlCc3Z9VMJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از روزی که محاصره دریایی برداشته شده تا امروز بیش از ۴۰ میلیون بشکه نفت صادر کردیم
🔹
ببینید حزب‌الله و شیخ نعیم قاسم نسبت به تفاهم‌نامه چه موضعی دارند و برخی دوستان ما در داخل چه موضعی دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/665118" target="_blank">📅 22:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665117">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f0f902f8b.mp4?token=ZNnD1YuIb6Nl5SNYk42CZUzMjT-3ihLo0QYSdmj8RMwevv3xNfl-39FIdqELz0IP0nw9uX25CzXV_JGCQUysVaQaYZSJJ05UTRkeCstZGh1bB3K3H88O_jAkESss5qlduSWLLZhbPnRisPYCrrO0d2F0QbKG0GqFFNnvjL0jhK7xWthhaT9Y4OAL-Z23Zx11yJHh521f3EQ3zUULhR0HWQ__njeYJDJc7CjiLJ0mIDbJ9IMTQ7c9fe-zWDS8RWEWp2DQdVSE6ERzwYEj93zFp0UmS2Od4uiwj_3In30EaSak4XHIjO0pFsIgH95ckcDnArK0uwzaiydHBf_iwNdShqDelZHKFkkqDkpFYw9MIE656iXDHheg-lq6GhxD6ZWq3sShZrNyJLl6KXJIxY7k05lBqafNZc7WNXzABxBXJa0p1jVtIRi7gEYG-kFYyq_YdCBYLBZ2V5S4F-bG4e3kgkC47Ut-twLOecD1lNBT_yHx6vuv4rh760_ewEOUzCugW-vwzwtfO2IFbSiIw07N2AZ4i1ghc8d37Zf4TjjBUEMFBEeEdrt9XkRE0lGgqlLoVMGQdy_c_oLeUbc18g5StwhHC5zAbbr1uqlRtiWXlgQXe6A9mnztj8Uh8niIHG_odzlaaw4plDcYa8jGn9VIonkXNX8m0ggenmsBjKfO_TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f0f902f8b.mp4?token=ZNnD1YuIb6Nl5SNYk42CZUzMjT-3ihLo0QYSdmj8RMwevv3xNfl-39FIdqELz0IP0nw9uX25CzXV_JGCQUysVaQaYZSJJ05UTRkeCstZGh1bB3K3H88O_jAkESss5qlduSWLLZhbPnRisPYCrrO0d2F0QbKG0GqFFNnvjL0jhK7xWthhaT9Y4OAL-Z23Zx11yJHh521f3EQ3zUULhR0HWQ__njeYJDJc7CjiLJ0mIDbJ9IMTQ7c9fe-zWDS8RWEWp2DQdVSE6ERzwYEj93zFp0UmS2Od4uiwj_3In30EaSak4XHIjO0pFsIgH95ckcDnArK0uwzaiydHBf_iwNdShqDelZHKFkkqDkpFYw9MIE656iXDHheg-lq6GhxD6ZWq3sShZrNyJLl6KXJIxY7k05lBqafNZc7WNXzABxBXJa0p1jVtIRi7gEYG-kFYyq_YdCBYLBZ2V5S4F-bG4e3kgkC47Ut-twLOecD1lNBT_yHx6vuv4rh760_ewEOUzCugW-vwzwtfO2IFbSiIw07N2AZ4i1ghc8d37Zf4TjjBUEMFBEeEdrt9XkRE0lGgqlLoVMGQdy_c_oLeUbc18g5StwhHC5zAbbr1uqlRtiWXlgQXe6A9mnztj8Uh8niIHG_odzlaaw4plDcYa8jGn9VIonkXNX8m0ggenmsBjKfO_TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میثاقی: به مردم توصیه می‌کنم در ایام جام جهانی روی مسابقات فوتبال شرط‌بندی نکنید چون پول خود را از دست می‌دهید / در فوتبال چیزی قابل پیش‌بینی نیست و نمونه آن برد اکوادور مقابل آلمان است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/665117" target="_blank">📅 22:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665116">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBtngLzNbwJdUK18lPvs0PFXSNwZLcbX6wIOKZJwFsjdlfB-aSGFzyrop_vbmgbhF5hUdnZNOLzztR0bae_J8rzRcpldklflrSShChxdLIXylgbMafW-A9HTtSvlqDz0LRCwSaj1r6QbmRWMC42pFNwz9vme8OT3d5-QjIAHWVAVFJoSJj4KsPbybVKc-ccY_2RpTUTzt4EjGHlmwNBJitATVRH05VRatLr5n53M05lJm4WFXCto4A0RTAjazikagbRzkp7rE7VFzs4gJZBMybVuGT5tFS0DjUH84sJhBQOg__D8Yfqn-wjcSXaaXuUZPLMKyXw9aljWTqIMb24qFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در شکوه بدرقه‌ی رهبر شهید،
کالکشن جدید تیشرت‌های مشکی قرار آماده سفارش شد.
طراحی‌های خاص، چاپ باکیفیت و جنس نخ پنبه؛
قیمت اصلی: ۱,۴۵۰,۰۰۰ تومان
قیمت با تخفیف: ۱,۱۰۰,۰۰۰ تومان
برای سفارش پیام بدید:
@gharar_order
مشاهده محصولات:
@ghararshop</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/665116" target="_blank">📅 22:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665115">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
قالیباف: اقدامات روبیو در کشورهای خلیج فارس علیه یادداشت تفاهم و برای تحریک کردن این کشورها بود/ تفاهم‌نامه ما استقلال لبنان را حفظ می‌کند  قالیباف، رییس هیئت مذاکره‌کننده:
🔹
تا ۵ بند تفاهم را نهایی نکنیم اصلا به مرحله بعدی و اجرای بقیه بندهای تفاهم نخواهیم…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/665115" target="_blank">📅 22:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665114">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‌
♦️
قالیباف: رژیم صهیونیستی به‌شدت با تفاهم‌نامه مخالف است و همه تلاشش این بود که تا می‌تواند آن را به‌هم بزند
🔹
تفاهم‌نامه سند شکست آمریکا و اسرائیل است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/665114" target="_blank">📅 22:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665113">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
ادعای روزنامه آمریکایی: پنتاگون در حال آماده‌سازی برای اعزام نیروی زمینی به لبنان است
واشنگتن‌پست:
🔹
پنتاگون در حال برنامه‌ریزی برای اعزام نیروهای زمینی به لبنان و اراضی اشغالی جهت نظارت بر اجرای توافق اخیر (خلع سلاح حزب‌الله) است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/665113" target="_blank">📅 22:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665112">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
مذاکرات ما فقط تا زمان امضای یادداشت تفاهم بود  رئیس هیئت مذاکره‌کننده:
🔹
الان هیچ مذاکره‌ای نداریم؛ سفر به سوئیس هم برای گفت و گو درباره اجرای بندهای ۵ گانه بود. در گفت و گوها ما نتایج مذاکرات قبلی را پیگیری می کنیم تا محقق شود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/665112" target="_blank">📅 22:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665111">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac4e8a59f.mp4?token=sD1dKg-xdFluXceqbJ6536CxCyphYaevYI8ZLKq6WiOTaYNDmqzInUdSZpzRgbU-mDVdj4XdrODgw0HGCzeXCmKtE4UPNgfRCjQ5vf3Bw1rBswoxymQsY7VuwhJVYaAtz6jSNly6_KSodxGDxjWSMFDMwUj_pF_7z8h2vaTT8HAqMncul6uK-UkrXeSsLppyo2Nm9OZYoABvZX817E-A6dlJHe6ZSm50TFXH5vO1w5QCRwjPTGIGWAjxCiouIfRhtkxP6H_edEfuppb1EUg_hqntIDVt03_rr8AiLkvKszQR5KNNbQA_iKLpRgwkgJhCLK21RpYC7up4XRR1E790PYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac4e8a59f.mp4?token=sD1dKg-xdFluXceqbJ6536CxCyphYaevYI8ZLKq6WiOTaYNDmqzInUdSZpzRgbU-mDVdj4XdrODgw0HGCzeXCmKtE4UPNgfRCjQ5vf3Bw1rBswoxymQsY7VuwhJVYaAtz6jSNly6_KSodxGDxjWSMFDMwUj_pF_7z8h2vaTT8HAqMncul6uK-UkrXeSsLppyo2Nm9OZYoABvZX817E-A6dlJHe6ZSm50TFXH5vO1w5QCRwjPTGIGWAjxCiouIfRhtkxP6H_edEfuppb1EUg_hqntIDVt03_rr8AiLkvKszQR5KNNbQA_iKLpRgwkgJhCLK21RpYC7up4XRR1E790PYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم نروژ به ساحل عاج توسط هالند
۸۶
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/665111" target="_blank">📅 22:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665110">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e01faa4075.mp4?token=qF_boXcxamZjYd8txpgUBgscLwUoX7Nn9zFbU1xgKjGgbdBbgqzxW13khOMxWZCbt8K9bbCG-KmqZaHf0FwLfE94XBiXJliRRUiEmq2LT6BepMwKttfVSaJw5L6aPXBj5b_bl4tqBvPfhdpsFvPSFKHKPUJi7h54YTfF_6WRu4QA9fQMibBsTbDpnuciLk7TwVvq3vtT-d27O6WxNpz-ntLO1dVi4dfZNaQl0d0OCe52vXGUd57fic7ejAblwvUuL0HGBD2NoZQ347Gvt66aSJS5CdhGz7s_I52F0vnSvV7_ZG1RU1bXzJANe2GCkSkrWsWfcV9usAXLlK1o5e3olQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e01faa4075.mp4?token=qF_boXcxamZjYd8txpgUBgscLwUoX7Nn9zFbU1xgKjGgbdBbgqzxW13khOMxWZCbt8K9bbCG-KmqZaHf0FwLfE94XBiXJliRRUiEmq2LT6BepMwKttfVSaJw5L6aPXBj5b_bl4tqBvPfhdpsFvPSFKHKPUJi7h54YTfF_6WRu4QA9fQMibBsTbDpnuciLk7TwVvq3vtT-d27O6WxNpz-ntLO1dVi4dfZNaQl0d0OCe52vXGUd57fic7ejAblwvUuL0HGBD2NoZQ347Gvt66aSJS5CdhGz7s_I52F0vnSvV7_ZG1RU1bXzJANe2GCkSkrWsWfcV9usAXLlK1o5e3olQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس مجلس: اگر نخواهند در گفت‌وگو به تعهدات خود عمل کنند، آماده جنگ هستیم؛ اتفاقات شب‌های اخیر خلیج‌فارس را نقض آتش‌بس می‌دانیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/665110" target="_blank">📅 22:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665109">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/205ddcc2be.mp4?token=qqylR6tZm2dQl0V4h91Oo0eQ04eozfqpU-yvlMcyJxnaF2jwmcGa1GLO3PI2hq3c0PEgJeu3AERjPcAA2B8b4YvMDtbp58DFrSBJmx7urYILb48W3Drx1TZTENqymGj6WC6pRFQG0vLh8SzFsIvfK_2DiZDnKrUgQWTNCcqR5IXfPFhi6HjTIR0raoOkBctfKg-QbtKrBcVYNr2wFOIsAf1fOEmhGIg5aN5ZGWc2ct9xDHz2dv6vXZ3ESNBteG9tTIqu3ZjPSXAk0es7NfPHqGLlC3b8gxs95Z-Dm1lDPJO93Ty9vaB_qamcscP5tmMzQOI6t5oNS0yQr2JjLnanWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/205ddcc2be.mp4?token=qqylR6tZm2dQl0V4h91Oo0eQ04eozfqpU-yvlMcyJxnaF2jwmcGa1GLO3PI2hq3c0PEgJeu3AERjPcAA2B8b4YvMDtbp58DFrSBJmx7urYILb48W3Drx1TZTENqymGj6WC6pRFQG0vLh8SzFsIvfK_2DiZDnKrUgQWTNCcqR5IXfPFhi6HjTIR0raoOkBctfKg-QbtKrBcVYNr2wFOIsAf1fOEmhGIg5aN5ZGWc2ct9xDHz2dv6vXZ3ESNBteG9tTIqu3ZjPSXAk0es7NfPHqGLlC3b8gxs95Z-Dm1lDPJO93Ty9vaB_qamcscP5tmMzQOI6t5oNS0yQr2JjLnanWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس مجلس: اگر نخواهند در گفت‌وگو به تعهدات خود عمل کنند، آماده جنگ هستیم
؛
اتفاقات شب‌های اخیر خلیج‌فارس را نقض آتش‌بس می‌دانیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/665109" target="_blank">📅 22:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665108">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72bae72ea8.mp4?token=QfuG0fae51GGS8LNkpI0SMIdcx5uteMkp1w5G98sjQ52JuXzrG4XL7-Glz4cOzCz1pzaliWXWIDo1Ec3dIzpBGV-q3GCnOpMyrY5RkNfjlA9wtuCdFMXmfISflsX_BSiZEXg9fBRQs3kPyAQnBnExon3NAm_F5PtQ6J8QY_sieWTUUjrLYgLDLH36EikHr_huG2pTomHbSNbVAvN7bt42MVTtjnztiqIVOaY7NBLkX-89zdSL1tMDW7QMtN7diq4Py7Wlfr-mCkQCkN9M70d80xbUEWVldxrFUuEvQnNvwx1KhqEMXLFfCg9nWG5A6aeuHw-6iends2RqIgwc76Xrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72bae72ea8.mp4?token=QfuG0fae51GGS8LNkpI0SMIdcx5uteMkp1w5G98sjQ52JuXzrG4XL7-Glz4cOzCz1pzaliWXWIDo1Ec3dIzpBGV-q3GCnOpMyrY5RkNfjlA9wtuCdFMXmfISflsX_BSiZEXg9fBRQs3kPyAQnBnExon3NAm_F5PtQ6J8QY_sieWTUUjrLYgLDLH36EikHr_huG2pTomHbSNbVAvN7bt42MVTtjnztiqIVOaY7NBLkX-89zdSL1tMDW7QMtN7diq4Py7Wlfr-mCkQCkN9M70d80xbUEWVldxrFUuEvQnNvwx1KhqEMXLFfCg9nWG5A6aeuHw-6iends2RqIgwc76Xrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: جنگ تحمیلی سوم یک جنگ همه‌جانبه علیه کشورمان بود؛ تعهد آمریکا برای پایان جنگ در لبنان یک پیروزی بسیار بزرگ است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/665108" target="_blank">📅 22:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665107">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkDneAmMfW2stPcGsWSW_GuLb1Mjdbl1BpEd1gJdaVdrtZ2Z807uIlUYi9L527crlWTZKPTOXNqxtyASvz6tn4dAUgs0GyDdYbXHOuHjseDkE3_fSX_vctwOgPG7MjYRTgxgvXwfdUY_vc5y4jPUe-9hB7z076F2WURES07WM2oQP23tBaOG7MKNA0mxL_kSCb34mswZro9vf_YuPoiJ1rGlx6fSbg8OobFmGI9cPNeOdAwycBW6yPvMsOWLILK22JJ6JFOSteiunIRMdAkzoOBPpV_PEGLqLSegn2Oovvf6bSuq5cLXZh-GubPdpn9siKqO273NjC1kBXDlJbDGTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقام این آدم از شهید کمتر نیست!
🔹
امام علی(ع) می‌فرماید پاداش انسان عفیفی که با وجود توان گناه، خویشتن‌داری می‌کند، کمتر از مجاهد شهید نیست؛ بلکه چون یکی از فرشتگان خدا است. این سخن نشان‌دهنده عظمت اخلاق، عفت نفس و مهار شهوت در اسلام است. نمونه روشن آن،…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/665107" target="_blank">📅 22:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665106">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتاپ تورز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f234qoh26QSvfJDnm4kzGjgyvCkoOUblRWvAxf_lOTeH5cSjeayL-fESDRlZTRqa12bfOouBKcBIMF8hSPUxkN5hfKyY6pavw_l5JI8xaTp5p7tbCYMbTerv7aFNQsDPrC3GWzjGhn9VRB5Yy_f0Vq_prMIgRivtdasFnwp-pbVgHDAlzueA3USVAPt2R7eNOIGxyQBaFYUFM9ucghHGvtcDPbstPy9PCuBrroZg7tSqZ67pGwVzwi_mhJd9BxIlLmtzZrRTHHtMYVNQwhcc7FO0cFnhD_Q7ai3pINsHcphO2CMws8ZhRhr0RB3Drl06Emmj9tH6fk2X8KKMSjKyPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
آغاز فروش پروازهای هواپیمایی سروش
📍
در مسیر تهران - کیش - تهران
✈️
ایرباس پهن پیکر A300-600
🗓
از پنجشنبه ۱۱ تیرماه
خرید آنلاین از :
www.Booking.ir
📞
+98 21 8586</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/665106" target="_blank">📅 22:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665105">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745f2de194.mp4?token=t8FAWAMoAm3TWEwCASAfJEDCH7dhkOBbmCxFXLGAWXaPy0plc2nmatooPpBv1hMo1_ranclJ43G-Ffd9ESEA2yHJhJrLMEpoJYH1zdgctG5_U5B5-DyPZgFRmX5I1LA9fiEdAskxvLDb5zNh-a9sDui8vlUa7_I5DZuW-Z0GBi6bRPKUUnpS0UOC0EkbeHIGUcrQ2F_Y3qFPLcBOChP3mQYFTwrYJEK_F4gJNIf5jh9Znvj3hwZvj7GhckuK05yXrEACR-b_E46crJm0b_oLZlOuP9WS8OTML4i7lCKt-AOsBLiRd7PCM9I-RDpIAn5Tj4S2izNiGA3awLAtUM1i5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745f2de194.mp4?token=t8FAWAMoAm3TWEwCASAfJEDCH7dhkOBbmCxFXLGAWXaPy0plc2nmatooPpBv1hMo1_ranclJ43G-Ffd9ESEA2yHJhJrLMEpoJYH1zdgctG5_U5B5-DyPZgFRmX5I1LA9fiEdAskxvLDb5zNh-a9sDui8vlUa7_I5DZuW-Z0GBi6bRPKUUnpS0UOC0EkbeHIGUcrQ2F_Y3qFPLcBOChP3mQYFTwrYJEK_F4gJNIf5jh9Znvj3hwZvj7GhckuK05yXrEACR-b_E46crJm0b_oLZlOuP9WS8OTML4i7lCKt-AOsBLiRd7PCM9I-RDpIAn5Tj4S2izNiGA3awLAtUM1i5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: اعلام پایان جنگ و رفع محاصره دریایی از نتایج مهم تفاهم‌نامه بود
محمدباقر قالیباف:
🔹
دو اتفاق مهم پس از امضای تفاهم‌نامه در شامگاه ۲۴ خرداد، اعلام پایان جنگ از سوی نخست‌وزیر پاکستان و توییت ترامپ درباره برداشته شدن محاصره دریایی بود. او افزود ایران در حال پیگیری گفت‌وگوها برای تحقق ماده ۱۳ تفاهم‌نامه است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/665105" target="_blank">📅 22:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665104">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4b154b416.mp4?token=cDZyMvTDnpEevqE2KOlppVF43luNSgR9TtqpumMMIp3ToeC2F0tEnGKbrAoupbOEpL4m-NRPgSl3Yyt2ZmcjsPBUfctGcMX_fE69nQOz0kRgSpU8EGINzDqjoHlhC1B1Va3QZJSwR-bX-6lW7olmQmt4kWKa2tN_XEPe-OfYgwS9iecIHb2aHxjkUYgziWTCFiuScOjOYLQfOGn14UDZxMOfitd9noxkp9MRFE5Z7VdyByzAAwgC756vJ3JIW2ZoHRHPPle2-vPB3b9sbvrspfp0gANqpgSV9Jxy5pT0mJReDt4KEW-MzpX1uLqwnRzShJrNvqnMTddzy8ubffAq2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4b154b416.mp4?token=cDZyMvTDnpEevqE2KOlppVF43luNSgR9TtqpumMMIp3ToeC2F0tEnGKbrAoupbOEpL4m-NRPgSl3Yyt2ZmcjsPBUfctGcMX_fE69nQOz0kRgSpU8EGINzDqjoHlhC1B1Va3QZJSwR-bX-6lW7olmQmt4kWKa2tN_XEPe-OfYgwS9iecIHb2aHxjkUYgziWTCFiuScOjOYLQfOGn14UDZxMOfitd9noxkp9MRFE5Z7VdyByzAAwgC756vJ3JIW2ZoHRHPPle2-vPB3b9sbvrspfp0gANqpgSV9Jxy5pT0mJReDt4KEW-MzpX1uLqwnRzShJrNvqnMTddzy8ubffAq2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل تساوی ساحل عاج به نروژ توسط آماد دیالو در دقیقه ۷۲
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/665104" target="_blank">📅 22:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665103">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stFbzxo2NdiIrEw1CM4S2BlwdLo8JBJidfocsDSykXeIMP3qP3rt1lI8fioI6EYe3yzsEi6JgTKLlM_c424SCY0Ce9b4rhJ4loFUGYT17IdsE8sK7u2erW8bLCK1FkoGoBP5D1GZOyHYn02bHKeV2TUf4gS9nyvr9Zv25kQ5zYmcA_4Ui7AsFE218dCTLGigc2iGqSDlxkKT3By1j-b2Cat84gyMeNwCAcuvSP3lzCQ4XzSJVGL-k2xZ5qhCcq0zslcuiLlNPsi585JkDeMqb66jMbQReNSELcectW1BZFbX0yz-RVRicWrRgpub7EHH1dqfz7oJqzVYUlxVtvl2eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طعنه ترامپ به چینی‌ها بعد از رای دیوان عالی آمریکا به دادن تابعیت از طریق ولادت در خاک این کشور
ترامپ:
🔹
من می‌خواهم رئیس‌جمهور شی و کشور بزرگ چین را به خاطر پیروزی بزرگ آن‌ها در تابعیت تولد تبریک بگویم!
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/665103" target="_blank">📅 22:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665093">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UCxlrWQ6zgVDo9y-RhcWLcp-xStXu4OgsUVjawmn2KxiB2SKEZdDq1zZQsDf1EKePTHW-dza8VhQIpV_YNxqUgjVwKjT5aHNQ3eor9Cy10tfZHDVsoYJdd8Ny_q1CQaEH7ogff4YP9hWxBm35QhbKFWPWsPjfknOoCLKAMw8M7i23ERajZyetfszgCY5GBc0bA4pAbD7Srlf5wxrp0cXzBiW4S8lnHL4j6oeyk1Nt8XsNPkLyKJINPE4mp9bhp4qHPFaynZ_06x9wrbdoRXl1PL_T0JpRqbewrjeNceOVxeB3xcNahvbYsz81iI__NtBlScYRvUaY0OmHphzXZVdTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aq6trZlPIhRt9X8Fbf45kpl9e6F8faDg_BVuHcQM9vagAN3R_4JyMBvFddF29To2hjfZk-I81RGs2gKM7JeGM0qmC4keTcYH8yKjhQ3ufPiUGkv2aYV7VDAWTlgNhz1WULM5zZCPT8X2awPEeyIt7eiIrK4g_gzZ2958lWq-a84ngkH4dLQPVyA60-IRMn6vHftxdf1vtmr9uTt0c1OX7PoNdH7OLEykOX_WCVUiwQ7ZMrdXnFIVmSKFAmBSwfrsRBzxfLW6ZbK_TnmPm_MsI7slUdX4ltiTvKVkEzFvByMJRftBuNLFQ9a86OScJEcxyw3qZJYvZkyxcTZCJ4SC4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EO8-Wdg4FUzaEKdnlPYrQlb-Ck8W8jtV1hvT4UpyfxJTAb9N1wxtsTPVnDpVK7YMyReBIisHYJ7XJNMshp66bgFrkpWZjsUzk-yW8eKPfh4FBk65FAdpJDU7-ooZUYt18gsaG57O0KYHE4Z6iB3AY0UTZjogNZyvvsOj8eYmUloL4fNLRCUvDpJysV3jaLTgr9hmSr8Lk-WczhC1h9BbR6fWsPzk3A8Zzlgo7WHp76c7LRZYa2ZACD-oLCQaLDW8K6fAYtlY18Qjb4J3t_MaffNvv7Yw-7DqVRgP_vBPNmETn_XVsAhhKJ7NevUGwPZ8Ei3YSepbCSWUdfQ31Dc_CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tELq5bVhMtVDDMyn296b9IfBsgqH1x4lO7rG8kWvQTE3X-NImlwU4gKawSBJzYjs92Z3jOBx85QGhtFRvNYZUYCYOFlvzpQax2sMI3zWg_s8RKqSbASc8CVlgbOowm8IojedOotgEzKRVaNyJLHqHlth0klHVlWIjL6oVI71UjFG7hb41EHoBEi3sUI5bQWqGA8qoplkLMb6aMvH0CAdwdxcO19m8cJzC5BEzLDihmio7-XfP45AJlJnRUHg3lAXIdtedRNP_DAX5bVfEpyYxDTPyQ8_uXS23R0W7VRu8pAm-YrVnHQKKYCD91s8YyauHp-qmgSPSMUPhGqLZJPEWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hx_mQF7wj9mKY9SZs0dzrlexfWUv70ce7un96ETS-nyM9pgILwuA3PbtW0FiyefQPYJ61mTQ2c6oEqL-xn-fxd2kqY5vpN3v7owSoXPhuZ_8YXIeKAcdtjyy5UjQa8IgnlZ5fXN5minpBlBrTsU_zwlnhjZr8l2Fadc-lW2HEtNA828o0fH9exVyLJynnmwCWhnwBtt04mzAEtrJaCQNOsPZh1q-chPEXXhhwBaVMjihAs2nZX9wrO5-TBMv7v3Ve5UByUPaWVHH-cw6LH7T2xK74_6NfWhr2EJJN_t2CuINdDffgCz3SkGT7cSKBx25avywzHZBOn-Aw80vZ6ichA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pgiTCg-nzO7LFvVu8mJvvhI6k1e__WqM8HfaoWB8DnzAPfqH8ftB4sv6Cy8oFv9r8ymGF1GlWcv05e3kKLD4K3SVY2K4MgbSYfsiGFYfv02f2wBos6mqUPxhwVtD_VTqwuoQkf3-JlsI_oXuZkGXPDlLES8_Jgzas0tlYDrYSybTSWbiP2lml6tJ9Pp4QA_0E2Xxs9ji5jqdl7qnmh11NaJ4JHdMqq7bpVSrr7Jos7WFtgtNiOoL_R2UrAPxO1gTW6RMExemJirTFhl0VLZCVF2-QfvT-pJtN0FXjDIIf5VYcllXpEo3BJT5wldnwiDeXAkkW2Flv7QaSrelaCqqtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ERRmd9YAuwUJjbfrO3ujG2xne6nlPEcFTqGr1KNcQby_12mz-7Xfb8IFsRKZri14ljCxXvIFGSN3Mgr8nsnwnN9-DBvKNzw-NYnruAu7lKWadroL_qsDeh30SzlhOw-DNByCvKMREZLwXAqYwmRDYUBa-CyJWObo-x8g9TlQFdI4PNSGxbw0_sU9zhd4TTGvojJ7aPZmJpns2Z5aEV0bFfaIL6LX0QkvTXlWBb9KQsqOL6SNeyPwt141IC9QSvcjuFNqal0SA7wVjLOYDE2MzW8YSYoqSP6B84a_rHKrYXXrI2F3GT84vLpdgL2Gw2MGle9_JrxC79mTm5zlf-KtvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XBHHtUB16Ww-Pnb2XtjyNt-5KZLXMKhyAedngLrfYAMWosmvT-Z37CJgkQ5wiRmSXZ41Fljoj-HTGB5gef0t-TKMM3OclKRmWCVLOyb0vzBdQnGVTJ1NMgaTp1WlZJNcLtMBvlTf9J11FD6k6VvhtxQSPXAqaHbUQM1nHrUegaMyPpzNu7p8VTXtHLcAluT_7CMKiwdrhTF_8gcuyAMfvB2oeHcwrpTBW2MuwDkma0ngbHNn5YtheMGQYdbbx6zNWE6W7MIHekcwtjO2qg08j_vB8Ri0E6nJM7xpUEX0teeLKt1MNlx3n2AcMJoJLMK9urqq0Mx3mFBJ7eLNPCMyUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fW9-WW4lcWVM9ZkcFO0vE8C9_q_ZEPxilJykDwMm92SW4u4LFiAxs_iRiNyfTYoEhPuHdk_l2ysjP4Fi41f_Y5XpLq0mo6JXqQKy71SMmGvbbecHeUAXspnC9IBE-3xR9kRusgd7ZEvGiEh2wUid9o7GwTUei6vAyetZw5r7zDEBeg7hU2kDo9SM2fFix5Bp38fhxOTNrDgILJ72AHFGjz827QaYvEEfRoUMd3PbEtY_OXRuwa6TsvHfCgQOLb83JxZBc_AvZuVsd7UhGXTvT-t4CfOifn2EyBLKG1W6i2bmZjNdo9nJN_l7RVv03UGY-at9CmDF5dMQrXRs31nVGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AMezVThGS7APVqWGpnzzRuYCGo9O4A45cPcOBbVJaw1JQVPyu_u5ukbIvmOz7dAeXL5m0TOWbFoR5nJ50jYq_R4lBjMTPbuLVDgMtD7iR0gc_oH20WFV9g6OQ_v2Q8tNcl8CJ6UNCB6159rZix3VcWH5UsT3wNTN-TFa3vBwkQ6Cw_m1QQcAHc3TjcyX04hyhNfk1_VgQaa9HVD0WKcV1col5XdytkbQI1E7XLjyXzHQAZ9CT1ki_TBYzpolm_HkIkiZRKJ0NpRka2hdbYGwF0gNodVxLEO985eprqK4KmFvyN_S7LJyjGZV7TL2wN_vhJfwfXkt_xyr9o29WRQqaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
روایت مخاطبان خبرفوری از اختلال اخیر در بانک‌های کشور
🔸
الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/665093" target="_blank">📅 22:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665092">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
رژیم صهیونیستی باز هم آتش‌بس را در جنوب لبنان نقض کرد
🔹
منابع خبری ز اجرای یک عملیات انفجاری توسط ارتش متجاوز صهیونیستی در شهرک بیت‌یاحون در جنوب لبنان خبر دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/665092" target="_blank">📅 22:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665087">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66378b9292.mp4?token=Za9xq56-BtyInlA_N1Z4lOnaoVWwSnVKcqYbyNp3eADgJvprGiyHPI_XVSOmxvjzSlONzSQYs7yCDuYpj3q5vrhsXIYYqEgX22ZLobQMi0lAu96AsmrMhieDp66wyilh_l0psu0feKIVjA1hAg2zSE5nuV8wC4A06RSEbuwzrBpYs-XDCJCHk_wxi_7egcufsKvDLhW3vprdTTfE-Gt5kvfiyAGxix0uFUdhsmRLBRre7mJ6NQ4eZsi4t_ZYNkcINSxAyx4UVENtO8nzM2yXlqgSxiyBUe2CluvhlP69vlmL9YuOVVHZGld4-966N4AVDhdNK8e0GJNkL9JFABpX-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66378b9292.mp4?token=Za9xq56-BtyInlA_N1Z4lOnaoVWwSnVKcqYbyNp3eADgJvprGiyHPI_XVSOmxvjzSlONzSQYs7yCDuYpj3q5vrhsXIYYqEgX22ZLobQMi0lAu96AsmrMhieDp66wyilh_l0psu0feKIVjA1hAg2zSE5nuV8wC4A06RSEbuwzrBpYs-XDCJCHk_wxi_7egcufsKvDLhW3vprdTTfE-Gt5kvfiyAGxix0uFUdhsmRLBRre7mJ6NQ4eZsi4t_ZYNkcINSxAyx4UVENtO8nzM2yXlqgSxiyBUe2CluvhlP69vlmL9YuOVVHZGld4-966N4AVDhdNK8e0GJNkL9JFABpX-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش خبرنگار خبرفوری از آخرین روند آماده سازی مصلی تهران برای تشییع باشکوه رهبر شهید انقلاب #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/665087" target="_blank">📅 21:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665061">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
تکذیب دفن امانتی پیکر «رهبر شهید» در حرم حضرت معصومه(س)
🔹
مسئولان آستان مقدس حضرت فاطمه معصومه(س) خبر منتشرشده در برخی کانال‌های فضای مجازی درباره دفن موقت پیکر «رهبر شهید» در این حرم را رد کردند و اعلام کردند این ادعا از اساس نادرست است.
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/665061" target="_blank">📅 21:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665060">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRCMioB_EYvokirMlsaDTj0L_zKEyyb78GI8QQbRYbTxi906WM0hHUQBC9gGkZI90TXRMkUGbWbZffjcu898AWsM6A58ZNGf_oVWHIdweBavL6uClnP4_25aS9pDmgY7XTiBtmt9mtV7Ute2HjkeXi821PemuTIJMKlExh-YOPShnisg5ly3uRtV0I_p6sQSMkrO8dQOvTy9xPa85F9sYE6pGnB-eV1jBlzEyWH_1W0oepYOXijZAD4mEQA3TeQ_aE_KPLrS2tz3NtI-or59KSGFhuIS-ORUFRtIs5sKDlSxkFlgMuTygRCL8THdAp7UaDOdH--6g7ipmpmPI7TbVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت‌های رویایی ۶ سال پیش یک رستوران در شمال تهران
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/665060" target="_blank">📅 21:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665049">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
پرداخت یک‌میلیون دلار پاداش به قلعه‌نویی پیش از جام‌جهانی
یک مقام آگاه در فدراسیون فوتبال:
🔹
امیر قلعه‌نویی معادل ریالی یک‌میلیون دلار پاداش حضور تیم ملی در جام‌جهانی را پیش از این رقابت‌ها به‌طور کامل دریافت کرده است. این مبلغ با هدف تقویت روحیه کادر فنی و بازیکنان پرداخت شد، اما تیم ملی بدون پیروزی از مرحله گروهی حذف شد.
🔹
با وجود این نتایج، مهدی تاج بر ادامه همکاری با سرمربی تیم ملی تأکید دارد.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/665049" target="_blank">📅 21:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665048">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czPPekjoAtLAxeo9ylmZ_jgf3tc3yEwKRYt8kLvXYSYKjU18K7y308JeFsqu5hNYS_Puko25AIiuG4VC3_43-TP0BBGF4GPrqbKAEcgKWIfoTAboWRG95qkDMZT_EyaNlRoVn6suD05XPKHcNtuPh5QXMcy4CrVFJQJx7SirsC40eaeoiI1vUMnYHDZ7aiw28zY-07aTUbzsmYjZb2fCyXnv2EbjcXdzlYSq1Lu_-m-i7z1jt_J8J7O5EEU8PfKBnTWiQeRb4UDupMSPAkKXJpR_KxSQdO44RSzyF2hX4lMm7Aizp2M8m6OmJ3CCf5ITT0FlL4WURja7c_6zmn1wWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معرفی سریال: خرس ۲۰۲۲-۲۰۲۶  | The Bear
🔹
ژانر: کمدی-درام، آشپزی
🔹
امتیاز (IMDb): ۸.۵
🔹
خلاصه: کارمی، سرآشپز جوان و نابغه پس از مرگ برادرش به زادگاهش برمی‌گردد تا رستوران کوچک خانوادگی را نجات دهد. «خرس» روایتی پرتنش، نفس‌گیر و واقع‌گرایانه از آشپزی، خانواده،…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/665048" target="_blank">📅 21:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665047">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88bdb2e333.mp4?token=YiBDKtEho0hpBs574-_wy8DrLOj8EOxhdUUI9zugsABjRflCpDIUfJUBHojmY6sh4_wi_d-JOvH45rtKF0uL7DSgtQrkWlvPP8EpZnUb6-QkBQUdqeblVsJ59XXKkQr7uAkM1wci88SomlLg_BYg7kI2y1rF2RpttuVSH9igE7rDuqzQXqEKxyWd82FQ6X0m1pYe0O6CPBYXzqNssqfdshjZoMqhEJCJf9dqODoA1tqfXca_78aqYsCjepHDvqZ1LsBWEQKuhwqcjDOSsXdyuKec0hXEwfsn5y1PtW25z72VRyY4NLjVbbAeTG0x9hjoEMiwSVIxaoCvFNyiPk427g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88bdb2e333.mp4?token=YiBDKtEho0hpBs574-_wy8DrLOj8EOxhdUUI9zugsABjRflCpDIUfJUBHojmY6sh4_wi_d-JOvH45rtKF0uL7DSgtQrkWlvPP8EpZnUb6-QkBQUdqeblVsJ59XXKkQr7uAkM1wci88SomlLg_BYg7kI2y1rF2RpttuVSH9igE7rDuqzQXqEKxyWd82FQ6X0m1pYe0O6CPBYXzqNssqfdshjZoMqhEJCJf9dqODoA1tqfXca_78aqYsCjepHDvqZ1LsBWEQKuhwqcjDOSsXdyuKec0hXEwfsn5y1PtW25z72VRyY4NLjVbbAeTG0x9hjoEMiwSVIxaoCvFNyiPk427g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جزئیات تازه از مدرسه میناب
🔹
تصاویری از حادثه مدرسه میناب حاکی از وارد شدن آسیب‌های حرارتی شدید و سوختگی‌های گسترده به قربانیان است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/665047" target="_blank">📅 21:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665046">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLoCLXG2rJdKoTlLuk4GxkMsQOx28JVIyhQRXMHQb5_In20mbAUy8AeXVW0eLqIl_i7n-QgP6cAL1qorF-MSkZtM6zaewzRd_DooViMcLytu0KfKn1_iQrYMMvPX7XqbeMim5oiWYc8s99Sndasg6C_cxLp5wlUTn65_I8yUmcKJTsXjtf3_iPhlQfTLH5dyZ0ErmsIIrU1bXFOxloUiJ9ix17z2rs6iK4yG5m0J2PpW2FY8kNpyHKAL-EszNqQQ4SukC21MH34sAZ5ENkGkWY06gLUe4Qzw34azOR6KCPVplbk7TAfT5rXWpOZTlOf_Tk038teiPYtMVnygyC4bBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر امنیت داخلی آمریکا: پس از حذف ایران از جام جهانی رقصیدم   نشریه اتلتیک:
🔹
مارک‌وین مولین، وزیر امنیت داخلی ایالات متحده اعلام کرد که پس از حذف تیم ملی ایران از مرحله گروهی جام جهانی ۲۰۲۶، «رقص شادی» کرده و حتی «چند آهنگ» خوانده است.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/665046" target="_blank">📅 21:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665045">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zb6tx6Wd_THq6RcF18i2FxKDTpdHRxS-GbpkSm4t_S-8DZF965fW05K8ek0X5HopdIFiPpjoDZRTLmhHzISaTYDAFg2a2aGIwpmChj2S1CB9WHuv6qN2AhriDBXXOqvYEpqzJGvohVibwICg58DGIxgx0DuW0LNWiHqUi9KmXNEd0TJ5MM3jy35NcHocI6INgSGTwccKPlPRmSINY9uJC3xKJyWDgdqsGNWhzsf-8ChJryPH6bR1dfS-jIbSro9qXuSTxrcjYNjX5oL2UadcHFAW9Aj5TjAGib7AJdV-iDR26ygunnM9IpI85Vha8GoDpuvOEOTtywFRYdil3rETew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
عضو بات صرافی دیجیتال کبرین شو و تا ۵۰ میلیون جایزه ببر!
بات کبرین چه امکاناتی داره:
✅
واچ‌لیست و قیمت لحظه‌ای ارزها
✅
دستیار هوشمند
✅
رصد فرصت‌های ترید
همین حالا دکمهٔ عضویت رو بزن و شانس‌ات رو امتحان کن
👇🏻
👇🏻
@kebrin_bot
@kebrin_bot
@kebrin_bot</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/665045" target="_blank">📅 21:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665044">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خطوط 4 رقمی و 5 رقمی کسب و کارها با یک تغییر بزرگ
❗
با اعلام روابط عمومی شرکت رسپینا، امکان دریافت خطوط ۴ و ۵ رقمی دوطرفه بصورت انحصاری توسط این شرکت با برند نکسفون (Nexfon) برای کسب‌وکارها ارائه می‌شود.
🌐
جزئیات بیشتر و ثبت درخواست:
https://zaya.io/nexfon-info
0219222</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/665044" target="_blank">📅 21:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665043">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvvGTykQj3ZtpbohTZ4WZF4CuN37WiRDEI7Nf0C06Uwi68MMVijUW2d2CvR4qoXPeW-_oKrS6fJKT5Rm3CsbLoKR60hPrCKUeX1aM-OpjXkvV4mo4mj2ejbvwnygCFn0l5WLnSMeE-is8PAfP7B8em3uwMNgYrBZ64bhdUQ-8pqG7i-KvRiQqPjz7pelmBuY5fUBlPqzJCy3D2_zexAI0uNt8UaNH1lobrpWnPDwHxOW_RrM0-JvmG_wLc4LbEY0H2if6JnJj5qEoyGa7OfBRH3WdpIIOjYdO4VQhCa1ZBGIETnRneZemjycZLbJBZ09K5FJB_25PISjVd4z5OK76Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از تابوت آماده شده برای پیکر رهبر شهید و خانواده ایشان
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/665043" target="_blank">📅 21:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665042">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avs5GtrqV38ZUUe1PImkPt9FswAaHJSn1-hAPG5_y1EDH1KPASvMExOAwgvw9JAuLeBEdyNZolBQK7WDdVEslmB15shiWMObHcCYWBWjpy4f_0i5F55f_fuS4ucPG1aOvmXVFkTGAlpcAJsjQVGPN-O8eEtyiGPnLbZAdErzFdXfMIiREZ4Jb1PVeyR0GFaLLRAoyoSRKyR7IVw7EE59an7ktY1TmzjyKcX0gl_9cyH-OINM_bgS_oVyyDoUWcb005lCJ8Aqh2K9RjDWJavE20MEi5NOzo1_WaVryOgZ-B8WLCu1kfdR9GlAT6nBL2ieeeyjL9DOKWqPKE7-0eLCqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ممنوعیت صادرات محصولات شیمیایی، پلیمری و پتروشیمی رفع شد
🔹
این تصمیم درحالی اتفاق می‌افتد که طبق گفته کارشناسان در داخل کشور دچار کمبود مواد پتروشیمی هستیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/665042" target="_blank">📅 21:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665041">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8001621dc.mp4?token=lyafu6RBeg_ARrQBTW9_AH8hhhloCPIICjk7E__DCYQCJejGQ35czi-WFa0nmn8CtGm8607tnWBWSbNJ8bkkLUX3BVlYNAOo4vrXt4fnC70ZocU0UoSTSDLvJk9-fTLc7kejwhdCuVHszFT8mh_tj5n4WPXCjsUlVSa4qSH3FXOSXoiDM09jhAWwF_rUp5NnRQKcqjHlPBRkyyGQ1cIDH7MmYS4Y5S5i5BKy80_kqNEjLob3SY3z2Zs2Fwy4kLq7RlWGcNP1YthZU3l3VRcpCLNhWYaKI2K5y1asovYvqQTzD6UfY4xWsnkhfGcJ9XUHmflt4hFU1GYH02zlfAN_fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8001621dc.mp4?token=lyafu6RBeg_ARrQBTW9_AH8hhhloCPIICjk7E__DCYQCJejGQ35czi-WFa0nmn8CtGm8607tnWBWSbNJ8bkkLUX3BVlYNAOo4vrXt4fnC70ZocU0UoSTSDLvJk9-fTLc7kejwhdCuVHszFT8mh_tj5n4WPXCjsUlVSa4qSH3FXOSXoiDM09jhAWwF_rUp5NnRQKcqjHlPBRkyyGQ1cIDH7MmYS4Y5S5i5BKy80_kqNEjLob3SY3z2Zs2Fwy4kLq7RlWGcNP1YthZU3l3VRcpCLNhWYaKI2K5y1asovYvqQTzD6UfY4xWsnkhfGcJ9XUHmflt4hFU1GYH02zlfAN_fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول نروژ به ساحل عاج توسط آنتونیو نوسا ۳۹
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/665041" target="_blank">📅 21:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665040">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
تانکر ترکرز: صادرات نفت ایران به ۵۰ میلیون بشکه رسید
مؤسسه «تانکر ترکرز»:
🔹
ایران از زمان رفع تحریم‌های آمریکا طی دو هفته گذشته، ۵۰ میلیون بشکه نفت خام صادر کرده؛ رقمی معادل روزانه ۱.۶۶ میلیون بشکه.
🔹
این در حالی است که بسیاری از کشورهای منطقه هنوز به سطح صادرات پیش از جنگ بازنگشته‌اند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/665040" target="_blank">📅 21:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665039">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3SBJBD8rasvWSIwoO-P8dbtmHVweGI4dLSYEtrabKC3lyPL054KO0C0CrmT93Ngwl_JeppODspUhFqRQmz8_Omr4Mnye3jUyVtchEACxb-q8nf4AxDg2iQCaS2pgNPO4LJe19GZ3CNeZpmY3D4ePDpTe-oZ454EmeMw57ako5dr2zD9zG9TaysaADAzI0GTwL19zNjqHfOPhwm226x9z4n8OclVZnBLYoE5ibZYvzOpEj5uVokiEO-r1WWBRfzwSc_C2XmeQ9zVl3VYs7sS47bsxj2ZIptRVh9TGQCghkqu0LMNeh8J5HNcaTgnHDXuYMuiOAT_Ek-gwToiUNBfjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقتی برق می‌رود، زندگی از جریان می‌ایستد
🔹
قطعی برق فقط خاموش شدن چراغ‌ها نیست؛ از اختلال در کسب‌وکار، آموزش، خدمات و ارتباطات گرفته تا مشکلات برای بیماران، سالمندان و خانواده‌ها است. #برق_مردم_کجاست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/665039" target="_blank">📅 21:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665038">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98b96a0955.mp4?token=d5jSDunaADwwoUJNGTdtBdqOBsPSw5z4rgK4TouPMVYoEHp5PBuZQSopLpL0lTztcvokfrnsBCYz-kMemrl8p-N8aECVFCo5lg9vqIErWWbgQepUsxI17wYMn6PvGDTA0G0KgDQZt64jAdbbCpZyNnGsCpgiTopsCc-eLog-RvUh-uYtARiSOaCLFX4PL7kG0lCysQmPDRW6OAH6QtGADdYwlP8gNmRYvqfDApJ_YcMxsowecVw_sVwqU0M8bQZKLlOIBN7cul81O6eGVXLMvdIp2Ri7EHF-qZ01yJRZR2QOXYQKrjIjKQRCxtQUnVJniVXFKIXLfPZHE-rrbtXxzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98b96a0955.mp4?token=d5jSDunaADwwoUJNGTdtBdqOBsPSw5z4rgK4TouPMVYoEHp5PBuZQSopLpL0lTztcvokfrnsBCYz-kMemrl8p-N8aECVFCo5lg9vqIErWWbgQepUsxI17wYMn6PvGDTA0G0KgDQZt64jAdbbCpZyNnGsCpgiTopsCc-eLog-RvUh-uYtARiSOaCLFX4PL7kG0lCysQmPDRW6OAH6QtGADdYwlP8gNmRYvqfDApJ_YcMxsowecVw_sVwqU0M8bQZKLlOIBN7cul81O6eGVXLMvdIp2Ri7EHF-qZ01yJRZR2QOXYQKrjIjKQRCxtQUnVJniVXFKIXLfPZHE-rrbtXxzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همزمان با افزایش شمار قربانیان زلزله در ونزوئلا، تابوت‌ها یکی پس از دیگری به لاگوایرا می‌رسند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/665038" target="_blank">📅 20:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665037">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f0e2e722a.mp4?token=YBWtdJtGvR8HxaMVuRZtmofpM20JFn7fIrUOCVInRgdkRf0PsLz912zf2DjtlZm1zCiQbsdu-_y1vIqFnVZdRL7ZJMkJ_fEHKJvak-0e37c_-1vVc5dtMtWzJPWASkgSV3S3hcYwcqpMTRC0qmWF_QRpDc7aPAWtvgqk9lHoJ0k2WulGpooRGmvovufQ1reRc5XHb8768kr8oQqOO5dqC0bWEOIZgISWk8Z2dk-J8zY42f64mpkXJhK_XH49GQpOUHOxsjg8xcxwmdEyJ14Iz7bwin7TNEFGxC37amMr1VtPiuzHcQ3CALKgHimxM-47_09RujtTjnRU2prchB06dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f0e2e722a.mp4?token=YBWtdJtGvR8HxaMVuRZtmofpM20JFn7fIrUOCVInRgdkRf0PsLz912zf2DjtlZm1zCiQbsdu-_y1vIqFnVZdRL7ZJMkJ_fEHKJvak-0e37c_-1vVc5dtMtWzJPWASkgSV3S3hcYwcqpMTRC0qmWF_QRpDc7aPAWtvgqk9lHoJ0k2WulGpooRGmvovufQ1reRc5XHb8768kr8oQqOO5dqC0bWEOIZgISWk8Z2dk-J8zY42f64mpkXJhK_XH49GQpOUHOxsjg8xcxwmdEyJ14Iz7bwin7TNEFGxC37amMr1VtPiuzHcQ3CALKgHimxM-47_09RujtTjnRU2prchB06dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌‌ای از منطقه مجدل زون در جنوب لبنان که توسط رژیم صهیونسیتی نابود شده‌است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/665037" target="_blank">📅 20:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665036">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/315cce5c2a.mp4?token=fwNI28Wps6_sFLJ5drC32B3NplibUJ8dC2GeUiTFmxnuetES0Vb2tpkfUfaT8MX1NNDuzwpPZY3fmVmxfr9ETCsVoCWWPSK5XI-z5RVHIzGgu_ntc5_05zog7yquQnkDJnZ6QHgNG9MIer4xvLYcqehavNCwXDCAeDGTrkum5EI2ithOZIUcCFgDD4PWuu7qkLC3IqWOuC_JEV2-FoRKOXgi4B9p30jQZpPGQDmiIwqNF4BtngVhcUCh-Iu3O5iDtUjhj1HCK8AMa-i1aL4uDntLBGIRALv2Hbz2j9n76p5V_UoYOgXE038eYgPB3XYlLdLksBcpWwr1_W-MGEvyaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/315cce5c2a.mp4?token=fwNI28Wps6_sFLJ5drC32B3NplibUJ8dC2GeUiTFmxnuetES0Vb2tpkfUfaT8MX1NNDuzwpPZY3fmVmxfr9ETCsVoCWWPSK5XI-z5RVHIzGgu_ntc5_05zog7yquQnkDJnZ6QHgNG9MIer4xvLYcqehavNCwXDCAeDGTrkum5EI2ithOZIUcCFgDD4PWuu7qkLC3IqWOuC_JEV2-FoRKOXgi4B9p30jQZpPGQDmiIwqNF4BtngVhcUCh-Iu3O5iDtUjhj1HCK8AMa-i1aL4uDntLBGIRALv2Hbz2j9n76p5V_UoYOgXE038eYgPB3XYlLdLksBcpWwr1_W-MGEvyaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور غیرمنتظره لیونل مسی در تیزر تبلیغاتی فصل جدید «مرد عنکبوتی»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/665036" target="_blank">📅 20:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665035">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
یک ایران عزاست...
🔹
از هر کوچه و هر نگاه، یک بغض برخاسته است... همه آمده‌اند تا با اشک، بدرقه‌ای عاشقانه را برای رهبرِ شهیدشان به جا آورند
#بدرقه_یار
@TV_Fori</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/665035" target="_blank">📅 20:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665034">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
هزینه جنگ با ایران برای هر آمریکایی ۱۰۰۰ دلار فاکتور شد
سی‌بی‌اس‌نیوز:
🔹
افزایش قیمت بنزین (۳۰۰ دلار)، رشد هزینه مواد غذایی (۲۰۰ دلار)، هزینه‌های نظامی (۲۵۰ دلار)، افزایش نرخ بهره و هزینه‌های استقراض (۱۵۰ دلار) و گرانی بلیت هواپیما (۱۰۰ دلار) مهم‌ترین عوامل این افزایش هستند.
🔹
همچنین برآورد دانشگاه براون نشان می‌دهد هزینه بنزین و گازوئیل به‌تنهایی ۴۸۶ دلار به ازای هر خانوار افزایش یافته است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/665034" target="_blank">📅 20:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665033">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20f2110fe3.mp4?token=u4hwu4quFlG7BcT3VLdRhL1JoJYi4kzHWbSnEOGafGD6uJFQXwiVtyi29JoBEMASiGAEYw18YuCwq-TFPdZXy5lQsBot2M3yvztpoi7BAhXSoj4AdtFDkml0Kus6jsBT2DHPNLak4k8EoaWGBsnxETWQtwmYWjjOx402MYMCeV6BtxwUiRsBD-P4Hqc60sAgb3re86_R1IK9ch2n3VQ_m4UG2ZweXExDtpLWr0ACfhGOzfXaKkhBTezENc8juqCRGzxa-uJKcHps0rgDs9WYAU0n0BFc48ToAhLQXdkfzpFXgKvBudfxGkjdbKyEjeNps3Rt-uIkFcyZcatT5UKSuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20f2110fe3.mp4?token=u4hwu4quFlG7BcT3VLdRhL1JoJYi4kzHWbSnEOGafGD6uJFQXwiVtyi29JoBEMASiGAEYw18YuCwq-TFPdZXy5lQsBot2M3yvztpoi7BAhXSoj4AdtFDkml0Kus6jsBT2DHPNLak4k8EoaWGBsnxETWQtwmYWjjOx402MYMCeV6BtxwUiRsBD-P4Hqc60sAgb3re86_R1IK9ch2n3VQ_m4UG2ZweXExDtpLWr0ACfhGOzfXaKkhBTezENc8juqCRGzxa-uJKcHps0rgDs9WYAU0n0BFc48ToAhLQXdkfzpFXgKvBudfxGkjdbKyEjeNps3Rt-uIkFcyZcatT5UKSuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت برفی ‌ارتفاعات سبلان، اردبیل
🇮🇷
#اخبار_اردبیل
در فضای مجازی
👇
@akhbarardebill</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/665033" target="_blank">📅 20:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665032">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffouYGivSVKyA-IbHUYMYbTwUtcJIVg3Adu8TwNU20n7Tm7bNhFh_bZ3GtXFCd3kvmj2y2f7nKftNRM9Tj_Sq_1GO1IgQekEr0NmSJY4D9lunJb1MRRXzrkEcc9S5LH93JxFLkNK51ctbtk1Rg4JomCptfqImS2pdLVKJC-xJ3Em_U9qEfoucCRdIqfiWxskyHO4Mw1oqeJS4s8NZKEMrDq9LtKfinM7L4dYcNUPszfpOO8iuR5zlsgnkj171-IlLzHHz8ns3jQJ3K3R8RCM6o8XCs-sWFo3xRgVrROD7paAMN3OO-wBHejK9amxuEmYfN6eDYy7AmuW4z5d06frfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا به دنبال الگوی مک‌دونالد برای ساخت موشک است | پشت پرده کارخانه مخفی موشک‌های ارزان آمریکا
🔹
ساختمانی کوتاه و ساده در شمال شرقی ایالت ویرجینیا، در نگاه اول هیچ نشانی از یک مرکز راهبردی نظامی ندارد؛ اما درون آن، ردیف‌هایی از موشک‌ها روی میزهای کار قرار گرفته‌اند تا تکنسین‌های جوان آن‌ها را برای جنگ احتمالی بعدی آمریکا آماده کنند.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3226643</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/665032" target="_blank">📅 20:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665030">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
پیام‌های متعدد مردم به برنامه شهروند مدار: چرا مسئولین ترمز گرانی محصولات بی‌کیفیت ایران‌خودرو را نمی‌کشند؟/
مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/665030" target="_blank">📅 20:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665029">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‌
♦️
سخنگوی وزارت خارجه: در نشست فردا عمدتاً در مورد دریافت پول‌های بلوکه‌شده و آتش‌بس در لبنان بحث خواهیم کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/665029" target="_blank">📅 20:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665028">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
توقف تردد در تنگه هرمز؛ انتظار IMO برای مجوز ایران
🔹
سازمان بین‌المللی دریانوردی (IMO) در پی حمله اخیر به یک نفت‌کش، عملیات خروج کشتی‌ها از تنگه هرمز را متوقف کرد و ازسرگیری تردد را منوط به تصمیم رسمی ایران دانست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/665028" target="_blank">📅 20:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665027">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e871f5e508.mp4?token=QpP4tct_YeRN_iZFFcWjv8kOfjkTFz9NZFPmYHOkgjvUW72PvBP4VfbcNz2QyHgK0NOc9u8t_DSnq7BoePzqFWzKolKI52vlzzJWb1KDsGo81gxV2zuuNvDtPEqHruOFmK5gfCwCljPyWC4uW-Ut10vbcz3pDq3l5OS9abnGWFRIomcZtCF1OrKUknKndExs0k27GrlgljVh2S2Drngdpf75h9m52wZ8ni1K7e4MtQJjJX5sfXU_tTlmEKs8_8eAg0K_RxSls0EWpVSZyhc9q0PjcbeTP97CFif8IG4fyM2NesTn2pdDFeJPaaFdDcIPcDEN3kDUElu-2BWt0a1Nhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e871f5e508.mp4?token=QpP4tct_YeRN_iZFFcWjv8kOfjkTFz9NZFPmYHOkgjvUW72PvBP4VfbcNz2QyHgK0NOc9u8t_DSnq7BoePzqFWzKolKI52vlzzJWb1KDsGo81gxV2zuuNvDtPEqHruOFmK5gfCwCljPyWC4uW-Ut10vbcz3pDq3l5OS9abnGWFRIomcZtCF1OrKUknKndExs0k27GrlgljVh2S2Drngdpf75h9m52wZ8ni1K7e4MtQJjJX5sfXU_tTlmEKs8_8eAg0K_RxSls0EWpVSZyhc9q0PjcbeTP97CFif8IG4fyM2NesTn2pdDFeJPaaFdDcIPcDEN3kDUElu-2BWt0a1Nhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش خبرنگار خبرفوری از آخرین روند آماده سازی مصلی تهران برای تشییع باشکوه رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/665027" target="_blank">📅 20:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665025">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ETVnm0g1lHMgO7GWl63Odd6IgyyQmCGf8yR4NdBNhycwobZtR60u_1Df9z58b4Af6E7iaHgI501bQXMAn9mKfsE-hzXBZbU-6WWWj3GsHZmxiaP4x2RoPGMGH4WfRU57K1GASDiD5imFaYmlgHJ1Uyrf-KBNQnwJwjurnjhGj8b13rTdjJDr0mhkAAskK1e32Yi9QEIIP0LN4obLoZYZfkKa1Hez3IPiYOn0giO8YRKw9F-N0ynE08O9Gsw_B9uDv8HfhFZn_KaIRVWAfewv3Bql4Z1q6zDHW05DYa7YsgN7suhTWbr9HtzGde-ES_8MfEaw8sQQnwLcCenpSkfIxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FxXSfU1FjLeTHb8bz1SBjiB5zBm_izZxwybX6gVhUQ6oAMLr3xBMV6rW5DtSBcA3UcMuhfXpU7GerrgaWCiF4yaHjCDQSdWwuQgHkT9Ef4k4A6FFRCUU7dmGhdgH3hzc_IG6li1Q3KOFirVNk2XLYDhbmEbiPwPx18aPaU8CHExwCfUK7wVFxGJAybDZKTVJk3vofUXs9NbBIeqLnJyRySPEEryT8OxafaWusWBws8GyJjPnSgxA_r2cXXarLAAbWIwPC_Pl14cP-A8EeqMuf6JB5ZdfXBEzCCfJwpzowff88jTcAJhwt6HorKFq33ux9_kx7_mVTg0MD5P-ZSP8ZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
آیا دموکراسی از ثروت مهم‌تر است؟ این کتاب پاسخ می‌دهد
🔹
اگر فکر می‌کنید نفت، موقعیت جغرافیایی یا فرهنگ، سرنوشت کشورها را تعیین می‌کند، این کتاب شما را غافلگیر خواهد کرد. «چرا ملت‌ها شکست می‌خورند» با مثال‌هایی از سراسر جهان، پاسخی جسورانه می‌دهد: تفاوت را نه جغرافیا، بلکه کیفیت نهادها و حکمرانی رقم می‌زند.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/665025" target="_blank">📅 20:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665024">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
هشدار چین: آتش‌بس بین ایران و آمریکا شکننده است
شینهوا:
🔹
وانگ یی، وزیر خارجه چین در دیدار با شاهزاده فیصل بن فرحان، وزیر خارجه عربستان گفت که آتش‌بس بین ایران و آمریکا همچنان شکننده است.
🔹
او افزود صحبت کردن بهتر از جنگیدن است و گفتگو بهتر از رویارویی است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/665024" target="_blank">📅 20:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665023">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
اعزام هیئت کارشناسی ایران به دوحه برای پیگیری تفاهم‌نامه
🔹
سخنگوی وزارت خارجه از اعزام هیئت کارشناسی ایران به سرپرستی «غریب‌آبادی» به قطر خبر داد؛ این سفر با هدف پیگیری اجرای تفاهم‌نامه و مذاکره با طرف قطری انجام شده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/665023" target="_blank">📅 20:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665022">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
اعزام هیئت کارشناسی ایران به دوحه برای پیگیری تفاهم‌نامه
🔹
سخنگوی وزارت خارجه از اعزام هیئت کارشناسی ایران به سرپرستی «غریب‌آبادی» به قطر خبر داد؛ این سفر با هدف پیگیری اجرای تفاهم‌نامه و مذاکره با طرف قطری انجام شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/665022" target="_blank">📅 20:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665021">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cxv4zluwz71pnQrFts7XlrtjH97fLvABvFT-XueZdp0KyXzMnJRnlitZxT9Yym2ZJwg-wPpI00KnIGFbaj4pzAMDSCT4G1YmWbsF60YPhtyQLXXFSZeTPEpqPjMrJit3e50T8F1fnc61whZ_dXPhDTXhM61WzPfMpW9gUX0FhrosLB4khFBlR_zyV8BgGWvNoTlJtJH7iXJJhM5gsQHq_XVS-trGFXvyY9-kOjDt7ZJY4GpPLBtxQwhuClExsda0XPya_MGreOy7fLT6lXpBBGeUTirihrzmWmE20H5wV-pU21XR3UFd8qP1orIve0NfgsfyvP-Ej5fWK8vs4zSjdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاسخ این سؤال را مردم می‌خواهند...
🔹
قطعی برق در نقاط مختلف کشور، این سؤال را برای بسیاری از شهروندان ایجاد کرده است: #برق_مردم_کجاست؟
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/665021" target="_blank">📅 20:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665020">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5804af890a.mp4?token=mfgKRAbgimeZmDbl5aRHCU6yzyusWtMEkKJKvb-db__k7OYYLCBPC1ty3xTafnvsLSLa-5YISDmj0gS-vKGKtizKK22hhxz3pi2Sgsd9XBEWLTLPTI56dqMCX59k6-D5fH5vPpGeAMNpLuI8YtQx7oioUMTq_fiIfC6SRNM-rPbSvoHb4Cw-k7lC9n2ESWi-rMOpXeS3EEVU4SDE-uLkegLivtRZLo_BnZnVbCFvzJJAVJ0rDsrlCh2r8HWTQgddzSudehM3ysXmhk7nsIFE4MYLRf4Y7a283hPMTQXcI0qLo4pHGKS6Ez1meLSiqJvgpte2zRd3uSQX1RXg4AG4Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5804af890a.mp4?token=mfgKRAbgimeZmDbl5aRHCU6yzyusWtMEkKJKvb-db__k7OYYLCBPC1ty3xTafnvsLSLa-5YISDmj0gS-vKGKtizKK22hhxz3pi2Sgsd9XBEWLTLPTI56dqMCX59k6-D5fH5vPpGeAMNpLuI8YtQx7oioUMTq_fiIfC6SRNM-rPbSvoHb4Cw-k7lC9n2ESWi-rMOpXeS3EEVU4SDE-uLkegLivtRZLo_BnZnVbCFvzJJAVJ0rDsrlCh2r8HWTQgddzSudehM3ysXmhk7nsIFE4MYLRf4Y7a283hPMTQXcI0qLo4pHGKS6Ez1meLSiqJvgpte2zRd3uSQX1RXg4AG4Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کرم کله‌مرده؛ قاتل زنبورها و آفت سیب‌زمینی
🔹
این حشره (African death’s head hawkmoth) در دو مرحله زیستی مخرب است؛ لاروهای آن آفت سیب‌زمینی محسوب می‌شوند و پروانه‌های بالغ با نفوذ به کندوها، دشمن خطرناک زنبورهای عسل هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/665020" target="_blank">📅 19:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665019">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4b730f0bc.mp4?token=WzMEQD5Dv6ej57euhAnzWchDwBYrBTFH6Wk33Waw5XS9mvkAI4NV5PPEw5sm9uh8DE1DEA2-47ShAlBvpr9SK_sJ44S_S3WjZW9nkzYGyQL9rmOhRMAcQry7XnamkVLIeq-g19mF-75WAmHbQbRoOlNZRHcJXo_i0uE6rLqc2xEMXSKo32WBKbJ88-ecYE8_Ai7RgVJi8S3xbF8Ty_H2BUU57sAuuFsGbBL7TO9WL8imXYo6s-q7KtQ2ajq3MLTQC8R-mP3C6PBwWI8KipYHx_2-FG298nHD1JwD459B-ek3g-vN7ZdtmHb7jYCgHgZXcDiaST_2bJTFAw_GqCAmwzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4b730f0bc.mp4?token=WzMEQD5Dv6ej57euhAnzWchDwBYrBTFH6Wk33Waw5XS9mvkAI4NV5PPEw5sm9uh8DE1DEA2-47ShAlBvpr9SK_sJ44S_S3WjZW9nkzYGyQL9rmOhRMAcQry7XnamkVLIeq-g19mF-75WAmHbQbRoOlNZRHcJXo_i0uE6rLqc2xEMXSKo32WBKbJ88-ecYE8_Ai7RgVJi8S3xbF8Ty_H2BUU57sAuuFsGbBL7TO9WL8imXYo6s-q7KtQ2ajq3MLTQC8R-mP3C6PBwWI8KipYHx_2-FG298nHD1JwD459B-ek3g-vN7ZdtmHb7jYCgHgZXcDiaST_2bJTFAw_GqCAmwzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میانجی مرموز بین ایران و آمریکا؛ علی ذوادی کیست؟
🔹
اسمش را شاید هرگز نشنیده باشید؛ نه مصاحبه‌ای، نه صفحه‌ای در شبکه‌های اجتماعی و نه حتی تصویری پررنگ در رسانه‌ها. اما گفته می‌شود یکی از حساس‌ترین مذاکرات ایران و آمریکا، با رفت‌وآمدهای او پیش رفته است.
🔹
مردی که گفته می‌شود در ۱۰ روز، چهار بار به تهران سفر کرد، ۱۷ ساعت پای میز مذاکره نشست و حتی نامش از زبان ترامپ شنیده شد. علی ذوادی کیست و چرا همه او را «میانجی مرموز» می‌نامند؟
در این ویدئو ببینید.
@TV_Fori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/665019" target="_blank">📅 19:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665012">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c25bb3b338.mp4?token=tOpAk17CpcHA5q8ak5fJP3oKSISmFCuYalWEkMQd5oY4omnejCjURKdWGlukBxbAebPRUHw2MnhQjGGP95rKtR65Ct9eQcKXQWp4uS3EpsU55bINwIMHx6nWOIPmFZwSXx126QrEce_YXwu7g-E3C8XB5yUhAHWqVAiTtSDbhh9t81V-fIKmy-oIm0jLq5R4pUrZqOlTv1ZYHksDkIZpA2KGXjtiT5R_IhXvfEFBJpwyjNECIvjQKzxUUYxK4KIXkbLeRmbD2WiHNhIlbVXVERa1Bcsg63g9-svX0NV7ilCG_tC2pghRSSryW3a9xzxdr6kubG23mIaKcR9zXZ3qTDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c25bb3b338.mp4?token=tOpAk17CpcHA5q8ak5fJP3oKSISmFCuYalWEkMQd5oY4omnejCjURKdWGlukBxbAebPRUHw2MnhQjGGP95rKtR65Ct9eQcKXQWp4uS3EpsU55bINwIMHx6nWOIPmFZwSXx126QrEce_YXwu7g-E3C8XB5yUhAHWqVAiTtSDbhh9t81V-fIKmy-oIm0jLq5R4pUrZqOlTv1ZYHksDkIZpA2KGXjtiT5R_IhXvfEFBJpwyjNECIvjQKzxUUYxK4KIXkbLeRmbD2WiHNhIlbVXVERa1Bcsg63g9-svX0NV7ilCG_tC2pghRSSryW3a9xzxdr6kubG23mIaKcR9zXZ3qTDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش خبرنگار خبرفوری
از
آماده‌سازی‌ها برای مراسم تشییع رهبری؛ اینجا همه‌چیز مهیای آغاز یک مراسم تاریخی است
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/665012" target="_blank">📅 19:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665011">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
ریزش سنگین مخاطبان رضا پهلوی؛ ۶۰۰ هزار آنفالو و سقوط ۷۳ درصدی لایک‌ها
🔹
صفحه اینستاگرام رضا پهلوی طی بیش از ۱۰۰ روز گذشته با ریزش قابل‌ توجه مخاطبان روبه‌رو شده، به‌ طوری‌ که حدود ۶۰۰ هزار نفر او را آنفالو کرده‌اند.
🔹
بر اساس داده‌های تحلیل شبکه‌های اجتماعی مجازی، میانگین لایک پست‌های او از حدود ۶۹۷ هزار پیش از آغاز جنگ به ۱۸۹ هزار در روزهای اخیر کاهش یافته که افتی ۷۳ درصدی را نشان می‌دهد.
🔹
هم‌زمان با بازگشایی اینترنت در اوایل خرداد، روند ریزش فالوورها شدت گرفته و بیش از ۱۷۰ هزار نفر در این مقطع صفحه او را ترک کرده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/665011" target="_blank">📅 19:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665008">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfZM7eepI96QcF9igOa8W4U2y41PyzG8PjvYbOSV3XBayCkz6MvRa1NwqoWqCYuhJTypGS4Jgm-Q81LrflUfwxhX05qEOuQQFMCkJwoI_z3m7CPichHAe512tUUAxS1634GcOvvN92TNmO2VnVSaMNL7Xniavkd8cKtVQoDCjrLmTP6KP9Re5rboW7ENFZcB1V2MOZfuNjNqmYdjsaLHG7Y7yhbvE2Rh7wGJUPbEscCQtlcpCFDngfEwMve51IX8npUh1nr02BHcemGJ4OkhlpWpaI0iCd7Cq59tc3j6fRcdK8U9RaSMAmZrwn1ev7oXIrCyeoPqM1h1v3dBDCVl5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دشت شقایق دماوند
🇮🇷
#ایران_زیبا
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/665008" target="_blank">📅 19:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665007">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfe298db09.mp4?token=gIcrgtlBhguwddb0l1QcSOwzwOVp5-3Us0ZcQXfis16xGJsyoPdh7avmYe26kpjR0mc8KZJXH0MDqrx2yvlzcrLbyaP3vV1WICO8zndUTrMDVnW6xy6v-ZRT7sjZcARUpEKycEGRQpV8oeTy1sw3FYokZHBdAA1glOBgdrYoVCa4LJfkoFPobckxJ5M69jzxXAoQDcsckryJTkO8KGBCo54YIQLvt3AXE7TABH9TPjRugGHUX3XvUe0KYOtD20j3BRdXnmiDhUeHc8O-jf1OuNnxTBYMOMJRpBEemN7QqHENijK3c6E71B9ILjHT_urmn4PLHLyfCVMguana-MNH8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfe298db09.mp4?token=gIcrgtlBhguwddb0l1QcSOwzwOVp5-3Us0ZcQXfis16xGJsyoPdh7avmYe26kpjR0mc8KZJXH0MDqrx2yvlzcrLbyaP3vV1WICO8zndUTrMDVnW6xy6v-ZRT7sjZcARUpEKycEGRQpV8oeTy1sw3FYokZHBdAA1glOBgdrYoVCa4LJfkoFPobckxJ5M69jzxXAoQDcsckryJTkO8KGBCo54YIQLvt3AXE7TABH9TPjRugGHUX3XvUe0KYOtD20j3BRdXnmiDhUeHc8O-jf1OuNnxTBYMOMJRpBEemN7QqHENijK3c6E71B9ILjHT_urmn4PLHLyfCVMguana-MNH8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اوباما درباره جنگ ایران: وضعیت پس از میلیاردها دلار هزینه جنگ، بدتر شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/665007" target="_blank">📅 19:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665006">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
نتانیاهوی خبیث، دقایقی پیش، از عون و سلام، چاکران درگاه ترامپ در بیروت، اینطور تشکر کرد: از دولت لبنان بابت شجاعتی که نشان داد، تشکر می‌کنم #Demon
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/665006" target="_blank">📅 19:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665004">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e683e35d7d.mp4?token=JsogNc4M-cmz4Hx80OKrPdzCORH6iLSsDVrUXTXyFtnHI3jI4BGFQSjH6GDZaVAhXWkM9wkaJlkuFKrDVT7SDcTC9V0V_-nzNyKFvp3diD5TBNB_Z64qLw30lvJqwMVb42VL_QoQCQ4NXnkrc82qaI1OXKdR9jom-COTHpnTNHgeQCuPwgoBN8hQhtR1MhFS1pWeN2AMgW7j4-MmlKCYlB3nwmOnWi5fZqP9JU2yztR4onmhp9rsQsEdgc0SWRrHNbbh_SsoSwcGwibYR8Vji0I8sG0n4BavQTwk6-_7mjKAG7PrDySwtFbertq7xEiP9dE4v28ZcZvvezi2b0IAbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e683e35d7d.mp4?token=JsogNc4M-cmz4Hx80OKrPdzCORH6iLSsDVrUXTXyFtnHI3jI4BGFQSjH6GDZaVAhXWkM9wkaJlkuFKrDVT7SDcTC9V0V_-nzNyKFvp3diD5TBNB_Z64qLw30lvJqwMVb42VL_QoQCQ4NXnkrc82qaI1OXKdR9jom-COTHpnTNHgeQCuPwgoBN8hQhtR1MhFS1pWeN2AMgW7j4-MmlKCYlB3nwmOnWi5fZqP9JU2yztR4onmhp9rsQsEdgc0SWRrHNbbh_SsoSwcGwibYR8Vji0I8sG0n4BavQTwk6-_7mjKAG7PrDySwtFbertq7xEiP9dE4v28ZcZvvezi2b0IAbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کتک زدن شهروندان مغرب از سوی پلیس هلند
🔹
پلیس هلند در حال کتک زدن و دستگیری شهروندان مغرب است که بعد از پیروزی بر تیم ملی فوتبال هلند به خیابان‌ها آمدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/665004" target="_blank">📅 19:08 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
