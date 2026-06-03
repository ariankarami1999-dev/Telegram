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
<img src="https://cdn4.telesco.pe/file/qegKs_oH9UrZBAiWNu7PKcQtxTfNNHILGM3gdaCLan3ZppQO-vG4P2GLsejpQPZUaJcF4kkq7WTfZq5xTEARqmqpkq-5tU0KJ3waPitG75qyz4gzipOxlzWgGXK7pmXaMGW_HVzPOWIxLxW2-GJEtiFLnuerOiqC_13OcVnZhY6u5YGybXQlPLGpBSLFqa7NF8GrOGx1tPvCB2LiTtd4TjUzqMOeLxL9oBAUs0o15p3pby2thxDoz3ykATkrNBi1YiTdcr8cYtwOQswxIyzGtzQJbn3Ppa3ErV6o9k6cwzuZ926j6szXsuWudU2Smnfsq6dz3Om0IcCP68Kh7TUbJw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 288K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 00:03:17</div>
<hr>

<div class="tg-post" id="msg-13449">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a531a29092.mp4?token=G-0LBpEib7Ul2FDagvzCOttCsX_l3hmLbj832sl3GqGfW8gNQbD4uHlMpiKRVaZudOQ_WFn1-I4xtj57WtXrDgtNz4OQseDNRAdqoFINnuw7ISBIsqDZ782-frnV4Uq2m1np8csdBvfCKZa4J251_J0vu7Blk7i7S4lUBTyrojOC3fWTfXow0e-bQ9o1rz9b1OqCPQxnu4hx3WIDKPW_dBBQbI_DEcuJ7Dr2ai-eP8p_x__1ma556G5XEqcLE-Z6Y_x7GHKv6u5pqip1NBaW7_QgenxaNGFetDm7frT-71UzrZkSQ-PuevrSRi8KYgPFFDE-i6kXGqbCbNLx4_sT8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a531a29092.mp4?token=G-0LBpEib7Ul2FDagvzCOttCsX_l3hmLbj832sl3GqGfW8gNQbD4uHlMpiKRVaZudOQ_WFn1-I4xtj57WtXrDgtNz4OQseDNRAdqoFINnuw7ISBIsqDZ782-frnV4Uq2m1np8csdBvfCKZa4J251_J0vu7Blk7i7S4lUBTyrojOC3fWTfXow0e-bQ9o1rz9b1OqCPQxnu4hx3WIDKPW_dBBQbI_DEcuJ7Dr2ai-eP8p_x__1ma556G5XEqcLE-Z6Y_x7GHKv6u5pqip1NBaW7_QgenxaNGFetDm7frT-71UzrZkSQ-PuevrSRi8KYgPFFDE-i6kXGqbCbNLx4_sT8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«ما می‌توانیم دو یا سه هفته دیگر ادامه بدهیم و همه را از بین ببریم. انجام این کار خیلی آسان است.
اما اگر بتوانیم چیزی را روی کاغذ بیاوریم و مکتوب کنیم که بدون کشتن همه، همان نتیجه را به دست بدهد، ترجیح می‌دهم آن راه را انتخاب کنیم.»
@withyashar</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/withyashar/13449" target="_blank">📅 00:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13448">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b07761ae5b.mp4?token=G4NyzB478YdIJX7BynEGNbDmWtI9Qy9mRjXz1bWE1dYgpLIW3NzYf2t1v98ZamC3pgkKGY1HRapwfIq7hK5Au4EP6Pt9CWW5yzkq8MSI2yfB6u9mSk1vteE3aIMkyQj673VchVY45QUzPxq_U2OIebk-4UMm6sMPddrvRyxZxvreEr-IBBSM3xi6Xg_wEGNgMSLHA-M5BLCflt61saLN61zIuufLGbJYyf9NsjWD5rIL7K7ERDLax7Rxvsj97SYmUDBRNyf0ZEV2lzyqN4xN1yg-_cdfrgn9tJAKbJEK-w3FEjBRXyEtF7FWnnFPc7Niwuv3hcrmYc5yMvlvIUlh6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b07761ae5b.mp4?token=G4NyzB478YdIJX7BynEGNbDmWtI9Qy9mRjXz1bWE1dYgpLIW3NzYf2t1v98ZamC3pgkKGY1HRapwfIq7hK5Au4EP6Pt9CWW5yzkq8MSI2yfB6u9mSk1vteE3aIMkyQj673VchVY45QUzPxq_U2OIebk-4UMm6sMPddrvRyxZxvreEr-IBBSM3xi6Xg_wEGNgMSLHA-M5BLCflt61saLN61zIuufLGbJYyf9NsjWD5rIL7K7ERDLax7Rxvsj97SYmUDBRNyf0ZEV2lzyqN4xN1yg-_cdfrgn9tJAKbJEK-w3FEjBRXyEtF7FWnnFPc7Niwuv3hcrmYc5yMvlvIUlh6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
در آن بخش از جهان«خاورمیانه»، آتش‌بس زمانی است که شما به شیوه‌ای معتدل‌تر تیراندازی می‌کنید.
@withyashar
🤣</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/withyashar/13448" target="_blank">📅 23:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13447">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ درباره حمله ایران به کویت:
برای هر چیزی دلیلی وجود دارد، و ما به آنها ضربه‌ای سخت زدیم... آنها کمی تحریک شده بودند؛ آنها در حال پاسخ دادن بودند.
@withyashar</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/withyashar/13447" target="_blank">📅 23:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13446">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترامپ : مذاکرات عالی پیش میره
می‌توانیم جنگ را دو یا سه هفته دیگر ادامه دهیم و همه را نابود کنیم اما ترجیح می‌دهم این کار را نکنم
هر اتفاقی ممکن است برای ایران بیفتد، و رهبری ایران سه بار تغییر کرده است
@withyashar</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/withyashar/13446" target="_blank">📅 23:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13445">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گزارش انفجار‌ قشم
🚨
@withyashar</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/withyashar/13445" target="_blank">📅 23:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13444">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ:دیشب و پریشب به ایران حمله کردیم و ضربه سختی به آنها زدیم
@withyashar</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/withyashar/13444" target="_blank">📅 23:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13443">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G25B1ggMkFyCqIKDtIefiWwyaar1kyIqWjoZU4rl9wXpZHlenpd03rvALIKB5BKJMq-dPafJsU8Q1mYdoWYnwtwaKBZW6h_wBfKX_5o5MO3LxOHwQKU_OExJTez1kvCYXQGzLNeq10PsQaixMwSyum4cU4gWcbeAZ8cDtrLKBMvFns9n00f6OuX5q-Hb44Ug2R7UCVv6Yg1xUf9OTLMsG2kMc0N709ATHidQcGUJDQyeuVJe4-kKtGBc2WtojioKnigv9HHIeyHB-RMV9KuQlRhHgSmL2ZNWtUKpxHRoqkjqjbrv3VwljS9oihaMYIUqWZ6KBEJOL_nCXnEOlFNFlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مذاکرات بین اسرائیل و لبنان به زودی به پایان خواهد رسید. به زودی اعلامیه‌ای از سوی ایالات متحده منتشر میشه.
@withyashar</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/withyashar/13443" target="_blank">📅 23:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13442">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دفتر بازرس کل وزارت دفاع آمریکا در حال آغاز یک بررسی (بازبینی و تحقیق رسمی) درباره «عملیات خشم حماسی» (Operation Epic Fury) است؛ کارزار نظامی آمریکا علیه ایران که با هدف برچیدن تهدید هسته‌ای تهران انجام شد.
@withyashar
این آغاز یک بررسی یا بازرسی رسمی است، نه لزوماً افشای تخلف یا شکست.
Office of Inspector General (OIG)
نهاد بازرسی داخلی وزارت دفاع آمریکاست و معمولاً پس از عملیات‌های بزرگ نظامی، نحوه برنامه‌ریزی، اجرای عملیات، هزینه‌ها، تلفات، رعایت قوانین و عملکرد فرماندهان را بررسی می‌کند</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/withyashar/13442" target="_blank">📅 23:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13441">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">پدافند شهریار فعال شد
🚨
@withyashar
اینو دیگه دوستم اونجاست و وارده</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/withyashar/13441" target="_blank">📅 23:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13440">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTVjecQ3oAK4JE8WvSMV-6L3kSgtOesCh0F5Ltxe0ejI5g1Qce-MmtKVKSUfKbgWpJZ00DdJo_bBg8SJNS679KmTF4Xdq3mZNeqxYLiCEjRSeQjVp7iBe8jbquD_E40jp5V4b1WAeAFJL0vuGMP-q0sowSbXaWVm72_PVBmVSohtuLANEc4qoah96bYJhJpzvZCrf-ODOQ3UO2O8NLruzo4utSNVfJyzzLIVFIwYZepSkZ1JWcay5zCZcQ7lhzmgCTKW39_AW7lUsQF3t2A1b9_hbnGFy3A8aB5g7K87bhiyLYpMebNEGrQx32fAKHCS7nsRWsr_XxuYQqoZuvCGpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من بلافاصله پس از یکی از سرگرم‌کننده‌ترین شب‌های تاریخ آمریکا، یعنی مسابقات قهرمانی جهان UFC در چمن جنوبی کاخ سفید، به اجلاس گروه ۷ در فرانسه خواهم رفت. سوابق نشان می‌دهد که اگرچه در طول تاریخ طولانی و پرماجرای کاخ سفید، مبارزاتی در سطح بسیار پایین‌تر در این کاخ برگزار شده است، اما هیچ رویدادی حتی نزدیک به این، یعنی بزرگترین مبارزان جهان، قهرمانان جهان، برای مجلس عوام در نظر گرفته نشده است! رئیس جمهور دونالد جی. ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/withyashar/13440" target="_blank">📅 23:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13439">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وزارت کشور بحرین به دلیل خطر احتمالی آژیر خطر را فعال کرد و از شهروندان خواست به نزدیک‌ترین مکان امن بروند.
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/withyashar/13439" target="_blank">📅 23:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13438">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نیروی دریایی جمهوری اسلامی ساعتی پیش یک ناو جنگی آمریکا را در دریای عمان هدف قرار دادیم @withyashar
🚨</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/withyashar/13438" target="_blank">📅 23:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13436">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">رویترز: رسانه‌های ایران گزارش دادند که تهران به یک کشتی نظامی آمریکایی که ادعا می‌شود حامل «مرکز فرماندهی و کنترل» بوده، هنگام نزدیک شدن به آب‌های سرزمینی ایران در خلیج عمان حمله کرده است
@withyashar</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/withyashar/13436" target="_blank">📅 22:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13435">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c287d7f770.mp4?token=teCDv7PhckqGEFHypB38QeNQMAoW1dVfdnQjDMxHPpEaCZQ9N5Q0OGpP0ymZUKLvPzAQemALVuthkh_mCa7gCMUWdeLnhch9OAWsvEEVHji9UPSPpRk_euN1KwX3xLpwdLyQszd-ADA2boxPFnc4Sn1FOjEGvcCW0TsEx8pEl88O9GI6hS1xosGWN_p0fUkzuv2AassDJLaw5dATdMoWpeF_8dOhLQWczSZ-HFv365e23SUVKbojUhJOM1iFbPThBDsKh1Y70soAl8sIPYoAs3W_LLQAopbs8mCEZrpvxqZRgJOKctvb0priT5dD2NnjYY5yRZ7U0Zm-qNSXKsLfkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c287d7f770.mp4?token=teCDv7PhckqGEFHypB38QeNQMAoW1dVfdnQjDMxHPpEaCZQ9N5Q0OGpP0ymZUKLvPzAQemALVuthkh_mCa7gCMUWdeLnhch9OAWsvEEVHji9UPSPpRk_euN1KwX3xLpwdLyQszd-ADA2boxPFnc4Sn1FOjEGvcCW0TsEx8pEl88O9GI6hS1xosGWN_p0fUkzuv2AassDJLaw5dATdMoWpeF_8dOhLQWczSZ-HFv365e23SUVKbojUhJOM1iFbPThBDsKh1Y70soAl8sIPYoAs3W_LLQAopbs8mCEZrpvxqZRgJOKctvb0priT5dD2NnjYY5yRZ7U0Zm-qNSXKsLfkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی جمهوری اسلامی امروز ویدیویی منتشر کرد که نشان می‌دهد ساعاتی پیش موشک‌های ضد کشتی از کنار ساحل به سمت یک ناوشکن آمریکایی در خلیج عمان شلیک کرده اند
@withyashar</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/withyashar/13435" target="_blank">📅 22:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13434">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">الجزیره: ستاد فرماندهی مرکزی ایالات متحده ادعاهای ایران مبنی بر اینکه خسارت به ترمینال مسافربری فرودگاه کویت ناشی از موشک رهگیر آمریکایی بوده، را تکذیب کرد
@withyashar</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/withyashar/13434" target="_blank">📅 22:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13433">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohamad▪️</strong></div>
<div class="tg-text">سمت منیریه پدافند که داره میزنه
یه صدا انفجار ام اومد ۵دقیقه پیش</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/withyashar/13433" target="_blank">📅 22:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13432">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پدافند تهران فرودگاه مهرآباد فعال شد
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/withyashar/13432" target="_blank">📅 22:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13431">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🤬</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/withyashar/13431" target="_blank">📅 22:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13430">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">فارس: نیروی دریایی ارتش یک ناوشکن آمریکایی که قصد شرارت رو داشت رو با موشک هدف قرار دادند  @withyashar
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/withyashar/13430" target="_blank">📅 22:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13429">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پدافند پرند فعال شد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/withyashar/13429" target="_blank">📅 22:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13428">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">گزارش هایی از پدافند غرب تهران
🚨
@withyashar</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/withyashar/13428" target="_blank">📅 22:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13427">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فارس: نیروی دریایی ارتش یک ناوشکن آمریکایی که قصد شرارت رو داشت رو با موشک هدف قرار دادند
@withyashar
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/withyashar/13427" target="_blank">📅 22:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13426">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
بچه جنگ شروع شد
@withyashar</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/withyashar/13426" target="_blank">📅 22:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13425">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElkBYcFyy8dhoX_gMv7Es7ZjL7n4yUObkBnaygR088FSEJ5Xqbde8Pu9kPTo1ymLURP0rZUD4QDTqzmvw4J0oWZNVklKo_xgFo14xxY1a71nZ3ntEpJNXQWkk4bpEDd69nVj-_Fbvx6l19bAmJ7oAa1OUaZYQSHux0xLMPjGIwQW0DowiVsHHZpIvFZFQR2AsapuyNcdJp7EMb8EPg9EBO-0TDooXoxueHACFK2Wh8jFTOWc8hrnH5t6HSFrKm5jJArgZWYWdwnjed72eKC_b6pRPGyiBTQJukCwZQ2sMVtUB-QHFWfK_yc4IjKfXp0TXlHnCs5o8zvdCx-p2gtMqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه های داخلی آخرین عکسی که از حاکمان سلسله مموشیان در ایران کنار هم بودند را منتشر کردند.
@withyashar</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/withyashar/13425" target="_blank">📅 22:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13424">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اتاق جنگ با شما : پدافند شیراز ساعت ۲۲:۲۷ دقیقه فعال شد!
@withyashar</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/withyashar/13424" target="_blank">📅 22:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13423">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">تسنیم به نقل از عراقی: ایران آمادگی کامل برای ادامه جنگ برای مدت بسیار طولانی را دارد و ما از توانایی‌های نظامی لازم برخورداریم.
@withyashar</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/withyashar/13423" target="_blank">📅 22:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13422">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">عراقچی: در حال حاضر هیچ روشی در مذاکره وجود ندارد، اما پیام هایی با آمریکایی ها رد و بدل می شود
دو روز پیش پیامی به آمریکایی ها مبنی بر لزوم توقف تجاوزات اسرائیل به بیروت فرستادیم
تماس ما با آمریکایی ها قطع نشد اما پیشرفتی در مذاکرات حاصل نشد.
@withyashar</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/withyashar/13422" target="_blank">📅 22:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13421">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAS6j_yUcUF2odcP2pbIn6-9rmaPpobYWcTRgD1uooIElUqN2UYBgTBoXs8TVvAyQKeg6HNnbU9aDUtmmedrqwu5bvQzw6NRnOxsRBsKiy7Dg1drVoTKjBiApBbj48ZTP9ypqhia-kxZVnqHWGz-04v__1CycS_IsVFtVQ3vgVlcHYKkGnyHBYIpVp5fqNmAtHzHZ6oZNe6TVR6szkI8hRam8wpNV-jTZjYb0bVlwzH6ZCkIpnpr79UYLK_cyjFOi2Jt5VXGI_H-j7Uie860Yzc-Qa2xGUKkm0oKiSXOj_m9dNUSewakU_zzowwR3k97j4WTiE0U8-kZD17v1bH3vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شجاع خلیل زاده با ارزش نزدیک به ۱۰۰ هزار یورو؛ کم ارزش ترین بازیکن تیم ملی فوتبال ایران و یکی از کم ارزش ترین بازیکنان کل رقابت های جام جهانی فوتبال ۲۰۲۶ خواهد بود.
خلیل زاده همچنین با ۳۷ سال سن پیرترین بازیکن ایران و جز ۱۵ بازیکن پیر کل رقابت های جام جهانی خواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/withyashar/13421" target="_blank">📅 21:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13420">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">یکی از اعضای تیم مذاکره‌کننده ایران به خبرگزاری فارس: ما هنوز پاسخ خود به پیش‌نویس تفاهم‌نامه را به ایالات متحده ارسال نکرده‌ایم. ما وارد هیچ توافقی که لبنان را نادیده بگیرد، نخواهیم شد.
@withyashar</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/withyashar/13420" target="_blank">📅 21:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13419">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">کانال 12 اسرائیل :ایران پیامی به آمریکا فرستاد که هر حمله‌ای به بیروت منجر به شلیک ده‌ها موشک به اسرائیل خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/withyashar/13419" target="_blank">📅 21:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13418">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سخنگوی ۳پا : تخریب ترمینال مسافربری فرودگاه کویت ناشی از خطای سامانه‌های پاتریوت آمریکایی بوده است
بررسی و تحقیقات ما در مورد اصابت ترمینال مسافربری کویت نشان می‌دهد، نیروی هوافضای سپاه هیچ شلیکی به سوی این هدف نداشته است و تخریب ترمینال مسافربری فرودگاه کویت ناشی از خطای سامانه‌های پاتریوت آمریکایی بوده، که پس از شکست در رهگیری موشک‌های ایرانی بر این ترمینال فرود آمده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/withyashar/13418" target="_blank">📅 21:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13417">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwEpDqNdflGd0cNMrUQGoXCGcxCGa1fm_sWmljGFddUOy5DXa_lo4YuiCoV19NcQ-aD_-LiGSPjE7ohA5rF6nP8MWRZeoF739BFv8BFT0-SMeGbWO0MgQKlbRZWj-7AXjRxaLcWz0m_NHx53BGnwLs4KhMIaAMDwfp_7IVGFuaKlKW8r-VnfMeqHt5yNae91hPfb-sk7H779ZWM0ajo4Jy4YuxFtz9utCEvVBUICx5UxtBgXFQI6gX0z_lP1n3QrMZwq4ca-WQvILU6vLcvmCLq3UMBmiIax1TZ2L5er3Cw87EgattZLo_S26SLWkOnNC2tWa51P1QSl2IWTjpxUUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ممد امین میمندیان، نویسنده پاورقی :
شایعه تجاوز به محمدرضا شهبازی، خزعبل و شایعه است و کاملا تکذیب می‌کنم.
برنامه طبق روال در حال پخش است و امشب هم منتشر می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/withyashar/13417" target="_blank">📅 21:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13416">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">عضو تیم رسانه‌ای در تیم مذاکره‌کننده ایران: دلیل عدم موفقیت مرحله اول مذاکرات اسلام‌آباد، امتناع ایران از ورود به مذاکرات هسته‌ای بود
@withyashar</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/withyashar/13416" target="_blank">📅 21:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13415">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">نتانیاهو:
اسرائیل آماده است. نیروهای آمریکا آماده‌اند.
ایران با آتش بازی می‌کند.
@withyashar
شمام آماده اید ؟
😁</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/withyashar/13415" target="_blank">📅 20:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13414">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/withyashar/13414" target="_blank">📅 20:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13413">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">یعنی چی ؟  منظورش اینه جنگ تموم شد ؟</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/withyashar/13413" target="_blank">📅 20:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13412">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromR</strong></div>
<div class="tg-text">یعنی چی ؟
منظورش اینه جنگ تموم شد ؟</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/withyashar/13412" target="_blank">📅 20:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13411">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">مقامات اسرائیلی: تخمین زده می‌شود که اسرائیل در روزهای آینده به بیروت حمله کند
@withyashar</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/withyashar/13411" target="_blank">📅 20:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13410">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ادعای روبیو، وزیر خارجه آمریکا:
ما دیگر حملات مداومی در داخل ایران برای تضعیف ارتش آنها انجام نمی‌دهیم، زیرا جنگ «خشم حماسی» تمام شده است.
@withyashar</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/withyashar/13410" target="_blank">📅 20:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13409">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">تکذیب شد
😃
🤣
خاک دوباره پس زد</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/withyashar/13409" target="_blank">📅 20:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13408">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">غرب‌ دوباره صدا اومد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/withyashar/13408" target="_blank">📅 20:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13407">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">غرب‌ دوباره صدا اومد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/withyashar/13407" target="_blank">📅 20:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13406">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">sample : yourname.warroom</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/withyashar/13406" target="_blank">📅 20:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13405">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">یه ایده جالب دارم ویس میدم …</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/withyashar/13405" target="_blank">📅 20:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13404">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">https://www.instagram.com/reel/DZIVRzvuaUf/?comment_id=17892109731481781
به درخواست شما متن برای بانو نور هم کامنت شد</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/withyashar/13404" target="_blank">📅 20:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13403">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">صدای مشکوک به انفجار از غرب‌ تهران
🚨
@withyashar</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/withyashar/13403" target="_blank">📅 20:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13402">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اتاق جنگ با یاشار : ما الان با دو بخار مواجه هستیم، بخار هسته ای و بخار خامنه ای
@withyashar
پایان چالش رو اعلام میکنم
🙌🏾
🤣</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/withyashar/13402" target="_blank">📅 20:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13401">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">رافائل گروسی مدیرکل آژانس بین‌المللی انرژی اتمی در گفت‌وگو با شبکه اسکای‌نیوز با بیان اینکه از موقعیت مکانی ذخایر اورانیوم غنی‌شده ایران که در جنگ  سال گذشته هدف حمله قرار گرفت، مطلع است.
او ادعا کرد که این مواد همچنان در همان محل پیشین قرار دارد اما دسترسی به آن به‌دلیل خسارت‌های فیزیکی دشوار شده است.
@withyashar</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/withyashar/13401" target="_blank">📅 20:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13400">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">💩
تاریخ برگزاری آئین وداع، تشییع و خاکسپاری علی خامنه‌ای اعلام شد   ۲۰، ۲۱، ۲۲ خرداد؛ وداع در حرم امام‌ خمینی  ۲۳ خرداد؛ تشییع در تهران  ۲۴ خرداد؛ تشییع در قم  ۲۵ خرداد؛ تشییع در عراق  ۲۶ خرداد؛ تشییع و خاکسپاری در مشهد @withyashar</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/withyashar/13400" target="_blank">📅 19:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13399">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">💩
تاریخ برگزاری آئین وداع، تشییع و خاکسپاری علی خامنه‌ای اعلام شد
۲۰، ۲۱، ۲۲ خرداد؛ وداع در حرم امام‌ خمینی
۲۳ خرداد؛ تشییع در تهران
۲۴ خرداد؛ تشییع در قم
۲۵ خرداد؛ تشییع در عراق
۲۶ خرداد؛ تشییع و خاکسپاری در مشهد
@withyashar</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/withyashar/13399" target="_blank">📅 19:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13398">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e72ba1695.mp4?token=JoeiKNnpHVN1vQav2ESycveRUVtUZVWyowG9OBtBIlbH65bTBdzk9XYYDW4DUQ3ms0LJs3YvAnvjXEqAiCo4XTmKZfnp4zFsrHJ9n1G26K4PEJFL3PN0thgZURxOyjaDhJIYBV82lEhXOhsbxA3qzKO0WYlqIRnB4_fzFhtnlaYNcAOo8SS0mqn0gDhZSc8i7u_cLx6pmls6tb3yukZFf_G7MlGHhU2LvjAkKY7kwzIrT1gDBnccN40ZC4uDwdXYdAEXeSIkOTi9CaAtAMeeb0GfrxYr6Htl7oKsaJHMkQnvX87KAMvMK_E5FdEi0a37FI7tlTJXrdsORdF_y4yOOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e72ba1695.mp4?token=JoeiKNnpHVN1vQav2ESycveRUVtUZVWyowG9OBtBIlbH65bTBdzk9XYYDW4DUQ3ms0LJs3YvAnvjXEqAiCo4XTmKZfnp4zFsrHJ9n1G26K4PEJFL3PN0thgZURxOyjaDhJIYBV82lEhXOhsbxA3qzKO0WYlqIRnB4_fzFhtnlaYNcAOo8SS0mqn0gDhZSc8i7u_cLx6pmls6tb3yukZFf_G7MlGHhU2LvjAkKY7kwzIrT1gDBnccN40ZC4uDwdXYdAEXeSIkOTi9CaAtAMeeb0GfrxYr6Htl7oKsaJHMkQnvX87KAMvMK_E5FdEi0a37FI7tlTJXrdsORdF_y4yOOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر امور خارجه عباس چپقچی:
نیروهای مسلح ما در حال انجام حملات دفاعی به سایت‌هایی هستند که آمریکا اجازه استفاده از آن‌ها را برای حمله به کشتی‌رانی غیرنظامی و نقض آتش‌بس دارد.
هر عمل خصمانه‌ای با پاسخی فوری و قاطع مواجه خواهد شد. تحریم‌ها و جنگی که نتوانستند به هدف برسند، با جنگ بیشتر به دست نخواهند آمد.
@withyashar</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/withyashar/13398" target="_blank">📅 19:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13397">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">پست جدید پیج دوم شاهزاده کامنت رو گزاشتم
🙌🏾
ادامه میدیم تا جوابی بگیریم
https://www.instagram.com/p/DZILMCsFoyR/?img_index=1&igsh=ZmZzNTQ2NHMwN2x2
و این پست
https://www.instagram.com/reel/DZIOnXHRKuy/?igsh=MWkzYmpzN2pjMmgyYQ==</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/withyashar/13397" target="_blank">📅 19:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13395">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/withyashar/13395" target="_blank">📅 18:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13394">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">مجری: چرا نمی‌تواند آمریکا فقط تنگه هرمز را باز کند؟
نتانیاهو: خب، می‌توانید، اما به مالکان کشتی‌هایی نیاز دارید که ریسک مالی برخورد را بپذیرند. از نظر نظامی ممکن است، اما ساده نیست
@withyashar</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/withyashar/13394" target="_blank">📅 18:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13393">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d25386882.mp4?token=NwvzwVYa5ZGFhw-9D5VA2t3X-heY-SNmK5lACQc1Xmg3qG4SJfUDJSsh70Eom0MoufQOmpvC2qfnzn8GvAB2t57eUyeINKBDNhjHpztYR8BkA6p6lDttW24dU7WlQDj7wpO0HnJfJsJVLHfcPnZFybSJS_P2J-adohhjxj4cMuCnHwngsZU-PQtxqeYzkydP3M05Yme61oBgOBN3saKMxHGSa8Pm10EXj5LZTEj6mWNmUS746trcJB_E6LlfnP2zY5cZ1Q37_M7p4-f4dbWPfh16FsLF8XgchH5tOvQ-FD3VoYDAGeRqazxrdHJbBZTbLlHctYOmaEki5COM_1H6gldqYN7DgZdeoDfCI3XOVT82SJw8YUb0t-4jHONeZ3Xo-G3zKRBkUAkbYGX-EBazdw0DwlM-LhqIP_SXSLqeKLQAr0SxsIt_S7wd2-cnxzcT5oQY6JO5WQsYWf2Va4RqqyvkZL6N-ZW08QnbZ6OyYLeRtQkfduMeYeG3yLzYrVBCIskI0DMX1s1K-sIhc-Pb2lRDdxuVPzE4JjThtvYjJjZHWbeLcxREKnIm9619-xpX561X277KOIr53yLxVSW_g1o2b4pn6_SHOSz4NzYMymSIZO_l9TpEz2J9x1uMeJp2pUIDwSRzLC3xhsk1ZmHoHSDA9Zh-8DXnHLCJhT81Loo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d25386882.mp4?token=NwvzwVYa5ZGFhw-9D5VA2t3X-heY-SNmK5lACQc1Xmg3qG4SJfUDJSsh70Eom0MoufQOmpvC2qfnzn8GvAB2t57eUyeINKBDNhjHpztYR8BkA6p6lDttW24dU7WlQDj7wpO0HnJfJsJVLHfcPnZFybSJS_P2J-adohhjxj4cMuCnHwngsZU-PQtxqeYzkydP3M05Yme61oBgOBN3saKMxHGSa8Pm10EXj5LZTEj6mWNmUS746trcJB_E6LlfnP2zY5cZ1Q37_M7p4-f4dbWPfh16FsLF8XgchH5tOvQ-FD3VoYDAGeRqazxrdHJbBZTbLlHctYOmaEki5COM_1H6gldqYN7DgZdeoDfCI3XOVT82SJw8YUb0t-4jHONeZ3Xo-G3zKRBkUAkbYGX-EBazdw0DwlM-LhqIP_SXSLqeKLQAr0SxsIt_S7wd2-cnxzcT5oQY6JO5WQsYWf2Va4RqqyvkZL6N-ZW08QnbZ6OyYLeRtQkfduMeYeG3yLzYrVBCIskI0DMX1s1K-sIhc-Pb2lRDdxuVPzE4JjThtvYjJjZHWbeLcxREKnIm9619-xpX561X277KOIr53yLxVSW_g1o2b4pn6_SHOSz4NzYMymSIZO_l9TpEz2J9x1uMeJp2pUIDwSRzLC3xhsk1ZmHoHSDA9Zh-8DXnHLCJhT81Loo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری
: ترامپ شما را «دیوانه لعنتی» خطاب کرد.
نتانیاهو: گاهی اوقات، مانند بهترین خانواده‌ها، ما این اختلافات تاکتیکی را داریم. همیشه راهی برای حل آن‌ها پیدا می‌کنیم.
می‌توانیم صبح با هم اختلاف نظر داشته باشیم و تا بعدازظهر اقدام مشترکی انجام دهیم.
@withyashar</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/withyashar/13393" target="_blank">📅 18:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13392">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d950e42b.mp4?token=DGjAtJ0TVGO_AoP09oGWO9nPYIBkBkgBUfCxW15wK4qW4rdLuYivrzA29sWFPgBmCL43ntR1-jeIZqnXL4gAOggpSYChIQ1P6gKEO53TkF5Du2sqoMh4mRIlX03SqWQ_kfT39_hMO2yigHbMjOtdQKRn0vZgB8-rCjwJZ4JdIEn9xZZasNLyt6j9wnHusvYJ9K4Z7uhZ38QhwhKX8fY7UDwYgodiD2JlwTvA4D81T6LnghzM2LU_bhPQAky6q7rfNk5RywDacWmDyhyYcP5XhjmG3G5SoR0xpeUfjrF0OPnpheaTso9uuax1GQjgs1HGt2Rq6uCWyCRoCL71z9tMmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d950e42b.mp4?token=DGjAtJ0TVGO_AoP09oGWO9nPYIBkBkgBUfCxW15wK4qW4rdLuYivrzA29sWFPgBmCL43ntR1-jeIZqnXL4gAOggpSYChIQ1P6gKEO53TkF5Du2sqoMh4mRIlX03SqWQ_kfT39_hMO2yigHbMjOtdQKRn0vZgB8-rCjwJZ4JdIEn9xZZasNLyt6j9wnHusvYJ9K4Z7uhZ38QhwhKX8fY7UDwYgodiD2JlwTvA4D81T6LnghzM2LU_bhPQAky6q7rfNk5RywDacWmDyhyYcP5XhjmG3G5SoR0xpeUfjrF0OPnpheaTso9uuax1GQjgs1HGt2Rq6uCWyCRoCL71z9tMmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: مردم ایران خواهان روابط خوب با آمریکا هستند و خواهان روابط خوب با اسرائیل. این می‌تواند اتفاق بیفتد.
@withyashar</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/withyashar/13392" target="_blank">📅 18:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13391">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">مجری : شما درباره تغییر رژیم صحبت می‌کردید. چرا الان هیچ‌کس درباره آن صحبت نمی‌کند؟
بی بی : چرا این را می‌گویید؟
مجری: به نظر می‌رسد ترامپ آماده است با این رژیم فعلی معامله کند.
بی بی : این به این معنا نیست که او می‌خواهد این رژیم فعلی باقی بماند.
ما باید به مردم ایران کمک کنیم تا این رژیم را سرنگون کنند و این تغییر نکرده است.
اما این اتفاق دقیقاً در لحظه‌ای که ما بخواهیم رخ نخواهد داد.
@withyashar</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/withyashar/13391" target="_blank">📅 18:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13390">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نتانیاهو به ان‌بی‌سی: وضعیت در ایران تمام نشده، اما ضعیف شده است. ما و آمریکایی‌ها آماده‌ایم در صورت لزوم اقدام کنیم.
اگر تشدید تنش لازم باشد، آن را به ترامپ واگذار می‌کنیم و باز کردن تنگه هرمز از طریق نظامی امکان‌پذیر است.
ترامپ در حال بررسی چندین گزینه است و ما هر دو روز یکبار با هم صحبت می‌کنیم.
ایران هنوز با حذف مواد هسته‌ای موافقت نکرده است، اما فشار فزاینده‌ای وجود دارد.
@withyashar</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/withyashar/13390" target="_blank">📅 18:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13389">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">روبیو: سکوهای پرتاب موشک ایران آسیب شدیدی دیده‌اند که منجر به زوال قابل توجه قابلیت‌های آنها شده است.
ما می‌خواهیم شاهد تغییر در ایران و حکومت مردم بر آن باشیم و دیگر تهدیدی برای منطقه نباشد.
امیدواریم که ایران جاه‌طلبی‌های هسته‌ای خود را کنار بگذارد و حمایت از تروریسم در سراسر جهان را متوقف کند.
«عملیات خشم حماسی» به هدف خود یعنی شکستن سپر سنتی ایران و کشاندن آن به پای میز مذاکره دست یافته است.
@withyashar</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/withyashar/13389" target="_blank">📅 18:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13388">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">روبیو: امیدواریم امروز بین اسرائیل و لبنان توافق صورت گیرد
وزیر امور خارجه ایالات متحده:
رهبران دولت‌های لبنان و اسرائیل در حال حاضر در مقر وزارتخانه ما برای مذاکره دیدار می‌کنند.
ما امیدواریم که جلسه امروز بین لبنان و اسرائیل به بیانیه و برنامه عملی برای مسیر امنیتی لبنان مستقل از حزب‌الله منجر شود.
@withyashar</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/withyashar/13388" target="_blank">📅 17:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13387">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fx7zGWsN7Yzq5huTCjVKZm6Zm5N5UqWusi23GaBnL3Rlwbf0qpfCetiCAZ-v7AUnbnHxlYNyZmPPtqIiZDCEKuGslc4NNQMyD4UsCvMIt9m7I6cUQj9_jd6pGGVkr9BMDQQapngjEAzIWJvye-IQbKJBrB4E3CEhLY-FjKLuR2BX0TK-kqAPOHQaLDtzAQhIBznzmd7KZ1fYbqFVOMnphPvvrFeXmb-tx_xUUR_SGzwAXPqMjr7tfg3t2z397xCA_hczad6SpXiFA5uK6p72Q6MVd7LV9f34u3Zqkz0FKTI1W4wbCkY8FtjVNiXT4N1mFoQPHBmMnBZdjFri9p2S0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تانکر ترکرز: یک ابرتانکر VLCC برای اولین بار در چهار هفته اخیر، نفت خام را در جزیره خارک ایران بارگیری می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/withyashar/13387" target="_blank">📅 17:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13386">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">وکیل شخصی نتانیاهو، مایکل رابلو، به عنوان بازرس کل دولت اسرائیل انتخاب شد.
@withyashar</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/withyashar/13386" target="_blank">📅 17:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13385">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">کویت در پاسخ حمله جمهوری اسلامی ، دو دیپلمات را عنصر نامطلوب اعلام و اخراج کرد.
@withyashar</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/withyashar/13385" target="_blank">📅 17:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13384">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ارتش کویت: ما 13 موشک بالستیک و 17 پهپاد رو شناسایی کردیم.
یک فرد هندی جان باخت و شماری از افراد زخمی شدن، همچنین خسارات مادی سنگینی وارد شده.
به دلیل حملات، امروز 5 بار آژیرهای خطر به صدا در اومدن.
@withyashar</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/withyashar/13384" target="_blank">📅 16:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13383">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">️بیانیه نیروی دریایی ایران:
فقط مسیر تعیین‌شده ایران برای تردد امن در خلیج فارس است / شناورهای متخلف هدف قرار می‌گیرند
@withyashar</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/withyashar/13383" target="_blank">📅 15:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13382">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ : ما خیلی خوب با هم کار کردیم. من «بی‌بی» رو خیلی دوست دارم و همکاری خیلی خوبی باهاش داشتم
می‌دونی، ما تو شرایطی بودیم که اون نخست‌وزیر زمان جنگه و من هم رئیس‌جمهور زمان جنگ هستم
ولی در کل رابطه خیلی خوبی دارم. با هم خوب کار کردیم، نتیجه هم گرفته شده
همیشه هم همین‌طوره. بدون آمریکا اصلاً نمی‌شد انجامش داد، همه اینو می‌دونن. ولی ما تونستیم
@withyashar</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/13382" target="_blank">📅 15:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13381">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PebnkRN28McbYk0N8Dq0ng-AV4KIwH74eC1PKUHHAG-EUFTkvwBPlyuahKnRPKWJnKmb3wbgXb1SLvpmvBg44P-efgRe9rX3aoOZEvW9TPmTN3Z3-QJ1AEntiZ60A6qBqx5q_W-GFYZwHY0HJDNOyyQi3RangMQbcUwWv-tJXxUWDiQ5mAht5Qt3qOvW9qcfKTKVdiIGYr6Hclfcxraa8GOofsq2ehi6___S-N_DXtFcUnClEgWDGwiN5VizzBmM5haZUqGAlnz6W5JCyiDqmP96eXVUFNNmmHFE4JIW3zYamiQI1JyIuNG8KwIJcDvzoIc8pY3A_Z334unxzglKoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در پست جدیدی در تروث با تلقین حس مخفی‌کاری و چند چهره بودن در قالب جیمز باند مأمور مخفی شکست ناپزیر ظاهر شده
@withyashar</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/13381" target="_blank">📅 14:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13380">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYVrutj9E36pMSSJUJPfJy4DqGbtG4-VYK1X_vkVL9XwcXDa5m23FU1VqXv81QiHCo-Sb3Jc4II_C8ffcF2lQ8NYJ0QOYAdqHT8nZr2LqeLWmSa3icsVgP3qTLW1RcX6qUl-TwIThVbF6wiM6M4YaopeItAPD0xyk34xML8y4duB5ZwXxo6B7inA3OzkxS7vFmzR5QzHLC-p6bH0xghn7wZ6uGL9-9W2iqvpQjpEJaj8g2iJ5YEpGZ_5SW69lPCXEcj6nMJ7pInbquG2pTRag-TfSYSLoYkLHYLaR0I27jY8vD2FQidvbLWmnT5Xb2jsJmIRlyi0k19q6IOCshRrzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین الان تحرکات سنگین دارن
جهیزیه را میارن
🎉
@withyashar</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/13380" target="_blank">📅 14:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13379">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ دربارهٔ سال ۲۰۲۸:  من هر دو نفر، جی‌دی ونس و مارکو روبیو را دوست دارم. دوست دارم که با هم باشند. جی‌دی و مارکو تیم فوق‌العاده‌ای خواهند بود. هر دو بسیار با استعداد هستند. @withyashar</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/withyashar/13379" target="_blank">📅 14:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13378">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامپ دربارهٔ سال ۲۰۲۸:
من هر دو نفر، جی‌دی ونس و مارکو روبیو را دوست دارم.
دوست دارم که با هم باشند. جی‌دی و مارکو تیم فوق‌العاده‌ای خواهند بود.
هر دو بسیار با استعداد هستند.
@withyashar</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/13378" target="_blank">📅 14:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13377">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترامپ درباره ایران:
ما نیازی به حضور نیروهای زمینی نداریم. با بمباران، بخش زیادی از نیروی نظامی آن‌ها را نابود کردیم.
آنها نه نیرو دریایی دارند و نه نیروی هوایی همچنین سرباز‌ زیادی هم ندارند
@withyashar</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/13377" target="_blank">📅 14:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13376">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ایالات متحده به تازگی یک جزیره کلیدی ایران را بمباران کرد.
این یک تشدید تنش بزرگ است.
کینگ ترامپ با ملاها بازی نمی‌کند و آنها دارند متوجه می‌شوند.
اوضاع به سرعت در حال وخیم شدن است.
@withyashar</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/withyashar/13376" target="_blank">📅 14:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13375">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامپ : گروه‌های مختلفی از آدم‌ها هستن؛ گروه اول دیگه نیست، گروه دوم هم نیست، بخشی از گروه سوم هم حذف شده
و اون آدم‌هایی که الان باهاشون طرف هستیم، همونایی هستن که الان کشور رو هدایت می‌کنن
@withyashar</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/withyashar/13375" target="_blank">📅 14:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13374">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ: اگر من نبودم، الان اسرائیلی هم وجود نداشت.
@withyashar</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/withyashar/13374" target="_blank">📅 14:06 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13373">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ:
هر کسی که من حمایت می‌کنم برنده می‌شود. منظورم این است، همه. هفته گذشته دیدی، درست است؟
هر فردی که من حمایت می‌کنم برنده می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/withyashar/13373" target="_blank">📅 14:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13372">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ:
می‌توانم پاسخی بدهم و سپس، ۲۰ دقیقه بعد، وارد دفتر بیضی‌شکل شوم و متوجه شوم پاسخم اکنون نادرست است.
می‌دانی، تغییر می‌کند. حقایق تغییر می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/withyashar/13372" target="_blank">📅 14:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13371">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ درباره اینکه آیا نتانیاهو او را برای جنگ با ایران فریب داده است:
یعنی من کسی هستم که این را شروع کردم.
نمی‌خواهم کسی را خسته کنم، اما من شروع‌کننده بودم چون نمی‌توانیم اجازه دهیم آنها سلاح هسته‌ای داشته باشند.
اگر من نبودم، اسرائیل هم وجود نداشت.
@withyashar</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/withyashar/13371" target="_blank">📅 14:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13370">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ: به نتانیاهو گفتم او کاملاً دیوانه است، چون از درگیری او با لبنان نگران بودم.
من رابطه خوبی با نتانیاهو دارم
@withyashar</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/withyashar/13370" target="_blank">📅 13:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13369">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">وزارت امور خارجه کویت : حمله ایران به فرودگاه کویت یک کشته و چند زخمی در بر داشته !
@withyashar</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/withyashar/13369" target="_blank">📅 13:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13368">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">صدای انفجار در‌ قشم
🚨
@withyashar</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/withyashar/13368" target="_blank">📅 13:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13367">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ تعریف میکنه نشونه زدنه
😁
🚨
@withyashar</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/withyashar/13367" target="_blank">📅 13:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13366">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ در پادکست :
: احتمالاً تا روز کارگر (Labor Day) بتونیم محاصره ایران رو برداریم
هیچ‌وقت به دیدار با هیچ‌یک از مقام‌های ایرانی فکر نکرده‌ام
آیت‌الله ایران تو مذاکرات با آمریکا نقش داره و تو جریان گفت‌وگوهاست.
احتمالاً یه زمانی با آیت‌الله ایران دیدار خواهم کرد
قیمت بنزین به زودی کاهش می‌یابد
وضعیت ایران خیلی سریع داره تغییر می‌کنه، و در نهایت اوضاع خیلی خوب پیش می‌ره
@withyashar</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/withyashar/13366" target="_blank">📅 13:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13365">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ: ایران موافقت کرده است که سلاح هسته‌ای نداشته باشد.
@withyashar</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/withyashar/13365" target="_blank">📅 13:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13364">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">صدای انفجار بندر عباس (گفته بودن ۳ روز مهمات عمل نکرده است که دیروز روز سوم بود )
@withyashar</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/withyashar/13364" target="_blank">📅 13:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13363">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5bPAkAcJmKq4vjNP9NR25msB0Uf77sCpVtAXMNWTT3JwhJtqZ6TWdFxGp_dFh083iPUm_n3ZEL-GP5-kPlXTRWq6gulUoCl5s2vs7s7zPbgnnc66TM1R0rsn_P3ZrDjyCt4wBEGlNhEZK3mrzad53NCVmcif0dujkM2SHlsTUga9f5vGlAtVDQ_WRxeatZzsjtMyQ2q5DfMwgD2nT71om6UHnpL_4yWUhuL72NA6kkg-awuZBUbRN8pcTBLWIM2bK1VROofYv75FoNyRh_gJAkP46bxXQTDjnadgaDE7dBD0ElRDr9IfjoMy1BuOJSV9-7g8PEzQhVZ5__wSndhNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ماهواره‌ای مربوط به دیروز ، آخرین موقعیت ناو هواپیمابر آبی خاکی یو‌اس‌اس تریپولی (LHA 7) را نشان می‌دهد که بسیار جلو و در نزدیکی رأس الحد عمان آمده!!!
🚨
@withyashar</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/withyashar/13363" target="_blank">📅 13:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13362">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b108e3f2b1.mp4?token=DxiqW8LJgnVtpCUZ8SFWX5uuM28BsQ1MM1EhIpdxpqkOxwkJZGPaS0j-wDERXlCkAviiaqmN7Me_cmOTCDbMzRqrVY2QZt2GisF87fzU8vd0XHufP3IY9HgPNdcQEQR4WW0xy-qac2QllO-HVXzn1lO8Db57cJ3GAhUjHMwb4TMPvw4FP1_4JcOx9dBwM6Kl0zP0u6X1Vla4-B8Wcl3FJXqfNEQhqYPRiaN4JivWGX9qVtcnGJQA3WgqpD1rckvwm7lF_RJrD001T8aJFcS5SV36HDrsoaw4iGFxfzU2MIaXlldHaXXmYGt02RqdJjCjaXjn8fWoKfSWrPQYqijx0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b108e3f2b1.mp4?token=DxiqW8LJgnVtpCUZ8SFWX5uuM28BsQ1MM1EhIpdxpqkOxwkJZGPaS0j-wDERXlCkAviiaqmN7Me_cmOTCDbMzRqrVY2QZt2GisF87fzU8vd0XHufP3IY9HgPNdcQEQR4WW0xy-qac2QllO-HVXzn1lO8Db57cJ3GAhUjHMwb4TMPvw4FP1_4JcOx9dBwM6Kl0zP0u6X1Vla4-B8Wcl3FJXqfNEQhqYPRiaN4JivWGX9qVtcnGJQA3WgqpD1rckvwm7lF_RJrD001T8aJFcS5SV36HDrsoaw4iGFxfzU2MIaXlldHaXXmYGt02RqdJjCjaXjn8fWoKfSWrPQYqijx0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همکنون فرودگاه بین المللی کویت
@withyashar</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/withyashar/13362" target="_blank">📅 13:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13361">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دیروز، مدیرعامل شرکت هواپیمایی کویت ایرویز از سرگیری فعالیت فرودگاه بین‌المللی کویت خبر داد و تصاویری از کارمندان فرودگاه در حال انجام آخرین مراحل بازگشت به ظرفیت کامل آن منتشر کرد ولی
لحظاتی پیش، شرکت هواپیمایی کویت ایرویز از به تعویق افتادن فعالیت‌های عملیاتی خود تا اطلاع ثانوی خبر داد.
@withyashar</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/withyashar/13361" target="_blank">📅 13:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13360">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16168fdf19.mp4?token=KnFh4qBOTN0A0mMhE1yRELoLyYzdowiCyGHO23aEjHUbIvRClVd5kkevS8LK4dwH9IsJEHz2In0yJfRHo8co0jUd_BttyZobMCKhyI8hGWUlbeN5qQt9T5ziXcGPFkS7jEOFryITDyjScoLSeTpIsla4V7dSxL_CpJmdmhOOUnTtPcIs495HWQ4VXLH8JrOd3OW-Z7M43MqmSHIHJbfmnEO4qrKxgtgoGnV6yuIoGyAiH8Ny-nnpsDdYgI8CjZP9F41S_kb6TVPFGJk_NhiVZ-51n4nbyTLbV75RKQJXFW5JGfL-q3Zci9Xsr1HtiXQyC9yK2-vFUwVt4CqvdZ0eZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16168fdf19.mp4?token=KnFh4qBOTN0A0mMhE1yRELoLyYzdowiCyGHO23aEjHUbIvRClVd5kkevS8LK4dwH9IsJEHz2In0yJfRHo8co0jUd_BttyZobMCKhyI8hGWUlbeN5qQt9T5ziXcGPFkS7jEOFryITDyjScoLSeTpIsla4V7dSxL_CpJmdmhOOUnTtPcIs495HWQ4VXLH8JrOd3OW-Z7M43MqmSHIHJbfmnEO4qrKxgtgoGnV6yuIoGyAiH8Ny-nnpsDdYgI8CjZP9F41S_kb6TVPFGJk_NhiVZ-51n4nbyTLbV75RKQJXFW5JGfL-q3Zci9Xsr1HtiXQyC9yK2-vFUwVt4CqvdZ0eZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت پس از حمله رژیم جمهوری اسلامی
@withyashar</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/withyashar/13360" target="_blank">📅 12:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13359">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ادعای ای‌بی‌سی به نقل از مقامات آمریکایی: ترامپ، از تهران می‌خواهد که امتیازات مشخص هسته‌ای را به صورت مکتوب به عنوان بخشی از یک توافق مقدماتی ارائه دهد
تا بتوان بر بن‌بست طولانی میان آمریکا و ایران غلبه کرد.
ایران در حال بررسی شرایط به‌روز شده است و مذاکره‌کنندگانش نشان نداده‌اند که آیا تهران این شرایط را می‌پذیرد یا خیر
@withyashar</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/withyashar/13359" target="_blank">📅 12:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13356">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from₃₆₄</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_k1j1V3oU9SJpAiZNiQzYSwpUl091Behczw8V25C-sH2Ghic3i8qof9kvkK6XYVrUDaSuqAN7MFg2zIci5EBg3Ku_-B-XMO5n4DWQ7nD5mEox84HaRBtYh_yHJA5XkAW54jE4FcO1amewIqNiCtln8MMLrA70yRDrkA3891mC1MQfLiw6qPLD-7xqrq545CMolKxNaqOcB7narLX1Z9cPnM_EeraU1IuV0yx2Oj55eEbxVfgO9BYyQECkQC59cfQi02LyPtpT1ZsI9Q4HuFnRKNAt-E5RT2ZAcYXgpy4e91hGqLFZ6gkCwwvD64jmuMH6_DitdzuvRhZquVce67VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا یاشار مهربان</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/withyashar/13356" target="_blank">📅 12:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13355">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/13355" target="_blank">📅 12:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13354">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🍁┅┅✿❀𝒩𝒾𝓃𝒶❀✿┅┅🍁</strong></div>
<div class="tg-text">درود آقا یاشار مهربان
تحلیل هاتون خیلی جالبه
جوری توضیح میدید که درکش برای همه راحت باشه
سپاس از شما
🙏
🌹
😊</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/withyashar/13354" target="_blank">📅 12:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13353">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">خبرهای تایید نشده از اینکه که سه نفر از وطن پرست ها مجری محمدرضا شهبازی رو گیر میارن و بهش تجاوز میکنن  به همین دلیل هم برنامه پاورقی فعلا متوقف شده @withyashar</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/13353" target="_blank">📅 12:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13352">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/13352" target="_blank">📅 11:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13351">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03f509353.mp4?token=B1h2It4dnSadxTp79Fh2tpX2fzrRB98d212y-MDtW3DmsdeZQbiSirgy3lzf9Ft7CxvWvIVP1Puc2jXZ7LAirgL7UgjL69bOrgBIVdVslphS47WaFPW4w1agSEqWYv62UJTpN6HCF60ni_x4BHBv_Jnf7PB6-NzQ8w3ug40wKJ9P5jjHCbt4K91MLmGeVm7BnIuUePSR8QOcP0P5KJRI6uB03_TeN74E9UxE8BKSsoaZqP4bDwl7FBVRyWX76-0sJRtyxjIFda6pn9rkH434Bfoqkl-VhITrt41WmRjLW3ws7gOJtEujA85DsnDIQibhUM3POXB5oJ3Mfxxi48JzCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03f509353.mp4?token=B1h2It4dnSadxTp79Fh2tpX2fzrRB98d212y-MDtW3DmsdeZQbiSirgy3lzf9Ft7CxvWvIVP1Puc2jXZ7LAirgL7UgjL69bOrgBIVdVslphS47WaFPW4w1agSEqWYv62UJTpN6HCF60ni_x4BHBv_Jnf7PB6-NzQ8w3ug40wKJ9P5jjHCbt4K91MLmGeVm7BnIuUePSR8QOcP0P5KJRI6uB03_TeN74E9UxE8BKSsoaZqP4bDwl7FBVRyWX76-0sJRtyxjIFda6pn9rkH434Bfoqkl-VhITrt41WmRjLW3ws7gOJtEujA85DsnDIQibhUM3POXB5oJ3Mfxxi48JzCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/13351" target="_blank">📅 11:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13350">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromToranj</strong></div>
<div class="tg-text">درود یاشار عزیز ، چرا حملات اخیر جمهوری اسلامی به کشور های منطقه نقض آتش بس نیست ؟ و واکنشی خاصی از امریکا و اسرائیل دیده نمیشه ؟</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/withyashar/13350" target="_blank">📅 11:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13347">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q_m0_bFAVVSJfcl1QbiY_uZUnY9sVo3HMfe2PHU3CvvsPEPHldInxufsr1e_UmvYDW3mcD5mLoakSzzv_X7NsyOvo5OW62V4jBh8dr5cgJHtUVKoqzkE-qc9Guxzb4aCGUtNrh6s9dVDnKWqZxU-xcSczLUlHz7i5-PtHyCnZrFU468rKxG_FZfBjMhI7UNjpING0UGiB_pEOKSLAzl6MY6BdRutk2mGWOXvvWdMg9-h7-ODVSkqtdJl6ONmx8hBvLw2R4we1ZzU3VJwFSyw18LXMREOIodNbv_unUeByGO9QAyFD_MZ6AT8tedPWig1DsgU_YCYDm71bbgGekZi2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EGpaFaGPVJYNjPtLPSOU0HaCKNu8ed-BfYiGfHBwY_N1njZjfVBM6RdTjtQxY6pGFjT255dYAMrjrLiZXIoPTG4CVcEHBiARwdc2awK6zneHwdGsEKp9hgi_sv01P_eMExhFRxYuMEixvIMx14-SFq-_Vj2N3DiNI1r58YlWc5nmhTAYfRFNMUdxqUDykgG_KpwMh6AcRblaAjaChye6PwmQRYUCCP2IjE9fnP_kXwNjnXrv_bCW3_ueEKTdP_7w5FFTT7PeiMUkafTaUrW9TCI7PLNUVka_TY6ICOlZSNxG_GIlvqgrGvppSyqiOKH7XmUpl1Upki-nZrgeqEpCZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VOqM7yI3gewlaXpsYN8fpFrwWFxmETsEaE5K6LTK5CY7-dbycFjQDEoZQF6swG47J-nZkf2bgvnxdgzEpjHMTc7PrGVedlnZoL3BNcYdtm5emS6tcLRzpQCQDibrK8Aj0W5VfPv1QxZmV-EU41kaIFH9gIjQeKC-6qi-FQWt1cZqJ2Ql3tVYrogYIuhUMlRVHiyN8iEmqCP5a6W5R4XZAcSJ0NUskZ0E5jsziRK9saFDbKl0kWbRyOFt9Nco2knP38WrgWg57Mb1GI8R5lgLO49Mi9MYvE98oyEE4P-bz9nMKVb-r6MifjPE6Gg9XV8b2bUws3Z59oAP_CLlAhsY0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همکنون وضعیت فرودگاه کویت
@withyashar</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/withyashar/13347" target="_blank">📅 11:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13346">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mN5Gtt-FJvfhWLTWI7oqrlUeNVZdpZi8Tr445Qgu8D5fyr2SCHK3gsujITb9Dj5BFelj6gIXa6RJxAmc9PBgs9mf5HhLfAf8Lz_IfUtY-u9cK4g53VlttDv6J3kvHSu_V4vFsWA1nEOOQ6S5hvLV4WbS76hehpGW-If1lB2uKnBK3B5uGnV8jIH_gQCuAWWWXq0B9Kgq0B-zbAxO3Z5o7dyR85HUcm1VnTSBexhRKqMTSYIvFB_ZNhL3EEosfnAm5CBPdgPaNtgc8eFcLwkDIkGssBm7UytZmk6q2zwyJc5O8l8hYOM0Ao1igPhe26bcHvApQcRMvhGKgYL98bgfgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با شما : مشاهده شدن سه ستون دود غیر معمول سمت آزادراه تهران پردیس
@withyashar</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/13346" target="_blank">📅 10:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13345">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">خبرهای تایید نشده از اینکه که سه نفر از وطن پرست ها مجری محمدرضا شهبازی رو گیر میارن و بهش تجاوز میکنن
به همین دلیل هم برنامه پاورقی فعلا متوقف شده
@withyashar</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/13345" target="_blank">📅 10:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13344">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">نایب رئیس مجلس: موشک‌هایی که به بیت اصابت کرد تنها چند کروز بود نه سنگرشکن
@withyashar</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/13344" target="_blank">📅 10:46 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
