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
<img src="https://cdn4.telesco.pe/file/J6KcmeRY7xxAcRrqbvEsL8tGxE1IYZPA_x7ZyZDhgqsa-FxI5TxDmqt_cieWiMNeVXu4m4io4lpVGk2b7EmYF596Pj5VGC-_b7OkBthCMkohVBlc9PdJs5vmNOLqMoSWbd3-J30R6bmXWE9EzBEROrIz2a6-B8scRSd2EazueSSLvNU9h8PG2KVcH46PdScI1rg66BWqmLJ5gBq6X3uh7Epw7XWhtowDn4-PZk0COt7SbcO-Ir_Y3Nuw03pXqwWP4ianlB65AhpRnPYiisetuI9jMffvtXTZq1_BXTAM3gERFWOgcxCq4hOuD5U4z9wBI0_GBiy7wYK1v4i0-0xxRg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 429K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 08:42:55</div>
<hr>

<div class="tg-post" id="msg-19960">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بصره عراق مورد حمله نظامی از سوی عربستان سعودی قرار گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/19960" target="_blank">📅 03:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19959">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">انفجار انبار مهمات در مقر فرماندهی عملیات حشد شعبی، بصره
@WarRoom</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/19959" target="_blank">📅 02:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19958">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ایرنا:
سنتکام دروغگوعه، تمام موشک‌های ما اصابت داشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/19958" target="_blank">📅 02:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19957">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">صدای جنگنده از کیش به سمت جنوب ایران
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/19957" target="_blank">📅 02:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19956">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">رسانه های داخلی : به اربیل عراق حمله پهپادی شده و جنگنده‌های آمریکایی بلند شدن.
@WarRoom</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/withyashar/19956" target="_blank">📅 02:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19955">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اخبار حاکی از فعال‌سازی سیستم دفاعی "پتریوت" در آسمان جمهوری آذربایجان، کشور همسایه ایران، است.(تایید نشده هست)
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/19955" target="_blank">📅 02:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19954">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yk7QdXrjclYjuIiFCD9RhBZ-Njx35yLsfostBSCFp_K95FLagHq0YBzC65vkqt2O1-XyAKEtUToMDt6UF1Nxt5dgiSWCvaeImT-6adQE93_2lwFh2zPNZu7Iv-vMqA2BPKaFcE3yxCTT9UEFAIauLbyruqgJ3C9g3z99qozCEDFfPVIw3aDbK6ItmXH0EBg3VqRuXe_In8SxH9cTGUVMVHb3Pb1xTgiTHgLXaHEFAnyMM0j-Tu7KEmVKg3_khan28FX9px5MBEa8G_0b2FpLdxksJjbukXL9wO8zxEifGzS5X4Q1f3UKt6cFXpW5VzCCDFgj1XtqjMKflfqoPNVvUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگاهی به برد موشک های سپاه به اکراین
@WarRoom</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/withyashar/19954" target="_blank">📅 02:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19953">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سپاه به اربیل عراق حملات سنگین موشکی/پهپادی کرد و چندین انفجار تو اربیل شنیده شده
@WarRoom</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/19953" target="_blank">📅 02:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19952">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اتاق جنگ با یاشار : دربون جهنم سابقه نداشت خبر از حمله سپاه بزنه! بدجور برد کوپر بد خواب شده ، مادر بگرید
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/19952" target="_blank">📅 02:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19951">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اتاق جنگ با یاشار : فرمانده سنتکام بردلی کوپر رو از خواب بیدار کردند
👺</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/19951" target="_blank">📅 01:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19950">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">منبع آمریکایی به شبکه i24NEWS گفت که جمهوری اسلامی حداقل 4 موشک بالستیک به سمت یک پایگاه آمریکایی در اردن شلیک کرده است و این اقدام را یک "حمله بزرگ" توصیف کرد
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/19950" target="_blank">📅 01:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19949">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">چنل و اینستاگرام رو فردا پرایویت میکنم یه مدت ، اگه فالو ندارید فالو کنید نمونین پشت در پیش عرزشی ها
t.me/WarRoom
instagram.com/yashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/19949" target="_blank">📅 01:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19948">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">من نمیدونم رسانه ها برای اینکه جو بدن چرا اطلاعات غلط میدن مردم اصلا آتش بسی نبود که بخواد نقض بشه. یه حمله شد، یه جوابی داده نشد. یه طرف کوتاه اومد، ادامه نداد! الان جواب اومده جواب داده
😁
چون نفت داشت میومد پایین فشاری شدن
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/19948" target="_blank">📅 01:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19947">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مقام ارشد آمریکایی: ایران موشک‌هایی را به سمت پایگاه آمریکایی در اردن شلیک کرد
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/19947" target="_blank">📅 01:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19946">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اتاق جنگ با یاشار : فرمانده سنتکام بردلی کوپر رو از خواب بیدار کردند
👺</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/19946" target="_blank">📅 01:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19945">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پرتاب موشک جدید از غرب ایران
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/19945" target="_blank">📅 01:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19944">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گزارش‌های تایید نشده از اصابت یک موشک به مرز اردن و اسرائیل و پایگاه آمریکا
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/19944" target="_blank">📅 01:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19943">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87354e52d8.mp4?token=HZo_adqH3slYdcrmkpJZAfY18mrkjuaIxyBWGfUWWnFwAJhXBbLMXXwpLaoDbpVacjjnBHOeAU5wdEra2kdMQDeidFyGHDqx808eQ8zBoje9ZvucGHQO1K-UPrWl6nHgUuRiW45ppFuLfoAjZaMliDQWkZO666-lk5FPgX9-uBdxzjZHdZ8dRb2bV-UGcZ0E1kpJW5UHtk9_wIpV0uj5LpbrmhosAVjRnMS5U6JYqXcoHJo_LkzPZMedz0IvDGR0Z7gCO6Y6L4DconvAczdLDhvAqZpOjxCCRRmZNC54ldeX5Vw2qZvQt-r6IX95PuEhad9jzaDOCpI-fNBVtX26Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87354e52d8.mp4?token=HZo_adqH3slYdcrmkpJZAfY18mrkjuaIxyBWGfUWWnFwAJhXBbLMXXwpLaoDbpVacjjnBHOeAU5wdEra2kdMQDeidFyGHDqx808eQ8zBoje9ZvucGHQO1K-UPrWl6nHgUuRiW45ppFuLfoAjZaMliDQWkZO666-lk5FPgX9-uBdxzjZHdZ8dRb2bV-UGcZ0E1kpJW5UHtk9_wIpV0uj5LpbrmhosAVjRnMS5U6JYqXcoHJo_LkzPZMedz0IvDGR0Z7gCO6Y6L4DconvAczdLDhvAqZpOjxCCRRmZNC54ldeX5Vw2qZvQt-r6IX95PuEhad9jzaDOCpI-fNBVtX26Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آسمان اردن ، پدافند درگیر شده
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/19943" target="_blank">📅 01:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19942">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snTvqnvU7zEaP8Dye5jD5ROHL44ziJ_oOYF1q_ol9fYo3M3bDV3fsopUaZh3_yUFGEGn9keGOLF3B55GJirPb6xYMCZ7CazXB945TXcQFBGoS-oOAB1WX3WBor2yZ1wYCz4410dbr1yi_RBtAb8Xt6TJnLfcqbekxXNil04dFTokI8seu07I6lHFIa5R8G3jDlf2xfZCEqbpTx9H2wmFDF1mbh93clmue5DjLKVaKyAhLHTaykin9zm_5jYYZPKo79DQ_y52CDD1q7KxIzvcgTj9yuStRdnCXbyCY5hurcir4nRZN4T2VU_LDs4y83cepAOPAlTZOU1Vz-mENFEXiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیر موشک ها
@WarRoom</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/19942" target="_blank">📅 01:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19941">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">فک کنم نتانیاهو با گوشی ترامپ به مم باقر فحش ناموسی داد</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/19941" target="_blank">📅 01:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19940">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z53v6QWpVluAAgdrplmH1eZ8cKZNzhCBcBegz0t5I9YQam1axeZHAksACbmC8opcyb7kV-MvVNJFO_i9ai7z4pknhMI6X6ghrgQgTYR0xCZxtXqLjoetmFyUiDw7iUHy7OzOq9BPaOlHYdIRjsjKW8_wV4GEVz0GPGsuQtXF79Jw1VJ0VeOdFniwMX1vRRKDua69WRn_X5do7Utf_MJnmwK62ph_y0UQxk6OygXARoxrKiQGiPE3af_c8MZhlqgnvgi4Ab1RiSuLnrJZR4OyKicuG2u68GzhbpoGK97ghgnLemh5Y0js8iy6iQWKWH3Sny29eHG-fxyf6VGkF2aQ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موشک ها در آسمان خرم آباد
@WarRoom</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/19940" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19939">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">آلارم اردن فعال شد
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/withyashar/19939" target="_blank">📅 01:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19937">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o4jJQ5O4jRZBHDaBSo7GzpkcGY9D-Q2duV4tmSPqst1LRPpzfbln9kEMEB6z_-LL7A7wuuCyWSnxQMLhhGVD2hxb7J9cAwksUNbCtbPHf2lF1GKIObRVO77ZciFlP3q1KO56y9Qa3ZSl5lORP-z_yxv1O2fcWgLrmrljlOA3yeRqvVkXQX7gGgP-84h9Al4UpsHf7xhO17f52af7QgOyUvSTeAiQ3ODMN8S4KIxM-b_huxoUFj0DoXbw3MCqe03LMNBij_qWxcyXN-DE9245tquAoVSQihOnodAjSXHzSW1vJyRD2MLT6PsCudrDwmc9VBVTo7zE-fzVO1kbd6N7KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M-IkhPqbHqwCtQjEl22bS1c8zEtiBhUv-UNRAL8_OpKOHGnxpfQhlHrKr_AAJqukRbocYnibuKZB1TAOdEg8uU4C86xkIXOuCrNwdrquoZj_W5AkiZ7726PUXuG0HDa2isalEmqKA-pBjgmxgvYkV8yvZzI64dh-ju3ikJXVJISBz5LxIiX1Nf_rfSQxLy8vltkLeOiBEPTHYXB6y8b_zWXP6YAyOvJSbv6ysQH0tAJQ_Ddcf_Fc6owinEvYoc6duRfPex5CsYrPzdfZgGxCDmY7RoiX7MWHi5mcITa9ixHHm75UzvqypDw1TlNtwBifHk_-G4ATh5eWXFWLqXiyAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شلیک ۳ موشک از خمین به اردن
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/19937" target="_blank">📅 01:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19936">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">کانال i24 عبری : تنها چیزی که ترامپ را به سمت امضای توافق با ایران سوق داد، قیمت نفت بود.
@WarRoom</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/19936" target="_blank">📅 01:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19935">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49ddcbdc52.mp4?token=JJ-XkEQciUHsXk9qEN-ArIeXDKAFHDD_9jqX32CznBvpRQjpbSOxyEr6dP3uD-xdoxPIL6SqbZqtR3S9_u6QmTBfs-mpSLRyQq_Ue51bpMq6pLK2g7mwmnPgzhO1Ffv9BdjB38v4aoJM8QGU2MjOKZEsKKRuPyM2DgBMcQ7ZFr0LxYJ4Nsb7IIq8OCmJg72kyN_ylH7XKCrn8G8NK-w49A92EnKA9S_9HOaFemdEYUgqbuFVn8-m4RwPY2iHq2oAOtE8iR36bZKCa_SH35rWIS3WXh0XcztLCCdRcttZJ6TvsyCzjZUXfgocvUvZH-KuhFfxCKARO5pgWLEDoc5ixllRJo9BlxiLzRrUTzWGzSBTnoWtp2HSjNl_YtMoB2NaSHWeOGKjHAXbriHWQhXT9PwTbbnBQkdau4FS-krfIgCNkFI0epuum4AmTuHgstRgua-kkADR_y97FQAfBa--lFGiuShqwsdXZKiVHSrXUppwtl1MT_PsQRZlMMUsD503MR3hdmhXaa4tO9w8PhgYQYAEmmAn3uSI2alTdbpNrj298KliaLeuvh40jIunvEYSiI6cwX1P9mBT-yXpzHbALqhAAwBOaJgTv2EpJRtfZmLycnvgQWWcrxdTDBoCZE4o_HxMbNf7EYk89PO0fW_qvKkPs_GIlkeqY8ifXAaeQGc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49ddcbdc52.mp4?token=JJ-XkEQciUHsXk9qEN-ArIeXDKAFHDD_9jqX32CznBvpRQjpbSOxyEr6dP3uD-xdoxPIL6SqbZqtR3S9_u6QmTBfs-mpSLRyQq_Ue51bpMq6pLK2g7mwmnPgzhO1Ffv9BdjB38v4aoJM8QGU2MjOKZEsKKRuPyM2DgBMcQ7ZFr0LxYJ4Nsb7IIq8OCmJg72kyN_ylH7XKCrn8G8NK-w49A92EnKA9S_9HOaFemdEYUgqbuFVn8-m4RwPY2iHq2oAOtE8iR36bZKCa_SH35rWIS3WXh0XcztLCCdRcttZJ6TvsyCzjZUXfgocvUvZH-KuhFfxCKARO5pgWLEDoc5ixllRJo9BlxiLzRrUTzWGzSBTnoWtp2HSjNl_YtMoB2NaSHWeOGKjHAXbriHWQhXT9PwTbbnBQkdau4FS-krfIgCNkFI0epuum4AmTuHgstRgua-kkADR_y97FQAfBa--lFGiuShqwsdXZKiVHSrXUppwtl1MT_PsQRZlMMUsD503MR3hdmhXaa4tO9w8PhgYQYAEmmAn3uSI2alTdbpNrj298KliaLeuvh40jIunvEYSiI6cwX1P9mBT-yXpzHbALqhAAwBOaJgTv2EpJRtfZmLycnvgQWWcrxdTDBoCZE4o_HxMbNf7EYk89PO0fW_qvKkPs_GIlkeqY8ifXAaeQGc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویترز: به نظر شما چه صلاحیت‌هایی برای رهبری یک دولت انتقالی در ایران دارید؟
شاهزاده رضا پهلوی: اگر یک وکیل تصمیم بگیرد پرونده‌ای را به صورت رایگان بپذیرد، آیا این به معنای آن است که او شغلی ندارد؟ من چهار دهه است که این کار را داوطلبانه و رایگان انجام می‌دهم، درست است؟ به عنوان فداکاری من برای کشورم.
من می‌توانستم به راحتی در قاهره، زمانی که پدرم فوت کرد، تصمیم بگیرم: "می‌دانی چیست؟ به جهنم." من می‌توانم مانند بسیاری دیگر، زندگی، تجارت یا چیزهای دیگر را دنبال کنم... اما تصمیم گرفتم به خاطر کشورم در آن بمانم.
این یک فداکاری شخصی برای یک عمر بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/19935" target="_blank">📅 00:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19934">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba487c3af7.mp4?token=GyLd7TDlanP4VGtBKlZT38WRPEa9xnaJKbvkw1YzqI_H8DkfqEGQzJpwVvFmkXGGbKQq3ADyqxTLoKwdAzYp7KI2h1mvZo_SDKjAQFulPxALt4ja2B7-92XZtaV-IE7v-vMGJ_rUGoIYijZlgKAAeYjNXrmgi9yAEYcC3N-MkITmYXAxXFadQaju0cpJiYMgx0lpz075C_fFtg0FRp85AImQak8H2WFkAVv_w4OwVaJpvTyoRh3O3QplzeyxjNNBcq4zbfoRYPvvI5eMOKD-JRP6aFRVa9VlnCeNGuIMXCP57bWdAgcQzANMbkVOG3XD1bBuiUipYaRXyER0uQhu8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba487c3af7.mp4?token=GyLd7TDlanP4VGtBKlZT38WRPEa9xnaJKbvkw1YzqI_H8DkfqEGQzJpwVvFmkXGGbKQq3ADyqxTLoKwdAzYp7KI2h1mvZo_SDKjAQFulPxALt4ja2B7-92XZtaV-IE7v-vMGJ_rUGoIYijZlgKAAeYjNXrmgi9yAEYcC3N-MkITmYXAxXFadQaju0cpJiYMgx0lpz075C_fFtg0FRp85AImQak8H2WFkAVv_w4OwVaJpvTyoRh3O3QplzeyxjNNBcq4zbfoRYPvvI5eMOKD-JRP6aFRVa9VlnCeNGuIMXCP57bWdAgcQzANMbkVOG3XD1bBuiUipYaRXyER0uQhu8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویترز: گزارش‌هایی، تقریباً ناشناس، مبنی بر دریافت بودجه از اسرائیل و عربستان سعودی توسط شما وجود دارد. آیا این درست است؟
شاهزاده رضا پهلوی: کاملاً نادرست. من هیچ بودجه دولتی یا عمومی از خارج دریافت نکرده‌ام.
هر ریالی که به کمپین من می‌رسد از کمک‌های خصوصی حامیان است. امیدوارم خیرین بیشتری داشته باشیم که چک‌های بزرگتری به ما بدهند.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/19934" target="_blank">📅 00:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19932">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">رویترز به نقل از یک مسئول آمریکایی: توافقی که در حال بررسی است و مربوط به تنگه هرمز، مربوط به هماهنگی است و شامل هیچ‌گونه عوارض عبوری یا هزینه‌های دیگری نمی‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/19932" target="_blank">📅 00:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19931">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4dee73717.mp4?token=bAAQ182cmEfx_YJ3yAimYpzIK7gBnAEJvKD5IiatFZoQccfvhEGsRsBAeL85LKQioGfNzW9upzB1DLp6gGj3PnrdVuXxbtfzgMmg9i6WRM4p8y_c7RyM8ikWwiHYv3gG_AgKBOl0jdpBJHSVnHg7RGLwOQVGJT4Bddv8E-b_H4an62R0IqeK_S0ViC5vm0tXbXusA11Wcw12pL4EeQp8n_Z6QRpa9WvJHT0CEqJS_ZCWnaA5uodT8Y4CFX_xbUXHUoNurM-La7dqYHpH4VLZ_CvELuRvDsEG6-CxkycyN1EeZwtfgy8A1He63EvZxMCKXMrWK8FH1aZqz9X6v9cZU4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4dee73717.mp4?token=bAAQ182cmEfx_YJ3yAimYpzIK7gBnAEJvKD5IiatFZoQccfvhEGsRsBAeL85LKQioGfNzW9upzB1DLp6gGj3PnrdVuXxbtfzgMmg9i6WRM4p8y_c7RyM8ikWwiHYv3gG_AgKBOl0jdpBJHSVnHg7RGLwOQVGJT4Bddv8E-b_H4an62R0IqeK_S0ViC5vm0tXbXusA11Wcw12pL4EeQp8n_Z6QRpa9WvJHT0CEqJS_ZCWnaA5uodT8Y4CFX_xbUXHUoNurM-La7dqYHpH4VLZ_CvELuRvDsEG6-CxkycyN1EeZwtfgy8A1He63EvZxMCKXMrWK8FH1aZqz9X6v9cZU4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی درباره ایران:
فکر می‌کنم ما به تغییر رژیم بسیار نزدیک هستیم.
رژیم در ضعیف‌ترین وضعیت خود در ۴۷ سال گذشته قرار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/19931" target="_blank">📅 00:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19930">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2dacc78c5.mp4?token=SXdE6KeIG4-7sBjVioHgRmbW2zR2rDaqqrYjSttznVDrXYoipIYn7T4LNRR9uGD1n07mDctY2971XYQZXtz_rsWybkuvQqjo7asQi8eKQ2dL_YrdeMRkI2xTbIWhutKLFzvlpAzo0rsR-utkzVFy9dhpMHo0fog72fIvclSA3khXJZ8cA-Sa6eztqAcLX3wn0Jd9Hcf0YFjpdo_9cAgglCV5O9rZVBNxUVORz335cRaQI3yqDosUeDI4Tbq8pP_5vaAaGHfGHgPg2QHkAayXmasyO_wSkH9EBkUtf-E21niE6GKXqJLYNMNcY_bQpr7qAHUktV4m2YWY9nMP3ApQaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2dacc78c5.mp4?token=SXdE6KeIG4-7sBjVioHgRmbW2zR2rDaqqrYjSttznVDrXYoipIYn7T4LNRR9uGD1n07mDctY2971XYQZXtz_rsWybkuvQqjo7asQi8eKQ2dL_YrdeMRkI2xTbIWhutKLFzvlpAzo0rsR-utkzVFy9dhpMHo0fog72fIvclSA3khXJZ8cA-Sa6eztqAcLX3wn0Jd9Hcf0YFjpdo_9cAgglCV5O9rZVBNxUVORz335cRaQI3yqDosUeDI4Tbq8pP_5vaAaGHfGHgPg2QHkAayXmasyO_wSkH9EBkUtf-E21niE6GKXqJLYNMNcY_bQpr7qAHUktV4m2YWY9nMP3ApQaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصویر واضح از حظور شاهزاده رضا پهلوی در مراسم
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/19930" target="_blank">📅 00:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19929">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQ1xn42F2QifleqWsIRI-e-_qzi87WxdXH_tQIag9yT4EX7Sj4FmT26On_i5gYhu7UXZeMliqkEJVx8l0_RAXZERXujfJYBkkKFPbn0b9LSelrrQaHLT_jGX9MziE-5c3IDj42M3PMUAt3z78vSBMlCWbrjC5kfjmdLw3SPmAQ1JGpkJjk1xWbYlKPCGafzuomVWj3v3TdiltWQT6lR-bKYfUnvsjOslJtlK4DxmxZy8eEeTe8PXZoFr79Tlnlw7rKG_jlSpVdnrgzvWr8bFGibjOETzhytaJUivo1XEFMLGn-udvlI38dUlveMf0B4FhX5c9Bv0peKXVxcQ46ySdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز: در حالی که ترامپ مدام از مذاکره با ایران حرف میزنه، طی چند روز اخیر گسترده‌ترین تحرکات نظامی و لجستیکی آمریکا تو منطقه گزارش شده.
به گفته برخی منابع نظامی، آمریکا در حال آماده‌سازی خودش برای یک جنگ تمام‌عیاره!
@WarRoom
اتاق جنگ با یاشار: هم اکنون، در هنگامی که همه در مراسم سناتور فقید لیندسی گراهام هستند، یکی از سنگین‌ترین ترابری های نظامی آمریکا در منطقه انجام می‌شود.</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/19929" target="_blank">📅 23:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19928">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">تقدیم به نگاه زیباتون ، بشوره ببره
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/19928" target="_blank">📅 23:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19927">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/19927" target="_blank">📅 23:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19926">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/19926" target="_blank">📅 23:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19925">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">فاکس‌نیوز:محور اصلی گفت‌وگوهای آمریکا و اسرائیل، تصمیم‌گیری درباره گام‌های بعدی پس از حملات اخیر به ایران بوده.
همچنین نتانیاهو احتمالا اسناد و اطلاعات تازه‌ای ارائه کرده که نشون میده جمهوری اسلامی با وجود صحبت از دیپلماسی، همچنان برنامه هسته‌ای خودش رو پیش می‌بره.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/19925" target="_blank">📅 23:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19924">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/19924" target="_blank">📅 23:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19921">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ViO1MUlgx9R1wOkVntgpwEKJhx7ruFoiXRU0K6TEXXE6j8kFasey0HkQx8xFMxHCC20Ru51NMFNI8SyvrjTsE4Z3HYKslZkkp8VsPPvdKw1YneMeUqi8uRe6JTCkshWzDJUF35VkBZ1aC90St34tXIIyWAzp9JF9z0nhsXbvx4d1Lyf-HO_cCkl-BDaW0WvOLKjnZMTd7B-vSRjAytYiZuPmgUx2Yj39kfIpUEiRWeYB3xOlp30y9ZVEuAbEdXdRvCM3u02y3CQkr_crMUABlXZ9QfyzDrmTPSZ8cpG-Cnk0BdvLhljf839lXe_Ud5V0eU0wWfB8XvKrDlaaBKCKYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g6fuokvZc8C1ju_CwAjeSJEPer7RavoueVqIQY5-J9M8f5yDtkIL8-dZus3Xf9Uc0_0lsSqQmVk0cqd8-RXFV_E6zLWHjOcsYDmXinoc2Es--MTWKCnqPJ3YeA27xgcmPqwBll1LtVr2tZh1eUnkFdy6Sm41zE6-0VhfJmpfCeteDp8EmGKLnR7XA-kBoGQRAcYA5yTUVSus7K6VyIzB5Tbl-vwP2QcTadWmvIg8glMuUcajuGgbGJ4r3m9sDrDgvTMa0P3KaSJL2pSdBWFBEJG1Du-FARYHj-Fac2td4bPMy1g27Nj0mbrmoGX58D4Uil3KKehD9Y3DQkXijG63kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SV5t0MjFYsaxrxmt0Sen2eQtw-dk4-uLO6KeGNGNo0mn-naRL-DOD0EZUqLarTEUbbp8qyVwk4bKZv3e45oj88CDkU75sxF76c5R5lCfMakARm5JTdDKGQIms16oRx-2cA31PigQYYC2zqeeJXJbzVCYYXcmNvM6hGp0dcsLBSboTrgUxzwT23NLpbGXQSch_acupxUprpcb8Aa-2FdfFuAknEX0y08WW_kfqIGNQWeTf_NO7A0Xow0ixvD8iQg0rgfu0zMEfxx-53Oy_MS9JzgH78qK6HXLzMqEdONURT_Rpw792-ioOAYlw3bSm9WJ82myYC_Wj-xf2t3sn-fDCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اولین تصویر شاهزاده در مراسم درگذشت سناتور فقید لینزی گراهام که با اندکی فاصله سناتور تیم شیهی که صحبتهای جنجالیی درباره ایران در سنا کرده بود و ویدئویش را برای شما گذاشته بودم دیده میشوند.
@WarRoom</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/19921" target="_blank">📅 23:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19919">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jME5n3JGiHtT5-q_QzmegB0oq5dCO-ISCtQRWiRBnCwmuk54KZPQyYV4vq1iiGB6SdFdROjNIeoWzoxAi8omsy7Y54DDEQkUUIsEofsT5f6zBeHQbAwDN-xVzf2rGIQ3XiThz9CtPvzxTTrlzBe4SQb_ViDTV2bZCGNH1l4hV0WC7SR85OTF-Famv8PveC0haLQNrJh7T-l331_1RDXfFfTFY_CYU4pDuWz1FamoLhz2gpI-j9T-GqbGP9pCTKSKr-IuOe3NtV9jwGck0e3kXvR4-VgM6UZbD6MfYx3y0sUy96gITJZd9PCfd3De4Fy_0_JRSTBoDbLQQQfVeXXe0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ff6vf20tfrL_Fl7kgY9wcvKIy97rye9p1f9MWnHvDiH6pYgwo-hoSEa8qjsL0MAXyFqLySQMYMYeoNCadoM1wB_D94HW5gQ7wBNrkbBqyhctwgBKrxcVaDK2ZLr6sDsYCYj4j07fsWSbSLdoJGsmx2sYU9AeSrsCAIEZtIGCCTmAwK7W6NCWkI8oiP-3RaxJybzmJWI12ExwzCzZQBou_rM5rclV-2IVbmFZZr_XEHogByjdZFpL97_ohkLwhhruQDZua6NIZ4grkwIYc5YIty1y7_Z0h5SDnn_aaAax5QFL6Sd3VPI6qZgua8nVZrBLMWERijLjugA59sTZPt6WIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شاهزاده در کنار کامران خوانساری‌نیا در مراسم
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/19919" target="_blank">📅 23:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19918">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer"><a href="https://t.me/withyashar/19918" target="_blank">📅 23:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19911">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اکسیوس:ترامپ و نتانیاهو جلسه‌ای به مدت ۹۰ دقیقه برگزار کردند که به عنوان یک جلسه سازنده توصیف شد و تمرکز آن بر روی ایران بود، بدون اینکه هیچ نشانه‌ای از اختلاف نظر بین آن‌ها دیده شود.
دفتر نتانیاهو تأکید کرد که اسرائیل، واشنگتن را در مورد ایران تحت فشار قرار نمی‌دهد و هر دو طرف در یک هدف مشترک برای جلوگیری از دستیابی تهران به سلاح هسته‌ای، سهیم هستند.
همچنین، دو طرف در مورد امکان عادی‌سازی روابط بین عربستان سعودی و اسرائیل گفتگو کردند. موضوع فروش جنگنده‌های F-35 به ترکیه مطرح نشد و ترامپ از اسرائیل درخواست انصراف از مناطق تحت کنترل خود را نکرد.
@WarRoom</div>
<div class="tg-footer">👁️ 196K · <a href="https://t.me/withyashar/19911" target="_blank">📅 22:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19910">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c9ed022ed.mp4?token=sZ7fRUb2X8srIaW_fJa9uKRrFaDrbdenekT70QH5Arf9BsB7PVCvHGJuUbneMKuwwcMH8n-hvlR9ciIIDF3-85YCfHsk8i3pkJDp77y9GeFWfdmmvb9yLj0yl0zI8XlCrypwJbqnJICpxCZS2EGF5M7zBf0Rbq-2bpAdV9-W51EXxGKuKtLz_iZds34Ad67r8Iy6QBjv6OOPxU9onvLSwkgSM8NbK-kxzkHHnDF1QzVzqRxuz_apPGw4-4p92W2yF4IxGf36yW8MlU1ZwPMGRRvwGk-esa0DrGPT1jJdQOy80YwPYrSndEmMMcsSnTettsSLGBnbGeGRke7O_5XLrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c9ed022ed.mp4?token=sZ7fRUb2X8srIaW_fJa9uKRrFaDrbdenekT70QH5Arf9BsB7PVCvHGJuUbneMKuwwcMH8n-hvlR9ciIIDF3-85YCfHsk8i3pkJDp77y9GeFWfdmmvb9yLj0yl0zI8XlCrypwJbqnJICpxCZS2EGF5M7zBf0Rbq-2bpAdV9-W51EXxGKuKtLz_iZds34Ad67r8Iy6QBjv6OOPxU9onvLSwkgSM8NbK-kxzkHHnDF1QzVzqRxuz_apPGw4-4p92W2yF4IxGf36yW8MlU1ZwPMGRRvwGk-esa0DrGPT1jJdQOy80YwPYrSndEmMMcsSnTettsSLGBnbGeGRke7O_5XLrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره لیندزی گراهام گفت:
او به‌شدت جنگ‌طلب بود.
راستش را بگویم، هیچ جنگی نبود که از آن خوشش نیاید.
فقط دوستان نزدیکش منظورم را می‌فهمند؛
اما او همه این‌ها را برای کشورمان میکرد.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/19910" target="_blank">📅 22:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19909">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">یک منبع آگاه گفت مهنام نواب صفوی، ۲۲ ساله، خواننده رپ فارسی و از بازداشت‌شدگان انقلاب ملی دی‌ماه، از سوی شعبه پنجم دادگاه انقلاب اصفهان به ریاست قاضی همتی‌نژاد به اعدام محکوم شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/19909" target="_blank">📅 22:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19908">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ixptzz8H3bLK1ILyi3eSrMEHqINo42MDZ0_V0OxCyrECbxp9GmG93um7BMzV9lasBkb4wpBi5Hb-SojQfGphlMfRSCI__DvgVIlJz4QAyHJabBkBFqayDMVe2r-4zArYLMVh1p7LkmsjkbH0pDE10dUQmt7h871UGPT0sl-fb6y0fPBOH1Cp_m0EO_WoZlIO0Lh0k82wf5c-g-JtzhtQoY3sP9IYwOGkclZAj6yK_JjAVvy4iZr9HSNGLp6K98YVfsd34mCrFPqX2any1O1LNDZNrTTy4xBjPCKdeH2T0bpOFI2_V1XLzuI5N2sEMN0BCyRN6L0kYo5JFRrKjuoz6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز : علی واعظ، مدیر پروژه ایران در گروه بین‌المللی بحران، یک سازمان پیشگیری از درگیری، گفت که پس از ملاقات با رضا پهلوی در ۱۵ سال پیش، به این نتیجه رسیده است که او اشتیاقی برای کشمکش‌های سیاسی لازم برای رهبری تغییر در ایران ندارد و از آن زمان تاکنون هیچ چیز دیدگاه او را تغییر نداده است. اما پهلوی به رویترز گفت: «من از حمایت زیادی در سراسر کشور، در داخل و خارج از ایران، برخوردار هستم.»
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/19908" target="_blank">📅 22:18 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19907">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">کانال ۱۲ اسرائیل: نتانیاهو به ترامپ تأکید کرده که حملات بیشتر علیه تأسیسات هسته‌ای بازسازی‌شده ایران حتمی است
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/19907" target="_blank">📅 22:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19906">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">نتانیاهو:من همین الان یک جلسه عالی با رئیس‌جمهور ترامپ داشتم. وقتی می‌گویم عالی، این فقط یک تعریف ساده نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/19906" target="_blank">📅 21:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19905">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">instagram.com/yashar
LIVE NOW !</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/19905" target="_blank">📅 21:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19904">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/19904" target="_blank">📅 21:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19903">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/19903" target="_blank">📅 21:18 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19902">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06b2086bda.mp4?token=oa6RCCyglq0Ar0HMU4C-AD7S6v6VWeV7okLsULf_0tTkLkaAG3_zE3t6rmLYxWOeAtXRkUzNK2ol-W7Q0sabWRrSXVqYnXeMn9d0DKTaIUy3FnBd0tLmGeqnRx8y-BON2NWcFaAL1bh-FS6LXvN0yuWWKVYrI77WM2stg6IiIIyfyit9NHicHCpU93rLHpq3nm-orP7qJRHDaQ3xrYjOMHgWO2YpYjT3dRvBhhQDefCj3UnN7D4H_mxn_2CThVdZr3VdVSyOqHAP8-XK-EVWqKUK056ALxMcbPYKiPEEo5K0PElf6tYmfwVNYwXaeNvD24Hd1eUCwe_pvJxvyiJZcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06b2086bda.mp4?token=oa6RCCyglq0Ar0HMU4C-AD7S6v6VWeV7okLsULf_0tTkLkaAG3_zE3t6rmLYxWOeAtXRkUzNK2ol-W7Q0sabWRrSXVqYnXeMn9d0DKTaIUy3FnBd0tLmGeqnRx8y-BON2NWcFaAL1bh-FS6LXvN0yuWWKVYrI77WM2stg6IiIIyfyit9NHicHCpU93rLHpq3nm-orP7qJRHDaQ3xrYjOMHgWO2YpYjT3dRvBhhQDefCj3UnN7D4H_mxn_2CThVdZr3VdVSyOqHAP8-XK-EVWqKUK056ALxMcbPYKiPEEo5K0PElf6tYmfwVNYwXaeNvD24Hd1eUCwe_pvJxvyiJZcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/19902" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19901">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">کاخ سفید : پایگاه مشترک چارلستون در کارولینای جنوبی به افتخار سناتور فقید لیندزی گراهام تغییر نام خواهد یافت.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/19901" target="_blank">📅 21:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19900">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">مقام اسرائیلی نزدیک به نتانیاهو:
ما در یک مقطع حساس هستیم. رئیس جمهور ترامپ به زودی تصمیم میگیره که کدوم سمتی باشه.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19900" target="_blank">📅 20:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19899">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">آندری سیبیها، وزیر امور خارجه اوکراین:
من با عراقچی، وزیر امور خارجه ایران، برای گفتگویی صریح تماس گرفتم.
من تأکید کردم که هدف ما جلوگیری از تشدید غیرضروری تنش است.
من مجدداً تأکید کردم که تمام اقدامات اوکراین صرفاً با هدف دفاع از کشورمان در برابر تجاوز روسیه انجام می‌شود و هرگز قصد هدف قرار دادن کشتی‌های غیرنظامی یا مردم را نداشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19899" target="_blank">📅 20:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19898">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">کانال 14 اسرائیل به نقل یک مقام بلند پایه : ترامپ و نتانیاهو بر این موضوع تاکید کردند که هدف مشترک آنها، جلوگیری از دستیابی ایران به سلاح هسته‌ای است
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/19898" target="_blank">📅 20:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19897">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-footer"><a href="https://t.me/withyashar/19897" target="_blank">📅 20:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19896">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">کاخ سفید:
جلسات ترامپ با زلنسکی و نتانیاهو، سازنده و مثبت بودند
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19896" target="_blank">📅 19:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19895">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پایان جلسه دیدار بین نتانیاهو و ترامپ.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19895" target="_blank">📅 19:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19894">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OO2Q7wABTfDdz97YouELqbM-lQVIGtwXmfTlguxhZm11-kBZZAzINk6KefzTSNy3eWq8wYZAC8YlcGUZ2oJMPc2XmPQcdP0rp0fgqxDlRAP15CfWBijUGINXSg7f-KRnlZh4X0Less7N2lM1DgoEbz0xrIWh4WyYaKg2k__zAKmCnSQKQAzgBv-QwRMNod4_5sMB-tIgcqHL9B6uWyeoBGFBS6YYxg-ROfn9Pmew4WWzONLfsFAjGjZ4bNb6_xm4jwPjIIMqS82B10tnsbHd3-QK_nGjIJcb9JkSZbmMiFJEPNWW95gLauvT4GxsBJVeuncd9oKIdTCOkvhlAo5hSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون نتانیاهو و ترامپ
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19894" target="_blank">📅 19:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19893">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">شاهزاده رضا پهلوی نیز ساعتی دیگر در مراسم سناتور فقید لیندسی گراهم در کلیسای واشنگتن شرکت خواهد کرد.
@WarRoom
🇮🇷</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/19893" target="_blank">📅 19:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19892">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">در دیدار نتانیاهو و ترامپ، یک تیم گسترده از مقامات ریاست جمهوری حضور دارند: معاون رئیس جمهور ونس، وزیر امور خارجه روبیو، وزیر جنگ گست، رئیس سازمان سیا راتکلیف و نماینده ویژه رئیس جمهور، ویتکوف.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/19892" target="_blank">📅 19:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19891">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3UImib_GdOTAWLT49htQVHSuZB4jnUfYR-KxN2-80ENoqRuHgnuHUaqG-VYkJtwGOfVYieFiKDKdJsOfO2mpjFyGeKSqALF5TVTxIU458GXGkFicTjN8so3N-RQFBb6tGnyEcwbCcNkDkKde5tiR-i5B_XGG79UNdrscBX-zDSPNswipUazUzbBR5637SQEHd-G6yKykMV5GwvxqvHtJzoVHikJ-I4v5jeQSBuK75fChPnLOAfQ9Z93BCbCPL5SfjbtYG2EyATw1Edobv2ZrMBzo9dUxyEe0-yscZNJcL07dpHjkqQXBBYxEc9BDz7tmIbKBAoKEVbTpicdotKOqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ملاقات ترامپ و زلنسکی در کاخ سفید: رئیس‌جمهور اوکراین گفت که آن‌ها در مورد مجوزهای تولید موشک‌های پدافندی پاتریوت در خاک اوکراین گفتگو کردند.
@WarRoom
پیشتر رسانه های فیک نیوز گفته بودند زلنسکی بدون ملاقات کاخ سفید را ترک کرده.</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/19891" target="_blank">📅 19:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19890">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OM07vdFrX25Hwm6uagP_gh9-LDYOXdf7Mi6OaH8i6RHsMHp4tiYVj3no-nezuQgfOIlgHxxQiNteITt5GiuJnayZSjsQ1Uo7KefySY4xlDek9ILueTpl3FQAF7gwsVqklQyh-axS2CBEZ4O_hRYsJh4_uOIGET7nK4WFBeZBJCjpu2IRZ0Ds3LAUdf8X1ouxDnzDqyz7eJYMyctRGvc3ttVG2fxZBeeyTejfdMxnuu-fY3n_6gyd6Q0Bt9s_l3Oh9P_Zh-n7slJ0GLzOaFYuWNt9pN58srCigc4veYE9kMdaILmIV_tvyPzgJYFoYRkycAalPHChyLMd3LaA2b1G4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست وزیر اسرائیل، پیش از دیدار با رئیس جمهور ترامپ در کاخ سفید، با مشاوران خود گفتگو کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/19890" target="_blank">📅 19:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19889">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">خبرنگار اکسیوس: یک مقام ارشد کاخ سفید گفت «ترامپ در مصاحبه با شبکه فاکس‌نیوز قصد داشت پیش از دیدار با بنیامین نتانیاهو، پیامی قاطع و سخت‌گیرانه به او منتقل کند.»
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/19889" target="_blank">📅 19:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19888">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سلاح دیوانه وار «میله های خدایان» گزینه دیگر غیر اتمی برای «کوه کلنگ گزلا» در ایران !
این ایده نخستین بار در دهه ۱۹۵۰ و سپس در دهه ۱۹۹۰ در مطالعات نظامی آمریکا مطرح شد و بعدها به دلیل جذابیتش در رسانه‌ها، مستندها و بازی‌های ویدئویی بسیار مشهور شد، عملیاتی بودن این سلاح مشخص نیست
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/19888" target="_blank">📅 18:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19887">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6b359db05.mp4?token=ca2KUv9ZFbuPRbzJn6LfBGApgjPJeuxJnU82okDHTGtfkNZFp8z-_lMjh0phrzha9NOdqXEvkBZBVVDSrDlnr3nARAqEWLGBiQFa7CAO6NQ3PuzZ5UTsnP-Y6ULFks7XoDL87Oq1v_6en8Vtmkd_PS37H4T0FasRb2597aDU3iq0RIlRtF3yAaciyBkFA3xzIwlcr4ojoO4aoXDjNjW9oxQSiKTUQMvQN5st34qQJW1RkrafrPtaA76gE36NZLwcm67URrvKlRJi07VJzdxl1cfMGaOxFIjiW-mmKHC1SsmQYOGdvclBd76Ei5nCY3D02jP16ae3KsLJUUnWEKHL1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6b359db05.mp4?token=ca2KUv9ZFbuPRbzJn6LfBGApgjPJeuxJnU82okDHTGtfkNZFp8z-_lMjh0phrzha9NOdqXEvkBZBVVDSrDlnr3nARAqEWLGBiQFa7CAO6NQ3PuzZ5UTsnP-Y6ULFks7XoDL87Oq1v_6en8Vtmkd_PS37H4T0FasRb2597aDU3iq0RIlRtF3yAaciyBkFA3xzIwlcr4ojoO4aoXDjNjW9oxQSiKTUQMvQN5st34qQJW1RkrafrPtaA76gE36NZLwcm67URrvKlRJi07VJzdxl1cfMGaOxFIjiW-mmKHC1SsmQYOGdvclBd76Ei5nCY3D02jP16ae3KsLJUUnWEKHL1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو برای دیدار با ترامپ وارد کاخ سفید شد
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/19887" target="_blank">📅 18:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19886">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اتاق جنگ با یاشار : طبق تجربه و تحلیل من این شرایط دوهفته دیگه پر پرش دوام بیاره و باز دعوا شروع میشه
😁
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/19886" target="_blank">📅 18:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19885">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFD9xstsbm4yWK3R1jSgcVU1uAv9fafyzdVW4uKOsQMkvq5ZRpXkQDUJg8xkU4Ba907xMcc5a3U2QSb9TZynXsMzfStGAWgn-YVdnHPrP68BiBSyakVnepfM8ym4lJT4ewd5E97IspQycmcJMvP_e29SqCC2q2_JFmDqUkFUhsHo3eIczO6i-FxMY9X-GsXdKTqeqYjqhA1B53rsVWBoZhJUUP5jkhgLX9MO8JhJB0xNJdbc06qRS6-JwyC7GGgwXn0Rz6d-jPaoeUjT_sCDku9OLXUb4fVsxMS16fHA4-gwFM9UFjuPx0B5IqUzb1dylePV6TuoBBLr1DWHRxFZfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تابوت لیندسی گراهام با استقبال خواهرش و اعضای کنگره ایالات متحده وارد ساختمان کنگره شد  جی‌دی ونس، معاون ترامپ پیش از مراسم تشییع جنازه امروز، برای ادای احترام به لیندسی گراهام وارد ساختمان کنگره شد طبق گزارش CBS News، مراسم امروز با آیین ورود به ساختمان کنگره…</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/19885" target="_blank">📅 18:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19884">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c954e618d1.mp4?token=BOua-pT-DSGN5IVUSyxWHtGuKO-8OF0aVcCzJCe-OhrLMZV7huxEKjxWj9jmwsbZQgAqfRt2UYtAqzXS8QN1ttDW8fU6vuxdv1iU4d-72c2hJit3Oi7dwJlketPmsKdfQW_2BEFm45yxso_ZFpVuSQOPsVnm-BHexAVBCzCXxziJ_yi5A_0v1o_DTxuZbAYoKSw2O_xYH9uZuDzyPvSUj6xA5uRMH03PXUGjtVl-ceyeWmwisj4pGaQyoZSj65XM-Ymo247xe0USM7t1COJtQb8Tnu1pBFNjTqjmjzBxqLN9UcO7M429-CoV-_ee7AK4_exYsoNdYq0J2EOWY2kmkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c954e618d1.mp4?token=BOua-pT-DSGN5IVUSyxWHtGuKO-8OF0aVcCzJCe-OhrLMZV7huxEKjxWj9jmwsbZQgAqfRt2UYtAqzXS8QN1ttDW8fU6vuxdv1iU4d-72c2hJit3Oi7dwJlketPmsKdfQW_2BEFm45yxso_ZFpVuSQOPsVnm-BHexAVBCzCXxziJ_yi5A_0v1o_DTxuZbAYoKSw2O_xYH9uZuDzyPvSUj6xA5uRMH03PXUGjtVl-ceyeWmwisj4pGaQyoZSj65XM-Ymo247xe0USM7t1COJtQb8Tnu1pBFNjTqjmjzBxqLN9UcO7M429-CoV-_ee7AK4_exYsoNdYq0J2EOWY2kmkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعتی پیش
لحظه ورود زلنسکی به کاخ سفید
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/19884" target="_blank">📅 18:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19883">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c7fe4f226.mp4?token=BmUtQN3u89UFJv6tCM1ylyEeJQPGXdLx8gLq2J4ENIegqBX2zGQvCJrD2I9EThjjvPk-x6f03Dv1g30Tn_k0kdlQBmtfr_qQh75bN5CEllHL1M7LDGi8xFxpfs9rWRAd17z7nlITviv9oYCP-denpbg6EJzt7kJFP4yrQs7ba7_RcJODkWlFZjSmrqkMzchvkT8Lelp7ezvuNMfH1mrjGCQD7PjwyMM6uYMY4lSyuI1y04vOq3MrGLZ41grr0-6L-Of_kuUjUqySH91uTUwHMVXFwNNHvWBem1Y5CJNoS9JW59lvNdJ4ouvccl7jJHjBVluWaX7tNGdKsm1FrK9EKSiaIXE09k2yA98Z_i14V_-l7whxFgIVz2GmrLPHoWzG8g5bcxCYhs6WTm67gg4OMF1RG10GOjwSHFGLucZpdFDLS6JJZgkgLXqm1q4nbLRyU415EcYlhk-K1iN_oPhSfEvy7_96B8-GKlYoSXS5ivMqIi88n4G3HLU-JCgZFTjFyCCx8jh62kLOpkxsOQSx55-bZv0OzxqhbxGKECzhcTyDFvwF2CmFSBoZUZgvT5tXQP7jB7guQ9sRF8D9cwTZjFM4onqLSLth1cld-FfaKqo1Jh2pgUKTruxb6oW3LoYRbMkcsCoAc2ZhTXQop_nGcTPTvEHRLzrbi3iAcEEy2WE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c7fe4f226.mp4?token=BmUtQN3u89UFJv6tCM1ylyEeJQPGXdLx8gLq2J4ENIegqBX2zGQvCJrD2I9EThjjvPk-x6f03Dv1g30Tn_k0kdlQBmtfr_qQh75bN5CEllHL1M7LDGi8xFxpfs9rWRAd17z7nlITviv9oYCP-denpbg6EJzt7kJFP4yrQs7ba7_RcJODkWlFZjSmrqkMzchvkT8Lelp7ezvuNMfH1mrjGCQD7PjwyMM6uYMY4lSyuI1y04vOq3MrGLZ41grr0-6L-Of_kuUjUqySH91uTUwHMVXFwNNHvWBem1Y5CJNoS9JW59lvNdJ4ouvccl7jJHjBVluWaX7tNGdKsm1FrK9EKSiaIXE09k2yA98Z_i14V_-l7whxFgIVz2GmrLPHoWzG8g5bcxCYhs6WTm67gg4OMF1RG10GOjwSHFGLucZpdFDLS6JJZgkgLXqm1q4nbLRyU415EcYlhk-K1iN_oPhSfEvy7_96B8-GKlYoSXS5ivMqIi88n4G3HLU-JCgZFTjFyCCx8jh62kLOpkxsOQSx55-bZv0OzxqhbxGKECzhcTyDFvwF2CmFSBoZUZgvT5tXQP7jB7guQ9sRF8D9cwTZjFM4onqLSLth1cld-FfaKqo1Jh2pgUKTruxb6oW3LoYRbMkcsCoAc2ZhTXQop_nGcTPTvEHRLzrbi3iAcEEy2WE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت لیندسی گراهام با استقبال خواهرش و اعضای کنگره ایالات متحده وارد ساختمان کنگره شد
جی‌دی ونس، معاون ترامپ پیش از مراسم تشییع جنازه امروز، برای ادای احترام به لیندسی گراهام وارد ساختمان کنگره شد
طبق گزارش CBS News، مراسم امروز با آیین ورود به ساختمان کنگره آغاز می‌شود. تابوت سناتور گراهام توسط تیم حمل‌کنندگان نیروهای مسلح حمل خواهد شد تا خدمات او در نیروی هوایی ارتش آمریکا گرامی داشته شود و سپس تحت نگهبانی پلیس کنگره قرار می‌گیرد. این مراسم در کنگره برگزار می‌شود و حضور برای عموم آزاد نیست.
مراسم اصلی تشییع جنازه ساعت ۲ بعدازظهر به وقت محلی در کلیسای جامع ملی واشنگتن (Washington National Cathedral) برگزار خواهد شد.
دونالد ترامپ سخنرانی خواهد کرد و نخست‌وزیر اسرائیل بنیامین نتانیاهو و رئیس‌جمهور اوکراین ولودیمیر زلنسکی نیز در آن حضور خواهند داشت.
@WarRoom
*ویدیو رو خودم از لایو مراسم رکورد و خلاصه کردم</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/19883" target="_blank">📅 17:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19881">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D6rrXrIUY800FVEVxqAQ7J6GiLlN8HPl-8C08yG-aj_NSXypjl5aD9TWdkZXd2gX19yPJZ0MJ6GosNkCEXxqbLfkNrUOtZpetwKKMwPUyGVI3dnkVadKeZqB8MAtkOPngCM-nwWdbLvQDzrlvbvSyzwF5zHVo8iIEg8Rv6WryW8ITZ1IFb0CVDwx-IJpuiU2ILeew0r7o7zD7YqAQr6RO0XFQNC51GSoDaRRaSvw1KhCXXrgvSouQfn0FnSpm1r2n4O8ATb_R9-X6GfIz-iiC2fvs-lqBufI0757SKegwpaVOFYtiRcj94TpYLf7L4Qys79D4utV2ou1OEODqyNYvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ltT5tlvdkCmw187WCaA0SY225Mz-tQ9uRycOtPEBHCyuN9PgehJemeWrJ4Fi48Hw7a42f9XqoviibuAssvo5OSsnTO6seR29qY0uyzlIHqX9iWjqt9Zc8gGpNBvXgbLiZZqOK6GHNM2mHpQtdEmLJCZoTHQrMF32Mwn9sMBhoULUaLEr9dGZtbAWYVu2e2uFKUfuYmlf2-sSvAh9b1VUAxYu1gtCTgkcHoovR4MqMCgTaE3Tu9NK2DlWqiErj4rheHwPvMoSkJvUxk3FnrhE1AUIEXMfRAvNYmQW5tdnXG9iPjfuGUH7Mm-vbxbcvDVVNec2E9LXDLkwdsLCzOhdMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">واکنش مارک لوین به اعدام و سرکوب مردم در اصفهان:
با این نازی‌ها مذاکره نکنید.
مردم رو مسلح کنید
@WarRoom
عکس دوم چهره کریه قاضی اصفهان که حکم داد</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/19881" target="_blank">📅 17:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19880">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اگر توافق نکنیم به راحتی کوه کلنگ را از بین می‌بریم ترامپ به فاکس :" من دقیقاً می‌دانم در کوه کلنگ چه می‌گذرد، مشکل بزرگی نیست. ما سایت‌های هسته‌ای آنها را از بین بردیم و اگر توافق نکنیم، باید کلنگ را از بین ببریم. اگر توافق نکنیم، خیلی راحت آن را از بین خواهیم…</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/19880" target="_blank">📅 16:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19879">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/049afcae48.mp4?token=UCuEUmhA4AGeZ95uHrown43mah81UwS1_5NMhRWl-CgWyFTzEpiSYpqc8nk5SSFbPHPI7eD0IGoM2lZtZB5Co3kGk1LTetdNrl897g8B0jd_JeNL67terZ5_F4zXAejH2eYz98TGWaR7yXMfhCzGMN_sa2aKYwWmzinVTUpmXTnf3PEEHzAZV3hzNlMR00Ook9NH3ABTHMjwtKIAZnTXlPEaHfC5V-NL1nMrdQ-K-xUYszDtzJ0ARdsNuWoqlVLxicPn-9OPff3ktIopaZGOYVlSrLzKsqfNVFGIEiDkF6yLjsR7HTDD1k8LtaREV1G06ttSiYK7TGhAVu92tvDFFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/049afcae48.mp4?token=UCuEUmhA4AGeZ95uHrown43mah81UwS1_5NMhRWl-CgWyFTzEpiSYpqc8nk5SSFbPHPI7eD0IGoM2lZtZB5Co3kGk1LTetdNrl897g8B0jd_JeNL67terZ5_F4zXAejH2eYz98TGWaR7yXMfhCzGMN_sa2aKYwWmzinVTUpmXTnf3PEEHzAZV3hzNlMR00Ook9NH3ABTHMjwtKIAZnTXlPEaHfC5V-NL1nMrdQ-K-xUYszDtzJ0ARdsNuWoqlVLxicPn-9OPff3ktIopaZGOYVlSrLzKsqfNVFGIEiDkF6yLjsR7HTDD1k8LtaREV1G06ttSiYK7TGhAVu92tvDFFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران گفت: ما محاصره را برداشتیم، اما بعد آن‌ها توافق را نقض کردند، بنابراین دوباره محاصره را برقرار کردیم.آن‌ها توافق را می‌شکنند.دیگر نمی‌توانیم اجازه دهیم که توافق‌ها را نقض کنند
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/19879" target="_blank">📅 16:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19878">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5f30f4312.mp4?token=QO-lUGO5pLyUKl6ujh50UEgSJrkxrPj-iDnkVVm5oVmiUHyUAql8uHZnfn1s9bKnpa1f4lklK9DsKgqFKBFFokUaFBzigTpFmQdFM2n4ZL8RYqsIzYZuni6yrsMoENVsp2VgaIaM90a-4X7Uw8XxhEFJv-6MYaomW35loTeybboOyM_y540t_OQFtaI2Q35qAIaM5vv6G4xLyRxz9v-cI3pvMzDDIwc6LZpb0c4kri3cnHcnljlZvxQL2PjkAWQ0zic227cEsHE1DTxLfI8_qbkivYEF_yJPuFa3LTgROTedaRQb0ERFeZNDdMMAiFS3uz-a3_ybg0hSTElgsDnuKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5f30f4312.mp4?token=QO-lUGO5pLyUKl6ujh50UEgSJrkxrPj-iDnkVVm5oVmiUHyUAql8uHZnfn1s9bKnpa1f4lklK9DsKgqFKBFFokUaFBzigTpFmQdFM2n4ZL8RYqsIzYZuni6yrsMoENVsp2VgaIaM90a-4X7Uw8XxhEFJv-6MYaomW35loTeybboOyM_y540t_OQFtaI2Q35qAIaM5vv6G4xLyRxz9v-cI3pvMzDDIwc6LZpb0c4kri3cnHcnljlZvxQL2PjkAWQ0zic227cEsHE1DTxLfI8_qbkivYEF_yJPuFa3LTgROTedaRQb0ERFeZNDdMMAiFS3uz-a3_ybg0hSTElgsDnuKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قرارگاه تروریستی خاتم الانبیا
هشدار داد هر شرکت یا کشوری که بر اساس طرح غرامت ایالات متحده برای کشتی‌های آسیب‌دیده در طول جنگ، از دارایی‌های مسدود شده ایران وجهی برداشت کند، از عبور از تنگه هرمز منع خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/19878" target="_blank">📅 16:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19877">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ترامپ در مورد ایران:
لیندسی گراهام یک جغد جنگی در مورد ایران بود، اما در چند هفته گذشته، شروع به این فکر کرد که یک توافق بهتر از نابودی بقیه ایران خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/19877" target="_blank">📅 16:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19876">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa71f5aa10.mp4?token=G5kn4vIQ_xxHRUdNqan0b29UllLRWDVNha7iU0sDqV2ra2hC5jsNbu2Z1vJuU5Bfaf2k8TS9sFZccGUvTEW7A_FogqAkDJIWJ4L_zTlkeMml4i4IhYc4tFhJfPfJ-seid2USq69jpGyWzi_EfAwURJjPeoHAv0vhUMmC08tjIJIjjqEV3IbHCLl-p0h3g-llBzWun9APdp__mg86WtKrOKPgR10xfQDxY8EJVCVCDQs87O8p1nnYFSK3FM51Wbmi6-dirdnPGhN3ek-rDFJf2aRKVWDb9pzMD7sN_cAvm54IgNDgPmtmlvRTolFyPokr2hsYrts7VNU_e-uqNF1aQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa71f5aa10.mp4?token=G5kn4vIQ_xxHRUdNqan0b29UllLRWDVNha7iU0sDqV2ra2hC5jsNbu2Z1vJuU5Bfaf2k8TS9sFZccGUvTEW7A_FogqAkDJIWJ4L_zTlkeMml4i4IhYc4tFhJfPfJ-seid2USq69jpGyWzi_EfAwURJjPeoHAv0vhUMmC08tjIJIjjqEV3IbHCLl-p0h3g-llBzWun9APdp__mg86WtKrOKPgR10xfQDxY8EJVCVCDQs87O8p1nnYFSK3FM51Wbmi6-dirdnPGhN3ek-rDFJf2aRKVWDb9pzMD7sN_cAvm54IgNDgPmtmlvRTolFyPokr2hsYrts7VNU_e-uqNF1aQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران:
آنها موافقت کردند که سلاح هسته‌ای نداشته باشند. اساساً، ما باید این را رسمی کنیم، اما آنها موافقت کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/19876" target="_blank">📅 16:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19875">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b1021ee49.mp4?token=OXekXUSMlrjlfzrIUCoQAa_ubNodK6EvU4ah4qbNaR6Khx_pIHu_fJ7zsfsHMuIhn3o-rWkcnWTGJ1qzceBKH1k2L3O1RjBoZJwsMTb-fEmGbfUseEY4_Q1CNJAIAc0CEmiiHHxC93RyZKFJtMizIb7p5Ppu9SQbA0-8EJz8GnKr_cx-voxpob3wVLHLIqU90oZ3q6z_qm6Ewl6J1lkuvx5CH6Jox5HaCEjD_Bm5Z9sn5n_dapZLXZR94-WgDPDwMCYT3kLSL__VoxwTNXUTK-tMfymEsrv_DK8gYNV_1_bt-hRo3nfQV8g_nSdMnH_28Tt22-At7w7gZTFZtNQWYWd34DnC80ebZzP2eYocJJQpFRWD3f5-TfLfR3OYJIBypiB8ugmxZDODJZpK3N9cWSMphG4u7H1ZvBStWAvFfiswTpslLAnZYje5Q_r3WGWmlfUlXEiKKKtVG1cnORZq1ZgMW_shrl1_KU99T0WLA5q1HCxmY5W38CelAsWte8stdQL2KdzPNglUWj3GJjUTmSOTFGP81efhFjyAjhi1WWl6NhCvzmPAViL_n7zm3psm81DtTNCpf0pfnROvOt2Fj3vnb4OM2UWEzkmUzPCieh9OoH2ZsHh7JLnMEArp4db3qDthApdBjxuqBMdoVWtcQ2E_BkJPrl_QK0vrcOTamSM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b1021ee49.mp4?token=OXekXUSMlrjlfzrIUCoQAa_ubNodK6EvU4ah4qbNaR6Khx_pIHu_fJ7zsfsHMuIhn3o-rWkcnWTGJ1qzceBKH1k2L3O1RjBoZJwsMTb-fEmGbfUseEY4_Q1CNJAIAc0CEmiiHHxC93RyZKFJtMizIb7p5Ppu9SQbA0-8EJz8GnKr_cx-voxpob3wVLHLIqU90oZ3q6z_qm6Ewl6J1lkuvx5CH6Jox5HaCEjD_Bm5Z9sn5n_dapZLXZR94-WgDPDwMCYT3kLSL__VoxwTNXUTK-tMfymEsrv_DK8gYNV_1_bt-hRo3nfQV8g_nSdMnH_28Tt22-At7w7gZTFZtNQWYWd34DnC80ebZzP2eYocJJQpFRWD3f5-TfLfR3OYJIBypiB8ugmxZDODJZpK3N9cWSMphG4u7H1ZvBStWAvFfiswTpslLAnZYje5Q_r3WGWmlfUlXEiKKKtVG1cnORZq1ZgMW_shrl1_KU99T0WLA5q1HCxmY5W38CelAsWte8stdQL2KdzPNglUWj3GJjUTmSOTFGP81efhFjyAjhi1WWl6NhCvzmPAViL_n7zm3psm81DtTNCpf0pfnROvOt2Fj3vnb4OM2UWEzkmUzPCieh9OoH2ZsHh7JLnMEArp4db3qDthApdBjxuqBMdoVWtcQ2E_BkJPrl_QK0vrcOTamSM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران:
اگر به عقب برگردم و کار را تمام کنم، همانطور که بعضی‌ها دوست دارند، با پل‌ها - خیلی راحت می‌توانم بیشتر پل‌هایشان را در کمتر از یک ساعت خراب کنم.اما می‌دانید، ساخت یک پل برای آنها 10 سال طول می‌کشد. پل‌ها طولانی‌ترین زمان را می‌برند و نیروگاه‌ها در رتبه دوم قرار دارند.من می‌توانم نیروگاه‌ها را در عرض یک روز از کار بیندازم. تمام نیروگاه‌هایشان از بین خواهند رفت.
فکر می‌کنم حدود 91 میلیون نفر بدون برق، بدون پل، باید زندگی کنند. و این یک تعادل بسیار بسیار ظریف است.آنها می‌دانند که اگر آنها توافق نکنند، من این کار را خواهم کرد.پل‌ها به معنای واقعی کلمه از بین خواهند رفت. در کمتر از... به نظرم در دو ساعت، بیشتر پل‌ها، پل‌های اصلی، همه از بین خواهند رفت.و نیروگاه‌ها در یک روز.اگر بتوانم از انجام این کار اجتناب کنم، می‌خواهم از آن اجتناب کنم.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/19875" target="_blank">📅 16:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19874">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8482ff12f2.mp4?token=Dfmcn49QEzgBwQziDDOvhXuYzDeVUXVPgrcCzNwZKpHqb0tl2dwaq1wcwJMbor1Ra_ETXF5yLmfUFwySGuwe0raD7Zy36xCYpnw3ket3EpN0rMUgAYShtQQpl8V9wneb1Ih4MsQD-G1S824oZhGnENfexoJA7v-VVRooHrIOExLS_-4fdQ_8rIywzEP_otQevVAGSqFFneYyfGViGujSdg99ySEgC0uq2BREy52SH6KhZLu5Mpod8593pBt0xJFCc7KYQqaiXcw7kd33t2KnSraQzWJ-aQ4ozg98fej9oSBGs1eZ9LdqbNnXECKvwtTEF8TtAdrhwn5qFg5Sx1MRGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8482ff12f2.mp4?token=Dfmcn49QEzgBwQziDDOvhXuYzDeVUXVPgrcCzNwZKpHqb0tl2dwaq1wcwJMbor1Ra_ETXF5yLmfUFwySGuwe0raD7Zy36xCYpnw3ket3EpN0rMUgAYShtQQpl8V9wneb1Ih4MsQD-G1S824oZhGnENfexoJA7v-VVRooHrIOExLS_-4fdQ_8rIywzEP_otQevVAGSqFFneYyfGViGujSdg99ySEgC0uq2BREy52SH6KhZLu5Mpod8593pBt0xJFCc7KYQqaiXcw7kd33t2KnSraQzWJ-aQ4ozg98fej9oSBGs1eZ9LdqbNnXECKvwtTEF8TtAdrhwn5qFg5Sx1MRGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگر توافق نکنیم به راحتی کوه کلنگ را از بین می‌بریم
ترامپ
به فاکس
:
" من دقیقاً می‌دانم در کوه کلنگ چه می‌گذرد، مشکل بزرگی نیست. ما سایت‌های هسته‌ای آنها را از بین بردیم و اگر توافق نکنیم، باید کلنگ را از بین ببریم. اگر توافق نکنیم، خیلی راحت آن را از بین خواهیم برد."
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/19874" target="_blank">📅 16:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19873">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رویترز به نقل از یک منبع خلیج فارس:
عمان حمایت کشورهای خلیج فارس را برای طرحی که به تهران اجازه می‌دهد داوطلبانه برای استفاده از تنگه هرمز هزینه دریافت کند، جلب کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/19873" target="_blank">📅 15:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19872">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">رسانه‌های عبری: دفاتر نتانیاهو و زلنسکی در حال هماهنگی برای دیداری سه جانبه در واشنگتن هستند؛ با وجود سردی روابط، دو طرف ، ولی در موضوع ایران منافع مشترکی دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/19872" target="_blank">📅 15:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19871">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cec75b87ae.mp4?token=TbRsGd5MA_0dL9EhtGkE_VHXn7Op596LFLCY1BAfU0H-nWCffiX4UJB7IZxUQyz-JfPkxPJFVE0360d9J39vYGOIvszu8kk59r7-UsZjfPCzW_Ito6n4CZBv0MLdikdG8baKrmcopNVsYcl7MAgzQ4wl57xKA1dduxDrtX5QgOf6RmIr0P3owmIgPbP_Q8cHuM6RtHQAMn0BZ6UNPyEJ8Q1Ll4dNsjA5EUuy7OFdtFKdXHotyZGGFvbYsYRb38QbjPQEnbnc0EfwDN6kHvjrmpDp-mI2wzg0nhfFAu3fgu4JItxpgrOUqGsbv2wuD7lmb8Kxfn2sgs1IOqKtP6qhCJEGhtDkyFFJp20J7Tm0DiyeR1D9-qQbMJLVwlFk-S6dir0ka_LXCxsddyLb4aDHhJ8FBPtDPd1-K9gcjhxkhNaVyRS_CJ_yl4UO31WqAzk1R0QPGph4Vv7Y2VttcYFrSMoi4527HTGu_vu-s0LRuXA7qYHkrBE2RKe4MXa3GckEMEz7KaJXjioLFQIKxI50xelIlSIrl5EH8B515BXXFhU5BADJfxJ4anC4Im0Srt_u-0pxbfeBjpxMSdlbZ8LOdFG_0rz0ttEjr9AvOGOUBSn-mqtK22wPe7KWFT0ESeAbz_7oPsQoYisDz86Z538iA-bnDSGg6mcPXd5p74J2eJ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cec75b87ae.mp4?token=TbRsGd5MA_0dL9EhtGkE_VHXn7Op596LFLCY1BAfU0H-nWCffiX4UJB7IZxUQyz-JfPkxPJFVE0360d9J39vYGOIvszu8kk59r7-UsZjfPCzW_Ito6n4CZBv0MLdikdG8baKrmcopNVsYcl7MAgzQ4wl57xKA1dduxDrtX5QgOf6RmIr0P3owmIgPbP_Q8cHuM6RtHQAMn0BZ6UNPyEJ8Q1Ll4dNsjA5EUuy7OFdtFKdXHotyZGGFvbYsYRb38QbjPQEnbnc0EfwDN6kHvjrmpDp-mI2wzg0nhfFAu3fgu4JItxpgrOUqGsbv2wuD7lmb8Kxfn2sgs1IOqKtP6qhCJEGhtDkyFFJp20J7Tm0DiyeR1D9-qQbMJLVwlFk-S6dir0ka_LXCxsddyLb4aDHhJ8FBPtDPd1-K9gcjhxkhNaVyRS_CJ_yl4UO31WqAzk1R0QPGph4Vv7Y2VttcYFrSMoi4527HTGu_vu-s0LRuXA7qYHkrBE2RKe4MXa3GckEMEz7KaJXjioLFQIKxI50xelIlSIrl5EH8B515BXXFhU5BADJfxJ4anC4Im0Srt_u-0pxbfeBjpxMSdlbZ8LOdFG_0rz0ttEjr9AvOGOUBSn-mqtK22wPe7KWFT0ESeAbz_7oPsQoYisDz86Z538iA-bnDSGg6mcPXd5p74J2eJ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فروریختن یک مرکز خرید در ژاپن در پی وقوع زلزله ۷/۱ ریشتری
به گزارش "ان اچ کی"، شمار زیادی زیر آوار گرفتار شده و شماری مصدوم شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19871" target="_blank">📅 15:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19870">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">آمیت سگال:در اقدامی که از دونالد ترامپ کمتر دیده می‌شود، دیدار او با بنیامین نتانیاهو دور از حضور دوربین‌ها برگزار خواهد شد؛ موضوعی که پیام‌های زیادی در خود دارد
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19870" target="_blank">📅 15:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19869">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‏شالوم بن حنان، از مقامات ارشد پیشین سازمان امنیت داخلی اسرائیل (شاباک)، گفت در طول سال‌ها صدها هزار حساب کاربری رباتی که بیشتر آن‌ها وابسته به رژیم جمهوری اسلامی بودند، شناسایی و مسدود شده‌اند. به گفته او، این شبکه‌ها با هدف مداخله در انتخابات اسرائیل، تأثیرگذاری بر افکار عمومی و ایجاد هرج‌ومرج فعالیت می‌کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19869" target="_blank">📅 15:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19867">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">وزیر جنگ اسرائیل:ما قویاً خواهان حمله به تأسیسات انرژی ایران هستیم، اما ایالات متحده در حال حاضر اجازه این کار را نمی‌دهد
۷۰ درصد غزه را نابود کردیم و الگوی آن را به جنوب لبنان منتقل کردیم.
ایالات متحده در موضوع ایران ملاحظات و منافعی دارد که با منافع اسرائیل متفاوت و فراتر از آن است.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19867" target="_blank">📅 13:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19866">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">کانال ۱۲ اسرائیل , وزیر دفاع کاتز فاش کرد: جنگنده‌های آمریکایی از اسرائیل برای انجام حملات به ایران به پرواز درمی‌آیند‌ و ایرانی‌ها از این موضوع آگاه هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19866" target="_blank">📅 13:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19865">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مهاجرانی: هواپیمای تازه‌خریداری‌شده در فرودگاه بوشهر بر اثر اصابت موشک منهدم شد؛ تنها بخشی از دم هواپیما باقی مانده است
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19865" target="_blank">📅 12:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19864">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سی‌ان‌ان‌ به نقل از مقام کاخ سفید: ترامپ در کاخ سفید با زلنسکی و نتانیاهو به طور جداگانه و پشت سر هم دیدار می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19864" target="_blank">📅 11:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19863">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حقیقت یاب اتاق جنگ :گزارش رسانه های غیررسمی در اینستاگرام و تلگرام نادرست است مبنی بر اجرای حکم ۳ نفر . دیشب مردم اصفهان درگیر شدند تیر اندازی شد و جلادان فقط توانستند دو نفر از عزیزان را اعدام کنند و یک نفر اعدام نشد. @WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19863" target="_blank">📅 11:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19862">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مدیرکل مدیریت بحران استانداری اصفهان:صداهای شبیه به انفجار در برخی مناطق جنوب و غرب اصفهان، بهارستان و حومه ارتفاعات صفه و شهر ابریشم شنیده خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19862" target="_blank">📅 11:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19861">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سخنگوی دولت: سهمیه بنزین ۳ هزار تومنی از ۱۰۰ لیتر به ۵۰ لیتر کاهش پیدا کرده
اما هنوز هیچ تصمیمی به صورت جمع‌بندی شده برای قیمت بنزین در جایگاه نگرفتیم
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19861" target="_blank">📅 11:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19860">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‏زلنسکی و نتانیاهو همزمان به کاخ سفید رسیدند
‏ولودیمیر زلنسکی، رئیس‌جمهوری اوکراین، و نتانیاهو، نخست‌وزیر اسرائیل، همزمان وارد کاخ سفید شدند تا در دیدارهایی جداگانه با پرزیدنت ترامپ گفت‌وگو کنند.
‏همزمانی حضور این دو رهبر در کاخ سفید، گمانه‌زنی‌ها درباره احتمال دیداری محرمانه میان آن‌ها برای جنگ همه‌جانبه با رژیم جمهوری اسلامی را افزایش داده است.
‏این دیدارها در شرایطی انجام می‌شود که پرونده‌های امنیتی مهمی از جمله جنگ اوکراین و تهدیدهای مرتبط با رژیم جمهوری اسلامی در دستور کار واشنگتن قرار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19860" target="_blank">📅 10:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19859">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">حقیقت یاب اتاق جنگ :گزارش رسانه های غیررسمی در اینستاگرام و تلگرام نادرست است مبنی بر اجرای حکم ۳ نفر . دیشب مردم اصفهان درگیر شدند تیر اندازی شد و جلادان فقط توانستند دو نفر از عزیزان را اعدام کنند و یک نفر اعدام نشد. @WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19859" target="_blank">📅 10:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19858">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">حکم ابوالفضل سپاهی بادجانی و امیرحسین صفری حسین‌آبادی در اصفهان انجام شد و جاویدنام شدند  @WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19858" target="_blank">📅 09:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19857">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">جلسۀ شورای هماهنگی مجلس با حضور قالیباف
سخنگوی هیئت‌رئیسۀ مجلس: صبح امروز جلسۀ شورای هماهنگی مجلس با حضور قالیباف، اعضای هیئت‌رئیسه و رؤسای کمیسیون‌های تخصصی تشکیل شد.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19857" target="_blank">📅 09:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19856">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppXA1AoQDQary_LvjAHwMlPoa2N6xeVQoUNC-iMgcwLbSO_f3Ygn5jIgNoZmpPps0KjglNR4760beztNd-VYbo08dyiYF0ifO5UKq7GXl-H2b3dhPMfDiyyCrLrjnEmBkQoMVvYdeW221P3doDeUkSeFo2S8nE3VIvD5_0wbRTtwAj_UgOYy2RHPy-rjNmNxkVMYehL6--t_hlF0fDbSxQD6h2AcaUKPOdRKCFEPQb4XDOEfjf9BmRcaB2yGpDz0IYZbg0YLrO2zmmXlcH_OZ74Lozus0VvqxUtow7tDxanQdaYYcZiYBSH8q0kkFqsTY8bt0cDTgnVXeNnrmORzOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویرک پست : ملانیا و بارون ترامپ در ویدئویی نگران‌کننده که ترور آنها را تشویق می‌کند
یک ویدئوی جدید از ایران، حامیان رژیم اسلامی را به ترور همسر رئیس جمهور ترامپ تشویق می‌کند.
این ویدئو با عنوان «چگونه ملانیا ترامپ را بکشیم» تصاویری از بانوی اول را در کاروان موتوری و در برخی مکان‌های اطراف شهر نیویورک نشان می‌دهد و حتی نام برخی از فروشگاه‌های طراحان مد که او از آنها خرید می‌کند را نیز ذکر می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19856" target="_blank">📅 09:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19855">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">روزنامه لبنانی "النذاع الوتان"، که با مخالفان حزب‌الله همسو است، امروز به نقل از منابع خود گزارش داد که ایالات متحده پیامی قاطع و جدی به لبنان ارسال کرده است. این پیام حاکی از آن است که هزینه دخالت حزب‌الله به نفع ایران و انجام حملات علیه اسرائیل ( در صورتی که ایالات متحده یک عملیات گسترده علیه تهران آغاز کند ) بسیار سنگین خواهد بود. منابعی که در این روزنامه ذکر شده‌اند، گفتند که این پیام به این معناست که هر راکت یا پهپادی که به سمت اسرائیل شلیک شود، در واقع دروازه‌های جهنم را برای حزب‌الله و لبنان باز خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19855" target="_blank">📅 09:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19854">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گزارش انفجار در اردن
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19854" target="_blank">📅 08:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19853">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2d1rqY7HGX_K6DoStD3Kn2bGFFeGls84LrQx30u-3uoFNzFbuItfcxy__jZYbZX41wqipIWiCUfFTCapvhRDbHKReXmkDzvgdx73z4-0E83hA1I5v0rH_NUaxDjqJb6XJ1t-JpcqnAB3ZX4QjglTY5ZM66kNZyzt_dboWKFjxh5hEkS1ARZ71Fgr477fzocaUsIX1Ycv3DZHVN4qnG7c-CzII5gwj5xWERdsW5wbvTUXQbY6idpF8B1RfEYvbdBzDGXBKcxb6IBGQTeHeJpnA9hqlady2xK0yAmifwvJ33GnAiHpkvG0GaDJdgj-ShgAdF4zdLgLPLvv8QQYzuFfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار نفت سعودی شده و همکنون 89 دلار است.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19853" target="_blank">📅 08:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19852">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KxHR0LnBy2jygwBxhfKT-lyz-4KdRmbZyOzYj4IPb80fuB91rU_0nb4uEXcnXXkqxD3wRghgTMGrYS4Qd0kRveqUunr6OAmVc-9ZT_VhfVLk2D4CCtoGtAsyKKLI4FGv9jYF3HZHfK1zPFIonJE65DJmuIjK7gKN8ShFTukOU5hDRFfiNEd9ioRirWsYBIy1zPpDqUSr20FnO3QwvuIhHcKF9N8-7jIz-q1uKsiM7kQO6h6fdwYxvkU-YKKVf91xGKZVIlhPBPps_1owMzUuZ4R9ieMssr9t9Xfww5J0rbFTB-PK17WMLOo3mmr4qQ7b8Macie9uEeQvtsF51UnoRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو و همسرش با «اطلاعات محرمانه‌ای» درباره ایران و تأسیسات هسته‌ای کوه کلنگ وارد واشنگتن دی‌سی شدند
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19852" target="_blank">📅 08:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19851">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">به گزارش وال استریت ژورنال، رئیس جمهور ترامپ پس از آنکه بیش از یک سال به مشاورانش گفته بود که کیف در حال شکست در جنگ است، به طور فزاینده‌ای نسبت به چشم‌انداز اوکراین در جنگ علیه روسیه خوش‌بین شده است.
ترامپ «برندگان را دوست دارد» و اکنون به طور فزاینده‌ای زلنسکی را یکی از آنها می‌داند. انتظار می‌رود این دو رهبر روز سه‌شنبه در جریان سفر زلنسکی به واشنگتن برای مراسم تشییع جنازه سناتور لیندسی گراهام در کاخ سفید دیدار کنند.
او تحت تأثیر صنعت پهپاد اوکراین، به ویژه توانایی آن در مقابله با پهپادهایی مشابه پهپادهایی که ایالات متحده در جریان درگیری با ایران با آنها مواجه شده است، قرار گرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/19851" target="_blank">📅 08:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19850">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">حکم ابوالفضل سپاهی بادجانی و امیرحسین صفری حسین‌آبادی در اصفهان انجام شد و جاویدنام شدند
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/19850" target="_blank">📅 08:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19849">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">شنیده شدن صدای انفجار در اربیل در شمال عراق
@WarRoom</div>
<div class="tg-footer">👁️ 173K · <a href="https://t.me/withyashar/19849" target="_blank">📅 00:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19847">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9da687f9ab.mp4?token=Ee9r7lKSR5Ec7bd44YGtT8IT2QJauoRz0TFpOCHxyyIAqEUXVa40SMMVPkqi7cTzykVhxquF5ZfsfFOCR1v1rSHCp2h5BKQYi-CQVNPi8q2I2Q2hLacACxFun246IJd-IbmpC7eO0XIBRWev37_WySpz05v7ZNRhIeaxULZSup76j-dd-DNjCEnc8uQ6nYv4wdVKuGgyqaR6UJ4rJ0MiwVJH69cjGa-oGeTZdupFWRo8IruqktNDKuE20EsYEYuk617qVFIhiGDZhcLahvlGFwXp4_OfgX4ETTQLBPQ-XHKYVDD1wogD6di2tSdv-jiXpCjOIanzsOnhWQJCKu5o8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9da687f9ab.mp4?token=Ee9r7lKSR5Ec7bd44YGtT8IT2QJauoRz0TFpOCHxyyIAqEUXVa40SMMVPkqi7cTzykVhxquF5ZfsfFOCR1v1rSHCp2h5BKQYi-CQVNPi8q2I2Q2hLacACxFun246IJd-IbmpC7eO0XIBRWev37_WySpz05v7ZNRhIeaxULZSup76j-dd-DNjCEnc8uQ6nYv4wdVKuGgyqaR6UJ4rJ0MiwVJH69cjGa-oGeTZdupFWRo8IruqktNDKuE20EsYEYuk617qVFIhiGDZhcLahvlGFwXp4_OfgX4ETTQLBPQ-XHKYVDD1wogD6di2tSdv-jiXpCjOIanzsOnhWQJCKu5o8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست وزیر قطر: پول‌هایی که به حماس پرداخت می‌شد، شفاف بود و با مجوز دولت بنت انجام می‌شد.
@WarRoom</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/withyashar/19847" target="_blank">📅 23:46 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
