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
<img src="https://cdn4.telesco.pe/file/aYLsSkJqCX775jxd-LIct-m1OcXMFrAqZBTsImVIA2OqVLCNAzdSdwDdrG9mWZgxnMl16j-0lVLFULfh_tVlDbnUKGg_b2n71ktSYk0zaBDeCq2HHfdwVVDbss82rWzFH6dclEWCvPgr8wbd0Omlz9OUF0tgjMsOayWJ43bkhp68d_CSTlBCgYFgXcfjbKF6JOPXPXHcboN-WKlEU7WkrBKvSdLUWkhgkqL6Ml2EolbZFE-ZfKSMzDC47LutCt1H0UW7ZaPzl7PT2dapnDdU8gaxvV_c3fBFGFL8nALSNAcRz9kmlEz0FXFQvjb8SpqkoGx9Z-P4HeG7RqjrVyF55A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.2K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 20:15:07</div>
<hr>

<div class="tg-post" id="msg-18684">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256741d101.mp4?token=Bmxf-UBkJZp3b4RkwUD9LfmytXVGxs1_Ri6N5-Bujh8LoYhjSbVfA5yL4Wc0_yspb9Z63W18CAQGC68pMG9PTtTW2QMyRwPd5s6TPC7eD8zmC8Pxf-Sb41WEhjMNxonYTmd8NPYntTF-vfTckMUq5FPx7MlKDkA9chBmZQgUfFfX8uFbwAr5_T1ko1GDHx3DcKDz3OHDzqSWG2pGv3gyPTV5rfD_ayXaQkaxaDuqgFbouLzbRqKB-oXbpF3adFBHPnjY7L0kAvQkfl0TkPNSiP0WfzItb0mueiQdVfOlDq9IBY8yMp96M2006jvs3rorC3kpIcHxWEY4K4rQuLD-dDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256741d101.mp4?token=Bmxf-UBkJZp3b4RkwUD9LfmytXVGxs1_Ri6N5-Bujh8LoYhjSbVfA5yL4Wc0_yspb9Z63W18CAQGC68pMG9PTtTW2QMyRwPd5s6TPC7eD8zmC8Pxf-Sb41WEhjMNxonYTmd8NPYntTF-vfTckMUq5FPx7MlKDkA9chBmZQgUfFfX8uFbwAr5_T1ko1GDHx3DcKDz3OHDzqSWG2pGv3gyPTV5rfD_ayXaQkaxaDuqgFbouLzbRqKB-oXbpF3adFBHPnjY7L0kAvQkfl0TkPNSiP0WfzItb0mueiQdVfOlDq9IBY8yMp96M2006jvs3rorC3kpIcHxWEY4K4rQuLD-dDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی مرکزی آمریکا:   برای اولین بار، یک پایگاه دریایی ایرانی در بندرعباس را با استفاده از قایق‌های بدون سرنشین انتحاری مورد بمباران قرار دادیم.</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/SBoxxx/18684" target="_blank">📅 18:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18683">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">فرماندهی مرکزی آمریکا:   برای اولین بار، یک پایگاه دریایی ایرانی در بندرعباس را با استفاده از قایق‌های بدون سرنشین انتحاری مورد بمباران قرار دادیم.</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/SBoxxx/18683" target="_blank">📅 18:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18682">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فرماندهی مرکزی آمریکا:
برای اولین بار، یک پایگاه دریایی ایرانی در بندرعباس را با استفاده از قایق‌های بدون سرنشین انتحاری مورد بمباران قرار دادیم.</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/SBoxxx/18682" target="_blank">📅 18:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18681">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مارکو روبیو:
دیوان کیفری بین‌الملل در پی آن است که به داوری پاسخگو و بدون پاسخگویی از قانون جهانی جدید تبدیل شود — که توانایی تعقیب و دستگیری شهروندان ما را به دلخواه دارد و حاکمیت آمریکا را به صورت وجودی تهدید می‌کند.
ما به دیوان کیفری بین‌الملل معنای کامل عزم آمریکا را آموزش خواهیم داد.</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/SBoxxx/18681" target="_blank">📅 18:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18680">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ در مورد ایران:   خمینی رفته است. پسر او ۹۰٪ رفته است.</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/SBoxxx/18680" target="_blank">📅 18:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18679">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ:   تنگه هرمز باز است و باقی خواهد ماند، چه با ایران و چه بدون آن.   ما محاصره ایران را که به این دلیل نامگذاری شده است که فقط کشتی‌ها یا مشتریان ایران را از ورود یا خروج باز می‌دارد، دوباره اعمال می‌کنیم.   تمام کشورهای دیگر می‌توانند از تنگه به صورت…</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/SBoxxx/18679" target="_blank">📅 18:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18678">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">پوتین: پاسخ روسیه به حملات دشمن متقابل و چندین برابر قدرتمندتر خواهد بود.</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/SBoxxx/18678" target="_blank">📅 18:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18677">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دبی برنامه‌ریزی برای ساخت بندر جدید برای دور زدن تنگه هرمز دارد</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/SBoxxx/18677" target="_blank">📅 17:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18676">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ:
تنگه هرمز باز است و باقی خواهد ماند، چه با ایران و چه بدون آن.
ما محاصره ایران را که به این دلیل نامگذاری شده است که فقط کشتی‌ها یا مشتریان ایران را از ورود یا خروج باز می‌دارد، دوباره اعمال می‌کنیم.
تمام کشورهای دیگر می‌توانند از تنگه به صورت عادلانه و آزاد استفاده کنند.
ایالات متحده آمریکا از این به بعد به عنوان «نگهبان تنگه هرمز» شناخته خواهد شد، اما به همین دلیل و به عنوان مسئله‌ای از عدالت، به میزان ۲۰ درصد از تمام محموله‌های حمل‌ونقلی، برای هرگونه هزینه‌ای که برای انجام وظیفه تأمین امنیت و ایمنی در این بخش بسیار ناپایدار جهان لازم باشد، جبران خسارت خواهد شد.
فرآیند و تشکیل این ساختار بلافاصله آغاز می‌شود.
از توجه شما به این موضوع سپاسگزارم!</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/SBoxxx/18676" target="_blank">📅 17:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18675">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ستاد مرکزی خاتم‌الانبیای ایران:
ما تحت هیچ شرایطی اجازه نخواهیم داد که ایالات متحده در مدیریت تنگه هرمز دخالت کند؛ نه اکنون و نه هرگز.</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SBoxxx/18675" target="_blank">📅 16:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18674">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ در مورد ایران:
خمینی رفته است. پسر او ۹۰٪ رفته است.</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SBoxxx/18674" target="_blank">📅 16:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18673">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ:
ما دیشب ضربه خیلی سختی به آن‌ها زدیم. هر بار که آن‌ها یک پهپاد می‌فرستند، ما ضربه خیلی سختی به آن‌ها می‌زنیم. اما ما یک توافق داشتیم؛ چیزی که هیچ‌کس نمی‌داند این است که ما یک توافق داشتیم، کار تمام شده بود، و بعد آن‌ها توافق را شکستند. آن‌ها همیشه توافق را می‌شکنند. ما تا به حال ۱۰ بار با این افراد توافق داشته‌ایم. بنابراین ما فقط قرار است ضربه خیلی سختی به آن‌ها بزنیم. و ما این تنگه را حفظ خواهیم کرد و احتمالاً آن را اداره می‌کنیم، ما تبدیل به "نگهبان تنگه" می‌شویم؛ شاید اسمش را بگذاریم "فرشته نگهبان تنگه". و ما باید هزینه‌ای که برای این کار می‌کنیم را پس بگیریم. وقتی این کار را انجام دهیم، پولمان را پس خواهیم گرفت چون کشورهای دیگری که طرف ما هستند بسیار ثروتمندند. و از ما انتظار نمی‌رود که این کار را مجانی انجام دهیم، برخلاف کاری که سال‌ها انجام دادیم. می‌دانید، ما برای ۵۰ سال یا بیشتر از این تنگه محافظت کردیم و هیچ‌وقت پولی بابت آن دریافت نکردیم. آن‌ها همه پول‌ها را به دست آوردند و ایالات متحده فقط... می‌دانید، هیچ... شگفت‌انگیز است. ما هیچ‌وقت سودی نبردیم. ما مجانی از آن محافظت کردیم. اما حالا که می‌خواهیم از آن محافظت کنیم، قرار است بابت محافظت از آن پول بگیریم، پول زیادی هم بگیریم. ما فقط می‌خواهیم هزینه‌ای که برای انجام تمام این کارها و به خطر انداختن نیروهایمان صرف می‌کنیم، جبران شود. اما ما در واقع مردم را در خطر قرار نمی‌دهیم، ما واقعاً داریم نجاتشان می‌دهیم.</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SBoxxx/18673" target="_blank">📅 16:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18672">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ :
ما قصد داریم‌ حملات جدی تری علیه ایران انجام دهیم</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SBoxxx/18672" target="_blank">📅 16:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18671">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ:  ۵.۲٪ از روسای جمهور کشته می‌شوند و  به ۸.۵٪ با گلوله شلیک می شود.  رئیس جمهور بودن خطرناک است.</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SBoxxx/18671" target="_blank">📅 16:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18670">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">این بنده خدا واقعا باورش شده ما برنامه ترورش را داریم!  یک نفر به او بگوید ما از سال 1367 هنوز سلمان رشدی را نتوانسته ایم کامل بکشیم.</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SBoxxx/18670" target="_blank">📅 15:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18669">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ درباره تنگه هرمز:
ما تنگه هزمز را حفظ خواهیم کرد. احتمالاً آن را اداره خواهیم کرد.
ما نگهبان تنگه خواهیم شد و وقتی این کار را انجام دهیم، برای آن جبران خسارت خواهیم شد.
ما به مدت ۵۰ سال از تنگه محافظت کردیم و هرگز بابت آن پولی دریافت نکردیم. ما بیهوده از آن محافظت کردیم، اما اکنون پول درخواهیم آورد.</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SBoxxx/18669" target="_blank">📅 15:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18668">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">در‌ این صوتی وضعیت خر تو خر یمن را توضیح داده بودم .</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SBoxxx/18668" target="_blank">📅 15:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18667">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">وزارت حمل و نقل یمن: حملات دشمن سعودی و هدف قرار دادن فرودگاه صنعا، تلاشی عمدی برای محروم کردن هزاران بیمار و مسافر از ابتدایی‌ترین حقوق تضمین شده‌شان است.
🔹️
ما از سازمان ملل متحد، جامعه بین‌المللی و سازمان‌های بشردوستانه بین‌المللی می‌خواهیم که مسئولیت خود…</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/SBoxxx/18667" target="_blank">📅 15:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18666">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دولت بریتانیا سپاه پاسداران انقلاب اسلامی را در فهرست سازمان‌های تروریستی قرار داد که بر اساس آن، عضویت در این نهاد، شرکت در نشست‌های آن و حمل نماد آن در انظار عمومی جرم کیفری خواهد بود.</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SBoxxx/18666" target="_blank">📅 15:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18665">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">وزارت حمل و نقل یمن: حملات دشمن سعودی و هدف قرار دادن فرودگاه صنعا، تلاشی عمدی برای محروم کردن هزاران بیمار و مسافر از ابتدایی‌ترین حقوق تضمین شده‌شان است.
🔹️
ما از سازمان ملل متحد، جامعه بین‌المللی و سازمان‌های بشردوستانه بین‌المللی می‌خواهیم که مسئولیت خود…</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SBoxxx/18665" target="_blank">📅 15:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18664">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">به نظر می رسد زمان حمله نیروهای مورد حمایت سعودی یا امارات به حوثی ها نزدیک است.</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SBoxxx/18664" target="_blank">📅 14:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18663">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دلیگانی، نایب‌رئیس اول کمیسیون اصل ۹۰ مجلس :    تحویل (ترامپ و نتانیاهو) به ایران، باید یکی از بندهای مذاکرات می‌بود</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SBoxxx/18663" target="_blank">📅 14:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18662">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دلیگانی، نایب‌رئیس اول کمیسیون اصل ۹۰ مجلس :
تحویل (ترامپ و نتانیاهو) به ایران، باید یکی از بندهای مذاکرات می‌بود</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SBoxxx/18662" target="_blank">📅 14:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18661">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پزشکیان:  آمریکایی ها ما را نکنند — تحریم — ما هم کاری به آنها نداریم و حتی با آنها هم برادریم!</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SBoxxx/18661" target="_blank">📅 13:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18660">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">فنلاند یک شهر زیرزمینی در زیر هلسینکی ساخته است که می‌تواند تقریباً یک میلیون نفر را محافظت کند.   زیر هلسینکی، یک شبکه گسترده از ۵۵۰۰ پناهگاه ضد بمب وجود دارد که می‌تواند تقریباً یک میلیون نفر را در صورت جنگ یا حمله هسته‌ای محافظت کند.  اکثر این پناهگاه‌ها…</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/18660" target="_blank">📅 12:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18659">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">فنلاند یک شهر زیرزمینی در زیر هلسینکی ساخته است که می‌تواند تقریباً یک میلیون نفر را محافظت کند.   زیر هلسینکی، یک شبکه گسترده از ۵۵۰۰ پناهگاه ضد بمب وجود دارد که می‌تواند تقریباً یک میلیون نفر را در صورت جنگ یا حمله هسته‌ای محافظت کند.  اکثر این پناهگاه‌ها…</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SBoxxx/18659" target="_blank">📅 12:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18658">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6uyZHbro6jqjH16tYkK7OkhZcp2VtTFatbjjBVjzIW4vcMM9AYDBLqamoZwZYhZrB1t1mQooTdwosw2YMvAcRjZOStUGp-yccjR2OEpHB_6BjWqFgsQOpfn4Ql4E5p5e3i63-laJ0DMe50N6KFQQNStHE37Wm9kJwr7jDcxlKZPnbK58Gsy1yxl_gdpd9Dj5zucx4pe087rIaqi0F5pcrQqQf3-5IL8G3zdXIAQhd0HpbkBEuz_dXEh1c-7JFJHVvHrnQvOyXKYvZxDl0pETFkZcBM6Y29YAlULApVj1Oq60kZpMrVX4LV5J5HTf505DVaZlzceEu8j357DUCcz5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فنلاند یک شهر زیرزمینی در زیر هلسینکی ساخته است که می‌تواند تقریباً یک میلیون نفر را محافظت کند.
زیر هلسینکی، یک شبکه گسترده از ۵۵۰۰ پناهگاه ضد بمب وجود دارد که می‌تواند تقریباً یک میلیون نفر را در صورت جنگ یا حمله هسته‌ای محافظت کند.
اکثر این پناهگاه‌ها برای اهداف روزمره مانند سالن‌های ورزشی، زمین‌های بازی، استخرهای شنا و حتی فضاهای تمرین برای گروه‌های موسیقی راک مورد استفاده قرار می‌گیرند، اما می‌توانند به سرعت به پناهگاه‌های اضطراری تبدیل شوند.
منبع: The Times</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/18658" target="_blank">📅 12:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18656">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار نظامی ایران و جهان</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/732e84f6ce.mp4?token=ucrWsj80DwMVId4wCW_EX1uXTJmz2fI4zFLx-hIBVm3GnyA6t_SiU3Lq5Mu8zBI-OMo7EZHi6JGe1nnZhe58tlEmXl_qctxN8yrQYM4-_zVCgBZ3y3rvKDNBfv4kNG6tdGus_PZuu1yOrKYVE6_DvDjmp7JqFSaqAY2c2pnhkmN1z8a6DQM_a_shwl7ASniheYHb20Q7jcbu-noCFee1L6kHfUaxqm0ZUzXoUmG9Px0J-whJuktnJZq0ZzdYqWA7toaNlyQKe_LidcmtxHJijuwgfR1NrF8zbstQAgzWhczjDsXXa1dwNTlCQeTVcX0T6dDSdzhacirTz9_91HdK8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/732e84f6ce.mp4?token=ucrWsj80DwMVId4wCW_EX1uXTJmz2fI4zFLx-hIBVm3GnyA6t_SiU3Lq5Mu8zBI-OMo7EZHi6JGe1nnZhe58tlEmXl_qctxN8yrQYM4-_zVCgBZ3y3rvKDNBfv4kNG6tdGus_PZuu1yOrKYVE6_DvDjmp7JqFSaqAY2c2pnhkmN1z8a6DQM_a_shwl7ASniheYHb20Q7jcbu-noCFee1L6kHfUaxqm0ZUzXoUmG9Px0J-whJuktnJZq0ZzdYqWA7toaNlyQKe_LidcmtxHJijuwgfR1NrF8zbstQAgzWhczjDsXXa1dwNTlCQeTVcX0T6dDSdzhacirTz9_91HdK8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
قاسمیان: شما نباید بگید آآآمریکاااا بی دوووووو ، باید بگید آمریکا بی دو. یعنی باید با تحقیر بگی
✍🏻
exxon
▪️
@World_Newsly</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SBoxxx/18656" target="_blank">📅 12:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18655">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پزشکیان:  آمریکایی ها ما را نکنند — تحریم — ما هم کاری به آنها نداریم و حتی با آنها هم برادریم!</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SBoxxx/18655" target="_blank">📅 12:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18654">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پزشکیان:  آمریکایی ها ما را نکنند — تحریم — ما هم کاری به آنها نداریم و حتی با آنها هم برادریم!</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SBoxxx/18654" target="_blank">📅 12:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18653">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d5052358e.mp4?token=mH99TnTumq2QcyQrQLCXSDCFwUztMZiyWjnpHxdSYi3pjySzzXZP9PCoJijE7bMYGxwftTdAeeTiYEgWYiLW-91rxC_35l8PCya26eCb-C829rovzEK4huFtnfzxz09wkBNHVO87EwzHoYYvu6BrGwXGAlaDTAJ_HkkLUpshyfu-WvuvWD7OQIvVRRv6-8k-hTPRoP7fKFpc-i334Hq7AOo9I6eOrupN2BJZWG6Oc3GDn53OHv3kNdDbSHaPmGPwpkxrauIZ5xB85WTwTMCu2lAioQgfAh-6KSS44lFHbtLYJQtjIEYnxL1dcqYoQu6PXMVcRUw3d810Zu-lcFFxDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d5052358e.mp4?token=mH99TnTumq2QcyQrQLCXSDCFwUztMZiyWjnpHxdSYi3pjySzzXZP9PCoJijE7bMYGxwftTdAeeTiYEgWYiLW-91rxC_35l8PCya26eCb-C829rovzEK4huFtnfzxz09wkBNHVO87EwzHoYYvu6BrGwXGAlaDTAJ_HkkLUpshyfu-WvuvWD7OQIvVRRv6-8k-hTPRoP7fKFpc-i334Hq7AOo9I6eOrupN2BJZWG6Oc3GDn53OHv3kNdDbSHaPmGPwpkxrauIZ5xB85WTwTMCu2lAioQgfAh-6KSS44lFHbtLYJQtjIEYnxL1dcqYoQu6PXMVcRUw3d810Zu-lcFFxDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
آمریکایی ها ما را نکنند — تحریم — ما هم کاری به آنها نداریم و حتی با آنها هم برادریم!</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/18653" target="_blank">📅 12:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18652">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔹
حسین شریعتمداری، مدیرمسوول و نماینده ولی‌فقیه در روزنامه کیهان، در یادداشتی، بابت مرگ لیندسی گراهام، به عزراییل، گلایه کرده که چرا:   «پیشدستی کردید و قبل از ما حسابش را رسیدید... از خدا اجازه می‌گرفتید و کمی صبر می‌کردید تا این عنصر پلید را با دست خود راهی…</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/18652" target="_blank">📅 12:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18651">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HivKhIOetMcSy0f6t5uw32iQ9XuLPfosH9Guv2MEwa-vGC56t61Awk00IUavNk8sJ34mQKBTCTf1FhoSB6sKMCteLYjeYHTExTK7dewAa59W-xWLLbMUs8vAeokVQkzsCmZBLkuovavi-_4imGKb2jXUV2pWZy7Xrv-ERfnVg7xMwbXf1a5oyAKz8mnk5oqOhZH2YboSUuW7Sf2P2LeogWxd9CYJd77Cb7-TlEzejaNBdLTcfyoQZd1KvtmAdAhCQz5C9wiofvNlu8LdWRcepeP_ZjGBpUksSEybSFRd4MtnFIbOYsh2rP0cckJ3pFknfM0OdPwBFAwvLHZXlRYw2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
حسین شریعتمداری، مدیرمسوول و نماینده ولی‌فقیه در روزنامه کیهان، در یادداشتی، بابت مرگ لیندسی گراهام، به عزراییل، گلایه کرده که چرا:
«پیشدستی کردید و قبل از ما حسابش را رسیدید... از خدا اجازه می‌گرفتید و کمی صبر می‌کردید تا این عنصر پلید را با دست خود راهی جهنم کنیم.»</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/18651" target="_blank">📅 12:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18650">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGAKogzkRvaazBJoBni-dRLnBobV21CEtlSJO7nTxN7GhWrjL5bOV-f3Z3QdN7ZyC0lxziLdyG7JMTVi_OHN2DWT72cGaagIrOt6NDeOOeZVg7a1CLfOyc2rjklRnrH0ZxbfPpHXY_rW41snHHo5xqE6S2oEuM7I_nQpZxWnarxqSYN6-ExGeeyBRoM9IDnzMSpMdRmwJ9x_eBR_KmEYmcC_A1lfuxSiCcCIgEeM7r65wuv4q8r02T5B_TnEcYVI8u03_rdCHP0PyYxLK6Pt9zDwmrrglMjJWdhr8ha2idn-Qw7uNGnfRGnvGklq6xC4TY_Ujo2ik1KF9JF_wtCMdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک در این لحظه کاهش اساسی یافته و کاهش تنش ها را پیش بینی می کند.</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/18650" target="_blank">📅 11:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18649">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سومین پرواز از سوی دولت روسیه از مسکو به سمت ایران به پرواز در حال انجام است.  هواپیماهای توپولوف ۱۳۴ معمولاً برای انتقال افراد مهم و مقامات رده‌بالا استفاده می‌شوند.</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/18649" target="_blank">📅 11:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18648">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سخنگوی وزارت امور خارجه ایران در مورد فوت لیندسی گراهام:
عزرائیل عدالت را جاری می‌کند.
برای چنین فردی که میراث زندگی‌اش سرشار از کینه و حمایت از تجاوز بود، چیزی جز یک سابقه تاریک در ذهن مردم باقی نخواهد ماند.
مرگ این سناتور پرخاشگر و با دهان گزنده، قطعاً قلب هیچ فرد آزاده‌ای را آزرده نخواهد کرد.</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/18648" target="_blank">📅 11:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18647">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">به نظر می رسد نیروهای آمریکایی دیشب از مهمات ویژه برای تخریب تونل‌ها استفاده کردند تا یک پایگاه موشکی زیرزمینی را در نزدیکی شهر دزفول، در پایگاه چهارم شکاری نیروی هوایی  مورد حمله قرار دهند.</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/18647" target="_blank">📅 11:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18646">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سنتکام:
موج دیگری از حملات را علیه ایران به پایان رساندیم
تامپا، فلوریدا —
فرماندهی مرکزی ایالات متحده (CENTCOM) در ۱۲ ژوئیه موج جدیدی از حملات تهاجمی علیه ایران را به پایان رساند و با استفاده از مهمات دقیق، ده‌ها هدف در چندین مکان را هدف قرار داد تا توانایی ایران در ادامه حمله به کشتیرانی بین‌المللی که از تنگه هرمز عبور می‌کند را تضعیف کند.
نیروهای CENTCOM به سیستم‌های دفاع هوایی نظامی ایران، سایت‌های راداری ساحلی، توان موشکی و پهپادی و قایق‌های کوچک حمله کردند و برای اولین بار از هواپیماهای جنگنده ایالات متحده، کشتی‌های دریایی، پهپادهای حمله هوایی یک‌طرفه و پهپادهای حمله دریایی یک‌طرفه استفاده کردند.
تنگه هرمز یک مسیر دریایی حیاتی برای تجارت جهانی است. ایران کنترل آن را در دست ندارد.
نیروهای ایالات متحده برای اطمینان از اینکه آزگان دریانوردی برای کشتیرانی تجاری باقی می‌ماند، حتی با وجود تهاجم بی‌دلیل، آزار و اذیت، تهدیدات و اعلامیه‌های خودسرانه مداوم ایران، آماده و مهیا شده‌اند.
@U_S_CENTCOM</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/18646" target="_blank">📅 10:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18645">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">آغاز خاموشی‌های برنامه ریزی شده در کشور!   مدیر امور مشتریان شرکت توانیر با اشاره به برنامه‌ریزی خاموشی‌های احتمالی:   این برنامه‌ها دو روز قبل اعلام می‌شوند و برای دو روز آینده نیز برنامه قطعی برق در کشور اطلاع‌رسانی شده است.</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/18645" target="_blank">📅 10:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18644">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">آغاز خاموشی‌های برنامه ریزی شده در کشور
!
مدیر امور مشتریان شرکت توانیر با اشاره به برنامه‌ریزی خاموشی‌های احتمالی:
این برنامه‌ها دو روز قبل اعلام می‌شوند و برای دو روز آینده نیز برنامه قطعی برق در کشور اطلاع‌رسانی شده است.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/18644" target="_blank">📅 10:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18643">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MF_8qxmNyRdNsTZNSrR7OG4nUgOIWJ9mOmk_tSv8T_P7wrZGISLrsCwTm7BztH-TTQgJce1tMlkFhEMQe7PXi4SHNjW-TOvgVUEZVx16v4drC572ZWL2DPHs140YWQ3zYLnwvBOv_4lais7RIhU2OTUXegXbS1egjjbHiYgJZHVJp7zk7iEnRYs0FypzeplTNoCi-AfJfNmK99mH3MG2trP0fU8NnSIrSZhgrmzseqmD2NlOdukkNa3Z8F_O4_pMyjj2TD1G89VL69vSziya4CXzFsn3RldODySMRzJrIvQGHZZuyGaocx97lqp7hpYBsfi7KoqMHvSSroXgiIsOgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک در این لحظه کاهش اساسی یافته و کاهش تنش ها را پیش بینی می کند.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/18643" target="_blank">📅 09:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18642">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18642" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 6
دوشنبه 13 جولای 2026</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/18642" target="_blank">📅 09:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18641">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">وزیر امور خارجه آرژانتین، پابلو کیرنو، ساکنان جزایر فالکلند را "جمعیتی که به طور مصنوعی وارد این منطقه شده‌اند" توصیف کرد و از بریتانیا خواست تا مذاکرات مربوط به حاکمیت این جزایر را آغاز کند.</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/18641" target="_blank">📅 09:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18640">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وزیر امور خارجه آرژانتین، پابلو کیرنو، ساکنان جزایر فالکلند را "جمعیتی که به طور مصنوعی وارد این منطقه شده‌اند" توصیف کرد و از بریتانیا خواست تا مذاکرات مربوط به حاکمیت این جزایر را آغاز کند.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/18640" target="_blank">📅 09:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18639">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ywssgm_QqXk4O_O5LQYnLx4mA4n13SP3epMdUfrbQ6dxW-3J0BxEh4_pP_q2lTPtyXvcW6VbRiN1gho7895UFVE7Rtf991LBuEibrDxWiHQTEIzLfm2DobyHz1kh0IVXAEn7wZCqAF2AG2CuqBjlHDUKxwXKAmPKRv80NzUs86MHRkltwzTjQSEAWyNUNc4PTobvouoVLnDgjv0bI7l5J79kZ9T8kzxAKdOOtbwr8cN_3g4exY6FvlXpYxDdZFld9CrWJsy4jX2_6cOOcVsyUnRNz2OWhFQyrBYk0m9qmWHYndil_7iklzD4WuCbCiI665LxeF_UAPZDJgJdfqpwlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گستره جغرافیایی حملات دیشب آمریکایی ها</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/18639" target="_blank">📅 08:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18638">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">— سپاه پاسداران:
«در مرحله چهارم عملیات «چشم در برابر چشم»، نیروهای زمینی قهرمان سپاه پاسداران پایگاه موشکی زمینی به زمینی ارتش ایالات متحده در کویت را هدف قرار دادند و دو پرتابگر موشکی هیمارس و انبارهای مهمات را آتش زده و به طور کامل نابود کردند».</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/18638" target="_blank">📅 08:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18637">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده اعلام کرد که برای اولین بار از شهپادهای دریایی انتحاری  برای هدف‌گیری دارایی‌های ایران استفاده شده است</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/18637" target="_blank">📅 08:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18636">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">سومین پرواز از سوی دولت روسیه از مسکو به سمت ایران به پرواز در حال انجام است.
هواپیماهای توپولوف ۱۳۴ معمولاً برای انتقال افراد مهم و مقامات رده‌بالا استفاده می‌شوند.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/18636" target="_blank">📅 08:08 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18635">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">آمریکایی ها دارند با هیمارس و از کویت، شهرهای خوزستان را شخم می زنند!</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/18635" target="_blank">📅 02:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18634">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1MYWIBtQSg-xsGdZSTShoqCX_yyfF4YFTeRsrpQWzFj56mRpChTWE_uUOlI2TCQVAFICKUfniKJjrNhXAiJ6Y8ABEp-xXilamr0f9Y8ZFapuTSh2m_L-c8tKCAQr0Bv4SHvWi2lyj1ELFEIBhcxjaZjVRm--bfvzeHLGPuo0rPn55B8Mrh563A_AujrtCF0auc7b2zPXOw4Xele4uTCulrop-6l9Cz7wRvVNnI7eBzGY1kBeDmxC2E6WcxhF_yCqUx8u7Bg4XSU31KjMHqfbjP66pM9W8Q-4hlBTvoFrRpKWl4iLqX28Bs7nTApj84Hmqzt3U_EVfthRO_fz4YvGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربها وقتی میفهمند دوباره ما برای آزادی قدس داریم خودشان را میزنیم!</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/18634" target="_blank">📅 02:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18633">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی:  هشدار فوری به تمامی شهروندان و ساکنان کویت، بحرین و امارات متحده عربی:  با توجه به تبعیت حاکمان شما و استفاده از برخی مناطق مسکونی در کشورهای مذکور برای شلیک موشک‌های زمین‌به‌زمین به‌سوی ایران، از شما می‌خواهیم نهایت احتیاط را…</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/18633" target="_blank">📅 01:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18632">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی:
هشدار فوری به تمامی شهروندان و ساکنان کویت، بحرین و امارات متحده عربی:
با توجه به تبعیت حاکمان شما و استفاده از برخی مناطق مسکونی در کشورهای مذکور برای شلیک موشک‌های زمین‌به‌زمین به‌سوی ایران، از شما می‌خواهیم نهایت احتیاط را به خرج دهید.
در صورتی که هرگونه سامانه یا سکوی پرتاب موشکی در نزدیکی مناطق مسکونی خود مشاهده کردید، لطفاً در اسرع وقت آن منطقه را ترک کنید. همچنین از پایگاه‌ها و تأسیسات نظامی آمریکا فاصله بگیرید و از نزدیک شدن یا عبور از اطراف آن‌ها خودداری کنید.
از تمامی شهروندان و ساکنان درخواست می‌شود این مناطق را فوراً تخلیه کرده و بدون هیچ‌گونه تأخیر به مکانی امن و با فاصله مناسب منتقل شوند تا جان و امنیت خود را حفظ کنند. ما پیش‌تر بارها و به‌طور صریح به حاکمان شما درباره خطرات ادامه این مسیر و به بازی گرفتن سرنوشت مردمشان هشدار داده بودیم.
با این حال، آنان تصمیم گرفتند به مسیر تبعیت کورکورانه ادامه دهند و تصمیماتی را اجرا کنند که نه بازتاب‌دهنده اراده مردمشان، بلکه تحمیل‌شده از خارج از مرزهایشان و در غیاب هرگونه حاکمیت واقعی است. بنابراین، مسئولیت کامل تمامی پیامدهایی که در نتیجه این مسیر به وجود خواهد آمد، بر عهده آنان خواهد بود.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/18632" target="_blank">📅 01:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18631">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سنتکام:
ساعت ۵ بعدازظهر به وقت شرقی امروز، نیروهای فرماندهی مرکزی ایالات متحده آغاز به انجام حملات بیشتری علیه ایران کردند تا توانایی آن‌ها برای حمله به دریانوردان غیرنظامی و کشتی‌های تجاری که به صورت آزادانه از تنگه هرمز عبور می‌کنند را تضعیف کنند. فرمانده کل قوا دستور این حملات را برای پاسخگویی نیروهای ایرانی صادر کرده است.
@U_S_CENTCOM</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/18631" target="_blank">📅 01:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18630">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">برای عربها تفاوتی که جنگ برایشان به ارمغان آورده این بوده که پیش از جنگ اسراییل آن سو مشغول کار‌ خیر با ایشان بود و ما ادعا میکردیم میخواهیم از شر جهود رهایشان کنیم اما اکنون خودمان هم از این سو مشغول مالش شان شده ایم.  همین</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/18630" target="_blank">📅 01:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18629">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">انفجاراتی متعدد در نزدیکی شهر سیریک در ایران شنیده شد: تلویزیون دولتی.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/18629" target="_blank">📅 00:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18628">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32bc32908f.mp4?token=s1by-bWYMdOcKkhTKAO_6JsHub1UcjmpVQJ0hus3BMnPtxKMN0XnIiL3ew53BUvwPVq7_5PyCv5HEGvUBharcoOzbS68vDmh_DZR0gRCctMS5zP6UZUc7gymVkC_n01CVWwpHlX_CxQ_XVLy-F_gsOMndf6hAuNDB8g7k8UGXLLfm0CzlEv7ugccnl48WbdKx3nQlVPsC7_9e0Rd3A_Zbrwf5jzM9j-FOJiaZq-zRs4jp071MVCd-hcNUPbM3YDOvR-z-2qUZz7Omv5AJB3Dmyr82_m6j86V5LUv4UonFXlyGxypS_Mh7rqO9HHW-PKHdO35wG1cypF5F53JSZnt4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32bc32908f.mp4?token=s1by-bWYMdOcKkhTKAO_6JsHub1UcjmpVQJ0hus3BMnPtxKMN0XnIiL3ew53BUvwPVq7_5PyCv5HEGvUBharcoOzbS68vDmh_DZR0gRCctMS5zP6UZUc7gymVkC_n01CVWwpHlX_CxQ_XVLy-F_gsOMndf6hAuNDB8g7k8UGXLLfm0CzlEv7ugccnl48WbdKx3nQlVPsC7_9e0Rd3A_Zbrwf5jzM9j-FOJiaZq-zRs4jp071MVCd-hcNUPbM3YDOvR-z-2qUZz7Omv5AJB3Dmyr82_m6j86V5LUv4UonFXlyGxypS_Mh7rqO9HHW-PKHdO35wG1cypF5F53JSZnt4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واقعا این  هواداران نروژی و انگلیسی را دارم میبینم یک جوری فوتبال میبینند انگار هیچ چالش و مشکل دیگری در زندگی شان نیست!</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/18628" target="_blank">📅 00:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18627">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سنتکام:
🚫
ادعا: تبلیغات ایران امروز ادعا کرد که سه نظامی آمریکایی در کویت بر اثر حملات ایران کشته شده‌اند. این ادعا نادرست است.
✅
واقعیت: هیچ گزارشی مبنی بر کشته یا مجروح شدن نظامیان آمریکایی در این منطقه وجود ندارد. تمام پرسنل در وضعیت سلامتی هستند.</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/18627" target="_blank">📅 00:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18626">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">منابع عربی از کشته و زخمی شدن چندین سرباز امریکایی در پی حملات سپاه به مواضع آمریکا در کویت خبر  می دهند!</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/18626" target="_blank">📅 00:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18625">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">این هم یکی دیگر!</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/18625" target="_blank">📅 23:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18624">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پست جدید ترامپ !</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/18624" target="_blank">📅 23:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18623">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRg2yKrXECFdjz04nYXtc9TzVw5quOL7X-cm9UlJLm-K91ir2FBkbvb4ydwMs40b4GgFx1mbeqie4dkGehBu61VnGBeF42Bt7va38Gbci-NLot1cZwbssyyunbX7BF2SByOBjDdB3kJT1oYeo09gB2E5XzN5WSPdq2hHE6Kvpne9gx94HNV1u1tQvxAamkz6gEbfHZCpuHXobZkdYux9tB3ApzTTZ3fy5MToGQxDF-8xHSI9DSfH2fsl3zQ_WdzWYtAdGrVVsWOYDSgT285dlvpgPO4flixa1ejRxg0N0h0gtWletiyIjezt0Ha911InpwfFiRAtd_V__n0It4XwAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ !</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/18623" target="_blank">📅 23:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18622">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkDWtXBDO41pe43MSYYDtiuNXiIgoz-TQUSdgfwPOHFudCkNHup2PWBPRiJsajQUq6KpcGGGkMP9SU7scl9QHT0g4RjF7wwJqknaDuGORZy1mQVNW5KvtCxo47eQuZHmodC_M5PsMDDA1d8iWdy8DpTFscak_L3QMiuEfSWrM889bPq7KsjPDgdVjXiVm3Hk2LcKC66v4I4JchDwojGX1s3hESrCyOsW5EBS2GWZ5hiM--LU-kDBwm6FhrTpLfpcXownBMMK9KAOufslOwpIosnADzwvjffR7-VBZa_Sf9pcbRnSPIMFmAXf10EQQfMqvDrLBkZjJklfVh6_cJyStQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">— هواپیماهای هشدار زودهنگام نظامی و سوخت‌رسانی هوایی ارتش آمریکا از پایگاه‌هایی در اسرائیل، عربستان سعودی، امارات متحده عربی و قطر به پرواز درآمده‌اند، در کنار فعالیت‌های مربوط به یک فروند P-8 Poseidon که از بحرین عملیات می‌کند.  ارزیابی‌های فعلی حاکی از آن…</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/18622" target="_blank">📅 23:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18621">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">منظورشان همین هفت هشت هواپیماست.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/18621" target="_blank">📅 23:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18620">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pY6L5f5LDf7Nn2KTYgAyx7RT5xdq-OF9vsmAccY38i7BcAfLQbjUgj_c4Vxya-rxL13kXYnYlb8nrmwWHKAAao32e4Phgx5E7RVGW8sXKMVBCO6xjTOpzJxucR-JXLSVGw2tb3OoOsJ3-tl1UMFzKLOSrqZ8S5yodpBiR5VE5ebWNjyrasNWXEVC9vJimmNPgfJgAKiF0WduDsJuwYT5jONAwIz2bxoeQD6sz0Cutsh2iixW-mCAbPDveMbwTQ8Sw2GX1O2pxfakJ18b9ziOmSztpYOn8k-x-3BeYwZlc4BFLlfhjqZHqsq8cmxQnxry0jgRMhzfBP6fQ6ITkDjJvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگنده های ارتش جمهوری اسلامی ایران بر فراز حریم هوایی مناطق مرزی غرب کشور به پرواز درآمدند</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18620" target="_blank">📅 23:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18619">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">آسمان کشور در حال کلیر شدن...</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18619" target="_blank">📅 23:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18618">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خداوکیلی این چه زندگی است....</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/18618" target="_blank">📅 23:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18617">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMLfc5N3vGY309qtYI14LBDYtZU3Q11zwG_AqX2OFR7MnuFu7yrt7OZnosJ83pHAVgWl3YuX8TMf_T29K5rVJlqoDUcxI8y_5XxSGzxVPsZxSUm9AMrW1YNaVYwuXyjydBY-RK-JCLNNgr96knSSrwEjsQlVgoSXxZV37mbT7VKfQsV-MPhJwGVJ0EbBUvhCu5jppHLTm2C-rW6ulzOV5J1UVa8_k8vzOzi9CTRnEhmFFQ1LA4F_4p-JnfZP4SGAp0NvDfLGIoqlGWhw6-mLTIqMHWvKkDH0cmexH19I9V_QtwqGwVkwZjh9YytOPmfNda60S8XfwUHd2dPXzfre4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">— هواپیماهای هشدار زودهنگام نظامی و سوخت‌رسانی هوایی ارتش آمریکا از پایگاه‌هایی در اسرائیل، عربستان سعودی، امارات متحده عربی و قطر به پرواز درآمده‌اند، در کنار فعالیت‌های مربوط به یک فروند P-8 Poseidon که از بحرین عملیات می‌کند.  ارزیابی‌های فعلی حاکی از آن…</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/18617" target="_blank">📅 23:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18616">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">— هواپیماهای هشدار زودهنگام نظامی و سوخت‌رسانی هوایی ارتش آمریکا از پایگاه‌هایی در اسرائیل، عربستان سعودی، امارات متحده عربی و قطر به پرواز درآمده‌اند، در کنار فعالیت‌های مربوط به یک فروند P-8 Poseidon که از بحرین عملیات می‌کند.
ارزیابی‌های فعلی حاکی از آن است که احتمال حملات نظامی در دو تا سه ساعت آینده وجود دارد.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/18616" target="_blank">📅 22:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18615">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دیروز عباس سعداکبر عراقچی عمان بود امروز سپاه عمان را زد
🤣
🤣</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/18615" target="_blank">📅 21:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18614">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">لازم به ذکر است که جناب خضریان عضو کانال ما هستند و پوزیشنهای سنگین Long روی نفت دارند</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/18614" target="_blank">📅 21:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18613">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گفته می‌شود ایران در جریان سفر ترامپ، رئیس‌جمهور آمریکا به ترکیه، تلاش کرده است او را ترور کند.
اطلاعات ارائه شده توسط یک منبع خارجی که به مقامات آمریکایی در مورد این توطئه ادعایی هشدار داده بود، باعث شد تا در آخرین لحظه، هواپیمای مورد استفاده رئیس‌جمهور در پرواز بازگشت به واشنگتن تغییر کند.
— یدیعوت آحارانوت |</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/18613" target="_blank">📅 21:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18612">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">تکرار حرف مدیر Secret Box از سوی دکتر خضریان:  علی خضریان، عضو کمیسیون امنیت ملی مجلس:   مسئولان دستگاه دیپلماسی ایران در دنیای موازی زندگی می‌کنند  آمریکا و ترامپ می‌گویند که ما از توافق‌نامه خارج شده‌ایم و آتش‌بس تمام شده است بعد مذاکره‌‌کنندگان ایرانی می‌گویند…</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/18612" target="_blank">📅 21:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18611">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اینها هم رسماً بیکار هستند. خود ترامپ دیروز گفت از دید او آتش بس تمام شده و دیشب آمریکایی ها جنوب کشور را شبیه جنوب لبنان کردند آن وقت اینها می گویند این کار نقص بندهای 1 و 5 یادداشت تفاهم است!</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/18611" target="_blank">📅 21:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18610">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">لابد دیده ایم آزادی قدس از دست یهود سخت است گفته ایم کویت و بحرین را از دست خود عربها آزاد کنیم.  به نظر من که ساده تر و بهتر است.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/18610" target="_blank">📅 21:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18609">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ادامه پرتاب موشک از ایران</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/18609" target="_blank">📅 19:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18608">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhbY5GsTbHGIm3QUPUwQxlargANv0rQKcqqimhZLTdREAgSX2_cK8UxZqzdHz_-qe8bzBOU_mSUjOBtKGEJ1lGd_ritP3usla8rg3Wl_EG3A57i6ZulVPmjZEOarCPx6hNJPhYODwF3olAbOuBTLLqMWMNwEJFO5IzOChWBpqg0eZLiTPMsaVcCyaHPrABow-vC2V_mMRCPg57-BRkrl_BL1ApRgRiQP8jxnK6EQ2ioyiYMLG7GMwtRnNZjLxI9TA0iSyG1sfS36yk8gTmuG-LlOQfwRpPu63mkPw0hLxU-EQFKI7y7gw454H34kjBKLs4n2jB3g_sxw1hth4mQMJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راستی این حرامزاده هم دیشب سقط شد
مردی که قطر‌ را به مرکز ترویج تروریسم اخوانی تبدیل کرد و از حامیان اصلی حماس و القاعده‌ در سوریه هم بود.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/18608" target="_blank">📅 19:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18607">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">منابع عربی از کشته و زخمی شدن چندین سرباز امریکایی در پی حملات سپاه به مواضع آمریکا در کویت خبر  می دهند!</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/18607" target="_blank">📅 19:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18606">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دود غلیظ پس از برخورد موشک های ایران به جایی در کویت</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/18606" target="_blank">📅 19:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18605">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">در حالی که سنتکام میگوید تنگه هرمز باز است، اژدهای بندر نظر دیگری دارد!</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/18605" target="_blank">📅 19:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18604">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">انفجارهای جدید در کویت!</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18604" target="_blank">📅 19:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18603">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TWc7fxQSe4VDthCHu898TnfWaOIU_Jxf4Zan5ZGy1e2X1xcOlYJ5Ixlwzmr42wKWU0SgrysdSguL7S6OIvKodxkI2NPmCAIjF0tj2Ia_yA6NV-UTFqHRak8_iytIIm8IqleF1QtMuHzB-kNeX7MKEI2mEmnLEmb5E4RK9s--wTOHV2j1xoWDN0XB4XTyA0m2T3WdSiT9atPp1hpeH1Ii0H1lNDbXz_A1N-ZlSKM_mu5ju2dJtKt8Jl6A_IhRq92_nKxb_Y1DOLN_lnrrRCAxF_vpJ3WKcm5uruPbl2RshHTWX_4Ddu7ry1JjkoLbDJzvmXeYC9pnONmlu8Io7SZV7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش کنایه‌آمیز مرندی به مرگ گراهام:   حیف شد؛ کاش قبل‌از رفتن به جهنم قیمت فردای نفت را می‌دید!</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/18603" target="_blank">📅 19:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18602">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">برای عربها تفاوتی که جنگ برایشان به ارمغان آورده این بوده که پیش از جنگ اسراییل آن سو مشغول کار‌ خیر با ایشان بود و ما ادعا میکردیم میخواهیم از شر جهود رهایشان کنیم اما اکنون خودمان هم از این سو مشغول مالش شان شده ایم.  همین</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/18602" target="_blank">📅 19:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18601">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">لابد دیده ایم آزادی قدس از دست یهود سخت است گفته ایم کویت و بحرین را از دست خود عربها آزاد کنیم.
به نظر من که ساده تر و بهتر است.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18601" target="_blank">📅 19:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18600">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">برای عربها تفاوتی که جنگ برایشان به ارمغان آورده این بوده که پیش از جنگ اسراییل آن سو مشغول کار‌ خیر با ایشان بود و ما ادعا میکردیم میخواهیم از شر جهود رهایشان کنیم اما اکنون خودمان هم از این سو مشغول مالش شان شده ایم.
همین</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/18600" target="_blank">📅 19:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18599">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDlzzsNJ1Lliaf4ffghDgL_ExkmSyao7ps0pNRCDOgUH76ntM3GWnolJ_2Y1_x-tFZ-Uykcev-XkKXh6My_kGapR0Zjzwekr_Orh1vQm6kweK2fEP0z1ANP0DIElp9ujqKIcZShbji5DrYez7XaQOvGdPAozeSbnrdg6agSvyhX79Z4f8JdRMviNsujUfW7qWnQkKJCfA7H4oYumvpCHDf7x-5HlNu_UEZ4xQKrUnI20OjLi6hK3Ne7z7jii4oIggIhjgnFTrd3P23trbELx0i6hH1kbLeVy_8upVh5cE6Rnd4t4CyaDix4C_4l_Y4Zoh1sTki23f_sptdh3FYGs7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارهای جدید در کویت!</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/18599" target="_blank">📅 18:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18598">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">انفجارهای جدید در کویت!</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/18598" target="_blank">📅 18:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18597">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامپ :  آنها (ایرانی ها) دیروز با توافقی موافقت کردند که از نظر ما کاملاً ایده‌ آل بود،دیگر هیچ برنامه هسته‌ ایی در کار نبود و از همه‌ چیز دست کشیدند  اما پس از آن، اتاق مذاکره را ترک کردند و کمتر از یک ساعت بعد، یک پهپاد به سمت یک کشتی شلیک کردند</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/18597" target="_blank">📅 17:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18596">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">خبرنگار: تنگه هرمز باز است یا بسته؟  ترامپ: «تنگه هرمز باز است و من نمی‌خواهم در مورد آن صحبت کنم چون می‌خواهم به یاد لیندسی گراهام باشم.  قبل از تماس تلفنی به شما گفتم.»</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/18596" target="_blank">📅 17:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18595">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سنتکام:
🚫
ادعا: فرمانده نیروی دریایی سپاه پاسداران انقلاب اسلامی اخیراً در رسانه‌های دولتی اعلام کرد که کشتی‌های خارجی ممکن نیست بدون شناسایی، ردیابی و پایش توسط نیروهای ایرانی از تنگه هرمز عبور کنند.
✅
واقعیت: ایران بر تنگه هرمز تسلط ندارد. این تنگه همچنان…</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/18595" target="_blank">📅 17:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18594">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">واکنش کنایه‌آمیز مرندی به مرگ گراهام:   حیف شد؛ کاش قبل‌از رفتن به جهنم قیمت فردای نفت را می‌دید!</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/18594" target="_blank">📅 17:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18593">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQDwz7Oihni_IG_zgkg9znosUnHNgfC4VGqwQU3fGmWph_JOCuA06fsRRxjqnZGmJXfmUsY-OyUO21gz5f0asPsvTWLoblFG6aeJvGaS1mk2PlHTX00UjERfMA6DdEeiiT9GxJ3kLojhAB0lwA1ASSmmM5JdPOVOGcciW-uGmDINh6p9sXt4GHRFNcorQdPdNLVcv7EVzBdzXa-8khLlfGEG8W0SOIjya0JwdTgm74KykCV0Npy1D_f9H5r89W5O8xZckqv-KpbhrZOtOtDt69uWzYDtLpYy9nNCmMLXxAqyDOIDQYFqTnvpEG6EISaSgnyuFDGIfdW1ExyDY_8FTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H2</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18593" target="_blank">📅 17:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18592">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سنتکام:
🚫
ادعا: فرمانده نیروی دریایی سپاه پاسداران انقلاب اسلامی اخیراً در رسانه‌های دولتی اعلام کرد که کشتی‌های خارجی ممکن نیست بدون شناسایی، ردیابی و پایش توسط نیروهای ایرانی از تنگه هرمز عبور کنند.
✅
واقعیت: ایران بر تنگه هرمز تسلط ندارد. این تنگه همچنان یک آبراه بین‌المللی باقی می‌ماند. نیروهای ایالات متحده مستقر و آماده هستند تا اطمینان حاصل کنند که این وضعیت حفظ شود.</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/18592" target="_blank">📅 17:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18591">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">توانیر: کاهش ظرفیت شبکه برق به دلیل آسیب‌های گسترده‌ در جنگ
‌
مدیرعامل شرکت توانیر:
حدود ۴۲۰۰ مگاوات از توان شبکه برق کشور کاهش یافته و بیش از ۲ هزار نقطه از شبکه دچار آسیب شده‌اند.
با وجود فشار مضاعف گرمای تابستان بر شبکه، عبور کم‌چالش از روزهای پیش‌رو در گرو همراهی مردم است.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/18591" target="_blank">📅 16:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18590">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYozdzqDH2v88bs1UK3B45Kd9v8t6YBk_XHkvuLrhZaUpcVeEW2u0wgwCkp8GdtAJViWI08I_NgEbwBeZhaNDwCfdU6H_UjpYZyVnXIkJpLa0F3ZK32PXBr7c69NJ9_C3pAQ4PaALjtGhdFlpwzaL4aEdueXZeU7pAvsBHH2N68zPIizW9M7i5rVyP99i6F6LHs6Y_lcU45LJs-RD3-Z5Nc1uXDpCee_DxWf7kCOXfQfpqOtfu8dHCRjlqEnM_WeaNtI-8SYfPDfSV1lkugSxgGzW5ky2SEV1BICv4FrUFCIwUOZGxRYCKkIRL_MvWCvPCuHvPaRuZrTL96liYXv8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمان:   ما از ایران درخواست می کنیم به ارزش های اخلاقی و فرهنگی که دو کشور را به هم وصل می کنند، احترام بگذارند</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/18590" target="_blank">📅 16:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18589">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">عمان سفیر ایران در مسقط را احضار و یادداشت اعتراضی در مورد حمله ایران به این کشور را به او تحویل داده است.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/18589" target="_blank">📅 16:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18588">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">عمان سفیر ایران در مسقط را احضار و یادداشت اعتراضی در مورد حمله ایران به این کشور را به او تحویل داده است.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/18588" target="_blank">📅 16:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18587">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دیروز عباس سعداکبر عراقچی عمان بود امروز سپاه عمان را زد
🤣
🤣</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/18587" target="_blank">📅 16:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18586">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">تنها راه نابودی اسراییل این است که با آنها رابطه سیاسی برقرار کنیم و بعد عباس آقا را بگذاریم سفیر دایمی مان در اورشلیم !</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/18586" target="_blank">📅 15:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18585">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دیروز عباس سعداکبر عراقچی عمان بود امروز سپاه عمان را زد
🤣
🤣</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/18585" target="_blank">📅 15:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18584">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یعنی وسط کویر لوت هم یک قایق کاغذی کاردستی پنج سانت و ده سانت چپه بشود چند هندی گم می شوند!</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/18584" target="_blank">📅 15:51 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
